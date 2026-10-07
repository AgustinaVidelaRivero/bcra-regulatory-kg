# Control (1): 30 nodos que el código asigna a la causa (i) sin leer (semilla 20261007)

## Unidad `ext::10.11.3` (item)
- herencia: **[abre la lista]** [intro 10.11] aduanero hasta el 12/12/23.
Se requerirá la conformidad previa del BCRA para el acceso al mercado de cambios para
realizar pagos de importaciones por bienes con registro de ingreso aduanero hasta el
12/12/23, excepto cuando, adicionalmente a los restantes requisitos aplicables, la entidad
verifique que:
- texto propio: 10.11.3. el cliente cuenta por el equivalente al monto a pagar con una “Certificación por los
regímenes de acceso a divisas para la producción incremental de petróleo y/o gas
natural (Decreto 277/22)” emitida en el marco de lo dispuesto en el punto 3.17.; o
- entidades de la unidad:
  - `c1` Condicion: Cliente cuenta con Certificación regímenes acceso divisas — El cliente cuenta con una Certificación por los regímenes de acceso a divisas para la producción incremental de petróleo y/o gas natural (Decreto 277/22) emitida conforme al punto 3.17, por el equival
  - `com1` Comunicacion: Decreto 277/22 — 
- relaciones del crudo (sin establecida_en ni de sujeto): to referencia com1
- NODOS A CLASIFICAR:
  - **caso C1** Condicion `c1`: Cliente cuenta con Certificación regímenes acceso divisas | descripcion: El cliente cuenta con una Certificación por los regímenes de acceso a divisas para la producción incremental de petróleo y/o gas natural (Decreto 277/22) emitida conforme al punto 3.17, por el equivalente al monto a pagar. | tramo: el cliente cuenta por el equivalente al monto a pagar con una "Certificación por los regímenes de acceso a divisas para la producción incremental de petróleo y/o gas natural (Decreto 277/22)" emitida en el marco de lo dispuesto en el punto 3.17.

## Unidad `cla::6.5.4.4` (item)
- herencia: [intro 6.5] Cada cliente, y la totalidad de sus financiaciones comprendidas, se incluirá en una de las si-
guientes cinco categorías, las que se definen teniendo en cuenta las condiciones que se deta-
llan en cada caso.
Los clientes que no registren asistencia crediticia de la entidad y que posteriormente reciban fi-
nanciaciones de ésta que no superen el importe resultante de aplicar sobre el saldo de deuda
registrado en el sistema financiero, según la última información disponible en la “Central de
deudor | **[abre la lista]** [intro 6.5.4] El análisis del flujo de fondos del cliente demuestra que es altamente improbable que
pueda atender la totalidad de sus compromisos financieros.
Entre los indicadores que pueden reflejar esta situación se destacan que el cliente:
- texto propio: 6.5.4.4. Tenga un sistema de información inadecuado, lo que impide conocer con exacti-
tud la real situación financiera y económica de la empresa. La información que
se presenta no es confiable pues no cuenta con la adecuada documentación
respaldatoria. En general, la información no es consistente y no está actualizada.
- entidades de la unidad:
  - `e1` Condicion: Sistema de información inadecuado — El cliente tiene un sistema de información inadecuado que impide conocer con exactitud su real situación financiera y económica
  - `e2` Condicion: Información no confiable sin documentación respaldatoria — La información presentada no es confiable porque carece de documentación respaldatoria adecuada
  - `e3` Condicion: Información inconsistente y desactualizada — La información no es consistente y no está actualizada
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso C2** Condicion `e3`: Información inconsistente y desactualizada | descripcion: La información no es consistente y no está actualizada | tramo: En general, la información no es consistente y no está actualizada

