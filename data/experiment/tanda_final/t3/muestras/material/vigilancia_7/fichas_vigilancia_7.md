# Material de T4 — vigilancia:7 (6 fichas; B6.1, tanda final, T3, punto 7.5)

Sorteo: `vigilancia_7.json` (deb59743…, 2026-10-20T14:08:58-03:00); material armado a las 2026-10-20T14:09:10-03:00. Sin el estado de E3 ni las marcas de E3.

## 1. `Sujeto_rol_alcance_snp_tr_nc | ejecuta | Operacion_suspension_preventiva_de_procedimientos_y_operatoria__snp_tr_nc_1_5_5_8_1cb77e` — RI:sin_raiz · vigilancia:7

Texto que vio E3 (e0, bloque de lista True; págs. 9):

```
[encabezado | punto S1]
Sección 1. Transferencias electrónicas de fondos. Conceptos básicos
[encabezado | punto 1.5]
1.5. Responsabilidades generales de los participantes
[encabezado | punto 1.5.5]
1.5.5. Administrador de un esquema de transferencias electrónicas de fondos
[texto propio | punto 1.5.5.8]
1.5.5.8. Suspender preventivamente, cuando así lo disponga el Directorio del BCRA,
cualquier procedimiento, operatoria, y/o regla comercial del esquema de pago
bajo su administración en situaciones en las que se encuentre gravemente
comprometida la estabilidad, la seguridad y/o la eficiencia para las transferen-
cias electrónicas de fondos.
```

