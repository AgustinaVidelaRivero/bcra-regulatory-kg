# Prueba en seco de P2.d: requests de E1 del perfil r2b (sin API)

Perfil `r2b`, hash canónico `14d6b63b508e`, namespace `e1_extraccion|cv=e1-extractor-v1-p14d6b63b508e|think=0`, modelo `claude-haiku-4-5`, E0 `data/experiment/reextraccion_v2/e0_chunking/salida_tanda0_r2`.

## cap::1.2

- system sha256 `cdb374508523e7f2308b1e3dd9790cdcfbb4000f2f1616279504af9475c6e227`; tools sha256 `e35358e5ab468078f2f22329a3c8e127505f6063e14ca28d4b4d5fc683404d16`; max_tokens 8192; clave `b0ff433287c6b5ac3013c7b4379ea5ae67d6dc02217f8a9136600491540fdc1f`.

Mensaje de usuario:

```text
Documento fuente: TO_capitales_minimos_actual.pdf
TO: cap
Tipo de unidad: chunk de punto
Punto del chunk: 1.2 — Exigencia básica.
Puntos admitidos para `punto`: 1.2, S1

Alcance de este TO: Sujeto_rol_alcance_capmin = {Entidades financieras}. Cuando la norma se dirija genéricamente a 'las entidades' / 'los sujetos obligados' / el colectivo del TO, sugerí Sujeto_rol_alcance_capmin en `sujeto_id`, con la expresión del texto como `sujeto_mencion`. Es el sujeto de aplica_a cuando la norma se dirige al colectivo; NO es el ejecutor por defecto en ejecuta.

Contexto estructural heredado (SOLO contexto y anclaje: NO extraigas contenido normativo de estos bloques — cada uno tiene su propia unidad de extracción; ver PROVENANCE):
[encabezado | punto S1]
Sección 1. Capital mínimo.

TABLAS SERIALIZADAS POR E0 en el texto (CONFIABLES: leelas y copiá sus valores, ver CONTENIDO NO-PROSA del sistema):
- `cap::tabla000` (columnas): confiable, sin celdas combinadas.

Texto del punto 1.2:
```
1.2. Exigencia básica.
Según la clase de entidad, serán las siguientes exigencias básicas:
[TABLA cap::tabla000 | página 4 | e0_tablas | columnas]
Rótulo: -En millones de pesos-
Columnas: Bancos | Restantes entidades (salvo Cajas de Crédito Cooperativas)
Fila 1: Bancos = 5.000 | Restantes entidades (salvo Cajas de Crédito Cooperativas) = 2.500
[FIN TABLA cap::tabla000]
Las compañías financieras que realicen, en forma directa, operaciones de comercio exterior
deberán observar las exigencias establecidas para los bancos.
```

Extraé las entidades y relaciones según el schema. Recordá: nodo TextoOrdenado con local_id='to'; todo elemento con `punto` de la lista admitida; toda entidad con su `tramo`; toda relación de sujeto con su `sujeto_mencion`; `omisiones` siempre (vacía si no omitiste nada).
```

## ric::9.2.1

- system sha256 `cdb374508523e7f2308b1e3dd9790cdcfbb4000f2f1616279504af9475c6e227`; tools sha256 `e35358e5ab468078f2f22329a3c8e127505f6063e14ca28d4b4d5fc683404d16`; max_tokens 8192; clave `7f44390dfdf8eecbc80e1b069028a010b6ddaa31fe625dc0263b6fe8a9eb4c75`.

Mensaje de usuario:

