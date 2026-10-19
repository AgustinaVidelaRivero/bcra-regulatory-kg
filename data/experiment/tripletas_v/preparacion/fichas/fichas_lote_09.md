# U-TRIP-V: fichas del lote 09 (10)

Acta del sorteo `acta_sorteo_V.json` (sha256 `5d6a237e510bcf086db717061dd146eaa9b3181006cb7b1d300164436c720c55`), sellada a las 2026-10-19T14:23:55-03:00; fichas generadas a las 2026-10-19T14:25:19-03:00. Grafo KG-Tanda0-Desarrollo-r2b-sincola-rs1 (`66e745f5…`). Las fichas van en el orden sellado. Criterio (§3.4 del pre-registro): la evidencia sostiene la relación entre esos dos nodos, con sus sujetos, valores, calificadores y modalidad.

Cada ficha trae los dos nodos (tipo, etiqueta, descripción y propiedades), el predicado y la evidencia de cada procedencia: el texto heredado y el propio de la unidad de E0, el tramo literal de cada extremo en esa unidad si lo hay, las páginas y la ruta del PDF con la página. «literal» dice si el tramo está tal cual en el texto (exacta), por tokens (tokens) o no (no).

## V091 · `aplica_a` · lote_09, 1 de 10

**Origen** — Obligacion «Inclusión información BI desde fecha de adquisición» (`Obligacion_la_informacion_sobre_el_indicador_de_negocios_de_los_periodos_anteriores_debe_se_385a38`)

- descripción: La información sobre el indicador de negocios de los períodos anteriores debe ser computada a partir de la fecha de adquisición, entendida como aquélla en la que la adquirente obtiene el control de la adquirida.
- tipo: calculo

**Predicado** — `aplica_a`

- tramo del sujeto: «las entidades financieras» (literal: exacta)

**Destino** — Sujeto «Entidades financieras» (`Sujeto_entidad_financiera`)

- descripción: —
- nivel: clase
- alias: ["Entidades financieras emisoras de tarjetas de crédito y/o compra", "Entidad financiera emisora de tarjetas de crédito y/o compra"]

**Evidencia 1 de 1** — `cap::7.1.1.4` · cap · punto 7.1.1.4 · punto_propio · págs. 149, 150

- PDF: `data/experiment/subset/TO_capitales_minimos_actual.pdf#page=149` · `data/experiment/subset/TO_capitales_minimos_actual.pdf#page=150`

