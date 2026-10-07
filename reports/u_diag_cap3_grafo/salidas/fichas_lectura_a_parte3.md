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
  - **caso 112** Excepcion `e1`: Excepción endosos para financiación | descripcion: Quedan exceptuados de los límites de endosos los que las entidades financieras realicen para obtener financiación a favor de otra entidad financiera o de un fiduciario de fideicomiso financiero comprendidos en la LEF, y las sucesivas transmisiones a favor de otros sujetos de la misma naturaleza. | tramo: Se exceptúan de las limitaciones establecidas en este punto a los endosos que las entidades financieras realicen para la obtención de financiación, a favor de una entidad financiera o de un fiduciario de un fideicomiso financiero, en ambos casos comprendidos en la Ley de Entidades Financieras y las sucesivas transmisiones a favor de otros sujetos de la misma naturaleza
  - **caso 113** Excepcion `e3`: Excepción endosos a favor del BCRA | descripcion: Quedan exceptuados los endosos a favor del BCRA de las limitaciones establecidas en el punto. | tramo: También se exceptuarán de la citada limitación los endosos a favor del BCRA
  - **caso 114** Excepcion `e2`: Excepción endosos para negociación en mercados de valores | descripcion: Quedan exceptuados los endosos cuando los cheques se depositen en la Caja de Valores S.A. para negociación en bolsas de comercio y mercados de valores autorizados por la CNV, debiendo extenderse los endosos con la cláusula "... para su negociación en mercados de valores". | tramo: cuando los cheques se depositen en la Caja de Valores S.A. para ser negociados en las bolsas de comercio y mercados de valores autorizados por la Comisión Nacional de Valores de la República Argentina, en cuyo caso los endosos deberán ser extendidos con la cláusula "... para su negociación en mercados de valores"
  - **caso 115** Excepcion `e4`: Excepción endosos en ECHEQ | descripcion: Quedan exceptuados los endosos efectuados en los ECHEQ de las limitaciones establecidas en el punto. | tramo: aquellos efectuados en los ECHEQ

## Unidad `cap::2.8.1` (punto_no_item)
- herencia: [chapeau_seccion S2] A los efectos de la aplicación de las disposiciones de la presente sección, las entidades financieras
se clasificarán en:
i)Grupo 1: entidades calificadas por el BCRA como de importancia sistémica a nivel local | [chapeau_seccion S2] (D-SIB) y sucursales o subsidiarias de bancos del exterior calificados como de impor-
tancia sistémica global (G-SIB). | [chapeau_seccion S2] ii) Grupo 2: entidades financieras no comprendidas en el acápite i).
En aquellos casos en que no se establezcan disposiciones específicas para cada uno de los citados
grupos de entidades financieras, deberá aplicarse el mismo tratamiento a ambos grupos.
Las entidades financieras que presenten cambios en su calificación –conforme a lo previsto en los
acápites precedentes–, contarán con un plazo de 6 meses para aplicar las disposiciones específicas
correspondientes al nuevo grupo al que pertenezca | [encabezado 2.8] 2.8. Exposiciones minoristas.
- texto propio: 2.8.1. Exposiciones comprendidas.
i) Personas humanas.
ii) Micro, pequeñas y medianas empresas (Mipyme), conforme al TO sobre Determina-
ción de la Condición de Micro, Pequeña y Mediana Empresa, que se ajusten a los cri-
terios para las exposiciones minoristas normativas previstos en el punto 2.8.3.
El resto de las exposiciones a Mipyme recibirán el tratamiento aplicable a las exposi-
ciones a empresas previsto en el punto 2.7.
Se excluyen a las exposiciones con garantía hipotecaria sobre vivienda residencial, las
participaciones en el capital de Mipyme y la tenencia de instrumentos de deuda emitidos
por esas empresas.
- entidades de la unidad:
  - `e1` Definicion: Exposiciones minoristas comprendidas — Comprenden personas humanas y Micro, pequeñas y medianas empresas (Mipyme) conforme al TO sobre Determinación de la Condición de Micro, Pequeña y Mediana Empresa, que se ajusten a los criterios para l
  - `e2` Excepcion: Exclusión exposiciones hipotecarias, participaciones y deuda de Mipyme — Quedan excluidas de las exposiciones minoristas las exposiciones con garantía hipotecaria sobre vivienda residencial, las participaciones en el capital de Mipyme y la tenencia de instrumentos de deuda
  - `e3` Obligacion: Tratamiento aplicable a Mipyme no normativas — Las exposiciones a Mipyme que no se ajusten a los criterios para las exposiciones minoristas normativas recibirán el tratamiento aplicable a las exposiciones a empresas previsto en el punto 2.7.
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 116** Excepcion `e2`: Exclusión exposiciones hipotecarias, participaciones y deuda de Mipyme | descripcion: Quedan excluidas de las exposiciones minoristas las exposiciones con garantía hipotecaria sobre vivienda residencial, las participaciones en el capital de Mipyme y la tenencia de instrumentos de deuda emitidos por esas empresas. | tramo: Se excluyen a las exposiciones con garantía hipotecaria sobre vivienda residencial, las participaciones en el capital de Mipyme y la tenencia de instrumentos de deuda emitidos por esas empresas.

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
  - **caso 117** Excepcion `e4`: Exclusión — posiciones en acciones cartera inversión | descripcion: Quedan excluidas de los conceptos comprendidos las posiciones en acciones en la cartera de inversión. | tramo: Posiciones en acciones en la cartera de inversión
  - **caso 120** Excepcion `e3`: Exclusión — activos fijos | descripcion: Quedan excluidos de los conceptos comprendidos los activos fijos. | tramo: Activos fijos
  - **caso 121** Excepcion `e2`: Exclusión — activos deducidos del capital ordinario nivel 1 | descripcion: Quedan excluidos de los conceptos comprendidos los activos que se deducen del capital ordinario del nivel 1 (COn1). | tramo: Activos que se deducen del capital ordinario del nivel 1 (COn1)

## Unidad `cap::2.6.1` (punto_no_item)
- herencia: [chapeau_seccion S2] A los efectos de la aplicación de las disposiciones de la presente sección, las entidades financieras
se clasificarán en:
i)Grupo 1: entidades calificadas por el BCRA como de importancia sistémica a nivel local | [chapeau_seccion S2] (D-SIB) y sucursales o subsidiarias de bancos del exterior calificados como de impor-
tancia sistémica global (G-SIB). | [chapeau_seccion S2] ii) Grupo 2: entidades financieras no comprendidas en el acápite i).
En aquellos casos en que no se establezcan disposiciones específicas para cada uno de los citados
grupos de entidades financieras, deberá aplicarse el mismo tratamiento a ambos grupos.
Las entidades financieras que presenten cambios en su calificación –conforme a lo previsto en los
acápites precedentes–, contarán con un plazo de 6 meses para aplicar las disposiciones específicas
correspondientes al nuevo grupo al que pertenezca | [encabezado 2.6] 2.6. Exposiciones a entidades financieras.
- texto propio: 2.6.1. Exposiciones comprendidas.
Comprende a las exposiciones a entidades financieras del país y del exterior (estas últi-
mas, sujetas a regulación y supervisión prudencial equiparables a los mínimos que se
establecen en los estándares internacionales o al cumplimiento del requisito de capitales
mínimos cuando se trate de bancos que no sean internacionalmente activos conforme a
la regulación de su jurisdicción). Se excluyen las exposiciones previstas en el punto
2.11.
Las exposiciones de corto plazo comprenden a aquellas denominadas en pesos cuya
fuente de fondos sea en esa moneda y su plazo contractual original sea de hasta 3 me-
ses, y a las exposiciones vinculadas con el comercio exterior cuyo plazo contractual ori-
ginal sea de hasta 6 meses.
- entidades de la unidad:
  - `e1` Operacion: Exposiciones a entidades financieras del país — Exposiciones a entidades financieras del país, comprendidas en el alcance de este punto.
  - `e2` Operacion: Exposiciones a entidades financieras del exterior — Exposiciones a entidades financieras del exterior, sujetas a regulación y supervisión prudencial equiparables a los mínimos de estándares internacionales o al cumplimiento del requisito de capitales m
  - `e3` Excepcion: Exclusión exposiciones punto 2.11 — Quedan excluidas del alcance de este punto las exposiciones previstas en el punto 2.11.
  - `e4` Definicion: Exposiciones de corto plazo — definición — Aquellas denominadas en pesos cuya fuente de fondos sea en esa moneda y su plazo contractual original sea de hasta 3 meses, y las exposiciones vinculadas con el comercio exterior cuyo plazo contractua
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 118** Excepcion `e3`: Exclusión exposiciones punto 2.11 | descripcion: Quedan excluidas del alcance de este punto las exposiciones previstas en el punto 2.11. | tramo: Se excluyen las exposiciones previstas en el punto 2.11

## Unidad `cap::4.1::intro` (intro)
- herencia: [encabezado 4.1] 4.1. Exigencia de capital por riesgo de crédito de contraparte para operaciones DvP fallidas y no
- texto propio: DvP.
En las operaciones con títulos valores, oro o moneda extranjera pendientes de liquidación
(como ocurre en las operaciones contado a liquidar), la exposición al riesgo de crédito de
contraparte se produce desde la fecha de la operación, con independencia de cuando se
registre o contabilice. Las entidades deberán desarrollar, implementar y mejorar sistemas para
realizar un seguimiento adecuado de la exposición al riesgo de crédito de contraparte
procedente de esas operaciones y obtener información que permita intervenir en el momento
oportuno.
Las operaciones concertadas bajo la modalidad de entrega contra pago (DvP) –que implica el
intercambio simultáneo de valores por efectivo– exponen a las entidades al riesgo de pérdida
por la exposición actual positiva –definida como la diferencia positiva entre el valor de la ope-
ración al precio de liquidación convenido y su valor al precio actual de mercado–.
Las operaciones en las que se entrega efectivo sin recibir la correspondiente contrapartida (tí-
tulos valores, oro o moneda extranjera) o, al contrario, en las que se entregan los efectos
acordados sin el correspondiente pago de efectivo –es decir, operaciones no DvP– exponen a
las entidades al riesgo de pérdida por el valor total del efectivo abonado o de los efectos en-
tregados.
En el presente punto se detalla el cómputo de la exigencia de capital para cubrir ambos tipos
de riesgo. Esto incluye operaciones sujetas a valuación diaria a precios de mercado y a repo-
sición diaria de márgenes realizadas a través de cámaras de compensación y de CCP sujetas
a regulación. No se incluyen las operaciones de pase que no hayan podido liquidarse.
- entidades de la unidad:
  - `e1` Operacion: Operaciones DvP con títulos, oro o moneda extranjera — Operaciones con títulos valores, oro o moneda extranjera pendientes de liquidación (como operaciones contado a liquidar) que implican intercambio simultáneo de valores por efectivo. La exposición al r
  - `e2` Operacion: Operaciones no DvP con títulos, oro o moneda extranjera — Operaciones en las que se entrega efectivo sin recibir la correspondiente contrapartida (títulos valores, oro o moneda extranjera) o se entregan los efectos acordados sin el correspondiente pago de ef
  - `e3` Obligacion: Desarrollar, implementar y mejorar sistemas de seguimiento — Las entidades deberán desarrollar, implementar y mejorar sistemas para realizar un seguimiento adecuado de la exposición al riesgo de crédito de contraparte procedente de operaciones con títulos valor
  - `e4` Excepcion: Exclusión de operaciones de pase no liquidadas — Quedan excluidas del cómputo de la exigencia de capital las operaciones de pase que no hayan podido liquidarse.
  - `e5` Condicion: Operaciones sujetas a valuación diaria y reposición de márgenes — El cómputo de la exigencia de capital incluye operaciones sujetas a valuación diaria a precios de mercado y a reposición diaria de márgenes realizadas a través de cámaras de compensación y de CCP suje
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 119** Excepcion `e4`: Exclusión de operaciones de pase no liquidadas | descripcion: Quedan excluidas del cómputo de la exigencia de capital las operaciones de pase que no hayan podido liquidarse. | tramo: No se incluyen las operaciones de pase que no hayan podido liquidarse
  - **caso 211** Condicion `e5`: Operaciones sujetas a valuación diaria y reposición de márgenes | descripcion: El cómputo de la exigencia de capital incluye operaciones sujetas a valuación diaria a precios de mercado y a reposición diaria de márgenes realizadas a través de cámaras de compensación y de CCP sujetas a regulación. | tramo: operaciones sujetas a valuación diaria a precios de mercado y a reposición diaria de márgenes realizadas a través de cámaras de compensación y de CCP sujetas a regulación

## Unidad `polcre::5.1` (punto_no_item)
- herencia: [encabezado S5] Sección 5. Financiamiento a residentes en el exterior.
- texto propio: 5.1. Criterio general.
El otorgamiento de asistencia financiera a residentes en el exterior sólo procederá en tanto se
ajuste al criterio general sobre política de crédito indicado en la Sección 1.
Conforme a ello, se podrán conceder líneas de crédito a bancos del exterior, corresponsales o
no, y a otros residentes en el exterior destinadas a facilitar las exportaciones locales.
También se admite la existencia de créditos a residentes en el exterior correspondientes a des-
fases de liquidación de operaciones con títulos valores o monedas extranjeras con cotización y
las operaciones previstas en los siguientes puntos.
- entidades de la unidad:
  - `e1` Condicion: Ajuste a criterio general de política de crédito — El otorgamiento de asistencia financiera a residentes en el exterior debe ajustarse al criterio general sobre política de crédito indicado en la Sección 1.
  - `e2` Operacion: Concesión de líneas de crédito a bancos del exterior — Concesión de líneas de crédito a bancos del exterior, corresponsales o no, destinadas a facilitar las exportaciones locales.
  - `e3` Operacion: Concesión de líneas de crédito a otros residentes en el exterior — Concesión de líneas de crédito a otros residentes en el exterior destinadas a facilitar las exportaciones locales.
  - `e4` Potestad: Facultad de conceder líneas de crédito a residentes en el exterior — Las entidades financieras quedan facultadas a conceder líneas de crédito a bancos del exterior, corresponsales o no, y a otros residentes en el exterior destinadas a facilitar las exportaciones locale
  - `e5` Operacion: Créditos por desfases de liquidación de operaciones con títulos valores — Créditos a residentes en el exterior correspondientes a desfases de liquidación de operaciones con títulos valores o monedas extranjeras con cotización.
  - `e6` Excepcion: Admisión de créditos por desfases de liquidación — Se admite la existencia de créditos a residentes en el exterior correspondientes a desfases de liquidación de operaciones con títulos valores o monedas extranjeras con cotización, como excepción a las
- relaciones del crudo (sin establecida_en ni de sujeto): e1 condicion_de e4
- NODOS A CLASIFICAR:
  - **caso 122** Excepcion `e6`: Admisión de créditos por desfases de liquidación | descripcion: Se admite la existencia de créditos a residentes en el exterior correspondientes a desfases de liquidación de operaciones con títulos valores o monedas extranjeras con cotización, como excepción a las restricciones generales. | tramo: También se admite la existencia de créditos a residentes en el exterior correspondientes a desfases de liquidación de operaciones con títulos valores o monedas extranjeras con cotización

