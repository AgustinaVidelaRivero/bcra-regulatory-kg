# Relectura de concordancia: 25 de los 255 casos leídos (semilla 20261008), sin ver los códigos

## Unidad `ext::3.11.3.1` (item)
- herencia: [chapeau_seccion S3] Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas
en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–,
adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán
cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables. | **[abre la lista]** [intro 3.11.3] endeudamientos comprendidos en el punto 7.9. originados a partir del 07/01/21
(únicamente originados a partir del 08/08/25 en el caso de aquellos comprendidos en
el punto 7.9.1.4.) o prefinanciaciones de exportaciones comprendidas en el punto
7.8.5., para la compra de moneda extranjera para la constitución de las garantías en
cuentas en moneda extranjera abiertas en entidades financieras locales o en el
exterior –cuando se trate de un endeudamiento financiero comprendido en el punto
3.5. o las p | [cierre 3.11.3] El acceso también podrá ser dado a los fideicomisos constituidos en el país para
garantizar la atención de los servicios de capital e intereses de tales endeudamientos.
- texto propio: 3.11.3.1. las compras se realicen en forma simultánea con la liquidación de divisas
y/o a partir de fondos ingresados a nombre del exportador en una cuenta
de corresponsalía en el exterior de una entidad local; y
- entidades de la unidad:
  - `e1` Operacion: Acceso al mercado de cambios para compra de moneda extranjera — Acceso al mercado de cambios para compra de moneda extranjera destinada a constituir garantías en cuentas en moneda extranjera, para residentes con endeudamientos o prefinanciaciones de exportaciones 
  - `e2` Potestad: Facultad de dar acceso al mercado de cambios — Las entidades quedan facultadas a dar acceso al mercado de cambios a los residentes bajo las condiciones especificadas
  - `e3` Condicion: Compras simultáneas con liquidación de divisas — Las compras deben realizarse en forma simultánea con la liquidación de divisas
  - `e4` Condicion: Fondos desde cuenta de corresponsalía en el exterior — Las compras pueden realizarse a partir de fondos ingresados a nombre del exportador en una cuenta de corresponsalía en el exterior de una entidad local
  - `e5` Excepcion: Acceso para fideicomisos constituidos en el país — El acceso al mercado de cambios también se extiende a los fideicomisos constituidos en el país para garantizar la atención de servicios de capital e intereses de los endeudamientos
- relaciones del crudo (sin establecida_en ni de sujeto): e3 condicion_de e2; e4 condicion_de e2
- NODOS A CLASIFICAR:
  - **caso 8** Excepcion `e5`: Acceso para fideicomisos constituidos en el país | descripcion: El acceso al mercado de cambios también se extiende a los fideicomisos constituidos en el país para garantizar la atención de servicios de capital e intereses de los endeudamientos | tramo: El acceso también podrá ser dado a los fideicomisos constituidos en el país para garantizar la atención de los servicios de capital e intereses de tales endeudamientos

## Unidad `cap::3.2.1.1` (punto_no_item)
- herencia: [intro 3.2] Las participaciones en fondos (carteras de activos) imputadas a la cartera de inversión
–incluidas las exposiciones fuera de balance, tales como los compromisos de suscripciones fu-
turas– se deberán tratar de acuerdo con uno o más de los siguientes enfoques: de transparen-
cia (“look-through approach”, LTA), reglamentario (“mandate-based approach”, MBA) y residual
(“fall-back approach”, FBA). | [intro 3.2] Quedan comprendidas las participaciones en fondos comunes regidos por la Ley 24.083 de
Fondos Comunes de Inversión y en fideicomisos –en este último caso, en la medida en que el
riesgo de la inversión no se estructure a través de instrumentos que se emitan con distinta pre-
lación para el cobro, tales como títulos de deuda y certificados de participación–, imputados a
la cartera de inversión. | [encabezado 3.2.1] 3.2.1. Enfoques.
- texto propio: 3.2.1.1. Enfoque de transparencia (LTA).
Las exposiciones con el fondo deberán ponderarse como si fueran exposiciones
directas de la entidad financiera.
Este enfoque deberá utilizarse cuando se verifiquen las siguientes condiciones
en forma concurrente:
i) La entidad financiera reciba información suficiente y con adecuada fre-
cuencia acerca de las exposiciones subyacentes.
Esta condición se considerará satisfecha si el fondo provee información fi-
nanciera con una frecuencia mínima trimestral y el grado de detalle de la in-
formación es suficiente para el cálculo de los ponderadores de riesgo.
ii) La información a que se refiere el acápite i) haya sido verificada por un ter-
cero independiente.
Esta condición se considerará satisfecha si las exposiciones subyacentes
son verificadas por un tercero independiente –tal como la entidad deposita-
ria o custodio, el agente de control y revisión de fideicomisos o, cuando fue-
re aplicable, un auditor externo o la compañía gerente–.
En el caso de las exposiciones subyacentes a las operaciones con deriva-
dos realizadas por el fondo –toda vez que esos subyacentes den origen a
una ponderación por riesgo de crédito– y de las exposiciones al riesgo de
crédito de contraparte concomitantes, en lugar de calcular el ajuste de va-
luación del crédito (CVA) asociado a esas exposiciones por derivados de
acuerdo con el punto 4.2.2., se deberá multiplicar la exposición al riesgo de
crédito de contraparte por un factor de 1,5 antes de aplicar el ponderador
que corresponda a la contraparte. Cuando el CVA no sea aplicable tampo-
co lo será el factor de 1,5. Tal es el caso de: (i) las exposiciones con CCP y
(ii) las operaciones de financiación con títulos valores (“Securities Financing
Transactions”, SFT).
Las entidades financieras podrán basar
- entidades de la unidad:
  - `e1` Operacion: Ponderación de exposiciones con fondos — Las exposiciones con el fondo se ponderan como si fueran exposiciones directas de la entidad financiera.
  - `e2` Obligacion: Utilizar LTA cuando se verifican condiciones — El enfoque de transparencia (LTA) deberá utilizarse cuando se verifiquen las siguientes condiciones en forma concurrente.
  - `e3` Condicion: Información suficiente y frecuencia trimestral — La entidad financiera recibe información suficiente y con adecuada frecuencia acerca de las exposiciones subyacentes, satisfecha si el fondo provee información financiera con frecuencia mínima trimest
  - `e4` Condicion: Verificación por tercero independiente — La información sobre exposiciones subyacentes ha sido verificada por un tercero independiente: entidad depositaria o custodio, agente de control y revisión de fideicomisos, auditor externo o compañía 
  - `e5` Excepcion: Excepción CVA — exposiciones con derivados — Para exposiciones subyacentes a operaciones con derivados realizadas por el fondo que den origen a ponderación por riesgo de crédito, en lugar de calcular CVA según punto 4.2.2., se multiplica la expo
  - `e6` Excepcion: No aplicación del factor 1,5 — CCP y SFT — El factor de 1,5 no se aplica cuando CVA no es aplicable: en exposiciones con entidades de contraparte central (CCP) y en operaciones de financiación con títulos valores (Securities Financing Transact
  - `e7` Potestad: Basarse en cálculos de terceros para ponderadores — Las entidades financieras pueden basarse en cálculos de terceros para determinar los ponderadores de riesgo a aplicar a inversiones en fondos (ponderadores de subyacentes) si carecen de información ne
  - `e8` Restriccion: Ponderador 1,2 veces cuando se usan cálculos de terceros — Cuando se utilizan cálculos de terceros para determinar ponderadores, el ponderador a aplicar será 1,2 veces el ponderador que correspondería a una exposición directa.
- relaciones del crudo (sin establecida_en ni de sujeto): e3 condicion_de e2; e4 condicion_de e2
- NODOS A CLASIFICAR:
  - **caso 12** Excepcion `e6`: No aplicación del factor 1,5 — CCP y SFT | descripcion: El factor de 1,5 no se aplica cuando CVA no es aplicable: en exposiciones con entidades de contraparte central (CCP) y en operaciones de financiación con títulos valores (Securities Financing Transactions, SFT). | tramo: Cuando el CVA no sea aplicable tampoco lo será el factor de 1,5. Tal es el caso de: (i) las exposiciones con CCP y (ii) las operaciones de financiación con títulos valores ("Securities Financing Transactions", SFT).

## Unidad `ext::10.4.2.6` (item)
- herencia: **[abre la lista]** [intro 10.4.2] La entidad podrá dar acceso al mercado de cambios para el pago al exterior en la
medida que verifique previamente que se cumplen la totalidad de los siguientes
requisitos:
- texto propio: 10.4.2.6. El cliente no registra situaciones de demora en la regularización de pagos
con registro de ingreso aduanero pendiente realizados a partir del 02/09/19.
Los pagos de importaciones de bienes con registro de ingreso aduanero
pendiente concretados entre el 02/09/19 y el 31/10/19, por operaciones
comprendidas en los puntos 10.4.1.2. a 10.4.1.4., que no se encuentren
regularizados según lo previsto en el punto 10.5. son considerados en
situación de demora a partir del 02/11/20.
Las entidades deberán consultar en el apartado “Régimen Informativo
SEPAIMPO” del sitio www3.bcra.gob.ar, si el cliente registra en el sistema
demoras en el conjunto de las entidades.
Este requisito no será de aplicación para:
i) el sector público;
ii) todas las organizaciones empresariales, cualquiera sea su forma
societaria, en donde el Estado Nacional tenga participación mayoritaria
en el capital o en la formación de las decisiones societarias;
iii)los fideicomisos constituidos con aportes del sector público nacional; y
iv)las personas jurídicas que tengan a su cargo la provisión de
medicamentos críticos a pacientes cuando realicen pagos anticipados
por ese tipo de bienes a ingresar por Solicitud Particular por el
beneficiario de dicha cobertura médica.
- entidades de la unidad:
  - `e1` Condicion: Cliente sin demoras en regularización de pagos — El cliente no registra situaciones de demora en la regularización de pagos con registro de ingreso aduanero pendiente realizados a partir del 02/09/19. Se consideran en situación de demora los pagos d
  - `e2` Obligacion: Consultar demoras en Régimen Informativo SEPAIMPO — Las entidades deberán consultar en el apartado Régimen Informativo SEPAIMPO del sitio www3.bcra.gob.ar si el cliente registra en el sistema demoras en el conjunto de las entidades
  - `e3` Excepcion: Excepción sector público — El requisito de que el cliente no registre situaciones de demora no será de aplicación para el sector público
  - `e4` Excepcion: Excepción organizaciones con participación estatal mayoritaria — El requisito de que el cliente no registre situaciones de demora no será de aplicación para todas las organizaciones empresariales, cualquiera sea su forma societaria, en donde el Estado Nacional teng
  - `e5` Excepcion: Excepción fideicomisos con aportes del sector público — El requisito de que el cliente no registre situaciones de demora no será de aplicación para los fideicomisos constituidos con aportes del sector público nacional
  - `e6` Excepcion: Excepción personas jurídicas proveedoras de medicamentos críticos — El requisito de que el cliente no registre situaciones de demora no será de aplicación para las personas jurídicas que tengan a su cargo la provisión de medicamentos críticos a pacientes cuando realic
  - `e7` Operacion: Pago anticipado de importación con registro aduanero pendiente — Pagos de importaciones de bienes con registro de ingreso aduanero pendiente realizados a partir del 02/09/19
- relaciones del crudo (sin establecida_en ni de sujeto): e1 condicion_de e7
- NODOS A CLASIFICAR:
  - **caso 23** Excepcion `e6`: Excepción personas jurídicas proveedoras de medicamentos críticos | descripcion: El requisito de que el cliente no registre situaciones de demora no será de aplicación para las personas jurídicas que tengan a su cargo la provisión de medicamentos críticos a pacientes cuando realicen pagos anticipados por ese tipo de bienes a ingresar por Solicitud Particular por el beneficiario de dicha cobertura médica | tramo: las personas jurídicas que tengan a su cargo la provisión de medicamentos críticos a pacientes cuando realicen pagos anticipados por ese tipo de bienes a ingresar por Solicitud Particular por el beneficiario de dicha cobertura médica

## Unidad `ext::3.5.6.6` (item)
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
- texto propio: 3.5.6.6. se trate de un pago de intereses que se concreta simultáneamente con la
liquidación por el importe al menos equivalente de:
i) nuevos endeudamientos financieros comprendidos en este punto 3.5.
con una vida promedio no inferior a 2 (dos) años y que contemplen
como mínimo 1 (un) año de gracia para el pago de capital, en ambos
casos contados desde la fecha en que se concreta el acceso al
mercado.
ii) nuevos aportes de inversión directa de no residentes.
Los endeudamientos financieros y/o los aportes de inversión extranjera
directa, que no podrán ser computados a los efectos de otros mecanismos
considerados en la normativa cambiaria, podrán ser ingresados y liquidados
por el deudor que cancela los intereses o por otra empresa residente
perteneciente a su grupo económico.
- entidades de la unidad:
  - `e1` Excepcion: Excepción — pago simultáneo de intereses con nuevo endeudamiento — Excepción al requisito de conformidad previa del BCRA cuando el pago de intereses se concreta simultáneamente con la liquidación de nuevos endeudamientos financieros con vida promedio no inferior a 2 
  - `e2` Excepcion: Excepción — pago simultáneo de intereses con aportes de inversión directa — Excepción al requisito de conformidad previa del BCRA cuando el pago de intereses se concreta simultáneamente con la liquidación de nuevos aportes de inversión directa de no residentes.
  - `e3` Restriccion: Prohibición — cómputo de endeudamientos en otros mecanismos — Los endeudamientos financieros y los aportes de inversión extranjera directa que se utilizan para cumplir con la excepción no podrán ser computados a los efectos de otros mecanismos considerados en la
  - `e4` Operacion: Ingreso y liquidación de endeudamientos e inversión extranjera — Ingreso y liquidación de endeudamientos financieros y/o aportes de inversión extranjera directa, que pueden ser realizados por el deudor que cancela los intereses o por otra empresa residente pertenec
  - `e5` Condicion: Condición — simultaneidad de pago de intereses y liquidación — El pago de intereses debe concretarse simultáneamente con la liquidación de nuevos endeudamientos o aportes de inversión.