> *heredado (encabezado, S7, p. 145):* Sección 7. Capital mínimo por riesgo operacional.
>
> *heredado (chapeau_seccion, S7, p. 145):* A los efectos de la aplicación de las disposiciones de la presente sección, las entidades financieras se clasificarán en grupo 1 y grupo 2, conforme a lo previsto en la Sección 2.
>
> *heredado (encabezado, 7.1, p. 145):* 7.1. Exigencia de capital por riesgo operacional para entidades del grupo 1.
>
> *heredado (intro, 7.1, p. 145):* Se determinará mensualmente por la siguiente expresión:
>
> *heredado (intro, 7.1, p. 145):* C = BIC x ILM
>
> *heredado (intro, 7.1, p. 145):* RO
>
> *heredado (intro, 7.1, p. 145):* Donde: C : exigencia de capital por riesgo operacional.
>
> *heredado (intro, 7.1, p. 145):* RO
>
> *heredado (intro, 7.1, p. 145):* BIC: componente del indicador de negocio, que es el producto del indicador de negocio (BI)
>
> *heredado (intro, 7.1, p. 145):* por una serie de coeficientes marginales (α), calculado según lo previsto en el punto
>
> *heredado (intro, 7.1, p. 145):* i
>
> *heredado (intro, 7.1, p. 145):* 7.1.2.
>
> *heredado (intro, 7.1, p. 145):* ILM: multiplicador de pérdida interna igual a 1. Los activos ponderados por riesgo (APR) para el riesgo operacional son iguales a 12,5 veces el C .
>
> *heredado (intro, 7.1, p. 145):* RO
>
> *heredado (encabezado, 7.1.1, p. 145):* 7.1.1. Indicador de negocio (BI).
>
> *heredado (intro, 7.1.1, p. 145):* El BI es una aproximación al riesgo operacional a partir de la información de los estados financieros. Se determinará por la siguiente expresión:
>
> *heredado (intro, 7.1.1, p. 145):* BI = VA (ILDC + SC + FC + RM )
>
> *heredado (intro, 7.1.1, p. 145):* Prom Prom Prom Prom
>
> *heredado (intro, 7.1.1, p. 145):* ILDC : Componente de intereses, arrendamientos y dividendos. Se determinará por la
>
> *heredado (intro, 7.1.1, p. 145):* Prom
>
> *heredado (intro, 7.1.1, p. 145):* siguiente expresión: Mín. [VA (ingresos por intereses – egresos por intereses); 5% x activos que devengan intereses] + ingresos por dividendos
>
> *heredado (intro, 7.1.1, p. 145):* SC : Componente de servicios. Se determinará por la siguiente expresión:
>
> *heredado (intro, 7.1.1, p. 145):* Prom
>
> *heredado (intro, 7.1.1, p. 145):* Máx. [otros ingresos por operaciones; otros egresos por operaciones] + Máx. [ingresos por honorarios y comisiones; egresos por honorarios y comisiones]
>
> *heredado (intro, 7.1.1, p. 146):* FC : Componente financiero. Se determinará por la siguiente expresión:
>
> *heredado (intro, 7.1.1, p. 146):* Prom
>
> *heredado (intro, 7.1.1, p. 146):* VA (resultado neto de cartera de negociación) + VA (resultado neto de cartera de inversión)
>
> *heredado (intro, 7.1.1, p. 146):* RM : Resultado monetario total
>
> *heredado (intro, 7.1.1, p. 146):* Prom
>
> *heredado (intro, 7.1.1, p. 146):* VA: Valor absoluto. Cada término dentro de los 3 componentes y el resultado monetario debe ser calculado como el promedio de los valores de los 3 últimos períodos consecutivos de 12 meses an- teriores al mes en que se efectúa el cálculo, expresados en moneda homogénea al cierre del período de cálculo de 36 meses: t, t-1 y t-2. Se debe determinar, en primer lugar, el valor de las partidas netas que correspondan (por ejemplo, ingresos por intereses menos egresos por intereses) para cada período de 12 meses consecutivos y, luego, el prome- dio de los 3 períodos.
>
> *propio:* 7.1.1.4. Inclusión de partidas del BI relacionadas con combinaciones de negocios (fusio- nes y adquisiciones). El promedio que se emplea para el cálculo del BI debe cubrir los últimos 3 perío- dos consecutivos de 12 meses (36 meses en total) de los negocios adquiridos en este lapso. La información sobre el indicador de negocios de los períodos anteriores debe ser computada a partir de la fecha de adquisición, que es aquélla en la que la adquirente obtiene el control de la adquirida. Esa información debe ser incluida en oportunidad de la primera determinación del requisito de capital mínimo por riesgo operacional e informada en la primera actualización de los activos ponde- rados por riesgo total posterior a la adquisición.

- tramo del origen: «La información sobre el indicador de negocios de los períodos anteriores debe ser computada a partir de la fecha de adquisición, que es aquélla en la que la adquirente obtiene el control de la adquirida.» (literal: exacta)
- tramo del destino: —

---

## V092 · `limita` · lote_09, 2 de 10

**Origen** — Restriccion «Instrumentación de exposiciones minoristas» (`Restriccion_las_exposiciones_minoristas_normativas_deben_instrumentarse_exclusivamente_como__9921b5`)

- descripción: Las exposiciones minoristas normativas deben instrumentarse exclusivamente como: financiaciones rotativas (revolving), préstamos prendarios, préstamos personales, arrendamientos financieros, o financiaciones a Mipyme.
- tipo: limite_cualitativo

**Predicado** — `limita`

**Destino** — Operacion «Financiaciones a Mipyme» (`Operacion_financiaciones_a_mipyme__cap_2_8_3_1_312f1e`)

- descripción: Financiaciones otorgadas a Mipyme, como instrumento de exposición minorista normativa.
- tipo: financiación a Mipyme

**Evidencia 1 de 1** — `cap::2.8.3.1` · cap · punto 2.8.3.1 · punto_propio · págs. 17

- PDF: `data/experiment/subset/TO_capitales_minimos_actual.pdf#page=17`

