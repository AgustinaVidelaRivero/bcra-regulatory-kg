# Punto 6: listas que exceptúan, b1 y b2 (U-REEXT-T0, T4) — fichas para adjudicar

Sobre la extracción final. b1: Excepcion del miembro con la norma exceptuada (ítems) y Definicion de la clase (encabezado); b2: Condicion del supuesto con el cuantificador y la norma exceptuada (ítems) y la norma unida a su excepción (encabezado). `ctacte::3.2` va aparte, declarada. La marca es mi propuesta; adjudica la autora.

# Lista `cla::5.1.1` (b1)

## `cla::5.1.1::intro` (encabezado) — propuesta: **cumple**

> *heredado:* Sección 5. Categorías de carteras.
> *heredado:* 5.1. Categorías.
> *heredado:* 5.1.1. Cartera comercial.
> *propio:* Abarca todas las financiaciones comprendidas, con excepción de las siguientes:

- Estado final: `completo_ok_directo`; rechazos: 0
- **e1 Definicion** «Cartera comercial — alcance» — Abarca todas las financiaciones comprendidas, con excepción de las siguientes · props: `{"termino": "Cartera comercial"}` · tramo: «Abarca todas las financiaciones comprendidas, con excepción de las siguientes:»
- Omisión `fuera_de_tipos`: «con excepción de las siguientes:» — Anuncio de lista de excepciones cuyo contenido está en los ítems siguientes (no en esta unidad intro). La excepción se extrae en cada ítem del punto 5.1.1.

- **Lectura:** Definicion «Cartera comercial — alcance» (la clase)

## `cla::5.1.1.1` (ítem) — propuesta: **cumple**

> *heredado:* Sección 5. Categorías de carteras.
> *heredado:* 5.1. Categorías.
> *heredado:* La cartera se agrupará en dos categorías básicas:
> *heredado:* 5.1.1. Cartera comercial.
> *heredado:* Abarca todas las financiaciones comprendidas, con excepción de las siguientes:
> *propio:* 5.1.1.1. Los créditos para consumo o vivienda. Los créditos de esta clase que superen el equivalente a dos veces el importe de referencia establecido en el punto 3.7. y cuyo repago no se encuentre vinculado a ingresos fijos o periódicos del cliente sino a la evolución de su actividad productiva o comercial se incluirán dentro de la cartera comercial.

- Estado final: `aceptado_con_residuales`; rechazos: 1
- **e1 Operacion** «Inclusión en cartera comercial — créditos consumo/vivienda» — Inclusión de créditos para consumo o vivienda en la cartera comercial cuando superan dos veces el importe de referencia del punto 3.7 y su repago está vinculado a la evolución de la actividad productiva o comercial del cliente, no a ingresos fijos o periódicos. · props: `{"tipo": "Clasificación de créditos en cartera comercial"}` · tramo: «Los créditos de esta clase que superen el equivalente a dos veces el importe de referencia establecido en el punto 3.7. y cuyo repago no se encuentre vinculado a ingresos fijos o periódicos del cliente sino a la evolución de su actividad productiva o comercial se incluirán dentro de la cartera comercial.»
- **e2 Excepcion** «Excepción cartera comercial — créditos consumo/vivienda» — Los créditos para consumo o vivienda quedan exceptuados de la cartera comercial, salvo cuando reúnen las condiciones especificadas en el punto 5.1.1.1. · tramo: «Los créditos para consumo o vivienda.»
- **e3 Condicion** «Superar dos veces importe referencia punto 3.7» — El crédito debe superar el equivalente a dos veces el importe de referencia establecido en el punto 3.7. · umbral: ['superen el equivalente a dos veces el importe de referencia establecido en el punto 3.7'] · tramo: «superen el equivalente a dos veces el importe de referencia establecido en el punto 3.7»
- **e4 Condicion** «Repago vinculado a actividad productiva/comercial» — El repago del crédito no debe estar vinculado a ingresos fijos o periódicos del cliente, sino a la evolución de su actividad productiva o comercial. · tramo: «cuyo repago no se encuentre vinculado a ingresos fijos o periódicos del cliente sino a la evolución de su actividad productiva o comercial»
- R: e3 Condicion «Superar dos veces importe referencia punto 3.7» —condicion_de→ e1 Operacion «Inclusión en cartera comercial — créditos consumo/vivienda»
- R: e4 Condicion «Repago vinculado a actividad productiva/comercial» —condicion_de→ e1 Operacion «Inclusión en cartera comercial — créditos consumo/vivienda»
- Omisión `meta_normativo`: «Los créditos para consumo o vivienda.» — Encabezado de punto que anuncia la clase de créditos tratada; no prescribe conducta sino que nombra el tema. El contenido normativo está en el párrafo siguiente.

- **Lectura:** Excepcion «quedan exceptuados de la cartera comercial» (el miembro, con la norma); el exceptua fue rechazado por la firma, sin colgante

## `cla::5.1.1.2` (ítem) — propuesta: **no_cumple**

> *heredado:* Sección 5. Categorías de carteras.
> *heredado:* 5.1. Categorías.
> *heredado:* La cartera se agrupará en dos categorías básicas:
> *heredado:* 5.1.1. Cartera comercial.
> *heredado:* Abarca todas las financiaciones comprendidas, con excepción de las siguientes:
> *propio:* 5.1.1.2. A opción de la entidad, las financiaciones de naturaleza comercial de hasta el equivalente a dos veces el importe de referencia establecido en el punto 3.7., cuenten o no con garantías preferidas, podrán agruparse junto con los créditos para consumo o vivienda, en cuyo caso recibirán el tratamiento previsto para estos últimos. Cuando el cliente mantenga financiaciones por ambos conceptos, los créditos para consumo o vivienda se sumarán a los de la cartera comercial para determinar su encuadramiento en una o en otra cartera en función del importe indicado, a cuyo fin los créditos con garantías preferidas se ponderarán al 50 %. De ejercerse, esta opción deberá aplicarse con carácter general a toda la cartera y encontrarse prevista en el "Manual de procedimientos de clasificación y previsión" y sólo podrá cambiarse con un preaviso de 6 meses a la Superintendencia de Entidades Financieras y Cambiarias (SEFyC).

- Estado final: `aceptado_con_residuales`; rechazos: 0
- **e1 Operacion** «Agrupamiento de financiaciones comerciales con créditos de consumo o vivienda» — Agrupamiento de financiaciones comerciales de hasta dos veces el importe de referencia del punto 3.7. con créditos para consumo o vivienda, con o sin garantías preferidas, recibiendo el tratamiento de estos últimos · props: `{"tipo": "agrupamiento de cartera"}` · tramo: «las financiaciones de naturaleza comercial de hasta el equivalente a dos veces el importe de referencia establecido en el punto 3.7., cuenten o no con garantías preferidas, podrán agruparse junto con los créditos para consumo o vivienda»
- **e2 Potestad** «Opción de agrupar financiaciones comerciales con créditos de consumo o vivienda» — La entidad tiene la facultad de agrupar financiaciones comerciales de hasta dos veces el importe de referencia del punto 3.7. junto con créditos para consumo o vivienda · tramo: «A opción de la entidad, las financiaciones de naturaleza comercial de hasta el equivalente a dos veces el importe de referencia establecido en el punto 3.7., cuenten o no con garantías preferidas, podrán agruparse junto con los créditos para consumo o vivienda»
- **e3 Operacion** «Suma de créditos para consumo o vivienda a cartera comercial para encuadramiento» — Cuando el cliente mantiene financiaciones por ambos conceptos, los créditos para consumo o vivienda se suman a los de cartera comercial para determinar encuadramiento, ponderando créditos con garantías preferidas al 50% · props: `{"tipo": "cálculo de encuadramiento de cartera"}` · tramo: «los créditos para consumo o vivienda se sumarán a los de la cartera comercial para determinar su encuadramiento en una o en otra cartera en función del importe indicado, a cuyo fin los créditos con garantías preferidas se ponderarán al 50 %»
- **e4 Obligacion** «Aplicación general de la opción a toda la cartera» — Si la entidad ejerce la opción de agrupamiento, debe aplicarla con carácter general a toda la cartera · props: `{"tipo": "otra"}` · tramo: «De ejercerse, esta opción deberá aplicarse con carácter general a toda la cartera»
- **e5 Obligacion** «Previsión de la opción en Manual de procedimientos» — La opción debe encontrarse prevista en el Manual de procedimientos de clasificación y previsión · props: `{"tipo": "otra"}` · tramo: «encontrarse prevista en el "Manual de procedimientos de clasificación y previsión"»
- **e6 Obligacion** «Preaviso a SEFyC para cambio de opción» — Cualquier cambio en la aplicación de esta opción requiere preaviso de 6 meses a la SEFyC · props: `{"tipo": "comunicacion_a_cliente"}` · umbral: ['preaviso de 6 meses'] · tramo: «sólo podrá cambiarse con un preaviso de 6 meses a la Superintendencia de Entidades Financieras y Cambiarias (SEFyC)»
- **e7 Condicion** «Cliente con financiaciones por ambos conceptos» — Supuesto en que el cliente mantiene financiaciones de naturaleza comercial y créditos para consumo o vivienda simultáneamente · tramo: «Cuando el cliente mantenga financiaciones por ambos conceptos»
- R: e2 Potestad «Opción de agrupar financiaciones comerciales con créditos de consumo o vivienda» —aplica_a→ Sujeto_rol_obligado_a_clasificar_clasificacion (mención «la entidad», exacta)
- R: e4 Obligacion «Aplicación general de la opción a toda la cartera» —aplica_a→ Sujeto_rol_obligado_a_clasificar_clasificacion (mención «la entidad», exacta)
- R: e5 Obligacion «Previsión de la opción en Manual de procedimientos» —aplica_a→ Sujeto_rol_obligado_a_clasificar_clasificacion (mención «la entidad», exacta)
- R: e6 Obligacion «Preaviso a SEFyC para cambio de opción» —aplica_a→ Sujeto_rol_obligado_a_clasificar_clasificacion (mención «la entidad», exacta)
- R: e7 Condicion «Cliente con financiaciones por ambos conceptos» —condicion_de→ e3 Operacion «Suma de créditos para consumo o vivienda a cartera comercial para encuadramiento»
- Omisión `meta_normativo`: «en cuyo caso recibirán el tratamiento previsto para estos últimos» — Cláusula que describe el efecto de la operación (recibir tratamiento de créditos de consumo o vivienda), no una prescripción independiente

- **Lectura:** sin Excepcion: el miembro (financiaciones comerciales de hasta dos veces el importe) va como Operacion y Potestad de agrupar

# Lista `ext::3.5.4` (b2)

## `ext::3.5.4::intro` (encabezado) — propuesta: **cumple** (dudosa)

> *heredado:* Sección 3. Disposiciones específicas para los egresos por el mercado de cambios
> *heredado:* 3.5. Pagos de títulos de deuda suscriptos en el exterior y endeudamientos financieros con el
> *heredado:* 3.5.4. En la medida que se encuentre vigente el requisito de conformidad previa del BCRA
> *propio:* para el acceso al mercado de cambios para la cancelación al vencimiento de capital e intereses de los endeudamientos financieros comprendidos en este punto 3.5., este requisito no resultará aplicable cuando se cumpla la totalidad de las siguientes condiciones:

- Estado final: `aceptado_tras_reintento`; rechazos: 0
- **e1 Condicion** «Vigencia requisito conformidad previa BCRA» — Condición de vigencia del requisito de conformidad previa del BCRA para acceso al mercado de cambios en cancelación de endeudamientos financieros · tramo: «En la medida que se encuentre vigente el requisito de conformidad previa del BCRA»
- **e2 Excepcion** «Excepción requisito conformidad previa — endeudamientos financieros» — El requisito de conformidad previa del BCRA para acceso al mercado de cambios no resultará aplicable cuando se cumpla la totalidad de las condiciones que siguen, en relación con la cancelación al vencimiento de capital e intereses de endeudamientos financieros comprendidos en el punto 3.5. · tramo: «este requisito no resultará aplicable cuando se cumpla la totalidad de las siguientes condiciones»
- R: e1 Condicion «Vigencia requisito conformidad previa BCRA» —condicion_de→ e2 Excepcion «Excepción requisito conformidad previa — endeudamientos financieros»

- **Lectura:** la Excepcion «El requisito de conformidad previa del BCRA… no resultará aplicable cuando se cumpla la totalidad de las condiciones» lleva la norma y su excepción en una entidad, con la Condicion de vigencia

## `ext::3.5.4.1` (ítem) — propuesta: **no_cumple**

> *heredado:* Sección 3. Disposiciones específicas para los egresos por el mercado de cambios
> *heredado:* Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–, adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables.
> *heredado:* 3.5. Pagos de títulos de deuda suscriptos en el exterior y endeudamientos financieros con el
> *heredado:* exterior. Las entidades podrán dar acceso al mercado de cambios para realizar pagos de capital o intereses de títulos de deuda con registro público en el exterior, otros endeudamientos financieros con el exterior y títulos de deuda con registro público en el país denominados en moneda extranjera íntegramente suscriptos en el exterior, en la medida que se verifiquen las siguientes condiciones:
> *heredado:* 3.5.4. En la medida que se encuentre vigente el requisito de conformidad previa del BCRA
> *heredado:* para el acceso al mercado de cambios para la cancelación al vencimiento de capital e intereses de los endeudamientos financieros comprendidos en este punto 3.5., este requisito no resultará aplicable cuando se cumpla la totalidad de las siguientes condiciones:
> *propio:* 3.5.4.1. el destino de los fondos haya sido la financiación de proyectos enmarcados en el "Plan de promoción de la producción del gas natural argentino – Esquema de oferta y demanda 2020-2024" establecido en el artículo 2° del Decreto 892/20 ("PLAN GAS");

- Estado final: `completo_ok_directo`; rechazos: 1
- **e1 Condicion** «Destino fondos financiación Plan Gas» — Condición que suspende el requisito de conformidad previa del BCRA para acceso al mercado de cambios cuando los fondos de endeudamientos financieros se destinan a financiar proyectos enmarcados en el Plan Gas (Decreto 892/20) · tramo: «el destino de los fondos haya sido la financiación de proyectos enmarcados en el "Plan de promoción de la producción del gas natural argentino – Esquema de oferta y demanda 2020-2024" establecido en el artículo 2° del Decreto 892/20 ("PLAN GAS")»
- Omisión `relacion_sin_predicado`: «el destino de los fondos haya sido la financiación de proyectos enmarcados en el "Plan de promoción de la producción del gas natural argentino – Esquema de oferta y demanda 2020-2024" establecido en el artículo 2° del Decreto 892/20 ("PLAN GAS")» — La condición del punto 3.5.4.1 condiciona la Excepcion enunciada en el encabezado del punto 3.5.4 (suspensión del requisito de conformidad previa del BCRA para acceso al mercado de cambios), pero esa Excepcion no está extraída en esta unidad (está en la unidad del encabezado 3.5.4, que tiene su propia unidad de extracción). Por lo tanto, la Condicion no puede conectarse con condicion_de a una entidad que no está en el chunk. Predicado que se habría usado: condicion_de hacia la Excepcion del punto 3.5.4.

- **Lectura:** la Condicion nombra la norma exceptuada (suspende el requisito de conformidad previa) pero no el cuantificador («la totalidad»)

## `ext::3.5.4.2` (ítem) — propuesta: **no_cumple**

> *heredado:* Sección 3. Disposiciones específicas para los egresos por el mercado de cambios
> *heredado:* Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–, adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables.
> *heredado:* 3.5. Pagos de títulos de deuda suscriptos en el exterior y endeudamientos financieros con el
> *heredado:* exterior. Las entidades podrán dar acceso al mercado de cambios para realizar pagos de capital o intereses de títulos de deuda con registro público en el exterior, otros endeudamientos financieros con el exterior y títulos de deuda con registro público en el país denominados en moneda extranjera íntegramente suscriptos en el exterior, en la medida que se verifiquen las siguientes condiciones:
> *heredado:* 3.5.4. En la medida que se encuentre vigente el requisito de conformidad previa del BCRA
> *heredado:* para el acceso al mercado de cambios para la cancelación al vencimiento de capital e intereses de los endeudamientos financieros comprendidos en este punto 3.5., este requisito no resultará aplicable cuando se cumpla la totalidad de las siguientes condiciones:
> *propio:* 3.5.4.2. los fondos hayan sido ingresados y liquidados por el mercado de cambios a partir del 16/11/20; y

- Estado final: `aceptado_con_residuales`; rechazos: 0
- **c1 Condicion** «Fondos ingresados y liquidados desde 16/11/20» — Los fondos deben haber sido ingresados y liquidados por el mercado de cambios a partir del 16 de noviembre de 2020 · umbral: ['a partir del 16/11/20'] · tramo: «los fondos hayan sido ingresados y liquidados por el mercado de cambios a partir del 16/11/20»
- Omisión `relacion_sin_predicado`: «los fondos hayan sido ingresados y liquidados por el mercado de cambios a partir del 16/11/20» — Relación entre la Condicion (c1) y la norma principal que esta condición condiciona (la Excepcion del punto 3.5.4 que suspende el requisito de conformidad previa del BCRA). La norma principal no está en esta unidad sino en el encabezado del punto 3.5.4, que tiene su propia unidad de extracción. Por lo tanto, la Condicion se emite sin condicion_de.

- **Lectura:** la Condicion no nombra la norma exceptuada ni el cuantificador

## `ext::3.5.4.3` (ítem) — propuesta: **no_cumple**

> *heredado:* Sección 3. Disposiciones específicas para los egresos por el mercado de cambios
> *heredado:* Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–, adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables.
> *heredado:* 3.5. Pagos de títulos de deuda suscriptos en el exterior y endeudamientos financieros con el
> *heredado:* exterior. Las entidades podrán dar acceso al mercado de cambios para realizar pagos de capital o intereses de títulos de deuda con registro público en el exterior, otros endeudamientos financieros con el exterior y títulos de deuda con registro público en el país denominados en moneda extranjera íntegramente suscriptos en el exterior, en la medida que se verifiquen las siguientes condiciones:
> *heredado:* 3.5.4. En la medida que se encuentre vigente el requisito de conformidad previa del BCRA
> *heredado:* para el acceso al mercado de cambios para la cancelación al vencimiento de capital e intereses de los endeudamientos financieros comprendidos en este punto 3.5., este requisito no resultará aplicable cuando se cumpla la totalidad de las siguientes condiciones:
> *propio:* 3.5.4.3. el endeudamiento tenga una vida promedio no inferior a los 2 (dos) años.

- Estado final: `aceptado_tras_reintento`; rechazos: 0
- **c1 Condicion** «Vigencia requisito conformidad previa BCRA» — La condición de que el requisito de conformidad previa del BCRA para el acceso al mercado de cambios para la cancelación al vencimiento de capital e intereses de los endeudamientos financieros se encuentre vigente · tramo: «En la medida que se encuentre vigente el requisito de conformidad previa del BCRA»
- **e1 Excepcion** «Excepción conformidad previa — condiciones cumplidas» — El requisito de conformidad previa del BCRA no resultará aplicable cuando se cumplan todas las condiciones enumeradas en el punto 3.5.4 · tramo: «este requisito no resultará aplicable cuando se cumpla la totalidad de las siguientes condiciones»
- **c2 Condicion** «Vida promedio endeudamiento mínimo 2 años» — Que el endeudamiento tenga una vida promedio no inferior a los 2 (dos) años · umbral: ['no inferior a los 2 (dos) años'] · tramo: «el endeudamiento tenga una vida promedio no inferior a los 2 (dos) años»
- R: c1 Condicion «Vigencia requisito conformidad previa BCRA» —condicion_de→ e1 Excepcion «Excepción conformidad previa — condiciones cumplidas»
- R: c2 Condicion «Vida promedio endeudamiento mínimo 2 años» —condicion_de→ e1 Excepcion «Excepción conformidad previa — condiciones cumplidas»

- **Lectura:** la Condicion del supuesto no nombra la norma ni el cuantificador; trae una Excepcion compuesta en el ítem

# Lista `ext::2.6.1` (b2)

## `ext::2.6.1::intro` (encabezado) — propuesta: **cumple**

> *heredado:* Sección 2. Disposiciones específicas para los ingresos por el mercado de cambios.
> *heredado:* 2.6. Excepción de liquidación de cobros de exportaciones de bienes y servicios para los
> *heredado:* 2.6.1. Las personas jurídicas inscriptas en el Registro Nacional de Beneficiarios del Régimen
> *propio:* de Promoción de la Economía del Conocimiento y que sean beneficiarios de lo dispuesto en el Capítulo II del Decreto 679/22 quedarán exceptuados de la obligación de liquidación de los cobros de exportaciones de bienes y servicios que correspondan a actividades de la economía del conocimiento, en la medida que se cumpla la totalidad de las siguientes condiciones:

- Estado final: `completo_ok_directo`; rechazos: 0
- **e1 Excepcion** «Excepción liquidación cobros exportaciones economía conocimiento» — Las personas jurídicas inscriptas en el Registro Nacional de Beneficiarios del Régimen de Promoción de la Economía del Conocimiento y beneficiarios del Capítulo II del Decreto 679/22 quedan exceptuadas de la obligación de liquidación de cobros de exportaciones de bienes y servicios correspondientes a actividades de la economía del conocimiento. · tramo: «quedarán exceptuados de la obligación de liquidación de los cobros de exportaciones de bienes y servicios que correspondan a actividades de la economía del conocimiento»
- **c1 Condicion** «Cumplimiento totalidad condiciones siguientes» — La excepción se aplica cuando se cumpla la totalidad de las condiciones que siguen. · tramo: «en la medida que se cumpla la totalidad de las siguientes condiciones»
- R: c1 Condicion «Cumplimiento totalidad condiciones siguientes» —condicion_de→ e1 Excepcion «Excepción liquidación cobros exportaciones economía conocimiento»
- R: e1 Excepcion «Excepción liquidación cobros exportaciones economía conocimiento» —aplica_a→ Sujeto_beneficiario_economia_conocimiento (mención «Las personas jurídicas inscriptas en el Registro Nacional de Beneficiarios del Régimen de Promoción de la Economía del Conocimiento», no)
- Omisión `fuera_de_tipos`: «Decreto 679/22» — Referencia a norma externa; se registra como Comunicacion en el grafo pero no se extrae como entidad en este bloque introductorio que solo enuncia la excepción sin desarrollar su contenido normativo específico.

- **Lectura:** Excepcion «quedan exceptuadas de la obligación de liquidación…» (la norma con su excepción) y Condicion «la totalidad de las condiciones»

## `ext::2.6.1.1` (ítem) — propuesta: **no_cumple**

> *heredado:* Sección 2. Disposiciones específicas para los ingresos por el mercado de cambios.
> *heredado:* 2.6. Excepción de liquidación de cobros de exportaciones de bienes y servicios para los
> *heredado:* beneficiarios del "Régimen de fomento para las exportaciones de la economía del conocimiento".
> *heredado:* 2.6.1. Las personas jurídicas inscriptas en el Registro Nacional de Beneficiarios del Régimen
> *heredado:* de Promoción de la Economía del Conocimiento y que sean beneficiarios de lo dispuesto en el Capítulo II del Decreto 679/22 quedarán exceptuados de la obligación de liquidación de los cobros de exportaciones de bienes y servicios que correspondan a actividades de la economía del conocimiento, en la medida que se cumpla la totalidad de las siguientes condiciones:
> *heredado:* Los montos de las divisas a ser afectadas en el marco de lo dispuesto en el Capítulo II del Decreto 679/22 no pueden resultar alcanzadas por ningún otro tratamiento cambiario diferencial que no sea aquel previsto en dicho capítulo.
> *propio:* 2.6.1.1. hayan ingresado por el mercado de cambios en los plazos establecidos en cada caso;

- Estado final: `cola_humana`; rechazos: 1
- **c1 Condicion** «Ingreso por mercado de cambios en plazos establecidos» — Las divisas deben haber ingresado por el mercado de cambios dentro de los plazos que correspondan en cada caso · tramo: «hayan ingresado por el mercado de cambios en los plazos establecidos en cada caso»
- Omisión `relacion_sin_predicado`: «hayan ingresado por el mercado de cambios en los plazos establecidos en cada caso» — La condición se vincula a la excepción de liquidación enunciada en el encabezado (punto 2.6.1), que no está en esta unidad. Se extrae la Condicion sin condicion_de hacia esa excepción, conforme a las instrucciones para ítems de listas de supuestos.
- Faltante de E3 pendiente (otro, alta): «Los montos de las divisas a ser afectadas en el marco de lo dispuesto en el Capítulo II del Decreto 679/22 no pueden resultar alcanzadas por ningún otro tratamiento cambiario diferencial que no sea aquel previsto en dicho capítulo»

- **Lectura:** Condicion sin la norma exceptuada ni el cuantificador

## `ext::2.6.1.2` (ítem) — propuesta: **no_cumple**

> *heredado:* Sección 2. Disposiciones específicas para los ingresos por el mercado de cambios.
> *heredado:* 2.6. Excepción de liquidación de cobros de exportaciones de bienes y servicios para los
> *heredado:* beneficiarios del "Régimen de fomento para las exportaciones de la economía del conocimiento".
> *heredado:* 2.6.1. Las personas jurídicas inscriptas en el Registro Nacional de Beneficiarios del Régimen
> *heredado:* de Promoción de la Economía del Conocimiento y que sean beneficiarios de lo dispuesto en el Capítulo II del Decreto 679/22 quedarán exceptuados de la obligación de liquidación de los cobros de exportaciones de bienes y servicios que correspondan a actividades de la economía del conocimiento, en la medida que se cumpla la totalidad de las siguientes condiciones:
> *heredado:* Los montos de las divisas a ser afectadas en el marco de lo dispuesto en el Capítulo II del Decreto 679/22 no pueden resultar alcanzadas por ningún otro tratamiento cambiario diferencial que no sea aquel previsto en dicho capítulo.
> *propio:* 2.6.1.2. cuenten con una "Certificación de incremento de exportaciones asociadas a la economía del conocimiento (Decreto 679/22)" en los términos previstos en el punto 2.6.2.;

- Estado final: `aceptado_tras_reintento`; rechazos: 0
- **e1 Excepcion** «Excepción liquidación cobros exportaciones economía conocimiento» — Las personas jurídicas inscriptas en el Registro Nacional de Beneficiarios del Régimen de Promoción de la Economía del Conocimiento y que sean beneficiarios de lo dispuesto en el Capítulo II del Decreto 679/22 quedan exceptuadas de la obligación de liquidación de los cobros de exportaciones de bienes y servicios que correspondan a actividades de la economía del conocimiento. · tramo: «quedarán exceptuados de la obligación de liquidación de los cobros de exportaciones de bienes y servicios que correspondan a actividades de la economía del conocimiento»
- **c1 Condicion** «Condición: certificación incremento exportaciones economía conocimiento» — Contar con una Certificación de incremento de exportaciones asociadas a la economía del conocimiento (Decreto 679/22) en los términos previstos en el punto 2.6.2. · tramo: «cuenten con una "Certificación de incremento de exportaciones asociadas a la economía del conocimiento (Decreto 679/22)" en los términos previstos en el punto 2.6.2.»
- **c2 Condicion** «Condición: montos divisas no alcanzados por otro tratamiento cambiario» — Los montos de las divisas a ser afectadas en el marco de lo dispuesto en el Capítulo II del Decreto 679/22 no pueden resultar alcanzadas por ningún otro tratamiento cambiario diferencial que no sea aquel previsto en dicho capítulo. · tramo: «Los montos de las divisas a ser afectadas en el marco de lo dispuesto en el Capítulo II del Decreto 679/22 no pueden resultar alcanzadas por ningún otro tratamiento cambiario diferencial que no sea aquel previsto en dicho capítulo»
- **d1 Definicion** «Sujeto alcanzado: personas jurídicas inscriptas Registro Nacional Beneficiarios» — Las personas jurídicas inscriptas en el Registro Nacional de Beneficiarios del Régimen de Promoción de la Economía del Conocimiento y que sean beneficiarios de lo dispuesto en el Capítulo II del Decreto 679/22. · props: `{"termino": "beneficiarios de la excepción de liquidación de cobros de exportaciones"}` · tramo: «Las personas jurídicas inscriptas en el Registro Nacional de Beneficiarios del Régimen de Promoción de la Economía del Conocimiento y que sean beneficiarios de lo dispuesto en el Capítulo II del Decreto 679/22»
- R: c1 Condicion «Condición: certificación incremento exportaciones economía conocimiento» —condicion_de→ e1 Excepcion «Excepción liquidación cobros exportaciones economía conocimiento»
- R: c2 Condicion «Condición: montos divisas no alcanzados por otro tratamiento cambiario» —condicion_de→ e1 Excepcion «Excepción liquidación cobros exportaciones economía conocimiento»
- R: e1 Excepcion «Excepción liquidación cobros exportaciones economía conocimiento» —aplica_a→ Sujeto_beneficiario_economia_conocimiento (mención «Las personas jurídicas inscriptas en el Registro Nacional de Beneficiarios del Régimen de Promoción de la Economía del Conocimiento y que sean beneficiarios de lo dispuesto en el Capítulo II del Decreto 679/22», exacta)
- Omisión `meta_normativo`: «en la medida que se cumpla la totalidad de las siguientes condiciones» — Enunciado que introduce la enumeración de condiciones; el cuantificador (totalidad) se captura en la estructura de relaciones condicion_de múltiples hacia la misma excepción

- **Lectura:** Condicion sin norma ni cuantificador, hacia una Excepcion compuesta que repite la del encabezado

## `ext::2.6.1.3` (ítem) — propuesta: **no_cumple**

> *heredado:* Sección 2. Disposiciones específicas para los ingresos por el mercado de cambios.
> *heredado:* 2.6. Excepción de liquidación de cobros de exportaciones de bienes y servicios para los
> *heredado:* beneficiarios del "Régimen de fomento para las exportaciones de la economía del conocimiento".
> *heredado:* 2.6.1. Las personas jurídicas inscriptas en el Registro Nacional de Beneficiarios del Régimen
> *heredado:* de Promoción de la Economía del Conocimiento y que sean beneficiarios de lo dispuesto en el Capítulo II del Decreto 679/22 quedarán exceptuados de la obligación de liquidación de los cobros de exportaciones de bienes y servicios que correspondan a actividades de la economía del conocimiento, en la medida que se cumpla la totalidad de las siguientes condiciones:
> *heredado:* Los montos de las divisas a ser afectadas en el marco de lo dispuesto en el Capítulo II del Decreto 679/22 no pueden resultar alcanzadas por ningún otro tratamiento cambiario diferencial que no sea aquel previsto en dicho capítulo.
> *propio:* 2.6.1.3. se den cumplimiento a los restantes requisitos establecidos en los puntos 2.2.2.2. o 7.8.4., según corresponda.

- Estado final: `completo_ok_directo`; rechazos: 0
- **c1 Condicion** «Cumplimiento requisitos puntos 2.2.2.2 o 7.8.4» — Se debe dar cumplimiento a los restantes requisitos establecidos en los puntos 2.2.2.2 o 7.8.4, según corresponda, como condición para la excepción de liquidación de cobros de exportaciones de bienes y servicios para beneficiarios del Régimen de Promoción de la Economía del Conocimiento. · tramo: «se den cumplimiento a los restantes requisitos establecidos en los puntos 2.2.2.2. o 7.8.4., según corresponda»
- Omisión `relacion_sin_predicado`: «se den cumplimiento a los restantes requisitos establecidos en los puntos 2.2.2.2. o 7.8.4., según corresponda» — La condición se vincula a la excepción de liquidación enunciada en el encabezado (punto 2.6.1), pero esa norma no está en esta unidad (está en la unidad del encabezado). No se emite condicion_de porque el destino no está en el chunk.

