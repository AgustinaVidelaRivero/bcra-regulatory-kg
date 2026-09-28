# U-INV-CANDIDATOS-2 — candidatos (O, D) con la remisión tal como la escribe el texto, grafo r1

- Grafo: `data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json` sha256 `0226e9477baee02d772bbfecee78a49441b189d0e0512ca5e22956dfb084196a`
- EV2: `data/experiment/exploracion/ev2_fidelidad/preguntas_ev2_fidelidad.json` sha256 `1d58733699c325c90510e1ead5f18eac6c3cd970ee3b0ab7ff141da539162b40`
- E0: `data/experiment/reextraccion_v2/e0_chunking/salida_enm01/chunks_cap.json` sha256 `1931138dac0a107a69a7ff6312400f00465b991d52135457735beeb3e442c825`
- E0: `data/experiment/reextraccion_v2/e0_chunking/salida_enm01/chunks_cla.json` sha256 `98808886a406d8321c678836a55f92eea983d594d95358dd21ceb537487ac0b1`
- E0: `data/experiment/reextraccion_v2/e0_chunking/salida_enm01/chunks_ext.json` sha256 `cbcd1a86f55ea49110610587873881c68c13a9d7975d3fd5e465f26302be2d12`
- E0: `data/experiment/reextraccion_v2/e0_chunking/salida_enm01/chunks_pro.json` sha256 `d8717d1c7423bb5f4d80cc830ff97635ce4d9839f8490b73860ea272568620e2`
- E0: `data/experiment/reextraccion_v2/e0_chunking/salida_enm01/chunks_ric.json` sha256 `fafebb82e07b34191b60022c1c179ea7d2213fd1f5d5f3a408b518c836c94c0d`
- Aristas de remisión: 5645; sin provenance to/punto: 0; destino Texto Ordenado completo: 6; destino sección: 116; destino de otra forma no numérica: 0; válidas: 5523
- Embudo: criterio 1: 413 → criterio 2: 357 → criterio 3: 333 → criterio 4: 80 → criterio 5: 59 → criterio 6: 14

## Candidatos que pasan los seis criterios (14)

### V01 — `cap::6.7.1.1` → {cap::1.1}

- Texto Ordenado de O: `cap`
- O = `cap::6.7.1.1` — 10 palabras
  - fragmento E0 `cap::6.7.1.1` (punto_terminal; campo `texto`):

````text
6.7.1.1. la RPC del último día del mes anterior; y
````

- d = `cap::1.1` — 51 palabras — mismo Texto Ordenado que O
  - fragmento E0 `cap::1.1` (punto_terminal; campo `texto`):

````text
1.1. Exigencia.
La exigencia de capital mínimo que las entidades financieras deberán tener integrada será
equivalente al mayor valor que resulte de la comparación entre la exigencia básica y la suma de
las determinadas por riesgos de crédito, de mercado –exigencia por las posiciones diarias de
los activos comprendidos– y operacional.
````

  - aristas de remisión con provenance O y destino d: 2
    - [Obligacion] «Integración de capital — RPC último día mes anterior» → [Obligacion] «Integración de capital mínimo requerido» (evidencia «rior | A los fines del cumplimiento de lo establecido en el punto 1.1., la integración se»)
    - [Obligacion] «Integración de capital — RPC último día mes anterior» → [Operacion] «Determinación de exigencia de capital mínimo» (evidencia «rior | A los fines del cumplimiento de lo establecido en el punto 1.1., la integración se»)
- Preguntas EV2 que citan O o algún d: ninguna

### V02 — `cla::3.3.3` → {cla::3.7}

- Texto Ordenado de O: `cla`
- O = `cla::3.3.3` — 43 palabras
  - fragmento E0 `cla::3.3.3` (punto_terminal; campo `texto`):

````text
3.3.3. El ejercicio de la opción de agrupar las financiaciones de naturaleza comercial de hasta el
equivalente a dos veces el importe de referencia establecido en el punto 3.7., cuenten o
no con garantías preferidas, junto con los créditos para consumo o vivienda.
````

- d = `cla::3.7` — 39 palabras — mismo Texto Ordenado que O
  - fragmento E0 `cla::3.7` (punto_terminal; campo `texto`):

````text
3.7. Importe de referencia.
El importe a considerar será el nivel máximo del valor de ventas totales anuales para la
categoría “Micro” correspondiente al sector “Comercio” que determine la autoridad de
aplicación de la Ley 24.467 (y sus modificatorias).
````

  - aristas de remisión con provenance O y destino d: 1
    - [Restriccion] «Tope de hasta dos veces importe referencia — agrupación comercial» → [Obligacion] «Considerar importe de referencia — ventas anuales Micro Comercio» (evidencia «ente a dos veces el importe de referencia establecido en el punto 3.7. | dos veces el impo»)
- Preguntas EV2 que citan O o algún d: ninguna

### V03 — `cla::5.1.1.1` → {cla::3.7}