- relaciones del crudo (sin establecida_en ni de sujeto): e5 condicion_de e1; e5 condicion_de e2
- NODOS A CLASIFICAR:
  - **caso 32** Excepcion `e1`: Excepción — pago simultáneo de intereses con nuevo endeudamiento | descripcion: Excepción al requisito de conformidad previa del BCRA cuando el pago de intereses se concreta simultáneamente con la liquidación de nuevos endeudamientos financieros con vida promedio no inferior a 2 años y con mínimo 1 año de gracia para el pago de capital. | tramo: se trate de un pago de intereses que se concreta simultáneamente con la liquidación por el importe al menos equivalente de: i) nuevos endeudamientos financieros comprendidos en este punto 3.5. con una vida promedio no inferior a 2 (dos) años y que contemplen como mínimo 1 (un) año de gracia para el pago de capital, en ambos casos contados desde la fecha en que se concreta el acceso al mercado.

## Unidad `cap::4.3.3.1` (punto_no_item)
- herencia: [intro 4.3] contraparte central.
Comprende a aquellas exposiciones de las entidades financieras con entidades de contrapar-
te central (CCP) que se originen en derivados OTC o negociados en mercados de valores y
en operaciones de financiación con títulos valores (“Securities Financing Transactions”, SFT)
y operaciones de liquidación diferida –definidas en el punto 4.2.–.
No están comprendidas las exposiciones originadas en operaciones al contado y que involu-
cren títulos valores, oro o moneda extranjera, c | [encabezado 4.3.3] 4.3.3. Exposiciones a entidades de contraparte central calificadas.
- texto propio: 4.3.3.1. Exposiciones por operaciones de negociación.
i) Exposiciones de los miembros compensadores con las CCP.
a) La entidad financiera que actúe en carácter de miembro compensa-
dor de una CCP por operaciones propias deberá aplicar un pondera-
dor de riesgo del 2 % a sus exposiciones con la CCP originadas en
operaciones de derivados –OTC o negociados en mercados de valo-
res–, de financiación con títulos valores (SFT) y de liquidación diferi-
da. Cuando la entidad financiera preste servicios de compensación a
clientes, aplicará el ponderador de riesgo del 2 % a la exposición con
la CCP que se origina si, en caso de incumplimiento de la CCP, la
entidad financiera se viera obligada –como miembro compensador a
reembolsar al cliente toda pérdida debido al cambio de valor de sus
transacciones. El ponderador de riesgo aplicado a los activos en ga-
rantía aportados por la entidad financiera a una CCP deberá determi-
narse de acuerdo con lo establecido en los párrafos primero a tercero
del acápite iv) del presente punto.
b) La exposición debida a dichas operaciones se calculará conforme al
enfoque estandarizado para el riesgo de crédito de contraparte (SA-
CCR) establecido en el punto 4.2. para los derivados OTC o negó
ciados en mercados de valores y operaciones de liquidación diferida,
y a lo previsto en la Sección 5. para las SFT.
No se aplicará el plazo mínimo de veinte días hábiles para el cálculo
del período de riesgo de margen (MPOR) de los conjuntos de neteo
en los que se verifiquen más de 5.000 operaciones en la medida en
que no existan disputas pendientes y que dicho conjunto no contenga
garantías ilíquidas u operaciones exóticas. Idéntico criterio se aplica-
rá para la determinación del período de mantenimiento mínimo (T )
M
utilizado en el cálculo de los aforos de
- entidades de la unidad:
  - `e1` Operacion: Exposiciones por operaciones de negociación — miembros compensadores con CCP — Exposiciones de los miembros compensadores con las CCP originadas en operaciones de derivados (OTC o negociados en mercados de valores), de financiación con títulos valores (SFT) y de liquidación dife
  - `e2` Restriccion: Ponderador 2% — exposiciones miembro compensador con CCP (operaciones propias) — Ponderador de riesgo del 2% aplicable a exposiciones de miembro compensador con CCP por operaciones propias (derivados OTC, derivados negociados en mercados de valores, SFT, liquidación diferida).
  - `e3` Restriccion: Ponderador 2% — exposiciones miembro compensador con CCP (servicios de compensación a clientes) — Ponderador de riesgo del 2% aplicable a exposición con CCP cuando miembro compensador presta servicios de compensación a clientes y se vería obligado a reembolsar pérdidas por cambio de valor de trans
  - `e4` Obligacion: Determinación ponderador — activos en garantía a CCP — El ponderador de riesgo de activos en garantía aportados a CCP debe determinarse conforme a lo establecido en los párrafos primero a tercero del acápite iv).
  - `e5` Obligacion: Cálculo exposición — enfoque estandarizado (SA-CCR) — La exposición debe calcularse conforme al enfoque estandarizado para riesgo de crédito de contraparte (SA-CCR) del punto 4.2 para derivados OTC, derivados negociados en mercados de valores y operacion
  - `e6` Excepcion: Excepción MPOR mínimo 20 días — conjuntos con más de 5.000 operaciones — No se aplica el plazo mínimo de 20 días hábiles para cálculo de MPOR en conjuntos de neteo con más de 5.000 operaciones, siempre que no existan disputas pendientes y no contengan garantías ilíquidas u
  - `e6a` Condicion: Condición — no existan disputas pendientes — No existan disputas pendientes en el conjunto de neteo.
  - `e6b` Condicion: Condición — conjunto no contenga garantías ilíquidas u operaciones exóticas — El conjunto de neteo no contenga garantías ilíquidas u operaciones exóticas.
  - `e7` Obligacion: Aplicación idéntico criterio — período de mantenimiento mínimo (TM) en SFT — Idéntico criterio de excepción al plazo mínimo se aplicará para determinación del período de mantenimiento mínimo (TM) en cálculo de aforos de SFT del punto 5.3.2.3.
  - `e8` Restriccion: MPOR mínimo 10 días — derivados OTC con CCP — Se utilizará un MPOR mínimo de 10 días para cálculo de exposiciones a CCP por operaciones de derivados OTC.
  - `e9` Restriccion: Horizonte temporal mínimo 1 año o plazo residual — margen de variación sin protección — Cuando CCP recibe margen de variación y activo del miembro compensador no está protegido contra insolvencia de CCP, horizonte temporal de riesgo mínimo será el menor entre 1 año y plazo residual de op
  - `e10` Operacion: Operaciones con CCP en jurisdicciones con validez legal de liquidación neta — Operaciones con CCP radicadas en jurisdicciones donde liquidación por saldos netos en caso de incumplimiento tiene validez legal, independientemente de insolvencia o quiebra de contraparte.
  - `e11` Obligacion: Cálculo costo de reposición neto — operaciones con CCP — Costo de reposición total de contratos relevantes puede calcularse como costo de reposición neto, siempre que conjunto de operaciones compensables cumpla requisitos de validez legal del punto 5.3.2.5 
  - `e12` Definicion: Acuerdo de neteo — interpretación inclusiva — Incluye todo acuerdo de neteo con validez legal que reconozca derechos de compensación legalmente exigibles, cuando las disposiciones refieran a 'acuerdo marco de neteo' o 'contrato de neteo con una c
  - `e13` Obligacion: Tratamiento individual de transacciones — sin cumplimiento de requisitos de neteo — Si entidad financiera no puede demostrar que acuerdos de neteo cumplen requisitos, cada transacción individual se considerará como conjunto de neteo separado para cálculo de exposición por operaciones
  - `e14` Operacion: Exposiciones de miembros compensadores con sus clientes — Exposiciones de miembros compensadores con sus clientes en operaciones compensadas.
  - `e15` Obligacion: Consideración exposición bilateral — miembro compensador con cliente — Miembro compensador debe considerar su exposición con cliente (incluyendo potencial exposición CVA) como operación bilateral, independientemente de si garantiza operación o actúa como intermediario en
  - `e16` Restriccion: MPOR mínimo 5 días — exposición miembro compensador con clientes — Miembros compensadores pueden calcular exigencia por exposición a clientes aplicando período de riesgo de margen mínimo de 5 días, dado que período de liquidación (close-out) para operaciones compensa
  - `e17` Obligacion: Utilización EAD reducida — cálculo CVA — La EAD reducida debe utilizarse también para cálculo del ajuste de valuación de crédito (CVA) del punto 4.2.3.
  - `e18` Potestad: Reconocimiento garantía — tramo CCP-miembro y miembro-cliente — Miembro compensador puede reconocer garantía recibida de cliente y transferida a CCP tanto para tramo CCP-miembro compensador como para tramo miembro compensador-cliente.
  - `e19` Obligacion: Mitigación exposición — margen inicial de clientes — El margen inicial aportado por clientes al miembro compensador mitiga su exposición respecto de sus clientes.
  - `e20` Obligacion: Aplicación idéntico tratamiento — estructuras multinivel de clientes — Idéntico tratamiento de garantía se aplica a estructuras multinivel de clientes (entre clientes de nivel superior e inferior).
  - `e21` Operacion: Exposiciones de clientes — transacción con miembro compensador como intermediario — Transacción realizada por cliente de miembro compensador donde miembro compensador actúa como intermediario financiero (realiza transacción con CCP por indicación del cliente).
  - `e22` Potestad: Tratamiento exposición cliente — condiciones de protección cumplidas — Exposición de cliente hacia miembro compensador puede recibir tratamiento del acápite i) si se cumplen condiciones de protección especificadas.
  - `e23` Condicion: Condición — identificación de transacciones y protección de garantías — CCP identifica transacciones como transacciones de clientes y garantías son mantenidas bajo acuerdos que impiden pérdidas del cliente por: (i) falta de pago/insolvencia del miembro compensador; (ii) f
  - `e24` Obligacion: Transferencia de garantía — ausencia de impedimentos legales — En caso de impago o insolvencia del miembro compensador, no habrá impedimentos legales (salvo orden judicial a la que cliente tiene derecho) para transferir garantía de clientes a CCP, otro miembro co
  - `e25` Obligacion: Revisión legal adecuada — acuerdos de protección de garantías — Cliente debe haber realizado revisión legal adecuada (y llevarla a cabo cuando sea necesario para asegurar aplicabilidad continua) y contar con fundamentos para concluir que acuerdos serán legales, vá
  - `e26` Condicion: Condición — portabilidad de transacciones y transferencia a valor de mercado — Leyes, regulaciones y acuerdos hacen altamente probable la portabilidad de transacciones: transacciones compensadoras del miembro en impago/insolvencia serán concluidas por CCP; posiciones y garantías
  - `e27` Obligacion: Cumplimiento idénticas condiciones — exposición de cliente con CCP y estructuras multinivel — Idénticas condiciones deben cumplirse para tratamiento de exposición de cliente con CCP (cuando cumplimiento garantizado por miembro compensador) y para exposiciones de clientes de nivel inferior con 
  - `e28` Restriccion: Ponderador 4% — cliente sin protección contra insolvencia conjunta — Cuando cliente no está protegido contra pérdidas por falta de pago/insolvencia conjunta del miembro compensador y alguno de sus clientes, pero se cumplen otras condiciones, exposición recibe ponderado
  - `e29` Obligacion: Tratamiento como operación bilateral — cliente sin cumplimiento de requisitos — Cuando cliente no cumple requisitos de protección, exposición con miembro compensador (incluyendo exposición potencial CVA) debe tratarse como operación bilateral.
  - `e30` Operacion: Tratamiento de garantías — activos constituidos en garantía de operaciones — Tratamiento de activos constituidos en garantía de operaciones con CCP.
  - `e31` Obligacion: Aplicación ponderador según cartera — activos en garantía — Activo constituido en garantía recibe ponderador según normas, considerando qué tratamiento (cartera de negociación o inversión) hubiera recibido si no hubiera sido depositado en CCP.
  - `e32` Restriccion: Riesgo de crédito de contraparte — garantías no protegidas contra quiebra — Cuando activos se coloquen en garantía sin protección contra quiebra de CCP o miembro compensador, entidad financiera debe reconocer riesgo de crédito por posibilidad de pérdidas por calidad creditici
  - `e33` Obligacion: Sujeción a requisito SA-CCR — activos en garantía — Activos constituidos en garantía están sujetos al requisito de riesgo de crédito de contraparte (SA-CCR) del punto 4.2, incluyendo incremento por aforos del punto 5.3.2.3, computados conforme acápite 
  - `e34` Restriccion: Ponderador 2% — garantías incluidas en exposición por operaciones (CCP) — Cuando CCP recibe activos en garantía, se aplica ponderador del 2% a garantías incluidas en definición de exposición por operaciones.
  - `e35` Obligacion: Aplicación ponderador CCP — garantías para otros fines — Ponderador de riesgo correspondiente a CCP se aplica a activos o garantías aportados para otros fines.
  - `e36` Obligacion: Consideración para NICA — garantía depositada sin protección — Garantía depositada sin protección en caso de quiebra debe considerarse para Monto Neto de Garantía Independiente (NICA) del acápite v) punto 4.2.1.1.
  - `e37` Excepcion: Excepción exigencia de capital — garantía de miembro compensador protegida — Garantía de miembro compensador (efectivo, títulos, otros activos, excesos de márgenes) mantenida por custodio y protegida contra quiebra de CCP no está sujeta a exigencia de capital por riesgo de cré
  - `e38` Definicion: Custodio — definición — Fiduciario o agente que mantiene activos bajo título que no acuerda derechos al custodio ni a sus acreedores y garantiza que no se obstaculizará judicialmente devolución de activos en caso de quiebra 
  - `e39` Excepcion: Excepción exigencia de capital — garantía de cliente protegida — Garantía de cliente mantenida por custodio y protegida contra quiebra de CCP, miembro compensador y otros clientes no está sujeta a exigencia de capital por riesgo de crédito de contraparte.
  - `e40` Restriccion: Ponderador 2% — garantía de cliente mantenida por CCP (condiciones cumplidas) — Si garantía de cliente es mantenida por CCP sin protección contra su quiebra, se aplica ponderador de riesgo del 2% si se cumplen condiciones a) y b) del acápite iii).
  - `e41` Restriccion: Ponderador 4% — garantía de cliente mantenida por CCP (condición anteúltima) — Se aplica ponderador de riesgo del 4% si se da el caso del anteúltimo párrafo del acápite iii) (cliente sin protección contra insolvencia conjunta).
