# Mapa de territorio quemado / disponible — 5 TOs del corpus

Unidad de lectura, 2026-08-03. Universo de referencia: el corpus (`data/experiment/subset/`), extraído con `pdftotext -layout`; NO el grafo.

**Regla laudada aplicada**: territorio quemado = el punto normativo exacto que cada pregunta quemada ancló (con sus subpuntos), no la sección entera. Unidad de conteo: punto x.y del índice del TO; una sección cuyo índice no lista puntos cuenta como una unidad (S<n>). Un ancla más profunda que x.y quema SOLO ese subpunto (y sus hijos): la unidad x.y queda *parcialmente quemada* y su resto sigue disponible.

## Sets quemados (M1)

| Set | Archivo | Preguntas |
|---|---|---|
| EV1 | `data/experiment/evaluacion_escalon1/EV1_preguntas.json` | 36 |
| CQ | `data/experiment/evaluacion/queries/eval_set_v2.json` (v1 ⊂ v2: 23 + 8 nuevas) | 31 |
| CQN | `data/experiment/evaluacion/queries/eval_set_cqn.json` | 15 |
| CQN2 | `data/experiment/evaluacion/queries/eval_set_cqn2.json` | 15 |

Total: 97 preguntas; 93 anclan territorio; sin ancla (unanswerable by design): CQ-036, CQ-037, CQ-038, CQ-039.

## Conteos (M4)

| TO | Unidades | Quemadas enteras | Parcialmente quemadas | Disponibles | % tocado | % quemado entero |
|---|---|---|---|---|---|---|
| Capitales Mínimos | 54 | 12 | 11 | 31 | 42.6% | 22.2% |
| Clasificación de Deudores | 35 | 14 | 5 | 16 | 54.3% | 40.0% |
| Exterior y Cambios | 116 | 8 | 8 | 100 | 13.8% | 6.9% |
| Protección de Usuarios | 17 | 4 | 3 | 10 | 41.2% | 23.5% |
| Régimen Informativo Contable Mensual (R.I.-C.M.) | 24 | 10 | 4 | 10 | 58.3% | 41.7% |
| **Total** | **246** | **48** | **31** | **167** | **32.1%** | **19.5%** |

«% tocado» = (quemadas enteras + parciales) / unidades; «% quemado entero» excluye las parciales, cuyo resto no anclado sigue disponible.

## Capitales Mínimos — `TO_capitales_minimos_actual.pdf`

### Quemadas enteras (12)

| Unidad | Título | Quemada por |
|---|---|---|
| 1.1 | Exigencia. | CQN:CQN-012 |
| 1.2 | Exigencia básica. | CQ:CQ-010, CQN:CQN-009 |
| 1.3 | Integración. | CQN:CQN-015 |
| 2.1 | Exigencia. | CQ:CQ-020, CQ:CQ-041, CQ:CQ-044 |
| 5.1 | Técnicas de cobertura del riesgo de crédito. | CQN:CQN-002 — además anclas internas: 5.1.1 (CQN2:CQN2-001) |
| 6.1 | Exigencia. | CQN2:CQN2-004 |
| 6.7 | Cómputo. | CQN:CQN-015 |
| 7.1 | Exigencia de capital por riesgo operacional para entidades del grupo 1. | CQ:CQ-043 |
| 7.2 | Exigencia de capital por riesgo operacional para entidades del grupo 2. | CQN:CQN-014 |
| 7.3 | Límite para las entidades del grupo 2. | CQ:CQ-033, CQN:CQN-014 — además anclas internas: 7.3.1 (EV1:EV1-033); 7.3.2 (EV1:EV1-033) |
| 7.4 | Nuevas entidades. | CQN:CQN-012 |
| 9.2 | Base consolidada. | CQN2:CQN2-008 |

### Parcialmente quemadas (11) — solo el subpunto listado (con sus hijos) está quemado