- Texto Ordenado de O: `cla`
- O = `cla::5.1.1.1` — 60 palabras
  - fragmento E0 `cla::5.1.1.1` (punto_terminal; campo `texto`):

````text
5.1.1.1. Los créditos para consumo o vivienda.
Los créditos de esta clase que superen el equivalente a dos veces el importe de
referencia establecido en el punto 3.7. y cuyo repago no se encuentre vinculado
a ingresos fijos o periódicos del cliente sino a la evolución de su actividad pro-
ductiva o comercial se incluirán dentro de la cartera comercial.
````

- d = `cla::3.7` — 39 palabras — mismo Texto Ordenado que O
  - fragmento E0 `cla::3.7` (punto_terminal; campo `texto`):

````text
3.7. Importe de referencia.
El importe a considerar será el nivel máximo del valor de ventas totales anuales para la
categoría “Micro” correspondiente al sector “Comercio” que determine la autoridad de
aplicación de la Ley 24.467 (y sus modificatorias).
````

  - aristas de remisión con provenance O y destino d: 1
    - [Restriccion] «Créditos consumo/vivienda — monto supera dos veces importe referencia» → [Obligacion] «Considerar importe de referencia — ventas anuales Micro Comercio» (evidencia «ente a dos veces el importe de referencia establecido en el punto 3.7. | 2x importe refere»)
- Preguntas EV2 que citan O o algún d: ninguna

### V04 — `cla::5.1.2.3` → {cla::3.7}

- Texto Ordenado de O: `cla`
- O = `cla::5.1.2.3` — 39 palabras
  - fragmento E0 `cla::5.1.2.3` (punto_terminal; campo `texto`):

````text
5.1.2.3. Préstamos a Instituciones de Microcrédito –hasta el equivalente al 40 % del im-
porte de referencia establecido en el punto 3.7.– y a microemprendedores (se-
gún lo previsto en el punto 1.1.3.4. de las normas sobre “Gestión crediticia”).
````

- d = `cla::3.7` — 39 palabras — mismo Texto Ordenado que O
  - fragmento E0 `cla::3.7` (punto_terminal; campo `texto`):

````text
3.7. Importe de referencia.
El importe a considerar será el nivel máximo del valor de ventas totales anuales para la
categoría “Micro” correspondiente al sector “Comercio” que determine la autoridad de
aplicación de la Ley 24.467 (y sus modificatorias).
````

  - aristas de remisión con provenance O y destino d: 1
    - [Restriccion] «Tope 40 % importe de referencia (punto 3.7)» → [Obligacion] «Considerar importe de referencia — ventas anuales Micro Comercio» (evidencia «Tope 40 % importe de referencia (punto 3.7) | hasta el equival»)
- Preguntas EV2 que citan O o algún d: ninguna

### V05 — `cla::5.1.2.4` → {cla::3.7}

- Texto Ordenado de O: `cla`
- O = `cla::5.1.2.4` — 35 palabras
  - fragmento E0 `cla::5.1.2.4` (punto_terminal; campo `texto`):

````text
5.1.2.4. Las financiaciones de naturaleza comercial de hasta el equivalente a dos veces
el importe de referencia establecido en el punto 3.7., cuenten o no con garantías
preferidas, cuando la entidad haya optado por ello.
````

- d = `cla::3.7` — 39 palabras — mismo Texto Ordenado que O
  - fragmento E0 `cla::3.7` (punto_terminal; campo `texto`):

````text
3.7. Importe de referencia.
El importe a considerar será el nivel máximo del valor de ventas totales anuales para la
categoría “Micro” correspondiente al sector “Comercio” que determine la autoridad de
aplicación de la Ley 24.467 (y sus modificatorias).
````

  - aristas de remisión con provenance O y destino d: 1
    - [Restriccion] «Límite cuantitativo — dos veces importe referencia» → [Obligacion] «Considerar importe de referencia — ventas anuales Micro Comercio» (evidencia «ente a dos veces el importe de referencia establecido en el punto 3.7. | 2x importe refere»)
- Preguntas EV2 que citan O o algún d: ninguna

### V06 — `ext::3.4.4.3` → {ext::14.2.2}

- Texto Ordenado de O: `ext`
- O = `ext::3.4.4.3` — 51 palabras
  - fragmento E0 `ext::3.4.4.3` (punto_terminal; campo `texto`):

````text
3.4.4.3. El cliente es un Vehículo de Proyecto Único (VPU) adherido al Régimen de
Incentivo para Grandes Inversiones (RIGI) y las utilidades corresponden a
aportes de inversión extranjera directa que encuadran en lo previsto en el
punto 14.2.2.
El cliente deberá presentar la documentación que avale la capitalización
definitiva del aporte.
````

- d = `ext::14.2.2` — 112 palabras — mismo Texto Ordenado que O
  - fragmento E0 `ext::14.2.2` (punto_terminal; campo `texto`):

