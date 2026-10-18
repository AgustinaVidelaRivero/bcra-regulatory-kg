# Lectura de los 14 límites de sub-documento de la tanda 1: fichas (mesa, §118)

Qué se lee: en cada página, el límite que detecta `limites_subdocumento` y que E0 no aplica en estos cinco documentos, porque no
están en la lista de la regla (`censo_sd_152_S2b.json`, `899db5d1…`, con las claves ordenadas). Las unidades se leen contra la página
renderizada (`paginas/`, `pdftoppm -r 110`), no contra el texto que extrae la librería.

**El criterio** es el de la lectura de cortes de S1 (`docs/mandatos/USEG_OFICIAL_segmentacion_e0r2.md:284-292`), el mismo de S1-bis.
Una unidad es correcta si: (1) empieza donde empieza su punto; (2) termina donde termina; (3) no trae texto de otro punto ni restos
de encabezados o pies de página; (4) no le falta texto propio; y (5) su número es el del punto. Rigen las tres reglas de los casos
dudosos y las dos clases de error, con su subclase.

**La pregunta de cada fila de la planilla:** con ese límite, ¿la unidad de E0 que lo contiene cumple el criterio? Si el límite abre de
verdad un sub-documento y la unidad lo atraviesa, es un error de corte (termina fuera de su punto o trae texto de otro punto). Si el
límite no abre nada (un encabezado de página, el renglón de una tabla o de un formulario) y la unidad está bien, es correcta.

La posición del límite: `top` en puntos desde el borde de arriba de la página; en la imagen, a unos `top × 110 / 72` píxeles.
Las marcas van en `planilla_subdocumento_tanda1.tsv`, una fila por límite.

## `ri_rml::3.1`

- TO: ri_rml; páginas: 31 (`paginas/ri_rml_p31.png`)
- tipo: punto_terminal; rol: None; caracteres propios: 1489
- límites en sus páginas (filas de la planilla):
  - fila 1: p. 31, top 91.4 pt (≈ 140 px), forma regimen, «B.C.R.A. 5. EFECTIVO MINIMO Y APLICACIÓN DE RECURSOS (R.I.-E.M. Y A.R.)»
- herencia:
  - encabezado: «Sección 3. Aplicación de la capacidad de préstamo en moneda extranjera»

```text
3.1. Instrucciones generales
Los importes se registrarán en miles de dólares estadounidenses, sin decimales.
En el caso de otras monedas extranjeras, se convertirán a dólares estadounidenses y los
tipos de pase a ser aplicados serán los comunicados por la Mesa de operaciones del Banco
Central de la República Argentina correspondiente a cada uno de los días del período bajo
informe o día anterior disponible.
No obstante ello, todas las partidas se identificarán según su moneda de origen, de acuerdo
con la codificación prevista en el Sistema Centralizado de requerimientos informativos
(SISCEN), tabla T0003, de la que se excluirán aquellas que no estén referenciadas con el
código SWIFT.
A los fines del redondeo de las magnitudes se incrementarán los valores en una unidad
cuando el primer dígito de las fracciones sea igual o mayor que 5, desechando estas últimas
si resultan inferiores.
Los datos se calcularán sobre el promedio mensual de saldos diarios (capitales e intereses)
de las partidas comprendidas, registrados en el mes bajo informe.
Se informarán por separado los capitales de los depósitos a plazo, a la vista y las
obligaciones interfinancieras y -en una única partida- los intereses computables sobre
dichos recursos, mientras que en el caso de las aplicaciones cada partida se
computará incluyendo los intereses que le correspondan.
Las aplicaciones se informarán netas de las previsiones por riesgos de incobrabilidad y de
desvalorización que les sean atribuibles.
```

## `ri_rml::3.2`

- TO: ri_rml; páginas: 31, 32 (`paginas/ri_rml_p31.png`, `paginas/ri_rml_p32.png`)
- tipo: punto_terminal; rol: None; caracteres propios: 3277
- límites en sus páginas (filas de la planilla):
  - fila 1: p. 31, top 91.4 pt (≈ 140 px), forma regimen, «B.C.R.A. 5. EFECTIVO MINIMO Y APLICACIÓN DE RECURSOS (R.I.-E.M. Y A.R.)»
- herencia:
  - encabezado: «Sección 3. Aplicación de la capacidad de préstamo en moneda extranjera»

```text
3.2. Instrucciones particulares
Códigos 101/M y 102/M
Se declararán los depósitos a la vista y a plazo en moneda extranjera y sus saldos
inmovilizados excepto los liquidables en pesos ( se tomarán como referencia los conceptos
registrados en los códigos 315100, 315700 y 316100 del Balance de Saldos ) No se incluyen
los depósitos de títulos valores.
Código 104/M
Deberán informarse los préstamos interfinancieros recibidos, siempre que la entidad otorgante
los haya computado como aplicación de estos recursos.
Código 106/M
Se consignarán los intereses correspondientes a los recursos computables.
Códigos 210/M y 211/M
Se informarán la totalidad de las prefinanciaciones y financiaciones de exportaciones, respectiva-
mente, efectuadas directamente o a través de mandatarios, consignatarios u otros intermediarios
actuantes por cuenta y orden del propietario de las mercaderías, teniendo en cuenta lo previsto en
el punto 2.1.1. de las normas sobre “Política de crédito”.
Código 212/M
Se consignarán las financiaciones a prestadores de servicios a ser exportados directamente com-
prendidas en el segundo párrafo del punto 2.1.1. de las Normas sobre “Política de crédito”.
Código 213/M
Se consignarán otras financiaciones a exportadores de acuerdo con lo establecido en el punto 2.1.2.
de las normas sobre “Política de crédito”.
Código 214/M
Se consignarán las financiaciones a clientes que cuenten con garantías en moneda extranje-
ra otorgadas por los sujetos señalados en el primer párrafo del punto 2.1.2. de las Normas
sobre “Política de crédito” y que se constituyan como principales pagadores con renuncia a
los beneficios de excusión y división.
Código 220/M
Se informarán las financiaciones a productores, procesadores o acopiadores de bienes a que alu-
den los puntos 2.1.3.1. y 2.1.3.2. de las normas sobre “Política de crédito”.
Código 221/M
Se informarán las financiaciones a proveedores de servicios directamente utilizados en el proceso
de exportación de bienes comprendidas en el tercer párrafo del punto 2.1.3. de las Normas sobre
“Política de crédito”.
Código 230/M
Se consignarán las financiaciones a productores de bienes para ser exportados teniendo en cuenta
lo previsto en el punto 2.1.4. de las normas sobre “Política de crédito”.
Código 231/M
Financiaciones a proveedores de bienes y/o servicios que formen parte del proceso productivo de
mercaderías fungibles, en los términos del punto 2.1.5. de las normas sobre “Política de crédito”.
Código 240/M
Se informarán las financiaciones de proyectos de inversión, de capital de trabajo y/o adquisición de
bienes vinculados con la producción de mercaderías para su exportación, comprendidas en el pri-
mer párrafo del punto 2.1.6. de las normas sobre “Política de crédito”.
Código 241/M
Se informarán las financiaciones de importaciones temporarias de insumos, que incrementen o es-
tén vinculados con la producción de mercaderías para su exportación, comprendidas en el primer
párrafo del punto 2.1.6. de las normas sobre “Política de crédito”.
Código 242/M
Se consignarán las financiaciones otorgadas mediante la participación de la entidad en “préstamos
sindicados” sea con entidades locales o del exterior comprendidas en el segundo párrafo del punto
2.1.6. de las normas sobre “Política de crédito”.
```

