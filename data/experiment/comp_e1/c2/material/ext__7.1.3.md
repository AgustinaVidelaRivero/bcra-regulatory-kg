# `ext::7.1.3` — Anticipos, prefinanciaciones y posfinanciaciones del exterior.

Grupos: omisiones. Estado final en la tanda 0: `completo_ok_directo`.

## Texto

> *heredado:* Sección 7. Cobros de exportaciones de bienes.
> *heredado:* 7.1. Obligación de ingreso y liquidación en los plazos establecidos.
> *propio:* 7.1.3. Anticipos, prefinanciaciones y posfinanciaciones del exterior. Los anticipos, prefinanciaciones y posfinanciaciones del exterior deberán ser ingresadas y liquidadas en el mercado de cambios dentro de los 20 (veinte) días hábiles de la fecha de cobro o desembolso en el exterior. En el caso que el cliente sea un Vehículo de Proyecto Único (VPU) adherido al Régimen de Incentivo para Grandes Inversiones (RIGI) que declaró ante la Autoridad de Aplicación que preveía hacer uso de los beneficios establecidos en el artículo 198 de la Ley 27.742 en materia de cobro de exportaciones de bienes y servicios, resultará aplicable lo dispuesto en el punto 14.1.4.

## Omisiones leídas en T4 (M2)

sin_marca:9 [normativa, remisión pura; propio] «resultará aplicable lo dispuesto en el punto 14.1.4»

## Código A

- **op1 Operacion** «Ingreso y liquidación de anticipos, prefinanciaciones y posfinanciaciones del exterior» — Ingreso y liquidación en el mercado de cambios de anticipos, prefinanciaciones y posfinanciaciones del exterior, contada desde la fecha de cobro o desembolso en el exterior. · props: `{"tipo": "ingreso y liquidación de divisas"}` · tramo [exacta]: «Los anticipos, prefinanciaciones y posfinanciaciones del exterior deberán ser ingresadas y liquidadas en el mercado de cambios»
- **ob1 Obligacion** «Ingreso y liquidación en 20 días hábiles» — Los anticipos, prefinanciaciones y posfinanciaciones del exterior deben ser ingresados y liquidados en el mercado de cambios dentro de los 20 días hábiles de la fecha de cobro o desembolso en el exterior. · props: `{"tipo": "otra"}` · umbral: ['dentro de los 20 (veinte) días hábiles de la fecha de cobro o desembolso en el e…'] · tramo [exacta]: «deberán ser ingresadas y liquidadas en el mercado de cambios dentro de los 20 (veinte) días hábiles de la fecha de cobro o desembolso en el exterior»
- **cond1 Condicion** «Cliente VPU adherido al RIGI con declaración de uso de beneficios» — Supuesto en que el cliente es un VPU adherido al RIGI que declaró ante la Autoridad de Aplicación que preveía usar los beneficios del art. 198 de la Ley 27.742 en materia de cobro de exportaciones; en ese caso resulta aplicable lo dispuesto en el punto 14.1.4 en lugar del plazo general del punto 7.1.3. · tramo [exacta]: «En el caso que el cliente sea un Vehículo de Proyecto Único (VPU) adherido al Régimen de Incentivo para Grandes Inversiones (RIGI) que declaró ante la Autoridad de Aplicación que preveía hacer uso de los beneficios establecidos en el artículo 198 de la Ley 27.742 en materia de cobro de exportaciones de bienes y servici…»
- **ley1 Comunicacion** «Ley 27.742» —  · props: `{"codigo": "Ley 27.742", "tipo": "externa"}` · tramo [exacta]: «Ley 27.742»
- R: ob1 Obligacion —regula→ op1 Operacion
- R: to TextoOrdenado —referencia→ ley1 Comunicacion

### A — omisiones de T4 a clasificar

- sin_marca:9 → entidades: — | omisiones: —

## Código H

