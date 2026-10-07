# `pro::2.3.5.1` — Todo importe cobrado o adeudado de cualquier forma al usuario de servicios fi-

Grupos: grupo_c. Estado final en la tanda 0: `aceptado_con_residuales`.

## Texto

> *heredado:* Sección 2. Derechos básicos de los usuarios de servicios financieros.
> *heredado:* 2.3. Recaudos mínimos de la relación de consumo.
> *heredado:* 2.3.5. Reintegro de importes.
> *propio:* 2.3.5.1. Todo importe cobrado o adeudado de cualquier forma al usuario de servicios financieros por los siguientes conceptos: i) tasas de interés, comisiones y/o cargos sin el cumplimiento de lo previsto en los puntos 2.3.2. a 2.3.4.; ii) cargos en exceso de los costos de los servicios que terceros les cobraron a los sujetos obligados en relación con servicios prestados a los usuarios y/o de los precios que el tercero prestador perciba de particulares en general; iii) comisiones en exceso de las máximas fijadas por el BCRA que sean de aplicación; iv) en incumplimiento al nivel de la tasa de interés máxima aplicable a financiaciones vinculadas a tarjetas de crédito previstas en el texto ordenado sobre Tasas de Interés en las Operaciones de Crédito; v) en exceso de lo oportunamente pactado entre el usuario y el sujeto obligado; vi) otros generados en forma impropia por su naturaleza, tales como intereses compensatorios por saldos deudores generados en cuentas de depósito distintas de la cuenta corriente bancaria; vii) así como los importes adeudados al usuario por haber liquidado en forma incorrecta promociones, descuentos u otro tipo de beneficios –es decir, que no se ajustan a los términos, condiciones y/o modalidades que hubieran sido ofrecidos, publicitados o convenidos–; deberá serle reintegrado dentro de: - los diez (10) días hábiles siguientes al momento de la presentación del reclamo ante el sujeto obligado, de conformidad con las previsiones del punto 3.1.6.; o - los cinco (5) días hábiles siguientes al momento de constatarse tal circunstancia por el sujeto obligado o por la fiscalización que realice la SEFYC. Ello, sin perjuicio de las sanciones que pudieran corresponder. En tales situaciones, corresponderá reconocer el importe de los gastos que resulten razonables realizados para la obtención del reintegro y, en todos los casos, los intereses compensatorios pertinentes, computados desde la fecha del cobro indebido hasta la de su efectiva devolución. A ese efecto, el sujeto obligado deberá aplicar 1,5 veces la tasa promedio correspondiente al período comprendido entre el momento en que la citada diferencia hubiera sido exigible –fecha en la que se cobraron los importes objeto del reclamo– y el de su efectiva cancelación, computado a partir de la encuesta diaria de tasas de interés de depósitos a plazo fijo de 30 a 59 días –de pesos o dólares estadounidenses, según la moneda de la operación– informada por el BCRA sobre la base de la información provista por la totalidad de bancos públicos y privados. Cuando la tasa correspondiente a tal encuesta no estuviera disponible, se deberá tomar la última informada. Cuando el usuario posea en la entidad financiera obligada una cuenta a la vista que se halle abierta a su nombre, ésta deberá acreditar ese importe en dicha cuenta en forma automática sin necesidad de requerimiento expreso. Si ello no fuera posible o no se tratare de una entidad financiera, el importe del reintegro deberá ser acreditado en una tarjeta de crédito de su titularidad o detraído del saldo vigente de la financiación que lo generó. Deberá notificarse la acreditación del reintegro o, en su caso, su puesta a disposición mediante aviso efectuado a través de medios electrónicos –cajeros automáticos, banca por Internet (home banking), etc.– y/o servicios telefónicos –tales como mensajes de texto y/o voz– y: a) documento escrito dirigido a su domicilio –en forma separada de cualquier otra información que se le remita (resúmenes de cuenta, boletines informativos, etc.), aun cuando forme parte de la misma remesa–; o b) a su correo electrónico –en aquellos casos en que hubiere expresamente aceptado esa forma de notificación–. Estas disposiciones serán de aplicación a los efectos de dar cumplimiento a acuerdos extrajudiciales homologados, acuerdos homologados por acciones colectivas (artículo 54 de la Ley 24.240) o sentencias judiciales, en la medida en que no se opongan a lo previsto en esos acuerdos o a lo dispuesto por los poderes públicos de las distintas jurisdicciones. Adicionalmente, el sujeto obligado deberá verificar si este tipo de situaciones que generan la obligación de reintegros ha ocurrido respecto de los usuarios que se encuentren en la misma situación y, de corresponder, proceder a su reintegro según el procedimiento previsto en este punto, notificando de tal circunstancia y resultados a su Responsable de Atención al Usuario de Servicios Financieros.

## Supuestos de la fase A de T4 (M1)

1. «conceptos i) a vii)» (miembros i))
2. «conceptos i) a vii)» (miembros ii))
3. «conceptos i) a vii)» (miembros iii))
4. «conceptos i) a vii)» (miembros iv))
5. «conceptos i) a vii)» (miembros v))
6. «conceptos i) a vii)» (miembros vi))
7. «conceptos i) a vii)» (miembros vii))
8. «plazo por reclamo»
9. «por constatación»
10. «tasa no disponible»
11. «cuenta a la vista»
12. «si no fuera posible»

## Código A

