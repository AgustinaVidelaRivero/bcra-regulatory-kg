# U-LECTURA-ACEPTADAS, L1: las 60 fichas de la muestra sellada (sin veredicto)

Sello L0: `sellos_l0.json` (sha256 `640cb1f43ffdf64231fed185d64c8c8d4f2736ded2eed0404feb35ab7f06010a`), sorteo a las 2026-10-06T19:18:34-03:00; fichas generadas a las 2026-10-06T19:20:28-03:00. Grafo: KG-Tanda0-Diez-r2b-sincola (`e22fae1a…`). Criterio (mandato §1, el de T4): una unidad tiene error si al menos un nodo o una relación suya no se sostiene en el texto de la unidad (propio o heredado); las omisiones van aparte y no cuentan como error.

Clases de arista: **extraccion** (predicados que emite E1), **remision_derivada** (`remite_a`, la deriva el código desde el texto de E0), **catalogo_sujetos** (`padre_sugerido`) y **estructural** (`establecida_en` y las del esqueleto). Las remisiones se agrupan por origen y destino; el detalle de cada arista está en `fichas_l1.jsonl`.

## 1. `cap::5.4.5` — estrato item (1 del sorteo) · cap · págs. 114 · estado `completo_ok_directo`

Flags de E0: `{"formula": true, "evidencia_formula": ["P = P x (t – 0,25) / (T – 0,25)", "donde:"]}`

> *heredado (encabezado, S5):* Sección 5. Cobertura del riesgo de crédito.
> *heredado (chapeau_seccion, S5):* A los efectos del cómputo de la exigencia de capital por riesgo de crédito, se reconocerá –total o parcialmente– la cobertura del riesgo de crédito (CRC) de las operaciones registradas en la cartera de inversión –tales como préstamos y responsabilidades eventuales– mediante la utilización de las técnicas previstas en el punto 5.1. La presente sección contempla, además, el cálculo de la exposición a las operaciones de financia- ción con títulos valores (securities financing transactions, SFT) –conforme a lo previsto en la Sec- ción 4.–, registradas tanto en la cartera de inversión como en la cartera de negociación.
> *heredado (encabezado, 5.4):* 5.4. Operaciones cubiertas con garantías (y contragarantías) personales y derivados de crédito.
> *heredado (intro, 5.4):* Se aplicará el método de sustitución de ponderadores. Con este método, el ponderador de riesgo de la contraparte se sustituye por el ponderador de riesgo del garante –o contragarante– o proveedor de protección crediticia –conforme a la tabla de ponderadores prevista en la Sec- ción 2.–. Se reconocerán sólo las garantías emitidas –o protección provista, en el caso de derivados de crédito– por entidades listadas en el punto 5.4.1. La parte de la exposición sin cobertura mantendrá el ponderador de riesgo de la contraparte original, mientras que a la parte cubierta se le asignará el ponderador de riesgo del garante o proveedor de protección crediticia, teniendo en consideración lo siguiente:
> *propio:* 5.4.5. Descalce de plazos de vencimiento. El descalce de plazos tiene lugar cuando el plazo de vencimiento residual de la CRC es inferior al de la exposición subyacente; ambos plazos de vencimiento deberán medirse en forma conservadora. El plazo de vencimiento de la exposición subyacente se calculará como el mayor plazo de vencimiento restante posible antes de que la contraparte deba cumplir su obligación, teniendo en cuenta cualquier período de gracia aplicable. Con relación a la CRC, se de- berá tener en cuenta las opciones incorporadas que puedan reducir el plazo de venci- miento, a fin de utilizar el menor plazo de vencimiento posible. Cuando el proveedor de protección pueda solicitar anticipadamente la liquidación de la operación, el plazo de vencimiento será siempre el correspondiente a la primera fecha en la que pueda solicitar su liquidación. Si la solicitud de liquidación de la operación por anticipado está sujeta a la discrecionali- dad de la entidad financiera compradora de la protección, pero los términos del acuerdo contienen un incentivo positivo para que la entidad exija la liquidación de la operación antes del plazo de vencimiento establecido en el contrato, se considerará que el plazo de vencimiento es el tiempo restante hasta la primera fecha posible de liquidación. De haber descalce de plazos de vencimiento, la CRC que tenga un plazo de vencimien- to original inferior a un año o residual no mayor a tres meses no será reconocida. Cuan- do en estos casos sea factible el cómputo de la CRC su reconocimiento será parcial, aplicándose el siguiente ajuste: P = P x (t – 0,25) / (T – 0,25) a donde: P : valor de la CRC ajustado por descalce de plazos de vencimiento. a P: valor de la protección crediticia ajustada por cualquier aforo aplicable. t: mín. (T; plazo de vencimiento residual de la protección crediticia), expresado en años. T: mín. (5; plazo de vencimiento residual de la exposición), expresado en años.

**Nodos (9)**
- **N1** Condicion «Medición conservadora de plazos de vencimiento» — Los plazos de vencimiento de la CRC y de la exposición subyacente deben medirse en forma conservadora. · tramo (exacta): «ambos plazos de vencimiento deberán medirse en forma conservadora» · punto_propio
- **N2** Condicion «Plazo de vencimiento con incentivo positivo para liquidación anticipada» — Cuando hay incentivo positivo en el acuerdo para liquidación anticipada, el plazo de vencimiento es el tiempo restante hasta la primera fecha posible de liquidación. · tramo (exacta): «Si la solicitud de liquidación de la operación por anticipado está sujeta a la discrecionalidad de la entidad financiera compradora de la protección, pero los términos del acuerdo contienen un incentivo positivo para que la entidad exija la liquidación de la operación antes del plazo de vencimiento establecido en el contrato, se considerará que el plazo de vencimiento es el tiempo restante hasta la primera fecha posible de liquidación» · punto_propio
- **N3** Condicion «Plazo de vencimiento cuando hay liquidación anticipada» — Cuando el proveedor de protección puede solicitar liquidación anticipada, el plazo de vencimiento es el de la primera fecha posible de liquidación. · tramo (exacta): «Cuando el proveedor de protección pueda solicitar anticipadamente la liquidación de la operación, el plazo de vencimiento será siempre el correspondiente a la primera fecha en la que pueda solicitar su liquidación» · punto_propio
- **N4** Definicion «Descalce de plazos de vencimiento» — Situación en la que el plazo de vencimiento residual de la cobertura del riesgo de crédito (CRC) es inferior al de la exposición subyacente. · props: `{"termino": "Descalce de plazos de vencimiento"}` · tramo (exacta): «El descalce de plazos tiene lugar cuando el plazo de vencimiento residual de la CRC es inferior al de la exposición subyacente» · punto_propio
- **N5** Excepcion «Reconocimiento parcial de CRC con descalce de plazos» — Cuando sea factible el cómputo de la CRC con descalce de plazos, se reconoce parcialmente aplicando un ajuste de descalce de plazos de vencimiento. · tramo (exacta): «Cuando en estos casos sea factible el cómputo de la CRC su reconocimiento será parcial, aplicándose el siguiente ajuste» · punto_propio
- **N6** Operacion «Cálculo del plazo de vencimiento de la CRC» — Cálculo del plazo de vencimiento de la CRC considerando las opciones incorporadas que puedan reducir el plazo, utilizando el menor plazo de vencimiento posible. · props: `{"tipo": "calculo"}` · tramo (exacta): «Con relación a la CRC, se deberá tener en cuenta las opciones incorporadas que puedan reducir el plazo de vencimiento, a fin de utilizar el menor plazo de vencimiento posible» · punto_propio
- **N7** Operacion «Cálculo del plazo de vencimiento de la exposición subyacente» — Cálculo del plazo de vencimiento de la exposición subyacente como el mayor plazo de vencimiento restante posible antes de que la contraparte deba cumplir su obligación, considerando períodos de gracia aplicables. · props: `{"tipo": "calculo"}` · tramo (exacta): «El plazo de vencimiento de la exposición subyacente se calculará como el mayor plazo de vencimiento restante posible antes de que la contraparte deba cumplir su obligación, teniendo en cuenta cualquier período de gracia aplicable» · punto_propio
- **N8** Restriccion «No reconocimiento de CRC con descalce de plazos» — Cuando hay descalce de plazos de vencimiento, no se reconoce la CRC que tenga un plazo de vencimiento original inferior a un año o residual no mayor a tres meses. · props: `{"tipo": "prohibicion", "umbrales": [{"tramo": "un año", "valor": "1", "unidad": "anios", "comparacion": "maximo_estricto", "regla_comparacion": "simple:inferior", "origen": "e1", "tramo_verificado": "exacta"}, {"tramo": "tres meses", "valor": "3", "unidad": "meses", "comparacion": "maximo_inclusivo", "regla_comparacion": "negacion:mayor", "origen": "e1", "tramo_verificado": "exacta"}]}` · tramo (exacta): «De haber descalce de plazos de vencimiento, la CRC que tenga un plazo de vencimiento original inferior a un año o residual no mayor a tres meses no será reconocida» · punto_propio
- **N9** TextoOrdenado «Texto Ordenado Capitales Mínimos» · props: `{"archivo": "TO_capitales_minimos_actual.pdf", "materia": "Capitales mínimos de las entidades financieras", "version": "Comunicación A 8418 (vigencia 10/04/2026)"}` · sin tramo · punto_propio · compartido (453 procedencias en el grafo)

**Aristas de la extracción (1)**
- **A1** N5 —exceptua→ N8 Restriccion «No reconocimiento de CRC con descalce de plazos»

**Remisiones derivadas (0 aristas)**

**Estructurales (8)**: establecida_en → TextoOrdenado «Texto Ordenado Capitales Mínimos» ×8

## 2. `ext::3.17.3.4` — estrato item (2 del sorteo) · ext · págs. 52 · estado `aceptado_con_residuales`

> *heredado (encabezado, S3):* Sección 3. Disposiciones específicas para los egresos por el mercado de cambios
> *heredado (chapeau_seccion, S3):* Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–, adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables.
> *heredado (encabezado, 3.17):* 3.17. Acceso con “Certificación por los regímenes de acceso a divisas para la producción
> *heredado (intro, 3.17):* incremental de petróleo y/o gas natural (Decreto 277/22)”.
> *heredado (encabezado, 3.17.3):* 3.17.3. La entidad nominada deberá tomar registro de los montos de los beneficios
> *heredado (intro, 3.17.3):* reconocidos por la Secretaría de Energía en el marco del Decreto 277/22 a favor del cliente, dejando constancia del período al que corresponde el beneficio y el monto total del beneficio en dólares estadounidenses obtenido para el período. En el caso de que el cliente sea un beneficiario directo del Decreto 277/22, la entidad podrá emitir “certificaciones de los regímenes de acceso a divisas para la producción incremental de petróleo y/o gas natural (Decreto 277/22)” por hasta el monto que surge de considerar el monto acumulado de los beneficios totales reconocidos al cliente por la Secretaría de Energía neto de los montos acumulados por los conceptos detallados a continuación:
> *propio:* 3.17.3.4. el monto de las “Certificaciones de aumento de exportaciones de bienes”, emitidas a nombre del beneficiario en el marco del punto 3.18. a partir del 01/07/22.

**Nodos (4)**
- **N1** Condicion «Beneficiario directo del Decreto 277/22» — El cliente debe ser un beneficiario directo del Decreto 277/22 para que la entidad pueda emitir certificaciones · tramo (exacta): «En el caso de que el cliente sea un beneficiario directo del Decreto 277/22» · punto_propio
- **N2** Operacion «Emisión de Certificaciones de aumento de exportaciones» — Emisión de certificaciones de aumento de exportaciones de bienes a nombre del beneficiario en el marco del punto 3.18, a partir del 01/07/22 · props: `{"tipo": "emisión de certificación"}` · tramo (exacta): «Certificaciones de aumento de exportaciones de bienes» · punto_propio
- **N3** Restriccion «Límite cuantitativo — monto de Certificaciones de aumento de exportaciones» — El monto de las certificaciones de aumento de exportaciones de bienes emitidas debe considerarse como concepto a deducir del monto acumulado de beneficios totales reconocidos al cliente por la Secretaría de Energía, en el marco del Decreto 277/22 · props: `{"tipo": "limite_cuantitativo"}` · tramo (exacta): «el monto de las "Certificaciones de aumento de exportaciones de bienes", emitidas a nombre del beneficiario en el marco del punto 3.18. a partir del 01/07/22.» · punto_propio
- **N4** TextoOrdenado «Texto Ordenado Exterior Cambios» · props: `{"archivo": "TO_exterior_cambios_actual.pdf", "materia": "Exterior y cambios", "version": "Comunicación A 8307 (vigencia 26/08/2025)"}` · sin tramo · punto_propio · compartido (930 procedencias en el grafo)

**Aristas de la extracción (2)**
- **A1** N1 —condicion_de→ N3 Restriccion «Límite cuantitativo — monto de Certificaciones de aumento de exportaciones»
- **A2** N3 —limita→ N2 Operacion «Emisión de Certificaciones de aumento de exportaciones» [coherencia: coherente]

**Remisiones derivadas (0 aristas)**

**Estructurales (3)**: establecida_en → TextoOrdenado «Texto Ordenado Exterior Cambios» ×3

## 3. `pro::3.2.3.1` — estrato item (3 del sorteo) · pro · págs. 29 · estado `aceptado_con_residuales`

> *heredado (encabezado, S3):* Sección 3. Servicio de atención al usuario de servicios financieros.
> *heredado (chapeau_seccion, S3):* Los sujetos obligados deberán establecer este servicio para dar tratamiento y resolver las consul- tas y reclamos que presenten los usuarios de servicios financieros, observando las normas lega- les, reglamentarias y disposiciones vigentes en materia de protección al usuario de servicios finan- cieros, adoptando acciones que reduzcan su reiteración.
> *heredado (encabezado, 3.2):* 3.2. Controles.
> *heredado (encabezado, 3.2.3):* 3.2.3. Del Banco Central de la República Argentina.
> *heredado (intro, 3.2.3):* En la sede en la cual desempeñe sus funciones el responsable de atención al usuario de servicios financieros (titular o suplente a cargo) deberán encontrarse a disposición del BCRA:
> *propio:* 3.2.3.1. Acceso al Registro Centralizado de Consultas y Reclamos así como la docu- mentación respaldatoria de los trámites a que dieron lugar.

**Nodos (3)**
- **N1** Obligacion «Disponibilidad de acceso al Registro Centralizado» — Los sujetos obligados deberán mantener a disposición del BCRA el acceso al Registro Centralizado de Consultas y Reclamos, así como la documentación respaldatoria de los trámites a que dieron lugar. · props: `{"tipo": "otra"}` · tramo (no): «deberán encontrarse a disposición del BCRA: Acceso al Registro Centralizado de Consultas y Reclamos así como la documentación respaldatoria de los trámites a que dieron lugar» · punto_propio
- **N2** Sujeto «Sujetos obligados (Protección de usuarios)» · props: `{"nivel": "rol"}` · sin tramo · punto_propio · compartido (75 procedencias en el grafo)
- **N3** TextoOrdenado «Texto Ordenado Protección de Usuarios» · props: `{"archivo": "TO_proteccion_usuarios_servicios_financieros_actual.pdf", "materia": "Protección de los usuarios de servicios financieros", "version": "Comunicación A 8433 (vigencia 07/05/2026)"}` · sin tramo · punto_propio · compartido (99 procedencias en el grafo)

**Aristas de la extracción (1)**
- **A1** N1 —aplica_a→ N2 Sujeto «Sujetos obligados (Protección de usuarios)» (mención «los sujetos obligados», exacta, R4_sugerencia_modelo)

**Remisiones derivadas (0 aristas)**

**Estructurales (1)**: establecida_en → TextoOrdenado «Texto Ordenado Protección de Usuarios» ×1

## 4. `ext::3.5.6.9` — estrato item (4 del sorteo) · ext · págs. 27 · estado `aceptado_tras_reintento`

> *heredado (encabezado, S3):* Sección 3. Disposiciones específicas para los egresos por el mercado de cambios
> *heredado (chapeau_seccion, S3):* Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–, adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables.
> *heredado (encabezado, 3.5):* 3.5. Pagos de títulos de deuda suscriptos en el exterior y endeudamientos financieros con el
> *heredado (intro, 3.5):* exterior. Las entidades podrán dar acceso al mercado de cambios para realizar pagos de capital o intereses de títulos de deuda con registro público en el exterior, otros endeudamientos financieros con el exterior y títulos de deuda con registro público en el país denominados en moneda extranjera íntegramente suscriptos en el exterior, en la medida que se verifiquen las siguientes condiciones:
> *heredado (encabezado, 3.5.6):* 3.5.6. Se requerirá la conformidad previa del BCRA para el acceso al mercado de cambios
> *heredado (intro, 3.5.6):* para la cancelación de capital e intereses de endeudamientos financieros comprendidos en este punto 3.5. cuando el acreedor sea una contraparte vinculada al deudor. Este requisito no resultará aplicable cuando la operación encuadre en alguna de las siguientes situaciones:
> *heredado (cierre, 3.5.6):* Las deudas comprendidas en este punto continuarán sujetas a la conformidad previa aun cuando existiese una modificación del acreedor o del deudor que conlleve a que ya no exista una vinculación entre el acreedor y el deudor residente.
> *propio:* 3.5.6.9. el cliente cuente con una “Certificación de aumento de exportaciones de bienes” para los años 2021 a 2023 emitida en el marco de lo dispuesto en el punto 3.18. por el equivalente del monto de capital que se abona.

**Nodos (5)**
- **N1** Condicion «Condición — cliente con certificación aumento exportaciones» — Que el cliente cuente con una Certificación de aumento de exportaciones de bienes para los años 2021 a 2023 emitida en el marco de lo dispuesto en el punto 3.18. por el equivalente del monto de capital que se abona · props: `{"umbrales": [{"tramo": "para los años 2021 a 2023", "comparacion": "no_determinada", "regla_comparacion": "limite_relativo:sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}, {"tramo": "por el equivalente del monto de capital que se abona", "comparacion": "no_determinada", "regla_comparacion": "limite_relativo:sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}]}` · tramo (exacta): «el cliente cuente con una "Certificación de aumento de exportaciones de bienes" para los años 2021 a 2023 emitida en el marco de lo dispuesto en el punto 3.18. por el equivalente del monto de capital que se abona» · punto_propio
- **N2** Excepcion «Excepción conformidad previa — certificación aumento exportaciones» — No resultará aplicable el requisito de conformidad previa cuando el cliente cuente con una Certificación de aumento de exportaciones de bienes para los años 2021 a 2023 emitida en el marco de lo dispuesto en el punto 3.18. por el equivalente del monto de capital que se abona · props: `{"umbrales": [{"tramo": "para los años 2021 a 2023", "comparacion": "no_determinada", "regla_comparacion": "limite_relativo:sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}, {"tramo": "por el equivalente del monto de capital que se abona", "comparacion": "no_determinada", "regla_comparacion": "limite_relativo:sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}]}` · tramo (exacta): «el cliente cuente con una "Certificación de aumento de exportaciones de bienes" para los años 2021 a 2023 emitida en el marco de lo dispuesto en el punto 3.18. por el equivalente del monto de capital que se abona» · punto_propio
- **N3** Obligacion «Conformidad previa BCRA — acceso mercado cambios endeudamientos vinculados» — Se requerirá la conformidad previa del BCRA para el acceso al mercado de cambios para la cancelación de capital e intereses de endeudamientos financieros cuando el acreedor sea una contraparte vinculada al deudor · props: `{"tipo": "reporte_al_supervisor"}` · tramo (exacta): «Se requerirá la conformidad previa del BCRA para el acceso al mercado de cambios para la cancelación de capital e intereses de endeudamientos financieros comprendidos en este punto 3.5. cuando el acreedor sea una contraparte vinculada al deudor» · herencia_encabezado
- **N4** Operacion «Acceso mercado cambios — cancelación endeudamientos con contraparte vinculada» — Acceso al mercado de cambios para la cancelación de capital e intereses de endeudamientos financieros cuando el acreedor sea una contraparte vinculada al deudor · props: `{"tipo": "acceso al mercado de cambios"}` · tramo (exacta): «acceso al mercado de cambios para la cancelación de capital e intereses de endeudamientos financieros comprendidos en este punto 3.5. cuando el acreedor sea una contraparte vinculada al deudor» · herencia_encabezado
- **N5** TextoOrdenado «Texto Ordenado Exterior Cambios» · props: `{"archivo": "TO_exterior_cambios_actual.pdf", "materia": "Exterior y cambios", "version": "Comunicación A 8307 (vigencia 26/08/2025)"}` · sin tramo · punto_propio · compartido (930 procedencias en el grafo)

**Aristas de la extracción (3)**
- **A1** N1 —condicion_de→ N2 Excepcion «Excepción conformidad previa — certificación aumento exportaciones»
- **A2** N2 —exceptua_obligacion→ N3 Obligacion «Conformidad previa BCRA — acceso mercado cambios endeudamientos vinculados»
- **A3** N3 —regula→ N4 Operacion «Acceso mercado cambios — cancelación endeudamientos con contraparte vinculada»

**Remisiones derivadas (8 aristas)**
- **R1–R4** N3 —remite_a→ `ext::3.5` (interna; 4 nodo(s) destino: Condicion «Verificación de condiciones siguientes»; Operacion «Pago de títulos de deuda y endeudamientos financieros con el exterior»; Potestad «Acceso al mercado de cambios — pagos de títulos y endeudamientos»; Potestad «Acceso al mercado de cambios para pagos de títulos y endeudamientos») · evidencia «intereses de endeudamientos financieros comprendidos en este punto 3.5. cuando el acreedor»
- **R5–R8** N4 —remite_a→ `ext::3.5` (interna; 4 nodo(s) destino: Condicion «Verificación de condiciones siguientes»; Operacion «Pago de títulos de deuda y endeudamientos financieros con el exterior»; Potestad «Acceso al mercado de cambios — pagos de títulos y endeudamientos»; Potestad «Acceso al mercado de cambios para pagos de títulos y endeudamientos») · evidencia «intereses de endeudamientos financieros comprendidos en este punto 3.5. cuando el acreedor»

**Estructurales (4)**: establecida_en → TextoOrdenado «Texto Ordenado Exterior Cambios» ×4

## 5. `cla::6.5.4.4` — estrato item (5 del sorteo) · cla · págs. 26 · estado `completo_ok_directo`

> *heredado (encabezado, S6):* Sección 6. Clasificación de los deudores de la cartera comercial.
> *heredado (encabezado, 6.5):* 6.5. Niveles de clasificación.
> *heredado (intro, 6.5):* Cada cliente, y la totalidad de sus financiaciones comprendidas, se incluirá en una de las si- guientes cinco categorías, las que se definen teniendo en cuenta las condiciones que se deta- llan en cada caso. Los clientes que no registren asistencia crediticia de la entidad y que posteriormente reciban fi- nanciaciones de ésta que no superen el importe resultante de aplicar sobre el saldo de deuda registrado en el sistema financiero, según la última información disponible en la “Central de deudores” a la fecha de su otorgamiento, el porcentaje establecido en el punto 2.2.5. de las normas sobre “Previsiones mínimas por riesgo de incobrabilidad” correspondiente a la peor cla- sificación asignada, podrán ser clasificados por la entidad teniendo en cuenta únicamente el análisis del flujo de fondos proyectado. Las asistencias así otorgadas no serán consideradas a los fines a que se refiere el punto 6.6. A fin de verificar el cumplimiento de las obligaciones sin recurrir a nueva financiación directa o indirecta o a refinanciaciones, no se considerarán refinanciaciones las facilidades adicionales que se otorguen respecto de los márgenes vigentes acordados, siempre que el nuevo apoyo crediticio implique nuevos desembolsos de fondos y no supere el 10 % del cupo asignado en oportunidad de la última evaluación crediticia del cliente, en la medida en que éstas sean con- sistentes con el curso normal de los negocios y exista capacidad para atender el resto de las obligaciones financieras, ni las nuevas financiaciones y las refinanciaciones asociadas a una mayor inversión derivada de la expansión de las actividades, y siempre que pueda demostrarse que el flujo de fondos proyectado permitirá afrontar la totalidad de sus obligaciones. Tampoco se considerarán dentro de ese concepto las refinanciaciones otorgadas a los produc- tores agropecuarios cuando ello resulte de la aplicación de disposiciones vinculadas a la Ley de Emergencia Agropecuaria, sin perjuicio de lo cual, a los fines de la clasificación, deberá tenerse en cuenta el flujo de fondos proyectado para el momento en que concluya la vigencia de la emergencia declarada. El tratamiento que se dispense en ese marco no podrá implicar mejora- miento de la clasificación asignada al cliente en función de su situación individual, preexistente a la emergencia, ni su aplicación extenderse más allá de la vigencia fijada para ella.
> *heredado (encabezado, 6.5.4):* 6.5.4. Con alto riesgo de insolvencia.
> *heredado (intro, 6.5.4):* El análisis del flujo de fondos del cliente demuestra que es altamente improbable que pueda atender la totalidad de sus compromisos financieros. Entre los indicadores que pueden reflejar esta situación se destacan que el cliente:
> *propio:* 6.5.4.4. Tenga un sistema de información inadecuado, lo que impide conocer con exacti- tud la real situación financiera y económica de la empresa. La información que se presenta no es confiable pues no cuenta con la adecuada documentación respaldatoria. En general, la información no es consistente y no está actualizada.

**Nodos (4)**
- **N1** Condicion «Información inconsistente y desactualizada» — La información no es consistente y no está actualizada · tramo (exacta): «En general, la información no es consistente y no está actualizada» · punto_propio
- **N2** Condicion «Información no confiable sin documentación respaldatoria» — La información presentada no es confiable porque carece de documentación respaldatoria adecuada · tramo (exacta): «La información que se presenta no es confiable pues no cuenta con la adecuada documentación respaldatoria» · punto_propio
- **N3** Condicion «Sistema de información inadecuado» — El cliente tiene un sistema de información inadecuado que impide conocer con exactitud su real situación financiera y económica · tramo (exacta): «Tenga un sistema de información inadecuado, lo que impide conocer con exactitud la real situación financiera y económica de la empresa» · punto_propio
- **N4** TextoOrdenado «Texto Ordenado Clasificación de Deudores» · props: `{"archivo": "TO_clasificacion_deudores_actual.pdf", "materia": "Clasificación de deudores", "version": "Comunicación A 8378 (vigencia 20/12/2025)"}` · sin tramo · punto_propio · compartido (140 procedencias en el grafo)

**Aristas de la extracción (0)**

**Remisiones derivadas (0 aristas)**

**Estructurales (3)**: establecida_en → TextoOrdenado «Texto Ordenado Clasificación de Deudores» ×3

## 6. `ext::7.5.7.2` — estrato item (6 del sorteo) · ext · págs. 88 · estado `completo_ok_directo`

> *heredado (encabezado, S7):* Sección 7. Cobros de exportaciones de bienes.
> *heredado (encabezado, 7.5):* 7.5. Ampliaciones del plazo para el ingreso y liquidación de divisas.
> *heredado (intro, 7.5):* La entidad encargada del seguimiento del permiso podrá conceder extensiones en el plazo de ingreso y liquidación en las siguientes circunstancias:
> *heredado (encabezado, 7.5.7):* 7.5.7. Cobros encuadrados en la excepción de liquidación para los beneficiarios del régimen
> *heredado (intro, 7.5.7):* de fomento para las exportaciones de la economía del conocimiento. La entidad encargada del seguimiento podrá extender el plazo para la liquidación de un permiso de embarque en la medida que:
> *propio:* 7.5.7.2. los fondos sigan depositados en una “Cuenta especial para el régimen de fomento de la economía del conocimiento. Decreto Nº 679/22” de titularidad del cliente.

**Nodos (2)**
- **N1** Condicion «Fondos depositados en cuenta especial» — Los fondos deben mantenerse depositados en una Cuenta especial para el régimen de fomento de la economía del conocimiento (Decreto Nº 679/22) de titularidad del cliente · tramo (exacta): «los fondos sigan depositados en una "Cuenta especial para el régimen de fomento de la economía del conocimiento. Decreto Nº 679/22" de titularidad del cliente» · punto_propio
- **N2** TextoOrdenado «Texto Ordenado Exterior Cambios» · props: `{"archivo": "TO_exterior_cambios_actual.pdf", "materia": "Exterior y cambios", "version": "Comunicación A 8307 (vigencia 26/08/2025)"}` · sin tramo · punto_propio · compartido (930 procedencias en el grafo)

**Aristas de la extracción (0)**

**Remisiones derivadas (0 aristas)**

**Estructurales (1)**: establecida_en → TextoOrdenado «Texto Ordenado Exterior Cambios» ×1

## 7. `cap::2.11.3.2` — estrato item (7 del sorteo) · cap · págs. 21 · estado `completo_ok_directo`

> *heredado (encabezado, S2):* Sección 2. Capital mínimo por riesgo de crédito.
> *heredado (chapeau_seccion, S2):* A los efectos de la aplicación de las disposiciones de la presente sección, las entidades financieras se clasificarán en: i)Grupo 1: entidades calificadas por el BCRA como de importancia sistémica a nivel local
> *heredado (chapeau_seccion, S2):* (D-SIB) y sucursales o subsidiarias de bancos del exterior calificados como de impor- tancia sistémica global (G-SIB).
> *heredado (chapeau_seccion, S2):* ii) Grupo 2: entidades financieras no comprendidas en el acápite i). En aquellos casos en que no se establezcan disposiciones específicas para cada uno de los citados grupos de entidades financieras, deberá aplicarse el mismo tratamiento a ambos grupos. Las entidades financieras que presenten cambios en su calificación –conforme a lo previsto en los acápites precedentes–, contarán con un plazo de 6 meses para aplicar las disposiciones específicas correspondientes al nuevo grupo al que pertenezcan.
> *heredado (encabezado, 2.11):* 2.11. Exposiciones a instrumentos.
> *heredado (encabezado, 2.11.3):* 2.11.3. Criterios para considerar una exposición a instrumentos como una acción.
> *heredado (intro, 2.11.3):* A los fines de determinar si una exposición debe ser tratada como una acción, las en- tidades financieras del grupo 1 deberán tener en cuenta la realidad económica del ins- trumento. Quedan comprendidas:
> *propio:* 2.11.3.2. Instrumentos, en la medida que cumplan las siguientes condiciones: i) No puedan amortizarse. Los resultados de la inversión se pueden reali- zar solo a través de la venta del instrumento o de los derechos sobre la inversión o mediante la liquidación del emisor. ii) No representan obligación alguna para el emisor. iii) Representan un derecho residual sobre los activos o las utilidades del emisor.

**Nodos (5)**
- **N1** Condicion «Derecho residual sobre activos o utilidades» — El instrumento representa un derecho residual sobre los activos o las utilidades del emisor. · tramo (exacta): «Representan un derecho residual sobre los activos o las utilidades del emisor.» · punto_propio
- **N2** Condicion «No amortización del instrumento» — El instrumento no puede amortizarse; los resultados de la inversión solo se pueden realizar a través de la venta del instrumento o de los derechos sobre la inversión o mediante la liquidación del emisor. · tramo (exacta): «No puedan amortizarse. Los resultados de la inversión se pueden realizar solo a través de la venta del instrumento o de los derechos sobre la inversión o mediante la liquidación del emisor.» · punto_propio
- **N3** Condicion «No obligación para el emisor» — El instrumento no representa obligación alguna para el emisor. · tramo (exacta): «No representan obligación alguna para el emisor.» · punto_propio
- **N4** Definicion «Instrumentos tratados como acciones» — Instrumentos que deben ser tratados como acciones cuando cumplen las siguientes condiciones: (i) no puedan amortizarse y los resultados de la inversión se realicen solo a través de la venta del instrumento o de los derechos sobre la inversión o mediante la liquidación del emisor; (ii) no representan obligación alguna para el emisor; (iii) representan un derecho residual sobre los activos o las utilidades del emisor. · props: `{"termino": "Instrumentos"}` · tramo (exacta): «Instrumentos, en la medida que cumplan las siguientes condiciones: i) No puedan amortizarse. Los resultados de la inversión se pueden realizar solo a través de la venta del instrumento o de los derechos sobre la inversión o mediante la liquidación del emisor. ii) No representan obligación alguna para el emisor. iii) Representan un derecho residual sobre los activos o las utilidades del emisor.» · punto_propio
- **N5** TextoOrdenado «Texto Ordenado Capitales Mínimos» · props: `{"archivo": "TO_capitales_minimos_actual.pdf", "materia": "Capitales mínimos de las entidades financieras", "version": "Comunicación A 8418 (vigencia 10/04/2026)"}` · sin tramo · punto_propio · compartido (453 procedencias en el grafo)

