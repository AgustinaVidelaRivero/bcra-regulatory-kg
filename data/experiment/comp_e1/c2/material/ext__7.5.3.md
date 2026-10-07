# `ext::7.5.3` — Permisos cuyos fondos se encuentran retenidos en las cuentas asociadas a los

Grupos: omisiones. Estado final en la tanda 0: `completo_ok_directo`.

## Texto

> *heredado:* Sección 7. Cobros de exportaciones de bienes.
> *heredado:* 7.5. Ampliaciones del plazo para el ingreso y liquidación de divisas.
> *heredado:* La entidad encargada del seguimiento del permiso podrá conceder extensiones en el plazo de ingreso y liquidación en las siguientes circunstancias:
> *propio:* 7.5.3. Permisos cuyos fondos se encuentran retenidos en las cuentas asociadas a los endeudamientos financieros referidas en los puntos 7.3.5., 7.9. y 7.11. y las prefinanciaciones de exportaciones comprendidas en el punto 7.8.5. En caso de que la fecha hasta la cual los cobros de un permiso deben permanecer depositados en virtud de lo exigido en el contrato del financiamiento fuese posterior al vencimiento del plazo para la liquidación de divisas del permiso, el exportador podrá solicitar que este plazo sea ampliado hasta el quinto día hábil posterior a dicha fecha. Esta opción estará disponible hasta alcanzar el 125% (ciento veinticinco por ciento) de los servicios por capital e intereses a abonar en el mes corriente y los siguientes 6 (seis) meses calendario.

## Omisiones leídas en T4 (M2)

con_marca:23 [normativa; heredado] «La entidad encargada del seguimiento del permiso podrá conceder extensiones en el plazo de ingreso y liquidación en las siguientes circunstancias:»

## Código A

- **op1 Operacion** «Ampliación plazo liquidación de divisas — fondos retenidos» — Ampliación del plazo para la liquidación de divisas de permisos cuyos fondos están retenidos en cuentas asociadas a endeudamientos financieros (puntos 7.3.5., 7.9. y 7.11.) y prefinanciaciones de exportaciones (punto 7.8.5.), hasta el quinto día hábil posterior a la fecha hasta la cual los cobros deben permanecer depositados según el contrato de financiamiento. · props: `{"tipo": "ampliacion_plazo_liquidacion"}` · tramo [exacta]: «el exportador podrá solicitar que este plazo sea ampliado hasta el quinto día hábil posterior a dicha fecha»
- **pot1 Potestad** «Exportador puede solicitar ampliación hasta 5.º día hábil» — El exportador puede solicitar que el plazo para la liquidación de divisas del permiso sea ampliado hasta el quinto día hábil posterior a la fecha hasta la cual los cobros deben permanecer depositados en virtud del contrato de financiamiento. · tramo [exacta]: «el exportador podrá solicitar que este plazo sea ampliado hasta el quinto día hábil posterior a dicha fecha»
- **pot2 Potestad** «Entidad concede extensión — fondos retenidos en cuentas asociadas» — La entidad encargada del seguimiento del permiso puede conceder extensiones en el plazo de ingreso y liquidación para permisos cuyos fondos se encuentran retenidos en las cuentas asociadas a los endeudamientos financieros referidos en los puntos 7.3.5., 7.9. y 7.11. y a las prefinanciaciones de exportaciones comprendidas en el punto 7.8.5. · tramo [exacta]: «La entidad encargada del seguimiento del permiso podrá conceder extensiones en el plazo de ingreso y liquidación en las siguientes circunstancias: [...] Permisos cuyos fondos se encuentran retenidos en las cuentas asociadas a los»
- **cond1 Condicion** «Fecha de depósito exigida posterior al vencimiento del plazo» — La fecha hasta la cual los cobros del permiso deben permanecer depositados según el contrato de financiamiento es posterior al vencimiento del plazo para la liquidación de divisas del permiso. · tramo [exacta]: «En caso de que la fecha hasta la cual los cobros de un permiso deben permanecer depositados en virtud de lo exigido en el contrato del financiamiento fuese posterior al vencimiento del plazo para la liquidación de divisas del permiso»
- **res1 Restriccion** «Tope 125% de servicios de capital e intereses» — La opción de ampliación del plazo está disponible hasta alcanzar el 125% de los servicios por capital e intereses a abonar en el mes corriente y los siguientes 6 meses calendario. · props: `{"tipo": "limite_cuantitativo"}` · umbral: ['hasta alcanzar el 125% (ciento veinticinco por ciento) de los servicios por capi…', 'el mes corriente y los siguientes 6 (seis) meses calendario'] · tramo [exacta]: «Esta opción estará disponible hasta alcanzar el 125% (ciento veinticinco por ciento) de los servicios por capital e intereses a abonar en el mes corriente y los siguientes 6 (seis) meses calendario.»
- R: pot1 Potestad —aplica_a→ Sujeto_exportador (mención «el exportador»)
- R: pot2 Potestad —aplica_a→ Sujeto (mención «La entidad encargada del seguimiento del permiso»)
- R: cond1 Condicion —condicion_de→ pot1 Potestad
- R: res1 Restriccion —limita→ op1 Operacion