- **op1 Operacion** «Reintegro de importes cobrados indebidamente al usuario» — Reintegro al usuario de importes cobrados o adeudados indebidamente por tasas, comisiones o cargos sin cumplir los puntos 2.3.2. a 2.3.4., cargos en exceso de costos de terceros, comisiones por encima de las máximas del BCRA, incumplimiento de la tasa máxima en tarjetas de crédito, excesos sobre lo pactado, cargos impropios por su naturaleza e importes adeudados por promociones, descuentos o benef… · props: `{"tipo": "reintegro"}` · tramo [exacta]: «Todo importe cobrado o adeudado de cualquier forma al usuario de servicios financieros por los siguientes conceptos»
- **ob1 Obligacion** «Reintegro en 10 días hábiles del reclamo o 5 de constatado» — Reintegrar al usuario el importe indebido dentro de los diez días hábiles de presentado el reclamo ante el sujeto obligado, o dentro de los cinco días hábiles de constatada la circunstancia por el sujeto obligado o por la SEFYC; sin perjuicio de las sanciones que pudieran corresponder · props: `{"tipo": "otra"}` · umbral: ['los diez (10) días hábiles siguientes al momento de la presentación del reclamo', 'los cinco (5) días hábiles siguientes al momento de constatarse tal circunstanci…'] · tramo [exacta]: «deberá serle reintegrado dentro de: - los diez (10) días hábiles siguientes al momento de la presentación del reclamo ante el sujeto obligado, de conformidad con las previsiones del punto 3.1.6.; o - los cinco (5) días hábiles siguientes al momento de constatarse tal circunstancia por el sujeto obligado o por la fiscal…»
- **ob2 Obligacion** «Reconocer gastos razonables e intereses compensatorios» — Reconocer al usuario los gastos razonables realizados para obtener el reintegro y, en todos los casos, los intereses compensatorios desde la fecha del cobro indebido hasta la efectiva devolución · props: `{"tipo": "calculo"}` · tramo [exacta]: «corresponderá reconocer el importe de los gastos que resulten razonables realizados para la obtención del reintegro y, en todos los casos, los intereses compensatorios pertinentes, computados desde la fecha del cobro indebido hasta la de su efectiva devolución»
- **ob3 Obligacion** «Intereses a 1,5 veces la tasa promedio plazo fijo» — Aplicar 1,5 veces la tasa promedio del período entre la exigibilidad de la diferencia y su efectiva cancelación, computada a partir de la encuesta diaria de tasas de depósitos a plazo fijo de 30 a 59 días (pesos o dólares según la moneda de la operación) informada por el BCRA con información de la totalidad de bancos públicos y privados · props: `{"tipo": "calculo"}` · umbral: ['1,5 veces la tasa promedio correspondiente al período comprendido entre el momen…'] · tramo [exacta]: «el sujeto obligado deberá aplicar 1,5 veces la tasa promedio correspondiente al período comprendido entre el momento en que la citada diferencia hubiera sido exigible»
- **ob4 Obligacion** «Tomar la última tasa informada si no hay encuesta» — Tomar la última tasa informada cuando la tasa de la encuesta del BCRA no estuviera disponible · props: `{"tipo": "calculo"}` · tramo [exacta]: «Cuando la tasa correspondiente a tal encuesta no estuviera disponible, se deberá tomar la última informada.»
- **c4 Condicion** «Tasa de la encuesta no disponible» — La tasa de la encuesta diaria de depósitos a plazo fijo no está disponible · tramo [exacta]: «Cuando la tasa correspondiente a tal encuesta no estuviera disponible»
- **ob5 Obligacion** «Acreditar automáticamente en cuenta a la vista» — Acreditar el importe del reintegro en forma automática, sin requerimiento expreso, en la cuenta a la vista abierta a nombre del usuario en la entidad financiera obligada · props: `{"tipo": "asignacion"}` · tramo [exacta]: «ésta deberá acreditar ese importe en dicha cuenta en forma automática sin necesidad de requerimiento expreso»
- **c5 Condicion** «Usuario con cuenta a la vista en la entidad» — El usuario posee en la entidad financiera obligada una cuenta a la vista abierta a su nombre · tramo [exacta]: «Cuando el usuario posea en la entidad financiera obligada una cuenta a la vista que se halle abierta a su nombre»
- **ob6 Obligacion** «Reintegro en tarjeta o detracción del saldo financiado» — Acreditar el reintegro en una tarjeta de crédito del usuario o detraerlo del saldo vigente de la financiación que lo generó · props: `{"tipo": "asignacion"}` · tramo [exacta]: «el importe del reintegro deberá ser acreditado en una tarjeta de crédito de su titularidad o detraído del saldo vigente de la financiación que lo generó»
- **c6 Condicion** «Acreditación en cuenta imposible o no es entidad financiera» — No es posible acreditar en cuenta a la vista o el sujeto obligado no es una entidad financiera · tramo [exacta]: «Si ello no fuera posible o no se tratare de una entidad financiera»
- **ob7 Obligacion** «Notificar acreditación del reintegro» — Notificar al usuario la acreditación del reintegro o su puesta a disposición mediante aviso por medios electrónicos y/o servicios telefónicos y, además, por documento escrito al domicilio (separado de otra información) o por correo electrónico si lo aceptó expresamente · props: `{"tipo": "comunicacion_a_cliente"}` · tramo [exacta]: «Deberá notificarse la acreditación del reintegro o, en su caso, su puesta a disposición mediante aviso efectuado a través de medios electrónicos –cajeros automáticos, banca por Internet (home banking), etc.– y/o servicios telefónicos –tales como mensajes de texto y/o voz– y:»
- **ob8 Obligacion** «Verificar casos análogos y reintegrar a otros usuarios» — Verificar si las situaciones que generan reintegros ocurrieron respecto de usuarios en la misma situación, reintegrar si corresponde según el procedimiento del punto y notificar circunstancia y resultados al Responsable de Atención al Usuario de Servicios Financieros · props: `{"tipo": "otra"}` · tramo [exacta]: «el sujeto obligado deberá verificar si este tipo de situaciones que generan la obligación de reintegros ha ocurrido respecto de los usuarios que se encuentren en la misma situación y, de corresponder, proceder a su reintegro según el procedimiento previsto en este punto, notificando de tal circunstancia y resultados a …»
- R: ob1 Obligacion —regula→ op1 Operacion
- R: ob2 Obligacion —regula→ op1 Operacion
- R: ob3 Obligacion —regula→ op1 Operacion
- R: ob5 Obligacion —regula→ op1 Operacion
- R: ob6 Obligacion —regula→ op1 Operacion
- R: ob7 Obligacion —regula→ op1 Operacion
- R: ob8 Obligacion —regula→ op1 Operacion
- R: c4 Condicion —condicion_de→ ob4 Obligacion
- R: c5 Condicion —condicion_de→ ob5 Obligacion
- R: c6 Condicion —condicion_de→ ob6 Obligacion
- R: ob1 Obligacion —aplica_a→ Sujeto_rol_sujeto_obligado_proteccion (mención «el sujeto obligado»)
- R: ob2 Obligacion —aplica_a→ Sujeto_rol_sujeto_obligado_proteccion (mención «sujeto obligado»)
- R: ob3 Obligacion —aplica_a→ Sujeto_rol_sujeto_obligado_proteccion (mención «el sujeto obligado»)
- R: ob5 Obligacion —aplica_a→ Sujeto_entidad_financiera (mención «la entidad financiera obligada»)
- R: ob6 Obligacion —aplica_a→ Sujeto_rol_sujeto_obligado_proteccion (mención «sujeto obligado»)
- R: ob7 Obligacion —aplica_a→ Sujeto_rol_sujeto_obligado_proteccion (mención «sujeto obligado»)
- R: ob8 Obligacion —aplica_a→ Sujeto_rol_sujeto_obligado_proteccion (mención «el sujeto obligado»)
- Omisión `fuera_de_tipos` [exacta]: «Ello, sin perjuicio de las sanciones que pudieran corresponder.» — Salvedad sobre consecuencias de un incumplimiento: no nombra al sujeto que las aplica; se habría usado Potestad. No altera el deber de reintegro.
- Omisión `fuera_de_tipos` [exacta]: «Estas disposiciones serán de aplicación a los efectos de dar cumplimiento a acuerdos extrajudiciales homologados, acuerdos homologados por acciones colectivas (artículo 54 de la Ley 24.240) o sentencias judiciales, en la medida en que no se opongan a lo previsto en esos acuerdos o a lo dispuesto por los poderes público…» — Cláusula de alcance/aplicación supletoria a acuerdos y sentencias; no encaja en ningún tipo sin sujeto nombrado (habría sido Condicion o alcance de la norma).

