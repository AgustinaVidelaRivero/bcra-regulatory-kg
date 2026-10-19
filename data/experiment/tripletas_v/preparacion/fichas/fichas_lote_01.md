# U-TRIP-V: fichas del lote 01 (10)

Acta del sorteo `acta_sorteo_V.json` (sha256 `5d6a237e510bcf086db717061dd146eaa9b3181006cb7b1d300164436c720c55`), sellada a las 2026-10-19T14:23:55-03:00; fichas generadas a las 2026-10-19T14:25:19-03:00. Grafo KG-Tanda0-Desarrollo-r2b-sincola-rs1 (`66e745f5…`). Las fichas van en el orden sellado. Criterio (§3.4 del pre-registro): la evidencia sostiene la relación entre esos dos nodos, con sus sujetos, valores, calificadores y modalidad.

Cada ficha trae los dos nodos (tipo, etiqueta, descripción y propiedades), el predicado y la evidencia de cada procedencia: el texto heredado y el propio de la unidad de E0, el tramo literal de cada extremo en esa unidad si lo hay, las páginas y la ruta del PDF con la página. «literal» dice si el tramo está tal cual en el texto (exacta), por tokens (tokens) o no (no).

## V011 · `condicion_de` · lote_01, 1 de 10

**Origen** — Condicion «Títulos ingresados y/o liquidados en mercado de cambios» (`Condicion_titulos_ingresados_y_o_liquidados_en_mercado_de_cambios__la_operacion_de_pago_de_f515ee`)

- descripción: La operación de pago de títulos de deuda solo aplica cuando los títulos fueron ingresados y/o liquidados en el mercado de cambios.

**Predicado** — `condicion_de`

**Destino** — Operacion «Pago de títulos de deuda con registro en país» (`Operacion_pago_de_titulos_de_deuda_con_registro_en_pais__ext_14_2_1_3_4a3d61`)

- descripción: Pago de otras emisiones de títulos de deuda con registro en el país, denominados en moneda extranjera, que fueron ingresados y/o liquidados en el mercado de cambios. Operación de egreso en el marco del acceso al mercado de cambios para VPU adheridos al RIGI.
- tipo: pago de títulos de deuda

**Evidencia 1 de 1** — `ext::14.2.1.3` · ext · punto 14.2.1.3 · punto_propio · págs. 176

- PDF: `data/experiment/subset/TO_exterior_cambios_actual.pdf#page=176`

> *heredado (encabezado, S14, p. 175):* Sección 14. Disposiciones complementarias asociadas al Régimen de Incentivo para Grandes Inversiones (RIGI).
>
> *heredado (chapeau_seccion, S14, p. 175):* En esta sección se detallan las disposiciones complementarias en materia cambiaria que, en la medida que las disposiciones generales no resulten más favorables, resultan aplicables a un Vehículo de Proyecto Único (VPU) adherido al Régimen de Incentivo los referidas al “Régimen de Incentivo para Grandes Inversiones” (RIGI) establecido en el Título VII de la Ley 27.742 y reglamentado por el Decreto 749/24 y concordantes.
>
> *heredado (encabezado, 14.2, p. 176):* 14.2. Beneficios relacionados con el acceso al mercado de cambios para operaciones de egreso.
>
> *heredado (intro, 14.2, p. 176):* Adicionalmente lo previsto en la normativa general en materia de egresos por el mercado de cambios, en la medida que se cumplan los restantes requisitos aplicables a cada operación, por aquellas financiaciones o aportes de inversión directa recibidos por el VPU adherido a partir de la vigencia de la Ley 27.742, las entidades podrán también dar acceso en las siguientes situaciones:
>
> *heredado (encabezado, 14.2.1, p. 176):* 14.2.1. En el marco de lo dispuesto en los puntos 3.3., 3.5., 3.6. y 10.3.2., según
>
> *heredado (intro, 14.2.1, p. 176):* corresponda, sin necesidad de contar con la conformidad previa del BCRA si tal requisito estuviese vigente, las entidades podrán darle acceso al cliente para pagar, incluso antes de la fecha de vencimiento, los intereses devengados hasta la fecha de acceso que se encuentren impagos y/o el capital pendiente de:
>
> *heredado (cierre, 14.2.1, p. 177):* En el caso de que la totalidad de los fondos obtenidos por la financiación no pudiese ser computada como ingresada y liquidada en el mercado de cambios, las entidades también podrán dar acceso al VPU adherido, sin necesidad de contar con la conformidad previa del BCRA si tal requisito estuviese vigente, para realizar:
>
> *heredado (cierre, 14.2.1, p. 177):* i) pagos de intereses devengados hasta la fecha de acceso que se encuentren
>
> *heredado (cierre, 14.2.1, p. 177):* impagos y que correspondan a la porción del capital equivalente a la proporción de los fondos recibidos por el VPU por la financiación que puede computarse como ingresada y liquidada por el mercado de cambios.
>
> *heredado (cierre, 14.2.1, p. 177):* ii) pagos por capital adeudado que corresponda a la porción del capital
>
> *heredado (cierre, 14.2.1, p. 177):* equivalente a la proporción de los fondos recibidos por el VPU por la financiación que puede computarse como ingresada y liquidada por el mercado de cambios.
>
> *propio:* 14.2.1.3. otras emisiones de títulos de deuda con registro en el país denominados en moneda extranjera y que fueron ingresados y/o liquidados en el mercado de cambios.

- tramo del origen: «que fueron ingresados y/o liquidados en el mercado de cambios» (literal: exacta)
- tramo del destino: «otras emisiones de títulos de deuda con registro en el país denominados en moneda extranjera y que fueron ingresados y/o liquidados en el mercado de cambios» (literal: exacta)

---

## V012 · `aplica_a` · lote_01, 2 de 10

**Origen** — Restriccion «Riesgo de crédito de contraparte — garantías no protegidas contra quiebra» (`Restriccion_cuando_activos_se_coloquen_en_garantia_sin_proteccion_contra_quiebra_de_ccp_o_mi_c21c75`)

- descripción: Cuando activos se coloquen en garantía sin protección contra quiebra de CCP o miembro compensador, entidad financiera debe reconocer riesgo de crédito por posibilidad de pérdidas por calidad crediticia de entidad que recibe garantía.
- tipo: limite_cualitativo

**Predicado** — `aplica_a`

- tramo del sujeto: «la entidad financiera que constituye la garantía» (literal: exacta)

**Destino** — Sujeto «Entidades alcanzadas (Capitales Mínimos)» (`Sujeto_rol_alcance_capmin`)

