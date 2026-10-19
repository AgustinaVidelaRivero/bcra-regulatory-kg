# U-TRIP-V: fichas del lote 07 (10)

Acta del sorteo `acta_sorteo_V.json` (sha256 `5d6a237e510bcf086db717061dd146eaa9b3181006cb7b1d300164436c720c55`), sellada a las 2026-10-19T14:23:55-03:00; fichas generadas a las 2026-10-19T14:25:19-03:00. Grafo KG-Tanda0-Desarrollo-r2b-sincola-rs1 (`66e745f5…`). Las fichas van en el orden sellado. Criterio (§3.4 del pre-registro): la evidencia sostiene la relación entre esos dos nodos, con sus sujetos, valores, calificadores y modalidad.

Cada ficha trae los dos nodos (tipo, etiqueta, descripción y propiedades), el predicado y la evidencia de cada procedencia: el texto heredado y el propio de la unidad de E0, el tramo literal de cada extremo en esa unidad si lo hay, las páginas y la ruta del PDF con la página. «literal» dice si el tramo está tal cual en el texto (exacta), por tokens (tokens) o no (no).

## V071 · `aplica_a` · lote_07, 1 de 10

**Origen** — Restriccion «Requisito mínimo capital — acciones de canje» (`Restriccion_el_requisito_de_capitales_minimos_para_acciones_originadas_en_canje_de_deuda_no__6b680c`)

- descripción: El requisito de capitales mínimos para acciones originadas en canje de deuda no puede ser inferior al que hubiera correspondido si permanecieran en cartera de créditos.
- tipo: limite_cuantitativo
- umbrales (1):
  - comparacion: minimo_inclusivo; base: que le hubiera correspondido de haber permanecido en la cartera de créditos; tramo: no puede ser menor al que le hubiera correspondido de haber permanecido en la cartera de créditos

**Predicado** — `aplica_a`

- tramo del sujeto: «las entidades financieras» (literal: exacta)

**Destino** — Sujeto «Entidades financieras» (`Sujeto_entidad_financiera`)

- descripción: —
- nivel: clase
- alias: ["Entidades financieras emisoras de tarjetas de crédito y/o compra", "Entidad financiera emisora de tarjetas de crédito y/o compra"]

**Evidencia 1 de 1** — `cap::2.11.3.5` · cap · punto 2.11.3.5 · punto_propio · págs. 22

- PDF: `data/experiment/subset/TO_capitales_minimos_actual.pdf#page=22`

> *heredado (encabezado, S2, p. 7):* Sección 2. Capital mínimo por riesgo de crédito.
>
> *heredado (chapeau_seccion, S2, p. 7):* A los efectos de la aplicación de las disposiciones de la presente sección, las entidades financieras se clasificarán en: i)Grupo 1: entidades calificadas por el BCRA como de importancia sistémica a nivel local
>
> *heredado (chapeau_seccion, S2, p. 7):* (D-SIB) y sucursales o subsidiarias de bancos del exterior calificados como de impor- tancia sistémica global (G-SIB).
>
> *heredado (chapeau_seccion, S2, p. 7):* ii) Grupo 2: entidades financieras no comprendidas en el acápite i). En aquellos casos en que no se establezcan disposiciones específicas para cada uno de los citados grupos de entidades financieras, deberá aplicarse el mismo tratamiento a ambos grupos. Las entidades financieras que presenten cambios en su calificación –conforme a lo previsto en los acápites precedentes–, contarán con un plazo de 6 meses para aplicar las disposiciones específicas correspondientes al nuevo grupo al que pertenezcan.
>
> *heredado (encabezado, 2.11, p. 21):* 2.11. Exposiciones a instrumentos.
>
> *heredado (encabezado, 2.11.3, p. 21):* 2.11.3. Criterios para considerar una exposición a instrumentos como una acción.
>
> *heredado (intro, 2.11.3, p. 21):* A los fines de determinar si una exposición debe ser tratada como una acción, las en- tidades financieras del grupo 1 deberán tener en cuenta la realidad económica del ins- trumento. Quedan comprendidas:
>
> *propio:* 2.11.3.5. Los títulos de deuda y otros valores, los derivados y los vehículos estructu- rados con el fin de replicar la realidad económica de una acción. Se incluyen las obligaciones cuyo rendimiento esté vinculado al de las ac- ciones, y las acciones contabilizadas como un préstamo que se originen en un canje de deuda por acciones realizado en un proceso de reestructuración de deudas. El requisito de capitales mínimos que se determine para estos úl- timos instrumentos no puede ser menor al que le hubiera correspondido de haber permanecido en la cartera de créditos. A los fines del cumplimiento de estas disposiciones, la SEFYC podrá recate- gorizar las posiciones de deuda como posiciones en acciones si advierte que no se cumplen las condiciones y requisitos que aseguren el adecuado trata- miento de las tenencias. Las inversiones en acciones estructuradas con el objeto de replicar la reali- dad económica de las exposiciones crediticias o de titulizaciones no se con- siderarán acciones.

