# U-CONF-MATRIZ, C3: lista para la revisión de la autora

Mandato §5: las incorrectas, las no decidibles y 5 correctas por par, sorteadas con la semilla de revisión del par. Cada entrada lleva la marca y la nota de C2 y la ficha de C1. La autora adjudica las que no comparta (C4).

## → Operacion

Cifras de C2: 29 correctas, 1 incorrectas, 0 no decidibles; Wilson 95 % [0.8333, 0.9941].

### Incorrectas: 1

#### F15 — incorrecta

- Nota de C2: 10.4.2.4: «En el caso de que un mismo pago anticipado incluya bienes de capital y bienes que no lo son, la operación se regirá por el plazo del tipo de bien que represente una mayor proporción». Es una regla que fija qué plazo rige para el compromiso de la declaración jurada (270 o 90 días), no un antecedente del acceso: el antecedente del acceso es contar con la declaración jurada (10.4.2, «en la medida que verifique previamente que se cumplen la totalidad de los siguientes requisitos»). El nodo Condicion tiene la forma de supuesto («cuando…»), pero su consecuente es el plazo, no el acceso.
- Origen: Condicion — «Plazo según proporción — bienes mixtos» (`Condicion_plazo_segun_proporcion_bienes_mixtos__cuando_un_pago_anticipado_incluye_tanto_bi_493546`)
  - descripción (salida del extractor): Cuando un pago anticipado incluye tanto bienes de capital como otros bienes, se aplica el plazo del tipo de bien que represente mayor proporción del valor total abonado
  - tramo de E1 (salida del extractor): 'En el caso de que un mismo pago anticipado incluya bienes de capital y bienes que no lo son, la operación se regirá por el plazo del tipo de bien que represente una mayor proporción del valor total abonado'
- Destino: Operacion — «Acceso al mercado de cambios para pago anticipado» (`Operacion_acceso_al_mercado_de_cambios_para_pago_anticipado__ext_10_4_2_e7eb03`)
  - descripción (salida del extractor): Acceso al mercado de cambios para el pago al exterior de importaciones con registro de ingreso aduanero pendiente
  - tramo de E1 (salida del extractor): 'dar acceso al mercado de cambios para el pago al exterior'
- Unidad `ext::10.4.2.4` (ext, punto 10.4.2.4), páginas [139, 140]; PDF `data/experiment/subset/TO_exterior_cambios_actual.pdf`; render `c1/paginas/ext_p139.png`, `c1/paginas/ext_p140.png`
- Texto heredado: [encabezado S10] Sección 10. Pagos de importaciones y otras compras de bienes en el exterior. / [encabezado 10.4] 10.4. Pagos de importaciones de bienes con registro de ingreso aduanero pendiente. / [encabezado 10.4.2] 10.4.2. Requisitos de acceso para el pago anticipado de importaciones. / [intro 10.4.2] La entidad podrá dar acceso al mercado de cambios para el pago al exterior en la medida que verifique previamente que se cumplen la totalidad de los siguientes requisitos:
- Texto propio:

```text
10.4.2.4. Cuenta con la declaración jurada del cliente de que se compromete a
demostrar el registro del ingreso aduanero de los bienes dentro del plazo
que corresponda según tipo de bien a importar, o en su defecto, proceder
en ese plazo a la liquidación en el mercado de cambios de los fondos en
moneda extranjera asociados a la devolución del pago efectuado.
En el caso de pagos anticipados de bienes de capital, el plazo para
demostrar el registro de ingreso aduanero será de 270 (doscientos setenta)
días corridos a partir de la fecha de acceso al mercado de cambios. A tal
efecto, se deberán considerar las posiciones arancelarias clasificadas
como BK (Bien de Capital) en la Nomenclatura Común del MERCOSUR
(Decreto 690/02 y complementarias).
Para el resto de los bienes, el plazo será de 90 (noventa) días corridos a
partir de la fecha de acceso al mercado de cambios.
En el caso de que un mismo pago anticipado incluya bienes de capital y
bienes que no lo son, la operación se regirá por el plazo del tipo de bien
que represente una mayor proporción del valor total abonado.
Si la nacionalización de los bienes requiere un plazo mayor y el pago
anticipado se concreta en su totalidad en el marco de lo previsto en los
puntos 10.10.2.3. a 10.10.2.6. o 10.10.2.14.ii), la entidad podrá considerar
que el referido plazo se extiende hasta la fecha que surge de sumar 15
(quince) días corridos a la fecha estimada de arribo de los bienes. La
entidad deberá reportar la extensión otorgada en el SEPAIMPO.
Si el proveedor del exterior es una contraparte vinculada con el importador
o se necesiten plazos mayores para la oficialización del despacho de
importación, se requerirá contar con la previa conformidad del BCRA antes
del acceso al mercado de cambios.
Los pedidos al BCRA deben ser canalizados por una entidad autorizada a
realizar este tipo de pago.
```

