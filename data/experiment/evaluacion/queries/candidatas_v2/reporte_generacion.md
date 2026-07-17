# Reporte de generación — preguntas de evaluación QA sobre normativa BCRA

Corpus: 5 Textos Ordenados (PDF) en la carpeta `SUBSET`. Todo el contenido de este reporte y de los archivos JSON deriva exclusivamente de esos documentos.

## Fase 0 — Preparación

### Formatos verificados (`file`)

Los 5 archivos son `PDF document, version 1.7 (zip deflate encoded)`:

```
/Users/agustinavidelarivero/SUBSET/TO_capitales_minimos_actual.pdf:                         PDF document, version 1.7 (zip deflate encoded)
/Users/agustinavidelarivero/SUBSET/TO_clasificacion_deudores_actual.pdf:                    PDF document, version 1.7 (zip deflate encoded)
/Users/agustinavidelarivero/SUBSET/TO_exterior_cambios_actual.pdf:                          PDF document, version 1.7 (zip deflate encoded)
/Users/agustinavidelarivero/SUBSET/TO_proteccion_usuarios_servicios_financieros_actual.pdf: PDF document, version 1.7 (zip deflate encoded)
/Users/agustinavidelarivero/SUBSET/TO_regimen_informativo_contable_mensual_actual.pdf:      PDF document, version 1.7 (zip deflate encoded)
```

### Extracción de texto (pdfplumber 0.11.10, Python 3.12)

| Documento | Páginas | Caracteres |
|---|---:|---:|
| TO_capitales_minimos_actual.pdf | 204 | 480,560 |
| TO_clasificacion_deudores_actual.pdf | 60 | 134,782 |
| TO_exterior_cambios_actual.pdf | 201 | 507,668 |
| TO_proteccion_usuarios_servicios_financieros_actual.pdf | 40 | 93,802 |
| TO_regimen_informativo_contable_mensual_actual.pdf | 59 | 110,471 |

### Inventario de secciones (`inventario_secciones.json`)

Parseado de los encabezados «Sección N.» / «N.M.» del cuerpo y del índice inicial (primera aparición de cada encabezado; títulos multilínea reconstruidos).

| Documento | Secciones | Puntos N.M. |
|---|---:|---:|
| TO_capitales_minimos_actual.pdf | 12 | 63 |
| TO_clasificacion_deudores_actual.pdf | 10 | 35 |
| TO_exterior_cambios_actual.pdf | 15 | 124 |
| TO_proteccion_usuarios_servicios_financieros_actual.pdf | 5 | 16 |
| TO_regimen_informativo_contable_mensual_actual.pdf | 12 | 28 |

## Fase 1 — Muestreo mecánico (semilla 20260718)

Sorteo de 4 secciones por documento con `random.Random(20260718)` sobre el inventario ordenado (documentos por nombre de archivo; secciones por número).

