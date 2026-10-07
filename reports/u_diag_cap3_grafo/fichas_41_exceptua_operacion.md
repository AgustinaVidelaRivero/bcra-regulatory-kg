# Fichas sin veredicto: relaciones (Excepcion, exceptua, Operacion)

Fichas sin veredicto de las relaciones (Excepcion, exceptua, Operacion) para la condición del §2 de la enmienda 8 a L-ESQ-R2. ⟦E: …⟧ marca el tramo de la Excepcion y ⟦O: …⟧ el de la Operacion.

Criterio: `criterio_41_exceptua_operacion.md (sellado antes de generar estas fichas)`.

Instrucción del prefijo de E1 que rige para todas (prefijo de E1 r2b: reemplazo P3B-c1 (`prompt_r2b_parche_p3b.json`) con el ajuste P3C-d1 (`prompt_r2b_parche_p3c.json`); el texto aparece literal en los pedidos guardados en las cachés de C1 de U-COMP-E1 (`data/experiment/comp_e1/c1/cache/`)):

> CONEXIÓN: si la norma que la Excepcion exceptúa está en tu unidad, conectala: `exceptua` hacia la Restriccion, `exceptua_obligacion` hacia la Obligacion. Si esa norma no está en tu unidad (está en la unidad del encabezado de una lista o en otro punto), emití la Excepcion sin esa relación y decí en la descripción qué norma exceptúa: no la conectes con otro elemento del chunk, no apuntes la relación a un `local_id` que no emitiste y no vuelvas a emitir esa norma dentro de tu unidad para tener a dónde conectarla.

Población: las 41 rechazadas en el crudo de KG-Tanda0-Diez-r2b (EO01 a EO41) y 4 de U-ESTUDIO-MATRIZ (EO42 a EO45: M21, M23, M24 y M25; M22 es la misma relación que una de las 41).

## EO01 — `cla::2.2.1.6`
- origen: crudo de KG-Tanda0-Diez-r2b (a9631a64…), extracción final r2 guardada
- unidad: item; páginas [7]; estado en E3 `completo_ok_directo`; en la cola: no; crudo que entra a E2: e1
- relación rechazada: índice 2 del crudo, `e2` `exceptua` `e1` (punto 2.2.1.6); validador de E1: firma_invalida: relations[2]: Excepcion --exceptua--> Operacion; vista por E3: no
- Excepcion `e2`: **Exclusión de clasificación — obligaciones negociables propias** — Las obligaciones negociables compradas que constituyen emisiones propias quedan exceptuadas de los requisitos de clasificación de deudores | tramo: Obligaciones negociables compradas (emisiones propias) | punto 2.2.1.6 | marcado en texto propio
- Operacion `e1`: **Compra de obligaciones negociables de emisión propia** — Compra de obligaciones negociables que constituyen emisiones propias del intermediario financiero | tramo: Obligaciones negociables compradas (emisiones propias) | punto 2.2.1.6 | marcado en texto propio
- heredado, herencia[0] encabezado S2: Sección 2. Financiaciones comprendidas.
- heredado, herencia[1] encabezado 2.2: 2.2. Exclusiones.
- heredado, herencia[2] encabezado 2.2.1: 2.2.1. Los siguientes conceptos por intermediación financiera:
- texto propio:

```
2.2.1.6. ⟦O:⟦E:Obligaciones negociables compradas (emisiones prop⟧ias⟧).
```

## EO02 — `cla::2.2.1.7`
- origen: crudo de KG-Tanda0-Diez-r2b (a9631a64…), extracción final r2 guardada
- unidad: item; páginas [7]; estado en E3 `aceptado_con_residuales`; en la cola: no; crudo que entra a E2: e1
- relación rechazada: índice 1 del crudo, `e2` `exceptua` `e1` (punto 2.2.1.7); validador de E1: firma_invalida: relations[1]: Excepcion --exceptua--> Operacion; vista por E3: no
- Excepcion `e2`: **Exclusión — Créditos frente al BCRA** — Los créditos frente al Banco Central de la República Argentina quedan excluidos de las financiaciones comprendidas en la clasificación de deudores | tramo: Créditos frente al Banco Central de la República Argentina | punto 2.2.1.7 | marcado en texto propio
- Operacion `e1`: **Créditos frente al BCRA** — Créditos otorgados frente al Banco Central de la República Argentina | tramo: Créditos frente al Banco Central de la República Argentina | punto 2.2.1.7 | marcado en texto propio
- heredado, herencia[0] encabezado S2: Sección 2. Financiaciones comprendidas.
- heredado, herencia[1] encabezado 2.2: 2.2. Exclusiones.
- heredado, herencia[2] encabezado 2.2.1: 2.2.1. Los siguientes conceptos por intermediación financiera:
- texto propio:

```
2.2.1.7. ⟦O:⟦E:Créditos frente al Banco Central de la República Argent⟧ina⟧.
```

## EO03 — `cla::5.1.1.1`
- origen: crudo de KG-Tanda0-Diez-r2b (a9631a64…), extracción final r2 guardada
- unidad: item; páginas [16]; estado en E3 `aceptado_con_residuales`; en la cola: no; crudo que entra a E2: e1
- relación rechazada: índice 6 del crudo, `e2` `exceptua` `e1` (punto 5.1.1.1); validador de E1: firma_invalida: relations[6]: Excepcion --exceptua--> Operacion; vista por E3: no
- Excepcion `e2`: **Excepción cartera comercial — créditos consumo/vivienda** — Los créditos para consumo o vivienda quedan exceptuados de la cartera comercial, salvo cuando reúnen las condiciones especificadas en el punto 5.1.1.1. | tramo: Los créditos para consumo o vivienda. | punto 5.1.1.1 | marcado en texto propio
- Operacion `e1`: **Inclusión en cartera comercial — créditos consumo/vivienda** — Inclusión de créditos para consumo o vivienda en la cartera comercial cuando superan dos veces el importe de referencia del punto 3.7 y su repago está vinculado a la evolución de la actividad productiva o comercial del cliente, no a ingresos fijos o periódicos. | tramo: Los créditos de esta clase que superen el equivalente a dos veces el importe de referencia establecido en el punto 3.7. y cuyo repago no se encuentre vinculado a ingresos fijos o periódicos del cliente sino a la evolución de su actividad productiva o comercial se incluirán dentro de la cartera comercial. | punto 5.1.1.1 | marcado en texto propio
- heredado, herencia[0] encabezado S5: Sección 5. Categorías de carteras.
- heredado, herencia[1] encabezado 5.1: 5.1. Categorías.
- heredado, herencia[2] intro 5.1: La cartera se agrupará en dos categorías básicas:
- heredado, herencia[3] encabezado 5.1.1: 5.1.1. Cartera comercial.
- heredado, herencia[4] intro 5.1.1: Abarca todas las financiaciones comprendidas, con excepción de las siguientes:
- texto propio:

```
5.1.1.1. ⟦E:Los créditos para consumo o vivienda⟧.
⟦O:Los créditos de esta clase que superen el equivalente a dos veces el importe de
referencia establecido en el punto 3.7. y cuyo repago no se encuentre vinculado
a ingresos fijos o periódicos del cliente sino a la evolución de su actividad pro-
ductiva o comercial se incluirán dentro de la cartera comercial⟧.
```

## EO04 — `cla::6.5.3.11`
- origen: crudo de KG-Tanda0-Diez-r2b (a9631a64…), extracción final r2 guardada
- unidad: item; páginas [25]; estado en E3 `completo_ok_directo`; en la cola: no; crudo que entra a E2: e1
- relación rechazada: índice 8 del crudo, `e4` `exceptua` `e5` (punto 6.5.3.11); validador de E1: firma_invalida: relations[8]: Excepcion --exceptua--> Operacion; vista por E3: no
- Excepcion `e4`: **Exclusión acciones sobre aspectos contractuales** — Se excluyen los casos en que las acciones judiciales se refieren a la discusión sobre otros aspectos contractuales distintos de la falta de pago | tramo: Se excluyen los casos en que las acciones se refieren a la discusión sobre otros aspectos contractuales | punto 6.5.3.11 | marcado en texto propio
- Operacion `e5`: **Clasificación de deudor con problemas** — Clasificación del cliente en la categoría 'Con problemas' cuando ha sido demandado judicialmente por cobro de acreencia vinculada a falta de pago con mora no superior a 180 días | tramo: Haya sido demandado judicialmente por la entidad para el cobro de su acreencia, cuando ello se encuentre vinculado a la falta de pago y registre mora en el pago de las obligaciones no superior a 180 días | punto 6.5.3.11 | marcado en texto propio
- heredado, herencia[0] encabezado S6: Sección 6. Clasificación de los deudores de la cartera comercial.
- heredado, herencia[1] encabezado 6.5: 6.5. Niveles de clasificación.
- heredado, herencia[2] intro 6.5: Cada cliente, y la totalidad de sus financiaciones comprendidas, se incluirá en una de las si-
guientes cinco categorías, las que se definen teniendo en cuenta las condiciones que se deta-
llan en cada caso.
Los clientes que no registren asistencia crediticia de la entidad y que posteriormente reciban fi-
nanciaciones de ésta que no superen el importe resultante de aplicar sobre el saldo de deuda
registrado en el sistema financiero, según la última información disponible en la “Central de
deudores” a la fecha de su otorgamiento, el porcentaje establecido en el punto 2.2.5. de las
normas sobre “Previsiones mínimas por riesgo de incobrabilidad” correspondiente a la peor cla-
sificación asignada, podrán ser clasificados por la entidad teniendo en cuenta únicamente el
análisis del flujo de fondos proyectado. Las asistencias así otorgadas no serán consideradas a
los fines a que se refiere el punto 6.6.
A fin de verificar el cumplimiento de las obligaciones sin recurrir a nueva financiación directa o
indirecta o a refinanciaciones, no se considerarán refinanciaciones las facilidades adicionales
que se otorguen respecto de los márgenes vigentes acordados, siempre que el nuevo apoyo
crediticio implique nuevos desembolsos de fondos y no supere el 10 % del cupo asignado en
oportunidad de la última evaluación crediticia del cliente, en la medida en que éstas sean con-
sistentes con el curso normal de los negocios y exista capacidad para atender el resto de las
obligaciones financieras, ni las nuevas financiaciones y las refinanciaciones asociadas a una
mayor inversión derivada de la expansión de las actividades, y siempre que pueda demostrarse
que el flujo de fondos proyectado permitirá afrontar la totalidad de sus obligaciones.
Tampoco se considerarán dentro de ese concepto las refinanciaciones otorgadas a los produc-
tores agropecuarios cuando ello resulte de la aplicación de disposiciones vinculadas a la Ley de
Emergencia Agropecuaria, sin perjuicio de lo cual, a los fines de la clasificación, deberá tenerse
en cuenta el flujo de fondos proyectado para el momento en que concluya la vigencia de la
emergencia declarada. El tratamiento que se dispense en ese marco no podrá implicar mejora-
miento de la clasificación asignada al cliente en función de su situación individual, preexistente
a la emergencia, ni su aplicación extenderse más allá de la vigencia fijada para ella.
- heredado, herencia[3] encabezado 6.5.3: 6.5.3. Con problemas.
- heredado, herencia[4] intro 6.5.3: El análisis del flujo de fondos del cliente demuestra que tiene problemas para atender
normalmente la totalidad de sus compromisos financieros y que, de no ser corregidos,
esos problemas pueden resultar en una pérdida para la entidad financiera.
Entre los indicadores que pueden reflejar esta situación se destacan que el cliente:
- texto propio:

```
6.5.3.11. ⟦O:Haya sido demandado judicialmente por la entidad para el cobro de su acreen-
cia, cuando ello se encuentre vinculado a la falta de pago y registre mora en el
pago de las obligaciones no superior a 180 días⟧. ⟦E:Se excluyen los casos en que
las acciones se refieren a la discusión sobre otros aspectos contractuales⟧.
```

## EO05 — `cla::6.5.5.7`
- origen: crudo de KG-Tanda0-Diez-r2b (a9631a64…), extracción final r2 guardada
- unidad: item; páginas [29]; estado en E3 `completo_ok_directo`; en la cola: no; crudo que entra a E2: e1
- relación rechazada: índice 14 del crudo, `e8` `exceptua` `e1` (punto 6.5.5.7); validador de E1: firma_invalida: relations[14]: Excepcion --exceptua--> Operacion; vista por E3: no
- Excepcion `e8`: **Excepción: financiaciones para cancelar préstamos originarios** — No se clasifican en la categoría Irrecuperable los deudores cuando las financiaciones otorgadas se destinen a cancelar los préstamos que originaron su inclusión en la nómina de deudores morosos y los fondos se acrediten directamente en las cuentas de las ex entidades acreedoras | tramo: Se exceptúa de ser clasificados en esta categoría a los deudores, cuando las financiaciones otorgadas a ellos se destinen a cancelar los préstamos que originaron su inclusión en la nómina de deudores morosos y siempre que los fondos se acrediten directamente en las cuentas de las ex entidades acreedoras | punto 6.5.5.7 | marcado en texto propio
- Operacion `e1`: **Clasificación en categoría Irrecuperable** — Clasificación de clientes que sean deudores en situación irregular, definidos como aquellos que registren atrasos superiores a 180 días en el cumplimiento de sus obligaciones, de acuerdo con la nómina que el BCRA elabore y proporcione a base de información suministrada por administradores de carteras crediticias | tramo: Clientes que a su vez sean deudores en situación irregular –considerando tales a los que registren atrasos superiores a 180 días en el cumplimiento de sus obligaciones– | punto 6.5.5.7 | marcado en texto propio
- heredado, herencia[0] encabezado S6: Sección 6. Clasificación de los deudores de la cartera comercial.
- heredado, herencia[1] encabezado 6.5: 6.5. Niveles de clasificación.
- heredado, herencia[2] intro 6.5: Cada cliente, y la totalidad de sus financiaciones comprendidas, se incluirá en una de las si-
guientes cinco categorías, las que se definen teniendo en cuenta las condiciones que se deta-
llan en cada caso.
Los clientes que no registren asistencia crediticia de la entidad y que posteriormente reciban fi-
nanciaciones de ésta que no superen el importe resultante de aplicar sobre el saldo de deuda
registrado en el sistema financiero, según la última información disponible en la “Central de
deudores” a la fecha de su otorgamiento, el porcentaje establecido en el punto 2.2.5. de las
normas sobre “Previsiones mínimas por riesgo de incobrabilidad” correspondiente a la peor cla-
sificación asignada, podrán ser clasificados por la entidad teniendo en cuenta únicamente el
análisis del flujo de fondos proyectado. Las asistencias así otorgadas no serán consideradas a
los fines a que se refiere el punto 6.6.
A fin de verificar el cumplimiento de las obligaciones sin recurrir a nueva financiación directa o
indirecta o a refinanciaciones, no se considerarán refinanciaciones las facilidades adicionales
que se otorguen respecto de los márgenes vigentes acordados, siempre que el nuevo apoyo
crediticio implique nuevos desembolsos de fondos y no supere el 10 % del cupo asignado en
oportunidad de la última evaluación crediticia del cliente, en la medida en que éstas sean con-
sistentes con el curso normal de los negocios y exista capacidad para atender el resto de las
obligaciones financieras, ni las nuevas financiaciones y las refinanciaciones asociadas a una
mayor inversión derivada de la expansión de las actividades, y siempre que pueda demostrarse
que el flujo de fondos proyectado permitirá afrontar la totalidad de sus obligaciones.
Tampoco se considerarán dentro de ese concepto las refinanciaciones otorgadas a los produc-
tores agropecuarios cuando ello resulte de la aplicación de disposiciones vinculadas a la Ley de
Emergencia Agropecuaria, sin perjuicio de lo cual, a los fines de la clasificación, deberá tenerse
en cuenta el flujo de fondos proyectado para el momento en que concluya la vigencia de la
emergencia declarada. El tratamiento que se dispense en ese marco no podrá implicar mejora-
miento de la clasificación asignada al cliente en función de su situación individual, preexistente
a la emergencia, ni su aplicación extenderse más allá de la vigencia fijada para ella.
- heredado, herencia[3] encabezado 6.5.5: 6.5.5. Irrecuperable.
- heredado, herencia[4] intro 6.5.5: Las deudas de clientes incorporados a esta categoría se consideran incobrables. Si bien
estos activos podrían tener algún valor de recuperación bajo un cierto conjunto de cir-
cunstancias futuras, su incobrabilidad es evidente al momento del análisis.
Entre los indicadores que pueden reflejar esta situación se destacan que el cliente:
- heredado, herencia[5] cierre 6.5.5: Además, corresponderá clasificar en esta categoría a los clientes que, cualquiera sea el
motivo (entre ellos por no contar con legajo o por no haber proporcionado información
confiable y/o actualizada), no hayan sido evaluados con la periodicidad correspondiente,
con excepción de los deudores en concurso o con acuerdo preventivo extrajudicial solici-
tado o en gestión judicial que, por un período de hasta 540 días contados a partir de la
apertura del concurso, solicitud del acuerdo preventivo o inicio de las gestiones judiciales
de cobro, según corresponda, no hubiesen presentado la documentación que permita
realizarla, siempre que se cuente con informe de abogado de la entidad financiera
acreedora sobre la razonabilidad del recupero de los créditos comprendidos.
Ello, sin perjuicio de que se trate de deudas que reúnan todas las condiciones previstas
por el punto 2.2.3.2. de las normas sobre “Previsiones mínimas por riesgo de incobrabili-
dad”.
- texto propio:

```
6.5.5.7. ⟦O:Clientes que a su vez sean deudores en situación irregular –considerando tales
a los que registren atrasos superiores a 180 días en el cumplimiento de sus obli-
gaciones⟧–, de acuerdo con la nómina que, a tal efecto y a base de la informa-
ción que deberán suministrar los administradores de las carteras crediticias, ela-
bore y proporcione el Banco Central de la República Argentina (BCRA) de:
i) Entidades liquidadas por el BCRA.
ii) Entes residuales de entidades financieras públicas privatizadas o en proce-
so de privatización o disolución.
iii) Entidades financieras cuya autorización para funcionar haya sido revocada
por el BCRA y se encuentren en estado de liquidación judicial o quiebra.
iv) Fideicomisos en los que SEDESA sea beneficiario.
⟦E:Se exceptúa de ser clasificados en esta categoría a los deudores, cuando las fi-
nanciaciones otorgadas a ellos se destinen a cancelar los préstamos que origina-
ron su inclusión en la nómina de deudores morosos y siempre que los fondos se
acrediten directamente en las cuentas de las ex entidades acreedoras⟧.
```

## EO06 — `cla::6.5.5.8`
- origen: crudo de KG-Tanda0-Diez-r2b (a9631a64…), extracción final r2 guardada
- unidad: item; páginas [29, 30]; estado en E3 `aceptado_con_residuales`; en la cola: no; crudo que entra a E2: e1
- relación rechazada: índice 18 del crudo, `e3` `exceptua` `e1` (punto 6.5.5.8); validador de E1: firma_invalida: relations[18]: Excepcion --exceptua--> Operacion; vista por E3: no
- Excepcion `e3`: **Exclusión casa matriz de sucursales locales de bancos del exterior** — Se excluyen de la clasificación en Irrecuperable la casa matriz de las sucursales locales de bancos del exterior o sus filiales y subsidiarias en otros países, en la medida en que estén sujetas a supervisión sobre base consolidada | tramo: Casa matriz de las sucursales locales de bancos del exterior o sus filiales y subsidiarias en otros países, en la medida en que aquélla esté sujeta a supervisión sobre base consolidada | punto 6.5.5.8 | marcado en texto propio
- Operacion `e1`: **Clasificación en categoría Irrecuperable** — Clasificación de bancos, otras instituciones financieras del exterior y otros prestatarios no radicados en el país en la categoría Irrecuperable cuando no cumplan con lo previsto en los puntos 3.1. y 3.2. de las normas sobre Evaluaciones crediticias | tramo: Bancos, otras instituciones financieras del exterior y otros prestatarios no radicados en el país que no cumplan con lo previsto en los puntos 3.1. y 3.2., según corresponda, de las normas sobre "Evaluaciones crediticias" | punto 6.5.5.8 | marcado en texto propio
- heredado, herencia[0] encabezado S6: Sección 6. Clasificación de los deudores de la cartera comercial.
- heredado, herencia[1] encabezado 6.5: 6.5. Niveles de clasificación.
- heredado, herencia[2] intro 6.5: Cada cliente, y la totalidad de sus financiaciones comprendidas, se incluirá en una de las si-
guientes cinco categorías, las que se definen teniendo en cuenta las condiciones que se deta-
llan en cada caso.
Los clientes que no registren asistencia crediticia de la entidad y que posteriormente reciban fi-
nanciaciones de ésta que no superen el importe resultante de aplicar sobre el saldo de deuda
registrado en el sistema financiero, según la última información disponible en la “Central de
deudores” a la fecha de su otorgamiento, el porcentaje establecido en el punto 2.2.5. de las
normas sobre “Previsiones mínimas por riesgo de incobrabilidad” correspondiente a la peor cla-
sificación asignada, podrán ser clasificados por la entidad teniendo en cuenta únicamente el
análisis del flujo de fondos proyectado. Las asistencias así otorgadas no serán consideradas a
los fines a que se refiere el punto 6.6.
A fin de verificar el cumplimiento de las obligaciones sin recurrir a nueva financiación directa o
indirecta o a refinanciaciones, no se considerarán refinanciaciones las facilidades adicionales
que se otorguen respecto de los márgenes vigentes acordados, siempre que el nuevo apoyo
crediticio implique nuevos desembolsos de fondos y no supere el 10 % del cupo asignado en
oportunidad de la última evaluación crediticia del cliente, en la medida en que éstas sean con-
sistentes con el curso normal de los negocios y exista capacidad para atender el resto de las
obligaciones financieras, ni las nuevas financiaciones y las refinanciaciones asociadas a una
mayor inversión derivada de la expansión de las actividades, y siempre que pueda demostrarse
que el flujo de fondos proyectado permitirá afrontar la totalidad de sus obligaciones.
Tampoco se considerarán dentro de ese concepto las refinanciaciones otorgadas a los produc-
tores agropecuarios cuando ello resulte de la aplicación de disposiciones vinculadas a la Ley de
Emergencia Agropecuaria, sin perjuicio de lo cual, a los fines de la clasificación, deberá tenerse
en cuenta el flujo de fondos proyectado para el momento en que concluya la vigencia de la
emergencia declarada. El tratamiento que se dispense en ese marco no podrá implicar mejora-
miento de la clasificación asignada al cliente en función de su situación individual, preexistente
a la emergencia, ni su aplicación extenderse más allá de la vigencia fijada para ella.
- heredado, herencia[3] encabezado 6.5.5: 6.5.5. Irrecuperable.
- heredado, herencia[4] intro 6.5.5: Las deudas de clientes incorporados a esta categoría se consideran incobrables. Si bien
estos activos podrían tener algún valor de recuperación bajo un cierto conjunto de cir-
cunstancias futuras, su incobrabilidad es evidente al momento del análisis.
Entre los indicadores que pueden reflejar esta situación se destacan que el cliente:
- heredado, herencia[5] cierre 6.5.5: Además, corresponderá clasificar en esta categoría a los clientes que, cualquiera sea el
motivo (entre ellos por no contar con legajo o por no haber proporcionado información
confiable y/o actualizada), no hayan sido evaluados con la periodicidad correspondiente,
con excepción de los deudores en concurso o con acuerdo preventivo extrajudicial solici-
tado o en gestión judicial que, por un período de hasta 540 días contados a partir de la
apertura del concurso, solicitud del acuerdo preventivo o inicio de las gestiones judiciales
de cobro, según corresponda, no hubiesen presentado la documentación que permita
realizarla, siempre que se cuente con informe de abogado de la entidad financiera
acreedora sobre la razonabilidad del recupero de los créditos comprendidos.
Ello, sin perjuicio de que se trate de deudas que reúnan todas las condiciones previstas
por el punto 2.2.3.2. de las normas sobre “Previsiones mínimas por riesgo de incobrabili-
dad”.
- texto propio:

```
6.5.5.8. ⟦O:Bancos, otras instituciones financieras del exterior y otros prestatarios no
radicados en el país que no cumplan con lo previsto en los puntos 3.1. y 3.2.,
según corresponda, de las normas sobre “Evaluaciones crediticias⟧”. A los
efectos del cumplimiento de los citados puntos se deberá contar con calificación
internacional de riesgo comprendida en la categoría “investment grade”.
Se excluirán:
a) Los siguientes deudores:
⟦E:Casa matriz de las sucursales locales de bancos del exterior o sus filiales y
subsidiarias en otros países, en la medida en que aquélla esté sujeta a super-
visión sobre base consolidada⟧.
Bancos u otras instituciones financieras del exterior sujetos a supervisión so-
bre base consolidada que ejerzan el control de entidades financieras locales
constituidas bajo la forma de sociedades anónimas.
Otros bancos del exterior autorizados a intervenir en los regímenes de conve-
nios de pagos y créditos recíprocos a los que haya adherido el BCRA, así co-
mo sus sucursales y subsidiarias, aun cuando ellas no estén comprendidas en
esos convenios, siempre que la casa matriz o entidad bancaria controlante es-
té sujeta a regímenes de supervisión sobre base consolidada, a satisfacción
de la SEFyC.
Sucursales y subsidiarias de entidades financieras locales sujetas al régimen
de supervisión consolidada.
b) Los deudores que únicamente registren las siguientes operaciones:
- Financiaciones que cuenten con aval de banco del exterior que cumpla con
lo previsto en el punto 3.1. de las normas sobre “Evaluaciones crediticias”,
requiriendo a ese efecto calificación internacional de riesgo comprendida en
la categoría “investment grade”.
- Financiaciones vinculadas a operaciones de compraventa de títulos valores
concertadas con residentes en el exterior, que se canalicen por la Caja de
Valores S.A., Clearstream, Euroclear o Depositary Trust Company (DTC), y
que se originen en el cumplimiento, por parte de la entidad financiera intervi-
niente, de la obligación a su cargo (entregar la especie transada o efectuar el
pago convenido) sin que la contraparte cancele su compromiso en el mismo
día, en razón de modalidades de liquidación usuales en esos mercados.
- Financiaciones vinculadas a operaciones de comercio exterior.
- Pases activos de dólares estadounidenses y de títulos valores públicos na-
cionales, siempre que:
 las especies transadas cuenten con un mercado de operaciones habitua-
les y relevantes,
 los precios pactados respondan a las condiciones del mercado y
 los márgenes de cobertura sean suficientes y se encuentren depositados
en los siguientes agentes de custodia o de registro:
* BCRA, por operaciones canalizadas a través de la Central de registro y
liquidación de instrumentos de deuda pública, regulación monetaria y fi-
deicomisos financieros (CRyL),
* Caja de Valores S.A.,
* Clearstream, Euroclear, Depositary Trust Company (DTC) y
- Asistencia crediticia concedida a través de las sucursales o subsidiarias en el
exterior de entidades financieras locales sujetas al régimen de supervisión
sobre base consolidada, siempre que se haya otorgado con recursos que no
provengan de fondos provistos, directa o indirectamente, por las entidades
financieras locales.
Los deudores excluidos precedentemente deberán ser clasificados y sus deudas
previsionadas conforme a las disposiciones de carácter general.
```

## EO07 — `cla::6.5.5.8`
- origen: crudo de KG-Tanda0-Diez-r2b (a9631a64…), extracción final r2 guardada
- unidad: item; páginas [29, 30]; estado en E3 `aceptado_con_residuales`; en la cola: no; crudo que entra a E2: e1
- relación rechazada: índice 19 del crudo, `e4` `exceptua` `e1` (punto 6.5.5.8); validador de E1: firma_invalida: relations[19]: Excepcion --exceptua--> Operacion; vista por E3: no
- Excepcion `e4`: **Exclusión bancos del exterior con supervisión consolidada que controlan entidades locales** — Se excluyen de la clasificación en Irrecuperable los bancos u otras instituciones financieras del exterior sujetos a supervisión sobre base consolidada que ejerzan el control de entidades financieras locales constituidas bajo la forma de sociedades anónimas | tramo: Bancos u otras instituciones financieras del exterior sujetos a supervisión sobre base consolidada que ejerzan el control de entidades financieras locales constituidas bajo la forma de sociedades anónimas | punto 6.5.5.8 | marcado en texto propio
- Operacion `e1`: **Clasificación en categoría Irrecuperable** — Clasificación de bancos, otras instituciones financieras del exterior y otros prestatarios no radicados en el país en la categoría Irrecuperable cuando no cumplan con lo previsto en los puntos 3.1. y 3.2. de las normas sobre Evaluaciones crediticias | tramo: Bancos, otras instituciones financieras del exterior y otros prestatarios no radicados en el país que no cumplan con lo previsto en los puntos 3.1. y 3.2., según corresponda, de las normas sobre "Evaluaciones crediticias" | punto 6.5.5.8 | marcado en texto propio
- heredado, herencia[0] encabezado S6: Sección 6. Clasificación de los deudores de la cartera comercial.
- heredado, herencia[1] encabezado 6.5: 6.5. Niveles de clasificación.
- heredado, herencia[2] intro 6.5: Cada cliente, y la totalidad de sus financiaciones comprendidas, se incluirá en una de las si-
guientes cinco categorías, las que se definen teniendo en cuenta las condiciones que se deta-
llan en cada caso.
Los clientes que no registren asistencia crediticia de la entidad y que posteriormente reciban fi-
nanciaciones de ésta que no superen el importe resultante de aplicar sobre el saldo de deuda
registrado en el sistema financiero, según la última información disponible en la “Central de
deudores” a la fecha de su otorgamiento, el porcentaje establecido en el punto 2.2.5. de las
normas sobre “Previsiones mínimas por riesgo de incobrabilidad” correspondiente a la peor cla-
sificación asignada, podrán ser clasificados por la entidad teniendo en cuenta únicamente el
análisis del flujo de fondos proyectado. Las asistencias así otorgadas no serán consideradas a
los fines a que se refiere el punto 6.6.
A fin de verificar el cumplimiento de las obligaciones sin recurrir a nueva financiación directa o
indirecta o a refinanciaciones, no se considerarán refinanciaciones las facilidades adicionales
que se otorguen respecto de los márgenes vigentes acordados, siempre que el nuevo apoyo
crediticio implique nuevos desembolsos de fondos y no supere el 10 % del cupo asignado en
oportunidad de la última evaluación crediticia del cliente, en la medida en que éstas sean con-
sistentes con el curso normal de los negocios y exista capacidad para atender el resto de las
obligaciones financieras, ni las nuevas financiaciones y las refinanciaciones asociadas a una
mayor inversión derivada de la expansión de las actividades, y siempre que pueda demostrarse
que el flujo de fondos proyectado permitirá afrontar la totalidad de sus obligaciones.
Tampoco se considerarán dentro de ese concepto las refinanciaciones otorgadas a los produc-
tores agropecuarios cuando ello resulte de la aplicación de disposiciones vinculadas a la Ley de
Emergencia Agropecuaria, sin perjuicio de lo cual, a los fines de la clasificación, deberá tenerse
en cuenta el flujo de fondos proyectado para el momento en que concluya la vigencia de la
emergencia declarada. El tratamiento que se dispense en ese marco no podrá implicar mejora-
miento de la clasificación asignada al cliente en función de su situación individual, preexistente
a la emergencia, ni su aplicación extenderse más allá de la vigencia fijada para ella.
- heredado, herencia[3] encabezado 6.5.5: 6.5.5. Irrecuperable.
- heredado, herencia[4] intro 6.5.5: Las deudas de clientes incorporados a esta categoría se consideran incobrables. Si bien
estos activos podrían tener algún valor de recuperación bajo un cierto conjunto de cir-
cunstancias futuras, su incobrabilidad es evidente al momento del análisis.
Entre los indicadores que pueden reflejar esta situación se destacan que el cliente:
- heredado, herencia[5] cierre 6.5.5: Además, corresponderá clasificar en esta categoría a los clientes que, cualquiera sea el
motivo (entre ellos por no contar con legajo o por no haber proporcionado información
confiable y/o actualizada), no hayan sido evaluados con la periodicidad correspondiente,
con excepción de los deudores en concurso o con acuerdo preventivo extrajudicial solici-
tado o en gestión judicial que, por un período de hasta 540 días contados a partir de la
apertura del concurso, solicitud del acuerdo preventivo o inicio de las gestiones judiciales
de cobro, según corresponda, no hubiesen presentado la documentación que permita
realizarla, siempre que se cuente con informe de abogado de la entidad financiera
acreedora sobre la razonabilidad del recupero de los créditos comprendidos.
Ello, sin perjuicio de que se trate de deudas que reúnan todas las condiciones previstas
por el punto 2.2.3.2. de las normas sobre “Previsiones mínimas por riesgo de incobrabili-
dad”.
- texto propio:

```
6.5.5.8. ⟦O:Bancos, otras instituciones financieras del exterior y otros prestatarios no
radicados en el país que no cumplan con lo previsto en los puntos 3.1. y 3.2.,
según corresponda, de las normas sobre “Evaluaciones crediticias⟧”. A los
efectos del cumplimiento de los citados puntos se deberá contar con calificación
internacional de riesgo comprendida en la categoría “investment grade”.
Se excluirán:
a) Los siguientes deudores:
Casa matriz de las sucursales locales de bancos del exterior o sus filiales y
subsidiarias en otros países, en la medida en que aquélla esté sujeta a super-
visión sobre base consolidada.
⟦E:Bancos u otras instituciones financieras del exterior sujetos a supervisión so-
bre base consolidada que ejerzan el control de entidades financieras locales
constituidas bajo la forma de sociedades anónimas⟧.
Otros bancos del exterior autorizados a intervenir en los regímenes de conve-
nios de pagos y créditos recíprocos a los que haya adherido el BCRA, así co-
mo sus sucursales y subsidiarias, aun cuando ellas no estén comprendidas en
esos convenios, siempre que la casa matriz o entidad bancaria controlante es-
té sujeta a regímenes de supervisión sobre base consolidada, a satisfacción
de la SEFyC.
Sucursales y subsidiarias de entidades financieras locales sujetas al régimen
de supervisión consolidada.
b) Los deudores que únicamente registren las siguientes operaciones:
- Financiaciones que cuenten con aval de banco del exterior que cumpla con
lo previsto en el punto 3.1. de las normas sobre “Evaluaciones crediticias”,
requiriendo a ese efecto calificación internacional de riesgo comprendida en
la categoría “investment grade”.
- Financiaciones vinculadas a operaciones de compraventa de títulos valores
concertadas con residentes en el exterior, que se canalicen por la Caja de
Valores S.A., Clearstream, Euroclear o Depositary Trust Company (DTC), y
que se originen en el cumplimiento, por parte de la entidad financiera intervi-
niente, de la obligación a su cargo (entregar la especie transada o efectuar el
pago convenido) sin que la contraparte cancele su compromiso en el mismo
día, en razón de modalidades de liquidación usuales en esos mercados.
- Financiaciones vinculadas a operaciones de comercio exterior.
- Pases activos de dólares estadounidenses y de títulos valores públicos na-
cionales, siempre que:
 las especies transadas cuenten con un mercado de operaciones habitua-
les y relevantes,
 los precios pactados respondan a las condiciones del mercado y
 los márgenes de cobertura sean suficientes y se encuentren depositados
en los siguientes agentes de custodia o de registro:
* BCRA, por operaciones canalizadas a través de la Central de registro y
liquidación de instrumentos de deuda pública, regulación monetaria y fi-
deicomisos financieros (CRyL),
* Caja de Valores S.A.,
* Clearstream, Euroclear, Depositary Trust Company (DTC) y
- Asistencia crediticia concedida a través de las sucursales o subsidiarias en el
exterior de entidades financieras locales sujetas al régimen de supervisión
sobre base consolidada, siempre que se haya otorgado con recursos que no
provengan de fondos provistos, directa o indirectamente, por las entidades
financieras locales.
Los deudores excluidos precedentemente deberán ser clasificados y sus deudas
previsionadas conforme a las disposiciones de carácter general.
```

## EO08 — `cla::6.5.5.8`
- origen: crudo de KG-Tanda0-Diez-r2b (a9631a64…), extracción final r2 guardada
- unidad: item; páginas [29, 30]; estado en E3 `aceptado_con_residuales`; en la cola: no; crudo que entra a E2: e1
- relación rechazada: índice 20 del crudo, `e5` `exceptua` `e1` (punto 6.5.5.8); validador de E1: firma_invalida: relations[20]: Excepcion --exceptua--> Operacion; vista por E3: no
- Excepcion `e5`: **Exclusión bancos del exterior en convenios de pagos y créditos recíprocos** — Se excluyen de la clasificación en Irrecuperable otros bancos del exterior autorizados a intervenir en los regímenes de convenios de pagos y créditos recíprocos a los que haya adherido el BCRA, así como sus sucursales y subsidiarias, siempre que la casa matriz o entidad bancaria controlante esté sujeta a supervisión sobre base consolidada, a satisfacción de la SEFyC | tramo: Otros bancos del exterior autorizados a intervenir en los regímenes de convenios de pagos y créditos recíprocos a los que haya adherido el BCRA, así como sus sucursales y subsidiarias, aun cuando ellas no estén comprendidas en esos convenios, siempre que la casa matriz o entidad bancaria controlante esté sujeta a regímenes de supervisión sobre base consolidada, a satisfacción de la SEFyC | punto 6.5.5.8 | marcado en texto propio
- Operacion `e1`: **Clasificación en categoría Irrecuperable** — Clasificación de bancos, otras instituciones financieras del exterior y otros prestatarios no radicados en el país en la categoría Irrecuperable cuando no cumplan con lo previsto en los puntos 3.1. y 3.2. de las normas sobre Evaluaciones crediticias | tramo: Bancos, otras instituciones financieras del exterior y otros prestatarios no radicados en el país que no cumplan con lo previsto en los puntos 3.1. y 3.2., según corresponda, de las normas sobre "Evaluaciones crediticias" | punto 6.5.5.8 | marcado en texto propio
- heredado, herencia[0] encabezado S6: Sección 6. Clasificación de los deudores de la cartera comercial.
- heredado, herencia[1] encabezado 6.5: 6.5. Niveles de clasificación.
- heredado, herencia[2] intro 6.5: Cada cliente, y la totalidad de sus financiaciones comprendidas, se incluirá en una de las si-
guientes cinco categorías, las que se definen teniendo en cuenta las condiciones que se deta-
llan en cada caso.
Los clientes que no registren asistencia crediticia de la entidad y que posteriormente reciban fi-
nanciaciones de ésta que no superen el importe resultante de aplicar sobre el saldo de deuda
registrado en el sistema financiero, según la última información disponible en la “Central de
deudores” a la fecha de su otorgamiento, el porcentaje establecido en el punto 2.2.5. de las
normas sobre “Previsiones mínimas por riesgo de incobrabilidad” correspondiente a la peor cla-
sificación asignada, podrán ser clasificados por la entidad teniendo en cuenta únicamente el
análisis del flujo de fondos proyectado. Las asistencias así otorgadas no serán consideradas a
los fines a que se refiere el punto 6.6.
A fin de verificar el cumplimiento de las obligaciones sin recurrir a nueva financiación directa o
indirecta o a refinanciaciones, no se considerarán refinanciaciones las facilidades adicionales
que se otorguen respecto de los márgenes vigentes acordados, siempre que el nuevo apoyo
crediticio implique nuevos desembolsos de fondos y no supere el 10 % del cupo asignado en
oportunidad de la última evaluación crediticia del cliente, en la medida en que éstas sean con-
sistentes con el curso normal de los negocios y exista capacidad para atender el resto de las
obligaciones financieras, ni las nuevas financiaciones y las refinanciaciones asociadas a una
mayor inversión derivada de la expansión de las actividades, y siempre que pueda demostrarse
que el flujo de fondos proyectado permitirá afrontar la totalidad de sus obligaciones.
Tampoco se considerarán dentro de ese concepto las refinanciaciones otorgadas a los produc-
tores agropecuarios cuando ello resulte de la aplicación de disposiciones vinculadas a la Ley de
Emergencia Agropecuaria, sin perjuicio de lo cual, a los fines de la clasificación, deberá tenerse
en cuenta el flujo de fondos proyectado para el momento en que concluya la vigencia de la
emergencia declarada. El tratamiento que se dispense en ese marco no podrá implicar mejora-
miento de la clasificación asignada al cliente en función de su situación individual, preexistente
a la emergencia, ni su aplicación extenderse más allá de la vigencia fijada para ella.
- heredado, herencia[3] encabezado 6.5.5: 6.5.5. Irrecuperable.
- heredado, herencia[4] intro 6.5.5: Las deudas de clientes incorporados a esta categoría se consideran incobrables. Si bien
estos activos podrían tener algún valor de recuperación bajo un cierto conjunto de cir-
cunstancias futuras, su incobrabilidad es evidente al momento del análisis.
Entre los indicadores que pueden reflejar esta situación se destacan que el cliente:
- heredado, herencia[5] cierre 6.5.5: Además, corresponderá clasificar en esta categoría a los clientes que, cualquiera sea el
motivo (entre ellos por no contar con legajo o por no haber proporcionado información
confiable y/o actualizada), no hayan sido evaluados con la periodicidad correspondiente,
con excepción de los deudores en concurso o con acuerdo preventivo extrajudicial solici-
tado o en gestión judicial que, por un período de hasta 540 días contados a partir de la
apertura del concurso, solicitud del acuerdo preventivo o inicio de las gestiones judiciales
de cobro, según corresponda, no hubiesen presentado la documentación que permita
realizarla, siempre que se cuente con informe de abogado de la entidad financiera
acreedora sobre la razonabilidad del recupero de los créditos comprendidos.
Ello, sin perjuicio de que se trate de deudas que reúnan todas las condiciones previstas
por el punto 2.2.3.2. de las normas sobre “Previsiones mínimas por riesgo de incobrabili-
dad”.
- texto propio:

```
6.5.5.8. ⟦O:Bancos, otras instituciones financieras del exterior y otros prestatarios no
radicados en el país que no cumplan con lo previsto en los puntos 3.1. y 3.2.,
según corresponda, de las normas sobre “Evaluaciones crediticias⟧”. A los
efectos del cumplimiento de los citados puntos se deberá contar con calificación
internacional de riesgo comprendida en la categoría “investment grade”.
Se excluirán:
a) Los siguientes deudores:
Casa matriz de las sucursales locales de bancos del exterior o sus filiales y
subsidiarias en otros países, en la medida en que aquélla esté sujeta a super-
visión sobre base consolidada.
Bancos u otras instituciones financieras del exterior sujetos a supervisión so-
bre base consolidada que ejerzan el control de entidades financieras locales
constituidas bajo la forma de sociedades anónimas.
⟦E:Otros bancos del exterior autorizados a intervenir en los regímenes de conve-
nios de pagos y créditos recíprocos a los que haya adherido el BCRA, así co-
mo sus sucursales y subsidiarias, aun cuando ellas no estén comprendidas en
esos convenios, siempre que la casa matriz o entidad bancaria controlante es-
té sujeta a regímenes de supervisión sobre base consolidada, a satisfacción
de la SEFyC⟧.
Sucursales y subsidiarias de entidades financieras locales sujetas al régimen
de supervisión consolidada.
b) Los deudores que únicamente registren las siguientes operaciones:
- Financiaciones que cuenten con aval de banco del exterior que cumpla con
lo previsto en el punto 3.1. de las normas sobre “Evaluaciones crediticias”,
requiriendo a ese efecto calificación internacional de riesgo comprendida en
la categoría “investment grade”.
- Financiaciones vinculadas a operaciones de compraventa de títulos valores
concertadas con residentes en el exterior, que se canalicen por la Caja de
Valores S.A., Clearstream, Euroclear o Depositary Trust Company (DTC), y
que se originen en el cumplimiento, por parte de la entidad financiera intervi-
niente, de la obligación a su cargo (entregar la especie transada o efectuar el
pago convenido) sin que la contraparte cancele su compromiso en el mismo
día, en razón de modalidades de liquidación usuales en esos mercados.
- Financiaciones vinculadas a operaciones de comercio exterior.
- Pases activos de dólares estadounidenses y de títulos valores públicos na-
cionales, siempre que:
 las especies transadas cuenten con un mercado de operaciones habitua-
les y relevantes,
 los precios pactados respondan a las condiciones del mercado y
 los márgenes de cobertura sean suficientes y se encuentren depositados
en los siguientes agentes de custodia o de registro:
* BCRA, por operaciones canalizadas a través de la Central de registro y
liquidación de instrumentos de deuda pública, regulación monetaria y fi-
deicomisos financieros (CRyL),
* Caja de Valores S.A.,
* Clearstream, Euroclear, Depositary Trust Company (DTC) y
- Asistencia crediticia concedida a través de las sucursales o subsidiarias en el
exterior de entidades financieras locales sujetas al régimen de supervisión
sobre base consolidada, siempre que se haya otorgado con recursos que no
provengan de fondos provistos, directa o indirectamente, por las entidades
financieras locales.
Los deudores excluidos precedentemente deberán ser clasificados y sus deudas
previsionadas conforme a las disposiciones de carácter general.
```