- descripción: —
- nivel: rol

**Evidencia 1 de 1** — `cap::4.3.3.1` · cap · punto 4.3.3.1 · punto_propio · págs. 88, 89, 90, 91, 92

- PDF: `data/experiment/subset/TO_capitales_minimos_actual.pdf#page=88` · `data/experiment/subset/TO_capitales_minimos_actual.pdf#page=89` · `data/experiment/subset/TO_capitales_minimos_actual.pdf#page=90` · `data/experiment/subset/TO_capitales_minimos_actual.pdf#page=91` · `data/experiment/subset/TO_capitales_minimos_actual.pdf#page=92`

> *heredado (encabezado, S4, p. 63):* Sección 4. Capital mínimo por riesgo de crédito de contraparte.
>
> *heredado (encabezado, 4.3, p. 85):* 4.3. Exigencia de capital por riesgo de crédito de contraparte en operaciones con entidades de
>
> *heredado (intro, 4.3, p. 85, 86):* contraparte central. Comprende a aquellas exposiciones de las entidades financieras con entidades de contrapar- te central (CCP) que se originen en derivados OTC o negociados en mercados de valores y en operaciones de financiación con títulos valores (“Securities Financing Transactions”, SFT) y operaciones de liquidación diferida –definidas en el punto 4.2.–. No están comprendidas las exposiciones originadas en operaciones al contado y que involu- cren títulos valores, oro o moneda extranjera, cuya exigencia de capital se calculará conforme a lo previsto en el punto 4.1.
>
> *heredado (encabezado, 4.3.3, p. 88):* 4.3.3. Exposiciones a entidades de contraparte central calificadas.
>
> *propio:* 4.3.3.1. Exposiciones por operaciones de negociación. i) Exposiciones de los miembros compensadores con las CCP. a) La entidad financiera que actúe en carácter de miembro compensa- dor de una CCP por operaciones propias deberá aplicar un pondera- dor de riesgo del 2 % a sus exposiciones con la CCP originadas en operaciones de derivados –OTC o negociados en mercados de valo- res–, de financiación con títulos valores (SFT) y de liquidación diferi- da. Cuando la entidad financiera preste servicios de compensación a clientes, aplicará el ponderador de riesgo del 2 % a la exposición con la CCP que se origina si, en caso de incumplimiento de la CCP, la entidad financiera se viera obligada –como miembro compensador a reembolsar al cliente toda pérdida debido al cambio de valor de sus transacciones. El ponderador de riesgo aplicado a los activos en ga- rantía aportados por la entidad financiera a una CCP deberá determi- narse de acuerdo con lo establecido en los párrafos primero a tercero del acápite iv) del presente punto. b) La exposición debida a dichas operaciones se calculará conforme al enfoque estandarizado para el riesgo de crédito de contraparte (SA- CCR) establecido en el punto 4.2. para los derivados OTC o negó ciados en mercados de valores y operaciones de liquidación diferida, y a lo previsto en la Sección 5. para las SFT. No se aplicará el plazo mínimo de veinte días hábiles para el cálculo del período de riesgo de margen (MPOR) de los conjuntos de neteo en los que se verifiquen más de 5.000 operaciones en la medida en que no existan disputas pendientes y que dicho conjunto no contenga garantías ilíquidas u operaciones exóticas. Idéntico criterio se aplica- rá para la determinación del período de mantenimiento mínimo (T ) M utilizado en el cálculo de los aforos de las SFT previsto en el punto 5.3.2.3. En todos los casos, se utilizará un MPOR mínimo de 10 días para el cálculo de las exposiciones a una CCP por operaciones de derivados OTC. Cuando la CCP reciba el margen de variación de una operación y el activo propiedad del miembro compensador no esté protegido contra la insolvencia de la CCP, el horizonte temporal de riesgo mínimo a aplicar a dichas exposiciones será el menor entre 1 año y el plazo re- sidual de la operación, con un plazo mínimo de 10 días hábiles. c) En las operaciones con CCP radicadas en jurisdicciones en las cua- les la liquidación por saldos netos en caso de incumplimiento tenga validez legal y con independencia de si la contraparte es insolvente o se ha declarado en quiebra, el costo de reposición total de todos los contratos relevantes para determinar la exposición por operaciones podrá calcularse como un costo de reposición neto, siempre que el conjunto de operaciones compensables aplicable a dicha liquidación cumpla con los requisitos que en materia de validez legal se estable- cen en: i. el punto 5.3.2.5. para las SFT y ii. el acápite ii) del punto 4.2.1.1. en el caso de las operaciones con derivados. En la medida en que las disposiciones antes referidas contengan la expresión “acuerdo marco de neteo” o la frase “un contrato de neteo con una contraparte u otro acuerdo”, deberá interpretarse que incluye a todo acuerdo de neteo con validez legal que reconozca derechos de compensación legalmente exigibles. Si la entidad financiera no pudiese demostrar que los acuerdos de neteo cumplen estos reque- rimientos, cada transacción individual se considerará como un con- junto de neteo en sí misma a los efectos de calcular la exposición por operaciones. ii) Exposiciones de los miembros compensadores con sus clientes. El miembro compensador considerará su exposición con un cliente –incluyendo la potencial exposición al riesgo CVA– como una operación bilateral, independientemente de que el miembro compensador garantice la operación o actúe como un intermediario entre el cliente y la CCP. Sin embargo, como el período de liquidación (close-out) para las operaciones compensadas de los clientes es más corto, los miembros compensado- res podrán calcular la exigencia por la exposición a sus clientes aplicando un período de riesgo de margen que sea, como mí- nimo, de 5 días. La EAD reducida se utilizará también para el cálculo del ajuste de valuación de crédito –CVA– establecido en el punto 4.2.3. Si un miembro compensador recibe activos en garantía por las opera- ciones a compensar del cliente y las transfiere a la CCP, el miembro compensador podrá reconocer esta garantía tanto para el tramo CCP- miembro compensador como para el tramo miembro compensador- cliente de la operación. El margen inicial aportado por los clientes al miembro compensador mitigará su exposición respecto de sus clientes. Similar tratamiento se aplicará a las estructuras multinivel de clientes –entre clientes de nivel superior e inferior–. iii) Exposiciones de los clientes. Si la entidad financiera es cliente de un miembro compensador y realiza una transacción en la que el miembro compensador actúa como inter- mediario financiero –es decir, el miembro compensador realiza una transacción con la CCP por indicación del cliente–, la exposición de la entidad financiera hacia el miembro compensador podrá recibir el trata- miento del acápite i) precedente, siempre que se cumplan las siguientes condiciones: a) La CCP identifica a las transacciones a compensar como transac- ciones de clientes y las garantías que las amparan son mantenidas por la CCP y/o el miembro compensador, según sea el caso, bajo acuerdos que impiden que el cliente sufra pérdidas debido a: i. la falta de pago o la insolvencia del miembro compensador; ii. la falta de pago o la insolvencia de los demás clientes del miembro com- pensador; y iii. la falta de pago o la insolvencia conjuntas del miem- bro compensador y cualquiera de sus otros clientes. Esto implica que, en caso de impago o insolvencia del miembro compensador, no habrá impedimentos legales –salvo la necesidad de obtener una orden judicial, a la cual el cliente tiene derecho– para transferir la garantía que pertenece a los clientes de ese miembro compensador a la CCP, a otro u otros miembros compensadores, al cliente o a quien éste designe. El cliente deberá haber realizado una revisión legal adecuada –y llevar a cabo esas revisiones cuando sea necesario a fin de asegu- rar una continua aplicabilidad– y contar con fundamentos que per- mitan concluir que esos acuerdos serán legales, válidos, vinculan- tes y exigibles bajo las leyes aplicables en la/s jurisdicción/es rele- vante/s. b) Las leyes, regulaciones y acuerdos contractuales o administrativos aplicables hacen que sea altamente probable la portabilidad de las transacciones. Esto es que las transacciones compensadoras reali- zadas a través del miembro compensador en situación de impago o insolvencia serán concluidas indirectamente a través de la CCP o por la CCP. En tal caso, las posiciones y garantías del cliente con la CCP serán transferidas a valor de mercado, a menos que el cliente peti- cione cerrar las posiciones a valor de mercado. Idénticas condiciones se deberán cumplir para que la entidad financiera dé ese tratamiento a su exposición con una CCP por transacciones reali- zadas en calidad de cliente en las que su cumplimiento es garantizado por un miembro compensador y para las exposiciones de los clientes de nivel inferior con los clientes de nivel superior en las estructuras multini- veles, siempre que en todos los niveles de los clientes involucrados se cumplan las dos condiciones de este acápite. Cuando el cliente no esté protegido de sufrir pérdidas en caso de falta de pago o insolvencia conjunta del miembro compensador y alguno de sus clientes, pero se cumplan todas las restantes condiciones anteriormente expuestas, la exposición del cliente con el miembro compensador o fren- te al cliente de mayor nivel, respectivamente, recibirá un ponderador de riesgo del 4%. Cuando la entidad financiera sea cliente del miembro compensador y no se cumplan estos requisitos, la exposición con el miembro compensador, incluida –de corresponder– la exposición potencial por riesgo CVA, se deberá tratar como una operación bilateral. iv) Tratamiento de las garantías. Todo activo que la entidad financiera constituya en garantía de estas operaciones recibirá el ponderador que le corresponda de acuerdo con lo previsto en estas normas, considerando a ese efecto qué tratamiento –cartera de negociación o de inversión– hubiera recibido en caso de no haber sido depositado en la CCP. Cuando los activos de un miembro compensador o cliente se coloquen en garantía a favor de una CCP o miembro compensador, pero de modo que no queden protegidos de su quiebra, la entidad financiera que constituye la garantía deberá reconocer además el riesgo de crédito que se deriva de la posibilidad de sufrir pér- didas por la calidad crediticia de la entidad que recibe los activos en ga- rantía. Es decir que, independientemente de la cartera a la que estén asignados, los activos constituidos en garantía estarán sujetos también al requisito de riesgo de crédito de contraparte (SA-CCR) establecido en el punto 4.2., incluido el incremento por los aforos descriptos en el punto 5.3.2.3., computados de acuerdo con lo previsto en el acápite v) del pun- to 4.2.1.1. Cuando la entidad que reciba los activos en garantía sea la CCP, se aplicará un ponderador del 2 % a las garantías incluidas en la definición de exposición por operaciones. El ponderador de riesgo correspondien- te a la CCP se aplicará a los activos o las garantías aportados para otros fines. La garantía depositada que no esté resguardada en caso de quiebra deberá ser considerada para el Monto Neto de Garantía Inde- pendiente (NICA) previsto en el acápite v) del punto 4.2.1.1. La garantía constituida por el miembro compensador –incluyendo efec- tivo, títulos valores y otros activos constituidos como garantías, así co- mo los excesos a los márgenes inicial o de variación– mantenida por un custodio y protegida de la quiebra de la CCP, no está sujeta a la exi- gencia de capital por la exposición al riesgo de crédito de contraparte –esto es, el ponderador de riesgo o la EAD es igual a cero–. A ese efec- to, se entiende por custodio a un fiduciario o agente que mantenga los activos bajo un título que no le acuerde ni al custodio ni a sus acreedo- res un derecho o participación sobre ellos y que garantice que no se podrá obstaculizar judicialmente la devolución de los activos en caso de quiebra o insolvencia del custodio. La garantía constituida por un cliente, mantenida por un custodio y pro- tegida de la quiebra de la CCP y del miembro compensador y sus otros clientes no está sujeta a exigencia de capital por riesgo de crédito de contraparte. Si la garantía es mantenida por la CCP y no está protegida de su quiebra se le deberá aplicar el ponderador de riesgo del 2 % en caso de que se cumplan las condiciones a) y b) del acápite iii), o del 4 % si se da el caso del anteúltimo párrafo del acápite iii).