**Aristas de la extracción (0)**

**Remisiones derivadas (0 aristas)**

**Estructurales (4)**: establecida_en → TextoOrdenado «Texto Ordenado Capitales Mínimos» ×4

## 8. `cap::6.8.1` — estrato item (8 del sorteo) · cap · págs. 138 · estado `completo_ok_directo`

> *heredado (encabezado, S6):* Sección 6. Capital mínimo por riesgo de mercado.
> *heredado (encabezado, 6.8):* 6.8. Políticas y procedimientos para la gestión de la cartera de negociación.
> *heredado (intro, 6.8):* Las entidades financieras deberán, como mínimo, tomar en consideración lo siguiente:
> *propio:* 6.8.1. Enunciar las actividades de negociación que la entidad incluye en esta cartera.

**Nodos (3)**
- **N1** Obligacion «Enunciar actividades de negociación en cartera» — Las entidades financieras deberán enunciar las actividades de negociación que incluyen en la cartera de negociación · props: `{"tipo": "otra"}` · tramo (exacta): «Enunciar las actividades de negociación que la entidad incluye en esta cartera» · punto_propio
- **N2** Sujeto «Entidades financieras» · props: `{"nivel": "clase", "alias": ["Entidades financieras emisoras de tarjetas de crédito y/o compra", "Entidad financiera emisora de tarjetas de crédito y/o compra"]}` · sin tramo · punto_propio · compartido (328 procedencias en el grafo)
- **N3** TextoOrdenado «Texto Ordenado Capitales Mínimos» · props: `{"archivo": "TO_capitales_minimos_actual.pdf", "materia": "Capitales mínimos de las entidades financieras", "version": "Comunicación A 8418 (vigencia 10/04/2026)"}` · sin tramo · punto_propio · compartido (453 procedencias en el grafo)

**Aristas de la extracción (1)**
- **A1** N1 —aplica_a→ N2 Sujeto «Entidades financieras» (mención «Las entidades financieras», exacta, R1_label_exacto)

**Remisiones derivadas (0 aristas)**

**Estructurales (1)**: establecida_en → TextoOrdenado «Texto Ordenado Capitales Mínimos» ×1

## 9. `cla::6.5.5.5` — estrato item (9 del sorteo) · cla · págs. 28 · estado `completo_ok_directo`

> *heredado (encabezado, S6):* Sección 6. Clasificación de los deudores de la cartera comercial.
> *heredado (encabezado, 6.5):* 6.5. Niveles de clasificación.
> *heredado (intro, 6.5):* Cada cliente, y la totalidad de sus financiaciones comprendidas, se incluirá en una de las si- guientes cinco categorías, las que se definen teniendo en cuenta las condiciones que se deta- llan en cada caso. Los clientes que no registren asistencia crediticia de la entidad y que posteriormente reciban fi- nanciaciones de ésta que no superen el importe resultante de aplicar sobre el saldo de deuda registrado en el sistema financiero, según la última información disponible en la “Central de deudores” a la fecha de su otorgamiento, el porcentaje establecido en el punto 2.2.5. de las normas sobre “Previsiones mínimas por riesgo de incobrabilidad” correspondiente a la peor cla- sificación asignada, podrán ser clasificados por la entidad teniendo en cuenta únicamente el análisis del flujo de fondos proyectado. Las asistencias así otorgadas no serán consideradas a los fines a que se refiere el punto 6.6. A fin de verificar el cumplimiento de las obligaciones sin recurrir a nueva financiación directa o indirecta o a refinanciaciones, no se considerarán refinanciaciones las facilidades adicionales que se otorguen respecto de los márgenes vigentes acordados, siempre que el nuevo apoyo crediticio implique nuevos desembolsos de fondos y no supere el 10 % del cupo asignado en oportunidad de la última evaluación crediticia del cliente, en la medida en que éstas sean con- sistentes con el curso normal de los negocios y exista capacidad para atender el resto de las obligaciones financieras, ni las nuevas financiaciones y las refinanciaciones asociadas a una mayor inversión derivada de la expansión de las actividades, y siempre que pueda demostrarse que el flujo de fondos proyectado permitirá afrontar la totalidad de sus obligaciones. Tampoco se considerarán dentro de ese concepto las refinanciaciones otorgadas a los produc- tores agropecuarios cuando ello resulte de la aplicación de disposiciones vinculadas a la Ley de Emergencia Agropecuaria, sin perjuicio de lo cual, a los fines de la clasificación, deberá tenerse en cuenta el flujo de fondos proyectado para el momento en que concluya la vigencia de la emergencia declarada. El tratamiento que se dispense en ese marco no podrá implicar mejora- miento de la clasificación asignada al cliente en función de su situación individual, preexistente a la emergencia, ni su aplicación extenderse más allá de la vigencia fijada para ella.
> *heredado (encabezado, 6.5.5):* 6.5.5. Irrecuperable.
> *heredado (intro, 6.5.5):* Las deudas de clientes incorporados a esta categoría se consideran incobrables. Si bien estos activos podrían tener algún valor de recuperación bajo un cierto conjunto de cir- cunstancias futuras, su incobrabilidad es evidente al momento del análisis. Entre los indicadores que pueden reflejar esta situación se destacan que el cliente:
> *heredado (cierre, 6.5.5):* Además, corresponderá clasificar en esta categoría a los clientes que, cualquiera sea el motivo (entre ellos por no contar con legajo o por no haber proporcionado información confiable y/o actualizada), no hayan sido evaluados con la periodicidad correspondiente, con excepción de los deudores en concurso o con acuerdo preventivo extrajudicial solici- tado o en gestión judicial que, por un período de hasta 540 días contados a partir de la apertura del concurso, solicitud del acuerdo preventivo o inicio de las gestiones judiciales de cobro, según corresponda, no hubiesen presentado la documentación que permita realizarla, siempre que se cuente con informe de abogado de la entidad financiera acreedora sobre la razonabilidad del recupero de los créditos comprendidos. Ello, sin perjuicio de que se trate de deudas que reúnan todas las condiciones previstas por el punto 2.2.3.2. de las normas sobre “Previsiones mínimas por riesgo de incobrabili- dad”.
> *propio:* 6.5.5.5. Pertenezca a un sector de la actividad económica o ramo de negocios en extin- ción, con graves problemas estructurales o que estén requiriendo una reestructu- ración generalizada.

**Nodos (2)**
- **N1** Condicion «Pertenencia a sector en extinción o reestructuración» — El cliente pertenece a un sector de la actividad económica o ramo de negocios en extinción, con graves problemas estructurales o que estén requiriendo una reestructuración generalizada · tramo (exacta): «Pertenezca a un sector de la actividad económica o ramo de negocios en extinción, con graves problemas estructurales o que estén requiriendo una reestructuración generalizada» · punto_propio
- **N2** TextoOrdenado «Texto Ordenado Clasificación de Deudores» · props: `{"archivo": "TO_clasificacion_deudores_actual.pdf", "materia": "Clasificación de deudores", "version": "Comunicación A 8378 (vigencia 20/12/2025)"}` · sin tramo · punto_propio · compartido (140 procedencias en el grafo)

**Aristas de la extracción (0)**

**Remisiones derivadas (0 aristas)**

**Estructurales (1)**: establecida_en → TextoOrdenado «Texto Ordenado Clasificación de Deudores» ×1

## 10. `ctacte::6.1.2.5` — estrato item (10 del sorteo) · ctacte · págs. 35 · estado `aceptado_con_residuales`

> *heredado (encabezado, S6):* Sección 6. Rechazo de cheques.
> *heredado (encabezado, 6.1):* 6.1. Causales.
> *heredado (encabezado, 6.1.2):* 6.1.2. Defectos formales.
> *heredado (intro, 6.1.2):* Se define como defecto formal todo aquel verificado en la creación del cheque que el beneficiario no pueda advertir por su mera apariencia. Quedan incluidos, entre otros, los siguientes casos:
> *propio:* 6.1.2.5. Firmante incluido en la “Central de cuentacorrentistas inhabilitados” al momento de la emisión del cheque.

**Nodos (3)**
- **N1** Operacion «Emisión de cheque» — Acto de crear y emitir un cheque · props: `{"tipo": "emisión de cheque"}` · tramo (exacta): «emisión del cheque» · punto_propio
- **N2** Restriccion «Prohibición — firmante inhabilitado en Central» — Se prohíbe la emisión de un cheque cuando el firmante está incluido en la Central de cuentacorrentistas inhabilitados al momento de la emisión · props: `{"tipo": "prohibicion"}` · tramo (exacta): «Firmante incluido en la "Central de cuentacorrentistas inhabilitados" al momento de la emisión del cheque» · punto_propio
- **N3** TextoOrdenado «Cuentas corrientes» · props: `{"archivo": "ctacte.pdf", "materia": "Reglamentación de la cuenta corriente bancaria", "version": "Comunicación A 8444 (vigencia 05/06/2026)"}` · sin tramo · punto_propio · compartido (380 procedencias en el grafo)

**Aristas de la extracción (1)**
- **A1** N2 —prohibe→ N1 Operacion «Emisión de cheque» [coherencia: coherente]

**Remisiones derivadas (0 aristas)**

**Estructurales (2)**: establecida_en → TextoOrdenado «Cuentas corrientes» ×2

## 11. `ctacte::12.1.2.7` — estrato item (11 del sorteo) · ctacte · págs. 55 · estado `aceptado_con_residuales`

> *heredado (encabezado, S12):* Sección 12. Disposiciones generales.
> *heredado (encabezado, 12.1):* 12.1. Recomendaciones para el uso de cajeros automáticos.
> *heredado (encabezado, 12.1.2):* 12.1.2. A continuación se enumeran las recomendaciones y recaudos que, como mínimo, de-
> *heredado (intro, 12.1.2):* berán comunicarse a los usuarios:
> *propio:* 12.1.2.7. Al realizar una operación de depósito, asegurarse de introducir el sobre que contenga el efectivo o cheques conjuntamente con el primer comprobante emitido por el cajero durante el proceso de esa transacción, en la ranura es- pecífica para esa función, y retirar el comprobante que la máquina entregue al finalizar la operación, el que le servirá para un eventual reclamo posterior.

**Nodos (4)**
- **N1** Obligacion «Recomendación — introducir sobre con comprobante inicial» — Recomendación: al realizar una operación de depósito, introducir el sobre que contenga el efectivo o cheques conjuntamente con el primer comprobante emitido por el cajero durante el proceso de esa transacción, en la ranura específica para esa función · props: `{"tipo": "otra"}` · tramo (exacta): «asegurarse de introducir el sobre que contenga el efectivo o cheques conjuntamente con el primer comprobante emitido por el cajero durante el proceso de esa transacción, en la ranura específica para esa función» · punto_propio
- **N2** Obligacion «Recomendación — retirar comprobante final» — Recomendación: retirar el comprobante que la máquina entregue al finalizar la operación de depósito, el que le servirá para un eventual reclamo posterior · props: `{"tipo": "otra"}` · tramo (exacta): «retirar el comprobante que la máquina entregue al finalizar la operación» · punto_propio
- **N3** Operacion «Depósito en cajero automático» — Operación de depósito en cajero automático mediante introducción de sobre con efectivo o cheques · props: `{"tipo": "depósito"}` · tramo (exacta): «operación de depósito» · punto_propio
- **N4** TextoOrdenado «Cuentas corrientes» · props: `{"archivo": "ctacte.pdf", "materia": "Reglamentación de la cuenta corriente bancaria", "version": "Comunicación A 8444 (vigencia 05/06/2026)"}` · sin tramo · punto_propio · compartido (380 procedencias en el grafo)

**Aristas de la extracción (2)**
- **A1** N3 —requiere→ N1 Obligacion «Recomendación — introducir sobre con comprobante inicial»
- **A2** N3 —requiere→ N2 Obligacion «Recomendación — retirar comprobante final»

**Remisiones derivadas (0 aristas)**

**Estructurales (3)**: establecida_en → TextoOrdenado «Cuentas corrientes» ×3

## 12. `ctacte::8.3.5` — estrato item (12 del sorteo) · ctacte · págs. 46 · estado `completo_ok_directo`

> *heredado (encabezado, S8):* Sección 8. “Central de cheques rechazados”, “Central de cuentacorrentistas inhabili- tados” y “Central de cheques denunciados como extraviados, sustraídos o adulterados”.
> *heredado (encabezado, 8.3):* 8.3. Cancelaciones de cheques rechazados.
> *heredado (intro, 8.3):* Se demostrará con cualquiera de las siguientes alternativas:
> *propio:* 8.3.5. Devolución de ECHEQ al librador ordenada por el tenedor legitimado a la entidad finan- ciera de la cual este último es cliente.

**Nodos (2)**
- **N1** Operacion «Devolución de ECHEQ al librador» — Devolución de ECHEQ (cheque electrónico) al librador, ordenada por el tenedor legitimado a la entidad financiera de la cual el tenedor es cliente. Constituye una alternativa para demostrar la cancelación de cheques rechazados. · props: `{"tipo": "devolución de instrumento de pago"}` · tramo (exacta): «Devolución de ECHEQ al librador ordenada por el tenedor legitimado a la entidad financiera de la cual este último es cliente» · punto_propio
- **N2** TextoOrdenado «Cuentas corrientes» · props: `{"archivo": "ctacte.pdf", "materia": "Reglamentación de la cuenta corriente bancaria", "version": "Comunicación A 8444 (vigencia 05/06/2026)"}` · sin tramo · punto_propio · compartido (380 procedencias en el grafo)

**Aristas de la extracción (0)**

**Remisiones derivadas (0 aristas)**

**Estructurales (1)**: establecida_en → TextoOrdenado «Cuentas corrientes» ×1

## 13. `ext::8.5.17.14` — estrato item (13 del sorteo) · ext · págs. 118 · estado `aceptado_con_residuales`

> *heredado (encabezado, S8):* Sección 8. Seguimiento de las negociaciones de divisas por exportaciones de bienes
> *heredado (encabezado, 8.5):* 8.5. Otras imputaciones admitidas en el cumplimiento del seguimiento.
> *heredado (intro, 8.5):* La entidad podrá considerar cumplimentado parcial o totalmente el seguimiento de un permiso de embarque cuando cuente con los elementos que le permitan considerar que la operación se encuentra en alguna de las situaciones detalladas a continuación y se verifiquen las condiciones previstas en cada caso. La documentación utilizada para certificar el concepto y monto de las divisas imputado en cada caso deberá quedar archivada en la entidad a disposición del BCRA.
> *heredado (encabezado, 8.5.17):* 8.5.17. Operaciones aduaneras exceptuadas del seguimiento.
> *heredado (intro, 8.5.17):* Por el valor que corresponda a ventajas aduaneras u otras situaciones previstas en el siguiente listado de operaciones:
> *propio:* 8.5.17.14. Exportaciones del Área Aduanera Especial a las áreas francas nacionales y al resto del territorio de la Nación. En cuanto a las exportaciones del Área Aduanera Especial al área franca, la exención de ingreso de divisas es procedente en tanto supongan abastecimiento mismo del área franca y no exista ulterior reexportación (a decisión de la Dirección General de Aduanas, según el apartado segundo del art. 12 del Decreto 9.208/72).

**Nodos (5)**
- **N1** Condicion «Abastecimiento área franca sin reexportación» — La operación supone abastecimiento del área franca y no existe ulterior reexportación · tramo (exacta): «supongan abastecimiento mismo del área franca y no exista ulterior reexportación» · punto_propio
- **N2** Excepcion «Exención seguimiento — exportaciones Área Aduanera Especial» — Exención del seguimiento de ingreso de divisas para exportaciones del Área Aduanera Especial a áreas francas cuando suponen abastecimiento del área franca y no existe ulterior reexportación · tramo (exacta): «la exención de ingreso de divisas es procedente en tanto supongan abastecimiento mismo del área franca y no exista ulterior reexportación» · punto_propio
- **N3** Operacion «Exportación Área Aduanera Especial a áreas francas» — Exportaciones del Área Aduanera Especial a las áreas francas nacionales y al resto del territorio de la Nación, exceptuadas del seguimiento de divisas cuando suponen abastecimiento del área franca sin ulterior reexportación · props: `{"tipo": "Exportación"}` · tramo (exacta): «Exportaciones del Área Aduanera Especial a las áreas francas nacionales y al resto del territorio de la Nación» · punto_propio
- **N4** Potestad «Decisión Dirección General de Aduanas — procedencia exención» — La Dirección General de Aduanas decide sobre la procedencia de la exención de ingreso de divisas, según el apartado segundo del artículo 12 del Decreto 9.208/72 · tramo (exacta): «a decisión de la Dirección General de Aduanas, según el apartado segundo del art. 12 del Decreto 9.208/72» · punto_propio
- **N5** TextoOrdenado «Texto Ordenado Exterior Cambios» · props: `{"archivo": "TO_exterior_cambios_actual.pdf", "materia": "Exterior y cambios", "version": "Comunicación A 8307 (vigencia 26/08/2025)"}` · sin tramo · punto_propio · compartido (930 procedencias en el grafo)

**Aristas de la extracción (1)**
- **A1** N1 —condicion_de→ N2 Excepcion «Exención seguimiento — exportaciones Área Aduanera Especial»

**Remisiones derivadas (0 aristas)**

**Estructurales (4)**: establecida_en → TextoOrdenado «Texto Ordenado Exterior Cambios» ×4

## 14. `ext::14.2.1.6` — estrato item (14 del sorteo) · ext · págs. 177 · estado `aceptado_con_residuales`

> *heredado (encabezado, S14):* Sección 14. Disposiciones complementarias asociadas al Régimen de Incentivo para Grandes Inversiones (RIGI).
> *heredado (chapeau_seccion, S14):* En esta sección se detallan las disposiciones complementarias en materia cambiaria que, en la medida que las disposiciones generales no resulten más favorables, resultan aplicables a un Vehículo de Proyecto Único (VPU) adherido al Régimen de Incentivo los referidas al “Régimen de Incentivo para Grandes Inversiones” (RIGI) establecido en el Título VII de la Ley 27.742 y reglamentado por el Decreto 749/24 y concordantes.
> *heredado (encabezado, 14.2):* 14.2. Beneficios relacionados con el acceso al mercado de cambios para operaciones de egreso.
> *heredado (intro, 14.2):* Adicionalmente lo previsto en la normativa general en materia de egresos por el mercado de cambios, en la medida que se cumplan los restantes requisitos aplicables a cada operación, por aquellas financiaciones o aportes de inversión directa recibidos por el VPU adherido a partir de la vigencia de la Ley 27.742, las entidades podrán también dar acceso en las siguientes situaciones:
> *heredado (encabezado, 14.2.1):* 14.2.1. En el marco de lo dispuesto en los puntos 3.3., 3.5., 3.6. y 10.3.2., según
> *heredado (intro, 14.2.1):* corresponda, sin necesidad de contar con la conformidad previa del BCRA si tal requisito estuviese vigente, las entidades podrán darle acceso al cliente para pagar, incluso antes de la fecha de vencimiento, los intereses devengados hasta la fecha de acceso que se encuentren impagos y/o el capital pendiente de:
> *heredado (cierre, 14.2.1):* En el caso de que la totalidad de los fondos obtenidos por la financiación no pudiese ser computada como ingresada y liquidada en el mercado de cambios, las entidades también podrán dar acceso al VPU adherido, sin necesidad de contar con la conformidad previa del BCRA si tal requisito estuviese vigente, para realizar:
> *heredado (cierre, 14.2.1):* i) pagos de intereses devengados hasta la fecha de acceso que se encuentren
> *heredado (cierre, 14.2.1):* impagos y que correspondan a la porción del capital equivalente a la proporción de los fondos recibidos por el VPU por la financiación que puede computarse como ingresada y liquidada por el mercado de cambios.
> *heredado (cierre, 14.2.1):* ii) pagos por capital adeudado que corresponda a la porción del capital
> *heredado (cierre, 14.2.1):* equivalente a la proporción de los fondos recibidos por el VPU por la financiación que puede computarse como ingresada y liquidada por el mercado de cambios.
> *propio:* 14.2.1.6. financiaciones financieras en moneda extranjera otorgadas por entidades financieras locales fondeadas a partir de una línea de crédito de una entidad financiera del exterior, liquidadas en el mercado de cambios.

**Nodos (6)**
- **N1** Condicion «Fondeo a partir de línea de crédito del exterior» — Las financiaciones deben estar fondeadas a partir de una línea de crédito de una entidad financiera del exterior. · tramo (exacta): «fondeadas a partir de una línea de crédito de una entidad financiera del exterior» · punto_propio
- **N2** Condicion «Liquidación en el mercado de cambios» — Las financiaciones deben estar liquidadas en el mercado de cambios. · tramo (exacta): «liquidadas en el mercado de cambios» · punto_propio
- **N3** Operacion «Financiaciones financieras en moneda extranjera» — Financiaciones financieras en moneda extranjera otorgadas por entidades financieras locales fondeadas a partir de una línea de crédito de una entidad financiera del exterior, liquidadas en el mercado de cambios. · props: `{"tipo": "financiación"}` · tramo (exacta): «financiaciones financieras en moneda extranjera otorgadas por entidades financieras locales fondeadas a partir de una línea de crédito de una entidad financiera del exterior, liquidadas en el mercado de cambios» · punto_propio
- **N4** Potestad «Acceso al mercado de cambios para financiaciones RIGI» — Las entidades podrán dar acceso al cliente para pagar, incluso antes de la fecha de vencimiento, los intereses devengados hasta la fecha de acceso que se encuentren impagos y/o el capital pendiente de financiaciones financieras en moneda extranjera otorgadas por entidades financieras locales fondeadas a partir de una línea de crédito de una entidad financiera del exterior, en el marco de lo dispuesto en los puntos 3.3., 3.5., 3.6. y 10.3.2., sin necesidad de contar con la conformidad previa del BCRA si tal requisito estuviese vigente. · tramo (exacta): «las entidades podrán darle acceso al cliente para pagar, incluso antes de la fecha de vencimiento, los intereses devengados hasta la fecha de acceso que se encuentren impagos y/o el capital pendiente» · punto_propio
- **N5** Sujeto «Entidades financieras» · props: `{"nivel": "clase", "alias": ["Entidades financieras emisoras de tarjetas de crédito y/o compra", "Entidad financiera emisora de tarjetas de crédito y/o compra"]}` · sin tramo · punto_propio · compartido (328 procedencias en el grafo)
- **N6** TextoOrdenado «Texto Ordenado Exterior Cambios» · props: `{"archivo": "TO_exterior_cambios_actual.pdf", "materia": "Exterior y cambios", "version": "Comunicación A 8307 (vigencia 26/08/2025)"}` · sin tramo · punto_propio · compartido (930 procedencias en el grafo)

**Aristas de la extracción (3)**
- **A1** N1 —condicion_de→ N3 Operacion «Financiaciones financieras en moneda extranjera»
- **A2** N2 —condicion_de→ N3 Operacion «Financiaciones financieras en moneda extranjera»
- **A3** N4 —aplica_a→ N5 Sujeto «Entidades financieras» (mención «entidades financieras locales», exacta, R4_sugerencia_modelo)

**Remisiones derivadas (16 aristas)**
- **R1–R16** N4 —remite_a→ `ext::10.3.2` (interna; 6 nodo(s) destino: Condicion «Casos no encuadrados en requisitos previos»; Condicion «Verificación previa de requisitos para acceso al mercado»; Obligacion «Canalización de pedidos por entidad autorizada»; Operacion «Acceso al mercado de cambios para pago de importaciones»; Potestad «Conformidad previa del BCRA — pago de oficializaciones»; Potestad «Facultad de dar acceso al mercado de cambios») · evidencia «14.2.1. En el marco de lo dispuesto en los puntos 3.3., 3.5., 3.6. y 10.3.2., según»
- **R2–R10** N4 —remite_a→ `ext::3.3` (interna; 4 nodo(s) destino: Condicion «Condiciones para acceso al mercado de cambios»; Obligacion «Verificación de condiciones para acceso al mercado de cambios»; Operacion «Acceso al mercado de cambios para pagos de intereses»; Operacion «Pago de intereses deuda comercial importación») · evidencia «14.2.1. En el marco de lo dispuesto en los puntos 3.3., 3.5., 3.6. y 10.3.2., según»
- **R3–R14** N4 —remite_a→ `ext::3.5` (interna; 4 nodo(s) destino: Condicion «Verificación de condiciones siguientes»; Operacion «Pago de títulos de deuda y endeudamientos financieros con el exterior»; Potestad «Acceso al mercado de cambios — pagos de títulos y endeudamientos»; Potestad «Acceso al mercado de cambios para pagos de títulos y endeudamientos») · evidencia «14.2.1. En el marco de lo dispuesto en los puntos 3.3., 3.5., 3.6. y 10.3.2., según»
- **R9–R11** N4 —remite_a→ `ext::3.6` (interna; 2 nodo(s) destino: Operacion «Obligaciones en moneda extranjera entre residentes»; Operacion «Pago de títulos de deuda en moneda extranjera») · evidencia «14.2.1. En el marco de lo dispuesto en los puntos 3.3., 3.5., 3.6. y 10.3.2., según»

**Estructurales (4)**: establecida_en → TextoOrdenado «Texto Ordenado Exterior Cambios» ×4

## 15. `ext::7.9.1.1` — estrato item (15 del sorteo) · ext · págs. 94 · estado `completo_ok_directo`

> *heredado (encabezado, S7):* Sección 7. Cobros de exportaciones de bienes.
> *heredado (encabezado, 7.9):* 7.9. Operaciones financieras habilitadas para aplicar cobros de exportaciones de bienes y
> *heredado (intro, 7.9):* servicios.
> *heredado (encabezado, 7.9.1):* 7.9.1. La aplicación de cobros de exportaciones y servicios estará habilitada, en la medida
> *heredado (intro, 7.9.1):* que se cumplan las condiciones consignadas en cada caso, en los siguientes casos:
> *propio:* 7.9.1.1. Pago de capital e intereses de endeudamientos financieros comprendidos en el punto 3.5. cuyos fondos hayan sido ingresados y liquidados en el mercado de cambios a partir del 02/10/20 y destinados a la financiación de proyectos que cumplen las condiciones previstas en el punto 7.9.2., en la medida que su vida promedio no sea inferior a 1 (un) año, considerando los pagos de servicios de capital e intereses.

**Nodos (4)**
- **N1** Condicion «Vida promedio mínima 1 año» — La vida promedio del endeudamiento no sea inferior a 1 año, considerando los pagos de servicios de capital e intereses · props: `{"umbrales": [{"tramo": "1 (un) año", "valor": "1", "unidad": "anios", "comparacion": "minimo_inclusivo", "regla_comparacion": "negacion:inferior", "origen": "e1", "tramo_verificado": "exacta"}]}` · tramo (exacta): «en la medida que su vida promedio no sea inferior a 1 (un) año, considerando los pagos de servicios de capital e intereses» · punto_propio
- **N2** Obligacion «Habilitación aplicación cobros exportaciones» — La aplicación de cobros de exportaciones y servicios estará habilitada para pago de capital e intereses de endeudamientos financieros comprendidos en punto 3.5., cuyos fondos fueron ingresados y liquidados en mercado de cambios a partir del 02/10/20, destinados a financiación de proyectos con condiciones del punto 7.9.2., siempre que vida promedio no sea inferior a 1 año · props: `{"tipo": "otra", "umbrales": [{"tramo": "1 año", "valor": "1", "unidad": "anios", "comparacion": "minimo_inclusivo", "regla_comparacion": "negacion:inferior", "origen": "descripcion", "tramo_verificado": "tokens"}]}` · tramo (exacta): «La aplicación de cobros de exportaciones y servicios estará habilitada, en la medida que se cumplan las condiciones consignadas en cada caso, en los siguientes casos: […] Pago de capital e intereses de endeudamientos financieros comprendidos en el punto 3.5. cuyos fondos hayan sido ingresados y liquidados en el mercado de cambios a partir del 02/10/20 y destinados a la financiación de proyectos que cumplen las condiciones previstas en el punto 7.9.2., en la medida que su vida promedio no sea inferior a 1 (un) año, considerando los pagos de servicios de capital e intereses» · punto_propio
- **N3** Operacion «Pago capital e intereses endeudamientos financieros» — Pago de capital e intereses de endeudamientos financieros cuyos fondos fueron ingresados y liquidados en el mercado de cambios a partir del 02/10/20 y destinados a financiación de proyectos que cumplen condiciones del punto 7.9.2. · props: `{"tipo": "Pago de capital e intereses"}` · tramo (exacta): «Pago de capital e intereses de endeudamientos financieros comprendidos en el punto 3.5. cuyos fondos hayan sido ingresados y liquidados en el mercado de cambios a partir del 02/10/20 y destinados a la financiación de proyectos que cumplen las condiciones previstas en el punto 7.9.2.» · punto_propio
- **N4** TextoOrdenado «Texto Ordenado Exterior Cambios» · props: `{"archivo": "TO_exterior_cambios_actual.pdf", "materia": "Exterior y cambios", "version": "Comunicación A 8307 (vigencia 26/08/2025)"}` · sin tramo · punto_propio · compartido (930 procedencias en el grafo)

**Aristas de la extracción (1)**
- **A1** N1 —condicion_de→ N2 Obligacion «Habilitación aplicación cobros exportaciones»

**Remisiones derivadas (12 aristas)**
- **R1–R5** N2 —remite_a→ `ext::7.9.2` (interna; 4 nodo(s) destino: Condicion «Destino fondos a financiación de proyectos de inversión»; Condicion «Elegibilidad por destino a financiación de proyectos»; Operacion «Elegibilidad operaciones 7.9.1.1 a 7.9.1.3»; Operacion «Operaciones de financiación de proyectos de inversión») · evidencia «financiación de proyectos que cumplen las condiciones previstas en el punto 7.9.2., en la medida que su»
- **R3–R8** N2 —remite_a→ `ext::3.5` (interna; 4 nodo(s) destino: Condicion «Verificación de condiciones siguientes»; Operacion «Pago de títulos de deuda y endeudamientos financieros con el exterior»; Potestad «Acceso al mercado de cambios — pagos de títulos y endeudamientos»; Potestad «Acceso al mercado de cambios para pagos de títulos y endeudamientos») · evidencia «intereses de endeudamientos financieros comprendidos en el punto 3.5. cuyos fondos hayan»
- **R9–R12** N3 —remite_a→ `ext::7.9.2` (interna; 4 nodo(s) destino: Condicion «Destino fondos a financiación de proyectos de inversión»; Condicion «Elegibilidad por destino a financiación de proyectos»; Operacion «Elegibilidad operaciones 7.9.1.1 a 7.9.1.3»; Operacion «Operaciones de financiación de proyectos de inversión») · evidencia «financiación de proyectos que cumplen las condiciones previstas en el punto 7.9.2., en la medida que su»

**Estructurales (3)**: establecida_en → TextoOrdenado «Texto Ordenado Exterior Cambios» ×3

## 16. `ext::4.6.1.4` — estrato item (16 del sorteo) · ext · págs. 62 · estado `aceptado_con_residuales`

> *heredado (encabezado, S4):* Sección 4. Otras disposiciones específicas.
> *heredado (encabezado, 4.6):* 4.6. Suscripción de bonos BOPREAL por utilidades y dividendos de accionistas no residentes
> *heredado (intro, 4.6):* pendientes de pago o ya percibidas en el país.
> *heredado (encabezado, 4.6.1):* 4.6.1. Suscripción de bonos BOPREAL por utilidades y dividendos pendientes de pago a no
> *heredado (intro, 4.6.1):* residentes a partir de la distribución determinada por la asamblea de accionistas. Los clientes podrán suscribir Bonos para la Reconstrucción de una Argentina Libre (BOPREAL) por hasta el equivalente al monto en moneda local de las utilidades y dividendos pendientes de pago a accionistas no residentes a partir de la distribución determinada por la asamblea de accionistas. La entidad que concrete la oferta de suscripción en nombre del cliente deberá verificar el cumplimiento de los siguientes requisitos:
> *heredado (cierre, 4.6.1):* Adicionalmente, la mencionada entidad deberá realizar un boleto de venta de cambio a nombre del cliente por el código de concepto "I09. Registro de utilidades y dividendos por adjudicación de bonos BOPREAL"; consignando el valor nominal en moneda extranjera de los bonos BOPREAL adjudicado al cliente.
> *propio:* 4.6.1.4. Cuenta con una declaración jurada del cliente en la que deja constancia de que: i) las utilidades y dividendos por las cuales solicita la suscripción se encuentran pendientes de pago; ii) no ha utilizado ya este mecanismo por esta deuda; y iii) toma conocimiento de que no tendrá acceso al mercado de cambios para pagar el equivalente de la deuda por la cual se suscribió excepto que el pago se concrete a partir de un canje y arbitraje con los fondos depositados en una cuenta local y originados en cobros de capital e intereses en moneda extranjera de los bonos BOPREAL. La declaración jurada deberá estar firmada por el representante legal de la empresa residente o un apoderado con facultades suficientes para asumir este compromiso en nombre de la empresa.