Versión: final (grafo sin cola).
- origen: {"id": "Sujeto_rol_alcance_snp_tr_nc", "type": "Sujeto", "label": "Sujetos alcanzados (SNP - Transferencias - Normas complementarias)", "properties": {"nivel": "rol"}, "procedencia": {"chunk_id": "ri_iesinap::S1", "punto": "S1", "rol_documental": "punto_propio", "paginas": [1]}}
- relación: `ejecuta`
- destino: {"id": "Operacion_suspension_preventiva_de_procedimientos_y_operatoria__snp_tr_nc_1_5_5_8_1cb77e", "type": "Operacion", "label": "Suspensión preventiva de procedimientos y operatoria", "properties": {"tipo": "Suspensión preventiva", "descripcion": "Suspensión preventiva de cualquier procedimiento, operatoria y/o regla comercial del esquema de pago bajo administración del participante, cuando así lo disponga el Directorio del BCRA, en situaciones en las que se encuentre gravemente comprometida la estabilidad, la seguridad y/o la eficiencia para las transferencias electrónicas de fondos."}, "pro
- arista: {"properties": {}, "sujeto_mencion": "Administrador de un esquema de transferencias electrónicas de fondos", "mencion_verificada": "exacta", "metodo_resolucion": "R4_sugerencia_modelo", "sujeto_id_modelo": "Sujeto_rol_alcance_snp_tr_nc", "procedencia": {"chunk_id": "snp_tr_nc::1.5.5.8", "punto": "1.5.5.8", "rol_documental": "punto_propio", "paginas": [9]}}

## 2. `Sujeto_rol_alcance_pagjub | ejecuta | Operacion_intercambio_de_informacion_bcra_entidades__snp_mep_1_2_1_bb17fc` — NG:resto · vigilancia:7

Texto que vio E3 (e0, bloque de lista True; págs. 3):

```
[encabezado | punto S1]
Sección 1. Generalidades
[encabezado | punto 1.2]
1.2. Objetivos
[texto propio | punto 1.2.1]
1.2.1. Establecer un sistema de intercambio de información entre el BCRA y las entidades par-
ticipantes basado en la transferencia de mensajes y transacciones entre computadores
a través de una plataforma moderna, eficiente y confiable en un marco de seguridad.
```

Versión: final (grafo sin cola).
- origen: {"id": "Sujeto_rol_alcance_pagjub", "type": "Sujeto", "label": "Entidades participantes (Pago de beneficios ANSES)", "properties": {"nivel": "rol"}, "procedencia": {"chunk_id": "snp_mep::1.2.1", "punto": "1.2.1", "rol_documental": "punto_propio", "paginas": [3]}}
- relación: `ejecuta`
- destino: {"id": "Operacion_intercambio_de_informacion_bcra_entidades__snp_mep_1_2_1_bb17fc", "type": "Operacion", "label": "Intercambio de información BCRA-entidades", "properties": {"tipo": "intercambio de información", "descripcion": "Sistema de intercambio de información entre el BCRA y las entidades participantes basado en la transferencia de mensajes y transacciones entre computadores a través de una plataforma moderna, eficiente y confiable en un marco de seguridad"}, "procedencia": {"chunk_id": "snp_mep::1.2.1", "punto": "1.2.1", "rol_documental": "punto_propio", "tramo": "Establecer un sistema 
- arista: {"properties": {}, "sujeto_mencion": "las entidades participantes", "mencion_verificada": "exacta", "metodo_resolucion": "R2_label_singularizado", "procedencia": {"chunk_id": "snp_mep::1.2.1", "punto": "1.2.1", "rol_documental": "punto_propio", "paginas": [3]}}

## 3. `Sujeto_rol_alcance_pimf | ejecuta | Operacion_presentacion_de_informacion_y_documentacion_por_imfs__pimf_3_2_2_f79fb8` — NG:resto · vigilancia:7

Texto que vio E3 (e0, bloque de lista True; págs. 9):

```
[encabezado | punto S3]
Sección 3. Procedimiento para el cumplimiento de los “Principios para las Infraestruc- turas de los Mercados Financieros” (PIMFs) por parte de las IMFs.
[encabezado | punto 3.2]
3.2. Adecuación.
[texto propio | punto 3.2.2]
3.2.2. BCRA podrá requerir a las IMFs, la información y documentación que considere necesa-
ria para evaluar la concreción de dichas adecuaciones.
```

Versión: final (grafo sin cola).
- origen: {"id": "Sujeto_rol_alcance_pimf", "type": "Sujeto", "label": "Infraestructuras del mercado financiero alcanzadas (PIMF)", "properties": {"nivel": "rol"}, "procedencia": {"chunk_id": "pimf::1.2.1", "punto": "1.2.1", "rol_documental": "punto_propio", "paginas": [4]}}
- relación: `ejecuta`
- destino: {"id": "Operacion_presentacion_de_informacion_y_documentacion_por_imfs__pimf_3_2_2_f79fb8", "type": "Operacion", "label": "Presentación de información y documentación por IMFs", "properties": {"tipo": "presentación informativa", "descripcion": "Presentación de información y documentación por parte de las IMFs, requerida por el BCRA para evaluar la concreción de adecuaciones a los Principios para las Infraestructuras de los Mercados Financieros."}, "procedencia": {"chunk_id": "pimf::3.2.2", "punto": "3.2.2", "rol_documental": "punto_propio", "tramo": "la información y documentación", "tramo_ver
- arista: {"properties": {}, "sujeto_mencion": "las IMFs", "mencion_verificada": "exacta", "metodo_resolucion": "R4_sugerencia_modelo", "sujeto_id_modelo": "Sujeto_rol_alcance_pimf", "procedencia": {"chunk_id": "pimf::3.2.2", "punto": "3.2.2", "rol_documental": "punto_propio", "paginas": [9]}}

## 4. `Sujeto_rol_alcance_retype | ejecuta | Operacion_deduccion_de_comision_del_monto_a_pagar__retype_3_2_3_5db10c` — NG:resto · vigilancia:7

Texto que vio E3 (e0, bloque de lista True; págs. 7):

```
[encabezado | punto S3]
Sección 3. Efectivización del pago.
[encabezado | punto 3.2]
3.2. Forma de pago.
[texto propio | punto 3.2.3]
3.2.3. Los bancos intervinientes deducirán la comisión convenida libremente con el Instituto
del monto a pagar a cada beneficiario.
```

Versión: final (grafo sin cola).
- origen: {"id": "Sujeto_rol_alcance_retype", "type": "Sujeto", "label": "Entidades bancarias participantes (Pago de retiros y pensiones militares)", "properties": {"nivel": "rol"}, "procedencia": {"chunk_id": "retype::1.1.2", "punto": "1.1.2", "rol_documental": "punto_propio", "paginas": [3]}}
- relación: `ejecuta`
- destino: {"id": "Operacion_deduccion_de_comision_del_monto_a_pagar__retype_3_2_3_5db10c", "type": "Operacion", "label": "Deducción de comisión del monto a pagar", "properties": {"tipo": "deducción de comisión", "descripcion": "Los bancos intervinientes deducen la comisión convenida libremente con el Instituto del monto a pagar a cada beneficiario"}, "procedencia": {"chunk_id": "retype::3.2.3", "punto": "3.2.3", "rol_documental": "punto_propio", "tramo": "Los bancos intervinientes deducirán la comisión convenida libremente con el Instituto del monto a pagar a cada beneficiario", "tramo_verificado": "exa
- arista: {"properties": {}, "sujeto_mencion": "Los bancos intervinientes", "mencion_verificada": "exacta", "metodo_resolucion": "R4_sugerencia_modelo", "sujeto_id_modelo": "Sujeto_rol_alcance_retype", "procedencia": {"chunk_id": "retype::3.2.3", "punto": "3.2.3", "rol_documental": "punto_propio", "paginas": [7]}}

## 5. `Sujeto_rol_alcance_retype | ejecuta | Operacion_utilizacion_de_servicios_de_casas_pagadoras__retype_2_1_1_927a1e` — NG:resto · vigilancia:7

Texto que vio E3 (e0, bloque de lista True; págs. 5):

```
[encabezado | punto S2]
Sección 2. Distribución de beneficios.
[encabezado | punto 2.1]
2.1. Designación de casas pagadoras.
[texto propio | punto 2.1.1]
2.1.1. El IAF utilizará los servicios de las casas correspondientes a los bancos
intervinientes que resulten mas convenientes, de acuerdo con los lugares de
residencia de sus beneficiarios o los lugares de pago que éstos indiquen.
```

Versión: final (grafo sin cola).
- origen: {"id": "Sujeto_rol_alcance_retype", "type": "Sujeto", "label": "Entidades bancarias participantes (Pago de retiros y pensiones militares)", "properties": {"nivel": "rol"}, "procedencia": {"chunk_id": "retype::1.1.2", "punto": "1.1.2", "rol_documental": "punto_propio", "paginas": [3]}}
- relación: `ejecuta`
- destino: {"id": "Operacion_utilizacion_de_servicios_de_casas_pagadoras__retype_2_1_1_927a1e", "type": "Operacion", "label": "Utilización de servicios de casas pagadoras", "properties": {"tipo": "Utilización de servicios de pago", "descripcion": "El IAF utilizará los servicios de las casas pagadoras correspondientes a los bancos intervinientes que resulten más convenientes, de acuerdo con los lugares de residencia de sus beneficiarios o los lugares de pago que éstos indiquen."}, "procedencia": {"chunk_id": "retype::2.1.1", "punto": "2.1.1", "rol_documental": "punto_propio", "tramo": "El IAF utilizará lo
- arista: {"properties": {}, "sujeto_mencion": "El IAF", "mencion_verificada": "exacta", "metodo_resolucion": "R4_sugerencia_modelo", "sujeto_id_modelo": "Sujeto_rol_alcance_retype", "procedencia": {"chunk_id": "retype::2.1.1", "punto": "2.1.1", "rol_documental": "punto_propio", "paginas": [5]}}

## 6. `Sujeto_rol_alcance_snp_spd | ejecuta | Operacion_solicitud_de_autorizacion_de_viaje_a_billetera_digital__snp_spd_8_4_1_2_69a9c6` — NG:resto · vigilancia:7

Texto que vio E3 (e0, bloque de lista True; págs. 24):

```
[encabezado | punto S8]
Sección 8. Viaje con QR
[encabezado | punto 8.4]
8.4. Funciones y responsabilidades
[encabezado | punto 8.4.1]
8.4.1. Administrador QR: gestionar los pagos. Es responsable de:
[texto propio | punto 8.4.1.2]
8.4.1.2. Solicitar, a partir de la información obtenida del código QR, la autorización del
viaje a la billetera digital emisora del código.
```

Versión: final (grafo sin cola).
- origen: {"id": "Sujeto_rol_alcance_snp_spd", "type": "Sujeto", "label": "Sujetos alcanzados (SNP - Servicios de pago)", "properties": {"nivel": "rol"}, "procedencia": {"chunk_id": "snp_mep::1.5", "punto": "1.5", "rol_documental": "punto_propio", "paginas": [4]}}
- relación: `ejecuta`
- destino: {"id": "Operacion_solicitud_de_autorizacion_de_viaje_a_billetera_digital__snp_spd_8_4_1_2_69a9c6", "type": "Operacion", "label": "Solicitud de autorización de viaje a billetera digital", "properties": {"tipo": "Solicitud de autorización", "descripcion": "Solicitud de autorización del viaje a la billetera digital emisora del código, realizada a partir de la información obtenida del código QR"}, "procedencia": {"chunk_id": "snp_spd::8.4.1.2", "punto": "8.4.1.2", "rol_documental": "punto_propio", "tramo": "Solicitar, a partir de la información obtenida del código QR, la autorización del viaje a l
- arista: {"properties": {}, "sujeto_mencion": "Administrador QR", "mencion_verificada": "exacta", "metodo_resolucion": "R4_sugerencia_modelo", "sujeto_id_modelo": "Sujeto_rol_alcance_snp_spd", "procedencia": {"chunk_id": "snp_spd::8.4.1.2", "punto": "8.4.1.2", "rol_documental": "punto_propio", "paginas": [24]}}