- tramo del origen: «Cuando los activos de un miembro compensador o cliente se coloquen en garantía a favor de una CCP o miembro compensador, pero de modo que no queden protegidos de su quiebra, la entidad financiera que constituye la garantía deberá reconocer además el riesgo de crédito que se deriva de la posibilidad de sufrir pérdidas por la calidad crediticia de la entidad que recibe los activos en garantía.» (literal: exacta)
- tramo del destino: —

---

## V013 · `aplica_a` · lote_01, 3 de 10

**Origen** — Obligacion «Notificación con antelación mínima de 60 días» (`Obligacion_el_usuario_de_servicios_financieros_debe_ser_notificado_de_las_modificaciones_qu_89ecc2`)

- descripción: El usuario de servicios financieros debe ser notificado de las modificaciones que aplicará el sujeto obligado con una antelación mínima de sesenta (60) días corridos a su entrada en vigencia.
- tipo: comunicacion_a_cliente
- umbrales (1):
  - valor: 60; unidad: dias; comparacion: minimo_inclusivo; dias_tipo: corridos; tramo: antelación mínima de sesenta (60) días corridos

**Predicado** — `aplica_a`

- tramo del sujeto: «el sujeto obligado» (literal: exacta)

**Destino** — Sujeto «Sujetos obligados (Protección de usuarios)» (`Sujeto_rol_sujeto_obligado_proteccion`)

