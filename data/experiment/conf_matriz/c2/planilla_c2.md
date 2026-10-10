# U-CONF-MATRIZ, C2: planilla de la lectura

Lectura de las 60 fichas de `c1/fichas_c1.md` (acta `f5990dff532e6ca2c9eb91e4f8db7e98be105da517e1071c7b8ddc14c8926602`), en el orden de lectura, contra el texto de E0 y la página renderizada. La planilla no lleva el par de cada ficha ni cuenta marcas: eso es C3.

## Reglas de lectura con que apliqué el protocolo

El criterio es el del protocolo del 28/09/2026 (sha256 en el acta) y el §2 del mandato. Estas reglas dicen cómo lo apliqué
a los casos que el protocolo no nombra; no lo cambian.

1. El nodo de destino se lee por su etiqueta, su descripción y su tramo juntos: la ficha da los tres como salida del extractor.
2. Una Condicion que restringe el alcance del destino (sujeto, objeto, finalidad, fecha, elegibilidad, calificación) es
   antecedente: el destino rige solo cuando ella se cumple. Cuenta como correcta. Si además reformula parte de la definición del
   destino, se anota («alcance» o «circular»).
3. Una de varias condiciones alternativas o acumuladas es antecedente del destino. Cuenta como correcta.
4. Una Condicion vacía (el tramo remite a una enumeración que está en otras unidades: «siempre que la contraparte sea:»,
   «las siguientes condiciones») es antecedente. Cuenta como correcta y se anota.
5. Es incorrecta la Condicion cuyo consecuente en el texto es otro y que no restringe el alcance del destino (por ejemplo, una
   regla que fija un plazo), y la que el texto declara indiferente («cuenten o no»).
6. Un destino permisivo o una regla de cómputo tipados Operacion, con la relación cierta, cuentan como correcta y se anotan
   (protocolo: nodo mal tipado con relación cierta).

## Planilla

### F01 — correcta

6.5.2.2: «Los deudores que hayan cancelado la totalidad de los intereses devengados, podrán ser clasificados en “situación normal” si además observan las otras condiciones». La cancelación es antecedente de la facultad de clasificar.

Páginas vistas: `cla_p23.png`.

### F02 — correcta

3.1.1.9: «Para los instrumentos de protección crediticia que estén expuestos solamente a las pérdidas que ocurran hasta su vencimiento, la entidad podrá aplicar el vencimiento contractual». El supuesto delimita cuándo rige la facultad.

Páginas vistas: `cap_p31.png`.

### F03 — correcta

7.2.3: «podrá ser reclasificado en el nivel inmediato superior si, además, el resto de sus deudas reúnen, como mínimo, las condiciones previstas en el citado nivel». Condición adicional de la misma reclasificación.

Páginas vistas: `cla_p37.png`.

### F04 — correcta

7.10.3: los cobros «que resulten elegibles para el mecanismo previsto en este punto […] podrán quedar depositados». La elegibilidad es antecedente del depósito. El destino es permisivo («podrán») y está tipado Operacion: la relación es cierta igual.

Anotaciones: tipo: destino permisivo tipado Operacion.

Páginas vistas: `ext_p102.png`.

### F05 — correcta

3.1.6: «podrá aplicar el tratamiento de transparencia […] siempre que en todo momento se conozca la composición del conjunto subyacente».

Páginas vistas: `cap_p37.png`.

### F06 — correcta

9.3.8: «podrá emitir las certificaciones […] en la medida que verifique las condiciones […], constate que la cancelación tuvo lugar a partir de la fecha de vencimiento y cuente con la documentación». Una de las condiciones acumuladas de la facultad.

Páginas vistas: `ext_p127.png`.

### F07 — correcta

1.4.6: «Habilitada la cuenta mediante el depósito inicial […] o la correspondiente autorización para girar en descubierto, la entidad entregará […] cuadernos de cheques». La habilitación es antecedente de la entrega.

Páginas vistas: `ctacte_p8.png`.

### F08 — correcta

10.4.4: «Para aquellas emitidas u otorgadas a partir del 14/04/25, en la medida que se cumplan las restantes condiciones, también se admitirá que el pago garantizado tuviera que ser concretado a partir de la fecha estimada de embarque». La fecha de emisión delimita cuándo rige la admisión.

Páginas vistas: `ext_p143.png`.

### F09 — correcta

14.2.1, cierre: «En el caso de que la totalidad de los fondos […] no pudiese ser computada como ingresada y liquidada […], las entidades también podrán dar acceso al VPU adherido, sin necesidad de contar con la conformidad previa».