### A — supuestos a clasificar

- 1. «conceptos i) a vii)» → candidatos: op1 Operacion (1.00)
- 2. «conceptos i) a vii)» → candidatos: op1 Operacion (1.00)
- 3. «conceptos i) a vii)» → candidatos: op1 Operacion (1.00)
- 4. «conceptos i) a vii)» → candidatos: op1 Operacion (1.00)
- 5. «conceptos i) a vii)» → candidatos: op1 Operacion (1.00)
- 6. «conceptos i) a vii)» → candidatos: op1 Operacion (1.00)
- 7. «conceptos i) a vii)» → candidatos: op1 Operacion (1.00)
- 8. «plazo por reclamo» → candidatos: c4 Condicion (0.50), ob1 Obligacion (0.50), ob3 Obligacion (0.50)
- 9. «por constatación» → candidatos: —
- 10. «tasa no disponible» → candidatos: c4 Condicion (1.00), ob4 Obligacion (1.00), ob3 Obligacion (0.50), op1 Operacion (0.50)
- 11. «cuenta a la vista» → candidatos: c5 Condicion (1.00), c6 Condicion (1.00), ob5 Obligacion (1.00)
- 12. «si no fuera posible» → candidatos: c6 Condicion (1.00)

## Código H

- **op_reintegro Operacion** «Reintegro de importes cobrados indebidamente» — Reintegro al usuario de todo importe cobrado o adeudado de cualquier forma por: tasas, comisiones y/o cargos sin cumplir los puntos 2.3.2. a 2.3.4.; cargos en exceso de costos de terceros o de precios a particulares; comisiones en exceso de las máximas fijadas por el BCRA; incumplimiento de la tasa máxima en financiaciones vinculadas a tarjetas de crédito; excesos de lo pactado; otros importes gen… · props: `{"tipo": "reintegro"}` · tramo [exacta]: «Todo importe cobrado o adeudado de cualquier forma al usuario de servicios financieros por los siguientes conceptos:»
- **ob_plazo Obligacion** «Reintegro en 10 o 5 días hábiles» — El importe cobrado o adeudado indebidamente debe reintegrarse al usuario dentro de los diez días hábiles siguientes a la presentación del reclamo ante el sujeto obligado, o dentro de los cinco días hábiles siguientes a constatarse la circunstancia por el sujeto obligado o por la fiscalización de la SEFYC. · props: `{"tipo": "otra"}` · umbral: ['los diez (10) días hábiles siguientes al momento de la presentación del reclamo', 'los cinco (5) días hábiles siguientes al momento de constatarse tal circunstanci…'] · tramo [exacta]: «deberá serle reintegrado dentro de: - los diez (10) días hábiles siguientes al momento de la presentación del reclamo ante el sujeto obligado, de conformidad con las previsiones del punto 3.1.6.; o - los cinco (5) días hábiles siguientes al momento de constatarse tal circunstancia por el sujeto obligado o por la fiscal…»
- **ob_gastos Obligacion** «Reconocer gastos razonables e intereses compensatorios» — Reconocer el importe de los gastos razonables realizados para obtener el reintegro y, en todos los casos, los intereses compensatorios pertinentes computados desde la fecha del cobro indebido hasta la efectiva devolución. · props: `{"tipo": "calculo"}` · tramo [exacta]: «corresponderá reconocer el importe de los gastos que resulten razonables realizados para la obtención del reintegro y, en todos los casos, los intereses compensatorios pertinentes, computados desde la fecha del cobro indebido hasta la de su efectiva devolución»
- **ob_tasa Obligacion** «Tasa 1,5 veces promedio plazo fijo 30-59 días» — Para los intereses compensatorios, aplicar 1,5 veces la tasa promedio del período entre la exigibilidad de la diferencia y su efectiva cancelación, computada con la encuesta diaria de tasas de depósitos a plazo fijo de 30 a 59 días (pesos o dólares según la moneda de la operación) informada por el BCRA con información de la totalidad de bancos públicos y privados; si la tasa de la encuesta no estu… · props: `{"tipo": "calculo"}` · umbral: ['1,5 veces la tasa promedio'] · tramo [exacta]: «el sujeto obligado deberá aplicar 1,5 veces la tasa promedio correspondiente al período comprendido entre el momento en que la citada diferencia hubiera sido exigible»
- **ob_acred_auto Obligacion** «Acreditación automática en cuenta a la vista» — Si el usuario posee en la entidad financiera obligada una cuenta a la vista abierta a su nombre, acreditar el importe del reintegro en ella en forma automática, sin requerimiento expreso. · props: `{"tipo": "otra"}` · tramo [exacta]: «Cuando el usuario posea en la entidad financiera obligada una cuenta a la vista que se halle abierta a su nombre, ésta deberá acreditar ese importe en dicha cuenta en forma automática sin necesidad de requerimiento expreso.»
- **cond_cuenta Condicion** «Usuario con cuenta a la vista a su nombre» — El usuario posee en la entidad financiera obligada una cuenta a la vista abierta a su nombre. · tramo [exacta]: «Cuando el usuario posea en la entidad financiera obligada una cuenta a la vista que se halle abierta a su nombre»
- **ob_acred_alt Obligacion** «Acreditación en tarjeta o detracción del saldo» — Si no fuera posible la acreditación en cuenta a la vista o no se tratare de una entidad financiera, acreditar el reintegro en una tarjeta de crédito de titularidad del usuario o detraerlo del saldo vigente de la financiación que lo generó. · props: `{"tipo": "otra"}` · tramo [exacta]: «el importe del reintegro deberá ser acreditado en una tarjeta de crédito de su titularidad o detraído del saldo vigente de la financiación que lo generó»
- **cond_alt Condicion** «Acreditación en cuenta imposible o no es entidad financiera» — No es posible acreditar en cuenta a la vista, o el sujeto obligado no es una entidad financiera. · tramo [exacta]: «Si ello no fuera posible o no se tratare de una entidad financiera»
- **ob_notif Obligacion** «Notificar acreditación del reintegro» — Notificar al usuario la acreditación del reintegro o su puesta a disposición mediante aviso por medios electrónicos y/o servicios telefónicos y, además, por documento escrito dirigido a su domicilio (separado de cualquier otra información remitida, aun en la misma remesa) o por correo electrónico si hubiere aceptado expresamente esa forma de notificación. · props: `{"tipo": "comunicacion_a_cliente"}` · tramo [exacta]: «Deberá notificarse la acreditación del reintegro o, en su caso, su puesta a disposición mediante aviso efectuado a través de medios electrónicos –cajeros automáticos, banca por Internet (home banking), etc.– y/o servicios telefónicos –tales como mensajes de texto y/o voz– y:»
- **ob_verificar Obligacion** «Verificar casos análogos y reintegrar» — Verificar si las situaciones que generan la obligación de reintegro ocurrieron respecto de usuarios en la misma situación y, de corresponder, reintegrar según este procedimiento, notificando la circunstancia y resultados al Responsable de Atención al Usuario de Servicios Financieros. · props: `{"tipo": "otra"}` · tramo [exacta]: «el sujeto obligado deberá verificar si este tipo de situaciones que generan la obligación de reintegros ha ocurrido respecto de los usuarios que se encuentren en la misma situación y, de corresponder, proceder a su reintegro según el procedimiento previsto en este punto, notificando de tal circunstancia y resultados a …»
- **ob_acuerdos Definicion** «Aplicación a acuerdos homologados y sentencias» — Las disposiciones del punto se aplican para dar cumplimiento a acuerdos extrajudiciales homologados, acuerdos homologados por acciones colectivas (art. 54 Ley 24.240) o sentencias judiciales, en la medida en que no se opongan a lo previsto en ellos o a lo dispuesto por los poderes públicos. · props: `{"termino": "Alcance a acuerdos homologados y sentencias"}` · tramo [exacta]: «Estas disposiciones serán de aplicación a los efectos de dar cumplimiento a acuerdos extrajudiciales homologados, acuerdos homologados por acciones colectivas (artículo 54 de la Ley 24.240) o sentencias judiciales, en la medida en que no se opongan a lo previsto en esos acuerdos o a lo dispuesto por los poderes público…»
- **ley Comunicacion** «Ley 24.240» —  · props: `{"codigo": "Ley 24.240", "tipo": "externa"}` · tramo [exacta]: «Ley 24.240»
- R: to TextoOrdenado —referencia→ ley Comunicacion
- R: ob_plazo Obligacion —regula→ op_reintegro Operacion
- R: ob_gastos Obligacion —regula→ op_reintegro Operacion
- R: ob_tasa Obligacion —regula→ op_reintegro Operacion
- R: ob_acred_auto Obligacion —regula→ op_reintegro Operacion
- R: ob_acred_alt Obligacion —regula→ op_reintegro Operacion
- R: ob_notif Obligacion —regula→ op_reintegro Operacion
- R: ob_verificar Obligacion —regula→ op_reintegro Operacion
- R: cond_cuenta Condicion —condicion_de→ ob_acred_auto Obligacion
- R: cond_alt Condicion —condicion_de→ ob_acred_alt Obligacion
- R: ob_plazo Obligacion —aplica_a→ Sujeto_rol_sujeto_obligado_proteccion (mención «sujeto obligado»)
- R: ob_tasa Obligacion —aplica_a→ Sujeto_rol_sujeto_obligado_proteccion (mención «el sujeto obligado»)
- R: ob_acred_auto Obligacion —aplica_a→ Sujeto_entidad_financiera (mención «la entidad financiera obligada»)
- R: ob_verificar Obligacion —aplica_a→ Sujeto_rol_sujeto_obligado_proteccion (mención «el sujeto obligado»)
- Omisión `fuera_de_tipos` [exacta]: «Ello, sin perjuicio de las sanciones que pudieran corresponder.» — Salvedad sobre consecuencias del incumplimiento; no nombra a quien las aplica. Sería una Potestad/Obligacion de sanción.

