# Lectura corta de 1.16 en la tanda final: fichas de los 30 cortes (mesa, §119)

En el orden sellado (`orden_y_cortes_116_tanda_final.json`). **Tramo 1: cortes 1 a 10. Si ninguno de los 10 tiene un error de corte
confirmado, la lectura para ahí** y el resto se declara con «0 de 10». Si alguno se confirma, se sigue con el tramo 2 (cortes 11 a 30).
Sale solo el documento con un error de corte confirmado.

**El criterio** es el de la lectura de cortes de S1 (`docs/mandatos/USEG_OFICIAL_segmentacion_e0r2.md:284-292`): la unidad es
correcta si (1) empieza donde empieza su punto; (2) termina donde termina; (3) no trae texto de otro punto ni restos de encabezados o
pies de página; (4) no le falta texto propio; y (5) su número es el del punto. Rigen las tres reglas de los casos dudosos y las dos
clases de error, con su subclase. Se lee contra la página renderizada (`paginas/`, `pdftoppm -r 110`), no contra el texto.

**Qué mira el patrón:** cada corte es el último ítem de una lista. El detector marca que después de su texto hay un párrafo que podría
ser el cierre de la lista (del padre) y no del ítem. Si ese párrafo es del padre y la unidad lo trae, es un error de corte (termina
fuera de su punto y trae texto de otro punto). Si es del ítem, la unidad es correcta. El «cierre candidato» es lo que marca el
detector, no un juicio.

## Corte 1 (tramo 1) — `snp_tr_nc::6.1.2`

- documento: snp_tr_nc; páginas de la unidad: 23; imágenes: `paginas/snp_tr_nc_p23.png`
- tipo: punto_terminal; rol: None; caracteres propios: 239
- lista: hijos de `6.1`, 2 ítems; cierre candidato del detector: «Se permitirá el cobro de comisiones por cobertura geográfica entre entidades y a los»
- herencia:
  - encabezado: «Sección 6. Transferencias electrónicas de fondos: variables operativas, precios y tasas de intercambio»
  - encabezado: «6.1. Transferencias en lote»

```text
6.1.2. Precio: los precios no podrán ser definidos como porcentajes de los montos transferidos.
Se permitirá el cobro de comisiones por cobertura geográfica entre entidades y a los
clientes por los valores que se acuerden entre las partes.
```

Contexto, la unidad que sigue en E0: `snp_tr_nc::6.2.1` (páginas 23)

```text
6.2.1. Gratuidad: aplican las condiciones de gratuidad establecidas en el punto 5.1.2.1. El tra-
mo inicial gratuito referido en el punto 5.1.2.1.ii) a) es equivalente a 7.500 UVA para las
operaciones en pesos y a 6.000 dólares estadounidenses o euros para las operaciones
en estas monedas (conforme a lo establecido en el punto 6.4.), siempre de forma acu-
mulada por mes calendario, por moneda y por proveedor de cuenta.
```

## Corte 2 (tramo 1) — `fimipyme::4.1.3.2`

- documento: fimipyme; páginas de la unidad: 10; imágenes: `paginas/fimipyme_p10.png`
- tipo: punto_terminal; rol: None; caracteres propios: 716
- lista: hijos de `4.1.3`, 2 ítems; cierre candidato del detector: «El remanente, de ser necesario, se saldará con fondos de otros orígenes.»
- herencia:
  - encabezado: «Sección 4. Financiaciones elegibles.»
  - encabezado: «4.1. Financiación de proyectos de inversión.»
  - cierre: «No podrán encuadrarse como aplicación elegible las financiaciones que se acuerden con- / forme a otros regímenes especiales de crédito en la medida en que los fondos para dichas / asistencias sean provistos a la entidad con ese fin específico o revistan el carácter de res- / ponsabilidades eventuales.»
  - intro: «4.1.3. Financiaciones otorgadas a clientes MiPyME comprendidos en el punto 3.1.1. y ca- / tegorizadas como micro y pequeñas empresas –según la definición de la Secretaría / de la Pequeña y Mediana Empresa y los Emprendedores–, siempre que:»
  - cierre: «La entidad financiera deberá exigir y disponer de la documentación que acredite el / cumplimiento de estas condiciones de acuerdo con lo previsto en el punto 6.1.»

```text
4.1.3.2. cuando los beneficiarios cuenten con un acopio igual o superior al 5 % de
trigo y/o soja deberán:
i) comprometerse a que el pago de las obligaciones emergentes del crédito
se origine primariamente en la venta del acopio de al menos dicho exce-
dente hasta cubrir la obligación, o
ii) al momento de desembolso del crédito acreditar venta neta a término con
entrega física de ese subyacente con vencimiento similar al del crédito de
al menos dicho excedente hasta cubrir la obligación.
El remanente, de ser necesario, se saldará con fondos de otros orígenes.
De corresponder, la mencionada venta deberá ser acreditada mediante la
Liquidación Primaria de Granos, según Resolución General de la AFIP N°
3419/12.
```

Contexto, la unidad que sigue en E0: `fimipyme::4.1.3::cierre` (páginas 10)

```text
La entidad financiera deberá exigir y disponer de la documentación que acredite el
cumplimiento de estas condiciones de acuerdo con lo previsto en el punto 6.1.
```

## Corte 3 (tramo 1) — `ordcom::1.3.4`

- documento: ordcom; páginas de la unidad: 5; imágenes: `paginas/ordcom_p5.png`
- tipo: punto_terminal; rol: None; caracteres propios: 709
- lista: hijos de `1.3`, 4 ítems; cierre candidato del detector: «Banco Central que en cada caso corresponda, información que esta Institución considera»
- herencia:
  - encabezado: «Sección 1. Lineamientos básicos del ordenamiento.»
  - encabezado: «1.3. Comunicaciones.»
  - intro: «Las Comunicaciones son el medio a través del cual se divulgan las normas. Sus distintos tipos / son:»

```text
1.3.4. Comunicaciones “D”: dan a conocer, exclusivamente a los entes supervisados por el
Banco Central que en cada caso corresponda, información que esta Institución considera
de carácter confidencial. Las rectificaciones de estas comunicaciones se efectuarán con
otra comunicación del mismo tipo.
Cuando estas comunicaciones sean emitidas por la Gerencia Administrativa Judicial, en
los documentos de texto se encontrará inserta una planilla de cálculo con los requeri-
mientos efectuados por los Juzgados y Fiscalías oficiantes, con la finalidad de que las
entidades financieras puedan conocer los mismos, para ser procesados de acuerdo con
la modalidad de cada institución y facilitar la operatoria diaria.
```

Contexto, la unidad que sigue en E0: `ordcom::1.4` (páginas 5)

```text
1.4. Comunicados de prensa.
Se identifican con la letra “P”, y dan a conocer informaciones dirigidas al público en general
(anuncios, comentarios sobre informes periódicos del Banco Central y toda otra información,
que no tenga carácter normativo de observancia obligatoria).
```

## Corte 4 (tramo 1) — `tasint::3.2.4`

- documento: tasint; páginas de la unidad: 9; imágenes: `paginas/tasint_p9.png`
- tipo: punto_terminal; rol: None; caracteres propios: 370
- lista: hijos de `3.2`, 4 ítems; cierre candidato del detector: «Para el cálculo del CFT se tomarán en cuenta la tasa de interés, las comisiones y los»
- herencia:
  - encabezado: «Sección 3. Expresión de las tasas.»
  - encabezado: «3.2. Exposición en los documentos.»
  - intro: «En todas las operaciones, cualquiera sea su instrumentación, corresponde que en los contratos, / recibos, notas de débito u otros documentos de relación con los clientes, donde se expliciten / tasas o importes de intereses, se deje expresa constancia de los siguientes aspectos:»
  - cierre: «Cuando se trate de operaciones con sujetos comprendidos dentro de la definición de usuarios / de servicios financieros, además: / i) El valor numérico del CFT y el signo “%” deberán identificarse de manera legible y destacada»
  - cierre: «según alguno de los siguientes criterios: / a) con al menos el doble del tamaño –en idéntica fuente y conservando todas las propor- / ciones de espesor de trazos, alto y ancho– al que se utilice para la demás información»
  - cierre: «incluida en el documento de que se trate; o»
  - cierre: «b) en una tipografía resaltada y/o en color destacado –en idéntica fuente y tamaño y»
  - cierre: «conservando todas las proporciones de alto y ancho– respecto de la que se utilice para / la demás información incluida en el documento de que se trate.»
  - cierre: «ii) Será de aplicación lo dispuesto por el punto 2.3.3. de las normas sobre “Protección de los»
  - cierre: «usuarios de servicios financieros”.»