### Código
```python
import json, random

inv = json.load(open('/Users/agustinavidelarivero/SUBSET/inventario_secciones.json'))
rng = random.Random(20260718)
sorteo = {}
for doc in sorted(inv):  # inventario ORDENADO por nombre de documento
    secs = sorted(s["seccion"] for s in inv[doc]["secciones"])  # secciones ordenadas
    elegidas = sorted(rng.sample(secs, 4))
    sorteo[doc] = elegidas
    titulos = {s["seccion"]: s["titulo"] for s in inv[doc]["secciones"]}
    print(doc)
    for n in elegidas:
        print(f"  Sección {n}. {titulos[n]}")
json.dump(sorteo, open('/private/tmp/claude-501/-Users-agustinavidelarivero-SUBSET/1981adc0-31f2-45e6-b158-42495fece7e4/scratchpad/sorteo.json', 'w'), indent=2)
```
### Output
```
TO_capitales_minimos_actual.pdf
  Sección 1. Capital mínimo.
  Sección 5. Cobertura del riesgo de crédito.
  Sección 6. Capital mínimo por riesgo de mercado.
  Sección 7. Capital mínimo por riesgo operacional.
TO_clasificacion_deudores_actual.pdf
  Sección 1. Deudores comprendidos.
  Sección 2. Financiaciones comprendidas.
  Sección 6. Clasificación de los deudores de la cartera comercial.
  Sección 10. Otros obligados a la observancia de las normas sobre clasificación de deudores.
TO_exterior_cambios_actual.pdf
  Sección 3. Disposiciones específicas para los egresos por el mercado de cambios.
  Sección 8. Seguimiento de las negociaciones de divisas por exportaciones de bienes (SECOEXPO).
  Sección 9. Seguimiento de anticipos y otras financiaciones de exportación de bienes.
  Sección 15. Disposiciones legales que determinan la estructura general del mercado de cambios.
TO_proteccion_usuarios_servicios_financieros_actual.pdf
  Sección 1. Disposiciones generales.
  Sección 2. Derechos básicos de los usuarios de servicios financieros.
  Sección 4. Actuación del Banco Central de la República Argentina.
  Sección 5. Sanciones.
TO_regimen_informativo_contable_mensual_actual.pdf
  Sección 2. Entidades comprendidas
  Sección 7. Facilidades otorgadas por el B.C.R.A.
  Sección 8. Totales de control
  Sección 11. Información complementaria vinculada al cálculo del riesgo de tasa de interés en cartera de inversión.
```

Las 15 preguntas versan únicamente sobre contenido de estas 20 secciones; en las multi-sección, ambas puntas caen en secciones sorteadas.

## Fase 2 — Las 15 preguntas candidatas

Distribución: 7 `factual_directa`, 5 `multi_norma`, 3 `cadena_normativa`. En las citas, el separador `[…]` une fragmentos verbatim de puntos/documentos distintos (cada fragmento se verifica por separado). Los guiones intercalados (p. ej. «fi- nancieros») son cortes de línea del PDF conservados verbatim.

### CQN-001 — `factual_directa`

**Pregunta:** ¿Qué monto mensual máximo puede comprar una persona humana residente, sin conformidad previa del BCRA, para la formación de activos externos bajo modalidades distintas de billetes y depósitos, la remisión de ayuda familiar o la operatoria con derivados?

**TOs fuente:** TO_exterior_cambios_actual.pdf

**Ground truth:** TO_exterior_cambios_actual.pdf Punto 3.9

**Sección sorteada de origen:** TO_exterior_cambios_actual.pdf Sección 3

**Cita textual:**
> para la formación de activos externos (códigos de conceptos A01, A02, A03, A04, A06, A08, A14 y A24), la remisión de ayuda familiar y para la operatoria con derivados (código de con- cepto A05) en la medida que no encuadre en el punto 3.12.1., sin la conformidad previa del BCRA, en la medida que se cumplan la totalidad de los siguientes requisitos: 3.9.1. El cliente no supere, en el mes calendario en el conjunto de las entidades y por el conjunto de los conceptos señalados, el equivalente a USD 200 (dólares estadounidenses doscientos).

**Respuesta breve:** El límite es el equivalente a USD 200 por mes calendario, computado en el conjunto de las entidades y por el conjunto de los conceptos señalados. Si la operación se hace con efectivo, el monto no puede superar el equivalente a USD 100 mensuales.

### CQN-002 — `factual_directa`

**Pregunta:** ¿Con cuánta anticipación debe una entidad financiera preavisar a la Superintendencia si desea cambiar el método que emplea para la técnica de activos admitidos como garantía en la cobertura del riesgo de crédito?

**TOs fuente:** TO_capitales_minimos_actual.pdf

**Ground truth:** TO_capitales_minimos_actual.pdf Punto 5.1

**Sección sorteada de origen:** TO_capitales_minimos_actual.pdf Sección 5

**Cita textual:**
> Las entidades deberán optar por un único método para la aplicación de la técnica de ac- tivos admitidos como garantía de las operaciones registradas en la cartera de inversión y para el cálculo de la exposición a las SFT, y sólo podrán cambiar el método empleado con un preaviso de 6 meses a la SEFYC.

