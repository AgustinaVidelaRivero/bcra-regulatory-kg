# U-REEXT-T0, T3-bis: declaraciones de la decisión 5 y listas del freno

Grafos: diez `a9631a64b422bdae634fb05135373c6f04c6272cdf7acd43a1be9f5b6c1f5f57`, desarrollo `6e7560433148cfe0c476cdd61199c32278187c4196d6f90dc0a38976a6d8e9a2`. Textos de la norma: E0 r2b (`salida_tanda0_r2b`), con los saltos de línea colapsados. Lo generó `data/experiment/reext_t0/t3bis/declaraciones_t3bis.py`.

## RT-C6-1 y RT-C6-2: siguen en persiste, declarados

Declaración: error de fidelidad del modelo en la descripción, conector «o» → «y»; tramo fiel.

- Norma (`pro::1.1.2.5`): «1.1.2.5. Otros proveedores no financieros de crédito alcanzados por las normas sobre “Proveedores no financieros de crédito”, excepto que se trate de asociaciones mutuales o cooperativas, por las financiaciones que otorguen.»
- Excepcion `Excepcion_quedan_exceptuadas_del_alcance_de_las_normas_sobre_proveedores_no_financieros_de_f8a3ba`, descripción: «Quedan exceptuadas del alcance de las normas sobre proveedores no financieros de crédito las asociaciones mutuales y cooperativas, en lo que respecta a las financiaciones que otorguen.»
- Su tramo: «excepto que se trate de asociaciones mutuales o cooperativas»
- Definicion del mismo chunk, descripción: «Proveedores no financieros de crédito que están alcanzados por las normas sobre protección de usuarios, con excepción de asociaciones mutuales o cooperativas, en lo que respecta a las financiaciones que otorguen.»
- Suite (diez y desarrollo): RT-C6-1 «persiste» (RT-C6-1: sin Excepcion anclada en pro 1.1.2.5 con «mutuales o cooperativas»); RT-C6-2 «persiste».

## RT-C5-3: sigue en persiste, declarado

Declaración: persiste por paráfrasis sin cambio de sentido (el ítem compara literalmente un gold escrito para la extracción textual).

- Norma (`cla::6.5.2.2`): «Incluye aquellos clientes que ante la imposibilidad de hacer frente al pago de sus obligaciones en las condiciones pactadas, manifiesten fehacientemente antes de los 60 días contados desde la fecha en que se verificó la mora en el pago de las obligaciones, la intención de refinanciar sus deudas, observando los demás indi- cadores pertinentes del punto 6.5.2.1.»
- Gold del ítem (`scripts/regression_kg.py`, `t_rt_c5_3`): «antes de los 60 dias» y «mora», en el texto normalizado del nodo N5.
- Definicion `Definicion_categoria_en_negociacion_o_con_acuerdos_de_refinanciacion__categoria_que_incluye_89a265`, descripción: «Categoría que incluye clientes que ante imposibilidad de pagar en condiciones pactadas manifiesten fehacientemente antes de 60 días desde la mora la intención de refinanciar, observando indicadores del punto 6.5.2.1»
- Su tramo: «Incluye aquellos clientes que ante la imposibilidad de hacer frente al pago de sus obligaciones en las condiciones pactadas, manifiesten fehacientemente antes de los 60 días contados desde la fecha en que se verificó la mora en el pago de las obligaciones, la intención de refinanciar sus deudas, observando los demás indicadores pertinentes del punto 6.5.2.1.»
- Suite: «persiste» (N5 ['Definicion_categoria_en_negociacion_o_con_acuerdos_de_refinanciacion__ca']: gold 1/2; faltan ['antes de los 60 dias']).

## S18: Restricciones limite_cuantitativo con la marca r2b `umbral_no_cuantificable`

La marca va en `properties_no_definidas` (NodoR2 y S26 cierran las claves de `properties`). Lista: `ens_<grafo>_r2b/r2/umbral_no_cuantificable.json`.