```text
3.2.4. Costo financiero total (CFT), a cuyo efecto se considerará lo establecido en el punto 3.4.
Para el cálculo del CFT se tomarán en cuenta la tasa de interés, las comisiones y los
cargos vigentes al momento de la contratación, indicando expresamente si esos concep-
tos podrán modificarse de conformidad con los parámetros y criterios preestablecidos en
el contrato.
```

Contexto, la unidad que sigue en E0: `tasint::3.2::cierre` (páginas 9)

```text
Cuando se trate de operaciones con sujetos comprendidos dentro de la definición de usuarios
de servicios financieros, además:
i) El valor numérico del CFT y el signo “%” deberán identificarse de manera legible y destacada
según alguno de los siguientes criterios:
a) con al menos el doble del tamaño –en idéntica fuente y conservando todas las propor-
ciones de espesor de trazos, alto y ancho– al que se utilice para la demás información
incluida en el documento de que se trate; o
b) en una tipografía resaltada y/o en color destacado –en idéntica fuente y tamaño y
conservando todas las proporciones de alto y ancho– respecto de la que se utilice para
la demás información incluida en el documento de que se trate.
ii) Será de aplicación lo dispuesto por el punto 2.3.3. de las normas sobre “Protección de los
usuarios de servicios financieros”.
```

## Corte 5 (tramo 1) — `fabcra::2.3.2`

- documento: fabcra; páginas de la unidad: 14, 15; imágenes: `paginas/fabcra_p14.png`, `paginas/fabcra_p15.png`
- tipo: punto_terminal; rol: None; caracteres propios: 390
- lista: hijos de `2.3`, 2 ítems; cierre candidato del detector: «La firma y cargo del funcionario que suscribe la nota deberán estar certificados por es-»
- herencia:
  - encabezado: «Sección 2. Libros de firmas autorizadas de las entidades financieras»
  - chapeau_seccion: «Sobre la base del “Libro de firmas autorizadas” de cada entidad financiera la Gerencia de Cuentas / Corrientes certifica las firmas de los funcionarios designados por éstas, ya sea en avales, garantías, / certificaciones de servicios u otro tipo de documentos a requerimiento de particulares, entidades, / empresas y/u otros organismos; siempre que dichas signaturas se encuentren incluidas en el libro / oportunamente presentado por cada entidad. / Con el objeto de evitar inconvenientes por divergencias en los rasgos y/o inexistencias de las firmas / y a efectos de mejorar el servicio de certificación de firmas que brinda el BCRA, las entidades debe- / rán mantener actualizado su correspondiente “Libro de firmas autorizadas”.»
  - encabezado: «2.3. Certificación de la nota de presentación»

```text
2.3.2. Certificación notarial
La firma y cargo del funcionario que suscribe la nota deberán estar certificados por es-
cribano público y contar con la correspondiente foja de actuación notarial cuando co-
rresponda.
Asimismo, el notario deberá dejar constancia del hecho que el firmante (funcionario / au-
toridad certificante) posee facultades suficientes para el acto que está realizando.
```

Contexto, la unidad que sigue en E0: `fabcra::2.4.1` (páginas 15)

```text
2.4.1. El BCRA no provee la información contenida en los libros de firmas, incluso a la misma
entidad, en virtud de la confidencialidad que revisten los nombramientos de los firmantes
autorizados.
```

## Corte 6 (tramo 1) — `inspag::1.3.1.6`

- documento: inspag; páginas de la unidad: 7, 8; imágenes: `paginas/inspag_p7.png`, `paginas/inspag_p8.png`
- tipo: punto_terminal; rol: None; caracteres propios: 803
- lista: hijos de `1.3.1`, 6 ítems; cierre candidato del detector: «Caso A:»
- herencia:
  - encabezado: «Sección 1. Disposiciones generales de los instrumentos de pago.»
  - chapeau_seccion: «Las normas de cumplimiento obligatorio que determinan la línea de código en caracteres magnéti- / cos y características de los instrumentos de pago que emiten las entidades financieras, son las que / seguidamente se detallan:»
  - encabezado: «1.3. Adjudicación y control del dígito verificador en el código de ruta.»
  - encabezado: «1.3.1. Adjudicación del dígito - (Ponderador 9713).»

```text
1.3.1.6. Ejemplos de aplicación:
Caso A:
- Código de Entidad Girada: 011
- Código Tipo de Casa: 038
- Código postal: 1425
El conjunto cuyo dígito verificador se desea determinar es: 011-038-1425.
Productos parciales:
0 x 1 = 0
1 x 3 = 3
1 x 9 = 9
0 x 7 = 0
3 x 1 = 3
8 x 3 = 24
1 x 9 = 9
4 x 7 = 28
2 x 1 = 2
5 x 3 = 15
Suma de productos parciales = 93
Dígito verificador = 10 - 3 = 7
Caso B:
-Código de Entidad Girada: 011
-Código Tipo de Casa: 138
-Código postal: 1425
El conjunto cuyo dígito verificador se desea determinar es: 011-138-1425.
Productos parciales:
0 x 1 = 0
1 x 3 = 3
1 x 9 = 9
1 x 7 = 7
3 x 1 = 3
8 x 3 = 24
1 x 9 = 9
4 x 7 = 28
2 x 1 = 2
5 x 3 = 15
Suma de productos parciales = 100
Dígito verificador = 10 - 0 = 10; por lo tanto, se adjudica por convención el dígito
verificador = 0
```

Contexto, la unidad que sigue en E0: `inspag::1.3.2.1` (páginas 8)

```text
1.3.2.1. Cada dígito de los componentes a verificar (el conjunto deberá incluir el dígito ve-
rificador) se multiplicará por:
- la posición de extrema derecha (dígito verificador) 1
- la posición siguiente consecutiva hacia la izquierda 3
- la posición siguiente consecutiva hacia la izquierda 1
- la posición siguiente consecutiva hacia la izquierda 7
- la posición siguiente consecutiva hacia la izquierda 9
- la posición siguiente consecutiva hacia la izquierda 3
- la posición siguiente consecutiva hacia la izquierda 1
- la posición siguiente consecutiva hacia la izquierda 7
- la posición siguiente consecutiva hacia la izquierda 9
- la posición siguiente consecutiva hacia la izquierda 3
- la posición siguiente consecutiva hacia la izquierda 1
```

## Corte 7 (tramo 1) — `snp_spd::5.3.2.3`

- documento: snp_spd; páginas de la unidad: 15, 16; imágenes: `paginas/snp_spd_p15.png`, `paginas/snp_spd_p16.png`
- tipo: punto_terminal; rol: None; caracteres propios: 1429
- lista: hijos de `5.3.2`, 3 ítems; cierre candidato del detector: «Los administradores deberán extender dicha certificación, como máximo,»
- herencia:
  - encabezado: «Sección 5. Servicio de “billetera digital”»
  - intro: «5.3. Inscripción en el “Registro de billeteras digitales interoperables” / Toda entidad financiera y PSP que desee brindar un servicio de billetera digital que permita / efectuar PCT iniciados mediante la lectura de códigos QR debe estar inscripta en el “Registro / de billeteras digitales interoperables”.»
  - encabezado: «5.3.2. PSP»
  - intro: «Para inscribirse al “Registro de billeteras digitales interoperables” cada PSP debe:»
  - cierre: «Satisfechos esos requisitos, la Superintendencia de Entidades Financieras y Cambiarias / (SEFyC) emitirá un certificado de inscripción y otorgará al solicitante un número en el / “Registro de billeteras digitales interoperables”. La recepción de ese certificado será / condición para poder brindar el servicio de billetera digital.»

```text
5.3.2.3. Presentar –a través del aplicativo referido en en el punto 5.3.1., ingresando con
el CUIT registrado–:
i. Certificación extendida por el representante legal de cada administrador de
esquema de transferencias inmediatas autorizado por BCRA en la que
afirme –en carácter de declaración jurada– que el servicio de que se trata
cumplimentó exitosamente la integración con cada uno de los aceptadores
adheridos a su esquema y que se encuentra en condiciones de ser utilizado
por el público en general para efectuar PCT mediante la lectura de los
códigos QR generados por todos y cada uno de esos aceptadores.
Los administradores deberán extender dicha certificación, como máximo,
dentro de los 5 días hábiles a partir de la finalización de las pruebas que
acrediten la referida integración.
ii. La siguiente información:
a. Nombres y apellidos, cargo, tipo y número de documento de identidad y
dirección de correo electrónico del máximo responsable de las tareas de
tecnología y sistemas de información.
b. Nombres y apellidos, cargo, tipo y número de documento de identidad y
dirección de correo electrónico del máximo responsable de las tareas
vinculadas con la seguridad de la información y protección de activos.
c. Ubicación de los centros/s de procesamiento principal y alternativo
(contingencias)
d. Listado de los proveedores que prestan servicios de tecnología
informática, sistemas y de seguridad de la información.
```

