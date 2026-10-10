# U-CONF-MATRIZ, C2-bis: lista para la revisión de la autora (C4)

Planilla nueva sellada (`abfde990d566533e7a78b21022b6564c466d6b8d24c92a611b49df135203e5b6`). Entran: las incorrectas y las no decidibles de la lectura nueva, 5 correctas por par con la semilla sellada en la nota del mandato, y toda ficha en la que las dos lecturas no coinciden. La primera lectura se muestra solo en las discrepancias. El texto de cada unidad está en `fichas_c1.md` y las páginas, en la carpeta del lector.


## → Operacion

C3: 26 correctas, 4 incorrectas, 0 no decidibles, de 30; límite inferior de Wilson al 95 % 0.7032; no confirma con el criterio del §2 (antes de C4).


### Incorrectas (4)

#### F27 — → Operacion
- **Origen:** Condicion «Cobros ingresados por sistema de monedas locales» — Supuesto en que los cobros de exportación de servicios se ingresan a través del sistema de monedas locales
- **Destino:** Operacion «Ingreso de cobros por sistema de monedas locales» — Ingreso de cobros de exportaciones de servicios a través del sistema de monedas locales. Se considera cumplimentada la liquidación por el monto acreditado en moneda nacional en la cuenta del exportador.
- **Tramos de E1:** origen 'En el caso de que los cobros sean ingresados a través del sistema de monedas locales'; destino 'los cobros sean ingresados a través del sistema de monedas locales'
- **Unidad:** `ext::2.2.3`, páginas [11]; render en la carpeta del lector: paginas/ext_p11.png
- **Lectura nueva:** `incorrecta` — El destino, por etiqueta y tramo, es el mismo supuesto que el origen ("los cobros sean ingresados a través del sistema de monedas locales"): la arista relaciona el supuesto consigo mismo. En el texto, el consecuente de ese supuesto es que "se considerará cumplimentada la liquidación por el monto acreditado en moneda nacional", y el nodo destino solo lo menciona en su descripción.
- **Primera lectura (contaminada, no decide):** `correcta` — 2.2.3: «En el caso de que los cobros sean ingresados a través del sistema de monedas locales se considerará cumplimentada la liquidación por el monto acreditado en moneda nacional». El supuesto (ingreso por el sistema de monedas locales) es antecedente del tratamiento que el destino describe («Se considera cumplimentada la liquidación por el monto acreditado…», en su descripción). Anotación: el destino tiene el mismo tramo que la Condicion, así que por etiqueta y tramo la arista es circular; leído por etiqueta, descripción y tramo, la relación es cierta. Con una lectura estricta del nodo por su etiqueta sería incorrecta: queda para la adjudicación.
- **Adjudicación de la autora:** 

#### F45 — → Operacion
- **Origen:** Condicion «Falta de autorización para girar en descubierto» — Supuesto de inclusión en la Central de cheques rechazados: falta de autorización para girar en descubierto
- **Destino:** Operacion «Rechazo de cheques por falta de fondos o autorización» — Rechazo de cheques comunes o de pago diferido por falta de fondos suficientes disponibles en cuenta o por falta de autorización para girar en descubierto
- **Tramos de E1:** origen 'falta de autorización para girar en descubierto'; destino 'rechazos de cheques -comunes o de pago diferido- por: [...] Falta de fondos suficientes disponibles en cuenta o de autorización para girar en descubierto'
- **Unidad:** `ctacte::8.2.1.1`, páginas [44]; render en la carpeta del lector: paginas/ctacte_p44.png
- **Lectura nueva:** `incorrecta` — El origen (falta de autorización para girar en descubierto) es el motivo que define al propio destino ("rechazos de cheques ... por falta de fondos suficientes ... o de autorización para girar en descubierto"): la relación es de parte a todo, no de condición. En el texto, el rechazo por ese motivo es lo que habilita la inclusión en la "Central de cheques rechazados" (8.2.1, motivos de inclusión); el fragmento no regula cuándo se rechaza un cheque.
- **Primera lectura (contaminada, no decide):** `correcta` — 8.2.1 y 8.2.1.1: motivo de inclusión en la Central, «Haber incurrido en uno o varios rechazos de cheques […] por: Falta de fondos suficientes disponibles en cuenta o de autorización para girar en descubierto». La falta de autorización es la causa del rechazo y el texto la enuncia como tal. Anotación: el consecuente que regula el texto es la inclusión en la Central, que no es nodo de la arista; la Condicion toma solo uno de los dos términos («fondos» o «autorización»).
- **Adjudicación de la autora:** 