### No decidibles: 0

### Correctas sorteadas (semilla 3317428300167781795): 5

#### F51 — correcta

- Nota de C2: 2.1.4: «Financiaciones a productores de bienes para ser exportados […], siempre que cuenten con avales o garantías totales en moneda extranjera de dichos terceros y/o contratos de venta en firme en moneda extranjera y/o en bienes exportables». Una de las alternativas («y/o») de la condición del destino admitido.
- Origen: Condicion — «Contratos de venta en firme en moneda extranjera» (`Condicion_contratos_de_venta_en_firme_en_moneda_extranjera__que_cuenten_con_contratos_de_v_2d5333`)
  - descripción (salida del extractor): Que cuenten con contratos de venta en firme en moneda extranjera
  - tramo de E1 (salida del extractor): 'y/o contratos de venta en firme en moneda extranjera'
- Destino: Operacion — «Financiación a productores de bienes exportables» (`Operacion_financiacion_a_productores_de_bienes_exportables__polcre_2_1_4_8d9c1f`)
  - descripción (salida del extractor): Financiación a productores de bienes para ser exportados, ya sea en el mismo estado o como parte integrante de otros bienes, realizada por terceros adquirentes de ellos
  - tramo de E1 (salida del extractor): 'Financiaciones a productores de bienes para ser exportados, ya sea en el mismo estado o como parte integrante de otros bienes, por terceros adquirentes de ellos'
- Unidad `polcre::2.1.4` (polcre, punto 2.1.4), páginas [7]; PDF `data/experiment/escalado_prep/pdfs/polcre.pdf`; render `c1/paginas/polcre_p6.png`, `c1/paginas/polcre_p7.png`, `c1/paginas/polcre_p8.png`, `c1/paginas/polcre_p9.png`
- Texto heredado: [encabezado S2] Sección 2. Aplicación de la capacidad de préstamo de depósitos en moneda extranjera. / [encabezado 2.1] 2.1. Destinos. / [intro 2.1] La capacidad de préstamo de los depósitos en moneda extranjera deberá aplicarse, en la co- rrespondiente moneda de captación, en forma indistinta, a los siguientes destinos: / [cierre 2.1] La aplicación de la capacidad de préstamo de depósitos en moneda extranjera a los destinos vinculados a operaciones de importación (previstos en los puntos 2.1.6., 2.1.7. y la parte atri- buible a éstos por aplicación de los puntos 2.1.8. y 2.1.9.), no podrá superar el valor que resulte de la siguiente expresión: C max (F / C ; 0,05) / [cierre 2.1] x / [cierre 2.1] t base base / [cierre 2.1] Siendo: C: capacidad de préstamo del mes al que corresponda. / [cierre 2.1] t / [cierre 2.1] F : financiación de importaciones comprendidas, correspondientes al trimestre agos- base / [cierre 2.1] to/octubre de 2008. / [cierre 2.1] C : capacidad de préstamo que corresponda al trimestre agosto/octubre de 2008. / [cierre 2.1] base / [cierre 2.1] Las financiaciones y capacidad de préstamo deberán ser computadas de acuerdo con lo esta- blecido en el punto 2.5.
- Texto propio:

```text
2.1.4. Financiaciones a productores de bienes para ser exportados, ya sea en el mismo estado
o como parte integrante de otros bienes, por terceros adquirentes de ellos, siempre que
cuenten con avales o garantías totales en moneda extranjera de dichos terceros y/o con-
tratos de venta en firme en moneda extranjera y/o en bienes exportables.
```

#### F33 — correcta

- Nota de C2: 2.12.2.3 (tabla de ponderadores, 0 %): «financiaciones otorgadas a beneficiarios de la seguridad social o a empleados públicos […], en la medida que dichas operaciones estén denominadas en pesos, la fuente de fondos sea en esa moneda y las cuotas […] no excedan […] del 30 %». La condición delimita qué financiaciones entran en el renglón; la consecuencia del texto es el ponderador, que no es nodo de la arista (anotación).
- Anotaciones: consecuencia fuera de la arista: el texto asigna un ponderador, que no es nodo
- Origen: Condicion — «Denominación en pesos y fondos en pesos» (`Condicion_denominacion_en_pesos_y_fondos_en_pesos__las_operaciones_deben_estar_denominadas_03e0d7`)
  - descripción (salida del extractor): Las operaciones deben estar denominadas en pesos y la fuente de fondos debe ser en esa moneda.
  - tramo de E1 (salida del extractor): 'en la medida que dichas operaciones estén denominadas en pesos, la fuente de fondos sea en esa moneda'