````text
14.2.2. En el marco de lo dispuesto en el punto 3.4. las entidades también podrán darle
acceso al mercado de cambios al VPU para pagar utilidades y dividendos a sus
accionistas no residentes, sin necesidad de contar con la conformidad previa del
BCRA si este requisito estuviese vigente, cuando el pago corresponda a montos
pendientes con el accionista no residente por:
i) la proporción de sus aportes de inversión directa en el VPU que fue ingresada y
liquidada por el mercado de cambios, o
ii) por sus aportes de inversión directa en especie instrumentados mediante la
entrega al VPU de bienes de capital que cumplen las condiciones previstas en
el punto 14.5.4.
````

  - aristas de remisión con provenance O y destino d: 5
    - [Restriccion] «Cliente debe encuadrar en situación — pagos de utilidades» → [Excepcion] «Exención conformidad previa BCRA — utilidades/dividendos» (evidencia «rsión extranjera directa que encuadran en lo previsto en el punto 14.2.2»)
    - [Restriccion] «Cliente debe encuadrar en situación — pagos de utilidades» → [Obligacion] «Cumplimiento requisitos — acceso cambios utilidades/dividendos» (evidencia «rsión extranjera directa que encuadran en lo previsto en el punto 14.2.2»)
    - [Restriccion] «Cliente debe encuadrar en situación — pagos de utilidades» → [Operacion] «Acceso mercado cambios — pago utilidades/dividendos VPU» (evidencia «rsión extranjera directa que encuadran en lo previsto en el punto 14.2.2»)
    - [Restriccion] «Cliente debe encuadrar en situación — pagos de utilidades» → [Restriccion] «Límite cualitativo — aportes inversión directa en especie» (evidencia «rsión extranjera directa que encuadran en lo previsto en el punto 14.2.2»)
    - [Restriccion] «Cliente debe encuadrar en situación — pagos de utilidades» → [Restriccion] «Límite cualitativo — proporción aportes inversión directa» (evidencia «rsión extranjera directa que encuadran en lo previsto en el punto 14.2.2»)
- Preguntas EV2 que citan O o algún d: ninguna

### V07 — `ext::3.6.1.2` → {ext::3.6.2}

- Texto Ordenado de O: `ext`
- O = `ext::3.6.1.2` — 34 palabras
  - fragmento E0 `ext::3.6.1.2` (punto_terminal; campo `texto`):

````text
3.6.1.2. las emisiones de títulos de deuda realizadas a partir del 01/09/19 con el
objeto de refinanciar deudas comprendidas en el punto 3.6.2. y conlleven un
incremento de la vida promedio de las obligaciones.
````

- d = `ext::3.6.2` — 33 palabras — mismo Texto Ordenado que O
  - fragmento E0 `ext::3.6.2` (punto_terminal; campo `texto`):

````text
3.6.2. Las entidades podrán dar acceso al mercado de cambios para la cancelación a partir
de su vencimiento de obligaciones en moneda extranjera entre residentes
instrumentadas mediante registros o escrituras públicos al 30/08/19.
````

  - aristas de remisión con provenance O y destino d: 2
    - [Restriccion] «Prohibición pagos deudas refinanciadas con incremento vida promedio» → [Obligacion] «Acceso mercado cambios para cancelación desde vencimiento» (evidencia «9/19 con el objeto de refinanciar deudas comprendidas en el punto 3.6.2., siempre que conlle»)
    - [Restriccion] «Prohibición pagos deudas refinanciadas con incremento vida promedio» → [Operacion] «Cancelación de obligaciones moneda extranjera» (evidencia «9/19 con el objeto de refinanciar deudas comprendidas en el punto 3.6.2., siempre que conlle»)
- Preguntas EV2 que citan O o algún d: ninguna

### V08 — `ext::3.17.1.4` → {ext::3.4.1, ext::3.4.2, ext::3.4.3}

- Texto Ordenado de O: `ext`
- O = `ext::3.17.1.4` — 25 palabras
  - fragmento E0 `ext::3.17.1.4` (punto_terminal; campo `texto`):

````text
3.17.1.4. Pagos de utilidades y dividendos a accionistas no residentes en la medida
que se verifiquen los requisitos previstos en los puntos 3.4.1. a 3.4.3.
````

- d = `ext::3.4.1` — 11 palabras — mismo Texto Ordenado que O
  - fragmento E0 `ext::3.4.1` (punto_terminal; campo `texto`):

````text
3.4.1. Las utilidades y dividendos correspondan a balances cerrados y auditados.
````

  - aristas de remisión con provenance O y destino d: 1
    - [Restriccion] «Requisitos puntos 3.4.1 a 3.4.3 — utilidades dividendos» → [Obligacion] «Balances cerrados y auditados» (evidencia «Requisitos puntos 3.4.1 a 3.4.3 — utilidades divide»)
- d = `ext::3.4.2` — 71 palabras — mismo Texto Ordenado que O
  - fragmento E0 `ext::3.4.2` (punto_terminal; campo `texto`):

