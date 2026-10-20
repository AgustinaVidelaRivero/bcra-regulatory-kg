# Material de T4 — observacion:12 (30 fichas; B6.1, tanda final, T3, punto 7.5)

Sorteo: `observacion_12.json` (64658703…, 2026-10-20T14:08:58-03:00); material armado a las 2026-10-20T14:09:15-03:00. Sin el estado de E3 ni las marcas de E3.

## 1. `Definicion_tercera_semana_estadistica__del_16_al_23_inclusive__ri_ot_sbloque1_9b288d | establecida_en | TextoOrdenado_ri_ot_pdf` — RI:sin_raiz · observacion:12

Texto que vio E3 de `ri_ot::Sbloque1` (e0, bloque de lista True; págs. 1):

```
[texto propio | punto Sbloque1]
Instrucciones Generales
Los montos se registrarán en unidades sin decimales.
A los fines del redondeo de las magnitudes se incrementarán los valores en una unidad cuando el
primer dígito de las fracciones sea igual o mayor que 5, desechando estas últimas si resultan inferio-
res.
El Régimen Informativo se presentará por semana estadística, operando su vencimiento a las 15
horas del día hábil siguiente al último día correspondiente a la semana estadística bajo informe, a
través del Sitio de Internet del Banco Central de la República Argentina.
Las semanas estadísticas son las siguientes:
Primera semana estadística: del 1 al 7 inclusive.
Segunda semana estadística: del 8 al 15 inclusive.
Tercera semana estadística: del 16 al 23 inclusive.
Cuarta semana estadística: del 24 al último día del mes inclusive.
```

Versión: final (grafo sin cola).
- origen: {"id": "Definicion_tercera_semana_estadistica__del_16_al_23_inclusive__ri_ot_sbloque1_9b288d", "type": "Definicion", "label": "Tercera semana estadística", "properties": {"termino": "Tercera semana estadística", "descripcion": "Del 16 al 23 inclusive."}, "procedencia": {"chunk_id": "ri_ot::Sbloque1", "punto": "Sbloque1", "rol_documental": "punto_propio", "tramo": "Tercera semana estadística: del 16 al 23 inclusive.", "tramo_verificado": "exacta", "termino_verificado": "exacta", "paginas": [1]}}
- relación: `establecida_en`
- destino: {"id": "TextoOrdenado_ri_ot_pdf", "type": "TextoOrdenado", "label": "Régimen Informativo — Normas de Procedimiento", "properties": {"archivo": "ri_ot.pdf", "materia": "RI Cont. Mensual - Operaciones a Término", "version": "Comunicación A 8271 (vigencia 05/07/2025)"}, "procedencia": {"chunk_id": "ri_ot::S0", "punto": "S0", "rol_documental": "punto_propio", "paginas": [1]}}
- arista: {"properties": {}, "procedencia": {"chunk_id": "ri_ot::Sbloque1", "punto": "Sbloque1", "rol_documental": "punto_propio", "paginas": [1]}}

## 2. `Sujeto_entidad_financiera | ejecuta | Operacion_originacion_de_transferencia_electronica_de_fondos__snp_tr_nc_1_3_5_d46999` — RI:sin_raiz · observacion:12

Texto que vio E3 de `snp_tr_nc::1.3.5` (e0, bloque de lista True; págs. 5):

```
[encabezado | punto S1]
Sección 1. Transferencias electrónicas de fondos. Conceptos básicos
[encabezado | punto 1.3]
1.3. Funciones de los esquemas de transferencias electrónicas de fondos
[texto propio | punto 1.3.5]
1.3.5. Originación, sólo para entidades financieras. Remitir una transferencia electrónica de
fondos a una entidad receptora a través del operador y recibir los mensajes de parte de
la entidad receptora, debitando los fondos cuando corresponda.
```

Versión: final (grafo sin cola).
- origen: {"id": "Sujeto_entidad_financiera", "type": "Sujeto", "label": "Entidades financieras", "properties": {"nivel": "clase", "alias": ["Entidades financieras emisoras de tarjetas de crédito y/o compra", "Entidad financiera emisora de tarjetas de crédito y/o compra"]}, "procedencia": {"chunk_id": "ri_esd::Sbloque1::chapeau_seccion", "punto": "Sbloque1", "rol_documental": "bloque_chapeau_seccion", "paginas": [1, 2]}}
- relación: `ejecuta`
- destino: {"id": "Operacion_originacion_de_transferencia_electronica_de_fondos__snp_tr_nc_1_3_5_d46999", "type": "Operacion", "label": "Originación de transferencia electrónica de fondos", "properties": {"tipo": "Originación de transferencia electrónica de fondos", "descripcion": "Remitir una transferencia electrónica de fondos a una entidad receptora a través del operador y recibir los mensajes de parte de la entidad receptora, debitando los fondos cuando corresponda. Operación restringida a entidades financieras."}, "procedencia": {"chunk_id": "snp_tr_nc::1.3.5", "punto": "1.3.5", "rol_documental": "punto_propio", "tramo": "Remitir una transferencia electrónica de fondos a una entidad receptora a través del operador y recibir los mensajes de parte de la entidad receptora, debitando los fondos cuando corresponda", "tramo_verificado": "exacta", "paginas": [5]}}
- arista: {"properties": {}, "sujeto_mencion": "entidades financieras", "mencion_verificada": "exacta", "metodo_resolucion": "R1_label_exacto", "sujeto_id_modelo": "Sujeto_entidad_financiera", "procedencia": {"chunk_id": "snp_tr_nc::1.3.5", "punto": "1.3.5", "rol_documental": "punto_propio", "paginas": [5]}}

## 3. `Obligacion_las_entidades_financieras_cedentes_y_cesionarias_deben_acordar_la_registracion_c_385cf7 | aplica_a | Sujeto_entidad_financiera` — RI:sin_raiz · observacion:12

Texto que vio E3 de `ri_dsf::2.1` (e0, bloque de lista True; págs. 2, 3):

```
[encabezado | punto S2]
2.Deudores comprendidos.
[chapeau_seccion | punto S2]
Se informará la totalidad de los deudores de las entidades financieras y otros entes mencionados
en el último párrafo del punto precedente, con excepción del B.C.R.A. y aquellos deudores cuyo
saldo de deuda sea inferior a $25 mil.
Para definir al deudor se tendrán en cuenta los conceptos vertidos en el Texto ordenado de las
Normas sobre “Gestión Crediticia”.
En los casos de grupos o conjuntos económicos no se consolidará la información.
Las entidades deben seguir informando a sus deudores en la medida que continúen las gestio-
nes de cobro de sus acreencias.
A fin de evitar posibles duplicaciones, las entidades financieras cedentes y cesionarias deberán
acordar la registración contable consistentemente tal como se encuentra establecido en el punto
2.1.4. de las normas sobre “Cesión de cartera de créditos”. El mismo criterio deberá aplicarse a
fin de informar la cartera que constituye el saldo inicial al 31/12/2017 de las financiaciones que
hayan sido objeto de cesiones concertadas previamente entre las entidades financieras. Asimis-
mo, por el mismo motivo, resulta necesaria la unificación de los criterios que se aplican para el
presente régimen a partir de la vigencia de las NIIF para los casos relativos a cesiones de cartera
realizadas entre entidades financieras y otro tipo de entidades.
[chapeau_seccion | punto S2]
3.Deudores del Sistema Financiero.
[chapeau_seccion | punto S2]
A. DATOS IDENTIFICATORIOS DEL DEUDOR
Se proveerán, respecto de cada uno de los deudores comprendidos, según corresponda, las si-
guientes informaciones.
[chapeau_seccion | punto S2]
1. Denominación.
[chapeau_seccion | punto S2]
1.1. Personas humanas y sociedades de hecho.
[chapeau_seccion | punto S2]
Apellidos y nombres, en forma completa.
[chapeau_seccion | punto S2]
1.2. Restantes personas jurídicas.
[chapeau_seccion | punto S2]
Razón social o denominación, en forma completa.
Teniendo en cuenta la identificación del deudor (tipo y número) este Banco Central re-
emplazará, bajo la exclusiva responsabilidad de la entidad, la “Denominación” origi-
nalmente informada, por la que figure en el “Padrón de la AFIP”.
Cuando el deudor no esté incluido en dicho padrón, deberá informarse según la identi-
ficación y denominación provista por la Administración Federal de Ingresos Públicos.
[chapeau_seccion | punto S2]
2. Identificación.
[chapeau_seccion | punto S2]
Se deberán tener en cuenta las disposiciones contenidas en la Sección 4. Verificación vin-
culada con los documentos de identidad del Texto Ordenado “Documentos de Identificación
en Vigencia”:
[texto propio | punto 2.1]
2.1. Tipo.
Administración Federal de Ingresos Públicos
- Clave Única de Identificación Tributaria (C.U.I.T.).
- Código Único de Identificación Laboral (C.U.I.L.).
- Clave de Identificación (C.D.I.).
Para las situaciones no previstas, se tendrá en cuenta lo establecido en las Nor-
mas de Presentación de Informaciones al Banco Central – Sección 3.
3.Deudores del Sistema Financiero.
```

Versión: final (grafo sin cola).
- origen: {"id": "Obligacion_las_entidades_financieras_cedentes_y_cesionarias_deben_acordar_la_registracion_c_385cf7", "type": "Obligacion", "label": "Acordar registración contable consistente en cesiones", "properties": {"tipo": "otra", "descripcion": "Las entidades financieras cedentes y cesionarias deben acordar la registración contable de manera consistente, conforme a lo establecido en el punto 2.1.4 de las normas sobre Cesión de cartera de créditos."}, "procedencia": {"chunk_id": "ri_dsf::2.1", "punto": "2.1", "rol_documental": "punto_propio", "tramo": "las entidades financieras cedentes y cesionarias deberán acordar la registración contable consistentemente tal como se encuentra establecido en el punto 2.1.4. de las normas sobre \"Cesión de cartera de créditos\".", "tramo_verificado": "exacta", "paginas": [2, 3]}}
- relación: `aplica_a`
- destino: {"id": "Sujeto_entidad_financiera", "type": "Sujeto", "label": "Entidades financieras", "properties": {"nivel": "clase", "alias": ["Entidades financieras emisoras de tarjetas de crédito y/o compra", "Entidad financiera emisora de tarjetas de crédito y/o compra"]}, "procedencia": {"chunk_id": "ri_esd::Sbloque1::chapeau_seccion", "punto": "Sbloque1", "rol_documental": "bloque_chapeau_seccion", "paginas": [1, 2]}}
- arista: {"properties": {}, "sujeto_mencion": "las entidades financieras cedentes y cesionarias", "mencion_verificada": "exacta", "metodo_resolucion": "R4_sugerencia_modelo", "sujeto_id_modelo": "Sujeto_entidad_financiera", "procedencia": {"chunk_id": "ri_dsf::2.1", "punto": "2.1", "rol_documental": "punto_propio", "paginas": [2, 3]}}

## 4. `Obligacion_en_el_campo_fecha_de_ultima_liquidacion_debe_consignarse_la_fecha_de_la_ultima_l_6b1d40 | aplica_a | Sujeto_rol_entidad_comprendida_reginf` — RI:sin_raiz · observacion:12

Texto que vio E3 de `ri_secoexpo::SB::rep3` (e0, bloque de lista True; págs. 6):

```
[encabezado | punto Sbloque1]
APARTADO A – DATOS A DISPOSICIÓN DE LAS ENTIDADES
[texto propio | punto SB]
APARTADO B – B.1 CERTIFICACION DE CUMPLIDO
B.1. CERTIFICACIÓN DE CUMPLIDO
Datos solicitados:
1. C.U.I.T. del exportador.
2. N° de destinación de exportación: Número de embarque o destinación de exportación que se
certifica como cumplida.
3. Fecha de cumplido.
4. Número de cumplido: corresponde al número interno de cumplido asignado por la entidad.
5. Liquidación efectiva de divisas con posterioridad a la fecha de embarque.
6. Fecha de vencimiento para la liquidación de divisas aplicable a la destinación.
7. Fecha de última liquidación.
8. Código de divisa del valor FOB: de acuerdo con codificación SWIFT.
9. Monto Cumplido.
Para el dato “Fecha de cumplido” se debe consignar la mayor fecha asignada a una imputación a la
destinación certificada como cumplido, independientemente de que la misma corresponda a una
liquidación, una aplicación o la utilización de otros mecanismos admitidos.
En el dato “Liquidación efectiva de divisas con posterioridad a la fecha de embarque” se debe
consignar “S” si se imputó a la destinación certificada como cumplido al menos una liquidación
efectiva de divisas ocurrida con posterioridad a la fecha de embarque. En caso contrario, consignar
“N”.
En el dato “Fecha de última liquidación”, se debe consignar la fecha en que se produjo la última
liquidación de cobros de exportaciones en el mercado de cambios. En caso de no existir ninguna, la
fecha consignada deberá coincidir con la fecha de embarque.
En el dato “Monto Cumplido” se debe consignar el monto que ha tenido en cuenta la entidad para
certificar el cumplido de la destinación. Es decir, se informará el valor FOB informado por la Aduana
o el valor facturado por la exportación según la condición de venta pactada, el que resulte mayor.
```

Versión: final (grafo sin cola).
- origen: {"id": "Obligacion_en_el_campo_fecha_de_ultima_liquidacion_debe_consignarse_la_fecha_de_la_ultima_l_6b1d40", "type": "Obligacion", "label": "Consignar fecha de última liquidación de cobros", "properties": {"tipo": "presentacion_informativa", "descripcion": "En el campo Fecha de última liquidación debe consignarse la fecha de la última liquidación de cobros de exportaciones en el mercado de cambios, o la fecha de embarque si no existe liquidación alguna."}, "procedencia": {"chunk_id": "ri_secoexpo::SB::rep3", "punto": "SB", "rol_documental": "punto_propio", "tramo": "En el dato \"Fecha de última liquidación\", se debe consignar la fecha en que se produjo la última liquidación de cobros de exportaciones en el mercado de cambios. En caso de no existir ninguna, la fecha consignada deberá coincidir con la fecha de embarque.", "tramo_verificado": "exacta", "paginas": [6]}}
- relación: `aplica_a`
- destino: {"id": "Sujeto_rol_entidad_comprendida_reginf", "type": "Sujeto", "label": "Entidades comprendidas (Régimen Informativo)", "properties": {"nivel": "rol"}, "procedencia": {"chunk_id": "ribspc::S4", "punto": "S4", "rol_documental": "punto_propio", "paginas": [1]}}
- arista: {"properties": {}, "sujeto_mencion": "la entidad", "mencion_verificada": "exacta", "metodo_resolucion": "R4_sugerencia_modelo", "sujeto_id_modelo": "Sujeto_rol_entidad_comprendida_reginf", "procedencia": {"chunk_id": "ri_secoexpo::SB::rep3", "punto": "SB", "rol_documental": "punto_propio", "paginas": [6]}}