- diez: 14 marcados (sin cuantía detectable: 13, cuantías solo en tabla residual forzada: 1); sin marca con cuantía: 0; detector `69c48d24387b…`; lista de tablas forzadas `98cc96b2fec4…`.
- desarrollo: 13 marcados (sin cuantía detectable: 12, cuantías solo en tabla residual forzada: 1); sin marca con cuantía: 0; detector `69c48d24387b…`; lista de tablas forzadas `98cc96b2fec4…`.

  - `Restriccion_cuando_la_suma_de_los_requisitos_de_capital_de_una_entidad_financiera_por_exposi_74a15c` (cap::4.3.3.2; sin cuantía detectable): «Cuando la suma de los requisitos de capital de una entidad financiera por exposiciones con una QCCP originadas en operaciones y aportes al fondo de garantía sea mayor que la exigencia del punto 4.3.4, se toma este último importe como requisito de capital.»
  - `Restriccion_el_monto_de_las_certificaciones_de_aumento_de_exportaciones_de_bienes_emitidas_d_769ce0` (ext::3.17.3.4; sin cuantía detectable): «El monto de las certificaciones de aumento de exportaciones de bienes emitidas debe considerarse como concepto a deducir del monto acumulado de beneficios totales reconocidos al cliente por la Secretaría de Energía, en el marco del Decreto 277/22»
  - `Restriccion_en_el_caso_de_una_extraccion_con_una_tarjeta_prepaga_sera_de_aplicacion_el_limit_7282fd` (ext::4.1.1; sin cuantía detectable): «En el caso de una extracción con una tarjeta prepaga, será de aplicación el límite dispuesto para operaciones en efectivo.»
  - `Restriccion_exigencia_adicional_de_capital_para_la_cobertura_del_riesgo_gamma_que_mide_la_ta_72fa25` (cap::6.6.3::intro; sin cuantía detectable): «Exigencia adicional de capital para la cobertura del riesgo gamma, que mide la tasa de cambio del coeficiente delta ante variaciones en el precio del subyacente.»
  - `Restriccion_exigencia_adicional_de_capital_para_la_cobertura_del_riesgo_vega_que_mide_la_sen_0616b8` (cap::6.6.3::intro; sin cuantía detectable): «Exigencia adicional de capital para la cobertura del riesgo vega, que mide la sensibilidad del precio de la opción a los cambios en la volatilidad del precio del subyacente.»
  - `Restriccion_la_exigencia_de_capital_minimo_por_riesgo_operacional_determinada_mediante_la_ex_3c9f4e` (cap::7.3::intro; sin cuantía detectable): «La exigencia de capital mínimo por riesgo operacional determinada mediante la expresión del punto 7.2 no podrá superar un límite máximo (cuantía a especificar en los ítems siguientes).»
  - `Restriccion_la_exposicion_maxima_frente_a_una_misma_contraparte_individual_no_debera_superar_f97a2c` (cap::2.8.3.3; sin cuantía detectable): «La exposición máxima frente a una misma contraparte individual no deberá superar, al momento del acuerdo, los siguientes importes especificados según la categoría de deudor.»
  - `Restriccion_las_compensaciones_horizontales_estan_sujetas_a_una_escala_de_desestimaciones_ho_8791ea` (cap::6.2.2.6; cuantías solo en tabla residual forzada; tablas: cap::tabla037): «Las compensaciones horizontales están sujetas a una escala de desestimaciones horizontales (exigencias adicionales) expresadas como porcentajes de las posiciones que se compensan, según la zona y banda temporal»
  - `Restriccion_las_entidades_financieras_situadas_en_cualquiera_de_las_posiciones_de_una_operac_3aa950` (cap::5.2.2.4; sin cuantía detectable): «Las entidades financieras situadas en cualquiera de las posiciones de una operación garantizada con un activo (tales como operaciones de pase y préstamos/endeudamiento en valores entre un cliente y un tercero) deberán cumplir con un requerimiento de capital, incluso cuando actúen como agente en la organización de la operación y garanticen a un cliente que un tercero cumplirá con sus obligaciones.»
  - `Restriccion_las_opciones_y_sus_subyacentes_al_contado_o_a_termino_estan_sujetas_a_una_exigen_63036d` (cap::6.6.2::intro; sin cuantía detectable): «Las opciones y sus subyacentes, al contado o a término, están sujetas a una exigencia de capital que incorpora tanto el riesgo de mercado general como el riesgo específico»
  - `Restriccion_las_operaciones_de_titulizacion_que_incluyan_una_opcion_de_exclusion_que_no_cump_03ec35` (cap::3.1.4::cierre; sin cuantía detectable): «Las operaciones de titulización que incluyan una opción de exclusión que no cumpla la totalidad de los criterios indicados precedentemente resultarán en una exigencia de capital para la entidad originante»
  - `Restriccion_los_rechazos_de_cheques_generaran_las_multas_legalmente_establecidas_segun_se_co_17f64d` (ctacte::6.5::intro; sin cuantía detectable): «Los rechazos de cheques generarán las multas legalmente establecidas, según se consigna a continuación»
  - `Restriccion_partidas_fuera_de_balance_que_refieren_a_compromisos_se_sujetan_al_menor_de_los__da643f` (cap::2.13; sin cuantía detectable): «Partidas fuera de balance que refieren a compromisos se sujetan al menor de los CCF que resulten aplicables.»
  - `Restriccion_si_el_cliente_es_beneficiario_directo_del_decreto_277_22_el_valor_de_los_benefic_e67451` (ext::3.4.4.5; sin cuantía detectable): «Si el cliente es beneficiario directo del Decreto 277/22, el valor de los beneficios del decreto utilizados por el cliente, en forma directa o indirecta, debe ser deducido del monto que se habilita para el giro de utilidades.»
  - En desarrollo, los mismos salvo `Restriccion_los_rechazos_de_cheques_generaran_las_multas_legalmente_establecidas_segun_se_co_17f64d` (TO fuera de desarrollo).