**Nodos (10)**
- **N1** Condicion «No utilización previa del mecanismo» — El cliente no debe haber utilizado ya este mecanismo de suscripción de BOPREAL por la misma deuda. · tramo (exacta): «no ha utilizado ya este mecanismo por esta deuda» · punto_propio
- **N2** Condicion «Utilidades y dividendos pendientes de pago» — Las utilidades y dividendos por los cuales se solicita la suscripción deben encontrarse pendientes de pago. · tramo (exacta): «las utilidades y dividendos por las cuales solicita la suscripción se encuentran pendientes de pago» · punto_propio
- **N3** Excepcion «Excepción acceso cambios — canje y arbitraje BOPREAL» — Queda exceptuada la restricción de acceso al mercado de cambios cuando el pago se concrete a partir de un canje y arbitraje con fondos depositados en una cuenta local originados en cobros de capital e intereses en moneda extranjera de los bonos BOPREAL. · tramo (exacta): «excepto que el pago se concrete a partir de un canje y arbitraje con los fondos depositados en una cuenta local y originados en cobros de capital e intereses en moneda extranjera de los bonos BOPREAL» · punto_propio
- **N4** Obligacion «Firma de declaración jurada — representante legal o apoderado» — La declaración jurada debe estar firmada por el representante legal de la empresa residente o un apoderado con facultades suficientes para asumir el compromiso en nombre de la empresa. · props: `{"tipo": "otra"}` · tramo (exacta): «La declaración jurada deberá estar firmada por el representante legal de la empresa residente o un apoderado con facultades suficientes para asumir este compromiso en nombre de la empresa.» · punto_propio
- **N5** Obligacion «Boleto de venta de cambio — código I09 BOPREAL» — La entidad deberá realizar un boleto de venta de cambio a nombre del cliente por el código de concepto I09 (Registro de utilidades y dividendos por adjudicación de bonos BOPREAL), consignando el valor nominal en moneda extranjera de los bonos BOPREAL adjudicados al cliente. · props: `{"tipo": "otra"}` · tramo (exacta): «la mencionada entidad deberá realizar un boleto de venta de cambio a nombre del cliente por el código de concepto "I09. Registro de utilidades y dividendos por adjudicación de bonos BOPREAL"; consignando el valor nominal en moneda extranjera de los bonos BOPREAL adjudicado al cliente» · herencia_encabezado
- **N6** Obligacion «Verificación de requisitos — suscripción BOPREAL» — La entidad que concrete la oferta de suscripción deberá verificar que el cliente cuente con una declaración jurada en la que conste que las utilidades y dividendos están pendientes de pago, que no ha utilizado ya este mecanismo por esta deuda, y que toma conocimiento de las restricciones de acceso al mercado de cambios. · props: `{"tipo": "otra"}` · tramo (exacta): «La entidad que concrete la oferta de suscripción en nombre del cliente deberá verificar el cumplimiento de los siguientes requisitos: […] Cuenta con una declaración jurada del cliente en la que deja constancia de que:» · herencia_encabezado
- **N7** Operacion «Suscripción BOPREAL por utilidades y dividendos» — Suscripción de BOPREAL por el equivalente en moneda local de las utilidades y dividendos pendientes de pago a accionistas no residentes, limitada al monto máximo equivalente a esas utilidades y dividendos, a partir de la distribución determinada por la asamblea de accionistas. · props: `{"tipo": "suscripción de bonos"}` · tramo (exacta): «Los clientes podrán suscribir Bonos para la Reconstrucción de una Argentina Libre (BOPREAL) por hasta el equivalente al monto en moneda local de las utilidades y dividendos pendientes de pago a accionistas no residentes a partir de la distribución determinada por la asamblea de accionistas.» · herencia_encabezado · compartido (3 procedencias en el grafo)
- **N8** Restriccion «Restricción acceso mercado de cambios — pago deuda BOPREAL» — El cliente no tendrá acceso al mercado de cambios para pagar el equivalente de la deuda por la cual se suscribió, excepto que el pago se concrete a partir de un canje y arbitraje con fondos depositados en una cuenta local originados en cobros de capital e intereses en moneda extranjera de los bonos BOPREAL. · props: `{"tipo": "prohibicion"}` · tramo (exacta): «no tendrá acceso al mercado de cambios para pagar el equivalente de la deuda por la cual se suscribió excepto que el pago se concrete a partir de un canje y arbitraje con los fondos depositados en una cuenta local y originados en cobros de capital e intereses en moneda extranjera de los bonos BOPREAL» · punto_propio
- **N9** Sujeto «Entidades autorizadas a operar en cambios (Exterior)» · props: `{"nivel": "rol"}` · sin tramo · herencia_encabezado · compartido (344 procedencias en el grafo)
- **N10** TextoOrdenado «Texto Ordenado Exterior Cambios» · props: `{"archivo": "TO_exterior_cambios_actual.pdf", "materia": "Exterior y cambios", "version": "Comunicación A 8307 (vigencia 26/08/2025)"}` · sin tramo · punto_propio · compartido (930 procedencias en el grafo)

**Aristas de la extracción (5)**
- **A1** N1 —condicion_de→ N6 Obligacion «Verificación de requisitos — suscripción BOPREAL»
- **A2** N2 —condicion_de→ N6 Obligacion «Verificación de requisitos — suscripción BOPREAL»
- **A3** N3 —exceptua→ N8 Restriccion «Restricción acceso mercado de cambios — pago deuda BOPREAL»
- **A4** N5 —aplica_a→ N9 Sujeto «Entidades autorizadas a operar en cambios (Exterior)» (mención «la mencionada entidad», exacta, R4_sugerencia_modelo)
- **A5** N6 —aplica_a→ N9 Sujeto «Entidades autorizadas a operar en cambios (Exterior)» (mención «La entidad que concrete la oferta de suscripción en nombre del cliente», exacta, R4_sugerencia_modelo)

**Remisiones derivadas (0 aristas)**

**Estructurales (8)**: establecida_en → TextoOrdenado «Texto Ordenado Exterior Cambios» ×8

## 17. `ctacte::6.1.2.7` — estrato item (17 del sorteo) · ctacte · págs. 35 · estado `aceptado_con_residuales`

> *heredado (encabezado, S6):* Sección 6. Rechazo de cheques.
> *heredado (encabezado, 6.1):* 6.1. Causales.
> *heredado (encabezado, 6.1.2):* 6.1.2. Defectos formales.
> *heredado (intro, 6.1.2):* Se define como defecto formal todo aquel verificado en la creación del cheque que el beneficiario no pueda advertir por su mera apariencia. Quedan incluidos, entre otros, los siguientes casos:
> *propio:* 6.1.2.7. Giro sobre el librador, salvo que se tratara de un cheque girado entre distintos establecimientos de un mismo librador.

**Nodos (4)**
- **N1** Excepcion «Excepción cheque entre establecimientos del mismo librador» — No aplica la prohibición de giro sobre el librador cuando se trata de un cheque girado entre distintos establecimientos de un mismo librador · tramo (exacta): «salvo que se tratara de un cheque girado entre distintos establecimientos de un mismo librador» · punto_propio
- **N2** Operacion «Giro sobre el librador» — Giro de cheque sobre el librador, defecto formal en la creación del cheque · props: `{"tipo": "giro de cheque"}` · tramo (exacta): «Giro sobre el librador» · punto_propio
- **N3** Restriccion «Prohibición giro sobre librador» — Se prohíbe el giro sobre el librador como causal de rechazo de cheques, salvo que se trate de un cheque girado entre distintos establecimientos de un mismo librador · props: `{"tipo": "prohibicion"}` · tramo (exacta): «Giro sobre el librador, salvo que se tratara de un cheque girado entre distintos establecimientos de un mismo librador» · punto_propio
- **N4** TextoOrdenado «Cuentas corrientes» · props: `{"archivo": "ctacte.pdf", "materia": "Reglamentación de la cuenta corriente bancaria", "version": "Comunicación A 8444 (vigencia 05/06/2026)"}` · sin tramo · punto_propio · compartido (380 procedencias en el grafo)

**Aristas de la extracción (2)**
- **A1** N1 —exceptua→ N3 Restriccion «Prohibición giro sobre librador»
- **A2** N3 —prohibe→ N2 Operacion «Giro sobre el librador» [coherencia: coherente]

**Remisiones derivadas (0 aristas)**

**Estructurales (3)**: establecida_en → TextoOrdenado «Cuentas corrientes» ×3

## 18. `cap::8.2.1.9` — estrato item (18 del sorteo) · cap · págs. 155 · estado `completo_ok_directo`

> *heredado (encabezado, S8):* Sección 8. Responsabilidad patrimonial computable.
> *heredado (encabezado, 8.2):* 8.2. Conceptos computables.
> *heredado (encabezado, 8.2.1):* 8.2.1. Capital ordinario de nivel uno (CO ).
> *heredado (intro, 8.2.1):* n1
> *heredado (intro, 8.2.1):* Comprende los siguientes rubros del patrimonio neto:
> *propio:* 8.2.1.9. Participaciones minoritarias. Acciones ordinarias emitidas por subsidiarias suje- tas a supervisión consolidada y en poder de terceros, que cumplan los criterios establecidos en el punto 8.3.5. A los conceptos citados en los puntos precedentes se les restarán los conceptos dedu- cibles previstos en el punto 8.4.1. y, de corresponder, en el punto 8.4.2.

**Nodos (4)**
- **N1** Definicion «Participaciones minoritarias — CO n1» — Acciones ordinarias emitidas por subsidiarias sujetas a supervisión consolidada y en poder de terceros, que cumplan los criterios establecidos en el punto 8.3.5 · props: `{"termino": "Participaciones minoritarias"}` · tramo (exacta): «Acciones ordinarias emitidas por subsidiarias sujetas a supervisión consolidada y en poder de terceros, que cumplan los criterios establecidos en el punto 8.3.5» · punto_propio
- **N2** Operacion «Emisión de acciones ordinarias por subsidiarias» — Acciones ordinarias emitidas por subsidiarias sujetas a supervisión consolidada y en poder de terceros que cumplan los criterios establecidos en el punto 8.3.5 · props: `{"tipo": "Emisión de acciones ordinarias"}` · tramo (exacta): «Acciones ordinarias emitidas por subsidiarias sujetas a supervisión consolidada y en poder de terceros» · punto_propio
- **N3** Restriccion «Deducción de conceptos deducibles — CO n1» — A los conceptos citados en los puntos precedentes se les restarán los conceptos deducibles previstos en el punto 8.4.1 y, de corresponder, en el punto 8.4.2 · props: `{"tipo": "limite_cualitativo"}` · tramo (exacta): «A los conceptos citados en los puntos precedentes se les restarán los conceptos deducibles previstos en el punto 8.4.1. y, de corresponder, en el punto 8.4.2.» · punto_propio
- **N4** TextoOrdenado «Texto Ordenado Capitales Mínimos» · props: `{"archivo": "TO_capitales_minimos_actual.pdf", "materia": "Capitales mínimos de las entidades financieras", "version": "Comunicación A 8418 (vigencia 10/04/2026)"}` · sin tramo · punto_propio · compartido (453 procedencias en el grafo)

**Aristas de la extracción (0)**

**Remisiones derivadas (2 aristas)**
- **R1** N1 —remite_a→ `cap::8.3.5` (interna; 1 nodo(s) destino: Definicion «Instrumentos computables como capital — subsidiarias en supervisión consolidada») · evidencia «poder de terceros, que cumplan los criterios establecidos en el punto 8.3.5. A los conceptos citados»
- **R2** N2 —remite_a→ `cap::8.3.5` (interna; 1 nodo(s) destino: Definicion «Instrumentos computables como capital — subsidiarias en supervisión consolidada») · evidencia «poder de terceros, que cumplan los criterios establecidos en el punto 8.3.5. A los conceptos citados»

**Estructurales (3)**: establecida_en → TextoOrdenado «Texto Ordenado Capitales Mínimos» ×3

## 19. `ext::10.3.2.1` — estrato item (19 del sorteo) · ext · págs. 134, 135 · estado `aceptado_con_residuales`

> *heredado (encabezado, S10):* Sección 10. Pagos de importaciones y otras compras de bienes en el exterior.
> *heredado (encabezado, 10.3):* 10.3. Pagos de importaciones de bienes que cuentan con registro de ingreso aduanero.
> *heredado (encabezado, 10.3.2):* 10.3.2. Requisitos de acceso para el pago de oficializaciones de importación comprendidas
> *heredado (intro, 10.3.2):* en el SEPAIMPO. La entidad interviniente podrá dar acceso al mercado de cambios para el pago al exterior de importaciones de bienes que cuentan con registro de ingreso aduanero que constan en el SEPAIMPO, en la medida que verifique previamente la totalidad de los siguientes requisitos:
> *heredado (cierre, 10.3.2):* Los casos que no encuadren en lo expuesto precedentemente quedan sujetos a la conformidad previa del BCRA, debiendo los pedidos ser canalizados por una entidad autorizada a realizar este tipo de pagos.
> *propio:* 10.3.2.1. Certifica en carácter de entidad encargada del seguimiento de la oficialización que se cumplen las condiciones que se enuncian a continuación o cuenta con una certificación para realizar el pago emitida por la entidad que tiene tal responsabilidad i) Cuenta con constancia del registro aduanero del ingreso al país de los bienes que originan el pago a cancelarse. ii) Cuenta con copia de factura comercial emitida en el exterior a nombre del cliente residente en el país, que efectúa la compra al exterior, donde conste nombre y dirección del emisor, nombre del importador argentino, la cantidad y descripción de la mercadería, condición de venta y valor de la factura. iii) Cuenta con copia del Documento de Transporte (Conocimiento de Embarque – Carta de Porte – Guía Aérea). iv) Que la información que surge de la factura comercial y del Documento de Transporte sea consistente con la que figura en los registros aduaneros, considerando las normas de declaración aduanera aplicables. v) Que la documentación presentada le permita establecer la fecha de vencimiento de la obligación con el exterior por parte del importador o, en su defecto, que la operación no tiene una fecha de vencimiento pactada. vi) Que, en caso de tratarse de operaciones financiadas, la documentación presentada le permite calificar a la misma como una deuda por importaciones de bienes según lo dispuesto en el punto 10.2.4. vii) Que el total de los pagos realizados con imputación a la oficialización de importación, incluyendo el pago cuyo curso se está solicitando, no supera el monto facturado en la condición de compra pactada. viii) Que el beneficiario del pago a realizar sea el proveedor del exterior o, en su caso, la entidad financiera del exterior o la agencia oficial de crédito que financió la compra al proveedor del exterior en la medida que las operaciones encuadren como deuda comercial por importaciones de bienes, o el no residente que compró el crédito al acreedor comercial del exterior y en la medida que no se modifiquen las condiciones en las que se otorgó el crédito. ix) Cuenta con constancia de que la operación se encuentra declarada, en caso de corresponder, en la última presentación vencida del “Relevamiento de activos y pasivos externos”. x) En el caso de importaciones oficializadas con anterioridad al 01/11/19, cuenta con una declaración jurada consignando el saldo de deuda pendiente a la fecha, firmada por el importador o quien ejerza su representación legal o un apoderado con facultades suficientes para asumir este compromiso en nombre del importador.

**Nodos (13)**
- **N1** Condicion «Beneficiario del pago es proveedor o acreedor autorizado» — El beneficiario del pago debe ser el proveedor del exterior, o la entidad financiera del exterior o agencia oficial de crédito que financió la compra (si encuadra como deuda comercial), o el no residente que compró el crédito al acreedor comercial, sin modificación de condiciones originales · tramo (exacta): «Que el beneficiario del pago a realizar sea el proveedor del exterior o, en su caso, la entidad financiera del exterior o la agencia oficial de crédito que financió la compra al proveedor del exterior en la medida que las operaciones encuadren como deuda comercial por importaciones de bienes, o el no residente que compró el crédito al acreedor comercial del exterior y en la medida que no se modifiquen las condiciones en las que se otorgó el crédito» · punto_propio
- **N2** Condicion «Calificación como deuda por importaciones financiadas» — En caso de operaciones financiadas, la documentación debe permitir calificar la operación como deuda por importaciones de bienes conforme al punto 10.2.4 · tramo (exacta): «Que, en caso de tratarse de operaciones financiadas, la documentación presentada le permite calificar a la misma como una deuda por importaciones de bienes según lo dispuesto en el punto 10.2.4» · punto_propio
- **N3** Condicion «Consistencia entre factura y registro aduanero» — La información de la factura comercial y del Documento de Transporte debe ser consistente con los registros aduaneros, conforme a las normas de declaración aduanera aplicables · tramo (exacta): «Que la información que surge de la factura comercial y del Documento de Transporte sea consistente con la que figura en los registros aduaneros, considerando las normas de declaración aduanera aplicables» · punto_propio
- **N4** Condicion «Constancia de registro aduanero del ingreso» — La entidad debe contar con constancia del registro aduanero del ingreso al país de los bienes que originan el pago · tramo (exacta): «Cuenta con constancia del registro aduanero del ingreso al país de los bienes que originan el pago a cancelarse» · punto_propio
- **N5** Condicion «Copia de factura comercial del exterior» — La entidad debe contar con copia de factura comercial emitida en el exterior a nombre del cliente residente, con datos del emisor, importador argentino, cantidad, descripción de mercadería, condición de venta y valor · tramo (exacta): «Cuenta con copia de factura comercial emitida en el exterior a nombre del cliente residente en el país, que efectúa la compra al exterior, donde conste nombre y dirección del emisor, nombre del importador argentino, la cantidad y descripción de la mercadería, condición de venta y valor de la factura» · punto_propio
- **N6** Condicion «Copia del Documento de Transporte» — La entidad debe contar con copia del Documento de Transporte (Conocimiento de Embarque, Carta de Porte o Guía Aérea) · tramo (exacta): «Cuenta con copia del Documento de Transporte (Conocimiento de Embarque – Carta de Porte – Guía Aérea)» · punto_propio
- **N7** Condicion «Declaración en Relevamiento de activos y pasivos externos» — La entidad debe contar con constancia de que la operación se encuentra declarada, cuando corresponda, en la última presentación vencida del Relevamiento de activos y pasivos externos · tramo (exacta): «Cuenta con constancia de que la operación se encuentra declarada, en caso de corresponder, en la última presentación vencida del "Relevamiento de activos y pasivos externos"» · punto_propio
- **N8** Condicion «Declaración jurada de saldo de deuda para importaciones anteriores a 01/11/19» — Para importaciones oficializadas antes del 01/11/19, la entidad debe contar con declaración jurada del saldo de deuda pendiente, firmada por el importador, su representante legal o apoderado con facultades suficientes · props: `{"umbrales": [{"tramo": "con anterioridad al 01/11/19", "comparacion": "no_determinada", "regla_comparacion": "limite_relativo:sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}]}` · tramo (exacta): «En el caso de importaciones oficializadas con anterioridad al 01/11/19, cuenta con una declaración jurada consignando el saldo de deuda pendiente a la fecha, firmada por el importador o quien ejerza su representación legal o un apoderado con facultades suficientes para asumir este compromiso en nombre del importador» · punto_propio
- **N9** Condicion «Determinación de fecha de vencimiento de obligación» — La documentación debe permitir establecer la fecha de vencimiento de la obligación con el exterior, o en su defecto, que la operación no tiene fecha de vencimiento pactada · tramo (exacta): «Que la documentación presentada le permita establecer la fecha de vencimiento de la obligación con el exterior por parte del importador o, en su defecto, que la operación no tiene una fecha de vencimiento pactada» · punto_propio
- **N10** Operacion «Certificación de cumplimiento de requisitos para pago de importación» — La entidad encargada del seguimiento de la oficialización certifica el cumplimiento de las condiciones para el pago de importaciones de bienes con registro aduanero, o cuenta con certificación emitida por la entidad responsable · props: `{"tipo": "Certificación de requisitos"}` · tramo (exacta): «Certifica en carácter de entidad encargada del seguimiento de la oficialización que se cumplen las condiciones que se enuncian a continuación o cuenta con una certificación para realizar el pago emitida por la entidad que tiene tal responsabilidad» · punto_propio
- **N11** Restriccion «Límite de pagos no supera monto facturado» — El total de los pagos realizados con imputación a la oficialización de importación, incluyendo el pago solicitado, no puede superar el monto facturado en la condición de compra pactada · props: `{"tipo": "limite_cuantitativo", "umbrales": [{"tramo": "no supera el monto facturado en la condición de compra pactada", "comparacion": "maximo_inclusivo", "base": "monto facturado en la condición de compra pactada", "regla_comparacion": "limite_relativo:negacion:raiz_super", "origen": "e1", "tramo_verificado": "exacta"}]}` · tramo (exacta): «Que el total de los pagos realizados con imputación a la oficialización de importación, incluyendo el pago cuyo curso se está solicitando, no supera el monto facturado en la condición de compra pactada» · punto_propio
- **N12** Sujeto «Entidades autorizadas a operar en cambios (Exterior)» · props: `{"nivel": "rol"}` · sin tramo · punto_propio · compartido (344 procedencias en el grafo)
- **N13** TextoOrdenado «Texto Ordenado Exterior Cambios» · props: `{"archivo": "TO_exterior_cambios_actual.pdf", "materia": "Exterior y cambios", "version": "Comunicación A 8307 (vigencia 26/08/2025)"}` · sin tramo · punto_propio · compartido (930 procedencias en el grafo)

**Aristas de la extracción (10)**
- **A1** N1 —condicion_de→ N10 Operacion «Certificación de cumplimiento de requisitos para pago de importación»
- **A2** N2 —condicion_de→ N10 Operacion «Certificación de cumplimiento de requisitos para pago de importación»
- **A3** N3 —condicion_de→ N10 Operacion «Certificación de cumplimiento de requisitos para pago de importación»
- **A4** N4 —condicion_de→ N10 Operacion «Certificación de cumplimiento de requisitos para pago de importación»
- **A5** N5 —condicion_de→ N10 Operacion «Certificación de cumplimiento de requisitos para pago de importación»
- **A6** N6 —condicion_de→ N10 Operacion «Certificación de cumplimiento de requisitos para pago de importación»
- **A7** N7 —condicion_de→ N10 Operacion «Certificación de cumplimiento de requisitos para pago de importación»
- **A8** N8 —condicion_de→ N10 Operacion «Certificación de cumplimiento de requisitos para pago de importación»
- **A9** N9 —condicion_de→ N10 Operacion «Certificación de cumplimiento de requisitos para pago de importación»
- **A10** N10 —aplica_a→ N12 Sujeto «Entidades autorizadas a operar en cambios (Exterior)» (mención «la entidad interviniente», exacta, R4_sugerencia_modelo)

**Remisiones derivadas (2 aristas)**
- **R1–R2** N2 —remite_a→ `ext::10.2.4` (interna; 2 nodo(s) destino: Definicion «Deuda comercial por importación de bienes»; Definicion «Deuda comercial por importación de bienes») · evidencia «deuda por importaciones de bienes según lo dispuesto en el punto 10.2.4. vii) Que el total de»

**Estructurales (11)**: establecida_en → TextoOrdenado «Texto Ordenado Exterior Cambios» ×11

## 20. `ext::11.1.3.9` — estrato item (20 del sorteo) · ext · págs. 163 · estado `completo_ok_directo`

> *heredado (encabezado, S11):* Sección 11. Sistema de seguimiento de pagos de importaciones (SEPAIMPO).
> *heredado (encabezado, 11.1):* 11.1. Seguimiento de oficializaciones de importación.
> *heredado (intro, 11.1):* Quedarán comprendidas todas las oficializaciones de importación ocurridas a partir del 01/11/19 y aquellas que sean anteriores por las cuales se solicite realizar pagos a través del mercado de cambios a partir de la mencionada fecha. Por cada oficialización del despacho de importación, el importador deberá nominar una entidad para que se haga responsable del seguimiento de la oficialización. Esta entidad será la responsable de verificar el cumplimiento de las condiciones estipuladas en la presente normativa que habilitarán el acceso al mercado de cambios y/o la afectación de una oficialización a la regularización de un pago con registro aduanero pendiente. La entidad será originalmente nominada por el importador ante la ARCA, pudiendo el importador posteriormente modificarla en la medida que, a la fecha de la solicitud de cambio de entidad, no existan certificaciones emitidas de acceso al mercado de cambios que estén pendientes de uso. En caso de que el importador no haya nominado a una entidad al momento de la oficialización podrá posteriormente seleccionar una entidad que se haga cargo del seguimiento. Serán elegibles para el importador, quedando obligadas a llevar a cabo las responsabilidades asociadas al presente seguimiento, todas las entidades financieras y casas de cambio salvo aquellas que hayan notificado al BCRA que han optado por no operar en comercio exterior.
> *heredado (encabezado, 11.1.3):* 11.1.3. Certificación para el acceso al mercado de cambios para el pago de importaciones de
> *heredado (intro, 11.1.3):* bienes con registro de ingreso aduanero. A solicitud del importador, la entidad procederá a emitir la certificación que habilita el acceso del importador al mercado de cambios para realizar un pago con imputación del despacho de importación bajo seguimiento de la entidad, por cualquier entidad que opere en comercio exterior. La emisión de una certificación por parte de la entidad implica que, a la fecha de su emisión, se verifican todos los requisitos normativos previstos en el punto 10.3.2.1. En la certificación que emita la entidad para habilitar el acceso al mercado de cambios deberá constar al menos la siguiente información:
> *heredado (cierre, 11.1.3):* Las certificaciones tendrán una validez de 10 (diez) días hábiles a contar desde la fecha de emisión y serán transmitidas por la entidad emisora a la entidad por la cual se curse el pago por un medio seguro, en la medida que el importador haya presentado la documentación correspondiente y que se cumplan los requisitos para su emisión. La devolución de las certificaciones no utilizadas será efectuada entre las entidades involucradas. La entidad a cargo del seguimiento deberá considerar como utilizada toda certificación no devuelta.
> *propio:* 11.1.3.9. Código de concepto del régimen informativo de operaciones de cambio.

**Nodos (1)**
- **N1** TextoOrdenado «Texto Ordenado Exterior Cambios» · props: `{"archivo": "TO_exterior_cambios_actual.pdf", "materia": "Exterior y cambios", "version": "Comunicación A 8307 (vigencia 26/08/2025)"}` · sin tramo · punto_propio · compartido (930 procedencias en el grafo)

**Aristas de la extracción (0)**

**Remisiones derivadas (0 aristas)**

**Estructurales (0)**: 

## 21. `lingob::2.3.2.1` — estrato item (21 del sorteo) · lingob · págs. 7 · estado `aceptado_con_residuales`

> *heredado (encabezado, S2):* Sección 2. Directorio.
> *heredado (chapeau_seccion, S2):* Los miembros del Directorio deberán contar con los conocimientos y competencias necesarias para comprender claramente sus responsabilidades y funciones dentro del gobierno societario y obrar con lealtad y con la diligencia de un buen hombre de negocios en los asuntos de la entidad financie- ra. Se considera una buena práctica que el Directorio se conforme observando el criterio de paridad de género, a efectos de potenciar la discusión y enriquecer la toma de decisiones con respecto a estra- tegias, políticas y asunción de riesgos. En los casos en que la presidencia del Directorio sea ejercida por un miembro que desempeña tam- bién funciones ejecutivas, se adoptarán las medidas necesarias a los efectos de que las decisiones se mantengan en línea con los objetivos societarios.
> *heredado (encabezado, 2.3):* 2.3. Objetivos estratégicos y valores organizacionales.
> *heredado (intro, 2.3):* Con ajuste al objeto social establecido por la Asamblea de accionistas, se considera como bue- na práctica que el Directorio apruebe y supervise los objetivos estratégicos y los valores socie- tarios, comunicándolos a toda la organización. A esos efectos, el Directorio:
> *heredado (encabezado, 2.3.2):* 2.3.2. Se asegurará de que la Alta Gerencia implemente procedimientos para promover con-
> *heredado (intro, 2.3.2):* ductas profesionales y que prevengan y/o limiten la existencia de actividades o situacio- nes que puedan afectar negativamente la calidad del gobierno societario, tales como:
> *propio:* 2.3.2.1. Conflictos de intereses entre la entidad financiera, el Directorio, la Alta Gerencia y el grupo económico al que pertenece la entidad.

**Nodos (4)**
- **N1** Condicion «Conflictos de intereses entre entidad, Directorio, Alta Gerencia y grupo económico» — Situación de conflicto de intereses que puede existir entre la entidad financiera, sus órganos de gobierno (Directorio y Alta Gerencia) y el grupo económico del cual forma parte · tramo (exacta): «Conflictos de intereses entre la entidad financiera, el Directorio, la Alta Gerencia y el grupo económico al que pertenece la entidad» · punto_propio
- **N2** Obligacion «Implementar procedimientos para prevenir conflictos de intereses» — El Directorio debe asegurar que la Alta Gerencia implemente procedimientos para prevenir y/o limitar conflictos de intereses entre la entidad financiera, el Directorio, la Alta Gerencia y el grupo económico al que pertenece la entidad, como parte de las medidas para promover conductas profesionales y mantener la calidad del gobierno societario · props: `{"tipo": "otra"}` · tramo (exacta): «Se asegurará de que la Alta Gerencia implemente procedimientos para promover conductas profesionales y que prevengan y/o limiten la existencia de actividades o situaciones que puedan afectar negativamente la calidad del gobierno societario, tales como: […] Conflictos de intereses entre la entidad financiera, el Directorio, la Alta Gerencia y el grupo económico al que pertenece la entidad» · punto_propio
- **N3** Sujeto «Directorio» · props: `{"nivel": "clase", "alias": ["Consejo de Administración"]}` · sin tramo · punto_propio · compartido (67 procedencias en el grafo)
- **N4** TextoOrdenado «Lineamientos de Gobierno Societario» · props: `{"archivo": "lingob.pdf", "materia": "Lineamientos para el gobierno societario en entidades financieras", "version": "Comunicación A 7465 (vigencia 26/02/2022)"}` · sin tramo · punto_propio · compartido (137 procedencias en el grafo)

**Aristas de la extracción (2)**
- **A1** N1 —condicion_de→ N2 Obligacion «Implementar procedimientos para prevenir conflictos de intereses»
- **A2** N2 —aplica_a→ N3 Sujeto «Directorio» (mención «el Directorio», exacta, R1_label_exacto)

**Remisiones derivadas (0 aristas)**

**Estructurales (2)**: establecida_en → TextoOrdenado «Lineamientos de Gobierno Societario» ×2

## 22. `ext::3.15.2.3` — estrato item (22 del sorteo) · ext · págs. 42 · estado `completo_ok_directo`

> *heredado (encabezado, S3):* Sección 3. Disposiciones específicas para los egresos por el mercado de cambios
> *heredado (chapeau_seccion, S3):* Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–, adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables.
> *heredado (encabezado, 3.15):* 3.15. Cancelación por parte de entidades financieras de líneas de crédito del exterior aplicadas a la
> *heredado (intro, 3.15):* financiación de operaciones de comercio exterior y garantías financieras otorgadas.
> *heredado (encabezado, 3.15.2):* 3.15.2. Cancelación de garantías financieras otorgadas por entidades financieras locales.
> *heredado (intro, 3.15.2):* Las entidades financieras locales podrán acceder al mercado de cambios para hacer frente a sus obligaciones con no residentes por garantías financieras otorgadas a partir del 01/10/21, en la medida que se reúnan la totalidad de las siguientes condiciones:
> *propio:* 3.15.2.3. La contraparte del mencionado contrato es un no residente no vinculado con el residente que exportará los bienes y/o servicios.

**Nodos (2)**
- **N1** Condicion «Contraparte no residente no vinculada» — La contraparte del contrato debe ser un no residente no vinculado con el residente que exportará los bienes y/o servicios · tramo (exacta): «La contraparte del mencionado contrato es un no residente no vinculado con el residente que exportará los bienes y/o servicios» · punto_propio
- **N2** TextoOrdenado «Texto Ordenado Exterior Cambios» · props: `{"archivo": "TO_exterior_cambios_actual.pdf", "materia": "Exterior y cambios", "version": "Comunicación A 8307 (vigencia 26/08/2025)"}` · sin tramo · punto_propio · compartido (930 procedencias en el grafo)

**Aristas de la extracción (0)**

**Remisiones derivadas (0 aristas)**

**Estructurales (1)**: establecida_en → TextoOrdenado «Texto Ordenado Exterior Cambios» ×1