- **op1 Operacion** «Anticipos, prefinanciaciones y posfinanciaciones del exterior» — Anticipos, prefinanciaciones y posfinanciaciones del exterior, cuyo cobro o desembolso se produce en el exterior · props: `{"tipo": "financiacion del exterior"}` · tramo [exacta]: «Los anticipos, prefinanciaciones y posfinanciaciones del exterior»
- **ob1 Obligacion** «Ingreso y liquidación en 20 días hábiles» — Los anticipos, prefinanciaciones y posfinanciaciones del exterior deben ser ingresados y liquidados en el mercado de cambios dentro de los 20 días hábiles de la fecha de cobro o desembolso en el exterior · props: `{"tipo": "otra"}` · umbral: ['dentro de los 20 (veinte) días hábiles de la fecha de cobro o desembolso en el e…'] · tramo [exacta]: «deberán ser ingresadas y liquidadas en el mercado de cambios dentro de los 20 (veinte) días hábiles de la fecha de cobro o desembolso en el exterior»
- **c1 Condicion** «Cliente VPU adherido al RIGI con beneficio art. 198» — Que el cliente sea un VPU adherido al RIGI que declaró ante la Autoridad de Aplicación que preveía usar los beneficios del art. 198 de la Ley 27.742 en materia de cobro de exportaciones; en ese caso rige el punto 14.1.4 en lugar del plazo de 20 días hábiles · tramo [exacta]: «En el caso que el cliente sea un Vehículo de Proyecto Único (VPU) adherido al Régimen de Incentivo para Grandes Inversiones (RIGI) que declaró ante la Autoridad de Aplicación que preveía hacer uso de los beneficios establecidos en el artículo 198 de la Ley 27.742 en materia de cobro de exportaciones de bienes y servici…»
- R: ob1 Obligacion —regula→ op1 Operacion
- R: c1 Condicion —condicion_de→ ob1 Obligacion

### H — omisiones de T4 a clasificar

- sin_marca:9 → entidades: c1 Condicion [exacta] solap 1.0 contiene | omisiones: —

## Código K

- **op1 Operacion** «Ingreso y liquidación de anticipos/prefinanciaciones del exterior» — Ingreso y liquidación en el mercado de cambios de anticipos, prefinanciaciones y posfinanciaciones del exterior de exportaciones de bienes · props: `{"tipo": "ingreso y liquidación de divisas"}` · tramo [exacta]: «Los anticipos, prefinanciaciones y posfinanciaciones del exterior deberán ser ingresadas y liquidadas en el mercado de cambios»
- **ob1 Obligacion** «Plazo 20 días hábiles — liquidar anticipos y financiaciones del exterior» — Los anticipos, prefinanciaciones y posfinanciaciones del exterior deben ingresarse y liquidarse en el mercado de cambios dentro de los 20 días hábiles de la fecha de cobro o desembolso en el exterior. · props: `{"tipo": "otra"}` · umbral: ['dentro de los 20 (veinte) días hábiles de la fecha de cobro o desembolso en el e…'] · tramo [exacta]: «Los anticipos, prefinanciaciones y posfinanciaciones del exterior deberán ser ingresadas y liquidadas en el mercado de cambios dentro de los 20 (veinte) días hábiles de la fecha de cobro o desembolso en el exterior.»
- **ex1 Excepcion** «VPU RIGI con beneficios art. 198 — régimen 14.1.4» — Cuando el cliente es un VPU adherido al RIGI que declaró prever usar los beneficios del art. 198 de la Ley 27.742 en cobro de exportaciones, en lugar del plazo de 20 días hábiles rige lo dispuesto en el punto 14.1.4. · tramo [exacta]: «En el caso que el cliente sea un Vehículo de Proyecto Único (VPU) adherido al Régimen de Incentivo para Grandes Inversiones (RIGI) que declaró ante la Autoridad de Aplicación que preveía hacer uso de los beneficios establecidos en el artículo 198 de la Ley 27.742 en materia de cobro de exportaciones de bienes y servici…»
- **c1 Condicion** «Cliente VPU RIGI que declaró usar art. 198» — El cliente es un VPU adherido al RIGI que declaró ante la Autoridad de Aplicación que preveía usar los beneficios del art. 198 de la Ley 27.742 en materia de cobro de exportaciones. · tramo [exacta]: «el cliente sea un Vehículo de Proyecto Único (VPU) adherido al Régimen de Incentivo para Grandes Inversiones (RIGI) que declaró ante la Autoridad de Aplicación que preveía hacer uso de los beneficios establecidos en el artículo 198 de la Ley 27.742»
- **l1 Comunicacion** «Ley 27.742» —  · props: `{"codigo": "Ley 27.742", "tipo": "externa"}` · tramo [exacta]: «Ley 27.742»
- R: ob1 Obligacion —regula→ op1 Operacion
- R: ex1 Excepcion —exceptua_obligacion→ ob1 Obligacion
- R: c1 Condicion —condicion_de→ ex1 Excepcion
- R: ex1 Excepcion —aplica_a→ Sujeto_vpu_rigi (mención «un Vehículo de Proyecto Único (VPU) adherido al Régimen de Incentivo para Grandes Inversiones (RIGI)»)
- R: to TextoOrdenado —referencia→ l1 Comunicacion