- tramo del origen: «El requisito de capitales mínimos que se determine para estos últimos instrumentos no puede ser menor al que le hubiera correspondido de haber permanecido en la cartera de créditos» (literal: exacta)
- tramo del destino: —

---

## V072 · `condicion_de` · lote_07, 2 de 10

**Origen** — Condicion «Cumplimiento requisitos punto 5.1.3.1» (`Condicion_cumplimiento_requisitos_punto_5_1_3_1__la_reduccion_de_exigencia_se_aplica_solo__fcca32`)

- descripción: La reducción de exigencia se aplica solo a las entidades que cumplen los requisitos establecidos en el punto 5.1.3.1.

**Predicado** — `condicion_de`

**Destino** — Operacion «Información de reducción de exigencia» (`Operacion_informacion_de_reduccion_de_exigencia__ric_5_1_3_2_dfac4e`)

- descripción: Información de la reducción de exigencia por riesgo crediticio en las partidas 36000001 o 36000004, cuando el límite aplicable sobre el promedio de las exigencias por riesgo crediticio de los 36 meses anteriores resulte inferior al informado en el código 70300000.
- tipo: presentación informativa

**Evidencia 1 de 1** — `ric::5.1.3.2` · ric · punto 5.1.3.2 · punto_propio · págs. 23

- PDF: `data/experiment/subset/TO_regimen_informativo_contable_mensual_actual.pdf#page=23`
- avisos de E0: {"contenido_tabular": true, "formula": true, "evidencia_tabular": ["Ent idad % Partida Cómputo", "A 20 70300000 - [0.20 * ( ERC(n-1) + ... + ERC(n-36)) / 36]", "B 17 70300000 - [0.17 * ( ERC(n-1) + ... + ERC(n-36)) / 36]"], "evidencia_formula": ["donde:", "( ERC + ... + ERC ) / 36 = promedio de las exigencias por riesgo de", "ERC = Partida 70100000 + ∑ 8XX00000"], "tablas_e0": [{"tabla": "ric::tabla015", "origen": "e0_tablas", "estado": "parseada", "paginas": [23], "serializada": true, "bloque": "ric::tabla015", "modo": "columnas", "celdas_propagadas": 1, "celdas_con_alcance": 0, "combinadas_sin_propagar": 0, "filas_subtitulo": 0}]}

> *heredado (encabezado, S5, p. 21):* Sección 5. Exigencia por riesgo operacional
>
> *heredado (encabezado, 5.1, p. 21):* 5.1. Normas de procedimiento
>
> *heredado (encabezado, 5.1.3, p. 23):* 5.1.3. Reducción de la exigencia para entidades financieras del Grupo 2 que pertenezcan a
>
> *heredado (intro, 5.1.3, p. 23):* los Grupos “A”, “B” y “C”.
>
> *propio:* 5.1.3.2. Reducción. Límite general. Se informará la correspondiente reducción de exigencia en las partidas 36000001 ó 36000004 cuando los límites aplicables sobre el promedio de las exigencias por riesgo crediticio de los 36 meses anteriores al bajo informe, resul- te inferior al informado en el código 70300000. Dicho cálculo responderá a la si- guiente expresión: [TABLA ric::tabla015 | página 23 | e0_tablas | columnas] Columnas: Ent idad | % | Partida | Cómputo Fila 1: Ent idad = A | % = 20 | Partida = 36000001 | Cómputo = 36  70300000 - [0.20 * ( ERC(n-1) + ... + ERC(n-36)) / 36] 1 Fila 2: Ent idad = B | % = 17 | Partida = 36000001 ⟨combinada con fila 1⟩ | Cómputo = 36  70300000 - [0.17 * ( ERC(n-1) + ... + ERC(n-36)) / 36] 1 Fila 3: Ent idad = C | % = 14 | Partida = 36000004 | Cómputo = 36  70300000 - [0.14 * ( ERC(n-1) + ... + ERC(n-36)) / 36] 1 [FIN TABLA ric::tabla015] donde: 36 ( ERC + ... + ERC ) / 36 = promedio de las exigencias por riesgo de (n-1) (n-36) 1 crédito correspondientes a los 36 meses anteriores al período a informar, expresadas en moneda homogénea del mes anterior al que se efectúa el cálculo. ERC = Partida 70100000 + ∑ 8XX00000 Esta reducción se aplicará respecto de las entidades que cumplan los requisi- tos aludidos en el punto 5.1.3.1., precedente.