> *heredado (encabezado, S2, p. 7):* Sección 2. Capital mínimo por riesgo de crédito.
>
> *heredado (chapeau_seccion, S2, p. 7):* A los efectos de la aplicación de las disposiciones de la presente sección, las entidades financieras se clasificarán en: i)Grupo 1: entidades calificadas por el BCRA como de importancia sistémica a nivel local
>
> *heredado (chapeau_seccion, S2, p. 7):* (D-SIB) y sucursales o subsidiarias de bancos del exterior calificados como de impor- tancia sistémica global (G-SIB).
>
> *heredado (chapeau_seccion, S2, p. 7):* ii) Grupo 2: entidades financieras no comprendidas en el acápite i). En aquellos casos en que no se establezcan disposiciones específicas para cada uno de los citados grupos de entidades financieras, deberá aplicarse el mismo tratamiento a ambos grupos. Las entidades financieras que presenten cambios en su calificación –conforme a lo previsto en los acápites precedentes–, contarán con un plazo de 6 meses para aplicar las disposiciones específicas correspondientes al nuevo grupo al que pertenezcan.
>
> *heredado (encabezado, 2.8, p. 16):* 2.8. Exposiciones minoristas.
>
> *heredado (encabezado, 2.8.3, p. 17):* 2.8.3. Exposiciones minoristas normativas. Criterios.
>
> *propio:* 2.8.3.1. Producto. Las exposiciones deberán instrumentarse como financiaciones rotativas (revol- ving), préstamos prendarios, personales, arrendamientos financieros y/o tratar- se de financiaciones a Mipyme. Se entiende por financiaciones rotativas a aquellas financiaciones en las cuales los prestatarios están autorizados a reali- zar giros y cancelaciones dentro de los límites convenidos en una línea de cré- dito, y que incluyen tarjetas de crédito y descubiertos en cuenta corriente.

- tramo del origen: «Las exposiciones deberán instrumentarse como financiaciones rotativas (revolving), préstamos prendarios, personales, arrendamientos financieros y/o tratarse de financiaciones a Mipyme.» (literal: exacta)
- tramo del destino: «financiaciones a Mipyme» (literal: exacta)

---

## V093 · `aplica_a` · lote_09, 3 de 10

**Origen** — Obligacion «Certificar cumplimiento de condiciones de elegibilidad — entidad financiera» (`Obligacion_la_entidad_financiera_local_designada_debera_certificar_el_cumplimiento_de_las_c_45327d`)

- descripción: La entidad financiera local designada deberá certificar el cumplimiento de las condiciones de elegibilidad de las operaciones de financiamiento a las cuales se aplicarán las divisas
- tipo: presentacion_informativa

**Predicado** — `aplica_a`

- tramo del sujeto: «la entidad financiera local» (literal: no)

**Destino** — Sujeto «Entidades financieras» (`Sujeto_entidad_financiera`)

- descripción: —
- nivel: clase
- alias: ["Entidades financieras emisoras de tarjetas de crédito y/o compra", "Entidad financiera emisora de tarjetas de crédito y/o compra"]

**Evidencia 1 de 1** — `ext::7.9.3.1` · ext · punto 7.9.3.1 · punto_propio · págs. 97

- PDF: `data/experiment/subset/TO_exterior_cambios_actual.pdf#page=97`

> *heredado (encabezado, S7, p. 80):* Sección 7. Cobros de exportaciones de bienes.
>
> *heredado (encabezado, 7.9, p. 94):* 7.9. Operaciones financieras habilitadas para aplicar cobros de exportaciones de bienes y
>
> *heredado (intro, 7.9, p. 94):* servicios.
>
> *heredado (encabezado, 7.9.3, p. 97):* 7.9.3. Los exportadores que opten por este mecanismo deberán designar una entidad
>
> *heredado (intro, 7.9.3, p. 97):* financiera local para que realice el seguimiento de la operación, la cual se encargará de:
>
> *heredado (intersticial, 7.9.3, p. 98):* En el caso de que se trate de operaciones destinadas a los proyectos comprendidos en el punto 7.9.2., la entidad encargada del seguimiento deberá adicionalmente:
>
> *propio:* 7.9.3.1. certificar el cumplimiento de las condiciones de elegibilidad de las operaciones de financiamiento a las cuales se aplicarán las divisas,

- tramo del origen: «certificar el cumplimiento de las condiciones de elegibilidad de las operaciones de financiamiento a las cuales se aplicarán las divisas» (literal: exacta)
- tramo del destino: —

---

## V094 · `regula` · lote_09, 4 de 10

**Origen** — Obligacion «Computar conceptos sobre base individual y consolidada mensual» (`Obligacion_deber_de_computar_los_conceptos_comprendidos_sobre_la_base_de_los_saldos_al_ulti_932c6a`)

