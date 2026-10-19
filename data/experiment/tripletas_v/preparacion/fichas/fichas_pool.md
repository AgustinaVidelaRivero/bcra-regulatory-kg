# U-TRIP-V: fichas del pool de calibración (20)

Acta del sorteo `acta_sorteo_V.json` (sha256 `5d6a237e510bcf086db717061dd146eaa9b3181006cb7b1d300164436c720c55`), sellada a las 2026-10-19T14:23:55-03:00; fichas generadas a las 2026-10-19T14:25:19-03:00. Grafo KG-Tanda0-Desarrollo-r2b-sincola-rs1 (`66e745f5…`). Las fichas van en el orden sellado. Criterio (§3.4 del pre-registro): la evidencia sostiene la relación entre esos dos nodos, con sus sujetos, valores, calificadores y modalidad.

Cada ficha trae los dos nodos (tipo, etiqueta, descripción y propiedades), el predicado y la evidencia de cada procedencia: el texto heredado y el propio de la unidad de E0, el tramo literal de cada extremo en esa unidad si lo hay, las páginas y la ruta del PDF con la página. «literal» dice si el tramo está tal cual en el texto (exacta), por tokens (tokens) o no (no).

## P01 · `aplica_a` · pool, 1 de 20

**Origen** — Obligacion «Convalidación de operación en sistema online BCRA» (`Obligacion_contar_con_la_convalidacion_de_la_situacion_de_la_operacion_en_el_sistema_online_7c4f5d`)

- descripción: contar con la convalidación de la situación de la operación en el sistema online implementado por el BCRA al momento de dar acceso al mercado de cambios
- tipo: otra

**Predicado** — `aplica_a`

- tramo del sujeto: «la entidad» (literal: exacta)

**Destino** — Sujeto «Entidades autorizadas a operar en cambios (Exterior)» (`Sujeto_rol_entidad_autorizada_exterior`)

- descripción: —
- nivel: rol

**Evidencia 1 de 1** — `ext::13.1.5` · ext · punto 13.1.5 · punto_propio · págs. 168

- PDF: `data/experiment/subset/TO_exterior_cambios_actual.pdf#page=168`

> *heredado (encabezado, S13, p. 168):* Sección 13. Pagos de servicios prestados por no residentes.
>
> *heredado (encabezado, 13.1, p. 168):* 13.1. Disposiciones generales.
>
> *heredado (intro, 13.1, p. 168):* Las entidades podrán dar acceso al mercado de cambios por pagos de servicios prestados por no residentes en la medida que se cumplan las siguientes condiciones:
>
> *heredado (cierre, 13.1, p. 168):* Los casos que no encuadren en lo expuesto precedentemente quedan sujetos a la conformidad previa del BCRA, debiendo los pedidos ser canalizados por una entidad autorizada a realizar este tipo de pagos.
>
> *propio:* 13.1.5. En todos los casos la entidad deberá, al momento de dar acceso al mercado de cambios, contar con la convalidación de la situación de la operación en el sistema online implementado por el BCRA a tales efectos.

- tramo del origen: «la entidad deberá, al momento de dar acceso al mercado de cambios, contar con la convalidación de la situación de la operación en el sistema online implementado por el BCRA a tales efectos» (literal: exacta)
- tramo del destino: —

---

## P02 · `regula` · pool, 2 de 20

**Origen** — Obligacion «Revisión semestral — clientes entre 1% y 5% RPC» (`Obligacion_deber_de_efectuar_la_revision_de_clientes_individualmente_considerados_cuyas_fin_dbef28`)

- descripción: Deber de efectuar la revisión de clientes individualmente considerados cuyas financiaciones comprendidas sumen entre el 1% (o el equivalente a dos veces el importe de referencia del punto 3.7., el menor de ambos) y menos del 5% de la RPC o del activo del fideicomiso financiero del mes anterior a la finalización del semestre calendario, dejando constancia en el legajo del cliente analizado. El grupo de contrapartes conectadas se trata como un solo cliente.
- tipo: presentacion_informativa
- frecuencia: cada semestre calendario
- umbrales (3):
  - valor: 1; unidad: porcentaje; comparacion: no_determinada; tramo: entre el 1 % –o el equivalente a dos veces el importe de referencia establecido en el punto 3.7., de ambos el menor– y menos del 5 %
  - valor: 2; unidad: veces; comparacion: no_determinada; base: importe de referencia establecido en el punto 3.7.; base_destino: cla::3.7; tramo: entre el 1 % –o el equivalente a dos veces el importe de referencia establecido en el punto 3.7., de ambos el menor– y menos del 5 %
  - valor: 5; unidad: porcentaje; comparacion: maximo_estricto; tramo: entre el 1 % –o el equivalente a dos veces el importe de referencia establecido en el punto 3.7., de ambos el menor– y menos del 5 %

**Predicado** — `regula`

**Destino** — Operacion «Revisión de clientes semestral — cartera comercial» (`Operacion_revision_de_clientes_semestral_cartera_comercial__cla_6_3_2_fc45a0`)

- descripción: Revisión de clientes individualmente considerados cuyas financiaciones comprendidas sumen entre el 1% (o el equivalente a dos veces el importe de referencia del punto 3.7., el menor de ambos) y menos del 5% de la RPC o del activo del fideicomiso financiero del mes anterior a la finalización del semestre calendario. El grupo de contrapartes conectadas se trata como un solo cliente.
- tipo: Clasificación de deudores

**Evidencia 1 de 1** — `cla::6.3.2` · cla · punto 6.3.2 · punto_propio · págs. 18

- PDF: `data/experiment/subset/TO_clasificacion_deudores_actual.pdf#page=18`

> *heredado (encabezado, S6, p. 17):* Sección 6. Clasificación de los deudores de la cartera comercial.
>
> *heredado (encabezado, 6.3, p. 17):* 6.3. Periodicidad mínima de clasificación.
>
> *heredado (intro, 6.3, p. 17):* La revisión deberá efectuarse como mínimo con la periodicidad que se indica seguidamente, dejando constancia de ello en el legajo del cliente analizado:
>
> *propio:* 6.3.2. En el curso de cada semestre calendario, respecto de clientes individualmente conside- rados cuyas financiaciones comprendidas sumen en algún momento entre el 1 % –o el equivalente a dos veces el importe de referencia establecido en el punto 3.7., de ambos el menor– y menos del 5 % de la RPC o del activo del fideicomiso financiero del mes an- terior a la finalización de dicho período según se trate de entidades o fideicomisos finan- cieros, respectivamente. A estos fines, el grupo de contrapartes conectadas se tratará como un solo cliente. Al cierre del primer semestre calendario, el examen deberá haber alcanzado no menos del 50 % del importe total de la cartera comercial comprendida, computando los clientes a que se refiere el punto 6.3.1., por lo que, de ser necesario para llegar a ese valor, se completará con la revisión de clientes cuyas financiaciones comprendidas sean inferiores al 1 % de la citada RPC o del activo del fideicomiso financiero, o del equivalente a dos veces el importe de referencia establecido en el punto 3.7., siguiendo un orden decre- ciente en función de su magnitud.

- tramo del origen: «La revisión deberá efectuarse como mínimo con la periodicidad que se indica seguidamente […] En el curso de cada semestre calendario, respecto de clientes individualmente considerados cuyas financiaciones comprendidas sumen en algún momento entre el 1 % –o el equivalente a dos veces el importe de referencia establecido en el punto 3.7., de ambos el menor– y menos del 5 % de la RPC o del activo del fideicomiso financiero del mes anterior a la finalización de dicho período según se trate de entidades o fideicomisos financieros, respectivamente» (literal: exacta)
- tramo del destino: «En el curso de cada semestre calendario, respecto de clientes individualmente considerados cuyas financiaciones comprendidas sumen en algún momento entre el 1 % –o el equivalente a dos veces el importe de referencia establecido en el punto 3.7., de ambos el menor– y menos del 5 % de la RPC o del activo del fideicomiso financiero del mes anterior a la finalización de dicho período según se trate de entidades o fideicomisos financieros, respectivamente» (literal: exacta)

---

## P03 · `aplica_a` · pool, 3 de 20

**Origen** — Obligacion «Documentación montos gastos colocación» (`Obligacion_la_entidad_debe_contar_con_documentacion_de_la_cual_surjan_los_montos_correspond_d544ff`)

- descripción: La entidad debe contar con documentación de la cual surjan los montos correspondientes a los gastos de colocación de bienes en el exterior
- tipo: presentacion_informativa

**Predicado** — `aplica_a`

- tramo del sujeto: «la entidad» (literal: exacta)

**Destino** — Sujeto «Entidades autorizadas a operar en cambios (Exterior)» (`Sujeto_rol_entidad_autorizada_exterior`)