- **Lectura:** la Condicion nombra la excepción de liquidación, pero no el cuantificador

# Lista `ext::7.8.4` (b2)

## `ext::7.8.4::intro` (encabezado) — propuesta: **cumple**

> *heredado:* Sección 7. Cobros de exportaciones de bienes.
> *heredado:* 7.8. Otras disposiciones.
> *heredado:* 7.8.4. Excepción de liquidación para cobros de exportaciones de bienes de beneficiarios del
> *propio:* régimen de fomento para las exportaciones de la economía del conocimiento. Quedarán exceptuados de la obligación de liquidación, en la medida que ingresen dentro de los plazos normativos establecidos, los cobros de exportaciones de bienes de personas jurídicas que sean beneficiarias del régimen de fomento para las exportaciones de la economía del conocimiento (Capítulo II del Decreto 679/22) y se cumplan la totalidad de las siguientes condiciones:

- Estado final: `completo_ok_directo`; rechazos: 0
- **e1 Excepcion** «Excepción liquidación — cobros exportaciones beneficiarios economía conocimiento» — Quedan exceptuados de la obligación de liquidación los cobros de exportaciones de bienes de personas jurídicas beneficiarias del régimen de fomento para las exportaciones de la economía del conocimiento, siempre que ingresen dentro de los plazos normativos establecidos. · umbral: ['dentro de los plazos normativos establecidos'] · tramo: «Quedarán exceptuados de la obligación de liquidación, en la medida que ingresen dentro de los plazos normativos establecidos, los cobros de exportaciones de bienes de personas jurídicas que sean beneficiarias del régimen de fomento para las exportaciones de la economía del conocimiento (Capítulo II del Decreto 679/22)»
- **e2 Condicion** «Cumplimiento totalidad condiciones — excepción liquidación» — Se deben cumplir la totalidad de las condiciones que siguen para que la excepción de liquidación sea aplicable. · tramo: «se cumplan la totalidad de las siguientes condiciones»
- R: e2 Condicion «Cumplimiento totalidad condiciones — excepción liquidación» —condicion_de→ e1 Excepcion «Excepción liquidación — cobros exportaciones beneficiarios economía conocimiento»
- Omisión `fuera_de_tipos`: «Capítulo II del Decreto 679/22» — Referencia normativa externa (decreto). No es una entidad Comunicacion porque no es citada como norma aplicable sino como fuente de definición del régimen; la definición del régimen va en la descripción de la Excepcion.

- **Lectura:** Excepcion de la obligación de liquidación y Condicion «la totalidad»

## `ext::7.8.4.1` (ítem) — propuesta: **no_cumple**

> *heredado:* Sección 7. Cobros de exportaciones de bienes.
> *heredado:* 7.8. Otras disposiciones.
> *heredado:* 7.8.4. Excepción de liquidación para cobros de exportaciones de bienes de beneficiarios del
> *heredado:* régimen de fomento para las exportaciones de la economía del conocimiento. Quedarán exceptuados de la obligación de liquidación, en la medida que ingresen dentro de los plazos normativos establecidos, los cobros de exportaciones de bienes de personas jurídicas que sean beneficiarias del régimen de fomento para las exportaciones de la economía del conocimiento (Capítulo II del Decreto 679/22) y se cumplan la totalidad de las siguientes condiciones:
> *heredado:* Los montos de las divisas a ser afectadas en el marco de lo dispuesto en el capítulo II del Decreto 679/22 no pueden resultar alcanzadas por ningún otro tratamiento cambiario diferencial que no sea aquel previsto en dicho capítulo. A los efectos del registro de estas operaciones se deberán confeccionar dos boletos sin movimiento de pesos, el boleto de compra se realizará por el concepto de cobros de exportaciones que corresponda y el boleto de venta deberá registrarse bajo el código de concepto "A22. Acreditación de cobros de exportaciones de bienes y servicios". La imputación del monto ingresado al cumplimiento del permiso de embarque requerirá que el exportador presente, ante la entidad encargada de su seguimiento, documentación que demuestre que se registraron por dicho monto transferencias en moneda extranjera desde la "Cuenta especial para el régimen de fomento de la economía del conocimiento. Decreto 679/22" por el pago de las remuneraciones de personal en relación de dependencia. Por otra parte, la entidad encargada del seguimiento del permiso de embarque podrá extender el plazo de liquidación del permiso cuando, por el monto que se encuentre pendiente de liquidación, el cliente haya utilizado este mecanismo y los fondos sigan depositados en "Cuenta especial para el régimen de fomento de la economía del conocimiento. Decreto 679/22" de titularidad del cliente.
> *propio:* 7.8.4.1. la entidad interviniente deberá contar con una declaración jurada del cliente en la que conste que los cobros que dejan de liquidarse corresponden a exportaciones de bienes que están relacionadas con actividades vinculadas a la economía del conocimiento.

- Estado final: `aceptado_con_residuales`; rechazos: 0
- **e1 Operacion** «Cobros de exportaciones de bienes — economía del conocimiento» — Cobros de exportaciones de bienes relacionadas con actividades vinculadas a la economía del conocimiento que dejan de liquidarse en el marco de la excepción para beneficiarios del régimen de fomento para las exportaciones de la economía del conocimiento. · props: `{"tipo": "cobro de exportación"}` · tramo: «los cobros que dejan de liquidarse corresponden a exportaciones de bienes que están relacionadas con actividades vinculadas a la economía del conocimiento»
- **e2 Obligacion** «Declaración jurada del cliente — cobros de exportaciones» — La entidad interviniente deberá contar con una declaración jurada del cliente en la que conste que los cobros que dejan de liquidarse corresponden a exportaciones de bienes que están relacionadas con actividades vinculadas a la economía del conocimiento. · props: `{"tipo": "presentacion_informativa"}` · tramo: «la entidad interviniente deberá contar con una declaración jurada del cliente en la que conste que los cobros que dejan de liquidarse corresponden a exportaciones de bienes que están relacionadas con actividades vinculadas a la economía del conocimiento»
- R: e2 Obligacion «Declaración jurada del cliente — cobros de exportaciones» —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad interviniente», exacta)
- R: e2 Obligacion «Declaración jurada del cliente — cobros de exportaciones» —regula→ e1 Operacion «Cobros de exportaciones de bienes — economía del conocimiento»

- **Lectura:** Operacion y Obligacion (declaración jurada); sin Condicion del supuesto

## `ext::7.8.4.2` (ítem) — propuesta: **no_cumple**

> *heredado:* Sección 7. Cobros de exportaciones de bienes.
> *heredado:* 7.8. Otras disposiciones.
> *heredado:* 7.8.4. Excepción de liquidación para cobros de exportaciones de bienes de beneficiarios del
> *heredado:* régimen de fomento para las exportaciones de la economía del conocimiento. Quedarán exceptuados de la obligación de liquidación, en la medida que ingresen dentro de los plazos normativos establecidos, los cobros de exportaciones de bienes de personas jurídicas que sean beneficiarias del régimen de fomento para las exportaciones de la economía del conocimiento (Capítulo II del Decreto 679/22) y se cumplan la totalidad de las siguientes condiciones:
> *heredado:* Los montos de las divisas a ser afectadas en el marco de lo dispuesto en el capítulo II del Decreto 679/22 no pueden resultar alcanzadas por ningún otro tratamiento cambiario diferencial que no sea aquel previsto en dicho capítulo. A los efectos del registro de estas operaciones se deberán confeccionar dos boletos sin movimiento de pesos, el boleto de compra se realizará por el concepto de cobros de exportaciones que corresponda y el boleto de venta deberá registrarse bajo el código de concepto "A22. Acreditación de cobros de exportaciones de bienes y servicios". La imputación del monto ingresado al cumplimiento del permiso de embarque requerirá que el exportador presente, ante la entidad encargada de su seguimiento, documentación que demuestre que se registraron por dicho monto transferencias en moneda extranjera desde la "Cuenta especial para el régimen de fomento de la economía del conocimiento. Decreto 679/22" por el pago de las remuneraciones de personal en relación de dependencia. Por otra parte, la entidad encargada del seguimiento del permiso de embarque podrá extender el plazo de liquidación del permiso cuando, por el monto que se encuentre pendiente de liquidación, el cliente haya utilizado este mecanismo y los fondos sigan depositados en "Cuenta especial para el régimen de fomento de la economía del conocimiento. Decreto 679/22" de titularidad del cliente.
> *propio:* 7.8.4.2. los fondos en moneda extranjera sean acreditados en una "Cuenta especial para el régimen de fomento de la economía del conocimiento. Decreto 679/22" de titularidad del cliente hasta que sean destinados al pago en moneda extranjera de las remuneraciones de personal en relación de dependencia, debidamente registrado, afectado a las actividades de la economía del conocimiento, conforme los criterios establecidos en el Decreto 679/22 y la Resolución 234/22 del Ministerio de Economía.

- Estado final: `aceptado_con_residuales`; rechazos: 0
- **e1 Operacion** «Acreditación fondos en cuenta especial» — Acreditación de fondos en moneda extranjera en una Cuenta especial para el régimen de fomento de la economía del conocimiento, de titularidad del cliente, hasta que sean destinados al pago en moneda extranjera de las remuneraciones de personal en relación de dependencia, debidamente registrado, afectado a las actividades de la economía del conocimiento, conforme los criterios establecidos en el Decreto 679/22 y la Resolución 234/22 del Ministerio de Economía. · props: `{"tipo": "acreditación de fondos en moneda extranjera"}` · tramo: «los fondos en moneda extranjera sean acreditados en una "Cuenta especial para el régimen de fomento de la economía del conocimiento. Decreto 679/22" de titularidad del cliente»
- **e2 Condicion** «Fondos destinados a pago de remuneraciones» — Los fondos deben ser destinados al pago en moneda extranjera de las remuneraciones de personal en relación de dependencia, debidamente registrado, afectado a las actividades de la economía del conocimiento, conforme los criterios establecidos en el Decreto 679/22 y la Resolución 234/22 del Ministerio de Economía. · tramo: «hasta que sean destinados al pago en moneda extranjera de las remuneraciones de personal en relación de dependencia, debidamente registrado, afectado a las actividades de la economía del conocimiento»
- **e3 Comunicacion** «Decreto 679/22» —  · props: `{"codigo": "Decreto 679/22", "tipo": "externa"}` · tramo: «Decreto 679/22»
- **e4 Comunicacion** «Resolución 234/22» —  · props: `{"codigo": "Resolución 234/22", "tipo": "externa"}` · tramo: «Resolución 234/22 del Ministerio de Economía»
- R: e2 Condicion «Fondos destinados a pago de remuneraciones» —condicion_de→ e1 Operacion «Acreditación fondos en cuenta especial»
- R: to TextoOrdenado «Texto Ordenado Exterior Cambios» —referencia→ e3 Comunicacion «Decreto 679/22»
- R: to TextoOrdenado «Texto Ordenado Exterior Cambios» —referencia→ e4 Comunicacion «Resolución 234/22»
- Omisión `meta_normativo`: «conforme los criterios establecidos en el Decreto 679/22 y la Resolución 234/22 del Ministerio de Economía» — Remisión a criterios externos que califican la operación; el contenido normativo está en las normas citadas, no en este punto.

- **Lectura:** Operacion y Condicion sin norma ni cuantificador

## `ext::7.8.4.3` (ítem) — propuesta: **no_cumple**

> *heredado:* Sección 7. Cobros de exportaciones de bienes.
> *heredado:* 7.8. Otras disposiciones.
> *heredado:* 7.8.4. Excepción de liquidación para cobros de exportaciones de bienes de beneficiarios del
> *heredado:* régimen de fomento para las exportaciones de la economía del conocimiento. Quedarán exceptuados de la obligación de liquidación, en la medida que ingresen dentro de los plazos normativos establecidos, los cobros de exportaciones de bienes de personas jurídicas que sean beneficiarias del régimen de fomento para las exportaciones de la economía del conocimiento (Capítulo II del Decreto 679/22) y se cumplan la totalidad de las siguientes condiciones:
> *heredado:* Los montos de las divisas a ser afectadas en el marco de lo dispuesto en el capítulo II del Decreto 679/22 no pueden resultar alcanzadas por ningún otro tratamiento cambiario diferencial que no sea aquel previsto en dicho capítulo. A los efectos del registro de estas operaciones se deberán confeccionar dos boletos sin movimiento de pesos, el boleto de compra se realizará por el concepto de cobros de exportaciones que corresponda y el boleto de venta deberá registrarse bajo el código de concepto "A22. Acreditación de cobros de exportaciones de bienes y servicios". La imputación del monto ingresado al cumplimiento del permiso de embarque requerirá que el exportador presente, ante la entidad encargada de su seguimiento, documentación que demuestre que se registraron por dicho monto transferencias en moneda extranjera desde la "Cuenta especial para el régimen de fomento de la economía del conocimiento. Decreto 679/22" por el pago de las remuneraciones de personal en relación de dependencia. Por otra parte, la entidad encargada del seguimiento del permiso de embarque podrá extender el plazo de liquidación del permiso cuando, por el monto que se encuentre pendiente de liquidación, el cliente haya utilizado este mecanismo y los fondos sigan depositados en "Cuenta especial para el régimen de fomento de la economía del conocimiento. Decreto 679/22" de titularidad del cliente.
> *propio:* 7.8.4.3. el cliente cuente por el equivalente del monto que se pretende no liquidar con una "Certificación de incremento de exportaciones asociadas a la economía del conocimiento (Decreto 679/22)" emitida en los términos previstos en el punto 2.6.2.

- Estado final: `aceptado_con_residuales`; rechazos: 1
- **e1 Condicion** «Cliente cuente con certificación de incremento de exportaciones» — El cliente debe contar con una Certificación de incremento de exportaciones asociadas a la economía del conocimiento (Decreto 679/22), emitida conforme a lo previsto en el punto 2.6.2, por el equivalente del monto que se pretende no liquidar. · tramo: «el cliente cuente por el equivalente del monto que se pretende no liquidar con una "Certificación de incremento de exportaciones asociadas a la economía del conocimiento (Decreto 679/22)" emitida en los términos previstos en el punto 2.6.2»
- Omisión `relacion_sin_predicado`: «emitida en los términos previstos en el punto 2.6.2» — referencia a otra norma (punto 2.6.2); la remisión la registra el código desde el texto, no se emite como relación entre entidades del chunk

- **Lectura:** Condicion sin norma ni cuantificador

# Lista `ext::2.7` (b2)

## `ext::2.7::intro` (encabezado) — propuesta: **cumple**

> *heredado:* Sección 2. Disposiciones específicas para los ingresos por el mercado de cambios.
> *heredado:* 2.7. Otras excepciones a la obligación de liquidación.
> *propio:* En adición a las excepciones enunciadas precedentemente, tampoco resultará exigible la liquidación en el mercado de cambios de los fondos en moneda extranjera que reciban los residentes por las operaciones previstas en los puntos 2.1. a 2.5., en la medida que se cumpla la totalidad de las siguientes condiciones:

- Estado final: `completo_ok_directo`; rechazos: 0
- **e1 Excepcion** «Excepción liquidación fondos moneda extranjera» — No será exigible la liquidación en el mercado de cambios de fondos en moneda extranjera recibidos por residentes de operaciones previstas en puntos 2.1 a 2.5, cuando se cumplan todas las condiciones siguientes · tramo: «tampoco resultará exigible la liquidación en el mercado de cambios de los fondos en moneda extranjera que reciban los residentes por las operaciones previstas en los puntos 2.1. a 2.5., en la medida que se cumpla la totalidad de las siguientes condiciones»
- **c1 Condicion** «Cumplimiento totalidad condiciones siguientes» — Se requiere el cumplimiento de la totalidad de las condiciones que se enuncian a continuación · tramo: «en la medida que se cumpla la totalidad de las siguientes condiciones»
- R: c1 Condicion «Cumplimiento totalidad condiciones siguientes» —condicion_de→ e1 Excepcion «Excepción liquidación fondos moneda extranjera»
- Omisión `meta_normativo`: «En adición a las excepciones enunciadas precedentemente» — Referencia a excepciones previas; no prescribe conducta nueva

- **Lectura:** Excepcion «No será exigible la liquidación… cuando se cumplan todas las condiciones» y Condicion «la totalidad»

## `ext::2.7.1` (ítem) — propuesta: **no_cumple**

> *heredado:* Sección 2. Disposiciones específicas para los ingresos por el mercado de cambios.
> *heredado:* 2.7. Otras excepciones a la obligación de liquidación.
> *heredado:* En adición a las excepciones enunciadas precedentemente, tampoco resultará exigible la liquidación en el mercado de cambios de los fondos en moneda extranjera que reciban los residentes por las operaciones previstas en los puntos 2.1. a 2.5., en la medida que se cumpla la totalidad de las siguientes condiciones:
> *heredado:* A los efectos del registro de estas operaciones se deberán confeccionar dos boletos sin movimiento de pesos, por los conceptos de compra y venta que correspondan, computándose el monto por el cual se utiliza este mecanismo a los efectos de los límites mensuales que pudieran ser aplicables según el caso. En todos los casos se deberá contar con una declaración jurada del cliente en la que deja constancia de tener conocimiento de que los fondos que se aplican bajo esta modalidad serán computados a los efectos del cálculo de los límites que normativamente correspondan al concepto de venta de cambio que corresponda y que no los excede.
> *propio:* 2.7.1. El ejercicio de la excepción se efectúe dentro del plazo para la liquidación de los fondos en el mercado de cambios que sea aplicable a la operación.

- Estado final: `completo_ok_directo`; rechazos: 1
- **e1 Condicion** «Ejercicio de excepción dentro del plazo de liquidación» — El ejercicio de la excepción a la obligación de liquidación debe efectuarse dentro del plazo para la liquidación de los fondos en el mercado de cambios que sea aplicable a la operación específica · umbral: ['dentro del plazo para la liquidación de los fondos en el mercado de cambios que sea aplicable a la operación'] · tramo: «El ejercicio de la excepción se efectúe dentro del plazo para la liquidación de los fondos en el mercado de cambios que sea aplicable a la operación»
- Omisión `relacion_sin_predicado`: «El ejercicio de la excepción se efectúe dentro del plazo para la liquidación de los fondos en el mercado de cambios que sea aplicable a la operación» — La condición se vincula a una excepción a la obligación de liquidación enunciada en el encabezado del punto 2.7, que no está en esta unidad. La relación condicion_de apunta a una entidad (e2) que no fue extraída en este chunk porque la excepción está en la unidad del encabezado heredado (punto 2.7). Se registra la omisión de la relación hacia esa excepción externa.

- **Lectura:** la Condicion nombra la excepción a la obligación de liquidación, pero no el cuantificador

## `ext::2.7.2` (ítem) — propuesta: **no_cumple**

> *heredado:* Sección 2. Disposiciones específicas para los ingresos por el mercado de cambios.
> *heredado:* 2.7. Otras excepciones a la obligación de liquidación.
> *heredado:* En adición a las excepciones enunciadas precedentemente, tampoco resultará exigible la liquidación en el mercado de cambios de los fondos en moneda extranjera que reciban los residentes por las operaciones previstas en los puntos 2.1. a 2.5., en la medida que se cumpla la totalidad de las siguientes condiciones:
> *heredado:* A los efectos del registro de estas operaciones se deberán confeccionar dos boletos sin movimiento de pesos, por los conceptos de compra y venta que correspondan, computándose el monto por el cual se utiliza este mecanismo a los efectos de los límites mensuales que pudieran ser aplicables según el caso. En todos los casos se deberá contar con una declaración jurada del cliente en la que deja constancia de tener conocimiento de que los fondos que se aplican bajo esta modalidad serán computados a los efectos del cálculo de los límites que normativamente correspondan al concepto de venta de cambio que corresponda y que no los excede.
> *propio:* 2.7.2. Los fondos hayan permanecido hasta el ejercicio de la excepción acreditados en cuentas en moneda extranjera de titularidad del cliente en entidades financieras locales o, en el caso de fondos percibidos en el exterior, ingresados a nombre del cliente en cuentas de corresponsalía de una entidad local.

- Estado final: `completo_ok_directo`; rechazos: 1
- **c1 Condicion** «Fondos permanecidos acreditados hasta ejercicio excepción» — Supuesto de que los fondos hayan permanecido acreditados en cuentas en moneda extranjera de titularidad del cliente en entidades financieras locales o, en el caso de fondos percibidos en el exterior, ingresados a nombre del cliente en cuentas de corresponsalía de una entidad local, hasta el ejercicio de la excepción a la obligación de liquidación en el mercado de cambios · tramo: «Los fondos hayan permanecido hasta el ejercicio de la excepción acreditados en cuentas en moneda extranjera de titularidad del cliente en entidades financieras locales o, en el caso de fondos percibidos en el exterior, ingresados a nombre del cliente en cuentas de corresponsalía de una entidad local»
- Omisión `relacion_sin_predicado`: «Los fondos hayan permanecido hasta el ejercicio de la excepción acreditados en cuentas en moneda extranjera de titularidad del cliente en entidades financieras locales o, en el caso de fondos percibidos en el exterior, ingresados a nombre del cliente en cuentas de corresponsalía de una entidad local» — La Condicion se vincula a la Excepcion del punto 2.7 (que no está en esta unidad), pero la relación condicion_de requiere que el destino esté en el chunk. La Excepcion está en la unidad del encabezado (punto 2.7), no en esta unidad (punto 2.7.2), por lo que no se emite la relación condicion_de hacia ella.

- **Lectura:** Condicion sin norma ni cuantificador

## `ext::2.7.3` (ítem) — propuesta: **no_cumple**

> *heredado:* Sección 2. Disposiciones específicas para los ingresos por el mercado de cambios.
> *heredado:* 2.7. Otras excepciones a la obligación de liquidación.
> *heredado:* En adición a las excepciones enunciadas precedentemente, tampoco resultará exigible la liquidación en el mercado de cambios de los fondos en moneda extranjera que reciban los residentes por las operaciones previstas en los puntos 2.1. a 2.5., en la medida que se cumpla la totalidad de las siguientes condiciones:
> *heredado:* A los efectos del registro de estas operaciones se deberán confeccionar dos boletos sin movimiento de pesos, por los conceptos de compra y venta que correspondan, computándose el monto por el cual se utiliza este mecanismo a los efectos de los límites mensuales que pudieran ser aplicables según el caso. En todos los casos se deberá contar con una declaración jurada del cliente en la que deja constancia de tener conocimiento de que los fondos que se aplican bajo esta modalidad serán computados a los efectos del cálculo de los límites que normativamente correspondan al concepto de venta de cambio que corresponda y que no los excede.
> *propio:* 2.7.3. Los fondos en moneda extranjera sean aplicados de manera simultánea con el ejercicio de la excepción a operaciones por las cuales la normativa cambiaria vigente permite el acceso al mercado de cambios contra moneda local, considerando los límites previstos para cada concepto involucrado.

- Estado final: `completo_ok_directo`; rechazos: 1
- **c1 Condicion** «Aplicación simultánea de fondos con ejercicio de excepción» — Los fondos en moneda extranjera deben ser aplicados de manera simultánea con el ejercicio de la excepción a operaciones por las cuales la normativa cambiaria vigente permite el acceso al mercado de cambios contra moneda local. · tramo: «Los fondos en moneda extranjera sean aplicados de manera simultánea con el ejercicio de la excepción a operaciones por las cuales la normativa cambiaria vigente permite el acceso al mercado de cambios contra moneda local»
- **c2 Condicion** «Respeto de límites previstos para cada concepto» — Deben considerarse los límites previstos para cada concepto involucrado en la operación. · tramo: «considerando los límites previstos para cada concepto involucrado»
- Omisión `relacion_sin_predicado`: «Los fondos en moneda extranjera sean aplicados de manera simultánea con el ejercicio de la excepción a operaciones por las cuales la normativa cambiaria vigente permite el acceso al mercado de cambios contra moneda local, considerando los límites previstos para cada concepto involucrado» — Relación entre las dos condiciones y la excepción a la obligación de liquidación enunciada en el punto 2.7 (contexto heredado). Las condiciones del punto 2.7.3 condicionan la excepción del punto 2.7, pero esa excepción no está extraída en esta unidad (está en la unidad del punto 2.7).

- **Lectura:** dos Condicion sin norma ni cuantificador

## `ext::2.7.4` (ítem) — propuesta: **no_cumple**

> *heredado:* Sección 2. Disposiciones específicas para los ingresos por el mercado de cambios.
> *heredado:* 2.7. Otras excepciones a la obligación de liquidación.
> *heredado:* En adición a las excepciones enunciadas precedentemente, tampoco resultará exigible la liquidación en el mercado de cambios de los fondos en moneda extranjera que reciban los residentes por las operaciones previstas en los puntos 2.1. a 2.5., en la medida que se cumpla la totalidad de las siguientes condiciones:
> *heredado:* A los efectos del registro de estas operaciones se deberán confeccionar dos boletos sin movimiento de pesos, por los conceptos de compra y venta que correspondan, computándose el monto por el cual se utiliza este mecanismo a los efectos de los límites mensuales que pudieran ser aplicables según el caso. En todos los casos se deberá contar con una declaración jurada del cliente en la que deja constancia de tener conocimiento de que los fondos que se aplican bajo esta modalidad serán computados a los efectos del cálculo de los límites que normativamente correspondan al concepto de venta de cambio que corresponda y que no los excede.
> *propio:* 2.7.4. La utilización de este mecanismo deberá resultar neutral en materia fiscal.

- Estado final: `completo_ok_directo`; rechazos: 0
- **e1 Obligacion** «Neutralidad fiscal — utilización de mecanismo» — La utilización de este mecanismo deberá resultar neutral en materia fiscal · props: `{"tipo": "otra"}` · tramo: «La utilización de este mecanismo deberá resultar neutral en materia fiscal»

- **Lectura:** Obligacion (neutralidad fiscal), sin Condicion del supuesto

# Lista `ctacte::3.2` (b1) — aparte, declarada

## `ctacte::3.2::intro` (encabezado) — propuesta: **no_cumple**

> *heredado:* Sección 3. Cheques.
> *heredado:* 3.2. Títulos que carecen de valor como cheques.
> *propio:* El título respecto del que se presentare alguna de las siguientes situaciones, enumeradas taxativamente a continuación, no valdrá como cheque:

- Estado final: `aceptado_con_residuales`; rechazos: 0
- **r1 Restriccion** «Título sin valor como cheque» — Un título que presente alguna de las situaciones enumeradas a continuación no tendrá valor como cheque. · props: `{"tipo": "prohibicion"}` · tramo: «El título respecto del que se presentare alguna de las siguientes situaciones, enumeradas taxativamente a continuación, no valdrá como cheque»
- Omisión `meta_normativo`: «enumeradas taxativamente a continuación» — Cláusula que predica sobre la forma de enumeración (carácter taxativo) de las situaciones que siguen, no sobre conducta regulada. El contenido normativo (qué situaciones hacen que el título no valga como cheque) está en los ítems del punto 3.2 que siguen a este bloque intro.

- **Lectura:** Restriccion «Título sin valor como cheque», no Definicion de la clase

## `ctacte::3.2.1::intro` (ítem) — propuesta: **no_cumple**

> *heredado:* Sección 3. Cheques.
> *heredado:* 3.2. Títulos que carecen de valor como cheques.
> *heredado:* 3.2.1. Falta de alguna de las especificaciones contenidas en los artículos 2°, incisos 1 a 6, 4°,
> *propio:* 23 y 54, incisos 1 a 9, de la Ley de Cheques, a saber:

- Estado final: `aceptado_tras_reintento`; rechazos: 0
- **e1 Restriccion** «Carencia de valor como cheque — falta de especificaciones» — Un título carece de valor como cheque cuando falta alguna de las especificaciones contenidas en los artículos 2° (incisos 1 a 6), 4°, 23 y 54 (incisos 1 a 9) de la Ley de Cheques. · props: `{"tipo": "prohibicion"}` · tramo: «Falta de alguna de las especificaciones contenidas en los artículos 2°, incisos 1 a 6, 4°, 23 y 54, incisos 1 a 9, de la Ley de Cheques»

- **Lectura:** Restriccion, no Excepcion

## `ctacte::3.2.2` (ítem) — propuesta: **no_cumple**

> *heredado:* Sección 3. Cheques.
> *heredado:* 3.2. Títulos que carecen de valor como cheques.
> *heredado:* El título respecto del que se presentare alguna de las siguientes situaciones, enumeradas taxativamente a continuación, no valdrá como cheque:
> *heredado:* Los títulos devueltos por esas situaciones no podrán ser objeto de nuevas presentaciones.
> *propio:* 3.2.2. Existencia de tachaduras o enmiendas no salvadas por el librador.

- Estado final: `completo_ok_directo`; rechazos: 2
- **e1 Restriccion** «Prohibición — cheques con tachaduras o enmiendas no salvadas» — El cheque que presente tachaduras o enmiendas no salvadas por el librador no valdrá como cheque. · props: `{"tipo": "prohibicion"}` · tramo: «El título respecto del que se presentare alguna de las siguientes situaciones, enumeradas taxativamente a continuación, no valdrá como cheque: […] Existencia de tachaduras o enmiendas no salvadas por el librador.»
- **e2 Restriccion** «Prohibición — nueva presentación de títulos devueltos» — Los títulos devueltos por falta de valor como cheque (incluyendo los con tachaduras o enmiendas no salvadas) no podrán ser objeto de nuevas presentaciones. · props: `{"tipo": "prohibicion"}` · tramo: «Los títulos devueltos por esas situaciones no podrán ser objeto de nuevas presentaciones.»
- Omisión `fuera_de_tipos`: «Existencia de tachaduras o enmiendas no salvadas por el librador.» — El punto es un título que enuncia una situación (un defecto del cheque), no una norma prescriptiva. El contenido normativo está en el encabezado del punto 3.2 ('no valdrá como cheque') y en el cierre ('no podrán ser objeto de nuevas presentaciones'). El título del punto 3.2.2 es descriptivo de la situación que activa la prohibición, no una prescripción independiente.

- **Lectura:** dos Restriccion, no Excepcion

## `ctacte::3.2.3` (ítem) — propuesta: **no_cumple**

> *heredado:* Sección 3. Cheques.
> *heredado:* 3.2. Títulos que carecen de valor como cheques.
> *heredado:* El título respecto del que se presentare alguna de las siguientes situaciones, enumeradas taxativamente a continuación, no valdrá como cheque:
> *heredado:* Los títulos devueltos por esas situaciones no podrán ser objeto de nuevas presentaciones.
> *propio:* 3.2.3. Que no estén redactados en idioma nacional.

- Estado final: `aceptado_con_residuales`; rechazos: 0
- **e1 Restriccion** «Prohibición cheques no redactados en idioma nacional» — Los cheques no redactados en idioma nacional no valen como cheques · props: `{"tipo": "prohibicion"}` · tramo: «Que no estén redactados en idioma nacional»
- **e2 Operacion** «Presentación de cheques» — La presentación de cheques para su procesamiento · props: `{"tipo": "presentación de cheques"}` · tramo: «títulos»
- R: e1 Restriccion «Prohibición cheques no redactados en idioma nacional» —prohibe→ e2 Operacion «Presentación de cheques» [coherente]
- Omisión `meta_normativo`: «no valdrá como cheque» — Cláusula interpretativa que declara el efecto jurídico de la situación enumerada, no una prescripción de conducta independiente

- **Lectura:** Restriccion y Operacion con prohibe, no Excepcion

## `ctacte::3.2.4` (ítem) — propuesta: **no_cumple**