## BKL-0039: no cierra (prefijo congelado; a la lista de T5)

- Norma (`ctacte::6.4.7::intro`, texto propio de la unidad): «a las presentes disposiciones, se observará el siguiente proceso:»
- Obligacion `Obligacion_cuando_sea_necesario_modificar_las_comunicaciones_de_rechazo_efectuadas_con_suje_d57f0f`, descripción: «Cuando sea necesario modificar las comunicaciones de rechazo efectuadas con sujeción a las presentes disposiciones, se observará el siguiente proceso.»; tramo: «se observará el siguiente proceso»

## BKL-0036: cerrada, con la condición releída sin atarla al tipo (la Restriccion conserva el calificador)

- Norma (`lingob::2.3.2.2`): «2.3.2.2. Operar con sus directores y administradores y con empresas o personas vincu- ladas con ellos –en los términos previstos en el punto 1.2.2. de las normas so- bre “Grandes exposiciones al riesgo de crédito”–, en condiciones más favora- bles que las acordadas de ordinario a su clientela.»
- Restriccion `Restriccion_no_se_podra_operar_con_directores_administradores_y_empresas_o_personas_vinculad_42f9c1`, descripción: «No se podrá operar con directores, administradores y empresas o personas vinculadas con ellos en condiciones más favorables que las acordadas de ordinario a la clientela, conforme a los términos previstos en el punto 1.2.2. de las normas sobre Grandes exposiciones al riesgo de crédito.»
- Su tramo: «Operar con sus directores y administradores y con empresas o personas vinculadas con ellos –en los términos previstos en el punto 1.2.2. de las normas sobre "Grandes exposiciones al riesgo de crédito"–, en condiciones más favorables que las acordadas de ordinario a su clientela»

## BKL-0028: a U-RERESOL-CAT

- Sin cambio en estos grafos: el miembro del rol de ctacor se re-adjudica en U-RERESOL-CAT.

## BKL-0021: opción (c) por U-RERESOL-CAT; mientras tanto, (d): los dos propuestos siguen en cuarentena