Páginas vistas: `ext_p177.png`.

### F10 — correcta

3.13.1.7 ii): la repatriación con aporte ingresado entre el 02/10/20 y el 20/04/25 queda exceptuada «en la medida que» tenga lugar como mínimo 2 años después. Es una de dos ramas alternativas (i o ii) de la condición de la operación; la relación es cierta.

Páginas vistas: `ext_p37.png`.

### F11 — correcta

7.5.5: «Cuando al vencimiento del plazo no haya sido posible […] determinar el precio definitivo […], la entidad podrá extender el plazo hasta los 120 […] días».

Páginas vistas: `ext_p87.png`.

### F12 — correcta

5.12: «Dichas entidades podrán realizar operaciones de arbitrajes y canjes en el exterior siempre que la contraparte sea:» (la lista 5.12.1 a 5.12.4 está en otras unidades). La relación es cierta; el nodo Condicion queda sin el contenido de la lista (tramo «siempre que la contraparte sea:»).

Anotaciones: condicion vacia: la enumeración está en otras unidades.

Páginas vistas: `ext_p73.png`.

### F13 — correcta

6.5.3.5: «Cuando al menos se haya cumplido con el pago […] del 5 % de las obligaciones refinanciadas y la totalidad de los intereses devengados […], podrá reclasificárselo en niveles superiores».

Páginas vistas: `cla_p24.png`.

### F14 — correcta

2.2.3: «El DNI-d en formato credencial virtual […] podrá ser exhibido […] en la medida que se observen las disposiciones contenidas en el punto 2.12.».

Páginas vistas: `docvig_p5.png`.

### F15 — incorrecta

10.4.2.4: «En el caso de que un mismo pago anticipado incluya bienes de capital y bienes que no lo son, la operación se regirá por el plazo del tipo de bien que represente una mayor proporción». Es una regla que fija qué plazo rige para el compromiso de la declaración jurada (270 o 90 días), no un antecedente del acceso: el antecedente del acceso es contar con la declaración jurada (10.4.2, «en la medida que verifique previamente que se cumplen la totalidad de los siguientes requisitos»). El nodo Condicion tiene la forma de supuesto («cuando…»), pero su consecuente es el plazo, no el acceso.

Páginas vistas: `ext_p139.png`, `ext_p140.png`.

### F16 — correcta

2.1.17: el destino admitido son las financiaciones garantizadas por cartas de crédito «emitidas por bancos del exterior o bancos multilaterales de desarrollo que cumplan con lo previsto en el punto 3.1.». El requisito sobre el emisor delimita cuándo la financiación es un destino admitido de la capacidad de préstamo (2.1, intro).

Páginas vistas: `polcre_p8.png`.

### F17 — correcta

8.3.4.4: la revocación de la autorización para funcionar es una de las alternativas del evento i) (con la solvencia o liquidez afectada) y «La emisión de nuevas acciones como consecuencia de haberse producido alguno de tales eventos». El nodo Condicion omite «estando afectada la solvencia y/o liquidez»; la relación es cierta.

Anotaciones: condicion parcial: omite el presupuesto del evento.

Páginas vistas: `cap_p159.png`, `cap_p160.png`.

### F18 — correcta

7.9.6: «podrán acceder al mercado, en la medida que se cumplan las condiciones previstas en el punto 3.11.3., para la compra de moneda extranjera».

Páginas vistas: `ext_p99.png`.

### F19 — correcta

4.8.1.2: el acceso con fondos de BOPREAL cubre «el pago de deudas comerciales por importaciones de servicios […] que resultaban elegibles de acuerdo con lo dispuesto en el punto 4.5.». La elegibilidad restringe qué pagos quedan comprendidos.

Páginas vistas: `ext_p64.png`.

### F20 — correcta

2.1.1: «También quedan comprendidas las operaciones que tengan por destino financiar a prestadores de servicios […], siempre que se verifique que el flujo de ingresos futuros […] sea suficiente para la cancelación de la financiación y se constate […]». Una de dos condiciones acumuladas.

Páginas vistas: `polcre_p6.png`.

### F21 — correcta

2.8: «Las entidades podrán dar curso a estas operaciones con clientes en la medida que no correspondan a operaciones alcanzadas por la obligación de liquidación».

Páginas vistas: `ext_p15.png`.

### F22 — correcta