````text
3.4.2. El monto total abonado por este concepto a accionistas no residentes, incluido el pago
cuyo curso se está solicitando, no supere el monto en moneda local que les
corresponda según la distribución determinada por la asamblea de accionistas.
La entidad deberá contar con una declaración jurada firmada por el representante legal
de la empresa residente o un apoderado con facultades suficientes para asumir este
compromiso en nombre de la empresa.
````

  - aristas de remisión con provenance O y destino d: 3
    - [Restriccion] «Requisitos puntos 3.4.1 a 3.4.3 — utilidades dividendos» → [Obligacion] «Declaración jurada representante legal» (evidencia «Requisitos puntos 3.4.1 a 3.4.3 — utilidades divide»)
    - [Restriccion] «Requisitos puntos 3.4.1 a 3.4.3 — utilidades dividendos» → [Operacion] «Giro divisas utilidades dividendos exterior» (evidencia «Requisitos puntos 3.4.1 a 3.4.3 — utilidades divide»)
    - [Restriccion] «Requisitos puntos 3.4.1 a 3.4.3 — utilidades dividendos» → [Restriccion] «Monto total no supere distribución asamblea» (evidencia «Requisitos puntos 3.4.1 a 3.4.3 — utilidades divide»)
- d = `ext::3.4.3` — 34 palabras — mismo Texto Ordenado que O
  - fragmento E0 `ext::3.4.3` (punto_terminal; campo `texto`):

````text
3.4.3. La entidad deberá verificar que el cliente haya dado cumplimiento en caso de
corresponder, a la declaración de la última presentación vencida del “Relevamiento de
activos y pasivos externos” por las operaciones involucradas.
````

  - aristas de remisión con provenance O y destino d: 2
    - [Restriccion] «Requisitos puntos 3.4.1 a 3.4.3 — utilidades dividendos» → [Obligacion] «Verificación de cumplimiento declaración de activos y pasivos externos» (evidencia «Requisitos puntos 3.4.1 a 3.4.3 — utilidades divide»)
    - [Restriccion] «Requisitos puntos 3.4.1 a 3.4.3 — utilidades dividendos» → [Operacion] «Giro de utilidades y dividendos al exterior» (evidencia «Requisitos puntos 3.4.1 a 3.4.3 — utilidades divide»)
- Preguntas EV2 que citan O o algún d: ninguna

### V09 — `ext::3.18.3.1` → {ext::7.1.1.2}

- Texto Ordenado de O: `ext`
- O = `ext::3.18.3.1` — 28 palabras
  - fragmento E0 `ext::3.18.3.1` (punto_terminal; campo `texto`):

````text
3.18.3.1. 5% (cinco por ciento) cuando corresponda a bienes que tienen asignado
un plazo de 30 (treinta) días corridos en virtud de lo dispuesto en el punto
7.1.1.2.
````

- d = `ext::7.1.1.2` — 30 palabras — mismo Texto Ordenado que O
  - fragmento E0 `ext::7.1.1.2` (punto_terminal; campo `texto`):

````text
7.1.1.2. 30 (treinta) días corridos para las exportaciones de bienes que correspondan
a las posiciones arancelarias 1003.90.10, 1003.90.80, 1007.90.00 y a las
correspondientes al capítulo 27 (excepto la posición 2716.00.00).
````

  - aristas de remisión con provenance O y destino d: 2
    - [Restriccion] «Coeficiente 5% — bienes plazo 30 días» → [Obligacion] «Ingreso y liquidación 30 días — exportaciones posiciones arancelarias» (evidencia «30 (treinta) días corridos en virtud de lo dispuesto en el punto 7.1.1.2 | 5%»)
    - [Restriccion] «Coeficiente 5% — bienes plazo 30 días» → [Operacion] «Ingreso y liquidación de divisas — exportación» (evidencia «30 (treinta) días corridos en virtud de lo dispuesto en el punto 7.1.1.2 | 5%»)
- Preguntas EV2 que citan O o algún d: ninguna

### V10 — `ext::3.18.3.3` → {ext::7.1.1.4, ext::7.1.1.5}

- Texto Ordenado de O: `ext`
- O = `ext::3.18.3.3` — 33 palabras
  - fragmento E0 `ext::3.18.3.3` (punto_terminal; campo `texto`):

````text
3.18.3.3. 15% (quince por ciento) cuando corresponda a bienes que tienen asignado
un plazo de 180 (ciento ochenta) o más días corridos en virtud de lo
dispuesto en los puntos 7.1.1.4. y 7.1.1.5.
````

- d = `ext::7.1.1.4` — 12 palabras — mismo Texto Ordenado que O
  - fragmento E0 `ext::7.1.1.4` (punto_terminal; campo `texto`):

````text
7.1.1.4. 180 (ciento ochenta) días corridos para el resto de los bienes.
````

  - aristas de remisión con provenance O y destino d: 2
    - [Restriccion] «Coeficiente 15% para bienes con plazo 180 días» → [Obligacion] «Plazo 180 días para resto de bienes» (evidencia «henta) o más días corridos en virtud de lo dispuesto en los puntos 7.1.1.4. y 7.1.1.5. | 15%»)
    - [Restriccion] «Coeficiente 15% para bienes con plazo 180 días» → [Operacion] «Ingreso y liquidación de divisas» (evidencia «henta) o más días corridos en virtud de lo dispuesto en los puntos 7.1.1.4. y 7.1.1.5. | 15%»)
