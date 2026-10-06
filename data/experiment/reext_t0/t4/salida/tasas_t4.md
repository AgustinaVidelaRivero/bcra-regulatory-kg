# Tasas de T4 de U-REEXT-T0 (segundo tramo), sobre la marca adjudicada

Wilson al 95 % (z = 1,959964); fracciones crudas, sin porcentajes. Adjudicación: `adjudicacion_autora.json`.

## Punto 1, cola humana

- Unidades con error: **12/30 [0,246; 0,577]**. Regla del 25 %: el límite superior 0,5768 supera 0,25: la regla se dispara. Salidas de la enmienda: re-procesar las 74 unidades de la cola humana de la tanda 0 o sacar las 74 unidades del grafo evaluado de la tanda 0. Elección: PENDIENTE de la autora.

  - `lingob::7.1.7`: e1 Obligacion «deben definir la política…»: el texto dice «Es deseable incluir… la siguiente información» (recomendación de divulgar, no deber de definir la política)
  - `ctacte::1.5.1.3`: aplica_a de e1 hacia Sujeto_banco (mención «la entidad»): la obligación es del cuentacorrentista (encabezado 1.5.1); la entidad solo estima la necesidad
  - `ext::10.4.3.5`: e2 Obligacion «debe dar acceso…»: el texto dice «podrá dar acceso… en la medida que verifique…» (facultad)
  - `ext::3.18.1.1`: e2 Restriccion «Se prohíbe… sin la conformidad previa» y su prohibe hacia e1: el texto habilita ese pago sin la conformidad (3.18.1: «podrá acceder… para realizar»)
  - `ext::5.4.1`: aplica_a de e2 hacia Sujeto_rol_entidad_autorizada_exterior (mención «La entidad»): la obligación de presentar el documento es del cliente
  - `ext::8.5.13.2`: ob1 Obligacion para «La entidad podrá considerar cumplimentado…»: es una facultad
  - `ctacte::1.5.1.12`: aplica_a de e1 hacia Sujeto_banco (mención «el cuentacorrentista», no verificada): la obligación es del cuentacorrentista (1.5.1)
  - `ext::7.1.1.2`: aplica_a de e2 hacia Sujeto_rol_entidad_autorizada_exterior (mención «las entidades», no verificada): la obligación de ingresar y liquidar es del exportador (7.1.1)
  - `pagjub::2.7.2`: e1 --prohibe--> e2 «Presentación de soportes con archivos»: el texto no prohíbe acompañar los soportes; rechaza la presentación que no los acompaña
  - `lingob::7.1.8`: e1 Obligacion «Incluir en los sitios públicos… las políticas…» sin la marca de recomendación: el texto dice «Es deseable incluir»
  - `pagjub::2.8.1.2`: aplica_a de e2 hacia Sujeto_rol_alcance_pagjub (mención «la entidad participante»): la obligación de acreditar es del BCRA («El BCRA… procederá a»); la entidad es la beneficiaria
  - `cap::10.3.3.1`: e3 (igual o preferente, del inciso i) --condicion_de--> e2 (la regla de la emisión calificada), y e4 (no podrá usarse la calificación) --prohibe--> e1 (la inversión en la emisión calificada): lo prohibido es usar la calificación, no invertir

- Omisiones, aparte (6 unidades): `cap::6.2.2.4` (filas y columna de la tabla); `ext::3.9::intro` («sin la conformidad previa del BCRA»); `ext::10.4.3.3` (la facultad «podrá dar acceso»); `ext::4.7.1` (la relación de la Condicion con su norma); `pro::4.2.1.4` (la facultad «podrá informar»); `ext::9.3.7` (la facultad «La entidad podrá emitir» (queda como Operacion, sin Potestad))

## Punto 5, las 27 de P4b

| grupo | cumple |
|---|---|
| a_transicion | 0/1 [0,000; 0,793] |
| a | 1/3 [0,061; 0,792] |
| c | 1/4 [0,046; 0,699] |
| d | 3/4 [0,301; 0,954] |
| e | 3/4 [0,301; 0,954] |
| b1_items | 0/3 [0,000; 0,561] |
| b2_items | 0/3 [0,000; 0,561] |
| b_encabezados | 0/2 [0,000; 0,658] |
| ejemplo | 2/2 [0,342; 1,000] |
| f | 1/1 [0,206; 1,000] |
| total | 11/27 [0,245; 0,593] |