## Unidad `ext::6.7` (item)
- herencia: **[abre la lista]** [chapeau_seccion S6] En el marco de estas disposiciones se definen los siguientes conceptos:
- texto propio: 6.7. Posición general de cambios (PGC).
Comprenderá la totalidad de los activos externos líquidos de la entidad, netos de los saldos
deudores de corresponsalía originados en la operatoria del mercado de cambios. También
quedarán comprendidas las compras y ventas concertadas en el mercado de cambios y que
se encuentran pendientes de liquidación.
Serán considerados activos externos líquidos de la entidad, entre otros: monedas y billetes en
moneda extranjera, disponibilidades en oro amonedado o en barras de buena entrega, saldos
acreedores de corresponsalía (incluyendo las transferencias a favor de terceros sin liquidación
concertada), otros depósitos a la vista en entidades financieras del exterior, inversiones en
títulos públicos externos y certificados de depósito a plazo.
No formarán parte de la PGC: inversiones directas en el exterior, activos externos de terceros
en custodia, ventas y compras a término de divisas o valores externos, depósitos en el BCRA
en moneda extranjera en cuentas a nombre de la entidad y demás activos locales en moneda
extranjera.
- entidades de la unidad:
  - `e1` Definicion: PGC — activos externos líquidos netos — La totalidad de los activos externos líquidos de la entidad, netos de los saldos deudores de corresponsalía originados en la operatoria del mercado de cambios.
  - `e2` Definicion: PGC — compras y ventas concertadas pendientes — Incluye las compras y ventas concertadas en el mercado de cambios que se encuentran pendientes de liquidación.
  - `e3` Definicion: Activos externos líquidos — componentes — Monedas y billetes en moneda extranjera, disponibilidades en oro amonedado o en barras de buena entrega, saldos acreedores de corresponsalía (incluyendo las transferencias a favor de terceros sin liqu
  - `e4` Excepcion: Exclusiones de PGC — inversiones directas — Las inversiones directas en el exterior no forman parte de la Posición general de cambios.
  - `e5` Excepcion: Exclusiones de PGC — activos en custodia — Los activos externos de terceros en custodia no forman parte de la Posición general de cambios.
  - `e6` Excepcion: Exclusiones de PGC — ventas y compras a término — Las ventas y compras a término de divisas o valores externos no forman parte de la Posición general de cambios.
  - `e7` Excepcion: Exclusiones de PGC — depósitos BCRA moneda extranjera — Los depósitos en el BCRA en moneda extranjera en cuentas a nombre de la entidad no forman parte de la Posición general de cambios.
  - `e8` Excepcion: Exclusiones de PGC — activos locales moneda extranjera — Los demás activos locales en moneda extranjera no forman parte de la Posición general de cambios.
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso C3** Excepcion `e8`: Exclusiones de PGC — activos locales moneda extranjera | descripcion: Los demás activos locales en moneda extranjera no forman parte de la Posición general de cambios. | tramo: No formarán parte de la PGC: demás activos locales en moneda extranjera

## Unidad `docvig::1.1` (punto_no_item)
- herencia: [encabezado S1] Sección 1. Para argentinos
- texto propio: 1.1. De hasta 75 años al 31.12.14.
Documento Nacional de Identidad digital (DNI-d), que comprende tanto al formato tarjeta como
a la credencial virtual para dispositivos móviles inteligentes.
- entidades de la unidad:
  - `e1` Definicion: DNI-d — Documento Nacional de Identidad digital — Comprende tanto al formato tarjeta como a la credencial virtual para dispositivos móviles inteligentes
  - `e2` Condicion: Edad hasta 75 años al 31.12.14 — Personas de hasta 75 años de edad al 31 de diciembre de 2014
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso C4** Condicion `e2`: Edad hasta 75 años al 31.12.14 | descripcion: Personas de hasta 75 años de edad al 31 de diciembre de 2014 | tramo: De hasta 75 años al 31.12.14

## Unidad `ctacte::8.2.3.2` (punto_no_item)
- herencia: [encabezado 8.2.3] 8.2.3. En la “Central de cheques denunciados como extraviados, sustraídos o adulterados”.
- texto propio: 8.2.3.2. Haber denunciado la entidad el extravío, sustracción o adulteración en algunas
de sus filiales de los documentos mencionados en el punto 7.1., excepto la fór-
mula especial para solicitar cuadernos de cheques.
- entidades de la unidad:
  - `e1` Condicion: Denuncia de extravío, sustracción o adulteración en filiales — La entidad ha denunciado el extravío, sustracción o adulteración de documentos en algunas de sus filiales, conforme a lo mencionado en el punto 7.1.
  - `e2` Excepcion: Excepción fórmula especial para cuadernos de cheques — No se incluye en la denuncia la fórmula especial para solicitar cuadernos de cheques
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso C5** Excepcion `e2`: Excepción fórmula especial para cuadernos de cheques | descripcion: No se incluye en la denuncia la fórmula especial para solicitar cuadernos de cheques | tramo: excepto la fórmula especial para solicitar cuadernos de cheques

## Unidad `polcre::6.2.1.1` (item)
- herencia: **[abre la lista]** [intro 6.2.1] costo de construcción (“ICC”) - Ley 27.271 (“UVI”) estarán sujetas a las siguientes condi-
ciones:
- texto propio: 6.2.1.1. Destino: préstamos hipotecarios.
- entidades de la unidad:
  - `c1` Condicion: Destino préstamos hipotecarios — Las operaciones de financiación de Unidades de Vivienda actualizables por el índice del costo de construcción (ICC) - Ley 27.271 (UVI) deben tener como destino préstamos hipotecarios
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso C6** Condicion `c1`: Destino préstamos hipotecarios | descripcion: Las operaciones de financiación de Unidades de Vivienda actualizables por el índice del costo de construcción (ICC) - Ley 27.271 (UVI) deben tener como destino préstamos hipotecarios | tramo: Destino: préstamos hipotecarios

## Unidad `cla::2.2.1.2` (item)
- herencia: **[abre la lista]** [encabezado 2.2.1] 2.2.1. Los siguientes conceptos por intermediación financiera:
- texto propio: 2.2.1.2. Compras a término por pases pasivos, a término no vinculadas a pases pasivos
y al contado a liquidar y sus correspondientes primas a devengar.
- entidades de la unidad:
  - `e1` Excepcion: Exclusión — compras a término por pases pasivos — Quedan exceptuadas de la clasificación de financiaciones las compras a término por pases pasivos, a término no vinculadas a pases pasivos y al contado a liquidar, así como sus correspondientes primas 
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso C7** Excepcion `e1`: Exclusión — compras a término por pases pasivos | descripcion: Quedan exceptuadas de la clasificación de financiaciones las compras a término por pases pasivos, a término no vinculadas a pases pasivos y al contado a liquidar, así como sus correspondientes primas a devengar | tramo: Compras a término por pases pasivos, a término no vinculadas a pases pasivos y al contado a liquidar y sus correspondientes primas a devengar

## Unidad `cla::6.5.3.4` (item)
- herencia: [intro 6.5] Cada cliente, y la totalidad de sus financiaciones comprendidas, se incluirá en una de las si-
guientes cinco categorías, las que se definen teniendo en cuenta las condiciones que se deta-
llan en cada caso.
Los clientes que no registren asistencia crediticia de la entidad y que posteriormente reciban fi-
nanciaciones de ésta que no superen el importe resultante de aplicar sobre el saldo de deuda
registrado en el sistema financiero, según la última información disponible en la “Central de
deudor | **[abre la lista]** [intro 6.5.3] El análisis del flujo de fondos del cliente demuestra que tiene problemas para atender
normalmente la totalidad de sus compromisos financieros y que, de no ser corregidos,
esos problemas pueden resultar en una pérdida para la entidad financiera.
Entre los indicadores que pueden reflejar esta situación se destacan que el cliente:
- texto propio: 6.5.3.4. Tenga un sistema de información no del todo adecuado, que dificulte conocer
con exactitud la real situación financiera y económica del cliente. La información
no es totalmente consistente y no existe un proceso de actualización adecuado
que permita contar con ella en el momento oportuno.
- entidades de la unidad:
  - `e1` Condicion: Sistema de información no adecuado — El cliente tiene un sistema de información no del todo adecuado que dificulta conocer con exactitud su real situación financiera y económica.
  - `e2` Condicion: Información no consistente y sin actualización adecuada — La información del cliente no es totalmente consistente y no existe un proceso de actualización adecuado que permita contar con ella en el momento oportuno.
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso C8** Condicion `e1`: Sistema de información no adecuado | descripcion: El cliente tiene un sistema de información no del todo adecuado que dificulta conocer con exactitud su real situación financiera y económica. | tramo: Tenga un sistema de información no del todo adecuado, que dificulte conocer con exactitud la real situación financiera y económica del cliente

## Unidad `ext::10.2.2` (punto_no_item)
- herencia: [encabezado 10.2] 10.2. Definiciones.
- texto propio: 10.2.2. Registro de ingreso aduanero.
A los efectos de esta norma se considera que una importación de bienes cuenta con
el registro de ingreso aduanero cuando el importador realizó la oficialización del
despacho de importación para su posterior despacho a plaza de los bienes.
También se da cumplimiento a dicho registro cuando los bienes son ingresados al
país con despacho a plaza a través de Solicitud Particular o Courier o se
cumplimentó el trámite aduanero por el ingreso de bienes del exterior a zonas francas
nacionales y dicho ingreso se corresponde con una venta de bienes de un no
residente a un residente.
No se incluyen los registros aduaneros por importaciones suspensivas de depósitos
de almacenamiento ni los ingresos de importaciones temporarias sin giro de divisas.
- entidades de la unidad:
  - `e1` Definicion: Registro de ingreso aduanero — importación — Una importación de bienes cuenta con el registro de ingreso aduanero cuando el importador realizó la oficialización del despacho de importación para su posterior despacho a plaza de los bienes.
  - `e2` Definicion: Registro de ingreso aduanero — despacho a plaza — Se da cumplimiento al registro de ingreso aduanero cuando los bienes son ingresados al país con despacho a plaza a través de Solicitud Particular o Courier.
  - `e3` Definicion: Registro de ingreso aduanero — zonas francas — Se da cumplimiento al registro de ingreso aduanero cuando se cumplimentó el trámite aduanero por el ingreso de bienes del exterior a zonas francas nacionales y dicho ingreso se corresponde con una ven
  - `e4` Excepcion: Exclusión — importaciones suspensivas de depósitos — No se incluyen los registros aduaneros por importaciones suspensivas de depósitos de almacenamiento en la definición de registro de ingreso aduanero.
  - `e5` Excepcion: Exclusión — importaciones temporarias sin giro — No se incluyen los ingresos de importaciones temporarias sin giro de divisas en la definición de registro de ingreso aduanero.
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso C9** Excepcion `e5`: Exclusión — importaciones temporarias sin giro | descripcion: No se incluyen los ingresos de importaciones temporarias sin giro de divisas en la definición de registro de ingreso aduanero. | tramo: No se incluyen los ingresos de importaciones temporarias sin giro de divisas

## Unidad `cap::2.10` (punto_no_item)
- herencia: [chapeau_seccion S2] A los efectos de la aplicación de las disposiciones de la presente sección, las entidades financieras
se clasificarán en:
i)Grupo 1: entidades calificadas por el BCRA como de importancia sistémica a nivel local | [chapeau_seccion S2] (D-SIB) y sucursales o subsidiarias de bancos del exterior calificados como de impor-
tancia sistémica global (G-SIB). | [chapeau_seccion S2] ii) Grupo 2: entidades financieras no comprendidas en el acápite i).
En aquellos casos en que no se establezcan disposiciones específicas para cada uno de los citados
grupos de entidades financieras, deberá aplicarse el mismo tratamiento a ambos grupos.
Las entidades financieras que presenten cambios en su calificación –conforme a lo previsto en los
acápites precedentes–, contarán con un plazo de 6 meses para aplicar las disposiciones específicas
correspondientes al nuevo grupo al que pertenezca
- texto propio: 2.10. Exposiciones en situación de incumplimiento.
Comprende a todas aquellas exposiciones a un deudor respecto del que se verifique alguna
de las siguientes situaciones:
i) El deudor posee un crédito en mora de más de 90 días. Se considera que un descubierto
en cuenta corriente se encuentra en mora a partir del momento en que el deudor excede
el límite autorizado o se le comunica un nuevo límite y éste es inferior a su saldo deudor.
ii) El deudor cuenta con cualquier obligación significativa respecto de la cual se haya sus-
pendido el devengamiento de intereses, o los intereses se encuentren totalmente previ-
sionados.
iii) Se ha dado de baja contablemente una obligación o se ha constituido una previsión es-
pecífica frente a una desmejora significativa en la calidad crediticia del deudor con poste-
rioridad al otorgamiento del crédito.
iv) Se ha vendido un crédito con una pérdida significativa con motivo de su situación crediti-
cia.
v) Se ha acordado una reestructuración de una obligación crediticia que puede resultar en
una reducción de la deuda como consecuencia de quitas, diferimientos del pago del capi-
tal o de los intereses o una disminución de las comisiones aplicables.
vi) Se ha solicitado la quiebra del deudor u otra medida similar que produzca el diferimiento
o impida el recupero del crédito por parte de la entidad.
vii) El deudor ha solicitado su concurso preventivo o quiebra u otra medida similar que pro-
duzca el diferimiento o impida el recupero del crédito por parte de la entidad.
viii) La entidad financiera considera que es improbable que pueda recuperar el total de las
acreencias del deudor sin recurrir a la ejecución de las garantías u otras medidas en de-
fensa de su crédito.
- entidades de la unidad:
  - `e1` Definicion: Exposiciones en situación de incumplimiento — Todas aquellas exposiciones a un deudor respecto del que se verifique alguna de las siguientes situaciones: (i) El deudor posee un crédito en mora de más de 90 días; (ii) El deudor cuenta con cualquie
  - `e2` Condicion: Crédito en mora de más de 90 días — Situación en que el deudor posee un crédito en mora de más de 90 días. Se considera que un descubierto en cuenta corriente se encuentra en mora a partir del momento en que el deudor excede el límite a
  - `e3` Condicion: Obligación significativa con intereses suspendidos o provisionados — Situación en que el deudor cuenta con cualquier obligación significativa respecto de la cual se haya suspendido el devengamiento de intereses, o los intereses se encuentren totalmente provisionados.
  - `e4` Condicion: Baja contable o previsión por desmejora crediticia — Situación en que se ha dado de baja contablemente una obligación o se ha constituido una previsión específica frente a una desmejora significativa en la calidad crediticia del deudor con posterioridad
  - `e5` Condicion: Venta de crédito con pérdida significativa — Situación en que se ha vendido un crédito con una pérdida significativa con motivo de su situación crediticia.
  - `e6` Condicion: Reestructuración de obligación crediticia — Situación en que se ha acordado una reestructuración de una obligación crediticia que puede resultar en una reducción de la deuda como consecuencia de quitas, diferimientos del pago del capital o de l
  - `e7` Condicion: Solicitud de quiebra del deudor — Situación en que se ha solicitado la quiebra del deudor u otra medida similar que produzca el diferimiento o impida el recupero del crédito por parte de la entidad.
  - `e8` Condicion: Solicitud de concurso preventivo o quiebra por el deudor — Situación en que el deudor ha solicitado su concurso preventivo o quiebra u otra medida similar que produzca el diferimiento o impida el recupero del crédito por parte de la entidad.
  - `e9` Condicion: Recupero improbable sin ejecución de garantías — Situación en que la entidad financiera considera que es improbable que pueda recuperar el total de las acreencias del deudor sin recurrir a la ejecución de las garantías u otras medidas en defensa de 
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso C10** Condicion `e8`: Solicitud de concurso preventivo o quiebra por el deudor | descripcion: Situación en que el deudor ha solicitado su concurso preventivo o quiebra u otra medida similar que produzca el diferimiento o impida el recupero del crédito por parte de la entidad. | tramo: El deudor ha solicitado su concurso preventivo o quiebra u otra medida similar que produzca el diferimiento o impida el recupero del crédito por parte de la entidad

