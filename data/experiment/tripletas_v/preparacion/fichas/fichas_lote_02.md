# U-TRIP-V: fichas del lote 02 (10)

Acta del sorteo `acta_sorteo_V.json` (sha256 `5d6a237e510bcf086db717061dd146eaa9b3181006cb7b1d300164436c720c55`), sellada a las 2026-10-19T14:23:55-03:00; fichas generadas a las 2026-10-19T14:25:19-03:00. Grafo KG-Tanda0-Desarrollo-r2b-sincola-rs1 (`66e745f5…`). Las fichas van en el orden sellado. Criterio (§3.4 del pre-registro): la evidencia sostiene la relación entre esos dos nodos, con sus sujetos, valores, calificadores y modalidad.

Cada ficha trae los dos nodos (tipo, etiqueta, descripción y propiedades), el predicado y la evidencia de cada procedencia: el texto heredado y el propio de la unidad de E0, el tramo literal de cada extremo en esa unidad si lo hay, las páginas y la ruta del PDF con la página. «literal» dice si el tramo está tal cual en el texto (exacta), por tokens (tokens) o no (no).

## V021 · `aplica_a` · lote_02, 1 de 10

**Origen** — Obligacion «Cálculo importe reconocido en CO» (`Obligacion_el_importe_a_reconocer_en_el_capital_ordinario_de_la_entidad_sera_igual_al_impor_c91a80`)

- descripción: El importe a reconocer en el capital ordinario de la entidad será igual al importe de la participación minoritaria en el CO de la subsidiaria, neto del excedente de CO de la subsidiaria que corresponde a los accionistas minoritarios
- tipo: calculo

**Predicado** — `aplica_a`

- tramo del sujeto: «la entidad financiera» (literal: no)

**Destino** — Sujeto «Entidades alcanzadas (Capitales Mínimos)» (`Sujeto_rol_alcance_capmin`)

- descripción: —
- nivel: rol

**Evidencia 1 de 1** — `cap::8.3.5.1` · cap · punto 8.3.5.1 · punto_propio · págs. 160, 161

- PDF: `data/experiment/subset/TO_capitales_minimos_actual.pdf#page=160` · `data/experiment/subset/TO_capitales_minimos_actual.pdf#page=161`

> *heredado (encabezado, S8, p. 154):* Sección 8. Responsabilidad patrimonial computable.
>
> *heredado (encabezado, 8.3, p. 156):* 8.3. Criterios relacionados con los conceptos computables.
>
> *heredado (encabezado, 8.3.5, p. 160):* 8.3.5. Participaciones minoritarias –no confieren control– y otros instrumentos computables
>
> *heredado (intro, 8.3.5, p. 160):* como capital emitidos por subsidiarias sujetas a supervisión consolidada en poder de terceros.
>
> *propio:* 8.3.5.1. Acciones ordinarias emitidas por subsidiarias sujetas a supervisión consolidada. Una participación minoritaria podrá reconocerse en el CO de la entidad finan- n1 ciera si el instrumento que la origina observa todos los requisitos para su clasifi- cación como acción ordinaria a efectos de la RPC. El importe que se reconocerá en el CO de la entidad será el importe de la par- n1 ticipación minoritaria en el CO de la subsidiaria neto del excedente de CO de n1 n1 la subsidiaria que corresponde a los accionistas minoritarios. El excedente de CO de la subsidiaria se calcula como el CO de la subsidiaria n1 n1 neto del menor de los siguientes importes: i) su requerimiento mínimo de CO más su margen de conservación de capital; n1 ii) la porción correspondiente a la subsidiaria del requerimiento mínimo de CO n1 más el margen de conservación de capital, ambos computados sobre base consolidada. El excedente de CO atribuible a los accionistas minoritarios resultará de multi- n1 plicar el excedente de CO de la subsidiaria –determinado conforme a lo seña- n1 lado precedentemente– por el porcentaje de CO en poder de accionistas mino- n1 ritarios.

- tramo del origen: «El importe que se reconocerá en el CO de la entidad será el importe de la participación minoritaria en el CO de la subsidiaria neto del excedente de CO de la subsidiaria que corresponde a los accionistas minoritarios» (literal: no)
- tramo del destino: —

---

## V022 · `regula` · lote_02, 2 de 10

**Origen** — Obligacion «Emitir Certificaciones de aumento de exportaciones» (`Obligacion_la_entidad_financiera_nominada_debera_emitir_las_certificaciones_de_aumento_de_l_db8fb7`)