- d = `ext::7.1.1.5` — 27 palabras — mismo Texto Ordenado que O
  - fragmento E0 `ext::7.1.1.5` (punto_terminal; campo `texto`):

````text
7.1.1.5. 365 (trescientos sesenta y cinco) días corridos para las operaciones que se
concreten en el marco del régimen “EXPORTA SIMPLE”,
independientemente del tipo de bien exportado.
````

  - aristas de remisión con provenance O y destino d: 2
    - [Restriccion] «Coeficiente 15% para bienes con plazo 180 días» → [Operacion] «Cobro exportación régimen EXPORTA SIMPLE» (evidencia «henta) o más días corridos en virtud de lo dispuesto en los puntos 7.1.1.4. y 7.1.1.5. | 15%»)
    - [Restriccion] «Coeficiente 15% para bienes con plazo 180 días» → [Restriccion] «Plazo 365 días cobros EXPORTA SIMPLE» (evidencia «henta) o más días corridos en virtud de lo dispuesto en los puntos 7.1.1.4. y 7.1.1.5. | 15%»)
- Preguntas EV2 que citan O o algún d: ninguna

### V11 — `ext::7.11.1.4` → {ext::7.11.1.2, ext::7.11.1.3}

- Texto Ordenado de O: `ext`
- O = `ext::7.11.1.4` — 63 palabras
  - fragmento E0 `ext::7.11.1.4` (punto_terminal; campo `texto`):

````text
7.11.1.4. Préstamos financieros otorgados por los acreedores referidos en los puntos
7.11.1.2. y 7.11.1.3. que son liquidados en el mercado de cambios y que
simultáneamente fueron utilizados para concretar pagos anticipados, a la
vista y/o diferidos de importaciones de bienes al proveedor del exterior y/o
al proveedor de servicios de fletes de importaciones de bienes no incluidos
en su condición de compra pactada.
````

- d = `ext::7.11.1.2` — 96 palabras — mismo Texto Ordenado que O
  - fragmento E0 `ext::7.11.1.2` (punto_terminal; campo `texto`):

````text
7.11.1.2. Financiaciones comerciales por la importación de bienes donde los
desembolsos en divisas se aplicaron, neto de gastos, directa e
íntegramente a pagos anticipados, a la vista y/o diferidos al proveedor del
exterior y/o a pagos en forma directa al proveedor de servicios de fletes de
importaciones de bienes no incluidos en su condición de compra pactada,
que hayan sido otorgados por:
i) una entidad financiera del exterior o agencia oficial de crédito a la
exportación del exterior.
ii) una entidad financiera local a partir de una línea de crédito de una
entidad financiera del exterior.
````

  - aristas de remisión con provenance O y destino d: 4
    - [Obligacion] «Aplicación de divisas de cobros de exportación — préstamos financieros» → [Operacion] «Financiaciones comerciales — importación de bienes» (evidencia «préstamos financieros otorgados por acreedores referidos en puntos 7.11.1.2 y 7.11.1.3, liquidados en merc»)
    - [Obligacion] «Aplicación de divisas de cobros de exportación — préstamos financieros» → [Restriccion] «Otorgamiento por entidad financiera del exterior o agencia oficial» (evidencia «préstamos financieros otorgados por acreedores referidos en puntos 7.11.1.2 y 7.11.1.3, liquidados en merc»)
    - [Obligacion] «Aplicación de divisas de cobros de exportación — préstamos financieros» → [Restriccion] «Otorgamiento por entidad financiera local con línea del exterior» (evidencia «préstamos financieros otorgados por acreedores referidos en puntos 7.11.1.2 y 7.11.1.3, liquidados en merc»)
    - [Obligacion] «Aplicación de divisas de cobros de exportación — préstamos financieros» → [Restriccion] «Desembolsos netos aplicados a pagos anticipados/a la vista/diferidos» (evidencia «préstamos financieros otorgados por acreedores referidos en puntos 7.11.1.2 y 7.11.1.3, liquidados en merc»)
- d = `ext::7.11.1.3` — 61 palabras — mismo Texto Ordenado que O
  - fragmento E0 `ext::7.11.1.3` (punto_terminal; campo `texto`):

````text
7.11.1.3. Préstamos financieros otorgados por contrapartes vinculadas al cliente en
los cuales los desembolsos en divisas se aplicaron directa e íntegramente
a pagos anticipados, a la vista y/o diferidos de importaciones de bienes al
proveedor del exterior y/o a pagos en forma directa al proveedor de
servicios de fletes de importaciones de bienes no incluidos en su condición
de compra pactada.
````

  - aristas de remisión con provenance O y destino d: 2
    - [Obligacion] «Aplicación de divisas de cobros de exportación — préstamos financieros» → [Operacion] «Préstamos financieros de contrapartes vinculadas» (evidencia «préstamos financieros otorgados por acreedores referidos en puntos 7.11.1.2 y 7.11.1.3, liquidados en merc»)
    - [Obligacion] «Aplicación de divisas de cobros de exportación — préstamos financieros» → [Restriccion] «Desembolsos — aplicación directa e íntegra a pagos» (evidencia «préstamos financieros otorgados por acreedores referidos en puntos 7.11.1.2 y 7.11.1.3, liquidados en merc»)
