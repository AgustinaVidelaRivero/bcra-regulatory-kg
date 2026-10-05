# Fichas de P4b (cegadas: sin grupo ni origen)

Orden: random.Random('U-PROMPT-R2:P4b:2026-10-04:fichas').shuffle sobre los 27 ids ordenados. ANTERIOR = prefijo `3817de475c93` con el código de `44c6e1b`; P3C = prefijo `322c5a23e9b7` con el código de `bb212f1`; la misma e0-r2b; las dos salidas, validadas con el validador de `bb212f1`.

## Ficha 1 — `ctacte::3.2.4`

**Texto propio:**

```
3.2.4. Que contengan inscripciones de propaganda.
```
**Heredado:** Sección 3. Cheques. / 3.2. Títulos que carecen de valor como cheques. / El título respecto del que se presentare alguna de las siguientes situaciones, enumeradas taxativamente a continuación, no valdrá como cheque: / Los títulos devueltos por esas situaciones no podrán ser objeto de nuevas presentaciones.

**ANTERIOR** — error: None; salida: 610 tokens

- Restriccion «Cheques con propaganda — valor nulo»: Los títulos que contengan inscripciones de propaganda no valdrán como cheques ‖ tramo (exacta): «Que contengan inscripciones de propaganda»
- Operacion «Uso como cheque»: Utilización de un título como cheque ‖ tramo (exacta): «valdrá como cheque»
  - Restriccion:Cheques con propaganda — valor nulo --establecida_en--> TextoOrdenado:Cuentas de Corresponsalía
  - Restriccion:Cheques con propaganda — valor nulo --prohibe--> Operacion:Uso como cheque
  - Restriccion:Cheques con propaganda — valor nulo --aplica_a--> Los títulos
  - omisión meta_normativo (exacta): «no podrán ser objeto de nuevas presentaciones» — nota: Cláusula de efecto jurídico derivado de la situación tipificada en 3.2.4; enunciada en el cierre de 3.2, no en el punto
  - heredado_compuesto: 0

**P3C** — error: None; salida: 433 tokens

- Restriccion «Prohibición — cheques con inscripciones de propaganda»: Los cheques que contengan inscripciones de propaganda no valen como cheques y no podrán ser objeto de nuevas presentaciones ‖ tramo (exacta): «Que contengan inscripciones de propaganda»
  - Restriccion:Prohibición — cheques con inscripciones de propaganda --establecida_en--> TextoOrdenado:Cuentas de corresponsalía
  - rechazo: ref_colgante: relations[1] (prohibe): source='e1' target='e2'
  - omisión meta_normativo (exacta): «no valdrá como cheque» — nota: Declaración de significado/efecto jurídico que el contenido de la Restriccion ya expresa; la prohibición ya captura que no vale como cheque
  - heredado_compuesto: 0

## Ficha 2 — `cap::5.3.1.3`

**Texto propio:**

```
5.3.1.3. Excepciones a la aplicación del ponderador de riesgo mínimo.
El ponderador de riesgo de la parte de la exposición cubierta podrá ser inferior
al 20% en los siguientes casos:
i) Las operaciones de pase estarán sujetas a un ponderador de riesgo del 0%
cuando la contraparte sea un “participante esencial del mercado” (punto
5.3.1.4.) y, además, se satisfaga la totalidad de las siguientes condiciones:
a) La exposición y el activo recibido en garantía consisten en efectivo o en
títulos valores emitidos por el sector público no financiero sujetos a un
ponderador de riesgo del 0%.
b) La exposición y el activo recibido en garantía estén denominados en la
misma moneda.
c) El plazo de vencimiento de la operación sea de un día hábil o bien la ex-
posición y el activo recibido en garantía se valúen diariamente a precios
de mercado y estén sujetos a liquidación/reposición diaria de márgenes.
d) Cuando una de las partes incumpla la liquidación/reposición de márge-
nes, el tiempo exigido entre la última valuación a precio de mercado pre-
via al incumplimiento y la liquidación del activo no supere los cuatro días
hábiles.
e) La operación se liquide a través de un sistema previamente comprobado
para este tipo de operaciones.
f) La documentación de la operación sea la documentación estándar para
las operaciones de pase con los títulos valores en cuestión.
g) La documentación de la operación contemple que, en el caso de que
una de las partes incumpla la obligación de entregar efectivo o títulos va-
lores o de reponer el margen o cualquier otra obligación, la operación se-
rá inmediatamente cancelable.
h) Ante cualquier evento de incumplimiento, la entidad financiera conserve
el derecho irrestricto y legalmente exigible de tomar inmediatamente po-
sesión del activo y liquidarlo para cobrar sus acreencias.
ii) Las operaciones de pase en las cuales la contraparte no sea un “participan-
te esencial del mercado” (punto 5.3.1.4.), pero que satisfagan las restantes
condiciones establecidas en el acápite i), estarán sujetas a un ponderador
de riesgo del 10%.
iii) Las operaciones en las que la exposición y el activo recibido en garantía es-
tén denominados en la misma moneda y el mencionado activo recibido sea
efectivo depositado en la entidad financiera, o títulos valores emitidos por el
sector público no financiero o instrumentos de regulación monetaria emitidos
por el BCRA a los que les corresponda un ponderador de riesgo del 0% y a
cuyo valor de mercado se le haya aplicado un aforo de al menos el 20%, es-
tarán sujetas a un ponderador de riesgo del 0%.
```
**Heredado:** Sección 5. Cobertura del riesgo de crédito. / A los efectos del cómputo de la exigencia de capital por riesgo de crédito, se reconocerá –total o parcialmente– la cobertura del riesgo de crédito (CRC) de las operaciones registradas en la cartera de inversión –tales como préstamos y responsabilidades eventu… / 5.3. Operaciones cubiertas con activos admitidos como garantía. / La aplicación de la técnica de cobertura mediante activos admitidos como garantía dependerá del método elegido. / 5.3.1. Método simple. / Con este método, el ponderador de riesgo de la contraparte se sustituye por el pondera- dor de riesgo del activo mediante el cual se cubre –parcial o totalmente– la exposición –conforme a la tabla de ponderadores prevista en la Sección 2.–.

**ANTERIOR** — error: None; salida: 4769 tokens

- Restriccion «Ponderador mínimo inferior al 20% — excepciones»: El ponderador de riesgo de la parte de la exposición cubierta podrá ser inferior al 20% en los siguientes casos. ‖ tramo (exacta): «El ponderador de riesgo de la parte de la exposición cubierta podrá ser inferior al 20% en los siguientes casos:» ‖ umbrales: ['inferior al 20%']
- Operacion «Operación de pase — participante esencial del mercado»: Operación de pase con contraparte que sea participante esencial del mercado, sujeta a ponderador de riesgo del 0%. ‖ tramo (exacta): «Las operaciones de pase estarán sujetas a un ponderador de riesgo del 0% cuando la contraparte sea un "participante esencial del mercado"»
- Condicion «Contraparte es participante esencial del mercado»: La contraparte de la operación de pase debe ser un participante esencial del mercado. ‖ tramo (exacta): «cuando la contraparte sea un "participante esencial del mercado"»
- Condicion «Exposición y garantía en efectivo o títulos sector público 0%»: La exposición y el activo recibido en garantía deben consistir en efectivo o en títulos valores emitidos por el sector público no financiero con ponderador de riesgo del 0%. ‖ tramo (exacta): «La exposición y el activo recibido en garantía consisten en efectivo o en títulos valores emitidos por el sector público no financiero sujetos a un ponderador de riesgo del 0%.»
- Condicion «Exposición y garantía en igual moneda»: La exposición y el activo recibido en garantía deben estar denominados en la misma moneda. ‖ tramo (exacta): «La exposición y el activo recibido en garantía estén denominados en la misma moneda.»
- Condicion «Plazo un día hábil o revaluación y márgenes diarios»: El plazo de vencimiento debe ser de un día hábil, o la exposición y el activo recibido en garantía deben valuarse diariamente a precios de mercado con liquidación/reposición diaria de márgenes. ‖ tramo (exacta): «El plazo de vencimiento de la operación sea de un día hábil o bien la exposición y el activo recibido en garantía se valúen diariamente a precios de mercado y estén sujetos a liquidación/reposición di…» ‖ umbrales: ['un día hábil']
- Condicion «Liquidación de activo dentro de cuatro días hábiles»: Ante incumplimiento de liquidación/reposición de márgenes, el tiempo entre la última valuación a precio de mercado y la liquidación del activo no debe superar cuatro días hábiles. ‖ tramo (exacta): «Cuando una de las partes incumpla la liquidación/reposición de márgenes, el tiempo exigido entre la última valuación a precio de mercado previa al incumplimiento y la liquidación del activo no supere …» ‖ umbrales: ['no supere los cuatro días hábiles']
- Condicion «Liquidación a través de sistema comprobado»: La operación debe liquidarse a través de un sistema previamente comprobado para operaciones de pase. ‖ tramo (exacta): «La operación se liquide a través de un sistema previamente comprobado para este tipo de operaciones.»
- Condicion «Documentación estándar para operaciones de pase»: La documentación de la operación debe ser la documentación estándar para operaciones de pase con los títulos valores respectivos. ‖ tramo (exacta): «La documentación de la operación sea la documentación estándar para las operaciones de pase con los títulos valores en cuestión.»
- Condicion «Cláusula de cancelación inmediata ante incumplimiento»: La documentación debe contemplar que ante incumplimiento de obligaciones (entrega de efectivo, títulos o margen), la operación será inmediatamente cancelable. ‖ tramo (exacta): «La documentación de la operación contemple que, en el caso de que una de las partes incumpla la obligación de entregar efectivo o títulos valores o de reponer el margen o cualquier otra obligación, la…»
- Condicion «Derecho irrestricto de tomar posesión y liquidar activo»: Ante incumplimiento, la entidad financiera debe conservar el derecho irrestricto y legalmente exigible de tomar inmediatamente posesión del activo y liquidarlo. ‖ tramo (exacta): «Ante cualquier evento de incumplimiento, la entidad financiera conserve el derecho irrestricto y legalmente exigible de tomar inmediatamente posesión del activo y liquidarlo para cobrar sus acreencias…»
- Restriccion «Ponderador 0% — operaciones de pase con participante esencial»: Las operaciones de pase con participante esencial del mercado que cumplan todas las condiciones establecidas estarán sujetas a un ponderador de riesgo del 0%. ‖ tramo (exacta): «Las operaciones de pase estarán sujetas a un ponderador de riesgo del 0%» ‖ umbrales: ['ponderador de riesgo del 0%']
- Restriccion «Ponderador 10% — operaciones de pase sin participante esencial»: Las operaciones de pase cuya contraparte no sea participante esencial del mercado, pero que satisfagan las restantes condiciones, estarán sujetas a un ponderador de riesgo del 10%. ‖ tramo (exacta): «Las operaciones de pase en las cuales la contraparte no sea un "participante esencial del mercado" [...] estarán sujetas a un ponderador de riesgo del 10%.» ‖ umbrales: ['ponderador de riesgo del 10%']
- Condicion «Contraparte no es participante esencial del mercado»: La contraparte de la operación de pase no es un participante esencial del mercado. ‖ tramo (exacta): «la contraparte no sea un "participante esencial del mercado"»
- Restriccion «Ponderador 0% — operaciones con efectivo o títulos sector público»: Operaciones con exposición y garantía en igual moneda, donde la garantía sea efectivo depositado en la entidad, o títulos valores del sector público no financiero o instrumentos de regulación monetaria del BCRA (con ponderador 0% y aforo de al menos 20%) estarán sujetas a ponderador de riesgo del 0%… ‖ tramo (exacta): «Las operaciones en las que la exposición y el activo recibido en garantía estén denominados en la misma moneda y el mencionado activo recibido sea efectivo depositado en la entidad financiera, o títul…» ‖ umbrales: ['ponderador de riesgo del 0%', 'aforo de al menos el 20%']
- Condicion «Garantía en efectivo o títulos SPNF/instrumentos regulación monetaria BCRA»: El activo recibido en garantía debe ser: efectivo depositado en la entidad financiera, o títulos valores del sector público no financiero, o instrumentos de regulación monetaria del BCRA con ponderador 0% y aforo de al menos 20%. ‖ tramo (exacta): «el mencionado activo recibido sea efectivo depositado en la entidad financiera, o títulos valores emitidos por el sector público no financiero o instrumentos de regulación monetaria emitidos por el BC…» ‖ umbrales: ['aforo de al menos el 20%']
  - Restriccion:Ponderador mínimo inferior al 20% — excepciones --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Restriccion:Ponderador 0% — operaciones de pase con participante esencial --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Restriccion:Ponderador 10% — operaciones de pase sin participante esencial --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Restriccion:Ponderador 0% — operaciones con efectivo o títulos sector público --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Condicion:Contraparte es participante esencial del mercado --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Condicion:Exposición y garantía en efectivo o títulos sector público 0% --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Condicion:Exposición y garantía en igual moneda --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Condicion:Plazo un día hábil o revaluación y márgenes diarios --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Condicion:Liquidación de activo dentro de cuatro días hábiles --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Condicion:Liquidación a través de sistema comprobado --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Condicion:Documentación estándar para operaciones de pase --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Condicion:Cláusula de cancelación inmediata ante incumplimiento --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Condicion:Derecho irrestricto de tomar posesión y liquidar activo --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Condicion:Contraparte no es participante esencial del mercado --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Condicion:Garantía en efectivo o títulos SPNF/instrumentos regulación monetaria … --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Restriccion:Ponderador 0% — operaciones de pase con participante esencial --limita--> Operacion:Operación de pase — participante esencial del mercado
  - Condicion:Contraparte es participante esencial del mercado --condicion_de--> Restriccion:Ponderador 0% — operaciones de pase con participante esencial
  - Condicion:Exposición y garantía en efectivo o títulos sector público 0% --condicion_de--> Restriccion:Ponderador 0% — operaciones de pase con participante esencial
  - Condicion:Exposición y garantía en igual moneda --condicion_de--> Restriccion:Ponderador 0% — operaciones de pase con participante esencial
  - Condicion:Plazo un día hábil o revaluación y márgenes diarios --condicion_de--> Restriccion:Ponderador 0% — operaciones de pase con participante esencial
  - Condicion:Liquidación de activo dentro de cuatro días hábiles --condicion_de--> Restriccion:Ponderador 0% — operaciones de pase con participante esencial
  - Condicion:Liquidación a través de sistema comprobado --condicion_de--> Restriccion:Ponderador 0% — operaciones de pase con participante esencial
  - Condicion:Documentación estándar para operaciones de pase --condicion_de--> Restriccion:Ponderador 0% — operaciones de pase con participante esencial
  - Condicion:Cláusula de cancelación inmediata ante incumplimiento --condicion_de--> Restriccion:Ponderador 0% — operaciones de pase con participante esencial
  - Condicion:Derecho irrestricto de tomar posesión y liquidar activo --condicion_de--> Restriccion:Ponderador 0% — operaciones de pase con participante esencial
  - Condicion:Contraparte no es participante esencial del mercado --condicion_de--> Restriccion:Ponderador 10% — operaciones de pase sin participante esencial
  - Condicion:Exposición y garantía en igual moneda --condicion_de--> Restriccion:Ponderador 0% — operaciones con efectivo o títulos sector público
  - Condicion:Garantía en efectivo o títulos SPNF/instrumentos regulación monetaria … --condicion_de--> Restriccion:Ponderador 0% — operaciones con efectivo o títulos sector público
  - omisión fuera_de_tipos (exacta): «punto 5.3.1.4.» — nota: Remisión a otro punto normativo del documento (definición de 'participante esencial del mercado'). La remisión la registra el código desde e…
  - heredado_compuesto: 0

**P3C** — error: None; salida: 4663 tokens

- Restriccion «Ponderador mínimo del 20% — cobertura con activos»: El ponderador de riesgo de la parte de la exposición cubierta no podrá ser inferior al 20%, salvo en los casos especificados. ‖ tramo (exacta): «El ponderador de riesgo de la parte de la exposición cubierta podrá ser inferior al 20% en los siguientes casos:» ‖ umbrales: ['inferior al 20%']
- Operacion «Operaciones de pase — participante esencial — ponderador 0%»: Operación de pase cuya contraparte es un participante esencial del mercado, cubierta con activos admitidos y sujeta a ponderador de riesgo del 0%. ‖ tramo (exacta): «Las operaciones de pase estarán sujetas a un ponderador de riesgo del 0% cuando la contraparte sea un "participante esencial del mercado"»
- Condicion «Exposición y garantía en efectivo o títulos públicos 0%»: La exposición y el activo garantía son efectivo o títulos del sector público no financiero con ponderador 0%. ‖ tramo (exacta): «La exposición y el activo recibido en garantía consisten en efectivo o en títulos valores emitidos por el sector público no financiero sujetos a un ponderador de riesgo del 0%.»
- Condicion «Exposición y garantía en la misma moneda»: La exposición y el activo recibido en garantía deben estar denominados en la misma moneda. ‖ tramo (exacta): «La exposición y el activo recibido en garantía estén denominados en la misma moneda.»
- Condicion «Plazo de vencimiento un día hábil o revaluación diaria»: Plazo de vencimiento de un día hábil, o revaluación diaria a precios de mercado con liquidación/reposición diaria de márgenes. ‖ tramo (exacta): «El plazo de vencimiento de la operación sea de un día hábil o bien la exposición y el activo recibido en garantía se valúen diariamente a precios de mercado y estén sujetos a liquidación/reposición di…» ‖ umbrales: ['de un día hábil', 'diariamente']
- Condicion «Liquidación de activo dentro de cuatro días hábiles»: Ante incumplimiento de márgenes, el plazo desde última revaluación a liquidación del activo no supera cuatro días hábiles. ‖ tramo (exacta): «Cuando una de las partes incumpla la liquidación/reposición de márgenes, el tiempo exigido entre la última valuación a precio de mercado previa al incumplimiento y la liquidación del activo no supere …» ‖ umbrales: ['no supere los cuatro días hábiles']
- Condicion «Liquidación a través de sistema comprobado»: La operación se liquida a través de un sistema previamente comprobado para operaciones de pase. ‖ tramo (exacta): «La operación se liquide a través de un sistema previamente comprobado para este tipo de operaciones.»
- Condicion «Documentación estándar para operaciones de pase»: La documentación de la operación es la documentación estándar para operaciones de pase con los títulos valores involucrados. ‖ tramo (exacta): «La documentación de la operación sea la documentación estándar para las operaciones de pase con los títulos valores en cuestión.»
- Condicion «Cancelación inmediata ante incumplimiento»: La documentación prevé cancelación inmediata de la operación ante incumplimiento de obligaciones de entregar efectivo, títulos o márgenes. ‖ tramo (exacta): «La documentación de la operación contemple que, en el caso de que una de las partes incumpla la obligación de entregar efectivo o títulos valores o de reponer el margen o cualquier otra obligación, la…»
- Condicion «Derecho de tomar posesión e liquidar activo»: La entidad financiera tiene derecho irrestricto y legalmente exigible de tomar inmediatamente posesión del activo y liquidarlo ante incumplimiento. ‖ tramo (exacta): «Ante cualquier evento de incumplimiento, la entidad financiera conserve el derecho irrestricto y legalmente exigible de tomar inmediatamente posesión del activo y liquidarlo para cobrar sus acreencias…»
- Operacion «Operaciones de pase — participante no esencial — ponderador 10%»: Operación de pase cuya contraparte no es un participante esencial del mercado, que satisface condiciones del acápite i), sujeta a ponderador de riesgo del 10%. ‖ tramo (no): «Las operaciones de pase en las cuales la contraparte no sea un "participante esencial del mercado" pero que satisfagan las restantes condiciones establecidas en el acápite i), estarán sujetas a un pon…»
- Operacion «Operaciones con garantía en efectivo o títulos públicos — ponderador 0%»: Operación cubierta con garantía (efectivo, títulos públicos o instrumentos monetarios del BCRA con ponderador 0% e aforo mínimo 20%), en la misma moneda, sujeta a ponderador 0%. ‖ tramo (exacta): «Las operaciones en las que la exposición y el activo recibido en garantía estén denominados en la misma moneda y el mencionado activo recibido sea efectivo depositado en la entidad financiera, o títul…»
- Excepcion «Excepción ponderador mínimo — operaciones de pase esencial»: El ponderador mínimo del 20% no aplica a operaciones de pase cuya contraparte es participante esencial del mercado; se aplica ponderador 0%. ‖ tramo (exacta): «El ponderador de riesgo de la parte de la exposición cubierta podrá ser inferior al 20% en los siguientes casos: i) Las operaciones de pase estarán sujetas a un ponderador de riesgo del 0% cuando la c…» ‖ umbrales: ['0%']
- Excepcion «Excepción ponderador mínimo — operaciones de pase no esencial»: El ponderador mínimo del 20% no aplica a operaciones de pase sin participante esencial que cumplen condiciones del acápite i); se aplica ponderador 10%. ‖ tramo (no): «Las operaciones de pase en las cuales la contraparte no sea un "participante esencial del mercado" pero que satisfagan las restantes condiciones establecidas en el acápite i), estarán sujetas a un pon…» ‖ umbrales: ['10%']
- Excepcion «Excepción ponderador mínimo — garantía efectivo/público con aforo»: El ponderador mínimo del 20% no aplica a operaciones cubierta con efectivo, títulos públicos o instrumentos monetarios BCRA (0%) con aforo mínimo 20%, misma moneda; se aplica ponderador 0%. ‖ tramo (exacta): «Las operaciones en las que la exposición y el activo recibido en garantía estén denominados en la misma moneda y el mencionado activo recibido sea efectivo depositado en la entidad financiera, o títul…» ‖ umbrales: ['aforo de al menos el 20%', '0%']
  - Restriccion:Ponderador mínimo del 20% — cobertura con activos --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Operacion:Operaciones de pase — participante esencial — ponderador 0% --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Condicion:Exposición y garantía en efectivo o títulos públicos 0% --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Condicion:Exposición y garantía en la misma moneda --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Condicion:Plazo de vencimiento un día hábil o revaluación diaria --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Condicion:Liquidación de activo dentro de cuatro días hábiles --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Condicion:Liquidación a través de sistema comprobado --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Condicion:Documentación estándar para operaciones de pase --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Condicion:Cancelación inmediata ante incumplimiento --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Condicion:Derecho de tomar posesión e liquidar activo --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Operacion:Operaciones de pase — participante no esencial — ponderador 10% --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Operacion:Operaciones con garantía en efectivo o títulos públicos — ponderador 0… --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Excepcion:Excepción ponderador mínimo — operaciones de pase esencial --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Excepcion:Excepción ponderador mínimo — operaciones de pase no esencial --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Excepcion:Excepción ponderador mínimo — garantía efectivo/público con aforo --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Excepcion:Excepción ponderador mínimo — operaciones de pase esencial --exceptua--> Restriccion:Ponderador mínimo del 20% — cobertura con activos
  - Excepcion:Excepción ponderador mínimo — operaciones de pase no esencial --exceptua--> Restriccion:Ponderador mínimo del 20% — cobertura con activos
  - Excepcion:Excepción ponderador mínimo — garantía efectivo/público con aforo --exceptua--> Restriccion:Ponderador mínimo del 20% — cobertura con activos
  - Condicion:Exposición y garantía en efectivo o títulos públicos 0% --condicion_de--> Excepcion:Excepción ponderador mínimo — operaciones de pase esencial
  - Condicion:Exposición y garantía en la misma moneda --condicion_de--> Excepcion:Excepción ponderador mínimo — operaciones de pase esencial
  - Condicion:Plazo de vencimiento un día hábil o revaluación diaria --condicion_de--> Excepcion:Excepción ponderador mínimo — operaciones de pase esencial
  - Condicion:Liquidación de activo dentro de cuatro días hábiles --condicion_de--> Excepcion:Excepción ponderador mínimo — operaciones de pase esencial
  - Condicion:Liquidación a través de sistema comprobado --condicion_de--> Excepcion:Excepción ponderador mínimo — operaciones de pase esencial
  - Condicion:Documentación estándar para operaciones de pase --condicion_de--> Excepcion:Excepción ponderador mínimo — operaciones de pase esencial
  - Condicion:Cancelación inmediata ante incumplimiento --condicion_de--> Excepcion:Excepción ponderador mínimo — operaciones de pase esencial
  - Condicion:Derecho de tomar posesión e liquidar activo --condicion_de--> Excepcion:Excepción ponderador mínimo — operaciones de pase esencial
  - omisión fuera_de_tipos (exacta): «punto 5.3.1.4.» — nota: Remisión a otro punto del documento; no es contenido normativo de este punto sino una referencia cruzada que el código resuelve desde el tex…
  - heredado_compuesto: 0

## Ficha 3 — `cap::10.2.2.4`

**Texto propio:**

```
10.2.2.4. Divulgación.
Las ECAI deberán divulgar la siguiente información: su código de conducta;
el carácter general de sus acuerdos de remuneración con las entidades eva-
luadas; sus métodos de evaluación, incluida la definición de incumplimiento,
el horizonte temporal y el significado de cada calificación; las tasas de in-
cumplimiento efectivamente registradas en cada categoría de evaluación y la
transición entre las calificaciones –es decir, la probabilidad de migrar entre
calificaciones–.
```
**Heredado:** Sección 10. Agentes de calificación externa (ECAI). / 10.2. Criterios de elegibilidad. / 10.2.2. Condiciones. / Las ECAI deberán cumplir cada uno de los siguientes seis criterios:

**ANTERIOR** — error: None; salida: 1318 tokens

- Obligacion «Divulgación de código de conducta»: Las ECAI deberán divulgar su código de conducta ‖ tramo (exacta): «Las ECAI deberán divulgar la siguiente información: su código de conducta»
- Obligacion «Divulgación de acuerdos de remuneración»: Las ECAI deberán divulgar el carácter general de sus acuerdos de remuneración con las entidades evaluadas ‖ tramo (no): «Las ECAI deberán divulgar la siguiente información: […] el carácter general de sus acuerdos de remuneración con las entidades evaluadas»
- Obligacion «Divulgación de métodos de evaluación»: Las ECAI deberán divulgar sus métodos de evaluación, incluida la definición de incumplimiento, el horizonte temporal y el significado de cada calificación ‖ tramo (no): «Las ECAI deberán divulgar la siguiente información: […] sus métodos de evaluación, incluida la definición de incumplimiento, el horizonte temporal y el significado de cada calificación»
- Obligacion «Divulgación de tasas de incumplimiento y transición»: Las ECAI deberán divulgar las tasas de incumplimiento efectivamente registradas en cada categoría de evaluación y la transición entre las calificaciones, es decir, la probabilidad de migrar entre calificaciones ‖ tramo (no): «Las ECAI deberán divulgar la siguiente información: […] las tasas de incumplimiento efectivamente registradas en cada categoría de evaluación y la transición entre las calificaciones –es decir, la pro…»
  - Obligacion:Divulgación de código de conducta --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Obligacion:Divulgación de acuerdos de remuneración --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Obligacion:Divulgación de métodos de evaluación --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Obligacion:Divulgación de tasas de incumplimiento y transición --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Obligacion:Divulgación de código de conducta --aplica_a--> Las ECAI
  - Obligacion:Divulgación de acuerdos de remuneración --aplica_a--> Las ECAI
  - Obligacion:Divulgación de métodos de evaluación --aplica_a--> Las ECAI
  - Obligacion:Divulgación de tasas de incumplimiento y transición --aplica_a--> Las ECAI
  - heredado_compuesto: 0

**P3C** — error: None; salida: 1274 tokens

- Obligacion «Divulgación de código de conducta»: Las ECAI deben divulgar su código de conducta como parte de los criterios de elegibilidad requeridos ‖ tramo (exacta): «Las ECAI deberán divulgar la siguiente información: su código de conducta»
- Obligacion «Divulgación de acuerdos de remuneración»: Las ECAI deben divulgar el carácter general de sus acuerdos de remuneración con las entidades evaluadas ‖ tramo (exacta): «el carácter general de sus acuerdos de remuneración con las entidades evaluadas»
- Obligacion «Divulgación de métodos de evaluación»: Las ECAI deben divulgar sus métodos de evaluación, incluida la definición de incumplimiento, el horizonte temporal y el significado de cada calificación ‖ tramo (exacta): «sus métodos de evaluación, incluida la definición de incumplimiento, el horizonte temporal y el significado de cada calificación»
- Obligacion «Divulgación de tasas de incumplimiento y transiciones»: Las ECAI deben divulgar las tasas de incumplimiento efectivamente registradas en cada categoría de evaluación y la transición entre las calificaciones (probabilidad de migrar entre calificaciones) ‖ tramo (exacta): «las tasas de incumplimiento efectivamente registradas en cada categoría de evaluación y la transición entre las calificaciones –es decir, la probabilidad de migrar entre calificaciones–»
  - Obligacion:Divulgación de código de conducta --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Obligacion:Divulgación de acuerdos de remuneración --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Obligacion:Divulgación de métodos de evaluación --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Obligacion:Divulgación de tasas de incumplimiento y transiciones --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Obligacion:Divulgación de código de conducta --aplica_a--> Las ECAI
  - Obligacion:Divulgación de acuerdos de remuneración --aplica_a--> Las ECAI
  - Obligacion:Divulgación de métodos de evaluación --aplica_a--> Las ECAI
  - Obligacion:Divulgación de tasas de incumplimiento y transiciones --aplica_a--> Las ECAI
  - heredado_compuesto: 0

## Ficha 4 — `ext::10.3.6`

**Texto propio:**

```
10.3.6. Pagos de importaciones con cartas de crédito o letras avaladas emitidas u otorgadas
por entidades financieras locales.
La entidad tendrá acceso al mercado de cambios para cancelar cartas de crédito o
letras avaladas emitidas u otorgadas para garantizar operaciones de importaciones
de bienes que tengan el registro aduanero de los bienes, incluso cuando no se
cumplan los requisitos establecidos para el acceso del cliente, en la medida que
cuente con la documentación que demuestre que, al momento de la apertura o
emisión por parte de la entidad, se cumplían las condiciones que resultaban
aplicables según la fecha en que se emitió u otorgó la carta de crédito o letra avalada
y el tipo de operación garantizada por la entidad.
En el caso de cartas de crédito o letras avaladas emitidas u otorgadas a partir del
13/12/23, la entidad deberá contar con la documentación que demuestre que, al
momento de la apertura o emisión, la operación garantizada correspondía a una
importación de bienes con registro de ingreso aduanero a partir de dicha fecha y,
salvo que la operación quedase comprendida en la situación prevista en el punto
10.10.2.11., que el pago garantizado debía ser concretado por el cliente a partir de la
fecha que resultaba de adicionar el plazo en días corridos que le correspondía al bien
por el punto 10.10.1. más otros 15 (quince) días corridos a la fecha estimada de
arribo de los bienes al país.
Para aquellas emitidas u otorgadas a partir del 14/04/25, en la medida que se
cumplan las restantes condiciones, también se admitirá que el pago garantizado
tuviera que ser concretado a partir de la fecha estimada de embarque de los bienes
en origen más un plazo adicional de 15 (quince) días corridos cuando correspondía a
la porción de una operación por la cual el cliente hubiese podido realizar pagos a la
vista en virtud de lo previsto en los puntos 10.10.2.1. o 10.10.2.2.
Las condiciones aplicables para las cartas de crédito o letras avaladas emitidas u
otorgadas hasta el 12/12/23 fueron oportunamente receptadas en el punto 10.3.6. del
Anexo de la Comunicación A 7914.
El boleto de venta deberá efectuarse a nombre de la propia entidad en calidad de
cliente por el concepto “B14. Cancelación de garantías comerciales de entidades
financieras por importaciones de bienes con registro de ingreso aduanero”.
```
**Heredado:** Sección 10. Pagos de importaciones y otras compras de bienes en el exterior. / 10.3. Pagos de importaciones de bienes que cuentan con registro de ingreso aduanero.

**ANTERIOR** — error: None; salida: 2925 tokens

- Operacion «Acceso al mercado de cambios — cancelación de cartas de crédito o letras avaladas»: Cancelación de cartas de crédito o letras avaladas emitidas u otorgadas para garantizar operaciones de importaciones de bienes con registro aduanero ‖ tramo (exacta): «La entidad tendrá acceso al mercado de cambios para cancelar cartas de crédito o letras avaladas emitidas u otorgadas para garantizar operaciones de importaciones de bienes que tengan el registro adua…»
- Condicion «Bienes con registro aduanero — condición para acceso»: La entidad debe contar con documentación que demuestre que al momento de la apertura o emisión se cumplían las condiciones aplicables según la fecha de emisión/otorgamiento y el tipo de operación garantizada ‖ tramo (exacta): «incluso cuando no se cumplan los requisitos establecidos para el acceso del cliente, en la medida que cuente con la documentación que demuestre que, al momento de la apertura o emisión por parte de la…»
- Obligacion «Documentación de operación garantizada — cartas emitidas desde 13/12/23»: Para cartas de crédito o letras avaladas emitidas u otorgadas a partir del 13/12/23, la entidad debe contar con documentación que demuestre que al momento de la apertura o emisión la operación garantizada correspondía a una importación de bienes con registro de ingreso aduanero a partir de esa fecha ‖ tramo (exacta): «En el caso de cartas de crédito o letras avaladas emitidas u otorgadas a partir del 13/12/23, la entidad deberá contar con la documentación que demuestre que, al momento de la apertura o emisión, la o…» ‖ umbrales: ['a partir del 13/12/23']
- Obligacion «Documentación de pago garantizado — plazo de pago desde 13/12/23»: La documentación debe demostrar que el pago garantizado debía ser concretado a partir de la fecha que resulta de adicionar el plazo en días corridos del bien (según punto 10.10.1) más 15 días corridos a la fecha estimada de arribo de los bienes al país, salvo que la operación esté comprendida en pun… ‖ tramo (exacta): «salvo que la operación quedase comprendida en la situación prevista en el punto 10.10.2.11., que el pago garantizado debía ser concretado por el cliente a partir de la fecha que resultaba de adicionar…» ‖ umbrales: ['más otros 15 (quince) días corridos']
- Excepcion «Excepto — operación comprendida en punto 10.10.2.11»: Exceptúa la documentación requerida cuando la operación queda comprendida en la situación prevista en el punto 10.10.2.11 ‖ tramo (exacta): «salvo que la operación quedase comprendida en la situación prevista en el punto 10.10.2.11.»
- Potestad «Admisibilidad de pago desde fecha de embarque — cartas desde 14/04/25»: Se admitirá que el pago garantizado se concretara a partir de la fecha estimada de embarque de los bienes en origen más 15 días corridos para cartas emitidas u otorgadas a partir del 14/04/25, cuando corresponda a porción de operación con opción de pago a la vista según puntos 10.10.2.1 o 10.10.2.2,… ‖ tramo (exacta): «Para aquellas emitidas u otorgadas a partir del 14/04/25, en la medida que se cumplan las restantes condiciones, también se admitirá que el pago garantizado tuviera que ser concretado a partir de la f…»
- Comunicacion «Com. A 7914»:  ‖ tramo (exacta): «Comunicación A 7914»
- Obligacion «Boleto de venta a nombre de la entidad — concepto B14»: El boleto de venta debe efectuarse a nombre de la propia entidad en calidad de cliente por el concepto 'B14. Cancelación de garantías comerciales de entidades financieras por importaciones de bienes con registro de ingreso aduanero' ‖ tramo (exacta): «El boleto de venta deberá efectuarse a nombre de la propia entidad en calidad de cliente por el concepto "B14. Cancelación de garantías comerciales de entidades financieras por importaciones de bienes…»
  - Operacion:Acceso al mercado de cambios — cancelación de cartas de crédito o letr… --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Condicion:Bienes con registro aduanero — condición para acceso --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Obligacion:Documentación de operación garantizada — cartas emitidas desde 13/12/2… --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Obligacion:Documentación de pago garantizado — plazo de pago desde 13/12/23 --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Excepcion:Excepto — operación comprendida en punto 10.10.2.11 --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Potestad:Admisibilidad de pago desde fecha de embarque — cartas desde 14/04/25 --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Obligacion:Boleto de venta a nombre de la entidad — concepto B14 --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Condicion:Bienes con registro aduanero — condición para acceso --condicion_de--> Operacion:Acceso al mercado de cambios — cancelación de cartas de crédito o letr…
  - Excepcion:Excepto — operación comprendida en punto 10.10.2.11 --exceptua_obligacion--> Obligacion:Documentación de pago garantizado — plazo de pago desde 13/12/23
  - Operacion:Acceso al mercado de cambios — cancelación de cartas de crédito o letr… --aplica_a--> La entidad
  - Obligacion:Documentación de operación garantizada — cartas emitidas desde 13/12/2… --aplica_a--> la entidad
  - Obligacion:Documentación de pago garantizado — plazo de pago desde 13/12/23 --aplica_a--> la entidad
  - Obligacion:Boleto de venta a nombre de la entidad — concepto B14 --aplica_a--> la propia entidad
  - omisión meta_normativo (exacta): «Las condiciones aplicables para las cartas de crédito o letras avaladas emitidas u otorgadas hasta el 12/12/23 fueron oportunamente receptadas en el punto 10.3.…» — nota: Remisión a norma anterior que ya fue incorporada en otra comunicación; no prescribe conducta nueva
  - heredado_compuesto: 0

**P3C** — error: None; salida: 2915 tokens