### A — omisiones de T4 a clasificar

- con_marca:23 → entidades: pot2 Potestad [exacta] solap 1.0 contiene | omisiones: —

## Código H

- **op1 Operacion** «Ampliación plazo liquidación — fondos retenidos en cuentas asociadas» — Ampliación del plazo para la liquidación de divisas de permisos cuyos fondos están retenidos en las cuentas asociadas a endeudamientos financieros (puntos 7.3.5., 7.9. y 7.11.) y prefinanciaciones de exportaciones (punto 7.8.5.), hasta el quinto día hábil posterior a la fecha hasta la cual los cobros deben permanecer depositados · props: `{"tipo": "ampliacion_plazo_liquidacion_divisas"}` · tramo [exacta]: «este plazo sea ampliado hasta el quinto día hábil posterior a dicha fecha»
- **pot1 Potestad** «Entidad puede conceder extensión — fondos retenidos» — La entidad encargada del seguimiento del permiso puede conceder extensiones en el plazo de ingreso y liquidación para permisos cuyos fondos se encuentran retenidos en las cuentas asociadas a los endeudamientos financieros (puntos 7.3.5., 7.9. y 7.11.) y a las prefinanciaciones de exportaciones (punto 7.8.5.) · tramo [exacta]: «La entidad encargada del seguimiento del permiso podrá conceder extensiones en el plazo de ingreso y liquidación en las siguientes circunstancias: […] Permisos cuyos fondos se encuentran retenidos en las cuentas asociadas a los endeudamientos financieros referidas en los puntos 7.3.5., 7.9. y 7.11. y las prefinanciacio…»
- **pot2 Potestad** «Exportador puede solicitar ampliación hasta quinto día hábil» — El exportador puede solicitar que el plazo para la liquidación de divisas del permiso sea ampliado hasta el quinto día hábil posterior a la fecha hasta la cual los cobros deben permanecer depositados según el contrato del financiamiento · tramo [exacta]: «el exportador podrá solicitar que este plazo sea ampliado hasta el quinto día hábil posterior a dicha fecha»
- **cond1 Condicion** «Fecha de retención posterior al vencimiento del plazo» — La fecha hasta la cual los cobros del permiso deben permanecer depositados según el contrato del financiamiento es posterior al vencimiento del plazo para la liquidación de divisas del permiso · tramo [exacta]: «En caso de que la fecha hasta la cual los cobros de un permiso deben permanecer depositados en virtud de lo exigido en el contrato del financiamiento fuese posterior al vencimiento del plazo para la liquidación de divisas del permiso»
- **res1 Restriccion** «Tope 125% servicios de capital e intereses — ampliación» — La opción de ampliación del plazo está disponible hasta alcanzar el 125% de los servicios por capital e intereses a abonar en el mes corriente y los siguientes 6 meses calendario · props: `{"tipo": "limite_cuantitativo"}` · umbral: ['hasta alcanzar el 125% (ciento veinticinco por ciento) de los servicios por capi…', 'los siguientes 6 (seis) meses calendario'] · tramo [exacta]: «Esta opción estará disponible hasta alcanzar el 125% (ciento veinticinco por ciento) de los servicios por capital e intereses a abonar en el mes corriente y los siguientes 6 (seis) meses calendario.»
- R: cond1 Condicion —condicion_de→ pot2 Potestad
- R: res1 Restriccion —limita→ op1 Operacion
- R: pot1 Potestad —aplica_a→ Sujeto (mención «La entidad encargada del seguimiento del permiso»)
- R: pot2 Potestad —aplica_a→ Sujeto_exportador (mención «el exportador»)