### H — supuestos a clasificar

- 1. «conceptos i) a vii)» → candidatos: op_reintegro Operacion (1.00)
- 2. «conceptos i) a vii)» → candidatos: op_reintegro Operacion (1.00)
- 3. «conceptos i) a vii)» → candidatos: op_reintegro Operacion (1.00)
- 4. «conceptos i) a vii)» → candidatos: op_reintegro Operacion (1.00)
- 5. «conceptos i) a vii)» → candidatos: op_reintegro Operacion (1.00)
- 6. «conceptos i) a vii)» → candidatos: op_reintegro Operacion (1.00)
- 7. «conceptos i) a vii)» → candidatos: op_reintegro Operacion (1.00)
- 8. «plazo por reclamo» → candidatos: ob_plazo Obligacion (0.50), ob_tasa Obligacion (0.50)
- 9. «por constatación» → candidatos: —
- 10. «tasa no disponible» → candidatos: ob_tasa Obligacion (1.00), op_reintegro Operacion (0.50)
- 11. «cuenta a la vista» → candidatos: cond_alt Condicion (1.00), cond_cuenta Condicion (1.00), ob_acred_alt Obligacion (1.00), ob_acred_auto Obligacion (1.00)
- 12. «si no fuera posible» → candidatos: cond_alt Condicion (1.00), ob_acred_alt Obligacion (1.00)

