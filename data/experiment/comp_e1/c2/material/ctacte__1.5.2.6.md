# `ctacte::1.5.2.6` — Pagar a la vista –excepto en los casos a que se refiere el punto 1.5.2.8., segundo

Grupos: omisiones. Estado final en la tanda 0: `aceptado_con_residuales`.

## Texto

> *heredado:* Sección 1. Funcionamiento.
> *heredado:* 1.5. Aspectos del funcionamiento a incluir en el contrato de cuenta corriente.
> *heredado:* En sus cláusulas se deberá prever, como mínimo:
> *heredado:* 1.5.2. Obligaciones de la entidad.
> *propio:* 1.5.2.6. Pagar a la vista –excepto en los casos a que se refiere el punto 1.5.2.8., segundo párrafo– los cheques librados por el cuentacorrentista, de acuerdo con las disposiciones legales y reglamentarias vigentes a la fecha de emisión del cheque, teniendo en cuenta en materia de plazos de presentación los establecidos en el artículo 25 de la Ley de Cheques. En el caso de cheques de pago diferido, ese plazo se computará a partir de la fecha de pago consignada en el cheque.

## Omisiones leídas en T4 (M2)

sin_marca:6 [normativa; propio] «de acuerdo con las disposiciones legales y reglamentarias vigentes a la fecha de emisión del cheque»

## Código A

- **ley Comunicacion** «Ley de Cheques» —  · props: `{"codigo": "Ley de Cheques", "tipo": "externa"}` · tramo [exacta]: «artículo 25 de la Ley de Cheques»
- **op1 Operacion** «Pago a la vista de cheques del cuentacorrentista» — Pago a la vista de los cheques librados por el cuentacorrentista, de acuerdo con las disposiciones legales y reglamentarias vigentes a la fecha de emisión del cheque · props: `{"tipo": "pago de cheques"}` · tramo [exacta]: «Pagar a la vista»
- **ob1 Obligacion** «Pagar a la vista cheques librados por cuentacorrentista» — Obligación de la entidad, a prever como mínimo en el contrato de cuenta corriente, de pagar a la vista los cheques librados por el cuentacorrentista, conforme a las disposiciones legales y reglamentarias vigentes a la fecha de emisión del cheque, teniendo en cuenta los plazos de presentación del artículo 25 de la Ley de Cheques · props: `{"tipo": "otra"}` · tramo [exacta]: «Pagar a la vista –excepto en los casos a que se refiere el punto 1.5.2.8., segundo párrafo– los cheques librados por el cuentacorrentista, de acuerdo con las disposiciones legales y reglamentarias vigentes a la fecha de emisión del cheque»
- **ex1 Excepcion** «Excepción casos del punto 1.5.2.8 segundo párrafo» — Quedan exceptuados del deber de pagar a la vista los cheques en los casos a que se refiere el punto 1.5.2.8., segundo párrafo · tramo [exacta]: «excepto en los casos a que se refiere el punto 1.5.2.8., segundo párrafo»
- **ob2 Obligacion** «Cómputo del plazo en cheques de pago diferido» — En cheques de pago diferido, el plazo de presentación se computa a partir de la fecha de pago consignada en el cheque · props: `{"tipo": "calculo"}` · tramo [exacta]: «En el caso de cheques de pago diferido, ese plazo se computará a partir de la fecha de pago consignada en el cheque.»
- R: to TextoOrdenado —referencia→ ley Comunicacion
- R: ob1 Obligacion —regula→ op1 Operacion
- R: ob2 Obligacion —regula→ op1 Operacion
- R: ex1 Excepcion —exceptua_obligacion→ ob1 Obligacion
- R: ob1 Obligacion —aplica_a→ Sujeto_banco (mención «la entidad»)
- R: ob2 Obligacion —aplica_a→ Sujeto_banco (mención «la entidad»)

### A — omisiones de T4 a clasificar

- sin_marca:6 → entidades: ob1 Obligacion [exacta] solap 1.0 contiene | omisiones: —

## Código H

