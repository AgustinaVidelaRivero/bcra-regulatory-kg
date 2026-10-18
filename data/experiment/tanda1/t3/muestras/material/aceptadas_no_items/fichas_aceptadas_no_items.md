# Material de T4 — aceptadas:no_items (30 fichas; B6.1, tanda 1, T3, punto 7.5)

Sorteo: `aceptadas_no_items.json` (41d2f3ea…, 2026-10-18T10:09:26-03:00); material armado a las 2026-10-18T10:12:10-03:00. Sin el estado de E3 ni las marcas de E3.

## 1. `ri_mmsef::2.5.11` — RI:sin_raiz · aceptadas:no_items

Texto que vio E3 (e0, bloque de lista True; págs. 9):

```
[encabezado | punto S2]
2. Instrucciones particulares.
[encabezado | punto 2.5]
2.5. Sistema de monitoreo remoto:
[texto propio | punto 2.5.11]
2.5.11. Blindaje (revestimiento).
```

Versión: final (grafo sin cola). Nodos 2, aristas 1.
- **N1** Definicion `Definicion_blindaje_revestimiento__medida_de_seguridad_de_sistemas_de_monitoreo_remoto_que__b1f742` — Blindaje (revestimiento) · {"termino": "Blindaje (revestimiento)", "descripcion": "Medida de seguridad de sistemas de monitoreo remoto que consiste en el revestimiento o blindaje de la infraestructura."} · tramo: Blindaje (revestimiento)
- **N2** TextoOrdenado `TextoOrdenado_ri_mmsef_pdf` — Régimen Informativo Medidas Mínimas Seguridad · {"archivo": "ri_mmsef.pdf", "materia": "RI Cont. Mensual - Medidas mínimas de seguridad en entidades financieras", "version": "Comunicación A 6623 (vigencia 05/01/2019)"} · tramo: 
- **E1** (estructural) N1 —establecida_en→ N2 · {}

## 2. `ri_mmsef::2.1.1` — RI:sin_raiz · aceptadas:no_items

Texto que vio E3 (e0, bloque de lista True; págs. 2):

```
[encabezado | punto S2]
2. Instrucciones particulares.
[encabezado | punto 2.1]
2.1. Datos identificatorios de las unidades de servicios.
[texto propio | punto 2.1.1]
2.1.1. Tipo de unidad de servicio.
```

Versión: final (grafo sin cola). Nodos 1, aristas 0.
- **N1** TextoOrdenado `TextoOrdenado_ri_mmsef_pdf` — Régimen Informativo Medidas Mínimas Seguridad · {"archivo": "ri_mmsef.pdf", "materia": "RI Cont. Mensual - Medidas mínimas de seguridad en entidades financieras", "version": "Comunicación A 6623 (vigencia 05/01/2019)"} · tramo: 

## 3. `ri_ccna::D1A1::S7` — RI:sin_raiz · aceptadas:no_items

Texto que vio E3 (e0, bloque de lista True; págs. 8):

```
[encabezado | punto D1A1]
ANEXO I
[texto propio | punto D1A1::S7]
7. Controles a cargo de la Superintendencia de Entidades Financieras y Cambiarias.
La Superintendencia de Entidades Financieras y Cambiarias verificará periódicamente el
cumplimiento, por parte de los auditores externos de las Cajas de crédito, de las Normas
mínimas sobre auditorías externas.
A tales efectos podrá requerir que el auditor externo comparezca ante esta Institución el día y
la hora en que formalmente se lo cite, a efectos de presentar los papeles de trabajo que
respalden sus informes y brindar las ampliaciones y aclaraciones que se estimen necesarias.
El profesional interviniente conservará siempre en su poder sus papeles de trabajo, como
evidencia de la tarea realizada, durante 6 (seis) años como mínimo.
```

Versión: final (grafo sin cola). Nodos 6, aristas 7.
- **N1** Obligacion `Obligacion_el_auditor_externo_debe_conservar_en_su_poder_los_papeles_de_trabajo_como_eviden_0fa29d` — Conservación de papeles de trabajo — 6 años mínimo · {"tipo": "otra", "descripcion": "El auditor externo debe conservar en su poder los papeles de trabajo como evidencia de la tarea realizada durante un mínimo de 6 años.", "umbrales": [{"tramo": "durante 6 (seis) años como mínimo", "valor": "6", "unidad": "anios", "comparacion": "minimo_inclusivo", "regla_comparacion": "compuesta:como_minimo", "origen": "e1", "tramo_verificado": "exacta"}]} · tramo: El profesional interviniente conservará siempre en su poder sus papeles de trabajo, como evidencia de la tarea realizada, durante 6 (seis) años como mínimo.
- **N2** Obligacion `Obligacion_la_superintendencia_verificara_periodicamente_que_los_auditores_externos_de_las__20993e` — Verificación periódica de cumplimiento de normas mínimas · {"tipo": "reporte_al_supervisor", "descripcion": "La Superintendencia verificará periódicamente que los auditores externos de las Cajas de crédito cumplan con las Normas mínimas sobre auditorías externas."} · tramo: La Superintendencia de Entidades Financieras y Cambiarias verificará periódicamente el cumplimiento, por parte de los auditores externos de las Cajas de crédito, de las Normas mínimas sobre auditorías externas.
- **N3** Potestad `Potestad_requerimiento_de_comparecencia_del_auditor_externo__la_superintendencia_podra_re_2a00c9` — Requerimiento de comparecencia del auditor externo · {"descripcion": "La Superintendencia podrá requerir que el auditor externo comparezca ante ella en el día y hora que se lo cite, para presentar los papeles de trabajo que respalden sus informes y brindar ampliaciones y aclaraciones necesarias."} · tramo: A tales efectos podrá requerir que el auditor externo comparezca ante esta Institución el día y la hora en que formalmente se lo cite, a efectos de presentar los papeles de trabajo que respalden sus informes y brindar las ampliaciones y aclaraciones que se estimen necesarias.
- **N4** Sujeto `Sujeto_propuesto_el_profesional_interviniente` — El profesional interviniente · {"nivel": "propuesto", "cuarentena": "true", "padre_sugerido": "Sujeto_sujeto_regulado"} · tramo: 
- **N5** Sujeto `Sujeto_sefyc` — SEFyC (Superintendencia de Entidades Financieras y Cambiarias) · {"nivel": "instancia", "alias": ["Superintendencia de Entidades Financieras y Cambiarias"], "instancia_de": "Sujeto_organismo_publico", "parte_de": "Sujeto_bcra"} · tramo: 
- **N6** TextoOrdenado `TextoOrdenado_ri_ccna_pdf` — Régimen de Información Contable · {"archivo": "ri_ccna.pdf", "materia": "RI para Cajas de Crédito - Normas de Auditoría", "version": "Comunicación A 4523 (vigencia 06/04/2006)"} · tramo: 
- **A1** (extraccion) N1 —aplica_a→ N4 · {}
- **E1** (estructural) N1 —establecida_en→ N6 · {}
- **A2** (extraccion) N2 —aplica_a→ N5 · {}
- **E2** (estructural) N2 —establecida_en→ N6 · {}
- **A3** (extraccion) N3 —aplica_a→ N5 · {}
- **E3** (estructural) N3 —establecida_en→ N6 · {}
- **C1** (catalogo_sujetos) N4 —padre_sugerido→ Sujeto_sujeto_regulado · {"flag": "padre_sugerido_no_laudado"}

## 4. `ri_ccna::D1A3L2::S33` — RI:sin_raiz · aceptadas:no_items

Texto que vio E3 (e0, bloque de lista True; págs. 20):

```
[encabezado | punto D1A3]
ANEXO III
[encabezado | punto D1A3L2]
B. PRUEBAS SUSTANTIVAS
[texto propio | punto D1A3L2::S33]
33. Evaluar la razonabilidad de la cobertura de seguros de la entidad (incendio,
dinero en caja y en tránsito, fidelidad de empleados, etc.)
```

Versión: final (grafo sin cola). Nodos 3, aristas 2.
- **N1** Obligacion `Obligacion_evaluar_la_razonabilidad_de_la_cobertura_de_seguros_de_la_entidad_incluyendo_seg_985685` — Evaluar razonabilidad cobertura de seguros · {"descripcion": "Evaluar la razonabilidad de la cobertura de seguros de la entidad, incluyendo seguros de incendio, dinero en caja y en tránsito, y fidelidad de empleados", "tipo": "otra"} · tramo: Evaluar la razonabilidad de la cobertura de seguros de la entidad (incendio, dinero en caja y en tránsito, fidelidad de empleados, etc.)
- **N2** Sujeto `Sujeto_caja_de_credito` — Cajas de crédito · {"nivel": "clase"} · tramo: 
- **N3** TextoOrdenado `TextoOrdenado_ri_ccna_pdf` — Régimen de Información Contable · {"archivo": "ri_ccna.pdf", "materia": "RI para Cajas de Crédito - Normas de Auditoría", "version": "Comunicación A 4523 (vigencia 06/04/2006)"} · tramo: 
- **A1** (extraccion) N1 —aplica_a→ N2 · {}
- **E1** (estructural) N1 —establecida_en→ N3 · {}

## 5. `ri_mmsef::2.4.5` — RI:sin_raiz · aceptadas:no_items

Texto que vio E3 (e0, bloque de lista True; págs. 8):

```
[encabezado | punto S2]
2. Instrucciones particulares.
[encabezado | punto 2.4]
2.4. Medidas de seguridad en terminales automáticas.
[texto propio | punto 2.4.5]
2.4.5. Sistema de entintado de billetes.
```

Versión: final (grafo sin cola). Nodos 1, aristas 0.
- **N1** TextoOrdenado `TextoOrdenado_ri_mmsef_pdf` — Régimen Informativo Medidas Mínimas Seguridad · {"archivo": "ri_mmsef.pdf", "materia": "RI Cont. Mensual - Medidas mínimas de seguridad en entidades financieras", "version": "Comunicación A 6623 (vigencia 05/01/2019)"} · tramo: 

## 6. `ri_mmsef::2.2.8.2.3` — RI:sin_raiz · aceptadas:no_items

Texto que vio E3 (e0, bloque de lista True; págs. 4):

```
[encabezado | punto S2]
2. Instrucciones particulares.
[encabezado | punto 2.2]
2.2. Cumplimiento de las medidas mínimas de seguridad.
[encabezado | punto 2.2.8]
2.2.8. Medidas de seguridad para atesoramiento de numerario.
[encabezado | punto 2.2.8.2]
2.2.8.2. Caja tesoro móvil:
[texto propio | punto 2.2.8.2.3]
2.2.8.2.3. Puertas (Cerraduras).
```

Versión: final (grafo sin cola). Nodos 1, aristas 0.
- **N1** TextoOrdenado `TextoOrdenado_ri_mmsef_pdf` — Régimen Informativo Medidas Mínimas Seguridad · {"archivo": "ri_mmsef.pdf", "materia": "RI Cont. Mensual - Medidas mínimas de seguridad en entidades financieras", "version": "Comunicación A 6623 (vigencia 05/01/2019)"} · tramo: 

## 7. `ri_ccna::D1A1::4.1` — RI:sin_raiz · aceptadas:no_items

Texto que vio E3 (e0, bloque de lista True; págs. 5):

```
[encabezado | punto D1A1]
ANEXO I
[encabezado | punto D1A1::S4]
4. Registro de Asociaciones de Profesionales Universitarios.
[texto propio | punto D1A1::4.1]
4.1. Inscripción.
Las asociaciones de profesionales universitarios, cuyos socios cumplan funciones de
auditoría externa en Cajas de crédito dejando constancia en sus informes de tal carácter,
deberán inscribirse en el Registro de Asociaciones de Profesionales Universitarios
habilitado en la Superintendencia de Entidades Financieras y Cambiarias.
Para cumplimentar este trámite presentará la solicitud de inscripción con la nómina
completa de todos los socios, cuyas firmas deberán estar certificadas por los respectivos
Consejos Profesionales (Fórmula 4368C)
La citada solicitud se remitirá acompañada de la fórmula a través de la cual la asociación
de profesionales universitarios se constituye en fiadora solidaria por las eventuales multas
que por el ejercicio de las tareas de auditoría externa en cajas de crédito se apliquen,
conforme a lo establecido en los artículos 41 y 42 de la Ley de Entidades Financieras.
Además, presentarán con carácter de declaración jurada, la nómina de la totalidad de los
socios integrantes del estudio, actúen o no como auditores externos de entidades
financieras y sean o no contadores públicos nacionales -detallando nombre y apellido,
documento de identidad, domicilio y matrícula profesional-.
Las asociaciones de profesionales constituidas de acuerdo con un tipo societario, sea éste
de naturaleza civil, comercial o simple asociación, constituida en el país o en el extranjero
y que actúen a nombre propio o a través de una representación local, deberán además
adjuntar testimonio del instrumento notarial debidamente legalizado, en su caso, por el
cual la sociedad o asociación asume la responsabilidad solidaria referida o, en su defecto,
deberán acreditar los firmantes la representatividad suficiente para obligarla en forma
solidaria.
```