- descripción: —
- nivel: rol

**Evidencia 1 de 1** — `pro::2.3.4` · pro · punto 2.3.4 · punto_propio · págs. 13, 14, 15

- PDF: `data/experiment/subset/TO_proteccion_usuarios_servicios_financieros_actual.pdf#page=13` · `data/experiment/subset/TO_proteccion_usuarios_servicios_financieros_actual.pdf#page=14` · `data/experiment/subset/TO_proteccion_usuarios_servicios_financieros_actual.pdf#page=15`

> *heredado (encabezado, S2, p. 5):* Sección 2. Derechos básicos de los usuarios de servicios financieros.
>
> *heredado (encabezado, 2.3, p. 7):* 2.3. Recaudos mínimos de la relación de consumo.
>
> *propio:* 2.3.4. Cambios de condiciones pactadas. A fin de modificar las condiciones pactadas debe darse la totalidad de las siguientes condiciones: i) En el contrato deberán encontrarse taxativamente especificadas las condiciones que pueden ser objeto de modificación, así como los parámetros o criterios objeti- vos para su concreción, ajustándose a lo señalado en el punto 2.3.2. Los incrementos en las tasas de interés, comisiones y/o cargos, además, deben ser justificados desde el punto de vista técnico y económico, en el marco de lo dispues- to en el punto 2.3.2.1. ii) La modificación no debe alterar el objeto del contrato ni importar un desmedro res- pecto de los productos o servicios contratados. iii) Consentimiento. En el caso de que el sujeto obligado pretenda incorporar nuevos conceptos en cali- dad de comisiones y/o cargos que no hubiesen sido previstos en el contrato o re- ducir prestaciones contempladas en él, deberá previamente obtener el consenti- miento expreso del usuario de servicios financieros. Cuando se trate de modificaciones en los valores de comisiones y/o cargos debi- damente aceptados por el usuario, su consentimiento al cambio podrá quedar con- formado por la falta de objeción al mismo dentro del plazo establecido en el acápite iv). En los contratos de tarjeta de crédito el consentimiento a modificaciones en las condiciones pactadas (nuevas comisiones y/o cargos) sólo puede ser dado por el ti- tular de la cuenta. iv) Notificaciones. Forma, plazos y efectos. El usuario de servicios financieros debe ser notificado de las modificaciones que aplicará el sujeto obligado con una antelación mínima de sesenta (60) días corridos a su entrada en vigencia. Las modificaciones que resulten económicamente más beneficiosas para el usuario –por una reducción de los valores pactados– no re- quieren notificación anticipada. Las notificaciones por cambios de condiciones pactadas (nuevos conceptos y/o va- lores o reducción de prestaciones del servicio) serán en todos los casos gratuitas para el usuario de servicios financieros. Deberán efectuarse mediante documento escrito dirigido al domicilio real del usuario de servicios financieros –en forma sepa- rada de cualquier otra información que remita el sujeto obligado (resúmenes de cuenta, boletines informativos, etc.), aun cuando forme parte de la misma remesa– o por vía electrónica en aquellos casos en que ésta fuera la forma de comunica- ción. En este último caso, la notificación deberá ser clara, de fácil acceso para el usuario e incluir la fecha de emisión. En el cuerpo de estas notificaciones deberán incluirse las siguientes leyendas: - “Usted podrá optar por rescindir el contrato en cualquier momento antes de la entrada en vigencia del cambio y sin cargo alguno, sin perjuicio de que deberá cumplir las obligaciones pendientes a su cargo”. - “Usted puede consultar el “Régimen de Transparencia” elaborado por el BCRA sobre la base de la información proporcionada por los sujetos obligados a fin de comparar los costos, características y requisitos de los productos y servicios financieros, ingresando a https://www.bcra.gob.ar/regimen-de-transparencia/ Asimismo, cuando se modifique el valor de las comisiones que se detallan a con- tinuación, el cuerpo de las notificaciones deberá exhibir un cuadro comparativo para esos importes que será elaborado y oportunamente puesto a disposición por la Superintendencia de Entidades Financieras y Cambiarias (SEFYC) en el sitio https://www.bcra.gob.ar/primeras-10-entidades/ : - Caja de ahorros: emisión de tarjetas de débito adicionales; reposición de tarje- tas de débito por robo o extravío y uso de cajeros automáticos (fuera de casas operativas de la entidad, de otra entidad y en el exterior). - Tarjetas de crédito: servicio de emisión, renovación, administración o mante- nimiento de cuenta; reposición o reimpresión de tarjeta por robo o extravío y tarjetas adicionales. - Específicas de la cuenta corriente: mantenimiento de cuenta y talonario de cheques. - Paquete destinado a beneficiarios de prestaciones de la seguridad social que incluyan el servicio de adelanto de haberes jubilatorios. - Servicio de mantenimiento de paquetes.

- tramo del origen: «El usuario de servicios financieros debe ser notificado de las modificaciones que aplicará el sujeto obligado con una antelación mínima de sesenta (60) días corridos a su entrada en vigencia.» (literal: exacta)
- tramo del destino: —

---

## V014 · `requiere` · lote_01, 4 de 10

**Origen** — Operacion «Presentación de declaración jurada del cliente» (`Operacion_presentacion_de_declaracion_jurada_del_cliente__ext_3_9_3_b95a60`)

- descripción: La entidad debe contar con una declaración jurada del cliente en la que conste que el cliente cumple con los requisitos mencionados precedentemente (ingresos y/o activos consistentes con el ahorro en moneda extranjera para compra de moneda extranjera por personas humanas residentes para formación de activos externos, remisión de ayuda familiar u operaciones con derivados).
- tipo: Presentación de declaración jurada

**Predicado** — `requiere`

**Destino** — Obligacion «Obtener declaración jurada de cumplimiento de requisitos» (`Obligacion_la_entidad_debera_contar_con_una_declaracion_jurada_del_cliente_en_la_que_conste_53cf61`)