## Unidad `cap::4.2.2` (punto_no_item)
- herencia: [intro 4.2] –OTC o negociados en mercados regulados– y con liquidación diferida.
La exigencia computada en este punto –basada en el Enfoque Estándar para la medición de
la exigencia por capital por riesgo de crédito de contraparte (“Standardised Approach for
measuring Counterparty Credit Risk”, SA-CCR)– se aplicará a operaciones con derivados
–OTC o negociados en mercados regulados– y con liquidación diferida, ya que las operacio-
nes de financiación con títulos valores (“Securities Financing Transactions”,
- texto propio: 4.2.2. Ajuste de valuación del crédito (CVA).
Además de la exposición al riesgo de incumplimiento determinada en el punto 4.2.1.,
las entidades financieras deberán observar una exigencia de capital por el riesgo de
pérdidas derivadas de valuar a precios de mercado el riesgo de contraparte esperado
–pérdidas conocidas como “ajustes de valuación del crédito”, CVA–.
Las entidades no observarán esta exigencia de capital cuando se trate de operaciones
de financiación con títulos valores –tales como las operaciones de pase– y en las ope-
raciones celebradas con una entidad de contraparte central (CCP).
La exigencia de capital por CVA correspondiente a la totalidad de contrapartes se de-
terminará según la siguiente expresión para un horizonte de riesgo de un año:
2
   
0,5 EADTotal Mcobertura w
w M B M B  
x x x x x x
i i i i i ind ind ind
 
K(CVA)2,33 i ind
x
 2
0,75 w2 EADTotal Mcobertura
M B
x x x x
i i i i i
i
donde:
- w: ponderador aplicable a la contraparte i, que se establece en 0 % para el sector
i
público no financiero y Banco Central, y en 3 % para el resto de las contrapar-
tes –excepto que se trate de entidades del exterior que no cumplan con lo pre-
visto en el punto 3.1. o 3.2., según corresponda, de las normas sobre “Evalua-
ciones crediticias”, en cuyo caso se les aplicará un ponderador del 10 %–. A los
efectos del cumplimiento de los citados puntos de las normas sobre “Evalua-
ciones crediticias” se deberá contar con calificación internacional de riesgo “in-
vestment grade”.
- EADTotal: exposición al incumplimiento de la contraparte i –agregada para todos los
i
conjuntos de neteo, de corresponder, e incluido el efecto del activo en ga-
rantía–, a cuyo valor se le aplica el factor de descuento (1-exp (-0,05 x
M:))/(0,05 x M:).
i i
- B: valor 
- entidades de la unidad:
  - `e1` Obligacion: Exigencia de capital por CVA — Las entidades financieras deben observar una exigencia de capital por el riesgo de pérdidas derivadas de valuar a precios de mercado el riesgo de contraparte esperado (CVA).
  - `e2` Excepcion: Excepción CVA — operaciones de financiación con títulos valores — Las entidades no observarán la exigencia de capital por CVA cuando se trate de operaciones de financiación con títulos valores, tales como operaciones de pase.
  - `e3` Excepcion: Excepción CVA — operaciones con CCP — Las entidades no observarán la exigencia de capital por CVA en operaciones celebradas con una entidad de contraparte central (CCP).
  - `e4` Obligacion: Determinación de exigencia de capital por CVA según fórmula — La exigencia de capital por CVA correspondiente a la totalidad de contrapartes se determinará según una expresión matemática para un horizonte de riesgo de un año. La fórmula incluye ponderadores apli
  - `e5` Restriccion: Ponderador 0% — sector público no financiero y Banco Central — El ponderador aplicable a la contraparte i se establece en 0% para el sector público no financiero y Banco Central.
  - `e6` Restriccion: Ponderador 3% — resto de contrapartes — El ponderador aplicable a la contraparte i se establece en 3% para el resto de las contrapartes, excepto entidades del exterior que no cumplan con lo previsto en puntos 3.1 o 3.2 de normas sobre Evalu
  - `e7` Excepcion: Excepción ponderador — entidades del exterior sin calificación investment grade — Se aplicará un ponderador del 10% a entidades del exterior que no cumplan con lo previsto en puntos 3.1 o 3.2 de normas sobre Evaluaciones crediticias (requieren calificación internacional de riesgo i
  - `e8` Obligacion: Calificación investment grade para cumplimiento de normas — Para cumplir con los puntos 3.1 o 3.2 de las normas sobre Evaluaciones crediticias, se debe contar con calificación internacional de riesgo investment grade.
  - `e9` Restriccion: Elegibilidad de coberturas — solo para mitigación de CVA — Solo las coberturas utilizadas con el propósito de mitigar el riesgo de CVA y gestionadas como tales son elegibles para ser consideradas en el cómputo de la exigencia de capital.
  - `e10` Definicion: Coberturas admisibles para CVA — Son coberturas admisibles: swaps de incumplimiento crediticio de referencia única (single-name CDS), swaps de incumplimiento crediticio contingentes de referencia única, otros instrumentos de cobertur
  - `e11` Restriccion: Exclusión de otros tipos de cobertura del cálculo de K(CVA) — No deben considerarse en el cálculo del K(CVA) otros tipos de cobertura del riesgo de contraparte, debiendo recibir el mismo tratamiento que cualquier otro instrumento de la cartera de la entidad fina
  - `e12` Restriccion: Exclusión de CDS por tramos o enésimo incumplimiento — Los swaps de incumplimiento crediticio por tramos o de enésimo incumplimiento no constituyen coberturas de CVA admisibles.
- relaciones del crudo (sin establecida_en ni de sujeto): e2 exceptua_obligacion e1; e3 exceptua_obligacion e1
- NODOS A CLASIFICAR:
  - **caso 123** Excepcion `e7`: Excepción ponderador — entidades del exterior sin calificación investment grade | descripcion: Se aplicará un ponderador del 10% a entidades del exterior que no cumplan con lo previsto en puntos 3.1 o 3.2 de normas sobre Evaluaciones crediticias (requieren calificación internacional de riesgo investment grade). | tramo: excepto que se trate de entidades del exterior que no cumplan con lo previsto en el punto 3.1. o 3.2., según corresponda, de las normas sobre "Evaluaciones crediticias", en cuyo caso se les aplicará un ponderador del 10 %

## Unidad `ext::10.10.2.10` (item)
- herencia: [intro 10.10] de ingreso aduanero a partir del 13/12/23. | **[abre la lista]** [intro 10.10.2] Las entidades podrán dar acceso al mercado de cambios para cursar pagos con
registro de ingreso aduanero pendiente por operaciones no comprendidas en el
punto 10.6.6. cuando, en adición a los restantes requisitos aplicables, se verifique
alguna de las siguientes situaciones: | [cierre 10.10.2] Se podrá considerar como importación de bienes de capital a: i) aquellas que
correspondan a bienes cuyas posiciones arancelarias se encuentren clasificadas
como BK en la Nomenclatura Común del MERCOSUR (Decreto 690/02 y
complementarias) y ii) aquellas que incluyan otros bienes en la medida que los
bienes clasificados como BK representen como mínimo el 90% (noventa por
ciento) del valor FOB total de la operación y la entidad cuente con una declaración
jurada del cliente en la cual deje constancia
- texto propio: 10.10.2.10. El pago corresponda a la cancelación de deudas por operaciones
financiadas o garantizadas con anterioridad al 13/12/23 por
organismos internacionales y/o agencias oficiales de crédito.
Las entidades podrán considerar también como operación
garantizada por una agencia oficial de crédito a aquella que se
encuentre cubierta por una garantía emitida por una aseguradora
privada por cuenta y orden de un gobierno nacional de otro país. En
todos los casos, la entidad interviniente deberá contar con
documentación en la que conste explícitamente tal situación.
- entidades de la unidad:
  - `c1` Condicion: Pago cancelación deudas operaciones financiadas/garantizadas — El pago debe corresponder a la cancelación de deudas por operaciones que fueron financiadas o garantizadas antes del 13/12/23 por organismos internacionales y/o agencias oficiales de crédito
  - `e1` Excepcion: Garantía aseguradora privada por cuenta de gobierno extranjero — Se considera como operación garantizada por agencia oficial de crédito aquella cubierta por garantía de aseguradora privada emitida por cuenta y orden de un gobierno nacional extranjero
  - `o1` Obligacion: Documentación de garantía aseguradora privada — La entidad interviniente debe contar con documentación que conste explícitamente la situación de cobertura por garantía de aseguradora privada por cuenta y orden de gobierno extranjero
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 124** Excepcion `e1`: Garantía aseguradora privada por cuenta de gobierno extranjero | descripcion: Se considera como operación garantizada por agencia oficial de crédito aquella cubierta por garantía de aseguradora privada emitida por cuenta y orden de un gobierno nacional extranjero | tramo: Las entidades podrán considerar también como operación garantizada por una agencia oficial de crédito a aquella que se encuentre cubierta por una garantía emitida por una aseguradora privada por cuenta y orden de un gobierno nacional de otro país
  - **caso 215** Condicion `c1`: Pago cancelación deudas operaciones financiadas/garantizadas | descripcion: El pago debe corresponder a la cancelación de deudas por operaciones que fueron financiadas o garantizadas antes del 13/12/23 por organismos internacionales y/o agencias oficiales de crédito | tramo: El pago corresponda a la cancelación de deudas por operaciones financiadas o garantizadas con anterioridad al 13/12/23 por organismos internacionales y/o agencias oficiales de crédito

## Unidad `ext::3.5.3.2` (item)
- herencia: [chapeau_seccion S3] Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas
en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–,
adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán
cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables. | [intro 3.5] exterior.
Las entidades podrán dar acceso al mercado de cambios para realizar pagos de capital o
intereses de títulos de deuda con registro público en el exterior, otros endeudamientos
financieros con el exterior y títulos de deuda con registro público en el país denominados en
moneda extranjera íntegramente suscriptos en el exterior, en la medida que se verifiquen las
siguientes condiciones: | [intro 3.5.3] (tres) días hábiles a la fecha de vencimiento del servicio de capital o interés a pagar.
En el caso de que se trate de un pago de capital de títulos de deuda emitidos a partir
del 08/11/24 que se concreta con una transferencia al exterior, el acceso al mercado
de cambios deberá adicionalmente producirse una vez transcurridos, como mínimo,
desde la fecha de emisión: | [intro 3.5.3] i) 12 (doce) meses si el título fue emitido entre el 08/11/24 y el 20/04/25.
ii) 6 (seis) meses si el título fue emitido entre 21/04/25 y el 15/05/25.
iii) 18 (dieciocho) meses si el título fue emitido a partir del 16/05/25. | **[abre la lista]** [intro 3.5.3] El acceso al mercado de cambios antes de lo indicado requerirá la conformidad previa
del BCRA excepto que el deudor encuadre en alguna de las siguientes situaciones y
se cumplan la totalidad de las condiciones estipuladas en cada caso:
- texto propio: 3.5.3.2. Precancelación de capital e intereses con la liquidación simultánea de otros
endeudamientos financieros comprendidos en este punto 3.5.
i) la precancelación de capital e intereses sea efectuada en manera
simultánea con los fondos liquidados de un nuevo endeudamiento
financiero comprendido en este punto 3.5.;
ii) la vida promedio del nuevo endeudamiento sea mayor a la vida
promedio remanente de la deuda que se precancela; y
iii) el monto acumulado de los vencimientos de capital del nuevo
endeudamiento en ningún momento podrá superar, hasta la fecha de
vencimiento de la deuda que se cancela, el monto que hubieran
acumulado los vencimientos de capital de la deuda que se cancela.
- entidades de la unidad:
  - `e1` Excepcion: Excepción precancelación con liquidación simultánea — Se exceptúa la exigencia de conformidad previa del BCRA para acceso al mercado de cambios antes del plazo establecido cuando se trata de precancelación de capital e intereses realizada simultáneamente
  - `c1` Condicion: Precancelación simultánea con nuevo endeudamiento — La precancelación de capital e intereses debe efectuarse de manera simultánea con los fondos liquidados de un nuevo endeudamiento financiero comprendido en el punto 3.5.
  - `c2` Condicion: Vida promedio del nuevo endeudamiento mayor — La vida promedio del nuevo endeudamiento debe ser mayor a la vida promedio remanente de la deuda que se precancela.
  - `r1` Restriccion: Límite monto acumulado vencimientos capital nuevo endeudamiento — El monto acumulado de los vencimientos de capital del nuevo endeudamiento no podrá superar, hasta la fecha de vencimiento de la deuda que se cancela, el monto que hubieran acumulado los vencimientos d
- relaciones del crudo (sin establecida_en ni de sujeto): c1 condicion_de e1; c2 condicion_de e1; r1 condicion_de e1
- NODOS A CLASIFICAR:
  - **caso 125** Excepcion `e1`: Excepción precancelación con liquidación simultánea | descripcion: Se exceptúa la exigencia de conformidad previa del BCRA para acceso al mercado de cambios antes del plazo establecido cuando se trata de precancelación de capital e intereses realizada simultáneamente con fondos de nuevo endeudamiento financiero, siempre que se cumplan todas las condiciones especificadas. | tramo: El acceso al mercado de cambios antes de lo indicado requerirá la conformidad previa del BCRA excepto que el deudor encuadre en alguna de las siguientes situaciones y se cumplan la totalidad de las condiciones estipuladas en cada caso: i) la precancelación de capital e intereses sea efectuada en manera simultánea con los fondos liquidados de un nuevo endeudamiento financiero comprendido en este punto 3.5.; ii) la vida promedio del nuevo endeudamiento sea mayor a la vida promedio remanente de la deuda que se precancela; y iii) el monto acumulado de los vencimientos de capital del nuevo endeudamiento en ningún momento podrá superar, hasta la fecha de vencimiento de la deuda que se cancela, el monto que hubieran acumulado los vencimientos de capital de la deuda que se cancela.

## Unidad `cla::6.5.4.6` (item)
- herencia: [intro 6.5] Cada cliente, y la totalidad de sus financiaciones comprendidas, se incluirá en una de las si-
guientes cinco categorías, las que se definen teniendo en cuenta las condiciones que se deta-
llan en cada caso.
Los clientes que no registren asistencia crediticia de la entidad y que posteriormente reciban fi-
nanciaciones de ésta que no superen el importe resultante de aplicar sobre el saldo de deuda
registrado en el sistema financiero, según la última información disponible en la “Central de
deudor | **[abre la lista]** [intro 6.5.4] El análisis del flujo de fondos del cliente demuestra que es altamente improbable que
pueda atender la totalidad de sus compromisos financieros.
Entre los indicadores que pueden reflejar esta situación se destacan que el cliente:
- texto propio: 6.5.4.6. Haya sido demandado judicialmente por la entidad para el cobro de su acreencia
cuando ello se encuentre vinculado a la falta de pago y registre mora en el pago
de hasta un año. Se excluyen los casos en que las acciones se refieren a la dis-
cusión sobre otros aspectos contractuales.
En caso de verificarse atrasos mayores a 540 días, corresponderá la reclasifica-
ción inmediata del deudor en el nivel siguiente inferior.
- entidades de la unidad:
  - `e1` Condicion: Demanda judicial por cobro vinculada a falta de pago — El cliente ha sido demandado judicialmente por la entidad para el cobro de su acreencia cuando ello se encuentra vinculado a la falta de pago
  - `e2` Condicion: Mora en pago hasta un año — El cliente registra mora en el pago de hasta un año
  - `e3` Excepcion: Excepción acciones sobre aspectos contractuales — Se excluyen de la clasificación en alto riesgo de insolvencia los casos en que las acciones judiciales se refieren a la discusión sobre otros aspectos contractuales, no al cobro de acreencia por falta
  - `e4` Obligacion: Reclasificación inmediata por atrasos mayores a 540 días — Cuando se verifiquen atrasos mayores a 540 días, corresponde la reclasificación inmediata del deudor al nivel siguiente inferior
- relaciones del crudo (sin establecida_en ni de sujeto): e1 condicion_de e4; e2 condicion_de e4
- NODOS A CLASIFICAR:
  - **caso 126** Excepcion `e3`: Excepción acciones sobre aspectos contractuales | descripcion: Se excluyen de la clasificación en alto riesgo de insolvencia los casos en que las acciones judiciales se refieren a la discusión sobre otros aspectos contractuales, no al cobro de acreencia por falta de pago | tramo: Se excluyen los casos en que las acciones se refieren a la discusión sobre otros aspectos contractuales

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
  - **caso 127** Excepcion `e9`: Reconocimiento parcial cuando reestructuración no está contemplada | descripcion: Se permite reconocimiento parcial del derivado de crédito cuando la reestructuración de la obligación subyacente no esté contemplada pero se cumplan los demás requisitos de los acápites i) a vii). | tramo: Cuando la reestructuración de la obligación subyacente no esté contemplada por el derivado de crédito, pero se cumplan los requisitos incluidos en los acápites i) a vii) precedentes, se permitirá el reconocimiento parcial del derivado de crédito.
  - **caso 140** Condicion `e5`: Aplicación de requisitos cuando obligación de referencia difiere de subyacente | descripcion: Cuando la obligación de referencia para liquidación en efectivo sea distinta de la obligación subyacente, aplican los requisitos del acápite ii) (descalce entre obligaciones). | tramo: Si la obligación de referencia especificada en el derivado de crédito, a efectos de la liquidación de la cobertura en efectivo, fuera distinta de la obligación subyacente, será de aplicación lo establecido en el acápite ii).
  - **caso 173** Condicion `e8`: Descalce en obligación para determinar evento de crédito | descripcion: Se permite descalce entre la obligación subyacente y la utilizada para determinar evento de crédito cuando: la obligación sea de categoría similar o inferior a la subyacente, ambas sean emitidas por el mismo deudor, y existan cláusulas recíprocas legalmente exigibles de incumplimiento cruzado o aceleración cruzada. | tramo: Se permite un descalce entre la obligación subyacente y la obligación utilizada a efectos de determinar si ha ocurrido un evento de crédito siempre que: a) esta última sea de categoría similar o inferior a la obligación subyacente, b) ambas obligaciones estén emitidas por el mismo deudor, y c) existan cláusulas recíprocas legalmente exigibles de incumplimiento cruzado o de aceleración cruzada.
  - **caso 174** Condicion `e2`: Descalce entre obligación subyacente y de referencia | descripcion: El derivado de crédito puede cubrir obligaciones distintas de la subyacente (descalce) cuando: la obligación de referencia sea de categoría similar o inferior a la subyacente, ambas sean emitidas por el mismo deudor, y existan cláusulas recíprocas de incumplimiento o aceleración legalmente exigibles. | tramo: Se admitirá que el derivado de crédito cubra obligaciones que no incluyen la obligación subyacente, es decir que exista un descalce entre esta última y la obligación de referencia del derivado de crédito –obligación utilizada a efectos de determinar el monto del efectivo a liquidar o la obligación a entregar– siempre que: a) la obligación de referencia sea de categoría similar o inferior a la obligación subyacente; b) ambas estén emitidas por el mismo deudor; y c) existan cláusulas recíprocas en caso de incumplimiento o cláusulas recíprocas de aceleración legalmente exigibles.

## Unidad `cap::6.2.1.2` (punto_no_item)
- herencia: [intro 6.2] La exigencia de capital por el riesgo de tasa de interés se deberá calcular respecto de los títu-
los de deuda y otros instrumentos imputados a la cartera de negociación, incluidas las accio-
nes preferidas no convertibles.
Un título valor vendido y recomprado a término en una operación de pase pasivo o en otro tipo
de operación de financiación con títulos valores se tratará como si todavía fuese propiedad de
la entidad cedente; es decir, recibirá el mismo tratamiento que un título en cartera.
L | [intro 6.2.1] La exigencia de capital por riesgo específico tiene por objeto proteger a la entidad ante
movimientos adversos en el precio de un título causados por factores relacionados con
su emisor. Para su cálculo, sólo se permitirá netear las posiciones opuestas respecto de
una misma especie, incluidas las posiciones en derivados.
- texto propio: 6.2.1.2. Exigencia de capital por riesgo específico en posiciones de titulización.
i) La exigencia de capital por riesgo específico de las posiciones de tituliza-
ción mantenidas en la cartera de negociación será el 8 % del importe pon-
derado por riesgo de las posiciones de titulización netas imputadas a esa
cartera, aplicando a ese efecto el ponderador resultante de observar las
disposiciones relativas al enfoque estandarizado –punto 3.1.11.–, multipli-
cado por un ratio de concentración.
El ratio de concentración se obtendrá de la suma de los valores nominales
de todos los tramos dividida por la suma de los valores nominales de los
tramos subordinados o de igual prelación (“pari passu”) que el tramo en el
que se tiene la posición.
Cuando la entidad no pueda determinar la exigencia de capital por riesgo
específico conforme a la metodología establecida o el ratio de concentra-
ción sea igual o superior a 12,5, se deberá aplicar a la posición neta un
ponderador de riesgo del 1250 %.
ii) Se podrá excluir del cómputo de la exigencia de capital por riesgo general
de mercado aquellas posiciones que, conforme a lo previsto en este punto,
conlleven un ponderador de riesgo del 1250 %.
- entidades de la unidad:
  - `e1` Operacion: Posiciones de titulización en cartera de negociación — Posiciones de titulización mantenidas en la cartera de negociación, sujetas a cálculo de exigencia de capital por riesgo específico.
  - `e2` Obligacion: Calcular exigencia capital riesgo específico titulización — La exigencia de capital por riesgo específico de las posiciones de titulización mantenidas en la cartera de negociación será el 8 % del importe ponderado por riesgo de las posiciones de titulización n
  - `e3` Definicion: Ratio de concentración — La suma de los valores nominales de todos los tramos dividida por la suma de los valores nominales de los tramos subordinados o de igual prelación (pari passu) que el tramo en el que se tiene la posic
  - `e4` Restriccion: Ponderador 1250 % cuando no se puede determinar exigencia — Cuando la entidad no pueda determinar la exigencia de capital por riesgo específico conforme a la metodología establecida o el ratio de concentración sea igual o superior a 12,5, se deberá aplicar a l
  - `e5` Condicion: Condición: no poder determinar exigencia o ratio ≥ 12,5 — La entidad no puede determinar la exigencia de capital por riesgo específico conforme a la metodología establecida, o el ratio de concentración es igual o superior a 12,5.
  - `e6` Excepcion: Exclusión de exigencia capital riesgo general mercado — Se podrá excluir del cómputo de la exigencia de capital por riesgo general de mercado aquellas posiciones que conlleven un ponderador de riesgo del 1250 %.
- relaciones del crudo (sin establecida_en ni de sujeto): e2 regula e1; e4 limita e1; e5 condicion_de e4
- NODOS A CLASIFICAR:
  - **caso 128** Excepcion `e6`: Exclusión de exigencia capital riesgo general mercado | descripcion: Se podrá excluir del cómputo de la exigencia de capital por riesgo general de mercado aquellas posiciones que conlleven un ponderador de riesgo del 1250 %. | tramo: Se podrá excluir del cómputo de la exigencia de capital por riesgo general de mercado aquellas posiciones que, conforme a lo previsto en este punto, conlleven un ponderador de riesgo del 1250 %.