## 5. `Obligacion_remitir_al_bcra_el_informe_tecnico_de_autoevaluacion_de_riesgos_de_la_ft_junto_c_2f410a | aplica_a | Sujeto_rol_sujeto_obligado_proteccion` — RI:sin_raiz · observacion:12

Texto que vio E3 de `ri_laft::1.2` (e0, bloque de lista True; págs. 1):

```
[encabezado | punto S1]
1. Instrucciones generales
[texto propio | punto 1.2]
1.2. Informe técnico de autoevaluación de riesgos de LA/FT y su metodología.
Deberán remitir al Banco Central de la República Argentina (BCRA) el citado informe jun-
to con la metodología de identificación, evaluación y comprensión de riesgos acorde con
la naturaleza y dimensión de su actividad comercial, según lo establecido por la UIF.
```

Versión: final (grafo sin cola).
- origen: {"id": "Obligacion_remitir_al_bcra_el_informe_tecnico_de_autoevaluacion_de_riesgos_de_la_ft_junto_c_2f410a", "type": "Obligacion", "label": "Remisión informe técnico autoevaluación riesgos LA/FT", "properties": {"tipo": "reporte_al_supervisor", "descripcion": "Remitir al BCRA el informe técnico de autoevaluación de riesgos de LA/FT junto con la metodología de identificación, evaluación y comprensión de riesgos acorde con la naturaleza y dimensión de la actividad comercial, según lo establecido por la UIF."}, "procedencia": {"chunk_id": "ri_laft::1.2", "punto": "1.2", "rol_documental": "punto_propio", "tramo": "Deberán remitir al Banco Central de la República Argentina (BCRA) el citado informe junto con la metodología de identificación, evaluación y comprensión de riesgos acorde con la naturaleza y dimensión de su actividad comercial, según lo establecido por la UIF.", "tramo_verificado": "exacta", "paginas": [1]}}
- relación: `aplica_a`
- destino: {"id": "Sujeto_rol_sujeto_obligado_proteccion", "type": "Sujeto", "label": "Sujetos obligados (Protección de usuarios)", "properties": {"nivel": "rol"}, "procedencia": {"chunk_id": "ri_laft::1.2", "punto": "1.2", "rol_documental": "punto_propio", "paginas": [1]}}
- arista: {"properties": {}, "sujeto_mencion": "Los sujetos obligados", "mencion_verificada": "exacta", "metodo_resolucion": "R4_sugerencia_modelo", "sujeto_id_modelo": "Sujeto_rol_sujeto_obligado_proteccion", "procedencia": {"chunk_id": "ri_laft::1.2", "punto": "1.2", "rol_documental": "punto_propio", "paginas": [1]}}

## 6. `Obligacion_se_debera_registrar_el_tipo_y_numero_de_identificacion_fiscal_de_la_persona_juri_53d252 | establecida_en | TextoOrdenado_ri_ii_31_12_19_pdf` — RI:sin_raiz · observacion:12

Texto que vio E3 de `ri_ii_31_12_19::4.3.2` (e0, bloque de lista True; págs. 11):

```
[encabezado | punto S4]
4. ACCIONISTAS
[texto propio | punto 4.3.2]
4.3.2. Tipo y número de identificación fiscal de la persona jurídica. Se deberá registrar el
Tipo y número con que se haya identificado a la persona jurídica de la que forma
parte el accionista - según lo previsto en el punto 4.2.4.- ya sea como accionista
de la entidad financiera, cambiaria o de otra persona jurídica
```

Versión: final (grafo sin cola).
- origen: {"id": "Obligacion_se_debera_registrar_el_tipo_y_numero_de_identificacion_fiscal_de_la_persona_juri_53d252", "type": "Obligacion", "label": "Registrar tipo y número de identificación fiscal", "properties": {"descripcion": "Se deberá registrar el tipo y número de identificación fiscal de la persona jurídica de la que forma parte el accionista, según lo previsto en el punto 4.2.4., ya sea como accionista de la entidad financiera, cambiaria o de otra persona jurídica", "tipo": "presentacion_informativa"}, "procedencia": {"chunk_id": "ri_ii_31_12_19::4.3.2", "punto": "4.3.2", "rol_documental": "punto_propio", "tramo": "Se deberá registrar el Tipo y número con que se haya identificado a la persona jurídica de la que forma parte el accionista", "tramo_verificado": "exacta", "paginas": [11]}}
- relación: `establecida_en`
- destino: {"id": "TextoOrdenado_ri_ii_31_12_19_pdf", "type": "TextoOrdenado", "label": "Información Institucional de Entidades Financieras y Cambiarias", "properties": {"archivo": "ri_ii_31_12_19.pdf", "materia": "RI Cont. Mensual - Información Institucional de Entidades Financieras y Cambiarias - Vigente a partir del 31.12.19", "version": "Comunicación A 8140 (vigencia 03/12/2024)"}, "procedencia": {"chunk_id": "ri_ii_31_12_19::S0", "punto": "S0", "rol_documental": "punto_propio", "paginas": [1, 2, 3, 4]}}
- arista: {"properties": {}, "procedencia": {"chunk_id": "ri_ii_31_12_19::4.3.2", "punto": "4.3.2", "rol_documental": "punto_propio", "paginas": [11]}}

## 7. `Obligacion_la_entidad_debe_reportar_cualquier_modificacion_que_implique_una_reduccion_del_m_d54a9f | establecida_en | TextoOrdenado_ri_secoexpo_pdf` — RI:sin_raiz · observacion:12

Texto que vio E3 de `ri_secoexpo::Sbloque3` (e0, bloque de lista True; págs. 10, 11):

```
[texto propio | punto Sbloque3]
APARTADO B – B.3. CERTIFICACION DE INCUMPLIDO / EN GESTION DE COBRO
B.3. CERTIFICACIÓN DE INCUMPLIDO EN GESTIÓN DE COBRO.
Datos solicitados:
1. Número de incumplido: otorgado por la entidad vinculado a la denuncia de incumplimiento de la
destinación.
2. C.U.I.T. del exportador.
3. N° de destinación de exportación: Número de embarque o destinación de exportación que se
certifica como incumplida en gestión de cobro.
4. Valor pendiente: monto pendiente de liquidación y/o aplicación a la fecha de información
expresado en la moneda del FOB.
5. Monto en dólares: monto pendiente de liquidación y/o aplicación expresado en su equivalente en
dólares estadounidenses.
6. Código de Condición.
El dato “Código de Condición” debe corresponder a uno de los códigos del siguiente listado:
[TABLA ri_secoexpo::tabla001 | página 10 | e0_tablas | columnas]
Columnas: col1 | Código | col3 | col4 | Descripción | col6
Fila 1: col1 = 1 ⟨abarca hasta col3⟩ | col4 = Control de Cambios en el país del importador. ⟨abarca hasta col6⟩
Fila 2: col1 = 2 ⟨abarca hasta col3⟩ | col4 = Insolvencia del importador. ⟨abarca hasta col6⟩
Fila 3: col1 = 3 ⟨abarca hasta col3⟩ | col4 = Deudor moroso con acciones judiciales en curso. ⟨abarca hasta col6⟩
Fila 4: col1 = 4 ⟨abarca hasta col3⟩ | col4 = Deudor moroso en gestión de cobro sin acciones. ⟨abarca hasta col6⟩
Fila 5: col1 = 5 ⟨abarca hasta col3⟩ | col4 = Deudores Morosos con gestión de cobro a través de agencias de recupero o com- pañías de seguro de crédito a la exportación. ⟨abarca hasta col6⟩
Fila 6: col1 = 6 ⟨abarca hasta col3⟩ | col4 = Deudor moroso constituido por un organismo del sector público del país desti- natario habiéndose efectuado los reclamos según legislación aplicable. ⟨abarca hasta col6⟩
Fila 7: col1 = 7 ⟨abarca hasta col3⟩ | col4 = Deudor moroso que ha generado el cobro de un seguro de crédito a la exportación con subrogación de derechos en favor de la compañía de seguro ⟨abarca hasta col6⟩
[FIN TABLA ri_secoexpo::tabla001]
El equivalente en dólares estadounidenses del monto pendiente de cumplimiento se calculará
utilizando el tipo de pase con el dólar estadounidense de la moneda en que se expresa el valor FOB
de la destinación, a la fecha de vencimiento del plazo para la negociación de las divisas
correspondientes al cobro de la exportación.
La entidad deberá reportar cualquier modificación que implique una reducción del monto pendiente
o un cambio en la condición que habilitó la inclusión del permiso de embarque en la categoría
“Incumplido en gestión de cobro”.
Las novedades que se registren deberán ser informadas remitiendo una nueva certificación con el
mismo número de incumplimiento ya asignado y detallando nuevamente la totalidad de la
información requerida.
No será necesario informar el ingreso total de las divisas pendientes de una destinación que tenía la
condición de “Incumplido en gestión de cobro”, la certificación pasará al estado inactiva
automáticamente a partir de la recepción del cierre de la denuncia de incumplido.
El total acumulado por el exportador, por año calendario, para el dato “Código de Condición” igual al
código N° 4 se computará tomando la suma del valor equivalente en dólares estadounidenses de
las certificaciones de incumplido en gestión de cobro activas para destinaciones del exportador
oficializadas cada año.
En el caso que se informe una operación con el dato “Código de Condición” igual al código N° 5, el
monto en dólares no podrá superar el límite establecido normativamente.
```

Versión: final (grafo sin cola).
- origen: {"id": "Obligacion_la_entidad_debe_reportar_cualquier_modificacion_que_implique_una_reduccion_del_m_d54a9f", "type": "Obligacion", "label": "Reportar modificaciones de monto o condición", "properties": {"tipo": "reporte_al_supervisor", "descripcion": "La entidad debe reportar cualquier modificación que implique una reducción del monto pendiente o un cambio en la condición que habilitó la inclusión del permiso de embarque en la categoría 'Incumplido en gestión de cobro'."}, "procedencia": {"chunk_id": "ri_secoexpo::Sbloque3", "punto": "Sbloque3", "rol_documental": "punto_propio", "tramo": "La entidad deberá reportar cualquier modificación que implique una reducción del monto pendiente o un cambio en la condición que habilitó la inclusión del permiso de embarque en la categoría \"Incumplido en gestión de cobro\".", "tramo_verificado": "exacta", "paginas": [10, 11]}}
- relación: `establecida_en`
- destino: {"id": "TextoOrdenado_ri_secoexpo_pdf", "type": "TextoOrdenado", "label": "Régimen Informativo Secundario Exportaciones", "properties": {"archivo": "ri_secoexpo.pdf", "materia": "RI Cont. Mensual - Seguimiento de las negociaciones de divisas de exportaciones de bienes", "version": "Comunicación A 8158 (vigencia 19/12/2024)"}, "procedencia": {"chunk_id": "ri_secoexpo::S0", "punto": "S0", "rol_documental": "punto_propio", "paginas": [1]}}
- arista: {"properties": {}, "procedencia": {"chunk_id": "ri_secoexpo::Sbloque3", "punto": "Sbloque3", "rol_documental": "punto_propio", "paginas": [10, 11]}}

## 8. `Obligacion_la_entidad_debera_transmitir_nuevamente_sus_partes_que_continuen_siendo_validas__b7eb56 | establecida_en | TextoOrdenado_ri_secoexpo_pdf` — RI:sin_raiz · observacion:12

Texto que vio E3 de `ri_secoexpo::SC` (e0, bloque de lista True; págs. 16):

```
[encabezado | punto Sbloque7]
25.SEGUIMIENTO DE LAS NEGOCIACIONES DE DIVISAS / APARTADO C – BAJA DE REPORTES DE LAS ENTIDADES / EN EL SEGUIMIENTO
[texto propio | punto SC]
APARTADO C: BAJA DE REPORTES DE LAS ENTIDADES EN EL SEGUIMIENTO.
A través de este Apartado la entidad podrá requerir la baja de reportes remitidos por cualquiera de
las siguientes secciones:
B.1. Certificación de cumplido
B.2. Denuncia de incumplido
B.3. Certificación de incumplido en gestión de cobro
B.4. Certificación de extensión de plazo.
B.5. Aplicaciones y otras imputaciones.
En el caso del requerimiento B.6., los errores en los datos enviados deberán revertirse mediante
una nueva cesión en sentido contrario.
El motivo de baja consignado constituye una declaración jurada por parte de la entidad. Al
consignarse un código de motivo que corresponda a una baja para rectificación, la entidad
financiera asume el compromiso de concretar tal rectificación dentro de los 2 días hábiles de
recibida la notificación de la aceptación de la baja solicitada.
Las solicitudes procesadas en forma exitosa que correspondan a reportes B.2. o B.5. resultarán en
la eliminación de todas las secuencias que componían el reporte dado de baja. La entidad deberá
transmitir nuevamente sus partes que continúen siendo válidas.
Dado que la rectificación de los incumplidos abiertos puede ser efectuada directamente a través
del reporte B.2., el código de motivo 2 sólo se admitirá en el caso de incumplidos cerrados, es
decir, aquellas denuncias para las cuales el dato “Valor pendiente” sea igual a cero.
Dado que la rectificación de los reportes B.5. puede ser efectuada directamente mediante el
envío de un nuevo reporte, no se admitirá el código de motivo 2.
En caso de que se procese exitosamente una solicitud de baja de una certificación de cumplido
(Reporte B.1.) y existiese una denuncia de incumplimiento “cerrada” asociada a dicho cumplido, el
sistema procederá automáticamente a excluir dicho Reporte B.2. La denuncia de incumplimiento,
abierta o cerrada según corresponda, deberá ser nuevamente transmitida por la entidad.
En caso de que se procese exitosamente una solicitud de baja de una denuncia de incumplido
(Reporte B.2.) y existiese una certificación de incumplido en gestión de cobro asociada a dicha
denuncia, el sistema procederá automáticamente a excluir dicho Reporte B.3. La certificación de
incumplido en gestión de cobro, en caso de corresponder, deberá ser nuevamente transmitida por
la entidad.
```

Versión: final (grafo sin cola).
- origen: {"id": "Obligacion_la_entidad_debera_transmitir_nuevamente_sus_partes_que_continuen_siendo_validas__b7eb56", "type": "Obligacion", "label": "Retransmisión de partes válidas", "properties": {"tipo": "presentacion_informativa", "descripcion": "La entidad deberá transmitir nuevamente sus partes que continúen siendo válidas tras la eliminación de secuencias de reportes B.2. o B.5."}, "procedencia": {"chunk_id": "ri_secoexpo::SC", "punto": "SC", "rol_documental": "punto_propio", "tramo": "La entidad deberá transmitir nuevamente sus partes que continúen siendo válidas", "tramo_verificado": "exacta", "paginas": [16]}}
- relación: `establecida_en`
- destino: {"id": "TextoOrdenado_ri_secoexpo_pdf", "type": "TextoOrdenado", "label": "Régimen Informativo Secundario Exportaciones", "properties": {"archivo": "ri_secoexpo.pdf", "materia": "RI Cont. Mensual - Seguimiento de las negociaciones de divisas de exportaciones de bienes", "version": "Comunicación A 8158 (vigencia 19/12/2024)"}, "procedencia": {"chunk_id": "ri_secoexpo::S0", "punto": "S0", "rol_documental": "punto_propio", "paginas": [1]}}
- arista: {"properties": {}, "procedencia": {"chunk_id": "ri_secoexpo::SC", "punto": "SC", "rol_documental": "punto_propio", "paginas": [16]}}