- descripción: La entidad financiera nominada deberá emitir las Certificaciones de aumento de las exportaciones de bienes en el marco del punto 3.18
- tipo: otra

**Predicado** — `regula`

**Destino** — Operacion «Emisión de Certificaciones de aumento de exportaciones» (`Operacion_emision_de_certificaciones_de_aumento_de_exportaciones__ext_3_17_2_1_a0fd83`)

- descripción: Emisión de las Certificaciones de aumento de las exportaciones de bienes en el marco del punto 3.18
- tipo: emisión de certificación

**Evidencia 1 de 1** — `ext::3.17.2.1` · ext · punto 3.17.2.1 · punto_propio · págs. 51

- PDF: `data/experiment/subset/TO_exterior_cambios_actual.pdf#page=51`

> *heredado (encabezado, S3, p. 16):* Sección 3. Disposiciones específicas para los egresos por el mercado de cambios
>
> *heredado (chapeau_seccion, S3, p. 16):* Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–, adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables.
>
> *heredado (encabezado, 3.17, p. 50):* 3.17. Acceso con “Certificación por los regímenes de acceso a divisas para la producción
>
> *heredado (intro, 3.17, p. 50):* incremental de petróleo y/o gas natural (Decreto 277/22)”.
>
> *heredado (encabezado, 3.17.2, p. 51):* 3.17.2. Los beneficiarios del Régimen de acceso a divisas para la producción incremental de
>
> *heredado (intro, 3.17.2, p. 51):* petróleo (RADPIP) y/o Régimen de acceso a divisas para la producción incremental de gas natural (RADPIGN) deberán nominar una única entidad financiera local que será la responsable de emitir las “certificaciones por los regímenes de acceso a divisas para la producción incremental de petróleo y/o gas natural (Decreto 277/22)” y remitirlas a las entidades por las cuales el cliente desee acceder al mercado de cambios. En caso de que el cliente sea un beneficiario directo del Decreto 277/22, para quedar habilitada para emitir las certificaciones la entidad también deberá estar nominada por el cliente como responsable de:
>
> *heredado (cierre, 3.17.2, p. 51):* Si fuese necesario modificar la entidad nominada responsable de lo indicado en los puntos 3.17.2.1. y/o 3.17.2.2., la nueva entidad será considerada responsable una vez que el cambio de entidad haya quedado registrado en el BCRA y la entidad previa le haya remitido el detalle de las certificaciones emitidas a nombre del cliente hasta ese momento.
>
> *propio:* 3.17.2.1. la emisión de las “Certificaciones de aumento de las exportaciones de bienes” en el marco del punto 3.18.

- tramo del origen: «la emisión de las "Certificaciones de aumento de las exportaciones de bienes" en el marco del punto 3.18» (literal: exacta)
- tramo del destino: «la emisión de las "Certificaciones de aumento de las exportaciones de bienes"» (literal: exacta)

---

## V023 · `aplica_a` · lote_02, 3 de 10

**Origen** — Excepcion «Excepción conformidad previa — pago simultáneo con liquidación» (`Excepcion_no_aplica_el_requisito_de_conformidad_previa_del_bcra_cuando_el_pago_se_concrete_0b473f`)

- descripción: No aplica el requisito de conformidad previa del BCRA cuando el pago se concrete de manera simultánea con la liquidación por un importe no menor al monto de intereses por el cual se accede al mercado de cambios
- umbrales (1):
  - comparacion: minimo_inclusivo; base: monto de intereses; tramo: no menor al monto de intereses

**Predicado** — `aplica_a`

- tramo del sujeto: «Las entidades» (literal: exacta)

**Destino** — Sujeto «Entidades autorizadas a operar en cambios (Exterior)» (`Sujeto_rol_entidad_autorizada_exterior`)

- descripción: —
- nivel: rol

**Evidencia 1 de 1** — `ext::3.3.3.4` · ext · punto 3.3.3.4 · punto_propio · págs. 17

- PDF: `data/experiment/subset/TO_exterior_cambios_actual.pdf#page=17`

