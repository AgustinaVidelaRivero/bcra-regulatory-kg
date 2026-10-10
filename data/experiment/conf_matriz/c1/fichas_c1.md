# U-CONF-MATRIZ, C1: fichas en el orden de lectura

Acta sellada `c1/acta_c1.json` (sha256 `f5990dff532e6ca2c9eb91e4f8db7e98be105da517e1071c7b8ddc14c8926602`). Las fichas no llevan el par ni el orden del sorteo; las descripciones y los tramos son salida del extractor, no del texto. Sin el veredicto de E3, sin otras aristas de los nodos y sin el resultado del estudio original.

## F01

- **Predicado:** `condicion_de`
- **Origen:** Condicion — «Cancelación total de intereses devengados» (`Condicion_cancelacion_total_de_intereses_devengados__supuesto_en_que_deudores_han_cancelad_d0093a`)
  - descripción (salida del extractor): Supuesto en que deudores han cancelado la totalidad de los intereses devengados
  - tramo de E1 en la unidad (salida del extractor): 'Los deudores que hayan cancelado la totalidad de los intereses devengados'
- **Destino:** Potestad — «Clasificación en situación normal si se cumplen condiciones» (`Potestad_clasificacion_en_situacion_normal_si_se_cumplen_condiciones__facultad_de_clasifi_cb98e3`)
  - descripción (salida del extractor): Facultad de clasificar deudores en situación normal si han cancelado totalidad de intereses devengados y observan otras condiciones de esa categoría
  - tramo de E1 en la unidad (salida del extractor): 'podrán ser clasificados en "situación normal" si además observan las otras condiciones previstas para esa categoría'
- **Unidad:** `cla::6.5.2.2` (cla, punto 6.5.2.2, punto_propio)
- **Páginas:** unidad [22, 23], arista [22, 23]; PDF `data/experiment/subset/TO_clasificacion_deudores_actual.pdf`
- **Render:** `paginas/cla_p19.png`, `paginas/cla_p22.png`, `paginas/cla_p23.png`
- **Texto heredado:**
  - [encabezado, S6, p. [17]] Sección 6. Clasificación de los deudores de la cartera comercial.
  - [encabezado, 6.5, p. [19]] 6.5. Niveles de clasificación.
  - [intro, 6.5, p. [19]] Cada cliente, y la totalidad de sus financiaciones comprendidas, se incluirá en una de las si- guientes cinco categorías, las que se definen teniendo en cuenta las condiciones que se deta- llan en cada caso. Los clientes que no registren asistencia crediticia de la entidad y que posteriormente reciban fi- nanciaciones de ésta que no superen el importe resultante de aplicar sobre el saldo de deuda registrado en el sistema financiero, según la última información disponible en la “Central de deudores” a la fecha de su otorgamiento, el porcentaje establecido en el punto 2.2.5. de las normas sobre “Previsiones mínimas por riesgo de incobrabilidad” correspondiente a la peor cla- sificación asignada, podrán ser clasificados por la entidad teniendo en cuenta únicamente el análisis del flujo de fondos proyectado. Las asistencias así otorgadas no serán consideradas a los fines a que se refiere el punto 6.6. A fin de verificar el cumplimiento de las obligaciones sin recurrir a nueva financiación directa o indirecta o a refinanciaciones, no se considerarán refinanciaciones las facilidades adicionales que se otorguen respecto de los márgenes vigentes acordados, siempre que el nuevo apoyo crediticio implique nuevos desembolsos de fondos y no supere el 10 % del cupo asignado en oportunidad de la última evaluación crediticia del cliente, en la medida en que éstas sean con- sistentes con el curso normal de los negocios y exista capacidad para atender el resto de las obligaciones financieras, ni las nuevas financiaciones y las refinanciaciones asociadas a una mayor inversión derivada de la expansión de las actividades, y siempre que pueda demostrarse que el flujo de fondos proyectado permitirá afrontar la totalidad de sus obligaciones. Tampoco se considerarán dentro de ese concepto las refinanciaciones otorgadas a los produc- tores agropecuarios cuando ello resulte de la aplicación de disposiciones vinculadas a la Ley de Emergencia Agropecuaria, sin perjuicio de lo cual, a los fines de la clasificación, deberá tenerse en cuenta el flujo de fondos proyectado para el momento en que concluya la vigencia de la emergencia declarada. El tratamiento que se dispense en ese marco no podrá implicar mejora- miento de la clasificación asignada al cliente en función de su situación individual, preexistente a la emergencia, ni su aplicación extenderse más allá de la vigencia fijada para ella.
  - [encabezado, 6.5.2, p. [20]] 6.5.2. Con seguimiento especial.
- **Texto propio** («En negociación o con acuerdos de refinanciación.»):

```text
6.5.2.2. En negociación o con acuerdos de refinanciación.
Incluye aquellos clientes que ante la imposibilidad de hacer frente al pago de sus
obligaciones en las condiciones pactadas, manifiesten fehacientemente antes de
los 60 días contados desde la fecha en que se verificó la mora en el pago de las
obligaciones, la intención de refinanciar sus deudas, observando los demás indi-
cadores pertinentes del punto 6.5.2.1.
No podrán incluirse deudores cuyas obligaciones hayan sido refinanciadas por la
entidad, bajo esta modalidad, en los últimos 24 meses.
El acuerdo con la entidad financiera deberá concertarse dentro de los 90 o 180
días contados desde la fecha en que se verificó la mora en el pago de las obliga-
ciones, según sea necesario llegar a acuerdos con hasta dos entidades o con
más de dos, respectivamente.
De no haberse alcanzado el acuerdo dentro del plazo establecido, deberá reclasi-
ficarse al deudor en la categoría inferior que corresponda, de acuerdo con los in-
dicadores establecidos para cada nivel.
Los deudores que hayan cancelado la totalidad de los intereses devengados, po-
drán ser clasificados en “situación normal” si además observan las otras condi-
ciones previstas para esa categoría.
Los deudores que no hubieran cancelado por lo menos los intereses devengados
dentro de los 180 días de concertada la refinanciación, deberán ser reclasificados
en la categoría “con alto riesgo de insolvencia”.
A los efectos previstos en los dos últimos párrafos anteriores y aun cuando se
hayan cancelado los mencionados porcentajes de deuda, los deudores que
hayan recibido crédito adicional en los términos a que se refiere el punto 2.2.5. de
las normas sobre “Previsiones mínimas por riesgo de incobrabilidad”, y en la me-
dida en que dicha financiación adicional no hubiese sido cancelada, deberán
permanecer en esta categoría por lo menos 180 días, contados desde la fecha en
que se otorgó crédito adicional o desde que se celebró el acuerdo de refinancia-
ción, la circunstancia más reciente. Ello, salvo que por aplicación de otras pautas
corresponda categorizarlo en el nivel inferior.
Los deudores que incurran en atrasos de más de 31 días respecto de las condi-
ciones pactadas en las obligaciones refinanciadas, deberán ser recategorizados
en el nivel inmediato inferior “con problemas”.
```

## F02

- **Predicado:** `condicion_de`
- **Origen:** Condicion — «Condición — instrumentos de protección crediticia limitados» (`Condicion_condicion_instrumentos_de_proteccion_crediticia_limitados__el_instrumento_de_pro_d6ac09`)
  - descripción (salida del extractor): El instrumento de protección crediticia está expuesto solamente a las pérdidas que ocurran hasta su vencimiento.
  - tramo de E1 en la unidad (salida del extractor): 'estén expuestos solamente a las pérdidas que ocurran hasta su vencimiento'
- **Destino:** Potestad — «Opción vencimiento contractual — instrumentos de protección crediticia» (`Potestad_opcion_vencimiento_contractual_instrumentos_de_proteccion_crediticia__la_entidad_12e572`)
  - descripción (salida del extractor): La entidad puede aplicar el vencimiento contractual del instrumento de protección crediticia sin necesidad de tener en cuenta el vencimiento de la posición protegida, cuando el instrumento esté expuesto solamente a las pérdidas que ocurran hasta su vencimiento.
  - tramo de E1 en la unidad (salida del extractor): 'Para los instrumentos de protección crediticia que estén expuestos solamente a las pérdidas que ocurran hasta su vencimiento, la entidad podrá aplicar el vencimiento contractual del instrumento sin necesidad de tener en cuenta el que corresponde a la posición protegida'
- **Unidad:** `cap::3.1.1.9` (cap, punto 3.1.1.9, punto_propio)
- **Páginas:** unidad [30, 31], arista [30, 31]; PDF `data/experiment/subset/TO_capitales_minimos_actual.pdf`
- **Render:** `paginas/cap_p29.png`, `paginas/cap_p30.png`, `paginas/cap_p31.png`
- **Texto heredado:**
  - [encabezado, S3, p. [29]] Sección 3. Capital mínimo por riesgo de crédito. Titulizaciones e inversiones en fon- dos.
  - [encabezado, 3.1, p. [29]] 3.1. Tratamiento de las titulizaciones.
  - [intro, 3.1, p. [29]] Se denomina “posición de titulización” a la exposición a una titulización (o retitulización), tradi- cional o sintética, o a una estructura con similares características. La exposición a los riesgos de una titulización puede surgir, entre otros, de los siguientes con- ceptos: tenencia de títulos valores emitidos en el marco de la titulización –es decir, títulos de deuda y/o certificados de participación, tales como bonos de titulización de activos (“Asset- Backed Securities”, ABS) y bonos de titulización hipotecaria (“Mortgage-Backed Securities”, MBS)–, mejoras crediticias, facilidades de liquidez, “swaps” de tasa de interés o de monedas y derivados de crédito. Las reservas (“reserve accounts”), tales como las cuentas de garantía en efectivo, se considerarán como un activo para la entidad financiera originante, recibiendo tam- bién el tratamiento de posiciones de titulización. Dado que las titulizaciones pueden estructurarse de diferentes formas, la exigencia de capital para una posición de titulización se determinará teniendo en cuenta su realidad o finalidad eco- nómica y no su forma jurídica. En los casos en que exista incertidumbre acerca de si una de- terminada operación debe considerarse como titulización, la entidad deberá aplicar el criterio que estime mejor se ajusta a la realidad económica de la operación e informar a la SEFyC los fundamentos que lo sustenten.
  - [encabezado, 3.1.1, p. [29]] 3.1.1. Conceptos.
- **Texto propio** («Vencimiento de los tramos: al determinar el vencimiento de una posición de titu-»):

```text
3.1.1.9. Vencimiento de los tramos: al determinar el vencimiento de una posición de titu-
lización se deberá tener en cuenta el plazo máximo durante el cual la entidad
estará expuesta a las pérdidas potenciales de los activos subyacentes tituliza-
dos.
En los casos de compromisos asumidos por la entidad, el vencimiento de la po-
sición de titulización que resulta de ese compromiso se calculará como la suma
del vencimiento contractual del compromiso y el vencimiento más prolongado
de los activos a los que estaría expuesta la entidad luego de una utilización de
la facilidad comprometida. Si dichos activos fueran de carácter rotativo, se ten-
drá que utilizar el vencimiento residual más prolongado contractualmente posi-
ble del activo que podría ser agregado durante el periodo de rotación (y no el
vencimiento más largo de los activos ya incluidos en el conjunto subyacente).
El mismo tratamiento se aplicará a todo otro instrumento en el cual el riesgo del
compromiso o de la protección otorgada no esté limitado sólo a las pérdidas in-
curridas hasta el vencimiento de tal instrumento, tales como un “swap” de ren-
dimiento total.
Para los instrumentos de protección crediticia que estén expuestos solamente a
las pérdidas que ocurran hasta su vencimiento, la entidad podrá aplicar el ven-
cimiento contractual del instrumento sin necesidad de tener en cuenta el que
corresponde a la posición protegida.
```

## F03

- **Predicado:** `condicion_de`
- **Origen:** Condicion — «Reclasificación — resto de deudas en nivel inmediato superior» (`Condicion_reclasificacion_resto_de_deudas_en_nivel_inmediato_superior__condicion_adicional_8e38df`)
  - descripción (salida del extractor): Condición adicional para reclasificación del deudor refinanciado: el resto de sus deudas debe reunir, como mínimo, las condiciones previstas en el nivel inmediato superior.
  - tramo de E1 en la unidad (salida del extractor): 'El deudor refinanciado que haya cumplido con lo dispuesto en los párrafos precedentes, según corresponda, podrá ser reclasificado en el nivel inmediato superior si, además, el resto de sus deudas reúnen, como mínimo, las condiciones previstas en el citado nivel.'
- **Destino:** Potestad — «Reclasificación en nivel inmediato superior — deudor refinanciado» (`Potestad_reclasificacion_en_nivel_inmediato_superior_deudor_refinanciado__facultad_de_rec_d7d5a2`)
  - descripción (salida del extractor): Facultad de reclasificar en el nivel inmediato superior a clientes cuyas deudas hayan sido refinanciadas mediante obligaciones de pago periódico (mensual o bimestral), cuando se cumplan las condiciones establecidas.
  - tramo de E1 en la unidad (salida del extractor): 'Los clientes cuyas deudas hayan sido refinanciadas mediante obligaciones de pago periódico (mensual o bimestral) podrán ser reclasificados en el nivel inmediato superior'
- **Unidad:** `cla::7.2.3` (cla, punto 7.2.3, punto_propio)
- **Páginas:** unidad [36, 37], arista [36, 37]; PDF `data/experiment/subset/TO_clasificacion_deudores_actual.pdf`
- **Render:** `paginas/cla_p36.png`, `paginas/cla_p37.png`
- **Texto heredado:**
  - [encabezado, S7, p. [33]] Sección 7. Clasificación de los deudores de la cartera para consumo o vivienda.
  - [encabezado, 7.2, p. [35]] 7.2. Niveles de clasificación.
- **Texto propio** («Riesgo medio.»):

```text
7.2.3. Riesgo medio.
Comprende los clientes que muestran alguna incapacidad para cancelar sus obligacio-
nes, con atrasos de más de 90 hasta 180 días.
En cuanto a la situación jurídica del deudor, se considerará si mantiene convenios de pa-
go resultantes de concordatos judiciales o extrajudiciales homologados (incluyendo los
acuerdos preventivos extrajudiciales homologados) a vencer cuando aún no se haya can-
celado el 10 % del importe involucrado en el citado acuerdo.
A fin de determinar el importe de la cancelación, se admitirá computar el 50 % de las ga-
rantías adicionales a las ofrecidas originalmente, constituidas sobre bienes no vinculados
a la explotación del deudor –con excepción de las hipotecas sobre inmuebles rurales que,
por lo tanto, serán computables–, observando los márgenes de cobertura establecidos en
las normas sobre “Garantías”.
Los clientes cuyas deudas hayan sido refinanciadas mediante obligaciones de pago pe-
riódico (mensual o bimestral) podrán ser reclasificados en el nivel inmediato superior,
cuando hayan cumplido puntualmente o con atrasos que no superen los 31 días, con el
pago de 2 cuotas consecutivas o, cuando se trate de financiaciones de pago único, perió-
dico superior a bimestral o irregular, hayan cancelado al menos el 5 % de sus obligacio-
nes refinanciadas (por capital), con más la cantidad de cuotas o el porcentaje acumulado
que pudiera corresponder, respectivamente, si la refinanciación se hubiera otorgado de
encontrarse incluido el deudor en el nivel inferior.
El deudor refinanciado que haya cumplido con lo dispuesto en los párrafos precedentes,
según corresponda, podrá ser reclasificado en el nivel inmediato superior si, además, el
resto de sus deudas reúnen, como mínimo, las condiciones previstas en el citado nivel.
El deudor que, encontrándose clasificado en esta categoría, haya refinanciado su deuda
–aun cuando haya cancelado las cuotas o el porcentaje establecidos precedentemente– y
recibido crédito adicional en los términos a que se refiere el punto 2.2.5. de las normas
sobre “Previsiones mínimas por riesgo de incobrabilidad”, y en la medida en que dicha fi-
nanciación adicional no hubiese sido cancelada, deberá permanecer en esta categoría
por lo menos 180 días contados desde la fecha en que se otorgó el crédito adicional o
desde que se celebró el acuerdo de refinanciación, la circunstancia más reciente.
En caso de verificarse atrasos mayores a 31 días en el pago de los servicios de la deuda
refinanciada contados a partir de la inclusión del deudor en esta categoría, corresponderá
la reclasificación inmediata del deudor en el nivel que surja de considerar la cantidad total
de días resultante de sumar los días de atraso efectivamente registrados a partir de la
primera cuota impaga de la refinanciación y los de atraso mínimo establecidos normati-
vamente que correspondan a la categoría en la que se encuentre clasificado el deudor en
el mes en que se verifica el nuevo atraso.
```

## F04

- **Predicado:** `condicion_de`
- **Origen:** Condicion — «Elegibilidad para mecanismo de cobros de exportación» (`Condicion_elegibilidad_para_mecanismo_de_cobros_de_exportacion__los_cobros_deben_resultar__617b9e`)
  - descripción (salida del extractor): Los cobros deben resultar elegibles para el mecanismo previsto en el punto 7.10.3
  - tramo de E1 en la unidad (salida del extractor): 'que resulten elegibles para el mecanismo previsto en este punto'
- **Destino:** Operacion — «Depósito de cobros de exportación en cuentas corresponsales» (`Operacion_deposito_de_cobros_de_exportacion_en_cuentas_corresponsales__ext_7_10_3_c7b377`)
  - descripción (salida del extractor): Depósito de cobros de exportación de bienes elegibles para el mecanismo del punto, no aplicados simultáneamente a usos admitidos, en cuentas corresponsales en el exterior de entidades financieras locales y/o en cuentas locales en moneda extranjera de entidades financieras locales, hasta su aplicación
  - tramo de E1 en la unidad (salida del extractor): 'Los cobros de exportación de bienes recibidos por un exportador que resulten elegibles para el mecanismo previsto en este punto y no sean aplicados simultáneamente a los usos admitidos podrán quedar depositados hasta su aplicación en las cuentas corresponsales en el exterior de entidades financieras locales y/o en cuentas locales en moneda extranjera de entidades financieras locales'
- **Unidad:** `ext::7.10.3` (ext, punto 7.10.3, punto_propio)
- **Páginas:** unidad [102], arista [102]; PDF `data/experiment/subset/TO_exterior_cambios_actual.pdf`
- **Render:** `paginas/ext_p99.png`, `paginas/ext_p102.png`
- **Texto heredado:**
  - [encabezado, S7, p. [80]] Sección 7. Cobros de exportaciones de bienes.
  - [encabezado, 7.10, p. [99]] 7.10. Operaciones habilitadas para la aplicación de cobros de exportaciones de bienes en el marco
  - [intro, 7.10, p. [99]] del régimen de fomento de inversión para las exportaciones (Decreto 234/21).
- **Texto propio** («Los cobros de exportación de bienes recibidos por un exportador que resulten»):

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

## F05

- **Predicado:** `condicion_de`
- **Origen:** Condicion — «Conocimiento de composición del conjunto subyacente» (`Condicion_conocimiento_de_composicion_del_conjunto_subyacente__condicion_de_que_en_todo_mo_6bf156`)
  - descripción (salida del extractor): Condición de que en todo momento se conozca la composición del conjunto subyacente de exposiciones.
  - tramo de E1 en la unidad (salida del extractor): 'siempre que en todo momento se conozca la composición del conjunto subyacente de exposiciones'
- **Destino:** Potestad — «Aplicar tratamiento de transparencia (look-through)» (`Potestad_aplicar_tratamiento_de_transparencia_look_through__facultad_de_la_entidad_que_po_fde257`)
  - descripción (salida del extractor): Facultad de la entidad que posea o garantice una posición de máxima preferencia en titulización tradicional de aplicar tratamiento de transparencia (look-through) para determinar el ponderador de riesgo, siempre que se conozca la composición del conjunto subyacente y no sea retitulización.
  - tramo de E1 en la unidad (salida del extractor): 'La entidad que posea o garantice una posición de máxima preferencia en una titulización tradicional podrá aplicar el tratamiento de transparencia (look-through) para determinar el ponderador de riesgo, siempre que en todo momento se conozca la composición del conjunto subyacente de exposiciones y que no se trate de una retitulización.'
- **Unidad:** `cap::3.1.6` (cap, punto 3.1.6, punto_propio)
- **Páginas:** unidad [36, 37], arista [36, 37]; PDF `data/experiment/subset/TO_capitales_minimos_actual.pdf`
- **Render:** `paginas/cap_p29.png`, `paginas/cap_p36.png`, `paginas/cap_p37.png`
- **Texto heredado:**
  - [encabezado, S3, p. [29]] Sección 3. Capital mínimo por riesgo de crédito. Titulizaciones e inversiones en fon- dos.
  - [encabezado, 3.1, p. [29]] 3.1. Tratamiento de las titulizaciones.
  - [intro, 3.1, p. [29]] Se denomina “posición de titulización” a la exposición a una titulización (o retitulización), tradi- cional o sintética, o a una estructura con similares características. La exposición a los riesgos de una titulización puede surgir, entre otros, de los siguientes con- ceptos: tenencia de títulos valores emitidos en el marco de la titulización –es decir, títulos de deuda y/o certificados de participación, tales como bonos de titulización de activos (“Asset- Backed Securities”, ABS) y bonos de titulización hipotecaria (“Mortgage-Backed Securities”, MBS)–, mejoras crediticias, facilidades de liquidez, “swaps” de tasa de interés o de monedas y derivados de crédito. Las reservas (“reserve accounts”), tales como las cuentas de garantía en efectivo, se considerarán como un activo para la entidad financiera originante, recibiendo tam- bién el tratamiento de posiciones de titulización. Dado que las titulizaciones pueden estructurarse de diferentes formas, la exigencia de capital para una posición de titulización se determinará teniendo en cuenta su realidad o finalidad eco- nómica y no su forma jurídica. En los casos en que exista incertidumbre acerca de si una de- terminada operación debe considerarse como titulización, la entidad deberá aplicar el criterio que estime mejor se ajusta a la realidad económica de la operación e informar a la SEFyC los fundamentos que lo sustenten.
- **Texto propio** («Posiciones de titulización de máxima preferencia.»):

```text
3.1.6. Posiciones de titulización de máxima preferencia.
Se entiende por posición de titulización de máxima preferencia al tramo de los títulos va-
lores emitidos en la operación de titulización que se sitúa en el primer lugar de prelación
a los efectos de la percepción de los correspondientes pagos.
A efectos de determinar qué posición recibe el tratamiento de máxima preferencia podrá,
si así correspondiera por la realidad o finalidad económica de la operación, no conside-
rarse ciertas operaciones o derechos que, en sentido técnico, se adelantan en el orden
de prelación –tal es el caso de los swaps de tasa de interés y de monedas–.
Cuando los tramos de máxima preferencia compartan una asignación de pérdidas a pro-
rrata, la diferencia en sus plazos no será considerada, dado que dichos tramos se bene-
fician del mismo nivel de mejora crediticia.
Si un tramo de máxima preferencia fuera a su vez estratificado en tramos o cubierto par-
cialmente –de acuerdo con lo previsto en el punto 3.1.13.2.–, solamente la nueva parte
de máxima preferencia deberá ser tratada como tal.
Una facilidad de liquidez que respalde un programa ABCP no será la posición de máxima
preferencia en el programa, sino que lo será el título valor que cuenta con el respaldo de
la liquidez. En cambio, la facilidad será la posición de máxima preferencia si no se pue-
den transferir los fondos que generan los activos subyacentes a los restantes acreedores
hasta tanto se reintegre la facilidad de liquidez que se hubiese empleado para cubrir pér-
didas. En caso contrario o si por cualquier otra razón la facilidad de liquidez se encontra-
ra en una posición intermedia y no en la posición de máxima preferencia respecto de los
activos subyacentes, no deberá ser tratada como de máxima preferencia.
La entidad que posea o garantice una posición de máxima preferencia en una titulización
tradicional podrá aplicar el tratamiento de transparencia (look-through) para determinar el
ponderador de riesgo, siempre que en todo momento se conozca la composición del con-
junto subyacente de exposiciones y que no se trate de una retitulización.
En el tratamiento de transparencia, dicha posición de máxima preferencia recibirá un
ponderador igual al promedio ponderado de los ponderadores aplicables a las exposicio-
nes subyacentes.
```

## F06

- **Predicado:** `condicion_de`
- **Origen:** Condicion — «Constatación de cancelación desde fecha de vencimiento» (`Condicion_constatacion_de_cancelacion_desde_fecha_de_vencimiento__la_cancelacion_del_capit_f918a4`)
  - descripción (salida del extractor): La cancelación del capital, intereses y otros conceptos tuvo lugar a partir de la fecha de vencimiento.
  - tramo de E1 en la unidad (salida del extractor): 'constate que la cancelación tuvo lugar a partir de la fecha de vencimiento'
- **Destino:** Potestad — «Emitir certificaciones de aplicación — endeudamientos con exterior» (`Potestad_emitir_certificaciones_de_aplicacion_endeudamientos_con_exterior__la_entidad_pod_cd617d`)
  - descripción (salida del extractor): La entidad podrá emitir las certificaciones de aplicación de las divisas a la cancelación del capital, intereses y otros conceptos admitidos en endeudamientos financieros con el exterior admitidos en los puntos 7.9. o 7.10.
  - tramo de E1 en la unidad (salida del extractor): 'La entidad podrá emitir las certificaciones de aplicación de las divisas a la cancelación del capital, intereses y otros conceptos admitidos'