- tramo del origen: «Esta reducción se aplicará respecto de las entidades que cumplan los requisitos aludidos en el punto 5.1.3.1., precedente» (literal: exacta)
- tramo del destino: «Se informará la correspondiente reducción de exigencia en las partidas 36000001 ó 36000004» (literal: exacta)

---

## V073 · `condicion_de` · lote_07, 3 de 10

**Origen** — Condicion «Cancelación de primera cuota de refinanciación» (`Condicion_cancelacion_de_primera_cuota_de_refinanciacion__se_ha_cancelado_la_primera_cuota_e2b368`)

- descripción: Se ha cancelado la primera cuota de la refinanciación

**Predicado** — `condicion_de`

**Destino** — Potestad «Facultad de reclasificar en tratamiento especial» (`Potestad_facultad_de_reclasificar_en_tratamiento_especial__las_entidades_obligadas_a_clas_a54444`)

- descripción: Las entidades obligadas a clasificar pueden reclasificar al cliente en tratamiento especial una única vez, cuando se cumplen las condiciones de primera refinanciación dentro del año y cancelación de la primera cuota

**Evidencia 1 de 1** — `cla::6.5.2.3` · cla · punto 6.5.2.3 · punto_propio · págs. 23

- PDF: `data/experiment/subset/TO_clasificacion_deudores_actual.pdf#page=23`

> *heredado (encabezado, S6, p. 17):* Sección 6. Clasificación de los deudores de la cartera comercial.
>
> *heredado (encabezado, 6.5, p. 19):* 6.5. Niveles de clasificación.
>
> *heredado (intro, 6.5, p. 19):* Cada cliente, y la totalidad de sus financiaciones comprendidas, se incluirá en una de las si- guientes cinco categorías, las que se definen teniendo en cuenta las condiciones que se deta- llan en cada caso. Los clientes que no registren asistencia crediticia de la entidad y que posteriormente reciban fi- nanciaciones de ésta que no superen el importe resultante de aplicar sobre el saldo de deuda registrado en el sistema financiero, según la última información disponible en la “Central de deudores” a la fecha de su otorgamiento, el porcentaje establecido en el punto 2.2.5. de las normas sobre “Previsiones mínimas por riesgo de incobrabilidad” correspondiente a la peor cla- sificación asignada, podrán ser clasificados por la entidad teniendo en cuenta únicamente el análisis del flujo de fondos proyectado. Las asistencias así otorgadas no serán consideradas a los fines a que se refiere el punto 6.6. A fin de verificar el cumplimiento de las obligaciones sin recurrir a nueva financiación directa o indirecta o a refinanciaciones, no se considerarán refinanciaciones las facilidades adicionales que se otorguen respecto de los márgenes vigentes acordados, siempre que el nuevo apoyo crediticio implique nuevos desembolsos de fondos y no supere el 10 % del cupo asignado en oportunidad de la última evaluación crediticia del cliente, en la medida en que éstas sean con- sistentes con el curso normal de los negocios y exista capacidad para atender el resto de las obligaciones financieras, ni las nuevas financiaciones y las refinanciaciones asociadas a una mayor inversión derivada de la expansión de las actividades, y siempre que pueda demostrarse que el flujo de fondos proyectado permitirá afrontar la totalidad de sus obligaciones. Tampoco se considerarán dentro de ese concepto las refinanciaciones otorgadas a los produc- tores agropecuarios cuando ello resulte de la aplicación de disposiciones vinculadas a la Ley de Emergencia Agropecuaria, sin perjuicio de lo cual, a los fines de la clasificación, deberá tenerse en cuenta el flujo de fondos proyectado para el momento en que concluya la vigencia de la emergencia declarada. El tratamiento que se dispense en ese marco no podrá implicar mejora- miento de la clasificación asignada al cliente en función de su situación individual, preexistente a la emergencia, ni su aplicación extenderse más allá de la vigencia fijada para ella.
>
> *heredado (encabezado, 6.5.2, p. 20):* 6.5.2. Con seguimiento especial.
>
> *propio:* 6.5.2.3. En tratamiento especial. Para las refinanciaciones otorgadas por primera vez dentro del año calendario y una vez que se haya cancelado la primera cuota de dicha refinanciación, el clien- te podrá ser reclasificado por única vez en esta situación. Luego de la citada refi- nanciación y a los fines de la clasificación, deberá tenerse en cuenta únicamente la mora en el atraso de sus obligaciones. Para las posteriores refinanciaciones, recibirán el tratamiento general previsto en estas disposiciones.