## Unidad `cap::6.2.2.3` (punto_no_item)
- herencia: [intro 6.2] La exigencia de capital por el riesgo de tasa de interés se deberá calcular respecto de los títu-
los de deuda y otros instrumentos imputados a la cartera de negociación, incluidas las accio-
nes preferidas no convertibles.
Un título valor vendido y recomprado a término en una operación de pase pasivo o en otro tipo
de operación de financiación con títulos valores se tratará como si todavía fuese propiedad de
la entidad cedente; es decir, recibirá el mismo tratamiento que un título en cartera.
L | [encabezado 6.2.2] 6.2.2. Exigencia de capital por riesgo general de mercado: método de los plazos residuales.
- texto propio: 6.2.2.3. Las posiciones compradas y vendidas en títulos de deuda e instrumentos deri-
vados se imputarán a escalas de vencimientos divididas en 15 o 13 bandas
temporales, según que el cupón del instrumento sea, o no, menor a 3 %. Los
instrumentos a tasa fija se asignarán según su plazo residual y los instrumen-
tos a tasa variable según el plazo que resta hasta el siguiente ajuste del inte-
rés. El ponderador de riesgo de los instrumentos a tasa variable dependerá de
que el cupón de renta del período en curso –o, de no estar disponible aún, el
último que se hubiera pagado– represente o no un rendimiento menor a 3 %
anual. Se podrán excluir las posiciones opuestas por el mismo importe en una
misma especie, como así también los derivados (“swaps”, “forwards”, futuros y
“forward rate agreements” –FRAs–) estrechamente relacionados y que cum-
plan las condiciones establecidas en el acápite i) del punto 6.2.3.5.
- entidades de la unidad:
  - `e1` Operacion: Imputación posiciones títulos deuda — escalas vencimientos — Las posiciones compradas y vendidas en títulos de deuda e instrumentos derivados se imputarán a escalas de vencimientos divididas en 15 bandas temporales si el cupón es mayor o igual a 3 %, o en 13 ba
  - `e2` Operacion: Asignación instrumentos tasa fija — plazo residual — Los instrumentos a tasa fija se asignarán según su plazo residual
  - `e3` Operacion: Asignación instrumentos tasa variable — plazo ajuste — Los instrumentos a tasa variable se asignarán según el plazo que resta hasta el siguiente ajuste del interés
  - `e4` Operacion: Determinación ponderador riesgo — tasa variable — El ponderador de riesgo de los instrumentos a tasa variable dependerá de si el cupón de renta del período en curso (o el último pagado si no está disponible) representa un rendimiento menor a 3 % anua
  - `e5` Excepcion: Exclusión posiciones opuestas mismo importe — Se pueden excluir las posiciones opuestas por el mismo importe en una misma especie de la imputación a escalas de vencimientos
  - `e6` Excepcion: Exclusión derivados relacionados — condiciones punto 6.2.3.5 — Se pueden excluir los derivados (swaps, forwards, futuros y FRAs) estrechamente relacionados que cumplan las condiciones establecidas en el acápite i) del punto 6.2.3.5
  - `e7` Potestad: Facultad de excluir posiciones y derivados — Facultad de excluir posiciones opuestas por el mismo importe en una misma especie y derivados estrechamente relacionados que cumplan condiciones específicas
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 129** Excepcion `e5`: Exclusión posiciones opuestas mismo importe | descripcion: Se pueden excluir las posiciones opuestas por el mismo importe en una misma especie de la imputación a escalas de vencimientos | tramo: Se podrán excluir las posiciones opuestas por el mismo importe en una misma especie
  - **caso 130** Excepcion `e6`: Exclusión derivados relacionados — condiciones punto 6.2.3.5 | descripcion: Se pueden excluir los derivados (swaps, forwards, futuros y FRAs) estrechamente relacionados que cumplan las condiciones establecidas en el acápite i) del punto 6.2.3.5 | tramo: Se podrán excluir [...] los derivados ("swaps", "forwards", futuros y "forward rate agreements" –FRAs–) estrechamente relacionados y que cumplan las condiciones establecidas en el acápite i) del punto 6.2.3.5

## Unidad `ext::2.2.1` (punto_no_item)
- herencia: [encabezado 2.2] 2.2. Cobros de exportaciones de servicios.
- texto propio: 2.2.1. Los cobros por la prestación de servicios por parte de residentes a no residentes
deberán ser ingresados y liquidados en el mercado de cambios en un plazo no mayor
a los 20 (veinte) días hábiles a partir de la fecha de su percepción en el exterior o en el
país o de su acreditación en cuentas del exterior.
En el caso de que el cliente sea un Vehículo de Proyecto Único (VPU) adherido al
Régimen de Incentivo para Grandes Inversiones (RIGI) que haya declarado ante la
Autoridad de Aplicación que preveía hacer uso de los beneficios establecidos en el
artículo 198 de la Ley 27.742 será aplicable la excepción prevista en el punto 14.1.3.
En el caso de fondos percibidos o acreditados en el exterior, se podrá considerar
cumplimentado el ingreso y liquidación por el monto equivalente a los gastos
habituales debitados por las entidades financieras del exterior por la transferencia de
fondos al país.
- entidades de la unidad:
  - `e1` Operacion: Ingreso y liquidación de cobros por servicios — Cobros por la prestación de servicios por parte de residentes a no residentes que deben ser ingresados y liquidados en el mercado de cambios
  - `e2` Obligacion: Plazo máximo 20 días hábiles — ingreso y liquidación de cobros — Los cobros por la prestación de servicios por parte de residentes a no residentes deberán ser ingresados y liquidados en el mercado de cambios en un plazo no mayor a los 20 (veinte) días hábiles a par
  - `e3` Condicion: Cliente VPU adherido al RIGI con declaración de beneficios — El cliente es un Vehículo de Proyecto Único (VPU) adherido al Régimen de Incentivo para Grandes Inversiones (RIGI) que haya declarado ante la Autoridad de Aplicación que preveía hacer uso de los benef
  - `e4` Excepcion: Excepción para VPU RIGI — punto 14.1.3 — Será aplicable la excepción prevista en el punto 14.1.3 para clientes VPU adheridos al RIGI que hayan declarado ante la Autoridad de Aplicación que preveían hacer uso de los beneficios del artículo 19
  - `e5` Condicion: Fondos percibidos o acreditados en el exterior — Los fondos han sido percibidos o acreditados en el exterior
  - `e6` Potestad: Facultad de considerar cumplido ingreso por gastos de transferencia — Se podrá considerar cumplimentado el ingreso y liquidación por el monto equivalente a los gastos habituales debitados por las entidades financieras del exterior por la transferencia de fondos al país
  - `e7` Comunicacion: Ley 27.742 — 
- relaciones del crudo (sin establecida_en ni de sujeto): e3 condicion_de e4; e5 condicion_de e6; e2 regula e1
- NODOS A CLASIFICAR:
  - **caso 131** Excepcion `e4`: Excepción para VPU RIGI — punto 14.1.3 | descripcion: Será aplicable la excepción prevista en el punto 14.1.3 para clientes VPU adheridos al RIGI que hayan declarado ante la Autoridad de Aplicación que preveían hacer uso de los beneficios del artículo 198 de la Ley 27.742 | tramo: será aplicable la excepción prevista en el punto 14.1.3

## Unidad `docvig::2.2.3` (punto_no_item)
- herencia: [encabezado 2.2] 2.2. Mayores de 75 años al 31.12.14 y los incapaces declarados judicialmente.
- texto propio: 2.2.3. A partir del año de otorgada la residencia permanente o temporaria en el país.
Documento Nacional de Identidad, manual o digital (DNI-m o DNI-d).
De existir prueba en contrario del país de domicilio, aplicará el punto 2.2.2.
En todos los casos deberá acreditarse la categoría de residencia, su vigencia y el tiempo de
radicación a partir de documentación emitida por la DNM.
El DNI-d en formato credencial virtual para dispositivos móviles inteligentes podrá ser exhibido
en las casas operativas de las entidades financieras en la medida que se observen las disposi-
ciones contenidas en el punto 2.12. de las normas sobre “Medidas mínimas de seguridad en
entidades financieras”.
- entidades de la unidad:
  - `c1` Condicion: Residencia permanente o temporaria otorgada — La documentación de identidad requerida aplica a partir del año en que se otorgó la residencia permanente o temporaria en el país
  - `op1` Operacion: Presentación de DNI manual o digital — Presentación de Documento Nacional de Identidad en formato manual o digital (DNI-m o DNI-d) como documentación válida
  - `ob1` Obligacion: Acreditación de categoría de residencia y vigencia — Deberá acreditarse la categoría de residencia, su vigencia y el tiempo de radicación a partir de documentación emitida por la Dirección Nacional de Migraciones
  - `pot1` Potestad: Exhibición de DNI-d en formato credencial virtual — El DNI-d en formato credencial virtual para dispositivos móviles inteligentes podrá ser exhibido en las casas operativas de las entidades financieras, sujeto a observancia de disposiciones sobre medid
  - `c2` Condicion: Observancia de medidas mínimas de seguridad — La exhibición del DNI-d en formato credencial virtual está condicionada a la observancia de las disposiciones sobre medidas mínimas de seguridad en entidades financieras
  - `exc1` Excepcion: Excepción por prueba en contrario del país de domicilio — Si existe prueba en contrario del país de domicilio, se aplicarán las disposiciones del punto 2.2.2 en lugar de las del presente punto
- relaciones del crudo (sin establecida_en ni de sujeto): c1 condicion_de op1; c2 condicion_de pot1
- NODOS A CLASIFICAR:
  - **caso 132** Excepcion `exc1`: Excepción por prueba en contrario del país de domicilio | descripcion: Si existe prueba en contrario del país de domicilio, se aplicarán las disposiciones del punto 2.2.2 en lugar de las del presente punto | tramo: De existir prueba en contrario del país de domicilio, aplicará el punto 2.2.2

## Unidad `ext::3.5.3::intro` (intro)
- herencia: [encabezado 3.5.3] 3.5.3. El acceso al mercado de cambios se produce con una anterioridad no mayor a los 3
- texto propio: (tres) días hábiles a la fecha de vencimiento del servicio de capital o interés a pagar.
En el caso de que se trate de un pago de capital de títulos de deuda emitidos a partir
del 08/11/24 que se concreta con una transferencia al exterior, el acceso al mercado
de cambios deberá adicionalmente producirse una vez transcurridos, como mínimo,
desde la fecha de emisión:
i) 12 (doce) meses si el título fue emitido entre el 08/11/24 y el 20/04/25.
ii) 6 (seis) meses si el título fue emitido entre 21/04/25 y el 15/05/25.
iii) 18 (dieciocho) meses si el título fue emitido a partir del 16/05/25.
El acceso al mercado de cambios antes de lo indicado requerirá la conformidad previa
del BCRA excepto que el deudor encuadre en alguna de las siguientes situaciones y
se cumplan la totalidad de las condiciones estipuladas en cada caso:
- entidades de la unidad:
  - `c1` Condicion: Acceso al mercado — anterioridad máxima 3 días — El acceso al mercado de cambios debe producirse con una anterioridad no mayor a 3 días hábiles antes de la fecha de vencimiento del servicio de capital o interés a pagar.
  - `c2` Condicion: Pago de capital — títulos emitidos 08/11/24 a 20/04/25 — 12 meses mínimo — Para pagos de capital de títulos de deuda emitidos entre el 08/11/24 y el 20/04/25 que se concretan con transferencia al exterior, el acceso al mercado de cambios debe producirse una vez transcurridos
  - `c3` Condicion: Pago de capital — títulos emitidos 21/04/25 a 15/05/25 — 6 meses mínimo — Para pagos de capital de títulos de deuda emitidos entre el 21/04/25 y el 15/05/25 que se concretan con transferencia al exterior, el acceso al mercado de cambios debe producirse una vez transcurridos
  - `c4` Condicion: Pago de capital — títulos emitidos a partir 16/05/25 — 18 meses mínimo — Para pagos de capital de títulos de deuda emitidos a partir del 16/05/25 que se concretan con transferencia al exterior, el acceso al mercado de cambios debe producirse una vez transcurridos, como mín
  - `p1` Potestad: Autorización previa del BCRA — acceso anticipado al mercado — El BCRA puede otorgar conformidad previa para que el acceso al mercado de cambios se produzca antes de los plazos indicados.
  - `e1` Excepcion: Excepción — conformidad previa del BCRA — situaciones especiales — No se requiere conformidad previa del BCRA si el deudor encuadra en alguna de las situaciones especiales que siguen y se cumplen todas las condiciones estipuladas en cada caso.
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 133** Condicion `c1`: Acceso al mercado — anterioridad máxima 3 días | descripcion: El acceso al mercado de cambios debe producirse con una anterioridad no mayor a 3 días hábiles antes de la fecha de vencimiento del servicio de capital o interés a pagar. | tramo: El acceso al mercado de cambios se produce con una anterioridad no mayor a los 3 (tres) días hábiles a la fecha de vencimiento del servicio de capital o interés a pagar
  - **caso 216** Condicion `c2`: Pago de capital — títulos emitidos 08/11/24 a 20/04/25 — 12 meses mínimo | descripcion: Para pagos de capital de títulos de deuda emitidos entre el 08/11/24 y el 20/04/25 que se concretan con transferencia al exterior, el acceso al mercado de cambios debe producirse una vez transcurridos, como mínimo, 12 meses desde la fecha de emisión. | tramo: si el título fue emitido entre el 08/11/24 y el 20/04/25
  - **caso 217** Condicion `c3`: Pago de capital — títulos emitidos 21/04/25 a 15/05/25 — 6 meses mínimo | descripcion: Para pagos de capital de títulos de deuda emitidos entre el 21/04/25 y el 15/05/25 que se concretan con transferencia al exterior, el acceso al mercado de cambios debe producirse una vez transcurridos, como mínimo, 6 meses desde la fecha de emisión. | tramo: si el título fue emitido entre 21/04/25 y el 15/05/25
  - **caso 218** Condicion `c4`: Pago de capital — títulos emitidos a partir 16/05/25 — 18 meses mínimo | descripcion: Para pagos de capital de títulos de deuda emitidos a partir del 16/05/25 que se concretan con transferencia al exterior, el acceso al mercado de cambios debe producirse una vez transcurridos, como mínimo, 18 meses desde la fecha de emisión. | tramo: si el título fue emitido a partir del 16/05/25

## Unidad `ctacte::7.3.3.2` (punto_no_item)
- herencia: [encabezado 7.3.3] 7.3.3. En caso de denuncia de extravío.
- texto propio: 7.3.3.2. Cuando el banco desconozca el juzgado interviniente.
i) Solicitar fehacientemente al cuentacorrentista, dentro de las 48 horas hábi-
les bancarias de producido cada rechazo, que en el término de 10 días co-
rridos contados desde dicha fecha acredite la formulación de la pertinente
denuncia ante el Juez competente, mediante presentación de copia auten-
ticada.
ii) Si el cuentacorrentista acredita dicha formulación, remitir el cheque o certifi-
cado nominativo transferible rechazado –retenido según lo previsto en el
punto 7.3.1.– al juzgado interviniente en la causa.
iii) Cuando el cuentacorrentista no acredite la formulación de la denuncia judi-
cial informar al BCRA, a los efectos de que cada rechazo sea incluido en la
“Central de cheques rechazados”.
A tal fin, corresponde que al momento en que la pertinente información
quede disponible en el aludido banco, la Superintendencia de Entidades
Financieras y Cambiarias –Gestión de la Información– cuente con el detalle
de las gestiones realizadas y de los comprobantes respectivos.
La formulación de la citada denuncia fuera del término establecido en el
punto 7.3.3.2. i) podrá dar lugar a las gestiones para lograr la eventual baja
de los rechazos de aquella central.
iv) Archivar las actuaciones vinculadas a la denuncia recibida y a los rechazos
efectuados por tal motivo.
- entidades de la unidad:
  - `e1` Obligacion: Solicitar acreditación de denuncia judicial — El banco debe solicitar fehacientemente al cuentacorrentista que acredite la formulación de denuncia ante el Juez competente mediante copia autenticada.
  - `e2` Obligacion: Remitir cheque al juzgado si se acredita denuncia — El banco debe remitir el cheque o certificado nominativo transferible rechazado al juzgado interviniente cuando el cuentacorrentista acredita la formulación de la denuncia.
  - `e3` Condicion: Acreditación de formulación de denuncia judicial — Que el cuentacorrentista acredite la formulación de la denuncia ante el Juez competente.
  - `e4` Obligacion: Informar al BCRA si no se acredita denuncia — El banco debe informar al BCRA cuando el cuentacorrentista no acredite la formulación de la denuncia judicial, a fin de que cada rechazo sea incluido en la Central de cheques rechazados.
  - `e5` Condicion: No acreditación de formulación de denuncia judicial — Que el cuentacorrentista no acredite la formulación de la denuncia judicial.
  - `e6` Obligacion: Proporcionar detalle de gestiones a la Superintendencia — El banco debe proporcionar a la Superintendencia de Entidades Financieras y Cambiarias el detalle de las gestiones realizadas y de los comprobantes respectivos cuando la información quede disponible.
  - `e7` Potestad: Gestiones para baja de rechazos por denuncia fuera de término — La Superintendencia o el BCRA puede realizar gestiones para lograr la eventual baja de los rechazos de la Central de cheques rechazados cuando la denuncia se formula fuera del término establecido.
  - `e8` Obligacion: Archivar actuaciones vinculadas a la denuncia — El banco debe archivar las actuaciones vinculadas a la denuncia recibida y a los rechazos efectuados por tal motivo.
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 134** Condicion `e3`: Acreditación de formulación de denuncia judicial | descripcion: Que el cuentacorrentista acredite la formulación de la denuncia ante el Juez competente. | tramo: Si el cuentacorrentista acredita dicha formulación
  - **caso 206** Condicion `e5`: No acreditación de formulación de denuncia judicial | descripcion: Que el cuentacorrentista no acredite la formulación de la denuncia judicial. | tramo: Cuando el cuentacorrentista no acredite la formulación de la denuncia judicial