- relaciones del crudo (sin establecida_en ni de sujeto): e6a condicion_de e6; e6b condicion_de e6; e23 condicion_de e22; e26 condicion_de e22
- NODOS A CLASIFICAR:
  - **caso 40** Excepcion `e39`: Excepción exigencia de capital — garantía de cliente protegida | descripcion: Garantía de cliente mantenida por custodio y protegida contra quiebra de CCP, miembro compensador y otros clientes no está sujeta a exigencia de capital por riesgo de crédito de contraparte. | tramo: La garantía constituida por un cliente, mantenida por un custodio y protegida de la quiebra de la CCP y del miembro compensador y sus otros clientes no está sujeta a exigencia de capital por riesgo de crédito de contraparte.

## Unidad `cla::6.5::intro` (intro)
- herencia: [encabezado 6.5] 6.5. Niveles de clasificación.
- texto propio: Cada cliente, y la totalidad de sus financiaciones comprendidas, se incluirá en una de las si-
guientes cinco categorías, las que se definen teniendo en cuenta las condiciones que se deta-
llan en cada caso.
Los clientes que no registren asistencia crediticia de la entidad y que posteriormente reciban fi-
nanciaciones de ésta que no superen el importe resultante de aplicar sobre el saldo de deuda
registrado en el sistema financiero, según la última información disponible en la “Central de
deudores” a la fecha de su otorgamiento, el porcentaje establecido en el punto 2.2.5. de las
normas sobre “Previsiones mínimas por riesgo de incobrabilidad” correspondiente a la peor cla-
sificación asignada, podrán ser clasificados por la entidad teniendo en cuenta únicamente el
análisis del flujo de fondos proyectado. Las asistencias así otorgadas no serán consideradas a
los fines a que se refiere el punto 6.6.
A fin de verificar el cumplimiento de las obligaciones sin recurrir a nueva financiación directa o
indirecta o a refinanciaciones, no se considerarán refinanciaciones las facilidades adicionales
que se otorguen respecto de los márgenes vigentes acordados, siempre que el nuevo apoyo
crediticio implique nuevos desembolsos de fondos y no supere el 10 % del cupo asignado en
oportunidad de la última evaluación crediticia del cliente, en la medida en que éstas sean con-
sistentes con el curso normal de los negocios y exista capacidad para atender el resto de las
obligaciones financieras, ni las nuevas financiaciones y las refinanciaciones asociadas a una
mayor inversión derivada de la expansión de las actividades, y siempre que pueda demostrarse
que el flujo de fondos proyectado permitirá afrontar la totalidad de sus obligaciones.
Tampoco se considerarán dentro de ese concepto las r
- entidades de la unidad:
  - `e1` Operacion: Inclusión de cliente en categoría de clasificación — Cada cliente y la totalidad de sus financiaciones comprendidas se incluirá en una de las cinco categorías de clasificación, definidas según las condiciones detalladas en cada caso.
  - `e2` Definicion: Categorías de clasificación — cinco niveles — Cinco categorías de clasificación de deudores, definidas según las condiciones detalladas en cada caso.
  - `e3` Condicion: Cliente sin asistencia crediticia previa — clasificación por flujo de fondos — Clientes sin asistencia crediticia previa de la entidad que reciben financiaciones que no superen el importe resultante de aplicar el porcentaje de previsiones mínimas sobre el saldo de deuda en la Ce
  - `e4` Potestad: Clasificación por flujo de fondos proyectado — clientes sin asistencia previa — La entidad podrá clasificar a clientes sin asistencia crediticia previa teniendo en cuenta únicamente el análisis del flujo de fondos proyectado, cuando se cumplan las condiciones especificadas.
  - `e5` Excepcion: Exclusión de asistencias — punto 6.6 — Las asistencias crediticias otorgadas a clientes sin asistencia previa no serán consideradas a los fines del punto 6.6.
  - `e6` Definicion: Facilidades adicionales — no refinanciación — Facilidades adicionales sobre márgenes vigentes acordados que impliquen nuevos desembolsos de fondos y no superen el 10 % del cupo asignado en la última evaluación crediticia, no se consideran refinan
  - `e7` Condicion: Facilidades adicionales — consistencia con curso normal de negocios — Las facilidades adicionales deben ser consistentes con el curso normal de los negocios y debe existir capacidad para atender el resto de las obligaciones financieras.
  - `e8` Definicion: Nuevas financiaciones y refinanciaciones — expansión de actividades — Nuevas financiaciones y refinanciaciones asociadas a mayor inversión derivada de expansión de actividades, cuando pueda demostrarse que el flujo de fondos proyectado permitirá afrontar la totalidad de
  - `e9` Condicion: Flujo de fondos proyectado — capacidad de pago total — Debe demostrarse que el flujo de fondos proyectado permitirá afrontar la totalidad de las obligaciones financieras.
  - `e10` Excepcion: Refinanciaciones — productores agropecuarios Ley de Emergencia — Las refinanciaciones otorgadas a productores agropecuarios derivadas de la aplicación de disposiciones de la Ley de Emergencia Agropecuaria no se consideran refinanciaciones a los fines de verificació
  - `e11` Obligacion: Consideración de flujo de fondos — productores agropecuarios emergencia — A los fines de la clasificación de productores agropecuarios beneficiarios de la Ley de Emergencia Agropecuaria, deberá tenerse en cuenta el flujo de fondos proyectado para el momento en que concluya 
  - `e12` Restriccion: Prohibición mejoramiento de clasificación — productores agropecuarios emergencia — El tratamiento dispensado en el marco de la Ley de Emergencia Agropecuaria no podrá implicar mejoramiento de la clasificación asignada al cliente en función de su situación individual preexistente a l
  - `e13` Restriccion: Límite temporal — aplicación emergencia agropecuaria — La aplicación del tratamiento de la Ley de Emergencia Agropecuaria no podrá extenderse más allá de la vigencia fijada para la emergencia.
- relaciones del crudo (sin establecida_en ni de sujeto): e3 condicion_de e4; e7 condicion_de e6; e9 condicion_de e8
- NODOS A CLASIFICAR:
  - **caso 55** Excepcion `e5`: Exclusión de asistencias — punto 6.6 | descripcion: Las asistencias crediticias otorgadas a clientes sin asistencia previa no serán consideradas a los fines del punto 6.6. | tramo: Las asistencias así otorgadas no serán consideradas a los fines a que se refiere el punto 6.6

## Unidad `ext::6.4` (item)
- herencia: **[abre la lista]** [chapeau_seccion S6] En el marco de estas disposiciones se definen los siguientes conceptos:
- texto propio: 6.4. Operaciones a término.
Comprende las operaciones en las cuales la liquidación está pactada en un plazo mayor a los
2 (dos) días hábiles desde la fecha de su concertación.
En el caso de que se prevea la entrega efectiva de instrumentos operados en el mercado de
cambios, estas operaciones quedan sujetas a la norma cambiaria y se consideran un acceso
al mercado de cambios a concretarse en la fecha de su liquidación.
No están sujetas a estas normas las concertaciones y cancelaciones de operaciones de
futuros en mercados regulados, “forwards”, opciones y cualquier otro tipo de derivado en la
medida que estén instrumentadas bajo ley argentina y su liquidación se efectúe en el país por
compensación en moneda doméstica, sin que pueda generar obligaciones presentes o futuras
de realizar pagos en moneda extranjera.
- entidades de la unidad:
  - `e1` Definicion: Operaciones a término — definición — Operaciones en las cuales la liquidación está pactada en un plazo mayor a los 2 (dos) días hábiles desde la fecha de su concertación.
  - `e2` Condicion: Entrega efectiva de instrumentos — condición — Cuando se prevea la entrega efectiva de instrumentos operados en el mercado de cambios.
  - `e3` Operacion: Acceso al mercado de cambios — operaciones a término — Operaciones a término con entrega efectiva de instrumentos que se consideran un acceso al mercado de cambios a concretarse en la fecha de su liquidación, sujetas a la norma cambiaria.
  - `e4` Excepcion: Excepción — futuros, forwards, opciones y derivados — Las concertaciones y cancelaciones de operaciones de futuros en mercados regulados, forwards, opciones y otros derivados instrumentados bajo ley argentina con liquidación en el país por compensación e
  - `e5` Condicion: Instrumentación bajo ley argentina — condición — Cuando los derivados estén instrumentados bajo ley argentina.
  - `e6` Condicion: Liquidación por compensación en moneda doméstica — condición — Cuando la liquidación se efectúe en el país por compensación en moneda doméstica.
  - `e7` Condicion: Sin obligaciones de pagos en moneda extranjera — condición — Cuando no pueda generar obligaciones presentes o futuras de realizar pagos en moneda extranjera.
- relaciones del crudo (sin establecida_en ni de sujeto): e2 condicion_de e3; e5 condicion_de e4; e6 condicion_de e4; e7 condicion_de e4
- NODOS A CLASIFICAR:
  - **caso 56** Excepcion `e4`: Excepción — futuros, forwards, opciones y derivados | descripcion: Las concertaciones y cancelaciones de operaciones de futuros en mercados regulados, forwards, opciones y otros derivados instrumentados bajo ley argentina con liquidación en el país por compensación en moneda doméstica sin obligaciones de pagos en moneda extranjera no están sujetas a estas normas. | tramo: No están sujetas a estas normas las concertaciones y cancelaciones de operaciones de futuros en mercados regulados, "forwards", opciones y cualquier otro tipo de derivado en la medida que estén instrumentadas bajo ley argentina y su liquidación se efectúe en el país por compensación en moneda doméstica, sin que pueda generar obligaciones presentes o futuras de realizar pagos en moneda extranjera.

## Unidad `cap::3.1.5.3` (punto_no_item)
- herencia: [intro 3.1] Se denomina “posición de titulización” a la exposición a una titulización (o retitulización), tradi-
cional o sintética, o a una estructura con similares características.
La exposición a los riesgos de una titulización puede surgir, entre otros, de los siguientes con-
ceptos: tenencia de títulos valores emitidos en el marco de la titulización –es decir, títulos de
deuda y/o certificados de participación, tales como bonos de titulización de activos (“Asset-
Backed Securities”, ABS) y bonos de tit | [encabezado 3.1.5] 3.1.5. Criterios a observar en el cómputo de la exigencia de capital mínimo.
- texto propio: 3.1.5.3. No se incluirán dentro de las previsiones por riesgo de incobrabilidad computa-
bles del punto 8.2.3.3. las previsiones generales ni las específicas asociadas a
las posiciones de titulización o a las exposiciones subyacentes que están toda-
vía en el activo de la entidad originante. No obstante, las entidades originantes
podrán deducir de las posiciones de titulización ponderadas al 1250 % tanto el
monto de las previsiones específicas como los descuentos no reembolsables en
el precio de adquisición de los activos subyacentes a la titulización. Las previ-
siones específicas asociadas a las posiciones de titulización se considerarán en
el cálculo del importe de la posición de acuerdo con la definición prevista en el
punto 3.1.5.4. Las previsiones generales de las exposiciones subyacentes no se
tendrán en cuenta en ningún cálculo.
- entidades de la unidad:
  - `e1` Restriccion: Exclusión previsiones generales — titulizaciones — No se incluirán dentro de las previsiones por riesgo de incobrabilidad computables las previsiones generales ni las específicas asociadas a las posiciones de titulización o a las exposiciones subyacen
  - `e2` Excepcion: Deducción previsiones específicas — posiciones ponderadas 1250% — Las entidades originantes pueden deducir de las posiciones de titulización ponderadas al 1250% tanto el monto de las previsiones específicas como los descuentos no reembolsables en el precio de adquis
  - `e3` Obligacion: Consideración previsiones específicas — cálculo posición — Las previsiones específicas asociadas a las posiciones de titulización se considerarán en el cálculo del importe de la posición de acuerdo con la definición prevista en el punto 3.1.5.4
  - `e4` Restriccion: Exclusión previsiones generales — exposiciones subyacentes — Las previsiones generales de las exposiciones subyacentes no se tendrán en cuenta en ningún cálculo
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 58** Excepcion `e2`: Deducción previsiones específicas — posiciones ponderadas 1250% | descripcion: Las entidades originantes pueden deducir de las posiciones de titulización ponderadas al 1250% tanto el monto de las previsiones específicas como los descuentos no reembolsables en el precio de adquisición de los activos subyacentes | tramo: las entidades originantes podrán deducir de las posiciones de titulización ponderadas al 1250 % tanto el monto de las previsiones específicas como los descuentos no reembolsables en el precio de adquisición de los activos subyacentes a la titulización

## Unidad `ext::8.5.17.20` (item)
- herencia: [intro 8.5] La entidad podrá considerar cumplimentado parcial o totalmente el seguimiento de un permiso
de embarque cuando cuente con los elementos que le permitan considerar que la operación
se encuentra en alguna de las situaciones detalladas a continuación y se verifiquen las
condiciones previstas en cada caso.
La documentación utilizada para certificar el concepto y monto de las divisas imputado en
cada caso deberá quedar archivada en la entidad a disposición del BCRA. | **[abre la lista]** [intro 8.5.17] Por el valor que corresponda a ventajas aduaneras u otras situaciones previstas en el
siguiente listado de operaciones:
- texto propio: 8.5.17.20. Exportaciones de bienes enviados al exterior con fines promocionales
amparadas por la Resolución 772/92 de Administración Nacional de
Aduanas, hasta un tope de USD 5.000 (dólares estadounidenses cinco
mil).
- entidades de la unidad:
  - `e1` Operacion: Exportación bienes con fines promocionales — Exportaciones de bienes enviados al exterior con fines promocionales amparadas por la Resolución 772/92 de Administración Nacional de Aduanas
  - `e2` Restriccion: Tope USD 5.000 — exportación promocional — El valor de las exportaciones de bienes enviados al exterior con fines promocionales no podrá exceder USD 5.000
  - `e3` Excepcion: Excepción seguimiento — exportación promocional — Las exportaciones de bienes enviados al exterior con fines promocionales amparadas por la Resolución 772/92 de Administración Nacional de Aduanas, hasta un tope de USD 5.000, quedan exceptuadas del se