**Respuesta breve:** Debe preavisar a la SEFyC con 6 meses de anticipación. Las entidades deben optar por un único método (simple o integral) para esa técnica y sólo pueden cambiarlo con ese preaviso.

### CQN-003 — `factual_directa`

**Pregunta:** ¿En qué categoría debe clasificarse a los firmantes de instrumentos cedidos a una entidad financiera sin responsabilidad para el cedente cuando no se efectúa su evaluación como sujetos de crédito?

**TOs fuente:** TO_clasificacion_deudores_actual.pdf

**Ground truth:** TO_clasificacion_deudores_actual.pdf Punto 1.2

**Sección sorteada de origen:** TO_clasificacion_deudores_actual.pdf Sección 1

**Cita textual:**
> Los créditos cedidos a favor de la entidad sin responsabilidad para el cedente -unidad económica receptora de los fondos- se imputarán al firmante, librador, deudor, codeudor o aceptante de los respectivos instrumentos, constituidos consecuentemente en principa- les y directos pagadores, realizando respecto de ellos su evaluación como sujetos de crédito con la pertinente apertura del legajo. En caso de no efectuarse la evaluación, cualquiera sea el motivo, estos clientes se clasificarán en categoría “irrecuperable”.

**Respuesta breve:** Deben clasificarse en la categoría “irrecuperable”. Los créditos cedidos sin responsabilidad para el cedente se imputan al firmante, librador, deudor, codeudor o aceptante, y si no se realiza su evaluación como sujetos de crédito —cualquiera sea el motivo— corresponde esa categoría.

### CQN-004 — `factual_directa`

**Pregunta:** ¿Cuántos escenarios de variación del tipo de cambio deben contemplarse, como mínimo, al analizar la capacidad de pago de un cliente de la cartera comercial con financiaciones en moneda extranjera?

**TOs fuente:** TO_clasificacion_deudores_actual.pdf

**Ground truth:** TO_clasificacion_deudores_actual.pdf Punto 6.2

**Sección sorteada de origen:** TO_clasificacion_deudores_actual.pdf Sección 6

**Cita textual:**
> Respecto de clientes por financiaciones en moneda extranjera, cualquiera sea la fuente de re- cursos que se aplique, deberá ponerse énfasis en analizar si el cliente cuenta con una capaci- dad de pago suficiente que permita cubrir los vencimientos aún ante variaciones significativas en el tipo de cambio. A tal fin, deberán tenerse en cuenta al menos dos escenarios en los que se contemplen variaciones significativas en el tipo de cambio de diferentes magnitudes en el término de hasta un año.

**Respuesta breve:** Deben tenerse en cuenta al menos dos escenarios que contemplen variaciones significativas del tipo de cambio de diferentes magnitudes, en el término de hasta un año, para verificar que la capacidad de pago cubra los vencimientos aun ante esas variaciones.

### CQN-005 — `factual_directa`

**Pregunta:** ¿A partir de qué monto adeudado se exige una certificación de auditor externo, además de la declaración jurada del exportador, para emitir certificaciones de aplicación de divisas por anticipos y prefinanciaciones del exterior pendientes al 31/08/19 que fueron liquidados en el mercado de cambios?

**TOs fuente:** TO_exterior_cambios_actual.pdf

**Ground truth:** TO_exterior_cambios_actual.pdf Punto 9.3

**Sección sorteada de origen:** TO_exterior_cambios_actual.pdf Sección 9

**Cita textual:**
> la entidad cuente con una declaración jurada del exportador detallando el monto pendiente de la deuda al 31/08/19 y las cancelaciones realizadas. En el caso de que el monto adeudado fuera superior a USD 25.000 (dólares estadounidenses veinticinco mil), la entidad deberá contar adicionalmente con una certificación de auditor externo en la cual se deje constancia que lo declarado por el exportador resulta consistente con la información que surge de la revisión de los registros contables, extracontables y toda otra documentación adicional aportada.

**Respuesta breve:** Cuando el monto adeudado supera USD 25.000, la entidad debe contar además con una certificación de auditor externo que deje constancia de que lo declarado por el exportador es consistente con los registros contables, extracontables y demás documentación aportada.

