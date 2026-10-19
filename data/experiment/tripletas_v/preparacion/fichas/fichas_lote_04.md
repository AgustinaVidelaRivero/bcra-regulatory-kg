# U-TRIP-V: fichas del lote 04 (10)

Acta del sorteo `acta_sorteo_V.json` (sha256 `5d6a237e510bcf086db717061dd146eaa9b3181006cb7b1d300164436c720c55`), sellada a las 2026-10-19T14:23:55-03:00; fichas generadas a las 2026-10-19T14:25:19-03:00. Grafo KG-Tanda0-Desarrollo-r2b-sincola-rs1 (`66e745f5…`). Las fichas van en el orden sellado. Criterio (§3.4 del pre-registro): la evidencia sostiene la relación entre esos dos nodos, con sus sujetos, valores, calificadores y modalidad.

Cada ficha trae los dos nodos (tipo, etiqueta, descripción y propiedades), el predicado y la evidencia de cada procedencia: el texto heredado y el propio de la unidad de E0, el tramo literal de cada extremo en esa unidad si lo hay, las páginas y la ruta del PDF con la página. «literal» dice si el tramo está tal cual en el texto (exacta), por tokens (tokens) o no (no).

## V041 · `condicion_de` · lote_04, 1 de 10

**Origen** — Condicion «Convalidación de la imputación por la entidad» (`Condicion_convalidacion_de_la_imputacion_por_la_entidad__la_imputacion_debe_haber_sido_con_ce7457`)

- descripción: La imputación debe haber sido convalidada por parte de la entidad.

**Predicado** — `condicion_de`

**Destino** — Obligacion «Reporte al BCRA de cumplimiento de seguimiento» (`Obligacion_la_entidad_debera_reportar_al_bcra_el_cumplimiento_parcial_o_total_del_seguimien_8fffa6`)

- descripción: La entidad deberá reportar al BCRA el cumplimiento parcial o total del seguimiento de un permiso de embarque dentro de los 5 (cinco) días hábiles de convalidada la imputación por parte de ella.
- tipo: reporte_al_supervisor
- umbrales (1):
  - valor: 5; unidad: dias; comparacion: maximo_inclusivo; dias_tipo: habiles; tramo: dentro de los 5 (cinco) días hábiles

**Evidencia 1 de 1** — `ext::8.4.3::cierre` · ext · punto 8.4.3 · bloque_cierre · págs. 110

- PDF: `data/experiment/subset/TO_exterior_cambios_actual.pdf#page=110`

> *heredado (encabezado, S8, p. 108):* Sección 8. Seguimiento de las negociaciones de divisas por exportaciones de bienes
>
> *heredado (encabezado, 8.4, p. 109):* 8.4. Responsabilidades de la entidad nominada para el seguimiento del permiso.
>
> *heredado (encabezado, 8.4.3, p. 110):* 8.4.3. Registro de las imputaciones al seguimiento del permiso.
>
> *propio:* Cuando se considere parcial o totalmente cumplimentado el seguimiento de un permiso de embarque por aplicaciones y/o por las situaciones consideradas en el punto 8.5., la entidad deberá reportarlo al BCRA dentro de los 5 (cinco) días hábiles de convalidada la imputación por parte de ella.

- tramo del origen: «de convalidada la imputación por parte de ella» (literal: exacta)
- tramo del destino: «la entidad deberá reportarlo al BCRA dentro de los 5 (cinco) días hábiles de convalidada la imputación por parte de ella» (literal: exacta)

---

## V042 · `aplica_a` · lote_04, 2 de 10

**Origen** — Potestad «Precancelación líneas crédito — facultad acceso mercado cambios» (`Potestad_precancelacion_lineas_credito_facultad_acceso_mercado_cambios__las_entidades_fin_120e59`)

- descripción: Las entidades financieras podrán acceder al mercado de cambios para precancelar líneas de crédito en la medida que la financiación otorgada por la entidad local haya sido precancelada por el deudor.

**Predicado** — `aplica_a`

- tramo del sujeto: «Las entidades financieras» (literal: exacta)

**Destino** — Sujeto «Entidades financieras» (`Sujeto_entidad_financiera`)

- descripción: —
- nivel: clase
- alias: ["Entidades financieras emisoras de tarjetas de crédito y/o compra", "Entidad financiera emisora de tarjetas de crédito y/o compra"]

