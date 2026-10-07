# `ctacte::3.5.3` — Presentación al cobro.

Grupos: omisiones. Estado final en la tanda 0: `completo_ok_directo`.

## Texto

> *heredado:* Sección 3. Cheques.
> *heredado:* 3.5. Cheques librados por medios electrónicos (ECHEQ).
> *propio:* 3.5.3. Presentación al cobro. El tenedor legitimado podrá efectuar la presentación al cobro de cada ECHEQ a partir de la correspondiente fecha de pago a través de una orden electrónica de acreditación o cobrarlo por ventanilla. En su defecto, quedará pendiente hasta la fecha de vencimiento del plazo previsto en el artículo 25 de la Ley de Cheques.

## Omisiones leídas en T4 (M2)

sin_marca:27 [normativa; propio] «En su defecto»

## Código A

- **op1 Operacion** «Presentación al cobro de ECHEQ» — Presentación al cobro de cada ECHEQ por el tenedor legitimado a partir de la fecha de pago, mediante orden electrónica de acreditación o por ventanilla. · props: `{"tipo": "presentacion_al_cobro"}` · tramo [exacta]: «efectuar la presentación al cobro de cada ECHEQ a partir de la correspondiente fecha de pago»
- **p1 Potestad** «Presentar ECHEQ al cobro desde fecha de pago» — El tenedor legitimado puede presentar al cobro cada ECHEQ a partir de la fecha de pago, a través de una orden electrónica de acreditación o cobrándolo por ventanilla. · tramo [exacta]: «El tenedor legitimado podrá efectuar la presentación al cobro de cada ECHEQ a partir de la correspondiente fecha de pago a través de una orden electrónica de acreditación o cobrarlo por ventanilla.»
- **c1 Comunicacion** «Ley de Cheques» —  · props: `{"codigo": "Ley de Cheques", "tipo": "externa"}` · tramo [exacta]: «artículo 25 de la Ley de Cheques»
- R: to TextoOrdenado —referencia→ c1 Comunicacion
- R: p1 Potestad —aplica_a→ Sujeto (mención «El tenedor legitimado»)
- Omisión `fuera_de_tipos` [exacta]: «En su defecto, quedará pendiente hasta la fecha de vencimiento del plazo previsto en el artículo 25 de la Ley de Cheques.» — Consecuencia de no presentar el ECHEQ al cobro; no nombra quien la aplica ni encaja en ningún tipo.

### A — omisiones de T4 a clasificar

- sin_marca:27 → entidades: — | omisiones: om#0 fuera_de_tipos [exacta] solap 1.0 contiene

## Código H

- **e1 Operacion** «Presentación al cobro de ECHEQ» — Presentación al cobro de cada ECHEQ por el tenedor legitimado, a partir de la fecha de pago, mediante orden electrónica de acreditación o cobro por ventanilla. · props: `{"tipo": "presentacion_al_cobro"}` · tramo [exacta]: «efectuar la presentación al cobro de cada ECHEQ a partir de la correspondiente fecha de pago a través de una orden electrónica de acreditación o cobrarlo por ventanilla»
- **e2 Potestad** «Facultad del tenedor: presentar ECHEQ al cobro» — El tenedor legitimado puede presentar al cobro cada ECHEQ desde la fecha de pago, mediante orden electrónica de acreditación o por ventanilla. · tramo [exacta]: «El tenedor legitimado podrá efectuar la presentación al cobro de cada ECHEQ a partir de la correspondiente fecha de pago a través de una orden electrónica de acreditación o cobrarlo por ventanilla»
- **e3 Condicion** «ECHEQ pendiente hasta vencimiento plazo art. 25» — Si no se lo presenta al cobro, el ECHEQ queda pendiente hasta el vencimiento del plazo previsto en el artículo 25 de la Ley de Cheques. · tramo [exacta]: «En su defecto, quedará pendiente hasta la fecha de vencimiento del plazo previsto en el artículo 25 de la Ley de Cheques.»
- R: e3 Condicion —condicion_de→ e2 Potestad

