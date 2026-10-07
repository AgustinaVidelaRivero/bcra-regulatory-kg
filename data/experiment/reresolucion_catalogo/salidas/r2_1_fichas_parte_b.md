# Lectura de la parte B de la enmienda 6 a L-ESQ-R2 — fichas para la adjudicación de la autora

Muestra de 30 normas de la población de la parte B (KG-Tanda0-Diez-r2b), sorteada con la semilla 20261006 antes de leer (r2_1_medicion.py). Lectura asistida y declarada; la adjudicación es de la autora.

**Criterio.** Correcta: el sujeto que tiene que cumplir la norma (o que tiene la potestad), según el texto de la unidad y su texto heredado, es el rol de alcance del documento o uno de sus miembros. Incorrecta: el texto pone la norma en cabeza de otro sujeto, que no es miembro del rol. Dudosa: la norma es impersonal o es una condición de una operación o de un instrumento, y el texto no dice quién la cumple, o la pone en cabeza de un sujeto que el catálogo distingue del rol (un órgano de la entidad). La lectura es asistida y declarada; la adjudicación es de la autora.

## Recuento de la lectura (antes de la adjudicación)

| veredicto | fichas |
|---|---|
| correcta | 18 |
| incorrecta | 5 |
| dudosa | 7 |

- Límite inferior de Wilson al 95 % con las correctas de la lectura: 18 de 30, 0.423 (piso 0.75).
- Si todas las dudosas se adjudicaran correctas: 25 de 30, 0.664.
- El piso de 28 de 30 da 0.787; 27 de 30 da 0.744.
- De las leídas, 5 vienen de una relación con una mención que no verifica: F06 correcta, F16 correcta, F20 incorrecta, F22 dudosa, F25 incorrecta.

| ficha | TO | unidad | tipo | categoría | cola | veredicto | sujeto según el texto |
|---|---|---|---|---|---|---|---|
| F01 | pro | `pro::2.3.1.1` | Obligacion | sin_aplica_a | no | correcta | el sujeto obligado (suscribe y entrega el contrato) |
| F02 | pro | `pro::2.3.3` | Obligacion | sin_aplica_a | no | correcta | el sujeto obligado (calcula y expone el CFT) |
| F03 | cla | `cla::3.4.2` | Obligacion | sin_aplica_a | no | correcta | quien clasifica y mantiene el legajo |
| F04 | cla | `cla::7.2.4` | Potestad | sin_aplica_a | no | correcta | quien clasifica (pasiva: «el deudor podrá ser reclasificado») |
| F05 | cla | `cla::7.2.5` | Potestad | sin_aplica_a | sí | correcta | quien clasifica (pasiva: «los clientes ... podrán ser reclasificados») |
| F06 | ric | `ric::4.5.2` | Obligacion | aplica_a_mencion_no_verifica | no | correcta | la entidad que informa (formulario del régimen informativo) |
| F07 | ric | `ric::6.3` | Restriccion | sin_aplica_a | no | correcta | la entidad comprendida (su capital) |
| F08 | cap | `cap::3.1.7` | Restriccion | sin_aplica_a | no | correcta | la entidad financiera (originante, que transfiere el riesgo) |
| F09 | cap | `cap::3.1.14.1` | Obligacion | sin_aplica_a | no | incorrecta | el originante o fiduciario |
| F10 | cap | `cap::3.1.14.2` | Obligacion | sin_aplica_a | no | dudosa | la estructura de la titulización; el heredado pone la divulgación en cabeza del originante/fiduciario |
| F11 | cap | `cap::3.1.14.2` | Obligacion | sin_aplica_a | no | dudosa | la estructura de la titulización (orden de cancelación de los tramos) |
| F12 | cap | `cap::4.2.1::intro` | Obligacion | sin_aplica_a | no | correcta | la entidad que calcula la exposición al riesgo de contraparte |
| F13 | cap | `cap::4.3.3.1` | Restriccion | sin_aplica_a | no | correcta | la entidad financiera que es cliente del miembro compensador |
| F14 | cap | `cap::4.3.3.1` | Restriccion | sin_aplica_a | no | correcta | la entidad que constituye la garantía |
| F15 | cap | `cap::6.5.2` | Restriccion | sin_aplica_a | no | correcta | la entidad que mide su exposición en productos básicos |
| F16 | cap | `cap::8.6.2` | Obligacion | aplica_a_mencion_no_verifica | no | correcta | la entidad que recibe y registra el aporte de capital |
| F17 | ext | `ext::3.5.3.1` | Potestad | sin_aplica_a | no | correcta | la entidad («la entidad podrá darle acceso») |
| F18 | ext | `ext::3.17.3.3` | Restriccion | sin_aplica_a | no | correcta | la entidad nominada (registra montos y emite la certificación) |
| F19 | ext | `ext::4.8.4.2` | Restriccion | sin_aplica_a | no | dudosa | el cliente que suscribió BOPREAL (titular de la potestad); la entidad verifica |
| F20 | ext | `ext::7.1.1.5` | Obligacion | aplica_a_mencion_no_verifica | no | incorrecta | el exportador (obligación de ingreso y liquidación) |
| F21 | ext | `ext::7.1.3` | Obligacion | sin_aplica_a | no | incorrecta | el exportador que recibe el anticipo o la financiación |
| F22 | ext | `ext::7.10.1.1` | Potestad | aplica_a_mencion_no_verifica | sí | dudosa | impersonal («Se admitirá la aplicación de cobros»); la aplicación la pide el exportador del régimen del Decreto 234/21 |
| F23 | ext | `ext::7.11.2::intro` | Potestad | sin_aplica_a | no | dudosa | impersonal («será admitida en la medida que se verifiquen») |
| F24 | ext | `ext::9.2` | Potestad | sin_aplica_a | no | incorrecta | el exportador («pudiendo el exportador modificarla») |
| F25 | ctacte | `ctacte::1.5.1.7` | Obligacion | aplica_a_mencion_no_verifica | no | incorrecta | el cuentacorrentista (heredado: «1.5.1. Obligaciones del cuentacorrentista») |
| F26 | ctacte | `ctacte::5.1.6` | Restriccion | sin_aplica_a | no | correcta | el banco girado (no puede rechazar el cheque) |
| F27 | ctacte | `ctacte::8.5.4` | Restriccion | sin_aplica_a | no | dudosa | impersonal («No procederá la inclusión»); la inclusión en la Central la hace el BCRA con lo que informan los bancos |
| F28 | lingob | `lingob::3.2::intro` | Obligacion | sin_aplica_a | no | dudosa | la Alta Gerencia (sección 3, «Alta Gerencia»; «Es recomendable que la Alta Gerencia») |
| F29 | polcre | `polcre::2.1.14` | Restriccion | sin_aplica_a | no | correcta | la entidad que aplica su capacidad de préstamo en moneda extranjera |
| F30 | polcre | `polcre::5.3` | Restriccion | sin_aplica_a | no | correcta | la entidad financiera (sus tenencias) |

## Fichas

### F01 — pro, `pro::2.3.1.1` (punto 2.3.1.1), Obligacion

- **Norma:** Información de derechos de precancelación en contrato
- **Descripción:** Los contratos deben contener el derecho del usuario de efectuar, en cualquier momento del plazo del crédito, la precancelación total o precancelaciones parciales con ajuste a lo previsto en el punto 2.3.2.1.
- **Tramo:** El derecho del usuario de efectuar, en cualquier momento del plazo del crédito, la precancelación total o precancelaciones parciales con ajuste a lo previsto en el punto 2.3.2.1.
- **Rol de alcance del documento:** `Sujeto_rol_sujeto_obligado_proteccion` — Sujetos obligados (Protección de usuarios) (miembros: Entidades financieras, Entidades cambiarias, Fiduciarios de fideicomisos financieros, Empresas no financieras emisoras de tarjetas de crédito y/o compra, Proveedores no financieros de crédito, Proveedores de servicios de pago que ofrecen cuentas de pago (PSPCP), Proveedores de servicios de pago iniciadores que prestan el servicio de billetera digital (PSI))
- **Categoría:** sin_aplica_a; cola humana: no; índice en la población: 11
- **Relaciones aplica_a que emitió el modelo:** ninguna

**Texto heredado.**

> [S2, encabezado] Sección 2. Derechos básicos de los usuarios de servicios financieros.
> [2.3, encabezado] 2.3. Recaudos mínimos de la relación de consumo.
> [2.3.1, encabezado] 2.3.1. Al momento de la contratación del producto o servicio.
> [2.3.1, intro] Las entidades financieras, ante requerimientos de apertura de cuentas a la vista por parte de los usuarios de servicios financieros, deberán ofrecer la “Caja de ahorros” en pesos con las prestaciones previstas en el punto 1.8. de las normas sobre “Depósitos de ahorro, cuenta sueldo y especiales” y conservar constancia del ofrecimiento expreso.

**Texto de la unidad.**

```
2.3.1.1. Requisitos mínimos de los contratos financieros.
Los contratos deben ser de clara redacción y con tamaño de tipografía mínimo
de 1,8 milímetros de altura.
Los ejemplares del contrato deben suscribirse a un solo efecto y en el acto de
la contratación debe entregarse uno al usuario de servicios financieros debi-
damente suscripto por el sujeto obligado.
Cuando se trate de solicitudes de productos o servicios que serán sometidas a
la aprobación posterior del sujeto obligado, deberá entregarse al usuario de
servicios financieros un ejemplar de la totalidad de los formularios que firma en
ese acto, intervenido por el sujeto obligado en carácter de constancia de re-
cepción, con ajuste a lo previsto en las normas sobre “Instrumentación, con-
servación y reproducción de documentos”, de corresponder. En dicha oportuni-
dad el sujeto obligado le deberá además notificar –conservando constancia de
ello– que una vez aprobada la solicitud se le proporcionará –dentro de los diez
días hábiles contados a partir de la fecha de su aprobación o de la disponibili-
dad efectiva del producto o servicio, lo que suceda último– el contrato con la
firma autorizada del sujeto obligado.
Las cláusulas del contrato deben ser comprensibles y autosuficientes, corres-
pondiendo tener por no escritas las que remitan a textos o documentos que no
se proporcionen al usuario de servicios financieros en forma simultánea al
momento de la firma del contrato.
Los contratos como mínimo deben contener:
i) La descripción y especificación completa del producto y/o servicio.
ii) La razón social, CUIT y domicilio legal del sujeto obligado.
iii) Identificación del usuario de servicios financieros.
Personas humanas: nombres y apellidos completos, tipo y número de do-
cumento, CUIT/CUIL/CDI y domicilio. Personas jurídicas: razón social,
CUIT y domicilio legal.
iv) Las comisiones y cargos, así como los términos y condiciones y demás
circunstancias conforme a las cuales hayan sido ofrecidos, publicitados y
convenidos.
En el caso de préstamos hipotecarios en pesos ofrecidos por entidades fi-
nancieras para la compra de vivienda y que permitan aplicar esos fondos
al pago de los inmuebles en moneda extranjera a través de una operación
de compraventa de títulos valores con liquidación en moneda extranjera
(dólar MEP), se deberá informar en forma clara y precisa su respectiva
comisión.
v) Cláusula de revocación en donde se indique que el usuario de servicios fi-
nancieros tiene derecho a revocar la aceptación del producto o servicio
dentro del plazo de diez (10) días hábiles contados a partir de la fecha de
recibido el contrato o de la disponibilidad efectiva del producto o servicio,
lo que suceda último, notificando de manera fehaciente o por el mismo
medio en que el servicio o producto fue contratado.
Para el caso de la contratación a distancia, este plazo se contará a partir
de la fecha en la cual el usuario reciba el contrato con la firma del sujeto
obligado.
Se aclarará en esta misma cláusula que dicha revocación será sin costo ni
responsabilidad alguna para el usuario de servicios financieros en la medi-
da que no haya hecho uso del respectivo producto o servicio y que, en el
caso de que lo haya utilizado, sólo se le cobrarán las comisiones y cargos
previstos para la prestación, proporcionados al tiempo de utilización del
servicio o producto.
La facultad de revocación debe ser informada al usuario en todo documen-
to que le sea presentado con motivo de la oferta y/o contratación del pro-
ducto o servicio.
Lo previsto en este punto no aplica a las operaciones de captación de fon-
dos que realizan las entidades financieras en el marco del TO sobre Depó-
sitos e Inversiones a Plazo.
vi) El derecho del usuario de efectuar, en cualquier momento del plazo del
crédito, la precancelación total o precancelaciones parciales con ajuste a
lo previsto en el punto 2.3.2.1.
vii) El derecho del usuario de realizar operaciones por ventanilla, sin restricciones de
tipo de operación –sujeto a las que por razones operativas pudieran existir– ni de
monto mínimo, conforme a lo previsto en el punto 2.3.2.2.
viii) La leyenda: “Usted puede consultar el “Régimen de Transparencia” elaborado por
el BCRA sobre la base de la información proporcionada por los sujetos obligados a
fin de comparar los costos, características y requisitos de los productos y servicios
financieros, ingresando a https://www.bcra.gob.ar/regimen-de-transparencia/.
ix) El derecho de solicitar la apertura de la Caja de Ahorros en pesos con las presta-
ciones previstas en el punto 1.8. del TO sobre Depósitos de Ahorro, Cuenta Sueldo
y Especiales, las cuales serán gratuitas.
x) Los restantes requisitos normativamente reglamentados según el producto o servi-
cio de que se trate.
```

**Lectura: CORRECTA.** Sujeto según el texto: el sujeto obligado (suscribe y entrega el contrato). La norma fija el contenido mínimo del contrato; el texto de la unidad pone la redacción, la firma y la entrega del contrato en cabeza del «sujeto obligado», que es el rol de pro. El derecho es del usuario, que es el beneficiario, no el obligado.

**Adjudicación de la autora:** PENDIENTE

### F02 — pro, `pro::2.3.3` (punto 2.3.3), Obligacion

- **Norma:** Incluir en cálculo CFT: tasa, comisiones y cargos vigentes
- **Descripción:** Para el cálculo del costo financiero total se debe tomar en cuenta la tasa de interés, las comisiones y cargos vigentes al momento de la contratación, indicando expresamente si esos conceptos podrán modificarse de conformidad con los parámetros y criterios preestablecidos en el contrato.
- **Tramo:** Para el cálculo del costo financiero total se tomará en cuenta la tasa de interés, las comisiones y cargos vigentes al momento de la contratación, indicando expresamente si esos conceptos podrán modificarse de conformidad con los parámetros y criterios preestablecidos en el contrato.
- **Rol de alcance del documento:** `Sujeto_rol_sujeto_obligado_proteccion` — Sujetos obligados (Protección de usuarios) (miembros: Entidades financieras, Entidades cambiarias, Fiduciarios de fideicomisos financieros, Empresas no financieras emisoras de tarjetas de crédito y/o compra, Proveedores no financieros de crédito, Proveedores de servicios de pago que ofrecen cuentas de pago (PSPCP), Proveedores de servicios de pago iniciadores que prestan el servicio de billetera digital (PSI))
- **Categoría:** sin_aplica_a; cola humana: no; índice en la población: 23
- **Relaciones aplica_a que emitió el modelo:** ninguna

**Texto heredado.**

> [S2, encabezado] Sección 2. Derechos básicos de los usuarios de servicios financieros.
> [2.3, encabezado] 2.3. Recaudos mínimos de la relación de consumo.

**Texto de la unidad.**

```
2.3.3. Exposición de las tasas de interés y del costo financiero total (CFT) en los documentos.
Para las operaciones de financiación debe aplicarse lo dispuesto en el punto 3.2. del
TO sobre Tasas de Interés en las Operaciones de Crédito.
La falta de inclusión en los documentos de la tasa de interés y/o del costo financiero to-
tal determinará que el sujeto obligado podrá aplicar al usuario, como máximo CFT, la
tasa promedio que surja de la encuesta de tasas de interés de depósitos a plazo fijo de
30 a 59 días –de pesos o dólares estadounidenses, según la moneda de la operación–
informada por el BCRA a la fecha de celebración del contrato –o, en caso de que no es-
tuviera disponible, la última informada– sobre la base de la información provista por la
totalidad de bancos públicos y privados.
Para el cálculo del costo financiero total se tomará en cuenta la tasa de interés, las co-
misiones y cargos vigentes al momento de la contratación, indicando expresamente si
esos conceptos podrán modificarse de conformidad con los parámetros y criterios
preestablecidos en el contrato.
```

**Lectura: CORRECTA.** Sujeto según el texto: el sujeto obligado (calcula y expone el CFT). Regla de cálculo del costo financiero total en los documentos del sujeto obligado; el mismo punto dice que, si falta, «el sujeto obligado podrá aplicar» la tasa supletoria.

**Adjudicación de la autora:** PENDIENTE

### F03 — cla, `cla::3.4.2` (punto 3.4.2), Obligacion

- **Norma:** Permitir clasificación en planillas separadas con procedimiento descrito
- **Descripción:** Se admite mantener la clasificación en planillas separadas si el procedimiento (descrito en Manual de procedimientos) permite identificar precisamente la clasificación de cada cliente entre planilla y legajo.
- **Tramo:** A los fines de la actualización del legajo del cliente, se admitirá que la clasificación asignada se mantenga en planillas separadas, siempre que el procedimiento adoptado –que deberá estar descripto en el "Manual de procedimientos de clasificación y previsión"– permita la identificación precisa de la clasificación asignada a cada cliente desde la planilla al legajo y viceversa.
- **Rol de alcance del documento:** `Sujeto_rol_obligado_a_clasificar_clasificacion` — Obligados a clasificar deudores (Clasificación) (miembros: Entidades financieras, Proveedores no financieros de crédito, Fiduciarios de fideicomisos financieros, Sociedades de garantía recíproca, Fondos de garantía de carácter público, Proveedores de servicios de créditos entre particulares a través de plataformas (PSCPP))
- **Categoría:** sin_aplica_a; cola humana: no; índice en la población: 65
- **Relaciones aplica_a que emitió el modelo:** ninguna

**Texto heredado.**

> [S3, encabezado] Sección 3. Tarea de clasificación.
> [3.4, encabezado] 3.4. Legajo del cliente.

**Texto de la unidad.**