- relaciones del crudo (sin establecida_en ni de sujeto): e2 limita e1
- NODOS A CLASIFICAR:
  - **caso 61** Excepcion `e3`: Excepción seguimiento — exportación promocional | descripcion: Las exportaciones de bienes enviados al exterior con fines promocionales amparadas por la Resolución 772/92 de Administración Nacional de Aduanas, hasta un tope de USD 5.000, quedan exceptuadas del seguimiento de permisos de embarque | tramo: Exportaciones de bienes enviados al exterior con fines promocionales amparadas por la Resolución 772/92 de Administración Nacional de Aduanas, hasta un tope de USD 5.000 (dólares estadounidenses cinco mil)

## Unidad `cap::2.11.3.5` (item)
- herencia: [chapeau_seccion S2] A los efectos de la aplicación de las disposiciones de la presente sección, las entidades financieras
se clasificarán en:
i)Grupo 1: entidades calificadas por el BCRA como de importancia sistémica a nivel local | [chapeau_seccion S2] (D-SIB) y sucursales o subsidiarias de bancos del exterior calificados como de impor-
tancia sistémica global (G-SIB). | [chapeau_seccion S2] ii) Grupo 2: entidades financieras no comprendidas en el acápite i).
En aquellos casos en que no se establezcan disposiciones específicas para cada uno de los citados
grupos de entidades financieras, deberá aplicarse el mismo tratamiento a ambos grupos.
Las entidades financieras que presenten cambios en su calificación –conforme a lo previsto en los
acápites precedentes–, contarán con un plazo de 6 meses para aplicar las disposiciones específicas
correspondientes al nuevo grupo al que pertenezca | **[abre la lista]** [intro 2.11.3] A los fines de determinar si una exposición debe ser tratada como una acción, las en-
tidades financieras del grupo 1 deberán tener en cuenta la realidad económica del ins-
trumento.
Quedan comprendidas:
- texto propio: 2.11.3.5. Los títulos de deuda y otros valores, los derivados y los vehículos estructu-
rados con el fin de replicar la realidad económica de una acción.
Se incluyen las obligaciones cuyo rendimiento esté vinculado al de las ac-
ciones, y las acciones contabilizadas como un préstamo que se originen en
un canje de deuda por acciones realizado en un proceso de reestructuración
de deudas. El requisito de capitales mínimos que se determine para estos úl-
timos instrumentos no puede ser menor al que le hubiera correspondido de
haber permanecido en la cartera de créditos.
A los fines del cumplimiento de estas disposiciones, la SEFYC podrá recate-
gorizar las posiciones de deuda como posiciones en acciones si advierte que
no se cumplen las condiciones y requisitos que aseguren el adecuado trata-
miento de las tenencias.
Las inversiones en acciones estructuradas con el objeto de replicar la reali-
dad económica de las exposiciones crediticias o de titulizaciones no se con-
siderarán acciones.
- entidades de la unidad:
  - `e1` Operacion: Títulos de deuda replicando acción — Títulos de deuda, otros valores, derivados y vehículos estructurados cuyo fin es replicar la realidad económica de una acción; incluye obligaciones cuyo rendimiento esté vinculado al de las acciones, 
  - `e2` Restriccion: Requisito mínimo capital — acciones de canje — El requisito de capitales mínimos para acciones originadas en canje de deuda no puede ser inferior al que hubiera correspondido si permanecieran en cartera de créditos.
  - `e3` Potestad: Recategorización de posiciones de deuda a acciones — La SEFYC está facultada a recategorizar posiciones de deuda como posiciones en acciones cuando advierte incumplimiento de las condiciones y requisitos para asegurar el adecuado tratamiento de las tene
  - `e4` Condicion: Incumplimiento de condiciones de tratamiento — Supuesto en que la SEFYC advierte que no se cumplen las condiciones y requisitos que aseguren el adecuado tratamiento de las tenencias.
  - `e5` Excepcion: Excepción — acciones estructuradas replicando exposiciones crediticias — Las inversiones en acciones estructuradas cuyo objeto es replicar la realidad económica de exposiciones crediticias o de titulizaciones quedan exceptuadas de ser consideradas acciones.
- relaciones del crudo (sin establecida_en ni de sujeto): e4 condicion_de e3
- NODOS A CLASIFICAR:
  - **caso 62** Excepcion `e5`: Excepción — acciones estructuradas replicando exposiciones crediticias | descripcion: Las inversiones en acciones estructuradas cuyo objeto es replicar la realidad económica de exposiciones crediticias o de titulizaciones quedan exceptuadas de ser consideradas acciones. | tramo: Las inversiones en acciones estructuradas con el objeto de replicar la realidad económica de las exposiciones crediticias o de titulizaciones no se considerarán acciones

## Unidad `cla::7.2.1` (punto_no_item)
- herencia: [encabezado 7.2] 7.2. Niveles de clasificación.
- texto propio: 7.2.1. Situación normal.
Comprende los clientes que atienden en forma puntual el pago de sus obligaciones o con
atrasos que no superan los 31 días.
Los adelantos transitorios en cuenta corriente se considerarán de cumplimiento normal
hasta los 61 días contados desde su otorgamiento.
A los fines de establecer los días de atraso, en el caso de las financiaciones instrumenta-
das mediante tarjetas de crédito, se considerarán los que resulten luego de imputar el
pago mínimo exigido en cada liquidación a cancelar la deuda en orden decreciente de an-
tigüedad.
Los deudores que hayan accedido a refinanciaciones de deudas encontrándose clasifica-
dos en niveles inferiores, sólo podrán incluirse en esta categoría en la medida en que se
hayan observado las pautas establecidas para cada uno de los correspondientes niveles
y, además, que el resto de sus deudas reúnan las condiciones para que el cliente pueda
ser recategorizado en este nivel.
Los deudores que hayan refinanciado sus deudas, aun no habiendo incurrido en atrasos
en el pago de sus servicios, podrán permanecer en esta categoría, cuando hayan accedi-
do, como máximo, a dos refinanciaciones, en el término de 12 meses, contados desde la
última refinanciación otorgada.
A esos efectos, no se considerará refinanciación la asistencia que se otorgue a los deu-
dores clasificados en esta categoría siempre que implique mayor deuda por capital –neto
de los intereses y accesorios que se capitalicen– respecto del importe adeudado con an-
terioridad por el mismo concepto y que se evalúe la capacidad de pago del deudor para
afrontar las obligaciones emergentes de esa ampliación del margen crediticio.
Los sobregiros en cuenta corriente bancaria por importes que excedan los márgenes de
utilización oportunamente acordados, o los que se ha
- entidades de la unidad:
  - `e1` Definicion: Situación normal — deudores — Categoría de clasificación que comprende los clientes que atienden en forma puntual el pago de sus obligaciones o con atrasos que no superan los 31 días.
  - `e2` Condicion: Atraso máximo 31 días — El cliente debe tener atrasos que no superen los 31 días para ser clasificado en situación normal.
  - `e3` Definicion: Adelantos transitorios — cumplimiento normal — Se considerarán de cumplimiento normal hasta los 61 días contados desde su otorgamiento.
  - `e4` Condicion: Plazo 61 días — adelantos transitorios — Los adelantos transitorios en cuenta corriente se consideran de cumplimiento normal dentro de este plazo.
  - `e5` Obligacion: Cálculo de atraso — tarjetas de crédito — Para financiaciones mediante tarjetas de crédito, los días de atraso se establecen considerando los que resulten luego de imputar el pago mínimo exigido en cada liquidación a cancelar la deuda en orde
  - `e6` Condicion: Refinanciación previa — recategorización — Para que deudores previamente clasificados en niveles inferiores puedan incluirse en situación normal tras refinanciación, deben haber observado las pautas de cada nivel y el resto de sus deudas debe 
  - `e7` Condicion: Máximo dos refinanciaciones en 12 meses — Deudores que refinanciaron sin incurrir en atrasos pueden permanecer en situación normal si accedieron a como máximo dos refinanciaciones en el término de 12 meses.
  - `e8` Excepcion: Excepción — ampliación de margen crediticio — No se considera refinanciación la asistencia a deudores en situación normal que implique mayor deuda por capital (neto de intereses y accesorios capitalizados) respecto del importe anterior, siempre q
  - `e9` Condicion: Condición — mayor deuda por capital — La asistencia debe implicar mayor deuda por capital (neto de intereses y accesorios capitalizados) respecto del importe anterior.
  - `e10` Condicion: Condición — evaluación de capacidad de pago — Debe evaluarse la capacidad de pago del deudor para afrontar las obligaciones emergentes de la ampliación del margen crediticio.
  - `e11` Excepcion: Excepción — sobregiros en cuenta corriente — Los sobregiros en cuenta corriente bancaria que excedan márgenes acordados o sin margen asignado no se consideran refinanciación si se cancelan dentro de 30 días.
  - `e12` Restriccion: Reclasificación — refinanciación en condiciones distintas — Si se verifican refinanciaciones en condiciones distintas a las excepciones señaladas, corresponderá la reclasificación del deudor como mínimo en el nivel inmediato inferior.
  - `e13` Operacion: Reclasificación de deudor — Cambio de categoría de clasificación del deudor a un nivel inmediato inferior cuando se verifican refinanciaciones en condiciones distintas a las permitidas.
- relaciones del crudo (sin establecida_en ni de sujeto): e2 condicion_de e1; e4 condicion_de e3; e6 condicion_de e1; e7 condicion_de e1; e9 condicion_de e8; e10 condicion_de e8; e12 limita e13
- NODOS A CLASIFICAR:
  - **caso 72** Excepcion `e11`: Excepción — sobregiros en cuenta corriente | descripcion: Los sobregiros en cuenta corriente bancaria que excedan márgenes acordados o sin margen asignado no se consideran refinanciación si se cancelan dentro de 30 días. | tramo: Los sobregiros en cuenta corriente bancaria por importes que excedan los márgenes de utilización oportunamente acordados, o los que se hayan efectivizado –cualquiera sea su importe– sin contar el cuentacorrentista con un margen previa y expresamente asignado, tampoco serán considerados refinanciación siempre que tales excesos se cancelen dentro de los 30 días.

## Unidad `ext::3.16.3.5` (item)
- herencia: [chapeau_seccion S3] Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas
en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–,
adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán
cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables. | [intro 3.16.3] operaciones con títulos valores y otros activos.
En el caso de que el cliente no sea una persona humana residente, la entidad deberá
contar con la conformidad previa del BCRA excepto que cuente con una declaración
jurada del cliente en la que deje constancia de que: | **[abre la lista]** [intersticial 3.16.3] En caso de que el cliente sea una persona jurídica, para que la operación no quede
comprendida por el requisito de conformidad previa, la entidad deberá contar
adicionalmente con una declaración jurada en la que conste:
- texto propio: 3.16.3.5. Lo previsto en los puntos 3.16.3.1. al 3.16.3.4. no resultará aplicable para
aquellas operaciones de egresos que correspondan a:
i) operaciones de clientes realizadas en el marco del punto 3.14.2.
ii) cancelaciones de financiaciones en moneda extranjera otorgadas por
entidades financieras locales, incluyendo los pagos por los consumos
en moneda extranjera efectuados mediante tarjetas de crédito o de
compra;
iii) operaciones comprendidas en el punto 3.13.1.4. en la medida que las
mismas sean cursadas en forma automática por la entidad en su
carácter de apoderada del beneficiario no residente.
iv) las repatriaciones de inversiones de portafolio de no residentes
cursadas en el marco de lo dispuesto en el punto 3.13.1.12.
Las entidades por sus operaciones propias en carácter de cliente deberán
dar cumplimiento sólo a lo previsto en los puntos 3.16.3.3. y 3.16.3.4.
- entidades de la unidad:
  - `e1` Excepcion: Excepción — operaciones punto 3.14.2 — No aplican los requisitos de declaración jurada de los puntos 3.16.3.1 a 3.16.3.4 para operaciones de clientes realizadas en el marco del punto 3.14.2
  - `e2` Excepcion: Excepción — cancelaciones de financiaciones en moneda extranjera — No aplican los requisitos de declaración jurada de los puntos 3.16.3.1 a 3.16.3.4 para cancelaciones de financiaciones en moneda extranjera otorgadas por entidades financieras locales, incluyendo pago
  - `e3` Excepcion: Excepción — operaciones punto 3.13.1.4 cursadas automáticamente — No aplican los requisitos de declaración jurada de los puntos 3.16.3.1 a 3.16.3.4 para operaciones del punto 3.13.1.4 cursadas automáticamente por la entidad como apoderada del beneficiario no residen
  - `e4` Excepcion: Excepción — repatriaciones de inversiones de portafolio — No aplican los requisitos de declaración jurada de los puntos 3.16.3.1 a 3.16.3.4 para repatriaciones de inversiones de portafolio de no residentes cursadas conforme al punto 3.13.1.12
  - `e5` Obligacion: Cumplimiento parcial — operaciones propias de entidades — Las entidades, por sus operaciones propias en carácter de cliente, deben cumplir solo con lo previsto en los puntos 3.16.3.3 y 3.16.3.4, quedando exceptuadas de los requisitos de los puntos 3.16.3.1 y
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 75** Excepcion `e3`: Excepción — operaciones punto 3.13.1.4 cursadas automáticamente | descripcion: No aplican los requisitos de declaración jurada de los puntos 3.16.3.1 a 3.16.3.4 para operaciones del punto 3.13.1.4 cursadas automáticamente por la entidad como apoderada del beneficiario no residente | tramo: Lo previsto en los puntos 3.16.3.1. al 3.16.3.4. no resultará aplicable para aquellas operaciones de egresos que correspondan a: iii) operaciones comprendidas en el punto 3.13.1.4. en la medida que las mismas sean cursadas en forma automática por la entidad en su carácter de apoderada del beneficiario no residente.