- descripción: Deber de computar los conceptos comprendidos sobre la base de los saldos al último día de cada mes, incluyendo capitales, intereses, primas, actualizaciones por CER y diferencias de cotización, netos de previsiones por riesgos de incobrabilidad (incluyendo las contabilizadas en pasivo), desvalorización, depreciaciones y amortizaciones acumuladas atribuibles y demás cuentas regularizadoras, sin deducir el 100% de la previsión por riesgo de incobrabilidad de deudores en situación normal ni de financiaciones cubiertas con garantías preferidas A.
- tipo: calculo
- umbrales (1):
  - comparacion: no_determinada; tramo: al último día de cada mes

**Predicado** — `regula`

**Destino** — Operacion «Cómputo de conceptos sobre saldos mensuales» (`Operacion_computo_de_conceptos_sobre_saldos_mensuales__cap_2_3_1_aba85b`)

- descripción: Cómputo de conceptos (capitales, intereses, primas, actualizaciones por CER, diferencias de cotización) sobre la base de los saldos al último día de cada mes, netos de previsiones por riesgos de incobrabilidad y desvalorización, y depreciaciones y amortizaciones acumuladas atribuibles, sin deducir el 100% de la previsión por riesgo de incobrabilidad de deudores en situación normal ni de financiaciones cubiertas con garantías preferidas A.
- tipo: cálculo

**Evidencia 1 de 1** — `cap::2.3.1` · cap · punto 2.3.1 · punto_propio · págs. 10

- PDF: `data/experiment/subset/TO_capitales_minimos_actual.pdf#page=10`

> *heredado (encabezado, S2, p. 7):* Sección 2. Capital mínimo por riesgo de crédito.
>
> *heredado (chapeau_seccion, S2, p. 7):* A los efectos de la aplicación de las disposiciones de la presente sección, las entidades financieras se clasificarán en: i)Grupo 1: entidades calificadas por el BCRA como de importancia sistémica a nivel local
>
> *heredado (chapeau_seccion, S2, p. 7):* (D-SIB) y sucursales o subsidiarias de bancos del exterior calificados como de impor- tancia sistémica global (G-SIB).
>
> *heredado (chapeau_seccion, S2, p. 7):* ii) Grupo 2: entidades financieras no comprendidas en el acápite i). En aquellos casos en que no se establezcan disposiciones específicas para cada uno de los citados grupos de entidades financieras, deberá aplicarse el mismo tratamiento a ambos grupos. Las entidades financieras que presenten cambios en su calificación –conforme a lo previsto en los acápites precedentes–, contarán con un plazo de 6 meses para aplicar las disposiciones específicas correspondientes al nuevo grupo al que pertenezcan.
>
> *heredado (encabezado, 2.3, p. 10):* 2.3. Cómputo de los conceptos comprendidos.
>
> *propio:* 2.3.1. Bases individual y consolidada mensual. Los conceptos comprendidos se computarán sobre la base de los saldos al último día de cada mes (capitales, intereses, primas, actualizaciones –por el Coeficiente de Estabilización de Referencia CER– y diferencias de cotización, según corresponda, netos de las previsiones por riesgos de incobrabilidad –incluyendo, de corresponder, las previsiones contabilizadas en el pasivo– y desvalorización y de las depreciaciones y amortizaciones acumuladas que les sean atribuibles y demás cuentas regularizadoras, sin deducir el 100% del importe de la previsión por riesgo de incobrabilidad correspondiente a la cartera de deudores clasificados “en situación normal” –puntos 6.5.1. y 7.2.1. del TO sobre Clasificación de Deudores– y a las financiaciones que se encuentran cubiertas con garantías preferidas A).

- tramo del origen: «Los conceptos comprendidos se computarán sobre la base de los saldos al último día de cada mes (capitales, intereses, primas, actualizaciones –por el Coeficiente de Estabilización de Referencia CER– y diferencias de cotización, según corresponda, netos de las previsiones por riesgos de incobrabilidad –incluyendo, de corresponder, las previsiones contabilizadas en el pasivo– y desvalorización y de las depreciaciones y amortizaciones acumuladas que les sean atribuibles y demás cuentas regularizadoras, sin deducir el 100% del importe de la previsión por riesgo de incobrabilidad correspondiente a la cartera de deudores clasificados "en situación normal" –puntos 6.5.1. y 7.2.1. del TO sobre Clasificación de Deudores– y a las financiaciones que se encuentran cubiertas con garantías preferidas A).» (literal: exacta)
- tramo del destino: «Los conceptos comprendidos se computarán sobre la base de los saldos al último día de cada mes» (literal: exacta)

