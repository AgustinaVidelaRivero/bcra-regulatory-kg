# Material de T4 — aceptadas:items (30 fichas; B6.1, tanda final, T3, punto 7.5)

Sorteo: `aceptadas_items.json` (396f3328…, 2026-10-20T14:08:58-03:00); material armado a las 2026-10-20T14:09:10-03:00. Sin el estado de E3 ni las marcas de E3.

## 1. `ri_pspapt::S3` — RI:sin_raiz · aceptadas:items

Texto que vio E3 (e0, bloque de lista True; págs. 2):

```
[encabezado | punto Sbloque1]
SECCION II – INSTRUCCIONES PARTICULARES
[encabezado | punto SA]
Apartado A: Operaciones de adquirencia
[chapeau_seccion | punto SA]
Los datos deberán informarse totalizando las operaciones por consumos efectuados en el país con
tarjetas emitidas tanto en el país como en el exterior (cantidad y monto en moneda de origen), del
mes bajo informe.
Datos solicitados:
[texto propio | punto S3]
3. Código de esquema de pago utilizado: de acuerdo con la Tabla 2.
```

Versión: final (grafo sin cola). Nodos 2, aristas 1.
- **N1** Obligacion `Obligacion_informar_el_codigo_de_esquema_de_pago_utilizado_de_acuerdo_con_la_tabla_2__ri_ps_9ae2f8` — Informar código de esquema de pago · {"descripcion": "Informar el código de esquema de pago utilizado, de acuerdo con la Tabla 2", "tipo": "presentacion_informativa"} · tramo: Código de esquema de pago utilizado: de acuerdo con la Tabla 2
- **N2** TextoOrdenado `TextoOrdenado_ri_pspapt_pdf` — Régimen Informativo Proveedores de Servicios de Pago · {"archivo": "ri_pspapt.pdf", "materia": "RI - Proveedores de Servicios de Pago - Adquirentes de pagos con tarjeta", "version": "Comunicación A 8381 (vigencia 01/12/2025)"} · tramo: 
- **E1** (estructural) N1 —establecida_en→ N2 · {}

## 2. `ri_sef::P1::S14` — RI:sin_raiz · aceptadas:items

Texto que vio E3 (e0, bloque de lista True; págs. 3):

```
[encabezado | punto P1]
I. Información solicitada
[chapeau_seccion | punto P1::S0]
Se deberá integrar la siguiente información en función del tipo y etapa del trámite, y de la unidad de
servicio que se trate:
[texto propio | punto P1::S14]
14. Lugar de emplazamiento: de acuerdo con el detalle del punto b) correspondiente al Anexo II.
```

Versión: final (grafo sin cola). Nodos 3, aristas 3.
- **N1** Obligacion `Obligacion_informar_el_lugar_de_emplazamiento_de_acuerdo_con_el_detalle_del_punto_b_corresp_80d8df` — Informar lugar de emplazamiento · {"descripcion": "Informar el lugar de emplazamiento de acuerdo con el detalle del punto b) correspondiente al Anexo II", "tipo": "presentacion_informativa"} · tramo: Lugar de emplazamiento: de acuerdo con el detalle del punto b) correspondiente al Anexo II
- **N2** Sujeto `Sujeto_propuesto_las_entidades__ri_sef` — las entidades · {"nivel": "propuesto", "cuarentena": "true", "colision_cross_to": "true", "padre_sugerido": "Sujeto_rol_entidad_comprendida_reginf", "padre_desde_sugerencia_modelo": "true"} · tramo: 
- **N3** TextoOrdenado `TextoOrdenado_ri_sef_pdf` — Régimen Informativo Expansión Entidades Financieras · {"archivo": "ri_sef.pdf", "materia": "RI Cont. Mensual - Unidades de servicios de las entidades financieras", "version": "Comunicación A 7302 (vigencia 14/06/2021)"} · tramo: 
- **A1** (extraccion) N1 —aplica_a→ N2 · {}
- **E1** (estructural) N1 —establecida_en→ N3 · {}
- **C1** (catalogo_sujetos) N2 —padre_sugerido→ Sujeto_rol_entidad_comprendida_reginf · {"flag": "padre_sugerido_no_laudado"}

## 3. `ri_sef::P1::11.11` — RI:sin_raiz · aceptadas:items

Texto que vio E3 (e0, bloque de lista True; págs. 3):

```
[encabezado | punto P1]
I. Información solicitada
[encabezado | punto P1::S11]
11. Domicilio y teléfono:
[texto propio | punto P1::11.11]
11.11. Provincia: deberá informarse el código de provincia de acuerdo con el Anexo I - CÓ-
DIGO DE PROVINCIAS del Régimen Informativo Contable Mensual – Deudores del
Sistema Financiero.
```

Versión: final (grafo sin cola). Nodos 4, aristas 4.
- **N1** Definicion `Definicion_provincia_codigo_segun_anexo_i__el_codigo_de_provincia_debe_informarse_de_acuerd_9cc84a` — Provincia — código según Anexo I · {"termino": "Provincia", "descripcion": "El código de provincia debe informarse de acuerdo con el Anexo I - CÓDIGO DE PROVINCIAS del Régimen Informativo Contable Mensual – Deudores del Sistema Financiero"} · tramo: Provincia: deberá informarse el código de provincia de acuerdo con el Anexo I - CÓDIGO DE PROVINCIAS
- **N2** Obligacion `Obligacion_debera_informarse_el_codigo_de_provincia_de_acuerdo_con_el_anexo_i_codigo_de_pro_1b5fdc` — Informar código de provincia · {"descripcion": "Deberá informarse el código de provincia de acuerdo con el Anexo I - CÓDIGO DE PROVINCIAS del Régimen Informativo Contable Mensual – Deudores del Sistema Financiero", "tipo": "presentacion_informativa"} · tramo: deberá informarse el código de provincia de acuerdo con el Anexo I - CÓDIGO DE PROVINCIAS del Régimen Informativo Contable Mensual – Deudores del Sistema Financiero
- **N3** Sujeto `Sujeto_propuesto_las_entidades__ri_sef` — las entidades · {"nivel": "propuesto", "cuarentena": "true", "colision_cross_to": "true", "padre_sugerido": "Sujeto_rol_entidad_comprendida_reginf", "padre_desde_sugerencia_modelo": "true"} · tramo: 
- **N4** TextoOrdenado `TextoOrdenado_ri_sef_pdf` — Régimen Informativo Expansión Entidades Financieras · {"archivo": "ri_sef.pdf", "materia": "RI Cont. Mensual - Unidades de servicios de las entidades financieras", "version": "Comunicación A 7302 (vigencia 14/06/2021)"} · tramo: 
- **E1** (estructural) N1 —establecida_en→ N4 · {}
- **A1** (extraccion) N2 —aplica_a→ N3 · {}
- **E2** (estructural) N2 —establecida_en→ N4 · {}
- **C1** (catalogo_sujetos) N3 —padre_sugerido→ Sujeto_rol_entidad_comprendida_reginf · {"flag": "padre_sugerido_no_laudado"}

## 4. `ri_sef::P1::11.5` — RI:sin_raiz · aceptadas:items

Texto que vio E3 (e0, bloque de lista True; págs. 3):

```
[encabezado | punto P1]
I. Información solicitada
[encabezado | punto P1::S11]
11. Domicilio y teléfono:
[texto propio | punto P1::11.5]
11.5. Esquina.
```

Versión: final (grafo sin cola). Nodos 1, aristas 0.
- **N1** TextoOrdenado `TextoOrdenado_ri_sef_pdf` — Régimen Informativo Expansión Entidades Financieras · {"archivo": "ri_sef.pdf", "materia": "RI Cont. Mensual - Unidades de servicios de las entidades financieras", "version": "Comunicación A 7302 (vigencia 14/06/2021)"} · tramo: 

## 5. `ri_sef::P1::11.13` — RI:sin_raiz · aceptadas:items

Texto que vio E3 (e0, bloque de lista True; págs. 3):

```
[encabezado | punto P1]
I. Información solicitada
[encabezado | punto P1::S11]
11. Domicilio y teléfono:
[texto propio | punto P1::11.13]
11.13. Código interurbano y teléfono.
```

Versión: final (grafo sin cola). Nodos 3, aristas 3.
- **N1** Obligacion `Obligacion_integrar_en_la_solicitud_el_codigo_interurbano_y_telefono_de_la_unidad_de_servic_faf47d` — Informar código interurbano y teléfono · {"descripcion": "Integrar en la solicitud el código interurbano y teléfono de la unidad de servicio", "tipo": "presentacion_informativa"} · tramo: Código interurbano y teléfono
- **N2** Sujeto `Sujeto_propuesto_las_entidades__ri_sef` — las entidades · {"nivel": "propuesto", "cuarentena": "true", "colision_cross_to": "true", "padre_sugerido": "Sujeto_rol_entidad_comprendida_reginf", "padre_desde_sugerencia_modelo": "true"} · tramo: 
- **N3** TextoOrdenado `TextoOrdenado_ri_sef_pdf` — Régimen Informativo Expansión Entidades Financieras · {"archivo": "ri_sef.pdf", "materia": "RI Cont. Mensual - Unidades de servicios de las entidades financieras", "version": "Comunicación A 7302 (vigencia 14/06/2021)"} · tramo: 
- **A1** (extraccion) N1 —aplica_a→ N2 · {}
- **E1** (estructural) N1 —establecida_en→ N3 · {}
- **C1** (catalogo_sujetos) N2 —padre_sugerido→ Sujeto_rol_entidad_comprendida_reginf · {"flag": "padre_sugerido_no_laudado"}

## 6. `ri_pspapt::S12` — RI:sin_raiz · aceptadas:items

Texto que vio E3 (e0, bloque de lista True; págs. 2):

```
[encabezado | punto Sbloque1]
SECCION II – INSTRUCCIONES PARTICULARES
[encabezado | punto SA]
Apartado A: Operaciones de adquirencia
[chapeau_seccion | punto SA]
Los datos deberán informarse totalizando las operaciones por consumos efectuados en el país con
tarjetas emitidas tanto en el país como en el exterior (cantidad y monto en moneda de origen), del
mes bajo informe.
Datos solicitados:
[texto propio | punto S12]
12. Monto total por moneda de origen.
(*) MCC: Los Códigos de Categoría de Comerciante (MCC) son números de cuatro dígitos asignados a los
negocios por las empresas de tarjetas de crédito cuando un comercio comienza a aceptar pagos con tarjeta.
Estos códigos clasifican al comerciante según el tipo de bienes o servicios que ofrece.
```

Versión: final (grafo sin cola). Nodos 3, aristas 2.
- **N1** Definicion `Definicion_mcc_codigos_de_categoria_de_comerciante__codigos_de_categoria_de_comerciante_num_163b4d` — MCC — Códigos de Categoría de Comerciante · {"termino": "MCC", "descripcion": "Códigos de Categoría de Comerciante: números de cuatro dígitos asignados a los negocios por las empresas de tarjetas de crédito cuando un comercio comienza a aceptar pagos con tarjeta, que clasifican al comerciante según el tipo de bienes o servicios que ofrece"} · tramo: MCC: Los Códigos de Categoría de Comerciante (MCC) son números de cuatro dígitos asignados a los negocios por las empresas de tarjetas de crédito cuando un comercio comienza a aceptar pagos con tarjeta. Estos códigos clasifican al comerciante según el tipo de bienes o servicios que ofrece.
- **N2** Operacion `Operacion_informe_de_monto_total_por_moneda_de_origen__ri_pspapt_s12_f0376b` — Informe de monto total por moneda de origen · {"tipo": "presentación informativa", "descripcion": "Información del monto total por moneda de origen de operaciones de adquirencia con tarjetas emitidas en el país o en el exterior, totalizadas por consumos efectuados en el país del mes bajo informe"} · tramo: Monto total por moneda de origen
- **N3** TextoOrdenado `TextoOrdenado_ri_pspapt_pdf` — Régimen Informativo Proveedores de Servicios de Pago · {"archivo": "ri_pspapt.pdf", "materia": "RI - Proveedores de Servicios de Pago - Adquirentes de pagos con tarjeta", "version": "Comunicación A 8381 (vigencia 01/12/2025)"} · tramo: 
- **E1** (estructural) N1 —establecida_en→ N3 · {}
- **E2** (estructural) N2 —establecida_en→ N3 · {}