Contexto, la unidad que sigue en E0: `snp_spd::5.3.2::cierre` (páginas 16)

```text
Satisfechos esos requisitos, la Superintendencia de Entidades Financieras y Cambiarias
(SEFyC) emitirá un certificado de inscripción y otorgará al solicitante un número en el
“Registro de billeteras digitales interoperables”. La recepción de ese certificado será
condición para poder brindar el servicio de billetera digital.
```

## Corte 8 (tramo 1) — `adfsp::2.8.2`

- documento: adfsp; páginas de la unidad: 16; imágenes: `paginas/adfsp_p16.png`
- tipo: punto_terminal; rol: None; caracteres propios: 360
- lista: hijos de `2.8`, 2 ítems; cierre candidato del detector: «El importe resultante se debitará en las cuentas corrientes habilitadas a las entidades»
- herencia:
  - encabezado: «Sección 2. Términos y condiciones de los adelantos.»
  - encabezado: «2.8. Tasa de interés.»

```text
2.8.2. El cálculo de los intereses se efectuará sobre los saldos de deuda por mes calendario.
El importe resultante se debitará en las cuentas corrientes habilitadas a las entidades
financieras en el Banco Central, en el plazo previsto en el punto 2.5.2. y se imputará al
primer día hábil de cada mes. El divisor fijo para el cálculo de la tasa es de 365 días.
```

Contexto, la unidad que sigue en E0: `adfsp::2.9` (páginas 16)

```text
2.9. Límite por entidad financiera.
El total de adelantos a otorgar a cada entidad no podrá superar el 100% de su
responsabilidad patrimonial computable del segundo mes anterior al de la subasta,
considerada en términos individuales sin consolidar.
Dicha limitación no será aplicable cuando se trate de bancos públicos cuyas operaciones se
encuentren garantizadas por los Estados Nacional, provinciales, municipales o la Ciudad
Autónoma de Buenos Aires.
```

## Corte 9 (tramo 1) — `raapal::2.2.4.10`

- documento: raapal; páginas de la unidad: 16, 17; imágenes: `paginas/raapal_p16.png`, `paginas/raapal_p17.png`
- tipo: punto_terminal; rol: None; caracteres propios: 1809
- lista: hijos de `2.2.4`, 10 ítems; cierre candidato del detector: «A ese efecto, las entidades financieras podrán computar como parte»
- herencia:
  - encabezado: «Sección 2. Medida de la exposición.»
  - chapeau_seccion: «La medida de la exposición resultará de la sumatoria de: / a) exposiciones en el activo –excluidas las partidas correspondientes a derivados y operaciones de»
  - chapeau_seccion: «financiación con títulos valores (SFT)–;»
  - chapeau_seccion: «b) exposiciones por derivados; / c) exposiciones por operaciones SFT y / d) partidas fuera de balance (PFB). / Los tratamientos específicos para cada uno de estos cuatro tipos de exposiciones se desarrollan en / esta sección.»
  - encabezado: «2.2. Criterios particulares.»
  - encabezado: «2.2.4. Exposiciones fuera de balance.»
  - intro: «Las exposiciones fuera de balance a computar son tanto aquellas consideradas para el / cálculo de la exigencia de capital por riesgo de crédito –incluso las originadas en las titu- / lizaciones– como las que se definen especialmente para la determinación del ratio de / apalancamiento. / Las exposiciones por derivados reciben el tratamiento detallado en el punto 2.2.2., por lo / tanto no se computarán como exposición fuera de balance. / Para determinar la exposición, las partidas fuera de balance se convertirán en exposicio- / nes crediticias multiplicando los montos comprometidos y no utilizados por el correspon- / diente factor de conversión crediticia (CCF), conforme a lo previsto en este punto. A este / efecto, se entiende por compromiso al acuerdo contractual aceptado por el cliente que / obliga a la entidad financiera a otorgar créditos, comprar activos o emitir algún otro tipo / de sustituto crediticio. / Podrá deducirse de la exposición crediticia equivalente –esto es, de la exposición luego / de aplicar el CCF– las previsiones generales y específicas que se deducen del capital de / nivel uno, no pudiendo el monto resultante para esas exposiciones ser menor que cero. / Los factores CCF –expresados en %– serán los siguientes:»
  - cierre: «La promesa de asumir un compromiso que deba ser tratado como una partida fuera de / balance recibirá el menor de los dos CCF aplicables –tal como el caso de un compromiso / de abrir una carta de crédito comercial a corto plazo autoliquidable originada en el movi- / miento de bienes, que recibirá un CCF del 20 %, y no del 40 %, o de un compromiso in- / condicionalmente cancelable de emitir un sustituto crediticio directo que estará sujeto a / un CCF del 10 %, y no del 100 %–.»

```text
2.2.4.10. Exposiciones fuera de balance vinculadas con titulizaciones.
i) Facilidades que no son coberturas de riesgo de crédito.
100
ii) Si fuese establecido de forma contractual que la entidad financiera
que actúa como agente de pago y adelanta fondos para asegurar un
flujo continuo de pagos hacia los inversores –en la medida que pueda
cancelar discrecional y unilateralmente esta facilidad– tiene derecho
al reembolso completo del adelanto otorgado y ese derecho tiene pre-
lación frente a cualquier otro derecho sobre los flujos generados por
las exposiciones subyacentes, podrá aplicar a la parte de los antici-
pos de efectivo o facilidades de liquidez que se estima no será utili-
zada el CCF previsto para los compromisos cancelables incondicio-
nalmente.
A ese efecto, las entidades financieras podrán computar como parte
no utilizada de cada contrato a la menor proporción no utilizada que
resulte del historial de utilización de posiciones de titulización simila-
res durante los últimos 7 años. La entidad financiera deberá demos-
trar que realiza un seguimiento activo de la situación financiera de la
titulización y que sus sistemas de control interno permiten cancelar la
línea ante cualquier muestra de deterioro de la solvencia del progra-
ma. Además, deberá fundamentar los criterios que sustentan su ex-
pectativa de que la parte utilizada de cada una de las facilidades no
excederá de la máxima proporción que resulta de sus registros, con-
siderando para ello todos los factores determinantes y toda la infor-
mación pertinente. La estimación de la máxima proporción utilizada
se deberá revisar con periodicidad anual o con mayor frecuencia,
cuando disponga de nueva información relevante. Todo lo que exce-
da de la proporción que se estima no será utilizada recibirá un CCF
del 100 %.
```

Contexto, la unidad que sigue en E0: `raapal::2.2.4::cierre` (páginas 17)

```text
La promesa de asumir un compromiso que deba ser tratado como una partida fuera de
balance recibirá el menor de los dos CCF aplicables –tal como el caso de un compromiso
de abrir una carta de crédito comercial a corto plazo autoliquidable originada en el movi-
miento de bienes, que recibirá un CCF del 20 %, y no del 40 %, o de un compromiso in-
condicionalmente cancelable de emitir un sustituto crediticio directo que estará sujeto a
un CCF del 10 %, y no del 100 %–.
```

## Corte 10 (tramo 1) — `repefe::2.6.2`

- documento: repefe; páginas de la unidad: 10; imágenes: `paginas/repefe_p10.png`, `paginas/repefe_p11.png`
- tipo: punto_terminal; rol: None; caracteres propios: 460
- lista: hijos de `2.6`, 2 ítems; cierre candidato del detector: «Libro Especial y demás registros de comercio previstos en el punto 5.1., asentando en»
- herencia:
  - encabezado: «Sección 2. Autorización.»
  - encabezado: «2.6. Condiciones básicas a las que quedará sujeta la autorización concedida.»

```text
2.6.2. Para mantener la autorización recibida, el representante deberá llevar en legal forma el
Libro Especial y demás registros de comercio previstos en el punto 5.1., asentando en
orden cronológico la totalidad de las actividades que desarrolla y cumplir el régimen in-
formativo a que se refiere el punto 5.2.
No se admitirá la invocación de la legislación del país de la representada cuando ello
implique una limitación al cumplimiento de estos requisitos.
```

Contexto, la unidad que sigue en E0: `repefe::S3::chapeau_seccion` (páginas 11)

```text
La entidad representada y sus representantes titular y suplente/s -según el caso-, deberán mante-
ner actualizadas la información y documentación proporcionadas en ocasión de gestionar la autori-
zación concedida.
```

## Corte 11 (tramo 2) — `rrci::3.6.2.2`

- documento: rrci; páginas de la unidad: 18; imágenes: `paginas/rrci_p18.png`
- tipo: punto_terminal; rol: None; caracteres propios: 1239
- lista: hijos de `3.6.2`, 2 ítems; cierre candidato del detector: «Tipo de notificación: 03 (se debe informar siempre el código 03).»
- herencia:
  - encabezado: «Sección 3. Notificación de ciberincidentes.»
  - encabezado: «3.6. Formato de la notificación.»
  - encabezado: «3.6.2. Reportes de cierre.»