- descripción: —
- nivel: rol

**Evidencia 1 de 1** — `ext::8.5.12` · ext · punto 8.5.12 · punto_propio · págs. 116

- PDF: `data/experiment/subset/TO_exterior_cambios_actual.pdf#page=116`

> *heredado (encabezado, S8, p. 108):* Sección 8. Seguimiento de las negociaciones de divisas por exportaciones de bienes
>
> *heredado (encabezado, 8.5, p. 112):* 8.5. Otras imputaciones admitidas en el cumplimiento del seguimiento.
>
> *heredado (intro, 8.5, p. 112):* La entidad podrá considerar cumplimentado parcial o totalmente el seguimiento de un permiso de embarque cuando cuente con los elementos que le permitan considerar que la operación se encuentra en alguna de las situaciones detalladas a continuación y se verifiquen las condiciones previstas en cada caso. La documentación utilizada para certificar el concepto y monto de las divisas imputado en cada caso deberá quedar archivada en la entidad a disposición del BCRA.
>
> *propio:* 8.5.12. Gastos relacionados con la colocación de los bienes en el exterior y no incorporados en el permiso de embarque. Por el valor de los gastos directamente relacionados con la colocación de los bienes en el exterior y que no estaban determinados a la fecha de embarque de los bienes, tales como gastos por promociones comerciales y descuentos debitados por el importador acorde a los usos y costumbres de colocación del producto exportado en el país de destino, en la medida que la entidad cuente con la declaración jurada del exportador respecto al carácter genuino de la operación y con la documentación de la cual surjan los montos correspondientes. En la medida que el monto a imputar al permiso por este mecanismo supere el equivalente a USD 25.000 (dólares estadounidenses veinticinco mil), la entidad deberá contar con una certificación de auditor externo en la cual se deje constancia que lo declarado por el exportador resulta consistente con la información que surge de la revisión de los registros contables, extracontables y toda otra documentación adicional aportada.

- tramo del origen: «con la documentación de la cual surjan los montos correspondientes» (literal: exacta)
- tramo del destino: —

---

## P04 · `requiere` · pool, 4 de 20

**Origen** — Operacion «Repatriación inversión directa — reducción capital/devolución aportes» (`Operacion_repatriacion_inversion_directa_reduccion_capital_devolucion_aportes__ext_3_13_1_bde0a6`)

- descripción: Repatriación de inversión directa de no residentes que consiste en una reducción de capital y/o devolución de aportes irrevocables realizadas por la empresa local
- tipo: Repatriación de inversión directa

**Predicado** — `requiere`

**Destino** — Obligacion «Contar con documentación de cumplimiento de mecanismos legales» (`Obligacion_la_entidad_debera_contar_con_la_documentacion_que_demuestre_que_se_han_cumplimen_11b675`)

- descripción: La entidad deberá contar con la documentación que demuestre que se han cumplimentado los mecanismos legales previstos para la reducción de capital y/o devolución de aportes irrevocables
- tipo: presentacion_informativa

**Evidencia 1 de 1** — `ext::3.13.1::cierre` · ext · punto 3.13.1 · bloque_cierre · págs. 39

- PDF: `data/experiment/subset/TO_exterior_cambios_actual.pdf#page=39`

> *heredado (encabezado, S3, p. 16):* Sección 3. Disposiciones específicas para los egresos por el mercado de cambios
>
> *heredado (encabezado, 3.13, p. 36):* 3.13. Repatriaciones de inversiones directas y otras compras de moneda extranjera por parte de no
>
> *heredado (encabezado, 3.13.1, p. 36):* 3.13.1. El acceso al mercado de cambios para la repatriación de inversiones de no
>
> *propio:* Si una repatriación de una inversión directa de no residentes consiste en una reducción de capital y/o devolución de aportes irrevocables realizadas por la empresa local, adicionalmente a los requisitos previstos en cada caso, la entidad deberá contar con la documentación que demuestre que se han cumplimentado los mecanismos legales previstos y haber verificado que se encuentra declarada, en caso de corresponder, en la última presentación vencida del “Relevamiento de activos y pasivos externos” el pasivo en pesos con el exterior generado a partir de la fecha de la no aceptación del aporte irrevocable o de la reducción de capital según corresponda.

- tramo del origen: «repatriación de una inversión directa de no residentes consiste en una reducción de capital y/o devolución de aportes irrevocables» (literal: exacta)
- tramo del destino: «la entidad deberá contar con la documentación que demuestre que se han cumplimentado los mecanismos legales previstos» (literal: exacta)

---

## P05 · `condicion_de` · pool, 5 de 20

**Origen** — Condicion «Condición: no se hayan registrado aplicaciones de divisas» (`Condicion_condicion_no_se_hayan_registrado_aplicaciones_de_divisas__la_modificacion_de_la__d32ea3`)

- descripción: La modificación de la entidad responsable solo es posible si no se han registrado aplicaciones de divisas a la cancelación de la operación.

**Predicado** — `condicion_de`

**Destino** — Potestad «Modificación de entidad responsable por exportador» (`Potestad_modificacion_de_entidad_responsable_por_exportador__el_exportador_puede_modifica_0ff47a`)

- descripción: El exportador puede modificar la entidad responsable del seguimiento posteriormente, siempre que no se hayan registrado aplicaciones de divisas a la cancelación de la operación.

**Evidencia 1 de 1** — `ext::9.2` · ext · punto 9.2 · punto_propio · págs. 123, 124

- PDF: `data/experiment/subset/TO_exterior_cambios_actual.pdf#page=123` · `data/experiment/subset/TO_exterior_cambios_actual.pdf#page=124`

> *heredado (encabezado, S9, p. 123):* Sección 9. Seguimiento de anticipos y otras financiaciones de exportación de bienes.
>
> *propio:* 9.2. Entidad nominada por el exportador. Por cada operación comprendida el exportador deberá seleccionar una entidad como responsable de su seguimiento. Esta entidad será la única responsable de emitir los certificados de aplicación que habilitan que los cobros de exportaciones puedan ser imputados a los permisos correspondientes. En el caso de financiaciones otorgadas por entidades financieras locales, el seguimiento estará a cargo de la entidad que otorgó la financiación hasta su cancelación total. Para las operaciones comprendidas en los puntos 9.1.6. y 9.1.7. el seguimiento quedará a cargo de la entidad nominada en cumplimiento a lo establecido en los puntos 7.9. o 7.10. En el caso de las operaciones comprendidas en el punto 9.1.8. el seguimiento quedará a cargo de la entidad que, a pedido del exportador y luego de verificar el cumplimiento de los requisitos previstos en el punto 7.11., realizó el registro de la operación ante el BCRA. En los restantes casos, el seguimiento quedará inicialmente a cargo de la entidad que dé curso a la liquidación por el mercado de cambios, pudiendo el exportador modificarla posteriormente en la medida que no se hayan registrado aplicaciones de divisas a la cancelación de ésta. En caso de que el exportador solicite el cambio, la entidad a cargo del seguimiento deberá notificarle la voluntad del exportador a la nueva entidad. La constancia de aceptación por parte de esta última liberará a la entidad previa de sus obligaciones hacia adelante.

- tramo del origen: «en la medida que no se hayan registrado aplicaciones de divisas a la cancelación de ésta» (literal: exacta)
- tramo del destino: «pudiendo el exportador modificarla posteriormente en la medida que no se hayan registrado aplicaciones de divisas a la cancelación de ésta» (literal: exacta)

---

## P06 · `aplica_a` · pool, 6 de 20

**Origen** — Obligacion «Deber asignar ponderador riesgo exposiciones moneda extranjera» (`Obligacion_las_entidades_financieras_del_grupo_1_deberan_asignar_a_las_exposiciones_denomin_b6df32`)

- descripción: Las entidades financieras del grupo 1 deberán asignar a las exposiciones denominadas en moneda distinta a la de los ingresos de sus contrapartes (en los casos de exposiciones minoristas sin cobertura del riesgo de crédito de la Sección 5 y de exposiciones con garantía hipotecaria sobre inmuebles residenciales) un ponderador de riesgo del 150% o el que resulte de multiplicar por 1,5 el ponderador que le correspondería según las presentes disposiciones, el mayor de ambos.
- tipo: asignacion
- umbrales (2):
  - comparacion: no_determinada; tramo: multiplicar por 1,5
  - valor: 150; unidad: porcentaje; comparacion: coeficiente; tramo: 150%

**Predicado** — `aplica_a`

- calificacion (de la arista, no definida en el esquema): grupo 1 (D-SIB o G-SIB)
- tramo del sujeto: «Las entidades financieras del grupo 1» (literal: exacta)

**Destino** — Sujeto «Entidades financieras» (`Sujeto_entidad_financiera`)