## 9. `Obligacion_registro_de_montos_en_miles_de_pesos__ri_acsf_s0_06b55a | aplica_a | Sujeto_entidad_financiera` — RI:sin_raiz · observacion:12

Texto que vio E3 de `ri_acsf::S0` (e0, bloque de lista True; págs. 1):

```
[texto propio | punto S0]
Preámbulo
I – INSTRUCCIONES GENERALES
Las entidades financieras que tengan contratos con agencias complementarias de servicios finan-
cieros para delegar la atención de sus clientes y público en general, informarán los datos sobre
cantidades y montos respecto de las operaciones y servicios realizados en el mes bajo informe,
por parte de tales agencias, teniendo en cuenta las actividades comprendidas en la Sección 9.
“Agencias complementarias de servicios financieros” de las normas sobre “Expansión de entida-
des financieras”. Asimismo, se informará el listado de personas que hayan operado por medio de
dichas unidades de servicios.
Los montos se registrarán en miles de pesos, sin decimales. A los fines del redondeo de las mag-
nitudes se incrementarán los valores en una unidad cuando el primer digito de las fracciones sea
igual o mayor que 5, desechando las que resulten inferiores.
II – INFORMACIÓN SOLICITADA
```

Versión: final (grafo sin cola).
- origen: {"id": "Obligacion_registro_de_montos_en_miles_de_pesos__ri_acsf_s0_06b55a", "type": "Obligacion", "label": "Registro de montos en miles de pesos", "properties": {"tipo": "presentacion_informativa"}, "procedencia": {"chunk_id": "ri_acsf::S0", "punto": "S0", "rol_documental": "punto_propio", "tramo": "Los montos se registrarán en miles de pesos, sin decimales", "tramo_verificado": "exacta", "paginas": [1]}}
- relación: `aplica_a`
- destino: {"id": "Sujeto_entidad_financiera", "type": "Sujeto", "label": "Entidades financieras", "properties": {"nivel": "clase", "alias": ["Entidades financieras emisoras de tarjetas de crédito y/o compra", "Entidad financiera emisora de tarjetas de crédito y/o compra"]}, "procedencia": {"chunk_id": "ri_esd::Sbloque1::chapeau_seccion", "punto": "Sbloque1", "rol_documental": "bloque_chapeau_seccion", "paginas": [1, 2]}}
- arista: {"properties": {}, "sujeto_mencion": "Las entidades financieras", "mencion_verificada": "exacta", "metodo_resolucion": "R1_label_exacto", "sujeto_id_modelo": "Sujeto_rol_entidad_comprendida_reginf", "procedencia": {"chunk_id": "ri_acsf::S0", "punto": "S0", "rol_documental": "punto_propio", "paginas": [1]}}

## 10. `Obligacion_se_debe_informar_el_pais_de_residencia_del_accionista_ingresando_el_codigo_swift_38953a | aplica_a | Sujeto_entidad_financiera` — RI:sin_raiz · observacion:12

Texto que vio E3 de `ri_ii_31_12_19::4.2.7` (e0, bloque de lista True; págs. 11):

```
[encabezado | punto S4]
4. ACCIONISTAS
[encabezado | punto 4.2]
4.2. Datos de los accionistas de las entidades financieras y cambiarias:
[texto propio | punto 4.2.7]
4.2.7. Residencia: Se informará el país de residencia ingresando el pertinente código
Swift de país.
```

Versión: final (grafo sin cola).
- origen: {"id": "Obligacion_se_debe_informar_el_pais_de_residencia_del_accionista_ingresando_el_codigo_swift_38953a", "type": "Obligacion", "label": "Informar país de residencia con código Swift", "properties": {"descripcion": "Se debe informar el país de residencia del accionista ingresando el código Swift de país correspondiente", "tipo": "presentacion_informativa"}, "procedencia": {"chunk_id": "ri_ii_31_12_19::4.2.7", "punto": "4.2.7", "rol_documental": "punto_propio", "tramo": "Se informará el país de residencia ingresando el pertinente código Swift de país", "tramo_verificado": "exacta", "paginas": [11]}}
- relación: `aplica_a`
- destino: {"id": "Sujeto_entidad_financiera", "type": "Sujeto", "label": "Entidades financieras", "properties": {"nivel": "clase", "alias": ["Entidades financieras emisoras de tarjetas de crédito y/o compra", "Entidad financiera emisora de tarjetas de crédito y/o compra"]}, "procedencia": {"chunk_id": "ri_esd::Sbloque1::chapeau_seccion", "punto": "Sbloque1", "rol_documental": "bloque_chapeau_seccion", "paginas": [1, 2]}}
- arista: {"properties": {}, "sujeto_mencion": "las entidades financieras y cambiarias", "mencion_verificada": "exacta", "metodo_resolucion": "R4_sugerencia_modelo", "sujeto_id_modelo": "Sujeto_entidad_financiera", "procedencia": {"chunk_id": "ri_ii_31_12_19::4.2.7", "punto": "4.2.7", "rol_documental": "punto_propio", "paginas": [11]}}

## 11. `Condicion_primer_periodo_certificado_de_inscripcion_emitido__el_primer_periodo_de_presenta_85ef87 | establecida_en | TextoOrdenado_ri_psp_pdf` — RI:resto · observacion:12

Texto que vio E3 de `ri_psp::SI` (e0, bloque de lista True; págs. 2):

```
[texto propio | punto SI]
Sección I. INSTRUCCIONES GENERALES
El vencimiento para la presentación de las informaciones comprendidas en los Apartados A y B
operará -para todos los proveedores de servicios de pago que ofrecen cuentas de pago (PSPCP)-
el día 22 del mes siguiente al mes al que corresponden los datos (o día hábil inmediato posterior),
mientras que el vencimiento para la presentación del Apartado C operará el día 20 del mes subsi-
guiente a la finalización de cada trimestre calendario.
El primer periodo para el que deberán presentar información -mes para el caso de los Apartados
A y B, trimestre calendario para el Apartado C- será aquel en que la Superintendencia de Entida-
des Financieras y Cambiarias haya emitido el certificado de inscripción en el “Registro de provee-
dores de servicios de pago”.
Los importes se registrarán en miles de pesos, sin decimales. A los fines del redondeo de las
magnitudes se incrementarán los valores en una unidad cuando el primer digito de las fracciones
sea igual o mayor que 5, desechando las que resulten inferiores.
La información se presentará de acuerdo con lo establecido en las normas sobre “Presentación de
informaciones al Banco Central de la República Argentina”.
```

Versión: final (grafo sin cola).
- origen: {"id": "Condicion_primer_periodo_certificado_de_inscripcion_emitido__el_primer_periodo_de_presenta_85ef87", "type": "Condicion", "label": "Primer período — certificado de inscripción emitido", "properties": {"descripcion": "El primer período de presentación es aquel en que la Superintendencia de Entidades Financieras y Cambiarias haya emitido el certificado de inscripción en el Registro de proveedores de servicios de pago."}, "procedencia": {"chunk_id": "ri_psp::SI", "punto": "SI", "rol_documental": "punto_propio", "tramo": "El primer periodo para el que deberán presentar información -mes para el caso de los Apartados A y B, trimestre calendario para el Apartado C- será aquel en que la Superintendencia de Entidades Financieras y Cambiarias haya emitido el certificado de inscripción en el \"Registro de proveedores de servicios de pago\"", "tramo_verificado": "exacta", "paginas": [2]}}
- relación: `establecida_en`
- destino: {"id": "TextoOrdenado_ri_psp_pdf", "type": "TextoOrdenado", "label": "Régimen Informativo PSPCP", "properties": {"archivo": "ri_psp.pdf", "materia": "RI - Proveedores de servicios de pago que ofrecen cuentas de pago", "version": "Comunicación A 8284 (vigencia 01/07/2025)"}, "procedencia": {"chunk_id": "ri_psp::SI", "punto": "SI", "rol_documental": "punto_propio", "paginas": [2]}}
- arista: {"properties": {}, "procedencia": {"chunk_id": "ri_psp::SI", "punto": "SI", "rol_documental": "punto_propio", "paginas": [2]}}

## 12. `Obligacion_se_suspende_el_envio_de_informaciones_con_codigo_de_consolidacion_3_a_partir_del_62cec8 | aplica_a | Sujeto_propuesto_las_entidades__ri_ai` — RI:resto · observacion:12

Texto que vio E3 de `ri_ai::6.2` (e0, bloque de lista True; págs. 9):

```
[encabezado | punto S6]
Sección 6. Disposiciones transitorias
[texto propio | punto 6.2]
6.2. Suspensión de la observancia de las regulaciones técnicas sobre base consolidada
trimestral (punto 6.1. de las normas sobre “Supervisión consolidada”).
A partir del período de información abril/24:
- Se suspende el envío de informaciones con código de consolidación 3., siendo mar-
zo/24 el último período trimestral que corresponde informar para este nivel de conso-
lidación;
- Las operaciones de los entes a que refieren los incisos ii) y iii) del primer párrafo del
punto 6.2. de las normas sobre “Supervisión consolidada”, de corresponder, se in-
formarán sobre base consolidada mensual (códigos 2 ó 9).
- Las entidades financieras que hasta el 31/03/24 informaban únicamente códigos de
consolidación 1 y 3, de mantenerse esta situación de consolidación, pasarán a infor-
mar:
a) códigos 1 y 9 sólo si consolidan con alguno de los entes a que refieren los incisos
ii) y iii) del punto 6.2. de las normas citadas;
b) en caso contrario, código 0.
```

Versión: final (grafo sin cola).
- origen: {"id": "Obligacion_se_suspende_el_envio_de_informaciones_con_codigo_de_consolidacion_3_a_partir_del_62cec8", "type": "Obligacion", "label": "Suspensión envío consolidación 3 desde abril/24", "properties": {"tipo": "otra", "descripcion": "Se suspende el envío de informaciones con código de consolidación 3 a partir del período de información abril/24, siendo marzo/24 el último período trimestral que corresponde informar para este nivel de consolidación."}, "procedencia": {"chunk_id": "ri_ai::6.2", "punto": "6.2", "rol_documental": "punto_propio", "tramo": "Se suspende el envío de informaciones con código de consolidación 3., siendo marzo/24 el último período trimestral que corresponde informar para este nivel de consolidación", "tramo_verificado": "exacta", "paginas": [9]}}
- relación: `aplica_a`
- destino: {"id": "Sujeto_propuesto_las_entidades__ri_ai", "type": "Sujeto", "label": "las entidades", "properties": {"nivel": "propuesto", "cuarentena": "true", "colision_cross_to": "true", "padre_sugerido": "Sujeto_rol_entidad_comprendida_reginf", "padre_desde_sugerencia_modelo": "true"}, "procedencia": {"chunk_id": "ri_ai::3.4", "punto": "3.4", "rol_documental": "punto_propio", "paginas": [6]}}
- arista: {"properties": {}, "sujeto_mencion": "las entidades", "mencion_verificada": "exacta", "metodo_resolucion": "cuarentena", "sujeto_id_modelo": "Sujeto_rol_entidad_comprendida_reginf", "procedencia": {"chunk_id": "ri_ai::6.2", "punto": "6.2", "rol_documental": "punto_propio", "paginas": [9]}}

## 13. `Obligacion_las_entidades_financieras_deberan_informar_los_componentes_del_ratio_de_fondeo_n_16526e | establecida_en | TextoOrdenado_ri_tsa_pdf` — RI:resto · observacion:12

Texto que vio E3 de `ri_tsa::3.2` (e0, bloque de lista True; págs. 80, 81, 82, 83, 84, 85):