- **Unidad:** `ext::9.3.8` (ext, punto 9.3.8, punto_propio)
- **Páginas:** unidad [127], arista [127]; PDF `data/experiment/subset/TO_exterior_cambios_actual.pdf`
- **Render:** `paginas/ext_p124.png`, `paginas/ext_p127.png`
- **Texto heredado:**
  - [encabezado, S9, p. [123]] Sección 9. Seguimiento de anticipos y otras financiaciones de exportación de bienes.
  - [encabezado, 9.3, p. [124]] 9.3. Certificaciones de aplicación de cobros de exportaciones.
  - [intro, 9.3, p. [124]] A solicitud del exportador, la entidad encargada del seguimiento emitirá las certificaciones de aplicación en la medida que se verifiquen las condiciones previstas en los puntos 9.3.1. al 9.3.13. La entidad deberá dejar registradas las certificaciones de aplicación emitidas para cada una de las operaciones bajo su seguimiento.
- **Texto propio** («Endeudamientos financieros con el exterior admitidos en los puntos 7.9. o 7.10.»):

```text
9.3.8. Endeudamientos financieros con el exterior admitidos en los puntos 7.9. o 7.10.
La entidad podrá emitir las certificaciones de aplicación de las divisas a la
cancelación del capital, intereses y otros conceptos admitidos, en la medida que
verifique las condiciones indicadas en el punto 9.3.1., constate que la cancelación
tuvo lugar a partir de la fecha de vencimiento y cuente con la documentación que le
permita verificar el cumplimiento de los requisitos establecidos en los puntos 7.9. o
7.10., según corresponda.
```

## F07

- **Predicado:** `condicion_de`
- **Origen:** Condicion — «Habilitación de cuenta por depósito inicial» (`Condicion_habilitacion_de_cuenta_por_deposito_inicial__la_cuenta_debe_estar_habilitada_med_fd3547`)
  - descripción (salida del extractor): La cuenta debe estar habilitada mediante depósito inicial o autorización para girar en descubierto.
  - tramo de E1 en la unidad (salida del extractor): 'Habilitada la cuenta mediante el depósito inicial que se convenga o la correspondiente autorización para girar en descubierto'
- **Destino:** Operacion — «Entrega de cuadernos de cheques» (`Operacion_entrega_de_cuadernos_de_cheques__ctacte_1_4_6_77b2f6`)
  - descripción (salida del extractor): Entrega de cuadernos de cheques al cuentacorrentista bajo recibo, conforme a la normativa aplicable, una vez habilitada la cuenta mediante depósito inicial o autorización para girar en descubierto.
  - tramo de E1 en la unidad (salida del extractor): 'la entidad entregará al cuentacorrentista, bajo recibo, cuadernos de cheques'
- **Unidad:** `ctacte::1.4.6` (ctacte, punto 1.4.6, punto_propio)
- **Páginas:** unidad [8], arista [8]; PDF `data/experiment/escalado_prep/pdfs/ctacte.pdf`
- **Render:** `paginas/ctacte_p8.png`
- **Texto heredado:**
  - [encabezado, S1, p. [5]] Sección 1. Funcionamiento.
  - [encabezado, 1.4, p. [7]] 1.4. Condiciones.
- **Texto propio** («Entrega de cuadernos de cheques y autorización para librar ECHEQ.»):

```text
1.4.6. Entrega de cuadernos de cheques y autorización para librar ECHEQ.
Habilitada la cuenta mediante el depósito inicial que se convenga o la correspondiente
autorización para girar en descubierto, la entidad entregará al cuentacorrentista, bajo re-
cibo, cuadernos de cheques, conforme a la normativa aplicable.
Dichos cuadernos podrán estar constituidos con fórmulas de cheques comunes o de pa-
go diferido, exclusivamente, o bien contener ambos tipos de documentos.
Si el aludido cuaderno no fuere retirado personalmente por el titular de la cuenta, el gira-
do no pagará los cheques librados en formato papel que se presenten al cobro (cualquie-
ra fuese su clase) ni registrará los cheques de pago diferido librados en ese formato que
a tales efectos se le presenten, de no contarse con su conformidad respecto de la recep-
ción del citado elemento.
La entidad girada procederá al rechazo por defecto formal de cada uno de los cheques
que contenga la chequera respecto de la cual no se haya recibido la conformidad del titu-
lar sobre su recepción.
Se entregarán cuadernos de cheques en cantidad y/o se autorizará el libramiento de
ECHEQ por un importe global máximo, según corresponda, en función de lo que solicite
el cliente y en la medida en que se justifique por el movimiento de la cuenta. En el caso
del ECHEQ, la entidad girada informará al librador el importe total autorizado y el monto
disponible.
```

## F08

- **Predicado:** `condicion_de`
- **Origen:** Condicion — «Cartas de crédito emitidas a partir del 14/04/25» (`Condicion_cartas_de_credito_emitidas_a_partir_del_14_04_25__cartas_de_credito_o_letras_ava_259aa4`)
  - descripción (salida del extractor): Cartas de crédito o letras avaladas emitidas u otorgadas a partir del 14/04/25
  - tramo de E1 en la unidad (salida del extractor): 'Para aquellas emitidas u otorgadas a partir del 14/04/25'
- **Destino:** Potestad — «Admisión de pago desde fecha estimada de embarque» (`Potestad_admision_de_pago_desde_fecha_estimada_de_embarque__se_admitira_que_el_pago_garan_ba3ff0`)
  - descripción (salida del extractor): Se admitirá que el pago garantizado tuviera que ser concretado a partir de la fecha estimada de embarque de los bienes en origen cuando correspondía a la porción de una operación por la cual el cliente hubiese podido realizar pagos a la vista en virtud de lo previsto en los puntos 10.10.2.1. o 10.10.2.2
  - tramo de E1 en la unidad (salida del extractor): 'también se admitirá que el pago garantizado tuviera que ser concretado a partir de la fecha estimada de embarque de los bienes en origen cuando correspondía a la porción de una operación por la cual el cliente hubiese podido realizar pagos a la vista en virtud de lo previsto en los puntos 10.10.2.1. o 10.10.2.2.'
- **Unidad:** `ext::10.4.4` (ext, punto 10.4.4, punto_propio)
- **Páginas:** unidad [142, 143], arista [142, 143]; PDF `data/experiment/subset/TO_exterior_cambios_actual.pdf`
- **Render:** `paginas/ext_p142.png`, `paginas/ext_p143.png`
- **Texto heredado:**
  - [encabezado, S10, p. [130]] Sección 10. Pagos de importaciones y otras compras de bienes en el exterior.
  - [encabezado, 10.4, p. [138]] 10.4. Pagos de importaciones de bienes con registro de ingreso aduanero pendiente.
- **Texto propio** («Cancelación de garantías comerciales de importaciones de bienes otorgadas por»):

```text
10.4.4. Cancelación de garantías comerciales de importaciones de bienes otorgadas por
entidades financieras locales.
La entidad tendrá acceso al mercado de cambios para cancelar cartas de crédito o
letras avaladas emitidas u otorgadas para garantizar operaciones de importaciones
de bienes que tengan el registro aduanero pendiente, incluso cuando no se cumplan
los requisitos establecidos para el acceso del cliente, en la medida que se verifique
que se cumplían las condiciones que resultaban aplicables según la fecha en que se
emitió u otorgó la carta de crédito o letra avalada y el tipo de operación garantizada
por la entidad.
En el caso de cartas de crédito o letras avaladas emitidas u otorgadas a partir del
13/12/23, la entidad deberá contar con la documentación que demuestre que, al
momento de la apertura o emisión, la operación garantizada correspondía a una
importación de bienes con registro de ingreso aduanero a partir de dicha fecha y,
salvo que la operación quedase comprendida en la situación prevista en el punto
10.10.2.11., que el pago garantizado debía ser concretado por el cliente a partir de la
fecha que resultaba de adicionar el plazo en días corridos que le correspondía al bien
por el punto 10.10.1. más otros 15 (quince) días corridos a la fecha estimada de
arribo de los bienes al país.
Para aquellas emitidas u otorgadas a partir del 14/04/25, en la medida que se
cumplan las restantes condiciones, también se admitirá que el pago garantizado
tuviera que ser concretado a partir de la fecha estimada de embarque de los bienes
en origen cuando correspondía a la porción de una operación por la cual el cliente
hubiese podido realizar pagos a la vista en virtud de lo previsto en los puntos
10.10.2.1. o 10.10.2.2.
Las condiciones aplicables para las cartas de crédito o letras avaladas emitidas u
otorgadas hasta el 12/12/23 fueron oportunamente receptadas en el punto 10.3.6. del
Anexo de la Comunicación A 7914.
El boleto de venta deberá efectuarse a nombre de la propia entidad en calidad de
cliente por el concepto “B11. Cancelación de garantías comerciales de entidades
financieras de importaciones de bienes sin registro de ingreso aduanero”.
Por los pagos que se realicen, la entidad deberá informar en el SEPAIMPO dentro de
los 5 (cinco) días hábiles, la CUIT del importador por el cual se ha efectuado el pago.
En la medida que la entidad no cuente con el registro de la oficialización del
despacho de importación dentro de los 90 (noventa) días corridos de la fecha de
acceso al mercado de cambios, la entidad deberá efectuar la correspondiente
denuncia.
```

## F09

- **Predicado:** `condicion_de`
- **Origen:** Condicion — «Condición: fondos no computables en mercado cambios» (`Condicion_condicion_fondos_no_computables_en_mercado_cambios__la_totalidad_de_los_fondos_o_45cf5b`)
  - descripción (salida del extractor): La totalidad de los fondos obtenidos por la financiación no puede ser computada como ingresada y liquidada en el mercado de cambios
  - tramo de E1 en la unidad (salida del extractor): 'En el caso de que la totalidad de los fondos obtenidos por la financiación no pudiese ser computada como ingresada y liquidada en el mercado de cambios'
- **Destino:** Potestad — «Facultad acceso VPU sin conformidad previa BCRA» (`Potestad_facultad_acceso_vpu_sin_conformidad_previa_bcra__las_entidades_pueden_dar_acceso_c3a889`)
  - descripción (salida del extractor): Las entidades pueden dar acceso al VPU adherido sin necesidad de contar con la conformidad previa del BCRA si tal requisito estuviese vigente
  - tramo de E1 en la unidad (salida del extractor): 'las entidades también podrán dar acceso al VPU adherido, sin necesidad de contar con la conformidad previa del BCRA si tal requisito estuviese vigente'
- **Unidad:** `ext::14.2.1::cierre` (ext, punto 14.2.1, bloque_cierre)
- **Páginas:** unidad [177], arista [177]; PDF `data/experiment/subset/TO_exterior_cambios_actual.pdf`
- **Render:** `paginas/ext_p177.png`
- **Texto heredado:**
  - [encabezado, S14, p. [175]] Sección 14. Disposiciones complementarias asociadas al Régimen de Incentivo para Grandes Inversiones (RIGI).
  - [encabezado, 14.2, p. [176]] 14.2. Beneficios relacionados con el acceso al mercado de cambios para operaciones de egreso.
  - [encabezado, 14.2.1, p. [176]] 14.2.1. En el marco de lo dispuesto en los puntos 3.3., 3.5., 3.6. y 10.3.2., según
- **Texto propio** («[bloque cierre] En el marco de lo dispuesto en los puntos 3.3., 3.5., 3.6. y 10.3.2., según»):

```text
En el caso de que la totalidad de los fondos obtenidos por la financiación no pudiese
ser computada como ingresada y liquidada en el mercado de cambios, las
entidades también podrán dar acceso al VPU adherido, sin necesidad de contar con
la conformidad previa del BCRA si tal requisito estuviese vigente, para realizar:
i) pagos de intereses devengados hasta la fecha de acceso que se encuentren
impagos y que correspondan a la porción del capital equivalente a la proporción
de los fondos recibidos por el VPU por la financiación que puede computarse
como ingresada y liquidada por el mercado de cambios.
ii) pagos por capital adeudado que corresponda a la porción del capital
equivalente a la proporción de los fondos recibidos por el VPU por la
financiación que puede computarse como ingresada y liquidada por el mercado
de cambios.
```

## F10

- **Predicado:** `condicion_de`
- **Origen:** Condicion — «Plazo mínimo 2 años — aporte 02/10/20 a 20/04/25» (`Condicion_plazo_minimo_2_anos_aporte_02_10_20_a_20_04_25__la_repatriacion_debe_tener_lugar_63a203`)
  - descripción (salida del extractor): La repatriación debe tener lugar como mínimo 2 años después de su liquidación si el aporte fue ingresado y liquidado entre el 02/10/20 y el 20/04/25
  - tramo de E1 en la unidad (salida del extractor): 'la repatriación tenga lugar como mínimo 2 (dos) años después de su liquidación si el aporte fue ingresado y liquidado entre el 02/10/20 y el 20/04/25'
- **Destino:** Operacion — «Repatriación inversión directa no residentes» (`Operacion_repatriacion_inversion_directa_no_residentes__ext_3_13_1_7_fa6676`)
  - descripción (salida del extractor): Repatriación de inversiones directas de no residentes en empresas que no sean controlantes de entidades financieras locales, de un aporte de capital ingresado y liquidado por el mercado de cambios a partir del 02/10/20
  - tramo de E1 en la unidad (salida del extractor): 'Repatriaciones de inversiones directas de no residentes en empresas que no sean controlantes de entidades financieras locales de un aporte de capital que haya sido ingresado y liquidado por el mercado de cambios a partir del 02/10/20'
- **Unidad:** `ext::3.13.1.7` (ext, punto 3.13.1.7, punto_propio)
- **Páginas:** unidad [37], arista [37]; PDF `data/experiment/subset/TO_exterior_cambios_actual.pdf`
- **Render:** `paginas/ext_p16.png`, `paginas/ext_p36.png`, `paginas/ext_p37.png`, `paginas/ext_p39.png`
- **Texto heredado:**
  - [encabezado, S3, p. [16]] Sección 3. Disposiciones específicas para los egresos por el mercado de cambios
  - [chapeau_seccion, S3, p. [16]] Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–, adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables.
  - [encabezado, 3.13, p. [36]] 3.13. Repatriaciones de inversiones directas y otras compras de moneda extranjera por parte de no
  - [intro, 3.13, p. [36]] residentes
  - [encabezado, 3.13.1, p. [36]] 3.13.1. El acceso al mercado de cambios para la repatriación de inversiones de no
  - [intro, 3.13.1, p. [36]] residentes y otras compras de moneda extranjera por parte de clientes no residentes requerirá la conformidad previa del BCRA, excepto para las operaciones de:
  - [cierre, 3.13.1, p. [39]] Si una repatriación de una inversión directa de no residentes consiste en una reducción de capital y/o devolución de aportes irrevocables realizadas por la empresa local, adicionalmente a los requisitos previstos en cada caso, la entidad deberá contar con la documentación que demuestre que se han cumplimentado los mecanismos legales previstos y haber verificado que se encuentra declarada, en caso de corresponder, en la última presentación vencida del “Relevamiento de activos y pasivos externos” el pasivo en pesos con el exterior generado a partir de la fecha de la no aceptación del aporte irrevocable o de la reducción de capital según corresponda.
- **Texto propio** («Repatriaciones de inversiones directas de no residentes en empresas que»):

```text
3.13.1.7. Repatriaciones de inversiones directas de no residentes en empresas que
no sean controlantes de entidades financieras locales de un aporte de
capital que haya sido ingresado y liquidado por el mercado de cambios a
partir del 02/10/20 en la medida que:
i) la repatriación tenga lugar como mínimo 180 (ciento ochenta) días
corridos después de la liquidación de los fondos del aporte si el
aporte fue ingresado y liquidado a partir del 21/04/25; o
ii) la repatriación tenga lugar como mínimo 2 (dos) años después de su
liquidación si el aporte fue ingresado y liquidado entre el 02/10/20 y el
20/04/25.
```

## F11

- **Predicado:** `condicion_de`
- **Origen:** Condicion — «Imposibilidad de determinar precio definitivo» (`Condicion_imposibilidad_de_determinar_precio_definitivo__supuesto_en_que_al_vencimiento_de_eb874d`)
  - descripción (salida del extractor): Supuesto en que al vencimiento del plazo no ha sido posible determinar el precio definitivo de los bienes por causas ajenas a la voluntad del exportador
  - tramo de E1 en la unidad (salida del extractor): 'Cuando al vencimiento del plazo no haya sido posible, por causas ajenas a la voluntad del exportador, determinar el precio definitivo de los bienes comprendidos en la operación'
- **Destino:** Potestad — «Extensión del plazo hasta 120 días — indeterminación de precio» (`Potestad_extension_del_plazo_hasta_120_dias_indeterminacion_de_precio__la_entidad_esta_fa_217734`)
  - descripción (salida del extractor): La entidad está facultada a extender el plazo para la liquidación de divisas hasta 120 días corridos contados desde la fecha de cumplido de embarque que figura en el permiso de embarque provisorio, cuando no haya sido posible determinar el precio definitivo por causas ajenas a la voluntad del exportador
  - tramo de E1 en la unidad (salida del extractor): 'la entidad podrá extender el plazo hasta los 120 (ciento veinte) días corridos a contar desde la fecha de cumplido de embarque que figura en el permiso de embarque provisorio'
- **Unidad:** `ext::7.5.5::intro` (ext, punto 7.5.5, bloque_intro)
- **Páginas:** unidad [87], arista [87]; PDF `data/experiment/subset/TO_exterior_cambios_actual.pdf`
- **Render:** `paginas/ext_p87.png`
- **Texto heredado:**
  - [encabezado, S7, p. [80]] Sección 7. Cobros de exportaciones de bienes.
  - [encabezado, 7.5, p. [86]] 7.5. Ampliaciones del plazo para el ingreso y liquidación de divisas.
  - [encabezado, 7.5.5, p. [87]] 7.5.5. Indeterminación del precio definitivo en exportaciones bajo los regímenes de precios
- **Texto propio** («[bloque intro] Indeterminación del precio definitivo en exportaciones bajo los regímenes de precios»):

```text
revisables o concentrados de minerales.
Cuando al vencimiento del plazo no haya sido posible, por causas ajenas a la voluntad
del exportador, determinar el precio definitivo de los bienes comprendidos en la opera-
ción, la entidad podrá extender el plazo hasta los 120 (ciento veinte) días corridos a
contar desde la fecha de cumplido de embarque que figura en el permiso de embarque
provisorio.
Para ello la entidad encargada del seguimiento deberá verificar el cumplimiento de las
siguientes condiciones:
```

## F12

- **Predicado:** `condicion_de`
- **Origen:** Condicion — «Contraparte en operaciones de arbitraje y canje» (`Condicion_contraparte_en_operaciones_de_arbitraje_y_canje__la_operacion_de_arbitraje_o_can_71c78d`)
  - descripción (salida del extractor): La operación de arbitraje o canje en el exterior solo puede realizarse cuando la contraparte reúne determinadas características (que se especifican en los ítems siguientes)
  - tramo de E1 en la unidad (salida del extractor): 'siempre que la contraparte sea:'
- **Destino:** Potestad — «Facultad realizar arbitrajes y canjes en exterior» (`Potestad_facultad_realizar_arbitrajes_y_canjes_en_exterior__las_entidades_autorizadas_que_cab9aa`)
  - descripción (salida del extractor): Las entidades autorizadas quedan facultadas a realizar operaciones de arbitrajes y canjes en el exterior
  - tramo de E1 en la unidad (salida del extractor): 'Dichas entidades podrán realizar operaciones de arbitrajes y canjes en el exterior'
- **Unidad:** `ext::5.12::intro` (ext, punto 5.12, bloque_intro)
- **Páginas:** unidad [73], arista [73]; PDF `data/experiment/subset/TO_exterior_cambios_actual.pdf`
- **Render:** `paginas/ext_p73.png`
- **Texto heredado:**
  - [encabezado, S5, p. [68]] Sección 5. Pautas operativas.
  - [encabezado, 5.12, p. [73]] 5.12. Operaciones de arbitrajes y canjes en el exterior de las entidades.
- **Texto propio** («[bloque intro] Operaciones de arbitrajes y canjes en el exterior de las entidades.»):

```text
Dichas entidades podrán realizar operaciones de arbitrajes y canjes en el exterior siempre que
la contraparte sea:
```

## F13

- **Predicado:** `condicion_de`
- **Origen:** Condicion — «Pago del 5% de obligaciones refinanciadas sin atrasos superiores a 31 días» (`Condicion_pago_del_5_de_obligaciones_refinanciadas_sin_atrasos_superiores_a_31_dias__se_ha_75360e`)
  - descripción (salida del extractor): Se ha pagado sin atrasos superiores a 31 días al menos el 5% de las obligaciones refinanciadas y la totalidad de los intereses devengados, más el porcentaje acumulado que correspondería si la refinanciación se hubiera otorgado en categorías inferiores
  - tramo de E1 en la unidad (salida del extractor): 'Cuando al menos se haya cumplido con el pago, sin haber incurrido en atrasos superiores a 31 días, del 5 % de las obligaciones refinanciadas y la totalidad de los intereses devengados, con más el porcentaje acumulado que pudiera corresponder si la refinanciación se hubiera otorgado de haberse encontrado el deudor en categorías inferiores'
- **Destino:** Potestad — «Reclasificación a niveles superiores si se cumplen condiciones» (`Potestad_reclasificacion_a_niveles_superiores_si_se_cumplen_condiciones__la_entidad_podra_2b469f`)
  - descripción (salida del extractor): La entidad podrá reclasificar al deudor en niveles superiores (en observación o en situación normal) si se observan las otras condiciones previstas en la correspondiente categoría
  - tramo de E1 en la unidad (salida del extractor): 'podrá reclasificárselo en niveles superiores ("en observación" o "en situación normal") si, además, se observan las otras condiciones previstas en la correspondiente categoría'
- **Unidad:** `cla::6.5.3.5` (cla, punto 6.5.3.5, punto_propio)
- **Páginas:** unidad [24], arista [24]; PDF `data/experiment/subset/TO_clasificacion_deudores_actual.pdf`
- **Render:** `paginas/cla_p19.png`, `paginas/cla_p23.png`, `paginas/cla_p24.png`
- **Texto heredado:**
  - [encabezado, S6, p. [17]] Sección 6. Clasificación de los deudores de la cartera comercial.
  - [encabezado, 6.5, p. [19]] 6.5. Niveles de clasificación.
  - [intro, 6.5, p. [19]] Cada cliente, y la totalidad de sus financiaciones comprendidas, se incluirá en una de las si- guientes cinco categorías, las que se definen teniendo en cuenta las condiciones que se deta- llan en cada caso. Los clientes que no registren asistencia crediticia de la entidad y que posteriormente reciban fi- nanciaciones de ésta que no superen el importe resultante de aplicar sobre el saldo de deuda registrado en el sistema financiero, según la última información disponible en la “Central de deudores” a la fecha de su otorgamiento, el porcentaje establecido en el punto 2.2.5. de las normas sobre “Previsiones mínimas por riesgo de incobrabilidad” correspondiente a la peor cla- sificación asignada, podrán ser clasificados por la entidad teniendo en cuenta únicamente el análisis del flujo de fondos proyectado. Las asistencias así otorgadas no serán consideradas a los fines a que se refiere el punto 6.6. A fin de verificar el cumplimiento de las obligaciones sin recurrir a nueva financiación directa o indirecta o a refinanciaciones, no se considerarán refinanciaciones las facilidades adicionales que se otorguen respecto de los márgenes vigentes acordados, siempre que el nuevo apoyo crediticio implique nuevos desembolsos de fondos y no supere el 10 % del cupo asignado en oportunidad de la última evaluación crediticia del cliente, en la medida en que éstas sean con- sistentes con el curso normal de los negocios y exista capacidad para atender el resto de las obligaciones financieras, ni las nuevas financiaciones y las refinanciaciones asociadas a una mayor inversión derivada de la expansión de las actividades, y siempre que pueda demostrarse que el flujo de fondos proyectado permitirá afrontar la totalidad de sus obligaciones. Tampoco se considerarán dentro de ese concepto las refinanciaciones otorgadas a los produc- tores agropecuarios cuando ello resulte de la aplicación de disposiciones vinculadas a la Ley de Emergencia Agropecuaria, sin perjuicio de lo cual, a los fines de la clasificación, deberá tenerse en cuenta el flujo de fondos proyectado para el momento en que concluya la vigencia de la emergencia declarada. El tratamiento que se dispense en ese marco no podrá implicar mejora- miento de la clasificación asignada al cliente en función de su situación individual, preexistente a la emergencia, ni su aplicación extenderse más allá de la vigencia fijada para ella.
  - [encabezado, 6.5.3, p. [23]] 6.5.3. Con problemas.
  - [intro, 6.5.3, p. [23]] El análisis del flujo de fondos del cliente demuestra que tiene problemas para atender normalmente la totalidad de sus compromisos financieros y que, de no ser corregidos, esos problemas pueden resultar en una pérdida para la entidad financiera. Entre los indicadores que pueden reflejar esta situación se destacan que el cliente:
- **Texto propio** («Cuente con refinanciaciones reiteradas y sistemáticas del capital adeudado vin-»):