- Preguntas EV2 que citan O o algún d: ninguna

### V12 — `ext::8.5.13.4` → {ext::6.6}

- Texto Ordenado de O: `ext`
- O = `ext::8.5.13.4` — 23 palabras
  - fragmento E0 `ext::8.5.13.4` (punto_terminal; campo `texto`):

````text
8.5.13.4. el exportador y el importador no estén vinculados en forma directa o
indirecta de acuerdo con lo previsto en el punto 6.6.
````

- d = `ext::6.6` — 44 palabras — mismo Texto Ordenado que O
  - fragmento E0 `ext::6.6` (punto_terminal; campo `texto`):

````text
6.6. Operaciones con contrapartes vinculadas.
Se considerarán operaciones con contrapartes vinculadas a aquellas en las que participan un
residente y una contraparte que mantienen entre ellos los tipos de relaciones descriptos en el
punto 1.2.2. de las normas “Grandes exposiciones al riesgo de crédito”.
````

  - aristas de remisión con provenance O y destino d: 1
    - [Restriccion] «No vinculación directa o indirecta — exportador e importador» → [Operacion] «Operaciones con contrapartes vinculadas» (evidencia «forma directa o indirecta de acuerdo con lo previsto en el punto 6.6»)
- Preguntas EV2 que citan O o algún d: ninguna

### V13 — `pro::3.2.3.8` → {pro::3.1.5}

- Texto Ordenado de O: `pro`
- O = `pro::3.2.3.8` — 21 palabras
  - fragmento E0 `pro::3.2.3.8` (punto_terminal; campo `texto`):

````text
3.2.3.8. El Registro de Denuncias ante las Instancias Judiciales y/o Administrativas de
Defensa del Consumidor (RDJA) establecido en el punto 3.1.5.
````

- d = `pro::3.1.5` — 58 palabras — mismo Texto Ordenado que O
  - fragmento E0 `pro::3.1.5` (punto_terminal; campo `texto`):

````text
3.1.5. Registro de Denuncias ante las Instancias Judiciales y/o Administrativas de Defensa del
Consumidor (RDJA).
En este registro se asentarán todas las intervenciones originadas en denuncias efec-
tuadas ante instancias judiciales y/o administrativas de defensa del consumidor, identi-
ficando al usuario afectado y especificando el importe involucrado, la causal generado-
ra del evento, los productos y casas involucradas.
````

  - aristas de remisión con provenance O y destino d: 2
    - [Obligacion] «Registro denuncias instancias judiciales administrativas» → [Obligacion] «Registro de denuncias judiciales y administrativas» (evidencia «trativas de Defensa del Consumidor (RDJA) establecido en el punto 3.1.5.»)
    - [Obligacion] «Registro denuncias instancias judiciales administrativas» → [Operacion] «Denuncias ante instancias judiciales y administrativas» (evidencia «trativas de Defensa del Consumidor (RDJA) establecido en el punto 3.1.5.»)
- Preguntas EV2 que citan O o algún d: ninguna

### V14 — `ric::10.1.2` → {ric::1.2}

- Texto Ordenado de O: `ric`
- O = `ric::10.1.2` — 43 palabras
  - fragmento E0 `ric::10.1.2` (punto_terminal; campo `texto`):

````text
10.1.2. Ratio de apalancamiento
Surgirá de aplicar la expresión prevista en el punto 1.2. de las citadas normas:
Ratio de apalancamiento = [Medida del capital / Medida de la exposición] * 100 =
[PNb / ∑ Códigos (45110000 a 45140000)] * 100
(CN1)
````

- d = `ric::1.2` — 87 palabras — mismo Texto Ordenado que O
  - fragmento E0 `ric::1.2` (punto_terminal; campo `texto`):

````text
1.2. Los importes se registrarán en miles de pesos, sin decimales.
A los fines del redondeo de las magnitudes se incrementarán los valores en una unidad
cuando el primer dígito de las fracciones sea igual o mayor que 5, desechando estas últimas
si resultan inferiores.
Los importes en moneda extranjera se convertirán a pesos utilizando el tipo de cambio de re-
ferencia publicado por el BCRA para el dólar estadounidense, previa aplicación del tipo de
pase correspondiente para las otras monedas comunicado por la Mesa de Operaciones.
````

  - aristas de remisión con provenance O y destino d: 3
    - [Obligacion] «Aplicar expresión Ratio apalancamiento punto 1.2» → [Obligacion] «Redondeo de magnitudes según dígito fraccional» (evidencia «Aplicar expresión Ratio apalancamiento punto 1.2 | Surgirá de aplica»)
    - [Obligacion] «Aplicar expresión Ratio apalancamiento punto 1.2» → [Obligacion] «Conversión importes moneda extranjera a pesos» (evidencia «Aplicar expresión Ratio apalancamiento punto 1.2 | Surgirá de aplica»)
    - [Obligacion] «Aplicar expresión Ratio apalancamiento punto 1.2» → [Obligacion] «Registrar importes en miles de pesos sin decimales» (evidencia «Aplicar expresión Ratio apalancamiento punto 1.2 | Surgirá de aplica»)