- Destino: Operacion — «Financiación a beneficiarios seguridad social o empleados públicos» (`Operacion_financiacion_a_beneficiarios_seguridad_social_o_empleados_publicos__cap_2_12_2_3_47c5fe`)
  - descripción (salida del extractor): Financiaciones otorgadas a beneficiarios de la seguridad social o a empleados públicos, con código de descuento, denominadas en pesos, con fondos en esa moneda, donde las cuotas de todas las financiaciones de la entidad con sistema de amortización periódica no excedan del 30% de los ingresos del deudor y/o codeudores.
  - tramo de E1 (salida del extractor): 'financiaciones otorgadas a beneficiarios de la seguridad social o a empleados públicos'
- Unidad `cap::2.12.2.3` (cap, punto 2.12.2.3), páginas [23]; PDF `data/experiment/subset/TO_capitales_minimos_actual.pdf`; render `c1/paginas/cap_p7.png`, `c1/paginas/cap_p22.png`, `c1/paginas/cap_p23.png`
- Texto heredado: [encabezado S2] Sección 2. Capital mínimo por riesgo de crédito. / [chapeau_seccion S2] A los efectos de la aplicación de las disposiciones de la presente sección, las entidades financieras se clasificarán en: i)Grupo 1: entidades calificadas por el BCRA como de importancia sistémica a nivel local / [chapeau_seccion S2] (D-SIB) y sucursales o subsidiarias de bancos del exterior calificados como de impor- tancia sistémica global (G-SIB). / [chapeau_seccion S2] ii) Grupo 2: entidades financieras no comprendidas en el acápite i). En aquellos casos en que no se establezcan disposiciones específicas para cada uno de los citados grupos de entidades financieras, deberá aplicarse el mismo tratamiento a ambos grupos. Las entidades financieras que presenten cambios en su calificación –conforme a lo previsto en los acápites precedentes–, contarán con un plazo de 6 meses para aplicar las disposiciones específicas correspondientes al nuevo grupo al que pertenezcan. / [encabezado 2.12] 2.12. Tabla de ponderadores de riesgo. / [intro 2.12] Concepto Ponderador / [intro 2.12] –en %– / [encabezado 2.12.2] 2.12.2. Exposición a gobiernos y bancos centrales.
- Texto propio:

```text
2.12.2.3. Al sector público no financiero por financiaciones otorgadas a
beneficiarios de la seguridad social o a empleados públicos –en
ambos casos, con código de descuento–, en la medida que di-
chas operaciones estén denominadas en pesos, la fuente de
fondos sea en esa moneda y las cuotas de todas las financia-
ciones de la entidad que cuenten con sistema de amortización
periódica no excedan, al momento de los acuerdos, del 30% de
los ingresos del deudor y/o, en su caso, de los codeudores. 0
```

#### F31 — correcta

- Nota de C2: 14.5.7 i): dentro de las condiciones del cómputo («podrán ser computados […] en la medida que:»), «La operación podrá incluir bienes que no revistan la condición de bien de capital en la medida que aquellos que lo sean representen como mínimo el 90 %». Es un requisito que puede fallar y del que depende el cómputo de un aporte con bienes mixtos.
- Origen: Condicion — «Composición de bienes — mínimo 90% bien de capital» (`Condicion_composicion_de_bienes_minimo_90_bien_de_capital__los_bienes_que_revistan_la_cond_171611`)
  - descripción (salida del extractor): Los bienes que revistan la condición de bien de capital deben representar como mínimo el 90% del valor FOB total pagado.
  - tramo de E1 (salida del extractor): 'aquellos que lo sean representen como mínimo el 90% (noventa por ciento) del valor FOB total pagado'
- Destino: Operacion — «Cómputo de aportes inversión directa en especie» (`Operacion_computo_de_aportes_inversion_directa_en_especie__ext_14_5_7_97c0f6`)
  - descripción (salida del extractor): Aportes de inversión directa en especie instrumentados mediante la entrega al VPU de bienes de capital que pueden ser computados como ingresados y liquidados en el mercado de cambios, sujeto a cumplimiento de condiciones específicas.
  - tramo de E1 (salida del extractor): 'Los aportes de inversión directa en especie instrumentados mediante la entrega al VPU de bienes de capital podrán ser computados como ingresados y liquidados en el mercado de cambios'
- Unidad `ext::14.5.7` (ext, punto 14.5.7), páginas [182, 183]; PDF `data/experiment/subset/TO_exterior_cambios_actual.pdf`; render `c1/paginas/ext_p175.png`, `c1/paginas/ext_p182.png`, `c1/paginas/ext_p183.png`
- Texto heredado: [encabezado S14] Sección 14. Disposiciones complementarias asociadas al Régimen de Incentivo para Grandes Inversiones (RIGI). / [chapeau_seccion S14] En esta sección se detallan las disposiciones complementarias en materia cambiaria que, en la medida que las disposiciones generales no resulten más favorables, resultan aplicables a un Vehículo de Proyecto Único (VPU) adherido al Régimen de Incentivo los referidas al “Régimen de Incentivo para Grandes Inversiones” (RIGI) establecido en el Título VII de la Ley 27.742 y reglamentado por el Decreto 749/24 y concordantes. / [encabezado 14.5] 14.5. Otras disposiciones.
- Texto propio:

```text
14.5.7. Los aportes de inversión directa en especie instrumentados mediante la entrega al
VPU de bienes de capital podrán ser computados como ingresados y liquidados en
el mercado de cambios en la medida que:
i) El VPU haya demostrado el registro de ingreso aduanero del bien de capital por
un valor consistente con el monto del aporte que será computado como
ingresado y liquidado en el mercado de cambios.
La operación podrá incluir bienes que no revistan la condición de bien de capital
en la medida que aquellos que lo sean representen como mínimo el 90%
(noventa por ciento) del valor FOB total pagado y la entidad cuente con una
declaración jurada del cliente en la cual deje constancia de que los restantes
bienes son repuestos, accesorios o materiales necesarios para el
funcionamiento, construcción o instalación de los bienes de capital que se están
adquiriendo.
La entidad deberá contar con la correspondiente certificación de la entidad
encargada del seguimiento de pago de importaciones de bienes (SEPAIMPO).
ii) El VPU deberá presentar la documentación que avale la capitalización definitiva
del aporte. En caso de no disponerla, deberá presentar constancia del inicio del
trámite de inscripción ante el Registro Público de Comercio de la decisión de
capitalización definitiva de los aportes de capital computados de acuerdo con
los requisitos legales correspondientes y comprometerse a presentar la
documentación de la capitalización definitiva del aporte dentro de los 365
(trescientos sesenta y cinco) días corridos desde el inicio del trámite.
iii) Una entidad financiera haya registrado al aporte de capital en el régimen
informático de operaciones de cambio (RIOC) mediante la confección de dos
boletos de cambio sin movimiento de fondos con las siguientes características:
a) Los boletos deberán ser registrados en la fecha en que se produjo el
registro de ingreso aduanero de los bienes, independientemente de cuál
sea el momento en que el cliente solicite su registro ante la entidad
financiera.
b) El boleto de compra se confeccionará con un código de concepto que
identifique que se trata de un aporte comprendido en este mecanismo.
En caso de que el VPU contemple la posibilidad de aplicar cobros de
exportaciones de bienes para la repatriación del aporte, la entidad deberá
asignar el correspondiente número de identificación (número APX) para el
"Seguimiento de anticipos y otras financiaciones de exportación de bienes",
el cual quedará a cargo de la propia entidad.
c) El boleto de venta se confeccionará con el código de concepto de pago
diferido de importaciones de bienes de capital, dejando constancia que el
pago se enmarca en el presente mecanismo.
```

#### F53 — correcta

- Nota de C2: 4.4 y 4.4.2: los importadores podrán suscribir BOPREAL y la entidad deberá contar con certificaciones que «deberán verificar que: […] la operación se encuentra declarada, en caso de corresponder, en la última presentación vencida del “Relevamiento de activos y pasivos externos”». Requisito de la suscripción, verificado por la certificación. Misma unidad y destino que otra ficha de la muestra.
- Origen: Condicion — «Operación declarada en presentación vencida de Relevamiento» (`Condicion_operacion_declarada_en_presentacion_vencida_de_relevamiento__la_operacion_debe_e_79ea4c`)
  - descripción (salida del extractor): La operación debe encontrarse declarada, en caso de corresponder, en la última presentación vencida del Relevamiento de activos y pasivos externos
  - tramo de E1 (salida del extractor): 'la operación se encuentra declarada, en caso de corresponder, en la última presentación vencida del "Relevamiento de activos y pasivos externos"'
- Destino: Operacion — «Suscripción de BOPREAL por deudores de importaciones» (`Operacion_suscripcion_de_bopreal_por_deudores_de_importaciones__ext_4_4_fefb25`)
  - descripción (salida del extractor): Suscripción de Bonos para la Reconstrucción de una Argentina Libre (BOPREAL) por deudores de importaciones de bienes con registro de ingreso aduanero hasta el 12/12/23, por hasta el monto de la deuda pendiente de pago
  - tramo de E1 (salida del extractor): 'Los importadores de bienes podrán suscribir Bonos para la Reconstrucción de una Argentina Libre (BOPREAL) por hasta el monto de la deuda pendiente de pago por sus importaciones de bienes con registro de ingreso aduanero hasta el 12/12/23.'