- descripción: —
- nivel: clase
- alias: ["Entidades financieras emisoras de tarjetas de crédito y/o compra", "Entidad financiera emisora de tarjetas de crédito y/o compra"]

**Evidencia 1 de 1** — `cap::2.5.3` · cap · punto 2.5.3 · punto_propio · págs. 11

- PDF: `data/experiment/subset/TO_capitales_minimos_actual.pdf#page=11`

> *heredado (encabezado, S2, p. 7):* Sección 2. Capital mínimo por riesgo de crédito.
>
> *heredado (chapeau_seccion, S2, p. 7):* A los efectos de la aplicación de las disposiciones de la presente sección, las entidades financieras se clasificarán en: i)Grupo 1: entidades calificadas por el BCRA como de importancia sistémica a nivel local
>
> *heredado (chapeau_seccion, S2, p. 7):* (D-SIB) y sucursales o subsidiarias de bancos del exterior calificados como de impor- tancia sistémica global (G-SIB).
>
> *heredado (chapeau_seccion, S2, p. 7):* ii) Grupo 2: entidades financieras no comprendidas en el acápite i). En aquellos casos en que no se establezcan disposiciones específicas para cada uno de los citados grupos de entidades financieras, deberá aplicarse el mismo tratamiento a ambos grupos. Las entidades financieras que presenten cambios en su calificación –conforme a lo previsto en los acápites precedentes–, contarán con un plazo de 6 meses para aplicar las disposiciones específicas correspondientes al nuevo grupo al que pertenezcan.
>
> *heredado (encabezado, 2.5, p. 11):* 2.5. Criterios para la determinación de los activos ponderados por riesgo.
>
> *propio:* 2.5.3. Las entidades financieras del grupo 1 deberán asignar a las exposiciones denominadas en una moneda distinta a la de los ingresos de sus contrapartes –en los casos de expo- siciones minoristas sin cobertura del riesgo de crédito de la Sección 5. y de exposiciones con garantía hipotecaria sobre inmuebles residenciales– un ponderador de riesgo del 150% o el que resulte de multiplicar por 1,5 el ponderador que le correspondería según las presentes disposiciones, el mayor de ambos.

- tramo del origen: «Las entidades financieras del grupo 1 deberán asignar a las exposiciones denominadas en una moneda distinta a la de los ingresos de sus contrapartes –en los casos de exposiciones minoristas sin cobertura del riesgo de crédito de la Sección 5. y de exposiciones con garantía hipotecaria sobre inmuebles residenciales– un ponderador de riesgo del 150% o el que resulte de multiplicar por 1,5 el ponderador que le correspondería según las presentes disposiciones, el mayor de ambos» (literal: exacta)
- tramo del destino: —

---

## P07 · `condicion_de` · pool, 7 de 20

**Origen** — Condicion «Oferta y comercialización de productos con contratos de adhesión» (`Condicion_oferta_y_comercializacion_de_productos_con_contratos_de_adhesion__la_obligacion__19f101`)

- descripción: La obligación de informar comisiones y cargos aplica cuando las entidades ofrezcan y comercialicen productos y/o servicios que se perfeccionan con contratos de adhesión.

**Predicado** — `condicion_de`

**Destino** — Obligacion «Informar comisiones y cargos al BCRA» (`Obligacion_las_entidades_financieras_pspcp_empresas_no_financieras_emisoras_de_tarjetas_de__e8ed9d`)

- descripción: Las entidades financieras, PSPCP, empresas no financieras emisoras de tarjetas de crédito y/o compra y otros proveedores no financieros de crédito que ofrezcan y comercialicen productos y/o servicios que se perfeccionan con contratos de adhesión deberán informar las comisiones y cargos que cobren a los usuarios de servicios financieros mediante el régimen informativo establecido al efecto.
- tipo: reporte_al_supervisor

**Evidencia 1 de 1** — `pro::2.5` · pro · punto 2.5 · punto_propio · págs. 21

- PDF: `data/experiment/subset/TO_proteccion_usuarios_servicios_financieros_actual.pdf#page=21`

> *heredado (encabezado, S2, p. 5):* Sección 2. Derechos básicos de los usuarios de servicios financieros.
>
> *propio:* 2.5. Información al Banco Central de la República Argentina. Las entidades financieras, los PSPCP, las empresas no financieras emisoras de tarjetas de crédito y/o compra y los otros proveedores no financieros de crédito que ofrezcan y comerciali- cen productos y/o servicios que se perfeccionan con la firma o aceptación de contratos con cláusulas preestablecidas (contratos de adhesión), deberán informar las comisiones y cargos que cobren a los usuarios de servicios financieros mediante el régimen informativo establecido al efecto. Las altas –comisiones de nuevos productos y/o servicios que deseen comercializar– y los au- mentos en las comisiones que deseen implementar deberán ser previamente informados al BCRA por la vía consignada en el párrafo precedente y luego ser notificadas a los usuarios de servicios financieros. También deberán informar las modificaciones de los cargos. Las reducciones en las comisiones y/o cargos podrán aplicarse sin demora, sin perjuicio de que deberán ser informadas al BCRA dentro de los treinta (30) días corridos siguientes de su apli- cación.

- tramo del origen: «que ofrezcan y comercialicen productos y/o servicios que se perfeccionan con la firma o aceptación de contratos con cláusulas preestablecidas (contratos de adhesión)» (literal: exacta)
- tramo del destino: «deberán informar las comisiones y cargos que cobren a los usuarios de servicios financieros mediante el régimen informativo establecido al efecto» (literal: exacta)

---

## P08 · `limita` · pool, 8 de 20

**Origen** — Restriccion «Ponderador 50% — calificación BBB+ hasta BBB-» (`Restriccion_ponderador_de_riesgo_del_50_para_exposiciones_a_otros_estados_soberanos_o_sus_ba_382920`)

- descripción: Ponderador de riesgo del 50% para exposiciones a otros estados soberanos o sus bancos centrales con calificación BBB+ hasta BBB-
- tipo: limite_cuantitativo
- umbrales (1):
  - valor: 50; unidad: porcentaje; comparacion: coeficiente; tramo: 50%

**Predicado** — `limita`

**Destino** — Operacion «Exposición a otros estados soberanos o sus bancos centrales» (`Operacion_exposicion_a_otros_estados_soberanos_o_sus_bancos_centrales__cap_2_12_2_5_55b981`)

- descripción: Exposición a otros estados soberanos o sus bancos centrales, sujeta a ponderación de riesgo según calificación crediticia
- tipo: Exposición crediticia

**Evidencia 1 de 1** — `cap::2.12.2.5` · cap · punto 2.12.2.5 · punto_propio · págs. 23

- PDF: `data/experiment/subset/TO_capitales_minimos_actual.pdf#page=23`
- avisos de E0: {"contenido_tabular": true, "tablas_e0": [{"tabla": "cap::tabla2f001", "origen": "r_tc2", "estado": "parseada", "paginas": [23], "serializada": true, "bloque": "cap::tabla2f001", "modo": "columnas", "celdas_propagadas": 0, "celdas_con_alcance": 0, "combinadas_sin_propagar": 0, "filas_subtitulo": 0}]}

> *heredado (encabezado, S2, p. 7):* Sección 2. Capital mínimo por riesgo de crédito.
>
> *heredado (chapeau_seccion, S2, p. 7):* A los efectos de la aplicación de las disposiciones de la presente sección, las entidades financieras se clasificarán en: i)Grupo 1: entidades calificadas por el BCRA como de importancia sistémica a nivel local
>
> *heredado (chapeau_seccion, S2, p. 7):* (D-SIB) y sucursales o subsidiarias de bancos del exterior calificados como de impor- tancia sistémica global (G-SIB).
>
> *heredado (chapeau_seccion, S2, p. 7):* ii) Grupo 2: entidades financieras no comprendidas en el acápite i). En aquellos casos en que no se establezcan disposiciones específicas para cada uno de los citados grupos de entidades financieras, deberá aplicarse el mismo tratamiento a ambos grupos. Las entidades financieras que presenten cambios en su calificación –conforme a lo previsto en los acápites precedentes–, contarán con un plazo de 6 meses para aplicar las disposiciones específicas correspondientes al nuevo grupo al que pertenezcan.
>
> *heredado (encabezado, 2.12, p. 22):* 2.12. Tabla de ponderadores de riesgo.
>
> *heredado (intro, 2.12, p. 22):* Concepto Ponderador
>
> *heredado (intro, 2.12, p. 22):* –en %–
>
> *heredado (encabezado, 2.12.2, p. 23):* 2.12.2. Exposición a gobiernos y bancos centrales.
>
> *propio:* 2.12.2.5. A otros estados soberanos (o sus bancos centrales). [TABLA cap::tabla2f001 | página 23 | R-TC2 | columnas] Columnas: Calificación | AAA hasta AA- | A+ hasta A- | BBB+ hasta BBB- | BB+ hasta B- | Inferior a B- | No calificado Fila 1: Calificación = Ponderador de riesgo | AAA hasta AA- = 0% | A+ hasta A- = 20% | BBB+ hasta BBB- = 50% | BB+ hasta B- = 100% | Inferior a B- = 150% | No calificado = 100% [FIN TABLA cap::tabla2f001]