## EO09 — `cla::6.5.5.8`
- origen: crudo de KG-Tanda0-Diez-r2b (a9631a64…), extracción final r2 guardada
- unidad: item; páginas [29, 30]; estado en E3 `aceptado_con_residuales`; en la cola: no; crudo que entra a E2: e1
- relación rechazada: índice 21 del crudo, `e6` `exceptua` `e1` (punto 6.5.5.8); validador de E1: firma_invalida: relations[21]: Excepcion --exceptua--> Operacion; vista por E3: no
- Excepcion `e6`: **Exclusión sucursales y subsidiarias de entidades financieras locales con supervisión consolidada** — Se excluyen de la clasificación en Irrecuperable las sucursales y subsidiarias de entidades financieras locales sujetas al régimen de supervisión consolidada | tramo: Sucursales y subsidiarias de entidades financieras locales sujetas al régimen de supervisión consolidada | punto 6.5.5.8 | marcado en texto propio
- Operacion `e1`: **Clasificación en categoría Irrecuperable** — Clasificación de bancos, otras instituciones financieras del exterior y otros prestatarios no radicados en el país en la categoría Irrecuperable cuando no cumplan con lo previsto en los puntos 3.1. y 3.2. de las normas sobre Evaluaciones crediticias | tramo: Bancos, otras instituciones financieras del exterior y otros prestatarios no radicados en el país que no cumplan con lo previsto en los puntos 3.1. y 3.2., según corresponda, de las normas sobre "Evaluaciones crediticias" | punto 6.5.5.8 | marcado en texto propio
- heredado, herencia[0] encabezado S6: Sección 6. Clasificación de los deudores de la cartera comercial.
- heredado, herencia[1] encabezado 6.5: 6.5. Niveles de clasificación.
- heredado, herencia[2] intro 6.5: Cada cliente, y la totalidad de sus financiaciones comprendidas, se incluirá en una de las si-
guientes cinco categorías, las que se definen teniendo en cuenta las condiciones que se deta-
llan en cada caso.
Los clientes que no registren asistencia crediticia de la entidad y que posteriormente reciban fi-
nanciaciones de ésta que no superen el importe resultante de aplicar sobre el saldo de deuda
registrado en el sistema financiero, según la última información disponible en la “Central de
deudores” a la fecha de su otorgamiento, el porcentaje establecido en el punto 2.2.5. de las
normas sobre “Previsiones mínimas por riesgo de incobrabilidad” correspondiente a la peor cla-
sificación asignada, podrán ser clasificados por la entidad teniendo en cuenta únicamente el
análisis del flujo de fondos proyectado. Las asistencias así otorgadas no serán consideradas a
los fines a que se refiere el punto 6.6.
A fin de verificar el cumplimiento de las obligaciones sin recurrir a nueva financiación directa o
indirecta o a refinanciaciones, no se considerarán refinanciaciones las facilidades adicionales
que se otorguen respecto de los márgenes vigentes acordados, siempre que el nuevo apoyo
crediticio implique nuevos desembolsos de fondos y no supere el 10 % del cupo asignado en
oportunidad de la última evaluación crediticia del cliente, en la medida en que éstas sean con-
sistentes con el curso normal de los negocios y exista capacidad para atender el resto de las
obligaciones financieras, ni las nuevas financiaciones y las refinanciaciones asociadas a una
mayor inversión derivada de la expansión de las actividades, y siempre que pueda demostrarse
que el flujo de fondos proyectado permitirá afrontar la totalidad de sus obligaciones.
Tampoco se considerarán dentro de ese concepto las refinanciaciones otorgadas a los produc-
tores agropecuarios cuando ello resulte de la aplicación de disposiciones vinculadas a la Ley de
Emergencia Agropecuaria, sin perjuicio de lo cual, a los fines de la clasificación, deberá tenerse
en cuenta el flujo de fondos proyectado para el momento en que concluya la vigencia de la
emergencia declarada. El tratamiento que se dispense en ese marco no podrá implicar mejora-
miento de la clasificación asignada al cliente en función de su situación individual, preexistente
a la emergencia, ni su aplicación extenderse más allá de la vigencia fijada para ella.
- heredado, herencia[3] encabezado 6.5.5: 6.5.5. Irrecuperable.
- heredado, herencia[4] intro 6.5.5: Las deudas de clientes incorporados a esta categoría se consideran incobrables. Si bien
estos activos podrían tener algún valor de recuperación bajo un cierto conjunto de cir-
cunstancias futuras, su incobrabilidad es evidente al momento del análisis.
Entre los indicadores que pueden reflejar esta situación se destacan que el cliente:
- heredado, herencia[5] cierre 6.5.5: Además, corresponderá clasificar en esta categoría a los clientes que, cualquiera sea el
motivo (entre ellos por no contar con legajo o por no haber proporcionado información
confiable y/o actualizada), no hayan sido evaluados con la periodicidad correspondiente,
con excepción de los deudores en concurso o con acuerdo preventivo extrajudicial solici-
tado o en gestión judicial que, por un período de hasta 540 días contados a partir de la
apertura del concurso, solicitud del acuerdo preventivo o inicio de las gestiones judiciales
de cobro, según corresponda, no hubiesen presentado la documentación que permita
realizarla, siempre que se cuente con informe de abogado de la entidad financiera
acreedora sobre la razonabilidad del recupero de los créditos comprendidos.
Ello, sin perjuicio de que se trate de deudas que reúnan todas las condiciones previstas
por el punto 2.2.3.2. de las normas sobre “Previsiones mínimas por riesgo de incobrabili-
dad”.
- texto propio:

```
6.5.5.8. ⟦O:Bancos, otras instituciones financieras del exterior y otros prestatarios no
radicados en el país que no cumplan con lo previsto en los puntos 3.1. y 3.2.,
según corresponda, de las normas sobre “Evaluaciones crediticias⟧”. A los
efectos del cumplimiento de los citados puntos se deberá contar con calificación
internacional de riesgo comprendida en la categoría “investment grade”.
Se excluirán:
a) Los siguientes deudores:
Casa matriz de las sucursales locales de bancos del exterior o sus filiales y
subsidiarias en otros países, en la medida en que aquélla esté sujeta a super-
visión sobre base consolidada.
Bancos u otras instituciones financieras del exterior sujetos a supervisión so-
bre base consolidada que ejerzan el control de entidades financieras locales
constituidas bajo la forma de sociedades anónimas.
Otros bancos del exterior autorizados a intervenir en los regímenes de conve-
nios de pagos y créditos recíprocos a los que haya adherido el BCRA, así co-
mo sus sucursales y subsidiarias, aun cuando ellas no estén comprendidas en
esos convenios, siempre que la casa matriz o entidad bancaria controlante es-
té sujeta a regímenes de supervisión sobre base consolidada, a satisfacción
de la SEFyC.
⟦E:Sucursales y subsidiarias de entidades financieras locales sujetas al régimen
de supervisión consolidada⟧.
b) Los deudores que únicamente registren las siguientes operaciones:
- Financiaciones que cuenten con aval de banco del exterior que cumpla con
lo previsto en el punto 3.1. de las normas sobre “Evaluaciones crediticias”,
requiriendo a ese efecto calificación internacional de riesgo comprendida en
la categoría “investment grade”.
- Financiaciones vinculadas a operaciones de compraventa de títulos valores
concertadas con residentes en el exterior, que se canalicen por la Caja de
Valores S.A., Clearstream, Euroclear o Depositary Trust Company (DTC), y
que se originen en el cumplimiento, por parte de la entidad financiera intervi-
niente, de la obligación a su cargo (entregar la especie transada o efectuar el
pago convenido) sin que la contraparte cancele su compromiso en el mismo
día, en razón de modalidades de liquidación usuales en esos mercados.
- Financiaciones vinculadas a operaciones de comercio exterior.
- Pases activos de dólares estadounidenses y de títulos valores públicos na-
cionales, siempre que:
 las especies transadas cuenten con un mercado de operaciones habitua-
les y relevantes,
 los precios pactados respondan a las condiciones del mercado y
 los márgenes de cobertura sean suficientes y se encuentren depositados
en los siguientes agentes de custodia o de registro:
* BCRA, por operaciones canalizadas a través de la Central de registro y
liquidación de instrumentos de deuda pública, regulación monetaria y fi-
deicomisos financieros (CRyL),
* Caja de Valores S.A.,
* Clearstream, Euroclear, Depositary Trust Company (DTC) y
- Asistencia crediticia concedida a través de las sucursales o subsidiarias en el
exterior de entidades financieras locales sujetas al régimen de supervisión
sobre base consolidada, siempre que se haya otorgado con recursos que no
provengan de fondos provistos, directa o indirectamente, por las entidades
financieras locales.
Los deudores excluidos precedentemente deberán ser clasificados y sus deudas
previsionadas conforme a las disposiciones de carácter general.
```

## EO10 — `cla::6.5.5.8`
- origen: crudo de KG-Tanda0-Diez-r2b (a9631a64…), extracción final r2 guardada
- unidad: item; páginas [29, 30]; estado en E3 `aceptado_con_residuales`; en la cola: no; crudo que entra a E2: e1
- relación rechazada: índice 22 del crudo, `e7` `exceptua` `e1` (punto 6.5.5.8); validador de E1: firma_invalida: relations[22]: Excepcion --exceptua--> Operacion; vista por E3: no
- Excepcion `e7`: **Exclusión financiaciones con aval de banco del exterior investment grade** — Se excluyen de la clasificación en Irrecuperable las financiaciones que cuenten con aval de banco del exterior que cumpla con lo previsto en el punto 3.1. de las normas sobre Evaluaciones crediticias, requiriendo calificación internacional de riesgo comprendida en la categoría investment grade | tramo: Financiaciones que cuenten con aval de banco del exterior que cumpla con lo previsto en el punto 3.1. de las normas sobre "Evaluaciones crediticias", requiriendo a ese efecto calificación internacional de riesgo comprendida en la categoría "investment grade" | punto 6.5.5.8 | marcado en texto propio
- Operacion `e1`: **Clasificación en categoría Irrecuperable** — Clasificación de bancos, otras instituciones financieras del exterior y otros prestatarios no radicados en el país en la categoría Irrecuperable cuando no cumplan con lo previsto en los puntos 3.1. y 3.2. de las normas sobre Evaluaciones crediticias | tramo: Bancos, otras instituciones financieras del exterior y otros prestatarios no radicados en el país que no cumplan con lo previsto en los puntos 3.1. y 3.2., según corresponda, de las normas sobre "Evaluaciones crediticias" | punto 6.5.5.8 | marcado en texto propio
- heredado, herencia[0] encabezado S6: Sección 6. Clasificación de los deudores de la cartera comercial.
- heredado, herencia[1] encabezado 6.5: 6.5. Niveles de clasificación.
- heredado, herencia[2] intro 6.5: Cada cliente, y la totalidad de sus financiaciones comprendidas, se incluirá en una de las si-
guientes cinco categorías, las que se definen teniendo en cuenta las condiciones que se deta-
llan en cada caso.
Los clientes que no registren asistencia crediticia de la entidad y que posteriormente reciban fi-
nanciaciones de ésta que no superen el importe resultante de aplicar sobre el saldo de deuda
registrado en el sistema financiero, según la última información disponible en la “Central de
deudores” a la fecha de su otorgamiento, el porcentaje establecido en el punto 2.2.5. de las
normas sobre “Previsiones mínimas por riesgo de incobrabilidad” correspondiente a la peor cla-
sificación asignada, podrán ser clasificados por la entidad teniendo en cuenta únicamente el
análisis del flujo de fondos proyectado. Las asistencias así otorgadas no serán consideradas a
los fines a que se refiere el punto 6.6.
A fin de verificar el cumplimiento de las obligaciones sin recurrir a nueva financiación directa o
indirecta o a refinanciaciones, no se considerarán refinanciaciones las facilidades adicionales
que se otorguen respecto de los márgenes vigentes acordados, siempre que el nuevo apoyo
crediticio implique nuevos desembolsos de fondos y no supere el 10 % del cupo asignado en
oportunidad de la última evaluación crediticia del cliente, en la medida en que éstas sean con-
sistentes con el curso normal de los negocios y exista capacidad para atender el resto de las
obligaciones financieras, ni las nuevas financiaciones y las refinanciaciones asociadas a una
mayor inversión derivada de la expansión de las actividades, y siempre que pueda demostrarse
que el flujo de fondos proyectado permitirá afrontar la totalidad de sus obligaciones.
Tampoco se considerarán dentro de ese concepto las refinanciaciones otorgadas a los produc-
tores agropecuarios cuando ello resulte de la aplicación de disposiciones vinculadas a la Ley de
Emergencia Agropecuaria, sin perjuicio de lo cual, a los fines de la clasificación, deberá tenerse
en cuenta el flujo de fondos proyectado para el momento en que concluya la vigencia de la
emergencia declarada. El tratamiento que se dispense en ese marco no podrá implicar mejora-
miento de la clasificación asignada al cliente en función de su situación individual, preexistente
a la emergencia, ni su aplicación extenderse más allá de la vigencia fijada para ella.
- heredado, herencia[3] encabezado 6.5.5: 6.5.5. Irrecuperable.
- heredado, herencia[4] intro 6.5.5: Las deudas de clientes incorporados a esta categoría se consideran incobrables. Si bien
estos activos podrían tener algún valor de recuperación bajo un cierto conjunto de cir-
cunstancias futuras, su incobrabilidad es evidente al momento del análisis.
Entre los indicadores que pueden reflejar esta situación se destacan que el cliente:
- heredado, herencia[5] cierre 6.5.5: Además, corresponderá clasificar en esta categoría a los clientes que, cualquiera sea el
motivo (entre ellos por no contar con legajo o por no haber proporcionado información
confiable y/o actualizada), no hayan sido evaluados con la periodicidad correspondiente,
con excepción de los deudores en concurso o con acuerdo preventivo extrajudicial solici-
tado o en gestión judicial que, por un período de hasta 540 días contados a partir de la
apertura del concurso, solicitud del acuerdo preventivo o inicio de las gestiones judiciales
de cobro, según corresponda, no hubiesen presentado la documentación que permita
realizarla, siempre que se cuente con informe de abogado de la entidad financiera
acreedora sobre la razonabilidad del recupero de los créditos comprendidos.
Ello, sin perjuicio de que se trate de deudas que reúnan todas las condiciones previstas
por el punto 2.2.3.2. de las normas sobre “Previsiones mínimas por riesgo de incobrabili-
dad”.
- texto propio:

```
6.5.5.8. ⟦O:Bancos, otras instituciones financieras del exterior y otros prestatarios no
radicados en el país que no cumplan con lo previsto en los puntos 3.1. y 3.2.,
según corresponda, de las normas sobre “Evaluaciones crediticias⟧”. A los
efectos del cumplimiento de los citados puntos se deberá contar con calificación
internacional de riesgo comprendida en la categoría “investment grade”.
Se excluirán:
a) Los siguientes deudores:
Casa matriz de las sucursales locales de bancos del exterior o sus filiales y
subsidiarias en otros países, en la medida en que aquélla esté sujeta a super-
visión sobre base consolidada.
Bancos u otras instituciones financieras del exterior sujetos a supervisión so-
bre base consolidada que ejerzan el control de entidades financieras locales
constituidas bajo la forma de sociedades anónimas.
Otros bancos del exterior autorizados a intervenir en los regímenes de conve-
nios de pagos y créditos recíprocos a los que haya adherido el BCRA, así co-
mo sus sucursales y subsidiarias, aun cuando ellas no estén comprendidas en
esos convenios, siempre que la casa matriz o entidad bancaria controlante es-
té sujeta a regímenes de supervisión sobre base consolidada, a satisfacción
de la SEFyC.
Sucursales y subsidiarias de entidades financieras locales sujetas al régimen
de supervisión consolidada.
b) Los deudores que únicamente registren las siguientes operaciones:
- ⟦E:Financiaciones que cuenten con aval de banco del exterior que cumpla con
lo previsto en el punto 3.1. de las normas sobre “Evaluaciones crediticias”,
requiriendo a ese efecto calificación internacional de riesgo comprendida en
la categoría “investment grade⟧”.
- Financiaciones vinculadas a operaciones de compraventa de títulos valores
concertadas con residentes en el exterior, que se canalicen por la Caja de
Valores S.A., Clearstream, Euroclear o Depositary Trust Company (DTC), y
que se originen en el cumplimiento, por parte de la entidad financiera intervi-
niente, de la obligación a su cargo (entregar la especie transada o efectuar el
pago convenido) sin que la contraparte cancele su compromiso en el mismo
día, en razón de modalidades de liquidación usuales en esos mercados.
- Financiaciones vinculadas a operaciones de comercio exterior.
- Pases activos de dólares estadounidenses y de títulos valores públicos na-
cionales, siempre que:
 las especies transadas cuenten con un mercado de operaciones habitua-
les y relevantes,
 los precios pactados respondan a las condiciones del mercado y
 los márgenes de cobertura sean suficientes y se encuentren depositados
en los siguientes agentes de custodia o de registro:
* BCRA, por operaciones canalizadas a través de la Central de registro y
liquidación de instrumentos de deuda pública, regulación monetaria y fi-
deicomisos financieros (CRyL),
* Caja de Valores S.A.,
* Clearstream, Euroclear, Depositary Trust Company (DTC) y
- Asistencia crediticia concedida a través de las sucursales o subsidiarias en el
exterior de entidades financieras locales sujetas al régimen de supervisión
sobre base consolidada, siempre que se haya otorgado con recursos que no
provengan de fondos provistos, directa o indirectamente, por las entidades
financieras locales.
Los deudores excluidos precedentemente deberán ser clasificados y sus deudas
previsionadas conforme a las disposiciones de carácter general.
```

## EO11 — `cla::6.5.5.8`
- origen: crudo de KG-Tanda0-Diez-r2b (a9631a64…), extracción final r2 guardada
- unidad: item; páginas [29, 30]; estado en E3 `aceptado_con_residuales`; en la cola: no; crudo que entra a E2: e1
- relación rechazada: índice 23 del crudo, `e8` `exceptua` `e1` (punto 6.5.5.8); validador de E1: firma_invalida: relations[23]: Excepcion --exceptua--> Operacion; vista por E3: no
- Excepcion `e8`: **Exclusión financiaciones vinculadas a compraventa de títulos valores con residentes exterior** — Se excluyen de la clasificación en Irrecuperable las financiaciones vinculadas a operaciones de compraventa de títulos valores concertadas con residentes en el exterior, canalizadas por Caja de Valores S.A., Clearstream, Euroclear o DTC, que se originen en el cumplimiento de obligaciones sin que la contraparte cancele su compromiso en el mismo día, por modalidades de liquidación usuales en esos mercados | tramo: Financiaciones vinculadas a operaciones de compraventa de títulos valores concertadas con residentes en el exterior, que se canalicen por la Caja de Valores S.A., Clearstream, Euroclear o Depositary Trust Company (DTC), y que se originen en el cumplimiento, por parte de la entidad financiera interviniente, de la obligación a su cargo (entregar la especie transada o efectuar el pago convenido) sin que la contraparte cancele su compromiso en el mismo día, en razón de modalidades de liquidación usuales en esos mercados | punto 6.5.5.8 | marcado en texto propio
- Operacion `e1`: **Clasificación en categoría Irrecuperable** — Clasificación de bancos, otras instituciones financieras del exterior y otros prestatarios no radicados en el país en la categoría Irrecuperable cuando no cumplan con lo previsto en los puntos 3.1. y 3.2. de las normas sobre Evaluaciones crediticias | tramo: Bancos, otras instituciones financieras del exterior y otros prestatarios no radicados en el país que no cumplan con lo previsto en los puntos 3.1. y 3.2., según corresponda, de las normas sobre "Evaluaciones crediticias" | punto 6.5.5.8 | marcado en texto propio
- heredado, herencia[0] encabezado S6: Sección 6. Clasificación de los deudores de la cartera comercial.
- heredado, herencia[1] encabezado 6.5: 6.5. Niveles de clasificación.
- heredado, herencia[2] intro 6.5: Cada cliente, y la totalidad de sus financiaciones comprendidas, se incluirá en una de las si-
guientes cinco categorías, las que se definen teniendo en cuenta las condiciones que se deta-
llan en cada caso.
Los clientes que no registren asistencia crediticia de la entidad y que posteriormente reciban fi-
nanciaciones de ésta que no superen el importe resultante de aplicar sobre el saldo de deuda
registrado en el sistema financiero, según la última información disponible en la “Central de
deudores” a la fecha de su otorgamiento, el porcentaje establecido en el punto 2.2.5. de las
normas sobre “Previsiones mínimas por riesgo de incobrabilidad” correspondiente a la peor cla-
sificación asignada, podrán ser clasificados por la entidad teniendo en cuenta únicamente el
análisis del flujo de fondos proyectado. Las asistencias así otorgadas no serán consideradas a
los fines a que se refiere el punto 6.6.
A fin de verificar el cumplimiento de las obligaciones sin recurrir a nueva financiación directa o
indirecta o a refinanciaciones, no se considerarán refinanciaciones las facilidades adicionales
que se otorguen respecto de los márgenes vigentes acordados, siempre que el nuevo apoyo
crediticio implique nuevos desembolsos de fondos y no supere el 10 % del cupo asignado en
oportunidad de la última evaluación crediticia del cliente, en la medida en que éstas sean con-
sistentes con el curso normal de los negocios y exista capacidad para atender el resto de las
obligaciones financieras, ni las nuevas financiaciones y las refinanciaciones asociadas a una
mayor inversión derivada de la expansión de las actividades, y siempre que pueda demostrarse
que el flujo de fondos proyectado permitirá afrontar la totalidad de sus obligaciones.
Tampoco se considerarán dentro de ese concepto las refinanciaciones otorgadas a los produc-
tores agropecuarios cuando ello resulte de la aplicación de disposiciones vinculadas a la Ley de
Emergencia Agropecuaria, sin perjuicio de lo cual, a los fines de la clasificación, deberá tenerse
en cuenta el flujo de fondos proyectado para el momento en que concluya la vigencia de la
emergencia declarada. El tratamiento que se dispense en ese marco no podrá implicar mejora-
miento de la clasificación asignada al cliente en función de su situación individual, preexistente
a la emergencia, ni su aplicación extenderse más allá de la vigencia fijada para ella.
- heredado, herencia[3] encabezado 6.5.5: 6.5.5. Irrecuperable.
- heredado, herencia[4] intro 6.5.5: Las deudas de clientes incorporados a esta categoría se consideran incobrables. Si bien
estos activos podrían tener algún valor de recuperación bajo un cierto conjunto de cir-
cunstancias futuras, su incobrabilidad es evidente al momento del análisis.
Entre los indicadores que pueden reflejar esta situación se destacan que el cliente:
- heredado, herencia[5] cierre 6.5.5: Además, corresponderá clasificar en esta categoría a los clientes que, cualquiera sea el
motivo (entre ellos por no contar con legajo o por no haber proporcionado información
confiable y/o actualizada), no hayan sido evaluados con la periodicidad correspondiente,
con excepción de los deudores en concurso o con acuerdo preventivo extrajudicial solici-
tado o en gestión judicial que, por un período de hasta 540 días contados a partir de la
apertura del concurso, solicitud del acuerdo preventivo o inicio de las gestiones judiciales
de cobro, según corresponda, no hubiesen presentado la documentación que permita
realizarla, siempre que se cuente con informe de abogado de la entidad financiera
acreedora sobre la razonabilidad del recupero de los créditos comprendidos.
Ello, sin perjuicio de que se trate de deudas que reúnan todas las condiciones previstas
por el punto 2.2.3.2. de las normas sobre “Previsiones mínimas por riesgo de incobrabili-
dad”.
- texto propio:

```
6.5.5.8. ⟦O:Bancos, otras instituciones financieras del exterior y otros prestatarios no
radicados en el país que no cumplan con lo previsto en los puntos 3.1. y 3.2.,
según corresponda, de las normas sobre “Evaluaciones crediticias⟧”. A los
efectos del cumplimiento de los citados puntos se deberá contar con calificación
internacional de riesgo comprendida en la categoría “investment grade”.
Se excluirán:
a) Los siguientes deudores:
Casa matriz de las sucursales locales de bancos del exterior o sus filiales y
subsidiarias en otros países, en la medida en que aquélla esté sujeta a super-
visión sobre base consolidada.
Bancos u otras instituciones financieras del exterior sujetos a supervisión so-
bre base consolidada que ejerzan el control de entidades financieras locales
constituidas bajo la forma de sociedades anónimas.
Otros bancos del exterior autorizados a intervenir en los regímenes de conve-
nios de pagos y créditos recíprocos a los que haya adherido el BCRA, así co-
mo sus sucursales y subsidiarias, aun cuando ellas no estén comprendidas en
esos convenios, siempre que la casa matriz o entidad bancaria controlante es-
té sujeta a regímenes de supervisión sobre base consolidada, a satisfacción
de la SEFyC.
Sucursales y subsidiarias de entidades financieras locales sujetas al régimen
de supervisión consolidada.
b) Los deudores que únicamente registren las siguientes operaciones:
- Financiaciones que cuenten con aval de banco del exterior que cumpla con
lo previsto en el punto 3.1. de las normas sobre “Evaluaciones crediticias”,
requiriendo a ese efecto calificación internacional de riesgo comprendida en
la categoría “investment grade”.
- ⟦E:Financiaciones vinculadas a operaciones de compraventa de títulos valores
concertadas con residentes en el exterior, que se canalicen por la Caja de
Valores S.A., Clearstream, Euroclear o Depositary Trust Company (DTC), y
que se originen en el cumplimiento, por parte de la entidad financiera intervi-
niente, de la obligación a su cargo (entregar la especie transada o efectuar el
pago convenido) sin que la contraparte cancele su compromiso en el mismo
día, en razón de modalidades de liquidación usuales en esos mercados⟧.
- Financiaciones vinculadas a operaciones de comercio exterior.
- Pases activos de dólares estadounidenses y de títulos valores públicos na-
cionales, siempre que:
 las especies transadas cuenten con un mercado de operaciones habitua-
les y relevantes,
 los precios pactados respondan a las condiciones del mercado y
 los márgenes de cobertura sean suficientes y se encuentren depositados
en los siguientes agentes de custodia o de registro:
* BCRA, por operaciones canalizadas a través de la Central de registro y
liquidación de instrumentos de deuda pública, regulación monetaria y fi-
deicomisos financieros (CRyL),
* Caja de Valores S.A.,
* Clearstream, Euroclear, Depositary Trust Company (DTC) y
- Asistencia crediticia concedida a través de las sucursales o subsidiarias en el
exterior de entidades financieras locales sujetas al régimen de supervisión
sobre base consolidada, siempre que se haya otorgado con recursos que no
provengan de fondos provistos, directa o indirectamente, por las entidades
financieras locales.
Los deudores excluidos precedentemente deberán ser clasificados y sus deudas
previsionadas conforme a las disposiciones de carácter general.
```

## EO12 — `cla::6.5.5.8`
- origen: crudo de KG-Tanda0-Diez-r2b (a9631a64…), extracción final r2 guardada
- unidad: item; páginas [29, 30]; estado en E3 `aceptado_con_residuales`; en la cola: no; crudo que entra a E2: e1
- relación rechazada: índice 24 del crudo, `e9` `exceptua` `e1` (punto 6.5.5.8); validador de E1: firma_invalida: relations[24]: Excepcion --exceptua--> Operacion; vista por E3: no
- Excepcion `e9`: **Exclusión financiaciones vinculadas a operaciones de comercio exterior** — Se excluyen de la clasificación en Irrecuperable las financiaciones vinculadas a operaciones de comercio exterior | tramo: Financiaciones vinculadas a operaciones de comercio exterior | punto 6.5.5.8 | marcado en texto propio
- Operacion `e1`: **Clasificación en categoría Irrecuperable** — Clasificación de bancos, otras instituciones financieras del exterior y otros prestatarios no radicados en el país en la categoría Irrecuperable cuando no cumplan con lo previsto en los puntos 3.1. y 3.2. de las normas sobre Evaluaciones crediticias | tramo: Bancos, otras instituciones financieras del exterior y otros prestatarios no radicados en el país que no cumplan con lo previsto en los puntos 3.1. y 3.2., según corresponda, de las normas sobre "Evaluaciones crediticias" | punto 6.5.5.8 | marcado en texto propio
- heredado, herencia[0] encabezado S6: Sección 6. Clasificación de los deudores de la cartera comercial.
- heredado, herencia[1] encabezado 6.5: 6.5. Niveles de clasificación.
- heredado, herencia[2] intro 6.5: Cada cliente, y la totalidad de sus financiaciones comprendidas, se incluirá en una de las si-
guientes cinco categorías, las que se definen teniendo en cuenta las condiciones que se deta-
llan en cada caso.
Los clientes que no registren asistencia crediticia de la entidad y que posteriormente reciban fi-
nanciaciones de ésta que no superen el importe resultante de aplicar sobre el saldo de deuda
registrado en el sistema financiero, según la última información disponible en la “Central de
deudores” a la fecha de su otorgamiento, el porcentaje establecido en el punto 2.2.5. de las
normas sobre “Previsiones mínimas por riesgo de incobrabilidad” correspondiente a la peor cla-
sificación asignada, podrán ser clasificados por la entidad teniendo en cuenta únicamente el
análisis del flujo de fondos proyectado. Las asistencias así otorgadas no serán consideradas a
los fines a que se refiere el punto 6.6.
A fin de verificar el cumplimiento de las obligaciones sin recurrir a nueva financiación directa o
indirecta o a refinanciaciones, no se considerarán refinanciaciones las facilidades adicionales
que se otorguen respecto de los márgenes vigentes acordados, siempre que el nuevo apoyo
crediticio implique nuevos desembolsos de fondos y no supere el 10 % del cupo asignado en
oportunidad de la última evaluación crediticia del cliente, en la medida en que éstas sean con-
sistentes con el curso normal de los negocios y exista capacidad para atender el resto de las
obligaciones financieras, ni las nuevas financiaciones y las refinanciaciones asociadas a una
mayor inversión derivada de la expansión de las actividades, y siempre que pueda demostrarse
que el flujo de fondos proyectado permitirá afrontar la totalidad de sus obligaciones.
Tampoco se considerarán dentro de ese concepto las refinanciaciones otorgadas a los produc-
tores agropecuarios cuando ello resulte de la aplicación de disposiciones vinculadas a la Ley de
Emergencia Agropecuaria, sin perjuicio de lo cual, a los fines de la clasificación, deberá tenerse
en cuenta el flujo de fondos proyectado para el momento en que concluya la vigencia de la
emergencia declarada. El tratamiento que se dispense en ese marco no podrá implicar mejora-
miento de la clasificación asignada al cliente en función de su situación individual, preexistente
a la emergencia, ni su aplicación extenderse más allá de la vigencia fijada para ella.
- heredado, herencia[3] encabezado 6.5.5: 6.5.5. Irrecuperable.
- heredado, herencia[4] intro 6.5.5: Las deudas de clientes incorporados a esta categoría se consideran incobrables. Si bien
estos activos podrían tener algún valor de recuperación bajo un cierto conjunto de cir-
cunstancias futuras, su incobrabilidad es evidente al momento del análisis.
Entre los indicadores que pueden reflejar esta situación se destacan que el cliente:
- heredado, herencia[5] cierre 6.5.5: Además, corresponderá clasificar en esta categoría a los clientes que, cualquiera sea el
motivo (entre ellos por no contar con legajo o por no haber proporcionado información
confiable y/o actualizada), no hayan sido evaluados con la periodicidad correspondiente,
con excepción de los deudores en concurso o con acuerdo preventivo extrajudicial solici-
tado o en gestión judicial que, por un período de hasta 540 días contados a partir de la
apertura del concurso, solicitud del acuerdo preventivo o inicio de las gestiones judiciales
de cobro, según corresponda, no hubiesen presentado la documentación que permita
realizarla, siempre que se cuente con informe de abogado de la entidad financiera
acreedora sobre la razonabilidad del recupero de los créditos comprendidos.
Ello, sin perjuicio de que se trate de deudas que reúnan todas las condiciones previstas
por el punto 2.2.3.2. de las normas sobre “Previsiones mínimas por riesgo de incobrabili-
dad”.
- texto propio:

```
6.5.5.8. ⟦O:Bancos, otras instituciones financieras del exterior y otros prestatarios no
radicados en el país que no cumplan con lo previsto en los puntos 3.1. y 3.2.,
según corresponda, de las normas sobre “Evaluaciones crediticias⟧”. A los
efectos del cumplimiento de los citados puntos se deberá contar con calificación
internacional de riesgo comprendida en la categoría “investment grade”.
Se excluirán:
a) Los siguientes deudores:
Casa matriz de las sucursales locales de bancos del exterior o sus filiales y
subsidiarias en otros países, en la medida en que aquélla esté sujeta a super-
visión sobre base consolidada.
Bancos u otras instituciones financieras del exterior sujetos a supervisión so-
bre base consolidada que ejerzan el control de entidades financieras locales
constituidas bajo la forma de sociedades anónimas.
Otros bancos del exterior autorizados a intervenir en los regímenes de conve-
nios de pagos y créditos recíprocos a los que haya adherido el BCRA, así co-
mo sus sucursales y subsidiarias, aun cuando ellas no estén comprendidas en
esos convenios, siempre que la casa matriz o entidad bancaria controlante es-
té sujeta a regímenes de supervisión sobre base consolidada, a satisfacción
de la SEFyC.
Sucursales y subsidiarias de entidades financieras locales sujetas al régimen
de supervisión consolidada.
b) Los deudores que únicamente registren las siguientes operaciones:
- Financiaciones que cuenten con aval de banco del exterior que cumpla con
lo previsto en el punto 3.1. de las normas sobre “Evaluaciones crediticias”,
requiriendo a ese efecto calificación internacional de riesgo comprendida en
la categoría “investment grade”.
- Financiaciones vinculadas a operaciones de compraventa de títulos valores
concertadas con residentes en el exterior, que se canalicen por la Caja de
Valores S.A., Clearstream, Euroclear o Depositary Trust Company (DTC), y
que se originen en el cumplimiento, por parte de la entidad financiera intervi-
niente, de la obligación a su cargo (entregar la especie transada o efectuar el
pago convenido) sin que la contraparte cancele su compromiso en el mismo
día, en razón de modalidades de liquidación usuales en esos mercados.
- ⟦E:Financiaciones vinculadas a operaciones de comercio exterior⟧.
- Pases activos de dólares estadounidenses y de títulos valores públicos na-
cionales, siempre que:
 las especies transadas cuenten con un mercado de operaciones habitua-
les y relevantes,
 los precios pactados respondan a las condiciones del mercado y
 los márgenes de cobertura sean suficientes y se encuentren depositados
en los siguientes agentes de custodia o de registro:
* BCRA, por operaciones canalizadas a través de la Central de registro y
liquidación de instrumentos de deuda pública, regulación monetaria y fi-
deicomisos financieros (CRyL),
* Caja de Valores S.A.,
* Clearstream, Euroclear, Depositary Trust Company (DTC) y
- Asistencia crediticia concedida a través de las sucursales o subsidiarias en el
exterior de entidades financieras locales sujetas al régimen de supervisión
sobre base consolidada, siempre que se haya otorgado con recursos que no
provengan de fondos provistos, directa o indirectamente, por las entidades
financieras locales.
Los deudores excluidos precedentemente deberán ser clasificados y sus deudas
previsionadas conforme a las disposiciones de carácter general.
```

## EO13 — `cla::6.5.5.8`
- origen: crudo de KG-Tanda0-Diez-r2b (a9631a64…), extracción final r2 guardada
- unidad: item; páginas [29, 30]; estado en E3 `aceptado_con_residuales`; en la cola: no; crudo que entra a E2: e1
- relación rechazada: índice 25 del crudo, `e10` `exceptua` `e1` (punto 6.5.5.8); validador de E1: firma_invalida: relations[25]: Excepcion --exceptua--> Operacion; vista por E3: no
- Excepcion `e10`: **Exclusión pases activos de dólares y títulos públicos nacionales** — Se excluyen de la clasificación en Irrecuperable los pases activos de dólares estadounidenses y de títulos valores públicos nacionales, siempre que las especies transadas cuenten con mercado de operaciones habituales y relevantes, los precios respondan a condiciones de mercado, los márgenes de cobertura sean suficientes y se encuentren depositados en BCRA (CRyL), Caja de Valores S.A., Clearstream, Euroclear o DTC | tramo: Pases activos de dólares estadounidenses y de títulos valores públicos nacionales, siempre que: las especies transadas cuenten con un mercado de operaciones habituales y relevantes, los precios pactados respondan a las condiciones del mercado y los márgenes de cobertura sean suficientes y se encuentren depositados en los siguientes agentes de custodia o de registro: BCRA, por operaciones canalizadas a través de la Central de registro y liquidación de instrumentos de deuda pública, regulación monetaria y fideicomisos financieros (CRyL), Caja de Valores S.A., Clearstream, Euroclear, Depositary Trust Company (DTC) | punto 6.5.5.8 | marcado en texto propio
- Operacion `e1`: **Clasificación en categoría Irrecuperable** — Clasificación de bancos, otras instituciones financieras del exterior y otros prestatarios no radicados en el país en la categoría Irrecuperable cuando no cumplan con lo previsto en los puntos 3.1. y 3.2. de las normas sobre Evaluaciones crediticias | tramo: Bancos, otras instituciones financieras del exterior y otros prestatarios no radicados en el país que no cumplan con lo previsto en los puntos 3.1. y 3.2., según corresponda, de las normas sobre "Evaluaciones crediticias" | punto 6.5.5.8 | marcado en texto propio
- heredado, herencia[0] encabezado S6: Sección 6. Clasificación de los deudores de la cartera comercial.
- heredado, herencia[1] encabezado 6.5: 6.5. Niveles de clasificación.
- heredado, herencia[2] intro 6.5: Cada cliente, y la totalidad de sus financiaciones comprendidas, se incluirá en una de las si-
guientes cinco categorías, las que se definen teniendo en cuenta las condiciones que se deta-
llan en cada caso.
Los clientes que no registren asistencia crediticia de la entidad y que posteriormente reciban fi-
nanciaciones de ésta que no superen el importe resultante de aplicar sobre el saldo de deuda
registrado en el sistema financiero, según la última información disponible en la “Central de
deudores” a la fecha de su otorgamiento, el porcentaje establecido en el punto 2.2.5. de las
normas sobre “Previsiones mínimas por riesgo de incobrabilidad” correspondiente a la peor cla-
sificación asignada, podrán ser clasificados por la entidad teniendo en cuenta únicamente el
análisis del flujo de fondos proyectado. Las asistencias así otorgadas no serán consideradas a
los fines a que se refiere el punto 6.6.
A fin de verificar el cumplimiento de las obligaciones sin recurrir a nueva financiación directa o
indirecta o a refinanciaciones, no se considerarán refinanciaciones las facilidades adicionales
que se otorguen respecto de los márgenes vigentes acordados, siempre que el nuevo apoyo
crediticio implique nuevos desembolsos de fondos y no supere el 10 % del cupo asignado en
oportunidad de la última evaluación crediticia del cliente, en la medida en que éstas sean con-
sistentes con el curso normal de los negocios y exista capacidad para atender el resto de las
obligaciones financieras, ni las nuevas financiaciones y las refinanciaciones asociadas a una
mayor inversión derivada de la expansión de las actividades, y siempre que pueda demostrarse
que el flujo de fondos proyectado permitirá afrontar la totalidad de sus obligaciones.
Tampoco se considerarán dentro de ese concepto las refinanciaciones otorgadas a los produc-
tores agropecuarios cuando ello resulte de la aplicación de disposiciones vinculadas a la Ley de
Emergencia Agropecuaria, sin perjuicio de lo cual, a los fines de la clasificación, deberá tenerse
en cuenta el flujo de fondos proyectado para el momento en que concluya la vigencia de la
emergencia declarada. El tratamiento que se dispense en ese marco no podrá implicar mejora-
miento de la clasificación asignada al cliente en función de su situación individual, preexistente
a la emergencia, ni su aplicación extenderse más allá de la vigencia fijada para ella.
- heredado, herencia[3] encabezado 6.5.5: 6.5.5. Irrecuperable.
- heredado, herencia[4] intro 6.5.5: Las deudas de clientes incorporados a esta categoría se consideran incobrables. Si bien
estos activos podrían tener algún valor de recuperación bajo un cierto conjunto de cir-
cunstancias futuras, su incobrabilidad es evidente al momento del análisis.
Entre los indicadores que pueden reflejar esta situación se destacan que el cliente:
- heredado, herencia[5] cierre 6.5.5: Además, corresponderá clasificar en esta categoría a los clientes que, cualquiera sea el
motivo (entre ellos por no contar con legajo o por no haber proporcionado información
confiable y/o actualizada), no hayan sido evaluados con la periodicidad correspondiente,
con excepción de los deudores en concurso o con acuerdo preventivo extrajudicial solici-
tado o en gestión judicial que, por un período de hasta 540 días contados a partir de la
apertura del concurso, solicitud del acuerdo preventivo o inicio de las gestiones judiciales
de cobro, según corresponda, no hubiesen presentado la documentación que permita
realizarla, siempre que se cuente con informe de abogado de la entidad financiera
acreedora sobre la razonabilidad del recupero de los créditos comprendidos.
Ello, sin perjuicio de que se trate de deudas que reúnan todas las condiciones previstas
por el punto 2.2.3.2. de las normas sobre “Previsiones mínimas por riesgo de incobrabili-
dad”.
- texto propio:

```
6.5.5.8. ⟦O:Bancos, otras instituciones financieras del exterior y otros prestatarios no
radicados en el país que no cumplan con lo previsto en los puntos 3.1. y 3.2.,
según corresponda, de las normas sobre “Evaluaciones crediticias⟧”. A los
efectos del cumplimiento de los citados puntos se deberá contar con calificación
internacional de riesgo comprendida en la categoría “investment grade”.
Se excluirán:
a) Los siguientes deudores:
Casa matriz de las sucursales locales de bancos del exterior o sus filiales y
subsidiarias en otros países, en la medida en que aquélla esté sujeta a super-
visión sobre base consolidada.
Bancos u otras instituciones financieras del exterior sujetos a supervisión so-
bre base consolidada que ejerzan el control de entidades financieras locales
constituidas bajo la forma de sociedades anónimas.
Otros bancos del exterior autorizados a intervenir en los regímenes de conve-
nios de pagos y créditos recíprocos a los que haya adherido el BCRA, así co-
mo sus sucursales y subsidiarias, aun cuando ellas no estén comprendidas en
esos convenios, siempre que la casa matriz o entidad bancaria controlante es-
té sujeta a regímenes de supervisión sobre base consolidada, a satisfacción
de la SEFyC.
Sucursales y subsidiarias de entidades financieras locales sujetas al régimen
de supervisión consolidada.
b) Los deudores que únicamente registren las siguientes operaciones:
- Financiaciones que cuenten con aval de banco del exterior que cumpla con
lo previsto en el punto 3.1. de las normas sobre “Evaluaciones crediticias”,
requiriendo a ese efecto calificación internacional de riesgo comprendida en
la categoría “investment grade”.
- Financiaciones vinculadas a operaciones de compraventa de títulos valores
concertadas con residentes en el exterior, que se canalicen por la Caja de
Valores S.A., Clearstream, Euroclear o Depositary Trust Company (DTC), y
que se originen en el cumplimiento, por parte de la entidad financiera intervi-
niente, de la obligación a su cargo (entregar la especie transada o efectuar el
pago convenido) sin que la contraparte cancele su compromiso en el mismo
día, en razón de modalidades de liquidación usuales en esos mercados.
- Financiaciones vinculadas a operaciones de comercio exterior.
- ⟦E:Pases activos de dólares estadounidenses y de títulos valores públicos na-
cionales, siempre que:
 las especies transadas cuenten con un mercado de operaciones habitua-
les y relevantes,
 los precios pactados respondan a las condiciones del mercado y
 los márgenes de cobertura sean suficientes y se encuentren depositados
en los siguientes agentes de custodia o de registro:
* BCRA, por operaciones canalizadas a través de la Central de registro y
liquidación de instrumentos de deuda pública, regulación monetaria y fi-
deicomisos financieros (CRyL),
* Caja de Valores S.A.,
* Clearstream, Euroclear, Depositary Trust Company (DTC⟧) y
- Asistencia crediticia concedida a través de las sucursales o subsidiarias en el
exterior de entidades financieras locales sujetas al régimen de supervisión
sobre base consolidada, siempre que se haya otorgado con recursos que no
provengan de fondos provistos, directa o indirectamente, por las entidades
financieras locales.
Los deudores excluidos precedentemente deberán ser clasificados y sus deudas
previsionadas conforme a las disposiciones de carácter general.
```

## EO14 — `cla::6.5.5.8`
- origen: crudo de KG-Tanda0-Diez-r2b (a9631a64…), extracción final r2 guardada
- unidad: item; páginas [29, 30]; estado en E3 `aceptado_con_residuales`; en la cola: no; crudo que entra a E2: e1
- relación rechazada: índice 26 del crudo, `e11` `exceptua` `e1` (punto 6.5.5.8); validador de E1: firma_invalida: relations[26]: Excepcion --exceptua--> Operacion; vista por E3: no
- Excepcion `e11`: **Exclusión asistencia crediticia a través de sucursales o subsidiarias en exterior** — Se excluyen de la clasificación en Irrecuperable la asistencia crediticia concedida a través de sucursales o subsidiarias en el exterior de entidades financieras locales sujetas a supervisión consolidada, siempre que se haya otorgado con recursos que no provengan de fondos provistos, directa o indirectamente, por las entidades financieras locales | tramo: Asistencia crediticia concedida a través de las sucursales o subsidiarias en el exterior de entidades financieras locales sujetas al régimen de supervisión sobre base consolidada, siempre que se haya otorgado con recursos que no provengan de fondos provistos, directa o indirectamente, por las entidades financieras locales | punto 6.5.5.8 | marcado en texto propio
- Operacion `e1`: **Clasificación en categoría Irrecuperable** — Clasificación de bancos, otras instituciones financieras del exterior y otros prestatarios no radicados en el país en la categoría Irrecuperable cuando no cumplan con lo previsto en los puntos 3.1. y 3.2. de las normas sobre Evaluaciones crediticias | tramo: Bancos, otras instituciones financieras del exterior y otros prestatarios no radicados en el país que no cumplan con lo previsto en los puntos 3.1. y 3.2., según corresponda, de las normas sobre "Evaluaciones crediticias" | punto 6.5.5.8 | marcado en texto propio
- heredado, herencia[0] encabezado S6: Sección 6. Clasificación de los deudores de la cartera comercial.
- heredado, herencia[1] encabezado 6.5: 6.5. Niveles de clasificación.
- heredado, herencia[2] intro 6.5: Cada cliente, y la totalidad de sus financiaciones comprendidas, se incluirá en una de las si-
guientes cinco categorías, las que se definen teniendo en cuenta las condiciones que se deta-
llan en cada caso.
Los clientes que no registren asistencia crediticia de la entidad y que posteriormente reciban fi-
nanciaciones de ésta que no superen el importe resultante de aplicar sobre el saldo de deuda
registrado en el sistema financiero, según la última información disponible en la “Central de
deudores” a la fecha de su otorgamiento, el porcentaje establecido en el punto 2.2.5. de las
normas sobre “Previsiones mínimas por riesgo de incobrabilidad” correspondiente a la peor cla-
sificación asignada, podrán ser clasificados por la entidad teniendo en cuenta únicamente el
análisis del flujo de fondos proyectado. Las asistencias así otorgadas no serán consideradas a
los fines a que se refiere el punto 6.6.
A fin de verificar el cumplimiento de las obligaciones sin recurrir a nueva financiación directa o
indirecta o a refinanciaciones, no se considerarán refinanciaciones las facilidades adicionales
que se otorguen respecto de los márgenes vigentes acordados, siempre que el nuevo apoyo
crediticio implique nuevos desembolsos de fondos y no supere el 10 % del cupo asignado en
oportunidad de la última evaluación crediticia del cliente, en la medida en que éstas sean con-
sistentes con el curso normal de los negocios y exista capacidad para atender el resto de las
obligaciones financieras, ni las nuevas financiaciones y las refinanciaciones asociadas a una
mayor inversión derivada de la expansión de las actividades, y siempre que pueda demostrarse
que el flujo de fondos proyectado permitirá afrontar la totalidad de sus obligaciones.
Tampoco se considerarán dentro de ese concepto las refinanciaciones otorgadas a los produc-
tores agropecuarios cuando ello resulte de la aplicación de disposiciones vinculadas a la Ley de
Emergencia Agropecuaria, sin perjuicio de lo cual, a los fines de la clasificación, deberá tenerse
en cuenta el flujo de fondos proyectado para el momento en que concluya la vigencia de la
emergencia declarada. El tratamiento que se dispense en ese marco no podrá implicar mejora-
miento de la clasificación asignada al cliente en función de su situación individual, preexistente
a la emergencia, ni su aplicación extenderse más allá de la vigencia fijada para ella.
- heredado, herencia[3] encabezado 6.5.5: 6.5.5. Irrecuperable.
- heredado, herencia[4] intro 6.5.5: Las deudas de clientes incorporados a esta categoría se consideran incobrables. Si bien
estos activos podrían tener algún valor de recuperación bajo un cierto conjunto de cir-
cunstancias futuras, su incobrabilidad es evidente al momento del análisis.
Entre los indicadores que pueden reflejar esta situación se destacan que el cliente:
- heredado, herencia[5] cierre 6.5.5: Además, corresponderá clasificar en esta categoría a los clientes que, cualquiera sea el
motivo (entre ellos por no contar con legajo o por no haber proporcionado información
confiable y/o actualizada), no hayan sido evaluados con la periodicidad correspondiente,
con excepción de los deudores en concurso o con acuerdo preventivo extrajudicial solici-
tado o en gestión judicial que, por un período de hasta 540 días contados a partir de la
apertura del concurso, solicitud del acuerdo preventivo o inicio de las gestiones judiciales
de cobro, según corresponda, no hubiesen presentado la documentación que permita
realizarla, siempre que se cuente con informe de abogado de la entidad financiera
acreedora sobre la razonabilidad del recupero de los créditos comprendidos.
Ello, sin perjuicio de que se trate de deudas que reúnan todas las condiciones previstas
por el punto 2.2.3.2. de las normas sobre “Previsiones mínimas por riesgo de incobrabili-
dad”.
- texto propio:

```
6.5.5.8. ⟦O:Bancos, otras instituciones financieras del exterior y otros prestatarios no
radicados en el país que no cumplan con lo previsto en los puntos 3.1. y 3.2.,
según corresponda, de las normas sobre “Evaluaciones crediticias⟧”. A los
efectos del cumplimiento de los citados puntos se deberá contar con calificación
internacional de riesgo comprendida en la categoría “investment grade”.
Se excluirán:
a) Los siguientes deudores:
Casa matriz de las sucursales locales de bancos del exterior o sus filiales y
subsidiarias en otros países, en la medida en que aquélla esté sujeta a super-
visión sobre base consolidada.
Bancos u otras instituciones financieras del exterior sujetos a supervisión so-
bre base consolidada que ejerzan el control de entidades financieras locales
constituidas bajo la forma de sociedades anónimas.
Otros bancos del exterior autorizados a intervenir en los regímenes de conve-
nios de pagos y créditos recíprocos a los que haya adherido el BCRA, así co-
mo sus sucursales y subsidiarias, aun cuando ellas no estén comprendidas en
esos convenios, siempre que la casa matriz o entidad bancaria controlante es-
té sujeta a regímenes de supervisión sobre base consolidada, a satisfacción
de la SEFyC.
Sucursales y subsidiarias de entidades financieras locales sujetas al régimen
de supervisión consolidada.
b) Los deudores que únicamente registren las siguientes operaciones:
- Financiaciones que cuenten con aval de banco del exterior que cumpla con
lo previsto en el punto 3.1. de las normas sobre “Evaluaciones crediticias”,
requiriendo a ese efecto calificación internacional de riesgo comprendida en
la categoría “investment grade”.
- Financiaciones vinculadas a operaciones de compraventa de títulos valores
concertadas con residentes en el exterior, que se canalicen por la Caja de
Valores S.A., Clearstream, Euroclear o Depositary Trust Company (DTC), y
que se originen en el cumplimiento, por parte de la entidad financiera intervi-
niente, de la obligación a su cargo (entregar la especie transada o efectuar el
pago convenido) sin que la contraparte cancele su compromiso en el mismo
día, en razón de modalidades de liquidación usuales en esos mercados.
- Financiaciones vinculadas a operaciones de comercio exterior.
- Pases activos de dólares estadounidenses y de títulos valores públicos na-
cionales, siempre que:
 las especies transadas cuenten con un mercado de operaciones habitua-
les y relevantes,
 los precios pactados respondan a las condiciones del mercado y
 los márgenes de cobertura sean suficientes y se encuentren depositados
en los siguientes agentes de custodia o de registro:
* BCRA, por operaciones canalizadas a través de la Central de registro y
liquidación de instrumentos de deuda pública, regulación monetaria y fi-
deicomisos financieros (CRyL),
* Caja de Valores S.A.,
* Clearstream, Euroclear, Depositary Trust Company (DTC) y
- ⟦E:Asistencia crediticia concedida a través de las sucursales o subsidiarias en el
exterior de entidades financieras locales sujetas al régimen de supervisión
sobre base consolidada, siempre que se haya otorgado con recursos que no
provengan de fondos provistos, directa o indirectamente, por las entidades
financieras locales⟧.
Los deudores excluidos precedentemente deberán ser clasificados y sus deudas
previsionadas conforme a las disposiciones de carácter general.
```

## EO15 — `cla::6.5.5::cierre`
- origen: crudo de KG-Tanda0-Diez-r2b (a9631a64…), extracción final r2 guardada
- unidad: cierre; páginas [31]; estado en E3 `aceptado_con_residuales`; en la cola: no; crudo que entra a E2: e1
- relación rechazada: índice 4 del crudo, `e2` `exceptua` `e1` (punto 6.5.5); validador de E1: firma_invalida: relations[4]: Excepcion --exceptua--> Operacion; vista por E3: no
- Excepcion `e2`: **Excepción deudores en concurso o acuerdo preventivo — hasta 540 días** — Quedan exceptuados de la clasificación en Irrecuperable los deudores en concurso, con acuerdo preventivo extrajudicial solicitado o en gestión judicial que, durante un período de hasta 540 días desde la apertura del concurso, solicitud del acuerdo o inicio de gestiones judiciales, no hayan presentado documentación para su evaluación, siempre que exista informe de abogado de la entidad financiera acreedora sobre la razonabilidad del recupero | tramo: con excepción de los deudores en concurso o con acuerdo preventivo extrajudicial solicitado o en gestión judicial que, por un período de hasta 540 días contados a partir de la apertura del concurso, solicitud del acuerdo preventivo o inicio de las gestiones judiciales de cobro, según corresponda, no hubiesen presentado la documentación que permita realizarla, siempre que se cuente con informe de abogado de la entidad financiera acreedora sobre la razonabilidad del recupero de los créditos comprendidos | punto 6.5.5 | marcado en texto propio
- Operacion `e1`: **Clasificación en categoría Irrecuperable por falta de evaluación** — Clasificación en la categoría Irrecuperable de clientes que no hayan sido evaluados con la periodicidad correspondiente, independientemente del motivo (falta de legajo, información no confiable o no actualizada) | tramo: corresponderá clasificar en esta categoría a los clientes que, cualquiera sea el motivo (entre ellos por no contar con legajo o por no haber proporcionado información confiable y/o actualizada), no hayan sido evaluados con la periodicidad correspondiente | punto 6.5.5 | marcado en texto propio
- heredado, herencia[0] encabezado S6: Sección 6. Clasificación de los deudores de la cartera comercial.
- heredado, herencia[1] encabezado 6.5: 6.5. Niveles de clasificación.
- heredado, herencia[2] encabezado 6.5.5: 6.5.5. Irrecuperable.
- texto propio:

```
Además, ⟦O:corresponderá clasificar en esta categoría a los clientes que, cualquiera sea el
motivo (entre ellos por no contar con legajo o por no haber proporcionado información
confiable y/o actualizada), no hayan sido evaluados con la periodicidad correspondiente⟧,
⟦E:con excepción de los deudores en concurso o con acuerdo preventivo extrajudicial solici-
tado o en gestión judicial que, por un período de hasta 540 días contados a partir de la
apertura del concurso, solicitud del acuerdo preventivo o inicio de las gestiones judiciales
de cobro, según corresponda, no hubiesen presentado la documentación que permita
realizarla, siempre que se cuente con informe de abogado de la entidad financiera
acreedora sobre la razonabilidad del recupero de los créditos comprendidos⟧.
Ello, sin perjuicio de que se trate de deudas que reúnan todas las condiciones previstas
por el punto 2.2.3.2. de las normas sobre “Previsiones mínimas por riesgo de incobrabili-
dad”.
```

## EO16 — `cap::5.2.3.2`
- origen: crudo de KG-Tanda0-Diez-r2b (a9631a64…), extracción final r2 guardada
- unidad: punto_no_item; páginas [101]; estado en E3 `aceptado_con_residuales`; en la cola: no; crudo que entra a E2: e1
- relación rechazada: índice 9 del crudo, `e7` `exceptua` `e6` (punto 5.2.3.2); validador de E1: firma_invalida: relations[9]: Excepcion --exceptua--> Operacion; vista por E3: no
- Excepcion `e7`: **Excepción — garantía que cubre únicamente capital** — Cuando la garantía cubre únicamente el capital, los intereses y otros pagos no cubiertos no están garantizados. | tramo: excepto cuando la garantía cubra únicamente el capital, en cuyo caso se considerará que los intereses y otros pagos no cubiertos no están garantizados | punto 5.2.3.2 | marcado en texto propio
- Operacion `e6`: **Cobertura de pagos del deudor por garantía** — El garante cubre cualquier pago que el deudor esté obligado a efectuar conforme a la documentación que regula la operación, incluyendo el importe nocional, la constitución de márgenes y otros pagos. | tramo: El garante cubre cualquier pago que el deudor esté obligado a efectuar en virtud de la documentación que regula la operación, como por ejemplo el importe nocional, la constitución de márgenes, etc. | punto 5.2.3.2 | marcado en texto propio
- heredado, herencia[0] encabezado S5: Sección 5. Cobertura del riesgo de crédito.
- heredado, herencia[1] chapeau_seccion S5: A los efectos del cómputo de la exigencia de capital por riesgo de crédito, se reconocerá –total o
parcialmente– la cobertura del riesgo de crédito (CRC) de las operaciones registradas en la cartera
de inversión –tales como préstamos y responsabilidades eventuales– mediante la utilización de las
técnicas previstas en el punto 5.1.
La presente sección contempla, además, el cálculo de la exposición a las operaciones de financia-
ción con títulos valores (securities financing transactions, SFT) –conforme a lo previsto en la Sec-
ción 4.–, registradas tanto en la cartera de inversión como en la cartera de negociación.
- heredado, herencia[2] encabezado 5.2: 5.2. Requisitos para la aplicación de técnicas de coberturas del riesgo de crédito.
- heredado, herencia[3] encabezado 5.2.3: 5.2.3. Requisitos para la aplicación de la técnica de cobertura mediante garantías (y contraga-
- heredado, herencia[4] intro 5.2.3: rantías) personales y derivados de crédito.
- texto propio:

```
5.2.3.2. Requisitos operativos específicos para las garantías (y contragarantías) perso-
nales –tales como fianzas y avales–.
i) En caso de incumplimiento de la contraparte, la entidad financiera puede
emprender acciones oportunas contra el garante con respecto a pagos pen-
dientes conforme a la documentación que regula la operación. El garante
puede realizar un pago único que cubra la totalidad del importe contemplado
en la documentación, o asumir el pago futuro de las obligaciones de la con-
traparte cubiertas por la garantía. La entidad financiera debe tener derecho
a recibir cualquiera de estos pagos del garante sin tener que iniciar acciones
legales frente a la contraparte para que abone sus deudas.
ii) La garantía es una obligación explícitamente documentada que asume el
garante.
iii) ⟦O:El garante cubre cualquier pago que el deudor esté obligado a efectuar en
virtud de la documentación que regula la operación, como por ejemplo el
importe nocional, la constitución de márgenes, etc⟧., ⟦E:excepto cuando la ga-
rantía cubra únicamente el capital, en cuyo caso se considerará que los in-
tereses y otros pagos no cubiertos no están garantizados⟧.
```

## EO17 — `cap::6.2.1.4`
- origen: crudo de KG-Tanda0-Diez-r2b (a9631a64…), extracción final r2 guardada
- unidad: punto_no_item; páginas [121, 122, 123]; estado en E3 `aceptado_tras_reintento`; en la cola: no; crudo que entra a E2: reintento_1:companero
- relación rechazada: índice 1 del crudo, `e2` `exceptua` `e1` (punto 6.2.1.4); validador de E1: firma_invalida: relations[1]: Excepcion --exceptua--> Operacion; vista por E3: no
- Excepcion `e2`: **Descalce de plazos permitido — swap de rendimiento total** — Se permite que exista descalce entre los plazos de vencimiento de la posición subyacente y del swap de rendimiento total, como excepción a la exigencia de coincidencia exacta. | tramo: Se admitirá que exista un descalce entre los plazos de vencimiento de la posición subyacente y del "swap" de rendimiento total. | punto 6.2.1.4 | marcado en texto propio
- Operacion `e1`: **Compensación íntegra de posiciones cubiertas con derivados de crédito** — Compensación íntegra de ambos lados de una operación (comprada y vendida) cuando los instrumentos sean idénticos o cuando una posición al contado comprada se cubra con un swap de rendimiento total (o viceversa) con coincidencia exacta de la obligación de referencia y la posición subyacente. | tramo: Se podrá compensar en forma íntegra ambos lados de una operación (comprada y vendida) cuando: a) los instrumentos de ambos lados sean idénticos; o b) un instrumento (posición al contado comprada) se cubra con un "swap" de rendimiento total, o viceversa, y coincidan exactamente la obligación de referencia del "swap" y la posición subyacente -es decir, la posición al contado-. | punto 6.2.1.4 | marcado en texto propio
- heredado, herencia[0] encabezado S6: Sección 6. Capital mínimo por riesgo de mercado.
- heredado, herencia[1] encabezado 6.2: 6.2. Exigencia de capital por riesgo de tasa de interés.
- heredado, herencia[2] intro 6.2: La exigencia de capital por el riesgo de tasa de interés se deberá calcular respecto de los títu-
los de deuda y otros instrumentos imputados a la cartera de negociación, incluidas las accio-
nes preferidas no convertibles.
Un título valor vendido y recomprado a término en una operación de pase pasivo o en otro tipo
de operación de financiación con títulos valores se tratará como si todavía fuese propiedad de
la entidad cedente; es decir, recibirá el mismo tratamiento que un título en cartera.
Las acciones preferidas convertibles a un precio predeterminado en acciones ordinarias de la
emisora se tratarán según cómo se negocien, como títulos de deuda o como acciones.
La exigencia se obtendrá como la suma de dos exigencias calculadas por separado: una por
el riesgo específico de cada instrumento, ya sea que se trate de una posición vendida o com-
prada, y otra por el riesgo general de mercado –vinculado al efecto de cambios en la tasa de
interés sobre la cartera–, en la que se podrán compensar las posiciones compradas y vendi-
das en diferentes instrumentos.
Para los instrumentos derivados, serán de aplicación las disposiciones establecidas en el pun-
to 6.2.3.
- heredado, herencia[3] encabezado 6.2.1: 6.2.1. Exigencia de capital por riesgo específico.
- heredado, herencia[4] intro 6.2.1: La exigencia de capital por riesgo específico tiene por objeto proteger a la entidad ante
movimientos adversos en el precio de un título causados por factores relacionados con
su emisor. Para su cálculo, sólo se permitirá netear las posiciones opuestas respecto de
una misma especie, incluidas las posiciones en derivados.
- texto propio:

```
6.2.1.4. Exigencia de capital por riesgo específico de posiciones cubiertas con deriva-
dos de crédito.
i) ⟦O:Se podrá compensar en forma íntegra ambos lados de una operación
(comprada y vendida) cuando:
a) los instrumentos de ambos lados sean idénticos; o
b) un instrumento (posición al contado comprada) se cubra con un “swap”
de rendimiento total, o viceversa, y coincidan exactamente la obliga-
ción de referencia del “swap” y la posición subyacente -es decir, la po-
sición al contado⟧-. ⟦E:Se admitirá que exista un descalce entre los plazos
de vencimiento de la posición subyacente y del “swap” de rendimiento
total⟧.
En estos casos, ningún lado de la operación estará sujeto a exigencia de
capital por riesgo específico.
ii) Se podrá compensar el riesgo específico cuando los valores de ambos la-
dos se muevan siempre en la dirección opuesta aunque no sustancialmente
en la misma medida y se verifique concurrentemente lo siguiente:
a) una posición al contado comprada se cubre con un “swap” de incum-
plimiento crediticio o con un instrumento con vinculación crediticia
(“credit linked note”), o viceversa;
b) coinciden exactamente la obligación de referencia, el plazo de ven-
cimiento de la obligación de referencia y del derivado de crédito y la
moneda de denominación de la posición subyacente;
c) las características básicas del derivado de crédito -tales como las defi-
niciones de los eventos de crédito, los mecanismos de liquidación,
etc.- no hagan que las variaciones del precio del derivado se desvíen
significativamente de las fluctuaciones del precio de la posición al con-
tado;
d) la operación transfiera riesgos, tomando en consideración el efecto de
las cláusulas que restringen la cobertura, tales como los pagos fijos y
los umbrales de significatividad.
En estos casos, se podrá compensar 80% del riesgo específico del lado de
la operación con la exigencia de capital más elevada, mientras que la exi-
gencia de capital por riesgo específico para el otro lado será cero.
iii) Se reconocerá una compensación parcial del riesgo específico cuando los
valores de ambos lados de la operación se correlacionen negativamente.
Esto ocurre cuando:
a) la posición es la indicada en el inciso b) del acápite i) y, si bien no
coinciden la obligación de referencia y la posición subyacente, satisfa-
ce las condiciones enunciadas en el inciso ii) del punto 5.2.3.3., o
b) la posición es la indicada en el inciso a) del acápite i) o en el acápite ii),
pero no coincide la moneda de denominación o el vencimiento de la
protección crediticia con los del activo subyacente –sin perjuicio de que
los descalces de monedas se deberán tomar en consideración a los
efectos de calcular la exigencia de capital por el riesgo por tipo de
cambio–, o
c) la posición es la indicada en el acápite ii), pero existe un descalce de
activos entre la posición al contado y el derivado de crédito. Sin em-
bargo, el activo de la posición al contado está incluido entre las obliga-
ciones que, de acuerdo con la documentación del derivado de crédito,
pueden ser entregadas por el comprador de la protección en caso de
ocurrir un evento crediticio.
iv)Un derivado de crédito de enésimo incumplimiento es el swap de incumpli-
miento crediticio en el cual el pago de la cobertura o indemnización aconte-
ce cuando tiene lugar el enésimo incumplimiento en una canasta de instru-
mentos de referencia subyacentes, luego de lo cual la operación se liquida y
termina.
a) La exigencia de capital por riesgo específico para un derivado de crédi-
to de primer incumplimiento será el menor de la suma de las exigen-
cias de capital por riesgo específico para los instrumentos de crédito
de referencia en la canasta y del máximo pago posible por un evento
crediticio previsto en el contrato.
Cuando la entidad tenga una posición en uno de los instrumentos de
crédito de referencia de un derivado de crédito de primer incumplimien-
to y el derivado le proporcione cobertura a la posición, podrá reducir
por hasta el importe cubierto las exigencias de capital por riesgo espe-
cífico tanto del instrumento de crédito como de la parte del derivado
que se relaciona con dicho instrumento.
Cuando la entidad tenga múltiples posiciones a riesgo en instrumentos
de crédito de referencia podrá efectuar dicha reducción sólo para el
instrumento de crédito de referencia que tenga la menor exigencia de
capital por riesgo específico.
b) La exigencia de capital por riesgo específico para un derivado de crédito
de enésimo incumplimiento con “n” mayor que 1 es el menor entre la su-
ma de las exigencias de capital por riesgo específico para los instrumen-
tos de crédito de referencia en la canasta –excluidas las (n-1) obligacio-
nes con las menores exigencias de capital por riesgo específico– y el
máximo pago posible por un evento crediticio previsto en el contrato. En
estos casos no se permite compensar las exigencias de capital por ries-
go específico.
c) Las entidades deberán calcular la exigencia de capital por cada posición
neta en derivados de crédito de enésimo incumplimiento independiente-
mente de que tengan una posición comprada o vendida; es decir, de si
obtienen o proveen protección.
En los casos enunciados en los acápites i) a iii), se tomará la mayor de las exi-
gencias de capital por riesgo específico de cada lado de la operación –esto es,
de la protección crediticia y del activo subyacente–. En los casos previstos en
el acápite iv), las entidades financieras deberán sumar la exigencia de capital
por riesgo específico de cada lado de la posición.
```

## EO18 — `cap::6.4.2.4`
- origen: crudo de KG-Tanda0-Diez-r2b (a9631a64…), extracción final r2 guardada
- unidad: punto_no_item; páginas [132]; estado en E3 `completo_ok_directo`; en la cola: no; crudo que entra a E2: e1
- relación rechazada: índice 3 del crudo, `e2` `exceptua` `e1` (punto 6.4.2.4); validador de E1: firma_invalida: relations[3]: Excepcion --exceptua--> Operacion; vista por E3: no
- Excepcion `e2`: **Excepción: valor actual neto con tasas de interés** — Cuando la entidad emplea valor actual neto para la gestión de posiciones, se utilizarán las tasas de interés y los tipos de cambio de contado corrientes en lugar de solo los tipos de cambio de contado | tramo: salvo que la entidad emplee para la gestión de dichas posiciones el valor actual neto, en cuyo caso se utilizarán las tasas de interés y los tipos de cambio de contado corrientes | punto 6.4.2.4 | marcado en texto propio
- Operacion `e1`: **Valuación de posiciones a término en moneda extranjera y oro** — Valuación de posiciones a término en moneda extranjera y en oro a los tipos de cambio de contado corrientes en el mercado | tramo: Las posiciones a término en moneda extranjera y en oro se valuarán a los tipos de cambio de contado corrientes en el mercado | punto 6.4.2.4 | marcado en texto propio
- heredado, herencia[0] encabezado S6: Sección 6. Capital mínimo por riesgo de mercado.
- heredado, herencia[1] encabezado 6.4: 6.4. Exigencia de capital por riesgo de tipo de cambio.
- heredado, herencia[2] intro 6.4: El presente punto establece el capital mínimo necesario para cubrir el riesgo de mantener po-
siciones en moneda extranjera, incluido el oro.
- heredado, herencia[3] encabezado 6.4.2: 6.4.2. Medición de la exposición en cada moneda.
- texto propio:

```
6.4.2.4. ⟦O:Las posiciones a término en moneda extranjera y en oro se valuarán a los tipos
de cambio de contado corrientes en el mercado⟧, ⟦E:salvo que la entidad emplee
para la gestión de dichas posiciones el valor actual neto, en cuyo caso se utili-
zarán las tasas de interés y los tipos de cambio de contado corrientes⟧.
Para determinar el importe de la posición abierta neta en cada moneda extran-
jera las entidades podrán excluir las posiciones comprendidas en las partidas
deducibles para determinar la responsabilidad patrimonial computable.
```

## EO19 — `ext::8.1`
- origen: crudo de KG-Tanda0-Diez-r2b (a9631a64…), extracción final r2 guardada
- unidad: punto_no_item; páginas [108]; estado en E3 `aceptado_con_residuales`; en la cola: no; crudo que entra a E2: e1
- relación rechazada: índice 3 del crudo, `e2` `exceptua` `e1` (punto 8.1); validador de E1: firma_invalida: relations[3]: Excepcion --exceptua--> Operacion; vista por E3: no
- Excepcion `e2`: **Excepción operaciones aduaneras punto 8.5.17** — Quedan exceptuadas del seguimiento las operaciones aduaneras detalladas en el punto 8.5.17. | tramo: excepto las operaciones aduaneras que se detallan en el punto 8.5.17 | punto 8.1 | marcado en texto propio
- Operacion `e1`: **Exportación de bienes con oficialización desde 02/09/19** — Exportaciones de bienes cuya oficialización se haya concretado a partir del 02/09/19 y que hayan obtenido el pertinente cumplido de embarque aduanero, alcanzadas por el seguimiento de negociaciones de divisas. | tramo: todas las exportaciones de bienes cuya oficialización se haya concretado a partir del 02/09/19 y que hayan obtenido el pertinente cumplido de embarque aduanero | punto 8.1 | marcado en texto propio
- heredado, herencia[0] encabezado S8: Sección 8. Seguimiento de las negociaciones de divisas por exportaciones de bienes
- texto propio:

```
8.1. Operaciones comprendidas.
Este seguimiento comprende a ⟦O:todas las exportaciones de bienes cuya oficialización se haya
concretado a partir del 02/09/19 y que hayan obtenido el pertinente cumplido de embarque
aduanero⟧, ⟦E:excepto las operaciones aduaneras que se detallan en el punto 8.5.17⟧.
Independientemente de que una exportación sea considerada como exceptuada del
seguimiento, si el exportador recibiera cobros por tal exportación, éstos también se
encontrarán alcanzados por la obligación de ingreso y liquidación de divisas.
```

## EO20 — `ext::8.5.17.4`
- origen: crudo de KG-Tanda0-Diez-r2b (a9631a64…), extracción final r2 guardada
- unidad: item; páginas [118]; estado en E3 `completo_ok_directo`; en la cola: no; crudo que entra a E2: e1
- relación rechazada: índice 2 del crudo, `e2` `exceptua` `e1` (punto 8.5.17.4); validador de E1: firma_invalida: relations[2]: Excepcion --exceptua--> Operacion; vista por E3: no
- Excepcion `e2`: **Excepción — franquicia diplomática del seguimiento** — Las operaciones aduaneras correspondientes al régimen de franquicia diplomática quedan exceptuadas del seguimiento de permisos de embarque por el valor que corresponda a ventajas aduaneras u otras situaciones previstas en el listado de operaciones aduaneras exceptuadas. | tramo: Régimen de franquicia diplomática (artículos 529 al 549 de la Ley 22.415) | punto 8.5.17.4 | marcado en texto propio
- Operacion `e1`: **Operación aduanera — régimen de franquicia diplomática** — Operación aduanera correspondiente al régimen de franquicia diplomática regulado en los artículos 529 al 549 de la Ley 22.415, exceptuada del seguimiento de permisos de embarque. | tramo: Régimen de franquicia diplomática (artículos 529 al 549 de la Ley 22.415) | punto 8.5.17.4 | marcado en texto propio
- heredado, herencia[0] encabezado S8: Sección 8. Seguimiento de las negociaciones de divisas por exportaciones de bienes
- heredado, herencia[1] encabezado 8.5: 8.5. Otras imputaciones admitidas en el cumplimiento del seguimiento.
- heredado, herencia[2] intro 8.5: La entidad podrá considerar cumplimentado parcial o totalmente el seguimiento de un permiso
de embarque cuando cuente con los elementos que le permitan considerar que la operación
se encuentra en alguna de las situaciones detalladas a continuación y se verifiquen las
condiciones previstas en cada caso.
La documentación utilizada para certificar el concepto y monto de las divisas imputado en
cada caso deberá quedar archivada en la entidad a disposición del BCRA.
- heredado, herencia[3] encabezado 8.5.17: 8.5.17. Operaciones aduaneras exceptuadas del seguimiento.
- heredado, herencia[4] intro 8.5.17: Por el valor que corresponda a ventajas aduaneras u otras situaciones previstas en el
siguiente listado de operaciones:
- texto propio:

```
8.5.17.4. ⟦O:⟦E:Régimen de franquicia diplomática (artículos 529 al 549 de la Ley 22.⟧415⟧).
```

## EO21 — `ext::8.5.17.5`
- origen: crudo de KG-Tanda0-Diez-r2b (a9631a64…), extracción final r2 guardada
- unidad: item; páginas [118]; estado en E3 `completo_ok_directo`; en la cola: no; crudo que entra a E2: e1
- relación rechazada: índice 2 del crudo, `e2` `exceptua` `e1` (punto 8.5.17.5); validador de E1: firma_invalida: relations[2]: Excepcion --exceptua--> Operacion; vista por E3: no
- Excepcion `e2`: **Excepción del seguimiento — régimen de muestras** — El régimen de muestras queda exceptuado del seguimiento de permisos de embarque | tramo: Régimen de muestras (artículos 560 al 565 de la Ley 22.415) | punto 8.5.17.5 | marcado en texto propio
- Operacion `e1`: **Régimen de muestras — operación aduanera** — Operación aduanera correspondiente al régimen de muestras conforme a los artículos 560 al 565 de la Ley 22.415 | tramo: Régimen de muestras (artículos 560 al 565 de la Ley 22.415) | punto 8.5.17.5 | marcado en texto propio
- heredado, herencia[0] encabezado S8: Sección 8. Seguimiento de las negociaciones de divisas por exportaciones de bienes
- heredado, herencia[1] encabezado 8.5: 8.5. Otras imputaciones admitidas en el cumplimiento del seguimiento.
- heredado, herencia[2] intro 8.5: La entidad podrá considerar cumplimentado parcial o totalmente el seguimiento de un permiso
de embarque cuando cuente con los elementos que le permitan considerar que la operación
se encuentra en alguna de las situaciones detalladas a continuación y se verifiquen las
condiciones previstas en cada caso.
La documentación utilizada para certificar el concepto y monto de las divisas imputado en
cada caso deberá quedar archivada en la entidad a disposición del BCRA.
- heredado, herencia[3] encabezado 8.5.17: 8.5.17. Operaciones aduaneras exceptuadas del seguimiento.
- heredado, herencia[4] intro 8.5.17: Por el valor que corresponda a ventajas aduaneras u otras situaciones previstas en el
siguiente listado de operaciones:
- texto propio:

```
8.5.17.5. ⟦O:⟦E:Régimen de muestras (artículos 560 al 565 de la Ley 22.⟧415⟧).
```

## EO22 — `ext::8.5.17.16`
- origen: crudo de KG-Tanda0-Diez-r2b (a9631a64…), extracción final r2 guardada
- unidad: item; páginas [118]; estado en E3 `completo_ok_directo`; en la cola: no; crudo que entra a E2: e1
- relación rechazada: índice 2 del crudo, `e2` `exceptua` `e1` (punto 8.5.17.16); validador de E1: firma_invalida: relations[2]: Excepcion --exceptua--> Operacion; vista por E3: no
- Excepcion `e2`: **Excepción seguimiento — exportaciones al Área aduanera especial** — Las exportaciones desde el Territorio Nacional Continental al Área aduanera especial quedan exceptuadas del seguimiento de permisos de embarque | tramo: Exportaciones desde el Territorio Nacional Continental al Área aduanera especial –art. 20 a) de la Ley 19.640– | punto 8.5.17.16 | marcado en texto propio
- Operacion `e1`: **Exportaciones al Área aduanera especial** — Exportaciones desde el Territorio Nacional Continental al Área aduanera especial conforme al artículo 20 a) de la Ley 19.640 | tramo: Exportaciones desde el Territorio Nacional Continental al Área aduanera especial –art. 20 a) de la Ley 19.640– | punto 8.5.17.16 | marcado en texto propio
- heredado, herencia[0] encabezado S8: Sección 8. Seguimiento de las negociaciones de divisas por exportaciones de bienes
- heredado, herencia[1] encabezado 8.5: 8.5. Otras imputaciones admitidas en el cumplimiento del seguimiento.
- heredado, herencia[2] intro 8.5: La entidad podrá considerar cumplimentado parcial o totalmente el seguimiento de un permiso
de embarque cuando cuente con los elementos que le permitan considerar que la operación
se encuentra en alguna de las situaciones detalladas a continuación y se verifiquen las
condiciones previstas en cada caso.
La documentación utilizada para certificar el concepto y monto de las divisas imputado en
cada caso deberá quedar archivada en la entidad a disposición del BCRA.
- heredado, herencia[3] encabezado 8.5.17: 8.5.17. Operaciones aduaneras exceptuadas del seguimiento.
- heredado, herencia[4] intro 8.5.17: Por el valor que corresponda a ventajas aduaneras u otras situaciones previstas en el
siguiente listado de operaciones:
- texto propio:

```
8.5.17.16. ⟦O:⟦E:Exportaciones desde el Territorio Nacional Continental al Área aduanera
especial –art. 20 a) de la Ley 19.⟧640⟧–.
```

## EO23 — `ext::8.5.17.25`
- origen: crudo de KG-Tanda0-Diez-r2b (a9631a64…), extracción final r2 guardada
- unidad: item; páginas [119]; estado en E3 `completo_ok_directo`; en la cola: no; crudo que entra a E2: e1
- relación rechazada: índice 2 del crudo, `e2` `exceptua` `e1` (punto 8.5.17.25); validador de E1: firma_invalida: relations[2]: Excepcion --exceptua--> Operacion; vista por E3: no
- Excepcion `e2`: **Excepción seguimiento — exportación automotores Ley 19.486** — Operación exceptuada del seguimiento de divisas por exportaciones: exportación a consumo de automotores de fabricación nacional, sus partes y piezas al amparo de la Ley 19.486 y del Decreto 5.529/72 | tramo: Exportación a consumo de automotores de fabricación nacional, sus partes y piezas al amparo de la Ley 19.486 y del Decreto 5.529/72 | punto 8.5.17.25 | marcado en texto propio
- Operacion `e1`: **Exportación a consumo automotores nacionales Ley 19.486** — Exportación a consumo de automotores de fabricación nacional, sus partes y piezas al amparo de la Ley 19.486 y del Decreto 5.529/72 | tramo: Exportación a consumo de automotores de fabricación nacional, sus partes y piezas al amparo de la Ley 19.486 y del Decreto 5.529/72 | punto 8.5.17.25 | marcado en texto propio
- heredado, herencia[0] encabezado S8: Sección 8. Seguimiento de las negociaciones de divisas por exportaciones de bienes
- heredado, herencia[1] encabezado 8.5: 8.5. Otras imputaciones admitidas en el cumplimiento del seguimiento.
- heredado, herencia[2] intro 8.5: La entidad podrá considerar cumplimentado parcial o totalmente el seguimiento de un permiso
de embarque cuando cuente con los elementos que le permitan considerar que la operación
se encuentra en alguna de las situaciones detalladas a continuación y se verifiquen las
condiciones previstas en cada caso.
La documentación utilizada para certificar el concepto y monto de las divisas imputado en
cada caso deberá quedar archivada en la entidad a disposición del BCRA.
- heredado, herencia[3] encabezado 8.5.17: 8.5.17. Operaciones aduaneras exceptuadas del seguimiento.
- heredado, herencia[4] intro 8.5.17: Por el valor que corresponda a ventajas aduaneras u otras situaciones previstas en el
siguiente listado de operaciones:
- texto propio:

```
8.5.17.25. ⟦O:⟦E:Exportación a consumo de automotores de fabricación nacional, sus
partes y piezas al amparo de la Ley 19.486 y del Decreto 5.529⟧/72⟧.
```

## EO24 — `ext::8.5.17.26`
- origen: crudo de KG-Tanda0-Diez-r2b (a9631a64…), extracción final r2 guardada
- unidad: item; páginas [119]; estado en E3 `completo_ok_directo`; en la cola: no; crudo que entra a E2: e1
- relación rechazada: índice 3 del crudo, `e2` `exceptua` `e1` (punto 8.5.17.26); validador de E1: firma_invalida: relations[3]: Excepcion --exceptua--> Operacion; vista por E3: no
- Excepcion `e2`: **Exceptuación seguimiento — exportaciones efectos personales** — Exceptúa del seguimiento de permisos de embarque las exportaciones de efectos personales que hacen a la profesión u oficio de personas humanas que fijan su residencia en el exterior, siempre que hayan sido autorizadas por la Aduana | tramo: Las exportaciones de efectos personales que hacen a la profesión u oficio de personas humanas que fijan su residencia en el exterior en la medida que dichas operaciones hayan sido autorizadas por la Aduana | punto 8.5.17.26 | marcado en texto propio
- Operacion `e1`: **Exportación efectos personales profesión u oficio** — Exportación de efectos personales que hacen a la profesión u oficio de personas humanas que fijan su residencia en el exterior, cuando hayan sido autorizadas por la Aduana | tramo: Las exportaciones de efectos personales que hacen a la profesión u oficio de personas humanas que fijan su residencia en el exterior | punto 8.5.17.26 | marcado en texto propio
- heredado, herencia[0] encabezado S8: Sección 8. Seguimiento de las negociaciones de divisas por exportaciones de bienes
- heredado, herencia[1] encabezado 8.5: 8.5. Otras imputaciones admitidas en el cumplimiento del seguimiento.
- heredado, herencia[2] intro 8.5: La entidad podrá considerar cumplimentado parcial o totalmente el seguimiento de un permiso
de embarque cuando cuente con los elementos que le permitan considerar que la operación
se encuentra en alguna de las situaciones detalladas a continuación y se verifiquen las
condiciones previstas en cada caso.
La documentación utilizada para certificar el concepto y monto de las divisas imputado en
cada caso deberá quedar archivada en la entidad a disposición del BCRA.
- heredado, herencia[3] encabezado 8.5.17: 8.5.17. Operaciones aduaneras exceptuadas del seguimiento.
- heredado, herencia[4] intro 8.5.17: Por el valor que corresponda a ventajas aduaneras u otras situaciones previstas en el
siguiente listado de operaciones:
- texto propio:

```
8.5.17.26. ⟦E:⟦O:Las exportaciones de efectos personales que hacen a la profesión u oficio
de personas humanas que fijan su residencia en el exterior⟧ en la medida
que dichas operaciones hayan sido autorizadas por la Ad⟧uana.
```

## EO25 — `ext::12.1`
- origen: crudo de KG-Tanda0-Diez-r2b (a9631a64…), extracción final r2 guardada
- unidad: punto_no_item; páginas [167]; estado en E3 `aceptado_con_residuales`; en la cola: no; crudo que entra a E2: e1
- relación rechazada: índice 5 del crudo, `exc4` `exceptua` `op4` (punto 12.1); validador de E1: firma_invalida: relations[5]: Excepcion --exceptua--> Operacion; vista por E3: no
- Excepcion `exc4`: **Excepción importación 8802.20.10 — empresas aeronavegación** — Quedan exceptuadas las importaciones de la posición NCM 8802.20.10 realizadas por empresas que presten servicios de aeronavegación | tramo: Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación. | punto 12.1 | marcado en texto propio
- Operacion `op4`: **Importación posición NCM 8802.20.10** — Importación de bienes clasificados en la posición arancelaria NCM 8802.20.10 | tramo: Posición NCM = 8802.20.10 | punto 12.1 | marcado en texto propio
- heredado, herencia[0] encabezado S12: Sección 12. Posiciones arancelarias de la NCM con tratamiento específico en las normas de importaciones de bienes.
- texto propio:

```
12.1. Posiciones arancelarias referidas en los puntos 10.10.2.1. y 10.10.2.2.
[TABLA ext::tabla000 | página 167 | e0_tablas | columnas]
Columnas: Posición NCM | Observaciones
Fila 1: Posición NCM = 8802.11.00
Fila 2: Posición NCM = 8802.12.10
Fila 3: Posición NCM = 8802.12.90
Fila 4: ⟦O:Posición NCM = 8802.20.10⟧ | Observaciones = ⟦E:Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación⟧.
Fila 5: Posición NCM = 8802.20.21 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 6: Posición NCM = 8802.20.22 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 7: Posición NCM = 8802.20.90 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 8: Posición NCM = 8802.30.10 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 9: Posición NCM = 8802.30.21 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 10: Posición NCM = 8802.30.29 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 11: Posición NCM = 8802.30.31 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 12: Posición NCM = 8802.30.39 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 13: Posición NCM = 8802.30.90 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 14: Posición NCM = 8802.40.10 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 15: Posición NCM = 8802.40.90 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
[FIN TABLA ext::tabla000]
```

## EO26 — `ext::12.1`
- origen: crudo de KG-Tanda0-Diez-r2b (a9631a64…), extracción final r2 guardada
- unidad: punto_no_item; páginas [167]; estado en E3 `aceptado_con_residuales`; en la cola: no; crudo que entra a E2: e1
- relación rechazada: índice 8 del crudo, `exc5` `exceptua` `op5` (punto 12.1); validador de E1: firma_invalida: relations[8]: Excepcion --exceptua--> Operacion; vista por E3: no
- Excepcion `exc5`: **Excepción importación 8802.20.21 — empresas aeronavegación** — Quedan exceptuadas las importaciones de la posición NCM 8802.20.21 realizadas por empresas que presten servicios de aeronavegación | tramo: Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación. | punto 12.1 | marcado en texto propio
- Operacion `op5`: **Importación posición NCM 8802.20.21** — Importación de bienes clasificados en la posición arancelaria NCM 8802.20.21 | tramo: Posición NCM = 8802.20.21 | punto 12.1 | marcado en texto propio
- heredado, herencia[0] encabezado S12: Sección 12. Posiciones arancelarias de la NCM con tratamiento específico en las normas de importaciones de bienes.
- texto propio:

```
12.1. Posiciones arancelarias referidas en los puntos 10.10.2.1. y 10.10.2.2.
[TABLA ext::tabla000 | página 167 | e0_tablas | columnas]
Columnas: Posición NCM | Observaciones
Fila 1: Posición NCM = 8802.11.00
Fila 2: Posición NCM = 8802.12.10
Fila 3: Posición NCM = 8802.12.90
Fila 4: Posición NCM = 8802.20.10 | Observaciones = ⟦E:Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación⟧.
Fila 5: ⟦O:Posición NCM = 8802.20.21⟧ | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 6: Posición NCM = 8802.20.22 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 7: Posición NCM = 8802.20.90 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 8: Posición NCM = 8802.30.10 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 9: Posición NCM = 8802.30.21 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 10: Posición NCM = 8802.30.29 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 11: Posición NCM = 8802.30.31 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 12: Posición NCM = 8802.30.39 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 13: Posición NCM = 8802.30.90 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 14: Posición NCM = 8802.40.10 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 15: Posición NCM = 8802.40.90 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
[FIN TABLA ext::tabla000]
```

## EO27 — `ext::12.1`
- origen: crudo de KG-Tanda0-Diez-r2b (a9631a64…), extracción final r2 guardada
- unidad: punto_no_item; páginas [167]; estado en E3 `aceptado_con_residuales`; en la cola: no; crudo que entra a E2: e1
- relación rechazada: índice 11 del crudo, `exc6` `exceptua` `op6` (punto 12.1); validador de E1: firma_invalida: relations[11]: Excepcion --exceptua--> Operacion; vista por E3: no
- Excepcion `exc6`: **Excepción importación 8802.20.22 — empresas aeronavegación** — Quedan exceptuadas las importaciones de la posición NCM 8802.20.22 realizadas por empresas que presten servicios de aeronavegación | tramo: Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación. | punto 12.1 | marcado en texto propio
- Operacion `op6`: **Importación posición NCM 8802.20.22** — Importación de bienes clasificados en la posición arancelaria NCM 8802.20.22 | tramo: Posición NCM = 8802.20.22 | punto 12.1 | marcado en texto propio
- heredado, herencia[0] encabezado S12: Sección 12. Posiciones arancelarias de la NCM con tratamiento específico en las normas de importaciones de bienes.
- texto propio:

```
12.1. Posiciones arancelarias referidas en los puntos 10.10.2.1. y 10.10.2.2.
[TABLA ext::tabla000 | página 167 | e0_tablas | columnas]
Columnas: Posición NCM | Observaciones
Fila 1: Posición NCM = 8802.11.00
Fila 2: Posición NCM = 8802.12.10
Fila 3: Posición NCM = 8802.12.90
Fila 4: Posición NCM = 8802.20.10 | Observaciones = ⟦E:Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación⟧.
Fila 5: Posición NCM = 8802.20.21 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 6: ⟦O:Posición NCM = 8802.20.22⟧ | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 7: Posición NCM = 8802.20.90 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 8: Posición NCM = 8802.30.10 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 9: Posición NCM = 8802.30.21 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 10: Posición NCM = 8802.30.29 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 11: Posición NCM = 8802.30.31 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 12: Posición NCM = 8802.30.39 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 13: Posición NCM = 8802.30.90 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 14: Posición NCM = 8802.40.10 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 15: Posición NCM = 8802.40.90 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
[FIN TABLA ext::tabla000]
```

## EO28 — `ext::12.1`
- origen: crudo de KG-Tanda0-Diez-r2b (a9631a64…), extracción final r2 guardada
- unidad: punto_no_item; páginas [167]; estado en E3 `aceptado_con_residuales`; en la cola: no; crudo que entra a E2: e1
- relación rechazada: índice 14 del crudo, `exc7` `exceptua` `op7` (punto 12.1); validador de E1: firma_invalida: relations[14]: Excepcion --exceptua--> Operacion; vista por E3: no
- Excepcion `exc7`: **Excepción importación 8802.20.90 — empresas aeronavegación** — Quedan exceptuadas las importaciones de la posición NCM 8802.20.90 realizadas por empresas que presten servicios de aeronavegación | tramo: Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación. | punto 12.1 | marcado en texto propio
- Operacion `op7`: **Importación posición NCM 8802.20.90** — Importación de bienes clasificados en la posición arancelaria NCM 8802.20.90 | tramo: Posición NCM = 8802.20.90 | punto 12.1 | marcado en texto propio
- heredado, herencia[0] encabezado S12: Sección 12. Posiciones arancelarias de la NCM con tratamiento específico en las normas de importaciones de bienes.
- texto propio:

```
12.1. Posiciones arancelarias referidas en los puntos 10.10.2.1. y 10.10.2.2.
[TABLA ext::tabla000 | página 167 | e0_tablas | columnas]
Columnas: Posición NCM | Observaciones
Fila 1: Posición NCM = 8802.11.00
Fila 2: Posición NCM = 8802.12.10
Fila 3: Posición NCM = 8802.12.90
Fila 4: Posición NCM = 8802.20.10 | Observaciones = ⟦E:Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación⟧.
Fila 5: Posición NCM = 8802.20.21 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 6: Posición NCM = 8802.20.22 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 7: ⟦O:Posición NCM = 8802.20.90⟧ | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 8: Posición NCM = 8802.30.10 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 9: Posición NCM = 8802.30.21 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 10: Posición NCM = 8802.30.29 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 11: Posición NCM = 8802.30.31 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 12: Posición NCM = 8802.30.39 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 13: Posición NCM = 8802.30.90 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 14: Posición NCM = 8802.40.10 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 15: Posición NCM = 8802.40.90 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
[FIN TABLA ext::tabla000]
```

## EO29 — `ext::12.1`
- origen: crudo de KG-Tanda0-Diez-r2b (a9631a64…), extracción final r2 guardada
- unidad: punto_no_item; páginas [167]; estado en E3 `aceptado_con_residuales`; en la cola: no; crudo que entra a E2: e1
- relación rechazada: índice 17 del crudo, `exc8` `exceptua` `op8` (punto 12.1); validador de E1: firma_invalida: relations[17]: Excepcion --exceptua--> Operacion; vista por E3: no
- Excepcion `exc8`: **Excepción importación 8802.30.10 — empresas aeronavegación** — Quedan exceptuadas las importaciones de la posición NCM 8802.30.10 realizadas por empresas que presten servicios de aeronavegación | tramo: Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación. | punto 12.1 | marcado en texto propio
- Operacion `op8`: **Importación posición NCM 8802.30.10** — Importación de bienes clasificados en la posición arancelaria NCM 8802.30.10 | tramo: Posición NCM = 8802.30.10 | punto 12.1 | marcado en texto propio
- heredado, herencia[0] encabezado S12: Sección 12. Posiciones arancelarias de la NCM con tratamiento específico en las normas de importaciones de bienes.
- texto propio:

```
12.1. Posiciones arancelarias referidas en los puntos 10.10.2.1. y 10.10.2.2.
[TABLA ext::tabla000 | página 167 | e0_tablas | columnas]
Columnas: Posición NCM | Observaciones
Fila 1: Posición NCM = 8802.11.00
Fila 2: Posición NCM = 8802.12.10
Fila 3: Posición NCM = 8802.12.90
Fila 4: Posición NCM = 8802.20.10 | Observaciones = ⟦E:Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación⟧.
Fila 5: Posición NCM = 8802.20.21 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 6: Posición NCM = 8802.20.22 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 7: Posición NCM = 8802.20.90 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 8: ⟦O:Posición NCM = 8802.30.10⟧ | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 9: Posición NCM = 8802.30.21 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 10: Posición NCM = 8802.30.29 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 11: Posición NCM = 8802.30.31 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 12: Posición NCM = 8802.30.39 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 13: Posición NCM = 8802.30.90 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 14: Posición NCM = 8802.40.10 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 15: Posición NCM = 8802.40.90 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
[FIN TABLA ext::tabla000]
```

## EO30 — `ext::12.1`
- origen: crudo de KG-Tanda0-Diez-r2b (a9631a64…), extracción final r2 guardada
- unidad: punto_no_item; páginas [167]; estado en E3 `aceptado_con_residuales`; en la cola: no; crudo que entra a E2: e1
- relación rechazada: índice 20 del crudo, `exc9` `exceptua` `op9` (punto 12.1); validador de E1: firma_invalida: relations[20]: Excepcion --exceptua--> Operacion; vista por E3: no
- Excepcion `exc9`: **Excepción importación 8802.30.21 — empresas aeronavegación** — Quedan exceptuadas las importaciones de la posición NCM 8802.30.21 realizadas por empresas que presten servicios de aeronavegación | tramo: Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación. | punto 12.1 | marcado en texto propio
- Operacion `op9`: **Importación posición NCM 8802.30.21** — Importación de bienes clasificados en la posición arancelaria NCM 8802.30.21 | tramo: Posición NCM = 8802.30.21 | punto 12.1 | marcado en texto propio
- heredado, herencia[0] encabezado S12: Sección 12. Posiciones arancelarias de la NCM con tratamiento específico en las normas de importaciones de bienes.
- texto propio:

```
12.1. Posiciones arancelarias referidas en los puntos 10.10.2.1. y 10.10.2.2.
[TABLA ext::tabla000 | página 167 | e0_tablas | columnas]
Columnas: Posición NCM | Observaciones
Fila 1: Posición NCM = 8802.11.00
Fila 2: Posición NCM = 8802.12.10
Fila 3: Posición NCM = 8802.12.90
Fila 4: Posición NCM = 8802.20.10 | Observaciones = ⟦E:Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación⟧.
Fila 5: Posición NCM = 8802.20.21 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 6: Posición NCM = 8802.20.22 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 7: Posición NCM = 8802.20.90 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 8: Posición NCM = 8802.30.10 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 9: ⟦O:Posición NCM = 8802.30.21⟧ | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 10: Posición NCM = 8802.30.29 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 11: Posición NCM = 8802.30.31 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 12: Posición NCM = 8802.30.39 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 13: Posición NCM = 8802.30.90 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 14: Posición NCM = 8802.40.10 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 15: Posición NCM = 8802.40.90 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
[FIN TABLA ext::tabla000]
```

## EO31 — `ext::12.1`
- origen: crudo de KG-Tanda0-Diez-r2b (a9631a64…), extracción final r2 guardada
- unidad: punto_no_item; páginas [167]; estado en E3 `aceptado_con_residuales`; en la cola: no; crudo que entra a E2: e1
- relación rechazada: índice 23 del crudo, `exc10` `exceptua` `op10` (punto 12.1); validador de E1: firma_invalida: relations[23]: Excepcion --exceptua--> Operacion; vista por E3: no
- Excepcion `exc10`: **Excepción importación 8802.30.29 — empresas aeronavegación** — Quedan exceptuadas las importaciones de la posición NCM 8802.30.29 realizadas por empresas que presten servicios de aeronavegación | tramo: Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación. | punto 12.1 | marcado en texto propio
- Operacion `op10`: **Importación posición NCM 8802.30.29** — Importación de bienes clasificados en la posición arancelaria NCM 8802.30.29 | tramo: Posición NCM = 8802.30.29 | punto 12.1 | marcado en texto propio
- heredado, herencia[0] encabezado S12: Sección 12. Posiciones arancelarias de la NCM con tratamiento específico en las normas de importaciones de bienes.
- texto propio:

```
12.1. Posiciones arancelarias referidas en los puntos 10.10.2.1. y 10.10.2.2.
[TABLA ext::tabla000 | página 167 | e0_tablas | columnas]
Columnas: Posición NCM | Observaciones
Fila 1: Posición NCM = 8802.11.00
Fila 2: Posición NCM = 8802.12.10
Fila 3: Posición NCM = 8802.12.90
Fila 4: Posición NCM = 8802.20.10 | Observaciones = ⟦E:Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación⟧.
Fila 5: Posición NCM = 8802.20.21 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 6: Posición NCM = 8802.20.22 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 7: Posición NCM = 8802.20.90 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 8: Posición NCM = 8802.30.10 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 9: Posición NCM = 8802.30.21 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 10: ⟦O:Posición NCM = 8802.30.29⟧ | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 11: Posición NCM = 8802.30.31 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 12: Posición NCM = 8802.30.39 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 13: Posición NCM = 8802.30.90 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 14: Posición NCM = 8802.40.10 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 15: Posición NCM = 8802.40.90 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
[FIN TABLA ext::tabla000]
```

## EO32 — `ext::12.1`
- origen: crudo de KG-Tanda0-Diez-r2b (a9631a64…), extracción final r2 guardada
- unidad: punto_no_item; páginas [167]; estado en E3 `aceptado_con_residuales`; en la cola: no; crudo que entra a E2: e1
- relación rechazada: índice 26 del crudo, `exc11` `exceptua` `op11` (punto 12.1); validador de E1: firma_invalida: relations[26]: Excepcion --exceptua--> Operacion; vista por E3: no
- Excepcion `exc11`: **Excepción importación 8802.30.31 — empresas aeronavegación** — Quedan exceptuadas las importaciones de la posición NCM 8802.30.31 realizadas por empresas que presten servicios de aeronavegación | tramo: Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación. | punto 12.1 | marcado en texto propio
- Operacion `op11`: **Importación posición NCM 8802.30.31** — Importación de bienes clasificados en la posición arancelaria NCM 8802.30.31 | tramo: Posición NCM = 8802.30.31 | punto 12.1 | marcado en texto propio
- heredado, herencia[0] encabezado S12: Sección 12. Posiciones arancelarias de la NCM con tratamiento específico en las normas de importaciones de bienes.
- texto propio:

```
12.1. Posiciones arancelarias referidas en los puntos 10.10.2.1. y 10.10.2.2.
[TABLA ext::tabla000 | página 167 | e0_tablas | columnas]
Columnas: Posición NCM | Observaciones
Fila 1: Posición NCM = 8802.11.00
Fila 2: Posición NCM = 8802.12.10
Fila 3: Posición NCM = 8802.12.90
Fila 4: Posición NCM = 8802.20.10 | Observaciones = ⟦E:Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación⟧.
Fila 5: Posición NCM = 8802.20.21 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 6: Posición NCM = 8802.20.22 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 7: Posición NCM = 8802.20.90 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 8: Posición NCM = 8802.30.10 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 9: Posición NCM = 8802.30.21 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 10: Posición NCM = 8802.30.29 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 11: ⟦O:Posición NCM = 8802.30.31⟧ | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 12: Posición NCM = 8802.30.39 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 13: Posición NCM = 8802.30.90 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 14: Posición NCM = 8802.40.10 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 15: Posición NCM = 8802.40.90 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
[FIN TABLA ext::tabla000]
```

## EO33 — `ext::12.1`
- origen: crudo de KG-Tanda0-Diez-r2b (a9631a64…), extracción final r2 guardada
- unidad: punto_no_item; páginas [167]; estado en E3 `aceptado_con_residuales`; en la cola: no; crudo que entra a E2: e1
- relación rechazada: índice 29 del crudo, `exc12` `exceptua` `op12` (punto 12.1); validador de E1: firma_invalida: relations[29]: Excepcion --exceptua--> Operacion; vista por E3: no
- Excepcion `exc12`: **Excepción importación 8802.30.39 — empresas aeronavegación** — Quedan exceptuadas las importaciones de la posición NCM 8802.30.39 realizadas por empresas que presten servicios de aeronavegación | tramo: Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación. | punto 12.1 | marcado en texto propio
- Operacion `op12`: **Importación posición NCM 8802.30.39** — Importación de bienes clasificados en la posición arancelaria NCM 8802.30.39 | tramo: Posición NCM = 8802.30.39 | punto 12.1 | marcado en texto propio
- heredado, herencia[0] encabezado S12: Sección 12. Posiciones arancelarias de la NCM con tratamiento específico en las normas de importaciones de bienes.
- texto propio:

```
12.1. Posiciones arancelarias referidas en los puntos 10.10.2.1. y 10.10.2.2.
[TABLA ext::tabla000 | página 167 | e0_tablas | columnas]
Columnas: Posición NCM | Observaciones
Fila 1: Posición NCM = 8802.11.00
Fila 2: Posición NCM = 8802.12.10
Fila 3: Posición NCM = 8802.12.90
Fila 4: Posición NCM = 8802.20.10 | Observaciones = ⟦E:Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación⟧.
Fila 5: Posición NCM = 8802.20.21 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 6: Posición NCM = 8802.20.22 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 7: Posición NCM = 8802.20.90 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 8: Posición NCM = 8802.30.10 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 9: Posición NCM = 8802.30.21 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 10: Posición NCM = 8802.30.29 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 11: Posición NCM = 8802.30.31 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 12: ⟦O:Posición NCM = 8802.30.39⟧ | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 13: Posición NCM = 8802.30.90 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 14: Posición NCM = 8802.40.10 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 15: Posición NCM = 8802.40.90 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
[FIN TABLA ext::tabla000]
```

## EO34 — `ext::12.1`
- origen: crudo de KG-Tanda0-Diez-r2b (a9631a64…), extracción final r2 guardada
- unidad: punto_no_item; páginas [167]; estado en E3 `aceptado_con_residuales`; en la cola: no; crudo que entra a E2: e1
- relación rechazada: índice 32 del crudo, `exc13` `exceptua` `op13` (punto 12.1); validador de E1: firma_invalida: relations[32]: Excepcion --exceptua--> Operacion; vista por E3: no
- Excepcion `exc13`: **Excepción importación 8802.30.90 — empresas aeronavegación** — Quedan exceptuadas las importaciones de la posición NCM 8802.30.90 realizadas por empresas que presten servicios de aeronavegación | tramo: Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación. | punto 12.1 | marcado en texto propio
- Operacion `op13`: **Importación posición NCM 8802.30.90** — Importación de bienes clasificados en la posición arancelaria NCM 8802.30.90 | tramo: Posición NCM = 8802.30.90 | punto 12.1 | marcado en texto propio
- heredado, herencia[0] encabezado S12: Sección 12. Posiciones arancelarias de la NCM con tratamiento específico en las normas de importaciones de bienes.
- texto propio:

```
12.1. Posiciones arancelarias referidas en los puntos 10.10.2.1. y 10.10.2.2.
[TABLA ext::tabla000 | página 167 | e0_tablas | columnas]
Columnas: Posición NCM | Observaciones
Fila 1: Posición NCM = 8802.11.00
Fila 2: Posición NCM = 8802.12.10
Fila 3: Posición NCM = 8802.12.90
Fila 4: Posición NCM = 8802.20.10 | Observaciones = ⟦E:Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación⟧.
Fila 5: Posición NCM = 8802.20.21 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 6: Posición NCM = 8802.20.22 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 7: Posición NCM = 8802.20.90 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 8: Posición NCM = 8802.30.10 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 9: Posición NCM = 8802.30.21 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 10: Posición NCM = 8802.30.29 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 11: Posición NCM = 8802.30.31 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 12: Posición NCM = 8802.30.39 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 13: ⟦O:Posición NCM = 8802.30.90⟧ | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 14: Posición NCM = 8802.40.10 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 15: Posición NCM = 8802.40.90 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
[FIN TABLA ext::tabla000]
```

## EO35 — `ext::12.1`
- origen: crudo de KG-Tanda0-Diez-r2b (a9631a64…), extracción final r2 guardada
- unidad: punto_no_item; páginas [167]; estado en E3 `aceptado_con_residuales`; en la cola: no; crudo que entra a E2: e1
- relación rechazada: índice 35 del crudo, `exc14` `exceptua` `op14` (punto 12.1); validador de E1: firma_invalida: relations[35]: Excepcion --exceptua--> Operacion; vista por E3: no
- Excepcion `exc14`: **Excepción importación 8802.40.10 — empresas aeronavegación** — Quedan exceptuadas las importaciones de la posición NCM 8802.40.10 realizadas por empresas que presten servicios de aeronavegación | tramo: Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación. | punto 12.1 | marcado en texto propio
- Operacion `op14`: **Importación posición NCM 8802.40.10** — Importación de bienes clasificados en la posición arancelaria NCM 8802.40.10 | tramo: Posición NCM = 8802.40.10 | punto 12.1 | marcado en texto propio
- heredado, herencia[0] encabezado S12: Sección 12. Posiciones arancelarias de la NCM con tratamiento específico en las normas de importaciones de bienes.
- texto propio:

```
12.1. Posiciones arancelarias referidas en los puntos 10.10.2.1. y 10.10.2.2.
[TABLA ext::tabla000 | página 167 | e0_tablas | columnas]
Columnas: Posición NCM | Observaciones
Fila 1: Posición NCM = 8802.11.00
Fila 2: Posición NCM = 8802.12.10
Fila 3: Posición NCM = 8802.12.90
Fila 4: Posición NCM = 8802.20.10 | Observaciones = ⟦E:Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación⟧.
Fila 5: Posición NCM = 8802.20.21 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 6: Posición NCM = 8802.20.22 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 7: Posición NCM = 8802.20.90 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 8: Posición NCM = 8802.30.10 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 9: Posición NCM = 8802.30.21 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 10: Posición NCM = 8802.30.29 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 11: Posición NCM = 8802.30.31 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 12: Posición NCM = 8802.30.39 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 13: Posición NCM = 8802.30.90 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 14: ⟦O:Posición NCM = 8802.40.10⟧ | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 15: Posición NCM = 8802.40.90 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
[FIN TABLA ext::tabla000]
```

## EO36 — `ext::12.1`
- origen: crudo de KG-Tanda0-Diez-r2b (a9631a64…), extracción final r2 guardada
- unidad: punto_no_item; páginas [167]; estado en E3 `aceptado_con_residuales`; en la cola: no; crudo que entra a E2: e1
- relación rechazada: índice 38 del crudo, `exc15` `exceptua` `op15` (punto 12.1); validador de E1: firma_invalida: relations[38]: Excepcion --exceptua--> Operacion; vista por E3: no
- Excepcion `exc15`: **Excepción importación 8802.40.90 — empresas aeronavegación** — Quedan exceptuadas las importaciones de la posición NCM 8802.40.90 realizadas por empresas que presten servicios de aeronavegación | tramo: Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación. | punto 12.1 | marcado en texto propio
- Operacion `op15`: **Importación posición NCM 8802.40.90** — Importación de bienes clasificados en la posición arancelaria NCM 8802.40.90 | tramo: Posición NCM = 8802.40.90 | punto 12.1 | marcado en texto propio
- heredado, herencia[0] encabezado S12: Sección 12. Posiciones arancelarias de la NCM con tratamiento específico en las normas de importaciones de bienes.
- texto propio:

```
12.1. Posiciones arancelarias referidas en los puntos 10.10.2.1. y 10.10.2.2.
[TABLA ext::tabla000 | página 167 | e0_tablas | columnas]
Columnas: Posición NCM | Observaciones
Fila 1: Posición NCM = 8802.11.00
Fila 2: Posición NCM = 8802.12.10
Fila 3: Posición NCM = 8802.12.90
Fila 4: Posición NCM = 8802.20.10 | Observaciones = ⟦E:Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación⟧.
Fila 5: Posición NCM = 8802.20.21 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 6: Posición NCM = 8802.20.22 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 7: Posición NCM = 8802.20.90 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 8: Posición NCM = 8802.30.10 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 9: Posición NCM = 8802.30.21 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 10: Posición NCM = 8802.30.29 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 11: Posición NCM = 8802.30.31 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 12: Posición NCM = 8802.30.39 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 13: Posición NCM = 8802.30.90 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 14: Posición NCM = 8802.40.10 | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
Fila 15: ⟦O:Posición NCM = 8802.40.90⟧ | Observaciones = Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación.
[FIN TABLA ext::tabla000]
```

## EO37 — `ctacte::4.2.2.6`
- origen: crudo de KG-Tanda0-Diez-r2b (a9631a64…), extracción final r2 guardada
- unidad: punto_no_item; páginas [27]; estado en E3 `aceptado_con_residuales`; en la cola: no; crudo que entra a E2: e1
- relación rechazada: índice 7 del crudo, `e2` `exceptua` `e1` (punto 4.2.2.6); validador de E1: firma_invalida: relations[7]: Excepcion --exceptua--> Operacion; vista por E3: no
- Excepcion `e2`: **Excepción — aval de la entidad** — No se devuelve el documento cuando la entidad otorgante otorga su aval al cheque. | tramo: salvo que la entidad otorgue su aval | punto 4.2.2.6 | marcado en texto propio
- Operacion `e1`: **Devolución de documento registrado** — Devolución del documento de cheque de pago diferido una vez efectuada su registración, con constancia que acredite la circunstancia mediante leyenda que incluya fecha de registro y firmas de funcionarios autorizados responsables. | tramo: se devolverá el documento | punto 4.2.2.6 | marcado en texto propio
- heredado, herencia[0] encabezado S4: Sección 4. Cheques de pago diferido.
- heredado, herencia[1] encabezado 4.2: 4.2. Registración de cheques librados en formato papel.
- heredado, herencia[2] intro 4.2: Una vez emitidos podrán ser presentados a registro hasta el día anterior a su vencimiento. En
caso de que esa presentación se efectúe en alguno de los 14 días corridos inmediatos anterio-
res al vencimiento, mantienen vigencia el procedimiento y los plazos previstos en el punto
4.2.2.4.
- heredado, herencia[3] encabezado 4.2.2: 4.2.2. Procedimiento.
- texto propio:

```
4.2.2.6. Efectuada la registración, ⟦O:se devolverá el documento⟧ –⟦E:salvo que la entidad otor-
gue su aval⟧– con la constancia que acredite tal circunstancia, mediante una le-
yenda que incluya:
i) Registrado –sin aval– con fecha .../.../..., artículo 57 de la Ley de Cheques.
ii)Dos firmas –con sus pertinentes aclaraciones– de funcionarios autorizados
responsables que comprometan a la entidad.
```

## EO38 — `ctacte::6.3.3`
- origen: crudo de KG-Tanda0-Diez-r2b (a9631a64…), extracción final r2 guardada
- unidad: item; páginas [36]; estado en E3 `completo_ok_directo`; en la cola: no; crudo que entra a E2: e1
- relación rechazada: índice 7 del crudo, `e4` `exceptua` `e1` (punto 6.3.3); validador de E1: firma_invalida: relations[7]: Excepcion --exceptua--> Operacion; vista por E3: no
- Excepcion `e4`: **Excepción cheques emitidos antes de notificación de cierre** — Los cheques emitidos con anterioridad a la pertinente notificación de cierre serán devueltos sin registrar, pero ello no se considerará rechazo a la registración y, por lo tanto, no deberá informarse al Banco Central de la República Argentina por ese motivo, ni dará lugar a la aplicación de multas. | tramo: Los cheques emitidos con anterioridad a la pertinente notificación de cierre serán devueltos sin registrar, pero ello no se considerará rechazo a la registración | punto 6.3.3 | marcado en texto propio
- Operacion `e1`: **Rechazo de registración de cheques de pago diferido** — Rechazo de la registración de cheques de pago diferido presentados a registro cuando la cuenta corriente se encuentre cerrada o exista suspensión del servicio de pago de cheques en forma previa a ello, exclusivamente en las condiciones a que se refiere la presente reglamentación, y se trate de cheques emitidos con posterioridad a la pertinente notificación de cierre. | tramo: rechazarse la registración de los cheques de pago diferido presentados a registro | punto 6.3 | marcado en herencia[2] intro 6.3
- heredado, herencia[0] encabezado S6: Sección 6. Rechazo de cheques.
- heredado, herencia[1] encabezado 6.3: 6.3. Causales de no registración.
- heredado, herencia[2] intro 6.3: Deberá ⟦O:rechazarse la registración de los cheques de pago diferido presentados a registro⟧
cuando:
- texto propio:

```
6.3.3. La cuenta corriente se encuentre cerrada o exista suspensión del servicio de pago de
cheques en forma previa a ello -exclusivamente en las condiciones a que se refiere la
presente reglamentación- y se trate de cheques emitidos con posterioridad a la pertinen-
te notificación de cierre.
⟦E:Los cheques emitidos con anterioridad a la pertinente notificación de cierre serán devuel-
tos sin registrar, pero ello no se considerará rechazo a la registración⟧ y, por lo tanto, no
deberá informarse al Banco Central de la República Argentina por ese motivo, ni dará lu-
gar a la aplicación de multas.
La leyenda a colocar en estos últimos casos será "Devuelto sin registrar por cuenta ce-
rrada. Art. 60 Ley de Cheques".
```

## EO39 — `ctacte::6.4.6.5`
- origen: crudo de KG-Tanda0-Diez-r2b (a9631a64…), extracción final r2 guardada
- unidad: item; páginas [38]; estado en E3 `aceptado_tras_reintento`; en la cola: no; crudo que entra a E2: reintento_1:companero
- relación rechazada: índice 3 del crudo, `e2` `exceptua` `e1` (punto 6.4.6.5); validador de E1: firma_invalida: relations[3]: Excepcion --exceptua--> Operacion; vista por E3: no
- Excepcion `e2`: **Excepción — concurso preventivo del librador** — No corresponde comunicar al BCRA los rechazos cuando se ha declarado judicialmente el concurso preventivo del librador, siempre que se trate de cheques de pago diferido emitidos hasta el día anterior a la presentación de la solicitud de apertura del proceso y su fecha de pago sea posterior a ella | tramo: Haberse declarado judicialmente el concurso preventivo del librador y siempre que se trate de cheques de pago diferido emitidos hasta el día anterior a la fecha de presentación de la solicitud de apertura de ese proceso y su fecha de pago sea posterior a ella | punto 6.4.6.5 | marcado en texto propio
- Operacion `e1`: **Comunicación al BCRA de rechazos de cheques** — Comunicación al BCRA de los rechazos de cheques | tramo: No corresponderá la comunicación al BCRA de los rechazos | punto 6.4.6 | marcado en herencia[2] encabezado 6.4.6
- heredado, herencia[0] encabezado S6: Sección 6. Rechazo de cheques.
- heredado, herencia[1] encabezado 6.4: 6.4. Procedimiento.
- heredado, herencia[2] encabezado 6.4.6: 6.4.6. ⟦O:No corresponderá la comunicación al BCRA de los rechazos⟧ motivados por:
- texto propio:

```
6.4.6.5. ⟦E:Haberse declarado judicialmente el concurso preventivo del librador y siempre
que se trate de cheques de pago diferido emitidos hasta el día anterior a la fecha
de presentación de la solicitud de apertura de ese proceso y su fecha de pago
sea posterior a ella⟧.
Además, en los casos de los puntos 6.4.6.2. a 6.4.6.4. los rechazos no se comunicarán única-
mente en los casos en que hubiera sido posible atenderlos con el saldo existente en la cuenta
de no haberse efectivizado el pago, incurrido en el error o dispuesta la medida cautelar.
```

## EO40 — `ctacte::9.1.2.1`
- origen: crudo de KG-Tanda0-Diez-r2b (a9631a64…), extracción final r2 guardada
- unidad: punto_no_item; páginas [49]; estado en E3 `aceptado_con_residuales`; en la cola: no; crudo que entra a E2: e1
- relación rechazada: índice 8 del crudo, `e4` `exceptua` `e1` (punto 9.1.2.1); validador de E1: firma_invalida: relations[8]: Excepcion --exceptua--> Operacion; vista por E3: no
- Excepcion `e4`: **Excepción cuentas de entes públicos** — No se cierran las cuentas ni se cancelan autorizaciones cuando se trata de cuentas abiertas a nombre de entes públicos | tramo: salvo que se trate de cuentas abiertas a nombre de entes públicos | punto 9.1.2.1 | marcado en texto propio
- Operacion `e1`: **Cierre de cuentas** — Cierre de cuentas en las que figuren personas incluidas en la Central de cuentacorrentistas inhabilitados, aun cuando en ellas figuren otros titulares | tramo: cerrarán esas cuentas (aun en las que figuren con otros titulares) | punto 9.1.2.1 | marcado en texto propio
- heredado, herencia[0] encabezado S9: Sección 9. Cierre de cuentas y suspensión del servicio de pago de cheques como medida previa al cierre de la cuenta.
- heredado, herencia[1] encabezado 9.1: 9.1. Causales.
- heredado, herencia[2] encabezado 9.1.2: 9.1.2. Inclusión de alguno de sus integrantes en la “Central de cuentacorrentistas inhabilitados”.
- heredado, herencia[3] intro 9.1.2: Las entidades deberán verificar si las personas incluidas en la "Central de cuentacorren-
tistas inhabilitados" tienen cuentas abiertas o están autorizadas para librar cheques de
cuentas a nombre de terceros.
- texto propio:

```
9.1.2.1. En caso afirmativo, ⟦O:cerrarán esas cuentas (aun en las que figuren con otros titu-
lares⟧) o dejarán sin efecto las pertinentes autorizaciones, ⟦E:salvo que se trate de
cuentas abiertas a nombre de entes públicos⟧, y remitirán los correspondientes
avisos.
```

## EO41 — `ctacte::9.1.2.1`
- origen: crudo de KG-Tanda0-Diez-r2b (a9631a64…), extracción final r2 guardada
- unidad: punto_no_item; páginas [49]; estado en E3 `aceptado_con_residuales`; en la cola: no; crudo que entra a E2: e1
- relación rechazada: índice 9 del crudo, `e4` `exceptua` `e2` (punto 9.1.2.1); validador de E1: firma_invalida: relations[9]: Excepcion --exceptua--> Operacion; vista por E3: no
- Excepcion `e4`: **Excepción cuentas de entes públicos** — No se cierran las cuentas ni se cancelan autorizaciones cuando se trata de cuentas abiertas a nombre de entes públicos | tramo: salvo que se trate de cuentas abiertas a nombre de entes públicos | punto 9.1.2.1 | marcado en texto propio
- Operacion `e2`: **Cancelación de autorizaciones para librar cheques** — Dejar sin efecto las autorizaciones para librar cheques de cuentas a nombre de terceros | tramo: dejarán sin efecto las pertinentes autorizaciones | punto 9.1.2.1 | marcado en texto propio
- heredado, herencia[0] encabezado S9: Sección 9. Cierre de cuentas y suspensión del servicio de pago de cheques como medida previa al cierre de la cuenta.
- heredado, herencia[1] encabezado 9.1: 9.1. Causales.
- heredado, herencia[2] encabezado 9.1.2: 9.1.2. Inclusión de alguno de sus integrantes en la “Central de cuentacorrentistas inhabilitados”.
- heredado, herencia[3] intro 9.1.2: Las entidades deberán verificar si las personas incluidas en la "Central de cuentacorren-
tistas inhabilitados" tienen cuentas abiertas o están autorizadas para librar cheques de
cuentas a nombre de terceros.
- texto propio:

```
9.1.2.1. En caso afirmativo, cerrarán esas cuentas (aun en las que figuren con otros titu-
lares) o ⟦O:dejarán sin efecto las pertinentes autorizaciones⟧, ⟦E:salvo que se trate de
cuentas abiertas a nombre de entes públicos⟧, y remitirán los correspondientes
avisos.
```

## EO42 — `cla::2.2.1.5`
- origen: U-ESTUDIO-MATRIZ, muestra sellada sin leer `7e72051` (uestmat_muestra_60.csv), fila M21: réplica en memoria de KG-Tanda0-Desarrollo-r1 (eab2fdd0); no es una relación del crudo r2b; agregada por el §2 de la enmienda 8
- Excepcion: **Exclusión Anticipos y préstamos Fondo de Garantía Depósitos** — Anticipos y préstamos al Fondo de Garantía de los Depósitos están excluidos de los conceptos por intermediación financiera comprendidos en clasificación de deudores. | tramo: None | punto None | sin tramo en la fuente
- Operacion: **Préstamos al Fondo de Garantía Depósitos** — Préstamos otorgados al Fondo de Garantía de los Depósitos. | tramo: None | punto None | sin tramo en la fuente
- texto propio (texto de E0 de la extracción de origen (títulos heredados y texto propio juntos), tal como está en la muestra):

```
Sección 2. Financiaciones comprendidas.
2.2. Exclusiones.
2.2.1. Los siguientes conceptos por intermediación financiera:
2.2.1.5. Anticipos y préstamos al Fondo de Garantía de los Depósitos.
```

## EO43 — `ext::8.5.17.21`
- origen: U-ESTUDIO-MATRIZ, muestra sellada sin leer `7e72051` (uestmat_muestra_60.csv), fila M23: réplica en memoria de KG-Tanda0-Desarrollo-r1 (eab2fdd0); no es una relación del crudo r2b; agregada por el §2 de la enmienda 8
- Excepcion: **Exceptuación seguimiento destinaciones suspensivas** — Las destinaciones suspensivas de exportaciones temporarias (artículos 349 a 373 del Código Aduanero) quedan exceptuadas del seguimiento de divisas por exportaciones de bienes | tramo: None | punto None | sin tramo en la fuente
- Operacion: **Destinaciones suspensivas exportaciones temporarias** — Operación aduanera de destinación suspensiva de exportaciones temporarias según artículos 349 a 373 del Código Aduanero | tramo: None | punto None | sin tramo en la fuente
- texto propio (texto de E0 de la extracción de origen (títulos heredados y texto propio juntos), tal como está en la muestra):

```
Sección 8. Seguimiento de las negociaciones de divisas por exportaciones de bienes
8.5. Otras imputaciones admitidas en el cumplimiento del seguimiento.
La entidad podrá considerar cumplimentado parcial o totalmente el seguimiento de un permiso
de embarque cuando cuente con los elementos que le permitan considerar que la operación
se encuentra en alguna de las situaciones detalladas a continuación y se verifiquen las
condiciones previstas en cada caso.
La documentación utilizada para certificar el concepto y monto de las divisas imputado en
cada caso deberá quedar archivada en la entidad a disposición del BCRA.
8.5.17. Operaciones aduaneras exceptuadas del seguimiento.
Por el valor que corresponda a ventajas aduaneras u otras situaciones previstas en el
siguiente listado de operaciones:
8.5.17.21. Destinaciones suspensivas de exportaciones temporarias (artículos 349 a
373 del Código Aduanero).
```

## EO44 — `ext::8.5.17.24`
- origen: U-ESTUDIO-MATRIZ, muestra sellada sin leer `7e72051` (uestmat_muestra_60.csv), fila M24: réplica en memoria de KG-Tanda0-Desarrollo-r1 (eab2fdd0); no es una relación del crudo r2b; agregada por el §2 de la enmienda 8
- Excepcion: **Reembarco subregímenes RE01 RE04 RE05 RE06 REP1 REP4 REP6** — Operaciones de reembarco consignadas mediante los subregímenes RE01, RE04, RE05, RE06, REP1, REP4 o REP6 están exceptuadas del seguimiento. | tramo: None | punto None | sin tramo en la fuente
- Operacion: **Operación de reembarco** — Operaciones de reembarco consignadas mediante los subregímenes RE01, RE04, RE05, RE06, REP1, REP4 o REP6 | tramo: None | punto None | sin tramo en la fuente
- texto propio (texto de E0 de la extracción de origen (títulos heredados y texto propio juntos), tal como está en la muestra):

```
Sección 8. Seguimiento de las negociaciones de divisas por exportaciones de bienes
8.5. Otras imputaciones admitidas en el cumplimiento del seguimiento.
La entidad podrá considerar cumplimentado parcial o totalmente el seguimiento de un permiso
de embarque cuando cuente con los elementos que le permitan considerar que la operación
se encuentra en alguna de las situaciones detalladas a continuación y se verifiquen las
condiciones previstas en cada caso.
La documentación utilizada para certificar el concepto y monto de las divisas imputado en
cada caso deberá quedar archivada en la entidad a disposición del BCRA.
8.5.17. Operaciones aduaneras exceptuadas del seguimiento.
Por el valor que corresponda a ventajas aduaneras u otras situaciones previstas en el
siguiente listado de operaciones:
8.5.17.24. Operaciones de reembarco consignadas mediante los subregímenes
RE01, RE04, RE05, RE06, REP1, REP4 o REP6.
```

## EO45 — `ext::8.5.17.28`
- origen: U-ESTUDIO-MATRIZ, muestra sellada sin leer `7e72051` (uestmat_muestra_60.csv), fila M25: réplica en memoria de KG-Tanda0-Desarrollo-r1 (eab2fdd0); no es una relación del crudo r2b; agregada por el §2 de la enmienda 8
- Excepcion: **Exceptuación — operaciones BARA y VMI1** — Operaciones aduaneras de los subregímenes BARA y VMI1 en el marco de la operatoria de proveedores de combustibles de medios de transporte | tramo: None | punto None | sin tramo en la fuente
- Operacion: **Operación aduanera — régimen VMI1** — Operación aduanera bajo el subrégimen VMI1 en el marco de la operatoria de proveedores de combustibles de medios de transporte | tramo: None | punto None | sin tramo en la fuente
- texto propio (texto de E0 de la extracción de origen (títulos heredados y texto propio juntos), tal como está en la muestra):

```
Sección 8. Seguimiento de las negociaciones de divisas por exportaciones de bienes
8.5. Otras imputaciones admitidas en el cumplimiento del seguimiento.
La entidad podrá considerar cumplimentado parcial o totalmente el seguimiento de un permiso
de embarque cuando cuente con los elementos que le permitan considerar que la operación
se encuentra en alguna de las situaciones detalladas a continuación y se verifiquen las
condiciones previstas en cada caso.
La documentación utilizada para certificar el concepto y monto de las divisas imputado en
cada caso deberá quedar archivada en la entidad a disposición del BCRA.
8.5.17. Operaciones aduaneras exceptuadas del seguimiento.
Por el valor que corresponda a ventajas aduaneras u otras situaciones previstas en el
siguiente listado de operaciones:
8.5.17.28. Operaciones aduaneras de los subregímenes “BARA” y “VMI1” en el
marco de la operatoria de proveedores de combustibles de medios de
transporte.
```
