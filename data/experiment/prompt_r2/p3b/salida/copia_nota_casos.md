# Copia de la nota de E3 en el reintento: los casos (salida_dirigida)

Regla: R-NORM, ventana de 5 tokens, en la nota y no en la unidad ni en las citas; descripción y etiqueta de cada entidad del reintento.

45 casos en 40 unidades.

| Unidad | Entidad | Campo | Ventanas en común | Texto de la entidad |
|---|---|---|---|---|
| `cla::2.2.4::intro` | e1 (Excepcion) | descripcion | sucursales locales de entidades financieras | Financiaciones y avales, fianzas y otras responsabilidades otorgados por sucursales locales de entidades financieras del exterior, por cuenta y orden de su casa |
| `cla::4.4` | e1 (Operacion) | label | evaluacion de capacidad de repago | Evaluación de capacidad de repago |
| `cla::4.4` | e2 (Definicion) | descripcion | evaluacion de capacidad de repago | Garantías que respaldan financiaciones para las que no corresponde la evaluación de capacidad de repago |
| `cla::6.3.3` | c2 (Condicion) | descripcion | cubiertos en otros puntos de; de los cubiertos en otros; distintos de los cubiertos en; en otros puntos de 6; los cubiertos en otros puntos | en los demás casos (supuestos residuales distintos de los cubiertos en otros puntos de 6.3) |
| `cla::6.5.5.8` | e2 (Condicion) | label | de puntos 3 1 3; puntos 3 1 3 2 | Cumplimiento de puntos 3.1/3.2 Evaluaciones crediticias |
| `cap::12.3` | e4 (Definicion) | label | promedio 36 meses moneda homogenea | Base de cálculo del límite: promedio 36 meses moneda homogénea |
| `cap::2.12.10::intro` | d1 (Definicion) | descripcion | la parte no deducible de | Exposiciones a instrumentos, específicamente la parte no deducible de la RPC conforme a lo previsto en la Sección 8 |
| `cap::8.3.5::intro` | e1 (Operacion) | descripcion | de terceros computables como capital; en poder de terceros computables; poder de terceros computables como | Participaciones minoritarias en subsidiarias sujetas a supervisión consolidada en poder de terceros, computables como capital emitidos por esas subsidiarias |
| `cap::8.4.1.6` | e2 (Excepcion) | label | contemplados en 8 4 1; en 8 4 1 19 | Títulos contemplados en 8.4.1.19 y 8.4.2 excluidos |
| `ext::13.2.7::cierre` | cond1 (Condicion) | label | comprendido en 13 2 1; en 13 2 1 a; no comprendido en 13 2 | Servicio no comprendido en 13.2.1 a 13.2.5 |
| `ext::13.4.1` | e2 (Condicion) | descripcion | servicios prestados o devengados hasta | servicios prestados o devengados hasta el 12/12/23 |
| `ext::13.4.1` | e2 (Condicion) | label | servicios prestados o devengados hasta | Servicios prestados o devengados hasta 12/12/23 |
| `ext::14.2.1.10` | e3 (Condicion) | descripcion | 10 3 2 que rigen; 2 que rigen el acceso; 3 2 que rigen el; que rigen el acceso al; rigen el acceso al mercado | En el marco de lo dispuesto en los puntos 3.3., 3.5., 3.6. y 10.3.2. que rigen el acceso al mercado de cambios para operaciones de egreso. |
| `ext::2.6.2.1` | e1 (Obligacion) | label | nominar unica entidad financiera local | Nominar única entidad financiera local |
| `ext::3.18.3::intro` | e3 (Operacion) | descripcion | coeficientes por tipo de bien; de coeficientes por tipo de; tabla de coeficientes por tipo | El monto máximo de las certificaciones para el exportador quedará determinado a partir de asignar coeficientes según el tipo de bien en que se registró el aumen |
| `ext::3.3.3.2` | e4 (Excepcion) | descripcion | de conformidad previa del bcra; el requisito de conformidad previa; requisito de conformidad previa del | No resultará aplicable el requisito de conformidad previa del BCRA cuando el cliente cuente con una 'Certificación de aumento de las exportaciones de bienes' pa |
| `ext::3.3.3.4` | e2 (Operacion) | descripcion | acreedor es una contraparte vinculada; cuando el acreedor es una; el acreedor es una contraparte | Pago de intereses de deudas comerciales por importaciones de bienes o servicios, cuando el acreedor es una contraparte vinculada al deudor y el vencimiento haya |
| `ext::3.3.3.4` | e3 (Excepcion) | descripcion | de conformidad previa del bcra; el requisito de conformidad previa; requisito de conformidad previa del | El requisito de conformidad previa del BCRA no resultará aplicable cuando el pago se concrete de manera simultánea con la liquidación por un importe no menor al |
| `ext::3.5.4.2` | cond1 (Condicion) | label | del requisito de conformidad previa; vigencia del requisito de conformidad | Vigencia del requisito de conformidad previa BCRA |
| `ext::3.5.6::cierre` | e2 (Operacion) | descripcion | endeudamientos financieros con el exterior | Acceso de deudas al mercado de cambios para egresos por títulos de deuda suscriptos en el exterior y endeudamientos financieros con el exterior |
| `ext::3.6.1.4` | e4 (Excepcion) | descripcion | de acceso al mercado de | Excepción a la prohibición de acceso al mercado de cambios para el pago de pagarés con oferta pública emitidos en el marco de la Resolución General 1.003/24 de  |
| `ext::4.4.1` | op1 (Operacion) | label | bonos bopreal por deudores de; bopreal por deudores de importaciones; de bonos bopreal por deudores | Suscripción de bonos BOPREAL por deudores de importaciones |
| `ext::4.8.6::intro` | e1 (Condicion) | label | con recompra de bopreal de; de bopreal de suscripcion primaria; recompra de bopreal de suscripcion; venta con recompra de bopreal | Venta con recompra de BOPREAL de suscripción primaria |
| `ext::7.1.1::intro` | e4 (Excepcion) | descripcion | del regimen general de plazos; en lugar del regimen general; lugar del regimen general de | Cuando el cliente sea un VPU adherido al RIGI que cumple con la declaración de intención de uso de beneficios, resultará aplicable lo dispuesto en los puntos 14 |
| `ext::7.10.1.1` | e3 (Operacion) | label | intereses de deudas por importacion; pago de capital e intereses | Pago de capital e intereses de deudas por importación |
| `ext::7.10.1.4` | e2 (Potestad) | label | de cobros de exportaciones para | Admisión de cobros de exportaciones para operaciones del régimen |
| `ext::7.11::intro` | e3 (Potestad) | descripcion | a importaciones de bienes quedan; bienes quedan habilitadas para la; de bienes quedan habilitadas para; importaciones de bienes quedan habilitadas; quedan habilitadas para la aplicacion | Financiaciones asociadas a importaciones de bienes quedan habilitadas para la aplicación de cobros de exportaciones de bienes |
| `ext::7.9.3.2` | e3 (Condicion) | label | exportadores que opten por el; que opten por el mecanismo | Exportadores que opten por el mecanismo |
| `ext::8.5.17.5` | e2 (Excepcion) | descripcion | seguimiento de negociaciones de divisas | Las operaciones aduaneras bajo régimen de muestras (artículos 560 al 565 de la Ley 22.415) están exceptuadas del seguimiento de negociaciones de divisas por exp |
| `ext::8.5.17.5` | e2 (Excepcion) | label | operaciones bajo regimen de muestras | Excepción seguimiento — operaciones bajo régimen de muestras |
| `ext::8.5.17.7` | e1 (Excepcion) | descripcion | de negociaciones de divisas por; seguimiento de negociaciones de divisas | Régimen de equipaje (artículos 488 al 505 de la Ley 22.415) — operación exceptuada del seguimiento de negociaciones de divisas por exportaciones de bienes |
| `ext::9.3.7` | e3 (Condicion) | descripcion | la aplicacion a permisos de; solicitado la aplicacion a permisos | El exportador ha solicitado la aplicación a permisos de embarque oficializados a partir del 02/09/19 |
| `ctacte::10.2.1.3` | e1 (Obligacion) | descripcion | requisito comun de contenido minimo | Los avisos deben incluir la fecha de emisión como requisito común de contenido mínimo. |
| `ctacte::10.2.1.4` | o1 (Obligacion) | descripcion | el caracter con el que | El aviso debe consignar el carácter con el que fue impuesto |
| `ctacte::10.2.4.2` | e1 (Obligacion) | descripcion | el saldo de la cuenta; informar el saldo de la | Informar el saldo de la cuenta corriente involucrada en el aviso del cierre de la cuenta o la suspensión previa del pago de cheques. |
| `ctacte::3.2.1.2` | e2 (Restriccion) | descripcion | carece de valor como cheque; determina que el titulo carece; el titulo carece de valor; que el titulo carece de; titulo carece de valor como | La falta del número de orden, impreso en el cuerpo del cheque librado en formato papel o incorporado a los datos del cheque librado por medios electrónicos, det |
| `ctacte::3.2.1.7` | e3 (Excepcion) | descripcion | carencia de valor como cheque; determina la carencia de valor; la carencia de valor como | La falta de firma del librador no determina la carencia de valor como cheque cuando se utilicen los medios establecidos al efecto. |
| `ctacte::5.1.2.1` | e3 (Operacion) | descripcion | endoso a favor de entidades | Transmisión de cheques, incluyendo cheques con cláusula 'no a la orden', por endoso a favor de entidades financieras en casos de transferencias primeras y suces |
| `ctacte::5.1.2.1` | e3 (Operacion) | label | endoso a favor de entidades | Endoso a favor de entidades financieras |
| `ctacte::6.2.5` | e2 (Excepcion) | descripcion | no son susceptibles de rechazo | Los cheques en los casos previstos en el punto 6.2 no son susceptibles de rechazo |
| `ctacte::6.4.1.1` | e1 (Obligacion) | label | consignar todos los motivos del; todos los motivos del rechazo | Consignar todos los motivos del rechazo |
| `ctacte::8.2.1.1` | e4 (Operacion) | descripcion | inclusion en la central de | Inclusión en la Central de cheques rechazados |
| `lingob::4.1` | e3 (Condicion) | label | integrante con experiencia contable financiera | Integrante con experiencia contable/financiera — Comité de auditoría |
| `pagjub::2.8.2::intro` | e3 (Obligacion) | descripcion | acciones de liquidacion de la; de liquidacion de la rendicion | El BCRA, en el mismo día de la aceptación, procederá a [acciones de liquidación de la rendición de cuentas] |
| `docvig::3.1.4` | e3 (Operacion) | label | modificacion del numero de dni | Modificación del número de DNI |
