# `ext::5.8.2.2` — Las transferencias tengan como ordenante la empresa del exterior firmante

Grupos: omisiones. Estado final en la tanda 0: `aceptado_con_residuales`.

## Texto

> *heredado:* Sección 5. Pautas operativas.
> *heredado:* 5.8. Boletos globales diarios.
> *heredado:* Las entidades podrán elaborar un boleto global diario para las situaciones que se detallan a continuación, en la medida que se verifiquen todas las condiciones indicadas en cada caso. En todos los casos, se deberá requerir una lista detallada de los beneficiarios/ordenantes de los pagos comprendidos en dicho boleto, debiendo como mínimo informar respecto de ellos: nombres y apellidos completos o denominación social (según corresponda), CUIT, CUIL o CDI y el monto que le corresponde.
> *heredado:* 5.8.2. Ingresos de divisas a través de empresas procesadores de pagos.
> *heredado:* A nombre de la empresa local que actúa como representante en el país de la empresa procesadora de pagos en la medida que se cumplan las siguientes condiciones:
> *heredado:* Por los ingresos cursados que correspondan al cobro de exportaciones de bienes y servicios, la entidad receptora de la transferencia emitirá, a pedido del exportador, una certificación de ingreso y liquidación de divisas por los fondos recibidos en moneda local.
> *propio:* 5.8.2.2. Las transferencias tengan como ordenante la empresa del exterior firmante del acuerdo y se canalicen a través de una entidad financiera del exterior cuya casa matriz o controlante se encuentre radicada en un país miembro del Comité de Supervisión Bancaria de Basilea.

## Omisiones leídas en T4 (M2)

con_marca:6 [normativa; propio] «5.8.2.2. Las transferencias tengan como ordenante la empresa del exterior firmante del acuerdo y se canalicen a través de una entidad financiera del exterior cuya casa matriz o controlante se encuentre radicada en un país miembro del Comité de Supervisión Bancaria de Basilea»

## Código A

- **c1 Condicion** «Ordenante empresa del exterior vía entidad de país Basilea» — Supuesto para el boleto global diario de ingresos de divisas a través de empresas procesadoras de pagos (punto 5.8.2): las transferencias tienen como ordenante la empresa del exterior firmante del acuerdo y se canalizan a través de una entidad financiera del exterior cuya casa matriz o controlante está radicada en un país miembro del Comité de Supervisión Bancaria de Basilea. · tramo [exacta]: «Las transferencias tengan como ordenante la empresa del exterior firmante del acuerdo y se canalicen a través de una entidad financiera del exterior cuya casa matriz o controlante se encuentre radicada en un país miembro del Comité de Supervisión Bancaria de Basilea.»

### A — omisiones de T4 a clasificar

- con_marca:6 → entidades: c1 Condicion [exacta] solap 0.88 contenido_en | omisiones: —

## Código H

- **c1 Condicion** «Ordenante empresa exterior y entidad financiera del exterior de país Basilea» — Condición del boleto global diario por ingresos de divisas a través de empresas procesadoras de pagos (norma del intro del punto 5.8.2): las transferencias deben tener como ordenante la empresa del exterior firmante del acuerdo y canalizarse a través de una entidad financiera del exterior cuya casa matriz o controlante esté radicada en un país miembro del Comité de Supervisión Bancaria de Basilea.… · tramo [exacta]: «Las transferencias tengan como ordenante la empresa del exterior firmante del acuerdo y se canalicen a través de una entidad financiera del exterior cuya casa matriz o controlante se encuentre radicada en un país miembro del Comité de Supervisión Bancaria de Basilea.»

### H — omisiones de T4 a clasificar

- con_marca:6 → entidades: c1 Condicion [exacta] solap 0.88 contenido_en | omisiones: —

## Código K

- **c1 Condicion** «Ordenante empresa del exterior firmante — boleto global procesadoras» — Una de las condiciones que deben cumplirse todas juntas para que el ingreso de divisas a través de una empresa procesadora de pagos pueda registrarse en un boleto global diario a nombre de su representante local: las transferencias deben tener como ordenante a la empresa del exterior que firmó el acuerdo. · tramo [exacta]: «Las transferencias tengan como ordenante la empresa del exterior firmante del acuerdo»
- **c2 Condicion** «Canalización vía entidad del exterior con matriz Basilea» — Una de las condiciones que deben cumplirse todas juntas para emitir el boleto global diario por ingresos a través de procesadoras de pagos: las transferencias deben canalizarse a través de una entidad financiera del exterior cuya casa matriz o controlante esté radicada en un país miembro del Comité de Supervisión Bancaria de Basilea. · tramo [exacta]: «se canalicen a través de una entidad financiera del exterior cuya casa matriz o controlante se encuentre radicada en un país miembro del Comité de Supervisión Bancaria de Basilea»

### K — omisiones de T4 a clasificar

- con_marca:6 → entidades: c2 Condicion [exacta] solap 0.65 contenido_en; c1 Condicion [exacta] solap 0.27 contenido_en | omisiones: —

## Código W

- **c1 Condicion** «Ordenante empresa exterior firmante — boleto global procesadoras» — Condición (exigida junto con las demás) para elaborar el boleto global diario a nombre de la empresa local representante de la procesadora de pagos por ingresos de divisas: que las transferencias tengan como ordenante a la empresa del exterior firmante del acuerdo. · tramo [exacta]: «Las transferencias tengan como ordenante la empresa del exterior firmante del acuerdo»
- **c2 Condicion** «Canal entidad exterior con matriz Basilea — boleto global» — Condición (exigida junto con las demás) para elaborar el boleto global diario por ingresos de divisas a través de procesadoras de pagos: que las transferencias se canalicen por una entidad financiera del exterior cuya casa matriz o controlante esté radicada en un país miembro del Comité de Supervisión Bancaria de Basilea. · tramo [exacta]: «se canalicen a través de una entidad financiera del exterior cuya casa matriz o controlante se encuentre radicada en un país miembro del Comité de Supervisión Bancaria de Basilea»

### W — omisiones de T4 a clasificar

- con_marca:6 → entidades: c2 Condicion [exacta] solap 0.65 contenido_en; c1 Condicion [exacta] solap 0.27 contenido_en | omisiones: —