> *heredado (encabezado, S3, p. 16):* Sección 3. Disposiciones específicas para los egresos por el mercado de cambios
>
> *heredado (chapeau_seccion, S3, p. 16):* Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–, adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables.
>
> *heredado (encabezado, 3.3, p. 16):* 3.3. Pagos de intereses de deudas por importaciones de bienes y servicios.
>
> *heredado (intro, 3.3, p. 16):* Las entidades para dar acceso al mercado de cambios para cursar pagos de intereses de deudas comerciales por importaciones de bienes o servicios deberán verificar que se cumplan las condiciones especificadas a continuación:
>
> *heredado (encabezado, 3.3.3, p. 16):* 3.3.3. Se requerirá la conformidad previa del BCRA cuando el acreedor sea una contraparte
>
> *heredado (intro, 3.3.3, p. 16):* vinculada al deudor y el vencimiento de los intereses a pagar haya tenido lugar hasta el 04/07/24. Este requisito no resultará aplicable cuando la operación encuadre en alguna de las siguientes situaciones:
>
> *heredado (cierre, 3.3.3, p. 17):* La entidad deberá verificar el cumplimiento de la totalidad de los restantes requisitos normativos aplicables a la operación previamente a realizar el pedido al BCRA. Por hasta el monto de los intereses compensatorios sujetos a conformidad previa los clientes podrán suscribir Bonos para la Reconstrucción de una Argentina Libre (BOPREAL) en la medida que se cumplan los requisitos previstos en el punto 4.7.
>
> *propio:* 3.3.3.4. el pago se concrete de manera simultánea con la liquidación por un importe no menor al monto de intereses por el cual se accede al mercado de cambios de: i) nuevos endeudamientos financieros comprendidos en el punto 3.5. con una vida promedio no inferior a 2 (dos) años y que contemplen como mínimo 1 (un) año de gracia para el pago de capital, en ambos casos contados desde la fecha en que se concreta el acceso al mercado. ii) nuevos aportes de inversión directa de no residentes. Los endeudamientos financieros y/o los aportes de inversión extranjera directa, que no podrán ser computados a los efectos de otros mecanismos considerados en la normativa cambiaria, podrán ser ingresados y liquidados por el deudor que cancela los intereses o por otra empresa residente perteneciente a su grupo económico.

- tramo del origen: «Este requisito no resultará aplicable cuando la operación encuadre en alguna de las siguientes situaciones: el pago se concrete de manera simultánea con la liquidación por un importe no menor al monto de intereses por el cual se accede al mercado de cambios» (literal: no)
- tramo del destino: —

---

## V024 · `aplica_a` · lote_02, 4 de 10

**Origen** — Obligacion «Reporte trimestral al Directorio sobre acciones realizadas» (`Obligacion_el_directivo_responsable_debe_elevar_al_directorio_o_autoridad_equivalente_un_re_637bda`)

- descripción: El Directivo Responsable debe elevar al Directorio o autoridad equivalente un reporte de análisis con las acciones realizadas en el marco de sus responsabilidades, haciendo especial énfasis en el resultado de la evaluación realizada sobre el informe que trimestralmente le eleva el Responsable de atención al usuario de servicios financieros. El referido reporte deberá ser evaluado por ese órgano directivo, dejando constancia en el Libro de Actas respectivo.
- tipo: reporte_al_supervisor
- frecuencia: trimestral
- umbrales (1):
  - comparacion: minimo_inclusivo; tramo: como mínimo trimestralmente

**Predicado** — `aplica_a`

- tramo del sujeto: «los otros proveedores no financieros de crédito» (literal: exacta)

**Destino** — Sujeto «Proveedores no financieros de crédito» (`Sujeto_proveedor_no_financiero_de_credito`)

- descripción: —
- nivel: clase
- alias: ["PNFC"]

**Evidencia 1 de 1** — `pro::3.2.1.1` · pro · punto 3.2.1.1 · punto_propio · págs. 26, 27, 28

- PDF: `data/experiment/subset/TO_proteccion_usuarios_servicios_financieros_actual.pdf#page=26` · `data/experiment/subset/TO_proteccion_usuarios_servicios_financieros_actual.pdf#page=27` · `data/experiment/subset/TO_proteccion_usuarios_servicios_financieros_actual.pdf#page=28`