## 23. `ext::10.10.2.12` — estrato item (23 del sorteo) · ext · págs. 157 · estado `completo_ok_directo`

> *heredado (encabezado, S10):* Sección 10. Pagos de importaciones y otras compras de bienes en el exterior.
> *heredado (encabezado, 10.10):* 10.10. Disposiciones complementarias para importaciones de bienes que tuvieron o tendrán registro
> *heredado (intro, 10.10):* de ingreso aduanero a partir del 13/12/23.
> *heredado (encabezado, 10.10.2):* 10.10.2. Pagos de importaciones de bienes con registro de ingreso aduanero pendiente.
> *heredado (intro, 10.10.2):* Las entidades podrán dar acceso al mercado de cambios para cursar pagos con registro de ingreso aduanero pendiente por operaciones no comprendidas en el punto 10.6.6. cuando, en adición a los restantes requisitos aplicables, se verifique alguna de las siguientes situaciones:
> *heredado (cierre, 10.10.2):* Se podrá considerar como importación de bienes de capital a: i) aquellas que correspondan a bienes cuyas posiciones arancelarias se encuentren clasificadas como BK en la Nomenclatura Común del MERCOSUR (Decreto 690/02 y complementarias) y ii) aquellas que incluyan otros bienes en la medida que los bienes clasificados como BK representen como mínimo el 90% (noventa por ciento) del valor FOB total de la operación y la entidad cuente con una declaración jurada del cliente en la cual deje constancia de que los restantes bienes son repuestos, accesorios o materiales necesarios para el funcionamiento, construcción o instalación de los bienes de capital que se están adquiriendo.
> *propio:* 10.10.2.12. Se trata de un pago de importaciones de bienes oficializadas a partir del 13/06/24 como parte de la implementación y ejecución de un plan de acción establecido por la Secretaría de Transporte del Ministerio de Economía en el marco de la emergencia pública en materia ferroviaria para los servicios de transporte de pasajeros y cargas de jurisdicción nacional establecida en el Decreto 525/24. La entidad deberá contar con la documentación emitida por la Secretaría de Transporte que certifique que los bienes a abonar se encuentran comprendidos en el Plan de Acción establecido por esa secretaría.

**Nodos (5)**
- **N1** Condicion «Bienes comprendidos en Plan de Acción Secretaría Transporte» — Los bienes a abonar se encuentran comprendidos en el Plan de Acción establecido por la Secretaría de Transporte · tramo (exacta): «los bienes a abonar se encuentran comprendidos en el Plan de Acción establecido por esa secretaría» · punto_propio
- **N2** Obligacion «Contar con documentación Secretaría Transporte» — La entidad deberá contar con la documentación emitida por la Secretaría de Transporte que certifique que los bienes a abonar se encuentran comprendidos en el Plan de Acción establecido por esa secretaría · props: `{"tipo": "otra"}` · tramo (exacta): «La entidad deberá contar con la documentación emitida por la Secretaría de Transporte que certifique que los bienes a abonar se encuentran comprendidos en el Plan de Acción establecido por esa secretaría» · punto_propio
- **N3** Operacion «Pago importaciones bienes oficializadas 13/06/24» — Pago de importaciones de bienes oficializadas a partir del 13/06/24 como parte de la implementación y ejecución de un plan de acción establecido por la Secretaría de Transporte del Ministerio de Economía en el marco de la emergencia pública en materia ferroviaria para los servicios de transporte de pasajeros y cargas de jurisdicción nacional establecida en el Decreto 525/24 · props: `{"tipo": "Pago de importaciones de bienes"}` · tramo (exacta): «Se trata de un pago de importaciones de bienes oficializadas a partir del 13/06/24 como parte de la implementación y ejecución de un plan de acción establecido por la Secretaría de Transporte del Ministerio de Economía en el marco de la emergencia pública en materia ferroviaria para los servicios de transporte de pasajeros y cargas de jurisdicción nacional establecida en el Decreto 525/24» · punto_propio
- **N4** Sujeto «Entidades autorizadas a operar en cambios (Exterior)» · props: `{"nivel": "rol"}` · sin tramo · punto_propio · compartido (344 procedencias en el grafo)
- **N5** TextoOrdenado «Texto Ordenado Exterior Cambios» · props: `{"archivo": "TO_exterior_cambios_actual.pdf", "materia": "Exterior y cambios", "version": "Comunicación A 8307 (vigencia 26/08/2025)"}` · sin tramo · punto_propio · compartido (930 procedencias en el grafo)

**Aristas de la extracción (3)**
- **A1** N1 —condicion_de→ N2 Obligacion «Contar con documentación Secretaría Transporte»
- **A2** N2 —aplica_a→ N4 Sujeto «Entidades autorizadas a operar en cambios (Exterior)» (mención «La entidad», exacta, R4_sugerencia_modelo)
- **A3** N2 —condiciona→ N3 Operacion «Pago importaciones bienes oficializadas 13/06/24»

**Remisiones derivadas (0 aristas)**

**Estructurales (3)**: establecida_en → TextoOrdenado «Texto Ordenado Exterior Cambios» ×3

## 24. `ext::10.6.6.2` — estrato item (24 del sorteo) · ext · págs. 150 · estado `aceptado_con_residuales`

> *heredado (encabezado, S10):* Sección 10. Pagos de importaciones y otras compras de bienes en el exterior.
> *heredado (encabezado, 10.6):* 10.6. Otras disposiciones.
> *heredado (encabezado, 10.6.6):* 10.6.6. Importaciones temporales de la posición arancelaria 1201.90.00 de la NCM (porotos
> *heredado (intro, 10.6.6):* de soja excluidos p/siembra). Las entidades para otorgar acceso al mercado de cambios para el pago de importaciones temporales de la posición arancelaria 1201.90.00 de la NCM (porotos de soja excluidos p/siembra) con registro de ingreso aduanero a partir del 13/12/23, adicionalmente a los restantes requisitos normativos aplicables, deberán verificar que el cliente por el monto que pretende abonar:
> *propio:* 10.6.6.2. liquida simultáneamente cobros anticipados o prefinanciaciones de exportaciones del exterior o prefinanciaciones de exportaciones otorgadas por entidades financieras locales con fondeo en líneas de crédito del exterior, que tengan una fecha de vencimiento que sea igual o posterior a la fecha en que se producirá la exportación de los bienes elaborados a partir de aquellos importados temporariamente que se abonan.

**Nodos (5)**
- **N1** Condicion «Vencimiento igual o posterior a fecha de exportación» — La fecha de vencimiento de los cobros anticipados o prefinanciaciones debe ser igual o posterior a la fecha en que se producirá la exportación de los bienes elaborados a partir de los importados temporariamente · tramo (exacta): «que tengan una fecha de vencimiento que sea igual o posterior a la fecha en que se producirá la exportación de los bienes elaborados a partir de aquellos importados temporariamente que se abonan» · punto_propio
- **N2** Obligacion «Verificar liquidación simultánea de cobros anticipados o prefinanciaciones» — Las entidades deberán verificar que el cliente liquida simultáneamente cobros anticipados o prefinanciaciones de exportaciones del exterior o prefinanciaciones de exportaciones otorgadas por entidades financieras locales con fondeo en líneas de crédito del exterior, con vencimiento igual o posterior a la fecha de exportación de los bienes elaborados a partir de importaciones temporales · props: `{"tipo": "presentacion_informativa"}` · tramo (exacta): «Las entidades para otorgar acceso al mercado de cambios para el pago de importaciones temporales de la posición arancelaria 1201.90.00 de la NCM (porotos de soja excluidos p/siembra) con registro de ingreso aduanero a partir del 13/12/23, adicionalmente a los restantes requisitos normativos aplicables, deberán verificar que el cliente por el monto que pretende abonar: […] liquida simultáneamente cobros anticipados o prefinanciaciones de exportaciones del exterior o prefinanciaciones de exportaciones otorgadas por entidades financieras locales con fondeo en líneas de crédito del exterior, que tengan una fecha de vencimiento que sea igual o posterior a la fecha en que se producirá la exportación de los bienes elaborados a partir de aquellos importados temporariamente que se abonan» · punto_propio
- **N3** Operacion «Liquidación simultánea de cobros anticipados o prefinanciaciones» — Liquidación simultánea de cobros anticipados o prefinanciaciones de exportaciones del exterior o prefinanciaciones de exportaciones otorgadas por entidades financieras locales con fondeo en líneas de crédito del exterior, con vencimiento igual o posterior a la fecha de exportación de los bienes elaborados a partir de importaciones temporales · props: `{"tipo": "liquidación de cobros anticipados y prefinanciaciones"}` · tramo (exacta): «liquida simultáneamente cobros anticipados o prefinanciaciones de exportaciones del exterior o prefinanciaciones de exportaciones otorgadas por entidades financieras locales con fondeo en líneas de crédito del exterior, que tengan una fecha de vencimiento que sea igual o posterior a la fecha en que se producirá la exportación de los bienes elaborados a partir de aquellos importados temporariamente que se abonan» · punto_propio
- **N4** Sujeto «Entidades autorizadas a operar en cambios (Exterior)» · props: `{"nivel": "rol"}` · sin tramo · punto_propio · compartido (344 procedencias en el grafo)
- **N5** TextoOrdenado «Texto Ordenado Exterior Cambios» · props: `{"archivo": "TO_exterior_cambios_actual.pdf", "materia": "Exterior y cambios", "version": "Comunicación A 8307 (vigencia 26/08/2025)"}` · sin tramo · punto_propio · compartido (930 procedencias en el grafo)

**Aristas de la extracción (3)**
- **A1** N1 —condicion_de→ N3 Operacion «Liquidación simultánea de cobros anticipados o prefinanciaciones»
- **A2** N2 —aplica_a→ N4 Sujeto «Entidades autorizadas a operar en cambios (Exterior)» (mención «Las entidades», exacta, R4_sugerencia_modelo)
- **A3** N2 —regula→ N3 Operacion «Liquidación simultánea de cobros anticipados o prefinanciaciones»

**Remisiones derivadas (0 aristas)**

**Estructurales (3)**: establecida_en → TextoOrdenado «Texto Ordenado Exterior Cambios» ×3

## 25. `ext::2.6.1.2` — estrato item (25 del sorteo) · ext · págs. 12 · estado `aceptado_tras_reintento`

> *heredado (encabezado, S2):* Sección 2. Disposiciones específicas para los ingresos por el mercado de cambios.
> *heredado (encabezado, 2.6):* 2.6. Excepción de liquidación de cobros de exportaciones de bienes y servicios para los
> *heredado (intro, 2.6):* beneficiarios del “Régimen de fomento para las exportaciones de la economía del conocimiento”.
> *heredado (encabezado, 2.6.1):* 2.6.1. Las personas jurídicas inscriptas en el Registro Nacional de Beneficiarios del Régimen
> *heredado (intro, 2.6.1):* de Promoción de la Economía del Conocimiento y que sean beneficiarios de lo dispuesto en el Capítulo II del Decreto 679/22 quedarán exceptuados de la obligación de liquidación de los cobros de exportaciones de bienes y servicios que correspondan a actividades de la economía del conocimiento, en la medida que se cumpla la totalidad de las siguientes condiciones:
> *heredado (cierre, 2.6.1):* Los montos de las divisas a ser afectadas en el marco de lo dispuesto en el Capítulo II del Decreto 679/22 no pueden resultar alcanzadas por ningún otro tratamiento cambiario diferencial que no sea aquel previsto en dicho capítulo.
> *propio:* 2.6.1.2. cuenten con una “Certificación de incremento de exportaciones asociadas a la economía del conocimiento (Decreto 679/22)” en los términos previstos en el punto 2.6.2.;

**Nodos (6)**
- **N1** Condicion «Condición: certificación incremento exportaciones economía conocimiento» — Contar con una Certificación de incremento de exportaciones asociadas a la economía del conocimiento (Decreto 679/22) en los términos previstos en el punto 2.6.2. · tramo (exacta): «cuenten con una "Certificación de incremento de exportaciones asociadas a la economía del conocimiento (Decreto 679/22)" en los términos previstos en el punto 2.6.2.» · punto_propio
- **N2** Condicion «Condición: montos divisas no alcanzados por otro tratamiento cambiario» — Los montos de las divisas a ser afectadas en el marco de lo dispuesto en el Capítulo II del Decreto 679/22 no pueden resultar alcanzadas por ningún otro tratamiento cambiario diferencial que no sea aquel previsto en dicho capítulo. · tramo (exacta): «Los montos de las divisas a ser afectadas en el marco de lo dispuesto en el Capítulo II del Decreto 679/22 no pueden resultar alcanzadas por ningún otro tratamiento cambiario diferencial que no sea aquel previsto en dicho capítulo» · herencia_encabezado
- **N3** Definicion «Sujeto alcanzado: personas jurídicas inscriptas Registro Nacional Beneficiarios» — Las personas jurídicas inscriptas en el Registro Nacional de Beneficiarios del Régimen de Promoción de la Economía del Conocimiento y que sean beneficiarios de lo dispuesto en el Capítulo II del Decreto 679/22. · props: `{"termino": "beneficiarios de la excepción de liquidación de cobros de exportaciones"}` · tramo (exacta): «Las personas jurídicas inscriptas en el Registro Nacional de Beneficiarios del Régimen de Promoción de la Economía del Conocimiento y que sean beneficiarios de lo dispuesto en el Capítulo II del Decreto 679/22» · herencia_encabezado
- **N4** Excepcion «Excepción liquidación cobros exportaciones economía conocimiento» — Las personas jurídicas inscriptas en el Registro Nacional de Beneficiarios del Régimen de Promoción de la Economía del Conocimiento y que sean beneficiarios de lo dispuesto en el Capítulo II del Decreto 679/22 quedan exceptuadas de la obligación de liquidación de los cobros de exportaciones de bienes y servicios que correspondan a actividades de la economía del conocimiento. · tramo (exacta): «quedarán exceptuados de la obligación de liquidación de los cobros de exportaciones de bienes y servicios que correspondan a actividades de la economía del conocimiento» · herencia_encabezado
- **N5** Sujeto «Beneficiarios del Régimen de Promoción de la Economía del Conocimiento» · props: `{"nivel": "clase"}` · sin tramo · herencia_encabezado · compartido (3 procedencias en el grafo)
- **N6** TextoOrdenado «Texto Ordenado Exterior Cambios» · props: `{"archivo": "TO_exterior_cambios_actual.pdf", "materia": "Exterior y cambios", "version": "Comunicación A 8307 (vigencia 26/08/2025)"}` · sin tramo · punto_propio · compartido (930 procedencias en el grafo)

**Aristas de la extracción (3)**
- **A1** N1 —condicion_de→ N4 Excepcion «Excepción liquidación cobros exportaciones economía conocimiento»
- **A2** N2 —condicion_de→ N4 Excepcion «Excepción liquidación cobros exportaciones economía conocimiento»
- **A3** N4 —aplica_a→ N5 Sujeto «Beneficiarios del Régimen de Promoción de la Economía del Conocimiento» (mención «Las personas jurídicas inscriptas en el Registro Nacional de Beneficiarios del Régimen de Promoción de la Economía del Conocimiento y que sean beneficiarios de lo dispuesto en el Capítulo II del Decreto 679/22», exacta, R4_sugerencia_modelo)

**Remisiones derivadas (6 aristas)**
- **R1–R6** N1 —remite_a→ `ext::2.6.2` (interna; 6 nodo(s) destino: Condicion «Verificación de totalidad de requisitos para emisión de certificaciones»; Condicion «Verificación de totalidad de requisitos posteriores»; Obligacion «Nominar única entidad financiera local responsable»; Obligacion «Nominación de entidad financiera local única»; Operacion «Cobros de exportaciones de bienes o servicios»; Potestad «Emisión de certificaciones por entidad nominada») · evidencia «conocimiento (Decreto 679/22)” en los términos previstos en el punto 2.6.2.;»

**Estructurales (4)**: establecida_en → TextoOrdenado «Texto Ordenado Exterior Cambios» ×4

## 26. `ctacte::12.1.2.1` — estrato item (26 del sorteo) · ctacte · págs. 55 · estado `aceptado_con_residuales`

> *heredado (encabezado, S12):* Sección 12. Disposiciones generales.
> *heredado (encabezado, 12.1):* 12.1. Recomendaciones para el uso de cajeros automáticos.
> *heredado (encabezado, 12.1.2):* 12.1.2. A continuación se enumeran las recomendaciones y recaudos que, como mínimo, de-
> *heredado (intro, 12.1.2):* berán comunicarse a los usuarios:
> *propio:* 12.1.2.1. Solicitar al personal del banco toda la información que estimen necesaria acerca del uso de los cajeros automáticos al momento de acceder por prime- ra vez al servicio o ante cualquier duda que se les presente posteriormente.

**Nodos (3)**
- **N1** Obligacion «Comunicar recomendaciones cajeros automáticos» — Comunicar a los usuarios la recomendación de solicitar al personal del banco toda la información que estimen necesaria acerca del uso de los cajeros automáticos al momento de acceder por primera vez al servicio o ante cualquier duda que se les presente posteriormente · props: `{"tipo": "comunicacion_a_cliente", "frecuencia": "al momento de acceder por primera vez al servicio o ante cualquier duda que se les presente posteriormente"}` · tramo (no): «deberán comunicarse a los usuarios: Solicitar al personal del banco toda la información que estimen necesaria acerca del uso de los cajeros automáticos al momento de acceder por primera vez al servicio o ante cualquier duda que se les presente posteriormente» · punto_propio
- **N2** Sujeto «Bancos» · props: `{"nivel": "clase"}` · sin tramo · punto_propio · compartido (149 procedencias en el grafo)
- **N3** TextoOrdenado «Cuentas corrientes» · props: `{"archivo": "ctacte.pdf", "materia": "Reglamentación de la cuenta corriente bancaria", "version": "Comunicación A 8444 (vigencia 05/06/2026)"}` · sin tramo · punto_propio · compartido (380 procedencias en el grafo)

**Aristas de la extracción (1)**
- **A1** N1 —aplica_a→ N2 Sujeto «Bancos» (mención «los bancos», no, R4_sugerencia_modelo)

**Remisiones derivadas (0 aristas)**

**Estructurales (1)**: establecida_en → TextoOrdenado «Cuentas corrientes» ×1

## 27. `ext::11.1.3.1` — estrato item (27 del sorteo) · ext · págs. 162 · estado `aceptado_con_residuales`

> *heredado (encabezado, S11):* Sección 11. Sistema de seguimiento de pagos de importaciones (SEPAIMPO).
> *heredado (encabezado, 11.1):* 11.1. Seguimiento de oficializaciones de importación.
> *heredado (intro, 11.1):* Quedarán comprendidas todas las oficializaciones de importación ocurridas a partir del 01/11/19 y aquellas que sean anteriores por las cuales se solicite realizar pagos a través del mercado de cambios a partir de la mencionada fecha. Por cada oficialización del despacho de importación, el importador deberá nominar una entidad para que se haga responsable del seguimiento de la oficialización. Esta entidad será la responsable de verificar el cumplimiento de las condiciones estipuladas en la presente normativa que habilitarán el acceso al mercado de cambios y/o la afectación de una oficialización a la regularización de un pago con registro aduanero pendiente. La entidad será originalmente nominada por el importador ante la ARCA, pudiendo el importador posteriormente modificarla en la medida que, a la fecha de la solicitud de cambio de entidad, no existan certificaciones emitidas de acceso al mercado de cambios que estén pendientes de uso. En caso de que el importador no haya nominado a una entidad al momento de la oficialización podrá posteriormente seleccionar una entidad que se haga cargo del seguimiento. Serán elegibles para el importador, quedando obligadas a llevar a cabo las responsabilidades asociadas al presente seguimiento, todas las entidades financieras y casas de cambio salvo aquellas que hayan notificado al BCRA que han optado por no operar en comercio exterior.
> *heredado (encabezado, 11.1.3):* 11.1.3. Certificación para el acceso al mercado de cambios para el pago de importaciones de
> *heredado (intro, 11.1.3):* bienes con registro de ingreso aduanero. A solicitud del importador, la entidad procederá a emitir la certificación que habilita el acceso del importador al mercado de cambios para realizar un pago con imputación del despacho de importación bajo seguimiento de la entidad, por cualquier entidad que opere en comercio exterior. La emisión de una certificación por parte de la entidad implica que, a la fecha de su emisión, se verifican todos los requisitos normativos previstos en el punto 10.3.2.1. En la certificación que emita la entidad para habilitar el acceso al mercado de cambios deberá constar al menos la siguiente información:
> *heredado (cierre, 11.1.3):* Las certificaciones tendrán una validez de 10 (diez) días hábiles a contar desde la fecha de emisión y serán transmitidas por la entidad emisora a la entidad por la cual se curse el pago por un medio seguro, en la medida que el importador haya presentado la documentación correspondiente y que se cumplan los requisitos para su emisión. La devolución de las certificaciones no utilizadas será efectuada entre las entidades involucradas. La entidad a cargo del seguimiento deberá considerar como utilizada toda certificación no devuelta.
> *propio:* 11.1.3.1. Código de la entidad que emite la certificación.

**Nodos (1)**
- **N1** TextoOrdenado «Texto Ordenado Exterior Cambios» · props: `{"archivo": "TO_exterior_cambios_actual.pdf", "materia": "Exterior y cambios", "version": "Comunicación A 8307 (vigencia 26/08/2025)"}` · sin tramo · punto_propio · compartido (930 procedencias en el grafo)

**Aristas de la extracción (0)**

**Remisiones derivadas (0 aristas)**

**Estructurales (0)**: 

## 28. `ext::7.8.2.5` — estrato item (28 del sorteo) · ext · págs. 92 · estado `completo_ok_directo`

> *heredado (encabezado, S7):* Sección 7. Cobros de exportaciones de bienes.
> *heredado (encabezado, 7.8):* 7.8. Otras disposiciones.
> *heredado (encabezado, 7.8.2):* 7.8.2. Exportaciones bajo los regímenes de precios revisables o concentrado de minerales.
> *heredado (intro, 7.8.2):* En los casos de exportaciones de productos que se comercializan sobre la base de precios FOB sujetos a una determinación posterior al momento de registro de la operación (Exportación de mercaderías con precios revisables – Resolución General 4073-E/17 de la Administración Federal de Ingresos Públicos) o al amparo del Régimen de Concentrados de Minerales (Resolución General 2108/06 de la Administración Federal de Ingresos Públicos) será aplicable lo siguiente:
> *propio:* 7.8.2.5. En caso de que un permiso de embarque definitivo esté asociado a un embarque provisorio oficializado con anterioridad al 02/09/19, las entidades podrán dar el cumplido de embarque del permiso definitivo.

**Nodos (5)**
- **N1** Condicion «Permiso embarque definitivo asociado a embarque provisorio anterior» — Supuesto en que un permiso de embarque definitivo está asociado a un embarque provisorio oficializado antes del 2 de septiembre de 2019 · props: `{"umbrales": [{"tramo": "con anterioridad al 02/09/19", "comparacion": "no_determinada", "regla_comparacion": "limite_relativo:sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}]}` · tramo (exacta): «En caso de que un permiso de embarque definitivo esté asociado a un embarque provisorio oficializado con anterioridad al 02/09/19» · punto_propio
- **N2** Operacion «Cumplido de embarque del permiso definitivo» — Acto de dar el cumplido de embarque del permiso de embarque definitivo · props: `{"tipo": "Cumplido de embarque"}` · tramo (exacta): «dar el cumplido de embarque del permiso definitivo» · punto_propio
- **N3** Potestad «Facultad de dar cumplido de embarque definitivo» — Las entidades quedan facultadas a dar el cumplido de embarque del permiso de embarque definitivo cuando se verifica el supuesto de asociación con embarque provisorio anterior · tramo (exacta): «las entidades podrán dar el cumplido de embarque del permiso definitivo» · punto_propio
- **N4** Sujeto «Entidades autorizadas a operar en cambios (Exterior)» · props: `{"nivel": "rol"}` · sin tramo · punto_propio · compartido (344 procedencias en el grafo)
- **N5** TextoOrdenado «Texto Ordenado Exterior Cambios» · props: `{"archivo": "TO_exterior_cambios_actual.pdf", "materia": "Exterior y cambios", "version": "Comunicación A 8307 (vigencia 26/08/2025)"}` · sin tramo · punto_propio · compartido (930 procedencias en el grafo)

**Aristas de la extracción (2)**
- **A1** N1 —condicion_de→ N3 Potestad «Facultad de dar cumplido de embarque definitivo»
- **A2** N3 —aplica_a→ N4 Sujeto «Entidades autorizadas a operar en cambios (Exterior)» (mención «las entidades», exacta, R4_sugerencia_modelo)

**Remisiones derivadas (0 aristas)**

**Estructurales (3)**: establecida_en → TextoOrdenado «Texto Ordenado Exterior Cambios» ×3

## 29. `ctacte::8.4.2` — estrato item (29 del sorteo) · ctacte · págs. 46 · estado `completo_ok_directo`

> *heredado (encabezado, S8):* Sección 8. “Central de cheques rechazados”, “Central de cuentacorrentistas inhabili- tados” y “Central de cheques denunciados como extraviados, sustraídos o adulterados”.
> *heredado (encabezado, 8.4):* 8.4. Cancelación de las multas después de vencido el plazo legalmente establecido.
> *heredado (intro, 8.4):* Se demostrará con cualquiera de las siguientes alternativas:
> *propio:* 8.4.2. Consignación judicial del importe de la multa.

**Nodos (2)**
- **N1** Condicion «Consignación judicial de multa» — Se demuestra la cancelación de la multa mediante consignación judicial de su importe · tramo (exacta): «Consignación judicial del importe de la multa» · punto_propio
- **N2** TextoOrdenado «Cuentas corrientes» · props: `{"archivo": "ctacte.pdf", "materia": "Reglamentación de la cuenta corriente bancaria", "version": "Comunicación A 8444 (vigencia 05/06/2026)"}` · sin tramo · punto_propio · compartido (380 procedencias en el grafo)

**Aristas de la extracción (0)**

**Remisiones derivadas (0 aristas)**

**Estructurales (1)**: establecida_en → TextoOrdenado «Cuentas corrientes» ×1

## 30. `ext::13.3.6` — estrato item (30 del sorteo) · ext · págs. 171 · estado `aceptado_con_residuales`

> *heredado (encabezado, S13):* Sección 13. Pagos de servicios prestados por no residentes.
> *heredado (encabezado, 13.3):* 13.3. Pagos de servicios que fueron o serán prestados o devengados a partir del 13/12/23 con
> *heredado (intro, 13.3):* anterioridad a lo previsto en los puntos 13.2.3. a 13.2.7. También será admisible el acceso para el pago de servicios que fueron o serán prestados o devengados a partir del 13/12/23 con antelación a los plazos previstos en los puntos 13.2.3. a 13.2.7., cuando adicionalmente a los restantes requisitos normativo, se verifique el encuadre en alguna de las siguientes situaciones:
> *propio:* 13.3.6. el pago corresponda a la cancelación de deudas por operaciones financiadas o garantizadas con anterioridad al 13/12/23 por entidades financieras locales o del exterior; o

**Nodos (2)**
- **N1** Condicion «Pago por cancelación de deudas financiadas» — El pago corresponde a la cancelación de deudas por operaciones que fueron financiadas o garantizadas con anterioridad al 13/12/23 por entidades financieras locales o del exterior. · props: `{"umbrales": [{"tramo": "con anterioridad al 13/12/23", "comparacion": "no_determinada", "regla_comparacion": "limite_relativo:sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}]}` · tramo (exacta): «el pago corresponda a la cancelación de deudas por operaciones financiadas o garantizadas con anterioridad al 13/12/23 por entidades financieras locales o del exterior» · punto_propio
- **N2** TextoOrdenado «Texto Ordenado Exterior Cambios» · props: `{"archivo": "TO_exterior_cambios_actual.pdf", "materia": "Exterior y cambios", "version": "Comunicación A 8307 (vigencia 26/08/2025)"}` · sin tramo · punto_propio · compartido (930 procedencias en el grafo)

**Aristas de la extracción (0)**

**Remisiones derivadas (0 aristas)**

**Estructurales (1)**: establecida_en → TextoOrdenado «Texto Ordenado Exterior Cambios» ×1

## 31. `ext::1.7` — estrato no_item (1 del sorteo) · ext · págs. 7 · estado `completo_ok_directo`

> *heredado (encabezado, S1):* Sección 1. Disposiciones generales.
> *propio:* 1.7. Las entidades deberán cumplir con las normas sobre “Prevención del lavado de activos, del financiamiento del terrorismo y otras actividades ilícitas”.

**Nodos (3)**
- **N1** Obligacion «Cumplimiento normas prevención lavado activos» — Las entidades deberán cumplir con las normas sobre prevención del lavado de activos, del financiamiento del terrorismo y otras actividades ilícitas · props: `{"tipo": "otra"}` · tramo (exacta): «Las entidades deberán cumplir con las normas sobre "Prevención del lavado de activos, del financiamiento del terrorismo y otras actividades ilícitas"» · punto_propio
- **N2** Sujeto «Entidades autorizadas a operar en cambios (Exterior)» · props: `{"nivel": "rol"}` · sin tramo · punto_propio · compartido (344 procedencias en el grafo)
- **N3** TextoOrdenado «Texto Ordenado Exterior Cambios» · props: `{"archivo": "TO_exterior_cambios_actual.pdf", "materia": "Exterior y cambios", "version": "Comunicación A 8307 (vigencia 26/08/2025)"}` · sin tramo · punto_propio · compartido (930 procedencias en el grafo)

**Aristas de la extracción (1)**
- **A1** N1 —aplica_a→ N2 Sujeto «Entidades autorizadas a operar en cambios (Exterior)» (mención «Las entidades», exacta, R4_sugerencia_modelo)

**Remisiones derivadas (0 aristas)**

**Estructurales (1)**: establecida_en → TextoOrdenado «Texto Ordenado Exterior Cambios» ×1

## 32. `cap::6.1.4.2` — estrato no_item (2 del sorteo) · cap · págs. 118 · estado `completo_ok_directo`

> *heredado (encabezado, S6):* Sección 6. Capital mínimo por riesgo de mercado.
> *heredado (encabezado, 6.1):* 6.1. Exigencia.
> *heredado (intro, 6.1):* El riesgo de mercado se define como la posibilidad de sufrir pérdidas en posiciones registra- das dentro y fuera de balance a raíz de las fluctuaciones adversas en los precios de mercado. La exigencia de capital por riesgo de mercado (RM) será la suma aritmética de la exigencia de capital por los riesgos por tasa de interés (RT), acciones (RA), tipo de cambio (RTC), produc- tos básicos (RPB) y opciones (ROP).
> *heredado (intro, 6.1):* RM = RT + RA + RTC + RPB + ROP
> *heredado (intro, 6.1):* Para su determinación, las entidades deberán emplear el Método de Medición Estándar pre- visto en el punto 6.1.4.
> *heredado (encabezado, 6.1.4):* 6.1.4. Medición de los riesgos de mercado.
> *propio:* 6.1.4.2. Para calcular la exigencia de capital por el riesgo de precio de opciones las en- tidades podrán usar el enfoque simplificado (previsto en el punto 6.6.2.) o el método delta-plus (establecido en el punto 6.6.3.), según corresponda.

**Nodos (6)**
- **N1** Comunicacion «Punto 6.6.2» · props: `{"codigo": "6.6.2"}` · tramo (exacta): «enfoque simplificado (previsto en el punto 6.6.2.)» · punto_propio
- **N2** Comunicacion «Punto 6.6.3» · props: `{"codigo": "6.6.3"}` · tramo (exacta): «método delta-plus (establecido en el punto 6.6.3.)» · punto_propio
- **N3** Operacion «Cálculo exigencia capital riesgo precio opciones» — Cálculo de la exigencia de capital por el riesgo de precio de opciones, que puede realizarse mediante el enfoque simplificado o el método delta-plus según corresponda. · props: `{"tipo": "cálculo de capital regulatorio"}` · tramo (exacta): «calcular la exigencia de capital por el riesgo de precio de opciones» · punto_propio
- **N4** Potestad «Opción enfoque simplificado o delta-plus» — Las entidades tienen la facultad de elegir entre el enfoque simplificado o el método delta-plus para calcular la exigencia de capital por riesgo de precio de opciones. · tramo (exacta): «las entidades podrán usar el enfoque simplificado (previsto en el punto 6.6.2.) o el método delta-plus (establecido en el punto 6.6.3.), según corresponda» · punto_propio
- **N5** Sujeto «Entidades alcanzadas (Capitales Mínimos)» · props: `{"nivel": "rol"}` · sin tramo · punto_propio · compartido (111 procedencias en el grafo)
- **N6** TextoOrdenado «Texto Ordenado Capitales Mínimos» · props: `{"archivo": "TO_capitales_minimos_actual.pdf", "materia": "Capitales mínimos de las entidades financieras", "version": "Comunicación A 8418 (vigencia 10/04/2026)"}` · sin tramo · punto_propio · compartido (453 procedencias en el grafo)