## Unidad `ext::2.7.3` (item)
- herencia: **[abre la lista]** [intro 2.7] En adición a las excepciones enunciadas precedentemente, tampoco resultará exigible la
liquidación en el mercado de cambios de los fondos en moneda extranjera que reciban los
residentes por las operaciones previstas en los puntos 2.1. a 2.5., en la medida que se cumpla
la totalidad de las siguientes condiciones: | [cierre 2.7] A los efectos del registro de estas operaciones se deberán confeccionar dos boletos sin
movimiento de pesos, por los conceptos de compra y venta que correspondan, computándose
el monto por el cual se utiliza este mecanismo a los efectos de los límites mensuales que
pudieran ser aplicables según el caso.
En todos los casos se deberá contar con una declaración jurada del cliente en la que deja
constancia de tener conocimiento de que los fondos que se aplican bajo esta modalidad serán
computados a 
- texto propio: 2.7.3. Los fondos en moneda extranjera sean aplicados de manera simultánea con el
ejercicio de la excepción a operaciones por las cuales la normativa cambiaria vigente
permite el acceso al mercado de cambios contra moneda local, considerando los
límites previstos para cada concepto involucrado.
- entidades de la unidad:
  - `c1` Condicion: Aplicación simultánea de fondos con ejercicio de excepción — Los fondos en moneda extranjera deben ser aplicados de manera simultánea con el ejercicio de la excepción a operaciones por las cuales la normativa cambiaria vigente permite el acceso al mercado de ca
  - `c2` Condicion: Respeto de límites previstos para cada concepto — Deben considerarse los límites previstos para cada concepto involucrado en la operación.
- relaciones del crudo (sin establecida_en ni de sujeto): c1 condicion_de c2
- NODOS A CLASIFICAR:
  - **caso C11** Condicion `c2`: Respeto de límites previstos para cada concepto | descripcion: Deben considerarse los límites previstos para cada concepto involucrado en la operación. | tramo: considerando los límites previstos para cada concepto involucrado

## Unidad `ext::9.3.10.4` (item)
- herencia: [intro 9.3] A solicitud del exportador, la entidad encargada del seguimiento emitirá las certificaciones de
aplicación en la medida que se verifiquen las condiciones previstas en los puntos 9.3.1. al
9.3.13.
La entidad deberá dejar registradas las certificaciones de aplicación emitidas para cada una
de las operaciones bajo su seguimiento. | **[abre la lista]** [intro 9.3.10] controlantes de entidades financieras locales admitidas en los puntos 7.9. o 7.10.
La entidad podrá emitir la certificación de aplicación en la medida que la entidad
cuenta con la documentación que le permita verificar:
- texto propio: 9.3.10.4. el pasivo en pesos con el exterior generado a partir de la fecha de la no
aceptación del aporte irrevocable o de la reducción de capital según
corresponda. Se encuentra declarado en la última presentación vencida del
“Relevamiento de activos y pasivos externos”, en caso de corresponder;
- entidades de la unidad:
  - `c1` Condicion: Pasivo en pesos con exterior desde no aceptación o reducción — El pasivo en pesos con el exterior debe haber sido generado a partir de la fecha de la no aceptación del aporte irrevocable o de la reducción de capital, según corresponda.
  - `c2` Condicion: Declaración en Relevamiento de activos y pasivos externos — El pasivo debe encontrarse declarado en la última presentación vencida del Relevamiento de activos y pasivos externos, en caso de corresponder.
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso C12** Condicion `c1`: Pasivo en pesos con exterior desde no aceptación o reducción | descripcion: El pasivo en pesos con el exterior debe haber sido generado a partir de la fecha de la no aceptación del aporte irrevocable o de la reducción de capital, según corresponda. | tramo: el pasivo en pesos con el exterior generado a partir de la fecha de la no aceptación del aporte irrevocable o de la reducción de capital según corresponda

## Unidad `ext::4.5.3` (item)
- herencia: **[abre la lista]** [intro 4.5] prestados o devengados hasta el 12/12/23.
Los importadores de servicios podrán suscribir Bonos para la Reconstrucción de una
Argentina Libre (BOPREAL) por hasta el monto de la deuda pendiente de pago por sus
importaciones de servicios en las que la prestación o devengamiento del servicio por parte del
no residente haya tenido lugar hasta el 12/12/23.
La entidad que concrete la oferta de suscripción en nombre del cliente deberá contar con la
documentación que permite avalar la existencia del serv | [cierre 4.5] Adicionalmente, la mencionada entidad deberá realizar un boleto de venta de cambio a
nombre del importador por el código de concepto "S33. Registro de importaciones de servicios
por adjudicación de bonos BOPREAL"; consignando el valor nominal en moneda extranjera de
bonos BOPREAL adjudicado al importador.
- texto propio: 4.5.3. el cliente cumple los requisitos complementarios previstos en los puntos 3.16.1. a
3.16.4. El punto 3.16.3. sólo será aplicable para clientes que no sean personas
humanas residentes.
- entidades de la unidad:
  - `c1` Condicion: Cumplimiento requisitos complementarios 3.16.1 a 3.16.4 — El cliente debe cumplir los requisitos complementarios establecidos en los puntos 3.16.1 a 3.16.4
  - `e1` Excepcion: Excepción punto 3.16.3 para personas humanas residentes — El punto 3.16.3 no aplica a clientes que sean personas humanas residentes