- Unidad `ext::4.4.2` (ext, punto 4.4.2), páginas [60]; PDF `data/experiment/subset/TO_exterior_cambios_actual.pdf`; render `c1/paginas/ext_p60.png`
- Texto heredado: [encabezado S4] Sección 4. Otras disposiciones específicas. / [encabezado 4.4] 4.4. Suscripción de bonos BOPREAL por parte de deudores de importaciones de bienes con / [intro 4.4] registro de ingreso aduanero hasta el 12/12/23. Los importadores de bienes podrán suscribir Bonos para la Reconstrucción de una Argentina Libre (BOPREAL) por hasta el monto de la deuda pendiente de pago por sus importaciones de bienes con registro de ingreso aduanero hasta el 12/12/23. La entidad que concrete la oferta de suscripción en nombre del cliente deberá contar con las respectivas certificaciones sobre el monto pendiente de pago emitidas por la/s entidad/es encargada/s del seguimiento de las oficializaciones involucradas en el Seguimiento de Pagos de Importaciones de Bienes (SEPAIMPO), las cuales deberán verificar que: / [cierre 4.4] En caso de que la importación de bienes encuadre en los puntos 10.3.3., 10.9.1., 10.9.2. y 10.9.3., la entidad que concrete la oferta de suscripción en nombre del cliente deberá verificar en forma directa lo previsto en los puntos 4.4.1. a 4.4.5. y, adicionalmente, contar con una declaración jurada del cliente en la que deja constancia de que no ha solicitado la utilización de este mecanismo en otra entidad por esa deuda. La entidad también deberá realizar la correspondiente intervención de la documentación aduanera. Adicionalmente, la mencionada entidad deberá realizar un boleto de venta de cambio a nombre del importador por el código de concepto “B26. Registro de importaciones de bienes por adjudicación de bonos BOPREAL”; consignando el valor nominal en moneda extranjera de bonos BOPREAL adjudicado al importador y el número de oficialización al que corresponde.
- Texto propio:

```text
4.4.2. la operación se encuentra declarada, en caso de corresponder, en la última
presentación vencida del "Relevamiento de activos y pasivos externos".
```

#### F04 — correcta

- Nota de C2: 7.10.3: los cobros «que resulten elegibles para el mecanismo previsto en este punto […] podrán quedar depositados». La elegibilidad es antecedente del depósito. El destino es permisivo («podrán») y está tipado Operacion: la relación es cierta igual.
- Anotaciones: tipo: destino permisivo tipado Operacion
- Origen: Condicion — «Elegibilidad para mecanismo de cobros de exportación» (`Condicion_elegibilidad_para_mecanismo_de_cobros_de_exportacion__los_cobros_deben_resultar__617b9e`)
  - descripción (salida del extractor): Los cobros deben resultar elegibles para el mecanismo previsto en el punto 7.10.3
  - tramo de E1 (salida del extractor): 'que resulten elegibles para el mecanismo previsto en este punto'
- Destino: Operacion — «Depósito de cobros de exportación en cuentas corresponsales» (`Operacion_deposito_de_cobros_de_exportacion_en_cuentas_corresponsales__ext_7_10_3_c7b377`)
  - descripción (salida del extractor): Depósito de cobros de exportación de bienes elegibles para el mecanismo del punto, no aplicados simultáneamente a usos admitidos, en cuentas corresponsales en el exterior de entidades financieras locales y/o en cuentas locales en moneda extranjera de entidades financieras locales, hasta su aplicación
  - tramo de E1 (salida del extractor): 'Los cobros de exportación de bienes recibidos por un exportador que resulten elegibles para el mecanismo previsto en este punto y no sean aplicados simultáneamente a los usos admitidos podrán quedar depositados hasta su aplicación en las cuentas corresponsales en el exterior de entidades financieras locales y/o en cuentas locales en moneda extranjera de entidades financieras locales'
- Unidad `ext::7.10.3` (ext, punto 7.10.3), páginas [102]; PDF `data/experiment/subset/TO_exterior_cambios_actual.pdf`; render `c1/paginas/ext_p99.png`, `c1/paginas/ext_p102.png`
- Texto heredado: [encabezado S7] Sección 7. Cobros de exportaciones de bienes. / [encabezado 7.10] 7.10. Operaciones habilitadas para la aplicación de cobros de exportaciones de bienes en el marco / [intro 7.10] del régimen de fomento de inversión para las exportaciones (Decreto 234/21).
- Texto propio:

```text
7.10.3. Los cobros de exportación de bienes recibidos por un exportador que resulten
elegibles para el mecanismo previsto en este punto y no sean aplicados
simultáneamente a los usos admitidos podrán quedar depositados hasta su
aplicación en las cuentas corresponsales en el exterior de entidades financieras
locales y/o en cuentas locales en moneda extranjera de entidades financieras locales.
En caso de que la aplicación no hubiese tenido lugar al momento del vencimiento del
plazo para la liquidación de divisas del correspondiente permiso, el exportador podrá
solicitar a la entidad encargada del seguimiento del permiso que el plazo sea
ampliado hasta la fecha en que se estima se efectuará la aplicación.
```

## → Potestad

Cifras de C2: 29 correctas, 1 incorrectas, 0 no decidibles; Wilson 95 % [0.8333, 0.9941].

### Incorrectas: 1

#### F57 — incorrecta