## Unidad `ext::7.10.2.2` (item)
- herencia: [intro 7.10] del régimen de fomento de inversión para las exportaciones (Decreto 234/21). | **[abre la lista]** [intro 7.10.2] que se verifiquen la totalidad de las siguientes condiciones:
- texto propio: 7.10.2.2. El monto aplicado en el año calendario no supere el equivalente al 25%
(veinticinco por ciento) del monto bruto de las inversiones ingresadas para
financiar el desarrollo del proyecto que genera las exportaciones aplicadas.
El monto bruto de las inversiones ingresadas a computar surgirá de la
suma de los montos acumulados por:
i) las liquidaciones efectuadas en el mercado de cambios a partir del
07/04/21 en concepto de endeudamientos financieros comprendidos
en el punto 3.5. y aportes de inversión extranjera directa.
ii) el valor FOB de las importaciones de bienes de capital incorporados al
proyecto de inversión cuyo registro de ingreso aduanero se haya
producido a partir del 07/04/21 y que hayan tenido una financiación de
un acreedor del exterior con una vida promedio no inferior a 1 (un) año
que no fue computada en el punto anterior o hayan constituido un
aporte de inversión directa en especie a la empresa residente.
Las inversiones podrán ser computadas una vez transcurrido un año
calendario desde su liquidación en el mercado de cambios y/o el registro de
ingreso aduanero de los bienes de capital, según corresponda.
En el caso de aportes de inversión directa, el cliente deberá presentar la
documentación que avale la capitalización definitiva del aporte. En caso de
no disponerla, deberá presentar constancia del inicio del trámite de
inscripción ante el Registro Público de Comercio de la decisión de
capitalización definitiva de los aportes de capital computados de acuerdo
con los requisitos legales correspondientes y comprometerse a presentar la
documentación de la capitalización definitiva del aporte dentro de los 365
(trescientos sesenta y cinco) días corridos desde el inicio del trámite.
- entidades de la unidad:
  - `c1` Condicion: Año calendario — monto aplicado — El monto aplicado en el año calendario no debe superar el equivalente al 25% del monto bruto de las inversiones ingresadas para financiar el desarrollo del proyecto que genera las exportaciones aplica
  - `d1` Definicion: Monto bruto de inversiones ingresadas — La suma de los montos acumulados por: (i) liquidaciones en el mercado de cambios a partir del 07/04/21 por endeudamientos financieros comprendidos en el punto 3.5 y aportes de inversión extranjera dir
  - `c2` Condicion: Plazo de un año desde liquidación o ingreso aduanero — Las inversiones pueden ser computadas solo después de transcurrido un año calendario desde su liquidación en el mercado de cambios y/o el registro de ingreso aduanero de los bienes de capital, según c
  - `o1` Obligacion: Presentar documentación de capitalización definitiva — En el caso de aportes de inversión directa, el cliente debe presentar la documentación que avale la capitalización definitiva del aporte.
  - `e1` Excepcion: Excepción — falta de documentación de capitalización — Cuando el cliente no dispone de la documentación que avala la capitalización definitiva del aporte.
  - `o2` Obligacion: Presentar constancia de inicio de trámite de inscripción — El cliente debe presentar constancia del inicio del trámite de inscripción ante el Registro Público de Comercio de la decisión de capitalización definitiva de los aportes de capital computados de acue
  - `o3` Obligacion: Comprometerse a presentar documentación de capitalización — El cliente debe comprometerse a presentar la documentación de la capitalización definitiva del aporte dentro de los 365 días corridos desde el inicio del trámite.
- relaciones del crudo (sin establecida_en ni de sujeto): e1 exceptua_obligacion o1; e1 condicion_de o2; e1 condicion_de o3
- NODOS A CLASIFICAR:
  - **caso 136** Condicion `c1`: Año calendario — monto aplicado | descripcion: El monto aplicado en el año calendario no debe superar el equivalente al 25% del monto bruto de las inversiones ingresadas para financiar el desarrollo del proyecto que genera las exportaciones aplicadas. | tramo: El monto aplicado en el año calendario no supere el equivalente al 25% (veinticinco por ciento) del monto bruto de las inversiones ingresadas para financiar el desarrollo del proyecto que genera las exportaciones aplicadas
  - **caso 225** Condicion `c2`: Plazo de un año desde liquidación o ingreso aduanero | descripcion: Las inversiones pueden ser computadas solo después de transcurrido un año calendario desde su liquidación en el mercado de cambios y/o el registro de ingreso aduanero de los bienes de capital, según corresponda. | tramo: Las inversiones podrán ser computadas una vez transcurrido un año calendario desde su liquidación en el mercado de cambios y/o el registro de ingreso aduanero de los bienes de capital, según corresponda

## Unidad `ext::3.5.3.5` (item)
- herencia: [chapeau_seccion S3] Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas
en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–,
adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán
cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables. | [intro 3.5] exterior.
Las entidades podrán dar acceso al mercado de cambios para realizar pagos de capital o
intereses de títulos de deuda con registro público en el exterior, otros endeudamientos
financieros con el exterior y títulos de deuda con registro público en el país denominados en
moneda extranjera íntegramente suscriptos en el exterior, en la medida que se verifiquen las
siguientes condiciones: | [intro 3.5.3] (tres) días hábiles a la fecha de vencimiento del servicio de capital o interés a pagar.
En el caso de que se trate de un pago de capital de títulos de deuda emitidos a partir
del 08/11/24 que se concreta con una transferencia al exterior, el acceso al mercado
de cambios deberá adicionalmente producirse una vez transcurridos, como mínimo,
desde la fecha de emisión: | [intro 3.5.3] i) 12 (doce) meses si el título fue emitido entre el 08/11/24 y el 20/04/25.
ii) 6 (seis) meses si el título fue emitido entre 21/04/25 y el 15/05/25.
iii) 18 (dieciocho) meses si el título fue emitido a partir del 16/05/25. | **[abre la lista]** [intro 3.5.3] El acceso al mercado de cambios antes de lo indicado requerirá la conformidad previa
del BCRA excepto que el deudor encuadre en alguna de las siguientes situaciones y
se cumplan la totalidad de las condiciones estipuladas en cada caso:
- texto propio: 3.5.3.5. Precancelación de capital e intereses por parte de un VPU adherido al RIGI.
El cliente es un Vehículo de Proyecto Único (VPU) adherido al Régimen de
Incentivo para Grandes Inversiones (RIGI) que precancela capital o intereses
devengados por endeudamientos financieros comprendidos en este punto
3.5. en el marco de lo previsto en el punto 14.2.1.
- entidades de la unidad:
  - `c1` Condicion: Anterioridad máxima 3 días hábiles — El acceso al mercado de cambios debe producirse con una anterioridad no mayor a 3 días hábiles a la fecha de vencimiento del servicio de capital o interés a pagar
  - `c2` Condicion: Plazo mínimo desde emisión — títulos 08/11/24 a 20/04/25 — Para títulos de deuda emitidos entre el 08/11/24 y el 20/04/25, el acceso al mercado de cambios debe producirse una vez transcurridos, como mínimo, 12 meses desde la fecha de emisión
  - `c3` Condicion: Plazo mínimo desde emisión — títulos 21/04/25 a 15/05/25 — Para títulos de deuda emitidos entre el 21/04/25 y el 15/05/25, el acceso al mercado de cambios debe producirse una vez transcurridos, como mínimo, 6 meses desde la fecha de emisión
  - `c4` Condicion: Plazo mínimo desde emisión — títulos a partir de 16/05/25 — Para títulos de deuda emitidos a partir del 16/05/25, el acceso al mercado de cambios debe producirse una vez transcurridos, como mínimo, 18 meses desde la fecha de emisión
  - `e1` Excepcion: Excepción VPU-RIGI — precancelación de capital e intereses — Quedan exceptuados de los requisitos de anterioridad y plazo mínimo desde emisión los VPU adheridos al RIGI que precancelen capital o intereses devengados por endeudamientos financieros comprendidos e
  - `op1` Operacion: Precancelación de capital e intereses — VPU-RIGI — Precancelación de capital o intereses devengados por endeudamientos financieros comprendidos en el punto 3.5, realizada por un VPU adherido al RIGI
- relaciones del crudo (sin establecida_en ni de sujeto): e1 exceptua c1; e1 exceptua c2; e1 exceptua c3; e1 exceptua c4; e1 condicion_de op1
- NODOS A CLASIFICAR:
  - **caso 137** Condicion `c1`: Anterioridad máxima 3 días hábiles | descripcion: El acceso al mercado de cambios debe producirse con una anterioridad no mayor a 3 días hábiles a la fecha de vencimiento del servicio de capital o interés a pagar | tramo: El acceso al mercado de cambios se produce con una anterioridad no mayor a los 3 (tres) días hábiles a la fecha de vencimiento del servicio de capital o interés a pagar
  - **caso 228** Condicion `c2`: Plazo mínimo desde emisión — títulos 08/11/24 a 20/04/25 | descripcion: Para títulos de deuda emitidos entre el 08/11/24 y el 20/04/25, el acceso al mercado de cambios debe producirse una vez transcurridos, como mínimo, 12 meses desde la fecha de emisión | tramo: 12 (doce) meses si el título fue emitido entre el 08/11/24 y el 20/04/25
  - **caso 229** Condicion `c3`: Plazo mínimo desde emisión — títulos 21/04/25 a 15/05/25 | descripcion: Para títulos de deuda emitidos entre el 21/04/25 y el 15/05/25, el acceso al mercado de cambios debe producirse una vez transcurridos, como mínimo, 6 meses desde la fecha de emisión | tramo: 6 (seis) meses si el título fue emitido entre 21/04/25 y el 15/05/25
  - **caso 230** Condicion `c4`: Plazo mínimo desde emisión — títulos a partir de 16/05/25 | descripcion: Para títulos de deuda emitidos a partir del 16/05/25, el acceso al mercado de cambios debe producirse una vez transcurridos, como mínimo, 18 meses desde la fecha de emisión | tramo: 18 (dieciocho) meses si el título fue emitido a partir del 16/05/25

## Unidad `cap::6.2::intro` (intro)
- herencia: [encabezado 6.2] 6.2. Exigencia de capital por riesgo de tasa de interés.
- texto propio: La exigencia de capital por el riesgo de tasa de interés se deberá calcular respecto de los títu-
los de deuda y otros instrumentos imputados a la cartera de negociación, incluidas las accio-
nes preferidas no convertibles.
Un título valor vendido y recomprado a término en una operación de pase pasivo o en otro tipo
de operación de financiación con títulos valores se tratará como si todavía fuese propiedad de
la entidad cedente; es decir, recibirá el mismo tratamiento que un título en cartera.
Las acciones preferidas convertibles a un precio predeterminado en acciones ordinarias de la
emisora se tratarán según cómo se negocien, como títulos de deuda o como acciones.
La exigencia se obtendrá como la suma de dos exigencias calculadas por separado: una por
el riesgo específico de cada instrumento, ya sea que se trate de una posición vendida o com-
prada, y otra por el riesgo general de mercado –vinculado al efecto de cambios en la tasa de
interés sobre la cartera–, en la que se podrán compensar las posiciones compradas y vendi-
das en diferentes instrumentos.
Para los instrumentos derivados, serán de aplicación las disposiciones establecidas en el pun-
to 6.2.3.
- entidades de la unidad:
  - `e1` Operacion: Cálculo de exigencia de capital por riesgo de tasa de interés — Cálculo de la exigencia de capital por riesgo de tasa de interés sobre títulos de deuda y otros instrumentos imputados a la cartera de negociación, incluidas las acciones preferidas no convertibles.
  - `e2` Operacion: Tratamiento de títulos en operaciones de pase pasivo — Un título valor vendido y recomprado a término en una operación de pase pasivo o en otro tipo de operación de financiación con títulos valores se trata como si todavía fuese propiedad de la entidad ce
  - `e3` Operacion: Tratamiento de acciones preferidas convertibles — Las acciones preferidas convertibles a un precio predeterminado en acciones ordinarias de la emisora se tratan según cómo se negocien, como títulos de deuda o como acciones.
  - `e4` Obligacion: Cálculo de exigencia como suma de dos componentes — La exigencia se obtendrá como la suma de dos exigencias calculadas por separado: una por el riesgo específico de cada instrumento (posición vendida o comprada) y otra por el riesgo general de mercado 
  - `e5` Condicion: Aplicación a instrumentos derivados — Para los instrumentos derivados, se aplican las disposiciones establecidas en el punto 6.2.3.
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 138** Condicion `e5`: Aplicación a instrumentos derivados | descripcion: Para los instrumentos derivados, se aplican las disposiciones establecidas en el punto 6.2.3. | tramo: Para los instrumentos derivados, serán de aplicación las disposiciones establecidas en el punto 6.2.3.

## Unidad `ctacte::10.2.4.1` (punto_no_item)
- herencia: [intro 10.2.4] pago de cheques.
- texto propio: 10.2.4.1. Motivo que origina el cierre (decisión del banco, inclusión en la “Central de
cuentacorrentistas inhabilitados”, etc.), como consecuencia de lo cual serán
de aplicación las normas insertas en la Sección 9.
- entidades de la unidad:
  - `e1` Obligacion: Aviso de motivo del cierre de cuenta — El banco debe informar el motivo que origina el cierre de la cuenta, ya sea por decisión del banco, inclusión en la Central de cuentacorrentistas inhabilitados u otra causa.
  - `e2` Condicion: Aplicación de normas de la Sección 9 — La aplicación de las normas de la Sección 9 se condiciona al cierre de la cuenta o suspensión previa del pago de cheques.
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 139** Condicion `e2`: Aplicación de normas de la Sección 9 | descripcion: La aplicación de las normas de la Sección 9 se condiciona al cierre de la cuenta o suspensión previa del pago de cheques. | tramo: como consecuencia de lo cual serán de aplicación las normas insertas en la Sección 9

## Unidad `cap::6.6.3.2` (punto_no_item)
- herencia: [intro 6.6.3] El método delta-plus utiliza los parámetros de sensibilidad o “letras griegas” asociadas
a las opciones para determinar el equivalente delta de cada posición.
Al equivalente delta de la posición, se le aplicará la metodología estándar de los pun-
tos 6.2. a 6.4., al efecto de calcular la exigencia de capital por riesgo general de mer-
cado para las opciones, al que se agregan exigencias adicionales para la cobertura de
los riesgos gamma –que mide la tasa de cambio del coeficiente delta ante vari
- texto propio: 6.6.3.2. Las posiciones ponderadas por delta cuyo subyacente sean títulos de deuda o
tasas de interés se asignarán a las bandas temporales establecidas en el pun-
to 6.2. Se informarán dos partes de la operación: uno cuando el contrato sub-
yacente entra en vigor y otro cuando vence. Los “caps” o “floors” se deberán
registrar como una combinación de un bono a interés variable y un conjunto
de opciones europeas. Serán de aplicación las disposiciones sobre posiciones
compensadas del acápite i) del punto 6.2.3.5.
- entidades de la unidad:
  - `e1` Operacion: Asignación posiciones delta a bandas temporales — Las posiciones ponderadas por delta cuyo subyacente sean títulos de deuda o tasas de interés se asignan a las bandas temporales establecidas en el punto 6.2.
  - `e2` Obligacion: Información dos partes operación — opciones delta — Se informarán dos partes de la operación: uno cuando el contrato subyacente entra en vigor y otro cuando vence.
  - `e3` Obligacion: Registro caps/floors como combinación — opciones europeas — Los "caps" o "floors" se deberán registrar como una combinación de un bono a interés variable y un conjunto de opciones europeas.
  - `e4` Condicion: Aplicación disposiciones posiciones compensadas — Se aplican las disposiciones sobre posiciones compensadas del acápite i) del punto 6.2.3.5.
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 141** Condicion `e4`: Aplicación disposiciones posiciones compensadas | descripcion: Se aplican las disposiciones sobre posiciones compensadas del acápite i) del punto 6.2.3.5. | tramo: Serán de aplicación las disposiciones sobre posiciones compensadas del acápite i) del punto 6.2.3.5.

## Unidad `cap::3.1.8.1` (punto_no_item)
- herencia: [intro 3.1] Se denomina “posición de titulización” a la exposición a una titulización (o retitulización), tradi-
cional o sintética, o a una estructura con similares características.
La exposición a los riesgos de una titulización puede surgir, entre otros, de los siguientes con-
ceptos: tenencia de títulos valores emitidos en el marco de la titulización –es decir, títulos de
deuda y/o certificados de participación, tales como bonos de titulización de activos (“Asset-
Backed Securities”, ABS) y bonos de tit | [encabezado 3.1.8] 3.1.8. Tratamiento de las titulizaciones con cláusulas de amortización anticipada.
- texto propio: 3.1.8.1. A los efectos de estimar la exigencia de capital, la entidad financiera originante
no podrá excluir las exposiciones objeto de titulización –punto 3.1.2.2.– ni podrá
reconocer el empleo de técnicas de CRC para la cobertura de la posición sub-
yacente en las titulizaciones sintéticas –punto 3.1.7.– si:
i) la entidad origina o patrocina una operación de titulización que incluye una o
más facilidades de crédito rotativas; y
ii) la operación de titulización incluye una cláusula de amortización anticipada
u otra disposición similar que, una vez activada:
a) subordine la participación de la entidad, preferente o de igual prelación
(“pari passu”), a la participación de otros inversores en las facilidades de
crédito rotativas subyacentes;
b) subordine aún más la participación subordinada de la entidad con
respecto a la participación de terceros; o
c) de cualquier otra forma aumente la exposición de la entidad a las pérdi-
das asociadas a las facilidades rotativas subyacentes.
- entidades de la unidad:
  - `e1` Restriccion: Exclusión de exposiciones en titulizaciones con amortización anticipada — La entidad financiera originante no podrá excluir las exposiciones objeto de titulización cuando origina o patrocina una operación de titulización que incluye una o más facilidades de crédito rotativa
  - `e2` Restriccion: Reconocimiento de técnicas CRC en titulizaciones sintéticas con amortización anticipada — La entidad financiera originante no podrá reconocer el empleo de técnicas de CRC para la cobertura de la posición subyacente en las titulizaciones sintéticas cuando origina o patrocina una operación d
  - `e3` Condicion: Originar o patrocinar titulización con facilidades rotativas — La entidad origina o patrocina una operación de titulización que incluye una o más facilidades de crédito rotativas.
  - `e4` Condicion: Cláusula de amortización anticipada activada — La operación de titulización incluye una cláusula de amortización anticipada u otra disposición similar que, una vez activada.
  - `e5` Condicion: Subordinación de participación de la entidad — La cláusula de amortización anticipada subordina la participación de la entidad, preferente o de igual prelación (pari passu), a la participación de otros inversores en las facilidades de crédito rota
  - `e6` Condicion: Subordinación adicional de participación subordinada — La cláusula de amortización anticipada subordina aún más la participación subordinada de la entidad con respecto a la participación de terceros.
  - `e7` Condicion: Aumento de exposición a pérdidas en facilidades rotativas — La cláusula de amortización anticipada de cualquier otra forma aumenta la exposición de la entidad a las pérdidas asociadas a las facilidades rotativas subyacentes.
- relaciones del crudo (sin establecida_en ni de sujeto): e3 condicion_de e1; e3 condicion_de e2; e4 condicion_de e1; e4 condicion_de e2
- NODOS A CLASIFICAR:
  - **caso 143** Condicion `e7`: Aumento de exposición a pérdidas en facilidades rotativas | descripcion: La cláusula de amortización anticipada de cualquier otra forma aumenta la exposición de la entidad a las pérdidas asociadas a las facilidades rotativas subyacentes. | tramo: de cualquier otra forma aumente la exposición de la entidad a las pérdidas asociadas a las facilidades rotativas subyacentes
  - **caso 246** Condicion `e6`: Subordinación adicional de participación subordinada | descripcion: La cláusula de amortización anticipada subordina aún más la participación subordinada de la entidad con respecto a la participación de terceros. | tramo: subordine aún más la participación subordinada de la entidad con respecto a la participación de terceros
  - **caso 247** Condicion `e5`: Subordinación de participación de la entidad | descripcion: La cláusula de amortización anticipada subordina la participación de la entidad, preferente o de igual prelación (pari passu), a la participación de otros inversores en las facilidades de crédito rotativas subyacentes. | tramo: subordine la participación de la entidad, preferente o de igual prelación ("pari passu"), a la participación de otros inversores en las facilidades de crédito rotativas subyacentes