## `ri_rml::S6`

- TO: ri_rml; páginas: 76, 77 (`paginas/ri_rml_p76.png`, `paginas/ri_rml_p77.png`)
- tipo: seccion_sin_puntos; rol: None; caracteres propios: 4102
- límites en sus páginas (filas de la planilla):
  - fila 2: p. 76, top 127.2 pt (≈ 194 px), forma parte, «I. Instrucciones generales para la presentación de información sobre las posiciones diarias en»
  - fila 3: p. 77, top 125.7 pt (≈ 192 px), forma parte, «II. Instrucciones especiales para el mes de Agosto 2025»
- herencia: (ninguna)

```text
Sección 6. Posición de Efectivo Mínimo Diaria
I. Instrucciones generales para la presentación de información sobre las posiciones diarias en
pesos
Entidades financieras del grupo A y sucursales o subsidiarias de G-SIB no incluidas en
ese grupo presentarán la información de acuerdo con el siguiente esquema:
- Partidas vinculadas con la exigencia y otras de cálculo mensual: se presentarán al inicio del
mes al que corresponde el cálculo de la posición y su vencimiento operará a las 15hs del
tercer día hábil de ese mes.
- Partidas correspondientes a la integración diaria, así como los saldos correspondientes a
“Depósitos en pesos en cuentas de los proveedores de servicios de pago que ofrecen
cuentas de pago (PSPOCP) en las que se encuentren depositados los fondos de sus clien-
tes”: se presentarán en forma diaria y su vencimiento operará a las 15 hs del segundo día
hábil posterior al que corresponden los datos.
Para el resto de las entidades, tanto para la información mensual como la diaria, el vencimien-
to para la presentación operará el día 22 del mes siguiente al que corresponden los datos.
1. Exigencia y Otras Informaciones
El modelo de información es el incluido en el punto 1.10.1 para partidas comprendidas en mo-
neda pesos. Se aclara que, si bien no forman parte de las posiciones que se deben cumplir en
forma diaria, se deben informar las partidas 110500/M, 10120X/M, 11010X7M expresadas en
pesos.
Para la partida 102200/001 “Depósitos en pesos en cuentas de los proveedores de servicios de
pago que ofrecen cuentas de pago (PSPOCP) en las que se encuentren depositados los fondos
de sus clientes” se informará el promedio acumulado desde el inicio del mes hasta el día repor-
tado.
Adicionalmente deberán considerarse las partidas del modelo de información incluido en los
puntos 1.10.3. y 1.10.4.
2. Integración
Se informará según el modelo de información detallado en el punto 1.10.2 de las presentes ins-
trucciones respecto de partidas en pesos.
Adicionalmente, a fin de informar la porción de la exigencia en pesos integrada en forma diaria
con títulos, se consignará el saldo de las partidas 210104/TP, 210105/TP, 210106/TP y
210109/TP.
Los controles respecto de las partidas 210100/TP y 500000/TP se realizarán cuando se informe
la información mensual para posiciones en títulos y moneda extranjera.
II. Instrucciones especiales para el mes de Agosto 2025
La información a remitir para el periodo agosto 2025 deberá realizarse conforme las instrucciones
que se detallan a continuación.
Las entidades financieras del grupo A y sucursales o subsidiarias de G-SIB no incluidas en ese gru-
po deberán presentar el día 12/09 los datos de las partidas correspondientes a la integración del
primer subperiodo de agosto, así como los diarios desde el 18/08.
Las entidades B y C remitirán la información de ambos subperiodos el 22/09.
Las partidas que componen la integración se informarán de acuerdo con las disposiciones de los
puntos 1 y 2 de esta sección. Las correspondientes al período comprendido entre el 1 y el 17/8 se
presentarán en promedio del período. A partir de los datos del día 18 y hasta el 31 de agosto, tanto
las partidas de integración como la 102200/001 se informarán con los datos de cada día.
A efectos de determinar la posición del primer subperiodo de agosto (del 1 al 17), se informará la
partida 760001 conforme la siguiente expresión:
760001= 760000 * 31/17
(JULIO)
El exceso (o defecto) que resulte de la posición en promedio del primer subperíodo, se trasladará al
segundo subperiodo de agosto, teniendo en cuenta la proporción de los días (*17/14) y se informará
en las siguientes partidas:
760002 = 760001 * 17/14
760003: Exceso (defecto) del subperiodo 1 *17/14 - 760002
A fin de determinar el importe de la partida 760000 a considerar en las posiciones diarias del mes
de septiembre, se calculará el promedio de los excesos y defectos reales de los 14 días del segun-
do subperiodo, según la siguiente expresión:
Si = [∑ (Excesos/ defectos) – 760002] / 14 > 0 entonces
760000 = Min { [∑ (Excesos/ defectos) – 760002] / 14}; 3% * EEMA
(AGOSTO)
```

## `ri_gerc::2.3`

- TO: ri_gerc; páginas: 4 (`paginas/ri_gerc_p4.png`)
- tipo: punto_terminal; rol: None; caracteres propios: 1356
- límites en sus páginas (filas de la planilla):
  - fila 4: p. 4, top 89.5 pt (≈ 137 px), forma regimen, «B.C.R.A. 23. GRANDES EXPOSICIONES AL RIESGO DE CRÉDITO (R.I.-G.E.)»
- herencia:
  - encabezado: «Sección 2. Instrucciones Particulares»

```text
2.3. Niveles de consolidación
Se tendrá en cuenta lo dispuesto en la Sección 6. de las normas sobre “Grandes exposiciones
al riesgo de crédito”, aplicándose los siguientes códigos, que deberán ser coincidentes con los
informados en el RI Exigencia e integración de capitales mínimos:
[TABLA ri_gerc::tabla002 | página 4 | e0_tablas | columnas]
Columnas: CODIGO | CASOS
Fila 1: CODIGO = 0 | CASOS = Entidad que no consolida, con filiales en el país y en el exterior
Fila 2: CODIGO = 1 | CASOS = Entidad que consolida, con filiales en el país y en el exterior
Fila 3: CODIGO = 2 | CASOS = Consolidado mensual (entidad financiera con filiales y subsidiarias significativas en el país y en el exterior) - (con el alcance definido en el punto 6.2. de las normas sobre “Supervisión consolidada”)
Fila 4: CODIGO = 9 | CASOS = Consolidado mensual (entidad financiera con filiales y subsidiarias significativas en el país y en el exterior -que no consolida con otras entidades financieras-) - (con el alcance definido en el punto 6.2. de las nor- mas sobre “Supervisión consolidada”)
Fila 5: CODIGO = 3 | CASOS = Consolidado trimestral (entidad financiera con filiales, subsidiarias significativas y otros entes en el país y en el exterior) - (suspendido desde abril/24 según punto 6.1. de las normas sobre “Supervisión con- solidada”)
[FIN TABLA ri_gerc::tabla002]
```