- descripción: La entidad deberá contar con una declaración jurada del cliente en la que conste que el cliente cumple con los requisitos mencionados precedentemente (posesión de ingresos y/o activos consistentes con el ahorro en moneda extranjera).
- tipo: presentacion_informativa

**Evidencia 1 de 1** — `ext::3.9.3` · ext · punto 3.9.3 · punto_propio · págs. 33

- PDF: `data/experiment/subset/TO_exterior_cambios_actual.pdf#page=33`

> *heredado (encabezado, S3, p. 16):* Sección 3. Disposiciones específicas para los egresos por el mercado de cambios
>
> *heredado (chapeau_seccion, S3, p. 16):* Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–, adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables.
>
> *heredado (encabezado, 3.9, p. 33):* 3.9. Compra de moneda extranjera por parte de personas humanas residentes para la formación
>
> *heredado (intro, 3.9, p. 33):* de activos externos bajo otras modalidades, la remisión de ayuda familiar u operaciones con derivados. Las entidades podrán dar acceso al mercado de cambios a las personas humanas residentes para la formación de activos externos (códigos de conceptos A01, A02, A03, A04, A06, A08, A14 y A24), la remisión de ayuda familiar y para la operatoria con derivados (código de con- cepto A05) en la medida que no encuadre en el punto 3.12.1., sin la conformidad previa del BCRA, en la medida que se cumplan la totalidad de los siguientes requisitos:
>
> *heredado (cierre, 3.9, p. 33):* En todos los casos, la entidad deberá obtener evidencia de que el cliente posee ingresos y/o activos consistentes con el ahorro en moneda extranjera.
>
> *propio:* 3.9.3. La entidad cuenta con una declaración jurada del cliente en la que consta que el cliente cumple con los requisitos mencionados precedentemente.

- tramo del origen: «La entidad cuenta con una declaración jurada del cliente en la que consta que el cliente cumple con los requisitos mencionados precedentemente» (literal: exacta)
- tramo del destino: «La entidad cuenta con una declaración jurada del cliente en la que consta que el cliente cumple con los requisitos mencionados precedentemente» (literal: exacta)

---

## V015 · `aplica_a` · lote_01, 5 de 10

**Origen** — Obligacion «Efectuar denuncia de falta de oficialización» (`Obligacion_la_entidad_debera_efectuar_la_correspondiente_denuncia__ext_10_4_4_c5a44a`)

- descripción: La entidad deberá efectuar la correspondiente denuncia
- tipo: comunicacion_a_cliente

**Predicado** — `aplica_a`

- tramo del sujeto: «la entidad» (literal: exacta)

**Destino** — Sujeto «Entidades autorizadas a operar en cambios (Exterior)» (`Sujeto_rol_entidad_autorizada_exterior`)

- descripción: —
- nivel: rol

**Evidencia 1 de 1** — `ext::10.4.4` · ext · punto 10.4.4 · punto_propio · págs. 142, 143

- PDF: `data/experiment/subset/TO_exterior_cambios_actual.pdf#page=142` · `data/experiment/subset/TO_exterior_cambios_actual.pdf#page=143`

> *heredado (encabezado, S10, p. 130):* Sección 10. Pagos de importaciones y otras compras de bienes en el exterior.
>
> *heredado (encabezado, 10.4, p. 138):* 10.4. Pagos de importaciones de bienes con registro de ingreso aduanero pendiente.
>
> *propio:* 10.4.4. Cancelación de garantías comerciales de importaciones de bienes otorgadas por entidades financieras locales. La entidad tendrá acceso al mercado de cambios para cancelar cartas de crédito o letras avaladas emitidas u otorgadas para garantizar operaciones de importaciones de bienes que tengan el registro aduanero pendiente, incluso cuando no se cumplan los requisitos establecidos para el acceso del cliente, en la medida que se verifique que se cumplían las condiciones que resultaban aplicables según la fecha en que se emitió u otorgó la carta de crédito o letra avalada y el tipo de operación garantizada por la entidad. En el caso de cartas de crédito o letras avaladas emitidas u otorgadas a partir del 13/12/23, la entidad deberá contar con la documentación que demuestre que, al momento de la apertura o emisión, la operación garantizada correspondía a una importación de bienes con registro de ingreso aduanero a partir de dicha fecha y, salvo que la operación quedase comprendida en la situación prevista en el punto 10.10.2.11., que el pago garantizado debía ser concretado por el cliente a partir de la fecha que resultaba de adicionar el plazo en días corridos que le correspondía al bien por el punto 10.10.1. más otros 15 (quince) días corridos a la fecha estimada de arribo de los bienes al país. Para aquellas emitidas u otorgadas a partir del 14/04/25, en la medida que se cumplan las restantes condiciones, también se admitirá que el pago garantizado tuviera que ser concretado a partir de la fecha estimada de embarque de los bienes en origen cuando correspondía a la porción de una operación por la cual el cliente hubiese podido realizar pagos a la vista en virtud de lo previsto en los puntos 10.10.2.1. o 10.10.2.2. Las condiciones aplicables para las cartas de crédito o letras avaladas emitidas u otorgadas hasta el 12/12/23 fueron oportunamente receptadas en el punto 10.3.6. del Anexo de la Comunicación A 7914. El boleto de venta deberá efectuarse a nombre de la propia entidad en calidad de cliente por el concepto “B11. Cancelación de garantías comerciales de entidades financieras de importaciones de bienes sin registro de ingreso aduanero”. Por los pagos que se realicen, la entidad deberá informar en el SEPAIMPO dentro de los 5 (cinco) días hábiles, la CUIT del importador por el cual se ha efectuado el pago. En la medida que la entidad no cuente con el registro de la oficialización del despacho de importación dentro de los 90 (noventa) días corridos de la fecha de acceso al mercado de cambios, la entidad deberá efectuar la correspondiente denuncia.

- tramo del origen: «la entidad deberá efectuar la correspondiente denuncia.» (literal: exacta)
- tramo del destino: —

---

## V016 · `exceptua` · lote_01, 6 de 10

**Origen** — Excepcion «Excepción — casa matriz de sucursales locales» (`Excepcion_no_se_deduciran_los_saldos_en_cuentas_de_corresponsalia_respecto_de_la_casa_matr_a64805`)

- descripción: No se deducirán los saldos en cuentas de corresponsalía respecto de la casa matriz de las sucursales locales de bancos del exterior o de sus sucursales y subsidiarias en otros países.

**Predicado** — `exceptua`

**Destino** — Restriccion «Deducción por mayor saldo mensual — corresponsalía» (`Restriccion_la_deduccion_se_realizara_unicamente_por_el_mayor_saldo_en_cada_banco_que_se_reg_56e8f8`)