8.3.4.4: la autorización de la reestructuración en defensa de los depositantes es una de las alternativas del evento i) y «La emisión de nuevas acciones como consecuencia de haberse producido alguno de tales eventos». Mismo destino y unidad que otra ficha de la muestra (otra alternativa del evento i).

Páginas vistas: `cap_p159.png`, `cap_p160.png`.

### F23 — correcta

3.12.2: «Las restantes operaciones de derivados financieros que quieran ser cursadas con acceso al mercado de cambios por parte de residentes que no sean entidades autorizadas a operar en cambios se regirán por lo dispuesto en los puntos 3.9. y 3.10.». La Condicion restringe el alcance subjetivo del destino y reformula parte de su propia definición (anotación: condición de alcance, cercana a un Sujeto); la relación es cierta como supuesto de aplicación.

Anotaciones: alcance: la Condicion reformula parte de la definición del destino.

Páginas vistas: `ext_p36.png`.

### F24 — correcta

3.11.3: «podrán dar acceso al mercado de cambios a los residentes con endeudamientos […] para la compra de moneda extranjera para la constitución de las garantías […], en las siguientes condiciones:». La Condicion es la finalidad que restringe el acceso y reformula parte de la definición del destino (anotación: condición de alcance por finalidad; las condiciones enumeradas 3.11.3.1 y 3.11.3.2 están en otras unidades); la relación es cierta como restricción.

Anotaciones: alcance: la Condicion es la finalidad que define el destino.

Páginas vistas: `ext_p35.png`.

### F25 — correcta

10.5.5.2: «podrá imputarlo en el SEPAIMPO como en “gestión de cobro” cuando se dé alguna de las siguientes condiciones: i) Control de cambios en el país del exportador». Una de tres condiciones alternativas. El destino es permisivo («podrá») y está tipado Operacion.

Anotaciones: tipo: destino permisivo tipado Operacion.

Páginas vistas: `ext_p146.png`.

### F26 — correcta

4.4 (texto heredado de la unidad 4.4.2): «Los importadores de bienes podrán suscribir […] BOPREAL […]. La entidad que concrete la oferta de suscripción en nombre del cliente deberá contar con las respectivas certificaciones sobre el monto pendiente de pago». Requisito de la suscripción, redactado como obligación de la entidad (anotación). La relación sale del texto heredado, no del propio de 4.4.2.

Anotaciones: requisito redactado como obligación de la entidad; relación en el texto heredado, no en el propio.

Páginas vistas: `ext_p60.png`.

### F27 — correcta

2.2.3: «En el caso de que los cobros sean ingresados a través del sistema de monedas locales se considerará cumplimentada la liquidación por el monto acreditado en moneda nacional». El supuesto (ingreso por el sistema de monedas locales) es antecedente del tratamiento que el destino describe («Se considera cumplimentada la liquidación por el monto acreditado…», en su descripción). Anotación: el destino tiene el mismo tramo que la Condicion, así que por etiqueta y tramo la arista es circular; leído por etiqueta, descripción y tramo, la relación es cierta. Con una lectura estricta del nodo por su etiqueta sería incorrecta: queda para la adjudicación.

Anotaciones: circular: el destino tiene el mismo tramo que la Condicion; la consecuencia del texto está solo en su descripción.

Páginas vistas: `ext_p11.png`.

Cambio antes del sello: marcada «incorrecta» en el borrador; pasó a «correcta» antes del sello, al revisar la consistencia con las condiciones de alcance (F23, F45, F60), que reformulan parte de la definición del destino y estaban marcadas correctas. Ninguna cifra estaba calculada.

### F28 — correcta

8.3.4.4 i): «estando afectada la solvencia y/o liquidez de la entidad financiera» es el presupuesto del evento i), y «La emisión de nuevas acciones como consecuencia de haberse producido alguno de tales eventos». Tercera arista de la muestra entre esta unidad y este destino.

Páginas vistas: `cap_p159.png`, `cap_p160.png`.

### F29 — correcta

3.14.4: «Las operaciones de arbitraje que no impliquen transferencias al exterior podrán realizarse sin restricciones en la medida que los fondos se debiten de una cuenta en moneda extranjera del cliente en una entidad financiera local».

Páginas vistas: `ext_p40.png`.

### F30 — correcta

7.8.2.5: «En caso de que un permiso de embarque definitivo esté asociado a un embarque provisorio oficializado con anterioridad al 02/09/19, las entidades podrán dar el cumplido de embarque del permiso definitivo».

Páginas vistas: `ext_p92.png`.

