# Insumos para la generación ciega de preguntas (U6)

Fecha: 2026-08-03.

Preparo en este documento los insumos que recibe la instancia generadora,
según el protocolo `docs/protocolo_u6.md` §4 (generación ciega): los hashes
de verificación del corpus y, por TO, la lista de unidades sobre las que se
pueden formular preguntas, informando únicamente numeración y título.

Dosificación (§3 del protocolo): 25 preguntas en total — 10 de Exterior y
Cambios, 5 de Capitales Mínimos, 4 de Clasificación de Deudores, 3 de
Régimen Informativo Contable Mensual y 3 de Protección de Usuarios de
Servicios Financieros.

## Verificación del corpus (sha256 de `data/experiment/subset/`)

Antes de generar, la instancia verifica que sus 5 PDFs sean byte-idénticos
a estos hashes:

```
f6ab71be7783c4192e67c13ee84f1fc585c6ae5e05aa074961c9c59429280bb8  TO_capitales_minimos_actual.pdf
6e7f528d3fea7b756f15e1278eecd828f203f0651fc6f778212033de6a0883e2  TO_clasificacion_deudores_actual.pdf
baea7264918877da132acca5f7ec6df1a3a33fd5be77109b90360a3d586bc130  TO_exterior_cambios_actual.pdf
48564cc714daa9a8c8bbd7115dfe006307ca7cb1c3d78b106c52555fe75a12ec  TO_proteccion_usuarios_servicios_financieros_actual.pdf
754c888ae6034f63eb04991c5cad441435b6bf6f8e8fb3669fd2bb279c3b35d5  TO_regimen_informativo_contable_mensual_actual.pdf
```

## Exterior y Cambios (`TO_exterior_cambios_actual.pdf`) — 10 preguntas — 108 unidades