## Código K

- **op1 Operacion** «Reintegro de importes cobrados indebidamente al usuario» — Reintegro al usuario de servicios financieros de importes cobrados o adeudados indebidamente · props: `{"tipo": "reintegro"}` · tramo [exacta]: «deberá serle reintegrado dentro de:»
- **o1 Obligacion** «Reintegro 10 días hábiles desde reclamo» — Reintegrar al usuario todo importe cobrado o adeudado por los conceptos i) a vii) dentro de los 10 días hábiles siguientes a la presentación del reclamo ante el sujeto obligado (conforme punto 3.1.6.); alternativa al plazo de 5 días desde constatación · props: `{"tipo": "otra"}` · umbral: ['los diez (10) días hábiles siguientes al momento de la presentación del reclamo'] · tramo [exacta]: «deberá serle reintegrado dentro de: - los diez (10) días hábiles siguientes al momento de la presentación del reclamo ante el sujeto obligado»
- **o2 Obligacion** «Reintegro 5 días hábiles desde constatación» — Reintegrar al usuario los importes indebidos dentro de los 5 días hábiles siguientes a su constatación por el sujeto obligado o por la fiscalización de la SEFyC · props: `{"tipo": "otra"}` · umbral: ['los cinco (5) días hábiles siguientes al momento de constatarse'] · tramo [exacta]: «los cinco (5) días hábiles siguientes al momento de constatarse tal circunstancia por el sujeto obligado o por la fiscalización que realice la SEFYC»
- **c1 Condicion** «Cobros sin cumplir puntos 2.3.2 a 2.3.4» — Importe cobrado por tasas, comisiones o cargos sin cumplir los puntos 2.3.2 a 2.3.4 · tramo [exacta]: «tasas de interés, comisiones y/o cargos sin el cumplimiento de lo previsto en los puntos 2.3.2. a 2.3.4.»
- **c2 Condicion** «Cargos en exceso de costos de terceros» — Cargos que exceden los costos cobrados por terceros o los precios que el tercero percibe de particulares · props: `{"umbrales": [{"tramo": "en exceso de los costos de los servicios que terceros les cobraron", "comparacion": "no_determinada", "regla_comparacion": "limite_relativo:sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['en exceso de los costos de los servicios que terceros les cobraron'] · tramo [exacta]: «cargos en exceso de los costos de los servicios que terceros les cobraron a los sujetos obligados en relación con servicios prestados a los usuarios y/o de los precios que el tercero prestador perciba de particulares en general»
- **c3 Condicion** «Comisiones en exceso de máximas BCRA» — Comisiones que exceden las máximas fijadas por el BCRA · props: `{"umbrales": [{"tramo": "en exceso de las máximas fijadas por el BCRA", "comparacion": "no_determinada", "regla_comparacion": "limite_relativo:sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['en exceso de las máximas fijadas por el BCRA'] · tramo [exacta]: «comisiones en exceso de las máximas fijadas por el BCRA que sean de aplicación»
- **c4 Condicion** «Incumplimiento de tasa máxima tarjetas de crédito» — Importes cobrados incumpliendo la tasa máxima de financiaciones con tarjeta de crédito (TO Tasas de Interés en las Operaciones de Crédito) · props: `{"umbrales": [{"tramo": "tasa de interés máxima aplicable a finan-\nciaciones vinculadas a tarjetas de crédito", "comparacion": "no_determinada", "regla_comparacion": "limite_relativo:sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['tasa de interés máxima aplicable a financiaciones vinculadas a tarjetas de crédi…'] · tramo [exacta]: «en incumplimiento al nivel de la tasa de interés máxima aplicable a financiaciones vinculadas a tarjetas de crédito»
- **c5 Condicion** «Exceso sobre lo pactado» — Importes en exceso de lo pactado entre usuario y sujeto obligado · props: `{"umbrales": [{"tramo": "en exceso de lo oportunamente pactado", "comparacion": "no_determinada", "regla_comparacion": "limite_relativo:sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['en exceso de lo oportunamente pactado'] · tramo [exacta]: «en exceso de lo oportunamente pactado entre el usuario y el sujeto obligado»
- **c6 Condicion** «Cobros impropios por su naturaleza» — Otros importes impropios por su naturaleza, p.ej. intereses compensatorios por saldos deudores en cuentas de depósito distintas de cuenta corriente · tramo [exacta]: «otros generados en forma impropia por su naturaleza»
- **c7 Condicion** «Promociones o beneficios mal liquidados» — Importes adeudados por liquidar incorrectamente promociones, descuentos o beneficios no ajustados a lo ofrecido, publicitado o convenido · tramo [exacta]: «importes adeudados al usuario por haber liquidado en forma incorrecta promociones, descuentos u otro tipo de beneficios»
- **o3 Obligacion** «Gastos razonables e intereses compensatorios — reintegro» — Reconocer gastos razonables para obtener el reintegro y siempre intereses compensatorios desde el cobro indebido hasta la devolución, aplicando 1,5 veces la tasa promedio de la encuesta diaria de plazo fijo de 30 a 59 días del BCRA (o la última informada si no está disponible) · props: `{"tipo": "calculo"}` · umbral: ['1,5 veces la tasa promedio'] · tramo [exacta]: «corresponderá reconocer el importe de los gastos que resulten razonables realizados para la obtención del reintegro y, en todos los casos, los intereses compensatorios pertinentes»
- **o4 Obligacion** «Acreditación automática en cuenta a la vista» — La entidad financiera debe acreditar automáticamente el reintegro en la cuenta a la vista del usuario · props: `{"tipo": "otra"}` · tramo [exacta]: «ésta deberá acreditar ese importe en dicha cuenta en forma automática sin necesidad de requerimiento expreso»
- **c8 Condicion** «Usuario con cuenta a la vista en la entidad» — El usuario posee cuenta a la vista a su nombre en la entidad financiera obligada · tramo [exacta]: «Cuando el usuario posea en la entidad financiera obligada una cuenta a la vista que se halle abierta a su nombre»
- **o5 Obligacion** «Acreditación en tarjeta o detracción de financiación» — Acreditar el reintegro en tarjeta de crédito del usuario o detraerlo del saldo de la financiación · props: `{"tipo": "otra"}` · tramo [exacta]: «el importe del reintegro deberá ser acreditado en una tarjeta de crédito de su titularidad o detraído del saldo vigente de la financiación que lo generó»
- **c9 Condicion** «Imposible acreditar en cuenta o no entidad financiera» — No es posible acreditar en cuenta a la vista o el obligado no es entidad financiera · tramo [exacta]: «Si ello no fuera posible o no se tratare de una entidad financiera»
- **o6 Obligacion** «Notificación del reintegro al usuario» — Notificar acreditación o puesta a disposición del reintegro por medios electrónicos y/o telefónicos y además por documento escrito separado a su domicilio o por correo electrónico si lo aceptó expresamente · props: `{"tipo": "comunicacion_a_cliente"}` · tramo [exacta]: «Deberá notificarse la acreditación del reintegro o, en su caso, su puesta a disposición mediante aviso efectuado a través de medios electrónicos»
- **o7 Obligacion** «Verificar usuarios en igual situación y reintegrar» — Verificar si otros usuarios en igual situación sufrieron cobros indebidos, reintegrarles según este punto y notificar circunstancias y resultados al Responsable de Atención al Usuario · props: `{"tipo": "otra"}` · tramo [exacta]: «el sujeto obligado deberá verificar si este tipo de situaciones que generan la obligación de reintegros ha ocurrido respecto de los usuarios que se encuentren en la misma situación»
- **c10 Condicion** «Cumplimiento de acuerdos homologados o sentencias» — Las disposiciones aplican para cumplir acuerdos extrajudiciales homologados, acuerdos por acciones colectivas (art. 54 Ley 24.240) o sentencias, en tanto no se opongan a ellos · tramo [exacta]: «en la medida en que no se opongan a lo previsto en esos acuerdos o a lo dispuesto por los poderes públicos»
- **cm1 Comunicacion** «Ley 24.240» —  · props: `{"codigo": "Ley 24.240", "tipo": "externa"}` · tramo [exacta]: «artículo 54 de la Ley 24.240»
- R: to TextoOrdenado —referencia→ cm1 Comunicacion
- R: o1 Obligacion —regula→ op1 Operacion
- R: o2 Obligacion —regula→ op1 Operacion
- R: o3 Obligacion —regula→ op1 Operacion
- R: o4 Obligacion —regula→ op1 Operacion
- R: o5 Obligacion —regula→ op1 Operacion
- R: op1 Operacion —requiere→ o6 Obligacion
- R: c1 Condicion —condicion_de→ op1 Operacion
- R: c2 Condicion —condicion_de→ op1 Operacion
- R: c3 Condicion —condicion_de→ op1 Operacion
- R: c4 Condicion —condicion_de→ op1 Operacion
- R: c5 Condicion —condicion_de→ op1 Operacion
- R: c6 Condicion —condicion_de→ op1 Operacion
- R: c7 Condicion —condicion_de→ op1 Operacion
- R: c8 Condicion —condicion_de→ o4 Obligacion
- R: c9 Condicion —condicion_de→ o5 Obligacion
- R: c10 Condicion —condicion_de→ op1 Operacion
- R: o1 Obligacion —aplica_a→ Sujeto_rol_sujeto_obligado_proteccion (mención «el sujeto obligado»)
- R: o2 Obligacion —aplica_a→ Sujeto_rol_sujeto_obligado_proteccion (mención «el sujeto obligado»)
- R: o3 Obligacion —aplica_a→ Sujeto_rol_sujeto_obligado_proteccion (mención «el sujeto obligado»)
- R: o4 Obligacion —aplica_a→ Sujeto_entidad_financiera (mención «la entidad financiera obligada»)
- R: o7 Obligacion —aplica_a→ Sujeto_rol_sujeto_obligado_proteccion (mención «el sujeto obligado»)
- Omisión `meta_normativo` [exacta]: «Ello, sin perjuicio de las sanciones que pudieran corresponder.» — Salvedad interpretativa sobre sanciones; no nombra quién las aplica

### K — supuestos a clasificar

- 1. «conceptos i) a vii)» → candidatos: o1 Obligacion (1.00)
- 2. «conceptos i) a vii)» → candidatos: o1 Obligacion (1.00)
- 3. «conceptos i) a vii)» → candidatos: o1 Obligacion (1.00)
- 4. «conceptos i) a vii)» → candidatos: o1 Obligacion (1.00)
- 5. «conceptos i) a vii)» → candidatos: o1 Obligacion (1.00)
- 6. «conceptos i) a vii)» → candidatos: o1 Obligacion (1.00)
- 7. «conceptos i) a vii)» → candidatos: o1 Obligacion (1.00)
- 8. «plazo por reclamo» → candidatos: o1 Obligacion (1.00), o3 Obligacion (0.50)
- 9. «por constatación» → candidatos: o1 Obligacion (1.00), o2 Obligacion (1.00)
- 10. «tasa no disponible» → candidatos: o3 Obligacion (1.00), c4 Condicion (0.50)
- 11. «cuenta a la vista» → candidatos: c8 Condicion (1.00), c9 Condicion (1.00), o4 Obligacion (1.00), c6 Condicion (0.50)
- 12. «si no fuera posible» → candidatos: c9 Condicion (1.00)