```
3.4.2. Contenido.
En el legajo se reunirán todos los elementos de juicio que se tengan en cuenta para rea-
lizar las evaluaciones y clasificaciones y se dejará constancia de las revisiones efectua-
das y de la clasificación asignada.
Cuando no corresponda evaluar la capacidad de repago del deudor por encontrarse la
deuda cubierta con garantías preferidas “A”, según lo previsto en el punto 4.4., no será
obligatorio incorporar al legajo del cliente el flujo de fondos, los estados contables ni toda
otra información necesaria para efectuar ese análisis.
A los fines de la actualización del legajo del cliente, se admitirá que la clasificación asig-
nada se mantenga en planillas separadas, siempre que el procedimiento adoptado –que
deberá estar descripto en el “Manual de procedimientos de clasificación y previsión”–
permita la identificación precisa de la clasificación asignada a cada cliente desde la plani-
lla al legajo y viceversa.
Dicho legajo deberá contar con información acerca de los márgenes crediticios, discrimi-
nado –de corresponder– por tipo o línea, conforme al punto 1.1.3.2., acápite ii) del TO
sobre Gestión Crediticia.
Las entidades financieras deberán comunicar a los deudores los cambios negativos en la
clasificación que se les asigne, siendo optativo cuando el saldo de deuda sea inferior al
monto establecido en el punto 2. “Deudores Comprendidos” de la Sección 3. “Deudores
del sistema financiero” –Normas de Procedimiento– del Régimen Informativo Contable
Mensual.
Deberán informarse los cambios negativos en la clasificación a los deudores que sean
clasificados en las situaciones 3, 4 o 5 y de los deudores en gestión judicial o extrajudi-
cial de cobro (estos últimos, en la medida que cuenten con notificaciones postales o
fehacientes respecto al inicio de las gestiones de cobro).
Tal información deberá ser remitida a los deudores comprendidos dentro de los 45 días
de realizada la reclasificación mediante alguno de los siguientes medios:
a) junto con el resumen impreso que se envíe al deudor con los movimientos de alguna
de las cuentas que se vinculen a las financiaciones que le hayan sido otorgadas,
b) junto con el resumen de cuenta mensual correspondiente a tarjetas de crédito,
c)junto con el recibo de pago de la cuota, o
d) en ausencia de los anteriores, a opción de la entidad, mediante la inclusión de esta in-
formación en cualquier correspondencia postal de carácter general que se remita al
cliente o específica dirigida a tal fin.
Adicionalmente y en igual plazo, las entidades financieras que brinden servicios de in-
formación a sus clientes a través de Internet (“home banking”), deberán poner en cono-
cimiento de cada cliente -por el medio señalado-, la información a la que se refiere esta
comunicación.
Por otra parte, el saldo actualizado de la totalidad de las financiaciones otorgadas -que
comprenderá las facilidades asignadas por todas las filiales y unidades operativas de la
entidad- deberá encontrarse disponible, discriminado por concepto, según el sistema de
información contable que utilice la entidad, en el lugar de radicación del legajo del cliente
o la casa central, de corresponder llevar copia en ésta, de acuerdo con las normas perti-
nentes.
En los casos de clientes del sector privado no financiero cuya deuda en la entidad pres-
tamista (por todo concepto) más el importe de la financiación solicitada, al momento del
otorgamiento de ésta, exceda del 2,5 % de la responsabilidad patrimonial computable de
la entidad del último día del mes anterior al que corresponda o el equivalente al importe
de referencia establecido en el punto 3.7., de ambos el menor, deberá mantenerse en el
legajo, a disposición permanente de la Superintendencia de Entidades Financieras y
Cambiarias, la declaración jurada sobre si revisten o no el carácter de vinculados al res-
pectivo intermediario financiero o si su relación con éste implica la existencia de influen-
cia controlante.
En los casos de corresponsales, el legajo deberá contener la información y demás ele-
mentos de juicio que permitan conocer su identificación, calificación, márgenes de crédito
y cualquier otro dato vinculado a esa relación, de acuerdo con lo establecido en las nor-
mas sobre “Cuentas de corresponsalía”.
Además, en los legajos deberán constar los análisis que se lleven a cabo con motivo de
la aplicación de las normas sobre graduación del crédito.
```

**Lectura: CORRECTA.** Sujeto según el texto: quien clasifica y mantiene el legajo. Admite que la clasificación se lleve en planillas separadas del legajo; lo hace quien está obligado a clasificar, que es el rol de cla.

**Adjudicación de la autora:** PENDIENTE

### F04 — cla, `cla::7.2.4` (punto 7.2.4), Potestad

- **Norma:** Reclasificación en niveles superiores — levantamiento de quiebra
- **Descripción:** El deudor podrá ser reclasificado en niveles superiores, según la situación previa, si se observan las condiciones allí previstas, en caso de levantarse el pedido de quiebra.
- **Tramo:** En caso de levantarse el pedido de quiebra, el deudor podrá ser reclasificado en niveles superiores, según la situación previa, si se observan las condiciones allí previstas.
- **Rol de alcance del documento:** `Sujeto_rol_obligado_a_clasificar_clasificacion` — Obligados a clasificar deudores (Clasificación) (miembros: Entidades financieras, Proveedores no financieros de crédito, Fiduciarios de fideicomisos financieros, Sociedades de garantía recíproca, Fondos de garantía de carácter público, Proveedores de servicios de créditos entre particulares a través de plataformas (PSCPP))
- **Categoría:** sin_aplica_a; cola humana: no; índice en la población: 164
- **Relaciones aplica_a que emitió el modelo:** ninguna

**Texto heredado.**

> [S7, encabezado] Sección 7. Clasificación de los deudores de la cartera para consumo o vivienda.
> [7.2, encabezado] 7.2. Niveles de clasificación.

**Texto de la unidad.**

```
7.2.4. Riesgo alto.
Comprende a los clientes con atrasos de más de 180 días hasta un año.
También incluirá a los deudores que hayan solicitado el concurso preventivo, celebrado
un acuerdo preventivo extrajudicial aún no homologado o se le haya requerido su quie-
bra, en tanto no hubiere sido declarada, por obligaciones que sean iguales o superiores
al 20 % del patrimonio del cliente o por obligaciones entre el 5 % y menos del 20 % del
patrimonio cuando persista el pedido de quiebra luego de transcurridos 90 días desde
que ésta haya sido requerida. En caso de levantarse el pedido de quiebra, el deudor po-
drá ser reclasificado en niveles superiores, según la situación previa, si se observan las
condiciones allí previstas.
En el caso de deudores que hayan solicitado el concurso preventivo o acuerdo preventi-
vo extrajudicial o se encuentren en gestión judicial, que verifiquen atrasos de hasta 540
días.
Los clientes cuyas deudas hayan sido refinanciadas mediante obligaciones de pago pe-
riódico (mensual o bimestral) podrán ser reclasificados en el nivel inmediato superior,
cuando hayan cumplido puntualmente o con atrasos que no superen los 31 días, con el
pago de 3 cuotas consecutivas o, cuando se trate de financiaciones de pago único, pe-
riódico superior a bimestral o irregular, hayan cancelado al menos el 10 % de sus obliga-
ciones refinanciadas (por capital), con más la cantidad de cuotas o el porcentaje acumu-
lado que pudiera corresponder, respectivamente, si la refinanciación se hubiera otorgado
de encontrarse incluido el deudor en el nivel inferior En el caso de deudores que hayan
solicitado el concurso preventivo, corresponderá la reclasificación inmediata en el nivel
siguiente inferior cuando se verifiquen atrasos de más de 540 días.
El deudor refinanciado que haya cumplido con lo dispuesto en los párrafos precedentes,
según corresponda, podrá ser reclasificado en el nivel inmediato superior si, además, el
resto de sus deudas reúnen, como mínimo, las condiciones previstas en el citado nivel.
El deudor que, encontrándose clasificado en esta categoría, haya refinanciado su deuda
–aun cuando haya cancelado las cuotas o el porcentaje establecidos precedentemente–
y recibido crédito adicional en los términos a que se refiere el punto 2.2.5. de las normas
sobre “Previsiones mínimas por riesgo de incobrabilidad”, y en la medida en que dicha fi-
nanciación adicional no hubiese sido cancelada, deberá permanecer en esta categoría
por lo menos 180 días contados desde la fecha en que se otorgó el crédito adicional o
desde que se celebró el acuerdo de refinanciación, la circunstancia más reciente.
En caso de verificarse atrasos mayores a 31 días en el pago de los servicios de la deuda
refinanciada contados a partir de la inclusión del deudor en esta categoría, corresponde-
rá la reclasificación inmediata del deudor en el nivel que surja de considerar la cantidad
total de días resultante de sumar los días de atraso efectivamente registrados a partir de
la primera cuota impaga de la refinanciación y los de atraso mínimo establecidos norma-
tivamente que correspondan a la categoría en la que se encuentre clasificado el deudor
en el mes en que se verifica el nuevo atraso.
```

**Lectura: CORRECTA.** Sujeto según el texto: quien clasifica (pasiva: «el deudor podrá ser reclasificado»). La potestad de reclasificar es de quien clasifica; el deudor es el objeto de la reclasificación, no el titular de la potestad.

**Adjudicación de la autora:** PENDIENTE

### F05 — cla, `cla::7.2.5` (punto 7.2.5), Potestad

- **Norma:** Reclasificación al nivel inmediato superior
- **Descripción:** Facultad de reclasificar en el nivel inmediato superior a clientes cuyas deudas hayan sido refinanciadas mediante obligaciones de pago periódico (mensual o bimestral), cuando se cumplan las condiciones especificadas.
- **Tramo:** Los clientes cuyas deudas hayan sido refinanciadas mediante obligaciones de pago periódico (mensual o bimestral) podrán ser reclasificados en el nivel inmediato superior
- **Rol de alcance del documento:** `Sujeto_rol_obligado_a_clasificar_clasificacion` — Obligados a clasificar deudores (Clasificación) (miembros: Entidades financieras, Proveedores no financieros de crédito, Fiduciarios de fideicomisos financieros, Sociedades de garantía recíproca, Fondos de garantía de carácter público, Proveedores de servicios de créditos entre particulares a través de plataformas (PSCPP))
- **Categoría:** sin_aplica_a; cola humana: sí; índice en la población: 166
- **Relaciones aplica_a que emitió el modelo:** ninguna

**Texto heredado.**

> [S7, encabezado] Sección 7. Clasificación de los deudores de la cartera para consumo o vivienda.
> [7.2, encabezado] 7.2. Niveles de clasificación.

**Texto de la unidad.**

```
7.2.5. Irrecuperable.
Comprende a los clientes insolventes o en quiebra con nula o escasa posibilidad de re-
cuperación del crédito o con atrasos superiores al año.
También incluirá a los clientes que se encuentren en gestión judicial, o que hayan solici-
tado el concurso preventivo o hayan solicitado el acuerdo preventivo extrajudicial, aun
cuando existan posibilidades de recuperación del crédito, una vez transcurridos más de
540 días de atraso.
Los clientes cuyas deudas hayan sido refinanciadas mediante obligaciones de pago pe-
riódico (mensual o bimestral) podrán ser reclasificados en el nivel inmediato superior,
cuando hayan cumplido puntualmente o con atrasos que no superen los 31 días, con el
pago de 3 cuotas consecutivas o, cuando se trate de financiaciones de pago único, pe-
riódico superior a bimestral o irregular, hayan cancelado al menos el 15 % de sus
obligaciones refinanciadas (por capital).
El deudor refinanciado que haya cumplido con lo dispuesto en los párrafos precedentes,
según corresponda, podrá ser reclasificado en el nivel inmediato superior si, además, el
resto de sus deudas reúnen, como mínimo, las condiciones previstas en el citado nivel.
El deudor que, encontrándose clasificado en esta categoría, haya refinanciado su deuda
–aun cuando haya cancelado las cuotas o el porcentaje establecidos precedentemente–
y recibido crédito adicional en los términos a que se refiere el punto 2.2.5. de las normas
sobre “Previsiones mínimas por riesgo de incobrabilidad”, y en la medida en que dicha fi-
nanciación adicional no hubiese sido cancelada, deberá permanecer en esta categoría
por lo menos 180 días contados desde la fecha en que se otorgó el crédito adicional o
desde que se celebró el acuerdo de refinanciación, la circunstancia más reciente.
Además, comprende los clientes que reúnan las condiciones previstas en los puntos
6.5.5.7. a 6.5.5.9.
```

**Lectura: CORRECTA.** Sujeto según el texto: quien clasifica (pasiva: «los clientes ... podrán ser reclasificados»). Mismo caso que F04, en el nivel irrecuperable. La unidad está en la cola humana.

**Adjudicación de la autora:** PENDIENTE

### F06 — ric, `ric::4.5.2` (punto 4.5.2), Obligacion

- **Norma:** Informar tasa de cupón del activo subyacente
- **Descripción:** Las entidades deberán informar la tasa de cupón del activo subyacente cuando corresponda, tal como la tasa del cupón corriente de un título público subyacente
- **Tramo:** Por ejemplo, en un futuro sobre un título público, es la tasa del cupón corriente de dicho título
- **Rol de alcance del documento:** `Sujeto_rol_entidad_comprendida_reginf` — Entidades comprendidas (Régimen Informativo) (miembros: Entidades financieras)
- **Categoría:** aplica_a_mencion_no_verifica; cola humana: no; índice en la población: 220
- **Relaciones aplica_a que emitió el modelo:** mención «las entidades» (no), sugerencia Sujeto_rol_entidad_comprendida_reginf, resuelta a Sujeto_rol_entidad_comprendida_reginf (R4_sugerencia_modelo)

**Texto heredado.**

> [S4, encabezado] Sección 4. Exigencia e integración por riesgo de mercado
> [4.5, encabezado] 4.5. Información sobre instrumentos derivados

**Texto de la unidad.**

```
4.5.2. Futuros y Contratos a Término, incluidos los FRA
[TABLA ric::tabla012 | página 19 | e0_tablas | posicional]
Fila 1: col1 = Descripción del activo subyacente(1) | col2 = Fecha correspondiente al plazo residual del subyacente (cuando corresponda)(2) | col3 = Vencimiento del derivado | col4 = Contraparte/Ámb ito de negociación | col5 = Valor nocional(3) | col6 = Tasa de cupón del activo subyacente (cuando corresponda)(4) | col7 = Precio pactado del subyacente (5) | col8 = Precio de mercado del activo subyacente | col9 = Compra / venta a término (6)
[FIN TABLA ric::tabla012]
(1) Describir el activo comprado o vendido a futuro. Por ejemplo: Tasa de interés Badlar Privada para
depósitos de más de 1 millón de pesos por un plazo de 30 a 35 días, dólar estadounidense, Bono
de la Nación Arg. en dólar link con vencimiento al 2017 - AJ17D, etc.
(2) Por ejemplo, en un futuro sobre un título público es el plazo residual del título público subyacente.
(3) Especificar el valor nocional incluyendo la moneda o unidad de medida. Por ejemplo, USD
25.000.000, $ 100.000, etc.
(4) Por ejemplo, en un futuro sobre un título público, es la tasa del cupón corriente de dicho título
(5) Valor del subyacente pactado. Por ejemplo, valor de la tasa fija pactada, valor pactado del dólar,
valor pactado del bono, etc.
(6) Consignar "C" si el contrato en cuestión es una compra a término, o "V" si es una venta a término.
```

**Lectura: CORRECTA.** Sujeto según el texto: la entidad que informa (formulario del régimen informativo). Columna del cuadro de futuros y contratos a término del régimen informativo: la informa la entidad comprendida. La mención del modelo («las entidades») no está en el texto, pero el destino del rol coincide con quien informa.

**Adjudicación de la autora:** PENDIENTE

### F07 — ric, `ric::6.3` (punto 6.3), Restriccion

- **Norma:** Límite mínimo COn1 4,5 %
- **Descripción:** El Capital Ordinario de Nivel 1 (COn1), calculado como 70210000 – 70220000, debe ser como mínimo el 4,5 % sobre 70900000
- **Tramo:** Capital Ordinario de Nivel 1 (COn1) = 70210000 – 70220000 ≥ 4,5 % s/70900000
- **Rol de alcance del documento:** `Sujeto_rol_entidad_comprendida_reginf` — Entidades comprendidas (Régimen Informativo) (miembros: Entidades financieras)
- **Categoría:** sin_aplica_a; cola humana: no; índice en la población: 238
- **Relaciones aplica_a que emitió el modelo:** ninguna

**Texto heredado.**

> [S6, encabezado] Sección 6. Responsabilidad Patrimonial Computable

**Texto de la unidad.**

```
6.3. Límites mínimos:
Capital Ordinario de Nivel 1 (COn1) = 70210000 – 70220000 ≥ 4,5 % s/70900000
Patrimonio Neto Básico (PNb) = 70210000 – 70220000 + 70230000 – 70240000 ≥ 6 %
s/70900000
Patrimonio Neto Complementario (PNc) = 70250000 – 70260000
Responsabilidad Patrimonial Computable (RPC) = 70200000 ≥ 8% s/70900000
```

**Lectura: CORRECTA.** Sujeto según el texto: la entidad comprendida (su capital). Límite mínimo de capital ordinario de nivel 1 en la sección de RPC del régimen informativo; se aplica a la entidad que informa y cuyo capital se mide.

**Adjudicación de la autora:** PENDIENTE

### F08 — cap, `cap::3.1.7` (punto 3.1.7), Restriccion

- **Norma:** Prohibición — aumento de posición a primera pérdida post-inicio
- **Descripción:** Se prohíben cláusulas que contemplen aumentos de la posición a primera pérdida retenida o de las mejoras crediticias provistas por la entidad originante después del inicio de la operación
- **Tramo:** Cláusulas que contemplen aumentos de la posición a primera pérdida retenida o de las mejoras crediticias provistas por la entidad originante después del inicio de la operación.
- **Rol de alcance del documento:** `Sujeto_rol_alcance_capmin` — Entidades alcanzadas (Capitales Mínimos) (miembros: Entidades financieras)
- **Categoría:** sin_aplica_a; cola humana: no; índice en la población: 403
- **Relaciones aplica_a que emitió el modelo:** ninguna

**Texto heredado.**

> [S3, encabezado] Sección 3. Capital mínimo por riesgo de crédito. Titulizaciones e inversiones en fon- dos.
> [3.1, encabezado] 3.1. Tratamiento de las titulizaciones.
> [3.1, intro] Se denomina “posición de titulización” a la exposición a una titulización (o retitulización), tradi- cional o sintética, o a una estructura con similares características. La exposición a los riesgos de una titulización puede surgir, entre otros, de los siguientes con- ceptos: tenencia de títulos valores emitidos en el marco de la titulización –es decir, títulos de deuda y/o certificados de participación, tales como bonos de titulización de activos (“Asset- Backed Securities”, ABS) y bonos de titulización hipotecaria (“Mortgage-Backed Securities”, MBS)–, mejoras crediticias, facilidades de liquidez, “swaps” de tasa de interés o de monedas y derivados de crédito. Las reservas (“reserve accounts”), tales como las cuentas de garantía en efectivo, se considerarán como un activo para la entidad financiera originante, recibiendo tam- bién el tratamiento de posiciones de titulización. Dado que las titulizaciones pueden estructurarse de diferentes formas, la exigencia de capital para una posición de titulización se determinará teniendo en cuenta su realidad o finalidad eco- nómica y no su forma jurídica. En los casos en que exista incertidumbre acerca de si una de- terminada operación debe considerarse como titulización, la entidad deberá aplicar el criterio que estime mejor se ajusta a la realidad económica de la operación e informar a la SEFyC los fundamentos que lo sustenten.

**Texto de la unidad.**

