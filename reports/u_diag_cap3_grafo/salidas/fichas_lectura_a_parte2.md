## Unidad `ext::5.13` (punto_no_item)
- herencia: [encabezado S5] Sección 5. Pautas operativas.
- texto propio: 5.13. Operaciones que impliquen importación y/o exportación de moneda nacional.
Las entidades podrán concretar operaciones de cambio que impliquen la importación y/o
exportación de monedas y billetes de pesos argentinos siempre que la contraparte sea alguna
de las previstas en el punto 5.12. Las operaciones que impliquen la importación de billetes de
pesos argentinos quedarán también sujetas a las disposiciones establecidas para la compra
de moneda extranjera por parte de no residentes.
La liquidación de las divisas remitidas a la entidad local por la contraparte para la adquisición
de billetes en moneda local estará exceptuada de lo dispuesto en el primer párrafo del punto
2.9. en la medida que exista un compromiso de la contraparte respecto a que dichos fondos
serán comercializados con el objeto de atender la demanda de turismo y viajes y la
exportación se realice en un plazo no mayor a los 30 (treinta) días corridos de la fecha de
concertación de cambio.
- entidades de la unidad:
  - `e1` Operacion: Importación y/o exportación de moneda nacional — Operaciones de cambio que impliquen la importación y/o exportación de monedas y billetes de pesos argentinos
  - `e2` Condicion: Contraparte prevista en punto 5.12 — La contraparte debe ser alguna de las previstas en el punto 5.12
  - `e3` Restriccion: Importación de billetes pesos — sujeta a disposiciones compra moneda extranjera no residentes — Las operaciones que impliquen la importación de billetes de pesos argentinos quedan sujetas a las disposiciones establecidas para la compra de moneda extranjera por parte de no residentes
  - `e4` Excepcion: Liquidación divisas remitidas — exceptuada punto 2.9 primer párrafo — La liquidación de las divisas remitidas a la entidad local por la contraparte para la adquisición de billetes en moneda local queda exceptuada de lo dispuesto en el primer párrafo del punto 2.9
  - `e5` Condicion: Compromiso contraparte — fondos para turismo y viajes — Debe existir un compromiso de la contraparte de que los fondos serán comercializados para atender la demanda de turismo y viajes
  - `e6` Condicion: Plazo exportación — no mayor a 30 días corridos — La exportación debe realizarse en un plazo no mayor a 30 días corridos desde la fecha de concertación de cambio
- relaciones del crudo (sin establecida_en ni de sujeto): e2 condicion_de e1; e5 condicion_de e4; e6 condicion_de e4
- NODOS A CLASIFICAR:
  - **caso 51** Excepcion `e4`: Liquidación divisas remitidas — exceptuada punto 2.9 primer párrafo | descripcion: La liquidación de las divisas remitidas a la entidad local por la contraparte para la adquisición de billetes en moneda local queda exceptuada de lo dispuesto en el primer párrafo del punto 2.9 | tramo: La liquidación de las divisas remitidas a la entidad local por la contraparte para la adquisición de billetes en moneda local estará exceptuada de lo dispuesto en el primer párrafo del punto 2.9

## Unidad `ext::3.16.3::intersticial` (intersticial)
- herencia: [encabezado 3.16.3] 3.16.3. Declaración jurada de clientes que no sean personas humanas residentes respecto a
- texto propio: En caso de que el cliente sea una persona jurídica, para que la operación no quede
comprendida por el requisito de conformidad previa, la entidad deberá contar
adicionalmente con una declaración jurada en la que conste:
- entidades de la unidad:
  - `e1` Condicion: Cliente es persona jurídica — El cliente es una persona jurídica
  - `e2` Excepcion: Excepción conformidad previa — persona jurídica — La operación no queda comprendida por el requisito de conformidad previa cuando se cumplen las condiciones de esta salvedad
  - `e3` Obligacion: Contar con declaración jurada — cliente persona jurídica — La entidad debe contar con una declaración jurada en la que conste la información requerida
- relaciones del crudo (sin establecida_en ni de sujeto): e1 condicion_de e3
- NODOS A CLASIFICAR:
  - **caso 52** Excepcion `e2`: Excepción conformidad previa — persona jurídica | descripcion: La operación no queda comprendida por el requisito de conformidad previa cuando se cumplen las condiciones de esta salvedad | tramo: para que la operación no quede comprendida por el requisito de conformidad previa

## Unidad `cap::4.2.1.2::parte1` (punto_no_item)
- herencia: [intro 4.2] –OTC o negociados en mercados regulados– y con liquidación diferida.
La exigencia computada en este punto –basada en el Enfoque Estándar para la medición de
la exigencia por capital por riesgo de crédito de contraparte (“Standardised Approach for
measuring Counterparty Credit Risk”, SA-CCR)– se aplicará a operaciones con derivados
–OTC o negociados en mercados regulados– y con liquidación diferida, ya que las operacio-
nes de financiación con títulos valores (“Securities Financing Transactions”, | [intro 4.2.1] La exposición al riesgo de crédito de contraparte (EAD) se calculará por separado para
cada conjunto de neteo (“netting set”, NS) y se determinará del siguiente modo:
donde:
α = 1,40.
CR: costo de reposición calculado de acuerdo con el punto 4.2.1.1.
EPF: exposición potencial futura calculado de acuerdo con el punto 4.2.1.2.
El cálculo del CR y de la EPF diferirá según que los conjuntos de neteo estén sujetos o
no al intercambio de márgenes de variación:
− Operaciones sin margen de variación: el | [intro 4.2.1] ante el incumplimiento de la contraparte y la liquidación inmediata de sus opera-
ciones y la EPF adicionará el incremento probable de la exposición, calculado de
modo conservador, en el horizonte temporal de un año a partir de la fecha de
cálculo. | [intro 4.2.1] − Operaciones con margen de variación: el CR representa la pérdida que ocurriría | [intro 4.2.1] ante el incumplimiento de la contraparte –en el presente o en el futuro– si la liqui-
dación y reposición de las operaciones fueran instantáneas. Dado que puede ha-
ber un lapso –período de riesgo de margen (“MPOR”)– entre el último intercambio
de garantías antes del incumplimiento y la reposición, el adicional por la EPF re-
presenta el potencial cambio de valor de las operaciones durante ese período. | [intro 4.2.1] En ambos casos, y a los efectos de determinar el costo de reposición, el aforo de los
activos recibidos en garantía (excepto efectivo) representará el cambio potencial del
valor de dicha garantía durante el período relevante –un año, para las operaciones sin
márgenes, y el período de riesgo de margen, para las operaciones con márgenes–.
Además:
− La EAD para un conjunto de neteo con márgenes de variación tendrá como límite | [intro 4.2.1] superior la EAD que resultaría para el mismo conjunto si no los tuviera. | [intro 4.2.1] − La EAD de un conjunto de neteo que sólo comprende opciones vendidas podrá | [intro 4.2.1] ser cero cuando hayan sido cobradas todas las primas y en tanto dichas opciones
no estén comprendidas en acuerdos de neteo que incluyan otros productos o la
constitución de márgenes.
- texto propio: 4.2.1.2. Cálculo de la EPF.
Resultará del producto entre:
- la suma de los adicionales correspondientes a cada clase de activos; y
- un multiplicador que permite reconocer la garantía en exceso o el valor de
mercado negativo de las operaciones, conforme a la siguiente expresión:
EPF = multiplicador x AdicionalTotal
donde:
es la suma de los adicionales correspondientes a cada clase de activos
–no se reconocen beneficios por diversificación–, calculados de acuerdo con
la metodología expuesta en los acápites viii) a xii) de este punto, y el multi-
plicador se define como:
El multiplicador se reduce a medida que se incrementa la tenencia de garan-
tías en exceso –sujeto a un mínimo de 5 % de la EPF– y operará de la si-
guiente manera:
− Cuando el costo de reposición corriente sea positivo –esto es, cuando el
valor de los activos en garantía sea inferior al valor de mercado neto de los
contratos de derivados– el multiplicador será igual a uno –esto es, el com-
ponente EPF será igual al valor del AdicionalTotal–.
− Cuando el valor de los activos en garantía supere el valor de mercado neto
de los contratos de derivados –garantías en exceso–, el multiplicador será
inferior a la unidad –esto es, el componente EPF será menor que el valor
del AdicionalTotal –.
− El multiplicador se activará –es decir, tomará un valor inferior a la unidad–
también cuando el valor corriente de las operaciones con derivados sea
negativo.
Para determinar el cálculo de la EPF, las operaciones se ajustarán a lo si-
guiente:
− Cada derivado se asignará a una clase de activo sobre la base de su factor
de riesgo principal –que en la mayoría de los casos será el único, definido
por la referencia a un instrumento subyacente, tal como una curva de tasas
de interés en el caso de un “swap” de tasas de interés o
- entidades de la unidad:
  - `e1` Operacion: Cálculo de la exposición potencial futura (EPF) — Cálculo de la exposición potencial futura (EPF) como producto de la suma de adicionales por clase de activos y un multiplicador que reconoce garantía en exceso o valor de mercado negativo
  - `e2` Definicion: AdicionalTotal — suma de adicionales por clase de activos — suma de los adicionales correspondientes a cada clase de activos, sin reconocimiento de beneficios por diversificación, calculados según la metodología de los acápites viii) a xii)
  - `e3` Restriccion: Límite mínimo del multiplicador — garantía en exceso — El multiplicador se reduce según la tenencia de garantías en exceso, con un mínimo del 5% de la EPF
  - `e4` Condicion: Cuando costo de reposición es positivo — Supuesto en que el valor de los activos en garantía es inferior al valor de mercado neto de los contratos de derivados
  - `e5` Obligacion: Multiplicador igual a uno cuando CR positivo — Cuando el costo de reposición sea positivo, el multiplicador toma valor uno, haciendo el EPF igual al AdicionalTotal
  - `e6` Condicion: Cuando valor de garantías en exceso supera valor de mercado neto — Supuesto en que los activos en garantía superan el valor de mercado neto de los contratos de derivados
  - `e7` Obligacion: Multiplicador menor a uno cuando garantías en exceso — Cuando hay garantías en exceso, el multiplicador es inferior a uno, reduciendo el EPF respecto a AdicionalTotal
  - `e8` Condicion: Cuando valor corriente de derivados es negativo — Supuesto en que el valor corriente de las operaciones con derivados es negativo
  - `e9` Obligacion: Asignación del derivado a clase de activo según factor de riesgo principal — Asignación de cada derivado a una clase de activo según su factor de riesgo principal, identificado por el instrumento subyacente
  - `e10` Obligacion: Asignación a clase de activo cuando se identifica claramente el factor principal — Cuando se identifica claramente el factor de riesgo principal, la operación se clasifica en una de cinco clases de activos: tasa de interés, tipo de cambio, crédito, acciones o commodities
  - `e11` Obligacion: Consideración de sensibilidad y volatilidad en derivados complejos — En derivados híbridos con múltiples factores de riesgo, las entidades deben considerar la sensibilidad y volatilidad de los subyacentes para identificar el factor de riesgo principal
  - `e12` Potestad: Potestad de la SEFyC — requerir asignación múltiple en derivados complejos — La SEFyC puede requerir que operaciones complejas se asignen a múltiples clases de activos, con determinación separada del signo y ajuste delta para cada factor de riesgo
  - `e13` Obligacion: Cálculo de adicional por clase de activo usando fórmulas específicas — El adicional para cada clase de activo se calcula mediante fórmulas específicas que determinan la EPE (Expected Positive Exposure) efectiva
  - `e14` Obligacion: Cálculo de nocional ajustado a partir de nocional real o precio — Cálculo del nocional ajustado a partir del nocional real o del precio de la operación
  - `e15` Definicion: Nocional ajustado para derivados de tasa de interés y créditos — Para derivados de tasa de interés y créditos, el nocional ajustado incorpora una medición del plazo (duration) establecida en el acápite ii)
  - `e16` Obligacion: Cálculo de factor plazo para cada operación — Cálculo del factor plazo (MF) para reflejar el horizonte temporal según el tipo de operación: con márgenes o sin márgenes
  - `e17` Obligacion: Aplicación de ajuste delta al nocional ajustado — Aplicación de ajuste delta al nocional ajustado según el tipo de posición (larga/corta) y tipo de instrumento (opción, segmento CDO, otro)
  - `e18` Obligacion: Aplicación de factor de volatilidad al nocional efectivo — Aplicación de un factor de volatilidad al nocional efectivo de cada operación
  - `e19` Obligacion: Separación de operaciones por conjunto de cobertura — Separación de operaciones dentro de cada clase de activo por conjunto de cobertura (hedging set)
  - `e20` Obligacion: Aplicación de método de suma con parámetros de correlación — Aplicación de método de suma para agregar operaciones dentro de cada conjunto y entre conjuntos, utilizando parámetros de correlación para derivados de crédito, acciones y commodities
  - `e21` Definicion: M (vencimiento) — parámetro de tiempo — Última fecha hasta la que podría estar activo el contrato. Se utiliza en el factor plazo para reducir el nocional ajustado de operaciones sin márgenes
  - `e22` Definicion: S (fecha de inicio) — parámetro de tiempo en derivados de interés y crédito — Fecha de inicio del período referenciado en derivados de tasas de interés y créditos. Se utiliza en la definición del plazo regulatorio
  - `e23` Definicion: E (fecha de finalización) — parámetro de tiempo en derivados de interés y crédito — Fecha de finalización del período referenciado en derivados de tasas de interés y créditos. Se utiliza en la definición del plazo regulatorio y categorización por plazos
  - `e24` Definicion: T (fecha de ejercicio) — parámetro de tiempo en opciones — Última fecha de ejercicio de la opción según el contrato. Se utiliza para determinar el delta de la opción
  - `e25` Definicion: Nocional ajustado a nivel de operación — derivados de tasa de interés y créditos — Producto del nocional en pesos y el plazo regulatorio (SD) para derivados de tasa de interés y créditos
  - `e26` Restriccion: Límite mínimo de período de plazo regulatorio — El período de plazo regulatorio tiene un mínimo de 10 días hábiles
  - `e27` Definicion: Nocional ajustado para derivados de tipo de cambio — Nocional del lado expresado en moneda extranjera convertido a pesos; si ambos lados están en moneda extranjera, se toma el mayor de ambos convertidos
  - `e28` Definicion: Nocional ajustado para derivados sobre acciones y commodities — Producto del precio corriente unitario por el número de unidades referenciadas en la operación
  - `e29` Definicion: Nocional ajustado para operaciones sobre volatilidad — Producto de la volatilidad o varianza referenciadas en la operación y el nocional contractual
  - `e30` Obligacion: Observancia de normas especiales para nocionales no claramente definidos — Para operaciones con nocionales no claramente definidos o variables, se deben observar reglas específicas de determinación
  - `e31` Obligacion: Cálculo de nocional para opciones digitales — Para opciones digitales con múltiples retribuciones contingentes, se calcula un nocional por estado y se toma el mayor
  - `e32` Obligacion: Determinación de nocional cuando es fórmula de valores de mercado — Cuando el nocional está definido como fórmula en valores de mercado, se utilizan los valores corrientes para su determinación
  - `e33` Obligacion: Cálculo de nocional promedio ponderado por tiempo en swaps de nocional variable — Para swaps de nocional variable, se utiliza el promedio ponderado por tiempo del nocional durante la vida residual del instrumento
  - `e34` Excepcion: Excepción a promedio ponderado — derivados FX, acciones y commodities — La regla de promedio ponderado por tiempo no aplica a operaciones donde el nocional varía por cambios de precios (derivados FX, acciones, commodities)
  - `e35` Obligacion: Conversión de swaps apalancados a equivalentes no apalancados — Los swaps apalancados se convierten a equivalentes no apalancados; cuando las tasas se multiplican por un factor, el nocional se multiplica por ese factor
  - `e36` Obligacion: Ajuste de nocional por número de intercambios de principal — Para derivados con intercambios múltiples del principal, el nocional se multiplica por el número de intercambios previstos
  - `e37` Obligacion: Ajuste de plazo residual en derivados con reformulación de condiciones — En derivados con reformulación periódica a fair value cero, el plazo residual se calcula hasta la próxima fecha de reformulación
  - `e38` Obligacion: Cálculo de parámetros precio, precio de ejercicio y volatilidad en opciones — Cálculo de parámetros de opciones: precio del subyacente (preferentemente forward), precio de ejercicio (K), fecha de ejercicio (T) y volatilidad conforme a factores regulatorios
  - `e39` Obligacion: Cálculo de parámetros en segmentos CDO — Cálculo de parámetros de segmentos de CDO: punto de unión (A) y punto de separación (D)
  - `e40` Obligacion: Aplicación de factores regulatorios de volatilidad — Aplicación de factores regulatorios de volatilidad específicos por clase de activo al nocional efectivo para obtener la EPE efectiva
  - `e41` Definicion: Conjuntos de cobertura en tasas de interés — Un conjunto de cobertura por cada moneda en derivados sobre tasas de interés
  - `e42` Definicion: Conjuntos de cobertura en derivados FX — Un conjunto de cobertura por cada par de monedas en derivados FX
  - `e43` Definicion: Conjuntos de cobertura en derivados de crédito — Un único conjunto de cobertura para todos los derivados de crédito
  - `e44` Definicion: Conjuntos de cobertura en derivados sobre acciones — Un único conjunto de cobertura para todos los derivados sobre acciones
  - `e45` Definicion: Conjuntos de cobertura en derivados sobre commodities — Cuatro conjuntos de cobertura según categoría: energía, metales, productos agrícolas y otros productos básicos
  - `e46` Obligacion: Asignación de derivados sobre bases a conjuntos de cobertura específicos — Derivados sobre bases denominados en una sola moneda se asignan a conjuntos de cobertura específicos dentro de su clase de activo
  - `e47` Excepcion: Excepción a tratamiento de bases — cross-currency swaps — Los cross-currency swaps no se tratan como derivados sobre bases; reciben el tratamiento de contratos FX ordinarios
  - `e48` Definicion: Conjuntos de cobertura para derivados sobre bases — Un conjunto por cada par de factores de riesgo (cada base específica); posiciones clasificadas como largas o cortas respecto de la base
  - `e49` Restriccion: Multiplicador del factor SF en derivados sobre bases — límite de 0,5 — En conjuntos de cobertura de derivados sobre bases, el factor de volatilidad (SF) se multiplica por 0,5
  - `e50` Definicion: Conjuntos de cobertura para derivados sobre volatilidad — Derivados sobre volatilidad (swaps de varianza/volatilidad, opciones sobre volatilidad real/implícita) se asignan a conjuntos específicos dentro de su clase de activo
  - `e51` Restriccion: Multiplicador del factor SF en derivados sobre volatilidad — límite de 5 — En conjuntos de cobertura de derivados sobre volatilidad, el factor de volatilidad (SF) se multiplica por 5
  - `e52` Definicion: Factor de plazo para operaciones sin margen de variación — Para operaciones sin margen, el horizonte temporal mínimo es el menor entre un año y el plazo residual, con un mínimo de 10 días hábiles
  - `e53` Obligacion: Aplicación de factor plazo a nocional ajustado en operaciones sin margen — Multiplicación del nocional ajustado por un factor de plazo cuyo numerador es el horizonte temporal mínimo y denominador el plazo residual (mínimo 10 días hábiles)
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 53** Excepcion `e34`: Excepción a promedio ponderado — derivados FX, acciones y commodities | descripcion: La regla de promedio ponderado por tiempo no aplica a operaciones donde el nocional varía por cambios de precios (derivados FX, acciones, commodities) | tramo: Esta regla no será aplicable a las operaciones en las que el nocional varía debido a cambios en los precios –tales como los derivados FX, y sobre acciones o "commodities"–
  - **caso 69** Excepcion `e47`: Excepción a tratamiento de bases — cross-currency swaps | descripcion: Los cross-currency swaps no se tratan como derivados sobre bases; reciben el tratamiento de contratos FX ordinarios | tramo: Este tratamiento no se aplicará a los derivados con dos lados flotantes denominados en monedas diferentes –tales como los "cross-currency swaps": acuerdos para intercambiar pagos de principal e intereses de préstamos denominados en dos monedas diferentes–, los que recibirán el tratamiento aplicable a los contratos FX ordinarios
  - **caso 162** Condicion `e4`: Cuando costo de reposición es positivo | descripcion: Supuesto en que el valor de los activos en garantía es inferior al valor de mercado neto de los contratos de derivados | tramo: Cuando el costo de reposición corriente sea positivo –esto es, cuando el valor de los activos en garantía sea inferior al valor de mercado neto de los contratos de derivados–
  - **caso 163** Condicion `e8`: Cuando valor corriente de derivados es negativo | descripcion: Supuesto en que el valor corriente de las operaciones con derivados es negativo | tramo: El multiplicador se activará –es decir, tomará un valor inferior a la unidad– también cuando el valor corriente de las operaciones con derivados sea negativo
  - **caso 164** Condicion `e6`: Cuando valor de garantías en exceso supera valor de mercado neto | descripcion: Supuesto en que los activos en garantía superan el valor de mercado neto de los contratos de derivados | tramo: Cuando el valor de los activos en garantía supere el valor de mercado neto de los contratos de derivados –garantías en exceso–