- Nota de C2: 3.3 y 3.3.3: entre lo que «Se volcarán en un “Manual de procedimientos de clasificación y previsión”», «El ejercicio de la opción de agrupar las financiaciones de naturaleza comercial […], cuenten o no con garantías preferidas, junto con los créditos para consumo o vivienda». «Cuenten o no con garantías preferidas» es una cláusula de indiferencia: dice que la opción rige con o sin garantías, es decir, que eso no la condiciona. La propia descripción del extractor la llama «condición indiferente». El texto no sostiene que sea antecedente de la opción.
- Origen: Condicion — «Garantías preferidas — condición indiferente» (`Condicion_garantias_preferidas_condicion_indiferente__que_las_financiaciones_cuenten_o_no__1a9e1c`)
  - descripción (salida del extractor): Que las financiaciones cuenten o no con garantías preferidas (condición indiferente para el ejercicio de la opción)
  - tramo de E1 (salida del extractor): 'cuenten o no con garantías preferidas'
- Destino: Potestad — «Opción de agrupar financiaciones comerciales» (`Potestad_opcion_de_agrupar_financiaciones_comerciales__facultad_de_agrupar_las_financiaci_20d56c`)
  - descripción (salida del extractor): Facultad de agrupar las financiaciones de naturaleza comercial de hasta el equivalente a dos veces el importe de referencia establecido en el punto 3.7., con o sin garantías preferidas, junto con los créditos para consumo o vivienda, en el manual de procedimientos de clasificación y previsión
  - tramo de E1 (salida del extractor): 'El ejercicio de la opción de agrupar las financiaciones de naturaleza comercial de hasta el equivalente a dos veces el importe de referencia establecido en el punto 3.7., cuenten o no con garantías preferidas, junto con los créditos para consumo o vivienda'
- Unidad `cla::3.3.3` (cla, punto 3.3.3), páginas [9]; PDF `data/experiment/subset/TO_clasificacion_deudores_actual.pdf`; render `c1/paginas/cla_p9.png`, `c1/paginas/cla_p10.png`
- Texto heredado: [encabezado S3] Sección 3. Tarea de clasificación. / [encabezado 3.3] 3.3. Manual de procedimientos de clasificación y previsión. / [intro 3.3] Se volcarán en un “Manual de procedimientos de clasificación y previsión”: / [cierre 3.3] El manual deberá estar a disposición permanente de la Superintendencia de Entidades Finan- cieras y Cambiarias.
- Texto propio:

```text
3.3.3. El ejercicio de la opción de agrupar las financiaciones de naturaleza comercial de hasta el
equivalente a dos veces el importe de referencia establecido en el punto 3.7., cuenten o
no con garantías preferidas, junto con los créditos para consumo o vivienda.
```

### No decidibles: 0

### Correctas sorteadas (semilla 9868107349525416484): 5

#### F12 — correcta

- Nota de C2: 5.12: «Dichas entidades podrán realizar operaciones de arbitrajes y canjes en el exterior siempre que la contraparte sea:» (la lista 5.12.1 a 5.12.4 está en otras unidades). La relación es cierta; el nodo Condicion queda sin el contenido de la lista (tramo «siempre que la contraparte sea:»).
- Anotaciones: condicion vacia: la enumeración está en otras unidades
- Origen: Condicion — «Contraparte en operaciones de arbitraje y canje» (`Condicion_contraparte_en_operaciones_de_arbitraje_y_canje__la_operacion_de_arbitraje_o_can_71c78d`)
  - descripción (salida del extractor): La operación de arbitraje o canje en el exterior solo puede realizarse cuando la contraparte reúne determinadas características (que se especifican en los ítems siguientes)
  - tramo de E1 (salida del extractor): 'siempre que la contraparte sea:'
- Destino: Potestad — «Facultad realizar arbitrajes y canjes en exterior» (`Potestad_facultad_realizar_arbitrajes_y_canjes_en_exterior__las_entidades_autorizadas_que_cab9aa`)
  - descripción (salida del extractor): Las entidades autorizadas quedan facultadas a realizar operaciones de arbitrajes y canjes en el exterior
  - tramo de E1 (salida del extractor): 'Dichas entidades podrán realizar operaciones de arbitrajes y canjes en el exterior'
- Unidad `ext::5.12::intro` (ext, punto 5.12), páginas [73]; PDF `data/experiment/subset/TO_exterior_cambios_actual.pdf`; render `c1/paginas/ext_p73.png`
- Texto heredado: [encabezado S5] Sección 5. Pautas operativas. / [encabezado 5.12] 5.12. Operaciones de arbitrajes y canjes en el exterior de las entidades.
- Texto propio:

```text
Dichas entidades podrán realizar operaciones de arbitrajes y canjes en el exterior siempre que
la contraparte sea:
```

#### F37 — correcta