```
3.1.7. Tratamiento de las operaciones sintéticas.
El empleo de técnicas de coberturas del riesgo de crédito (CRC) –tales como activos
admitidos como garantía, garantías personales y derivados de crédito– para cubrir la po-
sición subyacente se podrá reconocer a efectos de determinar la exigencia de capital co-
rrespondiente a titulizaciones sintéticas sólo si se satisfacen las siguientes condiciones:
i) Las coberturas del riesgo de crédito cumplen los requisitos establecidos en la Sec-
ción 5.
ii) Los activos admitidos como garantía se limitan a los especificados en los puntos
5.3.1.2. y 5.3.2.2. Podrán reconocerse los activos admisibles dados en garantía por
“entes de propósito especial” (SPE).
iii) Los garantes admisibles se limitan a los estipulados en el punto 5.4.1. Los SPE no
son garantes admisibles.
iv) La entidad transfiere a terceros el riesgo de crédito asociado a las exposiciones
subyacentes.
v) Los instrumentos utilizados para transferir el riesgo de crédito no contienen cláusu-
las o condiciones que limiten la cantidad del riesgo de crédito transferido, tales como
las siguientes:
a) Cláusulas que limiten de forma considerable la protección crediticia o la transfe-
rencia del riesgo de crédito, tales como cláusulas de amortización anticipada en
una titulización de facilidades crediticias rotativas que produzcan el efecto de
subordinar los derechos de la entidad financiera, umbrales por debajo de los cua-
les no se active la protección crediticia –incluso si se produce un evento de crédi-
to– establecidos en niveles elevados, o cláusulas que permitan la extinción de la
protección debido al deterioro de la calidad crediticia de las posiciones subyacen-
tes.
b) Cláusulas que obliguen a la entidad originante a alterar las exposiciones subya-
centes para mejorar la calidad crediticia promedio del conjunto de activos subya-
cente.
c) Cláusulas que incrementen el costo de la protección crediticia para la entidad en
respuesta al deterioro en la calidad crediticia del conjunto de activos subyacente.
d) Cláusulas que incrementen el rendimiento pagadero a partes distintas de la enti-
dad originante, tales como inversores y terceros proveedores de mejoras crediti-
cias, en respuesta al deterioro en la calidad crediticia del conjunto de activos
subyacente.
e) Cláusulas que contemplen aumentos de la posición a primera pérdida retenida o
de las mejoras crediticias provistas por la entidad originante después del inicio de
la operación.
vi) Se cuente con dictamen jurídico competente que confirme la exigibilidad del contra-
to.
vii) Las opciones de exclusión satisfacen las condiciones estipuladas en el punto 3.1.4.
```

**Lectura: CORRECTA.** Sujeto según el texto: la entidad financiera (originante, que transfiere el riesgo). Condición para reconocer la cobertura en una titulización sintética: los instrumentos que usa la entidad para transferir el riesgo no pueden tener esa cláusula. La entidad originante del texto es una entidad financiera, miembro del rol.

**Adjudicación de la autora:** PENDIENTE

### F09 — cap, `cap::3.1.14.1` (punto 3.1.14.1), Obligacion

- **Norma:** Verificación de evaluación de riesgo de incumplimiento
- **Descripción:** El obligado al pago no debe contar con evaluación de agencia de calificación de créditos o credit scoring que anticipen riesgo de incumplimiento significativo.
- **Tramo:** El obligado al pago no cuenta con una evaluación de una agencia de calificación de créditos o un credit scoring que anticipen un riesgo de incumplimiento significativo
- **Rol de alcance del documento:** `Sujeto_rol_alcance_capmin` — Entidades alcanzadas (Capitales Mínimos) (miembros: Entidades financieras)
- **Categoría:** sin_aplica_a; cola humana: no; índice en la población: 445
- **Relaciones aplica_a que emitió el modelo:** ninguna

**Texto heredado.**

> [S3, encabezado] Sección 3. Capital mínimo por riesgo de crédito. Titulizaciones e inversiones en fon- dos.
> [3.1, encabezado] 3.1. Tratamiento de las titulizaciones.
> [3.1, intro] Se denomina “posición de titulización” a la exposición a una titulización (o retitulización), tradi- cional o sintética, o a una estructura con similares características. La exposición a los riesgos de una titulización puede surgir, entre otros, de los siguientes con- ceptos: tenencia de títulos valores emitidos en el marco de la titulización –es decir, títulos de deuda y/o certificados de participación, tales como bonos de titulización de activos (“Asset- Backed Securities”, ABS) y bonos de titulización hipotecaria (“Mortgage-Backed Securities”, MBS)–, mejoras crediticias, facilidades de liquidez, “swaps” de tasa de interés o de monedas y derivados de crédito. Las reservas (“reserve accounts”), tales como las cuentas de garantía en efectivo, se considerarán como un activo para la entidad financiera originante, recibiendo tam- bién el tratamiento de posiciones de titulización. Dado que las titulizaciones pueden estructurarse de diferentes formas, la exigencia de capital para una posición de titulización se determinará teniendo en cuenta su realidad o finalidad eco- nómica y no su forma jurídica. En los casos en que exista incertidumbre acerca de si una de- terminada operación debe considerarse como titulización, la entidad deberá aplicar el criterio que estime mejor se ajusta a la realidad económica de la operación e informar a la SEFyC los fundamentos que lo sustenten.
> [3.1.14, encabezado] 3.1.14. Criterios para la determinación de titulizaciones simples, transparentes y comparables.
> [3.1.14, intro] A los fines de establecer el ponderador de riesgo a aplicar de acuerdo con el enfoque estandarizado –punto 3.1.11.–, una titulización se considerará simple, transparente y comparable (STC) si: -se trata de una titulización tradicional que no constituye un programa ABCP; - involucra una transferencia real de activos –en los términos del acápite v) del punto
> [3.1.14, intro] 3.1.14.1.–; y
> [3.1.14, intro] - cumple con la totalidad de los criterios previstos en el presente punto (en adelante,
> [3.1.14, intro] “criterios STC”).
> [3.1.14, intro] El originante/fiduciario deberá divulgar toda la información necesaria respecto de la transacción que permita a los inversores determinar si la titulización cumple con los cri- terios STC. En base a la información provista, el inversor deberá realizar sus propias evaluaciones respecto del cumplimiento de estos criterios previo a la aplicación del en- foque estandarizado. Para las posiciones retenidas en las que el originante haya transferido el riesgo de acuerdo con lo establecido en los puntos 3.1.2.2. y 3.1.8.2. la determinación respecto del cumplimiento de los criterios será efectuada únicamente por la entidad originante. Los criterios STC deberán cumplirse en todo momento. Algunos de los criterios se de- berán verificar sólo al momento de la originación o cuando se genere la posición –si és- ta es posterior–, tal como en el caso de las garantías y las facilidades de liquidez. No obstante, los inversores y tenedores de las posiciones de titulización deberán tener en cuenta las modificaciones que puedan invalidar las evaluaciones de cumplimiento pre- vias, tales como las deficiencias en la frecuencia y en el contenido de los informes a los inversores o los cambios en la documentación contrarios a los criterios STC. En los casos en que los criterios hagan referencia a activos subyacentes –incluidos los criterios previstos en el punto 3.1.14.4.– y el conjunto de subyacentes admita la incorpo- ración de nuevos activos, el cumplimiento estará sujeto a que se realicen verificaciones cada vez que se incorporen esos nuevos activos. Cuando la SEFyC detecte que una titulización no cumple con alguno de los criterios, podrá exigir la implementación de acciones correctivas y/o determinar que se suspenda el tratamiento STC para una o más posiciones de titulización.

**Texto de la unidad.**

```
3.1.14.1. Riesgo de los activos subyacentes.
i) Naturaleza de los activos.
Los activos subyacentes deberán estar constituidos por documentos a
cobrar o derechos de crédito de carácter homogéneo en cuanto a su tipo,
jurisdicción, legislación aplicable y moneda y sus flujos de fondos deberán
estar contractualmente identificados, ser periódicos y consistir exclusiva-
mente en pagos del principal e intereses o de arrendamientos financieros.
La homogeneidad de los activos subyacentes deberá evaluarse teniendo
en consideración los siguientes principios:
a) La naturaleza de los activos deberá ser tal que los inversores, al reali-
zar el proceso de debida diligencia, no necesiten analizar ni evaluar
perfiles o factores de riesgo, crediticios o legales, sustancialmente dife-
rentes entre sí.
b) La homogeneidad se deberá evaluar en función de factores y perfiles
de riesgo comunes al conjunto de los activos.
c) Los documentos y créditos incluidos en la titulización deberán constituir
obligaciones estándares, en términos de derechos de cobro y/o rentas
de los activos y generar un flujo de pago a los inversores periódico y
claramente definido –tal como el flujo que generan las facilidades que
proveen las tarjetas de crédito–.
d) El reembolso a los inversores en la titulización deberá provenir princi-
palmente del producido de los activos subyacentes y no deberá de-
pender de modo sustancial de la refinanciación de los créditos. Se po-
drá contar con la refinanciación o venta de los subyacentes siempre
que las operaciones a refinanciar estén suficientemente distribuidas en
el conjunto de los activos titulizados y que sus valores residuales no
sean significativos.
Las tasas de interés o de descuento de referencia deberán ser tasas de
interés de mercado y de fácil consulta –tales como tasas interbancarias o
tasas establecidas por el BCRA y tasas sectoriales que reflejen el costo
del fondeo de las entidades financieras–, evitándose referencias a fórmu-
las complejas o derivados exóticos. Los límites máximos y mínimos esta-
blecidos sobre las tasas de interés no serán considerados necesariamen-
te como derivados exóticos.
ii) Historia de desempeño de los activos.
Se deberá contar con información verificable sobre pérdidas e incumpli-
mientos respecto de activos con características de riesgo sustancialmente
similares a los que integran la titulización y por un período de tiempo lo
suficientemente prolongado. Ello a los efectos de proveer al inversor de
información respecto de las distintas categorías de activos, así como de
datos que le permitan realizar un cálculo preciso de las pérdidas espera-
das bajo distintos escenarios de estrés, para que pueda llevar a cabo un
adecuado proceso de debida diligencia.
Las fuentes de información y el acceso a los datos, así como los funda-
mentos que permitan aducir la similitud con los activos titulizados, debe-
rán estar disponibles para todos los participantes del mercado.
El inversor, además, deberán poder evaluar –durante su proceso de debi-
da diligencia– si el originante, fiduciario, administrador, agente de cobro u
otros sujetos con responsabilidad fiduciaria en la titulización cuentan con
probados antecedentes, reunidos a lo largo de un período suficientemente
largo, respecto de activos sustancialmente similares a aquellos que son
objeto de titulización. Esta consideración no será condición para dar cum-
plimiento con el presente criterio.
El originante de la titulización, así como el acreedor inicial de los créditos
titulizados, deberán contar con experiencia suficiente en el otorgamiento
de financiaciones similares a las titulizadas.
El inversor deberá determinar la experiencia y el historial de desempeño
del originante y del acreedor inicial respecto de activos sustancialmente
similares a los titulizados a través de un período convenientemente
prolongado. El desempeño se deberá verificar durante un período mínimo
de 5 años en el caso de las exposiciones minoristas que se ajusten a la
definición prevista en el punto 2.8.1. –sin considerar las exclusiones allí
previstas– y que cumplan con el criterio previsto en el punto 2.8.3.1. Para
el resto de las exposiciones, el desempeño deberá verificarse durante 7
años. Ello para evitar, por ejemplo, que se originen carteras con el solo fin
de transferirlas.
iii) Estado de cumplimiento de los activos.
A fin de asegurar que sólo se asignen a una titulización documentos a co-
brar o derechos de crédito que no estén en mora, no se podrán transferir
activos en situación de incumplimiento o mora u obligaciones respecto de
las cuales el originante o el fiduciario o los demás participantes de la tituli-
zación con responsabilidad fiduciaria cuenten con evidencia de un incre-
mento sustancial en las pérdidas esperadas o que se encuentran en ges-
tión de cobranza.
El originante o fiduciario deberá verificar que los activos cumplan con las
siguientes condiciones:
a) El obligado al pago no ha sido sometido a un proceso de quiebra o de
reestructuración de deuda debido a dificultades financieras en los 3
años previos a la fecha de originación, salvo que resulte de aplicación
el período de 2 años previsto en el art. 26, inciso 4, de la Ley 25.326.
b) El obligado al pago no cuenta con un historial de crédito desfavorable
en algún registro público de crédito.
c) El obligado al pago no cuenta con una evaluación de una agencia de
calificación de créditos o un credit scoring que anticipen un riesgo de
incumplimiento significativo.
d) El documento a cobrar o derecho de crédito transferido no es objeto de
litigios entre el obligado y el acreedor original.
El análisis de estas condiciones deberá ser llevado a cabo por el originan-
te o fiduciario dentro de los 45 días previos a la fecha de la transferencia
de los activos. Al momento de la evaluación, no deberá existir evidencia
que indique la posibilidad de deterioro en el estado de cumplimiento de
los activos.
Adicionalmente, al momento de la inclusión del activo en la cartera de
subyacentes, deberá haberse registrado al menos un pago, excepto en el
caso de las estructuras sobre activos de tipo rotativos (como tarjetas de
crédito, facturas y otras exposiciones cancelables en un solo pago).
iv)Consistencia en la originación de los activos.
El originante deberá demostrar al inversor que los activos transferidos han
sido generados en el curso normal de su negocio bajo estándares de ori-
ginación uniformes y consistentes.
Cuando esos estándares se vean afectados por cambios, el originante
deberá comunicar el momento y el propósito de las modificaciones. Los
estándares no deberán ser menos rigurosos que aquellos aplicados a los
activos retenidos por el originante.
Los documentos a cobrar o derechos de crédito titulizados –incluso cuan-
do formen parte de carteras atomizadas– deberán satisfacer criterios de
originación sólidos y prudentes que incluyan una evaluación de la capaci-
dad e intención de los obligados de cumplir puntualmente con sus obliga-
ciones. Además, en el caso de carteras atomizadas, tales documentos o
derechos deberán ser originados en el curso normal del negocio del origi-
nante y sus flujos de fondos esperados deberán permitir atender las obli-
gaciones establecidas en la titulización aun en escenarios de estrés sufi-
cientemente conservadores respecto de las pérdidas crediticias.
Cuando los activos hayan sido adquiridos a terceros, el originan-
te/fiduciario de la titulización deberá revisar los estándares de originación
de esos terceros –verificando su existencia y calidad– y constatar que el
acreedor original ha examinado y evaluado la habilidad y voluntad de los
obligados de hacer los respectivos pagos de manera puntual.
v) Selección y transferencia de los activos.
El desempeño de la titulización no deberá depender de una selección de
los subyacentes a través de la gestión activa y discrecional de la cartera.
Por el contrario, la selección de los activos deberá estar sujeta a criterios
de elegibilidad claramente definidos, tales como el tamaño de la obliga-
ción, la edad del sujeto de crédito y los ratios “loan-to-value” (LTV), “debt-
to-income” (DTI) y/o “debt service coverage” (DSC).
En la medida en que la selección no sea discrecional, la incorporación de
créditos en los períodos de rotación o su sustitución o recompra debido al
incumplimiento de cláusulas contractuales no se considerará una gestión
activa de la cartera.
Los documentos a cobrar y créditos transferidos luego de la fecha en que
se concreta la titulización tampoco deberán ser seleccionados de manera
discrecional ni gestionados de forma activa. Los inversores deberían po-
der evaluar el riesgo crediticio de la cartera de activos en forma previa a
sus decisiones de inversión.
A efectos de cumplir con el principio de transferencia real, deberá reali-
zarse una cesión efectiva de derechos de forma tal que los documentos a
cobrar y derechos de crédito:
a) constituyan una deuda de los respectivos obligados y ello conste en las
cláusulas de la titulización;
b) estén fuera del alcance del cedente, sus acreedores o liquidadores y
no estén sujetos a riesgos de modificación sustancial de los contratos
o restitución de los activos;
c) hayan sido objeto de una cesión de créditos; es decir, que la transfe-
rencia del riesgo de crédito no se haya efectuado mediante un CDS,
derivado o garantía (titulización sintética); y
d) proporcionen un efectivo derecho contra el último obligado y no consti-
tuyan una titulización de otras titulizaciones; es decir, que no se trate
de retitulizaciones.
El contrato de cesión de los créditos deberá contener cláusulas por las
cuales el originante garantice que los documentos a cobrar o los créditos
que están siendo transferidos para su titulización no están afectados en
garantía ni sujetos a ninguna otra condición o gravamen que, hasta donde
se pueda prever, afecten el cobro de las sumas pendientes.
La documentación que instrumente la titulización deberá incluir una opi-
nión legal independiente que respalde que la transferencia real y la cesión
de derechos bajo la legislación aplicable se ajustan a lo indicado en los
apartados a) a d) anteriores.
En el caso de que la legislación aplicable a la titulización no se ajuste a lo
previsto en los apartados a) a d) precedentes, se deberá demostrar la
existencia de los obstáculos que así lo impiden y especificar el método del
que disponen los inversores para ejercer sus derechos contra los obliga-
dos al pago. Además, de corresponder, deberá informarse toda condición
o evento que pueda retrasar o impedir la transferencia de los activos sub-
yacentes a la titulización así como cualquier factor que pueda afectar el
perfeccionamiento oportuno de los reclamos.
vi) Información inicial y periódica.
A fin de asistir a los inversores en la realización de un apropiado proceso
de debida diligencia en forma previa a la inversión en un nuevo
instrumento, se deberá contar con suficiente información a nivel de cada
préstamo o, en el caso de carteras atomizadas, con datos sobre las
características de riesgo relevantes resumidas a nivel de cada tramo de
activos subyacentes.
Para asistir a los inversores en el seguimiento permanente del desempe-
ño de sus inversiones y para que aquellos inversores que deseen adquirir
una titulización en el mercado secundario tengan información suficiente
para realizar una correcta evaluación de la inversión, se deberá suminis-
trar al menos trimestralmente durante la vida de la titulización datos a ni-
vel de préstamos en función de las regulaciones aplicables o, en el caso
de las carteras atomizadas, datos resumidos a nivel de cada tramo de ac-
tivos subyacentes, así como también informes estandarizados dirigidos al
inversor. Las fechas de corte de los datos deberán estar en línea con las
utilizadas para la emisión de los informes.
A efectos de generar confianza respecto tanto de la exactitud de lo infor-
mado sobre los activos subyacentes como de que estos activos cumplen
con los requisitos de elegibilidad –acápite v) precedente–, la cartera inicial
deberá ser revisada por un contador público independiente.
```

**Lectura: INCORRECTA.** Sujeto según el texto: el originante o fiduciario. El texto de la unidad dice «El originante o fiduciario deberá verificar que los activos cumplan con las siguientes condiciones» y «El análisis de estas condiciones deberá ser llevado a cabo por el originante o fiduciario». El fiduciario no es miembro del rol de cap (entidades financieras); la norma extraída, además, describe al obligado al pago.

**Adjudicación de la autora:** PENDIENTE

### F10 — cap, `cap::3.1.14.2` (punto 3.1.14.2), Obligacion

- **Norma:** Eventos desencadenantes claramente establecidos
- **Descripción:** Todos los eventos desencadenantes que puedan afectar el orden de prelación en los pagos de la titulización deberán estar claramente establecidos en los documentos de oferta de la transacción y en los reportes a los inversores.
- **Tramo:** A los efectos de garantizar total transparencia a los inversores, todos los eventos desencadenantes que puedan afectar el orden de prelación en los pagos de la titulización deberán estar claramente establecidos en los documentos de oferta de la transacción y en los reportes a los inversores.
- **Rol de alcance del documento:** `Sujeto_rol_alcance_capmin` — Entidades alcanzadas (Capitales Mínimos) (miembros: Entidades financieras)
- **Categoría:** sin_aplica_a; cola humana: no; índice en la población: 477
- **Relaciones aplica_a que emitió el modelo:** ninguna