- S1 — Disposiciones generales. (sección sin puntos en índice)
- 2.1 — Cobros de exportaciones de bienes.
- 2.2 — Cobros de exportaciones de servicios.
- 2.3 — Enajenación de activos no financieros no producidos.
- 2.4 — Títulos de deuda suscriptos en el exterior y endeudamientos financieros con el exterior.
- 2.5 — Títulos de deuda u otros valores representativos de deuda denominados y pagaderos en moneda extranjera en el país.
- 2.6 — Excepción de liquidación de cobros de exportaciones de bienes y servicios para los beneficiarios del "Régimen de fomento para las exportaciones de la economía del conocimiento”.
- 2.7 — Otras excepciones a la obligación de liquidación.
- 2.8 — Canjes y arbitrajes con clientes asociados a ingresos de divisas del exterior.
- 2.9 — Operaciones comprendidas en el artículo 3° del Decreto 616/05.
- 3.1 — Pagos de importaciones y otras compras de bienes al exterior.
- 3.2 — Pagos de servicios prestados por no residentes.
- 3.3 — Pagos de intereses de deudas por importaciones de bienes y servicios.
- 3.4 — Pagos de utilidades y dividendos.
- 3.5 — Pagos de títulos de deuda suscriptos en el exterior y endeudamientos financieros con el exterior.
- 3.6 — Pagos de títulos de deuda u otros valores representativos de deuda denominados y pagaderos en moneda extranjera en el país y obligaciones en moneda extranjera entre residentes.
- 3.7 — Pagos de endeudamientos en moneda extranjera de residentes por parte de fideicomisos constituidos en el país para garantizar la atención de los servicios.
- 3.11 — Otras compras de moneda extranjera por parte de residentes con aplicación específica.
- 3.12 — Compra de moneda extranjera para operaciones con derivados financieros.
- 3.13 — Repatriaciones de inversiones directas y otras compras de moneda extranjera por parte de no residentes.
- 3.14 — Canjes y arbitrajes con clientes no asociados a ingresos de divisas del exterior.
- 3.15 — Cancelación por parte de entidades financieras de líneas de crédito del exterior aplicadas a la financiación de operaciones de comercio exterior y garantías financieras otorgadas.
- 3.16 — Requisitos complementarios para los egresos por el mercado de cambios.
- 3.17 — Acceso con “Certificación por los regímenes de acceso a divisas para la producción incremental de petróleo y/o gas natural (Decreto 277/22)”.
- 3.18 — Acceso con “Certificación de aumento de las exportaciones de bienes”.
- 4.1 — Operaciones con débito en una cuenta en una entidad financiera local y/o con tarjetas de crédito, compra y prepagas emitidas en el país.
- 4.2 — Operaciones cursadas a través del Sistema de Monedas Locales (SML).
- 4.3 — Operaciones con títulos valores.
- 4.4 — Suscripción de bonos BOPREAL por parte de deudores de importaciones de bienes con registro de ingreso aduanero hasta el 12/12/23.
- 4.5 — Suscripción de bonos BOPREAL por parte de deudores de servicios de no residentes prestados o devengados hasta el 12/12/23.
- 4.6 — Suscripción de bonos BOPREAL por utilidades y dividendos de accionistas no residentes pendientes de pago o ya percibidas en el país.
- 4.7 — Suscripción de bonos BOPREAL por parte de deudores de capital e intereses vencidos con contrapartes vinculadas sujetos a la conformidad previa del BCRA prevista en los puntos 3.3.3. y 3.5.6.
- 4.8 — Disposiciones complementarias asociadas a los Bonos para la Reconstrucción de una Argentina Libre (BOPREAL).
- 5.1 — Horario de funcionamiento del mercado de cambios.
- 5.2 — Tipo de cambo minorista.
- 5.3 — Boletos de cambio.
- 5.4 — Identificación del cliente.
- 5.5 — Información mínima en las transferencias de fondos desde y hacia el exterior.
- 5.6 — Notificación al cliente de acreditación de fondos en cuentas de corresponsalía.
- 5.7 — Registro de las operaciones con clientes ante el BCRA.
- 5.8 — Boletos globales diarios.
- 5.9 — Posición general de cambios y tenencias en moneda extranjera de las entidades.
- 5.10 — Operaciones propias de las entidades.
- 5.11 — Operaciones de cambio entre entidades.
- 5.12 — Operaciones de arbitrajes y canjes en el exterior de las entidades.
- 5.13 — Operaciones que impliquen importación y/o exportación de moneda nacional.
- 5.14 — Liquidación de financiaciones en moneda extranjera otorgadas por entidades financieras locales.
- 5.15 — Suspensión de operaciones por incumplimiento en el registro ante el BCRA.
- 6.1 — Instrumentos operados en el mercado de cambios.
- 6.2 — Tipo de operaciones cursadas en el mercado de cambios.
- 6.3 — Operaciones al contado.
- 6.4 — Operaciones a término.
- 6.5 — Residente.
- 6.6 — Operaciones con contrapartes vinculadas.
- 6.7 — Posición general de cambios (PGC).
- 6.8 — Servicios.
- 6.9 — Rentas (ingreso primario).
- 6.10 — Transferencias corrientes (ingreso secundario).
- 6.11 — Activos no financieros no producidos.
- 6.12 — Gobiernos locales.
- 7.1 — Obligación de ingreso y liquidación en los plazos establecidos.
- 7.2 — Liquidaciones y otros ingresos imputables al cumplimiento de un permiso de embarque.
- 7.3 — Aplicación de divisas de cobros de exportaciones.
- 7.4 — Otras imputaciones admitidas en el cumplimiento de la obligación de ingreso y liquidación.
- 7.5 — Ampliaciones del plazo para el ingreso y liquidación de divisas.
- 7.6 — Incumplidos en gestión de cobro.
- 7.7 — Cancelación de anticipos u otras financiaciones de exportación sin aplicación de divisas por cobros de exportaciones de bienes.
- 7.8 — Otras disposiciones.
- 7.9 — Operaciones financieras habilitadas para aplicar cobros de exportaciones de bienes y servicios.
- 7.10 — Operaciones habilitadas para la aplicación de cobros de exportaciones de bienes en el marco del régimen de fomento de inversión para las exportaciones (Decreto 234/21).
- 7.11 — Financiaciones asociadas a importaciones de bienes habilitadas para la aplicación de cobros de exportaciones de bienes.
- 8.1 — Operaciones comprendidas.
- 8.2 — Entidad nominada por el exportador.
- 8.3 — Información de las destinaciones de exportación a disposición de las entidades.
- 8.5 — Otras imputaciones admitidas en el cumplimiento del seguimiento.
- 8.6 — Reportes de las entidades en el seguimiento.
- 9.1 — Operaciones comprendidas.
- 9.4 — Fecha de aplicación de divisas.
- 9.5 — Datos mínimos que conforman la certificación.
- 9.6 — Otras circunstancias que reduzcan el monto pendiente de aplicación.
- 9.7 — Operaciones cursadas por el Sistema de Monedas Locales (SML).
- 9.8 — Cumplimiento del régimen informativo del BCRA.
- 10.1 — Disposiciones generales.
- 10.2 — Definiciones.
- 10.3 — Pagos de importaciones de bienes que cuentan con registro de ingreso aduanero.
- 10.4 — Pagos de importaciones de bienes con registro de ingreso aduanero pendiente.
- 10.5 — Seguimiento de pagos de importaciones con registro de ingreso aduanero pendiente.
- 10.6 — Otras disposiciones.
- 10.7 — Líneas de crédito de entidades financieras aplicadas a la financiación de importaciones.
- 10.8 — Cancelación al exterior de deudas originadas en la importación argentina de bienes que no encuadran como deudas comerciales.
- 10.9 — Otras compras de bienes al exterior.
- 10.10 — Disposiciones complementarias para importaciones de bienes que tuvieron o tendrán registro de ingreso aduanero a partir del 13/12/23.
- 10.11 — Disposiciones complementarias para importaciones de bienes con registro de ingreso aduanero hasta el 12/12/23.
- 11.2 — Seguimiento de pagos de importaciones realizados con anterioridad al registro de ingreso aduanero.
- 13.1 — Disposiciones generales.
- 13.2 — Pagos de servicios que fueron o serán prestados o devengados a partir del 13/12/23.
- 13.3 — Pagos de servicios que fueron o serán prestados o devengados a partir del 13/12/23 con anterioridad a lo previsto en los puntos 13.2.3. a 13.2.7.
- 13.4 — Pagos de servicios de no residentes prestados o devengados hasta el 12/12/23.
- 13.5 — Cancelación de cartas de crédito o letras avaladas emitidas u otorgadas por entidades financieras para garantizar importaciones de servicios.
- 13.6 — Líneas de crédito de entidades financieras aplicadas a la financiación de importaciones de servicios.
- 14.1 — Beneficios relacionados con el ingreso y/o liquidación de cobros de exportaciones de bienes y servicios.
- 14.2 — Beneficios relacionados con el acceso al mercado de cambios para operaciones de egreso.
- 14.3 — Otros beneficios.
- 14.4 — Requisito complementario para egresos para un VPU que prevé hacer uso de los beneficios en materia de cobros de exportaciones de bienes y servicios.
- 14.5 — Otras disposiciones.
- 14.6 — Estabilidad cambiaria.
- 15.1 — Artículos 1° y 2° del Decreto 260/02.
- 15.2 — Artículos 1°, 2° y 3° del Decreto 609/19.