## Unidad `ctacte::8.6.3` (punto_no_item)
- herencia: [encabezado 8.6] 8.6. Información al Banco Central de la República Argentina.
- texto propio: 8.6.3. El responsable del régimen informativo y el auditor externo de la entidad deberán verifi-
car el cumplimiento de los requisitos y procedimientos establecidos y sus conclusiones
volcadas semestralmente en un informe especial, conforme a las normas que se esta-
blezcan en la materia.
Esta disposición no sustituye la obligación de informar al BCRA los rechazos y/o el pago
de las correspondientes multas, en los plazos establecidos con carácter general (puntos
6.4. y 6.5., respectivamente).
- entidades de la unidad:
  - `e1` Obligacion: Verificación semestral de requisitos y procedimientos — 
  - `e2` Excepcion: No sustituye obligación de informar rechazos y multas — La verificación semestral no sustituye la obligación de informar al BCRA los rechazos y/o el pago de multas en los plazos establecidos con carácter general
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 54** Excepcion `e2`: No sustituye obligación de informar rechazos y multas | descripcion: La verificación semestral no sustituye la obligación de informar al BCRA los rechazos y/o el pago de multas en los plazos establecidos con carácter general | tramo: Esta disposición no sustituye la obligación de informar al BCRA los rechazos y/o el pago de las correspondientes multas, en los plazos establecidos con carácter general

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
  - **caso 68** Excepcion `e10`: Refinanciaciones — productores agropecuarios Ley de Emergencia | descripcion: Las refinanciaciones otorgadas a productores agropecuarios derivadas de la aplicación de disposiciones de la Ley de Emergencia Agropecuaria no se consideran refinanciaciones a los fines de verificación de cumplimiento de obligaciones. | tramo: Tampoco se considerarán dentro de ese concepto las refinanciaciones otorgadas a los productores agropecuarios cuando ello resulte de la aplicación de disposiciones vinculadas a la Ley de Emergencia Agropecuaria

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

## Unidad `ext::3.5.1.9` (item)
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
- texto propio: 3.5.1.9. por los endeudamientos con el exterior originados a partir del 01/09/19 en
una refinanciación del capital y/o intereses de deudas comerciales con el
acreedor del exterior, en la medida que la nueva deuda financiera no anticipe
vencimientos respecto de la deuda comercial refinanciada ni implique la
realización de pagos antes de la fecha en que el cliente hubiera podido
acceder por la deuda comercial en virtud de la normativa aplicable.
Estas condiciones se podrán considerar cumplimentadas para los
endeudamientos con una vida promedio no inferior a los 2 (dos) años
originados entre 27/08/21 y el 12/12/23 en una refinanciación encuadrada en
el punto 20. de la Comunicación A 7626 y concordantes (disposiciones
receptadas oportunamente en el punto 3.20. del Anexo de la Comunicación
A 7914); en la medida que la entidad cuente con una certificación para el
acceso al mercado de cambios emitida, dentro de los 5 (cinco) días hábiles
previos, por la entidad que concretó el registro ante el BCRA con el código
de concepto “P17. Registro de refinanciación de deuda comercial en el
marco del punto 20. de la Comunicación A 7626”.
- entidades de la unidad:
  - `c1` Condicion: Endeudamiento originado a partir del 01/09/19 — El endeudamiento con el exterior debe haber sido originado a partir del 01/09/19
  - `c2` Condicion: Refinanciación de deuda comercial — El endeudamiento debe constituir una refinanciación del capital y/o intereses de deudas comerciales con el acreedor del exterior
  - `r1` Restriccion: No anticipación de vencimientos en refinanciación — La nueva deuda financiera no puede anticipar vencimientos respecto de la deuda comercial refinanciada
  - `r2` Restriccion: No realización de pagos anticipados respecto a deuda comercial — La nueva deuda financiera no puede implicar la realización de pagos antes de la fecha en que el cliente hubiera podido acceder por la deuda comercial en virtud de la normativa aplicable
  - `e1` Excepcion: Excepción vida promedio mínima 2 años — período 27/08/21 a 12/12/23 — Las condiciones de no anticipación de vencimientos y no realización de pagos anticipados se consideran cumplimentadas para endeudamientos con vida promedio no inferior a 2 años originados entre 27/08/
  - `c3` Condicion: Certificación de acceso al mercado de cambios — La entidad debe contar con certificación para acceso al mercado de cambios emitida dentro de 5 días hábiles previos por la entidad que concretó el registro ante el BCRA con código de concepto P17
  - `com1` Comunicacion: Com. A 7626 — 
  - `com2` Comunicacion: Com. A 7914 — 
- relaciones del crudo (sin establecida_en ni de sujeto): to referencia com1; to referencia com2; c1 condicion_de e1; c2 condicion_de e1; c3 condicion_de e1
- NODOS A CLASIFICAR:
  - **caso 57** Excepcion `e1`: Excepción vida promedio mínima 2 años — período 27/08/21 a 12/12/23 | descripcion: Las condiciones de no anticipación de vencimientos y no realización de pagos anticipados se consideran cumplimentadas para endeudamientos con vida promedio no inferior a 2 años originados entre 27/08/21 y 12/12/23 en refinanciación conforme punto 20 de Com. A 7626 | tramo: Estas condiciones se podrán considerar cumplimentadas para los endeudamientos con una vida promedio no inferior a los 2 (dos) años originados entre 27/08/21 y el 12/12/23 en una refinanciación encuadrada en el punto 20. de la Comunicación A 7626 y concordantes

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

## Unidad `ext::13.4.3` (item)
- herencia: **[abre la lista]** [intro 13.4] Se requerirá la conformidad previa del BCRA para el acceso al mercado de cambios para
realizar pagos de servicios de no residentes prestados o devengados hasta el 12/12/23,
excepto cuando, adicionalmente a los restantes requisitos aplicables, la entidad verifique
que:
- texto propio: 13.4.3. el pago corresponda a la cancelación de deudas por operaciones financiadas o
garantizadas con anterioridad al 13/12/23 por organismos internacionales y/o
agencias oficiales de crédito; o
Las entidades podrán considerar también como operación garantizada por una
agencia oficial de crédito a aquella que se encuentre cubierta por una garantía
emitida por una aseguradora privada por cuenta y orden de un gobierno nacional de
otro país. En todos los casos, la entidad interviniente deberá contar con
documentación en la que conste explícitamente tal situación.
- entidades de la unidad:
  - `c1` Condicion: Pago cancelación deudas operaciones financiadas/garantizadas — El pago debe corresponder a la cancelación de deudas por operaciones financiadas o garantizadas con anterioridad al 13/12/23 por organismos internacionales y/o agencias oficiales de crédito.
  - `e1` Excepcion: Operación garantizada por aseguradora privada por cuenta de gobierno — Las entidades pueden considerar como operación garantizada por una agencia oficial de crédito aquella cubierta por garantía emitida por aseguradora privada por cuenta y orden de un gobierno nacional d
  - `o1` Obligacion: Documentación explícita de garantía por aseguradora privada — La entidad interviniente debe contar con documentación que conste explícitamente la situación de cobertura por garantía de aseguradora privada por cuenta y orden de gobierno nacional de otro país.
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 59** Excepcion `e1`: Operación garantizada por aseguradora privada por cuenta de gobierno | descripcion: Las entidades pueden considerar como operación garantizada por una agencia oficial de crédito aquella cubierta por garantía emitida por aseguradora privada por cuenta y orden de un gobierno nacional de otro país. | tramo: Las entidades podrán considerar también como operación garantizada por una agencia oficial de crédito a aquella que se encuentre cubierta por una garantía emitida por una aseguradora privada por cuenta y orden de un gobierno nacional de otro país
  - **caso 214** Condicion `c1`: Pago cancelación deudas operaciones financiadas/garantizadas | descripcion: El pago debe corresponder a la cancelación de deudas por operaciones financiadas o garantizadas con anterioridad al 13/12/23 por organismos internacionales y/o agencias oficiales de crédito. | tramo: el pago corresponda a la cancelación de deudas por operaciones financiadas o garantizadas con anterioridad al 13/12/23 por organismos internacionales y/o agencias oficiales de crédito

## Unidad `ext::8.5.17.22` (item)
- herencia: [intro 8.5] La entidad podrá considerar cumplimentado parcial o totalmente el seguimiento de un permiso
de embarque cuando cuente con los elementos que le permitan considerar que la operación
se encuentra en alguna de las situaciones detalladas a continuación y se verifiquen las
condiciones previstas en cada caso.
La documentación utilizada para certificar el concepto y monto de las divisas imputado en
cada caso deberá quedar archivada en la entidad a disposición del BCRA. | **[abre la lista]** [intro 8.5.17] Por el valor que corresponda a ventajas aduaneras u otras situaciones previstas en el
siguiente listado de operaciones:
- texto propio: 8.5.17.22. Exportaciones a zonas francas nacionales.
- entidades de la unidad:
  - `e1` Operacion: Exportaciones a zonas francas nacionales — Exportaciones de bienes a zonas francas nacionales, operación aduanera exceptuada del seguimiento de divisas por exportaciones
  - `e2` Excepcion: Excepción seguimiento — exportaciones a zonas francas — Las exportaciones a zonas francas nacionales quedan exceptuadas del seguimiento de permisos de embarque por divisas
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 60** Excepcion `e2`: Excepción seguimiento — exportaciones a zonas francas | descripcion: Las exportaciones a zonas francas nacionales quedan exceptuadas del seguimiento de permisos de embarque por divisas | tramo: Exportaciones a zonas francas nacionales

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
  - **caso 63** Excepcion `e2`: Excepción notificación para modificaciones económicamente beneficiosas | descripcion: Las modificaciones que resulten económicamente más beneficiosas para el usuario por reducción de los valores pactados no requieren notificación anticipada. | tramo: Las modificaciones que resulten económicamente más beneficiosas para el usuario –por una reducción de los valores pactados– no requieren notificación anticipada.
  - **caso 103** Excepcion `e1`: Consentimiento por falta de objeción para cambios en valores de comisiones | descripcion: Para modificaciones en los valores de comisiones y/o cargos debidamente aceptados por el usuario, el consentimiento puede quedar conformado por la falta de objeción dentro del plazo establecido en el acápite iv). | tramo: Cuando se trate de modificaciones en los valores de comisiones y/o cargos debidamente aceptados por el usuario, su consentimiento al cambio podrá quedar conformado por la falta de objeción al mismo dentro del plazo establecido en el acápite iv).
  - **caso 152** Condicion `c2`: Concurrencia de todas las condiciones para modificación | descripcion: Para que sea válida la modificación de condiciones pactadas, deben cumplirse la totalidad de las condiciones enumeradas (i, ii, iii y iv), no basta con alguna de ellas. | tramo: A fin de modificar las condiciones pactadas debe darse la totalidad de las siguientes condiciones:

## Unidad `ext::8.5.17.24` (item)
- herencia: [intro 8.5] La entidad podrá considerar cumplimentado parcial o totalmente el seguimiento de un permiso
de embarque cuando cuente con los elementos que le permitan considerar que la operación
se encuentra en alguna de las situaciones detalladas a continuación y se verifiquen las
condiciones previstas en cada caso.
La documentación utilizada para certificar el concepto y monto de las divisas imputado en
cada caso deberá quedar archivada en la entidad a disposición del BCRA. | **[abre la lista]** [intro 8.5.17] Por el valor que corresponda a ventajas aduaneras u otras situaciones previstas en el
siguiente listado de operaciones:
- texto propio: 8.5.17.24. Operaciones de reembarco consignadas mediante los subregímenes
RE01, RE04, RE05, RE06, REP1, REP4 o REP6.
- entidades de la unidad:
  - `e1` Operacion: Reembarco consignado mediante subregímenes aduaneros — Operaciones de reembarco consignadas mediante los subregímenes aduaneros RE01, RE04, RE05, RE06, REP1, REP4 o REP6
  - `e2` Excepcion: Excepción reembarco — seguimiento de permiso de embarque — Las operaciones de reembarco consignadas mediante los subregímenes RE01, RE04, RE05, RE06, REP1, REP4 o REP6 quedan exceptuadas del seguimiento de un permiso de embarque
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 64** Excepcion `e2`: Excepción reembarco — seguimiento de permiso de embarque | descripcion: Las operaciones de reembarco consignadas mediante los subregímenes RE01, RE04, RE05, RE06, REP1, REP4 o REP6 quedan exceptuadas del seguimiento de un permiso de embarque | tramo: Operaciones de reembarco consignadas mediante los subregímenes RE01, RE04, RE05, RE06, REP1, REP4 o REP6

## Unidad `ext::8.5.17.23` (item)
- herencia: [intro 8.5] La entidad podrá considerar cumplimentado parcial o totalmente el seguimiento de un permiso
de embarque cuando cuente con los elementos que le permitan considerar que la operación
se encuentra en alguna de las situaciones detalladas a continuación y se verifiquen las
condiciones previstas en cada caso.
La documentación utilizada para certificar el concepto y monto de las divisas imputado en
cada caso deberá quedar archivada en la entidad a disposición del BCRA. | **[abre la lista]** [intro 8.5.17] Por el valor que corresponda a ventajas aduaneras u otras situaciones previstas en el
siguiente listado de operaciones:
- texto propio: 8.5.17.23. Operaciones de trasbordo (artículos 410 a 416 de la Ley 22.415).
- entidades de la unidad:
  - `e1` Operacion: Operaciones de trasbordo — Operaciones de trasbordo reguladas por los artículos 410 a 416 de la Ley 22.415, exceptuadas del seguimiento de negociaciones de divisas por exportaciones de bienes.
  - `e2` Excepcion: Excepción trasbordo — seguimiento de divisas — Las operaciones de trasbordo quedan exceptuadas del seguimiento de negociaciones de divisas por exportaciones de bienes.
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 65** Excepcion `e2`: Excepción trasbordo — seguimiento de divisas | descripcion: Las operaciones de trasbordo quedan exceptuadas del seguimiento de negociaciones de divisas por exportaciones de bienes. | tramo: Operaciones de trasbordo (artículos 410 a 416 de la Ley 22.415)

## Unidad `cap::4.3.2` (punto_no_item)
- herencia: [intro 4.3] contraparte central.
Comprende a aquellas exposiciones de las entidades financieras con entidades de contrapar-
te central (CCP) que se originen en derivados OTC o negociados en mercados de valores y
en operaciones de financiación con títulos valores (“Securities Financing Transactions”, SFT)
y operaciones de liquidación diferida –definidas en el punto 4.2.–.
No están comprendidas las exposiciones originadas en operaciones al contado y que involu-
cren títulos valores, oro o moneda extranjera, c
- texto propio: 4.3.2. Alcance.
Cuando la entidad financiera realice operaciones con una QCCP deberá determinar
su exposición aplicando las disposiciones del punto 4.3.3., mientras que de tratarse
de una CCP que no califica serán de aplicación las previsiones del punto 4.3.4.
En los casos en que una CCP deje de calificar como QCCP, durante los tres meses
siguientes las operaciones podrán mantener el tratamiento del punto 4.3.3.; finalizado
ese plazo será de aplicación el punto 4.3.4.
Cuando se trate de una operación con derivados concertada en un mercado de
valores y la transacción entre el miembro compensador y la entidad financiera cliente
sea realizada y regida en el marco de un acuerdo bilateral, tanto la entidad financiera
cliente como el miembro compensador deberán dar a esa transacción el tratamiento
de un derivado OTC y aplicar lo previsto en el acápite ii) del punto 4.3.3.1. Este
tratamiento también se aplicará a las transacciones entre clientes de nivel inferior y
superior en una estructura multinivel.
- entidades de la unidad:
  - `e1` Operacion: Operaciones con QCCP — Operaciones que una entidad financiera realiza con una entidad de contraparte central calificada (QCCP), cuya exposición debe determinarse aplicando las disposiciones del punto 4.3.3.
  - `e2` Operacion: Operaciones con CCP no calificada — Operaciones que una entidad financiera realiza con una entidad de contraparte central que no califica como QCCP, cuya exigencia de capital se calcula conforme a lo previsto en el punto 4.3.4.
  - `e3` Condicion: CCP deja de calificar como QCCP — Supuesto en que una entidad de contraparte central pierde su calificación como QCCP.
  - `e4` Excepcion: Excepción tratamiento QCCP por tres meses — Las operaciones pueden mantener el tratamiento de QCCP durante tres meses después de que la CCP deje de calificar; finalizado ese plazo se aplica el punto 4.3.4.
  - `e5` Operacion: Derivados en mercado de valores con acuerdo bilateral — Operación con derivados concertada en un mercado de valores donde la transacción entre el miembro compensador y la entidad financiera cliente es realizada y regida en el marco de un acuerdo bilateral.
  - `e6` Obligacion: Tratamiento de derivado OTC para operaciones bilaterales — La entidad financiera cliente y el miembro compensador deben dar a la transacción el tratamiento de un derivado OTC y aplicar lo previsto en el acápite ii) del punto 4.3.3.1.
  - `e7` Obligacion: Tratamiento OTC en estructura multinivel — El tratamiento de derivado OTC también se aplica a las transacciones entre clientes de nivel inferior y superior en una estructura multinivel.
- relaciones del crudo (sin establecida_en ni de sujeto): e3 condicion_de e4
- NODOS A CLASIFICAR:
  - **caso 66** Excepcion `e4`: Excepción tratamiento QCCP por tres meses | descripcion: Las operaciones pueden mantener el tratamiento de QCCP durante tres meses después de que la CCP deje de calificar; finalizado ese plazo se aplica el punto 4.3.4. | tramo: durante los tres meses siguientes las operaciones podrán mantener el tratamiento del punto 4.3.3.

## Unidad `cla::2.2.1.3` (item)
- herencia: **[abre la lista]** [encabezado 2.2.1] 2.2.1. Los siguientes conceptos por intermediación financiera:
- texto propio: 2.2.1.3. Primas por opciones de compra y de venta tomadas.
- entidades de la unidad:
  - `e1` Operacion: Primas por opciones de compra y venta tomadas — Primas por opciones de compra y de venta tomadas en operaciones de intermediación financiera
  - `e2` Excepcion: Exclusión — Primas por opciones de compra y venta tomadas — Las primas por opciones de compra y de venta tomadas quedan excluidas de las financiaciones comprendidas
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 67** Excepcion `e2`: Exclusión — Primas por opciones de compra y venta tomadas | descripcion: Las primas por opciones de compra y de venta tomadas quedan excluidas de las financiaciones comprendidas | tramo: Primas por opciones de compra y de venta tomadas

## Unidad `ric::12.3` (punto_no_item)
- herencia: [encabezado S12] Sección 12. Disposiciones transitorias.
- texto propio: 12.3. Tratamiento de los defectos originados en el cómputo del 50 % –en lugar del 100 %– de los
resultados provenientes de los ajustes NIIF por primera vez dentro de la RPC (período enero
– marzo 2018).
Estos defectos se consideran admitidos (es decir que no constituirán incumplimientos) de
verificarse las siguientes condiciones:
a) surjan de la última conciliación de los estados contables trimestrales en el marco de la
convergencia a NIIF que cuente con informe de auditor externo;
b) dicha conciliación evidencia que de haberse considerado los resultados positivos al 100
% –en lugar del al 50 %– no se hubiera registrado tal defecto.
De reunir los requisitos citados, se consignará en la partida 60500000 la porción pertinente
para la neutralización del defecto generado.
A tal fin, se consignará como “número” y “fecha de Resolución” la de la Comunicación “A”
6456.
También se agregará una descripción detallada del cálculo del importe para el período in-
formado.
- entidades de la unidad:
  - `e1` Condicion: Defectos admitidos si surgen de última conciliación — El defecto se considera admitido si surge de la última conciliación de los estados contables trimestrales en el marco de la convergencia a NIIF que cuente con informe de auditor externo.
  - `e2` Condicion: Defectos admitidos si conciliación evidencia ausencia de defecto al 100 % — El defecto se considera admitido si la conciliación evidencia que de haberse considerado los resultados positivos al 100 % en lugar del 50 % no se hubiera registrado tal defecto.
  - `e3` Obligacion: Consignación en partida 60500000 de porción para neutralización — De reunir los requisitos citados, se consignará en la partida 60500000 la porción pertinente para la neutralización del defecto generado.
  - `e4` Obligacion: Consignación de número y fecha de Resolución A 6456 — Se consignará como número y fecha de Resolución la de la Comunicación A 6456.
  - `e5` Obligacion: Descripción detallada del cálculo del importe — Se agregará una descripción detallada del cálculo del importe para el período informado.
  - `e6` Comunicacion: Com. A 6456 — 
  - `e7` Excepcion: Defectos no constituyen incumplimientos si se verifican condiciones — Los defectos originados en el cómputo del 50 % en lugar del 100 % de los resultados provenientes de los ajustes NIIF no constituirán incumplimientos si se verifican las condiciones especificadas.
- relaciones del crudo (sin establecida_en ni de sujeto): e1 condicion_de e7; e2 condicion_de e7; to referencia e6
- NODOS A CLASIFICAR:
  - **caso 70** Excepcion `e7`: Defectos no constituyen incumplimientos si se verifican condiciones | descripcion: Los defectos originados en el cómputo del 50 % en lugar del 100 % de los resultados provenientes de los ajustes NIIF no constituirán incumplimientos si se verifican las condiciones especificadas. | tramo: Estos defectos se consideran admitidos (es decir que no constituirán incumplimientos) de verificarse las siguientes condiciones

## Unidad `ext::10.3.5::intro` (intro)
- herencia: [encabezado 10.3.5] 10.3.5. Pagos de importaciones de bienes ingresadas desde zonas francas con transferencia
- texto propio: aduanera de dominio del exportador al importador.
La entidad interviniente podrá dar acceso al mercado de cambios para el pago al
exterior de importaciones de bienes ingresadas desde zonas francas con
transferencia aduanera de dominio del exportador al importador en la medida que
verifique previamente que se cumplen la totalidad de requisitos detallados en el punto
10.3.2., reemplazando lo requerido en los incisos i), iii) y iv) del punto 10.3.2.1. por lo
siguiente:
- entidades de la unidad:
  - `e1` Operacion: Acceso al mercado de cambios para pago de importaciones desde zonas francas — Acceso al mercado de cambios para el pago al exterior de importaciones de bienes ingresadas desde zonas francas con transferencia aduanera de dominio del exportador al importador
  - `e2` Condicion: Verificación previa de requisitos del punto 10.3.2 — Se cumplen la totalidad de requisitos detallados en el punto 10.3.2, con la sustitución de lo requerido en los incisos i), iii) y iv) del punto 10.3.2.1 por lo siguiente
  - `e3` Excepcion: Sustitución de incisos i), iii) y iv) del punto 10.3.2.1 — Los incisos i), iii) y iv) del punto 10.3.2.1 quedan reemplazados por requisitos distintos para el acceso al mercado de cambios en importaciones desde zonas francas
  - `e4` Potestad: Facultad de dar acceso al mercado de cambios — La entidad interviniente tiene la facultad de dar acceso al mercado de cambios para el pago al exterior de importaciones de bienes ingresadas desde zonas francas con transferencia aduanera, sujeto a v
- relaciones del crudo (sin establecida_en ni de sujeto): e2 condicion_de e4
- NODOS A CLASIFICAR:
  - **caso 71** Excepcion `e3`: Sustitución de incisos i), iii) y iv) del punto 10.3.2.1 | descripcion: Los incisos i), iii) y iv) del punto 10.3.2.1 quedan reemplazados por requisitos distintos para el acceso al mercado de cambios en importaciones desde zonas francas | tramo: reemplazando lo requerido en los incisos i), iii) y iv) del punto 10.3.2.1. por lo siguiente:

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
  - **caso 86** Excepcion `e8`: Excepción — ampliación de margen crediticio | descripcion: No se considera refinanciación la asistencia a deudores en situación normal que implique mayor deuda por capital (neto de intereses y accesorios capitalizados) respecto del importe anterior, siempre que se evalúe la capacidad de pago del deudor. | tramo: A esos efectos, no se considerará refinanciación la asistencia que se otorgue a los deudores clasificados en esta categoría siempre que implique mayor deuda por capital –neto de los intereses y accesorios que se capitalicen– respecto del importe adeudado con anterioridad por el mismo concepto y que se evalúe la capacidad de pago del deudor para afrontar las obligaciones emergentes de esa ampliación del margen crediticio.

## Unidad `ctacte::1.5.2.9` (punto_no_item)
- herencia: [intro 1.5] En sus cláusulas se deberá prever, como mínimo: | [encabezado 1.5.2] 1.5.2. Obligaciones de la entidad.
- texto propio: 1.5.2.9. Constatar –tanto en los cheques librados en formato papel como en los certifica-
dos nominativos transferibles– la regularidad de la serie de endosos pero no la
autenticidad de la firma de los endosantes y verificar la firma del presentante,
que deberá insertarse con carácter de recibo.
Estas obligaciones recaen sobre la entidad girada cuando el cheque se presen-
te para el cobro en ella, en tanto que a la entidad en que se deposita el cheque
–cuando sea distinta de la girada– le corresponde controlar que la última firma
extendida en carácter de recibo contenga las especificaciones fijadas en el pun-
to 5.1.3., salvo que resulte aplicable el procedimiento de truncamiento, en cuyo
caso se estará a lo previsto en los respectivos convenios.
Cuando la presentación se efectúe a través de mandatario o beneficiario de una
cesión ordinaria, deberá verificarse además el instrumento por el cual se haya
otorgado el mandato o efectuado la cesión, excepto cuando la gestión de cobro
sea realizada por una entidad financiera no autorizada a captar depósitos en
cuenta corriente.
- entidades de la unidad:
  - `e1` Operacion: Constatar regularidad de serie de endosos — Constatar la regularidad de la serie de endosos en cheques librados en formato papel y en certificados nominativos transferibles
  - `e2` Restriccion: No verificar autenticidad de firma de endosantes — No verificar la autenticidad de la firma de los endosantes
  - `e3` Operacion: Verificar firma del presentante como recibo — Verificar la firma del presentante, que deberá insertarse con carácter de recibo
  - `e4` Obligacion: Obligación de constatar y verificar — entidad girada — La entidad girada debe constatar la regularidad de la serie de endosos y verificar la firma del presentante cuando el cheque se presente para el cobro en ella
  - `e5` Obligacion: Controlar última firma de recibo — entidad depositaria — La entidad en que se deposita el cheque, cuando sea distinta de la girada, debe controlar que la última firma extendida en carácter de recibo contenga las especificaciones fijadas en el punto 5.1.3.
  - `e6` Excepcion: Excepción — procedimiento de truncamiento — No aplica la obligación de controlar la última firma de recibo cuando resulte aplicable el procedimiento de truncamiento; en ese caso se estará a lo previsto en los respectivos convenios
  - `e7` Obligacion: Verificar instrumento de mandato o cesión — Cuando la presentación se efectúe a través de mandatario o beneficiario de una cesión ordinaria, debe verificarse el instrumento por el cual se haya otorgado el mandato o efectuado la cesión
  - `e8` Excepcion: Excepción — entidad financiera no autorizada a captar depósitos — No se requiere verificar el instrumento de mandato o cesión cuando la gestión de cobro sea realizada por una entidad financiera no autorizada a captar depósitos en cuenta corriente
  - `e9` Condicion: Condición — presentación a través de mandatario o cesionario — La obligación de verificar el instrumento de mandato o cesión se activa cuando la presentación se efectúe a través de mandatario o beneficiario de una cesión ordinaria