### F31 — correcta

14.5.7 i): dentro de las condiciones del cómputo («podrán ser computados […] en la medida que:»), «La operación podrá incluir bienes que no revistan la condición de bien de capital en la medida que aquellos que lo sean representen como mínimo el 90 %». Es un requisito que puede fallar y del que depende el cómputo de un aporte con bienes mixtos.

Páginas vistas: `ext_p182.png`.

### F32 — correcta

7.5.2: «Cuando el monto pendiente de ingreso […] haya sido prefinanciado en su totalidad y los fondos liquidados […], se podrá extender el plazo para la liquidación de divisas del embarque hasta la fecha de vencimiento de la correspondiente financiación».

Páginas vistas: `ext_p86.png`.

### F33 — correcta

2.12.2.3 (tabla de ponderadores, 0 %): «financiaciones otorgadas a beneficiarios de la seguridad social o a empleados públicos […], en la medida que dichas operaciones estén denominadas en pesos, la fuente de fondos sea en esa moneda y las cuotas […] no excedan […] del 30 %». La condición delimita qué financiaciones entran en el renglón; la consecuencia del texto es el ponderador, que no es nodo de la arista (anotación).

Anotaciones: consecuencia fuera de la arista: el texto asigna un ponderador, que no es nodo.

Páginas vistas: `cap_p23.png`.

### F34 — correcta

2.2.3: «En caso de que se trate de servicios prestados a residentes paraguayos o uruguayos facturados en la moneda del país de destino de la exportación se computará el equivalente en dicha moneda del monto acreditado». El supuesto es antecedente del tratamiento que el destino describe («Se computa el equivalente en dicha moneda del monto acreditado», en su descripción). Anotación: mismo tramo en la Condicion y en el destino (circular por etiqueta y tramo), mismo patrón y misma unidad que otra ficha de la muestra; con una lectura estricta del nodo por su etiqueta sería incorrecta: queda para la adjudicación.

Anotaciones: circular: el destino tiene el mismo tramo que la Condicion; la consecuencia del texto está solo en su descripción.

Páginas vistas: `ext_p11.png`.

Cambio antes del sello: marcada «incorrecta» en el borrador; pasó a «correcta» antes del sello, al revisar la consistencia con las condiciones de alcance (F23, F45, F60), que reformulan parte de la definición del destino y estaban marcadas correctas. Ninguna cifra estaba calculada.

### F35 — correcta

10.10.2.2 ii): los pagos de bienes de capital con registro pendiente se admiten «en la medida que: […] ii) la suma de los pagos anticipados, a la vista y de deuda comercial […] no supera el 80 %». El destino (pago anticipado) es uno de los pagos que la condición acota.

Páginas vistas: `ext_p154.png`.

### F36 — correcta

3.3 y 3.3.2: «deberán verificar que se cumplan las condiciones especificadas a continuación: […] El acceso al mercado de cambios tiene lugar a partir de la fecha de vencimiento del interés a pagar». Condición temporal del acceso; el tramo del destino contiene el de la Condicion, pero son conceptos distintos (el acceso y su momento).

Páginas vistas: `ext_p16.png`.

### F37 — correcta

10.3.5: «podrá dar acceso al mercado de cambios […] en la medida que verifique previamente que se cumplen la totalidad de requisitos detallados en el punto 10.3.2.».

Páginas vistas: `ext_p137.png`.

### F38 — correcta

6.5.3.11: entre los indicadores de la categoría «con problemas», que el cliente «Haya sido demandado judicialmente […], cuando ello se encuentre vinculado a la falta de pago y registre mora […] no superior a 180 días». La vinculación con la falta de pago califica el indicador del que depende la clasificación. Anotación: el texto habla de indicadores que «pueden reflejar» la situación, no de condiciones necesarias; la clasificación está tipada Operacion.

Anotaciones: indicador, no condición necesaria; tipo: clasificación tipada Operacion.

Páginas vistas: `cla_p25.png`.

### F39 — correcta

6.5.5.2: «Cuando al menos se haya cumplido con el pago, sin haber incurrido en atrasos superiores a los 31 días del 15 % de las obligaciones refinanciadas y la totalidad de los intereses devengados, podrá reclasificarse al deudor en el nivel inmediato superior».

Páginas vistas: `cla_p28.png`.

### F40 — correcta