```text
Documento fuente: TO_regimen_informativo_contable_mensual_actual.pdf
TO: ric
Tipo de unidad: chunk de punto
Punto del chunk: 9.2.1 — Incrementos de exigencia
Puntos admitidos para `punto`: 9.2.1, S9, 9.2

Alcance de este TO: Sujeto_rol_entidad_comprendida_reginf = {Entidades financieras}. Cuando la norma se dirija genéricamente a 'las entidades' / 'los sujetos obligados' / el colectivo del TO, sugerí Sujeto_rol_entidad_comprendida_reginf en `sujeto_id`, con la expresión del texto como `sujeto_mencion`. Es el sujeto de aplica_a cuando la norma se dirige al colectivo; NO es el ejecutor por defecto en ejecuta.

Contexto estructural heredado (SOLO contexto y anclaje: NO extraigas contenido normativo de estos bloques — cada uno tiene su propia unidad de extracción; ver PROVENANCE):
[encabezado | punto S9]
Sección 9. Incrementos de exigencia por riesgo de crédito
[encabezado | punto 9.2]
9.2. Modelo de Información

TABLAS SERIALIZADAS POR E0 en el texto (CONFIABLES: leelas y copiá sus valores, ver CONTENIDO NO-PROSA del sistema):
- `ric::tabla022` (columnas): confiable, sin celdas combinadas.
- `ric::tabla023` (posicional): sin encabezado de columnas reconocido: las claves son colN y el nombre de cada columna está en las primeras filas del bloque.

Texto del punto 9.2.1:
```
9.2.1. Incrementos de exigencia
[TABLA ric::tabla022 | página 41 | e0_tablas | columnas]
Columnas: Código | Concepto | Importe
Fila 1: Código = 83100000 | Concepto = Incremento de la exigencia por riesgo de crédito por exceso en la relación de activos inmovilizados. Información en término
Fila 2: Código = 83200000 | Concepto = Incremento de la exigencia por riesgo de crédito por exceso en la relación de activos inmovilizados. Información fuera de término
Fila 3: Código = 83300000 | Concepto = Incremento de la exigencia por riesgo de crédito por exceso en la relación de activos inmovilizados. Incumplimientos reiterados
Fila 4: Código = 83400000 | Concepto = Incremento de la exigencia por riesgo de crédito por exceso en la relación de activos inmovilizados. Determinado por la SEFyC
Fila 5: Código = 83500000 | Concepto = Incremento de la exigencia por riesgo de crédito por exceso en Grandes Exposiciones al Riesgo de Crédito. Información en término
Fila 6: Código = 83600000 | Concepto = Incremento de la exigencia por riesgo de crédito por exceso en Grandes Exposiciones al Riesgo de Crédito. Información fuera de término
Fila 7: Código = 83700000 | Concepto = Incremento de la exigencia por riesgo de crédito por exceso en Grandes Exposiciones al Riesgo de Crédito. Incumplimientos reiterados
Fila 8: Código = 83800000 | Concepto = Incremento de la exigencia por riesgo de crédito por exceso en Grandes Exposiciones al Riesgo de Crédito. Determinado por la SEFyC
Fila 9: Código = 84300000 | Concepto = Incremento de la exigencia por riesgo de crédito por exceso en gradua- ción del crédito. Información en término
Fila 10: Código = 84400000 | Concepto = Incremento de la exigencia por riesgo de crédito por exceso en gradua- ción del crédito. Información fuera de término
Fila 11: Código = 84500000 | Concepto = Incremento de la exigencia por riesgo de crédito por exceso en gradua- ción del crédito. Incumplimientos reiterados.
Fila 12: Código = 84600000 | Concepto = Incremento de la exigencia por riesgo de crédito por exceso en gradua- ción del crédito. Determinado por la SEFyC.
Fila 13: Código = 85600000 | Concepto = Incremento de la exigencia por riesgo de crédito por la tenencia de certifi- cados o títulos de deuda de fideicomisos financieros. (25 %)
Fila 14: Código = 85700000 | Concepto = Incremento de la exigencia por riesgo de crédito por la tenencia de certifi- cados o títulos de deuda de fideicomisos financieros. (50 %)
Fila 15: Código = 85800000 | Concepto = Incremento de la exigencia por riesgo de crédito por la tenencia de certifi- cados o títulos de deuda de fideicomisos financieros. (100 %)
Fila 16: Código = 86300000 | Concepto = Incremento de la exigencia por riesgo de crédito por excesos en las parti- cipaciones en el capital de empresas (INC ) (Inversiones significativas en empresas)
[FIN TABLA ric::tabla022]
[TABLA ric::tabla023 | página 42 | e0_tablas | posicional]
Fila 1: col1 = 87100000 | col2 = Incremento de la exigencia por riesgo de crédito por exceso en financia- miento al sector público no financiero. Información en término
Fila 2: col1 = 87200000 | col2 = Incremento de la exigencia por riesgo de crédito por exceso en financia- miento al sector público no financiero. Información fuera de término
Fila 3: col1 = 87300000 | col2 = Incremento de la exigencia por riesgo de crédito por exceso en financia- miento al sector público no financiero. Incumplimientos reiterados
Fila 4: col1 = 87400000 | col2 = Incremento de la exigencia por riesgo de crédito por exceso en financia- miento al sector público no financiero. Determinado por la SEFyC
Fila 5: col1 = 87500000 | col2 = Incremento de la exigencia por riesgo de crédito por exceso en posicio- nes de derivados sobre “commodities”. Información en término
Fila 6: col1 = 87600000 | col2 = Incremento de la exigencia por riesgo de crédito por exceso en posicio- nes de derivados sobre “commodities”. Información fuera de término
Fila 7: col1 = 87700000 | col2 = Incremento de la exigencia por riesgo de crédito por exceso en posicio- nes de derivados sobre “commodities”. Incumplimientos reiterados
Fila 8: col1 = 87800000 | col2 = Incremento de la exigencia por riesgo de crédito por exceso en posicio- nes de derivados sobre “commodities”. Determinado por la SEFyC
[FIN TABLA ric::tabla023]
```

Extraé las entidades y relaciones según el schema. Recordá: nodo TextoOrdenado con local_id='to'; todo elemento con `punto` de la lista admitida; toda entidad con su `tramo`; toda relación de sujeto con su `sujeto_mencion`; `omisiones` siempre (vacía si no omitiste nada).
```