| Unidad | Título | Subpuntos quemados (por) |
|---|---|---|
| 1.4 | Incumplimientos. | 1.4.1 (EV1:EV1-030) |
| 2.3 | Cómputo de los conceptos comprendidos. | 2.3.1 (CQ:CQ-019) |
| 2.5 | Criterios para la determinación de los activos ponderados por riesgo. | 2.5.4 (CQN2:CQN2-015) |
| 2.8 | Exposiciones minoristas. | 2.8.3.3 (EV1:EV1-031) |
| 2.9 | Exposiciones con garantía hipotecaria. | 2.9.1 (EV1:EV1-036); 2.9.2.1 (EV1:EV1-036); 2.9.2.2 (EV1:EV1-035) |
| 2.12 | Tabla de ponderadores de riesgo. | 2.12.2.2 (CQN2:CQN2-015); 2.12.2.3 (CQN2:CQN2-015) |
| 4.1 | Exigencia de capital por riesgo de crédito de contraparte para operaciones DvP fallidas y no DvP. | 4.1.1 (EV1:EV1-032) |
| 8.2 | Conceptos computables. | 8.2.1 (EV1:EV1-034); 8.2.3.3 (CQ:CQ-040) |
| S10 | Agentes de calificación externa (ECAI). (sección sin puntos en índice) | 10.2.2.1 (CQN2:CQN2-007) |
| S11 | Otras disposiciones. (sección sin puntos en índice) | 11.2 (CQN2:CQN2-012) |
| S12 | Disposiciones transitorias. (sección sin puntos en índice) | 12.1 (CQN2:CQN2-011) |

### Disponibles (31)

- 2.2 — Exclusiones.
- 2.4 — Requisitos de debida diligencia.
- 2.6 — Exposiciones a entidades financieras.
- 2.7 — Exposiciones a empresas.
- 2.10 — Exposiciones en situación de incumplimiento.
- 2.11 — Exposiciones a instrumentos.
- 2.13 — Partidas fuera de balance. Factores de conversión crediticia (CCF).
- 3.1 — Tratamiento de las titulizaciones.
- 3.2 — Tratamiento de las posiciones en fondos.
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
- 8.3 — Criterios relacionados con los conceptos computables.
- 8.4 — Conceptos deducibles.
- 8.5 — Límites.
- 8.6 — Aportes de capital.
- 8.7 — Procedimiento.
- 9.1 — Base individual.

## Clasificación de Deudores — `TO_clasificacion_deudores_actual.pdf`

### Quemadas enteras (14)

| Unidad | Título | Quemada por |
|---|---|---|
| 1.1 | Criterio general. | EV1:EV1-015 |
| 1.2 | Criterios especiales de imputación. | CQN:CQN-003 |
| 3.7 | Importe de referencia. | CQ:CQ-042, EV1:EV1-013 |
| 4.4 | Financiaciones cubiertas con garantías preferidas “A”. | CQ:CQ-031, CQ:CQ-040 |
| 4.5 | Deudores que no deben ser objeto de clasificación. | CQ:CQ-031, CQ:CQ-040 |
| 6.2 | Criterio de clasificación. | CQN:CQN-004 |
| 6.4 | Reconsideración obligatoria de la clasificación. | CQ:CQ-024 — además anclas internas: 6.4.4 (CQ:CQ-047) |
| 6.5 | Niveles de clasificación. | EV1:EV1-011 — además anclas internas: 6.5.1 (CQ:CQ-019, EV1:EV1-011); 6.5.2 (EV1:EV1-011); 6.5.3 (EV1:EV1-011); 6.5.4 (EV1:EV1-011); 6.5.5 (EV1:EV1-011) |
| 6.6 | Recategorización obligatoria. | CQ:CQ-047 |
| 7.1 | Criterio de clasificación. | CQN2:CQN2-014 |
| 7.3 | Recategorización obligatoria. | EV1:EV1-014 |
| 8.1 | Informaciones a suministrar. | CQ:CQ-008, EV1:EV1-009 |
| 9.2 | Base consolidada. | CQN2:CQN2-002 |
| 10.1 | Proveedores no financieros de crédito. | CQ:CQ-018, CQN:CQN-008, EV1:EV1-014 |

### Parcialmente quemadas (5) — solo el subpunto listado (con sus hijos) está quemado

| Unidad | Título | Subpuntos quemados (por) |
|---|---|---|
| 2.2 | Exclusiones. | 2.2.1 (EV1:EV1-012) |
| 3.4 | Legajo del cliente. | 3.4.2 (CQ:CQ-021, EV1:EV1-008) |
| 5.1 | Categorías. | 5.1.1.1 (CQ:CQ-042, EV1:EV1-013); 5.1.1.2 (CQ:CQ-042); 5.1.2.4 (CQ:CQ-042) |
| 6.3 | Periodicidad mínima de clasificación. | 6.3.1 (CQ:CQ-024, CQN2:CQN2-010) |
| 7.2 | Niveles de clasificación. | 7.2.1 (CQ:CQ-006, CQ:CQ-019, EV1:EV1-010) |

