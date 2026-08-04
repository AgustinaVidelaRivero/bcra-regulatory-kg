# Registro de generación — set U6

Registro histórico de las 4 rondas de generación ciega del set U6. Cada bloque
reproduce el JSON crudo completo de su ronda, tal como salió de la generación,
incluidas las preguntas que luego fueron descartadas y reemplazadas. Este
archivo NO es el set: el set consolidado de 25 preguntas aptas vive en
`preguntas_u6.json` (mismo directorio).

Validador de anclas: `data/experiment/exploracion/validar_anclas.py` contra
`data/experiment/exploracion/mapa_territorio_quemado_5TOs_4sets.json`.

## Ronda 1

Semilla: U6-GEN-2026-08-04-S1

Generación inicial completa (25 preguntas, U6-001..U6-025).

```json
[
  {"id": "U6-001", "to": "ext", "ancla": "2.2.2.1", "pregunta": "Trabajo como desarrollador de software freelance y cobro mis servicios de clientes del exterior en una cuenta en dólares de un banco local. ¿Hasta qué monto por año calendario puedo quedarme con esos cobros sin liquidarlos en el mercado de cambios, y qué condiciones tengo que cumplir?"},
  {"id": "U6-002", "to": "ext", "ancla": "3.4", "pregunta": "Una sociedad local quiere girar dividendos a sus accionistas del exterior. ¿Qué debe verificar el banco respecto de los balances de la empresa y del monto aprobado por la asamblea antes de dar curso a la transferencia?"},
  {"id": "U6-003", "to": "ext", "ancla": "3.12.1", "pregunta": "Una empresa contrató una cobertura de tasa de interés por su deuda financiera con el exterior y la liquidación del derivado arrojó fondos a su favor. ¿En qué plazo debe ingresar y liquidar esos fondos en el mercado de cambios, y qué compromiso previo tuvo que asumir para operar con acceso al mercado?"},
  {"id": "U6-004", "to": "ext", "ancla": "3.16.2", "pregunta": "Antes de darle a una empresa acceso al mercado de cambios para un pago al exterior, ¿qué declaración jurada sobre activos externos líquidos y CEDEARs debe presentar el cliente, y a partir de qué valor de tenencias pasa a necesitarse la conformidad previa del BCRA?"},
  {"id": "U6-005", "to": "ext", "ancla": "4.1.1", "pregunta": "Estoy de viaje afuera y necesito efectivo: ¿cuál es el monto máximo por operación que puedo obtener como adelanto en efectivo con una tarjeta de crédito emitida en el país, y cambia ese tope si estoy en un país no limítrofe?"},
  {"id": "U6-006", "to": "ext", "ancla": "5.9.5", "pregunta": "Una entidad financiera suscribió títulos en una colocación primaria con liquidación contra cable en una cuenta del exterior. ¿Cuánto tiempo debe esperar para poder venderlos en el mercado secundario con liquidación en moneda extranjera en el país, y aplica esa espera si los vende contra cable en el exterior?"},
  {"id": "U6-007", "to": "ext", "ancla": "7.1.1", "pregunta": "Exportamos bienes industriales que no están alcanzados por plazos especiales y la operación no es con una contraparte vinculada. ¿De cuántos días disponemos desde el cumplido de embarque para ingresar y liquidar las divisas, y qué plazo rige si el cobro del exterior se percibe antes de ese vencimiento?"},
  {"id": "U6-008", "to": "ext", "ancla": "7.5.3", "pregunta": "El contrato de un financiamiento exige que los cobros de nuestras exportaciones queden retenidos en una cuenta de garantía hasta una fecha posterior al vencimiento del plazo de liquidación del permiso de embarque. ¿Puede ampliarse ese plazo, hasta cuándo, y con qué límite en función de los servicios de deuda a pagar?"},
  {"id": "U6-009", "to": "ext", "ancla": "10.3.2", "pregunta": "Para pagar al exterior una importación que ya cuenta con registro de ingreso aduanero bajo el SEPAIMPO, ¿qué documentación y verificaciones debe completar la entidad antes de dar acceso al mercado de cambios?"},
  {"id": "U6-010", "to": "ext", "ancla": "13.2.7", "pregunta": "Mi empresa recibe servicios de gestión de su casa matriz del exterior, prestados durante este año. ¿Cuánto tiempo debe transcurrir desde la prestación del servicio para poder pagarlo por el mercado de cambios, y qué pasa si después del devengamiento la deuda se transfiere a un acreedor no vinculado?"},
  {"id": "U6-011", "to": "cap", "ancla": "1.4.2.1", "pregunta": "Una entidad financiera en funcionamiento detecta e informa un incumplimiento de su exigencia de capital mínimo. ¿En qué plazo debe encuadrarse o presentar un plan de regularización y saneamiento, y qué restricciones le aplican sobre depósitos y distribución de dividendos mientras tanto?"},
  {"id": "U6-012", "to": "cap", "ancla": "2.8.3.3", "pregunta": "Para que un préstamo de consumo a una persona humana pueda computarse dentro de las exposiciones minoristas normativas, ¿cuál es la exposición máxima admitida frente a esa contraparte al momento del acuerdo y en qué referencia salarial se expresa?"},
  {"id": "U6-013", "to": "cap", "ancla": "4.1.1", "pregunta": "Una operación de compraventa de títulos bajo la modalidad entrega contra pago no se liquidó en la fecha acordada. ¿A partir de cuántos días hábiles de atraso se genera exigencia de capital y cómo va aumentando el porcentaje aplicable a medida que pasa el tiempo?"},
  {"id": "U6-014", "to": "cap", "ancla": "6.4.2.1", "pregunta": "Al calcular la exigencia de capital por riesgo de tipo de cambio, ¿qué componentes deben sumarse para determinar la posición abierta neta en cada moneda, además de la posición neta al contado?"},
  {"id": "U6-015", "to": "cap", "ancla": "8.4.1.3", "pregunta": "¿Cuándo deben deducirse del capital ordinario de nivel uno los saldos mantenidos en cuentas de corresponsalía en bancos del exterior, por qué importe se practica la deducción y qué contrapartes quedan exceptuadas?"},
  {"id": "U6-016", "to": "cla", "ancla": "4.6", "pregunta": "En financiaciones cedidas sin responsabilidad para el cedente que están amparadas con un seguro de crédito por riesgo comercial, ¿a quién debe clasificar la entidad y a partir de qué momento comienza a computarse la mora?"},
  {"id": "U6-017", "to": "cla", "ancla": "6.3.1", "pregunta": "¿Con qué frecuencia mínima debe revisarse la clasificación de un cliente de cartera comercial cuyas financiaciones alcanzan en algún momento el 5 % o más de la responsabilidad patrimonial computable de la entidad, y cómo se trata a un grupo de contrapartes conectadas a estos fines?"},
  {"id": "U6-018", "to": "cla", "ancla": "7.4", "pregunta": "¿En qué situaciones el deterioro de la cartera irregular de consumo o vivienda obliga a la entidad a informar su origen a la Superintendencia de Entidades Financieras y Cambiarias, y qué umbrales trimestral y anual disparan esa obligación?"},
  {"id": "U6-019", "to": "cla", "ancla": "3.3", "pregunta": "¿Qué aspectos del proceso de clasificación y previsionamiento debe documentar la entidad en su manual de procedimientos, y a disposición de quién debe estar ese manual?"},
  {"id": "U6-020", "to": "ric", "ancla": "S1 (1.1.)", "pregunta": "Dentro del régimen informativo de exigencia e integración de capitales mínimos, ¿qué informaciones se apartan de la frecuencia mensual general y con los datos de qué meses se integran?"},
  {"id": "U6-021", "to": "ric", "ancla": "4.1.1", "pregunta": "Al informar la exigencia por riesgo de mercado, ¿con los valores de qué fecha se determina el total, y cómo debe identificarse por moneda la partida de exigencia por riesgo general de tasa de interés?"},
  {"id": "U6-022", "to": "ric", "ancla": "5.1.1", "pregunta": "Para una entidad del Grupo 1, ¿cómo se determina la exigencia de capital por riesgo operacional a informar y qué coeficientes marginales se aplican según el tramo del indicador de negocio?"},
  {"id": "U6-023", "to": "pro", "ancla": "2.6", "pregunta": "¿Puede una entidad rechazar una solicitud de financiación basándose únicamente en la edad del solicitante cuando sus ingresos proyectados son suficientes, y qué papel juega la posibilidad de contratar un seguro de vida sobre saldo deudor?"},
  {"id": "U6-024", "to": "pro", "ancla": "2.7", "pregunta": "¿Qué características de identificación y ubicación deben cumplir el botón de arrepentimiento y el botón de baja en el home banking para que el usuario pueda revocar una contratación o rescindir un servicio en el mismo acto?"},
  {"id": "U6-025", "to": "pro", "ancla": "4.2.1", "pregunta": "Presenté un reclamo ante mi banco y no obtuve respuesta. ¿Cuántos días hábiles deben pasar para poder informar la situación al BCRA, y qué datos y documentación debe incluir esa presentación?"}
]
```