- tramo del origen: «BBB+ hasta BBB- = 50%» (literal: exacta)
- tramo del destino: «A otros estados soberanos (o sus bancos centrales)» (literal: exacta)

---

## P09 · `aplica_a` · pool, 9 de 20

**Origen** — Obligacion «Sistemas y controles — garantizar prudencia y fiabilidad» (`Obligacion_los_sistemas_y_controles_deben_garantizar_a_los_directores_y_o_gerentes_de_la_en_f61414`)

- descripción: Los sistemas y controles deben garantizar a los directores y/o gerentes de la entidad y a la SEFyC que los valores estimados sean prudentes y fiables.
- tipo: otra

**Predicado** — `aplica_a`

- tramo del sujeto: «la entidad» (literal: exacta)

**Destino** — Sujeto «Entidades alcanzadas (Capitales Mínimos)» (`Sujeto_rol_alcance_capmin`)

- descripción: —
- nivel: rol

**Evidencia 1 de 1** — `cap::6.10.1.1` · cap · punto 6.10.1.1 · punto_propio · págs. 140

- PDF: `data/experiment/subset/TO_capitales_minimos_actual.pdf#page=140`

> *heredado (encabezado, S6, p. 116):* Sección 6. Capital mínimo por riesgo de mercado.
>
> *heredado (encabezado, 6.10, p. 140):* 6.10. Tratamiento para las posiciones de menor liquidez.
>
> *heredado (intro, 6.10, p. 140):* Se establecen lineamientos para la valuación prudente de las posiciones contabilizadas a va- lor razonable (“fair value”), ya sea que se imputen a la cartera de negociación o a la de inver- sión. Estas pautas son especialmente importantes en el caso de las posiciones para las que no hay precios de mercado o datos observables a utilizar para la valuación, así como para las posiciones menos líquidas que exigen de las entidades mayores recaudos. Las siguientes disposiciones no modifican los criterios y procedimientos de valuación de las normas conta- bles, pero la SEFyC evaluará su cumplimiento a los efectos del cálculo de la exigencia de ca- pital y de la gestión del riesgo y para determinar si procede realizar ajustes en la valuación de las posiciones menos líquidas para reflejar condiciones de mercado más realistas cuando la información disponible sea insuficiente o la transparencia de los precios inadecuada.
>
> *heredado (encabezado, 6.10.1, p. 140):* 6.10.1. Un marco de valuación prudente deberá incluir, como mínimo, lo siguiente:
>
> *propio:* 6.10.1.1. Sistemas y controles. Los sistemas y controles deben garantizar a los directores y/o gerentes de la entidad y a la SEFyC que los valores estimados sean prudentes y fiables. Es- tos sistemas, que deberán estar integrados a los demás sistemas de gestión de riesgos de la organización, deberán incluir: i) Políticas y procedimientos documentados para el proceso de valuación. In- cluye definición clara de las responsabilidades de las áreas que participan en la valuación, fuentes a consultar para obtener información del mercado y opinión sobre su validez, guías para el uso de los datos que, por no ser observables, resultan de los supuestos de la entidad acerca de las consi- deraciones de los participantes del mercado para la determinación de los precios, frecuencia de las valuaciones independientes, oportunidad de los precios de cierre, procedimientos para los ajustes de valuación y procedi- mientos de verificación, tanto “ad-hoc” como de fin de mes; y ii) Claras líneas de reporte de la información para los responsables del pro- ceso de valuación, independientes de quienes deciden y generan las ope- raciones (“front office”), que lleguen hasta el directorio de la entidad.

- tramo del origen: «Los sistemas y controles deben garantizar a los directores y/o gerentes de la entidad y a la SEFyC que los valores estimados sean prudentes y fiables.» (literal: exacta)
- tramo del destino: —

---

## P10 · `limita` · pool, 10 de 20

**Origen** — Restriccion «Sin vencimientos hasta 240 días — financiaciones 7.11.1.1-7.11.1.4» (`Restriccion_las_financiaciones_de_los_puntos_7_11_1_1_a_7_11_1_4_no_deben_tener_vencimientos_0ad73c`)

- descripción: Las financiaciones de los puntos 7.11.1.1 a 7.11.1.4 no deben tener vencimientos de capital y/o intereses hasta que hayan transcurrido 240 días corridos desde el registro de ingreso aduanero de los bienes
- tipo: limite_cualitativo
- umbrales (1):
  - valor: 240; unidad: dias; comparacion: no_determinada; dias_tipo: corridos; tramo: 240 (doscientos cuarenta) días corridos desde el registro de ingreso aduanero de los bienes

**Predicado** — `limita`

**Destino** — Operacion «Financiación puntos 7.11.1.1 a 7.11.1.4» (`Operacion_financiacion_puntos_7_11_1_1_a_7_11_1_4__ext_7_11_2_4_c3ec14`)

- descripción: Financiaciones de los puntos 7.11.1.1 a 7.11.1.4 asociadas a importaciones de bienes habilitadas para la aplicación de cobros de exportaciones de bienes
- tipo: Financiación

**Evidencia 1 de 1** — `ext::7.11.2.4` · ext · punto 7.11.2.4 · punto_propio · págs. 105

- PDF: `data/experiment/subset/TO_exterior_cambios_actual.pdf#page=105`

> *heredado (encabezado, S7, p. 80):* Sección 7. Cobros de exportaciones de bienes.
>
> *heredado (encabezado, 7.11, p. 103):* 7.11. Financiaciones asociadas a importaciones de bienes habilitadas para la aplicación de cobros
>
> *heredado (intro, 7.11, p. 103):* de exportaciones de bienes.
>
> *heredado (encabezado, 7.11.2, p. 104):* 7.11.2. La aplicación de las divisas a las operaciones señaladas será admitida en la medida
>
> *heredado (intro, 7.11.2, p. 104):* que se verifiquen la totalidad de las siguientes condiciones:
>
> *heredado (cierre, 7.11.2, p. 106):* La entidad deberá verificar los requisitos habituales a los efectos de certificar la aplicación de divisas a la cancelación de la financiación.
>
> *propio:* 7.11.2.4. Las financiaciones de los puntos 7.11.1.1. a 7.11.1.4. no tengan vencimientos de capital y/o intereses hasta que hayan transcurrido 240 (doscientos cuarenta) días corridos desde el registro de ingreso aduanero de los bienes y las financiaciones de los puntos 7.11.1.5. a 7.11.1.6. no registren vencimientos de capital durante los primeros 2 (dos) años desde su emisión.

- tramo del origen: «Las financiaciones de los puntos 7.11.1.1. a 7.11.1.4. no tengan vencimientos de capital y/o intereses hasta que hayan transcurrido 240 (doscientos cuarenta) días corridos desde el registro de ingreso aduanero de los bienes» (literal: exacta)
- tramo del destino: «Las financiaciones de los puntos 7.11.1.1. a 7.11.1.4.» (literal: exacta)

---

## P11 · `requiere` · pool, 11 de 20

**Origen** — Operacion «Custodia de títulos del FGS» (`Operacion_custodia_de_titulos_del_fgs__ric_8_1_4_07397c`)

- descripción: custodia de títulos representativos de las inversiones del Fondo de Garantía de Sustentabilidad del Sistema Integrado Previsional Argentino (FGS)
- tipo: custodia de valores

**Predicado** — `requiere`

**Destino** — Obligacion «Informar importe total de títulos en custodia» (`Obligacion_informar_el_importe_total_de_los_titulos_representativos_de_las_inversiones_del__7f224b`)

- descripción: informar el importe total de los títulos representativos de las inversiones del FGS en custodia, sobre la base de los saldos al cierre de cada mes
- tipo: presentacion_informativa
- frecuencia: al cierre de cada mes

**Evidencia 1 de 1** — `ric::8.1.4` · ric · punto 8.1.4 · punto_propio · págs. 37

- PDF: `data/experiment/subset/TO_regimen_informativo_contable_mensual_actual.pdf#page=37`