## Unidad `cla::7.1` (punto_no_item)
- herencia: [encabezado S7] Sección 7. Clasificación de los deudores de la cartera para consumo o vivienda.
- texto propio: 7.1. Criterio de clasificación.
Sin perjuicio de que los análisis previos al otorgamiento de las financiaciones y refinanciaciones
también deben guardar relación con la capacidad de pago de los deudores, evaluando la afec-
tación de sus ingresos periódicos por la totalidad de los compromisos de crédito asumidos, la
clasificación de estos clientes se efectuará considerando -al cabo de cada mes- exclusivamente
pautas objetivas vinculadas al grado de cumplimiento de las correspondientes obligaciones o su
situación jurídica, las informaciones que surjan de la “Central de deudores del sistema financie-
ro” –cuando reflejen niveles de calidad inferiores al asignado por la entidad–, de la base de
“Deudores en situación irregular de ex entidades financieras” y la situación que surja de la apli-
cación de las pautas de refinanciación. En caso de discrepancias, se deberá considerar la pau-
ta que indique el mayor nivel de riesgo de incobrabilidad.
Se entiende que el cumplimiento de las obligaciones a que se refieren las citadas pautas tiene
lugar cuando no se recurra a nuevas financiaciones o refinanciaciones destinadas a cancelar
obligaciones preexistentes, cualquiera sea la modalidad (prórrogas, esperas, ampliaciones de
plazo o márgenes -sean tales modalidades expresas o tácitas-, disminuciones en los importes
de las cuotas o pagos, renovaciones, reestructuraciones, etc.). En el caso de refinanciaciones,
a fin de determinar una mejora en la clasificación del deudor, corresponderá tener en cuenta las
pautas específicas previstas en cada una de las categorías.
A esos efectos, no se considerarán dentro de ese concepto las refinanciaciones otorgadas a
productores cuando ello resulte de la aplicación de disposiciones vinculadas a la Ley de Emer-
gencia Agropecuaria, sin perjuicio de
- entidades de la unidad:
  - `e1` Operacion: Clasificación de clientes de cartera consumo/vivienda — Clasificación de clientes de cartera para consumo o vivienda considerando pautas objetivas vinculadas al grado de cumplimiento de obligaciones o situación jurídica, evaluada al cabo de cada mes
  - `e2` Obligacion: Análisis previos al otorgamiento — capacidad de pago — Los análisis previos al otorgamiento de financiaciones y refinanciaciones deben guardar relación con la capacidad de pago de los deudores, evaluando la afectación de sus ingresos periódicos por la tot
  - `e3` Condicion: Información de Central de deudores — nivel inferior — Cuando las informaciones de la Central de deudores del sistema financiero reflejen niveles de calidad inferiores al asignado por la entidad
  - `e4` Condicion: Información de base de deudores en situación irregular — Información de la base de Deudores en situación irregular de ex entidades financieras
  - `e5` Condicion: Situación de aplicación de pautas de refinanciación — La situación que surja de la aplicación de las pautas de refinanciación
  - `e6` Restriccion: Discrepancias — aplicar pauta de mayor riesgo — En caso de discrepancias entre pautas de clasificación, debe considerarse la pauta que indique el mayor nivel de riesgo de incobrabilidad
  - `e7` Definicion: Cumplimiento de obligaciones — exclusión de nuevas financiaciones — El cumplimiento de obligaciones tiene lugar cuando no se recurra a nuevas financiaciones o refinanciaciones destinadas a cancelar obligaciones preexistentes, cualquiera sea la modalidad (prórrogas, es
  - `e8` Obligacion: Mejora de clasificación en refinanciaciones — pautas específicas — En refinanciaciones, para determinar mejora en la clasificación del deudor debe tenerse en cuenta las pautas específicas previstas en cada una de las categorías
  - `e9` Excepcion: Excepción refinanciaciones — productores Ley Emergencia Agropecuaria — No se consideran refinanciaciones las otorgadas a productores cuando resulten de la aplicación de disposiciones vinculadas a la Ley de Emergencia Agropecuaria
  - `e10` Restriccion: Productores Emergencia Agropecuaria — sin mejora por emergencia — El tratamiento en el marco de la Ley de Emergencia Agropecuaria no podrá implicar mejoramiento de clasificación en función de situación preexistente a la emergencia, ni extenderse más allá de la vigen
  - `e11` Obligacion: Mora en atraso — consideración al fin de emergencia — A los fines de la clasificación, debe tenerse en cuenta la mora en el atraso de obligaciones para el momento en que concluya la vigencia de la emergencia declarada
  - `e12` Obligacion: Mejora de clasificación en refinanciaciones — cuotas mínimas o porcentaje — Para determinar mejora en clasificación de deudor recategorizado por atraso en obligaciones refinanciadas, debe tenerse en cuenta cancelación de cuotas mínimas (pago periódico, mensual o bimestral) o 
  - `e13` Restriccion: Atraso mayor a 31 días — prohibición de mejora — No se podrán efectuar mejoras en clasificaciones de clientes que registren atraso mayor a 31 días en pago de obligaciones refinanciadas
  - `e14` Definicion: Cobros no aplicados y quitas — no computables para mejora — Los cobros no aplicados y quitas concedidas previamente a la refinanciación reducen el importe de la obligación sujeta a refinanciación y no son computables para mejora de clasificación según parámetr
  - `e15` Potestad: Imputación de cobros no aplicados y quitas — criterio de entidad — Cada entidad podrá optar por el criterio de imputación de cobros no aplicados y quitas a la cancelación de deuda objeto de refinanciación, sin perjuicio de otras disposiciones aplicables
  - `e16` Obligacion: Pagos anticipados — cómputo en cuotas o porcentaje — Pagos por adelantado y anticipos efectuados en oportunidad de refinanciación o posteriormente serán computados en término de cuotas o porcentaje de amortización de capital según modalidad de pago, en 
  - `e17` Definicion: Facilidades adicionales — no consideradas nuevas financiaciones — Facilidades adicionales sobre márgenes vigentes acordados que impliquen nuevos desembolsos y no superen el 10% del cupo de última evaluación crediticia, no se consideran nuevas financiaciones
  - `e18` Definicion: Renovaciones de crédito capital trabajo — no consideradas nuevas financiaciones — Renovaciones periódicas de crédito para capital de trabajo y nuevas financiaciones/refinanciaciones asociadas a mayor inversión por expansión de actividades no se consideran nuevas financiaciones
  - `e19` Condicion: Consistencia con curso normal de negocios — Facilidades y renovaciones deben ser consistentes con curso normal de negocios y debe existir capacidad para atender resto de obligaciones financieras
  - `e20` Condicion: Capacidad para atender obligaciones financieras — Debe existir capacidad para atender el resto de las obligaciones financieras
  - `e21` Excepcion: Excepción márgenes de crédito — no refinanciación si no se supera límite — Cuando márgenes de crédito por líneas específicas se excedan, no se consideran refinanciaciones si no se supera límite de asistencia máxima acordada por todo concepto según capacidad de pago
  - `e22` Excepcion: Excepción evaluación capacidad pago — métodos específicos o monto reducido — No es obligatoria evaluación de capacidad de pago por ingresos del prestatario cuando se utilicen métodos específicos de evaluación o se trate de deudores por préstamos de monto reducido
  - `e23` Potestad: Asistencia crediticia — no obsta evaluación de otras facilidades — El otorgamiento de asistencia crediticia de monto reducido no obsta a que para otras facilidades crediticias al mismo prestatario deba observarse evaluación de capacidad de pago
- relaciones del crudo (sin establecida_en ni de sujeto): e2 regula e1; e8 regula e1; e12 regula e1; e16 regula e1
- NODOS A CLASIFICAR:
  - **caso 80** Excepcion `e22`: Excepción evaluación capacidad pago — métodos específicos o monto reducido | descripcion: No es obligatoria evaluación de capacidad de pago por ingresos del prestatario cuando se utilicen métodos específicos de evaluación o se trate de deudores por préstamos de monto reducido | tramo: No será obligatoria la evaluación de la capacidad de pago en función de los ingresos del prestatario, en la medida en que se utilicen métodos específicos de evaluación o se trate de deudores por préstamos de monto reducido en los términos del punto 1.1.3.3. de las normas sobre "Gestión crediticia"

## Unidad `ext::8.5.17.10` (item)
- herencia: [intro 8.5] La entidad podrá considerar cumplimentado parcial o totalmente el seguimiento de un permiso
de embarque cuando cuente con los elementos que le permitan considerar que la operación
se encuentra en alguna de las situaciones detalladas a continuación y se verifiquen las
condiciones previstas en cada caso.
La documentación utilizada para certificar el concepto y monto de las divisas imputado en
cada caso deberá quedar archivada en la entidad a disposición del BCRA. | **[abre la lista]** [intro 8.5.17] Por el valor que corresponda a ventajas aduaneras u otras situaciones previstas en el
siguiente listado de operaciones:
- texto propio: 8.5.17.10. Régimen de corredores de comercio (Resolución 122/93 de la
Administración Nacional de Aduanas).
- entidades de la unidad:
  - `e1` Operacion: Operación aduanera — régimen de corredores de comercio — Operación aduanera exceptuada del seguimiento de divisas por exportaciones de bienes, conforme al régimen de corredores de comercio establecido por la Resolución 122/93 de la Administración Nacional d
  - `e2` Excepcion: Excepción — régimen de corredores de comercio — Operación aduanera exceptuada del seguimiento de divisas por exportaciones de bienes conforme al régimen de corredores de comercio
  - `e3` Comunicacion: Resolución 122/93 — 
- relaciones del crudo (sin establecida_en ni de sujeto): to referencia e3
- NODOS A CLASIFICAR:
  - **caso 94** Excepcion `e2`: Excepción — régimen de corredores de comercio | descripcion: Operación aduanera exceptuada del seguimiento de divisas por exportaciones de bienes conforme al régimen de corredores de comercio | tramo: Régimen de corredores de comercio (Resolución 122/93 de la Administración Nacional de Aduanas)

## Unidad `pro::2.3.4` (punto_no_item)
- herencia: [encabezado 2.3] 2.3. Recaudos mínimos de la relación de consumo.
- texto propio: 2.3.4. Cambios de condiciones pactadas.
A fin de modificar las condiciones pactadas debe darse la totalidad de las siguientes
condiciones:
i) En el contrato deberán encontrarse taxativamente especificadas las condiciones
que pueden ser objeto de modificación, así como los parámetros o criterios objeti-
vos para su concreción, ajustándose a lo señalado en el punto 2.3.2.
Los incrementos en las tasas de interés, comisiones y/o cargos, además, deben ser
justificados desde el punto de vista técnico y económico, en el marco de lo dispues-
to en el punto 2.3.2.1.
ii) La modificación no debe alterar el objeto del contrato ni importar un desmedro res-
pecto de los productos o servicios contratados.
iii) Consentimiento.
En el caso de que el sujeto obligado pretenda incorporar nuevos conceptos en cali-
dad de comisiones y/o cargos que no hubiesen sido previstos en el contrato o re-
ducir prestaciones contempladas en él, deberá previamente obtener el consenti-
miento expreso del usuario de servicios financieros.
Cuando se trate de modificaciones en los valores de comisiones y/o cargos debi-
damente aceptados por el usuario, su consentimiento al cambio podrá quedar con-
formado por la falta de objeción al mismo dentro del plazo establecido en el acápite
iv).
En los contratos de tarjeta de crédito el consentimiento a modificaciones en las
condiciones pactadas (nuevas comisiones y/o cargos) sólo puede ser dado por el ti-
tular de la cuenta.
iv) Notificaciones. Forma, plazos y efectos.
El usuario de servicios financieros debe ser notificado de las modificaciones que
aplicará el sujeto obligado con una antelación mínima de sesenta (60) días corridos
a su entrada en vigencia. Las modificaciones que resulten económicamente más
beneficiosas para el usuario –por una reducción de los valore
- entidades de la unidad:
  - `c1` Condicion: Especificación taxativa de condiciones modificables — Las condiciones que pueden ser objeto de modificación deben estar taxativamente especificadas en el contrato, junto con los parámetros o criterios objetivos para su concreción, conforme a lo señalado 
  - `o1` Obligacion: Justificación técnica y económica de incrementos en tasas e intereses — Los incrementos en las tasas de interés, comisiones y/o cargos deben ser justificados desde el punto de vista técnico y económico, conforme a lo dispuesto en el punto 2.3.2.1.
  - `r1` Restriccion: Prohibición de alterar objeto del contrato o desmejorar servicios — La modificación de condiciones pactadas no debe alterar el objeto del contrato ni importar un desmedro respecto de los productos o servicios contratados.
  - `o2` Obligacion: Consentimiento expreso para nuevas comisiones o reducción de prestaciones — El sujeto obligado debe obtener previamente el consentimiento expreso del usuario de servicios financieros cuando pretenda incorporar nuevos conceptos en calidad de comisiones y/o cargos no previstos 
  - `e1` Excepcion: Consentimiento por falta de objeción para cambios en valores de comisiones — Para modificaciones en los valores de comisiones y/o cargos debidamente aceptados por el usuario, el consentimiento puede quedar conformado por la falta de objeción dentro del plazo establecido en el 
  - `r2` Restriccion: Consentimiento a modificaciones en tarjeta de crédito solo del titular — En los contratos de tarjeta de crédito, el consentimiento a modificaciones en las condiciones pactadas (nuevas comisiones y/o cargos) solo puede ser dado por el titular de la cuenta.
  - `o3` Obligacion: Notificación con antelación mínima de 60 días — El usuario de servicios financieros debe ser notificado de las modificaciones que aplicará el sujeto obligado con una antelación mínima de sesenta (60) días corridos a su entrada en vigencia.
  - `e2` Excepcion: Excepción notificación para modificaciones económicamente beneficiosas — Las modificaciones que resulten económicamente más beneficiosas para el usuario por reducción de los valores pactados no requieren notificación anticipada.
  - `o4` Obligacion: Notificaciones de cambios de condiciones gratuitas — Las notificaciones por cambios de condiciones pactadas (nuevos conceptos y/o valores o reducción de prestaciones del servicio) deben ser gratuitas para el usuario de servicios financieros.
  - `o5` Obligacion: Forma de notificación: documento escrito o electrónico — Las notificaciones deben efectuarse mediante documento escrito dirigido al domicilio real del usuario, en forma separada de cualquier otra información que remita el sujeto obligado, o por vía electrón
  - `o6` Obligacion: Requisitos de notificación electrónica: claridad, acceso y fecha — Cuando la notificación sea por vía electrónica, debe ser clara, de fácil acceso para el usuario e incluir la fecha de emisión.
  - `o7` Obligacion: Inclusión de leyenda sobre derecho a rescindir — Las notificaciones deben incluir la leyenda: 'Usted podrá optar por rescindir el contrato en cualquier momento antes de la entrada en vigencia del cambio y sin cargo alguno, sin perjuicio de que deber
  - `o8` Obligacion: Inclusión de leyenda sobre Régimen de Transparencia — Las notificaciones deben incluir la leyenda que remite al Régimen de Transparencia del BCRA para comparar costos, características y requisitos de productos y servicios financieros.
  - `o9` Obligacion: Cuadro comparativo de comisiones modificadas — Cuando se modifique el valor de las comisiones especificadas, las notificaciones deben exhibir un cuadro comparativo elaborado y puesto a disposición por la SEFYC.
  - `d1` Definicion: Comisiones de caja de ahorros sujetas a cuadro comparativo — Emisión de tarjetas de débito adicionales; reposición de tarjetas de débito por robo o extravío y uso de cajeros automáticos (fuera de casas operativas de la entidad, de otra entidad y en el exterior)
  - `d2` Definicion: Comisiones de tarjetas de crédito sujetas a cuadro comparativo — Servicio de emisión, renovación, administración o mantenimiento de cuenta; reposición o reimpresión de tarjeta por robo o extravío y tarjetas adicionales.
  - `d3` Definicion: Comisiones específicas de cuenta corriente — Mantenimiento de cuenta y talonario de cheques.
  - `d4` Definicion: Paquete para beneficiarios de prestaciones de seguridad social — Paquete que incluye el servicio de adelanto de haberes jubilatorios, destinado a beneficiarios de prestaciones de la seguridad social.
  - `d5` Definicion: Servicio de mantenimiento de paquetes — Servicio de mantenimiento de paquetes.
  - `c2` Condicion: Concurrencia de todas las condiciones para modificación — Para que sea válida la modificación de condiciones pactadas, deben cumplirse la totalidad de las condiciones enumeradas (i, ii, iii y iv), no basta con alguna de ellas.