7.3.10: entre las operaciones habilitadas para aplicar cobros de exportaciones, «Financiaciones comerciales o financieras asociadas a la realización de pagos diferidos o a la vista de importaciones de bienes que cumplan las condiciones y requisitos previstos en el punto 7.11.». La remisión a 7.11 restringe qué financiaciones quedan habilitadas.

Páginas vistas: `ext_p85.png`.

### F41 — correcta

8.3.5.2: los instrumentos «pueden reconocerse en el PNb de la entidad financiera si observan todos los requisitos para su clasificación como PNb a efectos de la RPC».

Páginas vistas: `cap_p161.png`.

### F42 — correcta

4.8.1 y 4.8.1.1: los clientes podrán acceder con fondos de BOPREAL «para concretar: […] el pago de deudas comerciales por importaciones de bienes […] que resultaban elegibles de acuerdo con lo dispuesto en el punto 4.4.». La elegibilidad es condición del acceso para esa finalidad (una de las cinco enumeradas); el destino es la facultad general de acceso.

Páginas vistas: `ext_p64.png`.

### F43 — correcta

14.5.7 i): los aportes «podrán ser computados […] en la medida que: i) El VPU haya demostrado el registro de ingreso aduanero del bien de capital por un valor consistente con el monto del aporte». Mismo destino y unidad que otra ficha de la muestra.

Páginas vistas: `ext_p182.png`.

### F44 — correcta

10.10.2.1: «Pagos a la vista de importaciones de bienes cursados por personas humanas o […] MiPyMe […], en la medida que se trate de bienes que hayan sido embarcados en origen a partir del 14/04/25 y las posiciones arancelarias de los bienes no correspondan a aquellas comprendidas en el punto 12.1.».

Páginas vistas: `ext_p154.png`.

### F45 — correcta

8.2.1 y 8.2.1.1: motivo de inclusión en la Central, «Haber incurrido en uno o varios rechazos de cheques […] por: Falta de fondos suficientes disponibles en cuenta o de autorización para girar en descubierto». La falta de autorización es la causa del rechazo y el texto la enuncia como tal. Anotación: el consecuente que regula el texto es la inclusión en la Central, que no es nodo de la arista; la Condicion toma solo uno de los dos términos («fondos» o «autorización»).

Anotaciones: consecuencia fuera de la arista: el texto regula la inclusión en la Central; condicion parcial: uno de dos términos.

Páginas vistas: `ctacte_p44.png`.

### F46 — correcta

5.8.2: el ingreso «A nombre de la empresa local que actúa como representante en el país de la empresa procesadora de pagos en la medida que se cumplan las siguientes condiciones:» (5.8.2.1 y siguientes, en otras unidades). La relación es cierta; la Condicion queda sin el contenido de la lista (tramo «en la medida que se cumplan las siguientes condiciones»).

Anotaciones: condicion vacia: la enumeración está en otras unidades.

Páginas vistas: `ext_p71.png`.

### F47 — correcta

5.1.1.2: «Cuando el cliente mantenga financiaciones por ambos conceptos, los créditos para consumo o vivienda se sumarán a los de la cartera comercial para determinar su encuadramiento». El destino es una regla de cómputo tipada Operacion (anotación); la relación es cierta.

Anotaciones: tipo: regla de cómputo tipada Operacion.

Páginas vistas: `cla_p16.png`.

### F48 — correcta

9.3.5: «Se podrán emitir las certificaciones de aplicación […], en la medida que en la cuenta de la entidad se hayan acreditado ingresos de divisas que correspondan a:» (9.3.5.1 a 9.3.5.3 en otras unidades). La relación es cierta; la Condicion queda sin la enumeración.

Anotaciones: condicion vacia: la enumeración está en otras unidades.

Páginas vistas: `ext_p126.png`.

### F49 — correcta

3.16.2.1: «la entidad también podrá aceptar una declaración jurada del cliente en la que deje constancia que no se excede tal monto al considerar que, parcial o totalmente, los activos externos líquidos: i) fueron utilizados durante esa jornada para realizar pagos que hubieran tenido acceso al mercado local de cambios». Una de siete situaciones alternativas que hacen aceptable la declaración. Anotación: la situación es contenido de lo que el cliente declara.

Anotaciones: la situación es contenido de la declaración jurada.

Páginas vistas: `ext_p43.png`, `ext_p44.png`.

### F50 — correcta

7.8.4, cierre: «la entidad encargada del seguimiento del permiso de embarque podrá extender el plazo de liquidación del permiso cuando, por el monto que se encuentre pendiente de liquidación, el cliente haya utilizado este mecanismo y los fondos sigan depositados en “Cuenta especial […]”».