```
[encabezado | punto S3]
Sección 3. Medición del Ratio
[texto propio | punto 3.2]
3.2. Conceptos computables
Se informarán los componentes del “Ratio de fondeo neto estable – NSFR” sin ponderar,
correspondientes al último día del trimestre, según las instrucciones respectivas.
Fondeo Estable Disponible
Código 10100: Capital ordinario de Nivel 1 (CO n1), capital adicional de nivel 1 (CA n1) y
capital de nivel 2 (PNc) -sin deducir los conceptos allí admitidos-, excluidos los instru-
mentos de Nivel 2 con vencimiento residual inferior a un año (punto 2.3.1.1 de las nor-
mas sobre “Ratio de fondeo neto estable”).
Código 10200: Instrumentos de capital –no comprendidos en el código 10100 – con
vencimiento residual efectivo igual o superior a un año (punto 2.3.1.2 de las normas so-
bre “Ratio de fondeo neto estable”).
Código 10300: Préstamos y otros pasivos –incluye depósitos a plazo– con vencimiento
residual efectivo igual o superior a un año (punto 2.3.1.3 de las normas sobre “Ratio de
fondeo neto estable”).
Código 10400: Pasivos por impuestos diferidos cuya fecha de cancelación más próxima
posible sea igual o superior a un año y participaciones minoritarias (puntos 2.3.1.4 y
2.3.1.5 de las normas sobre “Ratio de fondeo neto estable”).
Código 10500: Depósitos a la vista y a plazo “estables” con vencimiento residual inferior
a un año, realizados por clientes minoristas y MiPyMEs (punto 2.3.2 de las normas so-
bre “Ratio de fondeo neto estable”).
Código 10600: Depósitos a la vista y depósitos a plazo no comprendidos en el código
10500 con vencimiento residual inferior a un año, realizados por clientes minoristas y
MiPyMEs (punto 2.3.3.1 de las normas sobre “Ratio de fondeo neto estable”).
Código 10650: Depósitos a la vista y a plazo ordenados por la justicia en las causas sin
sentencia firme (punto 2.3.3.2 de las normas sobre “Ratio de fondeo neto estable”).
Código 10700: Fondeo garantizado o no garantizado del sector privado no financiero –
excepto MiPyMEs– con vencimiento residual inferior a un año (punto 2.3.4.1 de las nor-
mas sobre “Ratio de fondeo neto estable”).
Código 10800: Depósitos operativos conforme al punto 4.2.2 de las normas sobre “Ratio
de cobertura de liquidez” (punto 2.3.4.2 de las normas sobre “Ratio de fondeo neto esta-
ble”).
Código 10900: Fondeo obtenido del Gobierno Nacional y del resto del sector público no
financiero, de otros estados soberanos y de entes del sector público no financiero de
esos estados y de bancos multilaterales de desarrollo, con vencimiento residual inferior
a un año (punto 2.3.4.3 de las normas sobre “Ratio de fondeo neto estable”).
Código 11000: Otro fondeo (garantizado o no garantizado) no incluido en los códigos
10700 a 10900 con vencimiento residual desde seis meses hasta menos de un año –
incluye el fondeo procedente del Banco Central de la República Argentina y bancos cen-
trales de otros estados soberanos y de instituciones del sector financiero (punto 2.3.4.4
de las normas sobre “Ratio de fondeo neto estable”).
Código 11100: Pasivos por impuestos diferidos cuya fecha de cancelación más próxima
posible está comprendida entre seis meses y menos de un año (punto 2.3.4.5 de las
normas sobre “Ratio de fondeo neto estable”).
Código 11200: Instrumentos de capital no incluidos en los códigos 10100 y 10200., y
pasivos no comprendidos en los códigos anteriores –incluido fondeo con vencimiento
residual inferior a seis meses del BCRA, de bancos centrales de otros estados sobera-
nos y de instituciones del sector financiero (punto 2.3.5.1 de las normas sobre “Ratio de
fondeo neto estable”).
Código 11300: Otros pasivos con plazo de vencimiento indeterminado; incluye posicio-
nes vendidas y con plazo de vencimiento indeterminado –excluidos pasivos por impues-
tos diferidos y participaciones minoritarias previstas en los códigos 10400 y 11100, res-
pectivamente– (punto 2.3.5.2 de las normas sobre “Ratio de fondeo neto estable”).
Código 11400: Pasivos originados en operaciones de derivados netos de activos origi-
nados por derivados, si los pasivos resultan ser superiores a los activos (punto 2.3.5.3
de las normas sobre “Ratio de fondeo neto estable”).
Código 11500: Importes pendientes de pago por compras de instrumentos financieros,
divisas o productos básicos (punto 2.3.5.4 de las normas sobre “Ratio de fondeo neto
estable”).
Código 11550: Depósitos a la vista y a plazo ordenados por la justicia en las causas con
sentencia firme (punto 2.3.5.5 de las normas sobre “Ratio de fondeo neto estable”).
Código 11600: Pasivos interdependientes de acuerdo con disposiciones contractuales,
donde el pasivo no pueda vencer mientras el activo permanezca en el balance y no
puede utilizarse para financiar otros activos, en la medida que se verifiquen los criterios
establecidos en la sección 4 de las normas sobre “Ratio de fondeo neto estable”.
Fondeo Estable Requerido
Código 20100: Efectivo en caja, en tránsito, en transportadoras de valores y en cajeros
automáticos (punto 3.3.2.1 de las normas sobre “Ratio de fondeo neto estable”).
Código 20200: Depósitos en el BCRA –incluidos los computables como integración de
efectivo mínimo–, sin considerar los montos en cuentas especiales de garantía (punto
3.3.2.2 de las normas sobre “Ratio de fondeo neto estable”).
Código 20300: Exposiciones al BCRA y a bancos centrales de otros soberanos con ven-
cimiento residual inferior a seis meses (punto 3.3.2.3 de las normas sobre “Ratio de fon-
deo neto estable”).
Código 20400: Importes pendientes de liquidación por ventas de instrumentos financie-
ros, divisas o productos básicos (punto 3.3.2.4 de las normas sobre “Ratio de fondeo ne-
to estable”).
Código 20500: Activos interdependientes cuyos flujos de pago principal solo puedan
destinarse a la cancelación del pasivo, y el pasivo no pueda usarse para financiar otro
activo, en la medida que se verifiquen los criterios establecidos en la sección 4 de las
normas sobre “Ratio de fondeo neto estable”.
Código 206XX: Activos de Nivel 1 (A n1) libres de restricciones, excluidos los activos
que por su vencimiento residual estén previstos en los códigos anteriores. (punto 3.3.3
de las normas sobre “Ratio de fondeo neto estable”).
Código 20610: Títulos públicos nacionales e instrumentos de regulación monetaria del
BCRA en pesos (punto 3.3.3.1 de las normas sobre “Ratio de fondeo neto estable”).
Código 20620: Títulos públicos nacionales e instrumentos de regulación monetaria del
BCRA en moneda extranjera (punto 3.3.3.2 de las normas sobre “Ratio de fondeo neto
estable”).
Código 20630: Títulos valores emitidos y garantizados por el Banco de Pagos Interna-
cionales, Fondo Monetario Internacional, Banco Central Europeo, Unión Europea o Ban-
cos Multilaterales de Desarrollo (punto 3.3.3.3 de las normas sobre “Ratio de fondeo ne-
to estable”).
Código 20640: Títulos de deuda emitidos por otros soberanos (o sus bancos centrales)
en sus respectivas monedas (punto 3.3.3.4 de las normas sobre “Ratio de fondeo neto
estable”).
Código 20650: Títulos de deuda emitidos por otros soberanos (o sus bancos centrales)
en una moneda extranjera –distinta de la respectiva moneda de esos soberanos– (punto
3.3.3.5 de las normas sobre “Ratio de fondeo neto estable”).
Código 20700: Préstamos libres de restricciones con vencimiento residual inferior a seis
meses otorgados a instituciones del sector financiero, en la medida que estén garantiza-
dos con alguna de los activos Nivel 1 (A n1) y la entidad financiera tenga la capacidad
de reafectar libremente el activo recibido en garantía durante la vida del préstamo (punto
3.3.4 de las normas sobre “Ratio de fondeo neto estable”).
Código 20800: Préstamos libres de restricciones con vencimiento residual inferior a seis
meses otorgados a instituciones del sector financiero, no incluidos en el código 20700.
Incluye depósitos no operativos mantenidos en instituciones del sector financiero con-
forme al punto 3.2.7.1. (punto 3.3.5 de las normas sobre “Ratio de fondeo neto estable”).
Código 20900: Activos de Nivel 1 (A n1) de disponibilidad restringida durante un período
de entre seis meses y menos de un año (punto 3.3.6.1 de las normas sobre “Ratio de
fondeo neto estable”).
Código 21000: Préstamos otorgados a instituciones del sector financiero –incluye depó-
sitos no operativos mantenidos en ese sector conforme al punto 3.2.7.2 de la norma so-
bre “Ratio de fondeo neto estable”–, al BCRA y a bancos centrales de otros soberanos,
con vencimiento residual igual o superior a seis meses e inferiores a un año (punto
3.3.6.2 de las normas sobre “Ratio de fondeo neto estable”).
Código 21100: Depósitos operativos mantenidos en instituciones del sector financiero
(punto 3.3.6.3 de la norma).
Código 21200: Activos que no sean considerados como de Nivel 1 (A n1) y no estén
comprendidos en los códigos 20100 a 21100. con vencimiento residual inferior a un año,
incluidos préstamos a clientes minoristas, a MiPyMEs, a empresas del sector privado no
financiero, al Gobierno Nacional, al resto del sector público no financiero y a otros sobe-
ranos y entes del sector público no financiero de esos estados (punto 3.3.6.4 de las
normas sobre “Ratio de fondeo neto estable”).
Código 21300: Financiaciones con garantía hipotecaria sobre vivienda residencial –
única, familiar y de ocupación permanente– libres de restricciones sujetas a un ponde-
rador de riesgo igual o menor al 35 % de acuerdo con las normas sobre “Capitales mí-
nimos de las entidades financieras” con vencimiento residual igual o superior a un año
(punto 3.3.7.1 de las normas sobre “Ratio de fondeo neto estable”).
Código 21400: Otros préstamos libres de restricciones no incluidos en los códigos
20100 a 21300. –excluidos los otorgados a instituciones del sector financiero– con ven-
cimiento residual igual o superior a un año, sujetos a un ponderador de riesgo del 35 %
o menor conforme a lo establecido en las normas sobre “Capitales mínimos de las enti-
dades financieras” (punto 3.3.7.2 de las normas sobre “Ratio de fondeo neto estable”).
Código 21500: Activos constituidos en garantía –tales como efectivo y títulos valores,
incluso los que se encontraren fuera de balance– en concepto de margen inicial por con-
tratos de derivados –salvo que, por aplicación de otro punto les corresponda un mayor
FER– y el efectivo u otros activos aportados como contribución al fondo de garantía
constituido para hacer frente a incumplimientos de una CCP (punto 3.3.8.1 de las nor-
mas sobre “Ratio de fondeo neto estable”).
Código 21600: Otros préstamos libres de restricciones con hasta 90 días de atraso y
sujetos a un ponderador de riesgo superior al 35 % conforme a lo establecido en las
normas sobre “Capitales mínimos de las entidades financieras” y con vencimiento resi-
dual igual o superior a un año, excluidos los préstamos a instituciones del sector finan-
ciero (punto 3.3.8.2 de las normas sobre “Ratio de fondeo neto estable”).
Código 21700: Títulos de deuda con vencimiento residual igual o superior a un año y
acciones negociadas en mercados de valores, que no se consideren como activos de
Nivel 1 (A n1), libres de restricciones y correspondientes a emisores que no se encuen-
tren en situación de incumplimiento (punto 3.3.8.3 de las normas sobre “Ratio de fondeo
neto estable”).
Código 21800: Productos básicos negociados físicamente, incluido el oro (punto 3.3.8.4
de las normas sobre “Ratio de fondeo neto estable”).
Código 21900: Activos de disponibilidad restringida por período igual o superior a un año
(punto 3.3.9.1 de las normas sobre “Ratio de fondeo neto estable”).
Código 22000: Activos originados en operaciones con derivados calculados conforme a
lo establecido en el punto 3.2.5., netos de los pasivos originados en operaciones con de-
rivados calculados conforme al punto 2.2.2., siempre que los activos sean superiores a
los pasivos (punto 3.3.9.2 de las normas sobre “Ratio de fondeo neto estable”).
Código 22100: Demás activos no incluidos en los códigos 20100 a 22000. Incluye prés-
tamos con más de 90 días de atraso; préstamos a instituciones del sector financiero, con
vencimiento residual igual o superior a un año; acciones no negociadas en mercados de
valores; activos fijos; conceptos deducibles de la RPC y todo otro activo ponderado al
1250 %, conforme a lo previsto en las normas sobre “Capitales mínimos de las entida-
des financieras”. Incluye depósitos no operativos mantenidos en instituciones del sector
financiero según punto 3.2.7.3. (punto 3.3.9.3 de las normas sobre “Ratio de fondeo neto
estable”).
Código 22200: 20% de los pasivos originados en operaciones de derivados –costo de
reposición negativo– calculados según el punto 2.2.2. (sin deducir el margen de varia-
ción que se hubiera constituido), independientemente de su posición neta (punto 3.3.9.4
de las normas sobre “Ratio de fondeo neto estable”).
Exposiciones fuera de balance.
Código 223XX Exposiciones fuera de balance.
Código 22310: Facilidades de crédito y de liquidez comprometidas (monto no utilizado) –
con arreglo a la definición del punto 4.4.4. de las normas sobre “Ratio de cobertura de li-
quidez”–, otorgadas a cualquier contraparte (punto 3.4.1 de las normas sobre “Ratio de
fondeo neto estable”).
Código 22320: Facilidades de crédito y de liquidez no comprometidas (monto no utiliza-
do) –conforme a la definición del punto 4.4.6.3. de las normas sobre “Ratio de cobertura
de liquidez”– otorgadas a cualquier contraparte (punto 3.4.2.1 de las normas sobre “Ra-
tio de fondeo neto estable”).
Código 22330: Operaciones de financiación al comercio exterior –tales como garantías y
cartas de crédito– (punto 3.4.2.2 de las normas sobre “Ratio de fondeo neto estable”).
Código 22340: Garantías y cartas de crédito no relacionadas con operaciones de finan-
ciación al comercio exterior (punto 3.4.2.3 de las normas sobre “Ratio de fondeo neto
estable”).
Código 223XX: Obligaciones no contractuales (punto 3.4.2.4 de las normas sobre “Ratio
de fondeo neto estable”).
Código 22351: solicitudes de recompra de deuda emitida por la propia entidad financiera
o por vehículos de inversión vinculados u otra facilidad financiera de ese tipo.
Código 22352: productos estructurados, para mantener su negociabilidad, tales como
bonos a interés variable y bonos a la vista a interés variable (VRDN).
Código 22353: fondos administrados que se comercializan con el objetivo de mantener
un valor estable.
Código 22354: Otras obligaciones no contractuales.
Código 22260: Otras exposiciones fuera de balance (punto 3.4.2.5 de las normas sobre
“Ratio de fondeo neto estable”).
Totales de control
Código 10000: Monto total del Fondeo Estable Disponible (MFED), aplicando los ponde-
radores correspondientes a cada concepto.
Código 20000: Monto total de Fondeo Estable Requerido (MFER), aplicando los ponde-
radores correspondientes a cada concepto.
```

Versión: final (grafo sin cola).
- origen: {"id": "Obligacion_las_entidades_financieras_deberan_informar_los_componentes_del_ratio_de_fondeo_n_16526e", "type": "Obligacion", "label": "Informar componentes del NSFR", "properties": {"tipo": "presentacion_informativa", "descripcion": "Las entidades financieras deberán informar los componentes del Ratio de fondeo neto estable – NSFR sin ponderar, correspondientes al último día del trimestre, según las instrucciones respectivas."}, "procedencia": {"chunk_id": "ri_tsa::3.2", "punto": "3.2", "rol_documental": "punto_propio", "tramo": "Se informarán los componentes del \"Ratio de fondeo neto estable – NSFR\" sin ponderar, correspondientes al último día del trimestre, según las instrucciones respectivas.", "tramo_verificado": "exacta", "paginas": [80, 81, 82, 83, 84, 85]}}
- relación: `establecida_en`
- destino: {"id": "TextoOrdenado_ri_tsa_pdf", "type": "TextoOrdenado", "label": "Ratio de Cobertura de Liquidez", "properties": {"archivo": "ri_tsa.pdf", "materia": "RI para supervisión", "version": "Comunicación A 8465 (vigencia 31/07/2026)"}, "procedencia": {"chunk_id": "ri_tsa::S1", "punto": "S1", "rol_documental": "punto_propio", "paginas": [63]}}
- arista: {"properties": {}, "procedencia": {"chunk_id": "ri_tsa::3.2", "punto": "3.2", "rol_documental": "punto_propio", "paginas": [80, 81, 82, 83, 84, 85]}}

## 14. `Obligacion_si_se_registra_exceso_el_importe_debera_informarse_teniendo_en_cuenta_el_tratami_3298d4 | establecida_en | TextoOrdenado_ri_ai_pdf` — RI:resto · observacion:12

Texto que vio E3 de `ri_ai::1.2.2` (e0, bloque de lista True; págs. 2):