- Operacion «Cancelación de cartas de crédito o letras avaladas»: La entidad accede al mercado de cambios para cancelar cartas de crédito o letras avaladas emitidas u otorgadas para garantizar operaciones de importaciones de bienes que tengan registro aduanero de los bienes, incluso cuando no se cumplen los requisitos establecidos para el acceso del cliente ‖ tramo (exacta): «La entidad tendrá acceso al mercado de cambios para cancelar cartas de crédito o letras avaladas emitidas u otorgadas para garantizar operaciones de importaciones de bienes que tengan el registro adua…»
- Condicion «Documentación de emisión según fecha de cartas de crédito o letras»: La entidad debe contar con documentación que demuestre que al momento de la apertura o emisión se cumplían las condiciones aplicables según la fecha de emisión u otorgamiento de la carta de crédito o letra avalada ‖ tramo (exacta): «en la medida que cuente con la documentación que demuestre que, al momento de la apertura o emisión por parte de la entidad, se cumplían las condiciones que resultaban aplicables según la fecha en que…»
- Condicion «Registro aduanero a partir de 13/12/23»: Para cartas de crédito o letras avaladas emitidas u otorgadas a partir del 13/12/23, la operación garantizada debe corresponder a una importación de bienes con registro de ingreso aduanero a partir de esa fecha ‖ tramo (exacta): «En el caso de cartas de crédito o letras avaladas emitidas u otorgadas a partir del 13/12/23, la entidad deberá contar con la documentación que demuestre que, al momento de la apertura o emisión, la o…» ‖ umbrales: ['a partir del 13/12/23']
- Condicion «Plazo de pago según punto 10.10.1 más 15 días»: El pago garantizado debe ser concretado a partir de la fecha que suma el plazo en días corridos del bien según punto 10.10.1 más otros 15 días corridos a la fecha estimada de arribo de los bienes ‖ tramo (exacta): «que el pago garantizado debía ser concretado por el cliente a partir de la fecha que resultaba de adicionar el plazo en días corridos que le correspondía al bien por el punto 10.10.1. más otros 15 (qu…» ‖ umbrales: ['más otros 15 (quince) días corridos']
- Excepcion «Excepción cuando operación comprendida en punto 10.10.2.11»: Exceptúa la exigencia de pago a partir de la fecha de arribo más plazo cuando la operación queda comprendida en el punto 10.10.2.11 ‖ tramo (exacta): «salvo que la operación quedase comprendida en la situación prevista en el punto 10.10.2.11.»
- Condicion «Pago a partir de fecha estimada de embarque más 15 días (desde 14/04/25)»: Para cartas de crédito o letras avaladas emitidas u otorgadas a partir del 14/04/25, se admite que el pago garantizado sea concretado a partir de la fecha estimada de embarque más 15 días corridos, cuando sea porción de operación que permitía pagos a la vista conforme puntos 10.10.2.1 o 10.10.2.2 ‖ tramo (exacta): «Para aquellas emitidas u otorgadas a partir del 14/04/25, en la medida que se cumplan las restantes condiciones, también se admitirá que el pago garantizado tuviera que ser concretado a partir de la f…» ‖ umbrales: ['a partir del 14/04/25', 'más un plazo adicional de 15 (quince) días corridos']
- Definicion «Concepto de boleto de venta»: Debe efectuarse a nombre de la propia entidad en calidad de cliente por el concepto 'B14. Cancelación de garantías comerciales de entidades financieras por importaciones de bienes con registro de ingreso aduanero' ‖ tramo (exacta): «El boleto de venta deberá efectuarse a nombre de la propia entidad en calidad de cliente por el concepto "B14. Cancelación de garantías comerciales de entidades financieras por importaciones de bienes…»
- Obligacion «Boleto de venta con concepto específico»: La entidad debe efectuar el boleto de venta a su nombre en calidad de cliente, con el concepto específico 'B14. Cancelación de garantías comerciales de entidades financieras por importaciones de bienes con registro de ingreso aduanero' ‖ tramo (exacta): «El boleto de venta deberá efectuarse a nombre de la propia entidad en calidad de cliente por el concepto "B14. Cancelación de garantías comerciales de entidades financieras por importaciones de bienes…»
- Comunicacion «Com. A 7914»:  ‖ tramo (exacta): «Las condiciones aplicables para las cartas de crédito o letras avaladas emitidas u otorgadas hasta el 12/12/23 fueron oportunamente receptadas en el punto 10.3.6. del Anexo de la Comunicación A 7914.»
  - Operacion:Cancelación de cartas de crédito o letras avaladas --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Condicion:Documentación de emisión según fecha de cartas de crédito o letras --condicion_de--> Operacion:Cancelación de cartas de crédito o letras avaladas
  - Condicion:Registro aduanero a partir de 13/12/23 --condicion_de--> Operacion:Cancelación de cartas de crédito o letras avaladas
  - Condicion:Plazo de pago según punto 10.10.1 más 15 días --condicion_de--> Operacion:Cancelación de cartas de crédito o letras avaladas
  - Condicion:Pago a partir de fecha estimada de embarque más 15 días (desde 14/04/2… --condicion_de--> Operacion:Cancelación de cartas de crédito o letras avaladas
  - Obligacion:Boleto de venta con concepto específico --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Operacion:Cancelación de cartas de crédito o letras avaladas --aplica_a--> La entidad
  - Obligacion:Boleto de venta con concepto específico --aplica_a--> la propia entidad
  - TextoOrdenado:Texto Ordenado Exterior Cambios --referencia--> Comunicacion:Com. A 7914
  - rechazo: firma_invalida: relations[4]: Excepcion --exceptua--> Condicion
  - omisión meta_normativo (exacta): «Las condiciones aplicables para las cartas de crédito o letras avaladas emitidas u otorgadas hasta el 12/12/23 fueron oportunamente receptadas en el punto 10.3.…» — nota: Enunciado informativo sobre dónde se receptaron condiciones anteriores, sin prescripción normativa nueva
  - heredado_compuesto: 0

## Ficha 5 — `cap::3.2::intro`

**Texto propio:**

```
Las participaciones en fondos (carteras de activos) imputadas a la cartera de inversión
–incluidas las exposiciones fuera de balance, tales como los compromisos de suscripciones fu-
turas– se deberán tratar de acuerdo con uno o más de los siguientes enfoques: de transparen-
cia (“look-through approach”, LTA), reglamentario (“mandate-based approach”, MBA) y residual
(“fall-back approach”, FBA).
Quedan comprendidas las participaciones en fondos comunes regidos por la Ley 24.083 de
Fondos Comunes de Inversión y en fideicomisos –en este último caso, en la medida en que el
riesgo de la inversión no se estructure a través de instrumentos que se emitan con distinta pre-
lación para el cobro, tales como títulos de deuda y certificados de participación–, imputados a
la cartera de inversión.
```
**Heredado:** Sección 3. Capital mínimo por riesgo de crédito. Titulizaciones e inversiones en fon- dos. / 3.2. Tratamiento de las posiciones en fondos.

**ANTERIOR** — error: None; salida: 1314 tokens

- Operacion «Tratamiento de participaciones en fondos»: Las participaciones en fondos (carteras de activos) imputadas a la cartera de inversión, incluidas las exposiciones fuera de balance tales como compromisos de suscripciones futuras, se tratan de acuerdo con uno o más de los siguientes enfoques: de transparencia (LTA), reglamentario (MBA) y residual … ‖ tramo (exacta): «Las participaciones en fondos (carteras de activos) imputadas a la cartera de inversión –incluidas las exposiciones fuera de balance, tales como los compromisos de suscripciones futuras– se deberán tr…»
- Operacion «Participaciones en fondos comunes comprendidas»: Quedan comprendidas las participaciones en fondos comunes de inversión regidos por la Ley 24.083 y en fideicomisos (siempre que el riesgo de la inversión no se estructure mediante instrumentos con distinta prelación para el cobro, como títulos de deuda y certificados de participación), imputados a l… ‖ tramo (exacta): «Quedan comprendidas las participaciones en fondos comunes regidos por la Ley 24.083 de Fondos Comunes de Inversión y en fideicomisos –en este último caso, en la medida en que el riesgo de la inversión…»
- Condicion «Fideicomisos sin instrumentos con prelación diferente»: La inclusión de fideicomisos aplica solo cuando el riesgo de la inversión no se estructure mediante instrumentos emitidos con distinta prelación para el cobro (títulos de deuda, certificados de participación). ‖ tramo (exacta): «en la medida en que el riesgo de la inversión no se estructure a través de instrumentos que se emitan con distinta prelación para el cobro, tales como títulos de deuda y certificados de participación»
  - Operacion:Tratamiento de participaciones en fondos --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Operacion:Participaciones en fondos comunes comprendidas --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Condicion:Fideicomisos sin instrumentos con prelación diferente --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Condicion:Fideicomisos sin instrumentos con prelación diferente --condicion_de--> Operacion:Participaciones en fondos comunes comprendidas
  - omisión relacion_sin_predicado (no): «Las participaciones en fondos (carteras de activos) imputadas a la cartera de inversión se deberán tratar de acuerdo con uno o más de los siguientes enfoques» — nota: La operación e1 (tratamiento de participaciones) se regula por las entidades financieras del alcance (sujeto_rol_alcance_capmin), pero el bl…
  - heredado_compuesto: 0

**P3C** — error: None; salida: 1515 tokens

- Operacion «Tratamiento de posiciones en fondos (tres enfoques)»: Se deben tratar las participaciones en fondos imputadas a la cartera de inversión, incluidas exposiciones fuera de balance como compromisos de suscripciones futuras, según uno o más de estos enfoques: enfoque de transparencia (LTA), enfoque reglamentario (MBA) o enfoque residual (FBA) ‖ tramo (exacta): «Las participaciones en fondos (carteras de activos) imputadas a la cartera de inversión –incluidas las exposiciones fuera de balance, tales como los compromisos de suscripciones futuras– se deberán tr…»
- Definicion «Fondos comunes de inversión comprendidos»: Participaciones en fondos comunes de inversión regulados por la Ley 24.083, incluidas en el tratamiento de posiciones en fondos para fines de capital mínimo ‖ tramo (exacta): «Quedan comprendidas las participaciones en fondos comunes regidos por la Ley 24.083 de Fondos Comunes de Inversión»
- Definicion «Fideicomisos comprendidos (sin títulos de distinta prelación)»: Participaciones en fideicomisos imputadas a la cartera de inversión, quedando comprendidas cuando el riesgo de la inversión no se estructura a través de instrumentos emitidos con distinta prelación para el cobro (como títulos de deuda y certificados de participación) ‖ tramo (no): «Quedan comprendidas las participaciones en fideicomisos –en este último caso, en la medida en que el riesgo de la inversión no se estructure a través de instrumentos que se emitan con distinta prelaci…»
- Restriccion «Límite cualitativo — fideicomisos estructurados»: Las participaciones en fideicomisos no quedan comprendidas si el riesgo de la inversión se estructura a través de instrumentos emitidos con distinta prelación para el cobro (como títulos de deuda y certificados de participación) ‖ tramo (exacta): «en la medida en que el riesgo de la inversión no se estructure a través de instrumentos que se emitan con distinta prelación para el cobro, tales como títulos de deuda y certificados de participación»
  - Operacion:Tratamiento de posiciones en fondos (tres enfoques) --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Definicion:Fondos comunes de inversión comprendidos --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Definicion:Fideicomisos comprendidos (sin títulos de distinta prelación) --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Restriccion:Límite cualitativo — fideicomisos estructurados --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Operacion:Tratamiento de posiciones en fondos (tres enfoques) --aplica_a--> Las participaciones en fondos
  - rechazo: firma_invalida: relations[5]: Restriccion --limita--> Definicion
  - omisión meta_normativo (exacta): «se deberán tratar de acuerdo con uno o más de los siguientes enfoques» — nota: Cláusula que fija la obligación de tratamiento, pero ya está contenida en la descripción de la Operacion e1 como el acto regulado; la modali…
  - heredado_compuesto: 0

## Ficha 6 — `ext::4.1.4.7`

**Texto propio:**

```
4.1.4.7. la adquisición de tarjetas de regalo o equivalentes de tiendas o locales
radicados en el exterior.
```
**Heredado:** Sección 4. Otras disposiciones específicas. / 4.1. Operaciones con débito en una cuenta en una entidad financiera local y/o con tarjetas de / crédito, compra y prepagas emitidas en el país. / 4.1.4. Pagos al exterior por el uso de tarjetas de crédito, compra, débito o prepagas emitidas / en el país o cualquier modalidad que implique un débito inmediato en una cuenta en una entidad financiera local. Las entidades financieras y las empresas no financieras emisoras de tarjetas locales deberán contar con la conformidad previa del BCRA para acceder…

**ANTERIOR** — error: None; salida: 1094 tokens

- Operacion «Adquisición tarjetas de regalo exterior»: adquisición de tarjetas de regalo o equivalentes emitidas por tiendas o locales radicados en el exterior, realizada mediante débito en cuenta en entidad financiera local o con tarjetas de crédito, compra, débito o prepagas emitidas en el país ‖ tramo (exacta): «la adquisición de tarjetas de regalo o equivalentes de tiendas o locales radicados en el exterior»
- Obligacion «Conformidad previa BCRA — pagos al exterior tarjetas»: Las entidades financieras y las empresas no financieras emisoras de tarjetas locales deberán contar con conformidad previa del BCRA para acceder al mercado de cambios cuando realicen pagos al exterior por el uso de tarjetas o cualquier modalidad que implique débito inmediato en cuenta en entidad fin… ‖ tramo (exacta): «Las entidades financieras y las empresas no financieras emisoras de tarjetas locales deberán contar con la conformidad previa del BCRA […] la adquisición de tarjetas de regalo o equivalentes de tienda…»
  - Obligacion:Conformidad previa BCRA — pagos al exterior tarjetas --establecida_en--> TextoOrdenado:Exterior - Cambios
  - Operacion:Adquisición tarjetas de regalo exterior --establecida_en--> TextoOrdenado:Exterior - Cambios
  - Obligacion:Conformidad previa BCRA — pagos al exterior tarjetas --aplica_a--> Las entidades financieras y las empresas no financieras emisoras de tarjetas locales
  - Obligacion:Conformidad previa BCRA — pagos al exterior tarjetas --aplica_a--> empresas no financieras emisoras de tarjetas locales
  - Obligacion:Conformidad previa BCRA — pagos al exterior tarjetas --regula--> Operacion:Adquisición tarjetas de regalo exterior
  - omisión meta_normativo (exacta): «cuando tales pagos se originen, en forma directa o indirecta a través del uso de redes de pagos internacionales» — nota: cláusula aclaratoria del alcance del deber; predica sobre el significado y alcance de 'pagos al exterior' más que sobre conducta prescrita
  - heredado_compuesto: 0

**P3C** — error: None; salida: 1067 tokens

- Operacion «Adquisición de tarjetas de regalo — exterior»: adquisición de tarjetas de regalo o equivalentes de tiendas o locales radicados en el exterior, realizadas mediante débito en una cuenta en una entidad financiera local o mediante tarjetas de crédito, compra, débito o prepagas emitidas en el país, a través de redes de pagos internacionales ‖ tramo (exacta): «la adquisición de tarjetas de regalo o equivalentes de tiendas o locales radicados en el exterior»
- Obligacion «Conformidad previa BCRA — operación con tarjeta al exterior»: obtener conformidad previa del BCRA para acceder al mercado de cambios y realizar pagos al exterior por uso de tarjetas o débito inmediato en cuenta de entidad financiera local, cuando la operación sea adquisición de tarjetas de regalo o equivalentes de tiendas o locales radicados en el exterior, or… ‖ tramo (exacta): «Las entidades financieras y las empresas no financieras emisoras de tarjetas locales deberán contar con la conformidad previa del BCRA para acceder al mercado de cambios para realizar pagos al exterio…»
  - Obligacion:Conformidad previa BCRA — operación con tarjeta al exterior --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Obligacion:Conformidad previa BCRA — operación con tarjeta al exterior --regula--> Operacion:Adquisición de tarjetas de regalo — exterior
  - Obligacion:Conformidad previa BCRA — operación con tarjeta al exterior --aplica_a--> Las entidades financieras
  - Obligacion:Conformidad previa BCRA — operación con tarjeta al exterior --aplica_a--> las empresas no financieras emisoras de tarjetas locales
  - omisión fuera_de_tipos (exacta): «para acceder al mercado de cambios» — nota: Potestad discrecional del BCRA de permitir/autorizar el acceso al mercado de cambios; se enuncia aquí como condición de la obligación, pero …
  - heredado_compuesto: 0

## Ficha 7 — `ctacte::3.2.5`

**Texto propio:**

```
3.2.5. Fecha de vencimiento de un cheque de pago diferido –no registrado– anterior o igual a
la fecha de libramiento.
```
**Heredado:** Sección 3. Cheques. / 3.2. Títulos que carecen de valor como cheques. / El título respecto del que se presentare alguna de las siguientes situaciones, enumeradas taxativamente a continuación, no valdrá como cheque: / Los títulos devueltos por esas situaciones no podrán ser objeto de nuevas presentaciones.

**ANTERIOR** — error: None; salida: 820 tokens

- Operacion «Cheque de pago diferido no registrado»: cheque de pago diferido –no registrado– ‖ tramo (exacta): «Títulos»
- Restriccion «Prohibición — fecha vencimiento anterior/igual libramiento»: El cheque de pago diferido –no registrado– cuya fecha de vencimiento sea anterior o igual a la fecha de libramiento no vale como cheque ‖ tramo (exacta): «Fecha de vencimiento de un cheque de pago diferido –no registrado– anterior o igual a la fecha de libramiento»
- Restriccion «Prohibición — re-presentación de títulos devueltos»: Los títulos que carecen de valor como cheques no podrán ser objeto de nuevas presentaciones ‖ tramo (exacta): «Los títulos devueltos por esas situaciones no podrán ser objeto de nuevas presentaciones»
  - Restriccion:Prohibición — fecha vencimiento anterior/igual libramiento --establecida_en--> TextoOrdenado:Cuentas de corresponsalía
  - Restriccion:Prohibición — re-presentación de títulos devueltos --establecida_en--> TextoOrdenado:Cuentas de corresponsalía
  - Restriccion:Prohibición — fecha vencimiento anterior/igual libramiento --prohibe--> Operacion:Cheque de pago diferido no registrado
  - Restriccion:Prohibición — fecha vencimiento anterior/igual libramiento --aplica_a--> los bancos
  - omisión meta_normativo (exacta): «no valdrá como cheque» — nota: Cláusula que declara el efecto jurídico (pérdida de validez) de la condición enunciada, no prescribe conducta de un sujeto
  - heredado_compuesto: 0

**P3C** — error: None; salida: 846 tokens

- Operacion «Cheque de pago diferido no registrado»: Cheque de pago diferido que no ha sido registrado ‖ tramo (exacta): «cheque de pago diferido –no registrado–»
- Condicion «Fecha de vencimiento anterior o igual a fecha de libramiento»: La fecha de vencimiento del cheque es anterior o igual a la fecha de libramiento del mismo ‖ tramo (exacta): «Fecha de vencimiento de un cheque de pago diferido –no registrado– anterior o igual a la fecha de libramiento» ‖ umbrales: ['anterior o igual a la fecha de libramiento']
- Restriccion «El título no valdrá como cheque — vencimiento anterior o igual a libramiento»: Un título que es un cheque de pago diferido no registrado cuya fecha de vencimiento es anterior o igual a la fecha de libramiento no valdrá como cheque ‖ tramo (exacta): «El título respecto del que se presentare alguna de las siguientes situaciones, enumeradas taxativamente a continuación, no valdrá como cheque»
  - Restriccion:El título no valdrá como cheque — vencimiento anterior o igual a libra… --establecida_en--> TextoOrdenado:Texto Ordenado de Cuentas de Corresponsalía
  - Condicion:Fecha de vencimiento anterior o igual a fecha de libramiento --condicion_de--> Restriccion:El título no valdrá como cheque — vencimiento anterior o igual a libra…
  - Restriccion:El título no valdrá como cheque — vencimiento anterior o igual a libra… --prohibe--> Operacion:Cheque de pago diferido no registrado
  - omisión meta_normativo (exacta): «Los títulos devueltos por esas situaciones no podrán ser objeto de nuevas presentaciones» — nota: Párrafo de cierre del punto contenedor (3.2); no es contenido normativo propio de 3.2.5, sino consecuencia general de que el título no valga…
  - heredado_compuesto: 1

## Ficha 8 — `cap::11.4`

**Texto propio:**

```
11.4. A los efectos de la determinación de la RPC, las entidades financieras podrán computar como
capital ordinario de nivel uno (COn1) la diferencia positiva entre la nueva previsión contable
computada según el punto 5.5 de la NIIF 9 –teniendo en cuenta, de corresponder, la metodo-
logía de prorrateo prevista en la Comunicación A 6847– y la previsión regulatoria calculada
según las normas sobre Previsiones Mínimas por Riesgo de Incobrabilidad o la contable co-
rrespondiente al balance de saldos del 30/11 del año anterior al de la aplicación por primera
vez del citado punto de la NIIF 9 –la mayor de ambas–.
```
**Heredado:** Sección 11. Otras disposiciones.

**ANTERIOR** — error: None; salida: 1227 tokens

- Potestad «Cómputo de diferencia positiva como COn1»: Facultad de computar como capital ordinario de nivel uno (COn1) la diferencia positiva entre la nueva previsión contable (según punto 5.5 de NIIF 9 con metodología de prorrateo de Com. A 6847) y la previsión regulatoria (según normas de Previsiones Mínimas por Riesgo de Incobrabilidad o saldo contab… ‖ tramo (exacta): «las entidades financieras podrán computar como capital ordinario de nivel uno (COn1) la diferencia positiva entre la nueva previsión contable computada según el punto 5.5 de la NIIF 9 –teniendo en cue…»
- Operacion «Determinación de RPC»: Determinación de la Razón de Patrimonialización Compuesta (RPC) ‖ tramo (exacta): «determinación de la RPC»
- Definicion «COn1 — capital ordinario de nivel uno»: La diferencia positiva entre la nueva previsión contable computada según el punto 5.5 de la NIIF 9 (con metodología de prorrateo de Com. A 6847, de corresponder) y la previsión regulatoria calculada según normas sobre Previsiones Mínimas por Riesgo de Incobrabilidad o saldo contable al 30/11 del año… ‖ tramo (exacta): «capital ordinario de nivel uno (COn1)»
- Comunicacion «Com. A 6847»:  ‖ tramo (exacta): «Comunicación A 6847»
  - Potestad:Cómputo de diferencia positiva como COn1 --establecida_en--> TextoOrdenado:Texto Ordenado de Capitales Mínimos
  - Operacion:Determinación de RPC --establecida_en--> TextoOrdenado:Texto Ordenado de Capitales Mínimos
  - Definicion:COn1 — capital ordinario de nivel uno --establecida_en--> TextoOrdenado:Texto Ordenado de Capitales Mínimos
  - TextoOrdenado:Texto Ordenado de Capitales Mínimos --referencia--> Comunicacion:Com. A 6847
  - Potestad:Cómputo de diferencia positiva como COn1 --aplica_a--> las entidades financieras
  - rechazo: firma_invalida: relations[5]: Operacion --condicion_de--> Potestad
  - heredado_compuesto: 0

**P3C** — error: None; salida: 1376 tokens

- Operacion «Cómputo de diferencia positiva como COn1»: Cómputo de la diferencia positiva entre la nueva previsión contable según NIIF 9 punto 5.5 (con la metodología de prorrateo de Com. A 6847 si corresponde) y la previsión regulatoria según normas de Previsiones Mínimas por Riesgo de Incobrabilidad o la contable del balance de saldos del 30/11 del año… ‖ tramo (exacta): «las entidades financieras podrán computar como capital ordinario de nivel uno (COn1) la diferencia positiva entre la nueva previsión contable computada según el punto 5.5 de la NIIF 9 –teniendo en cue…»
- Potestad «Facultad de computar diferencia positiva como COn1»: Facultad de las entidades financieras de computar como capital ordinario de nivel uno la diferencia positiva entre previsiones contable y regulatoria, según las condiciones especificadas ‖ tramo (exacta): «las entidades financieras podrán computar como capital ordinario de nivel uno (COn1) la diferencia positiva»
- Condicion «Condición de aplicación de metodología de prorrateo»: Cuando corresponda, aplicar la metodología de prorrateo prevista en la Comunicación A 6847 en el cómputo de la nueva previsión contable según NIIF 9 ‖ tramo (exacta): «teniendo en cuenta, de corresponder, la metodología de prorrateo prevista en la Comunicación A 6847»
- Comunicacion «Com. A 6847»:  ‖ tramo (exacta): «Comunicación A 6847»
  - Operacion:Cómputo de diferencia positiva como COn1 --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Potestad:Facultad de computar diferencia positiva como COn1 --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - Condicion:Condición de aplicación de metodología de prorrateo --establecida_en--> TextoOrdenado:Texto Ordenado Capitales Mínimos
  - TextoOrdenado:Texto Ordenado Capitales Mínimos --referencia--> Comunicacion:Com. A 6847
  - Potestad:Facultad de computar diferencia positiva como COn1 --aplica_a--> las entidades financieras
  - Operacion:Cómputo de diferencia positiva como COn1 --aplica_a--> las entidades financieras
  - rechazo: firma_invalida: relations[6]: Condicion --condiciona--> Operacion
  - omisión meta_normativo (exacta): «A los efectos de la determinación de la RPC» — nota: Cláusula de alcance/finalidad: especifica el contexto regulatorio pero no prescribe conducta directa
  - heredado_compuesto: 0

## Ficha 9 — `ext::10.4.2.5`

**Texto propio:**

```
10.4.2.5. Cuenta con elementos que le permitan avalar la razonabilidad de los
montos a pagar considerando la actividad importadora del cliente en los
últimos años y/o los planes de negocios que le presente el importador.
Adicionalmente, en el caso de que el cliente no sea una persona humana y
se haya constituido hasta 365 (trescientos sesenta y cinco) días corridos
antes de la fecha de acceso al mercado de cambios, para dar curso a
nuevos pagos se requerirá la conformidad previa del BCRA cuando el
monto pendiente de regularización por pagos anticipados de importaciones
sea mayor al equivalente de USD 5 millones (dólares estadounidenses
cinco millones), incluido el monto por el cual se solicita el acceso al
mercado de cambios. En el caso de que el cliente sea una unión transitoria,
se tomará en cuenta la fecha de constitución de la sociedad más antigua
que la conforma.
Para los importadores comprendidos en el párrafo anterior, las entidades
deberán consultar en el apartado “Régimen Informativo SEPAIMPO” del
sitio www3.bcra.gob.ar, si el saldo pendiente de regularización por pagos
anticipados de importaciones del cliente se encuentra comprendido en el
límite previsto.
```
**Heredado:** Sección 10. Pagos de importaciones y otras compras de bienes en el exterior. / 10.4. Pagos de importaciones de bienes con registro de ingreso aduanero pendiente. / 10.4.2. Requisitos de acceso para el pago anticipado de importaciones. / La entidad podrá dar acceso al mercado de cambios para el pago al exterior en la medida que verifique previamente que se cumplen la totalidad de los siguientes requisitos:

**ANTERIOR** — error: None; salida: 1848 tokens

- Operacion «Pago anticipado de importaciones»: Pago al exterior para importaciones de bienes con registro de ingreso aduanero pendiente, considerando la actividad importadora del cliente en los últimos años o planes de negocios ‖ tramo (exacta): «pago al exterior»
- Obligacion «Verificar razonabilidad de montos pagables»: La entidad debe contar con elementos que le permitan avalar la razonabilidad de los montos a pagar considerando la actividad importadora del cliente en los últimos años y/o los planes de negocios presentados por el importador ‖ tramo (exacta): «Cuenta con elementos que le permitan avalar la razonabilidad de los montos a pagar considerando la actividad importadora del cliente en los últimos años y/o los planes de negocios que le presente el i…»
- Condicion «Cliente no es persona humana y constituido hace menos de 365 días»: Supuesto en que se requiere conformidad previa del BCRA para nuevos pagos ‖ tramo (exacta): «en el caso de que el cliente no sea una persona humana y se haya constituido hasta 365 (trescientos sesenta y cinco) días corridos antes de la fecha de acceso al mercado de cambios» ‖ umbrales: ['hasta 365 (trescientos sesenta y cinco) días corridos']
- Obligacion «Requerir conformidad previa BCRA por monto mayor a USD 5 millones»: Las entidades deberán requerir conformidad previa del BCRA para dar curso a nuevos pagos cuando el monto pendiente de regularización por pagos anticipados de importaciones sea mayor a USD 5 millones, incluido el monto por el cual se solicita el acceso al mercado de cambios ‖ tramo (exacta): «para dar curso a nuevos pagos se requerirá la conformidad previa del BCRA cuando el monto pendiente de regularización por pagos anticipados de importaciones sea mayor al equivalente de USD 5 millones …» ‖ umbrales: ['mayor al equivalente de USD 5 millones (dólares estadounidenses cinco millones)']
- Condicion «Cliente es unión transitoria»: Para uniones transitorias se considera la fecha de constitución de la sociedad más antigua que la conforma ‖ tramo (exacta): «En el caso de que el cliente sea una unión transitoria, se tomará en cuenta la fecha de constitución de la sociedad más antigua que la conforma»
- Obligacion «Consultar saldo pendiente en Régimen Informativo SEPAIMPO»: Las entidades deberán consultar en el apartado 'Régimen Informativo SEPAIMPO' del sitio www3.bcra.gob.ar si el saldo pendiente de regularización por pagos anticipados de importaciones del cliente se encuentra comprendido en el límite previsto ‖ tramo (exacta): «las entidades deberán consultar en el apartado "Régimen Informativo SEPAIMPO" del sitio www3.bcra.gob.ar, si el saldo pendiente de regularización por pagos anticipados de importaciones del cliente se …»
  - Obligacion:Verificar razonabilidad de montos pagables --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Obligacion:Requerir conformidad previa BCRA por monto mayor a USD 5 millones --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Obligacion:Consultar saldo pendiente en Régimen Informativo SEPAIMPO --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Obligacion:Verificar razonabilidad de montos pagables --regula--> Operacion:Pago anticipado de importaciones
  - Condicion:Cliente no es persona humana y constituido hace menos de 365 días --condicion_de--> Obligacion:Requerir conformidad previa BCRA por monto mayor a USD 5 millones
  - Obligacion:Verificar razonabilidad de montos pagables --aplica_a--> la entidad
  - Obligacion:Requerir conformidad previa BCRA por monto mayor a USD 5 millones --aplica_a--> las entidades
  - Obligacion:Consultar saldo pendiente en Régimen Informativo SEPAIMPO --aplica_a--> las entidades
  - heredado_compuesto: 1

**P3C** — error: None; salida: 1512 tokens

- Condicion «Razonabilidad de montos — actividad importadora»: La entidad verifica la razonabilidad de los montos a pagar considerando la actividad importadora del cliente en los últimos años y/o los planes de negocios que le presenta el importador ‖ tramo (exacta): «Cuenta con elementos que le permitan avalar la razonabilidad de los montos a pagar considerando la actividad importadora del cliente en los últimos años y/o los planes de negocios que le presente el i…»
- Condicion «Conformidad previa BCRA — cliente constituido hasta 365 días con monto mayor a USD 5 millo…»: Si el cliente no es una persona humana y se constituyó hasta 365 días corridos antes del acceso al mercado de cambios, para nuevos pagos se requiere conformidad previa del BCRA cuando el monto pendiente de regularización por pagos anticipados supere USD 5 millones, incluido el monto solicitado ‖ tramo (exacta): «en el caso de que el cliente no sea una persona humana y se haya constituido hasta 365 (trescientos sesenta y cinco) días corridos antes de la fecha de acceso al mercado de cambios, para dar curso a n…» ‖ umbrales: ['se haya constituido hasta 365 (trescientos sesenta y cinco) días corridos antes de la fecha de acceso al mercado de cambios', 'mayor al equivalente de USD 5 millones (dólares estadounidenses cinco millones)']
- Condicion «Fecha de constitución — unión transitoria»: Para clientes que sean unión transitoria, se considera la fecha de constitución de la sociedad más antigua que la integra ‖ tramo (exacta): «En el caso de que el cliente sea una unión transitoria, se tomará en cuenta la fecha de constitución de la sociedad más antigua que la conforma»
- Obligacion «Consulta SEPAIMPO — saldo pendiente regularización»: Las entidades deberán consultar en el apartado 'Régimen Informativo SEPAIMPO' del sitio www3.bcra.gob.ar si el saldo pendiente de regularización por pagos anticipados de importaciones del cliente se encuentra comprendido en el límite previsto ‖ tramo (exacta): «las entidades deberán consultar en el apartado "Régimen Informativo SEPAIMPO" del sitio www3.bcra.gob.ar, si el saldo pendiente de regularización por pagos anticipados de importaciones del cliente se …»
  - Condicion:Razonabilidad de montos — actividad importadora --establecida_en--> TextoOrdenado:TO Exterior - Cambios
  - Condicion:Conformidad previa BCRA — cliente constituido hasta 365 días con monto… --establecida_en--> TextoOrdenado:TO Exterior - Cambios
  - Condicion:Fecha de constitución — unión transitoria --establecida_en--> TextoOrdenado:TO Exterior - Cambios
  - Obligacion:Consulta SEPAIMPO — saldo pendiente regularización --establecida_en--> TextoOrdenado:TO Exterior - Cambios
  - Obligacion:Consulta SEPAIMPO — saldo pendiente regularización --aplica_a--> las entidades
  - omisión meta_normativo (exacta): «La entidad podrá dar acceso al mercado de cambios para el pago al exterior en la medida que verifique previamente que se cumplen la totalidad de los siguientes …» — nota: Encabezado introductorio que anuncia la lista de requisitos; se extrae en cada ítem como composición con el encabezado (ver COMPOSICIÓN CON …
  - heredado_compuesto: 0

## Ficha 10 — `cla::6.5.4.5`

**Texto propio:**

```
6.5.4.5. Cuente con refinanciaciones del capital adeudado y de los intereses devengados
vinculadas a una insuficiente capacidad para su pago, con otorgamiento de qui-
tas o con reducción en las tasas de interés pactadas –salvo que ello derive de
las condiciones del mercado– o cuando haya sido necesario recibir bienes en
pago de parte de las obligaciones. No obstante, el deudor cuyas deudas hayan
sido refinanciadas con otorgamiento de quitas de capital podrá ser recategoriza-
do directamente en niveles superiores (“con problemas”, “en observación”) por la
aplicación de la metodología establecida en el punto 2.2.6. de las normas sobre
“Previsiones mínimas por riesgo de incobrabilidad”, siempre que además se ob-
serven las otras condiciones previstas en las correspondientes categorías.
Cuando al menos se haya cumplido con el pago, sin haber incurrido en atrasos
superiores a los 31 días del 10 % de las obligaciones refinanciadas y la totalidad
de los intereses devengados, con más el porcentaje acumulado que pudiera co-
rresponder si la refinanciación se hubiera otorgado de haberse encontrado el
deudor en la categoría inferior, podrá reclasificárselo en el nivel inmediato supe-
rior si, además, se observan las otras condiciones previstas en el citado nivel.
El deudor que, encontrándose clasificado en esta categoría, haya refinanciado su
deuda –aun cuando haya cancelado el porcentaje establecido en el párrafo pre-
cedente– y recibido crédito adicional en los términos a que se refiere el punto
2.2.5. de las normas sobre “Previsiones mínimas por riesgo de incobrabilidad”, y
en la medida en que dicha financiación adicional no hubiese sido cancelada, de-
berá permanecer en esta categoría por lo menos 180 días contados desde la fe-
cha en que se otorgó crédito adicional o desde que se celebró el acuerdo de refi-
nanciación, la circunstancia más reciente. Ello, salvo que por aplicación de otras
pautas corresponda categorizarlo en el nivel inferior.
```
**Heredado:** Sección 6. Clasificación de los deudores de la cartera comercial. / 6.5. Niveles de clasificación. / Cada cliente, y la totalidad de sus financiaciones comprendidas, se incluirá en una de las si- guientes cinco categorías, las que se definen teniendo en cuenta las condiciones que se deta- llan en cada caso. Los clientes que no registren asistencia crediticia … / 6.5.4. Con alto riesgo de insolvencia. / El análisis del flujo de fondos del cliente demuestra que es altamente improbable que pueda atender la totalidad de sus compromisos financieros. Entre los indicadores que pueden reflejar esta situación se destacan que el cliente:

**ANTERIOR** — error: None; salida: 3216 tokens

- Operacion «Refinanciación capital e intereses por insuficiencia de pago»: Refinanciación del capital adeudado y de los intereses devengados vinculada a insuficiente capacidad para su pago ‖ tramo (exacta): «Cuente con refinanciaciones del capital adeudado y de los intereses devengados vinculadas a una insuficiente capacidad para su pago»
- Restriccion «Indicador clasificación: refinanciación con quitas o reducción de tasas»: Indicador de alto riesgo de insolvencia: refinanciaciones con otorgamiento de quitas o reducción de tasas de interés (salvo que derive de condiciones del mercado) ‖ tramo (exacta): «Cuente con refinanciaciones del capital adeudado y de los intereses devengados vinculadas a una insuficiente capacidad para su pago, con otorgamiento de quitas o con reducción en las tasas de interés …»
- Excepcion «Reducción de tasas por condiciones de mercado — no indicador»: No se considera indicador de alto riesgo cuando la reducción de tasas de interés deriva de condiciones del mercado ‖ tramo (exacta): «salvo que ello derive de las condiciones del mercado»
- Restriccion «Indicador clasificación: recepción de bienes en pago»: Indicador de alto riesgo de insolvencia: recepción de bienes en pago de parte de las obligaciones ‖ tramo (exacta): «o cuando haya sido necesario recibir bienes en pago de parte de las obligaciones»
- Potestad «Recategorización en niveles superiores — deudor con quitas de capital»: Facultad de recategorizar directamente en niveles superiores ('con problemas', 'en observación') al deudor cuyas deudas fueron refinanciadas con otorgamiento de quitas de capital, conforme metodología del punto 2.2.6 de normas de Previsiones mínimas ‖ tramo (exacta): «el deudor cuyas deudas hayan sido refinanciadas con otorgamiento de quitas de capital podrá ser recategorizado directamente en niveles superiores»
- Condicion «Condición para recategorización: otras condiciones de categoría superior»: Deben observarse las otras condiciones previstas en las categorías superiores a la que se recategoriza ‖ tramo (exacta): «siempre que además se observen las otras condiciones previstas en las correspondientes categorías»
- Condicion «Condición para reclasificación: pago del 10% sin atrasos superiores a 31 días»: Se haya pagado sin atrasos superiores a 31 días el 10% de las obligaciones refinanciadas y la totalidad de los intereses devengados ‖ tramo (exacta): «Cuando al menos se haya cumplido con el pago, sin haber incurrido en atrasos superiores a los 31 días del 10 % de las obligaciones refinanciadas y la totalidad de los intereses devengados» ‖ umbrales: ['atrasos superiores a los 31 días', '10 % de las obligaciones refinanciadas']
- Potestad «Reclasificación en nivel inmediato superior — pago del 10%»: Facultad de reclasificar al deudor en el nivel inmediato superior cuando haya pagado el 10% de obligaciones refinanciadas y la totalidad de intereses devengados sin atrasos superiores a 31 días ‖ tramo (exacta): «podrá reclasificárselo en el nivel inmediato superior»
- Condicion «Condición adicional para reclasificación: otras condiciones del nivel superior»: Deben observarse además las otras condiciones previstas en el nivel inmediato superior ‖ tramo (exacta): «si, además, se observan las otras condiciones previstas en el citado nivel»
- Restriccion «Permanencia mínima 180 días — deudor con refinanciación y crédito adicional»: Deudor clasificado en esta categoría que haya refinanciado su deuda y recibido crédito adicional debe permanecer en esta categoría por lo menos 180 días ‖ tramo (exacta): «deberá permanecer en esta categoría por lo menos 180 días contados desde la fecha en que se otorgó crédito adicional o desde que se celebró el acuerdo de refinanciación, la circunstancia más reciente» ‖ umbrales: ['por lo menos 180 días']
- Condicion «Condición para permanencia: financiación adicional no cancelada»: La restricción de permanencia 180 días aplica en la medida en que la financiación adicional no haya sido cancelada ‖ tramo (exacta): «en la medida en que dicha financiación adicional no hubiese sido cancelada»
- Excepcion «Excepción permanencia mínima — categorización en nivel inferior»: No aplica la permanencia mínima de 180 días si por aplicación de otras pautas corresponde categorizar al deudor en el nivel inferior ‖ tramo (exacta): «Ello, salvo que por aplicación de otras pautas corresponda categorizarlo en el nivel inferior»
  - Operacion:Refinanciación capital e intereses por insuficiencia de pago --establecida_en--> TextoOrdenado:Texto Ordenado Clasificación de Deudores
  - Restriccion:Indicador clasificación: refinanciación con quitas o reducción de tasa… --establecida_en--> TextoOrdenado:Texto Ordenado Clasificación de Deudores
  - Excepcion:Reducción de tasas por condiciones de mercado — no indicador --establecida_en--> TextoOrdenado:Texto Ordenado Clasificación de Deudores
  - Restriccion:Indicador clasificación: recepción de bienes en pago --establecida_en--> TextoOrdenado:Texto Ordenado Clasificación de Deudores
  - Potestad:Recategorización en niveles superiores — deudor con quitas de capital --establecida_en--> TextoOrdenado:Texto Ordenado Clasificación de Deudores
  - Condicion:Condición para recategorización: otras condiciones de categoría superi… --establecida_en--> TextoOrdenado:Texto Ordenado Clasificación de Deudores
  - Condicion:Condición para reclasificación: pago del 10% sin atrasos superiores a … --establecida_en--> TextoOrdenado:Texto Ordenado Clasificación de Deudores
  - Potestad:Reclasificación en nivel inmediato superior — pago del 10% --establecida_en--> TextoOrdenado:Texto Ordenado Clasificación de Deudores
  - Condicion:Condición adicional para reclasificación: otras condiciones del nivel … --establecida_en--> TextoOrdenado:Texto Ordenado Clasificación de Deudores
  - Restriccion:Permanencia mínima 180 días — deudor con refinanciación y crédito adic… --establecida_en--> TextoOrdenado:Texto Ordenado Clasificación de Deudores
  - Condicion:Condición para permanencia: financiación adicional no cancelada --establecida_en--> TextoOrdenado:Texto Ordenado Clasificación de Deudores
  - Excepcion:Excepción permanencia mínima — categorización en nivel inferior --establecida_en--> TextoOrdenado:Texto Ordenado Clasificación de Deudores
  - Excepcion:Reducción de tasas por condiciones de mercado — no indicador --exceptua--> Restriccion:Indicador clasificación: refinanciación con quitas o reducción de tasa…
  - Condicion:Condición para recategorización: otras condiciones de categoría superi… --condicion_de--> Potestad:Recategorización en niveles superiores — deudor con quitas de capital
  - Condicion:Condición para reclasificación: pago del 10% sin atrasos superiores a … --condicion_de--> Potestad:Reclasificación en nivel inmediato superior — pago del 10%
  - Condicion:Condición adicional para reclasificación: otras condiciones del nivel … --condicion_de--> Potestad:Reclasificación en nivel inmediato superior — pago del 10%
  - Condicion:Condición para permanencia: financiación adicional no cancelada --condicion_de--> Restriccion:Permanencia mínima 180 días — deudor con refinanciación y crédito adic…
  - Excepcion:Excepción permanencia mínima — categorización en nivel inferior --exceptua--> Restriccion:Permanencia mínima 180 días — deudor con refinanciación y crédito adic…
  - omisión meta_normativo (exacta): «con más el porcentaje acumulado que pudiera corresponder si la refinanciación se hubiera otorgado de haberse encontrado el deudor en la categoría inferior» — nota: 
  - heredado_compuesto: 0

**P3C** — error: None; salida: 2789 tokens

- Operacion «Refinanciación de capital e intereses»: Refinanciación del capital adeudado y de los intereses devengados vinculadas a una insuficiente capacidad para su pago ‖ tramo (exacta): «Cuente con refinanciaciones del capital adeudado y de los intereses devengados»
- Restriccion «Prohibición refinanciación sin quitas o reducción de tasas»: Indicador de alto riesgo de insolvencia: refinanciaciones vinculadas a insuficiente capacidad de pago, con otorgamiento de quitas o reducción de tasas (salvo si deriva de condiciones del mercado), o recepción de bienes en pago de obligaciones ‖ tramo (exacta): «Cuente con refinanciaciones del capital adeudado y de los intereses devengados vinculadas a una insuficiente capacidad para su pago, con otorgamiento de quitas o con reducción en las tasas de interés …»
- Potestad «Recategorización directa a nivel superior por quitas»: Facultad de recategorizar directamente en niveles superiores ('con problemas', 'en observación') al deudor cuyas deudas hayan sido refinanciadas con otorgamiento de quitas de capital, por aplicación de la metodología del punto 2.2.6 de normas sobre Previsiones mínimas, siempre que se observen las ot… ‖ tramo (exacta): «el deudor cuyas deudas hayan sido refinanciadas con otorgamiento de quitas de capital podrá ser recategorizado directamente en niveles superiores»
- Condicion «Cumplimiento de pago sin atrasos superiores a 31 días»: Supuesto para reclasificación en nivel inmediato superior: pago del 10% de obligaciones refinanciadas y totalidad de intereses devengados, más el porcentaje acumulado si correspondiera, sin atrasos superiores a 31 días ‖ tramo (exacta): «Cuando al menos se haya cumplido con el pago, sin haber incurrido en atrasos superiores a los 31 días del 10 % de las obligaciones refinanciadas y la totalidad de los intereses devengados» ‖ umbrales: ['sin haber incurrido en atrasos superiores a los 31 días', 'del 10 % de las obligaciones refinanciadas']
- Potestad «Reclasificación en nivel inmediato superior»: Facultad de reclasificar en el nivel inmediato superior cuando se cumplan el pago especificado en e4 y se observen las otras condiciones previstas en ese nivel ‖ tramo (exacta): «podrá reclasificárselo en el nivel inmediato superior»
- Restriccion «Permanencia mínima 180 días en categoría»: Deudor que haya refinanciado su deuda, recibido crédito adicional conforme punto 2.2.5 de normas sobre Previsiones mínimas, sin haber cancelado la financiación adicional, debe permanecer en esta categoría mínimo 180 días desde otorgamiento de crédito adicional o celebración del acuerdo de refinancia… ‖ tramo (exacta): «deberá permanecer en esta categoría por lo menos 180 días contados desde la fecha en que se otorgó crédito adicional o desde que se celebró el acuerdo de refinanciación, la circunstancia más reciente» ‖ umbrales: ['por lo menos 180 días']
- Excepcion «Excepción permanencia 180 días por categorización inferior»: Excepción a la permanencia mínima de 180 días si por aplicación de otras pautas corresponde categorizar en el nivel inferior ‖ tramo (exacta): «Ello, salvo que por aplicación de otras pautas corresponda categorizarlo en el nivel inferior»
- Condicion «Refinanciación con crédito adicional»: Supuesto para aplicación de plazo mínimo de permanencia: deudor en esta categoría que haya refinanciado su deuda y recibido crédito adicional conforme punto 2.2.5 de normas sobre Previsiones, mientras no haya cancelado la financiación adicional ‖ tramo (exacta): «El deudor que, encontrándose clasificado en esta categoría, haya refinanciado su deuda –aun cuando haya cancelado el porcentaje establecido en el párrafo precedente– y recibido crédito adicional en lo…»
  - Operacion:Refinanciación de capital e intereses --establecida_en--> TextoOrdenado:Clasificación de deudores
  - Restriccion:Prohibición refinanciación sin quitas o reducción de tasas --establecida_en--> TextoOrdenado:Clasificación de deudores
  - Potestad:Recategorización directa a nivel superior por quitas --establecida_en--> TextoOrdenado:Clasificación de deudores
  - Condicion:Cumplimiento de pago sin atrasos superiores a 31 días --establecida_en--> TextoOrdenado:Clasificación de deudores
  - Potestad:Reclasificación en nivel inmediato superior --establecida_en--> TextoOrdenado:Clasificación de deudores
  - Restriccion:Permanencia mínima 180 días en categoría --establecida_en--> TextoOrdenado:Clasificación de deudores
  - Excepcion:Excepción permanencia 180 días por categorización inferior --establecida_en--> TextoOrdenado:Clasificación de deudores
  - Condicion:Refinanciación con crédito adicional --establecida_en--> TextoOrdenado:Clasificación de deudores
  - Condicion:Cumplimiento de pago sin atrasos superiores a 31 días --condicion_de--> Potestad:Reclasificación en nivel inmediato superior
  - Excepcion:Excepción permanencia 180 días por categorización inferior --exceptua--> Restriccion:Permanencia mínima 180 días en categoría
  - Condicion:Refinanciación con crédito adicional --condicion_de--> Restriccion:Permanencia mínima 180 días en categoría
  - Potestad:Recategorización directa a nivel superior por quitas --aplica_a--> el deudor
  - Potestad:Reclasificación en nivel inmediato superior --aplica_a--> el deudor
  - Restriccion:Permanencia mínima 180 días en categoría --aplica_a--> El deudor
  - omisión relacion_sin_predicado (exacta): «el deudor cuyas deudas hayan sido refinanciadas con otorgamiento de quitas de capital podrá ser recategorizado directamente en niveles superiores» — nota: aplicación de la metodología establecida en el punto 2.2.6
  - heredado_compuesto: 0

## Ficha 11 — `polcre::2.1.15`

**Texto propio:**

```
2.1.15. Financiaciones de proyectos de inversión destinados a la ganadería bovina, incluido su
capital de trabajo, sin superar el 5 % de los depósitos en moneda extranjera de la entidad.
```
**Heredado:** Sección 2. Aplicación de la capacidad de préstamo de depósitos en moneda extranjera. / 2.1. Destinos. / La capacidad de préstamo de los depósitos en moneda extranjera deberá aplicarse, en la co- rrespondiente moneda de captación, en forma indistinta, a los siguientes destinos: / La aplicación de la capacidad de préstamo de depósitos en moneda extranjera a los destinos vinculados a operaciones de importación (previstos en los puntos 2.1.6., 2.1.7. y la parte atri- buible a éstos por aplicación de los puntos 2.1.8. y 2.1.9.), no podrá s… / x / t base base / Siendo: C: capacidad de préstamo del mes al que corresponda. / t / F : financiación de importaciones comprendidas, correspondientes al trimestre agos- base / to/octubre de 2008. / C : capacidad de préstamo que corresponda al trimestre agosto/octubre de 2008. / base / Las financiaciones y capacidad de préstamo deberán ser computadas de acuerdo con lo esta- blecido en el punto 2.5.

**ANTERIOR** — error: None; salida: 695 tokens

- Operacion «Financiaciones de proyectos inversión ganadería bovina»: Financiaciones de proyectos de inversión destinados a la ganadería bovina, incluido su capital de trabajo ‖ tramo (exacta): «Financiaciones de proyectos de inversión destinados a la ganadería bovina, incluido su capital de trabajo»
- Restriccion «Límite 5% depósitos moneda extranjera»: Financiaciones de proyectos de inversión destinados a ganadería bovina no podrán superar el 5% de los depósitos en moneda extranjera de la entidad ‖ tramo (exacta): «sin superar el 5 % de los depósitos en moneda extranjera de la entidad» ‖ umbrales: ['sin superar el 5 %']
  - Restriccion:Límite 5% depósitos moneda extranjera --establecida_en--> TextoOrdenado:Política de aplicación de capacidad de préstamo
  - Restriccion:Límite 5% depósitos moneda extranjera --limita--> Operacion:Financiaciones de proyectos inversión ganadería bovina
  - Operacion:Financiaciones de proyectos inversión ganadería bovina --establecida_en--> TextoOrdenado:Política de aplicación de capacidad de préstamo
  - Restriccion:Límite 5% depósitos moneda extranjera --aplica_a--> la entidad
  - heredado_compuesto: 0

**P3C** — error: None; salida: 705 tokens

- Operacion «Financiación de proyectos ganadería bovina»: Financiaciones de proyectos de inversión destinados a la ganadería bovina, incluido su capital de trabajo ‖ tramo (exacta): «Financiaciones de proyectos de inversión destinados a la ganadería bovina, incluido su capital de trabajo»
- Restriccion «Límite 5 % — depósitos en moneda extranjera»: Las financiaciones de proyectos de inversión destinados a la ganadería bovina no podrán superar el 5 % de los depósitos en moneda extranjera de la entidad ‖ tramo (exacta): «sin superar el 5 % de los depósitos en moneda extranjera de la entidad» ‖ umbrales: ['sin superar el 5 %']
  - Operacion:Financiación de proyectos ganadería bovina --establecida_en--> TextoOrdenado:Política de Crédito - Capacidad de Préstamo
  - Restriccion:Límite 5 % — depósitos en moneda extranjera --establecida_en--> TextoOrdenado:Política de Crédito - Capacidad de Préstamo
  - Restriccion:Límite 5 % — depósitos en moneda extranjera --limita--> Operacion:Financiación de proyectos ganadería bovina
  - Restriccion:Límite 5 % — depósitos en moneda extranjera --aplica_a--> la entidad
  - heredado_compuesto: 0

## Ficha 12 — `cla::5.1.1.1`

**Texto propio:**

```
5.1.1.1. Los créditos para consumo o vivienda.
Los créditos de esta clase que superen el equivalente a dos veces el importe de
referencia establecido en el punto 3.7. y cuyo repago no se encuentre vinculado
a ingresos fijos o periódicos del cliente sino a la evolución de su actividad pro-
ductiva o comercial se incluirán dentro de la cartera comercial.
```
**Heredado:** Sección 5. Categorías de carteras. / 5.1. Categorías. / La cartera se agrupará en dos categorías básicas: / 5.1.1. Cartera comercial. / Abarca todas las financiaciones comprendidas, con excepción de las siguientes:

**ANTERIOR** — error: None; salida: 1448 tokens

- Operacion «Créditos para consumo o vivienda»: Créditos otorgados para consumo o vivienda ‖ tramo (exacta): «Los créditos para consumo o vivienda»
- Condicion «Monto superior a dos veces importe de referencia»: El crédito supera el equivalente a dos veces el importe de referencia del punto 3.7 ‖ tramo (exacta): «superen el equivalente a dos veces el importe de referencia establecido en el punto 3.7.» ‖ umbrales: ['superen el equivalente a dos veces el importe de referencia establecido en el punto 3.7.']
- Condicion «Repago no vinculado a ingresos fijos o periódicos»: El repago no está vinculado a ingresos fijos o periódicos del cliente sino a la evolución de su actividad productiva o comercial ‖ tramo (exacta): «cuyo repago no se encuentre vinculado a ingresos fijos o periódicos del cliente sino a la evolución de su actividad productiva o comercial»
- Operacion «Inclusión en cartera comercial»: Créditos de consumo o vivienda que superen dos veces el importe de referencia y cuyo repago no esté vinculado a ingresos fijos o periódicos, se incluyen dentro de la cartera comercial ‖ tramo (exacta): «se incluirán dentro de la cartera comercial»
- Excepcion «Excepción de créditos para consumo o vivienda»: Los créditos para consumo o vivienda quedan exceptuados de la cartera comercial básica, salvo que superen dos veces el importe de referencia y su repago no esté vinculado a ingresos fijos o periódicos ‖ tramo (exacta): «con excepción de las siguientes: [...] Los créditos para consumo o vivienda»
  - Operacion:Créditos para consumo o vivienda --establecida_en--> TextoOrdenado:Clasificación de deudores
  - Condicion:Monto superior a dos veces importe de referencia --establecida_en--> TextoOrdenado:Clasificación de deudores
  - Condicion:Repago no vinculado a ingresos fijos o periódicos --establecida_en--> TextoOrdenado:Clasificación de deudores
  - Operacion:Inclusión en cartera comercial --establecida_en--> TextoOrdenado:Clasificación de deudores
  - Excepcion:Excepción de créditos para consumo o vivienda --establecida_en--> TextoOrdenado:Clasificación de deudores
  - Condicion:Monto superior a dos veces importe de referencia --condicion_de--> Operacion:Inclusión en cartera comercial
  - Condicion:Repago no vinculado a ingresos fijos o periódicos --condicion_de--> Operacion:Inclusión en cartera comercial
  - omisión relacion_sin_predicado (exacta): «Los créditos de esta clase que superen el equivalente a dos veces el importe de referencia establecido en el punto 3.7. y cuyo repago no se encuentre vinculado …» — nota: Relación de operación que se realiza cuando se cumplen condiciones (quizás condiciona o requiere, pero el predicado exacto depende de la dir…
  - heredado_compuesto: 0

**P3C** — error: None; salida: 1176 tokens

- Operacion «Inclusión en cartera comercial créditos para consumo o vivienda»: Inclusión de créditos para consumo o vivienda en la cartera comercial cuando superen el equivalente a dos veces el importe de referencia establecido en el punto 3.7 y cuyo repago esté vinculado a la evolución de la actividad productiva o comercial del cliente, no a ingresos fijos o periódicos. ‖ tramo (exacta): «Los créditos de esta clase que superen el equivalente a dos veces el importe de referencia establecido en el punto 3.7. y cuyo repago no se encuentre vinculado a ingresos fijos o periódicos del client…»
- Excepcion «Excepción — Cartera comercial: créditos para consumo o vivienda»: Los créditos para consumo o vivienda quedan exceptuados de la cartera comercial, salvo los que superen el equivalente a dos veces el importe de referencia establecido en el punto 3.7 y cuyo repago no esté vinculado a ingresos fijos o periódicos sino a la evolución de su actividad productiva o comerc… ‖ tramo (exacta): «Los créditos para consumo o vivienda.» ‖ umbrales: ['superen el equivalente a dos veces el importe de referencia establecido en el punto 3.7']
- Condicion «Condición — repago vinculado a actividad productiva o comercial»: El repago del crédito no está vinculado a ingresos fijos o periódicos del cliente, sino a la evolución de su actividad productiva o comercial. ‖ tramo (exacta): «cuyo repago no se encuentre vinculado a ingresos fijos o periódicos del cliente sino a la evolución de su actividad productiva o comercial»
  - Operacion:Inclusión en cartera comercial créditos para consumo o vivienda --establecida_en--> TextoOrdenado:Texto Ordenado Clasificación de Deudores
  - Excepcion:Excepción — Cartera comercial: créditos para consumo o vivienda --establecida_en--> TextoOrdenado:Texto Ordenado Clasificación de Deudores
  - Condicion:Condición — repago vinculado a actividad productiva o comercial --establecida_en--> TextoOrdenado:Texto Ordenado Clasificación de Deudores
  - Condicion:Condición — repago vinculado a actividad productiva o comercial --condicion_de--> Operacion:Inclusión en cartera comercial créditos para consumo o vivienda
  - rechazo: firma_invalida: relations[4]: Excepcion --exceptua--> Operacion
  - omisión meta_normativo (exacta): «Abarca todas las financiaciones comprendidas, con excepción de las siguientes:» — nota: Enunciado introductorio de la lista que abre el encabezado del punto 5.1.1; define el alcance de la cartera comercial pero no prescribe cond…
  - heredado_compuesto: 0

## Ficha 13 — `ctacte::3.2::intro`

**Texto propio:**

```
El título respecto del que se presentare alguna de las siguientes situaciones, enumeradas
taxativamente a continuación, no valdrá como cheque:
```
**Heredado:** Sección 3. Cheques. / 3.2. Títulos que carecen de valor como cheques.

**ANTERIOR** — error: None; salida: 414 tokens

- Restriccion «Título sin valor como cheque — situaciones enumeradas»: Un título que presente alguna de las situaciones enumeradas taxativamente en los ítems siguientes no tendrá valor como cheque ‖ tramo (exacta): «El título respecto del que se presentare alguna de las siguientes situaciones, enumeradas taxativamente a continuación, no valdrá como cheque»
  - Restriccion:Título sin valor como cheque — situaciones enumeradas --establecida_en--> TextoOrdenado:Texto Ordenado de Cuentas a la vista
  - omisión meta_normativo (exacta): «enumeradas taxativamente a continuación» — nota: Anuncio de lista; el contenido normativo está en los ítems siguientes (punto 3.2), que tienen su propia unidad de extracción
  - heredado_compuesto: 0

**P3C** — error: None; salida: 413 tokens

- Restriccion «Título sin valor como cheque»: El título que reúna cualquiera de las situaciones enumeradas a continuación no tendrá validez como cheque ‖ tramo (exacta): «El título respecto del que se presentare alguna de las siguientes situaciones, enumeradas taxativamente a continuación, no valdrá como cheque»
  - Restriccion:Título sin valor como cheque --establecida_en--> TextoOrdenado:Cuentas de corresponsalía
  - omisión fuera_de_tipos (exacta): «enumeradas taxativamente a continuación» — nota: Anuncio de lista: el contenido normativo específico de cada situación está en los ítems siguientes, no en este bloque intro. El anuncio no c…
  - heredado_compuesto: 0

## Ficha 14 — `cap::6.3.2.1`

**Texto propio:**

```
6.3.2.1. Cálculo de las posiciones.
Para el cálculo de las exigencias por riesgo específico y riesgo general de
mercado, las posiciones en derivados deberán convertirse en nocionales:
i) Los futuros y “forwards” sobre acciones individuales deberán declararse
al precio de mercado del subyacente.
ii) Los futuros sobre índices bursátiles deberán declararse al valor de mer-
cado del nocional de la cartera de acciones subyacente.
iii) Los “swaps” de acciones se considerarán como dos posiciones nociona-
les.
iv) Las opciones sobre acciones e índices bursátiles se excluirán junto con
sus subyacentes –si se utiliza el método simplificado– o bien se incorpo-
rarán a la medida de riesgo general de mercado –si se utiliza el método
delta-plus–.
```
**Heredado:** Sección 6. Capital mínimo por riesgo de mercado. / 6.3. Exigencia de capital por riesgo de posiciones en acciones. / La exigencia de capital por el riesgo de mantener posiciones en acciones en la cartera de ne- gociación alcanza a las posiciones compradas y vendidas en acciones ordinarias, títulos de deuda convertibles que se comporten como acciones y los compromisos para ad… / 6.3.2. Tratamiento de los derivados sobre acciones. / A excepción de las opciones sobre acciones e índices bursátiles, que se tratan en el punto 6.6., los restantes derivados sobre acciones y las posiciones fuera de balance sensibles a los cambios en los precios de mercado deberán incluirse en el cómputo de la ex…

**ANTERIOR** — error: None; salida: 2283 tokens

- Operacion «Conversión de derivados — posiciones nocionales»: Conversión de posiciones en derivados a su equivalente nocional para el cálculo de exigencias por riesgo específico y riesgo general de mercado ‖ tramo (exacta): «las posiciones en derivados deberán convertirse en nocionales»
- Obligacion «Declaración futuros/forwards — precio de mercado»: Los futuros y forwards sobre acciones individuales deben declararse al precio de mercado del subyacente ‖ tramo (exacta): «Los futuros y "forwards" sobre acciones individuales deberán declararse al precio de mercado del subyacente»
- Obligacion «Declaración futuros — valor nocional índices»: Los futuros sobre índices bursátiles deben declararse al valor de mercado del nocional de la cartera de acciones subyacente ‖ tramo (exacta): «Los futuros sobre índices bursátiles deberán declararse al valor de mercado del nocional de la cartera de acciones subyacente»
- Obligacion «Tratamiento swaps — dos posiciones nocionales»: Los swaps de acciones se consideran como dos posiciones nocionales ‖ tramo (exacta): «Los "swaps" de acciones se considerarán como dos posiciones nocionales»
- Obligacion «Exclusión de opciones — método simplificado»: Las opciones sobre acciones e índices bursátiles se excluyen junto con sus subyacentes cuando se utiliza el método simplificado ‖ tramo (exacta): «Las opciones sobre acciones e índices bursátiles se excluirán junto con sus subyacentes –si se utiliza el método simplificado–»
- Obligacion «Incorporación de opciones — método delta-plus»: Las opciones sobre acciones e índices bursátiles se incorporan a la medida de riesgo general de mercado cuando se utiliza el método delta-plus ‖ tramo (no): «Las opciones sobre acciones e índices bursátiles se incorporarán a la medida de riesgo general de mercado –si se utiliza el método delta-plus–»
- Condicion «Aplicación del método simplificado»: Se verifica cuando se utiliza el método simplificado para el tratamiento de opciones ‖ tramo (exacta): «si se utiliza el método simplificado»
- Condicion «Aplicación del método delta-plus»: Se verifica cuando se utiliza el método delta-plus para el tratamiento de opciones ‖ tramo (exacta): «si se utiliza el método delta-plus»
  - Operacion:Conversión de derivados — posiciones nocionales --establecida_en--> TextoOrdenado:TO Capitales Mínimos
  - Obligacion:Declaración futuros/forwards — precio de mercado --establecida_en--> TextoOrdenado:TO Capitales Mínimos
  - Obligacion:Declaración futuros — valor nocional índices --establecida_en--> TextoOrdenado:TO Capitales Mínimos
  - Obligacion:Tratamiento swaps — dos posiciones nocionales --establecida_en--> TextoOrdenado:TO Capitales Mínimos
  - Obligacion:Exclusión de opciones — método simplificado --establecida_en--> TextoOrdenado:TO Capitales Mínimos
  - Obligacion:Incorporación de opciones — método delta-plus --establecida_en--> TextoOrdenado:TO Capitales Mínimos
  - Condicion:Aplicación del método simplificado --establecida_en--> TextoOrdenado:TO Capitales Mínimos
  - Condicion:Aplicación del método delta-plus --establecida_en--> TextoOrdenado:TO Capitales Mínimos
  - Obligacion:Declaración futuros/forwards — precio de mercado --aplica_a--> las entidades
  - Obligacion:Declaración futuros — valor nocional índices --aplica_a--> las entidades
  - Obligacion:Tratamiento swaps — dos posiciones nocionales --aplica_a--> las entidades
  - Obligacion:Exclusión de opciones — método simplificado --aplica_a--> las entidades
  - Obligacion:Incorporación de opciones — método delta-plus --aplica_a--> las entidades
  - rechazo: firma_invalida: relations[13]: Obligacion --condiciona--> Condicion
  - rechazo: firma_invalida: relations[14]: Obligacion --condiciona--> Condicion
  - omisión fuera_de_tipos (exacta): «Para el cálculo de las exigencias por riesgo específico y riesgo general de mercado» — nota: Disposición introductoria que enuncia el ámbito de aplicación de las obligaciones siguientes; no es ella misma una norma sino el antecedente…
  - heredado_compuesto: 0

**P3C** — error: None; salida: 1484 tokens

- Operacion «Conversión en nocionales de derivados»: Para el cálculo de las exigencias por riesgo específico y riesgo general de mercado, las posiciones en derivados deberán convertirse en nocionales ‖ tramo (exacta): «las posiciones en derivados deberán convertirse en nocionales»
- Obligacion «Declarar futuros/forwards en acciones al precio de mercado»: Los futuros y forwards sobre acciones individuales deberán declararse al precio de mercado del subyacente ‖ tramo (exacta): «Los futuros y "forwards" sobre acciones individuales deberán declararse al precio de mercado del subyacente»
- Obligacion «Declarar futuros sobre índices al valor de mercado»: Los futuros sobre índices bursátiles deberán declararse al valor de mercado del nocional de la cartera de acciones subyacente ‖ tramo (exacta): «Los futuros sobre índices bursátiles deberán declararse al valor de mercado del nocional de la cartera de acciones subyacente»
- Operacion «Tratamiento de swaps de acciones como dos posiciones nocionales»: Los swaps de acciones se considerarán como dos posiciones nocionales ‖ tramo (exacta): «Los "swaps" de acciones se considerarán como dos posiciones nocionales»
- Excepcion «Exclusión de opciones — método simplificado»: Las opciones sobre acciones e índices bursátiles se excluirán del cómputo de la exigencia, junto con sus subyacentes, cuando se utiliza el método simplificado ‖ tramo (exacta): «Las opciones sobre acciones e índices bursátiles se excluirán junto con sus subyacentes –si se utiliza el método simplificado–»
- Obligacion «Incorporar opciones a medida de riesgo — método delta-plus»: Las opciones sobre acciones e índices bursátiles se incorporarán a la medida de riesgo general de mercado cuando se utiliza el método delta-plus ‖ tramo (exacta): «Las opciones sobre acciones e índices bursátiles se [...] incorporarán a la medida de riesgo general de mercado –si se utiliza el método delta-plus–»
  - Operacion:Conversión en nocionales de derivados --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Obligacion:Declarar futuros/forwards en acciones al precio de mercado --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Obligacion:Declarar futuros sobre índices al valor de mercado --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Operacion:Tratamiento de swaps de acciones como dos posiciones nocionales --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Excepcion:Exclusión de opciones — método simplificado --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Obligacion:Incorporar opciones a medida de riesgo — método delta-plus --establecida_en--> TextoOrdenado:Capitales Mínimos
  - omisión fuera_de_tipos (exacta): «Para el cálculo de las exigencias por riesgo específico y riesgo general de mercado» — nota: Enunciado de finalidad/alcance de aplicación de las normas que siguen; no prescribe conducta de un sujeto sino que enuncia el propósito regu…
  - heredado_compuesto: 0

## Ficha 15 — `ctacte::3.2.2`

**Texto propio:**

```
3.2.2. Existencia de tachaduras o enmiendas no salvadas por el librador.
```
**Heredado:** Sección 3. Cheques. / 3.2. Títulos que carecen de valor como cheques. / El título respecto del que se presentare alguna de las siguientes situaciones, enumeradas taxativamente a continuación, no valdrá como cheque: / Los títulos devueltos por esas situaciones no podrán ser objeto de nuevas presentaciones.

**ANTERIOR** — error: None; salida: 590 tokens

- Restriccion «Cheque con tachaduras o enmiendas no salvadas»: El título respecto del que se presentare existencia de tachaduras o enmiendas no salvadas por el librador no valdrá como cheque ‖ tramo (exacta): «Existencia de tachaduras o enmiendas no salvadas por el librador»
  - Restriccion:Cheque con tachaduras o enmiendas no salvadas --establecida_en--> TextoOrdenado:Cuentas de corresponsalía
  - Restriccion:Cheque con tachaduras o enmiendas no salvadas --aplica_a--> las entidades
  - rechazo: ref_colgante: relations[1] (prohibe): source='e1' target='e2'
  - rechazo: predicado_invalido: relations[2]: 'None'
  - heredado_compuesto: 0

**P3C** — error: None; salida: 585 tokens

- Restriccion «Tachaduras o enmiendas no salvadas — inválido como cheque»: El título que presente tachaduras o enmiendas no salvadas por el librador no valdrá como cheque. ‖ tramo (exacta): «Existencia de tachaduras o enmiendas no salvadas por el librador»
- Restriccion «Prohibición de presentación — títulos sin valor»: Los títulos devueltos por las situaciones enumeradas en 3.2, entre ellas la existencia de tachaduras o enmiendas no salvadas, no podrán ser objeto de nuevas presentaciones. ‖ tramo (exacta): «Los títulos devueltos por esas situaciones no podrán ser objeto de nuevas presentaciones»
  - Restriccion:Tachaduras o enmiendas no salvadas — inválido como cheque --establecida_en--> TextoOrdenado:Cheques
  - Restriccion:Prohibición de presentación — títulos sin valor --establecida_en--> TextoOrdenado:Cheques
  - omisión meta_normativo (exacta): «enumeradas taxativamente a continuación» — nota: Referencia a la estructura de enumeración, sin contenido normativo extraíble en sí mismo
  - heredado_compuesto: 0

## Ficha 16 — `ext::13.1.4`

**Texto propio:**

```
13.1.4. Si se trata de pagos de deudas por servicios de no residentes que fueron prestados
y/o devengados hasta el 12/12/23, la entidad deberá verificar que la operación
encuadra en alguna de las situaciones previstas en el punto 13.4.
Los clientes podrán suscribir Bonos para la Reconstrucción de una Argentina Libre
(BOPREAL) por hasta el monto de la deuda pendiente de pago por estas
operaciones en la medida que se cumplan los requisitos previstos en el punto 4.5.
```
**Heredado:** Sección 13. Pagos de servicios prestados por no residentes. / 13.1. Disposiciones generales. / Las entidades podrán dar acceso al mercado de cambios por pagos de servicios prestados por no residentes en la medida que se cumplan las siguientes condiciones: / Los casos que no encuadren en lo expuesto precedentemente quedan sujetos a la conformidad previa del BCRA, debiendo los pedidos ser canalizados por una entidad autorizada a realizar este tipo de pagos.

**ANTERIOR** — error: None; salida: 1679 tokens

- Condicion «Servicios prestados hasta 12/12/23»: El pago debe corresponder a servicios prestados por no residentes que fueron prestados y/o devengados hasta el 12 de diciembre de 2023 ‖ tramo (exacta): «Si se trata de pagos de deudas por servicios de no residentes que fueron prestados y/o devengados hasta el 12/12/23» ‖ umbrales: ['hasta el 12/12/23']
- Obligacion «Verificar operación encuadra punto 13.4»: La entidad deberá verificar que la operación de pago de deudas por servicios de no residentes prestados hasta el 12/12/23 encuadra en alguna de las situaciones previstas en el punto 13.4 ‖ tramo (exacta): «la entidad deberá verificar que la operación encuadra en alguna de las situaciones previstas en el punto 13.4»
- Potestad «Suscripción BOPREAL hasta monto deuda»: Los clientes podrán suscribir Bonos para la Reconstrucción de una Argentina Libre (BOPREAL) por hasta el monto de la deuda pendiente de pago derivada de los pagos de servicios de no residentes, siempre que cumplan los requisitos del punto 4.5 ‖ tramo (exacta): «Los clientes podrán suscribir Bonos para la Reconstrucción de una Argentina Libre (BOPREAL) por hasta el monto de la deuda pendiente de pago por estas operaciones en la medida que se cumplan los requi…»
- Condicion «Requisitos cumplidos punto 4.5»: Condición de que se cumplan los requisitos previstos en el punto 4.5 ‖ tramo (exacta): «en la medida que se cumplan los requisitos previstos en el punto 4.5»
- Operacion «Pago deuda servicios no residentes»: Pago de deudas por servicios prestados por no residentes hasta el 12/12/23 ‖ tramo (exacta): «pagos de deudas por servicios de no residentes»
  - Condicion:Servicios prestados hasta 12/12/23 --establecida_en--> TextoOrdenado:Exterior - Cambios
  - Obligacion:Verificar operación encuadra punto 13.4 --establecida_en--> TextoOrdenado:Exterior - Cambios
  - Potestad:Suscripción BOPREAL hasta monto deuda --establecida_en--> TextoOrdenado:Exterior - Cambios
  - Condicion:Requisitos cumplidos punto 4.5 --establecida_en--> TextoOrdenado:Exterior - Cambios
  - Operacion:Pago deuda servicios no residentes --establecida_en--> TextoOrdenado:Exterior - Cambios
  - Obligacion:Verificar operación encuadra punto 13.4 --aplica_a--> la entidad
  - Condicion:Servicios prestados hasta 12/12/23 --condicion_de--> Obligacion:Verificar operación encuadra punto 13.4
  - Obligacion:Verificar operación encuadra punto 13.4 --regula--> Operacion:Pago deuda servicios no residentes
  - Condicion:Requisitos cumplidos punto 4.5 --condicion_de--> Potestad:Suscripción BOPREAL hasta monto deuda
  - Potestad:Suscripción BOPREAL hasta monto deuda --aplica_a--> Los clientes
  - omisión relacion_sin_predicado (exacta): «operación encuadra en alguna de las situaciones previstas en el punto 13.4» — nota: se establecería un predicado como 'referencia' o 'remisión_a' entre e2 y el contenido del punto 13.4, pero las remisiones a otros puntos no …
  - heredado_compuesto: 0

**P3C** — error: None; salida: 1285 tokens

- Condicion «Pagos de servicios de no residentes hasta 12/12/23»: La operación corresponde a pagos de deudas por servicios prestados o devengados por no residentes hasta el 12 de diciembre de 2023 ‖ tramo (exacta): «Si se trata de pagos de deudas por servicios de no residentes que fueron prestados y/o devengados hasta el 12/12/23» ‖ umbrales: ['hasta el 12/12/23']
- Obligacion «Verificar encuadre operación en situaciones previstas punto 13.4»: La entidad deberá verificar que la operación se encuadra en alguna de las situaciones previstas en el punto 13.4 ‖ tramo (exacta): «la entidad deberá verificar que la operación encuadra en alguna de las situaciones previstas en el punto 13.4»
- Potestad «Suscripción BOPREAL hasta monto deuda pendiente»: Los clientes pueden suscribir Bonos para la Reconstrucción de una Argentina Libre (BOPREAL) por un monto que no exceda la deuda pendiente de pago por estas operaciones ‖ tramo (exacta): «Los clientes podrán suscribir Bonos para la Reconstrucción de una Argentina Libre (BOPREAL) por hasta el monto de la deuda pendiente de pago»
- Condicion «Cumplimiento requisitos punto 4.5 para suscripción BOPREAL»: Se cumplen los requisitos previstos en el punto 4.5 ‖ tramo (exacta): «en la medida que se cumplan los requisitos previstos en el punto 4.5»
  - Condicion:Pagos de servicios de no residentes hasta 12/12/23 --establecida_en--> TextoOrdenado:Exterior - Cambios
  - Obligacion:Verificar encuadre operación en situaciones previstas punto 13.4 --establecida_en--> TextoOrdenado:Exterior - Cambios
  - Condicion:Pagos de servicios de no residentes hasta 12/12/23 --condicion_de--> Obligacion:Verificar encuadre operación en situaciones previstas punto 13.4
  - Potestad:Suscripción BOPREAL hasta monto deuda pendiente --establecida_en--> TextoOrdenado:Exterior - Cambios
  - Condicion:Cumplimiento requisitos punto 4.5 para suscripción BOPREAL --establecida_en--> TextoOrdenado:Exterior - Cambios
  - Condicion:Cumplimiento requisitos punto 4.5 para suscripción BOPREAL --condicion_de--> Potestad:Suscripción BOPREAL hasta monto deuda pendiente
  - Obligacion:Verificar encuadre operación en situaciones previstas punto 13.4 --aplica_a--> la entidad
  - omisión meta_normativo (exacta): «Las entidades podrán dar acceso al mercado de cambios por pagos de servicios prestados por no residentes en la medida que se cumplan las siguientes condiciones:» — nota: El encabezado del ítem (punto 13.1) anuncia la composición de la norma: se compone en cada ítem con su contenido específico, no se extrae en…
  - heredado_compuesto: 0

## Ficha 17 — `ext::3.5.3.4`

**Texto propio:**

```
3.5.3.4. Precancelación de capital e intereses en forma simultánea con la liquidación
de un nuevo endeudamiento financiero otorgado por una entidad financiera
local a partir de una línea de crédito del exterior.
i) la precancelación de capital e intereses sea efectuada de manera
simultánea con los fondos liquidados de un nuevo endeudamiento
financiero otorgado por una entidad financiera local a partir de una línea
de crédito del exterior;
ii) la vida promedio del nuevo endeudamiento sea mayor a la vida
promedio remanente de la deuda que se precancela; y
iii) el monto acumulado de los vencimientos de capital del nuevo
endeudamiento en ningún momento, hasta la fecha de vencimiento de la
deuda que se cancela, podrá superar el monto que hubieran acumulado
los vencimientos de capital de la deuda que se cancela.
```
**Heredado:** Sección 3. Disposiciones específicas para los egresos por el mercado de cambios / Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–, adicionalmente a los requisitos y condiciones específicas detalladas… / 3.5. Pagos de títulos de deuda suscriptos en el exterior y endeudamientos financieros con el / exterior. Las entidades podrán dar acceso al mercado de cambios para realizar pagos de capital o intereses de títulos de deuda con registro público en el exterior, otros endeudamientos financieros con el exterior y títulos de deuda con registro público en el p… / 3.5.3. El acceso al mercado de cambios se produce con una anterioridad no mayor a los 3 / (tres) días hábiles a la fecha de vencimiento del servicio de capital o interés a pagar. En el caso de que se trate de un pago de capital de títulos de deuda emitidos a partir del 08/11/24 que se concreta con una transferencia al exterior, el acceso al mercado… / i) 12 (doce) meses si el título fue emitido entre el 08/11/24 y el 20/04/25. ii) 6 (seis) meses si el título fue emitido entre 21/04/25 y el 15/05/25. iii) 18 (dieciocho) meses si el título fue emitido a partir del 16/05/25. / El acceso al mercado de cambios antes de lo indicado requerirá la conformidad previa del BCRA excepto que el deudor encuadre en alguna de las siguientes situaciones y se cumplan la totalidad de las condiciones estipuladas en cada caso:

**ANTERIOR** — error: None; salida: 1891 tokens

- Condicion «Simultaneidad precancelación — liquidación nuevo endeudamiento»: La precancelación de capital e intereses debe efectuarse de manera simultánea con la liquidación de fondos de un nuevo endeudamiento financiero otorgado por una entidad financiera local a partir de una línea de crédito del exterior. ‖ tramo (exacta): «la precancelación de capital e intereses sea efectuada de manera simultánea con los fondos liquidados de un nuevo endeudamiento financiero otorgado por una entidad financiera local a partir de una lín…»
- Condicion «Vida promedio nuevo endeudamiento mayor que vida promedio remanente»: La vida promedio del nuevo endeudamiento debe ser mayor a la vida promedio remanente de la deuda que se precancela. ‖ tramo (exacta): «la vida promedio del nuevo endeudamiento sea mayor a la vida promedio remanente de la deuda que se precancela»
- Restriccion «Límite vencimientos capital — nuevo endeudamiento»: El monto acumulado de los vencimientos de capital del nuevo endeudamiento no podrá superar en ningún momento, hasta la fecha de vencimiento de la deuda que se cancela, el monto acumulado de los vencimientos de capital de la deuda que se cancela. ‖ tramo (exacta): «el monto acumulado de los vencimientos de capital del nuevo endeudamiento en ningún momento, hasta la fecha de vencimiento de la deuda que se cancela, podrá superar el monto que hubieran acumulado los…» ‖ umbrales: ['el monto acumulado de los vencimientos de capital del nuevo endeudamiento en ningún momento, hasta la fecha de vencimiento de la deuda que se cancela, podrá superar el monto que hubieran acumulado los vencimientos de capital de la deuda que se cancela']
- Operacion «Acceso al mercado de cambios — precancelación simultánea»: Acceso al mercado de cambios para precancelación de capital e intereses de títulos de deuda, efectuada de manera simultánea con la liquidación de fondos de un nuevo endeudamiento financiero otorgado por una entidad financiera local a partir de una línea de crédito del exterior. ‖ tramo (exacta): «Precancelación de capital e intereses en forma simultánea con la liquidación de un nuevo endeudamiento financiero otorgado por una entidad financiera local a partir de una línea de crédito del exterio…»
- Excepcion «Excepción — Conformidad previa BCRA en precancelación simultánea»: No se requiere conformidad previa del BCRA para acceso al mercado de cambios cuando el deudor encuadra en las situaciones especificadas (precancelación simultánea) y se cumplen la totalidad de las condiciones estipuladas. ‖ tramo (exacta): «El acceso al mercado de cambios antes de lo indicado requerirá la conformidad previa del BCRA excepto que el deudor encuadre en alguna de las siguientes situaciones y se cumplan la totalidad de las co…»
  - Condicion:Simultaneidad precancelación — liquidación nuevo endeudamiento --establecida_en--> TextoOrdenado:Exterior - Cambios
  - Condicion:Vida promedio nuevo endeudamiento mayor que vida promedio remanente --establecida_en--> TextoOrdenado:Exterior - Cambios
  - Restriccion:Límite vencimientos capital — nuevo endeudamiento --establecida_en--> TextoOrdenado:Exterior - Cambios
  - Operacion:Acceso al mercado de cambios — precancelación simultánea --establecida_en--> TextoOrdenado:Exterior - Cambios
  - Excepcion:Excepción — Conformidad previa BCRA en precancelación simultánea --establecida_en--> TextoOrdenado:Exterior - Cambios
  - Condicion:Simultaneidad precancelación — liquidación nuevo endeudamiento --condicion_de--> Operacion:Acceso al mercado de cambios — precancelación simultánea
  - Condicion:Vida promedio nuevo endeudamiento mayor que vida promedio remanente --condicion_de--> Operacion:Acceso al mercado de cambios — precancelación simultánea
  - Restriccion:Límite vencimientos capital — nuevo endeudamiento --limita--> Operacion:Acceso al mercado de cambios — precancelación simultánea
  - Excepcion:Excepción — Conformidad previa BCRA en precancelación simultánea --exceptua--> Restriccion:Límite vencimientos capital — nuevo endeudamiento
  - Operacion:Acceso al mercado de cambios — precancelación simultánea --aplica_a--> Las entidades
  - omisión meta_normativo (exacta): «El acceso al mercado de cambios antes de lo indicado requerirá la conformidad previa del BCRA excepto que» — nota: Contenido meta-normativo: negación de requisito (conformidad previa) que se suspende por la excepción; no prescribe conducta sino la ausenci…
  - heredado_compuesto: 1

**P3C** — error: None; salida: 1491 tokens

- Operacion «Precancelación de capital e intereses con nuevo endeudamiento»: Precancelación de capital e intereses efectuada de manera simultánea con los fondos liquidados de un nuevo endeudamiento financiero otorgado por una entidad financiera local a partir de una línea de crédito del exterior ‖ tramo (exacta): «precancelación de capital e intereses sea efectuada de manera simultánea con los fondos liquidados de un nuevo endeudamiento financiero otorgado por una entidad financiera local a partir de una línea …»
- Condicion «Vida promedio del nuevo endeudamiento mayor a remanente»: La vida promedio del nuevo endeudamiento debe ser mayor a la vida promedio remanente de la deuda que se precancela ‖ tramo (exacta): «la vida promedio del nuevo endeudamiento sea mayor a la vida promedio remanente de la deuda que se precancela»
- Restriccion «Límite monto acumulado vencimientos capital nuevo endeudamiento»: El monto acumulado de los vencimientos de capital del nuevo endeudamiento no podrá superar en ningún momento, hasta la fecha de vencimiento de la deuda que se cancela, el monto que hubieran acumulado los vencimientos de capital de la deuda que se cancela ‖ tramo (exacta): «el monto acumulado de los vencimientos de capital del nuevo endeudamiento en ningún momento, hasta la fecha de vencimiento de la deuda que se cancela, podrá superar el monto que hubieran acumulado los…» ‖ umbrales: ['podrá superar el monto que hubieran acumulado los vencimientos de capital de la deuda que se cancela']
- Excepcion «Excepción acceso mercado cambios sin conformidad BCRA»: Cuando se cumplen las condiciones de vida promedio del nuevo endeudamiento y límite de monto acumulado, el acceso al mercado de cambios no requerirá conformidad previa del BCRA ‖ tramo (exacta): «la precancelación de capital e intereses sea efectuada de manera simultánea con los fondos liquidados de un nuevo endeudamiento financiero otorgado por una entidad financiera local a partir de una lín…»
  - Operacion:Precancelación de capital e intereses con nuevo endeudamiento --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Condicion:Vida promedio del nuevo endeudamiento mayor a remanente --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Restriccion:Límite monto acumulado vencimientos capital nuevo endeudamiento --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Excepcion:Excepción acceso mercado cambios sin conformidad BCRA --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Condicion:Vida promedio del nuevo endeudamiento mayor a remanente --condicion_de--> Operacion:Precancelación de capital e intereses con nuevo endeudamiento
  - Restriccion:Límite monto acumulado vencimientos capital nuevo endeudamiento --limita--> Operacion:Precancelación de capital e intereses con nuevo endeudamiento
  - rechazo: firma_invalida: relations[5]: Restriccion --condicion_de--> Operacion
  - omisión relacion_sin_predicado (no): «el acceso al mercado de cambios no requerirá conformidad previa del BCRA excepto que...» — nota: La excepción a la exigencia de conformidad del BCRA está implícita en el contexto heredado (punto 3.5.3) pero no se enuncia explícitamente e…
  - heredado_compuesto: 0

## Ficha 18 — `ext::3.5.3.1`

**Texto propio:**

```
3.5.3.1. Precancelación de capital e intereses con la liquidación de fondos
ingresados desde el exterior por la emisión de un nuevo título de deuda
comprendido en este punto 3.5.
i) la precancelación de capital sea efectuada en manera simultánea con la
liquidación de los fondos ingresados desde el exterior por la emisión de
un nuevo título de deuda comprendido en este punto 3.5. emitido en el
marco de una operación de refinanciación, recompra y/o rescate
anticipado de deuda.
a) el nuevo título de deuda contempla 1 (un) año de gracia para el
pago de capital y su vida promedio es al menos 2 (dos) años mayor
a la vida promedio remanente de la deuda que se precancela; y
b) el monto acumulado de los vencimientos de capital del nuevo
endeudamiento en ningún momento podrá superar, hasta la fecha
de vencimiento de la deuda que se cancela, el monto que hubieran
acumulado los vencimientos de capital de la deuda que se cancela.
ii) la precancelación de intereses corresponde a los intereses devengados
por la deuda refinanciada hasta la fecha de cierre de la operación de
recompra y/o rescate, sin necesidad de que exista una liquidación de
fondos por el monto equivalente;
Adicionalmente, la entidad podrá darle acceso al mercado de cambios al
cliente para:
iii) pagar en concepto de prima de recompra, de rescate anticipado o
similar hasta el equivalente del 5% (cinco por ciento) del monto del
capital de la deuda recomprada y/o rescatada, en la medida que el pago
se concrete de manera simultánea con una liquidación de fondos
ingresados desde el exterior por el nuevo título de deuda que exceda al
monto de capital que se precancela, como mínimo, por un monto
equivalente al monto de la prima abonada.
iv)pagar a la fecha de cierre de la operación de recompra y/o rescate, sin
necesidad de que exista una liquidación de fondos por el monto
equivalente, los gastos de emisión u otros servicios prestados por no
residentes en el marco de la emisión de los nuevos títulos de deuda
emitidos y/o la operación de recompra y/o rescate.
```
**Heredado:** Sección 3. Disposiciones específicas para los egresos por el mercado de cambios / Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–, adicionalmente a los requisitos y condiciones específicas detalladas… / 3.5. Pagos de títulos de deuda suscriptos en el exterior y endeudamientos financieros con el / exterior. Las entidades podrán dar acceso al mercado de cambios para realizar pagos de capital o intereses de títulos de deuda con registro público en el exterior, otros endeudamientos financieros con el exterior y títulos de deuda con registro público en el p… / 3.5.3. El acceso al mercado de cambios se produce con una anterioridad no mayor a los 3 / (tres) días hábiles a la fecha de vencimiento del servicio de capital o interés a pagar. En el caso de que se trate de un pago de capital de títulos de deuda emitidos a partir del 08/11/24 que se concreta con una transferencia al exterior, el acceso al mercado… / i) 12 (doce) meses si el título fue emitido entre el 08/11/24 y el 20/04/25. ii) 6 (seis) meses si el título fue emitido entre 21/04/25 y el 15/05/25. iii) 18 (dieciocho) meses si el título fue emitido a partir del 16/05/25. / El acceso al mercado de cambios antes de lo indicado requerirá la conformidad previa del BCRA excepto que el deudor encuadre en alguna de las siguientes situaciones y se cumplan la totalidad de las condiciones estipuladas en cada caso:

**ANTERIOR** — error: None; salida: 4008 tokens

- Condicion «Precancelación simultánea con liquidación de fondos»: La precancelación de capital debe efectuarse simultáneamente con la liquidación de fondos ingresados desde el exterior por la emisión de un nuevo título de deuda comprendido en este punto 3.5. ‖ tramo (exacta): «la precancelación de capital sea efectuada en manera simultánea con la liquidación de los fondos ingresados desde el exterior por la emisión de un nuevo título de deuda comprendido en este punto 3.5.»
- Condicion «Operación dentro de refinanciación, recompra o rescate»: La emisión del nuevo título debe efectuarse en el marco de una operación de refinanciación, recompra y/o rescate anticipado de deuda. ‖ tramo (exacta): «emitido en el marco de una operación de refinanciación, recompra y/o rescate anticipado de deuda»
- Restriccion «Período de gracia — nuevo título 1 año mínimo»: El nuevo título de deuda debe contemplar un período de gracia de 1 (un) año para el pago de capital. ‖ tramo (exacta): «el nuevo título de deuda contempla 1 (un) año de gracia para el pago de capital»
- Restriccion «Vida promedio — diferencia mínima 2 años»: La vida promedio del nuevo título debe ser al menos 2 (dos) años mayor a la vida promedio remanente de la deuda que se precancela. ‖ tramo (exacta): «su vida promedio es al menos 2 (dos) años mayor a la vida promedio remanente de la deuda que se precancela» ‖ umbrales: ['al menos 2 (dos) años mayor']
- Restriccion «Monto acumulado de vencimientos — no superar deuda original»: El monto acumulado de los vencimientos de capital del nuevo endeudamiento no podrá superar, en ningún momento hasta la fecha de vencimiento de la deuda que se cancela, el monto que hubieran acumulado los vencimientos de capital de la deuda que se cancela. ‖ tramo (exacta): «el monto acumulado de los vencimientos de capital del nuevo endeudamiento en ningún momento podrá superar, hasta la fecha de vencimiento de la deuda que se cancela, el monto que hubieran acumulado los…»
- Condicion «Intereses devengados hasta cierre de operación»: La precancelación de intereses debe corresponder únicamente a los intereses devengados por la deuda refinanciada hasta la fecha de cierre de la operación de recompra y/o rescate. ‖ tramo (exacta): «la precancelación de intereses corresponde a los intereses devengados por la deuda refinanciada hasta la fecha de cierre de la operación de recompra y/o rescate»
- Restriccion «Prima de recompra/rescate — máximo 5% del capital»: La entidad podrá permitir al cliente pagar en concepto de prima de recompra, rescate anticipado o similar hasta el equivalente del 5% (cinco por ciento) del monto del capital de la deuda recomprada y/o rescatada. ‖ tramo (exacta): «pagar en concepto de prima de recompra, de rescate anticipado o similar hasta el equivalente del 5% (cinco por ciento) del monto del capital de la deuda recomprada y/o rescatada» ‖ umbrales: ['hasta el equivalente del 5% (cinco por ciento)']
- Condicion «Liquidación simultánea de fondos — mínimo prima abonada»: El pago de la prima debe concretarse de manera simultánea con una liquidación de fondos ingresados desde el exterior por el nuevo título de deuda que exceda al monto de capital que se precancela por un monto mínimo equivalente al monto de la prima abonada. ‖ tramo (exacta): «el pago se concrete de manera simultánea con una liquidación de fondos ingresados desde el exterior por el nuevo título de deuda que exceda al monto de capital que se precancela, como mínimo, por un m…»
- Potestad «Acceso a cambios — pago de prima de recompra/rescate»: La entidad podrá otorgar acceso al mercado de cambios al cliente para pagar prima de recompra, rescate anticipado o similar. ‖ tramo (no): «la entidad podrá darle acceso al mercado de cambios al cliente para pagar en concepto de prima de recompra, de rescate anticipado o similar»
- Potestad «Acceso a cambios — gastos de emisión y servicios»: La entidad podrá permitir al cliente acceso al mercado de cambios para pagar, a la fecha de cierre de la operación de recompra y/o rescate, sin necesidad de liquidación de fondos equivalente, los gastos de emisión u otros servicios prestados por no residentes en el marco de la emisión de nuevos títu… ‖ tramo (exacta): «pagar a la fecha de cierre de la operación de recompra y/o rescate, sin necesidad de que exista una liquidación de fondos por el monto equivalente, los gastos de emisión u otros servicios prestados po…»
- Operacion «Precancelación de capital e intereses»: Precancelación de capital e intereses de títulos de deuda, realizada de manera simultánea con la liquidación de fondos ingresados desde el exterior por la emisión de un nuevo título de deuda en el marco de operaciones de refinanciación, recompra y/o rescate anticipado. ‖ tramo (exacta): «Precancelación de capital e intereses con la liquidación de fondos ingresados desde el exterior por la emisión de un nuevo título de deuda comprendido en este punto 3.5.»
- Operacion «Pago de prima de recompra/rescate»: Pago de prima de recompra, rescate anticipado o similar en operaciones de refinanciación de deuda. ‖ tramo (exacta): «pagar en concepto de prima de recompra, de rescate anticipado o similar»
- Operacion «Pago de gastos de emisión y servicios»: Pago de gastos de emisión u otros servicios prestados por no residentes en el marco de la emisión de nuevos títulos de deuda y/o la operación de recompra y/o rescate. ‖ tramo (exacta): «pagar a la fecha de cierre de la operación de recompra y/o rescate, sin necesidad de que exista una liquidación de fondos por el monto equivalente, los gastos de emisión u otros servicios prestados po…»
  - Condicion:Precancelación simultánea con liquidación de fondos --establecida_en--> TextoOrdenado:Exterior — Cambios
  - Condicion:Operación dentro de refinanciación, recompra o rescate --establecida_en--> TextoOrdenado:Exterior — Cambios
  - Restriccion:Período de gracia — nuevo título 1 año mínimo --establecida_en--> TextoOrdenado:Exterior — Cambios
  - Restriccion:Vida promedio — diferencia mínima 2 años --establecida_en--> TextoOrdenado:Exterior — Cambios
  - Restriccion:Monto acumulado de vencimientos — no superar deuda original --establecida_en--> TextoOrdenado:Exterior — Cambios
  - Condicion:Intereses devengados hasta cierre de operación --establecida_en--> TextoOrdenado:Exterior — Cambios
  - Restriccion:Prima de recompra/rescate — máximo 5% del capital --establecida_en--> TextoOrdenado:Exterior — Cambios
  - Condicion:Liquidación simultánea de fondos — mínimo prima abonada --establecida_en--> TextoOrdenado:Exterior — Cambios
  - Potestad:Acceso a cambios — pago de prima de recompra/rescate --establecida_en--> TextoOrdenado:Exterior — Cambios
  - Potestad:Acceso a cambios — gastos de emisión y servicios --establecida_en--> TextoOrdenado:Exterior — Cambios
  - Operacion:Precancelación de capital e intereses --establecida_en--> TextoOrdenado:Exterior — Cambios
  - Operacion:Pago de prima de recompra/rescate --establecida_en--> TextoOrdenado:Exterior — Cambios
  - Operacion:Pago de gastos de emisión y servicios --establecida_en--> TextoOrdenado:Exterior — Cambios
  - Condicion:Precancelación simultánea con liquidación de fondos --condicion_de--> Operacion:Precancelación de capital e intereses
  - Condicion:Operación dentro de refinanciación, recompra o rescate --condicion_de--> Operacion:Precancelación de capital e intereses
  - Restriccion:Período de gracia — nuevo título 1 año mínimo --limita--> Operacion:Precancelación de capital e intereses
  - Restriccion:Vida promedio — diferencia mínima 2 años --limita--> Operacion:Precancelación de capital e intereses
  - Restriccion:Monto acumulado de vencimientos — no superar deuda original --limita--> Operacion:Precancelación de capital e intereses
  - Condicion:Intereses devengados hasta cierre de operación --condicion_de--> Operacion:Precancelación de capital e intereses
  - Restriccion:Prima de recompra/rescate — máximo 5% del capital --limita--> Operacion:Pago de prima de recompra/rescate
  - Condicion:Liquidación simultánea de fondos — mínimo prima abonada --condicion_de--> Operacion:Pago de prima de recompra/rescate
  - Potestad:Acceso a cambios — pago de prima de recompra/rescate --aplica_a--> la entidad
  - Potestad:Acceso a cambios — gastos de emisión y servicios --aplica_a--> la entidad
  - omisión fuera_de_tipos (exacta): «sin necesidad de que exista una liquidación de fondos por el monto equivalente» — nota: Cláusula interpretativa/meta-normativa que niega un requisito (no es una Excepcion ni una obligación: es una aclaración de alcance). Se regi…
  - heredado_compuesto: 0