Variación contra P5: 4 idénticas a una de P5 y 23 difieren; la marca cambia en 3 contra a y 5 contra b. `ext::10.3.6`: punto 5 «cumple» (regla de P4b sobre la respuesta de E1, marca de P5); punto 7 «cumple» sobre la extracción final; con la regla del punto 7, la respuesta de E1 no cumpliría (decisión 1: se declara, no se reconcilia).

## Punto 6, listas

| tipo y rol | cumple |
|---|---|
| b1_encabezados | 1/3 [0,061; 0,792] |
| b1_items | 9/21 [0,245; 0,634] |
| b2_encabezados | 5/7 [0,359; 0,918] |
| b2_items | 0/32 [0,000; 0,107] |
| aparte_b1_encabezados | 0/1 [0,000; 0,793] |
| aparte_b1_items | 0/5 [0,000; 0,434] |

| lista | tipo | cumple |
|---|---|---|
| cla::5.1.1 | b1 | 2/3 |
| ext::3.5.4 | b2 | 1/4 |
| ext::2.6.1 | b2 | 1/4 |
| ext::7.8.4 | b2 | 1/4 |
| ext::2.7 | b2 | 1/5 |
| ctacte::3.2 (aparte) | b1 | 0/6 |
| ext::3.5.3 | b2 | 0/6 |
| ext::3.13.1 | b1 | 4/14 |
| ext::3.6.1 | b1 | 4/7 |
| ext::3.6.4 | b2 | 0/8 |
| ext::10.11 | b2 | 1/8 |

Encabezados b1 con la forma de b2: ext::3.13.1 y ext::3.6.1 están selladas como b1 y sus encabezados tienen la forma de b2 (la norma y una excepción general); lectura mía con el criterio de b2, sin adjudicar; la cifra sellada no cambia; los ítems no se releyeron con el criterio de b2. Con el criterio de b2: `ext::3.13.1::intro` cumple (la Obligacion e3 de la conformidad previa y la Excepcion e4, unidas por exceptua_obligacion); `ext::3.6.1::intro` cumple (la Restriccion e1 de la prohibición y la Excepcion e2, unidas por exceptua). b1 encabezados con esos dos leídos como b2: 3/3 [0,439; 1,000]; si las dos listas fueran b2: b1 encabezados 1/1 [0,206; 1,000] y b2 encabezados 7/9 [0,453; 0,937].

## Punto 7, grupo c

- Criterio sellado: cumple **1/30 [0,006; 0,167]**. Etiquetas adjudicadas: {'en_norma': 26, 'sin_relacion': 7, 'umbral_en_norma': 6, 'fusion': 5, 'omitido': 3, 'incoherente': 2}.
- Por supuesto (137 supuestos de la fase A): condicion_con_relacion 43/137 [0,242; 0,396]; dentro_de_norma 76/137 [0,471; 0,635]; fusionado 7/137 [0,025; 0,102]; omitido 3/137 [0,007; 0,062]; sin_relacion 8/137 [0,030; 0,111]. Sin relación, por subtipo: {'norma_en_heredado': 4, 'norma_presente': 3, 'norma_no_emitida': 1}.

| documento | unidades | supuestos | condicion_con_relacion | dentro_de_norma | fusionado | omitido | sin_relacion |
|---|---|---|---|---|---|---|---|
| cap | 7 | 36 | 7/36 | 25/36 | 3/36 | 0/36 | 1/36 |
| cla | 7 | 32 | 13/32 | 13/32 | 2/32 | 0/32 | 4/32 |
| ext | 9 | 35 | 17/35 | 14/35 | 2/35 | 2/35 | 0/35 |
| polcre | 2 | 9 | 3/9 | 4/9 | 0/9 | 0/9 | 2/9 |
| pro | 2 | 14 | 0/14 | 13/14 | 0/14 | 1/14 | 0/14 |
| ric | 3 | 11 | 3/11 | 7/11 | 0/11 | 0/11 | 1/11 |
| total | 30 | 137 | 43/137 | 76/137 | 7/137 | 3/137 | 8/137 |