- tramo del origen: «una vez que se haya cancelado la primera cuota de dicha refinanciación» (literal: exacta)
- tramo del destino: «el cliente podrá ser reclasificado por única vez en esta situación» (literal: exacta)

---

## V074 · `condicion_de` · lote_07, 4 de 10

**Origen** — Condicion «Existencia de calificaciones en moneda nacional» (`Condicion_existencia_de_calificaciones_en_moneda_nacional__cuando_existan_calificaciones_e_5e7e91`)

- descripción: Cuando existan calificaciones en moneda nacional además de las calificaciones en moneda extranjera

**Predicado** — `condicion_de`

**Destino** — Obligacion «Utilizar calificaciones en moneda nacional para exposiciones en moneda nacional» (`Obligacion_las_calificaciones_en_moneda_nacional_se_utilizaran_solamente_para_ponderar_por__9ee8ea`)

- descripción: Las calificaciones en moneda nacional se utilizarán solamente para ponderar por riesgo las exposiciones denominadas en moneda nacional
- tipo: otra

**Evidencia 1 de 1** — `cap::10.3.4` · cap · punto 10.3.4 · punto_propio · págs. 175

- PDF: `data/experiment/subset/TO_capitales_minimos_actual.pdf#page=175`

> *heredado (encabezado, S10, p. 172):* Sección 10. Agentes de calificación externa (ECAI).
>
> *heredado (encabezado, 10.3, p. 173):* 10.3. Consideraciones para su implementación.
>
> *propio:* 10.3.4. Evaluaciones en moneda nacional y en moneda extranjera. Cuando se ponderen por riesgo exposiciones no calificadas sobre la base de la califi- cación de una exposición equivalente con ese mismo prestatario, el criterio general es que las calificaciones en moneda extranjera se utilizarán para ponderar por riesgo las exposiciones en moneda extranjera. Si existieran además calificaciones en moneda nacional, éstas se utilizarán solamente para ponderar por riesgo las exposiciones de- nominadas en esa moneda.

- tramo del origen: «Si existieran además calificaciones en moneda nacional» (literal: exacta)
- tramo del destino: «Si existieran además calificaciones en moneda nacional, éstas se utilizarán solamente para ponderar por riesgo las exposiciones denominadas en esa moneda» (literal: exacta)

---

## V075 · `aplica_a` · lote_07, 5 de 10

**Origen** — Obligacion «Auditoría interna — revisión exhaustiva del esquema de medición» (`Obligacion_la_auditoria_interna_debera_llevar_a_cabo_una_revision_exhaustiva_del_esquema_qu_212218`)

- descripción: La auditoría interna deberá llevar a cabo una revisión exhaustiva del esquema que adopte la entidad para la medición de la exigencia por riesgo de mercado, en especial en cuanto a lo dispuesto en el punto 6.10, dejando constancia de los programas de trabajo e informes que sobre el particular se elaboren.
- tipo: otra

**Predicado** — `aplica_a`

- tramo del sujeto: «la auditoría interna» (literal: exacta)

**Destino** — Sujeto «Comité de auditoría» (`Sujeto_comite_de_auditoria`)

- descripción: —
- nivel: clase

**Evidencia 1 de 1** — `cap::6.12` · cap · punto 6.12 · punto_propio · págs. 144

- PDF: `data/experiment/subset/TO_capitales_minimos_actual.pdf#page=144`

> *heredado (encabezado, S6, p. 116):* Sección 6. Capital mínimo por riesgo de mercado.
>
> *propio:* 6.12. Auditoría interna. La auditoría interna deberá llevar a cabo una revisión exhaustiva del esquema que adopte la entidad para la medición de la exigencia por riesgo de mercado, en especial en cuanto a lo dispuesto en el punto 6.10., dejando constancia de los programas de trabajo e informes que sobre el particular se elaboren. Asimismo, periódicamente deberá efectuar un segui- miento de su correcta aplicación y los cambios que se introduzcan en la medición de dicha exigencia.