## Unidad `cap::2.1` (punto_no_item)
- herencia: [chapeau_seccion S2] A los efectos de la aplicación de las disposiciones de la presente sección, las entidades financieras
se clasificarán en:
i)Grupo 1: entidades calificadas por el BCRA como de importancia sistémica a nivel local | [chapeau_seccion S2] (D-SIB) y sucursales o subsidiarias de bancos del exterior calificados como de impor-
tancia sistémica global (G-SIB). | [chapeau_seccion S2] ii) Grupo 2: entidades financieras no comprendidas en el acápite i).
En aquellos casos en que no se establezcan disposiciones específicas para cada uno de los citados
grupos de entidades financieras, deberá aplicarse el mismo tratamiento a ambos grupos.
Las entidades financieras que presenten cambios en su calificación –conforme a lo previsto en los
acápites precedentes–, contarán con un plazo de 6 meses para aplicar las disposiciones específicas
correspondientes al nuevo grupo al que pertenezca
- texto propio: 2.1. Exigencia.
Se determinará aplicando la siguiente expresión:
C = (k x 0,08 x APR ) + INC
RC C
donde:
C : exigencia de capital por riesgo de crédito.
RC
k: factor vinculado a la calificación asignada a la entidad según la evaluación efectuada por
la SEFYC, teniendo en cuenta la siguiente escala:
[TABLA cap::tabla001 | página 7 | e0_tablas | columnas]
Columnas: Calificación asignada | Valor de “k”
Fila 1: Calificación asignada = 1 | Valor de “k” = 1
Fila 2: Calificación asignada = 2 | Valor de “k” = 1,03
Fila 3: Calificación asignada = 3 | Valor de “k” = 1,08
Fila 4: Calificación asignada = 4 | Valor de “k” = 1,13
Fila 5: Calificación asignada = 5 | Valor de “k” = 1,19
[FIN TABLA cap::tabla001]
A este efecto, se considerará la última calificación informada para el cálculo de la
exigencia que corresponda integrar al tercer mes siguiente a aquel en que tenga lugar la
notificación. En tanto no se comunique, el valor de “k” será igual a 1,03.
APR : activos ponderados por riesgo de crédito, determinados mediante la suma de los valores
C
obtenidos luego de aplicar la siguiente expresión:
A x p + PFB x CCF x p + no DvP + (DVP + RCD + INC(inversiones empresas)) x 12,5
significativas en
donde:
A: activos computables/exposiciones.
PFB: partidas fuera de balance (conceptos computables no registrados en el balance
de saldos).
CCF: factor de conversión crediticia.
p: ponderador de riesgo, en tanto por uno.
no DvP: operaciones sin entrega contra pago. Importe determinado mediante la suma
de los valores obtenidos luego de aplicar a las operaciones comprendidas el
correspondiente ponderador de riesgo (p) conforme a lo dispuesto en el punto
4.1.
DvP: operaciones de entrega contra pago fallidas (a los efectos de estas normas,
incluyen las operaciones de pago contra pago –PvP– fallidas)
- entidades de la unidad:
  - `e1` Operacion: Cálculo de exigencia de capital por riesgo de crédito — Exigencia de capital por riesgo de crédito (C) determinada mediante la fórmula: C = (k x 0,08 x APR) + INC, donde k es factor vinculado a calificación asignada por SEFYC, APR son activos ponderados po
  - `e2` Definicion: Factor k según calificación SEFYC — Factor vinculado a la calificación asignada a la entidad según evaluación de SEFYC. Valores: calificación 1 = 1; calificación 2 = 1,03; calificación 3 = 1,08; calificación 4 = 1,13; calificación 5 = 1
  - `e3` Obligacion: Aplicación de última calificación informada para cálculo de k — Se considerará la última calificación informada para el cálculo de la exigencia de capital que corresponda integrar al tercer mes siguiente a aquel en que tenga lugar la notificación.
  - `e4` Condicion: Ausencia de comunicación de calificación — Cuando no se comunique calificación de la entidad, el valor de k será igual a 1,03.
  - `e5` Definicion: Activos ponderados por riesgo de crédito (APR) — Activos ponderados por riesgo de crédito, determinados mediante suma de: A x p + PFB x CCF x p + no DvP + (DVP + RCD + INC(inversiones empresas)) x 12,5, donde A son activos computables/exposiciones, 
  - `e6` Definicion: Activos computables/exposiciones (A) — Activos computables/exposiciones.
  - `e7` Definicion: Partidas fuera de balance (PFB) — Partidas fuera de balance, conceptos computables no registrados en el balance de saldos.
  - `e8` Definicion: Factor de conversión crediticia (CCF) — Factor de conversión crediticia.
  - `e9` Definicion: Ponderador de riesgo (p) — Ponderador de riesgo, en tanto por uno.
  - `e10` Definicion: Operaciones sin entrega contra pago (no DvP) — Operaciones sin entrega contra pago. Importe determinado mediante suma de valores obtenidos luego de aplicar a las operaciones comprendidas el correspondiente ponderador de riesgo (p) conforme a lo di
  - `e11` Definicion: Operaciones de entrega contra pago fallidas (DvP) — Operaciones de entrega contra pago fallidas, que incluyen operaciones de pago contra pago (PvP) fallidas. Importe determinado mediante suma de valores obtenidos luego de multiplicar exposición actual 
  - `e12` Definicion: Exigencia por riesgo de crédito de contraparte en derivados OTC (RCD) — Exigencia por riesgo de crédito de contraparte en operaciones con derivados extrabursátiles (over-the-counter, OTC), determinada conforme a lo establecido en punto 4.2.
  - `e13` Restriccion: Límite participación en capital de cada empresa — Límite máximo de participación en el capital de cada empresa del 15% de la responsabilidad patrimonial computable (RPC) de la entidad financiera del último día anterior al que corresponda.
  - `e14` Restriccion: Límite total participaciones en capital de empresas — Límite máximo de total de participaciones en el capital de empresas del 60% de la responsabilidad patrimonial computable (RPC) de la entidad financiera del último día anterior al que corresponda.
  - `e15` Definicion: Incremento por excesos a límites de inversiones en empresas (INC) — Incremento por los excesos a los límites de participación en el capital de cada empresa (15%) y total de participaciones en el capital de empresas (60%), calculados sobre la responsabilidad patrimonia
  - `e16` Definicion: Incremento por excesos a límites diversos (INC) — Incremento por excesos a: relación de activos inmovilizados y otros conceptos (Sección 4 del TO), límites en Financiamiento al Sector Público no Financiero, límites en Grandes Exposiciones al Riesgo d
  - `e17` Obligacion: Aplicación de disposiciones sobre incumplimientos de capitales mínimos — Serán de aplicación las disposiciones contenidas en la Sección 2 del TO sobre Incumplimientos de Capitales Mínimos y Relaciones Técnicas. Criterios Aplicables, salvo que resulte aplicable lo previsto 
  - `e18` Obligacion: Cómputo de exposición crediticia de cupos crediticios ampliados — Se computará en la expresión de APR la exposición crediticia resultante de utilización de cupos crediticios ampliados (puntos 6.1.1.2 y 6.1.2.1 acápite d del TO sobre Financiamiento al Sector Público 
  - `e19` Obligacion: Cómputo de uso de cupo ampliado — 25% primer mes — Cómputo como INC del uso del cupo ampliado: 25% a partir del primer mes de utilización económica de las obras o generación de ingresos.
  - `e20` Obligacion: Cómputo de uso de cupo ampliado — 50% séptimo mes — Cómputo como INC del uso del cupo ampliado: 50% a partir del séptimo mes de utilización económica de las obras o generación de ingresos.
  - `e21` Obligacion: Cómputo de uso de cupo ampliado — 100% décimo tercer mes — Cómputo como INC del uso del cupo ampliado: 100% a partir del décimo tercer mes de utilización económica de las obras o generación de ingresos.
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 145** Condicion `e4`: Ausencia de comunicación de calificación | descripcion: Cuando no se comunique calificación de la entidad, el valor de k será igual a 1,03. | tramo: En tanto no se comunique, el valor de "k" será igual a 1,03.

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

## Unidad `ext::3.17.2::cierre` (cierre)
- herencia: [encabezado 3.17.2] 3.17.2. Los beneficiarios del Régimen de acceso a divisas para la producción incremental de
- texto propio: Si fuese necesario modificar la entidad nominada responsable de lo indicado en los
puntos 3.17.2.1. y/o 3.17.2.2., la nueva entidad será considerada responsable una
vez que el cambio de entidad haya quedado registrado en el BCRA y la entidad
previa le haya remitido el detalle de las certificaciones emitidas a nombre del cliente
hasta ese momento.
- entidades de la unidad:
  - `c1` Condicion: Cambio de entidad nominada responsable — Supuesto en que es necesario modificar la entidad nominada responsable de lo indicado en los puntos 3.17.2.1. y/o 3.17.2.2.
  - `o1` Obligacion: Registro de cambio de entidad en BCRA — La nueva entidad será considerada responsable una vez que el cambio de entidad haya quedado registrado en el BCRA
  - `o2` Obligacion: Remisión de detalle de certificaciones por entidad previa — La entidad previa debe remitir a la nueva entidad el detalle de las certificaciones emitidas a nombre del cliente hasta el momento del cambio
  - `c2` Condicion: Registro en BCRA y remisión de certificaciones — Supuesto en que concurren dos hechos: el cambio de entidad está registrado en el BCRA y la entidad previa ha remitido el detalle de certificaciones
- relaciones del crudo (sin establecida_en ni de sujeto): c2 condicion_de o1
- NODOS A CLASIFICAR:
  - **caso 147** Condicion `c1`: Cambio de entidad nominada responsable | descripcion: Supuesto en que es necesario modificar la entidad nominada responsable de lo indicado en los puntos 3.17.2.1. y/o 3.17.2.2. | tramo: Si fuese necesario modificar la entidad nominada responsable de lo indicado en los puntos 3.17.2.1. y/o 3.17.2.2.

## Unidad `ext::3.15.1` (punto_no_item)
- herencia: [chapeau_seccion S3] Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas
en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–,
adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán
cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables. | [intro 3.15] financiación de operaciones de comercio exterior y garantías financieras otorgadas.
- texto propio: 3.15.1. Cancelación de líneas de crédito del exterior aplicadas por las entidades a la
financiación de operaciones de comercio exterior.
Las entidades financieras tendrán acceso al mercado de cambios a partir del
vencimiento para la cancelación de líneas de crédito otorgadas por entidades
financieras del exterior y aplicadas a la financiación de operaciones de exportación o
importación de residentes.
La cancelación de las líneas destinadas a la financiación de operaciones de
importación de bienes y servicios quedará adicionalmente alcanzada por las
condiciones específicas previstas en los puntos 10.7. y 13.6., respectivamente.
También podrán acceder para precancelar dichas líneas de crédito en la medida que
la financiación otorgada por la entidad local haya sido precancelada por el deudor. El
acceso al mercado de cambios por parte de los clientes para la precancelación de
estas financiaciones requerirá la conformidad previa del BCRA.
La entidad deberá contar con la validación de la declaración del “Relevamiento de
activos y pasivos externos” de la entidad, en la medida que sea aplicable.
- entidades de la unidad:
  - `e1` Operacion: Cancelación líneas crédito exterior — exportación/importación — Cancelación de líneas de crédito otorgadas por entidades financieras del exterior y aplicadas a la financiación de operaciones de exportación o importación de residentes.
  - `e2` Obligacion: Acceso mercado cambios — cancelación líneas crédito — Las entidades financieras tendrán acceso al mercado de cambios a partir del vencimiento para la cancelación de líneas de crédito otorgadas por entidades financieras del exterior y aplicadas a la finan
  - `e3` Condicion: Cancelación líneas importación — condiciones puntos 10.7 y 13.6 — La cancelación de líneas destinadas a la financiación de operaciones de importación de bienes y servicios está sujeta a las condiciones específicas previstas en los puntos 10.7. y 13.6.
  - `e4` Potestad: Precancelación líneas crédito — facultad acceso mercado cambios — Las entidades financieras podrán acceder al mercado de cambios para precancelar líneas de crédito en la medida que la financiación otorgada por la entidad local haya sido precancelada por el deudor.
  - `e5` Condicion: Precancelación por clientes — condición conformidad BCRA — El acceso al mercado de cambios por parte de los clientes para la precancelación de financiaciones requiere conformidad previa del BCRA.
  - `e6` Obligacion: Validación declaración activos pasivos externos — La entidad deberá contar con la validación de la declaración del 'Relevamiento de activos y pasivos externos' de la entidad, en la medida que sea aplicable.
- relaciones del crudo (sin establecida_en ni de sujeto): e2 condiciona e1; e6 condiciona e1
- NODOS A CLASIFICAR:
  - **caso 148** Condicion `e3`: Cancelación líneas importación — condiciones puntos 10.7 y 13.6 | descripcion: La cancelación de líneas destinadas a la financiación de operaciones de importación de bienes y servicios está sujeta a las condiciones específicas previstas en los puntos 10.7. y 13.6. | tramo: La cancelación de las líneas destinadas a la financiación de operaciones de importación de bienes y servicios quedará adicionalmente alcanzada por las condiciones específicas previstas en los puntos 10.7. y 13.6., respectivamente
  - **caso 231** Condicion `e5`: Precancelación por clientes — condición conformidad BCRA | descripcion: El acceso al mercado de cambios por parte de los clientes para la precancelación de financiaciones requiere conformidad previa del BCRA. | tramo: El acceso al mercado de cambios por parte de los clientes para la precancelación de estas financiaciones requerirá la conformidad previa del BCRA

## Unidad `ric::11.1.3` (punto_no_item)
- herencia: [intro 11.1] Conceptos comprendidos.
Se incluirán los flujos de fondos nocionales futuros sujetos a reapreciación de activos, pasi-
vos y partidas fuera de balance sensibles a variaciones en la tasa de interés.
Conceptos excluidos.
- Activos que se deducen del capital ordinario del nivel 1 (COn1);
- Activos fijos;
- Posiciones en acciones en la cartera de inversión.
Frecuencia y consolidación.
Los datos se informarán con frecuencia trimestral y se integrarán con los datos correspon-
dientes al último mes de 
- texto propio: 11.1.3. Instrucciones particulares para los cuadros 11.2.2. a) y 11.2.2. b).
Se aplicarán los criterios especificados anteriormente, considerando la apertura con-
ceptual definida en estos cuadros.
Consecuentemente, el total de flujos de fondos asignados de cada banda debe coin-
cidir con los totales informados en los cuadros 11.2.1. a) y b).
- entidades de la unidad:
  - `e1` Obligacion: Aplicar criterios especificados — cuadros 11.2.2 — Aplicar los criterios especificados anteriormente, considerando la apertura conceptual definida en los cuadros 11.2.2. a) y 11.2.2. b).
  - `e2` Condicion: Coincidencia de totales — flujos de fondos por banda — El total de flujos de fondos asignados de cada banda debe coincidir con los totales informados en los cuadros 11.2.1. a) y b).
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 151** Condicion `e2`: Coincidencia de totales — flujos de fondos por banda | descripcion: El total de flujos de fondos asignados de cada banda debe coincidir con los totales informados en los cuadros 11.2.1. a) y b). | tramo: el total de flujos de fondos asignados de cada banda debe coincidir con los totales informados en los cuadros 11.2.1. a) y b).

## Unidad `ric::S2` (seccion_sin_puntos)
- herencia: 
- texto propio: Sección 2. Entidades comprendidas.
CONSOLIDACIÓN
COD CASOS
0 Entidad que no consolida, con filiales en el país y en el exterior.
1 Entidad que consolida, con filiales en el país y en el exterior.
Consolidado mensual (entidad financiera con filiales y subsidiarias significativas en el país
y en el exterior) – (con el alcance definido en el punto 6.2. de las normas sobre “Su-
2
pervisión consolidada”)
Consolidado mensual (entidad financiera con filiales y subsidiarias significativas en el país y
9 en el exterior -que no consolida con otras entidades financieras-) - (con el alcance defini-
do en el punto 6.2. de las normas sobre “Supervisión consolidada”)
Consolidado trimestral (entidad financiera con filiales, subsidiarias significativas y otros
3
entes en el país y en el exterior) – (código de consolidación suspendido desde
abril/24 según punto 6.1. de las normas sobre “Supervisión consolidada”, excepto
para Ratio de apalancamiento, -Sección 10.- que continuará presentado código 3
con el alcance definido en el punto 6.2. de las normas citadas).
Código 9
No se presentará la información consolidada mensual, debiendo consignar en su lugar una decla-
ración conteniendo los siguientes datos:
- Exigencia por riesgo de crédito (código 70100000).
- Cálculo del riesgo de tasa de interés en la cartera de inversión - Medida de riesgo EVE estan-
darizada (sólo para el último mes del trimestre) (código 70500000).
- Exigencia por riesgo de mercado para las posiciones del último día del mes (código
70800000).
- Exigencia por riesgo operacional (código 70300000).
- Responsabilidad patrimonial computable.
- En los casos que corresponda:
a) Defecto de integración por riesgos de crédito, de mercado y operacional.
b) Incremento de la exigencia de capitales mínimos por excesos en la relación
- entidades de la unidad:
  - `e1` Definicion: Consolidación — código 0 — Entidad que no consolida, con filiales en el país y en el exterior.
  - `e2` Definicion: Consolidación — código 1 — Entidad que consolida, con filiales en el país y en el exterior.
  - `e3` Definicion: Consolidación — código 2 — Consolidado mensual (entidad financiera con filiales y subsidiarias significativas en el país y en el exterior) con el alcance definido en el punto 6.2. de las normas sobre Supervisión consolidada.
  - `e4` Definicion: Consolidación — código 9 — Consolidado mensual (entidad financiera con filiales y subsidiarias significativas en el país y en el exterior -que no consolida con otras entidades financieras-) con el alcance definido en el punto 6
  - `e5` Obligacion: Declaración — código 9 — exigencia riesgo crédito — Entidades con código 9 deberán presentar declaración conteniendo exigencia por riesgo de crédito (código 70100000).
  - `e6` Obligacion: Declaración — código 9 — riesgo tasa interés EVE — Entidades con código 9 deberán presentar declaración conteniendo cálculo del riesgo de tasa de interés en la cartera de inversión - Medida de riesgo EVE estandarizada, sólo para el último mes del trim
  - `e7` Obligacion: Declaración — código 9 — exigencia riesgo mercado — Entidades con código 9 deberán presentar declaración conteniendo exigencia por riesgo de mercado para las posiciones del último día del mes (código 70800000).
  - `e8` Obligacion: Declaración — código 9 — exigencia riesgo operacional — Entidades con código 9 deberán presentar declaración conteniendo exigencia por riesgo operacional (código 70300000).
  - `e9` Obligacion: Declaración — código 9 — responsabilidad patrimonial — Entidades con código 9 deberán presentar declaración conteniendo responsabilidad patrimonial computable.
  - `e10` Obligacion: Declaración — código 9 — defecto integración riesgos — Entidades con código 9 deberán incluir en la declaración, en los casos que corresponda, detalle del defecto de integración por riesgos de crédito, de mercado y operacional.
  - `e11` Obligacion: Declaración — código 9 — incremento exigencia capitales — Entidades con código 9 deberán incluir en la declaración, en los casos que corresponda, incremento de la exigencia de capitales mínimos por excesos en la relación de activos inmovilizados y otros conc
  - `e12` Obligacion: Declaración — código 9 — detalle franquicias — Entidades con código 9 deberán incluir en la declaración, en los casos que corresponda, detalle de las eventuales franquicias otorgadas y otras facilidades.
  - `e13` Obligacion: Declaración — código 9 — reducción exigencia riesgo operacional — Entidades con código 9 deberán incluir en la declaración, en los casos que corresponda, reducción de exigencia de riesgo operacional y los datos para su determinación.
  - `e14` Obligacion: Información — código 3 — frecuencia trimestral — Entidades con código 3 deberán presentar información con frecuencia trimestral, integrada con saldos al cierre del trimestre bajo informe.
  - `e15` Obligacion: Información — código 3 — datos códigos 0, 1, 2 — Entidades con código 3 deberán incluir los datos previstos para los códigos 0, 1 y 2, excepto en el caso de riesgo de mercado y riesgo operacional, donde se informarán únicamente las partidas 70800000
  - `e16` Excepcion: Excepción — código 3 — riesgo mercado y operacional — Para entidades con código 3, en el caso de riesgo de mercado y riesgo operacional se informarán únicamente las partidas 70800000 y 70300000 y, de corresponder, 3600000Y y 37000000, en lugar de los dat
  - `e17` Obligacion: Cómputo — código 3 — instrucciones mensuales — Para determinar las exigencias de código 3, se tendrán en cuenta las instrucciones establecidas para el cómputo mensual, en lo que resulte pertinente.
  - `e18` Condicion: Condición — código 3 — suspensión desde abril/24 — Código 3 de consolidación trimestral está suspendido desde abril/24 según punto 6.1. de las normas sobre Supervisión consolidada, excepto para Ratio de apalancamiento (Sección 10) que continuará prese