**Texto heredado.**

> [S3, encabezado] Sección 3. Capital mínimo por riesgo de crédito. Titulizaciones e inversiones en fon- dos.
> [3.1, encabezado] 3.1. Tratamiento de las titulizaciones.
> [3.1, intro] Se denomina “posición de titulización” a la exposición a una titulización (o retitulización), tradi- cional o sintética, o a una estructura con similares características. La exposición a los riesgos de una titulización puede surgir, entre otros, de los siguientes con- ceptos: tenencia de títulos valores emitidos en el marco de la titulización –es decir, títulos de deuda y/o certificados de participación, tales como bonos de titulización de activos (“Asset- Backed Securities”, ABS) y bonos de titulización hipotecaria (“Mortgage-Backed Securities”, MBS)–, mejoras crediticias, facilidades de liquidez, “swaps” de tasa de interés o de monedas y derivados de crédito. Las reservas (“reserve accounts”), tales como las cuentas de garantía en efectivo, se considerarán como un activo para la entidad financiera originante, recibiendo tam- bién el tratamiento de posiciones de titulización. Dado que las titulizaciones pueden estructurarse de diferentes formas, la exigencia de capital para una posición de titulización se determinará teniendo en cuenta su realidad o finalidad eco- nómica y no su forma jurídica. En los casos en que exista incertidumbre acerca de si una de- terminada operación debe considerarse como titulización, la entidad deberá aplicar el criterio que estime mejor se ajusta a la realidad económica de la operación e informar a la SEFyC los fundamentos que lo sustenten.
> [3.1.14, encabezado] 3.1.14. Criterios para la determinación de titulizaciones simples, transparentes y comparables.
> [3.1.14, intro] A los fines de establecer el ponderador de riesgo a aplicar de acuerdo con el enfoque estandarizado –punto 3.1.11.–, una titulización se considerará simple, transparente y comparable (STC) si: -se trata de una titulización tradicional que no constituye un programa ABCP; - involucra una transferencia real de activos –en los términos del acápite v) del punto
> [3.1.14, intro] 3.1.14.1.–; y
> [3.1.14, intro] - cumple con la totalidad de los criterios previstos en el presente punto (en adelante,
> [3.1.14, intro] “criterios STC”).
> [3.1.14, intro] El originante/fiduciario deberá divulgar toda la información necesaria respecto de la transacción que permita a los inversores determinar si la titulización cumple con los cri- terios STC. En base a la información provista, el inversor deberá realizar sus propias evaluaciones respecto del cumplimiento de estos criterios previo a la aplicación del en- foque estandarizado. Para las posiciones retenidas en las que el originante haya transferido el riesgo de acuerdo con lo establecido en los puntos 3.1.2.2. y 3.1.8.2. la determinación respecto del cumplimiento de los criterios será efectuada únicamente por la entidad originante. Los criterios STC deberán cumplirse en todo momento. Algunos de los criterios se de- berán verificar sólo al momento de la originación o cuando se genere la posición –si és- ta es posterior–, tal como en el caso de las garantías y las facilidades de liquidez. No obstante, los inversores y tenedores de las posiciones de titulización deberán tener en cuenta las modificaciones que puedan invalidar las evaluaciones de cumplimiento pre- vias, tales como las deficiencias en la frecuencia y en el contenido de los informes a los inversores o los cambios en la documentación contrarios a los criterios STC. En los casos en que los criterios hagan referencia a activos subyacentes –incluidos los criterios previstos en el punto 3.1.14.4.– y el conjunto de subyacentes admita la incorpo- ración de nuevos activos, el cumplimiento estará sujeto a que se realicen verificaciones cada vez que se incorporen esos nuevos activos. Cuando la SEFyC detecte que una titulización no cumple con alguno de los criterios, podrá exigir la implementación de acciones correctivas y/o determinar que se suspenda el tratamiento STC para una o más posiciones de titulización.

**Texto de la unidad.**

```
3.1.14.2. Riesgo estructural.
i) Pago de los compromisos.
El pago de los compromisos de una titulización no deberá depender de la
venta o refinanciación de los activos subyacentes, excepto que la cartera
subyacente esté lo suficientemente atomizada y su perfil de repago esté
suficientemente distribuido. De esta manera, se contribuye a que los acti-
vos subyacentes no necesiten ser refinanciados en el corto plazo.
El derecho a la renta que generen los activos designados para respaldar
pagos –tales como planes de ahorros cuya finalidad sea el repago del
principal a su vencimiento– se considerarán como documentos a cobrar o
derechos de crédito elegibles a estos efectos.
ii) Descalce de tasa y moneda de los activos y pasivos.
Para reducir el riesgo que surge de los distintos perfiles de tasa de interés
y de moneda de los activos y pasivos y con el fin de mejorar la capacidad
de los inversores de modelar los flujos de fondos, los riesgos de tasa de
interés y de moneda extranjera deberán mitigarse en forma adecuada, sin
que esto implique que deba obtenerse una cobertura perfecta y completa
de dichos riesgos.
Se deberá demostrar que tales riesgos son adecuadamente mitigados a
través de información cuantitativa que tiene que estar disponible para los
potenciales inversores de manera oportuna y regular. Esa información
deberá incluir la porción del monto nocional cubierto, así como un análisis
de sensibilidad que demuestre la eficacia de la cobertura bajo escenarios
extremos pero plausibles. El alcance y adecuación de la cobertura debe-
rán ser explicados y divulgados a los inversores durante toda la vida de la
titulización. Los contratos que instrumenten las operaciones de cobertura
deberán ser los usuales en la industria.
Los únicos derivados admisibles son los que se toman para la genuina
cobertura de los descalces de tasa y de moneda de los activos y pasivos
de la titulización.
Las coberturas que no se realicen a través de derivados sólo serán admi-
sibles si han sido especialmente creadas y usadas para cubrir un riesgo
específico individual y no múltiples riesgos simultáneamente –tales como
los riesgos de crédito y de tasa de interés–. Además, deberán estar dis-
ponibles y haber sido íntegramente fondeadas.
iii) Orden de prelación en el pago y su constatación.
El orden de prelación en el pago de todos los compromisos deberá estar
claramente definido desde el inicio y contar con apropiado respaldo jurídi-
co en lo relativo a su validez legal.
Los títulos valores subordinados no deberán tener preferencia de pago
sobre los títulos valores exigibles con mayor prelación. La titulización no
debe ser estructurada como una cascada inversa de modo que los com-
promisos subordinados sean cancelados habiendo obligaciones preferen-
tes vencidas que permanezcan impagas.
A los efectos de garantizar total transparencia a los inversores, todos los
eventos desencadenantes que puedan afectar el orden de prelación en
los pagos de la titulización deberán estar claramente establecidos en los
documentos de oferta de la transacción y en los reportes a los inversores.
Los reportes deberán contener información que identifique cualquier in-
cumplimiento, sus consecuencias y la capacidad de revertir la situación.
También deberán proveer información que permita realizar un seguimien-
to de la evolución de los indicadores que constituyen eventos desencade-
nantes y, cuando uno de estos eventos ocurra entre dos fechas de pago
previstas, se deberá informar a los inversores en los términos y condicio-
nes establecidos en los documentos de la transacción.
Las titulizaciones con períodos rotativos deberán establecer eventos de
amortización anticipada y/o eventos desencadenantes de la terminación
del período rotativo que incluyan, principalmente, las siguientes situacio-
nes: a) el deterioro de la calidad crediticia de las exposiciones subyacen-
tes; b) la imposibilidad de adquirir suficientes exposiciones nuevas de ca-
lidad crediticia similar a las subyacentes; y c) la ocurrencia de un evento
que indica la insolvencia del originante o fiduciario.
Luego de la ocurrencia de un incumplimiento u otro evento desencade-
nante de la aceleración de los reembolsos, las posiciones deberán ser
canceladas en forma secuencial, de acuerdo con la preferencia de cada
tramo. No deberán existir disposiciones que requieran la inmediata liqui-
dación de los activos subyacentes a valores de mercado.
El originante o fiduciario deberá poner a disposición de los inversores,
tanto antes de determinar el precio de los títulos valores como durante la
vida de la titulización, el modelo de flujos de fondos de los compromisos o
la información que permita a los inversores modelizar apropiadamente la
cascada de pagos de la titulización.
Deberán proporcionarse, en términos claros y consistentes, las políticas y
procedimientos, las definiciones, las acciones y los recursos asociados a
atrasos, impagos o reestructuraciones de los deudores subyacentes, de
modo tal de asegurar que los períodos de gracia, las esperas, condona-
ciones y las reestructuraciones de deuda puedan ser claramente identifi-
cados por los inversores durante la vida de la titulización.
iv) Derechos del inversor.
Todos los derechos inherentes a los documentos a cobrar y créditos de-
berán ser transferidos a la titulización, a los efectos de garantizar a los te-
nedores de los títulos valores claridad sobre sus derechos y su capacidad
de ejercerlos sobre los activos subyacentes aun en caso de insolvencia
del originante o fiduciario.
Los derechos del inversor deberán estar claramente definidos en toda cir-
cunstancia, incluidos los concernientes a los tenedores con preferencia
respecto de los subordinados.
v) Divulgación de documentación y revisión legal.
La documentación provisional inicial –oferta o prospecto provisional– y de
apoyo –tales como los contratos de venta de los activos, de cesión de
créditos, para la prestación de servicios, la administración o la gestión de
fondos, de fideicomiso, de derivados, de emisión de deuda subordinada,
acuerdos de facilidades de liquidez y toda otra documentación relevante,
incluso las opiniones legales–, deberá ser provista con anticipación sufi-
ciente y de manera clara y efectiva para todos los programas y ofertas.
De esta manera, se permitirá que los inversores comprendan los términos
y condiciones, la información legal y comercial, así como los factores de
riesgos involucrados, en forma previa a la realización de una inversión.
La documentación final de la oferta o el prospecto deberá estar disponible
desde la fecha en que se concrete la titulización y la documentación final
de apoyo tan pronto como sea posible. Toda esa documentación deberá
ser apropiadamente revisada por consultores legales independientes con
anterioridad a su publicación y deberá permitir a los lectores encontrar,
usar y comprender toda la información relevante para la toma de decisio-
nes.
Los inversores deberán ser notificados con la debida anticipación respec-
to de cualquier cambio en la documentación que pueda afectar los riesgos
estructurales de la titulización.
vi) Alineación de intereses.
A efectos de alinear los intereses de los acreedores originales de los acti-
vos titulizados con los de los inversores, el que origine o activamente
promocione una titulización deberá retener una exposición significativa en
dichos activos que demuestre que tiene un incentivo financiero concreto
respecto de su desempeño con posterioridad al inicio de la titulización.
```

**Lectura: DUDOSA.** Sujeto según el texto: la estructura de la titulización; el heredado pone la divulgación en cabeza del originante/fiduciario. Requisito de transparencia de la titulización STC («deberán estar claramente establecidos en los documentos de oferta»), en pasiva. El heredado del punto 3.1.14 dice que «El originante/fiduciario deberá divulgar toda la información»; la consecuencia (el ponderador STC) recae en la entidad que tiene la posición. No es la entidad la que redacta los documentos de oferta.

**Adjudicación de la autora:** PENDIENTE

### F11 — cap, `cap::3.1.14.2` (punto 3.1.14.2), Obligacion

- **Norma:** Cancelación posiciones secuencial tras incumplimiento
- **Descripción:** Luego de la ocurrencia de un incumplimiento u otro evento desencadenante de la aceleración de los reembolsos, las posiciones deberán ser canceladas en forma secuencial, de acuerdo con la preferencia de cada tramo.
- **Tramo:** Luego de la ocurrencia de un incumplimiento u otro evento desencadenante de la aceleración de los reembolsos, las posiciones deberán ser canceladas en forma secuencial, de acuerdo con la preferencia de cada tramo.
- **Rol de alcance del documento:** `Sujeto_rol_alcance_capmin` — Entidades alcanzadas (Capitales Mínimos) (miembros: Entidades financieras)
- **Categoría:** sin_aplica_a; cola humana: no; índice en la población: 481
- **Relaciones aplica_a que emitió el modelo:** ninguna

**Texto heredado.**

> [S3, encabezado] Sección 3. Capital mínimo por riesgo de crédito. Titulizaciones e inversiones en fon- dos.
> [3.1, encabezado] 3.1. Tratamiento de las titulizaciones.
> [3.1, intro] Se denomina “posición de titulización” a la exposición a una titulización (o retitulización), tradi- cional o sintética, o a una estructura con similares características. La exposición a los riesgos de una titulización puede surgir, entre otros, de los siguientes con- ceptos: tenencia de títulos valores emitidos en el marco de la titulización –es decir, títulos de deuda y/o certificados de participación, tales como bonos de titulización de activos (“Asset- Backed Securities”, ABS) y bonos de titulización hipotecaria (“Mortgage-Backed Securities”, MBS)–, mejoras crediticias, facilidades de liquidez, “swaps” de tasa de interés o de monedas y derivados de crédito. Las reservas (“reserve accounts”), tales como las cuentas de garantía en efectivo, se considerarán como un activo para la entidad financiera originante, recibiendo tam- bién el tratamiento de posiciones de titulización. Dado que las titulizaciones pueden estructurarse de diferentes formas, la exigencia de capital para una posición de titulización se determinará teniendo en cuenta su realidad o finalidad eco- nómica y no su forma jurídica. En los casos en que exista incertidumbre acerca de si una de- terminada operación debe considerarse como titulización, la entidad deberá aplicar el criterio que estime mejor se ajusta a la realidad económica de la operación e informar a la SEFyC los fundamentos que lo sustenten.
> [3.1.14, encabezado] 3.1.14. Criterios para la determinación de titulizaciones simples, transparentes y comparables.
> [3.1.14, intro] A los fines de establecer el ponderador de riesgo a aplicar de acuerdo con el enfoque estandarizado –punto 3.1.11.–, una titulización se considerará simple, transparente y comparable (STC) si: -se trata de una titulización tradicional que no constituye un programa ABCP; - involucra una transferencia real de activos –en los términos del acápite v) del punto
> [3.1.14, intro] 3.1.14.1.–; y
> [3.1.14, intro] - cumple con la totalidad de los criterios previstos en el presente punto (en adelante,
> [3.1.14, intro] “criterios STC”).
> [3.1.14, intro] El originante/fiduciario deberá divulgar toda la información necesaria respecto de la transacción que permita a los inversores determinar si la titulización cumple con los cri- terios STC. En base a la información provista, el inversor deberá realizar sus propias evaluaciones respecto del cumplimiento de estos criterios previo a la aplicación del en- foque estandarizado. Para las posiciones retenidas en las que el originante haya transferido el riesgo de acuerdo con lo establecido en los puntos 3.1.2.2. y 3.1.8.2. la determinación respecto del cumplimiento de los criterios será efectuada únicamente por la entidad originante. Los criterios STC deberán cumplirse en todo momento. Algunos de los criterios se de- berán verificar sólo al momento de la originación o cuando se genere la posición –si és- ta es posterior–, tal como en el caso de las garantías y las facilidades de liquidez. No obstante, los inversores y tenedores de las posiciones de titulización deberán tener en cuenta las modificaciones que puedan invalidar las evaluaciones de cumplimiento pre- vias, tales como las deficiencias en la frecuencia y en el contenido de los informes a los inversores o los cambios en la documentación contrarios a los criterios STC. En los casos en que los criterios hagan referencia a activos subyacentes –incluidos los criterios previstos en el punto 3.1.14.4.– y el conjunto de subyacentes admita la incorpo- ración de nuevos activos, el cumplimiento estará sujeto a que se realicen verificaciones cada vez que se incorporen esos nuevos activos. Cuando la SEFyC detecte que una titulización no cumple con alguno de los criterios, podrá exigir la implementación de acciones correctivas y/o determinar que se suspenda el tratamiento STC para una o más posiciones de titulización.

**Texto de la unidad.**

