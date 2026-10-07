# Fichas de C2 — código N

Lectura cegada (primera lectura de la instancia). El código no dice el brazo ni la corrida; la tabla sigue cerrada hasta la adjudicación. Clases de M1 y M2: `c0/reglas_lectura_c0.md`.

## `cla::6.5.4.5` — Cuente con refinanciaciones del capital adeudado y de los intereses devengados

Grupos: grupo_c.

### Texto

> *heredado:* Sección 6. Clasificación de los deudores de la cartera comercial.
> *heredado:* 6.5. Niveles de clasificación.
> *heredado:* Cada cliente, y la totalidad de sus financiaciones comprendidas, se incluirá en una de las siguientes cinco categorías, las que se definen teniendo en cuenta las condiciones que se detallan en cada caso. Los clientes que no registren asistencia crediticia de la entidad y que posteriormente reciban financiaciones de ésta que no superen el importe resultante de aplicar sobre el saldo de deuda registrado en el sistema financiero, según la última información disponible en la "Central de deudores" a la fecha de su otorgamiento, el porcentaje establecido en el punto 2.2.5. de las normas sobre "Previsiones mínimas por riesgo de incobrabilidad" correspondiente a la peor clasificación asignada, podrán ser clasificados por la entidad teniendo en cuenta únicamente el análisis del flujo de fondos proyectado. Las asistencias así otorgadas no serán consideradas a los fines a que se refiere el punto 6.6. A fin de verificar el cumplimiento de las obligaciones sin recurrir a nueva financiación directa o indirecta o a refinanciaciones, no se considerarán refinanciaciones las facilidades adicionales que se otorguen respecto de los márgenes vigentes acordados, siempre que el nuevo apoyo crediticio implique nuevos desembolsos de fondos y no supere el 10 % del cupo asignado en oportunidad de la última evaluación crediticia del cliente, en la medida en que éstas sean consistentes con el curso normal de los negocios y exista capacidad para atender el resto de las obligaciones financieras, ni las nuevas financiaciones y las refinanciaciones asociadas a una mayor inversión derivada de la expansión de las actividades, y siempre que pueda demostrarse que el flujo de fondos proyectado permitirá afrontar la totalidad de sus obligaciones. Tampoco se considerarán dentro de ese concepto las refinanciaciones otorgadas a los productores agropecuarios cuando ello resulte de la aplicación de disposiciones vinculadas a la Ley de Emergencia Agropecuaria, sin perjuicio de lo cual, a los fines de la clasificación, deberá tenerse en cuenta el flujo de fondos proyectado para el momento en que concluya la vigencia de la emergencia declarada. El tratamiento que se dispense en ese marco no podrá implicar mejoramiento de la clasificación asignada al cliente en función de su situación individual, preexistente a la emergencia, ni su aplicación extenderse más allá de la vigencia fijada para ella.
> *heredado:* 6.5.4. Con alto riesgo de insolvencia.
> *heredado:* El análisis del flujo de fondos del cliente demuestra que es altamente improbable que pueda atender la totalidad de sus compromisos financieros. Entre los indicadores que pueden reflejar esta situación se destacan que el cliente:
> *propio:* 6.5.4.5. Cuente con refinanciaciones del capital adeudado y de los intereses devengados vinculadas a una insuficiente capacidad para su pago, con otorgamiento de quitas o con reducción en las tasas de interés pactadas –salvo que ello derive de las condiciones del mercado– o cuando haya sido necesario recibir bienes en pago de parte de las obligaciones. No obstante, el deudor cuyas deudas hayan sido refinanciadas con otorgamiento de quitas de capital podrá ser recategorizado directamente en niveles superiores ("con problemas", "en observación") por la aplicación de la metodología establecida en el punto 2.2.6. de las normas sobre "Previsiones mínimas por riesgo de incobrabilidad", siempre que además se observen las otras condiciones previstas en las correspondientes categorías. Cuando al menos se haya cumplido con el pago, sin haber incurrido en atrasos superiores a los 31 días del 10 % de las obligaciones refinanciadas y la totalidad de los intereses devengados, con más el porcentaje acumulado que pudiera corresponder si la refinanciación se hubiera otorgado de haberse encontrado el deudor en la categoría inferior, podrá reclasificárselo en el nivel inmediato superior si, además, se observan las otras condiciones previstas en el citado nivel. El deudor que, encontrándose clasificado en esta categoría, haya refinanciado su deuda –aun cuando haya cancelado el porcentaje establecido en el párrafo precedente– y recibido crédito adicional en los términos a que se refiere el punto 2.2.5. de las normas sobre "Previsiones mínimas por riesgo de incobrabilidad", y en la medida en que dicha financiación adicional no hubiese sido cancelada, deberá permanecer en esta categoría por lo menos 180 días contados desde la fecha en que se otorgó crédito adicional o desde que se celebró el acuerdo de refinanciación, la circunstancia más reciente. Ello, salvo que por aplicación de otras pautas corresponda categorizarlo en el nivel inferior.

### Extracción (código N)