### Disponibles (16)

- 2.1 — Conceptos incluidos.
- 3.1 — Procedimientos de análisis de cartera.
- 3.2 — Periodicidad de clasificación.
- 3.3 — Manual de procedimientos de clasificación y previsión.
- 3.5 — Responsabilidad de la tarea de clasificación.
- 3.6 — Aprobación de la clasificación.
- 4.1 — Niveles de clasificación.
- 4.2 — Criterio básico de clasificación.
- 4.3 — Evaluación de la capacidad de pago.
- 4.6 — Financiaciones –sin responsabilidad para el cedente– amparadas con seguros de crédito por riesgo comercial y con seguros de riesgo de crédito “con alcance de comprador público”.
- 6.1 — Información básica.
- 7.4 — Información a la Superintendencia de Entidades Financieras y Cambiarias sobre incrementos de la cartera irregular.
- 9.1 — Base individual.
- 10.2 — Fiduciarios de fideicomisos financieros comprendidos en la Ley de Entidades Fi- nancieras.
- 10.3 — Sociedades de garantía recíproca y fondos de garantía de carácter público.
- 10.4 — Proveedores de servicios de créditos entre particulares a través de plataformas.

## Exterior y Cambios — `TO_exterior_cambios_actual.pdf`

### Quemadas enteras (8)

| Unidad | Título | Quemada por |
|---|---|---|
| 3.8 | Compra de moneda extranjera por parte de personas humanas residentes para la formación de activos externos en forma de billetes y/o depósitos. | CQ:CQ-034 |
| 3.9 | Compra de moneda extranjera por parte de personas humanas residentes para la formación de activos externos bajo otras modalidades, la remisión de ayuda familiar u operaciones con derivados. | CQ:CQ-034, CQN:CQN-001 |
| 3.10 | Compra de moneda extranjera por parte de otros residentes –excluidas las entidades– para la formación de activos externos y por operaciones con derivados. | EV1:EV1-022 |
| 8.4 | Responsabilidades de la entidad nominada para el seguimiento del permiso. | CQN:CQN-010 |
| 9.2 | Entidad nominada por el exportador. | CQN:CQN-010 |
| 9.3 | Certificaciones de aplicación de cobros de exportaciones. | CQN:CQN-005 — además anclas internas: 9.3.2 (CQN2:CQN2-009) |
| 11.1 | Seguimiento de oficializaciones de importación. | CQN2:CQN2-005 |
| 12.1 | Posiciones arancelarias referidas en los puntos 10.10.2.1. y 10.10.2.2. | CQN2:CQN2-011 |

### Parcialmente quemadas (8) — solo el subpunto listado (con sus hijos) está quemado

| Unidad | Título | Subpuntos quemados (por) |
|---|---|---|
| S1 | Disposiciones generales. (sección sin puntos en índice) | 1.1 (CQ:CQ-017) |
| 2.2 | Cobros de exportaciones de servicios. | 2.2.1 (CQ:CQ-014, EV1:EV1-021); 2.2.2 (EV1:EV1-017); 2.2.2.1 (EV1:EV1-016); 2.2.2.3 (EV1:EV1-017) |
| 4.1 | Operaciones con débito en una cuenta en una entidad financiera local y/o con tarjetas de crédito, compra y prepagas emitidas en el país. | 4.1.1 (EV1:EV1-019); 4.1.4 (EV1:EV1-018) |
| 6.5 | Residente. | 6.5.1 (CQ:CQ-015) |
| 7.1 | Obligación de ingreso y liquidación en los plazos establecidos. | 7.1.1.4 (EV1:EV1-020); 7.1.1.5 (EV1:EV1-020) |
| 10.10 | Disposiciones complementarias para importaciones de bienes que tuvieron o tendrán registro de ingreso aduanero a partir del 13/12/23. | 10.10.2.1 (CQN2:CQN2-011) |
| 13.2 | Pagos de servicios que fueron o serán prestados o devengados a partir del 13/12/23. | 13.2.7.1 (CQN2:CQN2-013) |
| 14.1 | Beneficios relacionados con el ingreso y/o liquidación de cobros de exportaciones de bienes y servicios. | 14.1.3 (EV1:EV1-021) |