> *heredado (encabezado, S8, p. 37):* Sección 8. Totales de control.
>
> *heredado (encabezado, 8.1, p. 37):* 8.1. Normas de procedimiento.
>
> *propio:* 8.1.4. Código 70400000. Los bancos comerciales que ejerzan la función de custodia de los títulos representati- vos de las inversiones del Fondo de Garantía de Sustentabilidad del Sistema Integrado Previsional Argentino (FGS), informarán el importe total de esos valores en custodia, sobre la base de los saldos al cierre de cada mes.

- tramo del origen: «custodia de los títulos representativos de las inversiones del Fondo de Garantía de Sustentabilidad del Sistema Integrado Previsional Argentino (FGS)» (literal: exacta)
- tramo del destino: «informarán el importe total de esos valores en custodia, sobre la base de los saldos al cierre de cada mes» (literal: exacta)

---

## P12 · `requiere` · pool, 12 de 20

**Origen** — Operacion «Cobertura proporcional de exposición al riesgo» (`Operacion_cobertura_proporcional_de_exposicion_al_riesgo__cap_5_4_2_ddedc5`)

- descripción: Operación de cobertura proporcional del riesgo de crédito mediante garantías o protección crediticia, donde el importe garantizado es inferior al monto de la exposición, las partes garantizadas y no garantizadas comparten la misma prelación para el cobro (prorrata), y se reduce la exigencia de capital de manera proporcional.
- tipo: cobertura de riesgo de crédito con garantías personales y derivados de crédito

**Predicado** — `requiere`

**Destino** — Obligacion «Tratamiento de parte protegida — cobertura proporcional» (`Obligacion_la_parte_protegida_de_la_exposicion_recibira_el_tratamiento_aplicable_a_las_gara_8d4894`)

- descripción: La parte protegida de la exposición recibirá el tratamiento aplicable a las garantías/derivados crediticios admisibles en el contexto de cobertura proporcional.
- tipo: asignacion

**Evidencia 1 de 1** — `cap::5.4.2` · cap · punto 5.4.2 · punto_propio · págs. 113

- PDF: `data/experiment/subset/TO_capitales_minimos_actual.pdf#page=113`

> *heredado (encabezado, S5, p. 98):* Sección 5. Cobertura del riesgo de crédito.
>
> *heredado (chapeau_seccion, S5, p. 98):* A los efectos del cómputo de la exigencia de capital por riesgo de crédito, se reconocerá –total o parcialmente– la cobertura del riesgo de crédito (CRC) de las operaciones registradas en la cartera de inversión –tales como préstamos y responsabilidades eventuales– mediante la utilización de las técnicas previstas en el punto 5.1. La presente sección contempla, además, el cálculo de la exposición a las operaciones de financia- ción con títulos valores (securities financing transactions, SFT) –conforme a lo previsto en la Sec- ción 4.–, registradas tanto en la cartera de inversión como en la cartera de negociación.
>
> *heredado (encabezado, 5.4, p. 112):* 5.4. Operaciones cubiertas con garantías (y contragarantías) personales y derivados de crédito.
>
> *heredado (intro, 5.4, p. 112, 113):* Se aplicará el método de sustitución de ponderadores. Con este método, el ponderador de riesgo de la contraparte se sustituye por el ponderador de riesgo del garante –o contragarante– o proveedor de protección crediticia –conforme a la tabla de ponderadores prevista en la Sec- ción 2.–. Se reconocerán sólo las garantías emitidas –o protección provista, en el caso de derivados de crédito– por entidades listadas en el punto 5.4.1. La parte de la exposición sin cobertura mantendrá el ponderador de riesgo de la contraparte original, mientras que a la parte cubierta se le asignará el ponderador de riesgo del garante o proveedor de protección crediticia, teniendo en consideración lo siguiente:
>
> *propio:* 5.4.2. Cobertura proporcional. Cuando el importe garantizado, o respecto del cual se tenga protección crediticia, sea inferior al monto de la exposición al riesgo, y en la medida que las partes garantizadas y no garantizadas tengan la misma prelación para el cobro –es decir, la entidad financiera y el garante compartan las pérdidas a prorrata–, se admitirá reducir la exigencia de capi- tal de manera proporcional. Es decir que la parte protegida de la exposición recibirá el tratamiento aplicable a las garantías/derivados crediticios admisibles y el resto se consi- derará como no cubierta.

- tramo del origen: «Cuando el importe garantizado, o respecto del cual se tenga protección crediticia, sea inferior al monto de la exposición al riesgo, y en la medida que las partes garantizadas y no garantizadas tengan la misma prelación para el cobro –es decir, la entidad financiera y el garante compartan las pérdidas a prorrata–, se admitirá reducir la exigencia de capital de manera proporcional.» (literal: exacta)
- tramo del destino: «la parte protegida de la exposición recibirá el tratamiento aplicable a las garantías/derivados crediticios admisibles» (literal: exacta)

---

## P13 · `regula` · pool, 13 de 20

**Origen** — Obligacion «Utilizar calificación ECAI para ponderador riesgo» (`Obligacion_deber_de_utilizar_calificacion_otorgada_por_ecai_admitida_por_el_bcra_para_deter_ec7efd`)

- descripción: Deber de utilizar calificación otorgada por ECAI admitida por el BCRA para determinar el ponderador de riesgo, conforme a lo establecido en la Sección 10
- tipo: otra

**Predicado** — `regula`

**Destino** — Operacion «Determinación ponderador riesgo exposiciones» (`Operacion_determinacion_ponderador_riesgo_exposiciones__cap_2_5_4_02f9aa`)

- descripción: Determinación del ponderador de riesgo aplicable a exposiciones específicas (puntos 2.12.2.4, 2.12.2.5, 2.12.2.6 y 2.12.2.8) utilizando calificación de ECAI admitida por el BCRA conforme a Sección 10
- tipo: Cálculo de ponderador de riesgo

**Evidencia 1 de 1** — `cap::2.5.4` · cap · punto 2.5.4 · punto_propio · págs. 11, 12

- PDF: `data/experiment/subset/TO_capitales_minimos_actual.pdf#page=11` · `data/experiment/subset/TO_capitales_minimos_actual.pdf#page=12`

> *heredado (encabezado, S2, p. 7):* Sección 2. Capital mínimo por riesgo de crédito.
>
> *heredado (chapeau_seccion, S2, p. 7):* A los efectos de la aplicación de las disposiciones de la presente sección, las entidades financieras se clasificarán en: i)Grupo 1: entidades calificadas por el BCRA como de importancia sistémica a nivel local
>
> *heredado (chapeau_seccion, S2, p. 7):* (D-SIB) y sucursales o subsidiarias de bancos del exterior calificados como de impor- tancia sistémica global (G-SIB).
>
> *heredado (chapeau_seccion, S2, p. 7):* ii) Grupo 2: entidades financieras no comprendidas en el acápite i). En aquellos casos en que no se establezcan disposiciones específicas para cada uno de los citados grupos de entidades financieras, deberá aplicarse el mismo tratamiento a ambos grupos. Las entidades financieras que presenten cambios en su calificación –conforme a lo previsto en los acápites precedentes–, contarán con un plazo de 6 meses para aplicar las disposiciones específicas correspondientes al nuevo grupo al que pertenezcan.
>
> *heredado (encabezado, 2.5, p. 11):* 2.5. Criterios para la determinación de los activos ponderados por riesgo.
>
> *propio:* 2.5.4. A los efectos de determinar el ponderador de riesgo a aplicar a las exposiciones a que se refieren los puntos 2.12.2.4., 2.12.2.5., 2.12.2.6. y 2.12.2.8., se deberá utilizar la cali- ficación otorgada por alguna entidad que sea agente de calificación externa (External Credit Assessment Institution, ECAI) admitida por el BCRA, conforme a lo establecido en la Sección 10. Las calificaciones de crédito contempladas en dichos puntos corresponden a la metodo- logía utilizada por Standard & Poor’s y sólo se utilizan a título de ejemplo. Ninguna exposición con deudores no calificados podrá recibir un ponderador de riesgo menor que el que se aplica al país de constitución, excepto que se trate de las exposi- ciones a que se refieren los puntos 2.12.2.2. y 2.12.2.3.

- tramo del origen: «se deberá utilizar la calificación otorgada por alguna entidad que sea agente de calificación externa (External Credit Assessment Institution, ECAI) admitida por el BCRA, conforme a lo establecido en la Sección 10» (literal: exacta)
- tramo del destino: «determinar el ponderador de riesgo a aplicar a las exposiciones a que se refieren los puntos 2.12.2.4., 2.12.2.5., 2.12.2.6. y 2.12.2.8.» (literal: exacta)

---

## P14 · `aplica_a` · pool, 14 de 20

**Origen** — Potestad «Libertad de pacto del tipo de cambio» (`Potestad_libertad_de_pacto_del_tipo_de_cambio__las_operaciones_de_cambio_en_divisas_extra_c6a4aa`)