- relaciones del crudo (sin establecida_en ni de sujeto): c1 condicion_de c2; r1 condicion_de c2; o2 condicion_de c2; o3 condicion_de c2
- NODOS A CLASIFICAR:
  - **caso 103** Excepcion `e1`: Consentimiento por falta de objeción para cambios en valores de comisiones | descripcion: Para modificaciones en los valores de comisiones y/o cargos debidamente aceptados por el usuario, el consentimiento puede quedar conformado por la falta de objeción dentro del plazo establecido en el acápite iv). | tramo: Cuando se trate de modificaciones en los valores de comisiones y/o cargos debidamente aceptados por el usuario, su consentimiento al cambio podrá quedar conformado por la falta de objeción al mismo dentro del plazo establecido en el acápite iv).

## Unidad `cap::7.1.1.1` (punto_no_item)
- herencia: [chapeau_seccion S7] A los efectos de la aplicación de las disposiciones de la presente sección, las entidades financieras
se clasificarán en grupo 1 y grupo 2, conforme a lo previsto en la Sección 2. | [intro 7.1] Se determinará mensualmente por la siguiente expresión: | [intro 7.1] C = BIC x ILM | [intro 7.1] RO | [intro 7.1] Donde:
C : exigencia de capital por riesgo operacional. | [intro 7.1] RO | [intro 7.1] BIC: componente del indicador de negocio, que es el producto del indicador de negocio (BI) | [intro 7.1] por una serie de coeficientes marginales (α), calculado según lo previsto en el punto | [intro 7.1] i | [intro 7.1] 7.1.2. | [intro 7.1] ILM: multiplicador de pérdida interna igual a 1.
Los activos ponderados por riesgo (APR) para el riesgo operacional son iguales a 12,5 veces el
C . | [intro 7.1] RO | [intro 7.1.1] El BI es una aproximación al riesgo operacional a partir de la información de los estados
financieros. Se determinará por la siguiente expresión: | [intro 7.1.1] BI = VA (ILDC + SC + FC + RM ) | [intro 7.1.1] Prom Prom Prom Prom | [intro 7.1.1] ILDC : Componente de intereses, arrendamientos y dividendos. Se determinará por la | [intro 7.1.1] Prom | [intro 7.1.1] siguiente expresión:
Mín. [VA (ingresos por intereses – egresos por intereses);
5% x activos que devengan intereses] + ingresos por dividendos | [intro 7.1.1] SC : Componente de servicios. Se determinará por la siguiente expresión: | [intro 7.1.1] Prom | [intro 7.1.1] Máx. [otros ingresos por operaciones; otros egresos por operaciones] + Máx.
[ingresos por honorarios y comisiones; egresos por honorarios y comisiones] | [intro 7.1.1] FC : Componente financiero. Se determinará por la siguiente expresión: | [intro 7.1.1] Prom | [intro 7.1.1] VA (resultado neto de cartera de negociación) + VA (resultado neto de cartera
de inversión) | [intro 7.1.1] RM : Resultado monetario total | [intro 7.1.1] Prom | [intro 7.1.1] VA: Valor absoluto.
Cada término dentro de los 3 componentes y el resultado monetario debe ser calculado
como el promedio de los valores de los 3 últimos períodos consecutivos de 12 meses an-
teriores al mes en que se efectúa el cálculo, expresados en moneda homogénea al cierre
del período de cálculo de 36 meses: t, t-1 y t-2. Se debe determinar, en primer lugar, el
valor de las partidas netas que correspondan (por ejemplo, ingresos por intereses menos
egresos por intereses) para cada período de
- texto propio: 7.1.1.1. Definición de los componentes del indicador de negocio (BI):
i) Componente de intereses, arrendamientos y dividendos (ILDC).
a) Ingresos por intereses y ajustes por índices: es el total de los intereses y
ajustes generados por los activos financieros y por los arrendamientos fi-
nancieros.
Se incluyen, entre otros:
- Los intereses y ajustes generados por los instrumentos financieros me-
didos a costo amortizado –por ejemplo, los préstamos y adelantos– y a
valor razonable con cambios en otro resultado integral (ORI) y los ingre-
sos generados por los arrendamientos financieros.
- Los intereses de instrumentos financieros derivados contabilizados co-
mo coberturas –siempre que sean identificables–.
- Todo otro interés y ajuste generado por un activo.
b) Egresos por intereses: es el total de los intereses y ajustes generados por
los pasivos financieros y los intereses y ajustes correspondientes a los
arrendamientos financieros cuando la entidad sea arrendataria.
Se incluyen, entre otros:
- Los intereses y ajustes generados por los instrumentos financieros me-
didos a costo amortizado –por ejemplo, los depósitos– y a valor razona-
ble con cambios en otro resultado integral (ORI) y los egresos genera-
dos por los arrendamientos financieros.
- Los intereses de instrumentos financieros derivados contabilizados co-
mo coberturas –siempre que sean identificables–.
- Todo otro interés y ajuste generado por un pasivo.
c) Activos que devengan intereses: importe bruto al cierre del mes anterior al
que se efectúa el cálculo para cada uno de los 3 años del total de los acti-
vos a tasa de interés o ajustes asimilables –aunque estuvieran en mora y
se hubiera suspendido el devengamiento de los accesorios– y de los acti-
vos dados en arrendamiento financiero. No se computan las 
- entidades de la unidad:
  - `e1` Definicion: ILDC — Componente de intereses, arrendamientos y dividendos — Comprende: (a) ingresos por intereses y ajustes generados por activos financieros y arrendamientos financieros, incluyendo instrumentos a costo amortizado, a valor razonable con cambios en ORI, deriva
  - `e2` Definicion: SC — Componente de servicios — Comprende: (a) ingresos por honorarios y comisiones: ingresos por asesoramiento y prestación de servicios, incluso a través de terceros, incluyendo servicios por cuenta de clientes relacionados con em
  - `e3` Definicion: FC — Componente financiero — Comprende: (a) resultado neto de la cartera de negociación (conforme a lo establecido en punto 6.1.2), conformado por el resultado neto de activos y pasivos mantenidos para negociación (títulos de deu
  - `e4` Definicion: RM — Resultado monetario total — Resultado monetario total, no medido en valores absolutos.
  - `e5` Restriccion: Exclusión — Negocios de seguros o reaseguros — Las siguientes partidas no contribuyen a ninguna de las partidas del BI: ingresos y gastos de negocios de seguros o reaseguros, que se realizan en carácter de agente institorio o a través de subsidiar
  - `e6` Restriccion: Exclusión — Pago de pólizas y cobro de indemnizaciones — Las siguientes partidas no contribuyen a ninguna de las partidas del BI: pago de pólizas y cobro de indemnizaciones por las coberturas de seguros o reaseguros.
  - `e7` Restriccion: Exclusión — Gastos administrativos — Las siguientes partidas no contribuyen a ninguna de las partidas del BI: gastos administrativos, incluidos gastos de personal, comisiones pagadas por la contratación externa de servicios no financiero
  - `e8` Restriccion: Exclusión — Recupero de gastos administrativos — Las siguientes partidas no contribuyen a ninguna de las partidas del BI: recupero de gastos administrativos, incluido el recupero de pagos efectuados por cuenta de clientes (tales como impuestos pagad
  - `e9` Restriccion: Exclusión — Gastos en inmuebles y activos fijos — Las siguientes partidas no contribuyen a ninguna de las partidas del BI: gastos en inmuebles y otros activos fijos, excepto los derivados de eventos de pérdida por riesgo operacional.
  - `e10` Excepcion: Excepción — Gastos en inmuebles por pérdida operacional — Gastos en inmuebles y otros activos fijos derivados de eventos de pérdida por riesgo operacional sí contribuyen a las partidas del BI.
  - `e11` Restriccion: Exclusión — Depreciación o amortización — Las siguientes partidas no contribuyen a ninguna de las partidas del BI: depreciación o amortización de activos tangibles e intangibles.
  - `e12` Restriccion: Exclusión — Provisiones por compromisos — Las siguientes partidas no contribuyen a ninguna de las partidas del BI: provisiones por compromisos asumidos o sus reversiones, salvo provisiones relacionadas con eventos de pérdidas por riesgo opera
  - `e13` Excepcion: Excepción — Provisiones por riesgo operacional — Provisiones relacionadas con eventos de pérdidas por riesgo operacional sí contribuyen a las partidas del BI.
  - `e14` Restriccion: Exclusión — Deterioro de activos — Las siguientes partidas no contribuyen a ninguna de las partidas del BI: deterioro del valor de activos financieros y no financieros o sus reversiones, inversiones en subsidiarias, joint ventures o as
  - `e15` Restriccion: Exclusión — Cambios en llave de negocios — Las siguientes partidas no contribuyen a ninguna de las partidas del BI: cambios en la llave de negocios reconocidos en resultados.
  - `e16` Restriccion: Exclusión — Impuesto a las ganancias — Las siguientes partidas no contribuyen a ninguna de las partidas del BI: impuesto a las ganancias corriente y diferido.
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 105** Excepcion `e13`: Excepción — Provisiones por riesgo operacional | descripcion: Provisiones relacionadas con eventos de pérdidas por riesgo operacional sí contribuyen a las partidas del BI. | tramo: salvo provisiones relacionadas con eventos de pérdidas por riesgo operacional

## Unidad `ctacte::5.1.1::cierre` (cierre)
- herencia: [encabezado 5.1.1] 5.1.1. Límite.
- texto propio: Se exceptúan de las limitaciones establecidas en este punto a los endosos que las enti-
dades financieras realicen para la obtención de financiación, a favor de una entidad fi-
nanciera o de un fiduciario de un fideicomiso financiero, en ambos casos comprendidos
en la Ley de Entidades Financieras y las sucesivas transmisiones a favor de otros sujetos
de la misma naturaleza, así como cuando los cheques se depositen en la Caja de Valo-
res S.A. para ser negociados en las bolsas de comercio y mercados de valores autoriza-
dos por la Comisión Nacional de Valores de la República Argentina, en cuyo caso los en-
dosos deberán ser extendidos con la cláusula “... para su negociación en mercados de
valores”. También se exceptuarán de la citada limitación los endosos a favor del BCRA y
aquellos efectuados en los ECHEQ.
- entidades de la unidad:
  - `e1` Excepcion: Excepción endosos para financiación — Quedan exceptuados de los límites de endosos los que las entidades financieras realicen para obtener financiación a favor de otra entidad financiera o de un fiduciario de fideicomiso financiero compre
  - `e2` Excepcion: Excepción endosos para negociación en mercados de valores — Quedan exceptuados los endosos cuando los cheques se depositen en la Caja de Valores S.A. para negociación en bolsas de comercio y mercados de valores autorizados por la CNV, debiendo extenderse los e
  - `e3` Excepcion: Excepción endosos a favor del BCRA — Quedan exceptuados los endosos a favor del BCRA de las limitaciones establecidas en el punto.
  - `e4` Excepcion: Excepción endosos en ECHEQ — Quedan exceptuados los endosos efectuados en los ECHEQ de las limitaciones establecidas en el punto.
  - `e5` Obligacion: Cláusula obligatoria en endosos para mercados de valores — Los endosos de cheques depositados en la Caja de Valores S.A. para negociación en mercados de valores deben extenderse con la cláusula "... para su negociación en mercados de valores".
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 113** Excepcion `e3`: Excepción endosos a favor del BCRA | descripcion: Quedan exceptuados los endosos a favor del BCRA de las limitaciones establecidas en el punto. | tramo: También se exceptuarán de la citada limitación los endosos a favor del BCRA

## Unidad `ric::11.1::intro` (intro)
- herencia: [encabezado 11.1] 11.1. Normas de procedimiento.
- texto propio: Conceptos comprendidos.
Se incluirán los flujos de fondos nocionales futuros sujetos a reapreciación de activos, pasi-
vos y partidas fuera de balance sensibles a variaciones en la tasa de interés.
Conceptos excluidos.
- Activos que se deducen del capital ordinario del nivel 1 (COn1);
- Activos fijos;
- Posiciones en acciones en la cartera de inversión.
Frecuencia y consolidación.
Los datos se informarán con frecuencia trimestral y se integrarán con los datos correspon-
dientes al último mes de cada trimestre (marzo, junio, septiembre y diciembre), sobre base
individual y consolidada mensual. Serán aplicables los siguientes códigos de consolidación
definidos en la Sección 2.:
Base individual (código de consolidación 0 o 1);
Base consolidada (código de consolidación 2).
Se regirá por los plazos de presentación previstos para el régimen informativo contable men-
sual correspondiente al mes siguiente al del cierre de cada trimestre.
- entidades de la unidad:
  - `e1` Definicion: Conceptos comprendidos — flujos nocionales — Flujos de fondos nocionales futuros sujetos a reapreciación de activos, pasivos y partidas fuera de balance sensibles a variaciones en la tasa de interés.
  - `e2` Excepcion: Exclusión — activos deducidos del capital ordinario nivel 1 — Quedan excluidos de los conceptos comprendidos los activos que se deducen del capital ordinario del nivel 1 (COn1).
  - `e3` Excepcion: Exclusión — activos fijos — Quedan excluidos de los conceptos comprendidos los activos fijos.
  - `e4` Excepcion: Exclusión — posiciones en acciones cartera inversión — Quedan excluidas de los conceptos comprendidos las posiciones en acciones en la cartera de inversión.
  - `e5` Obligacion: Presentación trimestral — datos con consolidación — Los datos se informarán con frecuencia trimestral, integrándose con los datos correspondientes al último mes de cada trimestre (marzo, junio, septiembre y diciembre), sobre base individual y consolida
  - `e6` Definicion: Base individual — código consolidación 0 o 1 — Base individual se identifica con código de consolidación 0 o 1.
  - `e7` Definicion: Base consolidada — código consolidación 2 — Base consolidada se identifica con código de consolidación 2.
  - `e8` Obligacion: Cumplimiento plazos — régimen informativo contable mensual — La presentación se regirá por los plazos de presentación previstos para el régimen informativo contable mensual correspondiente al mes siguiente al del cierre de cada trimestre.
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 120** Excepcion `e3`: Exclusión — activos fijos | descripcion: Quedan excluidos de los conceptos comprendidos los activos fijos. | tramo: Activos fijos

## Unidad `ctacte::4.4.2` (punto_no_item)
- herencia: [encabezado 4.4] 4.4. Aval.
- texto propio: 4.4.2. Cuando la entidad depositaria avale cheques de pago diferido presentados por su inter-
medio y registrados sin aval por la entidad girada, aquélla emitirá los pertinentes certifi-
cados nominativos transferibles. Los certificados de que se trata podrán extenderse –a
solicitud del depositante de los cheques– en forma individual por cada uno de ellos o por
un conjunto.
- entidades de la unidad:
  - `e1` Operacion: Aval de cheques de pago diferido — La entidad depositaria avala cheques de pago diferido presentados por su intermedio y registrados sin aval por la entidad girada.
  - `e2` Obligacion: Emisión de certificados nominativos transferibles — La entidad depositaria emitirá los pertinentes certificados nominativos transferibles cuando avale cheques de pago diferido presentados por su intermedio y registrados sin aval por la entidad girada.
  - `e3` Potestad: Extensión de certificados individual o conjunta — Los certificados podrán extenderse a solicitud del depositante de los cheques en forma individual por cada uno de ellos o por un conjunto.
  - `e4` Condicion: Aval de cheques sin aval previo de la entidad girada — Los cheques de pago diferido deben estar registrados sin aval por la entidad girada.
- relaciones del crudo (sin establecida_en ni de sujeto): e2 condiciona e1
- NODOS A CLASIFICAR:
  - **caso 146** Condicion `e4`: Aval de cheques sin aval previo de la entidad girada | descripcion: Los cheques de pago diferido deben estar registrados sin aval por la entidad girada. | tramo: registrados sin aval por la entidad girada

## Unidad `cap::5.2.3.3` (punto_no_item)
- herencia: [chapeau_seccion S5] A los efectos del cómputo de la exigencia de capital por riesgo de crédito, se reconocerá –total o
parcialmente– la cobertura del riesgo de crédito (CRC) de las operaciones registradas en la cartera
de inversión –tales como préstamos y responsabilidades eventuales– mediante la utilización de las
técnicas previstas en el punto 5.1.
La presente sección contempla, además, el cálculo de la exposición a las operaciones de financia-
ción con títulos valores (securities financing transactions, SFT) –co | [intro 5.2.3] rantías) personales y derivados de crédito.
- texto propio: 5.2.3.3. Requisitos operativos específicos para los derivados de crédito.
i) Los eventos de crédito especificados por las partes contratantes deberán
incluir, como mínimo: a) falta de pago de los importes vencidos según los
términos de la obligación subyacente que se encuentren vigentes al mo-
mento de producirse dicha falta de pago –pudiendo prever un período de
gracia cuando la obligación subyacente así lo contemple, en cuyo caso am-
bos períodos deberán estar en consonancia–; b) apertura de concurso pre-
ventivo, acuerdo preventivo extrajudicial, quiebra, insolvencia o incapacidad
del deudor para hacer frente a sus deudas, o su impago o la aceptación por
escrito de su incapacidad generalizada para satisfacerlas a su vencimiento
–así como eventos similares–; y c) reestructuración de la obligación subya-
cente que involucre la condonación o el aplazamiento del pago del capital,
los intereses y/o las comisiones, y que implique una pérdida.
ii) Se admitirá que el derivado de crédito cubra obligaciones que no incluyen la
obligación subyacente, es decir que exista un descalce entre esta última y la
obligación de referencia del derivado de crédito –obligación utilizada a efec-
tos de determinar el monto del efectivo a liquidar o la obligación a entregar–
siempre que: a) la obligación de referencia sea de categoría similar o inferior
a la obligación subyacente; b) ambas estén emitidas por el mismo deudor; y
c) existan cláusulas recíprocas en caso de incumplimiento o cláusulas recí-
procas de aceleración legalmente exigibles.
iii) El período de vigencia del derivado de crédito no podrá ser inferior a cual-
quier período de gracia necesario para poder determinar que efectivamente
se ha producido el incumplimiento de la obligación subyacente debido a su
impago.
iv) Los derivado
- entidades de la unidad:
  - `e1` Obligacion: Especificación de eventos de crédito en derivados — Las partes contratantes de derivados de crédito deben especificar eventos de crédito que incluyan como mínimo: falta de pago de importes vencidos (con posibilidad de período de gracia en consonancia c
  - `e2` Condicion: Descalce entre obligación subyacente y de referencia — El derivado de crédito puede cubrir obligaciones distintas de la subyacente (descalce) cuando: la obligación de referencia sea de categoría similar o inferior a la subyacente, ambas sean emitidas por 
  - `e3` Restriccion: Período de vigencia mínimo del derivado de crédito — El período de vigencia del derivado de crédito debe ser suficiente para determinar si se ha producido el incumplimiento de la obligación subyacente por impago, considerando cualquier período de gracia
  - `e4` Obligacion: Proceso de valuación para derivados con liquidación en efectivo — Para derivados de crédito con liquidación en efectivo, debe existir un sólido proceso de valuación que permita estimar la pérdida fehacientemente, y debe establecerse con exactitud el período durante 
  - `e5` Condicion: Aplicación de requisitos cuando obligación de referencia difiere de subyacente — Cuando la obligación de referencia para liquidación en efectivo sea distinta de la obligación subyacente, aplican los requisitos del acápite ii) (descalce entre obligaciones).
  - `e6` Obligacion: Transferencia de obligación subyacente al proveedor de protección — Cuando la liquidación de la protección crediticia requiera transferencia de la obligación subyacente, los términos de esa obligación deben permitir que el consentimiento para la transferencia no pueda
  - `e7` Obligacion: Identificación de responsables de determinar evento de crédito — Debe identificarse claramente a las partes responsables de determinar si ocurrió un evento de crédito. La responsabilidad no recae solo en el vendedor de protección; el comprador puede informar al ven
  - `e8` Condicion: Descalce en obligación para determinar evento de crédito — Se permite descalce entre la obligación subyacente y la utilizada para determinar evento de crédito cuando: la obligación sea de categoría similar o inferior a la subyacente, ambas sean emitidas por e
  - `e9` Excepcion: Reconocimiento parcial cuando reestructuración no está contemplada — Se permite reconocimiento parcial del derivado de crédito cuando la reestructuración de la obligación subyacente no esté contemplada pero se cumplan los demás requisitos de los acápites i) a vii).
  - `e10` Restriccion: Límite de reconocimiento cuando derivado es inferior a obligación — Cuando el importe del derivado de crédito es inferior o igual al de la obligación subyacente, puede computarse como máximo el 60% del valor de la cobertura.
  - `e11` Restriccion: Límite de reconocimiento cuando derivado es superior a obligación — Cuando el importe del derivado de crédito es superior al de la obligación subyacente, puede computarse como cobertura como máximo el 60% del valor de la obligación subyacente.
  - `e12` Restriccion: Reconocimiento de swaps de incumplimiento crediticio y rendimiento total — Solo se reconocen swaps de incumplimiento crediticio y de rendimiento total que brinden protección crediticia equivalente a garantías.
  - `e13` Excepcion: Excepción a reconocimiento de swaps de retorno total — No se reconoce la protección crediticia cuando una entidad financiera compra protección mediante swap de retorno total, contabiliza como renta neta los pagos netos recibidos, pero no contabiliza el de
  - `e14` Restriccion: Prohibición de reconocimiento de otros derivados de crédito — No se reconocen como cobertura del riesgo de crédito otros tipos de derivados de crédito, incluyendo derivados de primer y/o enésimo incumplimiento (first-to-default o nth-to-default).