### Disponibles (100)

- 2.1 — Cobros de exportaciones de bienes.
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
- 6.6 — Operaciones con contrapartes vinculadas.
- 6.7 — Posición general de cambios (PGC).
- 6.8 — Servicios.
- 6.9 — Rentas (ingreso primario).
- 6.10 — Transferencias corrientes (ingreso secundario).
- 6.11 — Activos no financieros no producidos.
- 6.12 — Gobiernos locales.
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
- 10.11 — Disposiciones complementarias para importaciones de bienes con registro de ingreso aduanero hasta el 12/12/23.
- 11.2 — Seguimiento de pagos de importaciones realizados con anterioridad al registro de ingreso aduanero.
- 13.1 — Disposiciones generales.
- 13.3 — Pagos de servicios que fueron o serán prestados o devengados a partir del 13/12/23 con anterioridad a lo previsto en los puntos 13.2.3. a 13.2.7.
- 13.4 — Pagos de servicios de no residentes prestados o devengados hasta el 12/12/23.
- 13.5 — Cancelación de cartas de crédito o letras avaladas emitidas u otorgadas por entidades financieras para garantizar importaciones de servicios.
- 13.6 — Líneas de crédito de entidades financieras aplicadas a la financiación de importaciones de servicios.
- 14.2 — Beneficios relacionados con el acceso al mercado de cambios para operaciones de egreso.
- 14.3 — Otros beneficios.
- 14.4 — Requisito complementario para egresos para un VPU que prevé hacer uso de los beneficios en materia de cobros de exportaciones de bienes y servicios.
- 14.5 — Otras disposiciones.
- 14.6 — Estabilidad cambiaria.
- 15.1 — Artículos 1° y 2° del Decreto 260/02.
- 15.2 — Artículos 1°, 2° y 3° del Decreto 609/19.

## Protección de Usuarios — `TO_proteccion_usuarios_servicios_financieros_actual.pdf`

### Quemadas enteras (4)

| Unidad | Título | Quemada por |
|---|---|---|
| 1.1 | Partes. | CQN:CQN-008 — además anclas internas: 1.1.1 (CQN2:CQN2-010, EV1:EV1-029); 1.1.2.2 (CQ:CQ-017); 1.1.2.3 (CQN2:CQN2-010); 1.1.2.4 (CQ:CQ-018); 1.1.2.5 (CQ:CQ-018, EV1:EV1-028) |
| 1.2 | Criterio general y supervisión. | CQN:CQN-013 |
| 2.3 | Recaudos mínimos de la relación de consumo. | CQN:CQN-006 — además anclas internas: 2.3.1.1 (CQ:CQ-002); 2.3.2.1 (CQ:CQ-028, EV1:EV1-023); 2.3.4 (CQ:CQ-046); 2.3.5 (CQ:CQ-045); 2.3.5.1 (CQ:CQ-045, EV1:EV1-027); 2.3.9 (EV1:EV1-025) |
| S5 | Sanciones. (sección sin puntos en índice) | CQN:CQN-013 (Sección 5 entera) |

### Parcialmente quemadas (3) — solo el subpunto listado (con sus hijos) está quemado

| Unidad | Título | Subpuntos quemados (por) |
|---|---|---|
| 2.2 | Casos especiales. | 2.2.2 (EV1:EV1-024) |
| 3.1 | Requisitos mínimos. | 3.1.1.1 (EV1:EV1-029); 3.1.3 (CQN2:CQN2-003); 3.1.6 (CQ:CQ-004, EV1:EV1-027) |
| 4.2 | Reclamos no respondidos o con respuestas insatisfactorias. | 4.2.1 (EV1:EV1-026); 4.2.1.1 (EV1:EV1-026); 4.2.1.2 (EV1:EV1-026); 4.2.1.3 (EV1:EV1-026); 4.2.1.4 (EV1:EV1-026); 4.2.1.5 (EV1:EV1-026); 4.2.1.6 (EV1:EV1-026) |

### Disponibles (10)

- 1.3 — Encuadre y alcance normativo.
- 2.1 — Concepto.
- 2.4 — Publicidad de la información.
- 2.5 — Información al Banco Central de la República Argentina.
- 2.6 — Trato digno.
- 2.7 — Revocación de la aceptación y rescisión de relaciones contractuales.
- 3.2 — Controles.
- 4.1 — Consultas, sugerencias y quejas.
- 4.3 — Actuación en defensa del interés general de los usuarios.
- 4.4 — Actuaciones de oficio.