- diez: `Sujeto_propuesto_la_entidad_nominada` («La entidad nominada», padre_sugerido `Sujeto_entidad_financiera`): 2 aplica_a (ext::11.1.1.10 desde «Emitir certificaciones a pedido del importador», mención «la entidad nominada»; ext::3.18.2::intro desde «Facultad de emitir certificación», mención «La entidad nominada»); 2 filas (ext::3.18.2::intro cuarentena sin_match; ext::11.1.1.10 cuarentena sin_match)
- diez: `Sujeto_propuesto_la_entidad_nominada_por_el_exportador` («la entidad nominada por el exportador», padre_sugerido `Sujeto_rol_entidad_autorizada_exterior`): 2 aplica_a (ext::7.3::intro desde «Incorporación al seguimiento — número ECO», mención «la entidad nominada por el exportador»; ext::7.3.7 desde «Presentar pedidos de conformidad ante BCRA por entidad nominada», mención «la entidad nominada por el exportador»); 2 filas (ext::7.3::intro cuarentena sin_match; ext::7.3.7 cuarentena sin_match)
- desarrollo: `Sujeto_propuesto_la_entidad_nominada` («La entidad nominada», padre_sugerido `Sujeto_entidad_financiera`): 2 aplica_a (ext::11.1.1.10 desde «Emitir certificaciones a pedido del importador», mención «la entidad nominada»; ext::3.18.2::intro desde «Facultad de emitir certificación», mención «La entidad nominada»); 2 filas (ext::3.18.2::intro cuarentena sin_match; ext::11.1.1.10 cuarentena sin_match)
- desarrollo: `Sujeto_propuesto_la_entidad_nominada_por_el_exportador` («la entidad nominada por el exportador», padre_sugerido `Sujeto_rol_entidad_autorizada_exterior`): 2 aplica_a (ext::7.3::intro desde «Incorporación al seguimiento — número ECO», mención «la entidad nominada por el exportador»; ext::7.3.7 desde «Presentar pedidos de conformidad ante BCRA por entidad nominada», mención «la entidad nominada por el exportador»); 2 filas (ext::7.3::intro cuarentena sin_match; ext::7.3.7 cuarentena sin_match)

## T5: sin casos (la arista de `ext::3.17.2::intro` sigue al texto)

- Norma (`ext::3.17.2::intro`): «petróleo (RADPIP) y/o Régimen de acceso a divisas para la producción incremental de gas natural (RADPIGN) deberán nominar una única entidad financiera local que será la responsable de emitir las “certificaciones por los regímenes de acceso a divisas para la producción incremental de petróleo y/o gas natural (Decreto 277/22)” y remitirlas a las entidades por las cuales el cliente desee acceder al mercado de cambios. En caso de que el cliente sea un beneficiario directo del Decreto 277/22, para quedar habilitada para emitir las certificaciones la entidad también deberá estar nominada por el cliente como responsable de:»
- `Obligacion_la_entidad_financiera_nominada_debe_emitir_las_certificaciones_por_los_regimenes_017bc1` («Emitir y remitir certificaciones de acceso a divisas») --aplica_a--> `Sujeto_entidad_financiera`, mención «la entidad financiera nominada», tramo del origen «será la responsable de emitir las "certificaciones por los regímenes de acceso a divisas para la producción incremental de petróleo y/o gas natural (Decreto 277/22)" y remitirlas a las entidades por las cuales el cliente desee acceder al mercado de cambios»
- `Obligacion_para_quedar_habilitada_a_emitir_las_certificaciones_la_entidad_financiera_debe_e_d9e269` («Estar nominada como responsable de funciones adicionales») --aplica_a--> `Sujeto_entidad_financiera`, mención «la entidad», tramo del origen «para quedar habilitada para emitir las certificaciones la entidad también deberá estar nominada por el cliente como responsable de»

## remite_a: no se toca

- Según la nota del 06/10/2026 al pie del mandato (`07ef3c9`): sobre el texto propio de las 2.439 unidades el detector del perfil r2 encuentra 1.385 citas; r2b registra 1.380 y deja 5 sin registrar. Se declaran, no se corrigen. Aristas `remite_a` en T3-bis: diez 13380, desarrollo 12318.