## Capitales Mínimos (`TO_capitales_minimos_actual.pdf`) — 5 preguntas — 42 unidades

- 1.4 — Incumplimientos.
- 2.2 — Exclusiones.
- 2.3 — Cómputo de los conceptos comprendidos.
- 2.4 — Requisitos de debida diligencia.
- 2.5 — Criterios para la determinación de los activos ponderados por riesgo.
- 2.6 — Exposiciones a entidades financieras.
- 2.7 — Exposiciones a empresas.
- 2.8 — Exposiciones minoristas.
- 2.9 — Exposiciones con garantía hipotecaria.
- 2.10 — Exposiciones en situación de incumplimiento.
- 2.11 — Exposiciones a instrumentos.
- 2.12 — Tabla de ponderadores de riesgo.
- 2.13 — Partidas fuera de balance. Factores de conversión crediticia (CCF).
- 3.1 — Tratamiento de las titulizaciones.
- 3.2 — Tratamiento de las posiciones en fondos.
- 4.1 — Exigencia de capital por riesgo de crédito de contraparte para operaciones DvP fallidas y no DvP.
- 4.2 — Exigencia de capital por riesgo de crédito de contraparte en operaciones con de- rivados –OTC o negociados en mercados regulados– y con liquidación diferida.
- 4.3 — Exigencia de capital por riesgo de crédito de contraparte en operaciones con en- tidades de contraparte central.
- 5.2 — Requisitos para la aplicación de técnicas de coberturas del riesgo de crédito.
- 5.3 — Operaciones cubiertas con activos admitidos como garantía.
- 5.4 — Operaciones cubiertas con garantías (y contragarantías) personales y derivados de crédito.
- 6.2 — Exigencia de capital por riesgo de tasa de interés.
- 6.3 — Exigencia de capital por riesgo de posiciones en acciones.
- 6.4 — Exigencia de capital por riesgo de tipo de cambio.
- 6.5 — Exigencia de capital por riesgo de posiciones en productos básicos –commodities–.
- 6.6 — Exigencia de capital por riesgo de posiciones en opciones.
- 6.8 — Políticas y procedimientos para la gestión de la cartera de negociación.
- 6.9 — Requisitos adicionales para incluir posiciones en la cartera de negociación.
- 6.10 — Tratamiento para las posiciones de menor liquidez.
- 6.11 — Responsabilidades.
- 6.12 — Auditoría interna.
- 8.1 — Determinación.
- 8.2 — Conceptos computables.
- 8.3 — Criterios relacionados con los conceptos computables.
- 8.4 — Conceptos deducibles.
- 8.5 — Límites.
- 8.6 — Aportes de capital.
- 8.7 — Procedimiento.
- 9.1 — Base individual.
- S10 — Agentes de calificación externa (ECAI). (sección sin puntos en índice)
- S11 — Otras disposiciones. (sección sin puntos en índice)
- S12 — Disposiciones transitorias. (sección sin puntos en índice)