### CQN-006 — `factual_directa`

**Pregunta:** ¿En qué plazo debe un sujeto obligado reintegrar al usuario de servicios financieros los importes que le cobró indebidamente?

**TOs fuente:** TO_proteccion_usuarios_servicios_financieros_actual.pdf

**Ground truth:** TO_proteccion_usuarios_servicios_financieros_actual.pdf Punto 2.3

**Sección sorteada de origen:** TO_proteccion_usuarios_servicios_financieros_actual.pdf Sección 2

**Cita textual:**
> deberá serle reintegrado dentro de: - los diez (10) días hábiles siguientes al momento de la presentación del re- clamo ante el sujeto obligado, de conformidad con las previsiones del punto 3.1.6.; o - los cinco (5) días hábiles siguientes al momento de constatarse tal circuns- tancia por el sujeto obligado o por la fiscalización que realice la SEFYC.

**Respuesta breve:** El reintegro debe hacerse dentro de los diez (10) días hábiles siguientes a la presentación del reclamo ante el sujeto obligado, o dentro de los cinco (5) días hábiles siguientes al momento en que la circunstancia sea constatada por el propio sujeto obligado o por la fiscalización de la SEFyC.

### CQN-007 — `factual_directa`

**Pregunta:** ¿En qué circunstancia se identifica a una entidad financiera como “entidad atípica” en relación con el riesgo de tasa de interés en la cartera de inversión?

**TOs fuente:** TO_regimen_informativo_contable_mensual_actual.pdf

**Ground truth:** TO_regimen_informativo_contable_mensual_actual.pdf Punto 8.1

**Sección sorteada de origen:** TO_regimen_informativo_contable_mensual_actual.pdf Sección 8

**Cita textual:**
> Cuando esta medida supere el 15 % del nivel de capital 1, se identificará a la entidad como una “entidad atípica” y la SEFyC podrá exigirle la adopción de medidas específicas

**Respuesta breve:** Cuando la medida de riesgo EVE estandarizada (la máxima pérdida registrada entre los escenarios) supera el 15 % del nivel de capital 1, la entidad se identifica como “entidad atípica” y la SEFyC puede exigirle la adopción de medidas específicas.

### CQN-008 — `multi_norma`

**Pregunta:** ¿Las empresas no financieras emisoras de tarjetas de crédito están alcanzadas por las normas de protección de los usuarios de servicios financieros y, a la vez, con qué criterio deben clasificar a sus deudores según las normas sobre clasificación de deudores?

**TOs fuente:** TO_proteccion_usuarios_servicios_financieros_actual.pdf, TO_clasificacion_deudores_actual.pdf

**Ground truth:** TO_proteccion_usuarios_servicios_financieros_actual.pdf Punto 1.1; TO_clasificacion_deudores_actual.pdf Punto 10.1

**Sección sorteada de origen:** TO_proteccion_usuarios_servicios_financieros_actual.pdf Sección 1; TO_clasificacion_deudores_actual.pdf Sección 10

**Cita textual:**
> 1.1.2. Sujetos obligados. 1.1.2.1. Entidades financieras. […] 1.1.2.4. Empresas no financieras emisoras de tarjetas de crédito y/o compra. […] Las empresas no financieras emisoras de tarjetas de crédito y/o compra y los otros proveedo- res no financieros de crédito alcanzados por las normas sobre “Proveedores no financieros de crédito”, deberán clasificar a los respectivos deudores en función de su mora, según los crite- rios aplicables para la cartera de “consumo o vivienda” y por aplicación de las disposiciones previstas en el punto 7.3. (recategorización obligatoria).

**Respuesta breve:** Sí: son sujetos obligados de las normas de protección de usuarios de servicios financieros. Además, según las normas de clasificación de deudores deben clasificar a sus deudores en función de su mora, con los criterios aplicables a la cartera de consumo o vivienda y la recategorización obligatoria correspondiente.

### CQN-009 — `multi_norma`