## Propuestos (decisión 1): los 7 sin padre de T3, el padre hacia una instancia, los renombrados y los descartados

- diez:
  - «cada una» (`Sujeto_propuesto_cada_una`, ext; padre_sugerido de E1: `None`): descartado por mención vacía; 1 arista quitada, 1 fila con estado «descartado».
  - «se» (`Sujeto_propuesto_se`, cap; padre_sugerido de E1: `Sujeto_sefyc`): descartado por mención vacía; 1 arista quitada, 1 fila con estado «descartado».
  - «Dichas evaluaciones» (`Sujeto_propuesto_dichas_evaluaciones`): padre_por_defecto → `Sujeto_rol_alcance_capmin`.
  - «la entidad» (`Sujeto_propuesto_la_entidad`): padre_por_defecto → `Sujeto_rol_alcance_capmin`.
  - «la entidad encargada del "Seguimiento de anticipos y otras financiaciones de exportación de bienes"» (`Sujeto_propuesto_la_entidad_encargada_del_seguimiento_de_anticipos_y_otras_financiaciones_de_expo`): padre_por_defecto → `Sujeto_rol_entidad_autorizada_exterior`.
  - «la entidad que cursó la operación de canje y/o arbitraje» (`Sujeto_propuesto_la_entidad_que_curso_la_operacion_de_canje_y_o_arbitraje`): padre_por_defecto → `Sujeto_rol_entidad_autorizada_exterior`.
  - «Los casos» (`Sujeto_propuesto_los_casos`): padre_por_defecto → `Sujeto_rol_entidad_autorizada_exterior`.
  - «los cobros de exportaciones» (`Sujeto_propuesto_los_cobros_de_exportaciones`): padre_por_defecto → `Sujeto_rol_entidad_autorizada_exterior`.
  - Padre hacia una instancia: 0 después del descarte (el único caso de T3, «se» → `Sujeto_sefyc`, salió con el propuesto).
  - `Sujeto_propuesto_la_entidad__ctacte`: 1 fila pasa de `Sujeto_propuesto_la_entidad` a este id (ctacte; ctacte::1.5.2.9).
  - `Sujeto_propuesto_la_entidad__ext`: 14 filas pasan de `Sujeto_propuesto_la_entidad` a este id (ext; ext::10.3.3, ext::3.11.5, ext::4.4.2, ext::7.8.3, ext::7.9.4, ext::8.4.5).
  - Aristas quitadas: 2 (`ens_diez_r2b/r2/propuestos_descartados_aristas_quitadas.jsonl`, insumo de R2 de U-RERESOL-CAT; sin rol asignado):
    - TO_exterior_cambios_actual.pdf `ext::7.3.11` (punto 7.3.11): «cada una» (exacta), aplica_a desde `Obligacion_cuando_la_operacion_ha_sido_liquidada_por_mas_de_una_entidad_cada_una_puede_cert_cc744f`; tramo del origen «En caso de que la operación haya sido liquidada por más de una entidad, cada una podrá certificar la aplicación de la porción no liquidada en proporción a su participación en la porción liquidada».
    - TO_capitales_minimos_actual.pdf `cap::12.3` (punto 12.3): «se» (exacta), aplica_a desde `Obligacion_se_considerara_la_ultima_calificacion_informada_para_el_calculo_de_la_exigencia__768b58`; tramo del origen «A este efecto, se considerará la última calificación informada para el cálculo de la exigencia que corresponda integrar al tercer mes siguiente a aquel en que tenga lugar la notificación».