**P3C** — error: None; salida: 2436 tokens

- Operacion «Precancelación de capital con liquidación de fondos — refinanciación»: Precancelación de capital realizada simultáneamente con la liquidación de fondos ingresados desde el exterior por emisión de nuevo título de deuda en operación de refinanciación, recompra y/o rescate anticipado ‖ tramo (exacta): «la precancelación de capital sea efectuada en manera simultánea con la liquidación de los fondos ingresados desde el exterior por la emisión de un nuevo título de deuda comprendido en este punto 3.5. …»
- Condicion «Grace period y vida promedio — título nuevo»: El nuevo título debe contemplar 1 año de gracia para capital y su vida promedio debe ser al menos 2 años mayor a la vida promedio remanente de la deuda precancelada ‖ tramo (exacta): «el nuevo título de deuda contempla 1 (un) año de gracia para el pago de capital y su vida promedio es al menos 2 (dos) años mayor a la vida promedio remanente de la deuda que se precancela» ‖ umbrales: ['1 (un) año de gracia', 'al menos 2 (dos) años mayor']
- Restriccion «Límite acumulado de vencimientos de capital — deuda nueva»: El monto acumulado de vencimientos de capital del nuevo endeudamiento no puede superar el monto acumulado de vencimientos de capital de la deuda que se precancela hasta la fecha de vencimiento de esta última ‖ tramo (exacta): «el monto acumulado de los vencimientos de capital del nuevo endeudamiento en ningún momento podrá superar, hasta la fecha de vencimiento de la deuda que se cancela, el monto que hubieran acumulado los…» ‖ umbrales: ['en ningún momento podrá superar, hasta la fecha de vencimiento de la deuda que se cancela, el monto que hubieran acumulado los vencimientos de capital de la deuda que se cancela']
- Operacion «Pago de intereses devengados — deuda refinanciada»: Precancelación de intereses devengados por la deuda refinanciada hasta la fecha de cierre de la operación de recompra y/o rescate, sin requerimiento de liquidación de fondos equivalente ‖ tramo (exacta): «la precancelación de intereses corresponde a los intereses devengados por la deuda refinanciada hasta la fecha de cierre de la operación de recompra y/o rescate, sin necesidad de que exista una liquid…»
- Potestad «Acceso al mercado para prima de recompra/rescate — hasta 5%»: La entidad puede autorizar acceso al mercado de cambios para que el cliente pague prima de recompra, rescate anticipado o similar hasta el 5% del monto del capital de la deuda recomprada y/o rescatada ‖ tramo (no): «la entidad podrá darle acceso al mercado de cambios al cliente para pagar en concepto de prima de recompra, de rescate anticipado o similar hasta el equivalente del 5% (cinco por ciento) del monto del…»
- Condicion «Liquidación simultánea de fondos excedente — prima de recompra»: El pago de prima debe concretarse simultáneamente con liquidación de fondos del nuevo título que exceda el monto de capital precancelado, como mínimo, por un monto equivalente a la prima abonada ‖ tramo (exacta): «en la medida que el pago se concrete de manera simultánea con una liquidación de fondos ingresados desde el exterior por el nuevo título de deuda que exceda al monto de capital que se precancela, como…» ‖ umbrales: ['exceda al monto de capital que se precancela, como mínimo, por un monto equivalente al monto de la prima abonada']
- Potestad «Acceso al mercado para gastos de emisión y servicios — cierre operación»: La entidad puede autorizar acceso al mercado de cambios para que el cliente pague, en la fecha de cierre de operación de recompra y/o rescate, gastos de emisión u otros servicios de no residentes por nuevos títulos y/o la operación de recompra/rescate, sin requerimiento de liquidación de fondos equi… ‖ tramo (no): «la entidad podrá darle acceso al mercado de cambios al cliente para pagar a la fecha de cierre de la operación de recompra y/o rescate, sin necesidad de que exista una liquidación de fondos por el mon…»
  - Operacion:Precancelación de capital con liquidación de fondos — refinanciación --establecida_en--> TextoOrdenado:Operaciones en el exterior - Cambios
  - Condicion:Grace period y vida promedio — título nuevo --condicion_de--> Operacion:Precancelación de capital con liquidación de fondos — refinanciación
  - Restriccion:Límite acumulado de vencimientos de capital — deuda nueva --establecida_en--> TextoOrdenado:Operaciones en el exterior - Cambios
  - Operacion:Pago de intereses devengados — deuda refinanciada --establecida_en--> TextoOrdenado:Operaciones en el exterior - Cambios
  - Potestad:Acceso al mercado para prima de recompra/rescate — hasta 5% --establecida_en--> TextoOrdenado:Operaciones en el exterior - Cambios
  - Condicion:Liquidación simultánea de fondos excedente — prima de recompra --condicion_de--> Potestad:Acceso al mercado para prima de recompra/rescate — hasta 5%
  - Potestad:Acceso al mercado para gastos de emisión y servicios — cierre operació… --establecida_en--> TextoOrdenado:Operaciones en el exterior - Cambios
  - rechazo: firma_invalida: relations[3]: Restriccion --condicion_de--> Operacion
  - omisión relacion_sin_predicado (no): «Adicionalmente, la entidad podrá darle acceso al mercado de cambios al cliente para: iii) pagar... iv) pagar...» — nota: Conjunción 'adicionalmente' establece una relación de conexión entre las potestades e5/e7 y la precancelación anterior (e1), pero ningún pre…
  - heredado_compuesto: 0