## Ronda 2

Semilla: U6-GEN-2026-08-04-S1-R2

Regeneración de los slots descartados tras la validación de anclas de la ronda 1 (10 preguntas).

```json
[
  {"id": "U6-001", "to": "ext", "ancla": "2.7", "pregunta": "Una empresa cobró una exportación y tiene los fondos en su cuenta en moneda extranjera en un banco local. ¿Bajo qué condiciones puede aplicar esas divisas directamente a un pago que tendría acceso al mercado de cambios, sin liquidarlas previamente a pesos, y cómo juegan los límites mensuales del concepto en ese mecanismo?"},
  {"id": "U6-005", "to": "ext", "ancla": "4.3.2", "pregunta": "Una persona jurídica quiere operar compraventa de títulos valores con liquidación en moneda extranjera. ¿Por qué mecanismos puede abonar esas operaciones y qué formas de pago están expresamente vedadas?"},
  {"id": "U6-007", "to": "ext", "ancla": "7.6", "pregunta": "El comprador del exterior no pagó nuestra exportación de bienes. ¿En qué situaciones la entidad de seguimiento puede registrar el permiso de embarque como incumplido en gestión de cobro, aplica esa figura si la contraparte es vinculada, y qué plazo rige para liquidar las divisas si el importador finalmente paga?"},
  {"id": "U6-010", "to": "ext", "ancla": "3.3", "pregunta": "Mi empresa debe intereses por una deuda comercial con su proveedor del exterior. ¿A partir de qué momento puede acceder al mercado de cambios para pagarlos y qué se necesita si quisiera precancelarlos antes del vencimiento?"},
  {"id": "U6-012", "to": "cap", "ancla": "2.13", "pregunta": "Al convertir partidas fuera de balance en equivalentes crediticios, ¿qué factor de conversión corresponde a una garantía financiera tipo carta de crédito stand-by, cuál a una garantía de cumplimiento de obligaciones comerciales y cuál a una carta de crédito comercial de corto plazo autoliquidable?"},
  {"id": "U6-013", "to": "cap", "ancla": "5.3.1", "pregunta": "Bajo el método simple de cobertura del riesgo de crédito con activos en garantía, ¿qué condiciones de plazo y de valuación debe cumplir la garantía para ser reconocida, y qué ponderador mínimo recibe la parte cubierta de la exposición?"},
  {"id": "U6-017", "to": "cla", "ancla": "7.2.1", "pregunta": "En la cartera de consumo o vivienda, ¿hasta cuántos días de atraso un cliente se mantiene en situación normal, qué tratamiento particular reciben los adelantos transitorios en cuenta corriente y cuántas refinanciaciones admite la categoría en un período de 12 meses?"},
  {"id": "U6-020", "to": "ric", "ancla": "3.1.2", "pregunta": "En la información de exigencia por riesgo de crédito, ¿mediante qué expresión se calcula la exigencia de capital, qué representa el factor vinculado a la calificación de la entidad y cómo se componen los activos ponderados por riesgo?"},
  {"id": "U6-022", "to": "ric", "ancla": "9.1.1", "pregunta": "Cuando una entidad verifica excesos a los límites crediticios individuales, ¿qué incrementos de exigencia por riesgo de crédito debe informar y qué datos debe consignar respecto de cada cliente que motivó el exceso?"},
  {"id": "U6-025", "to": "pro", "ancla": "3.2.1.1", "pregunta": "¿Qué jerarquía debe tener el Directivo Responsable de Protección de los Usuarios de Servicios Financieros, con qué frecuencia mínima debe elevar su reporte de análisis al Directorio y en qué casos puede reemplazarse esa figura por un comité?"}
]
```