> *heredado:* Sección 3. Cheques.
> *heredado:* 3.2. Títulos que carecen de valor como cheques.
> *heredado:* El título respecto del que se presentare alguna de las siguientes situaciones, enumeradas taxativamente a continuación, no valdrá como cheque:
> *heredado:* Los títulos devueltos por esas situaciones no podrán ser objeto de nuevas presentaciones.
> *propio:* 3.2.4. Que contengan inscripciones de propaganda.

- Estado final: `aceptado_con_residuales`; rechazos: 0
- **e1 Restriccion** «Prohibición cheques con inscripciones de propaganda» — Los cheques no podrán contener inscripciones de propaganda · props: `{"tipo": "prohibicion"}` · tramo: «Que contengan inscripciones de propaganda»
- **e2 Operacion** «Presentación de cheques» — Presentación de un cheque para su compensación o cobro · props: `{"tipo": "presentación de cheques"}` · tramo: «Los títulos devueltos por esas situaciones no podrán ser objeto de nuevas presentaciones»
- R: e1 Restriccion «Prohibición cheques con inscripciones de propaganda» —prohibe→ e2 Operacion «Presentación de cheques» [coherente]
- Omisión `meta_normativo`: «no valdrá como cheque» — Cláusula interpretativa que declara el efecto jurídico de la situación enumerada, no una conducta prescrita

- **Lectura:** Restriccion y Operacion con prohibe, no Excepcion

## `ctacte::3.2.5` (ítem) — propuesta: **no_cumple**

> *heredado:* Sección 3. Cheques.
> *heredado:* 3.2. Títulos que carecen de valor como cheques.
> *heredado:* El título respecto del que se presentare alguna de las siguientes situaciones, enumeradas taxativamente a continuación, no valdrá como cheque:
> *heredado:* Los títulos devueltos por esas situaciones no podrán ser objeto de nuevas presentaciones.
> *propio:* 3.2.5. Fecha de vencimiento de un cheque de pago diferido –no registrado– anterior o igual a la fecha de libramiento.

- Estado final: `completo_ok_directo`; rechazos: 0
- **e1 Operacion** «Cheque de pago diferido no registrado» — Cheque de pago diferido que no ha sido registrado · props: `{"tipo": "Cheque de pago diferido"}` · tramo: «cheque de pago diferido –no registrado–»
- **e2 Restriccion** «Fecha de vencimiento anterior o igual a libramiento» — El cheque de pago diferido no registrado no valdrá como cheque cuando su fecha de vencimiento sea anterior o igual a la fecha de libramiento · props: `{"tipo": "limite_cualitativo"}` · tramo: «Fecha de vencimiento de un cheque de pago diferido –no registrado– anterior o igual a la fecha de libramiento»
- R: e2 Restriccion «Fecha de vencimiento anterior o igual a libramiento» —limita→ e1 Operacion «Cheque de pago diferido no registrado» [coherente]
- R: e2 Restriccion «Fecha de vencimiento anterior o igual a libramiento» —aplica_a→ Sujeto_banco (mención «Los títulos», exacta)
- Omisión `meta_normativo`: «no valdrá como cheque» — Cláusula interpretativa que declara el efecto jurídico de la situación descrita (que el título pierde su carácter de cheque), no una prescripción de conducta. El contenido normativo (la prohibición de que el título valga como cheque) está implícito en la enumeración taxativa del punto 3.2 que declara qué títulos no valen como cheques.

- **Lectura:** Operacion y Restriccion, no Excepcion

# Lista `ext::3.5.3` (b2)

## `ext::3.5.3::intro` (encabezado) — propuesta: **no_cumple**

> *heredado:* Sección 3. Disposiciones específicas para los egresos por el mercado de cambios
> *heredado:* 3.5. Pagos de títulos de deuda suscriptos en el exterior y endeudamientos financieros con el
> *heredado:* 3.5.3. El acceso al mercado de cambios se produce con una anterioridad no mayor a los 3
> *propio:* (tres) días hábiles a la fecha de vencimiento del servicio de capital o interés a pagar. En el caso de que se trate de un pago de capital de títulos de deuda emitidos a partir del 08/11/24 que se concreta con una transferencia al exterior, el acceso al mercado de cambios deberá adicionalmente producirse una vez transcurridos, como mínimo, desde la fecha de emisión: i) 12 (doce) meses si el título fue emitido entre el 08/11/24 y el 20/04/25. ii) 6 (seis) meses si el título fue emitido entre 21/04/25 y el 15/05/25. iii) 18 (dieciocho) meses si el título fue emitido a partir del 16/05/25. El acceso al mercado de cambios antes de lo indicado requerirá la conformidad previa del BCRA excepto que el deudor encuadre en alguna de las siguientes situaciones y se cumplan la totalidad de las condiciones estipuladas en cada caso:

- Estado final: `aceptado_con_residuales`; rechazos: 0
- **c1 Condicion** «Acceso al mercado — anterioridad máxima 3 días» — El acceso al mercado de cambios debe producirse con una anterioridad no mayor a 3 días hábiles antes de la fecha de vencimiento del servicio de capital o interés a pagar. · umbral: ['no mayor a los 3 (tres) días hábiles'] · tramo: «El acceso al mercado de cambios se produce con una anterioridad no mayor a los 3 (tres) días hábiles a la fecha de vencimiento del servicio de capital o interés a pagar»
- **c2 Condicion** «Pago de capital — títulos emitidos 08/11/24 a 20/04/25 — 12 meses mínimo» — Para pagos de capital de títulos de deuda emitidos entre el 08/11/24 y el 20/04/25 que se concretan con transferencia al exterior, el acceso al mercado de cambios debe producirse una vez transcurridos, como mínimo, 12 meses desde la fecha de emisión. · umbral: ['12 (doce) meses'] · tramo: «si el título fue emitido entre el 08/11/24 y el 20/04/25»
- **c3 Condicion** «Pago de capital — títulos emitidos 21/04/25 a 15/05/25 — 6 meses mínimo» — Para pagos de capital de títulos de deuda emitidos entre el 21/04/25 y el 15/05/25 que se concretan con transferencia al exterior, el acceso al mercado de cambios debe producirse una vez transcurridos, como mínimo, 6 meses desde la fecha de emisión. · umbral: ['6 (seis) meses'] · tramo: «si el título fue emitido entre 21/04/25 y el 15/05/25»
- **c4 Condicion** «Pago de capital — títulos emitidos a partir 16/05/25 — 18 meses mínimo» — Para pagos de capital de títulos de deuda emitidos a partir del 16/05/25 que se concretan con transferencia al exterior, el acceso al mercado de cambios debe producirse una vez transcurridos, como mínimo, 18 meses desde la fecha de emisión. · umbral: ['18 (dieciocho) meses'] · tramo: «si el título fue emitido a partir del 16/05/25»
- **p1 Potestad** «Autorización previa del BCRA — acceso anticipado al mercado» — El BCRA puede otorgar conformidad previa para que el acceso al mercado de cambios se produzca antes de los plazos indicados. · tramo: «El acceso al mercado de cambios antes de lo indicado requerirá la conformidad previa del BCRA»
- **e1 Excepcion** «Excepción — conformidad previa del BCRA — situaciones especiales» — No se requiere conformidad previa del BCRA si el deudor encuadra en alguna de las situaciones especiales que siguen y se cumplen todas las condiciones estipuladas en cada caso. · tramo: «excepto que el deudor encuadre en alguna de las siguientes situaciones y se cumplan la totalidad de las condiciones estipuladas en cada caso»
- Omisión `relacion_sin_predicado`: «El acceso al mercado de cambios antes de lo indicado requerirá la conformidad previa del BCRA excepto que el deudor encuadre en alguna de las siguientes situaciones» — Relación entre Potestad (p1) y Excepcion (e1): la excepción suspende la exigencia de conformidad previa. Predicado sugerido: 'exceptua_potestad' (no existe en el schema; el schema solo tiene exceptua y exceptua_obligacion).

- **Lectura:** la norma (Potestad del BCRA) y la Excepcion, sin relación (relacion_sin_predicado)

## `ext::3.5.3.1` (ítem) — propuesta: **no_cumple**

> *heredado:* Sección 3. Disposiciones específicas para los egresos por el mercado de cambios
> *heredado:* Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–, adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables.
> *heredado:* 3.5. Pagos de títulos de deuda suscriptos en el exterior y endeudamientos financieros con el
> *heredado:* exterior. Las entidades podrán dar acceso al mercado de cambios para realizar pagos de capital o intereses de títulos de deuda con registro público en el exterior, otros endeudamientos financieros con el exterior y títulos de deuda con registro público en el país denominados en moneda extranjera íntegramente suscriptos en el exterior, en la medida que se verifiquen las siguientes condiciones:
> *heredado:* 3.5.3. El acceso al mercado de cambios se produce con una anterioridad no mayor a los 3
> *heredado:* (tres) días hábiles a la fecha de vencimiento del servicio de capital o interés a pagar. En el caso de que se trate de un pago de capital de títulos de deuda emitidos a partir del 08/11/24 que se concreta con una transferencia al exterior, el acceso al mercado de cambios deberá adicionalmente producirse una vez transcurridos, como mínimo, desde la fecha de emisión:
> *heredado:* i) 12 (doce) meses si el título fue emitido entre el 08/11/24 y el 20/04/25. ii) 6 (seis) meses si el título fue emitido entre 21/04/25 y el 15/05/25. iii) 18 (dieciocho) meses si el título fue emitido a partir del 16/05/25.
> *heredado:* El acceso al mercado de cambios antes de lo indicado requerirá la conformidad previa del BCRA excepto que el deudor encuadre en alguna de las siguientes situaciones y se cumplan la totalidad de las condiciones estipuladas en cada caso:
> *propio:* 3.5.3.1. Precancelación de capital e intereses con la liquidación de fondos ingresados desde el exterior por la emisión de un nuevo título de deuda comprendido en este punto 3.5. i) la precancelación de capital sea efectuada en manera simultánea con la liquidación de los fondos ingresados desde el exterior por la emisión de un nuevo título de deuda comprendido en este punto 3.5. emitido en el marco de una operación de refinanciación, recompra y/o rescate anticipado de deuda. a) el nuevo título de deuda contempla 1 (un) año de gracia para el pago de capital y su vida promedio es al menos 2 (dos) años mayor a la vida promedio remanente de la deuda que se precancela; y b) el monto acumulado de los vencimientos de capital del nuevo endeudamiento en ningún momento podrá superar, hasta la fecha de vencimiento de la deuda que se cancela, el monto que hubieran acumulado los vencimientos de capital de la deuda que se cancela. ii) la precancelación de intereses corresponde a los intereses devengados por la deuda refinanciada hasta la fecha de cierre de la operación de recompra y/o rescate, sin necesidad de que exista una liquidación de fondos por el monto equivalente; Adicionalmente, la entidad podrá darle acceso al mercado de cambios al cliente para: iii) pagar en concepto de prima de recompra, de rescate anticipado o similar hasta el equivalente del 5% (cinco por ciento) del monto del capital de la deuda recomprada y/o rescatada, en la medida que el pago se concrete de manera simultánea con una liquidación de fondos ingresados desde el exterior por el nuevo título de deuda que exceda al monto de capital que se precancela, como mínimo, por un monto equivalente al monto de la prima abonada. iv)pagar a la fecha de cierre de la operación de recompra y/o rescate, sin necesidad de que exista una liquidación de fondos por el monto equivalente, los gastos de emisión u otros servicios prestados por no residentes en el marco de la emisión de los nuevos títulos de deuda emitidos y/o la operación de recompra y/o rescate.

- Estado final: `aceptado_con_residuales`; rechazos: 0
- **e1 Operacion** «Precancelación de capital con liquidación de fondos» — Precancelación de capital efectuada de manera simultánea con la liquidación de fondos ingresados desde el exterior por la emisión de un nuevo título de deuda en operación de refinanciación, recompra y/o rescate anticipado de deuda. · props: `{"tipo": "Precancelación de capital"}` · tramo: «la precancelación de capital sea efectuada en manera simultánea con la liquidación de los fondos ingresados desde el exterior por la emisión de un nuevo título de deuda comprendido en este punto 3.5. emitido en el marco de una operación de refinanciación, recompra y/o rescate anticipado de deuda.»
- **e2 Condicion** «Nuevo título con 1 año de gracia y vida promedio mayor» — El nuevo título de deuda debe contemplar 1 año de gracia para el pago de capital y su vida promedio debe ser al menos 2 años mayor a la vida promedio remanente de la deuda que se precancela. · umbral: ['1 (un) año de gracia', 'al menos 2 (dos) años mayor'] · tramo: «el nuevo título de deuda contempla 1 (un) año de gracia para el pago de capital y su vida promedio es al menos 2 (dos) años mayor a la vida promedio remanente de la deuda que se precancela»
- **e3 Restriccion** «Límite monto acumulado vencimientos capital nuevo endeudamiento» — El monto acumulado de los vencimientos de capital del nuevo endeudamiento no podrá superar, hasta la fecha de vencimiento de la deuda que se cancela, el monto que hubieran acumulado los vencimientos de capital de la deuda que se cancela. · props: `{"tipo": "limite_cualitativo"}` · tramo: «el monto acumulado de los vencimientos de capital del nuevo endeudamiento en ningún momento podrá superar, hasta la fecha de vencimiento de la deuda que se cancela, el monto que hubieran acumulado los vencimientos de capital de la deuda que se cancela»
- **e4 Operacion** «Precancelación de intereses devengados» — Precancelación de intereses devengados por la deuda refinanciada hasta la fecha de cierre de la operación de recompra y/o rescate, sin necesidad de liquidación de fondos por el monto equivalente. · props: `{"tipo": "Precancelación de intereses"}` · tramo: «la precancelación de intereses corresponde a los intereses devengados por la deuda refinanciada hasta la fecha de cierre de la operación de recompra y/o rescate, sin necesidad de que exista una liquidación de fondos por el monto equivalente»
- **e5 Potestad** «Acceso mercado cambios para pago prima recompra/rescate» — La entidad podrá dar acceso al mercado de cambios al cliente para pagar prima de recompra, rescate anticipado o similar hasta el 5% del monto del capital de la deuda recomprada y/o rescatada, siempre que el pago se concrete de manera simultánea con una liquidación de fondos ingresados desde el exterior por el nuevo título de deuda que exceda al monto de capital que se precancela, como mínimo, por un monto equivalente al monto de la prima abonada. · tramo: «la entidad podrá darle acceso al mercado de cambios al cliente para pagar en concepto de prima de recompra, de rescate anticipado o similar hasta el equivalente del 5% (cinco por ciento) del monto del capital de la deuda recomprada y/o rescatada, en la medida que el pago se concrete de manera simultánea con una liquidación de fondos ingresados desde el exterior por el nuevo título de deuda que exceda al monto de capital que se precancela, como mínimo, por un monto equivalente al monto de la prima abonada»
- **e6 Condicion** «Pago simultáneo con liquidación de fondos que exceda capital precancelado» — El pago debe concretarse de manera simultánea con una liquidación de fondos ingresados desde el exterior por el nuevo título de deuda que exceda al monto de capital que se precancela, como mínimo, por un monto equivalente al monto de la prima abonada. · tramo: «el pago se concrete de manera simultánea con una liquidación de fondos ingresados desde el exterior por el nuevo título de deuda que exceda al monto de capital que se precancela, como mínimo, por un monto equivalente al monto de la prima abonada»
- **e7 Potestad** «Acceso mercado cambios para pago gastos emisión y servicios» — La entidad podrá dar acceso al mercado de cambios al cliente para pagar, a la fecha de cierre de la operación de recompra y/o rescate, sin necesidad de liquidación de fondos por el monto equivalente, los gastos de emisión u otros servicios prestados por no residentes en el marco de la emisión de los nuevos títulos de deuda emitidos y/o la operación de recompra y/o rescate. · tramo: «la entidad podrá darle acceso al mercado de cambios al cliente para pagar a la fecha de cierre de la operación de recompra y/o rescate, sin necesidad de que exista una liquidación de fondos por el monto equivalente, los gastos de emisión u otros servicios prestados por no residentes en el marco de la emisión de los nuevos títulos de deuda emitidos y/o la operación de recompra y/o rescate»
- **e8 Obligacion** «Cumplimiento de requisitos complementarios punto 3.16» — Las entidades deberán cumplimentar los requisitos complementarios que constan en el punto 3.16 que resulten aplicables, previamente a dar acceso al mercado de cambios para las operaciones comprendidas en los puntos 3.1 a 3.15, incluyendo aquellas que se concreten a través de canjes o arbitrajes. · props: `{"tipo": "otra"}` · tramo: «Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–, adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables.»
- R: e2 Condicion «Nuevo título con 1 año de gracia y vida promedio mayor» —condicion_de→ e1 Operacion «Precancelación de capital con liquidación de fondos»
- R: e3 Restriccion «Límite monto acumulado vencimientos capital nuevo endeudamiento» —limita→ e1 Operacion «Precancelación de capital con liquidación de fondos» [coherente]
- R: e6 Condicion «Pago simultáneo con liquidación de fondos que exceda capital precancelado» —condicion_de→ e5 Potestad «Acceso mercado cambios para pago prima recompra/rescate»
- R: e8 Obligacion «Cumplimiento de requisitos complementarios punto 3.16» —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «Las entidades», exacta)
- Omisión `meta_normativo`: «Adicionalmente, la entidad podrá darle acceso al mercado de cambios al cliente para:» — Enunciado introductorio que anuncia las facultades siguientes (ítems iii y iv); no prescribe conducta por sí solo.

- **Lectura:** Condicion hacia la Operacion, sin la norma exceptuada ni el cuantificador

## `ext::3.5.3.2` (ítem) — propuesta: **no_cumple**

> *heredado:* Sección 3. Disposiciones específicas para los egresos por el mercado de cambios
> *heredado:* Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–, adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables.
> *heredado:* 3.5. Pagos de títulos de deuda suscriptos en el exterior y endeudamientos financieros con el
> *heredado:* exterior. Las entidades podrán dar acceso al mercado de cambios para realizar pagos de capital o intereses de títulos de deuda con registro público en el exterior, otros endeudamientos financieros con el exterior y títulos de deuda con registro público en el país denominados en moneda extranjera íntegramente suscriptos en el exterior, en la medida que se verifiquen las siguientes condiciones:
> *heredado:* 3.5.3. El acceso al mercado de cambios se produce con una anterioridad no mayor a los 3
> *heredado:* (tres) días hábiles a la fecha de vencimiento del servicio de capital o interés a pagar. En el caso de que se trate de un pago de capital de títulos de deuda emitidos a partir del 08/11/24 que se concreta con una transferencia al exterior, el acceso al mercado de cambios deberá adicionalmente producirse una vez transcurridos, como mínimo, desde la fecha de emisión:
> *heredado:* i) 12 (doce) meses si el título fue emitido entre el 08/11/24 y el 20/04/25. ii) 6 (seis) meses si el título fue emitido entre 21/04/25 y el 15/05/25. iii) 18 (dieciocho) meses si el título fue emitido a partir del 16/05/25.
> *heredado:* El acceso al mercado de cambios antes de lo indicado requerirá la conformidad previa del BCRA excepto que el deudor encuadre en alguna de las siguientes situaciones y se cumplan la totalidad de las condiciones estipuladas en cada caso:
> *propio:* 3.5.3.2. Precancelación de capital e intereses con la liquidación simultánea de otros endeudamientos financieros comprendidos en este punto 3.5. i) la precancelación de capital e intereses sea efectuada en manera simultánea con los fondos liquidados de un nuevo endeudamiento financiero comprendido en este punto 3.5.; ii) la vida promedio del nuevo endeudamiento sea mayor a la vida promedio remanente de la deuda que se precancela; y iii) el monto acumulado de los vencimientos de capital del nuevo endeudamiento en ningún momento podrá superar, hasta la fecha de vencimiento de la deuda que se cancela, el monto que hubieran acumulado los vencimientos de capital de la deuda que se cancela.

- Estado final: `aceptado_tras_reintento`; rechazos: 1
- **e1 Excepcion** «Excepción precancelación con liquidación simultánea» — Se exceptúa la exigencia de conformidad previa del BCRA para acceso al mercado de cambios antes del plazo establecido cuando se trata de precancelación de capital e intereses realizada simultáneamente con fondos de nuevo endeudamiento financiero, siempre que se cumplan todas las condiciones especificadas. · tramo: «El acceso al mercado de cambios antes de lo indicado requerirá la conformidad previa del BCRA excepto que el deudor encuadre en alguna de las siguientes situaciones y se cumplan la totalidad de las condiciones estipuladas en cada caso: i) la precancelación de capital e intereses sea efectuada en manera simultánea con los fondos liquidados de un nuevo endeudamiento financiero comprendido en este punto 3.5.; ii) la vida promedio del nuevo endeudamiento sea mayor a la vida promedio remanente de la deuda que se precancela; y iii) el monto acumulado de los vencimientos de capital del nuevo endeudamiento en ningún momento podrá superar, hasta la fecha de vencimiento de la deuda que se cancela, el monto que hubieran acumulado los vencimientos de capital de la deuda que se cancela.»
- **c1 Condicion** «Precancelación simultánea con nuevo endeudamiento» — La precancelación de capital e intereses debe efectuarse de manera simultánea con los fondos liquidados de un nuevo endeudamiento financiero comprendido en el punto 3.5. · tramo: «la precancelación de capital e intereses sea efectuada en manera simultánea con los fondos liquidados de un nuevo endeudamiento financiero comprendido en este punto 3.5.»
- **c2 Condicion** «Vida promedio del nuevo endeudamiento mayor» — La vida promedio del nuevo endeudamiento debe ser mayor a la vida promedio remanente de la deuda que se precancela. · tramo: «la vida promedio del nuevo endeudamiento sea mayor a la vida promedio remanente de la deuda que se precancela»
- **r1 Restriccion** «Límite monto acumulado vencimientos capital nuevo endeudamiento» — El monto acumulado de los vencimientos de capital del nuevo endeudamiento no podrá superar, hasta la fecha de vencimiento de la deuda que se cancela, el monto que hubieran acumulado los vencimientos de capital de la deuda que se cancela. · props: `{"tipo": "limite_cuantitativo"}` · umbral: ['en ningún momento podrá superar, hasta la fecha de vencimiento de la deuda que se cancela, el monto que hubieran acumulado los vencimientos de capital de la deuda que se cancela'] · tramo: «el monto acumulado de los vencimientos de capital del nuevo endeudamiento en ningún momento podrá superar, hasta la fecha de vencimiento de la deuda que se cancela, el monto que hubieran acumulado los vencimientos de capital de la deuda que se cancela»
- R: c1 Condicion «Precancelación simultánea con nuevo endeudamiento» —condicion_de→ e1 Excepcion «Excepción precancelación con liquidación simultánea»
- R: c2 Condicion «Vida promedio del nuevo endeudamiento mayor» —condicion_de→ e1 Excepcion «Excepción precancelación con liquidación simultánea»

- **Lectura:** Condicion sin norma ni cuantificador, hacia una Excepcion compuesta en el ítem

## `ext::3.5.3.3` (ítem) — propuesta: **no_cumple**

> *heredado:* Sección 3. Disposiciones específicas para los egresos por el mercado de cambios
> *heredado:* Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–, adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables.
> *heredado:* 3.5. Pagos de títulos de deuda suscriptos en el exterior y endeudamientos financieros con el
> *heredado:* exterior. Las entidades podrán dar acceso al mercado de cambios para realizar pagos de capital o intereses de títulos de deuda con registro público en el exterior, otros endeudamientos financieros con el exterior y títulos de deuda con registro público en el país denominados en moneda extranjera íntegramente suscriptos en el exterior, en la medida que se verifiquen las siguientes condiciones:
> *heredado:* 3.5.3. El acceso al mercado de cambios se produce con una anterioridad no mayor a los 3
> *heredado:* (tres) días hábiles a la fecha de vencimiento del servicio de capital o interés a pagar. En el caso de que se trate de un pago de capital de títulos de deuda emitidos a partir del 08/11/24 que se concreta con una transferencia al exterior, el acceso al mercado de cambios deberá adicionalmente producirse una vez transcurridos, como mínimo, desde la fecha de emisión:
> *heredado:* i) 12 (doce) meses si el título fue emitido entre el 08/11/24 y el 20/04/25. ii) 6 (seis) meses si el título fue emitido entre 21/04/25 y el 15/05/25. iii) 18 (dieciocho) meses si el título fue emitido a partir del 16/05/25.
> *heredado:* El acceso al mercado de cambios antes de lo indicado requerirá la conformidad previa del BCRA excepto que el deudor encuadre en alguna de las siguientes situaciones y se cumplan la totalidad de las condiciones estipuladas en cada caso:
> *propio:* 3.5.3.3. Precancelación de intereses en el marco de un proceso de canje de títulos de deuda comprendidos en el punto 3.5. i) la precancelación de intereses se concreta en el marco de un proceso de canje de títulos de deuda emitidos por el cliente; ii) el monto abonado antes del vencimiento corresponde a los intereses devengados a la fecha de cierre del canje; iii) la vida promedio de los nuevos títulos de deuda es mayor a la vida promedio remanente del título canjeado; y iv)el monto acumulado de los vencimientos de capital de los nuevos títulos en ningún momento, hasta la fecha de vencimiento final del título canjeado, podrá superar el monto que hubieran acumulado los vencimientos de capital del título canjeado.

- Estado final: `aceptado_con_residuales`; rechazos: 0
- **e1 Operacion** «Precancelación de intereses en canje de títulos» — Precancelación de intereses en el marco de un proceso de canje de títulos de deuda emitidos por el cliente, donde el monto abonado antes del vencimiento corresponde a los intereses devengados a la fecha de cierre del canje. · props: `{"tipo": "Pago de intereses"}` · tramo: «precancelación de intereses se concreta en el marco de un proceso de canje de títulos de deuda emitidos por el cliente»
- **e2 Condicion** «Vida promedio nuevos títulos mayor a remanente» — La vida promedio de los nuevos títulos de deuda debe ser mayor a la vida promedio remanente del título canjeado. · tramo: «la vida promedio de los nuevos títulos de deuda es mayor a la vida promedio remanente del título canjeado»
- **e3 Restriccion** «Límite acumulado vencimientos capital nuevos títulos» — El monto acumulado de los vencimientos de capital de los nuevos títulos no podrá superar en ningún momento, hasta la fecha de vencimiento final del título canjeado, el monto que hubieran acumulado los vencimientos de capital del título canjeado. · props: `{"tipo": "limite_cualitativo"}` · tramo: «el monto acumulado de los vencimientos de capital de los nuevos títulos en ningún momento, hasta la fecha de vencimiento final del título canjeado, podrá superar el monto que hubieran acumulado los vencimientos de capital del título canjeado»
- **e4 Excepcion** «Excepción a conformidad previa BCRA — canje de títulos» — Se exceptúa del requisito de conformidad previa del BCRA para acceso al mercado de cambios cuando se trata de precancelación de intereses en el marco de un proceso de canje de títulos de deuda, siempre que se cumplan todas las condiciones especificadas. · tramo: «El acceso al mercado de cambios antes de lo indicado requerirá la conformidad previa del BCRA excepto que el deudor encuadre en alguna de las siguientes situaciones y se cumplan la totalidad de las condiciones estipuladas en cada caso: […] i) la precancelación de intereses se concreta en el marco de un proceso de canje de títulos de deuda emitidos por el cliente; ii) el monto abonado antes del vencimiento corresponde a los intereses devengados a la fecha de cierre del canje; iii) la vida promedio de los nuevos títulos de deuda es mayor a la vida promedio remanente del título canjeado; y iv) el monto acumulado de los vencimientos de capital de los nuevos títulos en ningún momento, hasta la fecha de vencimiento final del título canjeado, podrá superar el monto que hubieran acumulado los vencimientos de capital del título canjeado»
- R: e2 Condicion «Vida promedio nuevos títulos mayor a remanente» —condicion_de→ e1 Operacion «Precancelación de intereses en canje de títulos»
- R: e3 Restriccion «Límite acumulado vencimientos capital nuevos títulos» —limita→ e1 Operacion «Precancelación de intereses en canje de títulos» [coherente]
- R: e4 Excepcion «Excepción a conformidad previa BCRA — canje de títulos» —exceptua→ e3 Restriccion «Límite acumulado vencimientos capital nuevos títulos»
- Omisión `relacion_sin_predicado`: «el monto abonado antes del vencimiento corresponde a los intereses devengados a la fecha de cierre del canje» — Condición que especifica qué monto se abona (intereses devengados a cierre de canje); se extrae como parte de la descripción de e1 pero no como entidad separada porque es una caracterización del acto, no un supuesto independiente que condicione su realización

- **Lectura:** Condicion hacia la Operacion; Excepcion compuesta en el ítem, con exceptua hacia la Restriccion del ítem

## `ext::3.5.3.4` (ítem) — propuesta: **no_cumple**

> *heredado:* Sección 3. Disposiciones específicas para los egresos por el mercado de cambios
> *heredado:* Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–, adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables.
> *heredado:* 3.5. Pagos de títulos de deuda suscriptos en el exterior y endeudamientos financieros con el
> *heredado:* exterior. Las entidades podrán dar acceso al mercado de cambios para realizar pagos de capital o intereses de títulos de deuda con registro público en el exterior, otros endeudamientos financieros con el exterior y títulos de deuda con registro público en el país denominados en moneda extranjera íntegramente suscriptos en el exterior, en la medida que se verifiquen las siguientes condiciones:
> *heredado:* 3.5.3. El acceso al mercado de cambios se produce con una anterioridad no mayor a los 3
> *heredado:* (tres) días hábiles a la fecha de vencimiento del servicio de capital o interés a pagar. En el caso de que se trate de un pago de capital de títulos de deuda emitidos a partir del 08/11/24 que se concreta con una transferencia al exterior, el acceso al mercado de cambios deberá adicionalmente producirse una vez transcurridos, como mínimo, desde la fecha de emisión:
> *heredado:* i) 12 (doce) meses si el título fue emitido entre el 08/11/24 y el 20/04/25. ii) 6 (seis) meses si el título fue emitido entre 21/04/25 y el 15/05/25. iii) 18 (dieciocho) meses si el título fue emitido a partir del 16/05/25.
> *heredado:* El acceso al mercado de cambios antes de lo indicado requerirá la conformidad previa del BCRA excepto que el deudor encuadre en alguna de las siguientes situaciones y se cumplan la totalidad de las condiciones estipuladas en cada caso:
> *propio:* 3.5.3.4. Precancelación de capital e intereses en forma simultánea con la liquidación de un nuevo endeudamiento financiero otorgado por una entidad financiera local a partir de una línea de crédito del exterior. i) la precancelación de capital e intereses sea efectuada de manera simultánea con los fondos liquidados de un nuevo endeudamiento financiero otorgado por una entidad financiera local a partir de una línea de crédito del exterior; ii) la vida promedio del nuevo endeudamiento sea mayor a la vida promedio remanente de la deuda que se precancela; y iii) el monto acumulado de los vencimientos de capital del nuevo endeudamiento en ningún momento, hasta la fecha de vencimiento de la deuda que se cancela, podrá superar el monto que hubieran acumulado los vencimientos de capital de la deuda que se cancela.