> *heredado (encabezado, S3, p. 23):* Sección 3. Servicio de atención al usuario de servicios financieros.
>
> *heredado (chapeau_seccion, S3, p. 23):* Los sujetos obligados deberán establecer este servicio para dar tratamiento y resolver las consul- tas y reclamos que presenten los usuarios de servicios financieros, observando las normas lega- les, reglamentarias y disposiciones vigentes en materia de protección al usuario de servicios finan- cieros, adoptando acciones que reduzcan su reiteración.
>
> *heredado (encabezado, 3.2, p. 26):* 3.2. Controles.
>
> *heredado (encabezado, 3.2.1, p. 26):* 3.2.1. De los sujetos obligados.
>
> *propio:* 3.2.1.1. Directivo Responsable de Protección de los Usuarios de Servicios Financie- ros/Comité de Protección de los Usuarios de Servicios Financieros. Las entidades financieras, las empresas no financieras emisoras de tarjetas de crédito y/o compra y los otros proveedores no financieros de crédito que atien- den a usuarios de servicios financieros deberán designar a un miembro del Di- rectorio o autoridad equivalente como “Directivo Responsable de Protección de los Usuarios de Servicios Financieros” ante el BCRA, quien asumirá una res- ponsabilidad primaria por el cumplimiento de estas normas. El Directivo Responsable de Protección de los Usuarios de Servicios Financie- ros realizará un seguimiento de las actividades desarrolladas por los niveles gerenciales y/o jefaturas de la entidad involucrados en el proceso interno de protección al usuario a efectos de dar cumplimiento a las siguientes cuestiones: i) Vigilar el adecuado funcionamiento de los procesos relacionados con la protección de los usuarios de los servicios financieros según las disposi- ciones establecidas en estas normas y aquellas que regulan las operato- rias que involucran las prestaciones a usuarios de servicios financieros. ii) Contribuir a la mejora de los mencionados procesos, los controles relacio- nados y el esquema de gestión de riesgo asociado con la protección de los usuarios de servicios financieros, en coordinación con las áreas y/o funcio- narios a cargo de las siguientes cuestiones: cumplimiento normativo, ges- tión de riesgo operativo y asuntos legales. iii) Proponer al Directorio o autoridad equivalente a los funcionarios para el desempeño de la función de Responsable de atención al usuario de servi- cios financieros. iv) Participar en el proceso de definición y aprobación de nuevos productos y servicios y en la modificación de los existentes, vigilando que se hayan considerado adecuadamente los derechos de los usuarios de servicios fi- nancieros consagrados en esta normativa y las previsiones que resulten de las normas de fondo aplicables. v) Verificar el adecuado funcionamiento del proceso de análisis de las causas generadoras de los eventos de reclamos previsto en el punto 3.1.1.6. vi) Evaluar los reportes trimestrales que genere el Responsable de atención al usuario de servicios financieros, aprobar las propuestas correctivas que di- cho funcionario eleve a su consideración y efectuar el seguimiento de su implementación. vii) Evaluar los informes emitidos por la auditoría interna, la auditoría externa y las observaciones e indicaciones comunicadas por la SEFyC con relación al proceso de protección de los usuarios de servicios financieros, y velar por la ejecución de las acciones tendientes a regularizar o minimizar las debilidades que surjan de tales documentos. viii) Velar por el cumplimiento de los requerimientos informativos del BCRA que son materia de su incumbencia. ix) Elevar al Directorio o autoridad equivalente, como mínimo trimestralmen- te, un reporte de análisis con las acciones realizadas en el marco de sus responsabilidades haciendo especial énfasis en el resultado de la evalua- ción realizada sobre el informe que trimestralmente le eleva el Responsa- ble de atención al usuario de servicios financieros. El referido reporte de- berá ser evaluado por ese órgano directivo, dejando constancia en el Li- bro de Actas respectivo. Alternativamente, cuando la dimensión, operatoria y/o clientela de la entidad así lo aconsejaran, los sujetos obligados podrán optar por la conformación de un Comité integrado por al menos un miembro del Directorio o autoridad equi- valente y por los responsables de las áreas a cargo de las funciones de cum- plimiento normativo, gestión de riesgo operativo y asuntos legales, teniendo di- cho comité las mismas funciones y responsabilidades asignadas por la presen- te norma al “Directivo Responsable de Protección de los Usuarios de Servicios Financieros”.

- tramo del origen: «Elevar al Directorio o autoridad equivalente, como mínimo trimestralmente, un reporte de análisis con las acciones realizadas en el marco de sus responsabilidades haciendo especial énfasis en el resultado de la evaluación realizada sobre el informe que trimestralmente le eleva el Responsable de atención al usuario de servicios financieros» (literal: exacta)
- tramo del destino: —

---

## V025 · `condicion_de` · lote_02, 5 de 10

**Origen** — Condicion «Incumplimiento requisitos debida diligencia» (`Condicion_incumplimiento_requisitos_debida_diligencia__supuesto_en_que_no_se_cumpla_con_al_c04212`)

- descripción: Supuesto en que no se cumpla con alguno de los requisitos de debida diligencia en titulizaciones

**Predicado** — `condicion_de`

**Destino** — Obligacion «Ponderación posición titulización 1250 %» (`Obligacion_deber_de_ponderar_la_posicion_de_titulizacion_al_1250_cuando_no_se_cumpla_con_lo_11b2af`)

