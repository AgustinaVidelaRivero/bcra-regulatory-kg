# `ctacte::5.1.2.2` — A favor de fiduciarios de fideicomisos financieros comprendidos en la Ley de En-

Grupos: omisiones. Intento 0 de Haiku con marca: reintento_forma. Estado final en la tanda 0: `aceptado_tras_reintento`.

## Texto

> *heredado:* Sección 5. Endosos, modalidades especiales de emisión y aval.
> *heredado:* 5.1. Endoso.
> *heredado:* 5.1.2. El cheque extendido a favor de una persona determinada, que no posea la cláusula "no a
> *heredado:* la orden", será transmisible por endoso. También podrán ser transmitidos por endoso los cheques con la citada condición ("no a la orden"), en los casos de transferencias –primeras y sucesivas– cuando se extienda:
> *heredado:* En los casos de cheques librados al portador o a favor de una persona determinada –que posean o no la cláusula "no a la orden"– y que sean entregados por su beneficiario a un tercero para la gestión de cobro mediante su presentación en ventanilla o a través de su depósito en cuenta para su compensación electrónica, se deberá consignar al dorso la firma y aclaración –o en el correspondiente registro electrónico, la identificación– del mandante u ordenante de la gestión y su número de identificación personal –según las normas sobre "Documentos de identificación en vigencia"– en los casos de personas físicas, o CUIT o CDI en los casos de personas jurídicas, independientemente de la existencia o no del documento que instrumenta el mandato. Adicionalmente, se insertará alguna de las siguientes expresiones: "en procuración", "valor al cobro" o "para su gestión de cobro", como manifestación de los efectos de ese endoso. La obligación de consignar el número de identificación personal o CUIT o CDI, según corresponda y la leyenda mencionada anteriormente recae, indistintamente, en el mandante u ordenante y el mandatario o gestor.
> *propio:* 5.1.2.2. A favor de fiduciarios de fideicomisos financieros comprendidos en la Ley de Entidades Financieras, en la medida en que se trate de operaciones relativas al fideicomiso.

## Omisiones leídas en T4 (M2)

con_marca:28 [normativa; propio] «comprendidos en la Ley de Entidades Financieras»

## Código A

- **p1 Potestad** «Endoso de cheques "no a la orden" a fiduciarios financieros» — Podrán ser transmitidos por endoso los cheques con la cláusula "no a la orden", en los casos de transferencias (primeras y sucesivas), cuando se extiendan a favor de fiduciarios de fideicomisos financieros comprendidos en la Ley de Entidades Financieras, en la medida en que se trate de operaciones relativas al fideicomiso. · tramo [exacta]: «También podrán ser transmitidos por endoso los cheques con la citada condición ("no a la orden"), en los casos de transferencias –primeras y sucesivas– cuando se extienda: […] A favor de fiduciarios de fideicomisos financieros comprendidos en la Ley de Entidades Financieras, en la medida en que se trate de operaciones …»

### A — omisiones de T4 a clasificar

- con_marca:28 → entidades: p1 Potestad [exacta] solap 1.0 contiene | omisiones: —

## Código H

- **p1 Potestad** «Endoso de cheque "no a la orden" a favor de fiduciarios» — Facultad de transmitir por endoso los cheques con la cláusula "no a la orden", en transferencias primeras y sucesivas, cuando se extiendan a favor de fiduciarios de fideicomisos financieros comprendidos en la Ley de Entidades Financieras. · tramo [exacta]: «También podrán ser transmitidos por endoso los cheques con la citada condición ("no a la orden"), en los casos de transferencias –primeras y sucesivas– cuando se extienda: […] A favor de fiduciarios de fideicomisos financieros comprendidos en la Ley de Entidades Financieras»
- **c1 Condicion** «Operaciones relativas al fideicomiso» — El endoso del cheque "no a la orden" a favor de fiduciarios de fideicomisos financieros solo procede en la medida en que se trate de operaciones relativas al fideicomiso. · tramo [exacta]: «en la medida en que se trate de operaciones relativas al fideicomiso»
- **o1 Operacion** «Transmisión por endoso de cheque "no a la orden"» — Transmisión por endoso, en transferencias primeras y sucesivas, de cheques con la cláusula "no a la orden" extendidos a favor de fiduciarios de fideicomisos financieros comprendidos en la Ley de Entidades Financieras. · props: `{"tipo": "transmision_por_endoso"}` · tramo [exacta]: «También podrán ser transmitidos por endoso los cheques con la citada condición ("no a la orden")»
- R: c1 Condicion —condicion_de→ p1 Potestad

### H — omisiones de T4 a clasificar

- con_marca:28 → entidades: p1 Potestad [exacta] solap 1.0 contiene | omisiones: —

## Código K