**Aristas de la extracción (1)**
- **A1** N4 —aplica_a→ N5 Sujeto «Entidades alcanzadas (Capitales Mínimos)» (mención «las entidades», exacta, R4_sugerencia_modelo)

**Remisiones derivadas (18 aristas)**
- **R1–R8** N3 —remite_a→ `cap::6.6.3` (interna; 7 nodo(s) destino: Definicion «Riesgo gamma»; Definicion «Riesgo vega»; Operacion «Aplicación de metodología estándar — exigencia de capital por riesgo general de mercado»; Operacion «Cálculo de equivalente delta — método delta-plus»; Operacion «Determinación de exigencia por riesgo específico»; Restriccion «Exigencia adicional por riesgo gamma»; Restriccion «Exigencia adicional por riesgo vega») · evidencia «el punto 6.6.2.) o el método delta-plus (establecido en el punto 6.6.3.), según corresponda»
- **R6–R9** N3 —remite_a→ `cap::6.6.2` (interna; 2 nodo(s) destino: Operacion «Operación con opciones y subyacentes»; Restriccion «Exigencia de capital — opciones y subyacentes») · evidencia «en- tidades podrán usar el enfoque simplificado (previsto en el punto 6.6.2.) o el método delta-»
- **R10–R17** N4 —remite_a→ `cap::6.6.3` (interna; 7 nodo(s) destino: Definicion «Riesgo gamma»; Definicion «Riesgo vega»; Operacion «Aplicación de metodología estándar — exigencia de capital por riesgo general de mercado»; Operacion «Cálculo de equivalente delta — método delta-plus»; Operacion «Determinación de exigencia por riesgo específico»; Restriccion «Exigencia adicional por riesgo gamma»; Restriccion «Exigencia adicional por riesgo vega») · evidencia «el punto 6.6.2.) o el método delta-plus (establecido en el punto 6.6.3.), según corresponda»
- **R15–R18** N4 —remite_a→ `cap::6.6.2` (interna; 2 nodo(s) destino: Operacion «Operación con opciones y subyacentes»; Restriccion «Exigencia de capital — opciones y subyacentes») · evidencia «en- tidades podrán usar el enfoque simplificado (previsto en el punto 6.6.2.) o el método delta-»

**Estructurales (4)**: establecida_en → TextoOrdenado «Texto Ordenado Capitales Mínimos» ×2; referencia → Comunicacion «Punto 6.6.2» ×1; referencia → Comunicacion «Punto 6.6.3» ×1

## 33. `cap::2.12.2.7` — estrato no_item (3 del sorteo) · cap · págs. 24 · estado `completo_ok_directo`

> *heredado (encabezado, S2):* Sección 2. Capital mínimo por riesgo de crédito.
> *heredado (chapeau_seccion, S2):* A los efectos de la aplicación de las disposiciones de la presente sección, las entidades financieras se clasificarán en: i)Grupo 1: entidades calificadas por el BCRA como de importancia sistémica a nivel local
> *heredado (chapeau_seccion, S2):* (D-SIB) y sucursales o subsidiarias de bancos del exterior calificados como de impor- tancia sistémica global (G-SIB).
> *heredado (chapeau_seccion, S2):* ii) Grupo 2: entidades financieras no comprendidas en el acápite i). En aquellos casos en que no se establezcan disposiciones específicas para cada uno de los citados grupos de entidades financieras, deberá aplicarse el mismo tratamiento a ambos grupos. Las entidades financieras que presenten cambios en su calificación –conforme a lo previsto en los acápites precedentes–, contarán con un plazo de 6 meses para aplicar las disposiciones específicas correspondientes al nuevo grupo al que pertenezcan.
> *heredado (encabezado, 2.12):* 2.12. Tabla de ponderadores de riesgo.
> *heredado (intro, 2.12):* Concepto Ponderador
> *heredado (intro, 2.12):* –en %–
> *heredado (encabezado, 2.12.2):* 2.12.2. Exposición a gobiernos y bancos centrales.
> *propio:* 2.12.2.7. Al Banco de Pagos Internacionales, al Fondo Monetario Inter- nacional, al Banco Central Europeo, al Mecanismo Europeo de Estabilidad y al Fondo Europeo de Estabilidad Financiera. 0

**Nodos (2)**
- **N1** Operacion «Ponderador de riesgo 0 % — gobiernos y bancos centrales» — Asignación de ponderador de riesgo del 0 % a exposiciones frente al Banco de Pagos Internacionales, Fondo Monetario Internacional, Banco Central Europeo, Mecanismo Europeo de Estabilidad y Fondo Europeo de Estabilidad Financiera. · props: `{"tipo": "asignación de ponderador de riesgo"}` · tramo (exacta): «Al Banco de Pagos Internacionales, al Fondo Monetario Internacional, al Banco Central Europeo, al Mecanismo Europeo de Estabilidad y al Fondo Europeo de Estabilidad Financiera. 0» · punto_propio
- **N2** TextoOrdenado «Texto Ordenado Capitales Mínimos» · props: `{"archivo": "TO_capitales_minimos_actual.pdf", "materia": "Capitales mínimos de las entidades financieras", "version": "Comunicación A 8418 (vigencia 10/04/2026)"}` · sin tramo · punto_propio · compartido (453 procedencias en el grafo)

**Aristas de la extracción (0)**

**Remisiones derivadas (0 aristas)**

**Estructurales (1)**: establecida_en → TextoOrdenado «Texto Ordenado Capitales Mínimos» ×1

## 34. `cla::1.2.1` — estrato no_item (4 del sorteo) · cla · págs. 4 · estado `completo_ok_directo`

> *heredado (encabezado, S1):* Sección 1. Deudores comprendidos.
> *heredado (encabezado, 1.2):* 1.2. Criterios especiales de imputación.
> *propio:* 1.2.1. Créditos incorporados por cesión sin responsabilidad. Los créditos cedidos a favor de la entidad sin responsabilidad para el cedente -unidad económica receptora de los fondos- se imputarán al firmante, librador, deudor, codeudor o aceptante de los respectivos instrumentos, constituidos consecuentemente en principa- les y directos pagadores, realizando respecto de ellos su evaluación como sujetos de crédito con la pertinente apertura del legajo. En caso de no efectuarse la evaluación, cualquiera sea el motivo, estos clientes se clasificarán en categoría “irrecuperable”.

**Nodos (6)**
- **N1** Condicion «Falta de evaluación de sujetos de crédito» — Cuando no se efectúa la evaluación de los sujetos de crédito, por cualquier motivo. · tramo (exacta): «En caso de no efectuarse la evaluación, cualquiera sea el motivo» · punto_propio
- **N2** Obligacion «Evaluación de sujetos de crédito — créditos cedidos» — Realizar evaluación de los sujetos de crédito (firmante, librador, deudor, codeudor o aceptante) con apertura del legajo correspondiente. · props: `{"tipo": "otra"}` · tramo (exacta): «realizando respecto de ellos su evaluación como sujetos de crédito con la pertinente apertura del legajo» · punto_propio
- **N3** Operacion «Imputación de créditos cedidos sin responsabilidad» — Créditos cedidos sin responsabilidad para el cedente se imputan al firmante, librador, deudor, codeudor o aceptante de los instrumentos, constituyéndolos en principales y directos pagadores, con evaluación como sujetos de crédito y apertura del legajo. · props: `{"tipo": "Imputación de créditos"}` · tramo (exacta): «Los créditos cedidos a favor de la entidad sin responsabilidad para el cedente -unidad económica receptora de los fondos- se imputarán al firmante, librador, deudor, codeudor o aceptante de los respectivos instrumentos» · punto_propio
- **N4** Restriccion «Clasificación irrecuperable — falta de evaluación» — Si no se efectúa la evaluación de los sujetos de crédito, cualquiera sea el motivo, se clasificarán en categoría irrecuperable. · props: `{"tipo": "limite_cualitativo"}` · tramo (exacta): «En caso de no efectuarse la evaluación, cualquiera sea el motivo, estos clientes se clasificarán en categoría "irrecuperable"» · punto_propio
- **N5** Sujeto «Obligados a clasificar deudores (Clasificación)» · props: `{"nivel": "rol"}` · sin tramo · punto_propio · compartido (41 procedencias en el grafo)
- **N6** TextoOrdenado «Texto Ordenado Clasificación de Deudores» · props: `{"archivo": "TO_clasificacion_deudores_actual.pdf", "materia": "Clasificación de deudores", "version": "Comunicación A 8378 (vigencia 20/12/2025)"}` · sin tramo · punto_propio · compartido (140 procedencias en el grafo)

**Aristas de la extracción (5)**
- **A1** N1 —condicion_de→ N4 Restriccion «Clasificación irrecuperable — falta de evaluación»
- **A2** N2 —aplica_a→ N5 Sujeto «Obligados a clasificar deudores (Clasificación)» (mención «la entidad», exacta, R4_sugerencia_modelo)
- **A3** N2 —condiciona→ N3 Operacion «Imputación de créditos cedidos sin responsabilidad»
- **A4** N3 —aplica_a→ N5 Sujeto «Obligados a clasificar deudores (Clasificación)» (mención «la entidad», exacta, R4_sugerencia_modelo)
- **A5** N4 —aplica_a→ N5 Sujeto «Obligados a clasificar deudores (Clasificación)» (mención «la entidad», exacta, R4_sugerencia_modelo)

**Remisiones derivadas (0 aristas)**

**Estructurales (4)**: establecida_en → TextoOrdenado «Texto Ordenado Clasificación de Deudores» ×4

## 35. `ext::5.8.1` — estrato no_item (5 del sorteo) · ext · págs. 71 · estado `aceptado_tras_reintento`

> *heredado (encabezado, S5):* Sección 5. Pautas operativas.
> *heredado (encabezado, 5.8):* 5.8. Boletos globales diarios.
> *heredado (intro, 5.8):* Las entidades podrán elaborar un boleto global diario para las situaciones que se detallan a continuación, en la medida que se verifiquen todas las condiciones indicadas en cada caso. En todos los casos, se deberá requerir una lista detallada de los beneficiarios/ordenantes de los pagos comprendidos en dicho boleto, debiendo como mínimo informar respecto de ellos: nombres y apellidos completos o denominación social (según corresponda), CUIT, CUIL o CDI y el monto que le corresponde.
> *propio:* 5.8.1. Operaciones por cobros y pagos de jubilaciones y pensiones. Deben corresponder a transferencias efectuadas por organismos oficiales o privados de fondos de jubilaciones y pensiones o fondos compensadores de previsión, a personas humanas residentes en el país (compras de cambio) o en el exterior (ventas de cambio) e identificar el pago a nivel de cada beneficiario del país o del exterior. El boleto deberá ser confeccionado a nombre de la entidad que cursa la operación.

**Nodos (5)**
- **N1** Condicion «Operación corresponde a transferencia de jubilaciones» — La operación debe corresponder a una transferencia de fondos de jubilaciones y pensiones o fondos compensadores de previsión efectuada por organismos oficiales o privados, dirigida a personas humanas residentes en el país o en el exterior, identificando el pago a nivel de cada beneficiario. · tramo (exacta): «Deben corresponder a transferencias efectuadas por organismos oficiales o privados de fondos de jubilaciones y pensiones o fondos compensadores de previsión, a personas humanas residentes en el país (compras de cambio) o en el exterior (ventas de cambio) e identificar el pago a nivel de cada beneficiario del país o del exterior» · punto_propio
- **N2** Obligacion «Boleto confeccionado a nombre de entidad cursante» — El boleto global diario deberá ser confeccionado a nombre de la entidad que cursa la operación. · props: `{"tipo": "otra"}` · tramo (exacta): «El boleto deberá ser confeccionado a nombre de la entidad que cursa la operación» · punto_propio
- **N3** Operacion «Transferencias jubilaciones y pensiones» — Transferencias de fondos de jubilaciones y pensiones o fondos compensadores de previsión efectuadas por organismos oficiales o privados a personas humanas residentes en el país (compras de cambio) o en el exterior (ventas de cambio), identificando el pago a nivel de cada beneficiario del país o del exterior. · props: `{"tipo": "transferencia"}` · tramo (exacta): «transferencias efectuadas por organismos oficiales o privados de fondos de jubilaciones y pensiones o fondos compensadores de previsión, a personas humanas residentes en el país (compras de cambio) o en el exterior (ventas de cambio)» · punto_propio
- **N4** Sujeto «Entidades autorizadas a operar en cambios (Exterior)» · props: `{"nivel": "rol"}` · sin tramo · punto_propio · compartido (344 procedencias en el grafo)
- **N5** TextoOrdenado «Texto Ordenado Exterior Cambios» · props: `{"archivo": "TO_exterior_cambios_actual.pdf", "materia": "Exterior y cambios", "version": "Comunicación A 8307 (vigencia 26/08/2025)"}` · sin tramo · punto_propio · compartido (930 procedencias en el grafo)

**Aristas de la extracción (2)**
- **A1** N1 —condicion_de→ N3 Operacion «Transferencias jubilaciones y pensiones»
- **A2** N2 —aplica_a→ N4 Sujeto «Entidades autorizadas a operar en cambios (Exterior)» (mención «la entidad que cursa la operación», exacta, R4_sugerencia_modelo)

**Remisiones derivadas (0 aristas)**

**Estructurales (3)**: establecida_en → TextoOrdenado «Texto Ordenado Exterior Cambios» ×3

## 36. `ric::11.1.4` — estrato no_item (6 del sorteo) · ric · págs. 50, 51 · estado `completo_ok_directo`

Flags de E0: `{"formula": true, "evidencia_formula": ["Se informarán los siguientes cálculos, teniendo en cuenta el escenario (X= 1 a 6) o la", "moneda (M = 001 –pesos– o 010 –dólares estadounidenses–) en los casos en que", "11.2.1.a) y b), según se trate posiciones en pesos (M=001) o en dólares estadouni-"]}`

> *heredado (encabezado, S11):* Sección 11. Información complementaria vinculada al cálculo del riesgo de tasa de interés en cartera de inversión.
> *heredado (encabezado, 11.1):* 11.1. Normas de procedimiento.
> *heredado (intro, 11.1):* Conceptos comprendidos. Se incluirán los flujos de fondos nocionales futuros sujetos a reapreciación de activos, pasi- vos y partidas fuera de balance sensibles a variaciones en la tasa de interés. Conceptos excluidos. - Activos que se deducen del capital ordinario del nivel 1 (COn1); - Activos fijos; - Posiciones en acciones en la cartera de inversión. Frecuencia y consolidación. Los datos se informarán con frecuencia trimestral y se integrarán con los datos correspon- dientes al último mes de cada trimestre (marzo, junio, septiembre y diciembre), sobre base individual y consolidada mensual. Serán aplicables los siguientes códigos de consolidación definidos en la Sección 2.: Base individual (código de consolidación 0 o 1); Base consolidada (código de consolidación 2). Se regirá por los plazos de presentación previstos para el régimen informativo contable men- sual correspondiente al mes siguiente al del cierre de cada trimestre.
> *propio:* 11.1.4. Cálculo de la medida de riesgo EVE estandarizada. Se informarán los siguientes cálculos, teniendo en cuenta el escenario (X= 1 a 6) o la moneda (M = 001 –pesos– o 010 –dólares estadounidenses–) en los casos en que estén previstos tales atributos. • Medida total del riesgo por opciones automáticas (KAO) –partidas 3613000X/M–. Las entidades del Grupo “A” calcularán el componente adicional por las opcio- nes automáticas sobre tasas de interés vendidas, ya sean explícitas o implícitas (punto 5.4.3. de las normas sobre “Lineamientos para la gestión de riesgos en las entidades financieras”), por cada moneda y por escenario. • Valor económico del patrimonio –partidas 3612000X/M–. Mide el valor económico del patrimonio correspondiente a todas las bandas tempo- rales, para los 6 escenarios en cada moneda significativa (punto 5.4.4.3. de las normas sobre “Lineamientos para la gestión de riesgos en las entidades financie- ras”). No incluye las opciones automáticas sobre tasas de interés. • Valor económico del patrimonio para el escenario base –partidas 36110000/M–. Calculado con la estructura de tasas de interés vigentes en el escenario 0 o base (punto 5.4.4.4. de las normas sobre “Lineamientos para la gestión de riesgos en las entidades financieras”). • Variación del valor económico del patrimonio –partida 3610000X/M–. Surge de restar, para cada moneda, al EVE0 (resultante del escenario 0) el EVE del escenario de perturbación, según corresponda. A este valor se le sumará el riesgo de opción automática sobre tasas de interés - KAO - (punto 5.4.4.4. de las normas sobre “Lineamientos para la gestión de riesgos en las entidades financieras”). • Suma de pérdidas por escenario –partida 3650000X–. Se suman únicamente las pérdidas registradas en las monedas de los diferentes escenarios, es decir, se obtiene una pérdida agregada por escenario, sin compen- sar con los resultados positivos. No admite signo negativo (punto 5.4.4.4. de las normas sobre “Lineamientos para la gestión de riesgos en las entidades financie- ras”). Estos cálculos deberán ser consistentes con la información reportada en los cuadros 11.2.1.a) y b), según se trate posiciones en pesos (M=001) o en dólares estadouni- denses (M=010), respectivamente.

**Nodos (10)**
- **N1** Obligacion «Cálculo componente adicional opciones automáticas — Grupo A» — Las entidades del Grupo A deberán calcular el componente adicional por las opciones automáticas sobre tasas de interés vendidas, ya sean explícitas o implícitas, por cada moneda y por escenario. · props: `{"tipo": "calculo"}` · tramo (exacta): «Las entidades del Grupo "A" calcularán el componente adicional por las opciones automáticas sobre tasas de interés vendidas, ya sean explícitas o implícitas (punto 5.4.3. de las normas sobre "Lineamientos para la gestión de riesgos en las entidades financieras"), por cada moneda y por escenario.» · punto_propio
- **N2** Obligacion «Consistencia cálculos con cuadros 11.2.1.a) y b)» — Los cálculos deberán ser consistentes con la información reportada en los cuadros 11.2.1.a) y b), según se trate posiciones en pesos (M=001) o en dólares estadounidenses (M=010). · props: `{"tipo": "otra"}` · tramo (exacta): «Estos cálculos deberán ser consistentes con la información reportada en los cuadros 11.2.1.a) y b), según se trate posiciones en pesos (M=001) o en dólares estadounidenses (M=010), respectivamente.» · punto_propio
- **N3** Operacion «Cálculo medida riesgo EVE estandarizada» — Cálculo de la medida de riesgo EVE estandarizada, teniendo en cuenta el escenario (X= 1 a 6) o la moneda (M = 001 –pesos– o 010 –dólares estadounidenses–) en los casos en que estén previstos tales atributos. · props: `{"tipo": "cálculo"}` · tramo (exacta): «Cálculo de la medida de riesgo EVE estandarizada» · punto_propio
- **N4** Operacion «Cálculo medida total riesgo opciones automáticas KAO» — Medida total del riesgo por opciones automáticas (KAO) en partidas 3613000X/M. · props: `{"tipo": "cálculo"}` · tramo (exacta): «Medida total del riesgo por opciones automáticas (KAO) –partidas 3613000X/M–» · punto_propio
- **N5** Operacion «Cálculo suma pérdidas por escenario» — Suma de pérdidas por escenario donde se suman únicamente las pérdidas registradas en las monedas de los diferentes escenarios, obteniéndose una pérdida agregada por escenario, sin compensar con los resultados positivos. No admite signo negativo. · props: `{"tipo": "cálculo"}` · tramo (exacta): «Suma de pérdidas por escenario –partida 3650000X–» · punto_propio
- **N6** Operacion «Cálculo valor económico patrimonio» — Valor económico del patrimonio correspondiente a todas las bandas temporales, para los 6 escenarios en cada moneda significativa. No incluye las opciones automáticas sobre tasas de interés. · props: `{"tipo": "cálculo"}` · tramo (exacta): «Valor económico del patrimonio –partidas 3612000X/M–» · punto_propio
- **N7** Operacion «Cálculo valor económico patrimonio escenario base» — Valor económico del patrimonio para el escenario base, calculado con la estructura de tasas de interés vigentes en el escenario 0 o base. · props: `{"tipo": "cálculo"}` · tramo (exacta): «Valor económico del patrimonio para el escenario base –partidas 36110000/M–» · punto_propio
- **N8** Operacion «Cálculo variación valor económico patrimonio» — Variación del valor económico del patrimonio que surge de restar, para cada moneda, al EVE0 (resultante del escenario 0) el EVE del escenario de perturbación, según corresponda. Se le sumará el riesgo de opción automática sobre tasas de interés - KAO. · props: `{"tipo": "cálculo"}` · tramo (exacta): «Variación del valor económico del patrimonio –partida 3610000X/M–» · punto_propio
- **N9** Sujeto «Entidades comprendidas (Régimen Informativo)» · props: `{"nivel": "rol"}` · sin tramo · punto_propio · compartido (37 procedencias en el grafo)
- **N10** TextoOrdenado «Régimen Informativo Contable Mensual» · props: `{"archivo": "TO_regimen_informativo_contable_mensual_actual.pdf", "materia": "RI Cont. Mensual - Exigencia e integración de capitales mínimos", "version": "Comunicación A 8396 (vigencia 30/01/2026)"}` · sin tramo · punto_propio · compartido (88 procedencias en el grafo)

**Aristas de la extracción (1)**
- **A1** N1 —aplica_a→ N9 Sujeto «Entidades comprendidas (Régimen Informativo)» (mención «Las entidades del Grupo "A"», exacta, R4_sugerencia_modelo)

**Remisiones derivadas (0 aristas)**

**Estructurales (8)**: establecida_en → TextoOrdenado «Régimen Informativo Contable Mensual» ×8

## 37. `ext::7.3.11` — estrato no_item (7 del sorteo) · ext · págs. 85 · estado `aceptado_tras_reintento`

> *heredado (encabezado, S7):* Sección 7. Cobros de exportaciones de bienes.
> *heredado (encabezado, 7.3):* 7.3. Aplicación de divisas de cobros de exportaciones.
> *heredado (intro, 7.3):* Existe una aplicación de divisas de cobros de exportaciones de bienes cuando se ha certificado que los propios bienes exportados o las divisas cobradas por ellos fueron utilizados para cancelar el capital, intereses y/o gastos de otorgamiento de operaciones de financiamiento, pagar utilidades y dividendos y/o concretar la repatriación de una inversión directa de un accionista no residente en los casos admitidos en los puntos 7.3.1. a 7.3.11. A los efectos que los cobros de exportaciones aplicados puedan ser imputados al cumplimiento de los permisos de embarque oficializados a partir del 02/09/19, será necesario contar en todos los casos con una certificación de aplicación emitida por la entidad encargada del “Seguimiento de anticipos y otras financiaciones de exportación de bienes”. Los exportadores que efectúen liquidaciones de moneda extranjera asociadas a las operaciones comprendidas en los puntos 7.3.1. al 7.3.10. deberán solicitar a la entidad interviniente que le asigne un número de identificación (número APX) y la incorpore al mencionado seguimiento. En el caso de operaciones comprendidas en el punto 7.3.8. que no registren liquidaciones en el mercado de cambios por ser refinanciaciones de deudas preexistentes, la entidad nominada por el exportador atento a lo establecido en el punto 7.9.3. deberá incorporarla al mencionado seguimiento, usando para su identificación el número correlativo que se le asignó a la operación del cliente (número ECO: Entidad-CUIT-N° Operación).
> *propio:* 7.3.11. Anticipos, prefinanciaciones y posfinanciaciones del exterior con liquidación parcial en virtud de lo dispuesto por los Decretos 492/23, 549/23, 597/23 y 28/23. Se admitirá la aplicación de divisas a la cancelación del capital e intereses correspondiente a la porción no liquidada de anticipos, prefinanciaciones y posfinanciaciones del exterior a partir de lo dispuesto en los Decretos 492/23, 549/23, 597/23 y 28/23, en la medida que el cliente demuestre que, durante sus respectivas vigencias y en las condiciones estipuladas en los mencionados decretos, ingresó y liquidó divisas en el mercado de cambios por un monto no menor al porcentaje mínimo requerido de la operación y por la porción no liquidada del cobro concretó operaciones de compraventa con títulos valores, en las cuales los títulos valores son adquiridos con liquidación en moneda extranjera y vendidos con liquidación en moneda local en el país. La aplicación de la porción no liquidada deberá ser certificada por la entidad encargada del "Seguimiento de anticipos y otras financiaciones de exportación de bienes" de la porción liquidada de la operación, debiéndose verificarse los restantes requisitos habituales. En caso de que la operación haya sido liquidada por más de una entidad, cada una podrá certificar la aplicación de la porción no liquidada en proporción a su participación en la porción liquidada. En el caso de que la adquisición de títulos valores se haya concretado con liquidación en el país de la moneda extranjera se deberá contar con la certificación de la entidad que cursó la operación de canje y/o arbitraje por el ingreso de las divisas a través del mercado de cambios.

**Nodos (11)**
- **N1** Condicion «Ingreso y liquidación mínima de divisas — mercado de cambios» — El cliente debe demostrar que durante las vigencias de los decretos y en sus condiciones estipuladas ingresó y liquidó divisas en el mercado de cambios por un monto no menor al porcentaje mínimo requerido de la operación. · props: `{"umbrales": [{"tramo": "por un monto no menor al porcentaje mínimo requerido de la operación", "comparacion": "minimo_inclusivo", "base": "porcentaje mínimo requerido de la operación", "regla_comparacion": "limite_relativo:negacion:menor", "origen": "e1", "tramo_verificado": "exacta"}]}` · tramo (exacta): «en la medida que el cliente demuestre que, durante sus respectivas vigencias y en las condiciones estipuladas en los mencionados decretos, ingresó y liquidó divisas en el mercado de cambios por un monto no menor al porcentaje mínimo requerido de la operación» · punto_propio
- **N2** Condicion «Operaciones compraventa títulos valores — liquidación extranjera/local» — Por la porción no liquidada del cobro, el cliente debe concretar operaciones de compraventa con títulos valores donde los títulos son adquiridos con liquidación en moneda extranjera y vendidos con liquidación en moneda local en el país. · tramo (exacta): «por la porción no liquidada del cobro concretó operaciones de compraventa con títulos valores, en las cuales los títulos valores son adquiridos con liquidación en moneda extranjera y vendidos con liquidación en moneda local en el país» · punto_propio
- **N3** Obligacion «Certificación canje/arbitraje — liquidación en país» — Cuando la adquisición de títulos valores se ha concretado con liquidación en el país de la moneda extranjera, se debe contar con la certificación de la entidad que cursó la operación de canje y/o arbitraje por el ingreso de las divisas a través del mercado de cambios. · props: `{"tipo": "presentacion_informativa"}` · tramo (exacta): «En el caso de que la adquisición de títulos valores se haya concretado con liquidación en el país de la moneda extranjera se deberá contar con la certificación de la entidad que cursó la operación de canje y/o arbitraje por el ingreso de las divisas a través del mercado de cambios» · punto_propio
- **N4** Obligacion «Certificación proporcional — múltiples entidades liquidadoras» — Cuando la operación ha sido liquidada por más de una entidad, cada una puede certificar la aplicación de la porción no liquidada en proporción a su participación en la porción liquidada. · props: `{"tipo": "presentacion_informativa"}` · tramo (exacta): «En caso de que la operación haya sido liquidada por más de una entidad, cada una podrá certificar la aplicación de la porción no liquidada en proporción a su participación en la porción liquidada» · punto_propio
- **N5** Obligacion «Certificación aplicación porción no liquidada» — La entidad encargada del Seguimiento de anticipos y otras financiaciones de exportación de bienes debe certificar la aplicación de la porción no liquidada de la operación, verificándose los restantes requisitos habituales. · props: `{"tipo": "presentacion_informativa"}` · tramo (exacta): «La aplicación de la porción no liquidada deberá ser certificada por la entidad encargada del "Seguimiento de anticipos y otras financiaciones de exportación de bienes" de la porción liquidada de la operación» · punto_propio
- **N6** Operacion «Aplicación divisas — anticipos, prefinanciaciones, posfinanciaciones» — Cancelación del capital e intereses de la porción no liquidada de anticipos, prefinanciaciones y posfinanciaciones del exterior conforme a los Decretos 492/23, 549/23, 597/23 y 28/23. · props: `{"tipo": "Aplicación de divisas"}` · tramo (exacta): «aplicación de divisas a la cancelación del capital e intereses correspondiente a la porción no liquidada de anticipos, prefinanciaciones y posfinanciaciones del exterior» · punto_propio
- **N7** Potestad «Admisión de aplicación divisas — porción no liquidada» — Se admite la aplicación de divisas a la cancelación del capital e intereses de la porción no liquidada de anticipos, prefinanciaciones y posfinanciaciones del exterior conforme a los Decretos 492/23, 549/23, 597/23 y 28/23, sujeto al cumplimiento de las condiciones establecidas. · tramo (exacta): «Se admitirá la aplicación de divisas a la cancelación del capital e intereses correspondiente a la porción no liquidada de anticipos, prefinanciaciones y posfinanciaciones del exterior a partir de lo dispuesto en los Decretos 492/23, 549/23, 597/23 y 28/23» · punto_propio
- **N8** Sujeto «la entidad encargada del "Seguimiento de anticipos y otras financiaciones de exportación de bienes"» · props: `{"nivel": "propuesto", "cuarentena": "true", "padre_sugerido": "Sujeto_rol_entidad_autorizada_exterior", "padre_por_defecto": "true"}` · sin tramo · punto_propio
- **N9** Sujeto «la entidad que cursó la operación de canje y/o arbitraje» · props: `{"nivel": "propuesto", "cuarentena": "true", "padre_sugerido": "Sujeto_rol_entidad_autorizada_exterior", "padre_por_defecto": "true"}` · sin tramo · punto_propio
- **N10** Sujeto «Entidades autorizadas a operar en cambios (Exterior)» · props: `{"nivel": "rol"}` · sin tramo · punto_propio · compartido (344 procedencias en el grafo)
- **N11** TextoOrdenado «Texto Ordenado Exterior Cambios» · props: `{"archivo": "TO_exterior_cambios_actual.pdf", "materia": "Exterior y cambios", "version": "Comunicación A 8307 (vigencia 26/08/2025)"}` · sin tramo · punto_propio · compartido (930 procedencias en el grafo)

**Aristas de la extracción (5)**
- **A1** N1 —condicion_de→ N7 Potestad «Admisión de aplicación divisas — porción no liquidada»
- **A2** N2 —condicion_de→ N7 Potestad «Admisión de aplicación divisas — porción no liquidada»
- **A3** N3 —aplica_a→ N9 Sujeto «la entidad que cursó la operación de canje y/o arbitraje» (mención «la entidad que cursó la operación de canje y/o arbitraje», exacta, cuarentena)
- **A4** N5 —aplica_a→ N8 Sujeto «la entidad encargada del "Seguimiento de anticipos y otras financiaciones de exportación de bienes"» (mención «la entidad encargada del "Seguimiento de anticipos y otras financiaciones de exportación de bienes"», exacta, cuarentena)
- **A5** N7 —aplica_a→ N10 Sujeto «Entidades autorizadas a operar en cambios (Exterior)» (mención «las entidades», no, R4_sugerencia_modelo)

**Remisiones derivadas (0 aristas)**

**Catálogo de sujetos (2)**
- **C1** Sujeto «la entidad encargada del "Seguimiento de anticipos y otras financiaciones de exportación de bienes"» —padre_sugerido→ Sujeto «Entidades autorizadas a operar en cambios (Exterior)»
- **C2** Sujeto «la entidad que cursó la operación de canje y/o arbitraje» —padre_sugerido→ Sujeto «Entidades autorizadas a operar en cambios (Exterior)»

**Estructurales (7)**: establecida_en → TextoOrdenado «Texto Ordenado Exterior Cambios» ×7

## 38. `ric::8.1.7` — estrato no_item (8 del sorteo) · ric · págs. 38 · estado `completo_ok_directo`

> *heredado (encabezado, S8):* Sección 8. Totales de control.
> *heredado (encabezado, 8.1):* 8.1. Normas de procedimiento.
> *propio:* 8.1.7. Código 70300000. Exigencia por riesgo operacional según el punto 5.1.