```text
6.5.3.5. Cuente con refinanciaciones reiteradas y sistemáticas del capital adeudado vin-
culadas a una insuficiente capacidad para su pago aun cuando abone los intere-
ses y siempre que no haya quitas en el capital, que no se reduzcan las tasas de
interés pactadas –salvo que ello derive de las condiciones del mercado– o que
no sea necesario aceptar bienes en pago de parte de las obligaciones.
Cuando al menos se haya cumplido con el pago, sin haber incurrido en atrasos
superiores a 31 días, del 5 % de las obligaciones refinanciadas y la totalidad de
los intereses devengados, con más el porcentaje acumulado que pudiera co-
rresponder si la refinanciación se hubiera otorgado de haberse encontrado el
deudor en categorías inferiores, podrá reclasificárselo en niveles superiores (“en
observación” o “en situación normal”) si, además, se observan las otras condi-
ciones previstas en la correspondiente categoría.
El deudor que, encontrándose clasificado en esta categoría, haya refinanciado
su deuda –aun cuando haya cancelado el porcentaje establecido en el párrafo
precedente– y recibido crédito adicional en los términos a que se refiere el punto
2.2.5. de las normas sobre “Previsiones mínimas por riesgo de incobrabilidad”, y
en la medida en que dicha financiación adicional no hubiese sido cancelada, de-
berá permanecer en esta categoría por lo menos 180 días contados desde la fe-
cha en que se otorgó crédito adicional o desde que se celebró el acuerdo de re-
financiación, la circunstancia más reciente. Ello, salvo que por aplicación de
otras pautas corresponda categorizarlo en el nivel inferior.
```

## F14

- **Predicado:** `condicion_de`
- **Origen:** Condicion — «Observancia de medidas mínimas de seguridad» (`Condicion_observancia_de_medidas_minimas_de_seguridad__la_exhibicion_del_dni_d_en_formato__1c5c29`)
  - descripción (salida del extractor): La exhibición del DNI-d en formato credencial virtual está condicionada a la observancia de las disposiciones sobre medidas mínimas de seguridad en entidades financieras
  - tramo de E1 en la unidad (salida del extractor): 'en la medida que se observen las disposiciones contenidas en el punto 2.12. de las normas sobre "Medidas mínimas de seguridad en entidades financieras"'
- **Destino:** Potestad — «Exhibición de DNI-d en formato credencial virtual» (`Potestad_exhibicion_de_dni_d_en_formato_credencial_virtual__el_dni_d_en_formato_credencia_7b399e`)
  - descripción (salida del extractor): El DNI-d en formato credencial virtual para dispositivos móviles inteligentes podrá ser exhibido en las casas operativas de las entidades financieras, sujeto a observancia de disposiciones sobre medidas mínimas de seguridad
  - tramo de E1 en la unidad (salida del extractor): 'El DNI-d en formato credencial virtual para dispositivos móviles inteligentes podrá ser exhibido en las casas operativas de las entidades financieras en la medida que se observen las disposiciones contenidas en el punto 2.12. de las normas sobre "Medidas mínimas de seguridad en entidades financieras"'
- **Unidad:** `docvig::2.2.3` (docvig, punto 2.2.3, punto_propio)
- **Páginas:** unidad [5], arista [5]; PDF `data/experiment/escalado_prep/pdfs/docvig.pdf`
- **Render:** `paginas/docvig_p5.png`
- **Texto heredado:**
  - [encabezado, S2, p. [4]] Sección 2. Para extranjeros
  - [encabezado, 2.2, p. [4]] 2.2. Mayores de 75 años al 31.12.14 y los incapaces declarados judicialmente.
- **Texto propio** («A partir del año de otorgada la residencia permanente o temporaria en el país.»):

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

## F15

- **Predicado:** `condicion_de`
- **Origen:** Condicion — «Plazo según proporción — bienes mixtos» (`Condicion_plazo_segun_proporcion_bienes_mixtos__cuando_un_pago_anticipado_incluye_tanto_bi_493546`)
  - descripción (salida del extractor): Cuando un pago anticipado incluye tanto bienes de capital como otros bienes, se aplica el plazo del tipo de bien que represente mayor proporción del valor total abonado
  - tramo de E1 en la unidad (salida del extractor): 'En el caso de que un mismo pago anticipado incluya bienes de capital y bienes que no lo son, la operación se regirá por el plazo del tipo de bien que represente una mayor proporción del valor total abonado'
- **Destino:** Operacion — «Acceso al mercado de cambios para pago anticipado» (`Operacion_acceso_al_mercado_de_cambios_para_pago_anticipado__ext_10_4_2_e7eb03`)
  - descripción (salida del extractor): Acceso al mercado de cambios para el pago al exterior de importaciones con registro de ingreso aduanero pendiente
  - tramo de E1 en la unidad (salida del extractor): 'dar acceso al mercado de cambios para el pago al exterior'
- **Unidad:** `ext::10.4.2.4` (ext, punto 10.4.2.4, punto_propio)
- **Páginas:** unidad [139, 140], arista [139, 140]; PDF `data/experiment/subset/TO_exterior_cambios_actual.pdf`
- **Render:** `paginas/ext_p139.png`, `paginas/ext_p140.png`
- **Texto heredado:**
  - [encabezado, S10, p. [130]] Sección 10. Pagos de importaciones y otras compras de bienes en el exterior.
  - [encabezado, 10.4, p. [138]] 10.4. Pagos de importaciones de bienes con registro de ingreso aduanero pendiente.
  - [encabezado, 10.4.2, p. [139]] 10.4.2. Requisitos de acceso para el pago anticipado de importaciones.
  - [intro, 10.4.2, p. [139]] La entidad podrá dar acceso al mercado de cambios para el pago al exterior en la medida que verifique previamente que se cumplen la totalidad de los siguientes requisitos:
- **Texto propio** («Cuenta con la declaración jurada del cliente de que se compromete a»):

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

## F16

- **Predicado:** `condicion_de`
- **Origen:** Condicion — «Cumplimiento de normas sobre evaluaciones crediticias» (`Condicion_cumplimiento_de_normas_sobre_evaluaciones_crediticias__los_bancos_emisores_de_la_419328`)
  - descripción (salida del extractor): Los bancos emisores de las cartas de crédito deben cumplir con lo previsto en el punto 3.1. de las normas sobre Evaluaciones crediticias.
  - tramo de E1 en la unidad (salida del extractor): 'que cumplan con lo previsto en el punto 3.1. de las normas sobre "Evaluaciones crediticias"'
- **Destino:** Operacion — «Financiación a residentes garantizada por cartas de crédito stand-by» (`Operacion_financiacion_a_residentes_garantizada_por_cartas_de_credito_stand_by__polcre_2_1_6eb0e0`)
  - descripción (salida del extractor): Financiación a residentes del país garantizada por cartas de crédito stand-by emitidas por bancos del exterior o bancos multilaterales de desarrollo que cumplan con lo previsto en el punto 3.1. de las normas sobre Evaluaciones crediticias, requiriendo calificación internacional de riesgo investment grade, en la medida en que dichas cartas de crédito sean irrestrictas y que la acreditación de los fondos se efectúe en forma inmediata a simple requerimiento de la entidad beneficiaria.
  - tramo de E1 en la unidad (salida del extractor): 'Financiaciones a residentes del país que se encuentren garantizadas por cartas de crédito ("stand-by letters of credit") emitidas por bancos del exterior o bancos multilaterales de desarrollo'
- **Unidad:** `polcre::2.1.17` (polcre, punto 2.1.17, punto_propio)
- **Páginas:** unidad [8], arista [8]; PDF `data/experiment/escalado_prep/pdfs/polcre.pdf`
- **Render:** `paginas/polcre_p6.png`, `paginas/polcre_p8.png`, `paginas/polcre_p9.png`
- **Texto heredado:**
  - [encabezado, S2, p. [6]] Sección 2. Aplicación de la capacidad de préstamo de depósitos en moneda extranjera.
  - [encabezado, 2.1, p. [6]] 2.1. Destinos.
  - [intro, 2.1, p. [6]] La capacidad de préstamo de los depósitos en moneda extranjera deberá aplicarse, en la co- rrespondiente moneda de captación, en forma indistinta, a los siguientes destinos:
  - [cierre, 2.1, p. [8]] La aplicación de la capacidad de préstamo de depósitos en moneda extranjera a los destinos vinculados a operaciones de importación (previstos en los puntos 2.1.6., 2.1.7. y la parte atri- buible a éstos por aplicación de los puntos 2.1.8. y 2.1.9.), no podrá superar el valor que resulte de la siguiente expresión: C max (F / C ; 0,05)
  - [cierre, 2.1, p. [8]] x
  - [cierre, 2.1, p. [8]] t base base
  - [cierre, 2.1, p. [8]] Siendo: C: capacidad de préstamo del mes al que corresponda.
  - [cierre, 2.1, p. [8]] t
  - [cierre, 2.1, p. [9]] F : financiación de importaciones comprendidas, correspondientes al trimestre agos- base
  - [cierre, 2.1, p. [9]] to/octubre de 2008.
  - [cierre, 2.1, p. [9]] C : capacidad de préstamo que corresponda al trimestre agosto/octubre de 2008.
  - [cierre, 2.1, p. [9]] base
  - [cierre, 2.1, p. [9]] Las financiaciones y capacidad de préstamo deberán ser computadas de acuerdo con lo esta- blecido en el punto 2.5.
- **Texto propio** («Financiaciones a residentes del país que se encuentren garantizadas por cartas de»):

```text
2.1.17. Financiaciones a residentes del país que se encuentren garantizadas por cartas de
crédito (“stand-by letters of credit”) emitidas por bancos del exterior o bancos multilate-
rales de desarrollo que cumplan con lo previsto en el punto 3.1. de las normas sobre
“Evaluaciones crediticias”, requiriendo a ese efecto calificación internacional de riesgo
“investment grade”, en la medida en que dichas cartas de crédito sean irrestrictas y que
la acreditación de los fondos se efectúe en forma inmediata a simple requerimiento de
la entidad beneficiaria.
```

## F17

- **Predicado:** `condicion_de`
- **Origen:** Condicion — «BCRA revoca autorización para funcionar» (`Condicion_bcra_revoca_autorizacion_para_funcionar__condicion_de_que_el_bcra_revoque_la_aut_5ff671`)
  - descripción (salida del extractor): Condición de que el BCRA revoque la autorización para funcionar de la entidad
  - tramo de E1 en la unidad (salida del extractor): 'revoque su autorización para funcionar'
- **Destino:** Operacion — «Emisión de nuevas acciones» (`Operacion_emision_de_nuevas_acciones__cap_8_3_4_4_dc4307`)
  - descripción (salida del extractor): Emisión de nuevas acciones como consecuencia de la ocurrencia de alguno de los eventos desencadenantes
  - tramo de E1 en la unidad (salida del extractor): 'La emisión de nuevas acciones como consecuencia de haberse producido alguno de tales eventos'
- **Unidad:** `cap::8.3.4.4` (cap, punto 8.3.4.4, punto_propio)
- **Páginas:** unidad [160], arista [160]; PDF `data/experiment/subset/TO_capitales_minimos_actual.pdf`
- **Render:** `paginas/cap_p159.png`, `paginas/cap_p160.png`
- **Texto heredado:**
  - [encabezado, S8, p. [154]] Sección 8. Responsabilidad patrimonial computable.
  - [encabezado, 8.3, p. [156]] 8.3. Criterios relacionados con los conceptos computables.
  - [encabezado, 8.3.4, p. [159]] 8.3.4. Requisitos adicionales que los instrumentos a que se refieren los puntos 8.3.2. y 8.3.3.
  - [intro, 8.3.4, p. [159]] deberán observar para garantizar su capacidad de absorción de pérdidas.
- **Texto propio** («Eventos desencadenantes.»):

```text
8.3.4.4. Eventos desencadenantes.
La circunstancia que tornará operativa la disposición a que se refiere el punto
8.3.4.1. tendrá lugar cuando suceda alguno de los eventos que a continuación
se detallan:
i) estando afectada la solvencia y/o liquidez de la entidad financiera el Banco
Central de la República Argentina rechace el plan de regularización y sa-
neamiento que aquella presente –artículo 34 de la Ley de Entidades Finan-
cieras– o revoque su autorización para funcionar –artículo 44 inciso c) de la
Ley de Entidades Financieras– o autorice su reestructuración en defensa
de los depositantes –artículo 35 bis de la Ley de Entidades Financieras,
primer párrafo–, lo que ocurra primero; o
ii) la decisión de capitalizar a la entidad financiera con fondos públicos –o una
medida de apoyo equivalente proporcionada por el Sistema de Seguro de
Garantía de los Depósitos–, en el marco de la aplicación del artículo 35 bis
de la Ley de Entidades Financieras por verse afectada su liquidez y solven-
cia.
La emisión de nuevas acciones como consecuencia de haberse producido al-
guno de tales eventos debe realizarse con anterioridad a cualquier capitaliza-
ción con fondos públicos –o medida de apoyo equivalente– a que se refiere el
apartado ii).
```

## F18

- **Predicado:** `condicion_de`
- **Origen:** Condicion — «Cumplimiento de condiciones del punto 3.11.3.» (`Condicion_cumplimiento_de_condiciones_del_punto_3_11_3__se_requiere_el_cumplimiento_de_las_7d6a58`)
  - descripción (salida del extractor): Se requiere el cumplimiento de las condiciones previstas en el punto 3.11.3. para acceder al mercado.
  - tramo de E1 en la unidad (salida del extractor): 'en la medida que se cumplan las condiciones previstas en el punto 3.11.3.'
- **Destino:** Potestad — «Acceso al mercado para compra de moneda extranjera» (`Potestad_acceso_al_mercado_para_compra_de_moneda_extranjera__los_residentes_con_endeudami_275d27`)
  - descripción (salida del extractor): Los residentes con endeudamientos comprendidos en el punto 7.9.1. y originados a partir del 07/01/21 (únicamente a partir del 08/08/25 en el caso de aquellos comprendidos en el punto 7.9.1.4.) o los fideicomisos constituidos en el país para garantizar la atención de los servicios de capital e intereses de tales endeudamientos, quedan autorizados a acceder al mercado para la compra de moneda extranjera para la constitución de garantías.
  - tramo de E1 en la unidad (salida del extractor): 'podrán acceder al mercado, en la medida que se cumplan las condiciones previstas en el punto 3.11.3., para la compra de moneda extranjera'
- **Unidad:** `ext::7.9.6` (ext, punto 7.9.6, punto_propio)
- **Páginas:** unidad [99], arista [99]; PDF `data/experiment/subset/TO_exterior_cambios_actual.pdf`
- **Render:** `paginas/ext_p94.png`, `paginas/ext_p99.png`
- **Texto heredado:**
  - [encabezado, S7, p. [80]] Sección 7. Cobros de exportaciones de bienes.
  - [encabezado, 7.9, p. [94]] 7.9. Operaciones financieras habilitadas para aplicar cobros de exportaciones de bienes y
  - [intro, 7.9, p. [94]] servicios.
- **Texto propio** («Los residentes con endeudamientos comprendidos en el punto 7.9.1. y originados a»):

```text
7.9.6. Los residentes con endeudamientos comprendidos en el punto 7.9.1. y originados a
partir del 07/01/21 (únicamente a partir del 08/08/25 en el caso de aquellos
comprendidos en el punto 7.9.1.4.) o los fideicomisos constituidos en el país para
garantizar la atención de los servicios de capital e intereses de tales endeudamientos,
podrán acceder al mercado, en la medida que se cumplan las condiciones previstas en
el punto 3.11.3., para la compra de moneda extranjera para la constitución de las
garantías en cuentas en moneda extranjera abiertas en entidades financieras locales o
en el exterior -cuando se trate de un endeudamiento financiero comprendido en el
punto 3.5.-, por los montos exigibles en los contratos de endeudamiento.
```

## F19

- **Predicado:** `condicion_de`
- **Origen:** Condicion — «Elegibilidad según punto 4.5» (`Condicion_elegibilidad_segun_punto_4_5__la_operacion_debe_resultar_elegible_de_acuerdo_con_01f3cb`)
  - descripción (salida del extractor): La operación debe resultar elegible de acuerdo con lo dispuesto en el punto 4.5
  - tramo de E1 en la unidad (salida del extractor): 'que resultaban elegibles de acuerdo con lo dispuesto en el punto 4.5'
- **Destino:** Operacion — «Pago deudas comerciales importaciones servicios» (`Operacion_pago_deudas_comerciales_importaciones_servicios__ext_4_8_1_2_0abf53`)
  - descripción (salida del extractor): Pago de deudas comerciales por importaciones de servicios prestados o devengados hasta el 12/12/23, que resultaban elegibles de acuerdo con lo dispuesto en el punto 4.5
  - tramo de E1 en la unidad (salida del extractor): 'el pago de deudas comerciales por importaciones de servicios prestados o devengados hasta el 12/12/23'
- **Unidad:** `ext::4.8.1.2` (ext, punto 4.8.1.2, punto_propio)
- **Páginas:** unidad [64], arista [64]; PDF `data/experiment/subset/TO_exterior_cambios_actual.pdf`
- **Render:** `paginas/ext_p64.png`, `paginas/ext_p65.png`
- **Texto heredado:**
  - [encabezado, S4, p. [56]] Sección 4. Otras disposiciones específicas.
  - [encabezado, 4.8, p. [64]] 4.8. Disposiciones complementarias asociadas a los Bonos para la Reconstrucción de una
  - [intro, 4.8, p. [64]] Argentina Libre (BOPREAL).
  - [encabezado, 4.8.1, p. [64]] 4.8.1. Los clientes podrán, en la medida que se cumplan los requisitos aplicables, acceder al
  - [intro, 4.8.1, p. [64]] mercado de cambios mediante la realización de un canje y/o arbitraje con los fondos depositados en una cuenta local y originados en cobros de capital e intereses en moneda extranjera de los bonos BOPREAL para concretar:
  - [cierre, 4.8.1, p. [65]] También se podrán considerar comprendidos en los puntos 4.8.1.1. y 4.8.1.2. a aquellos pagos elegibles que se cursen por el Sistema de Moneda Locales (SML) a partir de la venta de fondos depositados en una cuenta local y originados en cobros de capital e intereses en moneda extranjera de los bonos BOPREAL.
- **Texto propio** («el pago de deudas comerciales por importaciones de servicios prestados o»):

```text
4.8.1.2. el pago de deudas comerciales por importaciones de servicios prestados o
devengados hasta el 12/12/23, que resultaban elegibles de acuerdo con lo
dispuesto en el punto 4.5.
```

## F20

- **Predicado:** `condicion_de`
- **Origen:** Condicion — «Flujo de ingresos futuros suficiente para cancelación» (`Condicion_flujo_de_ingresos_futuros_suficiente_para_cancelacion__el_flujo_de_ingresos_futu_95f0c6`)
  - descripción (salida del extractor): El flujo de ingresos futuros en moneda extranjera proveniente de las operaciones de exportación debe registrar una periodicidad y magnitud tal que sea suficiente para la cancelación de la financiación
  - tramo de E1 en la unidad (salida del extractor): 'siempre que se verifique que el flujo de ingresos futuros en moneda extranjera proveniente de las operaciones de exportación registre una periodicidad y magnitud tal que sea suficiente para la cancelación de la financiación'
- **Destino:** Operacion — «Financiación de prestadores de servicios exportables» (`Operacion_financiacion_de_prestadores_de_servicios_exportables__polcre_2_1_1_44dc88`)
  - descripción (salida del extractor): Operaciones que tengan por destino financiar a prestadores de servicios a ser exportados directamente (tales como los programas informáticos, centros de atención telefónica al cliente)
  - tramo de E1 en la unidad (salida del extractor): 'operaciones que tengan por destino financiar a prestadores de servicios a ser exportados directamente (tales como los programas informáticos, centros de atención telefónica al cliente)'
- **Unidad:** `polcre::2.1.1` (polcre, punto 2.1.1, punto_propio)
- **Páginas:** unidad [6], arista [6]; PDF `data/experiment/escalado_prep/pdfs/polcre.pdf`
- **Render:** `paginas/polcre_p6.png`, `paginas/polcre_p8.png`, `paginas/polcre_p9.png`
- **Texto heredado:**
  - [encabezado, S2, p. [6]] Sección 2. Aplicación de la capacidad de préstamo de depósitos en moneda extranjera.
  - [encabezado, 2.1, p. [6]] 2.1. Destinos.
  - [intro, 2.1, p. [6]] La capacidad de préstamo de los depósitos en moneda extranjera deberá aplicarse, en la co- rrespondiente moneda de captación, en forma indistinta, a los siguientes destinos:
  - [cierre, 2.1, p. [8]] La aplicación de la capacidad de préstamo de depósitos en moneda extranjera a los destinos vinculados a operaciones de importación (previstos en los puntos 2.1.6., 2.1.7. y la parte atri- buible a éstos por aplicación de los puntos 2.1.8. y 2.1.9.), no podrá superar el valor que resulte de la siguiente expresión: C max (F / C ; 0,05)
  - [cierre, 2.1, p. [8]] x
  - [cierre, 2.1, p. [8]] t base base
  - [cierre, 2.1, p. [8]] Siendo: C: capacidad de préstamo del mes al que corresponda.
  - [cierre, 2.1, p. [8]] t
  - [cierre, 2.1, p. [9]] F : financiación de importaciones comprendidas, correspondientes al trimestre agos- base
  - [cierre, 2.1, p. [9]] to/octubre de 2008.
  - [cierre, 2.1, p. [9]] C : capacidad de préstamo que corresponda al trimestre agosto/octubre de 2008.
  - [cierre, 2.1, p. [9]] base
  - [cierre, 2.1, p. [9]] Las financiaciones y capacidad de préstamo deberán ser computadas de acuerdo con lo esta- blecido en el punto 2.5.
- **Texto propio** («Prefinanciación y financiación de exportaciones que se efectúen directamente o a través»):

```text
2.1.1. Prefinanciación y financiación de exportaciones que se efectúen directamente o a través
de mandatarios, consignatarios u otros intermediarios actuantes por cuenta y orden del
propietario de las mercaderías.
También quedan comprendidas las operaciones que tengan por destino financiar a pres-
tadores de servicios a ser exportados directamente (tales como los programas informá-
ticos, centros de atención telefónica al cliente), siempre que se verifique que el flujo de
ingresos futuros en moneda extranjera proveniente de las operaciones de exportación
registre una periodicidad y magnitud tal que sea suficiente para la cancelación de la fi-
nanciación y se constate, en el año previo al otorgamiento de la financiación, una factu-
ración en moneda extranjera a clientes del exterior por un importe que guarde razonable
relación con esa actividad y con su financiación.
```

## F21

- **Predicado:** `condicion_de`
- **Origen:** Condicion — «Condición: no alcanzadas por obligación de liquidación» (`Condicion_condicion_no_alcanzadas_por_obligacion_de_liquidacion__las_operaciones_no_deben__8001ab`)
  - descripción (salida del extractor): Las operaciones no deben estar alcanzadas por la obligación de liquidación en el mercado de cambios
  - tramo de E1 en la unidad (salida del extractor): 'en la medida que no correspondan a operaciones alcanzadas por la obligación de liquidación en el mercado de cambios'
- **Destino:** Potestad — «Facultad de dar curso a canjes y arbitrajes» (`Potestad_facultad_de_dar_curso_a_canjes_y_arbitrajes__las_entidades_estan_facultadas_para_2cb196`)
  - descripción (salida del extractor): Las entidades están facultadas para dar curso a operaciones de canjes y arbitrajes con clientes
  - tramo de E1 en la unidad (salida del extractor): 'Las entidades podrán dar curso a estas operaciones con clientes'
- **Unidad:** `ext::2.8` (ext, punto 2.8, punto_propio)
- **Páginas:** unidad [15], arista [15]; PDF `data/experiment/subset/TO_exterior_cambios_actual.pdf`
- **Render:** `paginas/ext_p15.png`
- **Texto heredado:**
  - [encabezado, S2, p. [8]] Sección 2. Disposiciones específicas para los ingresos por el mercado de cambios.
- **Texto propio** («Canjes y arbitrajes con clientes asociados a ingresos de divisas del exterior.»):

```text
2.8. Canjes y arbitrajes con clientes asociados a ingresos de divisas del exterior.
Las entidades podrán dar curso a estas operaciones con clientes en la medida que no
correspondan a operaciones alcanzadas por la obligación de liquidación en el mercado de
cambios.
Por estas operaciones las entidades financieras deberán permitir la acreditación de ingresos
de divisas del exterior a las cuentas abiertas por el cliente en moneda extranjera.
En caso de que la transferencia corresponda a la misma moneda en la que está denominada
la cuenta, la entidad deberá acreditar el mismo monto recibido del exterior.
Cuando la entidad decida el cobro de una comisión y/o cargo por estas operaciones, ésta
deberá instrumentarse a través de un concepto individualizado específicamente.
```

## F22

- **Predicado:** `condicion_de`
- **Origen:** Condicion — «BCRA autoriza reestructuración en defensa de depositantes» (`Condicion_bcra_autoriza_reestructuracion_en_defensa_de_depositantes__condicion_de_que_el_b_902f54`)
  - descripción (salida del extractor): Condición de que el BCRA autorice la reestructuración de la entidad en defensa de los depositantes
  - tramo de E1 en la unidad (salida del extractor): 'autorice su reestructuración en defensa de los depositantes'
- **Destino:** Operacion — «Emisión de nuevas acciones» (`Operacion_emision_de_nuevas_acciones__cap_8_3_4_4_dc4307`)
  - descripción (salida del extractor): Emisión de nuevas acciones como consecuencia de la ocurrencia de alguno de los eventos desencadenantes
  - tramo de E1 en la unidad (salida del extractor): 'La emisión de nuevas acciones como consecuencia de haberse producido alguno de tales eventos'