## 7. `ri_sef::P3::S1` — RI:sin_raiz · aceptadas:items

Texto que vio E3 (e0, bloque de lista True; págs. 5):

```
[encabezado | punto P3]
III. Otras informaciones.
[chapeau_seccion | punto P3::S0]
Adicionalmente, se deberá remitir la siguiente documentación:
[texto propio | punto P3::S1]
1. Información que debe acompañar la solicitud de apertura de sucursales en el exterior (punto
1.2. de la Norma sobre “Expansión de entidades financieras”).
```

Versión: final (grafo sin cola). Nodos 4, aristas 5.
- **N1** Obligacion `Obligacion_las_entidades_financieras_deberan_remitir_la_informacion_que_debe_acompanar_la_s_206e5c` — Remitir documentación — apertura sucursales exterior · {"tipo": "presentacion_informativa", "descripcion": "Las entidades financieras deberán remitir la información que debe acompañar la solicitud de apertura de sucursales en el exterior, conforme a lo establecido en el punto 1.2 de la Norma sobre Expansión de entidades financieras"} · tramo: se deberá remitir la siguiente documentación […] Información que debe acompañar la solicitud de apertura de sucursales en el exterior
- **N2** Operacion `Operacion_apertura_de_sucursales_en_el_exterior__ri_sef_p3_s1_3b5653` — Apertura de sucursales en el exterior · {"tipo": "apertura de sucursal", "descripcion": "Apertura de sucursales de entidades financieras en el exterior, regulada por la Norma sobre Expansión de entidades financieras (punto 1.2)"} · tramo: apertura de sucursales en el exterior
- **N3** Sujeto `Sujeto_propuesto_las_entidades__ri_sef` — las entidades · {"nivel": "propuesto", "cuarentena": "true", "colision_cross_to": "true", "padre_sugerido": "Sujeto_rol_entidad_comprendida_reginf", "padre_desde_sugerencia_modelo": "true"} · tramo: 
- **N4** TextoOrdenado `TextoOrdenado_ri_sef_pdf` — Régimen Informativo Expansión Entidades Financieras · {"archivo": "ri_sef.pdf", "materia": "RI Cont. Mensual - Unidades de servicios de las entidades financieras", "version": "Comunicación A 7302 (vigencia 14/06/2021)"} · tramo: 
- **A1** (extraccion) N1 —aplica_a→ N3 · {}
- **A2** (extraccion) N1 —condiciona→ N2 · {}
- **E1** (estructural) N1 —establecida_en→ N4 · {}
- **E2** (estructural) N2 —establecida_en→ N4 · {}
- **C1** (catalogo_sujetos) N3 —padre_sugerido→ Sujeto_rol_entidad_comprendida_reginf · {"flag": "padre_sugerido_no_laudado"}

## 8. `ri_laft::2.3.1` — RI:sin_raiz · aceptadas:items

Texto que vio E3 (e0, bloque de lista True; págs. 4):

```
[encabezado | punto S2]
2. Periodicidad
[intro | punto 2.3]
2.3. Proveedores no Financieros de Crédito y Proveedores de Servicios de Pago
Los Proveedores no Financieros de Crédito (PNFC) y los Proveedores de Servicios
de Pago (PSP), con excepción de aquellos no considerados como sujetos obligados
de acuerdo con la Resolución UIF N° 200/24, deberán presentar los siguientes infor-
mes de acuerdo con la periodicidad que a continuación se detalla:
[texto propio | punto 2.3.1]
2.3.1. Anual
a) Informe técnico de autoevaluación de riesgos de LA/FT y su metodología, y
b) Declaración de tolerancia al riesgo
Deberán ser enviados al BCRA, una vez aprobados por el órgano de adminis-
tración o máxima autoridad de la entidad e incorporando el recibo electrónico
presentado ante la UIF, teniendo en cuenta las especificaciones establecidas en
el texto ordenado de “Presentación de informaciones al Banco Central”.
El vencimiento para la presentación operará el 30.04 de cada año (o día hábil
siguiente si éste fuese inhábil).
Ante la identificación de un nuevo riesgo o modificación relevante de uno exis-
tente, se deberá proceder oportunamente con la actualización de la autoevalua-
ción de riesgos.
```