- **ley Comunicacion** «Ley de Cheques» —  · props: `{"codigo": "Ley de Cheques", "tipo": "externa"}` · tramo [exacta]: «artículo 25 de la Ley de Cheques»
- **op1 Operacion** «Pago de cheques librados por el cuentacorrentista» — Pago a la vista de los cheques librados por el cuentacorrentista, según las disposiciones legales y reglamentarias vigentes a la fecha de emisión del cheque. · props: `{"tipo": "pago de cheques"}` · tramo [exacta]: «los cheques librados por el cuentacorrentista»
- **ob1 Obligacion** «Pagar a la vista los cheques librados» — Cláusula del contrato de cuenta corriente: pagar a la vista los cheques librados por el cuentacorrentista, de acuerdo con las disposiciones legales y reglamentarias vigentes a la fecha de emisión del cheque, teniendo en cuenta los plazos de presentación del artículo 25 de la Ley de Cheques. · props: `{"tipo": "otra"}` · tramo [no]: «Pagar a la vista –excepto en los casos a que se refiere el punto 1.5.2.8., segundo párrafo– los cheques librados por el cuentacorrentista, de acuerdo con las disposiciones legales y reglamentarias vigentes a la fecha de emisión del cheque»
- **ex1 Excepcion** «Excepción casos del punto 1.5.2.8 segundo párrafo» — Quedan exceptuados del deber de pagar a la vista los casos a que se refiere el punto 1.5.2.8., segundo párrafo. · tramo [exacta]: «excepto en los casos a que se refiere el punto 1.5.2.8., segundo párrafo»
- **ob2 Obligacion** «Plazo de presentación de cheque de pago diferido» — En cheques de pago diferido, el plazo de presentación se computa a partir de la fecha de pago consignada en el cheque. · props: `{"tipo": "calculo"}` · tramo [no]: «En el caso de cheques de pago diferido, ese plazo se computará a partir de la fecha de pago consignada en el cheque.»
- R: to TextoOrdenado —referencia→ ley Comunicacion
- R: ob1 Obligacion —regula→ op1 Operacion
- R: ob2 Obligacion —regula→ op1 Operacion
- R: ex1 Excepcion —exceptua_obligacion→ ob1 Obligacion

### H — omisiones de T4 a clasificar

- sin_marca:6 → entidades: ob1 Obligacion [no] solap 1.0 contiene | omisiones: —

## Código K

- **op1 Operacion** «Pago a la vista de cheques» — Pago a la vista por la entidad de los cheques librados por el cuentacorrentista · props: `{"tipo": "pago de cheques"}` · tramo [exacta]: «Pagar a la vista –excepto en los casos a que se refiere el punto 1.5.2.8., segundo párrafo– los cheques librados por el cuentacorrentista»
- **o1 Obligacion** «Pagar a la vista cheques librados — cláusula contractual» — El contrato de cuenta corriente debe prever, como mínimo, la obligación de la entidad de pagar a la vista los cheques librados por el cuentacorrentista, conforme a las disposiciones legales y reglamentarias vigentes a la fecha de emisión del cheque, considerando los plazos de presentación del art. 25 de la Ley de Cheques; salvo los casos del punto 1.5.2.8, segundo párrafo. · props: `{"tipo": "otra", "umbrales": [{"tramo": "teniendo en cuenta en materia de plazos de presentación los establecidos en el ar-\ntículo 25 de la Ley de Cheques", "comparacion": "no_determinada", "regla_comparacion": "limite_relativo:sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}]}` · umbral: ['teniendo en cuenta en materia de plazos de presentación los establecidos en el a…'] · tramo [exacta]: «En sus cláusulas se deberá prever, como mínimo: […] Pagar a la vista –excepto en los casos a que se refiere el punto 1.5.2.8., segundo párrafo– los cheques librados por el cuentacorrentista, de acuerdo con las disposiciones legales y reglamentarias vigentes a la fecha de emisión del cheque»
- **o2 Obligacion** «Cómputo plazo desde fecha de pago — cheques de pago diferido» — En cheques de pago diferido, el plazo de presentación se computa a partir de la fecha de pago consignada en el cheque. · props: `{"tipo": "calculo"}` · tramo [exacta]: «En el caso de cheques de pago diferido, ese plazo se computará a partir de la fecha de pago consignada en el cheque.»
- **c1 Condicion** «Cheque de pago diferido» — Supuesto de cheques de pago diferido · tramo [exacta]: «En el caso de cheques de pago diferido»
- **x1 Excepcion** «Casos del punto 1.5.2.8 — pago a la vista» — Exceptúa de la obligación de pagar a la vista los cheques en los casos del punto 1.5.2.8, segundo párrafo · tramo [exacta]: «excepto en los casos a que se refiere el punto 1.5.2.8., segundo párrafo»
- **cm1 Comunicacion** «Ley de Cheques» —  · props: `{"codigo": "Ley de Cheques", "tipo": "externa"}` · tramo [exacta]: «Ley de Cheques»
- R: to TextoOrdenado —referencia→ cm1 Comunicacion
- R: o1 Obligacion —regula→ op1 Operacion
- R: o2 Obligacion —regula→ op1 Operacion
- R: c1 Condicion —condicion_de→ o2 Obligacion
- R: x1 Excepcion —exceptua_obligacion→ o1 Obligacion
- R: o1 Obligacion —aplica_a→ Sujeto_banco (mención «la entidad»)
- R: Sujeto_banco (mención «la entidad») —ejecuta→ op1 Operacion