- relaciones del crudo (sin establecida_en ni de sujeto): c1 condicion_de e1
- NODOS A CLASIFICAR:
  - **caso C13** Excepcion `e1`: Excepción punto 3.16.3 para personas humanas residentes | descripcion: El punto 3.16.3 no aplica a clientes que sean personas humanas residentes | tramo: El punto 3.16.3. sólo será aplicable para clientes que no sean personas humanas residentes

## Unidad `ext::7.8.2::intro` (intro)
- herencia: [encabezado 7.8.2] 7.8.2. Exportaciones bajo los regímenes de precios revisables o concentrado de minerales.
- texto propio: En los casos de exportaciones de productos que se comercializan sobre la base de
precios FOB sujetos a una determinación posterior al momento de registro de la
operación (Exportación de mercaderías con precios revisables – Resolución General
4073-E/17 de la Administración Federal de Ingresos Públicos) o al amparo del
Régimen de Concentrados de Minerales (Resolución General 2108/06 de la
Administración Federal de Ingresos Públicos) será aplicable lo siguiente:
- entidades de la unidad:
  - `c1` Condicion: Exportación con precios FOB revisables — Exportación de mercaderías con precios revisables, conforme a la Resolución General 4073-E/17 de la Administración Federal de Ingresos Públicos
  - `c2` Condicion: Exportación bajo Régimen de Concentrados de Minerales — Exportación de minerales bajo el Régimen de Concentrados de Minerales conforme a la Resolución General 2108/06 de la Administración Federal de Ingresos Públicos
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso C14** Condicion `c2`: Exportación bajo Régimen de Concentrados de Minerales | descripcion: Exportación de minerales bajo el Régimen de Concentrados de Minerales conforme a la Resolución General 2108/06 de la Administración Federal de Ingresos Públicos | tramo: al amparo del Régimen de Concentrados de Minerales (Resolución General 2108/06 de la Administración Federal de Ingresos Públicos)

## Unidad `ext::3.5.6.3` (item)
- herencia: [chapeau_seccion S3] Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas
en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–,
adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán
cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables. | [intro 3.5] exterior.
Las entidades podrán dar acceso al mercado de cambios para realizar pagos de capital o
intereses de títulos de deuda con registro público en el exterior, otros endeudamientos
financieros con el exterior y títulos de deuda con registro público en el país denominados en
moneda extranjera íntegramente suscriptos en el exterior, en la medida que se verifiquen las
siguientes condiciones: | **[abre la lista]** [intro 3.5.6] para la cancelación de capital e intereses de endeudamientos financieros
comprendidos en este punto 3.5. cuando el acreedor sea una contraparte vinculada al
deudor.
Este requisito no resultará aplicable cuando la operación encuadre en alguna de las
siguientes situaciones: | [cierre 3.5.6] Las deudas comprendidas en este punto continuarán sujetas a la conformidad previa
aun cuando existiese una modificación del acreedor o del deudor que conlleve a que
ya no exista una vinculación entre el acreedor y el deudor residente.
- texto propio: 3.5.6.3. se trate de un endeudamiento financiero comprendido en este punto 3.5. que
tenga una vida promedio no inferior a los 2 (dos) años y los fondos hayan
sido ingresados y liquidados por el mercado de cambios entre el 02/10/20 y
el 20/04/25.
- entidades de la unidad:
  - `c1` Condicion: Vida promedio mínima 2 años — El endeudamiento financiero debe tener una vida promedio no inferior a 2 años
  - `c2` Condicion: Fondos ingresados y liquidados entre 02/10/20 y 20/04/25 — Los fondos del endeudamiento deben haber sido ingresados y liquidados por el mercado de cambios en el período comprendido entre el 2 de octubre de 2020 y el 20 de abril de 2025
  - `e1` Excepcion: Excepción conformidad previa BCRA — endeudamiento con vida promedio ≥2 años — No resultará aplicable el requisito de conformidad previa del BCRA cuando se trate de un endeudamiento financiero comprendido en el punto 3.5. que tenga una vida promedio no inferior a 2 años y los fo
- relaciones del crudo (sin establecida_en ni de sujeto): c1 condicion_de e1; c2 condicion_de e1
- NODOS A CLASIFICAR:
  - **caso C15** Excepcion `e1`: Excepción conformidad previa BCRA — endeudamiento con vida promedio ≥2 años | descripcion: No resultará aplicable el requisito de conformidad previa del BCRA cuando se trate de un endeudamiento financiero comprendido en el punto 3.5. que tenga una vida promedio no inferior a 2 años y los fondos hayan sido ingresados y liquidados por el mercado de cambios entre el 02/10/20 y el 20/04/25 | tramo: se trate de un endeudamiento financiero comprendido en este punto 3.5. que tenga una vida promedio no inferior a los 2 (dos) años y los fondos hayan sido ingresados y liquidados por el mercado de cambios entre el 02/10/20 y el 20/04/25

## Unidad `cap::2.10` (punto_no_item)
- herencia: [chapeau_seccion S2] A los efectos de la aplicación de las disposiciones de la presente sección, las entidades financieras
se clasificarán en:
i)Grupo 1: entidades calificadas por el BCRA como de importancia sistémica a nivel local | [chapeau_seccion S2] (D-SIB) y sucursales o subsidiarias de bancos del exterior calificados como de impor-
tancia sistémica global (G-SIB). | [chapeau_seccion S2] ii) Grupo 2: entidades financieras no comprendidas en el acápite i).
En aquellos casos en que no se establezcan disposiciones específicas para cada uno de los citados
grupos de entidades financieras, deberá aplicarse el mismo tratamiento a ambos grupos.
Las entidades financieras que presenten cambios en su calificación –conforme a lo previsto en los
acápites precedentes–, contarán con un plazo de 6 meses para aplicar las disposiciones específicas
correspondientes al nuevo grupo al que pertenezca
- texto propio: 2.10. Exposiciones en situación de incumplimiento.
Comprende a todas aquellas exposiciones a un deudor respecto del que se verifique alguna
de las siguientes situaciones:
i) El deudor posee un crédito en mora de más de 90 días. Se considera que un descubierto
en cuenta corriente se encuentra en mora a partir del momento en que el deudor excede
el límite autorizado o se le comunica un nuevo límite y éste es inferior a su saldo deudor.
ii) El deudor cuenta con cualquier obligación significativa respecto de la cual se haya sus-
pendido el devengamiento de intereses, o los intereses se encuentren totalmente previ-
sionados.
iii) Se ha dado de baja contablemente una obligación o se ha constituido una previsión es-
pecífica frente a una desmejora significativa en la calidad crediticia del deudor con poste-
rioridad al otorgamiento del crédito.
iv) Se ha vendido un crédito con una pérdida significativa con motivo de su situación crediti-
cia.
v) Se ha acordado una reestructuración de una obligación crediticia que puede resultar en
una reducción de la deuda como consecuencia de quitas, diferimientos del pago del capi-
tal o de los intereses o una disminución de las comisiones aplicables.
vi) Se ha solicitado la quiebra del deudor u otra medida similar que produzca el diferimiento
o impida el recupero del crédito por parte de la entidad.
vii) El deudor ha solicitado su concurso preventivo o quiebra u otra medida similar que pro-
duzca el diferimiento o impida el recupero del crédito por parte de la entidad.
viii) La entidad financiera considera que es improbable que pueda recuperar el total de las
acreencias del deudor sin recurrir a la ejecución de las garantías u otras medidas en de-
fensa de su crédito.
- entidades de la unidad:
  - `e1` Definicion: Exposiciones en situación de incumplimiento — Todas aquellas exposiciones a un deudor respecto del que se verifique alguna de las siguientes situaciones: (i) El deudor posee un crédito en mora de más de 90 días; (ii) El deudor cuenta con cualquie
  - `e2` Condicion: Crédito en mora de más de 90 días — Situación en que el deudor posee un crédito en mora de más de 90 días. Se considera que un descubierto en cuenta corriente se encuentra en mora a partir del momento en que el deudor excede el límite a
  - `e3` Condicion: Obligación significativa con intereses suspendidos o provisionados — Situación en que el deudor cuenta con cualquier obligación significativa respecto de la cual se haya suspendido el devengamiento de intereses, o los intereses se encuentren totalmente provisionados.
  - `e4` Condicion: Baja contable o previsión por desmejora crediticia — Situación en que se ha dado de baja contablemente una obligación o se ha constituido una previsión específica frente a una desmejora significativa en la calidad crediticia del deudor con posterioridad
  - `e5` Condicion: Venta de crédito con pérdida significativa — Situación en que se ha vendido un crédito con una pérdida significativa con motivo de su situación crediticia.
  - `e6` Condicion: Reestructuración de obligación crediticia — Situación en que se ha acordado una reestructuración de una obligación crediticia que puede resultar en una reducción de la deuda como consecuencia de quitas, diferimientos del pago del capital o de l
  - `e7` Condicion: Solicitud de quiebra del deudor — Situación en que se ha solicitado la quiebra del deudor u otra medida similar que produzca el diferimiento o impida el recupero del crédito por parte de la entidad.
  - `e8` Condicion: Solicitud de concurso preventivo o quiebra por el deudor — Situación en que el deudor ha solicitado su concurso preventivo o quiebra u otra medida similar que produzca el diferimiento o impida el recupero del crédito por parte de la entidad.
  - `e9` Condicion: Recupero improbable sin ejecución de garantías — Situación en que la entidad financiera considera que es improbable que pueda recuperar el total de las acreencias del deudor sin recurrir a la ejecución de las garantías u otras medidas en defensa de 
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso C16** Condicion `e9`: Recupero improbable sin ejecución de garantías | descripcion: Situación en que la entidad financiera considera que es improbable que pueda recuperar el total de las acreencias del deudor sin recurrir a la ejecución de las garantías u otras medidas en defensa de su crédito. | tramo: La entidad financiera considera que es improbable que pueda recuperar el total de las acreencias del deudor sin recurrir a la ejecución de las garantías u otras medidas en defensa de su crédito