- **Unidad:** `cap::8.3.4.4` (cap, punto 8.3.4.4, punto_propio)
- **Páginas:** unidad [160], arista [160]; PDF `data/experiment/subset/TO_capitales_minimos_actual.pdf`
- **Render:** `paginas/cap_p159.png`, `paginas/cap_p160.png`
- **Texto heredado:**
  - [encabezado, S8, p. [154]] Sección 8. Responsabilidad patrimonial computable.
  - [encabezado, 8.3, p. [156]] 8.3. Criterios relacionados con los conceptos computables.
  - [encabezado, 8.3.4, p. [159]] 8.3.4. Requisitos adicionales que los instrumentos a que se refieren los puntos 8.3.2. y 8.3.3.
  - [intro, 8.3.4, p. [159]] deberán observar para garantizar su capacidad de absorción de pérdidas.
- **Texto propio** («Eventos desencadenantes.»):

```text
8.3.4.4. Eventos desencadenantes.
La circunstancia que tornará operativa la disposición a que se refiere el punto
8.3.4.1. tendrá lugar cuando suceda alguno de los eventos que a continuación
se detallan:
i) estando afectada la solvencia y/o liquidez de la entidad financiera el Banco
Central de la República Argentina rechace el plan de regularización y sa-
neamiento que aquella presente –artículo 34 de la Ley de Entidades Finan-
cieras– o revoque su autorización para funcionar –artículo 44 inciso c) de la
Ley de Entidades Financieras– o autorice su reestructuración en defensa
de los depositantes –artículo 35 bis de la Ley de Entidades Financieras,
primer párrafo–, lo que ocurra primero; o
ii) la decisión de capitalizar a la entidad financiera con fondos públicos –o una
medida de apoyo equivalente proporcionada por el Sistema de Seguro de
Garantía de los Depósitos–, en el marco de la aplicación del artículo 35 bis
de la Ley de Entidades Financieras por verse afectada su liquidez y solven-
cia.
La emisión de nuevas acciones como consecuencia de haberse producido al-
guno de tales eventos debe realizarse con anterioridad a cualquier capitaliza-
ción con fondos públicos –o medida de apoyo equivalente– a que se refiere el
apartado ii).
```

## F23

- **Predicado:** `condicion_de`
- **Origen:** Condicion — «Residentes no autorizados a operar en cambios» (`Condicion_residentes_no_autorizados_a_operar_en_cambios__la_operacion_se_aplica_a_resident_dfb0b3`)
  - descripción (salida del extractor): La operación se aplica a residentes que no sean entidades autorizadas a operar en cambios
  - tramo de E1 en la unidad (salida del extractor): 'residentes que no sean entidades autorizadas a operar en cambios'
- **Destino:** Operacion — «Operaciones derivados financieros — residentes no autorizados» (`Operacion_operaciones_derivados_financieros_residentes_no_autorizados__ext_3_12_2_43d4fc`)
  - descripción (salida del extractor): Operaciones de derivados financieros cursadas con acceso al mercado de cambios por residentes que no sean entidades autorizadas a operar en cambios
  - tramo de E1 en la unidad (salida del extractor): 'Las restantes operaciones de derivados financieros que quieran ser cursadas con acceso al mercado de cambios por parte de residentes que no sean entidades autorizadas a operar en cambios'
- **Unidad:** `ext::3.12.2` (ext, punto 3.12.2, punto_propio)
- **Páginas:** unidad [36], arista [36]; PDF `data/experiment/subset/TO_exterior_cambios_actual.pdf`
- **Render:** `paginas/ext_p16.png`, `paginas/ext_p36.png`
- **Texto heredado:**
  - [encabezado, S3, p. [16]] Sección 3. Disposiciones específicas para los egresos por el mercado de cambios
  - [chapeau_seccion, S3, p. [16]] Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–, adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables.
  - [encabezado, 3.12, p. [36]] 3.12. Compra de moneda extranjera para operaciones con derivados financieros.
- **Texto propio** («Las restantes operaciones de derivados financieros que quieran ser cursadas con»):

```text
3.12.2. Las restantes operaciones de derivados financieros que quieran ser cursadas con
acceso al mercado de cambios por parte de residentes que no sean entidades
autorizadas a operar en cambios se regirán por lo dispuesto en los puntos 3.9. y
3.10., según corresponda.
```

## F24

- **Predicado:** `condicion_de`
- **Origen:** Condicion — «Compra de moneda extranjera para garantías» (`Condicion_compra_de_moneda_extranjera_para_garantias__el_acceso_se_condiciona_a_que_la_com_c8c356`)
  - descripción (salida del extractor): El acceso se condiciona a que la compra de moneda extranjera sea para la constitución de garantías en cuentas en moneda extranjera
  - tramo de E1 en la unidad (salida del extractor): 'para la compra de moneda extranjera para la constitución de las garantías en cuentas en moneda extranjera'
- **Destino:** Potestad — «Facultad de dar acceso al mercado de cambios» (`Potestad_facultad_de_dar_acceso_al_mercado_de_cambios__las_entidades_tienen_la_facultad_d_db79ee`)
  - descripción (salida del extractor): Las entidades tienen la facultad de dar acceso al mercado de cambios a los residentes con endeudamientos o prefinanciaciones de exportaciones para la compra de moneda extranjera destinada a la constitución de garantías en cuentas en moneda extranjera
  - tramo de E1 en la unidad (salida del extractor): 'Las entidades podrán dar acceso al mercado de cambios a los residentes'
- **Unidad:** `ext::3.11.3::intro` (ext, punto 3.11.3, bloque_intro)
- **Páginas:** unidad [35], arista [35]; PDF `data/experiment/subset/TO_exterior_cambios_actual.pdf`
- **Render:** `paginas/ext_p35.png`
- **Texto heredado:**
  - [encabezado, S3, p. [16]] Sección 3. Disposiciones específicas para los egresos por el mercado de cambios
  - [encabezado, 3.11, p. [34]] 3.11. Otras compras de moneda extranjera por parte de residentes con aplicación específica.
  - [encabezado, 3.11.3, p. [35]] 3.11.3. Las entidades podrán dar acceso al mercado de cambios a los residentes con
- **Texto propio** («[bloque intro] Las entidades podrán dar acceso al mercado de cambios a los residentes con»):

```text
endeudamientos comprendidos en el punto 7.9. originados a partir del 07/01/21
(únicamente originados a partir del 08/08/25 en el caso de aquellos comprendidos en
el punto 7.9.1.4.) o prefinanciaciones de exportaciones comprendidas en el punto
7.8.5., para la compra de moneda extranjera para la constitución de las garantías en
cuentas en moneda extranjera abiertas en entidades financieras locales o en el
exterior –cuando se trate de un endeudamiento financiero comprendido en el punto
3.5. o las prefinanciaciones admitidas–, por los montos exigibles en los contratos de
endeudamiento, en las siguientes condiciones:
```

## F25

- **Predicado:** `condicion_de`
- **Origen:** Condicion — «Control de cambios en país del exportador» (`Condicion_control_de_cambios_en_pais_del_exportador__supuesto_en_que_la_falta_de_ingreso_d_2ea541`)
  - descripción (salida del extractor): Supuesto en que la falta de ingreso del registro aduanero obedece a restricciones a los giros de divisas en el país del proveedor, acreditado mediante copia con legalización consular de la normativa que dispone ese control cambiario.
  - tramo de E1 en la unidad (salida del extractor): 'Control de cambios en el país del exportador. El importador puede demostrar su gestión de cobro y que la falta de ingreso obedece a que, en el país del proveedor del exterior, existen demoras por restricciones a los giros de divisas.'
- **Destino:** Operacion — «Imputación en SEPAIMPO como gestión de cobro» (`Operacion_imputacion_en_sepaimpo_como_gestion_de_cobro__ext_10_5_5_2_00bb51`)
  - descripción (salida del extractor): Imputación de un pago en el SEPAIMPO como operación en gestión de cobro, cuando se verifique alguna de las condiciones establecidas (control de cambios en país del exportador, insolvencia posterior del proveedor, o deudor moroso).
  - tramo de E1 en la unidad (salida del extractor): 'La entidad a cargo del seguimiento del pago realizado, podrá imputarlo en el SEPAIMPO como en "gestión de cobro" cuando se dé alguna de las siguientes condiciones'
- **Unidad:** `ext::10.5.5.2` (ext, punto 10.5.5.2, punto_propio)
- **Páginas:** unidad [146, 147, 148], arista [146, 147, 148]; PDF `data/experiment/subset/TO_exterior_cambios_actual.pdf`
- **Render:** `paginas/ext_p144.png`, `paginas/ext_p145.png`, `paginas/ext_p146.png`, `paginas/ext_p147.png`, `paginas/ext_p148.png`
- **Texto heredado:**
  - [encabezado, S10, p. [130]] Sección 10. Pagos de importaciones y otras compras de bienes en el exterior.
  - [encabezado, 10.5, p. [144]] 10.5. Seguimiento de pagos de importaciones con registro de ingreso aduanero pendiente.
  - [intro, 10.5, p. [144]] Todo pago de importaciones con registro de ingreso aduanero pendiente efectuado a partir del 02/09/19 estará sujeto a un seguimiento desde la fecha de acceso al mercado de cambios hasta la fecha en que se produzca su regularización. Se considerará regularizada la situación de estos pagos a los efectos cambiarios cuando se demuestre ante la entidad encargada del seguimiento de ese pago, y por hasta el monto girado, la existencia de:
  - [intro, 10.5, p. [144]] i) el registro de ingreso aduanero a su nombre o a nombre de un tercero en la medida
  - [intro, 10.5, p. [144]] que se cumplan las condiciones establecidas en la presente normativa; y/o
  - [intro, 10.5, p. [144]] ii) la liquidación en el mercado de cambios de las divisas asociadas a la devolución del
  - [intro, 10.5, p. [144]] pago efectuado; y/o
  - [intro, 10.5, p. [144]] iii) otras formas de regularización previstas en la presente norma según las condiciones
  - [intro, 10.5, p. [144]] y límites establecidos en cada caso; y/o
  - [intro, 10.5, p. [144]] iv) la conformidad otorgada por el BCRA para dar por regularizada parte o el total de la
  - [intro, 10.5, p. [144]] operación. El pedido solo podrá ser tramitado por la entidad encargada del seguimiento del pago y deberá estar debidamente justificado por ésta.
  - [encabezado, 10.5.5, p. [145]] 10.5.5. Prórrogas de plazos para la demostración del registro de ingreso aduanero.
  - [intro, 10.5.5, p. [145]] Las prórrogas del plazo para la demostración del registro de ingreso aduanero de importación serán concedidas por la entidad a cargo del seguimiento del pago realizado sin registro de ingreso aduanero, dentro de las condiciones que establece la presente normativa o con la previa conformidad del BCRA. Estas prórrogas deberán ser registradas por la entidad encargada del seguimiento del pago en el sistema SEPAIMPO.
- **Texto propio** («Operaciones en gestión de cobro por incumplimiento del proveedor.»):

```text
10.5.5.2. Operaciones en gestión de cobro por incumplimiento del proveedor.
La entidad a cargo del seguimiento del pago realizado, podrá imputarlo en
el SEPAIMPO como en “gestión de cobro” cuando se dé alguna de las
siguientes condiciones:
i) Control de cambios en el país del exportador.
El importador puede demostrar su gestión de cobro y que la falta de
ingreso obedece a que, en el país del proveedor del exterior, existen
demoras por restricciones a los giros de divisas. Lo cual será
acreditado mediante copia con legalización consular, de la normativa
que dispone dicho control cambiario.
ii) Insolvencia posterior del proveedor del exterior, no contándose con
garantías de devolución de los fondos.
En la medida que el importador argentino aporte la siguiente
documentación:
a) constancia de las publicaciones que hagan saber el inicio del
trámite falencial conforme a lo exigido por la legislación vigente en
el país en que tramite; y
b) constancia de la presentación efectuada para obtener el
reconocimiento y pago de su acreencia, certificada por la autoridad
interviniente en el proceso, conforme al procedimiento aplicable en
país donde haya debido efectuarla.
La documentación deberá estar legalizada por autoridad consular o
conforme a lo previsto por el Convenio de la Haya del 5 de octubre de
1961, cuando corresponda.
iii) Deudor moroso.
En la medida que se verifique alguna de las siguientes situaciones:
a) El importador demuestre en forma fehaciente su gestión de cobro
a través de los reclamos efectuados al obligado de pago por
compañías de seguro de crédito a la exportación o de entidades
constituidas como agencias de recupero nacionales o del exterior
contratadas por el importador a tal efecto. Esta alternativa solo
será válida en la medida que el valor adeudado al importador por
el no residente no supere el equivalente de USD 100.000 (dólares
estadounidenses cien mil); y/o
b) El importador argentino haya iniciado y mantenga acciones
judiciales contra el proveedor del exterior o contra quien
corresponda, acreditándolo con copia del escrito de iniciación de
demanda certificada por el juzgado interviniente en cuanto a su
fecha de inicio y radicación. La documentación deberá estar
legalizada por autoridad consular o conforme a lo previsto por el
Convenio de la Haya del 5 de octubre de 1961, cuando resultase
aplicable.
En todos los casos, la entidad deberá exigir, además de la documentación
señalada, una declaración jurada sobre el carácter genuino de lo
declarado, firmada por el importador o quien ejerza su representación legal
o un apoderado con facultades suficientes para asumir este compromiso en
nombre del importador.
Si el importador percibiera un monto en moneda extranjera, el mismo
deberá ser ingresado y liquidado en el mercado de cambios dentro de los
20 (veinte) días hábiles siguientes a la fecha de efectiva percepción.
En todos estos casos, la operación podrá permanecer en “gestión de
cobro” mientras se demuestre la vigencia del reclamo y de las condiciones
que explican la demora en la ejecución de la transferencia. A estos fines, la
entidad otorgará hasta cinco prórrogas sucesivas de hasta 180 (ciento
ochenta) días corridos.
Utilizados los plazos máximos con sus sucesivas renovaciones, la entidad
registrará la condición de no recupero total o parcial de los fondos en el
SEPAIMPO, dando por finalizado su seguimiento del pago. Esto es
independiente de la obligación del importador de ingresar por el mercado
de cambios dentro de los 20 (veinte) días hábiles de la fecha de cobro, todo
recupero en moneda extranjera que registre con relación a dicho pago.
```

## F26

- **Predicado:** `condicion_de`
- **Origen:** Condicion — «Certificaciones de monto pendiente de SEPAIMPO» (`Condicion_certificaciones_de_monto_pendiente_de_sepaimpo__la_entidad_que_concrete_la_ofert_26c793`)
  - descripción (salida del extractor): La entidad que concrete la oferta de suscripción debe contar con certificaciones sobre el monto pendiente de pago emitidas por las entidades encargadas del seguimiento en SEPAIMPO
  - tramo de E1 en la unidad (salida del extractor): 'La entidad que concrete la oferta de suscripción en nombre del cliente deberá contar con las respectivas certificaciones sobre el monto pendiente de pago emitidas por la/s entidad/es encargada/s del seguimiento de las oficializaciones involucradas en el Seguimiento de Pagos de Importaciones de Bienes (SEPAIMPO)'
- **Destino:** Operacion — «Suscripción de BOPREAL por deudores de importaciones» (`Operacion_suscripcion_de_bopreal_por_deudores_de_importaciones__ext_4_4_fefb25`)
  - descripción (salida del extractor): Suscripción de Bonos para la Reconstrucción de una Argentina Libre (BOPREAL) por deudores de importaciones de bienes con registro de ingreso aduanero hasta el 12/12/23, por hasta el monto de la deuda pendiente de pago
  - tramo de E1 en la unidad (salida del extractor): 'Los importadores de bienes podrán suscribir Bonos para la Reconstrucción de una Argentina Libre (BOPREAL) por hasta el monto de la deuda pendiente de pago por sus importaciones de bienes con registro de ingreso aduanero hasta el 12/12/23.'
- **Unidad:** `ext::4.4.2` (ext, punto 4.4, herencia_encabezado)
- **Páginas:** unidad [60], arista [60]; PDF `data/experiment/subset/TO_exterior_cambios_actual.pdf`
- **Render:** `paginas/ext_p60.png`
- **Texto heredado:**
  - [encabezado, S4, p. [56]] Sección 4. Otras disposiciones específicas.
  - [encabezado, 4.4, p. [60]] 4.4. Suscripción de bonos BOPREAL por parte de deudores de importaciones de bienes con
  - [intro, 4.4, p. [60]] registro de ingreso aduanero hasta el 12/12/23. Los importadores de bienes podrán suscribir Bonos para la Reconstrucción de una Argentina Libre (BOPREAL) por hasta el monto de la deuda pendiente de pago por sus importaciones de bienes con registro de ingreso aduanero hasta el 12/12/23. La entidad que concrete la oferta de suscripción en nombre del cliente deberá contar con las respectivas certificaciones sobre el monto pendiente de pago emitidas por la/s entidad/es encargada/s del seguimiento de las oficializaciones involucradas en el Seguimiento de Pagos de Importaciones de Bienes (SEPAIMPO), las cuales deberán verificar que:
  - [cierre, 4.4, p. [60]] En caso de que la importación de bienes encuadre en los puntos 10.3.3., 10.9.1., 10.9.2. y 10.9.3., la entidad que concrete la oferta de suscripción en nombre del cliente deberá verificar en forma directa lo previsto en los puntos 4.4.1. a 4.4.5. y, adicionalmente, contar con una declaración jurada del cliente en la que deja constancia de que no ha solicitado la utilización de este mecanismo en otra entidad por esa deuda. La entidad también deberá realizar la correspondiente intervención de la documentación aduanera. Adicionalmente, la mencionada entidad deberá realizar un boleto de venta de cambio a nombre del importador por el código de concepto “B26. Registro de importaciones de bienes por adjudicación de bonos BOPREAL”; consignando el valor nominal en moneda extranjera de bonos BOPREAL adjudicado al importador y el número de oficialización al que corresponde.
- **Texto propio** («la operación se encuentra declarada, en caso de corresponder, en la última»):

```text
4.4.2. la operación se encuentra declarada, en caso de corresponder, en la última
presentación vencida del "Relevamiento de activos y pasivos externos".
```

## F27

- **Predicado:** `condicion_de`
- **Origen:** Condicion — «Cobros ingresados por sistema de monedas locales» (`Condicion_cobros_ingresados_por_sistema_de_monedas_locales__supuesto_en_que_los_cobros_de__af0c92`)
  - descripción (salida del extractor): Supuesto en que los cobros de exportación de servicios se ingresan a través del sistema de monedas locales
  - tramo de E1 en la unidad (salida del extractor): 'En el caso de que los cobros sean ingresados a través del sistema de monedas locales'
- **Destino:** Operacion — «Ingreso de cobros por sistema de monedas locales» (`Operacion_ingreso_de_cobros_por_sistema_de_monedas_locales__ext_2_2_3_b672e2`)
  - descripción (salida del extractor): Ingreso de cobros de exportaciones de servicios a través del sistema de monedas locales. Se considera cumplimentada la liquidación por el monto acreditado en moneda nacional en la cuenta del exportador.
  - tramo de E1 en la unidad (salida del extractor): 'los cobros sean ingresados a través del sistema de monedas locales'
- **Unidad:** `ext::2.2.3` (ext, punto 2.2.3, punto_propio)
- **Páginas:** unidad [11], arista [11]; PDF `data/experiment/subset/TO_exterior_cambios_actual.pdf`
- **Render:** `paginas/ext_p11.png`
- **Texto heredado:**
  - [encabezado, S2, p. [8]] Sección 2. Disposiciones específicas para los ingresos por el mercado de cambios.
  - [encabezado, 2.2, p. [8]] 2.2. Cobros de exportaciones de servicios.
- **Texto propio** («En el caso de que los cobros sean ingresados a través del sistema de monedas»):

```text
2.2.3. En el caso de que los cobros sean ingresados a través del sistema de monedas
locales se considerará cumplimentada la liquidación por el monto acreditado en
moneda nacional en la cuenta del exportador. En caso de que se trate de servicios
prestados a residentes paraguayos o uruguayos facturados en la moneda del país de
destino de la exportación se computará el equivalente en dicha moneda del monto
acreditado.
```

## F28

- **Predicado:** `condicion_de`
- **Origen:** Condicion — «Solvencia y/o liquidez afectada» (`Condicion_solvencia_y_o_liquidez_afectada__condicion_de_que_la_solvencia_y_o_liquidez_de_l_31b358`)
  - descripción (salida del extractor): Condición de que la solvencia y/o liquidez de la entidad financiera esté afectada
  - tramo de E1 en la unidad (salida del extractor): 'estando afectada la solvencia y/o liquidez de la entidad financiera'
- **Destino:** Operacion — «Emisión de nuevas acciones» (`Operacion_emision_de_nuevas_acciones__cap_8_3_4_4_dc4307`)
  - descripción (salida del extractor): Emisión de nuevas acciones como consecuencia de la ocurrencia de alguno de los eventos desencadenantes
  - tramo de E1 en la unidad (salida del extractor): 'La emisión de nuevas acciones como consecuencia de haberse producido alguno de tales eventos'
- **Unidad:** `cap::8.3.4.4` (cap, punto 8.3.4.4, punto_propio)
- **Páginas:** unidad [160], arista [160]; PDF `data/experiment/subset/TO_capitales_minimos_actual.pdf`
- **Render:** `paginas/cap_p159.png`, `paginas/cap_p160.png`
- **Texto heredado:**
  - [encabezado, S8, p. [154]] Sección 8. Responsabilidad patrimonial computable.
  - [encabezado, 8.3, p. [156]] 8.3. Criterios relacionados con los conceptos computables.
  - [encabezado, 8.3.4, p. [159]] 8.3.4. Requisitos adicionales que los instrumentos a que se refieren los puntos 8.3.2. y 8.3.3.
  - [intro, 8.3.4, p. [159]] deberán observar para garantizar su capacidad de absorción de pérdidas.
- **Texto propio** («Eventos desencadenantes.»):

```text
8.3.4.4. Eventos desencadenantes.
La circunstancia que tornará operativa la disposición a que se refiere el punto
8.3.4.1. tendrá lugar cuando suceda alguno de los eventos que a continuación
se detallan:
i) estando afectada la solvencia y/o liquidez de la entidad financiera el Banco
Central de la República Argentina rechace el plan de regularización y sa-
neamiento que aquella presente –artículo 34 de la Ley de Entidades Finan-
cieras– o revoque su autorización para funcionar –artículo 44 inciso c) de la
Ley de Entidades Financieras– o autorice su reestructuración en defensa
de los depositantes –artículo 35 bis de la Ley de Entidades Financieras,
primer párrafo–, lo que ocurra primero; o
ii) la decisión de capitalizar a la entidad financiera con fondos públicos –o una
medida de apoyo equivalente proporcionada por el Sistema de Seguro de
Garantía de los Depósitos–, en el marco de la aplicación del artículo 35 bis
de la Ley de Entidades Financieras por verse afectada su liquidez y solven-
cia.
La emisión de nuevas acciones como consecuencia de haberse producido al-
guno de tales eventos debe realizarse con anterioridad a cualquier capitaliza-
ción con fondos públicos –o medida de apoyo equivalente– a que se refiere el
apartado ii).
```

## F29

- **Predicado:** `condicion_de`
- **Origen:** Condicion — «Fondos debitados de cuenta en moneda extranjera local» (`Condicion_fondos_debitados_de_cuenta_en_moneda_extranjera_local__los_fondos_deben_debitars_5e2cf7`)
  - descripción (salida del extractor): Los fondos deben debitarse de una cuenta en moneda extranjera del cliente en una entidad financiera local.
  - tramo de E1 en la unidad (salida del extractor): 'en la medida que los fondos se debiten de una cuenta en moneda extranjera del cliente en una entidad financiera local'
- **Destino:** Potestad — «Realizar arbitraje sin transferencias — fondos en moneda extranjera» (`Potestad_realizar_arbitraje_sin_transferencias_fondos_en_moneda_extranjera__las_entidades_f70b8e`)
  - descripción (salida del extractor): Las entidades podrán realizar operaciones de arbitraje que no impliquen transferencias al exterior sin restricciones cuando los fondos se debiten de una cuenta en moneda extranjera del cliente en una entidad financiera local.
  - tramo de E1 en la unidad (salida del extractor): 'Las operaciones de arbitraje que no impliquen transferencias al exterior podrán realizarse sin restricciones en la medida que los fondos se debiten de una cuenta en moneda extranjera del cliente en una entidad financiera local.'
- **Unidad:** `ext::3.14.4` (ext, punto 3.14.4, punto_propio)
- **Páginas:** unidad [40], arista [40]; PDF `data/experiment/subset/TO_exterior_cambios_actual.pdf`
- **Render:** `paginas/ext_p16.png`, `paginas/ext_p40.png`, `paginas/ext_p41.png`
- **Texto heredado:**
  - [encabezado, S3, p. [16]] Sección 3. Disposiciones específicas para los egresos por el mercado de cambios
  - [chapeau_seccion, S3, p. [16]] Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–, adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables.
  - [encabezado, 3.14, p. [40]] 3.14. Canjes y arbitrajes con clientes no asociados a ingresos de divisas del exterior.
  - [intro, 3.14, p. [40]] Las entidades podrán realizar con sus clientes operaciones de canje y arbitrajes no asociadas a un ingreso de divisas desde el exterior en los siguientes casos:
  - [cierre, 3.14, p. [41]] En caso de que la transferencia corresponda a la misma moneda en la que está denominada la cuenta, la entidad deberá debitar el monto enviado al exterior. Cuando la entidad decida el cobro de una comisión y/o cargo por estas operaciones, ésta deberá instrumentarse a través de un concepto individualizado específicamente.