- desarrollo:
  - «cada una» (`Sujeto_propuesto_cada_una`, ext; padre_sugerido de E1: `None`): descartado por mención vacía; 1 arista quitada, 1 fila con estado «descartado».
  - «se» (`Sujeto_propuesto_se`, cap; padre_sugerido de E1: `Sujeto_sefyc`): descartado por mención vacía; 1 arista quitada, 1 fila con estado «descartado».
  - «Dichas evaluaciones» (`Sujeto_propuesto_dichas_evaluaciones`): padre_por_defecto → `Sujeto_rol_alcance_capmin`.
  - «la entidad» (`Sujeto_propuesto_la_entidad`): padre_por_defecto → `Sujeto_rol_alcance_capmin`.
  - «la entidad encargada del "Seguimiento de anticipos y otras financiaciones de exportación de bienes"» (`Sujeto_propuesto_la_entidad_encargada_del_seguimiento_de_anticipos_y_otras_financiaciones_de_expo`): padre_por_defecto → `Sujeto_rol_entidad_autorizada_exterior`.
  - «la entidad que cursó la operación de canje y/o arbitraje» (`Sujeto_propuesto_la_entidad_que_curso_la_operacion_de_canje_y_o_arbitraje`): padre_por_defecto → `Sujeto_rol_entidad_autorizada_exterior`.
  - «Los casos» (`Sujeto_propuesto_los_casos`): padre_por_defecto → `Sujeto_rol_entidad_autorizada_exterior`.
  - «los cobros de exportaciones» (`Sujeto_propuesto_los_cobros_de_exportaciones`): padre_por_defecto → `Sujeto_rol_entidad_autorizada_exterior`.
  - Padre hacia una instancia: 0 después del descarte (el único caso de T3, «se» → `Sujeto_sefyc`, salió con el propuesto).
  - `Sujeto_propuesto_la_entidad__ext`: 14 filas pasan de `Sujeto_propuesto_la_entidad` a este id (ext; ext::10.3.3, ext::3.11.5, ext::4.4.2, ext::7.8.3, ext::7.9.4, ext::8.4.5).
  - Aristas quitadas: 2 (`ens_desarrollo_r2b/r2/propuestos_descartados_aristas_quitadas.jsonl`, insumo de R2 de U-RERESOL-CAT; sin rol asignado):
    - TO_exterior_cambios_actual.pdf `ext::7.3.11` (punto 7.3.11): «cada una» (exacta), aplica_a desde `Obligacion_cuando_la_operacion_ha_sido_liquidada_por_mas_de_una_entidad_cada_una_puede_cert_cc744f`; tramo del origen «En caso de que la operación haya sido liquidada por más de una entidad, cada una podrá certificar la aplicación de la porción no liquidada en proporción a su participación en la porción liquidada».
    - TO_capitales_minimos_actual.pdf `cap::12.3` (punto 12.3): «se» (exacta), aplica_a desde `Obligacion_se_considerara_la_ultima_calificacion_informada_para_el_calculo_de_la_exigencia__768b58`; tramo del origen «A este efecto, se considerará la última calificación informada para el cálculo de la exigencia que corresponda integrar al tercer mes siguiente a aquel en que tenga lugar la notificación».

## Umbrales que ganan valor por la unidad del rótulo (decisión 2)

- diez: 2 elementos, por TO {'cap': 2}:
  - `Restriccion_exigencia_basica_de_capital_minimo_para_bancos_5_000_millones_de_pesos__cap_1_2_48b450`: tramo «5.000» → 5000000000 moneda ARS (rótulo «-En millones de pesos-», `cap::tabla000`)
  - `Restriccion_exigencia_basica_de_capital_minimo_para_restantes_entidades_salvo_cajas_de_credi_a4fc21`: tramo «2.500» → 2500000000 moneda ARS (rótulo «-En millones de pesos-», `cap::tabla000`)
- desarrollo: 2 elementos, por TO {'cap': 2}:
  - `Restriccion_exigencia_basica_de_capital_minimo_para_bancos_5_000_millones_de_pesos__cap_1_2_48b450`: tramo «5.000» → 5000000000 moneda ARS (rótulo «-En millones de pesos-», `cap::tabla000`)
  - `Restriccion_exigencia_basica_de_capital_minimo_para_restantes_entidades_salvo_cajas_de_credi_a4fc21`: tramo «2.500» → 2500000000 moneda ARS (rótulo «-En millones de pesos-», `cap::tabla000`)