```
3.1.14.2. Riesgo estructural.
i) Pago de los compromisos.
El pago de los compromisos de una titulización no deberá depender de la
venta o refinanciación de los activos subyacentes, excepto que la cartera
subyacente esté lo suficientemente atomizada y su perfil de repago esté
suficientemente distribuido. De esta manera, se contribuye a que los acti-
vos subyacentes no necesiten ser refinanciados en el corto plazo.
El derecho a la renta que generen los activos designados para respaldar
pagos –tales como planes de ahorros cuya finalidad sea el repago del
principal a su vencimiento– se considerarán como documentos a cobrar o
derechos de crédito elegibles a estos efectos.
ii) Descalce de tasa y moneda de los activos y pasivos.
Para reducir el riesgo que surge de los distintos perfiles de tasa de interés
y de moneda de los activos y pasivos y con el fin de mejorar la capacidad
de los inversores de modelar los flujos de fondos, los riesgos de tasa de
interés y de moneda extranjera deberán mitigarse en forma adecuada, sin
que esto implique que deba obtenerse una cobertura perfecta y completa
de dichos riesgos.
Se deberá demostrar que tales riesgos son adecuadamente mitigados a
través de información cuantitativa que tiene que estar disponible para los
potenciales inversores de manera oportuna y regular. Esa información
deberá incluir la porción del monto nocional cubierto, así como un análisis
de sensibilidad que demuestre la eficacia de la cobertura bajo escenarios
extremos pero plausibles. El alcance y adecuación de la cobertura debe-
rán ser explicados y divulgados a los inversores durante toda la vida de la
titulización. Los contratos que instrumenten las operaciones de cobertura
deberán ser los usuales en la industria.
Los únicos derivados admisibles son los que se toman para la genuina
cobertura de los descalces de tasa y de moneda de los activos y pasivos
de la titulización.
Las coberturas que no se realicen a través de derivados sólo serán admi-
sibles si han sido especialmente creadas y usadas para cubrir un riesgo
específico individual y no múltiples riesgos simultáneamente –tales como
los riesgos de crédito y de tasa de interés–. Además, deberán estar dis-
ponibles y haber sido íntegramente fondeadas.
iii) Orden de prelación en el pago y su constatación.
El orden de prelación en el pago de todos los compromisos deberá estar
claramente definido desde el inicio y contar con apropiado respaldo jurídi-
co en lo relativo a su validez legal.
Los títulos valores subordinados no deberán tener preferencia de pago
sobre los títulos valores exigibles con mayor prelación. La titulización no
debe ser estructurada como una cascada inversa de modo que los com-
promisos subordinados sean cancelados habiendo obligaciones preferen-
tes vencidas que permanezcan impagas.
A los efectos de garantizar total transparencia a los inversores, todos los
eventos desencadenantes que puedan afectar el orden de prelación en
los pagos de la titulización deberán estar claramente establecidos en los
documentos de oferta de la transacción y en los reportes a los inversores.
Los reportes deberán contener información que identifique cualquier in-
cumplimiento, sus consecuencias y la capacidad de revertir la situación.
También deberán proveer información que permita realizar un seguimien-
to de la evolución de los indicadores que constituyen eventos desencade-
nantes y, cuando uno de estos eventos ocurra entre dos fechas de pago
previstas, se deberá informar a los inversores en los términos y condicio-
nes establecidos en los documentos de la transacción.
Las titulizaciones con períodos rotativos deberán establecer eventos de
amortización anticipada y/o eventos desencadenantes de la terminación
del período rotativo que incluyan, principalmente, las siguientes situacio-
nes: a) el deterioro de la calidad crediticia de las exposiciones subyacen-
tes; b) la imposibilidad de adquirir suficientes exposiciones nuevas de ca-
lidad crediticia similar a las subyacentes; y c) la ocurrencia de un evento
que indica la insolvencia del originante o fiduciario.
Luego de la ocurrencia de un incumplimiento u otro evento desencade-
nante de la aceleración de los reembolsos, las posiciones deberán ser
canceladas en forma secuencial, de acuerdo con la preferencia de cada
tramo. No deberán existir disposiciones que requieran la inmediata liqui-
dación de los activos subyacentes a valores de mercado.
El originante o fiduciario deberá poner a disposición de los inversores,
tanto antes de determinar el precio de los títulos valores como durante la
vida de la titulización, el modelo de flujos de fondos de los compromisos o
la información que permita a los inversores modelizar apropiadamente la
cascada de pagos de la titulización.
Deberán proporcionarse, en términos claros y consistentes, las políticas y
procedimientos, las definiciones, las acciones y los recursos asociados a
atrasos, impagos o reestructuraciones de los deudores subyacentes, de
modo tal de asegurar que los períodos de gracia, las esperas, condona-
ciones y las reestructuraciones de deuda puedan ser claramente identifi-
cados por los inversores durante la vida de la titulización.
iv) Derechos del inversor.
Todos los derechos inherentes a los documentos a cobrar y créditos de-
berán ser transferidos a la titulización, a los efectos de garantizar a los te-
nedores de los títulos valores claridad sobre sus derechos y su capacidad
de ejercerlos sobre los activos subyacentes aun en caso de insolvencia
del originante o fiduciario.
Los derechos del inversor deberán estar claramente definidos en toda cir-
cunstancia, incluidos los concernientes a los tenedores con preferencia
respecto de los subordinados.
v) Divulgación de documentación y revisión legal.
La documentación provisional inicial –oferta o prospecto provisional– y de
apoyo –tales como los contratos de venta de los activos, de cesión de
créditos, para la prestación de servicios, la administración o la gestión de
fondos, de fideicomiso, de derivados, de emisión de deuda subordinada,
acuerdos de facilidades de liquidez y toda otra documentación relevante,
incluso las opiniones legales–, deberá ser provista con anticipación sufi-
ciente y de manera clara y efectiva para todos los programas y ofertas.
De esta manera, se permitirá que los inversores comprendan los términos
y condiciones, la información legal y comercial, así como los factores de
riesgos involucrados, en forma previa a la realización de una inversión.
La documentación final de la oferta o el prospecto deberá estar disponible
desde la fecha en que se concrete la titulización y la documentación final
de apoyo tan pronto como sea posible. Toda esa documentación deberá
ser apropiadamente revisada por consultores legales independientes con
anterioridad a su publicación y deberá permitir a los lectores encontrar,
usar y comprender toda la información relevante para la toma de decisio-
nes.
Los inversores deberán ser notificados con la debida anticipación respec-
to de cualquier cambio en la documentación que pueda afectar los riesgos
estructurales de la titulización.
vi) Alineación de intereses.
A efectos de alinear los intereses de los acreedores originales de los acti-
vos titulizados con los de los inversores, el que origine o activamente
promocione una titulización deberá retener una exposición significativa en
dichos activos que demuestre que tiene un incentivo financiero concreto
respecto de su desempeño con posterioridad al inicio de la titulización.
```

**Lectura: DUDOSA.** Sujeto según el texto: la estructura de la titulización (orden de cancelación de los tramos). Requisito estructural del orden de pago («las posiciones deberán ser canceladas en forma secuencial»), en pasiva; lo cumple quien estructura y administra la titulización (originante/fiduciario), y la entidad solo lo verifica para aplicar el tratamiento STC.

**Adjudicación de la autora:** PENDIENTE

### F12 — cap, `cap::4.2.1::intro` (punto 4.2.1), Obligacion

- **Norma:** Aforo de activos recibidos en garantía
- **Descripción:** A los efectos de determinar el costo de reposición, el aforo de los activos recibidos en garantía (excepto efectivo) deberá representar el cambio potencial del valor de dicha garantía durante el período relevante: un año para operaciones sin márgenes, y el período de riesgo de margen para operaciones con márgenes.
- **Tramo:** el aforo de los activos recibidos en garantía (excepto efectivo) representará el cambio potencial del valor de dicha garantía durante el período relevante –un año, para las operaciones sin márgenes, y el período de riesgo de margen, para las operaciones con márgenes–.
- **Rol de alcance del documento:** `Sujeto_rol_alcance_capmin` — Entidades alcanzadas (Capitales Mínimos) (miembros: Entidades financieras)
- **Categoría:** sin_aplica_a; cola humana: no; índice en la población: 527
- **Relaciones aplica_a que emitió el modelo:** ninguna

**Texto heredado.**

> [S4, encabezado] Sección 4. Capital mínimo por riesgo de crédito de contraparte.
> [4.2, encabezado] 4.2. Exigencia de capital por riesgo de crédito de contraparte en operaciones con derivados
> [4.2.1, encabezado] 4.2.1. Exposición al riesgo de crédito de contraparte.

**Texto de la unidad.**

```
La exposición al riesgo de crédito de contraparte (EAD) se calculará por separado para
cada conjunto de neteo (“netting set”, NS) y se determinará del siguiente modo:
donde:
α = 1,40.
CR: costo de reposición calculado de acuerdo con el punto 4.2.1.1.
EPF: exposición potencial futura calculado de acuerdo con el punto 4.2.1.2.
El cálculo del CR y de la EPF diferirá según que los conjuntos de neteo estén sujetos o
no al intercambio de márgenes de variación:
− Operaciones sin margen de variación: el CR representa la pérdida que ocurriría
ante el incumplimiento de la contraparte y la liquidación inmediata de sus opera-
ciones y la EPF adicionará el incremento probable de la exposición, calculado de
modo conservador, en el horizonte temporal de un año a partir de la fecha de
cálculo.
− Operaciones con margen de variación: el CR representa la pérdida que ocurriría
ante el incumplimiento de la contraparte –en el presente o en el futuro– si la liqui-
dación y reposición de las operaciones fueran instantáneas. Dado que puede ha-
ber un lapso –período de riesgo de margen (“MPOR”)– entre el último intercambio
de garantías antes del incumplimiento y la reposición, el adicional por la EPF re-
presenta el potencial cambio de valor de las operaciones durante ese período.
En ambos casos, y a los efectos de determinar el costo de reposición, el aforo de los
activos recibidos en garantía (excepto efectivo) representará el cambio potencial del
valor de dicha garantía durante el período relevante –un año, para las operaciones sin
márgenes, y el período de riesgo de margen, para las operaciones con márgenes–.
Además:
− La EAD para un conjunto de neteo con márgenes de variación tendrá como límite
superior la EAD que resultaría para el mismo conjunto si no los tuviera.
− La EAD de un conjunto de neteo que sólo comprende opciones vendidas podrá
ser cero cuando hayan sido cobradas todas las primas y en tanto dichas opciones
no estén comprendidas en acuerdos de neteo que incluyan otros productos o la
constitución de márgenes.
```

**Lectura: CORRECTA.** Sujeto según el texto: la entidad que calcula la exposición al riesgo de contraparte. Regla de cálculo del costo de reposición (aforo de las garantías recibidas) dentro del cálculo de la EAD, que hace la entidad alcanzada.

**Adjudicación de la autora:** PENDIENTE

### F13 — cap, `cap::4.3.3.1` (punto 4.3.3.1), Restriccion

- **Norma:** Ponderador 4% — cliente sin protección contra insolvencia conjunta
- **Descripción:** Cuando cliente no está protegido contra pérdidas por falta de pago/insolvencia conjunta del miembro compensador y alguno de sus clientes, pero se cumplen otras condiciones, exposición recibe ponderador de riesgo del 4%.
- **Tramo:** Cuando el cliente no esté protegido de sufrir pérdidas en caso de falta de pago o insolvencia conjunta del miembro compensador y alguno de sus clientes, pero se cumplan todas las restantes condiciones anteriormente expuestas, la exposición del cliente con el miembro compensador o frente al cliente de mayor nivel, respectivamente, recibirá un ponderador de riesgo del 4%.
- **Rol de alcance del documento:** `Sujeto_rol_alcance_capmin` — Entidades alcanzadas (Capitales Mínimos) (miembros: Entidades financieras)
- **Categoría:** sin_aplica_a; cola humana: no; índice en la población: 586
- **Relaciones aplica_a que emitió el modelo:** ninguna

**Texto heredado.**

> [S4, encabezado] Sección 4. Capital mínimo por riesgo de crédito de contraparte.
> [4.3, encabezado] 4.3. Exigencia de capital por riesgo de crédito de contraparte en operaciones con entidades de
> [4.3, intro] contraparte central. Comprende a aquellas exposiciones de las entidades financieras con entidades de contrapar- te central (CCP) que se originen en derivados OTC o negociados en mercados de valores y en operaciones de financiación con títulos valores (“Securities Financing Transactions”, SFT) y operaciones de liquidación diferida –definidas en el punto 4.2.–. No están comprendidas las exposiciones originadas en operaciones al contado y que involu- cren títulos valores, oro o moneda extranjera, cuya exigencia de capital se calculará conforme a lo previsto en el punto 4.1.
> [4.3.3, encabezado] 4.3.3. Exposiciones a entidades de contraparte central calificadas.

**Texto de la unidad.**

```
4.3.3.1. Exposiciones por operaciones de negociación.
i) Exposiciones de los miembros compensadores con las CCP.
a) La entidad financiera que actúe en carácter de miembro compensa-
dor de una CCP por operaciones propias deberá aplicar un pondera-
dor de riesgo del 2 % a sus exposiciones con la CCP originadas en
operaciones de derivados –OTC o negociados en mercados de valo-
res–, de financiación con títulos valores (SFT) y de liquidación diferi-
da. Cuando la entidad financiera preste servicios de compensación a
clientes, aplicará el ponderador de riesgo del 2 % a la exposición con
la CCP que se origina si, en caso de incumplimiento de la CCP, la
entidad financiera se viera obligada –como miembro compensador a
reembolsar al cliente toda pérdida debido al cambio de valor de sus
transacciones. El ponderador de riesgo aplicado a los activos en ga-
rantía aportados por la entidad financiera a una CCP deberá determi-
narse de acuerdo con lo establecido en los párrafos primero a tercero
del acápite iv) del presente punto.
b) La exposición debida a dichas operaciones se calculará conforme al
enfoque estandarizado para el riesgo de crédito de contraparte (SA-
CCR) establecido en el punto 4.2. para los derivados OTC o negó
ciados en mercados de valores y operaciones de liquidación diferida,
y a lo previsto en la Sección 5. para las SFT.
No se aplicará el plazo mínimo de veinte días hábiles para el cálculo
del período de riesgo de margen (MPOR) de los conjuntos de neteo
en los que se verifiquen más de 5.000 operaciones en la medida en
que no existan disputas pendientes y que dicho conjunto no contenga
garantías ilíquidas u operaciones exóticas. Idéntico criterio se aplica-
rá para la determinación del período de mantenimiento mínimo (T )
M
utilizado en el cálculo de los aforos de las SFT previsto en el punto
5.3.2.3.
En todos los casos, se utilizará un MPOR mínimo de 10 días para el
cálculo de las exposiciones a una CCP por operaciones de derivados
OTC.
Cuando la CCP reciba el margen de variación de una operación y el
activo propiedad del miembro compensador no esté protegido contra
la insolvencia de la CCP, el horizonte temporal de riesgo mínimo a
aplicar a dichas exposiciones será el menor entre 1 año y el plazo re-
sidual de la operación, con un plazo mínimo de 10 días hábiles.
c) En las operaciones con CCP radicadas en jurisdicciones en las cua-
les la liquidación por saldos netos en caso de incumplimiento tenga
validez legal y con independencia de si la contraparte es insolvente o
se ha declarado en quiebra, el costo de reposición total de todos los
contratos relevantes para determinar la exposición por operaciones
podrá calcularse como un costo de reposición neto, siempre que el
conjunto de operaciones compensables aplicable a dicha liquidación
cumpla con los requisitos que en materia de validez legal se estable-
cen en: i. el punto 5.3.2.5. para las SFT y ii. el acápite ii) del punto
4.2.1.1. en el caso de las operaciones con derivados.
En la medida en que las disposiciones antes referidas contengan la
expresión “acuerdo marco de neteo” o la frase “un contrato de neteo
con una contraparte u otro acuerdo”, deberá interpretarse que incluye
a todo acuerdo de neteo con validez legal que reconozca derechos
de compensación legalmente exigibles. Si la entidad financiera no
pudiese demostrar que los acuerdos de neteo cumplen estos reque-
rimientos, cada transacción individual se considerará como un con-
junto de neteo en sí misma a los efectos de calcular la exposición por
operaciones.
ii) Exposiciones de los miembros compensadores con sus clientes.
El miembro compensador considerará su exposición con un cliente
–incluyendo la potencial exposición al riesgo CVA– como una operación
bilateral, independientemente de que el miembro compensador garantice
la operación o actúe como un intermediario entre el cliente y la CCP. Sin
embargo, como el período de liquidación (close-out) para las operaciones
compensadas de los clientes es más corto, los miembros compensado-
res podrán calcular la exigencia por la exposición a sus
clientes aplicando un período de riesgo de margen que sea, como mí-
nimo, de 5 días. La EAD reducida se utilizará también para el cálculo
del ajuste de valuación de crédito –CVA– establecido en el punto 4.2.3.
Si un miembro compensador recibe activos en garantía por las opera-
ciones a compensar del cliente y las transfiere a la CCP, el miembro
compensador podrá reconocer esta garantía tanto para el tramo CCP-
miembro compensador como para el tramo miembro compensador-
cliente de la operación. El margen inicial aportado por los clientes al
miembro compensador mitigará su exposición respecto de sus clientes.
Similar tratamiento se aplicará a las estructuras multinivel de clientes
–entre clientes de nivel superior e inferior–.
iii) Exposiciones de los clientes.
Si la entidad financiera es cliente de un miembro compensador y realiza
una transacción en la que el miembro compensador actúa como inter-
mediario financiero –es decir, el miembro compensador realiza una
transacción con la CCP por indicación del cliente–, la exposición de la
entidad financiera hacia el miembro compensador podrá recibir el trata-
miento del acápite i) precedente, siempre que se cumplan las siguientes
condiciones:
a) La CCP identifica a las transacciones a compensar como transac-
ciones de clientes y las garantías que las amparan son mantenidas
por la CCP y/o el miembro compensador, según sea el caso, bajo
acuerdos que impiden que el cliente sufra pérdidas debido a: i. la
falta de pago o la insolvencia del miembro compensador; ii. la falta
de pago o la insolvencia de los demás clientes del miembro com-
pensador; y iii. la falta de pago o la insolvencia conjuntas del miem-
bro compensador y cualquiera de sus otros clientes. Esto implica
que, en caso de impago o insolvencia del miembro compensador,
no habrá impedimentos legales –salvo la necesidad de obtener una
orden judicial, a la cual el cliente tiene derecho– para transferir la
garantía que pertenece a los clientes de ese miembro compensador
a la CCP, a otro u otros miembros compensadores, al cliente o a
quien éste designe.
El cliente deberá haber realizado una revisión legal adecuada –y
llevar a cabo esas revisiones cuando sea necesario a fin de asegu-
rar una continua aplicabilidad– y contar con fundamentos que per-
mitan concluir que esos acuerdos serán legales, válidos, vinculan-
tes y exigibles bajo las leyes aplicables en la/s jurisdicción/es rele-
vante/s.
b) Las leyes, regulaciones y acuerdos contractuales o administrativos
aplicables hacen que sea altamente probable la portabilidad de las
transacciones. Esto es que las transacciones compensadoras reali-
zadas a través del miembro compensador en situación de impago o
insolvencia serán concluidas indirectamente a través de la CCP o por
la CCP. En tal caso, las posiciones y garantías del cliente con la CCP
serán transferidas a valor de mercado, a menos que el cliente peti-
cione cerrar las posiciones a valor de mercado.
Idénticas condiciones se deberán cumplir para que la entidad financiera
dé ese tratamiento a su exposición con una CCP por transacciones reali-
zadas en calidad de cliente en las que su cumplimiento es garantizado
por un miembro compensador y para las exposiciones de los clientes de
nivel inferior con los clientes de nivel superior en las estructuras multini-
veles, siempre que en todos los niveles de los clientes involucrados se
cumplan las dos condiciones de este acápite.
Cuando el cliente no esté protegido de sufrir pérdidas en caso de falta de
pago o insolvencia conjunta del miembro compensador y alguno de sus
clientes, pero se cumplan todas las restantes condiciones anteriormente
expuestas, la exposición del cliente con el miembro compensador o fren-
te al cliente de mayor nivel, respectivamente, recibirá un ponderador de
riesgo del 4%.
Cuando la entidad financiera sea cliente del miembro compensador y no
se cumplan estos requisitos, la exposición con el miembro compensador,
incluida –de corresponder– la exposición potencial por riesgo CVA, se
deberá tratar como una operación bilateral.
iv) Tratamiento de las garantías.
Todo activo que la entidad financiera constituya en garantía de estas
operaciones recibirá el ponderador que le corresponda de acuerdo con lo
previsto en estas normas, considerando a ese efecto qué tratamiento
–cartera de negociación o de inversión– hubiera recibido en caso de no
haber sido depositado en la CCP. Cuando los activos de un miembro
compensador o cliente se coloquen en garantía a favor de una CCP o
miembro compensador, pero de modo que no queden protegidos de su
quiebra, la entidad financiera que constituye la garantía deberá reconocer
además el riesgo de crédito que se deriva de la posibilidad de sufrir pér-
didas por la calidad crediticia de la entidad que recibe los activos en ga-
rantía. Es decir que, independientemente de la cartera a la que estén
asignados, los activos constituidos en garantía estarán sujetos también al
requisito de riesgo de crédito de contraparte (SA-CCR) establecido en el
punto 4.2., incluido el incremento por los aforos descriptos en el punto
5.3.2.3., computados de acuerdo con lo previsto en el acápite v) del pun-
to 4.2.1.1.
Cuando la entidad que reciba los activos en garantía sea la CCP, se
aplicará un ponderador del 2 % a las garantías incluidas en la definición
de exposición por operaciones. El ponderador de riesgo correspondien-
te a la CCP se aplicará a los activos o las garantías aportados para
otros fines. La garantía depositada que no esté resguardada en caso de
quiebra deberá ser considerada para el Monto Neto de Garantía Inde-
pendiente (NICA) previsto en el acápite v) del punto 4.2.1.1.
La garantía constituida por el miembro compensador –incluyendo efec-
tivo, títulos valores y otros activos constituidos como garantías, así co-
mo los excesos a los márgenes inicial o de variación– mantenida por un
custodio y protegida de la quiebra de la CCP, no está sujeta a la exi-
gencia de capital por la exposición al riesgo de crédito de contraparte
–esto es, el ponderador de riesgo o la EAD es igual a cero–. A ese efec-
to, se entiende por custodio a un fiduciario o agente que mantenga los
activos bajo un título que no le acuerde ni al custodio ni a sus acreedo-
res un derecho o participación sobre ellos y que garantice que no se
podrá obstaculizar judicialmente la devolución de los activos en caso de
quiebra o insolvencia del custodio.
La garantía constituida por un cliente, mantenida por un custodio y pro-
tegida de la quiebra de la CCP y del miembro compensador y sus otros
clientes no está sujeta a exigencia de capital por riesgo de crédito de
contraparte. Si la garantía es mantenida por la CCP y no está protegida
de su quiebra se le deberá aplicar el ponderador de riesgo del 2 % en
caso de que se cumplan las condiciones a) y b) del acápite iii), o del 4
% si se da el caso del anteúltimo párrafo del acápite iii).
```