## `ri_gerc::2.4::intro`

- TO: ri_gerc; páginas: 4 (`paginas/ri_gerc_p4.png`)
- tipo: mini_chunk; rol: intro; caracteres propios: 2094
- límites en sus páginas (filas de la planilla):
  - fila 4: p. 4, top 89.5 pt (≈ 137 px), forma regimen, «B.C.R.A. 23. GRANDES EXPOSICIONES AL RIESGO DE CRÉDITO (R.I.-G.E.)»
- herencia:
  - encabezado: «Sección 2. Instrucciones Particulares»
  - encabezado: «2.4. Exposiciones»

```text
Se consignarán las exposiciones contempladas en el punto 1.4. de las normas sobre “Grandes
exposiciones al riesgo de crédito”, para cada nivel de consolidación definido, identificándose el
tipo de exposición de que se trate.
Cuando se trate de un grupo de contrapartes conectadas, se informará la exposición agrega-
da -bajo la identificación y denominación asignadas según lo previsto en los puntos 2.1. y 2.2.
para el código “88”-, remitiendo la composición del grupo y la exposición de cada uno de los in-
tegrantes en el cuadro del punto 3.3.
En el caso de “Cliente desconocido”, al considerarse como una contraparte, será tratada como
una gran exposición al riesgo de crédito si es igual o superior al 10 % del capital de nivel uno.
Consecuentemente, deberá cumplirse con los requisitos de información sobre las exposiciones
al riego de crédito a que hace referencia el punto 1.4.1. de las normas sobre “Grandes exposi-
ciones al riesgo de crédito”.
Si la exposición al “cliente desconocido” se encuentra entre las 20 mayores de la entidad fi-
nanciera, según el punto 1.4.4. de las normas sobre “Grandes exposiciones al riesgo de crédi-
to”, corresponderá remitir tal información a la SEFyC en cumplimiento de lo exigido en el punto
referenciado.
Respecto de los saldos de las entidades financieras en cuentas a la vista en bancos del exte-
rior que, con carácter transitorio y circunstancial, se originen exclusivamente por operaciones
de cambio de clientes en la medida que reúnan las condiciones previstas en la Comunicación
"A" 7623 y el criterio definido en el punto 1.4.3. de las normas sobre “Grandes exposiciones al
riesgo de crédito” deberán informarse como exposiciones no alcanzadas, utilizando a tal fin el
código 4 de tipo de exposición.
Para la base de capital admisible se considerará el capital de nivel 1 -según lo establecido en
el punto 1.2.4. de las mismas normas-, definido por los siguientes códigos de partida del régi-
men informativo de “Exigencia e integración de capitales mínimos”:
Capital de nivel 1 (Cn1) = Códigos (70210000 – 70220000 + 70230000 – 70240000)
```

## `ri_pgn::S1`

- TO: ri_pgn; páginas: 2 (`paginas/ri_pgn_p2.png`)
- tipo: seccion_sin_puntos; rol: None; caracteres propios: 1076
- límites en sus páginas (filas de la planilla):
  - fila 5: p. 2, top 95.0 pt (≈ 145 px), forma regimen, «B.C.R.A. 16. POSICION GLOBAL NETA DE MONEDA EXTRANJERA (R.I. – P.G.)»
- herencia: (ninguna)

```text
Sección 1. Instrucciones generales.
Las entidades financieras deberán suministrar información respecto de la Posición Global Neta de
Moneda Extranjera correspondiente a cada mes.
Esta información deberá elaborarse a nivel de casa central y filiales en el país.
Los datos se presentarán con las formalidades del Régimen Informativo Contable Mensual.
Los importes se expresarán en miles de pesos sin decimales.
A los fines del redondeo de las magnitudes se incrementarán los valores en una unidad cuando el
primer dígito de las fracciones sea igual o mayor que 5, desechando las que resulten inferiores.
Los saldos en moneda extranjera se deberán convertir a pesos diariamente considerando el tipo de
cambio de referencia del dólar estadounidense difundido por el B.C.R.A., considerando lo
establecido en las normas sobre “Posición global neta de moneda extranjera”.
Las monedas extranjeras distintas de dólar estadounidense se convertirán previamente a esta
moneda utilizando los tipos de pase comunicados por la Mesa de operaciones del Banco Central de
la República Argentina.
```

## `snp_tr::1.7.3`

- TO: snp_tr; páginas: 29, 30, 31, 32 (`paginas/snp_tr_p29.png`, `paginas/snp_tr_p30.png`, `paginas/snp_tr_p31.png`, `paginas/snp_tr_p32.png`)
- tipo: punto_terminal; rol: None; caracteres propios: 5535
- límites en sus páginas (filas de la planilla):
  - fila 6: p. 31, top 127.7 pt (≈ 195 px), forma regimen, «2 - CUIL»
- herencia:
  - encabezado: «Sección 1. Transferencias en lote.»
  - chapeau_seccion: «La presente sección tiene como objetivo definir las instrucciones operativas de las transferencias en / lote. / Estas instrucciones operativas definen la forma en que operarán los participantes del sistema, los / circuitos de envío, compensación y distribución de la información y las transacciones, los controles a / efectuar por los participantes, las responsabilidades de los mismos y las características de la infor- / mación a intercambiar electrónicamente. / Son aplicables a las presentes normas las definiciones de la Sección 1. de las normas “Sistema / Nacional de Pagos – Transferencias – Normas complementarias”.»
  - encabezado: «1.7. Diseño de registros.»