- Estado final: `aceptado_con_residuales`; rechazos: 1
- **e1 Operacion** «Precancelación de capital e intereses con nuevo endeudamiento» — Precancelación de capital e intereses efectuada de manera simultánea con los fondos liquidados de un nuevo endeudamiento financiero otorgado por una entidad financiera local a partir de una línea de crédito del exterior · props: `{"tipo": "Precancelación de deuda"}` · tramo: «Precancelación de capital e intereses en forma simultánea con la liquidación de un nuevo endeudamiento financiero otorgado por una entidad financiera local a partir de una línea de crédito del exterior»
- **e2 Condicion** «Simultaneidad con liquidación de nuevo endeudamiento» — La precancelación debe efectuarse de manera simultánea con los fondos liquidados del nuevo endeudamiento · tramo: «la precancelación de capital e intereses sea efectuada de manera simultánea con los fondos liquidados de un nuevo endeudamiento financiero otorgado por una entidad financiera local a partir de una línea de crédito del exterior»
- **e3 Condicion** «Vida promedio del nuevo endeudamiento mayor a remanente» — La vida promedio del nuevo endeudamiento debe ser mayor a la vida promedio remanente de la deuda que se precancela · tramo: «la vida promedio del nuevo endeudamiento sea mayor a la vida promedio remanente de la deuda que se precancela»
- **e4 Restriccion** «Límite acumulado de vencimientos de capital del nuevo endeudamiento» — El monto acumulado de los vencimientos de capital del nuevo endeudamiento no podrá superar en ningún momento, hasta la fecha de vencimiento de la deuda que se cancela, el monto que hubieran acumulado los vencimientos de capital de la deuda que se cancela · props: `{"tipo": "limite_cuantitativo"}` · umbral: ['en ningún momento, hasta la fecha de vencimiento de la deuda que se cancela, podrá superar el monto que hubieran acumulado los vencimientos de capital de la deuda que se cancela'] · tramo: «el monto acumulado de los vencimientos de capital del nuevo endeudamiento en ningún momento, hasta la fecha de vencimiento de la deuda que se cancela, podrá superar el monto que hubieran acumulado los vencimientos de capital de la deuda que se cancela»
- **e5 Excepcion** «Excepción a conformidad previa del BCRA — precancelación simultánea» — Se exceptúa del requisito de conformidad previa del BCRA cuando el deudor encuadra en la situación de precancelación de capital e intereses en forma simultánea con liquidación de nuevo endeudamiento y se cumplen todas las condiciones especificadas · tramo: «El acceso al mercado de cambios antes de lo indicado requerirá la conformidad previa del BCRA excepto que el deudor encuadre en alguna de las siguientes situaciones y se cumplan la totalidad de las condiciones estipuladas en cada caso»
- R: e2 Condicion «Simultaneidad con liquidación de nuevo endeudamiento» —condicion_de→ e1 Operacion «Precancelación de capital e intereses con nuevo endeudamiento»
- R: e3 Condicion «Vida promedio del nuevo endeudamiento mayor a remanente» —condicion_de→ e1 Operacion «Precancelación de capital e intereses con nuevo endeudamiento»
- R: e4 Restriccion «Límite acumulado de vencimientos de capital del nuevo endeudamiento» —limita→ e1 Operacion «Precancelación de capital e intereses con nuevo endeudamiento» [coherente]
- Omisión `relacion_sin_predicado`: «El acceso al mercado de cambios antes de lo indicado requerirá la conformidad previa del BCRA excepto que el deudor encuadre en alguna de las siguientes situaciones» — Relación entre la Excepcion (e5) y la Obligacion implícita de obtener conformidad previa del BCRA; no hay predicado que represente 'exceptúa una obligación de obtener conformidad' cuando la obligación no está explícitamente extraída en esta unidad (está en el contexto heredado punto 3.5.3)

- **Lectura:** Condicion hacia la Operacion, sin norma ni cuantificador; Excepcion compuesta en el ítem

## `ext::3.5.3.5` (ítem) — propuesta: **no_cumple**

> *heredado:* Sección 3. Disposiciones específicas para los egresos por el mercado de cambios
> *heredado:* Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–, adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables.
> *heredado:* 3.5. Pagos de títulos de deuda suscriptos en el exterior y endeudamientos financieros con el
> *heredado:* exterior. Las entidades podrán dar acceso al mercado de cambios para realizar pagos de capital o intereses de títulos de deuda con registro público en el exterior, otros endeudamientos financieros con el exterior y títulos de deuda con registro público en el país denominados en moneda extranjera íntegramente suscriptos en el exterior, en la medida que se verifiquen las siguientes condiciones:
> *heredado:* 3.5.3. El acceso al mercado de cambios se produce con una anterioridad no mayor a los 3
> *heredado:* (tres) días hábiles a la fecha de vencimiento del servicio de capital o interés a pagar. En el caso de que se trate de un pago de capital de títulos de deuda emitidos a partir del 08/11/24 que se concreta con una transferencia al exterior, el acceso al mercado de cambios deberá adicionalmente producirse una vez transcurridos, como mínimo, desde la fecha de emisión:
> *heredado:* i) 12 (doce) meses si el título fue emitido entre el 08/11/24 y el 20/04/25. ii) 6 (seis) meses si el título fue emitido entre 21/04/25 y el 15/05/25. iii) 18 (dieciocho) meses si el título fue emitido a partir del 16/05/25.
> *heredado:* El acceso al mercado de cambios antes de lo indicado requerirá la conformidad previa del BCRA excepto que el deudor encuadre en alguna de las siguientes situaciones y se cumplan la totalidad de las condiciones estipuladas en cada caso:
> *propio:* 3.5.3.5. Precancelación de capital e intereses por parte de un VPU adherido al RIGI. El cliente es un Vehículo de Proyecto Único (VPU) adherido al Régimen de Incentivo para Grandes Inversiones (RIGI) que precancela capital o intereses devengados por endeudamientos financieros comprendidos en este punto 3.5. en el marco de lo previsto en el punto 14.2.1.

- Estado final: `aceptado_tras_reintento`; rechazos: 5
- **c1 Condicion** «Anterioridad máxima 3 días hábiles» — El acceso al mercado de cambios debe producirse con una anterioridad no mayor a 3 días hábiles a la fecha de vencimiento del servicio de capital o interés a pagar · umbral: ['no mayor a los 3 (tres) días hábiles'] · tramo: «El acceso al mercado de cambios se produce con una anterioridad no mayor a los 3 (tres) días hábiles a la fecha de vencimiento del servicio de capital o interés a pagar»
- **c2 Condicion** «Plazo mínimo desde emisión — títulos 08/11/24 a 20/04/25» — Para títulos de deuda emitidos entre el 08/11/24 y el 20/04/25, el acceso al mercado de cambios debe producirse una vez transcurridos, como mínimo, 12 meses desde la fecha de emisión · umbral: ['12 (doce) meses'] · tramo: «12 (doce) meses si el título fue emitido entre el 08/11/24 y el 20/04/25»
- **c3 Condicion** «Plazo mínimo desde emisión — títulos 21/04/25 a 15/05/25» — Para títulos de deuda emitidos entre el 21/04/25 y el 15/05/25, el acceso al mercado de cambios debe producirse una vez transcurridos, como mínimo, 6 meses desde la fecha de emisión · umbral: ['6 (seis) meses'] · tramo: «6 (seis) meses si el título fue emitido entre 21/04/25 y el 15/05/25»
- **c4 Condicion** «Plazo mínimo desde emisión — títulos a partir de 16/05/25» — Para títulos de deuda emitidos a partir del 16/05/25, el acceso al mercado de cambios debe producirse una vez transcurridos, como mínimo, 18 meses desde la fecha de emisión · umbral: ['18 (dieciocho) meses'] · tramo: «18 (dieciocho) meses si el título fue emitido a partir del 16/05/25»
- **e1 Excepcion** «Excepción VPU-RIGI — precancelación de capital e intereses» — Quedan exceptuados de los requisitos de anterioridad y plazo mínimo desde emisión los VPU adheridos al RIGI que precancelen capital o intereses devengados por endeudamientos financieros comprendidos en el punto 3.5, en el marco de lo previsto en el punto 14.2.1 · tramo: «El cliente es un Vehículo de Proyecto Único (VPU) adherido al Régimen de Incentivo para Grandes Inversiones (RIGI) que precancela capital o intereses devengados por endeudamientos financieros comprendidos en este punto 3.5. en el marco de lo previsto en el punto 14.2.1»
- **op1 Operacion** «Precancelación de capital e intereses — VPU-RIGI» — Precancelación de capital o intereses devengados por endeudamientos financieros comprendidos en el punto 3.5, realizada por un VPU adherido al RIGI · props: `{"tipo": "Precancelación de capital o intereses"}` · tramo: «precancela capital o intereses devengados por endeudamientos financieros comprendidos en este punto 3.5»
- Omisión `meta_normativo`: «en el marco de lo previsto en el punto 14.2.1» — Remisión a otra norma que contextualiza pero no prescribe conducta en esta unidad

- **Lectura:** las Condicion son las del encabezado, copiadas; el supuesto (VPU adherido al RIGI) va en la Excepcion, sin Condicion propia

# Lista `ext::3.13.1` (b1)

## `ext::3.13.1::intro` (encabezado) — propuesta: **no_cumple**

> *heredado:* Sección 3. Disposiciones específicas para los egresos por el mercado de cambios
> *heredado:* 3.13. Repatriaciones de inversiones directas y otras compras de moneda extranjera por parte de no
> *heredado:* 3.13.1. El acceso al mercado de cambios para la repatriación de inversiones de no
> *propio:* residentes y otras compras de moneda extranjera por parte de clientes no residentes requerirá la conformidad previa del BCRA, excepto para las operaciones de:

- Estado final: `completo_ok_directo`; rechazos: 0
- **e1 Operacion** «Repatriación de inversiones de no residentes» — Repatriación de inversiones de no residentes mediante acceso al mercado de cambios · props: `{"tipo": "compra de moneda extranjera"}` · tramo: «repatriación de inversiones de no residentes»
- **e2 Operacion** «Compra de moneda extranjera por clientes no residentes» — Compras de moneda extranjera realizadas por clientes no residentes · props: `{"tipo": "compra de moneda extranjera"}` · tramo: «otras compras de moneda extranjera por parte de clientes no residentes»
- **e3 Obligacion** «Conformidad previa del BCRA requerida» — El acceso al mercado de cambios para la repatriación de inversiones de no residentes y otras compras de moneda extranjera por parte de clientes no residentes requiere la conformidad previa del BCRA · props: `{"tipo": "otra"}` · tramo: «requerirá la conformidad previa del BCRA»
- **e4 Excepcion** «Excepción conformidad previa — operaciones especificadas» — Quedan exceptuadas de la exigencia de conformidad previa del BCRA las operaciones que se especifican a continuación · tramo: «excepto para las operaciones de:»
- R: e3 Obligacion «Conformidad previa del BCRA requerida» —aplica_a→ Sujeto_contraparte (mención «clientes no residentes», exacta)
- R: e4 Excepcion «Excepción conformidad previa — operaciones especificadas» —exceptua_obligacion→ e3 Obligacion «Conformidad previa del BCRA requerida»

- **Lectura:** dos Operacion, la Obligacion de la conformidad previa y una Excepcion general con exceptua_obligacion; no hay Definicion de la clase

## `ext::3.13.1.1` (ítem) — propuesta: **cumple**

> *heredado:* Sección 3. Disposiciones específicas para los egresos por el mercado de cambios
> *heredado:* Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–, adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables.
> *heredado:* 3.13. Repatriaciones de inversiones directas y otras compras de moneda extranjera por parte de no
> *heredado:* residentes
> *heredado:* 3.13.1. El acceso al mercado de cambios para la repatriación de inversiones de no
> *heredado:* residentes y otras compras de moneda extranjera por parte de clientes no residentes requerirá la conformidad previa del BCRA, excepto para las operaciones de:
> *heredado:* Si una repatriación de una inversión directa de no residentes consiste en una reducción de capital y/o devolución de aportes irrevocables realizadas por la empresa local, adicionalmente a los requisitos previstos en cada caso, la entidad deberá contar con la documentación que demuestre que se han cumplimentado los mecanismos legales previstos y haber verificado que se encuentra declarada, en caso de corresponder, en la última presentación vencida del "Relevamiento de activos y pasivos externos" el pasivo en pesos con el exterior generado a partir de la fecha de la no aceptación del aporte irrevocable o de la reducción de capital según corresponda.
> *propio:* 3.13.1.1. Organismos internacionales e instituciones que cumplan funciones de agencias oficiales de crédito.

- Estado final: `aceptado_tras_reintento`; rechazos: 1
- **e1 Definicion** «Organismos internacionales — agencias oficiales de crédito» — Organismos internacionales e instituciones que cumplen funciones de agencias oficiales de crédito · props: `{"termino": "Organismos internacionales e instituciones que cumplan funciones de agencias oficiales de crédito"}` · tramo: «Organismos internacionales e instituciones que cumplan funciones de agencias oficiales de crédito»
- **e2 Excepcion** «Excepción — repatriación inversiones no residentes» — Las operaciones de repatriación de inversiones de no residentes y otras compras de moneda extranjera por parte de clientes no residentes realizadas por organismos internacionales e instituciones que cumplan funciones de agencias oficiales de crédito quedan exceptuadas del requisito de conformidad previa del BCRA · tramo: «Organismos internacionales e instituciones que cumplan funciones de agencias oficiales de crédito»
- Omisión `relacion_sin_predicado`: «El acceso al mercado de cambios para la repatriación de inversiones de no residentes y otras compras de moneda extranjera por parte de clientes no residentes requerirá la conformidad previa del BCRA, excepto para las operaciones de: Organismos internacionales e instituciones que cumplan funciones de agencias oficiales de crédito» — La norma troncal del punto 3.13.1 (obligación de conformidad previa del BCRA para acceso al mercado de cambios) está enunciada en el encabezado heredado 3.13.1, no en el texto de la unidad 3.13.1.1. El punto 3.13.1.1 enuncia solo la excepción a esa norma. La norma principal no está en el chunk de la unidad 3.13.1.1 sino en la unidad del encabezado 3.13.1, que tiene su propia unidad de extracción. Por lo tanto, la Excepcion e2 no puede conectarse con exceptua_obligacion a una Obligacion que no está en este chunk.

- **Lectura:** Excepcion «…quedan exceptuadas del requisito de conformidad previa del BCRA» por el miembro (organismos internacionales), sin exceptua colgante

## `ext::3.13.1.2` (ítem) — propuesta: **cumple**

> *heredado:* Sección 3. Disposiciones específicas para los egresos por el mercado de cambios
> *heredado:* Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–, adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables.
> *heredado:* 3.13. Repatriaciones de inversiones directas y otras compras de moneda extranjera por parte de no
> *heredado:* residentes
> *heredado:* 3.13.1. El acceso al mercado de cambios para la repatriación de inversiones de no
> *heredado:* residentes y otras compras de moneda extranjera por parte de clientes no residentes requerirá la conformidad previa del BCRA, excepto para las operaciones de:
> *heredado:* Si una repatriación de una inversión directa de no residentes consiste en una reducción de capital y/o devolución de aportes irrevocables realizadas por la empresa local, adicionalmente a los requisitos previstos en cada caso, la entidad deberá contar con la documentación que demuestre que se han cumplimentado los mecanismos legales previstos y haber verificado que se encuentra declarada, en caso de corresponder, en la última presentación vencida del "Relevamiento de activos y pasivos externos" el pasivo en pesos con el exterior generado a partir de la fecha de la no aceptación del aporte irrevocable o de la reducción de capital según corresponda.
> *propio:* 3.13.1.2. Representaciones diplomáticas y consulares y personal diplomático acreditado en el país por transferencias que efectúen en ejercicio de sus funciones.

- Estado final: `aceptado_con_residuales`; rechazos: 0
- **e1 Excepcion** «Excepción repatriación — representaciones diplomáticas» — Quedan exceptuadas de la exigencia de conformidad previa del BCRA las operaciones de repatriación de inversiones de no residentes y otras compras de moneda extranjera realizadas por representaciones diplomáticas y consulares y personal diplomático acreditado en el país, cuando las transferencias se efectúen en ejercicio de sus funciones. · tramo: «Representaciones diplomáticas y consulares y personal diplomático acreditado en el país por transferencias que efectúen en ejercicio de sus funciones»
- Omisión `relacion_sin_predicado`: «Representaciones diplomáticas y consulares y personal diplomático acreditado en el país por transferencias que efectúen en ejercicio de sus funciones» — La excepción exceptúa una norma (la exigencia de conformidad previa del BCRA para repatriaciones de inversiones de no residentes) que está en la unidad del encabezado (punto 3.13.1), no en esta unidad. No se emite la relación exceptua hacia esa norma porque no está en el chunk.

- **Lectura:** Excepcion por el miembro (representaciones diplomáticas), con la norma

## `ext::3.13.1.3` (ítem) — propuesta: **cumple**

> *heredado:* Sección 3. Disposiciones específicas para los egresos por el mercado de cambios
> *heredado:* Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–, adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables.
> *heredado:* 3.13. Repatriaciones de inversiones directas y otras compras de moneda extranjera por parte de no
> *heredado:* residentes
> *heredado:* 3.13.1. El acceso al mercado de cambios para la repatriación de inversiones de no
> *heredado:* residentes y otras compras de moneda extranjera por parte de clientes no residentes requerirá la conformidad previa del BCRA, excepto para las operaciones de:
> *heredado:* Si una repatriación de una inversión directa de no residentes consiste en una reducción de capital y/o devolución de aportes irrevocables realizadas por la empresa local, adicionalmente a los requisitos previstos en cada caso, la entidad deberá contar con la documentación que demuestre que se han cumplimentado los mecanismos legales previstos y haber verificado que se encuentra declarada, en caso de corresponder, en la última presentación vencida del "Relevamiento de activos y pasivos externos" el pasivo en pesos con el exterior generado a partir de la fecha de la no aceptación del aporte irrevocable o de la reducción de capital según corresponda.
> *propio:* 3.13.1.3. Representaciones en el país de Tribunales, Autoridades u Oficinas, Misiones Especiales, Comisiones u Órganos Bilaterales establecidos por Tratados o Convenios Internacionales, en los cuales la República Argentina es parte, en la medida que las transferencias se realicen en ejercicio de sus funciones.

- Estado final: `completo_ok_directo`; rechazos: 1
- **e1 Operacion** «Transferencias por Representaciones de Tribunales, Autoridades u Oficinas» — Transferencias realizadas por Representaciones en el país de Tribunales, Autoridades u Oficinas, Misiones Especiales, Comisiones u Órganos Bilaterales establecidos por Tratados o Convenios Internacionales, en los cuales la República Argentina es parte, en ejercicio de sus funciones. · props: `{"tipo": "transferencia de moneda extranjera"}` · tramo: «transferencias se realicen en ejercicio de sus funciones»
- **e2 Excepcion** «Excepción conformidad previa BCRA — Representaciones de Tribunales, Autoridades u Oficinas» — Quedan exceptuadas del requisito de conformidad previa del BCRA las transferencias realizadas por Representaciones en el país de Tribunales, Autoridades u Oficinas, Misiones Especiales, Comisiones u Órganos Bilaterales establecidos por Tratados o Convenios Internacionales, en los cuales la República Argentina es parte, cuando se realicen en ejercicio de sus funciones. · tramo: «Representaciones en el país de Tribunales, Autoridades u Oficinas, Misiones Especiales, Comisiones u Órganos Bilaterales establecidos por Tratados o Convenios Internacionales, en los cuales la República Argentina es parte, en la medida que las transferencias se realicen en ejercicio de sus funciones»
- Omisión `relacion_sin_predicado`: «Representaciones en el país de Tribunales, Autoridades u Oficinas, Misiones Especiales, Comisiones u Órganos Bilaterales establecidos por Tratados o Convenios Internacionales» — ejecuta

- **Lectura:** Excepcion por el miembro (representaciones de tribunales…), con la norma

## `ext::3.13.1.4` (ítem) — propuesta: **no_cumple**

> *heredado:* Sección 3. Disposiciones específicas para los egresos por el mercado de cambios
> *heredado:* Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–, adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables.
> *heredado:* 3.13. Repatriaciones de inversiones directas y otras compras de moneda extranjera por parte de no
> *heredado:* residentes
> *heredado:* 3.13.1. El acceso al mercado de cambios para la repatriación de inversiones de no
> *heredado:* residentes y otras compras de moneda extranjera por parte de clientes no residentes requerirá la conformidad previa del BCRA, excepto para las operaciones de:
> *heredado:* Si una repatriación de una inversión directa de no residentes consiste en una reducción de capital y/o devolución de aportes irrevocables realizadas por la empresa local, adicionalmente a los requisitos previstos en cada caso, la entidad deberá contar con la documentación que demuestre que se han cumplimentado los mecanismos legales previstos y haber verificado que se encuentra declarada, en caso de corresponder, en la última presentación vencida del "Relevamiento de activos y pasivos externos" el pasivo en pesos con el exterior generado a partir de la fecha de la no aceptación del aporte irrevocable o de la reducción de capital según corresponda.
> *propio:* 3.13.1.4. Transferencias al exterior a nombre de personas humanas que sean beneficiarias de jubilaciones y/o pensiones abonadas por la Administración Nacional de la Seguridad Social (ANSES) u otros organismos previsionales y/o de rentas vitalicias previsionales previstas por el art. 101 de la Ley 24.241, por hasta el monto percibido por tales conceptos en los últimos 30 (treinta) días corridos y en la medida que la transferencia se efectúe a una cuenta bancaria de titularidad del beneficiario en su país de residencia registrado.

- Estado final: `cola_humana_veredicto_inutilizable`; rechazos: 1
- **e1 Operacion** «Transferencia al exterior — jubilaciones/pensiones ANSES» — Transferencia al exterior a nombre de personas humanas beneficiarias de jubilaciones y/o pensiones abonadas por ANSES u otros organismos previsionales y/o de rentas vitalicias previsionales previstas por el art. 101 de la Ley 24.241, hacia una cuenta bancaria de titularidad del beneficiario en su país de residencia registrado · props: `{"tipo": "Transferencia de fondos al exterior"}` · tramo: «Transferencias al exterior a nombre de personas humanas que sean beneficiarias de jubilaciones y/o pensiones abonadas por la Administración Nacional de la Seguridad Social (ANSES) u otros organismos previsionales y/o de rentas vitalicias previsionales previstas por el art. 101 de la Ley 24.241»
- **e2 Restriccion** «Límite monto — últimos 30 días» — El monto de la transferencia no podrá exceder el monto percibido por jubilaciones, pensiones u otros conceptos previsionales en los últimos 30 días corridos · props: `{"tipo": "limite_cuantitativo"}` · umbral: ['por hasta el monto percibido por tales conceptos en los últimos 30 (treinta) días corridos'] · tramo: «por hasta el monto percibido por tales conceptos en los últimos 30 (treinta) días corridos»
- **e3 Condicion** «Transferencia a cuenta del beneficiario en país de residencia» — La transferencia debe efectuarse a una cuenta bancaria de titularidad del beneficiario en su país de residencia registrado · tramo: «en la medida que la transferencia se efectúe a una cuenta bancaria de titularidad del beneficiario en su país de residencia registrado»
- **e4 Obligacion** «Conformidad previa del BCRA — repatriación no residentes» — El acceso al mercado de cambios para la repatriación de inversiones de no residentes y otras compras de moneda extranjera por parte de clientes no residentes requiere la conformidad previa del BCRA, excepto para las operaciones enumeradas en los puntos siguientes · props: `{"tipo": "otra"}` · tramo: «El acceso al mercado de cambios para la repatriación de inversiones de no residentes y otras compras de moneda extranjera por parte de clientes no residentes requerirá la conformidad previa del BCRA, excepto para las operaciones de:»
- R: e2 Restriccion «Límite monto — últimos 30 días» —limita→ e1 Operacion «Transferencia al exterior — jubilaciones/pensiones ANSES» [coherente]
- R: e3 Condicion «Transferencia a cuenta del beneficiario en país de residencia» —condicion_de→ e1 Operacion «Transferencia al exterior — jubilaciones/pensiones ANSES»
- Omisión `meta_normativo`: «Si una repatriación de una inversión directa de no residentes consiste en una reducción de capital y/o devolución de aportes irrevocables realizadas por la empresa local, adicionalmente a los requisitos previstos en cada caso, la entidad deberá contar con la documentación que demuestre que se han cumplimentado los mecanismos legales previstos y haber verificado que se encuentra declarada, en caso de corresponder, en la última presentación vencida del "Relevamiento de activos y pasivos externos" el pasivo en pesos con el exterior generado a partir de la fecha de la no aceptación del aporte irrevocable o de la reducción de capital según corresponda.» — Contenido del párrafo de cierre del punto 3.13.1 (contexto heredado): no se extrae de bloques heredados salvo composición con encabezado de lista
- Faltante de E3 pendiente (otro, alta): «Si una repatriación de una inversión directa de no residentes consiste en una reducción de capital y/o devolución de aportes irrevocables realizadas por la empresa local, adicionalmente a los requisitos previstos en cada caso, la entidad deberá contar con la documentación que demuestre que se han cumplimentado los mecanismos legales previstos y haber verificado que se encuentra declarada, en caso de corresponder, en la última presentación vencida del "Relevamiento de activos y pasivos externos" el pasivo en pesos con el exterior generado a partir de la fecha de la no aceptación del aporte irrevocable o de la reducción de capital según corresponda.»

- **Lectura:** sin Excepcion; repite la Obligacion de la conformidad previa del encabezado

## `ext::3.13.1.5` (ítem) — propuesta: **no_cumple**

> *heredado:* Sección 3. Disposiciones específicas para los egresos por el mercado de cambios
> *heredado:* Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–, adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables.
> *heredado:* 3.13. Repatriaciones de inversiones directas y otras compras de moneda extranjera por parte de no
> *heredado:* residentes
> *heredado:* 3.13.1. El acceso al mercado de cambios para la repatriación de inversiones de no
> *heredado:* residentes y otras compras de moneda extranjera por parte de clientes no residentes requerirá la conformidad previa del BCRA, excepto para las operaciones de:
> *heredado:* Si una repatriación de una inversión directa de no residentes consiste en una reducción de capital y/o devolución de aportes irrevocables realizadas por la empresa local, adicionalmente a los requisitos previstos en cada caso, la entidad deberá contar con la documentación que demuestre que se han cumplimentado los mecanismos legales previstos y haber verificado que se encuentra declarada, en caso de corresponder, en la última presentación vencida del "Relevamiento de activos y pasivos externos" el pasivo en pesos con el exterior generado a partir de la fecha de la no aceptación del aporte irrevocable o de la reducción de capital según corresponda.
> *propio:* 3.13.1.5. Compra de billetes en moneda extranjera de personas humanas no residentes en concepto de turismo y viajes por hasta un monto máximo equivalente a USD 100 (dólares estadounidenses cien) en el conjunto de las entidades, en la medida que la entidad haya verificado en el sistema online implementado por el BCRA que el cliente ha liquidado un monto mayor o igual al que desea adquirir dentro de los 90 (noventa) días corridos anteriores. Esta operatoria quedará habilitada a partir de que la venta de moneda extranjera liquidada por el cliente haya sido registrada ante el BCRA por la entidad interviniente de acuerdo con las pautas habituales. Las liquidaciones encuadradas, durante su vigencia, en la operatoria con títulos valores por cuenta y orden de turistas no residentes no serán tomadas en cuenta a los efectos de lo establecido en este punto.

- Estado final: `aceptado_con_residuales`; rechazos: 0
- **e1 Operacion** «Compra de billetes en moneda extranjera — turismo» — Compra de billetes en moneda extranjera por personas humanas no residentes en concepto de turismo y viajes, sujeta a verificación de liquidación previa en el sistema online del BCRA · props: `{"tipo": "compra de moneda extranjera"}` · tramo: «Compra de billetes en moneda extranjera de personas humanas no residentes en concepto de turismo y viajes»
- **e2 Restriccion** «Tope USD 100 — compra de billetes turismo» — El monto máximo de compra de billetes en moneda extranjera por personas humanas no residentes en concepto de turismo no podrá exceder USD 100 en el conjunto de las entidades · props: `{"tipo": "limite_cuantitativo"}` · umbral: ['por hasta un monto máximo equivalente a USD 100 (dólares estadounidenses cien)'] · tramo: «por hasta un monto máximo equivalente a USD 100 (dólares estadounidenses cien) en el conjunto de las entidades»
- **e3 Condicion** «Verificación de liquidación previa — 90 días» — La operación se habilita cuando la entidad verifica en el sistema online del BCRA que el cliente ha liquidado un monto mayor o igual al que desea adquirir dentro de los 90 días corridos anteriores · umbral: ['dentro de los 90 (noventa) días corridos anteriores'] · tramo: «en la medida que la entidad haya verificado en el sistema online implementado por el BCRA que el cliente ha liquidado un monto mayor o igual al que desea adquirir dentro de los 90 (noventa) días corridos anteriores»
- **e4 Obligacion** «Registro de venta de moneda extranjera ante BCRA» — La operatoria de compra de billetes en moneda extranjera quedará habilitada a partir de que la venta de moneda extranjera liquidada por el cliente haya sido registrada ante el BCRA por la entidad interviniente de acuerdo con las pautas habituales · props: `{"tipo": "reporte_al_supervisor"}` · tramo: «la venta de moneda extranjera liquidada por el cliente haya sido registrada ante el BCRA por la entidad interviniente de acuerdo con las pautas habituales»
- **e5 Excepcion** «Exclusión — operatoria con títulos valores de turistas» — Las liquidaciones en la operatoria con títulos valores por cuenta y orden de turistas no residentes no se computan para el límite de USD 100 establecido en este punto · tramo: «Las liquidaciones encuadradas, durante su vigencia, en la operatoria con títulos valores por cuenta y orden de turistas no residentes no serán tomadas en cuenta a los efectos de lo establecido en este punto»
- R: e2 Restriccion «Tope USD 100 — compra de billetes turismo» —limita→ e1 Operacion «Compra de billetes en moneda extranjera — turismo» [coherente]
- R: e3 Condicion «Verificación de liquidación previa — 90 días» —condicion_de→ e1 Operacion «Compra de billetes en moneda extranjera — turismo»
- R: e4 Obligacion «Registro de venta de moneda extranjera ante BCRA» —condiciona→ e1 Operacion «Compra de billetes en moneda extranjera — turismo»
- R: e5 Excepcion «Exclusión — operatoria con títulos valores de turistas» —exceptua→ e2 Restriccion «Tope USD 100 — compra de billetes turismo»
- R: e1 Operacion «Compra de billetes en moneda extranjera — turismo» —aplica_a→ Sujeto_persona_humana (mención «personas humanas no residentes», exacta)
- R: e2 Restriccion «Tope USD 100 — compra de billetes turismo» —aplica_a→ Sujeto_persona_humana (mención «personas humanas no residentes», exacta)
- R: e4 Obligacion «Registro de venta de moneda extranjera ante BCRA» —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad interviniente», exacta)
- Omisión `meta_normativo`: «Esta operatoria quedará habilitada a partir de que la venta de moneda extranjera liquidada por el cliente haya sido registrada ante el BCRA por la entidad interviniente de acuerdo con las pautas habituales» — Cláusula que enuncia la habilitación de la operatoria como consecuencia de una acción previa (el registro), no como un deber autónomo; el contenido prescriptivo (el deber de registrar) se extrae en e4

- **Lectura:** la Excepcion es de otra cosa (las liquidaciones de títulos no se computan en el tope); sin la del miembro

## `ext::3.13.1.6` (ítem) — propuesta: **cumple**

> *heredado:* Sección 3. Disposiciones específicas para los egresos por el mercado de cambios
> *heredado:* Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–, adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables.
> *heredado:* 3.13. Repatriaciones de inversiones directas y otras compras de moneda extranjera por parte de no
> *heredado:* residentes
> *heredado:* 3.13.1. El acceso al mercado de cambios para la repatriación de inversiones de no
> *heredado:* residentes y otras compras de moneda extranjera por parte de clientes no residentes requerirá la conformidad previa del BCRA, excepto para las operaciones de:
> *heredado:* Si una repatriación de una inversión directa de no residentes consiste en una reducción de capital y/o devolución de aportes irrevocables realizadas por la empresa local, adicionalmente a los requisitos previstos en cada caso, la entidad deberá contar con la documentación que demuestre que se han cumplimentado los mecanismos legales previstos y haber verificado que se encuentra declarada, en caso de corresponder, en la última presentación vencida del "Relevamiento de activos y pasivos externos" el pasivo en pesos con el exterior generado a partir de la fecha de la no aceptación del aporte irrevocable o de la reducción de capital según corresponda.
> *propio:* 3.13.1.6. Transferencias a cuentas bancarias en el exterior de personas humanas por los fondos que percibieron en el país asociados a los beneficios otorgados por el Estado Nacional en el marco de las Leyes 24.043, 24.411 y 25.914 y concordantes.