**Evidencia 1 de 1** — `ext::3.15.1` · ext · punto 3.15.1 · punto_propio · págs. 41

- PDF: `data/experiment/subset/TO_exterior_cambios_actual.pdf#page=41`

> *heredado (encabezado, S3, p. 16):* Sección 3. Disposiciones específicas para los egresos por el mercado de cambios
>
> *heredado (chapeau_seccion, S3, p. 16):* Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–, adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables.
>
> *heredado (encabezado, 3.15, p. 41):* 3.15. Cancelación por parte de entidades financieras de líneas de crédito del exterior aplicadas a la
>
> *heredado (intro, 3.15, p. 41):* financiación de operaciones de comercio exterior y garantías financieras otorgadas.
>
> *propio:* 3.15.1. Cancelación de líneas de crédito del exterior aplicadas por las entidades a la financiación de operaciones de comercio exterior. Las entidades financieras tendrán acceso al mercado de cambios a partir del vencimiento para la cancelación de líneas de crédito otorgadas por entidades financieras del exterior y aplicadas a la financiación de operaciones de exportación o importación de residentes. La cancelación de las líneas destinadas a la financiación de operaciones de importación de bienes y servicios quedará adicionalmente alcanzada por las condiciones específicas previstas en los puntos 10.7. y 13.6., respectivamente. También podrán acceder para precancelar dichas líneas de crédito en la medida que la financiación otorgada por la entidad local haya sido precancelada por el deudor. El acceso al mercado de cambios por parte de los clientes para la precancelación de estas financiaciones requerirá la conformidad previa del BCRA. La entidad deberá contar con la validación de la declaración del “Relevamiento de activos y pasivos externos” de la entidad, en la medida que sea aplicable.

- tramo del origen: «También podrán acceder para precancelar dichas líneas de crédito en la medida que la financiación otorgada por la entidad local haya sido precancelada por el deudor» (literal: exacta)
- tramo del destino: —

---

## V043 · `regula` · lote_04, 3 de 10

**Origen** — Obligacion «Revisión trimestral mínima — clasificación de deudores» (`Obligacion_deber_de_efectuar_la_revision_de_clasificacion_de_deudores_con_periodicidad_mini_4c2549`)

- descripción: Deber de efectuar la revisión de clasificación de deudores con periodicidad mínima trimestral, respecto de clientes individuales cuyas financiaciones sean equivalentes al 5 % o más de la RPC o del activo del fideicomiso financiero del mes anterior al cierre del trimestre; dejar constancia en el legajo del cliente analizado
- tipo: otra
- umbrales (2):
  - comparacion: no_determinada; tramo: cada trimestre calendario
  - valor: 5; unidad: porcentaje; comparacion: minimo_inclusivo; tramo: 5 % o más de la RPC o del activo del fideicomiso financiero

**Predicado** — `regula`

**Destino** — Operacion «Clasificación trimestral de clientes — cartera comercial» (`Operacion_clasificacion_trimestral_de_clientes_cartera_comercial__cla_6_3_1_4b0e52`)

- descripción: Revisión y clasificación de clientes individuales cuyas financiaciones alcancen el 5 % o más de la RPC o del activo del fideicomiso financiero del mes anterior al cierre del trimestre; el grupo de contrapartes conectadas se trata como un solo cliente
- tipo: clasificación de deudores

**Evidencia 1 de 1** — `cla::6.3.1` · cla · punto 6.3.1 · punto_propio · págs. 18

- PDF: `data/experiment/subset/TO_clasificacion_deudores_actual.pdf#page=18`

> *heredado (encabezado, S6, p. 17):* Sección 6. Clasificación de los deudores de la cartera comercial.
>
> *heredado (encabezado, 6.3, p. 17):* 6.3. Periodicidad mínima de clasificación.
>
> *heredado (intro, 6.3, p. 17):* La revisión deberá efectuarse como mínimo con la periodicidad que se indica seguidamente, dejando constancia de ello en el legajo del cliente analizado:
>
> *propio:* 6.3.1. En el curso de cada trimestre calendario, respecto de clientes individualmente considera- dos cuyas financiaciones comprendidas en algún momento sean equivalentes al 5 % o más de la RPC o del activo del fideicomiso financiero del mes anterior a la finalización de dicho período según se trate de entidades o fideicomisos financieros, respectivamente. A estos fines, el grupo de contrapartes conectadas se tratará como un solo cliente.