- **Texto propio** («Las operaciones de arbitraje que no impliquen transferencias al exterior podrán»):

```text
3.14.4. Las operaciones de arbitraje que no impliquen transferencias al exterior podrán
realizarse sin restricciones en la medida que los fondos se debiten de una cuenta en
moneda extranjera del cliente en una entidad financiera local.
En la medida que los fondos no sean debitados de una cuenta en moneda extranjera
del cliente, estas operaciones sólo podrán ser realizadas, sin conformidad previa del
BCRA, por personas humanas hasta el monto admitido para el uso de efectivo en los
puntos 3.8., 3.9. y 3.13.
```

## F30

- **Predicado:** `condicion_de`
- **Origen:** Condicion — «Permiso embarque definitivo asociado a embarque provisorio anterior» (`Condicion_permiso_embarque_definitivo_asociado_a_embarque_provisorio_anterior__supuesto_en_d4ae50`)
  - descripción (salida del extractor): Supuesto en que un permiso de embarque definitivo está asociado a un embarque provisorio oficializado antes del 2 de septiembre de 2019
  - tramo de E1 en la unidad (salida del extractor): 'En caso de que un permiso de embarque definitivo esté asociado a un embarque provisorio oficializado con anterioridad al 02/09/19'
- **Destino:** Potestad — «Facultad de dar cumplido de embarque definitivo» (`Potestad_facultad_de_dar_cumplido_de_embarque_definitivo__las_entidades_quedan_facultadas_93ab56`)
  - descripción (salida del extractor): Las entidades quedan facultadas a dar el cumplido de embarque del permiso de embarque definitivo cuando se verifica el supuesto de asociación con embarque provisorio anterior
  - tramo de E1 en la unidad (salida del extractor): 'las entidades podrán dar el cumplido de embarque del permiso definitivo'
- **Unidad:** `ext::7.8.2.5` (ext, punto 7.8.2.5, punto_propio)
- **Páginas:** unidad [92], arista [92]; PDF `data/experiment/subset/TO_exterior_cambios_actual.pdf`
- **Render:** `paginas/ext_p91.png`, `paginas/ext_p92.png`
- **Texto heredado:**
  - [encabezado, S7, p. [80]] Sección 7. Cobros de exportaciones de bienes.
  - [encabezado, 7.8, p. [91]] 7.8. Otras disposiciones.
  - [encabezado, 7.8.2, p. [91]] 7.8.2. Exportaciones bajo los regímenes de precios revisables o concentrado de minerales.
  - [intro, 7.8.2, p. [91]] En los casos de exportaciones de productos que se comercializan sobre la base de precios FOB sujetos a una determinación posterior al momento de registro de la operación (Exportación de mercaderías con precios revisables – Resolución General 4073-E/17 de la Administración Federal de Ingresos Públicos) o al amparo del Régimen de Concentrados de Minerales (Resolución General 2108/06 de la Administración Federal de Ingresos Públicos) será aplicable lo siguiente:
- **Texto propio** («En caso de que un permiso de embarque definitivo esté asociado a un»):

```text
7.8.2.5. En caso de que un permiso de embarque definitivo esté asociado a un
embarque provisorio oficializado con anterioridad al 02/09/19, las entidades
podrán dar el cumplido de embarque del permiso definitivo.
```

## F31

- **Predicado:** `condicion_de`
- **Origen:** Condicion — «Composición de bienes — mínimo 90% bien de capital» (`Condicion_composicion_de_bienes_minimo_90_bien_de_capital__los_bienes_que_revistan_la_cond_171611`)
  - descripción (salida del extractor): Los bienes que revistan la condición de bien de capital deben representar como mínimo el 90% del valor FOB total pagado.
  - tramo de E1 en la unidad (salida del extractor): 'aquellos que lo sean representen como mínimo el 90% (noventa por ciento) del valor FOB total pagado'
- **Destino:** Operacion — «Cómputo de aportes inversión directa en especie» (`Operacion_computo_de_aportes_inversion_directa_en_especie__ext_14_5_7_97c0f6`)
  - descripción (salida del extractor): Aportes de inversión directa en especie instrumentados mediante la entrega al VPU de bienes de capital que pueden ser computados como ingresados y liquidados en el mercado de cambios, sujeto a cumplimiento de condiciones específicas.
  - tramo de E1 en la unidad (salida del extractor): 'Los aportes de inversión directa en especie instrumentados mediante la entrega al VPU de bienes de capital podrán ser computados como ingresados y liquidados en el mercado de cambios'
- **Unidad:** `ext::14.5.7` (ext, punto 14.5.7, punto_propio)
- **Páginas:** unidad [182, 183], arista [182, 183]; PDF `data/experiment/subset/TO_exterior_cambios_actual.pdf`
- **Render:** `paginas/ext_p175.png`, `paginas/ext_p182.png`, `paginas/ext_p183.png`
- **Texto heredado:**
  - [encabezado, S14, p. [175]] Sección 14. Disposiciones complementarias asociadas al Régimen de Incentivo para Grandes Inversiones (RIGI).
  - [chapeau_seccion, S14, p. [175]] En esta sección se detallan las disposiciones complementarias en materia cambiaria que, en la medida que las disposiciones generales no resulten más favorables, resultan aplicables a un Vehículo de Proyecto Único (VPU) adherido al Régimen de Incentivo los referidas al “Régimen de Incentivo para Grandes Inversiones” (RIGI) establecido en el Título VII de la Ley 27.742 y reglamentado por el Decreto 749/24 y concordantes.
  - [encabezado, 14.5, p. [180]] 14.5. Otras disposiciones.
- **Texto propio** («Los aportes de inversión directa en especie instrumentados mediante la entrega al»):

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

## F32

- **Predicado:** `condicion_de`
- **Origen:** Condicion — «Monto pendiente prefinanciado en su totalidad» (`Condicion_monto_pendiente_prefinanciado_en_su_totalidad__condicion_el_monto_pendiente_de_i_412be4`)
  - descripción (salida del extractor): Condición: el monto pendiente de ingreso ha sido prefinanciado en su totalidad y los fondos han sido liquidados en el mercado de cambios en concepto de prefinanciaciones de exportaciones locales y/o del exterior.
  - tramo de E1 en la unidad (salida del extractor): 'Cuando el monto pendiente de ingreso de las operaciones haya sido prefinanciado en su totalidad y los fondos liquidados en el mercado de cambios en concepto de prefinanciaciones de exportaciones locales y/o del exterior'
- **Destino:** Potestad — «Extensión del plazo para liquidación de divisas — prefinanciación total» (`Potestad_extension_del_plazo_para_liquidacion_de_divisas_prefinanciacion_total__la_entida_32af4f`)
  - descripción (salida del extractor): La entidad encargada del seguimiento del permiso podrá extender el plazo para la liquidación de divisas del embarque hasta la fecha de vencimiento de la financiación dada al comprador, cuando el monto pendiente haya sido prefinanciado en su totalidad.
  - tramo de E1 en la unidad (salida del extractor): 'se podrá extender el plazo para la liquidación de divisas del embarque hasta la fecha de vencimiento de la correspondiente financiación dada al comprador'
- **Unidad:** `ext::7.5.2` (ext, punto 7.5.2, punto_propio)
- **Páginas:** unidad [86, 87], arista [86, 87]; PDF `data/experiment/subset/TO_exterior_cambios_actual.pdf`
- **Render:** `paginas/ext_p86.png`, `paginas/ext_p87.png`
- **Texto heredado:**
  - [encabezado, S7, p. [80]] Sección 7. Cobros de exportaciones de bienes.
  - [encabezado, 7.5, p. [86]] 7.5. Ampliaciones del plazo para el ingreso y liquidación de divisas.
  - [intro, 7.5, p. [86]] La entidad encargada del seguimiento del permiso podrá conceder extensiones en el plazo de ingreso y liquidación en las siguientes circunstancias:
- **Texto propio** («Exportaciones financiadas al comprador totalmente prefinanciadas y/o posfinanciadas»):

```text
7.5.2. Exportaciones financiadas al comprador totalmente prefinanciadas y/o posfinanciadas
localmente o desde el exterior.
Cuando el monto pendiente de ingreso de las operaciones haya sido prefinanciado en
su totalidad y los fondos liquidados en el mercado de cambios en concepto de
prefinanciaciones de exportaciones locales y/o del exterior, se podrá extender el plazo
para la liquidación de divisas del embarque hasta la fecha de vencimiento de la
correspondiente financiación dada al comprador.
En tanto si el exportador demuestra haber liquidado en el mercado de cambio, antes
del vencimiento del plazo, posfinanciaciones de exportaciones que cubran la totalidad
del monto pendiente de ingreso del permiso, sin que se verifiquen las condiciones
previstas para los puntos 9.3.4. y 9.3.5. para la emisión de la correspondiente
certificación de aplicación, se podrá extender el plazo para la liquidación de divisas del
embarque hasta la fecha en que venza el crédito de mayor plazo descontado y/o
cedido por el exportador.
Esto último también será aplicable cuando el exportador haya prefinanciado
parcialmente la operación y demuestre haber liquidado en el mercado de cambio,
antes del vencimiento, posfinanciaciones de exportaciones que cubran el resto del
monto pendiente de ingreso.
Esta extensión del plazo también se podrá otorgar a exportaciones de bienes
comprendidas en lo dispuesto por los Decretos 492/23, 549/23, 597/23 y 28/23, en la
medida que el cliente demuestre que, durante sus respectivas vigencias y en las
condiciones estipuladas en los mencionados decretos, ingresó y liquidó divisas en el
mercado de cambios por un monto no menor al porcentaje mínimo requerido del
anticipo, prefinanciación o posfinanciación y la porción no liquidada concretó
operaciones de compraventa con títulos valores, en las cuales los títulos valores son
adquiridos con liquidación en moneda extranjera y vendidos con liquidación en moneda
local en el país.
En el caso de que la adquisición de títulos valores se haya concretado con liquidación
en el país de la moneda extranjera se deberá contar con la certificación de la entidad
que cursó la operación de canje y/o arbitraje por el ingreso de las divisas a través del
mercado de cambios.
```

## F33

- **Predicado:** `condicion_de`
- **Origen:** Condicion — «Denominación en pesos y fondos en pesos» (`Condicion_denominacion_en_pesos_y_fondos_en_pesos__las_operaciones_deben_estar_denominadas_03e0d7`)
  - descripción (salida del extractor): Las operaciones deben estar denominadas en pesos y la fuente de fondos debe ser en esa moneda.
  - tramo de E1 en la unidad (salida del extractor): 'en la medida que dichas operaciones estén denominadas en pesos, la fuente de fondos sea en esa moneda'
- **Destino:** Operacion — «Financiación a beneficiarios seguridad social o empleados públicos» (`Operacion_financiacion_a_beneficiarios_seguridad_social_o_empleados_publicos__cap_2_12_2_3_47c5fe`)
  - descripción (salida del extractor): Financiaciones otorgadas a beneficiarios de la seguridad social o a empleados públicos, con código de descuento, denominadas en pesos, con fondos en esa moneda, donde las cuotas de todas las financiaciones de la entidad con sistema de amortización periódica no excedan del 30% de los ingresos del deudor y/o codeudores.
  - tramo de E1 en la unidad (salida del extractor): 'financiaciones otorgadas a beneficiarios de la seguridad social o a empleados públicos'
- **Unidad:** `cap::2.12.2.3` (cap, punto 2.12.2.3, punto_propio)
- **Páginas:** unidad [23], arista [23]; PDF `data/experiment/subset/TO_capitales_minimos_actual.pdf`
- **Render:** `paginas/cap_p7.png`, `paginas/cap_p22.png`, `paginas/cap_p23.png`
- **Texto heredado:**
  - [encabezado, S2, p. [7]] Sección 2. Capital mínimo por riesgo de crédito.
  - [chapeau_seccion, S2, p. [7]] A los efectos de la aplicación de las disposiciones de la presente sección, las entidades financieras se clasificarán en: i)Grupo 1: entidades calificadas por el BCRA como de importancia sistémica a nivel local
  - [chapeau_seccion, S2, p. [7]] (D-SIB) y sucursales o subsidiarias de bancos del exterior calificados como de impor- tancia sistémica global (G-SIB).
  - [chapeau_seccion, S2, p. [7]] ii) Grupo 2: entidades financieras no comprendidas en el acápite i). En aquellos casos en que no se establezcan disposiciones específicas para cada uno de los citados grupos de entidades financieras, deberá aplicarse el mismo tratamiento a ambos grupos. Las entidades financieras que presenten cambios en su calificación –conforme a lo previsto en los acápites precedentes–, contarán con un plazo de 6 meses para aplicar las disposiciones específicas correspondientes al nuevo grupo al que pertenezcan.
  - [encabezado, 2.12, p. [22]] 2.12. Tabla de ponderadores de riesgo.
  - [intro, 2.12, p. [22]] Concepto Ponderador
  - [intro, 2.12, p. [22]] –en %–
  - [encabezado, 2.12.2, p. [23]] 2.12.2. Exposición a gobiernos y bancos centrales.
- **Texto propio** («Al sector público no financiero por financiaciones otorgadas a»):

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

## F34

- **Predicado:** `condicion_de`
- **Origen:** Condicion — «Servicios a residentes paraguayos o uruguayos en moneda de destino» (`Condicion_servicios_a_residentes_paraguayos_o_uruguayos_en_moneda_de_destino__supuesto_en__1ff0ec`)
  - descripción (salida del extractor): Supuesto en que se trata de servicios prestados a residentes paraguayos o uruguayos facturados en la moneda del país de destino de la exportación
  - tramo de E1 en la unidad (salida del extractor): 'En caso de que se trate de servicios prestados a residentes paraguayos o uruguayos facturados en la moneda del país de destino de la exportación'
- **Destino:** Operacion — «Ingreso de cobros servicios a residentes paraguayos o uruguayos» (`Operacion_ingreso_de_cobros_servicios_a_residentes_paraguayos_o_uruguayos__ext_2_2_3_c85cb5`)
  - descripción (salida del extractor): Ingreso de cobros de servicios prestados a residentes paraguayos o uruguayos facturados en la moneda del país de destino de la exportación. Se computa el equivalente en dicha moneda del monto acreditado.
  - tramo de E1 en la unidad (salida del extractor): 'servicios prestados a residentes paraguayos o uruguayos facturados en la moneda del país de destino de la exportación'
- **Unidad:** `ext::2.2.3` (ext, punto 2.2.3, punto_propio)
- **Páginas:** unidad [11], arista [11]; PDF `data/experiment/subset/TO_exterior_cambios_actual.pdf`
- **Render:** `paginas/ext_p11.png`
- **Texto heredado:**
  - [encabezado, S2, p. [8]] Sección 2. Disposiciones específicas para los ingresos por el mercado de cambios.
  - [encabezado, 2.2, p. [8]] 2.2. Cobros de exportaciones de servicios.
- **Texto propio** («En el caso de que los cobros sean ingresados a través del sistema de monedas»):

```text
2.2.3. En el caso de que los cobros sean ingresados a través del sistema de monedas
locales se considerará cumplimentada la liquidación por el monto acreditado en
moneda nacional en la cuenta del exportador. En caso de que se trate de servicios
prestados a residentes paraguayos o uruguayos facturados en la moneda del país de
destino de la exportación se computará el equivalente en dicha moneda del monto
acreditado.
```

## F35

- **Predicado:** `condicion_de`
- **Origen:** Condicion — «Condición: suma pagos ≤ 80% FOB» (`Condicion_condicion_suma_pagos_80_fob__la_suma_de_los_pagos_anticipados_a_la_vista_y_de_de_8c86d5`)
  - descripción (salida del extractor): La suma de los pagos anticipados, a la vista y de deuda comercial sin registro de ingreso aduanero no supera el 80% del valor FOB de los bienes de capital a importar
  - tramo de E1 en la unidad (salida del extractor): 'ii) la suma de los pagos anticipados, a la vista y de deuda comercial sin registro de ingreso aduanero cursados en el marco de este punto no supera el 80% (ochenta por ciento) del valor FOB de los bienes de capital a importar'
- **Destino:** Operacion — «Pago anticipado importación bienes capital» (`Operacion_pago_anticipado_importacion_bienes_capital__ext_10_10_2_2_6aeb8c`)
  - descripción (salida del extractor): Pago anticipado de importación de bienes de capital con registro de ingreso aduanero pendiente
  - tramo de E1 en la unidad (salida del extractor): 'pagos anticipados cursados en el marco de este punto'
- **Unidad:** `ext::10.10.2.2` (ext, punto 10.10.2.2, punto_propio)
- **Páginas:** unidad [154, 155], arista [154, 155]; PDF `data/experiment/subset/TO_exterior_cambios_actual.pdf`
- **Render:** `paginas/ext_p154.png`, `paginas/ext_p155.png`, `paginas/ext_p157.png`
- **Texto heredado:**
  - [encabezado, S10, p. [130]] Sección 10. Pagos de importaciones y otras compras de bienes en el exterior.
  - [encabezado, 10.10, p. [154]] 10.10. Disposiciones complementarias para importaciones de bienes que tuvieron o tendrán registro
  - [intro, 10.10, p. [154]] de ingreso aduanero a partir del 13/12/23.
  - [encabezado, 10.10.2, p. [154]] 10.10.2. Pagos de importaciones de bienes con registro de ingreso aduanero pendiente.
  - [intro, 10.10.2, p. [154]] Las entidades podrán dar acceso al mercado de cambios para cursar pagos con registro de ingreso aduanero pendiente por operaciones no comprendidas en el punto 10.6.6. cuando, en adición a los restantes requisitos aplicables, se verifique alguna de las siguientes situaciones:
  - [cierre, 10.10.2, p. [157]] Se podrá considerar como importación de bienes de capital a: i) aquellas que correspondan a bienes cuyas posiciones arancelarias se encuentren clasificadas como BK en la Nomenclatura Común del MERCOSUR (Decreto 690/02 y complementarias) y ii) aquellas que incluyan otros bienes en la medida que los bienes clasificados como BK representen como mínimo el 90% (noventa por ciento) del valor FOB total de la operación y la entidad cuente con una declaración jurada del cliente en la cual deje constancia de que los restantes bienes son repuestos, accesorios o materiales necesarios para el funcionamiento, construcción o instalación de los bienes de capital que se están adquiriendo.
- **Texto propio** («Pagos de importaciones de bienes de capital con registro de ingreso»):

```text
10.10.2.2. Pagos de importaciones de bienes de capital con registro de ingreso
aduanero pendiente en la medida que:
i) la suma de los pagos anticipados cursados en el marco de este
punto no supera el 30% (treinta por ciento) del valor FOB de los
bienes de capital a importar;
ii) la suma de los pagos anticipados, a la vista y de deuda comercial
sin registro de ingreso aduanero cursados en el marco de este
punto no supera el 80% (ochenta por ciento) del valor FOB de los
bienes de capital a importar;
iii) las posiciones arancelarias de los bienes de capital a importar no
correspondan a aquellas comprendidas en el punto 12.1.
```

## F36

- **Predicado:** `condicion_de`
- **Origen:** Condicion — «Fecha de vencimiento del interés» (`Condicion_fecha_de_vencimiento_del_interes__el_acceso_al_mercado_de_cambios_se_condiciona__824eb0`)
  - descripción (salida del extractor): El acceso al mercado de cambios se condiciona a que se verifique la fecha de vencimiento del interés a pagar.
  - tramo de E1 en la unidad (salida del extractor): 'a partir de la fecha de vencimiento del interés a pagar'
- **Destino:** Operacion — «Acceso al mercado de cambios — pago de intereses» (`Operacion_acceso_al_mercado_de_cambios_pago_de_intereses__ext_3_3_2_700024`)
  - descripción (salida del extractor): Acceso al mercado de cambios para cursar pagos de intereses de deudas comerciales por importaciones de bienes o servicios, que tiene lugar a partir de la fecha de vencimiento del interés a pagar.
  - tramo de E1 en la unidad (salida del extractor): 'El acceso al mercado de cambios tiene lugar a partir de la fecha de vencimiento del interés a pagar'
- **Unidad:** `ext::3.3.2` (ext, punto 3.3.2, punto_propio)
- **Páginas:** unidad [16], arista [16]; PDF `data/experiment/subset/TO_exterior_cambios_actual.pdf`
- **Render:** `paginas/ext_p16.png`
- **Texto heredado:**
  - [encabezado, S3, p. [16]] Sección 3. Disposiciones específicas para los egresos por el mercado de cambios
  - [chapeau_seccion, S3, p. [16]] Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–, adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables.
  - [encabezado, 3.3, p. [16]] 3.3. Pagos de intereses de deudas por importaciones de bienes y servicios.
  - [intro, 3.3, p. [16]] Las entidades para dar acceso al mercado de cambios para cursar pagos de intereses de deudas comerciales por importaciones de bienes o servicios deberán verificar que se cumplan las condiciones especificadas a continuación:
- **Texto propio** («El acceso al mercado de cambios tiene lugar a partir de la fecha de vencimiento del»):

```text
3.3.2. El acceso al mercado de cambios tiene lugar a partir de la fecha de vencimiento del
interés a pagar.
Este requisito no resultará aplicable si el cliente es un Vehículo de Proyecto Único
(VPU) adherido al Régimen de Incentivo para Grandes Inversiones (RIGI) que concreta
el pago en el marco de lo previsto en el punto 14.2.1.
En los restantes casos se requerirá la conformidad previa del BCRA para acceder al
mercado de cambios para precancelar los servicios de intereses de deudas
comerciales por importaciones de bienes y servicios.
```

## F37

- **Predicado:** `condicion_de`
- **Origen:** Condicion — «Verificación previa de requisitos del punto 10.3.2» (`Condicion_verificacion_previa_de_requisitos_del_punto_10_3_2__se_cumplen_la_totalidad_de_r_376e46`)
  - descripción (salida del extractor): Se cumplen la totalidad de requisitos detallados en el punto 10.3.2, con la sustitución de lo requerido en los incisos i), iii) y iv) del punto 10.3.2.1 por lo siguiente
  - tramo de E1 en la unidad (salida del extractor): 'en la medida que verifique previamente que se cumplen la totalidad de requisitos detallados en el punto 10.3.2.'
- **Destino:** Potestad — «Facultad de dar acceso al mercado de cambios» (`Potestad_facultad_de_dar_acceso_al_mercado_de_cambios__la_entidad_interviniente_tiene_la__fbebc9`)
  - descripción (salida del extractor): La entidad interviniente tiene la facultad de dar acceso al mercado de cambios para el pago al exterior de importaciones de bienes ingresadas desde zonas francas con transferencia aduanera, sujeto a verificación previa de requisitos
  - tramo de E1 en la unidad (salida del extractor): 'La entidad interviniente podrá dar acceso al mercado de cambios'
- **Unidad:** `ext::10.3.5::intro` (ext, punto 10.3.5, bloque_intro)
- **Páginas:** unidad [137], arista [137]; PDF `data/experiment/subset/TO_exterior_cambios_actual.pdf`
- **Render:** `paginas/ext_p137.png`
- **Texto heredado:**
  - [encabezado, S10, p. [130]] Sección 10. Pagos de importaciones y otras compras de bienes en el exterior.
  - [encabezado, 10.3, p. [133]] 10.3. Pagos de importaciones de bienes que cuentan con registro de ingreso aduanero.
  - [encabezado, 10.3.5, p. [137]] 10.3.5. Pagos de importaciones de bienes ingresadas desde zonas francas con transferencia
- **Texto propio** («[bloque intro] Pagos de importaciones de bienes ingresadas desde zonas francas con transferencia»):

```text
aduanera de dominio del exportador al importador.
La entidad interviniente podrá dar acceso al mercado de cambios para el pago al
exterior de importaciones de bienes ingresadas desde zonas francas con
transferencia aduanera de dominio del exportador al importador en la medida que
verifique previamente que se cumplen la totalidad de requisitos detallados en el punto
10.3.2., reemplazando lo requerido en los incisos i), iii) y iv) del punto 10.3.2.1. por lo
siguiente:
```

## F38

- **Predicado:** `condicion_de`
- **Origen:** Condicion — «Vinculación a falta de pago» (`Condicion_vinculacion_a_falta_de_pago__la_demanda_se_encuentra_vinculada_a_la_falta_de_pag_41f35b`)
  - descripción (salida del extractor): La demanda se encuentra vinculada a la falta de pago
  - tramo de E1 en la unidad (salida del extractor): 'cuando ello se encuentre vinculado a la falta de pago'
- **Destino:** Operacion — «Clasificación de deudor con problemas» (`Operacion_clasificacion_de_deudor_con_problemas__cla_6_5_3_11_f663c1`)
  - descripción (salida del extractor): Clasificación del cliente en la categoría 'Con problemas' cuando ha sido demandado judicialmente por cobro de acreencia vinculada a falta de pago con mora no superior a 180 días
  - tramo de E1 en la unidad (salida del extractor): 'Haya sido demandado judicialmente por la entidad para el cobro de su acreencia, cuando ello se encuentre vinculado a la falta de pago y registre mora en el pago de las obligaciones no superior a 180 días'