### H — omisiones de T4 a clasificar

- con_marca:23 → entidades: pot1 Potestad [exacta] solap 1.0 contiene | omisiones: —

## Código K

- **e1 Potestad** «Extensión de plazo por fondos retenidos en cuentas» — La entidad encargada del seguimiento del permiso podrá conceder extensiones en el plazo de ingreso y liquidación para permisos cuyos fondos se encuentran retenidos en las cuentas asociadas a endeudamientos financieros (puntos 7.3.5., 7.9. y 7.11.) y prefinanciaciones de exportaciones (punto 7.8.5.). · tramo [exacta]: «La entidad encargada del seguimiento del permiso podrá conceder extensiones en el plazo de ingreso y liquidación en las siguientes circunstancias: […] Permisos cuyos fondos se encuentran retenidos en las cuentas asociadas a los endeudamientos financieros referidas en los puntos 7.3.5., 7.9. y 7.11. y las prefinanciacio…»
- **e2 Potestad** «Solicitud de ampliación hasta quinto día hábil» — El exportador podrá solicitar que el plazo de liquidación del permiso sea ampliado hasta el quinto día hábil posterior a la fecha hasta la cual los cobros deben permanecer depositados según el contrato de financiamiento. · tramo [exacta]: «el exportador podrá solicitar que este plazo sea ampliado hasta el quinto día hábil posterior a dicha fecha.»
- **e3 Condicion** «Fecha de depósito posterior al vencimiento del plazo» — Que la fecha hasta la cual los cobros deben permanecer depositados por el contrato de financiamiento sea posterior al vencimiento del plazo de liquidación del permiso. · tramo [exacta]: «En caso de que la fecha hasta la cual los cobros de un permiso deben permanecer depositados en virtud de lo exigido en el contrato del financiamiento fuese posterior al vencimiento del plazo para la liquidación de divisas del permiso»
- **e4 Restriccion** «Tope 125% servicios de capital e intereses — ampliación» — La opción de ampliación está disponible hasta alcanzar el 125% de los servicios por capital e intereses a abonar en el mes corriente y los siguientes 6 meses calendario. · props: `{"tipo": "limite_cuantitativo"}` · umbral: ['hasta alcanzar el 125% (ciento veinticinco por ciento) de los servicios por capi…', 'el mes corriente y los siguientes 6 (seis) meses calendario'] · tramo [exacta]: «Esta opción estará disponible hasta alcanzar el 125% (ciento veinticinco por ciento) de los servicios por capital e intereses a abonar en el mes corriente y los siguientes 6 (seis) meses calendario.»
- **e5 Operacion** «Ampliación del plazo de liquidación de divisas» — Ampliación del plazo de ingreso y liquidación de divisas de un permiso de exportación con fondos retenidos en cuentas de financiamiento. · props: `{"tipo": "ampliación de plazo"}` · tramo [exacta]: «que este plazo sea ampliado hasta el quinto día hábil posterior a dicha fecha»
- R: e1 Potestad —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «La entidad encargada del seguimiento del permiso»)
- R: e2 Potestad —aplica_a→ Sujeto_exportador (mención «el exportador»)
- R: e3 Condicion —condicion_de→ e2 Potestad
- R: e4 Restriccion —limita→ e5 Operacion

