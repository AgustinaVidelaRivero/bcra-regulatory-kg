# Material de T4 — aceptadas:items (30 fichas; B6.1, tanda 1, T3, punto 7.5)

Sorteo: `aceptadas_items.json` (35622d64…, 2026-10-18T10:09:26-03:00); material armado a las 2026-10-18T10:12:10-03:00. Sin el estado de E3 ni las marcas de E3.

## 1. `ri_ccna::D1A3L2::29.3` — RI:sin_raiz · aceptadas:items

Texto que vio E3 (e0, bloque de lista True; págs. 20):

```
[encabezado | punto D1A3]
ANEXO III
[encabezado | punto D1A3L2]
B. PRUEBAS SUSTANTIVAS
[encabezado | punto D1A3L2::S29]
29. Cotejo de la documentación de respaldo y verificación detallada de los importes
más significativos imputados a los resultados del ejercicio de las cuentas que:
[texto propio | punto D1A3L2::29.3]
29.3. Por su naturaleza y/o significatividad requiera la realización de un examen
detallado a juicio del auditor externo.
```

Versión: final (grafo sin cola). Nodos 3, aristas 3.
- **N1** Condicion `Condicion_naturaleza_o_significatividad_requiera_examen_detallado__supuesto_en_que_la_docu_4f106b` — Naturaleza o significatividad requiera examen detallado · {"descripcion": "Supuesto en que la documentación de respaldo y verificación detallada de importes más significativos imputados a resultados requiere examen detallado a juicio del auditor externo, por su naturaleza y/o significatividad"} · tramo: Por su naturaleza y/o significatividad requiera la realización de un examen detallado a juicio del auditor externo
- **N2** Operacion `Operacion_examen_detallado_de_documentacion_de_respaldo__ri_ccna_d1a3l2_29_3_0e98c9` — Examen detallado de documentación de respaldo · {"tipo": "Examen de documentación", "descripcion": "Realización de examen detallado de la documentación de respaldo y verificación de importes más significativos imputados a resultados del ejercicio, a juicio del auditor externo"} · tramo: la realización de un examen detallado a juicio del auditor externo
- **N3** TextoOrdenado `TextoOrdenado_ri_ccna_pdf` — Régimen de Información Contable · {"archivo": "ri_ccna.pdf", "materia": "RI para Cajas de Crédito - Normas de Auditoría", "version": "Comunicación A 4523 (vigencia 06/04/2006)"} · tramo: 
- **A1** (extraccion) N1 —condicion_de→ N2 · {}
- **E1** (estructural) N1 —establecida_en→ N3 · {}
- **E2** (estructural) N2 —establecida_en→ N3 · {}

## 2. `ri_ccna::D1F2::3.5` — RI:sin_raiz · aceptadas:items

Texto que vio E3 (e0, bloque de lista True; págs. 32):

```
[encabezado | punto D1F2]
DECLARACIÓN JURADA DE AUDITORES EXTERNOS
[encabezado | punto D1F2::S3]
3. No me alcanza ninguna de las siguientes inhabilidades previstas por el artículo 10 de la Ley Nº 21.526, según se detalla a conti-
nuación:
[texto propio | punto D1F2::3.5]
3.5 Los inhabilitados por aplicación del inciso 5) del artículo 41 de la Ley Nº 21.526, mientras dure el tiempo de su sanción, o
sea para desempeñarse como promotores, fundadores, directores, administradores, miembros de los consejos de vigilan-
cia, síndicos, liquidadores o gerentes de entidades financieras comprendidas en dicha Ley;
```