```text
3.6.2.2. Cuerpo del correo electrónico. ID: XXXXXX (dejar solo un espacio luego de los
dos puntos, indicar el ID original).
Tipo de notificación: 03 (se debe informar siempre el código 03).
Descripción del incidente: (texto libre).
Servicio afectado: (texto libre según lo indicado en punto 3.5.3.).
Categorización: (texto libre según lo indicado en punto 3.5.3.).
Volumen de clientes afectados: (texto libre según lo indicado en punto 3.5.3.).
Cronología: (texto libre según lo indicado en punto 3.5.3.).
Incidente crítico sin plan de continuidad: (texto libre según lo indicado en punto
3.5.3).
Sectores internos involucrados: (texto libre según lo indicado en punto 3.5.3.).
Sectores internos afectados: (texto libre según lo indicado en punto 3.5.3.).
Prestadores de servicios: (texto libre según lo indicado en punto 3.5.3.).
Análisis de causa raíz: (texto libre según lo indicado en punto 3.5.3.).
Medidas de mitigación: (texto libre según lo indicado en punto 3.5.3.).
Notificaciones: (texto libre según lo indicado en punto 3.5.3.).
Planes de acción para evitar la recurrencia: (texto libre según lo indicado en punto
3.5.3).
Fecha y hora de resolución: (dd/mm/yyyy hh:mm) (respetar el formato de fecha,
no incluir los paréntesis).
```

## Corte 12 (tramo 2) — `opecam::3.2.2`

- documento: opecam; páginas de la unidad: 14; imágenes: `paginas/opecam_p14.png`
- tipo: punto_terminal; rol: None; caracteres propios: 286
- lista: hijos de `3.2`, 2 ítems; cierre candidato del detector: «A tal efecto se considerará la cotización “contado 48 horas” del Mercado Abierto Electró-»
- herencia:
  - encabezado: «Sección 3. Capital mínimo de casas y agencias de cambio.»
  - encabezado: «3.2. Aportes de capital.»
  - intro: «A los fines de todas las reglamentaciones vinculadas con el capital, su integración y aumento, / los aportes podrán ser efectuados:»
  - cierre: «Respecto de los citados aportes deberá acreditarse el origen de los fondos mediante la certifi- / cación de contador público independiente, la que deberá incluir en su elaboración una manifes- / tación respecto a que se aplicaron las disposiciones legales, reglamentarias y profesionales vi- / gentes en materia de prevención de lavado de activos y financiamiento al terrorismo.»

```text
3.2.2. En títulos públicos nacionales –que cuenten con cotización normal y habitual por importes
significativos en mercados del país–, para lo cual deberá optarse por una sola especie.
A tal efecto se considerará la cotización “contado 48 horas” del Mercado Abierto Electró-
nico (MAE).
```

Contexto, la unidad que sigue en E0: `opecam::3.2::cierre` (páginas 14)

```text
Respecto de los citados aportes deberá acreditarse el origen de los fondos mediante la certifi-
cación de contador público independiente, la que deberá incluir en su elaboración una manifes-
tación respecto a que se aplicaron las disposiciones legales, reglamentarias y profesionales vi-
gentes en materia de prevención de lavado de activos y financiamiento al terrorismo.
```

## Corte 13 (tramo 2) — `cedin::3.5`

- documento: cedin; páginas de la unidad: 6; imágenes: `paginas/cedin_p6.png`
- tipo: punto_terminal; rol: None; caracteres propios: 716
- lista: hijos de `3`, 5 ítems; cierre candidato del detector: «Deberán remitirse a la Subgerencia General de Medios de Pago a la casilla de correo»
- herencia:
  - encabezado: «3. Distribución.»

```text
3.5. Como responsable de esta operatoria el Directorio o autoridad equivalente de las entida-
des financieras deberán nombrar a un funcionario titular que represente a esta última y,
adicionalmente, a un funcionario por cada casa operativa. En ambos casos se deberán
designar suplentes.
Deberán remitirse a la Subgerencia General de Medios de Pago a la casilla de correo
electrónica habilitada al efecto sólo los datos personales de los funcionarios nombrados
como responsables de la entidad financiera (titular y suplente) y sus números de teléfo-
nos, fax y dirección/es postales y de correo electrónico.
Los datos de los funcionarios designados para cada casa operativa deberán encontrarse
a disposición del BCRA.
```

Contexto, la unidad que sigue en E0: `cedin::S4` (páginas 6)

```text
4. Endoso.
El CEDIN se transmite entre endosante y endosatario mediante endoso no sujeto a condición
alguna colocado al dorso del documento y su entrega, no admitiéndose agregados de ningún
tipo al cuerpo del certificado. Cualquier otra condición no prevista en estas normas se tendrá
por no escrita.
Los datos que deberá contener el endoso en el certificado serán:
- Firma del endosante.
- Aclaración de su identidad (nombre y apellido o razón social).
- Domicilio.
- Datos de identificación tributaria: CUIT, CUIL o CDI según corresponda.
```

## Corte 14 (tramo 2) — `snp_mep::4.3.3`

- documento: snp_mep; páginas de la unidad: 10; imágenes: `paginas/snp_mep_p10.png`
- tipo: punto_terminal; rol: None; caracteres propios: 319
- lista: hijos de `4.3`, 3 ítems; cierre candidato del detector: «Puede estar compuesta por uno o varios campos de acuerdo con su configuración:»
- herencia:
  - encabezado: «Sección 4. Operatorias»
  - encabezado: «4.3. Características»
  - intro: «Cada operatoria está compuesta por:»

```text
4.3.3. Instrucción de pago
Puede estar compuesta por uno o varios campos de acuerdo con su configuración:
− Genérica: un único campo de 254 caracteres.
− Configuradas: varios campos, con los datos pertinentes, separados por “punto y
coma” (;).
Los campos de la instrucción de pago podrán tener validaciones y controles.
```

Contexto, la unidad que sigue en E0: `snp_mep::4.4` (páginas 10)

```text
4.4. Extractos MEP
La Subgerencia de Administración de Medios de Pago enviará vía IDEAR los extractos en
formato MPB una vez efectuado el cierre del sistema.
Las entidades podrán, además, acceder a estos extractos a demanda, mediante las consultas
disponibles en los servicios web. El formato del archivo dependerá del estado del sistema
MEP al momento de efectuar la consulta: será MPA si el MEP está abierto y MPB si está ce-
rrado.
Los datos que incluye el extracto son:
− número de transacción: otorgado por el MEP al momento de la autorización;
− secuencia: depende del origen del registro;
− entidad y cuenta deudora;
− entidad y cuenta acreedora;
− operatoria MEP / operatoria interna del BCRA: aquellas que comienzan con las letras “U”,
“V” o “S” corresponden a códigos de operatorias internas del BCRA;
− fecha;
− instrucción de pago;
− importe;
− moneda;
− estado del MEP: de acuerdo con el momento de emisión del extracto;
− origen del movimiento: MEP.
```

## Corte 15 (tramo 2) — `ri_ai::1.2.2`

- documento: ri_ai; páginas de la unidad: 2; imágenes: `paginas/ri_ai_p2.png`, `paginas/ri_ai_p3.png`
- tipo: punto_terminal; rol: None; caracteres propios: 896
- lista: hijos de `1.2`, 2 ítems; cierre candidato del detector: «Las entidades financieras –excepto las que consoliden con otra/s entidad/es»
- herencia:
  - encabezado: «Sección 1. Entidades Comprendidas»
  - encabezado: «1.2. Sujetas al régimen de información sobre bases consolidadas:»

```text
1.2.2 Entidades financieras, filiales y subsidiarias significativas en el país y en el ex-
terior.
Las entidades financieras –excepto las que consoliden con otra/s entidad/es
financiera/s- no presentarán la información consolidada mensual, debiendo
consignar en su lugar, de acuerdo con las instrucciones operativas instrumen-
tadas a través de la respectiva Circular RUNOR, los siguientes datos:
- importe de activos inmovilizados y otros conceptos, (Código 100- Código
200+ Código 300)
- el 100% de la responsabilidad patrimonial computable de la entidad finan-
ciera del mes que corresponda.
- Detalle de las eventuales franquicias otorgadas (Códigos 401/402/403)
De registrar exceso, el importe deberá informarse teniendo en cuenta el tratamiento
establecido a través del texto ordenado de las normas sobre “Incumplimientos de capi-
tales mínimos y relaciones técnicas. Criterios aplicables”.
```

Contexto, la unidad que sigue en E0: `ri_ai::2.1` (páginas 3)

```text
2.1. La información tendrá frecuencia mensual y se integrará con datos referidos al mes
bajo análisis.
```

## Corte 16 (tramo 2) — `ri_dsf::8.2`