- **Unidad:** `cla::6.5.3.11` (cla, punto 6.5.3.11, punto_propio)
- **Páginas:** unidad [25], arista [25]; PDF `data/experiment/subset/TO_clasificacion_deudores_actual.pdf`
- **Render:** `paginas/cla_p19.png`, `paginas/cla_p23.png`, `paginas/cla_p25.png`
- **Texto heredado:**
  - [encabezado, S6, p. [17]] Sección 6. Clasificación de los deudores de la cartera comercial.
  - [encabezado, 6.5, p. [19]] 6.5. Niveles de clasificación.
  - [intro, 6.5, p. [19]] Cada cliente, y la totalidad de sus financiaciones comprendidas, se incluirá en una de las si- guientes cinco categorías, las que se definen teniendo en cuenta las condiciones que se deta- llan en cada caso. Los clientes que no registren asistencia crediticia de la entidad y que posteriormente reciban fi- nanciaciones de ésta que no superen el importe resultante de aplicar sobre el saldo de deuda registrado en el sistema financiero, según la última información disponible en la “Central de deudores” a la fecha de su otorgamiento, el porcentaje establecido en el punto 2.2.5. de las normas sobre “Previsiones mínimas por riesgo de incobrabilidad” correspondiente a la peor cla- sificación asignada, podrán ser clasificados por la entidad teniendo en cuenta únicamente el análisis del flujo de fondos proyectado. Las asistencias así otorgadas no serán consideradas a los fines a que se refiere el punto 6.6. A fin de verificar el cumplimiento de las obligaciones sin recurrir a nueva financiación directa o indirecta o a refinanciaciones, no se considerarán refinanciaciones las facilidades adicionales que se otorguen respecto de los márgenes vigentes acordados, siempre que el nuevo apoyo crediticio implique nuevos desembolsos de fondos y no supere el 10 % del cupo asignado en oportunidad de la última evaluación crediticia del cliente, en la medida en que éstas sean con- sistentes con el curso normal de los negocios y exista capacidad para atender el resto de las obligaciones financieras, ni las nuevas financiaciones y las refinanciaciones asociadas a una mayor inversión derivada de la expansión de las actividades, y siempre que pueda demostrarse que el flujo de fondos proyectado permitirá afrontar la totalidad de sus obligaciones. Tampoco se considerarán dentro de ese concepto las refinanciaciones otorgadas a los produc- tores agropecuarios cuando ello resulte de la aplicación de disposiciones vinculadas a la Ley de Emergencia Agropecuaria, sin perjuicio de lo cual, a los fines de la clasificación, deberá tenerse en cuenta el flujo de fondos proyectado para el momento en que concluya la vigencia de la emergencia declarada. El tratamiento que se dispense en ese marco no podrá implicar mejora- miento de la clasificación asignada al cliente en función de su situación individual, preexistente a la emergencia, ni su aplicación extenderse más allá de la vigencia fijada para ella.
  - [encabezado, 6.5.3, p. [23]] 6.5.3. Con problemas.
  - [intro, 6.5.3, p. [23]] El análisis del flujo de fondos del cliente demuestra que tiene problemas para atender normalmente la totalidad de sus compromisos financieros y que, de no ser corregidos, esos problemas pueden resultar en una pérdida para la entidad financiera. Entre los indicadores que pueden reflejar esta situación se destacan que el cliente:
- **Texto propio** («Haya sido demandado judicialmente por la entidad para el cobro de su acreen-»):

```text
6.5.3.11. Haya sido demandado judicialmente por la entidad para el cobro de su acreen-
cia, cuando ello se encuentre vinculado a la falta de pago y registre mora en el
pago de las obligaciones no superior a 180 días. Se excluyen los casos en que
las acciones se refieren a la discusión sobre otros aspectos contractuales.
```

## F39

- **Predicado:** `condicion_de`
- **Origen:** Condicion — «Pago del 15 % sin atrasos mayores a 31 días» (`Condicion_pago_del_15_sin_atrasos_mayores_a_31_dias__se_ha_cumplido_con_el_pago_sin_atraso_6acbec`)
  - descripción (salida del extractor): Se ha cumplido con el pago, sin atrasos superiores a 31 días, del 15 % de las obligaciones refinanciadas y la totalidad de los intereses devengados
  - tramo de E1 en la unidad (salida del extractor): 'se haya cumplido con el pago, sin haber incurrido en atrasos superiores a los 31 días del 15 % de las obligaciones refinanciadas y la totalidad de los intereses devengados'
- **Destino:** Potestad — «Reclasificación a nivel superior con pago del 15 %» (`Potestad_reclasificacion_a_nivel_superior_con_pago_del_15__la_entidad_podra_reclasificar__bde403`)
  - descripción (salida del extractor): La entidad podrá reclasificar al deudor en el nivel inmediato superior cuando se haya cumplido con el pago, sin atrasos superiores a 31 días, del 15 % de las obligaciones refinanciadas y la totalidad de los intereses devengados, y se observen las otras condiciones previstas en ese nivel
  - tramo de E1 en la unidad (salida del extractor): 'Cuando al menos se haya cumplido con el pago, sin haber incurrido en atrasos superiores a los 31 días del 15 % de las obligaciones refinanciadas y la totalidad de los intereses devengados, podrá reclasificarse al deudor en el nivel inmediato superior si, además, se observan las otras condiciones previstas en el citado nivel'
- **Unidad:** `cla::6.5.5.2` (cla, punto 6.5.5.2, punto_propio)
- **Páginas:** unidad [28], arista [28]; PDF `data/experiment/subset/TO_clasificacion_deudores_actual.pdf`
- **Render:** `paginas/cla_p19.png`, `paginas/cla_p28.png`, `paginas/cla_p31.png`
- **Texto heredado:**
  - [encabezado, S6, p. [17]] Sección 6. Clasificación de los deudores de la cartera comercial.
  - [encabezado, 6.5, p. [19]] 6.5. Niveles de clasificación.
  - [intro, 6.5, p. [19]] Cada cliente, y la totalidad de sus financiaciones comprendidas, se incluirá en una de las si- guientes cinco categorías, las que se definen teniendo en cuenta las condiciones que se deta- llan en cada caso. Los clientes que no registren asistencia crediticia de la entidad y que posteriormente reciban fi- nanciaciones de ésta que no superen el importe resultante de aplicar sobre el saldo de deuda registrado en el sistema financiero, según la última información disponible en la “Central de deudores” a la fecha de su otorgamiento, el porcentaje establecido en el punto 2.2.5. de las normas sobre “Previsiones mínimas por riesgo de incobrabilidad” correspondiente a la peor cla- sificación asignada, podrán ser clasificados por la entidad teniendo en cuenta únicamente el análisis del flujo de fondos proyectado. Las asistencias así otorgadas no serán consideradas a los fines a que se refiere el punto 6.6. A fin de verificar el cumplimiento de las obligaciones sin recurrir a nueva financiación directa o indirecta o a refinanciaciones, no se considerarán refinanciaciones las facilidades adicionales que se otorguen respecto de los márgenes vigentes acordados, siempre que el nuevo apoyo crediticio implique nuevos desembolsos de fondos y no supere el 10 % del cupo asignado en oportunidad de la última evaluación crediticia del cliente, en la medida en que éstas sean con- sistentes con el curso normal de los negocios y exista capacidad para atender el resto de las obligaciones financieras, ni las nuevas financiaciones y las refinanciaciones asociadas a una mayor inversión derivada de la expansión de las actividades, y siempre que pueda demostrarse que el flujo de fondos proyectado permitirá afrontar la totalidad de sus obligaciones. Tampoco se considerarán dentro de ese concepto las refinanciaciones otorgadas a los produc- tores agropecuarios cuando ello resulte de la aplicación de disposiciones vinculadas a la Ley de Emergencia Agropecuaria, sin perjuicio de lo cual, a los fines de la clasificación, deberá tenerse en cuenta el flujo de fondos proyectado para el momento en que concluya la vigencia de la emergencia declarada. El tratamiento que se dispense en ese marco no podrá implicar mejora- miento de la clasificación asignada al cliente en función de su situación individual, preexistente a la emergencia, ni su aplicación extenderse más allá de la vigencia fijada para ella.
  - [encabezado, 6.5.5, p. [28]] 6.5.5. Irrecuperable.
  - [intro, 6.5.5, p. [28]] Las deudas de clientes incorporados a esta categoría se consideran incobrables. Si bien estos activos podrían tener algún valor de recuperación bajo un cierto conjunto de cir- cunstancias futuras, su incobrabilidad es evidente al momento del análisis. Entre los indicadores que pueden reflejar esta situación se destacan que el cliente:
  - [cierre, 6.5.5, p. [31]] Además, corresponderá clasificar en esta categoría a los clientes que, cualquiera sea el motivo (entre ellos por no contar con legajo o por no haber proporcionado información confiable y/o actualizada), no hayan sido evaluados con la periodicidad correspondiente, con excepción de los deudores en concurso o con acuerdo preventivo extrajudicial solici- tado o en gestión judicial que, por un período de hasta 540 días contados a partir de la apertura del concurso, solicitud del acuerdo preventivo o inicio de las gestiones judiciales de cobro, según corresponda, no hubiesen presentado la documentación que permita realizarla, siempre que se cuente con informe de abogado de la entidad financiera acreedora sobre la razonabilidad del recupero de los créditos comprendidos. Ello, sin perjuicio de que se trate de deudas que reúnan todas las condiciones previstas por el punto 2.2.3.2. de las normas sobre “Previsiones mínimas por riesgo de incobrabili- dad”.
- **Texto propio** («Incurra en atrasos superiores a un año, cuente con refinanciación del capital y»):

```text
6.5.5.2. Incurra en atrasos superiores a un año, cuente con refinanciación del capital y
sus intereses y con financiación de pérdidas de explotación. A este fin, el cóm-
puto de los plazos no se interrumpirá por el otorgamiento de renovaciones cuan-
do previamente no se haya producido la cancelación efectiva de las obligaciones
vencidas, es decir sin recurrir a financiación directa o indirecta de la entidad.
Cuando al menos se haya cumplido con el pago, sin haber incurrido en atrasos
superiores a los 31 días del 15 % de las obligaciones refinanciadas y la totalidad
de los intereses devengados, podrá reclasificarse al deudor en el nivel inmediato
superior si, además, se observan las otras condiciones previstas en el citado ni-
vel.
El deudor que, encontrándose clasificado en esta categoría, haya refinanciado
su deuda –aun cuando haya cancelado el porcentaje establecido en el párrafo
precedente– y recibido crédito adicional en los términos a que se refiere el punto
2.2.5. de las normas sobre “Previsiones mínimas por riesgo de incobrabilidad”, y
en la medida en que dicha financiación adicional no hubiese sido cancelada, de-
berá permanecer en esta categoría por lo menos 180 días contados desde la fe-
cha en que se otorgó crédito adicional o desde que se celebró el acuerdo de re-
financiación, la circunstancia más reciente.
```

## F40

- **Predicado:** `condicion_de`
- **Origen:** Condicion — «Cumplimiento de condiciones y requisitos punto 7.11» (`Condicion_cumplimiento_de_condiciones_y_requisitos_punto_7_11__las_financiaciones_deben_cu_6d9f97`)
  - descripción (salida del extractor): Las financiaciones deben cumplir las condiciones y requisitos previstos en el punto 7.11.
  - tramo de E1 en la unidad (salida del extractor): 'que cumplan las condiciones y requisitos previstos en el punto 7.11'
- **Destino:** Operacion — «Financiaciones comerciales o financieras — importaciones de bienes» (`Operacion_financiaciones_comerciales_o_financieras_importaciones_de_bienes__ext_7_3_10_abb286`)
  - descripción (salida del extractor): Financiaciones comerciales o financieras asociadas a la realización de pagos diferidos o a la vista de importaciones de bienes que cumplan las condiciones y requisitos previstos en el punto 7.11.
  - tramo de E1 en la unidad (salida del extractor): 'Financiaciones comerciales o financieras asociadas a la realización de pagos diferidos o a la vista de importaciones de bienes'
- **Unidad:** `ext::7.3.10` (ext, punto 7.3.10, punto_propio)
- **Páginas:** unidad [85], arista [85]; PDF `data/experiment/subset/TO_exterior_cambios_actual.pdf`
- **Render:** `paginas/ext_p83.png`, `paginas/ext_p85.png`
- **Texto heredado:**
  - [encabezado, S7, p. [80]] Sección 7. Cobros de exportaciones de bienes.
  - [encabezado, 7.3, p. [83]] 7.3. Aplicación de divisas de cobros de exportaciones.
  - [intro, 7.3, p. [83]] Existe una aplicación de divisas de cobros de exportaciones de bienes cuando se ha certificado que los propios bienes exportados o las divisas cobradas por ellos fueron utilizados para cancelar el capital, intereses y/o gastos de otorgamiento de operaciones de financiamiento, pagar utilidades y dividendos y/o concretar la repatriación de una inversión directa de un accionista no residente en los casos admitidos en los puntos 7.3.1. a 7.3.11. A los efectos que los cobros de exportaciones aplicados puedan ser imputados al cumplimiento de los permisos de embarque oficializados a partir del 02/09/19, será necesario contar en todos los casos con una certificación de aplicación emitida por la entidad encargada del “Seguimiento de anticipos y otras financiaciones de exportación de bienes”. Los exportadores que efectúen liquidaciones de moneda extranjera asociadas a las operaciones comprendidas en los puntos 7.3.1. al 7.3.10. deberán solicitar a la entidad interviniente que le asigne un número de identificación (número APX) y la incorpore al mencionado seguimiento. En el caso de operaciones comprendidas en el punto 7.3.8. que no registren liquidaciones en el mercado de cambios por ser refinanciaciones de deudas preexistentes, la entidad nominada por el exportador atento a lo establecido en el punto 7.9.3. deberá incorporarla al mencionado seguimiento, usando para su identificación el número correlativo que se le asignó a la operación del cliente (número ECO: Entidad-CUIT-N° Operación).
- **Texto propio** («Financiaciones asociadas a importaciones de bienes habilitadas para la aplicación de»):

```text
7.3.10. Financiaciones asociadas a importaciones de bienes habilitadas para la aplicación de
cobros de exportaciones de bienes
Financiaciones comerciales o financieras asociadas a la realización de pagos diferidos
o a la vista de importaciones de bienes que cumplan las condiciones y requisitos
previstos en el punto 7.11.
```

## F41

- **Predicado:** `condicion_de`
- **Origen:** Condicion — «Observancia de requisitos para clasificación como PNb» (`Condicion_observancia_de_requisitos_para_clasificacion_como_pnb__que_los_instrumentos_en_p_dc561c`)
  - descripción (salida del extractor): Que los instrumentos en poder de terceros observen todos los requisitos para su clasificación como PNb a efectos de la RPC.
  - tramo de E1 en la unidad (salida del extractor): 'si observan todos los requisitos para su clasificación como PNb a efectos de la RPC'
- **Destino:** Operacion — «Reconocimiento de PNb de subsidiaria en PNb de entidad financiera» (`Operacion_reconocimiento_de_pnb_de_subsidiaria_en_pnb_de_entidad_financiera__cap_8_3_5_2_59d1b9`)
  - descripción (salida del extractor): Reconocimiento en el PNb de la entidad financiera de instrumentos en poder de terceros que conforman el PNb de una subsidiaria sujeta a supervisión consolidada, condicionado a que observen todos los requisitos para su clasificación como PNb a efectos de la RPC.
  - tramo de E1 en la unidad (salida del extractor): 'Los instrumentos en poder de terceros que conforman el PNb de una subsidiaria sujeta a supervisión consolidada pueden reconocerse en el PNb de la entidad financiera si observan todos los requisitos para su clasificación como PNb a efectos de la RPC.'
- **Unidad:** `cap::8.3.5.2` (cap, punto 8.3.5.2, punto_propio)
- **Páginas:** unidad [161], arista [161]; PDF `data/experiment/subset/TO_capitales_minimos_actual.pdf`
- **Render:** `paginas/cap_p160.png`, `paginas/cap_p161.png`
- **Texto heredado:**
  - [encabezado, S8, p. [154]] Sección 8. Responsabilidad patrimonial computable.
  - [encabezado, 8.3, p. [156]] 8.3. Criterios relacionados con los conceptos computables.
  - [encabezado, 8.3.5, p. [160]] 8.3.5. Participaciones minoritarias –no confieren control– y otros instrumentos computables
  - [intro, 8.3.5, p. [160]] como capital emitidos por subsidiarias sujetas a supervisión consolidada en poder de terceros.
- **Texto propio** («PNb emitido por subsidiarias sujetas a supervisión consolidada.»):

```text
8.3.5.2. PNb emitido por subsidiarias sujetas a supervisión consolidada.
Los instrumentos en poder de terceros que conforman el PNb de una subsidia-
ria sujeta a supervisión consolidada pueden reconocerse en el PNb de la enti-
dad financiera si observan todos los requisitos para su clasificación como PNb a
efectos de la RPC.
El importe que se reconocerá en el PNb de la entidad financiera será el importe
de la participación minoritaria en el PNb de la subsidiaria neto del excedente de
PNb de la subsidiaria que corresponde a los inversores minoritarios.
El excedente de PNb de la subsidiaria se calcula como el PNb de la subsidiaria
neto del menor de los siguientes importes:
i) su requerimiento mínimo de PNb más su margen de conservación de capital;
ii) la porción correspondiente a la subsidiaria del requerimiento mínimo de PNb
más el margen de conservación de capital, ambos computados sobre base
consolidada.
El excedente de PNb atribuible a los inversores minoritarios resultará de multi-
plicar el excedente de PNb de la subsidiaria –determinado conforme lo señalado
precedentemente– por el porcentaje de PNb en poder de inversores minorita-
rios.
El importe de este PNb que será admisible como CA excluye los importes re-
n1
conocidos como CO en orden a lo establecido en el punto 8.3.5.1.
n1
```

## F42

- **Predicado:** `condicion_de`
- **Origen:** Condicion — «Elegibilidad según punto 4.4» (`Condicion_elegibilidad_segun_punto_4_4__los_pagos_deben_resultar_elegibles_de_acuerdo_con__24608a`)
  - descripción (salida del extractor): Los pagos deben resultar elegibles de acuerdo con lo dispuesto en el punto 4.4
  - tramo de E1 en la unidad (salida del extractor): 'que resultaban elegibles de acuerdo con lo dispuesto en el punto 4.4'
- **Destino:** Potestad — «Acceso mercado cambios mediante canje/arbitraje BOPREAL» (`Potestad_acceso_mercado_cambios_mediante_canje_arbitraje_bopreal__los_clientes_tienen_la__855fb4`)
  - descripción (salida del extractor): Los clientes tienen la facultad de acceder al mercado de cambios mediante la realización de un canje y/o arbitraje con fondos depositados en cuenta local originados en cobros de capital e intereses en moneda extranjera de bonos BOPREAL, en la medida que se cumplan los requisitos aplicables
  - tramo de E1 en la unidad (salida del extractor): 'Los clientes podrán, en la medida que se cumplan los requisitos aplicables, acceder al mercado de cambios mediante la realización de un canje y/o arbitraje con los fondos depositados en una cuenta local y originados en cobros de capital e intereses en moneda extranjera de los bonos BOPREAL'
- **Unidad:** `ext::4.8.1.1` (ext, punto 4.8.1.1, punto_propio)
- **Páginas:** unidad [64], arista [64]; PDF `data/experiment/subset/TO_exterior_cambios_actual.pdf`
- **Render:** `paginas/ext_p64.png`, `paginas/ext_p65.png`
- **Texto heredado:**
  - [encabezado, S4, p. [56]] Sección 4. Otras disposiciones específicas.
  - [encabezado, 4.8, p. [64]] 4.8. Disposiciones complementarias asociadas a los Bonos para la Reconstrucción de una
  - [intro, 4.8, p. [64]] Argentina Libre (BOPREAL).
  - [encabezado, 4.8.1, p. [64]] 4.8.1. Los clientes podrán, en la medida que se cumplan los requisitos aplicables, acceder al
  - [intro, 4.8.1, p. [64]] mercado de cambios mediante la realización de un canje y/o arbitraje con los fondos depositados en una cuenta local y originados en cobros de capital e intereses en moneda extranjera de los bonos BOPREAL para concretar:
  - [cierre, 4.8.1, p. [65]] También se podrán considerar comprendidos en los puntos 4.8.1.1. y 4.8.1.2. a aquellos pagos elegibles que se cursen por el Sistema de Moneda Locales (SML) a partir de la venta de fondos depositados en una cuenta local y originados en cobros de capital e intereses en moneda extranjera de los bonos BOPREAL.
- **Texto propio** («el pago de deudas comerciales por importaciones de bienes con registro de»):

```text
4.8.1.1. el pago de deudas comerciales por importaciones de bienes con registro de
ingreso aduanero hasta el 12/12/23, que resultaban elegibles de acuerdo con
lo dispuesto en el punto 4.4.
```

## F43

- **Predicado:** `condicion_de`
- **Origen:** Condicion — «Registro de ingreso aduanero del bien de capital» (`Condicion_registro_de_ingreso_aduanero_del_bien_de_capital__el_vpu_debe_demostrar_el_regis_7a29c7`)
  - descripción (salida del extractor): El VPU debe demostrar el registro de ingreso aduanero del bien de capital por un valor consistente con el monto del aporte a computar.
  - tramo de E1 en la unidad (salida del extractor): 'El VPU haya demostrado el registro de ingreso aduanero del bien de capital por un valor consistente con el monto del aporte que será computado como ingresado y liquidado en el mercado de cambios'
- **Destino:** Operacion — «Cómputo de aportes inversión directa en especie» (`Operacion_computo_de_aportes_inversion_directa_en_especie__ext_14_5_7_97c0f6`)
  - descripción (salida del extractor): Aportes de inversión directa en especie instrumentados mediante la entrega al VPU de bienes de capital que pueden ser computados como ingresados y liquidados en el mercado de cambios, sujeto a cumplimiento de condiciones específicas.
  - tramo de E1 en la unidad (salida del extractor): 'Los aportes de inversión directa en especie instrumentados mediante la entrega al VPU de bienes de capital podrán ser computados como ingresados y liquidados en el mercado de cambios'
- **Unidad:** `ext::14.5.7` (ext, punto 14.5.7, punto_propio)
- **Páginas:** unidad [182, 183], arista [182, 183]; PDF `data/experiment/subset/TO_exterior_cambios_actual.pdf`
- **Render:** `paginas/ext_p175.png`, `paginas/ext_p182.png`, `paginas/ext_p183.png`
- **Texto heredado:**
  - [encabezado, S14, p. [175]] Sección 14. Disposiciones complementarias asociadas al Régimen de Incentivo para Grandes Inversiones (RIGI).
  - [chapeau_seccion, S14, p. [175]] En esta sección se detallan las disposiciones complementarias en materia cambiaria que, en la medida que las disposiciones generales no resulten más favorables, resultan aplicables a un Vehículo de Proyecto Único (VPU) adherido al Régimen de Incentivo los referidas al “Régimen de Incentivo para Grandes Inversiones” (RIGI) establecido en el Título VII de la Ley 27.742 y reglamentado por el Decreto 749/24 y concordantes.
  - [encabezado, 14.5, p. [180]] 14.5. Otras disposiciones.
- **Texto propio** («Los aportes de inversión directa en especie instrumentados mediante la entrega al»):

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

## F44

- **Predicado:** `condicion_de`
- **Origen:** Condicion — «Posiciones arancelarias no comprendidas en punto 12.1» (`Condicion_posiciones_arancelarias_no_comprendidas_en_punto_12_1__las_posiciones_arancelari_de37f3`)
  - descripción (salida del extractor): Las posiciones arancelarias de los bienes no deben corresponder a aquellas comprendidas en el punto 12.1
  - tramo de E1 en la unidad (salida del extractor): 'las posiciones arancelarias de los bienes no correspondan a aquellas comprendidas en el punto 12.1'
- **Destino:** Operacion — «Pagos a la vista — importaciones de bienes» (`Operacion_pagos_a_la_vista_importaciones_de_bienes__ext_10_10_2_1_879d77`)
  - descripción (salida del extractor): Pagos a la vista de importaciones de bienes cursados por personas humanas o personas jurídicas que clasifiquen como MiPyMe según lo dispuesto en las normas de 'Determinación de la condición de micro, pequeña y mediana empresa'
  - tramo de E1 en la unidad (salida del extractor): 'Pagos a la vista de importaciones de bienes cursados por personas humanas o personas jurídicas que clasifiquen como MiPyMe'
- **Unidad:** `ext::10.10.2.1` (ext, punto 10.10.2.1, punto_propio)
- **Páginas:** unidad [154], arista [154]; PDF `data/experiment/subset/TO_exterior_cambios_actual.pdf`
- **Render:** `paginas/ext_p154.png`, `paginas/ext_p157.png`
- **Texto heredado:**
  - [encabezado, S10, p. [130]] Sección 10. Pagos de importaciones y otras compras de bienes en el exterior.
  - [encabezado, 10.10, p. [154]] 10.10. Disposiciones complementarias para importaciones de bienes que tuvieron o tendrán registro
  - [intro, 10.10, p. [154]] de ingreso aduanero a partir del 13/12/23.
  - [encabezado, 10.10.2, p. [154]] 10.10.2. Pagos de importaciones de bienes con registro de ingreso aduanero pendiente.
  - [intro, 10.10.2, p. [154]] Las entidades podrán dar acceso al mercado de cambios para cursar pagos con registro de ingreso aduanero pendiente por operaciones no comprendidas en el punto 10.6.6. cuando, en adición a los restantes requisitos aplicables, se verifique alguna de las siguientes situaciones:
  - [cierre, 10.10.2, p. [157]] Se podrá considerar como importación de bienes de capital a: i) aquellas que correspondan a bienes cuyas posiciones arancelarias se encuentren clasificadas como BK en la Nomenclatura Común del MERCOSUR (Decreto 690/02 y complementarias) y ii) aquellas que incluyan otros bienes en la medida que los bienes clasificados como BK representen como mínimo el 90% (noventa por ciento) del valor FOB total de la operación y la entidad cuente con una declaración jurada del cliente en la cual deje constancia de que los restantes bienes son repuestos, accesorios o materiales necesarios para el funcionamiento, construcción o instalación de los bienes de capital que se están adquiriendo.