**Pregunta:** ¿Qué importe debe consignar un banco —que no sea caja de crédito cooperativa— en el total de control correspondiente al capital mínimo básico del régimen informativo sobre exigencia e integración de capitales mínimos?

**TOs fuente:** TO_regimen_informativo_contable_mensual_actual.pdf, TO_capitales_minimos_actual.pdf

**Ground truth:** TO_regimen_informativo_contable_mensual_actual.pdf Punto 8.1; TO_capitales_minimos_actual.pdf Punto 1.2

**Sección sorteada de origen:** TO_regimen_informativo_contable_mensual_actual.pdf Sección 8; TO_capitales_minimos_actual.pdf Sección 1

**Cita textual:**
> 8.1.3. Código 70700000. Capital Mínimo Básico –punto 1.2. de las normas sobre “Capitales mínimos de las entidades financieras”–. […] Según la clase de entidad, serán las siguientes exigencias básicas: Restantes entidades Bancos (salvo Cajas de Crédito Cooperativas) -En millones de pesos- 5.000 2.500

**Respuesta breve:** Debe consignar $ 5.000 millones. El total de control del capital mínimo básico remite a la exigencia básica de las normas sobre capitales mínimos, que para los bancos es de $ 5.000 millones (y de $ 2.500 millones para las restantes entidades, salvo cajas de crédito cooperativas).

*Nota sobre la cita:* la extracción lineal del PDF desordena el encabezado de la tabla de exigencias básicas («Restantes entidades / Bancos»). La correspondencia de columnas se verificó con `pdfplumber.extract_tables()` sobre la página 4 del TO: la tabla real es `['Bancos', 'Restantes entidades (salvo Cajas de Crédito Cooperativas)']` con valores `['5.000', '2.500']`, es decir, Bancos = 5.000 y Restantes entidades = 2.500 (en millones de pesos).

### CQN-010 — `multi_norma`

**Pregunta:** Cuando las divisas del cobro de una exportación se aplican a cancelar una prefinanciación, ¿qué documento necesita la entidad encargada del seguimiento del permiso de embarque para registrar esa imputación y qué entidad es la única habilitada para emitirlo?

**TOs fuente:** TO_exterior_cambios_actual.pdf

**Ground truth:** TO_exterior_cambios_actual.pdf Punto 8.4; TO_exterior_cambios_actual.pdf Punto 9.2

**Sección sorteada de origen:** TO_exterior_cambios_actual.pdf Sección 8; TO_exterior_cambios_actual.pdf Sección 9

**Cita textual:**
> 8.4.3.2. Aplicación de las divisas provenientes del cobro de la exportación de bienes admitidos por esta normativa. La entidad deberá contar con una certificación de aplicación emitida por la encargada del seguimiento de la operación a cuya cancelación se aplicaron las divisas. […] Esta entidad será la única responsable de emitir los certificados de aplicación que habilitan que los cobros de exportaciones puedan ser imputados a los permisos correspondientes.

**Respuesta breve:** Necesita una certificación de aplicación. La única habilitada para emitirla es la entidad nominada por el exportador para el seguimiento de la operación de financiación a cuya cancelación se aplicaron las divisas.

### CQN-011 — `multi_norma`

**Pregunta:** ¿Con qué frecuencia se informa la información complementaria vinculada al riesgo de tasa de interés en la cartera de inversión y a qué caso de entidad corresponde el código de consolidación con el que se presenta en base consolidada?

**TOs fuente:** TO_regimen_informativo_contable_mensual_actual.pdf

**Ground truth:** TO_regimen_informativo_contable_mensual_actual.pdf Punto 11.1; TO_regimen_informativo_contable_mensual_actual.pdf Sección 2

**Sección sorteada de origen:** TO_regimen_informativo_contable_mensual_actual.pdf Sección 11; TO_regimen_informativo_contable_mensual_actual.pdf Sección 2