- Nota de C2: 10.3.5: «podrá dar acceso al mercado de cambios […] en la medida que verifique previamente que se cumplen la totalidad de requisitos detallados en el punto 10.3.2.».
- Origen: Condicion — «Verificación previa de requisitos del punto 10.3.2» (`Condicion_verificacion_previa_de_requisitos_del_punto_10_3_2__se_cumplen_la_totalidad_de_r_376e46`)
  - descripción (salida del extractor): Se cumplen la totalidad de requisitos detallados en el punto 10.3.2, con la sustitución de lo requerido en los incisos i), iii) y iv) del punto 10.3.2.1 por lo siguiente
  - tramo de E1 (salida del extractor): 'en la medida que verifique previamente que se cumplen la totalidad de requisitos detallados en el punto 10.3.2.'
- Destino: Potestad — «Facultad de dar acceso al mercado de cambios» (`Potestad_facultad_de_dar_acceso_al_mercado_de_cambios__la_entidad_interviniente_tiene_la__fbebc9`)
  - descripción (salida del extractor): La entidad interviniente tiene la facultad de dar acceso al mercado de cambios para el pago al exterior de importaciones de bienes ingresadas desde zonas francas con transferencia aduanera, sujeto a verificación previa de requisitos
  - tramo de E1 (salida del extractor): 'La entidad interviniente podrá dar acceso al mercado de cambios'
- Unidad `ext::10.3.5::intro` (ext, punto 10.3.5), páginas [137]; PDF `data/experiment/subset/TO_exterior_cambios_actual.pdf`; render `c1/paginas/ext_p137.png`
- Texto heredado: [encabezado S10] Sección 10. Pagos de importaciones y otras compras de bienes en el exterior. / [encabezado 10.3] 10.3. Pagos de importaciones de bienes que cuentan con registro de ingreso aduanero. / [encabezado 10.3.5] 10.3.5. Pagos de importaciones de bienes ingresadas desde zonas francas con transferencia
- Texto propio:

```text
aduanera de dominio del exportador al importador.
La entidad interviniente podrá dar acceso al mercado de cambios para el pago al
exterior de importaciones de bienes ingresadas desde zonas francas con
transferencia aduanera de dominio del exportador al importador en la medida que
verifique previamente que se cumplen la totalidad de requisitos detallados en el punto
10.3.2., reemplazando lo requerido en los incisos i), iii) y iv) del punto 10.3.2.1. por lo
siguiente:
```

#### F54 — correcta

- Nota de C2: 5.8: «Las entidades podrán elaborar un boleto global diario para las situaciones que se detallan a continuación, en la medida que se verifiquen todas las condiciones indicadas en cada caso». La relación es cierta; la Condicion es una remisión genérica a las condiciones de cada caso, sin contenido propio.
- Anotaciones: condicion vacia: remisión genérica a las condiciones de cada caso
- Origen: Condicion — «Verificación de todas las condiciones» (`Condicion_verificacion_de_todas_las_condiciones__se_debe_verificar_que_se_cumplan_todas_la_b652de`)
  - descripción (salida del extractor): Se debe verificar que se cumplan todas las condiciones indicadas en cada caso para que la facultad de elaborar un boleto global diario sea ejercible.
  - tramo de E1 (salida del extractor): 'en la medida que se verifiquen todas las condiciones indicadas en cada caso'
- Destino: Potestad — «Elaboración boleto global diario» (`Potestad_elaboracion_boleto_global_diario__las_entidades_estan_facultadas_a_elaborar_un_b_ac2b1a`)
  - descripción (salida del extractor): Las entidades están facultadas a elaborar un boleto global diario para las situaciones que se detallan a continuación, en la medida que se verifiquen todas las condiciones indicadas en cada caso.
  - tramo de E1 (salida del extractor): 'Las entidades podrán elaborar un boleto global diario para las situaciones que se detallan a continuación'
- Unidad `ext::5.8::intro` (ext, punto 5.8), páginas [71]; PDF `data/experiment/subset/TO_exterior_cambios_actual.pdf`; render `c1/paginas/ext_p71.png`
- Texto heredado: [encabezado S5] Sección 5. Pautas operativas. / [encabezado 5.8] 5.8. Boletos globales diarios.
- Texto propio:

```text
Las entidades podrán elaborar un boleto global diario para las situaciones que se detallan a
continuación, en la medida que se verifiquen todas las condiciones indicadas en cada caso.
En todos los casos, se deberá requerir una lista detallada de los beneficiarios/ordenantes de
los pagos comprendidos en dicho boleto, debiendo como mínimo informar respecto de ellos:
nombres y apellidos completos o denominación social (según corresponda), CUIT, CUIL o CDI
y el monto que le corresponde.
```

#### F59 — correcta

