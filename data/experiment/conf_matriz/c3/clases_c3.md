# U-CONF-MATRIZ, C3: sensibilidad y señales de las clases (insumo de C4)

## Sensibilidad a la lectura de las correctas con anotación

Informativa: no cambia el criterio ni las cifras de C2. Cada escenario pasa a «incorrecta» las correctas cuya anotación empieza como se indica.

| escenario | fichas | → Operacion | → Potestad |
|---|---|---|---|
| C2, sellado | — | 29/30, Wilson [0.8333, 0.9941] | 29/30, Wilson [0.8333, 0.9941] |
| circular | F27, F34 | 27/30, Wilson [0.7438, 0.9654], no cumpliría | 29/30, Wilson [0.8333, 0.9941], cumpliría |
| circular + alcance | F23, F24, F27, F34, F60 | 26/30, Wilson [0.7032, 0.9469], no cumpliría | 27/30, Wilson [0.7438, 0.9654], no cumpliría |
| circular + alcance + consecuencia fuera de la arista | F23, F24, F27, F33, F34, F45, F60 | 24/30, Wilson [0.6269, 0.9049], no cumpliría | 27/30, Wilson [0.7438, 0.9654], no cumpliría |

## Señales de código sobre la población (907 aristas), caso por caso

### circular: 22 aristas (Operacion 19, Potestad 3)

Señal: el tramo del destino, normalizado, está contenido en el de la Condicion.

| par | unidad | páginas | origen | destino | lectura |
|---|---|---|---|---|---|
| Operacion | `ext::9.3.5.1` | [126] | Acreditación de ingresos de divisas en cuenta | Cobro efectivo de divisas del embarque | sin leer |
| Operacion | `ext::8.5.20.2` | [121] | Adquisición de títulos valores con liquidación en moneda extranjera | Adquisición de títulos valores con liquidación en moneda extranjera | sin leer |
| Operacion | `ext::3.18.2.1` | [53] | Aumento FOB año t respecto a año t-1 | Exportación de bienes con certificación SECOEXPO | sin leer |
| Operacion | `ext::7.11.2.7` | [106] | Cancelación de intereses — cobros desde fecha de completitud de ingreso | Cancelación de intereses mediante cobros de exportaciones | sin leer |
| Operacion | `ext::4.8.6::intro` | [67] | Cliente con venta BOPREAL de suscripción primaria | Venta con obligación de recompra de BOPREAL | sin leer |
| Operacion | `ext::2.2.3` | [11] | Cobros ingresados por sistema de monedas locales | Ingreso de cobros por sistema de monedas locales | leída en C2 (F27, correcta) |
| Operacion | `cap::8.3.1` | [156] | Condición: acción considerada en CO | Inclusión de acción en CO | sin leer |
| Operacion | `ext::10.10.2.2` | [154, 155] | Condición: suma pagos anticipados ≤ 30% FOB | Pago anticipado importación bienes capital | sin leer |
| Operacion | `ext::2.6.2.2` | [13] | Declaración jurada del exportador | Emisión de Certificaciones de incremento de exportaciones | sin leer |
| Operacion | `ext::7.6.3.1` | [90] | Demostración de cobertura por póliza de seguro | Operación cubierta por póliza de seguro de crédito | sin leer |
| Operacion | `ext::8.5.7.3` | [114] | Entidad cuenta con certificación de afectación | Certificación de afectación — importación temporal | sin leer |
| Operacion | `ext::7.6.3.1` | [90] | Liquidación de montos por compañía de seguro | Liquidación de montos cubiertos por compañía de seguro | sin leer |
| Operacion | `ctacte::6.4.7::cierre` | [39] | Modificación necesaria de comunicaciones de rechazo | Modificación de comunicaciones de rechazo | sin leer |
| Operacion | `cap::4.2.1.2::parte2` | [68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82] | MPOR mínimo 10 días hábiles — derivados sin liquidación centralizada | Operaciones derivados sin liquidación centralizada con márgenes diarios | sin leer |
| Operacion | `cap::4.2.1.2::parte2` | [68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82] | MPOR mínimo 5 días hábiles — derivados con liquidación centralizada | Operaciones derivados con liquidación centralizada y márgenes diarios | sin leer |
| Operacion | `ext::5.8.1` | [71] | Operación corresponde a transferencia de jubilaciones | Transferencias jubilaciones y pensiones | sin leer |
| Operacion | `ext::3.3.1` | [16] | Operación declarada en Relevamiento | Declaración en Relevamiento de activos y pasivos externos | sin leer |
| Operacion | `ext::2.2.3` | [11] | Servicios a residentes paraguayos o uruguayos en moneda de destino | Ingreso de cobros servicios a residentes paraguayos o uruguayos | leída en C2 (F34, correcta) |
| Operacion | `ext::4.3.2.3` | [59] | Suscripción primaria BOPREAL elegible | Venta de bonos BOPREAL contra cable | sin leer |
| Potestad | `ext::7.5.2` | [86, 87] | Exportaciones comprendidas en Decretos 492/23, 549/23, 597/23 y 28/23 | Extensión del plazo para liquidación de divisas — exportaciones Decretos 492/23, 549/23, 597/23 y 28/23 | sin leer |
| Potestad | `ext::8.4.1` | [109] | Presentación y verificación de documentación comercial | Otorgamiento de certificación de cumplido | sin leer |
| Potestad | `cla::7.2.3` | [36, 37] | Reclasificación — deudas refinanciadas con pago periódico | Reclasificación en nivel inmediato superior — deudor refinanciado | sin leer |

### indiferencia: 7 aristas (Operacion 6, Potestad 1)

Señal: la Condicion dice «o no», «con o sin» o «indiferente».

| par | unidad | páginas | origen | destino | lectura |
|---|---|---|---|---|---|
| Operacion | `ctacte::6.5.2.3` | [40] | Condición: débito no efectuado por cuenta cerrada | Incurrencia en situación de punto 8.2.2 | sin leer |
| Operacion | `ext::4.3.2.3` | [59] | Cuenta terceros exterior no GAFI | Venta de bonos BOPREAL contra cable | sin leer |
| Operacion | `cap::2.6.2.3` | [14] | Incumplimiento requisitos regulatorios — grado C | Asignación grado C — exposiciones a entidades financieras | sin leer |
| Operacion | `cap::4.2.1.1` | [65, 66, 67, 68] | Operaciones sujetas o no a acuerdos de margen de variación | Cálculo del CR a nivel de conjunto de neteo | sin leer |
| Operacion | `pagjub::2.8.5.1` | [10] | Rendición no presentada o no aceptada | Acreditación de cuenta ANSES — rendición no presentada o no aceptada | sin leer |
| Operacion | `pagjub::2.8.5.1` | [10] | Rendición no presentada o no aceptada | Débito de cuenta corriente — rendición no presentada o no aceptada | sin leer |
| Potestad | `cla::3.3.3` | [9] | Garantías preferidas — condición indiferente | Opción de agrupar financiaciones comerciales | leída en C2 (F57, incorrecta) |

### regla de plazo: 1 aristas (Operacion 1, Potestad 0)

Señal: la Condicion dice «se regirá», «se rige», «se aplica(rá) el plazo» o «el plazo será».

| par | unidad | páginas | origen | destino | lectura |
|---|---|---|---|---|---|
| Operacion | `ext::10.4.2.4` | [139, 140] | Plazo según proporción — bienes mixtos | Acceso al mercado de cambios para pago anticipado | leída en C2 (F15, incorrecta) |