- descripción: La deducción se realizará únicamente por el mayor saldo en cada banco que se registre durante el mes al que corresponda la determinación de la RPC.
- tipo: limite_cualitativo

**Evidencia 1 de 1** — `cap::8.4.1.3` · cap · punto 8.4.1.3 · punto_propio · págs. 162, 163

- PDF: `data/experiment/subset/TO_capitales_minimos_actual.pdf#page=162` · `data/experiment/subset/TO_capitales_minimos_actual.pdf#page=163`

> *heredado (encabezado, S8, p. 154):* Sección 8. Responsabilidad patrimonial computable.
>
> *heredado (encabezado, 8.4, p. 162):* 8.4. Conceptos deducibles.
>
> *heredado (encabezado, 8.4.1, p. 162):* 8.4.1. Conceptos deducibles del capital ordinario de nivel uno (CD ).
>
> *heredado (intro, 8.4.1, p. 162):* COn1
>
> *propio:* 8.4.1.3. Saldos en cuentas de corresponsalía respecto de bancos del exterior que no cumplan con lo previsto en el punto 3.1. de las normas sobre “Evaluaciones crediticias”. A los efectos del cumplimiento del citado punto se deberá contar con calificación internacional de riesgo comprendida en la categoría “investment grade”. Esta deducción se realizará por el mayor saldo en cada banco que se registre durante el mes al que corresponda la determinación de la RPC. A tal fin, no se deducirán los saldos en cuentas de corresponsalía que se regis- tren respecto de: i) La casa matriz de las sucursales locales de bancos del exterior o de sus sucursales y subsidiarias en otros países. ii) Los bancos u otras instituciones financieras del exterior que ejerzan el control de entidades financieras locales constituidas bajo la forma de so- ciedades anónimas. iii) Otros bancos del exterior autorizados a intervenir en los regímenes de convenios de pagos y créditos recíprocos a los que haya adherido el Ban- co Central de la República Argentina, así como sus sucursales y subsidia- rias, aun cuando ellas no estén comprendidas en esos convenios. iv) Sucursales y subsidiarias de entidades financieras locales. v) Los saldos que, con carácter transitorio y circunstancial, se originen por operaciones de clientes, tales como las vinculadas a operaciones de co- mercio exterior u otro tipo de acreditación ordenada por terceros que no impliquen responsabilidad patrimonial para la entidad.

- tramo del origen: «no se deducirán los saldos en cuentas de corresponsalía que se registren respecto de: i) La casa matriz de las sucursales locales de bancos del exterior o de sus sucursales y subsidiarias en otros países» (literal: exacta)
- tramo del destino: «Esta deducción se realizará por el mayor saldo en cada banco que se registre durante el mes al que corresponda la determinación de la RPC» (literal: exacta)

---

## V017 · `condicion_de` · lote_01, 7 de 10

**Origen** — Condicion «Condición márgenes de cobertura suficientes para pases activos» (`Condicion_condicion_margenes_de_cobertura_suficientes_para_pases_activos__la_exclusion_de__6a7450`)

- descripción: La exclusión de pases activos de dólares y títulos públicos nacionales se aplica cuando los márgenes de cobertura sean suficientes y se encuentren depositados en agentes de custodia o registro autorizados

**Predicado** — `condicion_de`

**Destino** — Excepcion «Exclusión pases activos de dólares y títulos públicos nacionales» (`Excepcion_se_excluyen_de_la_clasificacion_en_irrecuperable_los_pases_activos_de_dolares_es_c15c53`)

- descripción: Se excluyen de la clasificación en Irrecuperable los pases activos de dólares estadounidenses y de títulos valores públicos nacionales, siempre que las especies transadas cuenten con mercado de operaciones habituales y relevantes, los precios respondan a condiciones de mercado, los márgenes de cobertura sean suficientes y se encuentren depositados en BCRA (CRyL), Caja de Valores S.A., Clearstream, Euroclear o DTC

**Evidencia 1 de 1** — `cla::6.5.5.8` · cla · punto 6.5.5.8 · punto_propio · págs. 29, 30

- PDF: `data/experiment/subset/TO_clasificacion_deudores_actual.pdf#page=29` · `data/experiment/subset/TO_clasificacion_deudores_actual.pdf#page=30`