**Cita textual:**
> Los datos se informarán con frecuencia trimestral y se integrarán con los datos correspon- dientes al último mes de cada trimestre (marzo, junio, septiembre y diciembre), sobre base individual y consolidada mensual. Serán aplicables los siguientes códigos de consolidación definidos en la Sección 2.: Base individual (código de consolidación 0 o 1); Base consolidada (código de consolidación 2). […] Consolidado mensual (entidad financiera con filiales y subsidiarias significativas en el país y en el exterior) – (con el alcance definido en el punto 6.2. de las normas sobre “Su- 2 pervisión consolidada”)

**Respuesta breve:** Se informa con frecuencia trimestral, con los datos del último mes de cada trimestre (marzo, junio, septiembre y diciembre). La base consolidada usa el código de consolidación 2, que corresponde al consolidado mensual de una entidad financiera con filiales y subsidiarias significativas en el país y en el exterior.

### CQN-012 — `multi_norma`

**Pregunta:** ¿Cómo se determina la exigencia de capital mínimo que debe integrar una entidad financiera y cómo se calcula, en su primer mes de funcionamiento, el componente de esa exigencia correspondiente al riesgo operacional?

**TOs fuente:** TO_capitales_minimos_actual.pdf

**Ground truth:** TO_capitales_minimos_actual.pdf Punto 1.1; TO_capitales_minimos_actual.pdf Punto 7.4

**Sección sorteada de origen:** TO_capitales_minimos_actual.pdf Sección 1; TO_capitales_minimos_actual.pdf Sección 7

**Cita textual:**
> La exigencia de capital mínimo que las entidades financieras deberán tener integrada será equivalente al mayor valor que resulte de la comparación entre la exigencia básica y la suma de las determinadas por riesgos de crédito, de mercado –exigencia por las posiciones diarias de los activos comprendidos– y operacional. […] La exigencia mensual de capital mínimo por riesgo operacional de las entidades financieras de los grupos 1 y 2 correspondiente al primer mes será equivalente al 10% de la sumatoria de las exigencias determinadas por los riesgos de crédito y de mercado –en este caso, para las posi- ciones del último día– de ese mes.

**Respuesta breve:** La exigencia es el mayor valor entre la exigencia básica y la suma de las exigencias por riesgos de crédito, de mercado y operacional. Para una entidad nueva, la exigencia por riesgo operacional del primer mes equivale al 10 % de la sumatoria de las exigencias por riesgos de crédito y de mercado —para las posiciones del último día— de ese mes.

### CQN-013 — `cadena_normativa`

**Pregunta:** ¿Qué consecuencias sancionatorias enfrenta un sujeto obligado que incumple las normas sobre protección de los usuarios de servicios financieros?

**TOs fuente:** TO_proteccion_usuarios_servicios_financieros_actual.pdf

**Ground truth:** TO_proteccion_usuarios_servicios_financieros_actual.pdf Punto 1.2; TO_proteccion_usuarios_servicios_financieros_actual.pdf Sección 5

**Sección sorteada de origen:** TO_proteccion_usuarios_servicios_financieros_actual.pdf Sección 1; TO_proteccion_usuarios_servicios_financieros_actual.pdf Sección 5

**Cita textual:**
> El Banco Central de la República Argentina (BCRA) supervisará la actuación de los sujetos obligados, a quienes les resultarán de aplicación las disposiciones de la Sección 5. en caso de incumplimiento de estas normas. […] El sujeto obligado y quienes resulten responsables serán pasibles de la aplicación de las sanciones previstas en las normas sobre “Régimen disciplinario a cargo del Banco Central de la República Argentina (Leyes 21.526 y 25.065) y tramitación de sumarios cambiarios (Ley 19.359)”, por los in- cumplimientos que se constaten respecto de estas normas

**Respuesta breve:** El criterio general remite, en caso de incumplimiento, a la sección de sanciones: el sujeto obligado y los responsables son pasibles de las sanciones previstas en las normas sobre “Régimen disciplinario a cargo del BCRA (Leyes 21.526 y 25.065) y tramitación de sumarios cambiarios (Ley 19.359)”, incluso por incumplimientos de los manuales de procedimiento interno.

### CQN-014 — `cadena_normativa`