```
[encabezado | punto S1]
Sección 1. Entidades Comprendidas
[encabezado | punto 1.2]
1.2. Sujetas al régimen de información sobre bases consolidadas:
[texto propio | punto 1.2.2]
1.2.2 Entidades financieras, filiales y subsidiarias significativas en el país y en el ex-
terior.
Las entidades financieras –excepto las que consoliden con otra/s entidad/es
financiera/s- no presentarán la información consolidada mensual, debiendo
consignar en su lugar, de acuerdo con las instrucciones operativas instrumen-
tadas a través de la respectiva Circular RUNOR, los siguientes datos:
- importe de activos inmovilizados y otros conceptos, (Código 100- Código
200+ Código 300)
- el 100% de la responsabilidad patrimonial computable de la entidad finan-
ciera del mes que corresponda.
- Detalle de las eventuales franquicias otorgadas (Códigos 401/402/403)
De registrar exceso, el importe deberá informarse teniendo en cuenta el tratamiento
establecido a través del texto ordenado de las normas sobre “Incumplimientos de capi-
tales mínimos y relaciones técnicas. Criterios aplicables”.
```

Versión: final (grafo sin cola).
- origen: {"id": "Obligacion_si_se_registra_exceso_el_importe_debera_informarse_teniendo_en_cuenta_el_tratami_3298d4", "type": "Obligacion", "label": "Informar exceso según normas de capitales mínimos", "properties": {"descripcion": "Si se registra exceso, el importe deberá informarse teniendo en cuenta el tratamiento establecido a través del texto ordenado de las normas sobre Incumplimientos de capitales mínimos y relaciones técnicas. Criterios aplicables.", "tipo": "reporte_al_supervisor"}, "procedencia": {"chunk_id": "ri_ai::1.2.2", "punto": "1.2.2", "rol_documental": "punto_propio", "tramo": "De registrar exceso, el importe deberá informarse teniendo en cuenta el tratamiento establecido a través del texto ordenado de las normas sobre \"Incumplimientos de capitales mínimos y relaciones técnicas. Criterios aplicables\".", "tramo_verificado": "exacta", "paginas": [2]}}
- relación: `establecida_en`
- destino: {"id": "TextoOrdenado_ri_ai_pdf", "type": "TextoOrdenado", "label": "Régimen Informativo sobre Bases Consolidadas", "properties": {"archivo": "ri_ai.pdf", "materia": "RI Cont. Mensual - Relación para los activos inmovilizados y otros conceptos", "version": "Comunicación A 8009 (vigencia 01/04/2024)"}, "procedencia": {"chunk_id": "ri_ai::1.1", "punto": "1.1", "rol_documental": "punto_propio", "paginas": [2]}}
- arista: {"properties": {}, "procedencia": {"chunk_id": "ri_ai::1.2.2", "punto": "1.2.2", "rol_documental": "punto_propio", "paginas": [2]}}

## 15. `Definicion_cuenta_de_pago_comercial__se_debe_utilizar_cuando_los_movimientos_habituales_de__df59a0 | establecida_en | TextoOrdenado_ri_psp_pdf` — RI:resto · observacion:12

Texto que vio E3 de `ri_psp::Sbloque2` (e0, bloque de lista True; págs. 11):

```
[encabezado | punto SIII]
Sección III. APARTADO B: INFORMACIÓN ESTADÍSTICA – SISTEMA NACIONAL DE PAGOS
[texto propio | punto Sbloque2]
Cuenta a acreditar
Cuenta de pago “comercial”: se debe utilizar cuando los movimientos habituales de la
cuenta están relacionados con la actividad comercial del cliente (puede ser persona humana
o jurídica). El criterio para definir la categoría a partir de la habitualidad es atribución de cada
PSPCP.
Cuenta de pago “personal/no comercial”: se debe utilizar cuando los movimientos no se
relacionan con actividades comerciales (puede ser persona humana o jurídica).
Cuenta de otro PSPCP: se utiliza en el caso de que quien recibe el pago o transferencia
acredite sus fondos en una cuenta de pago de otro PSPCP distinto a quien realiza la presen-
tación al RI.
Cuenta de EF: se utiliza en el caso de que quien recibe el pago o transferencia acredite sus
fondos en una cuenta bancaria.
Otros: se utiliza en el caso de que los fondos no se acreditan en una cuenta, sino que son
extraídos en efectivo.
```

Versión: final (grafo sin cola).
- origen: {"id": "Definicion_cuenta_de_pago_comercial__se_debe_utilizar_cuando_los_movimientos_habituales_de__df59a0", "type": "Definicion", "label": "Cuenta de pago comercial", "properties": {"termino": "Cuenta de pago \"comercial\"", "descripcion": "Se debe utilizar cuando los movimientos habituales de la cuenta están relacionados con la actividad comercial del cliente (puede ser persona humana o jurídica). El criterio para definir la categoría a partir de la habitualidad es atribución de cada PSPCP."}, "procedencia": {"chunk_id": "ri_psp::Sbloque2", "punto": "Sbloque2", "rol_documental": "punto_propio", "tramo": "Cuenta de pago \"comercial\": se debe utilizar cuando los movimientos habituales de la cuenta están relacionados con la actividad comercial del cliente (puede ser persona humana o jurídica).", "tramo_verificado": "exacta", "termino_verificado": "exacta", "paginas": [11]}}
- relación: `establecida_en`
- destino: {"id": "TextoOrdenado_ri_psp_pdf", "type": "TextoOrdenado", "label": "Régimen Informativo PSPCP", "properties": {"archivo": "ri_psp.pdf", "materia": "RI - Proveedores de servicios de pago que ofrecen cuentas de pago", "version": "Comunicación A 8284 (vigencia 01/07/2025)"}, "procedencia": {"chunk_id": "ri_psp::SI", "punto": "SI", "rol_documental": "punto_propio", "paginas": [2]}}
- arista: {"properties": {}, "procedencia": {"chunk_id": "ri_psp::Sbloque2", "punto": "Sbloque2", "rol_documental": "punto_propio", "paginas": [11]}}

## 16. `Definicion_ipr_f_indicador_de_provisiones_minimas__indicador_de_provisiones_minimas_exigida_4f38ba | establecida_en | TextoOrdenado_seggar_pdf` — NG:sin_raiz · observacion:12

Texto que vio E3 de `seggar::7.1` (e0, bloque de lista True; págs. 7, 8):

```
[encabezado | punto S7]
7. Determinación del aporte adicional.
[texto propio | punto 7.1]
7.1. Entidades con calificación “CAMELS”.
Surgirá de la siguiente expresión:
Ic = {(Ipr/f + Iar/a + 2 Icamels)/4} - Irpc/Kmin
x
donde:
Ipr/f: indicador a que se refiere el punto 3.3.1. que tomará el valor que surja de la
siguiente expresión:
Ipr/f = (Vi/0,04)1,20
donde
Vi: relación entre las previsiones mínimas exigidas según el punto 2.1. de las
normas sobre “Previsiones mínimas por riesgo de incobrabilidad” y el total de
financiaciones comprendidas (Sección 2. de las normas sobre “Clasificación
de deudores”). Dicho concepto incluye los saldos de las garantías otorgadas
por obligaciones asumidas por cuenta de terceros, registrados al último día
del mes de que se trate, según la clasificación informada en el estado de si-
tuación de deudores.
El valor del índice estará acotado entre 1 y 2,5. Es decir que en los casos en que
el resultado de la expresión sea, respectivamente, menor o mayor que esos lími-
tes inferior y superior, se tomará 1 o 2,5, según corresponda.
Iar/a: indicador a que se refiere el punto 3.3.2. que tomará el valor que surja de la
siguiente expresión:
Iar/a = (Vi/0,70)1,30
donde
Vi: relación entre los activos ponderados por riesgo de crédito –APRc– de la en-
tidad y la suma de los conceptos A y PFB –este último multiplicado por el
correspondiente CCF–, conforme a lo establecido en el punto 2.1. de las
normas sobre “Capitales mínimos de las entidades financieras”.
Se excluirán del cómputo las exposiciones al sector público no financiero.
El valor del índice estará acotado entre 1 y 2. Es decir que en los casos en que
el resultado de la expresión sea, respectivamente, menor o mayor que esos lími-
tes inferior y superior, se tomará 1 o 2, según corresponda.
Icamels: indicador a que se refiere el punto 3.1. Se tomará el valor que surja de la
siguiente tabla:
Calificación Índice
1 1,00
2 1,33
3 1,66
4 2,00
5 2,00
La calificación que la Superintendencia de Entidades Financieras y Cambiarias
asigne a la entidad financiera será considerada a los fines del cálculo de los
aportes al Fondo de Garantía de los Depósitos que sean exigibles a partir del
tercer mes siguiente a aquel en que tuviere lugar la pertinente notificación.
Irpc/Kmin: indicador a que se refiere el punto 3.2. Se tomará el valor que surja de la
siguiente tabla:
Relación RPC/exigencia Indice
de capital mínimo
hasta 0,90 - 0,50
más de 0,90 a 0,95 - 0,25
más de 0,95 a 1,00 - 0,10
más de 1,00 a 1,10 0,00
más de 1,10 a 1,20 + 0,05
más de 1,20 a 1,30 + 0,10
más de 1,30 a 1,50 + 0,20
superior a 1,50 + 0,30
El valor del índice Ic estará acotado entre 1 y 2. Es decir que en los casos en que el resul-
tado de la expresión sea, respectivamente, menor o mayor que esos límites inferior y supe-
rior, se tomará 1 o 2, según corresponda.
Para el cálculo de las relaciones se considerarán los importes correspondientes al tercer
mes anterior a la fecha de vencimiento de los aportes.
```

Versión: final (grafo sin cola).
- origen: {"id": "Definicion_ipr_f_indicador_de_provisiones_minimas__indicador_de_provisiones_minimas_exigida_4f38ba", "type": "Definicion", "label": "Ipr/f: indicador de provisiones mínimas", "properties": {"termino": "Ipr/f", "descripcion": "Indicador de provisiones mínimas exigidas según punto 3.3.1., calculado como (Vi/0,04)^1,20, donde Vi es la relación entre previsiones mínimas exigidas y total de financiaciones comprendidas. El valor se acota entre 1 y 2,5."}, "procedencia": {"chunk_id": "seggar::7.1", "punto": "7.1", "rol_documental": "punto_propio", "tramo": "Ipr/f: indicador a que se refiere el punto 3.3.1. que tomará el valor que surja de la siguiente expresión: Ipr/f = (Vi/0,04)1,20", "tramo_verificado": "exacta", "termino_verificado": "exacta", "paginas": [7, 8]}}
- relación: `establecida_en`
- destino: {"id": "TextoOrdenado_seggar_pdf", "type": "TextoOrdenado", "label": "Seguro de Depósitos", "properties": {"archivo": "seggar.pdf", "materia": "Aplicación del sistema de seguro de garantía de depósitos", "version": "Comunicación A 8407 (vigencia 01/04/2026)"}, "procedencia": {"chunk_id": "seggar::S1", "punto": "S1", "rol_documental": "punto_propio", "paginas": [3]}}
- arista: {"properties": {}, "procedencia": {"chunk_id": "seggar::7.1", "punto": "7.1", "rol_documental": "punto_propio", "paginas": [7, 8]}}

## 17. `Operacion_deposito_en_cuenta_sueldo_seguridad_social__seggar_5_1_5_a2047d | aplica_a | Sujeto_entidad_financiera` — NG:sin_raiz · observacion:12

Texto que vio E3 de `seggar::5.1.5` (e0, bloque de lista True; págs. 4):

```
[encabezado | punto S5]
5.Alcances de la garantía.
[encabezado | punto 5.1]
5.1. Depósitos comprendidos.
[intro | punto 5.1]
Se encontrarán alcanzados con la cobertura que ofrece el sistema, los depósitos en pesos y
en moneda extranjera constituidos en las entidades participantes bajo la forma de:
[texto propio | punto 5.1.5]
5.1.5. Cuenta sueldo/de la seguridad social y especiales.
```

Versión: final (grafo sin cola).
- origen: {"id": "Operacion_deposito_en_cuenta_sueldo_seguridad_social__seggar_5_1_5_a2047d", "type": "Operacion", "label": "Depósito en cuenta sueldo/seguridad social", "properties": {"tipo": "depósito", "descripcion": "Depósito constituido en forma de cuenta sueldo, de la seguridad social o especiales, en pesos o moneda extranjera, en entidades participantes del sistema de garantía"}, "procedencia": {"chunk_id": "seggar::5.1.5", "punto": "5.1.5", "rol_documental": "punto_propio", "tramo": "Cuenta sueldo/de la seguridad social y especiales", "tramo_verificado": "exacta", "paginas": [4]}}
- relación: `aplica_a`
- destino: {"id": "Sujeto_entidad_financiera", "type": "Sujeto", "label": "Entidades financieras", "properties": {"nivel": "clase", "alias": ["Entidades financieras emisoras de tarjetas de crédito y/o compra", "Entidad financiera emisora de tarjetas de crédito y/o compra"]}, "procedencia": {"chunk_id": "ri_esd::Sbloque1::chapeau_seccion", "punto": "Sbloque1", "rol_documental": "bloque_chapeau_seccion", "paginas": [1, 2]}}
- arista: {"properties": {}, "sujeto_mencion": "las entidades participantes", "mencion_verificada": "exacta", "metodo_resolucion": "R4_sugerencia_modelo", "sujeto_id_modelo": "Sujeto_entidad_financiera", "procedencia": {"chunk_id": "seggar::5.1.5", "punto": "5.1.5", "rol_documental": "punto_propio", "paginas": [4]}}

## 18. `Obligacion_la_accion_de_destruccion_del_dfe_debera_estar_debidamente_registrada_y_formaliza_cbaf01 | regula | Operacion_destruccion_permanente_de_dfe__consyr_1_4_2_6_673c6b` — NG:sin_raiz · observacion:12

Texto que vio E3 de `consyr::1.4.2.6` (e0, bloque de lista True; págs. 5):

```
[encabezado | punto S1]
1. Instrumentación de documentos.
[encabezado | punto 1.4]
1.4. Requisitos de seguridad de la información.
[intro | punto 1.4.2]
1.4.2. Se deberán satisfacer los siguientes requisitos generales para la protección de los
DFE en cada etapa de su ciclo de vida:
[texto propio | punto 1.4.2.6]
1.4.2.6. Destrucción. Los DFE serán destruidos de forma permanente.
i) La acción de destrucción del DFE deberá estar debidamente registra-
da y formalizada.
ii) Deberá garantizarse la no recuperación parcial o total de los datos
mediante técnicas de borrado seguro.
```