- Estado final: `aceptado_tras_reintento`; rechazos: 0
- **e1 Operacion** «Repatriación inversiones no residentes» — Repatriación de inversiones directas de no residentes · props: `{"tipo": "repatriación de inversión directa"}` · tramo: «repatriación de inversiones de no residentes»
- **e2 Operacion** «Compras moneda extranjera no residentes» — Compras de moneda extranjera por parte de clientes no residentes · props: `{"tipo": "compra de moneda extranjera"}` · tramo: «otras compras de moneda extranjera por parte de clientes no residentes»
- **e3 Restriccion** «Conformidad previa BCRA repatriación» — El acceso al mercado de cambios para repatriación de inversiones de no residentes y otras compras de moneda extranjera por parte de clientes no residentes requiere conformidad previa del BCRA · props: `{"tipo": "limite_cualitativo"}` · tramo: «El acceso al mercado de cambios para la repatriación de inversiones de no residentes y otras compras de moneda extranjera por parte de clientes no residentes requerirá la conformidad previa del BCRA»
- **e4 Operacion** «Transferencias a cuentas bancarias exterior personas humanas» — Transferencias a cuentas bancarias en el exterior de personas humanas por fondos percibidos en el país asociados a beneficios otorgados por el Estado Nacional en el marco de las Leyes 24.043, 24.411 y 25.914 y concordantes · props: `{"tipo": "transferencia de fondos"}` · tramo: «Transferencias a cuentas bancarias en el exterior de personas humanas por los fondos que percibieron en el país asociados a los beneficios otorgados por el Estado Nacional en el marco de las Leyes 24.043, 24.411 y 25.914 y concordantes»
- **e5 Excepcion** «Excepción conformidad previa transferencias beneficios estatales» — Quedan exceptuadas de la exigencia de conformidad previa del BCRA las transferencias a cuentas bancarias en el exterior de personas humanas por fondos percibidos en el país asociados a beneficios otorgados por el Estado Nacional en el marco de las Leyes 24.043, 24.411 y 25.914 y concordantes · tramo: «Transferencias a cuentas bancarias en el exterior de personas humanas por los fondos que percibieron en el país asociados a los beneficios otorgados por el Estado Nacional en el marco de las Leyes 24.043, 24.411 y 25.914 y concordantes»
- R: e3 Restriccion «Conformidad previa BCRA repatriación» —limita→ e1 Operacion «Repatriación inversiones no residentes» [coherente]
- R: e3 Restriccion «Conformidad previa BCRA repatriación» —limita→ e2 Operacion «Compras moneda extranjera no residentes» [coherente]
- R: e5 Excepcion «Excepción conformidad previa transferencias beneficios estatales» —exceptua→ e3 Restriccion «Conformidad previa BCRA repatriación»
- Omisión `meta_normativo`: «excepto para las operaciones de:» — Anuncio de lista de excepciones; el contenido de cada excepción se extrae en su punto correspondiente

- **Lectura:** Excepcion por el miembro, con la norma, y exceptua hacia la Restriccion de la conformidad del mismo ítem (no colgante)

## `ext::3.13.1.7` (ítem) — propuesta: **no_cumple**

> *heredado:* Sección 3. Disposiciones específicas para los egresos por el mercado de cambios
> *heredado:* Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–, adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables.
> *heredado:* 3.13. Repatriaciones de inversiones directas y otras compras de moneda extranjera por parte de no
> *heredado:* residentes
> *heredado:* 3.13.1. El acceso al mercado de cambios para la repatriación de inversiones de no
> *heredado:* residentes y otras compras de moneda extranjera por parte de clientes no residentes requerirá la conformidad previa del BCRA, excepto para las operaciones de:
> *heredado:* Si una repatriación de una inversión directa de no residentes consiste en una reducción de capital y/o devolución de aportes irrevocables realizadas por la empresa local, adicionalmente a los requisitos previstos en cada caso, la entidad deberá contar con la documentación que demuestre que se han cumplimentado los mecanismos legales previstos y haber verificado que se encuentra declarada, en caso de corresponder, en la última presentación vencida del "Relevamiento de activos y pasivos externos" el pasivo en pesos con el exterior generado a partir de la fecha de la no aceptación del aporte irrevocable o de la reducción de capital según corresponda.
> *propio:* 3.13.1.7. Repatriaciones de inversiones directas de no residentes en empresas que no sean controlantes de entidades financieras locales de un aporte de capital que haya sido ingresado y liquidado por el mercado de cambios a partir del 02/10/20 en la medida que: i) la repatriación tenga lugar como mínimo 180 (ciento ochenta) días corridos después de la liquidación de los fondos del aporte si el aporte fue ingresado y liquidado a partir del 21/04/25; o ii) la repatriación tenga lugar como mínimo 2 (dos) años después de su liquidación si el aporte fue ingresado y liquidado entre el 02/10/20 y el 20/04/25.

- Estado final: `completo_ok_directo`; rechazos: 0
- **e1 Operacion** «Repatriación inversión directa no residentes» — Repatriación de inversiones directas de no residentes en empresas que no sean controlantes de entidades financieras locales, de un aporte de capital ingresado y liquidado por el mercado de cambios a partir del 02/10/20 · props: `{"tipo": "Repatriación de inversión directa"}` · tramo: «Repatriaciones de inversiones directas de no residentes en empresas que no sean controlantes de entidades financieras locales de un aporte de capital que haya sido ingresado y liquidado por el mercado de cambios a partir del 02/10/20»
- **e2 Condicion** «Plazo mínimo 180 días — aporte desde 21/04/25» — La repatriación debe tener lugar como mínimo 180 días corridos después de la liquidación de los fondos del aporte si el aporte fue ingresado y liquidado a partir del 21/04/25 · umbral: ['como mínimo 180 (ciento ochenta) días corridos'] · tramo: «la repatriación tenga lugar como mínimo 180 (ciento ochenta) días corridos después de la liquidación de los fondos del aporte si el aporte fue ingresado y liquidado a partir del 21/04/25»
- **e3 Condicion** «Plazo mínimo 2 años — aporte 02/10/20 a 20/04/25» — La repatriación debe tener lugar como mínimo 2 años después de su liquidación si el aporte fue ingresado y liquidado entre el 02/10/20 y el 20/04/25 · umbral: ['como mínimo 2 (dos) años'] · tramo: «la repatriación tenga lugar como mínimo 2 (dos) años después de su liquidación si el aporte fue ingresado y liquidado entre el 02/10/20 y el 20/04/25»
- R: e2 Condicion «Plazo mínimo 180 días — aporte desde 21/04/25» —condicion_de→ e1 Operacion «Repatriación inversión directa no residentes»
- R: e3 Condicion «Plazo mínimo 2 años — aporte 02/10/20 a 20/04/25» —condicion_de→ e1 Operacion «Repatriación inversión directa no residentes»
- Omisión `meta_normativo`: «excepto para las operaciones de» — Anuncio de lista de excepciones; el contenido de las excepciones está en otros puntos (3.13.1.1 a 3.13.1.6 y posteriores), no en esta unidad

- **Lectura:** Operacion y Condicion; sin Excepcion

## `ext::3.13.1.8` (ítem) — propuesta: **no_cumple**

> *heredado:* Sección 3. Disposiciones específicas para los egresos por el mercado de cambios
> *heredado:* Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–, adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables.
> *heredado:* 3.13. Repatriaciones de inversiones directas y otras compras de moneda extranjera por parte de no
> *heredado:* residentes
> *heredado:* 3.13.1. El acceso al mercado de cambios para la repatriación de inversiones de no
> *heredado:* residentes y otras compras de moneda extranjera por parte de clientes no residentes requerirá la conformidad previa del BCRA, excepto para las operaciones de:
> *heredado:* Si una repatriación de una inversión directa de no residentes consiste en una reducción de capital y/o devolución de aportes irrevocables realizadas por la empresa local, adicionalmente a los requisitos previstos en cada caso, la entidad deberá contar con la documentación que demuestre que se han cumplimentado los mecanismos legales previstos y haber verificado que se encuentra declarada, en caso de corresponder, en la última presentación vencida del "Relevamiento de activos y pasivos externos" el pasivo en pesos con el exterior generado a partir de la fecha de la no aceptación del aporte irrevocable o de la reducción de capital según corresponda.
> *propio:* 3.13.1.8. Repatriaciones de inversiones directas de no residentes hasta el monto de los aportes de inversión ingresados y liquidados por el mercado de cambios a partir del 16/11/20 en la medida que se cumplan la totalidad de las siguientes condiciones: i) el destino de los fondos haya sido la financiación de proyectos enmarcados en el "Plan de promoción de la producción del gas natural argentino – Esquema de oferta y demanda 2020-2024" establecido el artículo 2° del Decreto 892/20; ii) la entidad cuente con documentación que acredite el efectivo ingreso de la inversión directa en la empresa residente; y iii) el acceso se produce no antes de los 2 (dos) años corridos desde la fecha de liquidación en el mercado de cambios de la operación que permite el encuadre en el presente punto.

- Estado final: `aceptado_con_residuales`; rechazos: 0
- **e1 Operacion** «Repatriación inversión directa no residentes» — Repatriación de inversiones directas de no residentes hasta el monto de los aportes de inversión ingresados y liquidados por el mercado de cambios a partir del 16/11/20, sujeta al cumplimiento de las condiciones especificadas. · props: `{"tipo": "Repatriación de inversión directa"}` · tramo: «Repatriaciones de inversiones directas de no residentes hasta el monto de los aportes de inversión ingresados y liquidados por el mercado de cambios a partir del 16/11/20»
- **e2 Condicion** «Destino fondos Plan promoción gas natural» — El destino de los fondos debe haber sido la financiación de proyectos enmarcados en el Plan de promoción de la producción del gas natural argentino – Esquema de oferta y demanda 2020-2024 establecido en el artículo 2° del Decreto 892/20. · tramo: «el destino de los fondos haya sido la financiación de proyectos enmarcados en el "Plan de promoción de la producción del gas natural argentino – Esquema de oferta y demanda 2020-2024" establecido el artículo 2° del Decreto 892/20»
- **e3 Condicion** «Documentación acreditativa ingreso inversión directa» — La entidad debe contar con documentación que acredite el efectivo ingreso de la inversión directa en la empresa residente. · tramo: «la entidad cuente con documentación que acredite el efectivo ingreso de la inversión directa en la empresa residente»
- **e4 Condicion** «Plazo mínimo 2 años desde liquidación» — El acceso al mercado de cambios debe producirse no antes de 2 (dos) años corridos desde la fecha de liquidación en el mercado de cambios de la operación. · umbral: ['no antes de los 2 (dos) años corridos'] · tramo: «el acceso se produce no antes de los 2 (dos) años corridos desde la fecha de liquidación en el mercado de cambios de la operación que permite el encuadre en el presente punto»
- **e5 Comunicacion** «Decreto 892/20» —  · props: `{"codigo": "Decreto 892/20", "tipo": "externa"}` · tramo: «Decreto 892/20»
- R: e2 Condicion «Destino fondos Plan promoción gas natural» —condicion_de→ e1 Operacion «Repatriación inversión directa no residentes»
- R: e3 Condicion «Documentación acreditativa ingreso inversión directa» —condicion_de→ e1 Operacion «Repatriación inversión directa no residentes»
- R: e4 Condicion «Plazo mínimo 2 años desde liquidación» —condicion_de→ e1 Operacion «Repatriación inversión directa no residentes»
- R: to TextoOrdenado «Texto Ordenado Exterior Cambios» —referencia→ e5 Comunicacion «Decreto 892/20»
- Omisión `meta_normativo`: «en la medida que se cumplan la totalidad de las siguientes condiciones» — Enunciado que predica sobre la aplicación de la norma (cuándo rige), no una conducta prescrita. El contenido normativo (las condiciones) se extrae como Condicion.

- **Lectura:** Operacion y Condicion; sin Excepcion

## `ext::3.13.1.9` (ítem) — propuesta: **no_cumple**

> *heredado:* Sección 3. Disposiciones específicas para los egresos por el mercado de cambios
> *heredado:* Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–, adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables.
> *heredado:* 3.13. Repatriaciones de inversiones directas y otras compras de moneda extranjera por parte de no
> *heredado:* residentes
> *heredado:* 3.13.1. El acceso al mercado de cambios para la repatriación de inversiones de no
> *heredado:* residentes y otras compras de moneda extranjera por parte de clientes no residentes requerirá la conformidad previa del BCRA, excepto para las operaciones de:
> *heredado:* Si una repatriación de una inversión directa de no residentes consiste en una reducción de capital y/o devolución de aportes irrevocables realizadas por la empresa local, adicionalmente a los requisitos previstos en cada caso, la entidad deberá contar con la documentación que demuestre que se han cumplimentado los mecanismos legales previstos y haber verificado que se encuentra declarada, en caso de corresponder, en la última presentación vencida del "Relevamiento de activos y pasivos externos" el pasivo en pesos con el exterior generado a partir de la fecha de la no aceptación del aporte irrevocable o de la reducción de capital según corresponda.
> *propio:* 3.13.1.9. Repatriaciones de inversiones directas de no residentes en empresas que no sean controlantes de entidades financieras locales, en la medida que cuente con una "Certificación por los regímenes de acceso a divisas para la producción incremental de petróleo y/o gas natural (Decreto 277/22)", emitida en el marco de lo dispuesto en el punto 3.17., por el equivalente del monto a repatriar.

- Estado final: `completo_ok_directo`; rechazos: 1
- **e1 Operacion** «Repatriación inversión directa no residentes» — Repatriación de inversiones directas de no residentes en empresas que no sean controlantes de entidades financieras locales, condicionada a contar con Certificación por los regímenes de acceso a divisas para la producción incremental de petróleo y/o gas natural (Decreto 277/22), emitida en el marco del punto 3.17., por el equivalente del monto a repatriar. · props: `{"tipo": "Repatriación de inversión directa"}` · tramo: «Repatriaciones de inversiones directas de no residentes en empresas que no sean controlantes de entidades financieras locales»
- **e2 Condicion** «Certificación Decreto 277/22 para repatriación» — Contar con Certificación por los regímenes de acceso a divisas para la producción incremental de petróleo y/o gas natural (Decreto 277/22), emitida conforme al punto 3.17., por el equivalente del monto a repatriar · tramo: «en la medida que cuente con una "Certificación por los regímenes de acceso a divisas para la producción incremental de petróleo y/o gas natural (Decreto 277/22)", emitida en el marco de lo dispuesto en el punto 3.17., por el equivalente del monto a repatriar»
- **e3 Comunicacion** «Decreto 277/22» —  · props: `{"codigo": "Decreto 277/22", "tipo": "externa"}` · tramo: «Decreto 277/22»
- R: e2 Condicion «Certificación Decreto 277/22 para repatriación» —condicion_de→ e1 Operacion «Repatriación inversión directa no residentes»
- R: to TextoOrdenado «Texto Ordenado Exterior Cambios» —referencia→ e3 Comunicacion «Decreto 277/22»
- Omisión `relacion_sin_predicado`: «emitida en el marco de lo dispuesto en el punto 3.17.» — remisión a otro punto del TO; la relación entre la Condicion e2 y el punto 3.17. no tiene predicado en el schema (sería una remisión o referencia interna al TO, no un predicado de dominio-rango entre entidades del chunk)

- **Lectura:** Operacion y Condicion; sin Excepcion

## `ext::3.13.1.10` (ítem) — propuesta: **no_cumple**

> *heredado:* Sección 3. Disposiciones específicas para los egresos por el mercado de cambios
> *heredado:* Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–, adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables.
> *heredado:* 3.13. Repatriaciones de inversiones directas y otras compras de moneda extranjera por parte de no
> *heredado:* residentes
> *heredado:* 3.13.1. El acceso al mercado de cambios para la repatriación de inversiones de no
> *heredado:* residentes y otras compras de moneda extranjera por parte de clientes no residentes requerirá la conformidad previa del BCRA, excepto para las operaciones de:
> *heredado:* Si una repatriación de una inversión directa de no residentes consiste en una reducción de capital y/o devolución de aportes irrevocables realizadas por la empresa local, adicionalmente a los requisitos previstos en cada caso, la entidad deberá contar con la documentación que demuestre que se han cumplimentado los mecanismos legales previstos y haber verificado que se encuentra declarada, en caso de corresponder, en la última presentación vencida del "Relevamiento de activos y pasivos externos" el pasivo en pesos con el exterior generado a partir de la fecha de la no aceptación del aporte irrevocable o de la reducción de capital según corresponda.
> *propio:* 3.13.1.10. Repatriaciones de inversiones directas de no residentes en empresas a través del acceso del residente que adquirió su participación en el capital en una empresa residente en la medida que: i) el acceso se concrete en forma simultánea con la liquidación de fondos ingresados desde el exterior por endeudamientos financieros comprendidos en el punto 3.5. o fondos provenientes de un préstamo financiero en moneda extranjera otorgada por una entidad financiera local a partir de una línea de crédito de entidad financiera del exterior, que tengan una vida promedio no inferior a 4 (cuatro) años y que contemplen como mínimo 3 (tres) años de gracia para el pago de capital; ii) la empresa residente cuyo capital se transfiere quede comprendida entre los siguientes sectores: la forestoindustria, el turismo, la infraestructura, la minería, la tecnología, la siderurgia, la energía, el petróleo y el gas; y iii)la operación implique la transferencia de, como mínimo, el 10% (diez por ciento) del capital de la empresa residente. En caso de que al momento de concretarse el acceso el cliente no cuente con la documentación que demuestre que ha tomado posesión de la participación en el capital que se abona, deberá realizar una declaración jurada en la que se compromete a presentarla dentro de los 60 (sesenta) días corridos de concretado el acceso al mercado de cambios.

- Estado final: `cola_humana_veredicto_inutilizable`; rechazos: 0
- **e1 Operacion** «Repatriación inversión directa no residente» — Repatriación de inversiones directas de no residentes en empresas a través del acceso del residente que adquirió su participación en el capital en una empresa residente, sujeta a condiciones de simultaneidad con liquidación de fondos, sectores específicos y transferencia mínima de capital. · props: `{"tipo": "Repatriación de inversión directa"}` · tramo: «Repatriaciones de inversiones directas de no residentes en empresas a través del acceso del residente que adquirió su participación en el capital en una empresa residente»
- **e2 Condicion** «Simultaneidad con liquidación de fondos» — El acceso debe concretarse en forma simultánea con la liquidación de fondos ingresados desde el exterior por endeudamientos financieros o préstamos financieros en moneda extranjera con vida promedio no inferior a 4 años y mínimo 3 años de gracia. · umbral: ['una vida promedio no inferior a 4 (cuatro) años', 'como mínimo 3 (tres) años de gracia para el pago de capital'] · tramo: «el acceso se concrete en forma simultánea con la liquidación de fondos ingresados desde el exterior por endeudamientos financieros comprendidos en el punto 3.5. o fondos provenientes de un préstamo financiero en moneda extranjera otorgada por una entidad financiera local a partir de una línea de crédito de entidad financiera del exterior, que tengan una vida promedio no inferior a 4 (cuatro) años y que contemplen como mínimo 3 (tres) años de gracia para el pago de capital»
- **e3 Condicion** «Empresa residente en sectores específicos» — La empresa residente cuyo capital se transfiere debe estar comprendida en los sectores de forestoindustria, turismo, infraestructura, minería, tecnología, siderurgia, energía, petróleo y gas. · tramo: «la empresa residente cuyo capital se transfiere quede comprendida entre los siguientes sectores: la forestoindustria, el turismo, la infraestructura, la minería, la tecnología, la siderurgia, la energía, el petróleo y el gas»
- **e4 Condicion** «Transferencia mínima del 10% del capital» — La operación debe implicar la transferencia de como mínimo el 10% del capital de la empresa residente. · umbral: ['como mínimo, el 10% (diez por ciento) del capital'] · tramo: «la operación implique la transferencia de, como mínimo, el 10% (diez por ciento) del capital de la empresa residente»
- **e5 Obligacion** «Declaración jurada de posesión de participación» — Si el cliente no cuenta con documentación que demuestre posesión de la participación en el capital, debe realizar una declaración jurada comprometiéndose a presentarla dentro de 60 días corridos de concretado el acceso al mercado de cambios. · props: `{"tipo": "presentacion_informativa"}` · umbral: ['dentro de los 60 (sesenta) días corridos'] · tramo: «En caso de que al momento de concretarse el acceso el cliente no cuente con la documentación que demuestre que ha tomado posesión de la participación en el capital que se abona, deberá realizar una declaración jurada en la que se compromete a presentarla dentro de los 60 (sesenta) días corridos de concretado el acceso al mercado de cambios»
- **e6 Condicion** «Falta de documentación de posesión» — Cuando al momento de concretarse el acceso el cliente no cuenta con documentación que demuestre posesión de la participación en el capital. · tramo: «En caso de que al momento de concretarse el acceso el cliente no cuente con la documentación que demuestre que ha tomado posesión de la participación en el capital que se abona»
- R: e2 Condicion «Simultaneidad con liquidación de fondos» —condicion_de→ e1 Operacion «Repatriación inversión directa no residente»
- R: e3 Condicion «Empresa residente en sectores específicos» —condicion_de→ e1 Operacion «Repatriación inversión directa no residente»
- R: e4 Condicion «Transferencia mínima del 10% del capital» —condicion_de→ e1 Operacion «Repatriación inversión directa no residente»
- R: e6 Condicion «Falta de documentación de posesión» —condicion_de→ e5 Obligacion «Declaración jurada de posesión de participación»
- Omisión `meta_normativo`: «El acceso al mercado de cambios para la repatriación de inversiones de no residentes y otras compras de moneda extranjera por parte de clientes no residentes requerirá la conformidad previa del BCRA, excepto para las operaciones de:» — Enunciado de conformidad previa del BCRA que actúa como marco general del punto; el contenido específico de la operación y sus condiciones se extrae en las entidades correspondientes.
- Faltante de E3 pendiente (otro, alta): «El acceso al mercado de cambios para la repatriación de inversiones de no residentes y otras compras de moneda extranjera por parte de clientes no residentes requerirá la conformidad previa del BCRA, excepto para las operaciones de:»

- **Lectura:** Operacion, Condicion y Obligacion; sin Excepcion

## `ext::3.13.1.11` (ítem) — propuesta: **no_cumple**

> *heredado:* Sección 3. Disposiciones específicas para los egresos por el mercado de cambios
> *heredado:* Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–, adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables.
> *heredado:* 3.13. Repatriaciones de inversiones directas y otras compras de moneda extranjera por parte de no
> *heredado:* residentes
> *heredado:* 3.13.1. El acceso al mercado de cambios para la repatriación de inversiones de no
> *heredado:* residentes y otras compras de moneda extranjera por parte de clientes no residentes requerirá la conformidad previa del BCRA, excepto para las operaciones de:
> *heredado:* Si una repatriación de una inversión directa de no residentes consiste en una reducción de capital y/o devolución de aportes irrevocables realizadas por la empresa local, adicionalmente a los requisitos previstos en cada caso, la entidad deberá contar con la documentación que demuestre que se han cumplimentado los mecanismos legales previstos y haber verificado que se encuentra declarada, en caso de corresponder, en la última presentación vencida del "Relevamiento de activos y pasivos externos" el pasivo en pesos con el exterior generado a partir de la fecha de la no aceptación del aporte irrevocable o de la reducción de capital según corresponda.
> *propio:* 3.13.1.11. Repatriaciones de aportes de inversión directa de no residentes en una Vehículo de Proyecto Único (VPU) adherido al Régimen de Incentivo para Grandes Inversiones (RIGI) encuadradas en el punto 14.2.3.

- Estado final: `completo_ok_directo`; rechazos: 0
- **e1 Operacion** «Repatriación aportes inversión directa VPU-RIGI» — Repatriaciones de aportes de inversión directa de no residentes en una VPU adherida al RIGI, encuadradas en el punto 14.2.3 · props: `{"tipo": "repatriación de inversión directa"}` · tramo: «Repatriaciones de aportes de inversión directa de no residentes en una Vehículo de Proyecto Único (VPU) adherido al Régimen de Incentivo para Grandes Inversiones (RIGI)»
- **e2 Condicion** «Encuadramiento en punto 14.2.3» — La operación debe estar encuadrada en el punto 14.2.3 · tramo: «encuadradas en el punto 14.2.3»
- R: e2 Condicion «Encuadramiento en punto 14.2.3» —condicion_de→ e1 Operacion «Repatriación aportes inversión directa VPU-RIGI»
- Omisión `relacion_sin_predicado`: «Repatriaciones de aportes de inversión directa de no residentes en una Vehículo de Proyecto Único (VPU) adherido al Régimen de Incentivo para Grandes Inversiones (RIGI)» — Relación entre la operación y el sujeto (no residentes) sin predicado específico; el sujeto está implícito en la descripción de la operación pero no se emite como aplica_a porque el texto no lo nombra explícitamente en este punto

- **Lectura:** Operacion y Condicion; sin Excepcion

## `ext::3.13.1.12` (ítem) — propuesta: **no_cumple**

> *heredado:* Sección 3. Disposiciones específicas para los egresos por el mercado de cambios
> *heredado:* Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–, adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables.
> *heredado:* 3.13. Repatriaciones de inversiones directas y otras compras de moneda extranjera por parte de no
> *heredado:* residentes
> *heredado:* 3.13.1. El acceso al mercado de cambios para la repatriación de inversiones de no
> *heredado:* residentes y otras compras de moneda extranjera por parte de clientes no residentes requerirá la conformidad previa del BCRA, excepto para las operaciones de:
> *heredado:* Si una repatriación de una inversión directa de no residentes consiste en una reducción de capital y/o devolución de aportes irrevocables realizadas por la empresa local, adicionalmente a los requisitos previstos en cada caso, la entidad deberá contar con la documentación que demuestre que se han cumplimentado los mecanismos legales previstos y haber verificado que se encuentra declarada, en caso de corresponder, en la última presentación vencida del "Relevamiento de activos y pasivos externos" el pasivo en pesos con el exterior generado a partir de la fecha de la no aceptación del aporte irrevocable o de la reducción de capital según corresponda.
> *propio:* 3.13.1.12. Repatriación por parte de no residentes de servicios de capital, rentas y el producido de las ventas de inversiones de portafolio en instrumentos con cotizaciones en mercados locales autorizados por la Comisión Nacional de Valores, fondos comunes de inversión sin cotización directa conformados por esos instrumentos y/o los depósitos a la vista o a plazo en entidades financieras locales, siempre que: i) se cuente con la certificación de una entidad financiera local que acredite que la inversión fue constituida con fondos ingresados y liquidados en el mercado local de cambios a partir del 21/04/25. El requisito de liquidación se considerará cumplimentado cuando el cliente no residente haya aplicado moneda extranjera en forma directa a partir del 23/05/25 a la suscripción primaria de títulos de deuda emitidos por el Tesoro Nacional. ii) se cuente con la documentación que demuestre que el monto por el cual se accede al mercado no supera los servicios cobrados y/o el monto efectivamente recibido por la venta de la inversión realizada. En el caso que el cobro de los servicios o venta de la inversión sea percibido en moneda extranjera la repatriación podrá concretarse por hasta el equivalente de ese monto.

- Estado final: `aceptado_con_residuales`; rechazos: 1
- **e1 Operacion** «Repatriación de servicios de capital, rentas y ventas de inversiones de portafolio» — Repatriación por parte de no residentes de servicios de capital, rentas y el producido de las ventas de inversiones de portafolio en instrumentos con cotizaciones en mercados locales autorizados por la Comisión Nacional de Valores, fondos comunes de inversión sin cotización directa conformados por esos instrumentos y/o los depósitos a la vista o a plazo en entidades financieras locales · props: `{"tipo": "repatriación de inversiones"}` · tramo: «Repatriación por parte de no residentes de servicios de capital, rentas y el producido de las ventas de inversiones de portafolio en instrumentos con cotizaciones en mercados locales autorizados por la Comisión Nacional de Valores, fondos comunes de inversión sin cotización directa conformados por esos instrumentos y/o los depósitos a la vista o a plazo en entidades financieras locales»
- **e2 Condicion** «Certificación de entidad financiera local sobre fondos ingresados» — Se debe contar con la certificación de una entidad financiera local que acredite que la inversión fue constituida con fondos ingresados y liquidados en el mercado local de cambios a partir del 21/04/25 · umbral: ['a partir del 21/04/25'] · tramo: «se cuente con la certificación de una entidad financiera local que acredite que la inversión fue constituida con fondos ingresados y liquidados en el mercado local de cambios a partir del 21/04/25»
- **e3 Condicion** «Liquidación mediante aplicación directa de moneda extranjera a suscripción primaria» — El requisito de liquidación se considerará cumplimentado cuando el cliente no residente haya aplicado moneda extranjera en forma directa a partir del 23/05/25 a la suscripción primaria de títulos de deuda emitidos por el Tesoro Nacional · umbral: ['a partir del 23/05/25'] · tramo: «El requisito de liquidación se considerará cumplimentado cuando el cliente no residente haya aplicado moneda extranjera en forma directa a partir del 23/05/25 a la suscripción primaria de títulos de deuda emitidos por el Tesoro Nacional»
- **e4 Condicion** «Documentación que demuestre que el monto no supera servicios cobrados o venta» — Se debe contar con la documentación que demuestre que el monto por el cual se accede al mercado no supera los servicios cobrados y/o el monto efectivamente recibido por la venta de la inversión realizada · tramo: «se cuente con la documentación que demuestre que el monto por el cual se accede al mercado no supera los servicios cobrados y/o el monto efectivamente recibido por la venta de la inversión realizada»
- **e5 Excepcion** «Excepción cuando cobro o venta percibido en moneda extranjera» — Cuando el cobro de los servicios o venta de la inversión sea percibido en moneda extranjera, la repatriación podrá concretarse por hasta el equivalente de ese monto · umbral: ['por hasta el equivalente de ese monto'] · tramo: «En el caso que el cobro de los servicios o venta de la inversión sea percibido en moneda extranjera la repatriación podrá concretarse por hasta el equivalente de ese monto»
- R: e2 Condicion «Certificación de entidad financiera local sobre fondos ingresados» —condicion_de→ e1 Operacion «Repatriación de servicios de capital, rentas y ventas de inversiones de portafolio»
- R: e3 Condicion «Liquidación mediante aplicación directa de moneda extranjera a suscripción primaria» —condicion_de→ e1 Operacion «Repatriación de servicios de capital, rentas y ventas de inversiones de portafolio»
- R: e4 Condicion «Documentación que demuestre que el monto no supera servicios cobrados o venta» —condicion_de→ e1 Operacion «Repatriación de servicios de capital, rentas y ventas de inversiones de portafolio»
- Omisión `meta_normativo`: «El requisito de liquidación se considerará cumplimentado cuando» — 

- **Lectura:** la Excepcion es de otra cosa (cobro en moneda extranjera); sin la del miembro

## `ext::3.13.1.13` (ítem) — propuesta: **no_cumple**