### K — omisiones de T4 a clasificar

- con_marca:23 → entidades: e1 Potestad [exacta] solap 1.0 contiene | omisiones: —

## Código W

- **e1 Potestad** «Ampliación de plazo por fondos retenidos en cuentas» — La entidad encargada del seguimiento del permiso podrá conceder extensiones en el plazo de ingreso y liquidación de divisas para permisos cuyos fondos se encuentran retenidos en las cuentas asociadas a endeudamientos financieros (puntos 7.3.5., 7.9. y 7.11.) y prefinanciaciones de exportaciones (punto 7.8.5.). · tramo [exacta]: «La entidad encargada del seguimiento del permiso podrá conceder extensiones en el plazo de ingreso y liquidación en las siguientes circunstancias: […] Permisos cuyos fondos se encuentran retenidos en las cuentas asociadas a los endeudamientos financieros referidas en los puntos 7.3.5., 7.9. y 7.11. y las prefinanciacio…»
- **e2 Potestad** «Solicitud del exportador de ampliar plazo de liquidación» — El exportador podrá solicitar que el plazo para la liquidación de divisas del permiso sea ampliado hasta el quinto día hábil posterior a la fecha hasta la cual los cobros deben permanecer depositados según el contrato del financiamiento. · tramo [exacta]: «el exportador podrá solicitar que este plazo sea ampliado hasta el quinto día hábil posterior a dicha fecha.»
- **e3 Condicion** «Fecha de depósito contractual posterior al vencimiento» — Que la fecha hasta la cual los cobros deben permanecer depositados según el contrato del financiamiento sea posterior al vencimiento del plazo de liquidación del permiso. · tramo [exacta]: «En caso de que la fecha hasta la cual los cobros de un permiso deben permanecer depositados en virtud de lo exigido en el contrato del financiamiento fuese posterior al vencimiento del plazo para la liquidación de divisas del permiso»
- **e4 Restriccion** «Tope 125% servicios de capital e intereses — ampliación» — La ampliación está disponible hasta alcanzar el 125% de los servicios por capital e intereses a abonar en el mes corriente y los siguientes 6 meses calendario. · props: `{"tipo": "limite_cuantitativo"}` · umbral: ['hasta alcanzar el 125% (ciento veinticinco por ciento) de los servicios por capi…', 'el mes corriente y los siguientes 6 (seis) meses calendario'] · tramo [exacta]: «Esta opción estará disponible hasta alcanzar el 125% (ciento veinticinco por ciento) de los servicios por capital e intereses a abonar en el mes corriente y los siguientes 6 (seis) meses calendario.»
- **e5 Operacion** «Ampliación del plazo de liquidación por fondos retenidos» — Ampliación del plazo de ingreso y liquidación de divisas de un permiso con cobros retenidos en cuentas asociadas a financiamientos. · props: `{"tipo": "ampliación de plazo"}` · tramo [exacta]: «solicitar que este plazo sea ampliado hasta el quinto día hábil posterior a dicha fecha»
- R: e1 Potestad —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «La entidad encargada del seguimiento del permiso»)
- R: e2 Potestad —aplica_a→ Sujeto_exportador (mención «el exportador»)
- R: e3 Condicion —condicion_de→ e2 Potestad
- R: e4 Restriccion —limita→ e5 Operacion

### W — omisiones de T4 a clasificar

- con_marca:23 → entidades: e1 Potestad [exacta] solap 1.0 contiene | omisiones: —