## Ficha 19 — `ext::6.1.1`

**Texto propio:**

```
6.1.1. Monedas y billetes en moneda extranjera.
Comprende monedas y billetes emitidos por un estado extranjero.
```
**Heredado:** Sección 6. Definiciones. / En el marco de estas disposiciones se definen los siguientes conceptos: / 6.1. Instrumentos operados en el mercado de cambios.

**ANTERIOR** — error: None; salida: 317 tokens

- Definicion «Monedas y billetes — moneda extranjera»: Monedas y billetes emitidos por un estado extranjero. ‖ tramo (exacta): «Comprende monedas y billetes emitidos por un estado extranjero.»
  - Definicion:Monedas y billetes — moneda extranjera --establecida_en--> TextoOrdenado:Texto Ordenado Exterior — Cambios
  - heredado_compuesto: 0

**P3C** — error: None; salida: 316 tokens

- Definicion «Monedas y billetes en moneda extranjera»: Monedas y billetes emitidos por un estado extranjero. ‖ tramo (exacta): «Comprende monedas y billetes emitidos por un estado extranjero.»
  - Definicion:Monedas y billetes en moneda extranjera --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - heredado_compuesto: 0

## Ficha 20 — `polcre::5.3`

**Texto propio:**

```
5.3. Tenencia de títulos valores del exterior.
No podrán registrarse tenencias de títulos valores públicos y privados del exterior, incluidos los
títulos de deuda o participaciones correspondientes a carteras de activos entre los que se cuen-
ten títulos valores del exterior, como tampoco de certificados de depósito argentinos
(CEDEAR), excepto que se trate inversiones en títulos públicos externos emitidos por países
miembros de la OCDE cuya deuda soberana cuente con una calificación internacional no infe-
rior a “AA”.
Además, se admite la tenencia de títulos de deuda o participaciones correspondientes a carte-
ras de activos constituidas en el exterior, siempre que estén integradas exclusivamente por títu-
los valores públicos nacionales y/o privados del país, así como de “depository receipts” que co-
rrespondan a dichos títulos valores.
```
**Heredado:** Sección 5. Financiamiento a residentes en el exterior.

**ANTERIOR** — error: None; salida: 1570 tokens

- Operacion «Tenencia de títulos valores públicos externos de la OCDE»: Inversión en títulos públicos externos emitidos por países miembros de la OCDE cuya deuda soberana cuente con calificación internacional no inferior a AA ‖ tramo (exacta): «inversiones en títulos públicos externos emitidos por países miembros de la OCDE»
- Restriccion «Prohibición tenencia títulos valores externos»: No se permite registrar tenencias de títulos valores públicos y privados del exterior, incluidos títulos de deuda o participaciones de carteras de activos que contengan títulos valores del exterior, ni certificados de depósito argentinos (CEDEAR) ‖ tramo (no): «No podrán registrarse tenencias de títulos valores públicos y privados del exterior, incluidos los títulos de deuda o participaciones correspondientes a carteras de activos entre los que se cuentten t…»
- Excepcion «Excepción — títulos públicos externos OCDE AA mínimo»: Se excepciona la prohibición para inversiones en títulos públicos externos emitidos por países miembros de la OCDE con calificación de deuda soberana no inferior a AA ‖ tramo (exacta): «excepto que se trate inversiones en títulos públicos externos emitidos por países miembros de la OCDE cuya deuda soberana cuente con una calificación internacional no inferior a "AA"» ‖ umbrales: ['calificación internacional no inferior a "AA"']
- Operacion «Tenencia de títulos de carteras externas nacionales»: Tenencia de títulos de deuda o participaciones de carteras de activos constituidas en el exterior integradas exclusivamente por títulos valores públicos nacionales y/o privados del país, incluyendo depository receipts correspondientes a dichos títulos ‖ tramo (exacta): «tenencia de títulos de deuda o participaciones correspondientes a carteras de activos constituidas en el exterior, siempre que estén integradas exclusivamente por títulos valores públicos nacionales y…»
- Condicion «Integración exclusiva de cartera por títulos nacionales»: La cartera de activos debe estar integrada exclusivamente por títulos valores públicos nacionales y/o privados del país ‖ tramo (exacta): «siempre que estén integradas exclusivamente por títulos valores públicos nacionales y/o privados del país»
  - Restriccion:Prohibición tenencia títulos valores externos --establecida_en--> TextoOrdenado:Política de crédito
  - Excepcion:Excepción — títulos públicos externos OCDE AA mínimo --establecida_en--> TextoOrdenado:Política de crédito
  - Operacion:Tenencia de títulos de carteras externas nacionales --establecida_en--> TextoOrdenado:Política de crédito
  - Condicion:Integración exclusiva de cartera por títulos nacionales --establecida_en--> TextoOrdenado:Política de crédito
  - Operacion:Tenencia de títulos valores públicos externos de la OCDE --establecida_en--> TextoOrdenado:Política de crédito
  - Excepcion:Excepción — títulos públicos externos OCDE AA mínimo --exceptua--> Restriccion:Prohibición tenencia títulos valores externos
  - Restriccion:Prohibición tenencia títulos valores externos --prohibe--> Operacion:Tenencia de títulos valores públicos externos de la OCDE
  - Condicion:Integración exclusiva de cartera por títulos nacionales --condicion_de--> Operacion:Tenencia de títulos de carteras externas nacionales
  - Restriccion:Prohibición tenencia títulos valores externos --aplica_a--> las entidades
  - Operacion:Tenencia de títulos de carteras externas nacionales --aplica_a--> las entidades
  - heredado_compuesto: 0

**P3C** — error: None; salida: 1208 tokens

- Restriccion «Prohibición — tenencia títulos públicos/privados del exterior»: Prohibición de registrar tenencias de títulos valores públicos y privados del exterior, incluidos títulos de deuda o participaciones de carteras que contengan títulos del exterior, y certificados de depósito argentinos (CEDEAR). ‖ tramo (exacta): «No podrán registrarse tenencias de títulos valores públicos y privados del exterior, incluidos los títulos de deuda o participaciones correspondientes a carteras de activos entre los que se cuenten tí…»
- Excepcion «Excepción — títulos públicos OCDE con calificación mínima AA»: Excepción a la prohibición cuando se trata de inversiones en títulos públicos externos emitidos por países miembros de la OCDE con deuda soberana calificada no inferior a "AA". ‖ tramo (exacta): «excepto que se trate inversiones en títulos públicos externos emitidos por países miembros de la OCDE cuya deuda soberana cuente con una calificación internacional no inferior a "AA"» ‖ umbrales: ['no inferior a "AA"']
- Restriccion «Restricción cualitativa — carteras activos constituidas exterior»: La tenencia de títulos de deuda o participaciones de carteras constituidas en el exterior se admite solo si están integradas exclusivamente por títulos valores públicos nacionales y/o privados del país, o por "depository receipts" que correspondan a dichos títulos. ‖ tramo (exacta): «se admite la tenencia de títulos de deuda o participaciones correspondientes a carteras de activos constituidas en el exterior, siempre que estén integradas exclusivamente por títulos valores públicos…»
- Condicion «Condición — carteras integradas exclusivamente títulos nacionales»: Las carteras de activos constituidas en el exterior deben estar integradas exclusivamente por títulos valores públicos nacionales y/o privados del país para permitir la tenencia. ‖ tramo (exacta): «siempre que estén integradas exclusivamente por títulos valores públicos nacionales y/o privados del país»
  - Restriccion:Prohibición — tenencia títulos públicos/privados del exterior --establecida_en--> TextoOrdenado:Política de Crédito
  - Excepcion:Excepción — títulos públicos OCDE con calificación mínima AA --establecida_en--> TextoOrdenado:Política de Crédito
  - Excepcion:Excepción — títulos públicos OCDE con calificación mínima AA --exceptua--> Restriccion:Prohibición — tenencia títulos públicos/privados del exterior
  - Restriccion:Restricción cualitativa — carteras activos constituidas exterior --establecida_en--> TextoOrdenado:Política de Crédito
  - Condicion:Condición — carteras integradas exclusivamente títulos nacionales --establecida_en--> TextoOrdenado:Política de Crédito
  - Condicion:Condición — carteras integradas exclusivamente títulos nacionales --condicion_de--> Restriccion:Restricción cualitativa — carteras activos constituidas exterior
  - heredado_compuesto: 0