**Nodos (3)**
- **N1** Obligacion «Presentar exigencia riesgo operacional código 70300000» — Presentación de la exigencia por riesgo operacional según lo establecido en el punto 5.1, bajo el código 70300000 · props: `{"tipo": "presentacion_informativa"}` · tramo (exacta): «Exigencia por riesgo operacional según el punto 5.1» · punto_propio
- **N2** Operacion «Cálculo exigencia riesgo operacional» — Cálculo de la exigencia de capital por riesgo operacional conforme al punto 5.1 · props: `{"tipo": "cálculo de exigencia de capital"}` · tramo (exacta): «Exigencia por riesgo operacional» · punto_propio
- **N3** TextoOrdenado «Régimen Informativo Contable Mensual» · props: `{"archivo": "TO_regimen_informativo_contable_mensual_actual.pdf", "materia": "RI Cont. Mensual - Exigencia e integración de capitales mínimos", "version": "Comunicación A 8396 (vigencia 30/01/2026)"}` · sin tramo · punto_propio · compartido (88 procedencias en el grafo)

**Aristas de la extracción (1)**
- **A1** N1 —regula→ N2 Operacion «Cálculo exigencia riesgo operacional»

**Remisiones derivadas (0 aristas)**

**Estructurales (2)**: establecida_en → TextoOrdenado «Régimen Informativo Contable Mensual» ×2

## 39. `cla::9.1` — estrato no_item (9 del sorteo) · cla · págs. 42 · estado `completo_ok_directo`

> *heredado (encabezado, S9):* Sección 9. Bases de observancia de las normas.
> *propio:* 9.1. Base individual. Las entidades financieras (comprendidas sus filiales en el país y en el exterior) observarán las normas en materia de clasificación de deudores en forma individual.

**Nodos (3)**
- **N1** Obligacion «Observancia individual normas clasificación» — Las entidades financieras, comprendidas sus filiales en el país y en el exterior, deberán observar las normas en materia de clasificación de deudores en forma individual. · props: `{"tipo": "otra"}` · tramo (exacta): «Las entidades financieras (comprendidas sus filiales en el país y en el exterior) observarán las normas en materia de clasificación de deudores en forma individual.» · punto_propio
- **N2** Sujeto «Entidades financieras» · props: `{"nivel": "clase", "alias": ["Entidades financieras emisoras de tarjetas de crédito y/o compra", "Entidad financiera emisora de tarjetas de crédito y/o compra"]}` · sin tramo · punto_propio · compartido (328 procedencias en el grafo)
- **N3** TextoOrdenado «Texto Ordenado Clasificación de Deudores» · props: `{"archivo": "TO_clasificacion_deudores_actual.pdf", "materia": "Clasificación de deudores", "version": "Comunicación A 8378 (vigencia 20/12/2025)"}` · sin tramo · punto_propio · compartido (140 procedencias en el grafo)

**Aristas de la extracción (1)**
- **A1** N1 —aplica_a→ N2 Sujeto «Entidades financieras» (mención «Las entidades financieras», exacta, R1_label_exacto)

**Remisiones derivadas (0 aristas)**

**Estructurales (1)**: establecida_en → TextoOrdenado «Texto Ordenado Clasificación de Deudores» ×1

## 40. `ext::10.2.4::cierre` — estrato no_item (10 del sorteo) · ext · págs. 132 · estado `aceptado_tras_reintento`

> *heredado (encabezado, S10):* Sección 10. Pagos de importaciones y otras compras de bienes en el exterior.
> *heredado (encabezado, 10.2):* 10.2. Definiciones.
> *heredado (encabezado, 10.2.4):* 10.2.4. Deuda comercial por importación de bienes.
> *propio:* Los pagos por deudas originadas en importaciones de bienes que no encuadren como deudas comerciales de importación se regirán por las normas que sean aplicables para la cancelación de servicios de capital de préstamos financieros.

**Nodos (2)**
- **N1** Definicion «Deuda comercial por importación de bienes» — Pagos por deudas originadas en importaciones de bienes que no encuadren como deudas comerciales de importación; se rigen por las normas aplicables para la cancelación de servicios de capital de préstamos financieros · props: `{"termino": "deudas originadas en importaciones de bienes que no encuadren como deudas comerciales de importación"}` · tramo (exacta): «Los pagos por deudas originadas en importaciones de bienes que no encuadren como deudas comerciales de importación se regirán por las normas que sean aplicables para la cancelación de servicios de capital de préstamos financieros» · bloque_cierre
- **N2** TextoOrdenado «Texto Ordenado Exterior Cambios» · props: `{"archivo": "TO_exterior_cambios_actual.pdf", "materia": "Exterior y cambios", "version": "Comunicación A 8307 (vigencia 26/08/2025)"}` · sin tramo · bloque_cierre · compartido (930 procedencias en el grafo)

**Aristas de la extracción (0)**

**Remisiones derivadas (0 aristas)**

**Estructurales (1)**: establecida_en → TextoOrdenado «Texto Ordenado Exterior Cambios» ×1

## 41. `cap::3.1.1.6` — estrato no_item (11 del sorteo) · cap · págs. 30 · estado `completo_ok_directo`

> *heredado (encabezado, S3):* Sección 3. Capital mínimo por riesgo de crédito. Titulizaciones e inversiones en fon- dos.
> *heredado (encabezado, 3.1):* 3.1. Tratamiento de las titulizaciones.
> *heredado (intro, 3.1):* Se denomina “posición de titulización” a la exposición a una titulización (o retitulización), tradi- cional o sintética, o a una estructura con similares características. La exposición a los riesgos de una titulización puede surgir, entre otros, de los siguientes con- ceptos: tenencia de títulos valores emitidos en el marco de la titulización –es decir, títulos de deuda y/o certificados de participación, tales como bonos de titulización de activos (“Asset- Backed Securities”, ABS) y bonos de titulización hipotecaria (“Mortgage-Backed Securities”, MBS)–, mejoras crediticias, facilidades de liquidez, “swaps” de tasa de interés o de monedas y derivados de crédito. Las reservas (“reserve accounts”), tales como las cuentas de garantía en efectivo, se considerarán como un activo para la entidad financiera originante, recibiendo tam- bién el tratamiento de posiciones de titulización. Dado que las titulizaciones pueden estructurarse de diferentes formas, la exigencia de capital para una posición de titulización se determinará teniendo en cuenta su realidad o finalidad eco- nómica y no su forma jurídica. En los casos en que exista incertidumbre acerca de si una de- terminada operación debe considerarse como titulización, la entidad deberá aplicar el criterio que estime mejor se ajusta a la realidad económica de la operación e informar a la SEFyC los fundamentos que lo sustenten.
> *heredado (encabezado, 3.1.1):* 3.1.1. Conceptos.
> *propio:* 3.1.1.6. Cláusula de amortización anticipada: es un mecanismo que, una vez activado, acelera la reducción de la participación de los inversores en las exposiciones subyacentes de una titulización de facilidades de crédito rotativas y permite a los inversores obtener reembolsos antes del vencimiento inicialmente fijado de los títulos valores emitidos. Una titulización de facilidades de crédito rotativas es aquella en la cual una o más exposiciones subyacentes consisten, directa o indirectamente, en los giros –ya realizados o futuros– contra dichas facilidades rotativas, tales como tarjetas de crédito, líneas de crédito comerciales u otras líneas de crédito.

**Nodos (3)**
- **N1** Definicion «Cláusula de amortización anticipada» — Mecanismo que, una vez activado, acelera la reducción de la participación de los inversores en las exposiciones subyacentes de una titulización de facilidades de crédito rotativas y permite a los inversores obtener reembolsos antes del vencimiento inicialmente fijado de los títulos valores emitidos. · props: `{"termino": "Cláusula de amortización anticipada"}` · tramo (exacta): «Cláusula de amortización anticipada: es un mecanismo que, una vez activado, acelera la reducción de la participación de los inversores en las exposiciones subyacentes de una titulización de facilidades de crédito rotativas y permite a los inversores obtener reembolsos antes del vencimiento inicialmente fijado de los títulos valores emitidos.» · punto_propio
- **N2** Definicion «Titulización de facilidades de crédito rotativas» — Aquella en la cual una o más exposiciones subyacentes consisten, directa o indirectamente, en los giros –ya realizados o futuros– contra dichas facilidades rotativas, tales como tarjetas de crédito, líneas de crédito comerciales u otras líneas de crédito. · props: `{"termino": "titulización de facilidades de crédito rotativas"}` · tramo (exacta): «Una titulización de facilidades de crédito rotativas es aquella en la cual una o más exposiciones subyacentes consisten, directa o indirectamente, en los giros –ya realizados o futuros– contra dichas facilidades rotativas, tales como tarjetas de crédito, líneas de crédito comerciales u otras líneas de crédito.» · punto_propio
- **N3** TextoOrdenado «Texto Ordenado Capitales Mínimos» · props: `{"archivo": "TO_capitales_minimos_actual.pdf", "materia": "Capitales mínimos de las entidades financieras", "version": "Comunicación A 8418 (vigencia 10/04/2026)"}` · sin tramo · punto_propio · compartido (453 procedencias en el grafo)

**Aristas de la extracción (0)**

**Remisiones derivadas (0 aristas)**

**Estructurales (2)**: establecida_en → TextoOrdenado «Texto Ordenado Capitales Mínimos» ×2

## 42. `ctacte::1.5.2.9` — estrato no_item (12 del sorteo) · ctacte · págs. 12, 13 · estado `aceptado_tras_reintento`

> *heredado (encabezado, S1):* Sección 1. Funcionamiento.
> *heredado (encabezado, 1.5):* 1.5. Aspectos del funcionamiento a incluir en el contrato de cuenta corriente.
> *heredado (intro, 1.5):* En sus cláusulas se deberá prever, como mínimo:
> *heredado (encabezado, 1.5.2):* 1.5.2. Obligaciones de la entidad.
> *propio:* 1.5.2.9. Constatar –tanto en los cheques librados en formato papel como en los certifica- dos nominativos transferibles– la regularidad de la serie de endosos pero no la autenticidad de la firma de los endosantes y verificar la firma del presentante, que deberá insertarse con carácter de recibo. Estas obligaciones recaen sobre la entidad girada cuando el cheque se presen- te para el cobro en ella, en tanto que a la entidad en que se deposita el cheque –cuando sea distinta de la girada– le corresponde controlar que la última firma extendida en carácter de recibo contenga las especificaciones fijadas en el pun- to 5.1.3., salvo que resulte aplicable el procedimiento de truncamiento, en cuyo caso se estará a lo previsto en los respectivos convenios. Cuando la presentación se efectúe a través de mandatario o beneficiario de una cesión ordinaria, deberá verificarse además el instrumento por el cual se haya otorgado el mandato o efectuado la cesión, excepto cuando la gestión de cobro sea realizada por una entidad financiera no autorizada a captar depósitos en cuenta corriente.

**Nodos (13)**
- **N1** Condicion «Condición — presentación a través de mandatario o cesionario» — La obligación de verificar el instrumento de mandato o cesión se activa cuando la presentación se efectúe a través de mandatario o beneficiario de una cesión ordinaria · tramo (exacta): «Cuando la presentación se efectúe a través de mandatario o beneficiario de una cesión ordinaria» · punto_propio
- **N2** Excepcion «Excepción — procedimiento de truncamiento» — No aplica la obligación de controlar la última firma de recibo cuando resulte aplicable el procedimiento de truncamiento; en ese caso se estará a lo previsto en los respectivos convenios · tramo (exacta): «salvo que resulte aplicable el procedimiento de truncamiento, en cuyo caso se estará a lo previsto en los respectivos convenios» · punto_propio
- **N3** Excepcion «Excepción — entidad financiera no autorizada a captar depósitos» — No se requiere verificar el instrumento de mandato o cesión cuando la gestión de cobro sea realizada por una entidad financiera no autorizada a captar depósitos en cuenta corriente · tramo (exacta): «excepto cuando la gestión de cobro sea realizada por una entidad financiera no autorizada a captar depósitos en cuenta corriente» · punto_propio
- **N4** Obligacion «Verificar instrumento de mandato o cesión» — Cuando la presentación se efectúe a través de mandatario o beneficiario de una cesión ordinaria, debe verificarse el instrumento por el cual se haya otorgado el mandato o efectuado la cesión · props: `{"tipo": "otra"}` · tramo (exacta): «Cuando la presentación se efectúe a través de mandatario o beneficiario de una cesión ordinaria, deberá verificarse además el instrumento por el cual se haya otorgado el mandato o efectuado la cesión» · punto_propio
- **N5** Obligacion «Controlar última firma de recibo — entidad depositaria» — La entidad en que se deposita el cheque, cuando sea distinta de la girada, debe controlar que la última firma extendida en carácter de recibo contenga las especificaciones fijadas en el punto 5.1.3. · props: `{"tipo": "otra"}` · tramo (exacta): «a la entidad en que se deposita el cheque –cuando sea distinta de la girada– le corresponde controlar que la última firma extendida en carácter de recibo contenga las especificaciones fijadas en el punto 5.1.3.» · punto_propio
- **N6** Obligacion «Obligación de constatar y verificar — entidad girada» — La entidad girada debe constatar la regularidad de la serie de endosos y verificar la firma del presentante cuando el cheque se presente para el cobro en ella · props: `{"tipo": "otra"}` · tramo (exacta): «Estas obligaciones recaen sobre la entidad girada cuando el cheque se presente para el cobro en ella» · punto_propio
- **N7** Operacion «Constatar regularidad de serie de endosos» — Constatar la regularidad de la serie de endosos en cheques librados en formato papel y en certificados nominativos transferibles · props: `{"tipo": "verificación de instrumento"}` · tramo (exacta): «Constatar –tanto en los cheques librados en formato papel como en los certificados nominativos transferibles– la regularidad de la serie de endosos» · punto_propio
- **N8** Operacion «Verificar firma del presentante como recibo» — Verificar la firma del presentante, que deberá insertarse con carácter de recibo · props: `{"tipo": "verificación de instrumento"}` · tramo (exacta): «verificar la firma del presentante, que deberá insertarse con carácter de recibo» · punto_propio
- **N9** Restriccion «No verificar autenticidad de firma de endosantes» — No verificar la autenticidad de la firma de los endosantes · props: `{"tipo": "prohibicion"}` · tramo (exacta): «pero no la autenticidad de la firma de los endosantes» · punto_propio
- **N10** Sujeto «Entidades depositarias» · props: `{"nivel": "clase", "alias": ["entidad depositaria"]}` · sin tramo · punto_propio · compartido (6 procedencias en el grafo)
- **N11** Sujeto «Entidades giradas» · props: `{"nivel": "clase", "alias": ["entidad girada", "banco girado"]}` · sin tramo · punto_propio · compartido (22 procedencias en el grafo)
- **N12** Sujeto «la entidad» · props: `{"nivel": "propuesto", "cuarentena": "true", "padre_sugerido": "Sujeto_banco", "colision_cross_to": "true"}` · sin tramo · punto_propio
- **N13** TextoOrdenado «Cuentas corrientes» · props: `{"archivo": "ctacte.pdf", "materia": "Reglamentación de la cuenta corriente bancaria", "version": "Comunicación A 8444 (vigencia 05/06/2026)"}` · sin tramo · punto_propio · compartido (380 procedencias en el grafo)

**Aristas de la extracción (5)**
- **A1** N1 —condicion_de→ N4 Obligacion «Verificar instrumento de mandato o cesión»
- **A2** N3 —exceptua_obligacion→ N4 Obligacion «Verificar instrumento de mandato o cesión»
- **A3** N4 —aplica_a→ N12 Sujeto «la entidad» (mención «la entidad», exacta, cuarentena)
- **A4** N5 —aplica_a→ N10 Sujeto «Entidades depositarias» (mención «la entidad en que se deposita el cheque», exacta, R4_sugerencia_modelo)
- **A5** N6 —aplica_a→ N11 Sujeto «Entidades giradas» (mención «la entidad girada», exacta, R1_alias_exacto)

**Remisiones derivadas (3 aristas)**
- **R1–R3** N5 —remite_a→ `ctacte::5.1.3` (interna; 3 nodo(s) destino: Definicion «Firma para cobro o depósito — no constituye endoso»; Operacion «Gestión de cobro de documentos»; Restriccion «Exclusión de endosos de gestión de cobro del límite») · evidencia «carácter de recibo contenga las especificaciones fijadas en el pun- to 5.1.3., salvo que resulte»

**Catálogo de sujetos (1)**
- **C1** Sujeto «la entidad» —padre_sugerido→ Sujeto «Bancos»

**Estructurales (9)**: establecida_en → TextoOrdenado «Cuentas corrientes» ×9

## 43. `ctacte::9.1.3` — estrato no_item (13 del sorteo) · ctacte · págs. 49 · estado `completo_ok_directo`

> *heredado (encabezado, S9):* Sección 9. Cierre de cuentas y suspensión del servicio de pago de cheques como medida previa al cierre de la cuenta.
> *heredado (encabezado, 9.1):* 9.1. Causales.
> *propio:* 9.1.3. Falta de pago de las multas establecidas por la Ley 25.730. La entidad financiera que haya rechazado cheques sin haber percibido en tiempo y for- ma las respectivas multas llevará a cabo el cierre de cuentas, dentro de los 30 días co- rridos, contados desde la fecha en que la información se encuentre disponible para los usuarios del sistema en la "Central de cuentacorrentistas inhabilitados”.

**Nodos (5)**
- **N1** Condicion «Información disponible en Central de inhabilitados» — La condición se cumple cuando la información sobre el rechazo de cheques sin percepción de multas está disponible en la Central de cuentacorrentistas inhabilitados · tramo (exacta): «desde la fecha en que la información se encuentre disponible para los usuarios del sistema en la "Central de cuentacorrentistas inhabilitados"» · punto_propio
- **N2** Obligacion «Cierre de cuentas dentro de 30 días» — La entidad financiera debe llevar a cabo el cierre de cuentas dentro de los 30 días corridos, contados desde la fecha en que la información se encuentre disponible en la Central de cuentacorrentistas inhabilitados · props: `{"tipo": "asignacion", "umbrales": [{"tramo": "30 días corridos", "valor": "30", "unidad": "dias", "dias_tipo": "corridos", "comparacion": "maximo_inclusivo", "regla_comparacion": "compuesta:dentro_de", "origen": "e1", "tramo_verificado": "exacta"}]}` · tramo (exacta): «llevará a cabo el cierre de cuentas, dentro de los 30 días corridos, contados desde la fecha en que la información se encuentre disponible para los usuarios del sistema en la "Central de cuentacorrentistas inhabilitados"» · punto_propio
- **N3** Operacion «Rechazo de cheques sin percepción de multas» — Rechazo de cheques sin haber percibido en tiempo y forma las respectivas multas establecidas por la Ley 25.730 · props: `{"tipo": "Rechazo de cheques"}` · tramo (exacta): «haya rechazado cheques sin haber percibido en tiempo y forma las respectivas multas» · punto_propio
- **N4** Sujeto «Bancos» · props: `{"nivel": "clase"}` · sin tramo · punto_propio · compartido (149 procedencias en el grafo)
- **N5** TextoOrdenado «Cuentas corrientes» · props: `{"archivo": "ctacte.pdf", "materia": "Reglamentación de la cuenta corriente bancaria", "version": "Comunicación A 8444 (vigencia 05/06/2026)"}` · sin tramo · punto_propio · compartido (380 procedencias en el grafo)

**Aristas de la extracción (3)**
- **A1** N1 —condicion_de→ N2 Obligacion «Cierre de cuentas dentro de 30 días»
- **A2** N2 —aplica_a→ N4 Sujeto «Bancos» (mención «La entidad financiera», exacta, R4_sugerencia_modelo)
- **A3** N2 —condiciona→ N3 Operacion «Rechazo de cheques sin percepción de multas»

**Remisiones derivadas (0 aristas)**

**Estructurales (3)**: establecida_en → TextoOrdenado «Cuentas corrientes» ×3

## 44. `cap::2.5.6` — estrato no_item (14 del sorteo) · cap · págs. 12 · estado `completo_ok_directo`

> *heredado (encabezado, S2):* Sección 2. Capital mínimo por riesgo de crédito.
> *heredado (chapeau_seccion, S2):* A los efectos de la aplicación de las disposiciones de la presente sección, las entidades financieras se clasificarán en: i)Grupo 1: entidades calificadas por el BCRA como de importancia sistémica a nivel local
> *heredado (chapeau_seccion, S2):* (D-SIB) y sucursales o subsidiarias de bancos del exterior calificados como de impor- tancia sistémica global (G-SIB).
> *heredado (chapeau_seccion, S2):* ii) Grupo 2: entidades financieras no comprendidas en el acápite i). En aquellos casos en que no se establezcan disposiciones específicas para cada uno de los citados grupos de entidades financieras, deberá aplicarse el mismo tratamiento a ambos grupos. Las entidades financieras que presenten cambios en su calificación –conforme a lo previsto en los acápites precedentes–, contarán con un plazo de 6 meses para aplicar las disposiciones específicas correspondientes al nuevo grupo al que pertenezcan.
> *heredado (encabezado, 2.5):* 2.5. Criterios para la determinación de los activos ponderados por riesgo.
> *propio:* 2.5.6. El tratamiento otorgado a la exposición al sector público no financiero no será de aplica- ción en las operaciones con contrapartes a las cuales el BCRA les haya otorgado el tra- tamiento previsto para las personas del sector privado no financiero. En estos casos, co- rresponderá considerarlas como exposiciones a empresas del sector privado no finan- ciero.

**Nodos (6)**
- **N1** Condicion «Condición: BCRA otorgó tratamiento sector privado» — Supuesto en que el BCRA ha otorgado a la contraparte el tratamiento de persona del sector privado no financiero. · tramo (exacta): «a las cuales el BCRA les haya otorgado el tratamiento previsto para las personas del sector privado no financiero» · punto_propio
- **N2** Excepcion «Excepción tratamiento sector público no financiero» — El tratamiento de exposición al sector público no financiero no aplica cuando el BCRA ha otorgado a la contraparte el tratamiento de persona del sector privado no financiero. · tramo (exacta): «El tratamiento otorgado a la exposición al sector público no financiero no será de aplicación en las operaciones con contrapartes a las cuales el BCRA les haya otorgado el tratamiento previsto para las personas del sector privado no financiero» · punto_propio
- **N3** Obligacion «Consideración como exposición sector privado» — Las entidades financieras deben considerar las operaciones con contrapartes tratadas como sector privado no financiero como exposiciones a empresas del sector privado no financiero. · props: `{"tipo": "asignacion"}` · tramo (exacta): «corresponderá considerarlas como exposiciones a empresas del sector privado no financiero» · punto_propio
- **N4** Operacion «Operaciones con contrapartes tratadas como sector privado» — Operaciones con contrapartes que el BCRA ha tratado como personas del sector privado no financiero, que deben considerarse como exposiciones a empresas del sector privado no financiero. · props: `{"tipo": "Clasificación de exposición"}` · tramo (exacta): «operaciones con contrapartes a las cuales el BCRA les haya otorgado el tratamiento previsto para las personas del sector privado no financiero» · punto_propio
- **N5** Sujeto «Entidades financieras» · props: `{"nivel": "clase", "alias": ["Entidades financieras emisoras de tarjetas de crédito y/o compra", "Entidad financiera emisora de tarjetas de crédito y/o compra"]}` · sin tramo · punto_propio · compartido (328 procedencias en el grafo)
- **N6** TextoOrdenado «Texto Ordenado Capitales Mínimos» · props: `{"archivo": "TO_capitales_minimos_actual.pdf", "materia": "Capitales mínimos de las entidades financieras", "version": "Comunicación A 8418 (vigencia 10/04/2026)"}` · sin tramo · punto_propio · compartido (453 procedencias en el grafo)

**Aristas de la extracción (3)**
- **A1** N1 —condicion_de→ N2 Excepcion «Excepción tratamiento sector público no financiero»
- **A2** N1 —condicion_de→ N3 Obligacion «Consideración como exposición sector privado»
- **A3** N3 —aplica_a→ N5 Sujeto «Entidades financieras» (mención «las entidades financieras», exacta, R1_label_exacto)

**Remisiones derivadas (0 aristas)**

**Estructurales (4)**: establecida_en → TextoOrdenado «Texto Ordenado Capitales Mínimos» ×4

## 45. `ext::4.2::cierre` — estrato no_item (15 del sorteo) · ext · págs. 58 · estado `completo_ok_directo`

> *heredado (encabezado, S4):* Sección 4. Otras disposiciones específicas.
> *heredado (encabezado, 4.2):* 4.2. Operaciones cursadas a través del Sistema de Monedas Locales (SML).
> *propio:* En el caso de la República Federativa del Brasil, las operaciones comerciales no podrán tener un plazo de pago que exceda a los 360 (trescientos sesenta) días corridos. En todos los casos, la entidad deberá requerir una declaración jurada del cliente respecto a que la operación corresponde a aquellas comprendidas en este sistema y que se cumplen las disposiciones específicas y generales que le resulten normativamente aplicables. La entidad deberá realizar un boleto de compra y/o venta de cambio, según corresponda, conforme a lo estipulado en el punto 5.3.

**Nodos (6)**
- **N1** Obligacion «Realizar boleto de compra y/o venta de cambio — conforme punto 5.3» — La entidad deberá realizar un boleto de compra y/o venta de cambio, según corresponda, conforme a lo estipulado en el punto 5.3. · props: `{"tipo": "otra"}` · tramo (exacta): «La entidad deberá realizar un boleto de compra y/o venta de cambio, según corresponda, conforme a lo estipulado en el punto 5.3» · bloque_cierre
- **N2** Obligacion «Requerir declaración jurada del cliente — correspondencia SML» — La entidad deberá requerir una declaración jurada del cliente respecto a que la operación corresponde a aquellas comprendidas en este sistema y que se cumplen las disposiciones específicas y generales que le resulten normativamente aplicables. · props: `{"tipo": "otra"}` · tramo (exacta): «la entidad deberá requerir una declaración jurada del cliente respecto a que la operación corresponde a aquellas comprendidas en este sistema y que se cumplen las disposiciones específicas y generales que le resulten normativamente aplicables» · bloque_cierre
- **N3** Operacion «Operaciones comerciales Brasil SML» — Operaciones comerciales cursadas a través del Sistema de Monedas Locales con destino a la República Federativa del Brasil. · props: `{"tipo": "operación comercial en SML"}` · tramo (exacta): «operaciones comerciales» · bloque_cierre
- **N4** Restriccion «Plazo máximo 360 días — operaciones comerciales Brasil» — En el caso de la República Federativa del Brasil, las operaciones comerciales no podrán tener un plazo de pago que exceda a los 360 (trescientos sesenta) días corridos. · props: `{"tipo": "limite_cuantitativo", "umbrales": [{"tramo": "360 (trescientos sesenta) días corridos", "valor": "360", "unidad": "dias", "dias_tipo": "corridos", "comparacion": "maximo_inclusivo", "regla_comparacion": "negacion:raiz_exced", "origen": "e1", "tramo_verificado": "exacta"}]}` · tramo (exacta): «las operaciones comerciales no podrán tener un plazo de pago que exceda a los 360 (trescientos sesenta) días corridos» · bloque_cierre
- **N5** Sujeto «Entidades autorizadas a operar en cambios (Exterior)» · props: `{"nivel": "rol"}` · sin tramo · bloque_cierre · compartido (344 procedencias en el grafo)
- **N6** TextoOrdenado «Texto Ordenado Exterior Cambios» · props: `{"archivo": "TO_exterior_cambios_actual.pdf", "materia": "Exterior y cambios", "version": "Comunicación A 8307 (vigencia 26/08/2025)"}` · sin tramo · bloque_cierre · compartido (930 procedencias en el grafo)

**Aristas de la extracción (4)**
- **A1** N1 —aplica_a→ N5 Sujeto «Entidades autorizadas a operar en cambios (Exterior)» (mención «la entidad», exacta, R4_sugerencia_modelo)
- **A2** N2 —aplica_a→ N5 Sujeto «Entidades autorizadas a operar en cambios (Exterior)» (mención «la entidad», exacta, R4_sugerencia_modelo)
- **A3** N4 —aplica_a→ N5 Sujeto «Entidades autorizadas a operar en cambios (Exterior)» (mención «las entidades», no, R4_sugerencia_modelo)
- **A4** N4 —limita→ N3 Operacion «Operaciones comerciales Brasil SML» [coherencia: coherente]

**Remisiones derivadas (5 aristas)**
- **R1–R5** N1 —remite_a→ `ext::5.3` (interna; 5 nodo(s) destino: Obligacion «Declaración jurada en boleto de cambio»; Obligacion «Firma del cliente en boleto de cambio»; Obligacion «Identificación del cliente en boleto»; Obligacion «Constatación de carácter genuino y límites aplicables»; Operacion «Operación de cambio») · evidencia «de cambio, según corresponda, conforme a lo estipulado en el punto 5.3.»

**Estructurales (4)**: establecida_en → TextoOrdenado «Texto Ordenado Exterior Cambios» ×4

## 46. `cap::8.2.2.2` — estrato no_item (16 del sorteo) · cap · págs. 156 · estado `aceptado_tras_reintento`

> *heredado (encabezado, S8):* Sección 8. Responsabilidad patrimonial computable.
> *heredado (encabezado, 8.2):* 8.2. Conceptos computables.
> *heredado (encabezado, 8.2.2):* 8.2.2. Capital adicional de nivel uno (CA ).
> *heredado (intro, 8.2.2):* n1
> *propio:* 8.2.2.2. Primas de emisión resultantes de instrumentos incluidos en el CA . n1 Además, en los casos de consolidación, incluye:

**Nodos (2)**
- **N1** Definicion «Primas de emisión — CA n1» — Partida computable en el capital adicional de nivel uno que incluye las primas de emisión resultantes de instrumentos incluidos en el CA n1; en los casos de consolidación, se incluyen también en este concepto · props: `{"termino": "Primas de emisión resultantes de instrumentos incluidos en el CA"}` · tramo (exacta): «Primas de emisión resultantes de instrumentos incluidos en el CA» · punto_propio
- **N2** TextoOrdenado «Texto Ordenado Capitales Mínimos» · props: `{"archivo": "TO_capitales_minimos_actual.pdf", "materia": "Capitales mínimos de las entidades financieras", "version": "Comunicación A 8418 (vigencia 10/04/2026)"}` · sin tramo · punto_propio · compartido (453 procedencias en el grafo)

**Aristas de la extracción (0)**

**Remisiones derivadas (0 aristas)**

**Estructurales (1)**: establecida_en → TextoOrdenado «Texto Ordenado Capitales Mínimos» ×1

## 47. `ext::3.11.5` — estrato no_item (17 del sorteo) · ext · págs. 35, 36 · estado `completo_ok_directo`

> *heredado (encabezado, S3):* Sección 3. Disposiciones específicas para los egresos por el mercado de cambios
> *heredado (chapeau_seccion, S3):* Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–, adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables.
> *heredado (encabezado, 3.11):* 3.11. Otras compras de moneda extranjera por parte de residentes con aplicación específica.
> *propio:* 3.11.5. A los efectos del registro de las operaciones admitidas en los puntos 3.11.1., 3.11.2. y 3.11.3., la entidad interviniente deberá confeccionar un boleto de cambio bajo el concepto “A19. Constitución de depósitos en moneda extranjera para aplicar al pago de servicios de deuda”, y al momento de la aplicación de los fondos adquiridos se deberá efectuar un boleto de compra bajo el mismo concepto y otro de venta por el concepto correspondiente a la cancelación del servicio de deuda. Por las operaciones del punto 3.11.3., al momento de constitución de las garantías, la entidad deberá confeccionar el boleto por el concepto de cobro de exportaciones de bienes o servicios o por el ingreso o la liquidación del endeudamiento, según corresponda.