- tramo del origen: «La auditoría interna deberá llevar a cabo una revisión exhaustiva del esquema que adopte la entidad para la medición de la exigencia por riesgo de mercado, en especial en cuanto a lo dispuesto en el punto 6.10., dejando constancia de los programas de trabajo e informes que sobre el particular se elaboren.» (literal: exacta)
- tramo del destino: —

---

## V076 · `condicion_de` · lote_07, 6 de 10

**Origen** — Condicion «Cobros correspondan a exportaciones posteriores al registro» (`Condicion_cobros_correspondan_a_exportaciones_posteriores_al_registro__los_cobros_por_apli_60b045`)

- descripción: Los cobros por aplicarse deben corresponder a exportaciones de bienes concretadas con posterioridad al registro de ingreso de los bienes

**Predicado** — `condicion_de`

**Destino** — Operacion «Aplicación de cobros de exportaciones a cancelación de financiación» (`Operacion_aplicacion_de_cobros_de_exportaciones_a_cancelacion_de_financiacion__ext_7_11_2__09c1e5`)

- descripción: Aplicación de cobros de exportaciones de bienes a la cancelación de financiaciones asociadas a importaciones de bienes
- tipo: Aplicación de divisas de cobros de exportaciones

**Evidencia 1 de 1** — `ext::7.11.2.7` · ext · punto 7.11.2.7 · punto_propio · págs. 106

- PDF: `data/experiment/subset/TO_exterior_cambios_actual.pdf#page=106`

> *heredado (encabezado, S7, p. 80):* Sección 7. Cobros de exportaciones de bienes.
>
> *heredado (encabezado, 7.11, p. 103):* 7.11. Financiaciones asociadas a importaciones de bienes habilitadas para la aplicación de cobros
>
> *heredado (intro, 7.11, p. 103):* de exportaciones de bienes.
>
> *heredado (encabezado, 7.11.2, p. 104):* 7.11.2. La aplicación de las divisas a las operaciones señaladas será admitida en la medida
>
> *heredado (intro, 7.11.2, p. 104):* que se verifiquen la totalidad de las siguientes condiciones:
>
> *heredado (cierre, 7.11.2, p. 106):* La entidad deberá verificar los requisitos habituales a los efectos de certificar la aplicación de divisas a la cancelación de la financiación.
>
> *propio:* 7.11.2.7. Los cobros por aplicarse correspondan a exportaciones de bienes concretadas con posterioridad al registro de ingreso de los bienes. En el caso de operaciones comprendidas en el punto 7.11.1.6. también se admitirá la cancelación de intereses mediante la aplicación de cobros de exportaciones de bienes concretadas a partir de la fecha en que se completó el ingreso de la financiación.

- tramo del origen: «Los cobros por aplicarse correspondan a exportaciones de bienes concretadas con posterioridad al registro de ingreso de los bienes» (literal: exacta)
- tramo del destino: «la aplicación de cobros de exportaciones de bienes» (literal: exacta)

---

## V077 · `regula` · lote_07, 7 de 10

**Origen** — Obligacion «Tasación independiente del inmueble» (`Obligacion_el_valor_del_inmueble_debe_ser_resultado_de_una_tasacion_que_se_realice_en_forma_510a9a`)

- descripción: El valor del inmueble debe ser resultado de una tasación que se realice en forma independiente respecto de quienes participan de los procesos de otorgamiento del crédito.
- tipo: otra

**Predicado** — `regula`

**Destino** — Operacion «Cálculo prudente del LTV» (`Operacion_calculo_prudente_del_ltv__cap_2_9_2_3_bce3f2`)

- descripción: Cálculo de la relación entre el saldo de deuda pendiente y el valor del inmueble (LTV) de manera prudente y conforme a requisitos específicos.
- tipo: cálculo

**Evidencia 1 de 1** — `cap::2.9.2.3` · cap · punto 2.9.2.3 · punto_propio · págs. 19

- PDF: `data/experiment/subset/TO_capitales_minimos_actual.pdf#page=19`