### K — omisiones de T4 a clasificar

- sin_marca:6 → entidades: o1 Obligacion [exacta] solap 1.0 contiene | omisiones: —

## Código W

- **c1 Comunicacion** «Ley de Cheques» —  · props: `{"codigo": "Ley de Cheques", "tipo": "externa"}` · tramo [exacta]: «artículo 25 de la Ley de Cheques»
- **op1 Operacion** «Pago a la vista de cheques» — Pago a la vista por la entidad de los cheques librados por el cuentacorrentista · props: `{"tipo": "pago de cheques"}` · tramo [exacta]: «Pagar a la vista»
- **o1 Obligacion** «Cláusula contractual: pagar a la vista cheques» — El contrato de cuenta corriente debe prever, como mínimo, la obligación de la entidad de pagar a la vista los cheques librados por el cuentacorrentista, conforme a las disposiciones legales y reglamentarias vigentes a la fecha de emisión del cheque y considerando los plazos de presentación del art. 25 de la Ley de Cheques. · props: `{"tipo": "otra"}` · tramo [exacta]: «En sus cláusulas se deberá prever, como mínimo: […] Pagar a la vista –excepto en los casos a que se refiere el punto 1.5.2.8., segundo párrafo– los cheques librados por el cuentacorrentista»
- **x1 Excepcion** «Casos del punto 1.5.2.8 segundo párrafo» — La obligación de pagar a la vista no rige en los casos del punto 1.5.2.8., segundo párrafo. · tramo [exacta]: «excepto en los casos a que se refiere el punto 1.5.2.8., segundo párrafo»
- **o2 Obligacion** «Plazo pago diferido desde fecha de pago» — En cheques de pago diferido, el plazo de presentación se computa desde la fecha de pago consignada en el cheque. · props: `{"tipo": "calculo"}` · tramo [exacta]: «En el caso de cheques de pago diferido, ese plazo se computará a partir de la fecha de pago consignada en el cheque.»
- R: to TextoOrdenado —referencia→ c1 Comunicacion
- R: o1 Obligacion —regula→ op1 Operacion
- R: o2 Obligacion —regula→ op1 Operacion
- R: x1 Excepcion —exceptua_obligacion→ o1 Obligacion
- R: o1 Obligacion —aplica_a→ Sujeto_banco (mención «la entidad»)
- R: Sujeto_banco (mención «la entidad») —ejecuta→ op1 Operacion

### W — omisiones de T4 a clasificar

- sin_marca:6 → entidades: — | omisiones: —