Versión: final (grafo sin cola). Nodos 3, aristas 2.
- **N1** Comunicacion `Comunicacion_ley_no_21_526` — Ley Nº 21.526 · {"codigo": "Ley Nº 21.526", "tipo": "externa"} · tramo: artículo 41 de la Ley Nº 21.526
- **N2** Excepcion `Excepcion_inhabilidad_de_personas_inhabilitadas_por_el_inciso_5_del_articulo_41_de_la_ley__42c80b` — Inhabilidad inciso 5 art. 41 Ley 21.526 — auditores externos · {"descripcion": "Inhabilidad de personas inhabilitadas por el inciso 5) del artículo 41 de la Ley Nº 21.526 para desempeñarse como promotores, fundadores, directores, administradores, miembros de consejos de vigilancia, síndicos, liquidadores o gerentes de entidades financieras; la inhabilidad persiste mientras dure el tiempo de su sanción. Exceptúa la posibilidad de un auditor externo de certific · tramo: Los inhabilitados por aplicación del inciso 5) del artículo 41 de la Ley Nº 21.526, mientras dure el tiempo de su sanción, o sea para desempeñarse como promotores, fundadores, directores, administradores, miembros de los consejos de vigilancia, síndicos, liquidadores o gerentes de entidades financie
- **N3** TextoOrdenado `TextoOrdenado_ri_ccna_pdf` — Régimen de Información Contable · {"archivo": "ri_ccna.pdf", "materia": "RI para Cajas de Crédito - Normas de Auditoría", "version": "Comunicación A 4523 (vigencia 06/04/2006)"} · tramo: 
- **E1** (estructural) N2 —establecida_en→ N3 · {}
- **E2** (estructural) N3 —referencia→ N1 · {}

## 3. `ri_mmsef::2.2.8.3.2` — RI:sin_raiz · aceptadas:items

Texto que vio E3 (e0, bloque de lista True; págs. 4):

```
[encabezado | punto S2]
2. Instrucciones particulares.
[encabezado | punto 2.2]
2.2. Cumplimiento de las medidas mínimas de seguridad.
[encabezado | punto 2.2.8]
2.2.8. Medidas de seguridad para atesoramiento de numerario.
[encabezado | punto 2.2.8.3]
2.2.8.3. Tesoro modular:
[texto propio | punto 2.2.8.3.2]
2.2.8.3.2. Tenencia de certificado de aptitud.
```

Versión: final (grafo sin cola). Nodos 2, aristas 1.
- **N1** Operacion `Operacion_tenencia_de_certificado_de_aptitud__ri_mmsef_2_2_8_3_2_0589ab` — Tenencia de certificado de aptitud · {"tipo": "tenencia de certificado", "descripcion": "Tenencia de certificado de aptitud para tesoro modular"} · tramo: Tenencia de certificado de aptitud
- **N2** TextoOrdenado `TextoOrdenado_ri_mmsef_pdf` — Régimen Informativo Medidas Mínimas Seguridad · {"archivo": "ri_mmsef.pdf", "materia": "RI Cont. Mensual - Medidas mínimas de seguridad en entidades financieras", "version": "Comunicación A 6623 (vigencia 05/01/2019)"} · tramo: 
- **E1** (estructural) N1 —establecida_en→ N2 · {}

## 4. `ri_mmsef::2.2.10.2` — RI:sin_raiz · aceptadas:items

Texto que vio E3 (e0, bloque de lista True; págs. 5):

```
[encabezado | punto S2]
2. Instrucciones particulares.
[encabezado | punto 2.2]
2.2. Cumplimiento de las medidas mínimas de seguridad.
[encabezado | punto 2.2.10]
2.2.10. Vigilancia:
[texto propio | punto 2.2.10.2]
2.2.10.2. Seguridad privada.
```

Versión: final (grafo sin cola). Nodos 4, aristas 5.
- **N1** Obligacion `Obligacion_informar_el_cumplimiento_de_las_medidas_minimas_de_seguridad_respecto_de_segurid_494e2d` — Informar cumplimiento — Seguridad privada · {"tipo": "presentacion_informativa", "descripcion": "Informar el cumplimiento de las medidas mínimas de seguridad respecto de seguridad privada, según los parámetros: Si (cuando esté efectivamente cumplimentada), No (aun cuando esté en vías de realización), Eximida (cuando cuente exención expresa del BCRA), o No Aplicable (cuando la medida no es exigida)"} · tramo: Se informará el cumplimiento de las medidas mínimas de seguridad […] Seguridad privada
- **N2** Operacion `Operacion_vigilancia_seguridad_privada__ri_mmsef_2_2_10_2_ae6691` — Vigilancia — Seguridad privada · {"tipo": "vigilancia", "descripcion": "Cumplimiento de medidas mínimas de seguridad en materia de seguridad privada, conforme a las Normas Mínimas de Seguridad en Entidades Financieras"} · tramo: Seguridad privada
- **N3** Sujeto `Sujeto_propuesto_las_entidades__ri_mmsef` — las entidades · {"nivel": "propuesto", "cuarentena": "true", "colision_cross_to": "true", "padre_sugerido": "Sujeto_rol_entidad_comprendida_reginf", "padre_desde_sugerencia_modelo": "true"} · tramo: 
- **N4** TextoOrdenado `TextoOrdenado_ri_mmsef_pdf` — Régimen Informativo Medidas Mínimas Seguridad · {"archivo": "ri_mmsef.pdf", "materia": "RI Cont. Mensual - Medidas mínimas de seguridad en entidades financieras", "version": "Comunicación A 6623 (vigencia 05/01/2019)"} · tramo: 
- **A1** (extraccion) N1 —aplica_a→ N3 · {}
- **E1** (estructural) N1 —establecida_en→ N4 · {}
- **A2** (extraccion) N1 —regula→ N2 · {}
- **E2** (estructural) N2 —establecida_en→ N4 · {}
- **C1** (catalogo_sujetos) N3 —padre_sugerido→ Sujeto_rol_entidad_comprendida_reginf · {"flag": "padre_sugerido_no_laudado"}

## 5. `ri_ccna::D1F2::3.6` — RI:sin_raiz · aceptadas:items

Texto que vio E3 (e0, bloque de lista True; págs. 32):

```
[encabezado | punto D1F2]
DECLARACIÓN JURADA DE AUDITORES EXTERNOS
[encabezado | punto D1F2::S3]
3. No me alcanza ninguna de las siguientes inhabilidades previstas por el artículo 10 de la Ley Nº 21.526, según se detalla a conti-
nuación:
[texto propio | punto D1F2::3.6]
3.6 Quienes por decisión de autoridad competente hubieran sido declarados responsables de irregularidades en el gobierno y
administración de las entidades financieras, y
```

Versión: final (grafo sin cola). Nodos 2, aristas 1.
- **N1** Condicion `Condicion_declaracion_responsable_de_irregularidades_en_gobierno__supuesto_que_inhabilita__04a3ef` — Declaración responsable de irregularidades en gobierno · {"descripcion": "Supuesto que inhabilita: haber sido declarado responsable de irregularidades en el gobierno y administración de entidades financieras por decisión de autoridad competente"} · tramo: Quienes por decisión de autoridad competente hubieran sido declarados responsables de irregularidades en el gobierno y administración de las entidades financieras
- **N2** TextoOrdenado `TextoOrdenado_ri_ccna_pdf` — Régimen de Información Contable · {"archivo": "ri_ccna.pdf", "materia": "RI para Cajas de Crédito - Normas de Auditoría", "version": "Comunicación A 4523 (vigencia 06/04/2006)"} · tramo: 
- **E1** (estructural) N1 —establecida_en→ N2 · {}

## 6. `ri_mmsef::2.3.2.2` — RI:sin_raiz · aceptadas:items

Texto que vio E3 (e0, bloque de lista True; págs. 6):

```
[encabezado | punto S2]
2. Instrucciones particulares.
[encabezado | punto 2.3]
2.3. Identificación de los dispositivos de seguridad.
[encabezado | punto 2.3.2]
2.3.2. Castillete:
[texto propio | punto 2.3.2.2]
2.3.2.2. Número de serie.
```

Versión: final (grafo sin cola). Nodos 1, aristas 0.
- **N1** TextoOrdenado `TextoOrdenado_ri_mmsef_pdf` — Régimen Informativo Medidas Mínimas Seguridad · {"archivo": "ri_mmsef.pdf", "materia": "RI Cont. Mensual - Medidas mínimas de seguridad en entidades financieras", "version": "Comunicación A 6623 (vigencia 05/01/2019)"} · tramo: 

## 7. `ri_ccna::D1F6::3.1.2` — RI:sin_raiz · aceptadas:items

Texto que vio E3 (e0, bloque de lista True; págs. 41):

```
[encabezado | punto D1F6]
DECLARACIÓN JURADA DEL SOCIO RESPONSABLE
[encabezado | punto D1F6::S3]
3. No me alcanza ninguna de las siguientes inhabilidades previstas por el artículo 10 de la Ley Nº 21.526, según se detalla a continua-
ción:
[encabezado | punto D1F6::3.1]
3.1. Los afectados por las inhabilidades o incompatibilidades establecidas por el artículo 264 de la Ley Nº 19.550, a saber:
[texto propio | punto D1F6::3.1.2]
3.1.2. Los fallidos por quiebra culpable o fraudulenta hasta diez años después de su rehabilitación; los fallidos por quiebra
casual o los concursados hasta cinco años después de su rehabilitación; los directores o administradores de sociedad
cuya conducta se calificare de culpable o fraudulenta, hasta diez años después de su rehabilitación.
```

Versión: final (grafo sin cola). Nodos 4, aristas 3.
- **N1** Restriccion `Restriccion_no_pueden_desempenarse_como_socio_responsable_los_directores_o_administradores_d_4eae4e` — Inhabilidad directores/administradores conducta culpable/fraudulenta · {"tipo": "prohibicion", "descripcion": "No pueden desempeñarse como Socio Responsable los directores o administradores de sociedad cuya conducta se calificare de culpable o fraudulenta, hasta diez años después de su rehabilitación", "umbrales": [{"tramo": "hasta diez años después de su rehabilitación", "valor": "10", "unidad": "anios", "comparacion": "maximo_inclusivo", "regla_comparacion": "compu · tramo: los directores o administradores de sociedad cuya conducta se calificare de culpable o fraudulenta, hasta diez años después de su rehabilitación
- **N2** Restriccion `Restriccion_no_pueden_desempenarse_como_socio_responsable_los_fallidos_por_quiebra_casual_o__d4a592` — Inhabilidad fallidos quiebra casual · {"tipo": "prohibicion", "descripcion": "No pueden desempeñarse como Socio Responsable los fallidos por quiebra casual o los concursados hasta cinco años después de su rehabilitación", "umbrales": [{"tramo": "hasta cinco años después de su rehabilitación", "valor": "5", "unidad": "anios", "comparacion": "maximo_inclusivo", "regla_comparacion": "compuesta:hasta", "origen": "e1", "tramo_verificado":  · tramo: los fallidos por quiebra casual o los concursados hasta cinco años después de su rehabilitación
- **N3** Restriccion `Restriccion_no_pueden_desempenarse_como_socio_responsable_los_fallidos_por_quiebra_culpable__d0c257` — Inhabilidad fallidos quiebra culpable/fraudulenta · {"tipo": "prohibicion", "descripcion": "No pueden desempeñarse como Socio Responsable los fallidos por quiebra culpable o fraudulenta hasta diez años después de su rehabilitación", "umbrales": [{"tramo": "hasta diez años después de su rehabilitación", "valor": "10", "unidad": "anios", "comparacion": "maximo_inclusivo", "regla_comparacion": "compuesta:hasta", "origen": "e1", "tramo_verificado": "ex · tramo: Los fallidos por quiebra culpable o fraudulenta hasta diez años después de su rehabilitación
- **N4** TextoOrdenado `TextoOrdenado_ri_ccna_pdf` — Régimen de Información Contable · {"archivo": "ri_ccna.pdf", "materia": "RI para Cajas de Crédito - Normas de Auditoría", "version": "Comunicación A 4523 (vigencia 06/04/2006)"} · tramo: 
- **E1** (estructural) N1 —establecida_en→ N4 · {}
- **E2** (estructural) N2 —establecida_en→ N4 · {}
- **E3** (estructural) N3 —establecida_en→ N4 · {}

## 8. `ri_mmsef::2.2.13.1` — RI:sin_raiz · aceptadas:items

Texto que vio E3 (e0, bloque de lista True; págs. 5):

```
[encabezado | punto S2]
2. Instrucciones particulares.
[encabezado | punto 2.2]
2.2. Cumplimiento de las medidas mínimas de seguridad.
[encabezado | punto 2.2.13]
2.2.13. Circuito cerrado de televisión de seguridad:
[texto propio | punto 2.2.13.1]
2.2.13.1. UPS o red alternativa de alimentación eléctrica.
```

Versión: final (grafo sin cola). Nodos 3, aristas 3.
- **N1** Obligacion `Obligacion_informar_el_cumplimiento_de_la_medida_de_ups_o_red_alternativa_de_alimentacion_e_3986ef` — Informar cumplimiento UPS o red alternativa alimentación · {"tipo": "presentacion_informativa", "descripcion": "Informar el cumplimiento de la medida de UPS o red alternativa de alimentación eléctrica para el circuito cerrado de televisión de seguridad, según los parámetros: Si (cuando esté efectivamente cumplimentada), No (aun cuando esté en vías de realización), Eximida (cuando cuente exención expresa del BCRA), o No Aplicable (cuando la medida no es ex · tramo: Se informará el cumplimiento de las medidas mínimas de seguridad […] 2.2.13.1. UPS o red alternativa de alimentación eléctrica.
- **N2** Sujeto `Sujeto_propuesto_las_entidades__ri_mmsef` — las entidades · {"nivel": "propuesto", "cuarentena": "true", "colision_cross_to": "true", "padre_sugerido": "Sujeto_rol_entidad_comprendida_reginf", "padre_desde_sugerencia_modelo": "true"} · tramo: 
- **N3** TextoOrdenado `TextoOrdenado_ri_mmsef_pdf` — Régimen Informativo Medidas Mínimas Seguridad · {"archivo": "ri_mmsef.pdf", "materia": "RI Cont. Mensual - Medidas mínimas de seguridad en entidades financieras", "version": "Comunicación A 6623 (vigencia 05/01/2019)"} · tramo: 
- **A1** (extraccion) N1 —aplica_a→ N2 · {}
- **E1** (estructural) N1 —establecida_en→ N3 · {}
- **C1** (catalogo_sujetos) N2 —padre_sugerido→ Sujeto_rol_entidad_comprendida_reginf · {"flag": "padre_sugerido_no_laudado"}

## 9. `ri_mmsef::2.3.4.2` — RI:sin_raiz · aceptadas:items

Texto que vio E3 (e0, bloque de lista True; págs. 6):

```
[encabezado | punto S2]
2. Instrucciones particulares.
[encabezado | punto 2.3]
2.3. Identificación de los dispositivos de seguridad.
[encabezado | punto 2.3.4]
2.3.4. Tesoro Blindado (Bóveda de cemento y acero):
[texto propio | punto 2.3.4.2]
2.3.4.2. Número de serie.
```

Versión: final (grafo sin cola). Nodos 1, aristas 0.
- **N1** TextoOrdenado `TextoOrdenado_ri_mmsef_pdf` — Régimen Informativo Medidas Mínimas Seguridad · {"archivo": "ri_mmsef.pdf", "materia": "RI Cont. Mensual - Medidas mínimas de seguridad en entidades financieras", "version": "Comunicación A 6623 (vigencia 05/01/2019)"} · tramo: 

## 10. `ri_mmsef::2.4.1.1` — RI:sin_raiz · aceptadas:items

Texto que vio E3 (e0, bloque de lista True; págs. 8):

```
[encabezado | punto S2]
2. Instrucciones particulares.
[encabezado | punto 2.4]
2.4. Medidas de seguridad en terminales automáticas.
[encabezado | punto 2.4.1]
2.4.1. Individualización del dispositivo:
[texto propio | punto 2.4.1.1]
2.4.1.1. Marca.
```

Versión: final (grafo sin cola). Nodos 1, aristas 0.
- **N1** TextoOrdenado `TextoOrdenado_ri_mmsef_pdf` — Régimen Informativo Medidas Mínimas Seguridad · {"archivo": "ri_mmsef.pdf", "materia": "RI Cont. Mensual - Medidas mínimas de seguridad en entidades financieras", "version": "Comunicación A 6623 (vigencia 05/01/2019)"} · tramo: 

## 11. `ri_dcpc::3.4.4.1` — RI:resto · aceptadas:items

Texto que vio E3 (e0, bloque de lista True; págs. 17):

```
[encabezado | punto S3]
Sección 3. CRITERIOS GENERALES
[encabezado | punto 3.4]
3.4. Criterios específicos para determinados instrumentos financieros.
[encabezado | punto 3.4.4]
3.4.4. Operaciones de Pase
[intro | punto 3.4.4]
De acuerdo con los principios de baja en cuentas de la NIIF 9, estas operaciones se consideran
como financiaciones con garantía y, por tanto las registraciones deben realizarse de acuerdo con
las siguientes pautas:
[texto propio | punto 3.4.4.1]
3.4.4.1. Pases Activos
Las financiaciones otorgadas instrumentadas mediante pases activos se registrarán en las cuentas
de “Otros Créditos por Intermediación Financiera – Deudores por pases activos”, clasificándolas
según quien sea la contraparte en deudores financieros, BCRA y no financieros y atendiendo el
activo recibido en garantía.
Al cierre de cada mes, los intereses devengados a cobrar se imputarán en la cuenta “Otros créditos
por intermediación financiera - Intereses devengados a cobrar por pases activos” o “Intereses
devengados a cobrar por pases activos con el B.C.R.A.” con contrapartida en “Ingresos Financieros
- Intereses por pases activos del Sector Financiero”, “Intereses por pases activos con el B.C.R.A.” o
“Intereses por otros pases activos”, según corresponda.
Los activos subyacentes recibidos por las operaciones de pases activo se registrarán en partidas
fuera de balance. En estas cuentas se mostrarán al cierre de cada mes los valores nocionales de
las operaciones vigentes medidos a valor razonable, y convertidos a su equivalente en pesos, de
corresponder. No se deducirán los activos recibidos que hayan sido vendidos por la entidad, sino
que se darán de baja solo cuando finalice la operación de pase.
```

Versión: final (grafo sin cola). Nodos 11, aristas 22.
- **N1** Condicion `Condicion_conversion_a_pesos_cuando_corresponda__cuando_corresponda_la_conversion_a_pesos__ed0582` — Conversión a pesos cuando corresponda · {"descripcion": "Cuando corresponda la conversión a pesos de los valores nocionales"} · tramo: convertidos a su equivalente en pesos, de corresponder
- **N2** Obligacion `Obligacion_al_cierre_de_cada_mes_los_intereses_devengados_a_cobrar_se_imputaran_en_la_cuent_1bdb06` — Imputación intereses devengados a cobrar mensualmente · {"tipo": "presentacion_informativa", "descripcion": "Al cierre de cada mes, los intereses devengados a cobrar se imputarán en la cuenta correspondiente según la contraparte, con contrapartida en la cuenta de ingresos financieros que corresponda", "frecuencia": "Al cierre de cada mes", "umbrales": [{"tramo": "Al cierre de cada mes", "comparacion": "no_determinada", "regla_comparacion": "limite_rela · tramo: Al cierre de cada mes, los intereses devengados a cobrar se imputarán en la cuenta "Otros créditos por intermediación financiera - Intereses devengados a cobrar por pases activos" o "Intereses devengados a cobrar por pases activos con el B.C.R.A." con contrapartida en "Ingresos Financieros - Interes
- **N3** Obligacion `Obligacion_en_las_cuentas_de_partidas_fuera_de_balance_se_mostraran_al_cierre_de_cada_mes_l_604171` — Presentación valores nocionales a valor razonable mensualmente · {"tipo": "presentacion_informativa", "descripcion": "En las cuentas de partidas fuera de balance se mostrarán al cierre de cada mes los valores nocionales de las operaciones vigentes medidos a valor razonable, convertidos a su equivalente en pesos cuando corresponda", "frecuencia": "al cierre de cada mes", "umbrales": [{"tramo": "al cierre de cada mes", "comparacion": "no_determinada", "regla_comp · tramo: En estas cuentas se mostrarán al cierre de cada mes los valores nocionales de las operaciones vigentes medidos a valor razonable, y convertidos a su equivalente en pesos, de corresponder
- **N4** Obligacion `Obligacion_las_financiaciones_otorgadas_mediante_pases_activos_se_registraran_en_las_cuenta_d61f02` — Registración pases activos en cuentas específicas · {"tipo": "presentacion_informativa", "descripcion": "Las financiaciones otorgadas mediante pases activos se registrarán en las cuentas de 'Otros Créditos por Intermediación Financiera – Deudores por pases activos', clasificándolas según la contraparte (deudores financieros, BCRA, no financieros) y atendiendo el activo recibido en garantía"} · tramo: se registrarán en las cuentas de "Otros Créditos por Intermediación Financiera – Deudores por pases activos", clasificándolas según quien sea la contraparte en deudores financieros, BCRA y no financieros y atendiendo el activo recibido en garantía
- **N5** Obligacion `Obligacion_los_activos_recibidos_se_daran_de_baja_de_las_cuentas_de_partidas_fuera_de_balan_592f1c` — Baja de activos solo al finalizar pase · {"tipo": "presentacion_informativa", "descripcion": "Los activos recibidos se darán de baja de las cuentas de partidas fuera de balance solo cuando finalice la operación de pase"} · tramo: se darán de baja solo cuando finalice la operación de pase
- **N6** Obligacion `Obligacion_los_activos_subyacentes_recibidos_por_las_operaciones_de_pases_activo_se_registr_364a67` — Registración activos subyacentes fuera de balance · {"tipo": "presentacion_informativa", "descripcion": "Los activos subyacentes recibidos por las operaciones de pases activo se registrarán en partidas fuera de balance"} · tramo: Los activos subyacentes recibidos por las operaciones de pases activo se registrarán en partidas fuera de balance
- **N7** Operacion `Operacion_financiacion_mediante_pase_activo__ri_dcpc_3_4_4_1_1ab240` — Financiación mediante pase activo · {"tipo": "Financiación con garantía", "descripcion": "Financiación otorgada mediante pase activo, con activo recibido en garantía, clasificada según la contraparte (deudores financieros, BCRA, no financieros)"} · tramo: Las financiaciones otorgadas instrumentadas mediante pases activos
- **N8** Restriccion `Restriccion_no_se_deduciran_los_activos_recibidos_que_hayan_sido_vendidos_por_la_entidad_en__8f48b7` — Prohibición deducir activos vendidos en pases activos · {"tipo": "prohibicion", "descripcion": "No se deducirán los activos recibidos que hayan sido vendidos por la entidad en las cuentas de partidas fuera de balance"} · tramo: No se deducirán los activos recibidos que hayan sido vendidos por la entidad
- **N9** Sujeto `Sujeto_entidad_financiera` — Entidades financieras · {"nivel": "clase", "alias": ["Entidades financieras emisoras de tarjetas de crédito y/o compra", "Entidad financiera emisora de tarjetas de crédito y/o compra"]} · tramo: 
- **N10** Sujeto `Sujeto_propuesto_las_entidades__ri_dcpc` — las entidades · {"nivel": "propuesto", "cuarentena": "true", "colision_cross_to": "true", "padre_sugerido": "Sujeto_entidad_financiera", "padre_desde_sugerencia_modelo": "true"} · tramo: 
- **N11** TextoOrdenado `TextoOrdenado_ri_dcpc_pdf` — Marco Contable · {"archivo": "ri_dcpc.pdf", "materia": "RI - Disposiciones complementarias al plan de cuentas", "version": "Comunicación A 8400 (vigencia 13/02/2026)"} · tramo: 
- **A1** (extraccion) N1 —condicion_de→ N3 · {}
- **E1** (estructural) N1 —establecida_en→ N11 · {}
- **A2** (extraccion) N2 —aplica_a→ N10 · {}
- **E2** (estructural) N2 —establecida_en→ N11 · {}
- **A3** (extraccion) N2 —regula→ N7 · {}
- **A4** (extraccion) N3 —aplica_a→ N10 · {}
- **E3** (estructural) N3 —establecida_en→ N11 · {}
- **A5** (extraccion) N3 —regula→ N7 · {}
- **A6** (extraccion) N4 —aplica_a→ N10 · {}
- **E4** (estructural) N4 —establecida_en→ N11 · {}
- **A7** (extraccion) N4 —regula→ N7 · {}
- **A8** (extraccion) N5 —aplica_a→ N9 · {}
- **E5** (estructural) N5 —establecida_en→ N11 · {}
- **A9** (extraccion) N5 —regula→ N7 · {}
- **A10** (extraccion) N6 —aplica_a→ N10 · {}
- **E6** (estructural) N6 —establecida_en→ N11 · {}
- **A11** (extraccion) N6 —regula→ N7 · {}
- **E7** (estructural) N7 —establecida_en→ N11 · {}
- **A12** (extraccion) N8 —aplica_a→ N9 · {}
- **E8** (estructural) N8 —establecida_en→ N11 · {}
- **A13** (extraccion) N8 —prohibe→ N7 · {}
- **C1** (catalogo_sujetos) N10 —padre_sugerido→ N9 · {"flag": "padre_sugerido_no_laudado"}

## 12. `ri_rml::Sbloque5` — RI:resto · aceptadas:items

Texto que vio E3 (e0, bloque de lista True; págs. 30):

```
[encabezado | punto S2]
Sección 2. Metodología de cálculo del aporte al Fondo de Garantía de los Depósitos
[chapeau_seccion | punto S2]
Base de cálculo * 0,015% * Ic * 1000
[chapeau_seccion | punto S2]
donde:
Base de cálculo = 101078/M + 101079/M + 101081/M + 101082/M + 10140X/M a 10144X/M +
10147X/001 + 101470/M + 101460/M + 10146X/001 + 101490/001 + 10160X/001 + 10161X/001
+ 10162X/001 + 10163X/001 + 10164X/001 + 101650/001 + 10171X/001 + 10175X/001 +
102010/M a 102055/M + 102190/001 + 102200/001 + 102300/001 + 102350/010 + 102360/001 +
801000/M
La información será la del segundo mes anterior al del ingreso del aporte.
Los importes en dólares estadounidenses se convertirán a pesos utilizando el tipo de cambio de
referencia correspondiente al último día hábil del mes anterior al que corresponda la liquidación
del aporte.
Ic = [ (Ipr/f + Iar/a + 2 * Icamels) / 4] - Irpc/Kmin
[chapeau_seccion | punto S2]
La calificación asignada se considerará para el cálculo del aporte exigible el tercer mes si-
guiente al de notificación.
En tanto no se disponga de la calificación de la SEFyC (“CAMELS”) el cálculo del índice de
corrección surgirá de la siguiente expresión: Ic = ((Ipr/f + Iar/a)/2) - Irpc/Kmin
[chapeau_seccion | punto S2]
Ipr/f (*) = [(Previsiones mínimas / Financiaciones y Garantías) / 0,04] ** 1,2
[chapeau_seccion | punto S2]
Previsiones mínimas: se considerarán las determinadas de acuerdo con las normas so-
bre previsiones mínimas por riesgo de incobrabilidad, sobre los conceptos informados
en la Sección B, punto 2. del Régimen Informativo de Deudores del Sistema Financiero.
Financiaciones y garantías: la correspondiente información se obtendrá de la Sección B,
punto 2. del Régimen Informativo de Deudores del Sistema Financiero.
(El valor del índice estará acotado entre 1 y 2,5)
[chapeau_seccion | punto S2]
Iar/a (*) = {[APRc / (A + (PFB x CCF))] / 0,70} ** 1,3
[chapeau_seccion | punto S2]
APRc = ∑Códigos 11000000 a 12800000 (excepto 11100000) + 12550000 + [∑Código
13X00000 + Código 14000000 + Código 86300000] * 12,5 + 15000000.
Los importes de las mencionadas partidas (detalladas en Sección 3. del régimen de
Exigencia e Integración de capitales mínimos) se considerarán por su valor ponderado.
A = Σ Códigos 11000000 a 12500000, 12600000 a 12800000 (excepto 11100000,
1221000/CCF, 1222000/CCF y 12300000) del régimen informativo sobre Capitales mí-
nimos (Importes sin ponderar).
[chapeau_seccion | punto S2]
(*) Los importes considerados para el cálculo de las relaciones corresponderán al tercer mes anterior a la fecha de
vencimiento de los aportes.
[chapeau_seccion | punto S2]
PFB x CCF = Códigos 1221000/CCF y 1222000/CCF (importes multiplicados por el Factor
de Con-versión Crediticia).
(El valor del índice estará acotado entre 1 y 2)
[chapeau_seccion | punto S2]
Irpc / Kmin = (Integración de capitales mínimos + Previsiones por riesgo de incobrabilidad consti-
tui-das en exceso sobre los mínimos establecidos) / Exigencia de capitales mínimos (por riesgo de
crédito, de mercado para las posiciones al último día del mes y operacional).
(El resultado del indicador se tomará de la tabla consignada en el punto 7.1. de las normas sobre
“Aplicación del sistema de seguro de garantía de depósitos”).
Para obtener la relación antes mencionada, deberán considerarse los siguientes conceptos:
[chapeau_seccion | punto S2]
Régimen Informativo de Capitales Mínimos:
[texto propio | punto Sbloque5]
Menos
· Previsiones mínimas exigidas: De acuerdo con la referencia indicada para el cálculo de
Ipr/f.
```

Versión: final (grafo sin cola). Nodos 2, aristas 1.
- **N1** Definicion `Definicion_previsiones_minimas_exigidas__se_calculan_de_acuerdo_con_la_referencia_indicada__777afc` — Previsiones mínimas exigidas · {"termino": "Previsiones mínimas exigidas", "descripcion": "Se calculan de acuerdo con la referencia indicada para el cálculo de Ipr/f, que corresponde a las previsiones mínimas determinadas según las normas sobre previsiones mínimas por riesgo de incobrabilidad sobre los conceptos informados en la Sección B, punto 2. del Régimen Informativo de Deudores del Sistema Financiero."} · tramo: Previsiones mínimas exigidas: De acuerdo con la referencia indicada para el cálculo de Ipr/f.
- **N2** TextoOrdenado `TextoOrdenado_ri_rml_pdf` — Régimen Informativo Contable Mensual · {"archivo": "ri_rml.pdf", "materia": "RI Cont. Mensual - Efectivo mínimo y aplicación de recursos", "version": "Comunicación A 8453 (vigencia 12/06/2026)"} · tramo: 
- **E1** (estructural) N1 —establecida_en→ N2 · {}

## 13. `ri_dcpc::3.1.3.2` — RI:resto · aceptadas:items

Texto que vio E3 (e0, bloque de lista True; págs. 11):

```
[encabezado | punto S3]
Sección 3. CRITERIOS GENERALES
[encabezado | punto 3.1]
3.1. Criterios generales de imputación para activos financieros
[encabezado | punto 3.1.3]
3.1.3. Contrapartidas de medición de activos financieros.
[intro | punto 3.1.3]
Para los activos financieros, las contrapartidas de su medición al momento de incorporación, baja o
al cierre de cada mes se deben discriminar en función de los siguientes resultados:
[texto propio | punto 3.1.3.2]
3.1.3.2. Aplicables solo a activos financieros a valor razonable con cambios en el ORI.
- Otros Resultados Integrales – Ganancias o pérdidas por otros instrumentos a valor razonable
con cambios en ORI: se imputará la diferencia entre el valor razonable y el costo amortizado.
Cuando exista deterioro de valor crediticio para estos instrumentos, las imputaciones se
realizarán en la cuenta “Corrección de valor por pérdidas crediticias”.
- Otros Resultados Integrales – Ganancias o pérdidas por instrumentos de patrimonio designados
a valor razonable con cambios en ORI: se imputarán las diferencias que surjan de la variación del
valor razonable de instrumentos de patrimonio designados en su reconocimiento inicial a valor
razonable con cambios en ORI. Los dividendos se imputarán en “Ingresos Financieros –
Resultado por otros títulos privados”.
- Ingresos Financieros – Resultado por venta o baja en cuentas de activos financieros a valor
razonable: se imputarán los resultados que surjan por la expiración de los derechos
contractuales sobre los flujos de efectivo del activo o por transferencias que cumplen los
requisitos para la baja en cuentas. (Sección 3.2 de la NIIF 9). El resultado por la venta incluye la
reclasificación de la ganancia o pérdida acumulada en el ORI desde el patrimonio neto a esta
cuenta y, de corresponder, la diferencia entre el precio de venta y el valor razonable del activo
financiero.
Cuando a fin de un periodo mensual, el saldo de esta cuenta sea deudor, se expondrá en
“Egresos Financieros – Resultado por venta o baja”.
```

Versión: final (grafo sin cola). Nodos 11, aristas 17.
- **N1** Condicion `Condicion_existencia_de_deterioro_de_valor_crediticio__cuando_existe_deterioro_de_valor_cr_66ead0` — Existencia de deterioro de valor crediticio · {"descripcion": "Cuando existe deterioro de valor crediticio en instrumentos a valor razonable con cambios en ORI"} · tramo: Cuando exista deterioro de valor crediticio para estos instrumentos
- **N2** Condicion `Condicion_saldo_deudor_de_cuenta_resultado_venta_a_fin_de_periodo__cuando_a_fin_de_un_peri_512ef6` — Saldo deudor de cuenta resultado venta a fin de período · {"descripcion": "Cuando a fin de un período mensual el saldo de la cuenta 'Ingresos Financieros – Resultado por venta o baja' sea deudor"} · tramo: Cuando a fin de un periodo mensual, el saldo de esta cuenta sea deudor
- **N3** Obligacion `Obligacion_el_resultado_por_venta_incluye_la_reclasificacion_de_ganancia_o_perdida_acumulad_3c7785` — Incluir reclasificación ganancia/pérdida acumulada ORI · {"tipo": "asignacion", "descripcion": "El resultado por venta incluye la reclasificación de ganancia o pérdida acumulada en ORI desde patrimonio neto y la diferencia entre precio de venta y valor razonable del activo financiero"} · tramo: El resultado por la venta incluye la reclasificación de la ganancia o pérdida acumulada en el ORI desde el patrimonio neto a esta cuenta y, de corresponder, la diferencia entre el precio de venta y el valor razonable del activo financiero
- **N4** Obligacion `Obligacion_las_imputaciones_se_realizaran_en_la_cuenta_correccion_de_valor_por_perdidas_cre_ae06c6` — Imputar en cuenta corrección por pérdidas crediticias · {"tipo": "asignacion", "descripcion": "Las imputaciones se realizarán en la cuenta 'Corrección de valor por pérdidas crediticias' cuando existe deterioro de valor crediticio"} · tramo: las imputaciones se realizarán en la cuenta "Corrección de valor por pérdidas crediticias"
- **N5** Obligacion `Obligacion_los_dividendos_se_imputaran_en_ingresos_financieros_resultado_por_otros_titulos__4f2ece` — Imputar dividendos en ingresos financieros · {"tipo": "asignacion", "descripcion": "Los dividendos se imputarán en 'Ingresos Financieros – Resultado por otros títulos privados' para instrumentos de patrimonio designados a valor razonable con cambios en ORI"} · tramo: Los dividendos se imputarán en "Ingresos Financieros – Resultado por otros títulos privados"
- **N6** Obligacion `Obligacion_se_expondra_en_egresos_financieros_resultado_por_venta_o_baja_cuando_el_saldo_se_2f3384` — Exponer en egresos financieros saldo deudor · {"tipo": "presentacion_informativa", "descripcion": "Se expondrá en 'Egresos Financieros – Resultado por venta o baja' cuando el saldo sea deudor a fin de período mensual"} · tramo: se expondrá en "Egresos Financieros – Resultado por venta o baja"
- **N7** Obligacion `Obligacion_se_imputara_la_diferencia_entre_el_valor_razonable_y_el_costo_amortizado_para_ot_0a0ffb` — Imputar diferencia valor razonable-costo amortizado · {"tipo": "asignacion", "descripcion": "Se imputará la diferencia entre el valor razonable y el costo amortizado para otros instrumentos a valor razonable con cambios en ORI"} · tramo: se imputará la diferencia entre el valor razonable y el costo amortizado
- **N8** Obligacion `Obligacion_se_imputaran_en_ingresos_financieros_resultado_por_venta_o_baja_en_cuentas_de_ac_94f31e` — Imputar resultados venta o baja activos financieros · {"tipo": "asignacion", "descripcion": "Se imputarán en 'Ingresos Financieros – Resultado por venta o baja en cuentas de activos financieros a valor razonable' los resultados que surjan por expiración de derechos contractuales o transferencias que cumplen requisitos para baja en cuentas conforme Sección 3.2 de NIIF 9"} · tramo: se imputarán los resultados que surjan por la expiración de los derechos contractuales sobre los flujos de efectivo del activo o por transferencias que cumplen los requisitos para la baja en cuentas
- **N9** Obligacion `Obligacion_se_imputaran_las_diferencias_que_surjan_de_la_variacion_del_valor_razonable_de_i_265275` — Imputar diferencias variación valor razonable patrimonio · {"tipo": "asignacion", "descripcion": "Se imputarán las diferencias que surjan de la variación del valor razonable de instrumentos de patrimonio designados a valor razonable con cambios en ORI"} · tramo: se imputarán las diferencias que surjan de la variación del valor razonable de instrumentos de patrimonio designados en su reconocimiento inicial a valor razonable con cambios en ORI
- **N10** Operacion `Operacion_medicion_activos_financieros_a_valor_razonable_ori__ri_dcpc_3_1_3_2_4a1c1a` — Medición activos financieros a valor razonable ORI · {"tipo": "medición de activos financieros", "descripcion": "Medición de activos financieros a valor razonable con cambios en Otros Resultados Integrales (ORI) al momento de incorporación, baja o al cierre de cada mes"} · tramo: Aplicables solo a activos financieros a valor razonable con cambios en el ORI
- **N11** TextoOrdenado `TextoOrdenado_ri_dcpc_pdf` — Marco Contable · {"archivo": "ri_dcpc.pdf", "materia": "RI - Disposiciones complementarias al plan de cuentas", "version": "Comunicación A 8400 (vigencia 13/02/2026)"} · tramo: 
- **A1** (extraccion) N1 —condicion_de→ N4 · {}
- **E1** (estructural) N1 —establecida_en→ N11 · {}
- **A2** (extraccion) N2 —condicion_de→ N6 · {}
- **E2** (estructural) N2 —establecida_en→ N11 · {}
- **E3** (estructural) N3 —establecida_en→ N11 · {}
- **A3** (extraccion) N3 —regula→ N10 · {}
- **E4** (estructural) N4 —establecida_en→ N11 · {}
- **E5** (estructural) N5 —establecida_en→ N11 · {}
- **A4** (extraccion) N5 —regula→ N10 · {}
- **E6** (estructural) N6 —establecida_en→ N11 · {}
- **E7** (estructural) N7 —establecida_en→ N11 · {}
- **A5** (extraccion) N7 —regula→ N10 · {}
- **E8** (estructural) N8 —establecida_en→ N11 · {}
- **A6** (extraccion) N8 —regula→ N10 · {}
- **E9** (estructural) N9 —establecida_en→ N11 · {}
- **A7** (extraccion) N9 —regula→ N10 · {}
- **E10** (estructural) N10 —establecida_en→ N11 · {}

## 14. `ri_dcpc::3.2.2.1` — RI:resto · aceptadas:items

Texto que vio E3 (e0, bloque de lista True; págs. 13, 14):

```
[encabezado | punto S3]
Sección 3. CRITERIOS GENERALES
[encabezado | punto 3.2]
3.2. Criterios generales de imputación de Pasivos financieros
[encabezado | punto 3.2.2]
3.2.2. Contrapartidas de medición de pasivos financieros
[intro | punto 3.2.2]
En el caso de pasivos financieros, las contrapartidas de su medición al momento de incorporación,
baja o al cierre de cada mes se deben registrar en función del tipo de resultados en:
[texto propio | punto 3.2.2.1]
3.2.2.1. Pasivos a costo amortizado
- Egresos Financieros - Por reconocimiento inicial: incluye los resultados que surjan por la
diferencia entre el valor razonable menos los costos de transacción directamente atribuibles a la
emisión del pasivo financiero y el precio de la transacción (ver 5.1 y B5.1.1-B5.1.2 A NIIF 9).
Cuando a fin de un periodo mensual, el saldo de esta cuenta sea acreedor, se expondrá en
“Ingresos Financieros – Resultado por reconocimiento inicial de pasivos financieros”.
En los casos en que el valor razonable surja de una técnica de valoración que no utilice solo
datos de mercado observables (NIIF 9 - punto B 5.1.2 A.b) se utilizarán las cuentas de “Egresos
financieros – Intereses” que corresponda de acuerdo con el pasivo financiero involucrado, para
imputar la diferencia diferida inicialmente en las cuentas “Ajuste NIIF”.
- Egresos Financieros - Intereses y ajustes: se imputarán los resultados originados en el
devengamiento de la tasa de interés efectiva de pasivos financieros y los ajustes de capital, para
aquellos que sean actualizables por algún índice.
- Los intereses y ajustes devengados vinculados con el pasivo asociado a los activos financieros
transferidos no dados de baja se imputarán en la cuenta “Intereses por pasivos asociados a la
transferencia de activos financieros no dados de baja” –por moneda- y en la cuenta de “Ajustes
UVA/UVI por pasivos asociados a la transferencia de activos financieros no dados de baja”,
según corresponda.
- Egresos Financieros - Por baja o modificación sustancial de pasivos financieros: se imputarán los
resultados que surjan por la expiración de la obligación contractual o la modificación sustancial
de las condiciones de un pasivo financiero. (Sección 3.2 de la NIIF 9).
Cuando a fin de un periodo mensual, el saldo de esta cuenta sea acreedor, se expondrá en
“Ingresos Financieros - Resultado por baja o modificación sustancial de pasivos financieros”.
```

Versión: final (grafo sin cola). Nodos 10, aristas 10.
- **N1** Obligacion `Obligacion_las_entidades_deben_clasificar_y_medir_pasivos_financieros_a_costo_amortizado_co_127276` — Clasificación y medición pasivos financieros costo amortizado · {"tipo": "calculo", "descripcion": "Las entidades deben clasificar y medir pasivos financieros a costo amortizado, con excepciones de NIIF 9, registrando contrapartidas de medición al momento de incorporación, baja o cierre mensual según tipo de resultados"} · tramo: Los pasivos financieros comprendidos en los diversos rubros del plan de cuentas se clasificarán y medirán a costo amortizado, con las excepciones previstas por la NIIF 9 […] En el caso de pasivos financieros, las contrapartidas de su medición al momento de incorporación, baja o al cierre de cada mes
- **N2** Operacion `Operacion_baja_o_modificacion_sustancial_pasivos_financieros__ri_dcpc_3_2_2_1_668579` — Baja o modificación sustancial pasivos financieros · {"tipo": "Baja o modificación de pasivo financiero", "descripcion": "Imputación de resultados por expiración de obligación contractual o modificación sustancial de condiciones de pasivo financiero, conforme Sección 3.2 NIIF 9"} · tramo: Egresos Financieros - Por baja o modificación sustancial de pasivos financieros: se imputarán los resultados que surjan por la expiración de la obligación contractual o la modificación sustancial de las condiciones de un pasivo financiero
- **N3** Operacion `Operacion_devengamiento_tasa_interes_efectiva_pasivos__ri_dcpc_3_2_2_1_e1a672` — Devengamiento tasa interés efectiva pasivos · {"tipo": "Devengamiento de intereses", "descripcion": "Imputación de resultados originados en el devengamiento de la tasa de interés efectiva de pasivos financieros y ajustes de capital para pasivos actualizables por índice"} · tramo: Egresos Financieros - Intereses y ajustes: se imputarán los resultados originados en el devengamiento de la tasa de interés efectiva de pasivos financieros y los ajustes de capital, para aquellos que sean actualizables por algún índice
- **N4** Operacion `Operacion_imputacion_diferencia_tecnica_valoracion_pasivos__ri_dcpc_3_2_2_1_86082a` — Imputación diferencia técnica valoración pasivos · {"tipo": "Imputación contable", "descripcion": "Cuando el valor razonable surge de técnica de valoración que no utiliza solo datos de mercado observables (NIIF 9 B5.1.2 A.b), se utilizan cuentas de Egresos financieros – Intereses para imputar la diferencia diferida en cuentas Ajuste NIIF"} · tramo: se utilizarán las cuentas de "Egresos financieros – Intereses" que corresponda de acuerdo con el pasivo financiero involucrado, para imputar la diferencia diferida inicialmente en las cuentas "Ajuste NIIF"
- **N5** Operacion `Operacion_imputacion_intereses_pasivos_transferencia_activos__ri_dcpc_3_2_2_1_fa286a` — Imputación intereses pasivos transferencia activos · {"tipo": "Imputación contable", "descripcion": "Imputación de intereses y ajustes devengados vinculados con pasivos asociados a activos financieros transferidos no dados de baja, en cuentas específicas por moneda y ajustes UVA/UVI"} · tramo: Los intereses y ajustes devengados vinculados con el pasivo asociado a los activos financieros transferidos no dados de baja se imputarán en la cuenta "Intereses por pasivos asociados a la transferencia de activos financieros no dados de baja" –por moneda- y en la cuenta de "Ajustes UVA/UVI por pasi
- **N6** Operacion `Operacion_imputacion_resultados_baja_modificacion_pasivos__ri_dcpc_3_2_2_1_2594c0` — Imputación resultados baja modificación pasivos · {"tipo": "Imputación contable", "descripcion": "Cuando el saldo de la cuenta de egresos por baja o modificación sustancial sea acreedor al cierre de período mensual, se expondrá en Ingresos Financieros - Resultado por baja o modificación sustancial de pasivos financieros"} · tramo: se expondrá en "Ingresos Financieros - Resultado por baja o modificación sustancial de pasivos financieros"
- **N7** Operacion `Operacion_imputacion_resultados_reconocimiento_inicial_pasivos__ri_dcpc_3_2_2_1_2c18d9` — Imputación resultados reconocimiento inicial pasivos · {"tipo": "Imputación contable", "descripcion": "Cuando el saldo de la cuenta de egresos por reconocimiento inicial sea acreedor al cierre de período mensual, se expondrá en Ingresos Financieros – Resultado por reconocimiento inicial de pasivos financieros"} · tramo: se expondrá en "Ingresos Financieros – Resultado por reconocimiento inicial de pasivos financieros"
- **N8** Operacion `Operacion_reconocimiento_inicial_pasivos_a_costo_amortizado__ri_dcpc_3_2_2_1_d5d279` — Reconocimiento inicial pasivos a costo amortizado · {"tipo": "Reconocimiento inicial de pasivo financiero", "descripcion": "Medición inicial de pasivos financieros a costo amortizado: diferencia entre valor razonable menos costos de transacción directamente atribuibles a la emisión y el precio de la transacción, conforme NIIF 9 (5.1 y B5.1.1-B5.1.2 A)"} · tramo: Por reconocimiento inicial: incluye los resultados que surjan por la diferencia entre el valor razonable menos los costos de transacción directamente atribuibles a la emisión del pasivo financiero y el precio de la transacción
- **N9** Sujeto `Sujeto_propuesto_las_entidades__ri_dcpc` — las entidades · {"nivel": "propuesto", "cuarentena": "true", "colision_cross_to": "true", "padre_sugerido": "Sujeto_entidad_financiera", "padre_desde_sugerencia_modelo": "true"} · tramo: 
- **N10** TextoOrdenado `TextoOrdenado_ri_dcpc_pdf` — Marco Contable · {"archivo": "ri_dcpc.pdf", "materia": "RI - Disposiciones complementarias al plan de cuentas", "version": "Comunicación A 8400 (vigencia 13/02/2026)"} · tramo: 
- **A1** (extraccion) N1 —aplica_a→ N9 · {}
- **E1** (estructural) N1 —establecida_en→ N10 · {}
- **E2** (estructural) N2 —establecida_en→ N10 · {}
- **E3** (estructural) N3 —establecida_en→ N10 · {}
- **E4** (estructural) N4 —establecida_en→ N10 · {}
- **E5** (estructural) N5 —establecida_en→ N10 · {}
- **E6** (estructural) N6 —establecida_en→ N10 · {}
- **E7** (estructural) N7 —establecida_en→ N10 · {}
- **E8** (estructural) N8 —establecida_en→ N10 · {}
- **C1** (catalogo_sujetos) N9 —padre_sugerido→ Sujeto_entidad_financiera · {"flag": "padre_sugerido_no_laudado"}

## 15. `ri_dcpc::3.4.4.2` — RI:resto · aceptadas:items

Texto que vio E3 (e0, bloque de lista True; págs. 17, 18):

```
[encabezado | punto S3]
Sección 3. CRITERIOS GENERALES
[encabezado | punto 3.4]
3.4. Criterios específicos para determinados instrumentos financieros.
[encabezado | punto 3.4.4]
3.4.4. Operaciones de Pase
[intro | punto 3.4.4]
De acuerdo con los principios de baja en cuentas de la NIIF 9, estas operaciones se consideran
como financiaciones con garantía y, por tanto las registraciones deben realizarse de acuerdo con
las siguientes pautas:
[texto propio | punto 3.4.4.2]
3.4.4.2. Pases Pasivos
Las financiaciones recibidas instrumentadas mediante pases pasivos se registrarán en las cuentas
“Otras Obligaciones por Intermediación Financiera – Acreedores por pases pasivos”, clasificándolas
según quien sea la contraparte en acreedores financieros, BCRA y no financieros y atendiendo el
activo entregado en garantía.
Al cierre de cada mes, los intereses devengados a pagar se imputarán en la cuenta “Otras
obligaciones por intermediación financiera - Intereses devengados a pagar por pases pasivos” o
“Intereses devengados a pagar por pases pasivos con el B.C.R.A.” con contrapartida en “Egresos
Financieros - Intereses por pases pasivos con el Sector Financiero”, Intereses por pases pasivos
con el B.C.R.A. o “Intereses por otros pases pasivos”, según corresponda.
En estas operaciones, cuando el receptor del activo subyacente obtiene el derecho a venderlo o
pignorarlo, éste se reclasificará a las cuentas “Otros Créditos por Intermediación Financiera -
Compras a término por operaciones de pase pasivo”, según el tipo de subyacente. A fin de cada
mes, estos activos se medirán de acuerdo con la categoría que poseían antes de la operación de
pase, y los resultados se registrarán en las cuentas que correspondan según el tipo de activo.
```

Versión: final (grafo sin cola). Nodos 8, aristas 16.
- **N1** Condicion `Condicion_receptor_obtiene_derecho_a_vender_o_pignorar_activo_subyacente__cuando_el_recept_3248b7` — Receptor obtiene derecho a vender o pignorar activo subyacente · {"descripcion": "Cuando el receptor del activo subyacente obtiene el derecho a venderlo o pignorarlo"} · tramo: cuando el receptor del activo subyacente obtiene el derecho a venderlo o pignorarlo
- **N2** Obligacion `Obligacion_a_fin_de_cada_mes_los_activos_se_mediran_de_acuerdo_con_la_categoria_que_poseian_f5d22d` — Medición de activos a fin de mes — pase pasivo · {"tipo": "presentacion_informativa", "descripcion": "A fin de cada mes, los activos se medirán de acuerdo con la categoría que poseían antes de la operación de pase, y los resultados se registrarán en las cuentas que correspondan según el tipo de activo", "umbrales": [{"tramo": "A fin de cada mes", "comparacion": "no_determinada", "regla_comparacion": "limite_relativo:sin_marcador", "origen": "e1" · tramo: A fin de cada mes, estos activos se medirán de acuerdo con la categoría que poseían antes de la operación de pase, y los resultados se registrarán en las cuentas que correspondan según el tipo de activo
- **N3** Obligacion `Obligacion_al_cierre_de_cada_mes_los_intereses_devengados_a_pagar_se_imputaran_en_la_cuenta_db0a2d` — Imputación de intereses devengados — pases pasivos · {"tipo": "presentacion_informativa", "descripcion": "Al cierre de cada mes, los intereses devengados a pagar se imputarán en la cuenta correspondiente según la contraparte (Otras obligaciones por intermediación financiera - Intereses devengados a pagar por pases pasivos, o Intereses devengados a pagar por pases pasivos con el B.C.R.A.), con contrapartida en Egresos Financieros según corresponda",  · tramo: Al cierre de cada mes, los intereses devengados a pagar se imputarán en la cuenta "Otras obligaciones por intermediación financiera - Intereses devengados a pagar por pases pasivos" o "Intereses devengados a pagar por pases pasivos con el B.C.R.A." con contrapartida en "Egresos Financieros - Interes
- **N4** Obligacion `Obligacion_el_activo_subyacente_se_reclasificara_a_las_cuentas_otros_creditos_por_intermedi_d49aab` — Reclasificación a cuentas de compras a término — pase pasivo · {"tipo": "presentacion_informativa", "descripcion": "El activo subyacente se reclasificará a las cuentas 'Otros Créditos por Intermediación Financiera - Compras a término por operaciones de pase pasivo', según el tipo de subyacente"} · tramo: éste se reclasificará a las cuentas "Otros Créditos por Intermediación Financiera - Compras a término por operaciones de pase pasivo", según el tipo de subyacente
- **N5** Obligacion `Obligacion_las_financiaciones_recibidas_mediante_pases_pasivos_se_registraran_en_las_cuenta_9f414e` — Registración en cuentas — pases pasivos · {"tipo": "presentacion_informativa", "descripcion": "Las financiaciones recibidas mediante pases pasivos se registrarán en las cuentas 'Otras Obligaciones por Intermediación Financiera – Acreedores por pases pasivos', clasificándolas según la contraparte (acreedores financieros, BCRA y no financieros) y el activo entregado en garantía"} · tramo: se registrarán en las cuentas "Otras Obligaciones por Intermediación Financiera – Acreedores por pases pasivos", clasificándolas según quien sea la contraparte en acreedores financieros, BCRA y no financieros y atendiendo el activo entregado en garantía
- **N6** Operacion `Operacion_pases_pasivos_financiaciones_recibidas__ri_dcpc_3_4_4_2_4f167d` — Pases pasivos — financiaciones recibidas · {"tipo": "Pase pasivo", "descripcion": "Financiaciones recibidas instrumentadas mediante pases pasivos, registradas según la contraparte (acreedores financieros, BCRA y no financieros) y el activo entregado en garantía"} · tramo: Las financiaciones recibidas instrumentadas mediante pases pasivos
- **N7** Sujeto `Sujeto_propuesto_las_entidades__ri_dcpc` — las entidades · {"nivel": "propuesto", "cuarentena": "true", "colision_cross_to": "true", "padre_sugerido": "Sujeto_entidad_financiera", "padre_desde_sugerencia_modelo": "true"} · tramo: 
- **N8** TextoOrdenado `TextoOrdenado_ri_dcpc_pdf` — Marco Contable · {"archivo": "ri_dcpc.pdf", "materia": "RI - Disposiciones complementarias al plan de cuentas", "version": "Comunicación A 8400 (vigencia 13/02/2026)"} · tramo: 
- **A1** (extraccion) N1 —condicion_de→ N4 · {}
- **E1** (estructural) N1 —establecida_en→ N8 · {}
- **A2** (extraccion) N2 —aplica_a→ N7 · {}
- **E2** (estructural) N2 —establecida_en→ N8 · {}
- **A3** (extraccion) N2 —regula→ N6 · {}
- **A4** (extraccion) N3 —aplica_a→ N7 · {}
- **E3** (estructural) N3 —establecida_en→ N8 · {}
- **A5** (extraccion) N3 —regula→ N6 · {}
- **A6** (extraccion) N4 —aplica_a→ N7 · {}
- **E4** (estructural) N4 —establecida_en→ N8 · {}
- **A7** (extraccion) N4 —regula→ N6 · {}
- **A8** (extraccion) N5 —aplica_a→ N7 · {}
- **E5** (estructural) N5 —establecida_en→ N8 · {}
- **A9** (extraccion) N5 —regula→ N6 · {}
- **E6** (estructural) N6 —establecida_en→ N8 · {}
- **C1** (catalogo_sujetos) N7 —padre_sugerido→ Sujeto_entidad_financiera · {"flag": "padre_sugerido_no_laudado"}

## 16. `ceninf::5.1.2.4` — NG:sin_raiz · aceptadas:items

Texto que vio E3 (e0, bloque de lista True; págs. 18):

```
[encabezado | punto S5]
Sección 5. Central de Facturas de Crédito Electrónicas MiPyME impagas al vencimiento.
[encabezado | punto 5.1]
5.1. Consultas puntuales.
[intro | punto 5.1.2]
5.1.2. Los datos a publicar en la Central de Facturas de Crédito Electrónicas MiPyME
impagas al vencimiento (CenFIV) corresponderán a las FCEM que utilizaren co-
mo canal de negociación al Sistema de Circulación Abierta y se exhibirán de for-
ma agregada, por CUIT de las empresas deudoras de acuerdo con lo detallado a
continuación:
[texto propio | punto 5.1.2.4]
5.1.2.4. Promedio de días de atraso: es el cociente entre la sumatoria de la
cantidad de días de mora de todas las facturas impagas reportadas y
la cantidad total de facturas impagas, en el período considerado.
```

Versión: final (grafo sin cola). Nodos 2, aristas 1.
- **N1** Definicion `Definicion_promedio_de_dias_de_atraso__cociente_entre_la_sumatoria_de_la_cantidad_de_dias_d_c0a7b9` — Promedio de días de atraso · {"termino": "Promedio de días de atraso", "descripcion": "cociente entre la sumatoria de la cantidad de días de mora de todas las facturas impagas reportadas y la cantidad total de facturas impagas, en el período considerado"} · tramo: Promedio de días de atraso: es el cociente entre la sumatoria de la cantidad de días de mora de todas las facturas impagas reportadas y la cantidad total de facturas impagas, en el período considerado.
- **N2** TextoOrdenado `TextoOrdenado_ceninf_pdf` — Centrales de Información · {"archivo": "ceninf.pdf", "materia": "Centrales de información", "version": "Comunicación A 8393 (vigencia 01/03/2026)"} · tramo: 
- **E1** (estructural) N1 —establecida_en→ N2 · {}

## 17. `nmcief::A6::Sbloque12` — NG:sin_raiz · aceptadas:items

Texto que vio E3 (e0, bloque de lista True; págs. 33):

```
[encabezado | punto A6]
Anexo VI
[intersticial | punto A6::S0]
Procedimientos mínimos de auditoría a aplicar en oportunidad de la revisión del ciclo para
cada ejercicio:
[texto propio | punto A6::Sbloque12]
Desarrollo, adquisición y mantenimiento de “software”
Evaluar los Requisitos para los sistemas y aplicaciones, considerando la verificación de los
siguientes aspectos:
- Controles automatizados definidos en la normativa vigente.
- Controles para la identificación única del cliente y el registro de los datos obligatorios.
Asimismo, evaluar que se realicen procesos periódicos de control y depuración.
- Esquemas de autorización acordes a la política de control de accesos para el ingreso,
modificación y baja de operaciones y parámetros.
- Funcionalidad para la gestión de usuarios y perfiles, y la asignación de permisos sobre
las funciones del sistema.
- Funciones que permitan ejercer un control sobre la asignación de perfiles de acuerdo
con los roles y funciones establecidos por la entidad.
- Registros de auditoría que permitan asegurar la trazabilidad de cada una de las acciones
realizadas.
- Documentación funcional, técnica y de usuario actualizadas de los sistemas de
información.
Evaluar los requisitos para la generación de los regímenes informativos. Verificar los sis-
temas o procesos automatizados para la generación de los regímenes informativos requeri-
dos por el BCRA.
```

Versión: final (grafo sin cola). Nodos 12, aristas 18.
- **N1** Condicion `Condicion_control_sobre_asignacion_de_perfiles_segun_roles__que_existan_funciones_que_perm_d62817` — Control sobre asignación de perfiles según roles · {"descripcion": "Que existan funciones que permitan ejercer un control sobre la asignación de perfiles de acuerdo con los roles y funciones establecidos por la entidad."} · tramo: Funciones que permitan ejercer un control sobre la asignación de perfiles de acuerdo con los roles y funciones establecidos por la entidad.
- **N2** Condicion `Condicion_controles_automatizados_definidos_en_normativa_vigente__que_existan_controles_au_1aab0a` — Controles automatizados definidos en normativa vigente · {"descripcion": "Que existan controles automatizados definidos en la normativa vigente aplicable."} · tramo: Controles automatizados definidos en la normativa vigente.
- **N3** Condicion `Condicion_documentacion_funcional_tecnica_y_de_usuario_actualizadas__que_exista_documentac_29d894` — Documentación funcional, técnica y de usuario actualizadas · {"descripcion": "Que exista documentación funcional, técnica y de usuario actualizadas de los sistemas de información."} · tramo: Documentación funcional, técnica y de usuario actualizadas de los sistemas de información.
- **N4** Condicion `Condicion_esquemas_de_autorizacion_acordes_a_politica_de_control_de_accesos__que_existan_e_9fce33` — Esquemas de autorización acordes a política de control de accesos · {"descripcion": "Que existan esquemas de autorización acordes a la política de control de accesos para el ingreso, modificación y baja de operaciones y parámetros."} · tramo: Esquemas de autorización acordes a la política de control de accesos para el ingreso, modificación y baja de operaciones y parámetros.
- **N5** Condicion `Condicion_funcionalidad_gestion_de_usuarios_y_perfiles__que_exista_funcionalidad_para_la_g_723976` — Funcionalidad gestión de usuarios y perfiles · {"descripcion": "Que exista funcionalidad para la gestión de usuarios y perfiles, y la asignación de permisos sobre las funciones del sistema."} · tramo: Funcionalidad para la gestión de usuarios y perfiles, y la asignación de permisos sobre las funciones del sistema.
- **N6** Condicion `Condicion_identificacion_unica_del_cliente_y_registro_de_datos_obligatorios__que_existan_c_8e6b4a` — Identificación única del cliente y registro de datos obligatorios · {"descripcion": "Que existan controles para la identificación única del cliente y el registro de los datos obligatorios."} · tramo: Controles para la identificación única del cliente y el registro de los datos obligatorios.
- **N7** Condicion `Condicion_registros_de_auditoria_para_trazabilidad__que_existan_registros_de_auditoria_que_cd659a` — Registros de auditoría para trazabilidad · {"descripcion": "Que existan registros de auditoría que permitan asegurar la trazabilidad de cada una de las acciones realizadas."} · tramo: Registros de auditoría que permitan asegurar la trazabilidad de cada una de las acciones realizadas.
- **N8** Obligacion `Obligacion_evaluar_los_requisitos_para_la_generacion_de_los_regimenes_informativos_y_verifi_88c928` — Evaluar requisitos regímenes informativos · {"descripcion": "Evaluar los requisitos para la generación de los regímenes informativos y verificar los sistemas o procesos automatizados para la generación de los regímenes informativos requeridos por el BCRA.", "tipo": "otra"} · tramo: Evaluar los requisitos para la generación de los regímenes informativos. Verificar los sistemas o procesos automatizados para la generación de los regímenes informativos requeridos por el BCRA.
- **N9** Obligacion `Obligacion_evaluar_los_requisitos_para_los_sistemas_y_aplicaciones_considerando_la_verifica_decc49` — Evaluar requisitos sistemas y aplicaciones · {"descripcion": "Evaluar los Requisitos para los sistemas y aplicaciones, considerando la verificación de controles automatizados definidos en la normativa vigente, controles para la identificación única del cliente y el registro de datos obligatorios, esquemas de autorización acordes a la política de control de accesos, funcionalidad para la gestión de usuarios y perfiles, funciones de control so · tramo: Evaluar los Requisitos para los sistemas y aplicaciones, considerando la verificación de los siguientes aspectos:
- **N10** Obligacion `Obligacion_evaluar_que_se_realicen_procesos_periodicos_de_control_y_depuracion_de_los_siste_230eb2` — Procesos periódicos de control y depuración · {"descripcion": "Evaluar que se realicen procesos periódicos de control y depuración de los sistemas de información.", "tipo": "otra"} · tramo: Asimismo, evaluar que se realicen procesos periódicos de control y depuración.
- **N11** Operacion `Operacion_desarrollo_adquisicion_y_mantenimiento_de_software__nmcief_a6_sbloque12_111bd1` — Desarrollo, adquisición y mantenimiento de software · {"tipo": "Actividad de tecnología de la información", "descripcion": "Desarrollo, adquisición y mantenimiento de software en sistemas de información y aplicativos de la entidad."} · tramo: Desarrollo, adquisición y mantenimiento de "software"
- **N12** TextoOrdenado `TextoOrdenado_nmcief_pdf` — Normas de Capitales Mínimos · {"archivo": "nmcief.pdf", "materia": "Normas mínimas sobre controles internos para entidades financieras", "version": "Comunicación A 8168 (vigencia 01/01/2025)"} · tramo: 
- **A1** (extraccion) N1 —condicion_de→ N9 · {}
- **E1** (estructural) N1 —establecida_en→ N12 · {}
- **A2** (extraccion) N2 —condicion_de→ N9 · {}
- **E2** (estructural) N2 —establecida_en→ N12 · {}
- **A3** (extraccion) N3 —condicion_de→ N9 · {}
- **E3** (estructural) N3 —establecida_en→ N12 · {}
- **A4** (extraccion) N4 —condicion_de→ N9 · {}
- **E4** (estructural) N4 —establecida_en→ N12 · {}
- **A5** (extraccion) N5 —condicion_de→ N9 · {}
- **E5** (estructural) N5 —establecida_en→ N12 · {}
- **A6** (extraccion) N6 —condicion_de→ N9 · {}
- **E6** (estructural) N6 —establecida_en→ N12 · {}
- **A7** (extraccion) N7 —condicion_de→ N9 · {}
- **E7** (estructural) N7 —establecida_en→ N12 · {}
- **E8** (estructural) N8 —establecida_en→ N12 · {}
- **E9** (estructural) N9 —establecida_en→ N12 · {}
- **E10** (estructural) N10 —establecida_en→ N12 · {}
- **E11** (estructural) N11 —establecida_en→ N12 · {}

## 18. `nmcief::A6::Sbloque13` — NG:sin_raiz · aceptadas:items

Texto que vio E3 (e0, bloque de lista True; págs. 33):

```
[encabezado | punto A6]
Anexo VI
[intersticial | punto A6::S0]
Procedimientos mínimos de auditoría a aplicar en oportunidad de la revisión del ciclo para
cada ejercicio:
[texto propio | punto A6::Sbloque13]
Gestión de la relación con terceras partes
Evaluar las condiciones generales para las delegaciones de procesos, servicios y/o activi-
dades vinculadas con los procesos de tecnología y seguridad de la información y verificar
el establecimiento de un sector o una función responsable de la gestión de la relación con
las terceras partes, en función de los operaciones, procesos y estructura de la entidad.
Evaluar la política y el marco de gestión de procesos, servicios y/o actividades delegadas
en terceras partes.
Con respecto a la formalización de la relación, evaluar que la entidad formalice las relacio-
nes con terceras partes que brinden procesos, servicios y/o actividades delegadas de
acuerdo con los procedimientos establecidos. Para ello se evaluará el funcionamiento de
este control aplicado a aquellos servicios, procesos y/o actividades delegadas que la audi-
toría interna determine como de criticidad alta o relevantes para el negocio, en función de
los resultados de la gestión de riesgos de tecnología y seguridad de la información aplica-
dos a este tipo de activos.
En relación con los aspectos del control y monitoreo de estas actividades, evaluar el proce-
so de control que permita realizar un seguimiento y evaluación de los procesos, servicios y
actividades de tecnología y seguridad de la información delegados en terceras partes.
```

Versión: final (grafo sin cola). Nodos 8, aristas 9.
- **N1** Condicion `Condicion_servicios_delegados_de_criticidad_alta_o_relevantes__servicios_procesos_y_o_acti_332a13` — Servicios delegados de criticidad alta o relevantes · {"descripcion": "Servicios, procesos y/o actividades delegadas que la auditoría interna determine como de criticidad alta o relevantes para el negocio, en función de los resultados de la gestión de riesgos de tecnología y seguridad de la información"} · tramo: aquellos servicios, procesos y/o actividades delegadas que la auditoría interna determine como de criticidad alta o relevantes para el negocio
- **N2** Obligacion `Obligacion_evaluar_el_funcionamiento_del_control_de_formalizacion_aplicado_a_aquellos_servi_d51eff` — Evaluación de funcionamiento de control en servicios críticos · {"tipo": "otra", "descripcion": "Evaluar el funcionamiento del control de formalización aplicado a aquellos servicios, procesos y/o actividades delegadas que la auditoría interna determine como de criticidad alta o relevantes para el negocio, en función de los resultados de la gestión de riesgos de tecnología y seguridad de la información"} · tramo: se evaluará el funcionamiento de este control aplicado a aquellos servicios, procesos y/o actividades delegadas que la auditoría interna determine como de criticidad alta o relevantes para el negocio
- **N3** Obligacion `Obligacion_evaluar_el_proceso_de_control_que_permita_realizar_un_seguimiento_y_evaluacion_d_cbd782` — Evaluación de proceso de control y monitoreo de actividades delegadas · {"tipo": "otra", "descripcion": "Evaluar el proceso de control que permita realizar un seguimiento y evaluación de los procesos, servicios y actividades de tecnología y seguridad de la información delegados en terceras partes"} · tramo: evaluar el proceso de control que permita realizar un seguimiento y evaluación de los procesos, servicios y actividades de tecnología y seguridad de la información delegados en terceras partes
- **N4** Obligacion `Obligacion_evaluar_la_politica_y_el_marco_de_gestion_de_procesos_servicios_y_o_actividades__8ae849` — Evaluación de política y marco de gestión de procesos delegados · {"tipo": "otra", "descripcion": "Evaluar la política y el marco de gestión de procesos, servicios y/o actividades delegadas en terceras partes"} · tramo: Evaluar la política y el marco de gestión de procesos, servicios y/o actividades delegadas en terceras partes
- **N5** Obligacion `Obligacion_evaluar_que_la_entidad_formalice_las_relaciones_con_terceras_partes_que_brinden__a3e8fc` — Formalización de relaciones con terceras partes · {"tipo": "otra", "descripcion": "Evaluar que la entidad formalice las relaciones con terceras partes que brinden procesos, servicios y/o actividades delegadas de acuerdo con los procedimientos establecidos"} · tramo: evaluar que la entidad formalice las relaciones con terceras partes que brinden procesos, servicios y/o actividades delegadas de acuerdo con los procedimientos establecidos
- **N6** Obligacion `Obligacion_verificar_el_establecimiento_de_un_sector_o_una_funcion_responsable_de_la_gestio_20c2c4` — Establecimiento de sector responsable de gestión con terceras partes · {"tipo": "otra", "descripcion": "Verificar el establecimiento de un sector o una función responsable de la gestión de la relación con las terceras partes, en función de los operaciones, procesos y estructura de la entidad"} · tramo: verificar el establecimiento de un sector o una función responsable de la gestión de la relación con las terceras partes
- **N7** Operacion `Operacion_delegacion_de_procesos_servicios_y_actividades_de_tecnologia__nmcief_a6_sbloque1_b929f8` — Delegación de procesos, servicios y actividades de tecnología · {"tipo": "delegación de procesos y servicios", "descripcion": "Delegación de procesos, servicios y/o actividades vinculadas con los procesos de tecnología y seguridad de la información en terceras partes"} · tramo: delegaciones de procesos, servicios y/o actividades vinculadas con los procesos de tecnología y seguridad de la información
- **N8** TextoOrdenado `TextoOrdenado_nmcief_pdf` — Normas de Capitales Mínimos · {"archivo": "nmcief.pdf", "materia": "Normas mínimas sobre controles internos para entidades financieras", "version": "Comunicación A 8168 (vigencia 01/01/2025)"} · tramo: 
- **A1** (extraccion) N1 —condicion_de→ N2 · {}
- **E1** (estructural) N1 —establecida_en→ N8 · {}
- **E2** (estructural) N2 —establecida_en→ N8 · {}
- **E3** (estructural) N3 —establecida_en→ N8 · {}
- **E4** (estructural) N4 —establecida_en→ N8 · {}
- **E5** (estructural) N5 —establecida_en→ N8 · {}
- **A2** (extraccion) N5 —regula→ N7 · {}
- **E6** (estructural) N6 —establecida_en→ N8 · {}
- **E7** (estructural) N7 —establecida_en→ N8 · {}

## 19. `nmcief::A6::Sbloque8` — NG:sin_raiz · aceptadas:items

Texto que vio E3 (e0, bloque de lista True; págs. 32):

```
[encabezado | punto A6]
Anexo VI
[intersticial | punto A6::S0]
Procedimientos mínimos de auditoría a aplicar en oportunidad de la revisión del ciclo para
cada ejercicio:
[texto propio | punto A6::Sbloque8]
Anexo VI
En relación con la gestión de crisis y estrategias de comunicación, evaluar la designación
de los responsables, la elaboración de planes de gestión de crisis y los procedimientos de-
finidos para tal fin.
Evaluar el plan de ejercicios y pruebas de los planes de continuidad del negocio definido
por la entidad. Verificar que se contemple al menos uno de los escenarios de más alta criti-
cidad. Evaluar los resultados de las pruebas. Verificar que se mantenga un registro detalla-
do de los resultados de cada ejercicio, las observaciones y problemas detectados, y los
planes de acción definidos para su corrección.
```

Versión: final (grafo sin cola). Nodos 6, aristas 6.
- **N1** Condicion `Condicion_contemplar_escenario_de_alta_criticidad__el_plan_de_ejercicios_y_pruebas_debe_co_90867d` — Contemplar escenario de alta criticidad · {"descripcion": "El plan de ejercicios y pruebas debe contemplar al menos uno de los escenarios de más alta criticidad.", "umbrales": [{"tramo": "al menos uno", "comparacion": "minimo_inclusivo", "regla_comparacion": "limite_relativo:compuesta:al_menos", "origen": "e1", "tramo_verificado": "exacta"}]} · tramo: Verificar que se contemple al menos uno de los escenarios de más alta criticidad.
- **N2** Obligacion `Obligacion_la_auditoria_interna_debe_evaluar_el_plan_de_ejercicios_y_pruebas_de_los_planes__ca3c0f` — Evaluar plan de ejercicios y pruebas de continuidad · {"descripcion": "La auditoría interna debe evaluar el plan de ejercicios y pruebas de los planes de continuidad del negocio definido por la entidad.", "tipo": "otra"} · tramo: Evaluar el plan de ejercicios y pruebas de los planes de continuidad del negocio definido por la entidad.
- **N3** Obligacion `Obligacion_la_auditoria_interna_debe_evaluar_la_designacion_de_responsables_la_elaboracion__367a2a` — Evaluar gestión de crisis y comunicación · {"descripcion": "La auditoría interna debe evaluar la designación de responsables, la elaboración de planes de gestión de crisis y los procedimientos definidos para tal fin, en relación con la gestión de crisis y estrategias de comunicación.", "tipo": "otra"} · tramo: En relación con la gestión de crisis y estrategias de comunicación, evaluar la designación de los responsables, la elaboración de planes de gestión de crisis y los procedimientos definidos para tal fin.
- **N4** Obligacion `Obligacion_la_auditoria_interna_debe_evaluar_los_resultados_de_las_pruebas_de_los_planes_de_a45d06` — Evaluar resultados de pruebas de continuidad · {"descripcion": "La auditoría interna debe evaluar los resultados de las pruebas de los planes de continuidad del negocio.", "tipo": "otra"} · tramo: Evaluar los resultados de las pruebas.
- **N5** Obligacion `Obligacion_la_auditoria_interna_debe_verificar_que_se_mantenga_un_registro_detallado_de_los_d45c02` — Verificar registro detallado de resultados de ejercicios · {"descripcion": "La auditoría interna debe verificar que se mantenga un registro detallado de los resultados de cada ejercicio, las observaciones y problemas detectados, y los planes de acción definidos para su corrección.", "tipo": "otra"} · tramo: Verificar que se mantenga un registro detallado de los resultados de cada ejercicio, las observaciones y problemas detectados, y los planes de acción definidos para su corrección.
- **N6** TextoOrdenado `TextoOrdenado_nmcief_pdf` — Normas de Capitales Mínimos · {"archivo": "nmcief.pdf", "materia": "Normas mínimas sobre controles internos para entidades financieras", "version": "Comunicación A 8168 (vigencia 01/01/2025)"} · tramo: 
- **A1** (extraccion) N1 —condicion_de→ N2 · {}
- **E1** (estructural) N1 —establecida_en→ N6 · {}
- **E2** (estructural) N2 —establecida_en→ N6 · {}
- **E3** (estructural) N3 —establecida_en→ N6 · {}
- **E4** (estructural) N4 —establecida_en→ N6 · {}
- **E5** (estructural) N5 —establecida_en→ N6 · {}

## 20. `nmcief::A6::Sbloque9` — NG:sin_raiz · aceptadas:items

Texto que vio E3 (e0, bloque de lista True; págs. 32):

```
[encabezado | punto A6]
Anexo VI
[intersticial | punto A6::S0]
Procedimientos mínimos de auditoría a aplicar en oportunidad de la revisión del ciclo para
cada ejercicio:
[texto propio | punto A6::Sbloque9]
Infraestructura tecnológica y procesamiento
En relación con la Gestión de la infraestructura tecnológica, evaluar las estructuras, proce-
sos y procedimientos definidos por la entidad para llevar a cabo las actividades de gestión
de actualizaciones y configuraciones, la implementación de cambios, el monitoreo de la in-
fraestructura, la operación de los sistemas y la gestión de las comunicaciones. Asimismo,
se deberá verificar el proceso establecido para la gestión del registro y la respuesta de la
demanda de servicios de tecnología.
Evaluar el proceso de Gestión de cambios. Verificar que el mismo permita registrar, evaluar,
planificar, revisar, aprobar y comunicar los cambios en los activos de información antes de
la implementación en entornos productivos.
Sobre la Actualización de la infraestructura tecnológica, evaluar el proceso de gestión de
actualizaciones de infraestructura tecnológica, acorde con la arquitectura empresarial defi-
nida. Evaluar el proceso de gestión de las configuraciones. Evaluar el proceso de gestión
de actualizaciones de seguridad.
Evaluar el proceso para la gestión de las comunicaciones.
En relación con el Procesamiento de datos, evaluar los procesos de gestión, ejecución,
monitoreo y control de las operaciones de tecnología.
```

Versión: final (grafo sin cola). Nodos 10, aristas 9.
- **N1** Obligacion `Obligacion_evaluar_el_proceso_de_gestion_de_actualizaciones_de_infraestructura_tecnologica__66ec1e` — Evaluar proceso gestión actualizaciones infraestructura tecnológica · {"descripcion": "Evaluar el proceso de gestión de actualizaciones de infraestructura tecnológica, acorde con la arquitectura empresarial definida.", "tipo": "otra"} · tramo: Sobre la Actualización de la infraestructura tecnológica, evaluar el proceso de gestión de actualizaciones de infraestructura tecnológica, acorde con la arquitectura empresarial definida.
- **N2** Obligacion `Obligacion_evaluar_el_proceso_de_gestion_de_actualizaciones_de_seguridad__nmcief_a6_sbloque_88973f` — Evaluar proceso gestión actualizaciones seguridad · {"descripcion": "Evaluar el proceso de gestión de actualizaciones de seguridad.", "tipo": "otra"} · tramo: Evaluar el proceso de gestión de actualizaciones de seguridad.
- **N3** Obligacion `Obligacion_evaluar_el_proceso_de_gestion_de_cambios__nmcief_a6_sbloque9_95beac` — Evaluar proceso Gestión de cambios · {"descripcion": "Evaluar el proceso de Gestión de cambios.", "tipo": "otra"} · tramo: Evaluar el proceso de Gestión de cambios.
- **N4** Obligacion `Obligacion_evaluar_el_proceso_de_gestion_de_las_configuraciones__nmcief_a6_sbloque9_6e5ff3` — Evaluar proceso gestión configuraciones · {"descripcion": "Evaluar el proceso de gestión de las configuraciones.", "tipo": "otra"} · tramo: Evaluar el proceso de gestión de las configuraciones.
- **N5** Obligacion `Obligacion_evaluar_el_proceso_para_la_gestion_de_las_comunicaciones__nmcief_a6_sbloque9_952a74` — Evaluar proceso gestión comunicaciones · {"descripcion": "Evaluar el proceso para la gestión de las comunicaciones.", "tipo": "otra"} · tramo: Evaluar el proceso para la gestión de las comunicaciones.
- **N6** Obligacion `Obligacion_evaluar_las_estructuras_procesos_y_procedimientos_definidos_por_la_entidad_para__f24339` — Evaluar gestión infraestructura tecnológica · {"descripcion": "Evaluar las estructuras, procesos y procedimientos definidos por la entidad para llevar a cabo las actividades de gestión de actualizaciones y configuraciones, la implementación de cambios, el monitoreo de la infraestructura, la operación de los sistemas y la gestión de las comunicaciones.", "tipo": "otra"} · tramo: En relación con la Gestión de la infraestructura tecnológica, evaluar las estructuras, procesos y procedimientos definidos por la entidad para llevar a cabo las actividades de gestión de actualizaciones y configuraciones, la implementación de cambios, el monitoreo de la infraestructura, la operación
- **N7** Obligacion `Obligacion_evaluar_los_procesos_de_gestion_ejecucion_monitoreo_y_control_de_las_operaciones_b79c6c` — Evaluar procesos gestión ejecución monitoreo control operaciones tecnología · {"descripcion": "Evaluar los procesos de gestión, ejecución, monitoreo y control de las operaciones de tecnología en relación con el Procesamiento de datos.", "tipo": "otra"} · tramo: En relación con el Procesamiento de datos, evaluar los procesos de gestión, ejecución, monitoreo y control de las operaciones de tecnología.
- **N8** Obligacion `Obligacion_verificar_el_proceso_establecido_para_la_gestion_del_registro_y_la_respuesta_de__450204` — Verificar proceso gestión registro y respuesta demanda servicios · {"descripcion": "Verificar el proceso establecido para la gestión del registro y la respuesta de la demanda de servicios de tecnología.", "tipo": "otra"} · tramo: se deberá verificar el proceso establecido para la gestión del registro y la respuesta de la demanda de servicios de tecnología.
- **N9** Obligacion `Obligacion_verificar_que_el_proceso_de_gestion_de_cambios_permita_registrar_evaluar_planifi_50dab8` — Verificar registro evaluación planificación revisión aprobación comunicación cambios · {"descripcion": "Verificar que el proceso de Gestión de cambios permita registrar, evaluar, planificar, revisar, aprobar y comunicar los cambios en los activos de información antes de la implementación en entornos productivos.", "tipo": "otra"} · tramo: Verificar que el mismo permita registrar, evaluar, planificar, revisar, aprobar y comunicar los cambios en los activos de información antes de la implementación en entornos productivos.
- **N10** TextoOrdenado `TextoOrdenado_nmcief_pdf` — Normas de Capitales Mínimos · {"archivo": "nmcief.pdf", "materia": "Normas mínimas sobre controles internos para entidades financieras", "version": "Comunicación A 8168 (vigencia 01/01/2025)"} · tramo: 
- **E1** (estructural) N1 —establecida_en→ N10 · {}
- **E2** (estructural) N2 —establecida_en→ N10 · {}
- **E3** (estructural) N3 —establecida_en→ N10 · {}
- **E4** (estructural) N4 —establecida_en→ N10 · {}
- **E5** (estructural) N5 —establecida_en→ N10 · {}
- **E6** (estructural) N6 —establecida_en→ N10 · {}
- **E7** (estructural) N7 —establecida_en→ N10 · {}
- **E8** (estructural) N8 —establecida_en→ N10 · {}
- **E9** (estructural) N9 —establecida_en→ N10 · {}

## 21. `expaef::9.6.4` — NG:resto · aceptadas:items

Texto que vio E3 (e0, bloque de lista True; págs. 25):

```
[encabezado | punto S9]
Sección 9. Agencias complementarias de servicios financieros.
[encabezado | punto 9.6]
9.6. Contrato de delegación de actividades entre la entidad financiera y la agencia complementaria
de servicios financieros.
[intro | punto 9.6]
El contrato de delegación deberá contener como mínimo cláusulas con los siguientes concep-
tos:
[texto propio | punto 9.6.4]
9.6.4. Prohibición de ceder el contrato o de subcontratar.
```

Versión: final (grafo sin cola). Nodos 2, aristas 1.
- **N1** Restriccion `Restriccion_la_entidad_financiera_no_podra_ceder_el_contrato_de_delegacion_de_actividades_ni_fe8360` — Prohibición de ceder contrato o subcontratar · {"tipo": "prohibicion", "descripcion": "La entidad financiera no podrá ceder el contrato de delegación de actividades ni subcontratar con terceros las actividades delegadas a la agencia complementaria de servicios financieros."} · tramo: Prohibición de ceder el contrato o de subcontratar
- **N2** TextoOrdenado `TextoOrdenado_expaef_pdf` — Autorización de sucursales · {"archivo": "expaef.pdf", "materia": "Expansión de entidades financieras", "version": "Comunicación A 8401 (vigencia 06/02/2026)"} · tramo: 
- **E1** (estructural) N1 —establecida_en→ N2 · {}

## 22. `cirmo3::8.4.1.2` — NG:resto · aceptadas:items

Texto que vio E3 (e0, bloque de lista True; págs. 89):

```
[encabezado | punto S8]
Sección 8. Cheques cancelatorios.
[encabezado | punto 8.4]
8.4. Cobro de CHC en las entidades financieras.
[encabezado | punto 8.4.1]
8.4.1. Verificación de documentos.
[intro | punto 8.4.1]
La entidad financiera deberá:
[texto propio | punto 8.4.1.2]
8.4.1.2. Verificar que el CHC sea presentado al cobro por el beneficiario final que resulte de
acuerdo con los datos consignados al dorso del documento o por el propio compra-
dor.
```

Versión: final (grafo sin cola). Nodos 4, aristas 4.
- **N1** Obligacion `Obligacion_la_entidad_financiera_debera_verificar_que_el_cheque_cancelatorio_sea_presentado_6a7414` — Verificar presentación de CHC por beneficiario final · {"tipo": "presentacion_informativa", "descripcion": "La entidad financiera deberá verificar que el cheque cancelatorio sea presentado al cobro por el beneficiario final que resulte de acuerdo con los datos consignados al dorso del documento o por el propio comprador."} · tramo: Verificar que el CHC sea presentado al cobro por el beneficiario final que resulte de acuerdo con los datos consignados al dorso del documento o por el propio comprador
- **N2** Operacion `Operacion_presentacion_de_chc_al_cobro__cirmo3_8_4_1_2_17391d` — Presentación de CHC al cobro · {"tipo": "Presentación de cheque cancelatorio al cobro", "descripcion": "Presentación de un cheque cancelatorio (CHC) al cobro por el beneficiario final que resulte de acuerdo con los datos consignados al dorso del documento o por el propio comprador."} · tramo: CHC sea presentado al cobro
- **N3** Sujeto `Sujeto_entidad_financiera` — Entidades financieras · {"nivel": "clase", "alias": ["Entidades financieras emisoras de tarjetas de crédito y/o compra", "Entidad financiera emisora de tarjetas de crédito y/o compra"]} · tramo: 
- **N4** TextoOrdenado `TextoOrdenado_cirmo3_pdf` — Billetes y monedas en circulación · {"archivo": "cirmo3.pdf", "materia": "Circulación monetaria", "version": "Comunicación A 8439 (vigencia 01/06/2026)"} · tramo: 
- **A1** (extraccion) N1 —aplica_a→ N3 · {}
- **E1** (estructural) N1 —establecida_en→ N4 · {}
- **A2** (extraccion) N1 —regula→ N2 · {}
- **E2** (estructural) N2 —establecida_en→ N4 · {}

## 23. `lingeef::3.1.2.2` — NG:resto · aceptadas:items

Texto que vio E3 (e0, bloque de lista True; págs. 45):

```
[encabezado | punto S3]
Sección 3. Gestión del riesgo de liquidez.
[encabezado | punto 3.1]
3.1. Conceptos.
[encabezado | punto 3.1.2]
3.1.2. Gestión del riesgo de liquidez.
[intro | punto 3.1.2]
Se entiende por gestión del riesgo de liquidez al proceso de identificación, evaluación,
seguimiento, control y mitigación de ese riesgo que involucra, entre otros, los siguientes
procesos:
[texto propio | punto 3.1.2.2]
3.1.2.2. el estudio periódico de la estructura de depósitos;
```

Versión: final (grafo sin cola). Nodos 4, aristas 4.
- **N1** Obligacion `Obligacion_las_entidades_financieras_deben_realizar_el_estudio_periodico_de_la_estructura_d_dd37f9` — Realizar estudio periódico de estructura de depósitos · {"tipo": "otra", "descripcion": "Las entidades financieras deben realizar el estudio periódico de la estructura de depósitos como parte del proceso de gestión del riesgo de liquidez"} · tramo: el estudio periódico de la estructura de depósitos
- **N2** Operacion `Operacion_estudio_periodico_de_la_estructura_de_depositos__lingeef_3_1_2_2_bfe170` — Estudio periódico de la estructura de depósitos · {"tipo": "análisis", "descripcion": "Estudio periódico de la estructura de depósitos como proceso de gestión del riesgo de liquidez"} · tramo: el estudio periódico de la estructura de depósitos
- **N3** Sujeto `Sujeto_entidad_financiera` — Entidades financieras · {"nivel": "clase", "alias": ["Entidades financieras emisoras de tarjetas de crédito y/o compra", "Entidad financiera emisora de tarjetas de crédito y/o compra"]} · tramo: 
- **N4** TextoOrdenado `TextoOrdenado_lingeef_pdf` — Lineamientos para la gestión de riesgos · {"archivo": "lingeef.pdf", "materia": "Lineamientos para la gestión de riesgos en las entidades financieras", "version": "Comunicación A 8463 (vigencia 01/08/2026)"} · tramo: 
- **A1** (extraccion) N1 —aplica_a→ N3 · {}
- **E1** (estructural) N1 —establecida_en→ N4 · {}
- **A2** (extraccion) N1 —regula→ N2 · {}
- **E2** (estructural) N2 —establecida_en→ N4 · {}

## 24. `lingeef::9.3.2` — NG:resto · aceptadas:items

Texto que vio E3 (e0, bloque de lista True; págs. 148):

```
[encabezado | punto S9]
Sección 9. Gestión del riesgo reputacional.
[encabezado | punto 9.3]
9.3. Transparencia.
[intro | punto 9.3]
Las entidades financieras deben dar a conocer al público -de manera regular- a través de sus
páginas de Internet o reportes:
[texto propio | punto 9.3.2]
9.3.2. Una descripción del proceso implementado para gestionar el riesgo reputacional, su es-
tructura, los roles y responsabilidades de las unidades relacionadas con el tema;
```

Versión: final (grafo sin cola). Nodos 3, aristas 2.
- **N1** Obligacion `Obligacion_las_entidades_financieras_deben_dar_a_conocer_al_publico_de_manera_regular_a_tra_6baab6` — Descripción del proceso de gestión del riesgo reputacional · {"descripcion": "Las entidades financieras deben dar a conocer al público de manera regular a través de sus páginas de Internet o reportes una descripción del proceso implementado para gestionar el riesgo reputacional, su estructura, los roles y responsabilidades de las unidades relacionadas con el tema", "tipo": "presentacion_informativa", "frecuencia": "de manera regular"} · tramo: Una descripción del proceso implementado para gestionar el riesgo reputacional, su estructura, los roles y responsabilidades de las unidades relacionadas con el tema
- **N2** Sujeto `Sujeto_entidad_financiera` — Entidades financieras · {"nivel": "clase", "alias": ["Entidades financieras emisoras de tarjetas de crédito y/o compra", "Entidad financiera emisora de tarjetas de crédito y/o compra"]} · tramo: 
- **N3** TextoOrdenado `TextoOrdenado_lingeef_pdf` — Lineamientos para la gestión de riesgos · {"archivo": "lingeef.pdf", "materia": "Lineamientos para la gestión de riesgos en las entidades financieras", "version": "Comunicación A 8463 (vigencia 01/08/2026)"} · tramo: 
- **A1** (extraccion) N1 —aplica_a→ N2 · {}
- **E1** (estructural) N1 —establecida_en→ N3 · {}

## 25. `lingeef::4.3.5.2` — NG:resto · aceptadas:items

Texto que vio E3 (e0, bloque de lista True; págs. 79):

```
[encabezado | punto S4]
Sección 4. Gestión del riesgo de mercado.
[encabezado | punto 4.3]
4.3. Proceso de gestión del riesgo de mercado.
[encabezado | punto 4.3.5]
4.3.5. Planificación para la contingencia.
[intro | punto 4.3.5]
Las entidades financieras deben tener un plan de contingencias que establezca clara-
mente la estrategia para afrontar situaciones de emergencia.
El plan de contingencia debe:
[texto propio | punto 4.3.5.2]
4.3.5.2. Contemplar diferentes horizontes de tiempo, incluso intradiarios;
```

Versión: final (grafo sin cola). Nodos 3, aristas 2.
- **N1** Obligacion `Obligacion_el_plan_de_contingencia_debe_contemplar_diferentes_horizontes_de_tiempo_incluso__148b28` — Contemplar horizontes de tiempo intradiarios · {"descripcion": "El plan de contingencia debe contemplar diferentes horizontes de tiempo, incluso intradiarios", "tipo": "otra"} · tramo: Contemplar diferentes horizontes de tiempo, incluso intradiarios
- **N2** Sujeto `Sujeto_entidad_financiera` — Entidades financieras · {"nivel": "clase", "alias": ["Entidades financieras emisoras de tarjetas de crédito y/o compra", "Entidad financiera emisora de tarjetas de crédito y/o compra"]} · tramo: 
- **N3** TextoOrdenado `TextoOrdenado_lingeef_pdf` — Lineamientos para la gestión de riesgos · {"archivo": "lingeef.pdf", "materia": "Lineamientos para la gestión de riesgos en las entidades financieras", "version": "Comunicación A 8463 (vigencia 01/08/2026)"} · tramo: 
- **A1** (extraccion) N1 —aplica_a→ N2 · {}
- **E1** (estructural) N1 —establecida_en→ N3 · {}

## 26. `lingeef::5.3.2.4` — NG:resto · aceptadas:items

Texto que vio E3 (e0, bloque de lista True; págs. 89, 90):

```
[encabezado | punto S5]
Sección 5. Gestión del riesgo de tasa de interés en la cartera de inversión.
[encabezado | punto 5.3]
5.3. Proceso de gestión del riesgo de tasa de interés en la cartera de inversión.
[encabezado | punto 5.3.2]
5.3.2. Apetito por el riesgo. Política en materia de límites.
[intro | punto 5.3.2]
Las entidades financieras deben definir límites a los fines de mantener exposiciones
acordes con su apetito por el RTICI, expresados tanto en relación con su valor econó-
mico como con relación a sus resultados.
Tales límites deben ser establecidos por escrito en forma clara –detallando el nivel
agregado de riesgo y los tipos de exposiciones al RTICI que se acepta o evita a fin de
lograr los objetivos de negocio–, aprobados por el Directorio e implementados median-
te un marco comprehensivo para el apetito por este riesgo –es decir, políticas y proce-
dimientos que limiten y controlen el RTICI–.
El referido marco debe describir las facultades delegadas, las líneas de responsabili-
dad y de rendición de cuentas sobre las decisiones en materia de gestión del RTICI, y
definir claramente los instrumentos, las estrategias de cobertura y las oportunidades
para la toma de riesgos que están autorizados. Todas las políticas sobre el RTICI de-
ben revisarse periódicamente (al menos anualmente) y cada vez que sea necesario.
Los límites pueden estar asociados a determinados escenarios de variaciones de las
tasas de interés y/o de las estructuras temporales de tasa de interés, como un aumen-
to o descenso de una determinada proporción o un cambio de forma. Las variaciones
de las tasas de interés sobre las que se basan esos límites deben reproducir situacio-
nes significativas de perturbación y estrés, teniendo en cuenta la volatilidad histórica de
las tasas de interés y el tiempo necesario para que la gerencia mitigue dichas exposi-
ciones al riesgo.
Además, los límites deben:
[texto propio | punto 5.3.2.4]
5.3.2.4. Reflejar, en su grado de detalle, las características de las tenencias de la enti-
dad, incluyendo las diversas fuentes de exposición al RTICI.
Las entidades con exposiciones al riesgo de brecha, al riesgo de base o con
posiciones con opciones –explícitas o implícitas– que sean significativas, de-
ben establecer límites apropiados a tales subtipos de riesgos.
```

Versión: final (grafo sin cola). Nodos 4, aristas 4.
- **N1** Obligacion `Obligacion_las_entidades_con_exposiciones_al_riesgo_de_brecha_al_riesgo_de_base_o_con_posic_696dd0` — Establecer límites para subtipos de riesgos significativos · {"descripcion": "Las entidades con exposiciones al riesgo de brecha, al riesgo de base o con posiciones con opciones (explícitas o implícitas) que sean significativas deben establecer límites apropiados a tales subtipos de riesgos.", "tipo": "otra"} · tramo: Las entidades con exposiciones al riesgo de brecha, al riesgo de base o con posiciones con opciones –explícitas o implícitas– que sean significativas, deben establecer límites apropiados a tales subtipos de riesgos
- **N2** Obligacion `Obligacion_las_entidades_financieras_deben_reflejar_en_su_grado_de_detalle_las_caracteristi_8eace0` — Reflejar características de tenencias · {"descripcion": "Las entidades financieras deben reflejar, en su grado de detalle, las características de las tenencias de la entidad, incluyendo las diversas fuentes de exposición al RTICI.", "tipo": "otra"} · tramo: Reflejar, en su grado de detalle, las características de las tenencias de la entidad, incluyendo las diversas fuentes de exposición al RTICI
- **N3** Sujeto `Sujeto_entidad_financiera` — Entidades financieras · {"nivel": "clase", "alias": ["Entidades financieras emisoras de tarjetas de crédito y/o compra", "Entidad financiera emisora de tarjetas de crédito y/o compra"]} · tramo: 
- **N4** TextoOrdenado `TextoOrdenado_lingeef_pdf` — Lineamientos para la gestión de riesgos · {"archivo": "lingeef.pdf", "materia": "Lineamientos para la gestión de riesgos en las entidades financieras", "version": "Comunicación A 8463 (vigencia 01/08/2026)"} · tramo: 
- **A1** (extraccion) N1 —aplica_a→ N3 · {}
- **E1** (estructural) N1 —establecida_en→ N4 · {}
- **A2** (extraccion) N2 —aplica_a→ N3 · {}
- **E2** (estructural) N2 —establecida_en→ N4 · {}

## 27. `lingeef::2.3.6.5` — NG:resto · aceptadas:items

Texto que vio E3 (e0, bloque de lista True; págs. 35):

```
[encabezado | punto S2]
Sección 2. Gestión del riesgo de crédito.
[encabezado | punto 2.3]
2.3. Proceso de gestión del riesgo de crédito.
[encabezado | punto 2.3.6]
2.3.6. Controles.
[intro | punto 2.3.6]
Las entidades financieras deben establecer un sistema continuo, independiente y eficien-
te de revisión de los procesos de riesgo de crédito, que incluya auditorías internas perió-
dicas, cuyos resultados deben ser comunicados directamente al Directorio o a la Alta Ge-
rencia -en la medida que no esté involucrada en el proceso de otorgamiento-.
Se debe evaluar y reportar:
[texto propio | punto 2.3.6.5]
2.3.6.5. La condición de la cartera crediticia.
```

Versión: final (grafo sin cola). Nodos 3, aristas 2.
- **N1** Obligacion `Obligacion_las_entidades_financieras_deben_evaluar_y_reportar_sobre_la_condicion_de_la_cart_2b314b` — Evaluación y reporte de la cartera crediticia · {"descripcion": "Las entidades financieras deben evaluar y reportar sobre la condición de la cartera crediticia", "tipo": "reporte_al_supervisor"} · tramo: Se debe evaluar y reportar: La condición de la cartera crediticia
- **N2** Sujeto `Sujeto_entidad_financiera` — Entidades financieras · {"nivel": "clase", "alias": ["Entidades financieras emisoras de tarjetas de crédito y/o compra", "Entidad financiera emisora de tarjetas de crédito y/o compra"]} · tramo: 
- **N3** TextoOrdenado `TextoOrdenado_lingeef_pdf` — Lineamientos para la gestión de riesgos · {"archivo": "lingeef.pdf", "materia": "Lineamientos para la gestión de riesgos en las entidades financieras", "version": "Comunicación A 8463 (vigencia 01/08/2026)"} · tramo: 
- **A1** (extraccion) N1 —aplica_a→ N2 · {}
- **E1** (estructural) N1 —establecida_en→ N3 · {}

## 28. `lingeef::10.3.1` — NG:resto · aceptadas:items

Texto que vio E3 (e0, bloque de lista True; págs. 149):

```
[encabezado | punto S10]
Sección 10. Gestión del riesgo estratégico.
[encabezado | punto 10.3]
10.3. Responsabilidades.
[intro | punto 10.3]
El Directorio y la Alta Gerencia deben:
[texto propio | punto 10.3.1]
10.3.1. Considerar la planificación del capital como un elemento fundamental para el logro de
los objetivos estratégicos de la entidad financiera.
```

Versión: final (grafo sin cola). Nodos 4, aristas 3.
- **N1** Obligacion `Obligacion_el_directorio_y_la_alta_gerencia_deben_considerar_la_planificacion_del_capital_c_c2bac7` — Considerar planificación del capital — elemento fundamental · {"descripcion": "El Directorio y la Alta Gerencia deben considerar la planificación del capital como un elemento fundamental para el logro de los objetivos estratégicos de la entidad financiera.", "tipo": "otra"} · tramo: Considerar la planificación del capital como un elemento fundamental para el logro de los objetivos estratégicos de la entidad financiera
- **N2** Sujeto `Sujeto_alta_gerencia` — Alta Gerencia · {"nivel": "clase"} · tramo: 
- **N3** Sujeto `Sujeto_directorio` — Directorio · {"nivel": "clase", "alias": ["Consejo de Administración"]} · tramo: 
- **N4** TextoOrdenado `TextoOrdenado_lingeef_pdf` — Lineamientos para la gestión de riesgos · {"archivo": "lingeef.pdf", "materia": "Lineamientos para la gestión de riesgos en las entidades financieras", "version": "Comunicación A 8463 (vigencia 01/08/2026)"} · tramo: 
- **A1** (extraccion) N1 —aplica_a→ N2 · {}
- **A2** (extraccion) N1 —aplica_a→ N3 · {}
- **E1** (estructural) N1 —establecida_en→ N4 · {}

## 29. `lingeef::1.2.6` — NG:resto · aceptadas:items

Texto que vio E3 (e0, bloque de lista True; págs. 6):

```
[encabezado | punto S1]
Sección 1. Proceso de gestión de riesgos.
[encabezado | punto 1.2]
1.2. Consideraciones generales.
[intro | punto 1.2]
Los presentes lineamientos constituyen buenas prácticas en materia de gestión de riesgos y,
por ende, no son sustitutos de los requerimientos específicos contenidos en las normas dicta-
das por el Banco Central de la República Argentina, debiendo implementarse conforme a las
atribuciones conferidas al Directorio por la Asamblea de Accionistas u órgano de gobierno de
la sociedad que cumpla funciones semejantes y en el contexto de las pertinentes disposicio-
nes legales vigentes.
La información sobre el proceso integral para la gestión de riesgos que implemente la entidad
deberá estar a disposición de la Superintendencia de Entidades Financieras y Cambiarias
(SEFyC).
La gestión de los riesgos que surgen desde la negociación de operaciones de cambio que in-
volucren dos flujos de pago hasta su liquidación final, deberá realizarse de conformidad con lo
previsto en las normas sobre “Gestión de riesgos asociados a la liquidación de operaciones de
cambio”.
A los fines de estas normas se entiende como:
[texto propio | punto 1.2.6]
1.2.6. Cartera de inversión: la constituida por las posiciones en instrumentos que no encuadren
en el punto 1.2.5.
```

Versión: final (grafo sin cola). Nodos 2, aristas 2.
- **N1** Definicion `Definicion_cartera_de_inversion__la_constituida_por_las_posiciones_en_instrumentos_que_no_e_941577` — Cartera de inversión · {"termino": "Cartera de inversión", "descripcion": "la constituida por las posiciones en instrumentos que no encuadren en el punto 1.2.5"} · tramo: Cartera de inversión: la constituida por las posiciones en instrumentos que no encuadren en el punto 1.2.5
- **N2** TextoOrdenado `TextoOrdenado_lingeef_pdf` — Lineamientos para la gestión de riesgos · {"archivo": "lingeef.pdf", "materia": "Lineamientos para la gestión de riesgos en las entidades financieras", "version": "Comunicación A 8463 (vigencia 01/08/2026)"} · tramo: 
- **E1** (estructural) N1 —establecida_en→ N2 · {}
- **R1** (remision_derivada) N1 —remite_a→ Definicion_cartera_de_negociacion__la_constituida_por_las_posiciones_en_instrumentos_que_ve_5aa1f0 · {"alcance": "interna", "destino": "lingeef::1.2.5", "evidencia": "constituida por las posiciones en instrumentos que no encuadren\nen el punto 1.2.5."}

## 30. `cajasc::5.1.3` — NG:resto · aceptadas:items

Texto que vio E3 (e0, bloque de lista True; págs. 32):

```
[encabezado | punto S5]
Sección 5. Garantías.
[encabezado | punto 5.1]
5.1. Preferidas “A”.
[intro | punto 5.1]
Están constituidas por la cesión o caución de derechos respecto de títulos o documentos de
cualquier naturaleza que, fehacientemente instrumentadas, aseguren que la caja de crédito
cooperativa podrá disponer de los fondos en concepto de cancelación de la obligación contraí-
da por el prestatario, sin necesidad de requerir previamente el pago al deudor dado que la
efectivización depende de terceros solventes o de la existencia de mercados en los cuales
puedan liquidarse directamente los mencionados títulos o documentos, ya sea que el venci-
miento de ellos coincida o sea posterior al vencimiento del préstamo o de los pagos periódicos
comprometidos o que el producido sea aplicado a la cancelación de la deuda o transferido di-
rectamente a la entidad a ese fin, siempre que las operaciones de crédito no superen, medido
en forma residual, el término de 6 meses, salvo en los casos en que se establezca un plazo
distinto.
Se incluyen, con carácter de enumeración taxativa, las siguientes:
[texto propio | punto 5.1.3]
5.1.3. Garantías o cauciones de títulos valores públicos nacionales, teniendo en cuenta en
forma permanente su valor de mercado que debe responder a una cotización normal y
habitual en el país, de amplia difusión y fácil acceso al conocimiento público.
En el caso de ejecutarse la garantía, deberán ser liquidados los títulos valores públicos
nacionales cuyo plazo residual sea superior a 180 días.
```

Versión: final (grafo sin cola). Nodos 5, aristas 6.
- **N1** Condicion `Condicion_operaciones_de_credito_no_superen_6_meses__las_operaciones_de_credito_no_superen_b275d6` — Operaciones de crédito no superen 6 meses · {"descripcion": "Las operaciones de crédito no superen, medido en forma residual, el término de 6 meses", "umbrales": [{"tramo": "no superen, medido en forma residual, el término de 6 meses", "valor": "6", "unidad": "meses", "comparacion": "maximo_inclusivo", "regla_comparacion": "negacion:raiz_super", "origen": "e1", "tramo_verificado": "exacta"}]} · tramo: siempre que las operaciones de crédito no superen, medido en forma residual, el término de 6 meses
- **N2** Obligacion `Obligacion_cuando_se_ejecute_la_garantia_deberan_ser_liquidados_los_titulos_valores_publico_f50839` — Liquidación de títulos valores públicos nacionales al ejecutarse la garantía · {"tipo": "otra", "descripcion": "Cuando se ejecute la garantía, deberán ser liquidados los títulos valores públicos nacionales cuyo plazo residual sea superior a 180 días", "umbrales": [{"tramo": "plazo residual sea superior a 180 días", "valor": "180", "unidad": "dias", "comparacion": "minimo_estricto", "regla_comparacion": "simple:raiz_super", "origen": "e1", "tramo_verificado": "exacta"}]} · tramo: En el caso de ejecutarse la garantía, deberán ser liquidados los títulos valores públicos nacionales cuyo plazo residual sea superior a 180 días
- **N3** Operacion `Operacion_garantia_o_caucion_de_titulos_valores_publicos_nacionales__cajasc_5_1_3_1dccd4` — Garantía o caución de títulos valores públicos nacionales · {"tipo": "Garantía o caución", "descripcion": "Cesión o caución de títulos valores públicos nacionales cuyo valor de mercado debe responder a una cotización normal y habitual en el país, de amplia difusión y fácil acceso al conocimiento público, constituida para asegurar que la caja de crédito cooperativa podrá disponer de los fondos en concepto de cancelación de la obligación contraída por el pre · tramo: Garantías o cauciones de títulos valores públicos nacionales, teniendo en cuenta en forma permanente su valor de mercado que debe responder a una cotización normal y habitual en el país, de amplia difusión y fácil acceso al conocimiento público
- **N4** Sujeto `Sujeto_caja_de_credito_cooperativa` — Cajas de crédito cooperativas · {"nivel": "clase"} · tramo: 
- **N5** TextoOrdenado `TextoOrdenado_cajasc_pdf` — Cajas de crédito cooperativas · {"archivo": "cajasc.pdf", "materia": "Cajas de Crédito Cooperativas (Ley 26.173)", "version": "Comunicación A 7083 (vigencia 07/08/2020)"} · tramo: 
- **A1** (extraccion) N1 —condicion_de→ N3 · {}
- **E1** (estructural) N1 —establecida_en→ N5 · {}
- **A2** (extraccion) N2 —aplica_a→ N4 · {}
- **E2** (estructural) N2 —establecida_en→ N5 · {}
- **A3** (extraccion) N3 —aplica_a→ N4 · {}
- **E3** (estructural) N3 —establecida_en→ N5 · {}