- descripción: Las operaciones de cambio en divisas extranjeras serán realizadas al tipo de cambio que sea libremente pactado entre las partes

**Predicado** — `aplica_a`

- tramo del sujeto: «las entidades financieras y las demás personas autorizadas por el Banco Central de la República Argentina» (literal: exacta)

**Destino** — Sujeto «Entidades autorizadas a operar en cambios (Exterior)» (`Sujeto_rol_entidad_autorizada_exterior`)

- descripción: —
- nivel: rol

**Evidencia 1 de 1** — `ext::15.1` · ext · punto 15.1 · punto_propio · págs. 184

- PDF: `data/experiment/subset/TO_exterior_cambios_actual.pdf#page=184`

> *heredado (encabezado, S15, p. 184):* Sección 15. Disposiciones legales que determinan la estructura general del mercado de cambios.
>
> *heredado (chapeau_seccion, S15, p. 184):* Se trascribe a continuación la parte pertinente de las disposiciones legales que determinan la estructura general del mercado de cambios:
>
> *propio:* 15.1. Artículos 1° y 2° del Decreto 260/02. “ ARTÍCULO 1°.- (Artículo sustituido por art. 132 de la Ley N° 27444 B.O. 18/06/18) Establécese un mercado libre de cambios por el cual se cursarán las operaciones de cambio que sean realizadas por las entidades financieras y las demás personas autorizadas por el Banco Central de la República Argentina para dedicarse de manera permanente o habitual al comercio de la compra y venta de monedas y billetes extranjeros, oro amonedado o en barra de buena entrega y cheques de viajero, giros, transferencias u operaciones análogas en moneda extranjera. ARTÍCULO 2°.- Las operaciones de cambio en divisas extranjeras serán realizadas al tipo de cambio que sea libremente pactado y deberán sujetarse a los requisitos y a la reglamentación que establezca el BANCO CENTRAL DE LA REPUBLICA ARGENTINA.”

- tramo del origen: «Las operaciones de cambio en divisas extranjeras serán realizadas al tipo de cambio que sea libremente pactado» (literal: exacta)
- tramo del destino: —

---

## P15 · `condicion_de` · pool, 15 de 20

**Origen** — Condicion «Documentación constata entrega mercadería en país» (`Condicion_documentacion_constata_entrega_mercaderia_en_pais__la_documentacion_debe_permiti_ea9c44`)

- descripción: La documentación debe permitir constatar que la entrega de la mercadería exportada se ha producido en el país

**Predicado** — `condicion_de`

**Destino** — Obligacion «Cumplimiento seguimiento por cobros locales — ranchos a transporte extranjero» (`Obligacion_la_entidad_podra_considerar_cumplimentado_parcial_o_totalmente_el_seguimiento_de_57be1d`)

- descripción: La entidad podrá considerar cumplimentado parcial o totalmente el seguimiento de un permiso de embarque por el valor equivalente a los montos abonados localmente en pesos y/o en moneda extranjera al exportador por un agente local de la empresa propietaria de los medios de transporte de bandera extranjera, cuando la documentación permite constatar que la entrega de la mercadería exportada se ha producido en el país, que el agente local ha realizado localmente el pago al exportador y la moneda en que dicho pago se efectuó
- tipo: otra

**Evidencia 1 de 1** — `ext::8.5.18.1` · ext · punto 8.5.18.1 · punto_propio · págs. 120

- PDF: `data/experiment/subset/TO_exterior_cambios_actual.pdf#page=120`

> *heredado (encabezado, S8, p. 108):* Sección 8. Seguimiento de las negociaciones de divisas por exportaciones de bienes
>
> *heredado (encabezado, 8.5, p. 112):* 8.5. Otras imputaciones admitidas en el cumplimiento del seguimiento.
>
> *heredado (intro, 8.5, p. 112):* La entidad podrá considerar cumplimentado parcial o totalmente el seguimiento de un permiso de embarque cuando cuente con los elementos que le permitan considerar que la operación se encuentra en alguna de las situaciones detalladas a continuación y se verifiquen las condiciones previstas en cada caso. La documentación utilizada para certificar el concepto y monto de las divisas imputado en cada caso deberá quedar archivada en la entidad a disposición del BCRA.
>
> *heredado (encabezado, 8.5.18, p. 120):* 8.5.18. Cobros locales por exportaciones del régimen de ranchos a medios de transporte de
>
> *heredado (intro, 8.5.18, p. 120):* bandera extranjera. La entidad podrá considerar cumplimentado parcial o totalmente el seguimiento de un permiso de embarque por el valor equivalente a los montos abonados localmente en pesos y/o en moneda extranjera al exportador por un agente local de la empresa propietaria de los medios de transporte de bandera extranjera, en la medida que se verifiquen las siguientes condiciones:
>
> *propio:* 8.5.18.1. La documentación permite constatar que la entrega de la mercadería exportada se ha producido en el país, que el agente local de la empresa propietaria de los medios de transporte de bandera extranjera ha realizado localmente el pago al exportador y la moneda en la que dicho pago se efectuó.

- tramo del origen: «La documentación permite constatar que la entrega de la mercadería exportada se ha producido en el país» (literal: exacta)
- tramo del destino: «La entidad podrá considerar cumplimentado parcial o totalmente el seguimiento de un permiso de embarque por el valor equivalente a los montos abonados localmente en pesos y/o en moneda extranjera al exportador por un agente local de la empresa propietaria de los medios de transporte de bandera extranjera […] La documentación permite constatar que la entrega de la mercadería exportada se ha producido en el país, que el agente local de la empresa propietaria de los medios de transporte de bandera extranjera ha realizado localmente el pago al exportador y la moneda en la que dicho pago se efectuó» (literal: exacta)

---

## P16 · `prohibe` · pool, 16 de 20

**Origen** — Restriccion «Prohibición — cobro de tasas sin cumplimiento previo» (`Restriccion_se_prohibe_cobrar_tasas_de_interes_comisiones_y_o_cargos_sin_el_cumplimiento_de__d3aa76`)

- descripción: Se prohíbe cobrar tasas de interés, comisiones y/o cargos sin el cumplimiento de lo previsto en los puntos 2.3.2. a 2.3.4.
- tipo: prohibicion

**Predicado** — `prohibe`

**Destino** — Operacion «Cobro o adeudo de importes al usuario» (`Operacion_cobro_o_adeudo_de_importes_al_usuario__pro_2_3_5_1_fe9345`)

- descripción: Importe cobrado o adeudado de cualquier forma al usuario de servicios financieros por los conceptos enumerados en los incisos i) a vii)
- tipo: cobro o adeudo

**Evidencia 1 de 1** — `pro::2.3.5.1` · pro · punto 2.3.5.1 · punto_propio · págs. 15, 16

- PDF: `data/experiment/subset/TO_proteccion_usuarios_servicios_financieros_actual.pdf#page=15` · `data/experiment/subset/TO_proteccion_usuarios_servicios_financieros_actual.pdf#page=16`