## Ficha 21 — `ext::3.5.3::intro`

**Texto propio:**

```
(tres) días hábiles a la fecha de vencimiento del servicio de capital o interés a pagar.
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
```
**Heredado:** Sección 3. Disposiciones específicas para los egresos por el mercado de cambios / 3.5. Pagos de títulos de deuda suscriptos en el exterior y endeudamientos financieros con el / 3.5.3. El acceso al mercado de cambios se produce con una anterioridad no mayor a los 3

**ANTERIOR** — error: None; salida: 2551 tokens

- Condicion «Acceso al mercado de cambios hasta 3 días antes»: El acceso al mercado de cambios debe ocurrir con una anterioridad no mayor a 3 días hábiles respecto a la fecha de vencimiento del servicio de capital o interés a pagar. ‖ tramo (no): «El acceso al mercado de cambios se produce con una anterioridad no mayor a los 3 (tres) días hábiles a la fecha de vencimiento del servicio de capital o interés a pagar» ‖ umbrales: ['no mayor a los 3 (tres) días hábiles']
- Restriccion «Plazo mínimo desde emisión — títulos 08/11/24-20/04/25»: Para pagos de capital de títulos de deuda emitidos entre el 08/11/24 y el 20/04/25 que se concretan con transferencia al exterior, el acceso al mercado de cambios debe ocurrir como mínimo 12 meses después de la fecha de emisión. ‖ tramo (exacta): «En el caso de que se trate de un pago de capital de títulos de deuda emitidos a partir del 08/11/24 que se concreta con una transferencia al exterior, el acceso al mercado de cambios deberá adicionalm…» ‖ umbrales: ['como mínimo, desde la fecha de emisión: i) 12 (doce) meses si el título fue emitido entre el 08/11/24 y el 20/04/25']
- Restriccion «Plazo mínimo desde emisión — títulos 21/04/25-15/05/25»: Para pagos de capital de títulos de deuda emitidos entre el 21/04/25 y el 15/05/25 que se concretan con transferencia al exterior, el acceso al mercado de cambios debe ocurrir como mínimo 6 meses después de la fecha de emisión. ‖ tramo (exacta): «ii) 6 (seis) meses si el título fue emitido entre 21/04/25 y el 15/05/25» ‖ umbrales: ['6 (seis) meses si el título fue emitido entre 21/04/25 y el 15/05/25']
- Restriccion «Plazo mínimo desde emisión — títulos a partir 16/05/25»: Para pagos de capital de títulos de deuda emitidos a partir del 16/05/25 que se concretan con transferencia al exterior, el acceso al mercado de cambios debe ocurrir como mínimo 18 meses después de la fecha de emisión. ‖ tramo (exacta): «iii) 18 (dieciocho) meses si el título fue emitido a partir del 16/05/25» ‖ umbrales: ['18 (dieciocho) meses si el título fue emitido a partir del 16/05/25']
- Potestad «Conformidad previa del BCRA para acceso anticipado»: El BCRA puede otorgar conformidad previa para que se realice el acceso al mercado de cambios antes de los plazos estipulados, excepto en ciertos supuestos donde se cumplen determinadas condiciones. ‖ tramo (exacta): «El acceso al mercado de cambios antes de lo indicado requerirá la conformidad previa del BCRA»
- Excepcion «Conformidad previa no requerida — situaciones y condiciones específicas»: No se requiere conformidad previa del BCRA para el acceso anticipado al mercado de cambios cuando el deudor encuadra en alguna de las situaciones especificadas y se cumplen la totalidad de las condiciones estipuladas en cada caso. ‖ tramo (exacta): «El acceso al mercado de cambios antes de lo indicado requerirá la conformidad previa del BCRA excepto que el deudor encuadre en alguna de las siguientes situaciones y se cumplan la totalidad de las co…»
  - Condicion:Acceso al mercado de cambios hasta 3 días antes --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Restriccion:Plazo mínimo desde emisión — títulos 08/11/24-20/04/25 --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Restriccion:Plazo mínimo desde emisión — títulos 21/04/25-15/05/25 --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Restriccion:Plazo mínimo desde emisión — títulos a partir 16/05/25 --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Potestad:Conformidad previa del BCRA para acceso anticipado --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Excepcion:Conformidad previa no requerida — situaciones y condiciones específica… --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Restriccion:Plazo mínimo desde emisión — títulos 08/11/24-20/04/25 --aplica_a--> el deudor
  - Restriccion:Plazo mínimo desde emisión — títulos 21/04/25-15/05/25 --aplica_a--> el deudor
  - Restriccion:Plazo mínimo desde emisión — títulos a partir 16/05/25 --aplica_a--> el deudor
  - Excepcion:Conformidad previa no requerida — situaciones y condiciones específica… --aplica_a--> el deudor
  - rechazo: firma_invalida: relations[10]: Sujeto --ejecuta--> Potestad
  - omisión relacion_sin_predicado (exacta): «El acceso al mercado de cambios antes de lo indicado requerirá la conformidad previa del BCRA excepto que el deudor encuadre en alguna de las siguientes situaci…» — nota: La relación entre la Potestad (conformidad previa del BCRA) y la Excepcion (situaciones donde no se requiere) podría representarse como una …
  - heredado_compuesto: 0

**P3C** — error: None; salida: 2233 tokens

- Operacion «Acceso al mercado de cambios»: Acceso al mercado de cambios para realizar pagos de servicios de capital o interés, que debe producirse con una anterioridad no mayor a los 3 (tres) días hábiles a la fecha de vencimiento. ‖ tramo (no): «El acceso al mercado de cambios se produce con una anterioridad no mayor a los 3 (tres) días hábiles a la fecha de vencimiento del servicio de capital o interés a pagar.»
- Condicion «Pago de capital de título emitido a partir de 08/11/24 con transferencia exterior»: Se trata de un pago de capital de títulos de deuda emitidos a partir del 08/11/24 que se concreta con una transferencia al exterior ‖ tramo (exacta): «En el caso de que se trate de un pago de capital de títulos de deuda emitidos a partir del 08/11/24 que se concreta con una transferencia al exterior» ‖ umbrales: ['a partir del 08/11/24']
- Restriccion «Plazo mínimo acceso cambios — títulos emitidos 08/11/24 a 20/04/25»: El acceso al mercado de cambios deberá producirse como mínimo 12 (doce) meses desde la fecha de emisión para títulos emitidos entre el 08/11/24 y el 20/04/25 ‖ tramo (no): «el acceso al mercado de cambios deberá adicionalmente producirse una vez transcurridos, como mínimo, desde la fecha de emisión 12 (doce) meses si el título fue emitido entre el 08/11/24 y el 20/04/25.» ‖ umbrales: ['como mínimo, 12 (doce) meses', 'entre el 08/11/24 y el 20/04/25']
- Restriccion «Plazo mínimo acceso cambios — títulos emitidos 21/04/25 a 15/05/25»: El acceso al mercado de cambios deberá producirse como mínimo 6 (seis) meses desde la fecha de emisión para títulos emitidos entre 21/04/25 y el 15/05/25 ‖ tramo (exacta): «6 (seis) meses si el título fue emitido entre 21/04/25 y el 15/05/25.» ‖ umbrales: ['como mínimo, 6 (seis) meses', 'entre 21/04/25 y el 15/05/25']
- Restriccion «Plazo mínimo acceso cambios — títulos emitidos a partir de 16/05/25»: El acceso al mercado de cambios deberá producirse como mínimo 18 (dieciocho) meses desde la fecha de emisión para títulos emitidos a partir del 16/05/25 ‖ tramo (exacta): «18 (dieciocho) meses si el título fue emitido a partir del 16/05/25.» ‖ umbrales: ['como mínimo, 18 (dieciocho) meses', 'a partir del 16/05/25']
- Potestad «Conformidad previa BCRA — acceso anterior a plazos mínimos»: El BCRA puede otorgar su conformidad previa para el acceso al mercado de cambios antes de los plazos mínimos indicados ‖ tramo (exacta): «El acceso al mercado de cambios antes de lo indicado requerirá la conformidad previa del BCRA»
- Excepcion «Excepción — conformidad BCRA — deudor en situaciones especificadas»: La conformidad previa del BCRA no es requerida si el deudor encuadra en alguna de las situaciones que siguen y cumple la totalidad de las condiciones estipuladas en cada caso ‖ tramo (exacta): «excepto que el deudor encuadre en alguna de las siguientes situaciones y se cumplan la totalidad de las condiciones estipuladas en cada caso»
  - Operacion:Acceso al mercado de cambios --establecida_en--> TextoOrdenado:Exterior - Cambios
  - Condicion:Pago de capital de título emitido a partir de 08/11/24 con transferenc… --condicion_de--> Restriccion:Plazo mínimo acceso cambios — títulos emitidos 08/11/24 a 20/04/25
  - Condicion:Pago de capital de título emitido a partir de 08/11/24 con transferenc… --condicion_de--> Restriccion:Plazo mínimo acceso cambios — títulos emitidos 21/04/25 a 15/05/25
  - Condicion:Pago de capital de título emitido a partir de 08/11/24 con transferenc… --condicion_de--> Restriccion:Plazo mínimo acceso cambios — títulos emitidos a partir de 16/05/25
  - Restriccion:Plazo mínimo acceso cambios — títulos emitidos 08/11/24 a 20/04/25 --establecida_en--> TextoOrdenado:Exterior - Cambios
  - Restriccion:Plazo mínimo acceso cambios — títulos emitidos 21/04/25 a 15/05/25 --establecida_en--> TextoOrdenado:Exterior - Cambios
  - Restriccion:Plazo mínimo acceso cambios — títulos emitidos a partir de 16/05/25 --establecida_en--> TextoOrdenado:Exterior - Cambios
  - Potestad:Conformidad previa BCRA — acceso anterior a plazos mínimos --establecida_en--> TextoOrdenado:Exterior - Cambios
  - rechazo: firma_invalida: relations[8]: Excepcion --exceptua_obligacion--> Potestad
  - omisión meta_normativo (exacta): «El acceso al mercado de cambios antes de lo indicado requerirá la conformidad previa del BCRA» — nota: Cláusula que introduce la excepción que sigue; el contenido prescriptivo (la Potestad e7) se extrae, pero el anuncio de alternativa exceptua…
  - heredado_compuesto: 0

## Ficha 22 — `cla::5.1.1::intro`

**Texto propio:**

```
Abarca todas las financiaciones comprendidas, con excepción de las siguientes:
```
**Heredado:** Sección 5. Categorías de carteras. / 5.1. Categorías. / 5.1.1. Cartera comercial.

**ANTERIOR** — error: None; salida: 413 tokens

- Operacion «Financiaciones comprendidas en cartera comercial»: Todas las financiaciones comprendidas en la cartera comercial, con excepción de las siguientes ‖ tramo (exacta): «todas las financiaciones comprendidas»
  - Operacion:Financiaciones comprendidas en cartera comercial --establecida_en--> TextoOrdenado:Texto Ordenado de Clasificación de Deudores
  - omisión meta_normativo (exacta): «Abarca todas las financiaciones comprendidas, con excepción de las siguientes:» — nota: El enunciado es un anuncio de definición de alcance de la categoría de cartera (meta-normativo declarativo); el contenido normativo depende …
  - heredado_compuesto: 0

**P3C** — error: None; salida: 417 tokens

- Definicion «Cartera comercial — alcance»: Abarca todas las financiaciones comprendidas, con excepción de las siguientes ‖ tramo (exacta): «Abarca todas las financiaciones comprendidas»
  - Definicion:Cartera comercial — alcance --establecida_en--> TextoOrdenado:Texto Ordenado Clasificación de Deudores
  - omisión fuera_de_tipos (exacta): «con excepción de las siguientes» — nota: Anuncio de lista de excepciones; el contenido de esas excepciones (las categorías de carteras que quedan excluidas) está en los ítems siguie…
  - heredado_compuesto: 0

## Ficha 23 — `ext::10.4.3.6`

**Texto propio:**

```
10.4.3.6. Cuenta con la declaración jurada del cliente de que se compromete a
demostrar el registro de ingreso aduanero de los bienes dentro de los 90
(noventa) días corridos de la fecha de acceso al mercado de cambios, o en
su defecto, proceder dentro de ese plazo, al reingreso de las divisas desde
el exterior.
```
**Heredado:** Sección 10. Pagos de importaciones y otras compras de bienes en el exterior. / 10.4. Pagos de importaciones de bienes con registro de ingreso aduanero pendiente. / 10.4.3. Requisitos de acceso para el pago de deudas comerciales o a la vista contra la / presentación de la documentación de embarque. La entidad interviniente podrá dar acceso al mercado de cambios para el pago al exterior en la medida que verifique previamente que se cumplen la totalidad de los siguientes requisitos:

**ANTERIOR** — error: None; salida: 1095 tokens

- Operacion «Acceso al mercado de cambios para pago al exterior»: operación de acceso al mercado de cambios para pago al exterior de deudas comerciales o a la vista contra presentación de documentación de embarque ‖ tramo (exacta): «acceso al mercado de cambios para el pago al exterior»
- Condicion «Declaración jurada comprometiéndose a demostrar registro aduanero»: El cliente debe contar con declaración jurada comprometiéndose a demostrar el registro de ingreso aduanero de los bienes dentro de 90 días corridos desde el acceso al mercado de cambios ‖ tramo (exacta): «Cuenta con la declaración jurada del cliente de que se compromete a demostrar el registro de ingreso aduanero de los bienes dentro de los 90 (noventa) días corridos de la fecha de acceso al mercado de…» ‖ umbrales: ['dentro de los 90 (noventa) días corridos']
- Condicion «Reingreso de divisas en plazo de 90 días»: Alternativamente, el cliente debe proceder al reingreso de las divisas desde el exterior dentro del mismo plazo de 90 días ‖ tramo (exacta): «en su defecto, proceder dentro de ese plazo, al reingreso de las divisas desde el exterior» ‖ umbrales: ['dentro de ese plazo']
  - Condicion:Declaración jurada comprometiéndose a demostrar registro aduanero --establecida_en--> TextoOrdenado:Exterior — Cambios
  - Condicion:Reingreso de divisas en plazo de 90 días --establecida_en--> TextoOrdenado:Exterior — Cambios
  - Operacion:Acceso al mercado de cambios para pago al exterior --establecida_en--> TextoOrdenado:Exterior — Cambios
  - Condicion:Declaración jurada comprometiéndose a demostrar registro aduanero --condicion_de--> Operacion:Acceso al mercado de cambios para pago al exterior
  - Condicion:Reingreso de divisas en plazo de 90 días --condicion_de--> Operacion:Acceso al mercado de cambios para pago al exterior
  - Operacion:Acceso al mercado de cambios para pago al exterior --aplica_a--> la entidad interviniente
  - omisión meta_normativo (exacta): «podrá dar acceso» — nota: construcción de habilitación/facultad del sujeto regulado, no una conducta prescrita que deba extraerse; se registra como contenido de la Op…
  - heredado_compuesto: 0

**P3C** — error: None; salida: 1210 tokens

- Operacion «Pago al exterior — importaciones con documentación de embarque»: Acceso al mercado de cambios para el pago al exterior en relación con importaciones de bienes con registro de ingreso aduanero pendiente. ‖ tramo (exacta): «dar acceso al mercado de cambios para el pago al exterior»
- Obligacion «Declaración jurada compromiso — ingreso aduanero 90 días»: La entidad interviniente debe contar con la declaración jurada del cliente en que este se compromete a demostrar el registro de ingreso aduanero de los bienes dentro de los 90 días corridos de la fecha de acceso al mercado de cambios, o en su defecto, proceder al reingreso de las divisas desde el ex… ‖ tramo (exacta): «Cuenta con la declaración jurada del cliente de que se compromete a demostrar el registro de ingreso aduanero de los bienes dentro de los 90 (noventa) días corridos de la fecha de acceso al mercado de…» ‖ umbrales: ['dentro de los 90 (noventa) días corridos']
- Condicion «Verificación previa cumplimiento total requisitos»: El acceso al mercado de cambios está condicionado a que la entidad interviniente verifique previamente el cumplimiento de la totalidad de los requisitos, entre ellos el de contar con la declaración jurada del cliente. ‖ tramo (exacta): «en la medida que verifique previamente que se cumplen la totalidad de los siguientes requisitos»
  - Obligacion:Declaración jurada compromiso — ingreso aduanero 90 días --establecida_en--> TextoOrdenado:Operaciones de cambio en el exterior
  - Operacion:Pago al exterior — importaciones con documentación de embarque --establecida_en--> TextoOrdenado:Operaciones de cambio en el exterior
  - Condicion:Verificación previa cumplimiento total requisitos --establecida_en--> TextoOrdenado:Operaciones de cambio en el exterior
  - Operacion:Pago al exterior — importaciones con documentación de embarque --aplica_a--> La entidad interviniente
  - Obligacion:Declaración jurada compromiso — ingreso aduanero 90 días --aplica_a--> la entidad interviniente
  - Condicion:Verificación previa cumplimiento total requisitos --condicion_de--> Operacion:Pago al exterior — importaciones con documentación de embarque
  - Operacion:Pago al exterior — importaciones con documentación de embarque --requiere--> Obligacion:Declaración jurada compromiso — ingreso aduanero 90 días
  - omisión meta_normativo (exacta): «o en su defecto, proceder dentro de ese plazo, al reingreso de las divisas desde el exterior» — nota: 
  - heredado_compuesto: 0

## Ficha 24 — `cap::10.3.3.1`

**Texto propio:**

```
10.3.3.1. Cuando una entidad financiera invierta en una emisión que cuente con una
calificación específica para esa emisión, el ponderador de riesgo estará ba-
sado en esa calificación. De lo contrario, será de aplicación lo siguiente:
i) En los casos en que el prestatario cuente con una calificación específica
para una de sus emisiones de deuda –pero la exposición crediticia de la
entidad financiera no sea en dicha emisión– la exposición crediticia de la
entidad sólo recibirá una evaluación de crédito de alta calidad –es decir,
la que corresponde a un ponderador de riesgo inferior a la evaluación
aplicable a un crédito no calificado– cuando sea en todos sus aspectos
igual o preferente (“senior”) respecto del crédito evaluado. De lo contrario,
no podrá usarse dicha calificación y la exposición crediticia no calificada
recibirá el ponderador de riesgo correspondiente a los créditos no califi-
cados.
ii) Cuando el prestatario haya sido evaluado como emisor, esa calificación
se podrá aplicar a los créditos quirografarios no subordinados que le ha-
yan sido concedidos y no hayan sido evaluados. Las otras exposiciones
crediticias no calificadas del emisor serán tratadas como no calificadas.
iii) Cuando el emisor o una emisión específica tengan una baja evaluación
crediticia –es decir, asociada a un ponderador de riesgo igual o mayor
que el aplicable a exposiciones no calificadas–, una exposición crediticia
no evaluada frente a dicha contraparte que sea equiparable, o que esté
subordinada, a la evaluación del emisor –correspondiente a sus pasivos
quirografarios no subordinados– o a la evaluación de la exposición, recibi-
rá el mismo ponderador de riesgo que corresponda a esa baja calificación
crediticia.
```
**Heredado:** Sección 10. Agentes de calificación externa (ECAI). / 10.3. Consideraciones para su implementación. / 10.3.3. Evaluaciones de emisores o de emisiones.

**ANTERIOR** — error: None; salida: 3957 tokens

- Operacion «Inversión en emisión con calificación específica»: Inversión en una emisión que cuenta con calificación específica para esa emisión ‖ tramo (exacta): «una entidad financiera invierta en una emisión que cuente con una calificación específica para esa emisión»
- Operacion «Ponderación de riesgo según calificación emisión»: El ponderador de riesgo se determina basándose en la calificación específica de la emisión ‖ tramo (exacta): «el ponderador de riesgo estará basado en esa calificación»
- Operacion «Exposición crediticia en emisión con calificación de emisor»: Exposición crediticia de la entidad financiera que no es en la emisión específica calificada, pero el prestatario tiene calificación en otra de sus emisiones ‖ tramo (exacta): «el prestatario cuente con una calificación específica para una de sus emisiones de deuda –pero la exposición crediticia de la entidad financiera no sea en dicha emisión»
- Restriccion «Restricción calidad crediticia — exposición preferente»: La exposición crediticia recibe evaluación de alta calidad solo si es igual o preferente (senior) en todos los aspectos respecto del crédito evaluado ‖ tramo (exacta): «la exposición crediticia de la entidad sólo recibirá una evaluación de crédito de alta calidad –es decir, la que corresponde a un ponderador de riesgo inferior a la evaluación aplicable a un crédito n…»
- Restriccion «Prohibición uso calificación emisor — exposición no senior»: No se puede utilizar la calificación del emisor para exposiciones crediticias que no sean iguales o preferentes al crédito evaluado; esas exposiciones reciben el ponderador de créditos no calificados ‖ tramo (exacta): «no podrá usarse dicha calificación y la exposición crediticia no calificada recibirá el ponderador de riesgo correspondiente a los créditos no calificados»
- Operacion «Aplicación calificación emisor a créditos quirografarios»: Aplicación de la calificación del emisor a créditos quirografarios no subordinados no evaluados que han sido concedidos al emisor ‖ tramo (exacta): «Cuando el prestatario haya sido evaluado como emisor, esa calificación se podrá aplicar a los créditos quirografarios no subordinados que le hayan sido concedidos y no hayan sido evaluados»
- Potestad «Facultad aplicar calificación emisor a créditos»: La entidad financiera tiene la facultad de aplicar la calificación del emisor a los créditos quirografarios no subordinados no evaluados ‖ tramo (exacta): «esa calificación se podrá aplicar a los créditos quirografarios no subordinados que le hayan sido concedidos y no hayan sido evaluados»
- Restriccion «Restricción exposiciones no calificadas — otras exposiciones»: Las exposiciones crediticias del emisor que no sean créditos quirografarios no subordinados evaluados serán tratadas como no calificadas ‖ tramo (exacta): «Las otras exposiciones crediticias no calificadas del emisor serán tratadas como no calificadas»
- Operacion «Exposición crediticia frente a emisor baja evaluación»: Exposición crediticia no evaluada frente a un emisor o emisión con baja evaluación crediticia, siendo equiparable o subordinada a la evaluación del emisor en sus pasivos quirografarios no subordinados ‖ tramo (exacta): «Cuando el emisor o una emisión específica tengan una baja evaluación crediticia –es decir, asociada a un ponderador de riesgo igual o mayor que el aplicable a exposiciones no calificadas–, una exposic…»
- Restriccion «Ponderador riesgo — exposición frente emisor baja evaluación»: La exposición crediticia no evaluada frente al emisor recibirá el ponderador de riesgo correspondiente a la baja calificación crediticia, cuando sea equiparable o subordinada a la evaluación del emisor ‖ tramo (exacta): «una exposición crediticia no evaluada frente a dicha contraparte que sea equiparable, o que esté subordinada, a la evaluación del emisor –correspondiente a sus pasivos quirografarios no subordinados– …»
- Condicion «Supuesto — Emisión con calificación específica»: Supuesto: la inversión es en una emisión que cuenta con calificación específica para esa emisión ‖ tramo (exacta): «Cuando una entidad financiera invierta en una emisión que cuente con una calificación específica para esa emisión»
- Condicion «Supuesto — Prestatario con calificación pero exposición diferente»: Supuesto: el prestatario tiene calificación específica en una emisión pero la exposición crediticia de la entidad no es en esa emisión calificada ‖ tramo (exacta): «En los casos en que el prestatario cuente con una calificación específica para una de sus emisiones de deuda –pero la exposición crediticia de la entidad financiera no sea en dicha emisión»
- Condicion «Supuesto — Prestatario evaluado como emisor»: Supuesto: el prestatario ha sido evaluado en su calidad de emisor ‖ tramo (exacta): «Cuando el prestatario haya sido evaluado como emisor»
- Condicion «Supuesto — Emisor con baja evaluación crediticia»: Supuesto: el emisor o la emisión específica tiene una baja evaluación crediticia con ponderador igual o mayor al de exposiciones no calificadas ‖ tramo (exacta): «Cuando el emisor o una emisión específica tengan una baja evaluación crediticia –es decir, asociada a un ponderador de riesgo igual o mayor que el aplicable a exposiciones no calificadas»
  - Operacion:Ponderación de riesgo según calificación emisión --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Restriccion:Restricción calidad crediticia — exposición preferente --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Restriccion:Prohibición uso calificación emisor — exposición no senior --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Potestad:Facultad aplicar calificación emisor a créditos --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Restriccion:Restricción exposiciones no calificadas — otras exposiciones --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Restriccion:Ponderador riesgo — exposición frente emisor baja evaluación --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Operacion:Ponderación de riesgo según calificación emisión --aplica_a--> una entidad financiera
  - Restriccion:Restricción calidad crediticia — exposición preferente --aplica_a--> la entidad financiera
  - Restriccion:Prohibición uso calificación emisor — exposición no senior --aplica_a--> la entidad financiera
  - Potestad:Facultad aplicar calificación emisor a créditos --aplica_a--> la entidad financiera
  - Restriccion:Restricción exposiciones no calificadas — otras exposiciones --aplica_a--> la entidad financiera
  - Restriccion:Ponderador riesgo — exposición frente emisor baja evaluación --aplica_a--> la entidad financiera
  - Condicion:Supuesto — Emisión con calificación específica --condicion_de--> Operacion:Ponderación de riesgo según calificación emisión
  - Condicion:Supuesto — Prestatario con calificación pero exposición diferente --condicion_de--> Restriccion:Restricción calidad crediticia — exposición preferente
  - Condicion:Supuesto — Prestatario evaluado como emisor --condicion_de--> Potestad:Facultad aplicar calificación emisor a créditos
  - Condicion:Supuesto — Emisor con baja evaluación crediticia --condicion_de--> Restriccion:Ponderador riesgo — exposición frente emisor baja evaluación
  - Restriccion:Restricción calidad crediticia — exposición preferente --limita--> Operacion:Exposición crediticia en emisión con calificación de emisor
  - Restriccion:Prohibición uso calificación emisor — exposición no senior --prohibe--> Operacion:Exposición crediticia en emisión con calificación de emisor
  - Restriccion:Restricción exposiciones no calificadas — otras exposiciones --limita--> Operacion:Exposición crediticia en emisión con calificación de emisor
  - Restriccion:Ponderador riesgo — exposición frente emisor baja evaluación --limita--> Operacion:Exposición crediticia frente a emisor baja evaluación
  - omisión relacion_sin_predicado (no): «la exposición crediticia de la entidad recibirá una evaluación de crédito de alta calidad cuando sea en todos sus aspectos igual o preferente respecto del crédi…» — nota: Relación entre Restriccion e4 (límite cualitativo) y la determinación de que la evaluación sea de 'alta calidad': podría ser 'regula' si fue…
  - heredado_compuesto: 0