- documento: ri_dsf; páginas de la unidad: 14; imágenes: `paginas/ri_dsf_p14.png`
- tipo: punto_terminal; rol: None; caracteres propios: 267
- lista: hijos de `8`, 2 ítems; cierre candidato del detector: «A los fines de establecer los días de atraso para los deudores con más de una asis-»
- herencia:
  - encabezado: «8. Micro, pequeña y mediana empresa.»
  - chapeau_seccion: «[recorte de E0: no se transcriben 11810 caracteres de este bloque heredado]»
  - chapeau_seccion: «5. Refinanciaciones»
  - chapeau_seccion: «Se deberá informar, en caso de corresponder, la fecha de la última refinanciación concertada / por tipo de asistencia. / En el caso de deudores calificados como “en negociación o con acuerdos de refinanciación”, / la fecha que se deberá informar será la correspondiente a la manifestación fehaciente de la / intención de refinanciar. / Esta fecha se deberá informar hasta el momento en que al deudor se lo reclasifique en si- / tuación normal.»
  - chapeau_seccion: «6. Previsiones valuadas según NIIF. Previsiones por riesgo de incobrabilidad y provisiones»
  - chapeau_seccion: «constituidas individualmente respecto de la deuda de cada cliente. / 6.1. Por la asistencia crediticia registrada en Préstamos, Otros créditos por intermediación»
  - chapeau_seccion: «financiera, Créditos por arrendamientos financieros, Créditos diversos y por los con- / ceptos incluidos de Títulos privados (códigos 121135, 125135, 126135, 131601, / 131901, 132301, 135601, 135901, 136301, 141301, 142301, 145301, 146301, 151312, / 155312, 171302, 175302, 176302).»
  - chapeau_seccion: «6.2. Por Responsabilidades eventuales y Garantías otorgadas. (código 340018). / 6.3. En caso de que la entidad haya optado de acuerdo con lo dispuesto en el punto 2.2.3.»
  - chapeau_seccion: «de las normas sobre “Previsiones mínimas por riesgo de incobrabilidad, se informará el / incremento de previsión correspondiente. / 3. Deudores del Sistema Financiero.»
  - chapeau_seccion: «7. Máxima asistencia.»
  - chapeau_seccion: «En los casos de clientes vinculados o de aquellos cuyo saldo de deuda en algún momento / del mes supere el 0,5% de la Responsabilidad Patrimonial Computable de la entidad co- / rrespondiente al mes anterior o el equivalente al 40% de dos veces el importe de referencia / establecido en el punto 3.7 de las normas sobre “Clasificación de deudores”, de ambos el / mayor, no obstante informar su saldo a fin de mes, se suministrará el importe correspon- / diente a la máxima asistencia del período. / Dicha máxima asistencia deberá informarse aún en aquellos casos en que el saldo de deu- / da a fin de mes sea cero.»
  - chapeau_seccion: «8. Deudores de la cartera para consumo o vivienda en situación distinta a la normal:»

```text
8.2. Para cada uno de los deudores informados en el punto 8.1. se indicarán los días de
atraso en el pago de sus obligaciones.
A los fines de establecer los días de atraso para los deudores con más de una asis-
tencia otorgada, se tendrá en cuenta la de mayor atraso.
```

Contexto, la unidad que sigue en E0: `ri_dsf::S9` (páginas 14)

```text
9. Financiaciones para micro, pequeña o mediana empresa.
Se deberá informar el monto correspondiente a líneas de préstamos otorgados en condicio-
nes preferenciales (Sepyme y programas de otros organismos).
```

## Corte 17 (tramo 2) — `snp_atm::2.3.3`

- documento: snp_atm; páginas de la unidad: 4, 5; imágenes: `paginas/snp_atm_p4.png`, `paginas/snp_atm_p5.png`, `paginas/snp_atm_p6.png`
- tipo: punto_terminal; rol: None; caracteres propios: 287
- lista: hijos de `2.3`, 3 ítems; cierre candidato del detector: «Fecha de implementación Porcentaje de cajeros»
- herencia:
  - encabezado: «Sección 2. Acceso a cajeros automáticos con lectores de huellas digitales»
  - encabezado: «2.3. Plan de implementación»
  - intro: «A fin de cumplimentar lo dispuesto en los puntos 2.1. y 2.2., se establece el siguiente crono- / grama.»

```text
2.3.3. Cobertura geográfica. Los lectores biométricos referidos en el punto 2.1. deberán estar
disponibles en el 100 % de los cajeros, de acuerdo con el siguiente cronograma:
Fecha de implementación Porcentaje de cajeros
con lectores biométricos
31.12.21 35 %
30.6.22 60 %
31.12.22 100 %
```

Contexto, la unidad que sigue en E0: `snp_atm::S3` (páginas 6)

```text
Sección 3. Accesos a cajeros automáticos para casos especiales
Los cajeros automáticos destinados a los usuarios de servicios financieros con dificultades visuales
deberán contar con software reproductor de texto-a-voz, auriculares con su respectivo conector
estándar, teclado con sistema Braille o estándar con relieve resaltado y mecanismo audible y per-
ceptible destinado a alertar el olvido de la tarjeta y/o del dinero dispensado por el equipo. No se
podrán cobrar comisiones y/o cargos diferenciales a estos usuarios por esta prestación.
Las entidades deberán alcanzar la cobertura del servicio con esos cajeros automáticos en al menos
el 10 % del total de los equipos instalados, comenzando con aquellos emplazados en las localida-
des de mayor población, sin perjuicio de las mayores obligaciones a favor de tales personas que
pueda imponer la normativa local.
```

## Corte 18 (tramo 2) — `traval::3.3.2.5`

- documento: traval; páginas de la unidad: 10; imágenes: `paginas/traval_p10.png`
- tipo: punto_terminal; rol: None; caracteres propios: 509
- lista: hijos de `3.3.2`, 5 ítems; cierre candidato del detector: «Incorporar, en el vehículo que se utilice, cartelería disuasoria que dé a conocer»
- herencia:
  - encabezado: «Sección 3. Condiciones para funcionar.»
  - encabezado: «3.3. Seguridad física.»
  - intro: «Las TV deberán contar con un proceso integral para la gestión del riesgo de comisión de delitos / –que involucre su identificación, evaluación, seguimiento, control y mitigación– para salvaguar- / dar la integridad de las personas, como así también de los valores transportados, considerando / –entre otros aspectos– los montos a transportar, las distancias a recorrer y las zonas geográfi- / cas en las que se operará. Su implementación no requiere autorización del BCRA. / Ese proceso deberá ser suficientemente comprobado, debidamente documentado y revisado / periódicamente en función de los cambios que se produzcan en el perfil de este riesgo, y estar / en condiciones de ser presentado a requerimiento del BCRA, con un estado actualizado de su / efectivo cumplimiento. / Todas las operaciones vinculadas al transporte de valores deberán revestir carácter confiden- / cial.»
  - cierre: «Los organismos de seguridad jurisdiccionales y/o la Gerencia de Fiscalización Normativa del / BCRA podrán realizar las inspecciones relacionadas con aspectos de su competencia y al / cumplimiento de esta normativa, respectivamente, en los vehículos de transporte o bien en los / lugares de atesoramiento y/o custodia. / Los vehículos de transporte deberán ser inspeccionados únicamente en sede del organismo de / seguridad o en la dependencia de las TV. / El traslado de monedas de curso legal queda exceptuado de estas disposiciones.»
  - encabezado: «3.3.2. Recomendaciones.»

```text
3.3.2.5. Adoptar un sistema inteligente de entintado de billetes, que se empleará desde
la recepción de los valores transportados hasta su entrega en el destino final,
que deberá cumplimentar lo establecido en el punto 3.2.6. y en la Sección 4. de
las normas sobre “Circulación monetaria” (texto según la Comunicación “A”
6230).
Incorporar, en el vehículo que se utilice, cartelería disuasoria que dé a conocer
que cuenta con el citado sistema, con la finalidad de desalentar la comisión de
hechos delictivos.
```

Contexto, la unidad que sigue en E0: `traval::3.3::cierre` (páginas 10)

```text
Los organismos de seguridad jurisdiccionales y/o la Gerencia de Fiscalización Normativa del
BCRA podrán realizar las inspecciones relacionadas con aspectos de su competencia y al
cumplimiento de esta normativa, respectivamente, en los vehículos de transporte o bien en los
lugares de atesoramiento y/o custodia.
Los vehículos de transporte deberán ser inspeccionados únicamente en sede del organismo de
seguridad o en la dependencia de las TV.
El traslado de monedas de curso legal queda exceptuado de estas disposiciones.
```

## Corte 19 (tramo 2) — `relact::5.3.2`