> *heredado (encabezado, S2, p. 5):* Sección 2. Derechos básicos de los usuarios de servicios financieros.
>
> *heredado (encabezado, 2.3, p. 7):* 2.3. Recaudos mínimos de la relación de consumo.
>
> *heredado (encabezado, 2.3.5, p. 15):* 2.3.5. Reintegro de importes.
>
> *propio:* 2.3.5.1. Todo importe cobrado o adeudado de cualquier forma al usuario de servicios fi- nancieros por los siguientes conceptos: i) tasas de interés, comisiones y/o cargos sin el cumplimiento de lo previsto en los puntos 2.3.2. a 2.3.4.; ii) cargos en exceso de los costos de los servicios que terceros les cobraron a los sujetos obligados en relación con servicios prestados a los usuarios y/o de los precios que el tercero prestador perciba de particulares en general; iii) comisiones en exceso de las máximas fijadas por el BCRA que sean de aplicación; iv) en incumplimiento al nivel de la tasa de interés máxima aplicable a finan- ciaciones vinculadas a tarjetas de crédito previstas en el texto ordenado sobre Tasas de Interés en las Operaciones de Crédito; v) en exceso de lo oportunamente pactado entre el usuario y el sujeto obliga- do; vi) otros generados en forma impropia por su naturaleza, tales como intereses compensatorios por saldos deudores generados en cuentas de depósito distintas de la cuenta corriente bancaria; vii) así como los importes adeudados al usuario por haber liquidado en forma incorrecta promociones, descuentos u otro tipo de beneficios –es decir, que no se ajustan a los términos, condiciones y/o modalidades que hubieran sido ofrecidos, publicitados o convenidos–; deberá serle reintegrado dentro de: - los diez (10) días hábiles siguientes al momento de la presentación del re- clamo ante el sujeto obligado, de conformidad con las previsiones del punto 3.1.6.; o - los cinco (5) días hábiles siguientes al momento de constatarse tal circuns- tancia por el sujeto obligado o por la fiscalización que realice la SEFYC. Ello, sin perjuicio de las sanciones que pudieran corresponder. En tales situaciones, corresponderá reconocer el importe de los gastos que re- sulten razonables realizados para la obtención del reintegro y, en todos los ca- sos, los intereses compensatorios pertinentes, computados desde la fecha del cobro indebido hasta la de su efectiva devolución. A ese efecto, el sujeto obli- gado deberá aplicar 1,5 veces la tasa promedio correspondiente al período comprendido entre el momento en que la citada diferencia hubiera sido exigible –fecha en la que se cobraron los importes objeto del reclamo– y el de su efecti- va cancelación, computado a partir de la encuesta diaria de tasas de interés de depósitos a plazo fijo de 30 a 59 días –de pesos o dólares estadounidenses, según la moneda de la operación– informada por el BCRA sobre la base de la información provista por la totalidad de bancos públicos y privados. Cuando la tasa correspondiente a tal encuesta no estuviera disponible, se deberá tomar la última informada. Cuando el usuario posea en la entidad financiera obligada una cuenta a la vista que se halle abierta a su nombre, ésta deberá acreditar ese importe en dicha cuenta en forma automática sin necesidad de requerimiento expreso. Si ello no fuera posible o no se tratare de una entidad financiera, el importe del reintegro deberá ser acreditado en una tarjeta de crédito de su titularidad o detraído del saldo vigente de la financiación que lo generó. Deberá notificarse la acreditación del reintegro o, en su caso, su puesta a dis- posición mediante aviso efectuado a través de medios electrónicos –cajeros automáticos, banca por Internet (home banking), etc.– y/o servicios te- lefónicos –tales como mensajes de texto y/o voz– y: a) documento escrito dirigido a su domicilio –en forma separada de cualquier otra información que se le remita (resúmenes de cuenta, boletines informa- tivos, etc.), aun cuando forme parte de la misma remesa–; o b) a su correo electrónico –en aquellos casos en que hubiere expresamente aceptado esa forma de notificación–. Estas disposiciones serán de aplicación a los efectos de dar cumplimiento a acuerdos extrajudiciales homologados, acuerdos homologados por acciones colectivas (artículo 54 de la Ley 24.240) o sentencias judiciales, en la medida en que no se opongan a lo previsto en esos acuerdos o a lo dispuesto por los poderes públicos de las distintas jurisdicciones. Adicionalmente, el sujeto obligado deberá verificar si este tipo de situaciones que generan la obligación de reintegros ha ocurrido respecto de los usuarios que se encuentren en la misma situación y, de corresponder, proceder a su re- integro según el procedimiento previsto en este punto, notificando de tal cir- cunstancia y resultados a su Responsable de Atención al Usuario de Servicios Financieros.

- tramo del origen: «tasas de interés, comisiones y/o cargos sin el cumplimiento de lo previsto en los puntos 2.3.2. a 2.3.4.» (literal: exacta)
- tramo del destino: «Todo importe cobrado o adeudado de cualquier forma al usuario de servicios financieros» (literal: exacta)

---

## P17 · `aplica_a` · pool, 17 de 20

**Origen** — Operacion «Cálculo de exigencias de capital por moneda» (`Operacion_calculo_de_exigencias_de_capital_por_moneda__cap_6_2_2_2_9ab4c9`)

- descripción: Las exigencias de capital se calcularán por separado para las posiciones en pesos y en cada moneda extranjera
- tipo: cálculo de exigencias de capital

**Predicado** — `aplica_a`

- tramo del sujeto: «la entidad» (literal: exacta)

**Destino** — Sujeto «Entidades alcanzadas (Capitales Mínimos)» (`Sujeto_rol_alcance_capmin`)

- descripción: —
- nivel: rol

**Evidencia 1 de 1** — `cap::6.2.2.2` · cap · punto 6.2.2.2 · punto_propio · págs. 123

- PDF: `data/experiment/subset/TO_capitales_minimos_actual.pdf#page=123`

> *heredado (encabezado, S6, p. 116):* Sección 6. Capital mínimo por riesgo de mercado.
>
> *heredado (encabezado, 6.2, p. 118):* 6.2. Exigencia de capital por riesgo de tasa de interés.
>
> *heredado (intro, 6.2, p. 118):* La exigencia de capital por el riesgo de tasa de interés se deberá calcular respecto de los títu- los de deuda y otros instrumentos imputados a la cartera de negociación, incluidas las accio- nes preferidas no convertibles. Un título valor vendido y recomprado a término en una operación de pase pasivo o en otro tipo de operación de financiación con títulos valores se tratará como si todavía fuese propiedad de la entidad cedente; es decir, recibirá el mismo tratamiento que un título en cartera. Las acciones preferidas convertibles a un precio predeterminado en acciones ordinarias de la emisora se tratarán según cómo se negocien, como títulos de deuda o como acciones. La exigencia se obtendrá como la suma de dos exigencias calculadas por separado: una por el riesgo específico de cada instrumento, ya sea que se trate de una posición vendida o com- prada, y otra por el riesgo general de mercado –vinculado al efecto de cambios en la tasa de interés sobre la cartera–, en la que se podrán compensar las posiciones compradas y vendi- das en diferentes instrumentos. Para los instrumentos derivados, serán de aplicación las disposiciones establecidas en el pun- to 6.2.3.
>
> *heredado (encabezado, 6.2.2, p. 123):* 6.2.2. Exigencia de capital por riesgo general de mercado: método de los plazos residuales.
>
> *propio:* 6.2.2.2. Las exigencias de capital se calcularán por separado para las posiciones en pesos y en cada moneda extranjera. Cuando el total de las operaciones en una moneda extranjera no sea significativo –monedas extranjeras residuales–, la entidad podrá imputar las posiciones netas, compradas o vendidas, a las ban- das de una escala única. En tal caso, deberá sumar las posiciones individuales netas dentro de cada banda, con independencia de que sean compradas o vendidas, a fin de determinar el monto de la posición bruta en estas monedas extranjeras residuales.

- tramo del origen: «Las exigencias de capital se calcularán por separado para las posiciones en pesos y en cada moneda extranjera» (literal: exacta)
- tramo del destino: —

---

## P18 · `regula` · pool, 18 de 20

**Origen** — Obligacion «Valor del inmueble al momento del otorgamiento» (`Obligacion_el_valor_del_inmueble_debe_corresponder_al_del_momento_del_otorgamiento_del_cred_b08572`)

- descripción: El valor del inmueble debe corresponder al del momento del otorgamiento del crédito, salvo en los supuestos de ajustes por razones objetivas, reducciones generalizadas ordenadas por el BCRA, eventos idiosincrásicos extraordinarios o mejoras permanentes.
- tipo: otra

**Predicado** — `regula`

**Destino** — Operacion «Cálculo prudente del LTV» (`Operacion_calculo_prudente_del_ltv__cap_2_9_2_3_bce3f2`)

- descripción: Cálculo de la relación entre el saldo de deuda pendiente y el valor del inmueble (LTV) de manera prudente y conforme a requisitos específicos.
- tipo: cálculo

**Evidencia 1 de 1** — `cap::2.9.2.3` · cap · punto 2.9.2.3 · punto_propio · págs. 19

- PDF: `data/experiment/subset/TO_capitales_minimos_actual.pdf#page=19`