Supuestos, uno por uno:

- `ext::10.5.5.2` «i) control de cambios»: condicion_con_relacion — e2 Condicion → e1 Operacion
- `ext::10.5.5.2` «ii) insolvencia (con a y b)»: condicion_con_relacion — e3 Condicion → e1
- `ext::10.5.5.2` «a hasta USD 100.000»: condicion_con_relacion — e4 Condicion con el umbral → e1
- `ext::10.5.5.2` «b acciones judiciales»: condicion_con_relacion — e5 Condicion → e1
- `ext::10.5.5.2` «percepción en moneda extranjera»: dentro_de_norma — dentro de la Obligacion e7
- `ext::10.4.4` «emitidas desde el 13/12/23»: condicion_con_relacion — e2 Condicion con el umbral → e3 Obligacion
- `ext::10.4.4` «desde el 14/04/25»: condicion_con_relacion — e6 Condicion con el umbral → e7 Potestad
- `ext::10.4.4` «con pagos a la vista»: dentro_de_norma — dentro de la Potestad e7
- `ext::10.4.4` «sin oficialización a 90 días»: condicion_con_relacion — e10 Condicion con el umbral → e11 Obligacion
- `polcre::7.1.2` «financiaciones de más de $ 30.000 millones»: sin_relacion (norma_en_heredado) — c1 Condicion con el umbral, sin relación; la norma («Se encuentran comprendidos… los clientes… que reúnan concurrentemente las siguientes condiciones») está en el texto heredado
- `polcre::7.1.2` «pases o cauciones en 90 días»: sin_relacion (norma_en_heredado) — c2 Condicion con el umbral, sin relación; ídem
- `polcre::7.1.2` «declaración jurada contra la Central de deudores»: condicion_con_relacion — c3 Condicion → o1 Obligacion (un solo supuesto, por la adjudicación)
- `polcre::7.1.2` «MiPyME»: condicion_con_relacion — e1 Excepcion —exceptua_obligacion→ o1
- `pro::2.3.5.1` «conceptos i) a vii)» i): dentro_de_norma — cada concepto como Restriccion (e2 a e8) hacia la Operacion, no como Condicion del reintegro
- `pro::2.3.5.1` «conceptos i) a vii)» ii): dentro_de_norma — cada concepto como Restriccion (e2 a e8) hacia la Operacion, no como Condicion del reintegro
- `pro::2.3.5.1` «conceptos i) a vii)» iii): dentro_de_norma — cada concepto como Restriccion (e2 a e8) hacia la Operacion, no como Condicion del reintegro
- `pro::2.3.5.1` «conceptos i) a vii)» iv): dentro_de_norma — cada concepto como Restriccion (e2 a e8) hacia la Operacion, no como Condicion del reintegro
- `pro::2.3.5.1` «conceptos i) a vii)» v): dentro_de_norma — cada concepto como Restriccion (e2 a e8) hacia la Operacion, no como Condicion del reintegro
- `pro::2.3.5.1` «conceptos i) a vii)» vi): dentro_de_norma — cada concepto como Restriccion (e2 a e8) hacia la Operacion, no como Condicion del reintegro
- `pro::2.3.5.1` «conceptos i) a vii)» vii): dentro_de_norma — cada concepto como Restriccion (e2 a e8) hacia la Operacion, no como Condicion del reintegro
- `pro::2.3.5.1` «plazo por reclamo»: dentro_de_norma — dentro de la Obligacion e9
- `pro::2.3.5.1` «por constatación»: dentro_de_norma — dentro de la Obligacion e10
- `pro::2.3.5.1` «tasa no disponible»: omitido — sin extraer
- `pro::2.3.5.1` «cuenta a la vista»: dentro_de_norma — dentro de la Obligacion e13
- `pro::2.3.5.1` «si no fuera posible»: dentro_de_norma — dentro de la Obligacion e14
- `cap::6.2.3.5` «instrumentos idénticos»: condicion_con_relacion — e2 Condicion → e1 Operacion
- `cap::6.2.3.5` «futuro con gama de instrumentos»: dentro_de_norma — dentro de la Restriccion e4
- `cap::6.2.3.5` «a) futuros a 7 días»: dentro_de_norma — dentro de la Restriccion e9, con el umbral
- `cap::6.2.3.5` «b) swaps y FRAs»: dentro_de_norma — dentro de la Restriccion e10
- `cap::6.2.3.5` «c) tramos de fechas»: dentro_de_norma — dentro de las Restriccion e11 a e13
- `cap::6.2.3.5` «futuros sobre títulos»: condicion_con_relacion — e15 Excepcion —exceptua→ e14 Restriccion
- `ext::10.3.6` «emitidas desde el 13/12/23 (más 15 días)»: condicion_con_relacion — e4 Condicion con el umbral → e5 Obligacion
- `ext::10.3.6` «desde el 14/04/25»: condicion_con_relacion — e8 Condicion con el umbral → e9 Obligacion
- `ext::10.3.6` «con pagos a la vista»: condicion_con_relacion — e10 Condicion → e9
- `cla::6.5.3.10` «sin cancelar el 15 %»: sin_relacion (norma_en_heredado) — c2 Condicion con el umbral, hacia o1 (el cómputo de las garantías) y no hacia la norma que condiciona, la clasificación «Con problemas», que está en el texto heredado
- `cla::6.5.3.10` «acuerdo alcanzado en alto riesgo o irrecuperable»: sin_relacion (norma_en_heredado) — c3 Condicion hacia o1; ídem
- `cla::6.5.3.10` «acuerdos de más de 2,5 veces el importe de referencia»: condicion_con_relacion — c4 Condicion con el umbral → p1 Potestad
- `ext::7.9.4` «endeudamientos con cuentas de garantía»: dentro_de_norma — dentro de la Obligacion e3
- `ext::7.9.4` «proyectos del 7.9.2»: condicion_con_relacion — e5 Condicion → e6 Obligacion
- `ext::7.9.4` «proyecto sin aprobación de la Ley 26.360»: dentro_de_norma — dentro de la Obligacion e8
- `cla::7.2.2.1` «cancelado el 10 %»: sin_relacion (norma_presente) — e2 Condicion con el umbral, sin relación hacia la Definicion e1 de la categoría
- `cla::7.2.2.1` «pago de 1 cuota»: condicion_con_relacion — e4 Condicion con el umbral → e3 Operacion
- `cla::7.2.2.1` «pago único o irregular con 5 %»: condicion_con_relacion — e5 Condicion con el umbral → e3
- `cla::7.2.2.1` «financiación adicional sin cancelar»: dentro_de_norma — dentro de la Restriccion e6
- `cla::7.2.2.1` «atrasos de más de 31 días»: condicion_con_relacion — e7 Condicion con el umbral → e8 Operacion
- `cap::3.1.14.1` «refinanciación distribuida»: dentro_de_norma — dentro de la Obligacion e3
- `cap::3.1.14.1` «valores residuales no significativos»: dentro_de_norma — dentro de la Obligacion e3
- `cap::3.1.14.1` «minoristas 5 años»: fusionado — e8 Condicion junta el supuesto y la norma (5 años), sin relación
- `cap::3.1.14.1` «resto 7»: fusionado — e9 Condicion junta el supuesto y la norma (7 años), sin relación
- `cap::3.1.14.1` «salvo el período de 2 años»: dentro_de_norma — dentro de la Obligacion e11
- `cap::3.1.14.1` «condiciones a) a d)» a): dentro_de_norma — cada condición como Obligacion (e11 a e14)
- `cap::3.1.14.1` «condiciones a) a d)» b): dentro_de_norma — cada condición como Obligacion (e11 a e14)
- `cap::3.1.14.1` «condiciones a) a d)» c): dentro_de_norma — cada condición como Obligacion (e11 a e14)
- `cap::3.1.14.1` «condiciones a) a d)» d): dentro_de_norma — cada condición como Obligacion (e11 a e14)
- `cla::7.2.4` «concurso con 20 % o más»: dentro_de_norma — dentro de la Definicion e2
- `cla::7.2.4` «entre 5 % y 20 % con 90 días»: dentro_de_norma — dentro de la Definicion e2
- `cla::7.2.4` «levantamiento del pedido»: dentro_de_norma — dentro de la Potestad e3
- `cla::7.2.4` «refinanciados»: dentro_de_norma — dentro de la Operacion e5
- `cla::7.2.4` «más de 540 días»: dentro_de_norma — dentro de la Operacion e6
- `cla::7.2.4` «atrasos de más de 31 días»: dentro_de_norma — dentro de la Operacion e9
- `ext::14.5.7` «i) a iii) en la medida que» i): condicion_con_relacion — e2, e6 y e9 Condicion → e1 Operacion
- `ext::14.5.7` «i) a iii) en la medida que» ii): condicion_con_relacion — e2, e6 y e9 Condicion → e1 Operacion
- `ext::14.5.7` «i) a iii) en la medida que» iii): condicion_con_relacion — e2, e6 y e9 Condicion → e1 Operacion
- `ext::14.5.7` «al menos 90 % del FOB»: condicion_con_relacion — e3 Condicion con el umbral → e1
- `ext::14.5.7` «en caso de no disponer la documentación»: dentro_de_norma — dentro de la Obligacion e7
- `ext::14.5.7` «VPU con cobros de exportaciones»: dentro_de_norma — dentro de la Obligacion e12
- `cla::6.5.5.9` «deuda de más del 2,5 % de la RPC o del importe de referencia»: dentro_de_norma — como Restriccion e2 («no podrá exceder»), con el umbral
- `cla::6.5.5.9` «excepción de concurso hasta 540 días»: condicion_con_relacion — e4 Excepcion con el umbral —exceptua_obligacion→ e3
- `cla::6.5.5.9` «siempre que haya informe»: condicion_con_relacion — e5 Condicion → e4 Excepcion
- `cla::6.5.5.9` «primera declaración»: fusionado — e6 Condicion junta la primera declaración y las actualizaciones
- `cla::6.5.5.9` «actualizaciones»: fusionado — ídem, e6
- `cla::7.2.3` «sin cancelar el 10 %»: sin_relacion (norma_presente) — e2 Condicion con el umbral, sin relación hacia la Definicion e1 de la categoría
- `cla::7.2.3` «pago de 2 cuotas»: condicion_con_relacion — e4 Condicion con los umbrales → e6 Potestad
- `cla::7.2.3` «pago único o irregular con 5 %»: condicion_con_relacion — e5 Condicion con el umbral → e6
- `cla::7.2.3` «financiación adicional sin cancelar»: dentro_de_norma — dentro de la Restriccion e8
- `cla::7.2.3` «atrasos de más de 31 días»: dentro_de_norma — dentro de la Obligacion e9, con el umbral
- `cap::2.1` «en tanto no se comunique la calificación»: fusionado — e4 Condicion lleva el supuesto y la consecuencia (k = 1,03), sin relación
- `cap::2.1` «el cronograma opera desde que las obras se usan económicamente»: dentro_de_norma — dentro de las Obligacion e19 a e21
- `pro::3.1.3` «presentación por teléfono o Internet»: dentro_de_norma — dentro de la Obligacion e7
- `pro::3.1.3` «presentante que no recibe el número automáticamente»: dentro_de_norma — dentro de la Obligacion e8
- `cap::7.3.2` «grupo B (17 %)»: dentro_de_norma — dentro de la Restriccion e1
- `cap::7.3.2` «calificación 1, 2 o 3 (11 %)»: condicion_con_relacion — e3 Condicion → e2 Restriccion
- `cap::7.3.2` «calificación 1 o 2 (7 %)»: condicion_con_relacion — e5 Condicion → e4 Restriccion
- `ext::4.1.3.2` «emisoras no financieras»: omitido — sin extraer
- `ext::4.1.3.2` «pago en día inhábil»: fusionado — e3 Condicion junta la regla del tipo de cambio, el pago en pesos y el día inhábil
- `cap::3.1.11.3` «i) a iii) según D, A y KA» i): dentro_de_norma — dentro de las Restriccion e2 a e4
- `cap::3.1.11.3` «i) a iii) según D, A y KA» ii): dentro_de_norma — dentro de las Restriccion e2 a e4
- `cap::3.1.11.3` «i) a iii) según D, A y KA» iii): dentro_de_norma — dentro de las Restriccion e2 a e4
- `cap::3.1.11.3` «si no existiera la posición pari passu»: dentro_de_norma — dentro de la Operacion e5
- `cap::3.1.11.3` «mínimos por STC»: dentro_de_norma — dentro de las Restriccion e6 a e8
- `cap::3.1.11.3` «look-through menor que el mínimo»: condicion_con_relacion — e10 Excepcion —exceptua→ e6, e7 y e8
- `ext::3.16.3.6` «garantía desde el vencimiento»: dentro_de_norma — dentro de la Obligacion e3
- `ext::3.16.3.6` «fondos usados en 10 días»: dentro_de_norma — dentro de la Obligacion e4, con el umbral
- `ext::3.16.3.6` «repatriación a 1 año»: condicion_con_relacion — e6 Condicion con los umbrales → e4 Obligacion
- `ext::3.16.3.6` «BOPREAL hasta el monto suscripto»: dentro_de_norma — dentro de la Obligacion e11
- `ext::3.16.3.6` «valor de mercado que no supere la diferencia»: dentro_de_norma — dentro de la Obligacion e12
- `cap::6.3.2.2` «arbitrajes del a) (dos guiones)» primer guion: dentro_de_norma — dentro de las Excepcion e6 y e7
- `cap::6.3.2.2` «arbitrajes del a) (dos guiones)» segundo guion: dentro_de_norma — dentro de las Excepcion e6 y e7
- `cap::6.3.2.2` «b) canasta de al menos 90 %»: condicion_con_relacion — e11 Condicion con el umbral → e9 Restriccion
- `cap::6.3.2.2` «c) sólo si se tienen en cuenta los costos»: condicion_con_relacion — e14 Condicion → e13 Potestad
- `ext::4.1.3.1` «emisor entidad financiera»: omitido — solo en una omisión meta_normativo
- `ext::4.1.3.1` «pago en día inhábil»: dentro_de_norma — dentro de la Restriccion e2
- `ext::4.1.3.1` «débito automático pactado»: condicion_con_relacion — e3 Condicion → e4 Restriccion
- `ric::9.1.3` «obligación del plan de regularización»: condicion_con_relacion — c1 Condicion → r1 Restriccion
- `ric::9.1.3` «incrementos de más del 5 %»: condicion_con_relacion — c2 Condicion con el umbral → r1
- `ric::9.1.3` «base consolidada»: sin_relacion (norma_no_emitida) — c3 Condicion sin relación: la norma que condiciona (la asimilación de las partidas) no se emite y queda en una omisión meta_normativo
- `ric::9.1.3` «mientras persista»: condicion_con_relacion — c4 Condicion → r1
- `ext::8.4.2` «exportación de varios productos»: dentro_de_norma — dentro de la Operacion e2
- `ext::8.4.2` «fecha no hábil»: fusionado — e4 Condicion lleva el supuesto y la consecuencia, sin relación
- `ext::8.4.2` «ampliación del plazo»: dentro_de_norma — dentro de la Operacion e5
- `ext::8.4.2` «reducción del plazo»: dentro_de_norma — dentro de la Restriccion e6
- `ric::6.1.2` «código 22600000 (tres «cuando»)» opciones de exclusión: dentro_de_norma — dentro de la Operacion e12
- `ric::6.1.2` «código 22600000 (tres «cuando»)» respaldo implícito: dentro_de_norma — dentro de la Operacion e12
- `ric::6.1.2` «código 22600000 (tres «cuando»)» cancelación anticipada: dentro_de_norma — dentro de la Operacion e12
- `ric::6.1.2` «código 22700000»: dentro_de_norma — dentro de la Operacion e14
- `ric::6.1.2` «código 21800000»: dentro_de_norma — dentro de la Operacion e7
- `cla::6.5.4.5` «bienes en pago»: dentro_de_norma — dentro de la Restriccion e2
- `cla::6.5.4.5` «recategorización siempre que…»: condicion_con_relacion — e4 Condicion → e3 Potestad
- `cla::6.5.4.5` «pago del 10 %»: dentro_de_norma — dentro de la Obligacion e5, con el umbral
- `cla::6.5.4.5` «financiación adicional sin cancelar»: condicion_con_relacion — e8 Condicion → e7 Obligacion
- `cla::6.5.4.5` «salvo otras pautas»: condicion_con_relacion — e9 Excepcion —exceptua_obligacion→ e7
- `cap::3.1.11.2` «estructura con SPE»: dentro_de_norma — dentro de la Obligacion e3
- `cap::3.1.11.2` «si puede demostrar»: sin_relacion (norma_presente) — e4 Excepcion sin relación hacia e3 (la unidad no tiene ninguna relación)
- `cap::3.1.11.2` «sintéticas con fondos aportados»: dentro_de_norma — dentro de la Obligacion e5
- `cap::3.1.11.2` «previsión específica»: dentro_de_norma — dentro de la Obligacion e7
- `cap::3.1.11.2` «desconocida para 5 % o menos»: dentro_de_norma — dentro de la Obligacion e14, con el umbral
- `cap::3.1.11.2` «para más del 5 %»: dentro_de_norma — dentro de la Restriccion e15, con el umbral
- `ric::4.5.2` ««C» si es compra a término»: dentro_de_norma — dentro de la Obligacion e7
- `ric::4.5.2` ««V» si es venta»: dentro_de_norma — dentro de la Obligacion e7
- `polcre::7.1::cierre` «reúne 7.1.1»: condicion_con_relacion — e1 Condicion → e4 Potestad
- `polcre::7.1::cierre` «no supera $ 30.000 millones»: dentro_de_norma — como Restriccion e2, con el umbral
- `polcre::7.1::cierre` «sin pases»: dentro_de_norma — como Restriccion e3, con el umbral
- `polcre::7.1::cierre` «desembolsos que no superen el importe»: dentro_de_norma — dentro de la Potestad e4
- `polcre::7.1::cierre` «conjuntos económicos»: dentro_de_norma — como Definicion e6
- `cla::6.5.5.2` «sin cancelación efectiva previa»: dentro_de_norma — dentro de la Restriccion e5
- `cla::6.5.5.2` «pago del 15 %»: condicion_con_relacion — e7 Condicion con los umbrales → e6 Potestad
- `cla::6.5.5.2` «financiación adicional sin cancelar»: condicion_con_relacion — e10 Condicion → e8 Restriccion