Versión: final (grafo sin cola).
- origen: {"id": "Obligacion_la_accion_de_destruccion_del_dfe_debera_estar_debidamente_registrada_y_formaliza_cbaf01", "type": "Obligacion", "label": "Registro y formalización de destrucción de DFE", "properties": {"tipo": "presentacion_informativa", "descripcion": "La acción de destrucción del DFE deberá estar debidamente registrada y formalizada"}, "procedencia": {"chunk_id": "consyr::1.4.2.6", "punto": "1.4.2.6", "rol_documental": "punto_propio", "tramo": "La acción de destrucción del DFE deberá estar debidamente registrada y formalizada", "tramo_verificado": "exacta", "paginas": [5]}}
- relación: `regula`
- destino: {"id": "Operacion_destruccion_permanente_de_dfe__consyr_1_4_2_6_673c6b", "type": "Operacion", "label": "Destrucción permanente de DFE", "properties": {"tipo": "Destrucción de documentos financieros electrónicos", "descripcion": "Destrucción permanente de documentos financieros electrónicos (DFE) en el ciclo de vida de su protección"}, "procedencia": {"chunk_id": "consyr::1.4.2.6", "punto": "1.4.2.6", "rol_documental": "punto_propio", "tramo": "Los DFE serán destruidos de forma permanente", "tramo_verificado": "exacta", "paginas": [5]}}
- arista: {"properties": {}, "procedencia": {"chunk_id": "consyr::1.4.2.6", "punto": "1.4.2.6", "rol_documental": "punto_propio", "paginas": [5]}}

## 19. `Obligacion_los_datos_del_beneficiario_final_no_deben_ser_consignados_sino_hasta_el_momento__53b157 | establecida_en | TextoOrdenado_cedin_pdf` — NG:sin_raiz · observacion:12

Texto que vio E3 de `cedin::S14` (e0, bloque de lista True; págs. 17, 18):

```
[texto propio | punto S14]
14. Recomendaciones a los usuarios.
Con la entrega del CEDIN a los suscriptores, las entidades financieras deberán acompañar
un documento que incluya, como mínimo, las siguientes recomendaciones:
- Los datos del beneficiario final no deberán ser consignados sino hasta el momento de
presentación al cobro del CEDIN ante una entidad financiera.
- Los destinos admitidos son: compra de terrenos, lotes o parcelas -urbanas o rurales-,
galpones, locales, oficinas, cocheras y viviendas ya construidas y/o la construcción de
nuevas viviendas y/o la refacción, ampliación y mejora de inmuebles y/o adquisición de
materiales para la construcción cuando se trate de una refacción, ampliación o mejora. A
esos efectos, se deberá presentar ante la entidad financiera en el momento de la opera-
ción la documentación respaldatoria.
- El CEDIN podrá transmitirse entre endosante y endosatario mediante endoso no sujeto a
condición alguna, practicado al dorso del documento, con firma del endosante y aclara-
ción de su identidad (nombre y apellido o razón social), domicilio y datos de identificación
tributaria (CUIT/CUIL/CDI). No se admitirán agregados de ningún tipo al cuerpo del certi-
ficado.
- El estado de situación de un certificado de inversión, así como los datos en él ingresados
y su habilitación para el cobro, se verificarán en las entidades financieras.
- Cuando el CEDIN se aplique a alguno de los destinos admitidos -operación que sólo
puede realizarse en una entidad financiera-, tal situación quedará identificada por la enti-
dad interviniente en el dorso del documento con la leyenda “APLICADO” y en el sistema
del BCRA, pudiendo ser cobrado por ese endosatario o seguir siendo transmitido vía en-
doso.
- Los CEDIN pueden ser canjeados por otros de menor denominación.
- La normativa sobre CEDIN podrá ser consultada en la página web del Banco Central:
www.bcra.gob.ar.
- En caso de extravío, sustracción o destrucción del CEDIN, el tenedor desposeído comu-
nicará de inmediato lo sucedido en cualquier casa de una entidad financiera, mediante
nota recibida formalmente. Entre otros elementos, la notificación deberá contener el im-
porte, número y serie del CEDIN, descripción de las circunstancias de adquisición del
CEDIN así como de su extravío, sustracción o destrucción –según corresponda– y
acreditación fehaciente de la denuncia pertinente, efectuada ante la autoridad
competente, pudiendo recurrir al procedimiento previsto en el Capítulo XI del Decreto Ley
5965/63.
- Conforme a lo previsto por el art. 9° de la Ley 26.860 “estarán exentos del Impuesto so-
bre los Créditos y Débitos en Cuentas Bancarias y Otras Operatorias, los hechos imponi-
bles originados en la transferencia de la moneda extranjera que se exteriorice, así como
también los que pudieran corresponder a su depósito y extracción de las respectivas
cuentas bancarias, previstas en los artículos 4° y 7°” de esa ley.
```

Versión: final (grafo sin cola).
- origen: {"id": "Obligacion_los_datos_del_beneficiario_final_no_deben_ser_consignados_sino_hasta_el_momento__53b157", "type": "Obligacion", "label": "No consignar datos beneficiario hasta presentación al cobro", "properties": {"descripcion": "Los datos del beneficiario final no deben ser consignados sino hasta el momento de presentación al cobro del CEDIN ante una entidad financiera", "tipo": "otra"}, "procedencia": {"chunk_id": "cedin::S14", "punto": "S14", "rol_documental": "punto_propio", "tramo": "Los datos del beneficiario final no deberán ser consignados sino hasta el momento de presentación al cobro del CEDIN ante una entidad financiera", "tramo_verificado": "exacta", "paginas": [17, 18]}}
- relación: `establecida_en`
- destino: {"id": "TextoOrdenado_cedin_pdf", "type": "TextoOrdenado", "label": "Texto Ordenado CEDIN", "properties": {"archivo": "cedin.pdf", "materia": "Certificados de depósitos para la inversión", "version": "Comunicación A 8131 (vigencia 13/11/2024)"}, "procedencia": {"chunk_id": "cedin::1.1", "punto": "1.1", "rol_documental": "punto_propio", "paginas": [3]}}
- arista: {"properties": {}, "procedencia": {"chunk_id": "cedin::S14", "punto": "S14", "rol_documental": "punto_propio", "paginas": [17, 18]}}

## 20. `Obligacion_debera_garantizarse_la_no_recuperacion_parcial_o_total_de_los_datos_mediante_tec_9f894b | regula | Operacion_destruccion_permanente_de_dfe__consyr_1_4_2_6_673c6b` — NG:sin_raiz · observacion:12

Texto que vio E3 de `consyr::1.4.2.6` (e0, bloque de lista True; págs. 5):

```
[encabezado | punto S1]
1. Instrumentación de documentos.
[encabezado | punto 1.4]
1.4. Requisitos de seguridad de la información.
[intro | punto 1.4.2]
1.4.2. Se deberán satisfacer los siguientes requisitos generales para la protección de los
DFE en cada etapa de su ciclo de vida:
[texto propio | punto 1.4.2.6]
1.4.2.6. Destrucción. Los DFE serán destruidos de forma permanente.
i) La acción de destrucción del DFE deberá estar debidamente registra-
da y formalizada.
ii) Deberá garantizarse la no recuperación parcial o total de los datos
mediante técnicas de borrado seguro.
```

Versión: final (grafo sin cola).
- origen: {"id": "Obligacion_debera_garantizarse_la_no_recuperacion_parcial_o_total_de_los_datos_mediante_tec_9f894b", "type": "Obligacion", "label": "Garantía de no recuperación de datos mediante borrado seguro", "properties": {"tipo": "otra", "descripcion": "Deberá garantizarse la no recuperación parcial o total de los datos mediante técnicas de borrado seguro"}, "procedencia": {"chunk_id": "consyr::1.4.2.6", "punto": "1.4.2.6", "rol_documental": "punto_propio", "tramo": "Deberá garantizarse la no recuperación parcial o total de los datos mediante técnicas de borrado seguro", "tramo_verificado": "exacta", "paginas": [5]}}
- relación: `regula`
- destino: {"id": "Operacion_destruccion_permanente_de_dfe__consyr_1_4_2_6_673c6b", "type": "Operacion", "label": "Destrucción permanente de DFE", "properties": {"tipo": "Destrucción de documentos financieros electrónicos", "descripcion": "Destrucción permanente de documentos financieros electrónicos (DFE) en el ciclo de vida de su protección"}, "procedencia": {"chunk_id": "consyr::1.4.2.6", "punto": "1.4.2.6", "rol_documental": "punto_propio", "tramo": "Los DFE serán destruidos de forma permanente", "tramo_verificado": "exacta", "paginas": [5]}}
- arista: {"properties": {}, "procedencia": {"chunk_id": "consyr::1.4.2.6", "punto": "1.4.2.6", "rol_documental": "punto_propio", "paginas": [5]}}

## 21. `Obligacion_actuar_conforme_a_sus_competencias_con_el_debido_cuidado_y_diligencia_propia_de__61a7a1 | establecida_en | TextoOrdenado_autenf_pdf` — NG:resto · observacion:12

Texto que vio E3 de `autenf::3.2.2` (e0, bloque de lista True; págs. 11):

```
[encabezado | punto S3]
Sección 3. Antecedentes.
[encabezado | punto 3.2]
3.2. Principios y estándares de conducta.
[intro | punto 3.2]
A efectos de la evaluación prevista en estas normas y del posterior desempeño de los miem-
bros del órgano de administración (directores, consejeros o autoridades equivalentes) en la
entidad o que integran su Alta Gerencia –conforme a lo establecido en el punto 1.5. de las
normas sobre “Lineamientos para el gobierno societario en entidades financieras”–, se ten-
drán en consideración los principios y/o estándares de conducta establecidos en dichas nor-
mas y los que se enumeran a continuación:
[texto propio | punto 3.2.2]
3.2.2. La actuación conforme a sus competencias, con el debido cuidado y diligencia propia
de la actividad profesional.
```

Versión: final (grafo sin cola).
- origen: {"id": "Obligacion_actuar_conforme_a_sus_competencias_con_el_debido_cuidado_y_diligencia_propia_de__61a7a1", "type": "Obligacion", "label": "Actuación conforme a competencias con debido cuidado", "properties": {"descripcion": "Actuar conforme a sus competencias, con el debido cuidado y diligencia propia de la actividad profesional", "tipo": "otra"}, "procedencia": {"chunk_id": "autenf::3.2.2", "punto": "3.2.2", "rol_documental": "punto_propio", "tramo": "La actuación conforme a sus competencias, con el debido cuidado y diligencia propia de la actividad profesional", "tramo_verificado": "exacta", "paginas": [11]}}
- relación: `establecida_en`
- destino: {"id": "TextoOrdenado_autenf_pdf", "type": "TextoOrdenado", "label": "Autoridades de entidades financieras", "properties": {"archivo": "autenf.pdf", "materia": "Autoridades de entidades financieras", "version": "Comunicación A 8383 (vigencia 01/01/2026)"}, "procedencia": {"chunk_id": "autenf::1.1::intro", "punto": "1.1", "rol_documental": "bloque_intro", "paginas": [4]}}
- arista: {"properties": {}, "procedencia": {"chunk_id": "autenf::3.2.2", "punto": "3.2.2", "rol_documental": "punto_propio", "paginas": [11]}}

## 22. `Condicion_condicion_incumplimiento_durante_tres_meses_consecutivos_o_cuatro_alternados__el_5ead55 | establecida_en | TextoOrdenado_finsec_pdf` — NG:resto · observacion:12

Texto que vio E3 de `finsec::7.3.1` (e0, bloque de lista True; págs. 31, 32):

```
[encabezado | punto S7]
Sección 7. Incumplimientos.
[encabezado | punto 7.3]
7.3. Planes de regularización y saneamiento.
[texto propio | punto 7.3.1]
7.3.1. Exigencia de la presentación.
i) La entidad que incurra en incumplimientos de los límites máximos individuales respec-
to de un mismo cliente o de los globales durante tres meses consecutivos o cuatro al-
ternados, en un lapso de doce meses consecutivos, deberá presentar un plan de regu-
larización y saneamiento –salvo que le sea requerido previamente por la SEFyC– de-
ntro de los 30 días corridos siguientes al mes en que se haya producido el apartamien-
to que determine esa obligación, basado en el aumento de la RPC o en la eliminación
de los excesos registrados.
i) En caso de que la SEFyC formule observaciones al plan presentado, la entidad deberá
ajustarlo conforme a ellas dentro de los diez días corridos siguientes al de la notifica-
ción.
ii)La falta de presentación del plan dentro de los términos fijados, su rechazo o incum-
plimiento, dará lugar a la aplicación de las disposiciones previstas en las normas sobre
“Régimen disciplinario a cargo del Banco Central de la República Argentina (Leyes
21.526 y 25.065) y tramitación de sumarios cambiarios (Ley 19.359)”.
```

Versión: final (grafo sin cola).
- origen: {"id": "Condicion_condicion_incumplimiento_durante_tres_meses_consecutivos_o_cuatro_alternados__el_5ead55", "type": "Condicion", "label": "Condición: incumplimiento durante tres meses consecutivos o cuatro alternados", "properties": {"descripcion": "El incumplimiento de los límites debe verificarse durante tres meses consecutivos o cuatro alternados dentro de un lapso de doce meses consecutivos", "umbrales": [{"tramo": "durante tres meses consecutivos o cuatro alternados, en un lapso de doce meses consecutivos", "valor": "3", "unidad": "meses", "comparacion": "no_determinada", "regla_comparacion": "sin_marcador_plazo", "origen": "e1", "tramo_verificado": "exacta"}, {"tramo": "durante tres meses consecutivos o cuatro alternados, en un lapso de doce meses consecutivos", "valor": "12", "unidad": "meses", "comparacion": "no_determinada", "regla_comparacion": "sin_marcador_plazo", "origen": "e1", "tramo_verificado": "exacta"}]}, "procedencia": {"chunk_id": "finsec::7.3.1", "punto": "7.3.1", "rol_documental": "punto_propio", "tramo": "durante tres meses consecutivos o cuatro alternados, en un lapso de doce meses consecutivos", "tramo_verificado": "exacta", "paginas": [31, 32]}}
- relación: `establecida_en`
- destino: {"id": "TextoOrdenado_finsec_pdf", "type": "TextoOrdenado", "label": "Texto Ordenado Sector Público No Financiero", "properties": {"archivo": "finsec.pdf", "materia": "Financiamiento al sector público no financiero", "version": "Comunicación A 8435 (vigencia 17/04/2026)"}, "procedencia": {"chunk_id": "finsec::1.1", "punto": "1.1", "rol_documental": "punto_propio", "paginas": [3]}}
- arista: {"properties": {}, "procedencia": {"chunk_id": "finsec::7.3.1", "punto": "7.3.1", "rol_documental": "punto_propio", "paginas": [31, 32]}}

## 23. `Condicion_agotamiento_de_activos_elegibles_disponibles__las_entidades_financieras_solicita_beddd5 | establecida_en | TextoOrdenado_venliq_pdf` — NG:resto · observacion:12

Texto que vio E3 de `venliq::1.1.2` (e0, bloque de lista True; págs. 3):

```
[encabezado | punto S1]
Sección 1. Aspectos generales.
[encabezado | punto 1.1]
1.1. Condiciones generales.
[texto propio | punto 1.1.2]
1.1.2. El acceso a esta operatoria estará supeditado a que previamente las entidades
financieras solicitantes hayan agotado sus tenencias de activos elegibles disponibles
para operaciones de pase con esta Institución o que éstas se encuentren
comprometidas en otras operatorias, debiendo presentar la nota del punto 2.1. de la
Sección 2.
```