## Unidad `cla::6.5.5.4` (item)
- herencia: [intro 6.5] Cada cliente, y la totalidad de sus financiaciones comprendidas, se incluirá en una de las si-
guientes cinco categorías, las que se definen teniendo en cuenta las condiciones que se deta-
llan en cada caso.
Los clientes que no registren asistencia crediticia de la entidad y que posteriormente reciban fi-
nanciaciones de ésta que no superen el importe resultante de aplicar sobre el saldo de deuda
registrado en el sistema financiero, según la última información disponible en la “Central de
deudor | **[abre la lista]** [intro 6.5.5] Las deudas de clientes incorporados a esta categoría se consideran incobrables. Si bien
estos activos podrían tener algún valor de recuperación bajo un cierto conjunto de cir-
cunstancias futuras, su incobrabilidad es evidente al momento del análisis.
Entre los indicadores que pueden reflejar esta situación se destacan que el cliente: | [cierre 6.5.5] Además, corresponderá clasificar en esta categoría a los clientes que, cualquiera sea el
motivo (entre ellos por no contar con legajo o por no haber proporcionado información
confiable y/o actualizada), no hayan sido evaluados con la periodicidad correspondiente,
con excepción de los deudores en concurso o con acuerdo preventivo extrajudicial solici-
tado o en gestión judicial que, por un período de hasta 540 días contados a partir de la
apertura del concurso, solicitud del acuerdo preventivo o 
- texto propio: 6.5.5.4. Tenga un sistema de información inadecuado, lo que impide conocer con exacti-
tud la real situación financiera y económica de la empresa. La información que
se presenta no es confiable pues no cuenta con la adecuada documentación
respaldatoria. En general, la información no es consistente y no está actualizada.
- entidades de la unidad:
  - `e1` Condicion: Sistema de información inadecuado — El cliente tiene un sistema de información inadecuado que impide conocer con exactitud su real situación financiera y económica
  - `e2` Condicion: Información no confiable sin documentación — La información presentada no es confiable porque carece de documentación respaldatoria adecuada
  - `e3` Condicion: Información inconsistente y desactualizada — La información no es consistente y no está actualizada
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso C17** Condicion `e2`: Información no confiable sin documentación | descripcion: La información presentada no es confiable porque carece de documentación respaldatoria adecuada | tramo: La información que se presenta no es confiable pues no cuenta con la adecuada documentación respaldatoria

## Unidad `ext::2.6.1.2` (item)
- herencia: [intro 2.6] beneficiarios del “Régimen de fomento para las exportaciones de la economía
del conocimiento”. | **[abre la lista]** [intro 2.6.1] de Promoción de la Economía del Conocimiento y que sean beneficiarios de lo
dispuesto en el Capítulo II del Decreto 679/22 quedarán exceptuados de la obligación
de liquidación de los cobros de exportaciones de bienes y servicios que correspondan
a actividades de la economía del conocimiento, en la medida que se cumpla la
totalidad de las siguientes condiciones: | [cierre 2.6.1] Los montos de las divisas a ser afectadas en el marco de lo dispuesto en el Capítulo II
del Decreto 679/22 no pueden resultar alcanzadas por ningún otro tratamiento
cambiario diferencial que no sea aquel previsto en dicho capítulo.
- texto propio: 2.6.1.2. cuenten con una “Certificación de incremento de exportaciones asociadas a
la economía del conocimiento (Decreto 679/22)” en los términos previstos en
el punto 2.6.2.;
- entidades de la unidad:
  - `e1` Excepcion: Excepción liquidación cobros exportaciones economía conocimiento — Las personas jurídicas inscriptas en el Registro Nacional de Beneficiarios del Régimen de Promoción de la Economía del Conocimiento y que sean beneficiarios de lo dispuesto en el Capítulo II del Decre
  - `c1` Condicion: Condición: certificación incremento exportaciones economía conocimiento — Contar con una Certificación de incremento de exportaciones asociadas a la economía del conocimiento (Decreto 679/22) en los términos previstos en el punto 2.6.2.
  - `c2` Condicion: Condición: montos divisas no alcanzados por otro tratamiento cambiario — Los montos de las divisas a ser afectadas en el marco de lo dispuesto en el Capítulo II del Decreto 679/22 no pueden resultar alcanzadas por ningún otro tratamiento cambiario diferencial que no sea aq
  - `d1` Definicion: Sujeto alcanzado: personas jurídicas inscriptas Registro Nacional Beneficiarios — Las personas jurídicas inscriptas en el Registro Nacional de Beneficiarios del Régimen de Promoción de la Economía del Conocimiento y que sean beneficiarios de lo dispuesto en el Capítulo II del Decre
- relaciones del crudo (sin establecida_en ni de sujeto): c1 condicion_de e1; c2 condicion_de e1
- NODOS A CLASIFICAR:
  - **caso C18** Excepcion `e1`: Excepción liquidación cobros exportaciones economía conocimiento | descripcion: Las personas jurídicas inscriptas en el Registro Nacional de Beneficiarios del Régimen de Promoción de la Economía del Conocimiento y que sean beneficiarios de lo dispuesto en el Capítulo II del Decreto 679/22 quedan exceptuadas de la obligación de liquidación de los cobros de exportaciones de bienes y servicios que correspondan a actividades de la economía del conocimiento. | tramo: quedarán exceptuados de la obligación de liquidación de los cobros de exportaciones de bienes y servicios que correspondan a actividades de la economía del conocimiento

## Unidad `ext::3.18.2.6` (item)
- herencia: [chapeau_seccion S3] Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas
en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–,
adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán
cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables. | **[abre la lista]** [intro 3.18.2] exportador deberá nominar una única entidad financiera local que será la
responsable de emitir las correspondientes certificaciones y remitirlas a las entidades
por las cuales el cliente desee acceder al mercado.
La entidad nominada podrá emitir una “Certificación de aumento de las exportaciones
de bienes en el año t” cuando se verifiquen la totalidad de los siguientes requisitos:
- texto propio: 3.18.2.6. La entidad cuenta con una declaración jurada del exportador en la que deje
constancia de que, en caso de haber sido convocados tanto él como su
grupo económico a un acuerdo de precios por el Gobierno Nacional, no
han rechazado participar en tales acuerdos ni han incumplido lo acordado
en caso de poseer un programa vigente.
- entidades de la unidad:
  - `c1` Condicion: Declaración jurada del exportador — El exportador debe presentar una declaración jurada en la que conste que, si fue convocado junto con su grupo económico a un acuerdo de precios por el Gobierno Nacional, no rechazó participar ni incum
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso C19** Condicion `c1`: Declaración jurada del exportador | descripcion: El exportador debe presentar una declaración jurada en la que conste que, si fue convocado junto con su grupo económico a un acuerdo de precios por el Gobierno Nacional, no rechazó participar ni incumplió lo acordado si poseía un programa vigente | tramo: La entidad cuenta con una declaración jurada del exportador en la que deje constancia de que, en caso de haber sido convocados tanto él como su grupo económico a un acuerdo de precios por el Gobierno Nacional, no han rechazado participar en tales acuerdos ni han incumplido lo acordado en caso de poseer un programa vigente