#### F15 — → Operacion
- **Origen:** Condicion «Plazo según proporción — bienes mixtos» — Cuando un pago anticipado incluye tanto bienes de capital como otros bienes, se aplica el plazo del tipo de bien que represente mayor proporción del valor total abonado
- **Destino:** Operacion «Acceso al mercado de cambios para pago anticipado» — Acceso al mercado de cambios para el pago al exterior de importaciones con registro de ingreso aduanero pendiente
- **Tramos de E1:** origen 'En el caso de que un mismo pago anticipado incluya bienes de capital y bienes que no lo son, la operación se regirá por el plazo del tipo de bien que represente una mayor proporción del valor total abonado'; destino 'dar acceso al mercado de cambios para el pago al exterior'
- **Unidad:** `ext::10.4.2.4`, páginas [139, 140]; render en la carpeta del lector: paginas/ext_p139.png, paginas/ext_p140.png
- **Lectura nueva:** `incorrecta` — El párrafo establece qué plazo rige cuando un mismo pago anticipado incluye bienes de capital y otros bienes (el del tipo de bien de mayor proporción); ese plazo integra el compromiso de la declaración jurada del punto 10.4.2.4. El texto no condiciona el acceso al mercado de cambios a ese supuesto: el antecedente "pago mixto" gobierna la determinación del plazo, no el acceso. El nodo es una regla de cómputo de plazo, no un antecedente del destino.
- **Adjudicación de la autora:** 

#### F34 — → Operacion
- **Origen:** Condicion «Servicios a residentes paraguayos o uruguayos en moneda de destino» — Supuesto en que se trata de servicios prestados a residentes paraguayos o uruguayos facturados en la moneda del país de destino de la exportación
- **Destino:** Operacion «Ingreso de cobros servicios a residentes paraguayos o uruguayos» — Ingreso de cobros de servicios prestados a residentes paraguayos o uruguayos facturados en la moneda del país de destino de la exportación. Se computa el equivalente en dicha moneda del monto acreditado.
- **Tramos de E1:** origen 'En caso de que se trate de servicios prestados a residentes paraguayos o uruguayos facturados en la moneda del país de destino de la exportación'; destino 'servicios prestados a residentes paraguayos o uruguayos facturados en la moneda del país de destino de la exportación'
- **Unidad:** `ext::2.2.3`, páginas [11]; render en la carpeta del lector: paginas/ext_p11.png
- **Lectura nueva:** `incorrecta` — El destino, por etiqueta y tramo, es el mismo supuesto que el origen ("servicios prestados a residentes paraguayos o uruguayos facturados en la moneda del país de destino de la exportación"): la arista relaciona el supuesto consigo mismo. En el texto, el consecuente de ese supuesto es que "se computará el equivalente en dicha moneda del monto acreditado", y el nodo destino solo lo menciona en su descripción.
- **Primera lectura (contaminada, no decide):** `correcta` — 2.2.3: «En caso de que se trate de servicios prestados a residentes paraguayos o uruguayos facturados en la moneda del país de destino de la exportación se computará el equivalente en dicha moneda del monto acreditado». El supuesto es antecedente del tratamiento que el destino describe («Se computa el equivalente en dicha moneda del monto acreditado», en su descripción). Anotación: mismo tramo en la Condicion y en el destino (circular por etiqueta y tramo), mismo patrón y misma unidad que otra ficha de la muestra; con una lectura estricta del nodo por su etiqueta sería incorrecta: queda para la adjudicación.
- **Adjudicación de la autora:** 


### No decidibles (0)

(ninguna)


### Correctas sorteadas (semilla 4532495010434239514) (5)