Versión: final (grafo sin cola). Nodos 8, aristas 10.
- **N1** Excepcion `Excepcion_no_aplica_la_obligacion_de_presentacion_a_los_pnfc_y_psp_no_considerados_como_su_120efa` — Excepción PNFC/PSP no sujetos obligados UIF · {"descripcion": "No aplica la obligación de presentación a los PNFC y PSP no considerados como sujetos obligados de acuerdo con la Resolución UIF N° 200/24"} · tramo: con excepción de aquellos no considerados como sujetos obligados de acuerdo con la Resolución UIF N° 200/24
- **N2** Obligacion `Obligacion_ante_la_identificacion_de_un_nuevo_riesgo_o_modificacion_relevante_de_uno_existe_1c45e5` — Actualización autoevaluación ante nuevo riesgo o modificación relevante · {"tipo": "otra", "descripcion": "Ante la identificación de un nuevo riesgo o modificación relevante de uno existente, se deberá proceder oportunamente con la actualización de la autoevaluación de riesgos"} · tramo: Ante la identificación de un nuevo riesgo o modificación relevante de uno existente, se deberá proceder oportunamente con la actualización de la autoevaluación de riesgos
- **N3** Obligacion `Obligacion_los_pnfc_y_psp_deberan_enviar_al_bcra_una_vez_aprobados_por_el_organo_de_adminis_bc2be2` — Envío anual informe técnico y declaración tolerancia — PNFC y PSP · {"tipo": "presentacion_informativa", "descripcion": "Los PNFC y PSP deberán enviar al BCRA, una vez aprobados por el órgano de administración o máxima autoridad de la entidad e incorporando el recibo electrónico presentado ante la UIF, los informes técnico de autoevaluación de riesgos de LA/FT y su metodología, y la declaración de tolerancia al riesgo, conforme a las especificaciones del texto ord · tramo: Los Proveedores no Financieros de Crédito (PNFC) y los Proveedores de Servicios de Pago (PSP), con excepción de aquellos no considerados como sujetos obligados de acuerdo con la Resolución UIF N° 200/24, deberán presentar los siguientes informes […] Deberán ser enviados al BCRA, una vez aprobados po
- **N4** Operacion `Operacion_presentacion_declaracion_tolerancia_al_riesgo__ri_laft_2_3_1_40e388` — Presentación declaración tolerancia al riesgo · {"tipo": "presentación informativa", "descripcion": "Declaración de tolerancia al riesgo, a ser enviada al BCRA una vez aprobada por el órgano de administración o máxima autoridad de la entidad e incorporando el recibo electrónico presentado ante la UIF"} · tramo: Declaración de tolerancia al riesgo
- **N5** Operacion `Operacion_presentacion_informe_tecnico_autoevaluacion_la_ft__ri_laft_2_3_1_f73c13` — Presentación informe técnico autoevaluación LA/FT · {"tipo": "presentación informativa", "descripcion": "Informe técnico de autoevaluación de riesgos de LA/FT y su metodología, a ser enviado al BCRA una vez aprobado por el órgano de administración o máxima autoridad de la entidad e incorporando el recibo electrónico presentado ante la UIF"} · tramo: Informe técnico de autoevaluación de riesgos de LA/FT y su metodología
- **N6** Sujeto `Sujeto_proveedor_de_servicios_de_pago` — Proveedores de servicios de pago · {"nivel": "clase"} · tramo: 
- **N7** Sujeto `Sujeto_proveedor_no_financiero_de_credito` — Proveedores no financieros de crédito · {"nivel": "clase", "alias": ["PNFC"]} · tramo: 
- **N8** TextoOrdenado `TextoOrdenado_ri_laft_pdf` — Régimen Informativo LAFT · {"archivo": "ri_laft.pdf", "materia": "RI - Prevención del Lavado de Activos, del Financiamiento del Terrorismo y Otras Actividades Ilícitas", "version": "Comunicación A 8429 (vigencia 25/04/2026)"} · tramo: 
- **E1** (estructural) N1 —establecida_en→ N8 · {}
- **A1** (extraccion) N1 —exceptua_obligacion→ N3 · {}
- **A2** (extraccion) N2 —aplica_a→ N6 · {}
- **A3** (extraccion) N2 —aplica_a→ N7 · {}
- **E2** (estructural) N2 —establecida_en→ N8 · {}
- **A4** (extraccion) N3 —aplica_a→ N6 · {}
- **A5** (extraccion) N3 —aplica_a→ N7 · {}
- **E3** (estructural) N3 —establecida_en→ N8 · {}
- **E4** (estructural) N4 —establecida_en→ N8 · {}
- **E5** (estructural) N5 —establecida_en→ N8 · {}

## 9. `ri_dsf::2.1` — RI:sin_raiz · aceptadas:items

Texto que vio E3 (e0, bloque de lista True; págs. 2, 3):

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

Versión: final (grafo sin cola). Nodos 17, aristas 23.
- **N1** Definicion `Definicion_tipo_de_identificacion_del_deudor__los_tipos_de_identificacion_del_deudor_son_cl_5f34da` — Tipo de identificación del deudor · {"termino": "Tipo", "descripcion": "Los tipos de identificación del deudor son: Clave Única de Identificación Tributaria (C.U.I.T.), Código Único de Identificación Laboral (C.U.I.L.) y Clave de Identificación (C.D.I.), según la Administración Federal de Ingresos Públicos."} · tramo: Administración Federal de Ingresos Públicos - Clave Única de Identificación Tributaria (C.U.I.T.). - Código Único de Identificación Laboral (C.U.I.L.). - Clave de Identificación (C.D.I.).
- **N2** Excepcion `Excepcion_no_se_informaran_el_bcra_ni_los_deudores_cuyo_saldo_de_deuda_sea_inferior_a_25_m_ed952a` — Excepción BCRA y deudores bajo umbral · {"descripcion": "No se informarán el BCRA ni los deudores cuyo saldo de deuda sea inferior a $25 mil.", "umbrales": [{"tramo": "saldo de deuda sea inferior a $25 mil", "valor": "25000", "unidad": "moneda", "moneda": "ARS", "comparacion": "maximo_estricto", "regla_comparacion": "simple:inferior", "origen": "e1", "tramo_verificado": "exacta"}]} · tramo: con excepción del B.C.R.A. y aquellos deudores cuyo saldo de deuda sea inferior a $25 mil
- **N3** Obligacion `Obligacion_cuando_el_deudor_no_este_incluido_en_el_padron_de_la_afip_debe_informarse_segun__c74443` — Informar según AFIP cuando deudor no está en padrón · {"tipo": "presentacion_informativa", "descripcion": "Cuando el deudor no esté incluido en el Padrón de la AFIP, debe informarse según la identificación y denominación provista por la Administración Federal de Ingresos Públicos."} · tramo: Cuando el deudor no esté incluido en dicho padrón, deberá informarse según la identificación y denominación provista por la Administración Federal de Ingresos Públicos.
- **N4** Obligacion `Obligacion_el_mismo_criterio_de_consistencia_debe_aplicarse_al_informar_la_cartera_que_cons_8ca51f` — Aplicar criterio consistente a cartera inicial cesionada · {"tipo": "presentacion_informativa", "descripcion": "El mismo criterio de consistencia debe aplicarse al informar la cartera que constituye el saldo inicial al 31/12/2017 de las financiaciones que fueron objeto de cesiones previas entre entidades financieras."} · tramo: El mismo criterio deberá aplicarse a fin de informar la cartera que constituye el saldo inicial al 31/12/2017 de las financiaciones que hayan sido objeto de cesiones concertadas previamente entre las entidades financieras.
- **N5** Obligacion `Obligacion_es_necesario_unificar_los_criterios_aplicables_al_presente_regimen_a_partir_de_l_813557` — Unificar criterios para cesiones según NIIF · {"tipo": "otra", "descripcion": "Es necesario unificar los criterios aplicables al presente régimen a partir de la vigencia de las NIIF para los casos de cesiones de cartera realizadas entre entidades financieras y otro tipo de entidades."} · tramo: resulta necesaria la unificación de los criterios que se aplican para el presente régimen a partir de la vigencia de las NIIF para los casos relativos a cesiones de cartera realizadas entre entidades financieras y otro tipo de entidades.
- **N6** Obligacion `Obligacion_las_entidades_deben_continuar_informando_a_sus_deudores_mientras_persistan_las_g_6fee0a` — Continuar informando deudores en gestiones de cobro · {"tipo": "presentacion_informativa", "descripcion": "Las entidades deben continuar informando a sus deudores mientras persistan las gestiones de cobro de sus acreencias."} · tramo: Las entidades deben seguir informando a sus deudores en la medida que continúen las gestiones de cobro de sus acreencias.
- **N7** Obligacion `Obligacion_las_entidades_financieras_cedentes_y_cesionarias_deben_acordar_la_registracion_c_385cf7` — Acordar registración contable consistente en cesiones · {"tipo": "otra", "descripcion": "Las entidades financieras cedentes y cesionarias deben acordar la registración contable de manera consistente, conforme a lo establecido en el punto 2.1.4 de las normas sobre Cesión de cartera de créditos."} · tramo: las entidades financieras cedentes y cesionarias deberán acordar la registración contable consistentemente tal como se encuentra establecido en el punto 2.1.4. de las normas sobre "Cesión de cartera de créditos".
- **N8** Obligacion `Obligacion_las_entidades_financieras_y_otros_entes_deben_informar_la_totalidad_de_sus_deudo_7ee58f` — Informar totalidad de deudores con excepciones · {"tipo": "presentacion_informativa", "descripcion": "Las entidades financieras y otros entes deben informar la totalidad de sus deudores, excepto el BCRA y aquellos cuyo saldo de deuda sea inferior a $25 mil.", "umbrales": [{"tramo": "saldo de deuda sea inferior a $25 mil", "valor": "25000", "unidad": "moneda", "moneda": "ARS", "comparacion": "maximo_estricto", "regla_comparacion": "simple:inferio · tramo: Se informará la totalidad de los deudores de las entidades financieras y otros entes mencionados en el último párrafo del punto precedente, con excepción del B.C.R.A. y aquellos deudores cuyo saldo de deuda sea inferior a $25 mil.
- **N9** Obligacion `Obligacion_para_definir_al_deudor_se_deben_tener_en_cuenta_los_conceptos_del_texto_ordenado_a3db75` — Definir deudor según Gestión Crediticia · {"tipo": "otra", "descripcion": "Para definir al deudor se deben tener en cuenta los conceptos del Texto Ordenado de Normas sobre Gestión Crediticia."} · tramo: Para definir al deudor se tendrán en cuenta los conceptos vertidos en el Texto ordenado de las Normas sobre "Gestión Crediticia".
- **N10** Obligacion `Obligacion_se_debe_informar_la_razon_social_o_denominacion_de_personas_juridicas_en_forma_c_986346` — Informar razón social completa de personas jurídicas · {"tipo": "presentacion_informativa", "descripcion": "Se debe informar la razón social o denominación de personas jurídicas en forma completa."} · tramo: Razón social o denominación, en forma completa.
- **N11** Obligacion `Obligacion_se_debe_informar_los_apellidos_y_nombres_de_personas_humanas_y_sociedades_de_hec_369bab` — Informar apellidos y nombres completos de personas humanas · {"tipo": "presentacion_informativa", "descripcion": "Se debe informar los apellidos y nombres de personas humanas y sociedades de hecho en forma completa."} · tramo: Apellidos y nombres, en forma completa.
- **N12** Obligacion `Obligacion_se_deben_tener_en_cuenta_las_disposiciones_de_la_seccion_4_sobre_verificacion_vi_eb8293` — Tener en cuenta disposiciones sobre documentos de identidad · {"tipo": "otra", "descripcion": "Se deben tener en cuenta las disposiciones de la Sección 4 sobre Verificación vinculada con documentos de identidad del Texto Ordenado Documentos de Identificación en Vigencia."} · tramo: Se deberán tener en cuenta las disposiciones contenidas en la Sección 4. Verificación vinculada con los documentos de identidad del Texto Ordenado "Documentos de Identificación en Vigencia"
- **N13** Potestad `Potestad_bcra_reemplaza_denominacion_por_padron_afip__el_bcra_podra_reemplazar_la_denomin_de1971` — BCRA reemplaza denominación por Padrón AFIP · {"descripcion": "El BCRA podrá reemplazar la denominación originalmente informada por la que figure en el Padrón de la AFIP, bajo la exclusiva responsabilidad de la entidad."} · tramo: este Banco Central reemplazará, bajo la exclusiva responsabilidad de la entidad, la "Denominación" originalmente informada, por la que figure en el "Padrón de la AFIP".
- **N14** Restriccion `Restriccion_no_se_consolidara_la_informacion_en_los_casos_de_grupos_o_conjuntos_economicos___2b19cb` — Prohibición de consolidación en grupos económicos · {"tipo": "prohibicion", "descripcion": "No se consolidará la información en los casos de grupos o conjuntos económicos."} · tramo: En los casos de grupos o conjuntos económicos no se consolidará la información.
- **N15** Sujeto `Sujeto_entidad_financiera` — Entidades financieras · {"nivel": "clase", "alias": ["Entidades financieras emisoras de tarjetas de crédito y/o compra", "Entidad financiera emisora de tarjetas de crédito y/o compra"]} · tramo: 
- **N16** Sujeto `Sujeto_propuesto_las_entidades__ri_dsf` — Las entidades · {"nivel": "propuesto", "cuarentena": "true", "colision_cross_to": "true", "padre_sugerido": "Sujeto_entidad_financiera", "padre_desde_sugerencia_modelo": "true"} · tramo: 
- **N17** TextoOrdenado `TextoOrdenado_ri_dsf_pdf` — Deudores del Sistema Financiero · {"archivo": "ri_dsf.pdf", "materia": "RI Cont. Mensual - Deudores del Sistema Financiero y Composición de los conjuntos económicos", "version": "Comunicación A 8370 (vigencia 19/12/2025)"} · tramo: 
- **E1** (estructural) N1 —establecida_en→ N17 · {}
- **E2** (estructural) N2 —establecida_en→ N17 · {}
- **A1** (extraccion) N2 —exceptua_obligacion→ N8 · {}
- **E3** (estructural) N3 —establecida_en→ N17 · {}
- **E4** (estructural) N4 —establecida_en→ N17 · {}
- **E5** (estructural) N5 —establecida_en→ N17 · {}
- **A2** (extraccion) N6 —aplica_a→ N16 · {}
- **E6** (estructural) N6 —establecida_en→ N17 · {}
- **A3** (extraccion) N7 —aplica_a→ N15 · {}
- **E7** (estructural) N7 —establecida_en→ N17 · {}
- **R1** (remision_derivada) N7 —remite_a→ Obligacion_en_los_casos_de_cesion_de_cartera_sin_responsabilidad_para_el_cedente_el_pertine_584bda · {"alcance": "externa", "destino": "cescar::2.1.4", "evidencia": "punto\n2.1.4. de las normas sobre “Cesión de cartera de créditos"}
- **R2** (remision_derivada) N7 —remite_a→ Obligacion_en_los_demas_casos_debera_incluirse_una_clausula_en_la_que_se_especifique_expres_e18560 · {"alcance": "externa", "destino": "cescar::2.1.4", "evidencia": "punto\n2.1.4. de las normas sobre “Cesión de cartera de créditos"}
- **R3** (remision_derivada) N7 —remite_a→ Operacion_cesion_de_cartera_con_responsabilidad__cescar_2_1_4_1c11c0 · {"alcance": "externa", "destino": "cescar::2.1.4", "evidencia": "punto\n2.1.4. de las normas sobre “Cesión de cartera de créditos"}
- **R4** (remision_derivada) N7 —remite_a→ Operacion_cesion_de_cartera_sin_responsabilidad__cescar_2_1_4_2448fd · {"alcance": "externa", "destino": "cescar::2.1.4", "evidencia": "punto\n2.1.4. de las normas sobre “Cesión de cartera de créditos"}
- **A4** (extraccion) N8 —aplica_a→ N15 · {}
- **E8** (estructural) N8 —establecida_en→ N17 · {}
- **E9** (estructural) N9 —establecida_en→ N17 · {}
- **E10** (estructural) N10 —establecida_en→ N17 · {}
- **E11** (estructural) N11 —establecida_en→ N17 · {}
- **E12** (estructural) N12 —establecida_en→ N17 · {}
- **E13** (estructural) N13 —establecida_en→ N17 · {}
- **E14** (estructural) N14 —establecida_en→ N17 · {}
- **C1** (catalogo_sujetos) N16 —padre_sugerido→ N15 · {"flag": "padre_sugerido_no_laudado"}

## 10. `ri_sef::P1::11.8` — RI:sin_raiz · aceptadas:items

Texto que vio E3 (e0, bloque de lista True; págs. 3):

```
[encabezado | punto P1]
I. Información solicitada
[encabezado | punto P1::S11]
11. Domicilio y teléfono:
[texto propio | punto P1::11.8]
11.8. Localidad.
```

Versión: final (grafo sin cola). Nodos 1, aristas 0.
- **N1** TextoOrdenado `TextoOrdenado_ri_sef_pdf` — Régimen Informativo Expansión Entidades Financieras · {"archivo": "ri_sef.pdf", "materia": "RI Cont. Mensual - Unidades de servicios de las entidades financieras", "version": "Comunicación A 7302 (vigencia 14/06/2021)"} · tramo: 

## 11. `ri_sef::P1::11.1` — RI:sin_raiz · aceptadas:items

Texto que vio E3 (e0, bloque de lista True; págs. 2):

```
[encabezado | punto P1]
I. Información solicitada
[encabezado | punto P1::S11]
11. Domicilio y teléfono:
[texto propio | punto P1::11.1]
11.1. Calle.
```

Versión: final (grafo sin cola). Nodos 1, aristas 0.
- **N1** TextoOrdenado `TextoOrdenado_ri_sef_pdf` — Régimen Informativo Expansión Entidades Financieras · {"archivo": "ri_sef.pdf", "materia": "RI Cont. Mensual - Unidades de servicios de las entidades financieras", "version": "Comunicación A 7302 (vigencia 14/06/2021)"} · tramo: 

## 12. `ri_sef::P1::S6` — RI:sin_raiz · aceptadas:items

Texto que vio E3 (e0, bloque de lista True; págs. 2):

```
[encabezado | punto P1]
I. Información solicitada
[chapeau_seccion | punto P1::S0]
Se deberá integrar la siguiente información en función del tipo y etapa del trámite, y de la unidad de
servicio que se trate:
[texto propio | punto P1::S6]
6. Identificación de la unidad: deberán numerarse secuencialmente las unidades que depen-
den de una misma casa.
En el caso de las unidades de servicio código 37, la numeración secuencial deberá realizarse
en forma independiente respecto de cada agencia oportunamente informada al BCRA, que
dependa de cada sucursal o casa central / casa matriz.
```

Versión: final (grafo sin cola). Nodos 5, aristas 6.
- **N1** Obligacion `Obligacion_las_entidades_deberan_numerar_secuencialmente_las_unidades_que_dependen_de_una_m_0eda27` — Numeración secuencial de unidades · {"descripcion": "Las entidades deberán numerar secuencialmente las unidades que dependen de una misma casa.", "tipo": "otra"} · tramo: deberán numerarse secuencialmente las unidades que dependen de una misma casa
- **N2** Obligacion `Obligacion_para_las_unidades_de_servicio_codigo_37_la_numeracion_secuencial_debe_realizarse_eb4e9f` — Numeración independiente para unidades código 37 · {"descripcion": "Para las unidades de servicio código 37, la numeración secuencial debe realizarse de forma independiente respecto de cada agencia informada al BCRA que dependa de cada sucursal o casa central/casa matriz.", "tipo": "otra"} · tramo: para las unidades de servicio código 37, la numeración secuencial deberá realizarse en forma independiente respecto de cada agencia oportunamente informada al BCRA, que dependa de cada sucursal o casa central / casa matriz
- **N3** Sujeto `Sujeto_propuesto_las_unidades` — las unidades · {"nivel": "propuesto", "cuarentena": "true", "padre_sugerido": "Sujeto_estructura"} · tramo: 
- **N4** Sujeto `Sujeto_propuesto_las_unidades_de_servicio_codigo_37` — las unidades de servicio código 37 · {"nivel": "propuesto", "cuarentena": "true", "padre_sugerido": "Sujeto_estructura"} · tramo: 
- **N5** TextoOrdenado `TextoOrdenado_ri_sef_pdf` — Régimen Informativo Expansión Entidades Financieras · {"archivo": "ri_sef.pdf", "materia": "RI Cont. Mensual - Unidades de servicios de las entidades financieras", "version": "Comunicación A 7302 (vigencia 14/06/2021)"} · tramo: 
- **A1** (extraccion) N1 —aplica_a→ N3 · {}
- **E1** (estructural) N1 —establecida_en→ N5 · {}
- **A2** (extraccion) N2 —aplica_a→ N4 · {}
- **E2** (estructural) N2 —establecida_en→ N5 · {}
- **C1** (catalogo_sujetos) N3 —padre_sugerido→ Sujeto_estructura · {"flag": "padre_sugerido_no_laudado"}
- **C2** (catalogo_sujetos) N4 —padre_sugerido→ Sujeto_estructura · {"flag": "padre_sugerido_no_laudado"}

## 13. `ri_ai::1.2.1` — RI:resto · aceptadas:items

Texto que vio E3 (e0, bloque de lista True; págs. 2):

```
[encabezado | punto S1]
Sección 1. Entidades Comprendidas
[encabezado | punto 1.2]
1.2. Sujetas al régimen de información sobre bases consolidadas:
[texto propio | punto 1.2.1]
1.2.1 Entidad financiera con filiales en el país y en el exterior.
```

Versión: final (grafo sin cola). Nodos 2, aristas 1.
- **N1** Definicion `Definicion_entidad_financiera_con_filiales_consolidadas__entidad_financiera_que_posee_filia_3fd17d` — Entidad financiera con filiales consolidadas · {"termino": "Entidad financiera con filiales en el país y en el exterior", "descripcion": "Entidad financiera que posee filiales tanto en el país como en el exterior, sujeta al régimen de información sobre bases consolidadas"} · tramo: Entidad financiera con filiales en el país y en el exterior
- **N2** TextoOrdenado `TextoOrdenado_ri_ai_pdf` — Régimen Informativo sobre Bases Consolidadas · {"archivo": "ri_ai.pdf", "materia": "RI Cont. Mensual - Relación para los activos inmovilizados y otros conceptos", "version": "Comunicación A 8009 (vigencia 01/04/2024)"} · tramo: 
- **E1** (estructural) N1 —establecida_en→ N2 · {}

## 14. `ri_ai::1.2.2` — RI:resto · aceptadas:items

Texto que vio E3 (e0, bloque de lista True; págs. 2):

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

Versión: final (grafo sin cola). Nodos 5, aristas 7.
- **N1** Excepcion `Excepcion_las_entidades_financieras_que_consoliden_con_otra_s_entidad_es_financiera_s_qued_bf5463` — Excepción: entidades que consoliden con otras · {"descripcion": "Las entidades financieras que consoliden con otra/s entidad/es financiera/s quedan exceptuadas de la obligación de no presentar información consolidada mensual."} · tramo: excepto las que consoliden con otra/s entidad/es financiera/s
- **N2** Obligacion `Obligacion_las_entidades_financieras_no_presentaran_la_informacion_consolidada_mensual_debi_eb4bfc` — No presentar información consolidada mensual · {"descripcion": "Las entidades financieras no presentarán la información consolidada mensual, debiendo consignar en su lugar, de acuerdo con las instrucciones operativas instrumentadas a través de la respectiva Circular RUNOR, los siguientes datos: importe de activos inmovilizados y otros conceptos (Código 100- Código 200+ Código 300), el 100% de la responsabilidad patrimonial computable de la ent · tramo: no presentarán la información consolidada mensual
- **N3** Obligacion `Obligacion_si_se_registra_exceso_el_importe_debera_informarse_teniendo_en_cuenta_el_tratami_3298d4` — Informar exceso según normas de capitales mínimos · {"descripcion": "Si se registra exceso, el importe deberá informarse teniendo en cuenta el tratamiento establecido a través del texto ordenado de las normas sobre Incumplimientos de capitales mínimos y relaciones técnicas. Criterios aplicables.", "tipo": "reporte_al_supervisor"} · tramo: De registrar exceso, el importe deberá informarse teniendo en cuenta el tratamiento establecido a través del texto ordenado de las normas sobre "Incumplimientos de capitales mínimos y relaciones técnicas. Criterios aplicables".
- **N4** Sujeto `Sujeto_entidad_financiera` — Entidades financieras · {"nivel": "clase", "alias": ["Entidades financieras emisoras de tarjetas de crédito y/o compra", "Entidad financiera emisora de tarjetas de crédito y/o compra"]} · tramo: 
- **N5** TextoOrdenado `TextoOrdenado_ri_ai_pdf` — Régimen Informativo sobre Bases Consolidadas · {"archivo": "ri_ai.pdf", "materia": "RI Cont. Mensual - Relación para los activos inmovilizados y otros conceptos", "version": "Comunicación A 8009 (vigencia 01/04/2024)"} · tramo: 
- **E1** (estructural) N1 —establecida_en→ N5 · {}
- **A1** (extraccion) N1 —exceptua_obligacion→ N2 · {}
- **A2** (extraccion) N2 —aplica_a→ N4 · {}
- **E2** (estructural) N2 —establecida_en→ N5 · {}
- **A3** (extraccion) N3 —aplica_a→ N4 · {}
- **E3** (estructural) N3 —establecida_en→ N5 · {}
- **R1** (remision_derivada) N3 —remite_a→ TextoOrdenado_incuca_pdf · {"alcance": "to_entero", "destino": "incuca::TO", "evidencia": "texto ordenado de las normas sobre “Incumplimientos de capi-\ntales mínimos y relaciones técnicas"}

## 15. `ri_msrl::Sbloque1` — RI:resto · aceptadas:items

Texto que vio E3 (e0, bloque de lista True; págs. 3):

```
[encabezado | punto S2]
Sección 2. Instrucciones Particulares
[chapeau_seccion | punto S2]
El presente régimen informativo tiene como objetivo la obtención de los datos necesarios para la
determinación del coeficiente de cobertura de liquidez (LCR), teniendo en cuenta lo dispuesto en
las Normas sobre Ratio de Cobertura de Liquidez, de acuerdo con la siguiente fórmula:
[texto propio | punto Sbloque1]
Fondo de Activos líquidos de alta calidad (FALAC)
________________________________________________________ ≥ 1
Salidas de efectivo netas totales (siguientes 30 días corridos)
Donde:
FALAC = Partidas 100000 * aforo
Salidas de efectivo netas totales = Salidas – Mín (entradas; 75% salidas)
Salidas = Partidas 200000 * Factor (tasa de salida)
Entradas = Partidas 300000 * Factor (tasa de entrada)
Los aforos y los respectivos factores serán aplicados en esta Institución en la etapa de
procesamiento de la información.
```

Versión: final (grafo sin cola). Nodos 6, aristas 6.
- **N1** Definicion `Definicion_falac_fondo_de_activos_liquidos_de_alta_calidad__fondo_de_activos_liquidos_de_al_ccbaf9` — FALAC — Fondo de Activos líquidos de alta calidad · {"termino": "FALAC", "descripcion": "Fondo de Activos líquidos de alta calidad, calculado como Partidas 100000 multiplicadas por el aforo correspondiente."} · tramo: FALAC = Partidas 100000 * aforo
- **N2** Definicion `Definicion_salidas_de_efectivo_netas_totales__salidas_de_efectivo_netas_totales_calculadas__231f06` — Salidas de efectivo netas totales · {"termino": "Salidas de efectivo netas totales", "descripcion": "Salidas de efectivo netas totales, calculadas como Salidas menos el mínimo entre entradas y el 75% de salidas."} · tramo: Salidas de efectivo netas totales = Salidas – Mín (entradas; 75% salidas)
- **N3** Obligacion `Obligacion_las_entidades_deberan_aplicar_los_aforos_y_los_respectivos_factores_en_la_etapa__8031bc` — Aplicación de aforos y factores en procesamiento · {"tipo": "otra", "descripcion": "Las entidades deberán aplicar los aforos y los respectivos factores en la etapa de procesamiento de la información."} · tramo: Los aforos y los respectivos factores serán aplicados en esta Institución en la etapa de procesamiento de la información.
- **N4** Operacion `Operacion_calculo_del_coeficiente_lcr__ri_msrl_sbloque1_4d984a` — Cálculo del coeficiente LCR · {"tipo": "cálculo", "descripcion": "Determinación del coeficiente de cobertura de liquidez (LCR) mediante la relación entre el Fondo de Activos líquidos de alta calidad (FALAC) y las salidas de efectivo netas totales de los siguientes 30 días corridos, con un umbral mínimo de 1."} · tramo: Fondo de Activos líquidos de alta calidad (FALAC) ≥ 1 Salidas de efectivo netas totales (siguientes 30 días corridos)
- **N5** Sujeto `Sujeto_propuesto_esta_institucion` — esta Institución · {"nivel": "propuesto", "cuarentena": "true", "padre_sugerido": "Sujeto_rol_entidad_comprendida_reginf"} · tramo: 
- **N6** TextoOrdenado `TextoOrdenado_ri_msrl_pdf` — Régimen Informativo MSRL · {"archivo": "ri_msrl.pdf", "materia": "RI Cont. Mensual - Medición y Seguimiento del Riesgo de Liquidez", "version": "Comunicación A 8308 (vigencia 04/07/2025)"} · tramo: 
- **E1** (estructural) N1 —establecida_en→ N6 · {}
- **E2** (estructural) N2 —establecida_en→ N6 · {}
- **A1** (extraccion) N3 —aplica_a→ N5 · {}
- **E3** (estructural) N3 —establecida_en→ N6 · {}
- **E4** (estructural) N4 —establecida_en→ N6 · {}
- **C1** (catalogo_sujetos) N5 —padre_sugerido→ Sujeto_rol_entidad_comprendida_reginf · {"flag": "padre_sugerido_no_laudado"}

## 16. `micemp::1.2` — NG:sin_raiz · aceptadas:items

Texto que vio E3 (e0, bloque de lista True; págs. 3):

```
[encabezado | punto S1]
1. Determinación.
[chapeau_seccion | punto S1]
Serán de aplicación las disposiciones en la materia establecidas por la autoridad de aplicación de
la Ley 24.467 (y sus modificatorias).
A esos fines, el cómputo de los requisitos previstos por la Secretaría de Emprendedores y de la
Pequeña y Mediana Empresa del Ministerio de Producción –SEPyME– (por ej. los referidos al
valor de ventas netas y/o personal ocupado y/o valor de sus activos), podrá efectuarse a partir
de:
[texto propio | punto 1.2]
1.2. estados financieros o contables de la empresa, según corresponda, siempre que cuenten
con dictamen de auditor externo; o
```

Versión: final (grafo sin cola). Nodos 3, aristas 3.
- **N1** Condicion `Condicion_dictamen_de_auditor_externo__los_estados_financieros_o_contables_deben_contar_co_332e5a` — Dictamen de auditor externo · {"descripcion": "Los estados financieros o contables deben contar con dictamen de auditor externo."} · tramo: siempre que cuenten con dictamen de auditor externo
- **N2** Operacion `Operacion_presentacion_de_estados_financieros_o_contables__micemp_1_2_89b305` — Presentación de estados financieros o contables · {"tipo": "presentación de documentación contable", "descripcion": "Presentación de estados financieros o contables de la empresa, según corresponda, como medio de comprobación de requisitos de categorización MiCEMP."} · tramo: estados financieros o contables de la empresa, según corresponda
- **N3** TextoOrdenado `TextoOrdenado_micemp_pdf` — Texto Ordenado MiPyME · {"archivo": "micemp.pdf", "materia": "Determinación de la condición de micro, pequeña o mediana empresa", "version": "Comunicación A 7277 (vigencia 09/04/2021)"} · tramo: 
- **A1** (extraccion) N1 —condicion_de→ N2 · {}
- **E1** (estructural) N1 —establecida_en→ N3 · {}
- **E2** (estructural) N2 —establecida_en→ N3 · {}

## 17. `cedin::12.2.4` — NG:sin_raiz · aceptadas:items

Texto que vio E3 (e0, bloque de lista True; págs. 15):

```
[encabezado | punto S12]
12. Extravío, sustracción o destrucción del CEDIN.
[encabezado | punto 12.2]
12.2. Obligaciones a cargo de la entidad financiera.
[intro | punto 12.2]
Al recibir la notificación prevista en el punto 12.1., la entidad financiera deberá:
[texto propio | punto 12.2.4]
12.2.4. Remitir al BCRA, dentro de los diez días hábiles, la notificación y demás docu-
mentación recibida, junto con cualquier otro elemento o dato que entienda rele-
vante, conforme a lo previsto en el punto 11.
```

Versión: final (grafo sin cola). Nodos 3, aristas 2.
- **N1** Obligacion `Obligacion_la_entidad_financiera_debera_remitir_al_bcra_dentro_de_los_diez_dias_habiles_la__2fbd5d` — Remitir al BCRA notificación y documentación · {"descripcion": "La entidad financiera deberá remitir al BCRA, dentro de los diez días hábiles, la notificación y demás documentación recibida en relación con el extravío, sustracción o destrucción del CEDIN, junto con cualquier otro elemento o dato que entienda relevante, conforme a lo previsto en el punto 11.", "tipo": "reporte_al_supervisor", "frecuencia": "dentro de los diez días hábiles", "um · tramo: Remitir al BCRA, dentro de los diez días hábiles, la notificación y demás documentación recibida, junto con cualquier otro elemento o dato que entienda relevante
- **N2** Sujeto `Sujeto_entidad_financiera` — Entidades financieras · {"nivel": "clase", "alias": ["Entidades financieras emisoras de tarjetas de crédito y/o compra", "Entidad financiera emisora de tarjetas de crédito y/o compra"]} · tramo: 
- **N3** TextoOrdenado `TextoOrdenado_cedin_pdf` — Texto Ordenado CEDIN · {"archivo": "cedin.pdf", "materia": "Certificados de depósitos para la inversión", "version": "Comunicación A 8131 (vigencia 13/11/2024)"} · tramo: 
- **A1** (extraccion) N1 —aplica_a→ N2 · {}
- **E1** (estructural) N1 —establecida_en→ N3 · {}

## 18. `seggar::5.1.5` — NG:sin_raiz · aceptadas:items

Texto que vio E3 (e0, bloque de lista True; págs. 4):

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

Versión: final (grafo sin cola). Nodos 3, aristas 2.
- **N1** Operacion `Operacion_deposito_en_cuenta_sueldo_seguridad_social__seggar_5_1_5_a2047d` — Depósito en cuenta sueldo/seguridad social · {"tipo": "depósito", "descripcion": "Depósito constituido en forma de cuenta sueldo, de la seguridad social o especiales, en pesos o moneda extranjera, en entidades participantes del sistema de garantía"} · tramo: Cuenta sueldo/de la seguridad social y especiales
- **N2** Sujeto `Sujeto_entidad_financiera` — Entidades financieras · {"nivel": "clase", "alias": ["Entidades financieras emisoras de tarjetas de crédito y/o compra", "Entidad financiera emisora de tarjetas de crédito y/o compra"]} · tramo: 
- **N3** TextoOrdenado `TextoOrdenado_seggar_pdf` — Seguro de Depósitos · {"archivo": "seggar.pdf", "materia": "Aplicación del sistema de seguro de garantía de depósitos", "version": "Comunicación A 8407 (vigencia 01/04/2026)"} · tramo: 
- **A1** (extraccion) N1 —aplica_a→ N2 · {}
- **E1** (estructural) N1 —establecida_en→ N3 · {}

## 19. `consyr::3.3.1.1` — NG:sin_raiz · aceptadas:items

Texto que vio E3 (e0, bloque de lista True; págs. 7):

```
[encabezado | punto S3]
3. Régimen de reproducción.
[encabezado | punto 3.3]
3.3. Procedimiento de reproducción.
[encabezado | punto 3.3.1]
3.3.1. Requisitos mínimos.
[intro | punto 3.3.1]
Sin perjuicio de la adopción de otros que juzguen más apropiados a sus necesidades
el proceso de reproducción deberá ajustarse a los siguientes recaudos mínimos:
[texto propio | punto 3.3.1.1]
3.3.1.1. Acta de apertura.
Al momento de procederse a la iniciación del proceso de reproducción de los
documentos originales, se deberá formalizar un acta de apertura del proceso
que contenga los siguientes datos:
i) número de acta de apertura (correlativa en forma diaria desde 01 en
adelante);
ii) fecha de proceso;
iii) cantidad de originales a procesar;
iv) breve descripción de la información contenida en tales originales;
v) denominación y firma responsable de la dependencia remitente de los
originales a procesar;
vi) firma responsable de la recepción de los originales por parte de la de-
pendencia que tiene a su cargo el proceso de reproducción.
```

Versión: final (grafo sin cola). Nodos 4, aristas 5.
- **N1** Condicion `Condicion_iniciacion_del_proceso_de_reproduccion__supuesto_en_que_se_activa_el_deber_de_fo_86e825` — Iniciación del proceso de reproducción · {"descripcion": "Supuesto en que se activa el deber de formalizar el acta de apertura: cuando se procede a la iniciación del proceso de reproducción de documentos originales."} · tramo: Al momento de procederse a la iniciación del proceso de reproducción de los documentos originales
- **N2** Obligacion `Obligacion_deber_de_formalizar_un_acta_de_apertura_del_proceso_de_reproduccion_que_contenga_d90dc7` — Formalizar acta de apertura con datos mínimos · {"tipo": "presentacion_informativa", "descripcion": "Deber de formalizar un acta de apertura del proceso de reproducción que contenga los siguientes datos mínimos: número de acta de apertura (correlativa en forma diaria desde 01 en adelante), fecha de proceso, cantidad de originales a procesar, breve descripción de la información contenida en tales originales, denominación y firma responsable de l · tramo: Al momento de procederse a la iniciación del proceso de reproducción de los documentos originales, se deberá formalizar un acta de apertura del proceso que contenga los siguientes datos
- **N3** Operacion `Operacion_formalizacion_de_acta_de_apertura__consyr_3_3_1_1_e22da4` — Formalización de acta de apertura · {"tipo": "Formalización de acta de apertura", "descripcion": "Formalización de un acta de apertura del proceso de reproducción de documentos originales que contenga datos específicos: número de acta (correlativa diaria desde 01), fecha de proceso, cantidad de originales, descripción de la información contenida, denominación y firma responsable de la dependencia remitente, y firma responsable de la · tramo: se deberá formalizar un acta de apertura del proceso
- **N4** TextoOrdenado `TextoOrdenado_consyr_pdf` — Instrumentación de documentos · {"archivo": "consyr.pdf", "materia": "Instrumentación, conservación y reproducción de documentos", "version": "Comunicación A 6112 (vigencia 01/11/2016)"} · tramo: 
- **A1** (extraccion) N1 —condicion_de→ N2 · {}
- **E1** (estructural) N1 —establecida_en→ N4 · {}
- **A2** (extraccion) N2 —condiciona→ N3 · {}
- **E2** (estructural) N2 —establecida_en→ N4 · {}
- **E3** (estructural) N3 —establecida_en→ N4 · {}

## 20. `cedin::13.2.3` — NG:sin_raiz · aceptadas:items

Texto que vio E3 (e0, bloque de lista True; págs. 16):

```
[encabezado | punto S13]
13. Disposiciones generales.
[intro | punto 13.2]
13.2. Las entidades financieras no podrán percibir cargos, comisiones, ni forma alguna de re-
muneración o recupero de gastos por el desempeño de tareas vinculadas a los CEDIN,
excepto por los siguientes conceptos y valores computados sobre el importe equivalente
en pesos del CEDIN aplicando el tipo de cambio comprador del Banco de la Nación Ar-
gentina vigente a la fecha de cada operación conforme se indica seguidamente:
[texto propio | punto 13.2.3]
13.2.3. Pago: hasta 0,2%.
```

Versión: final (grafo sin cola). Nodos 4, aristas 4.
- **N1** Operacion `Operacion_pago_de_cedin__cedin_13_2_3_ab7285` — Pago de CEDIN · {"tipo": "pago", "descripcion": "Pago por el desempeño de tareas vinculadas a los CEDIN"} · tramo: Pago
- **N2** Restriccion `Restriccion_las_entidades_financieras_no_podran_percibir_comision_por_pago_de_cedin_superior_c992a3` — Límite comisión pago CEDIN · {"tipo": "limite_cuantitativo", "descripcion": "Las entidades financieras no podrán percibir comisión por pago de CEDIN superior al 0,2% del importe equivalente en pesos del CEDIN, aplicando el tipo de cambio comprador del Banco de la Nación Argentina vigente a la fecha de cada operación", "umbrales": [{"tramo": "hasta 0,2%", "valor": "0.2", "unidad": "porcentaje", "comparacion": "maximo_inclusivo · tramo: Pago: hasta 0,2%
- **N3** Sujeto `Sujeto_entidad_financiera` — Entidades financieras · {"nivel": "clase", "alias": ["Entidades financieras emisoras de tarjetas de crédito y/o compra", "Entidad financiera emisora de tarjetas de crédito y/o compra"]} · tramo: 
- **N4** TextoOrdenado `TextoOrdenado_cedin_pdf` — Texto Ordenado CEDIN · {"archivo": "cedin.pdf", "materia": "Certificados de depósitos para la inversión", "version": "Comunicación A 8131 (vigencia 13/11/2024)"} · tramo: 
- **E1** (estructural) N1 —establecida_en→ N4 · {}
- **A1** (extraccion) N2 —aplica_a→ N3 · {}
- **E2** (estructural) N2 —establecida_en→ N4 · {}
- **A2** (extraccion) N2 —limita→ N1 · {}

## 21. `garant::3.1.14.3` — NG:resto · aceptadas:items

Texto que vio E3 (e0, bloque de lista True; págs. 14):

```
[encabezado | punto S3]
Sección 3. Cómputo.
[encabezado | punto 3.1]
3.1. Márgenes de cobertura.
[intro | punto 3.1.14]
3.1.14. Hipoteca en primer grado sobre inmuebles o derechos de superficie, y cualquiera sea su
grado de prelación siempre que la entidad sea la acreedora en todos los grados (punto
1.2.1.):
[texto propio | punto 3.1.14.3]
3.1.14.3. Sobre inmuebles para vivienda propia que sean objeto del gravamen en las
restantes financiaciones: 75 % del valor de tasación del bien.
```

Versión: final (grafo sin cola). Nodos 3, aristas 6.
- **N1** Operacion `Operacion_hipoteca_primer_grado_inmuebles_vivienda_propia__garant_3_1_14_9c4a9d` — Hipoteca primer grado inmuebles vivienda propia · {"tipo": "Hipoteca", "descripcion": "Hipoteca en primer grado sobre inmuebles o derechos de superficie para vivienda propia, con cualquier grado de prelación siempre que la entidad sea la acreedora en todos los grados"} · tramo: Hipoteca en primer grado sobre inmuebles o derechos de superficie, y cualquiera sea su grado de prelación siempre que la entidad sea la acreedora en todos los grados
- **N2** Restriccion `Restriccion_el_margen_de_cobertura_para_hipoteca_sobre_inmuebles_para_vivienda_propia_que_se_1d654c` — Margen cobertura 75% vivienda propia restantes financiaciones · {"tipo": "limite_cuantitativo", "descripcion": "El margen de cobertura para hipoteca sobre inmuebles para vivienda propia que sean objeto del gravamen en las restantes financiaciones es del 75 % del valor de tasación del bien", "umbrales": [{"tramo": "75 % del valor de tasación del bien", "valor": "75", "unidad": "porcentaje", "comparacion": "no_determinada", "base": "valor de tasación del bien",  · tramo: Sobre inmuebles para vivienda propia que sean objeto del gravamen en las restantes financiaciones: 75 % del valor de tasación del bien
- **N3** TextoOrdenado `TextoOrdenado_garant_pdf` — Texto Ordenado de Garantías · {"archivo": "garant.pdf", "materia": "Garantías", "version": "Comunicación A 8447 (vigencia 12/06/2026)"} · tramo: 
- **E1** (estructural) N1 —establecida_en→ N3 · {}
- **R1** (remision_derivada) N1 —remite_a→ Definicion_preferidas_b_hipoteca_primer_grado__garantias_constituidas_por_hipoteca_en_prime_de9e35 · {"alcance": "interna", "destino": "garant::1.2.1", "evidencia": "siempre que la entidad sea la acreedora en todos los grados (punto\n1.2.1.):"}
- **R2** (remision_derivada) N1 —remite_a→ Definicion_preferidas_b_hipotecas_proyectos_inmobiliarios__se_incluyen_en_la_categoria_pref_0b3080 · {"alcance": "interna", "destino": "garant::1.2.1", "evidencia": "siempre que la entidad sea la acreedora en todos los grados (punto\n1.2.1.):"}
- **R3** (remision_derivada) N1 —remite_a→ Definicion_preferidas_b_propiedad_fiduciaria_inmuebles__se_incluyen_en_la_categoria_preferi_c9b368 · {"alcance": "interna", "destino": "garant::1.2.1", "evidencia": "siempre que la entidad sea la acreedora en todos los grados (punto\n1.2.1.):"}
- **E2** (estructural) N2 —establecida_en→ N3 · {}
- **A1** (extraccion) N2 —limita→ N1 · {}

## 22. `snp_spd::5.5.4.3` — NG:resto · aceptadas:items

Texto que vio E3 (e0, bloque de lista True; págs. 18):

```
[encabezado | punto S5]
Sección 5. Servicio de “billetera digital”
[encabezado | punto 5.5]
5.5. Medidas para mitigar el fraude
[intro | punto 5.5.4]
5.5.4. Cuando un pago con tarjeta de débito –sea efectuado en pesos o en dólares
estadounidenses–, de crédito o pregaga se inicie desde una billetera digital
interoperable mediante la lectura de un código QR, la responsabilidad por fraude será
asumida por la billetera, excepto:
[texto propio | punto 5.5.4.3]
5.5.4.3. que exista acuerdo en contrario entre emisores, billeteras y/o
adquirentes/agregadores involucrados en la transacción.
```

Versión: final (grafo sin cola). Nodos 2, aristas 1.
- **N1** Excepcion `Excepcion_excepcion_a_la_responsabilidad_por_fraude_de_la_billetera_digital_cuando_existe__d7e762` — Acuerdo en contrario — responsabilidad por fraude · {"descripcion": "Excepción a la responsabilidad por fraude de la billetera digital cuando existe acuerdo en contrario entre los sujetos intervinientes en la transacción"} · tramo: que exista acuerdo en contrario entre emisores, billeteras y/o adquirentes/agregadores involucrados en la transacción
- **N2** TextoOrdenado `TextoOrdenado_snp_spd_pdf` — Servicios de Pago — Clave Bancaria Uniforme · {"archivo": "snp_spd.pdf", "materia": "Sistema Nacional de Pagos - Servicios de pago", "version": "Comunicación A 8303 (vigencia 03/10/2025)"} · tramo: 
- **E1** (estructural) N1 —establecida_en→ N2 · {}

## 23. `garant::1.1.4` — NG:resto · aceptadas:items

Texto que vio E3 (e0, bloque de lista True; págs. 3):

```
[encabezado | punto S1]
Sección 1. Clases.
[encabezado | punto 1.1]
1.1. Preferidas “A”.
[intro | punto 1.1]
Están constituidas por la cesión o caución de derechos respecto de títulos o documentos de
cualquier naturaleza que, fehacientemente instrumentadas, aseguren que la entidad podrá dis-
poner de los fondos en concepto de cancelación de la obligación contraída por el cliente, sin
necesidad de requerir previamente el pago al deudor dado que la efectivización depende de
terceros solventes o de la existencia de mercados en los cuales puedan liquidarse directamente
los mencionados títulos o documentos, o los efectos que ellos representan, ya sea que el ven-
cimiento de ellos coincida o sea posterior al vencimiento del préstamo o de los pagos periódicos
comprometidos o que el producido sea aplicado a la cancelación de la deuda o transferido di-
rectamente a la entidad a ese fin.
Se incluyen en esta categoría, con el carácter de enumeración taxativa, las siguientes:
[texto propio | punto 1.1.4]
1.1.4. Reembolsos automáticos de operaciones de exportación, a cargo del Banco Central de la
República Argentina (BCRA), conforme a los respectivos regímenes de acuerdos bilate-
rales o multilaterales, cualquiera sea el plazo de la operación.
```

Versión: final (grafo sin cola). Nodos 3, aristas 2.
- **N1** Definicion `Definicion_garantia_preferida_a_reembolsos_automaticos_de_exportacion__incluye_reembolsos_a_8e4135` — Garantía preferida A — reembolsos automáticos de exportación · {"termino": "Garantía preferida A", "descripcion": "Incluye reembolsos automáticos de operaciones de exportación a cargo del BCRA, conforme a los respectivos regímenes de acuerdos bilaterales o multilaterales, sin limitación de plazo"} · tramo: Reembolsos automáticos de operaciones de exportación, a cargo del Banco Central de la República Argentina (BCRA), conforme a los respectivos regímenes de acuerdos bilaterales o multilaterales, cualquiera sea el plazo de la operación
- **N2** Operacion `Operacion_reembolsos_automaticos_de_exportacion_a_cargo_del_bcra__garant_1_1_4_154358` — Reembolsos automáticos de exportación a cargo del BCRA · {"tipo": "Reembolso automático de operación de exportación", "descripcion": "Reembolso automático de operaciones de exportación a cargo del BCRA, conforme a los respectivos regímenes de acuerdos bilaterales o multilaterales, sin limitación de plazo"} · tramo: Reembolsos automáticos de operaciones de exportación, a cargo del Banco Central de la República Argentina (BCRA), conforme a los respectivos regímenes de acuerdos bilaterales o multilaterales, cualquiera sea el plazo de la operación
- **N3** TextoOrdenado `TextoOrdenado_garant_pdf` — Texto Ordenado de Garantías · {"archivo": "garant.pdf", "materia": "Garantías", "version": "Comunicación A 8447 (vigencia 12/06/2026)"} · tramo: 
- **E1** (estructural) N1 —establecida_en→ N3 · {}
- **E2** (estructural) N2 —establecida_en→ N3 · {}

## 24. `raapal::2.1.5` — NG:resto · aceptadas:items

Texto que vio E3 (e0, bloque de lista True; págs. 4, 5):

```
[encabezado | punto S2]
Sección 2. Medida de la exposición.
[encabezado | punto 2.1]
2.1. Criterios generales.
[intro | punto 2.1]
A fin de determinar la medida de la exposición deberá tenerse en cuenta lo siguiente:
[texto propio | punto 2.1.5]
2.1.5. Cuando una entidad financiera sea originante de una titulización –en los términos defini-
dos en el punto 3.1.2.1. de las normas sobre “Capitales mínimos de las entidades finan-
cieras”–, podrá excluir a las exposiciones subyacentes a una titulización tradicional si se
reúnen los requisitos operativos para el reconocimiento de la transferencia del riesgo es-
tablecidos en esas normas –excepto por las posiciones retenidas, que deberán ser in-
cluidas–. En todos los demás casos las exposiciones subyacentes se deberán incluir en
la medida de la exposición de la entidad financiera.
Las entidades deberán prestar atención a las transacciones y productos estructurados
que no capten adecuadamente las fuentes de apalancamiento, tales como operaciones
SFT en las cuales la exposición a la contraparte se incrementa a medida que se deteriora
su calidad crediticia o en las que la calidad crediticia de la contraparte está positivamente
correlacionada con el valor de los títulos valores recibidos en la operación y el uso
de productos estructurados para apartar activos del activo.
Cuando la SEFyC considere que tales operaciones no están siendo adecuadamente
captadas por el ratio de apalancamiento o que podrían dar lugar a un proceso de
desapalancamiento potencialmente desestabilizante, podrá requerir que la entidad adop-
te medidas dirigidas a contrarrestar esas situaciones, tales como introducir mejoras en su
gestión del apalancamiento o que la exposición de que se trate esté adecuadamente ca-
pitalizada a través de un requerimiento de capital adicional, en el marco de las normas
sobre “Lineamientos para la gestión de riesgos en las entidades financieras”.
```

Versión: final (grafo sin cola). Nodos 9, aristas 11.
- **N1** Condicion `Condicion_inadecuada_captura_de_operaciones_en_ratio_de_apalancamiento__la_potestad_de_req_85689d` — Inadecuada captura de operaciones en ratio de apalancamiento · {"descripcion": "La potestad de requerir medidas se activa cuando la SEFyC considere que las operaciones no están siendo adecuadamente captadas por el ratio de apalancamiento o que podrían dar lugar a un proceso de desapalancamiento potencialmente desestabilizante."} · tramo: Cuando la SEFyC considere que tales operaciones no están siendo adecuadamente captadas por el ratio de apalancamiento o que podrían dar lugar a un proceso de desapalancamiento potencialmente desestabilizante
- **N2** Condicion `Condicion_requisitos_operativos_para_transferencia_de_riesgo__la_exclusion_de_exposiciones_f1282e` — Requisitos operativos para transferencia de riesgo · {"descripcion": "La exclusión de exposiciones subyacentes a titulización tradicional se habilita cuando se reúnen los requisitos operativos para el reconocimiento de la transferencia del riesgo establecidos en las normas sobre Capitales mínimos de las entidades financieras."} · tramo: si se reúnen los requisitos operativos para el reconocimiento de la transferencia del riesgo establecidos en esas normas
- **N3** Excepcion `Excepcion_las_posiciones_retenidas_en_una_titulizacion_tradicional_deberan_ser_incluidas_e_68d0d2` — Inclusión de posiciones retenidas en titulización · {"descripcion": "Las posiciones retenidas en una titulización tradicional deberán ser incluidas en la medida de la exposición, no obstante la exclusión de otras exposiciones subyacentes."} · tramo: excepto por las posiciones retenidas, que deberán ser incluidas
- **N4** Obligacion `Obligacion_en_todos_los_demas_casos_cuando_no_se_reunen_los_requisitos_operativos_para_la_t_3d6cdf` — Inclusión de exposiciones subyacentes en demás casos · {"tipo": "asignacion", "descripcion": "En todos los demás casos (cuando no se reúnen los requisitos operativos para la transferencia del riesgo), las exposiciones subyacentes deberán ser incluidas en la medida de la exposición de la entidad financiera."} · tramo: En todos los demás casos las exposiciones subyacentes se deberán incluir en la medida de la exposición de la entidad financiera
- **N5** Obligacion `Obligacion_las_entidades_deberan_prestar_atencion_a_las_transacciones_y_productos_estructur_b564ae` — Atención a transacciones y productos estructurados con apalancamiento · {"tipo": "otra", "descripcion": "Las entidades deberán prestar atención a las transacciones y productos estructurados que no capten adecuadamente las fuentes de apalancamiento, tales como operaciones SFT en las cuales la exposición a la contraparte se incrementa a medida que se deteriora su calidad crediticia o en las que la calidad crediticia de la contraparte está positivamente correlacionada co · tramo: Las entidades deberán prestar atención a las transacciones y productos estructurados que no capten adecuadamente las fuentes de apalancamiento
- **N6** Operacion `Operacion_exclusion_de_exposiciones_subyacentes_a_titulizacion_tradicional__raapal_2_1_5_cfd1bd` — Exclusión de exposiciones subyacentes a titulización tradicional · {"tipo": "exclusión de exposiciones", "descripcion": "Una entidad financiera originante de una titulización podrá excluir las exposiciones subyacentes a una titulización tradicional si se reúnen los requisitos operativos para el reconocimiento de la transferencia del riesgo establecidos en las normas sobre Capitales mínimos, excepto por las posiciones retenidas que deberán ser incluidas."} · tramo: podrá excluir a las exposiciones subyacentes a una titulización tradicional
- **N7** Potestad `Potestad_requerimiento_de_medidas_de_contrarrestacion_por_sefyc__cuando_la_sefyc_consider_309949` — Requerimiento de medidas de contrarrestación por SEFyC · {"descripcion": "Cuando la SEFyC considere que las operaciones no están siendo adecuadamente captadas por el ratio de apalancamiento o que podrían dar lugar a un proceso de desapalancamiento potencialmente desestabilizante, podrá requerir que la entidad adopte medidas dirigidas a contrarrestar esas situaciones, tales como introducir mejoras en su gestión del apalancamiento o que la exposición esté · tramo: podrá requerir que la entidad adopte medidas dirigidas a contrarrestar esas situaciones
- **N8** Sujeto `Sujeto_entidad_financiera` — Entidades financieras · {"nivel": "clase", "alias": ["Entidades financieras emisoras de tarjetas de crédito y/o compra", "Entidad financiera emisora de tarjetas de crédito y/o compra"]} · tramo: 
- **N9** TextoOrdenado `TextoOrdenado_raapal_pdf` — Ratio de apalancamiento · {"archivo": "raapal.pdf", "materia": "Ratio de apalancamiento", "version": "Comunicación A 8109 (vigencia 01/10/2024)"} · tramo: 
- **A1** (extraccion) N1 —condicion_de→ N7 · {}
- **E1** (estructural) N1 —establecida_en→ N9 · {}
- **A2** (extraccion) N2 —condicion_de→ N6 · {}
- **E2** (estructural) N2 —establecida_en→ N9 · {}
- **E3** (estructural) N3 —establecida_en→ N9 · {}
- **A3** (extraccion) N4 —aplica_a→ N8 · {}
- **E4** (estructural) N4 —establecida_en→ N9 · {}
- **A4** (extraccion) N5 —aplica_a→ N8 · {}
- **E5** (estructural) N5 —establecida_en→ N9 · {}
- **E6** (estructural) N6 —establecida_en→ N9 · {}
- **E7** (estructural) N7 —establecida_en→ N9 · {}

## 25. `depinv::1.17.1.1` — NG:resto · aceptadas:items

Texto que vio E3 (e0, bloque de lista True; págs. 14):

```
[encabezado | punto S1]
Sección 1. A plazo fijo.
[encabezado | punto 1.17]
1.17. Prohibiciones.
[encabezado | punto 1.17.1]
1.17.1. No se admitirán depósitos:
[texto propio | punto 1.17.1.1]
1.17.1.1. Constituidos a nombre de otras entidades financieras comprendidas en la Ley
de Entidades Financieras.
```

Versión: final (grafo sin cola). Nodos 3, aristas 2.
- **N1** Restriccion `Restriccion_no_se_admitiran_depositos_constituidos_a_nombre_de_otras_entidades_financieras_c_52cb48` — Prohibición depósitos a nombre de otras entidades financieras · {"tipo": "prohibicion", "descripcion": "No se admitirán depósitos constituidos a nombre de otras entidades financieras comprendidas en la Ley de Entidades Financieras."} · tramo: No se admitirán depósitos: Constituidos a nombre de otras entidades financieras comprendidas en la Ley de Entidades Financieras.
- **N2** Sujeto `Sujeto_entidad_financiera` — Entidades financieras · {"nivel": "clase", "alias": ["Entidades financieras emisoras de tarjetas de crédito y/o compra", "Entidad financiera emisora de tarjetas de crédito y/o compra"]} · tramo: 
- **N3** TextoOrdenado `TextoOrdenado_depinv_pdf` — Depósitos de inversión · {"archivo": "depinv.pdf", "materia": "Depósitos e inversiones a plazo", "version": "Comunicación A 8246 (vigencia 02/06/2025)"} · tramo: 
- **A1** (extraccion) N1 —aplica_a→ N2 · {}
- **E1** (estructural) N1 —establecida_en→ N3 · {}

## 26. `fclef::3.1.2` — NG:resto · aceptadas:items

Texto que vio E3 (e0, bloque de lista True; págs. 6):

```
[encabezado | punto S3]
Sección 3. Obligaciones de los fiduciantes.
[encabezado | punto 3.1]
3.1. Informaciones a suministrar.
[intro | punto 3.1]
Las entidades financieras fiduciantes deberán suministrar a la SEFyC lo siguiente:
[texto propio | punto 3.1.2]
3.1.2. Copia del contrato y modelo de apropiación de previsiones debidamente suscriptos.
```

Versión: final (grafo sin cola). Nodos 3, aristas 2.
- **N1** Obligacion `Obligacion_las_entidades_financieras_fiduciantes_deberan_suministrar_a_la_sefyc_copia_del_c_9246b7` — Suministro de copia de contrato y modelo de apropiación · {"tipo": "presentacion_informativa", "descripcion": "Las entidades financieras fiduciantes deberán suministrar a la SEFyC copia del contrato y modelo de apropiación de previsiones debidamente suscriptos."} · tramo: Las entidades financieras fiduciantes deberán suministrar a la SEFyC lo siguiente: […] Copia del contrato y modelo de apropiación de previsiones debidamente suscriptos.
- **N2** Sujeto `Sujeto_entidad_financiera` — Entidades financieras · {"nivel": "clase", "alias": ["Entidades financieras emisoras de tarjetas de crédito y/o compra", "Entidad financiera emisora de tarjetas de crédito y/o compra"]} · tramo: 
- **N3** TextoOrdenado `TextoOrdenado_fclef_pdf` — Texto Ordenado Fideicomisos Financieros · {"archivo": "fclef.pdf", "materia": "Fideicomisos financieros comprendidos en la Ley de Entidades Financieras", "version": "Comunicación A 6303 (vigencia 23/08/2017)"} · tramo: 
- **A1** (extraccion) N1 —aplica_a→ N2 · {}
- **E1** (estructural) N1 —establecida_en→ N3 · {}

## 27. `snp_psp::5.1.2.4` — NG:resto · aceptadas:items

Texto que vio E3 (e0, bloque de lista True; págs. 17):

```
[encabezado | punto S5]
Sección 5. Proveedores de servicios de pago que cumplen la función de aceptación
[encabezado | punto 5.1.2]
5.1.2. La siguiente información:
[texto propio | punto 5.1.2.4]
5.1.2.4. Listado de los proveedores que prestan servicios de tecnología informática, sis-
temas y de seguridad de la información.
```

Versión: final (grafo sin cola). Nodos 3, aristas 2.
- **N1** Obligacion `Obligacion_presentar_listado_de_los_proveedores_que_prestan_servicios_de_tecnologia_informa_2bb80e` — Presentar listado de proveedores de tecnología · {"descripcion": "Presentar listado de los proveedores que prestan servicios de tecnología informática, sistemas y de seguridad de la información", "tipo": "presentacion_informativa"} · tramo: Listado de los proveedores que prestan servicios de tecnología informática, sistemas y de seguridad de la información
- **N2** Sujeto `Sujeto_rol_alcance_snp_psp` — Sujetos alcanzados (SNP - Proveedores de servicios de pago) · {"nivel": "rol"} · tramo: 
- **N3** TextoOrdenado `TextoOrdenado_snp_psp_pdf` — SNP - Proveedores de servicios de pago · {"archivo": "snp_psp.pdf", "materia": "Proveedores de servicios de pago", "version": "Comunicación A 8454 (vigencia 15/07/2026)"} · tramo: 
- **A1** (extraccion) N1 —aplica_a→ N2 · {}
- **E1** (estructural) N1 —establecida_en→ N3 · {}

## 28. `opecam::2.5.2` — NG:resto · aceptadas:items

Texto que vio E3 (e0, bloque de lista True; págs. 12):

```
[encabezado | punto S2]
Sección 2. Inscripción en el “Registro de operadores de cambio”.
[encabezado | punto 2.5]
2.5. Impedimentos.
[intro | punto 2.5]
No podrán ser principales integrantes del órgano de gobierno, ni integrar los órganos de admi-
nistración y fiscalización de casas o agencias de cambio, ni ser responsable del cumplimiento
de la normativa cambiaria, quienes se encuentren comprendidos en alguna de las siguientes si-
tuaciones:
[texto propio | punto 2.5.2]
2.5.2. los condenados por delitos contra la propiedad o contra la administración pública o con-
tra la fe pública;
```

Versión: final (grafo sin cola). Nodos 4, aristas 3.
- **N1** Restriccion `Restriccion_no_podran_ser_principales_integrantes_del_organo_de_gobierno_ni_integrar_los_org_559119` — Impedimento condenados por delitos contra propiedad, administración pública o fe pública · {"tipo": "prohibicion", "descripcion": "No podrán ser principales integrantes del órgano de gobierno, ni integrar los órganos de administración y fiscalización de casas o agencias de cambio, ni ser responsable del cumplimiento de la normativa cambiaria, quienes se encuentren condenados por delitos contra la propiedad o contra la administración pública o contra la fe pública"} · tramo: los condenados por delitos contra la propiedad o contra la administración pública o contra la fe pública
- **N2** Sujeto `Sujeto_agencia_de_cambio` — Agencias de cambio · {"nivel": "clase"} · tramo: 
- **N3** Sujeto `Sujeto_casa_de_cambio` — Casas de cambio · {"nivel": "clase"} · tramo: 
- **N4** TextoOrdenado `TextoOrdenado_opecam_pdf` — Operadores de cambio · {"archivo": "opecam.pdf", "materia": "Operadores de cambio", "version": "Comunicación A 8219 (vigencia 21/03/2025)"} · tramo: 
- **A1** (extraccion) N1 —aplica_a→ N2 · {}
- **A2** (extraccion) N1 —aplica_a→ N3 · {}
- **E1** (estructural) N1 —establecida_en→ N4 · {}

## 29. `graloc::5.3.6.2` — NG:resto · aceptadas:items

Texto que vio E3 (e0, bloque de lista True; págs. 20):

```
[encabezado | punto S5]
Sección 5. Riesgo de liquidez.
[encabezado | punto 5.3]
5.3. Marco para la gestión del riesgo de liquidez.
[encabezado | punto 5.3.6]
5.3.6. Una evaluación de los riesgos asociados con la liquidación de las operaciones de cam-
bio a través de un banco corresponsal (de ser ese el caso).
[intro | punto 5.3.6]
Las entidades deben:
[texto propio | punto 5.3.6.2]
5.3.6.2. Reconocer que las alteraciones operativas o financieras de su banco corres-
ponsal podrían generar alteraciones en su gestión de liquidez.
```

Versión: final (grafo sin cola). Nodos 5, aristas 5.
- **N1** Condicion `Condicion_alteraciones_operativas_o_financieras_del_corresponsal__supuesto_en_que_se_verif_5abc11` — Alteraciones operativas o financieras del corresponsal · {"descripcion": "supuesto en que se verifica que el banco corresponsal experimenta alteraciones operativas o financieras"} · tramo: las alteraciones operativas o financieras de su banco corresponsal
- **N2** Obligacion `Obligacion_las_entidades_deben_reconocer_que_las_alteraciones_operativas_o_financieras_de_s_0fb360` — Reconocer riesgos de alteraciones del corresponsal en gestión de liquidez · {"tipo": "otra", "descripcion": "las entidades deben reconocer que las alteraciones operativas o financieras de su banco corresponsal podrían generar alteraciones en su gestión de liquidez"} · tramo: Reconocer que las alteraciones operativas o financieras de su banco corresponsal podrían generar alteraciones en su gestión de liquidez
- **N3** Operacion `Operacion_alteraciones_operativas_o_financieras_de_banco_corresponsal__graloc_5_3_6_2_ba1c1f` — Alteraciones operativas o financieras de banco corresponsal · {"tipo": "alteración de condiciones de banco corresponsal", "descripcion": "cambios operativos o financieros que pueden ocurrir en el banco corresponsal utilizado por la entidad para la liquidación de operaciones de cambio"} · tramo: alteraciones operativas o financieras de su banco corresponsal
- **N4** Sujeto `Sujeto_entidad_financiera` — Entidades financieras · {"nivel": "clase", "alias": ["Entidades financieras emisoras de tarjetas de crédito y/o compra", "Entidad financiera emisora de tarjetas de crédito y/o compra"]} · tramo: 
- **N5** TextoOrdenado `TextoOrdenado_graloc_pdf` — Gestión de riesgos en operaciones de cambio · {"archivo": "graloc.pdf", "materia": "Gestión de riesgos asociados a la liquidación de operaciones de cambio", "version": "Comunicación A 6762 (vigencia 23/08/2019)"} · tramo: 
- **A1** (extraccion) N1 —condicion_de→ N2 · {}
- **E1** (estructural) N1 —establecida_en→ N5 · {}
- **A2** (extraccion) N2 —aplica_a→ N4 · {}
- **E2** (estructural) N2 —establecida_en→ N5 · {}
- **E3** (estructural) N3 —establecida_en→ N5 · {}

## 30. `snp_spd::5.5.2.1` — NG:resto · aceptadas:items

Texto que vio E3 (e0, bloque de lista True; págs. 17):

```
[encabezado | punto S5]
Sección 5. Servicio de “billetera digital”
[encabezado | punto 5.5]
5.5. Medidas para mitigar el fraude
[intro | punto 5.5.2]
5.5.2. Las entidades financieras y los PSPCP que brindan el servicio de billetera digital,
deberán cumplir con los siguientes recaudos:
[texto propio | punto 5.5.2.1]
5.5.2.1. Verificar la identidad de las personas que requieren la apertura de una cuenta
de pago, observando a ese efecto las disposiciones para entidades financieras
del punto 1.3. de las normas sobre “Depósitos de ahorro, cuenta sueldo y
especiales” (excepto lo requerido en su último párrafo, en relación con la
declaración jurada del cliente) y concordantes –puntos 4.1., 4.2. y 4.16.1.–.
```

Versión: final (grafo sin cola). Nodos 6, aristas 15.
- **N1** Excepcion `Excepcion_no_aplica_el_requisito_de_declaracion_jurada_del_cliente_establecido_en_el_ultim_2ecd2c` — Excepción — declaración jurada del cliente · {"descripcion": "No aplica el requisito de declaración jurada del cliente establecido en el último párrafo del punto 1.3. de las normas sobre Depósitos de ahorro, cuenta sueldo y especiales"} · tramo: excepto lo requerido en su último párrafo, en relación con la declaración jurada del cliente
- **N2** Obligacion `Obligacion_las_entidades_financieras_y_los_pspcp_que_brindan_el_servicio_de_billetera_digit_7026a1` — Deber de verificar identidad — apertura de cuenta de pago · {"tipo": "otra", "descripcion": "Las entidades financieras y los PSPCP que brindan el servicio de billetera digital deberán verificar la identidad de las personas que requieren la apertura de una cuenta de pago, observando las disposiciones para entidades financieras del punto 1.3. de las normas sobre Depósitos de ahorro, cuenta sueldo y especiales (excepto lo requerido en su último párrafo, en re · tramo: deberán cumplir con los siguientes recaudos: […] Verificar la identidad de las personas que requieren la apertura de una cuenta de pago
- **N3** Operacion `Operacion_verificacion_de_identidad_apertura_de_cuenta_de_pago__snp_spd_5_5_2_1_d12d7b` — Verificación de identidad — apertura de cuenta de pago · {"tipo": "Verificación de identidad", "descripcion": "Verificar la identidad de las personas que requieren la apertura de una cuenta de pago, observando las disposiciones para entidades financieras del punto 1.3. de las normas sobre Depósitos de ahorro, cuenta sueldo y especiales (excepto lo requerido en su último párrafo, en relación con la declaración jurada del cliente) y concordantes (puntos 4 · tramo: Verificar la identidad de las personas que requieren la apertura de una cuenta de pago
- **N4** Sujeto `Sujeto_entidad_financiera` — Entidades financieras · {"nivel": "clase", "alias": ["Entidades financieras emisoras de tarjetas de crédito y/o compra", "Entidad financiera emisora de tarjetas de crédito y/o compra"]} · tramo: 
- **N5** Sujeto `Sujeto_pspcp` — Proveedores de servicios de pago que ofrecen cuentas de pago (PSPCP) · {"nivel": "clase", "alias": ["PSPCP"]} · tramo: 
- **N6** TextoOrdenado `TextoOrdenado_snp_spd_pdf` — Servicios de Pago — Clave Bancaria Uniforme · {"archivo": "snp_spd.pdf", "materia": "Sistema Nacional de Pagos - Servicios de pago", "version": "Comunicación A 8303 (vigencia 03/10/2025)"} · tramo: 
- **E1** (estructural) N1 —establecida_en→ N6 · {}
- **A1** (extraccion) N1 —exceptua_obligacion→ N2 · {}
- **A2** (extraccion) N2 —aplica_a→ N4 · {}
- **A3** (extraccion) N2 —aplica_a→ N5 · {}
- **E2** (estructural) N2 —establecida_en→ N6 · {}
- **A4** (extraccion) N2 —regula→ N3 · {}
- **R1** (remision_derivada) N2 —remite_a→ Obligacion_las_entidades_financieras_deben_habilitar_codigos_qr_regidos_por_los_estandares__92e0f1 · {"alcance": "interna", "destino": "snp_spd::4.2", "evidencia": "relación con la\ndeclaración jurada del cliente) y concordantes –puntos 4.1., 4.2. y 4.16.1.–."}
- **R2** (remision_derivada) N2 —remite_a→ Obligacion_los_pspcp_deben_habilitar_codigos_qr_regidos_por_los_estandares_del_bcra_para_cu_d3eaab · {"alcance": "interna", "destino": "snp_spd::4.2", "evidencia": "relación con la\ndeclaración jurada del cliente) y concordantes –puntos 4.1., 4.2. y 4.16.1.–."}
- **R3** (remision_derivada) N2 —remite_a→ Operacion_habilitacion_de_codigos_qr_para_cuentas_corrientes__snp_spd_4_2_06334d · {"alcance": "interna", "destino": "snp_spd::4.2", "evidencia": "relación con la\ndeclaración jurada del cliente) y concordantes –puntos 4.1., 4.2. y 4.16.1.–."}
- **R4** (remision_derivada) N2 —remite_a→ Operacion_habilitacion_de_codigos_qr_para_cuentas_de_pago__snp_spd_4_2_bbd9e1 · {"alcance": "interna", "destino": "snp_spd::4.2", "evidencia": "relación con la\ndeclaración jurada del cliente) y concordantes –puntos 4.1., 4.2. y 4.16.1.–."}
- **E3** (estructural) N3 —establecida_en→ N6 · {}
- **R5** (remision_derivada) N3 —remite_a→ Obligacion_las_entidades_financieras_deben_habilitar_codigos_qr_regidos_por_los_estandares__92e0f1 · {"alcance": "interna", "destino": "snp_spd::4.2", "evidencia": "relación con la\ndeclaración jurada del cliente) y concordantes –puntos 4.1., 4.2. y 4.16.1.–."}
- **R6** (remision_derivada) N3 —remite_a→ Obligacion_los_pspcp_deben_habilitar_codigos_qr_regidos_por_los_estandares_del_bcra_para_cu_d3eaab · {"alcance": "interna", "destino": "snp_spd::4.2", "evidencia": "relación con la\ndeclaración jurada del cliente) y concordantes –puntos 4.1., 4.2. y 4.16.1.–."}
- **R7** (remision_derivada) N3 —remite_a→ Operacion_habilitacion_de_codigos_qr_para_cuentas_corrientes__snp_spd_4_2_06334d · {"alcance": "interna", "destino": "snp_spd::4.2", "evidencia": "relación con la\ndeclaración jurada del cliente) y concordantes –puntos 4.1., 4.2. y 4.16.1.–."}
- **R8** (remision_derivada) N3 —remite_a→ Operacion_habilitacion_de_codigos_qr_para_cuentas_de_pago__snp_spd_4_2_bbd9e1 · {"alcance": "interna", "destino": "snp_spd::4.2", "evidencia": "relación con la\ndeclaración jurada del cliente) y concordantes –puntos 4.1., 4.2. y 4.16.1.–."}