**Nodos (11)**
- **N1** Obligacion «Efectuar boleto compra aplicación fondos» — Al momento de la aplicación de los fondos adquiridos se debe efectuar un boleto de compra bajo el concepto A19. · props: `{"tipo": "asignacion"}` · tramo (exacta): «al momento de la aplicación de los fondos adquiridos se deberá efectuar un boleto de compra bajo el mismo concepto» · punto_propio
- **N2** Obligacion «Confeccionar boleto cambio depósitos» — La entidad interviniente debe confeccionar un boleto de cambio bajo el concepto A19 para la constitución de depósitos en moneda extranjera destinados al pago de servicios de deuda. · props: `{"tipo": "asignacion"}` · tramo (exacta): «la entidad interviniente deberá confeccionar un boleto de cambio bajo el concepto "A19. Constitución de depósitos en moneda extranjera para aplicar al pago de servicios de deuda"» · punto_propio
- **N3** Obligacion «Confeccionar boleto garantías punto 3.11.3» — Para operaciones del punto 3.11.3., al momento de constitución de las garantías, la entidad debe confeccionar el boleto por el concepto de cobro de exportaciones de bienes o servicios o por el ingreso o liquidación del endeudamiento, según corresponda. · props: `{"tipo": "asignacion"}` · tramo (exacta): «Por las operaciones del punto 3.11.3., al momento de constitución de las garantías, la entidad deberá confeccionar el boleto por el concepto de cobro de exportaciones de bienes o servicios o por el ingreso o la liquidación del endeudamiento, según corresponda» · punto_propio
- **N4** Obligacion «Efectuar boleto venta cancelación deuda» — Se debe efectuar un boleto de venta por el concepto correspondiente a la cancelación del servicio de deuda. · props: `{"tipo": "asignacion"}` · tramo (exacta): «otro de venta por el concepto correspondiente a la cancelación del servicio de deuda» · punto_propio
- **N5** Operacion «Confección boleto cambio depósitos moneda extranjera» — Confección de un boleto de cambio bajo el concepto A19 para la constitución de depósitos en moneda extranjera destinados al pago de servicios de deuda, en relación con operaciones admitidas en puntos 3.11.1., 3.11.2. y 3.11.3. · props: `{"tipo": "Confección de boleto de cambio"}` · tramo (exacta): «la entidad interviniente deberá confeccionar un boleto de cambio bajo el concepto "A19. Constitución de depósitos en moneda extranjera para aplicar al pago de servicios de deuda"» · punto_propio
- **N6** Operacion «Confección boleto compra aplicación fondos» — Confección de un boleto de compra bajo el concepto A19 al momento de la aplicación de los fondos adquiridos. · props: `{"tipo": "Confección de boleto de compra"}` · tramo (exacta): «al momento de la aplicación de los fondos adquiridos se deberá efectuar un boleto de compra bajo el mismo concepto» · punto_propio
- **N7** Operacion «Confección boleto garantías exportaciones» — Confección de boleto al momento de constitución de garantías, por el concepto de cobro de exportaciones de bienes o servicios o por el ingreso o liquidación del endeudamiento, según corresponda, para operaciones del punto 3.11.3. · props: `{"tipo": "Confección de boleto"}` · tramo (exacta): «Por las operaciones del punto 3.11.3., al momento de constitución de las garantías, la entidad deberá confeccionar el boleto por el concepto de cobro de exportaciones de bienes o servicios o por el ingreso o la liquidación del endeudamiento, según corresponda» · punto_propio
- **N8** Operacion «Confección boleto venta cancelación deuda» — Confección de un boleto de venta por el concepto correspondiente a la cancelación del servicio de deuda. · props: `{"tipo": "Confección de boleto de venta"}` · tramo (exacta): «otro de venta por el concepto correspondiente a la cancelación del servicio de deuda» · punto_propio
- **N9** Sujeto «la entidad» · props: `{"nivel": "propuesto", "cuarentena": "true", "padre_sugerido": "Sujeto_rol_entidad_autorizada_exterior", "colision_cross_to": "true"}` · sin tramo · punto_propio · compartido (6 procedencias en el grafo)
- **N10** Sujeto «Entidades autorizadas a operar en cambios (Exterior)» · props: `{"nivel": "rol"}` · sin tramo · punto_propio · compartido (344 procedencias en el grafo)
- **N11** TextoOrdenado «Texto Ordenado Exterior Cambios» · props: `{"archivo": "TO_exterior_cambios_actual.pdf", "materia": "Exterior y cambios", "version": "Comunicación A 8307 (vigencia 26/08/2025)"}` · sin tramo · punto_propio · compartido (930 procedencias en el grafo)

**Aristas de la extracción (4)**
- **A1** N1 —aplica_a→ N9 Sujeto «la entidad» (mención «la entidad», exacta, cuarentena)
- **A2** N2 —aplica_a→ N10 Sujeto «Entidades autorizadas a operar en cambios (Exterior)» (mención «la entidad interviniente», exacta, R4_sugerencia_modelo)
- **A3** N3 —aplica_a→ N9 Sujeto «la entidad» (mención «la entidad», exacta, cuarentena)
- **A4** N4 —aplica_a→ N9 Sujeto «la entidad» (mención «la entidad», exacta, cuarentena)

**Remisiones derivadas (87 aristas)**
- **R1–R29** N3 —remite_a→ `ext::3.11.3` (interna; 16 nodo(s) destino: Condicion «Compra de moneda extranjera para garantías»; Condicion «Cuentas en entidades financieras locales o exterior»; Condicion «Endeudamiento financiero punto 3.5 o prefinanciaciones admitidas»; Condicion «Endeudamientos comprendidos en punto 7.9 originados desde 07/01/21»; Condicion «Endeudamientos punto 7.9.1.4 originados desde 08/08/25»; Condicion «Montos exigibles en contratos de endeudamiento»; Condicion «Prefinanciaciones de exportaciones punto 7.8.5»; Excepcion «Extensión a fideicomisos — acceso mercado cambios»; Excepcion «Acceso para fideicomisos constituidos en el país»; Operacion «Acceso al mercado de cambios para compra de moneda extranjera»; Operacion «Acceso al mercado de cambios para residentes»; Operacion «Acceso al mercado de cambios — residentes»; Potestad «Acceso mercado cambios — endeudamientos y prefinanciaciones»; Potestad «Facultad de dar acceso al mercado de cambios»; Potestad «Facultad de dar acceso al mercado de cambios»; Potestad «Facultad de dar acceso — entidades») · evidencia «los efectos del registro de las operaciones admitidas en los puntos 3.11.1., 3.11.2. y 3.11.3., la entidad interviniente»
- **R5–R28** N3 —remite_a→ `ext::3.11.1` (interna; 8 nodo(s) destino: Condicion «Endeudamientos o fideicomisos constituidos en el país»; Obligacion «Dar acceso al mercado de cambios — residentes con endeudamientos»; Operacion «Compra de moneda extranjera — garantías de endeudamientos»; Operacion «Compra de moneda extranjera para garantías»; Operacion «Compra de moneda extranjera para garantías de endeudamientos»; Potestad «Facultad de dar acceso al mercado de cambios»; Potestad «Facultad de dar acceso al mercado de cambios»; Potestad «Facultad de dar acceso al mercado de cambios — garantías») · evidencia «los efectos del registro de las operaciones admitidas en los puntos 3.11.1., 3.11.2. y 3.11.3., la entidad interviniente»
- **R13–R27** N3 —remite_a→ `ext::3.11.2` (interna; 5 nodo(s) destino: Operacion «Acceso al mercado de cambios para residentes»; Operacion «Compra de moneda extranjera — acceso anticipado»; Potestad «Facultad dar acceso mercado cambios — residentes deudores»; Potestad «Facultad de dar acceso al mercado de cambios»; Potestad «Facultad de dar acceso al mercado de cambios — compra anticipada») · evidencia «los efectos del registro de las operaciones admitidas en los puntos 3.11.1., 3.11.2. y 3.11.3., la entidad interviniente»
- **R30–R58** N5 —remite_a→ `ext::3.11.3` (interna; 16 nodo(s) destino: Condicion «Compra de moneda extranjera para garantías»; Condicion «Cuentas en entidades financieras locales o exterior»; Condicion «Endeudamiento financiero punto 3.5 o prefinanciaciones admitidas»; Condicion «Endeudamientos comprendidos en punto 7.9 originados desde 07/01/21»; Condicion «Endeudamientos punto 7.9.1.4 originados desde 08/08/25»; Condicion «Montos exigibles en contratos de endeudamiento»; Condicion «Prefinanciaciones de exportaciones punto 7.8.5»; Excepcion «Extensión a fideicomisos — acceso mercado cambios»; Excepcion «Acceso para fideicomisos constituidos en el país»; Operacion «Acceso al mercado de cambios para compra de moneda extranjera»; Operacion «Acceso al mercado de cambios para residentes»; Operacion «Acceso al mercado de cambios — residentes»; Potestad «Acceso mercado cambios — endeudamientos y prefinanciaciones»; Potestad «Facultad de dar acceso al mercado de cambios»; Potestad «Facultad de dar acceso al mercado de cambios»; Potestad «Facultad de dar acceso — entidades») · evidencia «los efectos del registro de las operaciones admitidas en los puntos 3.11.1., 3.11.2. y 3.11.3., la entidad interviniente»
- **R34–R57** N5 —remite_a→ `ext::3.11.1` (interna; 8 nodo(s) destino: Condicion «Endeudamientos o fideicomisos constituidos en el país»; Obligacion «Dar acceso al mercado de cambios — residentes con endeudamientos»; Operacion «Compra de moneda extranjera — garantías de endeudamientos»; Operacion «Compra de moneda extranjera para garantías»; Operacion «Compra de moneda extranjera para garantías de endeudamientos»; Potestad «Facultad de dar acceso al mercado de cambios»; Potestad «Facultad de dar acceso al mercado de cambios»; Potestad «Facultad de dar acceso al mercado de cambios — garantías») · evidencia «los efectos del registro de las operaciones admitidas en los puntos 3.11.1., 3.11.2. y 3.11.3., la entidad interviniente»
- **R42–R56** N5 —remite_a→ `ext::3.11.2` (interna; 5 nodo(s) destino: Operacion «Acceso al mercado de cambios para residentes»; Operacion «Compra de moneda extranjera — acceso anticipado»; Potestad «Facultad dar acceso mercado cambios — residentes deudores»; Potestad «Facultad de dar acceso al mercado de cambios»; Potestad «Facultad de dar acceso al mercado de cambios — compra anticipada») · evidencia «los efectos del registro de las operaciones admitidas en los puntos 3.11.1., 3.11.2. y 3.11.3., la entidad interviniente»
- **R59–R87** N7 —remite_a→ `ext::3.11.3` (interna; 16 nodo(s) destino: Condicion «Compra de moneda extranjera para garantías»; Condicion «Cuentas en entidades financieras locales o exterior»; Condicion «Endeudamiento financiero punto 3.5 o prefinanciaciones admitidas»; Condicion «Endeudamientos comprendidos en punto 7.9 originados desde 07/01/21»; Condicion «Endeudamientos punto 7.9.1.4 originados desde 08/08/25»; Condicion «Montos exigibles en contratos de endeudamiento»; Condicion «Prefinanciaciones de exportaciones punto 7.8.5»; Excepcion «Extensión a fideicomisos — acceso mercado cambios»; Excepcion «Acceso para fideicomisos constituidos en el país»; Operacion «Acceso al mercado de cambios para compra de moneda extranjera»; Operacion «Acceso al mercado de cambios para residentes»; Operacion «Acceso al mercado de cambios — residentes»; Potestad «Acceso mercado cambios — endeudamientos y prefinanciaciones»; Potestad «Facultad de dar acceso al mercado de cambios»; Potestad «Facultad de dar acceso al mercado de cambios»; Potestad «Facultad de dar acceso — entidades») · evidencia «los efectos del registro de las operaciones admitidas en los puntos 3.11.1., 3.11.2. y 3.11.3., la entidad interviniente»
- **R63–R86** N7 —remite_a→ `ext::3.11.1` (interna; 8 nodo(s) destino: Condicion «Endeudamientos o fideicomisos constituidos en el país»; Obligacion «Dar acceso al mercado de cambios — residentes con endeudamientos»; Operacion «Compra de moneda extranjera — garantías de endeudamientos»; Operacion «Compra de moneda extranjera para garantías»; Operacion «Compra de moneda extranjera para garantías de endeudamientos»; Potestad «Facultad de dar acceso al mercado de cambios»; Potestad «Facultad de dar acceso al mercado de cambios»; Potestad «Facultad de dar acceso al mercado de cambios — garantías») · evidencia «los efectos del registro de las operaciones admitidas en los puntos 3.11.1., 3.11.2. y 3.11.3., la entidad interviniente»
- **R71–R85** N7 —remite_a→ `ext::3.11.2` (interna; 5 nodo(s) destino: Operacion «Acceso al mercado de cambios para residentes»; Operacion «Compra de moneda extranjera — acceso anticipado»; Potestad «Facultad dar acceso mercado cambios — residentes deudores»; Potestad «Facultad de dar acceso al mercado de cambios»; Potestad «Facultad de dar acceso al mercado de cambios — compra anticipada») · evidencia «los efectos del registro de las operaciones admitidas en los puntos 3.11.1., 3.11.2. y 3.11.3., la entidad interviniente»

**Catálogo de sujetos (1)**
- **C1** Sujeto «la entidad» —padre_sugerido→ Sujeto «Entidades autorizadas a operar en cambios (Exterior)»

**Estructurales (8)**: establecida_en → TextoOrdenado «Texto Ordenado Exterior Cambios» ×8

## 48. `pro::S5` — estrato no_item (18 del sorteo) · pro · págs. 33 · estado `completo_ok_directo`

> *propio:* Sección 5. Sanciones. El sujeto obligado y quienes resulten responsables serán pasibles de la aplicación de las sanciones previstas en las normas sobre “Régimen disciplinario a cargo del Banco Central de la República Argentina (Leyes 21.526 y 25.065) y tramitación de sumarios cambiarios (Ley 19.359)”, por los in- cumplimientos que se constaten respecto de estas normas y respecto de los contenidos desarrolla- dos en los manuales de procedimiento interno con motivo de ellas.

**Nodos (5)**
- **N1** Comunicacion «Tramitación de sumarios cambiarios» · props: `{"codigo": "Ley 19.359", "tipo": "externa"}` · tramo (exacta): «tramitación de sumarios cambiarios (Ley 19.359)» · punto_propio
- **N2** Comunicacion «Régimen disciplinario BCRA» · props: `{"codigo": "Leyes 21.526 y 25.065", "tipo": "externa"}` · tramo (exacta): «Régimen disciplinario a cargo del Banco Central de la República Argentina (Leyes 21.526 y 25.065)» · punto_propio
- **N3** Obligacion «Sanciones por incumplimientos» — El sujeto obligado y quienes resulten responsables serán pasibles de la aplicación de sanciones conforme al Régimen disciplinario del BCRA (Leyes 21.526 y 25.065) y tramitación de sumarios cambiarios (Ley 19.359), por incumplimientos de estas normas y de los contenidos de los manuales de procedimiento interno. · props: `{"tipo": "otra"}` · tramo (exacta): «El sujeto obligado y quienes resulten responsables serán pasibles de la aplicación de las sanciones previstas en las normas sobre "Régimen disciplinario a cargo del Banco Central de la República Argentina (Leyes 21.526 y 25.065) y tramitación de sumarios cambiarios (Ley 19.359)"» · punto_propio
- **N4** Sujeto «Sujetos obligados (Protección de usuarios)» · props: `{"nivel": "rol"}` · sin tramo · punto_propio · compartido (75 procedencias en el grafo)
- **N5** TextoOrdenado «Texto Ordenado Protección de Usuarios» · props: `{"archivo": "TO_proteccion_usuarios_servicios_financieros_actual.pdf", "materia": "Protección de los usuarios de servicios financieros", "version": "Comunicación A 8433 (vigencia 07/05/2026)"}` · sin tramo · punto_propio · compartido (99 procedencias en el grafo)

**Aristas de la extracción (1)**
- **A1** N3 —aplica_a→ N4 Sujeto «Sujetos obligados (Protección de usuarios)» (mención «El sujeto obligado y quienes resulten responsables», exacta, R4_sugerencia_modelo)

**Remisiones derivadas (0 aristas)**

**Estructurales (3)**: establecida_en → TextoOrdenado «Texto Ordenado Protección de Usuarios» ×1; referencia → Comunicacion «Tramitación de sumarios cambiarios» ×1; referencia → Comunicacion «Régimen disciplinario BCRA» ×1

## 49. `ctacte::4.5.2::intro` — estrato no_item (19 del sorteo) · ctacte · págs. 28 · estado `aceptado_con_residuales`

> *heredado (encabezado, S4):* Sección 4. Cheques de pago diferido.
> *heredado (encabezado, 4.5):* 4.5. Negociación bursátil.
> *heredado (encabezado, 4.5.2):* 4.5.2. De tratarse de cheques que contengan la señalada leyenda (segundo párrafo del punto
> *propio:* 4.1.) y cuando sean presentados en los mercados de valores:

**Nodos (1)**
- **N1** TextoOrdenado «Cuentas corrientes» · props: `{"archivo": "ctacte.pdf", "materia": "Reglamentación de la cuenta corriente bancaria", "version": "Comunicación A 8444 (vigencia 05/06/2026)"}` · sin tramo · bloque_intro · compartido (380 procedencias en el grafo)

**Aristas de la extracción (0)**

**Remisiones derivadas (0 aristas)**

**Estructurales (0)**: 

## 50. `docvig::1.2.1` — estrato no_item (20 del sorteo) · docvig · págs. 3 · estado `aceptado_con_residuales`

> *heredado (encabezado, S1):* Sección 1. Para argentinos
> *heredado (encabezado, 1.2):* 1.2. Mayores de 75 años al 31.12.14 y los incapaces declarados judicialmente.
> *propio:* 1.2.1. Libreta de Enrolamiento.

**Nodos (1)**
- **N1** TextoOrdenado «Documento de Vigencia» · props: `{"archivo": "docvig.pdf", "materia": "Documentos de identificación en vigencia", "version": "Comunicación A 8338 (vigencia 02/10/2025)"}` · sin tramo · punto_propio · compartido (30 procedencias en el grafo)

**Aristas de la extracción (0)**

**Remisiones derivadas (0 aristas)**

**Estructurales (0)**: 

## 51. `ric::11.2::intro` — estrato no_item (21 del sorteo) · ric · págs. 52, 53, 54, 55 · estado `aceptado_con_residuales`

Flags de E0: `{"contenido_tabular": true, "formula": true, "evidencia_tabular": ["Coef. de CONCEPTOS COMPRENDIDOS B a n d a s T e m p o r a l e s", "actualización En pesos no actualizables y pesos actualizables 0 1 2 … 19", "1/2/3 0 1/2 10101 Activos susceptibles de estandarización a tasa de interés fija"], "evidencia_formula": ["0 a 6 1/2 50100 FF Netos (CF(k) o CF(tk)) = 10100(0)+20100(x)-30100(0)-40110(0)-40120(x) x", "0 a 6 1/2 50200 FF Netos (CF(k) o CF(tk)) = 10200(0)+20200(x)-30200(0)-40210(0)-40220(x) x", "0 a 6 1/2 101000000 Subtotal Activos (1)= 101010000(x)+101000099(0) x=0 a 6 (escenario)"], "tablas_e0": [{"tabla": "ric::tabla028", "origen": "e0_tablas", "estado": "parseada", "paginas": [52], "serializada": true, "bloque": "ric::tabla028", "modo": "posicional", "celdas_propagadas": 0, "celdas_con_alcance": 1, "combinadas_sin_propagar": 5, "filas_subtitulo": 2}, {"tabla": "ric::tabla029", "origen": "e0_tablas", "estado": "parseada", "paginas": [53], "serializada": true, "bloque": "ric::tabla029", "modo": "posicional", "celdas_propagadas": 0, "celdas_con_alcance": 1, "combinadas_sin_propagar": 4, "filas_subtitulo": 2}, {"tabla": "ric::tabla030", "origen": "e0_tablas", "estado": "parseada", "paginas": [54], "serializada": true, "bloque": "ric::tabla030", "modo": "posicional", "celdas_propagadas": 0, "celdas_con_alcance": 1, "combinadas_sin_propagar": 5, "filas_subtitulo": 2}, {"tabla": "ric::tabla031", "origen": "e0_tablas", "estado": "parseada", "paginas": [55], "serializada": true, "bloque": "ric::tabla031", "modo": "posicional", "celdas_propagadas": 0, "celdas_con_alcance": 1, "combinadas_sin_propagar": 4, "filas_subtitulo": 2}], "contenido_tabular_residual": true}`

> *heredado (encabezado, S11):* Sección 11. Información complementaria vinculada al cálculo del riesgo de tasa de interés en cartera de inversión.
> *heredado (encabezado, 11.2):* 11.2. Modelos de información.
> *propio:* Cuadros 11.2.1. a) [TABLA ric::tabla028 | página 52 | e0_tablas | posicional] Fila 1: col1 = Coef. de actualización | col2 = Escenarios | col3 = Margen | col4 = Código | col5 = CONCEPTOS COMPRENDIDOS En pesos no actualizables y pesos actualizables | col6 = B a n d a s T e m p o r a l e s ⟨abarca hasta col10⟩ Fila 2: col6 = 0 | col7 = 1 | col8 = 2 | col9 = … | col10 = 19 Fila 3: col1 = 1/2/3 | col2 = 0 | col3 = 1/2 | col4 = 10101 | col5 = Activos susceptibles de estandarización a tasa de interés fija Fila 4: col1 = 1 | col2 = 0 | col3 = 1/2 | col4 = 10102 | col5 = Activos susceptibles de estandarización a tasa de interés variable Fila 5: col1 = 1 | col2 = 0 | col3 = 1/2 | col4 = 10103 | col5 = Activos susceptibles de estandarización a tasa de interés fija con opciones automáticas implícitas Fila 6: col1 = 1 | col2 = 0 | col3 = 1/2 | col4 = 10104 | col5 = Activos susceptibles de estandarización a tasa de interés variable con opciones automáticas implícitas Fila 7: col1 = 1/2/3 | col2 = 0 | col3 = 1/2 | col4 = 10105 | col5 = Partidas fuera de Balance a tasa de Interes fija Fila 8: col1 = 1 | col2 = 0 | col3 = 1/2 | col4 = 10106 | col5 = Partidas fuera de Balance a tasa de Interes Variable Fila 9: col2 = 0 | col3 = 1/2 | col4 = 10100 | col5 = Activos susceptibles de estandarización Fila 10: col1 = 1/2/3 | col2 = 0 a 6 | col3 = 1/2 | col4 = 20101 | col5 = Préstamos a tasa fija sujetos al riesgo de cancelación anticipada Fila 11: col5 = Activos no susceptibles de estandarización Fila 12: col1 = 1/2/3 | col2 = 0 | col3 = 1/2 | col4 = 30101 | col5 = Pasivos susceptibles de estandarización a tasa de interés fija Fila 13: col1 = 1 | col2 = 0 | col3 = 1/2 | col4 = 30102 | col5 = Pasivos susceptibles de estandarización a tasa de interés variable Fila 14: col1 = 1/2/3 | col2 = 0 | col3 = 1/2 | col4 = 30103 | col5 = Pasivos susceptibles de estandarización a tasa de interés fija con opciones automáticas implícitas Fila 15: col1 = 1 | col2 = 0 | col3 = 1/2 | col4 = 30104 | col5 = Pasivos susceptibles de estandarización a tasa de interés variable con opciones automáticas implícitas Fila 16: col1 = 1/2/3 | col2 = 0 | col3 = 1/2 | col4 = 30105 | col5 = Partidas fuera de Balance a tasa de Interes fija Fila 17: col1 = 1 | col2 = 0 | col3 = 1/2 | col4 = 30106 | col5 = Partidas fuera de Balance a tasa de Interes Variable Fila 18: col2 = 0 | col3 = 1/2 | col4 = 30100 | col5 = Pasivos susceptibles de estandarización Fila 19: col1 = 1 | col2 = 0 | col3 = 1/2 | col4 = 40111 | col5 = Depósitos sin vencimiento minorista transaccional básicos Fila 20: col1 = 1 | col2 = 0 | col3 = 1/2 | col4 = 40112 | col5 = Depósitos sin vencimiento minorista transaccional no básicos Fila 21: col1 = 1 | col2 = 0 | col3 = 1/2 | col4 = 40113 | col5 = Depósitos sin vencimiento minorista no transaccional básicos Fila 22: col1 = 1 | col2 = 0 | col3 = 1/2 | col4 = 40114 | col5 = Depósitos sin vencimiento minorista no transaccional no básicos Fila 23: col1 = 1 | col2 = 0 | col3 = 1/2 | col4 = 40115 | col5 = Depósitos sin vencimiento mayoristas básicos Fila 24: col1 = 1 | col2 = 0 | col3 = 1/2 | col4 = 40116 | col5 = Depósitos sin vencimiento mayoristas no básicos Fila 25: col2 = 0 | col3 = 1/2 | col4 = 40110 | col5 = Subtotal Fila 26: col1 = 1/2/3 | col2 = 0 a 6 | col3 = 1/2 | col4 = 40120 | col5 = Depósito a plazo sujetos a riesgo de retiro anticipado Fila 27: col5 = Pasivos no susceptibles de estandarización Fila 28: col2 = 0 a 6 | col3 = 1/2 | col4 = 50100 | col5 = FF Netos (CF(k) o CF(tk)) = 10100(0)+20100(x)-30100(0)-40110(0)-40120(x) x=0 a 6 (escenario) Fila 29: col2 = 0 a 6 | col3 = 1/2 | col4 = 60100 | col5 = Factor de descuento compuesto continuo [FIN TABLA ric::tabla028] Cuadro 11.2.1. b) [TABLA ric::tabla029 | página 53 | e0_tablas | posicional] Fila 1: col1 = Escenarios | col2 = Margen | col3 = Código | col4 = CONCEPTOS COMPRENDIDOS En dólares estadounidenses | col5 = B a n d a s T e m p o r a l e s ⟨abarca hasta col9⟩ Fila 2: col5 = 0 | col6 = 1 | col7 = 2 | col8 = … | col9 = 19 Fila 3: col1 = 0 | col2 = 1/2 | col3 = 10201 | col4 = Activos susceptibles de estandarización a tasa de interés fija Fila 4: col1 = 0 | col2 = 1/2 | col3 = 10202 | col4 = Activos susceptibles de estandarización a tasa de interés variable Fila 5: col1 = 0 | col2 = 1/2 | col3 = 10203 | col4 = Activos susceptibles de estandarización a tasa de interés fija con opciones automáticas implícitas Fila 6: col1 = 0 | col2 = 1/2 | col3 = 10204 | col4 = Activos susceptibles de estandarización a tasa de interés variable con opciones automáticas implícitas Fila 7: col1 = 0 | col2 = 1/2 | col3 = 10205 | col4 = Partidas fuera de Balance a tasa de Interes fija Fila 8: col1 = 0 | col2 = 1/2 | col3 = 10206 | col4 = Partidas fuera de Balance a tasa de Interes Variable Fila 9: col1 = 0 | col2 = 1/2 | col3 = 10200 | col4 = Activos susceptibles de estandarización Fila 10: col1 = 0 a 6 | col2 = 1/2 | col3 = 20201 | col4 = Préstamos a tasa fija sujetos al riesgo de cancelación anticipada Fila 11: col4 = Activos no susceptibles de estandarización Fila 12: col1 = 0 | col2 = 1/2 | col3 = 30201 | col4 = Pasivos susceptibles de estandarización a tasa de interés fija Fila 13: col1 = 0 | col2 = 1/2 | col3 = 30202 | col4 = Pasivos susceptibles de estandarización a tasa de interés variable Fila 14: col1 = 0 | col2 = 1/2 | col3 = 30203 | col4 = Pasivos susceptibles de estandarización a tasa de interés fija con opciones automáticas implícitas Fila 15: col1 = 0 | col2 = 1/2 | col3 = 30204 | col4 = Pasivos susceptibles de estandarización a tasa de interés variable con opciones automáticas implícitas Fila 16: col1 = 0 | col2 = 1/2 | col3 = 30205 | col4 = Partidas fuera de Balance a tasa de Interes fija Fila 17: col1 = 0 | col2 = 1/2 | col3 = 30206 | col4 = Partidas fuera de Balance a tasa de Interes Variable Fila 18: col1 = 0 | col2 = 1/2 | col3 = 30200 | col4 = Pasivos susceptibles de estandarización Fila 19: col1 = 0 | col2 = 1/2 | col3 = 40211 | col4 = Depósitos sin vencimiento minorista transaccional básicos Fila 20: col1 = 0 | col2 = 1/2 | col3 = 40212 | col4 = Depósitos sin vencimiento minorista transaccional no básicos Fila 21: col1 = 0 | col2 = 1/2 | col3 = 40213 | col4 = Depósitos sin vencimiento minorista no transaccional básicos Fila 22: col1 = 0 | col2 = 1/2 | col3 = 40214 | col4 = Depósitos sin vencimiento minorista no transaccional no básicos Fila 23: col1 = 0 | col2 = 1/2 | col3 = 40215 | col4 = Depósitos sin vencimiento mayoristas básicos Fila 24: col1 = 0 | col2 = 1/2 | col3 = 40216 | col4 = Depósitos sin vencimiento mayoristas no básicos Fila 25: col1 = 0 | col2 = 1/2 | col3 = 40210 | col4 = Subtotal Fila 26: col1 = 0 a 6 | col2 = 1/2 | col3 = 40220 | col4 = Depósito a plazo sujetos a riesgo de retiro anticipado Fila 27: col4 = Pasivos no susceptibles de estandarización Fila 28: col1 = 0 a 6 | col2 = 1/2 | col3 = 50200 | col4 = FF Netos (CF(k) o CF(tk)) = 10200(0)+20200(x)-30200(0)-40210(0)-40220(x) x=0 a 6 (escenario) Fila 29: col1 = 0 a 6 | col2 = 1/2 | col3 = 60200 | col4 = Factor de descuento compuesto continuo [FIN TABLA ric::tabla029] Cuadro 11.2.2. a) [TABLA ric::tabla030 | página 54 | e0_tablas | posicional] Fila 1: col1 = Coef. de actualización | col2 = Escenarios | col3 = Margen | col4 = Código | col5 = CONCEPTOS COMPRENDIDOS En pesos no actualizables y pesos actualizables | col6 = B a n d a s T e m p o r a l e s ⟨abarca hasta col10⟩ Fila 2: col6 = 0 | col7 = 1 | col8 = 2 | col9 = … | col10 = 19 Fila 3: col5 = ACTIVOS Fila 4: col1 = 1/2/3 | col2 = 0 a 6 | col3 = 1/2 | col4 = 101010000 | col5 = Préstamos Fila 5: col1 = 1/2/3 | col2 = 0 a 6 | col3 = 1/2 | col4 = 101010100 | col5 = Sector privado no financiero y residentes en el exterior Fila 6: col1 = 1/2/3 | col2 = 0 a 6 | col3 = 1/2 | col4 = 101010101 | col5 = Hipotecarios sobre la vivienda Fila 7: col1 = 1/2/3 | col2 = 0 a 6 | col3 = 1/2 | col4 = 101010102 | col5 = Con otras garantías hipotecarias Fila 8: col1 = 1/2/3 | col2 = 0 a 6 | col3 = 1/2 | col4 = 101010103 | col5 = Prendarios sobre automotores Fila 9: col1 = 1/2/3 | col2 = 0 a 6 | col3 = 1/2 | col4 = 101010104 | col5 = Con otras garantías prendarias Fila 10: col1 = 1/2/3 | col2 = 0 a 6 | col3 = 1/2 | col4 = 101010105 | col5 = Personales Fila 11: col1 = 1/2/3 | col2 = 0 a 6 | col3 = 1/2 | col4 = 101010106 | col5 = Adelantos Fila 12: col1 = 1/2/3 | col2 = 0 a 6 | col3 = 1/2 | col4 = 101010107 | col5 = Tarjetas de Crédito Fila 13: col1 = 1/2/3 | col2 = 0 a 6 | col3 = 1/2 | col4 = 101010108 | col5 = Sola Firma Fila 14: col1 = 1/2/3 | col2 = 0 a 6 | col3 = 1/2 | col4 = 101010109 | col5 = Documentos descontados Fila 15: col1 = 1/2/3 | col2 = 0 a 6 | col3 = 1/2 | col4 = 101010110 | col5 = Otros Fila 16: col1 = 1/2/3 | col2 = 0 a 6 | col3 = 1/2 | col4 = 101010200 | col5 = Sector público Fila 17: col1 = 1/2/3 | col2 = 0 a 6 | col3 = 1/2 | col4 = 101010300 | col5 = Sector financiero Fila 18: col1 = 1/2/3 | col2 = 0 | col3 = 1/2 | col4 = 101020000 | col5 = Otros créditos por intermediación financiera Fila 19: col1 = 1/2/3 | col2 = 0 | col3 = 1/2 | col4 = 101030000 | col5 = Posición neta compradora de activos financieros no sujetos a riesgo de mercado. Fila 20: col1 = 1/2/3 | col2 = 0 | col3 = 1/2 | col4 = 101040000 | col5 = Otros activos Fila 21: col1 = 1/2/3 | col2 = 0 | col3 = 1/2 | col4 = 101050000 | col5 = Partidas fuera de balance no sujetos a riesgo de mercado. Fila 22: col2 = 0 | col3 = 1/2 | col4 = 101000099 | col5 = Subtotal Activos excluyendo prestamos Fila 23: col2 = 0 a 6 | col3 = 1/2 | col4 = 101000000 | col5 = Subtotal Activos (1)= 101010000(x)+101000099(0) x=0 a 6 (escenario) Fila 24: col5 = PASIVOS Fila 25: col1 = 1/2/3 | col2 = 0 a 6 | col3 = 1/2 | col4 = 201010000 | col5 = Depósitos Fila 26: col1 = 1 | col2 = 0 a 6 | col3 = 1/2 | col4 = 201010100 | col5 = A la vista Fila 27: col1 = 1/2/3 | col2 = 0 a 6 | col3 = 1/2 | col4 = 201010200 | col5 = Otros Depositos Fila 28: col1 = 1/2/3 | col2 = 0 a 6 | col3 = 1/2 | col4 = 201010201 | col5 = Deposito Plazo Fijo Sector Público no Financiero Fila 29: col1 = 1/2/3 | col2 = 0 a 6 | col3 = 1/2 | col4 = 201010202 | col5 = Deposito Plazo Fijo Sector Prívado no Financiero Fila 30: col1 = 1/2/3 | col2 = 0 a 6 | col3 = 1/2 | col4 = 201010203 | col5 = Otros Fila 31: col1 = 1/2/3 | col2 = 0 | col3 = 1/2 | col4 = 201020000 | col5 = Otras obligaciones intermediación financiera Fila 32: col1 = 1/2/3 | col2 = 0 | col3 = 1/2 | col4 = 201020100 | col5 = Obligaciones Negociables Fila 33: col1 = 1/2/3 | col2 = 0 | col3 = 1/2 | col4 = 201020200 | col5 = Otras Fila 34: col1 = 1/2/3 | col2 = 0 | col3 = 1/2 | col4 = 201020300 | col5 = Asistencia del B.C.R.A. Fila 35: col1 = 1/2/3 | col2 = 0 | col3 = 1/2 | col4 = 201030000 | col5 = Posición neta vendedora de activos financieros no sujetos a riesgo de mercado Fila 36: col1 = 1/2/3 | col2 = 0 | col3 = 1/2 | col4 = 201040000 | col5 = Otros pasivos Fila 37: col1 = 1/2/3 | col2 = 0 | col3 = 1/2 | col4 = 201050000 | col5 = Partidas fuera de balance no sujetos a riesgo de mercado. Fila 38: col2 = 0 | col3 = 1/2 | col4 = 201000099 | col5 = Subtotal Pasivos excluyendo depósitos Fila 39: col2 = 0 a 6 | col3 = 1/2 | col4 = 201000000 | col5 = Subtotal Pasivos (2)= 201010000(x)+201000099(0) x=0 a 6 (escenario) Fila 40: col2 = 0 a 6 | col3 = 1/2 | col4 = 501000000 | col5 = FF Netos (1) - (2) [FIN TABLA ric::tabla030] Cuadro 11.2.2. b) [TABLA ric::tabla031 | página 55 | e0_tablas | posicional] Fila 1: col1 = Escenarios | col2 = Margen | col3 = Código | col4 = CONCEPTOS COMPRENDIDOS En dólares estadounidenses | col5 = B a n d a s T e m p o r a l e s ⟨abarca hasta col9⟩ Fila 2: col5 = 0 | col6 = 1 | col7 = 2 | col8 = … | col9 = 19 Fila 3: col4 = ACTIVOS Fila 4: col1 = 0 a 6 | col2 = 1/2 | col3 = 102010000 | col4 = Préstamos Fila 5: col1 = 0 a 6 | col2 = 1/2 | col3 = 102010100 | col4 = Sector privado no financiero y residentes en el exterior Fila 6: col1 = 0 a 6 | col2 = 1/2 | col3 = 102010101 | col4 = Hipotecarios sobre la vivienda Fila 7: col1 = 0 a 6 | col2 = 1/2 | col3 = 102010102 | col4 = Con otras garantías hipotecarias Fila 8: col1 = 0 a 6 | col2 = 1/2 | col3 = 102010103 | col4 = Prendarios sobre automotores Fila 9: col1 = 0 a 6 | col2 = 1/2 | col3 = 102010104 | col4 = Con otras garantías prendarias Fila 10: col1 = 0 a 6 | col2 = 1/2 | col3 = 102010105 | col4 = Personales Fila 11: col1 = 0 a 6 | col2 = 1/2 | col3 = 102010106 | col4 = Adelantos Fila 12: col1 = 0 a 6 | col2 = 1/2 | col3 = 102010107 | col4 = Tarjetas de Crédito Fila 13: col1 = 0 a 6 | col2 = 1/2 | col3 = 102010108 | col4 = Sola Firma Fila 14: col1 = 0 a 6 | col2 = 1/2 | col3 = 102010109 | col4 = Documentos descontados Fila 15: col1 = 0 a 6 | col2 = 1/2 | col3 = 102010110 | col4 = Otros Fila 16: col1 = 0 a 6 | col2 = 1/2 | col3 = 102010200 | col4 = Sector público Fila 17: col1 = 0 a 6 | col2 = 1/2 | col3 = 102010300 | col4 = Sector financiero Fila 18: col1 = 0 | col2 = 1/2 | col3 = 102020000 | col4 = Otros créditos por intermediación financiera Fila 19: col1 = 0 | col2 = 1/2 | col3 = 102030000 | col4 = Posición neta compradora de activos financieros no sujetos a riesgo de mercado. Fila 20: col1 = 0 | col2 = 1/2 | col3 = 102040000 | col4 = Otros activos Fila 21: col1 = 0 | col2 = 1/2 | col3 = 102050000 | col4 = Partidas fuera de balance no sujetos a riesgo de mercado. Fila 22: col1 = 0 | col2 = 1/2 | col3 = 102000099 | col4 = Subtotal Activos excluyendo prestamos Fila 23: col1 = 0 a 6 | col2 = 1/2 | col3 = 102000000 | col4 = Subtotal Activos (1)= 101010000(x)+101000099(0) x=0 a 6 (escenario) Fila 24: col4 = PASIVOS Fila 25: col1 = 0 a 6 | col2 = 1/2 | col3 = 202010000 | col4 = Depósitos Fila 26: col1 = 0 a 6 | col2 = 1/2 | col3 = 202010100 | col4 = A la vista Fila 27: col1 = 0 a 6 | col2 = 1/2 | col3 = 202010200 | col4 = Otros Depositos Fila 28: col1 = 0 a 6 | col2 = 1/2 | col3 = 202010201 | col4 = Deposito Plazo Fijo Sector Público no Financiero Fila 29: col1 = 0 a 6 | col2 = 1/2 | col3 = 202010202 | col4 = Deposito Plazo Fijo Sector Prívado no Financiero Fila 30: col1 = 0 a 6 | col2 = 1/2 | col3 = 202010203 | col4 = Otros Fila 31: col1 = 0 | col2 = 1/2 | col3 = 202020000 | col4 = Otras obligaciones intermediación financiera Fila 32: col1 = 0 | col2 = 1/2 | col3 = 202020100 | col4 = Obligaciones Negociables Fila 33: col1 = 0 | col2 = 1/2 | col3 = 202020200 | col4 = Otras Fila 34: col1 = 0 | col2 = 1/2 | col3 = 202020300 | col4 = Asistencia del B.C.R.A. Fila 35: col1 = 0 | col2 = 1/2 | col3 = 202030000 | col4 = Posición neta vendedora de activos financieros no sujetos a riesgo de mercado Fila 36: col1 = 0 | col2 = 1/2 | col3 = 202040000 | col4 = Otros pasivos Fila 37: col1 = 0 | col2 = 1/2 | col3 = 202050000 | col4 = Partidas fuera de balance no sujetos a riesgo de mercado. Fila 38: col1 = 0 | col2 = 1/2 | col3 = 202000099 | col4 = Subtotal Pasivos excluyendo depósitos Fila 39: col1 = 0 a 6 | col2 = 1/2 | col3 = 202000000 | col4 = Subtotal Pasivos (2)= 202010000(x)+202000099(0) x=0 a 6 (escenario) Fila 40: col1 = 0 a 6 | col2 = 1/2 | col3 = 502000000 | col4 = FF Netos (1) - (2) [FIN TABLA ric::tabla031]