- relaciones del crudo (sin establecida_en ni de sujeto): e8 exceptua_obligacion e7; e9 condicion_de e7
- NODOS A CLASIFICAR:
  - **caso 73** Excepcion `e6`: Excepción — procedimiento de truncamiento | descripcion: No aplica la obligación de controlar la última firma de recibo cuando resulte aplicable el procedimiento de truncamiento; en ese caso se estará a lo previsto en los respectivos convenios | tramo: salvo que resulte aplicable el procedimiento de truncamiento, en cuyo caso se estará a lo previsto en los respectivos convenios

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
  - **caso 74** Excepcion `e1`: Excepción — operaciones punto 3.14.2 | descripcion: No aplican los requisitos de declaración jurada de los puntos 3.16.3.1 a 3.16.3.4 para operaciones de clientes realizadas en el marco del punto 3.14.2 | tramo: Lo previsto en los puntos 3.16.3.1. al 3.16.3.4. no resultará aplicable para aquellas operaciones de egresos que correspondan a: i) operaciones de clientes realizadas en el marco del punto 3.14.2.
  - **caso 75** Excepcion `e3`: Excepción — operaciones punto 3.13.1.4 cursadas automáticamente | descripcion: No aplican los requisitos de declaración jurada de los puntos 3.16.3.1 a 3.16.3.4 para operaciones del punto 3.13.1.4 cursadas automáticamente por la entidad como apoderada del beneficiario no residente | tramo: Lo previsto en los puntos 3.16.3.1. al 3.16.3.4. no resultará aplicable para aquellas operaciones de egresos que correspondan a: iii) operaciones comprendidas en el punto 3.13.1.4. en la medida que las mismas sean cursadas en forma automática por la entidad en su carácter de apoderada del beneficiario no residente.
  - **caso 76** Excepcion `e2`: Excepción — cancelaciones de financiaciones en moneda extranjera | descripcion: No aplican los requisitos de declaración jurada de los puntos 3.16.3.1 a 3.16.3.4 para cancelaciones de financiaciones en moneda extranjera otorgadas por entidades financieras locales, incluyendo pagos por consumos en moneda extranjera mediante tarjetas de crédito o de compra | tramo: Lo previsto en los puntos 3.16.3.1. al 3.16.3.4. no resultará aplicable para aquellas operaciones de egresos que correspondan a: ii) cancelaciones de financiaciones en moneda extranjera otorgadas por entidades financieras locales, incluyendo los pagos por los consumos en moneda extranjera efectuados mediante tarjetas de crédito o de compra;
  - **caso 77** Excepcion `e4`: Excepción — repatriaciones de inversiones de portafolio | descripcion: No aplican los requisitos de declaración jurada de los puntos 3.16.3.1 a 3.16.3.4 para repatriaciones de inversiones de portafolio de no residentes cursadas conforme al punto 3.13.1.12 | tramo: Lo previsto en los puntos 3.16.3.1. al 3.16.3.4. no resultará aplicable para aquellas operaciones de egresos que correspondan a: iv) las repatriaciones de inversiones de portafolio de no residentes cursadas en el marco de lo dispuesto en el punto 3.13.1.12.

## Unidad `ext::3.16.3.7` (item)
- herencia: [chapeau_seccion S3] Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas
en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–,
adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán
cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables. | [intro 3.16.3] operaciones con títulos valores y otros activos.
En el caso de que el cliente no sea una persona humana residente, la entidad deberá
contar con la conformidad previa del BCRA excepto que cuente con una declaración
jurada del cliente en la que deje constancia de que: | **[abre la lista]** [intersticial 3.16.3] En caso de que el cliente sea una persona jurídica, para que la operación no quede
comprendida por el requisito de conformidad previa, la entidad deberá contar
adicionalmente con una declaración jurada en la que conste:
- texto propio: 3.16.3.7. La entidad también podrá considerar cumplimentado lo indicado en los
puntos 3.16.3.3. y 3.16.3.4. cuando:
i) el cliente haya presentado una declaración jurada dejando constancia
de que en el plazo previsto en el punto 3.16.3.4., salvo por aquellos
directamente asociados a operaciones habituales en el marco del
desarrollo de su actividad, no ha entregado en el país fondos en
moneda local ni otros activos locales líquidos -excepto fondos en
moneda extranjera depositados en entidades financieras locales- a
ninguna persona humana o jurídica,
ii) el cliente haya presentado una declaración jurada rubricada por cada
persona humana o jurídica detallada en el punto 3.16.3.3. a la cual el
cliente le haya entregado fondos en los términos previstos en el punto
3.16.3.4., dejando constancia de lo requerido en los puntos 3.16.3.1.,
3.16.3.2. y 3.16.3.4.
iii)el cliente haya presentado una declaración jurada rubricada por cada
persona humana o jurídica detallada en el punto 3.16.3.3., en la cual
deje constancia de que:
a)que cumple lo requerido en los puntos 3.16.3.1. y 3.16.3.2.; o
b) que en el plazo previsto en el punto 3.16.3.4., salvo por aquellos
directamente asociados a operaciones habituales entre residentes
de adquisición de bienes y/o servicios, no ha recibido en el país
fondos en moneda local ni otros activos locales líquidos -excepto
fondos en moneda extranjera depositados en entidades
financieras locales- que hayan provenido del cliente o de alguna
persona detallada en el punto 3.16.3.3. a la cual el cliente le haya
entregado fondos en los términos previstos en el punto 3.16.3.4.
En caso de que alguna de las personas detallada en el punto 3.16.3.3. sea
un ente perteneciente al sector público nacional, no será necesaria la
presentación por parte de ese ente de la d
- entidades de la unidad:
  - `e1` Operacion: Cumplimiento de requisitos 3.16.3.3 y 3.16.3.4 — Consideración de cumplimiento de los requisitos indicados en los puntos 3.16.3.3. y 3.16.3.4. cuando se verifican las condiciones enumeradas en los incisos i), ii) o iii).
  - `e2` Condicion: Declaración jurada cliente — fondos no entregados — El cliente ha presentado declaración jurada acreditando que, en el plazo del punto 3.16.3.4., salvo fondos asociados a operaciones habituales de su actividad, no ha entregado en el país fondos en mone
  - `e3` Condicion: Declaración jurada rubricada — personas receptoras de fondos — El cliente ha presentado declaración jurada rubricada por cada persona humana o jurídica (detallada en punto 3.16.3.3.) a la cual le entregó fondos, dejando constancia de lo requerido en los puntos 3.
  - `e4` Condicion: Declaración jurada rubricada — cumplimiento o no recepción de fondos — El cliente ha presentado declaración jurada rubricada por cada persona humana o jurídica (detallada en punto 3.16.3.3.) en la cual consta: (a) que cumple lo requerido en puntos 3.16.3.1. y 3.16.3.2.; 
  - `e5` Excepcion: Excepción — entes sector público nacional — No es necesaria la presentación de declaración jurada por parte de entes del sector público nacional detallados en punto 3.16.3.3. para considerar cumplimentado lo requerido en los incisos ii) o iii).
  - `e6` Excepcion: Excepción — entes sector público nacional (inciso iii) — No es necesaria la presentación de declaración jurada por parte de entes del sector público nacional detallados en punto 3.16.3.3. para considerar cumplimentado lo requerido en los incisos ii) o iii).
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 79** Excepcion `e5`: Excepción — entes sector público nacional | descripcion: No es necesaria la presentación de declaración jurada por parte de entes del sector público nacional detallados en punto 3.16.3.3. para considerar cumplimentado lo requerido en los incisos ii) o iii). | tramo: En caso de que alguna de las personas detallada en el punto 3.16.3.3. sea un ente perteneciente al sector público nacional, no será necesaria la presentación por parte de ese ente de la declaración jurada requerida en los puntos ii) o iii) precedentes para considerar cumplimentado lo requerido.
  - **caso 168** Condicion `e2`: Declaración jurada cliente — fondos no entregados | descripcion: El cliente ha presentado declaración jurada acreditando que, en el plazo del punto 3.16.3.4., salvo fondos asociados a operaciones habituales de su actividad, no ha entregado en el país fondos en moneda local ni otros activos locales líquidos (excepto fondos en moneda extranjera en entidades financieras locales) a ninguna persona. | tramo: el cliente haya presentado una declaración jurada dejando constancia de que en el plazo previsto en el punto 3.16.3.4., salvo por aquellos directamente asociados a operaciones habituales en el marco del desarrollo de su actividad, no ha entregado en el país fondos en moneda local ni otros activos locales líquidos -excepto fondos en moneda extranjera depositados en entidades financieras locales- a ninguna persona humana o jurídica
  - **caso 169** Condicion `e4`: Declaración jurada rubricada — cumplimiento o no recepción de fondos | descripcion: El cliente ha presentado declaración jurada rubricada por cada persona humana o jurídica (detallada en punto 3.16.3.3.) en la cual consta: (a) que cumple lo requerido en puntos 3.16.3.1. y 3.16.3.2.; o (b) que en el plazo del punto 3.16.3.4., salvo fondos asociados a operaciones habituales entre residentes de adquisición de bienes/servicios, no ha recibido en el país fondos en moneda local ni otros activos locales líquidos (excepto fondos en moneda extranjera en entidades financieras locales) provenientes del cliente o de personas a las cuales el cliente entregó fondos. | tramo: el cliente haya presentado una declaración jurada rubricada por cada persona humana o jurídica detallada en el punto 3.16.3.3., en la cual deje constancia de que: a)que cumple lo requerido en los puntos 3.16.3.1. y 3.16.3.2.; o b) que en el plazo previsto en el punto 3.16.3.4., salvo por aquellos directamente asociados a operaciones habituales entre residentes de adquisición de bienes y/o servicios, no ha recibido en el país fondos en moneda local ni otros activos locales líquidos -excepto fondos en moneda extranjera depositados en entidades financieras locales- que hayan provenido del cliente o de alguna persona detallada en el punto 3.16.3.3. a la cual el cliente le haya entregado fondos en los términos previstos en el punto 3.16.3.4.
  - **caso 170** Condicion `e3`: Declaración jurada rubricada — personas receptoras de fondos | descripcion: El cliente ha presentado declaración jurada rubricada por cada persona humana o jurídica (detallada en punto 3.16.3.3.) a la cual le entregó fondos, dejando constancia de lo requerido en los puntos 3.16.3.1., 3.16.3.2. y 3.16.3.4. | tramo: el cliente haya presentado una declaración jurada rubricada por cada persona humana o jurídica detallada en el punto 3.16.3.3. a la cual el cliente le haya entregado fondos en los términos previstos en el punto 3.16.3.4., dejando constancia de lo requerido en los puntos 3.16.3.1., 3.16.3.2. y 3.16.3.4.