## Código W

- **op1 Operacion** «Reintegro de importes cobrados indebidamente al usuario» — Reintegro al usuario de servicios financieros de importes cobrados o adeudados por los conceptos enumerados en i) a vii) · props: `{"tipo": "reintegro"}` · tramo [exacta]: «deberá serle reintegrado dentro de:»
- **o1 Obligacion** «Reintegro tasas/comisiones/cargos sin cumplir 2.3.2–2.3.4» — Deber de reintegrar al usuario todo importe cobrado o adeudado por tasas de interés, comisiones y/o cargos sin cumplir los puntos 2.3.2 a 2.3.4, en los plazos de 10 días hábiles desde el reclamo o 5 días hábiles desde la constatación · props: `{"tipo": "otra"}` · umbral: ['los diez (10) días hábiles siguientes al momento de la presentación del reclamo', 'los cinco (5) días hábiles siguientes al momento de constatarse tal circunstanci…'] · tramo [exacta]: «Todo importe cobrado o adeudado de cualquier forma al usuario de servicios financieros por los siguientes conceptos: […] i) tasas de interés, comisiones y/o cargos sin el cumplimiento de lo previsto en los puntos 2.3.2. a 2.3.4.;»
- **o2 Obligacion** «Reintegro cargos en exceso de costos de terceros» — Deber de reintegrar cargos en exceso de los costos de servicios que terceros cobraron a los sujetos obligados por servicios a usuarios y/o de los precios que el tercero perciba de particulares en general, en 10 días hábiles desde el reclamo o 5 desde la constatación · props: `{"tipo": "otra"}` · umbral: ['los diez (10) días hábiles siguientes al momento de la presentación del reclamo', 'los cinco (5) días hábiles siguientes al momento de constatarse tal circunstanci…'] · tramo [exacta]: «Todo importe cobrado o adeudado de cualquier forma al usuario de servicios financieros por los siguientes conceptos: […] ii) cargos en exceso de los costos de los servicios que terceros les cobraron a los sujetos obligados»
- **o3 Obligacion** «Reintegro comisiones en exceso de máximas BCRA» — Deber de reintegrar comisiones en exceso de las máximas fijadas por el BCRA aplicables, en 10 días hábiles desde el reclamo o 5 desde la constatación · props: `{"tipo": "otra"}` · umbral: ['los diez (10) días hábiles siguientes al momento de la presentación del reclamo', 'los cinco (5) días hábiles siguientes al momento de constatarse tal circunstanci…'] · tramo [exacta]: «Todo importe cobrado o adeudado de cualquier forma al usuario de servicios financieros por los siguientes conceptos: […] iii) comisiones en exceso de las máximas fijadas por el BCRA»
- **o4 Obligacion** «Reintegro por exceder tasa máxima de tarjetas» — Deber de reintegrar importes cobrados en incumplimiento de la tasa máxima de financiaciones con tarjetas de crédito (TO Tasas de Interés en las Operaciones de Crédito), en 10 días hábiles desde el reclamo o 5 desde la constatación · props: `{"tipo": "otra"}` · umbral: ['los diez (10) días hábiles siguientes al momento de la presentación del reclamo', 'los cinco (5) días hábiles siguientes al momento de constatarse tal circunstanci…'] · tramo [exacta]: «Todo importe cobrado o adeudado de cualquier forma al usuario de servicios financieros por los siguientes conceptos: […] iv) en incumplimiento al nivel de la tasa de interés máxima aplicable a financiaciones vinculadas a tarjetas de crédito»
- **o5 Obligacion** «Reintegro por exceso sobre lo pactado» — Deber de reintegrar importes cobrados en exceso de lo pactado entre usuario y sujeto obligado, en 10 días hábiles desde el reclamo o 5 desde la constatación · props: `{"tipo": "otra"}` · umbral: ['los diez (10) días hábiles siguientes al momento de la presentación del reclamo', 'los cinco (5) días hábiles siguientes al momento de constatarse tal circunstanci…'] · tramo [exacta]: «Todo importe cobrado o adeudado de cualquier forma al usuario de servicios financieros por los siguientes conceptos: […] v) en exceso de lo oportunamente pactado entre el usuario y el sujeto obligado;»
- **o6 Obligacion** «Reintegro de conceptos impropios por su naturaleza» — Deber de reintegrar otros importes generados en forma impropia por su naturaleza, como intereses compensatorios por saldos deudores en cuentas de depósito distintas de la cuenta corriente, en 10 días hábiles desde el reclamo o 5 desde la constatación · props: `{"tipo": "otra"}` · umbral: ['los diez (10) días hábiles siguientes al momento de la presentación del reclamo', 'los cinco (5) días hábiles siguientes al momento de constatarse tal circunstanci…'] · tramo [exacta]: «Todo importe cobrado o adeudado de cualquier forma al usuario de servicios financieros por los siguientes conceptos: […] vi) otros generados en forma impropia por su naturaleza»
- **o7 Obligacion** «Reintegro por promociones o beneficios mal liquidados» — Deber de reintegrar importes adeudados por liquidar incorrectamente promociones, descuentos u otros beneficios (no ajustados a lo ofrecido, publicitado o convenido), en 10 días hábiles desde el reclamo o 5 desde la constatación · props: `{"tipo": "otra"}` · umbral: ['los diez (10) días hábiles siguientes al momento de la presentación del reclamo', 'los cinco (5) días hábiles siguientes al momento de constatarse tal circunstanci…'] · tramo [exacta]: «Todo importe cobrado o adeudado de cualquier forma al usuario de servicios financieros por los siguientes conceptos: […] vii) así como los importes adeudados al usuario por haber liquidado en forma incorrecta promociones, descuentos u otro tipo de beneficios»
- **o8 Obligacion** «Reconocimiento de gastos razonables e intereses compensatorios» — Reconocer gastos razonables para obtener el reintegro e intereses compensatorios desde el cobro indebido hasta la efectiva devolución · props: `{"tipo": "calculo"}` · tramo [exacta]: «corresponderá reconocer el importe de los gastos que resulten razonables realizados para la obtención del reintegro y, en todos los casos, los intereses compensatorios pertinentes»
- **o9 Obligacion** «Tasa 1,5 veces promedio plazo fijo 30-59 días» — Aplicar 1,5 veces la tasa promedio de la encuesta diaria de plazo fijo de 30 a 59 días (pesos o dólares según la operación) informada por el BCRA, entre la exigibilidad y la cancelación; si no está disponible, la última informada · props: `{"tipo": "calculo"}` · umbral: ['1,5 veces la tasa promedio'] · tramo [exacta]: «el sujeto obligado deberá aplicar 1,5 veces la tasa promedio»
- **o10 Obligacion** «Acreditación automática en cuenta a la vista» — La entidad financiera debe acreditar automáticamente el reintegro en la cuenta a la vista del usuario · props: `{"tipo": "otra"}` · tramo [exacta]: «ésta deberá acreditar ese importe en dicha cuenta en forma automática sin necesidad de requerimiento expreso»
- **c1 Condicion** «Usuario con cuenta a la vista en la entidad» — El usuario posee cuenta a la vista abierta a su nombre en la entidad financiera obligada · tramo [exacta]: «Cuando el usuario posea en la entidad financiera obligada una cuenta a la vista que se halle abierta a su nombre»
- **o11 Obligacion** «Acreditación alternativa en tarjeta o financiación» — Acreditar el reintegro en tarjeta de crédito del titular o detraerlo del saldo de la financiación que lo generó · props: `{"tipo": "otra"}` · tramo [exacta]: «el importe del reintegro deberá ser acreditado en una tarjeta de crédito de su titularidad o detraído del saldo vigente de la financiación que lo generó»
- **c2 Condicion** «Imposibilidad de acreditar en cuenta o no ser entidad financiera» — No es posible acreditar en cuenta a la vista o el sujeto no es entidad financiera · tramo [exacta]: «Si ello no fuera posible o no se tratare de una entidad financiera»
- **o12 Obligacion** «Notificación del reintegro por medio electrónico y documento» — Notificar la acreditación o puesta a disposición mediante medios electrónicos y/o telefónicos y, además, documento escrito separado al domicilio o correo electrónico si fue aceptado expresamente · props: `{"tipo": "comunicacion_a_cliente"}` · tramo [exacta]: «Deberá notificarse la acreditación del reintegro o, en su caso, su puesta a disposición mediante aviso efectuado a través de medios electrónicos»
- **o13 Obligacion** «Verificación de usuarios en igual situación» — Verificar si la situación ocurrió con otros usuarios en igual situación, reintegrarles según este punto y notificar circunstancias y resultados al Responsable de Atención al Usuario · props: `{"tipo": "otra"}` · tramo [exacta]: «el sujeto obligado deberá verificar si este tipo de situaciones que generan la obligación de reintegros ha ocurrido respecto de los usuarios que se encuentren en la misma situación»
- **o14 Obligacion** «Aplicación a acuerdos homologados y sentencias» — El procedimiento de reintegro aplica para cumplir acuerdos extrajudiciales u homologados por acciones colectivas (art. 54 Ley 24.240) o sentencias, en la medida que no se opongan a ellos · props: `{"tipo": "otra"}` · tramo [exacta]: «Estas disposiciones serán de aplicación a los efectos de dar cumplimiento a acuerdos extrajudiciales homologados»
- **cm1 Comunicacion** «Ley 24.240» —  · props: `{"codigo": "Ley 24.240", "tipo": "externa"}` · tramo [exacta]: «artículo 54 de la Ley 24.240»
- R: to TextoOrdenado —referencia→ cm1 Comunicacion
- R: o1 Obligacion —regula→ op1 Operacion
- R: o2 Obligacion —regula→ op1 Operacion
- R: o3 Obligacion —regula→ op1 Operacion
- R: o4 Obligacion —regula→ op1 Operacion
- R: o5 Obligacion —regula→ op1 Operacion
- R: o6 Obligacion —regula→ op1 Operacion
- R: o7 Obligacion —regula→ op1 Operacion
- R: o8 Obligacion —regula→ op1 Operacion
- R: o9 Obligacion —regula→ op1 Operacion
- R: o10 Obligacion —regula→ op1 Operacion
- R: o11 Obligacion —regula→ op1 Operacion
- R: op1 Operacion —requiere→ o12 Obligacion
- R: c1 Condicion —condicion_de→ o10 Obligacion
- R: c2 Condicion —condicion_de→ o11 Obligacion
- R: o9 Obligacion —aplica_a→ Sujeto_rol_sujeto_obligado_proteccion (mención «el sujeto obligado»)
- R: o10 Obligacion —aplica_a→ Sujeto_entidad_financiera (mención «la entidad financiera obligada»)
- R: o13 Obligacion —aplica_a→ Sujeto_rol_sujeto_obligado_proteccion (mención «el sujeto obligado»)
- Omisión `fuera_de_tipos` [exacta]: «Ello, sin perjuicio de las sanciones que pudieran corresponder.» — Consecuencia de un incumplimiento (sanciones) sin quien la aplica nombrado