- **e1 Operacion** «Refinanciación de capital e intereses» — Refinanciación del capital adeudado y de los intereses devengados vinculadas a una insuficiente capacidad para su pago, con otorgamiento de quitas o con reducción en las tasas de interés pactadas, o cuando haya sido necesario recibir bienes en pago de parte de las obligaciones. · props: `{"tipo": "refinanciación"}` · tramo [exacta]: «Cuente con refinanciaciones del capital adeudado y de los intereses devengados»
- **e2 Restriccion** «Indicador de alto riesgo — refinanciaciones con quitas o reducción de tasas» — Indicador de clasificación en categoría de alto riesgo de insolvencia: refinanciaciones con otorgamiento de quitas o reducción de tasas (salvo por condiciones de mercado) o recepción de bienes en pago de obligaciones. · props: `{"tipo": "limite_cualitativo"}` · tramo [exacta]: «Cuente con refinanciaciones del capital adeudado y de los intereses devengados vinculadas a una insuficiente capacidad para su pago, con otorgamiento de quitas o con reducción en las tasas de interés pactadas –salvo que ello derive de las condiciones del mercado– o cuando haya sido necesario recibir bienes en pago de p…»
- **e3 Excepcion** «Excepción — reducción de tasas por condiciones de mercado» — No se considera indicador de alto riesgo la reducción en las tasas de interés pactadas cuando derive de las condiciones del mercado. · tramo [exacta]: «salvo que ello derive de las condiciones del mercado»
- **e4 Potestad** «Recategorización directa a niveles superiores — aplicación de metodología» — Facultad de recategorizar directamente en niveles superiores (con problemas, en observación) al deudor cuyas deudas hayan sido refinanciadas con otorgamiento de quitas de capital, por aplicación de la metodología del punto 2.2.6 de normas sobre previsiones mínimas. · tramo [exacta]: «el deudor cuyas deudas hayan sido refinanciadas con otorgamiento de quitas de capital podrá ser recategorizado directamente en niveles superiores ("con problemas", "en observación") por la aplicación de la metodología establecida en el punto 2.2.6. de las normas sobre "Previsiones mínimas por riesgo de incobrabilidad"»
- **e5 Condicion** «Condición para recategorización — observancia de otras condiciones» — La recategorización requiere que además se observen las otras condiciones previstas en las correspondientes categorías. · tramo [exacta]: «siempre que además se observen las otras condiciones previstas en las correspondientes categorías»
- **e6 Obligacion** «Reclasificación a nivel inmediato superior — pago del 10 % sin atrasos» — Facultad de reclasificar al deudor en el nivel inmediato superior cuando haya pagado sin atrasos superiores a 31 días el 10 % de las obligaciones refinanciadas y la totalidad de los intereses devengados, más el porcentaje acumulado que correspondería si la refinanciación se hubiera otorgado en categoría inferior. · props: `{"tipo": "otra"}` · umbral: ['sin haber incurrido en atrasos superiores a los 31 días', 'del 10 % de las obligaciones refinanciadas'] · tramo [exacta]: «Cuando al menos se haya cumplido con el pago, sin haber incurrido en atrasos superiores a los 31 días del 10 % de las obligaciones refinanciadas y la totalidad de los intereses devengados, con más el porcentaje acumulado que pudiera corresponder si la refinanciación se hubiera otorgado de haberse encontrado el deudor e…»
- **e7 Condicion** «Condición para reclasificación — observancia de otras condiciones del nivel» — La reclasificación al nivel inmediato superior requiere que además se observen las otras condiciones previstas en ese nivel. · tramo [exacta]: «si, además, se observan las otras condiciones previstas en el citado nivel»
- **e8 Restriccion** «Permanencia mínima en categoría — 180 días tras crédito adicional» — Obligación de permanecer en la categoría de alto riesgo por lo menos 180 días contados desde la fecha más reciente entre el otorgamiento de crédito adicional o la celebración del acuerdo de refinanciación, cuando el deudor haya refinanciado su deuda y recibido crédito adicional que no haya sido cancelado. · props: `{"tipo": "limite_cuantitativo"}` · umbral: ['por lo menos 180 días'] · tramo [exacta]: «El deudor que, encontrándose clasificado en esta categoría, haya refinanciado su deuda –aun cuando haya cancelado el porcentaje establecido en el párrafo precedente– y recibido crédito adicional en los términos a que se refiere el punto 2.2.5. de las normas sobre "Previsiones mínimas por riesgo de incobrabilidad", y en…»
- **e9 Excepcion** «Excepción a permanencia mínima — categorización en nivel inferior» — No aplica la permanencia mínima de 180 días si por aplicación de otras pautas corresponde categorizar al deudor en el nivel inferior. · tramo [exacta]: «Ello, salvo que por aplicación de otras pautas corresponda categorizarlo en el nivel inferior»
- R: e3 Excepcion —exceptua→ e2 Restriccion
- R: e5 Condicion —condicion_de→ e4 Potestad
- R: e7 Condicion —condicion_de→ e6 Obligacion
- R: e9 Excepcion —exceptua→ e8 Restriccion
- Omisión `relacion_sin_predicado` [exacta]: «el deudor cuyas deudas hayan sido refinanciadas con otorgamiento de quitas de capital podrá ser recategorizado directamente en niveles superiores» — Relación entre Potestad (e4) y Operacion (e1): la potestad de recategorizar se habilita cuando se ha realizado la operación de refinanciación con quitas. Predicado sugerido: 'condicion_de' (la operaci…

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «bienes en pago» | `dentro_de_norma` |  | dentro de la Restriccion e2 (el indicador) y de la Operacion e1; sin Condicion |
| 2 | «recategorización siempre que…» | `condicion_con_relacion` |  | e5 Condicion —condicion_de→ e4 Potestad |
| 3 | «pago del 10 %» | `dentro_de_norma` |  | dentro de la Obligacion e6 (umbrales del 10 % y de 31 días); sin Condicion |
| 4 | «financiación adicional sin cancelar» | `dentro_de_norma` |  | dentro de la Restriccion e8 (tramo); sin Condicion |
| 5 | «salvo otras pautas» | `condicion_con_relacion` |  | e9 Excepcion —exceptua→ e8 Restriccion |

## `cla::6.5.5.2` — Incurra en atrasos superiores a un año, cuente con refinanciación del capital y

Grupos: grupo_c.

### Texto

> *heredado:* Sección 6. Clasificación de los deudores de la cartera comercial.
> *heredado:* 6.5. Niveles de clasificación.
> *heredado:* Cada cliente, y la totalidad de sus financiaciones comprendidas, se incluirá en una de las siguientes cinco categorías, las que se definen teniendo en cuenta las condiciones que se detallan en cada caso. Los clientes que no registren asistencia crediticia de la entidad y que posteriormente reciban financiaciones de ésta que no superen el importe resultante de aplicar sobre el saldo de deuda registrado en el sistema financiero, según la última información disponible en la "Central de deudores" a la fecha de su otorgamiento, el porcentaje establecido en el punto 2.2.5. de las normas sobre "Previsiones mínimas por riesgo de incobrabilidad" correspondiente a la peor clasificación asignada, podrán ser clasificados por la entidad teniendo en cuenta únicamente el análisis del flujo de fondos proyectado. Las asistencias así otorgadas no serán consideradas a los fines a que se refiere el punto 6.6. A fin de verificar el cumplimiento de las obligaciones sin recurrir a nueva financiación directa o indirecta o a refinanciaciones, no se considerarán refinanciaciones las facilidades adicionales que se otorguen respecto de los márgenes vigentes acordados, siempre que el nuevo apoyo crediticio implique nuevos desembolsos de fondos y no supere el 10 % del cupo asignado en oportunidad de la última evaluación crediticia del cliente, en la medida en que éstas sean consistentes con el curso normal de los negocios y exista capacidad para atender el resto de las obligaciones financieras, ni las nuevas financiaciones y las refinanciaciones asociadas a una mayor inversión derivada de la expansión de las actividades, y siempre que pueda demostrarse que el flujo de fondos proyectado permitirá afrontar la totalidad de sus obligaciones. Tampoco se considerarán dentro de ese concepto las refinanciaciones otorgadas a los productores agropecuarios cuando ello resulte de la aplicación de disposiciones vinculadas a la Ley de Emergencia Agropecuaria, sin perjuicio de lo cual, a los fines de la clasificación, deberá tenerse en cuenta el flujo de fondos proyectado para el momento en que concluya la vigencia de la emergencia declarada. El tratamiento que se dispense en ese marco no podrá implicar mejoramiento de la clasificación asignada al cliente en función de su situación individual, preexistente a la emergencia, ni su aplicación extenderse más allá de la vigencia fijada para ella.
> *heredado:* 6.5.5. Irrecuperable.
> *heredado:* Las deudas de clientes incorporados a esta categoría se consideran incobrables. Si bien estos activos podrían tener algún valor de recuperación bajo un cierto conjunto de circunstancias futuras, su incobrabilidad es evidente al momento del análisis. Entre los indicadores que pueden reflejar esta situación se destacan que el cliente:
> *heredado:* Además, corresponderá clasificar en esta categoría a los clientes que, cualquiera sea el motivo (entre ellos por no contar con legajo o por no haber proporcionado información confiable y/o actualizada), no hayan sido evaluados con la periodicidad correspondiente, con excepción de los deudores en concurso o con acuerdo preventivo extrajudicial solicitado o en gestión judicial que, por un período de hasta 540 días contados a partir de la apertura del concurso, solicitud del acuerdo preventivo o inicio de las gestiones judiciales de cobro, según corresponda, no hubiesen presentado la documentación que permita realizarla, siempre que se cuente con informe de abogado de la entidad financiera acreedora sobre la razonabilidad del recupero de los créditos comprendidos. Ello, sin perjuicio de que se trate de deudas que reúnan todas las condiciones previstas por el punto 2.2.3.2. de las normas sobre "Previsiones mínimas por riesgo de incobrabilidad".
> *propio:* 6.5.5.2. Incurra en atrasos superiores a un año, cuente con refinanciación del capital y sus intereses y con financiación de pérdidas de explotación. A este fin, el cómputo de los plazos no se interrumpirá por el otorgamiento de renovaciones cuando previamente no se haya producido la cancelación efectiva de las obligaciones vencidas, es decir sin recurrir a financiación directa o indirecta de la entidad. Cuando al menos se haya cumplido con el pago, sin haber incurrido en atrasos superiores a los 31 días del 15 % de las obligaciones refinanciadas y la totalidad de los intereses devengados, podrá reclasificarse al deudor en el nivel inmediato superior si, además, se observan las otras condiciones previstas en el citado nivel. El deudor que, encontrándose clasificado en esta categoría, haya refinanciado su deuda –aun cuando haya cancelado el porcentaje establecido en el párrafo precedente– y recibido crédito adicional en los términos a que se refiere el punto 2.2.5. de las normas sobre "Previsiones mínimas por riesgo de incobrabilidad", y en la medida en que dicha financiación adicional no hubiese sido cancelada, deberá permanecer en esta categoría por lo menos 180 días contados desde la fecha en que se otorgó crédito adicional o desde que se celebró el acuerdo de refinanciación, la circunstancia más reciente.

### Extracción (código N)

- **e1 Operacion** «Incurrir en atrasos superiores a un año» — El cliente incurre en atrasos superiores a un año en el pago de sus obligaciones · props: `{"tipo": "incumplimiento de obligación"}` · tramo [exacta]: «Incurra en atrasos superiores a un año»
- **e2 Operacion** «Refinanciación del capital e intereses» — El cliente cuenta con refinanciación del capital y sus intereses · props: `{"tipo": "refinanciación"}` · tramo [exacta]: «cuente con refinanciación del capital y sus intereses»
- **e3 Operacion** «Financiación de pérdidas de explotación» — El cliente cuenta con financiación de pérdidas de explotación · props: `{"tipo": "financiación"}` · tramo [exacta]: «financiación de pérdidas de explotación»
- **e4 Condicion** «Cómputo de plazos sin interrupción por renovaciones» — El cómputo de los plazos de atraso no se interrumpe por renovaciones si no ha habido cancelación efectiva de obligaciones vencidas sin financiación directa o indirecta · tramo [exacta]: «el cómputo de los plazos no se interrumpirá por el otorgamiento de renovaciones cuando previamente no se haya producido la cancelación efectiva de las obligaciones vencidas»
- **e5 Excepcion** «Reclasificación por pago del 15% de obligaciones refinanciadas» — Excepción a la clasificación en categoría Irrecuperable: el deudor puede reclasificarse al nivel superior si ha pagado sin atrasos mayores a 31 días el 15% de obligaciones refinanciadas y la totalidad de intereses · umbral: ['atrasos superiores a los 31 días', '15 % de las obligaciones refinanciadas'] · tramo [exacta]: «Cuando al menos se haya cumplido con el pago, sin haber incurrido en atrasos superiores a los 31 días del 15 % de las obligaciones refinanciadas y la totalidad de los intereses devengados, podrá reclasificarse al deudor en el nivel inmediato superior»
- **e6 Condicion** «Observancia de otras condiciones del nivel superior» — Para la reclasificación, además del pago del 15%, deben observarse las otras condiciones previstas en el nivel inmediato superior · tramo [exacta]: «si, además, se observan las otras condiciones previstas en el citado nivel»
- **e7 Restriccion** «Permanencia mínima 180 días con crédito adicional» — El deudor que ha refinanciado su deuda y recibido crédito adicional debe permanecer en la categoría Irrecuperable por lo menos 180 días desde la fecha más reciente entre otorgamiento de crédito adicional o celebración del acuerdo de refinanciación · props: `{"tipo": "limite_cuantitativo"}` · umbral: ['por lo menos 180 días'] · tramo [exacta]: «deberá permanecer en esta categoría por lo menos 180 días contados desde la fecha en que se otorgó crédito adicional o desde que se celebró el acuerdo de refinanciación, la circunstancia más reciente»
- **e8 Condicion** «Crédito adicional no cancelado» — La restricción de permanencia aplica en la medida en que el crédito adicional no haya sido cancelado · tramo [exacta]: «en la medida en que dicha financiación adicional no hubiese sido cancelada»
- R: e4 Condicion —condicion_de→ e1 Operacion
- R: e6 Condicion —condicion_de→ e5 Excepcion
- R: e8 Condicion —condicion_de→ e7 Restriccion
- Omisión `meta_normativo` [exacta]: «A este fin, el cómputo de los plazos no se interrumpirá por el otorgamiento de renovaciones cuando previamente no se haya producido la cancelación efectiva de las obligaciones vencidas, es decir sin recurrir a financiación directa o indirecta de la entidad» — Aclaración interpretativa sobre cómo se computa el plazo de atraso; el contenido normativo (la condición sobre la no interrupción) se extrajo como Condicion e4

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «sin cancelación efectiva previa» | `fusionado` |  | e4 Condicion junta la norma (el cómputo no se interrumpe por renovaciones) con el supuesto (sin cancelación efectiva previa) en un solo tramo; e4 —condicion_de→ e1 Operacion |
| 2 | «pago del 15 %» | `dentro_de_norma` |  | umbral dentro de la Excepcion e5 («Reclasificación por pago del 15 %», la norma de reclasificación extraída como Excepcion); sin Condicion propia |
| 3 | «financiación adicional sin cancelar» | `condicion_con_relacion` |  | e8 Condicion «Crédito adicional no cancelado» —condicion_de→ e7 Restriccion |

## `ctacte::5.1.2.2` — A favor de fiduciarios de fideicomisos financieros comprendidos en la Ley de En-

Grupos: omisiones.

### Texto

> *heredado:* Sección 5. Endosos, modalidades especiales de emisión y aval.
> *heredado:* 5.1. Endoso.
> *heredado:* 5.1.2. El cheque extendido a favor de una persona determinada, que no posea la cláusula "no a
> *heredado:* la orden", será transmisible por endoso. También podrán ser transmitidos por endoso los cheques con la citada condición ("no a la orden"), en los casos de transferencias –primeras y sucesivas– cuando se extienda:
> *heredado:* En los casos de cheques librados al portador o a favor de una persona determinada –que posean o no la cláusula "no a la orden"– y que sean entregados por su beneficiario a un tercero para la gestión de cobro mediante su presentación en ventanilla o a través de su depósito en cuenta para su compensación electrónica, se deberá consignar al dorso la firma y aclaración –o en el correspondiente registro electrónico, la identificación– del mandante u ordenante de la gestión y su número de identificación personal –según las normas sobre "Documentos de identificación en vigencia"– en los casos de personas físicas, o CUIT o CDI en los casos de personas jurídicas, independientemente de la existencia o no del documento que instrumenta el mandato. Adicionalmente, se insertará alguna de las siguientes expresiones: "en procuración", "valor al cobro" o "para su gestión de cobro", como manifestación de los efectos de ese endoso. La obligación de consignar el número de identificación personal o CUIT o CDI, según corresponda y la leyenda mencionada anteriormente recae, indistintamente, en el mandante u ordenante y el mandatario o gestor.
> *propio:* 5.1.2.2. A favor de fiduciarios de fideicomisos financieros comprendidos en la Ley de Entidades Financieras, en la medida en que se trate de operaciones relativas al fideicomiso.

### Extracción (código N)

- **c1 Condicion** «Supuesto fiduciario fideicomiso financiero LEF» — Supuesto en que el cheque se extiende a favor de un fiduciario de fideicomiso financiero regulado por la Ley de Entidades Financieras, y la operación es relativa al fideicomiso. · tramo [exacta]: «A favor de fiduciarios de fideicomisos financieros comprendidos en la Ley de Entidades Financieras, en la medida en que se trate de operaciones relativas al fideicomiso»
- **op1 Operacion** «Transmisión por endoso — cheque a favor de fiduciario» — Transmisión de un cheque por endoso cuando se extiende a favor de un fiduciario de fideicomiso financiero comprendido en la Ley de Entidades Financieras, en operaciones relativas al fideicomiso. · props: `{"tipo": "Transmisión de cheque por endoso"}` · tramo [exacta]: «el cheque extendido a favor de una persona determinada, que no posea la cláusula 'no a la orden', será transmisible por endoso»
- R: c1 Condicion —condicion_de→ op1 Operacion
- Omisión `relacion_sin_predicado` [exacta]: «A favor de fiduciarios de fideicomisos financieros comprendidos en la Ley de Entidades Financieras» — Relación de alcance/sujeto: la operación se dirige a un sujeto específico (fiduciario de fideicomiso financiero), pero el catálogo de sujetos no proporciona un id directo para 'fiduciario de fideicomi…

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| con_marca:28 | sí | «comprendidos en la Ley de Entidades Financieras» | `extraida_tramo_verificado` |  | c1 Condicion [exacta], tramo que contiene el fragmento (además om#0 relacion_sin_predicado sobre el mismo tramo) |

## `ext::10.3.6` — Pagos de importaciones con cartas de crédito o letras avaladas emitidas u otorgadas

Grupos: grupo_c.

### Texto

> *heredado:* Sección 10. Pagos de importaciones y otras compras de bienes en el exterior.
> *heredado:* 10.3. Pagos de importaciones de bienes que cuentan con registro de ingreso aduanero.
> *propio:* 10.3.6. Pagos de importaciones con cartas de crédito o letras avaladas emitidas u otorgadas por entidades financieras locales. La entidad tendrá acceso al mercado de cambios para cancelar cartas de crédito o letras avaladas emitidas u otorgadas para garantizar operaciones de importaciones de bienes que tengan el registro aduanero de los bienes, incluso cuando no se cumplan los requisitos establecidos para el acceso del cliente, en la medida que cuente con la documentación que demuestre que, al momento de la apertura o emisión por parte de la entidad, se cumplían las condiciones que resultaban aplicables según la fecha en que se emitió u otorgó la carta de crédito o letra avalada y el tipo de operación garantizada por la entidad. En el caso de cartas de crédito o letras avaladas emitidas u otorgadas a partir del 13/12/23, la entidad deberá contar con la documentación que demuestre que, al momento de la apertura o emisión, la operación garantizada correspondía a una importación de bienes con registro de ingreso aduanero a partir de dicha fecha y, salvo que la operación quedase comprendida en la situación prevista en el punto 10.10.2.11., que el pago garantizado debía ser concretado por el cliente a partir de la fecha que resultaba de adicionar el plazo en días corridos que le correspondía al bien por el punto 10.10.1. más otros 15 (quince) días corridos a la fecha estimada de arribo de los bienes al país. Para aquellas emitidas u otorgadas a partir del 14/04/25, en la medida que se cumplan las restantes condiciones, también se admitirá que el pago garantizado tuviera que ser concretado a partir de la fecha estimada de embarque de los bienes en origen más un plazo adicional de 15 (quince) días corridos cuando correspondía a la porción de una operación por la cual el cliente hubiese podido realizar pagos a la vista en virtud de lo previsto en los puntos 10.10.2.1. o 10.10.2.2. Las condiciones aplicables para las cartas de crédito o letras avaladas emitidas u otorgadas hasta el 12/12/23 fueron oportunamente receptadas en el punto 10.3.6. del Anexo de la Comunicación A 7914. El boleto de venta deberá efectuarse a nombre de la propia entidad en calidad de cliente por el concepto "B14. Cancelación de garantías comerciales de entidades financieras por importaciones de bienes con registro de ingreso aduanero".

### Extracción (código N)

- **e1 Operacion** «Cancelación de cartas de crédito o letras avaladas» — Cancelación de cartas de crédito o letras avaladas emitidas u otorgadas para garantizar operaciones de importaciones de bienes con registro aduanero · props: `{"tipo": "Acceso al mercado de cambios para cancelación de garantías comerciales"}` · tramo [exacta]: «La entidad tendrá acceso al mercado de cambios para cancelar cartas de crédito o letras avaladas emitidas u otorgadas para garantizar operaciones de importaciones de bienes que tengan el registro aduanero de los bienes»
- **e2 Condicion** «Documentación de cumplimiento de condiciones al momento de emisión» — La entidad debe contar con documentación que demuestre que al momento de la apertura o emisión se cumplían las condiciones aplicables según la fecha de emisión y el tipo de operación · tramo [exacta]: «en la medida que cuente con la documentación que demuestre que, al momento de la apertura o emisión por parte de la entidad, se cumplían las condiciones que resultaban aplicables según la fecha en que se emitió u otorgó la carta de crédito o letra avalada y el tipo de operación garantizada por la entidad»
- **e3 Condicion** «Cartas de crédito o letras avaladas emitidas a partir del 13/12/23» — Aplica a cartas de crédito o letras avaladas emitidas u otorgadas a partir del 13 de diciembre de 2023 · props: `{"umbrales": [{"tramo": "a partir del 13/12/23", "comparacion": "no_determinada", "regla_comparacion": "limite_relativo:sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['a partir del 13/12/23'] · tramo [exacta]: «En el caso de cartas de crédito o letras avaladas emitidas u otorgadas a partir del 13/12/23»
- **e4 Obligacion** «Documentación de importación con registro aduanero a partir del 13/12/23» — La entidad deberá contar con documentación que demuestre que la operación garantizada correspondía a una importación de bienes con registro de ingreso aduanero a partir del 13/12/23 · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «la entidad deberá contar con la documentación que demuestre que, al momento de la apertura o emisión, la operación garantizada correspondía a una importación de bienes con registro de ingreso aduanero a partir de dicha fecha»
- **e5 Condicion** «Operación no comprendida en punto 10.10.2.11» — Salvo que la operación quedase comprendida en la situación prevista en el punto 10.10.2.11 · tramo [exacta]: «salvo que la operación quedase comprendida en la situación prevista en el punto 10.10.2.11.»
- **e6 Obligacion** «Pago garantizado según plazo de bien más 15 días» — El pago garantizado debía ser concretado por el cliente a partir de la fecha que resultaba de adicionar el plazo en días corridos que le correspondía al bien por el punto 10.10.1 más otros 15 días corridos a la fecha estimada de arribo de los bienes al país · props: `{"tipo": "otra"}` · umbral: ['más otros 15 (quince) días corridos'] · tramo [exacta]: «que el pago garantizado debía ser concretado por el cliente a partir de la fecha que resultaba de adicionar el plazo en días corridos que le correspondía al bien por el punto 10.10.1. más otros 15 (quince) días corridos a la fecha estimada de arribo de los bienes al país»
- **e7 Condicion** «Cartas de crédito o letras avaladas emitidas a partir del 14/04/25» — Aplica a cartas de crédito o letras avaladas emitidas u otorgadas a partir del 14 de abril de 2025 · props: `{"umbrales": [{"tramo": "a partir del 14/04/25", "comparacion": "no_determinada", "regla_comparacion": "limite_relativo:sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['a partir del 14/04/25'] · tramo [exacta]: «Para aquellas emitidas u otorgadas a partir del 14/04/25»
- **e8 Excepcion** «Pago desde fecha estimada de embarque más 15 días» — Se admitirá que el pago garantizado tuviera que ser concretado a partir de la fecha estimada de embarque de los bienes en origen más un plazo adicional de 15 días corridos cuando correspondía a la porción de una operación por la cual el cliente hubiese podido realizar pagos a la vista según los puntos 10.10.2.1 o 10.10.2.2 · umbral: ['más un plazo adicional de 15 (quince) días corridos'] · tramo [exacta]: «también se admitirá que el pago garantizado tuviera que ser concretado a partir de la fecha estimada de embarque de los bienes en origen más un plazo adicional de 15 (quince) días corridos cuando correspondía a la porción de una operación por la cual el cliente hubiese podido realizar pagos a la vista en virtud de lo p…»
- **e9 Comunicacion** «Com. A 7914» —  · props: `{"codigo": "A-7914", "tipo": "A", "numero": 7914}` · tramo [exacta]: «Comunicación A 7914»
- **e10 Obligacion** «Boleto de venta a nombre de la entidad» — El boleto de venta deberá efectuarse a nombre de la propia entidad en calidad de cliente por el concepto 'B14. Cancelación de garantías comerciales de entidades financieras por importaciones de bienes con registro de ingreso aduanero' · props: `{"tipo": "otra"}` · tramo [exacta]: «El boleto de venta deberá efectuarse a nombre de la propia entidad en calidad de cliente por el concepto "B14. Cancelación de garantías comerciales de entidades financieras por importaciones de bienes con registro de ingreso aduanero".»
- R: e2 Condicion —condicion_de→ e1 Operacion
- R: e3 Condicion —condicion_de→ e4 Obligacion
- R: e5 Condicion —condicion_de→ e6 Obligacion
- R: e7 Condicion —condicion_de→ e8 Excepcion
- R: to TextoOrdenado —referencia→ e9 Comunicacion
- R: e1 Operacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «La entidad»)
- R: e4 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad»)
- R: e10 Obligacion —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la propia entidad»)
- Omisión `meta_normativo` [exacta]: «Las condiciones aplicables para las cartas de crédito o letras avaladas emitidas u otorgadas hasta el 12/12/23 fueron oportunamente receptadas en el punto 10.3.6. del Anexo de la Comunicación A 7914.» — 

### M1 — supuestos de la fase A de T4

| n | supuesto | clase | subtipo | ancla |
|---|---|---|---|---|
| 1 | «emitidas desde el 13/12/23 (más 15 días)» | `condicion_con_relacion` |  | e3 Condicion con el umbral «a partir del 13/12/23» —condicion_de→ e4 Obligacion |
| 2 | «desde el 14/04/25» | `condicion_con_relacion` |  | e7 Condicion con el umbral —condicion_de→ e8 Excepcion |
| 3 | «con pagos a la vista» | `dentro_de_norma` |  | dentro de la Excepcion e8 (tramo «…cuando correspondía a la porción… pagos a la vista»); sin Condicion |

## `ext::3.9::intro` — [bloque intro] Compra de moneda extranjera por parte de personas humanas residentes para la formación

Grupos: omisiones.

### Texto

> *heredado:* Sección 3. Disposiciones específicas para los egresos por el mercado de cambios
> *heredado:* 3.9. Compra de moneda extranjera por parte de personas humanas residentes para la formación
> *propio:* de activos externos bajo otras modalidades, la remisión de ayuda familiar u operaciones con derivados. Las entidades podrán dar acceso al mercado de cambios a las personas humanas residentes para la formación de activos externos (códigos de conceptos A01, A02, A03, A04, A06, A08, A14 y A24), la remisión de ayuda familiar y para la operatoria con derivados (código de concepto A05) en la medida que no encuadre en el punto 3.12.1., sin la conformidad previa del BCRA, en la medida que se cumplan la totalidad de los siguientes requisitos:

### Extracción (código N)

- **e1 Potestad** «Acceso al mercado de cambios — formación de activos externos» — Las entidades están facultadas a dar acceso al mercado de cambios a personas humanas residentes para la formación de activos externos bajo los códigos de conceptos A01, A02, A03, A04, A06, A08, A14 y A24, la remisión de ayuda familiar y la operatoria con derivados (código A05), siempre que no encuadre en el punto 3.12.1 y se cumplan los requisitos que siguen. · tramo [exacta]: «Las entidades podrán dar acceso al mercado de cambios a las personas humanas residentes para la formación de activos externos (códigos de conceptos A01, A02, A03, A04, A06, A08, A14 y A24), la remisión de ayuda familiar y para la operatoria con derivados (código de concepto A05)»
- **e2 Condicion** «Cumplimiento de totalidad de requisitos» — La facultad de dar acceso al mercado de cambios se condiciona al cumplimiento de la totalidad de los requisitos que siguen. · tramo [exacta]: «en la medida que se cumplan la totalidad de los siguientes requisitos»
- **e3 Condicion** «No encuadre en punto 3.12.1» — La operatoria no debe encuadrar en lo dispuesto en el punto 3.12.1. · tramo [exacta]: «en la medida que no encuadre en el punto 3.12.1.»
- R: e2 Condicion —condicion_de→ e1 Potestad
- R: e3 Condicion —condicion_de→ e1 Potestad
- R: e1 Potestad —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «Las entidades»)
- Omisión `meta_normativo` [exacta]: «de activos externos bajo otras modalidades, la remisión de ayuda familiar u operaciones con derivados.» — Enumeración introductoria que contextualiza pero no prescribe conducta normativa propia

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| con_marca:18 | no | «de activos externos bajo otras modalidades, la remisión de ayuda familiar u operaciones con derivados.» | `omision_otra_vez` | meta_normativo | om#0 meta_normativo [exacta] con el fragmento entero del título |

## `lingob::3.1.6` — Utilizar efectivamente el trabajo llevado a cabo por las auditorías interna y externa y las

Grupos: omisiones.

### Texto

> *heredado:* Sección 3. Alta Gerencia.
> *heredado:* Los integrantes de la Alta Gerencia deberán tener la idoneidad y experiencia necesarias en la actividad financiera para gestionar el negocio bajo su supervisión así como el control apropiado del personal de esas áreas.
> *heredado:* 3.1. Responsabilidades.
> *heredado:* La Alta Gerencia, como una buena práctica, será responsable de:
> *propio:* 3.1.6. Utilizar efectivamente el trabajo llevado a cabo por las auditorías interna y externa y las funciones relacionadas con el sistema de control interno, conforme a lo establecido en la Sección 5.

### Extracción (código N)

- **e1 Obligacion** «Utilizar efectivamente auditorías interna y externa» — La Alta Gerencia deberá utilizar efectivamente el trabajo llevado a cabo por las auditorías interna y externa y las funciones relacionadas con el sistema de control interno, conforme a lo establecido en la Sección 5. · props: `{"tipo": "otra"}` · no definidas: `{"modalidad": "como una buena práctica", "modalidad_clasificada": "recomendacion"}` · tramo [exacta]: «La Alta Gerencia, como una buena práctica, será responsable de: […] Utilizar efectivamente el trabajo llevado a cabo por las auditorías interna y externa y las funciones relacionadas con el sistema de control interno, conforme a lo establecido en la Sección 5.»
- R: e1 Obligacion —aplica_a→ Sujeto_alta_gerencia (mención «La Alta Gerencia»)
- Omisión `meta_normativo` [exacta]: «conforme a lo establecido en la Sección 5» — Remisión a otra norma; la estructura y contenido específico de la Sección 5 se extrae en su propia unidad

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| sin_marca:29 | sí (remisión pura) | «conforme a lo establecido en la Sección 5» | `extraida_tramo_verificado` |  | e1 Obligacion [exacta] con tramo de dos segmentos que contiene la remisión; además om#0 meta_normativo sobre la misma remisión (precedencia: entidad) |

## `lingob::7.1.7` — En las entidades financieras públicas, la definición de la política en función de su natura-

Grupos: omisiones.

### Texto

> *heredado:* Sección 7. Otras políticas organizacionales.
> *heredado:* 7.1. Política de transparencia.
> *heredado:* A los fines de que la entidad financiera sea dirigida con transparencia, es recomendable una apropiada divulgación de la información hacia el depositante, inversor, accionista y público en general que promueva la disciplina de mercado y, por ende, un buen gobierno societario. El objetivo de la política de transparencia en el gobierno societario es proveer a las citadas partes de la información necesaria para que evalúen la efectividad en la gestión del Directorio y de la Alta Gerencia. La publicación de informes sobre los aspectos del gobierno societario puede asistir a los participantes del mercado y a otras partes interesadas en el monitoreo de la fortaleza y solvencia de la entidad. Es deseable incluir en los sitios públicos de las entidades financieras (páginas de Internet) y en nota, memoria a los estados financieros u otra información periódica, según corresponda, la siguiente información, en función del tamaño, complejidad y estructura propietaria, importancia económica y perfil de riesgo de la entidad, dependiendo también de si la entidad cotiza o no en bolsas:
> *propio:* 7.1.7. En las entidades financieras públicas, la definición de la política en función de su naturaleza jurídica conforme su carta orgánica y/o estatutos.

### Extracción (código N)

- **e1 Obligacion** «Definición de política de transparencia — entidades públicas» — Las entidades financieras públicas deben definir la política de transparencia en función de su naturaleza jurídica conforme su carta orgánica y/o estatutos · props: `{"tipo": "otra"}` · no definidas: `{"modalidad": "Es deseable incluir", "contexto": "Política de transparencia en gobierno societario", "modalidad_clasificada": "recomendacion"}` · tramo [exacta]: «En las entidades financieras públicas, la definición de la política en función de su naturaleza jurídica conforme su carta orgánica y/o estatutos»
- R: e1 Obligacion —aplica_a→ Sujeto_entidad_financiera (mención «las entidades financieras públicas»)
- Omisión `meta_normativo` [exacta]: «Es deseable incluir en los sitios públicos de las entidades financieras (páginas de Internet) y en nota, memoria a los estados financieros u otra información periódica, según corresponda, la siguiente información, en función del tamaño, complejidad y estructura propietaria, importancia económica y perfil de riesgo de l…» — Contenido introductorio que anuncia la lista de ítems; no es una norma propia del punto sino el encabezado que abre la composición con cada ítem

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| con_marca:22 | sí | «Es deseable incluir en los sitios públicos de las entidades financieras (páginas de Internet) y en nota, memoria a los estados financieros u otra información pe…» | `omision_otra_vez` | meta_normativo | om#0 meta_normativo [exacta] con la oración del heredado |

## `ric::5.1.3.4` — Se informará una sola partida 3600000Y, reflejando la situación de la entidad

Grupos: omisiones.

### Texto

> *heredado:* Sección 5. Exigencia por riesgo operacional
> *heredado:* 5.1. Normas de procedimiento
> *heredado:* 5.1.3. Reducción de la exigencia para entidades financieras del Grupo 2 que pertenezcan a
> *heredado:* los Grupos "A", "B" y "C".
> *propio:* 5.1.3.4. Se informará una sola partida 3600000Y, reflejando la situación de la entidad respecto de su calificación; el promedio de las exigencias por riesgo de crédito se calculará en esta Institución en base a los datos sobre exigencia por riesgo de crédito informada en los períodos previos.

### Extracción (código N)

- **e1 Operacion** «Informe partida 3600000Y» — Informe de una sola partida 3600000Y que refleja la situación de la entidad respecto de su calificación · props: `{"tipo": "presentación informativa"}` · tramo [exacta]: «Se informará una sola partida 3600000Y, reflejando la situación de la entidad respecto de su calificación»
- **e2 Operacion** «Cálculo promedio exigencias riesgo crédito» — Cálculo del promedio de las exigencias por riesgo de crédito en la Institución sobre la base de los datos de exigencia por riesgo de crédito informados en períodos previos · props: `{"tipo": "cálculo"}` · tramo [exacta]: «el promedio de las exigencias por riesgo de crédito se calculará en esta Institución en base a los datos sobre exigencia por riesgo de crédito informada en los períodos previos»
- **e3 Obligacion** «Informar partida 3600000Y» — Deber de informar una sola partida 3600000Y · props: `{"tipo": "presentacion_informativa"}` · tramo [exacta]: «Se informará una sola partida 3600000Y»
- **e4 Obligacion** «Calcular promedio exigencias riesgo crédito» — Deber de calcular en la Institución el promedio de las exigencias por riesgo de crédito · props: `{"tipo": "calculo"}` · tramo [exacta]: «el promedio de las exigencias por riesgo de crédito se calculará en esta Institución»
- R: e3 Obligacion —aplica_a→ Sujeto_rol_entidad_comprendida_reginf (mención «la entidad»)
- R: e4 Obligacion —aplica_a→ Sujeto (mención «esta Institución»)
- Omisión `meta_normativo` [exacta]: «reflejando la situación de la entidad respecto de su calificación» — Cláusula que describe el propósito o el contenido informativo de la partida, no una prescripción de conducta separada
- Omisión `meta_normativo` [exacta]: «en base a los datos sobre exigencia por riesgo de crédito informada en los períodos previos» — Cláusula que especifica la base de cálculo, no una prescripción de conducta separada

### M2 — omisiones leídas en T4

| ficha | normativa | tramo de T4 | clase | categoría | ancla |
|---|---|---|---|---|---|
| sin_marca:12 | sí | «reflejando la situación de la entidad respecto de su calificación» | `extraida_tramo_verificado` |  | e1 Operacion [exacta], tramo que contiene el fragmento; además om#0 meta_normativo sobre el mismo fragmento (precedencia: entidad) |