## Unidad `ext::3.18.2.2` (item)
- herencia: [chapeau_seccion S3] Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas
en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–,
adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán
cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables. | **[abre la lista]** [intro 3.18.2] exportador deberá nominar una única entidad financiera local que será la
responsable de emitir las correspondientes certificaciones y remitirlas a las entidades
por las cuales el cliente desee acceder al mercado.
La entidad nominada podrá emitir una “Certificación de aumento de las exportaciones
de bienes en el año t” cuando se verifiquen la totalidad de los siguientes requisitos:
- texto propio: 3.18.2.2. El exportador no registra a la fecha de emisión permisos con plazo vencido
para el ingreso y liquidación de las divisas en situación de incumplimiento.
Los permisos que revistan la condición de “incumplido en gestión de cobro”
no serán considerados a estos efectos.
- entidades de la unidad:
  - `e1` Condicion: Exportador sin permisos vencidos a emisión — El exportador no registra a la fecha de emisión permisos con plazo vencido para el ingreso y liquidación de las divisas en situación de incumplimiento
  - `e2` Excepcion: Excepción permisos incumplidos en gestión de cobro — Los permisos que revistan la condición de 'incumplido en gestión de cobro' no serán considerados para la verificación del requisito de ausencia de permisos con plazo vencido
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso C20** Excepcion `e2`: Excepción permisos incumplidos en gestión de cobro | descripcion: Los permisos que revistan la condición de 'incumplido en gestión de cobro' no serán considerados para la verificación del requisito de ausencia de permisos con plazo vencido | tramo: Los permisos que revistan la condición de "incumplido en gestión de cobro" no serán considerados a estos efectos

## Unidad `ctacte::6.4.6.4` (item)
- herencia: **[abre la lista]** [encabezado 6.4.6] 6.4.6. No corresponderá la comunicación al BCRA de los rechazos motivados por:
- texto propio: 6.4.6.4. Haberse dispuesto medidas cautelares sobre los fondos destinados para el pago
del cheque, en tanto dicha circunstancia haya sido desconocida por el librador
en oportunidad de su emisión, lo que deberá ser suficientemente acreditado por
éste, a satisfacción de la entidad girada.
- entidades de la unidad:
  - `e1` Excepcion: Excepción medidas cautelares sobre fondos — No corresponde comunicar al BCRA los rechazos motivados por medidas cautelares sobre fondos destinados al pago del cheque, cuando esa circunstancia fue desconocida por el librador al momento de la emi
  - `e2` Condicion: Condición acreditación suficiente por librador — La circunstancia de desconocimiento debe ser suficientemente acreditada por el librador, a satisfacción de la entidad girada
- relaciones del crudo (sin establecida_en ni de sujeto): e2 condicion_de e1
- NODOS A CLASIFICAR:
  - **caso C21** Excepcion `e1`: Excepción medidas cautelares sobre fondos | descripcion: No corresponde comunicar al BCRA los rechazos motivados por medidas cautelares sobre fondos destinados al pago del cheque, cuando esa circunstancia fue desconocida por el librador al momento de la emisión | tramo: No corresponderá la comunicación al BCRA de los rechazos motivados por: Haberse dispuesto medidas cautelares sobre los fondos destinados para el pago del cheque, en tanto dicha circunstancia haya sido desconocida por el librador en oportunidad de su emisión