**Nodos (5)**
- **N1** Definicion «Cuadro 11.2.1.a) — Modelos información pesos» — Modelo de información para cálculo de riesgo de tasa de interés en cartera de inversión en pesos no actualizables y pesos actualizables, con bandas temporales de 0 a 19, incluyendo activos susceptibles de estandarización (códigos 10101-10106), activos no susceptibles de estandarización (código 20101), pasivos susceptibles de estandarización (códigos 30101-30106), pasivos no susceptibles de estandarización (código 40120), y factores de flujo neto (código 50100) y descuento (código 60100). · props: `{"termino": "Cuadro 11.2.1. a)"}` · tramo (exacta): «Cuadros 11.2.1. a)» · bloque_intro
- **N2** Definicion «Cuadro 11.2.1.b) — Modelos información dólares» — Modelo de información para cálculo de riesgo de tasa de interés en cartera de inversión en dólares estadounidenses, con bandas temporales de 0 a 19, incluyendo activos susceptibles de estandarización (códigos 10201-10206), activos no susceptibles de estandarización (código 20201), pasivos susceptibles de estandarización (códigos 30201-30206), pasivos no susceptibles de estandarización (código 40220), y factores de flujo neto (código 50200) y descuento (código 60200). · props: `{"termino": "Cuadro 11.2.1. b)"}` · tramo (exacta): «Cuadro 11.2.1. b)» · bloque_intro
- **N3** Definicion «Cuadro 11.2.2.a) — Modelos información detallada pesos» — Modelo de información detallada para cálculo de riesgo de tasa de interés en cartera de inversión en pesos no actualizables y pesos actualizables, con bandas temporales de 0 a 19, incluyendo activos (préstamos por sectores, otros créditos, posiciones netas, otros activos, partidas fuera de balance) y pasivos (depósitos, obligaciones de intermediación financiera, posiciones netas, otros pasivos, partidas fuera de balance), con subtotales y flujo neto. · props: `{"termino": "Cuadro 11.2.2. a)"}` · tramo (exacta): «Cuadro 11.2.2. a)» · bloque_intro
- **N4** Definicion «Cuadro 11.2.2.b) — Modelos información detallada dólares» — Modelo de información detallada para cálculo de riesgo de tasa de interés en cartera de inversión en dólares estadounidenses, con bandas temporales de 0 a 19, incluyendo activos (préstamos por sectores, otros créditos, posiciones netas, otros activos, partidas fuera de balance) y pasivos (depósitos, obligaciones de intermediación financiera, posiciones netas, otros pasivos, partidas fuera de balance), con subtotales y flujo neto. · props: `{"termino": "Cuadro 11.2.2. b)"}` · tramo (exacta): «Cuadro 11.2.2. b)» · bloque_intro
- **N5** TextoOrdenado «Régimen Informativo Contable Mensual» · props: `{"archivo": "TO_regimen_informativo_contable_mensual_actual.pdf", "materia": "RI Cont. Mensual - Exigencia e integración de capitales mínimos", "version": "Comunicación A 8396 (vigencia 30/01/2026)"}` · sin tramo · bloque_intro · compartido (88 procedencias en el grafo)

**Aristas de la extracción (0)**

**Remisiones derivadas (0 aristas)**

**Estructurales (4)**: establecida_en → TextoOrdenado «Régimen Informativo Contable Mensual» ×4

## 52. `ext::13.1::cierre` — estrato no_item (22 del sorteo) · ext · págs. 168 · estado `aceptado_con_residuales`

> *heredado (encabezado, S13):* Sección 13. Pagos de servicios prestados por no residentes.
> *heredado (encabezado, 13.1):* 13.1. Disposiciones generales.
> *propio:* Los casos que no encuadren en lo expuesto precedentemente quedan sujetos a la conformidad previa del BCRA, debiendo los pedidos ser canalizados por una entidad autorizada a realizar este tipo de pagos.

**Nodos (5)**
- **N1** Condicion «Supuesto: casos no encuadrados en disposiciones previas» — Supuesto en el que los casos no se ajustan a las disposiciones previas de la sección · tramo (exacta): «Los casos que no encuadren en lo expuesto precedentemente» · bloque_cierre
- **N2** Obligacion «Canalización de pedidos por entidad autorizada» — Los pedidos de conformidad previa deben ser canalizados a través de una entidad autorizada a realizar pagos de servicios prestados por no residentes · props: `{"tipo": "otra"}` · tramo (exacta): «debiendo los pedidos ser canalizados por una entidad autorizada a realizar este tipo de pagos» · bloque_cierre
- **N3** Potestad «Conformidad previa del BCRA — pagos no encuadrados» — El BCRA tiene la facultad de otorgar o denegar conformidad previa para los casos que no encuadren en las disposiciones precedentes · tramo (exacta): «quedan sujetos a la conformidad previa del BCRA» · bloque_cierre
- **N4** Sujeto «Entidades autorizadas a operar en cambios (Exterior)» · props: `{"nivel": "rol"}` · sin tramo · bloque_cierre · compartido (344 procedencias en el grafo)
- **N5** TextoOrdenado «Texto Ordenado Exterior Cambios» · props: `{"archivo": "TO_exterior_cambios_actual.pdf", "materia": "Exterior y cambios", "version": "Comunicación A 8307 (vigencia 26/08/2025)"}` · sin tramo · bloque_cierre · compartido (930 procedencias en el grafo)

**Aristas de la extracción (2)**
- **A1** N1 —condicion_de→ N3 Potestad «Conformidad previa del BCRA — pagos no encuadrados»
- **A2** N2 —aplica_a→ N4 Sujeto «Entidades autorizadas a operar en cambios (Exterior)» (mención «una entidad autorizada a realizar este tipo de pagos», exacta, R4_sugerencia_modelo)

**Remisiones derivadas (0 aristas)**

**Estructurales (3)**: establecida_en → TextoOrdenado «Texto Ordenado Exterior Cambios» ×3

## 53. `ric::10.1.2` — estrato no_item (23 del sorteo) · ric · págs. 43 · estado `completo_ok_directo`

Flags de E0: `{"formula": true, "evidencia_formula": ["Ratio de apalancamiento = [Medida del capital / Medida de la exposición] * 100 ="]}`

> *heredado (encabezado, S10):* Sección 10. Ratio de apalancamiento.
> *heredado (encabezado, 10.1):* 10.1. Normas de procedimiento
> *propio:* 10.1.2. Ratio de apalancamiento Surgirá de aplicar la expresión prevista en el punto 1.2. de las citadas normas: Ratio de apalancamiento = [Medida del capital / Medida de la exposición] * 100 = [PNb / ∑ Códigos (45110000 a 45140000)] * 100 (CN1)

**Nodos (4)**
- **N1** Definicion «Ratio de apalancamiento — fórmula» — Se calcula aplicando la expresión: [Medida del capital / Medida de la exposición] * 100, donde la Medida del capital es el PNb y la Medida de la exposición es la suma de los códigos 45110000 a 45140000. · props: `{"termino": "Ratio de apalancamiento"}` · tramo (exacta): «Ratio de apalancamiento = [Medida del capital / Medida de la exposición] * 100» · punto_propio
- **N2** Obligacion «Cálculo del Ratio de apalancamiento» — Las entidades deberán calcular el Ratio de apalancamiento aplicando la expresión prevista en el punto 1.2 de las normas de referencia. · props: `{"tipo": "calculo"}` · tramo (exacta): «Surgirá de aplicar la expresión prevista en el punto 1.2. de las citadas normas» · punto_propio
- **N3** Sujeto «Entidades comprendidas (Régimen Informativo)» · props: `{"nivel": "rol"}` · sin tramo · punto_propio · compartido (37 procedencias en el grafo)
- **N4** TextoOrdenado «Régimen Informativo Contable Mensual» · props: `{"archivo": "TO_regimen_informativo_contable_mensual_actual.pdf", "materia": "RI Cont. Mensual - Exigencia e integración de capitales mínimos", "version": "Comunicación A 8396 (vigencia 30/01/2026)"}` · sin tramo · punto_propio · compartido (88 procedencias en el grafo)

**Aristas de la extracción (1)**
- **A1** N2 —aplica_a→ N3 Sujeto «Entidades comprendidas (Régimen Informativo)» (mención «las entidades», no, R4_sugerencia_modelo)

**Remisiones derivadas (0 aristas)**

**Estructurales (2)**: establecida_en → TextoOrdenado «Régimen Informativo Contable Mensual» ×2

## 54. `cla::10.2.1` — estrato no_item (24 del sorteo) · cla · págs. 43 · estado `completo_ok_directo`

> *heredado (encabezado, S10):* Sección 10. Otros obligados a la observancia de las normas sobre clasificación de deudores.
> *heredado (encabezado, 10.2):* 10.2. Fiduciarios de fideicomisos financieros comprendidos en la Ley de Entidades Financieras.
> *propio:* 10.2.1. Clasificación de deudores de créditos fideicomitidos. Deberán clasificar a los deudores de los créditos fideicomitidos de acuerdo con la pe- riodicidad y demás condiciones establecidas para las carteras “comercial” o “para con- sumo o vivienda”, según corresponda.

**Nodos (5)**
- **N1** Condicion «Cartera comercial o para consumo o vivienda» — La clasificación se realiza según la cartera a la que corresponda el crédito fideicomitido: comercial o para consumo o vivienda · tramo (exacta): «de acuerdo con la periodicidad y demás condiciones establecidas para las carteras "comercial" o "para consumo o vivienda", según corresponda» · punto_propio
- **N2** Obligacion «Clasificar deudores de créditos fideicomitidos» — Deber de clasificar a los deudores de los créditos fideicomitidos de acuerdo con la periodicidad y demás condiciones establecidas para las carteras comercial o para consumo o vivienda, según corresponda · props: `{"tipo": "otra"}` · tramo (exacta): «Deberán clasificar a los deudores de los créditos fideicomitidos de acuerdo con la periodicidad y demás condiciones establecidas para las carteras "comercial" o "para consumo o vivienda", según corresponda» · punto_propio
- **N3** Operacion «Clasificación de deudores de créditos fideicomitidos» — Clasificación de deudores de créditos fideicomitidos según la periodicidad y demás condiciones establecidas para las carteras comercial o para consumo o vivienda · props: `{"tipo": "Clasificación de deudor"}` · tramo (no): «Clasificación de deudores de los créditos fideicomitidos» · punto_propio
- **N4** Sujeto «Fiduciarios de fideicomisos financieros» · props: `{"nivel": "clase"}` · sin tramo · punto_propio · compartido (4 procedencias en el grafo)
- **N5** TextoOrdenado «Texto Ordenado Clasificación de Deudores» · props: `{"archivo": "TO_clasificacion_deudores_actual.pdf", "materia": "Clasificación de deudores", "version": "Comunicación A 8378 (vigencia 20/12/2025)"}` · sin tramo · punto_propio · compartido (140 procedencias en el grafo)

**Aristas de la extracción (3)**
- **A1** N1 —condicion_de→ N2 Obligacion «Clasificar deudores de créditos fideicomitidos»
- **A2** N2 —aplica_a→ N4 Sujeto «Fiduciarios de fideicomisos financieros» (mención «Fiduciarios de fideicomisos financieros», exacta, R1_label_exacto)
- **A3** N3 —requiere→ N2 Obligacion «Clasificar deudores de créditos fideicomitidos»

**Remisiones derivadas (0 aristas)**

**Estructurales (3)**: establecida_en → TextoOrdenado «Texto Ordenado Clasificación de Deudores» ×3

## 55. `lingob::1.3::intro` — estrato no_item (25 del sorteo) · lingob · págs. 3 · estado `completo_ok_directo`

> *heredado (encabezado, S1):* Sección 1. Conceptos generales.
> *heredado (encabezado, 1.3):* 1.3. Directorio.
> *propio:* El Directorio de la entidad financiera, entre otros aspectos, será responsable de:

**Nodos (1)**
- **N1** TextoOrdenado «Lineamientos de Gobierno Societario» · props: `{"archivo": "lingob.pdf", "materia": "Lineamientos para el gobierno societario en entidades financieras", "version": "Comunicación A 7465 (vigencia 26/02/2022)"}` · sin tramo · bloque_intro · compartido (137 procedencias en el grafo)

**Aristas de la extracción (0)**

**Remisiones derivadas (0 aristas)**

**Estructurales (0)**: 

## 56. `pagjub::1.6` — estrato no_item (26 del sorteo) · pagjub · págs. 4 · estado `aceptado_tras_reintento`

> *heredado (encabezado, S1):* Sección 1. Disposiciones generales.
> *propio:* 1.6. Otras disposiciones. En los aspectos no previstos por la presente reglamentación, regirá lo que establezca la ANSES.

**Nodos (2)**
- **N1** Potestad «Competencia normativa residual ANSES» — ANSES tiene la facultad de establecer normas para los aspectos no previstos por la presente reglamentación. · tramo (exacta): «regirá lo que establezca la ANSES» · punto_propio
- **N2** TextoOrdenado «Pago de beneficios ANSES» · props: `{"archivo": "pagjub.pdf", "materia": "Pago de beneficios de la seg. soc. por cuenta de la Adm. Nacional de la Seguridad Social (ANSES)", "version": "Comunicación A 6386 (vigencia 08/12/2017)"}` · sin tramo · punto_propio · compartido (48 procedencias en el grafo)

**Aristas de la extracción (0)**

**Remisiones derivadas (0 aristas)**

**Estructurales (1)**: establecida_en → TextoOrdenado «Pago de beneficios ANSES» ×1

## 57. `ext::7.3.5` — estrato no_item (27 del sorteo) · ext · págs. 84 · estado `completo_ok_directo`

> *heredado (encabezado, S7):* Sección 7. Cobros de exportaciones de bienes.
> *heredado (encabezado, 7.3):* 7.3. Aplicación de divisas de cobros de exportaciones.
> *heredado (intro, 7.3):* Existe una aplicación de divisas de cobros de exportaciones de bienes cuando se ha certificado que los propios bienes exportados o las divisas cobradas por ellos fueron utilizados para cancelar el capital, intereses y/o gastos de otorgamiento de operaciones de financiamiento, pagar utilidades y dividendos y/o concretar la repatriación de una inversión directa de un accionista no residente en los casos admitidos en los puntos 7.3.1. a 7.3.11. A los efectos que los cobros de exportaciones aplicados puedan ser imputados al cumplimiento de los permisos de embarque oficializados a partir del 02/09/19, será necesario contar en todos los casos con una certificación de aplicación emitida por la entidad encargada del “Seguimiento de anticipos y otras financiaciones de exportación de bienes”. Los exportadores que efectúen liquidaciones de moneda extranjera asociadas a las operaciones comprendidas en los puntos 7.3.1. al 7.3.10. deberán solicitar a la entidad interviniente que le asigne un número de identificación (número APX) y la incorpore al mencionado seguimiento. En el caso de operaciones comprendidas en el punto 7.3.8. que no registren liquidaciones en el mercado de cambios por ser refinanciaciones de deudas preexistentes, la entidad nominada por el exportador atento a lo establecido en el punto 7.9.3. deberá incorporarla al mencionado seguimiento, usando para su identificación el número correlativo que se le asignó a la operación del cliente (número ECO: Entidad-CUIT-N° Operación).
> *propio:* 7.3.5. Préstamos financieros con contratos vigentes al 31/08/19 cuyas condiciones prevean la atención de los servicios mediante la aplicación en el exterior del flujo de fondos de exportaciones de bienes. En el caso de operaciones liquidadas en el mercado de cambios entre el 16/09/05 y 10/11/17, la aplicación de las divisas al capital, intereses y otros conceptos permitidos sólo será admisible cuando la liquidación se hubiese encuadrado en disposiciones que habilitaban la aplicación de divisas de exportaciones de bienes a su cancelación.

**Nodos (4)**
- **N1** Condicion «Encuadramiento en disposiciones habilitantes — aplicación de divisas» — La liquidación debe haberse encuadrado en disposiciones que habilitaban la aplicación de divisas de exportaciones de bienes a su cancelación · tramo (exacta): «cuando la liquidación se hubiese encuadrado en disposiciones que habilitaban la aplicación de divisas de exportaciones de bienes a su cancelación» · punto_propio
- **N2** Operacion «Préstamos financieros con aplicación de divisas de exportaciones» — Operación de préstamo financiero con contrato vigente al 31 de agosto de 2019 cuyas condiciones prevean la atención de los servicios mediante la aplicación en el exterior del flujo de fondos de exportaciones de bienes · props: `{"tipo": "Préstamo financiero"}` · tramo (exacta): «Préstamos financieros con contratos vigentes al 31/08/19 cuyas condiciones prevean la atención de los servicios mediante la aplicación en el exterior del flujo de fondos de exportaciones de bienes» · punto_propio
- **N3** Restriccion «Admisibilidad de aplicación de divisas — operaciones 16/09/05 a 10/11/17» — Para operaciones liquidadas en el mercado de cambios entre el 16/09/05 y 10/11/17, la aplicación de las divisas al capital, intereses y otros conceptos permitidos sólo será admisible cuando la liquidación se hubiese encuadrado en disposiciones que habilitaban la aplicación de divisas de exportaciones de bienes a su cancelación · props: `{"tipo": "limite_cualitativo", "umbrales": [{"tramo": "entre el 16/09/05 y 10/11/17", "comparacion": "no_determinada", "regla_comparacion": "limite_relativo:sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}]}` · tramo (exacta): «la aplicación de las divisas al capital, intereses y otros conceptos permitidos sólo será admisible cuando la liquidación se hubiese encuadrado en disposiciones que habilitaban la aplicación de divisas de exportaciones de bienes a su cancelación» · punto_propio
- **N4** TextoOrdenado «Texto Ordenado Exterior Cambios» · props: `{"archivo": "TO_exterior_cambios_actual.pdf", "materia": "Exterior y cambios", "version": "Comunicación A 8307 (vigencia 26/08/2025)"}` · sin tramo · punto_propio · compartido (930 procedencias en el grafo)

**Aristas de la extracción (2)**
- **A1** N1 —condicion_de→ N3 Restriccion «Admisibilidad de aplicación de divisas — operaciones 16/09/05 a 10/11/17»
- **A2** N3 —limita→ N2 Operacion «Préstamos financieros con aplicación de divisas de exportaciones» [coherencia: coherente]

**Remisiones derivadas (0 aristas)**

**Estructurales (3)**: establecida_en → TextoOrdenado «Texto Ordenado Exterior Cambios» ×3

## 58. `ctacte::10.2.2::intro` — estrato no_item (28 del sorteo) · ctacte · págs. 52 · estado `completo_ok_directo`

> *heredado (encabezado, S10):* Sección 10. Avisos.
> *heredado (encabezado, 10.2):* 10.2. Contenido mínimo.
> *heredado (encabezado, 10.2.2):* 10.2.2. Requisitos adicionales en los avisos de rechazos al pago o a la registración de che-
> *propio:* ques.

**Nodos (1)**
- **N1** TextoOrdenado «Cuentas corrientes» · props: `{"archivo": "ctacte.pdf", "materia": "Reglamentación de la cuenta corriente bancaria", "version": "Comunicación A 8444 (vigencia 05/06/2026)"}` · sin tramo · bloque_intro · compartido (380 procedencias en el grafo)

**Aristas de la extracción (0)**

**Remisiones derivadas (0 aristas)**

**Estructurales (0)**: 

## 59. `ext::11.1.1::intro` — estrato no_item (29 del sorteo) · ext · págs. 160 · estado `aceptado_con_residuales`

> *heredado (encabezado, S11):* Sección 11. Sistema de seguimiento de pagos de importaciones (SEPAIMPO).
> *heredado (encabezado, 11.1):* 11.1. Seguimiento de oficializaciones de importación.
> *heredado (encabezado, 11.1.1):* 11.1.1. Responsabilidades de la entidad nominada.
> *propio:* La entidad nominada por el importador para el seguimiento de la oficialización del despacho de importación será la responsable de:

**Nodos (1)**
- **N1** TextoOrdenado «Texto Ordenado Exterior Cambios» · props: `{"archivo": "TO_exterior_cambios_actual.pdf", "materia": "Exterior y cambios", "version": "Comunicación A 8307 (vigencia 26/08/2025)"}` · sin tramo · bloque_intro · compartido (930 procedencias en el grafo)

**Aristas de la extracción (0)**

**Remisiones derivadas (0 aristas)**

**Estructurales (0)**: 

## 60. `cap::3.1.3::cierre` — estrato no_item (30 del sorteo) · cap · págs. 34 · estado `completo_ok_directo`

> *heredado (encabezado, S3):* Sección 3. Capital mínimo por riesgo de crédito. Titulizaciones e inversiones en fon- dos.
> *heredado (encabezado, 3.1):* 3.1. Tratamiento de las titulizaciones.
> *heredado (encabezado, 3.1.3):* 3.1.3. Requisitos de debida diligencia.
> *propio:* Cuando no se cumpla con alguno de estos requisitos de debida diligencia se deberá ponderar la posición de titulización al 1250 %. De tratarse de una entidad originante, de- berá considerarse lo dispuesto en el punto 3.1.12.

**Nodos (7)**
- **N1** Condicion «Entidad originante en titulización» — Supuesto en que la entidad sea originante de la titulización · tramo (exacta): «De tratarse de una entidad originante» · bloque_cierre
- **N2** Condicion «Incumplimiento requisitos debida diligencia» — Supuesto en que no se cumpla con alguno de los requisitos de debida diligencia en titulizaciones · tramo (exacta): «Cuando no se cumpla con alguno de estos requisitos de debida diligencia» · bloque_cierre
- **N3** Obligacion «Consideración disposiciones punto 3.1.12» — Deber de considerar lo dispuesto en el punto 3.1.12 cuando se trate de una entidad originante · props: `{"tipo": "otra"}` · tramo (exacta): «deberá considerarse lo dispuesto en el punto 3.1.12» · bloque_cierre
- **N4** Obligacion «Ponderación posición titulización 1250 %» — Deber de ponderar la posición de titulización al 1250 % cuando no se cumpla con los requisitos de debida diligencia · props: `{"tipo": "calculo", "umbrales": [{"tramo": "1250 %", "valor": "1250", "unidad": "porcentaje", "comparacion": "coeficiente", "regla_comparacion": "coeficiente", "origen": "e1", "tramo_verificado": "exacta"}]}` · tramo (exacta): «se deberá ponderar la posición de titulización al 1250 %» · bloque_cierre
- **N5** Sujeto «una entidad originante» · props: `{"nivel": "propuesto", "cuarentena": "true", "padre_sugerido": "Sujeto_entidad_originante_de_transferencia"}` · sin tramo · bloque_cierre
- **N6** Sujeto «Entidades alcanzadas (Capitales Mínimos)» · props: `{"nivel": "rol"}` · sin tramo · bloque_cierre · compartido (111 procedencias en el grafo)
- **N7** TextoOrdenado «Texto Ordenado Capitales Mínimos» · props: `{"archivo": "TO_capitales_minimos_actual.pdf", "materia": "Capitales mínimos de las entidades financieras", "version": "Comunicación A 8418 (vigencia 10/04/2026)"}` · sin tramo · bloque_cierre · compartido (453 procedencias en el grafo)

**Aristas de la extracción (4)**
- **A1** N1 —condicion_de→ N3 Obligacion «Consideración disposiciones punto 3.1.12»
- **A2** N2 —condicion_de→ N4 Obligacion «Ponderación posición titulización 1250 %»
- **A3** N3 —aplica_a→ N5 Sujeto «una entidad originante» (mención «una entidad originante», exacta, cuarentena)
- **A4** N4 —aplica_a→ N6 Sujeto «Entidades alcanzadas (Capitales Mínimos)» (mención «las entidades», no, R4_sugerencia_modelo)

**Remisiones derivadas (8 aristas)**
- **R1–R8** N3 —remite_a→ `cap::3.1.12` (interna; 8 nodo(s) destino: Definicion «Participación P — múltiples tramos»; Definicion «Participación P — un solo tramo»; Excepcion «Excepción para retitulizaciones»; Obligacion «Deducción de ganancias por ventas y cupones de mejora crediticia»; Operacion «Cálculo de exigencia máxima agregada»; Operacion «Cálculo de participación máxima por tramo»; Operacion «Tenencia de posiciones de titulización por originante»; Restriccion «Tope de exigencia de capital — posiciones retenidas/recompradas») · evidencia «entidad originante, de- berá considerarse lo dispuesto en el punto 3.1.12.»

**Catálogo de sujetos (1)**
- **C1** Sujeto «una entidad originante» —padre_sugerido→ Sujeto «Entidades originantes»

**Estructurales (4)**: establecida_en → TextoOrdenado «Texto Ordenado Capitales Mínimos» ×4