- descripción: Deber de ponderar la posición de titulización al 1250 % cuando no se cumpla con los requisitos de debida diligencia
- tipo: calculo
- umbrales (1):
  - valor: 1250; unidad: porcentaje; comparacion: coeficiente; tramo: al 1250 %

**Evidencia 1 de 1** — `cap::3.1.3::cierre` · cap · punto 3.1.3 · bloque_cierre · págs. 34

- PDF: `data/experiment/subset/TO_capitales_minimos_actual.pdf#page=34`

> *heredado (encabezado, S3, p. 29):* Sección 3. Capital mínimo por riesgo de crédito. Titulizaciones e inversiones en fon- dos.
>
> *heredado (encabezado, 3.1, p. 29):* 3.1. Tratamiento de las titulizaciones.
>
> *heredado (encabezado, 3.1.3, p. 33):* 3.1.3. Requisitos de debida diligencia.
>
> *propio:* Cuando no se cumpla con alguno de estos requisitos de debida diligencia se deberá ponderar la posición de titulización al 1250 %. De tratarse de una entidad originante, de- berá considerarse lo dispuesto en el punto 3.1.12.

- tramo del origen: «Cuando no se cumpla con alguno de estos requisitos de debida diligencia» (literal: exacta)
- tramo del destino: «se deberá ponderar la posición de titulización al 1250 %» (literal: exacta)

---

## V026 · `limita` · lote_02, 6 de 10

**Origen** — Restriccion «Límite monto acumulado vencimientos capital nuevo endeudamiento» (`Restriccion_el_monto_acumulado_de_los_vencimientos_de_capital_del_nuevo_endeudamiento_no_pod_60b35d`)

- descripción: El monto acumulado de los vencimientos de capital del nuevo endeudamiento no podrá superar, hasta la fecha de vencimiento de la deuda que se cancela, el monto que hubieran acumulado los vencimientos de capital de la deuda que se cancela.
- tipo: limite_cuantitativo
- umbrales (1):
  - comparacion: maximo_inclusivo; tramo: en ningún momento podrá superar, hasta la fecha de vencimiento de la deuda que se cancela

**Predicado** — `limita`

**Destino** — Operacion «Precancelación de capital e intereses con liquidación de nuevo título» (`Operacion_precancelacion_de_capital_e_intereses_con_liquidacion_de_nuevo_titulo__ext_3_6_4_c4c784`)

- descripción: Precancelación de capital e intereses de un título de deuda comprendido en el punto 3.6 con liquidación simultánea de fondos ingresados desde el exterior por emisión de nuevo título de deuda comprendido en el punto 3.5, en marco de operación de refinanciación, recompra y/o rescate anticipado.
- tipo: Precancelación de deuda con refinanciación

**Evidencia 1 de 1** — `ext::3.6.4.4` · ext · punto 3.6.4.4 · punto_propio · págs. 30, 31

- PDF: `data/experiment/subset/TO_exterior_cambios_actual.pdf#page=30` · `data/experiment/subset/TO_exterior_cambios_actual.pdf#page=31`

> *heredado (encabezado, S3, p. 16):* Sección 3. Disposiciones específicas para los egresos por el mercado de cambios
>
> *heredado (chapeau_seccion, S3, p. 16):* Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–, adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables.
>
> *heredado (encabezado, 3.6, p. 28):* 3.6. Pagos de títulos de deuda u otros valores representativos de deuda denominados y
>
> *heredado (intro, 3.6, p. 28):* pagaderos en moneda extranjera en el país y obligaciones en moneda extranjera entre residentes.
>
> *heredado (encabezado, 3.6.4, p. 29):* 3.6.4. El acceso al mercado de cambios con anterioridad al vencimiento requerirá la
>
> *heredado (intro, 3.6.4, p. 29):* conformidad previa del BCRA excepto que la operación encuadre en alguna de las siguientes situaciones y se cumplan la totalidad de las condiciones estipuladas en cada caso:
>
> *propio:* 3.6.4.4. Precancelación de capital e intereses de un título de deuda comprendido en este punto 3.6. con la liquidación de fondos ingresados desde el exterior por la emisión de un nuevo título de deuda comprendido en el punto 3.5. i) la precancelación de capital sea efectuada en manera simultánea con la liquidación de los fondos ingresados desde el exterior por la emisión de un nuevo título de deuda comprendido en el punto 3.5. emitido en el marco de una operación de refinanciación, recompra y/o rescate anticipado del título de deuda. a) el nuevo título de deuda contempla 1 (un) año de gracia para el pago de capital y su vida promedio es al menos 2 (dos) años mayor a la vida promedio remanente del título de deuda que se precancela; y b) el monto acumulado de los vencimientos de capital del nuevo endeudamiento en ningún momento podrá superar, hasta la fecha de vencimiento de la deuda que se cancela, el monto que hubieran acumulado los vencimientos de capital de la deuda que se cancela. ii) la precancelación de intereses corresponde a los intereses devengados por la deuda refinanciada hasta la fecha de cierre de la operación de recompra y/o rescate, sin necesidad de que exista una liquidación de fondos por el monto equivalente; Adicionalmente, la entidad podrá darle acceso al mercado de cambios al cliente para: iii) pagar en concepto de prima de recompra, de rescate anticipado o similar hasta el equivalente del 5% (cinco por ciento) del monto del capital del título de deuda recomprado y/o rescatado, en la medida que el pago se concrete de manera simultánea con una liquidación de fondos ingresados desde el exterior por el nuevo título de deuda que exceda al monto de capital que se precancela, como mínimo, por un monto equivalente al monto de la prima abonada. iv)pagar a la fecha de cierre de la operación de recompra y/o rescate, sin necesidad de que exista una liquidación de fondos por el monto equivalente, los gastos de emisión u otros servicios prestados por no residentes en el marco de la emisión de los nuevos títulos de deuda emitidos y/o la operación de recompra y/o rescate.