#### F04 — → Operacion
- **Origen:** Condicion «Elegibilidad para mecanismo de cobros de exportación» — Los cobros deben resultar elegibles para el mecanismo previsto en el punto 7.10.3
- **Destino:** Operacion «Depósito de cobros de exportación en cuentas corresponsales» — Depósito de cobros de exportación de bienes elegibles para el mecanismo del punto, no aplicados simultáneamente a usos admitidos, en cuentas corresponsales en el exterior de entidades financieras locales y/o en cuentas locales en moneda extranjera de entidades financieras locales, hasta su aplicación
- **Tramos de E1:** origen 'que resulten elegibles para el mecanismo previsto en este punto'; destino 'Los cobros de exportación de bienes recibidos por un exportador que resulten elegibles para el mecanismo previsto en este punto y no sean aplicados simultáneamente a los usos admitidos podrán quedar depositados hasta su aplicación en las cuentas corresponsales en el exterior de entidades financieras locales y/o en cuentas locales en moneda extranjera de entidades financieras locales'
- **Unidad:** `ext::7.10.3`, páginas [102]; render en la carpeta del lector: paginas/ext_p99.png, paginas/ext_p102.png
- **Lectura nueva:** `correcta` — (sin nota)
- **Adjudicación de la autora:** 

#### F19 — → Operacion
- **Origen:** Condicion «Elegibilidad según punto 4.5» — La operación debe resultar elegible de acuerdo con lo dispuesto en el punto 4.5
- **Destino:** Operacion «Pago deudas comerciales importaciones servicios» — Pago de deudas comerciales por importaciones de servicios prestados o devengados hasta el 12/12/23, que resultaban elegibles de acuerdo con lo dispuesto en el punto 4.5
- **Tramos de E1:** origen 'que resultaban elegibles de acuerdo con lo dispuesto en el punto 4.5'; destino 'el pago de deudas comerciales por importaciones de servicios prestados o devengados hasta el 12/12/23'
- **Unidad:** `ext::4.8.1.2`, páginas [64]; render en la carpeta del lector: paginas/ext_p64.png, paginas/ext_p65.png
- **Lectura nueva:** `correcta` — (sin nota)
- **Adjudicación de la autora:** 

#### F23 — → Operacion
- **Origen:** Condicion «Residentes no autorizados a operar en cambios» — La operación se aplica a residentes que no sean entidades autorizadas a operar en cambios
- **Destino:** Operacion «Operaciones derivados financieros — residentes no autorizados» — Operaciones de derivados financieros cursadas con acceso al mercado de cambios por residentes que no sean entidades autorizadas a operar en cambios
- **Tramos de E1:** origen 'residentes que no sean entidades autorizadas a operar en cambios'; destino 'Las restantes operaciones de derivados financieros que quieran ser cursadas con acceso al mercado de cambios por parte de residentes que no sean entidades autorizadas a operar en cambios'
- **Unidad:** `ext::3.12.2`, páginas [36]; render en la carpeta del lector: paginas/ext_p16.png, paginas/ext_p36.png
- **Lectura nueva:** `correcta` — (sin nota) · anotaciones: Nodo mal tipado: es un sujeto que delimita el ámbito de la regla (residentes que no son entidades autorizadas), no una condición en sentido estricto, y ya está contenido en la etiqueta del destino. El texto sí restringe el régimen de 3.12.2 a las operaciones de esos residentes.
- **Adjudicación de la autora:** 

#### F38 — → Operacion
- **Origen:** Condicion «Vinculación a falta de pago» — La demanda se encuentra vinculada a la falta de pago
- **Destino:** Operacion «Clasificación de deudor con problemas» — Clasificación del cliente en la categoría 'Con problemas' cuando ha sido demandado judicialmente por cobro de acreencia vinculada a falta de pago con mora no superior a 180 días
- **Tramos de E1:** origen 'cuando ello se encuentre vinculado a la falta de pago'; destino 'Haya sido demandado judicialmente por la entidad para el cobro de su acreencia, cuando ello se encuentre vinculado a la falta de pago y registre mora en el pago de las obligaciones no superior a 180 días'
- **Unidad:** `cla::6.5.3.11`, páginas [25]; render en la carpeta del lector: paginas/cla_p19.png, paginas/cla_p23.png, paginas/cla_p25.png
- **Lectura nueva:** `correcta` — (sin nota) · anotaciones: La vinculación con la falta de pago califica al indicador 6.5.3.11 (demanda judicial), que es uno de los indicadores que "pueden reflejar" la situación "con problemas"; la intro de 6.5 los trata como condiciones de cada categoría. El nodo recoge solo uno de los requisitos del indicador (falta la mora no superior a 180 días).
- **Adjudicación de la autora:** 