> *heredado:* Sección 3. Disposiciones específicas para los egresos por el mercado de cambios
> *heredado:* Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–, adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables.
> *heredado:* 3.13. Repatriaciones de inversiones directas y otras compras de moneda extranjera por parte de no
> *heredado:* residentes
> *heredado:* 3.13.1. El acceso al mercado de cambios para la repatriación de inversiones de no
> *heredado:* residentes y otras compras de moneda extranjera por parte de clientes no residentes requerirá la conformidad previa del BCRA, excepto para las operaciones de:
> *heredado:* Si una repatriación de una inversión directa de no residentes consiste en una reducción de capital y/o devolución de aportes irrevocables realizadas por la empresa local, adicionalmente a los requisitos previstos en cada caso, la entidad deberá contar con la documentación que demuestre que se han cumplimentado los mecanismos legales previstos y haber verificado que se encuentra declarada, en caso de corresponder, en la última presentación vencida del "Relevamiento de activos y pasivos externos" el pasivo en pesos con el exterior generado a partir de la fecha de la no aceptación del aporte irrevocable o de la reducción de capital según corresponda.
> *propio:* 3.13.1.13. Repatriaciones de inversiones de portafolio de no residentes originadas en utilidades y dividendos cobrados en el país desde el 01/09/19, a partir de la distribución determinada por la asamblea de accionistas por balances cerrados y auditados, en la medida que la operación se concrete mediante la realización de un canje y/o arbitraje con fondos depositados en una cuenta local y originados en cobros en moneda extranjera de capital o intereses de los bonos BOPREAL.

- Estado final: `completo_ok_directo`; rechazos: 0
- **e1 Operacion** «Repatriación inversión portafolio no residentes» — Repatriación de inversiones de portafolio de no residentes originadas en utilidades y dividendos cobrados en el país desde el 01/09/19, a partir de la distribución determinada por la asamblea de accionistas por balances cerrados y auditados, mediante canje y/o arbitraje con fondos depositados en una cuenta local y originados en cobros en moneda extranjera de capital o intereses de los bonos BOPREAL · props: `{"tipo": "repatriación de inversión de portafolio"}` · tramo: «Repatriaciones de inversiones de portafolio de no residentes originadas en utilidades y dividendos cobrados en el país desde el 01/09/19, a partir de la distribución determinada por la asamblea de accionistas por balances cerrados y auditados, en la medida que la operación se concrete mediante la realización de un canje y/o arbitraje con fondos depositados en una cuenta local y originados en cobros en moneda extranjera de capital o intereses de los bonos BOPREAL»
- **e2 Condicion** «Distribución determinada por asamblea de accionistas» — La distribución debe ser determinada por la asamblea de accionistas por balances cerrados y auditados · tramo: «a partir de la distribución determinada por la asamblea de accionistas por balances cerrados y auditados»
- **e3 Condicion** «Operación mediante canje y/o arbitraje» — La operación debe concretarse mediante canje y/o arbitraje con fondos depositados en una cuenta local y originados en cobros en moneda extranjera de capital o intereses de los bonos BOPREAL · tramo: «en la medida que la operación se concrete mediante la realización de un canje y/o arbitraje con fondos depositados en una cuenta local y originados en cobros en moneda extranjera de capital o intereses de los bonos BOPREAL»
- **e4 Condicion** «Cobros desde 01/09/19» — Los dividendos y utilidades deben haber sido cobrados en el país desde el 01/09/19 · umbral: ['desde el 01/09/19'] · tramo: «cobrados en el país desde el 01/09/19»
- R: e2 Condicion «Distribución determinada por asamblea de accionistas» —condicion_de→ e1 Operacion «Repatriación inversión portafolio no residentes»
- R: e3 Condicion «Operación mediante canje y/o arbitraje» —condicion_de→ e1 Operacion «Repatriación inversión portafolio no residentes»
- R: e4 Condicion «Cobros desde 01/09/19» —condicion_de→ e1 Operacion «Repatriación inversión portafolio no residentes»
- Omisión `meta_normativo`: «Repatriaciones de inversiones de portafolio de no residentes originadas» — Título del punto que anuncia el contenido sin prescribir conducta; el contenido normativo está en el cuerpo del punto

- **Lectura:** Operacion y Condicion; sin Excepcion

# Lista `ext::3.6.1` (b1)

## `ext::3.6.1::intro` (encabezado) — propuesta: **no_cumple**

> *heredado:* Sección 3. Disposiciones específicas para los egresos por el mercado de cambios
> *heredado:* 3.6. Pagos de títulos de deuda u otros valores representativos de deuda denominados y
> *heredado:* 3.6.1. Se prohíbe el acceso al mercado de cambios para el pago de deudas y otras
> *propio:* obligaciones en moneda extranjera entre residentes concertadas a partir del 01/09/19, excepto para la cancelación en el país a partir de su vencimiento de capital e intereses de:

- Estado final: `completo_ok_directo`; rechazos: 0
- **e1 Restriccion** «Prohibición acceso mercado cambios — deudas entre residentes» — Se prohíbe el acceso al mercado de cambios para el pago de deudas y otras obligaciones en moneda extranjera entre residentes concertadas a partir del 01/09/19 · props: `{"tipo": "prohibicion"}` · tramo: «Se prohíbe el acceso al mercado de cambios para el pago de deudas y otras obligaciones en moneda extranjera entre residentes concertadas a partir del 01/09/19»
- **e2 Excepcion** «Excepción cancelación capital e intereses — vencimiento» — Queda exceptuada la prohibición de acceso al mercado de cambios para la cancelación en el país de capital e intereses a partir de su vencimiento · umbral: ['a partir de su vencimiento'] · tramo: «excepto para la cancelación en el país a partir de su vencimiento de capital e intereses»
- **e3 Condicion** «Condición concertación anterior a 01/09/19» — La prohibición se aplica a obligaciones concertadas a partir del 01/09/19 · umbral: ['a partir del 01/09/19'] · tramo: «concertadas a partir del 01/09/19»
- R: e2 Excepcion «Excepción cancelación capital e intereses — vencimiento» —exceptua→ e1 Restriccion «Prohibición acceso mercado cambios — deudas entre residentes»
- R: e3 Condicion «Condición concertación anterior a 01/09/19» —condicion_de→ e1 Restriccion «Prohibición acceso mercado cambios — deudas entre residentes»
- Omisión `fuera_de_tipos`: «de:» — Anuncio de lista de deudas específicas que continúa en los ítems del punto 3.6.1; el contenido de esa lista no está en esta unidad (bloque intro), sino en los ítems siguientes

- **Lectura:** Restriccion de la prohibición, Excepcion y Condicion; no hay Definicion de la clase

## `ext::3.6.1.1` (ítem) — propuesta: **cumple**

> *heredado:* Sección 3. Disposiciones específicas para los egresos por el mercado de cambios
> *heredado:* Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–, adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables.
> *heredado:* 3.6. Pagos de títulos de deuda u otros valores representativos de deuda denominados y
> *heredado:* pagaderos en moneda extranjera en el país y obligaciones en moneda extranjera entre residentes.
> *heredado:* 3.6.1. Se prohíbe el acceso al mercado de cambios para el pago de deudas y otras
> *heredado:* obligaciones en moneda extranjera entre residentes concertadas a partir del 01/09/19, excepto para la cancelación en el país a partir de su vencimiento de capital e intereses de:
> *propio:* 3.6.1.1. las financiaciones en moneda extranjera otorgadas por entidades financieras locales, incluyendo los pagos por los consumos en moneda extranjera efectuados mediante tarjetas de crédito o de compra, excepto la cancelación de giros en descubierto en cuentas corrientes en dólares estadounidenses que sólo podrá efectuarse con fondos en esa moneda de libre disponibilidad del cliente.

- Estado final: `cola_humana`; rechazos: 1
- **e1 Restriccion** «Prohibición acceso mercado cambios — deudas entre residentes» — Se prohíbe el acceso al mercado de cambios para el pago de deudas y otras obligaciones en moneda extranjera entre residentes concertadas a partir del 01/09/19 · props: `{"tipo": "prohibicion"}` · umbral: ['a partir del 01/09/19'] · tramo: «Se prohíbe el acceso al mercado de cambios para el pago de deudas y otras obligaciones en moneda extranjera entre residentes concertadas a partir del 01/09/19»
- **e2 Excepcion** «Cancelación en país — financiaciones entidades financieras» — Excepción a la prohibición de acceso al mercado de cambios: se permite la cancelación en el país de financiaciones en moneda extranjera otorgadas por entidades financieras locales, incluyendo pagos por consumos en moneda extranjera efectuados mediante tarjetas de crédito o de compra · tramo: «las financiaciones en moneda extranjera otorgadas por entidades financieras locales, incluyendo los pagos por los consumos en moneda extranjera efectuados mediante tarjetas de crédito o de compra»
- **e3 Restriccion** «Prohibición cancelación giros descubierto — fondos en moneda extranjera» — Se exceptúa de la excepción anterior la cancelación de giros en descubierto en cuentas corrientes en dólares estadounidenses, que solo podrá efectuarse con fondos en esa moneda de libre disponibilidad del cliente · props: `{"tipo": "prohibicion"}` · tramo: «excepto la cancelación de giros en descubierto en cuentas corrientes en dólares estadounidenses que sólo podrá efectuarse con fondos en esa moneda de libre disponibilidad del cliente»
- R: e2 Excepcion «Cancelación en país — financiaciones entidades financieras» —exceptua→ e1 Restriccion «Prohibición acceso mercado cambios — deudas entre residentes»
- Omisión `fuera_de_tipos`: «excepto para la cancelación en el país a partir de su vencimiento de capital e intereses de:» — Enunciado introductorio que anuncia la lista de excepciones; no es una norma autónoma sino un encabezado que se compone con los ítems. El contenido normativo se extrae en cada ítem como excepción compuesta.
- Faltante de E3 pendiente (modalidad_perdida, alta): «Se prohíbe el acceso al mercado de cambios para el pago de deudas y otras»
- Faltante de E3 pendiente (otro, media): «las financiaciones en moneda extranjera otorgadas por entidades financieras locales, incluyendo los pagos por los consumos en moneda extranjera efectuados mediante tarjetas de crédito o de compra»

- **Lectura:** Excepcion por el miembro (financiaciones de entidades locales) con la norma («Excepción a la prohibición…»), exceptua hacia la Restriccion del mismo ítem

## `ext::3.6.1.2` (ítem) — propuesta: **cumple**

> *heredado:* Sección 3. Disposiciones específicas para los egresos por el mercado de cambios
> *heredado:* Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–, adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables.
> *heredado:* 3.6. Pagos de títulos de deuda u otros valores representativos de deuda denominados y
> *heredado:* pagaderos en moneda extranjera en el país y obligaciones en moneda extranjera entre residentes.
> *heredado:* 3.6.1. Se prohíbe el acceso al mercado de cambios para el pago de deudas y otras
> *heredado:* obligaciones en moneda extranjera entre residentes concertadas a partir del 01/09/19, excepto para la cancelación en el país a partir de su vencimiento de capital e intereses de:
> *propio:* 3.6.1.2. las emisiones de títulos de deuda realizadas a partir del 01/09/19 con el objeto de refinanciar deudas comprendidas en el punto 3.6.2. y conlleven un incremento de la vida promedio de las obligaciones.

- Estado final: `aceptado_tras_reintento`; rechazos: 0
- **e1 Restriccion** «Prohibición acceso mercado cambios — deudas residentes» — Se prohíbe el acceso al mercado de cambios para el pago de deudas y otras obligaciones en moneda extranjera entre residentes concertadas a partir del 01/09/19 · props: `{"tipo": "prohibicion"}` · umbral: ['a partir del 01/09/19'] · tramo: «Se prohíbe el acceso al mercado de cambios para el pago de deudas y otras obligaciones en moneda extranjera entre residentes concertadas a partir del 01/09/19»
- **e2 Excepcion** «Excepción — cancelación títulos deuda refinanciamiento» — Quedan exceptuadas de la prohibición las emisiones de títulos de deuda realizadas a partir del 01/09/19 con el objeto de refinanciar deudas comprendidas en el punto 3.6.2. y que conlleven un incremento de la vida promedio de las obligaciones · umbral: ['a partir del 01/09/19'] · tramo: «las emisiones de títulos de deuda realizadas a partir del 01/09/19 con el objeto de refinanciar deudas comprendidas en el punto 3.6.2. y conlleven un incremento de la vida promedio de las obligaciones»
- **e3 Operacion** «Cancelación en el país — títulos deuda vencidos» — Cancelación en el país a partir de su vencimiento de capital e intereses de títulos de deuda · props: `{"tipo": "pago de títulos de deuda"}` · tramo: «cancelación en el país a partir de su vencimiento de capital e intereses»
- **e4 Condicion** «Condición — refinanciamiento deudas punto 3.6.2» — Las emisiones tienen por objeto refinanciar deudas comprendidas en el punto 3.6.2. · tramo: «con el objeto de refinanciar deudas comprendidas en el punto 3.6.2.»
- **e5 Condicion** «Condición — incremento vida promedio obligaciones» — Las emisiones conllevan un incremento de la vida promedio de las obligaciones · tramo: «conlleven un incremento de la vida promedio de las obligaciones»
- R: e2 Excepcion «Excepción — cancelación títulos deuda refinanciamiento» —exceptua→ e1 Restriccion «Prohibición acceso mercado cambios — deudas residentes»
- R: e4 Condicion «Condición — refinanciamiento deudas punto 3.6.2» —condicion_de→ e2 Excepcion «Excepción — cancelación títulos deuda refinanciamiento»
- R: e5 Condicion «Condición — incremento vida promedio obligaciones» —condicion_de→ e2 Excepcion «Excepción — cancelación títulos deuda refinanciamiento»
- R: e1 Restriccion «Prohibición acceso mercado cambios — deudas residentes» —prohibe→ e3 Operacion «Cancelación en el país — títulos deuda vencidos» [coherente]

- **Lectura:** Excepcion por el miembro (emisiones para refinanciar), con la norma

## `ext::3.6.1.3` (ítem) — propuesta: **no_cumple**

> *heredado:* Sección 3. Disposiciones específicas para los egresos por el mercado de cambios
> *heredado:* Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–, adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables.
> *heredado:* 3.6. Pagos de títulos de deuda u otros valores representativos de deuda denominados y
> *heredado:* pagaderos en moneda extranjera en el país y obligaciones en moneda extranjera entre residentes.
> *heredado:* 3.6.1. Se prohíbe el acceso al mercado de cambios para el pago de deudas y otras
> *heredado:* obligaciones en moneda extranjera entre residentes concertadas a partir del 01/09/19, excepto para la cancelación en el país a partir de su vencimiento de capital e intereses de:
> *propio:* 3.6.1.3. las emisiones realizadas a partir del 29/11/19 de títulos de deuda con registro público en el país no comprendidas en el punto 3.5., que estén denominadas y suscriptas en moneda extranjera y cuyos servicios de capital e intereses sean pagaderos en moneda extranjera, en la medida que la totalidad de los fondos obtenidos hayan sido liquidados en el mercado de cambios. En caso de tratarse de títulos de deuda emitidos por entidades financieras locales a través de operaciones concertadas a partir del 26/05/25, el pago debe tener lugar una vez transcurrido, como mínimo, 12 (doce) meses desde su fecha de emisión.

- Estado final: `aceptado_con_residuales`; rechazos: 0
- **e1 Operacion** «Pago de capital e intereses de títulos de deuda» — Pago en el país de capital e intereses de emisiones de títulos de deuda realizadas a partir del 29/11/19, con registro público, no comprendidas en punto 3.5., denominadas y suscriptas en moneda extranjera, con servicios pagaderos en moneda extranjera, en la medida que la totalidad de los fondos obtenidos hayan sido liquidados en el mercado de cambios · props: `{"tipo": "pago de capital e intereses"}` · tramo: «la cancelación en el país a partir de su vencimiento de capital e intereses de: las emisiones realizadas a partir del 29/11/19 de títulos de deuda con registro público en el país no comprendidas en el punto 3.5., que estén denominadas y suscriptas en moneda extranjera y cuyos servicios de capital e intereses sean pagaderos en moneda extranjera»
- **e2 Condicion** «Fondos obtenidos liquidados en mercado de cambios» — La totalidad de los fondos obtenidos de la emisión deben haber sido liquidados en el mercado de cambios · umbral: ['la totalidad de los fondos obtenidos'] · tramo: «en la medida que la totalidad de los fondos obtenidos hayan sido liquidados en el mercado de cambios»
- **e3 Condicion** «Plazo mínimo 12 meses desde emisión — títulos de entidades financieras» — Para títulos de deuda emitidos por entidades financieras locales a través de operaciones concertadas a partir del 26/05/25, el pago debe ocurrir después de transcurridos al menos 12 meses desde la emisión · umbral: ['como mínimo, 12 (doce) meses desde su fecha de emisión'] · tramo: «En caso de tratarse de títulos de deuda emitidos por entidades financieras locales a través de operaciones concertadas a partir del 26/05/25, el pago debe tener lugar una vez transcurrido, como mínimo, 12 (doce) meses desde su fecha de emisión»
- **e4 Restriccion** «Prohibición acceso mercado de cambios — deudas entre residentes» — Se prohíbe el acceso al mercado de cambios para el pago de deudas y otras obligaciones en moneda extranjera entre residentes concertadas a partir del 01/09/19 · props: `{"tipo": "prohibicion"}` · tramo: «Se prohíbe el acceso al mercado de cambios para el pago de deudas y otras obligaciones en moneda extranjera entre residentes concertadas a partir del 01/09/19»
- R: e2 Condicion «Fondos obtenidos liquidados en mercado de cambios» —condicion_de→ e1 Operacion «Pago de capital e intereses de títulos de deuda»
- R: e3 Condicion «Plazo mínimo 12 meses desde emisión — títulos de entidades financieras» —condicion_de→ e1 Operacion «Pago de capital e intereses de títulos de deuda»
- Omisión `relacion_sin_predicado`: «Se prohíbe el acceso al mercado de cambios para el pago de deudas y otras obligaciones en moneda extranjera entre residentes concertadas a partir del 01/09/19, excepto para la cancelación en el país a partir de su vencimiento de capital e intereses de: las emisiones realizadas a partir del 29/11/19» — exceptua

- **Lectura:** Operacion, Condicion y la Restriccion del encabezado copiada; sin Excepcion

## `ext::3.6.1.4` (ítem) — propuesta: **cumple**

> *heredado:* Sección 3. Disposiciones específicas para los egresos por el mercado de cambios
> *heredado:* Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–, adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables.
> *heredado:* 3.6. Pagos de títulos de deuda u otros valores representativos de deuda denominados y
> *heredado:* pagaderos en moneda extranjera en el país y obligaciones en moneda extranjera entre residentes.
> *heredado:* 3.6.1. Se prohíbe el acceso al mercado de cambios para el pago de deudas y otras
> *heredado:* obligaciones en moneda extranjera entre residentes concertadas a partir del 01/09/19, excepto para la cancelación en el país a partir de su vencimiento de capital e intereses de:
> *propio:* 3.6.1.4. pagarés con oferta pública emitidos en el marco de la Resolución General 1.003/24 de la Comisión Nacional de Valores (CNV) y concordantes, denominados y suscriptos en moneda extranjera y cuyos servicios de capital e intereses sean pagaderos en moneda extranjera en el país, en la medida que la totalidad de los fondos obtenidos hayan sido liquidados en el mercado de cambios.

- Estado final: `aceptado_con_residuales`; rechazos: 0
- **e1 Operacion** «Pago de pagarés con oferta pública en moneda extranjera» — Pago de capital e intereses de pagarés con oferta pública emitidos conforme a la Resolución General 1.003/24 de la CNV, denominados y suscriptos en moneda extranjera, pagaderos en moneda extranjera en el país · props: `{"tipo": "pago de títulos de deuda"}` · tramo: «pagarés con oferta pública emitidos en el marco de la Resolución General 1.003/24 de la Comisión Nacional de Valores (CNV) y concordantes, denominados y suscriptos en moneda extranjera y cuyos servicios de capital e intereses sean pagaderos en moneda extranjera en el país»
- **e2 Restriccion** «Prohibición acceso mercado cambios — deudas entre residentes» — Se prohíbe el acceso al mercado de cambios para el pago de deudas y otras obligaciones en moneda extranjera entre residentes concertadas a partir del 01/09/19, excepto para la cancelación en el país a partir de su vencimiento de capital e intereses de pagarés con oferta pública emitidos conforme a la Resolución General 1.003/24 de la CNV · props: `{"tipo": "prohibicion"}` · tramo: «Se prohíbe el acceso al mercado de cambios para el pago de deudas y otras obligaciones en moneda extranjera entre residentes concertadas a partir del 01/09/19, excepto para la cancelación en el país a partir de su vencimiento de capital e intereses de: […] pagarés con oferta pública emitidos en el marco de la Resolución General 1.003/24 de la Comisión Nacional de Valores (CNV) y concordantes, denominados y suscriptos en moneda extranjera y cuyos servicios de capital e intereses sean pagaderos en moneda extranjera en el país»
- **e3 Excepcion** «Excepción — pagarés con oferta pública conforme RG 1.003/24» — Excepción a la prohibición de acceso al mercado de cambios para el pago de deudas entre residentes: se permite la cancelación en el país a partir de su vencimiento de capital e intereses de pagarés con oferta pública emitidos conforme a la Resolución General 1.003/24 de la CNV · tramo: «excepto para la cancelación en el país a partir de su vencimiento de capital e intereses de: […] pagarés con oferta pública emitidos en el marco de la Resolución General 1.003/24 de la Comisión Nacional de Valores (CNV) y concordantes, denominados y suscriptos en moneda extranjera y cuyos servicios de capital e intereses sean pagaderos en moneda extranjera en el país»
- **e4 Condicion** «Condición — liquidación total de fondos en mercado cambios» — La excepción se aplica solo cuando la totalidad de los fondos obtenidos de la emisión hayan sido liquidados en el mercado de cambios · umbral: ['la totalidad de los fondos obtenidos'] · tramo: «en la medida que la totalidad de los fondos obtenidos hayan sido liquidados en el mercado de cambios»
- R: e3 Excepcion «Excepción — pagarés con oferta pública conforme RG 1.003/24» —exceptua→ e2 Restriccion «Prohibición acceso mercado cambios — deudas entre residentes»
- R: e4 Condicion «Condición — liquidación total de fondos en mercado cambios» —condicion_de→ e3 Excepcion «Excepción — pagarés con oferta pública conforme RG 1.003/24»
- R: e2 Restriccion «Prohibición acceso mercado cambios — deudas entre residentes» —prohibe→ e1 Operacion «Pago de pagarés con oferta pública en moneda extranjera» [coherente]
- R: e2 Restriccion «Prohibición acceso mercado cambios — deudas entre residentes» —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «las entidades», exacta)
- Omisión `meta_normativo`: «en el marco de la Resolución General 1.003/24 de la Comisión Nacional de Valores (CNV) y concordantes» — Referencia normativa que contextualiza pero no prescribe conducta propia

- **Lectura:** Excepcion por el miembro (pagarés RG 1.003/24), con la norma

## `ext::3.6.1.5` (ítem) — propuesta: **no_cumple** (dudosa)

> *heredado:* Sección 3. Disposiciones específicas para los egresos por el mercado de cambios
> *heredado:* Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–, adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables.
> *heredado:* 3.6. Pagos de títulos de deuda u otros valores representativos de deuda denominados y
> *heredado:* pagaderos en moneda extranjera en el país y obligaciones en moneda extranjera entre residentes.
> *heredado:* 3.6.1. Se prohíbe el acceso al mercado de cambios para el pago de deudas y otras
> *heredado:* obligaciones en moneda extranjera entre residentes concertadas a partir del 01/09/19, excepto para la cancelación en el país a partir de su vencimiento de capital e intereses de:
> *propio:* 3.6.1.5. valores de deuda fiduciaria emitidos por fiduciarios de fidecomisos financieros con oferta pública concretadas en concordancia con las disposiciones de la CNV en la materia, denominados y suscriptos en moneda extranjera y cuyos servicios de capital e intereses sean pagaderos en moneda extranjera en el país, en la medida que la totalidad de los fondos obtenidos hayan sido liquidados en el mercado de cambios.

- Estado final: `aceptado_con_residuales`; rechazos: 0
- **e1 Operacion** «Pago de valores de deuda fiduciaria» — Pago en el país de capital e intereses de valores de deuda fiduciaria emitidos por fiduciarios de fidecomisos financieros con oferta pública concretadas en concordancia con las disposiciones de la CNV, denominados y suscriptos en moneda extranjera, cuyos servicios de capital e intereses sean pagaderos en moneda extranjera en el país. · props: `{"tipo": "pago de títulos de deuda"}` · tramo: «pago de deudas y otras obligaciones en moneda extranjera entre residentes»
- **e2 Restriccion** «Prohibición acceso mercado cambios — deudas entre residentes» — Se prohíbe el acceso al mercado de cambios para el pago de deudas y otras obligaciones en moneda extranjera entre residentes concertadas a partir del 01/09/19. · props: `{"tipo": "prohibicion"}` · umbral: ['concertadas a partir del 01/09/19'] · tramo: «Se prohíbe el acceso al mercado de cambios para el pago de deudas y otras obligaciones en moneda extranjera entre residentes concertadas a partir del 01/09/19»
- **e3 Excepcion** «Excepción — cancelación de capital e intereses a partir del vencimiento» — Excepción a la prohibición de acceso al mercado de cambios para la cancelación en el país a partir del vencimiento de capital e intereses de valores de deuda fiduciaria emitidos por fiduciarios de fidecomisos financieros con oferta pública concretadas en concordancia con las disposiciones de la CNV, denominados y suscriptos en moneda extranjera, cuyos servicios de capital e intereses sean pagaderos en moneda extranjera en el país, siempre que la totalidad de los fondos obtenidos hayan sido liquidados en el mercado de cambios. · umbral: ['a partir de su vencimiento'] · tramo: «excepto para la cancelación en el país a partir de su vencimiento de capital e intereses de: […] valores de deuda fiduciaria emitidos por fiduciarios de fidecomisos financieros con oferta pública concretadas en concordancia con las disposiciones de la CNV en la materia, denominados y suscriptos en moneda extranjera y cuyos servicios de capital e intereses sean pagaderos en moneda extranjera en el país, en la medida que la totalidad de los fondos obtenidos hayan sido liquidados en el mercado de cambios»
- **e4 Condicion** «Condición — totalidad de fondos liquidados en mercado cambios» — La excepción se aplica en la medida que la totalidad de los fondos obtenidos hayan sido liquidados en el mercado de cambios. · tramo: «en la medida que la totalidad de los fondos obtenidos hayan sido liquidados en el mercado de cambios»
- R: e3 Excepcion «Excepción — cancelación de capital e intereses a partir del vencimiento» —exceptua→ e2 Restriccion «Prohibición acceso mercado cambios — deudas entre residentes»
- R: e4 Condicion «Condición — totalidad de fondos liquidados en mercado cambios» —condicion_de→ e3 Excepcion «Excepción — cancelación de capital e intereses a partir del vencimiento»
- R: e2 Restriccion «Prohibición acceso mercado cambios — deudas entre residentes» —prohibe→ e1 Operacion «Pago de valores de deuda fiduciaria» [coherente]
- R: e2 Restriccion «Prohibición acceso mercado cambios — deudas entre residentes» —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «las entidades», exacta)
- Omisión `meta_normativo`: «en concordancia con las disposiciones de la CNV en la materia» — Cláusula que predica sobre la conformidad con disposiciones de otra autoridad; no prescribe conducta propia del sujeto regulado.

- **Lectura:** la Excepcion es la genérica del encabezado y no nombra al miembro (valores de deuda fiduciaria), que va en la Operacion

## `ext::3.6.1.6` (ítem) — propuesta: **cumple**

> *heredado:* Sección 3. Disposiciones específicas para los egresos por el mercado de cambios
> *heredado:* Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–, adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables.
> *heredado:* 3.6. Pagos de títulos de deuda u otros valores representativos de deuda denominados y
> *heredado:* pagaderos en moneda extranjera en el país y obligaciones en moneda extranjera entre residentes.
> *heredado:* 3.6.1. Se prohíbe el acceso al mercado de cambios para el pago de deudas y otras
> *heredado:* obligaciones en moneda extranjera entre residentes concertadas a partir del 01/09/19, excepto para la cancelación en el país a partir de su vencimiento de capital e intereses de:
> *propio:* 3.6.1.6. emisiones de valores comprendidos en los puntos 3.6.1.3. a 3.6.1.5. que no generaron desembolsos por ser reestructuraciones de deudas comprendidas en esos mismos puntos, en la medida que las refinanciaciones no anticipen vencimientos respecto a la deuda original.

- Estado final: `aceptado_tras_reintento`; rechazos: 0
- **e1 Restriccion** «Prohibición acceso mercado cambios — deudas entre residentes» — Se prohíbe el acceso al mercado de cambios para el pago de deudas y otras obligaciones en moneda extranjera entre residentes concertadas a partir del 01/09/19 · props: `{"tipo": "prohibicion"}` · tramo: «Se prohíbe el acceso al mercado de cambios para el pago de deudas y otras obligaciones en moneda extranjera entre residentes concertadas a partir del 01/09/19»
- **e2 Condicion** «Deudas concertadas a partir del 01/09/19» — obligaciones concertadas a partir del 01/09/19 · umbral: ['a partir del 01/09/19'] · tramo: «concertadas a partir del 01/09/19»
- **e3 Excepcion** «Excepción — cancelación en país a partir de vencimiento» — Se exceptúa la prohibición de acceso al mercado de cambios para la cancelación en el país a partir de su vencimiento de capital e intereses · umbral: ['a partir de su vencimiento'] · tramo: «excepto para la cancelación en el país a partir de su vencimiento de capital e intereses»
- **e4 Operacion** «Reestructuración de deudas sin desembolsos» — Reestructuraciones de deudas que no generaron desembolsos, comprendidas en los puntos 3.6.1.3. a 3.6.1.5. · props: `{"tipo": "reestructuración de deuda"}` · tramo: «emisiones de valores comprendidos en los puntos 3.6.1.3. a 3.6.1.5. que no generaron desembolsos por ser reestructuraciones de deudas comprendidas en esos mismos puntos»
- **e5 Condicion** «Refinanciaciones no anticipan vencimientos» — Las refinanciaciones no anticipan vencimientos respecto a la deuda original · tramo: «en la medida que las refinanciaciones no anticipen vencimientos respecto a la deuda original»
- **e6 Excepcion** «Excepción — reestructuraciones sin desembolsos con refinanciaciones no anticipadas» — Se exceptúa la prohibición de acceso al mercado de cambios para emisiones de valores que constituyen reestructuraciones de deudas sin desembolsos, siempre que las refinanciaciones no anticipen vencimientos respecto a la deuda original · tramo: «emisiones de valores comprendidos en los puntos 3.6.1.3. a 3.6.1.5. que no generaron desembolsos por ser reestructuraciones de deudas comprendidas en esos mismos puntos, en la medida que las refinanciaciones no anticipen vencimientos respecto a la deuda original»
- R: e2 Condicion «Deudas concertadas a partir del 01/09/19» —condicion_de→ e1 Restriccion «Prohibición acceso mercado cambios — deudas entre residentes»
- R: e3 Excepcion «Excepción — cancelación en país a partir de vencimiento» —exceptua→ e1 Restriccion «Prohibición acceso mercado cambios — deudas entre residentes»
- R: e6 Excepcion «Excepción — reestructuraciones sin desembolsos con refinanciaciones no anticipadas» —exceptua→ e1 Restriccion «Prohibición acceso mercado cambios — deudas entre residentes»
- R: e5 Condicion «Refinanciaciones no anticipan vencimientos» —condicion_de→ e6 Excepcion «Excepción — reestructuraciones sin desembolsos con refinanciaciones no anticipadas»
- Omisión `relacion_sin_predicado`: «emisiones de valores comprendidos en los puntos 3.6.1.3. a 3.6.1.5.» — relación de referencia o remisión a otros puntos (3.6.1.3 a 3.6.1.5); la remisión la registra el código desde el texto, no se emite como relación de grafo