**Pregunta:** Si una entidad financiera del grupo 2 no registró ingreso bruto positivo en ninguno de los períodos de 12 meses de los últimos 36 meses, ¿qué exigencia de capital por riesgo operacional debe observar?

**TOs fuente:** TO_capitales_minimos_actual.pdf

**Ground truth:** TO_capitales_minimos_actual.pdf Punto 7.2; TO_capitales_minimos_actual.pdf Punto 7.3

**Sección sorteada de origen:** TO_capitales_minimos_actual.pdf Sección 7

**Cita textual:**
> Cuando n sea igual a cero (n=0), deberá observarse una exigencia equivalente al límite previsto en el punto 7.3. […] La exigencia determinada a través de la aplicación de la expresión descripta en el punto 7.2. no podrá superar: 7.3.1. El 20% en el caso de entidades del grupo A del promedio de los últimos 36 meses –anteriores al mes a que corresponda la determinación de la exigencia– de la exigencia de capital mínimo por riesgo de crédito calculada según lo previsto en la Sección 2., ex- presada en moneda homogénea del mes anterior al que se efectúa el cálculo. 7.3.2. El 17% en el caso de entidades del grupo B del promedio de los últimos 36 meses

**Respuesta breve:** Con n=0 debe observar una exigencia equivalente al límite fijado para el grupo 2: el 20 % (entidades del grupo A) o el 17 % (entidades del grupo B) del promedio de los últimos 36 meses de la exigencia de capital mínimo por riesgo de crédito, expresada en moneda homogénea del mes anterior al cálculo.

### CQN-015 — `cadena_normativa`

**Pregunta:** ¿Cómo se determina, día por día, la integración a considerar para verificar el cumplimiento de la exigencia de capital mínimo por riesgo de mercado?

**TOs fuente:** TO_capitales_minimos_actual.pdf

**Ground truth:** TO_capitales_minimos_actual.pdf Punto 1.3; TO_capitales_minimos_actual.pdf Punto 6.7

**Sección sorteada de origen:** TO_capitales_minimos_actual.pdf Sección 1; TO_capitales_minimos_actual.pdf Sección 6

**Cita textual:**
> En el caso de la exigencia de capital mínimo por riesgo de mercado, la integración se determi- nará en forma diaria de acuerdo con lo establecido en el punto 6.7.1. […] 6.7.1. Integración de capital. A los fines del cumplimiento de lo establecido en el punto 1.1., la integración se deter- minará en forma diaria considerando: 6.7.1.1. la RPC del último día del mes anterior; y 6.7.1.2. el cambio de valor diario que se produzca en el portafolio de activos incluidos en los cálculos de la exigencia por riesgo de mercado como consecuencia de cambios en sus precios de mercado, desde la última cotización registrada al cierre del mes inmediato anterior.

**Respuesta breve:** La integración por riesgo de mercado se determina en forma diaria considerando la responsabilidad patrimonial computable del último día del mes anterior más el cambio de valor diario del portafolio de activos incluidos en el cálculo de la exigencia, por variaciones de precios de mercado desde la última cotización del cierre del mes anterior.

## Fase 2/3 — Verificación programática de las citas (15/15)

Criterio: cada fragmento de `cita_textual` debe ser substring exacto del texto extraído del TO fuente, normalizando cadenas de espacios/saltos de línea a un espacio simple. Se verifica además que la pregunta no mencione números de punto/sección y que las secciones de origen pertenezcan al sorteo.