## Régimen Informativo Contable Mensual (R.I.-C.M.) — `TO_regimen_informativo_contable_mensual_actual.pdf`

### Quemadas enteras (10)

| Unidad | Título | Quemada por |
|---|---|---|
| S2 | Entidades comprendidas (sección sin puntos en índice) | CQN:CQN-011 (Sección 2 entera), EV1:EV1-001 (Sección 2 entera) |
| 4.3 | Información complementaria vinculada al cálculo de la exigencia por riesgo de mercado - Normas de procedimiento [no listado en índice] | CQ:CQ-025 — además anclas internas: 4.3.2 (EV1:EV1-002); 4.3.3 (EV1:EV1-006) |
| 4.4 | Información complementaria vinculada al cálculo de la exigencia por riesgo de mercado - Modelos de información [no listado en índice] | CQ:CQ-025 — además anclas internas: 4.4.3 (EV1:EV1-002) |
| 4.5 | Información sobre instrumentos derivados [no listado en índice] | CQ:CQ-025 |
| 7.1 | Normas de procedimiento | EV1:EV1-005 |
| 8.1 | Normas de procedimiento | CQN:CQN-007, CQN:CQN-009 — además anclas internas: 8.1.6 (CQN2:CQN2-012) |
| 8.2 | Modelo de información | EV1:EV1-003 |
| 10.1 | Normas de procedimiento. | CQ:CQ-025 (Sección 10 entera) |
| 10.2 | Modelo de información. | CQ:CQ-025 (Sección 10 entera) |
| 11.1 | Normas de procedimiento. | CQN:CQN-011 |

### Parcialmente quemadas (4) — solo el subpunto listado (con sus hijos) está quemado

| Unidad | Título | Subpuntos quemados (por) |
|---|---|---|
| S1 | Instrucciones generales (sección sin puntos en índice) | 1.1 (CQ:CQ-020, CQ:CQ-025); 1.2 (CQ:CQ-016) |
| 3.1 | Normas de procedimiento | 3.1.2 (CQ:CQ-020, CQN2:CQN2-013) |
| 5.1 | Normas de procedimiento | 5.1.1 (CQ:CQ-043, CQN2:CQN2-006); 5.1.3.1 (EV1:EV1-007); 5.1.3.2 (EV1:EV1-007) |
| 9.1 | Normas de procedimiento | 9.1.1 (CQ:CQ-041, EV1:EV1-004) |

### Disponibles (10)

- 3.2 — Modelo de información
- 4.1 — Normas de procedimiento
- 4.2 — Modelo de información
- 5.2 — Modelo de información
- 6.1 — Normas de procedimiento
- 6.2 — Modelos de información
- 7.2 — Modelo de información
- 9.2 — Modelo de información
- 11.2 — Modelos de información.
- S12 — Disposiciones transitorias. (sección sin puntos en índice)

## Anclaje por pregunta (M2) — qid → TO → puntos

Estados: todas `declarado` salvo las 4 `sin_ancla` (unanswerable). CQN2-010: asignación de puntos a TO tomada de `seccion_sorteada_origen` (CLA-S6 + PRO-S1). `S<n>` = sección entera declarada como ancla por el propio set.