- **Texto propio** («Pagos a la vista de importaciones de bienes cursados por personas»):

```text
10.10.2.1. Pagos a la vista de importaciones de bienes cursados por personas
humanas o personas jurídicas que clasifiquen como MiPyMe según lo
dispuesto en las normas de "Determinación de la condición de micro,
pequeña y mediana empresa", en la medida que se trate de bienes
que hayan sido embarcados en origen a partir del 14/04/25 y las
posiciones arancelarias de los bienes no correspondan a aquellas
comprendidas en el punto 12.1.
```

## F45

- **Predicado:** `condicion_de`
- **Origen:** Condicion — «Falta de autorización para girar en descubierto» (`Condicion_falta_de_autorizacion_para_girar_en_descubierto__supuesto_de_inclusion_en_la_cen_d4a9c1`)
  - descripción (salida del extractor): Supuesto de inclusión en la Central de cheques rechazados: falta de autorización para girar en descubierto
  - tramo de E1 en la unidad (salida del extractor): 'falta de autorización para girar en descubierto'
- **Destino:** Operacion — «Rechazo de cheques por falta de fondos o autorización» (`Operacion_rechazo_de_cheques_por_falta_de_fondos_o_autorizacion__ctacte_8_2_1_1_6433fa`)
  - descripción (salida del extractor): Rechazo de cheques comunes o de pago diferido por falta de fondos suficientes disponibles en cuenta o por falta de autorización para girar en descubierto
  - tramo de E1 en la unidad (salida del extractor): 'rechazos de cheques -comunes o de pago diferido- por: [...] Falta de fondos suficientes disponibles en cuenta o de autorización para girar en descubierto'
- **Unidad:** `ctacte::8.2.1.1` (ctacte, punto 8.2.1.1, punto_propio)
- **Páginas:** unidad [44], arista [44]; PDF `data/experiment/escalado_prep/pdfs/ctacte.pdf`
- **Render:** `paginas/ctacte_p44.png`
- **Texto heredado:**
  - [encabezado, S8, p. [44]] Sección 8. “Central de cheques rechazados”, “Central de cuentacorrentistas inhabili- tados” y “Central de cheques denunciados como extraviados, sustraídos o adulterados”.
  - [encabezado, 8.2, p. [44]] 8.2. Motivos de inclusión.
  - [encabezado, 8.2.1, p. [44]] 8.2.1. En la “Central de cheques rechazados”.
  - [intro, 8.2.1, p. [44]] Haber incurrido en uno o varios rechazos de cheques -comunes o de pago diferido- por:
- **Texto propio** («Falta de fondos suficientes disponibles en cuenta o de autorización para girar en»):

```text
8.2.1.1. Falta de fondos suficientes disponibles en cuenta o de autorización para girar en
descubierto.
```

## F46

- **Predicado:** `condicion_de`
- **Origen:** Condicion — «Cumplimiento de condiciones para ingreso de divisas» (`Condicion_cumplimiento_de_condiciones_para_ingreso_de_divisas__el_ingreso_de_divisas_a_tra_685701`)
  - descripción (salida del extractor): El ingreso de divisas a través de empresa procesadora de pagos requiere el cumplimiento de condiciones que se enumeran a continuación
  - tramo de E1 en la unidad (salida del extractor): 'en la medida que se cumplan las siguientes condiciones'
- **Destino:** Operacion — «Ingreso de divisas a través de empresa procesadora de pagos» (`Operacion_ingreso_de_divisas_a_traves_de_empresa_procesadora_de_pagos__ext_5_8_2_22cbc5`)
  - descripción (salida del extractor): Ingreso de divisas a nombre de la empresa local que actúa como representante en el país de la empresa procesadora de pagos
  - tramo de E1 en la unidad (salida del extractor): 'Ingresos de divisas a través de empresas procesadores de pagos'
- **Unidad:** `ext::5.8.2::intro` (ext, punto 5.8.2, bloque_intro)
- **Páginas:** unidad [71], arista [71]; PDF `data/experiment/subset/TO_exterior_cambios_actual.pdf`
- **Render:** `paginas/ext_p71.png`
- **Texto heredado:**
  - [encabezado, S5, p. [68]] Sección 5. Pautas operativas.
  - [encabezado, 5.8, p. [71]] 5.8. Boletos globales diarios.
  - [encabezado, 5.8.2, p. [71]] 5.8.2. Ingresos de divisas a través de empresas procesadores de pagos.
- **Texto propio** («[bloque intro] Ingresos de divisas a través de empresas procesadores de pagos.»):

```text
A nombre de la empresa local que actúa como representante en el país de la empresa
procesadora de pagos en la medida que se cumplan las siguientes condiciones:
```

## F47

- **Predicado:** `condicion_de`
- **Origen:** Condicion — «Cliente con financiaciones por ambos conceptos» (`Condicion_cliente_con_financiaciones_por_ambos_conceptos__supuesto_en_que_el_cliente_manti_a4cd0d`)
  - descripción (salida del extractor): Supuesto en que el cliente mantiene financiaciones de naturaleza comercial y créditos para consumo o vivienda simultáneamente
  - tramo de E1 en la unidad (salida del extractor): 'Cuando el cliente mantenga financiaciones por ambos conceptos'
- **Destino:** Operacion — «Suma de créditos para consumo o vivienda a cartera comercial para encuadramiento» (`Operacion_suma_de_creditos_para_consumo_o_vivienda_a_cartera_comercial_para_encuadramiento_1e1730`)
  - descripción (salida del extractor): Cuando el cliente mantiene financiaciones por ambos conceptos, los créditos para consumo o vivienda se suman a los de cartera comercial para determinar encuadramiento, ponderando créditos con garantías preferidas al 50%
  - tramo de E1 en la unidad (salida del extractor): 'los créditos para consumo o vivienda se sumarán a los de la cartera comercial para determinar su encuadramiento en una o en otra cartera en función del importe indicado, a cuyo fin los créditos con garantías preferidas se ponderarán al 50 %'
- **Unidad:** `cla::5.1.1.2` (cla, punto 5.1.1.2, punto_propio)
- **Páginas:** unidad [16], arista [16]; PDF `data/experiment/subset/TO_clasificacion_deudores_actual.pdf`
- **Render:** `paginas/cla_p16.png`
- **Texto heredado:**
  - [encabezado, S5, p. [16]] Sección 5. Categorías de carteras.
  - [encabezado, 5.1, p. [16]] 5.1. Categorías.
  - [intro, 5.1, p. [16]] La cartera se agrupará en dos categorías básicas:
  - [encabezado, 5.1.1, p. [16]] 5.1.1. Cartera comercial.
  - [intro, 5.1.1, p. [16]] Abarca todas las financiaciones comprendidas, con excepción de las siguientes:
- **Texto propio** («A opción de la entidad, las financiaciones de naturaleza comercial de hasta el»):

```text
5.1.1.2. A opción de la entidad, las financiaciones de naturaleza comercial de hasta el
equivalente a dos veces el importe de referencia establecido en el punto 3.7.,
cuenten o no con garantías preferidas, podrán agruparse junto con los créditos
para consumo o vivienda, en cuyo caso recibirán el tratamiento previsto para es-
tos últimos.
Cuando el cliente mantenga financiaciones por ambos conceptos, los créditos
para consumo o vivienda se sumarán a los de la cartera comercial para determi-
nar su encuadramiento en una o en otra cartera en función del importe indicado,
a cuyo fin los créditos con garantías preferidas se ponderarán al 50 %.
De ejercerse, esta opción deberá aplicarse con carácter general a toda la cartera
y encontrarse prevista en el “Manual de procedimientos de clasificación y previ-
sión” y sólo podrá cambiarse con un preaviso de 6 meses a la Superintendencia
de Entidades Financieras y Cambiarias (SEFyC).
```

## F48

- **Predicado:** `condicion_de`
- **Origen:** Condicion — «Acreditación de ingresos de divisas en cuenta» (`Condicion_acreditacion_de_ingresos_de_divisas_en_cuenta__la_emision_de_certificaciones_est_dff83f`)
  - descripción (salida del extractor): La emisión de certificaciones está condicionada a que en la cuenta de la entidad se hayan acreditado ingresos de divisas.
  - tramo de E1 en la unidad (salida del extractor): 'en la medida que en la cuenta de la entidad se hayan acreditado ingresos de divisas'
- **Destino:** Potestad — «Emisión de certificaciones de aplicación de divisas» (`Potestad_emision_de_certificaciones_de_aplicacion_de_divisas__las_entidades_autorizadas_p_2b3f22`)
  - descripción (salida del extractor): Las entidades autorizadas podrán emitir certificaciones de aplicación de divisas a la cancelación del capital y/o intereses que correspondan proporcionalmente al monto liquidado.
  - tramo de E1 en la unidad (salida del extractor): 'Se podrán emitir las certificaciones de aplicación de las divisas a la cancelación del capital y/o intereses que correspondan proporcionalmente al monto liquidado'
- **Unidad:** `ext::9.3.5::intro` (ext, punto 9.3.5, bloque_intro)
- **Páginas:** unidad [126], arista [126]; PDF `data/experiment/subset/TO_exterior_cambios_actual.pdf`
- **Render:** `paginas/ext_p126.png`
- **Texto heredado:**
  - [encabezado, S9, p. [123]] Sección 9. Seguimiento de anticipos y otras financiaciones de exportación de bienes.
  - [encabezado, 9.3, p. [124]] 9.3. Certificaciones de aplicación de cobros de exportaciones.
  - [encabezado, 9.3.5, p. [126]] 9.3.5. Posfinanciaciones de entidades financieras locales por descuentos y/o cesiones.
- **Texto propio** («[bloque intro] Posfinanciaciones de entidades financieras locales por descuentos y/o cesiones.»):

```text
Se podrán emitir las certificaciones de aplicación de las divisas a la cancelación del
capital y/o intereses que correspondan proporcionalmente al monto liquidado, en la
medida que en la cuenta de la entidad se hayan acreditado ingresos de divisas que
correspondan a:
```

## F49

- **Predicado:** `condicion_de`
- **Origen:** Condicion — «Activos utilizados durante la jornada para pagos en mercado local» (`Condicion_activos_utilizados_durante_la_jornada_para_pagos_en_mercado_local__los_activos_e_0f64f8`)
  - descripción (salida del extractor): Los activos externos líquidos fueron utilizados durante esa jornada para realizar pagos que hubieran tenido acceso al mercado local de cambios
  - tramo de E1 en la unidad (salida del extractor): 'fueron utilizados durante esa jornada para realizar pagos que hubieran tenido acceso al mercado local de cambios'
- **Destino:** Potestad — «Facultad de aceptar declaración jurada cuando activos externos líquidos superan USD 100.000» (`Potestad_facultad_de_aceptar_declaracion_jurada_cuando_activos_externos_liquidos_superan__df94d9`)
  - descripción (salida del extractor): Cuando el cliente tiene activos externos líquidos disponibles y/o CEDEARs por monto superior a USD 100.000, la entidad podrá aceptar una declaración jurada del cliente en la que conste que no se excede tal monto considerando que, parcial o totalmente, los activos externos líquidos se encuentran en alguna de las situaciones descritas en los incisos i) a vii)
  - tramo de E1 en la unidad (salida del extractor): 'En el caso de que el cliente tuviera activos externos líquidos disponibles y/o CEDEARs por un monto superior al establecido en el primer párrafo, la entidad también podrá aceptar una declaración jurada del cliente en la que deje constancia que no se excede tal monto al considerar que, parcial o totalmente, los activos externos líquidos:'
- **Unidad:** `ext::3.16.2.1` (ext, punto 3.16.2.1, punto_propio)
- **Páginas:** unidad [43, 44], arista [43, 44]; PDF `data/experiment/subset/TO_exterior_cambios_actual.pdf`
- **Render:** `paginas/ext_p16.png`, `paginas/ext_p43.png`, `paginas/ext_p44.png`, `paginas/ext_p45.png`
- **Texto heredado:**
  - [encabezado, S3, p. [16]] Sección 3. Disposiciones específicas para los egresos por el mercado de cambios
  - [chapeau_seccion, S3, p. [16]] Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–, adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables.
  - [encabezado, 3.16, p. [42]] 3.16. Requisitos complementarios para los egresos por el mercado de cambios.
  - [encabezado, 3.16.2, p. [43]] 3.16.2. Declaración jurada del cliente respecto a sus tenencias de activos externos líquidos
  - [intro, 3.16.2, p. [43]] y/o certificados de depósitos argentinos representativos de acciones extranjeras. La entidad deberá contar con la conformidad previa del BCRA excepto que cuente al momento de acceso al mercado de cambios con una declaración jurada del cliente en la que deje constancia de que:
  - [cierre, 3.16.2, p. [44]] Este requisito no resultará a aplicación para aquellas operaciones de egresos que correspondan a:
  - [cierre, 3.16.2, p. [44]] i) operaciones de clientes realizadas en el marco de los puntos 3.8., 3.9., 3.13.,
  - [cierre, 3.16.2, p. [44]] 3.14.1. y 3.14.2.;
  - [cierre, 3.16.2, p. [44, 45]] ii) operaciones propias de una entidad en carácter de cliente; iii) cancelaciones de financiaciones en moneda extranjera otorgadas por entidades
  - [cierre, 3.16.2, p. [45]] financieras locales por los consumos en moneda extranjera efectuados mediante tarjetas de crédito o de compra; o
  - [cierre, 3.16.2, p. [45]] iv) pagos al exterior de las empresas no financieras emisoras de tarjetas por el uso
  - [cierre, 3.16.2, p. [45]] de tarjetas de crédito, de compra, de débito o prepagas emitidas en el país.
- **Texto propio** («La totalidad de sus tenencias de moneda extranjera en el país se»):

```text
3.16.2.1. La totalidad de sus tenencias de moneda extranjera en el país se
encuentran depositadas en cuentas en entidades financieras y que no
poseía, al inicio del día en que solicita el acceso al mercado, certificados de
depósitos argentinos representativos de acciones extranjeras (CEDEARs)
y/o activos externos líquidos disponibles que conjuntamente tengan un
valor superior al equivalente de USD 100.000 (dólares estadounidenses
cien mil).
Serán considerados activos externos líquidos, entre otros: las tenencias de
billetes y monedas en moneda extranjera, disponibilidades en oro
amonedado o en barras de buena entrega, depósitos a la vista en
entidades financieras del exterior y otras inversiones que permitan obtener
disponibilidad inmediata de moneda extranjera (por ejemplo, inversiones en
títulos públicos externos con custodia en el país o en el exterior, fondos en
cuentas de inversión en administradores de inversiones radicados en el
exterior, criptoactivos, fondos en cuentas de proveedores de servicios de
pago, etc.).
No deben considerarse activos externos líquidos disponibles a aquellos
fondos depositados en el exterior que no pudiesen ser utilizados por el
cliente por tratarse de fondos de reserva o de garantía constituidos en
virtud de las exigencias previstas en contratos de endeudamiento con el
exterior, prefinanciaciones de exportaciones comprendidas en el punto
7.8.5. o de fondos constituidos como garantía de operaciones con
derivados concertadas en el exterior.
En el caso de que el cliente tuviera activos externos líquidos disponibles y/o
CEDEARs por un monto superior al establecido en el primer párrafo, la
entidad también podrá aceptar una declaración jurada del cliente en la que
deje constancia que no se excede tal monto al considerar que, parcial o
totalmente, los activos externos líquidos:
i) fueron utilizados durante esa jornada para realizar pagos que
hubieran tenido acceso al mercado local de cambios;
ii) fueron transferidos a favor del cliente a una cuenta de corresponsalía
de una entidad local autorizada a operar en cambios;
iii) son fondos depositados en cuentas bancarias en el exterior a su
nombre que se originan en cobros de exportaciones de bienes y/o
servicios o anticipos, prefinanciaciones o posfinanciaciones de
exportaciones de bienes otorgados por no residentes, o en la
enajenación de activos no financieros no producidos para los cuales
no ha transcurrido el plazo de 20 (veinte) días hábiles desde su
percepción.
iv) son fondos depositados en cuentas bancarias en el exterior a su
nombre originados en endeudamientos financieros comprendidos en
el punto 3.5. y su monto no supera el equivalente a pagar por capital
e intereses en los próximos 365 (trescientos sesenta y cinco) días
corridos.
v) son fondos depositados en cuentas bancarias del exterior a su
nombre originados en los últimos 180 (ciento ochenta) días corridos
por desembolsos en el exterior recibidos a partir del 29/11/24 de
endeudamientos financieros comprendidos en el punto 3.5.
vi) son fondos depositados en cuentas bancarias del exterior a su
nombre originados en las ventas de títulos valores con liquidación en
moneda extranjera contempladas en el punto 3.16.3.6.iii).
vii) son fondos depositados en cuentas bancarias en el exterior a su
nombre originados en emisiones de títulos de deuda concretadas en
los 120 (ciento veinte) días corridos previos y susceptibles de ser
encuadradas en lo previsto en los puntos 7.11.1.5. y 7.11.1.6.
En esta última declaración jurada del cliente deberá constar expresamente
el valor de sus activos externos líquidos disponibles al inicio del día y los
montos que asigna a cada una de las situaciones descriptas en los incisos
i)a vii) que sean aplicables.
```

## F50

- **Predicado:** `condicion_de`
- **Origen:** Condicion — «Condición para extensión: utilización del mecanismo y fondos depositados» (`Condicion_condicion_para_extension_utilizacion_del_mecanismo_y_fondos_depositados__se_requ_3ca0fd`)
  - descripción (salida del extractor): Se requiere que el cliente haya utilizado este mecanismo para el monto pendiente de liquidación y que los fondos sigan depositados en la Cuenta especial para el régimen de fomento de la economía del conocimiento (Decreto 679/22) de su titularidad.
  - tramo de E1 en la unidad (salida del extractor): 'cuando, por el monto que se encuentre pendiente de liquidación, el cliente haya utilizado este mecanismo y los fondos sigan depositados en "Cuenta especial para el régimen de fomento de la economía del conocimiento. Decreto 679/22" de titularidad del cliente.'
- **Destino:** Potestad — «Extensión del plazo de liquidación del permiso» (`Potestad_extension_del_plazo_de_liquidacion_del_permiso__la_entidad_encargada_del_seguimi_fec2c5`)
  - descripción (salida del extractor): La entidad encargada del seguimiento del permiso de embarque está facultada a extender el plazo de liquidación del permiso cuando el cliente haya utilizado este mecanismo para el monto pendiente de liquidación y los fondos sigan depositados en la Cuenta especial para el régimen de fomento de la economía del conocimiento (Decreto 679/22) de su titularidad.
  - tramo de E1 en la unidad (salida del extractor): 'la entidad encargada del seguimiento del permiso de embarque podrá extender el plazo de liquidación del permiso cuando, por el monto que se encuentre pendiente de liquidación, el cliente haya utilizado este mecanismo y los fondos sigan depositados en "Cuenta especial para el régimen de fomento de la economía del conocimiento. Decreto 679/22" de titularidad del cliente.'
- **Unidad:** `ext::7.8.4::cierre` (ext, punto 7.8.4, bloque_cierre)
- **Páginas:** unidad [93], arista [93]; PDF `data/experiment/subset/TO_exterior_cambios_actual.pdf`
- **Render:** `paginas/ext_p93.png`
- **Texto heredado:**
  - [encabezado, S7, p. [80]] Sección 7. Cobros de exportaciones de bienes.
  - [encabezado, 7.8, p. [91]] 7.8. Otras disposiciones.
  - [encabezado, 7.8.4, p. [93]] 7.8.4. Excepción de liquidación para cobros de exportaciones de bienes de beneficiarios del
- **Texto propio** («[bloque cierre] Excepción de liquidación para cobros de exportaciones de bienes de beneficiarios del»):

```text
Los montos de las divisas a ser afectadas en el marco de lo dispuesto en el capítulo II
del Decreto 679/22 no pueden resultar alcanzadas por ningún otro tratamiento
cambiario diferencial que no sea aquel previsto en dicho capítulo.
A los efectos del registro de estas operaciones se deberán confeccionar dos boletos
sin movimiento de pesos, el boleto de compra se realizará por el concepto de cobros
de exportaciones que corresponda y el boleto de venta deberá registrarse bajo el
código de concepto “A22. Acreditación de cobros de exportaciones de bienes y
servicios”.
La imputación del monto ingresado al cumplimiento del permiso de embarque requerirá
que el exportador presente, ante la entidad encargada de su seguimiento,
documentación que demuestre que se registraron por dicho monto transferencias en
moneda extranjera desde la “Cuenta especial para el régimen de fomento de la
economía del conocimiento. Decreto 679/22” por el pago de las remuneraciones de
personal en relación de dependencia.
Por otra parte, la entidad encargada del seguimiento del permiso de embarque podrá
extender el plazo de liquidación del permiso cuando, por el monto que se encuentre
pendiente de liquidación, el cliente haya utilizado este mecanismo y los fondos sigan
depositados en “Cuenta especial para el régimen de fomento de la economía del
conocimiento. Decreto 679/22” de titularidad del cliente.
```

## F51

- **Predicado:** `condicion_de`
- **Origen:** Condicion — «Contratos de venta en firme en moneda extranjera» (`Condicion_contratos_de_venta_en_firme_en_moneda_extranjera__que_cuenten_con_contratos_de_v_2d5333`)
  - descripción (salida del extractor): Que cuenten con contratos de venta en firme en moneda extranjera
  - tramo de E1 en la unidad (salida del extractor): 'y/o contratos de venta en firme en moneda extranjera'
- **Destino:** Operacion — «Financiación a productores de bienes exportables» (`Operacion_financiacion_a_productores_de_bienes_exportables__polcre_2_1_4_8d9c1f`)
  - descripción (salida del extractor): Financiación a productores de bienes para ser exportados, ya sea en el mismo estado o como parte integrante de otros bienes, realizada por terceros adquirentes de ellos
  - tramo de E1 en la unidad (salida del extractor): 'Financiaciones a productores de bienes para ser exportados, ya sea en el mismo estado o como parte integrante de otros bienes, por terceros adquirentes de ellos'
- **Unidad:** `polcre::2.1.4` (polcre, punto 2.1.4, punto_propio)
- **Páginas:** unidad [7], arista [7]; PDF `data/experiment/escalado_prep/pdfs/polcre.pdf`
- **Render:** `paginas/polcre_p6.png`, `paginas/polcre_p7.png`, `paginas/polcre_p8.png`, `paginas/polcre_p9.png`
- **Texto heredado:**
  - [encabezado, S2, p. [6]] Sección 2. Aplicación de la capacidad de préstamo de depósitos en moneda extranjera.
  - [encabezado, 2.1, p. [6]] 2.1. Destinos.
  - [intro, 2.1, p. [6]] La capacidad de préstamo de los depósitos en moneda extranjera deberá aplicarse, en la co- rrespondiente moneda de captación, en forma indistinta, a los siguientes destinos:
  - [cierre, 2.1, p. [8]] La aplicación de la capacidad de préstamo de depósitos en moneda extranjera a los destinos vinculados a operaciones de importación (previstos en los puntos 2.1.6., 2.1.7. y la parte atri- buible a éstos por aplicación de los puntos 2.1.8. y 2.1.9.), no podrá superar el valor que resulte de la siguiente expresión: C max (F / C ; 0,05)
  - [cierre, 2.1, p. [8]] x
  - [cierre, 2.1, p. [8]] t base base
  - [cierre, 2.1, p. [8]] Siendo: C: capacidad de préstamo del mes al que corresponda.
  - [cierre, 2.1, p. [8]] t
  - [cierre, 2.1, p. [9]] F : financiación de importaciones comprendidas, correspondientes al trimestre agos- base
  - [cierre, 2.1, p. [9]] to/octubre de 2008.
  - [cierre, 2.1, p. [9]] C : capacidad de préstamo que corresponda al trimestre agosto/octubre de 2008.
  - [cierre, 2.1, p. [9]] base
  - [cierre, 2.1, p. [9]] Las financiaciones y capacidad de préstamo deberán ser computadas de acuerdo con lo esta- blecido en el punto 2.5.
- **Texto propio** («Financiaciones a productores de bienes para ser exportados, ya sea en el mismo estado»):

```text
2.1.4. Financiaciones a productores de bienes para ser exportados, ya sea en el mismo estado
o como parte integrante de otros bienes, por terceros adquirentes de ellos, siempre que
cuenten con avales o garantías totales en moneda extranjera de dichos terceros y/o con-
tratos de venta en firme en moneda extranjera y/o en bienes exportables.
```

## F52

- **Predicado:** `condicion_de`
- **Origen:** Condicion — «Vencimiento del plazo sin oficialización permiso definitivo» (`Condicion_vencimiento_del_plazo_sin_oficializacion_permiso_definitivo__cuando_al_vencimien_98d21a`)
  - descripción (salida del extractor): Cuando al vencimiento del plazo no se hubiera oficializado aún el permiso de embarque definitivo
  - tramo de E1 en la unidad (salida del extractor): 'Cuando al vencimiento del plazo no se hubiera oficializado aún el permiso de embarque definitivo'