### Código
```python
import json, re, os

TXT = "/private/tmp/claude-501/-Users-agustinavidelarivero-SUBSET/1981adc0-31f2-45e6-b158-42495fece7e4/scratchpad/txt"
SCR = os.path.dirname(TXT)
norm = lambda s: re.sub(r"\s+", " ", s).strip()

textos = {f: norm(open(os.path.join(TXT, f.replace(".pdf", ".txt"))).read())
          for f in ["TO_capitales_minimos_actual.pdf", "TO_clasificacion_deudores_actual.pdf",
                    "TO_exterior_cambios_actual.pdf",
                    "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
                    "TO_regimen_informativo_contable_mensual_actual.pdf"]}
preguntas = json.load(open("/Users/agustinavidelarivero/SUBSET/preguntas_candidatas.json"))
sorteo = json.load(open(SCR + "/sorteo.json"))

ok = 0
for q in preguntas:
    # (d) cada fragmento de la cita debe hallarse VERBATIM (normalizado por
    # espacios) en el texto extraído de alguno de los TOs fuente
    frags = [f.strip() for f in q["cita_textual"].split("[…]") if f.strip()]
    verbatim = all(any(norm(fr) in textos[to] for to in q["tos_fuente"]) for fr in frags)
    # (c) la pregunta no menciona números de punto ni de sección
    sin_numeros = not re.search(r"([Ss]ecci[oó]n\s+\d|[Pp]unto\s+\d|\d+\.\d+\.)", q["pregunta"])
    # origen del sorteo válido
    origen_ok = all(
        int(o.rsplit(" ", 1)[1]) in sorteo[o.split(" Sección")[0]]
        for o in q["seccion_sorteada_origen"])
    estado = "OK " if (verbatim and sin_numeros and origen_ok) else "FALLA"
    ok += verbatim and sin_numeros and origen_ok
    print(f"{q['id']} [{q['categoria']:<16}] cita_verbatim={verbatim} "
          f"pregunta_sin_numeros={sin_numeros} seccion_sorteada={origen_ok} -> {estado}")
print(f"\nVerificación: {ok}/{len(preguntas)}")
cats = {}
for q in preguntas: cats[q["categoria"]] = cats.get(q["categoria"], 0) + 1
print("Distribución:", cats)
```
### Output
```
CQN-001 [factual_directa ] cita_verbatim=True pregunta_sin_numeros=True seccion_sorteada=True -> OK 
CQN-002 [factual_directa ] cita_verbatim=True pregunta_sin_numeros=True seccion_sorteada=True -> OK 
CQN-003 [factual_directa ] cita_verbatim=True pregunta_sin_numeros=True seccion_sorteada=True -> OK 
CQN-004 [factual_directa ] cita_verbatim=True pregunta_sin_numeros=True seccion_sorteada=True -> OK 
CQN-005 [factual_directa ] cita_verbatim=True pregunta_sin_numeros=True seccion_sorteada=True -> OK 
CQN-006 [factual_directa ] cita_verbatim=True pregunta_sin_numeros=True seccion_sorteada=True -> OK 
CQN-007 [factual_directa ] cita_verbatim=True pregunta_sin_numeros=True seccion_sorteada=True -> OK 
CQN-008 [multi_norma     ] cita_verbatim=True pregunta_sin_numeros=True seccion_sorteada=True -> OK 
CQN-009 [multi_norma     ] cita_verbatim=True pregunta_sin_numeros=True seccion_sorteada=True -> OK 
CQN-010 [multi_norma     ] cita_verbatim=True pregunta_sin_numeros=True seccion_sorteada=True -> OK 
CQN-011 [multi_norma     ] cita_verbatim=True pregunta_sin_numeros=True seccion_sorteada=True -> OK 
CQN-012 [multi_norma     ] cita_verbatim=True pregunta_sin_numeros=True seccion_sorteada=True -> OK 
CQN-013 [cadena_normativa] cita_verbatim=True pregunta_sin_numeros=True seccion_sorteada=True -> OK 
CQN-014 [cadena_normativa] cita_verbatim=True pregunta_sin_numeros=True seccion_sorteada=True -> OK 
CQN-015 [cadena_normativa] cita_verbatim=True pregunta_sin_numeros=True seccion_sorteada=True -> OK 

Verificación: 15/15
Distribución: {'factual_directa': 7, 'multi_norma': 5, 'cadena_normativa': 3}
```

## Entregables

- `inventario_secciones.json` — inventario de secciones y puntos de 1er/2do nivel.
- `preguntas_candidatas.json` — las 15 preguntas candidatas.
- `reporte_generacion.md` — este reporte.