- documento: relact; páginas de la unidad: 10; imágenes: `paginas/relact_p10.png`
- tipo: punto_terminal; rol: None; caracteres propios: 218
- lista: hijos de `5.3`, 2 ítems; cierre candidato del detector: «Son de aplicación las disposiciones establecidas en el punto 2.3. de las normas sobre»
- herencia:
  - encabezado: «Sección 5. Incumplimientos.»
  - encabezado: «5.3. Otras consecuencias.»

```text
5.3.2. Limitaciones al crecimiento de depósitos.
Son de aplicación las disposiciones establecidas en el punto 2.3. de las normas sobre
“Incumplimientos de capitales mínimos y relaciones técnicas. Criterios aplicables”.
```

Contexto, la unidad que sigue en E0: `relact::5.4` (páginas 10)

```text
5.4. Exposición contable.
Los incumplimientos deberán ser informados en notas a los estados financieros según los
criterios establecidos por la SEFyC.
```

## Corte 20 (tramo 2) — `apnf::1.3.2.5`

- documento: apnf; páginas de la unidad: 5; imágenes: `paginas/apnf_p5.png`
- tipo: punto_terminal; rol: None; caracteres propios: 43
- lista: hijos de `1.3.2`, 5 ítems; cierre candidato del detector: «FÓRMULA I»
- herencia:
  - encabezado: «Sección 1. Condiciones generales.»
  - encabezado: «1.3. Inscripción en el Banco Central de la República Argentina (BCRA).»
  - intro: «La Superintendencia de Entidades Financieras y Cambiarias (SEFyC) habilitará dos registros / según el tipo de proveedor. La inscripción no implica autorización para realizar operaciones de / intermediación financiera, captación de recursos del público, realización de publicidad o uso de / denominaciones reservadas a entidades autorizadas para ello, o que ofrezcan dudas acerca / de su naturaleza, individualidad u objeto.»
  - encabezado: «1.3.2. Trámite.»
  - intro: «La inscripción deberá efectuarse en forma electrónica a través del correspondiente apli- / cativo incluido en la página del BCRA www.bcra.gob.ar, adjuntando –en archivo con / formato “.pdf”– la documentación prevista en los puntos 1.3.2.1. y 1.3.2.2. e integrar la / información requerida en los puntos 1.3.2.3. a 1.3.2.5., según se detalla a continuación:»

```text
1.3.2.5. Las siguientes fórmulas:
FÓRMULA I
```

Contexto, la unidad que sigue en E0: `apnf::Sbloque1` (páginas 5)

```text
DATOS DEL PROVEEDOR NO FINANCIERO DE CRÉDITO
TIPO DE PROVEEDOR (*):
DENOMINACIÓN DE LA PERSONA JURÍDICA:
CLAVE UNICA DE IDENTIFICACIÓN TRIBUTARIA (CUIT):
```

## Corte 21 (tramo 2) — `graloc::6.3.3.3`