## Unidad `cla::1.2.2` (punto_no_item)
- herencia: [encabezado 1.2] 1.2. Criterios especiales de imputación.
- texto propio: 1.2.2. Deudores en concurso preventivo.
En el caso de deudores que hayan solicitado su concurso preventivo, los créditos que les
sean otorgados con posterioridad a ese pedido, en la medida que cuenten con garantías
de terceros que permitan su cobro al vencimiento sin necesidad de la intervención del
cliente en concurso, a los fines de esta clasificación podrán imputarse -a opción de la
entidad- al tercero constituido en principal o directo pagador o avalista o codeudor que
haya renunciado al beneficio de excusión.
Igual temperamento podrá observarse cuando se trate de créditos respecto de documen-
tos o valores cedidos por el deudor en concurso que puedan considerarse garantías pre-
feridas “A” por ser cobrables directamente del tercero responsable del documento (por
ejemplo: facturas de crédito, facturas a consumidores emitidas por empresas de servicios
públicos proveedoras de electricidad, gas, etc., cupones de tarjetas de crédito, etc.). En
los casos de deudores por servicios públicos o por tarjetas de crédito, no será obligatoria
la apertura del legajo.
- entidades de la unidad:
  - `e1` Operacion: Otorgamiento de créditos a deudor en concurso preventivo — Créditos otorgados a deudores que hayan solicitado concurso preventivo, con posterioridad a ese pedido, que cuenten con garantías de terceros que permitan su cobro al vencimiento sin necesidad de la i
  - `e2` Potestad: Opción de imputación a tercero — créditos en concurso — La entidad tiene la opción de imputar los créditos otorgados a deudor en concurso preventivo al tercero constituido en principal o directo pagador o avalista o codeudor que haya renunciado al benefici
  - `e3` Condicion: Garantías de terceros que permitan cobro al vencimiento — Los créditos deben contar con garantías de terceros que permitan su cobro al vencimiento sin necesidad de la intervención del cliente en concurso.
  - `e4` Operacion: Créditos sobre documentos o valores cedidos por deudor en concurso — Créditos respecto de documentos o valores cedidos por el deudor en concurso que puedan considerarse garantías preferidas "A" por ser cobrables directamente del tercero responsable del documento (por e
  - `e5` Potestad: Opción de imputación a tercero — créditos sobre documentos cedidos — La entidad tiene la opción de observar igual temperamento (imputar al tercero responsable) cuando se trate de créditos respecto de documentos o valores cedidos por el deudor en concurso que puedan con
  - `e6` Excepcion: No obligatoriedad de apertura de legajo — deudores por servicios públicos o tarjetas — No es obligatoria la apertura del legajo en los casos de deudores por servicios públicos o por tarjetas de crédito.
- relaciones del crudo (sin establecida_en ni de sujeto): e3 condicion_de e2
- NODOS A CLASIFICAR:
  - **caso 81** Excepcion `e6`: No obligatoriedad de apertura de legajo — deudores por servicios públicos o tarjetas | descripcion: No es obligatoria la apertura del legajo en los casos de deudores por servicios públicos o por tarjetas de crédito. | tramo: En los casos de deudores por servicios públicos o por tarjetas de crédito, no será obligatoria la apertura del legajo.

## Unidad `cla::3.4.2` (punto_no_item)
- herencia: [encabezado 3.4] 3.4. Legajo del cliente.
- texto propio: 3.4.2. Contenido.
En el legajo se reunirán todos los elementos de juicio que se tengan en cuenta para rea-
lizar las evaluaciones y clasificaciones y se dejará constancia de las revisiones efectua-
das y de la clasificación asignada.
Cuando no corresponda evaluar la capacidad de repago del deudor por encontrarse la
deuda cubierta con garantías preferidas “A”, según lo previsto en el punto 4.4., no será
obligatorio incorporar al legajo del cliente el flujo de fondos, los estados contables ni toda
otra información necesaria para efectuar ese análisis.
A los fines de la actualización del legajo del cliente, se admitirá que la clasificación asig-
nada se mantenga en planillas separadas, siempre que el procedimiento adoptado –que
deberá estar descripto en el “Manual de procedimientos de clasificación y previsión”–
permita la identificación precisa de la clasificación asignada a cada cliente desde la plani-
lla al legajo y viceversa.
Dicho legajo deberá contar con información acerca de los márgenes crediticios, discrimi-
nado –de corresponder– por tipo o línea, conforme al punto 1.1.3.2., acápite ii) del TO
sobre Gestión Crediticia.
Las entidades financieras deberán comunicar a los deudores los cambios negativos en la
clasificación que se les asigne, siendo optativo cuando el saldo de deuda sea inferior al
monto establecido en el punto 2. “Deudores Comprendidos” de la Sección 3. “Deudores
del sistema financiero” –Normas de Procedimiento– del Régimen Informativo Contable
Mensual.
Deberán informarse los cambios negativos en la clasificación a los deudores que sean
clasificados en las situaciones 3, 4 o 5 y de los deudores en gestión judicial o extrajudi-
cial de cobro (estos últimos, en la medida que cuenten con notificaciones postales o
fehacientes respecto al inicio de las ge
- entidades de la unidad:
  - `e1` Obligacion: Reunir elementos de juicio en legajo — Reunir en el legajo todos los elementos de juicio para evaluaciones y clasificaciones, dejando constancia de revisiones y clasificación asignada.
  - `e2` Excepcion: Excepción — información no obligatoria con garantías preferidas A — No es obligatorio incorporar flujo de fondos, estados contables ni información para análisis de capacidad de repago cuando la deuda está cubierta con garantías preferidas A.
  - `e3` Obligacion: Permitir clasificación en planillas separadas con procedimiento descrito — Se admite mantener la clasificación en planillas separadas si el procedimiento (descrito en Manual de procedimientos) permite identificar precisamente la clasificación de cada cliente entre planilla y
  - `e4` Obligacion: Incluir información de márgenes crediticios en legajo — El legajo debe incluir información sobre márgenes crediticios, discriminados por tipo o línea según corresponda, conforme a normas de Gestión Crediticia.
  - `e5` Obligacion: Comunicar cambios negativos en clasificación a deudores — Comunicar a los deudores los cambios negativos en su clasificación; es optativo cuando el saldo de deuda sea inferior al monto establecido en el Régimen Informativo Contable Mensual.
  - `e6` Obligacion: Informar cambios negativos a deudores en situaciones 3, 4, 5 o en gestión de cobro — Informar cambios negativos en clasificación a deudores en situaciones 3, 4 o 5, y a deudores en gestión judicial o extrajudicial de cobro (si cuentan con notificaciones postales o fehacientes del inic
  - `e7` Obligacion: Remitir información de cambios dentro de 45 días por medios especificados — Remitir información de cambios negativos a deudores dentro de 45 días de la reclasificación, mediante: resumen impreso de movimientos, resumen de cuenta de tarjetas, recibo de pago, o correspondencia 
  - `e8` Obligacion: Informar a clientes por home banking en igual plazo — Las entidades financieras que ofrecen home banking deben informar a cada cliente por ese medio la información de cambios negativos en clasificación en igual plazo (45 días).
  - `e9` Obligacion: Mantener disponible saldo actualizado de financiaciones — Mantener disponible el saldo actualizado de todas las financiaciones otorgadas (incluyendo filiales y unidades operativas), discriminado por concepto, en el lugar del legajo o casa central según corre
  - `e10` Obligacion: Mantener declaración jurada sobre vinculación para clientes sector privado no financiero — Mantener en el legajo declaración jurada sobre vinculación e influencia controlante de clientes del sector privado no financiero cuya deuda total exceda del 2,5% de responsabilidad patrimonial computa
  - `e11` Obligacion: Incluir información de corresponsales en legajo — El legajo de corresponsales debe contener información sobre identificación, calificación, márgenes de crédito y datos vinculados a esa relación, conforme a normas de Cuentas de corresponsalía.
  - `e12` Obligacion: Constar análisis de graduación del crédito en legajos — Los legajos deben incluir los análisis realizados por aplicación de normas sobre graduación del crédito.
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 82** Excepcion `e2`: Excepción — información no obligatoria con garantías preferidas A | descripcion: No es obligatorio incorporar flujo de fondos, estados contables ni información para análisis de capacidad de repago cuando la deuda está cubierta con garantías preferidas A. | tramo: Cuando no corresponda evaluar la capacidad de repago del deudor por encontrarse la deuda cubierta con garantías preferidas "A", según lo previsto en el punto 4.4., no será obligatorio incorporar al legajo del cliente el flujo de fondos, los estados contables ni toda otra información necesaria para efectuar ese análisis.

## Unidad `cap::10.2.2.6` (item)
- herencia: **[abre la lista]** [intro 10.2.2] Las ECAI deberán cumplir cada uno de los siguientes seis criterios:
- texto propio: 10.2.2.6. Credibilidad.
Las evaluaciones de crédito de las ECAI deben ser confiables para terceros
independientes. Además, la existencia de procedimientos internos destina-
dos a prevenir el uso indebido de información confidencial contribuye a la
credibilidad de una ECAI. Para ser reconocida, no es requisito que una ECAI
evalúe empresas en más de un país.
- entidades de la unidad:
  - `e1` Obligacion: Confiabilidad de evaluaciones de crédito — Las evaluaciones de crédito de las ECAI deben ser confiables para terceros independientes
  - `e2` Obligacion: Procedimientos internos para prevenir uso indebido de información — Existencia de procedimientos internos destinados a prevenir el uso indebido de información confidencial para contribuir a la credibilidad de una ECAI
  - `e3` Excepcion: No requisito de evaluación en múltiples países — No es requisito que una ECAI evalúe empresas en más de un país para ser reconocida
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 83** Excepcion `e3`: No requisito de evaluación en múltiples países | descripcion: No es requisito que una ECAI evalúe empresas en más de un país para ser reconocida | tramo: Para ser reconocida, no es requisito que una ECAI evalúe empresas en más de un país

## Unidad `ext::4.3.2::cierre` (cierre)
- herencia: [encabezado 4.3.2] 4.3.2. Las operaciones de compraventa de títulos valores con liquidación en moneda
- texto propio: En ningún caso se permite la liquidación de estas operaciones mediante el pago en
billetes en moneda extranjera o mediante su depósito en cuentas custodia o en
cuentas de terceros, excepto que se trate de operaciones contra cable que utilicen
cuentas de terceros en el marco de lo contemplado en el punto 4.3.2.3.
Los requisitos previstos en los puntos 4.3.2.1. y 4.3.2.2. no resultarán aplicables en las
compras de títulos valores que:
i) sean concretadas por los clientes con fondos en moneda extranjera recibidos en
los 15 (quince) días hábiles previos a partir del cobro de capital y/o intereses de
títulos de deuda emitidos por residentes; y
ii) la reinversión de los fondos por parte del beneficiario resulte neutra en materia
impositiva respecto de la operatoria de acreditación de los fondos en una cuenta
a la vista del beneficiario en una entidad financiera y su posterior débito para la
compra de valores.
- entidades de la unidad:
  - `e1` Restriccion: Prohibición liquidación en billetes o depósito custodia — Se prohíbe la liquidación de operaciones de compraventa de títulos valores con liquidación en moneda mediante el pago en billetes en moneda extranjera o mediante su depósito en cuentas custodia o en c
  - `e2` Excepcion: Excepción operaciones contra cable con cuentas de terceros — Quedan exceptuadas de la prohibición de liquidación mediante depósito en cuentas de terceros las operaciones contra cable que utilicen cuentas de terceros conforme a lo previsto en el punto 4.3.2.3.
  - `e3` Excepcion: Excepción compras con fondos recibidos por cobro de títulos — No resultan aplicables los requisitos de los puntos 4.3.2.1 y 4.3.2.2 en las compras de títulos valores concretadas por los clientes con fondos en moneda extranjera recibidos en los 15 días hábiles pr
  - `e4` Condicion: Condición reinversión neutra en materia impositiva — La reinversión de los fondos por parte del beneficiario debe resultar neutra en materia impositiva respecto de la operatoria de acreditación de los fondos en una cuenta a la vista del beneficiario en 
- relaciones del crudo (sin establecida_en ni de sujeto): e2 exceptua e1; e4 condicion_de e3
- NODOS A CLASIFICAR:
  - **caso 84** Excepcion `e3`: Excepción compras con fondos recibidos por cobro de títulos | descripcion: No resultan aplicables los requisitos de los puntos 4.3.2.1 y 4.3.2.2 en las compras de títulos valores concretadas por los clientes con fondos en moneda extranjera recibidos en los 15 días hábiles previos al cobro de capital y/o intereses de títulos de deuda emitidos por residentes. | tramo: Los requisitos previstos en los puntos 4.3.2.1. y 4.3.2.2. no resultarán aplicables en las compras de títulos valores que: i) sean concretadas por los clientes con fondos en moneda extranjera recibidos en los 15 (quince) días hábiles previos a partir del cobro de capital y/o intereses de títulos de deuda emitidos por residentes

## Unidad `ext::3.16.2.1` (item)
- herencia: [chapeau_seccion S3] Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas
en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–,
adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán
cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables. | **[abre la lista]** [intro 3.16.2] y/o certificados de depósitos argentinos representativos de acciones extranjeras.
La entidad deberá contar con la conformidad previa del BCRA excepto que cuente al
momento de acceso al mercado de cambios con una declaración jurada del cliente en
la que deje constancia de que: | [cierre 3.16.2] Este requisito no resultará a aplicación para aquellas operaciones de egresos que
correspondan a: | [cierre 3.16.2] i) operaciones de clientes realizadas en el marco de los puntos 3.8., 3.9., 3.13., | [cierre 3.16.2] 3.14.1. y 3.14.2.; | [cierre 3.16.2] ii) operaciones propias de una entidad en carácter de cliente;
iii) cancelaciones de financiaciones en moneda extranjera otorgadas por entidades | [cierre 3.16.2] financieras locales por los consumos en moneda extranjera efectuados
mediante tarjetas de crédito o de compra; o | [cierre 3.16.2] iv) pagos al exterior de las empresas no financieras emisoras de tarjetas por el uso | [cierre 3.16.2] de tarjetas de crédito, de compra, de débito o prepagas emitidas en el país.
- texto propio: 3.16.2.1. La totalidad de sus tenencias de moneda extranjera en el país se
encuentran depositadas en cuentas en entidades financieras y que no
poseía, al inicio del día en que solicita el acceso al mercado, certificados de
depósitos argentinos representativos de acciones extranjeras (CEDEARs)
y/o activos externos líquidos disponibles que conjuntamente tengan un
valor superior al equivalente de USD 100.000 (dólares estadounidenses
cien mil).
Serán considerados activos externos líquidos, entre otros: las tenencias de
billetes y monedas en moneda extranjera, disponibilidades en oro
amonedado o en barras de buena entrega, depósitos a la vista en
entidades financieras del exterior y otras inversiones que permitan obtener
disponibilidad inmediata de moneda extranjera (por ejemplo, inversiones en
títulos públicos externos con custodia en el país o en el exterior, fondos en
cuentas de inversión en administradores de inversiones radicados en el
exterior, criptoactivos, fondos en cuentas de proveedores de servicios de
pago, etc.).
No deben considerarse activos externos líquidos disponibles a aquellos
fondos depositados en el exterior que no pudiesen ser utilizados por el
cliente por tratarse de fondos de reserva o de garantía constituidos en
virtud de las exigencias previstas en contratos de endeudamiento con el
exterior, prefinanciaciones de exportaciones comprendidas en el punto
7.8.5. o de fondos constituidos como garantía de operaciones con
derivados concertadas en el exterior.
En el caso de que el cliente tuviera activos externos líquidos disponibles y/o
CEDEARs por un monto superior al establecido en el primer párrafo, la
entidad también podrá aceptar una declaración jurada del cliente en la que
deje constancia que no se excede tal monto al considerar que, parcial o
totalme
- entidades de la unidad:
  - `c1` Condicion: Tenencias de moneda extranjera depositadas en entidades financieras — La totalidad de las tenencias de moneda extranjera en el país están depositadas en cuentas en entidades financieras
  - `c2` Condicion: Ausencia de CEDEARs y activos externos líquidos superiores a USD 100.000 — No posee, al inicio del día en que solicita acceso al mercado, CEDEARs y/o activos externos líquidos disponibles que conjuntamente superen USD 100.000
  - `d1` Definicion: Activos externos líquidos — Tenencias de billetes y monedas en moneda extranjera, disponibilidades en oro amonedado o en barras de buena entrega, depósitos a la vista en entidades financieras del exterior e inversiones que permi
  - `e0` Excepcion: Exclusión de fondos de reserva o garantía en el exterior — No se consideran activos externos líquidos disponibles los fondos depositados en el exterior que no puedan ser utilizados por el cliente por ser fondos de reserva o garantía constituidos en virtud de 
  - `p1` Potestad: Facultad de aceptar declaración jurada cuando activos externos líquidos superan USD 100.000 — Cuando el cliente tiene activos externos líquidos disponibles y/o CEDEARs por monto superior a USD 100.000, la entidad podrá aceptar una declaración jurada del cliente en la que conste que no se exced
  - `c3` Condicion: Activos utilizados durante la jornada para pagos en mercado local — Los activos externos líquidos fueron utilizados durante esa jornada para realizar pagos que hubieran tenido acceso al mercado local de cambios
  - `c4` Condicion: Activos transferidos a cuenta de corresponsalía — Los activos externos líquidos fueron transferidos a favor del cliente a una cuenta de corresponsalía de una entidad local autorizada a operar en cambios
  - `c5` Condicion: Fondos de cobros de exportaciones o enajenación de activos no financieros — Los fondos están depositados en cuentas bancarias en el exterior a nombre del cliente y se originan en cobros de exportaciones de bienes y/o servicios, anticipos, prefinanciaciones o posfinanciaciones
  - `c6` Condicion: Fondos de endeudamientos financieros punto 3.5 — Los fondos están depositados en cuentas bancarias en el exterior a nombre del cliente, se originan en endeudamientos financieros del punto 3.5. y su monto no supera el equivalente a pagar por capital 
  - `c7` Condicion: Fondos de desembolsos de endeudamientos últimos 180 días — Los fondos están depositados en cuentas bancarias en el exterior a nombre del cliente, se originan en desembolsos en el exterior recibidos a partir del 29/11/24 de endeudamientos financieros del punto
  - `c8` Condicion: Fondos de ventas de títulos valores con liquidación en moneda extranjera — Los fondos están depositados en cuentas bancarias en el exterior a nombre del cliente y se originan en ventas de títulos valores con liquidación en moneda extranjera del punto 3.16.3.6.iii)
  - `c9` Condicion: Fondos de emisiones de títulos de deuda últimos 120 días — Los fondos están depositados en cuentas bancarias en el exterior a nombre del cliente y se originan en emisiones de títulos de deuda concretadas en los 120 días corridos previos, susceptibles de ser e
  - `o1` Obligacion: Constar en declaración jurada valor de activos externos líquidos y montos asignados — En la declaración jurada del cliente deberá constar expresamente el valor de sus activos externos líquidos disponibles al inicio del día y los montos que asigna a cada una de las situaciones descripta
- relaciones del crudo (sin establecida_en ni de sujeto): c3 condicion_de p1; c4 condicion_de p1; c5 condicion_de p1; c6 condicion_de p1; c7 condicion_de p1; c8 condicion_de p1; c9 condicion_de p1; p1 requiere o1
- NODOS A CLASIFICAR:
  - **caso 87** Excepcion `e0`: Exclusión de fondos de reserva o garantía en el exterior | descripcion: No se consideran activos externos líquidos disponibles los fondos depositados en el exterior que no puedan ser utilizados por el cliente por ser fondos de reserva o garantía constituidos en virtud de exigencias de contratos de endeudamiento con el exterior, prefinanciaciones de exportaciones del punto 7.8.5. o fondos constituidos como garantía de operaciones con derivados en el exterior | tramo: No deben considerarse activos externos líquidos disponibles a aquellos fondos depositados en el exterior que no pudiesen ser utilizados por el cliente por tratarse de fondos de reserva o de garantía constituidos en virtud de las exigencias previstas en contratos de endeudamiento con el exterior, prefinanciaciones de exportaciones comprendidas en el punto 7.8.5. o de fondos constituidos como garantía de operaciones con derivados concertadas en el exterior
  - **caso 144** Condicion `c2`: Ausencia de CEDEARs y activos externos líquidos superiores a USD 100.000 | descripcion: No posee, al inicio del día en que solicita acceso al mercado, CEDEARs y/o activos externos líquidos disponibles que conjuntamente superen USD 100.000 | tramo: que no poseía, al inicio del día en que solicita el acceso al mercado, certificados de depósitos argentinos representativos de acciones extranjeras (CEDEARs) y/o activos externos líquidos disponibles que conjuntamente tengan un valor superior al equivalente de USD 100.000 (dólares estadounidenses cien mil)
  - **caso 248** Condicion `c1`: Tenencias de moneda extranjera depositadas en entidades financieras | descripcion: La totalidad de las tenencias de moneda extranjera en el país están depositadas en cuentas en entidades financieras | tramo: La totalidad de sus tenencias de moneda extranjera en el país se encuentran depositadas en cuentas en entidades financieras