- **Destino:** Potestad — «Facultad otorgar cumplido permiso embarque provisorio» (`Potestad_facultad_otorgar_cumplido_permiso_embarque_provisorio__las_entidades_tienen_la_f_986dae`)
  - descripción (salida del extractor): Las entidades tienen la facultad de otorgar el cumplido del permiso de embarque provisorio considerando las imputaciones registradas hasta ese momento frente a los datos del permiso de embarque provisorio y documentación que justifique el monto liquidado por el exportador.
  - tramo de E1 en la unidad (salida del extractor): 'las entidades podrán otorgar el cumplido del permiso de embarque provisorio'
- **Unidad:** `ext::7.8.2.4` (ext, punto 7.8.2.4, punto_propio)
- **Páginas:** unidad [92], arista [92]; PDF `data/experiment/subset/TO_exterior_cambios_actual.pdf`
- **Render:** `paginas/ext_p91.png`, `paginas/ext_p92.png`
- **Texto heredado:**
  - [encabezado, S7, p. [80]] Sección 7. Cobros de exportaciones de bienes.
  - [encabezado, 7.8, p. [91]] 7.8. Otras disposiciones.
  - [encabezado, 7.8.2, p. [91]] 7.8.2. Exportaciones bajo los regímenes de precios revisables o concentrado de minerales.
  - [intro, 7.8.2, p. [91]] En los casos de exportaciones de productos que se comercializan sobre la base de precios FOB sujetos a una determinación posterior al momento de registro de la operación (Exportación de mercaderías con precios revisables – Resolución General 4073-E/17 de la Administración Federal de Ingresos Públicos) o al amparo del Régimen de Concentrados de Minerales (Resolución General 2108/06 de la Administración Federal de Ingresos Públicos) será aplicable lo siguiente:
- **Texto propio** («Cuando al vencimiento del plazo no se hubiera oficializado aún el permiso de»):

```text
7.8.2.4. Cuando al vencimiento del plazo no se hubiera oficializado aún el permiso de
embarque definitivo, las entidades podrán otorgar el cumplido del permiso de
embarque provisorio tomando en consideración las imputaciones registradas
hasta ese momento frente a los datos que surgen del permiso de embarque
provisorio y toda otra documentación que justifique el monto liquidado por el
exportador (tal es el caso de la factura por el monto correspondiente al
precio final).
En caso de que a esa fecha no hubiese sido posible determinar, por causas
ajenas a la voluntad del exportador, el precio definitivo de los bienes
comprendidos en la operación, el exportador podrá solicitar una extensión
del plazo a la entidad encargada del seguimiento en la medida que se
verifiquen las condiciones previstas en el punto 7.5.5.
```

## F53

- **Predicado:** `condicion_de`
- **Origen:** Condicion — «Operación declarada en presentación vencida de Relevamiento» (`Condicion_operacion_declarada_en_presentacion_vencida_de_relevamiento__la_operacion_debe_e_79ea4c`)
  - descripción (salida del extractor): La operación debe encontrarse declarada, en caso de corresponder, en la última presentación vencida del Relevamiento de activos y pasivos externos
  - tramo de E1 en la unidad (salida del extractor): 'la operación se encuentra declarada, en caso de corresponder, en la última presentación vencida del "Relevamiento de activos y pasivos externos"'
- **Destino:** Operacion — «Suscripción de BOPREAL por deudores de importaciones» (`Operacion_suscripcion_de_bopreal_por_deudores_de_importaciones__ext_4_4_fefb25`)
  - descripción (salida del extractor): Suscripción de Bonos para la Reconstrucción de una Argentina Libre (BOPREAL) por deudores de importaciones de bienes con registro de ingreso aduanero hasta el 12/12/23, por hasta el monto de la deuda pendiente de pago
  - tramo de E1 en la unidad (salida del extractor): 'Los importadores de bienes podrán suscribir Bonos para la Reconstrucción de una Argentina Libre (BOPREAL) por hasta el monto de la deuda pendiente de pago por sus importaciones de bienes con registro de ingreso aduanero hasta el 12/12/23.'
- **Unidad:** `ext::4.4.2` (ext, punto 4.4.2, punto_propio)
- **Páginas:** unidad [60], arista [60]; PDF `data/experiment/subset/TO_exterior_cambios_actual.pdf`
- **Render:** `paginas/ext_p60.png`
- **Texto heredado:**
  - [encabezado, S4, p. [56]] Sección 4. Otras disposiciones específicas.
  - [encabezado, 4.4, p. [60]] 4.4. Suscripción de bonos BOPREAL por parte de deudores de importaciones de bienes con
  - [intro, 4.4, p. [60]] registro de ingreso aduanero hasta el 12/12/23. Los importadores de bienes podrán suscribir Bonos para la Reconstrucción de una Argentina Libre (BOPREAL) por hasta el monto de la deuda pendiente de pago por sus importaciones de bienes con registro de ingreso aduanero hasta el 12/12/23. La entidad que concrete la oferta de suscripción en nombre del cliente deberá contar con las respectivas certificaciones sobre el monto pendiente de pago emitidas por la/s entidad/es encargada/s del seguimiento de las oficializaciones involucradas en el Seguimiento de Pagos de Importaciones de Bienes (SEPAIMPO), las cuales deberán verificar que:
  - [cierre, 4.4, p. [60]] En caso de que la importación de bienes encuadre en los puntos 10.3.3., 10.9.1., 10.9.2. y 10.9.3., la entidad que concrete la oferta de suscripción en nombre del cliente deberá verificar en forma directa lo previsto en los puntos 4.4.1. a 4.4.5. y, adicionalmente, contar con una declaración jurada del cliente en la que deja constancia de que no ha solicitado la utilización de este mecanismo en otra entidad por esa deuda. La entidad también deberá realizar la correspondiente intervención de la documentación aduanera. Adicionalmente, la mencionada entidad deberá realizar un boleto de venta de cambio a nombre del importador por el código de concepto “B26. Registro de importaciones de bienes por adjudicación de bonos BOPREAL”; consignando el valor nominal en moneda extranjera de bonos BOPREAL adjudicado al importador y el número de oficialización al que corresponde.
- **Texto propio** («la operación se encuentra declarada, en caso de corresponder, en la última»):

```text
4.4.2. la operación se encuentra declarada, en caso de corresponder, en la última
presentación vencida del "Relevamiento de activos y pasivos externos".
```

## F54

- **Predicado:** `condicion_de`
- **Origen:** Condicion — «Verificación de todas las condiciones» (`Condicion_verificacion_de_todas_las_condiciones__se_debe_verificar_que_se_cumplan_todas_la_b652de`)
  - descripción (salida del extractor): Se debe verificar que se cumplan todas las condiciones indicadas en cada caso para que la facultad de elaborar un boleto global diario sea ejercible.
  - tramo de E1 en la unidad (salida del extractor): 'en la medida que se verifiquen todas las condiciones indicadas en cada caso'
- **Destino:** Potestad — «Elaboración boleto global diario» (`Potestad_elaboracion_boleto_global_diario__las_entidades_estan_facultadas_a_elaborar_un_b_ac2b1a`)
  - descripción (salida del extractor): Las entidades están facultadas a elaborar un boleto global diario para las situaciones que se detallan a continuación, en la medida que se verifiquen todas las condiciones indicadas en cada caso.
  - tramo de E1 en la unidad (salida del extractor): 'Las entidades podrán elaborar un boleto global diario para las situaciones que se detallan a continuación'
- **Unidad:** `ext::5.8::intro` (ext, punto 5.8, bloque_intro)
- **Páginas:** unidad [71], arista [71]; PDF `data/experiment/subset/TO_exterior_cambios_actual.pdf`
- **Render:** `paginas/ext_p71.png`
- **Texto heredado:**
  - [encabezado, S5, p. [68]] Sección 5. Pautas operativas.
  - [encabezado, 5.8, p. [71]] 5.8. Boletos globales diarios.
- **Texto propio** («[bloque intro] Boletos globales diarios.»):

```text
Las entidades podrán elaborar un boleto global diario para las situaciones que se detallan a
continuación, en la medida que se verifiquen todas las condiciones indicadas en cada caso.
En todos los casos, se deberá requerir una lista detallada de los beneficiarios/ordenantes de
los pagos comprendidos en dicho boleto, debiendo como mínimo informar respecto de ellos:
nombres y apellidos completos o denominación social (según corresponda), CUIT, CUIL o CDI
y el monto que le corresponde.
```

## F55

- **Predicado:** `condicion_de`
- **Origen:** Condicion — «Operaciones compraventa títulos valores — liquidación extranjera/local» (`Condicion_operaciones_compraventa_titulos_valores_liquidacion_extranjera_local__por_la_por_d999e8`)
  - descripción (salida del extractor): Por la porción no liquidada del cobro, el cliente debe concretar operaciones de compraventa con títulos valores donde los títulos son adquiridos con liquidación en moneda extranjera y vendidos con liquidación en moneda local en el país.
  - tramo de E1 en la unidad (salida del extractor): 'por la porción no liquidada del cobro concretó operaciones de compraventa con títulos valores, en las cuales los títulos valores son adquiridos con liquidación en moneda extranjera y vendidos con liquidación en moneda local en el país'
- **Destino:** Potestad — «Admisión de aplicación divisas — porción no liquidada» (`Potestad_admision_de_aplicacion_divisas_porcion_no_liquidada__se_admite_la_aplicacion_de__b504f9`)
  - descripción (salida del extractor): Se admite la aplicación de divisas a la cancelación del capital e intereses de la porción no liquidada de anticipos, prefinanciaciones y posfinanciaciones del exterior conforme a los Decretos 492/23, 549/23, 597/23 y 28/23, sujeto al cumplimiento de las condiciones establecidas.
  - tramo de E1 en la unidad (salida del extractor): 'Se admitirá la aplicación de divisas a la cancelación del capital e intereses correspondiente a la porción no liquidada de anticipos, prefinanciaciones y posfinanciaciones del exterior a partir de lo dispuesto en los Decretos 492/23, 549/23, 597/23 y 28/23'
- **Unidad:** `ext::7.3.11` (ext, punto 7.3.11, punto_propio)
- **Páginas:** unidad [85], arista [85]; PDF `data/experiment/subset/TO_exterior_cambios_actual.pdf`
- **Render:** `paginas/ext_p83.png`, `paginas/ext_p85.png`
- **Texto heredado:**
  - [encabezado, S7, p. [80]] Sección 7. Cobros de exportaciones de bienes.
  - [encabezado, 7.3, p. [83]] 7.3. Aplicación de divisas de cobros de exportaciones.
  - [intro, 7.3, p. [83]] Existe una aplicación de divisas de cobros de exportaciones de bienes cuando se ha certificado que los propios bienes exportados o las divisas cobradas por ellos fueron utilizados para cancelar el capital, intereses y/o gastos de otorgamiento de operaciones de financiamiento, pagar utilidades y dividendos y/o concretar la repatriación de una inversión directa de un accionista no residente en los casos admitidos en los puntos 7.3.1. a 7.3.11. A los efectos que los cobros de exportaciones aplicados puedan ser imputados al cumplimiento de los permisos de embarque oficializados a partir del 02/09/19, será necesario contar en todos los casos con una certificación de aplicación emitida por la entidad encargada del “Seguimiento de anticipos y otras financiaciones de exportación de bienes”. Los exportadores que efectúen liquidaciones de moneda extranjera asociadas a las operaciones comprendidas en los puntos 7.3.1. al 7.3.10. deberán solicitar a la entidad interviniente que le asigne un número de identificación (número APX) y la incorpore al mencionado seguimiento. En el caso de operaciones comprendidas en el punto 7.3.8. que no registren liquidaciones en el mercado de cambios por ser refinanciaciones de deudas preexistentes, la entidad nominada por el exportador atento a lo establecido en el punto 7.9.3. deberá incorporarla al mencionado seguimiento, usando para su identificación el número correlativo que se le asignó a la operación del cliente (número ECO: Entidad-CUIT-N° Operación).
- **Texto propio** («Anticipos, prefinanciaciones y posfinanciaciones del exterior con liquidación parcial en»):

```text
7.3.11. Anticipos, prefinanciaciones y posfinanciaciones del exterior con liquidación parcial en
virtud de lo dispuesto por los Decretos 492/23, 549/23, 597/23 y 28/23.
Se admitirá la aplicación de divisas a la cancelación del capital e intereses
correspondiente a la porción no liquidada de anticipos, prefinanciaciones y
posfinanciaciones del exterior a partir de lo dispuesto en los Decretos 492/23, 549/23,
597/23 y 28/23, en la medida que el cliente demuestre que, durante sus respectivas
vigencias y en las condiciones estipuladas en los mencionados decretos, ingresó y
liquidó divisas en el mercado de cambios por un monto no menor al porcentaje mínimo
requerido de la operación y por la porción no liquidada del cobro concretó operaciones
de compraventa con títulos valores, en las cuales los títulos valores son adquiridos con
liquidación en moneda extranjera y vendidos con liquidación en moneda local en el
país.
La aplicación de la porción no liquidada deberá ser certificada por la entidad encargada
del "Seguimiento de anticipos y otras financiaciones de exportación de bienes" de la
porción liquidada de la operación, debiéndose verificarse los restantes requisitos
habituales. En caso de que la operación haya sido liquidada por más de una entidad,
cada una podrá certificar la aplicación de la porción no liquidada en proporción a su
participación en la porción liquidada.
En el caso de que la adquisición de títulos valores se haya concretado con liquidación
en el país de la moneda extranjera se deberá contar con la certificación de la entidad
que cursó la operación de canje y/o arbitraje por el ingreso de las divisas a través del
mercado de cambios.
```

## F56

- **Predicado:** `condicion_de`
- **Origen:** Condicion — «Destino fondos a financiación de proyectos de inversión» (`Condicion_destino_fondos_a_financiacion_de_proyectos_de_inversion__los_fondos_liquidados_d_b621a9`)
  - descripción (salida del extractor): Los fondos liquidados deben ser destinados a la financiación de proyectos de inversión en el país que generen
  - tramo de E1 en la unidad (salida del extractor): 'los fondos liquidados sean destinados a la financiación de proyectos de inversión en el país que generen'
- **Destino:** Operacion — «Elegibilidad operaciones 7.9.1.1 a 7.9.1.3» (`Operacion_elegibilidad_operaciones_7_9_1_1_a_7_9_1_3__ext_7_9_2_5b990b`)
  - descripción (salida del extractor): Las operaciones de los puntos 7.9.1.1. a 7.9.1.3. serán elegibles en la medida que los fondos liquidados sean destinados a la financiación de proyectos de inversión en el país que generen
  - tramo de E1 en la unidad (salida del extractor): 'Las operaciones de los puntos 7.9.1.1. a 7.9.1.3. serán elegibles'
- **Unidad:** `ext::7.9.2::intro` (ext, punto 7.9.2, bloque_intro)
- **Páginas:** unidad [97], arista [97]; PDF `data/experiment/subset/TO_exterior_cambios_actual.pdf`
- **Render:** `paginas/ext_p97.png`
- **Texto heredado:**
  - [encabezado, S7, p. [80]] Sección 7. Cobros de exportaciones de bienes.
  - [encabezado, 7.9, p. [94]] 7.9. Operaciones financieras habilitadas para aplicar cobros de exportaciones de bienes y
  - [encabezado, 7.9.2, p. [97]] 7.9.2. Las operaciones de los puntos 7.9.1.1. a 7.9.1.3. serán elegibles en la medida que los
- **Texto propio** («[bloque intro] Las operaciones de los puntos 7.9.1.1. a 7.9.1.3. serán elegibles en la medida que los»):

```text
fondos liquidados sean destinados a la financiación de proyectos de inversión en el
país que generen:
```

## F57

- **Predicado:** `condicion_de`
- **Origen:** Condicion — «Garantías preferidas — condición indiferente» (`Condicion_garantias_preferidas_condicion_indiferente__que_las_financiaciones_cuenten_o_no__1a9e1c`)
  - descripción (salida del extractor): Que las financiaciones cuenten o no con garantías preferidas (condición indiferente para el ejercicio de la opción)
  - tramo de E1 en la unidad (salida del extractor): 'cuenten o no con garantías preferidas'
- **Destino:** Potestad — «Opción de agrupar financiaciones comerciales» (`Potestad_opcion_de_agrupar_financiaciones_comerciales__facultad_de_agrupar_las_financiaci_20d56c`)
  - descripción (salida del extractor): Facultad de agrupar las financiaciones de naturaleza comercial de hasta el equivalente a dos veces el importe de referencia establecido en el punto 3.7., con o sin garantías preferidas, junto con los créditos para consumo o vivienda, en el manual de procedimientos de clasificación y previsión
  - tramo de E1 en la unidad (salida del extractor): 'El ejercicio de la opción de agrupar las financiaciones de naturaleza comercial de hasta el equivalente a dos veces el importe de referencia establecido en el punto 3.7., cuenten o no con garantías preferidas, junto con los créditos para consumo o vivienda'
- **Unidad:** `cla::3.3.3` (cla, punto 3.3.3, punto_propio)
- **Páginas:** unidad [9], arista [9]; PDF `data/experiment/subset/TO_clasificacion_deudores_actual.pdf`
- **Render:** `paginas/cla_p9.png`, `paginas/cla_p10.png`
- **Texto heredado:**
  - [encabezado, S3, p. [9]] Sección 3. Tarea de clasificación.
  - [encabezado, 3.3, p. [9]] 3.3. Manual de procedimientos de clasificación y previsión.
  - [intro, 3.3, p. [9]] Se volcarán en un “Manual de procedimientos de clasificación y previsión”:
  - [cierre, 3.3, p. [10]] El manual deberá estar a disposición permanente de la Superintendencia de Entidades Finan- cieras y Cambiarias.
- **Texto propio** («El ejercicio de la opción de agrupar las financiaciones de naturaleza comercial de hasta el»):

```text
3.3.3. El ejercicio de la opción de agrupar las financiaciones de naturaleza comercial de hasta el
equivalente a dos veces el importe de referencia establecido en el punto 3.7., cuenten o
no con garantías preferidas, junto con los créditos para consumo o vivienda.
```

## F58

- **Predicado:** `condicion_de`
- **Origen:** Condicion — «Condición — identificación de transacciones y protección de garantías» (`Condicion_condicion_identificacion_de_transacciones_y_proteccion_de_garantias__ccp_identif_4d09d5`)
  - descripción (salida del extractor): CCP identifica transacciones como transacciones de clientes y garantías son mantenidas bajo acuerdos que impiden pérdidas del cliente por: (i) falta de pago/insolvencia del miembro compensador; (ii) falta de pago/insolvencia de otros clientes del miembro; (iii) falta de pago/insolvencia conjuntas del miembro y cualquiera de sus otros clientes.
  - tramo de E1 en la unidad (salida del extractor): 'La CCP identifica a las transacciones a compensar como transacciones de clientes y las garantías que las amparan son mantenidas por la CCP y/o el miembro compensador, según sea el caso, bajo acuerdos que impiden que el cliente sufra pérdidas debido a: i. la falta de pago o la insolvencia del miembro compensador; ii. la falta de pago o la insolvencia de los demás clientes del miembro compensador; y iii. la falta de pago o la insolvencia conjuntas del miembro compensador y cualquiera de sus otros clientes.'
- **Destino:** Potestad — «Tratamiento exposición cliente — condiciones de protección cumplidas» (`Potestad_tratamiento_exposicion_cliente_condiciones_de_proteccion_cumplidas__exposicion_d_8fc89e`)
  - descripción (salida del extractor): Exposición de cliente hacia miembro compensador puede recibir tratamiento del acápite i) si se cumplen condiciones de protección especificadas.
  - tramo de E1 en la unidad (salida del extractor): 'la exposición de la entidad financiera hacia el miembro compensador podrá recibir el tratamiento del acápite i) precedente, siempre que se cumplan las siguientes condiciones:'
- **Unidad:** `cap::4.3.3.1` (cap, punto 4.3.3.1, punto_propio)
- **Páginas:** unidad [88, 89, 90, 91, 92], arista [88, 89, 90, 91, 92]; PDF `data/experiment/subset/TO_capitales_minimos_actual.pdf`
- **Render:** `paginas/cap_p85.png`, `paginas/cap_p86.png`, `paginas/cap_p88.png`, `paginas/cap_p89.png`, `paginas/cap_p90.png`, `paginas/cap_p91.png`, `paginas/cap_p92.png`
- **Texto heredado:**
  - [encabezado, S4, p. [63]] Sección 4. Capital mínimo por riesgo de crédito de contraparte.
  - [encabezado, 4.3, p. [85]] 4.3. Exigencia de capital por riesgo de crédito de contraparte en operaciones con entidades de
  - [intro, 4.3, p. [85, 86]] contraparte central. Comprende a aquellas exposiciones de las entidades financieras con entidades de contrapar- te central (CCP) que se originen en derivados OTC o negociados en mercados de valores y en operaciones de financiación con títulos valores (“Securities Financing Transactions”, SFT) y operaciones de liquidación diferida –definidas en el punto 4.2.–. No están comprendidas las exposiciones originadas en operaciones al contado y que involu- cren títulos valores, oro o moneda extranjera, cuya exigencia de capital se calculará conforme a lo previsto en el punto 4.1.
  - [encabezado, 4.3.3, p. [88]] 4.3.3. Exposiciones a entidades de contraparte central calificadas.
- **Texto propio** («Exposiciones por operaciones de negociación.»):

```text
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

## F59

- **Predicado:** `condicion_de`
- **Origen:** Condicion — «Verificación previa de requisitos para acceso al mercado» (`Condicion_verificacion_previa_de_requisitos_para_acceso_al_mercado__la_entidad_intervinien_340d50`)
  - descripción (salida del extractor): La entidad interviniente debe verificar previamente la totalidad de los requisitos que siguen para ejercer la facultad de dar acceso al mercado de cambios
  - tramo de E1 en la unidad (salida del extractor): 'en la medida que verifique previamente la totalidad de los siguientes requisitos'
- **Destino:** Potestad — «Facultad de dar acceso al mercado de cambios» (`Potestad_facultad_de_dar_acceso_al_mercado_de_cambios__la_entidad_interviniente_esta_facu_b82ae0`)
  - descripción (salida del extractor): La entidad interviniente está facultada para dar acceso al mercado de cambios para el pago al exterior de importaciones de bienes que cuentan con registro de ingreso aduanero que constan en el SEPAIMPO
  - tramo de E1 en la unidad (salida del extractor): 'La entidad interviniente podrá dar acceso al mercado de cambios para el pago al exterior de importaciones de bienes que cuentan con registro de ingreso aduanero que constan en el SEPAIMPO'
- **Unidad:** `ext::10.3.2::intro` (ext, punto 10.3.2, bloque_intro)
- **Páginas:** unidad [134], arista [134]; PDF `data/experiment/subset/TO_exterior_cambios_actual.pdf`
- **Render:** `paginas/ext_p134.png`
- **Texto heredado:**
  - [encabezado, S10, p. [130]] Sección 10. Pagos de importaciones y otras compras de bienes en el exterior.
  - [encabezado, 10.3, p. [133]] 10.3. Pagos de importaciones de bienes que cuentan con registro de ingreso aduanero.
  - [encabezado, 10.3.2, p. [134]] 10.3.2. Requisitos de acceso para el pago de oficializaciones de importación comprendidas
- **Texto propio** («[bloque intro] Requisitos de acceso para el pago de oficializaciones de importación comprendidas»):

```text
en el SEPAIMPO.
La entidad interviniente podrá dar acceso al mercado de cambios para el pago al
exterior de importaciones de bienes que cuentan con registro de ingreso aduanero
que constan en el SEPAIMPO, en la medida que verifique previamente la totalidad de
los siguientes requisitos:
```

## F60

- **Predicado:** `condicion_de`
- **Origen:** Condicion — «Calificación internacional mínima AA» (`Condicion_calificacion_internacional_minima_aa__las_entidades_en_las_que_se_colocan_certif_90e08f`)
  - descripción (salida del extractor): Las entidades en las que se colocan certificados de depósito a plazo fijo deben contar con calificación internacional no inferior a AA.
  - tramo de E1 en la unidad (salida del extractor): 'entidades que cuenten con calificación internacional no inferior a "AA"'
- **Destino:** Potestad — «Mantener certificados de depósito a plazo fijo en entidades calificadas» (`Potestad_mantener_certificados_de_deposito_a_plazo_fijo_en_entidades_calificadas__las_ent_1f6417`)
  - descripción (salida del extractor): Las entidades financieras quedan autorizadas a mantener certificados de depósito a plazo fijo en entidades que cuenten con calificación internacional no inferior a AA.
  - tramo de E1 en la unidad (salida del extractor): 'certificados de depósito a plazo fijo en entidades que cuenten con calificación internacional no inferior a "AA"'
- **Unidad:** `polcre::5.2` (polcre, punto 5.2, punto_propio)
- **Páginas:** unidad [13], arista [13]; PDF `data/experiment/escalado_prep/pdfs/polcre.pdf`
- **Render:** `paginas/polcre_p13.png`
- **Texto heredado:**
  - [encabezado, S5, p. [13]] Sección 5. Financiamiento a residentes en el exterior.
- **Texto propio** («Colocaciones en bancos del exterior.»):

```text
5.2. Colocaciones en bancos del exterior.
Las entidades financieras podrán mantener en bancos del exterior cuentas de corresponsalía y
cuentas a la vista necesarias para sus operaciones, de acuerdo con lo establecido en las nor-
mas sobre “Cuentas de corresponsalía” y certificados de depósito a plazo fijo en entidades que
cuenten con calificación internacional no inferior a “AA”.
```