- documento: graloc; páginas de la unidad: 23; imágenes: `paginas/graloc_p23.png`
- tipo: punto_terminal; rol: None; caracteres propios: 439
- lista: hijos de `6.3.3`, 3 ítems; cierre candidato del detector: «Las entidades financieras que realizan operaciones de alta frecuencia (“high-»
- herencia:
  - encabezado: «Sección 6. Riesgo operacional.»
  - encabezado: «6.3. Gestión del riesgo operacional.»
  - intro: «Los sistemas de las entidades financieras deben permitir ejercer controles apropiados de la / gestión de los riesgos y tener capacidad suficiente, escalabilidad y resiliencia para administrar / grandes volúmenes de operaciones de cambio de moneda extranjera, en condiciones norma- / les y de estrés.»
  - encabezado: «6.3.3. Gestión de la capacidad de los sistemas.»
  - intro: «Las entidades financieras deben contar con un plan de gestión de la capacidad de sus / sistemas de operaciones de cambio que incluya la negociación, el seguimiento de los / créditos, las operaciones, los servicios de corretaje brindados a grandes inversores insti- / tucionales (“prime brokerage services”) y los sistemas de liquidación. Además, ese plan / debe contemplar:»
  - cierre: «Las entidades financieras deben asegurarse de que sus sistemas para las operaciones / cambiarias están apropiadamente diseñados para la escala de sus operaciones cambia- / rias actuales y esperadas y que tienen suficiente capacidad, flexibilidad para adaptarse / a los cambios en las necesidades operacionales y escalabilidad para gestionar volúme- / nes crecientes y grandes picos de negociación en situaciones de estrés.»

```text
6.3.3.3. El monitoreo oportuno de los volúmenes de negociación y de la utilización de la
capacidad de los sistemas clave a fin de evitar que lleguen a niveles críticos.
Las entidades financieras que realizan operaciones de alta frecuencia (“high-
frequency trading”, HFT), propias o para sus clientes, deben monitorear los vo-
lúmenes operados en tiempo real y evaluar la posibilidad de que se produzcan
grandes picos en las negociaciones.
```

Contexto, la unidad que sigue en E0: `graloc::6.3.3::cierre` (páginas 23)

```text
Las entidades financieras deben asegurarse de que sus sistemas para las operaciones
cambiarias están apropiadamente diseñados para la escala de sus operaciones cambia-
rias actuales y esperadas y que tienen suficiente capacidad, flexibilidad para adaptarse
a los cambios en las necesidades operacionales y escalabilidad para gestionar volúme-
nes crecientes y grandes picos de negociación en situaciones de estrés.
```

## Corte 22 (tramo 2) — `ctavis::2.3.4.3`

- documento: ctavis; páginas de la unidad: 16, 17; imágenes: `paginas/ctavis_p16.png`, `paginas/ctavis_p17.png`
- tipo: punto_terminal; rol: None; caracteres propios: 737
- lista: hijos de `2.3.4`, 3 ítems; cierre candidato del detector: «Se utilizará la siguiente fórmula:»
- herencia:
  - encabezado: «Sección 2. Movimiento de las cuentas.»
  - encabezado: «2.3. Intereses.»
  - encabezado: «2.3.4. Se deberá especificar:»

```text
2.3.4.3. Cálculo de la tasa de interés efectiva anual.
Se utilizará la siguiente fórmula:
i= { [ (1 + i m/df 100)df/m ] - 1} 100
s x x x
donde:
i: tasa de interés anual efectiva, equivalente al cálculo de los intereses en forma
vencida sobre saldos, en tanto por ciento, con dos decimales.
i : tasa de interés anual contractualmente aplicada, en tanto por ciento.
s
m: cantidad de días correspondiente a cada uno de los subperíodos de liquida-
ción de intereses cuando se los abone en forma periódica o de la operación
cuando se los cobre en una sola oportunidad. Cuando dichos subperíodos
sean en días fijos por lapsos mensuales, bimestrales, etc., se consideran a
estos efectos como de 30 días, 60 días, etc., respectivamente.
df: 365.
```

Contexto, la unidad que sigue en E0: `ctavis::2.3.5` (páginas 17)

```text
2.3.5. Publicidad.
En las publicidades o publicaciones realizadas a través de cualquier medio gráfico (pe-
riódicos, revistas, carteleras en la vía pública, etc.), de las distintas alternativas de in-
versión ofrecidas, las entidades deberán exponer en forma legible y destacada la si-
guiente información:
i) Tasa de interés nominal anual.
ii) Tasa de interés efectiva anual.
```

## Corte 23 (tramo 2) — `jafip::5.7.2`

- documento: jafip; páginas de la unidad: 16, 17; imágenes: `paginas/jafip_p16.png`, `paginas/jafip_p17.png`
- tipo: punto_terminal; rol: None; caracteres propios: 484
- lista: hijos de `5.7`, 2 ítems; cierre candidato del detector: «Utilizando dicho mecanismo de intercambio de archivos, las entidades descargarán»
- herencia:
  - encabezado: «Sección 5. Gestión de Oficios por COELSA.»
  - encabezado: «5.7. Servicio en línea de las entidades financieras.»
  - intro: «Todas las entidades financieras alcanzadas por la presente norma deberán crear un servi- / cio del tipo REST API para ser invocado desde la CEC-BV.»

```text
5.7.2. La transmisión de archivos desde y hacia la CEC-BV será realizada mediante el pro-
tocolo de transferencia de archivos que la CEC-BV determine para tal fin.
Utilizando dicho mecanismo de intercambio de archivos, las entidades descargarán
los archivos correspondientes y enviarán los archivos de respuesta. Esta operatoria
será de exclusiva responsabilidad de las entidades financieras, y deberá reflejar
inexorablemente la información de la cuenta respectiva a las 07:00 horas.
```

Contexto, la unidad que sigue en E0: `jafip::5.8.1` (páginas 17)

```text
5.8.1. EMBARGO DE FONDOS: Cada entidad recibirá la información de la cuenta consulta-
da, y los datos correspondientes al oficio de embargo para su traba hasta el monto del
mismo. La entidad oficiada deberá devolver el saldo embargado en línea a partir de
los datos del oficio y de la información almacenada para la cuenta.
```

## Corte 24 (tramo 2) — `snp_debin::3.5.1.4`

- documento: snp_debin; páginas de la unidad: 13; imágenes: `paginas/snp_debin_p13.png`
- tipo: punto_terminal; rol: None; caracteres propios: 1159
- lista: hijos de `3.5.1`, 4 ítems; cierre candidato del detector: «Cada una de las entidades financieras y PSPCP, mediante sus canales habilita-»
- herencia:
  - encabezado: «Sección 3. Procesos y funciones»
  - encabezado: «3.5. Módulo de administración»
  - intro: «El módulo de administración, cuyo desarrollo y gestión se encontrará a cargo del administrador, / tendrá la función de procesar los débitos y créditos. / El módulo deberá ejecutar las siguientes acciones:»
  - encabezado: «3.5.1. Funcionalidad del módulo de administración»
  - intro: «El producto constará de los siguientes módulos: DEBIN, garantías, adhesiones, y enti- / dades financieras y PSPCP.»

```text
3.5.1.4. Entidades financieras y PSPCP
Cada una de las entidades financieras y PSPCP, mediante sus canales habilita-
dos, deberá contar con un servicio que le permita recibir notificaciones desde el
administrador mediante invocaciones realizadas a dichos servicios.
Deberá permitir realizar las siguientes operaciones:
− Aviso de un nuevo DEBIN: el administrador dará aviso a la entidad o PSPCP
que recibe el DEBIN, que deberá responder dicho aviso para que el adminis-
trador confirme la recepción.
− Aviso de finalización de un DEBIN: este aviso indicará que un DEBIN ha fi-
nalizado de forma correcta, ejecutándose las operaciones correspondientes
de débito y crédito.
− Crédito: el administrador solicitará a la entidad o PSPCP originante que
realice el crédito en la cuenta del cliente ordenante informada previamente.
Este mensaje deberá ser respondido de forma sincrónica, indicando si el
crédito pudo ser realizado o no.
− Débito: el administrador solicitará a la entidad o PSPCP que recibió el DE-
BIN que debite la cuenta del cliente receptor. Este mensaje deberá ser res-
pondido de forma sincrónica, indicando si el débito pudo ser realizado o no.
```

Contexto, la unidad que sigue en E0: `snp_debin::3.5.2` (páginas 13, 14)

```text
3.5.2. Esquema de cobertura
La operatoria contará con un esquema de cobertura específico a fin de asegurar la viabi-
lidad de los débitos y créditos.
El módulo de administración verificará y administrará la cobertura mediante la compen-
sación en línea de los débitos y créditos, con respaldo de las garantías constituidas por
cada entidad para la operatoria, de acuerdo con el punto 9.2.4. del texto ordenado (TO)
sobre Sistema Nacional de Pagos - Cámaras Electrónicas de Compensación. Asimismo,
liquidará los saldos netos de compensación en el sistema LBTR “Medio Electrónico de
Pagos” (MEP).
El administrador establecerá un horario operativo de corte y las órdenes de DEBIN reali-
zadas con posterioridad a dicho horario serán consideradas en la compensación del día
hábil siguiente.
```

## Corte 25 (tramo 2) — `finsec::7.3.2`

- documento: finsec; páginas de la unidad: 32; imágenes: `paginas/finsec_p32.png`, `paginas/finsec_p33.png`
- tipo: punto_terminal; rol: None; caracteres propios: 433
- lista: hijos de `7.3`, 2 ítems; cierre candidato del detector: «No podrán distribuirse dividendos y otras retribuciones en efectivo al capital, remesarse»
- herencia:
  - encabezado: «Sección 7. Incumplimientos.»
  - chapeau_seccion: «Los incumplimientos a lo previsto en estas disposiciones estarán sujetos al tratamiento establecido / en la Sección 2. de las normas sobre “Incumplimientos de capitales mínimos y relaciones técnicas. / Criterios aplicables”.»
  - encabezado: «7.3. Planes de regularización y saneamiento.»

```text
7.3.2. Limitaciones.
No podrán distribuirse dividendos y otras retribuciones en efectivo al capital, remesarse
utilidades ni efectuarse pagos de honorarios, participaciones o gratificaciones provenien-
tes de la distribución de resultados de la entidad, en tanto el plan de regularización y sa-
neamiento esté pendiente de presentación o, habiéndose presentado, no haya sido apro-
bado por la SEFyC o se incurra en su incumplimiento.
```

Contexto, la unidad que sigue en E0: `finsec::8.1` (páginas 33)

```text
8.1. Base individual.
Las asistencias otorgadas por las entidades financieras –comprendidas sus casas en el país y
en el exterior– observarán lo dispuesto en estas normas en forma individual.
```

## Corte 26 (tramo 2) — `retype::1.1.2`

- documento: retype; páginas de la unidad: 3; imágenes: `paginas/retype_p3.png`
- tipo: punto_terminal; rol: None; caracteres propios: 240
- lista: hijos de `1.1`, 2 ítems; cierre candidato del detector: «Las entidades bancarias participantes efectuarán el pago de los beneficios que el Instituto»
- herencia:
  - encabezado: «Sección 1. Disposiciones generales.»
  - encabezado: «1.1. Entidades intervinientes.»

```text
1.1.2. Otros bancos públicos.
Las entidades bancarias participantes efectuarán el pago de los beneficios que el Instituto
de Ayuda Financiera para Pago de Retiros y Pensiones Militares (IAF) les indique, por in-
termedio de todas sus casas.
```

Contexto, la unidad que sigue en E0: `retype::1.2.1` (páginas 3)

```text
1.2.1. Fechas de iniciación.
El IAF comunicará en cada oportunidad la fecha de iniciación de los respectivos períodos
de pago de retiros y pensiones.
```

## Corte 27 (tramo 2) — `gracre::3.1.2.2`

- documento: gracre; páginas de la unidad: 8, 9; imágenes: `paginas/gracre_p8.png`, `paginas/gracre_p9.png`, `paginas/gracre_p10.png`
- tipo: punto_terminal; rol: None; caracteres propios: 2171
- lista: hijos de `3.1.2`, 2 ítems; cierre candidato del detector: «El otorgamiento de asistencia dentro de este margen complementario, cualquiera»
- herencia:
  - encabezado: «Sección 3. Límites máximos.»
  - encabezado: «3.1. Generales.»
  - intro: «No podrán superar los porcentajes de la responsabilidad patrimonial computable de cada / cliente que se indican seguidamente:»
  - encabezado: «3.1.2. Margen complementario.»

```text
3.1.2.2. Aprobación.
El otorgamiento de asistencia dentro de este margen complementario, cualquiera
sea su importe, requerirá la previa aprobación del Directorio o Consejo de
Administración –por mayoría simple de la totalidad de sus miembros– o
autoridad equivalente de la entidad prestamista.
En este último caso, de tener que ausentarse del país la máxima autoridad local,
podrá delegarse en un funcionario del más alto nivel la tarea material de la
aprobación de la asistencia, sin que ello implique deslindar la responsabilidad de
la autoridad ausente por las asignaciones crediticias efectuadas conforme a este
procedimiento.
En los casos en que, por razones operativas, se asignen márgenes de crédito
cuya vigencia no sea superior a un año, a través de acuerdos que se comuni-
quen o no a los clientes, con desembolsos parciales referidos al respectivo
acuerdo marco en función de las necesidades de los deudores, su aprobación
por parte de las autoridades mencionadas cumple el requisito fijado preceden-
temente, en la medida en que se cuente con la opinión de los funcionarios cuya
intervención se requiere para el otorgamiento de financiaciones que superen el
2,5 % de la responsabilidad patrimonial computable de la entidad prestamista, en
ambos casos en forma previa.
Sin perjuicio de ello, el acuerdo deberá estar sujeto a revisión periódica -con la
conformidad de las autoridades mencionadas- siempre que el prestatario deba
ser reclasificado en categoría de menor calidad de acuerdo con las normas per-
tinentes.
Los funcionarios antes indicados deberán intervenir previamente a cada desem-
bolso a fin de verificar el cumplimiento de las condiciones que habilitan este tra-
tamiento especial.
En los casos de sobregiros en cuenta corriente u operaciones puntuales de trá-
mite rápido, se admite que la aprobación del Directorio, Consejo de Administra-
ción o funcionario local de mayor jerarquía se efectúe dentro de los 30 días si-
guientes al de concesión del crédito.
Este requisito no resulta aplicable a la concesión de financiaciones excluidas.
Las decisiones de las autoridades mencionadas deberán constar en los corres-
pondientes libros de actas.
```

Contexto, la unidad que sigue en E0: `gracre::3.2.1` (páginas 10)

```text
3.2.1. Límite máximo.
12,5 % del capital social, sin superar el 12,5 % de los votos o, en los casos en que los
porcentajes sean inferiores, cuando la participación otorgue los votos necesarios para
formar la voluntad social en las asambleas de accionistas o para adoptar decisiones en
reuniones de directorio u órgano similar, sin perjuicio de la observancia de los límites
máximos aplicables a la totalidad de las financiaciones comprendidas.
```

## Corte 28 (tramo 2) — `ri_ot::13.4`

- documento: ri_ot; páginas de la unidad: 4, 5, 6; imágenes: `paginas/ri_ot_p4.png`, `paginas/ri_ot_p5.png`, `paginas/ri_ot_p6.png`
- tipo: punto_terminal; rol: None; caracteres propios: 3376
- lista: hijos de `13`, 4 ítems; cierre candidato del detector: «Criterios de consistencia»
- herencia:
  - encabezado: «Instrucciones Particulares»
  - chapeau_seccion: «Deberán informarse las compras y ventas a término y opciones de moneda extranjera identificando / la fecha de concertación de cada operación, el ámbito de negociación o contraparte y el vencimiento / de la operación. / Los movimientos deberán informarse totalizando las operaciones de cada día de la semana estadís- / tica que tengan en común los atributos solicitados. / Como cantidad de activo subyacente deberá informarse el importe en la moneda correspondiente a / ese activo. / Se informarán como Bajas las operaciones rescindidas o ejercidas con anterioridad a la fecha de / vencimiento. Para las operaciones sin vencimiento, siempre se informará su Baja cuando se cance- / len. / Las operaciones de swaps de moneda se informarán desagregando la transacción en tantas opera- / ciones a término como pagos se hayan pactado. / En los casos en que el ámbito de negociación en el que se concerte la operación sea la BCBAIN- / DOL, el DOMAY y BYMA, no deberán consignarse los campos identificación fiscal y denominación / de la contraparte. / Cuando se trate de operaciones realizadas en “A3 Mercados” y pueda identificarse la contra- / parte de la operación, se deberán consignar los datos “Número de identificación de la con- / traparte” y “Denominación de la contraparte”. / Datos Solicitados»
  - encabezado: «13. Concepto»

```text
13.4. Baja de Ventas
Criterios de consistencia
La presentación se considerará validada cuando todas las categorías establecidas en los Apartados
B.2. y B.3. del Régimen informativo Contable Mensual de Operaciones de Cambios se correspon-
dan con los totales que a continuación se detallan:
 Concertaciones de compras a término en moneda extranjera:
- el punto B.2.1. debe corresponderse con el total equivalente en dólares estadounidenses
del activo subyacente de las operaciones de “Alta de Compras” menos las operaciones de
“Baja de Compras”, que afecten únicamente a las operaciones a término de moneda
extranjera liquidables en pesos concertadas en cada fecha.
- el punto B.3.1. debe corresponderse con el total equivalente en dólares estadounidenses
del activo subyacente de las operaciones de “Alta de Compras” menos las operaciones de
“Baja de Compras”, que afecten únicamente a las operaciones a término de moneda
extranjera realizadas y liquidables en el exterior concertadas en cada fecha.
 Vencimientos de compras a término de moneda extranjera:
- el punto B.2.2. debe corresponderse con el total equivalente en dólares estadounidenses
del activo subyacente del conjunto de las operaciones de compras concertadas, cuyo
vencimiento coincida con el de la fecha respectiva, que afecten únicamente a las
operaciones a término de moneda extranjera liquidables en pesos.
- el punto B.3.2. debe corresponderse con el total equivalente en dólares estadounidenses
del activo subyacente del conjunto de las operaciones de compras concertadas, cuyo
vencimiento coincida con el de la fecha respectiva, que afecten únicamente a las
operaciones a término de moneda extranjera realizadas y liquidables en el exterior.
 Concertaciones de ventas a término en moneda extranjera:
- el punto B.2.3. debe corresponderse con el total equivalente en dólares estadounidenses
del activo subyacente de las operaciones de “Alta de Ventas” menos las operaciones de
“Baja de Ventas”, que afecten únicamente a las operaciones a término de moneda
extranjera liquidables en pesos concertadas en cada fecha.
- el punto B.3.3. debe corresponderse con el total equivalente en dólares estadounidenses
del activo subyacente de las operaciones de “Alta de Ventas” menos las operaciones de
“Baja de Ventas”, que afecten únicamente a las operaciones a término de moneda
extranjera realizadas y liquidables en el exterior concertadas en cada fecha.
 Vencimientos de ventas a término de moneda extranjera:
- el punto B.2.4. debe corresponderse con el total equivalente en dólares estadounidenses
del activo subyacente del conjunto de las operaciones de ventas concertadas, cuyo
vencimiento coincida con el de la fecha respectiva, que afecten únicamente a las
operaciones a término de moneda extranjera liquidables en pesos.
- el punto B.3.4. debe corresponderse con el total equivalente en dólares estadounidenses
del activo subyacente del conjunto de las operaciones de ventas concertadas, cuyo
vencimiento coincida con el de la fecha respectiva, que afecten únicamente a las
operaciones a término de moneda extranjera realizadas y liquidables en el exterior.
Se aclara que a los fines de los cruces indicados, se tendrán en cuenta, de corresponder, los tipos
de pase a ser aplicados para la conversión de otras monedas extranjeras a dólares
estadounidenses informados diariamente por el Banco Central.
```

## Corte 29 (tramo 2) — `snp_spd::4.1.4`

- documento: snp_spd; páginas de la unidad: 12; imágenes: `paginas/snp_spd_p12.png`
- tipo: punto_terminal; rol: None; caracteres propios: 436
- lista: hijos de `4.1`, 4 ítems; cierre candidato del detector: «La reserva de uso exclusivo del campo del dato alias CBU es obligatorio, pero incluir in-»
- herencia:
  - encabezado: «Sección 4. Códigos de respuesta rápida»
  - chapeau_seccion: «Para la realización de pagos a través del código de respuesta rápida (código QR) que generen per- / sonas humanas y jurídicas titulares de cuentas en entidades financieras locales, se deberá observar / lo establecido en esta sección.»
  - encabezado: «4.1. Especificaciones técnicas»

```text
4.1.4. Se deberá incluir la CUIT/CUIL del comercio en la posición 50, y se deberá reservar la
posición 51 para la inclusión de la CBU o de la CVU alternativamente o para la incorpo-
ración de alguno de sus alias. Esta posición es de uso exclusivo para dicho dato.
La reserva de uso exclusivo del campo del dato alias CBU es obligatorio, pero incluir in-
formación es optativo. En el caso de la CUIT, el campo y el dato son obligatorios.
```

Contexto, la unidad que sigue en E0: `snp_spd::4.2` (páginas 12)

```text
4.2. Todas las entidades financieras deben habilitar para las cuentas corrientes establecidas en las
normas sobre “Reglamentación de la cuenta corriente bancaria” de personas humanas o jurídi-
cas, y los PSPCP para las cuentas de pago cuyos titulares sean personas jurídicas, códigos QR
regidos por los estándares definidos por el BCRA que les permitan recibir pagos con transfe-
rencia (PCT).
```

## Corte 30 (tramo 2) — `snp_tr_nc::1.5.4.5`

- documento: snp_tr_nc; páginas de la unidad: 8; imágenes: `paginas/snp_tr_nc_p8.png`
- tipo: punto_terminal; rol: None; caracteres propios: 333
- lista: hijos de `1.5.4`, 5 ítems; cierre candidato del detector: «Los PSPCP que no estén inscriptos en el “Registro de billeteras digitales inter-»
- herencia:
  - encabezado: «Sección 1. Transferencias electrónicas de fondos. Conceptos básicos»
  - encabezado: «1.5. Responsabilidades generales de los participantes»
  - encabezado: «1.5.4. PSPCP»

```text
1.5.4.5. Ofrecer todas las funcionalidades necesarias para que los pedidos de fondos
(transferencias pull) puedan efectuarse en forma exitosa.
Los PSPCP que no estén inscriptos en el “Registro de billeteras digitales inter-
operables” no podrán participar en el servicio de transferencia inmediata pull
previsto en el punto 1.5.5.12.
```

Contexto, la unidad que sigue en E0: `snp_tr_nc::1.5.5.1` (páginas 8)

```text
1.5.5.1. Definir las reglas comerciales, técnicas y/o operativas del esquema de transfe-
rencias inmediatas que administre, y asegurar que estén adecuadas al marco
legal y normativo vigente. Establecer relaciones contractuales con cada uno de
los participantes, mediante la suscripción de convenios que fijen la obligación
de éstos de cumplir con las reglas del esquema, disponiendo las multas y san-
ciones en caso de incumplimiento.
```