- relaciones del crudo (sin establecida_en ni de sujeto): e13 exceptua e12
- NODOS A CLASIFICAR:
  - **caso 173** Condicion `e8`: Descalce en obligación para determinar evento de crédito | descripcion: Se permite descalce entre la obligación subyacente y la utilizada para determinar evento de crédito cuando: la obligación sea de categoría similar o inferior a la subyacente, ambas sean emitidas por el mismo deudor, y existan cláusulas recíprocas legalmente exigibles de incumplimiento cruzado o aceleración cruzada. | tramo: Se permite un descalce entre la obligación subyacente y la obligación utilizada a efectos de determinar si ha ocurrido un evento de crédito siempre que: a) esta última sea de categoría similar o inferior a la obligación subyacente, b) ambas obligaciones estén emitidas por el mismo deudor, y c) existan cláusulas recíprocas legalmente exigibles de incumplimiento cruzado o de aceleración cruzada.

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
  - **caso 182** Condicion `e1`: Exportador sin permisos vencidos a emisión | descripcion: El exportador no registra a la fecha de emisión permisos con plazo vencido para el ingreso y liquidación de las divisas en situación de incumplimiento | tramo: El exportador no registra a la fecha de emisión permisos con plazo vencido para el ingreso y liquidación de las divisas en situación de incumplimiento