```text
1.7.3. Registro individual de órdenes de transferencia y devoluciones de órdenes de transferencia
[TABLA snp_tr::tabla020 | página 29 | e0_tablas | posicional]
Fila 1: col1 = Campo | col2 = 1 | col3 = 2 | col4 = 3 | col5 = 4 | col6 = 5 | col7 = 6 | col8 = 7 | col9 = 8 | col10 = 9 | col11 = 10
Fila 2: col1 = Nombre | col2 = Identifi- cador de registro | col3 = Código de transac- ción | col4 = Entidad a acre- ditar | col5 = Cuenta a acreditar | col6 = Importe | col7 = Referen- cia uní- voca de la trans- ferencia | col8 = Identifi- cación del cliente benefi- ciario | col9 = Moneda de transac- ción/Tipo de trans- ferencia | col10 = Regis- tros adicio- nales | col11 = Contador de regis- tro
Fila 3: col1 = Requeri- miento del cam- po | col2 = M | col3 = M | col4 = M | col5 = M | col6 = M | col7 = M | col8 = M | col9 = M | col10 = M | col11 = M
Fila 4: col1 = Tipo | col2 = ´6´ | col3 = Numéri- co | col4 = Numé- rico | col5 = Numéri- co | col6 = $$$$$$$ $$$$$cc | col7 = Alfanu- mérico | col8 = Alfa- numé- rico | col9 = Numéri- co | col10 = Numéri- co | col11 = Numéri- co
Fila 5: col1 = Longitud | col2 = 1 | col3 = 2 | col4 = 8 | col5 = 14 | col6 = 14 | col7 = 15 | col8 = 22 | col9 = 2 | col10 = 1 | col11 = 15
Fila 6: col1 = Posición | col2 = 01-01 | col3 = 02-03 | col4 = 04-11 | col5 = 12-25 | col6 = 26-39 | col7 = 40-54 | col8 = 55-76 | col9 = 77-78 | col10 = 79-79 | col11 = 80-94
[FIN TABLA snp_tr::tabla020]
Descripción de los campos:
1. Identificador de registro
6 Registro individual
2. Código de transacción
Indica el tipo de transacción informada y el tipo de cuenta involucrada en la transacción:
Transacciones/Devoluciones Rechazos/Rejects de cámara “Unwinding”
32 31 37
3. Entidad a acreditar
Contiene el número identificatorio de la entidad destino de la transacción (se incluye el número de entidad con 3 caracteres precedidos por un
cero -“0”- y el número de sucursal con 4 posiciones). Al número identificatorio de la entidad se le adicionan 500 cuando se envían transacciones
en dólares estadounidenses.
4. Cuenta a acreditar
Indica la cuenta a acreditar, y debe contener los datos exactos de la cuenta. Estos datos serán tomados del bloque dos de la Clave Bancaria
Uniforme (CBU) incluyendo su dígito verificador. Se incluyen números del 0 al 9, alineados a la derecha.
5. Importe
Indica el importe a ser acreditado en la cuenta antes detallada.
6. Referencia unívoca de la transferencia
Indica la referencia por medio de la cual la empresa o individuo identifica unívocamente la transferencia a efectuar.
Se deberá completar con los códigos de 12 posiciones libres alfanuméricas definidos en la Sección 3.
7. Identificación del cliente beneficiario
Se identifica en forma unívoca al cliente beneficiario de la transferencia, ya sea con su número de CUIT, CUIL o CDI; el campo se compondrá de
la siguiente forma:
a) En la primera posición a izquierda el código del tipo de clave:
1 - CUIT
2 - CUIL
3 - CDI
b) En las 11 posiciones siguientes el número de clave fiscal
c) 5 espacios en blanco
d) Las últimas tres posiciones se completarán de la siguiente manera: la primera posición con un “0” y las dos restantes con el código de ope-
ratoria del BCRA:
73 - Transferencias para acreditar en cuentas por operaciones gravadas.
74 - Transferencias para acreditar en cuentas por operaciones no gravadas.
75 - Transferencias por pago de sueldos.
8. Moneda de transacción/tipo de transferencia
Identifica la moneda de la transacción y el tipo de transferencia. Se completará de la siguiente manera: la primera posición con cero (0) para
transacciones en pesos, con uno (1) para transacciones en dólares estadounidenses y con dos (2) para transacciones en euros.
0 - Devoluciones de sueldos
1 - Pago de sueldos
2 - Pago a proveedores
3 - Transferencias entre clientes o terceros
4 - Asignaciones familiares
5 - Pagos previsionales
6 - Devoluciones de pagos previsionales
7 - Devoluciones de pago a proveedores
8 - Devoluciones entre clientes y/o terceros
9 - Devoluciones de asignaciones familiares
A - Embargos sobre haberes por orden judicial
B - Devoluciones embargos sobre haberes por orden judicial
C - Transferencias por orden judicial
D - Devoluciones de transferencias por orden judicial
9. Registros adicionales
Indica si existen o no registros adicionales (“1” o “0” respectivamente).
10. Contador de registro (“Trace number”)
Incluye el número de identificación de la entidad originante en 8 posiciones (4 para la entidad y 4 para la sucursal) y luego en las posiciones 9 a 15 un
número secuencial ascendente unívoco en todas las sesiones del día para cada registro enviado en un archivo. Esto implica que el número del conta-
dor de registro puede repetirse en distintos archivos transmitidos a lo largo del día. Estas 15 posiciones deberán ir ordenadas secuencialmente dentro
de cada lote. Al número identificatorio de la entidad se le adicionan 500 cuando se envían transacciones en dólares estadounidenses.
En caso de que una entidad represente a otra para la presentación de cheques, el número de sucursal será reemplazado por un “9” en la quinta
posición y el número de entidad representada en las siguientes posiciones.
Comentarios adicionales:
Cuando un campo posea más caracteres que los requeridos para la información a completar, se deberán llenar con ceros comenzando desde el
margen izquierdo, en el caso de campos numéricos y con blancos a la derecha en el caso de campos alfanuméricos. Los caracteres alfabéticos de
los campos alfanuméricos deberán ser siempre informados en mayúsculas.
```

## `manori::1.5.1`

- TO: manori; páginas: 32, 33, 34, 35, 36, 37, 38 (`paginas/manori_p32.png`, `paginas/manori_p33.png`, `paginas/manori_p34.png`, `paginas/manori_p35.png`, `paginas/manori_p36.png`, `paginas/manori_p37.png`, `paginas/manori_p38.png`)
- tipo: punto_terminal; rol: None; caracteres propios: 15949
- límites en sus páginas (filas de la planilla):
  - fila 7: p. 33, top 153.5 pt (≈ 235 px), forma parte, «I. TÉRMINOS Y CONDICIONES PRÉSTAMO HIPOTECARIO»
  - fila 8: p. 33, top 206.1 pt (≈ 315 px), forma parte, «II. DATOS PERSONALES»
  - fila 9: p. 33, top 412.8 pt (≈ 631 px), forma parte, «III. INFORMACIÓN LABORAL»
  - fila 10: p. 34, top 109.2 pt (≈ 167 px), forma parte, «IV. INGRESO MENSUAL Y GASTOS MENSUALES»
  - fila 11: p. 35, top 109.2 pt (≈ 167 px), forma parte, «V. ACTIVOS Y PASIVOS»
  - fila 12: p. 36, top 231.1 pt (≈ 353 px), forma parte, «VI. INFORMACIÓN DE LA PROPIEDAD Y DESTINO DE LOS FONDOS»
  - fila 13: p. 37, top 108.4 pt (≈ 166 px), forma parte, «VII. ACEPTACIÓN Y ACUERDO»
  - fila 14: p. 37, top 299.5 pt (≈ 458 px), forma parte, «VIII. INFORMACIÓN DE LA ENTIDAD»
- herencia:
  - encabezado: «Sección 1. Manual de Originación y Administración de Préstamos Hipotecarios.»
  - chapeau_seccion: «Introducción y objetivos. / En la presente sección se establece un conjunto de pautas, prácticas y procedimientos que las / entidades financieras pueden seguir en la originación y administración de préstamos con ga- / rantía hipotecaria sobre propiedades para vivienda. / La sección se encuentra organizada en cinco puntos: / 1.1. Características y lineamientos para el otorgamiento de los préstamos hipotecarios. / 1.2. Originación de los préstamos hipotecarios. / 1.3. Procedimientos de administración. / 1.4. Sistemas de información. / 1.5. Modelos de formularios.»
  - encabezado: «1.5. Modelos de formularios.»