- tramo del origen: «La revisión deberá efectuarse como mínimo con la periodicidad que se indica seguidamente […] En el curso de cada trimestre calendario, respecto de clientes individualmente considerados cuyas financiaciones comprendidas en algún momento sean equivalentes al 5 % o más de la RPC o del activo del fideicomiso financiero del mes anterior a la finalización de dicho período según se trate de entidades o fideicomisos financieros, respectivamente» (literal: exacta)
- tramo del destino: «En el curso de cada trimestre calendario, respecto de clientes individualmente considerados cuyas financiaciones comprendidas en algún momento sean equivalentes al 5 % o más de la RPC o del activo del fideicomiso financiero del mes anterior a la finalización de dicho período según se trate de entidades o fideicomisos financieros, respectivamente» (literal: exacta)

---

## V044 · `condicion_de` · lote_04, 4 de 10

**Origen** — Condicion «Existencia de más de dos calificaciones» (`Condicion_existencia_de_mas_de_dos_calificaciones__la_exposicion_cuenta_con_mas_de_dos_cal_286adc`)

- descripción: La exposición cuenta con más de dos calificaciones crediticias.
- umbrales (1):
  - comparacion: minimo_estricto; tramo: más de dos calificaciones

**Predicado** — `condicion_de`

**Destino** — Operacion «Selección de calificaciones — múltiples ECAI» (`Operacion_seleccion_de_calificaciones_multiples_ecai__cap_10_3_2_3_cf14e9`)

- descripción: Cuando para una exposición existan más de dos calificaciones crediticias, se utilizarán aquellas que correspondan a los dos menores ponderadores de riesgo.
- tipo: Selección de calificaciones crediticias

**Evidencia 1 de 1** — `cap::10.3.2.3` · cap · punto 10.3.2.3 · punto_propio · págs. 174

- PDF: `data/experiment/subset/TO_capitales_minimos_actual.pdf#page=174`

> *heredado (encabezado, S10, p. 172):* Sección 10. Agentes de calificación externa (ECAI).
>
> *heredado (encabezado, 10.3, p. 173):* 10.3. Consideraciones para su implementación.
>
> *heredado (encabezado, 10.3.2, p. 174):* 10.3.2. Tratamiento para múltiples calificaciones.
>
> *propio:* 10.3.2.3. Cuando para una exposición existan más de dos calificaciones crediticias se utilizarán aquellas que correspondan a los dos menores ponderadores de riesgo, debiéndose aplicar de ambos el mayor.

- tramo del origen: «Cuando para una exposición existan más de dos calificaciones crediticias» (literal: exacta)
- tramo del destino: «Cuando para una exposición existan más de dos calificaciones crediticias se utilizarán aquellas que correspondan a los dos menores ponderadores de riesgo» (literal: exacta)

---

## V045 · `condiciona` · lote_04, 5 de 10

**Origen** — Obligacion «Efectuar consultas a través de entidad autorizada» (`Obligacion_las_consultas_o_pedidos_de_conformidad_previa_por_operaciones_en_el_mercado_de_c_91a84f`)

- descripción: Las consultas o pedidos de conformidad previa por operaciones en el mercado de cambios deben efectuarse a través de una entidad autorizada a cursar el tipo de operación contenida en la consulta
- tipo: otra

**Predicado** — `condiciona`

**Destino** — Operacion «Consulta o pedido de conformidad previa — operaciones en mercado de cambios» (`Operacion_consulta_o_pedido_de_conformidad_previa_operaciones_en_mercado_de_cambios__ext_1_b27b34`)

- descripción: Consultas o pedidos de conformidad previa que realizan los clientes por operaciones a cursar en el mercado de cambios
- tipo: Consulta o pedido de conformidad previa

**Evidencia 1 de 1** — `ext::1.8` · ext · punto 1.8 · punto_propio · págs. 7

- PDF: `data/experiment/subset/TO_exterior_cambios_actual.pdf#page=7`