- tramo del origen: «el monto acumulado de los vencimientos de capital del nuevo endeudamiento en ningún momento podrá superar, hasta la fecha de vencimiento de la deuda que se cancela, el monto que hubieran acumulado los vencimientos de capital de la deuda que se cancela.» (literal: exacta)
- tramo del destino: «Precancelación de capital e intereses de un título de deuda comprendido en este punto 3.6. con la liquidación de fondos ingresados desde el exterior por la emisión de un nuevo título de deuda comprendido en el punto 3.5.» (literal: exacta)

---

## V027 · `limita` · lote_02, 7 de 10

**Origen** — Restriccion «Límite importe reducción — partida 70300000» (`Restriccion_el_importe_de_la_reduccion_de_exigencia_debe_ser_inferior_al_registrado_en_la_pa_8cda96`)

- descripción: El importe de la reducción de exigencia debe ser inferior al registrado en la partida 70300000
- tipo: limite_cualitativo

**Predicado** — `limita`

**Destino** — Operacion «Reducción exigencia Entidad B calificación 1-3» (`Operacion_reduccion_exigencia_entidad_b_calificacion_1_3__ric_5_1_3_3_6f65e8`)

- descripción: Reducción de exigencia reflejada en partida 36000002 con porcentaje del 11 % para Entidad B, calculada como 70300000 - [0.11 * (ERC(n-1) + ... + ERC(n-36)) / 36], siempre que el importe resulte inferior al registrado en la partida 70300000
- tipo: Reducción de exigencia por riesgo operacional

**Evidencia 1 de 1** — `ric::5.1.3.3` · ric · punto 5.1.3.3 · punto_propio · págs. 23, 24

- PDF: `data/experiment/subset/TO_regimen_informativo_contable_mensual_actual.pdf#page=23` · `data/experiment/subset/TO_regimen_informativo_contable_mensual_actual.pdf#page=24`
- avisos de E0: {"contenido_tabular": true, "evidencia_tabular": ["Calificación Entidad % Partida Cómputo", "B 11 36000002 70300000 - [0.11 * ( ERC(n-1) + ... + ERC(n-36)) / 36]", "C 8 36000005 70300000 - [0.08 * ( ERC(n-1) + ... + ERC(n-36)) / 36]"], "tablas_e0": [{"tabla": "ric::tabla016", "origen": "e0_tablas", "estado": "parseada", "paginas": [24], "serializada": true, "bloque": "ric::tabla016", "modo": "columnas", "celdas_propagadas": 2, "celdas_con_alcance": 0, "combinadas_sin_propagar": 0, "filas_subtitulo": 0}]}