## Unidad `ext::6.7` (item)
- herencia: **[abre la lista]** [chapeau_seccion S6] En el marco de estas disposiciones se definen los siguientes conceptos:
- texto propio: 6.7. Posición general de cambios (PGC).
Comprenderá la totalidad de los activos externos líquidos de la entidad, netos de los saldos
deudores de corresponsalía originados en la operatoria del mercado de cambios. También
quedarán comprendidas las compras y ventas concertadas en el mercado de cambios y que
se encuentran pendientes de liquidación.
Serán considerados activos externos líquidos de la entidad, entre otros: monedas y billetes en
moneda extranjera, disponibilidades en oro amonedado o en barras de buena entrega, saldos
acreedores de corresponsalía (incluyendo las transferencias a favor de terceros sin liquidación
concertada), otros depósitos a la vista en entidades financieras del exterior, inversiones en
títulos públicos externos y certificados de depósito a plazo.
No formarán parte de la PGC: inversiones directas en el exterior, activos externos de terceros
en custodia, ventas y compras a término de divisas o valores externos, depósitos en el BCRA
en moneda extranjera en cuentas a nombre de la entidad y demás activos locales en moneda
extranjera.
- entidades de la unidad:
  - `e1` Definicion: PGC — activos externos líquidos netos — La totalidad de los activos externos líquidos de la entidad, netos de los saldos deudores de corresponsalía originados en la operatoria del mercado de cambios.
  - `e2` Definicion: PGC — compras y ventas concertadas pendientes — Incluye las compras y ventas concertadas en el mercado de cambios que se encuentran pendientes de liquidación.
  - `e3` Definicion: Activos externos líquidos — componentes — Monedas y billetes en moneda extranjera, disponibilidades en oro amonedado o en barras de buena entrega, saldos acreedores de corresponsalía (incluyendo las transferencias a favor de terceros sin liqu
  - `e4` Excepcion: Exclusiones de PGC — inversiones directas — Las inversiones directas en el exterior no forman parte de la Posición general de cambios.
  - `e5` Excepcion: Exclusiones de PGC — activos en custodia — Los activos externos de terceros en custodia no forman parte de la Posición general de cambios.
  - `e6` Excepcion: Exclusiones de PGC — ventas y compras a término — Las ventas y compras a término de divisas o valores externos no forman parte de la Posición general de cambios.
  - `e7` Excepcion: Exclusiones de PGC — depósitos BCRA moneda extranjera — Los depósitos en el BCRA en moneda extranjera en cuentas a nombre de la entidad no forman parte de la Posición general de cambios.
  - `e8` Excepcion: Exclusiones de PGC — activos locales moneda extranjera — Los demás activos locales en moneda extranjera no forman parte de la Posición general de cambios.
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso C22** Excepcion `e4`: Exclusiones de PGC — inversiones directas | descripcion: Las inversiones directas en el exterior no forman parte de la Posición general de cambios. | tramo: No formarán parte de la PGC: inversiones directas en el exterior

## Unidad `cla::2.2.1.4` (item)
- herencia: **[abre la lista]** [encabezado 2.2.1] 2.2.1. Los siguientes conceptos por intermediación financiera:
- texto propio: 2.2.1.4. Anticipos por pago de jubilaciones y pensiones.
- entidades de la unidad:
  - `e1` Excepcion: Exclusión — Anticipos por pago de jubilaciones y pensiones — Quedan exceptuados de la clasificación de deudores los anticipos por pago de jubilaciones y pensiones, como concepto de intermediación financiera.
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso C23** Excepcion `e1`: Exclusión — Anticipos por pago de jubilaciones y pensiones | descripcion: Quedan exceptuados de la clasificación de deudores los anticipos por pago de jubilaciones y pensiones, como concepto de intermediación financiera. | tramo: Anticipos por pago de jubilaciones y pensiones

## Unidad `cla::6.5.1.1` (item)
- herencia: [intro 6.5] Cada cliente, y la totalidad de sus financiaciones comprendidas, se incluirá en una de las si-
guientes cinco categorías, las que se definen teniendo en cuenta las condiciones que se deta-
llan en cada caso.
Los clientes que no registren asistencia crediticia de la entidad y que posteriormente reciban fi-
nanciaciones de ésta que no superen el importe resultante de aplicar sobre el saldo de deuda
registrado en el sistema financiero, según la última información disponible en la “Central de
deudor | **[abre la lista]** [intro 6.5.1] El análisis del flujo de fondos del cliente demuestra que es capaz de atender adecuada-
mente todos sus compromisos financieros.
Entre los indicadores que pueden reflejar esta situación se destacan que el cliente:
- texto propio: 6.5.1.1. presente una situación financiera líquida, con bajo nivel y adecuada estructura
de endeudamiento en relación con su capacidad de ganancia, y muestre una al-
ta capacidad de pago de las deudas (capital e intereses) en las condiciones pac-
tadas generando fondos -medido a través del análisis de su flujo- en grado acep-
table. El flujo de fondos no es susceptible de variaciones significativas ante mo-
dificaciones importantes en el comportamiento de las variables tanto propias
como vinculadas a su sector de actividad.
En el análisis que se lleve a cabo deberá tenerse en cuenta, de corresponder, la
eventual incidencia que en su capacidad de pago pueda tener la situación en la
que se encuentran los demás integrantes del grupo de contrapartes conectadas
al cual pertenece.
- entidades de la unidad:
  - `e1` Definicion: Situación normal — indicador de flujo de fondos — El cliente presenta una situación financiera líquida, con bajo nivel y adecuada estructura de endeudamiento en relación con su capacidad de ganancia, y muestra una alta capacidad de pago de las deudas
  - `e2` Condicion: Estabilidad del flujo ante variaciones de variables — El flujo de fondos no es susceptible de variaciones significativas ante modificaciones importantes en el comportamiento de las variables tanto propias como vinculadas a su sector de actividad.
  - `e3` Condicion: Incidencia de situación de contrapartes conectadas — En el análisis debe considerarse, de corresponder, la eventual incidencia que en la capacidad de pago del cliente pueda tener la situación en la que se encuentran los demás integrantes del grupo de co
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso C24** Condicion `e3`: Incidencia de situación de contrapartes conectadas | descripcion: En el análisis debe considerarse, de corresponder, la eventual incidencia que en la capacidad de pago del cliente pueda tener la situación en la que se encuentran los demás integrantes del grupo de contrapartes conectadas al cual pertenece. | tramo: En el análisis que se lleve a cabo deberá tenerse en cuenta, de corresponder, la eventual incidencia que en su capacidad de pago pueda tener la situación en la que se encuentran los demás integrantes del grupo de contrapartes conectadas al cual pertenece

## Unidad `cap::2.10` (punto_no_item)
- herencia: [chapeau_seccion S2] A los efectos de la aplicación de las disposiciones de la presente sección, las entidades financieras
se clasificarán en:
i)Grupo 1: entidades calificadas por el BCRA como de importancia sistémica a nivel local | [chapeau_seccion S2] (D-SIB) y sucursales o subsidiarias de bancos del exterior calificados como de impor-
tancia sistémica global (G-SIB). | [chapeau_seccion S2] ii) Grupo 2: entidades financieras no comprendidas en el acápite i).
En aquellos casos en que no se establezcan disposiciones específicas para cada uno de los citados
grupos de entidades financieras, deberá aplicarse el mismo tratamiento a ambos grupos.
Las entidades financieras que presenten cambios en su calificación –conforme a lo previsto en los
acápites precedentes–, contarán con un plazo de 6 meses para aplicar las disposiciones específicas
correspondientes al nuevo grupo al que pertenezca
- texto propio: 2.10. Exposiciones en situación de incumplimiento.
Comprende a todas aquellas exposiciones a un deudor respecto del que se verifique alguna
de las siguientes situaciones:
i) El deudor posee un crédito en mora de más de 90 días. Se considera que un descubierto
en cuenta corriente se encuentra en mora a partir del momento en que el deudor excede
el límite autorizado o se le comunica un nuevo límite y éste es inferior a su saldo deudor.
ii) El deudor cuenta con cualquier obligación significativa respecto de la cual se haya sus-
pendido el devengamiento de intereses, o los intereses se encuentren totalmente previ-
sionados.
iii) Se ha dado de baja contablemente una obligación o se ha constituido una previsión es-
pecífica frente a una desmejora significativa en la calidad crediticia del deudor con poste-
rioridad al otorgamiento del crédito.
iv) Se ha vendido un crédito con una pérdida significativa con motivo de su situación crediti-
cia.
v) Se ha acordado una reestructuración de una obligación crediticia que puede resultar en
una reducción de la deuda como consecuencia de quitas, diferimientos del pago del capi-
tal o de los intereses o una disminución de las comisiones aplicables.
vi) Se ha solicitado la quiebra del deudor u otra medida similar que produzca el diferimiento
o impida el recupero del crédito por parte de la entidad.
vii) El deudor ha solicitado su concurso preventivo o quiebra u otra medida similar que pro-
duzca el diferimiento o impida el recupero del crédito por parte de la entidad.
viii) La entidad financiera considera que es improbable que pueda recuperar el total de las
acreencias del deudor sin recurrir a la ejecución de las garantías u otras medidas en de-
fensa de su crédito.
- entidades de la unidad:
  - `e1` Definicion: Exposiciones en situación de incumplimiento — Todas aquellas exposiciones a un deudor respecto del que se verifique alguna de las siguientes situaciones: (i) El deudor posee un crédito en mora de más de 90 días; (ii) El deudor cuenta con cualquie
  - `e2` Condicion: Crédito en mora de más de 90 días — Situación en que el deudor posee un crédito en mora de más de 90 días. Se considera que un descubierto en cuenta corriente se encuentra en mora a partir del momento en que el deudor excede el límite a
  - `e3` Condicion: Obligación significativa con intereses suspendidos o provisionados — Situación en que el deudor cuenta con cualquier obligación significativa respecto de la cual se haya suspendido el devengamiento de intereses, o los intereses se encuentren totalmente provisionados.
  - `e4` Condicion: Baja contable o previsión por desmejora crediticia — Situación en que se ha dado de baja contablemente una obligación o se ha constituido una previsión específica frente a una desmejora significativa en la calidad crediticia del deudor con posterioridad
  - `e5` Condicion: Venta de crédito con pérdida significativa — Situación en que se ha vendido un crédito con una pérdida significativa con motivo de su situación crediticia.
  - `e6` Condicion: Reestructuración de obligación crediticia — Situación en que se ha acordado una reestructuración de una obligación crediticia que puede resultar en una reducción de la deuda como consecuencia de quitas, diferimientos del pago del capital o de l
  - `e7` Condicion: Solicitud de quiebra del deudor — Situación en que se ha solicitado la quiebra del deudor u otra medida similar que produzca el diferimiento o impida el recupero del crédito por parte de la entidad.
  - `e8` Condicion: Solicitud de concurso preventivo o quiebra por el deudor — Situación en que el deudor ha solicitado su concurso preventivo o quiebra u otra medida similar que produzca el diferimiento o impida el recupero del crédito por parte de la entidad.
  - `e9` Condicion: Recupero improbable sin ejecución de garantías — Situación en que la entidad financiera considera que es improbable que pueda recuperar el total de las acreencias del deudor sin recurrir a la ejecución de las garantías u otras medidas en defensa de 
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso C25** Condicion `e5`: Venta de crédito con pérdida significativa | descripcion: Situación en que se ha vendido un crédito con una pérdida significativa con motivo de su situación crediticia. | tramo: Se ha vendido un crédito con una pérdida significativa con motivo de su situación crediticia

## Unidad `cap::4.3::intro` (intro)
- herencia: [encabezado 4.3] 4.3. Exigencia de capital por riesgo de crédito de contraparte en operaciones con entidades de
- texto propio: contraparte central.
Comprende a aquellas exposiciones de las entidades financieras con entidades de contrapar-
te central (CCP) que se originen en derivados OTC o negociados en mercados de valores y
en operaciones de financiación con títulos valores (“Securities Financing Transactions”, SFT)
y operaciones de liquidación diferida –definidas en el punto 4.2.–.
No están comprendidas las exposiciones originadas en operaciones al contado y que involu-
cren títulos valores, oro o moneda extranjera, cuya exigencia de capital se calculará conforme
a lo previsto en el punto 4.1.
- entidades de la unidad:
  - `e1` Definicion: Exposiciones CCP en derivados OTC, mercados de valores y SFT — Aquellas exposiciones de las entidades financieras con entidades de contraparte central (CCP) que se originen en derivados OTC o negociados en mercados de valores y en operaciones de financiación con 
  - `e2` Excepcion: Exclusión operaciones al contado con títulos, oro o moneda extranjera — Quedan excluidas de la exigencia de capital por riesgo de crédito de contraparte las exposiciones originadas en operaciones al contado que involucren títulos valores, oro o moneda extranjera; estas se
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso C26** Excepcion `e2`: Exclusión operaciones al contado con títulos, oro o moneda extranjera | descripcion: Quedan excluidas de la exigencia de capital por riesgo de crédito de contraparte las exposiciones originadas en operaciones al contado que involucren títulos valores, oro o moneda extranjera; estas se rigen por lo previsto en el punto 4.1. | tramo: No están comprendidas las exposiciones originadas en operaciones al contado y que involucren títulos valores, oro o moneda extranjera, cuya exigencia de capital se calculará conforme a lo previsto en el punto 4.1.