## cla::6.5.5.7

- system sha256 `cdb374508523e7f2308b1e3dd9790cdcfbb4000f2f1616279504af9475c6e227`; tools sha256 `e35358e5ab468078f2f22329a3c8e127505f6063e14ca28d4b4d5fc683404d16`; max_tokens 8192; clave `55d66b1c7a8313c88b2093be44bd901047f02f9375ec1d70ff8941f2214b9cc1`.

Mensaje de usuario:

```text
Documento fuente: TO_clasificacion_deudores_actual.pdf
TO: cla
Tipo de unidad: chunk de punto
Punto del chunk: 6.5.5.7 — Clientes que a su vez sean deudores en situación irregular –considerando tales
Puntos admitidos para `punto`: 6.5.5.7, S6, 6.5, 6.5.5

Alcance de este TO: Sujeto_rol_obligado_a_clasificar_clasificacion = {Entidades financieras, Proveedores no financieros de crédito, Fiduciarios de fideicomisos financieros, Sociedades de garantía recíproca, Fondos de garantía de carácter público, Proveedores de servicios de créditos entre particulares a través de plataformas (PSCPP)}. Cuando la norma se dirija genéricamente a 'las entidades' / 'los sujetos obligados' / el colectivo del TO, sugerí Sujeto_rol_obligado_a_clasificar_clasificacion en `sujeto_id`, con la expresión del texto como `sujeto_mencion`. Es el sujeto de aplica_a cuando la norma se dirige al colectivo; NO es el ejecutor por defecto en ejecuta.

Contexto estructural heredado (SOLO contexto y anclaje: NO extraigas contenido normativo de estos bloques — cada uno tiene su propia unidad de extracción; ver PROVENANCE):
[encabezado | punto S6]
Sección 6. Clasificación de los deudores de la cartera comercial.
[encabezado | punto 6.5]
6.5. Niveles de clasificación.
[intro | punto 6.5]
Cada cliente, y la totalidad de sus financiaciones comprendidas, se incluirá en una de las si-
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
[encabezado | punto 6.5.5]
6.5.5. Irrecuperable.
[intro | punto 6.5.5]
Las deudas de clientes incorporados a esta categoría se consideran incobrables. Si bien
estos activos podrían tener algún valor de recuperación bajo un cierto conjunto de cir-
cunstancias futuras, su incobrabilidad es evidente al momento del análisis.
Entre los indicadores que pueden reflejar esta situación se destacan que el cliente:
[cierre | punto 6.5.5]
Además, corresponderá clasificar en esta categoría a los clientes que, cualquiera sea el
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

Texto del punto 6.5.5.7:
```
6.5.5.7. Clientes que a su vez sean deudores en situación irregular –considerando tales
a los que registren atrasos superiores a 180 días en el cumplimiento de sus obli-
gaciones–, de acuerdo con la nómina que, a tal efecto y a base de la informa-
ción que deberán suministrar los administradores de las carteras crediticias, ela-
bore y proporcione el Banco Central de la República Argentina (BCRA) de:
i) Entidades liquidadas por el BCRA.
ii) Entes residuales de entidades financieras públicas privatizadas o en proce-
so de privatización o disolución.
iii) Entidades financieras cuya autorización para funcionar haya sido revocada
por el BCRA y se encuentren en estado de liquidación judicial o quiebra.
iv) Fideicomisos en los que SEDESA sea beneficiario.
Se exceptúa de ser clasificados en esta categoría a los deudores, cuando las fi-
nanciaciones otorgadas a ellos se destinen a cancelar los préstamos que origina-
ron su inclusión en la nómina de deudores morosos y siempre que los fondos se
acrediten directamente en las cuentas de las ex entidades acreedoras.
```

Extraé las entidades y relaciones según el schema. Recordá: nodo TextoOrdenado con local_id='to'; todo elemento con `punto` de la lista admitida; toda entidad con su `tramo`; toda relación de sujeto con su `sujeto_mencion`; `omisiones` siempre (vacía si no omitiste nada).
```