**P3C** — error: None; salida: 3127 tokens

- Operacion «Inversión en emisión con calificación específica»: Una entidad financiera invierte en una emisión que cuenta con una calificación específica para esa emisión. ‖ tramo (exacta): «una entidad financiera invierta en una emisión que cuente con una calificación específica para esa emisión»
- Restriccion «Ponderador basado en calificación específica de emisión»: Cuando una entidad financiera invierte en una emisión con calificación específica, el ponderador de riesgo debe estar basado en esa calificación de la emisión. ‖ tramo (exacta): «el ponderador de riesgo estará basado en esa calificación»
- Condicion «Exposición crediticia de igual o preferente rango que lo evaluado»: La exposición crediticia solo recibe evaluación de crédito de alta calidad cuando es en todos sus aspectos igual o preferente (senior) respecto del crédito evaluado. ‖ tramo (exacta): «cuando sea en todos sus aspectos igual o preferente ("senior") respecto del crédito evaluado»
- Restriccion «Prohibición de usar calificación sin equivalencia de rango»: No podrá usarse la calificación de una emisión evaluada cuando la exposición crediticia no sea de igual o preferente rango que el crédito evaluado. La exposición crediticia no calificada recibirá el ponderador de riesgo correspondiente a los créditos no calificados. ‖ tramo (exacta): «De lo contrario, no podrá usarse dicha calificación y la exposición crediticia no calificada recibirá el ponderador de riesgo correspondiente a los créditos no calificados»
- Operacion «Aplicación de calificación de emisor a créditos quirografarios»: Cuando el prestatario ha sido evaluado como emisor, la calificación se puede aplicar a los créditos quirografarios no subordinados que le han sido concedidos y no han sido evaluados. ‖ tramo (exacta): «Cuando el prestatario haya sido evaluado como emisor, esa calificación se podrá aplicar a los créditos quirografarios no subordinados que le hayan sido concedidos y no hayan sido evaluados»
- Potestad «Opción de aplicar calificación del emisor a créditos quirografarios»: Cuando el prestatario ha sido evaluado como emisor, la entidad financiera está facultada para aplicar esa calificación a los créditos quirografarios no subordinados que le han sido concedidos y no han sido evaluados. ‖ tramo (exacta): «esa calificación se podrá aplicar a los créditos quirografarios no subordinados que le hayan sido concedidos y no hayan sido evaluados»
- Restriccion «Otras exposiciones crediticias tratadas como no calificadas»: Cuando el prestatario ha sido evaluado como emisor, las otras exposiciones crediticias no calificadas del emisor serán tratadas como no calificadas. ‖ tramo (exacta): «Las otras exposiciones crediticias no calificadas del emisor serán tratadas como no calificadas»
- Operacion «Aplicación de ponderador de baja calificación a exposición subordinada o equiparable»: Una exposición crediticia no evaluada frente a una contraparte con baja evaluación crediticia que sea equiparable o subordinada a la evaluación del emisor o de la emisión. ‖ tramo (exacta): «una exposición crediticia no evaluada frente a dicha contraparte que sea equiparable, o que esté subordinada, a la evaluación del emisor»
- Restriccion «Ponderador de riesgo igual a baja calificación crediticia»: Cuando el emisor o una emisión tengan baja evaluación crediticia (igual o mayor que el aplicable a exposiciones no calificadas), una exposición crediticia no evaluada que sea equiparable o subordinada recibirá el mismo ponderador de riesgo que corresponda a esa baja calificación crediticia. ‖ tramo (exacta): «recibirá el mismo ponderador de riesgo que corresponda a esa baja calificación crediticia»
- Condicion «Baja evaluación crediticia del emisor o emisión»: El emisor o una emisión específica tienen una baja evaluación crediticia, es decir, asociada a un ponderador de riesgo igual o mayor que el aplicable a exposiciones no calificadas. ‖ tramo (exacta): «Cuando el emisor o una emisión específica tengan una baja evaluación crediticia –es decir, asociada a un ponderador de riesgo igual o mayor que el aplicable a exposiciones no calificadas»
  - Restriccion:Ponderador basado en calificación específica de emisión --establecida_en--> TextoOrdenado:Texto Ordenado de Capitales Mínimos
  - Restriccion:Prohibición de usar calificación sin equivalencia de rango --establecida_en--> TextoOrdenado:Texto Ordenado de Capitales Mínimos
  - Restriccion:Otras exposiciones crediticias tratadas como no calificadas --establecida_en--> TextoOrdenado:Texto Ordenado de Capitales Mínimos
  - Restriccion:Ponderador de riesgo igual a baja calificación crediticia --establecida_en--> TextoOrdenado:Texto Ordenado de Capitales Mínimos
  - Potestad:Opción de aplicar calificación del emisor a créditos quirografarios --establecida_en--> TextoOrdenado:Texto Ordenado de Capitales Mínimos
  - Condicion:Exposición crediticia de igual o preferente rango que lo evaluado --establecida_en--> TextoOrdenado:Texto Ordenado de Capitales Mínimos
  - Condicion:Baja evaluación crediticia del emisor o emisión --establecida_en--> TextoOrdenado:Texto Ordenado de Capitales Mínimos
  - Restriccion:Ponderador basado en calificación específica de emisión --limita--> Operacion:Inversión en emisión con calificación específica
  - Restriccion:Prohibición de usar calificación sin equivalencia de rango --prohibe--> Operacion:Aplicación de calificación de emisor a créditos quirografarios
  - Restriccion:Otras exposiciones crediticias tratadas como no calificadas --limita--> Operacion:Aplicación de calificación de emisor a créditos quirografarios
  - Restriccion:Ponderador de riesgo igual a baja calificación crediticia --limita--> Operacion:Aplicación de ponderador de baja calificación a exposición subordinada…
  - Condicion:Exposición crediticia de igual o preferente rango que lo evaluado --condicion_de--> Restriccion:Ponderador basado en calificación específica de emisión
  - Condicion:Baja evaluación crediticia del emisor o emisión --condicion_de--> Restriccion:Ponderador de riesgo igual a baja calificación crediticia
  - Restriccion:Ponderador basado en calificación específica de emisión --aplica_a--> una entidad financiera
  - Restriccion:Prohibición de usar calificación sin equivalencia de rango --aplica_a--> la entidad
  - Restriccion:Otras exposiciones crediticias tratadas como no calificadas --aplica_a--> el emisor
  - Restriccion:Ponderador de riesgo igual a baja calificación crediticia --aplica_a--> una entidad
  - Potestad:Opción de aplicar calificación del emisor a créditos quirografarios --aplica_a--> la entidad financiera
  - omisión relacion_sin_predicado (exacta): «De lo contrario, será de aplicación lo siguiente:» — nota: Conexión entre condición negativa y enumeración de casos alternativos; no hay predicado que exprese 'aplicación alternativa de reglas según …
  - heredado_compuesto: 0

## Ficha 25 — `cap::6.2.2.6`

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
**Heredado:** Sección 6. Capital mínimo por riesgo de mercado. / 6.2. Exigencia de capital por riesgo de tasa de interés. / La exigencia de capital por el riesgo de tasa de interés se deberá calcular respecto de los títu- los de deuda y otros instrumentos imputados a la cartera de negociación, incluidas las accio- nes preferidas no convertibles. Un título valor vendido y recomprado… / 6.2.2. Exigencia de capital por riesgo general de mercado: método de los plazos residuales.

**ANTERIOR** — error: None; salida: 1590 tokens

- Operacion «Compensaciones horizontales de posiciones»: Realización de dos series de compensaciones horizontales de posiciones netas: primera serie dentro de cada una de las tres zonas de agrupación de bandas temporales; segunda serie entre las posiciones netas de las tres zonas ‖ tramo (exacta): «las entidades podrán realizar dos series de compensaciones horizontales: primero, entre las posiciones netas dentro de cada una de las tres zonas en las que se agrupan las bandas temporales y, luego, …»
- Restriccion «Desestimaciones horizontales — compensaciones»: Las compensaciones horizontales de posiciones netas se sujetan a una escala de desestimaciones horizontales expresadas como porcentajes de las posiciones compensadas. La escala varía según zona y banda temporal: Zona 1 (0-1, 1-3, 3-6, 6-12 meses) aplicación dentro de zona 40%, entre zonas adyacentes… ‖ tramo (exacta): «Dichas compensaciones estarán sujetas a la siguiente escala de desestimaciones horizontales -exigencias adicionales- expresadas como porcentajes de las posiciones que se compensan» ‖ umbrales: ['40%', '40%', '30%', '40%', '100%', '30%', '40%']
- Condicion «Imputación a banda cuando plazo es límite entre bandas»: Cuando el plazo residual o el plazo hasta el siguiente ajuste de interés es igual al límite entre dos bandas temporales, la posición debe imputarse a la banda temporal más próxima a la fecha de cálculo ‖ tramo (exacta): «Al efecto de imputar una posición a la escala de vencimientos cuando el plazo residual o el plazo que resta hasta el siguiente ajuste del interés, según el caso, es igual al límite entre dos bandas, c…»
  - Operacion:Compensaciones horizontales de posiciones --establecida_en--> TextoOrdenado:Capital Mínimo
  - Restriccion:Desestimaciones horizontales — compensaciones --establecida_en--> TextoOrdenado:Capital Mínimo
  - Condicion:Imputación a banda cuando plazo es límite entre bandas --establecida_en--> TextoOrdenado:Capital Mínimo
  - Restriccion:Desestimaciones horizontales — compensaciones --limita--> Operacion:Compensaciones horizontales de posiciones
  - Operacion:Compensaciones horizontales de posiciones --aplica_a--> las entidades
  - Restriccion:Desestimaciones horizontales — compensaciones --aplica_a--> las entidades
  - omisión tabla (no): «[TABLA cap::tabla037 | página 125 | e0_tablas | posicional] Fila 8: col1 = Años* ⟨abarca hasta col3⟩ | col4 = 40%; Fila 12: col1 = Años* ⟨abarca hasta col3⟩ | c…» — nota: Celdas combinadas sin fila asignada (20 celdas no asignadas por E0) y filas incompletas. Los valores para las filas 8, 12 y la última banda …
  - heredado_compuesto: 0

**P3C** — error: None; salida: 2318 tokens

- Operacion «Compensaciones horizontales de posiciones netas»: Realización de dos series de compensaciones horizontales de posiciones netas: dentro de cada una de las tres zonas de bandas temporales y entre las tres zonas. ‖ tramo (exacta): «las entidades podrán realizar dos series de compensaciones horizontales: primero, entre las posiciones netas dentro de cada una de las tres zonas en las que se agrupan las bandas temporales y, luego, …»
- Restriccion «Desestimaciones horizontales en compensaciones de posiciones»: Las compensaciones horizontales están sujetas a una escala de desestimaciones (exigencias adicionales) expresadas como porcentajes de las posiciones compensadas. Los porcentajes varían según la zona (dentro de zona, entre zonas adyacentes, entre zonas 1 y 3) y la banda temporal. ‖ tramo (exacta): «Dichas compensaciones estarán sujetas a la siguiente escala de desestimaciones horizontales -exigencias adicionales- expresadas como porcentajes de las posiciones que se compensan»
- Condicion «Imputación a banda temporal por proximidad»: Cuando el plazo residual o el plazo que resta hasta el siguiente ajuste del interés es igual al límite entre dos bandas, la imputación debe realizarse a la banda temporal más próxima a la fecha de cálculo. ‖ tramo (exacta): «Al efecto de imputar una posición a la escala de vencimientos cuando el plazo residual o el plazo que resta hasta el siguiente ajuste del interés, según el caso, es igual al límite entre dos bandas, c…»
- Definicion «Desestimaciones verticales y horizontales»: Las desestimaciones verticales resultan del cálculo previsto en el punto 6.2.2.5, junto con conjuntos de posiciones netas compradas y vendidas. ‖ tramo (exacta): «Como resultado de lo previsto en el punto 6.2.2.5. se obtendrá un conjunto de posiciones netas compradas, un conjunto de posiciones netas vendidas y las desestimaciones verticales»
  - Operacion:Compensaciones horizontales de posiciones netas --establecida_en--> TextoOrdenado:Texto Ordenado de Capitales Mínimos
  - Restriccion:Desestimaciones horizontales en compensaciones de posiciones --establecida_en--> TextoOrdenado:Texto Ordenado de Capitales Mínimos
  - Condicion:Imputación a banda temporal por proximidad --establecida_en--> TextoOrdenado:Texto Ordenado de Capitales Mínimos
  - Definicion:Desestimaciones verticales y horizontales --establecida_en--> TextoOrdenado:Texto Ordenado de Capitales Mínimos
  - Restriccion:Desestimaciones horizontales en compensaciones de posiciones --limita--> Operacion:Compensaciones horizontales de posiciones netas
  - Condicion:Imputación a banda temporal por proximidad --condicion_de--> Operacion:Compensaciones horizontales de posiciones netas
  - Operacion:Compensaciones horizontales de posiciones netas --aplica_a--> las entidades
  - omisión tabla (exacta): «[TABLA cap::tabla037 | página 125 | e0_tablas | posicional] Fila 1: col1 = Zona | col2 = Banda | col3 = Porcentaje de desestimación aplicable: ⟨abarca hasta col…» — nota: Tabla serializada declarada NO-CONFIABLE: contiene porcentajes de desestimación horizontal por zona y banda temporal que no se pueden copiar…
  - heredado_compuesto: 0

## Ficha 26 — `ext::3.5.3.5`

**Texto propio:**

```
3.5.3.5. Precancelación de capital e intereses por parte de un VPU adherido al RIGI.
El cliente es un Vehículo de Proyecto Único (VPU) adherido al Régimen de
Incentivo para Grandes Inversiones (RIGI) que precancela capital o intereses
devengados por endeudamientos financieros comprendidos en este punto
3.5. en el marco de lo previsto en el punto 14.2.1.
```
**Heredado:** Sección 3. Disposiciones específicas para los egresos por el mercado de cambios / Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–, adicionalmente a los requisitos y condiciones específicas detalladas… / 3.5. Pagos de títulos de deuda suscriptos en el exterior y endeudamientos financieros con el / exterior. Las entidades podrán dar acceso al mercado de cambios para realizar pagos de capital o intereses de títulos de deuda con registro público en el exterior, otros endeudamientos financieros con el exterior y títulos de deuda con registro público en el p… / 3.5.3. El acceso al mercado de cambios se produce con una anterioridad no mayor a los 3 / (tres) días hábiles a la fecha de vencimiento del servicio de capital o interés a pagar. En el caso de que se trate de un pago de capital de títulos de deuda emitidos a partir del 08/11/24 que se concreta con una transferencia al exterior, el acceso al mercado… / i) 12 (doce) meses si el título fue emitido entre el 08/11/24 y el 20/04/25. ii) 6 (seis) meses si el título fue emitido entre 21/04/25 y el 15/05/25. iii) 18 (dieciocho) meses si el título fue emitido a partir del 16/05/25. / El acceso al mercado de cambios antes de lo indicado requerirá la conformidad previa del BCRA excepto que el deudor encuadre en alguna de las siguientes situaciones y se cumplan la totalidad de las condiciones estipuladas en cada caso:

**ANTERIOR** — error: None; salida: 963 tokens

- Condicion «VPU adherido al RIGI precancela capital»: El deudor es un VPU adherido al RIGI que precancela capital o intereses devengados por endeudamientos financieros comprendidos en el punto 3.5 ‖ tramo (exacta): «El cliente es un Vehículo de Proyecto Único (VPU) adherido al Régimen de Incentivo para Grandes Inversiones (RIGI) que precancela capital o intereses devengados por endeudamientos financieros comprend…»
- Excepcion «Excepción — precancelación VPU RIGI»: Se exceptúa del requisito de conformidad previa del BCRA para acceso al mercado de cambios en caso de precancelación de capital o intereses por parte de un VPU adherido al RIGI, en los términos del punto 14.2.1 ‖ tramo (exacta): «El cliente es un Vehículo de Proyecto Único (VPU) adherido al Régimen de Incentivo para Grandes Inversiones (RIGI) que precancela capital o intereses devengados por endeudamientos financieros comprend…»
  - Condicion:VPU adherido al RIGI precancela capital --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Excepcion:Excepción — precancelación VPU RIGI --establecida_en--> TextoOrdenado:Texto Ordenado Exterior Cambios
  - Excepcion:Excepción — precancelación VPU RIGI --aplica_a--> las entidades
  - omisión meta_normativo (exacta): «en el marco de lo previsto en el punto 14.2.1» — nota: Remisión a otro punto que fija alcance y condiciones; no es contenido normativo propio de esta unidad
  - omisión relacion_sin_predicado (exacta): «endeudamientos financieros comprendidos en este punto 3.5» — nota: Relación entre la Condicion (o la Excepcion) y una Operacion implícita (los endeudamientos financieros) sin predicado claro en el esquema; s…
  - heredado_compuesto: 0

**P3C** — error: None; salida: 864 tokens

- Condicion «Cliente es VPU adherido al RIGI»: El cliente que realiza la operación debe ser un Vehículo de Proyecto Único (VPU) adherido al Régimen de Incentivo para Grandes Inversiones (RIGI) ‖ tramo (exacta): «El cliente es un Vehículo de Proyecto Único (VPU) adherido al Régimen de Incentivo para Grandes Inversiones (RIGI)»
- Operacion «Precancelación de capital o intereses — endeudamientos financieros»: Operación de precancelación de capital o intereses devengados por endeudamientos financieros, realizada dentro del marco establecido en el punto 14.2.1 ‖ tramo (exacta): «precancela capital o intereses devengados por endeudamientos financieros comprendidos en este punto 3.5. en el marco de lo previsto en el punto 14.2.1»
  - Condicion:Cliente es VPU adherido al RIGI --establecida_en--> TextoOrdenado:Texto Ordenado Exterior y Cambios
  - Operacion:Precancelación de capital o intereses — endeudamientos financieros --establecida_en--> TextoOrdenado:Texto Ordenado Exterior y Cambios
  - Condicion:Cliente es VPU adherido al RIGI --condicion_de--> Operacion:Precancelación de capital o intereses — endeudamientos financieros
  - Operacion:Precancelación de capital o intereses — endeudamientos financieros --aplica_a--> un VPU adherido al RIGI
  - omisión relacion_sin_predicado (exacta): «precancela capital o intereses devengados por endeudamientos financieros comprendidos en este punto 3.5» — nota: Relación implícita entre la Operacion (precancelación) y el punto 3.5 que define el marco normativo de los endeudamientos financieros; esta …
  - heredado_compuesto: 0

## Ficha 27 — `cap::6.3.2::intro`

**Texto propio:**

```
A excepción de las opciones sobre acciones e índices bursátiles, que se tratan en el
punto 6.6., los restantes derivados sobre acciones y las posiciones fuera de balance
sensibles a los cambios en los precios de mercado deberán incluirse en el cómputo de
la exigencia. Esto comprende a los futuros, “forwards” y “swaps”, tanto de acciones in-
dividuales como de índices bursátiles. Los derivados se convertirán en posiciones en su
correspondiente subyacente.
```
**Heredado:** Sección 6. Capital mínimo por riesgo de mercado. / 6.3. Exigencia de capital por riesgo de posiciones en acciones. / 6.3.2. Tratamiento de los derivados sobre acciones.

**ANTERIOR** — error: None; salida: 1250 tokens

- Excepcion «Excepción opciones sobre acciones e índices — derivados»: Las opciones sobre acciones e índices bursátiles quedan exceptuadas del cómputo de la exigencia de capital por riesgo de derivados; su tratamiento se establece en el punto 6.6. ‖ tramo (exacta): «A excepción de las opciones sobre acciones e índices bursátiles, que se tratan en el punto 6.6.»
- Operacion «Conversión de derivados a posiciones de subyacente»: Los derivados sobre acciones (futuros, forwards, swaps de acciones individuales e índices bursátiles) se convierten a posiciones en su subyacente para propósitos del cómputo de exigencia de capital. ‖ tramo (exacta): «Los derivados se convertirán en posiciones en su correspondiente subyacente.»
- Obligacion «Incluir derivados en cómputo de exigencia de capital»: Las entidades deberán incluir en el cómputo de la exigencia de capital por riesgo de posiciones en acciones los derivados sobre acciones (excepto opciones) y las posiciones fuera de balance sensibles a cambios en precios de mercado, incluyendo futuros, forwards y swaps de acciones individuales e índ… ‖ tramo (exacta): «los restantes derivados sobre acciones y las posiciones fuera de balance sensibles a los cambios en los precios de mercado deberán incluirse en el cómputo de la exigencia. Esto comprende a los futuros…»
  - Excepcion:Excepción opciones sobre acciones e índices — derivados --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Obligacion:Incluir derivados en cómputo de exigencia de capital --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Operacion:Conversión de derivados a posiciones de subyacente --establecida_en--> TextoOrdenado:Capitales Mínimos
  - Obligacion:Incluir derivados en cómputo de exigencia de capital --aplica_a--> las entidades
  - Excepcion:Excepción opciones sobre acciones e índices — derivados --exceptua_obligacion--> Obligacion:Incluir derivados en cómputo de exigencia de capital
  - Obligacion:Incluir derivados en cómputo de exigencia de capital --regula--> Operacion:Conversión de derivados a posiciones de subyacente
  - omisión relacion_sin_predicado (exacta): «Los derivados se convertirán en posiciones en su correspondiente subyacente.» — nota: Relación entre Obligacion (e3) y Operacion (e2): el deber de incluir derivados en el cómputo se implementa mediante su conversión a posicion…
  - heredado_compuesto: 0

**P3C** — error: None; salida: 968 tokens

- Operacion «Inclusión de derivados en cómputo de exigencia»: Los derivados sobre acciones (futuros, forwards y swaps de acciones individuales e índices bursátiles) y las posiciones fuera de balance sensibles a cambios de precios de mercado deben incluirse en el cómputo de la exigencia de capital, a excepción de las opciones sobre acciones e índices bursátiles… ‖ tramo (exacta): «los restantes derivados sobre acciones y las posiciones fuera de balance sensibles a los cambios en los precios de mercado deberán incluirse en el cómputo de la exigencia»
- Operacion «Conversión de derivados en posiciones»: Los derivados deben convertirse en posiciones en su correspondiente subyacente para propósitos del cómputo de la exigencia. ‖ tramo (exacta): «Los derivados se convertirán en posiciones en su correspondiente subyacente»
- Excepcion «Opciones sobre acciones e índices — tratamiento en 6.6»: Las opciones sobre acciones e índices bursátiles se exceptúan del tratamiento general de inclusión en la exigencia, siendo tratadas de conformidad con lo dispuesto en el punto 6.6. ‖ tramo (exacta): «A excepción de las opciones sobre acciones e índices bursátiles, que se tratan en el punto 6.6.»
  - Operacion:Inclusión de derivados en cómputo de exigencia --establecida_en--> TextoOrdenado:Texto Ordenado de Capitales Mínimos
  - Operacion:Conversión de derivados en posiciones --establecida_en--> TextoOrdenado:Texto Ordenado de Capitales Mínimos
  - Excepcion:Opciones sobre acciones e índices — tratamiento en 6.6 --establecida_en--> TextoOrdenado:Texto Ordenado de Capitales Mínimos
  - rechazo: firma_invalida: relations[3]: Excepcion --exceptua--> Operacion
  - omisión meta_normativo (exacta): «Esto comprende a los futuros, "forwards" y "swaps", tanto de acciones individuales como de índices bursátiles.» — nota: Oración que enumera ejemplos incluidos en la operación e1; clarifica su alcance sin prescribir conducta separada.
  - heredado_compuesto: 0