## Unidad `ext::3.18.2.1` (item)
- herencia: [chapeau_seccion S3] Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas
en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–,
adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán
cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables. | **[abre la lista]** [intro 3.18.2] exportador deberá nominar una única entidad financiera local que será la
responsable de emitir las correspondientes certificaciones y remitirlas a las entidades
por las cuales el cliente desee acceder al mercado.
La entidad nominada podrá emitir una “Certificación de aumento de las exportaciones
de bienes en el año t” cuando se verifiquen la totalidad de los siguientes requisitos:
- texto propio: 3.18.2.1. El valor FOB de las exportaciones de bienes comprendidos en los puntos
7.1.1.2. a 7.1.1.5. embarcados en el año t y que cuenten con una
certificación de cumplido en el marco del SECOEXPO, es superior al valor
FOB de sus exportaciones para ese mismo conjunto de bienes
embarcadas en todo el año t-1.
A los efectos de este cómputo no deberán considerarse los bienes
exportados a través de operaciones exceptuadas del seguimiento en virtud
de lo dispuesto en el punto 8.5.17., las exportaciones a consumo con
despacho de importación temporaria (DIT) o aquellos que cuenten con las
ventajas aduaneras “EXPONOTITONEROSO” o “PROMOEXPO”.
- entidades de la unidad:
  - `e1` Operacion: Exportación de bienes con certificación SECOEXPO — Exportación de bienes comprendidos en los puntos 7.1.1.2. a 7.1.1.5., embarcados en el año t, con certificación de cumplido en el marco del SECOEXPO
  - `e2` Condicion: Aumento FOB año t respecto a año t-1 — El valor FOB de las exportaciones en el año t es superior al valor FOB de las exportaciones del mismo conjunto de bienes en el año t-1
  - `e3` Excepcion: Exclusión operaciones exceptuadas punto 8.5.17 — No se consideran en el cómputo los bienes exportados a través de operaciones exceptuadas del seguimiento conforme al punto 8.5.17
  - `e4` Excepcion: Exclusión exportaciones DIT — No se consideran en el cómputo las exportaciones a consumo con despacho de importación temporaria (DIT)
  - `e5` Excepcion: Exclusión bienes con ventajas aduaneras EXPONOTITONEROSO o PROMOEXPO — No se consideran en el cómputo los bienes que cuenten con las ventajas aduaneras EXPONOTITONEROSO o PROMOEXPO
- relaciones del crudo (sin establecida_en ni de sujeto): e2 condicion_de e1
- NODOS A CLASIFICAR:
  - **caso 88** Excepcion `e4`: Exclusión exportaciones DIT | descripcion: No se consideran en el cómputo las exportaciones a consumo con despacho de importación temporaria (DIT) | tramo: las exportaciones a consumo con despacho de importación temporaria (DIT)
  - **caso 89** Excepcion `e3`: Exclusión operaciones exceptuadas punto 8.5.17 | descripcion: No se consideran en el cómputo los bienes exportados a través de operaciones exceptuadas del seguimiento conforme al punto 8.5.17 | tramo: no deberán considerarse los bienes exportados a través de operaciones exceptuadas del seguimiento en virtud de lo dispuesto en el punto 8.5.17.
  - **caso 90** Excepcion `e5`: Exclusión bienes con ventajas aduaneras EXPONOTITONEROSO o PROMOEXPO | descripcion: No se consideran en el cómputo los bienes que cuenten con las ventajas aduaneras EXPONOTITONEROSO o PROMOEXPO | tramo: aquellos que cuenten con las ventajas aduaneras "EXPONOTITONEROSO" o "PROMOEXPO"

## Unidad `ext::14.2.1.2` (item)
- herencia: [chapeau_seccion S14] En esta sección se detallan las disposiciones complementarias en materia cambiaria que, en la
medida que las disposiciones generales no resulten más favorables, resultan aplicables a un
Vehículo de Proyecto Único (VPU) adherido al Régimen de Incentivo los referidas al “Régimen de
Incentivo para Grandes Inversiones” (RIGI) establecido en el Título VII de la Ley 27.742 y
reglamentado por el Decreto 749/24 y concordantes. | [intro 14.2] Adicionalmente lo previsto en la normativa general en materia de egresos por el mercado de
cambios, en la medida que se cumplan los restantes requisitos aplicables a cada operación,
por aquellas financiaciones o aportes de inversión directa recibidos por el VPU adherido a
partir de la vigencia de la Ley 27.742, las entidades podrán también dar acceso en las
siguientes situaciones: | **[abre la lista]** [intro 14.2.1] corresponda, sin necesidad de contar con la conformidad previa del BCRA si tal
requisito estuviese vigente, las entidades podrán darle acceso al cliente para pagar,
incluso antes de la fecha de vencimiento, los intereses devengados hasta la fecha
de acceso que se encuentren impagos y/o el capital pendiente de: | [cierre 14.2.1] En el caso de que la totalidad de los fondos obtenidos por la financiación no pudiese
ser computada como ingresada y liquidada en el mercado de cambios, las
entidades también podrán dar acceso al VPU adherido, sin necesidad de contar con
la conformidad previa del BCRA si tal requisito estuviese vigente, para realizar: | [cierre 14.2.1] i) pagos de intereses devengados hasta la fecha de acceso que se encuentren | [cierre 14.2.1] impagos y que correspondan a la porción del capital equivalente a la proporción
de los fondos recibidos por el VPU por la financiación que puede computarse
como ingresada y liquidada por el mercado de cambios. | [cierre 14.2.1] ii) pagos por capital adeudado que corresponda a la porción del capital | [cierre 14.2.1] equivalente a la proporción de los fondos recibidos por el VPU por la
financiación que puede computarse como ingresada y liquidada por el mercado
de cambios.
- texto propio: 14.2.1.2. emisiones de títulos de deuda con registro en el país suscriptos
íntegramente en el exterior y que fueron ingresados y liquidados en el
mercado de cambios.
- entidades de la unidad:
  - `e1` Operacion: Pago de intereses y capital — emisiones de títulos de deuda — Pago de intereses devengados hasta la fecha de acceso que se encuentren impagos y/o el capital pendiente de emisiones de títulos de deuda con registro en el país suscriptos íntegramente en el exterior
  - `e2` Potestad: Facultad de dar acceso al cliente para pagar — títulos de deuda — Las entidades quedan facultadas para dar acceso al cliente para pagar, incluso antes de la fecha de vencimiento, los intereses devengados hasta la fecha de acceso que se encuentren impagos y/o el capi
  - `e3` Excepcion: Excepción — conformidad previa del BCRA no requerida — No se requiere la conformidad previa del BCRA si tal requisito estuviese vigente para dar acceso al cliente para pagar intereses y capital de emisiones de títulos de deuda
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 92** Excepcion `e3`: Excepción — conformidad previa del BCRA no requerida | descripcion: No se requiere la conformidad previa del BCRA si tal requisito estuviese vigente para dar acceso al cliente para pagar intereses y capital de emisiones de títulos de deuda | tramo: sin necesidad de contar con la conformidad previa del BCRA si tal requisito estuviese vigente

