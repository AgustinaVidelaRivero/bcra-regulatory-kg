# Fichas pareadas de P4 (cegadas: sin grupo, estrato ni origen)

Orden: random.Random('U-PROMPT-R2:P4:2026-10-04:fichas').shuffle sobre los 76 ids ordenados. SELLADO = prefijo v3_b54 con la E0 legada; NUEVO = prefijo r2b `3817de475c93` con la e0-r2 (release contra release).

## Ficha 1 — `cap::8.6::intro`

**Texto propio:**

```
A los fines de todas las reglamentaciones vinculadas al capital, su integración y aumento, in-
clusive los referidos a planes de regularización y saneamiento y sin perjuicio de lo previsto en
los puntos 5.1. a 5.3. de las normas sobre “Autorización y composición del capital de entidades
financieras” en materia de negociación de acciones o de aportes irrevocables para futuros au-
mentos de capital, los aportes deben ser efectuados en efectivo.
Excepcionalmente, mediando autorización previa de la SEFyC, podrán admitirse aportes en:
```
**Último bloque heredado:** 8.6. Aportes de capital.

**SELLADO** — error: None

- Operacion «Aporte de capital en efectivo»: Aporte de capital efectuado en efectivo a fines de integración y aumento de capital, inclusive en planes de regularización y saneamiento
- Obligacion «Obligación de aportes en efectivo»: Los aportes deben ser efectuados en efectivo
- Restriccion «Restricción de aportes no en efectivo»: Se prohíben aportes en especie, salvo excepcionalmente con autorización previa de la SEFyC
- Excepcion «Excepción por autorización SEFyC»: Mediando autorización previa de la SEFyC, podrán admitirse aportes en especie
- Potestad «Autorización de aportes en especie SEFyC»: La SEFyC puede autorizar previamente aportes en especie
  - Obligacion:Obligación de aportes en efectivo --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Restriccion:Restricción de aportes no en efectivo --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Excepcion:Excepción por autorización SEFyC --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Potestad:Autorización de aportes en especie SEFyC --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Obligacion:Obligación de aportes en efectivo --regula--> Operacion:Aporte de capital en efectivo
  - Restriccion:Restricción de aportes no en efectivo --prohibe--> Operacion:Aporte de capital en efectivo
  - Excepcion:Excepción por autorización SEFyC --exceptua_obligacion--> Obligacion:Obligación de aportes en efectivo
  - Obligacion:Obligación de aportes en efectivo --aplica_a--> None
  - Restriccion:Restricción de aportes no en efectivo --aplica_a--> None
  - Potestad:Autorización de aportes en especie SEFyC --aplica_a--> None
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}]; omisiones []; condicion_de []; limita []

**NUEVO** — error: None

- Obligacion «Aportes de capital en efectivo»: Los aportes de capital deben ser efectuados en efectivo, en el marco de todas las reglamentaciones vinculadas al capital, su integración y aumento, inclusive los referidos a planes de regularización y saneamiento y sin perjuicio de lo previ… ‖ tramo (exacta): «los aportes deben ser efectuados en efectivo»
- Potestad «Admisión de aportes no-efectivo — autorización SEFyC»: La SEFyC tiene la facultad de autorizar, excepcionalmente, la admisión de aportes en formas distintas al efectivo. ‖ tramo (exacta): «mediando autorización previa de la SEFyC, podrán admitirse aportes en»
- Excepcion «Excepción a obligación de aportes en efectivo»: Se exceptúa de la obligación de efectuar aportes en efectivo cuando medie autorización previa de la SEFyC. ‖ tramo (exacta): «Excepcionalmente, mediando autorización previa de la SEFyC, podrán admitirse aportes en»
  - Obligacion:Aportes de capital en efectivo --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Potestad:Admisión de aportes no-efectivo — autorización SEFyC --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Excepcion:Excepción a obligación de aportes en efectivo --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Obligacion:Aportes de capital en efectivo --aplica_a--> las entidades
  - Potestad:Admisión de aportes no-efectivo — autorización SEFyC --aplica_a--> la SEFyC
  - Excepcion:Excepción a obligación de aportes en efectivo --exceptua_obligacion--> Obligacion:Aportes de capital en efectivo
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "las entidades", "verificada": "no", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "la SEFyC", "verificada": "exacta", "sujeto_id": null}]; omisiones [{"categoria": "fuera_de_tipos", "tramo": "podrán admitirse aportes en", "verificacion": "exacta", "nota": "Enumeración incompleta: el texto abre una enumeración de formas de aportes admisibles excepto en efe…"}]; condicion_de []; limita []

*Cuantías en el texto propio: 0.*

## Ficha 2 — `cap::4.3.3.2`

**Texto propio:**

```
4.3.3.2. Exposiciones a fondos de garantía constituidos para hacer frente a
incumplimientos.
Si un fondo de garantía constituido para hacer frente a incumplimientos
respalda a productos sujetos a riesgo de liquidación –tales como bonos y
acciones– y a productos expuestos a riesgo de crédito de contraparte
–tales como derivados OTC, derivados negociados en mercados de valo-
res, SFTs u operaciones de liquidación diferida–, todos los aportes a ese
fondo recibirán el ponderador de riesgo determinado según lo previsto en
este punto, no admitiendo el prorrateo entre las clases o tipo de negocios
y productos.
Si los aportes de los miembros compensadores a un fondo de garantía se
segregan por tipo de producto y sólo se pueden utilizar para tipos de pro-
ductos específicos, la exigencia de capital para esa exposición al fondo
de garantía para incumplimientos se determinará de acuerdo con las fór-
mulas y metodología indicada en este punto pero aplicada por separado
para cada producto sujeto a riesgo de crédito de contraparte.
Al efecto de computar la exigencia de capital por los aportes a fondos de
garantía para incumplimientos de una QCCP, las entidades financieras
que sean miembros compensadores aplicarán un ponderador de riesgo
que se determinará considerando i. la cantidad y calidad de los recursos
de la QCCP; ii. la exposición de dicha CCP al riesgo de crédito de contra-
parte y iii. el orden en que se aplican los recursos de la CCP –prioridad
en la asunción de pérdidas– en el caso de incumplir uno o varios miem-
bros compensadores, conforme a la secuencia de cálculo que se indica a
continuación:
i) Calcular el requerimiento de capital hipotético para la CCP por su ex-
posición al riesgo de crédito de contraparte (K ) frente a todos los
CCP
miembros compensadores y sus clientes mediante la siguiente fórmu-
la:
donde:
20 %: ponderador de riesgo.
EAD: es el valor de la exposición de la CCP con el miembro com-
i
pensador “i”, incluyendo tanto las operaciones propias del
miembro compensador como las de sus clientes garantizadas
por él, y todos los activos en garantía en poder de la CCP co-
mo consecuencia de esas operaciones –incluyendo los aportes
al fondo de garantía para incumplimientos–, todo a valores de
cierre del día de cálculo, antes de transferirse el margen reque-
rido en el último pedido de reposición de márgenes de ese día.
La suma comprende las cuentas de todos los miembros compensado-
res.
Cuando los miembros compensadores brinden servicios de compen-
sación a sus clientes y las operaciones y activos en garantía de los
clientes se mantengan en subcuentas –individuales o colectivas– se-
paradas de la operatoria propia del miembro compensador, cada sub-
cuenta correspondiente a los clientes también deberá sumarse; esto
es, la EAD calculada para el miembro compensador con la fórmula
anterior será la suma de las EAD de las subcuentas correspondientes
a sus clientes y de las correspondientes al propio miembro compen-
sador. Si alguna de las sub
```
**Último bloque heredado:** 4.3.3. Exposiciones a entidades de contraparte central calificadas.

**SELLADO** — error: None

- Operacion «Cálculo requerimiento capital hipotético CCP»: Calcular el requerimiento de capital hipotético para la CCP por su exposición al riesgo de crédito de contraparte frente a todos los miembros compensadores y sus clientes, aplicando un ponderador de riesgo del 20%.
- Operacion «Cálculo EAD derivados con SA-CCR»: Para derivados, calcular la EAD aplicando el enfoque SA-CCR como si se tratara de una exposición por operaciones bilaterales entre la CCP y el miembro compensador, empleando un MPOR de 10 días.
- Operacion «Cálculo EAD SFT»: Para SFT, calcular la EAD como el máximo entre: valor de la exposición antes de mitigar riesgo más variación de margen transferida, menos margen inicial, menos aporte a fondo de garantía, o cero.
- Operacion «Segregación aportes fondo garantía por tipo producto»: Cuando los aportes de miembros compensadores a un fondo de garantía se segregan por tipo de producto y solo se pueden usar para tipos específicos, la exigencia de capital se determina aplicando fórmulas y metodología por separado para cada …
- Operacion «Asignación aporte fondo garantía por subcuenta»: Cuando aportes al fondo de garantía de un miembro no están separados por subcuentas de clientes y miembro compensador, deberán ser asignados por subcuenta según la respectiva porción del margen inicial que cada subcuenta tenga en relación a…
- Operacion «Asignación margen inicial integrado a exposiciones»: Cuando activos se constituyan en garantía de una cuenta con operaciones SFT y derivados, el margen inicial debe ser asignado a exposiciones SFT y derivados en la proporción de sus respectivas EAD específicas.
- Obligacion «Aplicar ponderador riesgo QCCP»: Las entidades financieras que sean miembros compensadores aplicarán un ponderador de riesgo para computar la exigencia de capital por aportes a fondos de garantía para incumplimientos de una QCCP, considerando: (i) cantidad y calidad de rec…
- Obligacion «Aplicar períodos mantenimiento mínimo»: Se aplicarán períodos de mantenimiento mínimo de acuerdo con punto 5.3.2.3 para SFT y de 10 días hábiles para operaciones con derivados sujetas a reposición diaria de márgenes y valuación diaria a precios de mercado.
- Condicion «Período extendido para garantías ilíquidas»: Para conjuntos de neteo con una o más operaciones con activos en garantía ilíquidos o derivados OTC que no puedan sustituirse fácilmente, el período mínimo será de 20 días hábiles.
- Condicion «Período extendido por concentración contraparte»: El período mínimo se extenderá si operaciones o activos recibidos en garantía se concentran en una contraparte determinada, particularmente si no pudieran ser reemplazados si dicha contraparte saliera de forma precipitada del mercado.
- Restriccion «No aplica extensión período por cantidad operaciones»: La sola existencia de 5.000 operaciones o más en un conjunto de neteo no determinará, por sí misma, la extensión del período de mantenimiento mínimo.
- Obligacion «Calcular K_CCP con periodicidad trimestral»: El cálculo de K_CCP deberá hacerse como mínimo con periodicidad trimestral.
- Obligacion «Proveer información composición exposiciones CCP»: Las entidades financieras deberán asegurarse de que la composición de las exposiciones de las CCP frente a los miembros compensadores y toda otra información proporcionada para el cálculo del K_CCP, DF_pref_CM y DF_CCP esté a disposición de…
- Obligacion «CCP calcular K_CCP y proveer información»: La CCP, la entidad financiera, la autoridad de control de la CCP u otro organismo con acceso a datos requeridos deberá calcular K_CCP, DF_pref_CM y DF_CCP de forma tal que la autoridad de control de la CCP pueda comprobarlos y proveer infor…
- Restriccion «Límite requisito capital vs punto 4.3.4»: Cuando la suma de los requisitos de capital de una entidad financiera por exposiciones con una QCCP sea mayor que la exigencia que resultaría de la aplicación del punto 4.3.4., se tomará este último importe como requisito de capital.
- Restriccion «No admite prorrateo entre clases de productos»: Si un fondo de garantía respalda productos sujetos a riesgo de liquidación y productos expuestos a riesgo de crédito de contraparte, todos los aportes recibirán el ponderador de riesgo correspondiente, no admitiendo prorrateo entre las clas…
- Obligacion «Aplicar conjuntos neteo establecidos»: Los conjuntos de neteo aplicables a las entidades financieras que actúen como miembros compensadores serán los referidos en el inciso c) del acápite i) del punto 4.3.3.1. Los demás miembros compensadores deberán observar las normas de neteo…
  - Operacion:Cálculo requerimiento capital hipotético CCP --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Operacion:Cálculo EAD derivados con SA-CCR --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Operacion:Cálculo EAD SFT --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Operacion:Segregación aportes fondo garantía por tipo producto --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Operacion:Asignación aporte fondo garantía por subcuenta --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Operacion:Asignación margen inicial integrado a exposiciones --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Obligacion:Aplicar ponderador riesgo QCCP --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Obligacion:Aplicar períodos mantenimiento mínimo --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Condicion:Período extendido para garantías ilíquidas --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Condicion:Período extendido por concentración contraparte --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Restriccion:No aplica extensión período por cantidad operaciones --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Obligacion:Calcular K_CCP con periodicidad trimestral --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Obligacion:Proveer información composición exposiciones CCP --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Obligacion:CCP calcular K_CCP y proveer información --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Restriccion:Límite requisito capital vs punto 4.3.4 --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Restriccion:No admite prorrateo entre clases de productos --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Obligacion:Aplicar conjuntos neteo establecidos --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Obligacion:Aplicar ponderador riesgo QCCP --aplica_a--> None
  - Obligacion:Aplicar períodos mantenimiento mínimo --aplica_a--> None
  - Obligacion:Proveer información composición exposiciones CCP --aplica_a--> None
  - Obligacion:Aplicar conjuntos neteo establecidos --aplica_a--> None
  - Obligacion:Aplicar ponderador riesgo QCCP --regula--> Operacion:Cálculo requerimiento capital hipotético CCP
  - Obligacion:Aplicar períodos mantenimiento mínimo --regula--> Operacion:Cálculo EAD derivados con SA-CCR
  - Obligacion:Aplicar períodos mantenimiento mínimo --regula--> Operacion:Cálculo EAD SFT
  - Obligacion:Calcular K_CCP con periodicidad trimestral --regula--> Operacion:Cálculo requerimiento capital hipotético CCP
  - Restriccion:Límite requisito capital vs punto 4.3.4 --limita--> Operacion:Cálculo requerimiento capital hipotético CCP
  - Restriccion:No admite prorrateo entre clases de productos --prohibe--> Operacion:Segregación aportes fondo garantía por tipo producto
  - rechazo: firma_invalida: relations[27]: Condicion --condiciona--> Obligacion
  - rechazo: firma_invalida: relations[28]: Condicion --condiciona--> Obligacion
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}]; omisiones [{"categoria": null, "tramo": "", "verificacion": "ausente", "nota": "Fórmula de K_CCP con detalles de componentes EAD, ponderadores y sumas: estructura matemática no con…"}, {"categoria": null, "tramo": "", "verificacion": "ausente", "nota": "Fórmula de K_CMi (requerimiento capital por aporte al fondo de garantía por miembro): estructura mat…"}, {"categoria": null, "tramo": "", "verificacion": "ausente", "nota": "Fórmula de EAD para SFT: estructura con variables específicas no confiable en valores extraídos del …"}, {"categoria": null, "tramo": "", "verificacion": "ausente", "nota": "Tabla de aforos aplicables a SFT referenciada al punto 5.3.2.3: contenido tabular no reconstruible d…"}, {"categoria": null, "tramo": "", "verificacion": "ausente", "nota": "Valores numéricos específicos de ponderadores, umbrales y parámetros técnicos cuando forman parte de…"}]; condicion_de []; limita [{"de": "Restriccion:Límite requisito capital vs punto 4.3.4", "a": "Operacion:Cálculo requerimiento capital hipotético CCP"}]

**NUEVO** — error: None

- Operacion «Aporte a fondo de garantía para incumplimientos»: Aporte a fondo de garantía constituido para hacer frente a incumplimientos que respalda productos de riesgo de liquidación y de riesgo de crédito de contraparte ‖ tramo (exacta): «aportes a ese fondo»
- Restriccion «No prorrateo entre clases de negocios — aporte a fondo»: Cuando un fondo de garantía respalda tanto productos de riesgo de liquidación como productos de riesgo de crédito de contraparte, todos los aportes reciben el mismo ponderador sin prorrateo entre clases o tipos de negocios ‖ tramo (exacta): «todos los aportes a ese fondo recibirán el ponderador de riesgo determinado según lo previsto en este punto, no admitiendo el prorrateo entre las clases o tipo …»
- Condicion «Fondo respalda productos de liquidación y crédito»: El fondo respalda simultáneamente productos de riesgo de liquidación y productos de riesgo de crédito de contraparte ‖ tramo (exacta): «Si un fondo de garantía constituido para hacer frente a incumplimientos respalda a productos sujetos a riesgo de liquidación –tales como bonos y acciones– y a p…»
- Operacion «Segregación de aportes por tipo de producto»: Aportes de miembros compensadores segregados por tipo de producto con uso limitado a tipos específicos ‖ tramo (exacta): «aportes de los miembros compensadores a un fondo de garantía se segregan por tipo de producto»
- Obligacion «Aplicar exigencia por separado — aportes segregados»: Cuando los aportes están segregados por tipo de producto, la exigencia de capital se determina aplicando fórmulas por separado para cada producto sujeto a riesgo de crédito de contraparte ‖ tramo (exacta): «la exigencia de capital para esa exposición al fondo de garantía para incumplimientos se determinará de acuerdo con las fórmulas y metodología indicada en este …»
- Condicion «Aportes segregados por producto — uso específico»: Los aportes están segregados por tipo de producto y se pueden utilizar únicamente para tipos específicos ‖ tramo (exacta): «Si los aportes de los miembros compensadores a un fondo de garantía se segregan por tipo de producto y sólo se pueden utilizar para tipos de productos específic…»
- Obligacion «Aplicar ponderador de riesgo — miembros QCCP»: Las entidades financieras que sean miembros compensadores deben aplicar un ponderador de riesgo para aportes a fondos de garantía de QCCP, considerando: cantidad y calidad de recursos, exposición al riesgo de crédito de contraparte, y orden… ‖ tramo (exacta): «las entidades financieras que sean miembros compensadores aplicarán un ponderador de riesgo que se determinará considerando i. la cantidad y calidad de los recu…»
- Operacion «Cálculo del requerimiento de capital hipotético de CCP»: Cálculo del requerimiento de capital hipotético para la CCP por exposición al riesgo de crédito de contraparte frente a todos los miembros compensadores ‖ tramo (no): «Calcular el requerimiento de capital hipotético para la CCP por su exposición al riesgo de crédito de contraparte (K ) frente a todos los miembros compensadores»
- Operacion «Cálculo del requisito de capital por miembro compensador»: Cálculo del requisito de capital para cada miembro compensador por su aporte al fondo de garantía ‖ tramo (exacta): «Calcular el requisito de capital para cada miembro compensador»
- Potestad «CCP puede realizar cómputo de capital»: La CCP, la entidad financiera o cualquier otro organismo con acceso a datos puede realizar el cómputo del requerimiento de capital ‖ tramo (no): «El cómputo de este requerimiento de capital podrá realizarlo la CCP, la entidad financiera o cualquier otro organismo con acceso a los datos requeridos»
- Obligacion «Calcular K_CCP, DF_pref, DF_CCP verificables»: La CCP, entidad financiera, autoridad de control o institución con acceso a datos debe calcular K_CCP, DF_pref y DF_CCP de forma verificable por la autoridad de control ‖ tramo (no): «calcular K , DF pref y DF de forma tal que la autoridad de control de la CCP pueda comprobarlos»
- Obligacion «Proveer información para cálculo de capital»: Proveer información que permita al miembro compensador calcular la exigencia de capital y a la SEFyC revisar esos cálculos ‖ tramo (exacta): «proveer información que permita al miembro compensador calcular la exigencia de capital por su aporte al fondo de garantía constituido para hacer frente a incum…»
- Obligacion «Calcular K_CCP con periodicidad trimestral»:  ‖ tramo (tokens): «El cálculo de K deberá hacerse como mínimo con periodicidad CCP trimestral»
- Obligacion «Asegurar disponibilidad de información trimestral»: Las entidades financieras deben asegurar que información sobre composición de exposiciones de CCP y datos para cálculos esté disponible para la SEFyC ‖ tramo (no): «Las entidades financieras deberán asegurarse de que la composición de las exposiciones de las CCP frente a los miembros compensadores y toda otra información qu…»
- Restriccion «Límite al requisito de capital respecto de QCCP»: Límite máximo al requisito de capital por exposiciones con una QCCP: el menor entre el calculado y el requerido en punto 4.3.4 ‖ tramo (exacta): «cuando la suma de los requisitos de capital de una entidad financiera por las exposiciones con una QCCP originadas en las operaciones y aportes realizados al fo…»
  - Operacion:Aporte a fondo de garantía para incumplimientos --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Restriccion:No prorrateo entre clases de negocios — aporte a fondo --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Condicion:Fondo respalda productos de liquidación y crédito --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Condicion:Fondo respalda productos de liquidación y crédito --condicion_de--> Restriccion:No prorrateo entre clases de negocios — aporte a fondo
  - Operacion:Segregación de aportes por tipo de producto --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Condicion:Aportes segregados por producto — uso específico --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Obligacion:Aplicar exigencia por separado — aportes segregados --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Condicion:Aportes segregados por producto — uso específico --condicion_de--> Obligacion:Aplicar exigencia por separado — aportes segregados
  - Obligacion:Aplicar exigencia por separado — aportes segregados --regula--> Operacion:Segregación de aportes por tipo de producto
  - Obligacion:Aplicar ponderador de riesgo — miembros QCCP --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Obligacion:Aplicar ponderador de riesgo — miembros QCCP --aplica_a--> las entidades financieras que sean miembros compensadores
  - Obligacion:Aplicar ponderador de riesgo — miembros QCCP --regula--> Operacion:Aporte a fondo de garantía para incumplimientos
  - Operacion:Cálculo del requerimiento de capital hipotético de CCP --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Operacion:Cálculo del requerimiento de capital hipotético de CCP --requiere--> Obligacion:Calcular K_CCP, DF_pref, DF_CCP verificables
  - Operacion:Cálculo del requisito de capital por miembro compensador --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Potestad:CCP puede realizar cómputo de capital --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Potestad:CCP puede realizar cómputo de capital --aplica_a--> la CCP, la entidad financiera o cualquier otro organismo con acceso a los datos requeridos
  - Obligacion:Calcular K_CCP, DF_pref, DF_CCP verificables --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Obligacion:Calcular K_CCP, DF_pref, DF_CCP verificables --aplica_a--> la CCP, la entidad financiera, la autoridad de control de la CCP u otro organismo con acceso a los datos requeridos
  - Obligacion:Proveer información para cálculo de capital --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Obligacion:Proveer información para cálculo de capital --aplica_a--> la CCP, la entidad financiera, la autoridad de control de la CCP u otro organismo con acceso a los datos requeridos
  - Obligacion:Calcular K_CCP con periodicidad trimestral --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Obligacion:Calcular K_CCP con periodicidad trimestral --aplica_a--> la CCP, la entidad financiera, la autoridad de control de la CCP u otro organismo con acceso a los datos requeridos
  - Obligacion:Calcular K_CCP con periodicidad trimestral --condiciona--> Operacion:Cálculo del requisito de capital por miembro compensador
  - Obligacion:Asegurar disponibilidad de información trimestral --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Obligacion:Asegurar disponibilidad de información trimestral --aplica_a--> Las entidades financieras
  - Restriccion:Límite al requisito de capital respecto de QCCP --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Restriccion:Límite al requisito de capital respecto de QCCP --aplica_a--> una entidad financiera
  - Restriccion:Límite al requisito de capital respecto de QCCP --limita--> Operacion:Cálculo del requisito de capital por miembro compensador
  - rechazo: firma_invalida: relations[17]: Potestad --regula--> Operacion
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "las entidades financieras que sean miembros compensadores", "verificada": "exacta", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "la CCP, la entidad financiera o cualquier otro organismo con acceso a los datos …", "verificada": "no", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "la CCP, la entidad financiera, la autoridad de control de la CCP u otro organism…", "verificada": "exacta", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "la CCP, la entidad financiera, la autoridad de control de la CCP u otro organism…", "verificada": "exacta", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "la CCP, la entidad financiera, la autoridad de control de la CCP u otro organism…", "verificada": "exacta", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "Las entidades financieras", "verificada": "exacta", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "una entidad financiera", "verificada": "exacta", "sujeto_id": null}]; omisiones [{"categoria": "tabla", "tramo": "K = EAD × 20% con fórmula de suma de exposiciones por miembros compensadores", "verificacion": "no", "nota": "Fórmula con variables (K_CCP, EAD_i, 20%) declarada NO-CONFIABLE por FLAGS E0; contenido tabular det…"}, {"categoria": "tabla", "tramo": "EAD calculada para miembros compensadores incluyendo operaciones propias y clientes con subcuentas i…", "verificacion": "no", "nota": "Especificaciones de cálculo de EAD con detalles de subcuentas y asignación de márgenes declaradas NO…"}, {"categoria": "tabla", "tramo": "Para SFT: EAD = máx. (EBRM_i - IM_i - DF_i; 0)", "verificacion": "no", "nota": "Fórmula específica para SFT con variables (EBRM, IM, DF) declarada NO-CONFIABLE"}, {"categoria": "tabla", "tramo": "K_CMi = (EAD_i - min(DF_i, DF_pref_CM)) × (DF_pref_CM - DF_CCP) / (DF_pref_CM - DF_CCP) × 2%", "verificacion": "no", "nota": "Fórmula compleja para cálculo de requisito de capital por miembro compensador con múltiples variable…"}, {"categoria": "tabla", "tramo": "Períodos de mantenimiento mínimo: 10 días hábiles para derivados con reposición diaria; 20 días hábi…", "verificacion": "no", "nota": "Especificaciones de períodos y condiciones declaradas NO-CONFIABLES; solo se extrajeron las obligaci…"}, {"categoria": "tabla", "tramo": "Conjuntos de neteo aplicables a entidades financieras como miembros compensadores según punto 4.3.3.…", "verificacion": "no", "nota": "Regla de selección de conjuntos de neteo con remisión a otras normas y condiciones de aplicación; co…"}, {"categoria": "meta_normativo", "tramo": "Definiciones de términos: K_CCP (requerimiento de capital hipotético de CCP), DF_pref_CM (total de a…", "verificacion": "no", "nota": "Cláusulas definitoria de variables de fórmulas; contenido meta-normativo (predicación sobre alcance …"}]; condicion_de [{"de": "Condicion:Fondo respalda productos de liquidación y crédito", "a": "Restriccion:No prorrateo entre clases de negocios — aporte a fondo", "firma_nueva": false}, {"de": "Condicion:Aportes segregados por producto — uso específico", "a": "Obligacion:Aplicar exigencia por separado — aportes segregados", "firma_nueva": false}]; limita [{"de": "Restriccion:Límite al requisito de capital respecto de QCCP", "a": "Operacion:Cálculo del requisito de capital por miembro compensador"}]

*Cuantías en el texto propio: 6.*

## Ficha 3 — `adrei::S5`

**Texto propio:**

```
Sección 5. Supervisión por parte de la Superintendencia de Entidades Financieras y Cambiarias.
La Superintendencia de Entidades Financieras y Cambiarias examinará y evaluará periódicamente
el cumplimiento por parte de las entidades financieras de estas disposiciones, para lo cual deberá
tener acceso a todos los documentos pertinentes –tales como informes de auditoría y validación
interna–.
Asimismo, podrá exigir a las entidades financieras no sólo la adopción de medidas correctivas efica-
ces y oportunas cuando detecte deficiencias en sus capacidades de agregación de datos sobre
riesgos, sus prácticas de elaboración de informes de riesgos o sus controles internos, sino también
la implementación de límites más restrictivos a los riesgos o al crecimiento de sus actividades.
Además, podrá intensificar la supervisión y requerir capital adicional de acuerdo con lo establecido
en las normas sobre “Lineamientos para la gestión de riesgos en las entidades financieras”, entre
otras medidas.
Previo a que esta Institución otorgue autorización a las entidades financieras para que inicien un
nuevo negocio o una adquisición, la Superintendencia de Entidades Financieras y Cambiarias podrá
exigir que sus planes de sistemas garanticen que será posible una sólida agregación de datos sobre
riesgos.
```
**Último bloque heredado:** 

**SELLADO** — error: None

- Obligacion «Examen periódico cumplimiento normas»: La Superintendencia de Entidades Financieras y Cambiarias examinará y evaluará periódicamente el cumplimiento por parte de las entidades financieras de estas disposiciones
- Obligacion «Acceso a documentos pertinentes»: la Superintendencia deberá tener acceso a todos los documentos pertinentes –tales como informes de auditoría y validación interna–
- Potestad «Exigir medidas correctivas deficiencias»: podrá exigir a las entidades financieras la adopción de medidas correctivas eficaces y oportunas cuando detecte deficiencias en sus capacidades de agregación de datos sobre riesgos, sus prácticas de elaboración de informes de riesgos o sus …
- Potestad «Implementar límites riesgos restricción»: podrá exigir la implementación de límites más restrictivos a los riesgos o al crecimiento de sus actividades
- Potestad «Intensificar supervisión capital adicional»: podrá intensificar la supervisión y requerir capital adicional de acuerdo con lo establecido en las normas sobre 'Lineamientos para la gestión de riesgos en las entidades financieras'
- Obligacion «Garantizar agregación datos riesgos planes»: Previo a que esta Institución otorgue autorización a las entidades financieras para que inicien un nuevo negocio o una adquisición, la Superintendencia de Entidades Financieras y Cambiarias podrá exigir que sus planes de sistemas garanticen…
  - Obligacion:Examen periódico cumplimiento normas --establecida_en--> TextoOrdenado:Agregación de datos sobre riesgos: D-SIB
  - Obligacion:Acceso a documentos pertinentes --establecida_en--> TextoOrdenado:Agregación de datos sobre riesgos: D-SIB
  - Potestad:Exigir medidas correctivas deficiencias --establecida_en--> TextoOrdenado:Agregación de datos sobre riesgos: D-SIB
  - Potestad:Implementar límites riesgos restricción --establecida_en--> TextoOrdenado:Agregación de datos sobre riesgos: D-SIB
  - Potestad:Intensificar supervisión capital adicional --establecida_en--> TextoOrdenado:Agregación de datos sobre riesgos: D-SIB
  - Obligacion:Garantizar agregación datos riesgos planes --establecida_en--> TextoOrdenado:Agregación de datos sobre riesgos: D-SIB
  - Obligacion:Examen periódico cumplimiento normas --aplica_a--> None
  - Obligacion:Acceso a documentos pertinentes --aplica_a--> None
  - Potestad:Exigir medidas correctivas deficiencias --aplica_a--> None
  - Potestad:Implementar límites riesgos restricción --aplica_a--> None
  - Potestad:Intensificar supervisión capital adicional --aplica_a--> None
  - Obligacion:Garantizar agregación datos riesgos planes --aplica_a--> None
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}]; omisiones []; condicion_de []; limita []

**NUEVO** — error: None

- Obligacion «Acceso a documentos de auditoría y validación»: La Superintendencia de Entidades Financieras y Cambiarias debe tener acceso a todos los documentos pertinentes, incluyendo informes de auditoría y validación interna, para examinar y evaluar periódicamente el cumplimiento de las disposicion… ‖ tramo (exacta): «deberá tener acceso a todos los documentos pertinentes –tales como informes de auditoría y validación interna–»
- Potestad «Adopción de medidas correctivas — deficiencias detectadas»: La Superintendencia de Entidades Financieras y Cambiarias está facultada para exigir a las entidades financieras que adopten medidas correctivas eficaces y oportunas cuando detecte deficiencias en sus capacidades de agregación de datos sobr… ‖ tramo (no): «podrá exigir a las entidades financieras la adopción de medidas correctivas eficaces y oportunas cuando detecte deficiencias en sus capacidades de agregación de…»
- Potestad «Implementación de límites restrictivos a riesgos»: La Superintendencia de Entidades Financieras y Cambiarias está facultada para exigir a las entidades financieras la implementación de límites más restrictivos a los riesgos o al crecimiento de sus actividades. ‖ tramo (no): «podrá exigir a las entidades financieras la implementación de límites más restrictivos a los riesgos o al crecimiento de sus actividades»
- Potestad «Intensificación de supervisión y capital adicional»: La Superintendencia de Entidades Financieras y Cambiarias está facultada para intensificar la supervisión y requerir capital adicional, de acuerdo con lo establecido en las normas sobre "Lineamientos para la gestión de riesgos en las entida… ‖ tramo (exacta): «podrá intensificar la supervisión y requerir capital adicional de acuerdo con lo establecido en las normas sobre "Lineamientos para la gestión de riesgos en las…»
- Potestad «Exigencia de planes de sistemas — nuevo negocio o adquisición»: Previo a que esta Institución otorgue autorización a las entidades financieras para que inicien un nuevo negocio o una adquisición, la Superintendencia de Entidades Financieras y Cambiarias está facultada para exigir que sus planes de siste… ‖ tramo (exacta): «podrá exigir que sus planes de sistemas garanticen que será posible una sólida agregación de datos sobre riesgos»
- Obligacion «Examen y evaluación periódica del cumplimiento»: La Superintendencia de Entidades Financieras y Cambiarias debe examinar y evaluar periódicamente el cumplimiento de las disposiciones por parte de las entidades financieras. ‖ tramo (exacta): «La Superintendencia de Entidades Financieras y Cambiarias examinará y evaluará periódicamente el cumplimiento por parte de las entidades financieras de estas di…»
  - Obligacion:Acceso a documentos de auditoría y validación --establecida_en--> TextoOrdenado:Agregación de datos sobre riesgos (D-SIB)
  - Potestad:Adopción de medidas correctivas — deficiencias detectadas --establecida_en--> TextoOrdenado:Agregación de datos sobre riesgos (D-SIB)
  - Potestad:Implementación de límites restrictivos a riesgos --establecida_en--> TextoOrdenado:Agregación de datos sobre riesgos (D-SIB)
  - Potestad:Intensificación de supervisión y capital adicional --establecida_en--> TextoOrdenado:Agregación de datos sobre riesgos (D-SIB)
  - Potestad:Exigencia de planes de sistemas — nuevo negocio o adquisició… --establecida_en--> TextoOrdenado:Agregación de datos sobre riesgos (D-SIB)
  - Obligacion:Examen y evaluación periódica del cumplimiento --establecida_en--> TextoOrdenado:Agregación de datos sobre riesgos (D-SIB)
  - Potestad:Adopción de medidas correctivas — deficiencias detectadas --aplica_a--> las entidades financieras
  - Potestad:Implementación de límites restrictivos a riesgos --aplica_a--> las entidades financieras
  - Potestad:Exigencia de planes de sistemas — nuevo negocio o adquisició… --aplica_a--> las entidades financieras
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "las entidades financieras", "verificada": "exacta", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "las entidades financieras", "verificada": "exacta", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "las entidades financieras", "verificada": "exacta", "sujeto_id": null}]; omisiones [{"categoria": "meta_normativo", "tramo": "para lo cual deberá tener acceso a todos los documentos pertinentes", "verificacion": "exacta", "nota": "Cláusula que expresa el propósito o fundamento de la obligación de examen y evaluación, no una presc…"}]; condicion_de []; limita []

*Cuantías en el texto propio: 0.*

## Ficha 4 — `opefci::7.2.1.2`

**Texto propio:**

```
7.2.1.2. Excepciones.
i) Cuotapartes de nuevos fondos comunes de inversión por 120 días corridos
contados a partir de aquel en que se lance el ofrecimiento al público, respecto
de los cuales las entidades financieras actúen como gerentes, depositarias,
colocadoras o promotoras.
ii) Cuotapartes de fondos comunes de inversión cerrados con oferta pública au-
torizada por la CNV, cuyo objeto de inversión sea alguno –uno o más– de los
previstos en el artículo 206 de la Ley 27440 de Financiamiento Productivo.
iii) Cuotapartes de fondos comunes de inversión abiertos autorizados por la
CNV, sujetos al “Régimen especial para la constitución de Fondos Comunes
de Inversión Abiertos para el Financiamiento de la Infraestructura y la Eco-
nomía Real” establecido por ese organismo mediante la Resolución General
N° 897/21 (sus modificatorias y complementarias).
iv) Cuotapartes de fondos comunes de inversión autorizados por la CNV, sujetos
al “Régimen especial para la constitución de Fondos Comunes de Inversión
PYMES” establecido por ese organismo mediante la Resolución General N°
803/19 (sus modificatorias y complementarias). La inversión podrá efectuarse
siempre que se trate de fondos cuyas inversiones se compongan por:
a) instrumentos previstos en los acápites i), ii), iii) y/o iv) del artículo 21 de la
Sección V “Régimen especial para la constitución de Fondos Comunes de
Inversión PYMES”, Capítulo II del Título V, de las normas de la Comisión
Nacional de Valores (N.T. 2013 y modif.), que no impliquen otorgamiento
de asistencia financiera a personas –humanas o jurídicas– vinculadas a la
entidad financiera conforme al punto 1.2.2. del TO sobre Grandes Exposi-
ciones al Riesgo de Crédito.
En el caso de instrumentos descontados, los valores deberán provenir del
cobro de operaciones de venta y/o de prestación de servicios correspon-
dientes a la actividad de la Pyme que los descuenta.
b) al menos el 85% de las inversiones, por instrumentos respecto de los cua-
les los sujetos legalmente obligados al pago se encuentren clasificados en
situación normal (categoría 1) según la última información disponible en la
Central de Deudores del Sistema Financiero.
Estas condiciones deberán ser verificadas de manera previa a realizar la in-
versión.
La participación en cada uno de los fondos a que se refieren los acápites ii), iii) y
iv)podrá ser de hasta el 15% del total de la emisión.
Las tenencias totales de cuotapartes de los fondos a que se refieren los incisos
i) a iv) –calculadas en promedio mensual de saldos diarios– no deberán superar
el importe equivalente al 2% de la RPC que registre la entidad financiera en el
mes inmediato precedente al que corresponda.
v) Cuotapartes de fondos comunes de inversión cerrados, con oferta pública au-
torizada por la CNV cuyo objeto sea la inversión en créditos originados por
entidades financieras u otros sujetos obligados a la observancia del TO sobre
Clasificación de Deudores.
Las participaciones en los fondos a que se refiere este i
```
**Último bloque heredado:** 7.2.1. Tenencia de cuotapartes.

**SELLADO** — error: None

- Excepcion «Cuotapartes nuevos FCI — 120 días desde lanzamiento»: Cuotapartes de nuevos fondos comunes de inversión por 120 días corridos contados a partir de aquel en que se lance el ofrecimiento al público, respecto de los cuales las entidades financieras actúen como gerentes, depositarias, colocadoras …
- Excepcion «Cuotapartes FCI cerrados — Ley 27440 artículo 206»: Cuotapartes de fondos comunes de inversión cerrados con oferta pública autorizada por la CNV, cuyo objeto de inversión sea alguno –uno o más– de los previstos en el artículo 206 de la Ley 27440 de Financiamiento Productivo.
- Excepcion «Cuotapartes FCI abiertos — Régimen infraestructura economía real»: Cuotapartes de fondos comunes de inversión abiertos autorizados por la CNV, sujetos al "Régimen especial para la constitución de Fondos Comunes de Inversión Abiertos para el Financiamiento de la Infraestructura y la Economía Real" estableci…
- Excepcion «Cuotapartes FCI PYMES — Régimen especial instrumentos permitidos»: Cuotapartes de fondos comunes de inversión autorizados por la CNV, sujetos al "Régimen especial para la constitución de Fondos Comunes de Inversión PYMES" establecido por ese organismo mediante la Resolución General N° 803/19 (sus modificat…
- Condicion «Instrumentos descontados — valores de operaciones Pyme»: En el caso de instrumentos descontados, los valores deberán provenir del cobro de operaciones de venta y/o de prestación de servicios correspondientes a la actividad de la Pyme que los descuenta.
- Condicion «Mínimo 85% inversiones — deudores clasificación normal»: Al menos el 85% de las inversiones, por instrumentos respecto de los cuales los sujetos legalmente obligados al pago se encuentren clasificados en situación normal (categoría 1) según la última información disponible en la Central de Deudor…
- Obligacion «Verificación previa condiciones de inversión»: Estas condiciones deberán ser verificadas de manera previa a realizar la inversión.
- Restriccion «Participación máxima 15% emisión por fondo»: La participación en cada uno de los fondos a que se refieren los acápites ii), iii) y iv) podrá ser de hasta el 15% del total de la emisión.
- Restriccion «Tenencias totales cuotapartes — máximo 2% RPC»: Las tenencias totales de cuotapartes de los fondos a que se refieren los incisos i) a iv) –calculadas en promedio mensual de saldos diarios– no deberán superar el importe equivalente al 2% de la RPC que registre la entidad financiera en el …
- Excepcion «Cuotapartes FCI cerrados — créditos entidades obligadas clasificación»: Cuotapartes de fondos comunes de inversión cerrados, con oferta pública autorizada por la CNV cuyo objeto sea la inversión en créditos originados por entidades financieras u otros sujetos obligados a la observancia del TO sobre Clasificació…
- Definicion «Tratamiento crediticio FCI créditos — equivalencia fideicomisos»: Las participaciones en los fondos a que se refiere este inciso recibirán el mismo tratamiento en materia crediticia que el previsto para los fideicomisos de créditos.
  - Excepcion:Cuotapartes nuevos FCI — 120 días desde lanzamiento --establecida_en--> TextoOrdenado:Operaciones con Fondos Comunes de Inversión
  - Excepcion:Cuotapartes FCI cerrados — Ley 27440 artículo 206 --establecida_en--> TextoOrdenado:Operaciones con Fondos Comunes de Inversión
  - Excepcion:Cuotapartes FCI abiertos — Régimen infraestructura economía … --establecida_en--> TextoOrdenado:Operaciones con Fondos Comunes de Inversión
  - Excepcion:Cuotapartes FCI PYMES — Régimen especial instrumentos permit… --establecida_en--> TextoOrdenado:Operaciones con Fondos Comunes de Inversión
  - Condicion:Instrumentos descontados — valores de operaciones Pyme --establecida_en--> TextoOrdenado:Operaciones con Fondos Comunes de Inversión
  - Condicion:Mínimo 85% inversiones — deudores clasificación normal --establecida_en--> TextoOrdenado:Operaciones con Fondos Comunes de Inversión
  - Obligacion:Verificación previa condiciones de inversión --establecida_en--> TextoOrdenado:Operaciones con Fondos Comunes de Inversión
  - Restriccion:Participación máxima 15% emisión por fondo --establecida_en--> TextoOrdenado:Operaciones con Fondos Comunes de Inversión
  - Restriccion:Tenencias totales cuotapartes — máximo 2% RPC --establecida_en--> TextoOrdenado:Operaciones con Fondos Comunes de Inversión
  - Excepcion:Cuotapartes FCI cerrados — créditos entidades obligadas clas… --establecida_en--> TextoOrdenado:Operaciones con Fondos Comunes de Inversión
  - Definicion:Tratamiento crediticio FCI créditos — equivalencia fideicomi… --establecida_en--> TextoOrdenado:Operaciones con Fondos Comunes de Inversión
  - Excepcion:Cuotapartes nuevos FCI — 120 días desde lanzamiento --aplica_a--> None
  - Excepcion:Cuotapartes FCI cerrados — Ley 27440 artículo 206 --aplica_a--> None
  - Excepcion:Cuotapartes FCI abiertos — Régimen infraestructura economía … --aplica_a--> None
  - Excepcion:Cuotapartes FCI PYMES — Régimen especial instrumentos permit… --aplica_a--> None
  - Obligacion:Verificación previa condiciones de inversión --aplica_a--> None
  - Restriccion:Participación máxima 15% emisión por fondo --aplica_a--> None
  - Restriccion:Tenencias totales cuotapartes — máximo 2% RPC --aplica_a--> None
  - Excepcion:Cuotapartes FCI cerrados — créditos entidades obligadas clas… --aplica_a--> None
  - Condicion:Instrumentos descontados — valores de operaciones Pyme --condicion_de--> Excepcion:Cuotapartes FCI PYMES — Régimen especial instrumentos permit…
  - Condicion:Mínimo 85% inversiones — deudores clasificación normal --condicion_de--> Excepcion:Cuotapartes FCI PYMES — Régimen especial instrumentos permit…
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}]; omisiones []; condicion_de [{"de": "Condicion:Instrumentos descontados — valores de operaciones Pyme", "a": "Excepcion:Cuotapartes FCI PYMES — Régimen especial instrumentos permit…", "firma_nueva": false}, {"de": "Condicion:Mínimo 85% inversiones — deudores clasificación normal", "a": "Excepcion:Cuotapartes FCI PYMES — Régimen especial instrumentos permit…", "firma_nueva": false}]; limita []

**NUEVO** — error: None

- Excepcion «Excepto nuevos FCI 120 días — tenencia de cuotapartes»: Excepción a la restricción de tenencia de cuotapartes: se exceptúan cuotapartes de nuevos fondos comunes de inversión por un plazo de 120 días corridos contados desde el lanzamiento del ofrecimiento al público, cuando las entidades financie… ‖ tramo (exacta): «Cuotapartes de nuevos fondos comunes de inversión por 120 días corridos contados a partir de aquel en que se lance el ofrecimiento al público, respecto de los c…»
- Excepcion «Excepto FCI cerrados ley 27440 — tenencia de cuotapartes»: Excepción a la restricción de tenencia de cuotapartes: se exceptúan cuotapartes de fondos comunes de inversión cerrados con oferta pública autorizada por la CNV, cuyo objeto de inversión sea alguno de los previstos en el artículo 206 de la … ‖ tramo (exacta): «Cuotapartes de fondos comunes de inversión cerrados con oferta pública autorizada por la CNV, cuyo objeto de inversión sea alguno –uno o más– de los previstos e…»
- Excepcion «Excepto FCI abiertos régimen especial infraestructura — tenencia de cuotapartes»: Excepción a la restricción de tenencia de cuotapartes: se exceptúan cuotapartes de fondos comunes de inversión abiertos autorizados por la CNV, sujetos al régimen especial para financiamiento de infraestructura y economía real establecido p… ‖ tramo (exacta): «Cuotapartes de fondos comunes de inversión abiertos autorizados por la CNV, sujetos al "Régimen especial para la constitución de Fondos Comunes de Inversión Abi…»
- Excepcion «Excepto FCI PYMES — tenencia de cuotapartes»: Excepción a la restricción de tenencia de cuotapartes: se exceptúan cuotapartes de fondos comunes de inversión PYMES autorizados por la CNV, sujetos al régimen especial establecido por Resolución General N° 803/19. ‖ tramo (exacta): «Cuotapartes de fondos comunes de inversión autorizados por la CNV, sujetos al "Régimen especial para la constitución de Fondos Comunes de Inversión PYMES" estab…»
- Condicion «Fondos PYMES compuestos por instrumentos art. 21 NC y sin vinculación»: Condición para la inversión en FCI PYMES: los fondos deben estar compuestos por instrumentos previstos en los acápites i), ii), iii) y/o iv) del artículo 21 de la Sección V del régimen especial de FCI PYMES de las normas CNV, que no impliqu… ‖ tramo (exacta): «instrumentos previstos en los acápites i), ii), iii) y/o iv) del artículo 21 de la Sección V "Régimen especial para la constitución de Fondos Comunes de Inversi…»
- Condicion «Instrumentos descontados de operaciones de venta/servicios Pyme»: Condición para instrumentos descontados en FCI PYMES: los valores deben provenir del cobro de operaciones de venta y/o prestación de servicios correspondientes a la actividad de la Pyme que los descuenta. ‖ tramo (exacta): «En el caso de instrumentos descontados, los valores deberán provenir del cobro de operaciones de venta y/o de prestación de servicios correspondientes a la acti…»
- Restriccion «Mínimo 85% inversiones clasificación normal — FCI PYMES»: Restricción sobre la composición de inversiones en FCI PYMES: al menos el 85% de las inversiones debe estar compuesta por instrumentos respecto de los cuales los sujetos legalmente obligados al pago se encuentren clasificados en situación n… ‖ tramo (exacta): «al menos el 85% de las inversiones, por instrumentos respecto de los cuales los sujetos legalmente obligados al pago se encuentren clasificados en situación nor…»
- Obligacion «Verificar previo inversión condiciones fondos PYMES»: Obligación de verificar de manera previa a realizar la inversión las condiciones de composición de los fondos PYMES (instrumentos y clasificación de deudores). ‖ tramo (exacta): «Estas condiciones deberán ser verificadas de manera previa a realizar la inversión.»
- Restriccion «Participación máx. 15% por fondo — FCI excepciones ii), iii), iv)»: Restricción sobre la participación de la entidad financiera en cada uno de los fondos excepcionales (ii, iii, iv): no podrá exceder el 15% del total de la emisión. ‖ tramo (exacta): «La participación en cada uno de los fondos a que se refieren los acápites ii), iii) y iv)podrá ser de hasta el 15% del total de la emisión.»
- Restriccion «Tenencias totales máx. 2% RPC mensual — FCI excepciones i-iv»: Restricción sobre las tenencias totales de cuotapartes de los fondos de las excepciones i) a iv): no deben superar el 2% de la RPC de la entidad financiera, calculadas en promedio mensual de saldos diarios, con referencia al mes inmediato p… ‖ tramo (exacta): «Las tenencias totales de cuotapartes de los fondos a que se refieren los incisos i) a iv) –calculadas en promedio mensual de saldos diarios– no deberán superar …»
- Excepcion «Excepto FCI cerrados créditos — tenencia de cuotapartes»: Excepción a la restricción de tenencia de cuotapartes: se exceptúan cuotapartes de fondos comunes de inversión cerrados, con oferta pública autorizada por la CNV, cuyo objeto sea la inversión en créditos originados por entidades financieras… ‖ tramo (exacta): «Cuotapartes de fondos comunes de inversión cerrados, con oferta pública autorizada por la CNV cuyo objeto sea la inversión en créditos originados por entidades …»
- Obligacion «Trato crediticio igual a fideicomisos créditos — FCI créditos»: Obligación de otorgar a las participaciones en fondos comunes de inversión cerrados de créditos el mismo tratamiento en materia crediticia que el previsto para los fideicomisos de créditos. ‖ tramo (exacta): «Las participaciones en los fondos a que se refiere este inciso recibirán el mismo tratamiento en materia crediticia que el previsto para los fideicomisos de cré…»
- Comunicacion «Com. RG 897/21»:  ‖ tramo (exacta): «Resolución General N° 897/21»
- Comunicacion «Com. RG 803/19»:  ‖ tramo (exacta): «Resolución General N° 803/19»
- Comunicacion «Ley 27440 Financiamiento Productivo»:  ‖ tramo (exacta): «Ley 27440 de Financiamiento Productivo»
  - Excepcion:Excepto nuevos FCI 120 días — tenencia de cuotapartes --establecida_en--> TextoOrdenado:Operaciones con FCI
  - Excepcion:Excepto FCI cerrados ley 27440 — tenencia de cuotapartes --establecida_en--> TextoOrdenado:Operaciones con FCI
  - Excepcion:Excepto FCI abiertos régimen especial infraestructura — tene… --establecida_en--> TextoOrdenado:Operaciones con FCI
  - Excepcion:Excepto FCI PYMES — tenencia de cuotapartes --establecida_en--> TextoOrdenado:Operaciones con FCI
  - Condicion:Fondos PYMES compuestos por instrumentos art. 21 NC y sin vi… --establecida_en--> TextoOrdenado:Operaciones con FCI
  - Condicion:Instrumentos descontados de operaciones de venta/servicios P… --establecida_en--> TextoOrdenado:Operaciones con FCI
  - Restriccion:Mínimo 85% inversiones clasificación normal — FCI PYMES --establecida_en--> TextoOrdenado:Operaciones con FCI
  - Obligacion:Verificar previo inversión condiciones fondos PYMES --establecida_en--> TextoOrdenado:Operaciones con FCI
  - Restriccion:Participación máx. 15% por fondo — FCI excepciones ii), iii)… --establecida_en--> TextoOrdenado:Operaciones con FCI
  - Restriccion:Tenencias totales máx. 2% RPC mensual — FCI excepciones i-iv --establecida_en--> TextoOrdenado:Operaciones con FCI
  - Excepcion:Excepto FCI cerrados créditos — tenencia de cuotapartes --establecida_en--> TextoOrdenado:Operaciones con FCI
  - Obligacion:Trato crediticio igual a fideicomisos créditos — FCI crédito… --establecida_en--> TextoOrdenado:Operaciones con FCI
  - Condicion:Fondos PYMES compuestos por instrumentos art. 21 NC y sin vi… --condicion_de--> Excepcion:Excepto FCI PYMES — tenencia de cuotapartes
  - Condicion:Instrumentos descontados de operaciones de venta/servicios P… --condicion_de--> Excepcion:Excepto FCI PYMES — tenencia de cuotapartes
  - Obligacion:Verificar previo inversión condiciones fondos PYMES --aplica_a--> las entidades financieras
  - Obligacion:Trato crediticio igual a fideicomisos créditos — FCI crédito… --aplica_a--> las entidades financieras
  - TextoOrdenado:Operaciones con FCI --referencia--> Comunicacion:Com. RG 897/21
  - TextoOrdenado:Operaciones con FCI --referencia--> Comunicacion:Com. RG 803/19
  - TextoOrdenado:Operaciones con FCI --referencia--> Comunicacion:Ley 27440 Financiamiento Productivo
- hechos: umbrales [{"entidad": "Excepcion:Excepto nuevos FCI 120 días — tenencia de cuotapartes", "tramo": "por 120 días corridos", "verificacion": "exacta"}, {"entidad": "Restriccion:Mínimo 85% inversiones clasificación normal — FCI PYMES", "tramo": "al menos el 85%", "verificacion": "exacta"}, {"entidad": "Restriccion:Participación máx. 15% por fondo — FCI excepciones ii), iii)…", "tramo": "de hasta el 15% del total de la emisión", "verificacion": "exacta"}, {"entidad": "Restriccion:Tenencias totales máx. 2% RPC mensual — FCI excepciones i-iv", "tramo": "no deberán superar el importe equivalente al 2% de la RPC que registre la entidad financiera en el mes inmediato precede…", "verificacion": "exacta"}]; menciones [{"pred": "aplica_a", "mencion": "las entidades financieras", "verificada": "exacta", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "las entidades financieras", "verificada": "exacta", "sujeto_id": null}]; omisiones [{"categoria": "relacion_sin_predicado", "tramo": "La inversión podrá efectuarse siempre que se trate de fondos cuyas inversiones se compongan por: ...", "verificacion": "exacta", "nota": "condicion_sobre (Excepcion e4 condiciona una Operacion implícita de 'inversión en FCI PYMES')"}]; condicion_de [{"de": "Condicion:Fondos PYMES compuestos por instrumentos art. 21 NC y sin vi…", "a": "Excepcion:Excepto FCI PYMES — tenencia de cuotapartes", "firma_nueva": false}, {"de": "Condicion:Instrumentos descontados de operaciones de venta/servicios P…", "a": "Excepcion:Excepto FCI PYMES — tenencia de cuotapartes", "firma_nueva": false}]; limita []

*Cuantías en el texto propio: 4.*

## Ficha 5 — `expaef::1.1.2.5`

**Texto propio:**

```
1.1.2.5. No registrar deuda por asistencia financiera del BCRA por iliquidez.
```
**Último bloque heredado:** contar con la autorización previa del Directorio del Banco Central de la República Argenti- na (BCRA). A esos efectos deberán cumplir las siguientes condiciones:

**SELLADO** — error: None

- Obligacion «No registrar deuda asistencia financiera BCRA por iliquidez»: No registrar deuda por asistencia financiera del BCRA por iliquidez.
  - Obligacion:No registrar deuda asistencia financiera BCRA por iliquidez --establecida_en--> TextoOrdenado:Sucursales en el país y exterior
  - Obligacion:No registrar deuda asistencia financiera BCRA por iliquidez --aplica_a--> None
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}]; omisiones []; condicion_de []; limita []

**NUEVO** — error: None

- Restriccion «No registrar deuda por asistencia financiera BCRA iliquidez»: Las entidades financieras no deberán registrar deuda por asistencia financiera del BCRA por motivos de iliquidez ‖ tramo (exacta): «No registrar deuda por asistencia financiera del BCRA por iliquidez»
  - Restriccion:No registrar deuda por asistencia financiera BCRA iliquidez --establecida_en--> TextoOrdenado:Autorización Sucursales Exterior
  - Restriccion:No registrar deuda por asistencia financiera BCRA iliquidez --aplica_a--> Las entidades financieras
  - rechazo: ref_colgante: relations[1] (prohibe): source='e1' target='e2'
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "Las entidades financieras", "verificada": "exacta", "sujeto_id": null}]; omisiones []; condicion_de []; limita []

*Cuantías en el texto propio: 0.*

## Ficha 6 — `cap::8.5.3`

**Texto propio:**

```
8.5.3. RPC: importe resultante de multiplicar 8% por los APR.
```
**Último bloque heredado:** La falta de cumplimiento de cualquiera de estos límites mínimos será considerada incumpli- miento de integración del capital mínimo, correspondiendo la aplicación de lo previsto por el punto 1.4. de estas normas y la Sección 1. de las normas sobre “Incumplimientos de capitales mínimos y relaciones t…

**SELLADO** — error: None

- Definicion «RPC: importe 8% de APR»: Importe resultante de multiplicar 8% por los APR (activos ponderados por riesgo)
- Operacion «Cálculo de Responsabilidad Patrimonial Computable»: Importe resultante de multiplicar 8% por los APR
  - Definicion:RPC: importe 8% de APR --establecida_en--> TextoOrdenado:Texto Ordenado de Capitales Mínimos
  - Operacion:Cálculo de Responsabilidad Patrimonial Computable --establecida_en--> TextoOrdenado:Texto Ordenado de Capitales Mínimos
  - Operacion:Cálculo de Responsabilidad Patrimonial Computable --aplica_a--> None
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}]; omisiones []; condicion_de []; limita []

**NUEVO** — error: None

- Definicion «RPC: 8% de los APR»: importe resultante de multiplicar 8% por los APR ‖ tramo (exacta): «RPC: importe resultante de multiplicar 8% por los APR»
- Restriccion «Límite RPC — 8% de los APR»: el RPC deberá ser un importe resultante de multiplicar 8% por los APR, conforme a los límites mínimos que las entidades deben observar ‖ tramo (exacta): «RPC: importe resultante de multiplicar 8% por los APR»
- Operacion «Cálculo de RPC»: determinación del importe de la Responsabilidad Patrimonial Computable multiplicando 8% por los Activos Ponderados por Riesgo ‖ tramo (exacta): «importe resultante de multiplicar 8% por los APR»
  - Definicion:RPC: 8% de los APR --establecida_en--> TextoOrdenado:Capitales mínimos
  - Restriccion:Límite RPC — 8% de los APR --establecida_en--> TextoOrdenado:Capitales mínimos
  - Operacion:Cálculo de RPC --establecida_en--> TextoOrdenado:Capitales mínimos
  - Restriccion:Límite RPC — 8% de los APR --limita--> Operacion:Cálculo de RPC
- hechos: umbrales [{"entidad": "Restriccion:Límite RPC — 8% de los APR", "tramo": "8%", "verificacion": "exacta"}]; menciones []; omisiones [{"categoria": "meta_normativo", "tramo": "La falta de cumplimiento de cualquiera de estos límites mínimos será considerada incumplimiento de i…", "verificacion": "no", "nota": "cláusula que predica sobre las consecuencias del incumplimiento (sanción/aplicación de régimen disci…"}]; condicion_de []; limita [{"de": "Restriccion:Límite RPC — 8% de los APR", "a": "Operacion:Cálculo de RPC"}]

*Cuantías en el texto propio: 1.*

## Ficha 7 — `adrei::4.3.1::intro`

**Texto propio:**

```
Las entidades financieras deben:
```
**Último bloque heredado:** 4.3.1. Requisitos.

**SELLADO** — error: None

- hechos: umbrales []; menciones []; omisiones []; condicion_de []; limita []

**NUEVO** — error: None

- hechos: umbrales []; menciones []; omisiones [{"categoria": "meta_normativo", "tramo": "Las entidades financieras deben:", "verificacion": "exacta", "nota": "Anuncio de lista de requisitos sin contenido normativo completo en el bloque intro; el contenido se …"}]; condicion_de []; limita []

*Cuantías en el texto propio: 0.*

## Ficha 8 — `cap::2.12.2.4`

**Texto propio:**

```
2.12.2.4. Al sector público no financiero y al BCRA. Demás.
[TABLA cap::tabla2f000 | página 23 | R-TC2 | columnas]
Columnas: Calificación | AAA hasta AA- | A+ hasta A- | BBB+ hasta BBB- | BB+ hasta B- | Inferior a B- | No calificado
Fila 1: Calificación = Ponderador de riesgo | AAA hasta AA- = 0% | A+ hasta A- = 20% | BBB+ hasta BBB- = 50% | BB+ hasta B- = 100% | Inferior a B- = 150% | No calificado = 100%
[FIN TABLA cap::tabla2f000]
```
**Último bloque heredado:** 2.12.2. Exposición a gobiernos y bancos centrales.

**SELLADO** — error: None

- Operacion «Ponderación de riesgo — gobiernos y bancos centrales»: Asignación de ponderador de riesgo a exposiciones a gobiernos y bancos centrales según calificación crediticia (AAA, AA-, A+, A-, BBB+, BBB-, BB+, B- inferior, o no calificados)
- Restriccion «Tope ponderador 0% — AAA a A+»: Ponderador de riesgo del 0% para exposiciones a gobiernos y bancos centrales con calificación desde AAA hasta A+
- Restriccion «Tope ponderador 20% — AA- a A-»: Ponderador de riesgo del 20% para exposiciones a gobiernos y bancos centrales con calificación desde AA- hasta A-
- Restriccion «Tope ponderador 50% — BBB+ a BBB-»: Ponderador de riesgo del 50% para exposiciones a gobiernos y bancos centrales con calificación desde BBB+ hasta BBB-
- Restriccion «Tope ponderador 100% — BB+ a inferior B-»: Ponderador de riesgo del 100% para exposiciones a gobiernos y bancos centrales con calificación desde BB+ hasta inferior a B-
- Restriccion «Tope ponderador 150% — sin calificación suficiente»: Ponderador de riesgo del 150% para exposiciones a gobiernos y bancos centrales no calificados o sin calificación crediticia
  - Operacion:Ponderación de riesgo — gobiernos y bancos centrales --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Restriccion:Tope ponderador 0% — AAA a A+ --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Restriccion:Tope ponderador 20% — AA- a A- --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Restriccion:Tope ponderador 50% — BBB+ a BBB- --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Restriccion:Tope ponderador 100% — BB+ a inferior B- --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Restriccion:Tope ponderador 150% — sin calificación suficiente --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Restriccion:Tope ponderador 0% — AAA a A+ --limita--> Operacion:Ponderación de riesgo — gobiernos y bancos centrales
  - Restriccion:Tope ponderador 20% — AA- a A- --limita--> Operacion:Ponderación de riesgo — gobiernos y bancos centrales
  - Restriccion:Tope ponderador 50% — BBB+ a BBB- --limita--> Operacion:Ponderación de riesgo — gobiernos y bancos centrales
  - Restriccion:Tope ponderador 100% — BB+ a inferior B- --limita--> Operacion:Ponderación de riesgo — gobiernos y bancos centrales
  - Restriccion:Tope ponderador 150% — sin calificación suficiente --limita--> Operacion:Ponderación de riesgo — gobiernos y bancos centrales
  - Operacion:Ponderación de riesgo — gobiernos y bancos centrales --aplica_a--> None
  - Restriccion:Tope ponderador 0% — AAA a A+ --aplica_a--> None
  - Restriccion:Tope ponderador 20% — AA- a A- --aplica_a--> None
  - Restriccion:Tope ponderador 50% — BBB+ a BBB- --aplica_a--> None
  - Restriccion:Tope ponderador 100% — BB+ a inferior B- --aplica_a--> None
  - Restriccion:Tope ponderador 150% — sin calificación suficiente --aplica_a--> None
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}]; omisiones [{"categoria": null, "tramo": "", "verificacion": "ausente", "nota": "Estructura tabular de mapeo de calificaciones crediticias a ponderadores: la matriz de calificacione…"}]; condicion_de []; limita [{"de": "Restriccion:Tope ponderador 0% — AAA a A+", "a": "Operacion:Ponderación de riesgo — gobiernos y bancos centrales"}, {"de": "Restriccion:Tope ponderador 20% — AA- a A-", "a": "Operacion:Ponderación de riesgo — gobiernos y bancos centrales"}, {"de": "Restriccion:Tope ponderador 50% — BBB+ a BBB-", "a": "Operacion:Ponderación de riesgo — gobiernos y bancos centrales"}, {"de": "Restriccion:Tope ponderador 100% — BB+ a inferior B-", "a": "Operacion:Ponderación de riesgo — gobiernos y bancos centrales"}, {"de": "Restriccion:Tope ponderador 150% — sin calificación suficiente", "a": "Operacion:Ponderación de riesgo — gobiernos y bancos centrales"}]

**NUEVO** — error: None

- Operacion «Exposición a gobiernos y bancos centrales — ponderadores por calificación»: Aplicación de ponderadores de riesgo a la exposición a gobiernos y bancos centrales no calificados según su clase de riesgo: 0 % para AAA hasta AA-, 20 % para A+ hasta A-, 50 % para BBB+ hasta BBB-, 100 % para BB+ hasta B-, 150 % para infer… ‖ tramo (no): «Exposición a gobiernos y bancos centrales. Demás.»
- Restriccion «Ponderador 0 % — AAA hasta AA-»: El ponderador de riesgo para exposiciones a gobiernos y bancos centrales calificados entre AAA hasta AA- es del 0 %. ‖ tramo (exacta): «AAA hasta AA- = 0%»
- Restriccion «Ponderador 20 % — A+ hasta A-»: El ponderador de riesgo para exposiciones a gobiernos y bancos centrales calificados entre A+ hasta A- es del 20 %. ‖ tramo (exacta): «A+ hasta A- = 20%»
- Restriccion «Ponderador 50 % — BBB+ hasta BBB-»: El ponderador de riesgo para exposiciones a gobiernos y bancos centrales calificados entre BBB+ hasta BBB- es del 50 %. ‖ tramo (exacta): «BBB+ hasta BBB- = 50%»
- Restriccion «Ponderador 100 % — BB+ hasta B-»: El ponderador de riesgo para exposiciones a gobiernos y bancos centrales calificados entre BB+ hasta B- es del 100 %. ‖ tramo (exacta): «BB+ hasta B- = 100%»
- Restriccion «Ponderador 150 % — Inferior a B-»: El ponderador de riesgo para exposiciones a gobiernos y bancos centrales calificados inferior a B- es del 150 %. ‖ tramo (exacta): «Inferior a B- = 150%»
- Restriccion «Ponderador 100 % — No calificado»: El ponderador de riesgo para exposiciones a gobiernos y bancos centrales no calificados es del 100 %. ‖ tramo (exacta): «No calificado = 100%»
  - Restriccion:Ponderador 0 % — AAA hasta AA- --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Restriccion:Ponderador 20 % — A+ hasta A- --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Restriccion:Ponderador 50 % — BBB+ hasta BBB- --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Restriccion:Ponderador 100 % — BB+ hasta B- --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Restriccion:Ponderador 150 % — Inferior a B- --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Restriccion:Ponderador 100 % — No calificado --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Restriccion:Ponderador 0 % — AAA hasta AA- --limita--> Operacion:Exposición a gobiernos y bancos centrales — ponderadores por…
  - Restriccion:Ponderador 20 % — A+ hasta A- --limita--> Operacion:Exposición a gobiernos y bancos centrales — ponderadores por…
  - Restriccion:Ponderador 50 % — BBB+ hasta BBB- --limita--> Operacion:Exposición a gobiernos y bancos centrales — ponderadores por…
  - Restriccion:Ponderador 100 % — BB+ hasta B- --limita--> Operacion:Exposición a gobiernos y bancos centrales — ponderadores por…
  - Restriccion:Ponderador 150 % — Inferior a B- --limita--> Operacion:Exposición a gobiernos y bancos centrales — ponderadores por…
  - Restriccion:Ponderador 100 % — No calificado --limita--> Operacion:Exposición a gobiernos y bancos centrales — ponderadores por…
  - Operacion:Exposición a gobiernos y bancos centrales — ponderadores por… --aplica_a--> las entidades
- hechos: umbrales [{"entidad": "Restriccion:Ponderador 0 % — AAA hasta AA-", "tramo": "0%", "verificacion": "exacta"}, {"entidad": "Restriccion:Ponderador 20 % — A+ hasta A-", "tramo": "20%", "verificacion": "exacta"}, {"entidad": "Restriccion:Ponderador 50 % — BBB+ hasta BBB-", "tramo": "50%", "verificacion": "exacta"}, {"entidad": "Restriccion:Ponderador 100 % — BB+ hasta B-", "tramo": "100%", "verificacion": "exacta"}, {"entidad": "Restriccion:Ponderador 150 % — Inferior a B-", "tramo": "150%", "verificacion": "exacta"}, {"entidad": "Restriccion:Ponderador 100 % — No calificado", "tramo": "100%", "verificacion": "exacta"}]; menciones [{"pred": "aplica_a", "mencion": "las entidades", "verificada": "exacta", "sujeto_id": null}]; omisiones []; condicion_de []; limita [{"de": "Restriccion:Ponderador 0 % — AAA hasta AA-", "a": "Operacion:Exposición a gobiernos y bancos centrales — ponderadores por…"}, {"de": "Restriccion:Ponderador 20 % — A+ hasta A-", "a": "Operacion:Exposición a gobiernos y bancos centrales — ponderadores por…"}, {"de": "Restriccion:Ponderador 50 % — BBB+ hasta BBB-", "a": "Operacion:Exposición a gobiernos y bancos centrales — ponderadores por…"}, {"de": "Restriccion:Ponderador 100 % — BB+ hasta B-", "a": "Operacion:Exposición a gobiernos y bancos centrales — ponderadores por…"}, {"de": "Restriccion:Ponderador 150 % — Inferior a B-", "a": "Operacion:Exposición a gobiernos y bancos centrales — ponderadores por…"}, {"de": "Restriccion:Ponderador 100 % — No calificado", "a": "Operacion:Exposición a gobiernos y bancos centrales — ponderadores por…"}]

*Cuantías en el texto propio: 6.*

## Ficha 9 — `cap::8.5.2`

**Texto propio:**

```
8.5.2. PNb: importe resultante de multiplicar 6% por los APR.
```
**Último bloque heredado:** La falta de cumplimiento de cualquiera de estos límites mínimos será considerada incumpli- miento de integración del capital mínimo, correspondiendo la aplicación de lo previsto por el punto 1.4. de estas normas y la Sección 1. de las normas sobre “Incumplimientos de capitales mínimos y relaciones t…

**SELLADO** — error: None

- Operacion «PNb: cálculo del patrimonio neto básico»: PNb: importe resultante de multiplicar 6% por los APR (activos ponderados por riesgo)
- Obligacion «Cálculo de PNb según 6% de APR»: El patrimonio neto básico (PNb) deberá calcularse como el importe resultante de multiplicar 6% por los activos ponderados por riesgo (APR)
  - Obligacion:Cálculo de PNb según 6% de APR --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Obligacion:Cálculo de PNb según 6% de APR --aplica_a--> None
  - Obligacion:Cálculo de PNb según 6% de APR --regula--> Operacion:PNb: cálculo del patrimonio neto básico
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}]; omisiones []; condicion_de []; limita []

**NUEVO** — error: None

- Operacion «Cálculo PNb — 6% de APR»: Cálculo del Patrimonio Neto básico (PNb): importe resultante de multiplicar 6% por los Activos Ponderados por Riesgo (APR). Esta exigencia forma parte de los límites mínimos que deben observarse conforme al encabezado de la norma. ‖ tramo (exacta): «importe resultante de multiplicar 6% por los APR»
- Restriccion «Límite PNb — 6% de APR»: Límite mínimo de Patrimonio Neto básico fijado en 6% de los Activos Ponderados por Riesgo (APR). Este límite forma parte de los límites mínimos que deben observarse conforme al punto 8.5. ‖ tramo (exacta): «PNb: importe resultante de multiplicar 6% por los APR»
  - Operacion:Cálculo PNb — 6% de APR --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Restriccion:Límite PNb — 6% de APR --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Restriccion:Límite PNb — 6% de APR --aplica_a--> las entidades
- hechos: umbrales [{"entidad": "Restriccion:Límite PNb — 6% de APR", "tramo": "6% por los APR", "verificacion": "exacta"}]; menciones [{"pred": "aplica_a", "mencion": "las entidades", "verificada": "no", "sujeto_id": null}]; omisiones [{"categoria": "meta_normativo", "tramo": "La falta de cumplimiento de cualquiera de estos límites mínimos será considerada incumplimiento de i…", "verificacion": "no", "nota": "Cláusula que predica sobre las consecuencias jurídicas del incumplimiento (sanción / aplicación de r…"}]; condicion_de []; limita []

*Cuantías en el texto propio: 1.*

## Ficha 10 — `ctacte::8.4::intro`

**Texto propio:**

```
Se demostrará con cualquiera de las siguientes alternativas:
```
**Último bloque heredado:** 8.4. Cancelación de las multas después de vencido el plazo legalmente establecido.

**SELLADO** — error: None

- hechos: umbrales []; menciones []; omisiones []; condicion_de []; limita []

**NUEVO** — error: None

- hechos: umbrales []; menciones []; omisiones [{"categoria": "meta_normativo", "tramo": "Se demostrará con cualquiera de las siguientes alternativas:", "verificacion": "exacta", "nota": "Enunciado que predica sobre cómo probar un supuesto (modalidad de demostración) sin prescribir condu…"}]; condicion_de []; limita []

*Cuantías en el texto propio: 0.*

## Ficha 11 — `ext::10.2.2`

**Texto propio:**

```
10.2.2. Registro de ingreso aduanero.
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
```
**Último bloque heredado:** 10.2. Definiciones.

**SELLADO** — error: None

- Definicion «Registro de ingreso aduanero — importación de bienes»: Se considera que una importación de bienes cuenta con el registro de ingreso aduanero cuando el importador realizó la oficialización del despacho de importación para su posterior despacho a plaza de los bienes.
- Definicion «Cumplimiento — ingreso de bienes por Solicitud Particular»: Se da cumplimiento al registro de ingreso aduanero cuando los bienes son ingresados al país con despacho a plaza a través de Solicitud Particular o Courier.
- Definicion «Cumplimiento — ingreso de bienes a zonas francas»: Se da cumplimiento al registro de ingreso aduanero cuando se cumplimentó el trámite aduanero por el ingreso de bienes del exterior a zonas francas nacionales y dicho ingreso se corresponde con una venta de bienes de un no residente a un res…
- Excepcion «Exclusión — importaciones suspensivas de depósitos»: No se incluyen los registros aduaneros por importaciones suspensivas de depósitos de almacenamiento.
- Excepcion «Exclusión — importaciones temporarias sin giro de divisas»: No se incluyen los ingresos de importaciones temporarias sin giro de divisas.
- Operacion «Oficialización del despacho de importación»: Acto realizado por el importador de oficializar el despacho de importación para posterior despacho a plaza de bienes.
- Operacion «Ingreso de bienes con despacho a plaza por Solicitud Particular o Courier»: Ingreso al país de bienes con despacho a plaza a través de Solicitud Particular o Courier.
- Operacion «Trámite aduanero por ingreso de bienes a zonas francas»: Cumplimentación del trámite aduanero por el ingreso de bienes del exterior a zonas francas nacionales correspondiente a una venta de bienes de un no residente a un residente.
  - Definicion:Registro de ingreso aduanero — importación de bienes --establecida_en--> TextoOrdenado:Exterior Cambios
  - Definicion:Cumplimiento — ingreso de bienes por Solicitud Particular --establecida_en--> TextoOrdenado:Exterior Cambios
  - Definicion:Cumplimiento — ingreso de bienes a zonas francas --establecida_en--> TextoOrdenado:Exterior Cambios
  - Excepcion:Exclusión — importaciones suspensivas de depósitos --establecida_en--> TextoOrdenado:Exterior Cambios
  - Excepcion:Exclusión — importaciones temporarias sin giro de divisas --establecida_en--> TextoOrdenado:Exterior Cambios
  - Operacion:Oficialización del despacho de importación --establecida_en--> TextoOrdenado:Exterior Cambios
  - Operacion:Ingreso de bienes con despacho a plaza por Solicitud Particu… --establecida_en--> TextoOrdenado:Exterior Cambios
  - Operacion:Trámite aduanero por ingreso de bienes a zonas francas --establecida_en--> TextoOrdenado:Exterior Cambios
- hechos: umbrales []; menciones []; omisiones []; condicion_de []; limita []

**NUEVO** — error: None

- Definicion «Registro de ingreso aduanero»: Una importación de bienes cuenta con el registro de ingreso aduanero cuando el importador realizó la oficialización del despacho de importación para su posterior despacho a plaza de los bienes. ‖ tramo (exacta): «A los efectos de esta norma se considera que una importación de bienes cuenta con el registro de ingreso aduanero cuando el importador realizó la oficialización…»
- Definicion «Registro aduanero — despacho a plaza por Solicitud Particular o Courier»: También se da cumplimiento a dicho registro cuando los bienes son ingresados al país con despacho a plaza a través de Solicitud Particular o Courier. ‖ tramo (exacta): «También se da cumplimiento a dicho registro cuando los bienes son ingresados al país con despacho a plaza a través de Solicitud Particular o Courier»
- Definicion «Registro aduanero — zonas francas nacionales»: También se da cumplimiento a dicho registro cuando se cumplimentó el trámite aduanero por el ingreso de bienes del exterior a zonas francas nacionales y dicho ingreso se corresponde con una venta de bienes de un no residente a un residente. ‖ tramo (exacta): «o se cumplimentó el trámite aduanero por el ingreso de bienes del exterior a zonas francas nacionales y dicho ingreso se corresponde con una venta de bienes de …»
- Excepcion «Exclusión — importaciones suspensivas de depósitos»: No se incluyen los registros aduaneros por importaciones suspensivas de depósitos de almacenamiento en la definición de registro de ingreso aduanero. ‖ tramo (exacta): «No se incluyen los registros aduaneros por importaciones suspensivas de depósitos de almacenamiento»
- Excepcion «Exclusión — importaciones temporarias sin giro de divisas»: No se incluyen los ingresos de importaciones temporarias sin giro de divisas en la definición de registro de ingreso aduanero. ‖ tramo (exacta): «ni los ingresos de importaciones temporarias sin giro de divisas.»
  - Definicion:Registro de ingreso aduanero --establecida_en--> TextoOrdenado:Exterior — Cambios
  - Definicion:Registro aduanero — despacho a plaza por Solicitud Particula… --establecida_en--> TextoOrdenado:Exterior — Cambios
  - Definicion:Registro aduanero — zonas francas nacionales --establecida_en--> TextoOrdenado:Exterior — Cambios
  - Excepcion:Exclusión — importaciones suspensivas de depósitos --establecida_en--> TextoOrdenado:Exterior — Cambios
  - Excepcion:Exclusión — importaciones temporarias sin giro de divisas --establecida_en--> TextoOrdenado:Exterior — Cambios
- hechos: umbrales []; menciones []; omisiones []; condicion_de []; limita []

*Cuantías en el texto propio: 0.*

## Ficha 12 — `ric::11.1.4`

**Texto propio:**

```
11.1.4. Cálculo de la medida de riesgo EVE estandarizada.
Se informarán los siguientes cálculos, teniendo en cuenta el escenario (X= 1 a 6) o la
moneda (M = 001 –pesos– o 010 –dólares estadounidenses–) en los casos en que
estén previstos tales atributos.
• Medida total del riesgo por opciones automáticas (KAO) –partidas 3613000X/M–.
Las entidades del Grupo “A” calcularán el componente adicional por las opcio-
nes automáticas sobre tasas de interés vendidas, ya sean explícitas o implícitas
(punto 5.4.3. de las normas sobre “Lineamientos para la gestión de riesgos en las
entidades financieras”), por cada moneda y por escenario.
• Valor económico del patrimonio –partidas 3612000X/M–.
Mide el valor económico del patrimonio correspondiente a todas las bandas tempo-
rales, para los 6 escenarios en cada moneda significativa (punto 5.4.4.3. de las
normas sobre “Lineamientos para la gestión de riesgos en las entidades financie-
ras”).
No incluye las opciones automáticas sobre tasas de interés.
• Valor económico del patrimonio para el escenario base –partidas 36110000/M–.
Calculado con la estructura de tasas de interés vigentes en el escenario 0 o base
(punto 5.4.4.4. de las normas sobre “Lineamientos para la gestión de riesgos en las
entidades financieras”).
• Variación del valor económico del patrimonio –partida 3610000X/M–.
Surge de restar, para cada moneda, al EVE0 (resultante del escenario 0) el EVE del
escenario de perturbación, según corresponda.
A este valor se le sumará el riesgo de opción automática sobre tasas de interés -
KAO - (punto 5.4.4.4. de las normas sobre “Lineamientos para la gestión de riesgos
en las entidades financieras”).
• Suma de pérdidas por escenario –partida 3650000X–.
Se suman únicamente las pérdidas registradas en las monedas de los diferentes
escenarios, es decir, se obtiene una pérdida agregada por escenario, sin compen-
sar con los resultados positivos. No admite signo negativo (punto 5.4.4.4. de las
normas sobre “Lineamientos para la gestión de riesgos en las entidades financie-
ras”).
Estos cálculos deberán ser consistentes con la información reportada en los cuadros
11.2.1.a) y b), según se trate posiciones en pesos (M=001) o en dólares estadouni-
denses (M=010), respectivamente.
```
**Último bloque heredado:** Conceptos comprendidos. Se incluirán los flujos de fondos nocionales futuros sujetos a reapreciación de activos, pasi- vos y partidas fuera de balance sensibles a variaciones en la tasa de interés. Conceptos excluidos. - Activos que se deducen del capital ordinario del nivel 1 (COn1); - Activos fijo…

**SELLADO** — error: None

- Definicion «Medida total del riesgo por opciones automáticas (KAO)»: Partidas 3613000X/M. Las entidades del Grupo 'A' calcularán el componente adicional por las opciones automáticas sobre tasas de interés vendidas, ya sean explícitas o implícitas (punto 5.4.3. de las normas sobre 'Lineamientos para la gestió…
- Operacion «Cálculo KAO — opciones automáticas sobre tasas»: Cálculo del componente adicional por las opciones automáticas sobre tasas de interés vendidas, ya sean explícitas o implícitas, por cada moneda y por escenario.
- Definicion «Valor económico del patrimonio (EVE)»: Partidas 3612000X/M. Mide el valor económico del patrimonio correspondiente a todas las bandas temporales, para los 6 escenarios en cada moneda significativa (punto 5.4.4.3. de las normas sobre 'Lineamientos para la gestión de riesgos en la…
- Operacion «Cálculo EVE — valor económico del patrimonio»: Cálculo del valor económico del patrimonio correspondiente a todas las bandas temporales, para los 6 escenarios en cada moneda significativa.
- Definicion «Valor económico del patrimonio escenario base (EVE0)»: Partidas 36110000/M. Calculado con la estructura de tasas de interés vigentes en el escenario 0 o base (punto 5.4.4.4. de las normas sobre 'Lineamientos para la gestión de riesgos en las entidades financieras').
- Operacion «Cálculo EVE0 — valor económico escenario base»: Cálculo del valor económico del patrimonio calculado con la estructura de tasas de interés vigentes en el escenario 0 o base.
- Definicion «Variación del valor económico del patrimonio»: Partida 3610000X/M. Surge de restar, para cada moneda, al EVE0 (resultante del escenario 0) el EVE del escenario de perturbación, según corresponda. A este valor se le sumará el riesgo de opción automática sobre tasas de interés - KAO - (pu…
- Operacion «Cálculo variación EVE — resta escenarios»: Cálculo que surge de restar, para cada moneda, al EVE0 el EVE del escenario de perturbación, más la suma del riesgo de opción automática (KAO).
- Definicion «Suma de pérdidas por escenario»: Partida 3650000X. Se suman únicamente las pérdidas registradas en las monedas de los diferentes escenarios, es decir, se obtiene una pérdida agregada por escenario, sin compensar con los resultados positivos. No admite signo negativo (punto…
- Operacion «Cálculo suma pérdidas — agregación por escenario»: Suma únicamente de las pérdidas registradas en las monedas de los diferentes escenarios, sin compensar con los resultados positivos, sin admitir signo negativo.
- Obligacion «Consistencia cálculos — cuadros informativos 11.2.1»: Estos cálculos deberán ser consistentes con la información reportada en los cuadros 11.2.1.a) y b), según se trate posiciones en pesos (M=001) o en dólares estadounidenses (M=010), respectivamente.
- Operacion «Informe de cálculos EVE estandarizada — RIC»: Informe de los cálculos de medida de riesgo EVE estandarizada (KAO, EVE, EVE0, variación EVE, suma pérdidas por escenario) teniendo en cuenta escenarios (X=1 a 6) y monedas (M=001 pesos o M=010 dólares estadounidenses).
- Obligacion «Cálculo KAO — Grupo A por moneda y escenario»: Las entidades del Grupo 'A' calcularán el componente adicional por las opciones automáticas sobre tasas de interés vendidas, ya sean explícitas o implícitas, por cada moneda y por escenario.
  - Definicion:Medida total del riesgo por opciones automáticas (KAO) --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Operacion:Cálculo KAO — opciones automáticas sobre tasas --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Definicion:Valor económico del patrimonio (EVE) --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Operacion:Cálculo EVE — valor económico del patrimonio --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Definicion:Valor económico del patrimonio escenario base (EVE0) --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Operacion:Cálculo EVE0 — valor económico escenario base --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Definicion:Variación del valor económico del patrimonio --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Operacion:Cálculo variación EVE — resta escenarios --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Definicion:Suma de pérdidas por escenario --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Operacion:Cálculo suma pérdidas — agregación por escenario --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Obligacion:Consistencia cálculos — cuadros informativos 11.2.1 --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Operacion:Informe de cálculos EVE estandarizada — RIC --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Obligacion:Cálculo KAO — Grupo A por moneda y escenario --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Operacion:Informe de cálculos EVE estandarizada — RIC --aplica_a--> None
  - Obligacion:Consistencia cálculos — cuadros informativos 11.2.1 --aplica_a--> None
  - Obligacion:Cálculo KAO — Grupo A por moneda y escenario --aplica_a--> None
  - Operacion:Informe de cálculos EVE estandarizada — RIC --requiere--> Obligacion:Consistencia cálculos — cuadros informativos 11.2.1
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}]; omisiones [{"categoria": null, "tramo": "", "verificacion": "ausente", "nota": "Fórmulas de cálculo para EVE estandarizada: estructura de fórmulas detectada (valores de escenarios …"}, {"categoria": null, "tramo": "", "verificacion": "ausente", "nota": "Tabla de partidas/referencias cruzadas (3613000X/M, 3612000X/M, 36110000/M, 3610000X/M, 3650000X): e…"}]; condicion_de []; limita []

**NUEVO** — error: None

- Obligacion «Informar cálculos de medida EVE estandarizada»: Las entidades informarán cálculos de medida de riesgo EVE estandarizada, considerando escenarios (X=1 a 6) y monedas (pesos M=001 o dólares estadounidenses M=010) cuando corresponda. ‖ tramo (exacta): «Se informarán los siguientes cálculos, teniendo en cuenta el escenario (X= 1 a 6) o la moneda (M = 001 –pesos– o 010 –dólares estadounidenses–) en los casos en …»
- Operacion «Cálculo de medida total riesgo opciones automáticas KAO»: Medida total del riesgo por opciones automáticas sobre tasas de interés (KAO) para cada moneda y escenario. ‖ tramo (exacta): «Medida total del riesgo por opciones automáticas (KAO) –partidas 3613000X/M–.»
- Obligacion «Calcular componente opciones automáticas — Grupo A»: Entidades del Grupo A calcularán componente adicional por opciones automáticas sobre tasas de interés vendidas (explícitas o implícitas), por cada moneda y escenario. ‖ tramo (exacta): «Las entidades del Grupo "A" calcularán el componente adicional por las opciones automáticas sobre tasas de interés vendidas, ya sean explícitas o implícitas (pu…»
- Operacion «Cálculo de valor económico del patrimonio»: Valor económico del patrimonio para todas las bandas temporales en 6 escenarios por moneda significativa, sin incluir opciones automáticas sobre tasas de interés. ‖ tramo (exacta): «Valor económico del patrimonio –partidas 3612000X/M–.»
- Operacion «Cálculo valor económico patrimonio escenario base»: Valor económico del patrimonio calculado con la estructura de tasas de interés vigentes en el escenario 0 o base. ‖ tramo (exacta): «Valor económico del patrimonio para el escenario base –partidas 36110000/M–.»
- Operacion «Cálculo variación valor económico patrimonio»: Diferencia entre EVE del escenario 0 y EVE del escenario de perturbación por moneda, más riesgo KAO. ‖ tramo (exacta): «Variación del valor económico del patrimonio –partida 3610000X/M–.»
- Operacion «Cálculo suma pérdidas por escenario»: Suma única de pérdidas por moneda en diferentes escenarios, sin compensar con resultados positivos. ‖ tramo (exacta): «Suma de pérdidas por escenario –partida 3650000X–.»
- Obligacion «Consistencia con cuadros reportados»: Los cálculos de EVE estandarizada deben guardar consistencia con información reportada en cuadros 11.2.1.a) (pesos) y 11.2.1.b) (dólares estadounidenses). ‖ tramo (exacta): «Estos cálculos deberán ser consistentes con la información reportada en los cuadros 11.2.1.a) y b), según se trate posiciones en pesos (M=001) o en dólares esta…»
  - Obligacion:Informar cálculos de medida EVE estandarizada --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Operacion:Cálculo de medida total riesgo opciones automáticas KAO --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Obligacion:Calcular componente opciones automáticas — Grupo A --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Operacion:Cálculo de valor económico del patrimonio --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Operacion:Cálculo valor económico patrimonio escenario base --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Operacion:Cálculo variación valor económico patrimonio --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Operacion:Cálculo suma pérdidas por escenario --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Obligacion:Consistencia con cuadros reportados --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Obligacion:Informar cálculos de medida EVE estandarizada --aplica_a--> las entidades
  - Obligacion:Calcular componente opciones automáticas — Grupo A --aplica_a--> Las entidades del Grupo "A"
  - Obligacion:Consistencia con cuadros reportados --aplica_a--> las entidades
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "las entidades", "verificada": "exacta", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "Las entidades del Grupo \"A\"", "verificada": "exacta", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "las entidades", "verificada": "exacta", "sujeto_id": null}]; omisiones [{"categoria": "formula", "tramo": "Se informarán los siguientes cálculos, teniendo en cuenta el escenario (X= 1 a 6) o la moneda (M = 0…", "verificacion": "exacta", "nota": "Contenido formulaico con parámetros de fórmula (X y M) declarado no confiable por FLAG E0. La estruc…"}, {"categoria": "formula", "tramo": "Surge de restar, para cada moneda, al EVE0 (resultante del escenario 0) el EVE del escenario de pert…", "verificacion": "exacta", "nota": "Contenido de operación matemática (sustracción) no extraído. Se captura la operación en e6 como conc…"}, {"categoria": "formula", "tramo": "A este valor se le sumará el riesgo de opción automática sobre tasas de interés - KAO", "verificacion": "exacta", "nota": "Operación matemática de suma no extraída del contenido no confiable. Se menciona en la descripción d…"}]; condicion_de []; limita []

*Cuantías en el texto propio: 0.*

## Ficha 13 — `ayccef::2.9.3.1`

**Texto propio:**

```
2.9.3.1. Inscripción del estatuto de la sociedad por la autoridad de contralor societario
competente en el Registro Público de la correspondiente jurisdicción.
```
**Último bloque heredado:** Con una antelación no inferior a 30 días corridos a la fecha prevista para la iniciación de actividades, se deberán cumplir las siguientes exigencias:

**SELLADO** — error: None

- Obligacion «Inscripción estatuto en Registro Público jurisdiccional»: Inscripción del estatuto de la sociedad por la autoridad de contralor societario competente en el Registro Público de la correspondiente jurisdicción
  - Obligacion:Inscripción estatuto en Registro Público jurisdiccional --establecida_en--> TextoOrdenado:Autorización de Casas de Cambio y Entidades Financieras
  - Obligacion:Inscripción estatuto en Registro Público jurisdiccional --aplica_a--> None
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}]; omisiones []; condicion_de []; limita []

**NUEVO** — error: None

- Obligacion «Inscripción del estatuto — Registro Público»: Inscribir el estatuto de la sociedad en el Registro Público de la jurisdicción competente, por la autoridad de contralor societario, dentro de los 30 días corridos anteriores a la fecha prevista para la iniciación de actividades. ‖ tramo (exacta): «se deberán cumplir las siguientes exigencias: […] Inscripción del estatuto de la sociedad por la autoridad de contralor societario competente en el Registro Púb…»
  - Obligacion:Inscripción del estatuto — Registro Público --establecida_en--> TextoOrdenado:Autorización y Control de Entidades Financieras
  - Obligacion:Inscripción del estatuto — Registro Público --aplica_a--> las autorizaciones otorgadas
- hechos: umbrales [{"entidad": "Obligacion:Inscripción del estatuto — Registro Público", "tramo": "no inferior a 30 días corridos", "verificacion": "exacta"}]; menciones [{"pred": "aplica_a", "mencion": "las autorizaciones otorgadas", "verificada": "exacta", "sujeto_id": null}]; omisiones []; condicion_de []; limita []

*Cuantías en el texto propio: 0.*

## Ficha 14 — `lingob::6.2.4.3`

**Texto propio:**

```
6.2.4.3. El sistema vincule el monto destinado al pago de incentivos con el desempeño
y el resultado general obtenido por la entidad financiera.
En el caso de entidades financieras con una significativa dimensión, compleji-
dad, importancia económica y perfil de riesgo -considerando el grupo económi-
co al cual pertenezcan-, los incentivos no deberían debilitar la política estable-
cida en materia de mantenimiento y fortalecimiento del capital. En este caso,
esos fondos y su asignación dentro de la entidad tendrán en cuenta el rango
completo de riesgos actuales y potenciales, y en particular:
i) el costo y la cantidad de capital requerido para hacer frente al riesgo asumi-
do;
ii) el costo y el nivel de riesgo de liquidez asumido para llevar adelante el ne-
gocio; y
iii) la probabilidad de que se materialicen los ingresos potenciales y la fecha
estimada de su incorporación a los resultados.
```
**Último bloque heredado:** A fin de que los incentivos económicos conduzcan a una prudente toma de riesgos, se consideran buenas prácticas que:

**SELLADO** — error: None

- Obligacion «Vinculación monto incentivos con desempeño y resultado general»: El sistema vincule el monto destinado al pago de incentivos con el desempeño y el resultado general obtenido por la entidad financiera.
- Condicion «Entidades financieras con dimensión significativa y perfil de riesgo»: En caso de entidades financieras con una significativa dimensión, complejidad, importancia económica y perfil de riesgo, considerando el grupo económico al cual pertenezcan
- Restriccion «Incentivos no debilitarán política de capital»: Los incentivos no deberían debilitar la política establecida en materia de mantenimiento y fortalecimiento del capital.
- Obligacion «Asignación de fondos considerará rango completo de riesgos»: Los fondos y su asignación dentro de la entidad tendrán en cuenta el rango completo de riesgos actuales y potenciales.
- Obligacion «Consideración del costo y cantidad de capital requerido»: La asignación de fondos tendrá en cuenta el costo y la cantidad de capital requerido para hacer frente al riesgo asumido.
- Obligacion «Consideración del costo y nivel de riesgo de liquidez»: La asignación de fondos tendrá en cuenta el costo y el nivel de riesgo de liquidez asumido para llevar adelante el negocio.
- Obligacion «Consideración de probabilidad e incorporación de ingresos potenciales»: La asignación de fondos tendrá en cuenta la probabilidad de que se materialicen los ingresos potenciales y la fecha estimada de su incorporación a los resultados.
- Operacion «Pago de incentivos económicos al personal»: Pago de incentivos económicos al personal vinculado con desempeño y resultado general.
  - Obligacion:Vinculación monto incentivos con desempeño y resultado gener… --establecida_en--> TextoOrdenado:Política de incentivos económicos al personal
  - Condicion:Entidades financieras con dimensión significativa y perfil d… --establecida_en--> TextoOrdenado:Política de incentivos económicos al personal
  - Restriccion:Incentivos no debilitarán política de capital --establecida_en--> TextoOrdenado:Política de incentivos económicos al personal
  - Obligacion:Asignación de fondos considerará rango completo de riesgos --establecida_en--> TextoOrdenado:Política de incentivos económicos al personal
  - Obligacion:Consideración del costo y cantidad de capital requerido --establecida_en--> TextoOrdenado:Política de incentivos económicos al personal
  - Obligacion:Consideración del costo y nivel de riesgo de liquidez --establecida_en--> TextoOrdenado:Política de incentivos económicos al personal
  - Obligacion:Consideración de probabilidad e incorporación de ingresos po… --establecida_en--> TextoOrdenado:Política de incentivos económicos al personal
  - Operacion:Pago de incentivos económicos al personal --establecida_en--> TextoOrdenado:Política de incentivos económicos al personal
  - Obligacion:Vinculación monto incentivos con desempeño y resultado gener… --aplica_a--> None
  - Restriccion:Incentivos no debilitarán política de capital --aplica_a--> None
  - Obligacion:Asignación de fondos considerará rango completo de riesgos --aplica_a--> None
  - Obligacion:Consideración del costo y cantidad de capital requerido --aplica_a--> None
  - Obligacion:Consideración del costo y nivel de riesgo de liquidez --aplica_a--> None
  - Obligacion:Consideración de probabilidad e incorporación de ingresos po… --aplica_a--> None
  - Condicion:Entidades financieras con dimensión significativa y perfil d… --condicion_de--> Restriccion:Incentivos no debilitarán política de capital
  - Condicion:Entidades financieras con dimensión significativa y perfil d… --condicion_de--> Obligacion:Asignación de fondos considerará rango completo de riesgos
  - Condicion:Entidades financieras con dimensión significativa y perfil d… --condicion_de--> Obligacion:Consideración del costo y cantidad de capital requerido
  - Condicion:Entidades financieras con dimensión significativa y perfil d… --condicion_de--> Obligacion:Consideración del costo y nivel de riesgo de liquidez
  - Condicion:Entidades financieras con dimensión significativa y perfil d… --condicion_de--> Obligacion:Consideración de probabilidad e incorporación de ingresos po…
  - Obligacion:Vinculación monto incentivos con desempeño y resultado gener… --regula--> Operacion:Pago de incentivos económicos al personal
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}]; omisiones []; condicion_de [{"de": "Condicion:Entidades financieras con dimensión significativa y perfil d…", "a": "Restriccion:Incentivos no debilitarán política de capital", "firma_nueva": false}, {"de": "Condicion:Entidades financieras con dimensión significativa y perfil d…", "a": "Obligacion:Asignación de fondos considerará rango completo de riesgos", "firma_nueva": false}, {"de": "Condicion:Entidades financieras con dimensión significativa y perfil d…", "a": "Obligacion:Consideración del costo y cantidad de capital requerido", "firma_nueva": false}, {"de": "Condicion:Entidades financieras con dimensión significativa y perfil d…", "a": "Obligacion:Consideración del costo y nivel de riesgo de liquidez", "firma_nueva": false}, {"de": "Condicion:Entidades financieras con dimensión significativa y perfil d…", "a": "Obligacion:Consideración de probabilidad e incorporación de ingresos po…", "firma_nueva": false}]; limita []

**NUEVO** — error: None

- Obligacion «Vinculación de incentivos con desempeño»: Es una recomendación de buena práctica (no un deber mandatorio): el sistema de incentivos debe vincular el monto destinado al pago de incentivos con el desempeño y el resultado general obtenido por la entidad financiera. ‖ tramo (exacta): «El sistema vincule el monto destinado al pago de incentivos con el desempeño y el resultado general obtenido por la entidad financiera» ‖ no definidas: {"modalidad": "se consideran buenas prácticas que", "modalidad_clasificada": "recomendacion"}
- Restriccion «Incentivos no debiliten capital — entidades complejas»: Para entidades financieras con significativa dimensión, complejidad, importancia económica y perfil de riesgo (considerando el grupo económico al cual pertenezcan), los incentivos no deben debilitar la política establecida en materia de man… ‖ tramo (exacta): «los incentivos no deberían debilitar la política establecida en materia de mantenimiento y fortalecimiento del capital»
- Condicion «Condición: entidades con significativa dimensión»: Supuesto que activa la exigencia de que los incentivos no debiliten la política de capital: que la entidad financiera tenga significativa dimensión, complejidad, importancia económica y perfil de riesgo, considerando el grupo económico al c… ‖ tramo (exacta): «En el caso de entidades financieras con una significativa dimensión, complejidad, importancia económica y perfil de riesgo -considerando el grupo económico al c…»
- Obligacion «Consideración de riesgos en fondos de incentivos»: Para entidades financieras complejas, los fondos de incentivos y su asignación dentro de la entidad deberán tener en cuenta el rango completo de riesgos actuales y potenciales, incluyendo tres aspectos específicos. ‖ tramo (exacta): «esos fondos y su asignación dentro de la entidad tendrán en cuenta el rango completo de riesgos actuales y potenciales»
- Obligacion «Consideración de costo y capital del riesgo»: En la asignación de fondos de incentivos, se debe considerar el costo y la cantidad de capital requerido para hacer frente al riesgo asumido. ‖ tramo (exacta): «el costo y la cantidad de capital requerido para hacer frente al riesgo asumido»
- Obligacion «Consideración de riesgo de liquidez»: En la asignación de fondos de incentivos, se debe considerar el costo y el nivel de riesgo de liquidez asumido para llevar adelante el negocio. ‖ tramo (exacta): «el costo y el nivel de riesgo de liquidez asumido para llevar adelante el negocio»
- Obligacion «Consideración de probabilidad de materialización de ingresos»: En la asignación de fondos de incentivos, se debe considerar la probabilidad de que se materialicen los ingresos potenciales y la fecha estimada de su incorporación a los resultados. ‖ tramo (exacta): «la probabilidad de que se materialicen los ingresos potenciales y la fecha estimada de su incorporación a los resultados»
  - Obligacion:Vinculación de incentivos con desempeño --establecida_en--> TextoOrdenado:TO Política de incentivos económicos
  - Obligacion:Vinculación de incentivos con desempeño --aplica_a--> la entidad financiera
  - Restriccion:Incentivos no debiliten capital — entidades complejas --establecida_en--> TextoOrdenado:TO Política de incentivos económicos
  - Restriccion:Incentivos no debiliten capital — entidades complejas --aplica_a--> entidades financieras con una significativa dimensión, complejidad, importancia económica y perfil de riesgo
  - Condicion:Condición: entidades con significativa dimensión --condicion_de--> Restriccion:Incentivos no debiliten capital — entidades complejas
  - Condicion:Condición: entidades con significativa dimensión --establecida_en--> TextoOrdenado:TO Política de incentivos económicos
  - Obligacion:Consideración de riesgos en fondos de incentivos --establecida_en--> TextoOrdenado:TO Política de incentivos económicos
  - Obligacion:Consideración de riesgos en fondos de incentivos --aplica_a--> entidades financieras con una significativa dimensión, complejidad, importancia económica y perfil de riesgo
  - Condicion:Condición: entidades con significativa dimensión --condicion_de--> Obligacion:Consideración de riesgos en fondos de incentivos
  - Obligacion:Consideración de costo y capital del riesgo --establecida_en--> TextoOrdenado:TO Política de incentivos económicos
  - Obligacion:Consideración de costo y capital del riesgo --aplica_a--> entidades financieras con una significativa dimensión, complejidad, importancia económica y perfil de riesgo
  - Condicion:Condición: entidades con significativa dimensión --condicion_de--> Obligacion:Consideración de costo y capital del riesgo
  - Obligacion:Consideración de riesgo de liquidez --establecida_en--> TextoOrdenado:TO Política de incentivos económicos
  - Obligacion:Consideración de riesgo de liquidez --aplica_a--> entidades financieras con una significativa dimensión, complejidad, importancia económica y perfil de riesgo
  - Condicion:Condición: entidades con significativa dimensión --condicion_de--> Obligacion:Consideración de riesgo de liquidez
  - Obligacion:Consideración de probabilidad de materialización de ingresos --establecida_en--> TextoOrdenado:TO Política de incentivos económicos
  - Obligacion:Consideración de probabilidad de materialización de ingresos --aplica_a--> entidades financieras con una significativa dimensión, complejidad, importancia económica y perfil de riesgo
  - Condicion:Condición: entidades con significativa dimensión --condicion_de--> Obligacion:Consideración de probabilidad de materialización de ingresos
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "la entidad financiera", "verificada": "exacta", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "entidades financieras con una significativa dimensión, complejidad, importancia …", "verificada": "exacta", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "entidades financieras con una significativa dimensión, complejidad, importancia …", "verificada": "exacta", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "entidades financieras con una significativa dimensión, complejidad, importancia …", "verificada": "exacta", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "entidades financieras con una significativa dimensión, complejidad, importancia …", "verificada": "exacta", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "entidades financieras con una significativa dimensión, complejidad, importancia …", "verificada": "exacta", "sujeto_id": null}]; omisiones []; condicion_de [{"de": "Condicion:Condición: entidades con significativa dimensión", "a": "Restriccion:Incentivos no debiliten capital — entidades complejas", "firma_nueva": false}, {"de": "Condicion:Condición: entidades con significativa dimensión", "a": "Obligacion:Consideración de riesgos en fondos de incentivos", "firma_nueva": false}, {"de": "Condicion:Condición: entidades con significativa dimensión", "a": "Obligacion:Consideración de costo y capital del riesgo", "firma_nueva": false}, {"de": "Condicion:Condición: entidades con significativa dimensión", "a": "Obligacion:Consideración de riesgo de liquidez", "firma_nueva": false}, {"de": "Condicion:Condición: entidades con significativa dimensión", "a": "Obligacion:Consideración de probabilidad de materialización de ingresos", "firma_nueva": false}]; limita []

*Cuantías en el texto propio: 0.*

## Ficha 15 — `cap::3.1.14::intro`

**Texto propio:**

```
A los fines de establecer el ponderador de riesgo a aplicar de acuerdo con el enfoque
estandarizado –punto 3.1.11.–, una titulización se considerará simple, transparente y
comparable (STC) si:
-se trata de una titulización tradicional que no constituye un programa ABCP;
- involucra una transferencia real de activos –en los términos del acápite v) del punto
3.1.14.1.–; y
- cumple con la totalidad de los criterios previstos en el presente punto (en adelante,
“criterios STC”).
El originante/fiduciario deberá divulgar toda la información necesaria respecto de la
transacción que permita a los inversores determinar si la titulización cumple con los cri-
terios STC. En base a la información provista, el inversor deberá realizar sus propias
evaluaciones respecto del cumplimiento de estos criterios previo a la aplicación del en-
foque estandarizado.
Para las posiciones retenidas en las que el originante haya transferido el riesgo de
acuerdo con lo establecido en los puntos 3.1.2.2. y 3.1.8.2. la determinación respecto
del cumplimiento de los criterios será efectuada únicamente por la entidad originante.
Los criterios STC deberán cumplirse en todo momento. Algunos de los criterios se de-
berán verificar sólo al momento de la originación o cuando se genere la posición –si és-
ta es posterior–, tal como en el caso de las garantías y las facilidades de liquidez. No
obstante, los inversores y tenedores de las posiciones de titulización deberán tener en
cuenta las modificaciones que puedan invalidar las evaluaciones de cumplimiento pre-
vias, tales como las deficiencias en la frecuencia y en el contenido de los informes a los
inversores o los cambios en la documentación contrarios a los criterios STC.
En los casos en que los criterios hagan referencia a activos subyacentes –incluidos los
criterios previstos en el punto 3.1.14.4.– y el conjunto de subyacentes admita la incorpo-
ración de nuevos activos, el cumplimiento estará sujeto a que se realicen verificaciones
cada vez que se incorporen esos nuevos activos.
Cuando la SEFyC detecte que una titulización no cumple con alguno de los criterios,
podrá exigir la implementación de acciones correctivas y/o determinar que se suspenda
el tratamiento STC para una o más posiciones de titulización.
```
**Último bloque heredado:** 3.1.14. Criterios para la determinación de titulizaciones simples, transparentes y comparables.

**SELLADO** — error: None

- Definicion «Titulización STC — definición con criterios»: Una titulización se considerará simple, transparente y comparable (STC) si: (i) se trata de una titulización tradicional que no constituye un programa ABCP; (ii) involucra una transferencia real de activos en los términos del acápite v) del…
- Obligacion «Divulgación de información STC por originante/fiduciario»: El originante/fiduciario deberá divulgar toda la información necesaria respecto de la transacción que permita a los inversores determinar si la titulización cumple con los criterios STC.
- Obligacion «Evaluación propia de cumplimiento STC por inversor»: En base a la información provista, el inversor deberá realizar sus propias evaluaciones respecto del cumplimiento de los criterios STC previo a la aplicación del enfoque estandarizado.
- Restriccion «Cumplimiento continuo de criterios STC»: Los criterios STC deberán cumplirse en todo momento.
- Obligacion «Determinación STC solo por originante (posiciones retenidas con transferencia de…»: Para las posiciones retenidas en las que el originante haya transferido el riesgo de acuerdo con lo establecido en los puntos 3.1.2.2. y 3.1.8.2., la determinación respecto del cumplimiento de los criterios será efectuada únicamente por la …
- Condicion «Verificación al momento de originación o generación de posición»: Algunos de los criterios se deberán verificar sólo al momento de la originación o cuando se genere la posición (si ésta es posterior), tal como en el caso de las garantías y las facilidades de liquidez.
- Obligacion «Consideración de modificaciones invalidantes por inversores y tenedores»: Los inversores y tenedores de las posiciones de titulización deberán tener en cuenta las modificaciones que puedan invalidar las evaluaciones de cumplimiento previas, tales como las deficiencias en la frecuencia y en el contenido de los inf…
- Condicion «Verificación de nuevos activos incorporados»: En los casos en que los criterios hagan referencia a activos subyacentes (incluidos los criterios previstos en el punto 3.1.14.4.) y el conjunto de subyacentes admita la incorporación de nuevos activos, el cumplimiento estará sujeto a que s…
- Potestad «Exigencia de acciones correctivas por SEFyC ante incumplimiento STC»: Cuando la SEFyC detecte que una titulización no cumple con alguno de los criterios, podrá exigir la implementación de acciones correctivas.
- Potestad «Suspensión del tratamiento STC por SEFyC»: Cuando la SEFyC detecte que una titulización no cumple con alguno de los criterios, podrá determinar que se suspenda el tratamiento STC para una o más posiciones de titulización.
  - Definicion:Titulización STC — definición con criterios --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Obligacion:Divulgación de información STC por originante/fiduciario --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Obligacion:Evaluación propia de cumplimiento STC por inversor --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Restriccion:Cumplimiento continuo de criterios STC --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Obligacion:Determinación STC solo por originante (posiciones retenidas … --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Condicion:Verificación al momento de originación o generación de posic… --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Obligacion:Consideración de modificaciones invalidantes por inversores … --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Condicion:Verificación de nuevos activos incorporados --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Potestad:Exigencia de acciones correctivas por SEFyC ante incumplimie… --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Potestad:Suspensión del tratamiento STC por SEFyC --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Obligacion:Divulgación de información STC por originante/fiduciario --aplica_a--> originante/fiduciario
  - Obligacion:Evaluación propia de cumplimiento STC por inversor --aplica_a--> inversor
  - Restriccion:Cumplimiento continuo de criterios STC --aplica_a--> None
  - Obligacion:Determinación STC solo por originante (posiciones retenidas … --aplica_a--> originante
  - Obligacion:Consideración de modificaciones invalidantes por inversores … --aplica_a--> inversores y tenedores
  - Potestad:Exigencia de acciones correctivas por SEFyC ante incumplimie… --aplica_a--> None
  - Potestad:Suspensión del tratamiento STC por SEFyC --aplica_a--> None
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "originante/fiduciario", "verificada": "exacta", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "inversor", "verificada": "exacta", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "originante", "verificada": "exacta", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "inversores y tenedores", "verificada": "exacta", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}]; omisiones []; condicion_de []; limita []

**NUEVO** — error: None

- Definicion «Titulización simple, transparente y comparable (STC)»: Titulización que es tradicional (no programa ABCP), involucra transferencia real de activos y cumple con la totalidad de los criterios STC previstos en el punto 3.1.14 ‖ tramo (exacta): «una titulización se considerará simple, transparente y comparable (STC) si: -se trata de una titulización tradicional que no constituye un programa ABCP; - invo…»
- Obligacion «Divulgación información transacción — originante/fiduciario»: El originante/fiduciario debe divulgar toda la información necesaria sobre la transacción que permita a los inversores determinar si la titulización cumple con los criterios STC ‖ tramo (exacta): «El originante/fiduciario deberá divulgar toda la información necesaria respecto de la transacción que permita a los inversores determinar si la titulización cum…»
- Obligacion «Evaluaciones propias — inversor cumplimiento criterios STC»: El inversor debe realizar sus propias evaluaciones sobre el cumplimiento de los criterios STC previo a la aplicación del enfoque estandarizado, en base a la información provista ‖ tramo (exacta): «el inversor deberá realizar sus propias evaluaciones respecto del cumplimiento de estos criterios previo a la aplicación del enfoque estandarizado»
- Obligacion «Determinación cumplimiento criterios — posiciones retenidas con transferencia ri…»: Para posiciones retenidas en que el originante haya transferido el riesgo según puntos 3.1.2.2 y 3.1.8.2, la determinación del cumplimiento de criterios STC será efectuada únicamente por la entidad originante ‖ tramo (exacta): «Para las posiciones retenidas en las que el originante haya transferido el riesgo de acuerdo con lo establecido en los puntos 3.1.2.2. y 3.1.8.2. la determinaci…»
- Restriccion «Cumplimiento continuo — criterios STC»: Los criterios STC deben cumplirse en todo momento, sin excepción temporal ‖ tramo (exacta): «Los criterios STC deberán cumplirse en todo momento»
- Condicion «Verificación al momento originación o generación posición»: Ciertos criterios solo deben verificarse al momento de la originación o cuando se genera la posición (si es posterior), como en el caso de garantías y facilidades de liquidez ‖ tramo (exacta): «Algunos de los criterios se deberán verificar sólo al momento de la originación o cuando se genere la posición –si ésta es posterior–, tal como en el caso de la…»
- Obligacion «Consideración modificaciones — inversores y tenedores posiciones»: Los inversores y tenedores de posiciones de titulización deben tener en cuenta modificaciones que puedan invalidar evaluaciones previas de cumplimiento, como deficiencias en frecuencia/contenido de informes o cambios en documentación contra… ‖ tramo (exacta): «los inversores y tenedores de las posiciones de titulización deberán tener en cuenta las modificaciones que puedan invalidar las evaluaciones de cumplimiento pr…»
- Condicion «Incorporación nuevos activos subyacentes — verificaciones»: Cuando criterios refieren activos subyacentes (incluido 3.1.14.4) y se pueden incorporar nuevos activos, el cumplimiento requiere verificaciones cada vez que se incorporen nuevos activos ‖ tramo (exacta): «En los casos en que los criterios hagan referencia a activos subyacentes –incluidos los criterios previstos en el punto 3.1.14.4.– y el conjunto de subyacentes …»
- Potestad «Acciones correctivas — SEFyC incumplimiento criterios»: La SEFyC, cuando detecte incumplimiento de criterios, puede exigir acciones correctivas y/o determinar la suspensión del tratamiento STC para una o más posiciones de titulización ‖ tramo (exacta): «Cuando la SEFyC detecte que una titulización no cumple con alguno de los criterios, podrá exigir la implementación de acciones correctivas y/o determinar que se…»
  - Definicion:Titulización simple, transparente y comparable (STC) --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Obligacion:Divulgación información transacción — originante/fiduciario --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Obligacion:Divulgación información transacción — originante/fiduciario --aplica_a--> El originante/fiduciario
  - Obligacion:Evaluaciones propias — inversor cumplimiento criterios STC --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Obligacion:Evaluaciones propias — inversor cumplimiento criterios STC --aplica_a--> el inversor
  - Obligacion:Determinación cumplimiento criterios — posiciones retenidas … --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Obligacion:Determinación cumplimiento criterios — posiciones retenidas … --aplica_a--> la entidad originante
  - Restriccion:Cumplimiento continuo — criterios STC --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Condicion:Verificación al momento originación o generación posición --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Obligacion:Consideración modificaciones — inversores y tenedores posici… --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Obligacion:Consideración modificaciones — inversores y tenedores posici… --aplica_a--> los inversores y tenedores de las posiciones de titulización
  - Condicion:Incorporación nuevos activos subyacentes — verificaciones --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Potestad:Acciones correctivas — SEFyC incumplimiento criterios --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Potestad:Acciones correctivas — SEFyC incumplimiento criterios --aplica_a--> la SEFyC
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "El originante/fiduciario", "verificada": "exacta", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "el inversor", "verificada": "exacta", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "la entidad originante", "verificada": "exacta", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "los inversores y tenedores de las posiciones de titulización", "verificada": "exacta", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "la SEFyC", "verificada": "exacta", "sujeto_id": null}]; omisiones [{"categoria": "meta_normativo", "tramo": "A los fines de establecer el ponderador de riesgo a aplicar de acuerdo con el enfoque estandarizado …", "verificacion": "exacta", "nota": "Cláusula que declara el propósito/contexto de la norma (establecimiento de ponderador de riesgo), no…"}]; condicion_de []; limita []

*Cuantías en el texto propio: 0.*

## Ficha 16 — `pro::1.1.2.5`

**Texto propio:**

```
1.1.2.5. Otros proveedores no financieros de crédito alcanzados por las normas sobre
“Proveedores no financieros de crédito”, excepto que se trate de asociaciones
mutuales o cooperativas, por las financiaciones que otorguen.
```
**Último bloque heredado:** 1.1.2. Sujetos obligados.

**SELLADO** — error: None

- Definicion «Otros proveedores no financieros de crédito alcanzados»: Otros proveedores no financieros de crédito alcanzados por las normas sobre 'Proveedores no financieros de crédito', excepto que se trate de asociaciones mutuales o cooperativas, por las financiaciones que otorguen.
- Excepcion «Exclusión asociaciones mutuales o cooperativas»: Excepto que se trate de asociaciones mutuales o cooperativas
  - Definicion:Otros proveedores no financieros de crédito alcanzados --establecida_en--> TextoOrdenado:Protección de usuarios servicios financieros
  - Excepcion:Exclusión asociaciones mutuales o cooperativas --establecida_en--> TextoOrdenado:Protección de usuarios servicios financieros
  - rechazo: firma_invalida: relations[2]: Excepcion --exceptua_obligacion--> Definicion
  - rechazo: firma_invalida: relations[3]: Definicion --aplica_a--> Sujeto
- hechos: umbrales []; menciones []; omisiones []; condicion_de []; limita []

**NUEVO** — error: None

- Definicion «Otros proveedores no financieros de crédito alcanzados»: Otros proveedores no financieros de crédito que se sujetan a las normas sobre proveedores no financieros de crédito, con excepción de asociaciones mutuales o cooperativas, respecto de las financiaciones que otorguen. ‖ tramo (exacta): «Otros proveedores no financieros de crédito alcanzados por las normas sobre "Proveedores no financieros de crédito", excepto que se trate de asociaciones mutual…»
- Excepcion «Excepción asociaciones mutuales cooperativas»: No se aplican a asociaciones mutuales o cooperativas las normas sobre proveedores no financieros de crédito. ‖ tramo (exacta): «excepto que se trate de asociaciones mutuales o cooperativas»
  - Definicion:Otros proveedores no financieros de crédito alcanzados --establecida_en--> TextoOrdenado:Protección de usuarios servicios financieros
  - Excepcion:Excepción asociaciones mutuales cooperativas --establecida_en--> TextoOrdenado:Protección de usuarios servicios financieros
- hechos: umbrales []; menciones []; omisiones [{"categoria": "relacion_sin_predicado", "tramo": "excepto que se trate de asociaciones mutuales o cooperativas, por las financiaciones que otorguen", "verificacion": "exacta", "nota": "relación entre la Excepcion (e2) y la Definicion (e1): la excepción especifica qué entidades no son …"}]; condicion_de []; limita []

*Cuantías en el texto propio: 0.*

## Ficha 17 — `ext::3.16.2.2`

**Texto propio:**

```
3.16.2.2. Se compromete a liquidar en el mercado de cambios, dentro de los 5
(cinco) días hábiles de su puesta a disposición, aquellos fondos que reciba
en el exterior originados en el cobro de préstamos otorgados a terceros, el
cobro de un depósito a plazo o de la venta de cualquier tipo de activo,
cuando el activo hubiera sido adquirido, el depósito constituido o el
préstamo otorgado con posterioridad al 28/05/20.
```
**Último bloque heredado:** de tarjetas de crédito, de compra, de débito o prepagas emitidas en el país.

**SELLADO** — error: None

- Operacion «Liquidación en mercado de cambios»: Liquidar en el mercado de cambios fondos recibidos en el exterior originados en cobro de préstamos otorgados a terceros, cobro de depósito a plazo o venta de activos, cuando el activo hubiera sido adquirido, depósito constituido o préstamo …
- Obligacion «Comprometerse a liquidar en 5 días hábiles»: Se compromete a liquidar en el mercado de cambios, dentro de los 5 (cinco) días hábiles de su puesta a disposición, aquellos fondos que reciba en el exterior originados en el cobro de préstamos otorgados a terceros, el cobro de un depósito …
- Condicion «Activo adquirido/depósito/préstamo posterior a 28/05/20»: Cuando el activo hubiera sido adquirido, el depósito constituido o el préstamo otorgado con posterioridad al 28/05/20
  - Obligacion:Comprometerse a liquidar en 5 días hábiles --establecida_en--> TextoOrdenado:Exterior cambios
  - Operacion:Liquidación en mercado de cambios --establecida_en--> TextoOrdenado:Exterior cambios
  - Condicion:Activo adquirido/depósito/préstamo posterior a 28/05/20 --establecida_en--> TextoOrdenado:Exterior cambios
  - Operacion:Liquidación en mercado de cambios --requiere--> Obligacion:Comprometerse a liquidar en 5 días hábiles
  - Obligacion:Comprometerse a liquidar en 5 días hábiles --condiciona--> Operacion:Liquidación en mercado de cambios
  - Condicion:Activo adquirido/depósito/préstamo posterior a 28/05/20 --condicion_de--> Obligacion:Comprometerse a liquidar en 5 días hábiles
  - Obligacion:Comprometerse a liquidar en 5 días hábiles --aplica_a--> None
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}]; omisiones []; condicion_de [{"de": "Condicion:Activo adquirido/depósito/préstamo posterior a 28/05/20", "a": "Obligacion:Comprometerse a liquidar en 5 días hábiles", "firma_nueva": false}]; limita []

**NUEVO** — error: None

- Obligacion «Liquidar fondos en mercado de cambios — 5 días hábiles»: La entidad se compromete a liquidar en el mercado de cambios aquellos fondos que reciba en el exterior originados en el cobro de préstamos otorgados a terceros, el cobro de un depósito a plazo o de la venta de cualquier tipo de activo, dent… ‖ tramo (exacta): «Se compromete a liquidar en el mercado de cambios, dentro de los 5 (cinco) días hábiles de su puesta a disposición, aquellos fondos que reciba en el exterior or…»
- Condicion «Activo adquirido, depósito constituido o préstamo otorgado después del 28/05/20»: El acto debe realizarse cuando el activo hubiera sido adquirido, el depósito constituido o el préstamo otorgado con posterioridad al 28 de mayo de 2020. ‖ tramo (exacta): «cuando el activo hubiera sido adquirido, el depósito constituido o el préstamo otorgado con posterioridad al 28/05/20»
- Operacion «Liquidación en mercado de cambios de fondos del exterior»: Liquidación en el mercado de cambios de fondos que la entidad recibe en el exterior, originados en: cobro de préstamos otorgados a terceros, cobro de un depósito a plazo, o venta de activos. ‖ tramo (no): «liquidar en el mercado de cambios [...] aquellos fondos que reciba en el exterior originados en el cobro de préstamos otorgados a terceros, el cobro de un depós…»
  - Obligacion:Liquidar fondos en mercado de cambios — 5 días hábiles --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Condicion:Activo adquirido, depósito constituido o préstamo otorgado d… --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Operacion:Liquidación en mercado de cambios de fondos del exterior --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Condicion:Activo adquirido, depósito constituido o préstamo otorgado d… --condicion_de--> Obligacion:Liquidar fondos en mercado de cambios — 5 días hábiles
  - Obligacion:Liquidar fondos en mercado de cambios — 5 días hábiles --condiciona--> Operacion:Liquidación en mercado de cambios de fondos del exterior
  - Obligacion:Liquidar fondos en mercado de cambios — 5 días hábiles --aplica_a--> La entidad
- hechos: umbrales [{"entidad": "Obligacion:Liquidar fondos en mercado de cambios — 5 días hábiles", "tramo": "dentro de los 5 (cinco) días hábiles", "verificacion": "exacta"}, {"entidad": "Condicion:Activo adquirido, depósito constituido o préstamo otorgado d…", "tramo": "con posterioridad al 28/05/20", "verificacion": "exacta"}]; menciones [{"pred": "aplica_a", "mencion": "La entidad", "verificada": "exacta", "sujeto_id": null}]; omisiones []; condicion_de [{"de": "Condicion:Activo adquirido, depósito constituido o préstamo otorgado d…", "a": "Obligacion:Liquidar fondos en mercado de cambios — 5 días hábiles", "firma_nueva": false}]; limita []

*Cuantías en el texto propio: 1.*

## Ficha 18 — `ctacte::6.1.3.6`

**Texto propio:**

```
6.1.3.6. Orden judicial (medidas cautelares, cierre de la cuenta, etc.).
```
**Último bloque heredado:** Se define como tales a los que generan la imposibilidad de proceder al pago de un che- que o que no existían o eran desconocidos por el librador al momento de su emisión. En forma taxativa, ellos son:

**SELLADO** — error: None

- Operacion «Rechazo de cheque por orden judicial»: Rechazo de cheque en virtud de orden judicial (medidas cautelares, cierre de la cuenta, etc.)
- Obligacion «Aplicar causal de rechazo por orden judicial»: Las entidades deben rechazar cheques cuando existe una orden judicial, incluyendo medidas cautelares, cierre de la cuenta u otras ordenes judiciales
  - Obligacion:Aplicar causal de rechazo por orden judicial --establecida_en--> TextoOrdenado:Texto Ordenado Cuentas de Corresponsalía
  - Obligacion:Aplicar causal de rechazo por orden judicial --aplica_a--> None
  - Obligacion:Aplicar causal de rechazo por orden judicial --regula--> Operacion:Rechazo de cheque por orden judicial
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}]; omisiones []; condicion_de []; limita []

**NUEVO** — error: None

- Operacion «Orden judicial — generando rechazo de cheque»: Causal de rechazo de cheque generada por orden judicial, que incluye medidas cautelares, cierre de la cuenta y casos análogos ‖ tramo (exacta): «Orden judicial (medidas cautelares, cierre de la cuenta, etc.)»
  - Operacion:Orden judicial — generando rechazo de cheque --establecida_en--> TextoOrdenado:Cuentas corrientes
- hechos: umbrales []; menciones []; omisiones []; condicion_de []; limita []

*Cuantías en el texto propio: 0.*

## Ficha 19 — `polcre::7.1::intro`

**Texto propio:**

```
Se encuentran comprendidos en la categoría de “Grandes empresas exportadoras” los clientes
del sector privado no financiero que reúnan concurrentemente las siguientes condiciones:
```
**Último bloque heredado:** 7.1. Clientes comprendidos.

**SELLADO** — error: None

- Definicion «Grandes empresas exportadoras — definición»: Se encuentran comprendidos en la categoría de 'Grandes empresas exportadoras' los clientes del sector privado no financiero que reúnan concurrentemente las siguientes condiciones
- Condicion «Condiciones concurrentes para Grandes empresas exportadoras»: reúnan concurrentemente las siguientes condiciones
  - Definicion:Grandes empresas exportadoras — definición --establecida_en--> TextoOrdenado:Política de Crédito
  - Condicion:Condiciones concurrentes para Grandes empresas exportadoras --establecida_en--> TextoOrdenado:Política de Crédito
  - rechazo: firma_invalida: relations[2]: Definicion --aplica_a--> Sujeto
- hechos: umbrales []; menciones []; omisiones []; condicion_de []; limita []

**NUEVO** — error: None

- Definicion «Grandes empresas exportadoras — clientes comprendidos»: Clientes del sector privado no financiero que reúnan concurrentemente las siguientes condiciones ‖ tramo (exacta): «Se encuentran comprendidos en la categoría de "Grandes empresas exportadoras" los clientes del sector privado no financiero que reúnan concurrentemente las sigu…»
  - Definicion:Grandes empresas exportadoras — clientes comprendidos --establecida_en--> TextoOrdenado:Financiaciones a Grandes empresas exportadoras
  - rechazo: firma_invalida: relations[1]: Definicion --aplica_a--> Sujeto
- hechos: umbrales []; menciones []; omisiones [{"categoria": "meta_normativo", "tramo": "que reúnan concurrentemente las siguientes condiciones:", "verificacion": "exacta", "nota": "Anuncio de ítems enumerados que seguirán en el punto; contenido meta-estructural que predica sobre l…"}]; condicion_de []; limita []

*Cuantías en el texto propio: 0.*

## Ficha 20 — `ext::2.7::cierre`

**Texto propio:**

```
A los efectos del registro de estas operaciones se deberán confeccionar dos boletos sin
movimiento de pesos, por los conceptos de compra y venta que correspondan, computándose
el monto por el cual se utiliza este mecanismo a los efectos de los límites mensuales que
pudieran ser aplicables según el caso.
En todos los casos se deberá contar con una declaración jurada del cliente en la que deja
constancia de tener conocimiento de que los fondos que se aplican bajo esta modalidad serán
computados a los efectos del cálculo de los límites que normativamente correspondan al
concepto de venta de cambio que corresponda y que no los excede.
```
**Último bloque heredado:** 2.7. Otras excepciones a la obligación de liquidación.

**SELLADO** — error: None

- Operacion «Confección de boletos sin movimiento de pesos»: Confección de dos boletos sin movimiento de pesos por los conceptos de compra y venta que correspondan
- Obligacion «Confeccionar dos boletos sin movimiento»: A los efectos del registro de estas operaciones se deberán confeccionar dos boletos sin movimiento de pesos, por los conceptos de compra y venta que correspondan
- Restriccion «Límite mensual computable para modalidad de boletos»: El monto por el cual se utiliza este mecanismo se computa a los efectos de los límites mensuales que pudieran ser aplicables según el caso
- Obligacion «Declaración jurada de cliente sobre fondos aplicados»: En todos los casos se deberá contar con una declaración jurada del cliente en la que deja constancia de tener conocimiento de que los fondos que se aplican bajo esta modalidad serán computados a los efectos del cálculo de los límites que no…
- Condicion «Fondos aplicados bajo modalidad de boletos sin movimiento»: Que los fondos que se aplican bajo esta modalidad sean computados a los efectos del cálculo de los límites que normativamente correspondan al concepto de venta de cambio
  - Obligacion:Confeccionar dos boletos sin movimiento --establecida_en--> TextoOrdenado:Operatoria de cambios exterior
  - Restriccion:Límite mensual computable para modalidad de boletos --establecida_en--> TextoOrdenado:Operatoria de cambios exterior
  - Obligacion:Declaración jurada de cliente sobre fondos aplicados --establecida_en--> TextoOrdenado:Operatoria de cambios exterior
  - Condicion:Fondos aplicados bajo modalidad de boletos sin movimiento --establecida_en--> TextoOrdenado:Operatoria de cambios exterior
  - Operacion:Confección de boletos sin movimiento de pesos --requiere--> Obligacion:Confeccionar dos boletos sin movimiento
  - Obligacion:Confeccionar dos boletos sin movimiento --regula--> Operacion:Confección de boletos sin movimiento de pesos
  - Restriccion:Límite mensual computable para modalidad de boletos --limita--> Operacion:Confección de boletos sin movimiento de pesos
  - Operacion:Confección de boletos sin movimiento de pesos --requiere--> Obligacion:Declaración jurada de cliente sobre fondos aplicados
  - Condicion:Fondos aplicados bajo modalidad de boletos sin movimiento --condicion_de--> Obligacion:Declaración jurada de cliente sobre fondos aplicados
  - Obligacion:Confeccionar dos boletos sin movimiento --aplica_a--> None
  - Restriccion:Límite mensual computable para modalidad de boletos --aplica_a--> None
  - Obligacion:Declaración jurada de cliente sobre fondos aplicados --aplica_a--> None
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}]; omisiones []; condicion_de [{"de": "Condicion:Fondos aplicados bajo modalidad de boletos sin movimiento", "a": "Obligacion:Declaración jurada de cliente sobre fondos aplicados", "firma_nueva": false}]; limita [{"de": "Restriccion:Límite mensual computable para modalidad de boletos", "a": "Operacion:Confección de boletos sin movimiento de pesos"}]

**NUEVO** — error: None

- Operacion «Registro de operaciones con dos boletos sin movimiento»: Confección de dos boletos sin movimiento de pesos por conceptos de compra y venta ‖ tramo (exacta): «A los efectos del registro de estas operaciones se deberán confeccionar dos boletos sin movimiento de pesos, por los conceptos de compra y venta que corresponda…»
- Restriccion «Cómputo de monto a límites mensuales»: El monto utilizado bajo este mecanismo se computa a los efectos de los límites mensuales aplicables ‖ tramo (exacta): «computándose el monto por el cual se utiliza este mecanismo a los efectos de los límites mensuales que pudieran ser aplicables según el caso»
- Obligacion «Declaración jurada del cliente sobre fondos»: Obtención de declaración jurada del cliente acreditando su conocimiento de que los fondos aplicados bajo esta modalidad se computarán a los efectos de los límites normativos de venta de cambio y que no los excede ‖ tramo (exacta): «En todos los casos se deberá contar con una declaración jurada del cliente en la que deja constancia de tener conocimiento de que los fondos que se aplican bajo…»
- Condicion «Conocimiento del cliente sobre cómputo de límites»: El cliente debe tener conocimiento de que los fondos bajo esta modalidad se computan a los límites normativos de venta de cambio y no los excede ‖ tramo (exacta): «los fondos que se aplican bajo esta modalidad serán computados a los efectos del cálculo de los límites que normativamente correspondan al concepto de venta de …»
  - Operacion:Registro de operaciones con dos boletos sin movimiento --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Restriccion:Cómputo de monto a límites mensuales --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Obligacion:Declaración jurada del cliente sobre fondos --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Condicion:Conocimiento del cliente sobre cómputo de límites --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Obligacion:Declaración jurada del cliente sobre fondos --aplica_a--> las entidades
  - Condicion:Conocimiento del cliente sobre cómputo de límites --condicion_de--> Obligacion:Declaración jurada del cliente sobre fondos
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "las entidades", "verificada": "no", "sujeto_id": null}]; omisiones []; condicion_de [{"de": "Condicion:Conocimiento del cliente sobre cómputo de límites", "a": "Obligacion:Declaración jurada del cliente sobre fondos", "firma_nueva": false}]; limita []

*Cuantías en el texto propio: 0.*

## Ficha 21 — `cap::5.4.4`

**Texto propio:**

```
5.4.4. Franquicias.
Las franquicias por debajo de las cuales no se recibirá compensación en caso de pérdi-
da son equivalentes a las posiciones a primera pérdida y deberán ser ponderadas por
riesgo al 1250%.
```
**Último bloque heredado:** Se aplicará el método de sustitución de ponderadores. Con este método, el ponderador de riesgo de la contraparte se sustituye por el ponderador de riesgo del garante –o contragarante– o proveedor de protección crediticia –conforme a la tabla de ponderadores prevista en la Sec- ción 2.–. Se reconocer…

**SELLADO** — error: None

- Definicion «Franquicias — equivalentes a posiciones primera pérdida»: Las franquicias por debajo de las cuales no se recibirá compensación en caso de pérdida son equivalentes a las posiciones a primera pérdida.
- Restriccion «Franquicias — ponderación al 1250%»: Las franquicias deberán ser ponderadas por riesgo al 1250%.
  - Definicion:Franquicias — equivalentes a posiciones primera pérdida --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Restriccion:Franquicias — ponderación al 1250% --establecida_en--> TextoOrdenado:Capitales Mínimos
- hechos: umbrales []; menciones []; omisiones []; condicion_de []; limita []

**NUEVO** — error: None

- Definicion «Franquicias — posiciones a primera pérdida»: Franquicias son posiciones a primera pérdida, por debajo de las cuales no se recibirá compensación en caso de pérdida ‖ tramo (exacta): «Las franquicias por debajo de las cuales no se recibirá compensación en caso de pérdida son equivalentes a las posiciones a primera pérdida»
- Restriccion «Ponderación franquicias al 1250%»: Las franquicias (posiciones a primera pérdida) deberán ser ponderadas por riesgo al 1250% ‖ tramo (exacta): «deberán ser ponderadas por riesgo al 1250%»
  - Definicion:Franquicias — posiciones a primera pérdida --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Restriccion:Ponderación franquicias al 1250% --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - rechazo: firma_invalida: relations[2]: Restriccion --limita--> Definicion
- hechos: umbrales [{"entidad": "Restriccion:Ponderación franquicias al 1250%", "tramo": "al 1250%", "verificacion": "exacta"}]; menciones []; omisiones []; condicion_de []; limita []

*Cuantías en el texto propio: 1.*

## Ficha 22 — `ric::3.1.6`

**Texto propio:**

```
3.1.6. Exigencia por riesgo de crédito de contraparte en operaciones con derivados
-OTC) o negociados en mercados regulados- y con liquidación diferida.
La exigencia final (RCD) surgirá de la sumatoria de las exposiciones al ries-
go de crédito de contraparte determinadas para cada conjunto de neteo (pun-
to 4.2. de las normas sobre “Capitales mínimos de las entidades financieras”),
y se informará en el código 14000000.
Para su determinación se seguirá la siguiente metodología:
i) Exposición al riesgo de crédito de contraparte
EAD = α (CR + EPF)
donde:
α = 1,40
CR = Costo de reposición calculado de acuerdo con el punto 4.2.1.1. de
las normas sobre “Capitales mínimos de las entidades financieras”.
EPF = Exposición potencial futura calculada de acuerdo con el punto
4.2.1.2. de dicho ordenamiento.
En caso de acuerdos de márgenes y de conjuntos de neteo múltiples, se
aplicarán las disposiciones del punto 4.2.1.3. de las citadas disposiciones.
ii) Ajuste de valuación del crédito (CVA)
Para determinar el riesgo de pérdidas derivadas de valuar a precios de
mercado el riesgo de contraparte esperado, se aplicará la fórmula del
punto 4.2.2. de las normas sobre “Capitales mínimos de las entidades fi-
nancieras”.
iii) Ponderador de riesgo (p)
Se aplicará el ponderador que corresponda a la contraparte, de acuerdo
con lo establecido en el punto 2.12. de las normas sobre “Capitales mí-
nimos de las entidades financieras”.
iv) Exigencia final (RCD)
Surgirá de la sumatoria de las exigencias EAD informadas para cada con-
traparte, de acuerdo con la siguiente expresión:
RCD = 8% x p x EAD + K(CVA)
```
**Último bloque heredado:** 3.1. Normas de procedimiento.

**SELLADO** — error: None

- Obligacion «Informar exigencia por riesgo crédito contraparte»: La exigencia final (RCD) surgirá de la sumatoria de las exposiciones al riesgo de crédito de contraparte determinadas para cada conjunto de neteo y se informará en el código 14000000.
- Operacion «Determinación EAD contraparte — derivados»: Exposición al riesgo de crédito de contraparte (EAD) en operaciones con derivados OTC o negociados en mercados regulados con liquidación diferida. La fórmula es EAD = α (CR + EPF) donde α = 1,40, CR es el Costo de reposición y EPF es la Exp…
- Operacion «Determinación CVA — ajuste de valuación crédito»: Ajuste de valuación del crédito (CVA) para determinar el riesgo de pérdidas derivadas de valuar a precios de mercado el riesgo de contraparte esperado, conforme punto 4.2.2. de las normas sobre Capitales mínimos.
- Operacion «Aplicación ponderador riesgo contraparte»: Aplicación del ponderador de riesgo (p) que corresponda a la contraparte, conforme punto 2.12. de las normas sobre Capitales mínimos de las entidades financieras.
- Obligacion «Calcular exigencia final RCD»: La exigencia final (RCD) surgirá de la sumatoria de las exigencias EAD informadas para cada contraparte, de acuerdo con la expresión: RCD = 8% x p x EAD + K(CVA)
- Obligacion «Aplicar disposiciones márgenes múltiples»: En caso de acuerdos de márgenes y de conjuntos de neteo múltiples, se aplicarán las disposiciones del punto 4.2.1.3. de las normas sobre Capitales mínimos de las entidades financieras.
  - Obligacion:Informar exigencia por riesgo crédito contraparte --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Operacion:Determinación EAD contraparte — derivados --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Operacion:Determinación CVA — ajuste de valuación crédito --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Operacion:Aplicación ponderador riesgo contraparte --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Obligacion:Calcular exigencia final RCD --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Obligacion:Aplicar disposiciones márgenes múltiples --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Obligacion:Informar exigencia por riesgo crédito contraparte --aplica_a--> None
  - Obligacion:Calcular exigencia final RCD --aplica_a--> None
  - Obligacion:Aplicar disposiciones márgenes múltiples --aplica_a--> None
  - Operacion:Determinación EAD contraparte — derivados --requiere--> Obligacion:Calcular exigencia final RCD
  - Operacion:Determinación CVA — ajuste de valuación crédito --requiere--> Obligacion:Calcular exigencia final RCD
  - Operacion:Aplicación ponderador riesgo contraparte --requiere--> Obligacion:Calcular exigencia final RCD
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}]; omisiones [{"categoria": null, "tramo": "", "verificacion": "ausente", "nota": "Fórmulas matemáticas con coeficientes: EAD = α (CR + EPF), RCD = 8% x p x EAD + K(CVA) — estructura …"}]; condicion_de []; limita []

**NUEVO** — error: None

- Operacion «Operaciones con derivados OTC o en mercados regulados»: Operaciones con derivados OTC o negociados en mercados regulados con liquidación diferida ‖ tramo (exacta): «operaciones con derivados -OTC) o negociados en mercados regulados- y con liquidación diferida»
- Operacion «Cálculo de exposición al riesgo de crédito de contraparte»: Determinación de la exposición al riesgo de crédito de contraparte (EAD) según la metodología especificada ‖ tramo (exacta): «Exposición al riesgo de crédito de contraparte»
- Operacion «Cálculo de ajuste de valuación del crédito (CVA)»: Determinación del riesgo de pérdidas derivadas de valuar a precios de mercado el riesgo de contraparte esperado ‖ tramo (exacta): «Ajuste de valuación del crédito (CVA)»
- Operacion «Determinación de la exigencia final de capital por riesgo de crédito»: Determinación de la exigencia final (RCD) como sumatoria de exposiciones al riesgo de crédito de contraparte para cada conjunto de neteo ‖ tramo (exacta): «La exigencia final (RCD) surgirá de la sumatoria de las exposiciones al riesgo de crédito de contraparte»
- Obligacion «Informar exigencia de capital por riesgo de crédito en código 14000000»: Las entidades deberán informar la exigencia final (RCD) en el código 14000000 ‖ tramo (exacta): «se informará en el código 14000000»
- Obligacion «Seguir metodología de determinación de exigencia de crédito»: Las entidades deberán seguir la metodología especificada para determinar la exigencia por riesgo de crédito de contraparte, que incluye el cálculo de EAD, CVA, aplicación de ponderador de riesgo y exigencia final ‖ tramo (exacta): «Para su determinación se seguirá la siguiente metodología»
- Condicion «Existencia de acuerdos de márgenes y conjuntos de neteo múltiples»: Supuesto en el que aplican disposiciones especiales del punto 4.2.1.3 de las normas sobre Capitales mínimos ‖ tramo (exacta): «En caso de acuerdos de márgenes y de conjuntos de neteo múltiples»
  - Operacion:Operaciones con derivados OTC o en mercados regulados --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Operacion:Cálculo de exposición al riesgo de crédito de contraparte --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Operacion:Cálculo de ajuste de valuación del crédito (CVA) --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Operacion:Determinación de la exigencia final de capital por riesgo de… --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Obligacion:Informar exigencia de capital por riesgo de crédito en códig… --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Obligacion:Seguir metodología de determinación de exigencia de crédito --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Condicion:Existencia de acuerdos de márgenes y conjuntos de neteo múlt… --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Obligacion:Informar exigencia de capital por riesgo de crédito en códig… --aplica_a--> las entidades
  - Obligacion:Seguir metodología de determinación de exigencia de crédito --aplica_a--> las entidades
  - rechazo: firma_invalida: relations[9]: Condicion --condiciona--> Operacion
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "las entidades", "verificada": "exacta", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "las entidades", "verificada": "exacta", "sujeto_id": null}]; omisiones [{"categoria": "formula", "tramo": "EAD = α (CR + EPF)", "verificacion": "exacta", "nota": "Fórmula de cálculo de exposición; contenido no confiable declarado por FLAGS E0"}, {"categoria": "formula", "tramo": "α = 1,40", "verificacion": "exacta", "nota": "Valor de parámetro en fórmula; contenido no confiable declarado por FLAGS E0"}, {"categoria": "formula", "tramo": "RCD = 8% x p x EAD + K(CVA)", "verificacion": "exacta", "nota": "Fórmula de cálculo de exigencia final; contenido no confiable declarado por FLAGS E0"}]; condicion_de []; limita []

*Cuantías en el texto propio: 1.*

## Ficha 23 — `ric::4.1.1.1`

**Texto propio:**

```
4.1.1.1. La exigencia por riesgo de mercado se determinará con los valores que se registren
al último día del período de información (n), y el total surgirá de la siguiente suma:
Código 70800000 (n) = Código 311000/xx + Código 312000/xx + Código 313000/xx
+Código 315000/xx + Código 314000/xx
A estos fines, se reemplazarán las dos últimas posiciones de cada partida de
exigencia por el último día del período que corresponda (ejemplo, xx = 31).
```
**Último bloque heredado:** 4.1.1. Exigencia

**SELLADO** — error: None

- Operacion «Determinación exigencia riesgo de mercado»: La exigencia por riesgo de mercado se determinará con los valores que se registren al último día del período de información (n), resultando de una suma de códigos contables específicos (311000, 312000, 313000, 315000, 314000 con sustitución…
- Obligacion «Calcular exigencia con valores período final»: Se determinará la exigencia por riesgo de mercado con los valores que se registren al último día del período de información.
- Obligacion «Reemplazar últimas posiciones con día período»: Se reemplazarán las dos últimas posiciones de cada partida de exigencia por el último día del período que corresponda (ejemplo, xx = 31).
  - Obligacion:Calcular exigencia con valores período final --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Obligacion:Reemplazar últimas posiciones con día período --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Obligacion:Calcular exigencia con valores período final --aplica_a--> None
  - Obligacion:Reemplazar últimas posiciones con día período --aplica_a--> None
  - Obligacion:Calcular exigencia con valores período final --regula--> Operacion:Determinación exigencia riesgo de mercado
  - Obligacion:Reemplazar últimas posiciones con día período --regula--> Operacion:Determinación exigencia riesgo de mercado
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}]; omisiones [{"categoria": null, "tramo": "", "verificacion": "ausente", "nota": "Fórmula de suma de códigos contables: Código 70800000 (n) = Código 311000/xx + Código 312000/xx + Có…"}, {"categoria": null, "tramo": "", "verificacion": "ausente", "nota": "Ejemplo específico xx=31: no extraído como valor concreto, solo enunciada la regla de sustitución en…"}]; condicion_de []; limita []

**NUEVO** — error: None

- Operacion «Determinación exigencia por riesgo de mercado»: Se determinará con los valores registrados al último día del período de información. El total surge de la suma: Código 70800000 (n) = Código 311000/xx + Código 312000/xx + Código 313000/xx + Código 315000/xx + Código 314000/xx, donde las do… ‖ tramo (exacta): «La exigencia por riesgo de mercado se determinará con los valores que se registren al último día del período de información (n)»
- Obligacion «Registrar valores último día período»: Las entidades deberán utilizar los valores que se registren al último día del período de información para la determinación de la exigencia por riesgo de mercado. ‖ tramo (exacta): «se determinará con los valores que se registren al último día del período de información (n)»
- Obligacion «Reemplazar posiciones con día del período»: Las entidades reemplazarán las dos últimas posiciones de cada partida de exigencia por el último día del período que corresponda (ejemplo, xx = 31). ‖ tramo (exacta): «se reemplazarán las dos últimas posiciones de cada partida de exigencia por el último día del período que corresponda»
  - Operacion:Determinación exigencia por riesgo de mercado --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Obligacion:Registrar valores último día período --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Obligacion:Reemplazar posiciones con día del período --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Obligacion:Registrar valores último día período --aplica_a--> las entidades
  - Obligacion:Reemplazar posiciones con día del período --aplica_a--> las entidades
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "las entidades", "verificada": "no", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "las entidades", "verificada": "no", "sujeto_id": null}]; omisiones [{"categoria": "formula", "tramo": "Código 70800000 (n) = Código 311000/xx + Código 312000/xx + Código 313000/xx + Código 315000/xx + Có…", "verificacion": "exacta", "nota": "Fórmula de cálculo declarada no confiable por E0. El contenido se registra en la descripción de la O…"}]; condicion_de []; limita []

*Cuantías en el texto propio: 0.*

## Ficha 24 — `ext::10.4.2.7`

**Texto propio:**

```
10.4.2.7. Se requerirá la conformidad previa del BCRA cuando el cliente registre por
operaciones anteriores al 02/09/19, una condena o un sumario en materia
penal cambiario en trámite, en ambos casos, por infracciones al artículo 1°
inciso c) de la Ley 19.359 relativas a regímenes de pagos por
importaciones de bienes. Serán consideradas las condenas dictadas por
hasta 5 (cinco) años anteriores a la fecha de la operación.
Las entidades deberán consultar en el apartado “Régimen Informativo
SEPAIMPO” del sitio www3.bcra.gob.ar, si el cliente se encuentra en la
situación prevista en el párrafo precedente.
Este requisito no será de aplicación para:
i) el sector público;
ii) todas las organizaciones empresariales, cualquiera sea su forma
societaria, en donde el Estado Nacional tenga participación mayoritaria
en el capital o en la formación de las decisiones societarias; y
iii)los fideicomisos constituidos con aportes del sector público nacional.
```
**Último bloque heredado:** La entidad podrá dar acceso al mercado de cambios para el pago al exterior en la medida que verifique previamente que se cumplen la totalidad de los siguientes requisitos:

**SELLADO** — error: None

- Obligacion «Consulta en SEPAIMPO — conformidad previa BCRA»: Se requerirá la conformidad previa del BCRA cuando el cliente registre por operaciones anteriores al 02/09/19, una condena o un sumario en materia penal cambiario en trámite, en ambos casos, por infracciones al artículo 1° inciso c) de la L…
- Obligacion «Verificar situación penal-cambiaria en SEPAIMPO»: Las entidades deberán consultar en el apartado 'Régimen Informativo SEPAIMPO' del sitio www3.bcra.gob.ar, si el cliente se encuentra en la situación prevista en el párrafo precedente.
- Excepcion «Exención — sector público y entidades con participación estatal»: Este requisito no será de aplicación para: i) el sector público; ii) todas las organizaciones empresariales, cualquiera sea su forma societaria, en donde el Estado Nacional tenga participación mayoritaria en el capital o en la formación de …
- Operacion «Pago anticipado de importaciones de bienes»: Acceso al mercado de cambios para el pago al exterior de importaciones de bienes con registro de ingreso aduanero pendiente, condicionado a requisitos previos de verificación de conformidad.
  - Obligacion:Consulta en SEPAIMPO — conformidad previa BCRA --establecida_en--> TextoOrdenado:Texto Ordenado de Exterior y Cambios
  - Obligacion:Verificar situación penal-cambiaria en SEPAIMPO --establecida_en--> TextoOrdenado:Texto Ordenado de Exterior y Cambios
  - Excepcion:Exención — sector público y entidades con participación esta… --establecida_en--> TextoOrdenado:Texto Ordenado de Exterior y Cambios
  - Operacion:Pago anticipado de importaciones de bienes --establecida_en--> TextoOrdenado:Texto Ordenado de Exterior y Cambios
  - Obligacion:Consulta en SEPAIMPO — conformidad previa BCRA --aplica_a--> None
  - Obligacion:Verificar situación penal-cambiaria en SEPAIMPO --aplica_a--> None
  - Excepcion:Exención — sector público y entidades con participación esta… --aplica_a--> None
  - Excepcion:Exención — sector público y entidades con participación esta… --aplica_a--> Organizaciones empresariales con participación mayoritaria del Estado Nacional
  - Excepcion:Exención — sector público y entidades con participación esta… --aplica_a--> None
  - Obligacion:Verificar situación penal-cambiaria en SEPAIMPO --regula--> Operacion:Pago anticipado de importaciones de bienes
  - Operacion:Pago anticipado de importaciones de bienes --requiere--> Obligacion:Consulta en SEPAIMPO — conformidad previa BCRA
  - Operacion:Pago anticipado de importaciones de bienes --requiere--> Obligacion:Verificar situación penal-cambiaria en SEPAIMPO
  - Excepcion:Exención — sector público y entidades con participación esta… --exceptua_obligacion--> Obligacion:Consulta en SEPAIMPO — conformidad previa BCRA
  - Excepcion:Exención — sector público y entidades con participación esta… --exceptua_obligacion--> Obligacion:Verificar situación penal-cambiaria en SEPAIMPO
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "Organizaciones empresariales con participación mayoritaria del Estado Nacional", "verificada": "no", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}]; omisiones []; condicion_de []; limita []

**NUEVO** — error: None

- Operacion «Pago anticipado importaciones — requisito condena/sumario»: Pago anticipado de importaciones de bienes, cuando el cliente registra por operaciones anteriores al 02/09/19 una condena o un sumario en materia penal cambiario en trámite por infracciones al artículo 1° inciso c) de la Ley 19.359 relativa… ‖ tramo (exacta): «acceso al mercado de cambios para el pago al exterior»
- Obligacion «Obtener conformidad previa BCRA — antecedentes penales cambiararios»: Las entidades deberán obtener conformidad previa del BCRA cuando el cliente registre por operaciones anteriores al 02/09/19 una condena o un sumario en materia penal cambiario en trámite por infracciones al artículo 1° inciso c) de la Ley 1… ‖ tramo (exacta): «Se requerirá la conformidad previa del BCRA cuando el cliente registre por operaciones anteriores al 02/09/19, una condena o un sumario en materia penal cambiar…»
- Obligacion «Consultar Régimen Informativo SEPAIMPO — situación cliente»: Las entidades deberán consultar en el apartado 'Régimen Informativo SEPAIMPO' del sitio www3.bcra.gob.ar si el cliente se encuentra en la situación de tener una condena o un sumario en materia penal cambiario en trámite por infracciones al … ‖ tramo (exacta): «Las entidades deberán consultar en el apartado "Régimen Informativo SEPAIMPO" del sitio www3.bcra.gob.ar, si el cliente se encuentra en la situación prevista en…»
- Excepcion «Excepción sector público — antecedentes penales»: El requisito de conformidad previa del BCRA por antecedentes penales cambiarios no aplica al sector público. ‖ tramo (exacta): «Este requisito no será de aplicación para: i) el sector público»
- Excepcion «Excepción empresas con participación estatal mayoritaria — antecedentes penales»: El requisito de conformidad previa del BCRA por antecedentes penales cambiarios no aplica a las organizaciones empresariales en donde el Estado Nacional tenga participación mayoritaria en el capital o en la formación de las decisiones socie… ‖ tramo (no): «Este requisito no será de aplicación para: ii) todas las organizaciones empresariales, cualquiera sea su forma societaria, en donde el Estado Nacional tenga par…»
- Excepcion «Excepción fideicomisos con aportes del sector público — antecedentes penales»: El requisito de conformidad previa del BCRA por antecedentes penales cambiarios no aplica a los fideicomisos constituidos con aportes del sector público nacional. ‖ tramo (no): «Este requisito no será de aplicación para: iii) los fideicomisos constituidos con aportes del sector público nacional»
  - Obligacion:Obtener conformidad previa BCRA — antecedentes penales cambi… --establecida_en--> TextoOrdenado:Texto Ordenado Exterior - Cambios
  - Obligacion:Consultar Régimen Informativo SEPAIMPO — situación cliente --establecida_en--> TextoOrdenado:Texto Ordenado Exterior - Cambios
  - Excepcion:Excepción sector público — antecedentes penales --establecida_en--> TextoOrdenado:Texto Ordenado Exterior - Cambios
  - Excepcion:Excepción empresas con participación estatal mayoritaria — a… --establecida_en--> TextoOrdenado:Texto Ordenado Exterior - Cambios
  - Excepcion:Excepción fideicomisos con aportes del sector público — ante… --establecida_en--> TextoOrdenado:Texto Ordenado Exterior - Cambios
  - Operacion:Pago anticipado importaciones — requisito condena/sumario --establecida_en--> TextoOrdenado:Texto Ordenado Exterior - Cambios
  - Obligacion:Obtener conformidad previa BCRA — antecedentes penales cambi… --aplica_a--> Las entidades
  - Obligacion:Consultar Régimen Informativo SEPAIMPO — situación cliente --aplica_a--> Las entidades
  - Excepcion:Excepción sector público — antecedentes penales --exceptua_obligacion--> Obligacion:Obtener conformidad previa BCRA — antecedentes penales cambi…
  - Excepcion:Excepción empresas con participación estatal mayoritaria — a… --exceptua_obligacion--> Obligacion:Obtener conformidad previa BCRA — antecedentes penales cambi…
  - Excepcion:Excepción fideicomisos con aportes del sector público — ante… --exceptua_obligacion--> Obligacion:Obtener conformidad previa BCRA — antecedentes penales cambi…
- hechos: umbrales [{"entidad": "Obligacion:Obtener conformidad previa BCRA — antecedentes penales cambi…", "tramo": "5 (cinco) años anteriores a la fecha de la operación", "verificacion": "exacta"}]; menciones [{"pred": "aplica_a", "mencion": "Las entidades", "verificada": "exacta", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "Las entidades", "verificada": "exacta", "sujeto_id": null}]; omisiones [{"categoria": "meta_normativo", "tramo": "Este requisito no será de aplicación para", "verificacion": "exacta", "nota": "Encabezado que anuncia una lista de excepciones; no es contenido normativo por sí solo, sino introdu…"}]; condicion_de []; limita []

*Cuantías en el texto propio: 1.*

## Ficha 25 — `cap::6.2.2.4`

**Texto propio:**

```
6.2.2.4. Las posiciones imputadas a cada banda temporal deberán ponderarse por un
factor que refleje su sensibilidad a los cambios en las tasas de interés, confor-
me al siguiente cuadro:
[TABLA cap::tabla036 | página 124 | e0_tablas | posicional]
Fila 1: col1 = Zona | col2 = Cupón menor a 3 % | col3 = Cupón igual o mayor a 3 % | col4 = Ponderador de riesgo | col5 = Cambio supuesto en el rendimiento –a utilizar en el método delta-plus (punto 6.6.3.)–
Fila 2: col2 = Meses* ⟨abarca hasta col3⟩
Fila 3: col1 = 1 | col2 = 0-1 | col3 = 0-1 | col4 = 0,00 % | col5 = 1,00
Fila 4: col1 = 1 ⟨combinada con fila 3⟩ | col2 = 1-3 | col3 = 1-3 | col4 = 0,20 % | col5 = 1,00
Fila 5: col1 = 1 ⟨combinada con fila 3⟩ | col2 = 3-6 | col3 = 3-6 | col4 = 0,40 % | col5 = 1,00
Fila 6: col1 = 1 ⟨combinada con fila 3⟩ | col2 = 6-12 | col3 = 6-12 | col4 = 0,70 % | col5 = 1,00
Fila 7: col2 = Años* ⟨abarca hasta col3⟩
Fila 8: col1 = 2 | col2 = 1-1,9 | col3 = 1-2 | col4 = 1,25 % | col5 = 0,90
Fila 9: col1 = 2 ⟨combinada con fila 8⟩ | col2 = 1,9-2,8 | col3 = 2-3 | col4 = 1,75 % | col5 = 0,80
Fila 10: col1 = 2 ⟨combinada con fila 8⟩ | col2 = 2,8-3,6 | col3 = 3-4 | col4 = 2,25 % | col5 = 0,75
Fila 11: col2 = Años* ⟨abarca hasta col3⟩
Fila 12: col1 = 3 | col2 = 3,6-4,3 | col3 = 4-5 | col4 = 2,75 % | col5 = 0,75
Fila 13: col1 = 3 ⟨combinada con fila 12⟩ | col2 = 4,3-5,7 | col3 = 5-7 | col4 = 3,25 % | col5 = 0,70
Fila 14: col1 = 3 ⟨combinada con fila 12⟩ | col2 = 5,7-7,3 | col3 = 7-10 | col4 = 3,75 % | col5 = 0,65
Fila 15: col1 = 3 ⟨combinada con fila 12⟩ | col2 = 7,3-9,3 | col3 = 10-15 | col4 = 4,50 % | col5 = 0,60
Fila 16: col1 = 3 ⟨combinada con fila 12⟩ | col2 = 9,3-10,6 | col3 = 15-20 | col4 = 5,25 % | col5 = 0,60
Fila 17: col1 = 3 ⟨combinada con fila 12⟩ | col2 = 10,6-12 | col3 = Más de 20 | col4 = 6,00 % | col5 = 0,60
Fila 18: col1 = 3 ⟨combinada con fila 12⟩ | col2 = 12-20 | col4 = 8,00 % | col5 = 0,60
Fila 19: col1 = 3 ⟨combinada con fila 12⟩ | col2 = Más de 20 | col4 = 12,50 % | col5 = 0,60
[FIN TABLA cap::tabla036]
*
Al efecto de imputar una posición a la escala de vencimientos cuando el plazo residual o el plazo que res-
ta hasta el siguiente ajuste del interés, según el caso, es igual al límite entre dos bandas, corresponderá
realizar la imputación a la banda temporal más próxima a la fecha de cálculo.
```
**Último bloque heredado:** 6.2.2. Exigencia de capital por riesgo general de mercado: método de los plazos residuales.

**SELLADO** — error: None

- Operacion «Ponderación de posiciones por sensibilidad a tasas»: Las posiciones imputadas a cada banda temporal deberán ponderarse por un factor que refleje su sensibilidad a los cambios en las tasas de interés, conforme al cuadro especificado
- Obligacion «Ponderar posiciones por factor de sensibilidad»: Las posiciones imputadas a cada banda temporal deberán ponderarse por un factor que refleje su sensibilidad a los cambios en las tasas de interés, conforme al cuadro especificado
- Condicion «Imputación a banda según plazo residual»: Al efecto de imputar una posición a la escala de vencimientos cuando el plazo residual o el plazo que resta hasta el siguiente ajuste del interés, según el caso, es igual al límite entre dos bandas, corresponderá realizar la imputación a la…
  - Obligacion:Ponderar posiciones por factor de sensibilidad --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Condicion:Imputación a banda según plazo residual --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Obligacion:Ponderar posiciones por factor de sensibilidad --aplica_a--> None
  - Operacion:Ponderación de posiciones por sensibilidad a tasas --requiere--> Obligacion:Ponderar posiciones por factor de sensibilidad
  - Condicion:Imputación a banda según plazo residual --condicion_de--> Obligacion:Ponderar posiciones por factor de sensibilidad
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}]; omisiones [{"categoria": null, "tramo": "", "verificacion": "ausente", "nota": "Tabla de ponderadores por banda temporal, cambio supuesto, cupón y zona menor: estructura tabular no…"}]; condicion_de [{"de": "Condicion:Imputación a banda según plazo residual", "a": "Obligacion:Ponderar posiciones por factor de sensibilidad", "firma_nueva": false}]; limita []

**NUEVO** — error: None

- Operacion «Ponderación de posiciones por sensibilidad a tasas»: Asignación a cada posición de un factor de ponderación según su sensibilidad a cambios en las tasas de interés, conforme a la tabla de zonas y cupones especificada ‖ tramo (exacta): «Las posiciones imputadas a cada banda temporal deberán ponderarse por un factor que refleje su sensibilidad a los cambios en las tasas de interés»
- Obligacion «Ponderar posiciones imputadas a bandas temporales»: Las entidades deberán aplicar a las posiciones imputadas a cada banda temporal un factor de ponderación que refleje su sensibilidad a los cambios en las tasas de interés, según la tabla de ponderadores por zona y cupón ‖ tramo (exacta): «Las posiciones imputadas a cada banda temporal deberán ponderarse por un factor que refleje su sensibilidad a los cambios en las tasas de interés»
- Condicion «Imputación a banda según plazo residual»: Cuando el plazo residual o el plazo hasta el siguiente ajuste del interés iguala el límite entre dos bandas, la posición se imputa a la banda más próxima a la fecha de cálculo ‖ tramo (exacta): «Al efecto de imputar una posición a la escala de vencimientos cuando el plazo residual o el plazo que resta hasta el siguiente ajuste del interés, según el caso…»
- Definicion «Ponderador de riesgo — factor según sensibilidad»: Factor que refleja la sensibilidad de cada posición a los cambios en las tasas de interés, asignado según la zona y el nivel de cupón de cada instrumento conforme a la tabla especificada ‖ tramo (exacta): «factor que refleje su sensibilidad a los cambios en las tasas de interés»
  - Obligacion:Ponderar posiciones imputadas a bandas temporales --establecida_en--> TextoOrdenado:Texto Ordenado de Capitales Mínimos
  - Condicion:Imputación a banda según plazo residual --establecida_en--> TextoOrdenado:Texto Ordenado de Capitales Mínimos
  - Definicion:Ponderador de riesgo — factor según sensibilidad --establecida_en--> TextoOrdenado:Texto Ordenado de Capitales Mínimos
  - Condicion:Imputación a banda según plazo residual --condicion_de--> Obligacion:Ponderar posiciones imputadas a bandas temporales
  - Obligacion:Ponderar posiciones imputadas a bandas temporales --aplica_a--> Las entidades
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "Las entidades", "verificada": "no", "sujeto_id": null}]; omisiones [{"categoria": "tabla", "tramo": "[TABLA cap::tabla036 | página 124 | e0_tablas | posicional] ... [FIN TABLA cap::tabla036]", "verificacion": "no", "nota": "Tabla de ponderadores de riesgo por zona, cupón y plazo residual. La tabla es confiable (serializada…"}]; condicion_de [{"de": "Condicion:Imputación a banda según plazo residual", "a": "Obligacion:Ponderar posiciones imputadas a bandas temporales", "firma_nueva": false}]; limita []

*Cuantías en el texto propio: 17.*

## Ficha 26 — `ext::7.1.1.3`

**Texto propio:**

```
7.1.1.3. 60 (sesenta) días corridos para las operaciones con contrapartes vinculadas
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
```
**Último bloque heredado:** Independientemente de los plazos máximos precedentes, los cobros de exportaciones deberán ser ingresados y liquidados en el mercado de cambios dentro de los 20 (veinte) días hábiles de la fecha de cobro. La posibilidad de utilizar este plazo quedará supeditada en todos los casos al cumplimiento de l…

**SELLADO** — error: None

- Obligacion «Ingreso y liquidación en 60 días — contrapartes vinculadas»: Las operaciones con contrapartes vinculadas que no correspondan a los bienes indicados en los puntos 7.1.1.1. y 7.1.1.2. y las exportaciones correspondientes a los capítulos 26 (excepto las posiciones especificadas) y 71 (excepto las posici…
- Operacion «Cobro de exportación con contrapartes vinculadas»: Operación de ingreso y liquidación de divisas provenientes de exportación realizada con contrapartes vinculadas, según los capítulos arancelarios 26 y 71 (con exclusiones especificadas)
- Potestad «Solicitar extensión de plazo — entidad seguimiento»: Los exportadores que realizaron operaciones con contrapartes vinculadas correspondientes a bienes comprendidos en el punto 7.1.1.4., en las cuales el importador sea una sociedad controlada por el exportador argentino, podrán solicitar a la …
- Condicion «Exportador no ha superado USD 50.000.000 año anterior»: Cuando el exportador no haya registrado exportaciones por un valor total superior al equivalente a USD 50.000.000 (dólares estadounidenses cincuenta millones) en el año calendario inmediato anterior a la oficialización de la destinación.
- Restriccion «Plazo máximo 60 días — condición umbral USD 50M»: Cuando el exportador no haya superado USD 50.000.000 en el año calendario anterior, la extensión del plazo no podrá exceder el plazo previsto en el punto 7.1.1.4.
- Condicion «Exportador ha superado USD 50.000.000 e bienes en posiciones específicas»: Cuando el exportador haya superado el monto de USD 50.000.000 en el año calendario anterior y los bienes exportados correspondan a las posiciones arancelarias especificadas (tabla de posiciones 0202 y siguientes).
- Restriccion «Plazo máximo 120 días — bienes posiciones especificadas»: Un plazo de 120 (ciento veinte) días corridos cuando el exportador haya superado USD 50.000.000 en el año anterior y los bienes exportados correspondan a las posiciones arancelarias especificadas.
  - Obligacion:Ingreso y liquidación en 60 días — contrapartes vinculadas --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Operacion:Cobro de exportación con contrapartes vinculadas --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Potestad:Solicitar extensión de plazo — entidad seguimiento --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Condicion:Exportador no ha superado USD 50.000.000 año anterior --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Restriccion:Plazo máximo 60 días — condición umbral USD 50M --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Condicion:Exportador ha superado USD 50.000.000 e bienes en posiciones… --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Restriccion:Plazo máximo 120 días — bienes posiciones especificadas --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Obligacion:Ingreso y liquidación en 60 días — contrapartes vinculadas --regula--> Operacion:Cobro de exportación con contrapartes vinculadas
  - Condicion:Exportador no ha superado USD 50.000.000 año anterior --condicion_de--> Restriccion:Plazo máximo 60 días — condición umbral USD 50M
  - Condicion:Exportador ha superado USD 50.000.000 e bienes en posiciones… --condicion_de--> Restriccion:Plazo máximo 120 días — bienes posiciones especificadas
  - Obligacion:Ingreso y liquidación en 60 días — contrapartes vinculadas --aplica_a--> None
  - Potestad:Solicitar extensión de plazo — entidad seguimiento --aplica_a--> Exportadores
  - Restriccion:Plazo máximo 60 días — condición umbral USD 50M --aplica_a--> Exportadores
  - Restriccion:Plazo máximo 120 días — bienes posiciones especificadas --aplica_a--> Exportadores
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "Exportadores", "verificada": "exacta", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "Exportadores", "verificada": "exacta", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "Exportadores", "verificada": "exacta", "sujeto_id": null}]; omisiones [{"categoria": null, "tramo": "", "verificacion": "ausente", "nota": "Tabla de posiciones arancelarias (0202.30.00.126T, 0202.30.00.131K, ..., 2204.21.00): estructura tab…"}]; condicion_de [{"de": "Condicion:Exportador no ha superado USD 50.000.000 año anterior", "a": "Restriccion:Plazo máximo 60 días — condición umbral USD 50M", "firma_nueva": false}, {"de": "Condicion:Exportador ha superado USD 50.000.000 e bienes en posiciones…", "a": "Restriccion:Plazo máximo 120 días — bienes posiciones especificadas", "firma_nueva": false}]; limita []

**NUEVO** — error: None

- Operacion «Operaciones exportación con contrapartes vinculadas»: Operaciones de exportación realizadas con contrapartes vinculadas que no correspondan a los bienes de los puntos 7.1.1.1 y 7.1.1.2, incluyendo exportaciones de capítulos 26 y 71 según posiciones arancelarias especificadas ‖ tramo (exacta): «operaciones con contrapartes vinculadas que no correspondan a los bienes indicados en los puntos 7.1.1.1. y 7.1.1.2. y las exportaciones correspondientes a los …»
- Restriccion «Plazo 60 días — operaciones contrapartes vinculadas»: El ingreso y liquidación de divisas para operaciones con contrapartes vinculadas deberá concretarse en 60 (sesenta) días corridos desde la fecha del cumplido de embarque otorgado por la Aduana ‖ tramo (exacta): «60 (sesenta) días corridos para las operaciones con contrapartes vinculadas»
- Potestad «Solicitar extensión de plazo — controladas por exportador»: Los exportadores que realizaron operaciones con contrapartes vinculadas cuyo importador sea una sociedad controlada por el exportador argentino podrán solicitar a la entidad encargada del seguimiento de la destinación que extienda el plazo ‖ tramo (exacta): «podrán solicitar a la entidad encargada del seguimiento de la destinación que extienda el plazo»
- Condicion «Exportador no superó USD 50.000.000 en año anterior»: Supuesto en que el exportador no haya registrado exportaciones por un valor total superior a USD 50.000.000 en el año calendario inmediato anterior a la oficialización de la destinación ‖ tramo (exacta): «cuando el exportador no haya registrado exportaciones por un valor total superior al equivalente a USD 50.000.000 (dólares estadounidenses cincuenta millones) e…»
- Excepcion «Extensión a plazo original — exportador bajo umbral USD 50M»: Extensión del plazo hasta el plazo previsto en el punto 7.1.1.4 cuando el exportador no haya superado el monto de USD 50.000.000 en el año anterior ‖ tramo (exacta): «el plazo previsto en dicho punto cuando el exportador no haya registrado exportaciones por un valor total superior al equivalente a USD 50.000.000 (dólares esta…»
- Condicion «Exportador superó USD 50.000.000 y posiciones arancelarias específicas»: Supuesto en que el exportador haya superado el monto de USD 50.000.000 en el año anterior y los bienes exportados correspondan a posiciones arancelarias específicas ‖ tramo (exacta): «cuando el exportador haya superado el monto indicado en el punto precedente y los bienes exportados correspondan a las posiciones que se detallan»
- Excepcion «Extensión 120 días — exportador sobre USD 50M con posiciones especificadas»: Extensión del plazo hasta 120 (ciento veinte) días corridos cuando el exportador ha superado USD 50.000.000 y los bienes corresponden a las posiciones arancelarias especificadas ‖ tramo (exacta): «un plazo de 120 (ciento veinte) días corridos cuando el exportador haya superado el monto indicado en el punto precedente y los bienes exportados correspondan a…»
  - Restriccion:Plazo 60 días — operaciones contrapartes vinculadas --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Operacion:Operaciones exportación con contrapartes vinculadas --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Potestad:Solicitar extensión de plazo — controladas por exportador --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Condicion:Exportador no superó USD 50.000.000 en año anterior --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Excepcion:Extensión a plazo original — exportador bajo umbral USD 50M --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Condicion:Exportador superó USD 50.000.000 y posiciones arancelarias e… --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Excepcion:Extensión 120 días — exportador sobre USD 50M con posiciones… --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Restriccion:Plazo 60 días — operaciones contrapartes vinculadas --limita--> Operacion:Operaciones exportación con contrapartes vinculadas
  - Condicion:Exportador no superó USD 50.000.000 en año anterior --condicion_de--> Excepcion:Extensión a plazo original — exportador bajo umbral USD 50M
  - Condicion:Exportador superó USD 50.000.000 y posiciones arancelarias e… --condicion_de--> Excepcion:Extensión 120 días — exportador sobre USD 50M con posiciones…
  - Restriccion:Plazo 60 días — operaciones contrapartes vinculadas --aplica_a--> los exportadores
  - Potestad:Solicitar extensión de plazo — controladas por exportador --aplica_a--> Los exportadores que realizaron operaciones con contrapartes vinculadas
- hechos: umbrales [{"entidad": "Restriccion:Plazo 60 días — operaciones contrapartes vinculadas", "tramo": "60 (sesenta) días corridos", "verificacion": "exacta"}, {"entidad": "Condicion:Exportador no superó USD 50.000.000 en año anterior", "tramo": "valor total superior al equivalente a USD 50.000.000", "verificacion": "exacta"}, {"entidad": "Condicion:Exportador superó USD 50.000.000 y posiciones arancelarias e…", "tramo": "superado el monto indicado", "verificacion": "exacta"}, {"entidad": "Excepcion:Extensión 120 días — exportador sobre USD 50M con posiciones…", "tramo": "plazo de 120 (ciento veinte) días corridos", "verificacion": "exacta"}]; menciones [{"pred": "aplica_a", "mencion": "los exportadores", "verificada": "exacta", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "Los exportadores que realizaron operaciones con contrapartes vinculadas", "verificada": "exacta", "sujeto_id": null}]; omisiones [{"categoria": "tabla", "tramo": "0202.30.00.111D, 0202.30.00.115M, 0202.30.00.117R; 0202.30.00.118U, 0202.30.00.121G, 0202.30.00.124N…", "verificacion": "exacta", "nota": "Contenido tabular no confiable declarado en FLAGS E0. Lista de posiciones arancelarias específicas q…"}]; condicion_de [{"de": "Condicion:Exportador no superó USD 50.000.000 en año anterior", "a": "Excepcion:Extensión a plazo original — exportador bajo umbral USD 50M", "firma_nueva": false}, {"de": "Condicion:Exportador superó USD 50.000.000 y posiciones arancelarias e…", "a": "Excepcion:Extensión 120 días — exportador sobre USD 50M con posiciones…", "firma_nueva": false}]; limita [{"de": "Restriccion:Plazo 60 días — operaciones contrapartes vinculadas", "a": "Operacion:Operaciones exportación con contrapartes vinculadas"}]

*Cuantías en el texto propio: 3.*

## Ficha 27 — `adrei::4.3.1.1`

**Texto propio:**

```
4.3.1.1. Establecer políticas y procedimientos de elaboración de informes que den res-
puesta a las diferentes necesidades del Directorio, la Alta Gerencia y los demás
niveles de la organización, y que prevean la confirmación periódica por parte de
los destinatarios de que la información agregada y presentada es pertinente y
adecuada –tanto en cantidad como en calidad– para el proceso de gobierno y la
toma de decisiones.
Tanto el Directorio como la Alta Gerencia deben establecer sus propios requisi-
tos de elaboración de informes de riesgos y asegurarse de que solicitan y reci-
ben información relevante que les permita cumplir con sus funciones, en relación
con la entidad financiera y los riesgos a los que está expuesta.
El Directorio debe alertar a la Alta Gerencia cuando los informes de riesgos no
cumplan sus requisitos o no proporcionen el nivel o el tipo de información que le
permitan controlar que la entidad esté operando dentro de su grado de tolerancia
al/apetito por el riesgo. Además, el Directorio debe advertirle cuando no se está
obteniendo una relación equilibrada entre información detallada y cuantitativa e
información cualitativa.
```
**Último bloque heredado:** Las entidades financieras deben:

**SELLADO** — error: None

- Obligacion «Establecer políticas y procedimientos de informes»: Establecer políticas y procedimientos de elaboración de informes que den respuesta a las diferentes necesidades del Directorio, la Alta Gerencia y los demás niveles de la organización, y que prevean la confirmación periódica por parte de lo…
- Obligacion «Directorio y Alta Gerencia: establecer requisitos de informes»: Tanto el Directorio como la Alta Gerencia deben establecer sus propios requisitos de elaboración de informes de riesgos y asegurarse de que solicitan y reciben información relevante que les permita cumplir con sus funciones, en relación con…
- Obligacion «Directorio: alertar cuando informes incumplen requisitos»: El Directorio debe alertar a la Alta Gerencia cuando los informes de riesgos no cumplan sus requisitos o no proporcionen el nivel o el tipo de información que le permitan controlar que la entidad esté operando dentro de su grado de toleranc…
- Obligacion «Directorio: advertir sobre desequilibrio información»: El Directorio debe advertirle cuando no se está obteniendo una relación equilibrada entre información detallada y cuantitativa e información cualitativa.
- Operacion «Elaboración de informes de riesgos»: Elaboración de informes de riesgos dirigidos al Directorio, la Alta Gerencia y demás niveles de la organización, con confirmación periódica de pertinencia y adecuación de la información agregada.
  - Obligacion:Establecer políticas y procedimientos de informes --establecida_en--> TextoOrdenado:Agregación de datos sobre riesgos (D-SIB)
  - Obligacion:Directorio y Alta Gerencia: establecer requisitos de informe… --establecida_en--> TextoOrdenado:Agregación de datos sobre riesgos (D-SIB)
  - Obligacion:Directorio: alertar cuando informes incumplen requisitos --establecida_en--> TextoOrdenado:Agregación de datos sobre riesgos (D-SIB)
  - Obligacion:Directorio: advertir sobre desequilibrio información --establecida_en--> TextoOrdenado:Agregación de datos sobre riesgos (D-SIB)
  - Operacion:Elaboración de informes de riesgos --establecida_en--> TextoOrdenado:Agregación de datos sobre riesgos (D-SIB)
  - Obligacion:Establecer políticas y procedimientos de informes --regula--> Operacion:Elaboración de informes de riesgos
  - Obligacion:Directorio y Alta Gerencia: establecer requisitos de informe… --regula--> Operacion:Elaboración de informes de riesgos
  - Obligacion:Establecer políticas y procedimientos de informes --aplica_a--> None
  - Obligacion:Directorio y Alta Gerencia: establecer requisitos de informe… --aplica_a--> Directorio
  - Obligacion:Directorio: alertar cuando informes incumplen requisitos --aplica_a--> Directorio
  - Obligacion:Directorio: advertir sobre desequilibrio información --aplica_a--> Directorio
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "Directorio", "verificada": "exacta", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "Directorio", "verificada": "exacta", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "Directorio", "verificada": "exacta", "sujeto_id": null}]; omisiones []; condicion_de []; limita []

**NUEVO** — error: None

- Obligacion «Establecer políticas y procedimientos de informes»: Deber de establecer políticas y procedimientos de elaboración de informes que satisfagan las necesidades del Directorio, Alta Gerencia y otros niveles de la organización, con confirmación periódica de la pertinencia y adecuación de la infor… ‖ tramo (no): «Las entidades financieras deben: Establecer políticas y procedimientos de elaboración de informes que den respuesta a las diferentes necesidades del Directorio,…»
- Obligacion «Directorio y Alta Gerencia establecen requisitos propios»: Tanto el Directorio como la Alta Gerencia deben establecer sus propios requisitos de elaboración de informes de riesgos y asegurar que solicitan y reciben información relevante para cumplir sus funciones respecto de la entidad y sus riesgos… ‖ tramo (exacta): «Tanto el Directorio como la Alta Gerencia deben establecer sus propios requisitos de elaboración de informes de riesgos y asegurarse de que solicitan y reciben …»
- Obligacion «Directorio alerta sobre informes de riesgos inadecuados»: El Directorio debe alertar a la Alta Gerencia cuando los informes de riesgos no cumplan sus requisitos o no proporcionen el nivel o tipo de información para controlar que la entidad opera dentro de su grado de tolerancia al/apetito por el r… ‖ tramo (exacta): «El Directorio debe alertar a la Alta Gerencia cuando los informes de riesgos no cumplan sus requisitos o no proporcionen el nivel o el tipo de información que l…»
- Obligacion «Directorio advierte sobre desequilibrio informativo»: El Directorio debe advertir a la Alta Gerencia cuando no existe una relación equilibrada entre información detallada cuantitativa e información cualitativa. ‖ tramo (exacta): «Además, el Directorio debe advertirle cuando no se está obteniendo una relación equilibrada entre información detallada y cuantitativa e información cualitativa…»
  - Obligacion:Establecer políticas y procedimientos de informes --establecida_en--> TextoOrdenado:Agregación de datos sobre riesgos D-SIB
  - Obligacion:Directorio y Alta Gerencia establecen requisitos propios --establecida_en--> TextoOrdenado:Agregación de datos sobre riesgos D-SIB
  - Obligacion:Directorio alerta sobre informes de riesgos inadecuados --establecida_en--> TextoOrdenado:Agregación de datos sobre riesgos D-SIB
  - Obligacion:Directorio advierte sobre desequilibrio informativo --establecida_en--> TextoOrdenado:Agregación de datos sobre riesgos D-SIB
  - Obligacion:Establecer políticas y procedimientos de informes --aplica_a--> Las entidades financieras
  - Obligacion:Directorio y Alta Gerencia establecen requisitos propios --aplica_a--> el Directorio
  - Obligacion:Directorio y Alta Gerencia establecen requisitos propios --aplica_a--> la Alta Gerencia
  - Obligacion:Directorio alerta sobre informes de riesgos inadecuados --aplica_a--> El Directorio
  - Obligacion:Directorio advierte sobre desequilibrio informativo --aplica_a--> el Directorio
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "Las entidades financieras", "verificada": "exacta", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "el Directorio", "verificada": "exacta", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "la Alta Gerencia", "verificada": "exacta", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "El Directorio", "verificada": "exacta", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "el Directorio", "verificada": "exacta", "sujeto_id": null}]; omisiones []; condicion_de []; limita []

*Cuantías en el texto propio: 0.*

## Ficha 28 — `ext::3.5.6.9`

**Texto propio:**

```
3.5.6.9. el cliente cuente con una “Certificación de aumento de exportaciones de
bienes” para los años 2021 a 2023 emitida en el marco de lo dispuesto en el
punto 3.18. por el equivalente del monto de capital que se abona.
```
**Último bloque heredado:** Las deudas comprendidas en este punto continuarán sujetas a la conformidad previa aun cuando existiese una modificación del acreedor o del deudor que conlleve a que ya no exista una vinculación entre el acreedor y el deudor residente.

**SELLADO** — error: None

- Condicion «Certificación aumento exportaciones bienes»: el cliente cuente con una "Certificación de aumento de exportaciones de bienes" para los años 2021 a 2023 emitida en el marco de lo dispuesto en el punto 3.18. por el equivalente del monto de capital que se abona
- Operacion «Pago de capital - endeudamiento financiero»: Pago de capital de endeudamientos financieros con acreedor vinculado, condicionado a conformidad previa del BCRA
  - Condicion:Certificación aumento exportaciones bienes --establecida_en--> TextoOrdenado:Operaciones en Mercado de Cambios - Exterior
  - Operacion:Pago de capital - endeudamiento financiero --establecida_en--> TextoOrdenado:Operaciones en Mercado de Cambios - Exterior
  - Condicion:Certificación aumento exportaciones bienes --condicion_de--> Operacion:Pago de capital - endeudamiento financiero
  - Operacion:Pago de capital - endeudamiento financiero --aplica_a--> None
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}]; omisiones []; condicion_de [{"de": "Condicion:Certificación aumento exportaciones bienes", "a": "Operacion:Pago de capital - endeudamiento financiero", "firma_nueva": true}]; limita []

**NUEVO** — error: None

- Condicion «Cliente con certificación de aumento de exportaciones»: El cliente cuenta con una Certificación de aumento de exportaciones de bienes para los años 2021 a 2023, emitida conforme al punto 3.18, por el equivalente del monto de capital que se abona ‖ tramo (exacta): «el cliente cuente con una "Certificación de aumento de exportaciones de bienes" para los años 2021 a 2023 emitida en el marco de lo dispuesto en el punto 3.18. …»
  - Condicion:Cliente con certificación de aumento de exportaciones --establecida_en--> TextoOrdenado:Exterior y cambios
- hechos: umbrales [{"entidad": "Condicion:Cliente con certificación de aumento de exportaciones", "tramo": "para los años 2021 a 2023", "verificacion": "exacta"}, {"entidad": "Condicion:Cliente con certificación de aumento de exportaciones", "tramo": "por el equivalente del monto de capital que se abona", "verificacion": "exacta"}]; menciones []; omisiones [{"categoria": "relacion_sin_predicado", "tramo": "emitida en el marco de lo dispuesto en el punto 3.18", "verificacion": "exacta", "nota": "referencia a otra norma; predicado sería 'referencia' pero la dirección es desde Condicion hacia pun…"}]; condicion_de []; limita []

*Cuantías en el texto propio: 0.*

## Ficha 29 — `adrei::4.4.1.1`

**Texto propio:**

```
4.4.1.1. Evaluar periódicamente el propósito de cada informe y establecer requisitos so-
bre la frecuencia con la que deben elaborarse tanto en situaciones normales co-
mo de estrés.
```
**Último bloque heredado:** Las entidades financieras deben:

**SELLADO** — error: None

- Obligacion «Evaluar periódicamente propósito cada informe»: Evaluar periódicamente el propósito de cada informe
- Obligacion «Establecer requisitos frecuencia informes»: Establecer requisitos sobre la frecuencia con la que deben elaborarse los informes tanto en situaciones normales como de estrés
  - Obligacion:Evaluar periódicamente propósito cada informe --establecida_en--> TextoOrdenado:Agregación de datos sobre riesgos D-SIB
  - Obligacion:Establecer requisitos frecuencia informes --establecida_en--> TextoOrdenado:Agregación de datos sobre riesgos D-SIB
  - Obligacion:Evaluar periódicamente propósito cada informe --aplica_a--> None
  - Obligacion:Establecer requisitos frecuencia informes --aplica_a--> None
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}]; omisiones []; condicion_de []; limita []

**NUEVO** — error: None

- Obligacion «Evaluar periódicamente propósito de informes»: Las entidades financieras deben evaluar periódicamente el propósito de cada informe ‖ tramo (exacta): «Evaluar periódicamente el propósito de cada informe»
- Obligacion «Establecer requisitos frecuencia informes situaciones normales y estrés»: Las entidades financieras deben establecer requisitos sobre la frecuencia con la que deben elaborarse los informes tanto en situaciones normales como de estrés ‖ tramo (exacta): «establecer requisitos sobre la frecuencia con la que deben elaborarse tanto en situaciones normales como de estrés»
  - Obligacion:Evaluar periódicamente propósito de informes --establecida_en--> TextoOrdenado:Agregación de datos sobre riesgos (D-SIB)
  - Obligacion:Establecer requisitos frecuencia informes situaciones normal… --establecida_en--> TextoOrdenado:Agregación de datos sobre riesgos (D-SIB)
  - Obligacion:Evaluar periódicamente propósito de informes --aplica_a--> Las entidades financieras
  - Obligacion:Establecer requisitos frecuencia informes situaciones normal… --aplica_a--> Las entidades financieras
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "Las entidades financieras", "verificada": "exacta", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "Las entidades financieras", "verificada": "exacta", "sujeto_id": null}]; omisiones []; condicion_de []; limita []

*Cuantías en el texto propio: 0.*

## Ficha 30 — `adrei::4.3.1.3`

**Texto propio:**

```
4.3.1.3. Elaborar un inventario y clasificación de los elementos de datos de riesgos que
incluya una referencia a los conceptos utilizados para elaborar los informes.
```
**Último bloque heredado:** Las entidades financieras deben:

**SELLADO** — error: None

- Obligacion «Inventario y clasificación de elementos de datos de riesgos»: Elaborar un inventario y clasificación de los elementos de datos de riesgos que incluya una referencia a los conceptos utilizados para elaborar los informes.
  - Obligacion:Inventario y clasificación de elementos de datos de riesgos --establecida_en--> TextoOrdenado:Agregación de datos sobre riesgos: D-SIB
  - Obligacion:Inventario y clasificación de elementos de datos de riesgos --aplica_a--> None
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}]; omisiones []; condicion_de []; limita []

**NUEVO** — error: None

- Obligacion «Elaborar inventario y clasificación de elementos de datos de riesgos»: Las entidades financieras deben elaborar un inventario y clasificación de los elementos de datos de riesgos que incluya una referencia a los conceptos utilizados para elaborar los informes. ‖ tramo (exacta): «Las entidades financieras deben: […] Elaborar un inventario y clasificación de los elementos de datos de riesgos que incluya una referencia a los conceptos util…»
  - Obligacion:Elaborar inventario y clasificación de elementos de datos de… --establecida_en--> TextoOrdenado:Agregación de datos sobre riesgos (D-SIB)
  - Obligacion:Elaborar inventario y clasificación de elementos de datos de… --aplica_a--> Las entidades financieras
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "Las entidades financieras", "verificada": "exacta", "sujeto_id": null}]; omisiones []; condicion_de []; limita []

*Cuantías en el texto propio: 0.*

## Ficha 31 — `cap::1.2`

**Texto propio:**

```
1.2. Exigencia básica.
Según la clase de entidad, serán las siguientes exigencias básicas:
[TABLA cap::tabla000 | página 4 | e0_tablas | columnas]
Rótulo: -En millones de pesos-
Columnas: Bancos | Restantes entidades (salvo Cajas de Crédito Cooperativas)
Fila 1: Bancos = 5.000 | Restantes entidades (salvo Cajas de Crédito Cooperativas) = 2.500
[FIN TABLA cap::tabla000]
Las compañías financieras que realicen, en forma directa, operaciones de comercio exterior
deberán observar las exigencias establecidas para los bancos.
```
**Último bloque heredado:** Sección 1. Capital mínimo.

**SELLADO** — error: None

- Operacion «Comercio exterior directo»: Operaciones de comercio exterior realizadas en forma directa por compañías financieras
- Restriccion «Exigencia capital mínimo 5.000 M$ entidades residuales»: Las restantes entidades (salvo Bancos y Cajas de Crédito Cooperativas) deberán mantener un capital mínimo de 5.000 millones de pesos
- Restriccion «Exigencia capital mínimo 2.500 M$ bancos»: Los bancos (salvo Cajas de Crédito Cooperativas) deberán mantener un capital mínimo de 2.500 millones de pesos
- Excepcion «Cajas de Crédito Cooperativas exoneradas»: Las Cajas de Crédito Cooperativas están exceptuadas de las exigencias de capital mínimo enunciadas
- Obligacion «Observar exigencias bancos comercio exterior»: Las compañías financieras que realicen, en forma directa, operaciones de comercio exterior deberán observar las exigencias establecidas para los bancos
  - Restriccion:Exigencia capital mínimo 5.000 M$ entidades residuales --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Restriccion:Exigencia capital mínimo 2.500 M$ bancos --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Excepcion:Cajas de Crédito Cooperativas exoneradas --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Obligacion:Observar exigencias bancos comercio exterior --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Restriccion:Exigencia capital mínimo 5.000 M$ entidades residuales --aplica_a--> Restantes entidades
  - Restriccion:Exigencia capital mínimo 2.500 M$ bancos --aplica_a--> None
  - Excepcion:Cajas de Crédito Cooperativas exoneradas --aplica_a--> None
  - Obligacion:Observar exigencias bancos comercio exterior --aplica_a--> None
  - Obligacion:Observar exigencias bancos comercio exterior --condiciona--> Operacion:Comercio exterior directo
  - Restriccion:Exigencia capital mínimo 5.000 M$ entidades residuales --limita--> Operacion:Comercio exterior directo
  - Restriccion:Exigencia capital mínimo 2.500 M$ bancos --limita--> Operacion:Comercio exterior directo
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "Restantes entidades", "verificada": "exacta", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}]; omisiones []; condicion_de []; limita [{"de": "Restriccion:Exigencia capital mínimo 5.000 M$ entidades residuales", "a": "Operacion:Comercio exterior directo"}, {"de": "Restriccion:Exigencia capital mínimo 2.500 M$ bancos", "a": "Operacion:Comercio exterior directo"}]

**NUEVO** — error: None

- Restriccion «Exigencia básica 5000 millones pesos bancos»: Exigencia básica de capital mínimo de 5.000 millones de pesos para bancos ‖ tramo (exacta): «serán las siguientes exigencias básicas: [...] Bancos = 5.000»
- Restriccion «Exigencia básica 2500 millones pesos entidades restantes»: Exigencia básica de capital mínimo de 2.500 millones de pesos para restantes entidades, salvo Cajas de Crédito Cooperativas ‖ tramo (exacta): «serán las siguientes exigencias básicas: [...] Restantes entidades (salvo Cajas de Crédito Cooperativas) = 2.500»
- Restriccion «Equiparación compañías financieras comercio exterior»: Las compañías financieras que realicen operaciones de comercio exterior en forma directa deben observar las exigencias básicas establecidas para bancos (5.000 millones de pesos) ‖ tramo (exacta): «Las compañías financieras que realicen, en forma directa, operaciones de comercio exterior deberán observar las exigencias establecidas para los bancos»
  - Restriccion:Exigencia básica 5000 millones pesos bancos --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Restriccion:Exigencia básica 2500 millones pesos entidades restantes --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Restriccion:Equiparación compañías financieras comercio exterior --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Restriccion:Exigencia básica 5000 millones pesos bancos --aplica_a--> Bancos
  - Restriccion:Exigencia básica 2500 millones pesos entidades restantes --aplica_a--> Restantes entidades (salvo Cajas de Crédito Cooperativas)
  - Restriccion:Equiparación compañías financieras comercio exterior --aplica_a--> Las compañías financieras que realicen, en forma directa, operaciones de comercio exterior
- hechos: umbrales [{"entidad": "Restriccion:Exigencia básica 5000 millones pesos bancos", "tramo": "5.000", "verificacion": "exacta"}, {"entidad": "Restriccion:Exigencia básica 2500 millones pesos entidades restantes", "tramo": "2.500", "verificacion": "exacta"}, {"entidad": "Restriccion:Equiparación compañías financieras comercio exterior", "tramo": "5.000", "verificacion": "exacta"}]; menciones [{"pred": "aplica_a", "mencion": "Bancos", "verificada": "exacta", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "Restantes entidades (salvo Cajas de Crédito Cooperativas)", "verificada": "exacta", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "Las compañías financieras que realicen, en forma directa, operaciones de comerci…", "verificada": "exacta", "sujeto_id": null}]; omisiones [{"categoria": "fuera_de_tipos", "tramo": "Según la clase de entidad", "verificacion": "exacta", "nota": "Enunciado introductorio que anuncia la estructura de la tabla; no prescribe conducta ni tiene conten…"}]; condicion_de []; limita []

*Cuantías en el texto propio: 0.*

## Ficha 32 — `ric::5.2.4`

**Texto propio:**

```
5.2.4. Correlación con partidas del Balance de Saldos
[TABLA ric::tabla018 | página 26 | e0_tablas | columnas]
Columnas: Código | Concepto | Cuentas Contables
Fila 1: Código = 3510000X | Concepto = Ingresos financieros | Cuentas Contables = 510000 excepto parte pertinente de 511102 / 515102 / 511099 / 511106 / 515099 / 515106 / 511541 / 515541
Fila 2: Código = 3520000X | Concepto = Egresos financieros | Cuentas Contables = 520000 excepto 521023 / 521036 / 521074 / 525004 y parte pertinente de 521103 / 525103 / 521107 / 521101 / 525107 / 525101 / 521541 / 525541
Fila 3: Código = 3530000X | Concepto = Ingresos por servicios | Cuentas Contables = 540000 excepto parte pertinente de 541018 / 545018
Fila 4: Código = 3540000X | Concepto = Egresos por servicios | Cuentas Contables = 550000 excepto parte pertinente de 551018 / 555018
Fila 5: Código = 3550000X | Concepto = Utilidades diversas | Cuentas Contables = 570000 excepto 570006 / 570009 / 570021 / 570024 y parte pertinente de 570003 / 570025 / 570045 / 570034
Fila 6: Código = 3560000X | Concepto = Pérdidas diversas | Cuentas Contables = 580000 excepto 580006 / 580009 / 580018 / 580021 / 580027 / 580031 / 580033 y parte pertinente de 580003 / 580035 / 580045 / 580041 / 580046 / 580047 / 580048 / 580050 / 580056
Fila 7: Código = 3570000X | Concepto = Resultado Monetario total | Cuentas Contables = 620000
[FIN TABLA ric::tabla018]
```
**Último bloque heredado:** 5.2. Modelo de información

**SELLADO** — error: None

- Definicion «Correlación partidas Balance Saldos — Ingresos financieros»: Corresponde a cuentas contables del rubro 510000 excepto parte pertinente de 511102 / 515102 / 511099 / 511106 / 515099 / 515106 / 511541 / 515541, y del rubro 520000 excepto 521023 / 521036 / 521074 / 525004 y parte pertinente de 521103 / …
- Definicion «Correlación partidas Balance Saldos — Egresos financieros»: Corresponde a cuentas contables del rubro 520000 excepto 521023 / 521036 / 521074 / 525004 y parte pertinente de 521103 / 525103 / 521107 / 521101 / 525107 / 525101 / 521541 / 525541
- Definicion «Correlación partidas Balance Saldos — Ingresos por servicios»: Corresponde a cuentas contables del rubro 540000 excepto parte pertinente de 541018 / 545018
- Definicion «Correlación partidas Balance Saldos — Egresos por servicios»: Corresponde a cuentas contables del rubro 550000 excepto parte pertinente de 551018 / 555018
- Definicion «Correlación partidas Balance Saldos — Utilidades diversas»: Corresponde a cuentas contables del rubro 570000 excepto 570006 / 570009 / 570021 / 570024 y parte pertinente de 570003 / 570025 / 570045 / 570034
- Definicion «Correlación partidas Balance Saldos — Pérdidas diversas»: Corresponde a cuentas contables del rubro 580000 excepto 580006 / 580009 / 580018 / 580021 / 580027 / 580031 / 580033 y parte pertinente de 580003 / 580035 / 580045 / 580041 / 580046 / 580047 / 580048 / 580050 / 580056
- Definicion «Correlación partidas Balance Saldos — Resultado Monetario total»: Corresponde a cuentas contables del rubro 620000
  - Definicion:Correlación partidas Balance Saldos — Ingresos financieros --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Definicion:Correlación partidas Balance Saldos — Egresos financieros --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Definicion:Correlación partidas Balance Saldos — Ingresos por servicios --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Definicion:Correlación partidas Balance Saldos — Egresos por servicios --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Definicion:Correlación partidas Balance Saldos — Utilidades diversas --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Definicion:Correlación partidas Balance Saldos — Pérdidas diversas --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Definicion:Correlación partidas Balance Saldos — Resultado Monetario to… --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
- hechos: umbrales []; menciones []; omisiones [{"categoria": null, "tramo": "", "verificacion": "ausente", "nota": "Tabla de correlación completa: estructura tabular no confiable, mapeos de códigos de concepto a núme…"}]; condicion_de []; limita []

**NUEVO** — error: None

- Operacion «Correlación — Ingresos financieros con Balance de Saldos»: Correlación del concepto de Ingresos financieros (código 3510000X) con las cuentas contables del Balance de Saldos, específicamente la cuenta 510000 excepto las partidas pertinentes de 511102, 515102, 511099, 511106, 515099, 515106, 511541 … ‖ tramo (exacta): «Código = 3510000X | Concepto = Ingresos financieros | Cuentas Contables = 510000 excepto parte pertinente de 511102 / 515102 / 511099 / 511106 / 515099 / 515106…»
- Operacion «Correlación — Egresos financieros con Balance de Saldos»: Correlación del concepto de Egresos financieros (código 3520000X) con las cuentas contables del Balance de Saldos, específicamente la cuenta 520000 excepto 521023, 521036, 521074, 525004 y las partes pertinentes de 521103, 525103, 521107, 5… ‖ tramo (exacta): «Código = 3520000X | Concepto = Egresos financieros | Cuentas Contables = 520000 excepto 521023 / 521036 / 521074 / 525004 y parte pertinente de 521103 / 525103 …»
- Operacion «Correlación — Ingresos por servicios con Balance de Saldos»: Correlación del concepto de Ingresos por servicios (código 3530000X) con las cuentas contables del Balance de Saldos, específicamente la cuenta 540000 excepto las partes pertinentes de 541018 y 545018. ‖ tramo (exacta): «Código = 3530000X | Concepto = Ingresos por servicios | Cuentas Contables = 540000 excepto parte pertinente de 541018 / 545018»
- Operacion «Correlación — Egresos por servicios con Balance de Saldos»: Correlación del concepto de Egresos por servicios (código 3540000X) con las cuentas contables del Balance de Saldos, específicamente la cuenta 550000 excepto las partes pertinentes de 551018 y 555018. ‖ tramo (exacta): «Código = 3540000X | Concepto = Egresos por servicios | Cuentas Contables = 550000 excepto parte pertinente de 551018 / 555018»
- Operacion «Correlación — Utilidades diversas con Balance de Saldos»: Correlación del concepto de Utilidades diversas (código 3550000X) con las cuentas contables del Balance de Saldos, específicamente la cuenta 570000 excepto 570006, 570009, 570021, 570024 y las partes pertinentes de 570003, 570025, 570045 y … ‖ tramo (exacta): «Código = 3550000X | Concepto = Utilidades diversas | Cuentas Contables = 570000 excepto 570006 / 570009 / 570021 / 570024 y parte pertinente de 570003 / 570025 …»
- Operacion «Correlación — Pérdidas diversas con Balance de Saldos»: Correlación del concepto de Pérdidas diversas (código 3560000X) con las cuentas contables del Balance de Saldos, específicamente la cuenta 580000 excepto 580006, 580009, 580018, 580021, 580027, 580031, 580033 y las partes pertinentes de 580… ‖ tramo (exacta): «Código = 3560000X | Concepto = Pérdidas diversas | Cuentas Contables = 580000 excepto 580006 / 580009 / 580018 / 580021 / 580027 / 580031 / 580033 y parte perti…»
- Operacion «Correlación — Resultado Monetario total con Balance de Saldos»: Correlación del concepto de Resultado Monetario total (código 3570000X) con la cuenta contable 620000 del Balance de Saldos. ‖ tramo (exacta): «Código = 3570000X | Concepto = Resultado Monetario total | Cuentas Contables = 620000»
  - Operacion:Correlación — Ingresos financieros con Balance de Saldos --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Operacion:Correlación — Egresos financieros con Balance de Saldos --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Operacion:Correlación — Ingresos por servicios con Balance de Saldos --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Operacion:Correlación — Egresos por servicios con Balance de Saldos --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Operacion:Correlación — Utilidades diversas con Balance de Saldos --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Operacion:Correlación — Pérdidas diversas con Balance de Saldos --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Operacion:Correlación — Resultado Monetario total con Balance de Saldo… --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
- hechos: umbrales []; menciones []; omisiones []; condicion_de []; limita []

*Cuantías en el texto propio: 0.*

## Ficha 33 — `cla::7.4`

**Texto propio:**

```
7.4. Información a la SEFyC sobre incrementos de la cartera irregular.
En los casos en que la expresión que seguidamente se establece sea mayor al 5 % al último
día de un trimestre calendario o al 10 % en un año, la entidad financiera deberá informar el ori-
gen de dicha circunstancia a la SEFyC debiendo brindar las explicaciones que les sean reque-
ridas y, de corresponder, las modificaciones a realizar en su política de crédito tendientes a me-
jorar la calidad de su cartera crediticia.
FICC - FICC - Máx (FICCS - FICCS ; 0)
T T-1 T T-1
Siendo:
FICC: cociente, expresado en tanto por ciento, entre el importe total de las financiaciones de
la cartera de consumo o vivienda, de la entidad financiera, clasificadas en situación 3 a
5 según las normas sobre “Clasificación de deudores” y el importe total de sus finan-
ciaciones de la cartera de consumo o vivienda.
FICCS: cociente, expresado en tanto por ciento, entre el importe total de las financiaciones de
la cartera de consumo o vivienda, del total del sistema financiero, clasificadas en si-
tuación 3 a 5 según las normas sobre “Clasificación de deudores” y el importe total de
sus financiaciones de la cartera de consumo o vivienda, según la información que dé a
conocer el BCRA.
T: el último día de un trimestre calendario al que corresponda el cálculo del cociente.
T-1: el último día del trimestre calendario inmediato anterior y el último día del mismo tri-
mestre correspondiente al año anterior, según corresponda.
```
**Último bloque heredado:** Sección 7. Clasificación de los deudores de la cartera para consumo o vivienda.

**SELLADO** — error: None

- Condicion «Incremento cartera irregular > 5% trimestral o > 10% anual»: Cuando la expresión FICC sea mayor al 5% al último día de un trimestre calendario o al 10% en un año
- Obligacion «Informar origen incremento cartera irregular a SEFyC»: La entidad financiera deberá informar el origen de dicha circunstancia a la SEFyC debiendo brindar las explicaciones que les sean requeridas y, de corresponder, las modificaciones a realizar en su política de crédito tendientes a mejorar la…
- Definicion «FICC - Índice cartera irregular entidad»: Cociente, expresado en tanto por ciento, entre el importe total de las financiaciones de la cartera de consumo o vivienda, de la entidad financiera, clasificadas en situación 3 a 5 según las normas sobre 'Clasificación de deudores' y el imp…
- Definicion «FICCS - Índice cartera irregular sistema»: Cociente, expresado en tanto por ciento, entre el importe total de las financiaciones de la cartera de consumo o vivienda, del total del sistema financiero, clasificadas en situación 3 a 5 según las normas sobre 'Clasificación de deudores' …
- Definicion «T - Período trimestral para cálculo»: El último día de un trimestre calendario al que corresponda el cálculo del cociente.
- Definicion «T-1 - Período comparativo anterior»: El último día del trimestre calendario inmediato anterior y el último día del mismo trimestre correspondiente al año anterior, según corresponda.
  - Condicion:Incremento cartera irregular > 5% trimestral o > 10% anual --establecida_en--> TextoOrdenado:Clasificación de deudores
  - Obligacion:Informar origen incremento cartera irregular a SEFyC --establecida_en--> TextoOrdenado:Clasificación de deudores
  - Definicion:FICC - Índice cartera irregular entidad --establecida_en--> TextoOrdenado:Clasificación de deudores
  - Definicion:FICCS - Índice cartera irregular sistema --establecida_en--> TextoOrdenado:Clasificación de deudores
  - Definicion:T - Período trimestral para cálculo --establecida_en--> TextoOrdenado:Clasificación de deudores
  - Definicion:T-1 - Período comparativo anterior --establecida_en--> TextoOrdenado:Clasificación de deudores
  - Condicion:Incremento cartera irregular > 5% trimestral o > 10% anual --condicion_de--> Obligacion:Informar origen incremento cartera irregular a SEFyC
  - Obligacion:Informar origen incremento cartera irregular a SEFyC --aplica_a--> None
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}]; omisiones [{"categoria": null, "tramo": "", "verificacion": "ausente", "nota": "Fórmula FICC - FICC con función MAX: estructura de cálculo con subíndices (T, T-1) no extraída de ta…"}]; condicion_de [{"de": "Condicion:Incremento cartera irregular > 5% trimestral o > 10% anual", "a": "Obligacion:Informar origen incremento cartera irregular a SEFyC", "firma_nueva": false}]; limita []

**NUEVO** — error: None

- Condicion «Incremento cartera irregular > 5% trimestre o > 10% anual»: La cartera irregular (FICC) resulta mayor al 5% al último día de un trimestre calendario o al 10% en un año ‖ tramo (exacta): «En los casos en que la expresión que seguidamente se establece sea mayor al 5 % al último día de un trimestre calendario o al 10 % en un año»
- Obligacion «Informar origen incremento cartera irregular»: La entidad financiera debe informar el origen del incremento de la cartera irregular a la SEFyC ‖ tramo (exacta): «la entidad financiera deberá informar el origen de dicha circunstancia a la SEFyC»
- Obligacion «Brindar explicaciones requeridas por SEFyC»: La entidad debe brindar a la SEFyC las explicaciones que sean requeridas sobre el incremento ‖ tramo (exacta): «debiendo brindar las explicaciones que les sean requeridas»
- Obligacion «Implementar modificaciones política de crédito»: De corresponder, la entidad debe realizar las modificaciones necesarias en su política de crédito para mejorar la calidad de su cartera crediticia ‖ tramo (exacta): «de corresponder, las modificaciones a realizar en su política de crédito tendientes a mejorar la calidad de su cartera crediticia»
- Definicion «FICC: índice cartera irregular propia»: Cociente porcentual entre el importe total de financiaciones de cartera de consumo o vivienda clasificadas en situación 3 a 5 de la entidad financiera y el importe total de sus financiaciones de cartera de consumo o vivienda ‖ tramo (exacta): «FICC: cociente, expresado en tanto por ciento, entre el importe total de las financiaciones de la cartera de consumo o vivienda, de la entidad financiera, clasi…»
- Definicion «FICCS: índice cartera irregular sistema»: Cociente porcentual entre el importe total de financiaciones de cartera de consumo o vivienda del sistema financiero clasificadas en situación 3 a 5 y el importe total de sus financiaciones de cartera de consumo o vivienda, según informació… ‖ tramo (exacta): «FICCS: cociente, expresado en tanto por ciento, entre el importe total de las financiaciones de la cartera de consumo o vivienda, del total del sistema financie…»
- Definicion «T: período de cálculo trimestral»: El último día de un trimestre calendario al que corresponda el cálculo del cociente ‖ tramo (exacta): «T: el último día de un trimestre calendario al que corresponda el cálculo del cociente.»
- Definicion «T-1: períodos de comparación»: El último día del trimestre calendario inmediato anterior y el último día del mismo trimestre correspondiente al año anterior, según corresponda ‖ tramo (exacta): «T-1: el último día del trimestre calendario inmediato anterior y el último día del mismo trimestre correspondiente al año anterior, según corresponda.»
  - Condicion:Incremento cartera irregular > 5% trimestre o > 10% anual --establecida_en--> TextoOrdenado:Clasificación de deudores
  - Obligacion:Informar origen incremento cartera irregular --establecida_en--> TextoOrdenado:Clasificación de deudores
  - Obligacion:Brindar explicaciones requeridas por SEFyC --establecida_en--> TextoOrdenado:Clasificación de deudores
  - Obligacion:Implementar modificaciones política de crédito --establecida_en--> TextoOrdenado:Clasificación de deudores
  - Definicion:FICC: índice cartera irregular propia --establecida_en--> TextoOrdenado:Clasificación de deudores
  - Definicion:FICCS: índice cartera irregular sistema --establecida_en--> TextoOrdenado:Clasificación de deudores
  - Definicion:T: período de cálculo trimestral --establecida_en--> TextoOrdenado:Clasificación de deudores
  - Definicion:T-1: períodos de comparación --establecida_en--> TextoOrdenado:Clasificación de deudores
  - Obligacion:Informar origen incremento cartera irregular --aplica_a--> la entidad financiera
  - Obligacion:Brindar explicaciones requeridas por SEFyC --aplica_a--> la entidad financiera
  - Obligacion:Implementar modificaciones política de crédito --aplica_a--> la entidad financiera
  - Condicion:Incremento cartera irregular > 5% trimestre o > 10% anual --condicion_de--> Obligacion:Informar origen incremento cartera irregular
- hechos: umbrales [{"entidad": "Condicion:Incremento cartera irregular > 5% trimestre o > 10% anual", "tramo": "mayor al 5 % al último día de un trimestre calendario", "verificacion": "exacta"}, {"entidad": "Condicion:Incremento cartera irregular > 5% trimestre o > 10% anual", "tramo": "al 10 % en un año", "verificacion": "exacta"}]; menciones [{"pred": "aplica_a", "mencion": "la entidad financiera", "verificada": "exacta", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "la entidad financiera", "verificada": "exacta", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "la entidad financiera", "verificada": "exacta", "sujeto_id": null}]; omisiones [{"categoria": "formula", "tramo": "FICC - FICC - Máx (FICCS - FICCS ; 0)", "verificacion": "exacta", "nota": "Fórmula de cálculo del incremento de la cartera irregular. No se extraen valores numéricos de conten…"}]; condicion_de [{"de": "Condicion:Incremento cartera irregular > 5% trimestre o > 10% anual", "a": "Obligacion:Informar origen incremento cartera irregular", "firma_nueva": false}]; limita []

*Cuantías en el texto propio: 3.*

## Ficha 34 — `ctacte::6.2.4`

**Texto propio:**

```
6.2.4. Se observen faltas de ortografía.
```
**Último bloque heredado:** Idéntico tratamiento corresponderá aplicar a los cheques de pago diferido registrados, aun cuando contengan defectos formales.

**SELLADO** — error: None

- Condicion «Faltas de ortografía»: Se observen faltas de ortografía
  - Condicion:Faltas de ortografía --establecida_en--> TextoOrdenado:Cuentas de corresponsalía
  - rechazo: ref_colgante: relations[1] (condicion_de): source='e1' target='e2'
- hechos: umbrales []; menciones []; omisiones []; condicion_de []; limita []

**NUEVO** — error: None

- Excepcion «Faltas de ortografía — cheques atendidos»: Los cheques serán atendidos aunque contengan faltas de ortografía, por lo que esta deficiencia formal no es causa de rechazo. ‖ tramo (exacta): «Se observen faltas de ortografía»
  - Excepcion:Faltas de ortografía — cheques atendidos --establecida_en--> TextoOrdenado:Cuentas de Corresponsalía
  - rechazo: ref_colgante: relations[1] (exceptua): source='e1' target='e2'
- hechos: umbrales []; menciones []; omisiones [{"categoria": "relacion_sin_predicado", "tramo": "Serán atendidos los cheques presentados al cobro, no comprendidos en las situaciones previstas en el…", "verificacion": "no", "nota": "La relación entre la Excepcion (faltas de ortografía) y la Operacion subyacente (atención/cobro de c…"}]; condicion_de []; limita []

*Cuantías en el texto propio: 0.*

## Ficha 35 — `ric::8.1.6`

**Texto propio:**

```
8.1.6. Código 70200000.
Responsabilidad patrimonial computable: (CO -CD ) + (CA -CD ) + (PNc-CD )
n1 COn1 n1 CAn1 PNc
```
**Último bloque heredado:** 8.1. Normas de procedimiento.

**SELLADO** — error: None

- Definicion «Responsabilidad patrimonial computable — Código 70200000»: (CO n1 - CD n1) + (CA n1 - CD n1) + (PNc - CD PNc)
  - Definicion:Responsabilidad patrimonial computable — Código 70200000 --establecida_en--> TextoOrdenado:Texto Ordenado Régimen Informativo
- hechos: umbrales []; menciones []; omisiones [{"categoria": null, "tramo": "", "verificacion": "ausente", "nota": "Fórmula matemática de cálculo: estructura de fórmula con variables (CO, CD, CA, PNc) y subíndices (n…"}]; condicion_de []; limita []

**NUEVO** — error: None

- Definicion «Responsabilidad patrimonial computable»: (CO -CD ) + (CA -CD ) + (PNc-CD ) ‖ tramo (exacta): «Responsabilidad patrimonial computable: (CO -CD ) + (CA -CD ) + (PNc-CD )»
  - Definicion:Responsabilidad patrimonial computable --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
- hechos: umbrales []; menciones []; omisiones [{"categoria": "formula", "tramo": "n1 COn1 n1 CAn1 PNc", "verificacion": "exacta", "nota": "Fórmula con subíndices no reconstruidos confiablemente desde el PDF; la estructura de exponentes y r…"}]; condicion_de []; limita []

*Cuantías en el texto propio: 0.*

## Ficha 36 — `ayccef::4.2.7.2`

**Texto propio:**

```
4.2.7.2. Los sistemas informáticos.
```
**Último bloque heredado:** 4.2.7. Tener calificación 1, 2 o 3 de la SEFyC, en todos los siguientes aspectos:

**SELLADO** — error: None

- hechos: umbrales []; menciones []; omisiones []; condicion_de []; limita []

**NUEVO** — error: None

- Definicion «Aspecto calificable: sistemas informáticos»: Aspecto específico de calificación que las entidades financieras deben tener con calificación 1, 2 o 3 de la SEFyC según la condición básica para transformación ‖ tramo (exacta): «Los sistemas informáticos»
  - Definicion:Aspecto calificable: sistemas informáticos --establecida_en--> TextoOrdenado:Texto Ordenado Autorización y Cambios de Control en Entidade…
- hechos: umbrales []; menciones []; omisiones [{"categoria": "meta_normativo", "tramo": "Los sistemas informáticos.", "verificacion": "exacta", "nota": "El punto contiene solo el nombre de un aspecto de calificación que es un encabezado de subsección va…"}]; condicion_de []; limita []

*Cuantías en el texto propio: 0.*

## Ficha 37 — `ext::10.2.5`

**Texto propio:**

```
10.2.5. Proveedor del exterior.
A los efectos de la normativa cambiaria se considerará proveedor del exterior a quien
ha emitido o emitirá la factura comercial en el exterior a nombre del comprador
residente que accede al mercado de cambios.
Asimismo, las entidades podrán considerar como equivalente a un pago a un
proveedor del exterior, a aquellos pagos que se realicen a un beneficiario del exterior
distinto de quien emitió la factura comercial, en la medida que cuenten con
documentación que le permita acreditar que ambas empresas del exterior forman
parte de un mismo grupo económico y que la intervención de ambas en la operación
está asociada a cuestiones administrativas y/u operacionales internas de dicho grupo,
que son ajenas a la voluntad del importador argentino.
Las entidades también podrán admitir la afectación de bienes remitidos por una
empresa distinta de la que fuera beneficiaria del pago sin registro de ingreso
aduanero cuando se verifique lo indicado en párrafo precedente.
```
**Último bloque heredado:** 10.2. Definiciones.

**SELLADO** — error: None

- Definicion «Proveedor del exterior — factura comercial»: A quien ha emitido o emitirá la factura comercial en el exterior a nombre del comprador residente que accede al mercado de cambios.
- Potestad «Considerar pago equivalente a beneficiario distinto»: Las entidades podrán considerar como equivalente a un pago a un proveedor del exterior, a aquellos pagos que se realicen a un beneficiario del exterior distinto de quien emitió la factura comercial, en la medida que cuenten con documentació…
- Condicion «Grupo económico y razones administrativas/operacionales»: Cuando ambas empresas del exterior forman parte de un mismo grupo económico y la intervención de ambas en la operación está asociada a cuestiones administrativas y/u operacionales internas de dicho grupo, que son ajenas a la voluntad del im…
- Potestad «Admitir afectación de bienes remitidos por empresa distinta»: Las entidades también podrán admitir la afectación de bienes remitidos por una empresa distinta de la que fuera beneficiaria del pago sin registro de ingreso aduanero cuando se verifique lo indicado en párrafo precedente.
- Condicion «Sin registro de ingreso aduanero — mismo grupo económico»: Cuando los bienes sean remitidos por una empresa distinta de la que fuera beneficiaria del pago sin registro de ingreso aduanero y se verifique lo indicado en el párrafo precedente (grupo económico y razones administrativas/operacionales).
  - Definicion:Proveedor del exterior — factura comercial --establecida_en--> TextoOrdenado:Exterior cambios
  - Potestad:Considerar pago equivalente a beneficiario distinto --establecida_en--> TextoOrdenado:Exterior cambios
  - Condicion:Grupo económico y razones administrativas/operacionales --establecida_en--> TextoOrdenado:Exterior cambios
  - Potestad:Admitir afectación de bienes remitidos por empresa distinta --establecida_en--> TextoOrdenado:Exterior cambios
  - Condicion:Sin registro de ingreso aduanero — mismo grupo económico --establecida_en--> TextoOrdenado:Exterior cambios
  - Condicion:Grupo económico y razones administrativas/operacionales --condicion_de--> Potestad:Considerar pago equivalente a beneficiario distinto
  - Condicion:Sin registro de ingreso aduanero — mismo grupo económico --condicion_de--> Potestad:Admitir afectación de bienes remitidos por empresa distinta
  - Potestad:Considerar pago equivalente a beneficiario distinto --aplica_a--> None
  - Potestad:Admitir afectación de bienes remitidos por empresa distinta --aplica_a--> None
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}]; omisiones []; condicion_de [{"de": "Condicion:Grupo económico y razones administrativas/operacionales", "a": "Potestad:Considerar pago equivalente a beneficiario distinto", "firma_nueva": true}, {"de": "Condicion:Sin registro de ingreso aduanero — mismo grupo económico", "a": "Potestad:Admitir afectación de bienes remitidos por empresa distinta", "firma_nueva": true}]; limita []

**NUEVO** — error: None

- Definicion «Proveedor del exterior»: Quien ha emitido o emitirá la factura comercial en el exterior a nombre del comprador residente que accede al mercado de cambios. ‖ tramo (exacta): «A los efectos de la normativa cambiaria se considerará proveedor del exterior a quien ha emitido o emitirá la factura comercial en el exterior a nombre del comp…»
- Potestad «Consideración de pago equivalente — beneficiario exterior distinto»: Las entidades pueden considerar como equivalente a un pago a proveedor del exterior los pagos a beneficiario exterior distinto del que emitió la factura, si cuentan con documentación que acredite que ambas empresas forman parte del mismo gr… ‖ tramo (exacta): «las entidades podrán considerar como equivalente a un pago a un proveedor del exterior, a aquellos pagos que se realicen a un beneficiario del exterior distinto…»
- Condicion «Grupo económico y documentación acreditativa»: Posesión de documentación que acredite que ambas empresas exteriores forman parte del mismo grupo económico y que su intervención responde a cuestiones administrativas u operacionales internas ajenas a la voluntad del importador argentino. ‖ tramo (exacta): «en la medida que cuenten con documentación que le permita acreditar que ambas empresas del exterior forman parte de un mismo grupo económico y que la intervenci…»
- Potestad «Admisión de afectación de bienes sin registro aduanero»: Las entidades pueden admitir la afectación de bienes remitidos por una empresa distinta de la beneficiaria del pago sin que exista registro de ingreso aduanero, cuando se verifiquen las condiciones del párrafo precedente. ‖ tramo (exacta): «Las entidades también podrán admitir la afectación de bienes remitidos por una empresa distinta de la que fuera beneficiaria del pago sin registro de ingreso ad…»
- Condicion «Verificación de condiciones precedentes»: Que se verifiquen las condiciones establecidas en el párrafo precedente respecto al grupo económico y la documentación acreditativa. ‖ tramo (exacta): «cuando se verifique lo indicado en párrafo precedente.»
  - Definicion:Proveedor del exterior --establecida_en--> TextoOrdenado:Exterior cambios
  - Potestad:Consideración de pago equivalente — beneficiario exterior di… --establecida_en--> TextoOrdenado:Exterior cambios
  - Condicion:Grupo económico y documentación acreditativa --establecida_en--> TextoOrdenado:Exterior cambios
  - Potestad:Admisión de afectación de bienes sin registro aduanero --establecida_en--> TextoOrdenado:Exterior cambios
  - Condicion:Verificación de condiciones precedentes --establecida_en--> TextoOrdenado:Exterior cambios
  - Condicion:Grupo económico y documentación acreditativa --condicion_de--> Potestad:Consideración de pago equivalente — beneficiario exterior di…
  - Condicion:Verificación de condiciones precedentes --condicion_de--> Potestad:Admisión de afectación de bienes sin registro aduanero
  - Potestad:Consideración de pago equivalente — beneficiario exterior di… --aplica_a--> las entidades
  - Potestad:Admisión de afectación de bienes sin registro aduanero --aplica_a--> Las entidades
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "las entidades", "verificada": "exacta", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "Las entidades", "verificada": "exacta", "sujeto_id": null}]; omisiones []; condicion_de [{"de": "Condicion:Grupo económico y documentación acreditativa", "a": "Potestad:Consideración de pago equivalente — beneficiario exterior di…", "firma_nueva": true}, {"de": "Condicion:Verificación de condiciones precedentes", "a": "Potestad:Admisión de afectación de bienes sin registro aduanero", "firma_nueva": true}]; limita []

*Cuantías en el texto propio: 0.*

## Ficha 38 — `expaef::2.2.6.5`

**Texto propio:**

```
2.2.6.5. Todo resguardo de documentación original, cuando normas legales, reglamen-
tarias y/o disposiciones del Banco Central de la República Argentina (BCRA)
determinen cursos de acción específicos.
```
**Último bloque heredado:** 2.2.6. Deberán mantenerse en la República Argentina:

**SELLADO** — error: None

- Obligacion «Resguardo documentación original»: Todo resguardo de documentación original, cuando normas legales, reglamentarias y/o disposiciones del Banco Central de la República Argentina (BCRA) determinen cursos de acción específicos.
  - Obligacion:Resguardo documentación original --establecida_en--> TextoOrdenado:Tercerización de actividades
  - Obligacion:Resguardo documentación original --aplica_a--> None
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}]; omisiones []; condicion_de []; limita []

**NUEVO** — error: None

- Obligacion «Mantenimiento de resguardo de documentación original»: Las entidades financieras deberán mantener en la República Argentina todo resguardo de documentación original cuando normas legales, reglamentarias y/o disposiciones del BCRA determinen cursos de acción específicos. ‖ tramo (no): «Deberán mantenerse en la República Argentina: Todo resguardo de documentación original, cuando normas legales, reglamentarias y/o disposiciones del Banco Centra…»
  - Obligacion:Mantenimiento de resguardo de documentación original --establecida_en--> TextoOrdenado:Tercerización de actividades
  - Obligacion:Mantenimiento de resguardo de documentación original --aplica_a--> Las entidades
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "Las entidades", "verificada": "no", "sujeto_id": null}]; omisiones [{"categoria": "meta_normativo", "tramo": "cuando normas legales, reglamentarias y/o disposiciones del Banco Central de la República Argentina …", "verificacion": "exacta", "nota": "Cláusula condicional que clarifica el alcance de la obligación principal, pero cuya función es inter…"}]; condicion_de []; limita []

*Cuantías en el texto propio: 0.*

## Ficha 39 — `lingob::S3::chapeau_seccion`

**Texto propio:**

```
Los integrantes de la Alta Gerencia deberán tener la idoneidad y experiencia necesarias en la acti-
vidad financiera para gestionar el negocio bajo su supervisión así como el control apropiado del per-
sonal de esas áreas.
```
**Último bloque heredado:** Sección 3. Alta Gerencia.

**SELLADO** — error: None

- Obligacion «Idoneidad y experiencia — Alta Gerencia»: Los integrantes de la Alta Gerencia deberán tener la idoneidad y experiencia necesarias en la actividad financiera
- Obligacion «Gestión del negocio — Alta Gerencia»: Los integrantes de la Alta Gerencia deberán gestionar el negocio bajo su supervisión
- Obligacion «Control apropiado del personal — Alta Gerencia»: Los integrantes de la Alta Gerencia deberán ejercer el control apropiado del personal de esas áreas
  - Obligacion:Idoneidad y experiencia — Alta Gerencia --establecida_en--> TextoOrdenado:Texto Ordenado de Línea de Gobierno
  - Obligacion:Gestión del negocio — Alta Gerencia --establecida_en--> TextoOrdenado:Texto Ordenado de Línea de Gobierno
  - Obligacion:Control apropiado del personal — Alta Gerencia --establecida_en--> TextoOrdenado:Texto Ordenado de Línea de Gobierno
  - Obligacion:Idoneidad y experiencia — Alta Gerencia --aplica_a--> integrantes de la Alta Gerencia
  - Obligacion:Gestión del negocio — Alta Gerencia --aplica_a--> integrantes de la Alta Gerencia
  - Obligacion:Control apropiado del personal — Alta Gerencia --aplica_a--> integrantes de la Alta Gerencia
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "integrantes de la Alta Gerencia", "verificada": "exacta", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "integrantes de la Alta Gerencia", "verificada": "exacta", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "integrantes de la Alta Gerencia", "verificada": "exacta", "sujeto_id": null}]; omisiones []; condicion_de []; limita []

**NUEVO** — error: None

- Obligacion «Idoneidad y experiencia — gestión del negocio»: Los integrantes de la Alta Gerencia tienen el deber de poseer la idoneidad y experiencia necesarias en la actividad financiera para gestionar el negocio bajo su supervisión. ‖ tramo (exacta): «Los integrantes de la Alta Gerencia deberán tener la idoneidad y experiencia necesarias en la actividad financiera para gestionar el negocio bajo su supervisión»
- Obligacion «Control apropiado del personal — supervisión»: Los integrantes de la Alta Gerencia deberán ejercer el control apropiado del personal de las áreas bajo su supervisión. ‖ tramo (exacta): «así como el control apropiado del personal de esas áreas»
  - Obligacion:Idoneidad y experiencia — gestión del negocio --establecida_en--> TextoOrdenado:Lingob
  - Obligacion:Control apropiado del personal — supervisión --establecida_en--> TextoOrdenado:Lingob
  - Obligacion:Idoneidad y experiencia — gestión del negocio --aplica_a--> Los integrantes de la Alta Gerencia
  - Obligacion:Control apropiado del personal — supervisión --aplica_a--> Los integrantes de la Alta Gerencia
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "Los integrantes de la Alta Gerencia", "verificada": "exacta", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "Los integrantes de la Alta Gerencia", "verificada": "exacta", "sujeto_id": null}]; omisiones []; condicion_de []; limita []

*Cuantías en el texto propio: 0.*

## Ficha 40 — `ric::7.2`

**Texto propio:**

```
7.2. Modelo de información
Cuadro 7.2.1.
[TABLA ric::tabla020 | página 36 | e0_tablas | columnas]
Columnas: Código | Concepto | col3
Fila 1: Código = 60100000 | Concepto = Disminución de la exigencia de capital mínimo por riesgo de crédito
Fila 2: Código = 60300000 | Concepto = Disminución de la exigencia de capital mínimo por riesgo de mercado
Fila 3: Código = 60400000 | Concepto = Disminución de la exigencia de capital mínimo por riesgo operacional
Fila 4: Código = 60500000 | Concepto = Aumento de la integración de capital mínimo por riesgo de crédito
Fila 5: Código = 60700000 | Concepto = Aumento de la integración de capital mínimo por riesgo de mercado.
Fila 6: Código = 60900000 | Concepto = Disminución del defecto de integración del capital mínimo por riesgo de crédito y operacional
Fila 7: Código = 61100000 | Concepto = Disminución del defecto de integración del capital mínimo por riesgo de mercado
[FIN TABLA ric::tabla020]
```
**Último bloque heredado:** Sección 7. Facilidades otorgadas por el B.C.R.A.

**SELLADO** — error: None

- hechos: umbrales []; menciones []; omisiones [{"categoria": null, "tramo": "", "verificacion": "ausente", "nota": "Cuadro 7.2.1 — códigos y conceptos (60100000 a 61100000): estructura tabular de modelo de informació…"}]; condicion_de []; limita []

**NUEVO** — error: None

  - rechazo: type_invalido: entities[0]: 'None'
- hechos: umbrales []; menciones []; omisiones [{"categoria": "fuera_de_tipos", "tramo": "", "verificacion": "ausente", "nota": "label: 'Régimen Informativo Contable Mensual'; tipo propuesto: None"}, {"categoria": "tabla", "tramo": "[TABLA ric::tabla020 | página 36 | e0_tablas | columnas] Columnas: Código | Concepto | col3 Fila 1: …", "verificacion": "exacta", "nota": "Tabla de códigos y conceptos de facilidades otorgadas por el BCRA: contenido clasificatorio/referenc…"}]; condicion_de []; limita []

*Cuantías en el texto propio: 0.*

## Ficha 41 — `ctacte::6.4.7::intro`

**Texto propio:**

```
a las presentes disposiciones, se observará el siguiente proceso:
```
**Último bloque heredado:** 6.4.7. Cuando sea necesario modificar las comunicaciones de rechazo efectuadas con sujeción

**SELLADO** — error: None

- Operacion «Modificación de comunicaciones de rechazo»: Modificar las comunicaciones de rechazo efectuadas con sujeción a las presentes disposiciones
  - Operacion:Modificación de comunicaciones de rechazo --establecida_en--> TextoOrdenado:Cuentas de corresponsalía
- hechos: umbrales []; menciones []; omisiones []; condicion_de []; limita []

**NUEVO** — error: None

- hechos: umbrales []; menciones []; omisiones [{"categoria": "meta_normativo", "tramo": "Cuando sea necesario modificar las comunicaciones de rechazo efectuadas con sujeción a las presentes…", "verificacion": "no", "nota": "Enunciado de condición o circunstancia que introduce el procedimiento: no prescribo conducta sino qu…"}]; condicion_de []; limita []

*Cuantías en el texto propio: 0.*

## Ficha 42 — `cap::8.4.1.6`

**Texto propio:**

```
8.4.1.6. Títulos valores e instrumentos de deuda no contemplados en los puntos
8.4.1.19. y 8.4.2., contractualmente subordinados a los demás pasivos, emitidos
por otras entidades financieras.
Esta deducción se efectuará por el importe del mayor saldo registrado durante
el mes al que corresponda la determinación de la RPC.
```
**Último bloque heredado:** COn1

**SELLADO** — error: None

- Operacion «Deducción títulos subordinados emitidos»: Deducción del capital ordinario de nivel uno de títulos valores e instrumentos de deuda contractualmente subordinados a los demás pasivos, emitidos por otras entidades financieras, por el importe del mayor saldo registrado durante el mes
- Restriccion «Títulos subordinados — solo de entidades financieras»: Los títulos valores e instrumentos de deuda deducibles deben ser emitidos por otras entidades financieras
- Restriccion «Subordinación contractual obligatoria»: Los títulos valores e instrumentos de deuda deben estar contractualmente subordinados a los demás pasivos
- Obligacion «Determinación deducción por mayor saldo mensual»: La deducción se efectuará por el importe del mayor saldo registrado durante el mes al que corresponda la determinación de la RPC
  - Operacion:Deducción títulos subordinados emitidos --establecida_en--> TextoOrdenado:Capitales mínimos
  - Restriccion:Títulos subordinados — solo de entidades financieras --establecida_en--> TextoOrdenado:Capitales mínimos
  - Restriccion:Subordinación contractual obligatoria --establecida_en--> TextoOrdenado:Capitales mínimos
  - Obligacion:Determinación deducción por mayor saldo mensual --establecida_en--> TextoOrdenado:Capitales mínimos
  - Restriccion:Títulos subordinados — solo de entidades financieras --limita--> Operacion:Deducción títulos subordinados emitidos
  - Restriccion:Subordinación contractual obligatoria --limita--> Operacion:Deducción títulos subordinados emitidos
  - Obligacion:Determinación deducción por mayor saldo mensual --regula--> Operacion:Deducción títulos subordinados emitidos
  - Operacion:Deducción títulos subordinados emitidos --aplica_a--> None
  - Restriccion:Títulos subordinados — solo de entidades financieras --aplica_a--> None
  - Restriccion:Subordinación contractual obligatoria --aplica_a--> None
  - Obligacion:Determinación deducción por mayor saldo mensual --aplica_a--> None
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}]; omisiones []; condicion_de []; limita [{"de": "Restriccion:Títulos subordinados — solo de entidades financieras", "a": "Operacion:Deducción títulos subordinados emitidos"}, {"de": "Restriccion:Subordinación contractual obligatoria", "a": "Operacion:Deducción títulos subordinados emitidos"}]

**NUEVO** — error: None

- Operacion «Emisión de títulos valores subordinados»: Títulos valores e instrumentos de deuda contractualmente subordinados a los demás pasivos, emitidos por otras entidades financieras, no contemplados en los puntos 8.4.1.19 y 8.4.2 ‖ tramo (exacta): «Títulos valores e instrumentos de deuda no contemplados en los puntos 8.4.1.19. y 8.4.2., contractualmente subordinados a los demás pasivos, emitidos por otras …»
- Obligacion «Deducción por mayor saldo mensual»: Efectuar la deducción del capital ordinario de nivel uno por el importe del mayor saldo registrado durante el mes al que corresponda la determinación de la RPC ‖ tramo (exacta): «Esta deducción se efectuará por el importe del mayor saldo registrado durante el mes al que corresponda la determinación de la RPC»
  - Operacion:Emisión de títulos valores subordinados --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Obligacion:Deducción por mayor saldo mensual --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Obligacion:Deducción por mayor saldo mensual --aplica_a--> las entidades
  - Obligacion:Deducción por mayor saldo mensual --regula--> Operacion:Emisión de títulos valores subordinados
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "las entidades", "verificada": "no", "sujeto_id": null}]; omisiones []; condicion_de []; limita []

*Cuantías en el texto propio: 0.*

## Ficha 43 — `expaef::6.5.3::intro`

**Texto propio:**

```
de sujeta a supervisión consolidada, a suministrar:
```
**Último bloque heredado:** 6.5.3. La entidad local deberá comprometerse, para el caso de que la entidad del exterior que-

**SELLADO** — error: None

- Obligacion «Suministro información supervisión consolidada»: La entidad local deberá comprometerse, para el caso de que la entidad del exterior esté sujeta a supervisión consolidada, a suministrar
  - Obligacion:Suministro información supervisión consolidada --establecida_en--> TextoOrdenado:Participación en entidades financieras exterior
  - Obligacion:Suministro información supervisión consolidada --aplica_a--> None
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}]; omisiones []; condicion_de []; limita []

**NUEVO** — error: None

- Obligacion «Suministro de información — supervisión consolidada»: La entidad local deberá comprometerse, cuando la entidad del exterior está sujeta a supervisión consolidada, a suministrar información ‖ tramo (exacta): «a suministrar»
- Condicion «Entidad del exterior sujeta a supervisión consolidada»: Condición de que la entidad del exterior esté sujeta a supervisión consolidada ‖ tramo (exacta): «para el caso de que la entidad del exterior que [...] de sujeta a supervisión consolidada»
  - Obligacion:Suministro de información — supervisión consolidada --establecida_en--> TextoOrdenado:Exterior - Participación en EF
  - Condicion:Entidad del exterior sujeta a supervisión consolidada --establecida_en--> TextoOrdenado:Exterior - Participación en EF
  - Condicion:Entidad del exterior sujeta a supervisión consolidada --condicion_de--> Obligacion:Suministro de información — supervisión consolidada
  - Obligacion:Suministro de información — supervisión consolidada --aplica_a--> La entidad local
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "La entidad local", "verificada": "exacta", "sujeto_id": null}]; omisiones [{"categoria": "fuera_de_tipos", "tramo": "suministrar", "verificacion": "exacta", "nota": "El contenido específico de lo que debe suministrarse no está completo en el bloque; el verbo no trae…"}]; condicion_de [{"de": "Condicion:Entidad del exterior sujeta a supervisión consolidada", "a": "Obligacion:Suministro de información — supervisión consolidada", "firma_nueva": false}]; limita []

*Cuantías en el texto propio: 0.*

## Ficha 44 — `ext::3.3.3.3`

**Texto propio:**

```
3.3.3.3. el cliente cuente con una “Certificación por los regímenes de acceso a
divisas para la producción incremental de petróleo y/o gas natural (Decreto
277/22)”, emitida en el marco de lo dispuesto en el punto 3.17., por el
equivalente al valor que se abona.
```
**Último bloque heredado:** La entidad deberá verificar el cumplimiento de la totalidad de los restantes requisitos normativos aplicables a la operación previamente a realizar el pedido al BCRA. Por hasta el monto de los intereses compensatorios sujetos a conformidad previa los clientes podrán suscribir Bonos para la Reconstru…

**SELLADO** — error: None

- Condicion «Cliente cuente con Certificación regímenes acceso divisas»: el cliente cuente con una "Certificación por los regímenes de acceso a divisas para la producción incremental de petróleo y/o gas natural (Decreto 277/22)", emitida en el marco de lo dispuesto en el punto 3.17., por el equivalente al valor …
- Operacion «Pago de intereses de deuda por importación»: pago de intereses de deudas comerciales por importaciones de bienes o servicios
  - Condicion:Cliente cuente con Certificación regímenes acceso divisas --establecida_en--> TextoOrdenado:Texto Ordenado de Exterior - Cambios
  - Condicion:Cliente cuente con Certificación regímenes acceso divisas --condicion_de--> Operacion:Pago de intereses de deuda por importación
- hechos: umbrales []; menciones []; omisiones []; condicion_de [{"de": "Condicion:Cliente cuente con Certificación regímenes acceso divisas", "a": "Operacion:Pago de intereses de deuda por importación", "firma_nueva": true}]; limita []

**NUEVO** — error: None

- Condicion «Certificación regímenes acceso divisas petróleo/gas»: El cliente debe contar con una Certificación por los regímenes de acceso a divisas para la producción incremental de petróleo y/o gas natural (Decreto 277/22), emitida conforme al punto 3.17., por el equivalente al valor que se abona ‖ tramo (exacta): «el cliente cuente con una "Certificación por los regímenes de acceso a divisas para la producción incremental de petróleo y/o gas natural (Decreto 277/22)", emi…»
- Operacion «Emisión certificación acceso divisas petróleo/gas»: Emisión de una Certificación por los regímenes de acceso a divisas para la producción incremental de petróleo y/o gas natural (Decreto 277/22), emitida en el marco del punto 3.17., por el equivalente al valor que se abona en la operación de… ‖ tramo (exacta): «Certificación por los regímenes de acceso a divisas para la producción incremental de petróleo y/o gas natural (Decreto 277/22)»
  - Condicion:Certificación regímenes acceso divisas petróleo/gas --establecida_en--> TextoOrdenado:Texto Ordenado Exterior y Cambios
  - Operacion:Emisión certificación acceso divisas petróleo/gas --establecida_en--> TextoOrdenado:Texto Ordenado Exterior y Cambios
  - Condicion:Certificación regímenes acceso divisas petróleo/gas --condicion_de--> Operacion:Emisión certificación acceso divisas petróleo/gas
- hechos: umbrales []; menciones []; omisiones [{"categoria": "relacion_sin_predicado", "tramo": "Certificación por los regímenes de acceso a divisas para la producción incremental de petróleo y/o g…", "verificacion": "exacta", "nota": "remisión_normativa"}]; condicion_de [{"de": "Condicion:Certificación regímenes acceso divisas petróleo/gas", "a": "Operacion:Emisión certificación acceso divisas petróleo/gas", "firma_nueva": true}]; limita []

*Cuantías en el texto propio: 0.*

## Ficha 45 — `ext::13.4.8`

**Texto propio:**

```
13.4.8. el pago es concretado a partir del 10/02/24 por una persona humana o una persona
jurídica que clasifique como MiPyMe según lo dispuesto en las normas de
“Determinación de la condición de micro, pequeña y mediana empresa” y se cumple
la totalidad de las siguientes condiciones:
i) El monto total de sus deudas por importaciones de bienes y servicios previas al
13/12/23 pendiente de pago sea menor o igual al equivalente a USD 500.000
(dólares estadounidenses quinientos mil).
ii) El cliente haya registrado la totalidad de sus deudas por importaciones de
bienes y servicios en el “Padrón de Deuda Comercial por Importaciones con
Proveedores del Exterior” establecido por Resolución General Conjunta
5466/23 de la Administración Federal de Ingresos Públicos y la Secretaría de
Comercio y concordantes.
iii) Los pagos por deudas de bienes o servicios realizados en el marco de los
mecanismos previstos en este punto y/o en el punto 10.11.7., en el conjunto de
las entidades y por el conjunto de los conceptos, no superen el equivalente al
monto declarado en el referido padrón.
iv) La operación se encuentra declarada, en caso de corresponder, en la última
presentación vencida del “Relevamiento de activos y pasivos externos”.
v) La entidad cuente con una declaración jurada del cliente en la que conste que:
a) la totalidad de sus deudas por importaciones de bienes y servicios previas
al 13/12/23 han sido declaradas en el “Padrón de Deuda Comercial por
Importaciones con Proveedores del Exterior” y el monto total adeudado a la
fecha de cierre del mencionado registro no supera el equivalente a USD
500.000 (dólares estadounidenses quinientos mil).
b) los montos abonados por este mecanismo en el conjunto de las entidades
y por el conjunto de los conceptos no superan los límites previstos en el
punto iii) precedente.
```
**Último bloque heredado:** Se requerirá la conformidad previa del BCRA para el acceso al mercado de cambios para realizar pagos de servicios de no residentes prestados o devengados hasta el 12/12/23, excepto cuando, adicionalmente a los restantes requisitos aplicables, la entidad verifique que:

**SELLADO** — error: None

- Condicion «Pago a partir del 10/02/24 por persona humana o MiPyMe»: el pago es concretado a partir del 10/02/24 por una persona humana o una persona jurídica que clasifique como MiPyMe según lo dispuesto en las normas de 'Determinación de la condición de micro, pequeña y mediana empresa'
- Condicion «Monto total deuda importaciones menor o igual USD 500.000»: El monto total de sus deudas por importaciones de bienes y servicios previas al 13/12/23 pendiente de pago sea menor o igual al equivalente a USD 500.000 (dólares estadounidenses quinientos mil)
- Condicion «Registro en Padrón de Deuda Comercial por Importaciones»: El cliente haya registrado la totalidad de sus deudas por importaciones de bienes y servicios en el 'Padrón de Deuda Comercial por Importaciones con Proveedores del Exterior' establecido por Resolución General Conjunta 5466/23 de la Adminis…
- Condicion «Pagos no superan monto declarado en padrón»: Los pagos por deudas de bienes o servicios realizados en el marco de los mecanismos previstos en este punto y/o en el punto 10.11.7., en el conjunto de las entidades y por el conjunto de los conceptos, no superen el equivalente al monto dec…
- Condicion «Operación declarada en Relevamiento de activos y pasivos externos»: La operación se encuentra declarada, en caso de corresponder, en la última presentación vencida del 'Relevamiento de activos y pasivos externos'
- Condicion «Declaración jurada del cliente sobre deudas y límites»: La entidad cuente con una declaración jurada del cliente en la que conste que la totalidad de sus deudas por importaciones de bienes y servicios previas al 13/12/23 han sido declaradas en el 'Padrón de Deuda Comercial por Importaciones con …
- Operacion «Pago de servicios de no residentes»: Pago de servicios prestados o devengados por no residentes hasta el 12/12/23, concretado por persona humana o MiPyMe que cumple condiciones específicas de deuda y registro
- Obligacion «Acceso al mercado de cambios con conformidad previa del BCRA»: Se requerirá la conformidad previa del BCRA para el acceso al mercado de cambios para realizar pagos de servicios de no residentes prestados o devengados hasta el 12/12/23, excepto cuando se verifiquen las condiciones del presente punto
  - Condicion:Pago a partir del 10/02/24 por persona humana o MiPyMe --establecida_en--> TextoOrdenado:Exterior - Cambios
  - Condicion:Monto total deuda importaciones menor o igual USD 500.000 --establecida_en--> TextoOrdenado:Exterior - Cambios
  - Condicion:Registro en Padrón de Deuda Comercial por Importaciones --establecida_en--> TextoOrdenado:Exterior - Cambios
  - Condicion:Pagos no superan monto declarado en padrón --establecida_en--> TextoOrdenado:Exterior - Cambios
  - Condicion:Operación declarada en Relevamiento de activos y pasivos ext… --establecida_en--> TextoOrdenado:Exterior - Cambios
  - Condicion:Declaración jurada del cliente sobre deudas y límites --establecida_en--> TextoOrdenado:Exterior - Cambios
  - Operacion:Pago de servicios de no residentes --establecida_en--> TextoOrdenado:Exterior - Cambios
  - Obligacion:Acceso al mercado de cambios con conformidad previa del BCRA --establecida_en--> TextoOrdenado:Exterior - Cambios
  - Condicion:Pago a partir del 10/02/24 por persona humana o MiPyMe --condicion_de--> Obligacion:Acceso al mercado de cambios con conformidad previa del BCRA
  - Condicion:Monto total deuda importaciones menor o igual USD 500.000 --condicion_de--> Obligacion:Acceso al mercado de cambios con conformidad previa del BCRA
  - Condicion:Registro en Padrón de Deuda Comercial por Importaciones --condicion_de--> Obligacion:Acceso al mercado de cambios con conformidad previa del BCRA
  - Condicion:Pagos no superan monto declarado en padrón --condicion_de--> Obligacion:Acceso al mercado de cambios con conformidad previa del BCRA
  - Condicion:Operación declarada en Relevamiento de activos y pasivos ext… --condicion_de--> Obligacion:Acceso al mercado de cambios con conformidad previa del BCRA
  - Condicion:Declaración jurada del cliente sobre deudas y límites --condicion_de--> Obligacion:Acceso al mercado de cambios con conformidad previa del BCRA
  - Obligacion:Acceso al mercado de cambios con conformidad previa del BCRA --regula--> Operacion:Pago de servicios de no residentes
  - Obligacion:Acceso al mercado de cambios con conformidad previa del BCRA --aplica_a--> None
  - [sujeto] --ejecuta--> Operacion:Pago de servicios de no residentes
  - [sujeto] --ejecuta--> Operacion:Pago de servicios de no residentes
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "ejecuta", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "ejecuta", "mencion": "", "verificada": "ausente", "sujeto_id": null}]; omisiones []; condicion_de [{"de": "Condicion:Pago a partir del 10/02/24 por persona humana o MiPyMe", "a": "Obligacion:Acceso al mercado de cambios con conformidad previa del BCRA", "firma_nueva": false}, {"de": "Condicion:Monto total deuda importaciones menor o igual USD 500.000", "a": "Obligacion:Acceso al mercado de cambios con conformidad previa del BCRA", "firma_nueva": false}, {"de": "Condicion:Registro en Padrón de Deuda Comercial por Importaciones", "a": "Obligacion:Acceso al mercado de cambios con conformidad previa del BCRA", "firma_nueva": false}, {"de": "Condicion:Pagos no superan monto declarado en padrón", "a": "Obligacion:Acceso al mercado de cambios con conformidad previa del BCRA", "firma_nueva": false}, {"de": "Condicion:Operación declarada en Relevamiento de activos y pasivos ext…", "a": "Obligacion:Acceso al mercado de cambios con conformidad previa del BCRA", "firma_nueva": false}, {"de": "Condicion:Declaración jurada del cliente sobre deudas y límites", "a": "Obligacion:Acceso al mercado de cambios con conformidad previa del BCRA", "firma_nueva": false}]; limita []

**NUEVO** — error: None

- Operacion «Pago de servicios — desde 10/02/24»: Pago de servicios de no residentes prestados o devengados hasta el 12/12/23, concretado a partir del 10/02/24 por una persona humana o persona jurídica clasificada como MiPyMe. ‖ tramo (exacta): «el pago es concretado a partir del 10/02/24 por una persona humana o una persona jurídica que clasifique como MiPyMe»
- Condicion «Monto deuda importaciones ≤ USD 500.000»: El monto total de deudas por importaciones de bienes y servicios anteriores a 13/12/23 pendiente de pago no exceda USD 500.000. ‖ tramo (exacta): «El monto total de sus deudas por importaciones de bienes y servicios previas al 13/12/23 pendiente de pago sea menor o igual al equivalente a USD 500.000»
- Condicion «Registro en Padrón de Deuda Comercial»: El cliente ha registrado la totalidad de sus deudas por importaciones de bienes y servicios en el Padrón de Deuda Comercial por Importaciones con Proveedores del Exterior conforme a la Resolución General Conjunta 5466/23 de la AFIP y Secret… ‖ tramo (exacta): «El cliente haya registrado la totalidad de sus deudas por importaciones de bienes y servicios en el "Padrón de Deuda Comercial por Importaciones con Proveedores…»
- Condicion «Pagos no superen monto declarado en padrón»: Los pagos por deudas de bienes o servicios realizados en el marco de estos mecanismos, considerando el conjunto de entidades y conceptos, no superan el monto declarado en el Padrón. ‖ tramo (exacta): «Los pagos por deudas de bienes o servicios realizados en el marco de los mecanismos previstos en este punto y/o en el punto 10.11.7., en el conjunto de las enti…»
- Condicion «Operación declarada en Relevamiento de activos»: La operación está declarada, cuando corresponda, en la última presentación vencida del Relevamiento de activos y pasivos externos. ‖ tramo (exacta): «La operación se encuentra declarada, en caso de corresponder, en la última presentación vencida del "Relevamiento de activos y pasivos externos"»
- Obligacion «Contar con declaración jurada del cliente»: La entidad debe contar con una declaración jurada del cliente que certifique: (a) que la totalidad de sus deudas por importaciones de bienes y servicios previas al 13/12/23 han sido declaradas en el Padrón de Deuda Comercial y el monto tota… ‖ tramo (exacta): «La entidad cuente con una declaración jurada del cliente en la que conste que: a) la totalidad de sus deudas por importaciones de bienes y servicios previas al …»
- Comunicacion «Res. Gen. Conj. 5466/23»:  ‖ tramo (exacta): «Resolución General Conjunta 5466/23 de la Administración Federal de Ingresos Públicos y la Secretaría de Comercio»
  - Operacion:Pago de servicios — desde 10/02/24 --establecida_en--> TextoOrdenado:Exterior - Cambios
  - Condicion:Monto deuda importaciones ≤ USD 500.000 --establecida_en--> TextoOrdenado:Exterior - Cambios
  - Condicion:Registro en Padrón de Deuda Comercial --establecida_en--> TextoOrdenado:Exterior - Cambios
  - Condicion:Pagos no superen monto declarado en padrón --establecida_en--> TextoOrdenado:Exterior - Cambios
  - Condicion:Operación declarada en Relevamiento de activos --establecida_en--> TextoOrdenado:Exterior - Cambios
  - Obligacion:Contar con declaración jurada del cliente --establecida_en--> TextoOrdenado:Exterior - Cambios
  - Condicion:Monto deuda importaciones ≤ USD 500.000 --condicion_de--> Operacion:Pago de servicios — desde 10/02/24
  - Condicion:Registro en Padrón de Deuda Comercial --condicion_de--> Operacion:Pago de servicios — desde 10/02/24
  - Condicion:Pagos no superen monto declarado en padrón --condicion_de--> Operacion:Pago de servicios — desde 10/02/24
  - Condicion:Operación declarada en Relevamiento de activos --condicion_de--> Operacion:Pago de servicios — desde 10/02/24
  - Operacion:Pago de servicios — desde 10/02/24 --aplica_a--> entidad cuente con una
  - Obligacion:Contar con declaración jurada del cliente --aplica_a--> La entidad
  - TextoOrdenado:Exterior - Cambios --referencia--> Comunicacion:Res. Gen. Conj. 5466/23
  - rechazo: firma_invalida: relations[10]: Obligacion --condicion_de--> Operacion
- hechos: umbrales [{"entidad": "Condicion:Monto deuda importaciones ≤ USD 500.000", "tramo": "menor o igual al equivalente a USD 500.000", "verificacion": "exacta"}, {"entidad": "Obligacion:Contar con declaración jurada del cliente", "tramo": "no supera el equivalente a USD 500.000", "verificacion": "exacta"}]; menciones [{"pred": "aplica_a", "mencion": "entidad cuente con una", "verificada": "tokens", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "La entidad", "verificada": "exacta", "sujeto_id": null}]; omisiones [{"categoria": "meta_normativo", "tramo": "se requerirá la conformidad previa del BCRA para el acceso al mercado de cambios para realizar pagos", "verificacion": "no", "nota": "Enunciado de alcance o aplicabilidad general de la sección; no prescribe conducta regulada de manera…"}, {"categoria": "relacion_sin_predicado", "tramo": "la totalidad de las siguientes condiciones", "verificacion": "exacta", "nota": "Enumeración que marca que las condiciones e2-e6 se exigen concurrentemente; la relación de 'totalida…"}]; condicion_de [{"de": "Condicion:Monto deuda importaciones ≤ USD 500.000", "a": "Operacion:Pago de servicios — desde 10/02/24", "firma_nueva": true}, {"de": "Condicion:Registro en Padrón de Deuda Comercial", "a": "Operacion:Pago de servicios — desde 10/02/24", "firma_nueva": true}, {"de": "Condicion:Pagos no superen monto declarado en padrón", "a": "Operacion:Pago de servicios — desde 10/02/24", "firma_nueva": true}, {"de": "Condicion:Operación declarada en Relevamiento de activos", "a": "Operacion:Pago de servicios — desde 10/02/24", "firma_nueva": true}]; limita []

*Cuantías en el texto propio: 2.*

## Ficha 46 — `ayccef::3.4.1`

**Texto propio:**

```
3.4.1. Fundamentos en que se basa la iniciativa.
```
**Último bloque heredado:** La solicitud de autorización deberá ser interpuesta por las entidades que se fusionan para constituir una nueva entidad o la entidad absorbente con las siguientes informaciones y do- cumentación:

**SELLADO** — error: None

- hechos: umbrales []; menciones []; omisiones []; condicion_de []; limita []

**NUEVO** — error: None

- Obligacion «Presentar fundamentos de la iniciativa»: Las entidades que se fusionan o la entidad absorbente deberán presentar los fundamentos en que se basa la iniciativa de fusión como parte de la solicitud de autorización. ‖ tramo (exacta): «La solicitud de autorización deberá ser interpuesta por las entidades que se fusionan para constituir una nueva entidad o la entidad absorbente con las siguient…»
  - Obligacion:Presentar fundamentos de la iniciativa --establecida_en--> TextoOrdenado:Fusión de entidades financieras
  - Obligacion:Presentar fundamentos de la iniciativa --aplica_a--> las entidades que se fusionan para constituir una nueva entidad o la entidad absorbente
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "las entidades que se fusionan para constituir una nueva entidad o la entidad abs…", "verificada": "exacta", "sujeto_id": null}]; omisiones []; condicion_de []; limita []

*Cuantías en el texto propio: 0.*

## Ficha 47 — `ctacte::8.8.2::intro`

**Texto propio:**

```
A fin de ser excluidas de la “Central de cheques rechazados” y/o de la “Central de cuen-
tacorrentistas inhabilitados”, las personas que hayan sido incorporadas a ellas como
consecuencia de ese motivo deberán efectuar una presentación ante el banco que haya
informado los rechazos en la que expongan sucintamente los hechos acontecidos, junto
con los siguientes elementos:
```
**Último bloque heredado:** 8.8.2. Apertura de cuentas con documentación apócrifa.

**SELLADO** — error: None

- Obligacion «Presentación ante banco — exclusión de centrales»: las personas que hayan sido incorporadas a la Central de cheques rechazados y/o de la Central de cuentacorrentistas inhabilitados deberán efectuar una presentación ante el banco que haya informado los rechazos en la que expongan sucintament…
- Operacion «Incorporación en centrales de cheques rechazados e inhabilitados»: Incorporación de personas a la Central de cheques rechazados y/o a la Central de cuentacorrentistas inhabilitados como consecuencia de motivo de documentación apócrifa
- Condicion «Personas incorporadas a centrales por documentación apócrifa»: personas que hayan sido incorporadas a la Central de cheques rechazados y/o de la Central de cuentacorrentistas inhabilitados como consecuencia de ese motivo [documentación apócrifa]
- Excepcion «Exclusión de centrales — presentación y cumplimiento»: A fin de ser excluidas de la Central de cheques rechazados y/o de la Central de cuentacorrentistas inhabilitados, las personas deberán efectuar presentación con exposición de hechos
  - Obligacion:Presentación ante banco — exclusión de centrales --establecida_en--> TextoOrdenado:Cuentas Corrientes
  - Operacion:Incorporación en centrales de cheques rechazados e inhabilit… --establecida_en--> TextoOrdenado:Cuentas Corrientes
  - Condicion:Personas incorporadas a centrales por documentación apócrifa --establecida_en--> TextoOrdenado:Cuentas Corrientes
  - Excepcion:Exclusión de centrales — presentación y cumplimiento --establecida_en--> TextoOrdenado:Cuentas Corrientes
  - Obligacion:Presentación ante banco — exclusión de centrales --aplica_a--> personas que hayan sido incorporadas a las centrales
  - Condicion:Personas incorporadas a centrales por documentación apócrifa --condicion_de--> Excepcion:Exclusión de centrales — presentación y cumplimiento
  - Obligacion:Presentación ante banco — exclusión de centrales --condiciona--> Operacion:Incorporación en centrales de cheques rechazados e inhabilit…
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "personas que hayan sido incorporadas a las centrales", "verificada": "no", "sujeto_id": null}]; omisiones []; condicion_de [{"de": "Condicion:Personas incorporadas a centrales por documentación apócrifa", "a": "Excepcion:Exclusión de centrales — presentación y cumplimiento", "firma_nueva": false}]; limita []

**NUEVO** — error: None

- Obligacion «Presentación ante banco — exclusión de centrales»: Las personas incorporadas a la Central de cheques rechazados y/o a la Central de cuentacorrentistas inhabilitados como consecuencia de esa causa deberán hacer una presentación ante el banco que haya informado los rechazos, exponiendo sucint… ‖ tramo (exacta): «las personas que hayan sido incorporadas a ellas como consecuencia de ese motivo deberán efectuar una presentación ante el banco que haya informado los rechazos»
- Obligacion «Exposición de hechos y elementos en presentación»: En la presentación, las personas deberán exponer sucintamente los hechos acontecidos junto con los elementos que la norma especifica. ‖ tramo (exacta): «expongan sucintamente los hechos acontecidos, junto con los siguientes elementos»
- Condicion «Supuesto de incorporación a centrales por documentación apócrifa»: La obligación de hacer presentación se activa cuando las personas hayan sido incorporadas a la Central de cheques rechazados y/o a la Central de cuentacorrentistas inhabilitados como consecuencia de la apertura de cuentas con documentación … ‖ tramo (exacta): «que hayan sido incorporadas a ellas como consecuencia de ese motivo»
  - Obligacion:Presentación ante banco — exclusión de centrales --establecida_en--> TextoOrdenado:Cuentas corrientes
  - Obligacion:Exposición de hechos y elementos en presentación --establecida_en--> TextoOrdenado:Cuentas corrientes
  - Condicion:Supuesto de incorporación a centrales por documentación apóc… --establecida_en--> TextoOrdenado:Cuentas corrientes
  - Obligacion:Presentación ante banco — exclusión de centrales --aplica_a--> las personas que hayan sido incorporadas a ellas
  - Obligacion:Exposición de hechos y elementos en presentación --aplica_a--> las personas
  - Condicion:Supuesto de incorporación a centrales por documentación apóc… --condicion_de--> Obligacion:Presentación ante banco — exclusión de centrales
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "las personas que hayan sido incorporadas a ellas", "verificada": "exacta", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "las personas", "verificada": "exacta", "sujeto_id": null}]; omisiones [{"categoria": "fuera_de_tipos", "tramo": "A fin de ser excluidas de la \"Central de cheques rechazados\" y/o de la \"Central de cuentacorrentista…", "verificacion": "exacta", "nota": "Finalidad o propósito: la frase enuncia el objetivo que motiva la conducta obligada, que la norma no…"}]; condicion_de [{"de": "Condicion:Supuesto de incorporación a centrales por documentación apóc…", "a": "Obligacion:Presentación ante banco — exclusión de centrales", "firma_nueva": false}]; limita []

*Cuantías en el texto propio: 0.*

## Ficha 48 — `cla::6.5.4.8`

**Texto propio:**

```
6.5.4.8. Se encuentre permanentemente atrasado en el pago, con incumplimientos supe-
riores a 180 días respecto de las condiciones contractuales.
```
**Último bloque heredado:** El análisis del flujo de fondos del cliente demuestra que es altamente improbable que pueda atender la totalidad de sus compromisos financieros. Entre los indicadores que pueden reflejar esta situación se destacan que el cliente:

**SELLADO** — error: None

- Condicion «Permanentemente atrasado >180 días»: Se encuentre permanentemente atrasado en el pago, con incumplimientos superiores a 180 días respecto de las condiciones contractuales.
  - Condicion:Permanentemente atrasado >180 días --establecida_en--> TextoOrdenado:Clasificación de deudores
- hechos: umbrales []; menciones []; omisiones []; condicion_de []; limita []

**NUEVO** — error: None

- Condicion «Atraso permanente superior a 180 días»: El cliente se encuentra permanentemente atrasado en el pago, con incumplimientos que superan los 180 días respecto de las condiciones contractuales ‖ tramo (exacta): «Se encuentre permanentemente atrasado en el pago, con incumplimientos superiores a 180 días respecto de las condiciones contractuales»
- Operacion «Clasificación con alto riesgo de insolvencia»: Clasificación del deudor en la categoría de alto riesgo de insolvencia, cuando el análisis del flujo de fondos demuestra que es altamente improbable que el cliente pueda atender la totalidad de sus compromisos financieros ‖ tramo (no): «se incluirá en una de las siguientes cinco categorías […] Con alto riesgo de insolvencia»
  - Condicion:Atraso permanente superior a 180 días --establecida_en--> TextoOrdenado:Clasificación de Deudores
  - Condicion:Atraso permanente superior a 180 días --condicion_de--> Operacion:Clasificación con alto riesgo de insolvencia
- hechos: umbrales [{"entidad": "Condicion:Atraso permanente superior a 180 días", "tramo": "superiores a 180 días", "verificacion": "exacta"}]; menciones []; omisiones []; condicion_de [{"de": "Condicion:Atraso permanente superior a 180 días", "a": "Operacion:Clasificación con alto riesgo de insolvencia", "firma_nueva": true}]; limita []

*Cuantías en el texto propio: 1.*

## Ficha 49 — `cap::2.12.3.2`

**Texto propio:**

```
2.12.3.2. Demás.
[TABLA cap::tabla2f004 | página 24 | R-TC2 | columnas]
Columnas: Calificación | AAA hasta AA- | A+ hasta A- | BBB+ hasta BBB- | BB+ hasta B- | Inferior a B- | No calificado
Fila 1: Calificación = Ponderador de riesgo | AAA hasta AA- = 20% | A+ hasta A- = 30% | BBB+ hasta BBB- = 50% | BB+ hasta B- = 100% | Inferior a B- = 150% | No calificado = 50%
[FIN TABLA cap::tabla2f004]
```
**Último bloque heredado:** 2.12.3. Exposiciones a bancos multilaterales de desarrollo (BMD).

**SELLADO** — error: None

- Restriccion «Ponderador riesgo BMD — AAA a AA-»: Para exposiciones a bancos multilaterales de desarrollo (BMD) con calificación de AAA hasta AA-, ponderador de riesgo del 20%
- Restriccion «Ponderador riesgo BMD — A+ a A-»: Para exposiciones a bancos multilaterales de desarrollo (BMD) con calificación de A+ hasta A-, ponderador de riesgo del 30%
- Restriccion «Ponderador riesgo BMD — BBB+ a BBB-»: Para exposiciones a bancos multilaterales de desarrollo (BMD) con calificación de BBB+ hasta BBB-, ponderador de riesgo del 50%
- Restriccion «Ponderador riesgo BMD — BB+ a B-»: Para exposiciones a bancos multilaterales de desarrollo (BMD) con calificación de BB+ hasta B-, ponderador de riesgo del 100%
- Restriccion «Ponderador riesgo BMD — inferior a B-»: Para exposiciones a bancos multilaterales de desarrollo (BMD) con calificación inferior a B-, ponderador de riesgo del 150%
- Restriccion «Ponderador riesgo BMD — no calificado»: Para exposiciones a bancos multilaterales de desarrollo (BMD) no calificados, ponderador de riesgo del 50%
- Operacion «Exposiciones a bancos multilaterales de desarrollo»: Exposiciones de las entidades a bancos multilaterales de desarrollo (BMD)
  - Restriccion:Ponderador riesgo BMD — AAA a AA- --establecida_en--> TextoOrdenado:Capitales mínimos
  - Restriccion:Ponderador riesgo BMD — A+ a A- --establecida_en--> TextoOrdenado:Capitales mínimos
  - Restriccion:Ponderador riesgo BMD — BBB+ a BBB- --establecida_en--> TextoOrdenado:Capitales mínimos
  - Restriccion:Ponderador riesgo BMD — BB+ a B- --establecida_en--> TextoOrdenado:Capitales mínimos
  - Restriccion:Ponderador riesgo BMD — inferior a B- --establecida_en--> TextoOrdenado:Capitales mínimos
  - Restriccion:Ponderador riesgo BMD — no calificado --establecida_en--> TextoOrdenado:Capitales mínimos
  - Operacion:Exposiciones a bancos multilaterales de desarrollo --establecida_en--> TextoOrdenado:Capitales mínimos
  - Restriccion:Ponderador riesgo BMD — AAA a AA- --limita--> Operacion:Exposiciones a bancos multilaterales de desarrollo
  - Restriccion:Ponderador riesgo BMD — A+ a A- --limita--> Operacion:Exposiciones a bancos multilaterales de desarrollo
  - Restriccion:Ponderador riesgo BMD — BBB+ a BBB- --limita--> Operacion:Exposiciones a bancos multilaterales de desarrollo
  - Restriccion:Ponderador riesgo BMD — BB+ a B- --limita--> Operacion:Exposiciones a bancos multilaterales de desarrollo
  - Restriccion:Ponderador riesgo BMD — inferior a B- --limita--> Operacion:Exposiciones a bancos multilaterales de desarrollo
  - Restriccion:Ponderador riesgo BMD — no calificado --limita--> Operacion:Exposiciones a bancos multilaterales de desarrollo
  - Restriccion:Ponderador riesgo BMD — AAA a AA- --aplica_a--> None
  - Restriccion:Ponderador riesgo BMD — A+ a A- --aplica_a--> None
  - Restriccion:Ponderador riesgo BMD — BBB+ a BBB- --aplica_a--> None
  - Restriccion:Ponderador riesgo BMD — BB+ a B- --aplica_a--> None
  - Restriccion:Ponderador riesgo BMD — inferior a B- --aplica_a--> None
  - Restriccion:Ponderador riesgo BMD — no calificado --aplica_a--> None
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}]; omisiones [{"categoria": null, "tramo": "", "verificacion": "ausente", "nota": "Estructura tabular de ponderadores por categoría de calificación crediticia: tabla de dos columnas (…"}]; condicion_de []; limita [{"de": "Restriccion:Ponderador riesgo BMD — AAA a AA-", "a": "Operacion:Exposiciones a bancos multilaterales de desarrollo"}, {"de": "Restriccion:Ponderador riesgo BMD — A+ a A-", "a": "Operacion:Exposiciones a bancos multilaterales de desarrollo"}, {"de": "Restriccion:Ponderador riesgo BMD — BBB+ a BBB-", "a": "Operacion:Exposiciones a bancos multilaterales de desarrollo"}, {"de": "Restriccion:Ponderador riesgo BMD — BB+ a B-", "a": "Operacion:Exposiciones a bancos multilaterales de desarrollo"}, {"de": "Restriccion:Ponderador riesgo BMD — inferior a B-", "a": "Operacion:Exposiciones a bancos multilaterales de desarrollo"}, {"de": "Restriccion:Ponderador riesgo BMD — no calificado", "a": "Operacion:Exposiciones a bancos multilaterales de desarrollo"}]

**NUEVO** — error: None

- Operacion «Exposición a BMD calificadas AAA-AA-»: Exposición a bancos multilaterales de desarrollo con calificación de AAA hasta AA-, ponderada al 20% ‖ tramo (exacta): «Exposiciones a bancos multilaterales de desarrollo (BMD)»
- Operacion «Exposición a BMD calificadas A+-A-»: Exposición a bancos multilaterales de desarrollo con calificación de A+ hasta A-, ponderada al 30% ‖ tramo (exacta): «Exposiciones a bancos multilaterales de desarrollo (BMD)»
- Operacion «Exposición a BMD calificadas BBB+-BBB-»: Exposición a bancos multilaterales de desarrollo con calificación de BBB+ hasta BBB-, ponderada al 50% ‖ tramo (exacta): «Exposiciones a bancos multilaterales de desarrollo (BMD)»
- Operacion «Exposición a BMD calificadas BB+-B-»: Exposición a bancos multilaterales de desarrollo con calificación de BB+ hasta B-, ponderada al 100% ‖ tramo (exacta): «Exposiciones a bancos multilaterales de desarrollo (BMD)»
- Operacion «Exposición a BMD calificadas Inferior a B-»: Exposición a bancos multilaterales de desarrollo con calificación inferior a B-, ponderada al 150% ‖ tramo (exacta): «Exposiciones a bancos multilaterales de desarrollo (BMD)»
- Operacion «Exposición a BMD no calificadas»: Exposición a bancos multilaterales de desarrollo no calificadas, ponderada al 50% ‖ tramo (exacta): «Exposiciones a bancos multilaterales de desarrollo (BMD)»
- Restriccion «Ponderador 20% exposición BMD AAA-AA-»: Las exposiciones a bancos multilaterales de desarrollo con calificación de AAA hasta AA- se ponderan al 20% ‖ tramo (exacta): «AAA hasta AA- = 20%»
- Restriccion «Ponderador 30% exposición BMD A+-A-»: Las exposiciones a bancos multilaterales de desarrollo con calificación de A+ hasta A- se ponderan al 30% ‖ tramo (exacta): «A+ hasta A- = 30%»
- Restriccion «Ponderador 50% exposición BMD BBB+-BBB-»: Las exposiciones a bancos multilaterales de desarrollo con calificación de BBB+ hasta BBB- se ponderan al 50% ‖ tramo (exacta): «BBB+ hasta BBB- = 50%»
- Restriccion «Ponderador 100% exposición BMD BB+-B-»: Las exposiciones a bancos multilaterales de desarrollo con calificación de BB+ hasta B- se ponderan al 100% ‖ tramo (exacta): «BB+ hasta B- = 100%»
- Restriccion «Ponderador 150% exposición BMD Inferior a B-»: Las exposiciones a bancos multilaterales de desarrollo con calificación inferior a B- se ponderan al 150% ‖ tramo (exacta): «Inferior a B- = 150%»
- Restriccion «Ponderador 50% exposición BMD no calificadas»: Las exposiciones a bancos multilaterales de desarrollo no calificadas se ponderan al 50% ‖ tramo (exacta): «No calificado = 50%»
  - Restriccion:Ponderador 20% exposición BMD AAA-AA- --establecida_en--> TextoOrdenado:Texto Ordenado de Capitales Mínimos
  - Restriccion:Ponderador 30% exposición BMD A+-A- --establecida_en--> TextoOrdenado:Texto Ordenado de Capitales Mínimos
  - Restriccion:Ponderador 50% exposición BMD BBB+-BBB- --establecida_en--> TextoOrdenado:Texto Ordenado de Capitales Mínimos
  - Restriccion:Ponderador 100% exposición BMD BB+-B- --establecida_en--> TextoOrdenado:Texto Ordenado de Capitales Mínimos
  - Restriccion:Ponderador 150% exposición BMD Inferior a B- --establecida_en--> TextoOrdenado:Texto Ordenado de Capitales Mínimos
  - Restriccion:Ponderador 50% exposición BMD no calificadas --establecida_en--> TextoOrdenado:Texto Ordenado de Capitales Mínimos
  - Restriccion:Ponderador 20% exposición BMD AAA-AA- --limita--> Operacion:Exposición a BMD calificadas AAA-AA-
  - Restriccion:Ponderador 30% exposición BMD A+-A- --limita--> Operacion:Exposición a BMD calificadas A+-A-
  - Restriccion:Ponderador 50% exposición BMD BBB+-BBB- --limita--> Operacion:Exposición a BMD calificadas BBB+-BBB-
  - Restriccion:Ponderador 100% exposición BMD BB+-B- --limita--> Operacion:Exposición a BMD calificadas BB+-B-
  - Restriccion:Ponderador 150% exposición BMD Inferior a B- --limita--> Operacion:Exposición a BMD calificadas Inferior a B-
  - Restriccion:Ponderador 50% exposición BMD no calificadas --limita--> Operacion:Exposición a BMD no calificadas
  - Restriccion:Ponderador 20% exposición BMD AAA-AA- --aplica_a--> las entidades
  - Restriccion:Ponderador 30% exposición BMD A+-A- --aplica_a--> las entidades
  - Restriccion:Ponderador 50% exposición BMD BBB+-BBB- --aplica_a--> las entidades
  - Restriccion:Ponderador 100% exposición BMD BB+-B- --aplica_a--> las entidades
  - Restriccion:Ponderador 150% exposición BMD Inferior a B- --aplica_a--> las entidades
  - Restriccion:Ponderador 50% exposición BMD no calificadas --aplica_a--> las entidades
- hechos: umbrales [{"entidad": "Restriccion:Ponderador 20% exposición BMD AAA-AA-", "tramo": "20%", "verificacion": "exacta"}, {"entidad": "Restriccion:Ponderador 30% exposición BMD A+-A-", "tramo": "30%", "verificacion": "exacta"}, {"entidad": "Restriccion:Ponderador 50% exposición BMD BBB+-BBB-", "tramo": "50%", "verificacion": "exacta"}, {"entidad": "Restriccion:Ponderador 100% exposición BMD BB+-B-", "tramo": "100%", "verificacion": "exacta"}, {"entidad": "Restriccion:Ponderador 150% exposición BMD Inferior a B-", "tramo": "150%", "verificacion": "exacta"}, {"entidad": "Restriccion:Ponderador 50% exposición BMD no calificadas", "tramo": "50%", "verificacion": "exacta"}]; menciones [{"pred": "aplica_a", "mencion": "las entidades", "verificada": "exacta", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "las entidades", "verificada": "exacta", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "las entidades", "verificada": "exacta", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "las entidades", "verificada": "exacta", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "las entidades", "verificada": "exacta", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "las entidades", "verificada": "exacta", "sujeto_id": null}]; omisiones []; condicion_de []; limita [{"de": "Restriccion:Ponderador 20% exposición BMD AAA-AA-", "a": "Operacion:Exposición a BMD calificadas AAA-AA-"}, {"de": "Restriccion:Ponderador 30% exposición BMD A+-A-", "a": "Operacion:Exposición a BMD calificadas A+-A-"}, {"de": "Restriccion:Ponderador 50% exposición BMD BBB+-BBB-", "a": "Operacion:Exposición a BMD calificadas BBB+-BBB-"}, {"de": "Restriccion:Ponderador 100% exposición BMD BB+-B-", "a": "Operacion:Exposición a BMD calificadas BB+-B-"}, {"de": "Restriccion:Ponderador 150% exposición BMD Inferior a B-", "a": "Operacion:Exposición a BMD calificadas Inferior a B-"}, {"de": "Restriccion:Ponderador 50% exposición BMD no calificadas", "a": "Operacion:Exposición a BMD no calificadas"}]

*Cuantías en el texto propio: 6.*

## Ficha 50 — `ric::3.1.8`

**Texto propio:**

```
3.1.8. Exigencia adicional de capital por riesgo de crédito por financiaciones a clientes
con actividad agrícola que no sean MIPyMES y tengan un ratio de acopio supe-
rior al 5 % de su cosecha anual - Código 15000000.
Para el cómputo de la exigencia adicional establecida en el punto 11.5. de las
normas sobre “Capitales mínimos de las entidades financieras”, deberá aplicar-
se la siguiente metodología:
a) El saldo de las financiaciones y otras exposiciones se registrará en los códi-
gos que correspondan, previstos en esta sección, consignando los ponde-
radores y CCF pertinentes, de manera tal de determinar la exigencia gene-
ral;
b) En el código 15000000 se consignará el cargo adicional de capital resultan-
te de la diferencia entre lo registrado según lo señalado en el apartado a)
y el que resulte de aplicar a dicho importe el factor 4.
```
**Último bloque heredado:** 3.1. Normas de procedimiento.

**SELLADO** — error: None

- Operacion «Financiaciones a clientes agrícolas no MiPyME»: Financiaciones y otras exposiciones a clientes con actividad agrícola que no sean MiPyMEs y tengan un ratio de acopio superior al 5% de su cosecha anual
- Obligacion «Registrar saldo en códigos con ponderadores y CCF»: El saldo de las financiaciones y otras exposiciones se registrará en los códigos que correspondan, previstos en esta sección, consignando los ponderadores y CCF pertinentes, de manera tal de determinar la exigencia general
- Obligacion «Registrar cargo adicional en código 15000000»: En el código 15000000 se consignará el cargo adicional de capital resultante de la diferencia entre lo registrado según lo señalado en el apartado a) y el que resulte de aplicar a dicho importe el factor 4
- Definicion «Exigencia adicional de capital código 15000000»: Diferencia entre lo registrado según apartado a) y el que resulte de aplicar a dicho importe el factor 4
  - Operacion:Financiaciones a clientes agrícolas no MiPyME --establecida_en--> TextoOrdenado:Régimen informativo contable mensual
  - Obligacion:Registrar saldo en códigos con ponderadores y CCF --establecida_en--> TextoOrdenado:Régimen informativo contable mensual
  - Obligacion:Registrar cargo adicional en código 15000000 --establecida_en--> TextoOrdenado:Régimen informativo contable mensual
  - Definicion:Exigencia adicional de capital código 15000000 --establecida_en--> TextoOrdenado:Régimen informativo contable mensual
  - Obligacion:Registrar saldo en códigos con ponderadores y CCF --regula--> Operacion:Financiaciones a clientes agrícolas no MiPyME
  - Obligacion:Registrar cargo adicional en código 15000000 --regula--> Operacion:Financiaciones a clientes agrícolas no MiPyME
  - Obligacion:Registrar saldo en códigos con ponderadores y CCF --aplica_a--> None
  - Obligacion:Registrar cargo adicional en código 15000000 --aplica_a--> None
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}]; omisiones []; condicion_de []; limita []

**NUEVO** — error: None

- Operacion «Financiaciones a clientes con actividad agrícola»: Financiaciones y otras exposiciones de clientes con actividad agrícola que no sean MIPyMES y tengan un ratio de acopio superior al 5% de su cosecha anual ‖ tramo (exacta): «Financiaciones y otras exposiciones»
- Obligacion «Registrar saldo en códigos correspondientes»: El saldo de las financiaciones y otras exposiciones deberá registrarse en los códigos que correspondan, previstos en esta sección, consignando los ponderadores y CCF pertinentes, de manera tal de determinar la exigencia general ‖ tramo (exacta): «El saldo de las financiaciones y otras exposiciones se registrará en los códigos que correspondan, previstos en esta sección, consignando los ponderadores y CCF…»
- Obligacion «Consignar cargo adicional de capital en código 15000000»: En el código 15000000 deberá consignarse el cargo adicional de capital resultante de la diferencia entre lo registrado según el apartado a) y el que resulte de aplicar a dicho importe el factor 4 ‖ tramo (exacta): «En el código 15000000 se consignará el cargo adicional de capital resultante de la diferencia entre lo registrado según lo señalado en el apartado a) y el que r…»
- Definicion «Código 15000000»: Designación para registrar el cargo adicional de capital resultante de la diferencia entre lo registrado según la metodología general y el que resulte de aplicar a dicho importe el factor 4 ‖ tramo (exacta): «Código 15000000»
- Condicion «Ratio de acopio superior al 5% de cosecha anual»: Los clientes deben tener un ratio de acopio superior al 5% de su cosecha anual ‖ tramo (exacta): «tengan un ratio de acopio superior al 5 % de su cosecha anual»
- Restriccion «Exclusión de MIPyMES en exigencia adicional»: La exigencia adicional de capital no aplica a clientes que sean MIPyMES ‖ tramo (exacta): «que no sean MIPyMES»
  - Obligacion:Registrar saldo en códigos correspondientes --establecida_en--> TextoOrdenado:Régimen Informativo Contable
  - Obligacion:Consignar cargo adicional de capital en código 15000000 --establecida_en--> TextoOrdenado:Régimen Informativo Contable
  - Definicion:Código 15000000 --establecida_en--> TextoOrdenado:Régimen Informativo Contable
  - Condicion:Ratio de acopio superior al 5% de cosecha anual --establecida_en--> TextoOrdenado:Régimen Informativo Contable
  - Restriccion:Exclusión de MIPyMES en exigencia adicional --establecida_en--> TextoOrdenado:Régimen Informativo Contable
  - Operacion:Financiaciones a clientes con actividad agrícola --establecida_en--> TextoOrdenado:Régimen Informativo Contable
  - Obligacion:Registrar saldo en códigos correspondientes --aplica_a--> las entidades
  - Obligacion:Consignar cargo adicional de capital en código 15000000 --aplica_a--> las entidades
  - Obligacion:Registrar saldo en códigos correspondientes --regula--> Operacion:Financiaciones a clientes con actividad agrícola
  - Obligacion:Consignar cargo adicional de capital en código 15000000 --regula--> Operacion:Financiaciones a clientes con actividad agrícola
  - Condicion:Ratio de acopio superior al 5% de cosecha anual --condicion_de--> Obligacion:Registrar saldo en códigos correspondientes
  - Condicion:Ratio de acopio superior al 5% de cosecha anual --condicion_de--> Obligacion:Consignar cargo adicional de capital en código 15000000
  - rechazo: firma_invalida: relations[12]: Restriccion --exceptua_obligacion--> Obligacion
  - rechazo: firma_invalida: relations[13]: Restriccion --exceptua_obligacion--> Obligacion
- hechos: umbrales [{"entidad": "Condicion:Ratio de acopio superior al 5% de cosecha anual", "tramo": "superior al 5 %", "verificacion": "exacta"}]; menciones [{"pred": "aplica_a", "mencion": "las entidades", "verificada": "exacta", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "las entidades", "verificada": "exacta", "sujeto_id": null}]; omisiones [{"categoria": "meta_normativo", "tramo": "Para el cómputo de la exigencia adicional establecida en el punto 11.5. de las normas sobre \"Capital…", "verificacion": "exacta", "nota": "Remisión a otra norma y presentación de la metodología que será desarrollada a continuación. No pres…"}]; condicion_de [{"de": "Condicion:Ratio de acopio superior al 5% de cosecha anual", "a": "Obligacion:Registrar saldo en códigos correspondientes", "firma_nueva": false}, {"de": "Condicion:Ratio de acopio superior al 5% de cosecha anual", "a": "Obligacion:Consignar cargo adicional de capital en código 15000000", "firma_nueva": false}]; limita []

*Cuantías en el texto propio: 1.*

## Ficha 51 — `ric::4.3.3`

**Texto propio:**

```
4.3.3. Riesgo de posiciones en opciones
El total de exigencia por riesgo de posiciones en opciones se calculará conforme a lo
indicado en el punto 6.5. de las normas sobre “Capitales mínimos de las entidades
financieras”, utilizando los códigos de partida previstos en el punto 4.4.4.
La entidad podrá aplicar un sólo método de los previstos (simplificado o delta plus)
conforme a lo establecido en el punto 6.5.1. de las normas sobre “Capitales mínimos
de las entidades financieras”. Consecuentemente, si se informa el código 554100/xx no
podrán admitirse los códigos 554210/xx y/o 554220/xx, y viceversa. A estos efectos:
§ Si la entidad aplica el método simplificado:
Código 314000/xx = Código 554100/xx
§ Si la entidad aplica el método delta plus:
Código 314000/xx = Código 554210/xx + Código 554220/xx
4.3. Información complementaria vinculada al cálculo de la exigencia por riesgo de
mercado - Modelos de información
4.3.1. Riesgo específico de tasa
[TABLA ric::tabla004 | página 16 | e0_tablas | posicional]
Fila 1: col2 = Código de | col4 = Descripción ⟨abarca hasta col5⟩
Fila 2: col2 = Partida
Fila 3: col1 = 551100/xx ⟨abarca hasta col3⟩ | col4 = BCRA, Gobierno Nacional, gobiernos provinciales, municipales y de la Ciudad Autónoma de Buenos Aires en pesos cuando su fuente de financiación es esa moneda. ⟨abarca hasta col5⟩
Fila 4: col2 = 551110/xx | col4 = Plazo ≤ 6 meses.
Fila 5: col2 = 551120/xx | col4 = 6 meses < Plazo ≤ 24 meses.
Fila 6: col2 = 551130/xx | col4 = Plazo > 24 meses.
Fila 7: col1 = 551200/xx ⟨abarca hasta col3⟩ | col4 = Banco de Pagos Internacionales, Fondo Monetario Internacional,
Fila 8: col4 = Banco Central Europeo y Comunidad Europea y Bancos Multila-
Fila 9: col4 = terales de Desarrollo del punto 2.6.3.1. de las normas sobre “Ca-
Fila 10: col4 = pitales mínimos de las entidades financieras”
Fila 11: col1 = 551300/xx ⟨abarca hasta col3⟩ | col4 = BCRA y sector público no financiero. Demás. ⟨abarca hasta col5⟩
Fila 12: col1 = 551400/xx ⟨abarca hasta col3⟩ | col4 = Otros soberanos y sus bancos centrales. ⟨abarca hasta col5⟩
Fila 13: col1 = 551500/xx ⟨abarca hasta col3⟩ | col4 = Entidades financieras del país y del exterior. ⟨abarca hasta col5⟩
Fila 14: col1 = 551600/xx ⟨abarca hasta col3⟩ | col4 = Instrumentos con oferta pública autorizada emitidos por empre- sas y otras personas jurídicas del país y del exterior -incluyendo entidades cambiarias, aseguradoras, agentes regulados por la CNV y fiduciarios de fideicomisos no financieros- ⟨abarca hasta col5⟩
Fila 15: col1 = 551700/xx ⟨abarca hasta col3⟩ | col4 = Sector privado no financiero. Demás. ⟨abarca hasta col5⟩
[FIN TABLA ric::tabla004]
4.3.2. Riesgo general de tasa
a) Totales de exigencia
[TABLA ric::tabla005 | página 16 | e0_tablas | posicional]
Fila 1: col1 = Código de Partida | col2 = Descripción ⟨abarca hasta col4⟩
Fila 2: col1 = 5521 00/xx/M | col3 = Valor absoluto de la posición ponderada neta, comprada o vendida | col4 = ,
Fila 3: col3 = en toda la cartera de negociación.
Fila
```
**Último bloque heredado:** La información a que refieren los puntos 4.1.1.1. a 4.1.1.8. del presente régimen se comple- mentará con el envío mensual de los datos que se explicitan en el presente punto según el riesgo considerado. Las posiciones en los respectivos instrumentos y los componentes de exigencia se calcularán en fo…

**SELLADO** — error: None

- Operacion «Cálculo exigencia riesgo opciones»: Cálculo del total de exigencia por riesgo de posiciones en opciones conforme a lo indicado en punto 6.5. de normas de Capitales mínimos de entidades financieras
- Potestad «Elección método cálculo opciones»: La entidad podrá aplicar un sólo método de los previstos (simplificado o delta plus) conforme a lo establecido en punto 6.5.1. de normas sobre Capitales mínimos de entidades financieras
- Restriccion «Prohibición códigos simultáneos método»: Si se informa código 554100/xx no podrán admitirse códigos 554210/xx y/o 554220/xx, y viceversa
- Obligacion «Igualdad código simplificado»: Si la entidad aplica método simplificado: Código 314000/xx = Código 554100/xx
- Obligacion «Igualdad código delta plus»: Si la entidad aplica método delta plus: Código 314000/xx = Código 554210/xx + Código 554220/xx
- Definicion «Código 554100/xx - Exigencia simplificado»: Exigencia por método simplificado
- Definicion «Código 554210/xx - Riesgo Gamma»: Riesgo Gamma
- Definicion «Código 554220/xx - Riesgo Vega»: Riesgo Vega
  - Operacion:Cálculo exigencia riesgo opciones --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Potestad:Elección método cálculo opciones --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Restriccion:Prohibición códigos simultáneos método --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Obligacion:Igualdad código simplificado --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Obligacion:Igualdad código delta plus --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Definicion:Código 554100/xx - Exigencia simplificado --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Definicion:Código 554210/xx - Riesgo Gamma --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Definicion:Código 554220/xx - Riesgo Vega --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Operacion:Cálculo exigencia riesgo opciones --aplica_a--> None
  - Potestad:Elección método cálculo opciones --aplica_a--> None
  - Restriccion:Prohibición códigos simultáneos método --aplica_a--> None
  - Obligacion:Igualdad código simplificado --aplica_a--> None
  - Obligacion:Igualdad código delta plus --aplica_a--> None
  - Obligacion:Igualdad código simplificado --regula--> Operacion:Cálculo exigencia riesgo opciones
  - Obligacion:Igualdad código delta plus --regula--> Operacion:Cálculo exigencia riesgo opciones
  - Restriccion:Prohibición códigos simultáneos método --prohibe--> Operacion:Cálculo exigencia riesgo opciones
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}]; omisiones [{"categoria": null, "tramo": "", "verificacion": "ausente", "nota": "Tabla de ponderadores por banda y zona (punto 4.3.2.b): estructura tabular con 15 bandas y ponderado…"}, {"categoria": null, "tramo": "", "verificacion": "ausente", "nota": "Fórmulas de igualdad con códigos de partida: los valores específicos de mapeo de códigos en formatos…"}, {"categoria": null, "tramo": "", "verificacion": "ausente", "nota": "Tabla de definición de rangos de plazo y moneda (punto 4.3.2.b): estructura de Zona 1, Zona 2 y Zona…"}]; condicion_de []; limita []

**NUEVO** — error: None

- Operacion «Cálculo de exigencia por riesgo de opciones»: Cálculo del total de exigencia por riesgo de posiciones en opciones según las disposiciones de Capitales mínimos, utilizando los códigos de partida del punto 4.4.4. ‖ tramo (exacta): «El total de exigencia por riesgo de posiciones en opciones se calculará conforme a lo indicado en el punto 6.5. de las normas sobre "Capitales mínimos de las en…»
- Potestad «Aplicación de método simplificado o delta plus»: La entidad tiene la facultad de elegir aplicar únicamente un método entre el método simplificado o el método delta plus, según lo establecido en las normas de Capitales mínimos. ‖ tramo (exacta): «La entidad podrá aplicar un sólo método de los previstos (simplificado o delta plus) conforme a lo establecido en el punto 6.5.1. de las normas sobre "Capitales…»
- Restriccion «Exclusión mutua entre códigos métodos»: Si se informa el código 554100/xx (método simplificado) no pueden admitirse simultáneamente los códigos 554210/xx (Riesgo Gamma) y/o 554220/xx (Riesgo Vega), que corresponden al método delta plus. La prohibición es recíproca: si se informan… ‖ tramo (exacta): «Consecuentemente, si se informa el código 554100/xx no podrán admitirse los códigos 554210/xx y/o 554220/xx, y viceversa.»
- Definicion «Equivalencia método simplificado»: Cuando la entidad aplica el método simplificado, el código 314000/xx se equipara al código 554100/xx. ‖ tramo (exacta): «Código 314000/xx = Código 554100/xx»
- Definicion «Equivalencia método delta plus»: Cuando la entidad aplica el método delta plus, el código 314000/xx se equipara a la suma de los códigos 554210/xx y 554220/xx. ‖ tramo (exacta): «Código 314000/xx = Código 554210/xx + Código 554220/xx»
  - Operacion:Cálculo de exigencia por riesgo de opciones --establecida_en--> TextoOrdenado:Régimen Informativo Contable
  - Potestad:Aplicación de método simplificado o delta plus --establecida_en--> TextoOrdenado:Régimen Informativo Contable
  - Potestad:Aplicación de método simplificado o delta plus --aplica_a--> La entidad
  - Restriccion:Exclusión mutua entre códigos métodos --establecida_en--> TextoOrdenado:Régimen Informativo Contable
  - Definicion:Equivalencia método simplificado --establecida_en--> TextoOrdenado:Régimen Informativo Contable
  - Definicion:Equivalencia método delta plus --establecida_en--> TextoOrdenado:Régimen Informativo Contable
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "La entidad", "verificada": "exacta", "sujeto_id": null}]; omisiones [{"categoria": "formula", "tramo": "Código 314000/xx = Código 554100/xx", "verificacion": "exacta", "nota": "Fórmula de equivalencia entre códigos de partida. Contenido no confiable (FLAGS E0). Extraído como D…"}, {"categoria": "formula", "tramo": "Código 314000/xx = Código 554210/xx + Código 554220/xx", "verificacion": "exacta", "nota": "Fórmula de equivalencia entre códigos de partida. Contenido no confiable (FLAGS E0). Extraído como D…"}, {"categoria": "tabla", "tramo": "[TABLA ric::tabla010 | Códigos de partida para riesgo de posiciones en opciones]", "verificacion": "no", "nota": "Tabla serializada de códigos de partida (554100/xx, 554210/xx, 554220/xx) contenida en el punto 4.4.…"}]; condicion_de []; limita []

*Cuantías en el texto propio: 6.*

## Ficha 52 — `ric::9.2.1`

**Texto propio:**

```
9.2.1. Incrementos de exigencia
[TABLA ric::tabla022 | página 41 | e0_tablas | columnas]
Columnas: Código | Concepto | Importe
Fila 1: Código = 83100000 | Concepto = Incremento de la exigencia por riesgo de crédito por exceso en la relación de activos inmovilizados. Información en término
Fila 2: Código = 83200000 | Concepto = Incremento de la exigencia por riesgo de crédito por exceso en la relación de activos inmovilizados. Información fuera de término
Fila 3: Código = 83300000 | Concepto = Incremento de la exigencia por riesgo de crédito por exceso en la relación de activos inmovilizados. Incumplimientos reiterados
Fila 4: Código = 83400000 | Concepto = Incremento de la exigencia por riesgo de crédito por exceso en la relación de activos inmovilizados. Determinado por la SEFyC
Fila 5: Código = 83500000 | Concepto = Incremento de la exigencia por riesgo de crédito por exceso en Grandes Exposiciones al Riesgo de Crédito. Información en término
Fila 6: Código = 83600000 | Concepto = Incremento de la exigencia por riesgo de crédito por exceso en Grandes Exposiciones al Riesgo de Crédito. Información fuera de término
Fila 7: Código = 83700000 | Concepto = Incremento de la exigencia por riesgo de crédito por exceso en Grandes Exposiciones al Riesgo de Crédito. Incumplimientos reiterados
Fila 8: Código = 83800000 | Concepto = Incremento de la exigencia por riesgo de crédito por exceso en Grandes Exposiciones al Riesgo de Crédito. Determinado por la SEFyC
Fila 9: Código = 84300000 | Concepto = Incremento de la exigencia por riesgo de crédito por exceso en gradua- ción del crédito. Información en término
Fila 10: Código = 84400000 | Concepto = Incremento de la exigencia por riesgo de crédito por exceso en gradua- ción del crédito. Información fuera de término
Fila 11: Código = 84500000 | Concepto = Incremento de la exigencia por riesgo de crédito por exceso en gradua- ción del crédito. Incumplimientos reiterados.
Fila 12: Código = 84600000 | Concepto = Incremento de la exigencia por riesgo de crédito por exceso en gradua- ción del crédito. Determinado por la SEFyC.
Fila 13: Código = 85600000 | Concepto = Incremento de la exigencia por riesgo de crédito por la tenencia de certifi- cados o títulos de deuda de fideicomisos financieros. (25 %)
Fila 14: Código = 85700000 | Concepto = Incremento de la exigencia por riesgo de crédito por la tenencia de certifi- cados o títulos de deuda de fideicomisos financieros. (50 %)
Fila 15: Código = 85800000 | Concepto = Incremento de la exigencia por riesgo de crédito por la tenencia de certifi- cados o títulos de deuda de fideicomisos financieros. (100 %)
Fila 16: Código = 86300000 | Concepto = Incremento de la exigencia por riesgo de crédito por excesos en las parti- cipaciones en el capital de empresas (INC ) (Inversiones significativas en empresas)
[FIN TABLA ric::tabla022]
[TABLA ric::tabla023 | página 42 | e0_tablas | posicional]
Fila 1: col1 = 87100000 | col2 = Incremento de la exigencia por riesgo de crédito po
```
**Último bloque heredado:** 9.2. Modelo de Información

**SELLADO** — error: None

- hechos: umbrales []; menciones []; omisiones [{"categoria": null, "tramo": "", "verificacion": "ausente", "nota": "Contenido tabular con códigos de cuenta (columna Código) y conceptos normativo-informativos (columna…"}, {"categoria": null, "tramo": "", "verificacion": "ausente", "nota": "Análisis de cada fila de la tabla: cada entrada enumera un tipo de 'Incremento de exigencia' calific…"}]; condicion_de []; limita []

**NUEVO** — error: None

- Operacion «Incremento exigencia — activos inmovilizados — término»: Incremento de la exigencia por riesgo de crédito por exceso en la relación de activos inmovilizados cuando la información se presenta en término. Código contable: 83100000. ‖ tramo (exacta): «Incremento de la exigencia por riesgo de crédito por exceso en la relación de activos inmovilizados. Información en término»
- Operacion «Incremento exigencia — activos inmovilizados — fuera de término»: Incremento de la exigencia por riesgo de crédito por exceso en la relación de activos inmovilizados cuando la información se presenta fuera de término. Código contable: 83200000. ‖ tramo (exacta): «Incremento de la exigencia por riesgo de crédito por exceso en la relación de activos inmovilizados. Información fuera de término»
- Operacion «Incremento exigencia — activos inmovilizados — incumplimientos reiterados»: Incremento de la exigencia por riesgo de crédito por exceso en la relación de activos inmovilizados por incumplimientos reiterados. Código contable: 83300000. ‖ tramo (exacta): «Incremento de la exigencia por riesgo de crédito por exceso en la relación de activos inmovilizados. Incumplimientos reiterados»
- Operacion «Incremento exigencia — activos inmovilizados — determinado SEFyC»: Incremento de la exigencia por riesgo de crédito por exceso en la relación de activos inmovilizados determinado por la SEFyC. Código contable: 83400000. ‖ tramo (exacta): «Incremento de la exigencia por riesgo de crédito por exceso en la relación de activos inmovilizados. Determinado por la SEFyC»
- Operacion «Incremento exigencia — Grandes Exposiciones — término»: Incremento de la exigencia por riesgo de crédito por exceso en Grandes Exposiciones al Riesgo de Crédito cuando la información se presenta en término. Código contable: 83500000. ‖ tramo (exacta): «Incremento de la exigencia por riesgo de crédito por exceso en Grandes Exposiciones al Riesgo de Crédito. Información en término»
- Operacion «Incremento exigencia — Grandes Exposiciones — fuera de término»: Incremento de la exigencia por riesgo de crédito por exceso en Grandes Exposiciones al Riesgo de Crédito cuando la información se presenta fuera de término. Código contable: 83600000. ‖ tramo (exacta): «Incremento de la exigencia por riesgo de crédito por exceso en Grandes Exposiciones al Riesgo de Crédito. Información fuera de término»
- Operacion «Incremento exigencia — Grandes Exposiciones — incumplimientos reiterados»: Incremento de la exigencia por riesgo de crédito por exceso en Grandes Exposiciones al Riesgo de Crédito por incumplimientos reiterados. Código contable: 83700000. ‖ tramo (exacta): «Incremento de la exigencia por riesgo de crédito por exceso en Grandes Exposiciones al Riesgo de Crédito. Incumplimientos reiterados»
- Operacion «Incremento exigencia — Grandes Exposiciones — determinado SEFyC»: Incremento de la exigencia por riesgo de crédito por exceso en Grandes Exposiciones al Riesgo de Crédito determinado por la SEFyC. Código contable: 83800000. ‖ tramo (exacta): «Incremento de la exigencia por riesgo de crédito por exceso en Grandes Exposiciones al Riesgo de Crédito. Determinado por la SEFyC»
- Operacion «Incremento exigencia — graduación crédito — término»: Incremento de la exigencia por riesgo de crédito por exceso en graduación del crédito cuando la información se presenta en término. Código contable: 84300000. ‖ tramo (no): «Incremento de la exigencia por riesgo de crédito por exceso en graduación del crédito. Información en término»
- Operacion «Incremento exigencia — graduación crédito — fuera de término»: Incremento de la exigencia por riesgo de crédito por exceso en graduación del crédito cuando la información se presenta fuera de término. Código contable: 84400000. ‖ tramo (no): «Incremento de la exigencia por riesgo de crédito por exceso en graduación del crédito. Información fuera de término»
- Operacion «Incremento exigencia — graduación crédito — incumplimientos reiterados»: Incremento de la exigencia por riesgo de crédito por exceso en graduación del crédito por incumplimientos reiterados. Código contable: 84500000. ‖ tramo (no): «Incremento de la exigencia por riesgo de crédito por exceso en graduación del crédito. Incumplimientos reiterados»
- Operacion «Incremento exigencia — graduación crédito — determinado SEFyC»: Incremento de la exigencia por riesgo de crédito por exceso en graduación del crédito determinado por la SEFyC. Código contable: 84600000. ‖ tramo (no): «Incremento de la exigencia por riesgo de crédito por exceso en graduación del crédito. Determinado por la SEFyC»
- Operacion «Incremento exigencia — fideicomisos financieros — 25 %»: Incremento de la exigencia por riesgo de crédito por la tenencia de certificados o títulos de deuda de fideicomisos financieros al 25 %. Código contable: 85600000. ‖ tramo (no): «Incremento de la exigencia por riesgo de crédito por la tenencia de certificados o títulos de deuda de fideicomisos financieros. (25 %)»
- Operacion «Incremento exigencia — fideicomisos financieros — 50 %»: Incremento de la exigencia por riesgo de crédito por la tenencia de certificados o títulos de deuda de fideicomisos financieros al 50 %. Código contable: 85700000. ‖ tramo (no): «Incremento de la exigencia por riesgo de crédito por la tenencia de certificados o títulos de deuda de fideicomisos financieros. (50 %)»
- Operacion «Incremento exigencia — fideicomisos financieros — 100 %»: Incremento de la exigencia por riesgo de crédito por la tenencia de certificados o títulos de deuda de fideicomisos financieros al 100 %. Código contable: 85800000. ‖ tramo (no): «Incremento de la exigencia por riesgo de crédito por la tenencia de certificados o títulos de deuda de fideicomisos financieros. (100 %)»
- Operacion «Incremento exigencia — participaciones capital empresas»: Incremento de la exigencia por riesgo de crédito por excesos en las participaciones en el capital de empresas (inversiones significativas en empresas). Código contable: 86300000. ‖ tramo (no): «Incremento de la exigencia por riesgo de crédito por excesos en las participaciones en el capital de empresas (INC ) (Inversiones significativas en empresas)»
- Operacion «Incremento exigencia — sector público no financiero — término»: Incremento de la exigencia por riesgo de crédito por exceso en financiamiento al sector público no financiero cuando la información se presenta en término. Código contable: 87100000. ‖ tramo (no): «Incremento de la exigencia por riesgo de crédito por exceso en financiamiento al sector público no financiero. Información en término»
- Operacion «Incremento exigencia — sector público no financiero — fuera de término»: Incremento de la exigencia por riesgo de crédito por exceso en financiamiento al sector público no financiero cuando la información se presenta fuera de término. Código contable: 87200000. ‖ tramo (no): «Incremento de la exigencia por riesgo de crédito por exceso en financiamiento al sector público no financiero. Información fuera de término»
- Operacion «Incremento exigencia — sector público no financiero — incumplimientos reiterados»: Incremento de la exigencia por riesgo de crédito por exceso en financiamiento al sector público no financiero por incumplimientos reiterados. Código contable: 87300000. ‖ tramo (no): «Incremento de la exigencia por riesgo de crédito por exceso en financiamiento al sector público no financiero. Incumplimientos reiterados»
- Operacion «Incremento exigencia — sector público no financiero — determinado SEFyC»: Incremento de la exigencia por riesgo de crédito por exceso en financiamiento al sector público no financiero determinado por la SEFyC. Código contable: 87400000. ‖ tramo (no): «Incremento de la exigencia por riesgo de crédito por exceso en financiamiento al sector público no financiero. Determinado por la SEFyC»
- Operacion «Incremento exigencia — derivados commodities — término»: Incremento de la exigencia por riesgo de crédito por exceso en posiciones de derivados sobre commodities cuando la información se presenta en término. Código contable: 87500000. ‖ tramo (no): «Incremento de la exigencia por riesgo de crédito por exceso en posiciones de derivados sobre "commodities". Información en término»
- Operacion «Incremento exigencia — derivados commodities — fuera de término»: Incremento de la exigencia por riesgo de crédito por exceso en posiciones de derivados sobre commodities cuando la información se presenta fuera de término. Código contable: 87600000. ‖ tramo (no): «Incremento de la exigencia por riesgo de crédito por exceso en posiciones de derivados sobre "commodities". Información fuera de término»
- Operacion «Incremento exigencia — derivados commodities — incumplimientos reiterados»: Incremento de la exigencia por riesgo de crédito por exceso en posiciones de derivados sobre commodities por incumplimientos reiterados. Código contable: 87700000. ‖ tramo (no): «Incremento de la exigencia por riesgo de crédito por exceso en posiciones de derivados sobre "commodities". Incumplimientos reiterados»
- Operacion «Incremento exigencia — derivados commodities — determinado SEFyC»: Incremento de la exigencia por riesgo de crédito por exceso en posiciones de derivados sobre commodities determinado por la SEFyC. Código contable: 87800000. ‖ tramo (no): «Incremento de la exigencia por riesgo de crédito por exceso en posiciones de derivados sobre "commodities". Determinado por la SEFyC»
  - Operacion:Incremento exigencia — activos inmovilizados — término --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Operacion:Incremento exigencia — activos inmovilizados — fuera de térm… --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Operacion:Incremento exigencia — activos inmovilizados — incumplimient… --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Operacion:Incremento exigencia — activos inmovilizados — determinado S… --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Operacion:Incremento exigencia — Grandes Exposiciones — término --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Operacion:Incremento exigencia — Grandes Exposiciones — fuera de térmi… --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Operacion:Incremento exigencia — Grandes Exposiciones — incumplimiento… --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Operacion:Incremento exigencia — Grandes Exposiciones — determinado SE… --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Operacion:Incremento exigencia — graduación crédito — término --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Operacion:Incremento exigencia — graduación crédito — fuera de término --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Operacion:Incremento exigencia — graduación crédito — incumplimientos … --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Operacion:Incremento exigencia — graduación crédito — determinado SEFy… --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Operacion:Incremento exigencia — fideicomisos financieros — 25 % --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Operacion:Incremento exigencia — fideicomisos financieros — 50 % --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Operacion:Incremento exigencia — fideicomisos financieros — 100 % --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Operacion:Incremento exigencia — participaciones capital empresas --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Operacion:Incremento exigencia — sector público no financiero — términ… --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Operacion:Incremento exigencia — sector público no financiero — fuera … --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Operacion:Incremento exigencia — sector público no financiero — incump… --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Operacion:Incremento exigencia — sector público no financiero — determ… --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Operacion:Incremento exigencia — derivados commodities — término --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Operacion:Incremento exigencia — derivados commodities — fuera de térm… --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Operacion:Incremento exigencia — derivados commodities — incumplimient… --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Operacion:Incremento exigencia — derivados commodities — determinado S… --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
- hechos: umbrales []; menciones []; omisiones []; condicion_de []; limita []

*Cuantías en el texto propio: 3.*

## Ficha 53 — `ctacte::8.3::intro`

**Texto propio:**

```
Se demostrará con cualquiera de las siguientes alternativas:
```
**Último bloque heredado:** 8.3. Cancelaciones de cheques rechazados.

**SELLADO** — error: None

- hechos: umbrales []; menciones []; omisiones []; condicion_de []; limita []

**NUEVO** — error: None

- hechos: umbrales []; menciones []; omisiones [{"categoria": "meta_normativo", "tramo": "Se demostrará con cualquiera de las siguientes alternativas:", "verificacion": "exacta", "nota": "Enunciado introductorio que declara cómo se probará algo (contenido procedural que anuncia una lista…"}]; condicion_de []; limita []

*Cuantías en el texto propio: 0.*

## Ficha 54 — `ext::13.4.4`

**Texto propio:**

```
13.4.4. el cliente cuenta por el equivalente al monto a pagar con una “Certificación por los
regímenes de acceso a divisas para la producción incremental de petróleo y/o gas
natural (Decreto 277/22)” emitida en el marco de lo dispuesto en el punto 3.17.; o
```
**Último bloque heredado:** Se requerirá la conformidad previa del BCRA para el acceso al mercado de cambios para realizar pagos de servicios de no residentes prestados o devengados hasta el 12/12/23, excepto cuando, adicionalmente a los restantes requisitos aplicables, la entidad verifique que:

**SELLADO** — error: None

- Condicion «Cliente cuenta certificación — regímenes acceso divisas»: el cliente cuenta por el equivalente al monto a pagar con una 'Certificación por los regímenes de acceso a divisas para la producción incremental de petróleo y/o gas natural (Decreto 277/22)' emitida en el marco de lo dispuesto en el punto …
- Operacion «Acceso al mercado de cambios — pago servicios no residentes»: Acceso al mercado de cambios para realizar pagos de servicios de no residentes prestados o devengados hasta el 12/12/23
- Obligacion «Verificación cliente cuenta certificación acceso divisas»: la entidad verifique que el cliente cuenta por el equivalente al monto a pagar con una Certificación por los regímenes de acceso a divisas para la producción incremental de petróleo y/o gas natural (Decreto 277/22)
  - Condicion:Cliente cuenta certificación — regímenes acceso divisas --condicion_de--> Obligacion:Verificación cliente cuenta certificación acceso divisas
  - Obligacion:Verificación cliente cuenta certificación acceso divisas --aplica_a--> None
  - Condicion:Cliente cuenta certificación — regímenes acceso divisas --establecida_en--> TextoOrdenado:Exterior - Operaciones en cambios
  - Obligacion:Verificación cliente cuenta certificación acceso divisas --establecida_en--> TextoOrdenado:Exterior - Operaciones en cambios
  - rechazo: firma_invalida: relations[1]: Obligacion --requiere--> Operacion
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}]; omisiones []; condicion_de [{"de": "Condicion:Cliente cuenta certificación — regímenes acceso divisas", "a": "Obligacion:Verificación cliente cuenta certificación acceso divisas", "firma_nueva": false}]; limita []

**NUEVO** — error: None

- Condicion «Cliente con Certificación regímenes acceso divisas»: El cliente posee una Certificación por los regímenes de acceso a divisas para la producción incremental de petróleo y/o gas natural (Decreto 277/22), emitida conforme al punto 3.17. ‖ tramo (exacta): «el cliente cuenta por el equivalente al monto a pagar con una "Certificación por los regímenes de acceso a divisas para la producción incremental de petróleo y/…»
- Excepcion «Excepción conformidad previa BCRA — cliente con Certificación»: No se requiere conformidad previa del BCRA para el acceso al mercado de cambios cuando la entidad verifica que el cliente cuenta con Certificación por los regímenes de acceso a divisas para la producción incremental de petróleo y/o gas natu… ‖ tramo (exacta): «adicionalmente a los restantes requisitos aplicables, la entidad verifique que: […] el cliente cuenta por el equivalente al monto a pagar con una "Certificación…»
- Operacion «Acceso al mercado de cambios — pago servicios no residentes»: Pago de servicios de no residentes prestados o devengados hasta el 12/12/23 en acceso al mercado de cambios. ‖ tramo (exacta): «pagos de servicios de no residentes prestados o devengados hasta el 12/12/23»
- Restriccion «Requerimiento conformidad previa BCRA — acceso mercado cambios»: Se requerirá la conformidad previa del BCRA para el acceso al mercado de cambios para realizar pagos de servicios de no residentes prestados o devengados hasta el 12/12/23, excepto cuando se verifiquen los supuestos enumerados. ‖ tramo (exacta): «Se requerirá la conformidad previa del BCRA para el acceso al mercado de cambios para realizar pagos de servicios de no residentes prestados o devengados hasta …»
  - Condicion:Cliente con Certificación regímenes acceso divisas --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Excepcion:Excepción conformidad previa BCRA — cliente con Certificació… --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Operacion:Acceso al mercado de cambios — pago servicios no residentes --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Restriccion:Requerimiento conformidad previa BCRA — acceso mercado cambi… --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Condicion:Cliente con Certificación regímenes acceso divisas --condicion_de--> Excepcion:Excepción conformidad previa BCRA — cliente con Certificació…
  - Excepcion:Excepción conformidad previa BCRA — cliente con Certificació… --exceptua--> Restriccion:Requerimiento conformidad previa BCRA — acceso mercado cambi…
  - Restriccion:Requerimiento conformidad previa BCRA — acceso mercado cambi… --limita--> Operacion:Acceso al mercado de cambios — pago servicios no residentes
  - Restriccion:Requerimiento conformidad previa BCRA — acceso mercado cambi… --aplica_a--> la entidad
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "la entidad", "verificada": "exacta", "sujeto_id": null}]; omisiones [{"categoria": "meta_normativo", "tramo": "emitida en el marco de lo dispuesto en el punto 3.17.", "verificacion": "exacta", "nota": "Remisión a otro punto del TO para definir el marco de emisión de la Certificación; la remisión se re…"}]; condicion_de [{"de": "Condicion:Cliente con Certificación regímenes acceso divisas", "a": "Excepcion:Excepción conformidad previa BCRA — cliente con Certificació…", "firma_nueva": false}]; limita [{"de": "Restriccion:Requerimiento conformidad previa BCRA — acceso mercado cambi…", "a": "Operacion:Acceso al mercado de cambios — pago servicios no residentes"}]

*Cuantías en el texto propio: 0.*

## Ficha 55 — `opefci::2.1`

**Texto propio:**

```
2.1. Entidades habilitadas.
Entidades financieras.
```
**Último bloque heredado:** Sección 2. Operaciones al contado a liquidar.

**SELLADO** — error: None

- hechos: umbrales []; menciones []; omisiones []; condicion_de []; limita []

**NUEVO** — error: None

- Operacion «Operaciones al contado a liquidar»: Operaciones al contado a liquidar realizadas por entidades financieras ‖ tramo (exacta): «Operaciones al contado a liquidar»
  - Operacion:Operaciones al contado a liquidar --establecida_en--> TextoOrdenado:Operaciones al Contado a Liquidar
  - Operacion:Operaciones al contado a liquidar --aplica_a--> Entidades financieras
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "Entidades financieras", "verificada": "exacta", "sujeto_id": null}]; omisiones []; condicion_de []; limita []

*Cuantías en el texto propio: 0.*

## Ficha 56 — `cap::8.4.1.19`

**Texto propio:**

```
8.4.1.19. Inversiones en el capital de entidades financieras sujetas a supervisión con-
solidada.
i) Participaciones en entidades financieras, excepto cuando rijan franquicias
para no deducirlas.
ii) Participaciones en entidades financieras del exterior.
En dichos casos, serán netas de las previsiones por riesgo de desvalorización y,
cuando se trate de entidades financieras controladas y corresponda aplicar lo
previsto en el punto 8.2.1.6. –acápite iii)–, del 50 % de las ganancias de éstas
en la proporción de la respectiva participación.
```
**Último bloque heredado:** COn1

**SELLADO** — error: None

- Operacion «Inversiones en capital de entidades financieras — supervisión consolidada»: Inversiones en el capital de entidades financieras sujetas a supervisión consolidada
- Restriccion «Participaciones en entidades financieras — deducción salvo franquicia»: Las participaciones en entidades financieras se deducen, excepto cuando rijan franquicias para no deducirlas
- Restriccion «Participaciones en entidades financieras del exterior — deducción»: Las participaciones en entidades financieras del exterior son deducibles
- Obligacion «Neto de previsiones por riesgo de desvalorización»: Las participaciones serán netas de las previsiones por riesgo de desvalorización
- Condicion «Entidades financieras controladas — aplicación del 50% de ganancias»: Cuando se trate de entidades financieras controladas y corresponda aplicar lo previsto en el punto 8.2.1.6 –acápite iii)–
- Obligacion «Aplicar 50% de ganancias — entidades controladas»: Del 50% de las ganancias de las entidades financieras controladas en la proporción de la respectiva participación
  - Operacion:Inversiones en capital de entidades financieras — supervisió… --establecida_en--> TextoOrdenado:Capitales mínimos
  - Restriccion:Participaciones en entidades financieras — deducción salvo f… --establecida_en--> TextoOrdenado:Capitales mínimos
  - Restriccion:Participaciones en entidades financieras del exterior — dedu… --establecida_en--> TextoOrdenado:Capitales mínimos
  - Obligacion:Neto de previsiones por riesgo de desvalorización --establecida_en--> TextoOrdenado:Capitales mínimos
  - Condicion:Entidades financieras controladas — aplicación del 50% de ga… --establecida_en--> TextoOrdenado:Capitales mínimos
  - Obligacion:Aplicar 50% de ganancias — entidades controladas --establecida_en--> TextoOrdenado:Capitales mínimos
  - Restriccion:Participaciones en entidades financieras — deducción salvo f… --limita--> Operacion:Inversiones en capital de entidades financieras — supervisió…
  - Restriccion:Participaciones en entidades financieras del exterior — dedu… --limita--> Operacion:Inversiones en capital de entidades financieras — supervisió…
  - Obligacion:Neto de previsiones por riesgo de desvalorización --regula--> Operacion:Inversiones en capital de entidades financieras — supervisió…
  - Condicion:Entidades financieras controladas — aplicación del 50% de ga… --condicion_de--> Obligacion:Aplicar 50% de ganancias — entidades controladas
  - Obligacion:Aplicar 50% de ganancias — entidades controladas --regula--> Operacion:Inversiones en capital de entidades financieras — supervisió…
  - Operacion:Inversiones en capital de entidades financieras — supervisió… --aplica_a--> None
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}]; omisiones []; condicion_de [{"de": "Condicion:Entidades financieras controladas — aplicación del 50% de ga…", "a": "Obligacion:Aplicar 50% de ganancias — entidades controladas", "firma_nueva": false}]; limita [{"de": "Restriccion:Participaciones en entidades financieras — deducción salvo f…", "a": "Operacion:Inversiones en capital de entidades financieras — supervisió…"}, {"de": "Restriccion:Participaciones en entidades financieras del exterior — dedu…", "a": "Operacion:Inversiones en capital de entidades financieras — supervisió…"}]

**NUEVO** — error: None

- Operacion «Participaciones en entidades financieras sujetas a supervisión consolidada»: Participaciones en entidades financieras, excepto cuando rijan franquicias para no deducirlas. ‖ tramo (exacta): «Participaciones en entidades financieras»
- Operacion «Participaciones en entidades financieras del exterior»: Participaciones en entidades financieras del exterior. ‖ tramo (exacta): «Participaciones en entidades financieras del exterior»
- Restriccion «Deducción neta de previsiones por riesgo de desvalorización»: Las participaciones serán netas de las previsiones por riesgo de desvalorización. ‖ tramo (exacta): «serán netas de las previsiones por riesgo de desvalorización»
- Restriccion «Deducción 50% ganancias en entidades financieras controladas»: Cuando se trate de entidades financieras controladas y corresponda aplicar lo previsto en el punto 8.2.1.6 –acápite iii)–, serán netas del 50 % de las ganancias de éstas en la proporción de la respectiva participación. ‖ tramo (exacta): «del 50 % de las ganancias de éstas en la proporción de la respectiva participación»
- Excepcion «Excepción por franquicias para no deducir participaciones»: Las participaciones en entidades financieras no serán deducibles cuando rijan franquicias para no deducirlas. ‖ tramo (exacta): «excepto cuando rijan franquicias para no deducirlas»
  - Operacion:Participaciones en entidades financieras sujetas a supervisi… --establecida_en--> TextoOrdenado:Texto Ordenado de Capitales Mínimos
  - Operacion:Participaciones en entidades financieras del exterior --establecida_en--> TextoOrdenado:Texto Ordenado de Capitales Mínimos
  - Restriccion:Deducción neta de previsiones por riesgo de desvalorización --establecida_en--> TextoOrdenado:Texto Ordenado de Capitales Mínimos
  - Restriccion:Deducción 50% ganancias en entidades financieras controladas --establecida_en--> TextoOrdenado:Texto Ordenado de Capitales Mínimos
  - Excepcion:Excepción por franquicias para no deducir participaciones --establecida_en--> TextoOrdenado:Texto Ordenado de Capitales Mínimos
  - Restriccion:Deducción neta de previsiones por riesgo de desvalorización --limita--> Operacion:Participaciones en entidades financieras sujetas a supervisi…
  - Restriccion:Deducción neta de previsiones por riesgo de desvalorización --limita--> Operacion:Participaciones en entidades financieras del exterior
  - Restriccion:Deducción 50% ganancias en entidades financieras controladas --limita--> Operacion:Participaciones en entidades financieras sujetas a supervisi…
  - Excepcion:Excepción por franquicias para no deducir participaciones --exceptua--> Restriccion:Deducción neta de previsiones por riesgo de desvalorización
- hechos: umbrales [{"entidad": "Restriccion:Deducción 50% ganancias en entidades financieras controladas", "tramo": "del 50 % de las ganancias", "verificacion": "exacta"}]; menciones []; omisiones [{"categoria": "relacion_sin_predicado", "tramo": "cuando se trate de entidades financieras controladas y corresponda aplicar lo previsto en el punto 8…", "verificacion": "exacta", "nota": "remisión a norma externa (punto 8.2.1.6); el vínculo condicional entre esta restricción y esa norma …"}]; condicion_de []; limita [{"de": "Restriccion:Deducción neta de previsiones por riesgo de desvalorización", "a": "Operacion:Participaciones en entidades financieras sujetas a supervisi…"}, {"de": "Restriccion:Deducción neta de previsiones por riesgo de desvalorización", "a": "Operacion:Participaciones en entidades financieras del exterior"}, {"de": "Restriccion:Deducción 50% ganancias en entidades financieras controladas", "a": "Operacion:Participaciones en entidades financieras sujetas a supervisi…"}]

*Cuantías en el texto propio: 1.*

## Ficha 57 — `adrei::4.3.1.2`

**Texto propio:**

```
4.3.1.2. Procurar que los informes reflejen un adecuado equilibrio entre los datos detalla-
dos de riesgos, su análisis cualitativo e interpretación, explicaciones y recomen-
daciones. Las interpretaciones y explicaciones que se hagan de los datos deben
ser claras.
El balance entre información cualitativa y cuantitativa variará en los diferentes ni-
veles de la organización y dependerá también del nivel de agregación que se
aplique a los informes. En los niveles superiores de la organización se espera
más agregación, siendo necesario, por lo tanto, un mayor grado de interpretación
cualitativa.
```
**Último bloque heredado:** Las entidades financieras deben:

**SELLADO** — error: None

- Obligacion «Equilibrio entre datos detallados, análisis cualitativo e interpretación»: Procurar que los informes reflejen un adecuado equilibrio entre los datos detallados de riesgos, su análisis cualitativo e interpretación, explicaciones y recomendaciones. Las interpretaciones y explicaciones que se hagan de los datos deben…
- Condicion «Variación del balance según niveles organizacionales»: El balance entre información cualitativa y cuantitativa variará en los diferentes niveles de la organización y dependerá también del nivel de agregación que se aplique a los informes.
- Obligacion «Mayor interpretación cualitativa en niveles superiores»: En los niveles superiores de la organización se espera más agregación, siendo necesario, por lo tanto, un mayor grado de interpretación cualitativa.
  - Obligacion:Equilibrio entre datos detallados, análisis cualitativo e in… --establecida_en--> TextoOrdenado:Agregación de datos sobre riesgos: D-SIB
  - Condicion:Variación del balance según niveles organizacionales --establecida_en--> TextoOrdenado:Agregación de datos sobre riesgos: D-SIB
  - Obligacion:Mayor interpretación cualitativa en niveles superiores --establecida_en--> TextoOrdenado:Agregación de datos sobre riesgos: D-SIB
  - Obligacion:Equilibrio entre datos detallados, análisis cualitativo e in… --aplica_a--> None
  - Obligacion:Mayor interpretación cualitativa en niveles superiores --aplica_a--> None
  - Condicion:Variación del balance según niveles organizacionales --condicion_de--> Obligacion:Equilibrio entre datos detallados, análisis cualitativo e in…
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}]; omisiones []; condicion_de [{"de": "Condicion:Variación del balance según niveles organizacionales", "a": "Obligacion:Equilibrio entre datos detallados, análisis cualitativo e in…", "firma_nueva": false}]; limita []

**NUEVO** — error: None

- Obligacion «Balance entre datos detallados, análisis cualitativo e interpretación»: Las entidades financieras deben procurar que los informes reflejen un adecuado equilibrio entre los datos detallados de riesgos, su análisis cualitativo e interpretación, explicaciones y recomendaciones; las interpretaciones y explicaciones… ‖ tramo (exacta): «Procurar que los informes reflejen un adecuado equilibrio entre los datos detallados de riesgos, su análisis cualitativo e interpretación, explicaciones y recom…»
- Obligacion «Claridad en interpretaciones y explicaciones de datos»: Las interpretaciones y explicaciones que se hagan de los datos en los informes deben ser claras ‖ tramo (exacta): «Las interpretaciones y explicaciones que se hagan de los datos deben ser claras»
- Condicion «Balance variará según niveles organizacionales y agregación»: El balance entre información cualitativa y cuantitativa varía según los diferentes niveles de la organización y depende del nivel de agregación aplicado a los informes ‖ tramo (exacta): «El balance entre información cualitativa y cuantitativa variará en los diferentes niveles de la organización y dependerá también del nivel de agregación que se …»
- Obligacion «Mayor agregación e interpretación cualitativa en niveles superiores»: En los niveles superiores de la organización se espera una mayor agregación y, por lo tanto, un mayor grado de interpretación cualitativa en los informes ‖ tramo (exacta): «En los niveles superiores de la organización se espera más agregación, siendo necesario, por lo tanto, un mayor grado de interpretación cualitativa» ‖ no definidas: {"modalidad": "se espera", "modalidad_clasificada": "recomendacion"}
  - Obligacion:Balance entre datos detallados, análisis cualitativo e inter… --establecida_en--> TextoOrdenado:Agregación de datos sobre riesgos: D-SIB
  - Obligacion:Claridad en interpretaciones y explicaciones de datos --establecida_en--> TextoOrdenado:Agregación de datos sobre riesgos: D-SIB
  - Condicion:Balance variará según niveles organizacionales y agregación --establecida_en--> TextoOrdenado:Agregación de datos sobre riesgos: D-SIB
  - Obligacion:Mayor agregación e interpretación cualitativa en niveles sup… --establecida_en--> TextoOrdenado:Agregación de datos sobre riesgos: D-SIB
  - Obligacion:Balance entre datos detallados, análisis cualitativo e inter… --aplica_a--> Las entidades financieras
  - Obligacion:Claridad en interpretaciones y explicaciones de datos --aplica_a--> Las entidades financieras
  - Obligacion:Mayor agregación e interpretación cualitativa en niveles sup… --aplica_a--> Las entidades financieras
  - Condicion:Balance variará según niveles organizacionales y agregación --condicion_de--> Obligacion:Balance entre datos detallados, análisis cualitativo e inter…
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "Las entidades financieras", "verificada": "exacta", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "Las entidades financieras", "verificada": "exacta", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "Las entidades financieras", "verificada": "exacta", "sujeto_id": null}]; omisiones [{"categoria": "meta_normativo", "tramo": "Para alcanzar de forma eficaz sus objetivos, los informes de riesgos deben satisfacer los criterios …", "verificacion": "no", "nota": "Declaración de objetivo y estructura del capítulo; no enuncia conducta prescrita"}]; condicion_de [{"de": "Condicion:Balance variará según niveles organizacionales y agregación", "a": "Obligacion:Balance entre datos detallados, análisis cualitativo e inter…", "firma_nueva": false}]; limita []

*Cuantías en el texto propio: 0.*

## Ficha 58 — `ctacte::4.2.1`

**Texto propio:**

```
4.2.1. Solicitud.
El titular de una cuenta corriente en la que se utilicen cheques de pago diferido o el tene-
dor de uno de ellos podrán –indistintamente– requerir en forma directa, mediante la inte-
gración de la pertinente solicitud, el registro de un cheque de esas características librado
por aquél, recibiendo, en caso de no existir objeciones por parte del girado, el cartular o,
cuando se otorgue el aval, el certificado nominativo transferible extendido a nombre del
solicitante.
```
**Último bloque heredado:** Una vez emitidos podrán ser presentados a registro hasta el día anterior a su vencimiento. En caso de que esa presentación se efectúe en alguno de los 14 días corridos inmediatos anterio- res al vencimiento, mantienen vigencia el procedimiento y los plazos previstos en el punto 4.2.2.4.

**SELLADO** — error: None

- Operacion «Registro de cheque de pago diferido»: El titular de una cuenta corriente en la que se utilicen cheques de pago diferido o el tenedor de uno de ellos podrán requerir en forma directa, mediante la integración de la pertinente solicitud, el registro de un cheque de esas caracterís…
- Potestad «Requerir registro de cheque diferido en forma directa»: El titular de una cuenta corriente en la que se utilicen cheques de pago diferido o el tenedor de uno de ellos podrán requerir en forma directa, mediante la integración de la pertinente solicitud, el registro de un cheque de esas caracterís…
  - Operacion:Registro de cheque de pago diferido --establecida_en--> TextoOrdenado:Cuentas de corresponsalía
  - Potestad:Requerir registro de cheque diferido en forma directa --establecida_en--> TextoOrdenado:Cuentas de corresponsalía
  - rechazo: firma_invalida: relations[2]: Sujeto --ejecuta--> Potestad
  - rechazo: firma_invalida: relations[3]: Sujeto --ejecuta--> Potestad
- hechos: umbrales []; menciones []; omisiones []; condicion_de []; limita []

**NUEVO** — error: None

- Operacion «Solicitud de registro de cheque de pago diferido»: El titular de una cuenta corriente donde se usan cheques de pago diferido o el tenedor de uno de ellos pueden requerir directamente el registro de un cheque de pago diferido mediante la presentación de una solicitud, recibiendo en caso de n… ‖ tramo (exacta): «requerir en forma directa, mediante la integración de la pertinente solicitud, el registro de un cheque de esas características librado por aquél»
- Potestad «Facultad de solicitar registro — titular de cuenta corriente»: El titular de una cuenta corriente donde se utilizan cheques de pago diferido o el tenedor pueden requerir indistintamente el registro de un cheque de pago diferido en forma directa mediante solicitud. ‖ tramo (exacta): «El titular de una cuenta corriente en la que se utilicen cheques de pago diferido o el tenedor de uno de ellos podrán –indistintamente– requerir en forma direct…»
- Operacion «Emisión de cartular o certificado nominativo transferible»: En caso de no existir objeciones del girado, se emite el cartular o, cuando se otorgue aval, el certificado nominativo transferible a nombre del solicitante. ‖ tramo (exacta): «recibiendo, en caso de no existir objeciones por parte del girado, el cartular o, cuando se otorgue el aval, el certificado nominativo transferible extendido a …»
  - Operacion:Solicitud de registro de cheque de pago diferido --establecida_en--> TextoOrdenado:Cuentas de corresponsalía
  - Potestad:Facultad de solicitar registro — titular de cuenta corriente --establecida_en--> TextoOrdenado:Cuentas de corresponsalía
  - Operacion:Emisión de cartular o certificado nominativo transferible --establecida_en--> TextoOrdenado:Cuentas de corresponsalía
  - Potestad:Facultad de solicitar registro — titular de cuenta corriente --aplica_a--> El titular de una cuenta corriente en la que se utilicen cheques de pago diferido
  - Potestad:Facultad de solicitar registro — titular de cuenta corriente --aplica_a--> el tenedor de uno de ellos
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "El titular de una cuenta corriente en la que se utilicen cheques de pago diferid…", "verificada": "exacta", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "el tenedor de uno de ellos", "verificada": "exacta", "sujeto_id": null}]; omisiones [{"categoria": "meta_normativo", "tramo": "recibiendo, en caso de no existir objeciones por parte del girado", "verificacion": "exacta", "nota": "Cláusula que describe el efecto condicional de la ausencia de objeciones, no prescribe conducta prop…"}]; condicion_de []; limita []

*Cuantías en el texto propio: 0.*

## Ficha 59 — `ext::3.3.3.1`

**Texto propio:**

```
3.3.3.1. se trate de operaciones propias de las entidades financieras locales.
```
**Último bloque heredado:** La entidad deberá verificar el cumplimiento de la totalidad de los restantes requisitos normativos aplicables a la operación previamente a realizar el pedido al BCRA. Por hasta el monto de los intereses compensatorios sujetos a conformidad previa los clientes podrán suscribir Bonos para la Reconstru…

**SELLADO** — error: None

- Excepcion «Operaciones propias entidades financieras locales»: se trate de operaciones propias de las entidades financieras locales
- Restriccion «Conformidad previa BCRA — pago intereses deuda importación»: Se requerirá la conformidad previa del BCRA cuando el acreedor sea una contraparte vinculada al deudor y el vencimiento de los intereses a pagar haya tenido lugar hasta el 04/07/24
  - Excepcion:Operaciones propias entidades financieras locales --establecida_en--> TextoOrdenado:Texto Ordenado Exterior - Cambios
  - Restriccion:Conformidad previa BCRA — pago intereses deuda importación --establecida_en--> TextoOrdenado:Texto Ordenado Exterior - Cambios
  - Restriccion:Conformidad previa BCRA — pago intereses deuda importación --aplica_a--> None
  - rechazo: firma_invalida: relations[2]: Excepcion --exceptua_obligacion--> Restriccion
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}]; omisiones []; condicion_de []; limita []

**NUEVO** — error: None

- Excepcion «Excepción operaciones entidades financieras locales»: Excepción al requisito de conformidad previa del BCRA cuando se trata de operaciones propias de entidades financieras locales ‖ tramo (exacta): «se trate de operaciones propias de las entidades financieras locales»
  - Excepcion:Excepción operaciones entidades financieras locales --aplica_a--> entidades financieras locales
  - rechazo: type_invalido: entities[0]: 'None'
  - rechazo: ref_colgante: relations[0] (establecida_en): source='e1' target='to'
  - rechazo: ref_colgante: relations[1] (exceptua): source='e1' target='r1_implícita'
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "entidades financieras locales", "verificada": "exacta", "sujeto_id": null}]; omisiones [{"categoria": "fuera_de_tipos", "tramo": "", "verificacion": "ausente", "nota": "label: 'Texto Ordenado Exterior y Cambios'; tipo propuesto: None"}, {"categoria": "relacion_sin_predicado", "tramo": "se trate de operaciones propias de las entidades financieras locales", "verificacion": "exacta", "nota": "La Excepción debería conectarse a la Restricción de conformidad previa ('se requerirá conformidad pr…"}]; condicion_de []; limita []

*Cuantías en el texto propio: 0.*

## Ficha 60 — `cap::5.1.1`

**Texto propio:**

```
5.1.1. Activos admitidos como garantía (protección desembolsada).
La aplicación de la técnica –que se detalla en el punto 5.3.– requerirá emplear el método
simple (punto 5.3.1.) o el método integral o de reducción de la exposición (punto 5.3.2.),
y estará sujeta al cumplimiento de los requisitos establecidos en los puntos 5.2.1. y
5.2.2.
Las entidades deberán optar por un único método para la aplicación de la técnica de ac-
tivos admitidos como garantía de las operaciones registradas en la cartera de inversión
y para el cálculo de la exposición a las SFT, y sólo podrán cambiar el método empleado
con un preaviso de 6 meses a la SEFYC.
Los activos admitidos como garantía serán aquellos listados en los puntos 5.3.1.2. o
5.3.2.2. –según se emplee el método simple o integral, respectivamente– entregados
por la contraparte o por un tercero en favor de la contraparte.
El descalce de plazos de vencimiento entre la exposición y el activo admitido como ga-
rantía no se permitirá bajo la aplicación del método simple, mientras que para la aplica-
ción del método integral el valor de la cobertura deberá ajustarse conforme a lo estable-
cido en el punto 5.4.5.
El descalce de monedas que se origina cuando la exposición y el activo recibido en ga-
rantía se encuentran denominados en distintas monedas se admitirá al emplear tanto el
método simple –en este caso, sin requerirse la utilización de tratamiento alguno–, como
el método integral. En este último caso, el importe del activo deberá ajustarse mediante
la aplicación de un aforo (H ) para considerar las posibles fluctuaciones futuras en los
fx
tipos de cambio (conforme a lo previsto en el punto 5.3.2.1.).
```
**Último bloque heredado:** 5.1. Técnicas de cobertura del riesgo de crédito.

**SELLADO** — error: None

- Operacion «Aplicación de técnica activos como garantía»: La aplicación de la técnica de activos admitidos como garantía de las operaciones registradas en la cartera de inversión y para el cálculo de la exposición a las SFT, mediante el método simple o el método integral de reducción de la exposic…
- Obligacion «Optar por un único método de aplicación»: Las entidades deberán optar por un único método para la aplicación de la técnica de activos admitidos como garantía de las operaciones registradas en la cartera de inversión y para el cálculo de la exposición a las SFT.
- Potestad «Cambio de método — con preaviso 6 meses»: Las entidades podrán cambiar el método empleado con un preaviso de 6 meses a la SEFYC.
- Definicion «Activos admitidos como garantía»: Aquellos activos listados en los puntos 5.3.1.2. o 5.3.2.2. —según se emplee el método simple o integral, respectivamente— entregados por la contraparte o por un tercero en favor de la contraparte.
- Restriccion «Descalce de plazos — prohibido método simple»: El descalce de plazos de vencimiento entre la exposición y el activo admitido como garantía no se permitirá bajo la aplicación del método simple.
- Restriccion «Descalce de plazos — ajuste método integral»: Para la aplicación del método integral el valor de la cobertura deberá ajustarse conforme a lo establecido en el punto 5.4.5.
- Potestad «Admisión descalce de monedas — método simple»: El descalce de monedas entre la exposición y el activo recibido en garantía se admitirá al emplear el método simple, sin requerirse tratamiento alguno.
- Potestad «Admisión descalce de monedas — método integral»: El descalce de monedas se admitirá al emplear el método integral, debiendo ajustarse el importe del activo mediante la aplicación de un aforo (H_fx) para considerar las posibles fluctuaciones futuras en los tipos de cambio, conforme a lo pr…
  - Operacion:Aplicación de técnica activos como garantía --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Obligacion:Optar por un único método de aplicación --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Potestad:Cambio de método — con preaviso 6 meses --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Definicion:Activos admitidos como garantía --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Restriccion:Descalce de plazos — prohibido método simple --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Restriccion:Descalce de plazos — ajuste método integral --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Potestad:Admisión descalce de monedas — método simple --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Potestad:Admisión descalce de monedas — método integral --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Obligacion:Optar por un único método de aplicación --aplica_a--> None
  - Potestad:Cambio de método — con preaviso 6 meses --aplica_a--> None
  - Restriccion:Descalce de plazos — prohibido método simple --aplica_a--> None
  - Restriccion:Descalce de plazos — ajuste método integral --aplica_a--> None
  - Potestad:Admisión descalce de monedas — método simple --aplica_a--> None
  - Potestad:Admisión descalce de monedas — método integral --aplica_a--> None
  - Restriccion:Descalce de plazos — prohibido método simple --prohibe--> Operacion:Aplicación de técnica activos como garantía
  - Restriccion:Descalce de plazos — ajuste método integral --limita--> Operacion:Aplicación de técnica activos como garantía
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}]; omisiones []; condicion_de []; limita [{"de": "Restriccion:Descalce de plazos — ajuste método integral", "a": "Operacion:Aplicación de técnica activos como garantía"}]

**NUEVO** — error: None

- Operacion «Aplicación de técnica de activos admitidos como garantía»: Técnica de activos admitidos como garantía que requiere emplear el método simple o el método integral/de reducción de la exposición para operaciones registradas en la cartera de inversión y para cálculo de exposición a SFT. Está sujeta al c… ‖ tramo (exacta): «La aplicación de la técnica –que se detalla en el punto 5.3.– requerirá emplear el método simple (punto 5.3.1.) o el método integral o de reducción de la exposi…»
- Obligacion «Optar por único método — cobertura del riesgo de crédito»: Las entidades deberán optar por un único método (simple o integral) para la aplicación de la técnica de activos admitidos como garantía de las operaciones registradas en la cartera de inversión y para el cálculo de la exposición a las opera… ‖ tramo (exacta): «Las entidades deberán optar por un único método para la aplicación de la técnica de activos admitidos como garantía de las operaciones registradas en la cartera…»
- Restriccion «Cambio de método — preaviso 6 meses»: Las entidades solo podrán cambiar el método empleado con un preaviso de 6 meses a la SEFYC. ‖ tramo (exacta): «sólo podrán cambiar el método empleado con un preaviso de 6 meses a la SEFYC»
- Definicion «Activos admitidos como garantía»: Son aquellos listados en los puntos 5.3.1.2. o 5.3.2.2. (según se emplee el método simple o integral, respectivamente), entregados por la contraparte o por un tercero en favor de la contraparte. ‖ tramo (exacta): «Los activos admitidos como garantía serán aquellos listados en los puntos 5.3.1.2. o 5.3.2.2. –según se emplee el método simple o integral, respectivamente– ent…»
- Restriccion «Descalce de plazos — prohibición en método simple»: El descalce de plazos de vencimiento entre la exposición y el activo admitido como garantía no se permitirá bajo la aplicación del método simple. ‖ tramo (exacta): «El descalce de plazos de vencimiento entre la exposición y el activo admitido como garantía no se permitirá bajo la aplicación del método simple»
- Obligacion «Ajuste de cobertura conforme punto 5.4.5 — método integral»: Para la aplicación del método integral, el valor de la cobertura deberá ajustarse conforme a lo establecido en el punto 5.4.5. ‖ tramo (exacta): «para la aplicación del método integral el valor de la cobertura deberá ajustarse conforme a lo establecido en el punto 5.4.5»
- Excepcion «Descalce de monedas admitido — método simple sin tratamiento»: Se admite el descalce de monedas cuando la exposición y el activo recibido en garantía se encuentran denominados en distintas monedas, tanto en el método simple (sin requerirse tratamiento alguno) como en el método integral. ‖ tramo (exacta): «El descalce de monedas que se origina cuando la exposición y el activo recibido en garantía se encuentran denominados en distintas monedas se admitirá al emplea…»
- Obligacion «Ajuste mediante aforo — descalce de monedas en método integral»: En el método integral, el importe del activo deberá ajustarse mediante la aplicación de un aforo (H fx) para considerar las posibles fluctuaciones futuras en los tipos de cambio (conforme a lo previsto en el punto 5.3.2.1.). ‖ tramo (no): «En este último caso, el importe del activo deberá ajustarse mediante la aplicación de un aforo (H fx) para considerar las posibles fluctuaciones futuras en los …»
  - Operacion:Aplicación de técnica de activos admitidos como garantía --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Obligacion:Optar por único método — cobertura del riesgo de crédito --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Restriccion:Cambio de método — preaviso 6 meses --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Definicion:Activos admitidos como garantía --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Restriccion:Descalce de plazos — prohibición en método simple --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Obligacion:Ajuste de cobertura conforme punto 5.4.5 — método integral --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Excepcion:Descalce de monedas admitido — método simple sin tratamiento --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Obligacion:Ajuste mediante aforo — descalce de monedas en método integr… --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Obligacion:Optar por único método — cobertura del riesgo de crédito --aplica_a--> Las entidades
  - Restriccion:Cambio de método — preaviso 6 meses --aplica_a--> Las entidades
- hechos: umbrales [{"entidad": "Restriccion:Cambio de método — preaviso 6 meses", "tramo": "preaviso de 6 meses", "verificacion": "exacta"}]; menciones [{"pred": "aplica_a", "mencion": "Las entidades", "verificada": "exacta", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "Las entidades", "verificada": "exacta", "sujeto_id": null}]; omisiones [{"categoria": "fuera_de_tipos", "tramo": "estará sujeta al cumplimiento de los requisitos establecidos en los puntos 5.2.1. y 5.2.2", "verificacion": "exacta", "nota": "Condición o remisión a otros puntos para requisitos previos; la remisión estructural (la necesidad d…"}]; condicion_de []; limita []

*Cuantías en el texto propio: 1.*

## Ficha 61 — `ext::3.5.6.1`

**Texto propio:**

```
3.5.6.1. se trate de operaciones propias de las entidades financieras locales.
```
**Último bloque heredado:** Las deudas comprendidas en este punto continuarán sujetas a la conformidad previa aun cuando existiese una modificación del acreedor o del deudor que conlleve a que ya no exista una vinculación entre el acreedor y el deudor residente.

**SELLADO** — error: None

- Excepcion «Operaciones propias de EF locales»: se trate de operaciones propias de las entidades financieras locales
- Restriccion «Conformidad previa BCRA — vinculación acreedor-deudor»: Se requerirá la conformidad previa del BCRA para el acceso al mercado de cambios para la cancelación de capital e intereses de endeudamientos financieros comprendidos en este punto 3.5. cuando el acreedor sea una contraparte vinculada al de…
  - Restriccion:Conformidad previa BCRA — vinculación acreedor-deudor --establecida_en--> TextoOrdenado:Exterior — Cambios
  - Restriccion:Conformidad previa BCRA — vinculación acreedor-deudor --aplica_a--> None
  - rechazo: firma_invalida: relations[1]: Excepcion --exceptua_obligacion--> Restriccion
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}]; omisiones []; condicion_de []; limita []

**NUEVO** — error: None

- Excepcion «Excepción — operaciones propias de entidades financieras locales»: No aplica el requisito de conformidad previa del BCRA cuando se trate de operaciones propias de las entidades financieras locales ‖ tramo (exacta): «se trate de operaciones propias de las entidades financieras locales»
  - Excepcion:Excepción — operaciones propias de entidades financieras loc… --establecida_en--> TextoOrdenado:Normas de Operaciones en Exterior y Cambios
  - rechazo: ref_colgante: relations[1] (exceptua_obligacion): source='e1' target='e2'
- hechos: umbrales []; menciones []; omisiones [{"categoria": "relacion_sin_predicado", "tramo": "se trate de operaciones propias de las entidades financieras locales", "verificacion": "exacta", "nota": "El texto no especifica explícitamente cuál es la Obligación concreta que esta salvedad exceptúa (aun…"}]; condicion_de []; limita []

*Cuantías en el texto propio: 0.*

## Ficha 62 — `cap::4.2.1::intro`

**Texto propio:**

```
La exposición al riesgo de crédito de contraparte (EAD) se calculará por separado para
cada conjunto de neteo (“netting set”, NS) y se determinará del siguiente modo:
donde:
α = 1,40.
CR: costo de reposición calculado de acuerdo con el punto 4.2.1.1.
EPF: exposición potencial futura calculado de acuerdo con el punto 4.2.1.2.
El cálculo del CR y de la EPF diferirá según que los conjuntos de neteo estén sujetos o
no al intercambio de márgenes de variación:
− Operaciones sin margen de variación: el CR representa la pérdida que ocurriría
ante el incumplimiento de la contraparte y la liquidación inmediata de sus opera-
ciones y la EPF adicionará el incremento probable de la exposición, calculado de
modo conservador, en el horizonte temporal de un año a partir de la fecha de
cálculo.
− Operaciones con margen de variación: el CR representa la pérdida que ocurriría
ante el incumplimiento de la contraparte –en el presente o en el futuro– si la liqui-
dación y reposición de las operaciones fueran instantáneas. Dado que puede ha-
ber un lapso –período de riesgo de margen (“MPOR”)– entre el último intercambio
de garantías antes del incumplimiento y la reposición, el adicional por la EPF re-
presenta el potencial cambio de valor de las operaciones durante ese período.
En ambos casos, y a los efectos de determinar el costo de reposición, el aforo de los
activos recibidos en garantía (excepto efectivo) representará el cambio potencial del
valor de dicha garantía durante el período relevante –un año, para las operaciones sin
márgenes, y el período de riesgo de margen, para las operaciones con márgenes–.
Además:
− La EAD para un conjunto de neteo con márgenes de variación tendrá como límite
superior la EAD que resultaría para el mismo conjunto si no los tuviera.
− La EAD de un conjunto de neteo que sólo comprende opciones vendidas podrá
ser cero cuando hayan sido cobradas todas las primas y en tanto dichas opciones
no estén comprendidas en acuerdos de neteo que incluyan otros productos o la
constitución de márgenes.
```
**Último bloque heredado:** 4.2.1. Exposición al riesgo de crédito de contraparte.

**SELLADO** — error: None

- Operacion «Cálculo EAD por netting set»: La exposición al riesgo de crédito de contraparte (EAD) se calculará por separado para cada conjunto de neteo (netting set, NS) y se determinará mediante la fórmula: EAD = (CR + EPF) × α, donde α = 1,40; CR es el costo de reposición y EPF e…
- Operacion «Cálculo CR — operaciones sin margen variación»: En operaciones sin margen de variación, el CR representa la pérdida que ocurriría ante el incumplimiento de la contraparte y la liquidación inmediata de sus operaciones.
- Operacion «Cálculo EPF — operaciones sin margen variación»: En operaciones sin margen de variación, la EPF adicionará el incremento probable de la exposición, calculado de modo conservador, en el horizonte temporal de un año a partir de la fecha de cálculo.
- Operacion «Cálculo CR — operaciones con margen variación»: En operaciones con margen de variación, el CR representa la pérdida que ocurriría ante el incumplimiento de la contraparte (en el presente o en el futuro) si la liquidación y reposición de las operaciones fueran instantáneas.
- Operacion «Cálculo EPF — operaciones con margen variación»: En operaciones con margen de variación, el adicional por la EPF representa el potencial cambio de valor de las operaciones durante el período de riesgo de margen (MPOR) entre el último intercambio de garantías antes del incumplimiento y la …
- Operacion «Aforo de activos recibidos en garantía»: A efectos de determinar el costo de reposición, el aforo de los activos recibidos en garantía (excepto efectivo) representará el cambio potencial del valor de dicha garantía durante el período relevante: un año para operaciones sin márgenes…
- Restriccion «EAD con márgenes — límite superior»: La EAD para un conjunto de neteo con márgenes de variación tendrá como límite superior la EAD que resultaría para el mismo conjunto si no los tuviera.
- Excepcion «EAD nulo — opciones vendidas»: La EAD de un conjunto de neteo que sólo comprende opciones vendidas podrá ser cero cuando hayan sido cobradas todas las primas y en tanto dichas opciones no estén comprendidas en acuerdos de neteo que incluyan otros productos o la constituc…
- Definicion «EAD — Exposición al riesgo de crédito de contraparte»: Se calcula por separado para cada conjunto de neteo (netting set, NS) mediante la fórmula: EAD = (CR + EPF) × α, donde CR es el costo de reposición, EPF es la exposición potencial futura, y α = 1,40.
- Definicion «CR — Costo de reposición»: Se calcula de acuerdo con el punto 4.2.1.1. En operaciones sin margen representa la pérdida ante incumplimiento y liquidación inmediata. En operaciones con margen representa la pérdida ante incumplimiento presente o futuro si la liquidación…
- Definicion «EPF — Exposición potencial futura»: Se calcula de acuerdo con el punto 4.2.1.2. En operaciones sin margen adicionará el incremento probable de la exposición en horizonte de un año. En operaciones con margen representa el potencial cambio de valor durante el período de riesgo …
- Definicion «NS — Conjunto de neteo»: Unidad sobre la cual se calcula por separado la exposición al riesgo de crédito de contraparte (EAD).
- Definicion «MPOR — Período de riesgo de margen»: Lapso entre el último intercambio de garantías antes del incumplimiento de la contraparte y la reposición de las operaciones.
  - Operacion:Cálculo EAD por netting set --establecida_en--> TextoOrdenado:Capital Mínimo
  - Operacion:Cálculo CR — operaciones sin margen variación --establecida_en--> TextoOrdenado:Capital Mínimo
  - Operacion:Cálculo EPF — operaciones sin margen variación --establecida_en--> TextoOrdenado:Capital Mínimo
  - Operacion:Cálculo CR — operaciones con margen variación --establecida_en--> TextoOrdenado:Capital Mínimo
  - Operacion:Cálculo EPF — operaciones con margen variación --establecida_en--> TextoOrdenado:Capital Mínimo
  - Operacion:Aforo de activos recibidos en garantía --establecida_en--> TextoOrdenado:Capital Mínimo
  - Restriccion:EAD con márgenes — límite superior --establecida_en--> TextoOrdenado:Capital Mínimo
  - Excepcion:EAD nulo — opciones vendidas --establecida_en--> TextoOrdenado:Capital Mínimo
  - Definicion:EAD — Exposición al riesgo de crédito de contraparte --establecida_en--> TextoOrdenado:Capital Mínimo
  - Definicion:CR — Costo de reposición --establecida_en--> TextoOrdenado:Capital Mínimo
  - Definicion:EPF — Exposición potencial futura --establecida_en--> TextoOrdenado:Capital Mínimo
  - Definicion:NS — Conjunto de neteo --establecida_en--> TextoOrdenado:Capital Mínimo
  - Definicion:MPOR — Período de riesgo de margen --establecida_en--> TextoOrdenado:Capital Mínimo
  - Restriccion:EAD con márgenes — límite superior --limita--> Operacion:Cálculo EAD por netting set
  - rechazo: firma_invalida: relations[14]: Excepcion --exceptua_obligacion--> Operacion
- hechos: umbrales []; menciones []; omisiones [{"categoria": null, "tramo": "", "verificacion": "ausente", "nota": "Fórmula EAD = (CR + EPF) × α: estructura y parámetros detallados no extraídos (contenido tabular/fór…"}, {"categoria": null, "tramo": "", "verificacion": "ausente", "nota": "Métodos específicos de cálculo de CR según punto 4.2.1.1 y EPF según punto 4.2.1.2: referencias inte…"}]; condicion_de []; limita [{"de": "Restriccion:EAD con márgenes — límite superior", "a": "Operacion:Cálculo EAD por netting set"}]

**NUEVO** — error: None

- Operacion «Cálculo de EAD por conjunto de neteo»: Cálculo de la exposición al riesgo de crédito de contraparte (EAD) por separado para cada conjunto de neteo, determinada según la fórmula con componentes CR y EPF, cuyas características varían según si los conjuntos están sujetos al interca… ‖ tramo (exacta): «La exposición al riesgo de crédito de contraparte (EAD) se calculará por separado para cada conjunto de neteo ("netting set", NS) y se determinará del siguiente…»
- Operacion «CR — costo de reposición»: Componente de cálculo del EAD que representa la pérdida ante incumplimiento de la contraparte. En operaciones sin margen de variación, es la pérdida por liquidación inmediata. En operaciones con margen de variación, es la pérdida si liquida… ‖ tramo (exacta): «CR: costo de reposición calculado de acuerdo con el punto 4.2.1.1.»
- Operacion «EPF — exposición potencial futura»: Componente de cálculo del EAD que representa el incremento probable de exposición. En operaciones sin margen de variación, se calcula en horizonte de un año. En operaciones con margen de variación, representa el cambio potencial durante el … ‖ tramo (exacta): «EPF: exposición potencial futura calculado de acuerdo con el punto 4.2.1.2.»
- Condicion «Operaciones sin margen de variación»: Supuesto en que los conjuntos de neteo no están sujetos al intercambio de márgenes de variación, caracterizado por liquidación inmediata y horizonte temporal de cálculo de un año. ‖ tramo (exacta): «Operaciones sin margen de variación: el CR representa la pérdida que ocurriría ante el incumplimiento de la contraparte y la liquidación inmediata de sus operac…»
- Condicion «Operaciones con margen de variación»: Supuesto en que los conjuntos de neteo están sujetos al intercambio de márgenes de variación, caracterizado por un período de riesgo de margen (MPOR) entre último intercambio de garantías y reposición. ‖ tramo (exacta): «Operaciones con margen de variación: el CR representa la pérdida que ocurriría ante el incumplimiento de la contraparte –en el presente o en el futuro– si la li…»
- Obligacion «Aforo de activos en garantía — período relevante»: Requisito de que el aforo de activos recibidos en garantía (excepto efectivo) debe representar el cambio potencial del valor de la garantía durante el período relevante: un año para operaciones sin márgenes, o el período de riesgo de margen… ‖ tramo (exacta): «el aforo de los activos recibidos en garantía (excepto efectivo) representará el cambio potencial del valor de dicha garantía durante el período relevante –un a…»
- Restriccion «Límite superior EAD con márgenes de variación»: Límite de la EAD para conjuntos de neteo con márgenes de variación, cuyo valor máximo es la EAD que resultaría sin márgenes. ‖ tramo (exacta): «La EAD para un conjunto de neteo con márgenes de variación tendrá como límite superior la EAD que resultaría para el mismo conjunto si no los tuviera.»
- Excepcion «EAD cero — opciones vendidas sin margen»: Excepción que permite EAD cero para conjuntos que solo incluyen opciones vendidas cuando todas las primas han sido cobradas y las opciones no integran acuerdos de neteo con otros productos ni tienen márgenes constituidos. ‖ tramo (exacta): «La EAD de un conjunto de neteo que sólo comprende opciones vendidas podrá ser cero cuando hayan sido cobradas todas las primas y en tanto dichas opciones no est…»
  - Operacion:Cálculo de EAD por conjunto de neteo --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Operacion:CR — costo de reposición --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Operacion:EPF — exposición potencial futura --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Condicion:Operaciones sin margen de variación --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Condicion:Operaciones con margen de variación --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Obligacion:Aforo de activos en garantía — período relevante --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Restriccion:Límite superior EAD con márgenes de variación --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Excepcion:EAD cero — opciones vendidas sin margen --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Obligacion:Aforo de activos en garantía — período relevante --aplica_a--> las entidades
  - Restriccion:Límite superior EAD con márgenes de variación --limita--> Operacion:Cálculo de EAD por conjunto de neteo
  - Excepcion:EAD cero — opciones vendidas sin margen --exceptua--> Restriccion:Límite superior EAD con márgenes de variación
- hechos: umbrales [{"entidad": "Condicion:Operaciones sin margen de variación", "tramo": "en el horizonte temporal de un año a partir de la fecha de cálculo", "verificacion": "exacta"}, {"entidad": "Obligacion:Aforo de activos en garantía — período relevante", "tramo": "un año, para las operaciones sin márgenes", "verificacion": "exacta"}, {"entidad": "Obligacion:Aforo de activos en garantía — período relevante", "tramo": "el período de riesgo de margen, para las operaciones con márgenes", "verificacion": "exacta"}]; menciones [{"pred": "aplica_a", "mencion": "las entidades", "verificada": "no", "sujeto_id": null}]; omisiones [{"categoria": "formula", "tramo": "donde: α = 1,40.", "verificacion": "exacta", "nota": "Fórmula con parámetro no confiable — contenido extraído del PDF con destrucción de estructura. El pa…"}]; condicion_de []; limita [{"de": "Restriccion:Límite superior EAD con márgenes de variación", "a": "Operacion:Cálculo de EAD por conjunto de neteo"}]

*Cuantías en el texto propio: 2.*

## Ficha 63 — `ayccef::2.4.8.1`

**Texto propio:**

```
2.4.8.1. Antecedentes sobre la responsabilidad, la idoneidad y experiencia en la
actividad financiera.
```
**Último bloque heredado:** La información y documentación prevista en los puntos 2.4.8.1. a 2.4.8.3. y 2.4.8.5. se presentará conforme a lo indicado en el punto 6.2.

**SELLADO** — error: None

- Obligacion «Presentación de antecedentes sobre responsabilidad e idoneidad»: Presentar antecedentes sobre la responsabilidad, la idoneidad y experiencia en la actividad financiera de accionistas e integrantes de órganos de gobierno, administración y fiscalización
  - Obligacion:Presentación de antecedentes sobre responsabilidad e idoneid… --establecida_en--> TextoOrdenado:Autorización de nuevas entidades financieras (AYCCEF)
  - Obligacion:Presentación de antecedentes sobre responsabilidad e idoneid… --aplica_a--> None
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}]; omisiones []; condicion_de []; limita []

**NUEVO** — error: None

- Obligacion «Presentación de antecedentes sobre responsabilidad e idoneidad»: Presentación de antecedentes sobre la responsabilidad, la idoneidad y experiencia en la actividad financiera de cada uno de los accionistas e integrantes de los órganos de gobierno, de administración y de fiscalización de la entidad ‖ tramo (exacta): «Antecedentes sobre la responsabilidad, la idoneidad y experiencia en la actividad financiera»
  - Obligacion:Presentación de antecedentes sobre responsabilidad e idoneid… --establecida_en--> TextoOrdenado:Autorización y control entidades financieras
  - Obligacion:Presentación de antecedentes sobre responsabilidad e idoneid… --aplica_a--> futuros fundadores
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "futuros fundadores", "verificada": "exacta", "sujeto_id": null}]; omisiones [{"categoria": "meta_normativo", "tramo": "2.4.8.1. Antecedentes sobre la responsabilidad, la idoneidad y experiencia en la actividad financier…", "verificacion": "exacta", "nota": "Encabezado que anuncia el contenido; el texto del punto no contiene prescripción sino solo la enumer…"}]; condicion_de []; limita []

*Cuantías en el texto propio: 0.*

## Ficha 64 — `ctacte::5.1.2.2`

**Texto propio:**

```
5.1.2.2. A favor de fiduciarios de fideicomisos financieros comprendidos en la Ley de En-
tidades Financieras, en la medida en que se trate de operaciones relativas al fi-
deicomiso.
```
**Último bloque heredado:** En los casos de cheques librados al portador o a favor de una persona determinada –que posean o no la cláusula “no a la orden”– y que sean entregados por su beneficia- rio a un tercero para la gestión de cobro mediante su presentación en ventanilla o a tra- vés de su depósito en cuenta para su compe…

**SELLADO** — error: None

- Operacion «Endoso a fiduciarios de fideicomisos financieros»: Endoso de cheque a favor de fiduciarios de fideicomisos financieros comprendidos en la Ley de Entidades Financieras, en operaciones relativas al fideicomiso
- Condicion «Operaciones relativas al fideicomiso»: en la medida en que se trate de operaciones relativas al fideicomiso
  - Operacion:Endoso a fiduciarios de fideicomisos financieros --establecida_en--> TextoOrdenado:Cuentas a la vista
  - Operacion:Endoso a fiduciarios de fideicomisos financieros --aplica_a--> None
  - Condicion:Operaciones relativas al fideicomiso --condicion_de--> Operacion:Endoso a fiduciarios de fideicomisos financieros
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}]; omisiones []; condicion_de [{"de": "Condicion:Operaciones relativas al fideicomiso", "a": "Operacion:Endoso a fiduciarios de fideicomisos financieros", "firma_nueva": true}]; limita []

**NUEVO** — error: None

- Operacion «Transmisión de cheque por endoso»: Transmisión de cheques extendidos a favor de fiduciarios de fideicomisos financieros comprendidos en la Ley de Entidades Financieras, en la medida en que se trate de operaciones relativas al fideicomiso. ‖ tramo (no): «cheques a favor de fiduciarios de fideicomisos financieros»
- Condicion «Operación relativa al fideicomiso»: La transmisión por endoso aplica cuando se trata de operaciones relativas al fideicomiso, no para otras operaciones del fiduciario. ‖ tramo (exacta): «en la medida en que se trate de operaciones relativas al fideicomiso»
  - Operacion:Transmisión de cheque por endoso --establecida_en--> TextoOrdenado:Texto Ordenado Cuentas de Corresponsalía
  - Condicion:Operación relativa al fideicomiso --establecida_en--> TextoOrdenado:Texto Ordenado Cuentas de Corresponsalía
  - Condicion:Operación relativa al fideicomiso --condicion_de--> Operacion:Transmisión de cheque por endoso
  - Operacion:Transmisión de cheque por endoso --aplica_a--> fiduciarios de fideicomisos financieros comprendidos en la Ley de Entidades Financieras
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "fiduciarios de fideicomisos financieros comprendidos en la Ley de Entidades Fina…", "verificada": "exacta", "sujeto_id": null}]; omisiones [{"categoria": "meta_normativo", "tramo": "A favor de fiduciarios de fideicomisos financieros comprendidos en la Ley de Entidades Financieras", "verificacion": "exacta", "nota": "Especificación de alcance del punto que actúa como delimitador de destinatarios de la norma compuest…"}]; condicion_de [{"de": "Condicion:Operación relativa al fideicomiso", "a": "Operacion:Transmisión de cheque por endoso", "firma_nueva": true}]; limita []

*Cuantías en el texto propio: 0.*

## Ficha 65 — `cap::6.2.2.6`

**Texto propio:**

```
6.2.2.6. Como resultado de lo previsto en el punto 6.2.2.5. se obtendrá un conjunto de
posiciones netas compradas, un conjunto de posiciones netas vendidas y las
desestimaciones verticales. Luego, las entidades podrán realizar dos series de
compensaciones horizontales: primero, entre las posiciones netas dentro de
cada una de las tres zonas en las que se agrupan las bandas temporales y,
luego, entre las posiciones netas de las tres zonas. Dichas compensaciones
estarán sujetas a la siguiente escala de desestimaciones horizontales
-exigencias adicionales- expresadas como porcentajes de las posiciones que
se compensan:
[TABLA cap::tabla037 | página 125 | e0_tablas | posicional]
Fila 1: col1 = Zona | col2 = Banda | col3 = Porcentaje de desestimación aplicable: ⟨abarca hasta col5⟩
Fila 2: col3 = dentro de zona | col4 = entre zonas adyacentes | col5 = entre zonas 1 y 3
Fila 3: col2 = Meses*
Fila 4: col1 = 1 | col2 = 0-1 | col3 = 40%
Fila 5: col1 = 1 ⟨combinada con fila 4⟩ | col2 = 1-3 | col3 = 40% ⟨combinada con fila 4⟩
Fila 6: col1 = 1 ⟨combinada con fila 4⟩ | col2 = 3-6 | col3 = 40% ⟨combinada con fila 4⟩
Fila 7: col1 = 1 ⟨combinada con fila 4⟩ | col2 = 6-12 | col3 = 40% ⟨combinada con fila 4⟩
Fila 8: col1 = Años* ⟨abarca hasta col3⟩ | col4 = 40%
Fila 9: col1 = 2 | col2 = 1-2 | col3 = 30%
Fila 10: col1 = 2 ⟨combinada con fila 9⟩ | col2 = 2-3 | col3 = 30% ⟨combinada con fila 9⟩ | col5 = 100%
Fila 11: col1 = 2 ⟨combinada con fila 9⟩ | col2 = 3-4 | col3 = 30% ⟨combinada con fila 9⟩
Fila 12: col1 = Años* ⟨abarca hasta col3⟩ | col4 = 40%
Fila 13: col1 = 3 | col2 = 4-5 | col3 = 30%
Fila 14: col1 = 3 ⟨combinada con fila 13⟩ | col2 = 5-7 | col3 = 30% ⟨combinada con fila 13⟩
Fila 15: col1 = 3 ⟨combinada con fila 13⟩ | col2 = 7-10 | col3 = 30% ⟨combinada con fila 13⟩
Fila 16: col1 = 3 ⟨combinada con fila 13⟩ | col2 = 10-15 | col3 = 30% ⟨combinada con fila 13⟩
Fila 17: col1 = 3 ⟨combinada con fila 13⟩ | col2 = 15-20 | col3 = 30% ⟨combinada con fila 13⟩
Fila 18: col2 = Más de 20
[FIN TABLA cap::tabla037]
ei se puede simplificar menciones a “meses” y “años”ese
*
Al efecto de imputar una posición a la escala de vencimientos cuando el plazo residual o el plazo que
resta hasta el siguiente ajuste del interés, según el caso, es igual al límite entre dos bandas, correspon-
derá realizar la imputación a la banda temporal más próxima a la fecha de cálculo.
```
**Último bloque heredado:** 6.2.2. Exigencia de capital por riesgo general de mercado: método de los plazos residuales.

**SELLADO** — error: None

- Operacion «Cálculo de exigencias capital riesgo tasa interés»: Como resultado de lo previsto en el punto 6.2.2.5 se obtendrá un conjunto de posiciones netas compradas, un conjunto de posiciones netas vendidas y las desestimaciones verticales.
- Operacion «Compensaciones horizontales posiciones netas»: Las entidades podrán realizar dos series de compensaciones horizontales: primero, entre las posiciones netas dentro de cada una de las tres zonas en las que se agrupan las bandas temporales y, luego, entre las posiciones netas de las tres z…
- Restriccion «Desestimaciones horizontales zona 1 (40%)»: Las compensaciones entre posiciones dentro de la zona 1 (bandas 0-1, 1-3, 3-6, 6-12 meses) están sujetas a desestimación horizontal del 40% de las posiciones que se compensan dentro de la misma zona.
- Restriccion «Desestimaciones horizontales zona 2 (30% intra, 100% inter)»: Las compensaciones en la zona 2 (bandas 1-2, 2-3, 3-4, 4-5, 5-7, 7-10 años) están sujetas a desestimación horizontal del 30% dentro de la zona y del 100% entre zonas adyacentes.
- Restriccion «Desestimaciones horizontales zona 3 (30% intra, 40% zona 1)»: Las compensaciones en la zona 3 (bandas 10-15, 15-20, más de 20 años) están sujetas a desestimación horizontal del 30% dentro de la zona y del 40% entre zonas adyacentes.
- Condicion «Imputación posición con plazo igual a límite de banda»: Cuando el plazo residual o el plazo que resta hasta el siguiente ajuste del interés es igual al límite entre dos bandas, corresponderá realizar la imputación a la banda temporal más próxima a la fecha de cálculo.
- Potestad «Realización de compensaciones horizontales»: Las entidades podrán realizar dos series de compensaciones horizontales: primero, entre las posiciones netas dentro de cada una de las tres zonas y, luego, entre las posiciones netas de las tres zonas.
  - Operacion:Cálculo de exigencias capital riesgo tasa interés --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Operacion:Compensaciones horizontales posiciones netas --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Restriccion:Desestimaciones horizontales zona 1 (40%) --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Restriccion:Desestimaciones horizontales zona 2 (30% intra, 100% inter) --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Restriccion:Desestimaciones horizontales zona 3 (30% intra, 40% zona 1) --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Condicion:Imputación posición con plazo igual a límite de banda --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Potestad:Realización de compensaciones horizontales --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Restriccion:Desestimaciones horizontales zona 1 (40%) --limita--> Operacion:Compensaciones horizontales posiciones netas
  - Restriccion:Desestimaciones horizontales zona 2 (30% intra, 100% inter) --limita--> Operacion:Compensaciones horizontales posiciones netas
  - Restriccion:Desestimaciones horizontales zona 3 (30% intra, 40% zona 1) --limita--> Operacion:Compensaciones horizontales posiciones netas
  - Potestad:Realización de compensaciones horizontales --aplica_a--> None
  - Restriccion:Desestimaciones horizontales zona 1 (40%) --aplica_a--> None
  - Restriccion:Desestimaciones horizontales zona 2 (30% intra, 100% inter) --aplica_a--> None
  - Restriccion:Desestimaciones horizontales zona 3 (30% intra, 40% zona 1) --aplica_a--> None
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}]; omisiones [{"categoria": null, "tramo": "", "verificacion": "ausente", "nota": "Tabla de desestimaciones horizontales: estructura tabular con encabezados de filas (bandas de plazo)…"}]; condicion_de []; limita [{"de": "Restriccion:Desestimaciones horizontales zona 1 (40%)", "a": "Operacion:Compensaciones horizontales posiciones netas"}, {"de": "Restriccion:Desestimaciones horizontales zona 2 (30% intra, 100% inter)", "a": "Operacion:Compensaciones horizontales posiciones netas"}, {"de": "Restriccion:Desestimaciones horizontales zona 3 (30% intra, 40% zona 1)", "a": "Operacion:Compensaciones horizontales posiciones netas"}]

**NUEVO** — error: None

- Operacion «Compensaciones horizontales zonas temporales»: Las entidades podrán realizar dos series de compensaciones horizontales: entre posiciones netas dentro de cada zona y luego entre las posiciones netas de las tres zonas, sujetas a escala de desestimaciones horizontales ‖ tramo (exacta): «compensaciones horizontales: primero, entre las posiciones netas dentro de cada una de las tres zonas en las que se agrupan las bandas temporales y, luego, entr…»
- Restriccion «Desestimación horizontal zona 1, 0-1 meses»: Desestimación horizontal aplicable a compensaciones dentro de zona 1, banda 0-1 meses ‖ tramo (exacta): «40%»
- Restriccion «Desestimación horizontal zona 1, 1-3 meses»: Desestimación horizontal aplicable a compensaciones dentro de zona 1, banda 1-3 meses ‖ tramo (exacta): «40%»
- Restriccion «Desestimación horizontal zona 1, 3-6 meses»: Desestimación horizontal aplicable a compensaciones dentro de zona 1, banda 3-6 meses ‖ tramo (exacta): «40%»
- Restriccion «Desestimación horizontal zona 1, 6-12 meses»: Desestimación horizontal aplicable a compensaciones dentro de zona 1, banda 6-12 meses ‖ tramo (exacta): «40%»
- Restriccion «Desestimación horizontal zona 1 entre zonas adyacentes»: Desestimación horizontal aplicable a compensaciones entre zonas adyacentes desde zona 1 ‖ tramo (exacta): «40%»
- Restriccion «Desestimación horizontal zona 2, 1-2 años»: Desestimación horizontal aplicable a compensaciones dentro de zona 2, banda 1-2 años ‖ tramo (exacta): «30%»
- Restriccion «Desestimación horizontal zona 2, 2-3 años»: Desestimación horizontal aplicable a compensaciones dentro de zona 2, banda 2-3 años ‖ tramo (exacta): «30%»
- Restriccion «Desestimación horizontal zona 2, 2-3 años entre zonas 1 y 3»: Desestimación horizontal aplicable a compensaciones entre zonas 1 y 3 desde banda 2-3 años de zona 2 ‖ tramo (exacta): «100%»
- Restriccion «Desestimación horizontal zona 2, 3-4 años»: Desestimación horizontal aplicable a compensaciones dentro de zona 2, banda 3-4 años ‖ tramo (exacta): «30%»
- Restriccion «Desestimación horizontal zona 2 entre zonas adyacentes»: Desestimación horizontal aplicable a compensaciones entre zonas adyacentes desde zona 2 ‖ tramo (exacta): «40%»
- Restriccion «Desestimación horizontal zona 3, 4-5 años»: Desestimación horizontal aplicable a compensaciones dentro de zona 3, banda 4-5 años ‖ tramo (exacta): «30%»
- Restriccion «Desestimación horizontal zona 3, 5-7 años»: Desestimación horizontal aplicable a compensaciones dentro de zona 3, banda 5-7 años ‖ tramo (exacta): «30%»
- Restriccion «Desestimación horizontal zona 3, 7-10 años»: Desestimación horizontal aplicable a compensaciones dentro de zona 3, banda 7-10 años ‖ tramo (exacta): «30%»
- Restriccion «Desestimación horizontal zona 3, 10-15 años»: Desestimación horizontal aplicable a compensaciones dentro de zona 3, banda 10-15 años ‖ tramo (exacta): «30%»
- Restriccion «Desestimación horizontal zona 3, 15-20 años»: Desestimación horizontal aplicable a compensaciones dentro de zona 3, banda 15-20 años ‖ tramo (exacta): «30%»
- Restriccion «Desestimación horizontal zona 3 entre zonas adyacentes»: Desestimación horizontal aplicable a compensaciones entre zonas adyacentes desde zona 3 ‖ tramo (exacta): «40%»
- Potestad «Potestad de realizar compensaciones horizontales»: Las entidades podrán realizar compensaciones horizontales entre posiciones netas, sujetas a la escala de desestimaciones establecida ‖ tramo (exacta): «las entidades podrán realizar dos series de compensaciones horizontales»
- Condicion «Condición de imputación por plazo residual»: Si el plazo residual o el plazo hasta el siguiente ajuste de interés es igual al límite entre dos bandas, la imputación debe hacerse a la banda más próxima a la fecha de cálculo ‖ tramo (exacta): «cuando el plazo residual o el plazo que resta hasta el siguiente ajuste del interés, según el caso, es igual al límite entre dos bandas, corresponderá realizar …»
  - Operacion:Compensaciones horizontales zonas temporales --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Restriccion:Desestimación horizontal zona 1, 0-1 meses --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Restriccion:Desestimación horizontal zona 1, 1-3 meses --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Restriccion:Desestimación horizontal zona 1, 3-6 meses --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Restriccion:Desestimación horizontal zona 1, 6-12 meses --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Restriccion:Desestimación horizontal zona 1 entre zonas adyacentes --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Restriccion:Desestimación horizontal zona 2, 1-2 años --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Restriccion:Desestimación horizontal zona 2, 2-3 años --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Restriccion:Desestimación horizontal zona 2, 2-3 años entre zonas 1 y 3 --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Restriccion:Desestimación horizontal zona 2, 3-4 años --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Restriccion:Desestimación horizontal zona 2 entre zonas adyacentes --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Restriccion:Desestimación horizontal zona 3, 4-5 años --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Restriccion:Desestimación horizontal zona 3, 5-7 años --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Restriccion:Desestimación horizontal zona 3, 7-10 años --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Restriccion:Desestimación horizontal zona 3, 10-15 años --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Restriccion:Desestimación horizontal zona 3, 15-20 años --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Restriccion:Desestimación horizontal zona 3 entre zonas adyacentes --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Potestad:Potestad de realizar compensaciones horizontales --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Condicion:Condición de imputación por plazo residual --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Potestad:Potestad de realizar compensaciones horizontales --aplica_a--> las entidades
  - Restriccion:Desestimación horizontal zona 1, 0-1 meses --limita--> Operacion:Compensaciones horizontales zonas temporales
  - Restriccion:Desestimación horizontal zona 1, 1-3 meses --limita--> Operacion:Compensaciones horizontales zonas temporales
  - Restriccion:Desestimación horizontal zona 1, 3-6 meses --limita--> Operacion:Compensaciones horizontales zonas temporales
  - Restriccion:Desestimación horizontal zona 1, 6-12 meses --limita--> Operacion:Compensaciones horizontales zonas temporales
  - Restriccion:Desestimación horizontal zona 1 entre zonas adyacentes --limita--> Operacion:Compensaciones horizontales zonas temporales
  - Restriccion:Desestimación horizontal zona 2, 1-2 años --limita--> Operacion:Compensaciones horizontales zonas temporales
  - Restriccion:Desestimación horizontal zona 2, 2-3 años --limita--> Operacion:Compensaciones horizontales zonas temporales
  - Restriccion:Desestimación horizontal zona 2, 2-3 años entre zonas 1 y 3 --limita--> Operacion:Compensaciones horizontales zonas temporales
  - Restriccion:Desestimación horizontal zona 2, 3-4 años --limita--> Operacion:Compensaciones horizontales zonas temporales
  - Restriccion:Desestimación horizontal zona 2 entre zonas adyacentes --limita--> Operacion:Compensaciones horizontales zonas temporales
  - Restriccion:Desestimación horizontal zona 3, 4-5 años --limita--> Operacion:Compensaciones horizontales zonas temporales
  - Restriccion:Desestimación horizontal zona 3, 5-7 años --limita--> Operacion:Compensaciones horizontales zonas temporales
  - Restriccion:Desestimación horizontal zona 3, 7-10 años --limita--> Operacion:Compensaciones horizontales zonas temporales
  - Restriccion:Desestimación horizontal zona 3, 10-15 años --limita--> Operacion:Compensaciones horizontales zonas temporales
  - Restriccion:Desestimación horizontal zona 3, 15-20 años --limita--> Operacion:Compensaciones horizontales zonas temporales
  - Restriccion:Desestimación horizontal zona 3 entre zonas adyacentes --limita--> Operacion:Compensaciones horizontales zonas temporales
  - Condicion:Condición de imputación por plazo residual --condicion_de--> Operacion:Compensaciones horizontales zonas temporales
- hechos: umbrales [{"entidad": "Restriccion:Desestimación horizontal zona 1, 0-1 meses", "tramo": "40%", "verificacion": "exacta"}, {"entidad": "Restriccion:Desestimación horizontal zona 1, 1-3 meses", "tramo": "40%", "verificacion": "exacta"}, {"entidad": "Restriccion:Desestimación horizontal zona 1, 3-6 meses", "tramo": "40%", "verificacion": "exacta"}, {"entidad": "Restriccion:Desestimación horizontal zona 1, 6-12 meses", "tramo": "40%", "verificacion": "exacta"}, {"entidad": "Restriccion:Desestimación horizontal zona 1 entre zonas adyacentes", "tramo": "40%", "verificacion": "exacta"}, {"entidad": "Restriccion:Desestimación horizontal zona 2, 1-2 años", "tramo": "30%", "verificacion": "exacta"}, {"entidad": "Restriccion:Desestimación horizontal zona 2, 2-3 años", "tramo": "30%", "verificacion": "exacta"}, {"entidad": "Restriccion:Desestimación horizontal zona 2, 2-3 años entre zonas 1 y 3", "tramo": "100%", "verificacion": "exacta"}, {"entidad": "Restriccion:Desestimación horizontal zona 2, 3-4 años", "tramo": "30%", "verificacion": "exacta"}, {"entidad": "Restriccion:Desestimación horizontal zona 2 entre zonas adyacentes", "tramo": "40%", "verificacion": "exacta"}, {"entidad": "Restriccion:Desestimación horizontal zona 3, 4-5 años", "tramo": "30%", "verificacion": "exacta"}, {"entidad": "Restriccion:Desestimación horizontal zona 3, 5-7 años", "tramo": "30%", "verificacion": "exacta"}, {"entidad": "Restriccion:Desestimación horizontal zona 3, 7-10 años", "tramo": "30%", "verificacion": "exacta"}, {"entidad": "Restriccion:Desestimación horizontal zona 3, 10-15 años", "tramo": "30%", "verificacion": "exacta"}, {"entidad": "Restriccion:Desestimación horizontal zona 3, 15-20 años", "tramo": "30%", "verificacion": "exacta"}, {"entidad": "Restriccion:Desestimación horizontal zona 3 entre zonas adyacentes", "tramo": "40%", "verificacion": "exacta"}]; menciones [{"pred": "aplica_a", "mencion": "las entidades", "verificada": "exacta", "sujeto_id": null}]; omisiones [{"categoria": "tabla", "tramo": "Fila 18: col2 = Más de 20", "verificacion": "exacta", "nota": "Fila incompleta: carece de valores para col3 (porcentaje dentro de zona), col4 (entre zonas adyacent…"}, {"categoria": "tabla", "tramo": "20 celdas combinadas no asignadas por E0 a sus filas respectivas", "verificacion": "no", "nota": "E0 registró que 20 celdas combinadas carecen de asignación clara a filas: sus valores pueden valer p…"}]; condicion_de [{"de": "Condicion:Condición de imputación por plazo residual", "a": "Operacion:Compensaciones horizontales zonas temporales", "firma_nueva": true}]; limita [{"de": "Restriccion:Desestimación horizontal zona 1, 0-1 meses", "a": "Operacion:Compensaciones horizontales zonas temporales"}, {"de": "Restriccion:Desestimación horizontal zona 1, 1-3 meses", "a": "Operacion:Compensaciones horizontales zonas temporales"}, {"de": "Restriccion:Desestimación horizontal zona 1, 3-6 meses", "a": "Operacion:Compensaciones horizontales zonas temporales"}, {"de": "Restriccion:Desestimación horizontal zona 1, 6-12 meses", "a": "Operacion:Compensaciones horizontales zonas temporales"}, {"de": "Restriccion:Desestimación horizontal zona 1 entre zonas adyacentes", "a": "Operacion:Compensaciones horizontales zonas temporales"}, {"de": "Restriccion:Desestimación horizontal zona 2, 1-2 años", "a": "Operacion:Compensaciones horizontales zonas temporales"}, {"de": "Restriccion:Desestimación horizontal zona 2, 2-3 años", "a": "Operacion:Compensaciones horizontales zonas temporales"}, {"de": "Restriccion:Desestimación horizontal zona 2, 2-3 años entre zonas 1 y 3", "a": "Operacion:Compensaciones horizontales zonas temporales"}, {"de": "Restriccion:Desestimación horizontal zona 2, 3-4 años", "a": "Operacion:Compensaciones horizontales zonas temporales"}, {"de": "Restriccion:Desestimación horizontal zona 2 entre zonas adyacentes", "a": "Operacion:Compensaciones horizontales zonas temporales"}, {"de": "Restriccion:Desestimación horizontal zona 3, 4-5 años", "a": "Operacion:Compensaciones horizontales zonas temporales"}, {"de": "Restriccion:Desestimación horizontal zona 3, 5-7 años", "a": "Operacion:Compensaciones horizontales zonas temporales"}, {"de": "Restriccion:Desestimación horizontal zona 3, 7-10 años", "a": "Operacion:Compensaciones horizontales zonas temporales"}, {"de": "Restriccion:Desestimación horizontal zona 3, 10-15 años", "a": "Operacion:Compensaciones horizontales zonas temporales"}, {"de": "Restriccion:Desestimación horizontal zona 3, 15-20 años", "a": "Operacion:Compensaciones horizontales zonas temporales"}, {"de": "Restriccion:Desestimación horizontal zona 3 entre zonas adyacentes", "a": "Operacion:Compensaciones horizontales zonas temporales"}]

*Cuantías en el texto propio: 15.*

## Ficha 66 — `ric::4.5.1`

**Texto propio:**

```
4.5.1. Swaps
[TABLA ric::tabla011 | página 19 | e0_tablas | posicional]
Fila 1: col1 = Descripción del activo subyacente(1) | col2 = Activo comprado(2) | col3 = Activo vendido(2) | col4 = Próxima fecha de recálculo del flujo variable (cuando corresponda) | col5 = Vencimiento del derivado | col6 = Contraparte/Ámb ito de negociación | col7 = Valor nocional sobre el que se calculan los flujos a pagar (3a) | col8 = Valor nocional sobre el que se calculan los pagos de la contraparte o flujos a recibir (3b) | col9 = Precio pactado del subyacente (4)
[FIN TABLA ric::tabla011]
(1) Describir el activo subyacente del swap como indican los siguientes ejemplos: Tasa de interés
Badlar Privada para depósitos de más de 1 millón de pesos por un plazo de 30 a 35 días contra
tasa fija en pesos, dólar estadounidense contra peso argentino, Variación del Coeficiente de
Estabilización de Referencia contra tasa fija en pesos, etc.
(2) Por ejemplo, en un swap de tasa Badlar contra tasa fija en el que se debe pagar tasa fija y recibir
variable, indicar "Badlar " en el campo Activo comprado y "Tasa fija" en el Activo vendido.
(3a) y (3b) Especificar el valor nocional incluyendo la moneda o unidad de medida. Por ejemplo, USD
25.000.000, $ 100.000, etc. En swaps en la misma moneda coincidirán (3a) y (3b)
(4) Valor del subyacente pactado en el tramo fijo. Por ejemplo, valor de la tasa fija pactada.
```
**Último bloque heredado:** 4.5. Información sobre instrumentos derivados

**SELLADO** — error: None

- Operacion «Swap: información de nocional»: Reportar valor nocional sobre el que se calculan los pagos de flujos a pagar y flujos a recibir en un swap, incluyendo moneda o unidad de medida (ej.: USD 25.000.000, $ 100.000). En swaps en la misma moneda, los valores coinciden.
- Operacion «Swap: descripción activo subyacente»: Describir el activo subyacente del swap según ejemplos: Tasa de interés Badlar Privada para depósitos de más de 1 millón de pesos por plazo de 30 a 35 días contra tasa fija en pesos, dólar estadounidense contra peso argentino, Variación del…
- Operacion «Swap: especificación activo comprado/vendido»: Indicar activo comprado y activo vendido: en un swap de tasa Badlar contra tasa fija donde se paga tasa fija y recibe variable, indicar 'Badlar' en campo Activo comprado e indicar 'Tasa fija' en Activo vendido.
- Operacion «Swap: precio pactado tramo fijo»: Reportar valor del subyacente pactado en el tramo fijo (ej.: valor de la tasa fija pactada).
- Obligacion «Reporte de swaps — información nocional»: Reportar valor nocional sobre el que se calculan los pagos de flujos a pagar y flujos a recibir; especificar moneda o unidad de medida.
- Obligacion «Reporte de swaps — descripción subyacente»: Describir el activo subyacente del swap conforme a los ejemplos especificados (tasas, monedas, índices).
- Obligacion «Reporte de swaps — activos comprado/vendido»: Indicar en los campos correspondientes el activo comprado y el activo vendido según la estructura de la operación.
- Obligacion «Reporte de swaps — precio subyacente tramo fijo»: Reportar el valor del subyacente pactado en el tramo fijo de la operación.
  - Operacion:Swap: información de nocional --establecida_en--> TextoOrdenado:Régimen informativo contable mensual
  - Operacion:Swap: descripción activo subyacente --establecida_en--> TextoOrdenado:Régimen informativo contable mensual
  - Operacion:Swap: especificación activo comprado/vendido --establecida_en--> TextoOrdenado:Régimen informativo contable mensual
  - Operacion:Swap: precio pactado tramo fijo --establecida_en--> TextoOrdenado:Régimen informativo contable mensual
  - Obligacion:Reporte de swaps — información nocional --establecida_en--> TextoOrdenado:Régimen informativo contable mensual
  - Obligacion:Reporte de swaps — descripción subyacente --establecida_en--> TextoOrdenado:Régimen informativo contable mensual
  - Obligacion:Reporte de swaps — activos comprado/vendido --establecida_en--> TextoOrdenado:Régimen informativo contable mensual
  - Obligacion:Reporte de swaps — precio subyacente tramo fijo --establecida_en--> TextoOrdenado:Régimen informativo contable mensual
  - Obligacion:Reporte de swaps — información nocional --aplica_a--> None
  - Obligacion:Reporte de swaps — descripción subyacente --aplica_a--> None
  - Obligacion:Reporte de swaps — activos comprado/vendido --aplica_a--> None
  - Obligacion:Reporte de swaps — precio subyacente tramo fijo --aplica_a--> None
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}]; omisiones [{"categoria": null, "tramo": "", "verificacion": "ausente", "nota": "Tabla de estructura de swap con columnas (Activo comprado, Activo vendido, Valor nocional comprado/v…"}, {"categoria": null, "tramo": "", "verificacion": "ausente", "nota": "Valores numéricos específicos de columnas (montos, fechas, tasas): no extraídos de celdas de tabla p…"}]; condicion_de []; limita []

**NUEVO** — error: None

- Operacion «Swap — información requerida»: Operación de swap con especificación de descripción del activo subyacente (tasa de interés Badlar, divisas, CER), activo comprado, activo vendido, próxima fecha de recálculo del flujo variable, vencimiento del derivado, contraparte/ámbito d… ‖ tramo (exacta): «4.5.1. Swaps»
- Obligacion «Información sobre swaps — descripción del subyacente»: Las entidades deben presentar información describiendo el activo subyacente del swap con los ejemplos indicados: Tasa de interés Badlar Privada para depósitos de más de 1 millón de pesos por un plazo de 30 a 35 días contra tasa fija en peso… ‖ tramo (exacta): «Describir el activo subyacente del swap como indican los siguientes ejemplos: Tasa de interés Badlar Privada para depósitos de más de 1 millón de pesos por un p…»
- Obligacion «Información sobre swaps — activo comprado y vendido»: Las entidades deben indicar en la información sobre swaps el activo comprado y activo vendido, especificando conforme al ejemplo: en un swap de tasa Badlar contra tasa fija en el que se debe pagar tasa fija y recibir variable, indicar 'Badl… ‖ tramo (exacta): «en un swap de tasa Badlar contra tasa fija en el que se debe pagar tasa fija y recibir variable, indicar "Badlar" en el campo Activo comprado y "Tasa fija" en e…»
- Obligacion «Información sobre swaps — valor nocional»: Las entidades deben especificar el valor nocional incluyendo la moneda o unidad de medida (ejemplos: USD 25.000.000, $ 100.000). En swaps en la misma moneda los valores nominales coincidirán en columnas (3a) y (3b) ‖ tramo (exacta): «Especificar el valor nocional incluyendo la moneda o unidad de medida. Por ejemplo, USD 25.000.000, $ 100.000, etc. En swaps en la misma moneda coincidirán (3a)…»
- Obligacion «Información sobre swaps — precio pactado»: Las entidades deben informar el precio pactado del subyacente en el tramo fijo (por ejemplo, valor de la tasa fija pactada) ‖ tramo (exacta): «Valor del subyacente pactado en el tramo fijo. Por ejemplo, valor de la tasa fija pactada»
  - Operacion:Swap — información requerida --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Obligacion:Información sobre swaps — descripción del subyacente --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Obligacion:Información sobre swaps — activo comprado y vendido --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Obligacion:Información sobre swaps — valor nocional --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Obligacion:Información sobre swaps — precio pactado --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Obligacion:Información sobre swaps — descripción del subyacente --aplica_a--> las entidades
  - Obligacion:Información sobre swaps — activo comprado y vendido --aplica_a--> las entidades
  - Obligacion:Información sobre swaps — valor nocional --aplica_a--> las entidades
  - Obligacion:Información sobre swaps — precio pactado --aplica_a--> las entidades
  - Obligacion:Información sobre swaps — descripción del subyacente --regula--> Operacion:Swap — información requerida
  - Obligacion:Información sobre swaps — activo comprado y vendido --regula--> Operacion:Swap — información requerida
  - Obligacion:Información sobre swaps — valor nocional --regula--> Operacion:Swap — información requerida
  - Obligacion:Información sobre swaps — precio pactado --regula--> Operacion:Swap — información requerida
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "las entidades", "verificada": "no", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "las entidades", "verificada": "no", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "las entidades", "verificada": "no", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "las entidades", "verificada": "no", "sujeto_id": null}]; omisiones [{"categoria": "fuera_de_tipos", "tramo": "[TABLA ric::tabla011 | página 19 | e0_tablas | posicional] Fila 1: col1 = Descripción del activo sub…", "verificacion": "exacta", "nota": "Tabla serializada: estructura de datos de presentación informativa. Los campos de la tabla (columnas…"}]; condicion_de []; limita []

*Cuantías en el texto propio: 3.*

## Ficha 67 — `expaef::6.6.2`

**Texto propio:**

```
6.6.2. Las sanciones que sean impuestas a la entidad por las autoridades de control del país
de radicación.
```
**Último bloque heredado:** Se deberá comunicar de inmediato a la SEFyC:

**SELLADO** — error: None

- Obligacion «Comunicar de inmediato sanciones de autoridades de control»: Las sanciones que sean impuestas a la entidad por las autoridades de control del país de radicación deberán comunicarse de inmediato a la SEFyC
  - Obligacion:Comunicar de inmediato sanciones de autoridades de control --establecida_en--> TextoOrdenado:Participación en entidades financieras del exterior
  - Obligacion:Comunicar de inmediato sanciones de autoridades de control --aplica_a--> None
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}]; omisiones []; condicion_de []; limita []

**NUEVO** — error: None

- Obligacion «Comunicación inmediata de sanciones de autoridades de control»: Comunicar inmediatamente a la SEFyC las sanciones que sean impuestas a la entidad por las autoridades de control del país de radicación. ‖ tramo (no): «Se deberá comunicar de inmediato a la SEFyC: Las sanciones que sean impuestas a la entidad por las autoridades de control del país de radicación.»
  - Obligacion:Comunicación inmediata de sanciones de autoridades de contro… --establecida_en--> TextoOrdenado:Exposición de posiciones en entidades financieras del exteri…
  - Obligacion:Comunicación inmediata de sanciones de autoridades de contro… --aplica_a--> la entidad
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "la entidad", "verificada": "exacta", "sujeto_id": null}]; omisiones []; condicion_de []; limita []

*Cuantías en el texto propio: 0.*

## Ficha 68 — `cap::7.1.2`

**Texto propio:**

```
7.1.2. Componente del indicador de negocio (BIC).
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
```
**Último bloque heredado:** RO

**SELLADO** — error: None

- Operacion «Determinación de BIC — expresión matemática»: Se determinará por la siguiente expresión: BIC = ∑ BI x α, donde los coeficientes marginales (α) se determinarán en función del tramo del BI
- Definicion «Coeficientes marginales (α) — categoría 1»: Para las entidades incluidas en la categoría 1 (BI igual o inferior al equivalente en pesos de €1.000 millones), el coeficiente marginal es del 12%
- Definicion «Coeficientes marginales (α) — categoría 2»: Para la categoría 2 (BI mayor a €1.000 millones e igual o inferior a €30.000 millones), el coeficiente marginal es del 15%
- Definicion «Coeficientes marginales (α) — categoría 3»: Para la categoría 3 (BI mayor a €30.000 millones), el coeficiente marginal es del 18%
- Obligacion «Conversión a pesos — equivalente en moneda local»: Deberá calcularse el importe equivalente en pesos al tipo de cambio vendedor del Banco de la Nación Argentina al cierre de las operaciones del último día hábil del mes anterior del que se trate
  - Operacion:Determinación de BIC — expresión matemática --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Definicion:Coeficientes marginales (α) — categoría 1 --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Definicion:Coeficientes marginales (α) — categoría 2 --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Definicion:Coeficientes marginales (α) — categoría 3 --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Obligacion:Conversión a pesos — equivalente en moneda local --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Operacion:Determinación de BIC — expresión matemática --aplica_a--> None
  - Obligacion:Conversión a pesos — equivalente en moneda local --aplica_a--> None
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}]; omisiones [{"categoria": null, "tramo": "", "verificacion": "ausente", "nota": "Tabla de categorías y tramos de BI: estructura tabular no confiable. Encabezados 'Tramo de BI (en mi…"}, {"categoria": null, "tramo": "", "verificacion": "ausente", "nota": "Fórmula 'BIC = ∑ BI x α' con subíndices i: estructura visual y notación matemática no confiable en e…"}]; condicion_de []; limita []

**NUEVO** — error: None

- Operacion «Determinación del componente del indicador de negocio (BIC)»: El BIC se determina como el producto del indicador de negocio (BI) por coeficientes marginales (α), determinados según el tramo del BI conforme a la tabla de categorías. ‖ tramo (exacta): «Se determinará por la siguiente expresión: BIC = ∑ BI x α»
- Condicion «Tramo de BI ≤ 1 mil millones EUR»: El BI es igual o inferior al equivalente en pesos de €1.000 millones (según tipo de cambio vendedor del Banco de la Nación Argentina al cierre de las operaciones del último día hábil del mes anterior). ‖ tramo (exacta): «Categoría = 1 | Tramo de BI (en miles de millones de euros*) = ≤ 1»
- Restriccion «Coeficiente marginal 12% para categoría 1 (BI ≤ 1 mil millones EUR)»: El coeficiente marginal (α) aplicable al BI cuando este es igual o inferior a €1.000 millones es del 12%. ‖ tramo (tokens): «1 | Coeficientes marginales de BI (α) i = 12% Fila 2: Categoría»
- Condicion «Tramo de BI > 1 y ≤ 30 mil millones EUR»: El BI es superior a €1.000 millones pero no superior a €30.000 millones (según tipo de cambio vendedor del Banco de la Nación Argentina al cierre de las operaciones del último día hábil del mes anterior). ‖ tramo (exacta): «Categoría = 2 | Tramo de BI (en miles de millones de euros*) = 1 < BI ≤ 30»
- Restriccion «Coeficiente marginal 15% para categoría 2 (BI > 1 y ≤ 30 mil millones EUR)»: El coeficiente marginal (α) aplicable al BI cuando este es superior a €1.000 millones pero no superior a €30.000 millones es del 15%. ‖ tramo (no): «Categoría = 2 | Coeficientes marginales de BI (α) i = 15%»
- Condicion «Tramo de BI > 30 mil millones EUR»: El BI es superior a €30.000 millones (según tipo de cambio vendedor del Banco de la Nación Argentina al cierre de las operaciones del último día hábil del mes anterior). ‖ tramo (exacta): «Categoría = 3 | Tramo de BI (en miles de millones de euros*) = >30»
- Restriccion «Coeficiente marginal 18% para categoría 3 (BI > 30 mil millones EUR)»: El coeficiente marginal (α) aplicable al BI cuando este es superior a €30.000 millones es del 18%. ‖ tramo (no): «Categoría = 3 | Coeficientes marginales de BI (α) i = 18%»
- Obligacion «Equivalente en pesos a tipo de cambio vendedor Banco Nación»: Las entidades deberán convertir los tramos de BI expresados en euros al equivalente en pesos utilizando el tipo de cambio vendedor del Banco de la Nación Argentina al cierre de las operaciones del último día hábil del mes anterior. ‖ tramo (exacta): «Deberá calcularse el importe equivalente en pesos al tipo de cambio vendedor del Banco de la Nación Argentina al cierre de las operaciones del último día hábil …»
  - Operacion:Determinación del componente del indicador de negocio (BIC) --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Condicion:Tramo de BI ≤ 1 mil millones EUR --condicion_de--> Restriccion:Coeficiente marginal 12% para categoría 1 (BI ≤ 1 mil millon…
  - Restriccion:Coeficiente marginal 12% para categoría 1 (BI ≤ 1 mil millon… --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Condicion:Tramo de BI > 1 y ≤ 30 mil millones EUR --condicion_de--> Restriccion:Coeficiente marginal 15% para categoría 2 (BI > 1 y ≤ 30 mil…
  - Restriccion:Coeficiente marginal 15% para categoría 2 (BI > 1 y ≤ 30 mil… --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Condicion:Tramo de BI > 30 mil millones EUR --condicion_de--> Restriccion:Coeficiente marginal 18% para categoría 3 (BI > 30 mil millo…
  - Restriccion:Coeficiente marginal 18% para categoría 3 (BI > 30 mil millo… --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Obligacion:Equivalente en pesos a tipo de cambio vendedor Banco Nación --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Obligacion:Equivalente en pesos a tipo de cambio vendedor Banco Nación --aplica_a--> las entidades
- hechos: umbrales [{"entidad": "Condicion:Tramo de BI ≤ 1 mil millones EUR", "tramo": "≤ 1", "verificacion": "exacta"}, {"entidad": "Restriccion:Coeficiente marginal 12% para categoría 1 (BI ≤ 1 mil millon…", "tramo": "12%", "verificacion": "exacta"}, {"entidad": "Condicion:Tramo de BI > 1 y ≤ 30 mil millones EUR", "tramo": "1 < BI ≤ 30", "verificacion": "exacta"}, {"entidad": "Restriccion:Coeficiente marginal 15% para categoría 2 (BI > 1 y ≤ 30 mil…", "tramo": "15%", "verificacion": "exacta"}, {"entidad": "Condicion:Tramo de BI > 30 mil millones EUR", "tramo": ">30", "verificacion": "exacta"}, {"entidad": "Restriccion:Coeficiente marginal 18% para categoría 3 (BI > 30 mil millo…", "tramo": "18%", "verificacion": "exacta"}]; menciones [{"pred": "aplica_a", "mencion": "las entidades", "verificada": "exacta", "sujeto_id": null}]; omisiones [{"categoria": "formula", "tramo": "BIC = ∑ BI x α", "verificacion": "exacta", "nota": "Fórmula matemática no-confiable: la expresión contiene sumas y productos cuyo significado computacio…"}, {"categoria": "meta_normativo", "tramo": "Los coeficientes marginales aumentan conforme se incrementa el tamaño del BI.", "verificacion": "exacta", "nota": "Enunciado interpretativo que predica sobre la lógica de los coeficientes sin prescribir conducta. No…"}]; condicion_de [{"de": "Condicion:Tramo de BI ≤ 1 mil millones EUR", "a": "Restriccion:Coeficiente marginal 12% para categoría 1 (BI ≤ 1 mil millon…", "firma_nueva": false}, {"de": "Condicion:Tramo de BI > 1 y ≤ 30 mil millones EUR", "a": "Restriccion:Coeficiente marginal 15% para categoría 2 (BI > 1 y ≤ 30 mil…", "firma_nueva": false}, {"de": "Condicion:Tramo de BI > 30 mil millones EUR", "a": "Restriccion:Coeficiente marginal 18% para categoría 3 (BI > 30 mil millo…", "firma_nueva": false}]; limita []

*Cuantías en el texto propio: 8.*

## Ficha 69 — `cap::7.1.3.2`

**Texto propio:**

```
7.1.3.2. Las partidas del BI para cada uno de los 3 períodos consecutivos de 12 meses
de cálculo del BI.
```
**Último bloque heredado:** Las entidades financieras deben dar a conocer al público, de manera regular, a través de sus páginas de Internet o reportes –conforme a los requerimientos que al efecto se esta- blezcan– lo siguiente:

**SELLADO** — error: None

- Obligacion «Divulgación partidas BI — 3 períodos 12 meses»: Las entidades financieras deben dar a conocer al público, de manera regular, a través de sus páginas de Internet o reportes lo siguiente: Las partidas del BI para cada uno de los 3 períodos consecutivos de 12 meses de cálculo del BI.
  - Obligacion:Divulgación partidas BI — 3 períodos 12 meses --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Obligacion:Divulgación partidas BI — 3 períodos 12 meses --aplica_a--> None
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}]; omisiones []; condicion_de []; limita []

**NUEVO** — error: None

- Operacion «Divulgación partidas BI 12 meses»: Divulgación al público, de manera regular a través de páginas de Internet o reportes, de las partidas del indicador de negocio (BI) para cada uno de los 3 períodos consecutivos de 12 meses de cálculo del BI ‖ tramo (exacta): «Las partidas del BI para cada uno de los 3 períodos consecutivos de 12 meses de cálculo del BI»
- Obligacion «Divulgar partidas BI períodos 12 meses»: Las entidades financieras deben dar a conocer al público, de manera regular, a través de sus páginas de Internet o reportes, las partidas del indicador de negocio (BI) para cada uno de los 3 períodos consecutivos de 12 meses de cálculo del … ‖ tramo (no): «Las entidades financieras deben dar a conocer al público, de manera regular, a través de sus páginas de Internet o reportes […] lo siguiente: […] Las partidas d…»
  - Obligacion:Divulgar partidas BI períodos 12 meses --establecida_en--> TextoOrdenado:Capitales mínimos
  - Obligacion:Divulgar partidas BI períodos 12 meses --aplica_a--> Las entidades financieras
  - Obligacion:Divulgar partidas BI períodos 12 meses --regula--> Operacion:Divulgación partidas BI 12 meses
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "Las entidades financieras", "verificada": "exacta", "sujeto_id": null}]; omisiones [{"categoria": "meta_normativo", "tramo": "conforme a los requerimientos que al efecto se establezcan", "verificacion": "no", "nota": "cláusula interpretativa que predica sobre el alcance de los requerimientos, no sobre conducta prescr…"}]; condicion_de []; limita []

*Cuantías en el texto propio: 1.*

## Ficha 70 — `cla::5.1.1::intro`

**Texto propio:**

```
Abarca todas las financiaciones comprendidas, con excepción de las siguientes:
```
**Último bloque heredado:** 5.1.1. Cartera comercial.

**SELLADO** — error: None

- Definicion «Cartera comercial — alcance»: Abarca todas las financiaciones comprendidas, con excepción de las siguientes
  - Definicion:Cartera comercial — alcance --establecida_en--> TextoOrdenado:Clasificación de Deudores
- hechos: umbrales []; menciones []; omisiones []; condicion_de []; limita []

**NUEVO** — error: None

- hechos: umbrales []; menciones []; omisiones [{"categoria": "meta_normativo", "tramo": "Abarca todas las financiaciones comprendidas", "verificacion": "exacta", "nota": "Declaración de alcance sobre lo que la categoría de cartera comercial incluye; enuncia el contenido …"}]; condicion_de []; limita []

*Cuantías en el texto propio: 0.*

## Ficha 71 — `cap::10.1`

**Texto propio:**

```
10.1. Disposiciones generales.
Las calificaciones crediticias efectuadas por entidades que sean agentes de calificación ex-
terna (“External Credit Assessment Institution”, ECAI) sólo podrán ser utilizadas para la de-
terminación del ponderador de riesgo de una exposición cuando la ECAI que las efectuó sea
elegible conforme a las disposiciones de esta Sección.
Las entidades financieras, a través de sus responsables del área de riesgos, deberán informar
las ECAI elegidas a la Gerencia de Supervisión de Entidades Financieras de la SEFyC que
corresponda, a la casilla de correo electrónico entidades.super@bcra.gob.ar.
```
**Último bloque heredado:** Sección 10. Agentes de calificación externa (ECAI).

**SELLADO** — error: None

- Operacion «Utilización de calificaciones crediticias ECAI»: Utilización de calificaciones crediticias efectuadas por ECAI para la determinación del ponderador de riesgo de una exposición
- Restriccion «ECAI elegible — utilización calificaciones»: Las calificaciones crediticias efectuadas por ECAI sólo podrán ser utilizadas para la determinación del ponderador de riesgo cuando la ECAI que las efectuó sea elegible conforme a las disposiciones de esta Sección
- Obligacion «Informar ECAI elegidas a SEFyC»: Las entidades financieras, a través de sus responsables del área de riesgos, deberán informar las ECAI elegidas a la Gerencia de Supervisión de Entidades Financieras de la SEFyC que corresponda, a la casilla de correo electrónico entidades.…
- Condicion «ECAI elegible conforme Sección 10»: cuando la ECAI sea elegible conforme a las disposiciones de la Sección 10
  - Restriccion:ECAI elegible — utilización calificaciones --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Obligacion:Informar ECAI elegidas a SEFyC --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Condicion:ECAI elegible conforme Sección 10 --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Restriccion:ECAI elegible — utilización calificaciones --limita--> Operacion:Utilización de calificaciones crediticias ECAI
  - Condicion:ECAI elegible conforme Sección 10 --condicion_de--> Restriccion:ECAI elegible — utilización calificaciones
  - Obligacion:Informar ECAI elegidas a SEFyC --aplica_a--> None
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}]; omisiones []; condicion_de [{"de": "Condicion:ECAI elegible conforme Sección 10", "a": "Restriccion:ECAI elegible — utilización calificaciones", "firma_nueva": false}]; limita [{"de": "Restriccion:ECAI elegible — utilización calificaciones", "a": "Operacion:Utilización de calificaciones crediticias ECAI"}]

**NUEVO** — error: None

- Restriccion «Uso de calificaciones crediticias de ECAI para ponderador de riesgo»: Las calificaciones crediticias de ECAI solo pueden utilizarse para determinar el ponderador de riesgo cuando la ECAI sea elegible según las disposiciones de la Sección 10. ‖ tramo (exacta): «Las calificaciones crediticias efectuadas por entidades que sean agentes de calificación externa ("External Credit Assessment Institution", ECAI) sólo podrán se…»
- Operacion «Utilización de calificaciones crediticias de ECAI»: Utilización de calificaciones crediticias efectuadas por ECAI para la determinación del ponderador de riesgo de una exposición ‖ tramo (exacta): «las calificaciones crediticias efectuadas por entidades que sean agentes de calificación externa ("External Credit Assessment Institution", ECAI) sólo podrán se…»
- Operacion «Elegibilidad de ECAI conforme a Sección 10»: Verificación de que la ECAI que efectuó la calificación crediticia sea elegible conforme a las disposiciones de la Sección 10 ‖ tramo (exacta): «la ECAI que las efectuó sea elegible conforme a las disposiciones de esta Sección»
- Obligacion «Informe de ECAI elegidas al supervisor»: Las entidades financieras, por conducto de sus responsables del área de riesgos, deberán informar las ECAI elegidas a la Gerencia de Supervisión de Entidades Financieras de la SEFyC, a través de la dirección entidades.super@bcra.gob.ar ‖ tramo (exacta): «Las entidades financieras, a través de sus responsables del área de riesgos, deberán informar las ECAI elegidas a la Gerencia de Supervisión de Entidades Financ…»
  - Restriccion:Uso de calificaciones crediticias de ECAI para ponderador de… --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Obligacion:Informe de ECAI elegidas al supervisor --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Restriccion:Uso de calificaciones crediticias de ECAI para ponderador de… --limita--> Operacion:Utilización de calificaciones crediticias de ECAI
  - Obligacion:Informe de ECAI elegidas al supervisor --aplica_a--> Las entidades financieras
  - rechazo: firma_invalida: relations[3]: Operacion --condicion_de--> Restriccion
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "Las entidades financieras", "verificada": "exacta", "sujeto_id": null}]; omisiones []; condicion_de []; limita [{"de": "Restriccion:Uso de calificaciones crediticias de ECAI para ponderador de…", "a": "Operacion:Utilización de calificaciones crediticias de ECAI"}]

*Cuantías en el texto propio: 0.*

## Ficha 72 — `cap::2.5.7`

**Texto propio:**

```
2.5.7. En el caso de que al menos una de las operaciones de la contraparte con la entidad fi-
nanciera se encuentre en situación de incumplimiento, a la totalidad de la exposición de
la entidad financiera a la contraparte se le aplicará el tratamiento previsto en el punto
2.10.
```
**Último bloque heredado:** 2.5. Criterios para la determinación de los activos ponderados por riesgo.

**SELLADO** — error: None

- Condicion «Incumplimiento al menos una operación contraparte»: al menos una de las operaciones de la contraparte con la entidad financiera se encuentre en situación de incumplimiento
- Operacion «Aplicación tratamiento exposición incumplida»: a la totalidad de la exposición de la entidad financiera a la contraparte se le aplicará el tratamiento previsto en el punto 2.10
  - Condicion:Incumplimiento al menos una operación contraparte --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Operacion:Aplicación tratamiento exposición incumplida --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Condicion:Incumplimiento al menos una operación contraparte --condicion_de--> Operacion:Aplicación tratamiento exposición incumplida
  - Operacion:Aplicación tratamiento exposición incumplida --aplica_a--> None
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}]; omisiones []; condicion_de [{"de": "Condicion:Incumplimiento al menos una operación contraparte", "a": "Operacion:Aplicación tratamiento exposición incumplida", "firma_nueva": true}]; limita []

**NUEVO** — error: None

- Condicion «Operación en incumplimiento»: La condición se verifica cuando al menos una operación de la contraparte está en situación de incumplimiento. ‖ tramo (exacta): «al menos una de las operaciones de la contraparte con la entidad financiera se encuentre en situación de incumplimiento»
- Operacion «Aplicación de tratamiento por incumplimiento»: Cuando al menos una operación de la contraparte está en incumplimiento, se aplica a la totalidad de la exposición el tratamiento de riesgo de crédito previsto en el punto 2.10. ‖ tramo (exacta): «a la totalidad de la exposición de la entidad financiera a la contraparte se le aplicará el tratamiento previsto en el punto 2.10»
- Restriccion «Ponderación por incumplimiento total de exposición»: Cuando existe incumplimiento en al menos una operación, la totalidad de la exposición a esa contraparte recibe el tratamiento de riesgo de crédito del punto 2.10. ‖ tramo (exacta): «a la totalidad de la exposición de la entidad financiera a la contraparte se le aplicará el tratamiento previsto en el punto 2.10»
  - Condicion:Operación en incumplimiento --establecida_en--> TextoOrdenado:Capitales mínimos
  - Operacion:Aplicación de tratamiento por incumplimiento --establecida_en--> TextoOrdenado:Capitales mínimos
  - Restriccion:Ponderación por incumplimiento total de exposición --establecida_en--> TextoOrdenado:Capitales mínimos
  - Condicion:Operación en incumplimiento --condicion_de--> Restriccion:Ponderación por incumplimiento total de exposición
  - Restriccion:Ponderación por incumplimiento total de exposición --aplica_a--> la entidad financiera
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "la entidad financiera", "verificada": "exacta", "sujeto_id": null}]; omisiones [{"categoria": "relacion_sin_predicado", "tramo": "se le aplicará el tratamiento previsto en el punto 2.10", "verificacion": "exacta", "nota": "remisión_a_otro_punto"}]; condicion_de [{"de": "Condicion:Operación en incumplimiento", "a": "Restriccion:Ponderación por incumplimiento total de exposición", "firma_nueva": false}]; limita []

*Cuantías en el texto propio: 0.*

## Ficha 73 — `ext::3.16.3.6`

**Texto propio:**

```
3.16.3.6. En las declaraciones juradas elaboradas para dar cumplimiento a los
puntos 3.16.3.1. y 3.16.3.2. no deberán tenerse en cuenta:
i) las transferencias de títulos valores a entidades depositarias del
exterior realizadas o a realizar por el cliente con el objeto de
participar de un canje o una operación de recompra de títulos de
deuda emitidos por el Gobierno Nacional, gobiernos locales u otros
emisores residentes del sector privado. El cliente deberá
comprometerse a presentar la correspondiente certificación por los
títulos de deuda canjeados.
ii) la entrega de activos locales con el objeto de cancelar una deuda con
una agencia oficial de crédito o una entidad financiera del exterior, en
la medida que se produzca a partir del vencimiento como
consecuencia de una cláusula de garantía prevista en el contrato de
endeudamiento.
iii) las ventas de títulos valores con liquidación en moneda extranjera en
el país o en el exterior cuando la totalidad de los fondos obtenidos de
tales liquidaciones se haya utilizado o será utilizada dentro de los 10
(diez) días corridos a las siguientes operaciones:
a) Pagos a partir del vencimiento de capital o intereses de nuevos
endeudamientos financieros comprendidos en el punto 3.5.,
desembolsados a partir del 02/10/23 y que contemplen como
mínimo 1 (un) año de gracia para el pago de capital.
b) Repatriaciones del capital y rentas asociadas a las inversiones
directas de no residentes recibidas a partir del 02/10/23, en la
medida que la repatriación se produzca como mínimo 1 (un) año
después de la concreción del aporte de capital y se haya dado
cumplimiento a los mecanismos legales previstos en tales casos.
c) Pagos a partir del vencimiento de capital o intereses de títulos de
deuda emitidos a partir del 02/10/23 con registro público en el
país no comprendidos en el punto 3.5., denominados y
suscriptos en moneda extranjera, con servicios pagaderos en
moneda extranjera y que contemplen como mínimo 2 (dos) años
de gracia para el pago de capital.
d) Pagos a partir del vencimiento de capital o intereses de
endeudamientos financieros comprendidos en el punto 3.5. que
no generen desembolsos por ser refinanciaciones de capital y/o
intereses de operaciones contempladas en los incisos a) y c)
precedentes, en la medida que las refinanciaciones no anticipen
el vencimiento de la deuda original.
e) Pagos a partir del vencimiento de capital o intereses de títulos de
emitidos con registro público en el país no comprendidos en el
punto 3.5., denominados en moneda extranjera, con servicios
pagaderos en moneda extranjera y que no generen desembolsos
por ser refinanciaciones de capital y/o intereses de operaciones
contempladas en el inciso c) precedente en la medida que las
refinanciaciones no anticipen el vencimiento de la deuda original.
En todos los casos el cliente deberá presentar una declaración jurada
dejando constancia de que los fondos oportunamente recibidos por
las operaciones detalladas en los incisos a) a c) precedente
```
**Último bloque heredado:** En caso de que el cliente sea una persona jurídica, para que la operación no quede comprendida por el requisito de conformidad previa, la entidad deberá contar adicionalmente con una declaración jurada en la que conste:

**SELLADO** — error: None

- Excepcion «Excepción transferencias a depositarias para canje»: Las transferencias de títulos valores a entidades depositarias del exterior realizadas o a realizar por el cliente con el objeto de participar de un canje o una operación de recompra de títulos de deuda emitidos por el Gobierno Nacional, go…
- Obligacion «Presentación certificación títulos canjeados»: El cliente deberá comprometerse a presentar la correspondiente certificación por los títulos de deuda canjeados.
- Excepcion «Excepción entrega activos para cancelar deuda»: La entrega de activos locales con el objeto de cancelar una deuda con una agencia oficial de crédito o una entidad financiera del exterior, en la medida que se produzca a partir del vencimiento como consecuencia de una cláusula de garantía …
- Excepcion «Excepción ventas títulos con liquidación plazo 10 días»: Las ventas de títulos valores con liquidación en moneda extranjera en el país o en el exterior cuando la totalidad de los fondos obtenidos de tales liquidaciones se haya utilizado o será utilizada dentro de los 10 (diez) días corridos a las…
- Operacion «Pagos capital/intereses endeudamientos financieros»: Pagos a partir del vencimiento de capital o intereses de nuevos endeudamientos financieros comprendidos en el punto 3.5., desembolsados a partir del 02/10/23 y que contemplen como mínimo 1 (un) año de gracia para el pago de capital.
- Operacion «Repatriaciones capital e inversiones directas»: Repatriaciones del capital y rentas asociadas a las inversiones directas de no residentes recibidas a partir del 02/10/23, en la medida que la repatriación se produzca como mínimo 1 (un) año después de la concreción del aporte de capital y …
- Operacion «Pagos capital/intereses títulos deuda emitidos»: Pagos a partir del vencimiento de capital o intereses de títulos de deuda emitidos a partir del 02/10/23 con registro público en el país no comprendidos en el punto 3.5., denominados y suscriptos en moneda extranjera, con servicios pagadero…
- Operacion «Pagos refinanciaciones punto 3.5.»: Pagos a partir del vencimiento de capital o intereses de endeudamientos financieros comprendidos en el punto 3.5. que no generen desembolsos por ser refinanciaciones de capital y/o intereses de operaciones contempladas en los incisos a) y c…
- Operacion «Pagos refinanciaciones títulos no punto 3.5.»: Pagos a partir del vencimiento de capital o intereses de títulos emitidos con registro público en el país no comprendidos en el punto 3.5., denominados en moneda extranjera, con servicios pagaderos en moneda extranjera y que no generen dese…
- Obligacion «Presentación declaración utilización fondos inversiones»: El cliente deberá presentar una declaración jurada dejando constancia de que los fondos oportunamente recibidos por las operaciones detalladas en los incisos a) a c) se utilizaron en su totalidad para concretar pagos en el país relacionados…
- Excepcion «Excepción ventas/transferencias BOPREAL monto adquirido»: Las ventas con liquidación en moneda extranjera en el país o en el exterior de los Bonos para la Reconstrucción de una Argentina Libre (BOPREAL) o las transferencias de estos bonos a depositarios en el exterior, cuando sean realizados por h…
- Excepcion «Excepción ventas/transferencias BOPREAL importadores»: Las ventas con liquidación en moneda extranjera en el exterior o las transferencias a depositarios del exterior que concreten los importadores de bienes y servicios que hayan adquirido en una suscripción primaria Bonos para la Reconstrucció…
- Condicion «Condición utilización fondos en 10 días»: La totalidad de los fondos obtenidos de liquidaciones de ventas de títulos valores se haya utilizado o será utilizada dentro de los 10 (diez) días corridos a las operaciones detalladas.
  - Excepcion:Excepción transferencias a depositarias para canje --establecida_en--> TextoOrdenado:Texto Ordenado Exterior - Cambios
  - Obligacion:Presentación certificación títulos canjeados --establecida_en--> TextoOrdenado:Texto Ordenado Exterior - Cambios
  - Excepcion:Excepción entrega activos para cancelar deuda --establecida_en--> TextoOrdenado:Texto Ordenado Exterior - Cambios
  - Excepcion:Excepción ventas títulos con liquidación plazo 10 días --establecida_en--> TextoOrdenado:Texto Ordenado Exterior - Cambios
  - Operacion:Pagos capital/intereses endeudamientos financieros --establecida_en--> TextoOrdenado:Texto Ordenado Exterior - Cambios
  - Operacion:Repatriaciones capital e inversiones directas --establecida_en--> TextoOrdenado:Texto Ordenado Exterior - Cambios
  - Operacion:Pagos capital/intereses títulos deuda emitidos --establecida_en--> TextoOrdenado:Texto Ordenado Exterior - Cambios
  - Operacion:Pagos refinanciaciones punto 3.5. --establecida_en--> TextoOrdenado:Texto Ordenado Exterior - Cambios
  - Operacion:Pagos refinanciaciones títulos no punto 3.5. --establecida_en--> TextoOrdenado:Texto Ordenado Exterior - Cambios
  - Obligacion:Presentación declaración utilización fondos inversiones --establecida_en--> TextoOrdenado:Texto Ordenado Exterior - Cambios
  - Excepcion:Excepción ventas/transferencias BOPREAL monto adquirido --establecida_en--> TextoOrdenado:Texto Ordenado Exterior - Cambios
  - Excepcion:Excepción ventas/transferencias BOPREAL importadores --establecida_en--> TextoOrdenado:Texto Ordenado Exterior - Cambios
  - Condicion:Condición utilización fondos en 10 días --establecida_en--> TextoOrdenado:Texto Ordenado Exterior - Cambios
  - Excepcion:Excepción transferencias a depositarias para canje --aplica_a--> None
  - Obligacion:Presentación certificación títulos canjeados --aplica_a--> cliente
  - Excepcion:Excepción entrega activos para cancelar deuda --aplica_a--> None
  - Excepcion:Excepción ventas títulos con liquidación plazo 10 días --aplica_a--> None
  - Obligacion:Presentación declaración utilización fondos inversiones --aplica_a--> cliente
  - Condicion:Condición utilización fondos en 10 días --condicion_de--> Excepcion:Excepción ventas títulos con liquidación plazo 10 días
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "cliente", "verificada": "exacta", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "cliente", "verificada": "exacta", "sujeto_id": null}]; omisiones []; condicion_de [{"de": "Condicion:Condición utilización fondos en 10 días", "a": "Excepcion:Excepción ventas títulos con liquidación plazo 10 días", "firma_nueva": false}]; limita []

**NUEVO** — error: None

- Excepcion «Excepción — transferencias a depositarias del exterior para canjes»: No se tienen en cuenta en la declaración jurada las transferencias de títulos valores a entidades depositarias del exterior realizadas o a realizar por el cliente con el objeto de participar de un canje o una operación de recompra de título… ‖ tramo (exacta): «las transferencias de títulos valores a entidades depositarias del exterior realizadas o a realizar por el cliente con el objeto de participar de un canje o una…»
- Obligacion «Presentación certificación de títulos canjeados»: El cliente deberá comprometerse a presentar la correspondiente certificación por los títulos de deuda canjeados. ‖ tramo (exacta): «El cliente deberá comprometerse a presentar la correspondiente certificación por los títulos de deuda canjeados»
- Excepcion «Excepción — entrega de activos para cancelación de deuda»: No se tienen en cuenta en la declaración jurada la entrega de activos locales con el objeto de cancelar una deuda con una agencia oficial de crédito o una entidad financiera del exterior, en la medida que se produzca a partir del vencimient… ‖ tramo (exacta): «la entrega de activos locales con el objeto de cancelar una deuda con una agencia oficial de crédito o una entidad financiera del exterior, en la medida que se …»
- Excepcion «Excepción — ventas de títulos con liquidación en moneda extranjera»: No se tienen en cuenta en la declaración jurada las ventas de títulos valores con liquidación en moneda extranjera en el país o en el exterior cuando la totalidad de los fondos obtenidos de tales liquidaciones se haya utilizado o será utili… ‖ tramo (exacta): «las ventas de títulos valores con liquidación en moneda extranjera en el país o en el exterior cuando la totalidad de los fondos obtenidos de tales liquidacione…»
- Condicion «Condición — pagos de capital de endeudamientos post 02/10/23»: Condición para la excepción de ventas de títulos valores: pagos de capital o intereses de nuevos endeudamientos financieros desembolsados a partir del 02/10/23 con al menos 1 año de gracia. ‖ tramo (exacta): «Pagos a partir del vencimiento de capital o intereses de nuevos endeudamientos financieros comprendidos en el punto 3.5., desembolsados a partir del 02/10/23 y …»
- Condicion «Condición — repatriaciones de inversiones directas post 02/10/23»: Condición para la excepción de ventas de títulos valores: repatriaciones de capital y rentas de inversiones directas de no residentes recibidas a partir del 02/10/23, con al menos 1 año posterior a la concreción del aporte. ‖ tramo (exacta): «Repatriaciones del capital y rentas asociadas a las inversiones directas de no residentes recibidas a partir del 02/10/23, en la medida que la repatriación se p…»
- Condicion «Condición — pagos de títulos públicos post 02/10/23»: Condición para la excepción de ventas de títulos valores: pagos de capital o intereses de títulos de deuda emitidos a partir del 02/10/23 con registro público, en moneda extranjera, con al menos 2 años de gracia. ‖ tramo (exacta): «Pagos a partir del vencimiento de capital o intereses de títulos de deuda emitidos a partir del 02/10/23 con registro público en el país no comprendidos en el p…»
- Condicion «Condición — refinanciaciones de endeudamientos punto 3.5»: Condición para la excepción de ventas de títulos valores: pagos de refinanciaciones de capital e intereses que no anticipen el vencimiento de la deuda original. ‖ tramo (exacta): «Pagos a partir del vencimiento de capital o intereses de endeudamientos financieros comprendidos en el punto 3.5. que no generen desembolsos por ser refinanciac…»
- Condicion «Condición — refinanciaciones de títulos públicos»: Condición para la excepción de ventas de títulos valores: pagos de refinanciaciones de títulos públicos en moneda extranjera que no anticipen el vencimiento original. ‖ tramo (exacta): «Pagos a partir del vencimiento de capital o intereses de títulos de emitidos con registro público en el país no comprendidos en el punto 3.5., denominados en mo…»
- Obligacion «Declaración jurada — utilización de fondos en inversiones»: En todos los casos el cliente debe presentar declaración jurada certificando que los fondos recibidos de las operaciones de pago, repatriación y títulos públicos se utilizaron en su totalidad para pagos en el país relacionados con inversion… ‖ tramo (exacta): «En todos los casos el cliente deberá presentar una declaración jurada dejando constancia de que los fondos oportunamente recibidos por las operaciones detallada…»
- Excepcion «Excepción — ventas de BOPREAL hasta monto suscrito»: No se tienen en cuenta en la declaración jurada las ventas o transferencias de BOPREAL realizadas por hasta el monto adquirido en la suscripción primaria. ‖ tramo (exacta): «las ventas con liquidación en moneda extranjera en el país o en el exterior de los Bonos para la Reconstrucción de una Argentina Libre (BOPREAL) o las transfere…»
- Excepcion «Excepción — ventas BOPREAL por importadores elegibles»: No se tienen en cuenta en la declaración jurada las ventas o transferencias de BOPREAL realizadas por importadores de bienes y servicios elegibles cuando el valor de mercado no supere la diferencia entre el valor obtenido en ventas anterior… ‖ tramo (exacta): «las ventas con liquidación en moneda extranjera en el exterior o las transferencias a depositarios del exterior que concreten los importadores de bienes y servi…»
  - Excepcion:Excepción — transferencias a depositarias del exterior para … --establecida_en--> TextoOrdenado:Texto Ordenado Exterior y Cambios
  - Obligacion:Presentación certificación de títulos canjeados --establecida_en--> TextoOrdenado:Texto Ordenado Exterior y Cambios
  - Excepcion:Excepción — entrega de activos para cancelación de deuda --establecida_en--> TextoOrdenado:Texto Ordenado Exterior y Cambios
  - Excepcion:Excepción — ventas de títulos con liquidación en moneda extr… --establecida_en--> TextoOrdenado:Texto Ordenado Exterior y Cambios
  - Condicion:Condición — pagos de capital de endeudamientos post 02/10/23 --establecida_en--> TextoOrdenado:Texto Ordenado Exterior y Cambios
  - Condicion:Condición — repatriaciones de inversiones directas post 02/1… --establecida_en--> TextoOrdenado:Texto Ordenado Exterior y Cambios
  - Condicion:Condición — pagos de títulos públicos post 02/10/23 --establecida_en--> TextoOrdenado:Texto Ordenado Exterior y Cambios
  - Condicion:Condición — refinanciaciones de endeudamientos punto 3.5 --establecida_en--> TextoOrdenado:Texto Ordenado Exterior y Cambios
  - Condicion:Condición — refinanciaciones de títulos públicos --establecida_en--> TextoOrdenado:Texto Ordenado Exterior y Cambios
  - Obligacion:Declaración jurada — utilización de fondos en inversiones --establecida_en--> TextoOrdenado:Texto Ordenado Exterior y Cambios
  - Excepcion:Excepción — ventas de BOPREAL hasta monto suscrito --establecida_en--> TextoOrdenado:Texto Ordenado Exterior y Cambios
  - Excepcion:Excepción — ventas BOPREAL por importadores elegibles --establecida_en--> TextoOrdenado:Texto Ordenado Exterior y Cambios
  - Excepcion:Excepción — transferencias a depositarias del exterior para … --aplica_a--> la entidad
  - Obligacion:Presentación certificación de títulos canjeados --aplica_a--> El cliente
  - Excepcion:Excepción — entrega de activos para cancelación de deuda --aplica_a--> la entidad
  - Excepcion:Excepción — ventas de títulos con liquidación en moneda extr… --aplica_a--> la entidad
  - Obligacion:Declaración jurada — utilización de fondos en inversiones --aplica_a--> el cliente
  - Excepcion:Excepción — ventas de BOPREAL hasta monto suscrito --aplica_a--> la entidad
  - Excepcion:Excepción — ventas BOPREAL por importadores elegibles --aplica_a--> la entidad
- hechos: umbrales [{"entidad": "Excepcion:Excepción — ventas de títulos con liquidación en moneda extr…", "tramo": "dentro de los 10 (diez) días corridos", "verificacion": "exacta"}, {"entidad": "Condicion:Condición — pagos de capital de endeudamientos post 02/10/23", "tramo": "desembolsados a partir del 02/10/23", "verificacion": "exacta"}, {"entidad": "Condicion:Condición — pagos de capital de endeudamientos post 02/10/23", "tramo": "contemplen como mínimo 1 (un) año de gracia para el pago de capital", "verificacion": "exacta"}, {"entidad": "Condicion:Condición — repatriaciones de inversiones directas post 02/1…", "tramo": "recibidas a partir del 02/10/23", "verificacion": "exacta"}, {"entidad": "Condicion:Condición — repatriaciones de inversiones directas post 02/1…", "tramo": "como mínimo 1 (un) año después de la concreción del aporte de capital", "verificacion": "exacta"}, {"entidad": "Condicion:Condición — pagos de títulos públicos post 02/10/23", "tramo": "emitidos a partir del 02/10/23", "verificacion": "exacta"}, {"entidad": "Condicion:Condición — pagos de títulos públicos post 02/10/23", "tramo": "contemplen como mínimo 2 (dos) años de gracia para el pago de capital", "verificacion": "exacta"}, {"entidad": "Excepcion:Excepción — ventas de BOPREAL hasta monto suscrito", "tramo": "por hasta el monto adquirido en la suscripción primaria", "verificacion": "exacta"}, {"entidad": "Excepcion:Excepción — ventas BOPREAL por importadores elegibles", "tramo": "cuando el valor de mercado de estas operaciones no supere a la diferencia entre el valor obtenido por la venta con liqui…", "verificacion": "exacta"}]; menciones [{"pred": "aplica_a", "mencion": "la entidad", "verificada": "exacta", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "El cliente", "verificada": "exacta", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "la entidad", "verificada": "exacta", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "la entidad", "verificada": "exacta", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "el cliente", "verificada": "exacta", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "la entidad", "verificada": "exacta", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "la entidad", "verificada": "exacta", "sujeto_id": null}]; omisiones [{"categoria": "relacion_sin_predicado", "tramo": "En las declaraciones juradas elaboradas para dar cumplimiento a los puntos 3.16.3.1. y 3.16.3.2. no …", "verificacion": "exacta", "nota": "La relación entre el encabezado que anuncia 'no deberán tenerse en cuenta' y cada excepción que sigu…"}]; condicion_de []; limita []

*Cuantías en el texto propio: 4.*

## Ficha 74 — `ric::11.1.1`

**Texto propio:**

```
11.1.1. Instrucciones generales para los cuadros 11.2.1 a) y b) y 11.2.2 a) y b).
Los citados flujos de fondos nocionales futuros se asignarán a 19 bandas temporales
predefinidas o sus puntos medios (tabla 1) para cada escenario de perturbación de
tasas de interés (tabla 2).
Deberá declararse en la partida 38000000 si se adopta la asignación de los flujos a
bandas temporales o a sus puntos medios, opción que debe mantenerse para todos
los cálculos del Marco Estandarizado y todas las posiciones de la entidad, de acuerdo
con la siguiente codificación:
1 = Asignación a banda temporales
2 = Asignación a puntos medios
Deberán informar los flujos asignados a todas las bandas o puntos medios para cada
uno de los escenarios previstos (0 a 6).
En la banda 0 (cero) se informarán los saldos a fin del último mes del trimestre.
Los importes se consignarán en valores absolutos.
Moneda:
La información se referirá a posiciones en pesos -cuadros 11.2.1 a) y 11.2.2 a)- y
en dólares estadounidenses -cuadros 11.2.1 b) y 11.2.2 b)-, siempre que se trate de
exposiciones relevantes (superiores al 5 % de los activos o pasivos de la cartera de
inversión), considerando lo indicado en el punto 1.2.
En caso que la entidad registre posiciones significativas en otras monedas distintas
de pesos o dólares estadounidenses, se incluirán dentro de la posición en esta última
moneda, previa aplicación del tipo de pase comunicado por la Mesa de Operaciones
del BCRA.
Coeficiente de actualización –cuadros 11.2.1. a) y 11.2.2. a)–.
1. No actualizable
2. CER
3. UVA/UVI:
Los saldos correspondientes a instrumentos actualizables por CER/UVA/UVI deberán
identificarse con el código respectivo, e imputarse a la banda 0 (saldos a fin de mes)
en su totalidad.
Márgenes comerciales:
Las entidades pueden optar por deducir los márgenes comerciales y otros componen-
tes del diferencial (spread), en cuyo caso:
• Si se incluyen los márgenes comerciales.
Solo se informarán los flujos y el factor de descuento continuo con margen (código
2)
• Si se deducen los márgenes.
Deberán informar los flujos y el factor de descuento continuo sin márgenes (código
1) y con márgenes (código 2).
Deberán informarse las partidas que registren importes, considerando los atributos
detallados precedentemente, indicados en los modelos de información de los cuadros
11.2.1. a) y b) y 11.2.2. a) y b) para cada una de ellas.
Cuando la estructura del modelo requiera datos en todos los escenarios (0 a 6) para
un concepto determinado, deberán consignarse los importes en todos ellos, aun
cuando no se registren variaciones.
Tabla 1.
[TABLA ric::tabla026 | página 48 | e0_tablas | posicional]
Fila 1: col1 = BANDAS TEMPORALES ⟨abarca hasta col23⟩
Fila 2: col4 = Tasas de corto plazo ⟨abarca hasta col12⟩ | col13 = Tasas de mediano plazo ⟨abarca hasta col17⟩ | col18 = Tasas de largo plazo ⟨abarca hasta col23⟩
Fila 3: col2 = Código de Ban- | col4 = 0 | col5 = 1 | col6 = 2 | col7 = 3 | col8 = 4 | col9 = 5 | col10 = 6 | col11 = 7 | col12 = 8 |
```
**Último bloque heredado:** Conceptos comprendidos. Se incluirán los flujos de fondos nocionales futuros sujetos a reapreciación de activos, pasi- vos y partidas fuera de balance sensibles a variaciones en la tasa de interés. Conceptos excluidos. - Activos que se deducen del capital ordinario del nivel 1 (COn1); - Activos fijo…

**SELLADO** — error: None

- Obligacion «Asignación de flujos a bandas o puntos medios»: Los citados flujos de fondos nocionales futuros se asignarán a 19 bandas temporales predefinidas o sus puntos medios (tabla 1) para cada escenario de perturbación de tasas de interés (tabla 2).
- Obligacion «Declaración en partida 38000000 de método de asignación»: Deberá declararse en la partida 38000000 si se adopta la asignación de los flujos a bandas temporales o a sus puntos medios, opción que debe mantenerse para todos los cálculos del Marco Estandarizado y todas las posiciones de la entidad, de…
- Obligacion «Informe de flujos para todos los escenarios»: Deberán informar los flujos asignados a todas las bandas o puntos medios para cada uno de los escenarios previstos (0 a 6).
- Obligacion «Informe de saldos en banda 0»: En la banda 0 (cero) se informarán los saldos a fin del último mes del trimestre.
- Obligacion «Expresión de importes en valores absolutos»: Los importes se consignarán en valores absolutos.
- Restriccion «Información en monedas relevantes: pesos y USD»: La información se referirá a posiciones en pesos -cuadros 11.2.1 a) y 11.2.2 a)- y en dólares estadounidenses -cuadros 11.2.1 b) y 11.2.2 b)-, siempre que se trate de exposiciones relevantes (superiores al 5 % de los activos o pasivos de la…
- Obligacion «Inclusión de posiciones en otras monedas al USD»: En caso que la entidad registre posiciones significativas en otras monedas distintas de pesos o dólares estadounidenses, se incluirán dentro de la posición en esta última moneda, previa aplicación del tipo de pase comunicado por la Mesa de …
- Obligacion «Identificación de instrumentos actualizables por CER/UVA/UVI»: Los saldos correspondientes a instrumentos actualizables por CER/UVA/UVI deberán identificarse con el código respectivo, e imputarse a la banda 0 (saldos a fin de mes) en su totalidad.
- Potestad «Opción de deducir márgenes comerciales»: Las entidades pueden optar por deducir los márgenes comerciales y otros componentes del diferencial (spread).
- Obligacion «Informe de flujos con margen cuando se incluyen»: Si se incluyen los márgenes comerciales, solo se informarán los flujos y el factor de descuento continuo con margen (código 2).
- Obligacion «Informe de flujos sin y con margen cuando se deducen»: Si se deducen los márgenes, deberán informar los flujos y el factor de descuento continuo sin márgenes (código 1) y con márgenes (código 2).
- Obligacion «Informe de partidas con importes»: Deberán informarse las partidas que registren importes, considerando los atributos detallados precedentemente, indicados en los modelos de información de los cuadros 11.2.1. a) y b) y 11.2.2. a) y b) para cada una de ellas.
- Obligacion «Consignación de importes en todos escenarios»: Cuando la estructura del modelo requiera datos en todos los escenarios (0 a 6) para un concepto determinado, deberán consignarse los importes en todos ellos, aun cuando no se registren variaciones.
  - Obligacion:Asignación de flujos a bandas o puntos medios --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Obligacion:Declaración en partida 38000000 de método de asignación --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Obligacion:Informe de flujos para todos los escenarios --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Obligacion:Informe de saldos en banda 0 --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Obligacion:Expresión de importes en valores absolutos --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Restriccion:Información en monedas relevantes: pesos y USD --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Obligacion:Inclusión de posiciones en otras monedas al USD --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Obligacion:Identificación de instrumentos actualizables por CER/UVA/UVI --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Potestad:Opción de deducir márgenes comerciales --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Obligacion:Informe de flujos con margen cuando se incluyen --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Obligacion:Informe de flujos sin y con margen cuando se deducen --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Obligacion:Informe de partidas con importes --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Obligacion:Consignación de importes en todos escenarios --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Obligacion:Asignación de flujos a bandas o puntos medios --aplica_a--> None
  - Obligacion:Declaración en partida 38000000 de método de asignación --aplica_a--> None
  - Obligacion:Informe de flujos para todos los escenarios --aplica_a--> None
  - Obligacion:Informe de saldos en banda 0 --aplica_a--> None
  - Restriccion:Información en monedas relevantes: pesos y USD --aplica_a--> None
  - Obligacion:Inclusión de posiciones en otras monedas al USD --aplica_a--> None
  - Obligacion:Identificación de instrumentos actualizables por CER/UVA/UVI --aplica_a--> None
  - Potestad:Opción de deducir márgenes comerciales --aplica_a--> None
  - Obligacion:Informe de flujos con margen cuando se incluyen --aplica_a--> None
  - Obligacion:Informe de flujos sin y con margen cuando se deducen --aplica_a--> None
  - Obligacion:Informe de partidas con importes --aplica_a--> None
  - Obligacion:Consignación de importes en todos escenarios --aplica_a--> None
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}]; omisiones [{"categoria": null, "tramo": "", "verificacion": "ausente", "nota": "Tabla 1 (BANDAS TEMPORALES): estructura tabular con códigos de banda (0-19), intervalos de tiempo y …"}, {"categoria": null, "tramo": "", "verificacion": "ausente", "nota": "Tabla 2 (ESCENARIOS): estructura tabular con códigos de escenario (0-6) y descripción de escenarios …"}]; condicion_de []; limita []

**NUEVO** — error: None

- Obligacion «Asignación de flujos a bandas temporales o puntos medios»: Se deben asignar los flujos de fondos nocionales futuros a 19 bandas temporales predefinidas o a sus puntos medios para cada escenario de perturbación de tasas de interés. ‖ tramo (exacta): «Los citados flujos de fondos nocionales futuros se asignarán a 19 bandas temporales predefinidas o sus puntos medios (tabla 1) para cada escenario de perturbaci…»
- Obligacion «Declaración de opción asignación — partida 38000000»: Debe declararse en la partida 38000000 si se adopta la asignación a bandas temporales (código 1) o a puntos medios (código 2). ‖ tramo (exacta): «Deberá declararse en la partida 38000000 si se adopta la asignación de los flujos a bandas temporales o a sus puntos medios»
- Condicion «Consistencia de opción asignación — todos los cálculos del Marco Estandarizado»: La opción elegida debe mantenerse para todos los cálculos del Marco Estandarizado y todas las posiciones de la entidad. ‖ tramo (exacta): «opción que debe mantenerse para todos los cálculos del Marco Estandarizado y todas las posiciones de la entidad»
- Obligacion «Información de flujos en todos los escenarios»: Deben informarse los flujos asignados a todas las bandas o puntos medios para cada escenario de perturbación de tasas de interés (escenarios 0 a 6). ‖ tramo (exacta): «Deberán informar los flujos asignados a todas las bandas o puntos medios para cada uno de los escenarios previstos (0 a 6).»
- Obligacion «Información de saldos en banda 0»: En la banda 0 se deben informar los saldos al fin del último mes de cada trimestre. ‖ tramo (exacta): «En la banda 0 (cero) se informarán los saldos a fin del último mes del trimestre.»
- Restriccion «Valores absolutos — importes»: Los importes deben consignarse en valores absolutos. ‖ tramo (exacta): «Los importes se consignarán en valores absolutos.»
- Restriccion «Cobertura de exposiciones relevantes — pesos»: La información en pesos aplica solo a exposiciones relevantes, superiores al 5 % de los activos o pasivos de la cartera de inversión. ‖ tramo (exacta): «La información se referirá a posiciones en pesos -cuadros 11.2.1 a) y 11.2.2 a)- [...] siempre que se trate de exposiciones relevantes (superiores al 5 % de los…»
- Restriccion «Cobertura de exposiciones relevantes — dólares estadounidenses»: La información en dólares estadounidenses aplica solo a exposiciones relevantes, superiores al 5 % de los activos o pasivos de la cartera de inversión. ‖ tramo (exacta): «La información se referirá a [...] en dólares estadounidenses -cuadros 11.2.1 b) y 11.2.2 b)-, siempre que se trate de exposiciones relevantes (superiores al 5 …»
- Obligacion «Conversión de otras monedas a dólares — tipo de pase»: Si la entidad registra posiciones significativas en otras monedas, deben incluirse en la posición en dólares estadounidenses, aplicando el tipo de pase comunicado por la Mesa de Operaciones del BCRA. ‖ tramo (exacta): «En caso que la entidad registre posiciones significativas en otras monedas distintas de pesos o dólares estadounidenses, se incluirán dentro de la posición en e…»
- Obligacion «Identificación de instrumentos CER/UVA/UVI — banda 0»: Los saldos de instrumentos actualizables por CER, UVA o UVI deben identificarse con el código correspondiente e imputarse íntegramente a la banda 0. ‖ tramo (exacta): «Los saldos correspondientes a instrumentos actualizables por CER/UVA/UVI deberán identificarse con el código respectivo, e imputarse a la banda 0 (saldos a fin …»
- Potestad «Opción deducción márgenes comerciales»: Las entidades pueden elegir deducir los márgenes comerciales y otros componentes del diferencial. ‖ tramo (exacta): «Las entidades pueden optar por deducir los márgenes comerciales y otros componentes del diferencial (spread)»
- Obligacion «Información de flujos — opción incluir márgenes»: Si se incluyen los márgenes comerciales, deben informarse solo los flujos y el factor de descuento continuo con margen (código 2). ‖ tramo (exacta): «Si se incluyen los márgenes comerciales. Solo se informarán los flujos y el factor de descuento continuo con margen (código 2)»
- Obligacion «Información de flujos — opción deducir márgenes»: Si se deducen los márgenes, deben informarse los flujos y el factor de descuento continuo tanto sin márgenes (código 1) como con márgenes (código 2). ‖ tramo (exacta): «Si se deducen los márgenes. Deberán informar los flujos y el factor de descuento continuo sin márgenes (código 1) y con márgenes (código 2).»
- Obligacion «Información de partidas — atributos detallados»: Deben informarse las partidas que registren importes, considerando los atributos detallados en los modelos de información de los cuadros especificados. ‖ tramo (exacta): «Deberán informarse las partidas que registren importes, considerando los atributos detallados precedentemente, indicados en los modelos de información de los cu…»
- Obligacion «Información en todos los escenarios — estructura requerida»: Cuando la estructura del modelo requiera datos en todos los escenarios (0 a 6) para un concepto, deben consignarse los importes en todos ellos, incluso si no hay variaciones. ‖ tramo (exacta): «Cuando la estructura del modelo requiera datos en todos los escenarios (0 a 6) para un concepto determinado, deberán consignarse los importes en todos ellos, au…»
- Definicion «Código asignación — bandas temporales»: Asignación de los flujos a bandas temporales predefinidas. ‖ tramo (exacta): «1 = Asignación a banda temporales»
- Definicion «Código asignación — puntos medios»: Asignación de los flujos a los puntos medios de las bandas temporales. ‖ tramo (exacta): «2 = Asignación a puntos medios»
  - Obligacion:Asignación de flujos a bandas temporales o puntos medios --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Obligacion:Declaración de opción asignación — partida 38000000 --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Condicion:Consistencia de opción asignación — todos los cálculos del M… --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Obligacion:Información de flujos en todos los escenarios --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Obligacion:Información de saldos en banda 0 --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Restriccion:Valores absolutos — importes --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Restriccion:Cobertura de exposiciones relevantes — pesos --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Restriccion:Cobertura de exposiciones relevantes — dólares estadounidens… --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Obligacion:Conversión de otras monedas a dólares — tipo de pase --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Obligacion:Identificación de instrumentos CER/UVA/UVI — banda 0 --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Potestad:Opción deducción márgenes comerciales --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Obligacion:Información de flujos — opción incluir márgenes --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Obligacion:Información de flujos — opción deducir márgenes --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Obligacion:Información de partidas — atributos detallados --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Obligacion:Información en todos los escenarios — estructura requerida --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Definicion:Código asignación — bandas temporales --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Definicion:Código asignación — puntos medios --establecida_en--> TextoOrdenado:Régimen Informativo Contable Mensual
  - Obligacion:Asignación de flujos a bandas temporales o puntos medios --aplica_a--> las entidades
  - Obligacion:Declaración de opción asignación — partida 38000000 --aplica_a--> la entidad
  - Obligacion:Información de flujos en todos los escenarios --aplica_a--> las entidades
  - Obligacion:Información de saldos en banda 0 --aplica_a--> las entidades
  - Restriccion:Valores absolutos — importes --aplica_a--> las entidades
  - Restriccion:Cobertura de exposiciones relevantes — pesos --aplica_a--> la entidad
  - Restriccion:Cobertura de exposiciones relevantes — dólares estadounidens… --aplica_a--> la entidad
  - Obligacion:Conversión de otras monedas a dólares — tipo de pase --aplica_a--> la entidad
  - Obligacion:Identificación de instrumentos CER/UVA/UVI — banda 0 --aplica_a--> las entidades
  - Potestad:Opción deducción márgenes comerciales --aplica_a--> Las entidades
  - Obligacion:Información de flujos — opción incluir márgenes --aplica_a--> las entidades
  - Obligacion:Información de flujos — opción deducir márgenes --aplica_a--> las entidades
  - Obligacion:Información de partidas — atributos detallados --aplica_a--> las entidades
  - Obligacion:Información en todos los escenarios — estructura requerida --aplica_a--> las entidades
  - Condicion:Consistencia de opción asignación — todos los cálculos del M… --condicion_de--> Obligacion:Declaración de opción asignación — partida 38000000
- hechos: umbrales [{"entidad": "Obligacion:Información de flujos en todos los escenarios", "tramo": "escenarios previstos (0 a 6)", "verificacion": "exacta"}, {"entidad": "Restriccion:Cobertura de exposiciones relevantes — pesos", "tramo": "superiores al 5 % de los activos o pasivos de la cartera de inversión", "verificacion": "exacta"}, {"entidad": "Restriccion:Cobertura de exposiciones relevantes — dólares estadounidens…", "tramo": "superiores al 5 % de los activos o pasivos de la cartera de inversión", "verificacion": "exacta"}, {"entidad": "Obligacion:Información en todos los escenarios — estructura requerida", "tramo": "escenarios (0 a 6)", "verificacion": "exacta"}]; menciones [{"pred": "aplica_a", "mencion": "las entidades", "verificada": "exacta", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "la entidad", "verificada": "exacta", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "las entidades", "verificada": "exacta", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "las entidades", "verificada": "exacta", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "las entidades", "verificada": "exacta", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "la entidad", "verificada": "exacta", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "la entidad", "verificada": "exacta", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "la entidad", "verificada": "exacta", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "las entidades", "verificada": "exacta", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "Las entidades", "verificada": "exacta", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "las entidades", "verificada": "exacta", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "las entidades", "verificada": "exacta", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "las entidades", "verificada": "exacta", "sujeto_id": null}, {"pred": "aplica_a", "mencion": "las entidades", "verificada": "exacta", "sujeto_id": null}]; omisiones [{"categoria": "formula", "tramo": "evidencia: 1 = Asignación a banda temporales; evidencia: 2 = Asignación a puntos medios", "verificacion": "no", "nota": "FLAGS E0 declara contenido de fórmulas como NO-CONFIABLE; se registra la referencia a la codificació…"}, {"categoria": "tabla", "tramo": "[TABLA ric::tabla026 | Tabla 1: Bandas temporales con código de banda, intervalos de tiempo, punto m…", "verificacion": "no", "nota": "Tabla serializada confiable por E0 pero su contenido es estructura de datos de referencia (intervalo…"}, {"categoria": "tabla", "tramo": "[TABLA ric::tabla027 | Tabla 2: Escenarios de perturbación de tasas de interés con códigos 0 a 6]", "verificacion": "no", "nota": "Tabla serializada confiable por E0 documenta los 6 escenarios de perturbación (0=Base, 1=Despl. para…"}]; condicion_de [{"de": "Condicion:Consistencia de opción asignación — todos los cálculos del M…", "a": "Obligacion:Declaración de opción asignación — partida 38000000", "firma_nueva": false}]; limita []

*Cuantías en el texto propio: 3.*

## Ficha 75 — `cla::5.1.1.1`

**Texto propio:**

```
5.1.1.1. Los créditos para consumo o vivienda.
Los créditos de esta clase que superen el equivalente a dos veces el importe de
referencia establecido en el punto 3.7. y cuyo repago no se encuentre vinculado
a ingresos fijos o periódicos del cliente sino a la evolución de su actividad pro-
ductiva o comercial se incluirán dentro de la cartera comercial.
```
**Último bloque heredado:** Abarca todas las financiaciones comprendidas, con excepción de las siguientes:

**SELLADO** — error: None

- Definicion «Cartera comercial — créditos consumo/vivienda»: Los créditos para consumo o vivienda que superen el equivalente a dos veces el importe de referencia establecido en el punto 3.7. y cuyo repago no se encuentre vinculado a ingresos fijos o periódicos del cliente sino a la evolución de su ac…
- Condicion «Monto supera dos veces importe referencia 3.7»: que superen el equivalente a dos veces el importe de referencia establecido en el punto 3.7
- Condicion «Repago vinculado a actividad productiva/comercial»: cuyo repago no se encuentre vinculado a ingresos fijos o periódicos del cliente sino a la evolución de su actividad productiva o comercial
- Operacion «Clasificación de crédito en cartera comercial»: inclusión de créditos para consumo o vivienda en la cartera comercial
  - Definicion:Cartera comercial — créditos consumo/vivienda --establecida_en--> TextoOrdenado:Clasificación de deudores
  - Condicion:Monto supera dos veces importe referencia 3.7 --condicion_de--> Operacion:Clasificación de crédito en cartera comercial
  - Condicion:Repago vinculado a actividad productiva/comercial --condicion_de--> Operacion:Clasificación de crédito en cartera comercial
  - Operacion:Clasificación de crédito en cartera comercial --establecida_en--> TextoOrdenado:Clasificación de deudores
  - Operacion:Clasificación de crédito en cartera comercial --aplica_a--> None
- hechos: umbrales []; menciones [{"pred": "aplica_a", "mencion": "", "verificada": "ausente", "sujeto_id": null}]; omisiones []; condicion_de [{"de": "Condicion:Monto supera dos veces importe referencia 3.7", "a": "Operacion:Clasificación de crédito en cartera comercial", "firma_nueva": true}, {"de": "Condicion:Repago vinculado a actividad productiva/comercial", "a": "Operacion:Clasificación de crédito en cartera comercial", "firma_nueva": true}]; limita []

**NUEVO** — error: None

- Operacion «Créditos para consumo o vivienda»: Créditos destinados a consumo o vivienda, susceptibles de inclusión en cartera comercial bajo condiciones específicas ‖ tramo (exacta): «Los créditos para consumo o vivienda»
- Condicion «Monto superior a dos veces importe de referencia»: El repago del crédito no está vinculado a ingresos fijos o periódicos del cliente, sino a la evolución de su actividad productiva o comercial ‖ tramo (exacta): «cuyo repago no se encuentre vinculado a ingresos fijos o periódicos del cliente sino a la evolución de su actividad productiva o comercial»
- Operacion «Inclusión en cartera comercial»: Los créditos para consumo o vivienda que cumplen condiciones específicas deben incluirse en la cartera comercial ‖ tramo (exacta): «se incluirán dentro de la cartera comercial»
  - Operacion:Créditos para consumo o vivienda --establecida_en--> TextoOrdenado:Clasificación de Deudores
  - Condicion:Monto superior a dos veces importe de referencia --establecida_en--> TextoOrdenado:Clasificación de Deudores
  - Operacion:Inclusión en cartera comercial --establecida_en--> TextoOrdenado:Clasificación de Deudores
  - Condicion:Monto superior a dos veces importe de referencia --condicion_de--> Operacion:Inclusión en cartera comercial
- hechos: umbrales [{"entidad": "Condicion:Monto superior a dos veces importe de referencia", "tramo": "superen el equivalente a dos veces el importe de referencia establecido en el punto 3.7.", "verificacion": "exacta"}]; menciones []; omisiones [{"categoria": "meta_normativo", "tramo": "Abarca todas las financiaciones comprendidas, con excepción de las siguientes", "verificacion": "no", "nota": "Enunciado de alcance que predica sobre la estructura de categorización de cartera, no sobre conducta…"}]; condicion_de [{"de": "Condicion:Monto superior a dos veces importe de referencia", "a": "Operacion:Inclusión en cartera comercial", "firma_nueva": true}]; limita []

*Cuantías en el texto propio: 1.*

## Ficha 76 — `cap::8.5.1`

**Texto propio:**

```
8.5.1. CO : importe resultante de multiplicar 4,5% por los APR.
n1
```
**Último bloque heredado:** La falta de cumplimiento de cualquiera de estos límites mínimos será considerada incumpli- miento de integración del capital mínimo, correspondiendo la aplicación de lo previsto por el punto 1.4. de estas normas y la Sección 1. de las normas sobre “Incumplimientos de capitales mínimos y relaciones t…

**SELLADO** — error: None

- Definicion «CO: importe resultante de multiplicar 4,5% por APR»: importe resultante de multiplicar 4,5% por los APR
  - Definicion:CO: importe resultante de multiplicar 4,5% por APR --establecida_en--> TextoOrdenado:Capitales Mínimos
- hechos: umbrales []; menciones []; omisiones []; condicion_de []; limita []

**NUEVO** — error: None

- Definicion «CO — capital operacional mínimo»: importe resultante de multiplicar 4,5% por los APR ‖ tramo (exacta): «CO : importe resultante de multiplicar 4,5% por los APR.»
- Restriccion «Tope CO — 4,5% de activos ponderados por riesgo»: El capital operacional computable no podrá ser inferior a un importe igual al 4,5% de los activos ponderados por riesgo ‖ tramo (exacta): «importe resultante de multiplicar 4,5% por los APR.»
  - Definicion:CO — capital operacional mínimo --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Restriccion:Tope CO — 4,5% de activos ponderados por riesgo --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Restriccion:Tope CO — 4,5% de activos ponderados por riesgo --aplica_a--> las entidades
- hechos: umbrales [{"entidad": "Restriccion:Tope CO — 4,5% de activos ponderados por riesgo", "tramo": "4,5% por los APR", "verificacion": "exacta"}]; menciones [{"pred": "aplica_a", "mencion": "las entidades", "verificada": "no", "sujeto_id": null}]; omisiones [{"categoria": "fuera_de_tipos", "tramo": "Los activos ponderados por riesgo (APR) resultan de aplicar la siguiente expresión: APR = APR + [(RM…", "verificacion": "no", "nota": "Fórmula de cálculo de APR: es un procedimiento matemático que define cómo se compone APR, no una pre…"}]; condicion_de []; limita []

*Cuantías en el texto propio: 1.*