- **c1 Condicion** «Cheque a favor de fiduciario de fideicomiso financiero» — Uno de los supuestos alternativos en que los cheques con cláusula "no a la orden" pueden transmitirse por endoso (transferencias primeras y sucesivas): que el cheque se extienda a favor de fiduciarios de fideicomisos financieros comprendidos en la Ley de Entidades Financieras. · tramo [exacta]: «A favor de fiduciarios de fideicomisos financieros comprendidos en la Ley de Entidades Financieras»
- **c2 Condicion** «Operaciones relativas al fideicomiso» — Para el supuesto del fiduciario, el endoso de cheques "no a la orden" se admite solo si se trata de operaciones relativas al fideicomiso. · tramo [exacta]: «en la medida en que se trate de operaciones relativas al fideicomiso»

### K — omisiones de T4 a clasificar

- con_marca:28 → entidades: c1 Condicion [exacta] solap 1.0 contiene | omisiones: —

## Código N

- **c1 Condicion** «Supuesto fiduciario fideicomiso financiero LEF» — Supuesto en que el cheque se extiende a favor de un fiduciario de fideicomiso financiero regulado por la Ley de Entidades Financieras, y la operación es relativa al fideicomiso. · tramo [exacta]: «A favor de fiduciarios de fideicomisos financieros comprendidos en la Ley de Entidades Financieras, en la medida en que se trate de operaciones relativas al fideicomiso»
- **op1 Operacion** «Transmisión por endoso — cheque a favor de fiduciario» — Transmisión de un cheque por endoso cuando se extiende a favor de un fiduciario de fideicomiso financiero comprendido en la Ley de Entidades Financieras, en operaciones relativas al fideicomiso. · props: `{"tipo": "Transmisión de cheque por endoso"}` · tramo [exacta]: «el cheque extendido a favor de una persona determinada, que no posea la cláusula 'no a la orden', será transmisible por endoso»
- R: c1 Condicion —condicion_de→ op1 Operacion
- Omisión `relacion_sin_predicado` [exacta]: «A favor de fiduciarios de fideicomisos financieros comprendidos en la Ley de Entidades Financieras» — Relación de alcance/sujeto: la operación se dirige a un sujeto específico (fiduciario de fideicomiso financiero), pero el catálogo de sujetos no proporciona un id directo para 'fiduciario de fideicomi…

### N — omisiones de T4 a clasificar

- con_marca:28 → entidades: c1 Condicion [exacta] solap 1.0 contiene | omisiones: om#0 relacion_sin_predicado [exacta] solap 1.0 contiene

## Código W

- **op1 Operacion** «Endoso de cheque «no a la orden» a fiduciario» — Transmisión por endoso (primeras y sucesivas transferencias) de cheques con cláusula «no a la orden» extendidos a favor de fiduciarios de fideicomisos financieros comprendidos en la Ley de Entidades Financieras · props: `{"tipo": "transmisión por endoso"}` · tramo [exacta]: «A favor de fiduciarios de fideicomisos financieros comprendidos en la Ley de Entidades Financieras»
- **p1 Potestad** «Endoso admitido: cheque «no a la orden» a fiduciario» — Los cheques con cláusula «no a la orden» podrán ser transmitidos por endoso, en transferencias primeras y sucesivas, cuando se extiendan a favor de fiduciarios de fideicomisos financieros comprendidos en la Ley de Entidades Financieras (uno de los supuestos alternativos de la lista). · tramo [exacta]: «También podrán ser transmitidos por endoso los cheques con la citada condición ("no a la orden"), en los casos de transferencias –primeras y sucesivas– cuando se extienda: […] A favor de fiduciarios de fideicomisos financieros comprendidos en la Ley de Entidades Financieras»
- **c1 Condicion** «Operaciones relativas al fideicomiso» — El endoso del cheque «no a la orden» al fiduciario procede en la medida en que se trate de operaciones relativas al fideicomiso. · tramo [exacta]: «en la medida en que se trate de operaciones relativas al fideicomiso»
- **ley Comunicacion** «Ley de Entidades Financieras» —  · props: `{"codigo": "Ley de Entidades Financieras", "tipo": "externa"}` · tramo [exacta]: «Ley de Entidades Financieras»
- R: c1 Condicion —condicion_de→ p1 Potestad
- R: c1 Condicion —condicion_de→ op1 Operacion
- R: to TextoOrdenado —referencia→ ley Comunicacion
- Omisión `relacion_sin_predicado` [exacta]: «También podrán ser transmitidos por endoso» — Potestad que habilita la Operacion; no hay predicado Potestad→Operacion

### W — omisiones de T4 a clasificar

- con_marca:28 → entidades: op1 Operacion [exacta] solap 1.0 contiene; p1 Potestad [exacta] solap 1.0 contiene; ley Comunicacion [exacta] solap 0.75 contenido_en | omisiones: —