## Unidad `cap::8.6.3` (item)
- herencia: **[abre la lista]** [intro 8.6] A los fines de todas las reglamentaciones vinculadas al capital, su integración y aumento, in-
clusive los referidos a planes de regularización y saneamiento y sin perjuicio de lo previsto en
los puntos 5.1. a 5.3. de las normas sobre “Autorización y composición del capital de entidades
financieras” en materia de negociación de acciones o de aportes irrevocables para futuros au-
mentos de capital, los aportes deben ser efectuados en efectivo.
Excepcionalmente, mediando autorización previa de la  | [cierre 8.6] En los casos comprendidos en los puntos 8.6.1. y 8.6.2., los aportes deberán registrarse a su
valor de mercado. Se entenderá que los instrumentos cuentan con valor de mercado cuando
tengan cotización habitual en las bolsas y mercados regulados del país o del exterior en los
que se negocien, con transacciones relevantes en cuyo monto, la eventual liquidación de las
tenencias no pueda distorsionar significativamente su cotización.
En los casos del punto 8.6.3., los aportes deberán registrarse a su | [cierre 8.6] n1 | [cierre 8.6] punto 8.3.4.
En ningún caso la capitalización de deuda podrá implicar una limitación o suspensión al dere-
cho de preferencia establecido en el artículo 194 de la Ley General de Sociedades, por lo que
no será aplicable lo dispuesto en el artículo 197 de dicha ley.
La decisión de capitalización de los conceptos indicados en los puntos 8.6.1. a 8.6.3. por parte
de la Asamblea (o autoridad equivalente) será “ad referéndum” de su aprobación por parte de
la SEFyC o, en su caso, del BCRA –puntos 5.1. 
- texto propio: 8.6.3. depósitos y otras obligaciones por intermediación financiera de la entidad.
- entidades de la unidad:
  - `e1` Operacion: Aporte de depósitos y obligaciones por intermediación financiera — Aporte de depósitos y otras obligaciones por intermediación financiera de la entidad como forma de capitalización
  - `e2` Obligacion: Registrar aportes a valor contable — depósitos sin negociación en mercados secundarios — Cuando se trate de depósitos y otras obligaciones por intermediación financiera que no cuenten con autorización para ser negociados en mercados secundarios regulados del país o del exterior, los aport
  - `e3` Condicion: Depósitos sin autorización para negociación en mercados secundarios — Supuesto en que los depósitos y obligaciones por intermediación financiera no cuentan con autorización para ser negociados en mercados secundarios regulados del país o del exterior
  - `e4` Obligacion: Considerar disposiciones sobre instrumentos de deuda computables — capitalización — Cuando se trate de instrumentos de deuda computables como CA o PNc, al admitir los aportes se deberá tener en cuenta lo dispuesto en el punto 8.3.4
  - `e5` Restriccion: Prohibición — capitalización de deuda limitando derecho de preferencia — La capitalización de deuda no podrá implicar una limitación o suspensión al derecho de preferencia establecido en el artículo 194 de la Ley General de Sociedades
  - `e6` Excepcion: Inaplicabilidad artículo 197 LGS — capitalización de deuda — No será aplicable lo dispuesto en el artículo 197 de la Ley General de Sociedades en materia de capitalización de deuda
  - `e7` Obligacion: Decisión de capitalización ad referéndum de aprobación — SEFyC o BCRA — La decisión de capitalización de los conceptos indicados en los puntos 8.6.1. a 8.6.3. por parte de la Asamblea (o autoridad equivalente) será ad referéndum de su aprobación por parte de la SEFyC o, e
  - `e8` Obligacion: Exposición en nota a estados contables — capitalización ad referéndum — La circunstancia de que la decisión de capitalización sea ad referéndum de aprobación deberá ser expuesta en nota a los estados contables de los períodos siguientes (trimestral o anual, según correspo
  - `e9` Obligacion: Deducción de aportes no notificados de RPC — hasta notificación de aprobación — Hasta tanto se le haya notificado la aprobación de los aportes y en la medida en que éstos hayan sido contabilizados, se deducirán del respectivo componente de la RPC de la entidad financiera
  - `e10` Obligacion: Mantenimiento de tratamiento de deuda subordinada capitalizada — como pasivo — Cuando los aportes contabilizados provengan de la capitalización de deuda subordinada o de instrumentos representativos de deuda que puedan ser considerados (total o parcialmente) como parte integrant
- relaciones del crudo (sin establecida_en ni de sujeto): e3 condicion_de e2
- NODOS A CLASIFICAR:
  - **caso 93** Excepcion `e6`: Inaplicabilidad artículo 197 LGS — capitalización de deuda | descripcion: No será aplicable lo dispuesto en el artículo 197 de la Ley General de Sociedades en materia de capitalización de deuda | tramo: no será aplicable lo dispuesto en el artículo 197 de dicha ley

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

## Unidad `ext::8.5.17.27` (item)
- herencia: [intro 8.5] La entidad podrá considerar cumplimentado parcial o totalmente el seguimiento de un permiso
de embarque cuando cuente con los elementos que le permitan considerar que la operación
se encuentra en alguna de las situaciones detalladas a continuación y se verifiquen las
condiciones previstas en cada caso.
La documentación utilizada para certificar el concepto y monto de las divisas imputado en
cada caso deberá quedar archivada en la entidad a disposición del BCRA. | **[abre la lista]** [intro 8.5.17] Por el valor que corresponda a ventajas aduaneras u otras situaciones previstas en el
siguiente listado de operaciones:
- texto propio: 8.5.17.27. Exportaciones de valores (billetes, monedas, etc.) mediante el régimen
EC51.
- entidades de la unidad:
  - `e1` Operacion: Exportación de valores mediante régimen EC51 — Exportación de valores (billetes, monedas, etc.) mediante el régimen EC51, operación aduanera exceptuada del seguimiento de permiso de embarque
  - `e2` Excepcion: Excepción seguimiento — exportaciones valores EC51 — Operación aduanera exceptuada del seguimiento de permiso de embarque por el valor que corresponda a ventajas aduaneras u otras situaciones previstas
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 95** Excepcion `e2`: Excepción seguimiento — exportaciones valores EC51 | descripcion: Operación aduanera exceptuada del seguimiento de permiso de embarque por el valor que corresponda a ventajas aduaneras u otras situaciones previstas | tramo: Exportaciones de valores (billetes, monedas, etc.) mediante el régimen EC51

## Unidad `ext::8.5.17.6` (item)
- herencia: [intro 8.5] La entidad podrá considerar cumplimentado parcial o totalmente el seguimiento de un permiso
de embarque cuando cuente con los elementos que le permitan considerar que la operación
se encuentra en alguna de las situaciones detalladas a continuación y se verifiquen las
condiciones previstas en cada caso.
La documentación utilizada para certificar el concepto y monto de las divisas imputado en
cada caso deberá quedar archivada en la entidad a disposición del BCRA. | **[abre la lista]** [intro 8.5.17] Por el valor que corresponda a ventajas aduaneras u otras situaciones previstas en el
siguiente listado de operaciones:
- texto propio: 8.5.17.6. Régimen de material promocional (Resolución General 2.345/07 de la
Administración Federal de Ingresos Públicos).
- entidades de la unidad:
  - `e1` Operacion: Régimen de material promocional — Operación aduanera exceptuada del seguimiento conforme a la Resolución General 2.345/07 de la Administración Federal de Ingresos Públicos
  - `e2` Excepcion: Excepción seguimiento — material promocional — Operación aduanera exceptuada del seguimiento de permisos de embarque por el régimen de material promocional regulado por la Resolución General 2.345/07 de la Administración Federal de Ingresos Públic
  - `e3` Comunicacion: Resolución General 2.345/07 — 
- relaciones del crudo (sin establecida_en ni de sujeto): to referencia e3
- NODOS A CLASIFICAR:
  - **caso 96** Excepcion `e2`: Excepción seguimiento — material promocional | descripcion: Operación aduanera exceptuada del seguimiento de permisos de embarque por el régimen de material promocional regulado por la Resolución General 2.345/07 de la Administración Federal de Ingresos Públicos | tramo: Régimen de material promocional (Resolución General 2.345/07 de la Administración Federal de Ingresos Públicos)

## Unidad `ext::8.5.17.17` (item)
- herencia: [intro 8.5] La entidad podrá considerar cumplimentado parcial o totalmente el seguimiento de un permiso
de embarque cuando cuente con los elementos que le permitan considerar que la operación
se encuentra en alguna de las situaciones detalladas a continuación y se verifiquen las
condiciones previstas en cada caso.
La documentación utilizada para certificar el concepto y monto de las divisas imputado en
cada caso deberá quedar archivada en la entidad a disposición del BCRA. | **[abre la lista]** [intro 8.5.17] Por el valor que corresponda a ventajas aduaneras u otras situaciones previstas en el
siguiente listado de operaciones:
- texto propio: 8.5.17.17. Exportación a consumo con Destinación de Importación Temporaria, sin
transformación (subregímenes EC02, EG02 o PER1). Se refiere a la
exportación a consumo de bienes que retorna en cumplimiento de una
obligación asumida en el régimen de importación temporaria, egresando
al exterior en el mismo estado en que se importó.
- entidades de la unidad:
  - `e1` Operacion: Exportación a consumo con Destinación de Importación Temporaria — Exportación a consumo de bienes que retorna en cumplimiento de una obligación asumida en el régimen de importación temporaria, egresando al exterior en el mismo estado en que se importó. Subregímenes:
  - `e2` Excepcion: Excepción seguimiento — Exportación a consumo con Destinación de Importación Temporaria — Operación exceptuada del seguimiento de divisas por exportaciones de bienes, por corresponder a ventajas aduaneras u otras situaciones previstas en el régimen de importación temporaria.
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 97** Excepcion `e2`: Excepción seguimiento — Exportación a consumo con Destinación de Importación Temporaria | descripcion: Operación exceptuada del seguimiento de divisas por exportaciones de bienes, por corresponder a ventajas aduaneras u otras situaciones previstas en el régimen de importación temporaria. | tramo: Exportación a consumo con Destinación de Importación Temporaria, sin transformación (subregímenes EC02, EG02 o PER1)

## Unidad `ext::8.5.17.21` (item)
- herencia: [intro 8.5] La entidad podrá considerar cumplimentado parcial o totalmente el seguimiento de un permiso
de embarque cuando cuente con los elementos que le permitan considerar que la operación
se encuentra en alguna de las situaciones detalladas a continuación y se verifiquen las
condiciones previstas en cada caso.
La documentación utilizada para certificar el concepto y monto de las divisas imputado en
cada caso deberá quedar archivada en la entidad a disposición del BCRA. | **[abre la lista]** [intro 8.5.17] Por el valor que corresponda a ventajas aduaneras u otras situaciones previstas en el
siguiente listado de operaciones:
- texto propio: 8.5.17.21. Destinaciones suspensivas de exportaciones temporarias (artículos 349 a
373 del Código Aduanero).
- entidades de la unidad:
  - `e1` Operacion: Destinaciones suspensivas exportaciones temporarias — Destinaciones suspensivas de exportaciones temporarias conforme a los artículos 349 a 373 del Código Aduanero
  - `e2` Excepcion: Excepción seguimiento — destinaciones suspensivas — Operación exceptuada del seguimiento de permisos de embarque por el valor que corresponda a ventajas aduaneras u otras situaciones previstas
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 98** Excepcion `e2`: Excepción seguimiento — destinaciones suspensivas | descripcion: Operación exceptuada del seguimiento de permisos de embarque por el valor que corresponda a ventajas aduaneras u otras situaciones previstas | tramo: Destinaciones suspensivas de exportaciones temporarias (artículos 349 a 373 del Código Aduanero)

## Unidad `ext::8.5.17.11` (item)
- herencia: [intro 8.5] La entidad podrá considerar cumplimentado parcial o totalmente el seguimiento de un permiso
de embarque cuando cuente con los elementos que le permitan considerar que la operación
se encuentra en alguna de las situaciones detalladas a continuación y se verifiquen las
condiciones previstas en cada caso.
La documentación utilizada para certificar el concepto y monto de las divisas imputado en
cada caso deberá quedar archivada en la entidad a disposición del BCRA. | **[abre la lista]** [intro 8.5.17] Por el valor que corresponda a ventajas aduaneras u otras situaciones previstas en el
siguiente listado de operaciones:
- texto propio: 8.5.17.11. Régimen de donación de órganos y sangre humana (Resolución 384/97
de la Administración Nacional de Aduanas).
- entidades de la unidad:
  - `e1` Operacion: Donación de órganos y sangre humana — Operación aduanera correspondiente al régimen de donación de órganos y sangre humana, exceptuada del seguimiento de permisos de embarque conforme a la Resolución 384/97 de la Administración Nacional d
  - `e2` Excepcion: Excepción seguimiento — donación órganos y sangre — Operación exceptuada del seguimiento de permisos de embarque por el valor que corresponda al régimen de donación de órganos y sangre humana, conforme a la Resolución 384/97 de la Administración Nacion
  - `e3` Comunicacion: Res. 384/97 — 
- relaciones del crudo (sin establecida_en ni de sujeto): to referencia e3
- NODOS A CLASIFICAR:
  - **caso 99** Excepcion `e2`: Excepción seguimiento — donación órganos y sangre | descripcion: Operación exceptuada del seguimiento de permisos de embarque por el valor que corresponda al régimen de donación de órganos y sangre humana, conforme a la Resolución 384/97 de la Administración Nacional de Aduanas. | tramo: Régimen de donación de órganos y sangre humana (Resolución 384/97 de la Administración Nacional de Aduanas)

## Unidad `ext::8.5.17.9` (item)
- herencia: [intro 8.5] La entidad podrá considerar cumplimentado parcial o totalmente el seguimiento de un permiso
de embarque cuando cuente con los elementos que le permitan considerar que la operación
se encuentra en alguna de las situaciones detalladas a continuación y se verifiquen las
condiciones previstas en cada caso.
La documentación utilizada para certificar el concepto y monto de las divisas imputado en
cada caso deberá quedar archivada en la entidad a disposición del BCRA. | **[abre la lista]** [intro 8.5.17] Por el valor que corresponda a ventajas aduaneras u otras situaciones previstas en el
siguiente listado de operaciones:
- texto propio: 8.5.17.9. Régimen de envíos de asistencia y salvamento (artículos 581 al 584 de la
Ley 22.415).
- entidades de la unidad:
  - `e1` Operacion: Régimen de envíos de asistencia y salvamento — Envíos de asistencia y salvamento regulados por los artículos 581 al 584 de la Ley 22.415, exceptuados del seguimiento de divisas por exportaciones de bienes
  - `e2` Excepcion: Excepción operaciones aduaneras — seguimiento — Operaciones de envíos de asistencia y salvamento quedan exceptuadas del seguimiento de divisas por exportaciones de bienes
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 100** Excepcion `e2`: Excepción operaciones aduaneras — seguimiento | descripcion: Operaciones de envíos de asistencia y salvamento quedan exceptuadas del seguimiento de divisas por exportaciones de bienes | tramo: Régimen de envíos de asistencia y salvamento (artículos 581 al 584 de la Ley 22.415)

## Unidad `ctacte::6.4.6.5` (item)
- herencia: **[abre la lista]** [encabezado 6.4.6] 6.4.6. No corresponderá la comunicación al BCRA de los rechazos motivados por:
- texto propio: 6.4.6.5. Haberse declarado judicialmente el concurso preventivo del librador y siempre
que se trate de cheques de pago diferido emitidos hasta el día anterior a la fecha
de presentación de la solicitud de apertura de ese proceso y su fecha de pago
sea posterior a ella.
Además, en los casos de los puntos 6.4.6.2. a 6.4.6.4. los rechazos no se comunicarán única-
mente en los casos en que hubiera sido posible atenderlos con el saldo existente en la cuenta
de no haberse efectivizado el pago, incurrido en el error o dispuesta la medida cautelar.
- entidades de la unidad:
  - `e1` Operacion: Comunicación al BCRA de rechazos de cheques — Comunicación al BCRA de los rechazos de cheques
  - `e2` Excepcion: Excepción — concurso preventivo del librador — No corresponde comunicar al BCRA los rechazos cuando se ha declarado judicialmente el concurso preventivo del librador, siempre que se trate de cheques de pago diferido emitidos hasta el día anterior 
  - `e3` Condicion: Condición — cheques de pago diferido — La excepción aplica únicamente cuando se trata de cheques de pago diferido
  - `e4` Excepcion: Excepción — saldo insuficiente en puntos 6.4.6.2 a 6.4.6.4 — Para los rechazos de los puntos 6.4.6.2 a 6.4.6.4, no se comunican al BCRA únicamente cuando hubiera sido posible atenderlos con el saldo existente en la cuenta de no haberse efectivizado el pago, inc
- relaciones del crudo (sin establecida_en ni de sujeto): e2 exceptua e1; e3 condicion_de e2
- NODOS A CLASIFICAR:
  - **caso 102** Excepcion `e4`: Excepción — saldo insuficiente en puntos 6.4.6.2 a 6.4.6.4 | descripcion: Para los rechazos de los puntos 6.4.6.2 a 6.4.6.4, no se comunican al BCRA únicamente cuando hubiera sido posible atenderlos con el saldo existente en la cuenta de no haberse efectivizado el pago, incurrido en el error o dispuesta la medida cautelar | tramo: en los casos de los puntos 6.4.6.2. a 6.4.6.4. los rechazos no se comunicarán únicamente en los casos en que hubiera sido posible atenderlos con el saldo existente en la cuenta de no haberse efectivizado el pago, incurrido en el error o dispuesta la medida cautelar

## Unidad `ext::13.6` (punto_no_item)
- herencia: [encabezado S13] Sección 13. Pagos de servicios prestados por no residentes.
- texto propio: 13.6. Líneas de crédito de entidades financieras aplicadas a la financiación de importaciones de
servicios.
La entidad financiera tendrá acceso al mercado de cambios, en las condiciones previstas en
el punto 3.15.1., para la cancelación de líneas de crédito del exterior aplicadas a la
financiación de importaciones argentinas de servicios en la medida que la misma califique
como deuda comercial según lo dispuesto en el segundo párrafo del punto 13.1.2. y la
entidad cuente la documentación que demuestre que, al momento del otorgamiento de la
financiación al importador, se cumplían las condiciones que resultaban aplicables en ese
momento al tipo de operación financiada por la entidad.
En el caso de las financiaciones otorgadas a partir del 13/12/23, la entidad deberá contar con
la documentación que demuestre que:
i) la operación financiada correspondía a una importación de servicios prestada o
devengada a partir del 13/12/23.
ii) la fecha de vencimiento de la financiación otorgada era compatible con los plazos
previstos en el punto 13.2.:
a) si el otorgamiento de la financiación es anterior de la fecha de prestación o
devengamiento del servicio, los plazos previstos en el punto 13.2. se computarán a
partir de la fecha estimada de prestación o devengamiento del servicio más 15
(quince) días corridos.
En caso de tratarse una operación del concepto “S30. Servicios de fletes por
operaciones de importaciones de bienes” que encuadra en lo previsto en el punto
10.10.2.1., deberá financiarse hasta la fecha estimada de embarque de los bienes
en origen más un plazo adicional de 15 (quince) días corridos.
b) si el otorgamiento de la financiación es posterior a la fecha de prestación o
devengamiento del servicio, los plazos previstos en el punto 13.2. se computarán
desde la última fec
- entidades de la unidad:
  - `e1` Operacion: Acceso al mercado de cambios para cancelación de líneas de crédito — Acceso al mercado de cambios para la cancelación de líneas de crédito del exterior aplicadas a la financiación de importaciones argentinas de servicios, en las condiciones previstas en el punto 3.15.1
  - `e2` Condicion: Calificación como deuda comercial según punto 13.1.2. — La línea de crédito debe calificar como deuda comercial según lo dispuesto en el segundo párrafo del punto 13.1.2.
  - `e3` Condicion: Documentación de cumplimiento de condiciones al otorgamiento — La entidad debe contar con documentación que demuestre que al momento del otorgamiento de la financiación al importador se cumplían las condiciones aplicables en ese momento al tipo de operación finan
  - `e4` Obligacion: Documentación de importación de servicios a partir de 13/12/23 — Para financiaciones otorgadas a partir del 13/12/23, la entidad deberá contar con documentación que demuestre que la operación financiada correspondía a una importación de servicios prestada o devenga
  - `e5` Obligacion: Compatibilidad de vencimiento con plazos punto 13.2. — La fecha de vencimiento de la financiación otorgada debe ser compatible con los plazos previstos en el punto 13.2.
  - `e6` Condicion: Otorgamiento anterior a prestación o devengamiento del servicio — Cuando el otorgamiento de la financiación es anterior a la fecha de prestación o devengamiento del servicio, los plazos previstos en el punto 13.2. se computarán a partir de la fecha estimada de prest
  - `e7` Excepcion: Excepción servicios de fletes importaciones de bienes — Para operaciones del concepto S30 (Servicios de fletes por operaciones de importaciones de bienes) que encuadran en el punto 10.10.2.1., la financiación debe extenderse hasta la fecha estimada de emba
  - `e8` Condicion: Otorgamiento posterior a prestación o devengamiento del servicio — Cuando el otorgamiento de la financiación es posterior a la fecha de prestación o devengamiento del servicio, los plazos previstos en el punto 13.2. se computarán desde la última fecha mencionada.
  - `e9` Restriccion: Sujeción a conformidad previa del BCRA por incumplimiento — Los casos que no cumplan las condiciones requeridas quedan sujetos a la conformidad previa del BCRA para acceder al mercado de cambios.
- relaciones del crudo (sin establecida_en ni de sujeto): e2 condicion_de e1; e3 condicion_de e1; e6 condicion_de e5; e8 condicion_de e5
- NODOS A CLASIFICAR:
  - **caso 104** Excepcion `e7`: Excepción servicios de fletes importaciones de bienes | descripcion: Para operaciones del concepto S30 (Servicios de fletes por operaciones de importaciones de bienes) que encuadran en el punto 10.10.2.1., la financiación debe extenderse hasta la fecha estimada de embarque de los bienes en origen más 15 días corridos. | tramo: En caso de tratarse una operación del concepto "S30. Servicios de fletes por operaciones de importaciones de bienes" que encuadra en lo previsto en el punto 10.10.2.1., deberá financiarse hasta la fecha estimada de embarque de los bienes en origen más un plazo adicional de 15 (quince) días corridos.

## Unidad `ext::7.1.1.3` (item)
- herencia: **[abre la lista]** [intro 7.1.1] El contravalor en divisas de la exportación hasta alcanzar el valor facturado según la
condición de venta pactada deberá ingresarse al país y liquidarse en el mercado de
cambios.
En el caso que el cliente sea un Vehículo de Proyecto Único (VPU) adherido al
Régimen de Incentivo para Grandes Inversiones (RIGI) que declaró ante la Autoridad
de Aplicación que preveía hacer uso de los beneficios establecidos en el artículo 198
de la Ley 27.742 en materia de cobro de exportaciones de bienes y servicio | [cierre 7.1.1] Independientemente de los plazos máximos precedentes, los cobros de exportaciones
deberán ser ingresados y liquidados en el mercado de cambios dentro de los 20
(veinte) días hábiles de la fecha de cobro. La posibilidad de utilizar este plazo quedará
supeditada en todos los casos al cumplimiento de los plazos previstos en los puntos
7.1.1.1. a 7.1.1.5.
Los montos en moneda extranjera originados en cobros de siniestros por coberturas
contratadas, en la medida que los mismos cubran el valor de los 
- texto propio: 7.1.1.3. 60 (sesenta) días corridos para las operaciones con contrapartes vinculadas
que no correspondan a los bienes indicados en los puntos 7.1.1.1. y 7.1.1.2.
y las exportaciones correspondientes a los capítulos 26 (excepto las
posiciones 2601.11.00, 2603.00.90, 2607.00.00, 2608.00.10, 2613.90.90,
2616.10.00, 2616.90.00 y 2621.10.00) y 71 (excepto las posiciones
7106.91.00, 7108.12.10 y 7112.99.00).
Los exportadores que realizaron operaciones con contrapartes vinculadas
que correspondan a bienes comprendidos en el punto 7.1.1.4., en las cuales
el importador sea una sociedad controlada por el exportador argentino,
podrán solicitar a la entidad encargada del seguimiento de la destinación que
extienda el plazo hasta:
i) el plazo previsto en dicho punto cuando el exportador no haya registrado
exportaciones por un valor total superior al equivalente a USD
50.000.000 (dólares estadounidenses cincuenta millones) en el año
calendario inmediato anterior a la oficialización de la destinación;
ii) un plazo de 120 (ciento veinte) días corridos cuando el exportador haya
superado el monto indicado en el punto precedente y los bienes
exportados correspondan a las posiciones que se detallan a
continuación:
0202.30.00.111D, 0202.30.00.115M, 0202.30.00.117R;
0202.30.00.118U, 0202.30.00.121G, 0202.30.00.124N,
0202.30.00.126T, 0202.30.00.131K, 0202.30.00.133P,
0202.30.00.136W, 0202.30.00.137Y, 0202.30.00.141N,
0202.30.00.142Q, 0202.30.00.146Z, 0202.30.00.147B,
0202.30.00.151R, 0202.30.00.943L, 0202.30.00.991Y,
0202.30.00.992A, 0202.30.00.995G, 0203.21.00.000J,
0206.29.90.300P, 0207.14.00.100K, 1901.90.20 (en envases inmediatos
de contenido neto inferior o igual a 1 kg) y 2204.21.00.
- entidades de la unidad:
  - `e1` Operacion: Ingreso y liquidación de divisas — exportaciones — Ingreso al país y liquidación en el mercado de cambios del contravalor en divisas de la exportación hasta alcanzar el valor facturado según la condición de venta pactada.
  - `e2` Obligacion: Plazo 60 días — operaciones contrapartes vinculadas — Ingreso y liquidación de divisas en plazo de 60 (sesenta) días corridos para operaciones con contrapartes vinculadas que no correspondan a los bienes de los puntos 7.1.1.1. y 7.1.1.2., y para exportac
  - `e3` Excepcion: Exclusión posiciones arancelarias — capítulo 26 — Quedan exceptuadas del plazo de 60 días las exportaciones de las posiciones arancelarias del capítulo 26 especificadas.
  - `e4` Excepcion: Exclusión posiciones arancelarias — capítulo 71 — Quedan exceptuadas del plazo de 60 días las exportaciones de las posiciones arancelarias del capítulo 71 especificadas.
  - `e5` Potestad: Solicitud extensión plazo — contrapartes vinculadas controladas — Facultad de los exportadores que realizaron operaciones con contrapartes vinculadas (bienes del punto 7.1.1.4., importador sociedad controlada por el exportador argentino) de solicitar a la entidad en
  - `e6` Condicion: Condición — exportaciones no superiores USD 50.000.000 — Supuesto en que el exportador no ha registrado exportaciones por valor total superior a USD 50.000.000 en el año calendario inmediato anterior a la oficialización de la destinación.
  - `e7` Obligacion: Plazo según punto 7.1.1.4. — extensión condicionada — Extensión del plazo hasta el previsto en el punto 7.1.1.4. cuando el exportador no haya registrado exportaciones por valor total superior a USD 50.000.000 en el año calendario inmediato anterior a la 
  - `e8` Condicion: Condición — exportaciones superiores USD 50.000.000 — Supuesto en que el exportador ha superado USD 50.000.000 en exportaciones y los bienes corresponden a las posiciones arancelarias especificadas.
  - `e9` Obligacion: Plazo 120 días — extensión condicionada — Extensión del plazo hasta 120 (ciento veinte) días corridos cuando el exportador ha superado USD 50.000.000 en exportaciones y los bienes corresponden a las posiciones arancelarias especificadas.