#### F44 — → Operacion
- **Origen:** Condicion «Posiciones arancelarias no comprendidas en punto 12.1» — Las posiciones arancelarias de los bienes no deben corresponder a aquellas comprendidas en el punto 12.1
- **Destino:** Operacion «Pagos a la vista — importaciones de bienes» — Pagos a la vista de importaciones de bienes cursados por personas humanas o personas jurídicas que clasifiquen como MiPyMe según lo dispuesto en las normas de 'Determinación de la condición de micro, pequeña y mediana empresa'
- **Tramos de E1:** origen 'las posiciones arancelarias de los bienes no correspondan a aquellas comprendidas en el punto 12.1'; destino 'Pagos a la vista de importaciones de bienes cursados por personas humanas o personas jurídicas que clasifiquen como MiPyMe'
- **Unidad:** `ext::10.10.2.1`, páginas [154]; render en la carpeta del lector: paginas/ext_p154.png, paginas/ext_p157.png
- **Lectura nueva:** `correcta` — (sin nota)
- **Adjudicación de la autora:** 


## → Potestad

C3: 29 correctas, 1 incorrectas, 0 no decidibles, de 30; límite inferior de Wilson al 95 % 0.8333; confirma con el criterio del §2 (antes de C4).


### Incorrectas (1)

#### F57 — → Potestad
- **Origen:** Condicion «Garantías preferidas — condición indiferente» — Que las financiaciones cuenten o no con garantías preferidas (condición indiferente para el ejercicio de la opción)
- **Destino:** Potestad «Opción de agrupar financiaciones comerciales» — Facultad de agrupar las financiaciones de naturaleza comercial de hasta el equivalente a dos veces el importe de referencia establecido en el punto 3.7., con o sin garantías preferidas, junto con los créditos para consumo o vivienda, en el manual de procedimientos de clasificación y previsión
- **Tramos de E1:** origen 'cuenten o no con garantías preferidas'; destino 'El ejercicio de la opción de agrupar las financiaciones de naturaleza comercial de hasta el equivalente a dos veces el importe de referencia establecido en el punto 3.7., cuenten o no con garantías preferidas, junto con los créditos para consumo o vivienda'
- **Unidad:** `cla::3.3.3`, páginas [9]; render en la carpeta del lector: paginas/cla_p9.png, paginas/cla_p10.png
- **Lectura nueva:** `incorrecta` — "Cuenten o no con garantías preferidas" expresa que la existencia de garantías preferidas es indiferente para la opción de agrupar: el texto descarta que sea antecedente, no lo establece. Además, la unidad 3.3.3 solo enumera un contenido del "Manual de procedimientos de clasificación y previsión" y no regula las condiciones de la opción.
- **Adjudicación de la autora:** 


### No decidibles (0)

(ninguna)


### Correctas sorteadas (semilla 2215609819628898327) (5)

#### F01 — → Potestad
- **Origen:** Condicion «Cancelación total de intereses devengados» — Supuesto en que deudores han cancelado la totalidad de los intereses devengados
- **Destino:** Potestad «Clasificación en situación normal si se cumplen condiciones» — Facultad de clasificar deudores en situación normal si han cancelado totalidad de intereses devengados y observan otras condiciones de esa categoría
- **Tramos de E1:** origen 'Los deudores que hayan cancelado la totalidad de los intereses devengados'; destino 'podrán ser clasificados en "situación normal" si además observan las otras condiciones previstas para esa categoría'
- **Unidad:** `cla::6.5.2.2`, páginas [22, 23]; render en la carpeta del lector: paginas/cla_p19.png, paginas/cla_p22.png, paginas/cla_p23.png
- **Lectura nueva:** `correcta` — (sin nota)
- **Adjudicación de la autora:** 

#### F12 — → Potestad
- **Origen:** Condicion «Contraparte en operaciones de arbitraje y canje» — La operación de arbitraje o canje en el exterior solo puede realizarse cuando la contraparte reúne determinadas características (que se especifican en los ítems siguientes)
- **Destino:** Potestad «Facultad realizar arbitrajes y canjes en exterior» — Las entidades autorizadas quedan facultadas a realizar operaciones de arbitrajes y canjes en el exterior
- **Tramos de E1:** origen 'siempre que la contraparte sea:'; destino 'Dichas entidades podrán realizar operaciones de arbitrajes y canjes en el exterior'
- **Unidad:** `ext::5.12::intro`, páginas [73]; render en la carpeta del lector: paginas/ext_p73.png
- **Lectura nueva:** `correcta` — (sin nota) · anotaciones: El nodo origen solo enuncia el requisito ("siempre que la contraparte sea:"); el contenido de la condición está en las alternativas 5.12.1 a 5.12.4, fuera de la unidad. La relación es cierta.
- **Adjudicación de la autora:** 