## cla::5.1.1.1

- system sha256 `cdb374508523e7f2308b1e3dd9790cdcfbb4000f2f1616279504af9475c6e227`; tools sha256 `e35358e5ab468078f2f22329a3c8e127505f6063e14ca28d4b4d5fc683404d16`; max_tokens 8192; clave `290a60dab9e1175c512902a42da72349894225a9360f013dbd67cbb3677c8e43`.

Mensaje de usuario:

```text
Documento fuente: TO_clasificacion_deudores_actual.pdf
TO: cla
Tipo de unidad: chunk de punto
Punto del chunk: 5.1.1.1 — Los créditos para consumo o vivienda.
Puntos admitidos para `punto`: 5.1.1.1, S5, 5.1, 5.1.1

Alcance de este TO: Sujeto_rol_obligado_a_clasificar_clasificacion = {Entidades financieras, Proveedores no financieros de crédito, Fiduciarios de fideicomisos financieros, Sociedades de garantía recíproca, Fondos de garantía de carácter público, Proveedores de servicios de créditos entre particulares a través de plataformas (PSCPP)}. Cuando la norma se dirija genéricamente a 'las entidades' / 'los sujetos obligados' / el colectivo del TO, sugerí Sujeto_rol_obligado_a_clasificar_clasificacion en `sujeto_id`, con la expresión del texto como `sujeto_mencion`. Es el sujeto de aplica_a cuando la norma se dirige al colectivo; NO es el ejecutor por defecto en ejecuta.

Contexto estructural heredado (contexto y anclaje; NO extraigas contenido normativo de estos bloques, salvo un caso: el último bloque abre la lista de la que este punto es un ítem, así que la norma del ítem se compone con ese encabezado — ver COMPOSICIÓN CON EL ENCABEZADO DE UNA LISTA):
[encabezado | punto S5]
Sección 5. Categorías de carteras.
[encabezado | punto 5.1]
5.1. Categorías.
[intro | punto 5.1]
La cartera se agrupará en dos categorías básicas:
[encabezado | punto 5.1.1]
5.1.1. Cartera comercial.
[intro | punto 5.1.1]
Abarca todas las financiaciones comprendidas, con excepción de las siguientes:

Texto del punto 5.1.1.1:
```
5.1.1.1. Los créditos para consumo o vivienda.
Los créditos de esta clase que superen el equivalente a dos veces el importe de
referencia establecido en el punto 3.7. y cuyo repago no se encuentre vinculado
a ingresos fijos o periódicos del cliente sino a la evolución de su actividad pro-
ductiva o comercial se incluirán dentro de la cartera comercial.
```

Extraé las entidades y relaciones según el schema. Recordá: nodo TextoOrdenado con local_id='to'; todo elemento con `punto` de la lista admitida; toda entidad con su `tramo`; toda relación de sujeto con su `sujeto_mencion`; `omisiones` siempre (vacía si no omitiste nada).
```