- relaciones del crudo (sin establecida_en ni de sujeto): e6 condicion_de e7; e8 condicion_de e9
- NODOS A CLASIFICAR:
  - **caso 106** Excepcion `e3`: Exclusión posiciones arancelarias — capítulo 26 | descripcion: Quedan exceptuadas del plazo de 60 días las exportaciones de las posiciones arancelarias del capítulo 26 especificadas. | tramo: excepto las posiciones 2601.11.00, 2603.00.90, 2607.00.00, 2608.00.10, 2613.90.90, 2616.10.00, 2616.90.00 y 2621.10.00
  - **caso 107** Excepcion `e4`: Exclusión posiciones arancelarias — capítulo 71 | descripcion: Quedan exceptuadas del plazo de 60 días las exportaciones de las posiciones arancelarias del capítulo 71 especificadas. | tramo: excepto las posiciones 7106.91.00, 7108.12.10 y 7112.99.00

## Unidad `ext::8.5.17.18` (item)
- herencia: [intro 8.5] La entidad podrá considerar cumplimentado parcial o totalmente el seguimiento de un permiso
de embarque cuando cuente con los elementos que le permitan considerar que la operación
se encuentra en alguna de las situaciones detalladas a continuación y se verifiquen las
condiciones previstas en cada caso.
La documentación utilizada para certificar el concepto y monto de las divisas imputado en
cada caso deberá quedar archivada en la entidad a disposición del BCRA. | **[abre la lista]** [intro 8.5.17] Por el valor que corresponda a ventajas aduaneras u otras situaciones previstas en el
siguiente listado de operaciones:
- texto propio: 8.5.17.18. Exportación a consumo de bienes que se encuentran excluidos del
Régimen de Equipaje –art. 59 inc. B) del Decreto 1.001/82–: son aquellos
bienes (por ejemplo: automotores, motocicletas, motores dentro o fuera
de borda, aeronaves, embarcaciones, etc.) que un residente del país
exporta con motivo de su radicación en el exterior.
- entidades de la unidad:
  - `e1` Definicion: Exportación a consumo — bienes excluidos Equipaje — Bienes tales como automotores, motocicletas, motores dentro o fuera de borda, aeronaves, embarcaciones, etc., que un residente del país exporta con motivo de su radicación en el exterior, excluidos de
  - `e2` Operacion: Exportación a consumo — bienes excluidos Equipaje — Exportación de bienes excluidos del Régimen de Equipaje (automotores, motocicletas, motores, aeronaves, embarcaciones, etc.) realizada por un residente del país con motivo de su radicación en el exter
  - `e3` Excepcion: Excepción — operaciones aduaneras exceptuadas seguimiento — Quedan exceptuadas del seguimiento las exportaciones a consumo de bienes excluidos del Régimen de Equipaje, por el valor que corresponda a ventajas aduaneras u otras situaciones previstas.
- relaciones del crudo (sin establecida_en ni de sujeto): ninguna
- NODOS A CLASIFICAR:
  - **caso 108** Excepcion `e3`: Excepción — operaciones aduaneras exceptuadas seguimiento | descripcion: Quedan exceptuadas del seguimiento las exportaciones a consumo de bienes excluidos del Régimen de Equipaje, por el valor que corresponda a ventajas aduaneras u otras situaciones previstas. | tramo: Exportación a consumo de bienes que se encuentran excluidos del Régimen de Equipaje

## Unidad `cla::6.5.3.2` (item)
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
- texto propio: 6.5.3.2. Incurra en atrasos de hasta 180 días, con exclusión de los deudores comprendi-
dos en el punto 6.5.2.2. A este fin, el cómputo de los plazos no se interrumpirá
por el otorgamiento de renovaciones cuando previamente no se haya producido
la cancelación efectiva de las obligaciones vencidas, es decir sin recurrir a finan-
ciación directa o indirecta de la entidad.
- entidades de la unidad:
  - `e1` Condicion: Atrasos hasta 180 días — El cliente incurre en atrasos de hasta 180 días como indicador de problemas para atender normalmente sus compromisos financieros.
  - `e2` Excepcion: Exclusión deudores punto 6.5.2.2 — Quedan exceptuados de esta condición los deudores comprendidos en el punto 6.5.2.2.
  - `e3` Obligacion: Cómputo de plazos sin interrupción por renovaciones — El cómputo de los plazos de atrasos no se interrumpirá por el otorgamiento de renovaciones cuando previamente no se haya producido la cancelación efectiva de las obligaciones vencidas, es decir sin re
  - `e4` Condicion: Cancelación sin financiación directa o indirecta — La cancelación efectiva de las obligaciones vencidas debe realizarse sin recurrir a financiación directa o indirecta de la entidad.
- relaciones del crudo (sin establecida_en ni de sujeto): e4 condicion_de e3
- NODOS A CLASIFICAR:
  - **caso 109** Excepcion `e2`: Exclusión deudores punto 6.5.2.2 | descripcion: Quedan exceptuados de esta condición los deudores comprendidos en el punto 6.5.2.2. | tramo: con exclusión de los deudores comprendidos en el punto 6.5.2.2
  - **caso 142** Condicion `e1`: Atrasos hasta 180 días | descripcion: El cliente incurre en atrasos de hasta 180 días como indicador de problemas para atender normalmente sus compromisos financieros. | tramo: Incurra en atrasos de hasta 180 días

## Unidad `ext::2.2.2.3` (item)
- herencia: **[abre la lista]** [intro 2.2.2] servicios que ingresen en los plazos normativos previstos y encuadren en las
siguientes situaciones:
- texto propio: 2.2.2.3. Se trata de cobros de exportaciones de servicios que correspondan a las
siguientes operaciones asociadas al turismo internacional en el país:
i) los cobros por consumos en el país efectuados por no residentes
mediante tarjetas de débito, crédito, compra o prepagas emitidas en el
exterior.
ii) los cobros por consumos en el país efectuados por no residentes
mediante billeteras electrónicas o cualquier otra modalidad de pago que
implique un débito inmediato en una cuenta en una entidad financiera en
el exterior o en una cuenta virtual en una empresa en el exterior.
En el caso de que la modalidad por la cual se canaliza el consumo
contemple la posibilidad de utilizar cuentas virtuales, quien ingresa los
fondos deberá demostrar que el mecanismo de pago utilizado prevé que
tales cuentas se encuentren abiertas en instituciones cuya operatoria
esté autorizada por la autoridad monetaria o equivalente de su país de
radicación y que la tenencia de una clave fiscal de ese país es condición
para la apertura de la cuenta.
iii) los cobros por cualquier tipo de servicio turístico en el país contratado
por no residentes, incluyendo aquellos servicios contratados a través de
agencias mayoristas y/o minoristas de viajes y turismo del país.
iv)los cobros por servicios de transporte de pasajeros no residentes con
destino en el país por vía terrestre, aérea o acuática.
A los efectos del registro de estas operaciones se deberán confeccionar dos
boletos sin movimiento de pesos, el boleto de compra se realizará por el
concepto de servicios al que corresponda el ingreso y el boleto de venta bajo
el concepto “A10. Débito/crédito de moneda extranjera en cuentas locales
por transferencias con el exterior”.
- entidades de la unidad:
  - `e1` Operacion: Cobros exportaciones servicios turismo internacional — Cobros de exportaciones de servicios que correspondan a operaciones asociadas al turismo internacional en el país, incluyendo: consumos en el país efectuados por no residentes mediante tarjetas de déb
  - `e2` Operacion: Cobros consumos tarjetas no residentes — Cobros por consumos en el país efectuados por no residentes mediante tarjetas de débito, crédito, compra o prepagas emitidas en el exterior.
  - `e3` Operacion: Cobros consumos billeteras electrónicas no residentes — Cobros por consumos en el país efectuados por no residentes mediante billeteras electrónicas o cualquier otra modalidad de pago que implique un débito inmediato en una cuenta en una entidad financiera
  - `e4` Condicion: Cuentas virtuales autorizadas por autoridad monetaria — Cuando la modalidad de pago contemple la posibilidad de utilizar cuentas virtuales, estas deben estar abiertas en instituciones cuya operatoria esté autorizada por la autoridad monetaria o equivalente
  - `e5` Obligacion: Demostración requisitos cuentas virtuales — Quien ingresa los fondos deberá demostrar que el mecanismo de pago utilizado prevé que las cuentas virtuales se encuentren abiertas en instituciones cuya operatoria esté autorizada por la autoridad mo
  - `e6` Operacion: Cobros servicios turísticos no residentes — Cobros por cualquier tipo de servicio turístico en el país contratado por no residentes, incluyendo aquellos servicios contratados a través de agencias mayoristas y/o minoristas de viajes y turismo de
  - `e7` Operacion: Cobros transporte pasajeros no residentes — Cobros por servicios de transporte de pasajeros no residentes con destino en el país por vía terrestre, aérea o acuática.
  - `e8` Obligacion: Confección boletos sin movimiento de pesos — A los efectos del registro de estas operaciones se deberán confeccionar dos boletos sin movimiento de pesos: el boleto de compra se realizará por el concepto de servicios al que corresponda el ingreso
  - `e9` Excepcion: Excepción obligación liquidación cobros exportaciones servicios — Quedan exceptuados de la obligación de liquidación los cobros de exportaciones de servicios que ingresen en los plazos normativos previstos y encuadren en las situaciones descritas en este punto.
- relaciones del crudo (sin establecida_en ni de sujeto): e4 condicion_de e5; e8 regula e1
- NODOS A CLASIFICAR:
  - **caso 110** Excepcion `e9`: Excepción obligación liquidación cobros exportaciones servicios | descripcion: Quedan exceptuados de la obligación de liquidación los cobros de exportaciones de servicios que ingresen en los plazos normativos previstos y encuadren en las situaciones descritas en este punto. | tramo: Quedarán exceptuados de la obligación de liquidación los cobros de exportaciones de servicios que ingresen en los plazos normativos previstos y encuadren en las siguientes situaciones

## Unidad `ext::2.2.2.2` (item)
- herencia: **[abre la lista]** [intro 2.2.2] servicios que ingresen en los plazos normativos previstos y encuadren en las
siguientes situaciones:
- texto propio: 2.2.2.2. Se trata de cobros de exportaciones de servicios prestados por personas
jurídicas que sean beneficiarias del Régimen de fomento para las
exportaciones de la economía del conocimiento (Capítulo II del Decreto
679/22) y se cumplen la totalidad de las siguientes condiciones:
i) las operaciones corresponden a los códigos de concepto enunciados en
el punto 2.2.2.1.i).
La entidad interviniente deberá adicionalmente contar con una
declaración jurada del cliente en la que conste que los cobros que dejan
de liquidarse corresponden a exportaciones de servicios que están
relacionadas con actividades vinculadas a la economía del
conocimiento.
ii) el cliente cuente por el equivalente del monto que se pretende no
liquidar con una “Certificación de incremento de exportaciones
asociadas a la economía del conocimiento (Decreto 679/22)” emitida en
los términos previstos en el punto 2.6.2.
iii) los fondos en moneda extranjera deberán ser acreditados en una
“Cuenta especial para el régimen de fomento de la economía del
conocimiento. Decreto 679/22” de titularidad del cliente hasta que sean
destinados al pago en moneda extranjera de las remuneraciones de
personal en relación de dependencia, debidamente registrado, afectado
a las actividades de la economía del conocimiento, conforme los
criterios establecidos en el Decreto 679/22 y la Resolución 234/22 del
Ministerio de Economía.
A los efectos del registro de estas operaciones se deberán confeccionar dos
boletos sin movimiento de pesos, el boleto de compra se realizará por el
concepto de servicios que corresponda y el boleto de venta deberá
registrarse bajo el código de concepto “A22. Acreditación de cobros de
exportaciones de bienes y servicios”.
- entidades de la unidad:
  - `e1` Excepcion: Excepción liquidación — cobros servicios economía conocimiento — Quedan exceptuados de la obligación de liquidación los cobros de exportaciones de servicios prestados por personas jurídicas beneficiarias del Régimen de fomento para las exportaciones de la economía 
  - `c1` Condicion: Códigos de concepto — punto 2.2.2.1.i) — Las operaciones deben corresponder a los códigos de concepto enunciados en el punto 2.2.2.1.i).
  - `o1` Obligacion: Declaración jurada cliente — cobros servicios economía conocimiento — La entidad interviniente debe contar con una declaración jurada del cliente en la que conste que los cobros que dejan de liquidarse corresponden a exportaciones de servicios relacionadas con actividad
  - `c2` Condicion: Certificación incremento exportaciones — Decreto 679/22 — El cliente debe contar, por el equivalente del monto que se pretende no liquidar, con una Certificación de incremento de exportaciones asociadas a la economía del conocimiento (Decreto 679/22) emitida
  - `c3` Condicion: Acreditación fondos — Cuenta especial economía conocimiento — Los fondos en moneda extranjera deben ser acreditados en una Cuenta especial para el régimen de fomento de la economía del conocimiento (Decreto 679/22) de titularidad del cliente, hasta que sean dest
  - `o2` Obligacion: Confección boletos — registro operaciones servicios economía conocimiento — Para el registro de estas operaciones se deben confeccionar dos boletos sin movimiento de pesos: el boleto de compra por el concepto de servicios que corresponda y el boleto de venta registrado bajo e
  - `com1` Comunicacion: Decreto 679/22 — 
  - `com2` Comunicacion: Resolución 234/22 Ministerio de Economía — 
- relaciones del crudo (sin establecida_en ni de sujeto): c1 condicion_de e1; c2 condicion_de e1; c3 condicion_de e1
- NODOS A CLASIFICAR:
  - **caso 111** Excepcion `e1`: Excepción liquidación — cobros servicios economía conocimiento | descripcion: Quedan exceptuados de la obligación de liquidación los cobros de exportaciones de servicios prestados por personas jurídicas beneficiarias del Régimen de fomento para las exportaciones de la economía del conocimiento, cuando se cumplen la totalidad de las condiciones especificadas. | tramo: Quedarán exceptuados de la obligación de liquidación los cobros de exportaciones de servicios que ingresen en los plazos normativos previstos y encuadren en las siguientes situaciones: Se trata de cobros de exportaciones de servicios prestados por personas jurídicas que sean beneficiarias del Régimen de fomento para las exportaciones de la economía del conocimiento (Capítulo II del Decreto 679/22) y se cumplen la totalidad de las siguientes condiciones