> *heredado (encabezado, S5, p. 21):* Sección 5. Exigencia por riesgo operacional
>
> *heredado (encabezado, 5.1, p. 21):* 5.1. Normas de procedimiento
>
> *heredado (encabezado, 5.1.3, p. 23):* 5.1.3. Reducción de la exigencia para entidades financieras del Grupo 2 que pertenezcan a
>
> *heredado (intro, 5.1.3, p. 23):* los Grupos “A”, “B” y “C”.
>
> *propio:* 5.1.3.3. Reducción. Límites especiales. Cuando la calificación de la entidad en todos los aspectos previstos en las perti- nentes disposiciones normativas permita la aplicación de porcentajes menores a los indicados en el punto 5.1.3.2., las reducciones de exigencia resultantes se reflejarán en las partidas 36000002, 36000003, 36000005 o 36000006 -siempre que su importe resulte inferior al registrado en la partida 70300000-, conforme se explicita seguidamente: [TABLA ric::tabla016 | página 24 | e0_tablas | columnas] Columnas: Calificación | col2 | Entidad | % | Partida | Cómputo Fila 1: Calificación = 1, 2 o 3 | Entidad = B | % = 11 | Partida = 36000002 | Cómputo = 36  70300000 - [0.11 * ( ERC(n-1) + ... + ERC(n-36)) / 36] 1 Fila 2: Calificación = 1, 2 o 3 ⟨combinada con fila 1⟩ | Entidad = C | % = 8 | Partida = 36000005 | Cómputo = 3 6  70300000 - [0.08 * ( ERC(n-1) + ... + ERC(n-36)) / 36] 1 Fila 3: Calificación = 1 o 2 | Entidad = B | % = 7 | Partida = 36000003 | Cómputo = 3 6  70300000 - [0.07 * ( ERC(n-1) + ... + ERC(n-36)) / 36] 1 Fila 4: Calificación = 1 o 2 ⟨combinada con fila 3⟩ | Entidad = C | % = 5 | Partida = 36000006 | Cómputo = 3 6  70300000 - [0.05 * ( ERC(n-1) + ... + ERC(n-36)) / 36] 1 [FIN TABLA ric::tabla016] A estos efectos, se considerará la última calificación informada para el cálculo de la exigencia que corresponda integrar al tercer mes siguiente a aquel en que tenga lugar la notificación.

- tramo del origen: «siempre que su importe resulte inferior al registrado en la partida 70300000» (literal: exacta)
- tramo del destino: «las reducciones de exigencia resultantes se reflejarán en las partidas 36000002, 36000003, 36000005 o 36000006» (literal: exacta)

---

## V028 · `limita` · lote_02, 8 de 10

**Origen** — Restriccion «Requerimiento capital no superior — CRC reconocidas» (`Restriccion_el_requerimiento_de_capital_para_una_exposicion_crediticia_con_coberturas_de_rie_2026d3`)

- descripción: El requerimiento de capital para una exposición crediticia con coberturas de riesgo de crédito (CRC) reconocidas no podrá ser superior al requerimiento asignado a una operación idéntica sin tales coberturas. Aplica a créditos, títulos valores y responsabilidades eventuales que den lugar a posiciones de titulización.
- tipo: limite_cualitativo

**Predicado** — `limita`

**Destino** — Operacion «Exposición crediticia con CRC reconocidas» (`Operacion_exposicion_crediticia_con_crc_reconocidas__cap_5_2_1_4_785a0e`)

- descripción: Exposición crediticia que incluye créditos, títulos valores y responsabilidades eventuales que den lugar a posiciones de titulización, en la que se utilizan técnicas de cobertura del riesgo de crédito (CRC) reconocidas en la sección 5.
- tipo: operación de crédito con cobertura

**Evidencia 1 de 1** — `cap::5.2.1.4` · cap · punto 5.2.1.4 · punto_propio · págs. 99

- PDF: `data/experiment/subset/TO_capitales_minimos_actual.pdf#page=99`

> *heredado (encabezado, S5, p. 98):* Sección 5. Cobertura del riesgo de crédito.
>
> *heredado (chapeau_seccion, S5, p. 98):* A los efectos del cómputo de la exigencia de capital por riesgo de crédito, se reconocerá –total o parcialmente– la cobertura del riesgo de crédito (CRC) de las operaciones registradas en la cartera de inversión –tales como préstamos y responsabilidades eventuales– mediante la utilización de las técnicas previstas en el punto 5.1. La presente sección contempla, además, el cálculo de la exposición a las operaciones de financia- ción con títulos valores (securities financing transactions, SFT) –conforme a lo previsto en la Sec- ción 4.–, registradas tanto en la cartera de inversión como en la cartera de negociación.
>
> *heredado (encabezado, 5.2, p. 99):* 5.2. Requisitos para la aplicación de técnicas de coberturas del riesgo de crédito.
>
> *heredado (encabezado, 5.2.1, p. 99):* 5.2.1. Requisitos generales.
>
> *propio:* 5.2.1.4. Ninguna exposición crediticia –incluyendo créditos, títulos valores y responsabi- lidades eventuales que den lugar a posiciones de titulización– en la que se utili- cen CRC reconocidas en esta sección originará un requerimiento de capital su- perior al asignado a otra operación idéntica que no cuente con tales coberturas.