**Lectura: CORRECTA.** Sujeto según el texto: la entidad financiera que es cliente del miembro compensador. Ponderador del 4 % para la exposición del cliente con el miembro compensador; el párrafo trata el caso en que la entidad financiera actúa como cliente, y es ella la que aplica el ponderador.

**Adjudicación de la autora:** PENDIENTE

### F14 — cap, `cap::4.3.3.1` (punto 4.3.3.1), Restriccion

- **Norma:** Ponderador 2% — garantía de cliente mantenida por CCP (condiciones cumplidas)
- **Descripción:** Si garantía de cliente es mantenida por CCP sin protección contra su quiebra, se aplica ponderador de riesgo del 2% si se cumplen condiciones a) y b) del acápite iii).
- **Tramo:** Si la garantía es mantenida por la CCP y no está protegida de su quiebra se le deberá aplicar el ponderador de riesgo del 2 % en caso de que se cumplan las condiciones a) y b) del acápite iii)
- **Rol de alcance del documento:** `Sujeto_rol_alcance_capmin` — Entidades alcanzadas (Capitales Mínimos) (miembros: Entidades financieras)
- **Categoría:** sin_aplica_a; cola humana: no; índice en la población: 591
- **Relaciones aplica_a que emitió el modelo:** ninguna

**Texto heredado.**

> [S4, encabezado] Sección 4. Capital mínimo por riesgo de crédito de contraparte.
> [4.3, encabezado] 4.3. Exigencia de capital por riesgo de crédito de contraparte en operaciones con entidades de
> [4.3, intro] contraparte central. Comprende a aquellas exposiciones de las entidades financieras con entidades de contrapar- te central (CCP) que se originen en derivados OTC o negociados en mercados de valores y en operaciones de financiación con títulos valores (“Securities Financing Transactions”, SFT) y operaciones de liquidación diferida –definidas en el punto 4.2.–. No están comprendidas las exposiciones originadas en operaciones al contado y que involu- cren títulos valores, oro o moneda extranjera, cuya exigencia de capital se calculará conforme a lo previsto en el punto 4.1.
> [4.3.3, encabezado] 4.3.3. Exposiciones a entidades de contraparte central calificadas.

**Texto de la unidad.**

```
4.3.3.1. Exposiciones por operaciones de negociación.
i) Exposiciones de los miembros compensadores con las CCP.
a) La entidad financiera que actúe en carácter de miembro compensa-
dor de una CCP por operaciones propias deberá aplicar un pondera-
dor de riesgo del 2 % a sus exposiciones con la CCP originadas en
operaciones de derivados –OTC o negociados en mercados de valo-
res–, de financiación con títulos valores (SFT) y de liquidación diferi-
da. Cuando la entidad financiera preste servicios de compensación a
clientes, aplicará el ponderador de riesgo del 2 % a la exposición con
la CCP que se origina si, en caso de incumplimiento de la CCP, la
entidad financiera se viera obligada –como miembro compensador a
reembolsar al cliente toda pérdida debido al cambio de valor de sus
transacciones. El ponderador de riesgo aplicado a los activos en ga-
rantía aportados por la entidad financiera a una CCP deberá determi-
narse de acuerdo con lo establecido en los párrafos primero a tercero
del acápite iv) del presente punto.
b) La exposición debida a dichas operaciones se calculará conforme al
enfoque estandarizado para el riesgo de crédito de contraparte (SA-
CCR) establecido en el punto 4.2. para los derivados OTC o negó
ciados en mercados de valores y operaciones de liquidación diferida,
y a lo previsto en la Sección 5. para las SFT.
No se aplicará el plazo mínimo de veinte días hábiles para el cálculo
del período de riesgo de margen (MPOR) de los conjuntos de neteo
en los que se verifiquen más de 5.000 operaciones en la medida en
que no existan disputas pendientes y que dicho conjunto no contenga
garantías ilíquidas u operaciones exóticas. Idéntico criterio se aplica-
rá para la determinación del período de mantenimiento mínimo (T )
M
utilizado en el cálculo de los aforos de las SFT previsto en el punto
5.3.2.3.
En todos los casos, se utilizará un MPOR mínimo de 10 días para el
cálculo de las exposiciones a una CCP por operaciones de derivados
OTC.
Cuando la CCP reciba el margen de variación de una operación y el
activo propiedad del miembro compensador no esté protegido contra
la insolvencia de la CCP, el horizonte temporal de riesgo mínimo a
aplicar a dichas exposiciones será el menor entre 1 año y el plazo re-
sidual de la operación, con un plazo mínimo de 10 días hábiles.
c) En las operaciones con CCP radicadas en jurisdicciones en las cua-
les la liquidación por saldos netos en caso de incumplimiento tenga
validez legal y con independencia de si la contraparte es insolvente o
se ha declarado en quiebra, el costo de reposición total de todos los
contratos relevantes para determinar la exposición por operaciones
podrá calcularse como un costo de reposición neto, siempre que el
conjunto de operaciones compensables aplicable a dicha liquidación
cumpla con los requisitos que en materia de validez legal se estable-
cen en: i. el punto 5.3.2.5. para las SFT y ii. el acápite ii) del punto
4.2.1.1. en el caso de las operaciones con derivados.
En la medida en que las disposiciones antes referidas contengan la
expresión “acuerdo marco de neteo” o la frase “un contrato de neteo
con una contraparte u otro acuerdo”, deberá interpretarse que incluye
a todo acuerdo de neteo con validez legal que reconozca derechos
de compensación legalmente exigibles. Si la entidad financiera no
pudiese demostrar que los acuerdos de neteo cumplen estos reque-
rimientos, cada transacción individual se considerará como un con-
junto de neteo en sí misma a los efectos de calcular la exposición por
operaciones.
ii) Exposiciones de los miembros compensadores con sus clientes.
El miembro compensador considerará su exposición con un cliente
–incluyendo la potencial exposición al riesgo CVA– como una operación
bilateral, independientemente de que el miembro compensador garantice
la operación o actúe como un intermediario entre el cliente y la CCP. Sin
embargo, como el período de liquidación (close-out) para las operaciones
compensadas de los clientes es más corto, los miembros compensado-
res podrán calcular la exigencia por la exposición a sus
clientes aplicando un período de riesgo de margen que sea, como mí-
nimo, de 5 días. La EAD reducida se utilizará también para el cálculo
del ajuste de valuación de crédito –CVA– establecido en el punto 4.2.3.
Si un miembro compensador recibe activos en garantía por las opera-
ciones a compensar del cliente y las transfiere a la CCP, el miembro
compensador podrá reconocer esta garantía tanto para el tramo CCP-
miembro compensador como para el tramo miembro compensador-
cliente de la operación. El margen inicial aportado por los clientes al
miembro compensador mitigará su exposición respecto de sus clientes.
Similar tratamiento se aplicará a las estructuras multinivel de clientes
–entre clientes de nivel superior e inferior–.
iii) Exposiciones de los clientes.
Si la entidad financiera es cliente de un miembro compensador y realiza
una transacción en la que el miembro compensador actúa como inter-
mediario financiero –es decir, el miembro compensador realiza una
transacción con la CCP por indicación del cliente–, la exposición de la
entidad financiera hacia el miembro compensador podrá recibir el trata-
miento del acápite i) precedente, siempre que se cumplan las siguientes
condiciones:
a) La CCP identifica a las transacciones a compensar como transac-
ciones de clientes y las garantías que las amparan son mantenidas
por la CCP y/o el miembro compensador, según sea el caso, bajo
acuerdos que impiden que el cliente sufra pérdidas debido a: i. la
falta de pago o la insolvencia del miembro compensador; ii. la falta
de pago o la insolvencia de los demás clientes del miembro com-
pensador; y iii. la falta de pago o la insolvencia conjuntas del miem-
bro compensador y cualquiera de sus otros clientes. Esto implica
que, en caso de impago o insolvencia del miembro compensador,
no habrá impedimentos legales –salvo la necesidad de obtener una
orden judicial, a la cual el cliente tiene derecho– para transferir la
garantía que pertenece a los clientes de ese miembro compensador
a la CCP, a otro u otros miembros compensadores, al cliente o a
quien éste designe.
El cliente deberá haber realizado una revisión legal adecuada –y
llevar a cabo esas revisiones cuando sea necesario a fin de asegu-
rar una continua aplicabilidad– y contar con fundamentos que per-
mitan concluir que esos acuerdos serán legales, válidos, vinculan-
tes y exigibles bajo las leyes aplicables en la/s jurisdicción/es rele-
vante/s.
b) Las leyes, regulaciones y acuerdos contractuales o administrativos
aplicables hacen que sea altamente probable la portabilidad de las
transacciones. Esto es que las transacciones compensadoras reali-
zadas a través del miembro compensador en situación de impago o
insolvencia serán concluidas indirectamente a través de la CCP o por
la CCP. En tal caso, las posiciones y garantías del cliente con la CCP
serán transferidas a valor de mercado, a menos que el cliente peti-
cione cerrar las posiciones a valor de mercado.
Idénticas condiciones se deberán cumplir para que la entidad financiera
dé ese tratamiento a su exposición con una CCP por transacciones reali-
zadas en calidad de cliente en las que su cumplimiento es garantizado
por un miembro compensador y para las exposiciones de los clientes de
nivel inferior con los clientes de nivel superior en las estructuras multini-
veles, siempre que en todos los niveles de los clientes involucrados se
cumplan las dos condiciones de este acápite.
Cuando el cliente no esté protegido de sufrir pérdidas en caso de falta de
pago o insolvencia conjunta del miembro compensador y alguno de sus
clientes, pero se cumplan todas las restantes condiciones anteriormente
expuestas, la exposición del cliente con el miembro compensador o fren-
te al cliente de mayor nivel, respectivamente, recibirá un ponderador de
riesgo del 4%.
Cuando la entidad financiera sea cliente del miembro compensador y no
se cumplan estos requisitos, la exposición con el miembro compensador,
incluida –de corresponder– la exposición potencial por riesgo CVA, se
deberá tratar como una operación bilateral.
iv) Tratamiento de las garantías.
Todo activo que la entidad financiera constituya en garantía de estas
operaciones recibirá el ponderador que le corresponda de acuerdo con lo
previsto en estas normas, considerando a ese efecto qué tratamiento
–cartera de negociación o de inversión– hubiera recibido en caso de no
haber sido depositado en la CCP. Cuando los activos de un miembro
compensador o cliente se coloquen en garantía a favor de una CCP o
miembro compensador, pero de modo que no queden protegidos de su
quiebra, la entidad financiera que constituye la garantía deberá reconocer
además el riesgo de crédito que se deriva de la posibilidad de sufrir pér-
didas por la calidad crediticia de la entidad que recibe los activos en ga-
rantía. Es decir que, independientemente de la cartera a la que estén
asignados, los activos constituidos en garantía estarán sujetos también al
requisito de riesgo de crédito de contraparte (SA-CCR) establecido en el
punto 4.2., incluido el incremento por los aforos descriptos en el punto
5.3.2.3., computados de acuerdo con lo previsto en el acápite v) del pun-
to 4.2.1.1.
Cuando la entidad que reciba los activos en garantía sea la CCP, se
aplicará un ponderador del 2 % a las garantías incluidas en la definición
de exposición por operaciones. El ponderador de riesgo correspondien-
te a la CCP se aplicará a los activos o las garantías aportados para
otros fines. La garantía depositada que no esté resguardada en caso de
quiebra deberá ser considerada para el Monto Neto de Garantía Inde-
pendiente (NICA) previsto en el acápite v) del punto 4.2.1.1.
La garantía constituida por el miembro compensador –incluyendo efec-
tivo, títulos valores y otros activos constituidos como garantías, así co-
mo los excesos a los márgenes inicial o de variación– mantenida por un
custodio y protegida de la quiebra de la CCP, no está sujeta a la exi-
gencia de capital por la exposición al riesgo de crédito de contraparte
–esto es, el ponderador de riesgo o la EAD es igual a cero–. A ese efec-
to, se entiende por custodio a un fiduciario o agente que mantenga los
activos bajo un título que no le acuerde ni al custodio ni a sus acreedo-
res un derecho o participación sobre ellos y que garantice que no se
podrá obstaculizar judicialmente la devolución de los activos en caso de
quiebra o insolvencia del custodio.
La garantía constituida por un cliente, mantenida por un custodio y pro-
tegida de la quiebra de la CCP y del miembro compensador y sus otros
clientes no está sujeta a exigencia de capital por riesgo de crédito de
contraparte. Si la garantía es mantenida por la CCP y no está protegida
de su quiebra se le deberá aplicar el ponderador de riesgo del 2 % en
caso de que se cumplan las condiciones a) y b) del acápite iii), o del 4
% si se da el caso del anteúltimo párrafo del acápite iii).
```

**Lectura: CORRECTA.** Sujeto según el texto: la entidad que constituye la garantía. Ponderador del 2 % a la garantía mantenida por la CCP; lo aplica la entidad financiera que la constituyó («Todo activo que la entidad financiera constituya en garantía», en la misma unidad).

**Adjudicación de la autora:** PENDIENTE

### F15 — cap, `cap::6.5.2` (punto 6.5.2), Restriccion

- **Norma:** Prohibición compensación entre productos básicos
- **Descripción:** No se admite la compensación entre posiciones en diferentes productos básicos ni entre subcategorías diferentes del mismo producto básico
- **Tramo:** No se admite la compensación entre posiciones en diferentes productos básicos ni entre subcategorías diferentes del mismo producto básico
- **Rol de alcance del documento:** `Sujeto_rol_alcance_capmin` — Entidades alcanzadas (Capitales Mínimos) (miembros: Entidades financieras)
- **Categoría:** sin_aplica_a; cola humana: no; índice en la población: 754
- **Relaciones aplica_a que emitió el modelo:** ninguna

**Texto heredado.**

> [S6, encabezado] Sección 6. Capital mínimo por riesgo de mercado.
> [6.5, encabezado] 6.5. Exigencia de capital por riesgo de posiciones en productos básicos –“commodities”–.
> [6.5, intro] Cubre el riesgo de mantener posiciones en productos básicos, incluidos metales preciosos ex- cepto el oro (tratado en el punto 6.4.). A los fines de estas normas, se define como producto básico (o materia prima) –“commodities”– a todo producto físico negociado o negociable en un mercado secundario.

**Texto de la unidad.**

```
6.5.2. Medición de la exposición.
Las posiciones cortas y largas podrán netearse a efectos de calcular las posiciones
abiertas, siempre que se trate de un mismo producto básico. No se admite la compen-
sación entre posiciones en diferentes productos básicos ni entre subcategorías diferen-
tes del mismo producto básico.
Para calcular los requerimientos de capital se deberá expresar cada posición en un pro-
ducto básico (al contado y a plazo) en términos de la correspondiente unidad estándar
de medida (barriles, kilos, gramos, etc.). La posición neta de cada producto básico se
convertirá a pesos utilizando su precio al contado y, si estuviera expresado en moneda
extranjera, convirtiéndolo al tipo de cambio de referencia del dólar estadounidense di-
fundido por el BCRA vigente al cierre de las operaciones del día. De tratarse de mone-
das extranjeras distintas del dólar estadounidense, se convertirán a esta moneda utili-
zando los tipos de pase comunicados por la mesa de operaciones del BCRA.
Los instrumentos derivados –tales como futuros, “forwards”, “swaps” y las opciones tra-
tadas conforme al punto 6.6.3. (luego de aplicar el método delta-plus)– sobre productos
básicos y las posiciones fuera de balance a las que les afecten los cambios en los pre-
cios de los productos básicos deberán convertirse en posiciones nocionales de esos
productos conforme a lo siguiente:
− Los futuros y “forwards” deberán expresarse como cantidades nocionales de barriles,
kilos, etc.
− Los “swaps” en los que un tramo sea un precio fijo y el otro el precio de mercado vi-
gente se tratarán como una posición larga si la entidad financiera paga precio fijo y
recibe variable, y corta en el caso contrario.
− Los “swaps” referidos a diferentes productos básicos no podrán compensarse.
```

**Lectura: CORRECTA.** Sujeto según el texto: la entidad que mide su exposición en productos básicos. Regla de medición del riesgo de mercado: la entidad no puede compensar posiciones entre productos distintos.

**Adjudicación de la autora:** PENDIENTE

### F16 — cap, `cap::8.6.2` (punto 8.6.2), Obligacion

- **Norma:** Registro a valor de mercado — instrumentos de regulación monetaria
- **Descripción:** Los aportes en instrumentos de regulación monetaria del BCRA deberán registrarse a su valor de mercado, entendido como aquel que existe cuando los instrumentos tienen cotización habitual en bolsas y mercados regulados del país o del exterior con transacciones relevantes cuyo monto no distorsione significativamente la cotización
- **Tramo:** los aportes deberán registrarse a su valor de mercado
- **Rol de alcance del documento:** `Sujeto_rol_alcance_capmin` — Entidades alcanzadas (Capitales Mínimos) (miembros: Entidades financieras)
- **Categoría:** aplica_a_mencion_no_verifica; cola humana: no; índice en la población: 874
- **Relaciones aplica_a que emitió el modelo:** mención «las entidades» (no), sugerencia Sujeto_rol_alcance_capmin, resuelta a Sujeto_rol_alcance_capmin (R4_sugerencia_modelo)

**Texto heredado.**