- **Lectura:** Excepcion por el miembro (reestructuraciones sin desembolsos), con la norma (además de la genérica)

# Lista `ext::3.6.4` (b2)

## `ext::3.6.4::intro` (encabezado) — propuesta: **no_cumple**

> *heredado:* Sección 3. Disposiciones específicas para los egresos por el mercado de cambios
> *heredado:* 3.6. Pagos de títulos de deuda u otros valores representativos de deuda denominados y
> *heredado:* 3.6.4. El acceso al mercado de cambios con anterioridad al vencimiento requerirá la
> *propio:* conformidad previa del BCRA excepto que la operación encuadre en alguna de las siguientes situaciones y se cumplan la totalidad de las condiciones estipuladas en cada caso:

- Estado final: `completo_ok_directo`; rechazos: 1
- **e1 Potestad** «Acceso al mercado de cambios con conformidad previa del BCRA» — El acceso al mercado de cambios con anterioridad al vencimiento requiere la conformidad previa del BCRA · tramo: «El acceso al mercado de cambios con anterioridad al vencimiento requerirá la conformidad previa del BCRA»
- **e2 Excepcion** «Excepción — acceso sin conformidad previa» — El requisito de conformidad previa del BCRA no aplica cuando la operación encuadra en alguna de las situaciones siguientes y se cumplen todas las condiciones estipuladas en cada caso · tramo: «excepto que la operación encuadre en alguna de las siguientes situaciones y se cumplan la totalidad de las condiciones estipuladas en cada caso»
- Omisión `fuera_de_tipos`: «las siguientes situaciones» — Anuncio de lista de supuestos/excepciones cuyo contenido está en los ítems del punto 3.6.4 (no en esta unidad intro). La lista entera se extrae en cada ítem como Condicion de la Excepcion e2, sin duplicar aquí el anuncio.

- **Lectura:** la norma (Potestad) y la Excepcion, sin relación entre ellas

## `ext::3.6.4.1` (ítem) — propuesta: **no_cumple** (dudosa)

> *heredado:* Sección 3. Disposiciones específicas para los egresos por el mercado de cambios
> *heredado:* Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–, adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables.
> *heredado:* 3.6. Pagos de títulos de deuda u otros valores representativos de deuda denominados y
> *heredado:* pagaderos en moneda extranjera en el país y obligaciones en moneda extranjera entre residentes.
> *heredado:* 3.6.4. El acceso al mercado de cambios con anterioridad al vencimiento requerirá la
> *heredado:* conformidad previa del BCRA excepto que la operación encuadre en alguna de las siguientes situaciones y se cumplan la totalidad de las condiciones estipuladas en cada caso:
> *propio:* 3.6.4.1. Financiaciones de entidades locales por consumos en moneda extranjera mediante tarjetas de crédito o de compra. La deuda se origina en financiaciones en moneda extranjera otorgadas por entidades financieras locales por los consumos en moneda extranjera efectuados mediante tarjetas de crédito o de compra.

- Estado final: `aceptado_tras_reintento`; rechazos: 0
- **e1 Operacion** «Financiación de consumos en moneda extranjera» — Financiaciones en moneda extranjera otorgadas por entidades financieras locales por consumos en moneda extranjera efectuados mediante tarjetas de crédito o de compra · props: `{"tipo": "Financiación"}` · tramo: «Financiaciones de entidades locales por consumos en moneda extranjera mediante tarjetas de crédito o de compra»
- **e2 Restriccion** «Acceso anticipado al mercado de cambios requiere conformidad previa» — El acceso al mercado de cambios con anterioridad al vencimiento requiere la conformidad previa del BCRA · props: `{"tipo": "limite_cualitativo"}` · tramo: «El acceso al mercado de cambios con anterioridad al vencimiento requerirá la conformidad previa del BCRA»
- **e3 Excepcion** «Excepción conformidad previa — financiaciones por consumos en tarjeta» — No se requiere conformidad previa del BCRA cuando la operación encuadra en financiaciones de entidades locales por consumos en moneda extranjera mediante tarjetas de crédito o de compra y se cumplen las condiciones estipuladas · tramo: «excepto que la operación encuadre en alguna de las siguientes situaciones y se cumplan la totalidad de las condiciones estipuladas en cada caso»
- **e4 Condicion** «Cumplimiento de totalidad de condiciones del ítem» — Se deben cumplir la totalidad de las condiciones estipuladas para que la excepción a la conformidad previa sea aplicable · umbral: ['la totalidad de las condiciones'] · tramo: «se cumplan la totalidad de las condiciones estipuladas en cada caso»
- R: e3 Excepcion «Excepción conformidad previa — financiaciones por consumos en tarjeta» —exceptua→ e2 Restriccion «Acceso anticipado al mercado de cambios requiere conformidad previa»
- R: e4 Condicion «Cumplimiento de totalidad de condiciones del ítem» —condicion_de→ e3 Excepcion «Excepción conformidad previa — financiaciones por consumos en tarjeta»
- R: e2 Restriccion «Acceso anticipado al mercado de cambios requiere conformidad previa» —aplica_a→ Sujeto_entidad_financiera (mención «entidades financieras locales», exacta)

- **Lectura:** una Condicion con el cuantificador y la norma («la totalidad… para que la excepción a la conformidad previa sea aplicable»), pero el supuesto va en una Excepcion compuesta, no en una Condicion

## `ext::3.6.4.2` (ítem) — propuesta: **no_cumple**

> *heredado:* Sección 3. Disposiciones específicas para los egresos por el mercado de cambios
> *heredado:* Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–, adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables.
> *heredado:* 3.6. Pagos de títulos de deuda u otros valores representativos de deuda denominados y
> *heredado:* pagaderos en moneda extranjera en el país y obligaciones en moneda extranjera entre residentes.
> *heredado:* 3.6.4. El acceso al mercado de cambios con anterioridad al vencimiento requerirá la
> *heredado:* conformidad previa del BCRA excepto que la operación encuadre en alguna de las siguientes situaciones y se cumplan la totalidad de las condiciones estipuladas en cada caso:
> *propio:* 3.6.4.2. Otras financiaciones en moneda extranjera de entidades financieras locales, excepto la cancelación de giros en descubierto en cuentas corrientes en dólares estadounidenses, canceladas en forma simultánea con la liquidación de fondos desde el exterior por nuevos endeudamientos. i) la precancelación sea efectuada en manera simultánea con los fondos liquidados de un nuevo endeudamiento financiero comprendido en el punto 3.5. y/o una nueva prefinanciación de exportaciones del exterior; ii) la vida promedio del nuevo endeudamiento sea mayor a la vida promedio remanente de la deuda que se precancela; iii) el monto acumulado de los vencimientos de capital del nuevo endeudamiento en ningún momento, hasta la fecha de vencimiento de la deuda que se cancela, podrá superar el monto que hubieran acumulado los vencimientos de capital de la financiación a precancelar; y iv)en caso de que el nuevo endeudamiento sea una prefinanciación de exportaciones del exterior, la entidad deberá contar con una declaración jurada del cliente dejando constancia de que será necesaria la conformidad previa del BCRA para la aplicación de divisas de cobros de exportaciones a la cancelación del capital con anterioridad a los vencimientos computados a los efectos del cumplimiento de las condiciones indicadas. Si la financiación precancelada por el cliente hubiese sido otorgada a partir de una línea de crédito del exterior, la entidad financiera podrá a su vez precancelar el capital y los intereses devengados de la línea de crédito por la parte proporcional a la deuda cobrada anticipadamente.

- Estado final: `cola_humana`; rechazos: 0
- **e1 Operacion** «Precancelación de financiaciones en moneda extranjera» — Precancelación de financiaciones en moneda extranjera de entidades financieras locales, excepto la cancelación de giros en descubierto en cuentas corrientes en dólares estadounidenses, canceladas en forma simultánea con la liquidación de fondos desde el exterior por nuevos endeudamientos · props: `{"tipo": "Precancelación de financiaciones"}` · tramo: «Otras financiaciones en moneda extranjera de entidades financieras locales, excepto la cancelación de giros en descubierto en cuentas corrientes en dólares estadounidenses, canceladas en forma simultánea con la liquidación de fondos desde el exterior por nuevos endeudamientos»
- **e2 Condicion** «Simultaneidad con fondos de nuevo endeudamiento» — La precancelación debe efectuarse de manera simultánea con los fondos liquidados de un nuevo endeudamiento financiero comprendido en el punto 3.5 y/o una nueva prefinanciación de exportaciones del exterior · tramo: «la precancelación sea efectuada en manera simultánea con los fondos liquidados de un nuevo endeudamiento financiero comprendido en el punto 3.5. y/o una nueva prefinanciación de exportaciones del exterior»
- **e3 Condicion** «Vida promedio del nuevo endeudamiento mayor» — La vida promedio del nuevo endeudamiento debe ser mayor a la vida promedio remanente de la deuda que se precancela · tramo: «la vida promedio del nuevo endeudamiento sea mayor a la vida promedio remanente de la deuda que se precancela»
- **e4 Restriccion** «Límite acumulado de vencimientos de capital» — El monto acumulado de los vencimientos de capital del nuevo endeudamiento no podrá superar el monto que hubieran acumulado los vencimientos de capital de la financiación a precancelar · props: `{"tipo": "limite_cuantitativo"}` · umbral: ['podrá superar el monto que hubieran acumulado los vencimientos de capital de la financiación a precancelar'] · tramo: «el monto acumulado de los vencimientos de capital del nuevo endeudamiento en ningún momento, hasta la fecha de vencimiento de la deuda que se cancela, podrá superar el monto que hubieran acumulado los vencimientos de capital de la financiación a precancelar»
- **e5 Obligacion** «Declaración jurada del cliente — prefinanciación de exportaciones» — La entidad debe contar con una declaración jurada del cliente dejando constancia de que será necesaria la conformidad previa del BCRA para la aplicación de divisas de cobros de exportaciones a la cancelación del capital con anterioridad a los vencimientos computados a los efectos del cumplimiento de las condiciones indicadas · props: `{"tipo": "otra"}` · tramo: «en caso de que el nuevo endeudamiento sea una prefinanciación de exportaciones del exterior, la entidad deberá contar con una declaración jurada del cliente dejando constancia de que será necesaria la conformidad previa del BCRA para la aplicación de divisas de cobros de exportaciones a la cancelación del capital con anterioridad a los vencimientos computados a los efectos del cumplimiento de las condiciones indicadas»
- **e6 Potestad** «Precancelación de línea de crédito del exterior» — La entidad financiera puede precancelar el capital y los intereses devengados de la línea de crédito por la parte proporcional a la deuda cobrada anticipadamente, cuando la financiación precancelada por el cliente hubiese sido otorgada a partir de una línea de crédito del exterior · tramo: «Si la financiación precancelada por el cliente hubiese sido otorgada a partir de una línea de crédito del exterior, la entidad financiera podrá a su vez precancelar el capital y los intereses devengados de la línea de crédito por la parte proporcional a la deuda cobrada anticipadamente»
- R: e2 Condicion «Simultaneidad con fondos de nuevo endeudamiento» —condicion_de→ e1 Operacion «Precancelación de financiaciones en moneda extranjera»
- R: e3 Condicion «Vida promedio del nuevo endeudamiento mayor» —condicion_de→ e1 Operacion «Precancelación de financiaciones en moneda extranjera»
- R: e4 Restriccion «Límite acumulado de vencimientos de capital» —limita→ e1 Operacion «Precancelación de financiaciones en moneda extranjera» [coherente]
- R: e5 Obligacion «Declaración jurada del cliente — prefinanciación de exportaciones» —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad», exacta)
- R: e6 Potestad «Precancelación de línea de crédito del exterior» —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad financiera», exacta)
- Omisión `meta_normativo`: «El acceso al mercado de cambios con anterioridad al vencimiento requerirá la conformidad previa del BCRA excepto que la operación encuadre en alguna de las siguientes situaciones y se cumplan la totalidad de las condiciones estipuladas en cada caso» — Encabezado de lista que anuncia la excepción general a la exigencia de conformidad previa del BCRA; el contenido se compone en los ítems de la lista
- Faltante de E3 pendiente (excepcion_ausente, alta): «excepto la cancelación de giros en descubierto en cuentas corrientes en dólares estadounidenses, canceladas en forma simultánea con la liquidación de fondos desde el exterior por nuevos endeudamientos.»

- **Lectura:** Condicion sin norma ni cuantificador

## `ext::3.6.4.3` (ítem) — propuesta: **no_cumple**

> *heredado:* Sección 3. Disposiciones específicas para los egresos por el mercado de cambios
> *heredado:* Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–, adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables.
> *heredado:* 3.6. Pagos de títulos de deuda u otros valores representativos de deuda denominados y
> *heredado:* pagaderos en moneda extranjera en el país y obligaciones en moneda extranjera entre residentes.
> *heredado:* 3.6.4. El acceso al mercado de cambios con anterioridad al vencimiento requerirá la
> *heredado:* conformidad previa del BCRA excepto que la operación encuadre en alguna de las siguientes situaciones y se cumplan la totalidad de las condiciones estipuladas en cada caso:
> *propio:* 3.6.4.3. Precancelación de intereses en el marco de un proceso de canje de títulos de deuda. i) la precancelación de intereses se concreta en el marco de un proceso de canje de títulos de deuda emitidos por el cliente, en el cual se entrega al acreedor un nuevo título con registro público en el país no comprendido en el punto 3.5. ii) el monto abonado antes del vencimiento corresponde a los intereses devengados a la fecha de cierre del canje; iii) la vida promedio de los nuevos títulos de deuda es mayor a la vida promedio remanente del título canjeado; y iv)el monto acumulado de los vencimientos de capital de los nuevos títulos en ningún momento, hasta la fecha de vencimiento de la deuda que se cancela, podrá superar el monto que hubieran acumulado los vencimientos de capital del título canjeado.

- Estado final: `aceptado_tras_reintento`; rechazos: 0
- **e1 Condicion** «Precancelación en marco de canje de títulos» — La precancelación de intereses debe concretarse en el marco de un proceso de canje de títulos de deuda emitidos por el cliente, en el cual se entrega al acreedor un nuevo título con registro público en el país no comprendido en el punto 3.5. · tramo: «la precancelación de intereses se concreta en el marco de un proceso de canje de títulos de deuda emitidos por el cliente, en el cual se entrega al acreedor un nuevo título con registro público en el país no comprendido en el punto 3.5.»
- **e2 Condicion** «Monto abonado corresponde a intereses devengados» — El monto abonado antes del vencimiento debe corresponder a los intereses devengados a la fecha de cierre del canje. · tramo: «el monto abonado antes del vencimiento corresponde a los intereses devengados a la fecha de cierre del canje»
- **e3 Condicion** «Vida promedio nuevos títulos mayor a remanente» — La vida promedio de los nuevos títulos de deuda debe ser mayor a la vida promedio remanente del título canjeado. · tramo: «la vida promedio de los nuevos títulos de deuda es mayor a la vida promedio remanente del título canjeado»
- **e4 Restriccion** «Tope vencimientos capital nuevos títulos» — El monto acumulado de los vencimientos de capital de los nuevos títulos no podrá superar, en ningún momento hasta la fecha de vencimiento de la deuda que se cancela, el monto que hubieran acumulado los vencimientos de capital del título canjeado. · props: `{"tipo": "limite_cuantitativo"}` · umbral: ['podrá superar el monto que hubieran acumulado los vencimientos de capital del título canjeado'] · tramo: «el monto acumulado de los vencimientos de capital de los nuevos títulos en ningún momento, hasta la fecha de vencimiento de la deuda que se cancela, podrá superar el monto que hubieran acumulado los vencimientos de capital del título canjeado»
- **e5 Operacion** «Precancelación de intereses en canje de títulos» — Precancelación de intereses en el marco de un proceso de canje de títulos de deuda, sujeta a conformidad previa del BCRA excepto cuando encuadre en las condiciones especificadas. · props: `{"tipo": "precancelación de intereses"}` · tramo: «Precancelación de intereses en el marco de un proceso de canje de títulos de deuda»
- R: e1 Condicion «Precancelación en marco de canje de títulos» —condicion_de→ e5 Operacion «Precancelación de intereses en canje de títulos»
- R: e2 Condicion «Monto abonado corresponde a intereses devengados» —condicion_de→ e5 Operacion «Precancelación de intereses en canje de títulos»
- R: e3 Condicion «Vida promedio nuevos títulos mayor a remanente» —condicion_de→ e5 Operacion «Precancelación de intereses en canje de títulos»
- R: e4 Restriccion «Tope vencimientos capital nuevos títulos» —limita→ e5 Operacion «Precancelación de intereses en canje de títulos» [coherente]
- Omisión `meta_normativo`: «El acceso al mercado de cambios con anterioridad al vencimiento requerirá la conformidad previa del BCRA excepto que la operación encuadre en alguna de las siguientes situaciones y se cumplan la totalidad de las condiciones estipuladas en cada caso» — Enunciado del encabezado 3.6.4 que abre la lista de excepciones; el contenido normativo (la exigencia de conformidad previa y su excepción) se compone en cada ítem según COMPOSICIÓN CON EL ENCABEZADO DE UNA LISTA

- **Lectura:** Condicion sin norma ni cuantificador

## `ext::3.6.4.4` (ítem) — propuesta: **no_cumple**

> *heredado:* Sección 3. Disposiciones específicas para los egresos por el mercado de cambios
> *heredado:* Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–, adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables.
> *heredado:* 3.6. Pagos de títulos de deuda u otros valores representativos de deuda denominados y
> *heredado:* pagaderos en moneda extranjera en el país y obligaciones en moneda extranjera entre residentes.
> *heredado:* 3.6.4. El acceso al mercado de cambios con anterioridad al vencimiento requerirá la
> *heredado:* conformidad previa del BCRA excepto que la operación encuadre en alguna de las siguientes situaciones y se cumplan la totalidad de las condiciones estipuladas en cada caso:
> *propio:* 3.6.4.4. Precancelación de capital e intereses de un título de deuda comprendido en este punto 3.6. con la liquidación de fondos ingresados desde el exterior por la emisión de un nuevo título de deuda comprendido en el punto 3.5. i) la precancelación de capital sea efectuada en manera simultánea con la liquidación de los fondos ingresados desde el exterior por la emisión de un nuevo título de deuda comprendido en el punto 3.5. emitido en el marco de una operación de refinanciación, recompra y/o rescate anticipado del título de deuda. a) el nuevo título de deuda contempla 1 (un) año de gracia para el pago de capital y su vida promedio es al menos 2 (dos) años mayor a la vida promedio remanente del título de deuda que se precancela; y b) el monto acumulado de los vencimientos de capital del nuevo endeudamiento en ningún momento podrá superar, hasta la fecha de vencimiento de la deuda que se cancela, el monto que hubieran acumulado los vencimientos de capital de la deuda que se cancela. ii) la precancelación de intereses corresponde a los intereses devengados por la deuda refinanciada hasta la fecha de cierre de la operación de recompra y/o rescate, sin necesidad de que exista una liquidación de fondos por el monto equivalente; Adicionalmente, la entidad podrá darle acceso al mercado de cambios al cliente para: iii) pagar en concepto de prima de recompra, de rescate anticipado o similar hasta el equivalente del 5% (cinco por ciento) del monto del capital del título de deuda recomprado y/o rescatado, en la medida que el pago se concrete de manera simultánea con una liquidación de fondos ingresados desde el exterior por el nuevo título de deuda que exceda al monto de capital que se precancela, como mínimo, por un monto equivalente al monto de la prima abonada. iv)pagar a la fecha de cierre de la operación de recompra y/o rescate, sin necesidad de que exista una liquidación de fondos por el monto equivalente, los gastos de emisión u otros servicios prestados por no residentes en el marco de la emisión de los nuevos títulos de deuda emitidos y/o la operación de recompra y/o rescate.

- Estado final: `completo_ok_directo`; rechazos: 1
- **e1 Operacion** «Precancelación de capital e intereses con liquidación de nuevo título» — Precancelación de capital e intereses de un título de deuda comprendido en el punto 3.6 con liquidación simultánea de fondos ingresados desde el exterior por emisión de nuevo título de deuda comprendido en el punto 3.5, en marco de operación de refinanciación, recompra y/o rescate anticipado. · props: `{"tipo": "Precancelación de deuda con refinanciación"}` · tramo: «Precancelación de capital e intereses de un título de deuda comprendido en este punto 3.6. con la liquidación de fondos ingresados desde el exterior por la emisión de un nuevo título de deuda comprendido en el punto 3.5.»
- **e2 Condicion** «Precancelación simultánea con liquidación de fondos» — La precancelación de capital debe efectuarse de manera simultánea con la liquidación de fondos ingresados desde el exterior por emisión de nuevo título de deuda en marco de refinanciación, recompra y/o rescate anticipado. · tramo: «la precancelación de capital sea efectuada en manera simultánea con la liquidación de los fondos ingresados desde el exterior por la emisión de un nuevo título de deuda comprendido en el punto 3.5. emitido en el marco de una operación de refinanciación, recompra y/o rescate anticipado del título de deuda.»
- **e3 Condicion** «Nuevo título con 1 año de gracia y vida promedio mayor» — El nuevo título de deuda debe contemplar 1 año de gracia para el pago de capital y su vida promedio debe ser al menos 2 años mayor a la vida promedio remanente del título que se precancela. · umbral: ['1 (un) año de gracia', 'al menos 2 (dos) años mayor'] · tramo: «el nuevo título de deuda contempla 1 (un) año de gracia para el pago de capital y su vida promedio es al menos 2 (dos) años mayor a la vida promedio remanente del título de deuda que se precancela»
- **e4 Restriccion** «Límite monto acumulado vencimientos capital nuevo endeudamiento» — El monto acumulado de los vencimientos de capital del nuevo endeudamiento no podrá superar, hasta la fecha de vencimiento de la deuda que se cancela, el monto que hubieran acumulado los vencimientos de capital de la deuda que se cancela. · props: `{"tipo": "limite_cuantitativo"}` · umbral: ['en ningún momento podrá superar, hasta la fecha de vencimiento de la deuda que se cancela'] · tramo: «el monto acumulado de los vencimientos de capital del nuevo endeudamiento en ningún momento podrá superar, hasta la fecha de vencimiento de la deuda que se cancela, el monto que hubieran acumulado los vencimientos de capital de la deuda que se cancela.»
- **e5 Condicion** «Precancelación de intereses devengados hasta cierre de operación» — La precancelación de intereses corresponde a los intereses devengados por la deuda refinanciada hasta la fecha de cierre de la operación de recompra y/o rescate, sin necesidad de liquidación de fondos por monto equivalente. · tramo: «la precancelación de intereses corresponde a los intereses devengados por la deuda refinanciada hasta la fecha de cierre de la operación de recompra y/o rescate, sin necesidad de que exista una liquidación de fondos por el monto equivalente»
- **e6 Potestad** «Acceso mercado cambios para pago prima recompra/rescate hasta 5%» — La entidad podrá darle acceso al mercado de cambios al cliente para pagar prima de recompra, rescate anticipado o similar hasta el 5% del monto del capital del título recomprado y/o rescatado, siempre que el pago sea simultáneo con liquidación de fondos del nuevo título que exceda el monto de capital precancelado por monto equivalente a la prima. · tramo: «la entidad podrá darle acceso al mercado de cambios al cliente para pagar en concepto de prima de recompra, de rescate anticipado o similar hasta el equivalente del 5% (cinco por ciento) del monto del capital del título de deuda recomprado y/o rescatado, en la medida que el pago se concrete de manera simultánea con una liquidación de fondos ingresados desde el exterior por el nuevo título de deuda que exceda al monto de capital que se precancela, como mínimo, por un monto equivalente al monto de la prima abonada.»
- **e7 Condicion** «Pago prima simultáneo con liquidación fondos nuevo título» — El pago de la prima debe ser simultáneo con liquidación de fondos ingresados desde el exterior por nuevo título de deuda que exceda el monto de capital precancelado, como mínimo, por monto equivalente a la prima abonada. · umbral: ['como mínimo, por un monto equivalente al monto de la prima abonada'] · tramo: «en la medida que el pago se concrete de manera simultánea con una liquidación de fondos ingresados desde el exterior por el nuevo título de deuda que exceda al monto de capital que se precancela, como mínimo, por un monto equivalente al monto de la prima abonada»
- **e8 Restriccion** «Límite prima recompra/rescate 5% del capital» — La prima de recompra, rescate anticipado o similar no podrá exceder el 5% del monto del capital del título recomprado y/o rescatado. · props: `{"tipo": "limite_cuantitativo"}` · umbral: ['hasta el equivalente del 5% (cinco por ciento)'] · tramo: «hasta el equivalente del 5% (cinco por ciento) del monto del capital del título de deuda recomprado y/o rescatado»
- **e9 Potestad** «Acceso mercado cambios para pago gastos emisión y servicios» — La entidad podrá darle acceso al mercado de cambios al cliente para pagar, a la fecha de cierre de la operación de recompra y/o rescate, sin necesidad de liquidación de fondos por monto equivalente, los gastos de emisión u otros servicios prestados por no residentes en marco de emisión de nuevos títulos de deuda y/o operación de recompra y/o rescate. · tramo: «la entidad podrá darle acceso al mercado de cambios al cliente para pagar a la fecha de cierre de la operación de recompra y/o rescate, sin necesidad de que exista una liquidación de fondos por el monto equivalente, los gastos de emisión u otros servicios prestados por no residentes en el marco de la emisión de los nuevos títulos de deuda emitidos y/o la operación de recompra y/o rescate.»
- **e10 Condicion** «Pago gastos a fecha cierre operación recompra/rescate» — El pago de gastos de emisión y servicios debe realizarse a la fecha de cierre de la operación de recompra y/o rescate, sin necesidad de liquidación de fondos por monto equivalente. · tramo: «a la fecha de cierre de la operación de recompra y/o rescate, sin necesidad de que exista una liquidación de fondos por el monto equivalente»
- R: e2 Condicion «Precancelación simultánea con liquidación de fondos» —condicion_de→ e1 Operacion «Precancelación de capital e intereses con liquidación de nuevo título»
- R: e3 Condicion «Nuevo título con 1 año de gracia y vida promedio mayor» —condicion_de→ e1 Operacion «Precancelación de capital e intereses con liquidación de nuevo título»
- R: e4 Restriccion «Límite monto acumulado vencimientos capital nuevo endeudamiento» —limita→ e1 Operacion «Precancelación de capital e intereses con liquidación de nuevo título» [coherente]
- R: e5 Condicion «Precancelación de intereses devengados hasta cierre de operación» —condicion_de→ e1 Operacion «Precancelación de capital e intereses con liquidación de nuevo título»
- R: e7 Condicion «Pago prima simultáneo con liquidación fondos nuevo título» —condicion_de→ e6 Potestad «Acceso mercado cambios para pago prima recompra/rescate hasta 5%»
- R: e10 Condicion «Pago gastos a fecha cierre operación recompra/rescate» —condicion_de→ e9 Potestad «Acceso mercado cambios para pago gastos emisión y servicios»
- R: e1 Operacion «Precancelación de capital e intereses con liquidación de nuevo título» —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad», exacta)
- R: e6 Potestad «Acceso mercado cambios para pago prima recompra/rescate hasta 5%» —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad», exacta)
- R: e9 Potestad «Acceso mercado cambios para pago gastos emisión y servicios» —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad», exacta)
- Omisión `meta_normativo`: «Adicionalmente, la entidad podrá darle acceso al mercado de cambios al cliente para» — Introducción a opciones adicionales; el contenido normativo (las potestades e6 y e9) se extrae en sus respectivas entidades.

- **Lectura:** Condicion sin norma ni cuantificador

## `ext::3.6.4.5` (ítem) — propuesta: **no_cumple**

> *heredado:* Sección 3. Disposiciones específicas para los egresos por el mercado de cambios
> *heredado:* Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–, adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables.
> *heredado:* 3.6. Pagos de títulos de deuda u otros valores representativos de deuda denominados y
> *heredado:* pagaderos en moneda extranjera en el país y obligaciones en moneda extranjera entre residentes.
> *heredado:* 3.6.4. El acceso al mercado de cambios con anterioridad al vencimiento requerirá la
> *heredado:* conformidad previa del BCRA excepto que la operación encuadre en alguna de las siguientes situaciones y se cumplan la totalidad de las condiciones estipuladas en cada caso:
> *propio:* 3.6.4.5. Precancelación de capital e intereses de un título de deuda comprendido en este punto 3.6. en forma simultánea con la liquidación de otros endeudamientos financieros comprendidos en el punto 3.5. i) la precancelación de capital e intereses sea efectuada en manera simultánea con los fondos liquidados de un nuevo endeudamiento financiero comprendido en el punto 3.5.; y ii) la vida promedio del nuevo endeudamiento sea mayor a la vida promedio remanente del título de deuda que se precancela; y iii) el monto acumulado de los vencimientos de capital del nuevo endeudamiento en ningún momento, hasta la fecha de vencimiento de la deuda que se cancela, podrá superar el monto que hubieran acumulado los vencimientos de capital del título de deuda que se cancela.

- Estado final: `aceptado_con_residuales`; rechazos: 1
- **e1 Operacion** «Precancelación de capital e intereses de título de deuda» — Precancelación de capital e intereses de un título de deuda comprendido en el punto 3.6, realizada en forma simultánea con la liquidación de otros endeudamientos financieros comprendidos en el punto 3.5. · props: `{"tipo": "Precancelación de deuda"}` · tramo: «Precancelación de capital e intereses de un título de deuda comprendido en este punto 3.6.»
- **e2 Operacion** «Liquidación de nuevo endeudamiento financiero» — Liquidación de fondos de un nuevo endeudamiento financiero comprendido en el punto 3.5. · props: `{"tipo": "Liquidación de endeudamiento"}` · tramo: «fondos liquidados de un nuevo endeudamiento financiero comprendido en el punto 3.5.»
- **e3 Condicion** «Simultaneidad de precancelación y liquidación» — La precancelación de capital e intereses debe efectuarse en forma simultánea con los fondos liquidados del nuevo endeudamiento financiero. · tramo: «la precancelación de capital e intereses sea efectuada en manera simultánea con los fondos liquidados de un nuevo endeudamiento financiero comprendido en el punto 3.5.»
- **e4 Condicion** «Vida promedio del nuevo endeudamiento mayor a remanente» — La vida promedio del nuevo endeudamiento debe ser mayor a la vida promedio remanente del título de deuda que se precancela. · umbral: ['mayor a la vida promedio remanente'] · tramo: «la vida promedio del nuevo endeudamiento sea mayor a la vida promedio remanente del título de deuda que se precancela»
- **e5 Restriccion** «Límite acumulado de vencimientos de capital del nuevo endeudamiento» — El monto acumulado de los vencimientos de capital del nuevo endeudamiento no podrá superar, en ningún momento hasta la fecha de vencimiento de la deuda que se cancela, el monto que hubieran acumulado los vencimientos de capital del título de deuda que se cancela. · props: `{"tipo": "limite_cuantitativo"}` · umbral: ['podrá superar el monto que hubieran acumulado los vencimientos de capital del título de deuda que se cancela'] · tramo: «el monto acumulado de los vencimientos de capital del nuevo endeudamiento en ningún momento, hasta la fecha de vencimiento de la deuda que se cancela, podrá superar el monto que hubieran acumulado los vencimientos de capital del título de deuda que se cancela»
- **e6 Potestad** «Acceso al mercado de cambios sin conformidad previa del BCRA» — Las entidades pueden acceder al mercado de cambios con anterioridad al vencimiento sin requerir conformidad previa del BCRA cuando la operación encuadra en las situaciones especificadas y se cumplen todas las condiciones estipuladas. · tramo: «El acceso al mercado de cambios con anterioridad al vencimiento requerirá la conformidad previa del BCRA excepto que la operación encuadre en alguna de las siguientes situaciones y se cumplan la totalidad de las condiciones estipuladas en cada caso»
- R: e3 Condicion «Simultaneidad de precancelación y liquidación» —condicion_de→ e1 Operacion «Precancelación de capital e intereses de título de deuda»
- R: e4 Condicion «Vida promedio del nuevo endeudamiento mayor a remanente» —condicion_de→ e1 Operacion «Precancelación de capital e intereses de título de deuda»
- R: e5 Restriccion «Límite acumulado de vencimientos de capital del nuevo endeudamiento» —limita→ e2 Operacion «Liquidación de nuevo endeudamiento financiero» [coherente]
- R: e6 Potestad «Acceso al mercado de cambios sin conformidad previa del BCRA» —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «Las entidades», exacta)
- Omisión `meta_normativo`: «El acceso al mercado de cambios con anterioridad al vencimiento requerirá la conformidad previa del BCRA excepto que» — Cláusula interpretativa que enuncia la regla general (conformidad previa del BCRA) de la cual el punto 3.6.4.5 es una excepción; el contenido normativo se extrae en la Potestad e6 que habilita el acceso sin conformidad cuando se cumplen las condiciones.