- relaciones del crudo (sin establecida_en ni de sujeto): e16 exceptua_obligacion e15
- NODOS A CLASIFICAR:
  - **caso 153** Condicion `e18`: Condición — código 3 — suspensión desde abril/24 | descripcion: Código 3 de consolidación trimestral está suspendido desde abril/24 según punto 6.1. de las normas sobre Supervisión consolidada, excepto para Ratio de apalancamiento (Sección 10) que continuará presentando código 3. | tramo: código de consolidación suspendido desde abril/24 según punto 6.1. de las normas sobre "Supervisión consolidada", excepto para Ratio de apalancamiento, -Sección 10.- que continuará presentado código 3

## Unidad `ext::2.7::cierre` (cierre)
- herencia: [encabezado 2.7] 2.7. Otras excepciones a la obligación de liquidación.
- texto propio: A los efectos del registro de estas operaciones se deberán confeccionar dos boletos sin
movimiento de pesos, por los conceptos de compra y venta que correspondan, computándose
el monto por el cual se utiliza este mecanismo a los efectos de los límites mensuales que
pudieran ser aplicables según el caso.
En todos los casos se deberá contar con una declaración jurada del cliente en la que deja
constancia de tener conocimiento de que los fondos que se aplican bajo esta modalidad serán
computados a los efectos del cálculo de los límites que normativamente correspondan al
concepto de venta de cambio que corresponda y que no los excede.
- entidades de la unidad:
  - `e1` Operacion: Confección de boletos sin movimiento de pesos — Confección de dos boletos sin movimiento de pesos, por los conceptos de compra y venta que correspondan, para el registro de operaciones bajo la modalidad de excepciones a la obligación de liquidación
  - `e2` Obligacion: Cómputo de monto en límites mensuales — El monto utilizado bajo esta modalidad debe computarse a los efectos de los límites mensuales que pudieran ser aplicables según el caso.
  - `e3` Obligacion: Declaración jurada del cliente — conocimiento de cómputo — Debe contarse con una declaración jurada del cliente en la que conste que tiene conocimiento de que los fondos aplicados bajo esta modalidad serán computados a los efectos del cálculo de los límites q
  - `e4` Restriccion: Límite — fondos no exceden límites aplicables — Los fondos que se aplican bajo esta modalidad no deben exceder los límites que normativamente correspondan al concepto de venta de cambio que corresponda.
  - `e5` Condicion: Condición — declaración jurada del cliente — La operación bajo esta modalidad requiere que el cliente otorgue una declaración jurada en la que conste su conocimiento del cómputo de los fondos en los límites y que esos fondos no exceden los límit
- relaciones del crudo (sin establecida_en ni de sujeto): e3 condiciona e1; e4 limita e1
- NODOS A CLASIFICAR:
  - **caso 154** Condicion `e5`: Condición — declaración jurada del cliente | descripcion: La operación bajo esta modalidad requiere que el cliente otorgue una declaración jurada en la que conste su conocimiento del cómputo de los fondos en los límites y que esos fondos no exceden los límites aplicables. | tramo: En todos los casos se deberá contar con una declaración jurada del cliente

## Unidad `cap::4.3.1.1` (punto_no_item)
- herencia: [intro 4.3] contraparte central.
Comprende a aquellas exposiciones de las entidades financieras con entidades de contrapar-
te central (CCP) que se originen en derivados OTC o negociados en mercados de valores y
en operaciones de financiación con títulos valores (“Securities Financing Transactions”, SFT)
y operaciones de liquidación diferida –definidas en el punto 4.2.–.
No están comprendidas las exposiciones originadas en operaciones al contado y que involu-
cren títulos valores, oro o moneda extranjera, c | [encabezado 4.3.1] 4.3.1. Definiciones.
- texto propio: 4.3.1.1. Entidad de contraparte central calificada (“Qualifying Central Counterparty”,
QCCP): aquella entidad autorizada a operar como CCP por el regulador de
su jurisdicción –en el país, la Comisión Nacional de Valores (CNV)– en
relación a los productos que ofrece, que se encuentre radicada y sea
supervisada en una jurisdicción en la que el regulador ha establecido –y
hecho público que aplica a dicha CCP en forma permanente– regulaciones
compatibles con las normas sobre “Principios para las infraestructuras del
mercado financiero”.
En el caso de que la CCP esté localizada en una jurisdicción en la que no
le sean aplicables los citados Principios, el BCRA podrá determinar que de
todos modos encuadra en la categoría de QCCP.
Además, a efectos de que la CCP pueda ser considerada QCCP, deberá
estar disponible la información necesaria para el cómputo de la exigencia
de capital para la exposición a fondos de garantía constituidos para hacer
frente a incumplimientos, conforme a lo previsto en el acápite ii) del punto
4.3.3.2.
Las entidades financieras podrán considerar como QCCP a la CCP que,
de acuerdo con las normas de la CNV,:
i) cuente con un informe de su auditoría externa acerca de si cumple o
cumple en general con los principios y recomendaciones de la Organi-
zación Internacional de Comisiones de Valores ("International Organi-
zation of Securities Commissions", IOSCO) y del Comité de Pagos e
Infraestructuras del Mercado ("Committee on Payments and Market In-
frastructures", CPMI) y,
ii) brinde la información necesaria para el cómputo de la exigencia de ca-
pital por riesgo de crédito de contraparte por la exposición de las enti-
dades financieras a los fondos de garantía constituidos para hacer
frente a incumplimientos (punto 4.3.3.2.).
- entidades de la unidad:
  - `e1` Definicion: QCCP — Entidad de contraparte central calificada — Aquella entidad autorizada a operar como CCP por el regulador de su jurisdicción (en Argentina, la CNV) en relación a los productos que ofrece, que se encuentre radicada y sea supervisada en una juris
  - `e2` Condicion: Condición — CCP en jurisdicción sin Principios aplicables — La CCP está localizada en una jurisdicción en la que no le son aplicables los Principios para las infraestructuras del mercado financiero.
  - `e3` Potestad: BCRA — Determinar QCCP en jurisdicción sin Principios — El BCRA tiene la facultad de determinar que una CCP encuadra en la categoría de QCCP aun cuando esté localizada en una jurisdicción en la que no le sean aplicables los Principios para las infraestruct
  - `e5` Condicion: Condición — Disponibilidad de información para cómputo de capital — Debe estar disponible la información necesaria para el cómputo de la exigencia de capital para la exposición a fondos de garantía constituidos para hacer frente a incumplimientos, conforme a lo previs
  - `e6` Obligacion: Entidades financieras — Considerar QCCP según normas CNV — Las entidades financieras tienen la facultad de considerar como QCCP a una CCP que cumpla con los requisitos establecidos en las normas de la CNV.
  - `e7` Condicion: Condición — Informe de auditoría externa sobre cumplimiento IOSCO/CPMI — La CCP cuenta con un informe de su auditoría externa acerca de si cumple o cumple en general con los principios y recomendaciones de IOSCO y del CPMI.
  - `e8` Condicion: Condición — Información para cómputo de capital por riesgo de crédito — La CCP brinda la información necesaria para el cómputo de la exigencia de capital por riesgo de crédito de contraparte por la exposición de las entidades financieras a los fondos de garantía constitui
- relaciones del crudo (sin establecida_en ni de sujeto): e2 condicion_de e3; e7 condicion_de e6; e8 condicion_de e6
- NODOS A CLASIFICAR:
  - **caso 155** Condicion `e5`: Condición — Disponibilidad de información para cómputo de capital | descripcion: Debe estar disponible la información necesaria para el cómputo de la exigencia de capital para la exposición a fondos de garantía constituidos para hacer frente a incumplimientos, conforme a lo previsto en el acápite ii) del punto 4.3.3.2. | tramo: deberá estar disponible la información necesaria para el cómputo de la exigencia de capital para la exposición a fondos de garantía constituidos para hacer frente a incumplimientos, conforme a lo previsto en el acápite ii) del punto 4.3.3.2

## Unidad `cap::8.6::cierre` (cierre)
- herencia: [encabezado 8.6] 8.6. Aportes de capital.
- texto propio: En los casos comprendidos en los puntos 8.6.1. y 8.6.2., los aportes deberán registrarse a su
valor de mercado. Se entenderá que los instrumentos cuentan con valor de mercado cuando
tengan cotización habitual en las bolsas y mercados regulados del país o del exterior en los
que se negocien, con transacciones relevantes en cuyo monto, la eventual liquidación de las
tenencias no pueda distorsionar significativamente su cotización.
En los casos del punto 8.6.3., los aportes deberán registrarse a su valor de mercado –con el al-
cance definido en el párrafo anterior– o, cuando se trate de entidades financieras que realicen
oferta pública de sus acciones, al precio que fije la autoridad de contralor competente del co-
rrespondiente mercado. No se admitirán los aportes de esta clase de instrumentos cuando no
se verifique el cumplimiento de las condiciones mencionadas precedentemente.
Cuando se trate de depósitos y otras obligaciones por intermediación financiera de la entidad
financiera que no cuenten con autorización para ser negociados en mercados secundarios re-
gulados del país o del exterior, los aportes se admitirán a su valor contable –capital, intereses,
ajustes, diferencias de cotización por moneda extranjera y, de corresponder, descuentos de
emisión–, conforme a las normas del BCRA. En el caso de los instrumentos de deuda compu-
tables como CA o PNc, al admitir los aportes, se deberá tener en cuenta lo dispuesto en el
n1
punto 8.3.4.
En ningún caso la capitalización de deuda podrá implicar una limitación o suspensión al dere-
cho de preferencia establecido en el artículo 194 de la Ley General de Sociedades, por lo que
no será aplicable lo dispuesto en el artículo 197 de dicha ley.
La decisión de capitalización de los conceptos indicados en los puntos 8.6.1. a 8.6.3. 
- entidades de la unidad:
  - `e1` Operacion: Registro de aportes a valor de mercado — Registro de aportes a su valor de mercado en los casos comprendidos en los puntos 8.6.1. y 8.6.2., cuando los instrumentos tengan cotización habitual en bolsas y mercados regulados del país o del exte
  - `e2` Definicion: Valor de mercado — instrumentos cotizados — Los instrumentos cuentan con valor de mercado cuando tengan cotización habitual en las bolsas y mercados regulados del país o del exterior en los que se negocien, con transacciones relevantes en cuyo 
  - `e3` Operacion: Registro de aportes punto 8.6.3. a valor de mercado o precio de autoridad — En los casos del punto 8.6.3., registro de aportes a su valor de mercado o, cuando se trate de entidades financieras que realicen oferta pública de sus acciones, al precio que fije la autoridad de con
  - `e4` Restriccion: Prohibición de aportes sin cumplimiento de condiciones — No se admitirán los aportes de instrumentos del punto 8.6.3. cuando no se verifique el cumplimiento de las condiciones de valor de mercado o precio de autoridad mencionadas precedentemente.
  - `e5` Operacion: Registro de depósitos y obligaciones a valor contable — Cuando se trate de depósitos y otras obligaciones por intermediación financiera de la entidad financiera que no cuenten con autorización para ser negociados en mercados secundarios regulados del país 
  - `e6` Condicion: Condición — instrumentos de deuda CA o PNc — Cuando se trate de instrumentos de deuda computables como CA o PNc, al admitir los aportes se debe tener en cuenta lo dispuesto en el punto 8.3.4.
  - `e7` Restriccion: Prohibición — capitalización de deuda no limita derecho de preferencia — La capitalización de deuda no podrá implicar una limitación o suspensión al derecho de preferencia establecido en el artículo 194 de la Ley General de Sociedades; por lo tanto, no será aplicable lo di
  - `e8` Obligacion: Decisión de capitalización ad referéndum de aprobación — La decisión de capitalización de los conceptos indicados en los puntos 8.6.1. a 8.6.3. por parte de la Asamblea (o autoridad equivalente) será ad referéndum de su aprobación por parte de la SEFyC o, e
  - `e9` Obligacion: Exposición en nota a estados contables de capitalización — La circunstancia de que la capitalización está ad referéndum de aprobación deberá ser expuesta en nota a los estados contables de los períodos siguientes (trimestral o anual, según corresponda), en lo
  - `e10` Obligacion: Deducción de aportes de RPC hasta notificación de aprobación — Hasta tanto se le haya notificado la aprobación de los aportes y en la medida en que éstos hayan sido contabilizados, se deducirán del respectivo componente de la RPC de la entidad financiera.
  - `e11` Obligacion: Mantenimiento de tratamiento de deuda subordinada capitalizada — Cuando los aportes contabilizados provengan de la capitalización de deuda subordinada o de instrumentos representativos de deuda que puedan ser considerados (total o parcialmente) como parte integrant
  - `e12` Comunicacion: Com. Autorización y composición del capital — 
- relaciones del crudo (sin establecida_en ni de sujeto): to referencia e12
- NODOS A CLASIFICAR:
  - **caso 156** Condicion `e6`: Condición — instrumentos de deuda CA o PNc | descripcion: Cuando se trate de instrumentos de deuda computables como CA o PNc, al admitir los aportes se debe tener en cuenta lo dispuesto en el punto 8.3.4. | tramo: En el caso de los instrumentos de deuda computables como CA o PNc, al admitir los aportes, se deberá tener en cuenta lo dispuesto en el punto 8.3.4