> *heredado (encabezado, S2, p. 7):* Sección 2. Capital mínimo por riesgo de crédito.
>
> *heredado (chapeau_seccion, S2, p. 7):* A los efectos de la aplicación de las disposiciones de la presente sección, las entidades financieras se clasificarán en: i)Grupo 1: entidades calificadas por el BCRA como de importancia sistémica a nivel local
>
> *heredado (chapeau_seccion, S2, p. 7):* (D-SIB) y sucursales o subsidiarias de bancos del exterior calificados como de impor- tancia sistémica global (G-SIB).
>
> *heredado (chapeau_seccion, S2, p. 7):* ii) Grupo 2: entidades financieras no comprendidas en el acápite i). En aquellos casos en que no se establezcan disposiciones específicas para cada uno de los citados grupos de entidades financieras, deberá aplicarse el mismo tratamiento a ambos grupos. Las entidades financieras que presenten cambios en su calificación –conforme a lo previsto en los acápites precedentes–, contarán con un plazo de 6 meses para aplicar las disposiciones específicas correspondientes al nuevo grupo al que pertenezcan.
>
> *heredado (encabezado, 2.9, p. 18):* 2.9. Exposiciones con garantía hipotecaria.
>
> *heredado (encabezado, 2.9.2, p. 18):* 2.9.2. Exposiciones con garantía hipotecaria normativas. Requisitos.
>
> *propio:* 2.9.2.3. La relación entre el saldo de deuda y el valor del inmueble (loan-to-value, LTV) se deberá calcular de manera prudente y con ajuste a los siguientes requisitos: i) El saldo de deuda pendiente se compute sin deducir previsiones por riesgo de incobrabilidad ni coberturas del riesgo de crédito previstas en la Sección 5. ii) El valor del inmueble se corresponda al del momento del otorgamiento, ex- cepto que: a) Se realicen ajustes por razones objetivas. b) El BCRA establezca que se debe hacer una reducción generalizada del valor. Si posteriormente se autorizan incrementos, el valor ajustado del inmueble no podrá superar el valor considerado en oportunidad del otorgamiento del crédito debidamente actualizado. c) Se produzca un evento idiosincrásico y extraordinario del que resulte una reducción permanente del valor del inmueble. d) Se realicen mejoras de carácter permanente en el inmueble que in- crementen su valor en forma indubitable. iii) El valor del inmueble sea el resultado de una tasación que cumpla los si- guientes criterios: a) se ajuste a una valuación conservadora; b) se realice en forma independiente respecto de quienes participan de los procesos de otorgamiento del crédito; c) no se base en la expectativa de que se incrementará el precio del in- mueble; d) no resulte mayor al precio de mercado; e) no sea mayor al precio de adquisición –en los casos en que el présta- mo con garantía hipotecaria financie la compra del inmueble hipoteca- do–, contemplando lo dispuesto en el acápite ii), inciso a); y f) no dependa de la situación económica del prestatario.

- tramo del origen: «se realice en forma independiente respecto de quienes participan de los procesos de otorgamiento del crédito» (literal: exacta)
- tramo del destino: «La relación entre el saldo de deuda y el valor del inmueble (loan-to-value, LTV) se deberá calcular de manera prudente» (literal: exacta)

---

## V078 · `aplica_a` · lote_07, 8 de 10

**Origen** — Obligacion «Informar origen incremento cartera irregular a SEFyC» (`Obligacion_la_entidad_financiera_debe_informar_a_la_sefyc_el_origen_del_incremento_de_la_ca_a325e0`)

- descripción: La entidad financiera debe informar a la SEFyC el origen del incremento de la cartera irregular cuando se supera el 5 % trimestral o el 10 % anual.
- tipo: reporte_al_supervisor
- umbrales (2):
  - valor: 5; unidad: porcentaje; comparacion: minimo_estricto; tramo: 5 %
  - valor: 10; unidad: porcentaje; comparacion: no_determinada; tramo: 10 %

**Predicado** — `aplica_a`

- tramo del sujeto: «la entidad financiera» (literal: exacta)

**Destino** — Sujeto «Entidades financieras» (`Sujeto_entidad_financiera`)

- descripción: —
- nivel: clase
- alias: ["Entidades financieras emisoras de tarjetas de crédito y/o compra", "Entidad financiera emisora de tarjetas de crédito y/o compra"]

**Evidencia 1 de 1** — `cla::7.4` · cla · punto 7.4 · punto_propio · págs. 39, 40

- PDF: `data/experiment/subset/TO_clasificacion_deudores_actual.pdf#page=39` · `data/experiment/subset/TO_clasificacion_deudores_actual.pdf#page=40`