Versión: final (grafo sin cola).
- origen: {"id": "Condicion_agotamiento_de_activos_elegibles_disponibles__las_entidades_financieras_solicita_beddd5", "type": "Condicion", "label": "Agotamiento de activos elegibles disponibles", "properties": {"descripcion": "Las entidades financieras solicitantes deben haber agotado previamente sus tenencias de activos elegibles disponibles para operaciones de pase con esta Institución."}, "procedencia": {"chunk_id": "venliq::1.1.2", "punto": "1.1.2", "rol_documental": "punto_propio", "tramo": "que previamente las entidades financieras solicitantes hayan agotado sus tenencias de activos elegibles disponibles para operaciones de pase con esta Institución", "tramo_verificado": "exacta", "paginas": [3]}}
- relación: `establecida_en`
- destino: {"id": "TextoOrdenado_venliq_pdf", "type": "TextoOrdenado", "label": "Texto Ordenado Venta de Liquidez", "properties": {"archivo": "venliq.pdf", "materia": "Ventanilla de liquidez del BCRA", "version": "Comunicación A 6130 (vigencia 23/12/2016)"}, "procedencia": {"chunk_id": "venliq::1.1.1", "punto": "1.1.1", "rol_documental": "punto_propio", "paginas": [3]}}
- arista: {"properties": {}, "procedencia": {"chunk_id": "venliq::1.1.2", "punto": "1.1.2", "rol_documental": "punto_propio", "paginas": [3]}}

## 24. `Obligacion_el_titular_debe_proceder_de_igual_forma_dar_aviso_por_escrito_cuando_tenga_conoc_b2581c | aplica_a | Sujeto_propuesto_el_titular` — NG:resto · observacion:12

Texto que vio E3 de `ctavis::1.5.1.4` (e0, bloque de lista True; págs. 8):

```
[encabezado | punto S1]
Sección 1. Funcionamiento.
[encabezado | punto 1.5]
1.5. Aspectos del funcionamiento a incluir en el contrato de cuentas a la vista.
[encabezado | punto 1.5.1]
1.5.1. Obligaciones del titular.
[texto propio | punto 1.5.1.4]
1.5.1.4. Dar aviso a la caja de crédito cooperativa, por escrito, del extravío, sustracción o
adulteración de las fórmulas de letras de cambio en blanco o de letras de cambio
giradas y no entregadas a terceros o de la fórmula especial para pedirlos, según
el procedimiento establecido en el punto 6.2.
Deberá proceder de igual forma cuando tuviese conocimiento de que una letra
de cambio ya emitida hubiera sido extraviada, sustraída o alterada. El aviso tam-
bién puede darlo el tenedor desposeído.
```

Versión: final (grafo sin cola).
- origen: {"id": "Obligacion_el_titular_debe_proceder_de_igual_forma_dar_aviso_por_escrito_cuando_tenga_conoc_b2581c", "type": "Obligacion", "label": "Obligación de aviso de letra emitida extraviada o alterada", "properties": {"tipo": "comunicacion_a_cliente", "descripcion": "El titular debe proceder de igual forma (dar aviso por escrito) cuando tenga conocimiento de que una letra de cambio ya emitida hubiera sido extraviada, sustraída o alterada"}, "procedencia": {"chunk_id": "ctavis::1.5.1.4", "punto": "1.5.1.4", "rol_documental": "punto_propio", "tramo": "Deberá proceder de igual forma cuando tuviese conocimiento de que una letra de cambio ya emitida hubiera sido extraviada, sustraída o alterada", "tramo_verificado": "exacta", "paginas": [8]}}
- relación: `aplica_a`
- destino: {"id": "Sujeto_propuesto_el_titular", "type": "Sujeto", "label": "el titular", "properties": {"nivel": "propuesto", "cuarentena": "true", "padre_sugerido": "Sujeto_cliente"}, "procedencia": {"chunk_id": "ctavis::1.5.1.2", "punto": "1.5.1.2", "rol_documental": "punto_propio", "paginas": [8]}}
- arista: {"properties": {}, "sujeto_mencion": "el titular", "mencion_verificada": "exacta", "metodo_resolucion": "cuarentena", "procedencia": {"chunk_id": "ctavis::1.5.1.4", "punto": "1.5.1.4", "rol_documental": "punto_propio", "paginas": [8]}}

## 25. `Obligacion_al_inscribirse_en_el_padron_las_entidades_financieras_obligadas_deberan_indicar__1a1052 | aplica_a | Sujeto_entidad_financiera` — NG:resto · observacion:12

Texto que vio E3 de `depinv::3.9.2` (e0, bloque de lista True; págs. 32):

```
[encabezado | punto S3]
Sección 3. Disposiciones generales.
[encabezado | punto 3.9]
3.9. Procedimientos especiales de identificación de clientes en materia de cooperación tributaria
internacional.
[texto propio | punto 3.9.2]
3.9.2. Padrón de entidades financieras obligadas a reportar información para la cooperación tri-
butaria internacional.
Las entidades financieras obligadas (conforme a los términos del Estándar citado en el
punto 3.9.1. y de las disposiciones de la ARCA), deberán inscribirse en el “Padrón de en-
tidades financieras obligadas a reportar información para la cooperación tributaria inter-
nacional”.
Cuando se inscriban las entidades deberán indicar: i) código de la entidad financiera; ii)
su situación –obligada/no obligada–; iii) si registran cuentas declarables en pesos y/o en
moneda extranjera en el período a informar (definidas en la Resolución General de la ex
AFIP 4056/17 y modificatorias) y, en caso afirmativo, iv) cantidad de cuentas declarables
y v) porcentaje de esas cuentas que corresponden a personas humanas o a personas ju-
rídicas residentes en una jurisdicción extranjera.
La información declarada conforme a lo establecido precedentemente tendrá carácter de
declaración jurada y deberá ser actualizada por parte de la entidad en el mes de diciem-
bre de cada año.
```