## Punto 8, omisiones meta_normativo

- **sin marca** (N = 733): normativas 19/30 [0,455; 0,781] con remisiones y 14/30 [0,302; 0,639] sin; habilitantes 0/30 [0,000; 0,114]; tramo heredado 4 (3 normativas). Tramo propio: normativas 16/30 [0,361; 0,698] con remisiones y 11/30 [0,219; 0,545] sin; estimación al universo 390,9 [264,9; 511,4] con remisiones y 268,8 [160,3; 399,4] sin.
- **con marca** (N = 404): normativas 27/30 [0,744; 0,965] con remisiones y 27/30 [0,744; 0,965] sin; habilitantes 3/30 [0,035; 0,256]; tramo heredado 18 (17 normativas). Tramo propio: normativas 10/30 [0,192; 0,512] con remisiones y 10/30 [0,192; 0,512] sin; estimación al universo 134,7 [77,7; 206,9] con remisiones y 134,7 [77,7; 206,9] sin.

Se le escapan al contador: la cifra del grupo sin marca, con el tramo propio: 268,8 [160,3; 399,4] sin remisiones y 390,9 [264,9; 511,4] con remisiones, de 733. Supuesto: muestra aleatoria simple de 30 dentro de cada grupo; estimación = N × fracción, intervalo = N × Wilson.