### K — omisiones de T4 a clasificar

- sin_marca:9 → entidades: ex1 Excepcion [exacta] solap 1.0 contiene | omisiones: —

## Código W

- **op1 Operacion** «Ingreso y liquidación de anticipos y financiaciones del exterior» — Ingreso y liquidación en el mercado de cambios de anticipos, prefinanciaciones y posfinanciaciones del exterior de exportaciones de bienes · props: `{"tipo": "ingreso y liquidación de divisas"}` · tramo [exacta]: «Los anticipos, prefinanciaciones y posfinanciaciones del exterior deberán ser ingresadas y liquidadas en el mercado de cambios»
- **ob1 Obligacion** «Plazo 20 días hábiles — ingreso y liquidación de anticipos» — Los anticipos, prefinanciaciones y posfinanciaciones del exterior deben ingresarse y liquidarse en el mercado de cambios dentro de los 20 días hábiles de la fecha de cobro o desembolso en el exterior. · props: `{"tipo": "otra"}` · umbral: ['dentro de los 20 (veinte) días hábiles de la fecha de cobro o desembolso en el e…'] · tramo [exacta]: «Los anticipos, prefinanciaciones y posfinanciaciones del exterior deberán ser ingresadas y liquidadas en el mercado de cambios dentro de los 20 (veinte) días hábiles de la fecha de cobro o desembolso en el exterior.»
- **ex1 Excepcion** «VPU RIGI con beneficios art. 198 — régimen 14.1.4» — Si el cliente es un VPU adherido al RIGI que declaró prever usar los beneficios del art. 198 de la Ley 27.742 en cobro de exportaciones, en lugar del plazo de 20 días hábiles rige lo dispuesto en el punto 14.1.4. · tramo [exacta]: «En el caso que el cliente sea un Vehículo de Proyecto Único (VPU) adherido al Régimen de Incentivo para Grandes Inversiones (RIGI) que declaró ante la Autoridad de Aplicación que preveía hacer uso de los beneficios establecidos en el artículo 198 de la Ley 27.742 en materia de cobro de exportaciones de bienes y servici…»
- **c1 Condicion** «Declaración ante Autoridad de Aplicación de uso art. 198» — Que el VPU haya declarado ante la Autoridad de Aplicación que preveía usar los beneficios del art. 198 de la Ley 27.742 en materia de cobro de exportaciones de bienes y servicios. · tramo [exacta]: «que declaró ante la Autoridad de Aplicación que preveía hacer uso de los beneficios establecidos en el artículo 198 de la Ley 27.742»
- **com1 Comunicacion** «Ley 27.742» —  · props: `{"codigo": "Ley 27.742", "tipo": "externa"}` · tramo [exacta]: «Ley 27.742»
- R: ob1 Obligacion —regula→ op1 Operacion
- R: ex1 Excepcion —exceptua_obligacion→ ob1 Obligacion
- R: c1 Condicion —condicion_de→ ex1 Excepcion
- R: ex1 Excepcion —aplica_a→ Sujeto_vpu_rigi (mención «Vehículo de Proyecto Único (VPU) adherido al Régimen de Incentivo para Grandes Inversiones (RIGI)»)
- R: to TextoOrdenado —referencia→ com1 Comunicacion

### W — omisiones de T4 a clasificar

- sin_marca:9 → entidades: ex1 Excepcion [exacta] solap 1.0 contiene | omisiones: —