---

## V095 · `aplica_a` · lote_09, 5 de 10

**Origen** — Obligacion «Clasificar deudores de créditos fideicomitidos» (`Obligacion_deber_de_clasificar_a_los_deudores_de_los_creditos_fideicomitidos_de_acuerdo_con_2a04b3`)

- descripción: Deber de clasificar a los deudores de los créditos fideicomitidos de acuerdo con la periodicidad y demás condiciones establecidas para las carteras comercial o para consumo o vivienda, según corresponda
- tipo: otra

**Predicado** — `aplica_a`

- tramo del sujeto: «Fiduciarios de fideicomisos financieros» (literal: exacta)

**Destino** — Sujeto «Fiduciarios de fideicomisos financieros» (`Sujeto_fiduciario_de_fideicomiso_financiero`)

- descripción: —
- nivel: clase

**Evidencia 1 de 1** — `cla::10.2.1` · cla · punto 10.2.1 · punto_propio · págs. 43

- PDF: `data/experiment/subset/TO_clasificacion_deudores_actual.pdf#page=43`

> *heredado (encabezado, S10, p. 43):* Sección 10. Otros obligados a la observancia de las normas sobre clasificación de deudores.
>
> *heredado (encabezado, 10.2, p. 43):* 10.2. Fiduciarios de fideicomisos financieros comprendidos en la Ley de Entidades Financieras.
>
> *propio:* 10.2.1. Clasificación de deudores de créditos fideicomitidos. Deberán clasificar a los deudores de los créditos fideicomitidos de acuerdo con la pe- riodicidad y demás condiciones establecidas para las carteras “comercial” o “para con- sumo o vivienda”, según corresponda.

- tramo del origen: «Deberán clasificar a los deudores de los créditos fideicomitidos de acuerdo con la periodicidad y demás condiciones establecidas para las carteras "comercial" o "para consumo o vivienda", según corresponda» (literal: exacta)
- tramo del destino: —

---

## V096 · `aplica_a` · lote_09, 6 de 10

**Origen** — Obligacion «Entrega o acreditación de fondos — compra de billetes» (`Obligacion_la_entidad_vendedora_debe_entregar_los_billetes_en_moneda_extranjera_o_acreditar_663275`)

- descripción: La entidad vendedora debe entregar los billetes en moneda extranjera o acreditar los fondos en una cuenta en moneda extranjera de titularidad del cliente en entidades financieras locales o en una cuenta bancaria de titularidad del cliente en el exterior, según corresponda
- tipo: otra

**Predicado** — `aplica_a`

- tramo del sujeto: «La entidad vendedora» (literal: exacta)

**Destino** — Sujeto «Entidades autorizadas a operar en cambios (Exterior)» (`Sujeto_rol_entidad_autorizada_exterior`)

- descripción: —
- nivel: rol

**Evidencia 1 de 1** — `ext::3.8.2` · ext · punto 3.8.2 · punto_propio · págs. 32

- PDF: `data/experiment/subset/TO_exterior_cambios_actual.pdf#page=32`

> *heredado (encabezado, S3, p. 16):* Sección 3. Disposiciones específicas para los egresos por el mercado de cambios
>
> *heredado (chapeau_seccion, S3, p. 16):* Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–, adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables.
>
> *heredado (encabezado, 3.8, p. 32):* 3.8. Compra de moneda extranjera por parte de personas humanas residentes para la formación
>
> *heredado (intro, 3.8, p. 32):* de activos externos en forma de billetes y/o depósitos. Las entidades podrán dar acceso al mercado de cambios a las personas humanas residentes para la compra de billetes en moneda extranjera para su tenencia o para la constitución de depósitos (códigos de concepto A07 y A09) en la medida que se cumplan la totalidad de los siguientes requisitos:
>
> *propio:* 3.8.2. La entidad vendedora deberá entregar los billetes en moneda extranjera o acreditar los fondos en una cuenta en moneda extranjera de titularidad del cliente en entidades financieras locales o en una cuenta bancaria de titularidad del cliente en el exterior, según corresponda.

- tramo del origen: «La entidad vendedora deberá entregar los billetes en moneda extranjera o acreditar los fondos en una cuenta en moneda extranjera de titularidad del cliente en entidades financieras locales o en una cuenta bancaria de titularidad del cliente en el exterior, según corresponda» (literal: exacta)
- tramo del destino: —

---

## V097 · `condicion_de` · lote_09, 7 de 10