- Nota de C2: 10.3.2: «La entidad interviniente podrá dar acceso al mercado de cambios para el pago […], en la medida que verifique previamente la totalidad de los siguientes requisitos:» (10.3.2.1 y siguientes, en otras unidades). La relación es cierta; la Condicion queda sin la enumeración.
- Anotaciones: condicion vacia: la enumeración está en otras unidades
- Origen: Condicion — «Verificación previa de requisitos para acceso al mercado» (`Condicion_verificacion_previa_de_requisitos_para_acceso_al_mercado__la_entidad_intervinien_340d50`)
  - descripción (salida del extractor): La entidad interviniente debe verificar previamente la totalidad de los requisitos que siguen para ejercer la facultad de dar acceso al mercado de cambios
  - tramo de E1 (salida del extractor): 'en la medida que verifique previamente la totalidad de los siguientes requisitos'
- Destino: Potestad — «Facultad de dar acceso al mercado de cambios» (`Potestad_facultad_de_dar_acceso_al_mercado_de_cambios__la_entidad_interviniente_esta_facu_b82ae0`)
  - descripción (salida del extractor): La entidad interviniente está facultada para dar acceso al mercado de cambios para el pago al exterior de importaciones de bienes que cuentan con registro de ingreso aduanero que constan en el SEPAIMPO
  - tramo de E1 (salida del extractor): 'La entidad interviniente podrá dar acceso al mercado de cambios para el pago al exterior de importaciones de bienes que cuentan con registro de ingreso aduanero que constan en el SEPAIMPO'
- Unidad `ext::10.3.2::intro` (ext, punto 10.3.2), páginas [134]; PDF `data/experiment/subset/TO_exterior_cambios_actual.pdf`; render `c1/paginas/ext_p134.png`
- Texto heredado: [encabezado S10] Sección 10. Pagos de importaciones y otras compras de bienes en el exterior. / [encabezado 10.3] 10.3. Pagos de importaciones de bienes que cuentan con registro de ingreso aduanero. / [encabezado 10.3.2] 10.3.2. Requisitos de acceso para el pago de oficializaciones de importación comprendidas
- Texto propio:

```text
en el SEPAIMPO.
La entidad interviniente podrá dar acceso al mercado de cambios para el pago al
exterior de importaciones de bienes que cuentan con registro de ingreso aduanero
que constan en el SEPAIMPO, en la medida que verifique previamente la totalidad de
los siguientes requisitos:
```

#### F14 — correcta

- Nota de C2: 2.2.3: «El DNI-d en formato credencial virtual […] podrá ser exhibido […] en la medida que se observen las disposiciones contenidas en el punto 2.12.».
- Origen: Condicion — «Observancia de medidas mínimas de seguridad» (`Condicion_observancia_de_medidas_minimas_de_seguridad__la_exhibicion_del_dni_d_en_formato__1c5c29`)
  - descripción (salida del extractor): La exhibición del DNI-d en formato credencial virtual está condicionada a la observancia de las disposiciones sobre medidas mínimas de seguridad en entidades financieras
  - tramo de E1 (salida del extractor): 'en la medida que se observen las disposiciones contenidas en el punto 2.12. de las normas sobre "Medidas mínimas de seguridad en entidades financieras"'
- Destino: Potestad — «Exhibición de DNI-d en formato credencial virtual» (`Potestad_exhibicion_de_dni_d_en_formato_credencial_virtual__el_dni_d_en_formato_credencia_7b399e`)
  - descripción (salida del extractor): El DNI-d en formato credencial virtual para dispositivos móviles inteligentes podrá ser exhibido en las casas operativas de las entidades financieras, sujeto a observancia de disposiciones sobre medidas mínimas de seguridad
  - tramo de E1 (salida del extractor): 'El DNI-d en formato credencial virtual para dispositivos móviles inteligentes podrá ser exhibido en las casas operativas de las entidades financieras en la medida que se observen las disposiciones contenidas en el punto 2.12. de las normas sobre "Medidas mínimas de seguridad en entidades financieras"'
- Unidad `docvig::2.2.3` (docvig, punto 2.2.3), páginas [5]; PDF `data/experiment/escalado_prep/pdfs/docvig.pdf`; render `c1/paginas/docvig_p5.png`
- Texto heredado: [encabezado S2] Sección 2. Para extranjeros / [encabezado 2.2] 2.2. Mayores de 75 años al 31.12.14 y los incapaces declarados judicialmente.
- Texto propio:

```text
2.2.3. A partir del año de otorgada la residencia permanente o temporaria en el país.
Documento Nacional de Identidad, manual o digital (DNI-m o DNI-d).
De existir prueba en contrario del país de domicilio, aplicará el punto 2.2.2.
En todos los casos deberá acreditarse la categoría de residencia, su vigencia y el tiempo de
radicación a partir de documentación emitida por la DNM.
El DNI-d en formato credencial virtual para dispositivos móviles inteligentes podrá ser exhibido
en las casas operativas de las entidades financieras en la medida que se observen las disposi-
ciones contenidas en el punto 2.12. de las normas sobre “Medidas mínimas de seguridad en
entidades financieras”.
```