#### F30 — → Potestad
- **Origen:** Condicion «Permiso embarque definitivo asociado a embarque provisorio anterior» — Supuesto en que un permiso de embarque definitivo está asociado a un embarque provisorio oficializado antes del 2 de septiembre de 2019
- **Destino:** Potestad «Facultad de dar cumplido de embarque definitivo» — Las entidades quedan facultadas a dar el cumplido de embarque del permiso de embarque definitivo cuando se verifica el supuesto de asociación con embarque provisorio anterior
- **Tramos de E1:** origen 'En caso de que un permiso de embarque definitivo esté asociado a un embarque provisorio oficializado con anterioridad al 02/09/19'; destino 'las entidades podrán dar el cumplido de embarque del permiso definitivo'
- **Unidad:** `ext::7.8.2.5`, páginas [92]; render en la carpeta del lector: paginas/ext_p91.png, paginas/ext_p92.png
- **Lectura nueva:** `correcta` — (sin nota)
- **Adjudicación de la autora:** 

#### F32 — → Potestad
- **Origen:** Condicion «Monto pendiente prefinanciado en su totalidad» — Condición: el monto pendiente de ingreso ha sido prefinanciado en su totalidad y los fondos han sido liquidados en el mercado de cambios en concepto de prefinanciaciones de exportaciones locales y/o del exterior.
- **Destino:** Potestad «Extensión del plazo para liquidación de divisas — prefinanciación total» — La entidad encargada del seguimiento del permiso podrá extender el plazo para la liquidación de divisas del embarque hasta la fecha de vencimiento de la financiación dada al comprador, cuando el monto pendiente haya sido prefinanciado en su totalidad.
- **Tramos de E1:** origen 'Cuando el monto pendiente de ingreso de las operaciones haya sido prefinanciado en su totalidad y los fondos liquidados en el mercado de cambios en concepto de prefinanciaciones de exportaciones locales y/o del exterior'; destino 'se podrá extender el plazo para la liquidación de divisas del embarque hasta la fecha de vencimiento de la correspondiente financiación dada al comprador'
- **Unidad:** `ext::7.5.2`, páginas [86, 87]; render en la carpeta del lector: paginas/ext_p86.png, paginas/ext_p87.png
- **Lectura nueva:** `correcta` — (sin nota)
- **Adjudicación de la autora:** 

#### F50 — → Potestad
- **Origen:** Condicion «Condición para extensión: utilización del mecanismo y fondos depositados» — Se requiere que el cliente haya utilizado este mecanismo para el monto pendiente de liquidación y que los fondos sigan depositados en la Cuenta especial para el régimen de fomento de la economía del conocimiento (Decreto 679/22) de su titularidad.
- **Destino:** Potestad «Extensión del plazo de liquidación del permiso» — La entidad encargada del seguimiento del permiso de embarque está facultada a extender el plazo de liquidación del permiso cuando el cliente haya utilizado este mecanismo para el monto pendiente de liquidación y los fondos sigan depositados en la Cuenta especial para el régimen de fomento de la economía del conocimiento (Decreto 679/22) de su titularidad.
- **Tramos de E1:** origen 'cuando, por el monto que se encuentre pendiente de liquidación, el cliente haya utilizado este mecanismo y los fondos sigan depositados en "Cuenta especial para el régimen de fomento de la economía del conocimiento. Decreto 679/22" de titularidad del cliente.'; destino 'la entidad encargada del seguimiento del permiso de embarque podrá extender el plazo de liquidación del permiso cuando, por el monto que se encuentre pendiente de liquidación, el cliente haya utilizado este mecanismo y los fondos sigan depositados en "Cuenta especial para el régimen de fomento de la economía del conocimiento. Decreto 679/22" de titularidad del cliente.'
- **Unidad:** `ext::7.8.4::cierre`, páginas [93]; render en la carpeta del lector: paginas/ext_p93.png
- **Lectura nueva:** `correcta` — (sin nota)
- **Adjudicación de la autora:** 


## Discrepancias con la primera lectura que no están arriba (0 de 3)

(ninguna)