- Preguntas EV2 que citan O o algún d: ninguna

---

## Protección de usuarios (pro): todos los pares que pasan el criterio 1 (17)

| O | D | palabras O | palabras de cada d | tipo de fragmento de O | tipo de fragmento de cada d | primer criterio que no cumple |
|---|---|---|---|---|---|---|
| `pro::2.3.1.1` | `pro::2.3.2.1`, `pro::2.3.2.2` | 763 | 299, 340 | punto_terminal | punto_terminal; punto_terminal | criterio 4 |
| `pro::2.3.1.2` | `pro::2.4` | 181 | 181 | punto_terminal | mini_chunk, rol_bloque intro / mini_chunk, rol_bloque cierre | criterio 4 |
| `pro::2.3.1.4` | `pro::2.3.1.1`, `pro::2.3.1.2`, `pro::2.3.4` | 478 | 763, 181, 636 | punto_terminal | punto_terminal; punto_terminal; punto_terminal | criterio 4 |
| `pro::2.3.2.2` | `pro::2.3.2.1`, `pro::2.3.12` | 340 | 299, 22 | punto_terminal | punto_terminal; mini_chunk, rol_bloque intro | criterio 4 |
| `pro::2.3.4` | `pro::2.3.2.1` | 636 | 299 | punto_terminal | punto_terminal | criterio 4 |
| `pro::2.3.5.1` | `pro::3.1.6` | 720 | 184 | punto_terminal | punto_terminal | criterio 4 |
| `pro::2.6` | `pro::2.4` | 161 | 181 | punto_terminal | mini_chunk, rol_bloque intro / mini_chunk, rol_bloque cierre | criterio 4 |
| `pro::2.7.1` | `pro::2.3.1.1` | 24 | 763 | punto_terminal | punto_terminal | criterio 4 |
| `pro::3.1.1` | `pro::3.1.2` | 223 | 135 | mini_chunk, rol_bloque intro / mini_chunk, rol_bloque cierre | punto_terminal | criterio 4 |
| `pro::3.1.1.6` | `pro::2.3.5.1` | 58 | 720 | punto_terminal | punto_terminal | criterio 4 |
| `pro::3.1.1.7` | `pro::3.1.3`, `pro::3.1.4`, `pro::3.1.5` | 73 | 365, 37, 58 | punto_terminal | punto_terminal; punto_terminal; punto_terminal | criterio 4 |
| `pro::3.1.1.8` | `pro::3.2.1.1` | 142 | 593 | punto_terminal | punto_terminal | criterio 4 |
| `pro::3.2.1.1` | `pro::3.1.1.6` | 593 | 58 | punto_terminal | punto_terminal | criterio 4 |
| `pro::3.2.1.2` | `pro::3.2.1.1` | 52 | 593 | punto_terminal | punto_terminal | criterio 4 |
| `pro::3.2.3.4` | `pro::3.1.1.8` | 58 | 142 | punto_terminal | punto_terminal | criterio 4 |
| `pro::3.2.3.8` | `pro::3.1.5` | 21 | 58 | punto_terminal | punto_terminal | pasa |
| `pro::4.3` | `pro::4.2.1` | 89 | 47 | punto_terminal | mini_chunk, rol_bloque intro | criterio 4 |

- Conteo por primer criterio no cumplido: 2: 0, 3: 0, 4: 16, 5: 0, 6: 0, pasa: 1

---

## REFERENCIA: `ext::3.17.1.4` con la definición de esta vuelta

- D(O) = {ext::3.4.1, ext::3.4.2, ext::3.4.3}
  - criterio 1: cumple
  - criterio 2: cumple
  - criterio 3: cumple
  - criterio 4: cumple
  - criterio 5: cumple
  - criterio 6: cumple
- Resultado del embudo para este O: pasa

- Texto Ordenado de O: `ext`
- O = `ext::3.17.1.4` — 25 palabras
  - fragmento E0 `ext::3.17.1.4` (punto_terminal; campo `texto`):

````text
3.17.1.4. Pagos de utilidades y dividendos a accionistas no residentes en la medida
que se verifiquen los requisitos previstos en los puntos 3.4.1. a 3.4.3.
````

- d = `ext::3.4.1` — 11 palabras — mismo Texto Ordenado que O
  - fragmento E0 `ext::3.4.1` (punto_terminal; campo `texto`):