## Clasificación de Deudores (`TO_clasificacion_deudores_actual.pdf`) — 4 preguntas — 21 unidades

- 2.1 — Conceptos incluidos.
- 2.2 — Exclusiones.
- 3.1 — Procedimientos de análisis de cartera.
- 3.2 — Periodicidad de clasificación.
- 3.3 — Manual de procedimientos de clasificación y previsión.
- 3.4 — Legajo del cliente.
- 3.5 — Responsabilidad de la tarea de clasificación.
- 3.6 — Aprobación de la clasificación.
- 4.1 — Niveles de clasificación.
- 4.2 — Criterio básico de clasificación.
- 4.3 — Evaluación de la capacidad de pago.
- 4.6 — Financiaciones –sin responsabilidad para el cedente– amparadas con seguros de crédito por riesgo comercial y con seguros de riesgo de crédito “con alcance de comprador público”.
- 5.1 — Categorías.
- 6.1 — Información básica.
- 6.3 — Periodicidad mínima de clasificación.
- 7.2 — Niveles de clasificación.
- 7.4 — Información a la Superintendencia de Entidades Financieras y Cambiarias sobre incrementos de la cartera irregular.
- 9.1 — Base individual.
- 10.2 — Fiduciarios de fideicomisos financieros comprendidos en la Ley de Entidades Fi- nancieras.
- 10.3 — Sociedades de garantía recíproca y fondos de garantía de carácter público.
- 10.4 — Proveedores de servicios de créditos entre particulares a través de plataformas.

## Régimen Informativo Contable Mensual (R.I.-C.M.) (`TO_regimen_informativo_contable_mensual_actual.pdf`) — 3 preguntas — 14 unidades

- S1 — Instrucciones generales (sección sin puntos en índice)
- 3.1 — Normas de procedimiento
- 3.2 — Modelo de información
- 4.1 — Normas de procedimiento
- 4.2 — Modelo de información
- 5.1 — Normas de procedimiento
- 5.2 — Modelo de información
- 6.1 — Normas de procedimiento
- 6.2 — Modelos de información
- 7.2 — Modelo de información
- 9.1 — Normas de procedimiento
- 9.2 — Modelo de información
- 11.2 — Modelos de información.
- S12 — Disposiciones transitorias. (sección sin puntos en índice)

## Protección de Usuarios (`TO_proteccion_usuarios_servicios_financieros_actual.pdf`) — 3 preguntas — 13 unidades

- 1.3 — Encuadre y alcance normativo.
- 2.1 — Concepto.
- 2.2 — Casos especiales.
- 2.4 — Publicidad de la información.
- 2.5 — Información al Banco Central de la República Argentina.
- 2.6 — Trato digno.
- 2.7 — Revocación de la aceptación y rescisión de relaciones contractuales.
- 3.1 — Requisitos mínimos.
- 3.2 — Controles.
- 4.1 — Consultas, sugerencias y quejas.
- 4.2 — Reclamos no respondidos o con respuestas insatisfactorias.
- 4.3 — Actuación en defensa del interés general de los usuarios.
- 4.4 — Actuaciones de oficio.