```text
1.5.1. Solicitud de crédito hipotecario.
Cuando los préstamos se otorguen mediante métodos específicos de evaluación a los
que se refieren las normas sobre “Gestión crediticia” (sistemas de “screening” y modelos
de “credit scoring”), aquellas variables que se hayan tenido en cuenta en los modelos y
que no hayan sido previstas en este formulario, deberán ser explicitadas utilizando a
esos efectos la hoja complementaria/solicitud de crédito hipotecario.
[TABLA manori::tabla000 | página 33 | e0_tablas | posicional]
Fila 1: col1 = SOLICITUD CRÉDITO HIPOTECARIO CÓDIGO O NÚMERO IDENTIFICACIÓN CRÉDITO: CÓDIGO O NÚMERO CRÉDITO TITULIZADO: TITULAR GARANTE ⟨abarca hasta col7⟩
Fila 2: col1 = I. TÉRMINOS Y CONDICIONES PRÉSTAMO HIPOTECARIO ⟨abarca hasta col7⟩
Fila 3: col1 = MONTO OTORGADO $ CANTIDAD D E UVA/ UVI (DE CORRES- PONDER) (6) | col2 = TASA DE INTE- RÉS NOMINAL ANUAL % | col3 = COSTO FINAN- CIERO TOTAL % | col4 = PLAZO ( N° DE MESES) ⟨abarca hasta col5⟩ | col6 = SISTEMA DE AMORTIZACIÓN FRANCÉS ALEMÁN OTROS (DETALLAR) | col7 = MONTO DE LA PRIMERA CUOTA MENSUAL $ CANTIDAD DE UVA/ UVI (DE CORRESPONDER)(6)
Fila 4: col1 = II. DATOS PERSONALES ⟨abarca hasta col7⟩
Fila 5: col1 = APELLIDO Y NOMBRES (SEGÚN CONSTA EN DOCUMENTO DE IDENTIDAD) ⟨abarca hasta col7⟩
Fila 6: col1 = TELÉFONO PARTICULAR (INCLUIR CÓDIGO DE ÁREA) TELÉFONO LABORAL (INCLUIR CÓDIGO DE ÁREA) –SI DIFIERE DEL PARTICULAR– FIJO: CELULAR: FIJO: CELULAR: ⟨abarca hasta col7⟩
Fila 7: col1 = FECHA DE NACIMIENTO ⟨abarca hasta col4⟩ | col5 = SEXO F M ⟨abarca hasta col7⟩
Fila 8: col1 = TIPO Y NÚMERO DE DOCUMENTO DE IDENTIDAD ⟨abarca hasta col5⟩ | col6 = MÁXIMO NIVEL EDUCACIONAL COMPLETADO PRIMARIO SECUNDARIO TERCIARIO UNIVERSITARIO ⟨abarca hasta col7⟩
Fila 9: col1 = PROFESIÓN / ACTIVIDAD ⟨abarca hasta col7⟩
Fila 10: col1 = CASADA/O SOLTERA/O (cid:31) DIVORCIADA/O (cid:31) VIUDA/O (cid:31)UNION CONVIVENCIAL INSCRIPTA ⟨abarca hasta col5⟩ | col6 = CANTIDAD DE HIJOS MENORES DE 18 AÑOS ⟨abarca hasta col7⟩
Fila 11: col1 = NÚMERO DE IDENTIFICACIÓN TRIBUTARIA Y/O PREVISIONAL (cid:31) CUIT (cid:31) CUIL ⟨abarca hasta col5⟩ | col6 = POSICIÓN IMPOSITIVA (IVA) (cid:31) INSCRIPTO (cid:31)NO INSCRIPTO (cid:31) EXENTO (cid:31)MONOTRIBUTO ⟨abarca hasta col7⟩
Fila 12: col1 = APELLIDO Y NOMBRES DEL CÓNYUGE O CONVIVIENTE (SEGÚN DOCUMENTO DE IDENTIDAD) ⟨abarca hasta col4⟩ | col5 = TIPO Y NÚMERO DE DOCUMENTO DE IDENTIDAD ⟨abarca hasta col7⟩
Fila 13: col1 = DIRECCIÓN DE CORREO ELECTRÓNICO: ⟨abarca hasta col7⟩
Fila 14: col1 = DOMICILIO ACTUAL (cid:31) PROPIO (cid:31) ALQUILADO (cid:31) FAMILIAR (CALLE Y NÚMERO, PISO, NÚMERO DEPTO., LOCALIDAD, PROVINCIA, CÓDIGO POSTAL) ⟨abarca hasta col7⟩
Fila 15: col1 = III. INFORMACIÓN LABORAL ⟨abarca hasta col7⟩
Fila 16: col1 = (cid:31)(cid:31) EN RELACIÓN DE DEPENDENCIA NOMBRE Y DIRECCIÓN DEL EMPLEADOR (cid:31) FIJO (cid:31) CONTRATADO (cid:31) ANTIGÜEDAD ⟨abarca hasta col4⟩ | col5 = (cid:31) AUTÓNOMO / MONOTRIBUTISTA ANTIGÜEDAD EN LA ACTIVIDAD / PROFESIÓN ⟨abarca hasta col7⟩
Fila 17: col1 = (cid:31) EN RELACIÓN DE DEPENDENCIA NOMBRE Y DIRECCIÓN DEL EMPLEADOR (cid:31) FIJO (cid:31) CONTRATADO (cid:31) ANTIGÜEDAD ⟨abarca hasta col4⟩ | col5 = (cid:31) (cid:31) AUTÓNOMO / MONOTRIBUTISTA ANTIGÜEDAD EN LA ACTIVIDAD / PROFESIÓN ⟨abarca hasta col7⟩
Fila 18: col1 = COMPLETAR DE TENER UNA ANTIGÜEDAD MENOR A UN AÑO EN POSICIÓN, HASTA COMPLETAR UN AÑO DE ANTIGUEDAD ⟨abarca hasta col7⟩
Fila 19: col1 = (cid:31) AUTÓNOMO (cid:31) EN RELACIÓN DE DEPENDENCIA NOMBRE Y DIRECCIÓN DEL EMPLEADOR ⟨abarca hasta col4⟩ | col5 = FECHA (DESDE / HASTA) - INGRESO MENSUAL NETO $ ⟨abarca hasta col7⟩
Fila 20: col1 = (cid:31) AUTÓNOMO (cid:31) EN RELACIÓN DE DEPENDENCIA NOMBRE Y DIRECCIÓN DEL EMPLEADOR ⟨abarca hasta col4⟩ | col5 = FECHA (DESDE / HASTA) - INGRESO MENSUAL NETO $ ⟨abarca hasta col7⟩
Fila 21: col1 = FIRMA Y ACLARACIÓN: FECHA: ⟨abarca hasta col7⟩
[FIN TABLA manori::tabla000]
[TABLA manori::tabla001 | página 34 | e0_tablas | posicional]
Fila 1: col1 = IV. INGRESO MENSUAL Y GASTOS MENSUALES (1) ⟨abarca hasta col7⟩
Fila 2: col1 = INGRESO MENSUAL (2) | col2 = DEUDOR | col3 = TOTAL SOLICITANTES (3) | col4 = GASTOS DE VIVIENDA DE LOS SOLICITANTES | col5 = ACTUAL (5) ⟨abarca hasta col6⟩ | col7 = PRESU- PUESTADO (5)
Fila 3: col1 = SUELDO / INGRESO NETO MENSUAL SUELDO ANUAL COMPLEMENTARIO (DIVIDIDO DOCE) COMISIONES (PROMEDIO MENSUAL ÚLTIMOS 12 MESES) INGRESOS POR RENTAS (PROMEDIO MENSUAL ÚLTIMO AÑO) GRATIFICACIONES (PROMEDIO MENSUAL ÚLTIMO AÑO) OTROS TOTAL | col4 = ALQUILER CUOTA MENSUAL PRÉSTAMO HIPOTECARIO (CAPITAL + INT) IVA ( SI CORRESPONDE) SEGURO DE LA PROPIEDAD IMPUESTOS INMOBILIARIOS EXPENSAS OTROS PAGOS MENSUALES (4) TOTAL
Fila 4: col1 = DESCRIPCIÓN OTROS INGRESOS/GASTOS. ⟨abarca hasta col5⟩ | col6 = MONTOS NETOS MEN- SUALES ⟨abarca hasta col7⟩
Fila 5: col1 = EL ABAJO FIRMANTE MANIFIESTA, CON CARÁCTER DE DECLARACIÓN JURADA, QUE A LA FECHA NO CONOCE LA EXISTENCIA DE NINGUNA CAUSA O RAZÓN QUE PUDIERA PRODUCIR UNA REDUCCIÓN SIGNIFICATIVA DE SUS INGRESOS. ⟨abarca hasta col7⟩
[FIN TABLA manori::tabla001]
(1) EN PRÉSTAMOS OTORGADOS POR MÉTODOS “SCREENING” O “SCORING” NO SE REQUERIRÁ LA INTEGRACIÓN DE INGRESOS EN ESTA PLANILLA Y SE COMPU-
TARÁN AQUELLOS GASTOS QUE FUERAN TENIDOS EN CUENTA EN EL MODELO EMPLEADO.
(2) TODOS LOS ÍTEMS A SER EXPRESADOS EN MONTOS NETOS MENSUALES.
(3) INCLUYE GARANTES, SEGÚN LA DEFINICIÓN DEL PUNTO 1.1.2.
(4) ESTE ÍTEM DEBERÁ SER IGUAL A LA SUMA DE TODOS LOS CONCEPTOS DE SERVICIOS MENSUALES QUE SE DETALLAN EN LA SECCIÓN V CORRESPONDIENTE A
PASIVOS.
(5) A SER COMPLETADOS EN LA SOLICITUD DEL DEUDOR.
(6) EN PRÉSTAMOS OTORGADOS BAJO LA MODALIDAD DE UNIDADES DE VALOR ADQUISITIVO ACTUALIZABLES POR “CER” - LEY 25.827 (“UVA”) O DE UNIDADES DE
VIVIENDA ACTUALIZABLES POR “ICC”- LEY 27.271 (“UVI”): IMPORTE DE CAPITAL DESEMBOLSADO EXPRESADO EN CANTIDADES DE UVA O UVI, SEGÚN CORRES-
PONDA.
FIRMA Y ACLARACIÓN : FECHA:
[TABLA manori::tabla002 | página 35 | e0_tablas | posicional]
Fila 1: col1 = V. ACTIVOS Y PASIVOS ⟨abarca hasta col7⟩
Fila 2: col1 = COMPLETAR ÚNICAMENTE EN FORMA CONJUNTA S I CODEUDOR ES CÓNYUGE O CONVIVIENTE, EN EL RESTO DE LOS CASOS COMPLETAR FORMULARIOS SEPARADOS PARA CADA CODEUDOR Y GARANTE. ⟨abarca hasta col7⟩
Fila 3: col1 = ACTIVOS DESCRIPCIÓN | col2 = EFECTIVO O V ALOR DE MERCADO | col3 = PASIVOS Y PRÉSTAMOS CON GARANTÍA REAL: DETALLAR EL NOMBRE DEL ACREEDOR, DOMICI- LIO, NÚMEROS DE CUENTAS Y SALDOS DE TODOS LOS PASIVOS, INCLUYENDO PRÉSTAMOS PRENDARIOS PARA AUTOMOTORES, TARJETAS DE CRÉDITO, PRÉSTAMOS PARA LA VIVIENDA, SENTENCIAS JUDICIALES (COMO POR EJEMPLO POR ALIMENTOS), PRENDAS SOBRE ACCIONES, PRÉSTAMOS OTORGADOS POR EL EMPLEADOR, GARANTÍAS OTORGADAS, ETC. UTILIZAR, DE SER NECESARIO, LA HOJA COMPLEMENTARIA DE ESTA SOLICITUD. INDICAR CON ASTERISCO (*) LOS PASIVOS QUE SERÁN CANCELADOS POR LA VENTA DE INMUEBLES PROPIOS O POR LA REFINANCIACIÓN DE LA DEUDA HIPOTECARIA. ⟨abarca hasta col7⟩
Fila 4: col1 = TENEDOR DE LOS FONDOS PROPIOS: | col2 = $ | col3 = PASIVOS ⟨abarca hasta col5⟩ | col6 = PASIVOS MENSUALES Y CUOTAS RESTANTES | col7 = SALDO DE DEUDA
Fila 5: col1 = DETALLAR A CONTINUACIÓN CUENTAS CORRIENTES Y CAJAS DE AHORRO: ⟨abarca hasta col2⟩
Fila 6: col1 = NOMBRE Y DIRECCIÓN DE LA ENTIDAD FINANCIERA ⟨abarca hasta col2⟩ | col3 = NOMBRE Y DIRECCIÓN DEL ACREEDOR ⟨abarca hasta col5⟩ | col6 = PAGOS MENSUALES EN $ | col7 = $
Fila 7: col3 = USO DE LOS FONDOS: ⟨abarca hasta col5⟩
Fila 8: col1 = NÚMERO DE CUENTA : | col2 = $ | col3 = NÚMERO DE CUENTA: ⟨abarca hasta col5⟩
Fila 9: col1 = NOMBRE Y DIRECCIÓN DE LA ENTIDAD FINANCIERA ⟨abarca hasta col2⟩ | col3 = NOMBRE Y DIRECCIÓN DEL ACREEDOR ⟨abarca hasta col5⟩ | col6 = PAGOS MENSUALES EN $ | col7 = $
Fila 10: col3 = USO DE LOS FONDOS: ⟨abarca hasta col5⟩
Fila 11: col1 = NÚMERO DE CUENTA : | col2 = $ | col3 = NÚMERO DE CUENTA: ⟨abarca hasta col5⟩
Fila 12: col1 = ACCIONES Y TÍTULOS (TENEDO R, NÚMERO DE CUENTA, MONTO) | col2 = $ | col3 = NOMBRE Y DIRECCIÓN DEL ACREEDOR ⟨abarca hasta col5⟩ | col6 = PAGOS MENSUALES EN $ | col7 = $
Fila 13: col3 = USO DE LOS FONDOS: ⟨abarca hasta col5⟩
Fila 14: col1 = SUBTOTAL ACTIVOS LÍQUIDOS | col2 = $ | col3 = NÚMERO DE CUENTA: ⟨abarca hasta col5⟩
Fila 15: col1 = INMUEBLES (INGRESAR VALOR ACTUAL TOTAL DE MERCADO SEGÚN DETALLE EN PRÓXIMA HOJA) | col2 = $ | col3 = NOMBRE Y DIRECCIÓN DEL ACREEDOR ⟨abarca hasta col5⟩ | col6 = PAGOS MENSUALES EN $ | col7 = $
Fila 16: col3 = USO DE LOS FONDOS: ⟨abarca hasta col5⟩
Fila 17: col1 = PATRIMONIO NETO DE EMPRES AS (SEGÚN BALANCES ADJUNTOS) | col2 = $ | col3 = NÚMERO DE CUENTA: ⟨abarca hasta col5⟩
Fila 18: col3 = NOMBRE Y DIRECCIÓN DEL ACREEDOR ⟨abarca hasta col5⟩ | col6 = PAGOS MENSUALES EN $ | col7 = $
Fila 19: col3 = USO DE LOS FONDOS: ⟨abarca hasta col5⟩
Fila 20: col1 = AUTOMÓVILES (MARCA, MODELO, AÑO) | col2 = $ | col3 = NÚMERO DE CUENTA: ⟨abarca hasta col5⟩
Fila 21: col3 = SENTENCIAS JUDICIALES (COMO POR EJEMPLO PAGO DE CUOTA POR ALI- MENTOS) ⟨abarca hasta col5⟩ | col6 = $
Fila 22: col1 = OTROS ACTIVOS (DETALLAR) | col2 = $ | col3 = OTROS PASIVOS (DETALLAR): ⟨abarca hasta col5⟩
Fila 23: col3 = TOTAL PAGOS MENSUALES ⟨abarca hasta col5⟩ | col6 = $
Fila 24: col1 = TOTAL ACTIVOS (A ): | col2 = $ | col3 = PATRI- MONI O (A-B ) | col4 = $ ⟨abarca hasta col5⟩ | col6 = TOTAL PASIVOS (B) | col7 = $
Fila 25: col1 = FIRMA Y ACLARACIÓN FECHA: ⟨abarca hasta col4⟩ | col5 = FIRMA CODEUDOR Y ACLARACIÓN FECHA: (SI CODEUDOR ES CÓNYUGE O CONVIVIENTE) ⟨abarca hasta col7⟩
[FIN TABLA manori::tabla002]
[TABLA manori::tabla003 | página 36 | e0_tablas | posicional]
Fila 1: col1 = V. ACTIVOS Y PASIVOS (CONTINUACIÓN) ⟨abarca hasta col14⟩
Fila 2: col1 = DETALLE DE INMUEBLES PROPIOS CONSI GNADOS, EN LA PÁGINA ANTERIOR, EN ACTIVOS (DE REQUERIR MAYOR ESPACIO DETALLAR EN LA HOJA COMPLEMENTARIA DE ESTA SOLICITUD). ⟨abarca hasta col14⟩
Fila 3: col1 = DOMICILIO PROPIEDAD ("PV" SI ESTA PARA LA VENTA O "A" SI GENERA INGRES OS POR ALQUILER) ⟨abarca hasta col2⟩ | col3 = PV / A | col4 = TIPO DE PROPIEDAD ⟨abarca hasta col5⟩ | col6 = VALOR ACTUAL DE MERCADO | col7 = SALDO DE DEUDA CON GARANT ÍAS REALES ⟨abarca hasta col8⟩ | col9 = INGRESO BRUTO POR ALQUILER ⟨abarca hasta col10⟩ | col11 = CUOTAS HIPOTECA RIAS MENSUALES ⟨abarca hasta col12⟩ | col13 = SEGUROS, GASTOS, IMPUES- TOS, ETC. MENSU A- LES | col14 = INGRESO NETO POR ALQUILER
Fila 4: col6 = $ | col7 = $ ⟨abarca hasta col8⟩ | col9 = $ ⟨abarca hasta col10⟩ | col11 = $ ⟨abarca hasta col12⟩ | col13 = $ | col14 = $
Fila 5: col4 = TOTALES ⟨abarca hasta col5⟩ | col6 = $ | col7 = $ ⟨abarca hasta col8⟩ | col9 = $ ⟨abarca hasta col10⟩ | col11 = $ ⟨abarca hasta col12⟩ | col13 = $ | col14 = $
Fila 6: col1 = VI. INFORMACIÓN DE LA PROPIEDAD Y DESTINO DE LOS FONDOS ⟨abarca hasta col14⟩
Fila 7: col1 = DOMICILIO DE LA PROPIEDAD A SER HIPOTECADA (CALLE Y NÚMERO, PISO, DEPTO., LOCALIDAD, PROVINCIA, CÓDIGO POS- TAL) ⟨abarca hasta col12⟩ | col13 = TIPO DE PROPIEDAD ⟨abarca hasta col14⟩
Fila 8: col1 = DESCRIPCIÓN DE LA PROPIEDAD (DE SER NECESARIO USAR HOJA COMPLEMENTARIA) ⟨abarca hasta col12⟩ | col13 = AÑO CONSTRUCCIÓN ⟨abarca hasta col14⟩
Fila 9: col1 = ESPACIO CUBIERTO (METROS CUADRADOS) ⟨abarca hasta col6⟩ | col7 = TERRENO (METROS CUADRA- DOS) ⟨abarca hasta col10⟩ | col11 = VALOR (ESTIMADO) ⟨abarca hasta col14⟩
Fila 10: col1 = DESTINO DEL PRÉSTAMO (cid:31) ADQUISICIÓN MEJORAS (cid:31) REFINANCIACIÓN CONSTRUCCIÓN O TERMINACIÓN. OTROS (DETALLAR): ⟨abarca hasta col9⟩ | col10 = DESTINO DE LA PROPIEDAD (cid:31) RESIDENCIA PERMANENTE (cid:31) RESIDENCIA NO PERMANENTE ⟨abarca hasta col14⟩
Fila 11: col1 = COMPLETAR LA LÍNEA A CONTINUACIÓN SI EL DESTINO DE LOS FONDOS ES PARA MEJORAS ⟨abarca hasta col14⟩
Fila 12: col1 = AÑO DE COMPRA/ CONSTRUCCIÓN | col2 = PRECIO ADQUISICIÓN/ COSTO $ ⟨abarca hasta col6⟩ | col7 = SALDO HIPOTECAS EXISTENTES $ ⟨abarca hasta col11⟩ | col12 = VALOR ESTIMADO $ | col13 = COSTO ESTIMADO MEJORAS (ADJUNTAR PRESU- PUESTO) $ ⟨abarca hasta col14⟩
Fila 13: col1 = COMPLETAR LA LÍNEA A CONTINUACIÓN SI EL DESTINO DE LOS FONDOS ES PARA REFINANCIACIÓN ⟨abarca hasta col14⟩
Fila 14: col1 = AÑO DE COMPRA/ CONSTRUCCIÓN | col2 = PRECIO ADQUISI- CION/COSTO $ ⟨abarca hasta col4⟩ | col5 = MONTO HIPOTECAS EXISTENTES $ ⟨abarca hasta col7⟩ | col8 = SALDO CAPITAL ADEUDADO $ ⟨abarca hasta col10⟩ | col11 = PRÓXIMA CUOTA MEN- SUAL $ ⟨abarca hasta col12⟩ | col13 = MOTIVOS DE LA REFI- NANCIACIÓN ⟨abarca hasta col14⟩
Fila 15: col1 = TITULAR/ES DEL TÍTULO DE PROPIEDAD ⟨abarca hasta col14⟩
Fila 16: col1 = MODALIDAD DE FINANCIACIÓN: LA DIFERENCIA ENTRE EL PRECIO DE COMPRA Y EL MONTO SOLICITADO SERÁ FINANCIADO CON: PRÉSTAMO AHORRO OTROS ⟨abarca hasta col14⟩
Fila 17: col1 = SI ES PRÉSTAMO, COMPLETAR A CONTINUACIÓN: ⟨abarca hasta col14⟩
Fila 18: col1 = MONTO ⟨abarca hasta col2⟩ | col3 = ACREEDOR ⟨abarca hasta col7⟩ | col8 = PLAZO TOTAL EN MESES ⟨abarca hasta col12⟩ | col13 = CUOTA MENSUAL ⟨abarca hasta col14⟩
Fila 19: col1 = ORIGEN DE LOS FONDOS PROPIOS (DETALLAR): ⟨abarca hasta col14⟩
Fila 20: col1 = EL ABAJO FIRMANTE DECLARA QUE LOS FONDOS PROPIOS NO PROVIENEN DE ENDEUDAMIENTO ADICIONAL. ⟨abarca hasta col14⟩
Fila 21: col1 = FIRMA Y ACLARACIÓN FECHA: ⟨abarca hasta col14⟩
[FIN TABLA manori::tabla003]
VII. ACEPTACIÓN Y ACUERDO
EL/LOS ABAJO FIRMANTE/S ACEPTA/N Y ACUERDA/N QUE: 1) EL PRÉSTAMO OBJETO DE ESTA SOLICITUD SERÁ GARANTIZADO CON UNA HIPOTECA
EN PRIMER GRADO SOBRE LA PROPIEDAD DESCRIPTA EN LA PRESENTE; 2) NO SE LE DARÁ USO A LA PROPIEDAD PARA DESTINOS ILEGALES O
DISTINTOS A LOS MANIFESTADOS EN LA PRESENTE; 3) TODOS LOS DATOS Y DECLARACIONES CONSIGNADOS EN ESTA SOLICITUD SON HECHAS
CON EL SOLO PROPÓSITO DE CALIFICAR PARA EL PRÉSTAMO REQUERIDO; 4) EL USO QUE SE LE DARÁ A LA PROPIEDAD ES Y SERÁ EL QUE SE
INDICA EN ESTA SOLICITUD; 5) LA VERIFICACIÓN Y POSTERIOR REVERIFICACIÓN DE LOS DATOS CONTENIDOS EN ESTA SOLICITUD PUEDEN SER
REALIZADOS EN CUALQUIER MOMENTO POR EL ACREEDOR, SUS AGENTES, SUCESORES Y CESIONARIOS, EN FORMA DIRECTA O A TRAVÉS DE
AQUELLAS PERSONAS O ENTIDADES DESIGNADAS POR ESTAS. LA COPIA ORIGINAL DE ESTA SOLICITUD SERÁ RETENIDA POR EL ACREEDOR,
AUNQUE EL PRÉSTAMO SEA DENEGADO; 6) EL ACREEDOR, SUS AGENTES, SUCESORES Y CESIONARIOS FUNDAMENTAN SU DECISIÓN CREDITICIA
EN LA INFORMACIÓN AQUÍ CONTENIDA, POR LO CUAL ME/NOS COMPROMETO/EMOS A COMUNICAR CUALQUIER MODIFICACIÓN Y MANTENER
ACTUALIZADA LA MISMA; 7) EN EL SUPUESTO DE QUE CUOTAS QUE SURJAN DE LA SIGUIENTE SOLICITUD SE ENCONTRASEN EN MORA, EL ACREE-
DOR, SUS AGENTES, SUCESORES Y CESIONARIOS PODRÁN, EN ADICIÓN A TOMAR TODAS LAS MEDIDAS QUE CONSIDEREN PERTINENTES, SUMI-
NISTRAR MI/NUESTROS NOMBRE/S A LAS EMPRESAS DE INFORMACIÓN CREDITICIA; 8) EL ACREEDOR PODRÁ TRANSFERIR LA TITULARIDAD DEL
PRÉSTAMO (A SUS AGENTES, SUCESORES Y CESIONARIOS ) COMO ASÍ TAMBIÉN SU ADMINISTRACIÓN SIN NECESIDAD DE COMUNICACIÓN ALGUNA
AL DEUDOR, CODEUDOR/ES, O AL/LOS GARANTE/S; 9 ) EL ACREEDOR, SUS AGENTES, SUCESORES Y CESIONARIOS NO HAN INDUCIDO DE NINGUNA
MANERA AL DEUDOR, CODEUDOR/ES, O AL/LOS GARANTE/S A SOLICITAR EL PR ÉSTAMO OBJETO DE LA PRESENTE. TAMPOCO LOS HA/N ACONSE-
JADO SOBRE EL PRECIO DEL INMUEBLE, NI GARANTIZAN EL PRECIO DEL MISMO.
CERTIFICACIÓN: EL/LOS ABAJO FIRMANTE/S CERTIFICA/N CON CARÁCTER DE DECLARACIÓN JURADA QUE LOS DATOS CONSIGNADOS EN LA
PRESENTE SOLICITUD SON CORRECTOS Y EXACTOS A LA FECHA QUE CONSTA AL PIE DE LA PRESENTE. ASIMISMO, ME/NOS HAGO/HACEMOS
RESPONSABLE/S LEGALMENTE FRENTE A CUALQUIER PERSONA PO R CUALQUIER DAÑO QUE PUDIERA CAUSAR LA INFORMACIÓN QUE INTENCIO-
NAL O NEGLIGENTEMENTE SE HAYA CONSIGNADO ERRÓNEAMENTE.
[TABLA manori::tabla004 | página 37 | e0_tablas | posicional]
Fila 1: col1 = VIII. INFORMACIÓN DE LA ENTIDAD ⟨abarca hasta col3⟩
Fila 2: col1 = CÓDIGO DE LA ENTIDAD | col2 = CÓDIGO DE LA SUCURSAL | col3 = OFICIAL DE CRÉDITO
Fila 3: col3 = ( CÓDIGO O NOMBRE )
[FIN TABLA manori::tabla004]
FIRMA Y ACLARACIÓN FECHA:
HOJA COMPLEMENTARIA /SOLICITUD CRÉDITO HIPOTECARIO
UTILIZAR ESTA HOJA COMPLEMENTARIA SI NECESITA ESPACIO ADICIONAL PARA COMPLEMENTAR LA SOLICITUD DE CRÉDITO HIPOTECARIO.
FIRMA Y ACLARACIÓN FECHA:
```