> *heredado (encabezado, S6, p. 17):* Sección 6. Clasificación de los deudores de la cartera comercial.
>
> *heredado (encabezado, 6.5, p. 19):* 6.5. Niveles de clasificación.
>
> *heredado (intro, 6.5, p. 19):* Cada cliente, y la totalidad de sus financiaciones comprendidas, se incluirá en una de las si- guientes cinco categorías, las que se definen teniendo en cuenta las condiciones que se deta- llan en cada caso. Los clientes que no registren asistencia crediticia de la entidad y que posteriormente reciban fi- nanciaciones de ésta que no superen el importe resultante de aplicar sobre el saldo de deuda registrado en el sistema financiero, según la última información disponible en la “Central de deudores” a la fecha de su otorgamiento, el porcentaje establecido en el punto 2.2.5. de las normas sobre “Previsiones mínimas por riesgo de incobrabilidad” correspondiente a la peor cla- sificación asignada, podrán ser clasificados por la entidad teniendo en cuenta únicamente el análisis del flujo de fondos proyectado. Las asistencias así otorgadas no serán consideradas a los fines a que se refiere el punto 6.6. A fin de verificar el cumplimiento de las obligaciones sin recurrir a nueva financiación directa o indirecta o a refinanciaciones, no se considerarán refinanciaciones las facilidades adicionales que se otorguen respecto de los márgenes vigentes acordados, siempre que el nuevo apoyo crediticio implique nuevos desembolsos de fondos y no supere el 10 % del cupo asignado en oportunidad de la última evaluación crediticia del cliente, en la medida en que éstas sean con- sistentes con el curso normal de los negocios y exista capacidad para atender el resto de las obligaciones financieras, ni las nuevas financiaciones y las refinanciaciones asociadas a una mayor inversión derivada de la expansión de las actividades, y siempre que pueda demostrarse que el flujo de fondos proyectado permitirá afrontar la totalidad de sus obligaciones. Tampoco se considerarán dentro de ese concepto las refinanciaciones otorgadas a los produc- tores agropecuarios cuando ello resulte de la aplicación de disposiciones vinculadas a la Ley de Emergencia Agropecuaria, sin perjuicio de lo cual, a los fines de la clasificación, deberá tenerse en cuenta el flujo de fondos proyectado para el momento en que concluya la vigencia de la emergencia declarada. El tratamiento que se dispense en ese marco no podrá implicar mejora- miento de la clasificación asignada al cliente en función de su situación individual, preexistente a la emergencia, ni su aplicación extenderse más allá de la vigencia fijada para ella.
>
> *heredado (encabezado, 6.5.5, p. 28):* 6.5.5. Irrecuperable.
>
> *heredado (intro, 6.5.5, p. 28):* Las deudas de clientes incorporados a esta categoría se consideran incobrables. Si bien estos activos podrían tener algún valor de recuperación bajo un cierto conjunto de cir- cunstancias futuras, su incobrabilidad es evidente al momento del análisis. Entre los indicadores que pueden reflejar esta situación se destacan que el cliente:
>
> *heredado (cierre, 6.5.5, p. 31):* Además, corresponderá clasificar en esta categoría a los clientes que, cualquiera sea el motivo (entre ellos por no contar con legajo o por no haber proporcionado información confiable y/o actualizada), no hayan sido evaluados con la periodicidad correspondiente, con excepción de los deudores en concurso o con acuerdo preventivo extrajudicial solici- tado o en gestión judicial que, por un período de hasta 540 días contados a partir de la apertura del concurso, solicitud del acuerdo preventivo o inicio de las gestiones judiciales de cobro, según corresponda, no hubiesen presentado la documentación que permita realizarla, siempre que se cuente con informe de abogado de la entidad financiera acreedora sobre la razonabilidad del recupero de los créditos comprendidos. Ello, sin perjuicio de que se trate de deudas que reúnan todas las condiciones previstas por el punto 2.2.3.2. de las normas sobre “Previsiones mínimas por riesgo de incobrabili- dad”.
>
> *propio:* 6.5.5.8. Bancos, otras instituciones financieras del exterior y otros prestatarios no radicados en el país que no cumplan con lo previsto en los puntos 3.1. y 3.2., según corresponda, de las normas sobre “Evaluaciones crediticias”. A los efectos del cumplimiento de los citados puntos se deberá contar con calificación internacional de riesgo comprendida en la categoría “investment grade”. Se excluirán: a) Los siguientes deudores: Casa matriz de las sucursales locales de bancos del exterior o sus filiales y subsidiarias en otros países, en la medida en que aquélla esté sujeta a super- visión sobre base consolidada. Bancos u otras instituciones financieras del exterior sujetos a supervisión so- bre base consolidada que ejerzan el control de entidades financieras locales constituidas bajo la forma de sociedades anónimas. Otros bancos del exterior autorizados a intervenir en los regímenes de conve- nios de pagos y créditos recíprocos a los que haya adherido el BCRA, así co- mo sus sucursales y subsidiarias, aun cuando ellas no estén comprendidas en esos convenios, siempre que la casa matriz o entidad bancaria controlante es- té sujeta a regímenes de supervisión sobre base consolidada, a satisfacción de la SEFyC. Sucursales y subsidiarias de entidades financieras locales sujetas al régimen de supervisión consolidada. b) Los deudores que únicamente registren las siguientes operaciones: - Financiaciones que cuenten con aval de banco del exterior que cumpla con lo previsto en el punto 3.1. de las normas sobre “Evaluaciones crediticias”, requiriendo a ese efecto calificación internacional de riesgo comprendida en la categoría “investment grade”. - Financiaciones vinculadas a operaciones de compraventa de títulos valores concertadas con residentes en el exterior, que se canalicen por la Caja de Valores S.A., Clearstream, Euroclear o Depositary Trust Company (DTC), y que se originen en el cumplimiento, por parte de la entidad financiera intervi- niente, de la obligación a su cargo (entregar la especie transada o efectuar el pago convenido) sin que la contraparte cancele su compromiso en el mismo día, en razón de modalidades de liquidación usuales en esos mercados. - Financiaciones vinculadas a operaciones de comercio exterior. - Pases activos de dólares estadounidenses y de títulos valores públicos na- cionales, siempre que:  las especies transadas cuenten con un mercado de operaciones habitua- les y relevantes,  los precios pactados respondan a las condiciones del mercado y  los márgenes de cobertura sean suficientes y se encuentren depositados en los siguientes agentes de custodia o de registro: * BCRA, por operaciones canalizadas a través de la Central de registro y liquidación de instrumentos de deuda pública, regulación monetaria y fi- deicomisos financieros (CRyL), * Caja de Valores S.A., * Clearstream, Euroclear, Depositary Trust Company (DTC) y - Asistencia crediticia concedida a través de las sucursales o subsidiarias en el exterior de entidades financieras locales sujetas al régimen de supervisión sobre base consolidada, siempre que se haya otorgado con recursos que no provengan de fondos provistos, directa o indirectamente, por las entidades financieras locales. Los deudores excluidos precedentemente deberán ser clasificados y sus deudas previsionadas conforme a las disposiciones de carácter general.

- tramo del origen: «los márgenes de cobertura sean suficientes y se encuentren depositados en los siguientes agentes de custodia o de registro» (literal: exacta)
- tramo del destino: «Pases activos de dólares estadounidenses y de títulos valores públicos nacionales, siempre que: las especies transadas cuenten con un mercado de operaciones habituales y relevantes, los precios pactados respondan a las condiciones del mercado y los márgenes de cobertura sean suficientes y se encuentren depositados en los siguientes agentes de custodia o de registro: BCRA, por operaciones canalizadas a través de la Central de registro y liquidación de instrumentos de deuda pública, regulación monetaria y fideicomisos financieros (CRyL), Caja de Valores S.A., Clearstream, Euroclear, Depositary Trust Company (DTC)» (literal: exacta)

---

## V018 · `condicion_de` · lote_01, 8 de 10

**Origen** — Condicion «Originado entre 27/08/21 y 12/12/23» (`Condicion_originado_entre_27_08_21_y_12_12_23__el_endeudamiento_debe_haber_sido_originado__3bbe41`)

- descripción: El endeudamiento debe haber sido originado entre el 27 de agosto de 2021 y el 12 de diciembre de 2023.
- umbrales (1):
  - comparacion: no_determinada; tramo: entre el 27/08/21 y el 12/12/23

**Predicado** — `condicion_de`

**Destino** — Potestad «Conformidad previa del BCRA para acceso al mercado de cambios» (`Potestad_conformidad_previa_del_bcra_para_acceso_al_mercado_de_cambios__el_bcra_tiene_la__2a81f1`)