## Ronda 3

Semilla: U6-GEN-2026-08-04-S1-R3

Regeneración de los slots descartados tras la validación de anclas de la ronda 2 (3 preguntas).

```json
[
  {"id": "U6-017", "to": "cla", "ancla": "3.4.2", "pregunta": "Si un banco le baja la clasificación crediticia a un cliente, ¿en qué casos está obligado a comunicárselo, dentro de qué plazo debe hacerlo y por qué medios puede cursar esa notificación?"},
  {"id": "U6-020", "to": "ric", "ancla": "6.1", "pregunta": "Al informar la responsabilidad patrimonial computable, ¿con los saldos registrados a qué fecha se determinan las partidas admitidas, y qué conceptos deducibles se informan en cambio por el mayor saldo registrado durante el mes?"},
  {"id": "U6-022", "to": "ric", "ancla": "11.2.1", "pregunta": "En los modelos de información complementaria del cálculo del riesgo de tasa de interés en la cartera de inversión, ¿con qué apertura por monedas se presentan los cuadros y qué dimensiones —escenarios, bandas temporales, tipo de tasa— se utilizan para informar los activos y pasivos susceptibles de estandarización?"}
]
```

## Ronda 4

Semilla: U6-GEN-2026-08-04-S1-R4

Regeneración del slot descartado tras la validación de anclas de la ronda 3 (1 pregunta).

```json
[
  {"id": "U6-017", "to": "cla", "ancla": "3.6", "pregunta": "¿A partir de qué magnitud de financiaciones la clasificación de un deudor y el cálculo de sus previsiones requieren la aprobación previa del Directorio de la entidad, y qué mayoría se exige cuando se trata de clientes vinculados?"}
]
```