- tramo del origen: «Ninguna exposición crediticia –incluyendo créditos, títulos valores y responsabilidades eventuales que den lugar a posiciones de titulización– en la que se utilicen CRC reconocidas en esta sección originará un requerimiento de capital superior al asignado a otra operación idéntica que no cuente con tales coberturas» (literal: exacta)
- tramo del destino: «exposición crediticia –incluyendo créditos, títulos valores y responsabilidades eventuales que den lugar a posiciones de titulización– en la que se utilicen CRC reconocidas en esta sección» (literal: exacta)

---

## V029 · `aplica_a` · lote_02, 9 de 10

**Origen** — Obligacion «Revisión periódica de clasificación con constancia» (`Obligacion_las_entidades_obligadas_a_clasificar_deudores_deben_efectuar_la_revision_de_clas_418f0f`)

- descripción: Las entidades obligadas a clasificar deudores deben efectuar la revisión de clasificación con la periodicidad mínima que se especifica en los ítems siguientes, dejando constancia de ello en el legajo del cliente analizado.
- tipo: otra
- frecuencia: como mínimo con la periodicidad que se indica seguidamente

**Predicado** — `aplica_a`

- tramo del sujeto: «los sujetos obligados» (literal: no)

**Destino** — Sujeto «Obligados a clasificar deudores (Clasificación)» (`Sujeto_rol_obligado_a_clasificar_clasificacion`)

- descripción: —
- nivel: rol

**Evidencia 1 de 1** — `cla::6.3::intro` · cla · punto 6.3 · bloque_intro · págs. 17

- PDF: `data/experiment/subset/TO_clasificacion_deudores_actual.pdf#page=17`

> *heredado (encabezado, S6, p. 17):* Sección 6. Clasificación de los deudores de la cartera comercial.
>
> *heredado (encabezado, 6.3, p. 17):* 6.3. Periodicidad mínima de clasificación.
>
> *propio:* La revisión deberá efectuarse como mínimo con la periodicidad que se indica seguidamente, dejando constancia de ello en el legajo del cliente analizado:

- tramo del origen: «La revisión deberá efectuarse como mínimo con la periodicidad que se indica seguidamente, dejando constancia de ello en el legajo del cliente analizado» (literal: exacta)
- tramo del destino: —

---

## V030 · `exceptua_obligacion` · lote_02, 10 de 10

**Origen** — Excepcion «Excepción — aportes en especie con autorización SEFyC» (`Excepcion_excepcionalmente_mediando_autorizacion_previa_de_la_sefyc_podran_admitirse_aport_e91a54`)

- descripción: Excepcionalmente, mediando autorización previa de la SEFyC, podrán admitirse aportes en especie, exceptuando así la exigencia de efectivo.

**Predicado** — `exceptua_obligacion`

**Destino** — Obligacion «Efectuar aportes en efectivo» (`Obligacion_los_aportes_de_capital_deben_ser_efectuados_en_efectivo_a_los_fines_de_todas_las_6e3ef1`)

- descripción: Los aportes de capital deben ser efectuados en efectivo, a los fines de todas las reglamentaciones vinculadas al capital, su integración y aumento, inclusive los referidos a planes de regularización y saneamiento.
- tipo: otra

**Evidencia 1 de 1** — `cap::8.6::intro` · cap · punto 8.6 · bloque_intro · págs. 169

- PDF: `data/experiment/subset/TO_capitales_minimos_actual.pdf#page=169`

> *heredado (encabezado, S8, p. 154):* Sección 8. Responsabilidad patrimonial computable.
>
> *heredado (encabezado, 8.6, p. 169):* 8.6. Aportes de capital.
>
> *propio:* A los fines de todas las reglamentaciones vinculadas al capital, su integración y aumento, in- clusive los referidos a planes de regularización y saneamiento y sin perjuicio de lo previsto en los puntos 5.1. a 5.3. de las normas sobre “Autorización y composición del capital de entidades financieras” en materia de negociación de acciones o de aportes irrevocables para futuros au- mentos de capital, los aportes deben ser efectuados en efectivo. Excepcionalmente, mediando autorización previa de la SEFyC, podrán admitirse aportes en:

- tramo del origen: «Excepcionalmente, mediando autorización previa de la SEFyC, podrán admitirse aportes en» (literal: exacta)
- tramo del destino: «los aportes deben ser efectuados en efectivo» (literal: exacta)

---