## Unidad `ext::11.1.6.1` (item)
- herencia: [intro 11.1] Quedarán comprendidas todas las oficializaciones de importación ocurridas a partir del
01/11/19 y aquellas que sean anteriores por las cuales se solicite realizar pagos a través del
mercado de cambios a partir de la mencionada fecha.
Por cada oficialización del despacho de importación, el importador deberá nominar una
entidad para que se haga responsable del seguimiento de la oficialización. Esta entidad será
la responsable de verificar el cumplimiento de las condiciones estipuladas en la presen | **[abre la lista]** [intro 11.1.6] La entidad encargada del seguimiento de la oficialización del despacho de
importación deberá reportar al BCRA en el marco del SEPAIMPO cuando, a pedido
del importador, ceda su seguimiento a otra entidad de plaza.
A los efectos de poder concretarse la cesión se deberán verificar las siguientes
condiciones:
- texto propio: 11.1.6.1. La entidad cedente no registra certificaciones emitidas y no devueltas
cuyo plazo de vigencia aún no haya vencido.
- entidades de la unidad:
  - `e1` Condicion: Entidad cedente sin certificaciones pendientes — La entidad cedente no debe tener certificaciones emitidas y no devueltas cuyo plazo de vigencia aún no haya vencido
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso C27** Condicion `e1`: Entidad cedente sin certificaciones pendientes | descripcion: La entidad cedente no debe tener certificaciones emitidas y no devueltas cuyo plazo de vigencia aún no haya vencido | tramo: La entidad cedente no registra certificaciones emitidas y no devueltas cuyo plazo de vigencia aún no haya vencido

## Unidad `ext::9.3.1.3` (item)
- herencia: [intro 9.3] A solicitud del exportador, la entidad encargada del seguimiento emitirá las certificaciones de
aplicación en la medida que se verifiquen las condiciones previstas en los puntos 9.3.1. al
9.3.13.
La entidad deberá dejar registradas las certificaciones de aplicación emitidas para cada una
de las operaciones bajo su seguimiento. | **[abre la lista]** [intro 9.3.1] partir del 02/09/19 y prefinanciaciones locales.
La entidad podrá emitir las certificaciones de aplicación de las divisas a la
cancelación del capital e intereses en la medida que se verifiquen las siguientes
condiciones: | [cierre 9.3.1] La entidad también podrá emitir certificaciones de aplicación con imputación a una
operación bajo su seguimiento, en la medida que el exportador demuestre
fehacientemente que las divisas del permiso se utilizaron para cancelar la deuda
original que fue cedida a otro acreedor externo por el acreedor originalmente
declarado, o una renovación de la operación original con el mismo acreedor.
- texto propio: 9.3.1.3. Que el monto de la certificación por una aplicación de intereses u otros
conceptos admitidos sea consistente con los pactados para la operación y
que reflejen condiciones de mercado.
- entidades de la unidad:
  - `c1` Condicion: Consistencia monto certificación con pactado — El monto de la certificación por aplicación de intereses u otros conceptos admitidos debe ser consistente con los montos pactados para la operación.
  - `c2` Condicion: Reflejo de condiciones de mercado — Los montos de la certificación deben reflejar condiciones de mercado.
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso C28** Condicion `c1`: Consistencia monto certificación con pactado | descripcion: El monto de la certificación por aplicación de intereses u otros conceptos admitidos debe ser consistente con los montos pactados para la operación. | tramo: Que el monto de la certificación por una aplicación de intereses u otros conceptos admitidos sea consistente con los pactados para la operación

## Unidad `ext::7.11.2.3` (item)
- herencia: [intro 7.11] de exportaciones de bienes. | **[abre la lista]** [intro 7.11.2] que se verifiquen la totalidad de las siguientes condiciones: | [cierre 7.11.2] La entidad deberá verificar los requisitos habituales a los efectos de certificar la
aplicación de divisas a la cancelación de la financiación.
- texto propio: 7.11.2.3. El importador haya demostrado el registro de ingreso aduanero de los
bienes por un valor equivalente al monto total de la financiación que
pretende ser cancelada con este mecanismo. A los efectos del valor de los
bienes podrá tomarse en todo concepto que forme parte de la condición de
compra pactada registrada en la factura emitida por el proveedor del
exterior.
Si existiesen fondos destinados al pago de fletes de importaciones de
bienes no incluidos en la condición de compra y el importador demostró el
registro de ingreso aduanero de los bienes cuyos fletes se abonaron,
también se podrá computar el valor de los fletes que consten en la
documentación de transporte asociada al registro de ingreso aduanero de
los bienes.
En el caso de operaciones comprendidas en el punto 7.11.1.6. también se
admitirá la cancelación de intereses a partir de la fecha en que se complete
el ingreso de la financiación, sin necesidad de contar en ese momento con
el registro de ingreso aduanero de los bienes.
- entidades de la unidad:
  - `c1` Condicion: Importador demuestra registro ingreso aduanero — El importador debe haber demostrado el registro de ingreso aduanero de los bienes cuyo valor sea equivalente al monto total de la financiación que se pretende cancelar con este mecanismo.
  - `d1` Definicion: Valor de bienes para cálculo de equivalencia — Para determinar el valor de los bienes se puede considerar todo concepto que forme parte de la condición de compra pactada registrada en la factura emitida por el proveedor del exterior.
  - `e1` Excepcion: Excepción — fletes de importaciones no incluidos en condición de compra — Se admite computar el valor de los fletes no incluidos en la condición de compra cuando el importador ha demostrado el registro de ingreso aduanero de los bienes cuyos fletes se abonaron y constan en 
  - `e2` Excepcion: Excepción — cancelación de intereses sin registro aduanero previo — Para operaciones comprendidas en el punto 7.11.1.6, se admite la cancelación de intereses desde la fecha en que se complete el ingreso de la financiación, sin requerir en ese momento el registro de in
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso C29** Excepcion `e2`: Excepción — cancelación de intereses sin registro aduanero previo | descripcion: Para operaciones comprendidas en el punto 7.11.1.6, se admite la cancelación de intereses desde la fecha en que se complete el ingreso de la financiación, sin requerir en ese momento el registro de ingreso aduanero de los bienes. | tramo: En el caso de operaciones comprendidas en el punto 7.11.1.6. también se admitirá la cancelación de intereses a partir de la fecha en que se complete el ingreso de la financiación, sin necesidad de contar en ese momento con el registro de ingreso aduanero de los bienes

## Unidad `cla::6.5.3.8` (item)
- herencia: [intro 6.5] Cada cliente, y la totalidad de sus financiaciones comprendidas, se incluirá en una de las si-
guientes cinco categorías, las que se definen teniendo en cuenta las condiciones que se deta-
llan en cada caso.
Los clientes que no registren asistencia crediticia de la entidad y que posteriormente reciban fi-
nanciaciones de ésta que no superen el importe resultante de aplicar sobre el saldo de deuda
registrado en el sistema financiero, según la última información disponible en la “Central de
deudor | **[abre la lista]** [intro 6.5.3] El análisis del flujo de fondos del cliente demuestra que tiene problemas para atender
normalmente la totalidad de sus compromisos financieros y que, de no ser corregidos,
esos problemas pueden resultar en una pérdida para la entidad financiera.
Entre los indicadores que pueden reflejar esta situación se destacan que el cliente:
- texto propio: 6.5.3.8. Pertenezca a un sector de la actividad económica o ramo de negocios cuya ten-
dencia futura no sea firme, y tenga una perspectiva de disminución de los ingre-
sos y los beneficios, o exista la posibilidad de que se reduzca la demanda de los
productos.
- entidades de la unidad:
  - `e1` Condicion: Sector con tendencia futura no firme — El cliente pertenece a un sector de la actividad económica o ramo de negocios cuya tendencia futura no es firme.
  - `e2` Condicion: Perspectiva de disminución de ingresos y beneficios — El cliente tiene una perspectiva de disminución de los ingresos y los beneficios.
  - `e3` Condicion: Posibilidad de reducción de demanda de productos — Existe la posibilidad de que se reduzca la demanda de los productos que el cliente ofrece.
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso C30** Condicion `e1`: Sector con tendencia futura no firme | descripcion: El cliente pertenece a un sector de la actividad económica o ramo de negocios cuya tendencia futura no es firme. | tramo: Pertenezca a un sector de la actividad económica o ramo de negocios cuya tendencia futura no sea firme