**Origen** — Condicion «Verificación de totalidad de requisitos posteriores» (`Condicion_verificacion_de_totalidad_de_requisitos_posteriores__la_emision_de_certificacion_7d815d`)

- descripción: La emisión de certificaciones está condicionada a que se verifique la totalidad de los requisitos que siguen.

**Predicado** — `condicion_de`

**Destino** — Potestad «Emisión de certificaciones por entidad nominada» (`Potestad_emision_de_certificaciones_por_entidad_nominada__la_entidad_nominada_esta_facult_bdaa9d`)

- descripción: La entidad nominada está facultada a emitir las certificaciones para cada periodo trimestral de referencia posterior a la inscripción del cliente en el registro, cuando se verifiquen la totalidad de los siguientes requisitos.

**Evidencia 1 de 1** — `ext::2.6.2::intro` · ext · punto 2.6.2 · bloque_intro · págs. 12

- PDF: `data/experiment/subset/TO_exterior_cambios_actual.pdf#page=12`

> *heredado (encabezado, S2, p. 8):* Sección 2. Disposiciones específicas para los ingresos por el mercado de cambios.
>
> *heredado (encabezado, 2.6, p. 12):* 2.6. Excepción de liquidación de cobros de exportaciones de bienes y servicios para los
>
> *heredado (encabezado, 2.6.2, p. 12):* 2.6.2. El beneficiario deberá nominar una única entidad financiera local que será la
>
> *propio:* responsable de emitir las “Certificaciones de incremento de exportaciones asociadas a la economía del conocimiento (Decreto 679/22)” y remitirlas a las entidades por las cuales el cliente desee concretar los ingresos de sus cobros de exportaciones de bienes o servicios. La entidad nominada podrá emitir estas certificaciones para cada periodo trimestral de referencia posterior a la inscripción del cliente en el registro, cuando se verifiquen la totalidad de los siguientes requisitos:

- tramo del origen: «cuando se verifiquen la totalidad de los siguientes requisitos:» (literal: exacta)
- tramo del destino: «La entidad nominada podrá emitir estas certificaciones para cada periodo trimestral de referencia posterior a la inscripción del cliente en el registro, cuando se verifiquen la totalidad de los siguientes requisitos:» (literal: exacta)

---

## V098 · `aplica_a` · lote_09, 8 de 10

**Origen** — Obligacion «Informar comisiones y cargos al BCRA» (`Obligacion_las_entidades_financieras_pspcp_empresas_no_financieras_emisoras_de_tarjetas_de__e8ed9d`)

- descripción: Las entidades financieras, PSPCP, empresas no financieras emisoras de tarjetas de crédito y/o compra y otros proveedores no financieros de crédito que ofrezcan y comercialicen productos y/o servicios que se perfeccionan con contratos de adhesión deberán informar las comisiones y cargos que cobren a los usuarios de servicios financieros mediante el régimen informativo establecido al efecto.
- tipo: reporte_al_supervisor

**Predicado** — `aplica_a`

- tramo del sujeto: «los otros proveedores no financieros de crédito» (literal: exacta)

**Destino** — Sujeto «Proveedores no financieros de crédito» (`Sujeto_proveedor_no_financiero_de_credito`)

- descripción: —
- nivel: clase
- alias: ["PNFC"]

**Evidencia 1 de 1** — `pro::2.5` · pro · punto 2.5 · punto_propio · págs. 21

- PDF: `data/experiment/subset/TO_proteccion_usuarios_servicios_financieros_actual.pdf#page=21`

> *heredado (encabezado, S2, p. 5):* Sección 2. Derechos básicos de los usuarios de servicios financieros.
>
> *propio:* 2.5. Información al Banco Central de la República Argentina. Las entidades financieras, los PSPCP, las empresas no financieras emisoras de tarjetas de crédito y/o compra y los otros proveedores no financieros de crédito que ofrezcan y comerciali- cen productos y/o servicios que se perfeccionan con la firma o aceptación de contratos con cláusulas preestablecidas (contratos de adhesión), deberán informar las comisiones y cargos que cobren a los usuarios de servicios financieros mediante el régimen informativo establecido al efecto. Las altas –comisiones de nuevos productos y/o servicios que deseen comercializar– y los au- mentos en las comisiones que deseen implementar deberán ser previamente informados al BCRA por la vía consignada en el párrafo precedente y luego ser notificadas a los usuarios de servicios financieros. También deberán informar las modificaciones de los cargos. Las reducciones en las comisiones y/o cargos podrán aplicarse sin demora, sin perjuicio de que deberán ser informadas al BCRA dentro de los treinta (30) días corridos siguientes de su apli- cación.