Páginas vistas: `ext_p93.png`.

### F51 — correcta

2.1.4: «Financiaciones a productores de bienes para ser exportados […], siempre que cuenten con avales o garantías totales en moneda extranjera de dichos terceros y/o contratos de venta en firme en moneda extranjera y/o en bienes exportables». Una de las alternativas («y/o») de la condición del destino admitido.

Páginas vistas: `polcre_p7.png`.

### F52 — correcta

7.8.2.4: «Cuando al vencimiento del plazo no se hubiera oficializado aún el permiso de embarque definitivo, las entidades podrán otorgar el cumplido del permiso de embarque provisorio».

Páginas vistas: `ext_p92.png`.

### F53 — correcta

4.4 y 4.4.2: los importadores podrán suscribir BOPREAL y la entidad deberá contar con certificaciones que «deberán verificar que: […] la operación se encuentra declarada, en caso de corresponder, en la última presentación vencida del “Relevamiento de activos y pasivos externos”». Requisito de la suscripción, verificado por la certificación. Misma unidad y destino que otra ficha de la muestra.

Páginas vistas: `ext_p60.png`.

### F54 — correcta

5.8: «Las entidades podrán elaborar un boleto global diario para las situaciones que se detallan a continuación, en la medida que se verifiquen todas las condiciones indicadas en cada caso». La relación es cierta; la Condicion es una remisión genérica a las condiciones de cada caso, sin contenido propio.

Anotaciones: condicion vacia: remisión genérica a las condiciones de cada caso.

Páginas vistas: `ext_p71.png`.

### F55 — correcta

7.3.11: «Se admitirá la aplicación de divisas […] en la medida que el cliente demuestre que […] ingresó y liquidó divisas […] y por la porción no liquidada del cobro concretó operaciones de compraventa con títulos valores […]». Una de dos condiciones acumuladas.

Páginas vistas: `ext_p85.png`.

### F56 — correcta

7.9.2: «Las operaciones de los puntos 7.9.1.1. a 7.9.1.3. serán elegibles en la medida que los fondos liquidados sean destinados a la financiación de proyectos de inversión en el país que generen:». La relación es cierta; la Condicion queda trunca («que generen», con 7.9.2.1 y 7.9.2.2 en otras unidades) y el destino es la elegibilidad, tipada Operacion (anotación).

Anotaciones: condicion trunca; tipo: elegibilidad tipada Operacion.

Páginas vistas: `ext_p97.png`.

### F57 — incorrecta

3.3 y 3.3.3: entre lo que «Se volcarán en un “Manual de procedimientos de clasificación y previsión”», «El ejercicio de la opción de agrupar las financiaciones de naturaleza comercial […], cuenten o no con garantías preferidas, junto con los créditos para consumo o vivienda». «Cuenten o no con garantías preferidas» es una cláusula de indiferencia: dice que la opción rige con o sin garantías, es decir, que eso no la condiciona. La propia descripción del extractor la llama «condición indiferente». El texto no sostiene que sea antecedente de la opción.

Páginas vistas: `cla_p9.png`.

### F58 — correcta

4.3.3.1 iii): «la exposición de la entidad financiera hacia el miembro compensador podrá recibir el tratamiento del acápite i) precedente, siempre que se cumplan las siguientes condiciones: a) La CCP identifica a las transacciones a compensar como transacciones de clientes y las garantías […] son mantenidas […] bajo acuerdos que impiden que el cliente sufra pérdidas […]». Una de dos condiciones acumuladas (a y b).

Páginas vistas: `cap_p90.png`.

### F59 — correcta

10.3.2: «La entidad interviniente podrá dar acceso al mercado de cambios para el pago […], en la medida que verifique previamente la totalidad de los siguientes requisitos:» (10.3.2.1 y siguientes, en otras unidades). La relación es cierta; la Condicion queda sin la enumeración.

Anotaciones: condicion vacia: la enumeración está en otras unidades.

Páginas vistas: `ext_p134.png`.

### F60 — correcta

5.2: «Las entidades financieras podrán mantener en bancos del exterior […] certificados de depósito a plazo fijo en entidades que cuenten con calificación internacional no inferior a “AA”». La calificación restringe en qué entidades rige la facultad; reformula parte de la definición del destino (anotación, como en las condiciones de alcance).

Anotaciones: alcance: la Condicion reformula parte de la definición del destino.

Páginas vistas: `polcre_p13.png`.