````text
3.4.1. Las utilidades y dividendos correspondan a balances cerrados y auditados.
````

  - aristas de remisión con provenance O y destino d: 1
    - [Restriccion] «Requisitos puntos 3.4.1 a 3.4.3 — utilidades dividendos» → [Obligacion] «Balances cerrados y auditados» (evidencia «Requisitos puntos 3.4.1 a 3.4.3 — utilidades divide»)
- d = `ext::3.4.2` — 71 palabras — mismo Texto Ordenado que O
  - fragmento E0 `ext::3.4.2` (punto_terminal; campo `texto`):

````text
3.4.2. El monto total abonado por este concepto a accionistas no residentes, incluido el pago
cuyo curso se está solicitando, no supere el monto en moneda local que les
corresponda según la distribución determinada por la asamblea de accionistas.
La entidad deberá contar con una declaración jurada firmada por el representante legal
de la empresa residente o un apoderado con facultades suficientes para asumir este
compromiso en nombre de la empresa.
````

  - aristas de remisión con provenance O y destino d: 3
    - [Restriccion] «Requisitos puntos 3.4.1 a 3.4.3 — utilidades dividendos» → [Obligacion] «Declaración jurada representante legal» (evidencia «Requisitos puntos 3.4.1 a 3.4.3 — utilidades divide»)
    - [Restriccion] «Requisitos puntos 3.4.1 a 3.4.3 — utilidades dividendos» → [Operacion] «Giro divisas utilidades dividendos exterior» (evidencia «Requisitos puntos 3.4.1 a 3.4.3 — utilidades divide»)
    - [Restriccion] «Requisitos puntos 3.4.1 a 3.4.3 — utilidades dividendos» → [Restriccion] «Monto total no supere distribución asamblea» (evidencia «Requisitos puntos 3.4.1 a 3.4.3 — utilidades divide»)
- d = `ext::3.4.3` — 34 palabras — mismo Texto Ordenado que O
  - fragmento E0 `ext::3.4.3` (punto_terminal; campo `texto`):

````text
3.4.3. La entidad deberá verificar que el cliente haya dado cumplimiento en caso de
corresponder, a la declaración de la última presentación vencida del “Relevamiento de
activos y pasivos externos” por las operaciones involucradas.
````

  - aristas de remisión con provenance O y destino d: 2
    - [Restriccion] «Requisitos puntos 3.4.1 a 3.4.3 — utilidades dividendos» → [Obligacion] «Verificación de cumplimiento declaración de activos y pasivos externos» (evidencia «Requisitos puntos 3.4.1 a 3.4.3 — utilidades divide»)
    - [Restriccion] «Requisitos puntos 3.4.1 a 3.4.3 — utilidades dividendos» → [Operacion] «Giro de utilidades y dividendos al exterior» (evidencia «Requisitos puntos 3.4.1 a 3.4.3 — utilidades divide»)
- Preguntas EV2 que citan O o algún d: ninguna

### `ext::3.18.1.2` como O

- No aparece como O: ninguna arista de remisión tiene provenance `ext::3.18.1.2`.
- Aristas de remisión cuyo campo `provenances` incluye `ext::3.18.1.2`: 6; su campo `provenance` es: ['ext::3.17.1.4']; sus destinos: ['ext::3.4.1', 'ext::3.4.2', 'ext::3.4.3']
  - nodo origen [Restriccion] «Requisitos puntos 3.4.1 a 3.4.3 — utilidades dividendos» con procedencias `ext::3.17.1.4`, `ext::3.18.1.2` → destino `ext::3.4.2`
  - nodo origen [Restriccion] «Requisitos puntos 3.4.1 a 3.4.3 — utilidades dividendos» con procedencias `ext::3.17.1.4`, `ext::3.18.1.2` → destino `ext::3.4.3`
  - nodo origen [Restriccion] «Requisitos puntos 3.4.1 a 3.4.3 — utilidades dividendos» con procedencias `ext::3.17.1.4`, `ext::3.18.1.2` → destino `ext::3.4.1`
  - nodo origen [Restriccion] «Requisitos puntos 3.4.1 a 3.4.3 — utilidades dividendos» con procedencias `ext::3.17.1.4`, `ext::3.18.1.2` → destino `ext::3.4.3`
  - nodo origen [Restriccion] «Requisitos puntos 3.4.1 a 3.4.3 — utilidades dividendos» con procedencias `ext::3.17.1.4`, `ext::3.18.1.2` → destino `ext::3.4.2`
  - nodo origen [Restriccion] «Requisitos puntos 3.4.1 a 3.4.3 — utilidades dividendos» con procedencias `ext::3.17.1.4`, `ext::3.18.1.2` → destino `ext::3.4.2`
- Texto propio de `ext::3.18.1.2` en E0:
  - fragmento E0 `ext::3.18.1.2` (punto_terminal; campo `texto`):

````text
3.18.1.2. Pagos de utilidades y dividendos a accionistas no residentes en la medida
que se verifiquen los requisitos previstos en los puntos 3.4.1. a 3.4.3.
````