> *heredado (encabezado, S2, p. 7):* Sección 2. Capital mínimo por riesgo de crédito.
>
> *heredado (chapeau_seccion, S2, p. 7):* A los efectos de la aplicación de las disposiciones de la presente sección, las entidades financieras se clasificarán en: i)Grupo 1: entidades calificadas por el BCRA como de importancia sistémica a nivel local
>
> *heredado (chapeau_seccion, S2, p. 7):* (D-SIB) y sucursales o subsidiarias de bancos del exterior calificados como de impor- tancia sistémica global (G-SIB).
>
> *heredado (chapeau_seccion, S2, p. 7):* ii) Grupo 2: entidades financieras no comprendidas en el acápite i). En aquellos casos en que no se establezcan disposiciones específicas para cada uno de los citados grupos de entidades financieras, deberá aplicarse el mismo tratamiento a ambos grupos. Las entidades financieras que presenten cambios en su calificación –conforme a lo previsto en los acápites precedentes–, contarán con un plazo de 6 meses para aplicar las disposiciones específicas correspondientes al nuevo grupo al que pertenezcan.
>
> *heredado (encabezado, 2.9, p. 18):* 2.9. Exposiciones con garantía hipotecaria.
>
> *heredado (encabezado, 2.9.2, p. 18):* 2.9.2. Exposiciones con garantía hipotecaria normativas. Requisitos.
>
> *propio:* 2.9.2.3. La relación entre el saldo de deuda y el valor del inmueble (loan-to-value, LTV) se deberá calcular de manera prudente y con ajuste a los siguientes requisitos: i) El saldo de deuda pendiente se compute sin deducir previsiones por riesgo de incobrabilidad ni coberturas del riesgo de crédito previstas en la Sección 5. ii) El valor del inmueble se corresponda al del momento del otorgamiento, ex- cepto que: a) Se realicen ajustes por razones objetivas. b) El BCRA establezca que se debe hacer una reducción generalizada del valor. Si posteriormente se autorizan incrementos, el valor ajustado del inmueble no podrá superar el valor considerado en oportunidad del otorgamiento del crédito debidamente actualizado. c) Se produzca un evento idiosincrásico y extraordinario del que resulte una reducción permanente del valor del inmueble. d) Se realicen mejoras de carácter permanente en el inmueble que in- crementen su valor en forma indubitable. iii) El valor del inmueble sea el resultado de una tasación que cumpla los si- guientes criterios: a) se ajuste a una valuación conservadora; b) se realice en forma independiente respecto de quienes participan de los procesos de otorgamiento del crédito; c) no se base en la expectativa de que se incrementará el precio del in- mueble; d) no resulte mayor al precio de mercado; e) no sea mayor al precio de adquisición –en los casos en que el présta- mo con garantía hipotecaria financie la compra del inmueble hipoteca- do–, contemplando lo dispuesto en el acápite ii), inciso a); y f) no dependa de la situación económica del prestatario.

- tramo del origen: «El valor del inmueble se corresponda al del momento del otorgamiento» (literal: exacta)
- tramo del destino: «La relación entre el saldo de deuda y el valor del inmueble (loan-to-value, LTV) se deberá calcular de manera prudente» (literal: exacta)

---

## P19 · `condicion_de` · pool, 19 de 20

**Origen** — Condicion «Bienes importados temporalmente sin uso de divisas incorporados» (`Condicion_bienes_importados_temporalmente_sin_uso_de_divisas_incorporados__condicion_que_l_d65365`)

- descripción: Condición: que la operación incorpore bienes importados temporalmente sin uso de divisas mediante los subregímenes EC03, EG03, EC04 o EG13.

**Predicado** — `condicion_de`

**Destino** — Operacion «Certificación de afectación — importación temporal» (`Operacion_certificacion_de_afectacion_importacion_temporal__ext_8_5_7_3_d61e54`)

- descripción: Certificación de afectación emitida por la entidad encargada del seguimiento en el SEPAIMPO del despacho de importación temporal para transformación, que acredita el registro de ingreso aduanero de la mercadería exportada.
- tipo: Certificación de afectación

**Evidencia 1 de 1** — `ext::8.5.7.3` · ext · punto 8.5.7.3 · punto_propio · págs. 114

- PDF: `data/experiment/subset/TO_exterior_cambios_actual.pdf#page=114`

> *heredado (encabezado, S8, p. 108):* Sección 8. Seguimiento de las negociaciones de divisas por exportaciones de bienes
>
> *heredado (encabezado, 8.5, p. 112):* 8.5. Otras imputaciones admitidas en el cumplimiento del seguimiento.
>
> *heredado (intro, 8.5, p. 112):* La entidad podrá considerar cumplimentado parcial o totalmente el seguimiento de un permiso de embarque cuando cuente con los elementos que le permitan considerar que la operación se encuentra en alguna de las situaciones detalladas a continuación y se verifiquen las condiciones previstas en cada caso. La documentación utilizada para certificar el concepto y monto de las divisas imputado en cada caso deberá quedar archivada en la entidad a disposición del BCRA.
>
> *heredado (encabezado, 8.5.7, p. 114):* 8.5.7. Exportaciones que incorporan bienes importados temporalmente sin uso de divisas.
>
> *heredado (intro, 8.5.7, p. 114):* Por el valor de los bienes importados temporalmente sin uso de divisas que fueron incorporados en el valor de los bienes exportados mediante los subregímenes EC03 (Exportación a consumo con despacho de importación temporaria (DIT) con transformación), EG03 (Exportación a consumo con DIT con transformación Gran Operador), EC04 (Exportación a consumo con DIT ingresada para transformación egresado sin transformación) o EG13 (Exportación para Consumo con DIT con Transformación Gran Operador con Autorización) en la medida que la entidad cuente con:
>
> *propio:* 8.5.7.3. La certificación de afectación emitida por la entidad encargada del seguimiento en el SEPAIMPO (Sección 11.) del despacho de importación temporal para transformación por la cual se produjo el registro de ingreso aduanero de la mercadería exportada.

- tramo del origen: «Por el valor de los bienes importados temporalmente sin uso de divisas que fueron incorporados en el valor de los bienes exportados mediante los subregímenes EC03 (Exportación a consumo con despacho de importación temporaria (DIT) con transformación), EG03 (Exportación a consumo con DIT con transformación Gran Operador), EC04 (Exportación a consumo con DIT ingresada para transformación egresado sin transformación) o EG13 (Exportación para Consumo con DIT con Transformación Gran Operador con Autorización)» (literal: exacta)
- tramo del destino: «La certificación de afectación emitida por la entidad encargada del seguimiento en el SEPAIMPO (Sección 11.) del despacho de importación temporal para transformación» (literal: exacta)

---

## P20 · `aplica_a` · pool, 20 de 20

**Origen** — Obligacion «Conformidad previa del BCRA para acceso al mercado de cambios» (`Obligacion_las_entidades_financieras_y_las_empresas_no_financieras_emisoras_de_tarjetas_loc_f706c4`)

- descripción: Las entidades financieras y las empresas no financieras emisoras de tarjetas locales deberán contar con la conformidad previa del BCRA para acceder al mercado de cambios para realizar pagos al exterior por el uso de dichas tarjetas o cualquier modalidad que implique un débito inmediato en una cuenta en una entidad financiera local, cuando tales pagos se originen en forma directa o indirecta a través del uso de redes de pagos internacionales en la transferencia de fondos a cuentas de inversión en administradores de inversiones radicados en el exterior.
- tipo: otra

**Predicado** — `aplica_a`

- tramo del sujeto: «Las entidades financieras» (literal: exacta)

**Destino** — Sujeto «Entidades financieras» (`Sujeto_entidad_financiera`)

- descripción: —
- nivel: clase
- alias: ["Entidades financieras emisoras de tarjetas de crédito y/o compra", "Entidad financiera emisora de tarjetas de crédito y/o compra"]

**Evidencia 1 de 1** — `ext::4.1.4.3` · ext · punto 4.1.4 · herencia_encabezado · págs. 57

- PDF: `data/experiment/subset/TO_exterior_cambios_actual.pdf#page=57`

> *heredado (encabezado, S4, p. 56):* Sección 4. Otras disposiciones específicas.
>
> *heredado (encabezado, 4.1, p. 56):* 4.1. Operaciones con débito en una cuenta en una entidad financiera local y/o con tarjetas de
>
> *heredado (intro, 4.1, p. 56):* crédito, compra y prepagas emitidas en el país.
>
> *heredado (encabezado, 4.1.4, p. 57):* 4.1.4. Pagos al exterior por el uso de tarjetas de crédito, compra, débito o prepagas emitidas
>
> *heredado (intro, 4.1.4, p. 57):* en el país o cualquier modalidad que implique un débito inmediato en una cuenta en una entidad financiera local. Las entidades financieras y las empresas no financieras emisoras de tarjetas locales deberán contar con la conformidad previa del BCRA para acceder al mercado de cambios para realizar pagos al exterior por el uso de dichas tarjetas o cualquier modalidad que implique un débito inmediato en una cuenta en una entidad financiera local, cuando tales pagos se originen, en forma directa o indirecta a través del uso de redes de pagos internacionales, en las siguientes operaciones:
>
> *propio:* 4.1.4.3. la transferencia de fondos a cuentas de inversión en administradores de inversiones radicados el exterior, y/o

- tramo del origen: «Las entidades financieras y las empresas no financieras emisoras de tarjetas locales deberán contar con la conformidad previa del BCRA para acceder al mercado de cambios para realizar pagos al exterior por el uso de dichas tarjetas o cualquier modalidad que implique un débito inmediato en una cuenta en una entidad financiera local, cuando tales pagos se originen, en forma directa o indirecta a través del uso de redes de pagos internacionales, en las siguientes operaciones: […] la transferencia de fondos a cuentas de inversión en administradores de inversiones radicados el exterior, y/o» (literal: exacta)
- tramo del destino: —

---