### H — omisiones de T4 a clasificar

- sin_marca:27 → entidades: e3 Condicion [exacta] solap 1.0 contiene | omisiones: —

## Código K

- **op1 Operacion** «Presentación al cobro de ECHEQ» — Presentación al cobro de un cheque librado por medios electrónicos (ECHEQ) por el tenedor legitimado, mediante orden electrónica de acreditación o cobro por ventanilla · props: `{"tipo": "presentacion_al_cobro"}` · tramo [exacta]: «presentación al cobro de cada ECHEQ»
- **p1 Potestad** «Cobro de ECHEQ desde fecha de pago — tenedor legitimado» — El tenedor legitimado podrá presentar al cobro cada ECHEQ a partir de su fecha de pago, a través de una orden electrónica de acreditación o cobrándolo por ventanilla. · tramo [exacta]: «El tenedor legitimado podrá efectuar la presentación al cobro de cada ECHEQ a partir de la correspondiente fecha de pago a través de una orden electrónica de acreditación o cobrarlo por ventanilla»
- **c1 Condicion** «Desde la fecha de pago del ECHEQ» — La presentación al cobro puede efectuarse a partir de la correspondiente fecha de pago del ECHEQ. · tramo [exacta]: «a partir de la correspondiente fecha de pago»
- R: c1 Condicion —condicion_de→ p1 Potestad
- R: Sujeto (mención «El tenedor legitimado») —ejecuta→ op1 Operacion
- R: p1 Potestad —aplica_a→ Sujeto (mención «El tenedor legitimado»)
- Omisión `fuera_de_tipos` [exacta]: «En su defecto, quedará pendiente hasta la fecha de vencimiento del plazo previsto en el artículo 25 de la Ley de Cheques.» — Efecto/estado del ECHEQ no presentado (queda pendiente hasta el vencimiento del plazo legal); no es deber, prohibición ni facultad de un sujeto. Tipo que se habría usado: estado o efecto jurídico del …

### K — omisiones de T4 a clasificar

- sin_marca:27 → entidades: — | omisiones: om#0 fuera_de_tipos [exacta] solap 1.0 contiene

## Código W

- **op1 Operacion** «Presentación al cobro de ECHEQ» — Presentación al cobro de un cheque librado por medios electrónicos (ECHEQ) por el tenedor legitimado, a través de una orden electrónica de acreditación o por ventanilla · props: `{"tipo": "presentacion_al_cobro"}` · tramo [exacta]: «presentación al cobro de cada ECHEQ»
- **p1 Potestad** «Cobro de ECHEQ desde fecha de pago» — El tenedor legitimado puede presentar al cobro cada ECHEQ a partir de su fecha de pago, mediante una orden electrónica de acreditación, o cobrarlo por ventanilla · tramo [exacta]: «El tenedor legitimado podrá efectuar la presentación al cobro de cada ECHEQ a partir de la correspondiente fecha de pago a través de una orden electrónica de acreditación o cobrarlo por ventanilla»
- R: p1 Potestad —aplica_a→ Sujeto (mención «El tenedor legitimado»)
- R: Sujeto (mención «El tenedor legitimado») —ejecuta→ op1 Operacion
- Omisión `fuera_de_tipos` [exacta]: «En su defecto, quedará pendiente hasta la fecha de vencimiento del plazo previsto en el artículo 25 de la Ley de Cheques.» — Efecto sobre el estado del ECHEQ no presentado (queda pendiente hasta el vencimiento del plazo legal); no es un deber, una prohibición ni una facultad de ningún sujeto. Habría sido una Condicion o un …

### W — omisiones de T4 a clasificar

- sin_marca:27 → entidades: — | omisiones: om#0 fuera_de_tipos [exacta] solap 1.0 contiene