## Unidad `cap::2.5.5` (punto_no_item)
- herencia: [chapeau_seccion S2] A los efectos de la aplicación de las disposiciones de la presente sección, las entidades financieras
se clasificarán en:
i)Grupo 1: entidades calificadas por el BCRA como de importancia sistémica a nivel local | [chapeau_seccion S2] (D-SIB) y sucursales o subsidiarias de bancos del exterior calificados como de impor-
tancia sistémica global (G-SIB). | [chapeau_seccion S2] ii) Grupo 2: entidades financieras no comprendidas en el acápite i).
En aquellos casos en que no se establezcan disposiciones específicas para cada uno de los citados
grupos de entidades financieras, deberá aplicarse el mismo tratamiento a ambos grupos.
Las entidades financieras que presenten cambios en su calificación –conforme a lo previsto en los
acápites precedentes–, contarán con un plazo de 6 meses para aplicar las disposiciones específicas
correspondientes al nuevo grupo al que pertenezca | [encabezado 2.5] 2.5. Criterios para la determinación de los activos ponderados por riesgo.
- texto propio: 2.5.5. El término “exposición” abarca a todas las financiaciones otorgadas por la entidad –en
sus distintas modalidades, tales como préstamos, tenencias de títulos valores, fianzas,
avales y demás responsabilidades eventuales–, incluidas las que provengan de opera-
ciones realizadas en los mercados de títulos valores, de monedas y de derivados.
En el caso de exposiciones a entidades financieras, exposiciones a empresas, exposi-
ciones minoristas, exposiciones con garantía hipotecaria, exposiciones en situación de
incumplimiento y exposiciones a instrumentos, deberá tenerse en cuenta las disposicio-
nes específicas de los puntos 2.6., 2.7., 2.8., 2.9., 2.10. y 2.11., respectivamente.
A fin de determinar el importe de las financiaciones comprendidas en la exposición al
sector público no financiero, respecto de los títulos públicos nacionales que cuenten con
cotización normal y habitual por importes significativos en mercados del país que se
apliquen a operaciones de pase pasivo en pesos y que estén fondeados con depósitos
de esos títulos públicos, se observará el criterio de posición neta de títulos previsto en el
TO sobre Financiamiento al Sector Público no Financiero.
Las exposiciones incluirán los saldos de deuda y los compromisos eventuales multipli-
cados por el correspondiente factor de conversión crediticia (CCF).
- entidades de la unidad:
  - `e1` Definicion: Exposición — financiaciones otorgadas — Todas las financiaciones otorgadas por la entidad en sus distintas modalidades (préstamos, tenencias de títulos valores, fianzas, avales y demás responsabilidades eventuales), incluidas las que proven
  - `e2` Condicion: Exposiciones a entidades financieras — aplicación de disposiciones específicas — Cuando se trate de exposiciones a entidades financieras, deben aplicarse las disposiciones específicas del punto 2.6.
  - `e3` Condicion: Exposiciones a empresas — aplicación de disposiciones específicas — Cuando se trate de exposiciones a empresas, deben aplicarse las disposiciones específicas del punto 2.7.
  - `e4` Condicion: Exposiciones minoristas — aplicación de disposiciones específicas — Cuando se trate de exposiciones minoristas, deben aplicarse las disposiciones específicas del punto 2.8.
  - `e5` Condicion: Exposiciones con garantía hipotecaria — aplicación de disposiciones específicas — Cuando se trate de exposiciones con garantía hipotecaria, deben aplicarse las disposiciones específicas del punto 2.9.
  - `e6` Condicion: Exposiciones en situación de incumplimiento — aplicación de disposiciones específicas — Cuando se trate de exposiciones en situación de incumplimiento, deben aplicarse las disposiciones específicas del punto 2.10.
  - `e7` Condicion: Exposiciones a instrumentos — aplicación de disposiciones específicas — Cuando se trate de exposiciones a instrumentos, deben aplicarse las disposiciones específicas del punto 2.11.
  - `e8` Obligacion: Observar criterio de posición neta — títulos públicos nacionales — Observar el criterio de posición neta de títulos previsto en el TO sobre Financiamiento al Sector Público no Financiero para determinar el importe de las financiaciones comprendidas en la exposición a
  - `e9` Obligacion: Incluir saldos de deuda y compromisos eventuales — factor de conversión crediticia — Las exposiciones incluirán los saldos de deuda y los compromisos eventuales multiplicados por el correspondiente factor de conversión crediticia (CCF).
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 184** Condicion `e2`: Exposiciones a entidades financieras — aplicación de disposiciones específicas | descripcion: Cuando se trate de exposiciones a entidades financieras, deben aplicarse las disposiciones específicas del punto 2.6. | tramo: En el caso de exposiciones a entidades financieras

## Unidad `polcre::7.1.2` (item)
- herencia: **[abre la lista]** [intro 7.1] Se encuentran comprendidos en la categoría de “Grandes empresas exportadoras” los clientes
del sector privado no financiero que reúnan concurrentemente las siguientes condiciones: | [cierre 7.1] Cuando el cliente reúna la condición del punto 7.1.1. pero el importe total de sus financiaciones
en pesos en el sistema financiero no supere el importe de $ 30.000 millones y no haya mante-
nido pases y/o cauciones bursátiles tomadas –en pesos– durante los últimos 90 días corridos,
la entidad financiera podrá otorgarle nuevas financiaciones en la medida que con tales desem-
bolsos no se supere ese importe.
Cuando se trate de conjuntos económicos se los considerará como un solo cliente, a cuyo
e
- texto propio: 7.1.2. Mantengan un importe total de financiaciones alcanzadas en pesos en el conjunto del
sistema financiero que supere el monto de $ 30.000 millones, y/o pases y/o cauciones
bursátiles tomadas –en pesos– cualquiera sea su importe durante los últimos 90 días
corridos.
Las financiaciones alcanzadas serán aquellas que hayan implicado desembolsos de
fondos, así como el importe no utilizado del límite de crédito asignado para adelantos en
cuenta corriente. Se computará su saldo de capital a fin del mes anterior al que corres-
ponda su determinación.
Cuando un cliente manifieste por declaración jurada que no se encuadra en la categoría
de “Gran empresa exportadora” y, de la información disponible en la “Central de deudo-
res del sistema financiero”, surja que supera el importe de $ 30.000 millones, deberá
presentar una certificación extendida por Auditor Externo o Contador Público indepen-
diente (con firma debidamente certificada por el respectivo Consejo Profesional de
Ciencias Económicas) en la que se detallen las financiaciones en pesos y moneda ex-
tranjera en el conjunto de las entidades financieras, desagregando los datos correspon-
dientes a cada uno de esos intermediarios a la fecha a la cual se refiera, y los citados
pases y cauciones bursátiles tomados –en pesos– durante los últimos 90 días corridos.
Lo previsto en este párrafo no será de aplicación cuando el cliente reúna la condición de
MiPyME –de acuerdo con las normas sobre “Determinación de la condición de micro,
pequeña y mediana empresa”–.
Esa certificación mantendrá vigencia durante 90 días corridos desde la fecha a la cual
se refiera, sin perjuicio de la presentación de una nueva certificación en caso de corres-
ponder.
- entidades de la unidad:
  - `c1` Condicion: Importe total financiaciones pesos supera $ 30.000 millones — El cliente mantiene un importe total de financiaciones alcanzadas en pesos en el conjunto del sistema financiero que supera el monto de $ 30.000 millones
  - `c2` Condicion: Pases y/o cauciones bursátiles tomadas en pesos últimos 90 días — El cliente ha mantenido pases y/o cauciones bursátiles tomadas en pesos durante los últimos 90 días corridos, cualquiera sea su importe
  - `d1` Definicion: Financiaciones alcanzadas — Aquellas que hayan implicado desembolsos de fondos, así como el importe no utilizado del límite de crédito asignado para adelantos en cuenta corriente
  - `o1` Obligacion: Presentar certificación de Auditor Externo o Contador Público — El cliente debe presentar una certificación extendida por Auditor Externo o Contador Público independiente (con firma debidamente certificada por el respectivo Consejo Profesional de Ciencias Económic
  - `c3` Condicion: Cliente manifiesta por declaración jurada no encuadrarse en categoría — El cliente manifiesta por declaración jurada que no se encuadra en la categoría de Gran empresa exportadora y de la información disponible en la Central de deudores del sistema financiero surge que su
  - `e1` Excepcion: Excepción para clientes MiPyME — La obligación de presentar certificación no aplica cuando el cliente reúna la condición de MiPyME de acuerdo con las normas sobre Determinación de la condición de micro, pequeña y mediana empresa
  - `c4` Condicion: Vigencia de certificación 90 días corridos — La certificación mantiene vigencia durante 90 días corridos desde la fecha a la cual se refiera
- relaciones del crudo (sin establecida_en ni de sujeto): c3 condicion_de o1; e1 exceptua_obligacion o1
- NODOS A CLASIFICAR:
  - **caso 192** Condicion `c1`: Importe total financiaciones pesos supera $ 30.000 millones | descripcion: El cliente mantiene un importe total de financiaciones alcanzadas en pesos en el conjunto del sistema financiero que supera el monto de $ 30.000 millones | tramo: un importe total de financiaciones alcanzadas en pesos en el conjunto del sistema financiero que supere el monto de $ 30.000 millones

## Unidad `ext::9.3.1.2` (item)
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
- texto propio: 9.3.1.2. Que el monto a certificar por una aplicación a la cancelación del capital
sea menor o igual al saldo liquidado pendiente de aplicación que registra
la entidad para la operación en cuestión.
En caso de tratarse de una operación del exterior liquidada parcialmente
durante las respectivas vigencias de los Decretos 492/23, 549/23, 597/23
y 28/23, también se podrá emitir certificaciones por la porción no liquidada
en la medida que se verifique lo previsto en el punto 7.3.11.
- entidades de la unidad:
  - `e1` Condicion: Monto a certificar menor o igual al saldo liquidado — El monto a certificar por una aplicación a la cancelación del capital debe ser menor o igual al saldo liquidado pendiente de aplicación que registra la entidad para la operación en cuestión.
  - `e2` Excepcion: Excepción operaciones del exterior liquidadas parcialmente — Se permite emitir certificaciones por la porción no liquidada de operaciones del exterior liquidadas parcialmente durante las vigencias de los Decretos 492/23, 549/23, 597/23 y 28/23, siempre que se v
  - `e3` Condicion: Verificación de lo previsto en punto 7.3.11 — Condición de que se verifique lo previsto en el punto 7.3.11 para la emisión de certificaciones por la porción no liquidada.
- relaciones del crudo (sin establecida_en ni de sujeto): e3 condicion_de e2
- NODOS A CLASIFICAR:
  - **caso 201** Condicion `e1`: Monto a certificar menor o igual al saldo liquidado | descripcion: El monto a certificar por una aplicación a la cancelación del capital debe ser menor o igual al saldo liquidado pendiente de aplicación que registra la entidad para la operación en cuestión. | tramo: Que el monto a certificar por una aplicación a la cancelación del capital sea menor o igual al saldo liquidado pendiente de aplicación que registra la entidad para la operación en cuestión

## Unidad `cap::7.1.2` (punto_no_item)
- herencia: [chapeau_seccion S7] A los efectos de la aplicación de las disposiciones de la presente sección, las entidades financieras
se clasificarán en grupo 1 y grupo 2, conforme a lo previsto en la Sección 2. | [intro 7.1] Se determinará mensualmente por la siguiente expresión: | [intro 7.1] C = BIC x ILM | [intro 7.1] RO | [intro 7.1] Donde:
C : exigencia de capital por riesgo operacional. | [intro 7.1] RO | [intro 7.1] BIC: componente del indicador de negocio, que es el producto del indicador de negocio (BI) | [intro 7.1] por una serie de coeficientes marginales (α), calculado según lo previsto en el punto | [intro 7.1] i | [intro 7.1] 7.1.2. | [intro 7.1] ILM: multiplicador de pérdida interna igual a 1.
Los activos ponderados por riesgo (APR) para el riesgo operacional son iguales a 12,5 veces el
C . | [intro 7.1] RO
- texto propio: 7.1.2. Componente del indicador de negocio (BIC).
Se determinará por la siguiente expresión:
BIC = ∑ BI x α
i i
donde los coeficientes marginales (α) se determinarán en función del tramo del BI:
i
[TABLA cap::tabla038 | página 150 | e0_tablas | columnas]
Columnas: Categoría | Tramo de BI (en miles de millones de euros*) | Coeficientes marginales de BI (α) i
Fila 1: Categoría = 1 | Tramo de BI (en miles de millones de euros*) = ≤ 1 | Coeficientes marginales de BI (α) i = 12%
Fila 2: Categoría = 2 | Tramo de BI (en miles de millones de euros*) = 1 < BI ≤ 30 | Coeficientes marginales de BI (α) i = 15%
Fila 3: Categoría = 3 | Tramo de BI (en miles de millones de euros*) = >30 | Coeficientes marginales de BI (α) i = 18%
[FIN TABLA cap::tabla038]
* En línea con los estándares internacionales. Deberá calcularse el importe equivalente
en pesos al tipo de cambio vendedor del Banco de la Nación Argentina al cierre de las
operaciones del último día hábil del mes anterior del que se trate.
Los coeficientes marginales aumentan conforme se incrementa el tamaño del BI. Para las
entidades incluidas en la categoría 1 (BI igual o inferior al equivalente en pesos de
€1.000 millones), el BIC equivale al BI x 12%. El incremento marginal del BIC derivado
del aumento de una unidad del BI es del 12% en la categoría 1, del 15% en la categoría 2
y del 18% en la categoría 3.
- entidades de la unidad:
  - `e1` Operacion: Cálculo de BIC por tramos de BI — Cálculo del componente del indicador de negocio (BIC) como suma del producto del indicador de negocio (BI) por coeficientes marginales (α) según el tramo de BI: categoría 1 (BI ≤ €1.000 millones equiv
  - `e2` Obligacion: Conversión de BI a pesos — tipo de cambio vendedor BNA — Deberá calcularse el importe equivalente en pesos al tipo de cambio vendedor del Banco de la Nación Argentina al cierre de las operaciones del último día hábil del mes anterior del que se trate, para 
  - `e3` Definicion: Coeficientes marginales (α) — categoría 1 — En la categoría 1 (BI igual o inferior al equivalente en pesos de €1.000 millones), el coeficiente marginal es 12%, de modo que BIC = BI x 12%.
  - `e4` Definicion: Incremento marginal de BIC — categoría 1 — El incremento marginal del BIC derivado del aumento de una unidad del BI es del 12% en la categoría 1.
  - `e5` Definicion: Incremento marginal de BIC — categoría 2 — El incremento marginal del BIC derivado del aumento de una unidad del BI es del 15% en la categoría 2.
  - `e6` Definicion: Incremento marginal de BIC — categoría 3 — El incremento marginal del BIC derivado del aumento de una unidad del BI es del 18% en la categoría 3.
  - `e7` Condicion: Tramo de BI ≤ €1.000 millones equivalente en pesos — El BI es igual o inferior al equivalente en pesos de €1.000 millones (categoría 1).
  - `e8` Condicion: Tramo de BI entre €1.000 y €30.000 millones equivalente en pesos — El BI es superior a €1.000 millones e igual o inferior a €30.000 millones equivalente en pesos (categoría 2).
  - `e9` Condicion: Tramo de BI > €30.000 millones equivalente en pesos — El BI es superior a €30.000 millones equivalente en pesos (categoría 3).
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 249** Condicion `e7`: Tramo de BI ≤ €1.000 millones equivalente en pesos | descripcion: El BI es igual o inferior al equivalente en pesos de €1.000 millones (categoría 1). | tramo: BI igual o inferior al equivalente en pesos de €1.000 millones