> [S8, encabezado] Sección 8. Responsabilidad patrimonial computable.
> [8.6, encabezado] 8.6. Aportes de capital.
> [8.6, intro] A los fines de todas las reglamentaciones vinculadas al capital, su integración y aumento, in- clusive los referidos a planes de regularización y saneamiento y sin perjuicio de lo previsto en los puntos 5.1. a 5.3. de las normas sobre “Autorización y composición del capital de entidades financieras” en materia de negociación de acciones o de aportes irrevocables para futuros au- mentos de capital, los aportes deben ser efectuados en efectivo. Excepcionalmente, mediando autorización previa de la SEFyC, podrán admitirse aportes en:
> [8.6, cierre] En los casos comprendidos en los puntos 8.6.1. y 8.6.2., los aportes deberán registrarse a su valor de mercado. Se entenderá que los instrumentos cuentan con valor de mercado cuando tengan cotización habitual en las bolsas y mercados regulados del país o del exterior en los que se negocien, con transacciones relevantes en cuyo monto, la eventual liquidación de las tenencias no pueda distorsionar significativamente su cotización. En los casos del punto 8.6.3., los aportes deberán registrarse a su valor de mercado –con el al- cance definido en el párrafo anterior– o, cuando se trate de entidades financieras que realicen oferta pública de sus acciones, al precio que fije la autoridad de contralor competente del co- rrespondiente mercado. No se admitirán los aportes de esta clase de instrumentos cuando no se verifique el cumplimiento de las condiciones mencionadas precedentemente. Cuando se trate de depósitos y otras obligaciones por intermediación financiera de la entidad financiera que no cuenten con autorización para ser negociados en mercados secundarios re- gulados del país o del exterior, los aportes se admitirán a su valor contable –capital, intereses, ajustes, diferencias de cotización por moneda extranjera y, de corresponder, descuentos de emisión–, conforme a las normas del BCRA. En el caso de los instrumentos de deuda compu- tables como CA o PNc, al admitir los aportes, se deberá tener en cuenta lo dispuesto en el
> [8.6, cierre] n1
> [8.6, cierre] punto 8.3.4. En ningún caso la capitalización de deuda podrá implicar una limitación o suspensión al dere- cho de preferencia establecido en el artículo 194 de la Ley General de Sociedades, por lo que no será aplicable lo dispuesto en el artículo 197 de dicha ley. La decisión de capitalización de los conceptos indicados en los puntos 8.6.1. a 8.6.3. por parte de la Asamblea (o autoridad equivalente) será “ad referéndum” de su aprobación por parte de la SEFyC o, en su caso, del BCRA –puntos 5.1. a 5.3. en las normas sobre “Autorización y composición del capital de entidades financieras”–, circunstancia que deberá ser expuesta en nota a los estados contables de los períodos siguientes –trimestral o anual, según correspon- da–, en los términos que establezca la SEFyC. Hasta tanto se le haya notificado la aprobación de los aportes y en la medida en que éstos hayan sido contabilizados, se deducirán del respectivo componente de la RPC de la entidad financiera. Cuando los aportes contabilizados provengan de la capitalización de deuda subor- dinada o de instrumentos representativos de deuda que puedan ser considerados –total o par- cialmente– como parte integrante de la RPC, se mantendrá el tratamiento que corresponda aplicar en la materia de haber permanecido registrados contablemente como pasivos.

**Texto de la unidad.**

```
8.6.2. instrumentos de regulación monetaria del BCRA;
```

**Lectura: CORRECTA.** Sujeto según el texto: la entidad que recibe y registra el aporte de capital. El cierre heredado del punto 8.6 dice que «los aportes deberán registrarse a su valor de mercado»; los registra la entidad cuyo capital se integra. La mención del modelo («las entidades») no está en el texto propio de la unidad, que es solo el ítem.

**Adjudicación de la autora:** PENDIENTE

### F17 — ext, `ext::3.5.3.1` (punto 3.5.3.1), Potestad

- **Norma:** Acceso mercado cambios para pago gastos emisión y servicios
- **Descripción:** La entidad podrá dar acceso al mercado de cambios al cliente para pagar, a la fecha de cierre de la operación de recompra y/o rescate, sin necesidad de liquidación de fondos por el monto equivalente, los gastos de emisión u otros servicios prestados por no residentes en el marco de la emisión de los nuevos títulos de deuda emitidos y/o la operación de recompra y/o rescate.
- **Tramo:** la entidad podrá darle acceso al mercado de cambios al cliente para pagar a la fecha de cierre de la operación de recompra y/o rescate, sin necesidad de que exista una liquidación de fondos por el monto equivalente, los gastos de emisión u otros servicios prestados por no residentes en el marco de la emisión de los nuevos títulos de deuda emitidos y/o la operación de recompra y/o rescate
- **Rol de alcance del documento:** `Sujeto_rol_entidad_autorizada_exterior` — Entidades autorizadas a operar en cambios (Exterior) (miembros: Entidades financieras, Entidades cambiarias)
- **Categoría:** sin_aplica_a; cola humana: no; índice en la población: 945
- **Relaciones aplica_a que emitió el modelo:** ninguna

**Texto heredado.**

> [S3, encabezado] Sección 3. Disposiciones específicas para los egresos por el mercado de cambios
> [S3, chapeau_seccion] Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–, adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables.
> [3.5, encabezado] 3.5. Pagos de títulos de deuda suscriptos en el exterior y endeudamientos financieros con el
> [3.5, intro] exterior. Las entidades podrán dar acceso al mercado de cambios para realizar pagos de capital o intereses de títulos de deuda con registro público en el exterior, otros endeudamientos financieros con el exterior y títulos de deuda con registro público en el país denominados en moneda extranjera íntegramente suscriptos en el exterior, en la medida que se verifiquen las siguientes condiciones:
> [3.5.3, encabezado] 3.5.3. El acceso al mercado de cambios se produce con una anterioridad no mayor a los 3
> [3.5.3, intro] (tres) días hábiles a la fecha de vencimiento del servicio de capital o interés a pagar. En el caso de que se trate de un pago de capital de títulos de deuda emitidos a partir del 08/11/24 que se concreta con una transferencia al exterior, el acceso al mercado de cambios deberá adicionalmente producirse una vez transcurridos, como mínimo, desde la fecha de emisión:
> [3.5.3, intro] i) 12 (doce) meses si el título fue emitido entre el 08/11/24 y el 20/04/25. ii) 6 (seis) meses si el título fue emitido entre 21/04/25 y el 15/05/25. iii) 18 (dieciocho) meses si el título fue emitido a partir del 16/05/25.
> [3.5.3, intro] El acceso al mercado de cambios antes de lo indicado requerirá la conformidad previa del BCRA excepto que el deudor encuadre en alguna de las siguientes situaciones y se cumplan la totalidad de las condiciones estipuladas en cada caso:

**Texto de la unidad.**

```
3.5.3.1. Precancelación de capital e intereses con la liquidación de fondos
ingresados desde el exterior por la emisión de un nuevo título de deuda
comprendido en este punto 3.5.
i) la precancelación de capital sea efectuada en manera simultánea con la
liquidación de los fondos ingresados desde el exterior por la emisión de
un nuevo título de deuda comprendido en este punto 3.5. emitido en el
marco de una operación de refinanciación, recompra y/o rescate
anticipado de deuda.
a) el nuevo título de deuda contempla 1 (un) año de gracia para el
pago de capital y su vida promedio es al menos 2 (dos) años mayor
a la vida promedio remanente de la deuda que se precancela; y
b) el monto acumulado de los vencimientos de capital del nuevo
endeudamiento en ningún momento podrá superar, hasta la fecha
de vencimiento de la deuda que se cancela, el monto que hubieran
acumulado los vencimientos de capital de la deuda que se cancela.
ii) la precancelación de intereses corresponde a los intereses devengados
por la deuda refinanciada hasta la fecha de cierre de la operación de
recompra y/o rescate, sin necesidad de que exista una liquidación de
fondos por el monto equivalente;
Adicionalmente, la entidad podrá darle acceso al mercado de cambios al
cliente para:
iii) pagar en concepto de prima de recompra, de rescate anticipado o
similar hasta el equivalente del 5% (cinco por ciento) del monto del
capital de la deuda recomprada y/o rescatada, en la medida que el pago
se concrete de manera simultánea con una liquidación de fondos
ingresados desde el exterior por el nuevo título de deuda que exceda al
monto de capital que se precancela, como mínimo, por un monto
equivalente al monto de la prima abonada.
iv)pagar a la fecha de cierre de la operación de recompra y/o rescate, sin
necesidad de que exista una liquidación de fondos por el monto
equivalente, los gastos de emisión u otros servicios prestados por no
residentes en el marco de la emisión de los nuevos títulos de deuda
emitidos y/o la operación de recompra y/o rescate.
```

**Lectura: CORRECTA.** Sujeto según el texto: la entidad («la entidad podrá darle acceso»). Potestad explícita de la entidad autorizada a operar en cambios de dar acceso al cliente; el modelo no emitió la relación aunque el texto nombra a «la entidad».

**Adjudicación de la autora:** PENDIENTE

### F18 — ext, `ext::3.17.3.3` (punto 3.17.3.3), Restriccion

- **Norma:** Límite de vencimientos de capital — 365 días
- **Descripción:** El monto de los vencimientos de capital de endeudamientos financieros comprendidos en el punto 3.5., que deban ser atendidos con cobros de exportaciones de bienes conforme a los puntos 7.9. y/o 7.10., que se registren en los siguientes 365 días corridos
- **Tramo:** el monto de los vencimientos de capital que, registrarán en los siguientes 365 (trescientos sesenta y cinco) días corridos, aquellos endeudamientos financieros comprendidos en el punto 3.5. que deban ser atendidos con la aplicación de cobros de exportaciones de bienes en el marco de lo dispuesto en los puntos 7.9. y/o 7.10.
- **Rol de alcance del documento:** `Sujeto_rol_entidad_autorizada_exterior` — Entidades autorizadas a operar en cambios (Exterior) (miembros: Entidades financieras, Entidades cambiarias)
- **Categoría:** sin_aplica_a; cola humana: no; índice en la población: 1013
- **Relaciones aplica_a que emitió el modelo:** ninguna

**Texto heredado.**

> [S3, encabezado] Sección 3. Disposiciones específicas para los egresos por el mercado de cambios
> [S3, chapeau_seccion] Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–, adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables.
> [3.17, encabezado] 3.17. Acceso con “Certificación por los regímenes de acceso a divisas para la producción
> [3.17, intro] incremental de petróleo y/o gas natural (Decreto 277/22)”.
> [3.17.3, encabezado] 3.17.3. La entidad nominada deberá tomar registro de los montos de los beneficios
> [3.17.3, intro] reconocidos por la Secretaría de Energía en el marco del Decreto 277/22 a favor del cliente, dejando constancia del período al que corresponde el beneficio y el monto total del beneficio en dólares estadounidenses obtenido para el período. En el caso de que el cliente sea un beneficiario directo del Decreto 277/22, la entidad podrá emitir “certificaciones de los regímenes de acceso a divisas para la producción incremental de petróleo y/o gas natural (Decreto 277/22)” por hasta el monto que surge de considerar el monto acumulado de los beneficios totales reconocidos al cliente por la Secretaría de Energía neto de los montos acumulados por los conceptos detallados a continuación:

**Texto de la unidad.**

```
3.17.3.3. el monto de los vencimientos de capital que, registrarán en los siguientes
365 (trescientos sesenta y cinco) días corridos, aquellos endeudamientos
financieros comprendidos en el punto 3.5. que deban ser atendidos con la
aplicación de cobros de exportaciones de bienes en el marco de lo
dispuesto en los puntos 7.9. y/o 7.10.
```

**Lectura: CORRECTA.** Sujeto según el texto: la entidad nominada (registra montos y emite la certificación). Ítem del cálculo del monto certificable del Decreto 277/22; el heredado dice que «La entidad nominada deberá tomar registro de los montos». La entidad nominada es una entidad autorizada a operar en cambios, miembro del rol; el rol es más amplio que ella.

**Adjudicación de la autora:** PENDIENTE

### F19 — ext, `ext::4.8.4.2` (punto 4.8.4.2), Restriccion

- **Norma:** Límite 10% monto deudas elegibles sin BOPREAL
- **Descripción:** El monto total de deudas abonadas en el mes calendario bajo este mecanismo no puede superar el 10% del monto de las deudas elegibles por las cuales no se suscribió un título BOPREAL
- **Tramo:** el monto total de deudas abonadas en el mes calendario bajo este mecanismo no supera el 10% (diez por ciento) del monto de las deudas elegibles por las cuales no se suscribió un título BOPREAL
- **Rol de alcance del documento:** `Sujeto_rol_entidad_autorizada_exterior` — Entidades autorizadas a operar en cambios (Exterior) (miembros: Entidades financieras, Entidades cambiarias)
- **Categoría:** sin_aplica_a; cola humana: no; índice en la población: 1044
- **Relaciones aplica_a que emitió el modelo:** ninguna

**Texto heredado.**

> [S4, encabezado] Sección 4. Otras disposiciones específicas.
> [4.8, encabezado] 4.8. Disposiciones complementarias asociadas a los Bonos para la Reconstrucción de una
> [4.8, intro] Argentina Libre (BOPREAL).
> [4.8.4, encabezado] 4.8.4. Los clientes que suscribieron BOPREAL Serie 1 con anterioridad al 31/01/24 por un
> [4.8.4, intro] monto igual o mayor al 50% (cincuenta por ciento) del total pendiente por sus deudas elegibles para los puntos 4.4. y 4.5., podrán acceder al mercado de cambios para pagar capital de deudas elegibles por las cuales no se suscribió un título BOPREAL, cuando se verifique alguna de las siguientes condiciones:
> [4.8.4, cierre] Adicionalmente a los restantes requisitos normativos aplicables, la entidad deberá contar con una declaración jurada del cliente en la que conste el monto suscripto del BOPREAL Serie 1, los montos de las deudas comerciales de bienes y servicios por operaciones anteriores al 13/12/23 elegibles y que el pago queda encuadrado en los límites previstos.

**Texto de la unidad.**

```
4.8.4.2. en forma simultánea concrete la liquidación por un monto equivalente al
pagado de cobros diferidos de exportaciones de bienes que hubiera
correspondido ingresar a partir del 01/03/25 según los plazos normativos
establecidos y el monto total de deudas abonadas en el mes calendario bajo
este mecanismo no supera el 10% (diez por ciento) del monto de las deudas
elegibles por las cuales no se suscribió un título BOPREAL; o
```

**Lectura: DUDOSA.** Sujeto según el texto: el cliente que suscribió BOPREAL (titular de la potestad); la entidad verifica. Condición de acceso del cliente: el heredado dice «Los clientes que suscribieron BOPREAL Serie 1 ... podrán acceder al mercado de cambios ... cuando se verifique alguna de las siguientes condiciones», y el cierre, que «la entidad deberá contar con una declaración jurada del cliente». El límite del 10 % restringe los pagos del cliente; la entidad lo controla.

**Adjudicación de la autora:** PENDIENTE

### F20 — ext, `ext::7.1.1.5` (punto 7.1.1.5), Obligacion

- **Norma:** Plazo 365 días — ingreso y liquidación EXPORTA SIMPLE
- **Descripción:** El ingreso y liquidación de divisas por el mercado de cambios deberá concretarse en el plazo de 365 días corridos a computar desde la fecha del cumplido de embarque otorgado por la Aduana, para las operaciones que se concreten en el marco del régimen EXPORTA SIMPLE, independientemente del tipo de bien exportado.
- **Tramo:** 365 (trescientos sesenta y cinco) días corridos para las operaciones que se concreten en el marco del régimen "EXPORTA SIMPLE"
- **Rol de alcance del documento:** `Sujeto_rol_entidad_autorizada_exterior` — Entidades autorizadas a operar en cambios (Exterior) (miembros: Entidades financieras, Entidades cambiarias)
- **Categoría:** aplica_a_mencion_no_verifica; cola humana: no; índice en la población: 1072
- **Relaciones aplica_a que emitió el modelo:** mención «los exportadores» (no), sugerencia None, resuelta a None (cuarentena)

**Texto heredado.**

> [S7, encabezado] Sección 7. Cobros de exportaciones de bienes.
> [7.1, encabezado] 7.1. Obligación de ingreso y liquidación en los plazos establecidos.
> [7.1.1, encabezado] 7.1.1. Exportaciones oficializadas a partir del 02/09/19.
> [7.1.1, intro] El contravalor en divisas de la exportación hasta alcanzar el valor facturado según la condición de venta pactada deberá ingresarse al país y liquidarse en el mercado de cambios. En el caso que el cliente sea un Vehículo de Proyecto Único (VPU) adherido al Régimen de Incentivo para Grandes Inversiones (RIGI) que declaró ante la Autoridad de Aplicación que preveía hacer uso de los beneficios establecidos en el artículo 198 de la Ley 27.742 en materia de cobro de exportaciones de bienes y servicios resultará aplicable lo dispuesto en los puntos 14.1.1. y 14.1.2., según corresponda. El ingreso y liquidación de las divisas por el mercado de cambios deberá concretarse en los siguientes plazos a computar desde la fecha del cumplido de embarque otorgado por la Aduana:
> [7.1.1, cierre] Independientemente de los plazos máximos precedentes, los cobros de exportaciones deberán ser ingresados y liquidados en el mercado de cambios dentro de los 20 (veinte) días hábiles de la fecha de cobro. La posibilidad de utilizar este plazo quedará supeditada en todos los casos al cumplimiento de los plazos previstos en los puntos 7.1.1.1. a 7.1.1.5. Los montos en moneda extranjera originados en cobros de siniestros por coberturas contratadas, en la medida que los mismos cubran el valor de los bienes exportados, están alcanzados por esta obligación. El exportador deberá seleccionar una entidad para que realice el “Seguimiento de las negociaciones de divisas por exportaciones de bienes”. La obligación de ingreso y liquidación de divisas de un permiso de embarque se considerará cumplida cuando la entidad haya certificado tal situación por los mecanismos establecidos a tal efecto.

**Texto de la unidad.**

```
7.1.1.5. 365 (trescientos sesenta y cinco) días corridos para las operaciones que se
concreten en el marco del régimen “EXPORTA SIMPLE”,
independientemente del tipo de bien exportado.
```

**Lectura: INCORRECTA.** Sujeto según el texto: el exportador (obligación de ingreso y liquidación). Plazo de la obligación de ingreso y liquidación de los cobros de exportaciones (sección 7.1, «Obligación de ingreso y liquidación en los plazos establecidos»): la cumple el exportador. La mención del modelo, «los exportadores», no verifica pero nombra al sujeto correcto; la derivada la reemplazaría por el rol de las entidades.

**Adjudicación de la autora:** PENDIENTE

### F21 — ext, `ext::7.1.3` (punto 7.1.3), Obligacion

- **Norma:** Plazo 20 días hábiles — ingreso y liquidación
- **Descripción:** Ingreso y liquidación de anticipos, prefinanciaciones y posfinanciaciones del exterior en el mercado de cambios dentro del plazo establecido
- **Tramo:** deberán ser ingresadas y liquidadas en el mercado de cambios dentro de los 20 (veinte) días hábiles de la fecha de cobro o desembolso en el exterior
- **Rol de alcance del documento:** `Sujeto_rol_entidad_autorizada_exterior` — Entidades autorizadas a operar en cambios (Exterior) (miembros: Entidades financieras, Entidades cambiarias)
- **Categoría:** sin_aplica_a; cola humana: no; índice en la población: 1074
- **Relaciones aplica_a que emitió el modelo:** ninguna

**Texto heredado.**

> [S7, encabezado] Sección 7. Cobros de exportaciones de bienes.
> [7.1, encabezado] 7.1. Obligación de ingreso y liquidación en los plazos establecidos.