Versión: final (grafo sin cola). Nodos 10, aristas 15.
- **N1** Condicion `Condicion_condicion_asociacion_constituida_con_tipo_societario__cuando_la_asociacion_de_pr_85e6e3` — Condición: asociación constituida con tipo societario · {"descripcion": "Cuando la asociación de profesionales esté constituida de acuerdo con un tipo societario de naturaleza civil, comercial o simple asociación, constituida en el país o en el extranjero y que actúe a nombre propio o a través de una representación local"} · tramo: Las asociaciones de profesionales constituidas de acuerdo con un tipo societario, sea éste de naturaleza civil, comercial o simple asociación, constituida en el país o en el extranjero y que actúen a nombre propio o a través de una representación local
- **N2** Definicion `Definicion_definicion_asociaciones_de_profesionales_universitarios__asociaciones_de_profesi_0dd18f` — Definición: asociaciones de profesionales universitarios · {"termino": "asociaciones de profesionales universitarios", "descripcion": "Asociaciones de profesionales universitarios cuyos socios cumplan funciones de auditoría externa en cajas de crédito dejando constancia en sus informes de tal carácter"} · tramo: Las asociaciones de profesionales universitarios, cuyos socios cumplan funciones de auditoría externa en Cajas de crédito dejando constancia en sus informes de tal carácter
- **N3** Obligacion `Obligacion_la_solicitud_se_remitira_acompanada_de_la_formula_a_traves_de_la_cual_la_asociac_4e5900` — Remisión de solicitud con fórmula de responsabilidad solidaria · {"tipo": "presentacion_informativa", "descripcion": "La solicitud se remitirá acompañada de la fórmula a través de la cual la asociación de profesionales universitarios se constituye en fiadora solidaria por las eventuales multas que por el ejercicio de las tareas de auditoría externa en cajas de crédito se apliquen, conforme a lo establecido en los artículos 41 y 42 de la Ley de Entidades Financi · tramo: La citada solicitud se remitirá acompañada de la fórmula a través de la cual la asociación de profesionales universitarios se constituye en fiadora solidaria por las eventuales multas que por el ejercicio de las tareas de auditoría externa en cajas de crédito se apliquen
- **N4** Obligacion `Obligacion_las_asociaciones_de_profesionales_constituidas_de_acuerdo_con_un_tipo_societario_28aba4` — Adjunción de testimonio notarial o acreditación de representatividad · {"tipo": "presentacion_informativa", "descripcion": "Las asociaciones de profesionales constituidas de acuerdo con un tipo societario, sea éste de naturaleza civil, comercial o simple asociación, constituida en el país o en el extranjero y que actúen a nombre propio o a través de una representación local, deberán adjuntar testimonio del instrumento notarial debidamente legalizado, en su caso, por  · tramo: deberán además adjuntar testimonio del instrumento notarial debidamente legalizado, en su caso, por el cual la sociedad o asociación asume la responsabilidad solidaria referida o, en su defecto, deberán acreditar los firmantes la representatividad suficiente para obligarla en forma solidaria
- **N5** Obligacion `Obligacion_las_asociaciones_de_profesionales_universitarios_cuyos_socios_cumplan_funciones__324084` — Deber de inscripción en Registro · {"tipo": "otra", "descripcion": "Las asociaciones de profesionales universitarios cuyos socios cumplan funciones de auditoría externa en cajas de crédito deberán inscribirse en el Registro de Asociaciones de Profesionales Universitarios habilitado en la Superintendencia de Entidades Financieras y Cambiarias"} · tramo: deberán inscribirse en el Registro de Asociaciones de Profesionales Universitarios habilitado en la Superintendencia de Entidades Financieras y Cambiarias
- **N6** Obligacion `Obligacion_para_cumplimentar_el_tramite_de_inscripcion_presentara_la_solicitud_de_inscripci_de0512` — Presentación de solicitud con nómina de socios · {"tipo": "presentacion_informativa", "descripcion": "Para cumplimentar el trámite de inscripción, presentará la solicitud de inscripción con la nómina completa de todos los socios, cuyas firmas deberán estar certificadas por los respectivos Consejos Profesionales (Fórmula 4368C)"} · tramo: presentará la solicitud de inscripción con la nómina completa de todos los socios, cuyas firmas deberán estar certificadas por los respectivos Consejos Profesionales
- **N7** Obligacion `Obligacion_presentaran_con_caracter_de_declaracion_jurada_la_nomina_de_la_totalidad_de_los__6ed2e2` — Presentación de nómina de socios como declaración jurada · {"tipo": "presentacion_informativa", "descripcion": "Presentarán con carácter de declaración jurada la nómina de la totalidad de los socios integrantes del estudio, actúen o no como auditores externos de entidades financieras y sean o no contadores públicos nacionales, detallando nombre y apellido, documento de identidad, domicilio y matrícula profesional"} · tramo: presentarán con carácter de declaración jurada, la nómina de la totalidad de los socios integrantes del estudio, actúen o no como auditores externos de entidades financieras y sean o no contadores públicos nacionales -detallando nombre y apellido, documento de identidad, domicilio y matrícula profes
- **N8** Operacion `Operacion_inscripcion_en_registro_de_asociaciones__ri_ccna_d1a1_4_1_6bf405` — Inscripción en Registro de Asociaciones · {"tipo": "inscripción", "descripcion": "Inscripción de asociaciones de profesionales universitarios cuyos socios cumplan funciones de auditoría externa en cajas de crédito en el Registro de Asociaciones de Profesionales Universitarios habilitado en la Superintendencia de Entidades Financieras y Cambiarias"} · tramo: inscribirse en el Registro de Asociaciones de Profesionales Universitarios habilitado en la Superintendencia de Entidades Financieras y Cambiarias
- **N9** Sujeto `Sujeto_propuesto_las_asociaciones_de_profesionales_universitarios_cuyos_socios_cumplan_funciones_` — Las asociaciones de profesionales universitarios, cuyos socios cumplan funciones de auditoría externa en Cajas de crédito · {"nivel": "propuesto", "cuarentena": "true", "padre_sugerido": "Sujeto_sujeto_regulado"} · tramo: 
- **N10** TextoOrdenado `TextoOrdenado_ri_ccna_pdf` — Régimen de Información Contable · {"archivo": "ri_ccna.pdf", "materia": "RI para Cajas de Crédito - Normas de Auditoría", "version": "Comunicación A 4523 (vigencia 06/04/2006)"} · tramo: 
- **A1** (extraccion) N1 —condicion_de→ N4 · {}
- **E1** (estructural) N1 —establecida_en→ N10 · {}
- **E2** (estructural) N2 —establecida_en→ N10 · {}
- **E3** (estructural) N3 —establecida_en→ N10 · {}
- **E4** (estructural) N4 —establecida_en→ N10 · {}
- **A2** (extraccion) N5 —aplica_a→ N9 · {}
- **A3** (extraccion) N5 —condiciona→ N8 · {}
- **E5** (estructural) N5 —establecida_en→ N10 · {}
- **E6** (estructural) N6 —establecida_en→ N10 · {}
- **E7** (estructural) N7 —establecida_en→ N10 · {}
- **E8** (estructural) N8 —establecida_en→ N10 · {}
- **A4** (extraccion) N8 —requiere→ N3 · {}
- **A5** (extraccion) N8 —requiere→ N6 · {}
- **A6** (extraccion) N8 —requiere→ N7 · {}
- **C1** (catalogo_sujetos) N9 —padre_sugerido→ Sujeto_sujeto_regulado · {"flag": "padre_sugerido_no_laudado"}

## 8. `ri_mmsef::2.2.8.2.6` — RI:sin_raiz · aceptadas:no_items

Texto que vio E3 (e0, bloque de lista True; págs. 4):

```
[encabezado | punto S2]
2. Instrucciones particulares.
[encabezado | punto 2.2]
2.2. Cumplimiento de las medidas mínimas de seguridad.
[encabezado | punto 2.2.8]
2.2.8. Medidas de seguridad para atesoramiento de numerario.
[encabezado | punto 2.2.8.2]
2.2.8.2. Caja tesoro móvil:
[texto propio | punto 2.2.8.2.6]
2.2.8.2.6. Sensorización.
```

Versión: final (grafo sin cola). Nodos 1, aristas 0.
- **N1** TextoOrdenado `TextoOrdenado_ri_mmsef_pdf` — Régimen Informativo Medidas Mínimas Seguridad · {"archivo": "ri_mmsef.pdf", "materia": "RI Cont. Mensual - Medidas mínimas de seguridad en entidades financieras", "version": "Comunicación A 6623 (vigencia 05/01/2019)"} · tramo: 

## 9. `ri_ccna::D1A3L2::S25` — RI:sin_raiz · aceptadas:no_items

Texto que vio E3 (e0, bloque de lista True; págs. 19):

```
[encabezado | punto D1A3]
ANEXO III
[encabezado | punto D1A3L2]
B. PRUEBAS SUSTANTIVAS
[texto propio | punto D1A3L2::S25]
25. Evaluación de la razonabilidad de las previsiones para contingencias, mediante la
obtención de confirmaciones directas de los asesores legales de la entidad sobre
el estado de los asuntos en trámite y de otros procedimientos que, a juicio del
auditor externo, se consideren convenientes.
```

Versión: final (grafo sin cola). Nodos 4, aristas 4.
- **N1** Obligacion `Obligacion_obtener_confirmaciones_directas_de_los_asesores_legales_de_la_entidad_sobre_el_e_bc194d` — Obtención confirmaciones asesores legales · {"tipo": "presentacion_informativa", "descripcion": "Obtener confirmaciones directas de los asesores legales de la entidad sobre el estado de los asuntos en trámite como parte de la evaluación de razonabilidad de previsiones para contingencias."} · tramo: obtención de confirmaciones directas de los asesores legales de la entidad sobre el estado de los asuntos en trámite
- **N2** Operacion `Operacion_evaluacion_razonabilidad_previsiones_contingencias__ri_ccna_d1a3l2_s25_9c633b` — Evaluación razonabilidad previsiones contingencias · {"tipo": "Evaluación de previsiones", "descripcion": "Evaluación de la razonabilidad de las previsiones para contingencias mediante la obtención de confirmaciones directas de los asesores legales de la entidad sobre el estado de los asuntos en trámite y de otros procedimientos que, a juicio del auditor externo, se consideren convenientes."} · tramo: Evaluación de la razonabilidad de las previsiones para contingencias
- **N3** Potestad `Potestad_facultad_auditor_externo_procedimientos_adicionales__el_auditor_externo_tiene_la_c531d4` — Facultad auditor externo procedimientos adicionales · {"descripcion": "El auditor externo tiene la facultad de realizar otros procedimientos que a su juicio se consideren convenientes para la evaluación de la razonabilidad de las previsiones para contingencias."} · tramo: otros procedimientos que, a juicio del auditor externo, se consideren convenientes
- **N4** TextoOrdenado `TextoOrdenado_ri_ccna_pdf` — Régimen de Información Contable · {"archivo": "ri_ccna.pdf", "materia": "RI para Cajas de Crédito - Normas de Auditoría", "version": "Comunicación A 4523 (vigencia 06/04/2006)"} · tramo: 
- **E1** (estructural) N1 —establecida_en→ N4 · {}
- **E2** (estructural) N2 —establecida_en→ N4 · {}
- **A1** (extraccion) N2 —requiere→ N1 · {}
- **E3** (estructural) N3 —establecida_en→ N4 · {}

## 10. `ri_ccna::D1A3L2::S7` — RI:sin_raiz · aceptadas:no_items

Texto que vio E3 (e0, bloque de lista True; págs. 16):

```
[encabezado | punto D1A3]
ANEXO III
[encabezado | punto D1A3L2]
B. PRUEBAS SUSTANTIVAS
[texto propio | punto D1A3L2::S7]
7. Revisión de la adecuada valuación de los rubros inversiones y bienes en
locación financiera, de acuerdo con las normas respectivas del B.C.R.A., así
como de la razonabilidad de las previsiones constituidas y de las amortizaciones
acumuladas de bienes en locación financiera, según corresponda.
```

Versión: final (grafo sin cola). Nodos 4, aristas 4.
- **N1** Condicion `Condicion_conformidad_con_normas_bcra__la_valuacion_debe_realizarse_de_acuerdo_con_las_nor_450f63` — Conformidad con normas BCRA · {"descripcion": "La valuación debe realizarse de acuerdo con las normas respectivas del Banco Central de la República Argentina"} · tramo: de acuerdo con las normas respectivas del B.C.R.A.
- **N2** Operacion `Operacion_evaluacion_de_razonabilidad_de_previsiones_y_amortizaciones__ri_ccna_d1a3l2_s7_c9185b` — Evaluación de razonabilidad de previsiones y amortizaciones · {"tipo": "Evaluación de razonabilidad", "descripcion": "Evaluación de la razonabilidad de las previsiones constituidas y de las amortizaciones acumuladas de bienes en locación financiera, según corresponda"} · tramo: de la razonabilidad de las previsiones constituidas y de las amortizaciones acumuladas de bienes en locación financiera
- **N3** Operacion `Operacion_valuacion_de_inversiones_y_bienes_en_locacion_financiera__ri_ccna_d1a3l2_s7_95bde1` — Valuación de inversiones y bienes en locación financiera · {"tipo": "Revisión de valuación", "descripcion": "Revisión de la adecuada valuación de los rubros inversiones y bienes en locación financiera, de acuerdo con las normas respectivas del B.C.R.A."} · tramo: Revisión de la adecuada valuación de los rubros inversiones y bienes en locación financiera
- **N4** TextoOrdenado `TextoOrdenado_ri_ccna_pdf` — Régimen de Información Contable · {"archivo": "ri_ccna.pdf", "materia": "RI para Cajas de Crédito - Normas de Auditoría", "version": "Comunicación A 4523 (vigencia 06/04/2006)"} · tramo: 
- **A1** (extraccion) N1 —condicion_de→ N3 · {}
- **E1** (estructural) N1 —establecida_en→ N4 · {}
- **E2** (estructural) N2 —establecida_en→ N4 · {}
- **E3** (estructural) N3 —establecida_en→ N4 · {}

## 11. `ri_rml::1.4.1` — RI:resto · aceptadas:no_items

Texto que vio E3 (e0, bloque de lista True; págs. 10, 11):

```
[encabezado | punto S1]
Sección 1. Efectivo mínimo
[encabezado | punto 1.4]
1.4. Exigencia trasladable
[texto propio | punto 1.4.1]
1.4.1. Moneda extranjera, títulos valores e instrumentos de regulación monetaria del BCRA.
Para determinar el traslado de la exigencia se utilizará la siguiente metodología: EEMA (n) =
[EEF (n)] + [ENI (n-1)]
Donde:
EEMA (n): Exigencia de efectivo mínimo ajustada correspondiente al mes “n”
[EEF (n)]: Exigencia de efectivo mínimo según normas vigentes correspondiente al mes “n”
[ENI (n-1)]: Exigencia no integrada del mes “n-1”, informada en el código 750000/M –TP
I (n): Integración del mes bajo informe.
Si: I (n) ≤ que [EEMA (n) * 0,8] => Defecto trasladable máximo = EEMA (n) * 0,20
Si: I (n) > [EEMA (n) * 0,8] => Defecto trasladable máximo = EEMA (n) - I(n)
```

Versión: final (grafo sin cola). Nodos 8, aristas 9.
- **N1** Condicion `Condicion_defecto_trasladable_maximo_cuando_integracion_80_eema__cuando_la_integracion_del_4215c2` — Defecto trasladable máximo cuando integración > 80% EEMA · {"descripcion": "Cuando la integración del mes bajo informe es mayor al 80% de la exigencia de efectivo mínimo ajustada, el defecto trasladable máximo es la diferencia entre la EEMA y la integración.", "umbrales": [{"tramo": "I (n) > [EEMA (n) * 0,8]", "comparacion": "no_determinada", "regla_comparacion": "limite_relativo:sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}, {"tramo": "Def · tramo: Si: I (n) > [EEMA (n) * 0,8] => Defecto trasladable máximo = EEMA (n) - I(n)
- **N2** Condicion `Condicion_defecto_trasladable_maximo_cuando_integracion_80_eema__cuando_la_integracion_del_8fde61` — Defecto trasladable máximo cuando integración ≤ 80% EEMA · {"descripcion": "Cuando la integración del mes bajo informe es menor o igual al 80% de la exigencia de efectivo mínimo ajustada, el defecto trasladable máximo es el 20% de la EEMA.", "umbrales": [{"tramo": "I (n) ≤ que [EEMA (n) * 0,8]", "comparacion": "no_determinada", "regla_comparacion": "limite_relativo:sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}, {"tramo": "Defecto trasladabl · tramo: Si: I (n) ≤ que [EEMA (n) * 0,8] => Defecto trasladable máximo = EEMA (n) * 0,20
- **N3** Definicion `Definicion_eef_exigencia_de_efectivo_minimo_segun_normas_vigentes__exigencia_de_efectivo_mi_936024` — EEF — Exigencia de efectivo mínimo según normas vigentes · {"termino": "EEF (n)", "descripcion": "Exigencia de efectivo mínimo según normas vigentes correspondiente al mes \"n\"."} · tramo: [EEF (n)]: Exigencia de efectivo mínimo según normas vigentes correspondiente al mes "n"
- **N4** Definicion `Definicion_eema_exigencia_de_efectivo_minimo_ajustada__exigencia_de_efectivo_minimo_ajustad_c9f92e` — EEMA — Exigencia de efectivo mínimo ajustada · {"termino": "EEMA (n)", "descripcion": "Exigencia de efectivo mínimo ajustada correspondiente al mes \"n\", calculada como la suma de la exigencia de efectivo mínimo según normas vigentes [EEF (n)] más la exigencia no integrada del mes anterior [ENI (n-1)]."} · tramo: EEMA (n): Exigencia de efectivo mínimo ajustada correspondiente al mes "n"
- **N5** Definicion `Definicion_eni_exigencia_no_integrada_del_mes_anterior__exigencia_no_integrada_del_mes_n_1__eb7556` — ENI — Exigencia no integrada del mes anterior · {"termino": "ENI (n-1)", "descripcion": "Exigencia no integrada del mes \"n-1\", informada en el código 750000/M –TP."} · tramo: [ENI (n-1)]: Exigencia no integrada del mes "n-1", informada en el código 750000/M –TP
- **N6** Definicion `Definicion_i_integracion_del_mes_bajo_informe__integracion_del_mes_bajo_informe__ri_rml_1_4_47d9bf` — I — Integración del mes bajo informe · {"termino": "I (n)", "descripcion": "Integración del mes bajo informe."} · tramo: I (n): Integración del mes bajo informe.
- **N7** Operacion `Operacion_traslado_de_exigencia_de_efectivo_minimo__ri_rml_1_4_1_adf38a` — Traslado de exigencia de efectivo mínimo · {"tipo": "Traslado de exigencia de efectivo mínimo", "descripcion": "Operación de traslado de la exigencia de efectivo mínimo ajustada (EEMA) en moneda extranjera, títulos valores e instrumentos de regulación monetaria del BCRA, sujeta a metodología de cálculo y límites cuantitativos según integración del mes bajo informe."} · tramo: traslado de la exigencia
- **N8** TextoOrdenado `TextoOrdenado_ri_rml_pdf` — Régimen Informativo Contable Mensual · {"archivo": "ri_rml.pdf", "materia": "RI Cont. Mensual - Efectivo mínimo y aplicación de recursos", "version": "Comunicación A 8453 (vigencia 12/06/2026)"} · tramo: 
- **A1** (extraccion) N1 —condicion_de→ N7 · {}
- **E1** (estructural) N1 —establecida_en→ N8 · {}
- **A2** (extraccion) N2 —condicion_de→ N7 · {}
- **E2** (estructural) N2 —establecida_en→ N8 · {}
- **E3** (estructural) N3 —establecida_en→ N8 · {}
- **E4** (estructural) N4 —establecida_en→ N8 · {}
- **E5** (estructural) N5 —establecida_en→ N8 · {}
- **E6** (estructural) N6 —establecida_en→ N8 · {}
- **E7** (estructural) N7 —establecida_en→ N8 · {}

## 12. `ri_dcpc::3.7.5` — RI:resto · aceptadas:no_items

Texto que vio E3 (e0, bloque de lista True; págs. 24, 25, 26):

```
[encabezado | punto S3]
Sección 3. CRITERIOS GENERALES
[encabezado | punto 3.7]
3.7. Mecanismo de reexpresión
[texto propio | punto 3.7.5]
3.7.5. Procedimiento de reexpresión mensual
1. A efectos de aplicar el procedimiento de ajuste, se deberán clasificar las partidas en
monetarias y no monetarias según las definiciones de la NIC 29 y la Tabla de
correspondencia para la reexpresión de partidas anexa en esta Sección 3.
2. Al 01.01.2020 deberán practicar el procedimiento de aplicación inicial detallado en la Sección
7 de la presente Guía.
3. Asimismo, a partir del 01.01.2020, al cierre de cada mes, se deberán reexpresar los saldos
iniciales (que no se hubieren dado de baja durante el mes) de las “partidas no monetarias”
aplicando el coeficiente de reexpresión. La diferencia entre el importe original y el
reexpresado deberá incrementar el saldo de la cuenta sujeta a ajuste con contrapartida en
“Ajustes al patrimonio- Ajuste por reexpresión de partidas”.
4. Respecto de los movimientos del mes se procederá de la siguiente forma:
 Resultados por transacciones: no se ajustarán cuando se encuentren expresados en
moneda del período.
 Resultados originados en la medición a valor razonable de activos no monetarios (por
ejemplo inversiones en instrumentos de patrimonio medidos a valor razonable con cambio
en resultados y propiedades de inversión medidas a valor razonable): a efectos de
reconocer estos resultados se comparará el saldo de la partida que los origina medida a
valor razonable al cierre con el saldo al cierre del mes anterior reexpresado y los
movimientos del periodo sin reexpresar –ya que se encuentran expresados en moneda
del periodo-.
 Amortizaciones de activos no monetarios: deberán devengarse a base del valor residual
reexpresado del activo.
 Baja de activos no monetarios: en estos casos se recalculará el resultado por la baja o
por la venta de estos activos teniendo en cuenta el saldo inicial reexpresado a fin de mes
con contrapartida en “Ajustes al patrimonio- Ajuste por reexpresión de partidas”.
 Altas de activos no monetarios: no se reexpresarán cuando se encuentren expresados en
moneda del período. Deberán reexpresarse las partidas reimputadas que hayan
conformado el saldo inicial de otras partidas no monetarias.
 Otros Resultados Integrales provenientes de partidas no monetarias en moneda de
cierre del período: la imputación surgirá por diferencia entre la medición al cierre
del mes anterior de la partida que los origina reexpresada a fecha de cierre, los
movimientos del periodo sin reexpresar -ya que se encuentran expresados en
moneda del periodo- y el saldo de la partida al cierre.
 Participaciones en subsidiarias, asociadas y negocios conjuntos medidos según el
método de la participación: este método se aplicará sobre la base de los estados
financieros ajustados por inflación de la sociedad emisora.
5. El resultado de la posición monetaria se calculará por medio del producto del saldo inicial de
cada partida monetaria (incluidas las que se encuentren medidas a valor razonable con
cambios en ORI) y la tasa de inflación. Este resultado se clasificará en función de la partida
que le dió origen en las siguientes cuentas, con contrapartida en “Ajustes al patrimonio-
Ajuste por reexpresión de partidas”:
620001 – Resultado monetario de partidas con cláusula de ajuste.
620002 – Resultado monetario de partidas en moneda extranjera.
620004 – Resultado monetario por otras partidas.
6. Los activos y pasivos por impuesto diferido al cierre del mes bajo informe se calcularán luego
de practicar el ajuste de las partidas no monetarias, es decir sus saldos surgirán de la
comparación entre las bases fiscales de activos y pasivos y los importes contables
reexpresados, de corresponder. El importe del impuesto diferido a imputar en la partida de
Impuesto a las Ganancias, surgirá de comparar los saldos de activos y pasivos por impuesto
diferido determinados el mes anterior reexpresados por el coeficiente mensual y los
determinados al cierre del mes.
7. A fin de mes, una vez reexpresadas las partidas que corresponda y registrado el Resultado
Monetario del período, la cuenta “Ajustes al patrimonio- Ajuste por reexpresión de partidas”
deberá quedar saldada.
8. Otras consideraciones:
 Ajuste de capital: la reexpresión monetaria tanto del Capital Social como de los Aportes
no Capitalizados, se imputará en la cuenta “Ajustes al patrimonio- Ajustes al capital”
considerándose como fecha de origen la de suscripción.
 Valor recuperable: Al aplicar la reexpresión de activos no monetarios, se debe tener en
cuenta que, en ningún caso, el importe resultante debe exceder el valor recuperable
dispuesto en la NIC 36.
```

Versión: final (grafo sin cola). Nodos 21, aristas 39.
- **N1** Obligacion `Obligacion_calculo_de_activos_y_pasivos_por_impuesto_diferido_al_cierre_del_mes_comparando__18630c` — Cálculo de activos y pasivos por impuesto diferido · {"tipo": "calculo", "descripcion": "Cálculo de activos y pasivos por impuesto diferido al cierre del mes comparando bases fiscales con importes contables reexpresados, luego del ajuste de partidas no monetarias"} · tramo: Los activos y pasivos por impuesto diferido al cierre del mes bajo informe se calcularán luego de practicar el ajuste de las partidas no monetarias, es decir sus saldos surgirán de la comparación entre las bases fiscales de activos y pasivos y los importes contables reexpresados, de corresponder
- **N2** Obligacion `Obligacion_clasificacion_del_resultado_monetario_en_cuentas_620001_620002_o_620004_segun_or_0a00a8` — Clasificación de resultado monetario en cuentas específicas · {"tipo": "asignacion", "descripcion": "Clasificación del resultado monetario en cuentas 620001, 620002 o 620004 según origen, con contrapartida en Ajustes al patrimonio - Ajuste por reexpresión de partidas"} · tramo: Este resultado se clasificará en función de la partida que le dió origen en las siguientes cuentas, con contrapartida en "Ajustes al patrimonio- Ajuste por reexpresión de partidas": 620001 – Resultado monetario de partidas con cláusula de ajuste. 620002 – Resultado monetario de partidas en moneda ex
- **N3** Obligacion `Obligacion_deber_de_practicar_el_procedimiento_de_aplicacion_inicial_conforme_a_seccion_7_d_f966db` — Aplicación inicial del procedimiento al 01.01.2020 · {"tipo": "otra", "descripcion": "Deber de practicar el procedimiento de aplicación inicial conforme a Sección 7 de la Guía a partir del 01.01.2020", "umbrales": [{"tramo": "Al 01.01.2020", "comparacion": "no_determinada", "regla_comparacion": "limite_relativo:sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}]} · tramo: Al 01.01.2020 deberán practicar el procedimiento de aplicación inicial detallado en la Sección 7 de la presente Guía
- **N4** Obligacion `Obligacion_el_metodo_de_participacion_para_subsidiarias_asociadas_y_negocios_conjuntos_se_a_e6aba3` — Aplicación del método de participación sobre estados ajustados · {"tipo": "otra", "descripcion": "El método de participación para subsidiarias, asociadas y negocios conjuntos se aplicará sobre estados financieros ajustados por inflación de la sociedad emisora"} · tramo: Participaciones en subsidiarias, asociadas y negocios conjuntos medidos según el método de la participación: este método se aplicará sobre la base de los estados financieros ajustados por inflación de la sociedad emisora
- **N5** Obligacion `Obligacion_en_baja_de_activos_no_monetarios_recalcular_resultado_considerando_saldo_inicial_eab268` — Recálculo de resultado por baja de activos no monetarios · {"tipo": "calculo", "descripcion": "En baja de activos no monetarios, recalcular resultado considerando saldo inicial reexpresado a fin de mes con contrapartida en Ajustes al patrimonio - Ajuste por reexpresión de partidas"} · tramo: Baja de activos no monetarios: en estos casos se recalculará el resultado por la baja o por la venta de estos activos teniendo en cuenta el saldo inicial reexpresado a fin de mes con contrapartida en "Ajustes al patrimonio- Ajuste por reexpresión de partidas"
- **N6** Obligacion `Obligacion_importe_de_impuesto_diferido_a_imputar_en_impuesto_a_las_ganancias_surge_de_comp_9df236` — Imputación de impuesto diferido en Ganancias · {"tipo": "calculo", "descripcion": "Importe de impuesto diferido a imputar en Impuesto a las Ganancias surge de comparar saldos del mes anterior reexpresados y saldos al cierre"} · tramo: El importe del impuesto diferido a imputar en la partida de Impuesto a las Ganancias, surgirá de comparar los saldos de activos y pasivos por impuesto diferido determinados el mes anterior reexpresados por el coeficiente mensual y los determinados al cierre del mes
- **N7** Obligacion `Obligacion_la_cuenta_ajustes_al_patrimonio_ajuste_por_reexpresion_de_partidas_debe_quedar_s_22672b` — Saldo de cuenta de Ajustes al patrimonio a fin de mes · {"tipo": "otra", "descripcion": "La cuenta Ajustes al patrimonio - Ajuste por reexpresión de partidas debe quedar saldada a fin de mes, luego de reexpresar partidas y registrar resultado monetario"} · tramo: A fin de mes, una vez reexpresadas las partidas que corresponda y registrado el Resultado Monetario del período, la cuenta "Ajustes al patrimonio- Ajuste por reexpresión de partidas" deberá quedar saldada
- **N8** Obligacion `Obligacion_la_diferencia_entre_importe_original_y_reexpresado_debe_incrementar_la_cuenta_de_01d997` — Registro de diferencia de reexpresión en patrimonio · {"tipo": "asignacion", "descripcion": "La diferencia entre importe original y reexpresado debe incrementar la cuenta de ajuste con contrapartida en Ajustes al patrimonio - Ajuste por reexpresión de partidas"} · tramo: La diferencia entre el importe original y el reexpresado deberá incrementar el saldo de la cuenta sujeta a ajuste con contrapartida en "Ajustes al patrimonio- Ajuste por reexpresión de partidas"
- **N9** Obligacion `Obligacion_la_imputacion_de_ori_de_partidas_no_monetarias_surge_por_diferencia_entre_medici_6d9c97` — Imputación de ORI de partidas no monetarias por diferencia · {"tipo": "calculo", "descripcion": "La imputación de ORI de partidas no monetarias surge por diferencia entre medición del mes anterior reexpresada, movimientos del período sin reexpresar y saldo al cierre"} · tramo: Otros Resultados Integrales provenientes de partidas no monetarias en moneda de cierre del período: la imputación surgirá por diferencia entre la medición al cierre del mes anterior de la partida que los origina reexpresada a fecha de cierre, los movimientos del periodo sin reexpresar -ya que se enc
- **N10** Obligacion `Obligacion_las_altas_de_activos_no_monetarios_expresados_en_moneda_del_periodo_no_se_reexpr_69fac1` — No reexpresión de altas de activos en moneda del período · {"tipo": "otra", "descripcion": "Las altas de activos no monetarios expresados en moneda del período no se reexpresarán"} · tramo: Altas de activos no monetarios: no se reexpresarán cuando se encuentren expresados en moneda del período
- **N11** Obligacion `Obligacion_las_amortizaciones_de_activos_no_monetarios_deben_devengarse_sobre_la_base_del_v_ca72f2` — Devengación de amortizaciones sobre valor residual reexpresado · {"tipo": "calculo", "descripcion": "Las amortizaciones de activos no monetarios deben devengarse sobre la base del valor residual reexpresado del activo"} · tramo: Amortizaciones de activos no monetarios: deberán devengarse a base del valor residual reexpresado del activo
- **N12** Obligacion `Obligacion_las_partidas_reimputadas_que_conformaron_el_saldo_inicial_de_otras_partidas_no_m_4e3c54` — Reexpresión de partidas reimputadas en altas de activos · {"tipo": "calculo", "descripcion": "Las partidas reimputadas que conformaron el saldo inicial de otras partidas no monetarias deben reexpresarse"} · tramo: Deberán reexpresarse las partidas reimputadas que hayan conformado el saldo inicial de otras partidas no monetarias
- **N13** Obligacion `Obligacion_los_resultados_por_transacciones_expresados_en_moneda_del_periodo_no_se_ajustara_b9fe95` — No ajuste de resultados por transacciones en moneda del período · {"tipo": "otra", "descripcion": "Los resultados por transacciones expresados en moneda del período no se ajustarán"} · tramo: Resultados por transacciones: no se ajustarán cuando se encuentren expresados en moneda del período
- **N14** Obligacion `Obligacion_para_resultados_de_medicion_a_valor_razonable_de_activos_no_monetarios_comparar__d37417` — Comparación de resultados por medición a valor razonable · {"tipo": "calculo", "descripcion": "Para resultados de medición a valor razonable de activos no monetarios, comparar saldo al cierre con saldo del mes anterior reexpresado y movimientos del período sin reexpresar"} · tramo: Resultados originados en la medición a valor razonable de activos no monetarios (por ejemplo inversiones en instrumentos de patrimonio medidos a valor razonable con cambio en resultados y propiedades de inversión medidas a valor razonable): a efectos de reconocer estos resultados se comparará el sal
- **N15** Obligacion `Obligacion_reexpresion_de_saldos_iniciales_de_partidas_no_monetarias_al_cierre_de_cada_mes__21e0dd` — Reexpresión mensual de saldos iniciales de partidas no monetarias · {"tipo": "calculo", "descripcion": "Reexpresión de saldos iniciales de partidas no monetarias al cierre de cada mes aplicando coeficiente de reexpresión, excluyendo partidas dadas de baja durante el mes", "frecuencia": "al cierre de cada mes", "umbrales": [{"tramo": "a partir del 01.01.2020", "comparacion": "no_determinada", "regla_comparacion": "limite_relativo:sin_marcador", "origen": "e1", "tra · tramo: a partir del 01.01.2020, al cierre de cada mes, se deberán reexpresar los saldos iniciales (que no se hubieren dado de baja durante el mes) de las "partidas no monetarias" aplicando el coeficiente de reexpresión
- **N16** Obligacion `Obligacion_reexpresion_monetaria_del_capital_social_y_aportes_no_capitalizados_se_imputa_en_14d179` — Imputación de reexpresión del Capital Social · {"tipo": "asignacion", "descripcion": "Reexpresión monetaria del Capital Social y Aportes no Capitalizados se imputa en Ajustes al patrimonio - Ajustes al capital, considerando fecha de origen la de suscripción"} · tramo: Ajuste de capital: la reexpresión monetaria tanto del Capital Social como de los Aportes no Capitalizados, se imputará en la cuenta "Ajustes al patrimonio- Ajustes al capital" considerándose como fecha de origen la de suscripción
- **N17** Obligacion `Obligacion_resultado_de_posicion_monetaria_calculado_como_producto_del_saldo_inicial_de_cad_21827c` — Cálculo de resultado de posición monetaria · {"tipo": "calculo", "descripcion": "Resultado de posición monetaria calculado como producto del saldo inicial de cada partida monetaria y la tasa de inflación"} · tramo: El resultado de la posición monetaria se calculará por medio del producto del saldo inicial de cada partida monetaria (incluidas las que se encuentren medidas a valor razonable con cambios en ORI) y la tasa de inflación
- **N18** Operacion `Operacion_clasificacion_de_partidas_monetarias_y_no_monetarias__ri_dcpc_3_7_5_7e81c9` — Clasificación de partidas monetarias y no monetarias · {"tipo": "clasificación contable", "descripcion": "Clasificación de partidas en monetarias y no monetarias conforme a NIC 29 y tabla de correspondencia de la Sección 3"} · tramo: se deberán clasificar las partidas en monetarias y no monetarias según las definiciones de la NIC 29 y la Tabla de correspondencia para la reexpresión de partidas anexa en esta Sección 3
- **N19** Restriccion `Restriccion_el_importe_resultante_de_la_reexpresion_de_activos_no_monetarios_no_debe_exceder_ede9a8` — Límite de valor recuperable en reexpresión de activos · {"tipo": "limite_cualitativo", "descripcion": "El importe resultante de la reexpresión de activos no monetarios no debe exceder el valor recuperable conforme a NIC 36"} · tramo: Valor recuperable: Al aplicar la reexpresión de activos no monetarios, se debe tener en cuenta que, en ningún caso, el importe resultante debe exceder el valor recuperable dispuesto en la NIC 36
- **N20** Sujeto `Sujeto_propuesto_las_entidades__ri_dcpc` — las entidades · {"nivel": "propuesto", "cuarentena": "true", "colision_cross_to": "true", "padre_sugerido": "Sujeto_entidad_financiera", "padre_desde_sugerencia_modelo": "true"} · tramo: 
- **N21** TextoOrdenado `TextoOrdenado_ri_dcpc_pdf` — Marco Contable · {"archivo": "ri_dcpc.pdf", "materia": "RI - Disposiciones complementarias al plan de cuentas", "version": "Comunicación A 8400 (vigencia 13/02/2026)"} · tramo: 
- **A1** (extraccion) N1 —aplica_a→ N20 · {}
- **E1** (estructural) N1 —establecida_en→ N21 · {}
- **A2** (extraccion) N2 —aplica_a→ N20 · {}
- **E2** (estructural) N2 —establecida_en→ N21 · {}
- **A3** (extraccion) N3 —aplica_a→ N20 · {}
- **E3** (estructural) N3 —establecida_en→ N21 · {}
- **A4** (extraccion) N4 —aplica_a→ N20 · {}
- **E4** (estructural) N4 —establecida_en→ N21 · {}
- **A5** (extraccion) N5 —aplica_a→ N20 · {}
- **E5** (estructural) N5 —establecida_en→ N21 · {}
- **A6** (extraccion) N6 —aplica_a→ N20 · {}
- **E6** (estructural) N6 —establecida_en→ N21 · {}
- **A7** (extraccion) N7 —aplica_a→ N20 · {}
- **E7** (estructural) N7 —establecida_en→ N21 · {}
- **A8** (extraccion) N8 —aplica_a→ N20 · {}
- **E8** (estructural) N8 —establecida_en→ N21 · {}
- **A9** (extraccion) N9 —aplica_a→ N20 · {}
- **E9** (estructural) N9 —establecida_en→ N21 · {}
- **A10** (extraccion) N10 —aplica_a→ N20 · {}
- **E10** (estructural) N10 —establecida_en→ N21 · {}
- **A11** (extraccion) N11 —aplica_a→ N20 · {}
- **E11** (estructural) N11 —establecida_en→ N21 · {}
- **A12** (extraccion) N12 —aplica_a→ N20 · {}
- **E12** (estructural) N12 —establecida_en→ N21 · {}
- **A13** (extraccion) N13 —aplica_a→ N20 · {}
- **E13** (estructural) N13 —establecida_en→ N21 · {}
- **A14** (extraccion) N14 —aplica_a→ N20 · {}
- **E14** (estructural) N14 —establecida_en→ N21 · {}
- **A15** (extraccion) N15 —aplica_a→ N20 · {}
- **E15** (estructural) N15 —establecida_en→ N21 · {}
- **A16** (extraccion) N16 —aplica_a→ N20 · {}
- **E16** (estructural) N16 —establecida_en→ N21 · {}
- **A17** (extraccion) N17 —aplica_a→ N20 · {}
- **E17** (estructural) N17 —establecida_en→ N21 · {}
- **A18** (extraccion) N18 —aplica_a→ N20 · {}
- **E18** (estructural) N18 —establecida_en→ N21 · {}
- **A19** (extraccion) N19 —aplica_a→ N20 · {}
- **E19** (estructural) N19 —establecida_en→ N21 · {}
- **C1** (catalogo_sujetos) N20 —padre_sugerido→ Sujeto_entidad_financiera · {"flag": "padre_sugerido_no_laudado"}

## 13. `ri_gerc::2.5.3` — RI:resto · aceptadas:no_items

Texto que vio E3 (e0, bloque de lista True; págs. 6):

```
[encabezado | punto S2]
Sección 2. Instrucciones Particulares
[encabezado | punto 2.5]
2.5. Excesos
[texto propio | punto 2.5.3]
2.5.3. Origen del exceso
Se consignará si el origen del exceso es imputable o no imputable a la entidad financiera
(EF), conforme al siguiente detalle:
1 = No imputable a la EF
2 = Imputable a la EF
```

Versión: final (grafo sin cola). Nodos 4, aristas 3.
- **N1** Definicion `Definicion_origen_del_exceso_clasificacion__se_clasifica_en_dos_categorias_1_no_imputable_a_144abb` — Origen del exceso — clasificación · {"termino": "origen del exceso", "descripcion": "Se clasifica en dos categorías: 1 = No imputable a la EF; 2 = Imputable a la EF"} · tramo: el origen del exceso es imputable o no imputable a la entidad financiera (EF), conforme al siguiente detalle: 1 = No imputable a la EF; 2 = Imputable a la EF
- **N2** Operacion `Operacion_consignacion_de_origen_del_exceso__ri_gerc_2_5_3_ed3ea7` — Consignación de origen del exceso · {"tipo": "Presentación informativa", "descripcion": "Consignación de si el origen del exceso es imputable o no imputable a la entidad financiera, conforme a: 1 = No imputable a la EF; 2 = Imputable a la EF"} · tramo: Se consignará si el origen del exceso es imputable o no imputable a la entidad financiera
- **N3** Sujeto `Sujeto_entidad_financiera` — Entidades financieras · {"nivel": "clase", "alias": ["Entidades financieras emisoras de tarjetas de crédito y/o compra", "Entidad financiera emisora de tarjetas de crédito y/o compra"]} · tramo: 
- **N4** TextoOrdenado `TextoOrdenado_ri_gerc_pdf` — Régimen Informativo Contable Mensual · {"archivo": "ri_gerc.pdf", "materia": "RI Cont. Mensual - Grandes exposiciones al riesgo de crédito", "version": "Comunicación A 8317 (vigencia 01/09/2025)"} · tramo: 
- **E1** (estructural) N1 —establecida_en→ N4 · {}
- **A1** (extraccion) N2 —aplica_a→ N3 · {}
- **E2** (estructural) N2 —establecida_en→ N4 · {}

## 14. `ri_rml::1.7.1` — RI:resto · aceptadas:no_items

Texto que vio E3 (e0, bloque de lista True; págs. 13, 14):

```
[encabezado | punto S1]
Sección 1. Efectivo mínimo
[encabezado | punto 1.7]
1.7. Cargos
[texto propio | punto 1.7.1]
1.7.1. Determinación.
Para calcular los cargos correspondientes a las posiciones mensuales, se utiliza la si-
guiente metodología:
EEMA - Código 750000/M-TP recalculado según pto. 1.4. - I – 671000/M-TP
(n) (n) (n) (n)
= Defecto neto por moneda o instrumento de deuda (expresado en numerales)
Para M = 001 se deducirá / incrementará también el importe del Código 700000/001
Defecto * (T.N.A. / 36500) * 1000 = Cargo por moneda o instrumento de deuda
Cargo/M–TP – Código 681000/M-TP = Cargo a debitar
Los cargos por defecto de integración mínima diaria (por moneda) se calcularán de la si-
guiente manera:
[ Suma de defectos diarios (por moneda) * (TNA / 36500) ] * 1000, deducidas las
franquicias incluidas en código 682000/M.
En caso de coexistir defectos de integración el importe a debitar será el que resulte mayor
entre: Cargo por defectos de integración mínima diaria y el cargo por la posición en pro-
medio.
La comparación se efectuará teniendo en cuenta la moneda en que esté expresada la po-
sición que dio origen a la determinación de cargos.
La conversión a pesos de los cargos determinados se efectuará utilizando el tipo de cam-
bio de referencia del dólar estadounidense difundido por el BCRA correspondiente al día
hábil cambiario anterior a la fecha de presentación de la nota de débito o en su caso, de
vencimiento fijada para ello.
Por el importe del cargo se acompañará nota de débito (Fórmula 3030) indicando como
concepto de la operación ¨Cargo por defecto de integración de Efectivo Mínimo” en (men-
cionar la moneda o instrumento de deuda de que se trate).
Para determinar los intereses aplicables a los cargos no ingresados en tiempo y forma se
considerarán las distintas tasas vigentes durante el lapso de la mora
```

Versión: final (grafo sin cola). Nodos 8, aristas 9.
- **N1** Condicion `Condicion_cargos_no_ingresados_en_tiempo_y_forma__supuesto_en_que_los_cargos_no_se_ingresa_7d6b3f` — Cargos no ingresados en tiempo y forma · {"descripcion": "Supuesto en que los cargos no se ingresan en tiempo y forma"} · tramo: los cargos no ingresados en tiempo y forma
- **N2** Condicion `Condicion_coexistencia_de_defectos_de_integracion__supuesto_en_que_coexisten_defectos_de_i_ce85e1` — Coexistencia de defectos de integración · {"descripcion": "Supuesto en que coexisten defectos de integración"} · tramo: En caso de coexistir defectos de integración
- **N3** Obligacion `Obligacion_para_determinar_los_intereses_aplicables_a_los_cargos_no_ingresados_en_tiempo_y__504d94` — Consideración de tasas vigentes para intereses en mora · {"tipo": "calculo", "descripcion": "Para determinar los intereses aplicables a los cargos no ingresados en tiempo y forma, se deben considerar las distintas tasas vigentes durante el lapso de la mora"} · tramo: Para determinar los intereses aplicables a los cargos no ingresados en tiempo y forma se considerarán las distintas tasas vigentes durante el lapso de la mora
- **N4** Obligacion `Obligacion_se_debe_acompanar_nota_de_debito_formula_3030_indicando_como_concepto_cargo_por__108877` — Acompañamiento de nota de débito con concepto especificado · {"tipo": "presentacion_informativa", "descripcion": "Se debe acompañar nota de débito (Fórmula 3030) indicando como concepto 'Cargo por defecto de integración de Efectivo Mínimo' en la moneda o instrumento de deuda de que se trate"} · tramo: Por el importe del cargo se acompañará nota de débito (Fórmula 3030) indicando como concepto de la operación ¨Cargo por defecto de integración de Efectivo Mínimo" en (mencionar la moneda o instrumento de deuda de que se trate)
- **N5** Operacion `Operacion_calculo_de_cargos_por_defecto_de_integracion_minima__ri_rml_1_7_1_1db38b` — Cálculo de cargos por defecto de integración mínima · {"tipo": "cálculo de cargos", "descripcion": "Cálculo de cargos por defecto de integración mínima diaria (por moneda) mediante la fórmula: Suma de defectos diarios (por moneda) * (TNA / 36500) * 1000, deducidas las franquicias incluidas en código 682000/M"} · tramo: Para calcular los cargos correspondientes a las posiciones mensuales, se utiliza la siguiente metodología
- **N6** Operacion `Operacion_comparacion_de_cargos_por_defectos_coexistentes__ri_rml_1_7_1_ddc320` — Comparación de cargos por defectos coexistentes · {"tipo": "comparación y selección", "descripcion": "Cuando coexisten defectos de integración, se debita el importe mayor entre el cargo por defectos de integración mínima diaria y el cargo por la posición en promedio"} · tramo: En caso de coexistir defectos de integración el importe a debitar será el que resulte mayor entre: Cargo por defectos de integración mínima diaria y el cargo por la posición en promedio
- **N7** Operacion `Operacion_conversion_a_pesos_de_cargos_determinados__ri_rml_1_7_1_af0627` — Conversión a pesos de cargos determinados · {"tipo": "conversión de moneda", "descripcion": "Conversión a pesos de los cargos determinados utilizando el tipo de cambio de referencia del dólar estadounidense difundido por el BCRA del día hábil cambiario anterior a la fecha de presentación de la nota de débito o de vencimiento"} · tramo: La conversión a pesos de los cargos determinados se efectuará utilizando el tipo de cambio de referencia del dólar estadounidense difundido por el BCRA correspondiente al día hábil cambiario anterior a la fecha de presentación de la nota de débito o en su caso, de vencimiento fijada para ello
- **N8** TextoOrdenado `TextoOrdenado_ri_rml_pdf` — Régimen Informativo Contable Mensual · {"archivo": "ri_rml.pdf", "materia": "RI Cont. Mensual - Efectivo mínimo y aplicación de recursos", "version": "Comunicación A 8453 (vigencia 12/06/2026)"} · tramo: 
- **A1** (extraccion) N1 —condicion_de→ N3 · {}
- **E1** (estructural) N1 —establecida_en→ N8 · {}
- **A2** (extraccion) N2 —condicion_de→ N6 · {}
- **E2** (estructural) N2 —establecida_en→ N8 · {}
- **E3** (estructural) N3 —establecida_en→ N8 · {}
- **E4** (estructural) N4 —establecida_en→ N8 · {}
- **E5** (estructural) N5 —establecida_en→ N8 · {}
- **E6** (estructural) N6 —establecida_en→ N8 · {}
- **E7** (estructural) N7 —establecida_en→ N8 · {}

## 15. `ri_rml::1.9.1` — RI:resto · aceptadas:no_items

Texto que vio E3 (e0, bloque de lista True; págs. 16, 17, 18):

```
[encabezado | punto S1]
Sección 1. Efectivo mínimo
[encabezado | punto 1.9]
1.9. Totales de control
[texto propio | punto 1.9.1]
1.9.1. Totales de control
Código 907000/M
Moneda extranjera: se informará el total de exigencia que surja de aplicar la tasa de en-
caje vigente en el mes bajo informe sobre los promedios de los conceptos previstos en el
punto 1.3. de las normas sobre “Efectivo mínimo”, de dicho mes.
Pesos, total que surja de aplicar la tasa de encaje vigente en el mes bajo informe sobre
los promedios del mes anterior, excepto para los depósitos en cuentas de los proveedo-
res de servicios de pago que ofrecen cuentas de pago (PSPOCP) en las que se encuen-
tren depositados los fondos de sus clientes, para los que se aplicará la tasa de encaje vi-
gente en el mes bajo informe sobre los promedios de dicho mes.
907000/001 = ∑ [Código 10XXXX/001 (excluyendo partida 102200 ) * ep ] + Partida
(n) (n-1) (n-1) (n)
102200 * ep
(n) (n)
Código 903000/M
Moneda extranjera: se informará el importe total de los conceptos de exigencia del mes -
en moneda extranjera- y se obtendrá adicionando al importe de las partidas 907000/M, el
valor de las exigencias adicionales (incrementos) que resulten aplicables por todo concep-
to, sin tener en cuenta los defectos trasladados.
Código 903000/M = Código 907000/M + 102400/M + 101500/M + 102160/M
(n) (n) (n) (n)
Pesos: total que surja de aplicar la tasa de encaje vigente en el mes bajo informe sobre
los promedios del mes anterior, excepto para los depósitos en cuentas de los proveedo-
res de servicios de pago que ofrecen cuentas de pago (PSPOCP) en las que se encuen-
tren depositados los fondos de sus clientes, para los que se aplicará la tasa de encaje vi-
gente en el mes bajo informe sobre los promedios de dicho mes, adicionando el valor
de las exigencias adicionales (incrementos) que resulten aplicables por todo con-
cepto, sin tener en cuenta el importe del código 700000/001.
Código 903000/001 = Código 907000/001 + 101500/001 + 102160/001
(n) (n-1) (n-1)
Código 903200/M
Se informará la exigencia del mes sobre los depósitos y obligaciones a plazo -en moneda
extranjera- según las tasas establecidas, sin tener en cuenta los traslados y el defecto de
aplicación de recursos.
Este total se conformará con las exigencias determinadas sobre las siguientes partidas:
[TABLA ri_rml::tabla001 | página 17 | e0_tablas | posicional]
Fila 1: col1 = 10120X/M | col2 = 10121X/M | col3 = 10122X/M | col4 = 10123X/M | col5 = 10124X/M | col6 = 10127X/M | col7 = 10128X/M | col8 = 10140X/M
Fila 2: col1 = 10141X/M | col2 = 10142X/M | col3 = 10143X/M | col4 = 10144X/M | col5 = 10145X/M | col6 = 101460/M | col7 = 10146X/001 | col8 = 10147X/001
Fila 3: col1 = 101470/M | col2 = 101490/001 | col3 = 101500/M | col4 = 10160X/001 | col5 = 10161X/001 | col6 = 10162X/001 | col7 = 10163X/001 | col8 = 10164X/001
Fila 4: col1 = 101650/001 | col2 = 10166X/001 | col3 = 10171X/001 | col4 = 10175X/001 | col5 = 10180X/M | col6 = 10190X/001 | col7 = 11010X/M | col8 = 10206X/M
[FIN TABLA ri_rml::tabla001]
Código 904000/M
Moneda extranjera: se consignará la integración total del mes, teniendo en cuenta que
para el código 904000/010, se deberá deducir la porción informada en las partidas
255035/M, 255040/M, 255050/M.
Para M= 010: 904000 = ∑ 20XXXX/010 + ∑ 210200/TP - ∑ 25XXXX/M
Otras ME: 904000 = ∑ (20XXXX/M +25XXXX/M)
Pesos: Para M= 001: 904000 = ∑ 20XXXX/001 + ∑ 210100/TP
Código 905000/TP
Se informará la exigencia del mes sobre los depósitos a plazo fijo de títulos valores públi-
cos o instrumentos de regulación monetaria del BCRA por cada especie captada según
las tasas establecidas teniendo en cuenta su moneda de denominación y sin considerar
los defectos trasladados.
Código 906000/TP
Se consignará la integración total del mes por cada especie de títulos valores públicos o
instrumentos de regulación monetaria del BCRA que registre exigencia (partida
905000/TP distinta de cero).
En caso de corresponder, el valor a consignar se calculará de la siguiente forma, de
acuerdo con la especie de que se trate:
[TABLA ri_rml::tabla002 | página 18 | e0_tablas | columnas]
Columnas: Especie | Cálculo
Fila 1: Especie = 9132 | Cálculo = 500000/9132 – 210100/9132
Fila 2: Especie = 9166 | Cálculo = 500000/9166 – 210100/9166
Fila 3: Especie = 13000 | Cálculo = 500000/130000 – 210100/13000
Fila 4: Especie = 14000 | Cálculo = 500000/14000 – 210100/14000
Fila 5: Especie = Otros TP | Cálculo = 500000/TP – (210100/TP o 210200/TP)
[FIN TABLA ri_rml::tabla002]
```

Versión: final (grafo sin cola). Nodos 18, aristas 42.
- **N1** Excepcion `Excepcion_excepcion_a_la_aplicacion_de_la_tasa_de_encaje_del_mes_anterior_para_depositos_e_c7e2d6` — Excepción PSPOCP — tasa de encaje mes actual · {"descripcion": "Excepción a la aplicación de la tasa de encaje del mes anterior: para depósitos en cuentas de PSPOCP con fondos de clientes, se aplica la tasa vigente en el mes bajo informe sobre los promedios de dicho mes."} · tramo: excepto para los depósitos en cuentas de los proveedores de servicios de pago que ofrecen cuentas de pago (PSPOCP) en las que se encuentren depositados los fondos de sus clientes, para los que se aplicará la tasa de encaje vigente en el mes bajo informe sobre los promedios de dicho mes
- **N2** Obligacion `Obligacion_obligacion_de_consignar_la_integracion_total_del_mes_por_cada_especie_de_titulos_7e5c68` — Consignar integración total títulos valores — Código 906000/TP · {"tipo": "presentacion_informativa", "descripcion": "Obligación de consignar la integración total del mes por cada especie de títulos valores públicos o instrumentos de regulación monetaria del BCRA que registre exigencia (partida 905000/TP distinta de cero). Código 906000/TP."} · tramo: Se consignará la integración total del mes por cada especie de títulos valores públicos o instrumentos de regulación monetaria del BCRA que registre exigencia (partida 905000/TP distinta de cero)
- **N3** Obligacion `Obligacion_obligacion_de_consignar_la_integracion_total_del_mes_teniendo_en_cuenta_que_para_8fc76b` — Consignar integración total — Código 904000/M · {"tipo": "presentacion_informativa", "descripcion": "Obligación de consignar la integración total del mes, teniendo en cuenta que para el código 904000/010, se deberá deducir la porción informada en las partidas 255035/M, 255040/M, 255050/M. Código 904000/M."} · tramo: se consignará la integración total del mes, teniendo en cuenta que para el código 904000/010, se deberá deducir la porción informada en las partidas 255035/M, 255040/M, 255050/M
- **N4** Obligacion `Obligacion_obligacion_de_informar_el_importe_total_de_los_conceptos_de_exigencia_del_mes_en_fd55f7` — Informar importe total exigencia — Código 903000/M · {"tipo": "presentacion_informativa", "descripcion": "Obligación de informar el importe total de los conceptos de exigencia del mes en moneda extranjera, adicionando al importe de las partidas 907000/M el valor de las exigencias adicionales (incrementos) aplicables por todo concepto, sin tener en cuenta los defectos trasladados. Código 903000/M."} · tramo: se informará el importe total de los conceptos de exigencia del mes -en moneda extranjera- y se obtendrá adicionando al importe de las partidas 907000/M, el valor de las exigencias adicionales (incrementos) que resulten aplicables por todo concepto, sin tener en cuenta los defectos trasladados
- **N5** Obligacion `Obligacion_obligacion_de_informar_el_total_de_exigencia_en_moneda_extranjera_que_surja_de_a_7d6866` — Informar exigencia moneda extranjera — Código 907000/M · {"tipo": "presentacion_informativa", "descripcion": "Obligación de informar el total de exigencia en moneda extranjera que surja de aplicar la tasa de encaje vigente en el mes bajo informe sobre los promedios de los conceptos previstos en el punto 1.3 de las normas sobre Efectivo mínimo, de dicho mes. Código 907000/M."} · tramo: se informará el total de exigencia que surja de aplicar la tasa de encaje vigente en el mes bajo informe sobre los promedios de los conceptos previstos en el punto 1.3. de las normas sobre "Efectivo mínimo", de dicho mes
- **N6** Obligacion `Obligacion_obligacion_de_informar_el_total_de_exigencia_en_pesos_que_surja_de_aplicar_la_ta_0b35a4` — Informar exigencia pesos — Código 907000/001 · {"tipo": "presentacion_informativa", "descripcion": "Obligación de informar el total de exigencia en pesos que surja de aplicar la tasa de encaje vigente en el mes bajo informe sobre los promedios del mes anterior, excepto para depósitos en cuentas de PSPOCP con fondos de clientes (tasa vigente en mes bajo informe sobre promedios de dicho mes). Código 907000/001."} · tramo: total que surja de aplicar la tasa de encaje vigente en el mes bajo informe sobre los promedios del mes anterior, excepto para los depósitos en cuentas de los proveedores de servicios de pago que ofrecen cuentas de pago (PSPOCP) en las que se encuentren depositados los fondos de sus clientes, para l
- **N7** Obligacion `Obligacion_obligacion_de_informar_la_exigencia_del_mes_sobre_depositos_a_plazo_fijo_de_titu_34253f` — Informar exigencia depósitos a plazo fijo títulos valores — Código 905000/TP · {"tipo": "presentacion_informativa", "descripcion": "Obligación de informar la exigencia del mes sobre depósitos a plazo fijo de títulos valores públicos o instrumentos de regulación monetaria del BCRA por cada especie captada según las tasas establecidas, teniendo en cuenta su moneda de denominación y sin considerar los defectos trasladados. Código 905000/TP."} · tramo: Se informará la exigencia del mes sobre los depósitos a plazo fijo de títulos valores públicos o instrumentos de regulación monetaria del BCRA por cada especie captada según las tasas establecidas teniendo en cuenta su moneda de denominación y sin considerar los defectos trasladados
- **N8** Obligacion `Obligacion_obligacion_de_informar_la_exigencia_del_mes_sobre_depositos_y_obligaciones_a_pla_64a1e9` — Informar exigencia depósitos a plazo — Código 903200/M · {"tipo": "presentacion_informativa", "descripcion": "Obligación de informar la exigencia del mes sobre depósitos y obligaciones a plazo en moneda extranjera según las tasas establecidas, sin tener en cuenta los traslados y el defecto de aplicación de recursos. Código 903200/M."} · tramo: Se informará la exigencia del mes sobre los depósitos y obligaciones a plazo -en moneda extranjera- según las tasas establecidas, sin tener en cuenta los traslados y el defecto de aplicación de recursos
- **N9** Operacion `Operacion_calculo_exigencia_depositos_a_plazo_codigo_903200_m__ri_rml_1_9_1_96a7bd` — Cálculo exigencia depósitos a plazo — Código 903200/M · {"tipo": "cálculo de exigencia", "descripcion": "Cálculo de la exigencia del mes sobre depósitos y obligaciones a plazo en moneda extranjera según las tasas establecidas, sin tener en cuenta los traslados y el defecto de aplicación de recursos. Código 903200/M. Se conforma con exigencias sobre partidas: 10120X/M, 10121X/M, 10122X/M, 10123X/M, 10124X/M, 10127X/M, 10128X/M, 10140X/M, 10141X/M, 10142 · tramo: Se informará la exigencia del mes sobre los depósitos y obligaciones a plazo -en moneda extranjera- según las tasas establecidas, sin tener en cuenta los traslados y el defecto de aplicación de recursos
- **N10** Operacion `Operacion_calculo_exigencia_depositos_a_plazo_fijo_titulos_valores_codigo_905000_tp__ri_rm_621d6f` — Cálculo exigencia depósitos a plazo fijo títulos valores — Código 905000/TP · {"tipo": "cálculo de exigencia", "descripcion": "Cálculo de la exigencia del mes sobre depósitos a plazo fijo de títulos valores públicos o instrumentos de regulación monetaria del BCRA por cada especie captada según las tasas establecidas, teniendo en cuenta su moneda de denominación y sin considerar los defectos trasladados. Código 905000/TP."} · tramo: Se informará la exigencia del mes sobre los depósitos a plazo fijo de títulos valores públicos o instrumentos de regulación monetaria del BCRA por cada especie captada según las tasas establecidas teniendo en cuenta su moneda de denominación y sin considerar los defectos trasladados
- **N11** Operacion `Operacion_calculo_exigencia_moneda_extranjera_codigo_903000_m__ri_rml_1_9_1_012ff4` — Cálculo exigencia moneda extranjera — Código 903000/M · {"tipo": "cálculo de exigencia total", "descripcion": "Cálculo del importe total de los conceptos de exigencia del mes en moneda extranjera, adicionando al importe de las partidas 907000/M el valor de las exigencias adicionales (incrementos) aplicables por todo concepto, sin tener en cuenta los defectos trasladados. Código 903000/M."} · tramo: se informará el importe total de los conceptos de exigencia del mes -en moneda extranjera- y se obtendrá adicionando al importe de las partidas 907000/M, el valor de las exigencias adicionales (incrementos) que resulten aplicables por todo concepto, sin tener en cuenta los defectos trasladados
- **N12** Operacion `Operacion_calculo_exigencia_moneda_extranjera_codigo_907000_m__ri_rml_1_9_1_b89591` — Cálculo exigencia moneda extranjera — Código 907000/M · {"tipo": "cálculo de exigencia de encaje", "descripcion": "Cálculo del total de exigencia en moneda extranjera aplicando la tasa de encaje vigente en el mes bajo informe sobre los promedios de los conceptos previstos en el punto 1.3 de las normas sobre Efectivo mínimo, de dicho mes. Código 907000/M."} · tramo: se informará el total de exigencia que surja de aplicar la tasa de encaje vigente en el mes bajo informe sobre los promedios de los conceptos previstos en el punto 1.3. de las normas sobre "Efectivo mínimo", de dicho mes
- **N13** Operacion `Operacion_calculo_exigencia_pesos_codigo_903000_001__ri_rml_1_9_1_ab4fb7` — Cálculo exigencia pesos — Código 903000/001 · {"tipo": "cálculo de exigencia total", "descripcion": "Cálculo del total de exigencia en pesos aplicando la tasa de encaje vigente en el mes bajo informe sobre los promedios del mes anterior, excepto para depósitos en cuentas de PSPOCP con fondos de clientes (tasa vigente en mes bajo informe sobre promedios de dicho mes), adicionando el valor de exigencias adicionales (incrementos) aplicables por  · tramo: total que surja de aplicar la tasa de encaje vigente en el mes bajo informe sobre los promedios del mes anterior, excepto para los depósitos en cuentas de los proveedores de servicios de pago que ofrecen cuentas de pago (PSPOCP) en las que se encuentren depositados los fondos de sus clientes, para l
- **N14** Operacion `Operacion_calculo_exigencia_pesos_codigo_907000_001__ri_rml_1_9_1_15614b` — Cálculo exigencia pesos — Código 907000/001 · {"tipo": "cálculo de exigencia de encaje", "descripcion": "Cálculo del total de exigencia en pesos aplicando la tasa de encaje vigente en el mes bajo informe sobre los promedios del mes anterior, excepto para depósitos en cuentas de PSPOCP donde se encuentren depositados fondos de clientes, para los que se aplicará la tasa vigente en el mes bajo informe sobre los promedios de dicho mes. Código 907 · tramo: total que surja de aplicar la tasa de encaje vigente en el mes bajo informe sobre los promedios del mes anterior, excepto para los depósitos en cuentas de los proveedores de servicios de pago que ofrecen cuentas de pago (PSPOCP) en las que se encuentren depositados los fondos de sus clientes, para l
- **N15** Operacion `Operacion_calculo_integracion_total_codigo_904000_m__ri_rml_1_9_1_3fca19` — Cálculo integración total — Código 904000/M · {"tipo": "cálculo de integración", "descripcion": "Cálculo de la integración total del mes. Para código 904000/010, se deducirá la porción informada en partidas 255035/M, 255040/M, 255050/M. Código 904000/M."} · tramo: se consignará la integración total del mes, teniendo en cuenta que para el código 904000/010, se deberá deducir la porción informada en las partidas 255035/M, 255040/M, 255050/M
- **N16** Operacion `Operacion_calculo_integracion_total_titulos_valores_codigo_906000_tp__ri_rml_1_9_1_1b62c3` — Cálculo integración total títulos valores — Código 906000/TP · {"tipo": "cálculo de integración", "descripcion": "Cálculo de la integración total del mes por cada especie de títulos valores públicos o instrumentos de regulación monetaria del BCRA que registre exigencia (partida 905000/TP distinta de cero). Código 906000/TP. Cálculos según especie: 9132: 500000/9132 – 210100/9132; 9166: 500000/9166 – 210100/9166; 13000: 500000/130000 – 210100/13000; 14000: 500 · tramo: Se consignará la integración total del mes por cada especie de títulos valores públicos o instrumentos de regulación monetaria del BCRA que registre exigencia (partida 905000/TP distinta de cero)
- **N17** Sujeto `Sujeto_propuesto_las_entidades__ri_rml` — las entidades · {"nivel": "propuesto", "cuarentena": "true", "colision_cross_to": "true", "padre_sugerido": "Sujeto_rol_entidad_comprendida_reginf", "padre_desde_sugerencia_modelo": "true"} · tramo: 
- **N18** TextoOrdenado `TextoOrdenado_ri_rml_pdf` — Régimen Informativo Contable Mensual · {"archivo": "ri_rml.pdf", "materia": "RI Cont. Mensual - Efectivo mínimo y aplicación de recursos", "version": "Comunicación A 8453 (vigencia 12/06/2026)"} · tramo: 
- **E1** (estructural) N1 —establecida_en→ N18 · {}
- **A1** (extraccion) N2 —aplica_a→ N17 · {}
- **E2** (estructural) N2 —establecida_en→ N18 · {}
- **A2** (extraccion) N3 —aplica_a→ N17 · {}
- **E3** (estructural) N3 —establecida_en→ N18 · {}
- **A3** (extraccion) N4 —aplica_a→ N17 · {}
- **E4** (estructural) N4 —establecida_en→ N18 · {}
- **A4** (extraccion) N5 —aplica_a→ N17 · {}
- **E5** (estructural) N5 —establecida_en→ N18 · {}
- **R1** (remision_derivada) N5 —remite_a→ Condicion_titulos_adquiridos_por_suscripcion_primaria_o_canje__la_integracion_de_la_exigen_a2210f · {"alcance": "externa", "destino": "efemin::1.3", "evidencia": "punto 1.3. de las normas sobre “Efectivo mínimo"}
- **R2** (remision_derivada) N5 —remite_a→ Excepcion_quedan_excluidos_de_la_integracion_los_titulos_publicos_nacionales_en_pesos_vinc_f7888c · {"alcance": "externa", "destino": "efemin::1.3", "evidencia": "punto 1.3. de las normas sobre “Efectivo mínimo"}
- **R3** (remision_derivada) N5 —remite_a→ Obligacion_deber_de_integrar_los_importes_de_efectivo_minimo_aplicando_tasas_diferenciadas__5065cd · {"alcance": "externa", "destino": "efemin::1.3", "evidencia": "punto 1.3. de las normas sobre “Efectivo mínimo"}
- **R4** (remision_derivada) N5 —remite_a→ Obligacion_integracion_de_los_importes_de_efectivo_minimo_mediante_aplicacion_de_tasas_dife_2d34ad · {"alcance": "externa", "destino": "efemin::1.3", "evidencia": "punto 1.3. de las normas sobre “Efectivo mínimo"}
- **R5** (remision_derivada) N5 —remite_a→ Obligacion_los_titulos_publicos_nacionales_en_pesos_leliq_y_o_nobac_admitidos_para_la_integ_0182cc · {"alcance": "externa", "destino": "efemin::1.3", "evidencia": "punto 1.3. de las normas sobre “Efectivo mínimo"}
- **R6** (remision_derivada) N5 —remite_a→ Obligacion_los_titulos_publicos_nacionales_en_pesos_leliq_y_o_nobac_admitidos_para_la_integ_0bbd4e · {"alcance": "externa", "destino": "efemin::1.3", "evidencia": "punto 1.3. de las normas sobre “Efectivo mínimo"}
- **R7** (remision_derivada) N5 —remite_a→ Operacion_integracion_de_efectivo_minimo_con_leliq_para_garantias_de_compensacion__efemin__850416 · {"alcance": "externa", "destino": "efemin::1.3", "evidencia": "punto 1.3. de las normas sobre “Efectivo mínimo"}
- **R8** (remision_derivada) N5 —remite_a→ Operacion_integracion_de_efectivo_minimo_con_titulos_publicos_nacionales__efemin_1_3_df70a8 · {"alcance": "externa", "destino": "efemin::1.3", "evidencia": "punto 1.3. de las normas sobre “Efectivo mínimo"}
- **R9** (remision_derivada) N5 —remite_a→ Restriccion_las_leliq_admitidas_para_la_integracion_de_la_exigencia_de_efectivo_minimo_en_pe_9965a0 · {"alcance": "externa", "destino": "efemin::1.3", "evidencia": "punto 1.3. de las normas sobre “Efectivo mínimo"}
- **A5** (extraccion) N6 —aplica_a→ N17 · {}
- **E6** (estructural) N6 —establecida_en→ N18 · {}
- **A6** (extraccion) N7 —aplica_a→ N17 · {}
- **E7** (estructural) N7 —establecida_en→ N18 · {}
- **A7** (extraccion) N8 —aplica_a→ N17 · {}
- **E8** (estructural) N8 —establecida_en→ N18 · {}
- **E9** (estructural) N9 —establecida_en→ N18 · {}
- **E10** (estructural) N10 —establecida_en→ N18 · {}
- **E11** (estructural) N11 —establecida_en→ N18 · {}
- **E12** (estructural) N12 —establecida_en→ N18 · {}
- **R10** (remision_derivada) N12 —remite_a→ Condicion_titulos_adquiridos_por_suscripcion_primaria_o_canje__la_integracion_de_la_exigen_a2210f · {"alcance": "externa", "destino": "efemin::1.3", "evidencia": "punto 1.3. de las normas sobre “Efectivo mínimo"}
- **R11** (remision_derivada) N12 —remite_a→ Excepcion_quedan_excluidos_de_la_integracion_los_titulos_publicos_nacionales_en_pesos_vinc_f7888c · {"alcance": "externa", "destino": "efemin::1.3", "evidencia": "punto 1.3. de las normas sobre “Efectivo mínimo"}
- **R12** (remision_derivada) N12 —remite_a→ Obligacion_deber_de_integrar_los_importes_de_efectivo_minimo_aplicando_tasas_diferenciadas__5065cd · {"alcance": "externa", "destino": "efemin::1.3", "evidencia": "punto 1.3. de las normas sobre “Efectivo mínimo"}
- **R13** (remision_derivada) N12 —remite_a→ Obligacion_integracion_de_los_importes_de_efectivo_minimo_mediante_aplicacion_de_tasas_dife_2d34ad · {"alcance": "externa", "destino": "efemin::1.3", "evidencia": "punto 1.3. de las normas sobre “Efectivo mínimo"}
- **R14** (remision_derivada) N12 —remite_a→ Obligacion_los_titulos_publicos_nacionales_en_pesos_leliq_y_o_nobac_admitidos_para_la_integ_0182cc · {"alcance": "externa", "destino": "efemin::1.3", "evidencia": "punto 1.3. de las normas sobre “Efectivo mínimo"}
- **R15** (remision_derivada) N12 —remite_a→ Obligacion_los_titulos_publicos_nacionales_en_pesos_leliq_y_o_nobac_admitidos_para_la_integ_0bbd4e · {"alcance": "externa", "destino": "efemin::1.3", "evidencia": "punto 1.3. de las normas sobre “Efectivo mínimo"}
- **R16** (remision_derivada) N12 —remite_a→ Operacion_integracion_de_efectivo_minimo_con_leliq_para_garantias_de_compensacion__efemin__850416 · {"alcance": "externa", "destino": "efemin::1.3", "evidencia": "punto 1.3. de las normas sobre “Efectivo mínimo"}
- **R17** (remision_derivada) N12 —remite_a→ Operacion_integracion_de_efectivo_minimo_con_titulos_publicos_nacionales__efemin_1_3_df70a8 · {"alcance": "externa", "destino": "efemin::1.3", "evidencia": "punto 1.3. de las normas sobre “Efectivo mínimo"}
- **R18** (remision_derivada) N12 —remite_a→ Restriccion_las_leliq_admitidas_para_la_integracion_de_la_exigencia_de_efectivo_minimo_en_pe_9965a0 · {"alcance": "externa", "destino": "efemin::1.3", "evidencia": "punto 1.3. de las normas sobre “Efectivo mínimo"}
- **E13** (estructural) N13 —establecida_en→ N18 · {}
- **E14** (estructural) N14 —establecida_en→ N18 · {}
- **E15** (estructural) N15 —establecida_en→ N18 · {}
- **E16** (estructural) N16 —establecida_en→ N18 · {}
- **C1** (catalogo_sujetos) N17 —padre_sugerido→ Sujeto_rol_entidad_comprendida_reginf · {"flag": "padre_sugerido_no_laudado"}

## 16. `nmcief::A2::S3::chapeau_seccion` — NG:sin_raiz · aceptadas:no_items

Texto que vio E3 (e0, bloque de lista True; págs. 18):

```
[encabezado | punto A2]
Anexo II
[encabezado | punto A2::S3]
3. Evaluación del control interno
[bloque chapeau_seccion | punto A2::S3]
La evaluación del control interno de los ciclos de la entidad deberá ser documentada con la
frecuencia que surja de la evaluación de riesgos realizada, ya sea a partir de su relevamiento
inicial o de sucesivas actualizaciones.
Tanto el relevamiento como la identificación, evaluación y prueba de los controles podrá ser
documentada mediante narrativos, flujogramas, cursogramas, matrices, cuestionarios u otra
forma que permita apreciar claramente el proceso seguido y los controles existentes.
Dicha documentación deberá estar preparada con el suficiente detalle de manera que permita
entender el propósito seguido, origen y conclusiones obtenidas. Deberá contener para cada
actividad de cada ciclo de la entidad una conclusión sobre el cumplimiento de los objetivos de
con trol definidos y, dado el caso, su efecto sobre la estructura de control. Dichas conclusiones
serán informadas en un informe por ciclo que se elevará al Comité de Auditoría.
```

Versión: final (grafo sin cola). Nodos 6, aristas 5.
- **N1** Obligacion `Obligacion_el_relevamiento_identificacion_evaluacion_y_prueba_de_los_controles_podra_ser_do_77c2c7` — Documentación de relevamiento, identificación, evaluación y prueba de controles · {"tipo": "presentacion_informativa", "descripcion": "El relevamiento, identificación, evaluación y prueba de los controles podrá ser documentada mediante narrativos, flujogramas, cursogramas, matrices, cuestionarios u otra forma que permita apreciar claramente el proceso seguido y los controles existentes."} · tramo: Tanto el relevamiento como la identificación, evaluación y prueba de los controles podrá ser documentada mediante narrativos, flujogramas, cursogramas, matrices, cuestionarios u otra forma que permita apreciar claramente el proceso seguido y los controles existentes
- **N2** Obligacion `Obligacion_la_documentacion_debera_contener_para_cada_actividad_de_cada_ciclo_de_la_entidad_3a3847` — Conclusión sobre cumplimiento de objetivos de control por ciclo · {"tipo": "presentacion_informativa", "descripcion": "La documentación deberá contener para cada actividad de cada ciclo de la entidad una conclusión sobre el cumplimiento de los objetivos de control definidos y, dado el caso, su efecto sobre la estructura de control."} · tramo: Deberá contener para cada actividad de cada ciclo de la entidad una conclusión sobre el cumplimiento de los objetivos de control definidos y, dado el caso, su efecto sobre la estructura de control
- **N3** Obligacion `Obligacion_la_documentacion_debera_estar_preparada_con_el_suficiente_detalle_de_manera_que__cc518e` — Preparación de documentación con suficiente detalle · {"tipo": "presentacion_informativa", "descripcion": "La documentación deberá estar preparada con el suficiente detalle de manera que permita entender el propósito seguido, origen y conclusiones obtenidas."} · tramo: Dicha documentación deberá estar preparada con el suficiente detalle de manera que permita entender el propósito seguido, origen y conclusiones obtenidas
- **N4** Obligacion `Obligacion_la_evaluacion_del_control_interno_de_los_ciclos_de_la_entidad_debera_ser_documen_e4cd14` — Documentación de evaluación del control interno · {"tipo": "presentacion_informativa", "descripcion": "La evaluación del control interno de los ciclos de la entidad deberá ser documentada con la frecuencia que surja de la evaluación de riesgos realizada, ya sea a partir de su relevamiento inicial o de sucesivas actualizaciones.", "umbrales": [{"tramo": "con la frecuencia que surja de la evaluación de riesgos realizada", "comparacion": "no_determi · tramo: La evaluación del control interno de los ciclos de la entidad deberá ser documentada con la frecuencia que surja de la evaluación de riesgos realizada
- **N5** Obligacion `Obligacion_las_conclusiones_seran_informadas_en_un_informe_por_ciclo_que_se_elevara_al_comi_d491a1` — Informe de conclusiones por ciclo al Comité de Auditoría · {"tipo": "reporte_al_supervisor", "descripcion": "Las conclusiones serán informadas en un informe por ciclo que se elevará al Comité de Auditoría."} · tramo: Dichas conclusiones serán informadas en un informe por ciclo que se elevará al Comité de Auditoría
- **N6** TextoOrdenado `TextoOrdenado_nmcief_pdf` — Normas de Capitales Mínimos · {"archivo": "nmcief.pdf", "materia": "Normas mínimas sobre controles internos para entidades financieras", "version": "Comunicación A 8168 (vigencia 01/01/2025)"} · tramo: 
- **E1** (estructural) N1 —establecida_en→ N6 · {}
- **E2** (estructural) N2 —establecida_en→ N6 · {}
- **E3** (estructural) N3 —establecida_en→ N6 · {}
- **E4** (estructural) N4 —establecida_en→ N6 · {}
- **E5** (estructural) N5 —establecida_en→ N6 · {}

## 17. `ceninf::4.1::intro` — NG:sin_raiz · aceptadas:no_items

Texto que vio E3 (e0, bloque de lista True; págs. 10):

```
[encabezado | punto S4]
Sección 4. Central de Deudores del Sistema Financiero.
[encabezado | punto 4.1]
4.1. Base de datos.
[bloque intro | punto 4.1]
La información se brindará mensualmente.
Residirá en el sitio seguro https://www3.bcra.gob.ar y quedará a disposición de los si-
guientes sujetos:
a. Entidades financieras.
b. Fiduciarios de fideicomisos financieros comprendidos en la Ley de Entida-
des Financieras.
c. Proveedores no financieros de crédito.
d. Administradores de carteras crediticias de ex – entidades financieras.
e. Sociedades de garantía recíproca y fondos de garantía de carácter público
inscriptos en los Registros habilitados en el Banco Central de la República
Argentina.
f. Proveedores de servicios de créditos entre particulares a través de plata-
formas.
Asimismo, este mecanismo de consulta estará disponible para el público en general
ingresando a través de la clave de ARCA.
Aquellos que seleccionen esta opción, deberán prestar declaración jurada respecto
del conocimiento de las disposiciones y sanciones previstas en la Ley de Protección
de los datos Personales –incluyendo el deber de inscripción ante el Registro Nacional
de Base de Datos, en los casos que corresponda.
```

Versión: final (grafo sin cola). Nodos 12, aristas 13.
- **N1** Obligacion `Obligacion_deber_de_prestar_declaracion_jurada_sobre_conocimiento_de_disposiciones_y_sancio_b02194` — Declaración jurada — acceso público a base de datos · {"tipo": "presentacion_informativa", "descripcion": "Deber de prestar declaración jurada sobre conocimiento de disposiciones y sanciones de la Ley de Protección de Datos Personales, incluyendo inscripción ante el Registro Nacional de Base de Datos cuando corresponda"} · tramo: Aquellos que seleccionen esta opción, deberán prestar declaración jurada respecto del conocimiento de las disposiciones y sanciones previstas en la Ley de Protección de los datos Personales –incluyendo el deber de inscripción ante el Registro Nacional de Base de Datos, en los casos que corresponda.
- **N2** Obligacion `Obligacion_informacion_mensual_base_de_datos__ceninf_4_1_9adb78` — Información mensual — Base de datos · {"tipo": "presentacion_informativa", "frecuencia": "mensual"} · tramo: La información se brindará mensualmente.
- **N3** Operacion `Operacion_acceso_a_base_de_datos_en_sitio_seguro__ceninf_4_1_78aec0` — Acceso a base de datos en sitio seguro · {"tipo": "acceso a información", "descripcion": "Acceso a la base de datos de la Central de Deudores en sitio seguro del BCRA"} · tramo: Residirá en el sitio seguro https://www3.bcra.gob.ar y quedará a disposición de los siguientes sujetos
- **N4** Sujeto `Sujeto_entidad_financiera` — Entidades financieras · {"nivel": "clase", "alias": ["Entidades financieras emisoras de tarjetas de crédito y/o compra", "Entidad financiera emisora de tarjetas de crédito y/o compra"]} · tramo: 
- **N5** Sujeto `Sujeto_fiduciario_de_fideicomiso_financiero` — Fiduciarios de fideicomisos financieros · {"nivel": "clase"} · tramo: 
- **N6** Sujeto `Sujeto_fondo_de_garantia_publico` — Fondos de garantía de carácter público · {"nivel": "clase"} · tramo: 
- **N7** Sujeto `Sujeto_propuesto_administradores_de_carteras_crediticias_de_ex_entidades_financieras` — Administradores de carteras crediticias de ex – entidades financieras · {"nivel": "propuesto", "cuarentena": "true", "padre_sugerido": "Sujeto_sujeto_regulado"} · tramo: 
- **N8** Sujeto `Sujeto_propuesto_el_publico_en_general` — el público en general · {"nivel": "propuesto", "cuarentena": "true", "padre_sugerido": "Sujeto_contraparte"} · tramo: 
- **N9** Sujeto `Sujeto_proveedor_no_financiero_de_credito` — Proveedores no financieros de crédito · {"nivel": "clase", "alias": ["PNFC"]} · tramo: 
- **N10** Sujeto `Sujeto_pscpp` — Proveedores de servicios de créditos entre particulares a través de plataformas (PSCPP) · {"nivel": "clase", "alias": ["PSCPP"]} · tramo: 
- **N11** Sujeto `Sujeto_sociedad_de_garantia_reciproca` — Sociedades de garantía recíproca · {"nivel": "clase", "alias": ["SGR"]} · tramo: 
- **N12** TextoOrdenado `TextoOrdenado_ceninf_pdf` — Centrales de Información · {"archivo": "ceninf.pdf", "materia": "Centrales de información", "version": "Comunicación A 8393 (vigencia 01/03/2026)"} · tramo: 
- **A1** (extraccion) N1 —aplica_a→ N8 · {}
- **E1** (estructural) N1 —establecida_en→ N12 · {}
- **E2** (estructural) N2 —establecida_en→ N12 · {}
- **A2** (extraccion) N3 —aplica_a→ N4 · {}
- **A3** (extraccion) N3 —aplica_a→ N5 · {}
- **A4** (extraccion) N3 —aplica_a→ N6 · {}
- **A5** (extraccion) N3 —aplica_a→ N7 · {}
- **A6** (extraccion) N3 —aplica_a→ N9 · {}
- **A7** (extraccion) N3 —aplica_a→ N10 · {}
- **A8** (extraccion) N3 —aplica_a→ N11 · {}
- **E3** (estructural) N3 —establecida_en→ N12 · {}
- **C1** (catalogo_sujetos) N7 —padre_sugerido→ Sujeto_sujeto_regulado · {"flag": "padre_sugerido_no_laudado"}
- **C2** (catalogo_sujetos) N8 —padre_sugerido→ Sujeto_contraparte · {"flag": "padre_sugerido_no_laudado"}

## 18. `nmcief::A2::3.2::intro` — NG:sin_raiz · aceptadas:no_items

Texto que vio E3 (e0, bloque de lista True; págs. 19):

```
[encabezado | punto A2]
Anexo II
[encabezado | punto A2::S3]
3. Evaluación del control interno
[encabezado | punto A2::3.2]
3.2 Relevamiento de los ciclos.
[bloque intro | punto A2::3.2]
Los relevamientos deberán contener claramente el flujo de la transacción y el ambiente de
sistemas en el cual operan las transacciones identificándose los riesgos existentes para
cada uno de los seis objetivos de control mencionados precedentemente y los controles
implementados por la entidad.
A efectos de un adecuado análisis y documentación de la estructura de control interno de
las entidades, se debe cumplir, en lo que se relaciona con cada ciclo, como mínimo con las
siguientes etapas y aspectos de relevamiento y evaluación:
```

Versión: final (grafo sin cola). Nodos 5, aristas 5.
- **N1** Obligacion `Obligacion_a_efectos_de_un_adecuado_analisis_y_documentacion_de_la_estructura_de_control_in_8bb18e` — Cumplimiento de etapas y aspectos de relevamiento y evaluación por ciclo · {"tipo": "otra", "descripcion": "A efectos de un adecuado análisis y documentación de la estructura de control interno de las entidades, se debe cumplir, en lo que se relaciona con cada ciclo, como mínimo con las siguientes etapas y aspectos de relevamiento y evaluación."} · tramo: se debe cumplir, en lo que se relaciona con cada ciclo, como mínimo con las siguientes etapas y aspectos de relevamiento y evaluación
- **N2** Obligacion `Obligacion_los_relevamientos_deberan_contener_claramente_el_flujo_de_la_transaccion_y_el_am_8c298d` — Relevamientos con flujo de transacción y ambiente de sistemas · {"tipo": "otra", "descripcion": "Los relevamientos deberán contener claramente el flujo de la transacción y el ambiente de sistemas en el cual operan las transacciones, identificándose los riesgos existentes para cada uno de los seis objetivos de control mencionados precedentemente y los controles implementados por la entidad."} · tramo: Los relevamientos deberán contener claramente el flujo de la transacción y el ambiente de sistemas en el cual operan las transacciones identificándose los riesgos existentes para cada uno de los seis objetivos de control mencionados precedentemente y los controles implementados por la entidad.
- **N3** Sujeto `Sujeto_entidad_financiera` — Entidades financieras · {"nivel": "clase", "alias": ["Entidades financieras emisoras de tarjetas de crédito y/o compra", "Entidad financiera emisora de tarjetas de crédito y/o compra"]} · tramo: 
- **N4** Sujeto `Sujeto_propuesto_las_entidades__nmcief` — Las entidades · {"nivel": "propuesto", "cuarentena": "true", "colision_cross_to": "true", "padre_sugerido": "Sujeto_entidad_financiera", "padre_desde_sugerencia_modelo": "true"} · tramo: 
- **N5** TextoOrdenado `TextoOrdenado_nmcief_pdf` — Normas de Capitales Mínimos · {"archivo": "nmcief.pdf", "materia": "Normas mínimas sobre controles internos para entidades financieras", "version": "Comunicación A 8168 (vigencia 01/01/2025)"} · tramo: 
- **A1** (extraccion) N1 —aplica_a→ N4 · {}
- **E1** (estructural) N1 —establecida_en→ N5 · {}
- **A2** (extraccion) N2 —aplica_a→ N3 · {}
- **E2** (estructural) N2 —establecida_en→ N5 · {}
- **C1** (catalogo_sujetos) N4 —padre_sugerido→ N3 · {"flag": "padre_sugerido_no_laudado"}

## 19. `nmcief::A4::S0::chapeau_seccion` — NG:sin_raiz · aceptadas:no_items

Texto que vio E3 (e0, bloque de lista True; págs. 25):

```
[encabezado | punto A4::S0]
Anexo IV
[bloque chapeau_seccion | punto A4::S0]
DOCUMENTACIÓN E INFORMES DE AUDITORÍA INTERNA
```

Versión: final (grafo sin cola). Nodos 1, aristas 0.
- **N1** TextoOrdenado `TextoOrdenado_nmcief_pdf` — Normas de Capitales Mínimos · {"archivo": "nmcief.pdf", "materia": "Normas mínimas sobre controles internos para entidades financieras", "version": "Comunicación A 8168 (vigencia 01/01/2025)"} · tramo: 

## 20. `ceninf::4.1.3` — NG:sin_raiz · aceptadas:no_items

Texto que vio E3 (e0, bloque de lista True; págs. 15):

```
[encabezado | punto S4]
Sección 4. Central de Deudores del Sistema Financiero.
[encabezado | punto 4.1]
4.1. Base de datos.
[texto propio | punto 4.1.3]
4.1.3. El diseño que contiene la Fecha desde la cual el deudor se encuentra en situación
1 (normal) de acuerdo con las siguientes pautas, es el detallado a continuación:
(cid:252) Se difundirá este dato respecto de los deudores que en la última Central de
Deudores se encuentren en situación 1 en todas las entidades.
(cid:252) La fecha de origen será la primera desde la cual el deudor registre situación 1
en todas las entidades informantes en forma ininterrumpida, sin perjuicio de
que existiera algún período intermedio donde no hubiera sido incluido en la
Central de Deudores.
La información podrá ser descargada en archivos comprimidos denominados
1DSFAAAAMM.
[TABLA ceninf::tabla011 | página 15 | e0_tablas | columnas]
Columnas: Nº Campo | Nombre | Tipo | Long. | Observaciones
Fila 1: Nº Campo = 1 | Nombre = Tipo de identifica- ción | Tipo = Numérico | Long. = 2 | Observaciones = Tipo de identificación (punto 2.1 del apartado A del T.O.).
Fila 2: Nº Campo = 2 | Nombre = N° de identifica- ción | Tipo = Carácter | Long. = 11 | Observaciones = Número de identificación (punto 2.2 del apartado A del T.O.).
Fila 3: Nº Campo = 3 | Nombre = Fecha de origen situación 1 | Tipo = Numérico | Long. = 6 | Observaciones = AAAAMM
[FIN TABLA ceninf::tabla011]
```

Versión: final (grafo sin cola). Nodos 5, aristas 24.
- **N1** Definicion `Definicion_fecha_de_origen_situacion_1__primera_fecha_desde_la_cual_el_deudor_registra_situ_4266a0` — Fecha de origen situación 1 · {"termino": "Fecha de origen situación 1", "descripcion": "Primera fecha desde la cual el deudor registra situación 1 en todas las entidades informantes en forma ininterrumpida, sin perjuicio de períodos intermedios donde no hubiera sido incluido en la Central de Deudores."} · tramo: La fecha de origen será la primera desde la cual el deudor registre situación 1 en todas las entidades informantes en forma ininterrumpida, sin perjuicio de que existiera algún período intermedio donde no hubiera sido incluido en la Central de Deudores.
- **N2** Operacion `Operacion_descarga_de_informacion_en_archivos_comprimidos__ceninf_4_1_3_33bcb4` — Descarga de información en archivos comprimidos · {"tipo": "descarga de datos", "descripcion": "La información podrá ser descargada en archivos comprimidos con denominación 1DSFAAAAMM."} · tramo: La información podrá ser descargada en archivos comprimidos denominados 1DSFAAAAMM.
- **N3** Operacion `Operacion_difusion_de_fecha_origen_situacion_1__ceninf_4_1_3_e1b814` — Difusión de fecha origen situación 1 · {"tipo": "presentación informativa", "descripcion": "Difusión del dato de fecha de origen de situación 1 para deudores que se encuentren en situación 1 en todas las entidades en la última Central de Deudores."} · tramo: Se difundirá este dato respecto de los deudores que en la última Central de Deudores se encuentren en situación 1 en todas las entidades.
- **N4** Potestad `Potestad_facultad_de_descargar_informacion_en_archivos_comprimidos__facultad_de_descargar_fd0d04` — Facultad de descargar información en archivos comprimidos · {"descripcion": "Facultad de descargar la información en archivos comprimidos denominados 1DSFAAAAMM."} · tramo: La información podrá ser descargada en archivos comprimidos denominados 1DSFAAAAMM.
- **N5** TextoOrdenado `TextoOrdenado_ceninf_pdf` — Centrales de Información · {"archivo": "ceninf.pdf", "materia": "Centrales de información", "version": "Comunicación A 8393 (vigencia 01/03/2026)"} · tramo: 
- **E1** (estructural) N1 —establecida_en→ N5 · {}
- **R1** (remision_derivada) N1 —remite_a→ Obligacion_la_pagina_de_internet_sera_actualizada_diariamente__ceninf_2_1_5938cd · {"alcance": "interna", "destino": "ceninf::2.1", "evidencia": "Numérico | Long. = 2 | Observaciones = Tipo de identificación (punto 2.1 del apartado A del"}
- **R2** (remision_derivada) N1 —remite_a→ Obligacion_se_informaran_los_siguientes_datos_entidad_bancaria_numero_de_sucursal_numero_de_9b7c91 · {"alcance": "interna", "destino": "ceninf::2.1", "evidencia": "Numérico | Long. = 2 | Observaciones = Tipo de identificación (punto 2.1 del apartado A del"}
- **R3** (remision_derivada) N1 —remite_a→ Operacion_consulta_puntual_de_cheques_por_internet__ceninf_2_1_1dd728 · {"alcance": "interna", "destino": "ceninf::2.1", "evidencia": "Numérico | Long. = 2 | Observaciones = Tipo de identificación (punto 2.1 del apartado A del"}
- **R4** (remision_derivada) N1 —remite_a→ Potestad_disponibilidad_publica_del_mecanismo_de_consulta__el_mecanismo_de_consulta_estar_ad1df9 · {"alcance": "interna", "destino": "ceninf::2.1", "evidencia": "Numérico | Long. = 2 | Observaciones = Tipo de identificación (punto 2.1 del apartado A del"}
- **R5** (remision_derivada) N1 —remite_a→ Restriccion_no_se_debera_utilizar_el_mecanismo_de_consulta_para_extraer_datos_en_forma_masiv_99625d · {"alcance": "interna", "destino": "ceninf::2.1", "evidencia": "Numérico | Long. = 2 | Observaciones = Tipo de identificación (punto 2.1 del apartado A del"}
- **E2** (estructural) N2 —establecida_en→ N5 · {}
- **R6** (remision_derivada) N2 —remite_a→ Obligacion_la_pagina_de_internet_sera_actualizada_diariamente__ceninf_2_1_5938cd · {"alcance": "interna", "destino": "ceninf::2.1", "evidencia": "Numérico | Long. = 2 | Observaciones = Tipo de identificación (punto 2.1 del apartado A del"}
- **R7** (remision_derivada) N2 —remite_a→ Obligacion_se_informaran_los_siguientes_datos_entidad_bancaria_numero_de_sucursal_numero_de_9b7c91 · {"alcance": "interna", "destino": "ceninf::2.1", "evidencia": "Numérico | Long. = 2 | Observaciones = Tipo de identificación (punto 2.1 del apartado A del"}
- **R8** (remision_derivada) N2 —remite_a→ Operacion_consulta_puntual_de_cheques_por_internet__ceninf_2_1_1dd728 · {"alcance": "interna", "destino": "ceninf::2.1", "evidencia": "Numérico | Long. = 2 | Observaciones = Tipo de identificación (punto 2.1 del apartado A del"}
- **R9** (remision_derivada) N2 —remite_a→ Potestad_disponibilidad_publica_del_mecanismo_de_consulta__el_mecanismo_de_consulta_estar_ad1df9 · {"alcance": "interna", "destino": "ceninf::2.1", "evidencia": "Numérico | Long. = 2 | Observaciones = Tipo de identificación (punto 2.1 del apartado A del"}
- **R10** (remision_derivada) N2 —remite_a→ Restriccion_no_se_debera_utilizar_el_mecanismo_de_consulta_para_extraer_datos_en_forma_masiv_99625d · {"alcance": "interna", "destino": "ceninf::2.1", "evidencia": "Numérico | Long. = 2 | Observaciones = Tipo de identificación (punto 2.1 del apartado A del"}
- **E3** (estructural) N3 —establecida_en→ N5 · {}
- **R11** (remision_derivada) N3 —remite_a→ Obligacion_la_pagina_de_internet_sera_actualizada_diariamente__ceninf_2_1_5938cd · {"alcance": "interna", "destino": "ceninf::2.1", "evidencia": "Numérico | Long. = 2 | Observaciones = Tipo de identificación (punto 2.1 del apartado A del"}
- **R12** (remision_derivada) N3 —remite_a→ Obligacion_se_informaran_los_siguientes_datos_entidad_bancaria_numero_de_sucursal_numero_de_9b7c91 · {"alcance": "interna", "destino": "ceninf::2.1", "evidencia": "Numérico | Long. = 2 | Observaciones = Tipo de identificación (punto 2.1 del apartado A del"}
- **R13** (remision_derivada) N3 —remite_a→ Operacion_consulta_puntual_de_cheques_por_internet__ceninf_2_1_1dd728 · {"alcance": "interna", "destino": "ceninf::2.1", "evidencia": "Numérico | Long. = 2 | Observaciones = Tipo de identificación (punto 2.1 del apartado A del"}
- **R14** (remision_derivada) N3 —remite_a→ Potestad_disponibilidad_publica_del_mecanismo_de_consulta__el_mecanismo_de_consulta_estar_ad1df9 · {"alcance": "interna", "destino": "ceninf::2.1", "evidencia": "Numérico | Long. = 2 | Observaciones = Tipo de identificación (punto 2.1 del apartado A del"}
- **R15** (remision_derivada) N3 —remite_a→ Restriccion_no_se_debera_utilizar_el_mecanismo_de_consulta_para_extraer_datos_en_forma_masiv_99625d · {"alcance": "interna", "destino": "ceninf::2.1", "evidencia": "Numérico | Long. = 2 | Observaciones = Tipo de identificación (punto 2.1 del apartado A del"}
- **E4** (estructural) N4 —establecida_en→ N5 · {}
- **R16** (remision_derivada) N4 —remite_a→ Obligacion_la_pagina_de_internet_sera_actualizada_diariamente__ceninf_2_1_5938cd · {"alcance": "interna", "destino": "ceninf::2.1", "evidencia": "Numérico | Long. = 2 | Observaciones = Tipo de identificación (punto 2.1 del apartado A del"}
- **R17** (remision_derivada) N4 —remite_a→ Obligacion_se_informaran_los_siguientes_datos_entidad_bancaria_numero_de_sucursal_numero_de_9b7c91 · {"alcance": "interna", "destino": "ceninf::2.1", "evidencia": "Numérico | Long. = 2 | Observaciones = Tipo de identificación (punto 2.1 del apartado A del"}
- **R18** (remision_derivada) N4 —remite_a→ Operacion_consulta_puntual_de_cheques_por_internet__ceninf_2_1_1dd728 · {"alcance": "interna", "destino": "ceninf::2.1", "evidencia": "Numérico | Long. = 2 | Observaciones = Tipo de identificación (punto 2.1 del apartado A del"}
- **R19** (remision_derivada) N4 —remite_a→ Potestad_disponibilidad_publica_del_mecanismo_de_consulta__el_mecanismo_de_consulta_estar_ad1df9 · {"alcance": "interna", "destino": "ceninf::2.1", "evidencia": "Numérico | Long. = 2 | Observaciones = Tipo de identificación (punto 2.1 del apartado A del"}
- **R20** (remision_derivada) N4 —remite_a→ Restriccion_no_se_debera_utilizar_el_mecanismo_de_consulta_para_extraer_datos_en_forma_masiv_99625d · {"alcance": "interna", "destino": "ceninf::2.1", "evidencia": "Numérico | Long. = 2 | Observaciones = Tipo de identificación (punto 2.1 del apartado A del"}

## 21. `expaef::6.4` — NG:resto · aceptadas:no_items

Texto que vio E3 (e0, bloque de lista True; págs. 18):

```
[encabezado | punto S6]
Sección 6. Participación en entidades financieras del exterior.
[texto propio | punto 6.4]
6.4. Resolución.
La SEFyC ponderará las características de cada proyecto y considerará la oportunidad y con-
veniencia de acceder o no a los pedidos de autorización.
Las solicitudes se considerarán conformadas una vez transcurridos 120 (ciento veinte) días
desde que se verifiquen las condiciones establecidas en el punto 6.5. si la SEFyC no manifes-
tare oposición. No obstante, dicho plazo podrá ser extendido si mediaren circunstancias que
impidieran adoptar resolución.
```

Versión: final (grafo sin cola). Nodos 8, aristas 11.
- **N1** Condicion `Condicion_ausencia_de_oposicion_de_la_sefyc__el_supuesto_de_que_la_sefyc_no_haya_manifesta_e27d38` — Ausencia de oposición de la SEFyC · {"descripcion": "El supuesto de que la SEFyC no haya manifestado oposición."} · tramo: si la SEFyC no manifestare oposición
- **N2** Condicion `Condicion_existencia_de_circunstancias_que_impidan_adoptar_resolucion__el_supuesto_de_que__45d7f4` — Existencia de circunstancias que impidan adoptar resolución · {"descripcion": "El supuesto de que existan circunstancias que impidan adoptar resolución."} · tramo: si mediaren circunstancias que impidieran adoptar resolución
- **N3** Condicion `Condicion_transcurso_de_120_dias_desde_verificacion_de_condiciones__el_supuesto_de_que_hay_4ce35e` — Transcurso de 120 días desde verificación de condiciones · {"descripcion": "El supuesto de que hayan transcurrido 120 días desde la verificación de las condiciones establecidas en el punto 6.5.", "umbrales": [{"tramo": "120 (ciento veinte) días", "valor": "120", "unidad": "dias", "comparacion": "no_determinada", "regla_comparacion": "sin_marcador_plazo", "origen": "e1", "tramo_verificado": "exacta"}]} · tramo: una vez transcurridos 120 (ciento veinte) días desde que se verifiquen las condiciones establecidas en el punto 6.5
- **N4** Operacion `Operacion_conformacion_de_solicitudes_de_autorizacion__expaef_6_4_249cb6` — Conformación de solicitudes de autorización · {"tipo": "Conformación de solicitud", "descripcion": "Las solicitudes de autorización se consideran conformadas una vez transcurridos 120 días desde la verificación de las condiciones del punto 6.5, si la SEFyC no ha manifestado oposición."} · tramo: Las solicitudes se considerarán conformadas
- **N5** Potestad `Potestad_extension_del_plazo_por_circunstancias_que_impidan_resolucion__la_sefyc_tiene_la_aca4bf` — Extensión del plazo por circunstancias que impidan resolución · {"descripcion": "La SEFyC tiene la facultad de extender el plazo de 120 días si existen circunstancias que impidan adoptar resolución."} · tramo: dicho plazo podrá ser extendido si mediaren circunstancias que impidieran adoptar resolución
- **N6** Potestad `Potestad_ponderacion_de_caracteristicas_y_oportunidad_de_autorizacion__la_sefyc_tiene_la__39b425` — Ponderación de características y oportunidad de autorización · {"descripcion": "La SEFyC tiene la facultad de ponderar las características de cada proyecto y considerar la oportunidad y conveniencia de acceder o no a los pedidos de autorización."} · tramo: La SEFyC ponderará las características de cada proyecto y considerará la oportunidad y conveniencia de acceder o no a los pedidos de autorización.
- **N7** Sujeto `Sujeto_sefyc` — SEFyC (Superintendencia de Entidades Financieras y Cambiarias) · {"nivel": "instancia", "alias": ["Superintendencia de Entidades Financieras y Cambiarias"], "instancia_de": "Sujeto_organismo_publico", "parte_de": "Sujeto_bcra"} · tramo: 
- **N8** TextoOrdenado `TextoOrdenado_expaef_pdf` — Autorización de sucursales · {"archivo": "expaef.pdf", "materia": "Expansión de entidades financieras", "version": "Comunicación A 8401 (vigencia 06/02/2026)"} · tramo: 
- **A1** (extraccion) N1 —condicion_de→ N4 · {}
- **E1** (estructural) N1 —establecida_en→ N8 · {}
- **A2** (extraccion) N2 —condicion_de→ N5 · {}
- **E2** (estructural) N2 —establecida_en→ N8 · {}
- **A3** (extraccion) N3 —condicion_de→ N4 · {}
- **E3** (estructural) N3 —establecida_en→ N8 · {}
- **E4** (estructural) N4 —establecida_en→ N8 · {}
- **A4** (extraccion) N5 —aplica_a→ N7 · {}
- **E5** (estructural) N5 —establecida_en→ N8 · {}
- **A5** (extraccion) N6 —aplica_a→ N7 · {}
- **E6** (estructural) N6 —establecida_en→ N8 · {}

## 22. `lingeef::4.3.5::intro` — NG:resto · aceptadas:no_items

Texto que vio E3 (e0, bloque de lista True; págs. 78, 79):

```
[encabezado | punto S4]
Sección 4. Gestión del riesgo de mercado.
[encabezado | punto 4.3]
4.3. Proceso de gestión del riesgo de mercado.
[encabezado | punto 4.3.5]
4.3.5. Planificación para la contingencia.
[bloque intro | punto 4.3.5]
Las entidades financieras deben tener un plan de contingencias que establezca clara-
mente la estrategia para afrontar situaciones de emergencia.
El plan de contingencia debe:
```

Versión: final (grafo sin cola). Nodos 4, aristas 4.
- **N1** Obligacion `Obligacion_las_entidades_financieras_deben_tener_un_plan_de_contingencias_que_establezca_cl_3674b1` — Tener plan de contingencias · {"tipo": "otra", "descripcion": "Las entidades financieras deben tener un plan de contingencias que establezca claramente la estrategia para afrontar situaciones de emergencia"} · tramo: Las entidades financieras deben tener un plan de contingencias que establezca claramente la estrategia para afrontar situaciones de emergencia
- **N2** Operacion `Operacion_plan_de_contingencias__lingeef_4_3_5_842b9a` — Plan de contingencias · {"tipo": "Planificación", "descripcion": "Plan de contingencias que establezca claramente la estrategia para afrontar situaciones de emergencia"} · tramo: plan de contingencias que establezca claramente la estrategia para afrontar situaciones de emergencia
- **N3** Sujeto `Sujeto_entidad_financiera` — Entidades financieras · {"nivel": "clase", "alias": ["Entidades financieras emisoras de tarjetas de crédito y/o compra", "Entidad financiera emisora de tarjetas de crédito y/o compra"]} · tramo: 
- **N4** TextoOrdenado `TextoOrdenado_lingeef_pdf` — Lineamientos para la gestión de riesgos · {"archivo": "lingeef.pdf", "materia": "Lineamientos para la gestión de riesgos en las entidades financieras", "version": "Comunicación A 8463 (vigencia 01/08/2026)"} · tramo: 
- **A1** (extraccion) N1 —aplica_a→ N3 · {}
- **E1** (estructural) N1 —establecida_en→ N4 · {}
- **E2** (estructural) N2 —establecida_en→ N4 · {}
- **A2** (extraccion) N2 —requiere→ N1 · {}

## 23. `cajasc::7.5` — NG:resto · aceptadas:no_items

Texto que vio E3 (e0, bloque de lista True; págs. 44):

```
[encabezado | punto S7]
Sección 7. Fraccionamiento del crédito.
[texto propio | punto 7.5]
7.5. Incumplimientos.
Los excesos a los límites fijados estarán sujetos a las disposiciones establecidas con carácter
general en las normas sobre “Incumplimientos de capitales mínimos y relaciones técnicas. Cri-
terios aplicables”.
```

Versión: final (grafo sin cola). Nodos 2, aristas 1.
- **N1** Restriccion `Restriccion_los_excesos_a_los_limites_fijados_en_materia_de_fraccionamiento_del_credito_esta_3e776e` — Excesos a límites de fraccionamiento · {"tipo": "limite_cuantitativo", "descripcion": "Los excesos a los límites fijados en materia de fraccionamiento del crédito están sujetos a las disposiciones sobre incumplimientos de capitales mínimos y relaciones técnicas."} · tramo: Los excesos a los límites fijados estarán sujetos a las disposiciones establecidas con carácter general en las normas sobre "Incumplimientos de capitales mínimos y relaciones técnicas. Criterios aplicables".
- **N2** TextoOrdenado `TextoOrdenado_cajasc_pdf` — Cajas de crédito cooperativas · {"archivo": "cajasc.pdf", "materia": "Cajas de Crédito Cooperativas (Ley 26.173)", "version": "Comunicación A 7083 (vigencia 07/08/2020)"} · tramo: 
- **E1** (estructural) N1 —establecida_en→ N2 · {}

## 24. `depaho::3.1.9.4` — NG:resto · aceptadas:no_items

Texto que vio E3 (e0, bloque de lista True; págs. 24):

```
[encabezado | punto S3]
Sección 3. Especiales.
[encabezado | punto 3.1]
3.1. Fondo de Cese Laboral para los Trabajadores de la Industria de la Construcción.
[encabezado | punto 3.1.9]
3.1.9. Otras disposiciones.
[texto propio | punto 3.1.9.4]
3.1.9.4. Se especificará la situación de la cuenta frente al sistema de seguro de garan-
tía de los depósitos conforme a lo establecido en el punto 6. del TO sobre Apli-
cación del Sistema de Seguro de Garantía de los Depósitos.
```

Versión: final (grafo sin cola). Nodos 3, aristas 2.
- **N1** Comunicacion `Comunicacion_to_sobre_aplicacion_del_sistema_de_seguro_de_garantia_de_los_depositos` — TO Aplicación del Sistema de Seguro de Garantía de los Depósitos · {"codigo": "TO sobre Aplicación del Sistema de Seguro de Garantía de los Depósitos"} · tramo: TO sobre Aplicación del Sistema de Seguro de Garantía de los Depósitos
- **N2** Obligacion `Obligacion_se_especificara_la_situacion_de_la_cuenta_frente_al_sistema_de_seguro_de_garanti_f29365` — Especificar situación de cuenta frente a seguro de garantía · {"descripcion": "Se especificará la situación de la cuenta frente al sistema de seguro de garantía de los depósitos conforme a lo establecido en el punto 6. del TO sobre Aplicación del Sistema de Seguro de Garantía de los Depósitos.", "tipo": "otra"} · tramo: Se especificará la situación de la cuenta frente al sistema de seguro de garantía de los depósitos
- **N3** TextoOrdenado `TextoOrdenado_depaho_pdf` — Depósitos de ahorro · {"archivo": "depaho.pdf", "materia": "Depósitos de ahorro, cuenta sueldo y especiales", "version": "Comunicación A 8444 (vigencia 05/06/2026)"} · tramo: 
- **E1** (estructural) N2 —establecida_en→ N3 · {}
- **E2** (estructural) N3 —referencia→ N1 · {}

## 25. `depaho::3.15::intro` — NG:resto · aceptadas:no_items

Texto que vio E3 (e0, bloque de lista True; págs. 60):

```
[encabezado | punto S3]
Sección 3. Especiales.
[encabezado | punto 3.15]
3.15. Cuenta especial para el régimen de fomento de la economía del conocimiento. Decreto
N° 679/22.
[bloque intro | punto 3.15]
Las entidades financieras del Grupo “A” –según lo previsto en la Sección 4. de las normas so-
bre “Autoridades de entidades financieras”– deberán abrir estas cuentas, conforme a lo si-
guiente:
```

Versión: final (grafo sin cola). Nodos 3, aristas 2.
- **N1** Obligacion `Obligacion_las_entidades_financieras_del_grupo_a_deberan_abrir_cuentas_especiales_para_el_r_9bee24` — Apertura de cuentas especiales — economía del conocimiento · {"descripcion": "Las entidades financieras del Grupo \"A\" deberán abrir cuentas especiales para el régimen de fomento de la economía del conocimiento, conforme a lo siguiente.", "tipo": "otra"} · tramo: deberán abrir estas cuentas, conforme a lo siguiente:
- **N2** Sujeto `Sujeto_rol_alcance_depaho` — Entidades intervinientes (Depósitos de ahorro) · {"nivel": "rol"} · tramo: 
- **N3** TextoOrdenado `TextoOrdenado_depaho_pdf` — Depósitos de ahorro · {"archivo": "depaho.pdf", "materia": "Depósitos de ahorro, cuenta sueldo y especiales", "version": "Comunicación A 8444 (vigencia 05/06/2026)"} · tramo: 
- **A1** (extraccion) N1 —aplica_a→ N2 · {}
- **E1** (estructural) N1 —establecida_en→ N3 · {}

## 26. `cirmo3::5.4.2` — NG:resto · aceptadas:no_items

Texto que vio E3 (e0, bloque de lista True; págs. 40, 41):

```
[encabezado | punto S5]
Sección 5. Gestión sobre el numerario.
[encabezado | punto 5.4]
5.4. Pagos.
[texto propio | punto 5.4.2]
5.4.2. Entrega de monedas
Con el fin de cumplir con el abastecimiento de metálico en CABA e interior del país, se
atenderán los requerimientos que realicen las entidades financieras a través de un cro-
nograma de pagos.
Las entidades financieras que requieran monedas realizarán su pedido a la casilla gené-
rica operaciones.monedas@bcra.gob.ar, con una semana de anticipación a la Gerencia
de Operaciones de Tesoro en el horario de 10:00 a 15:00. Las mismas deberán atender
las especificaciones indicadas por el BCRA en cuanto a su acondicionamiento en tam-
bores, cantidad total y por bolsas, diseño y denominación.
Una vez realizados los pedidos y autorizado el cronograma de pagos concertado con la
Gerencia de Operaciones de Emisión se informará a las entidades requirentes las canti-
dades asignadas, la fecha, horario y el lugar de entrega del metálico.
El día asignado para el retiro, las entidades financieras cursarán la solicitud de provisión
de monedas mediante débito en su cuenta corriente por medio del sistema MEP.
Los requerimientos vía MEP de las entidades deberán coincidir con lo solicitado y asig-
nado oportunamente por el BCRA.
El horario dispuesto para la remisión del débito MEP es de 8:00 a 10:00, caso contrario,
no se realizará el pago, debiéndose asignar a la entidad una nueva fecha de entrega.
El pago de monedas se realizará en el lugar donde el BCRA determine tanto en CABA
como en el interior del país, siendo un tambor la unidad menor de medida.
Los tambores para provisión de metálico a las entidades financieras serán acondiciona-
dos con monedas nuevas, salvo que el BCRA decida otro estado para su entrega, acon-
dicionadas por valor y diseño.
Las entidades financieras y las transportadoras de valores controlarán el contenido de
los tambores mediante el trasvasado de bolsas, en presencia de veedores antes de su
retiro.
Las entidades financieras que necesiten, en determinadas épocas del año, cantidades
de monedas por encima de sus necesidades normales, deberán realizar planes de pro-
visión anticipada y paulatina, para evitar los inconvenientes del movimiento de una gran
masa de numerario en uno o varios días.
```

Versión: final (grafo sin cola). Nodos 15, aristas 23.
- **N1** Condicion `Condicion_estado_de_acondicionamiento_de_tambores__los_tambores_se_acondicionan_con_moneda_e48bb3` — Estado de acondicionamiento de tambores · {"descripcion": "Los tambores se acondicionan con monedas nuevas, a menos que el BCRA decida otro estado para su entrega"} · tramo: Los tambores para provisión de metálico a las entidades financieras serán acondicionados con monedas nuevas, salvo que el BCRA decida otro estado para su entrega
- **N2** Obligacion `Obligacion_el_bcra_informara_a_las_entidades_requirentes_las_cantidades_asignadas_la_fecha__c37f06` — Información de cantidades asignadas y fecha de entrega · {"tipo": "comunicacion_a_cliente", "descripcion": "El BCRA informará a las entidades requirentes las cantidades asignadas, la fecha, horario y el lugar de entrega del metálico una vez realizados los pedidos y autorizado el cronograma de pagos"} · tramo: se informará a las entidades requirentes las cantidades asignadas, la fecha, horario y el lugar de entrega del metálico
- **N3** Obligacion `Obligacion_las_entidades_financieras_deben_atender_las_especificaciones_del_bcra_respecto_a_240fb1` — Cumplimiento de especificaciones de acondicionamiento · {"tipo": "otra", "descripcion": "Las entidades financieras deben atender las especificaciones del BCRA respecto al acondicionamiento de monedas en tambores, cantidad total y por bolsas, diseño y denominación"} · tramo: Las mismas deberán atender las especificaciones indicadas por el BCRA en cuanto a su acondicionamiento en tambores, cantidad total y por bolsas, diseño y denominación
- **N4** Obligacion `Obligacion_las_entidades_financieras_deben_cursar_la_solicitud_de_provision_de_monedas_medi_66798c` — Solicitud de provisión mediante débito MEP · {"tipo": "otra", "descripcion": "Las entidades financieras deben cursar la solicitud de provisión de monedas mediante débito en su cuenta corriente por medio del sistema MEP en el día asignado para el retiro"} · tramo: El día asignado para el retiro, las entidades financieras cursarán la solicitud de provisión de monedas mediante débito en su cuenta corriente por medio del sistema MEP
- **N5** Obligacion `Obligacion_las_entidades_financieras_deben_realizar_su_pedido_de_monedas_a_la_casilla_opera_d4a765` — Pedido de monedas con anticipación · {"tipo": "comunicacion_a_cliente", "descripcion": "Las entidades financieras deben realizar su pedido de monedas a la casilla operaciones.monedas@bcra.gob.ar con una semana de anticipación a la Gerencia de Operaciones de Tesoro en el horario de 10:00 a 15:00", "umbrales": [{"tramo": "en el horario de 10:00 a 15:00", "comparacion": "no_determinada", "regla_comparacion": "limite_relativo:sin_marcado · tramo: Las entidades financieras que requieran monedas realizarán su pedido a la casilla genérica operaciones.monedas@bcra.gob.ar, con una semana de anticipación a la Gerencia de Operaciones de Tesoro en el horario de 10:00 a 15:00
- **N6** Obligacion `Obligacion_las_entidades_financieras_que_requieran_cantidades_de_monedas_por_encima_de_sus__ec1031` — Planes de provisión anticipada para épocas de alta demanda · {"tipo": "otra", "descripcion": "Las entidades financieras que requieran cantidades de monedas por encima de sus necesidades normales en determinadas épocas del año deben realizar planes de provisión anticipada y paulatina para evitar inconvenientes del movimiento de gran masa de numerario"} · tramo: Las entidades financieras que necesiten, en determinadas épocas del año, cantidades de monedas por encima de sus necesidades normales, deberán realizar planes de provisión anticipada y paulatina, para evitar los inconvenientes del movimiento de una gran masa de numerario en uno o varios días
- **N7** Obligacion `Obligacion_las_entidades_financieras_y_las_transportadoras_de_valores_deben_controlar_el_co_e31fb8` — Control de contenido de tambores mediante trasvasado · {"tipo": "otra", "descripcion": "Las entidades financieras y las transportadoras de valores deben controlar el contenido de los tambores mediante el trasvasado de bolsas, en presencia de veedores antes de su retiro"} · tramo: Las entidades financieras y las transportadoras de valores controlarán el contenido de los tambores mediante el trasvasado de bolsas, en presencia de veedores antes de su retiro
- **N8** Operacion `Operacion_entrega_de_monedas_a_traves_de_cronograma__cirmo3_5_4_2_ba1c4e` — Entrega de monedas a través de cronograma · {"tipo": "entrega de monedas", "descripcion": "Entrega de monedas a entidades financieras mediante un cronograma de pagos para abastecer de metálico en CABA e interior del país"} · tramo: se atenderán los requerimientos que realicen las entidades financieras a través de un cronograma de pagos
- **N9** Restriccion `Restriccion_el_debito_mep_debe_remitirse_en_el_horario_de_8_00_a_10_00_si_no_se_cumple_no_se_0228f6` — Horario para remisión de débito MEP · {"tipo": "limite_cuantitativo", "descripcion": "El débito MEP debe remitirse en el horario de 8:00 a 10:00; si no se cumple, no se realizará el pago y se asignará una nueva fecha de entrega", "umbrales": [{"tramo": "de 8:00 a 10:00", "comparacion": "no_determinada", "regla_comparacion": "limite_relativo:sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}]} · tramo: El horario dispuesto para la remisión del débito MEP es de 8:00 a 10:00, caso contrario, no se realizará el pago, debiéndose asignar a la entidad una nueva fecha de entrega
- **N10** Restriccion `Restriccion_el_tambor_es_la_unidad_menor_de_medida_para_la_provision_de_monedas__cirmo3_5_4__3feb78` — Unidad mínima de medida: tambor · {"tipo": "limite_cualitativo", "descripcion": "El tambor es la unidad menor de medida para la provisión de monedas"} · tramo: siendo un tambor la unidad menor de medida
- **N11** Restriccion `Restriccion_los_requerimientos_via_mep_de_las_entidades_deben_coincidir_exactamente_con_lo_s_293df7` — Coincidencia entre requerimientos MEP y lo asignado · {"tipo": "limite_cualitativo", "descripcion": "Los requerimientos vía MEP de las entidades deben coincidir exactamente con lo solicitado y asignado oportunamente por el BCRA"} · tramo: Los requerimientos vía MEP de las entidades deberán coincidir con lo solicitado y asignado oportunamente por el BCRA
- **N12** Sujeto `Sujeto_entidad_financiera` — Entidades financieras · {"nivel": "clase", "alias": ["Entidades financieras emisoras de tarjetas de crédito y/o compra", "Entidad financiera emisora de tarjetas de crédito y/o compra"]} · tramo: 
- **N13** Sujeto `Sujeto_propuesto_las_entidades__cirmo3` — las entidades · {"nivel": "propuesto", "cuarentena": "true", "colision_cross_to": "true", "padre_sugerido": "Sujeto_sujeto", "padre_por_defecto_generico": "true"} · tramo: 
- **N14** Sujeto `Sujeto_rol_alcance_traval` — Sujetos comprendidos (Transportadoras de valores) · {"nivel": "rol"} · tramo: 
- **N15** TextoOrdenado `TextoOrdenado_cirmo3_pdf` — Billetes y monedas en circulación · {"archivo": "cirmo3.pdf", "materia": "Circulación monetaria", "version": "Comunicación A 8439 (vigencia 01/06/2026)"} · tramo: 
- **E1** (estructural) N1 —establecida_en→ N15 · {}
- **E2** (estructural) N2 —establecida_en→ N15 · {}
- **A1** (extraccion) N3 —aplica_a→ N12 · {}
- **E3** (estructural) N3 —establecida_en→ N15 · {}
- **A2** (extraccion) N4 —aplica_a→ N12 · {}
- **E4** (estructural) N4 —establecida_en→ N15 · {}
- **A3** (extraccion) N5 —aplica_a→ N12 · {}
- **E5** (estructural) N5 —establecida_en→ N15 · {}
- **A4** (extraccion) N6 —aplica_a→ N12 · {}
- **E6** (estructural) N6 —establecida_en→ N15 · {}
- **A5** (extraccion) N7 —aplica_a→ N12 · {}
- **A6** (extraccion) N7 —aplica_a→ N14 · {}
- **E7** (estructural) N7 —establecida_en→ N15 · {}
- **A7** (extraccion) N8 —aplica_a→ N12 · {}
- **E8** (estructural) N8 —establecida_en→ N15 · {}
- **A8** (extraccion) N9 —aplica_a→ N13 · {}
- **E9** (estructural) N9 —establecida_en→ N15 · {}
- **E10** (estructural) N10 —establecida_en→ N15 · {}
- **A9** (extraccion) N10 —limita→ N8 · {}
- **A10** (extraccion) N11 —aplica_a→ N13 · {}
- **E11** (estructural) N11 —establecida_en→ N15 · {}
- **A11** (extraccion) N11 —limita→ N8 · {}
- **C1** (catalogo_sujetos) N13 —padre_sugerido→ Sujeto_sujeto · {"flag": "padre_sugerido_no_laudado"}

## 27. `depaho::3.16.7` — NG:resto · aceptadas:no_items

Texto que vio E3 (e0, bloque de lista True; págs. 63):

```
[encabezado | punto S3]
Sección 3. Especiales.
[encabezado | punto 3.16]
3.16. Cuenta especial de regularización de activos – Ley 27.743.
[texto propio | punto 3.16.7]
3.16.7. Otras disposiciones.
En cuanto no se encuentre previsto y en la medida en que no se opongan a lo detalla-
do en los puntos precedentes, serán de aplicación las disposiciones establecidas para
los depósitos en caja de ahorros y cuenta corriente especial para personas jurídicas,
según corresponda.
```

Versión: final (grafo sin cola). Nodos 4, aristas 5.
- **N1** Condicion `Condicion_supuesto_no_previsto_en_puntos_precedentes__cuando_una_materia_no_se_encuentre_p_c6399e` — Supuesto: no previsto en puntos precedentes · {"descripcion": "Cuando una materia no se encuentre prevista en los puntos precedentes de la Cuenta especial de regularización de activos."} · tramo: En cuanto no se encuentre previsto
- **N2** Condicion `Condicion_supuesto_no_se_opone_a_lo_detallado__cuando_las_disposiciones_aplicables_no_se_o_e975c8` — Supuesto: no se opone a lo detallado · {"descripcion": "Cuando las disposiciones aplicables no se oponen a lo detallado en los puntos precedentes de esta norma."} · tramo: en la medida en que no se opongan a lo detallado en los puntos precedentes
- **N3** Obligacion `Obligacion_seran_de_aplicacion_las_disposiciones_establecidas_para_los_depositos_en_caja_de_51343a` — Aplicación de disposiciones de depósitos en caja de ahorros · {"tipo": "otra", "descripcion": "Serán de aplicación las disposiciones establecidas para los depósitos en caja de ahorros y cuenta corriente especial para personas jurídicas, según corresponda, en cuanto no se encuentre previsto en los puntos precedentes y en la medida en que no se opongan a lo detallado en ellos."} · tramo: serán de aplicación las disposiciones establecidas para los depósitos en caja de ahorros y cuenta corriente especial para personas jurídicas, según corresponda
- **N4** TextoOrdenado `TextoOrdenado_depaho_pdf` — Depósitos de ahorro · {"archivo": "depaho.pdf", "materia": "Depósitos de ahorro, cuenta sueldo y especiales", "version": "Comunicación A 8444 (vigencia 05/06/2026)"} · tramo: 
- **A1** (extraccion) N1 —condicion_de→ N3 · {}
- **E1** (estructural) N1 —establecida_en→ N4 · {}
- **A2** (extraccion) N2 —condicion_de→ N3 · {}
- **E2** (estructural) N2 —establecida_en→ N4 · {}
- **E3** (estructural) N3 —establecida_en→ N4 · {}

## 28. `depaho::3.4.2::intro` — NG:resto · aceptadas:no_items

Texto que vio E3 (e0, bloque de lista True; págs. 28):

```
[encabezado | punto S3]
Sección 3. Especiales.
[encabezado | punto 3.4]
3.4. Cuentas corrientes especiales para personas jurídicas.
[encabezado | punto 3.4.2]
3.4.2. Identificación y situación fiscal del titular.
[bloque intro | punto 3.4.2]
Como mínimo se exigirán los siguientes datos:
```

Versión: final (grafo sin cola). Nodos 1, aristas 0.
- **N1** TextoOrdenado `TextoOrdenado_depaho_pdf` — Depósitos de ahorro · {"archivo": "depaho.pdf", "materia": "Depósitos de ahorro, cuenta sueldo y especiales", "version": "Comunicación A 8444 (vigencia 05/06/2026)"} · tramo: 

## 29. `depaho::3.10.4::intro` — NG:resto · aceptadas:no_items

Texto que vio E3 (e0, bloque de lista True; págs. 49):

```
[encabezado | punto S3]
Sección 3. Especiales.
[encabezado | punto 3.10]
3.10. Caja de ahorros destinada a menores de edad adolescentes.
[encabezado | punto 3.10.4]
3.10.4. Extracción de fondos.
[bloque intro | punto 3.10.4]
Se podrán efectuar, a opción del titular, según cualquiera de las siguientes alternativas
y de acuerdo con las condiciones previstas en el punto 1.7.:
```

Versión: final (grafo sin cola). Nodos 3, aristas 3.
- **N1** Condicion `Condicion_condiciones_del_punto_1_7__la_extraccion_de_fondos_esta_condicionada_al_cumplimi_2e2aef` — Condiciones del punto 1.7 · {"descripcion": "La extracción de fondos está condicionada al cumplimiento de las condiciones previstas en el punto 1.7."} · tramo: de acuerdo con las condiciones previstas en el punto 1.7.
- **N2** Potestad `Potestad_extraccion_de_fondos_a_opcion_del_titular__el_titular_de_la_caja_de_ahorros_para_86b1ac` — Extracción de fondos a opción del titular · {"descripcion": "El titular de la caja de ahorros para menores de edad adolescentes podrá efectuar la extracción de fondos a su opción, según cualquiera de las alternativas previstas, de acuerdo con las condiciones del punto 1.7."} · tramo: Se podrán efectuar, a opción del titular, según cualquiera de las siguientes alternativas
- **N3** TextoOrdenado `TextoOrdenado_depaho_pdf` — Depósitos de ahorro · {"archivo": "depaho.pdf", "materia": "Depósitos de ahorro, cuenta sueldo y especiales", "version": "Comunicación A 8444 (vigencia 05/06/2026)"} · tramo: 
- **A1** (extraccion) N1 —condicion_de→ N2 · {}
- **E1** (estructural) N1 —establecida_en→ N3 · {}
- **E2** (estructural) N2 —establecida_en→ N3 · {}

## 30. `lingeef::2.3.1::intro` — NG:resto · aceptadas:no_items

Texto que vio E3 (e0, bloque de lista True; págs. 25, 26, 27):

```
[encabezado | punto S2]
Sección 2. Gestión del riesgo de crédito.
[encabezado | punto 2.3]
2.3. Proceso de gestión del riesgo de crédito.
[encabezado | punto 2.3.1]
2.3.1. Otorgamiento.
[bloque intro | punto 2.3.1]
Las entidades deben operar bajo criterios sólidos y bien definidos para el otorgamiento
de créditos, los cuales deben:
a) Identificar de manera clara el mercado al cual está dirigido y garantizar un nivel de
conocimiento adecuado del deudor o contraparte, del propósito y estructura de la
operación y de su probabilidad de repago;
b) Definir el perfil del tomador de crédito, así como los tipos, montos y términos y condi-
ciones de crédito.
A esos efectos, las entidades deben:
i) Lograr un conocimiento suficiente del cliente previo al otorgamiento, debiendo esta-
blecer políticas estrictas para evitar relacionarse con personas o empresas involucra-
das en actividades fraudulentas.
También deben tener procesos para detectar grupos de contrapartes conectadas
que deban ser considerados como un solo cliente y para agrupar las exposiciones al
riesgo con un mismo deudor o contraparte en distintas líneas de negocio;
ii) Realizar previamente a su participación en préstamos sindicados y otros tipos de con-
sorcios de créditos, un procedimiento de debida diligencia en forma independiente,
procurando su propio análisis del riesgo de crédito y una revisión de los términos de
la operación.
iii) Sustentar sus decisiones crediticias fundamentalmente en el riesgo de incumplimiento
del deudor y sólo de manera secundaria en el patrimonio del deudor o en los
mitigadores de riesgo de la operación.
El riesgo de incumplimiento depende de la capacidad y voluntad de repago del deu-
dor y para evaluarlo de manera integral la entidad debe contar con información sufi-
ciente;
iv) Considerar y documentar al momento del otorgamiento, dependiendo del tipo de
exposición crediticia –créditos hipotecarios, tarjetas de crédito, etc.– y de la
naturaleza de la relación crediticia –categorías comercial, comercial asimilable a
consumo o de consumo o vivienda– los siguientes elementos:
- la finalidad o el destino del crédito y su fuente de repago;
- los términos y condiciones del crédito;
- el perfil del riesgo actual del deudor o contraparte y sus mitigadores de riesgo, eva-
luando su integridad, eficacia, posibilidad de ejecución y su sensibilidad a la evolu-
ción de la economía y del mercado;
- el comportamiento histórico y actual del deudor en el cumplimiento de sus obliga-
ciones;
- la capacidad de pago actual y futura del deudor, según sus flujos de fondos proyec-
tados bajo diversos escenarios; y
- la experiencia del deudor en el negocio, situación del sector económico al que per-
tenece y su posicionamiento dentro de ese sector, en los casos de créditos comer-
ciales;
v) Efectuar la evaluación del deudor independientemente de la existencia de mitigado-
res de riesgo;
vi) Contar, respecto de los mitigadores de riesgo, con:
-políticas que definan los mitigadores de riesgo aceptables;
-procesos para su evaluación periódica -en función de su naturaleza-; y
-procesos para garantizar la ejecución y liquidación de las garantías.
Las entidades financieras no deben soslayar el tiempo y costo que implica ejecutar
los mitigadores de riesgo y su efecto en la rentabilidad de la operación, como tampo-
co la potencial correlación entre la calidad crediticia del mitigador de riesgo -por ejem-
plo, el valor de mercado de una garantía- y el riesgo del crédito que pretenden miti-
gar;
vii) Evaluar la relación riesgo-rentabilidad de la operación y del cliente -por todas sus
operaciones con la entidad y procurar que los riesgos estén adecuadamente conside-
rados en la determinación de los costos y en el precio de la operación, especialmente
en la evaluación de nuevos productos. El precio del crédito debe ser adecuado para
que la entidad esté debidamente compensada por los riesgos que asume.
Además, deben evaluar escenarios negativos y su posible incidencia en los deudores
y contrapartes.
```

Versión: final (grafo sin cola). Nodos 16, aristas 28.
- **N1** Obligacion `Obligacion_el_precio_del_credito_debe_ser_adecuado_para_que_la_entidad_este_debidamente_com_61a16e` — Precio del crédito adecuado para compensación de riesgos · {"descripcion": "El precio del crédito debe ser adecuado para que la entidad esté debidamente compensada por los riesgos que asume.", "tipo": "otra"} · tramo: El precio del crédito debe ser adecuado para que la entidad esté debidamente compensada por los riesgos que asume
- **N2** Obligacion `Obligacion_las_entidades_deben_considerar_y_documentar_al_momento_del_otorgamiento_dependie_3f5f96` — Documentación de elementos al otorgamiento de crédito · {"descripcion": "Las entidades deben considerar y documentar al momento del otorgamiento, dependiendo del tipo de exposición crediticia y de la naturaleza de la relación crediticia, los siguientes elementos: la finalidad o el destino del crédito y su fuente de repago; los términos y condiciones del crédito; el perfil del riesgo actual del deudor o contraparte y sus mitigadores de riesgo; el compor · tramo: Considerar y documentar al momento del otorgamiento, dependiendo del tipo de exposición crediticia –créditos hipotecarios, tarjetas de crédito, etc.– y de la naturaleza de la relación crediticia –categorías comercial, comercial asimilable a consumo o de consumo o vivienda– los siguientes elementos: 
- **N3** Obligacion `Obligacion_las_entidades_deben_contar_con_procesos_para_garantizar_la_ejecucion_y_liquidaci_857fc7` — Procesos para garantizar ejecución de garantías · {"descripcion": "Las entidades deben contar con procesos para garantizar la ejecución y liquidación de las garantías.", "tipo": "otra"} · tramo: Contar, respecto de los mitigadores de riesgo, con procesos para garantizar la ejecución y liquidación de las garantías
- **N4** Obligacion `Obligacion_las_entidades_deben_contar_con_procesos_para_la_evaluacion_periodica_de_los_miti_88c5ce` — Procesos de evaluación periódica de mitigadores de riesgo · {"descripcion": "Las entidades deben contar con procesos para la evaluación periódica de los mitigadores de riesgo en función de su naturaleza.", "tipo": "otra"} · tramo: Contar, respecto de los mitigadores de riesgo, con procesos para su evaluación periódica -en función de su naturaleza-
- **N5** Obligacion `Obligacion_las_entidades_deben_contar_respecto_de_los_mitigadores_de_riesgo_con_politicas_q_d5d8e6` — Políticas para mitigadores de riesgo aceptables · {"descripcion": "Las entidades deben contar, respecto de los mitigadores de riesgo, con políticas que definan los mitigadores de riesgo aceptables.", "tipo": "otra"} · tramo: Contar, respecto de los mitigadores de riesgo, con políticas que definan los mitigadores de riesgo aceptables
- **N6** Obligacion `Obligacion_las_entidades_deben_efectuar_la_evaluacion_del_deudor_independientemente_de_la_e_98fce3` — Evaluación del deudor independiente de mitigadores · {"descripcion": "Las entidades deben efectuar la evaluación del deudor independientemente de la existencia de mitigadores de riesgo.", "tipo": "otra"} · tramo: Efectuar la evaluación del deudor independientemente de la existencia de mitigadores de riesgo
- **N7** Obligacion `Obligacion_las_entidades_deben_evaluar_escenarios_negativos_y_su_posible_incidencia_en_los__d31e08` — Evaluación de escenarios negativos y su incidencia · {"descripcion": "Las entidades deben evaluar escenarios negativos y su posible incidencia en los deudores y contrapartes.", "tipo": "otra"} · tramo: Además, deben evaluar escenarios negativos y su posible incidencia en los deudores y contrapartes
- **N8** Obligacion `Obligacion_las_entidades_deben_evaluar_la_relacion_riesgo_rentabilidad_de_la_operacion_y_de_8e6dce` — Evaluación de relación riesgo-rentabilidad de la operación · {"descripcion": "Las entidades deben evaluar la relación riesgo-rentabilidad de la operación y del cliente por todas sus operaciones con la entidad y procurar que los riesgos estén adecuadamente considerados en la determinación de los costos y en el precio de la operación, especialmente en la evaluación de nuevos productos.", "tipo": "otra"} · tramo: Evaluar la relación riesgo-rentabilidad de la operación y del cliente -por todas sus operaciones con la entidad y procurar que los riesgos estén adecuadamente considerados en la determinación de los costos y en el precio de la operación, especialmente en la evaluación de nuevos productos
- **N9** Obligacion `Obligacion_las_entidades_deben_lograr_un_conocimiento_suficiente_del_cliente_previo_al_otor_3b4b32` — Conocimiento suficiente del cliente previo al otorgamiento · {"descripcion": "Las entidades deben lograr un conocimiento suficiente del cliente previo al otorgamiento, debiendo establecer políticas estrictas para evitar relacionarse con personas o empresas involucradas en actividades fraudulentas.", "tipo": "otra"} · tramo: las entidades deben: i) Lograr un conocimiento suficiente del cliente previo al otorgamiento, debiendo esta- blecer políticas estrictas para evitar relacionarse con personas o empresas involucra- das en actividades fraudulentas
- **N10** Obligacion `Obligacion_las_entidades_deben_operar_bajo_criterios_solidos_y_bien_definidos_para_el_otorg_c6267f` — Criterios sólidos para otorgamiento de créditos · {"descripcion": "Las entidades deben operar bajo criterios sólidos y bien definidos para el otorgamiento de créditos, los cuales deben identificar de manera clara el mercado al cual está dirigido y garantizar un nivel de conocimiento adecuado del deudor o contraparte, del propósito y estructura de la operación y de su probabilidad de repago, y definir el perfil del tomador de crédito, así como los · tramo: Las entidades deben operar bajo criterios sólidos y bien definidos para el otorgamiento de créditos
- **N11** Obligacion `Obligacion_las_entidades_deben_realizar_previamente_a_su_participacion_en_prestamos_sindica_a62cb7` — Debida diligencia en préstamos sindicados y consorcios · {"descripcion": "Las entidades deben realizar previamente a su participación en préstamos sindicados y otros tipos de consorcios de créditos, un procedimiento de debida diligencia en forma independiente, procurando su propio análisis del riesgo de crédito y una revisión de los términos de la operación.", "tipo": "otra"} · tramo: Realizar previamente a su participación en préstamos sindicados y otros tipos de consorcios de créditos, un procedimiento de debida diligencia en forma independiente, procurando su propio análisis del riesgo de crédito y una revisión de los términos de la operación
- **N12** Obligacion `Obligacion_las_entidades_deben_sustentar_sus_decisiones_crediticias_fundamentalmente_en_el__a700ba` — Decisiones crediticias basadas en riesgo de incumplimiento · {"descripcion": "Las entidades deben sustentar sus decisiones crediticias fundamentalmente en el riesgo de incumplimiento del deudor y sólo de manera secundaria en el patrimonio del deudor o en los mitigadores de riesgo de la operación. El riesgo de incumplimiento depende de la capacidad y voluntad de repago del deudor y para evaluarlo de manera integral la entidad debe contar con información sufi · tramo: Sustentar sus decisiones crediticias fundamentalmente en el riesgo de incumplimiento del deudor y sólo de manera secundaria en el patrimonio del deudor o en los mitigadores de riesgo de la operación
- **N13** Obligacion `Obligacion_las_entidades_deben_tener_procesos_para_detectar_grupos_de_contrapartes_conectad_755605` — Procesos para detectar grupos de contrapartes conectadas · {"descripcion": "Las entidades deben tener procesos para detectar grupos de contrapartes conectadas que deban ser considerados como un solo cliente y para agrupar las exposiciones al riesgo con un mismo deudor o contraparte en distintas líneas de negocio.", "tipo": "otra"} · tramo: También deben tener procesos para detectar grupos de contrapartes conectadas que deban ser considerados como un solo cliente y para agrupar las exposiciones al riesgo con un mismo deudor o contraparte en distintas líneas de negocio
- **N14** Restriccion `Restriccion_las_entidades_financieras_no_deben_soslayar_el_tiempo_y_costo_que_implica_ejecut_34e10b` — No soslayar tiempo y costo de ejecución de mitigadores · {"descripcion": "Las entidades financieras no deben soslayar el tiempo y costo que implica ejecutar los mitigadores de riesgo y su efecto en la rentabilidad de la operación, ni la potencial correlación entre la calidad crediticia del mitigador de riesgo y el riesgo del crédito que pretenden mitigar.", "tipo": "limite_cualitativo"} · tramo: Las entidades financieras no deben soslayar el tiempo y costo que implica ejecutar los mitigadores de riesgo y su efecto en la rentabilidad de la operación, como tampoco la potencial correlación entre la calidad crediticia del mitigador de riesgo -por ejemplo, el valor de mercado de una garantía- y 
- **N15** Sujeto `Sujeto_entidad_financiera` — Entidades financieras · {"nivel": "clase", "alias": ["Entidades financieras emisoras de tarjetas de crédito y/o compra", "Entidad financiera emisora de tarjetas de crédito y/o compra"]} · tramo: 
- **N16** TextoOrdenado `TextoOrdenado_lingeef_pdf` — Lineamientos para la gestión de riesgos · {"archivo": "lingeef.pdf", "materia": "Lineamientos para la gestión de riesgos en las entidades financieras", "version": "Comunicación A 8463 (vigencia 01/08/2026)"} · tramo: 
- **A1** (extraccion) N1 —aplica_a→ N15 · {}
- **E1** (estructural) N1 —establecida_en→ N16 · {}
- **A2** (extraccion) N2 —aplica_a→ N15 · {}
- **E2** (estructural) N2 —establecida_en→ N16 · {}
- **A3** (extraccion) N3 —aplica_a→ N15 · {}
- **E3** (estructural) N3 —establecida_en→ N16 · {}
- **A4** (extraccion) N4 —aplica_a→ N15 · {}
- **E4** (estructural) N4 —establecida_en→ N16 · {}
- **A5** (extraccion) N5 —aplica_a→ N15 · {}
- **E5** (estructural) N5 —establecida_en→ N16 · {}
- **A6** (extraccion) N6 —aplica_a→ N15 · {}
- **E6** (estructural) N6 —establecida_en→ N16 · {}
- **A7** (extraccion) N7 —aplica_a→ N15 · {}
- **E7** (estructural) N7 —establecida_en→ N16 · {}
- **A8** (extraccion) N8 —aplica_a→ N15 · {}
- **E8** (estructural) N8 —establecida_en→ N16 · {}
- **A9** (extraccion) N9 —aplica_a→ N15 · {}
- **E9** (estructural) N9 —establecida_en→ N16 · {}
- **A10** (extraccion) N10 —aplica_a→ N15 · {}
- **E10** (estructural) N10 —establecida_en→ N16 · {}
- **A11** (extraccion) N11 —aplica_a→ N15 · {}
- **E11** (estructural) N11 —establecida_en→ N16 · {}
- **A12** (extraccion) N12 —aplica_a→ N15 · {}
- **E12** (estructural) N12 —establecida_en→ N16 · {}
- **A13** (extraccion) N13 —aplica_a→ N15 · {}
- **E13** (estructural) N13 —establecida_en→ N16 · {}
- **A14** (extraccion) N14 —aplica_a→ N15 · {}
- **E14** (estructural) N14 —establecida_en→ N16 · {}