### W — supuestos a clasificar

- 1. «conceptos i) a vii)» → candidatos: o1 Obligacion (1.00), o2 Obligacion (1.00), o3 Obligacion (1.00), o4 Obligacion (1.00)
- 2. «conceptos i) a vii)» → candidatos: o1 Obligacion (1.00), o2 Obligacion (1.00), o3 Obligacion (1.00), o4 Obligacion (1.00)
- 3. «conceptos i) a vii)» → candidatos: o1 Obligacion (1.00), o2 Obligacion (1.00), o3 Obligacion (1.00), o4 Obligacion (1.00)
- 4. «conceptos i) a vii)» → candidatos: o1 Obligacion (1.00), o2 Obligacion (1.00), o3 Obligacion (1.00), o4 Obligacion (1.00)
- 5. «conceptos i) a vii)» → candidatos: o1 Obligacion (1.00), o2 Obligacion (1.00), o3 Obligacion (1.00), o4 Obligacion (1.00)
- 6. «conceptos i) a vii)» → candidatos: o1 Obligacion (1.00), o2 Obligacion (1.00), o3 Obligacion (1.00), o4 Obligacion (1.00)
- 7. «conceptos i) a vii)» → candidatos: o1 Obligacion (1.00), o2 Obligacion (1.00), o3 Obligacion (1.00), o4 Obligacion (1.00)
- 8. «plazo por reclamo» → candidatos: o1 Obligacion (0.50), o2 Obligacion (0.50), o3 Obligacion (0.50), o4 Obligacion (0.50)
- 9. «por constatación» → candidatos: o1 Obligacion (1.00), o2 Obligacion (1.00), o3 Obligacion (1.00), o4 Obligacion (1.00)
- 10. «tasa no disponible» → candidatos: o9 Obligacion (1.00), o4 Obligacion (0.50)
- 11. «cuenta a la vista» → candidatos: c1 Condicion (1.00), c2 Condicion (1.00), o10 Obligacion (1.00), o6 Obligacion (0.50)
- 12. «si no fuera posible» → candidatos: c2 Condicion (1.00)