- tramo del origen: «deberán informar las comisiones y cargos que cobren a los usuarios de servicios financieros mediante el régimen informativo establecido al efecto» (literal: exacta)
- tramo del destino: —

---

## V099 · `condicion_de` · lote_09, 9 de 10

**Origen** — Condicion «Transcurso de plazo en precancelación total» (`Condicion_transcurso_de_plazo_en_precancelacion_total__cuando_al_momento_de_efectuar_la_pr_74ac9a`)

- descripción: Cuando al momento de efectuar la precancelación total haya transcurrido al menos la cuarta parte del plazo original de la financiación o 180 días corridos desde su otorgamiento, de ambos el mayor.
- umbrales (2):
  - comparacion: minimo_inclusivo; tramo: al menos la cuarta parte del plazo original de la financiación
  - valor: 180; unidad: dias; comparacion: no_determinada; dias_tipo: corridos; tramo: 180 días corridos desde su otorgamiento

**Predicado** — `condicion_de`

**Destino** — Restriccion «Prohibición de comisiones en precancelación total con plazo cumplido» (`Restriccion_en_precancelacion_total_no_se_admitira_la_aplicacion_de_comisiones_cuando_haya_t_239bd5`)

- descripción: En precancelación total, no se admitirá la aplicación de comisiones cuando haya transcurrido al menos la cuarta parte del plazo original de la financiación o 180 días corridos desde su otorgamiento, de ambos el mayor.
- tipo: prohibicion
- umbrales (2):
  - comparacion: minimo_inclusivo; tramo: al menos la cuarta parte del plazo original de la financiación
  - valor: 180; unidad: dias; comparacion: no_determinada; dias_tipo: corridos; tramo: 180 días corridos desde su otorgamiento

**Evidencia 1 de 1** — `pro::2.3.2.1` · pro · punto 2.3.2.1 · punto_propio · págs. 11, 12

- PDF: `data/experiment/subset/TO_proteccion_usuarios_servicios_financieros_actual.pdf#page=11` · `data/experiment/subset/TO_proteccion_usuarios_servicios_financieros_actual.pdf#page=12`

> *heredado (encabezado, S2, p. 5):* Sección 2. Derechos básicos de los usuarios de servicios financieros.
>
> *heredado (encabezado, 2.3, p. 7):* 2.3. Recaudos mínimos de la relación de consumo.
>
> *heredado (encabezado, 2.3.2, p. 11):* 2.3.2. Comisiones y cargos.
>
> *propio:* 2.3.2.1. Admitidos. Todas las comisiones, cargos, costos, gastos, seguros y/o cualquier otro con- cepto –excluyendo la tasa de interés– que los sujetos obligados perciban o pre- tendan percibir de los usuarios de servicios financieros (comisiones y cargos), deben tener origen en un costo real, directo y demostrable y estar debidamente justificados desde el punto de vista técnico y económico. La aplicación de comisiones y/o cargos debe quedar circunscripta a la efectiva prestación de un servicio que haya sido previamente solicitado, pactado y/o au- torizado por el usuario. Las comisiones obedecen a servicios que prestan los sujetos obligados y, en tal sentido, pueden incluir retribuciones a su favor que excedan el costo de la prestación. Los cargos obedecen a servicios que prestan terceros, por lo que solamente pueden ser transferidos al costo a los usuarios. Asimismo, el importe de los cargos que el sujeto obligado transfiera a los usua- rios no podrá ser superior al que el tercero prestador perciba de particulares, sin intermediarios y en similares condiciones (servicios postales, compañía de seguros, escribanía y registros de propiedad, u otros de índole similar). En las operaciones de crédito, los sujetos obligados podrán aplicar comisiones sobre los importes no utilizados de los acuerdos de asignación de fondos, dado que su puesta a disposición a los usuarios configura la prestación del servicio. La precancelación total o parcial de financiaciones podrá dar lugar a la aplica- ción de comisiones. En el caso de precancelación total, no se admitirá la apli- cación de comisiones cuando al momento de efectuarla haya transcurrido al menos la cuarta parte del plazo original de la financiación o 180 días corridos desde su otorgamiento, de ambos el mayor. Además, será de aplicación lo previsto en el punto 1.7. del TO sobre Tasas de Interés en las Operaciones de Crédito.