> *heredado (encabezado, S1, p. 7):* Sección 1. Disposiciones generales.
>
> *propio:* 1.8. Las distintas consultas o pedidos de conformidad previa que realicen los clientes por operaciones a cursar en el mercado de cambios deberán indefectiblemente efectuarse a través de una entidad que esté autorizada a cursar el tipo de operación contenida en ella. Las presentaciones de las entidades deberán ser realizadas en la mesa de entrada del BCRA, dirigidas a la Gerencia Principal de Exterior y Cambios. En las presentaciones deberá constar un análisis de la entidad interviniente del encuadre de la operación, la nota original del cliente y los datos necesarios para identificar la operación y poder proceder a su análisis de acuerdo con el tipo de consulta o pedido que se realiza, acompañando la documentación que entienda relevante para el análisis de lo solicitado.

- tramo del origen: «Las distintas consultas o pedidos de conformidad previa que realicen los clientes por operaciones a cursar en el mercado de cambios deberán indefectiblemente efectuarse a través de una entidad que esté autorizada a cursar el tipo de operación contenida en ella» (literal: exacta)
- tramo del destino: «consultas o pedidos de conformidad previa que realicen los clientes por operaciones a cursar en el mercado de cambios» (literal: exacta)

---

## V046 · `condicion_de` · lote_04, 6 de 10

**Origen** — Condicion «Utilización para pagar deudas comerciales por importación» (`Condicion_utilizacion_para_pagar_deudas_comerciales_por_importacion__el_endeudamiento_debe_1b02c1`)

- descripción: El endeudamiento debe haber sido utilizado para pagar deudas comerciales derivadas de la importación de bienes y servicios

**Predicado** — `condicion_de`

**Destino** — Excepcion «Excepción — conformidad previa BCRA no requerida» (`Excepcion_exceptua_el_requisito_de_conformidad_previa_del_bcra_para_el_acceso_al_mercado_d_0e351b`)

- descripción: Exceptúa el requisito de conformidad previa del BCRA para el acceso al mercado de cambios para la cancelación de capital e intereses de endeudamientos financieros cuando se cumplen todas las condiciones enumeradas: endeudamiento comprendido en punto 3.5., vida promedio no inferior a 2 años, liquidado entre 27/08/21 y 12/12/23, utilizado para pagar deudas comerciales por importación de bienes y servicios, y emitida Certificación conforme Com. A 7348
- umbrales (1):
  - valor: 2; unidad: anios; comparacion: minimo_inclusivo; tramo: 2 años

**Evidencia 1 de 1** — `ext::3.5.6.10` · ext · punto 3.5.6.10 · punto_propio · págs. 27

- PDF: `data/experiment/subset/TO_exterior_cambios_actual.pdf#page=27`

> *heredado (encabezado, S3, p. 16):* Sección 3. Disposiciones específicas para los egresos por el mercado de cambios
>
> *heredado (chapeau_seccion, S3, p. 16):* Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–, adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables.
>
> *heredado (encabezado, 3.5, p. 20):* 3.5. Pagos de títulos de deuda suscriptos en el exterior y endeudamientos financieros con el
>
> *heredado (intro, 3.5, p. 20):* exterior. Las entidades podrán dar acceso al mercado de cambios para realizar pagos de capital o intereses de títulos de deuda con registro público en el exterior, otros endeudamientos financieros con el exterior y títulos de deuda con registro público en el país denominados en moneda extranjera íntegramente suscriptos en el exterior, en la medida que se verifiquen las siguientes condiciones:
>
> *heredado (encabezado, 3.5.6, p. 26):* 3.5.6. Se requerirá la conformidad previa del BCRA para el acceso al mercado de cambios
>
> *heredado (intro, 3.5.6, p. 26):* para la cancelación de capital e intereses de endeudamientos financieros comprendidos en este punto 3.5. cuando el acreedor sea una contraparte vinculada al deudor. Este requisito no resultará aplicable cuando la operación encuadre en alguna de las siguientes situaciones:
>
> *heredado (cierre, 3.5.6, p. 27):* Las deudas comprendidas en este punto continuarán sujetas a la conformidad previa aun cuando existiese una modificación del acreedor o del deudor que conlleve a que ya no exista una vinculación entre el acreedor y el deudor residente.
>
> *propio:* 3.5.6.10. se trate de un endeudamiento financiero comprendido en este punto 3.5. con una vida promedio no inferior a los 2 (dos) años liquidado entre el 27/08/21 y el 12/12/23 y que fue utilizado para pagar deudas comerciales por la importación de bienes y servicios a partir de la emisión de una “Certificación de ingreso de nuevo endeudamiento financiero con el exterior” en el marco del punto 1. de la Comunicación A 7348 y concordantes (disposiciones receptadas oportunamente en el punto 3.19. del Anexo de la Comunicación A 7914).