**Texto de la unidad.**

```
7.1.3. Anticipos, prefinanciaciones y posfinanciaciones del exterior.
Los anticipos, prefinanciaciones y posfinanciaciones del exterior deberán ser
ingresadas y liquidadas en el mercado de cambios dentro de los 20 (veinte) días
hábiles de la fecha de cobro o desembolso en el exterior.
En el caso que el cliente sea un Vehículo de Proyecto Único (VPU) adherido al
Régimen de Incentivo para Grandes Inversiones (RIGI) que declaró ante la Autoridad
de Aplicación que preveía hacer uso de los beneficios establecidos en el artículo 198
de la Ley 27.742 en materia de cobro de exportaciones de bienes y servicios, resultará
aplicable lo dispuesto en el punto 14.1.4.
```

**Lectura: INCORRECTA.** Sujeto según el texto: el exportador que recibe el anticipo o la financiación. «Los anticipos, prefinanciaciones y posfinanciaciones del exterior deberán ser ingresadas y liquidadas ... dentro de los 20 días hábiles»: la obligación es del exportador que recibió los fondos, no de la entidad.

**Adjudicación de la autora:** PENDIENTE

### F22 — ext, `ext::7.10.1.1` (punto 7.10.1.1), Potestad

- **Norma:** Habilitación de cobros en divisas por exportaciones
- **Descripción:** Se admite la aplicación de cobros en divisas por exportaciones de bienes para el pago de capital e intereses de deudas por importación de bienes y servicios, en los términos fijados por la autoridad de aplicación
- **Tramo:** Se admitirá la aplicación de cobros en divisas por exportaciones de bienes
- **Rol de alcance del documento:** `Sujeto_rol_entidad_autorizada_exterior` — Entidades autorizadas a operar en cambios (Exterior) (miembros: Entidades financieras, Entidades cambiarias)
- **Categoría:** aplica_a_mencion_no_verifica; cola humana: sí; índice en la población: 1115
- **Relaciones aplica_a que emitió el modelo:** mención «las entidades» (no), sugerencia Sujeto_rol_entidad_autorizada_exterior, resuelta a Sujeto_rol_entidad_autorizada_exterior (R4_sugerencia_modelo)

**Texto heredado.**

> [S7, encabezado] Sección 7. Cobros de exportaciones de bienes.
> [7.10, encabezado] 7.10. Operaciones habilitadas para la aplicación de cobros de exportaciones de bienes en el marco
> [7.10, intro] del régimen de fomento de inversión para las exportaciones (Decreto 234/21).
> [7.10.1, encabezado] 7.10.1. Se admitirá la aplicación de cobros en divisas por exportaciones de bienes que
> [7.10.1, intro] correspondan a proyectos comprendidos en el régimen de fomento de inversión para las exportaciones (Decreto 234/21) y en los términos fijados por la autoridad de aplicación para las siguientes operaciones:

**Texto de la unidad.**

```
7.10.1.1. Pago a partir del vencimiento de capital e intereses de deudas por la
importación de bienes y servicios.
```

**Lectura: DUDOSA.** Sujeto según el texto: impersonal («Se admitirá la aplicación de cobros»); la aplicación la pide el exportador del régimen del Decreto 234/21. Permiso para aplicar cobros de exportaciones al pago de deudas de importación. El texto no dice quién es el titular; la aplicación es del exportador beneficiario y la entidad la procesa. La unidad está en la cola humana. La mención del modelo («las entidades») no está en el texto.

**Adjudicación de la autora:** PENDIENTE

### F23 — ext, `ext::7.11.2::intro` (punto 7.11.2), Potestad

- **Norma:** Admisión aplicación divisas a operaciones
- **Descripción:** Se admite la aplicación de las divisas a las operaciones señaladas cuando se verifiquen la totalidad de las condiciones que siguen.
- **Tramo:** La aplicación de las divisas a las operaciones señaladas será admitida en la medida que se verifiquen la totalidad de las siguientes condiciones
- **Rol de alcance del documento:** `Sujeto_rol_entidad_autorizada_exterior` — Entidades autorizadas a operar en cambios (Exterior) (miembros: Entidades financieras, Entidades cambiarias)
- **Categoría:** sin_aplica_a; cola humana: no; índice en la población: 1144
- **Relaciones aplica_a que emitió el modelo:** ninguna

**Texto heredado.**

> [S7, encabezado] Sección 7. Cobros de exportaciones de bienes.
> [7.11, encabezado] 7.11. Financiaciones asociadas a importaciones de bienes habilitadas para la aplicación de cobros
> [7.11.2, encabezado] 7.11.2. La aplicación de las divisas a las operaciones señaladas será admitida en la medida

**Texto de la unidad.**

```
que se verifiquen la totalidad de las siguientes condiciones:
```

**Lectura: DUDOSA.** Sujeto según el texto: impersonal («será admitida en la medida que se verifiquen»). Encabezado de condiciones para aplicar divisas a financiaciones de importaciones; sin sujeto en el texto. La aplicación es del cliente y la admisión, de la entidad que registra; no se puede decidir solo con el texto.

**Adjudicación de la autora:** PENDIENTE

### F24 — ext, `ext::9.2` (punto 9.2), Potestad

- **Norma:** Modificación de entidad responsable por exportador
- **Descripción:** El exportador puede modificar la entidad responsable del seguimiento posteriormente, siempre que no se hayan registrado aplicaciones de divisas a la cancelación de la operación.
- **Tramo:** pudiendo el exportador modificarla posteriormente en la medida que no se hayan registrado aplicaciones de divisas a la cancelación de ésta
- **Rol de alcance del documento:** `Sujeto_rol_entidad_autorizada_exterior` — Entidades autorizadas a operar en cambios (Exterior) (miembros: Entidades financieras, Entidades cambiarias)
- **Categoría:** sin_aplica_a; cola humana: no; índice en la población: 1178
- **Relaciones aplica_a que emitió el modelo:** ninguna

**Texto heredado.**

> [S9, encabezado] Sección 9. Seguimiento de anticipos y otras financiaciones de exportación de bienes.

**Texto de la unidad.**

```
9.2. Entidad nominada por el exportador.
Por cada operación comprendida el exportador deberá seleccionar una entidad como
responsable de su seguimiento.
Esta entidad será la única responsable de emitir los certificados de aplicación que habilitan
que los cobros de exportaciones puedan ser imputados a los permisos correspondientes.
En el caso de financiaciones otorgadas por entidades financieras locales, el seguimiento
estará a cargo de la entidad que otorgó la financiación hasta su cancelación total.
Para las operaciones comprendidas en los puntos 9.1.6. y 9.1.7. el seguimiento quedará a
cargo de la entidad nominada en cumplimiento a lo establecido en los puntos 7.9. o 7.10.
En el caso de las operaciones comprendidas en el punto 9.1.8. el seguimiento quedará a
cargo de la entidad que, a pedido del exportador y luego de verificar el cumplimiento de los
requisitos previstos en el punto 7.11., realizó el registro de la operación ante el BCRA.
En los restantes casos, el seguimiento quedará inicialmente a cargo de la entidad que dé
curso a la liquidación por el mercado de cambios, pudiendo el exportador modificarla
posteriormente en la medida que no se hayan registrado aplicaciones de divisas a la
cancelación de ésta.
En caso de que el exportador solicite el cambio, la entidad a cargo del seguimiento deberá
notificarle la voluntad del exportador a la nueva entidad. La constancia de aceptación por
parte de esta última liberará a la entidad previa de sus obligaciones hacia adelante.
```

**Lectura: INCORRECTA.** Sujeto según el texto: el exportador («pudiendo el exportador modificarla»). La potestad de cambiar la entidad responsable del seguimiento es explícitamente del exportador.

**Adjudicación de la autora:** PENDIENTE

### F25 — ctacte, `ctacte::1.5.1.7` (punto 1.5.1.7), Obligacion

- **Norma:** Devolución de cheques en blanco tras suspensión de servicio
- **Descripción:** El cuentacorrentista debe devolver a la entidad todos los cheques en blanco que conserve dentro de los 5 días hábiles de la fecha de haber recibido la comunicación de la suspensión del servicio de pago de cheques como medida previa al cierre de la cuenta
- **Tramo:** Devolver a la entidad todos los cheques en blanco que conserve al momento de [...] dentro de los 5 días hábiles de la fecha de haber recibido la comunicación de la suspensión del servicio de pago de cheques
- **Rol de alcance del documento:** `Sujeto_banco` — Bancos (miembros: Bancos)
- **Categoría:** aplica_a_mencion_no_verifica; cola humana: no; índice en la población: 1280
- **Relaciones aplica_a que emitió el modelo:** mención «el cuentacorrentista» (no), sugerencia None, resuelta a None (cuarentena)

**Texto heredado.**

> [S1, encabezado] Sección 1. Funcionamiento.
> [1.5, encabezado] 1.5. Aspectos del funcionamiento a incluir en el contrato de cuenta corriente.
> [1.5, intro] En sus cláusulas se deberá prever, como mínimo:
> [1.5.1, encabezado] 1.5.1. Obligaciones del cuentacorrentista.

**Texto de la unidad.**

```
1.5.1.7. Devolver a la entidad todos los cheques en blanco que conserve al momento de
solicitar el cierre de la cuenta o dentro de los 5 días hábiles de la fecha de haber
recibido la comunicación de la suspensión del servicio de pago de cheques como
medida previa al cierre de la cuenta o del cierre de la cuenta.
```

**Lectura: INCORRECTA.** Sujeto según el texto: el cuentacorrentista (heredado: «1.5.1. Obligaciones del cuentacorrentista»). Obligación del cuentacorrentista de devolver los cheques en blanco. El rol de ctacte (bancos) es quien debe prever la cláusula en el contrato (punto 1.5), no quien devuelve los cheques. La mención del modelo («el cuentacorrentista») no verifica porque está en el encabezado heredado y no en el texto propio, pero nombra al sujeto correcto.

**Adjudicación de la autora:** PENDIENTE

### F26 — ctacte, `ctacte::5.1.6` (punto 5.1.6), Restriccion

- **Norma:** Prohibición de rechazar endoso por deficiencia de especificaciones
- **Descripción:** No puede ser rechazado el endoso por la deficiencia de especificaciones del punto 5.1.4
- **Tramo:** no pudiendo ser rechazado por esa deficiencia
- **Rol de alcance del documento:** `Sujeto_banco` — Bancos (miembros: Bancos)
- **Categoría:** sin_aplica_a; cola humana: no; índice en la población: 1380
- **Relaciones aplica_a que emitió el modelo:** ninguna

**Texto heredado.**

> [S5, encabezado] Sección 5. Endosos, modalidades especiales de emisión y aval.
> [5.1, encabezado] 5.1. Endoso.

**Texto de la unidad.**

```
5.1.6. El endoso que no contenga las especificaciones establecidas en el punto 5.1.4. no per-
judica al título ni a su transmisibilidad, no pudiendo ser rechazado por esa deficiencia.
```

**Lectura: CORRECTA.** Sujeto según el texto: el banco girado (no puede rechazar el cheque). «no pudiendo ser rechazado por esa deficiencia», en pasiva: quien rechaza o paga el cheque es el banco girado, el rol de ctacte.

**Adjudicación de la autora:** PENDIENTE

### F27 — ctacte, `ctacte::8.5.4` (punto 8.5.4), Restriccion

- **Norma:** No inclusión apoderados cuenta corriente
- **Descripción:** No procederá la inclusión en la Central de cheques rechazados, Central de cuentacorrentistas inhabilitados o Central de cheques denunciados respecto de apoderados para el uso de la cuenta corriente
- **Tramo:** No procederá la inclusión respecto de apoderados para el uso de la cuenta corriente
- **Rol de alcance del documento:** `Sujeto_banco` — Bancos (miembros: Bancos)
- **Categoría:** sin_aplica_a; cola humana: no; índice en la población: 1451
- **Relaciones aplica_a que emitió el modelo:** ninguna

**Texto heredado.**

> [S8, encabezado] Sección 8. “Central de cheques rechazados”, “Central de cuentacorrentistas inhabili- tados” y “Central de cheques denunciados como extraviados, sustraídos o adulterados”.
> [8.5, encabezado] 8.5. Pautas para la inclusión.

**Texto de la unidad.**

```
8.5.4. No procederá la inclusión respecto de apoderados para el uso de la cuenta corriente o de
personas simplemente autorizadas para la firma de cheques o de titulares, en las cuen-
tas a la orden recíproca, en la medida en que no hayan suscripto los documentos recha-
zados.
```

**Lectura: DUDOSA.** Sujeto según el texto: impersonal («No procederá la inclusión»); la inclusión en la Central la hace el BCRA con lo que informan los bancos. Pauta de qué personas no se incluyen en las centrales de cheques; el banco informa y el BCRA incluye. Si la pauta se lee como límite de lo que el banco informa, el rol es correcto; si se lee como acto del BCRA, no. El texto de la unidad no lo dice.

**Adjudicación de la autora:** PENDIENTE

### F28 — lingob, `lingob::3.2::intro` (punto 3.2), Obligacion

- **Norma:** Adopción de decisiones gerenciales por más de una persona
- **Descripción:** Las principales decisiones gerenciales, en orden a las buenas prácticas, serán adoptadas por más de una persona
- **Tramo:** Las principales decisiones gerenciales, en orden a las buenas prácticas, serán adoptadas por más de una persona
- **Rol de alcance del documento:** `Sujeto_entidad_financiera` — Entidades financieras (miembros: Entidades financieras)
- **Categoría:** sin_aplica_a; cola humana: no; índice en la población: 1517
- **Relaciones aplica_a que emitió el modelo:** ninguna

**Texto heredado.**

> [S3, encabezado] Sección 3. Alta Gerencia.
> [3.2, encabezado] 3.2. Decisiones gerenciales.

**Texto de la unidad.**

```
Las principales decisiones gerenciales, en orden a las buenas prácticas, serán adoptadas por
más de una persona. Es recomendable que la Alta Gerencia:
```

**Lectura: DUDOSA.** Sujeto según el texto: la Alta Gerencia (sección 3, «Alta Gerencia»; «Es recomendable que la Alta Gerencia»). Las decisiones gerenciales las adopta la Alta Gerencia, órgano de la entidad que el catálogo tiene como id propio (Sujeto_alta_gerencia). El rol de lingob (entidades financieras) es la entidad de la que forma parte; la derivada perdería el sujeto más preciso que el texto nombra.

**Adjudicación de la autora:** PENDIENTE

### F29 — polcre, `polcre::2.1.14` (punto 2.1.14), Restriccion

- **Norma:** Límite cuantitativo — financiamiento Tesoro Nacional
- **Descripción:** El financiamiento de instrumentos de deuda en moneda extranjera del Tesoro Nacional no podrá superar un tercio del total de las aplicaciones realizadas conforme a lo previsto en esta sección
- **Tramo:** por hasta el importe equivalente a un tercio del total de las aplicaciones realizadas conforme a lo previsto en esta sección
- **Rol de alcance del documento:** `Sujeto_entidad_financiera` — Entidades financieras (miembros: Entidades financieras)
- **Categoría:** sin_aplica_a; cola humana: no; índice en la población: 1547
- **Relaciones aplica_a que emitió el modelo:** ninguna

**Texto heredado.**

> [S2, encabezado] Sección 2. Aplicación de la capacidad de préstamo de depósitos en moneda extranjera.
> [2.1, encabezado] 2.1. Destinos.
> [2.1, intro] La capacidad de préstamo de los depósitos en moneda extranjera deberá aplicarse, en la co- rrespondiente moneda de captación, en forma indistinta, a los siguientes destinos:
> [2.1, cierre] La aplicación de la capacidad de préstamo de depósitos en moneda extranjera a los destinos vinculados a operaciones de importación (previstos en los puntos 2.1.6., 2.1.7. y la parte atri- buible a éstos por aplicación de los puntos 2.1.8. y 2.1.9.), no podrá superar el valor que resulte de la siguiente expresión: C max (F / C ; 0,05)
> [2.1, cierre] x
> [2.1, cierre] t base base
> [2.1, cierre] Siendo: C: capacidad de préstamo del mes al que corresponda.
> [2.1, cierre] t
> [2.1, cierre] F : financiación de importaciones comprendidas, correspondientes al trimestre agos- base
> [2.1, cierre] to/octubre de 2008.
> [2.1, cierre] C : capacidad de préstamo que corresponda al trimestre agosto/octubre de 2008.
> [2.1, cierre] base
> [2.1, cierre] Las financiaciones y capacidad de préstamo deberán ser computadas de acuerdo con lo esta- blecido en el punto 2.5.

**Texto de la unidad.**

```
2.1.14. Instrumentos de deuda en moneda extranjera del Tesoro Nacional, por hasta el importe
equivalente a un tercio del total de las aplicaciones realizadas conforme a lo previsto en
esta sección.
```

**Lectura: CORRECTA.** Sujeto según el texto: la entidad que aplica su capacidad de préstamo en moneda extranjera. Destino de la capacidad de préstamo con su tope (un tercio): lo aplica la entidad financiera.

**Adjudicación de la autora:** PENDIENTE

### F30 — polcre, `polcre::5.3` (punto 5.3), Restriccion

- **Norma:** Prohibición tenencia títulos valores exterior
- **Descripción:** Prohibición de registrar tenencias de títulos valores públicos y privados del exterior, incluidos títulos de deuda o participaciones de carteras de activos que contengan títulos valores del exterior, y certificados de depósito argentinos (CEDEAR)
- **Tramo:** No podrán registrarse tenencias de títulos valores públicos y privados del exterior, incluidos los títulos de deuda o participaciones correspondientes a carteras de activos entre los que se cuenten títulos valores del exterior, como tampoco de certificados de depósito argentinos (CEDEAR)
- **Rol de alcance del documento:** `Sujeto_entidad_financiera` — Entidades financieras (miembros: Entidades financieras)
- **Categoría:** sin_aplica_a; cola humana: no; índice en la población: 1555
- **Relaciones aplica_a que emitió el modelo:** ninguna

**Texto heredado.**

> [S5, encabezado] Sección 5. Financiamiento a residentes en el exterior.

**Texto de la unidad.**

```
5.3. Tenencia de títulos valores del exterior.
No podrán registrarse tenencias de títulos valores públicos y privados del exterior, incluidos los
títulos de deuda o participaciones correspondientes a carteras de activos entre los que se cuen-
ten títulos valores del exterior, como tampoco de certificados de depósito argentinos
(CEDEAR), excepto que se trate inversiones en títulos públicos externos emitidos por países
miembros de la OCDE cuya deuda soberana cuente con una calificación internacional no infe-
rior a “AA”.
Además, se admite la tenencia de títulos de deuda o participaciones correspondientes a carte-
ras de activos constituidas en el exterior, siempre que estén integradas exclusivamente por títu-
los valores públicos nacionales y/o privados del país, así como de “depository receipts” que co-
rrespondan a dichos títulos valores.
```

**Lectura: CORRECTA.** Sujeto según el texto: la entidad financiera (sus tenencias). «No podrán registrarse tenencias de títulos valores ... del exterior»: tenencias de la entidad financiera.

**Adjudicación de la autora:** PENDIENTE