> *heredado (encabezado, S7, p. 33):* Sección 7. Clasificación de los deudores de la cartera para consumo o vivienda.
>
> *propio:* 7.4. Información a la SEFyC sobre incrementos de la cartera irregular. En los casos en que la expresión que seguidamente se establece sea mayor al 5 % al último día de un trimestre calendario o al 10 % en un año, la entidad financiera deberá informar el ori- gen de dicha circunstancia a la SEFyC debiendo brindar las explicaciones que les sean reque- ridas y, de corresponder, las modificaciones a realizar en su política de crédito tendientes a me- jorar la calidad de su cartera crediticia. FICC - FICC - Máx (FICCS - FICCS ; 0) T T-1 T T-1 Siendo: FICC: cociente, expresado en tanto por ciento, entre el importe total de las financiaciones de la cartera de consumo o vivienda, de la entidad financiera, clasificadas en situación 3 a 5 según las normas sobre “Clasificación de deudores” y el importe total de sus finan- ciaciones de la cartera de consumo o vivienda. FICCS: cociente, expresado en tanto por ciento, entre el importe total de las financiaciones de la cartera de consumo o vivienda, del total del sistema financiero, clasificadas en si- tuación 3 a 5 según las normas sobre “Clasificación de deudores” y el importe total de sus financiaciones de la cartera de consumo o vivienda, según la información que dé a conocer el BCRA. T: el último día de un trimestre calendario al que corresponda el cálculo del cociente. T-1: el último día del trimestre calendario inmediato anterior y el último día del mismo tri- mestre correspondiente al año anterior, según corresponda.

- tramo del origen: «la entidad financiera deberá informar el origen de dicha circunstancia a la SEFyC» (literal: exacta)
- tramo del destino: —

---

## V079 · `condicion_de` · lote_07, 9 de 10

**Origen** — Condicion «Financiaciones en pesos 01/11/24 a 10/04/26» (`Condicion_financiaciones_en_pesos_01_11_24_a_10_04_26__financiaciones_en_pesos_que_se_acue_48de5c`)

- descripción: Financiaciones en pesos que se acuerden a partir del 1 de noviembre de 2024 y hasta el 10 de abril de 2026
- umbrales (1):
  - comparacion: maximo_inclusivo; tramo: a partir del 01/11/24 y hasta el 10/04/26

**Predicado** — `condicion_de`

**Destino** — Restriccion «Factor multiplicador 4 — capital mínimo riesgo crédito» (`Restriccion_el_importe_resultante_de_aplicar_lo_dispuesto_en_la_seccion_2_debera_ser_multipl_67b85a`)

- descripción: El importe resultante de aplicar lo dispuesto en la Sección 2 deberá ser multiplicado por un factor igual a 4 para determinar la exigencia de capital mínimo por riesgo de crédito
- tipo: limite_cuantitativo
- umbrales (1):
  - comparacion: no_determinada; tramo: factor igual a 4

**Evidencia 1 de 1** — `cap::11.5` · cap · punto 11.5 · punto_propio · págs. 176

- PDF: `data/experiment/subset/TO_capitales_minimos_actual.pdf#page=176`

> *heredado (encabezado, S11, p. 176):* Sección 11. Otras disposiciones.
>
> *propio:* 11.5. A los efectos de determinar la exigencia de capital mínimo por riesgo de crédito, el importe resultante de aplicar lo dispuesto en la Sección 2. deberá ser multiplicado por un factor igual a 4 de tratarse de financiaciones a clientes con actividad agrícola que no sean Mipyme y man- tengan un acopio de su producción por un valor superior al 5% de su capacidad de cosecha anual, según lo siguiente: – Financiaciones acordadas a partir del 18/05/2020 y hasta el 31/10/24. – Financiaciones en pesos que se acuerden a partir del 01/11/24 y hasta el 10/04/26.

- tramo del origen: «Financiaciones en pesos que se acuerden a partir del 01/11/24 y hasta el 10/04/26» (literal: exacta)
- tramo del destino: «el importe resultante de aplicar lo dispuesto en la Sección 2. deberá ser multiplicado por un factor igual a 4» (literal: exacta)

---

## V080 · `condicion_de` · lote_07, 10 de 10

**Origen** — Condicion «Ubicación bajo media sector con dificultades competencia» (`Condicion_ubicacion_bajo_media_sector_con_dificultades_competencia__el_cliente_se_encuentr_d4c5f6`)

- descripción: El cliente se encuentra ubicado bajo la media del sector con dificultades para enfrentar la competencia y con problemas leves en materia de adecuación a la tecnología