- tramo del origen: «que fue utilizado para pagar deudas comerciales por la importación de bienes y servicios» (literal: exacta)
- tramo del destino: «se trate de un endeudamiento financiero comprendido en este punto 3.5. con una vida promedio no inferior a los 2 (dos) años liquidado entre el 27/08/21 y el 12/12/23 y que fue utilizado para pagar deudas comerciales por la importación de bienes y servicios a partir de la emisión de una "Certificación de ingreso de nuevo endeudamiento financiero con el exterior" en el marco del punto 1. de la Comunicación A 7348 y concordantes» (literal: exacta)

---

## V047 · `limita` · lote_04, 7 de 10

**Origen** — Restriccion «Exigencia de capital — titulización con exclusión incompleta» (`Restriccion_las_operaciones_de_titulizacion_que_incluyan_una_opcion_de_exclusion_que_no_cump_03ec35`)

- descripción: Las operaciones de titulización que incluyan una opción de exclusión que no cumpla la totalidad de los criterios indicados precedentemente resultarán en una exigencia de capital para la entidad originante
- tipo: limite_cuantitativo

**Predicado** — `limita`

**Destino** — Operacion «Titulización con opción de exclusión incompleta» (`Operacion_titulizacion_con_opcion_de_exclusion_incompleta__cap_3_1_4_53aace`)

- descripción: Operación de titulización que incluye una opción de exclusión que no cumple la totalidad de los criterios indicados precedentemente
- tipo: titulización

**Evidencia 1 de 1** — `cap::3.1.4::cierre` · cap · punto 3.1.4 · bloque_cierre · págs. 34, 35

- PDF: `data/experiment/subset/TO_capitales_minimos_actual.pdf#page=34` · `data/experiment/subset/TO_capitales_minimos_actual.pdf#page=35`

> *heredado (encabezado, S3, p. 29):* Sección 3. Capital mínimo por riesgo de crédito. Titulizaciones e inversiones en fon- dos.
>
> *heredado (encabezado, 3.1, p. 29):* 3.1. Tratamiento de las titulizaciones.
>
> *heredado (encabezado, 3.1.4, p. 34):* 3.1.4. Tratamiento de las opciones de exclusión.
>
> *propio:* Todas aquellas operaciones de titulización que incluyan una opción de exclusión que no cumpla la totalidad de los criterios indicados precedentemente resultarán en una exigen- cia de capital para la entidad originante. En el caso de titulizaciones tradicionales, las exposiciones subyacentes se tratarán como si no estuviesen titulizadas. Además, la entidad financiera deberá deducir del capital or- dinario de nivel uno (CO ) el importe total en concepto de ganancia por venta resultante n1 de la operación de titulización, de acuerdo con lo establecido en el punto 8.4.1.17. En el caso de titulizaciones sintéticas, la entidad que adquiera protección deberá mante- ner capital frente al total de las posiciones titulizadas, como si no gozaran de ningún tipo de protección crediticia. Si una operación de titulización sintética incorporara cualquier otra opción (distinta de la opción de exclusión) que ponga fin efectivo en una fecha dada, tanto a la operación como a la protección crediticia adquirida, la entidad aplicará a dicha operación el tratamiento recogido en el punto 3.1.13.3. Si una opción de exclusión, tras haber sido ejercida, ha servido de mejora crediticia, el ejercicio de dicha opción se considerará como un respaldo crediticio implícito –es decir, no contemplado contractualmente– y recibirá el tratamiento establecido en el punto 3.1.5.2.

- tramo del origen: «resultarán en una exigencia de capital para la entidad originante» (literal: exacta)
- tramo del destino: «operaciones de titulización que incluyan una opción de exclusión que no cumpla la totalidad de los criterios indicados precedentemente» (literal: exacta)

---

## V048 · `aplica_a` · lote_04, 8 de 10

**Origen** — Potestad «Facultad de dar acceso a pagos diferidos» (`Potestad_facultad_de_dar_acceso_a_pagos_diferidos__las_entidades_tienen_la_facultad_de_da_7dacfc`)

- descripción: Las entidades tienen la facultad de dar acceso al mercado de cambios para cursar pagos diferidos de importaciones de bienes con registro de ingreso aduanero a partir del 13/12/23