## Unidad `cap::3.1.7` (punto_no_item)
- herencia: [intro 3.1] Se denomina “posición de titulización” a la exposición a una titulización (o retitulización), tradi-
cional o sintética, o a una estructura con similares características.
La exposición a los riesgos de una titulización puede surgir, entre otros, de los siguientes con-
ceptos: tenencia de títulos valores emitidos en el marco de la titulización –es decir, títulos de
deuda y/o certificados de participación, tales como bonos de titulización de activos (“Asset-
Backed Securities”, ABS) y bonos de tit
- texto propio: 3.1.7. Tratamiento de las operaciones sintéticas.
El empleo de técnicas de coberturas del riesgo de crédito (CRC) –tales como activos
admitidos como garantía, garantías personales y derivados de crédito– para cubrir la po-
sición subyacente se podrá reconocer a efectos de determinar la exigencia de capital co-
rrespondiente a titulizaciones sintéticas sólo si se satisfacen las siguientes condiciones:
i) Las coberturas del riesgo de crédito cumplen los requisitos establecidos en la Sec-
ción 5.
ii) Los activos admitidos como garantía se limitan a los especificados en los puntos
5.3.1.2. y 5.3.2.2. Podrán reconocerse los activos admisibles dados en garantía por
“entes de propósito especial” (SPE).
iii) Los garantes admisibles se limitan a los estipulados en el punto 5.4.1. Los SPE no
son garantes admisibles.
iv) La entidad transfiere a terceros el riesgo de crédito asociado a las exposiciones
subyacentes.
v) Los instrumentos utilizados para transferir el riesgo de crédito no contienen cláusu-
las o condiciones que limiten la cantidad del riesgo de crédito transferido, tales como
las siguientes:
a) Cláusulas que limiten de forma considerable la protección crediticia o la transfe-
rencia del riesgo de crédito, tales como cláusulas de amortización anticipada en
una titulización de facilidades crediticias rotativas que produzcan el efecto de
subordinar los derechos de la entidad financiera, umbrales por debajo de los cua-
les no se active la protección crediticia –incluso si se produce un evento de crédi-
to– establecidos en niveles elevados, o cláusulas que permitan la extinción de la
protección debido al deterioro de la calidad crediticia de las posiciones subyacen-
tes.
b) Cláusulas que obliguen a la entidad originante a alterar las exposiciones subya-
centes para mejorar 
- entidades de la unidad:
  - `e1` Operacion: Cobertura de riesgo de crédito en titulizaciones sintéticas — Empleo de técnicas de coberturas del riesgo de crédito (CRC) tales como activos admitidos como garantía, garantías personales y derivados de crédito para cubrir la posición subyacente en titulizacione
  - `e2` Obligacion: Reconocimiento de coberturas — requisitos de Sección 5 — Las coberturas del riesgo de crédito deben cumplir los requisitos establecidos en la Sección 5 para ser reconocidas a efectos de determinar la exigencia de capital en titulizaciones sintéticas
  - `e3` Restriccion: Límite cualitativo — activos admitidos como garantía — Los activos admitidos como garantía se limitan a los especificados en los puntos 5.3.1.2. y 5.3.2.2.
  - `e4` Excepcion: Excepción — SPE como garantes de activos en garantía — Se permite el reconocimiento de activos admisibles dados en garantía por entes de propósito especial (SPE), como excepción a la limitación de activos admitidos como garantía
  - `e5` Restriccion: Límite cualitativo — garantes admisibles — Los garantes admisibles se limitan a los estipulados en el punto 5.4.1.
  - `e6` Restriccion: Prohibición — SPE como garantes — Los entes de propósito especial (SPE) no son garantes admisibles
  - `e7` Obligacion: Transferencia de riesgo de crédito a terceros — La entidad debe transferir a terceros el riesgo de crédito asociado a las exposiciones subyacentes
  - `e8` Restriccion: Prohibición — cláusulas limitantes de protección crediticia — Los instrumentos utilizados para transferir el riesgo de crédito no pueden contener cláusulas o condiciones que limiten la cantidad del riesgo de crédito transferido
  - `e9` Restriccion: Prohibición — cláusulas de amortización anticipada subordinante — Se prohíben cláusulas de amortización anticipada en una titulización de facilidades crediticias rotativas que produzcan el efecto de subordinar los derechos de la entidad financiera
  - `e10` Restriccion: Prohibición — umbrales elevados de activación de protección — Se prohíben umbrales por debajo de los cuales no se active la protección crediticia, incluso si se produce un evento de crédito, cuando están establecidos en niveles elevados
  - `e11` Restriccion: Prohibición — cláusulas de extinción por deterioro crediticio — Se prohíben cláusulas que permitan la extinción de la protección debido al deterioro de la calidad crediticia de las posiciones subyacentes
  - `e12` Restriccion: Prohibición — obligación de alterar exposiciones subyacentes — Se prohíben cláusulas que obliguen a la entidad originante a alterar las exposiciones subyacentes para mejorar la calidad crediticia promedio del conjunto de activos subyacente
  - `e13` Restriccion: Prohibición — incremento de costo de protección por deterioro crediticio — Se prohíben cláusulas que incrementen el costo de la protección crediticia para la entidad en respuesta al deterioro en la calidad crediticia del conjunto de activos subyacente
  - `e14` Restriccion: Prohibición — incremento de rendimiento a terceros por deterioro crediticio — Se prohíben cláusulas que incrementen el rendimiento pagadero a partes distintas de la entidad originante, tales como inversores y terceros proveedores de mejoras crediticias, en respuesta al deterior
  - `e15` Restriccion: Prohibición — aumento de posición a primera pérdida post-inicio — Se prohíben cláusulas que contemplen aumentos de la posición a primera pérdida retenida o de las mejoras crediticias provistas por la entidad originante después del inicio de la operación
  - `e16` Obligacion: Dictamen jurídico — exigibilidad del contrato — Debe contarse con dictamen jurídico competente que confirme la exigibilidad del contrato
  - `e17` Condicion: Opciones de exclusión — requisitos del punto 3.1.4 — Las opciones de exclusión deben satisfacer las condiciones estipuladas en el punto 3.1.4
  - `e18` Condicion: Condición — satisfacción de todas las condiciones enumeradas — El reconocimiento de coberturas del riesgo de crédito para determinar la exigencia de capital en titulizaciones sintéticas está condicionado a la satisfacción de todas las condiciones enumeradas (i a 
- relaciones del crudo (sin establecida_en ni de sujeto): e2 condicion_de e1; e3 condicion_de e1; e5 condicion_de e1; e7 condicion_de e1; e8 condicion_de e1; e16 condicion_de e1; e17 condicion_de e1; e4 exceptua e3; e8 prohibe e1; e9 prohibe e1; e10 prohibe e1; e11 prohibe e1; e12 prohibe e1; e13 prohibe e1; e14 prohibe e1; e15 prohibe e1
- NODOS A CLASIFICAR:
  - **caso 157** Condicion `e18`: Condición — satisfacción de todas las condiciones enumeradas | descripcion: El reconocimiento de coberturas del riesgo de crédito para determinar la exigencia de capital en titulizaciones sintéticas está condicionado a la satisfacción de todas las condiciones enumeradas (i a vii) | tramo: se podrá reconocer a efectos de determinar la exigencia de capital correspondiente a titulizaciones sintéticas sólo si se satisfacen las siguientes condiciones

## Unidad `ext::7.7` (punto_no_item)
- herencia: [encabezado S7] Sección 7. Cobros de exportaciones de bienes.
- texto propio: 7.7. Cancelación de anticipos u otras financiaciones de exportación sin aplicación de divisas por
cobros de exportaciones de bienes.
Dadas las características que definen a los anticipos, prefinanciaciones de exportaciones -
locales o externas- y otras financiaciones de exportación, estas operaciones deberán ser
canceladas con fondos originados en el cobro de exportaciones de bienes, salvo que el cliente
pueda demostrar que no puede hacerlo de dicha forma por causas ajenas a su voluntad (por
ejemplo: desistimiento de la operación por parte del comprador externo, falta de pago por
parte del comprador externo, etc.).
El acceso al mercado local de cambios para cancelar anticipos u otras financiaciones de
exportaciones del exterior sin aplicación de divisas de cobros de exportaciones de bienes se
regirá por las normas para la cancelación de servicios de capital de préstamos financieros.
El acceso al mercado de cambios por parte de clientes para la precancelación de
financiaciones de exportación otorgadas por entidades financieras locales quedará sujeto a la
conformidad previa del BCRA. Este requisito se considerará cumplimentado en la medida que
el cliente registre, en la fecha de acceso al mercado, liquidaciones por cobros de
exportaciones de bienes por un monto igual o mayor al que se precancela a la entidad
financiera local.
En el caso de operaciones comprendidas en el “Seguimiento de anticipos y otras
financiaciones de exportación de bienes” (Sección 9.), la entidad para dar acceso al mercado
de cambios deberá contar con la correspondiente certificación por parte de la entidad
encargada del seguimiento de la financiación.
Los exportadores que registren anticipos u otras financiaciones de exportación comprendidas
en el “Seguimiento de anticipos y otras financiaciones de 
- entidades de la unidad:
  - `e1` Operacion: Cancelación de anticipos u otras financiaciones de exportación — Cancelación de anticipos, prefinanciaciones de exportaciones (locales o externas) y otras financiaciones de exportación sin aplicación de divisas por cobros de exportaciones de bienes
  - `e2` Obligacion: Cancelación con fondos de cobros de exportación — Las operaciones de anticipos, prefinanciaciones de exportaciones y otras financiaciones de exportación deberán ser canceladas con fondos originados en el cobro de exportaciones de bienes
  - `e3` Excepcion: Excepción por causas ajenas a la voluntad del cliente — No aplica la obligación de cancelación con fondos de cobros de exportación cuando el cliente demuestra que no puede hacerlo por causas ajenas a su voluntad
  - `e4` Obligacion: Acceso al mercado local de cambios — cancelación de anticipos — El acceso al mercado local de cambios para cancelar anticipos u otras financiaciones de exportaciones del exterior sin aplicación de divisas de cobros de exportaciones de bienes se regirá por las norm
  - `e5` Condicion: Conformidad previa del BCRA — precancelación de financiaciones — El acceso al mercado de cambios para precancelación de financiaciones de exportación otorgadas por entidades financieras locales requiere conformidad previa del BCRA
  - `e6` Excepcion: Cumplimiento de conformidad previa — liquidaciones de cobros — La conformidad previa del BCRA se considera cumplida cuando el cliente registra liquidaciones por cobros de exportaciones de bienes por monto igual o mayor al que se precancela
  - `e7` Condicion: Operaciones en Seguimiento de anticipos y financiaciones — Operaciones comprendidas en el Seguimiento de anticipos y otras financiaciones de exportación de bienes (Sección 9)
  - `e8` Obligacion: Certificación para acceso al mercado de cambios — La entidad debe contar con certificación de la entidad encargada del seguimiento de la financiación para dar acceso al mercado de cambios en operaciones comprendidas en el Seguimiento de anticipos y o
  - `e9` Obligacion: Notificación de disminución de capital adeudado — Los exportadores con anticipos u otras financiaciones de exportación por deudas directas no garantizadas por entidades financieras locales deben notificar a la entidad encargada del seguimiento cualqu
  - `e10` Definicion: Anticipos y prefinanciaciones de exportación — Operaciones que se caracterizan por ser anticipos, prefinanciaciones de exportaciones (locales o externas) y otras financiaciones de exportación
- relaciones del crudo (sin establecida_en ni de sujeto): e3 exceptua_obligacion e2; e6 exceptua_obligacion e5; e7 condicion_de e8
- NODOS A CLASIFICAR:
  - **caso 158** Condicion `e5`: Conformidad previa del BCRA — precancelación de financiaciones | descripcion: El acceso al mercado de cambios para precancelación de financiaciones de exportación otorgadas por entidades financieras locales requiere conformidad previa del BCRA | tramo: El acceso al mercado de cambios por parte de clientes para la precancelación de financiaciones de exportación otorgadas por entidades financieras locales quedará sujeto a la conformidad previa del BCRA

## Unidad `cla::7.2.2.1` (punto_no_item)
- herencia: [encabezado 7.2.2] 7.2.2. Riesgo bajo.
- texto propio: 7.2.2.1. En observación.
Comprende los clientes que registran incumplimientos ocasionales en la atención
de sus obligaciones, con atrasos de más de 31 hasta 90 días.
En cuanto a la situación jurídica del deudor, se considerará si mantiene conve-
nios de pago resultantes de concordatos judiciales o extrajudiciales homologados
(incluyendo los acuerdos preventivos extrajudiciales homologados) a vencer
cuando se haya cancelado, al menos, el 10 % del importe involucrado en el cita-
do acuerdo.
Los clientes cuyas deudas hayan sido refinanciadas mediante obligaciones de
pago periódico (mensual o bimestral) podrán ser reclasificados en el nivel inme-
diato superior, cuando hayan cumplido puntualmente o con atrasos que no su-
peren los 31 días, con el pago de 1 cuota o, cuando se trate de financiaciones de
pago único, periódico superior a bimestral o irregular, hayan cancelado al menos
el 5 % de sus obligaciones refinanciadas (por capital), con más la cantidad de
cuotas o el porcentaje acumulado que pudiera corresponder, respectivamente, si
la refinanciación se hubiera otorgado de encontrarse incluido el deudor en nive-
les inferiores.
El deudor que, encontrándose clasificado en esta categoría, haya refinanciado su
deuda –aun cuando haya cancelado la cuota citada en el párrafo precedente– y
recibido crédito adicional en los términos a que se refiere el punto 2.2.5. de las
normas sobre “Previsiones mínimas por riesgo de incobrabilidad”, y en la medida
en que dicha financiación adicional no hubiese sido cancelada, deberá permane-
cer en esta categoría por lo menos 180 días contados desde la fecha en que se
otorgó el crédito adicional o desde que se celebró el acuerdo de refinanciación, la
circunstancia más reciente.
En caso de verificarse atrasos mayores a 31 días en el pago de lo
- entidades de la unidad:
  - `e1` Definicion: En observación — deudores cartera consumo/vivienda — Categoría de clasificación que comprende los clientes que registran incumplimientos ocasionales en la atención de sus obligaciones, con atrasos de más de 31 hasta 90 días.
  - `e2` Condicion: Convenios de pago homologados — cancelación 10 % — Condición relativa a la situación jurídica del deudor: se considera si mantiene convenios de pago homologados a vencer cuando se haya cancelado al menos el 10 % del importe involucrado.
  - `e3` Operacion: Reclasificación a nivel inmediato superior — deudas refinanciadas — Reclasificación de clientes con deudas refinanciadas mediante obligaciones de pago periódico (mensual o bimestral) al nivel inmediato superior, cuando hayan cumplido puntualmente o con atrasos no supe
  - `e4` Condicion: Cumplimiento puntual o atrasos ≤ 31 días — 1 cuota — Condición para reclasificación: cumplimiento puntual o atrasos que no superen los 31 días, con el pago de 1 cuota.
  - `e5` Condicion: Cancelación 5 % obligaciones refinanciadas — pago único/irregular — Condición para reclasificación en financiaciones de pago único, periódico superior a bimestral o irregular: cancelación de al menos el 5 % de las obligaciones refinanciadas (por capital).
  - `e6` Restriccion: Permanencia mínima 180 días — crédito adicional — El deudor clasificado en esta categoría que haya refinanciado su deuda y recibido crédito adicional en los términos del punto 2.2.5 de las normas sobre Previsiones mínimas por riesgo de incobrabilidad
  - `e7` Condicion: Atrasos mayores a 31 días — servicios deuda refinanciada — Condición que activa reclasificación inmediata: verificación de atrasos mayores a 31 días en el pago de los servicios de la deuda refinanciada contados a partir de la inclusión del deudor en esta cate
  - `e8` Operacion: Reclasificación inmediata — atrasos mayores a 31 días — Reclasificación inmediata del deudor en el nivel que resulte de considerar la cantidad total de días de atraso (días efectivamente registrados desde la primera cuota impaga de la refinanciación más lo
  - `e9` Condicion: Deudas refinanciadas — obligaciones pago periódico — Condición: deudas refinanciadas mediante obligaciones de pago periódico (mensual o bimestral).
- relaciones del crudo (sin establecida_en ni de sujeto): e4 condicion_de e3; e5 condicion_de e3; e9 condicion_de e3; e7 condicion_de e8
- NODOS A CLASIFICAR:
  - **caso 160** Condicion `e2`: Convenios de pago homologados — cancelación 10 % | descripcion: Condición relativa a la situación jurídica del deudor: se considera si mantiene convenios de pago homologados a vencer cuando se haya cancelado al menos el 10 % del importe involucrado. | tramo: se considerará si mantiene convenios de pago resultantes de concordatos judiciales o extrajudiciales homologados (incluyendo los acuerdos preventivos extrajudiciales homologados) a vencer cuando se haya cancelado, al menos, el 10 % del importe involucrado en el citado acuerdo.

## Unidad `cla::7.2.3` (punto_no_item)
- herencia: [encabezado 7.2] 7.2. Niveles de clasificación.
- texto propio: 7.2.3. Riesgo medio.
Comprende los clientes que muestran alguna incapacidad para cancelar sus obligacio-
nes, con atrasos de más de 90 hasta 180 días.
En cuanto a la situación jurídica del deudor, se considerará si mantiene convenios de pa-
go resultantes de concordatos judiciales o extrajudiciales homologados (incluyendo los
acuerdos preventivos extrajudiciales homologados) a vencer cuando aún no se haya can-
celado el 10 % del importe involucrado en el citado acuerdo.
A fin de determinar el importe de la cancelación, se admitirá computar el 50 % de las ga-
rantías adicionales a las ofrecidas originalmente, constituidas sobre bienes no vinculados
a la explotación del deudor –con excepción de las hipotecas sobre inmuebles rurales que,
por lo tanto, serán computables–, observando los márgenes de cobertura establecidos en
las normas sobre “Garantías”.
Los clientes cuyas deudas hayan sido refinanciadas mediante obligaciones de pago pe-
riódico (mensual o bimestral) podrán ser reclasificados en el nivel inmediato superior,
cuando hayan cumplido puntualmente o con atrasos que no superen los 31 días, con el
pago de 2 cuotas consecutivas o, cuando se trate de financiaciones de pago único, perió-
dico superior a bimestral o irregular, hayan cancelado al menos el 5 % de sus obligacio-
nes refinanciadas (por capital), con más la cantidad de cuotas o el porcentaje acumulado
que pudiera corresponder, respectivamente, si la refinanciación se hubiera otorgado de
encontrarse incluido el deudor en el nivel inferior.
El deudor refinanciado que haya cumplido con lo dispuesto en los párrafos precedentes,
según corresponda, podrá ser reclasificado en el nivel inmediato superior si, además, el
resto de sus deudas reúnen, como mínimo, las condiciones previstas en el citado nivel.
El deudor q
- entidades de la unidad:
  - `e1` Definicion: Riesgo medio — deudores — Categoría que comprende los clientes que muestran alguna incapacidad para cancelar sus obligaciones, con atrasos de más de 90 hasta 180 días.
  - `e2` Condicion: Convenios de pago — situación jurídica — Se considera la situación jurídica del deudor respecto a convenios de pago de concordatos judiciales o extrajudiciales homologados, incluyendo acuerdos preventivos extrajudiciales homologados, cuando 
  - `e3` Obligacion: Computar garantías adicionales — determinación de cancelación — Para determinar el importe de la cancelación, se admitirá computar el 50 % de las garantías adicionales a las ofrecidas originalmente, constituidas sobre bienes no vinculados a la explotación del deud
  - `e4` Condicion: Reclasificación — deudas refinanciadas con pago periódico — Condición para reclasificación de deudores cuyas deudas hayan sido refinanciadas mediante obligaciones de pago periódico (mensual o bimestral): cumplimiento puntual o con atrasos que no superen los 31
  - `e5` Condicion: Reclasificación — financiaciones de pago único o irregular — Condición para reclasificación cuando se trate de financiaciones de pago único, periódico superior a bimestral o irregular: cancelación de al menos el 5 % de las obligaciones refinanciadas (por capita
  - `e6` Potestad: Reclasificación en nivel inmediato superior — deudor refinanciado — Facultad de reclasificar en el nivel inmediato superior a clientes cuyas deudas hayan sido refinanciadas mediante obligaciones de pago periódico (mensual o bimestral), cuando se cumplan las condicione
  - `e7` Condicion: Reclasificación — resto de deudas en nivel inmediato superior — Condición adicional para reclasificación del deudor refinanciado: el resto de sus deudas debe reunir, como mínimo, las condiciones previstas en el nivel inmediato superior.
  - `e8` Restriccion: Permanencia mínima — deudor refinanciado con crédito adicional — Deudor clasificado en riesgo medio que haya refinanciado su deuda y recibido crédito adicional (en los términos del punto 2.2.5 de normas sobre Previsiones mínimas por riesgo de incobrabilidad), mient
  - `e9` Obligacion: Reclasificación inmediata — atrasos mayores a 31 días — Cuando se verifiquen atrasos mayores a 31 días en el pago de los servicios de la deuda refinanciada contados a partir de la inclusión del deudor en riesgo medio, corresponde la reclasificación inmedia
- relaciones del crudo (sin establecida_en ni de sujeto): e4 condicion_de e6; e5 condicion_de e6; e7 condicion_de e6
- NODOS A CLASIFICAR:
  - **caso 161** Condicion `e2`: Convenios de pago — situación jurídica | descripcion: Se considera la situación jurídica del deudor respecto a convenios de pago de concordatos judiciales o extrajudiciales homologados, incluyendo acuerdos preventivos extrajudiciales homologados, cuando aún no se haya cancelado el 10 % del importe involucrado. | tramo: se considerará si mantiene convenios de pago resultantes de concordatos judiciales o extrajudiciales homologados (incluyendo los acuerdos preventivos extrajudiciales homologados) a vencer cuando aún no se haya cancelado el 10 % del importe involucrado en el citado acuerdo.

## Unidad `ctacte::9.2.1.4` (punto_no_item)
- herencia: [intro 9.2] Al verificarse cualquiera de las causales previstas en el punto 9.1., se observará el siguiente
procedimiento. | [encabezado 9.2.1] 9.2.1. Por parte del cuentacorrentista.
- texto propio: 9.2.1.4. Depositar en una cuenta especial, en tiempo oportuno para hacer frente a ellos
en las correspondientes fechas indicadas para el pago, los importes de los che-
ques de pago diferido (registrados o no) a vencer con posterioridad a la fecha de
notificación de cierre de la cuenta, que hayan sido incluidos en la nómina a que
se refiere el punto 9.2.1.1.
Cuando el cuentacorrentista revista la condición de usuario de servicios financieros
y la cuenta corriente de que se trate no prevea el uso de cheques ni registre saldo deu-
dor, deberá ofrecerse la utilización de mecanismos electrónicos simples, eficaces e in-
mediatos que permitan el cierre de la cuenta en un solo acto (tales como correo electró-
nico, telefonía, banca por Internet –“home banking”–, cajeros automáticos y terminales
de autoservicio).
A tal efecto, se deberá admitir como mínimo la utilización de la banca por Internet
–“home banking”–.
Sin perjuicio de ello, las entidades financieras deberán permitir el cierre de la cuenta co-
rriente en cualquier sucursal –no necesariamente en la de radicación de la cuenta–.
En todos los casos, la entidad deberá proporcionar –en ese mismo acto– constancia del
respectivo trámite de cierre, no pudiéndose devengar ningún tipo de comisión y/o cargo
desde la fecha de presentación de la correspondiente solicitud.
En caso de que registre saldo deudor, el cierre deberá al menos poder ser realizado en
forma presencial –en cualquier sucursal de la entidad financiera a opción del usuario–
conforme a lo previsto precedentemente.
Cuando existan fondos remanentes, a opción del titular, se procederá al cierre de la
cuenta transfiriéndose dichos fondos a saldos inmovilizados de acuerdo con el procedi-
miento establecido con carácter general para el tratamiento de dichos saldos.
- entidades de la unidad:
  - `e1` Obligacion: Depositar importes de cheques diferidos en cuenta especial — El cuentacorrentista debe depositar en una cuenta especial, en tiempo oportuno para hacer frente a los cheques de pago diferido (registrados o no) a vencer con posterioridad a la fecha de notificación
  - `e2` Condicion: Cuentacorrentista usuario de servicios financieros sin cheques ni saldo deudor — El cuentacorrentista reviste la condición de usuario de servicios financieros y la cuenta corriente no prevé el uso de cheques ni registra saldo deudor.
  - `e3` Obligacion: Ofrecer mecanismos electrónicos simples para cierre de cuenta — Debe ofrecerse la utilización de mecanismos electrónicos simples, eficaces e inmediatos que permitan el cierre de la cuenta en un solo acto, tales como correo electrónico, telefonía, banca por Interne
  - `e4` Condicion: Condición para ofrecer mecanismos electrónicos — Esta obligación se aplica cuando el cuentacorrentista reviste la condición de usuario de servicios financieros y la cuenta corriente no prevé el uso de cheques ni registra saldo deudor.
  - `e5` Obligacion: Admitir como mínimo banca por Internet para cierre — Se debe admitir como mínimo la utilización de la banca por Internet (home banking).
  - `e6` Obligacion: Permitir cierre de cuenta en cualquier sucursal — Las entidades financieras deben permitir el cierre de la cuenta corriente en cualquier sucursal, no necesariamente en la de radicación de la cuenta.
  - `e7` Obligacion: Proporcionar constancia de cierre sin comisiones — La entidad debe proporcionar en el mismo acto constancia del trámite de cierre, sin poder devengar ningún tipo de comisión y/o cargo desde la fecha de presentación de la solicitud.
  - `e8` Restriccion: Prohibición de devengar comisiones desde presentación de solicitud — No se puede devengar ningún tipo de comisión y/o cargo desde la fecha de presentación de la solicitud de cierre.
  - `e9` Condicion: Cierre con saldo deudor — Cuando la cuenta registra saldo deudor.
  - `e10` Obligacion: Permitir cierre presencial en cualquier sucursal con saldo deudor — El cierre debe poder ser realizado al menos en forma presencial en cualquier sucursal de la entidad financiera a opción del usuario.
  - `e11` Condicion: Existencia de fondos remanentes — Cuando existen fondos remanentes en la cuenta.
  - `e12` Potestad: Opción del titular para transferencia de fondos remanentes — A opción del titular, se procede al cierre de la cuenta transfiriendo los fondos remanentes a saldos inmovilizados conforme al procedimiento general para el tratamiento de dichos saldos.
- relaciones del crudo (sin establecida_en ni de sujeto): e4 condicion_de e3; e9 condicion_de e10; e11 condicion_de e12
- NODOS A CLASIFICAR:
  - **caso 165** Condicion `e2`: Cuentacorrentista usuario de servicios financieros sin cheques ni saldo deudor | descripcion: El cuentacorrentista reviste la condición de usuario de servicios financieros y la cuenta corriente no prevé el uso de cheques ni registra saldo deudor. | tramo: Cuando el cuentacorrentista revista la condición de usuario de servicios financieros y la cuenta corriente de que se trate no prevea el uso de cheques ni registre saldo deudor

## Unidad `ext::4.4.3` (item)
- herencia: **[abre la lista]** [intro 4.4] registro de ingreso aduanero hasta el 12/12/23.
Los importadores de bienes podrán suscribir Bonos para la Reconstrucción de una Argentina
Libre (BOPREAL) por hasta el monto de la deuda pendiente de pago por sus importaciones de
bienes con registro de ingreso aduanero hasta el 12/12/23.
La entidad que concrete la oferta de suscripción en nombre del cliente deberá contar con las
respectivas certificaciones sobre el monto pendiente de pago emitidas por la/s entidad/es
encargada/s del seguimiento de | [cierre 4.4] En caso de que la importación de bienes encuadre en los puntos 10.3.3., 10.9.1., 10.9.2. y
10.9.3., la entidad que concrete la oferta de suscripción en nombre del cliente deberá verificar
en forma directa lo previsto en los puntos 4.4.1. a 4.4.5. y, adicionalmente, contar con una
declaración jurada del cliente en la que deja constancia de que no ha solicitado la utilización
de este mecanismo en otra entidad por esa deuda. La entidad también deberá realizar la
correspondiente intervención de la d
- texto propio: 4.4.3. se cumplen las condiciones previstas en el punto 10.3.2.1. para el acceso al mercado
de cambios excepto aquella prevista en el inciso viii).
- entidades de la unidad:
  - `c1` Condicion: Cumplimiento condiciones acceso mercado cambios — Se cumplen las condiciones previstas en el punto 10.3.2.1. para el acceso al mercado de cambios
  - `e1` Excepcion: Excepción inciso viii) acceso mercado cambios — Queda exceptuada la condición prevista en el inciso viii) del punto 10.3.2.1. para el acceso al mercado de cambios
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 166** Condicion `c1`: Cumplimiento condiciones acceso mercado cambios | descripcion: Se cumplen las condiciones previstas en el punto 10.3.2.1. para el acceso al mercado de cambios | tramo: se cumplen las condiciones previstas en el punto 10.3.2.1. para el acceso al mercado de cambios