**Predicado** — `condicion_de`

**Destino** — Operacion «Clasificación de deudor en categoría Con problemas» (`Operacion_clasificacion_de_deudor_en_categoria_con_problemas__cla_6_5_3_9_4aa3d2`)

- descripción: Clasificación del cliente en la categoría 'Con problemas' cuando se encuentre ubicado bajo la media del sector con dificultades para enfrentar la competencia y con problemas leves en materia de adecuación a la tecnología, y presente problemas en su relación con proveedores y clientes
- tipo: Clasificación de deudor

**Evidencia 1 de 1** — `cla::6.5.3.9` · cla · punto 6.5.3.9 · punto_propio · págs. 25

- PDF: `data/experiment/subset/TO_clasificacion_deudores_actual.pdf#page=25`

> *heredado (encabezado, S6, p. 17):* Sección 6. Clasificación de los deudores de la cartera comercial.
>
> *heredado (encabezado, 6.5, p. 19):* 6.5. Niveles de clasificación.
>
> *heredado (intro, 6.5, p. 19):* Cada cliente, y la totalidad de sus financiaciones comprendidas, se incluirá en una de las si- guientes cinco categorías, las que se definen teniendo en cuenta las condiciones que se deta- llan en cada caso. Los clientes que no registren asistencia crediticia de la entidad y que posteriormente reciban fi- nanciaciones de ésta que no superen el importe resultante de aplicar sobre el saldo de deuda registrado en el sistema financiero, según la última información disponible en la “Central de deudores” a la fecha de su otorgamiento, el porcentaje establecido en el punto 2.2.5. de las normas sobre “Previsiones mínimas por riesgo de incobrabilidad” correspondiente a la peor cla- sificación asignada, podrán ser clasificados por la entidad teniendo en cuenta únicamente el análisis del flujo de fondos proyectado. Las asistencias así otorgadas no serán consideradas a los fines a que se refiere el punto 6.6. A fin de verificar el cumplimiento de las obligaciones sin recurrir a nueva financiación directa o indirecta o a refinanciaciones, no se considerarán refinanciaciones las facilidades adicionales que se otorguen respecto de los márgenes vigentes acordados, siempre que el nuevo apoyo crediticio implique nuevos desembolsos de fondos y no supere el 10 % del cupo asignado en oportunidad de la última evaluación crediticia del cliente, en la medida en que éstas sean con- sistentes con el curso normal de los negocios y exista capacidad para atender el resto de las obligaciones financieras, ni las nuevas financiaciones y las refinanciaciones asociadas a una mayor inversión derivada de la expansión de las actividades, y siempre que pueda demostrarse que el flujo de fondos proyectado permitirá afrontar la totalidad de sus obligaciones. Tampoco se considerarán dentro de ese concepto las refinanciaciones otorgadas a los produc- tores agropecuarios cuando ello resulte de la aplicación de disposiciones vinculadas a la Ley de Emergencia Agropecuaria, sin perjuicio de lo cual, a los fines de la clasificación, deberá tenerse en cuenta el flujo de fondos proyectado para el momento en que concluya la vigencia de la emergencia declarada. El tratamiento que se dispense en ese marco no podrá implicar mejora- miento de la clasificación asignada al cliente en función de su situación individual, preexistente a la emergencia, ni su aplicación extenderse más allá de la vigencia fijada para ella.
>
> *heredado (encabezado, 6.5.3, p. 23):* 6.5.3. Con problemas.
>
> *heredado (intro, 6.5.3, p. 23):* El análisis del flujo de fondos del cliente demuestra que tiene problemas para atender normalmente la totalidad de sus compromisos financieros y que, de no ser corregidos, esos problemas pueden resultar en una pérdida para la entidad financiera. Entre los indicadores que pueden reflejar esta situación se destacan que el cliente:
>
> *propio:* 6.5.3.9. Se encuentre ubicado bajo la media del sector con dificultades para enfrentar la competencia y con problemas leves en materia de adecuación a la tecnología. Presente problemas en su relación con proveedores y clientes.

- tramo del origen: «Se encuentre ubicado bajo la media del sector con dificultades para enfrentar la competencia y con problemas leves en materia de adecuación a la tecnología» (literal: exacta)
- tramo del destino: «Se encuentre ubicado bajo la media del sector con dificultades para enfrentar la competencia y con problemas leves en materia de adecuación a la tecnología. Presente problemas en su relación con proveedores y clientes» (literal: exacta)

---