- **Lectura:** Condicion sin norma ni cuantificador; la norma en una Potestad compuesta

## `ext::3.6.4.6` (ítem) — propuesta: **no_cumple**

> *heredado:* Sección 3. Disposiciones específicas para los egresos por el mercado de cambios
> *heredado:* Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–, adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables.
> *heredado:* 3.6. Pagos de títulos de deuda u otros valores representativos de deuda denominados y
> *heredado:* pagaderos en moneda extranjera en el país y obligaciones en moneda extranjera entre residentes.
> *heredado:* 3.6.4. El acceso al mercado de cambios con anterioridad al vencimiento requerirá la
> *heredado:* conformidad previa del BCRA excepto que la operación encuadre en alguna de las siguientes situaciones y se cumplan la totalidad de las condiciones estipuladas en cada caso:
> *propio:* 3.6.4.6. Precancelación de capital e intereses de un título de deuda comprendido en este punto 3.6. en forma simultánea con la liquidación de un nuevo título de deuda del mismo tipo. i) la precancelación de capital e intereses de un título de deuda comprendido en este punto 3.6. sea efectuada en manera simultánea con los fondos liquidados por la emisión de un nuevo título de deuda con registro público en el país no comprendido en el punto 3.5., denominado y suscripto en moneda extranjera y cuyos servicios sean pagaderos en moneda extranjera, y ii) la vida promedio del nuevo título sea mayor a la vida promedio remanente del título de deuda que se precancela; y iii) el monto acumulado de los vencimientos de capital del nuevo título de deuda en ningún momento, hasta la fecha de vencimiento de la deuda que se cancela, podrá superar el monto que hubieran acumulado los vencimientos de capital del título de deuda que se cancela.

- Estado final: `aceptado_con_residuales`; rechazos: 1
- **e1 Operacion** «Precancelación simultánea de título con nueva emisión» — Precancelación de capital e intereses de un título de deuda comprendido en el punto 3.6., efectuada de manera simultánea con los fondos liquidados por la emisión de un nuevo título de deuda con registro público en el país no comprendido en el punto 3.5., denominado y suscripto en moneda extranjera y cuyos servicios sean pagaderos en moneda extranjera · props: `{"tipo": "Precancelación de título de deuda"}` · tramo: «Precancelación de capital e intereses de un título de deuda comprendido en este punto 3.6. en forma simultánea con la liquidación de un nuevo título de deuda del mismo tipo»
- **e2 Condicion** «Vida promedio nuevo título mayor a remanente» — La vida promedio del nuevo título debe ser mayor a la vida promedio remanente del título de deuda que se precancela · umbral: ['mayor a la vida promedio remanente'] · tramo: «la vida promedio del nuevo título sea mayor a la vida promedio remanente del título de deuda que se precancela»
- **e3 Condicion** «Monto acumulado vencimientos no supera límite» — El monto acumulado de los vencimientos de capital del nuevo título de deuda en ningún momento, hasta la fecha de vencimiento de la deuda que se cancela, no podrá superar el monto que hubieran acumulado los vencimientos de capital del título de deuda que se cancela · umbral: ['podrá superar el monto que hubieran acumulado los vencimientos de capital del título de deuda que se cancela'] · tramo: «el monto acumulado de los vencimientos de capital del nuevo título de deuda en ningún momento, hasta la fecha de vencimiento de la deuda que se cancela, podrá superar el monto que hubieran acumulado los vencimientos de capital del título de deuda que se cancela»
- **e4 Potestad** «Acceso al mercado de cambios sin conformidad previa BCRA» — Las entidades quedan autorizadas a acceder al mercado de cambios con anterioridad al vencimiento sin requerir conformidad previa del BCRA cuando la operación encuadra en las situaciones especificadas y se cumplen la totalidad de las condiciones estipuladas · tramo: «El acceso al mercado de cambios con anterioridad al vencimiento requerirá la conformidad previa del BCRA excepto que la operación encuadre en alguna de las siguientes situaciones y se cumplan la totalidad de las condiciones estipuladas en cada caso»
- R: e2 Condicion «Vida promedio nuevo título mayor a remanente» —condicion_de→ e1 Operacion «Precancelación simultánea de título con nueva emisión»
- R: e3 Condicion «Monto acumulado vencimientos no supera límite» —condicion_de→ e1 Operacion «Precancelación simultánea de título con nueva emisión»
- R: e4 Potestad «Acceso al mercado de cambios sin conformidad previa BCRA» —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «las entidades», exacta)
- Omisión `meta_normativo`: «El acceso al mercado de cambios con anterioridad al vencimiento requerirá la conformidad previa del BCRA excepto que» — Cláusula interpretativa que establece la regla general (conformidad previa requerida) de la cual el punto 3.6.4.6 es una excepción; el contenido normativo se extrae en la Potestad e4

- **Lectura:** Condicion sin norma ni cuantificador

## `ext::3.6.4.7` (ítem) — propuesta: **no_cumple**

> *heredado:* Sección 3. Disposiciones específicas para los egresos por el mercado de cambios
> *heredado:* Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–, adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables.
> *heredado:* 3.6. Pagos de títulos de deuda u otros valores representativos de deuda denominados y
> *heredado:* pagaderos en moneda extranjera en el país y obligaciones en moneda extranjera entre residentes.
> *heredado:* 3.6.4. El acceso al mercado de cambios con anterioridad al vencimiento requerirá la
> *heredado:* conformidad previa del BCRA excepto que la operación encuadre en alguna de las siguientes situaciones y se cumplan la totalidad de las condiciones estipuladas en cada caso:
> *propio:* 3.6.4.7. Precancelación de capital e intereses por parte de un VPU adherido al RIGI. El cliente es un Vehículo de Proyecto Único (VPU) adherido al Régimen de Incentivo para Grandes Inversiones (RIGI) que precancela capital o intereses devengados por deudas comprendidas en este punto 3.6. en el marco de lo previsto en el punto 14.2.1.

- Estado final: `completo_ok_directo`; rechazos: 0
- **e1 Operacion** «Precancelación de capital e intereses por VPU RIGI» — Precancelación de capital o intereses devengados por deudas comprendidas en el punto 3.6 (Pagos de títulos de deuda u otros valores representativos de deuda denominados y pagaderos en moneda extranjera en el país y obligaciones en moneda extranjera entre residentes), realizada por un Vehículo de Proyecto Único (VPU) adherido al Régimen de Incentivo para Grandes Inversiones (RIGI), en el marco de lo previsto en el punto 14.2.1. · props: `{"tipo": "Precancelación de deuda"}` · tramo: «Precancelación de capital o intereses devengados por deudas comprendidas en este punto 3.6.»
- **e2 Condicion** «Cliente es VPU adherido al RIGI» — El cliente que realiza la precancelación es un Vehículo de Proyecto Único (VPU) adherido al Régimen de Incentivo para Grandes Inversiones (RIGI). · tramo: «El cliente es un Vehículo de Proyecto Único (VPU) adherido al Régimen de Incentivo para Grandes Inversiones (RIGI)»
- **e3 Potestad** «Acceso al mercado de cambios sin conformidad previa del BCRA» — Las entidades quedan habilitadas a acceder al mercado de cambios con anterioridad al vencimiento sin requerir conformidad previa del BCRA cuando la operación encuadra en una de las situaciones especificadas (incluyendo la precancelación de capital e intereses por parte de un VPU adherido al RIGI) y se cumplen la totalidad de las condiciones estipuladas en cada caso. · tramo: «El acceso al mercado de cambios con anterioridad al vencimiento requerirá la conformidad previa del BCRA excepto que la operación encuadre en alguna de las siguientes situaciones y se cumplan la totalidad de las condiciones estipuladas en cada caso»
- R: e2 Condicion «Cliente es VPU adherido al RIGI» —condicion_de→ e1 Operacion «Precancelación de capital e intereses por VPU RIGI»
- R: e2 Condicion «Cliente es VPU adherido al RIGI» —condicion_de→ e3 Potestad «Acceso al mercado de cambios sin conformidad previa del BCRA»
- R: e3 Potestad «Acceso al mercado de cambios sin conformidad previa del BCRA» —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «Las entidades», exacta)
- Omisión `meta_normativo`: «en el marco de lo previsto en el punto 14.2.1» — 

- **Lectura:** la Condicion del supuesto (VPU adherido al RIGI) sin norma ni cuantificador

# Lista `ext::10.11` (b2)

## `ext::10.11::intro` (encabezado) — propuesta: **cumple**

> *heredado:* Sección 10. Pagos de importaciones y otras compras de bienes en el exterior.
> *heredado:* 10.11. Disposiciones complementarias para importaciones de bienes con registro de ingreso
> *propio:* aduanero hasta el 12/12/23. Se requerirá la conformidad previa del BCRA para el acceso al mercado de cambios para realizar pagos de importaciones por bienes con registro de ingreso aduanero hasta el 12/12/23, excepto cuando, adicionalmente a los restantes requisitos aplicables, la entidad verifique que:

- Estado final: `completo_ok_directo`; rechazos: 0
- **e1 Obligacion** «Conformidad previa BCRA — acceso mercado cambios» — Se requerirá la conformidad previa del BCRA para el acceso al mercado de cambios para realizar pagos de importaciones por bienes con registro de ingreso aduanero hasta el 12/12/23 · props: `{"tipo": "otra"}` · umbral: ['hasta el 12/12/23'] · tramo: «Se requerirá la conformidad previa del BCRA para el acceso al mercado de cambios para realizar pagos de importaciones por bienes con registro de ingreso aduanero hasta el 12/12/23»
- **e2 Excepcion** «Excepción — conformidad previa cuando entidad verifica requisitos» — No se requiere conformidad previa del BCRA cuando la entidad verifica adicionalmente los restantes requisitos aplicables · tramo: «excepto cuando, adicionalmente a los restantes requisitos aplicables, la entidad verifique que:»
- R: e2 Excepcion «Excepción — conformidad previa cuando entidad verifica requisitos» —exceptua_obligacion→ e1 Obligacion «Conformidad previa BCRA — acceso mercado cambios»
- R: e1 Obligacion «Conformidad previa BCRA — acceso mercado cambios» —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad», exacta)
- Omisión `fuera_de_tipos`: «excepto cuando, adicionalmente a los restantes requisitos aplicables, la entidad verifique que:» — Condicion: el bloque intro anuncia una excepción cuyas condiciones se enumeran en los ítems siguientes (no presentes en esta unidad). La Excepcion se extrae sin condicion_de porque la norma que exceptúa (la Obligacion e1) está en la misma unidad, pero el supuesto que activa la excepción está incompleto en el bloque intro y se desarrolla en los ítems del punto. Se registra como omisión porque el tramo del bloque intro solo anuncia la excepción sin enunciar sus condiciones específicas.

- **Lectura:** la Obligacion de la conformidad previa y su Excepcion, unidas por exceptua_obligacion

## `ext::10.11.1` (ítem) — propuesta: **no_cumple**

> *heredado:* Sección 10. Pagos de importaciones y otras compras de bienes en el exterior.
> *heredado:* 10.11. Disposiciones complementarias para importaciones de bienes con registro de ingreso
> *heredado:* aduanero hasta el 12/12/23. Se requerirá la conformidad previa del BCRA para el acceso al mercado de cambios para realizar pagos de importaciones por bienes con registro de ingreso aduanero hasta el 12/12/23, excepto cuando, adicionalmente a los restantes requisitos aplicables, la entidad verifique que:
> *propio:* 10.11.1. el pago corresponda a la cancelación de deudas por operaciones financiadas o garantizadas con anterioridad al 13/12/23 por entidades financieras locales o del exterior; o

- Estado final: `aceptado_con_residuales`; rechazos: 0
- **e1 Operacion** «Cancelación de deudas por operaciones financiadas» — Cancelación de deudas por operaciones financiadas o garantizadas con anterioridad al 13/12/23 por entidades financieras locales o del exterior · props: `{"tipo": "Pago de importación"}` · tramo: «el pago corresponda a la cancelación de deudas por operaciones financiadas o garantizadas con anterioridad al 13/12/23»
- **e2 Condicion** «Operación financiada antes del 13/12/23» — La operación debe haber sido financiada o garantizada con anterioridad al 13/12/23 · umbral: ['con anterioridad al 13/12/23'] · tramo: «operaciones financiadas o garantizadas con anterioridad al 13/12/23»
- **e3 Obligacion** «Requerir conformidad previa BCRA — acceso mercado cambios» — Se requiere conformidad previa del BCRA para acceso al mercado de cambios para realizar pagos de importaciones por bienes con registro de ingreso aduanero hasta el 12/12/23, excepto cuando el pago corresponda a cancelación de deudas por operaciones financiadas o garantizadas con anterioridad al 13/12/23 · props: `{"tipo": "reporte_al_supervisor"}` · tramo: «Se requerirá la conformidad previa del BCRA para el acceso al mercado de cambios para realizar pagos de importaciones por bienes con registro de ingreso aduanero hasta el 12/12/23, excepto cuando, adicionalmente a los restantes requisitos aplicables, la entidad verifique que: […] el pago corresponda a la cancelación de deudas por operaciones financiadas o garantizadas con anterioridad al 13/12/23»
- **e4 Excepcion** «Excepción — cancelación de deudas financiadas antes del 13/12/23» — No se requiere conformidad previa del BCRA cuando el pago corresponda a cancelación de deudas por operaciones financiadas o garantizadas con anterioridad al 13/12/23 · tramo: «excepto cuando, adicionalmente a los restantes requisitos aplicables, la entidad verifique que: […] el pago corresponda a la cancelación de deudas por operaciones financiadas o garantizadas con anterioridad al 13/12/23»
- R: e2 Condicion «Operación financiada antes del 13/12/23» —condicion_de→ e4 Excepcion «Excepción — cancelación de deudas financiadas antes del 13/12/23»
- R: e4 Excepcion «Excepción — cancelación de deudas financiadas antes del 13/12/23» —exceptua_obligacion→ e3 Obligacion «Requerir conformidad previa BCRA — acceso mercado cambios»
- R: e3 Obligacion «Requerir conformidad previa BCRA — acceso mercado cambios» —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad», exacta)
- Omisión `meta_normativo`: «adicionalmente a los restantes requisitos aplicables» — Referencia a otros requisitos sin contenido normativo específico en esta unidad

- **Lectura:** Condicion sin norma ni cuantificador, hacia una Excepcion compuesta en el ítem

## `ext::10.11.2` (ítem) — propuesta: **no_cumple**

> *heredado:* Sección 10. Pagos de importaciones y otras compras de bienes en el exterior.
> *heredado:* 10.11. Disposiciones complementarias para importaciones de bienes con registro de ingreso
> *heredado:* aduanero hasta el 12/12/23. Se requerirá la conformidad previa del BCRA para el acceso al mercado de cambios para realizar pagos de importaciones por bienes con registro de ingreso aduanero hasta el 12/12/23, excepto cuando, adicionalmente a los restantes requisitos aplicables, la entidad verifique que:
> *propio:* 10.11.2. el pago corresponda a la cancelación de deudas por operaciones financiadas o garantizadas con anterioridad al 13/12/23 por organismos internacionales y/o agencias oficiales de crédito; o Las entidades podrán considerar también como operación garantizada por una agencia oficial de crédito a aquella que se encuentre cubierta por una garantía emitida por una aseguradora privada por cuenta y orden de un gobierno nacional de otro país. En todos los casos, la entidad interviniente deberá contar con documentación en la que conste explícitamente tal situación.

- Estado final: `completo_ok_directo`; rechazos: 0
- **e1 Condicion** «Pago cancelación deudas operaciones financiadas/garantizadas» — El pago corresponde a la cancelación de deudas por operaciones financiadas o garantizadas con anterioridad al 13/12/23 por organismos internacionales y/o agencias oficiales de crédito · umbral: ['con anterioridad al 13/12/23'] · tramo: «el pago corresponda a la cancelación de deudas por operaciones financiadas o garantizadas con anterioridad al 13/12/23 por organismos internacionales y/o agencias oficiales de crédito»
- **e2 Potestad** «Considerar operación garantizada por aseguradora privada» — Las entidades podrán considerar como operación garantizada por una agencia oficial de crédito aquella que se encuentre cubierta por una garantía emitida por una aseguradora privada por cuenta y orden de un gobierno nacional de otro país · tramo: «Las entidades podrán considerar también como operación garantizada por una agencia oficial de crédito a aquella que se encuentre cubierta por una garantía emitida por una aseguradora privada por cuenta y orden de un gobierno nacional de otro país»
- **e3 Obligacion** «Contar con documentación de garantía de aseguradora privada» — La entidad interviniente deberá contar con documentación en la que conste explícitamente que la operación se encuentra cubierta por una garantía emitida por una aseguradora privada por cuenta y orden de un gobierno nacional de otro país · props: `{"tipo": "otra"}` · tramo: «la entidad interviniente deberá contar con documentación en la que conste explícitamente tal situación»
- **e4 Definicion** «Operación garantizada por agencia oficial de crédito» — Aquella que se encuentre cubierta por una garantía emitida por una aseguradora privada por cuenta y orden de un gobierno nacional de otro país · props: `{"termino": "operación garantizada por una agencia oficial de crédito"}` · tramo: «operación garantizada por una agencia oficial de crédito a aquella que se encuentre cubierta por una garantía emitida por una aseguradora privada por cuenta y orden de un gobierno nacional de otro país»
- R: e2 Potestad «Considerar operación garantizada por aseguradora privada» —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «Las entidades», exacta)
- R: e3 Obligacion «Contar con documentación de garantía de aseguradora privada» —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad interviniente», exacta)
- Omisión `meta_normativo`: «En todos los casos» — Expresión introductoria que no prescribe conducta sino que introduce el alcance de la obligación siguiente

- **Lectura:** Condicion sin norma ni cuantificador

## `ext::10.11.3` (ítem) — propuesta: **no_cumple**

> *heredado:* Sección 10. Pagos de importaciones y otras compras de bienes en el exterior.
> *heredado:* 10.11. Disposiciones complementarias para importaciones de bienes con registro de ingreso
> *heredado:* aduanero hasta el 12/12/23. Se requerirá la conformidad previa del BCRA para el acceso al mercado de cambios para realizar pagos de importaciones por bienes con registro de ingreso aduanero hasta el 12/12/23, excepto cuando, adicionalmente a los restantes requisitos aplicables, la entidad verifique que:
> *propio:* 10.11.3. el cliente cuenta por el equivalente al monto a pagar con una "Certificación por los regímenes de acceso a divisas para la producción incremental de petróleo y/o gas natural (Decreto 277/22)" emitida en el marco de lo dispuesto en el punto 3.17.; o

- Estado final: `completo_ok_directo`; rechazos: 0
- **c1 Condicion** «Cliente cuenta con Certificación regímenes acceso divisas» — El cliente cuenta con una Certificación por los regímenes de acceso a divisas para la producción incremental de petróleo y/o gas natural (Decreto 277/22) emitida conforme al punto 3.17, por el equivalente al monto a pagar. · tramo: «el cliente cuenta por el equivalente al monto a pagar con una "Certificación por los regímenes de acceso a divisas para la producción incremental de petróleo y/o gas natural (Decreto 277/22)" emitida en el marco de lo dispuesto en el punto 3.17.»
- **com1 Comunicacion** «Decreto 277/22» —  · props: `{"codigo": "Decreto 277/22", "tipo": "externa"}` · tramo: «Decreto 277/22»
- R: to TextoOrdenado «Texto Ordenado Exterior Cambios» —referencia→ com1 Comunicacion «Decreto 277/22»
- Omisión `relacion_sin_predicado`: «emitida en el marco de lo dispuesto en el punto 3.17» — remisión a otro punto del TO; no se emite como relación entre entidades del chunk

- **Lectura:** Condicion sin norma ni cuantificador

## `ext::10.11.4` (ítem) — propuesta: **no_cumple**

> *heredado:* Sección 10. Pagos de importaciones y otras compras de bienes en el exterior.
> *heredado:* 10.11. Disposiciones complementarias para importaciones de bienes con registro de ingreso
> *heredado:* aduanero hasta el 12/12/23. Se requerirá la conformidad previa del BCRA para el acceso al mercado de cambios para realizar pagos de importaciones por bienes con registro de ingreso aduanero hasta el 12/12/23, excepto cuando, adicionalmente a los restantes requisitos aplicables, la entidad verifique que:
> *propio:* 10.11.4. el pago es concretado mediante la realización de un canje y/o arbitraje con los fondos depositados en una cuenta local y originados en cobros de capital e intereses en moneda extranjera de los Bonos para la Reconstrucción de una Argentina Libre (BOPREAL); o

- Estado final: `completo_ok_directo`; rechazos: 1
- **c1 Condicion** «Pago mediante canje y/o arbitraje con fondos BOPREAL» — El pago se realiza mediante canje y/o arbitraje con fondos depositados en cuenta local, originados en cobros de capital e intereses en moneda extranjera de BOPREAL · tramo: «el pago es concretado mediante la realización de un canje y/o arbitraje con los fondos depositados en una cuenta local y originados en cobros de capital e intereses en moneda extranjera de los Bonos para la Reconstrucción de una Argentina Libre (BOPREAL)»
- Omisión `relacion_sin_predicado`: «Se requerirá la conformidad previa del BCRA para el acceso al mercado de cambios para realizar pagos de importaciones por bienes con registro de ingreso aduanero hasta el 12/12/23, excepto cuando, adicionalmente a los restantes requisitos aplicables, la entidad verifique que:» — La relación entre la Obligacion (requerimiento de conformidad previa del BCRA) y la Condicion (verificación de que el pago se realiza mediante canje/arbitraje con fondos BOPREAL) no tiene predicado que la represente en el schema. El texto enuncia que la obligación NO aplica cuando se verifica la condición, pero eso es una Excepcion de la Obligacion, que está en el contexto heredado (punto 10.11), no en esta unidad.

- **Lectura:** Condicion sin norma ni cuantificador

## `ext::10.11.5` (ítem) — propuesta: **no_cumple**

> *heredado:* Sección 10. Pagos de importaciones y otras compras de bienes en el exterior.
> *heredado:* 10.11. Disposiciones complementarias para importaciones de bienes con registro de ingreso
> *heredado:* aduanero hasta el 12/12/23. Se requerirá la conformidad previa del BCRA para el acceso al mercado de cambios para realizar pagos de importaciones por bienes con registro de ingreso aduanero hasta el 12/12/23, excepto cuando, adicionalmente a los restantes requisitos aplicables, la entidad verifique que:
> *propio:* 10.11.5. el pago es concretado en el marco de lo dispuesto en el punto 4.8.4. por un cliente que suscribió BOPREAL Serie 1 por un monto igual o mayor al 50% (cincuenta por ciento) del total pendiente por sus deudas elegibles para los puntos 4.4. y 4.5. con anterioridad al 31/01/24; o

- Estado final: `aceptado_con_residuales`; rechazos: 0
- **c1 Condicion** «Pago en marco punto 4.8.4» — El pago debe ser concretado en el marco de lo dispuesto en el punto 4.8.4. · tramo: «el pago es concretado en el marco de lo dispuesto en el punto 4.8.4.»
- **c2 Condicion** «Cliente suscribió BOPREAL Serie 1 mínimo 50%» — El cliente debe haber suscrito BOPREAL Serie 1 por un monto igual o mayor al 50% del total pendiente por sus deudas elegibles para los puntos 4.4. y 4.5., con anterioridad al 31/01/24. · umbral: ['igual o mayor al 50% (cincuenta por ciento)', 'con anterioridad al 31/01/24'] · tramo: «un cliente que suscribió BOPREAL Serie 1 por un monto igual o mayor al 50% (cincuenta por ciento) del total pendiente por sus deudas elegibles para los puntos 4.4. y 4.5. con anterioridad al 31/01/24»
- **op1 Operacion** «Pago de importación de bien con registro aduanero» — Pago de importación de bienes con registro de ingreso aduanero hasta el 12/12/23, concretado en el marco del punto 4.8.4., por un cliente que suscribió BOPREAL Serie 1 por monto igual o mayor al 50% del total pendiente por deudas elegibles. · props: `{"tipo": "pago de importación"}` · tramo: «el pago es concretado en el marco de lo dispuesto en el punto 4.8.4. por un cliente que suscribió BOPREAL Serie 1 por un monto igual o mayor al 50% (cincuenta por ciento) del total pendiente por sus deudas elegibles para los puntos 4.4. y 4.5. con anterioridad al 31/01/24»
- R: c1 Condicion «Pago en marco punto 4.8.4» —condicion_de→ op1 Operacion «Pago de importación de bien con registro aduanero»
- R: c2 Condicion «Cliente suscribió BOPREAL Serie 1 mínimo 50%» —condicion_de→ op1 Operacion «Pago de importación de bien con registro aduanero»
- R: op1 Operacion «Pago de importación de bien con registro aduanero» —aplica_a→ Sujeto_propuesto_un_cliente (mención «un cliente», exacta)
- Omisión `meta_normativo`: «excepto cuando, adicionalmente a los restantes requisitos aplicables, la entidad verifique que:» — Cláusula introductoria que anuncia la excepción a la regla de conformidad previa del BCRA; el contenido sustantivo está en los ítems de la lista (punto 10.11.5 es uno de ellos). La excepción se compone en cada ítem con su contenido específico.

- **Lectura:** Condicion sin norma ni cuantificador

## `ext::10.11.6` (ítem) — propuesta: **no_cumple**

> *heredado:* Sección 10. Pagos de importaciones y otras compras de bienes en el exterior.
> *heredado:* 10.11. Disposiciones complementarias para importaciones de bienes con registro de ingreso
> *heredado:* aduanero hasta el 12/12/23. Se requerirá la conformidad previa del BCRA para el acceso al mercado de cambios para realizar pagos de importaciones por bienes con registro de ingreso aduanero hasta el 12/12/23, excepto cuando, adicionalmente a los restantes requisitos aplicables, la entidad verifique que:
> *propio:* 10.11.6. el pago es concretado en el marco de lo dispuesto en el punto 4.8.5. por un cliente que suscribió BOPREAL Serie 1 por un monto igual o mayor al 25% (veinticinco por ciento) del total pendiente por sus deudas elegibles para los puntos 4.4. y 4.5. con anterioridad al 31/01/24; o

- Estado final: `aceptado_con_residuales`; rechazos: 0
- **c1 Condicion** «Pago en marco punto 4.8.5» — El pago debe ser concretado en el marco de lo dispuesto en el punto 4.8.5. · tramo: «el pago es concretado en el marco de lo dispuesto en el punto 4.8.5.»
- **c2 Condicion** «Cliente suscribió BOPREAL Serie 1 mínimo 25%» — El cliente debe haber suscrito BOPREAL Serie 1 por un monto igual o mayor al 25% del total pendiente por sus deudas elegibles para los puntos 4.4. y 4.5., con anterioridad al 31/01/24. · umbral: ['igual o mayor al 25% (veinticinco por ciento)'] · tramo: «cliente que suscribió BOPREAL Serie 1 por un monto igual o mayor al 25% (veinticinco por ciento) del total pendiente por sus deudas elegibles para los puntos 4.4. y 4.5. con anterioridad al 31/01/24»
- **op1 Operacion** «Pago de importación de bien con registro aduanero» — Pago de importación de bienes con registro de ingreso aduanero hasta el 12/12/23, realizado por un cliente que suscribió BOPREAL Serie 1 por monto igual o mayor al 25% del total pendiente por deudas elegibles, con anterioridad al 31/01/24. · props: `{"tipo": "pago de importación"}` · tramo: «el pago es concretado en el marco de lo dispuesto en el punto 4.8.5. por un cliente que suscribió BOPREAL Serie 1 por un monto igual o mayor al 25% (veinticinco por ciento) del total pendiente por sus deudas elegibles para los puntos 4.4. y 4.5. con anterioridad al 31/01/24»
- R: c1 Condicion «Pago en marco punto 4.8.5» —condicion_de→ op1 Operacion «Pago de importación de bien con registro aduanero»
- R: c2 Condicion «Cliente suscribió BOPREAL Serie 1 mínimo 25%» —condicion_de→ op1 Operacion «Pago de importación de bien con registro aduanero»
- Omisión `relacion_sin_predicado`: «Se requerirá la conformidad previa del BCRA para el acceso al mercado de cambios para realizar pagos de importaciones por bienes con registro de ingreso aduanero hasta el 12/12/23, excepto cuando, adicionalmente a los restantes requisitos aplicables, la entidad verifique que:» — La relación entre la excepción a la conformidad previa del BCRA (enunciada en el encabezado del punto 10.11) y las condiciones del ítem 10.11.6 no tiene predicado que la represente. El encabezado enuncia una Excepcion a una Obligacion (requerimiento de conformidad previa), y el ítem 10.11.6 enuncia las condiciones de esa excepción, pero la relación entre la Excepcion y sus Condiciones no está en los 13 predicados disponibles.

- **Lectura:** Condicion sin norma ni cuantificador

## `ext::10.11.7::intro` (ítem) — propuesta: **no_cumple**

> *heredado:* Sección 10. Pagos de importaciones y otras compras de bienes en el exterior.
> *heredado:* 10.11. Disposiciones complementarias para importaciones de bienes con registro de ingreso
> *heredado:* 10.11.7. el pago es concretado por una persona humana o una persona jurídica que
> *propio:* clasifique como MiPyMe según lo dispuesto en las normas de "Determinación de la condición de micro, pequeña y mediana empresa" y se cumple la totalidad de las siguientes condiciones:.

- Estado final: `aceptado_tras_reintento`; rechazos: 0
- **c1 Condicion** «Pagador es persona humana o jurídica MiPyMe» — El pagador debe ser una persona humana o una persona jurídica que califique como MiPyMe conforme a las normas de determinación de esa condición · tramo: «el pago es concretado por una persona humana o una persona jurídica que clasifique como MiPyMe según lo dispuesto en las normas de "Determinación de la condición de micro, pequeña y mediana empresa"»
- **c2 Condicion** «Se cumplen todas las condiciones siguientes» — Deben cumplirse todas las condiciones que se enumeran a continuación · tramo: «se cumple la totalidad de las siguientes condiciones»

- **Lectura:** Condicion del supuesto (MiPyMe) y una del cuantificador de su sublista; sin la norma exceptuada