## Unidad `ext::4.4.4` (item)
- herencia: **[abre la lista]** [intro 4.4] registro de ingreso aduanero hasta el 12/12/23.
Los importadores de bienes podrán suscribir Bonos para la Reconstrucción de una Argentina
Libre (BOPREAL) por hasta el monto de la deuda pendiente de pago por sus importaciones de
bienes con registro de ingreso aduanero hasta el 12/12/23.
La entidad que concrete la oferta de suscripción en nombre del cliente deberá contar con las
respectivas certificaciones sobre el monto pendiente de pago emitidas por la/s entidad/es
encargada/s del seguimiento de | [cierre 4.4] En caso de que la importación de bienes encuadre en los puntos 10.3.3., 10.9.1., 10.9.2. y
10.9.3., la entidad que concrete la oferta de suscripción en nombre del cliente deberá verificar
en forma directa lo previsto en los puntos 4.4.1. a 4.4.5. y, adicionalmente, contar con una
declaración jurada del cliente en la que deja constancia de que no ha solicitado la utilización
de este mecanismo en otra entidad por esa deuda. La entidad también deberá realizar la
correspondiente intervención de la d
- texto propio: 4.4.4. el cliente cumple los requisitos complementarios previstos en los puntos 3.16.1. a
3.16.4. El punto 3.16.3. sólo será aplicable para clientes que no sean personas
humanas residentes.
- entidades de la unidad:
  - `c1` Condicion: Cumplimiento requisitos complementarios 3.16.1 a 3.16.4 — El cliente debe cumplir los requisitos complementarios previstos en los puntos 3.16.1. a 3.16.4.
  - `e1` Excepcion: Excepción punto 3.16.3 para personas humanas residentes — El punto 3.16.3. no es aplicable para clientes que sean personas humanas residentes.
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 167** Condicion `c1`: Cumplimiento requisitos complementarios 3.16.1 a 3.16.4 | descripcion: El cliente debe cumplir los requisitos complementarios previstos en los puntos 3.16.1. a 3.16.4. | tramo: el cliente cumple los requisitos complementarios previstos en los puntos 3.16.1. a 3.16.4.

## Unidad `ctacte::8.2.3.1` (punto_no_item)
- herencia: [encabezado 8.2.3] 8.2.3. En la “Central de cheques denunciados como extraviados, sustraídos o adulterados”.
- texto propio: 8.2.3.1. Haber denunciado el titular o tenedor desposeído a la entidad el extravío, la
sustracción o la adulteración de los documentos mencionados en el punto 7.1.,
excepto la fórmula especial para solicitar cuadernos de cheques.
- entidades de la unidad:
  - `e1` Condicion: Denuncia de extravío, sustracción o adulteración — El titular o tenedor desposeído debe haber denunciado a la entidad el extravío, la sustracción o la adulteración de los documentos mencionados en el punto 7.1.
  - `e2` Excepcion: Excepción fórmula especial cuadernos de cheques — La fórmula especial para solicitar cuadernos de cheques queda exceptuada de la exigencia de denuncia de extravío, sustracción o adulteración.
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 171** Condicion `e1`: Denuncia de extravío, sustracción o adulteración | descripcion: El titular o tenedor desposeído debe haber denunciado a la entidad el extravío, la sustracción o la adulteración de los documentos mencionados en el punto 7.1. | tramo: Haber denunciado el titular o tenedor desposeído a la entidad el extravío, la sustracción o la adulteración de los documentos mencionados en el punto 7.1.

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
  - **caso 172** Condicion `e1`: Denuncia de extravío, sustracción o adulteración en filiales | descripcion: La entidad ha denunciado el extravío, sustracción o adulteración de documentos en algunas de sus filiales, conforme a lo mencionado en el punto 7.1. | tramo: Haber denunciado la entidad el extravío, sustracción o adulteración en algunas de sus filiales de los documentos mencionados en el punto 7.1.

## Unidad `cla::6.5.4.1` (item)
- herencia: [intro 6.5] Cada cliente, y la totalidad de sus financiaciones comprendidas, se incluirá en una de las si-
guientes cinco categorías, las que se definen teniendo en cuenta las condiciones que se deta-
llan en cada caso.
Los clientes que no registren asistencia crediticia de la entidad y que posteriormente reciban fi-
nanciaciones de ésta que no superen el importe resultante de aplicar sobre el saldo de deuda
registrado en el sistema financiero, según la última información disponible en la “Central de
deudor | **[abre la lista]** [intro 6.5.4] El análisis del flujo de fondos del cliente demuestra que es altamente improbable que
pueda atender la totalidad de sus compromisos financieros.
Entre los indicadores que pueden reflejar esta situación se destacan que el cliente:
- texto propio: 6.5.4.1. Presente una situación financiera ilíquida y muy alto nivel de endeudamiento, con
resultados negativos en la explotación y obligación de vender activos de impor-
tancia para la actividad desarrollada y que materialmente sean de magnitud sig-
nificativa. El flujo de fondos es manifiestamente insuficiente, no alcanzando a cu-
brir el pago de intereses, y es factible presumir que también tendrá dificultades
para cumplir eventuales acuerdos de refinanciación.
En el análisis que se lleve a cabo deberá tenerse en cuenta, de corresponder, la
eventual incidencia que en su capacidad de pago pueda tener la situación en la
que se encuentran los demás integrantes del grupo de contrapartes conectadas
al cual pertenece.
- entidades de la unidad:
  - `e1` Operacion: Situación financiera ilíquida con alto endeudamiento — Situación financiera caracterizada por iliquidez, muy alto nivel de endeudamiento, resultados negativos en la explotación y obligación de vender activos de importancia para la actividad desarrollada q
  - `e2` Operacion: Flujo de fondos insuficiente para cobertura de intereses — Flujo de fondos manifiestamente insuficiente que no alcanza a cubrir el pago de intereses
  - `e3` Condicion: Dificultades presumibles para cumplir acuerdos de refinanciación — Presunción de dificultades para cumplir eventuales acuerdos de refinanciación
  - `e4` Condicion: Incidencia de situación de contrapartes conectadas — Debe tenerse en cuenta la eventual incidencia en la capacidad de pago del cliente derivada de la situación de los demás integrantes del grupo de contrapartes conectadas al cual pertenece
  - `e5` Obligacion: Análisis de incidencia de contrapartes conectadas — En el análisis de clasificación deberá tenerse en cuenta, de corresponder, la eventual incidencia en la capacidad de pago del cliente derivada de la situación de los demás integrantes del grupo de con
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 177** Condicion `e3`: Dificultades presumibles para cumplir acuerdos de refinanciación | descripcion: Presunción de dificultades para cumplir eventuales acuerdos de refinanciación | tramo: es factible presumir que también tendrá dificultades para cumplir eventuales acuerdos de refinanciación
  - **caso 194** Condicion `e4`: Incidencia de situación de contrapartes conectadas | descripcion: Debe tenerse en cuenta la eventual incidencia en la capacidad de pago del cliente derivada de la situación de los demás integrantes del grupo de contrapartes conectadas al cual pertenece | tramo: la eventual incidencia que en su capacidad de pago pueda tener la situación en la que se encuentran los demás integrantes del grupo de contrapartes conectadas al cual pertenece

## Unidad `ext::14.4.1` (item)
- herencia: [chapeau_seccion S14] En esta sección se detallan las disposiciones complementarias en materia cambiaria que, en la
medida que las disposiciones generales no resulten más favorables, resultan aplicables a un
Vehículo de Proyecto Único (VPU) adherido al Régimen de Incentivo los referidas al “Régimen de
Incentivo para Grandes Inversiones” (RIGI) establecido en el Título VII de la Ley 27.742 y
reglamentado por el Decreto 749/24 y concordantes. | **[abre la lista]** [intro 14.4] en materia de cobros de exportaciones de bienes y servicios.
Para dar acceso al mercado de cambios por cualquier concepto de egreso a un VPU que
haya solicitado la inscripción al RIGI indicando ante la Autoridad de Aplicación que preveía
hacer uso de los beneficios establecidos en el régimen en materia de cobro de exportaciones
de bienes y servicios, adicionalmente a los restantes requisitos que le sean aplicables a la
operación, las entidades deberán: | [cierre 14.4] Este requisito complementario no resultará aplicable cuando el acceso al mercado de
cambios del VPU sea con el objeto de realizar alguna de las siguientes operaciones: | [cierre 14.4] i) pagos de intereses admitidos por las financiaciones contempladas en los puntos | [cierre 14.4] 14.2.1.1. al 14.2.1.11. | [cierre 14.4] ii) pagos de utilidades y dividendos a accionistas no residentes admitidos en el punto | [cierre 14.4] 14.2.2. | [cierre 14.4] iii) pagos de capital de las financiaciones locales contempladas en los puntos 14.2.1.3. | [cierre 14.4] al 14.2.1.5.
- texto propio: 14.4.1. contar con una declaración jurada del representante legal del VPU, o un apoderado
con facultades suficientes para asumir este compromiso en nombre del VPU, en la
que deje constancia de que el importe total de divisas ingresadas desde el exterior y
liquidadas en el mercado de cambios por cualquier concepto por parte del VPU ad-
herido es, al momento de cada acceso, igual o mayor al monto que surge de sumar
el monto de la operación que se pretende cursar al monto total de los accesos al
mercado de cambios del VPU para egresos por todo concepto excepto los pagos
admitidos de intereses y/o utilidades y dividendos y/o el capital de financiaciones lo-
cales contempladas en los puntos 14.2.1.3. al 14.2.1.5.
La liquidación en el mercado de cambios de financiaciones en moneda extranjera
otorgadas al VPU por una entidad financiera local a partir de una línea de crédito del
exterior también deberán ser computadas a favor del VPU como parte de las divisas
ingresadas desde el exterior.
- entidades de la unidad:
  - `e1` Obligacion: Declaración jurada de divisas ingresadas — VPU RIGI — El VPU debe contar con una declaración jurada del representante legal o apoderado con facultades suficientes en la que conste que el importe total de divisas ingresadas desde el exterior y liquidadas 
  - `e2` Condicion: Divisas ingresadas igual o mayor al monto de operación más accesos previos — El importe total de divisas ingresadas desde el exterior y liquidadas en el mercado de cambios debe ser, al momento de cada acceso, igual o mayor al monto que resulta de sumar el monto de la operación
  - `e3` Obligacion: Computar liquidación de financiaciones en moneda extranjera como divisas ingresadas — La liquidación en el mercado de cambios de financiaciones en moneda extranjera otorgadas al VPU por una entidad financiera local a partir de una línea de crédito del exterior debe ser computada a favo
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 178** Condicion `e2`: Divisas ingresadas igual o mayor al monto de operación más accesos previos | descripcion: El importe total de divisas ingresadas desde el exterior y liquidadas en el mercado de cambios debe ser, al momento de cada acceso, igual o mayor al monto que resulta de sumar el monto de la operación pretendida al monto total de accesos previos para egresos, excluyendo pagos de intereses, utilidades, dividendos y capital de financiaciones locales. | tramo: el importe total de divisas ingresadas desde el exterior y liquidadas en el mercado de cambios por cualquier concepto por parte del VPU adherido es, al momento de cada acceso, igual o mayor al monto que surge de sumar el monto de la operación que se pretende cursar al monto total de los accesos al mercado de cambios del VPU para egresos por todo concepto excepto los pagos admitidos de intereses y/o utilidades y dividendos y/o el capital de financiaciones locales contempladas en los puntos 14.2.1.3. al 14.2.1.5.

## Unidad `ext::3.5.1.1` (item)
- herencia: [chapeau_seccion S3] Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas
en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–,
adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán
cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables. | [intro 3.5] exterior.
Las entidades podrán dar acceso al mercado de cambios para realizar pagos de capital o
intereses de títulos de deuda con registro público en el exterior, otros endeudamientos
financieros con el exterior y títulos de deuda con registro público en el país denominados en
moneda extranjera íntegramente suscriptos en el exterior, en la medida que se verifiquen las
siguientes condiciones: | **[abre la lista]** [intro 3.5.1] un monto equivalente al valor nominal del endeudamiento financiero.
Este requisito se considerará cumplimentado en los siguientes casos:
- texto propio: 3.5.1.1. los endeudamientos desembolsados con anterioridad al 01/09/19.
- entidades de la unidad:
  - `e1` Condicion: Endeudamientos desembolsados antes 01/09/19 — El requisito de demostrar ingreso y liquidación de divisas se considera cumplimentado cuando los endeudamientos fueron desembolsados con anterioridad al 01/09/19
  - `e2` Excepcion: Excepción requisito liquidación divisas — endeudamientos anteriores 01/09/19 — Quedan exceptuados del requisito de demostrar ingreso y liquidación de divisas en el mercado de cambios los endeudamientos desembolsados con anterioridad al 01/09/19
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 179** Condicion `e1`: Endeudamientos desembolsados antes 01/09/19 | descripcion: El requisito de demostrar ingreso y liquidación de divisas se considera cumplimentado cuando los endeudamientos fueron desembolsados con anterioridad al 01/09/19 | tramo: los endeudamientos desembolsados con anterioridad al 01/09/19