- descripción: El BCRA tiene la facultad de otorgar conformidad previa para el acceso al mercado de cambios en los supuestos del punto 3.5.6, incluido el presente punto 3.5.6.11.

**Evidencia 1 de 1** — `ext::3.5.6.11` · ext · punto 3.5.6.11 · punto_propio · págs. 27

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
> *propio:* 3.5.6.11. se trate de un endeudamiento financiero comprendido en este punto 3.5. con una vida promedio no inferior a los 2 (dos) años originado entre el 27/08/21 y el 12/12/23, a partir de una refinanciación de deudas comerciales por la importación de bienes y servicios con el propio acreedor encuadrada en el punto 20. de la Comunicación A 7626 y concordantes (disposiciones receptadas oportunamente en el punto 3.20. del Anexo de la Comunicación A 7914). La entidad deberá contar con una certificación para el acceso al mercado de cambios emitida, dentro de los 5 (cinco) días hábiles previos, por la entidad que concretó el registro ante el BCRA con el código de concepto “P17. Registro de refinanciación de deuda comercial en el marco del punto 20. de la Comunicación A 7626”.

- tramo del origen: «originado entre el 27/08/21 y el 12/12/23» (literal: exacta)
- tramo del destino: «Se requerirá la conformidad previa del BCRA para el acceso al mercado de cambios» (literal: exacta)

---

## V019 · `condicion_de` · lote_01, 9 de 10

**Origen** — Condicion «VPU adherido al RIGI con beneficios exportaciones» (`Condicion_vpu_adherido_al_rigi_con_beneficios_exportaciones__el_cliente_es_un_vpu_adherido_31ed99`)

- descripción: El cliente es un VPU adherido al RIGI que ha declarado ante la Autoridad de Aplicación su intención de hacer uso de los beneficios del artículo 198 de la Ley 27.742 en materia de cobro de exportaciones de bienes y servicios

**Predicado** — `condicion_de`

**Destino** — Obligacion «Cumplimiento requisito complementario punto 14.4» (`Obligacion_debe_darse_cumplimiento_al_requisito_complementario_previsto_en_el_punto_14_4__e_618873`)

- descripción: Debe darse cumplimiento al requisito complementario previsto en el punto 14.4
- tipo: otra

**Evidencia 1 de 1** — `ext::3.16.5` · ext · punto 3.16.5 · punto_propio · págs. 50

- PDF: `data/experiment/subset/TO_exterior_cambios_actual.pdf#page=50`

> *heredado (encabezado, S3, p. 16):* Sección 3. Disposiciones específicas para los egresos por el mercado de cambios
>
> *heredado (chapeau_seccion, S3, p. 16):* Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–, adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables.
>
> *heredado (encabezado, 3.16, p. 42):* 3.16. Requisitos complementarios para los egresos por el mercado de cambios.
>
> *propio:* 3.16.5. VPU adherido al RIGI con beneficios en materia de cobros de exportaciones de bienes y servicios. Si el cliente fuese un Vehículo de Proyecto Único (VPU) adherido al Régimen de Incentivo para Grandes Inversiones (RIGI) que haya declarado ante la Autoridad de Aplicación que preveía hacer uso de los beneficios establecidos en el artículo 198 de la Ley 27.742 en materia de cobro de exportaciones de bienes y servicios, deberá darse cumplimiento al requisito complementario previsto en el punto 14.4.

- tramo del origen: «Si el cliente fuese un Vehículo de Proyecto Único (VPU) adherido al Régimen de Incentivo para Grandes Inversiones (RIGI) que haya declarado ante la Autoridad de Aplicación que preveía hacer uso de los beneficios establecidos en el artículo 198 de la Ley 27.742 en materia de cobro de exportaciones de bienes y servicios» (literal: exacta)
- tramo del destino: «deberá darse cumplimiento al requisito complementario previsto en el punto 14.4» (literal: exacta)

---

## V020 · `condicion_de` · lote_01, 10 de 10

**Origen** — Condicion «Operación de venta con obligación de recompra de BOPREAL» (`Condicion_operacion_de_venta_con_obligacion_de_recompra_de_bopreal__cuando_un_cliente_ha_c_c90fa6`)

- descripción: Cuando un cliente ha concretado una operación de venta con obligación de recompra utilizando bonos BOPREAL adquiridos en suscripción primaria

**Predicado** — `condicion_de`

**Destino** — Restriccion «Exclusión de venta inicial — declaraciones juradas BOPREAL» (`Restriccion_la_venta_de_los_titulos_en_el_origen_de_la_operacion_no_debe_considerarse_a_efec_031712`)

- descripción: La venta de los títulos en el origen de la operación no debe considerarse a efectos de la confección de las declaraciones juradas previstas en los puntos 3.16.3.1 y 3.16.3.2
- tipo: limite_cualitativo

**Evidencia 1 de 1** — `ext::4.8.6.1` · ext · punto 4.8.6 · herencia_encabezado · págs. 67

- PDF: `data/experiment/subset/TO_exterior_cambios_actual.pdf#page=67`

> *heredado (encabezado, S4, p. 56):* Sección 4. Otras disposiciones específicas.
>
> *heredado (encabezado, 4.8, p. 64):* 4.8. Disposiciones complementarias asociadas a los Bonos para la Reconstrucción de una
>
> *heredado (intro, 4.8, p. 64):* Argentina Libre (BOPREAL).
>
> *heredado (encabezado, 4.8.6, p. 67):* 4.8.6. En el caso de que un cliente haya concretado una operación de venta con obligación
>
> *heredado (intro, 4.8.6, p. 67):* de recompra utilizando los bonos BOPREAL adquiridos en una suscripción primaria complementariamente será aplicable lo siguiente:
>
> *propio:* 4.8.6.1. la venta de los títulos en el origen de la operación no deberá tenerse en cuenta a los efectos de la confección de las declaraciones juradas previstas en los puntos 3.16.3.1. y 3.16.3.2., en línea con lo previsto en el primer párrafo del punto 4.8.2.

- tramo del origen: «En el caso de que un cliente haya concretado una operación de venta con obligación de recompra utilizando los bonos BOPREAL adquiridos en una suscripción primaria» (literal: exacta)
- tramo del destino: «la venta de los títulos en el origen de la operación no deberá tenerse en cuenta a los efectos de la confección de las declaraciones juradas previstas en los puntos 3.16.3.1. y 3.16.3.2.» (literal: exacta)

---

