# Verificaciones de la adjudicación del DEV v7 — barridos determinísticos (parte 2)

Log íntegro de los puntos 3 (run_4/CQ-021) y 4 (run_4/CQ-028). Tabla resumen y notas
metodológicas en la parte 1 (`verificaciones_dev_v7_1.md`).

```
==============================================================================
3. run_4/CQ-021 (16 outputs re-ejecutables)
==============================================================================

[3a] nodos que soportaron los 3 centrales verdaderos — identificación por exposición:
  ['optatividad'] exposición en outputs de run_4/CQ-021:
    AUSENTE en todos los outputs completos
  ['saldo'] exposición en outputs de run_4/CQ-021:
    paso 1 resultados[1] id=cambio_negativo_en_clasificacion
       …ediante medios especificados, con excepciones segun el saldo de deu…"}…
    paso 2 resultados[1] id=cambio_negativo_en_clasificacion
       …ediante medios especificados, con excepciones segun el saldo de deu…"}…
    paso 3 nodo id=cambio_negativo_en_clasificacion
       …ediante medios especificados, con excepciones segun el saldo de deuda.", "version": "vigente", "type_raw": ["evento…
    paso 5 resultados[1] id=saldo_de_deuda
       …{"id": "saldo_de_deuda", "type": "componente_de_exposicion", "label"…
    paso 5 resultados[1] id=saldo_de_deuda
       …_deuda", "type": "componente_de_exposicion", "label": "saldo de deuda", "tokens_matcheados": 2, "resumen_propiedade…
    paso 5 resultados[2] id=saldo_de_deuda_pendiente
       …{"id": "saldo_de_deuda_pendiente", "type": "componente_de_ltv", "lab…
    paso 5 resultados[2] id=saldo_de_deuda_pendiente
       …uda_pendiente", "type": "componente_de_ltv", "label": "saldo de deuda pendiente", "tokens_matcheados": 2, "resumen_…
    paso 5 resultados[3] id=declaracion_jurada_de_saldo_de_deuda_pendiente
       …{"id": "declaracion_jurada_de_saldo_de_deuda_pendiente", "type": "requisito_de_verificacio…
    paso 5 resultados[3] id=declaracion_jurada_de_saldo_de_deuda_pendiente
       …sito_de_verificacion", "label": "declaracion jurada de saldo de deuda pendiente", "tokens_matcheados": 2, "resumen_…
    paso 5 resultados[4] id=saldo_bruto
       …{"id": "saldo_bruto", "type": "medida_de_exposicion", "label": "sald…
    paso 5 resultados[4] id=saldo_bruto
       …aldo_bruto", "type": "medida_de_exposicion", "label": "saldo bruto", "tokens_matcheados": 1, "resumen_propiedades":…
    paso 6 resultados[1] id=saldo_bruto
       …{"id": "saldo_bruto", "type": "medida_de_exposicion", "label": "sald…
    paso 6 resultados[1] id=saldo_bruto
       …aldo_bruto", "type": "medida_de_exposicion", "label": "saldo bruto", "tokens_matcheados": 1, "resumen_propiedades":…
    paso 6 resultados[2] id=saldo_de_deuda
       …{"id": "saldo_de_deuda", "type": "componente_de_exposicion", "label"…
    paso 6 resultados[2] id=saldo_de_deuda
       …_deuda", "type": "componente_de_exposicion", "label": "saldo de deuda", "tokens_matcheados": 1, "resumen_propiedade…
    paso 6 resultados[4] id=saldo_de_deuda_pendiente
       …{"id": "saldo_de_deuda_pendiente", "type": "componente_de_ltv", "lab…
    paso 6 resultados[4] id=saldo_de_deuda_pendiente
       …uda_pendiente", "type": "componente_de_ltv", "label": "saldo de deuda pendiente", "tokens_matcheados": 1, "resumen_…
    paso 6 resultados[7] id=saldo_pendiente_de_entrega
       …{"id": "saldo_pendiente_de_entrega", "type": "excepcion_a_regulariza…
    paso 6 resultados[7] id=saldo_pendiente_de_entrega
       …rega", "type": "excepcion_a_regularizacion", "label": "saldo pendiente de entrega", "tokens_matcheados": 1, "resume…
    paso 6 resultados[9] id=cambio_negativo_en_clasificacion
       …ediante medios especificados, con excepciones segun el saldo de deu…"}…
    paso 6 resultados[10] id=saldo_pendiente_de_regularizacion
       …{"id": "saldo_pendiente_de_regularizacion", "type": "concepto_regula…
    paso 6 resultados[10] id=saldo_pendiente_de_regularizacion
       …larizacion", "type": "concepto_regulatorio", "label": "saldo pendiente de regularizacion", "tokens_matcheados": 1, …
    paso 8 resultados[1] id=cambio_negativo_en_clasificacion
       …ediante medios especificados, con excepciones segun el saldo de deu…"}…
    paso 12 resultados[2] id=seguro_de_vida_sobre_saldo_deudor
       …{"id": "seguro_de_vida_sobre_saldo_deudor", "type": "producto_financiero", "label": "segu…
    paso 12 resultados[2] id=seguro_de_vida_sobre_saldo_deudor
       … "producto_financiero", "label": "seguro de vida sobre saldo deudor", "tokens_matcheados": 2, "resumen_propiedades"…
    paso 12 resultados[4] id=saldo_deudor_de_otros_resultados_integrales
       …{"id": "saldo_deudor_de_otros_resultados_integrales", "type": "compo…
    paso 12 resultados[4] id=saldo_deudor_de_otros_resultados_integrales
       …"type": "componente_de_capital_regulatorio", "label": "saldo deudor de otros resultados integrales", "tokens_matche…
    paso 12 resultados[6] id=saldo_bruto
       …{"id": "saldo_bruto", "type": "medida_de_exposicion", "label": "sald…
    paso 12 resultados[6] id=saldo_bruto
       …aldo_bruto", "type": "medida_de_exposicion", "label": "saldo bruto", "tokens_matcheados": 1, "resumen_propiedades":…
    paso 12 resultados[8] id=saldo_de_deuda
       …{"id": "saldo_de_deuda", "type": "componente_de_exposicion", "label"…
    paso 12 resultados[8] id=saldo_de_deuda
       …_deuda", "type": "componente_de_exposicion", "label": "saldo de deuda", "tokens_matcheados": 1, "resumen_propiedade…
    paso 16 resultados[2] id=cambio_negativo_en_clasificacion
       …ediante medios especificados, con excepciones segun el saldo de deu…"}…
  ['régimen informativo'] exposición en outputs de run_4/CQ-021:
    paso 8 resultados[3] id=regimen_informativo_de_operaciones_de_cambio_rioc
       …mbio_rioc", "type": "mecanismo_de_registro", "label": "regimen informativo de operaciones de cambio (rioc)", "tokens_matcheados":…

  nodos fuente identificados (unión de las 3 exposiciones): ['cambio_negativo_en_clasificacion', 'declaracion_jurada_de_saldo_de_deuda_pendiente', 'regimen_informativo_de_operaciones_de_cambio_rioc', 'saldo_bruto', 'saldo_de_deuda', 'saldo_de_deuda_pendiente', 'saldo_deudor_de_otros_resultados_integrales', 'saldo_pendiente_de_entrega', 'saldo_pendiente_de_regularizacion', 'seguro_de_vida_sobre_saldo_deudor']

  --- cambio_negativo_en_clasificacion (ÍNTEGRO, con provenances) ---
{
 "id": "cambio_negativo_en_clasificacion",
 "type": "evento_regulatorio",
 "label": "Cambio negativo en clasificación",
 "properties": {
  "description": "Reclasificación desfavorable del deudor que debe ser comunicada al deudor dentro de 45 días mediante medios especificados, con excepciones según el saldo de deuda.",
  "version": "vigente",
  "type_raw": [
   "Evento regulatorio"
  ],
  "type_raw_counts": {
   "Evento regulatorio": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "p.9-12 / Punto 3.4.2"
  }
 ]
}

  --- declaracion_jurada_de_saldo_de_deuda_pendiente (ÍNTEGRO, con provenances) ---
{
 "id": "declaracion_jurada_de_saldo_de_deuda_pendiente",
 "type": "requisito_de_verificacion",
 "label": "Declaración jurada de saldo de deuda pendiente",
 "properties": {
  "description": "Para importaciones oficializadas con anterioridad al 01/11/19, declaración jurada consignando el saldo de deuda pendiente a la fecha, firmada por el importador o su representante legal o apoderado con facultades suficientes.",
  "version": "vigente",
  "type_raw": [
   "Requisito de verificación"
  ],
  "type_raw_counts": {
   "Requisito de verificación": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.133-136 / Punto 10.3.2.1, inciso x)"
  }
 ]
}

  --- regimen_informativo_de_operaciones_de_cambio_rioc (ÍNTEGRO, con provenances) ---
{
 "id": "regimen_informativo_de_operaciones_de_cambio_rioc",
 "type": "mecanismo_de_registro",
 "label": "Régimen informativo de operaciones de cambio (RIOC)",
 "properties": {
  "description": "Sistema ante el BCRA mediante el cual la entidad financiera registra la financiación una vez verificado el registro de ingreso aduanero de los bienes.",
  "version": "vigente",
  "type_raw": [
   "Mecanismo de registro"
  ],
  "type_raw_counts": {
   "Mecanismo de registro": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.180-182 / Punto 14.5.3, inciso iii)"
  }
 ]
}

  --- saldo_bruto (ÍNTEGRO, con provenances) ---
{
 "id": "saldo_bruto",
 "type": "medida_de_exposicion",
 "label": "Saldo bruto",
 "properties": {
  "description": "Monto bruto de exposiciones minoristas sin computar coberturas del riesgo de crédito.",
  "version": "vigente",
  "type_raw": [
   "Medida de exposición"
  ],
  "type_raw_counts": {
   "Medida de exposición": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.14-17 / Punto 2.8.3.2"
  }
 ]
}

  --- saldo_de_deuda (ÍNTEGRO, con provenances) ---
{
 "id": "saldo_de_deuda",
 "type": "componente_de_exposicion",
 "label": "Saldo de deuda",
 "properties": {
  "description": "Importe adeudado por la contraparte, incluido en el cálculo de exposición.",
  "version": "vigente",
  "type_raw": [
   "Componente de exposición"
  ],
  "type_raw_counts": {
   "Componente de exposición": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.11-13 / Punto 2.5.5"
  }
 ]
}

  --- saldo_de_deuda_pendiente (ÍNTEGRO, con provenances) ---
{
 "id": "saldo_de_deuda_pendiente",
 "type": "componente_de_ltv",
 "label": "Saldo de deuda pendiente",
 "properties": {
  "description": "Saldo de deuda sin deducir previsiones por riesgo de incobrabilidad ni coberturas del riesgo de crédito.",
  "version": "vigente",
  "type_raw": [
   "Componente de LTV"
  ],
  "type_raw_counts": {
   "Componente de LTV": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.18-21 / Punto 2.9.2.3.i"
  }
 ]
}

  --- saldo_deudor_de_otros_resultados_integrales (ÍNTEGRO, con provenances) ---
{
 "id": "saldo_deudor_de_otros_resultados_integrales",
 "type": "componente_de_capital_regulatorio",
 "label": "Saldo deudor de otros resultados integrales",
 "properties": {
  "description": "Saldo deudor proveniente del resto de los conceptos componentes de los otros resultados integrales no contemplados en revaluaciones.",
  "version": "vigente",
  "type_raw": [
   "Componente de Capital Regulatorio"
  ],
  "type_raw_counts": {
   "Componente de Capital Regulatorio": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "p.31-35 / Sección 6.2, código 28200000"
  }
 ]
}

  --- saldo_pendiente_de_entrega (ÍNTEGRO, con provenances) ---
{
 "id": "saldo_pendiente_de_entrega",
 "type": "excepcion_a_regularizacion",
 "label": "Saldo pendiente de entrega",
 "properties": {
  "description": "Situación en la cual el importador puede optar por no demostrar la oficialización del ingreso de bienes o divisas, dentro de límites establecidos.",
  "version": "vigente",
  "type_raw": [
   "Excepción a regularización"
  ],
  "type_raw_counts": {
   "Excepción a regularización": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.143-145 / Punto 10.5.4"
  }
 ]
}

  --- saldo_pendiente_de_regularizacion (ÍNTEGRO, con provenances) ---
{
 "id": "saldo_pendiente_de_regularizacion",
 "type": "concepto_regulatorio",
 "label": "Saldo pendiente de regularización",
 "properties": {
  "description": "Monto de pagos anticipados de importaciones que aún no han sido regularizados mediante el registro de ingreso aduanero.",
  "version": "vigente",
  "type_raw": [
   "Concepto regulatorio"
  ],
  "type_raw_counts": {
   "Concepto regulatorio": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.140-142 / Punto 10.4.2.5"
  }
 ]
}

  --- seguro_de_vida_sobre_saldo_deudor (ÍNTEGRO, con provenances) ---
{
 "id": "seguro_de_vida_sobre_saldo_deudor",
 "type": "producto_financiero",
 "label": "Seguro de vida sobre saldo deudor",
 "properties": {
  "description": "Seguro que puede contratarse para tomar cobertura por riesgo de muerte del deudor, cuya contratación es decisión del sujeto obligado.",
  "version": "vigente",
  "type_raw": [
   "Producto de seguros accesorio",
   "Producto financiero"
  ],
  "type_raw_counts": {
   "Producto de seguros accesorio": 1,
   "Producto financiero": 1
  },
  "name_variants": [],
  "n_observations": 2
 },
 "provenances": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.18-20 / Sección 2.3.12.1"
  },
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.21-24 / Punto 2.6"
  }
 ]
}

[3b] barridos kg run_4 (exposición [3c] y D1 sobre no expuestos [3d] integrados):
  [barrido kg run_4: 'optativo|optativa'] en id/label/properties: 0
  [barrido kg run_4: 'regimen informativo ∧ deudores'] en id/label/properties: 0
  [barrido kg run_4: 'saldo de deuda'] en id/label/properties: 5

  --- cambio_negativo_en_clasificacion (props) | expuesto en outputs de CQ-021: pasos [1, 2, 3, 4, 6, 8, 16] ---
{
 "id": "cambio_negativo_en_clasificacion",
 "type": "evento_regulatorio",
 "label": "Cambio negativo en clasificación",
 "properties": {
  "description": "Reclasificación desfavorable del deudor que debe ser comunicada al deudor dentro de 45 días mediante medios especificados, con excepciones según el saldo de deuda.",
  "version": "vigente",
  "type_raw": [
   "Evento regulatorio"
  ],
  "type_raw_counts": {
   "Evento regulatorio": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "p.9-12 / Punto 3.4.2"
  }
 ]
}

  --- declaracion_jurada_de_saldo_de_deuda_pendiente (props) | expuesto en outputs de CQ-021: pasos [5] ---
{
 "id": "declaracion_jurada_de_saldo_de_deuda_pendiente",
 "type": "requisito_de_verificacion",
 "label": "Declaración jurada de saldo de deuda pendiente",
 "properties": {
  "description": "Para importaciones oficializadas con anterioridad al 01/11/19, declaración jurada consignando el saldo de deuda pendiente a la fecha, firmada por el importador o su representante legal o apoderado con facultades suficientes.",
  "version": "vigente",
  "type_raw": [
   "Requisito de verificación"
  ],
  "type_raw_counts": {
   "Requisito de verificación": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.133-136 / Punto 10.3.2.1, inciso x)"
  }
 ]
}

  --- saldo_de_deuda (props) | expuesto en outputs de CQ-021: pasos [5, 6, 12] ---
{
 "id": "saldo_de_deuda",
 "type": "componente_de_exposicion",
 "label": "Saldo de deuda",
 "properties": {
  "description": "Importe adeudado por la contraparte, incluido en el cálculo de exposición.",
  "version": "vigente",
  "type_raw": [
   "Componente de exposición"
  ],
  "type_raw_counts": {
   "Componente de exposición": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.11-13 / Punto 2.5.5"
  }
 ]
}

  --- loan_to_value_ltv (props) | expuesto en outputs de CQ-021: NO ---
{
 "id": "loan_to_value_ltv",
 "type": "metrica_de_riesgo",
 "label": "Loan-to-value (LTV)",
 "properties": {
  "description": "Relación entre el saldo de deuda pendiente y el valor del inmueble, calculada de manera prudente con requisitos específicos de cómputo y valuación.",
  "version": "vigente",
  "type_raw": [
   "Métrica de riesgo",
   "Ratio de elegibilidad"
  ],
  "type_raw_counts": {
   "Métrica de riesgo": 1,
   "Ratio de elegibilidad": 1
  },
  "name_variants": [],
  "n_observations": 2
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.18-21 / Punto 2.9.2.3"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.49-51 / Sección v)"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": null, "n_consultas": 36, "top10": []}

  --- saldo_de_deuda_pendiente (props) | expuesto en outputs de CQ-021: pasos [5, 6] ---
{
 "id": "saldo_de_deuda_pendiente",
 "type": "componente_de_ltv",
 "label": "Saldo de deuda pendiente",
 "properties": {
  "description": "Saldo de deuda sin deducir previsiones por riesgo de incobrabilidad ni coberturas del riesgo de crédito.",
  "version": "vigente",
  "type_raw": [
   "Componente de LTV"
  ],
  "type_raw_counts": {
   "Componente de LTV": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.18-21 / Punto 2.9.2.3.i"
  }
 ]
}
  [barrido kg run_4: '45 dias'] en id/label/properties: 4

  --- cambio_negativo_en_clasificacion (props) | expuesto en outputs de CQ-021: pasos [1, 2, 3, 4, 6, 8, 16] ---
{
 "id": "cambio_negativo_en_clasificacion",
 "type": "evento_regulatorio",
 "label": "Cambio negativo en clasificación",
 "properties": {
  "description": "Reclasificación desfavorable del deudor que debe ser comunicada al deudor dentro de 45 días mediante medios especificados, con excepciones según el saldo de deuda.",
  "version": "vigente",
  "type_raw": [
   "Evento regulatorio"
  ],
  "type_raw_counts": {
   "Evento regulatorio": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "p.9-12 / Punto 3.4.2"
  }
 ]
}

  --- operaciones_dvp_fallidas_entre_31_y_45_dias (props) | expuesto en outputs de CQ-021: pasos [12, 16] ---
{
 "id": "operaciones_dvp_fallidas_entre_31_y_45_dias",
 "type": "categoria_de_exposicion",
 "label": "Operaciones DvP fallidas entre 31 y 45 días",
 "properties": {
  "description": "Operaciones con entrega contra pago fallidas con código 1330000 y cargo de capital del 75% cuando el pago no se realiza dentro de 31 a 45 días hábiles.",
  "version": "vigente",
  "type_raw": [
   "Categoría de exposición"
  ],
  "type_raw_counts": {
   "Categoría de exposición": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "p.6-10 / Sección 3.1.5, tabla de operaciones DvP fallidas"
  }
 ]
}

  --- periodo_de_45_dias (props) | expuesto en outputs de CQ-021: pasos [12, 13, 14, 16] ---
{
 "id": "periodo_de_45_dias",
 "type": "plazo_regulatorio",
 "label": "Período de 45 días",
 "properties": {
  "description": "Plazo máximo previo a la transferencia de activos dentro del cual el originante o fiduciario debe analizar las condiciones de cumplimiento.",
  "version": "vigente",
  "type_raw": [
   "Plazo regulatorio"
  ],
  "type_raw_counts": {
   "Plazo regulatorio": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.49-51 / Sección iii)"
  }
 ]
}

  --- factor_de_exigencia_de_capital_75 (props) | expuesto en outputs de CQ-021: NO ---
{
 "id": "factor_de_exigencia_de_capital_75",
 "type": "factor_regulatorio",
 "label": "Factor de exigencia de capital 75%",
 "properties": {
  "description": "Factor aplicable a operaciones DvP fallidas entre 31 y 45 días hábiles posteriores a la fecha de liquidación acordada.",
  "version": "vigente",
  "type_raw": [
   "Factor regulatorio"
  ],
  "type_raw_counts": {
   "Factor regulatorio": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.63-65 / Punto 4.1.1, cuadro"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 1427, "n_consultas": 36, "top10": []}
  [barrido kg run_4: '3.4.2 (props)'] en id/label/properties: 0 | SOLO en provenances: 10

  --- garantia_preferida_a (SOLO provenance) | expuesto en outputs de CQ-021: NO ---
{
 "id": "garantia_preferida_a",
 "type": "tipo_de_garantia",
 "label": "Garantía preferida A",
 "properties": {
  "description": "Garantía que cubre la deuda del deudor, cuya existencia exime de la obligación de evaluar la capacidad de repago e incorporar cierta información al legajo del cliente.",
  "version": "vigente",
  "type_raw": [
   "Tipo de garantía",
   "Instrumento de garantía"
  ],
  "type_raw_counts": {
   "Tipo de garantía": 1,
   "Instrumento de garantía": 1
  },
  "name_variants": [],
  "n_observations": 2
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "p.1-8 / Sección 1.2.2"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "p.9-12 / Punto 3.4.2"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": null, "n_consultas": 36, "top10": []}

  --- superintendencia_de_entidades_financieras_y_cambiarias (SOLO provenance) | expuesto en outputs de CQ-021: NO ---
{
 "id": "superintendencia_de_entidades_financieras_y_cambiarias",
 "type": "autoridad_regulatoria",
 "label": "Superintendencia de Entidades Financieras y Cambiarias",
 "properties": {
  "description": "Autoridad ante la cual debe estar a disposición permanente el Manual de procedimientos de clasificación y previsión y cierta información de los legajos de clientes.",
  "version": "vigente",
  "type_raw": [
   "Autoridad regulatoria",
   "Autoridad reguladora",
   "Organismo regulador"
  ],
  "type_raw_counts": {
   "Autoridad regulatoria": 5,
   "Autoridad reguladora": 1,
   "Organismo regulador": 1
  },
  "name_variants": [],
  "n_observations": 7
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "p.9-12 / Puntos 3.3, 3.4.2"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "p.13-16 / Punto 3.5.2, 3.5.3"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "p.20-22 / Punto 6.5.2.1"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "p.39-43 / Sección 7, punto 7.4 y Sección 10, punto 10.2.2"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "p.28-30 / Punto 6.1.2, Códigos 21800000 y 22300000"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.1-6 / Sección 1, punto 1.4.2.1"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.146-149 / Punto 7.1.1.3"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 463, "n_consultas": 36, "top10": []}

  --- cambio_negativo_en_clasificacion (SOLO provenance) | expuesto en outputs de CQ-021: pasos [1, 2, 3, 4, 6, 8, 16] ---
{
 "id": "cambio_negativo_en_clasificacion",
 "type": "evento_regulatorio",
 "label": "Cambio negativo en clasificación",
 "properties": {
  "description": "Reclasificación desfavorable del deudor que debe ser comunicada al deudor dentro de 45 días mediante medios especificados, con excepciones según el saldo de deuda.",
  "version": "vigente",
  "type_raw": [
   "Evento regulatorio"
  ],
  "type_raw_counts": {
   "Evento regulatorio": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "p.9-12 / Punto 3.4.2"
  }
 ]
}

  --- corresponsal (SOLO provenance) | expuesto en outputs de CQ-021: NO ---
{
 "id": "corresponsal",
 "type": "sujeto_regulado",
 "label": "Corresponsal",
 "properties": {
  "description": "Entidad con la que la entidad financiera mantiene relaciones de corresponsalía, para la cual debe llevarse legajo con información de identificación, calificación y márgenes de crédito.",
  "version": "vigente",
  "type_raw": [
   "Sujeto regulado"
  ],
  "type_raw_counts": {
   "Sujeto regulado": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "p.9-12 / Puntos 3.4.1, 3.4.2"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": null, "n_consultas": 36, "top10": []}

  --- margen_crediticio (SOLO provenance) | expuesto en outputs de CQ-021: NO ---
{
 "id": "margen_crediticio",
 "type": "parametro_crediticio",
 "label": "Margen crediticio",
 "properties": {
  "description": "Límite de crédito asignado al deudor, que debe constar en el legajo del cliente discriminado por tipo o línea.",
  "version": "vigente",
  "type_raw": [
   "Parámetro crediticio"
  ],
  "type_raw_counts": {
   "Parámetro crediticio": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "p.9-12 / Punto 3.4.2"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": null, "n_consultas": 36, "top10": []}

  --- deudor_en_gestion_judicial_o_extrajudicial_de_cobro (SOLO provenance) | expuesto en outputs de CQ-021: pasos [4] ---
{
 "id": "deudor_en_gestion_judicial_o_extrajudicial_de_cobro",
 "type": "categoria_de_deudor",
 "label": "Deudor en gestión judicial o extrajudicial de cobro",
 "properties": {
  "description": "Deudor respecto del cual se han iniciado gestiones de cobro judicial o extrajudicial, a quien deben comunicarse los cambios negativos en clasificación en la medida que cuente con notificaciones postales o fehacientes.",
  "version": "vigente",
  "type_raw": [
   "Categoría de deudor"
  ],
  "type_raw_counts": {
   "Categoría de deudor": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "p.9-12 / Punto 3.4.2"
  }
 ]
}

  --- responsabilidad_patrimonial_computable (SOLO provenance) | expuesto en outputs de CQ-021: NO ---
{
 "id": "responsabilidad_patrimonial_computable",
 "type": "concepto_regulatorio",
 "label": "Responsabilidad patrimonial computable",
 "properties": {
  "description": "Medida de capital regulatorio total que incluye Capital Ordinario de Nivel 1, Capital Adicional de Nivel 1 y Patrimonio Neto Complementario menos sus respectivos deducibles, con requisito mínimo del 8% sobre activos ponderados por riesgo.",
  "version": "vigente",
  "type_raw": [
   "Parámetro regulatorio",
   "Métrica financiera",
   "Requisito regulatorio de capital",
   "Concepto regulatorio de capital",
   "Medida de Capital Regulatorio",
   "Concepto de exigencia de capital",
   "Concepto regulatorio",
   "Concepto de integración"
  ],
  "type_raw_counts": {
   "Concepto de integración": 1,
   "Concepto regulatorio": 2,
   "Parámetro regulatorio": 1,
   "Métrica financiera": 1,
   "Requisito regulatorio de capital": 1,
   "Concepto regulatorio de capital": 1,
   "Medida de Capital Regulatorio": 1,
   "Concepto de exigencia de capital": 1
  },
  "name_variants": [
   "Responsabilidad Patrimonial Computable",
   "Responsabilidad patrimonial computable"
  ],
  "n_observations": 9
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "p.9-12 / Punto 3.4.2"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "p.13-16 / Punto 3.4.4, 3.5.2, 3.6"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "p.1-5 / Sección 6"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "p.28-30 / Sección 6, punto 6.1"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "p.31-35 / Sección 6.3"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "p.36-39 / Sección 8.1.6, código 70200000"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "p.40-43 / Sección 10.1.3"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.1-6 / Sección 1, punto 1.3"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.167-170 / Punto 8.5, 8.6"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": null, "n_consultas": 36, "top10": []}

  --- vinculacion_al_intermediario_financiero (SOLO provenance) | expuesto en outputs de CQ-021: NO ---
{
 "id": "vinculacion_al_intermediario_financiero",
 "type": "relacion_comercial",
 "label": "Vinculación al intermediario financiero",
 "properties": {
  "description": "Relación entre cliente del sector privado no financiero e intermediario financiero que debe ser declarada jurada cuando la deuda excede ciertos umbrales.",
  "version": "vigente",
  "type_raw": [
   "Relación comercial"
  ],
  "type_raw_counts": {
   "Relación comercial": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "p.9-12 / Punto 3.4.2"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 1638, "n_consultas": 36, "top10": []}

  --- asamblea_de_accionistas (SOLO provenance) | expuesto en outputs de CQ-021: NO ---
{
 "id": "asamblea_de_accionistas",
 "type": "organo_corporativo",
 "label": "Asamblea de accionistas",
 "properties": {
  "description": "Autoridad competente para adoptar decisiones sobre capitalización de deuda y aportes de capital, cuyas decisiones están sujetas a aprobación posterior de la SEFyC o BCRA.",
  "version": "vigente",
  "type_raw": [
   "Órgano corporativo"
  ],
  "type_raw_counts": {
   "Órgano corporativo": 4
  },
  "name_variants": [],
  "n_observations": 4
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.16-18 / Punto 3.4.2"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.40-42 / Punto 3.14.5.4"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.126-128 / Punto 9.3.12.2"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.167-170 / Punto 8.6, 8.7"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 893, "n_consultas": 36, "top10": []}

  --- representante_legal_de_la_empresa_residente (SOLO provenance) | expuesto en outputs de CQ-021: NO ---
{
 "id": "representante_legal_de_la_empresa_residente",
 "type": "sujeto_regulado",
 "label": "Representante legal de la empresa residente",
 "properties": {
  "description": "Persona autorizada para firmar declaración jurada sobre cumplimiento de límites de distribución de utilidades.",
  "version": "vigente",
  "type_raw": [
   "Sujeto regulado"
  ],
  "type_raw_counts": {
   "Sujeto regulado": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.16-18 / Punto 3.4.2"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 349, "n_consultas": 36, "top10": []}

[3e] secundario — exposición conjunta 'medios' ∧ 'comunicac':
  ['medios ∧ comunicación' = medios ∧ comunicac] exposición conjunta en outputs de run_4/CQ-021:
    AUSENTE (ninguna unidad contiene todos los términos)

==============================================================================
4. run_4/CQ-028 (15 outputs re-ejecutables)
==============================================================================

[4a] barridos kg run_4 (íntegros; exposición [4b] y D1 [4c] integrados):
  [barrido kg run_4: 'precancelacion (TODOS ÍNTEGROS)'] en id/label/properties: 14

  --- derecho_de_precancelacion_total_o_parcial (props) | expuesto en outputs de CQ-028: pasos [2, 5] ---
{
 "id": "derecho_de_precancelacion_total_o_parcial",
 "type": "contenido_contractual_obligatorio",
 "label": "Derecho de precancelación total o parcial",
 "properties": {
  "description": "Derecho del usuario a efectuar en cualquier momento del plazo del crédito la precancelación total o precancelaciones parciales.",
  "version": "vigente",
  "type_raw": [
   "Contenido contractual obligatorio"
  ],
  "type_raw_counts": {
   "Contenido contractual obligatorio": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.6-8 / Punto 2.3.1.1, inciso vi)"
  }
 ]
}

  --- comision_por_precancelacion (props) | expuesto en outputs de CQ-028: pasos [1, 3, 4, 6, 7] ---
{
 "id": "comision_por_precancelacion",
 "type": "comision_permitida",
 "label": "Comisión por precancelación",
 "properties": {
  "description": "Comisión que puede aplicarse por precancelación total o parcial de financiaciones, con restricción en precancelación total cuando haya transcurrido al menos la cuarta parte del plazo original o 180 días.",
  "version": "vigente",
  "type_raw": [
   "Comisión permitida"
  ],
  "type_raw_counts": {
   "Comisión permitida": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.12-14 / Punto 2.3.2.1, párrafo segundo"
  }
 ]
}

  --- precancelacion_de_capital_e_intereses_con_liquidacion_de_fondos_de_nuevo_titulo (props) | expuesto en outputs de CQ-028: NO ---
{
 "id": "precancelacion_de_capital_e_intereses_con_liquidacion_de_fondos_de_nuevo_titulo",
 "type": "operacion_de_refinanciacion",
 "label": "Precancelación de capital e intereses con liquidación de fondos de nuevo título",
 "properties": {
  "description": "Precancelación simultánea de capital e intereses con liquidación de fondos ingresados desde el exterior por emisión de nuevo título de deuda.",
  "version": "vigente",
  "type_raw": [
   "Operación de refinanciación"
  ],
  "type_raw_counts": {
   "Operación de refinanciación": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.22-24 / Punto 3.5.3.1"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 13, "n_consultas": 38, "top10": []}

  --- precancelacion_con_liquidacion_simultanea_de_otros_endeudamientos (props) | expuesto en outputs de CQ-028: NO ---
{
 "id": "precancelacion_con_liquidacion_simultanea_de_otros_endeudamientos",
 "type": "operacion_de_refinanciacion",
 "label": "Precancelación con liquidación simultánea de otros endeudamientos",
 "properties": {
  "description": "Precancelación de capital e intereses efectuada de manera simultánea con fondos liquidados de nuevo endeudamiento financiero.",
  "version": "vigente",
  "type_raw": [
   "Operación de refinanciación"
  ],
  "type_raw_counts": {
   "Operación de refinanciación": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.22-24 / Punto 3.5.3.2"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 12, "n_consultas": 38, "top10": []}

  --- precancelacion_de_intereses_en_canje_de_titulos (props) | expuesto en outputs de CQ-028: NO ---
{
 "id": "precancelacion_de_intereses_en_canje_de_titulos",
 "type": "operacion_de_canje",
 "label": "Precancelación de intereses en canje de títulos",
 "properties": {
  "description": "Precancelación de intereses que se concreta en marco de proceso de canje de títulos de deuda emitidos por el cliente.",
  "version": "vigente",
  "type_raw": [
   "Operación de canje"
  ],
  "type_raw_counts": {
   "Operación de canje": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.22-24 / Punto 3.5.3.3"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 11, "n_consultas": 38, "top10": []}

  --- titulo_de_deuda (props) | expuesto en outputs de CQ-028: NO ---
{
 "id": "titulo_de_deuda",
 "type": "instrumento_financiero",
 "label": "Título de deuda",
 "properties": {
  "description": "Valor mobiliario emitido por residentes en moneda extranjera, sujeto a recompra, rescate o precancelación de capital e intereses.",
  "version": "vigente",
  "type_raw": [
   "Instrumento financiero",
   "Activo subyacente"
  ],
  "type_raw_counts": {
   "Activo subyacente": 1,
   "Instrumento financiero": 2
  },
  "name_variants": [],
  "n_observations": 3
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.25-27 / Punto 3.5.3.3, inciso iii-iv"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.31-33 / Puntos 3.6.4.3 a 3.6.4.6"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.134-137 / Punto 6.6.3.2"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 171, "n_consultas": 38, "top10": []}

  --- precancelacion_de_deudas (props) | expuesto en outputs de CQ-028: pasos [1] ---
{
 "id": "precancelacion_de_deudas",
 "type": "operacion_de_pago_anticipado",
 "label": "Precancelación de deudas",
 "properties": {
  "description": "Cancelación de obligaciones en moneda extranjera con anterioridad al vencimiento, que requiere conformidad previa del BCRA excepto en situaciones específicas.",
  "version": "vigente",
  "type_raw": [
   "Operación de pago anticipado"
  ],
  "type_raw_counts": {
   "Operación de pago anticipado": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.28-30 / Punto 3.6.4"
  }
 ]
}

  --- canje_de_titulos_de_deuda (props) | expuesto en outputs de CQ-028: NO ---
{
 "id": "canje_de_titulos_de_deuda",
 "type": "operacion_de_refinanciacion",
 "label": "Canje de títulos de deuda",
 "properties": {
  "description": "Proceso en el cual se entrega al acreedor un nuevo título con registro público en el país a cambio de uno existente, permitiendo la precancelación de intereses devengados.",
  "version": "vigente",
  "type_raw": [
   "Operación de refinanciación"
  ],
  "type_raw_counts": {
   "Operación de refinanciación": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.28-30 / Punto 3.6.4.3"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 504, "n_consultas": 38, "top10": []}

  --- vencimientos_de_capital (props) | expuesto en outputs de CQ-028: NO ---
{
 "id": "vencimientos_de_capital",
 "type": "parametro_tecnico",
 "label": "Vencimientos de capital",
 "properties": {
  "description": "Fechas de vencimiento del capital de las obligaciones, cuya acumulación debe cumplir condiciones específicas en operaciones de precancelación.",
  "version": "vigente",
  "type_raw": [
   "Parámetro regulatorio",
   "Parámetro técnico"
  ],
  "type_raw_counts": {
   "Parámetro regulatorio": 1,
   "Parámetro técnico": 1
  },
  "name_variants": [],
  "n_observations": 2
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.28-30 / Punto 3.6.4.2 y 3.6.4.3"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.31-33 / Punto 3.6.4.5.iii"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 460, "n_consultas": 38, "top10": []}

  --- intereses_devengados (props) | expuesto en outputs de CQ-028: NO ---
{
 "id": "intereses_devengados",
 "type": "parametro_regulatorio",
 "label": "Intereses devengados",
 "properties": {
  "description": "Intereses acumulados hasta una fecha específica, cuya precancelación está permitida en ciertos procesos de refinanciación y canje de títulos.",
  "version": "vigente",
  "type_raw": [
   "Parámetro regulatorio"
  ],
  "type_raw_counts": {
   "Parámetro regulatorio": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.28-30 / Punto 3.6.4.3 y 3.6.4.4"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": null, "n_consultas": 38, "top10": []}

  --- registro_publico_en_el_pais (props) | expuesto en outputs de CQ-028: NO ---
{
 "id": "registro_publico_en_el_pais",
 "type": "requisito_regulatorio",
 "label": "Registro público en el país",
 "properties": {
  "description": "Condición de que un nuevo título de deuda esté registrado públicamente en el país para ser elegible en operaciones de precancelación.",
  "version": "vigente",
  "type_raw": [
   "Requisito regulatorio"
  ],
  "type_raw_counts": {
   "Requisito regulatorio": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.31-33 / Punto 3.6.4.6.i"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 1050, "n_consultas": 38, "top10": []}

  --- precancelacion_de_capital_e_intereses (props) | expuesto en outputs de CQ-028: NO ---
{
 "id": "precancelacion_de_capital_e_intereses",
 "type": "operacion_de_cambio",
 "label": "Precancelación de capital e intereses",
 "properties": {
  "description": "Pago anticipado del capital e intereses de un título de deuda o endeudamiento financiero antes de su vencimiento.",
  "version": "vigente",
  "type_raw": [
   "Operación de cambio"
  ],
  "type_raw_counts": {
   "Operación de cambio": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.31-33 / Puntos 3.6.4.5 a 3.6.4.7"
  }
 ]
}
    D1: {"alcanzable": true, "mejor_rank": 8, "n_consultas": 38, "top10": [{"consulta": "comision precancelacion", "rank": 8}, {"consulta": "cobrar comision precancelacion", "rank": 10}]}

  --- precancelacion_de_linea_de_credito (props) | expuesto en outputs de CQ-028: pasos [7, 8, 11] ---
{
 "id": "precancelacion_de_linea_de_credito",
 "type": "operacion_cambiaria",
 "label": "Precancelación de línea de crédito",
 "properties": {
  "description": "Cancelación anticipada de una línea de crédito del exterior antes de su vencimiento.",
  "version": "vigente",
  "type_raw": [
   "Operación cambiaria"
  ],
  "type_raw_counts": {
   "Operación cambiaria": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.40-42 / Punto 3.15.1"
  }
 ]
}

  --- precancelacion_de_financiaciones_de_exportacion (props) | expuesto en outputs de CQ-028: NO ---
{
 "id": "precancelacion_de_financiaciones_de_exportacion",
 "type": "operacion_de_cambios",
 "label": "Precancelación de financiaciones de exportación",
 "properties": {
  "description": "Cancelación anticipada de financiaciones de exportación otorgadas por entidades financieras locales, sujeta a conformidad previa del BCRA.",
  "version": "vigente",
  "type_raw": [
   "Operación de cambios"
  ],
  "type_raw_counts": {
   "Operación de cambios": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.91-93 / Segundo párrafo, sección 7.8"
  }
 ]
}
    D1: {"alcanzable": true, "mejor_rank": 10, "n_consultas": 38, "top10": [{"consulta": "comision precancelacion", "rank": 10}]}
  [barrido kg run_4: '180 dias'] en id/label/properties: 17

  --- comision_por_precancelacion (props) | expuesto en outputs de CQ-028: pasos [1, 3, 4, 6, 7] ---
{
 "id": "comision_por_precancelacion",
 "type": "comision_permitida",
 "label": "Comisión por precancelación",
 "properties": {
  "description": "Comisión que puede aplicarse por precancelación total o parcial de financiaciones, con restricción en precancelación total cuando haya transcurrido al menos la cuarta parte del plazo original o 180 días.",
  "version": "vigente",
  "type_raw": [
   "Comisión permitida"
  ],
  "type_raw_counts": {
   "Comisión permitida": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.12-14 / Punto 2.3.2.1, párrafo segundo"
  }
 ]
}

  --- con_alto_riesgo_de_insolvencia (props) | expuesto en outputs de CQ-028: NO ---
{
 "id": "con_alto_riesgo_de_insolvencia",
 "type": "categoria_de_clasificacion",
 "label": "Con alto riesgo de insolvencia",
 "properties": {
  "description": "Categoría de clasificación para deudores que no cancelan intereses devengados dentro de 180 días de concertada la refinanciación.",
  "version": "vigente",
  "type_raw": [
   "Categoría de clasificación"
  ],
  "type_raw_counts": {
   "Categoría de clasificación": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "p.23-25 / Párrafo sobre no cancelación de intereses en 180 días"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 734, "n_consultas": 38, "top10": []}

  --- credito_adicional (props) | expuesto en outputs de CQ-028: NO ---
{
 "id": "credito_adicional",
 "type": "operacion_crediticia",
 "label": "Crédito adicional",
 "properties": {
  "description": "Financiación adicional otorgada conforme al punto 2.2.5 de normas sobre Previsiones mínimas por riesgo de incobrabilidad, que genera permanencia mínima de 180 días en categoría.",
  "version": "vigente",
  "type_raw": [
   "Operación crediticia",
   "Tipo de operación crediticia"
  ],
  "type_raw_counts": {
   "Operación crediticia": 3,
   "Tipo de operación crediticia": 1
  },
  "name_variants": [],
  "n_observations": 4
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "p.23-25 / Párrafos sobre permanencia en categoría por 180 días"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "p.26-28 / Punto 6.5.4.5 y 6.5.5.2"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "p.36-38 / Párrafos sobre crédito adicional en secciones 7.2.2.1, 7.2.3, 7.2.4"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "p.39-43 / Sección 7, párrafo inicial"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 11, "n_consultas": 38, "top10": []}

  --- atraso_recurrente (props) | expuesto en outputs de CQ-028: NO ---
{
 "id": "atraso_recurrente",
 "type": "indicador_de_riesgo",
 "label": "Atraso recurrente",
 "properties": {
  "description": "Patrón de incumplimientos repetidos de hasta 180 días respecto de condiciones contractuales.",
  "version": "vigente",
  "type_raw": [
   "Indicador de riesgo"
  ],
  "type_raw_counts": {
   "Indicador de riesgo": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "p.23-25 / Punto 6.5.3.7"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": null, "n_consultas": 38, "top10": []}

  --- incumplimientos_superiores_a_180_dias (props) | expuesto en outputs de CQ-028: NO ---
{
 "id": "incumplimientos_superiores_a_180_dias",
 "type": "indicador_de_incumplimiento",
 "label": "Incumplimientos superiores a 180 días",
 "properties": {
  "description": "Atrasos permanentes en el pago respecto de las condiciones contractuales que superan seis meses.",
  "version": "vigente",
  "type_raw": [
   "Indicador de incumplimiento"
  ],
  "type_raw_counts": {
   "Indicador de incumplimiento": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "p.26-28 / Punto 6.5.4.8"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": null, "n_consultas": 38, "top10": []}

  --- deudor_en_situacion_irregular (props) | expuesto en outputs de CQ-028: NO ---
{
 "id": "deudor_en_situacion_irregular",
 "type": "categoria_de_deudor",
 "label": "Deudor en situación irregular",
 "properties": {
  "description": "Cliente que registra atrasos superiores a 180 días en el cumplimiento de sus obligaciones, según nómina elaborada por el BCRA en base a información de administradores de carteras crediticias.",
  "version": "vigente",
  "type_raw": [
   "Categoría de deudor"
  ],
  "type_raw_counts": {
   "Categoría de deudor": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "p.29-32 / Punto 6.5.5.7"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 1119, "n_consultas": 38, "top10": []}

  --- riesgo_medio (props) | expuesto en outputs de CQ-028: NO ---
{
 "id": "riesgo_medio",
 "type": "categoria_de_clasificacion_de_deudores",
 "label": "Riesgo medio",
 "properties": {
  "description": "Comprende clientes con alguna incapacidad para cancelar obligaciones, con atrasos de más de 90 hasta 180 días.",
  "version": "vigente",
  "type_raw": [
   "Categoría de clasificación de deudores"
  ],
  "type_raw_counts": {
   "Categoría de clasificación de deudores": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "p.36-38 / Sección 7.2.3"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": null, "n_consultas": 38, "top10": []}

  --- riesgo_alto (props) | expuesto en outputs de CQ-028: NO ---
{
 "id": "riesgo_alto",
 "type": "categoria_de_clasificacion_de_deudores",
 "label": "Riesgo alto",
 "properties": {
  "description": "Comprende clientes con atrasos de más de 180 días hasta un año, o en situaciones de concurso preventivo, acuerdo preventivo extrajudicial no homologado, o quiebra requerida.",
  "version": "vigente",
  "type_raw": [
   "Categoría de clasificación de deudores"
  ],
  "type_raw_counts": {
   "Categoría de clasificación de deudores": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "p.36-38 / Sección 7.2.4"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": null, "n_consultas": 38, "top10": []}

  --- atraso_de_mas_de_90_hasta_180_dias (props) | expuesto en outputs de CQ-028: NO ---
{
 "id": "atraso_de_mas_de_90_hasta_180_dias",
 "type": "condicion_de_pago",
 "label": "Atraso de más de 90 hasta 180 días",
 "properties": {
  "description": "Retraso que define la inclusión en la categoría de Riesgo medio.",
  "version": "vigente",
  "type_raw": [
   "Condición de pago"
  ],
  "type_raw_counts": {
   "Condición de pago": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "p.36-38 / Sección 7.2.3"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 897, "n_consultas": 38, "top10": []}

  --- atraso_de_mas_de_180_dias_hasta_un_ano (props) | expuesto en outputs de CQ-028: NO ---
{
 "id": "atraso_de_mas_de_180_dias_hasta_un_ano",
 "type": "condicion_de_pago",
 "label": "Atraso de más de 180 días hasta un año",
 "properties": {
  "description": "Retraso que define la inclusión en la categoría de Riesgo alto.",
  "version": "vigente",
  "type_raw": [
   "Condición de pago"
  ],
  "type_raw_counts": {
   "Condición de pago": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "p.36-38 / Sección 7.2.4"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 161, "n_consultas": 38, "top10": []}

  --- periodo_de_permanencia_de_180_dias (props) | expuesto en outputs de CQ-028: NO ---
{
 "id": "periodo_de_permanencia_de_180_dias",
 "type": "requisito_temporal",
 "label": "Período de permanencia de 180 días",
 "properties": {
  "description": "Plazo mínimo de permanencia en categoría contado desde la fecha de otorgamiento de crédito adicional o celebración de acuerdo de refinanciación, el que sea más reciente.",
  "version": "vigente",
  "type_raw": [
   "Requisito temporal"
  ],
  "type_raw_counts": {
   "Requisito temporal": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "p.36-38 / Párrafos sobre crédito adicional en secciones 7.2.2.1, 7.2.3, 7.2.4"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 924, "n_consultas": 38, "top10": []}

  --- refinanciacion_de_deuda (props) | expuesto en outputs de CQ-028: NO ---
{
 "id": "refinanciacion_de_deuda",
 "type": "operacion_crediticia",
 "label": "Refinanciación de deuda",
 "properties": {
  "description": "Acuerdo mediante el cual se reestructura una deuda existente y se otorga crédito adicional, requiriendo permanencia mínima de 180 días en la categoría asignada.",
  "version": "vigente",
  "type_raw": [
   "Operación crediticia"
  ],
  "type_raw_counts": {
   "Operación crediticia": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "p.39-43 / Sección 7, párrafo inicial"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 452, "n_consultas": 38, "top10": []}

  --- plazo_de_vigencia_de_garantia (props) | expuesto en outputs de CQ-028: NO ---
{
 "id": "plazo_de_vigencia_de_garantia",
 "type": "parametro_regulatorio",
 "label": "Plazo de vigencia de garantía",
 "properties": {
  "description": "Período máximo de 180 días corridos desde la fecha de embarque de bienes o finalización de servicios durante el cual la garantía es válida.",
  "version": "vigente",
  "type_raw": [
   "Parámetro regulatorio"
  ],
  "type_raw_counts": {
   "Parámetro regulatorio": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.40-42 / Punto 3.15.2.6"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 37, "n_consultas": 38, "top10": []}

  --- desembolsos_en_el_exterior_desde_29_11_24 (props) | expuesto en outputs de CQ-028: NO ---
{
 "id": "desembolsos_en_el_exterior_desde_29_11_24",
 "type": "operacion_de_financiamiento",
 "label": "Desembolsos en el exterior desde 29/11/24",
 "properties": {
  "description": "Fondos depositados en cuentas bancarias en el exterior originados en desembolsos recibidos a partir del 29/11/24 de endeudamientos financieros, dentro de los últimos 180 días corridos.",
  "version": "vigente",
  "type_raw": [
   "Operación de financiamiento"
  ],
  "type_raw_counts": {
   "Operación de financiamiento": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.43-46 / Punto 3.16.2.1, inciso v)"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 1652, "n_consultas": 38, "top10": []}

  --- exportaciones_de_bienes_diversos (props) | expuesto en outputs de CQ-028: NO ---
{
 "id": "exportaciones_de_bienes_diversos",
 "type": "categoria_de_exportacion",
 "label": "Exportaciones de bienes diversos",
 "properties": {
  "description": "Resto de bienes no comprendidos en categorías anteriores, con plazo de 180 días corridos para ingreso y liquidación.",
  "version": "vigente",
  "type_raw": [
   "Categoría de exportación"
  ],
  "type_raw_counts": {
   "Categoría de exportación": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.78-81 / Punto 7.1.1.4"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 819, "n_consultas": 38, "top10": []}

  --- prorroga_de_gestion_de_cobro (props) | expuesto en outputs de CQ-028: NO ---
{
 "id": "prorroga_de_gestion_de_cobro",
 "type": "mecanismo_regulatorio",
 "label": "Prórroga de gestión de cobro",
 "properties": {
  "description": "Extensión de plazo otorgada por la entidad para mantener la operación en gestión de cobro, hasta cinco prórrogas sucesivas de hasta 180 días corridos.",
  "version": "vigente",
  "type_raw": [
   "Mecanismo regulatorio"
  ],
  "type_raw_counts": {
   "Mecanismo regulatorio": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.146-149 / Punto 10.5.5.2"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 666, "n_consultas": 38, "top10": []}

  --- plazo_de_180_dias_corridos (props) | expuesto en outputs de CQ-028: NO ---
{
 "id": "plazo_de_180_dias_corridos",
 "type": "requisito_temporal",
 "label": "Plazo de 180 días corridos",
 "properties": {
  "description": "Plazo requerido desde la fecha de prestación o devengamiento del servicio para acceso al mercado de cambios en operaciones de contraparte vinculada previas al 14/04/25.",
  "version": "vigente",
  "type_raw": [
   "Requisito temporal"
  ],
  "type_raw_counts": {
   "Requisito temporal": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.168-170 / 13.2.7.2"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 30, "n_consultas": 38, "top10": []}
  [barrido kg run_4: 'cuarta parte'] en id/label/properties: 1

  --- comision_por_precancelacion (props) | expuesto en outputs de CQ-028: pasos [1, 3, 4, 6, 7] ---
{
 "id": "comision_por_precancelacion",
 "type": "comision_permitida",
 "label": "Comisión por precancelación",
 "properties": {
  "description": "Comisión que puede aplicarse por precancelación total o parcial de financiaciones, con restricción en precancelación total cuando haya transcurrido al menos la cuarta parte del plazo original o 180 días.",
  "version": "vigente",
  "type_raw": [
   "Comisión permitida"
  ],
  "type_raw_counts": {
   "Comisión permitida": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.12-14 / Punto 2.3.2.1, párrafo segundo"
  }
 ]
}
  [barrido kg run_4: '2.3.2 (props)'] en id/label/properties: 0 | SOLO en provenances: 19
    (> 12 candidatos: regla declarada — ids completos abajo; íntegros solo los que cruzan con 'precancel|comision': 13)
    ids: ['usuario_de_servicios_financieros', 'comisiones_y_cargos', 'sujeto_obligado', 'operacion_por_ventanilla', 'comision', 'cargo', 'prestacion_de_servicio', 'tercero_prestador', 'comision_sobre_importes_no_utilizados', 'comision_por_precancelacion', 'servicio_financiero_no_solicitado', 'deposito_de_efectivo_en_pesos', 'micro_pequena_o_mediana_empresa_mipyme', 'contratacion_y_administracion_de_seguros', 'generacion_y_envio_de_resumenes_de_cuenta', 'evaluacion_otorgamiento_y_administracion_de_financiaciones', 'gastos_de_tasacion_notariales_o_de_escribania', 'persona_humana', 'base_consolidada_trimestral']

  --- comisiones_y_cargos (SOLO provenance) | expuesto en outputs de CQ-028: NO ---
{
 "id": "comisiones_y_cargos",
 "type": "concepto_de_costo",
 "label": "Comisiones y cargos",
 "properties": {
  "description": "Comisiones, cargos, costos, gastos, seguros u otros conceptos que los sujetos obligados perciben de los usuarios, excluyendo la tasa de interés, que deben tener origen en un costo real, directo y demostrable.",
  "version": "vigente",
  "type_raw": [
   "Contenido contractual obligatorio",
   "Concepto de costo",
   "Concepto regulado",
   "Concepto regulatorio"
  ],
  "type_raw_counts": {
   "Contenido contractual obligatorio": 1,
   "Concepto de costo": 1,
   "Concepto regulado": 1,
   "Concepto regulatorio": 1
  },
  "name_variants": [],
  "n_observations": 4
 },
 "provenances": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.6-8 / Punto 2.3.1.1, inciso iv)"
  },
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.9-11 / Punto 2.3.2.1"
  },
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.21-24 / Punto 2.5"
  },
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.28-32 / Punto 3.2.1.3, viñetas segunda y cuarta"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": null, "n_consultas": 38, "top10": []}

  --- operacion_por_ventanilla (SOLO provenance) | expuesto en outputs de CQ-028: NO ---
{
 "id": "operacion_por_ventanilla",
 "type": "comision_prohibida",
 "label": "Operación por ventanilla",
 "properties": {
  "description": "No pueden aplicarse comisiones ni cargos por operaciones efectuadas por ventanilla para usuarios personas humanas, incluyendo movimientos de fondos en efectivo en pesos y recepción de depósitos de cheques en casas operativas distintas.",
  "version": "vigente",
  "type_raw": [
   "Operación financiera",
   "Comisión prohibida"
  ],
  "type_raw_counts": {
   "Operación financiera": 1,
   "Comisión prohibida": 1
  },
  "name_variants": [],
  "n_observations": 2
 },
 "provenances": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.9-11 / Punto 2.3.1.1, inciso vii"
  },
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.12-14 / Punto 2.3.2.2.ii.a"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 73, "n_consultas": 38, "top10": []}

  --- comision (SOLO provenance) | expuesto en outputs de CQ-028: pasos [1, 3, 4, 6, 7, 9, 13] ---
{
 "id": "comision",
 "type": "tipo_de_costo",
 "label": "Comisión",
 "properties": {
  "description": "Retribución que obedece a servicios prestados por los sujetos obligados y puede incluir retribuciones que excedan el costo de la prestación.",
  "version": "vigente",
  "type_raw": [
   "Tipo de costo",
   "Concepto regulatorio",
   "Componente de precio"
  ],
  "type_raw_counts": {
   "Tipo de costo": 1,
   "Concepto regulatorio": 1,
   "Componente de precio": 1
  },
  "name_variants": [],
  "n_observations": 3
 },
 "provenances": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.9-11 / Punto 2.3.2.1"
  },
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.15-17 / Punto 2.3.5.1"
  },
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.18-20 / Sección 2.3.9.8"
  }
 ]
}

  --- prestacion_de_servicio (SOLO provenance) | expuesto en outputs de CQ-028: NO ---
{
 "id": "prestacion_de_servicio",
 "type": "requisito_regulatorio",
 "label": "Prestación de servicio",
 "properties": {
  "description": "Requisito para la aplicación de comisiones y cargos, que deben corresponder a servicios previamente solicitados, pactados y/o autorizados por el usuario.",
  "version": "vigente",
  "type_raw": [
   "Requisito regulatorio"
  ],
  "type_raw_counts": {
   "Requisito regulatorio": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.9-11 / Punto 2.3.2.1"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 407, "n_consultas": 38, "top10": []}

  --- comision_sobre_importes_no_utilizados (SOLO provenance) | expuesto en outputs de CQ-028: pasos [6, 13] ---
{
 "id": "comision_sobre_importes_no_utilizados",
 "type": "comision_permitida",
 "label": "Comisión sobre importes no utilizados",
 "properties": {
  "description": "Comisión que los sujetos obligados pueden aplicar sobre los importes no utilizados de acuerdos de asignación de fondos, dado que su puesta a disposición configura la prestación del servicio.",
  "version": "vigente",
  "type_raw": [
   "Comisión permitida"
  ],
  "type_raw_counts": {
   "Comisión permitida": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.12-14 / Punto 2.3.2.1, párrafo inicial"
  }
 ]
}

  --- comision_por_precancelacion (SOLO provenance) | expuesto en outputs de CQ-028: pasos [1, 3, 4, 6, 7] ---
{
 "id": "comision_por_precancelacion",
 "type": "comision_permitida",
 "label": "Comisión por precancelación",
 "properties": {
  "description": "Comisión que puede aplicarse por precancelación total o parcial de financiaciones, con restricción en precancelación total cuando haya transcurrido al menos la cuarta parte del plazo original o 180 días.",
  "version": "vigente",
  "type_raw": [
   "Comisión permitida"
  ],
  "type_raw_counts": {
   "Comisión permitida": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.12-14 / Punto 2.3.2.1, párrafo segundo"
  }
 ]
}

  --- servicio_financiero_no_solicitado (SOLO provenance) | expuesto en outputs de CQ-028: NO ---
{
 "id": "servicio_financiero_no_solicitado",
 "type": "comision_prohibida",
 "label": "Servicio financiero no solicitado",
 "properties": {
  "description": "No pueden aplicarse comisiones ni cargos por servicios financieros que no hayan sido solicitados, pactados y/o autorizados por el usuario, ni aun cuando hayan sido solicitados pero no prestados de manera efectiva.",
  "version": "vigente",
  "type_raw": [
   "Comisión prohibida"
  ],
  "type_raw_counts": {
   "Comisión prohibida": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.12-14 / Punto 2.3.2.2.i, párrafo segundo"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 35, "n_consultas": 38, "top10": []}

  --- deposito_de_efectivo_en_pesos (SOLO provenance) | expuesto en outputs de CQ-028: NO ---
{
 "id": "deposito_de_efectivo_en_pesos",
 "type": "comision_prohibida",
 "label": "Depósito de efectivo en pesos",
 "properties": {
  "description": "No pueden aplicarse comisiones por depósitos de efectivo en pesos en cuentas cuyos titulares sean personas humanas o Mipyme.",
  "version": "vigente",
  "type_raw": [
   "Comisión prohibida"
  ],
  "type_raw_counts": {
   "Comisión prohibida": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.12-14 / Punto 2.3.2.2.ii.b"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 89, "n_consultas": 38, "top10": []}

  --- micro_pequena_o_mediana_empresa_mipyme (SOLO provenance) | expuesto en outputs de CQ-028: NO ---
{
 "id": "micro_pequena_o_mediana_empresa_mipyme",
 "type": "categoria_de_usuario",
 "label": "Micro, pequeña o mediana empresa (Mipyme)",
 "properties": {
  "description": "Categoría de persona jurídica que goza de protección especial respecto de comisiones por depósitos de efectivo en pesos, conforme a las condiciones previstas en el TO sobre Determinación de la Condición de Mipyme.",
  "version": "vigente",
  "type_raw": [
   "Categoría de usuario"
  ],
  "type_raw_counts": {
   "Categoría de usuario": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.12-14 / Punto 2.3.2.2.ii.b"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": null, "n_consultas": 38, "top10": []}

  --- contratacion_y_administracion_de_seguros (SOLO provenance) | expuesto en outputs de CQ-028: NO ---
{
 "id": "contratacion_y_administracion_de_seguros",
 "type": "comision_prohibida",
 "label": "Contratación y administración de seguros",
 "properties": {
  "description": "No pueden aplicarse comisiones por contratación y/o administración de seguros.",
  "version": "vigente",
  "type_raw": [
   "Comisión prohibida"
  ],
  "type_raw_counts": {
   "Comisión prohibida": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.12-14 / Punto 2.3.2.2.ii.c"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 1139, "n_consultas": 38, "top10": []}

  --- generacion_y_envio_de_resumenes_de_cuenta (SOLO provenance) | expuesto en outputs de CQ-028: NO ---
{
 "id": "generacion_y_envio_de_resumenes_de_cuenta",
 "type": "comision_prohibida",
 "label": "Generación y envío de resúmenes de cuenta",
 "properties": {
  "description": "No pueden aplicarse comisiones por generación de resúmenes de cuenta y envío de resúmenes virtuales, servicios que deben estar incluidos en la comisión por mantenimiento de cuenta.",
  "version": "vigente",
  "type_raw": [
   "Comisión prohibida"
  ],
  "type_raw_counts": {
   "Comisión prohibida": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.12-14 / Punto 2.3.2.2.ii.d"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 1183, "n_consultas": 38, "top10": []}

  --- evaluacion_otorgamiento_y_administracion_de_financiaciones (SOLO provenance) | expuesto en outputs de CQ-028: NO ---
{
 "id": "evaluacion_otorgamiento_y_administracion_de_financiaciones",
 "type": "comision_prohibida",
 "label": "Evaluación, otorgamiento y administración de financiaciones",
 "properties": {
  "description": "No pueden aplicarse comisiones por evaluación, otorgamiento y/o administración de financiaciones.",
  "version": "vigente",
  "type_raw": [
   "Comisión prohibida"
  ],
  "type_raw_counts": {
   "Comisión prohibida": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.12-14 / Punto 2.3.2.2.ii.e"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 1620, "n_consultas": 38, "top10": []}

  --- gastos_de_tasacion_notariales_o_de_escribania (SOLO provenance) | expuesto en outputs de CQ-028: NO ---
{
 "id": "gastos_de_tasacion_notariales_o_de_escribania",
 "type": "comision_prohibida",
 "label": "Gastos de tasación, notariales o de escribanía",
 "properties": {
  "description": "No pueden aplicarse comisiones por gastos de tasación, notariales o de escribanía que se originen en ocasión del otorgamiento o cancelación de financiaciones, tales como constitución de prenda o hipoteca.",
  "version": "vigente",
  "type_raw": [
   "Comisión prohibida"
  ],
  "type_raw_counts": {
   "Comisión prohibida": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.12-14 / Punto 2.3.2.2.ii.f"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 1338, "n_consultas": 38, "top10": []}

[4b] exposición con fragmento de cada término en los outputs:
  ['precancelacion'] exposición en outputs de run_4/CQ-028:
    paso 1 resultados[1] id=comision_por_precancelacion
       …{"id": "comision_por_precancelacion", "type": "comision_permitida", "label": "comision por…
    paso 1 resultados[1] id=comision_por_precancelacion
       …, "type": "comision_permitida", "label": "comision por precancelacion", "tokens_matcheados": 2, "resumen_propiedades": "comi…
    paso 1 resultados[5] id=precancelacion_de_deudas
       …{"id": "precancelacion_de_deudas", "type": "operacion_de_pago_anticipado", "l…
    paso 1 resultados[5] id=precancelacion_de_deudas
       …as", "type": "operacion_de_pago_anticipado", "label": "precancelacion de deudas", "tokens_matcheados": 1, "resumen_propiedad…
    paso 2 resultados[3] id=derecho_de_precancelacion_total_o_parcial
       …{"id": "derecho_de_precancelacion_total_o_parcial", "type": "contenido_contractual_oblig…
    paso 2 resultados[3] id=derecho_de_precancelacion_total_o_parcial
       …ntenido_contractual_obligatorio", "label": "derecho de precancelacion total o parcial", "tokens_matcheados": 2, "resumen_pro…
    paso 3 nodo id=comision_por_precancelacion
       …{"id": "comision_por_precancelacion", "type": "comision_permitida", "label": "comision por…
    paso 3 nodo id=comision_por_precancelacion
       …, "type": "comision_permitida", "label": "comision por precancelacion", "properties": {"description": "comision que puede ap…
    paso 5 resultados[1] id=derecho_de_precancelacion_total_o_parcial
       …{"id": "derecho_de_precancelacion_total_o_parcial", "type": "contenido_contractual_oblig…
    paso 5 resultados[1] id=derecho_de_precancelacion_total_o_parcial
       …ntenido_contractual_obligatorio", "label": "derecho de precancelacion total o parcial", "tokens_matcheados": 2, "resumen_pro…
    paso 6 resultados[1] id=comision_por_precancelacion
       …{"id": "comision_por_precancelacion", "type": "comision_permitida", "label": "comision por…
    paso 6 resultados[1] id=comision_por_precancelacion
       …, "type": "comision_permitida", "label": "comision por precancelacion", "tokens_matcheados": 2, "resumen_propiedades": "comi…
    paso 7 resultados[1] id=comision_por_precancelacion
       …{"id": "comision_por_precancelacion", "type": "comision_permitida", "label": "comision por…
    paso 7 resultados[1] id=comision_por_precancelacion
       …, "type": "comision_permitida", "label": "comision por precancelacion", "tokens_matcheados": 2, "resumen_propiedades": "comi…
    paso 7 resultados[3] id=precancelacion_de_linea_de_credito
       …{"id": "precancelacion_de_linea_de_credito", "type": "operacion_cambiaria", "…
    paso 7 resultados[3] id=precancelacion_de_linea_de_credito
       …_de_credito", "type": "operacion_cambiaria", "label": "precancelacion de linea de credito", "tokens_matcheados": 2, "resumen…
    paso 8 resultados[1] id=precancelacion_de_linea_de_credito
       …{"id": "precancelacion_de_linea_de_credito", "type": "operacion_cambiaria", "…
    paso 8 resultados[1] id=precancelacion_de_linea_de_credito
       …_de_credito", "type": "operacion_cambiaria", "label": "precancelacion de linea de credito", "tokens_matcheados": 3, "resumen…
    paso 11 resultados[2] id=precancelacion_de_linea_de_credito
       …{"id": "precancelacion_de_linea_de_credito", "type": "operacion_cambiaria", "…
    paso 11 resultados[2] id=precancelacion_de_linea_de_credito
       …_de_credito", "type": "operacion_cambiaria", "label": "precancelacion de linea de credito", "tokens_matcheados": 3, "resumen…

  ['180 dias'] exposición en outputs de run_4/CQ-028:
    paso 3 nodo id=comision_por_precancelacion
       …scurrido al menos la cuarta parte del plazo original o 180 dias.", "version": "vigente", "type_raw": ["comision permit…

  ['cuarta parte'] exposición en outputs de run_4/CQ-028:
    paso 3 nodo id=comision_por_precancelacion
       …cancelacion total cuando haya transcurrido al menos la cuarta parte del plazo original o 180 dias.", "version": "vigente",…

  ['criterio: 'primero' vs 'el mayor''] exposición en outputs de run_4/CQ-028:
    paso 2 resultados[10] id=posicion_neta_total
       … "tokens_matcheados": 1, "resumen_propiedades": "suma del mayor entre los valores absolutos de posiciones netas vendid…
    paso 5 resultados[9] id=posicion_neta_total
       … "tokens_matcheados": 1, "resumen_propiedades": "suma del mayor entre los valores absolutos de posiciones netas vendid…

[4d] secundario — exposición 'precancelacion parcial':
  ['precancelacion parcial'] exposición en outputs de run_4/CQ-028:
    AUSENTE en todos los outputs completos
```