**Predicado** — `aplica_a`

- tramo del sujeto: «Las entidades» (literal: exacta)

**Destino** — Sujeto «Entidades autorizadas a operar en cambios (Exterior)» (`Sujeto_rol_entidad_autorizada_exterior`)

- descripción: —
- nivel: rol

**Evidencia 1 de 1** — `ext::10.10.1` · ext · punto 10.10.1 · punto_propio · págs. 154

- PDF: `data/experiment/subset/TO_exterior_cambios_actual.pdf#page=154`

> *heredado (encabezado, S10, p. 130):* Sección 10. Pagos de importaciones y otras compras de bienes en el exterior.
>
> *heredado (encabezado, 10.10, p. 154):* 10.10. Disposiciones complementarias para importaciones de bienes que tuvieron o tendrán registro
>
> *heredado (intro, 10.10, p. 154):* de ingreso aduanero a partir del 13/12/23.
>
> *propio:* 10.10.1. Plazos para pagos diferidos de importaciones de bienes con registro de ingreso aduanero a partir del 13/12/23. Las entidades podrán dar acceso al mercado de cambios para cursar pagos diferidos de importaciones de bienes con registro de ingreso aduanero a partir del 13/12/23 desde la fecha de registro de ingreso aduanero, en la medida que se trate de operaciones no comprendidas en el punto 10.6.6. y se verifiquen los restantes requisitos normativos aplicables.

- tramo del origen: «Las entidades podrán dar acceso al mercado de cambios para cursar pagos diferidos de importaciones de bienes con registro de ingreso aduanero a partir del 13/12/23» (literal: exacta)
- tramo del destino: —

---

## V049 · `condiciona` · lote_04, 9 de 10

**Origen** — Obligacion «Cumplimiento del seguimiento — exportación Decreto 929/13» (`Obligacion_la_entidad_podra_considerar_cumplimentado_el_seguimiento_de_un_permiso_de_embarq_06c05f`)

- descripción: La entidad podrá considerar cumplimentado el seguimiento de un permiso de embarque por la parte amparada por un Certificado DECRETO 929/13 emitido conforme a la Resolución 26/23 de la Secretaría de Energía
- tipo: otra
- modalidad (no definida en el esquema): podrá considerar

**Predicado** — `condiciona`

**Destino** — Operacion «Exportación amparada por Decreto 929/13» (`Operacion_exportacion_amparada_por_decreto_929_13__ext_8_5_22_47c08d`)

- descripción: Exportación de un cliente con proyecto incluido en el Régimen de Promoción de Inversión para la Explotación de Hidrocarburos (Decreto 929/13), amparada por un Certificado DECRETO 929/13 emitido conforme a la Resolución 26/23 de la Secretaría de Energía
- tipo: Exportación con beneficios cambiarios

**Evidencia 1 de 1** — `ext::8.5.22` · ext · punto 8.5.22 · punto_propio · págs. 122

- PDF: `data/experiment/subset/TO_exterior_cambios_actual.pdf#page=122`

> *heredado (encabezado, S8, p. 108):* Sección 8. Seguimiento de las negociaciones de divisas por exportaciones de bienes
>
> *heredado (encabezado, 8.5, p. 112):* 8.5. Otras imputaciones admitidas en el cumplimiento del seguimiento.
>
> *heredado (intro, 8.5, p. 112):* La entidad podrá considerar cumplimentado parcial o totalmente el seguimiento de un permiso de embarque cuando cuente con los elementos que le permitan considerar que la operación se encuentra en alguna de las situaciones detalladas a continuación y se verifiquen las condiciones previstas en cada caso. La documentación utilizada para certificar el concepto y monto de las divisas imputado en cada caso deberá quedar archivada en la entidad a disposición del BCRA.
>
> *propio:* 8.5.22. Exportación alcanzada por los beneficios cambiarios del Régimen de Promoción de Inversión para la Explotación de Hidrocarburos (Decreto 929/13). A pedido de un cliente que posea un proyecto incluido en el Régimen de Promoción de Inversión para la Explotación de Hidrocarburos establecido por el Decreto 929/13, la entidad podrá considerar cumplimentado el seguimiento de un permiso de embarque por la parte del permiso que se encuentre amparado por un “Certificado DECRETO 929/13” emitido a partir de lo dispuesto por la Resolución 26/23 de la Secretaría de Energía.