- tramo del origen: «cuando al momento de efectuarla haya transcurrido al menos la cuarta parte del plazo original de la financiación o 180 días corridos desde su otorgamiento, de ambos el mayor» (literal: exacta)
- tramo del destino: «En el caso de precancelación total, no se admitirá la aplicación de comisiones cuando al momento de efectuarla haya transcurrido al menos la cuarta parte del plazo original de la financiación o 180 días corridos desde su otorgamiento, de ambos el mayor» (literal: exacta)

---

## V100 · `aplica_a` · lote_09, 10 de 10

**Origen** — Obligacion «Reconocer protección crediticia — bancos multilaterales de desarrollo» (`Obligacion_se_reconocera_la_proteccion_crediticia_provista_por_bancos_multilaterales_de_des_e580f3`)

- descripción: Se reconocerá la protección crediticia provista por bancos multilaterales de desarrollo a que se refiere el punto 2.12.3, cuando las garantías o derivados de crédito sean directos, explícitos, irrevocables e incondicionales, en la medida de que su ponderador de riesgo sea inferior al de la contraparte
- tipo: otra

**Predicado** — `aplica_a`

- tramo del sujeto: «Bancos multilaterales de desarrollo» (literal: exacta)

**Destino** — Sujeto «Bancos multilaterales de desarrollo» (`Sujeto_banco_multilateral_de_desarrollo`)

- descripción: —
- nivel: clase
- alias: ["BMD"]

**Evidencia 1 de 1** — `cap::5.4.1` · cap · punto 5.4.1 · punto_propio · págs. 113

- PDF: `data/experiment/subset/TO_capitales_minimos_actual.pdf#page=113`

> *heredado (encabezado, S5, p. 98):* Sección 5. Cobertura del riesgo de crédito.
>
> *heredado (chapeau_seccion, S5, p. 98):* A los efectos del cómputo de la exigencia de capital por riesgo de crédito, se reconocerá –total o parcialmente– la cobertura del riesgo de crédito (CRC) de las operaciones registradas en la cartera de inversión –tales como préstamos y responsabilidades eventuales– mediante la utilización de las técnicas previstas en el punto 5.1. La presente sección contempla, además, el cálculo de la exposición a las operaciones de financia- ción con títulos valores (securities financing transactions, SFT) –conforme a lo previsto en la Sec- ción 4.–, registradas tanto en la cartera de inversión como en la cartera de negociación.
>
> *heredado (encabezado, 5.4, p. 112):* 5.4. Operaciones cubiertas con garantías (y contragarantías) personales y derivados de crédito.
>
> *heredado (intro, 5.4, p. 112, 113):* Se aplicará el método de sustitución de ponderadores. Con este método, el ponderador de riesgo de la contraparte se sustituye por el ponderador de riesgo del garante –o contragarante– o proveedor de protección crediticia –conforme a la tabla de ponderadores prevista en la Sec- ción 2.–. Se reconocerán sólo las garantías emitidas –o protección provista, en el caso de derivados de crédito– por entidades listadas en el punto 5.4.1. La parte de la exposición sin cobertura mantendrá el ponderador de riesgo de la contraparte original, mientras que a la parte cubierta se le asignará el ponderador de riesgo del garante o proveedor de protección crediticia, teniendo en consideración lo siguiente:
>
> *propio:* 5.4.1. Garantes (y contragarantes) y proveedores de protección crediticia admisibles en el mé- todo de sustitución de ponderadores. Cuando las garantías o derivados de crédito sean directos, explícitos, irrevocables e in- condicionales, se reconocerá la protección crediticia provista por los siguientes entes en la medida de que su ponderador de riesgo –conforme a lo establecido en la Sección 2.– sea inferior al de la contraparte: i) Sector público no financiero. ii) Entidades financieras. iii) Sociedades de garantía recíproca y fondos de garantía de carácter público, inscriptos en los registros habilitados en el BCRA. iv) Bancos multilaterales de desarrollo a que se refiere el punto 2.12.3. v) Organismos internacionales a los que se les asigne un ponderador del 0%, conforme a la tabla de ponderadores prevista en la Sección 2. vi) Empresas con “grado de inversión”, de acuerdo con la definición prevista en el inciso b) del acápite v) del punto 5.3.1.2.

- tramo del origen: «se reconocerá la protección crediticia provida por los siguientes entes […] iv) Bancos multilaterales de desarrollo a que se refiere el punto 2.12.3» (literal: no)
- tramo del destino: —

---