- CQ-002: pro: 2.3.1.1
- CQ-004: pro: 3.1.6
- CQ-006: cla: 7.2.1
- CQ-008: cla: 8.1
- CQ-010: cap: 1.2
- CQ-014: ext: 2.2.1
- CQ-015: ext: 6.5.1
- CQ-016: ric: 1.2
- CQ-017: pro: 1.1.2.2; ext: 1.1
- CQ-018: pro: 1.1.2.4, 1.1.2.5; cla: 10.1
- CQ-019: cap: 2.3.1; cla: 6.5.1, 7.2.1
- CQ-020: cap: 2.1; ric: 3.1.2, 1.1
- CQ-021: cla: 3.4.2
- CQ-024: cla: 6.3.1, 6.4
- CQ-025: ric: 1.1, 4.3, 4.4, 4.5, S10
- CQ-028: pro: 2.3.2.1
- CQ-031: cla: 4.5, 4.4
- CQ-033: cap: 7.3
- CQ-034: ext: 3.8, 3.9
- CQ-036: sin_ancla (unanswerable by design: no ancla punto normativo)
- CQ-037: sin_ancla (unanswerable by design: no ancla punto normativo)
- CQ-038: sin_ancla (unanswerable by design: no ancla punto normativo)
- CQ-039: sin_ancla (unanswerable by design: no ancla punto normativo)
- CQ-040: cla: 4.4, 4.5; cap: 8.2.3.3
- CQ-041: cap: 2.1; ric: 9.1.1
- CQ-042: cla: 3.7, 5.1.1.1, 5.1.1.2, 5.1.2.4
- CQ-043: cap: 7.1; ric: 5.1.1
- CQ-044: cap: 2.1
- CQ-045: pro: 2.3.5, 2.3.5.1
- CQ-046: pro: 2.3.4
- CQ-047: cla: 6.6, 6.4.4
- CQN-001: ext: 3.9
- CQN-002: cap: 5.1
- CQN-003: cla: 1.2
- CQN-004: cla: 6.2
- CQN-005: ext: 9.3
- CQN-006: pro: 2.3
- CQN-007: ric: 8.1
- CQN-008: pro: 1.1; cla: 10.1
- CQN-009: ric: 8.1; cap: 1.2
- CQN-010: ext: 8.4, 9.2
- CQN-011: ric: 11.1, S2
- CQN-012: cap: 1.1, 7.4
- CQN-013: pro: 1.2, S5
- CQN-014: cap: 7.2, 7.3
- CQN-015: cap: 1.3, 6.7
- CQN2-001: cap: 5.1.1
- CQN2-002: cla: 9.2
- CQN2-003: pro: 3.1.3
- CQN2-004: cap: 6.1
- CQN2-005: ext: 11.1
- CQN2-006: ric: 5.1.1
- CQN2-007: cap: 10.2.2.1
- CQN2-008: cap: 9.2
- CQN2-009: ext: 9.3.2
- CQN2-010: pro: 1.1.2.3, 1.1.1; cla: 6.3.1
- CQN2-011: cap: 12.1; ext: 12.1, 10.10.2.1
- CQN2-012: cap: 11.2; ric: 8.1.6
- CQN2-013: ric: 3.1.2; ext: 13.2.7.1
- CQN2-014: cla: 7.1
- CQN2-015: cap: 2.5.4, 2.12.2.2, 2.12.2.3
- EV1-001: ric: S2
- EV1-002: ric: 4.3.2, 4.4.3
- EV1-003: ric: 8.2
- EV1-004: ric: 9.1.1
- EV1-005: ric: 7.1
- EV1-006: ric: 4.3.3
- EV1-007: ric: 5.1.3.1, 5.1.3.2
- EV1-008: cla: 3.4.2
- EV1-009: cla: 8.1
- EV1-010: cla: 7.2.1
- EV1-011: cla: 6.5, 6.5.1, 6.5.2, 6.5.3, 6.5.4, 6.5.5
- EV1-012: cla: 2.2.1
- EV1-013: cla: 5.1.1.1, 3.7
- EV1-014: cla: 10.1, 7.3
- EV1-015: cla: 1.1
- EV1-016: ext: 2.2.2.1
- EV1-017: ext: 2.2.2, 2.2.2.3
- EV1-018: ext: 4.1.4
- EV1-019: ext: 4.1.1
- EV1-020: ext: 7.1.1.4, 7.1.1.5
- EV1-021: ext: 2.2.1, 14.1.3
- EV1-022: ext: 3.10
- EV1-023: pro: 2.3.2.1
- EV1-024: pro: 2.2.2
- EV1-025: pro: 2.3.9
- EV1-026: pro: 4.2.1, 4.2.1.1, 4.2.1.2, 4.2.1.3, 4.2.1.4, 4.2.1.5, 4.2.1.6
- EV1-027: pro: 3.1.6, 2.3.5.1
- EV1-028: pro: 1.1.2.5
- EV1-029: pro: 1.1.1, 3.1.1.1
- EV1-030: cap: 1.4.1
- EV1-031: cap: 2.8.3.3
- EV1-032: cap: 4.1.1
- EV1-033: cap: 7.3.1, 7.3.2
- EV1-034: cap: 8.2.1
- EV1-035: cap: 2.9.2.2
- EV1-036: cap: 2.9.1, 2.9.2.1