- tramo del origen: «la entidad podrá considerar cumplimentado el seguimiento de un permiso de embarque por la parte del permiso que se encuentre amparado por un "Certificado DECRETO 929/13" emitido a partir de lo dispuesto por la Resolución 26/23 de la Secretaría de Energía» (literal: exacta)
- tramo del destino: «Exportación alcanzada por los beneficios cambiarios del Régimen de Promoción de Inversión para la Explotación de Hidrocarburos (Decreto 929/13)» (literal: exacta)

---

## V050 · `aplica_a` · lote_04, 10 de 10

**Origen** — Obligacion «Origen real, directo y demostrable de comisiones y cargos» (`Obligacion_las_comisiones_cargos_costos_gastos_seguros_y_otros_conceptos_excluyendo_tasa_de_4e09d5`)

- descripción: Las comisiones, cargos, costos, gastos, seguros y otros conceptos (excluyendo tasa de interés) que los sujetos obligados perciban o pretendan percibir de los usuarios deben tener origen en un costo real, directo y demostrable y estar debidamente justificados desde el punto de vista técnico y económico.
- tipo: otra

**Predicado** — `aplica_a`

- tramo del sujeto: «los sujetos obligados» (literal: exacta)

**Destino** — Sujeto «Sujetos obligados (Protección de usuarios)» (`Sujeto_rol_sujeto_obligado_proteccion`)

- descripción: —
- nivel: rol

**Evidencia 1 de 1** — `pro::2.3.2.1` · pro · punto 2.3.2.1 · punto_propio · págs. 11, 12

- PDF: `data/experiment/subset/TO_proteccion_usuarios_servicios_financieros_actual.pdf#page=11` · `data/experiment/subset/TO_proteccion_usuarios_servicios_financieros_actual.pdf#page=12`

> *heredado (encabezado, S2, p. 5):* Sección 2. Derechos básicos de los usuarios de servicios financieros.
>
> *heredado (encabezado, 2.3, p. 7):* 2.3. Recaudos mínimos de la relación de consumo.
>
> *heredado (encabezado, 2.3.2, p. 11):* 2.3.2. Comisiones y cargos.
>
> *propio:* 2.3.2.1. Admitidos. Todas las comisiones, cargos, costos, gastos, seguros y/o cualquier otro con- cepto –excluyendo la tasa de interés– que los sujetos obligados perciban o pre- tendan percibir de los usuarios de servicios financieros (comisiones y cargos), deben tener origen en un costo real, directo y demostrable y estar debidamente justificados desde el punto de vista técnico y económico. La aplicación de comisiones y/o cargos debe quedar circunscripta a la efectiva prestación de un servicio que haya sido previamente solicitado, pactado y/o au- torizado por el usuario. Las comisiones obedecen a servicios que prestan los sujetos obligados y, en tal sentido, pueden incluir retribuciones a su favor que excedan el costo de la prestación. Los cargos obedecen a servicios que prestan terceros, por lo que solamente pueden ser transferidos al costo a los usuarios. Asimismo, el importe de los cargos que el sujeto obligado transfiera a los usua- rios no podrá ser superior al que el tercero prestador perciba de particulares, sin intermediarios y en similares condiciones (servicios postales, compañía de seguros, escribanía y registros de propiedad, u otros de índole similar). En las operaciones de crédito, los sujetos obligados podrán aplicar comisiones sobre los importes no utilizados de los acuerdos de asignación de fondos, dado que su puesta a disposición a los usuarios configura la prestación del servicio. La precancelación total o parcial de financiaciones podrá dar lugar a la aplica- ción de comisiones. En el caso de precancelación total, no se admitirá la apli- cación de comisiones cuando al momento de efectuarla haya transcurrido al menos la cuarta parte del plazo original de la financiación o 180 días corridos desde su otorgamiento, de ambos el mayor. Además, será de aplicación lo previsto en el punto 1.7. del TO sobre Tasas de Interés en las Operaciones de Crédito.

- tramo del origen: «todas las comisiones, cargos, costos, gastos, seguros y/o cualquier otro concepto –excluyendo la tasa de interés– que los sujetos obligados perciban o pretendan percibir de los usuarios de servicios financieros (comisiones y cargos), deben tener origen en un costo real, directo y demostrable y estar debidamente justificados desde el punto de vista técnico y económico» (literal: exacta)
- tramo del destino: —

---