Versión: final (grafo sin cola).
- origen: {"id": "Obligacion_al_inscribirse_en_el_padron_las_entidades_financieras_obligadas_deberan_indicar__1a1052", "type": "Obligacion", "label": "Indicar código, situación y cuentas declarables", "properties": {"tipo": "presentacion_informativa", "descripcion": "Al inscribirse en el Padrón, las entidades financieras obligadas deberán indicar: i) código de la entidad financiera; ii) su situación (obligada/no obligada); iii) si registran cuentas declarables en pesos y/o en moneda extranjera en el período a informar (conforme a la Resolución General de la ex AFIP 4056/17 y modificatorias); y en caso afirmativo, iv) cantidad de cuentas declarables y v) porcentaje de esas cuentas que corresponden a personas humanas o a personas jurídicas residentes en una jurisdicción extranjera."}, "procedencia": {"chunk_id": "depinv::3.9.2", "punto": "3.9.2", "rol_documental": "punto_propio", "tramo": "Cuando se inscriban las entidades deberán indicar: i) código de la entidad financiera; ii) su situación –obligada/no obligada–; iii) si registran cuentas declarables en pesos y/o en moneda extranjera en el período a informar (definidas en la Resolución General de la ex AFIP 4056/17 y modificatorias) y, en ca…
- relación: `aplica_a`
- destino: {"id": "Sujeto_entidad_financiera", "type": "Sujeto", "label": "Entidades financieras", "properties": {"nivel": "clase", "alias": ["Entidades financieras emisoras de tarjetas de crédito y/o compra", "Entidad financiera emisora de tarjetas de crédito y/o compra"]}, "procedencia": {"chunk_id": "ri_esd::Sbloque1::chapeau_seccion", "punto": "Sbloque1", "rol_documental": "bloque_chapeau_seccion", "paginas": [1, 2]}}
- arista: {"properties": {}, "sujeto_mencion": "las entidades", "mencion_verificada": "exacta", "metodo_resolucion": "R4_sugerencia_modelo", "sujeto_id_modelo": "Sujeto_entidad_financiera", "procedencia": {"chunk_id": "depinv::3.9.2", "punto": "3.9.2", "rol_documental": "punto_propio", "paginas": [32]}}

## 26. `Condicion_agente_sin_garantias_otorgadas_a_ninguna_parte__la_entidad_financiera_actua_como_f01456 | condicion_de | Excepcion_la_entidad_no_esta_expuesta_a_la_operacion_sft_y_por_lo_tanto_no_debe_computarla_899767` — NG:resto · observacion:12

Texto que vio E3 de `raapal::2.2.3.2` (e0, bloque de lista True; págs. 14, 15):

```
[encabezado | punto S2]
Sección 2. Medida de la exposición.
[encabezado | punto 2.2]
2.2. Criterios particulares.
[encabezado | punto 2.2.3]
2.2.3. Exposiciones por operaciones de financiación con valores (SFT).
[texto propio | punto 2.2.3.2]
2.2.3.2. Tratamiento especial aplicable en los casos en que la entidad actúe por cuenta
de terceros.
Cuando la entidad financiera sea agente y su exposición a la operación se limite
a garantizar a su cliente la diferencia entre el valor de los títulos o el efectivo
prestados por su cliente y el valor de la garantía recibida de su contraparte po-
drá calcular su medida de la exposición aplicando sólo el acápite ii) del punto
2.2.3.1. Si su exposición fuera mayor –tal como sería el caso si la entidad finan-
ciera administra por cuenta propia la garantía recibida o ésta no está segregada
de sus activos–, deberá incluir el total del título o del efectivo en su medida de la
exposición.
En cambio, si la entidad financiera que actúa en calidad de agente, además de
reunir las condiciones anteriores, no ha otorgado garantías a ninguna de las par-
tes intervinientes, no está expuesta a la SFT y, por lo tanto, no la deberá compu-
tar en su medida de la exposición.
Si la entidad en su calidad de agente garantiza a las dos partes de una SFT, de-
berá calcular su medida de la exposición de acuerdo con lo expuesto en este
punto para cada una de ellas, en forma separada.
```

Versión: final (grafo sin cola).
- origen: {"id": "Condicion_agente_sin_garantias_otorgadas_a_ninguna_parte__la_entidad_financiera_actua_como_f01456", "type": "Condicion", "label": "Agente sin garantías otorgadas a ninguna parte", "properties": {"descripcion": "La entidad financiera actúa como agente, reúne las condiciones anteriores y no ha otorgado garantías a ninguna de las partes intervinientes"}, "procedencia": {"chunk_id": "raapal::2.2.3.2", "punto": "2.2.3.2", "rol_documental": "punto_propio", "tramo": "si la entidad financiera que actúa en calidad de agente, además de reunir las condiciones anteriores, no ha otorgado garantías a ninguna de las partes intervinientes", "tramo_verificado": "exacta", "paginas": [14, 15]}}
- relación: `condicion_de`
- destino: {"id": "Excepcion_la_entidad_no_esta_expuesta_a_la_operacion_sft_y_por_lo_tanto_no_debe_computarla_899767", "type": "Excepcion", "label": "Excepción — no computar SFT si agente sin garantías", "properties": {"descripcion": "La entidad no está expuesta a la operación SFT y, por lo tanto, no debe computarla en su medida de exposición"}, "procedencia": {"chunk_id": "raapal::2.2.3.2", "punto": "2.2.3.2", "rol_documental": "punto_propio", "tramo": "no está expuesta a la SFT y, por lo tanto, no la deberá computar en su medida de la exposición", "tramo_verificado": "exacta", "paginas": [14, 15]}}
- arista: {"properties": {}, "procedencia": {"chunk_id": "raapal::2.2.3.2", "punto": "2.2.3.2", "rol_documental": "punto_propio", "paginas": [14, 15]}}

## 27. `Obligacion_debera_designarse_por_lo_menos_un_representante_suplente_para_sustituir_al_titul_1c4b87 | establecida_en | TextoOrdenado_repefe_pdf` — NG:resto · observacion:12

Texto que vio E3 de `repefe::1.2.1` (e0, bloque de lista True; págs. 3):

```
[encabezado | punto S1]
Sección 1. Actividad.
[encabezado | punto 1.2]
1.2. Funciones.
[texto propio | punto 1.2.1]
1.2.1. Las funciones del representante son indelegables. Consecuentemente, deberá
designarse por lo menos un representante suplente para sustituir al titular en caso de
vacancia transitoria asumiendo las responsabilidades propias de la función mientras
dure la suplencia.
```

Versión: final (grafo sin cola).
- origen: {"id": "Obligacion_debera_designarse_por_lo_menos_un_representante_suplente_para_sustituir_al_titul_1c4b87", "type": "Obligacion", "label": "Designar representante suplente", "properties": {"tipo": "otra", "descripcion": "Deberá designarse por lo menos un representante suplente para sustituir al titular en caso de vacancia transitoria, asumiendo las responsabilidades propias de la función mientras dure la suplencia"}, "procedencia": {"chunk_id": "repefe::1.2.1", "punto": "1.2.1", "rol_documental": "punto_propio", "tramo": "deberá designarse por lo menos un representante suplente para sustituir al titular en caso de vacancia transitoria asumiendo las responsabilidades propias de la función mientras dure la suplencia", "tramo_verificado": "exacta", "paginas": [3]}}
- relación: `establecida_en`
- destino: {"id": "TextoOrdenado_repefe_pdf", "type": "TextoOrdenado", "label": "Representantes de entidades financieras del exterior", "properties": {"archivo": "repefe.pdf", "materia": "Representantes de entidades financieras del exterior no autorizadas para operar  en el país", "version": "Comunicación A 6462 (vigencia 01/03/2018)"}, "procedencia": {"chunk_id": "repefe::1.1", "punto": "1.1", "rol_documental": "punto_propio", "paginas": [3]}}
- arista: {"properties": {}, "procedencia": {"chunk_id": "repefe::1.2.1", "punto": "1.2.1", "rol_documental": "punto_propio", "paginas": [3]}}

## 28. `Restriccion_el_importe_de_la_inversion_a_plazo_no_podra_superar_2_veces_el_valor_total_de_la_5ca7b6 | aplica_a | Sujeto_persona_humana` — NG:resto · observacion:12

Texto que vio E3 de `depinv::2.5.2.2` (e0, bloque de lista True; págs. 20):

```
[encabezado | punto S2]
Sección 2. Inversiones a plazo.
[encabezado | punto 2.5]
2.5. A plazo con retribución variable.
[encabezado | punto 2.5.2]
2.5.2. Titulares.
[texto propio | punto 2.5.2.2]
2.5.2.2. Personas –humanas o jurídicas– con actividad agrícola.
Podrán efectuar inversiones a plazo con retribución variable con rendimiento de-
terminado en función del valor de los cereales u oleaginosas previstos en el pun-
to 2.5.6.4. y de la cotización del dólar estadounidense –punto 2.5.6.6.–, por un
importe de hasta 2 veces el valor total de sus ventas de cereales y/u oleaginosas
registradas a partir del 1.1.22.
Se admitirá la renovación de esas inversiones a plazo existentes al 23.6.22 por
hasta el monto a cobrar a sus vencimientos sin tener en cuenta el límite previsto
en el párrafo precedente.
```

Versión: final (grafo sin cola).
- origen: {"id": "Restriccion_el_importe_de_la_inversion_a_plazo_no_podra_superar_2_veces_el_valor_total_de_la_5ca7b6", "type": "Restriccion", "label": "Tope 2 veces ventas — inversión a plazo cereales/oleaginosas", "properties": {"tipo": "limite_cuantitativo", "descripcion": "El importe de la inversión a plazo no podrá superar 2 veces el valor total de las ventas de cereales y/u oleaginosas registradas a partir del 1.1.22", "umbrales": [{"tramo": "hasta 2 veces el valor total de sus ventas de cereales y/u oleaginosas registradas a partir del 1.1.22", "valor": "2", "unidad": "veces", "comparacion": "maximo_inclusivo", "base": "valor total de sus ventas de cereales y/u oleaginosas registradas a partir del 1.1.22", "regla_comparacion": "compuesta:hasta", "origen": "e1", "tramo_verificado": "exacta", "base_no_resuelta": true}]}, "procedencia": {"chunk_id": "depinv::2.5.2.2", "punto": "2.5.2.2", "rol_documental": "punto_propio", "tramo": "por un importe de hasta 2 veces el valor total de sus ventas de cereales y/u oleaginosas registradas a partir del 1.1.22", "tramo_verificado": "exacta", "paginas": [20]}}
- relación: `aplica_a`
- destino: {"id": "Sujeto_persona_humana", "type": "Sujeto", "label": "Personas humanas", "properties": {"nivel": "clase"}, "procedencia": {"chunk_id": "lavdin::1.3.1.1", "punto": "1.3.1.1", "rol_documental": "punto_propio", "paginas": [4]}}
- arista: {"properties": {}, "sujeto_mencion": "Personas –humanas o jurídicas– con actividad agrícola", "mencion_verificada": "exacta", "metodo_resolucion": "R4_sugerencia_modelo", "sujeto_id_modelo": "Sujeto_persona_humana", "procedencia": {"chunk_id": "depinv::2.5.2.2", "punto": "2.5.2.2", "rol_documental": "punto_propio", "paginas": [20]}}

## 29. `Condicion_evaluacion_capacidad_pago_sobre_documentacion_ingresos__cuando_la_evaluacion_de__993dba | condicion_de | Obligacion_aun_cuando_se_utilicen_en_forma_complementaria_los_metodos_de_screening_o_credit_c540ad` — NG:resto · observacion:12

Texto que vio E3 de `gescre::1.1.3.3` (e0, bloque de lista True; págs. 6, 7, 8, 9):

```
[encabezado | punto S1]
Sección 1. Requisitos para el otorgamiento de financiaciones.
[encabezado | punto 1.1]
1.1. Legajo del cliente.
[encabezado | punto 1.1.3]
1.1.3. Contenido.
[texto propio | punto 1.1.3.3]
1.1.3.3. Operatorias especiales.
a) De monto reducido.
Sólo será exigible que el legajo cuente con los datos que permitan la identifi-
cación del cliente, de acuerdo con las normas sobre “Documentos de identifi-
cación en vigencia”.
i) Prestatarios.
Personas humanas no vinculadas a la entidad financiera, en la medida en
que no hayan recibido financiación en los términos previstos en el punto
1.1.3.4., inciso a).
ii) Límite individual.
El capital adeudado en ningún momento podrá superar el importe equiva-
lente a 8 (ocho) veces el Salario Mínimo, Vital y Móvil establecido por el
Consejo Nacional del Empleo, la Productividad y el Salario Mínimo, Vital y
Móvil para los trabajadores mensualizados que cumplan la jornada legal
completa de trabajo por cliente, bajo la modalidad de sistema francés o
alemán.
iii) Límite global de la cartera.
20 % de la responsabilidad patrimonial computable (RPC) de la entidad del
mes anterior al que corresponda. Dicho límite será computable a los efec-
tos de calcular el límite global previsto en el punto 1.1.3.4., inciso a), acápi-
te iii), para el caso que la entidad también haya otorgado financiaciones
bajo esa modalidad (préstamos para microemprendedores).
iv)Periodicidad máxima de la cuota.
La frecuencia del pago de la cuota no podrá ser por un mayor período del
mensual.
v) Clasificación del cliente e información a la “Central de deudores del siste-
ma financiero”.
Se efectuará sobre la base de las pautas objetivas según lo establecido en la
Sección 7. de las normas sobre "Clasificación de deudores".
Asimismo, se incorporarán los datos que la entidad financiera, a su criterio,
estime necesarios para su evaluación crediticia.
El otorgamiento de este tipo de asistencia no obsta a que, en el caso de que
se concedan al mismo prestatario otras facilidades crediticias, deban obser-
varse las disposiciones en materia de contenido del legajo de crédito estable-
cidas en el punto 1.1.3.1.
b) Asignación mediante métodos específicos de evaluación (sistemas de “scree-
ning” y modelos de “credit scoring”) para decidir sobre el otorgamiento de los
créditos a que se refiere el acápite ii).
Se entiende por sistemas de “screening” al conjunto de pasos y reglas de de-
cisión que recogen la experiencia acumulada en el otorgamiento de créditos,
el seguimiento de su comportamiento posterior y la política de créditos de la
entidad.
Este método deberá aplicarse de forma sistemática y actualizarse de manera
periódica, a fin de extraer conclusiones en relación con el otorgamiento de
créditos y asignar márgenes de financiación.
Por otra parte, los modelos de “credit scoring” son métodos matemáticos o es-
tadísticos-econométricos empleados para medir el riesgo y/o la probabilidad
de incumplimiento de los solicitantes de crédito.
Ambas técnicas, deben basarse en las variables que las entidades financieras
consideren relevantes para medir el riesgo de incobrabilidad asociado a cada
deudor y clase de crédito, pudiendo emplear el mismo tipo de información.
La metodología e información que se empleen para sustituir la demostración
de ingresos mediante documentación específica deberá asegurar que la eva-
luación de la capacidad de repago esté incorporada en el resultado del
“screening” o “credit scoring” empleado a los efectos de inferir el comporta-
miento crediticio (probabilidad de repago de las obligaciones en el futuro).
Asimismo, las citadas metodologías deben permitir estimar el nivel de ingre-
sos del cliente.
Adicionalmente, en ambos casos, deberá efectuarse el cotejo de las predic-
ciones realizadas con el comportamiento crediticio finalmente observado, a los
fines de adoptar, en su caso, las adecuaciones que se estimen pertinentes.
Deberán observarse las siguientes condiciones:
i) Prestatarios alcanzados: personas humanas y jurídicas, no vinculadas a la
entidad financiera.
ii) Límite individual.
− Para personas humanas la relación cuota/ingreso estimado no deberá
superar el 50 %.
A los efectos de la verificación de la relación máxima prevista prece-
dentemente, se deberán tener en cuenta las cuotas de todas las finan-
ciaciones de la entidad financiera que cuenten con amortización perió-
dica, sin considerar las cuotas de créditos de otras entidades.
En consecuencia, los márgenes acordados para los descubiertos en
cuenta corriente y los límites de compra de las tarjetas de crédito –en
ambos casos, tanto el utilizado como el disponible–, así como los prés-
tamos personales preacordados –en la medida en que aún no hayan
sido formalizados ni desembolsados al cliente–, no formarán parte del
numerador de la relación cuota/ingreso estimado por no contar con una
amortización periódica. Sin embargo, deberá considerarse dentro del
concepto “cuotas” aquellas que el cliente tenga por compras financia-
das en el marco del sistema de tarjeta de crédito.
Los ingresos y cuotas a considerar serán los del deudor y/o, en su ca-
so, de los codeudores.
- Para MiPyME y personas jurídicas, no vinculadas a la entidad, el capi-
tal adeudado en ningún momento podrá superar en su conjunto el
equivalente al importe de referencia establecido en el punto 1.9.
iii) Límite global para las financiaciones a MiPyME y personas jurídicas no
vinculadas.
40 % de la RPC de la entidad del mes anterior al que corresponda.
iv) Clasificación del cliente e información a la “Central de deudores del siste-
ma financiero”.
Se efectuará sobre la base de las pautas objetivas según lo establecido en
la Sección 7. de las normas sobre “Clasificación de deudores”.
v) En el legajo del cliente deberá quedar constancia de la evaluación efectua-
da de acuerdo con este procedimiento y, de tratarse de personas humanas,
el ingreso estimado del deudor y/o, en su caso, de los codeudores.
Asimismo, podrá contener otros elementos que la entidad financiera, a su
criterio, estime necesarios para la evaluación crediticia, sin que ello consti-
tuya una condición necesaria para su aplicación.
Las entidades deberán efectuar una descripción pormenorizada del proce-
dimiento adoptado para la evaluación del cliente y la asignación de márge-
nes crediticios discriminados, de corresponder, según la clase de crédito.
vi) Este procedimiento deberá contar con la previa opinión de:
– Funcionario de mayor jerarquía del área de créditos o comercial res-
ponsable de decidir en materia crediticia.
– Gerente General o autoridad equivalente.
– Comité de Créditos, salvo que no exista en la estructura funcional de la
entidad.
Asimismo, será necesario contar con la aprobación del procedimiento se-
ñalado por parte del Directorio, Consejo de Administración o autoridad
equivalente de la entidad financiera.
vii) En los casos en que la evaluación de la capacidad de pago se efectúe di-
rectamente sobre la base de documentación respaldatoria de los ingresos
del prestatario o sea de aplicación lo previsto por el cuarto párrafo del
punto 1.1.3.1., aun cuando se utilicen en forma complementaria los méto-
dos indicados en el presente apartado, deberán observarse las disposi-
ciones en materia de contenido de legajo establecidas en el punto 1.1.3.1.
```

Versión: final (grafo sin cola).
- origen: {"id": "Condicion_evaluacion_capacidad_pago_sobre_documentacion_ingresos__cuando_la_evaluacion_de__993dba", "type": "Condicion", "label": "Evaluación capacidad pago sobre documentación ingresos", "properties": {"descripcion": "Cuando la evaluación de capacidad de pago se efectúe directamente sobre documentación respaldatoria de ingresos del prestatario o sea de aplicación lo previsto en el cuarto párrafo del punto 1.1.3.1."}, "procedencia": {"chunk_id": "gescre::1.1.3.3", "punto": "1.1.3.3", "rol_documental": "punto_propio", "tramo": "En los casos en que la evaluación de la capacidad de pago se efectúe directamente sobre la base de documentación respaldatoria de los ingresos del prestatario o sea de aplicación lo previsto por el cuarto párrafo del punto 1.1.3.1.", "tramo_verificado": "exacta", "paginas": [6, 7, 8, 9]}}
- relación: `condicion_de`
- destino: {"id": "Obligacion_aun_cuando_se_utilicen_en_forma_complementaria_los_metodos_de_screening_o_credit_c540ad", "type": "Obligacion", "label": "Observancia disposiciones legajo (evaluación documentación)", "properties": {"tipo": "otra", "descripcion": "Aun cuando se utilicen en forma complementaria los métodos de screening o credit scoring, deben observarse las disposiciones en materia de contenido de legajo establecidas en el punto 1.1.3.1."}, "procedencia": {"chunk_id": "gescre::1.1.3.3", "punto": "1.1.3.3", "rol_documental": "punto_propio", "tramo": "aun cuando se utilicen en forma complementaria los métodos indicados en el presente apartado, deberán observarse las disposiciones en materia de contenido de legajo establecidas en el punto 1.1.3.1.", "tramo_verificado": "exacta", "paginas": [6, 7, 8, 9]}}
- arista: {"properties": {}, "procedencia": {"chunk_id": "gescre::1.1.3.3", "punto": "1.1.3.3", "rol_documental": "punto_propio", "paginas": [6, 7, 8, 9]}}

## 30. `Condicion_moneda_significativa_pasivos_al_5_o_mas__una_moneda_es_significativa_cuando_los__54b631 | establecida_en | TextoOrdenado_ratio_pdf` — NG:resto · observacion:12

Texto que vio E3 de `ratio::1.7` (e0, bloque de lista True; págs. 7):

```
[encabezado | punto S1]
Sección 1. Consideraciones generales.
[texto propio | punto 1.7]
1.7. Monedas.
El LCR deberá observarse e informarse en moneda nacional, incluyendo la totalidad de los con-
ceptos en moneda extranjera expresados en esa moneda -pesos-.
Sin perjuicio de ello, las entidades financieras deberán cubrir las necesidades de liquidez en ca-
da moneda significativa en la que operen -cuando los pasivos y otras obligaciones en esa mo-
neda representen al menos el 5% del total de pasivos y demás obligaciones de la entidad-, inde-
pendientemente del cumplimiento de lo previsto en el punto 2.1.12. Además, la composición del
FALAC por moneda deberá ser similar a la de las necesidades operativas de la entidad financie-
ra.
```

Versión: final (grafo sin cola).
- origen: {"id": "Condicion_moneda_significativa_pasivos_al_5_o_mas__una_moneda_es_significativa_cuando_los__54b631", "type": "Condicion", "label": "Moneda significativa — pasivos al 5% o más", "properties": {"descripcion": "Una moneda es significativa cuando los pasivos y otras obligaciones en esa moneda representan al menos el 5% del total de pasivos y demás obligaciones de la entidad.", "umbrales": [{"tramo": "al menos el 5% del total de pasivos y demás obligaciones de la entidad", "valor": "5", "unidad": "porcentaje", "comparacion": "minimo_inclusivo", "base": "total de pasivos y demás obligaciones de la entidad", "regla_comparacion": "compuesta:al_menos", "origen": "e1", "tramo_verificado": "exacta", "base_no_resuelta": true}]}, "procedencia": {"chunk_id": "ratio::1.7", "punto": "1.7", "rol_documental": "punto_propio", "tramo": "cuando los pasivos y otras obligaciones en esa moneda representen al menos el 5% del total de pasivos y demás obligaciones de la entidad", "tramo_verificado": "exacta", "paginas": [7]}}
- relación: `establecida_en`
- destino: {"id": "TextoOrdenado_ratio_pdf", "type": "TextoOrdenado", "label": "Ratio de fondeo neto estable", "properties": {"archivo": "ratio.pdf", "materia": "Ratio de cobertura de liquidez", "version": "Comunicación A 8445 (vigencia 05/06/2026)"}, "procedencia": {"chunk_id": "ratio::1.1", "punto": "1.1", "rol_documental": "punto_propio", "paginas": [4]}}
- arista: {"properties": {}, "procedencia": {"chunk_id": "ratio::1.7", "punto": "1.7", "rol_documental": "punto_propio", "paginas": [7]}}

