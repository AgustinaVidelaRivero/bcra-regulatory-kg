# Verificaciones de la adjudicación de la validación — parte 2: run_4 (puntos 3, 4, 6)

Fecha: 2026-07-16. Continuación de `verificaciones_validacion_1.md` (mismo mecanismo, misma
regla declarada de volumen; el CÓDIGO completo compartido está pegado en la parte 1).
**Solo hechos — cero adjudicación.**

## Output completo — run_4

```
==============================================================================
3. run_4/CQ-017 (16 outputs)
==============================================================================

[3a] barridos kg run_4:
  [barrido kg run_4: 'autorizadas a operar'] en id/label/properties: 2

  --- personas_juridicas_no_autorizadas_a_operar_en_cambios (props) | expuesto en outputs de CQ-017: pasos [13, 15, 16] ---
{
 "id": "personas_juridicas_no_autorizadas_a_operar_en_cambios",
 "type": "sujeto_regulado",
 "label": "Personas jurídicas no autorizadas a operar en cambios",
 "properties": {
  "description": "Personas jurídicas que no sean entidades autorizadas a operar en cambios, que requieren conformidad previa del BCRA para acceder al mercado de cambios para formación de activos externos y operaciones con derivados.",
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
   "location": "p.34-36 / Punto 3.10"
  }
 ]
}

  --- transferencia_a_cuenta_de_corresponsalia (props) | expuesto en outputs de CQ-017: NO ---
{
 "id": "transferencia_a_cuenta_de_corresponsalia",
 "type": "operacion_de_cambios",
 "label": "Transferencia a cuenta de corresponsalía",
 "properties": {
  "description": "Transferencia de activos externos líquidos a favor del cliente a una cuenta de corresponsalía de una entidad local autorizada a operar en cambios.",
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
   "location": "p.43-46 / Punto 3.16.2.1, inciso ii)"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 1077, "n_consultas": 36, "top10": []}
  [barrido kg run_4: 'deberan intervenir'] en id/label/properties: 0
  [barrido kg run_4: 'mercado libre de cambios'] en id/label/properties: 1

  --- mercado_libre_de_cambios (props) | expuesto en outputs de CQ-017: pasos [3, 10, 11, 12] ---
{
 "id": "mercado_libre_de_cambios",
 "type": "sistema_regulatorio",
 "label": "Mercado libre de cambios",
 "properties": {
  "description": "Mercado por el cual se cursan las operaciones de cambio realizadas por entidades financieras y demás personas autorizadas por el BCRA para dedicarse al comercio de compra y venta de monedas y billetes extranjeros, oro amonedado o en barra, cheques de viajero, giros, transferencias u operaciones análogas en moneda extranjera.",
  "version": "vigente",
  "type_raw": [
   "Sistema regulatorio"
  ],
  "type_raw_counts": {
   "Sistema regulatorio": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.183-185 / Sección 15.1, Artículo 1° del Decreto 260/02"
  }
 ]
}
  [barrido kg run_4: 'canje'] en id/label/properties: 24
    (> 12 candidatos: regla declarada — ids completos abajo; íntegros solo los que cruzan con 'cambio|mercado': 8)
    ids: ['operacion_de_cambio', 'operacion_de_canje_y_o_arbitraje', 'prima_de_participacion_recompra_o_rescate_anticipado', 'precancelacion_de_intereses_en_canje_de_titulos', 'intereses_devengados_a_fecha_de_cierre_del_canje', 'canje_de_titulos_de_deuda', 'intereses_devengados', 'operacion_de_canje', 'cobro_de_capital_de_bopreal', 'cobro_de_intereses_de_bopreal', 'canje_de_titulos_valores_emitidos_por_residentes_por_activos_externos', 'canje_y_arbitraje_con_fondos_depositados', 'cuenta_local', 'canje_y_arbitraje', 'operaciones_propias_de_la_entidad', 'operaciones_de_cambio_canje_o_arbitraje_con_el_bcra', 'operaciones_de_cambio_canje_o_arbitraje_con_otras_entidades', 'operaciones_de_arbitrajes_y_canjes_en_el_exterior', 'sucursal_o_agencia_en_el_exterior_de_bancos_oficiales_locales', 'canje', 'operacion_de_canje_de_titulos_de_deuda', 'canje_y_o_arbitraje', 'pago_a_la_vista', 'acciones_contabilizadas_como_prestamo']

  --- operacion_de_cambio (props) | expuesto en outputs de CQ-017: pasos [1, 3, 10] ---
{
 "id": "operacion_de_cambio",
 "type": "operacion_regulada",
 "label": "Operación de cambio",
 "properties": {
  "description": "Operación de cambio, canje y/o arbitraje que se cursa en el mercado de cambios y requiere boleto de compra y/o venta conforme a lo estipulado en el TO.",
  "version": "vigente",
  "type_raw": [
   "Operación regulada"
  ],
  "type_raw_counts": {
   "Operación regulada": 2
  },
  "name_variants": [],
  "n_observations": 2
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.5-8 / Punto 1.4"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.74-77 / Punto 5.13, 6.2.1"
  }
 ]
}

  --- operacion_de_canje_y_o_arbitraje (props) | expuesto en outputs de CQ-017: NO ---
{
 "id": "operacion_de_canje_y_o_arbitraje",
 "type": "tipo_de_operacion_de_cambio",
 "label": "Operación de canje y/o arbitraje",
 "properties": {
  "description": "Operación de cambio que puede realizarse con fondos depositados en cuenta local originados en cobros de capital o intereses de BOPREAL.",
  "version": "vigente",
  "type_raw": [
   "Tipo de operación de cambio"
  ],
  "type_raw_counts": {
   "Tipo de operación de cambio": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.16-18 / Punto 3.4.4.2"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 256, "n_consultas": 36, "top10": []}

  --- canje_de_titulos_de_deuda (props) | expuesto en outputs de CQ-017: NO ---
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
    D1: {"alcanzable": false, "mejor_rank": 388, "n_consultas": 36, "top10": []}

  --- canje_y_arbitraje_con_fondos_depositados (props) | expuesto en outputs de CQ-017: NO ---
{
 "id": "canje_y_arbitraje_con_fondos_depositados",
 "type": "mecanismo_de_pago",
 "label": "Canje y arbitraje con fondos depositados",
 "properties": {
  "description": "Mecanismo mediante el cual se puede acceder al mercado de cambios para pagar deudas de utilidades y dividendos, utilizando fondos depositados en cuenta local originados en cobros de capital e intereses de BOPREAL.",
  "version": "vigente",
  "type_raw": [
   "Mecanismo de pago"
  ],
  "type_raw_counts": {
   "Mecanismo de pago": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.60-62 / Punto 4.6.1.4"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 1698, "n_consultas": 36, "top10": []}

  --- operaciones_propias_de_la_entidad (props) | expuesto en outputs de CQ-017: NO ---
{
 "id": "operaciones_propias_de_la_entidad",
 "type": "operacion_regulada",
 "label": "Operaciones propias de la entidad",
 "properties": {
  "description": "Operaciones de cambio realizadas por la entidad en carácter de cliente, incluyendo cobros, pagos, cambio, canje o arbitraje.",
  "version": "vigente",
  "type_raw": [
   "Operación regulada"
  ],
  "type_raw_counts": {
   "Operación regulada": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.70-73 / Punto 5.10.1"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 48, "n_consultas": 36, "top10": []}

  --- operaciones_de_cambio_canje_o_arbitraje_con_el_bcra (props) | expuesto en outputs de CQ-017: NO ---
{
 "id": "operaciones_de_cambio_canje_o_arbitraje_con_el_bcra",
 "type": "operacion_regulada",
 "label": "Operaciones de cambio, canje o arbitraje con el BCRA",
 "properties": {
  "description": "Operaciones de cambio, canje o arbitraje realizadas entre la entidad y el BCRA.",
  "version": "vigente",
  "type_raw": [
   "Operación regulada"
  ],
  "type_raw_counts": {
   "Operación regulada": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.70-73 / Punto 5.10.1.2"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 31, "n_consultas": 36, "top10": []}

  --- operaciones_de_cambio_canje_o_arbitraje_con_otras_entidades (props) | expuesto en outputs de CQ-017: NO ---
{
 "id": "operaciones_de_cambio_canje_o_arbitraje_con_otras_entidades",
 "type": "operacion_regulada",
 "label": "Operaciones de cambio, canje o arbitraje con otras entidades",
 "properties": {
  "description": "Operaciones de cambio, canje o arbitraje realizadas entre la entidad y otras entidades financieras o cambiarias del país.",
  "version": "vigente",
  "type_raw": [
   "Operación regulada"
  ],
  "type_raw_counts": {
   "Operación regulada": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.70-73 / Punto 5.10.1.2"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 34, "n_consultas": 36, "top10": []}

  --- canje (props) | expuesto en outputs de CQ-017: pasos [1] ---
{
 "id": "canje",
 "type": "tipo_de_operacion",
 "label": "Canje",
 "properties": {
  "description": "Operación en la cual se intercambia con una misma contraparte dos instrumentos operados en el mercado de cambios expresados en la misma moneda extranjera.",
  "version": "vigente",
  "type_raw": [
   "Tipo de operación"
  ],
  "type_raw_counts": {
   "Tipo de operación": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.74-77 / Punto 6.2.2"
  }
 ]
}
  [barrido kg run_4: 'arbitraje'] en id/label/properties: 20
    (> 12 candidatos: regla declarada — ids completos abajo; íntegros solo los que cruzan con 'cambio|mercado': 8)
    ids: ['operacion_de_cambio', 'operacion_de_canje_y_o_arbitraje', 'operacion_de_arbitraje', 'cobro_de_capital_de_bopreal', 'cobro_de_intereses_de_bopreal', 'canje_y_arbitraje_con_fondos_depositados', 'cuenta_local', 'canje_y_arbitraje', 'operaciones_propias_de_la_entidad', 'operaciones_de_cambio_canje_o_arbitraje_con_el_bcra', 'operaciones_de_cambio_canje_o_arbitraje_con_otras_entidades', 'operaciones_de_arbitrajes_y_canjes_en_el_exterior', 'sucursal_o_agencia_en_el_exterior_de_bancos_oficiales_locales', 'arbitraje', 'canje_y_o_arbitraje', 'pago_a_la_vista', 'estrategia_de_arbitraje_con_futuros', 'estrategia_de_arbitraje_con_canasta_de_acciones', 'riesgo_de_divergencia', 'riesgo_de_ejecucion']

  --- operacion_de_cambio (props) | expuesto en outputs de CQ-017: pasos [1, 3, 10] ---
{
 "id": "operacion_de_cambio",
 "type": "operacion_regulada",
 "label": "Operación de cambio",
 "properties": {
  "description": "Operación de cambio, canje y/o arbitraje que se cursa en el mercado de cambios y requiere boleto de compra y/o venta conforme a lo estipulado en el TO.",
  "version": "vigente",
  "type_raw": [
   "Operación regulada"
  ],
  "type_raw_counts": {
   "Operación regulada": 2
  },
  "name_variants": [],
  "n_observations": 2
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.5-8 / Punto 1.4"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.74-77 / Punto 5.13, 6.2.1"
  }
 ]
}

  --- operacion_de_canje_y_o_arbitraje (props) | expuesto en outputs de CQ-017: NO ---
{
 "id": "operacion_de_canje_y_o_arbitraje",
 "type": "tipo_de_operacion_de_cambio",
 "label": "Operación de canje y/o arbitraje",
 "properties": {
  "description": "Operación de cambio que puede realizarse con fondos depositados en cuenta local originados en cobros de capital o intereses de BOPREAL.",
  "version": "vigente",
  "type_raw": [
   "Tipo de operación de cambio"
  ],
  "type_raw_counts": {
   "Tipo de operación de cambio": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.16-18 / Punto 3.4.4.2"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 256, "n_consultas": 36, "top10": []}

  --- canje_y_arbitraje_con_fondos_depositados (props) | expuesto en outputs de CQ-017: NO ---
{
 "id": "canje_y_arbitraje_con_fondos_depositados",
 "type": "mecanismo_de_pago",
 "label": "Canje y arbitraje con fondos depositados",
 "properties": {
  "description": "Mecanismo mediante el cual se puede acceder al mercado de cambios para pagar deudas de utilidades y dividendos, utilizando fondos depositados en cuenta local originados en cobros de capital e intereses de BOPREAL.",
  "version": "vigente",
  "type_raw": [
   "Mecanismo de pago"
  ],
  "type_raw_counts": {
   "Mecanismo de pago": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.60-62 / Punto 4.6.1.4"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 1698, "n_consultas": 36, "top10": []}

  --- operaciones_propias_de_la_entidad (props) | expuesto en outputs de CQ-017: NO ---
{
 "id": "operaciones_propias_de_la_entidad",
 "type": "operacion_regulada",
 "label": "Operaciones propias de la entidad",
 "properties": {
  "description": "Operaciones de cambio realizadas por la entidad en carácter de cliente, incluyendo cobros, pagos, cambio, canje o arbitraje.",
  "version": "vigente",
  "type_raw": [
   "Operación regulada"
  ],
  "type_raw_counts": {
   "Operación regulada": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.70-73 / Punto 5.10.1"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 48, "n_consultas": 36, "top10": []}

  --- operaciones_de_cambio_canje_o_arbitraje_con_el_bcra (props) | expuesto en outputs de CQ-017: NO ---
{
 "id": "operaciones_de_cambio_canje_o_arbitraje_con_el_bcra",
 "type": "operacion_regulada",
 "label": "Operaciones de cambio, canje o arbitraje con el BCRA",
 "properties": {
  "description": "Operaciones de cambio, canje o arbitraje realizadas entre la entidad y el BCRA.",
  "version": "vigente",
  "type_raw": [
   "Operación regulada"
  ],
  "type_raw_counts": {
   "Operación regulada": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.70-73 / Punto 5.10.1.2"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 31, "n_consultas": 36, "top10": []}

  --- operaciones_de_cambio_canje_o_arbitraje_con_otras_entidades (props) | expuesto en outputs de CQ-017: NO ---
{
 "id": "operaciones_de_cambio_canje_o_arbitraje_con_otras_entidades",
 "type": "operacion_regulada",
 "label": "Operaciones de cambio, canje o arbitraje con otras entidades",
 "properties": {
  "description": "Operaciones de cambio, canje o arbitraje realizadas entre la entidad y otras entidades financieras o cambiarias del país.",
  "version": "vigente",
  "type_raw": [
   "Operación regulada"
  ],
  "type_raw_counts": {
   "Operación regulada": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.70-73 / Punto 5.10.1.2"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 34, "n_consultas": 36, "top10": []}

  --- arbitraje (props) | expuesto en outputs de CQ-017: pasos [1] ---
{
 "id": "arbitraje",
 "type": "tipo_de_operacion",
 "label": "Arbitraje",
 "properties": {
  "description": "Operación en la cual se intercambia con una misma contraparte instrumentos operados en el mercado de cambios expresados en distinta moneda extranjera.",
  "version": "vigente",
  "type_raw": [
   "Tipo de operación"
  ],
  "type_raw_counts": {
   "Tipo de operación": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.74-77 / Punto 6.2.3"
  }
 ]
}

  --- estrategia_de_arbitraje_con_futuros (props) | expuesto en outputs de CQ-017: NO ---
{
 "id": "estrategia_de_arbitraje_con_futuros",
 "type": "estrategia_de_negociacion",
 "label": "Estrategia de arbitraje con futuros",
 "properties": {
  "description": "Estrategia donde la entidad asume posiciones contrarias en futuros sobre índices a distintos vencimientos, mercados o índices similares.",
  "version": "vigente",
  "type_raw": [
   "Estrategia de negociación"
  ],
  "type_raw_counts": {
   "Estrategia de negociación": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.127-130 / Punto 6.3.2.2.iii)a)"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 851, "n_consultas": 36, "top10": []}

[3a-provs] nodos con provenance 'Punto 1.1' del TO Exterior (aparte):
  3 nodos: ['entidad_financiera', 'mercado_de_cambios', 'entidad_cambiaria']

  --- entidad_financiera ---
{
 "id": "entidad_financiera",
 "type": "sujeto_regulado",
 "label": "Entidad financiera",
 "properties": {
  "description": "Entidades financieras que deben verificar el listado de CUITs con operaciones inconsistentes y reforzar medidas de control, así como abstenerse de cursar operaciones ante detección de inconsistencias.",
  "version": "vigente",
  "type_raw": [
   "Sujeto obligado",
   "Agente regulado",
   "Sujeto regulado",
   "Institución regulada",
   "Sujeto regulador",
   "Intermediario regulado",
   "Sujeto regulatorio",
   "Participante esencial del mercado"
  ],
  "type_raw_counts": {
   "Sujeto regulado": 27,
   "Sujeto regulatorio": 2,
   "Participante esencial del mercado": 1,
   "Institución regulada": 1,
   "Sujeto regulador": 1,
   "Agente regulado": 2,
   "Intermediario regulado": 2,
   "Sujeto obligado": 2
  },
  "name_variants": [],
  "n_observations": 38
 },
 "provenances": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.1-5 / Punto 1.1.2.1"
  },
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.6-8 / Múltiples puntos"
  },
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.18-20 / Sección 2.4"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "p.9-12 / Puntos 3.1, 3.2, 3.3, 3.4"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "p.23-25 / Párrafo inicial sobre acuerdo con entidad financiera"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "p.33-35 / Punto 7.1"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "p.39-43 / Sección 9, punto 9.1"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "p.1-5 / Sección 2"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.5-8 / Punto 1.1"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.31-33 / Puntos 3.6.4.3 a 3.9.5"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.37-39 / Punto 3.13.1.5"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.47-49 / Punto 3.16.4"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.50-52 / Punto 3.16.4"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.63-65 / Punto 4.6 y 4.7"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.66-69 / Múltiples puntos"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.74-77 / Punto 5.13, 5.14, 5.15"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.106-109 / Punto 8.2"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.116-118 / Punto 8.5.11"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.129-132 / Punto 10.1"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.150-152 / Punto 10.7.1"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.160-162 / Punto 11.1"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.171-173 / Punto 13.5"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.174-176 / Punto 13.6"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.183-185 / Punto iii)"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.11-13 / Punto 2.5.5, 2.6.1"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.66-69 / Múltiples puntos"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.70-73 / Párrafo inicial y múltiples referencias"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.83-85 / Punto 4.2.2, párrafo inicial"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.86-88 / Punto 4.3.2"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.100-102 / 5.2.2.1, 5.2.2.2, 5.2.2.3, 5.2.2.4"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.103-106 / Punto 5.3.1.4, acápite ii)"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.134-137 / Punto 6.5 y siguientes"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.138-141 / Sección 6.7.2.1, 6.8, 6.9, 6.10"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.155-157 / Punto 8.2.1 y siguientes"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.158-160 / Múltiples referencias en todo el fragmento"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.167-170 / Punto 8.4.2.1, 8.4.2.2, 8.5, 8.6"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.171-174 / Sección 9.1, 9.2"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.175-178 / Punto 10.3.3.2"
  }
 ]
}

  --- mercado_de_cambios ---
{
 "id": "mercado_de_cambios",
 "type": "mercado_regulado",
 "label": "Mercado de cambios",
 "properties": {
  "description": "Mercado donde se realizan operaciones de cambio de divisas, regulado por el BCRA con pautas operativas, horarios de funcionamiento, y requisitos de identificación de clientes.",
  "version": "vigente",
  "type_raw": [
   "Mercado regulado",
   "Mecanismo regulatorio",
   "Mecanismo operativo",
   "Mercado regulatorio",
   "Mecanismo regulado",
   "Mecanismo de acceso regulado",
   "Mecanismo de acceso regulatorio"
  ],
  "type_raw_counts": {
   "Mercado regulado": 19,
   "Mecanismo regulatorio": 5,
   "Mecanismo operativo": 1,
   "Mercado regulatorio": 1,
   "Mecanismo regulado": 1,
   "Mecanismo de acceso regulado": 1,
   "Mecanismo de acceso regulatorio": 1
  },
  "name_variants": [],
  "n_observations": 29
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.5-8 / Punto 1.1"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.12-15 / Punto 2.5"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.16-18 / Punto 3, párrafo introductorio"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.25-27 / Punto 3.5.4, 3.5.5, 3.5.6"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.28-30 / Punto 3.6.1 y siguientes"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.37-39 / Punto 3.13.1.7"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.63-65 / Punto 4.6, 4.7 y 4.8"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.66-69 / Sección 5"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.70-73 / Punto 5.5.4"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.78-81 / Punto 7.1.1"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.82-84 / Punto 7.1.4"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.85-87 / Punto 7.3.11"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.94-96 / Punto 7.8.5.1"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.110-112 / Sección 8.4.3.1"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.119-122 / 8.5.18.2"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.129-132 / Punto 10.1"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.133-136 / Múltiples referencias"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.140-142 / Punto 10.4.2.4 y siguientes"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.146-149 / Punto 10.5.5.1, inciso v)"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.150-152 / Múltiples referencias en toda la sección"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.153-155 / Puntos 10.9.1 a 10.9.4, 10.10.1 a 10.10.2.4"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.156-159 / Múltiples puntos"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.160-162 / Punto 11.1"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.163-167 / Puntos 11.1.4, 11.2"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.168-170 / 13.1, 13.1.5"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.171-173 / Punto 13.3.2, 13.3.3, 13.5"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.174-176 / Punto 13.6, punto 3.15.1"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.177-179 / Puntos 14.2.1.6 a 14.4.1"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.180-182 / Punto 14.4.1, 14.4.2"
  }
 ]
}

  --- entidad_cambiaria ---
{
 "id": "entidad_cambiaria",
 "type": "sujeto_regulado",
 "label": "Entidad cambiaria",
 "properties": {
  "description": "Instituciones especializadas en operaciones de cambio que deben suspender sus operaciones en caso de atraso en la validación del régimen informativo.",
  "version": "vigente",
  "type_raw": [
   "Sujeto regulado",
   "Tipo de entidad financiera"
  ],
  "type_raw_counts": {
   "Tipo de entidad financiera": 1,
   "Sujeto regulado": 2
  },
  "name_variants": [],
  "n_observations": 3
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.5-8 / Punto 1.1"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.74-77 / Punto 5.15"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.14-17 / Punto 2.7.1, inciso i"
  }
 ]
}

[3b] nodos operador-de-cambio en run_4 (íntegros + TODOS sus edges) y chequeo 0-aristas:
  nodos operador-de-cambio: 1: ['operador_de_cambio']

  --- operador_de_cambio | expuesto: pasos [1, 4, 5, 6, 14] ---
{
 "id": "operador_de_cambio",
 "type": "sujeto_obligado",
 "label": "Operador de cambio",
 "properties": {
  "description": "Sujeto obligado que realiza operaciones comprendidas en las normas sobre Exterior y cambios.",
  "version": "vigente",
  "type_raw": [
   "Sujeto obligado"
  ],
  "type_raw_counts": {
   "Sujeto obligado": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.1-5 / Punto 1.1.2.2"
  }
 ]
}
    edges de operador_de_cambio: 0 salientes, 2 entrantes
    ENTRANTE: {"relation": "utiliza_servicios_de", "source": "usuario_de_servicios_financieros", "provenances": [{"source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf", "location": "p.1-5 / Punto 1.1.1"}]}
    ENTRANTE: {"relation": "supervisa", "source": "banco_central_de_la_republica_argentina", "provenances": [{"source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf", "location": "p.1-5 / Punto 1.2"}]}

  aristas operador↔(entidad-autorizada|mercado-de-cambios) sobre 3434 edges: 0

[3c] exposición y D1 de candidatos de 3a:
  mercado_libre_de_cambios: expuesto=pasos [3, 10, 11, 12]
  personas_juridicas_no_autorizadas_a_operar_en_cambios: expuesto=pasos [13, 15, 16]
  transferencia_a_cuenta_de_corresponsalia: expuesto=NO
    D1: {"alcanzable": false, "mejor_rank": 1077, "n_consultas": 36, "top10": []}

[3d] secundarios — exposición y nodos fuente:
  ['mercado libre de cambios (output)'] exposición en outputs de run_4/CQ-017:
    paso 3 resultados[2] id=mercado_libre_de_cambios
       …ambios", "type": "sistema_regulatorio", "label": "mercado libre de cambios", "tokens_matcheados": 3, "resumen_propiedades": …
    paso 10 resultados[3] id=mercado_libre_de_cambios
       …ambios", "type": "sistema_regulatorio", "label": "mercado libre de cambios", "tokens_matcheados": 2, "resumen_propiedades": …
    paso 11 nodo id=mercado_libre_de_cambios
       …ambios", "type": "sistema_regulatorio", "label": "mercado libre de cambios", "properties": {"description": "mercado por el c…
  [''no autorizadas' (output)'] exposición en outputs de run_4/CQ-017:
    paso 13 resultados[4] id=personas_juridicas_no_autorizadas_a_operar_en_cambios
       …: "sujeto_regulado", "label": "personas juridicas no autorizadas a operar en cambios", "tokens_matcheados": 2, "re…
    paso 15 nodo id=personas_juridicas_no_autorizadas_a_operar_en_cambios
       …: "sujeto_regulado", "label": "personas juridicas no autorizadas a operar en cambios", "properties": {"description…
  ['conformidad previa (output)'] exposición en outputs de run_4/CQ-017:
    paso 13 resultados[4] id=personas_juridicas_no_autorizadas_a_operar_en_cambios
       …es autorizadas a operar en cambios, que requieren conformidad previa del bcra para acceder al mercado de cambios para …
    paso 15 nodo id=personas_juridicas_no_autorizadas_a_operar_en_cambios
       …es autorizadas a operar en cambios, que requieren conformidad previa del bcra para acceder al mercado de cambios para …

==============================================================================
4. run_4/CQ-020 (15 outputs)
==============================================================================

[4a] exposición:

  ['sefyc'] exposición en outputs de run_4/CQ-020:
    paso 14 resultados[5] id=factor_k
       …a la entidad segun la evaluacion efectuada por la sefyc, con valores que varian de 1 a 1,19 segun la cali…
    paso 14 resultados[7] id=calificacion_sefyc
       …{"id": "calificacion_sefyc", "type": "evaluacion_regulatoria", "label": "cal…

  ['1,03'] exposición en outputs de run_4/CQ-020:
    AUSENTE en todos los outputs completos

  ['1,08'] exposición en outputs de run_4/CQ-020:
    AUSENTE en todos los outputs completos

  ['1,13'] exposición en outputs de run_4/CQ-020:
    AUSENTE en todos los outputs completos

  ['1,19'] exposición en outputs de run_4/CQ-020:
    paso 14 resultados[5] id=factor_k
       …tuada por la sefyc, con valores que varian de 1 a 1,19 segun la calificacion (1…"}…

  ['ponderadores'] exposición en outputs de run_4/CQ-020:
    paso 14 resultados[4] id=aprc
       …ados mediante suma de valores obtenidos aplicando ponderadores de riesgo a activos computables, partidas fuera…"…

  ['activos computables'] exposición en outputs de run_4/CQ-020:
    paso 7 resultados[1] id=activos_ponderados_por_riesgo_de_credito
       …, "tokens_matcheados": 4, "resumen_propiedades": "activos computables ponderados segun factores de riesgo, utilizados e…
    paso 8 nodo id=activos_ponderados_por_riesgo_de_credito
       …iesgo de credito", "properties": {"description": "activos computables ponderados segun factores de riesgo, utilizados e…
    paso 11 resultados[2] id=activos_ponderados_por_riesgo_de_credito
       …, "tokens_matcheados": 3, "resumen_propiedades": "activos computables ponderados segun factores de riesgo, utilizados e…
    paso 14 resultados[4] id=aprc
       …ores obtenidos aplicando ponderadores de riesgo a activos computables, partidas fuera…"}…

  ['regimen informativo (∧capital anotado)'] exposición en outputs de run_4/CQ-020:
    paso 10 resultados[1] id=regimen_informativo_del_bcra
       …bcra", "type": "requisito_regulatorio", "label": "regimen informativo del bcra", "tokens_matcheados": 2, "resumen_propi…
    paso 10 resultados[2] id=regimen_informativo_de_operaciones_cambiarias
       …rias", "type": "requisito_regulatorio", "label": "regimen informativo de operaciones cambiarias", "tokens_matcheados": …
    paso 10 resultados[3] id=regimen_informativo_de_operaciones_de_cambios
       …pe": "sistema_informatico_regulatorio", "label": "regimen informativo de operaciones de cambios", "tokens_matcheados": …
    paso 10 resultados[4] id=regimen_informativo_de_operaciones_de_cambio_rioc
       …rioc", "type": "mecanismo_de_registro", "label": "regimen informativo de operaciones de cambio (rioc)", "tokens_matchea…
    paso 10 resultados[5] id=regimen_informativo_de_operaciones_de_cambios_rioc
       …s_rioc", "type": "sistema_de_registro", "label": "regimen informativo de operaciones de cambios (rioc)", "tokens_matche…

[4b-i] kg run_4: frecuencia/periodicidad/mensual ∧ credito|crc:
  [barrido kg run_4: 'freq ∧ credito'] en id/label/properties: 0

[4b-ii] kg run_4: frecuencia general del régimen:
  [barrido kg run_4: 'frecuencia general'] en id/label/properties: 13

  --- prestamo_personal (props) | expuesto en outputs de CQ-020: NO ---
{
 "id": "prestamo_personal",
 "type": "producto_de_credito",
 "label": "Préstamo personal",
 "properties": {
  "description": "Préstamo en cuotas cuya información debe incluir importe del capital, monto total a pagar, cantidad de cuotas, periodicidad, vencimiento y sistema de amortización.",
  "version": "vigente",
  "type_raw": [
   "Producto financiero",
   "Producto de crédito"
  ],
  "type_raw_counts": {
   "Producto de crédito": 1,
   "Producto financiero": 1
  },
  "name_variants": [],
  "n_observations": 2
 },
 "provenances": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.9-11 / Punto 2.3.1.4, inciso vi"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.14-17 / Punto 2.8.3.1"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": null, "n_consultas": 29, "top10": []}

  --- prestamo_prendario (props) | expuesto en outputs de CQ-020: NO ---
{
 "id": "prestamo_prendario",
 "type": "producto_de_credito",
 "label": "Préstamo prendario",
 "properties": {
  "description": "Préstamo garantizado con prenda cuya información debe incluir importe del capital, monto total a pagar, cantidad de cuotas, periodicidad, vencimiento y sistema de amortización.",
  "version": "vigente",
  "type_raw": [
   "Producto financiero",
   "Producto de crédito"
  ],
  "type_raw_counts": {
   "Producto de crédito": 1,
   "Producto financiero": 1
  },
  "name_variants": [],
  "n_observations": 2
 },
 "provenances": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.9-11 / Punto 2.3.1.4, inciso vi"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.14-17 / Punto 2.8.3.1"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": null, "n_consultas": 29, "top10": []}

  --- prestamo_hipotecario (props) | expuesto en outputs de CQ-020: NO ---
{
 "id": "prestamo_hipotecario",
 "type": "producto_financiero",
 "label": "Préstamo hipotecario",
 "properties": {
  "description": "Préstamo garantizado con hipoteca cuya información debe incluir importe del capital, monto total a pagar, cantidad de cuotas, periodicidad, vencimiento y sistema de amortización.",
  "version": "vigente",
  "type_raw": [
   "Producto financiero"
  ],
  "type_raw_counts": {
   "Producto financiero": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.9-11 / Punto 2.3.1.4, inciso vi"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": null, "n_consultas": 29, "top10": []}

  --- cuenta_de_deposito (props) | expuesto en outputs de CQ-020: NO ---
{
 "id": "cuenta_de_deposito",
 "type": "producto_financiero",
 "label": "Cuenta de depósito",
 "properties": {
  "description": "Cuenta de depósito cuya información debe incluir periodicidad de generación del resumen de cuenta, plazo para su envío y mecanismo para reclamar objeciones a movimientos o consumos.",
  "version": "vigente",
  "type_raw": [
   "Producto financiero"
  ],
  "type_raw_counts": {
   "Producto financiero": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.9-11 / Punto 2.3.1.4, inciso viii"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 762, "n_consultas": 29, "top10": []}

  --- reporte_trimestral (props) | expuesto en outputs de CQ-020: pasos [3, 13] ---
{
 "id": "reporte_trimestral",
 "type": "documento_obligatorio",
 "label": "Reporte trimestral",
 "properties": {
  "description": "Reporte que debe elaborar y elevar el responsable de atención al usuario con periodicidad mínima trimestral, conteniendo información sobre consultas, reclamos, intervenciones requeridas y reintegros de importes.",
  "version": "vigente",
  "type_raw": [
   "Documento obligatorio"
  ],
  "type_raw_counts": {
   "Documento obligatorio": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.21-24 / Punto 3.1.1.8"
  }
 ]
}

  --- clasificacion_de_deudores (props) | expuesto en outputs de CQ-020: pasos [11] ---
{
 "id": "clasificacion_de_deudores",
 "type": "tarea_regulatoria",
 "label": "Clasificación de deudores",
 "properties": {
  "description": "Clasificación que debe efectuarse con una periodicidad que atienda a la importancia del deudor, considerando la totalidad de las financiaciones comprendidas, debiendo documentarse el análisis efectuado.",
  "version": "vigente",
  "type_raw": [
   "Proceso regulatorio",
   "Tarea regulatoria"
  ],
  "type_raw_counts": {
   "Proceso regulatorio": 1,
   "Tarea regulatoria": 1
  },
  "name_variants": [],
  "n_observations": 2
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "p.1-8 / Sección 1.1"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "p.9-12 / Punto 3.2"
  }
 ]
}

  --- fiduciario_de_fideicomiso_financiero (props) | expuesto en outputs de CQ-020: NO ---
{
 "id": "fiduciario_de_fideicomiso_financiero",
 "type": "sujeto_regulado",
 "label": "Fiduciario de fideicomiso financiero",
 "properties": {
  "description": "Entidad responsable de administrar créditos fideicomitidos y clasificar deudores según periodicidad y condiciones de cartera comercial o consumo/vivienda.",
  "version": "vigente",
  "type_raw": [
   "Sujeto regulado"
  ],
  "type_raw_counts": {
   "Sujeto regulado": 2
  },
  "name_variants": [],
  "n_observations": 2
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "p.1-8 / Sección 10.2"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "p.39-43 / Sección 10, punto 10.2.1"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 1507, "n_consultas": 29, "top10": []}

  --- garantias_preferidas_b (props) | expuesto en outputs de CQ-020: NO ---
{
 "id": "garantias_preferidas_b",
 "type": "tipo_de_garantia",
 "label": "Garantías preferidas B",
 "properties": {
  "description": "Garantías que permiten a la entidad requerir información con frecuencia específica para evaluar al deudor, observando periodicidad mínima.",
  "version": "vigente",
  "type_raw": [
   "Tipo de garantía"
  ],
  "type_raw_counts": {
   "Tipo de garantía": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "p.20-22 / Punto 6.5.1.4, 6.5.2.1"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": null, "n_consultas": 29, "top10": []}

  --- deudor_no_evaluado_periodicamente (props) | expuesto en outputs de CQ-020: NO ---
{
 "id": "deudor_no_evaluado_periodicamente",
 "type": "categoria_de_deudor",
 "label": "Deudor no evaluado periódicamente",
 "properties": {
  "description": "Cliente que, por cualquier motivo incluyendo falta de legajo o información no confiable, no haya sido evaluado con la periodicidad correspondiente.",
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
   "location": "p.29-32 / Punto 6.5.5.9"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": null, "n_consultas": 29, "top10": []}

  --- informacion_de_frecuencia_mensual (props) | expuesto en outputs de CQ-020: NO ---
{
 "id": "informacion_de_frecuencia_mensual",
 "type": "requisito_de_reporte",
 "label": "Información de frecuencia mensual",
 "properties": {
  "description": "Información que se integra con datos referidos al mes bajo análisis, con excepciones para ciertos datos que tienen frecuencia trimestral.",
  "version": "vigente",
  "type_raw": [
   "Requisito de reporte"
  ],
  "type_raw_counts": {
   "Requisito de reporte": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "p.1-5 / Punto 1.1"
  }
 ]
}
    D1: {"alcanzable": true, "mejor_rank": 2, "n_consultas": 29, "top10": [{"consulta": "crc frecuencia", "rank": 3}, {"consulta": "frecuencia se", "rank": 2}, {"consulta": "crc frecuencia se", "rank": 3}, {"consulta": "frecuencia se reporta", "rank": 2}]}

  --- kccp (props) | expuesto en outputs de CQ-020: NO ---
{
 "id": "kccp",
 "type": "requerimiento_de_capital",
 "label": "KCCP",
 "properties": {
  "description": "Requerimiento de capital de la CCP que debe calcularse con periodicidad trimestral mínima.",
  "version": "vigente",
  "type_raw": [
   "Requerimiento de capital"
  ],
  "type_raw_counts": {
   "Requerimiento de capital": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.96-99 / Párrafo sobre periodicidad de cálculo"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": null, "n_consultas": 29, "top10": []}

  --- supuestos_y_parametros_de_modelo (props) | expuesto en outputs de CQ-020: NO ---
{
 "id": "supuestos_y_parametros_de_modelo",
 "type": "componente_de_modelo",
 "label": "Supuestos y parámetros de modelo",
 "properties": {
  "description": "Estimaciones utilizadas en modelos de valuación que deben ser fiables y evaluadas con periodicidad diaria.",
  "version": "vigente",
  "type_raw": [
   "Componente de modelo"
  ],
  "type_raw_counts": {
   "Componente de modelo": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.138-141 / Sección 6.8.3.3, 6.9.2.4"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 261, "n_consultas": 29, "top10": []}

  --- verificacion_independiente_de_precios (props) | expuesto en outputs de CQ-020: NO ---
{
 "id": "verificacion_independiente_de_precios",
 "type": "procedimiento_regulatorio",
 "label": "Verificación independiente de precios",
 "properties": {
  "description": "Proceso de verificación periódica de la exactitud de precios o datos de modelo, a cargo de una unidad independiente del dealing room, con periodicidad al menos mensual.",
  "version": "vigente",
  "type_raw": [
   "Procedimiento regulatorio"
  ],
  "type_raw_counts": {
   "Procedimiento regulatorio": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.142-145 / Sección iii)"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 1570, "n_consultas": 29, "top10": []}

[4c-i] kg run_4: escala k ('1,19' | calificacion ∧ token k):
  [barrido kg run_4: '1,19'] en id/label/properties: 1

  --- factor_k (props) | expuesto en outputs de CQ-020: pasos [14] ---
{
 "id": "factor_k",
 "type": "componente_de_calculo_de_capital",
 "label": "Factor k",
 "properties": {
  "description": "Factor vinculado a la calificación asignada a la entidad según la evaluación efectuada por la SEFYC, con valores que varían de 1 a 1,19 según la calificación (1 a 5).",
  "version": "vigente",
  "type_raw": [
   "Componente de cálculo de capital"
  ],
  "type_raw_counts": {
   "Componente de cálculo de capital": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.7-10 / Punto 2.1. Exigencia, tabla de factor k"
  }
 ]
}
  [calificacion ∧ token 'k']: 1: ['factor_k']

  --- factor_k | expuesto: pasos [14] ---
{
 "id": "factor_k",
 "type": "componente_de_calculo_de_capital",
 "label": "Factor k",
 "properties": {
  "description": "Factor vinculado a la calificación asignada a la entidad según la evaluación efectuada por la SEFYC, con valores que varían de 1 a 1,19 según la calificación (1 a 5).",
  "version": "vigente",
  "type_raw": [
   "Componente de cálculo de capital"
  ],
  "type_raw_counts": {
   "Componente de cálculo de capital": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.7-10 / Punto 2.1. Exigencia, tabla de factor k"
  }
 ]
}

[4c-ii] kg run_4: 'ponderadores' | 'aprc':
  [barrido kg run_4: 'ponderadores|aprc'] en id/label/properties: 37
    (> 12 candidatos: regla declarada — ids completos abajo; íntegros solo los que cruzan con 'riesgo de credito|capital|activos computables': 10)
    ids: ['debida_diligencia_de_entidades_financieras_grupo_1', 'partidas_fuera_de_balance', 'ponderador_de_riesgo_de_contraparte', 'operaciones_sin_entrega_contra_pago', 'enfoque_simple_o_de_sustitucion_de_ponderadores', 'exposiciones_sujetas_a_multiplicador', 'activos_ponderados_por_riesgo', 'exigencia_por_riesgo_de_credito_sin_incluir_el_termino_inc', 'organismos_internacionales', 'grupo_2', 'crc', 'aprc', 'activos_computables', 'entidad_de_calificacion_externa_ecai', 'calificacion_de_credito', 'metodo_de_evaluacion_del_riesgo_de_credito_estandarizado_scra', 'moneda_de_ingresos', 'pais_de_constitucion', 'ponderadores_de_riesgo', 'exposicion_al_sector_publico_no_financiero_y_al_bcra_demas', 'exposicion_a_otros_estados_soberanos', 'exposicion_a_entes_del_sector_publico_no_financiero_de_otros_estados_soberanos', 'exposicion_a_sector_publico_no_financiero_provincial_por_titulos_publicos', 'exposicion_a_bmd_demas', 'exposicion_a_entidades_financieras_del_grupo_1_scra', 'exposicion_a_entidades_financieras_del_grupo_2', 'exposicion_con_garantia_hipotecaria_normativa_sobre_inmueble_residencial', 'enfoque_estandarizado', 'tratamiento_de_transparencia', 'criterios_stc', 'titulizacion_simple_transparente_y_comparable_stc', 'informacion_financiera_trimestral', 'ponderador_de_riesgo_de_terceros', 'metodo_simple', 'metodo_de_sustitucion_de_ponderadores', 'moneda_residual', 'agente_de_calificacion_externa_ecai']

  --- operaciones_sin_entrega_contra_pago (props) | expuesto en outputs de CQ-020: NO ---
{
 "id": "operaciones_sin_entrega_contra_pago",
 "type": "tipo_de_operacion",
 "label": "Operaciones sin entrega contra pago",
 "properties": {
  "description": "Operaciones no DvP a las que se aplican ponderadores de riesgo según el punto 4.1.2. de las normas sobre Capitales mínimos.",
  "version": "vigente",
  "type_raw": [
   "Tipo de operación",
   "Categoría de exposición"
  ],
  "type_raw_counts": {
   "Tipo de operación": 2,
   "Categoría de exposición": 1
  },
  "name_variants": [],
  "n_observations": 3
 },
 "provenances": [
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "p.6-10 / Sección 3.1, definición de no DvP"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "p.6-10 / Sección 3.1.4, tabla de modelo de información"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.7-10 / Punto 2.1. Exigencia, definición de no DvP"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": null, "n_consultas": 29, "top10": []}

  --- activos_ponderados_por_riesgo (props) | expuesto en outputs de CQ-020: pasos [6, 7, 8, 11, 12] ---
{
 "id": "activos_ponderados_por_riesgo",
 "type": "medida_de_riesgo",
 "label": "Activos ponderados por riesgo",
 "properties": {
  "description": "Resultado de aplicar la fórmula APR = APRc + [(RM+RO) x 12,5], donde APRc es activos ponderados por riesgo de crédito, RM es exigencia por riesgo de mercado y RO es exigencia por riesgo operacional.",
  "version": "vigente",
  "type_raw": [
   "Medida de Riesgo",
   "Concepto de exigencia de capital",
   "Concepto regulatorio",
   "Medida de exposición",
   "Medida regulatoria"
  ],
  "type_raw_counts": {
   "Concepto regulatorio": 1,
   "Medida de exposición": 1,
   "Medida regulatoria": 1,
   "Medida de Riesgo": 1,
   "Concepto de exigencia de capital": 1
  },
  "name_variants": [],
  "n_observations": 5
 },
 "provenances": [
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "p.31-35 / Sección 6.3"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "p.36-39 / Sección 8.1.9, código 70900000"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.29-31 / Punto 3.1.2.2"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.39-41 / Punto 3.1.8.2"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.167-170 / Punto 8.5"
  }
 ]
}

  --- exigencia_por_riesgo_de_credito_sin_incluir_el_termino_inc (props) | expuesto en outputs de CQ-020: NO ---
{
 "id": "exigencia_por_riesgo_de_credito_sin_incluir_el_termino_inc",
 "type": "concepto_de_exigencia_de_capital",
 "label": "Exigencia por riesgo de crédito sin incluir el término INC",
 "properties": {
  "description": "Exigencia de capital mínimo calculada según riesgo de crédito, excluyendo el término INC, determinada mediante fórmula específica que incluye códigos de partida y ponderadores.",
  "version": "vigente",
  "type_raw": [
   "Concepto de exigencia de capital"
  ],
  "type_raw_counts": {
   "Concepto de exigencia de capital": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "p.36-39 / Sección 8.1.1, código 70100000"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 14, "n_consultas": 29, "top10": []}

  --- crc (props) | expuesto en outputs de CQ-020: pasos [1, 5, 14] ---
{
 "id": "crc",
 "type": "exigencia_de_capital",
 "label": "CRC",
 "properties": {
  "description": "Exigencia de capital por riesgo de crédito, determinada mediante la fórmula CRC = (k x 0,08 x APRC) + INC.",
  "version": "vigente",
  "type_raw": [
   "Exigencia de capital"
  ],
  "type_raw_counts": {
   "Exigencia de capital": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.7-10 / Punto 2.1. Exigencia"
  }
 ]
}

  --- aprc (props) | expuesto en outputs de CQ-020: pasos [14] ---
{
 "id": "aprc",
 "type": "componente_de_calculo_de_capital",
 "label": "APRC",
 "properties": {
  "description": "Activos ponderados por riesgo de crédito, determinados mediante suma de valores obtenidos aplicando ponderadores de riesgo a activos computables, partidas fuera de balance, operaciones sin entrega contra pago, operaciones fallidas, riesgo de crédito de contraparte en derivados OTC e incrementos por excesos en inversiones significativas.",
  "version": "vigente",
  "type_raw": [
   "Componente de cálculo de capital"
  ],
  "type_raw_counts": {
   "Componente de cálculo de capital": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.7-10 / Punto 2.1. Exigencia"
  }
 ]
}

  --- activos_computables (props) | expuesto en outputs de CQ-020: NO ---
{
 "id": "activos_computables",
 "type": "componente_de_aprc",
 "label": "Activos computables",
 "properties": {
  "description": "Exposiciones que se incluyen en el cálculo de activos ponderados por riesgo de crédito.",
  "version": "vigente",
  "type_raw": [
   "Componente de APRC"
  ],
  "type_raw_counts": {
   "Componente de APRC": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.7-10 / Punto 2.1. Exigencia, definición de A"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 32, "n_consultas": 29, "top10": []}

  --- metodo_de_evaluacion_del_riesgo_de_credito_estandarizado_scra (props) | expuesto en outputs de CQ-020: NO ---
{
 "id": "metodo_de_evaluacion_del_riesgo_de_credito_estandarizado_scra",
 "type": "metodologia_regulatoria",
 "label": "Método de Evaluación del Riesgo de Crédito Estandarizado (SCRA)",
 "properties": {
  "description": "Método utilizado por entidades financieras del grupo 1 para asignar ponderadores de riesgo a contrapartes.",
  "version": "vigente",
  "type_raw": [
   "Metodología regulatoria"
  ],
  "type_raw_counts": {
   "Metodología regulatoria": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.11-13 / Punto 2.6.2"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 25, "n_consultas": 29, "top10": []}

  --- ponderadores_de_riesgo (props) | expuesto en outputs de CQ-020: NO ---
{
 "id": "ponderadores_de_riesgo",
 "type": "parametro_regulatorio",
 "label": "Ponderadores de riesgo",
 "properties": {
  "description": "Factores utilizados para calcular el capital mínimo requerido por riesgo de crédito según la clasificación de exposiciones.",
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
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.14-17 / Puntos 2.6.3 y 2.12"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 47, "n_consultas": 29, "top10": []}

  --- exposicion_a_entidades_financieras_del_grupo_1_scra (props) | expuesto en outputs de CQ-020: NO ---
{
 "id": "exposicion_a_entidades_financieras_del_grupo_1_scra",
 "type": "exposicion_a_entidades_financieras",
 "label": "Exposición a entidades financieras del grupo 1 (SCRA)",
 "properties": {
  "description": "Exposición de entidades financieras del grupo 1 (SCRA) a otras entidades financieras, con ponderadores de riesgo que varían según evaluación del riesgo de crédito de la contraparte (20% a 150%) y plazo de la exposición.",
  "version": "vigente",
  "type_raw": [
   "Exposición a entidades financieras"
  ],
  "type_raw_counts": {
   "Exposición a entidades financieras": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.22-25 / Punto 2.12.4.1"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": null, "n_consultas": 29, "top10": []}

  --- metodo_simple (props) | expuesto en outputs de CQ-020: NO ---
{
 "id": "metodo_simple",
 "type": "metodo_de_calculo",
 "label": "Método simple",
 "properties": {
  "description": "Método en el cual el ponderador de riesgo de la contraparte se sustituye por el ponderador de riesgo del activo mediante el cual se cubre la exposición, conforme a la tabla de ponderadores de la Sección 2.",
  "version": "vigente",
  "type_raw": [
   "Método de cálculo",
   "Técnica de cobertura de riesgo de crédito",
   "Método de cobertura de riesgo de crédito"
  ],
  "type_raw_counts": {
   "Método de cálculo": 1,
   "Técnica de cobertura de riesgo de crédito": 1,
   "Método de cobertura de riesgo de crédito": 1
  },
  "name_variants": [],
  "n_observations": 3
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.96-99 / Punto 5.1.1"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.103-106 / Punto 5.3.1"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.107-111 / Punto 5.3.2.2, inciso i)"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": null, "n_consultas": 29, "top10": []}

==============================================================================
6. run_4/CQ-019 (15 outputs)
==============================================================================

[6a] exposición de los términos guía de los 7 reprobados:

  ['prevision especifica'] exposición en outputs de run_4/CQ-019:
    paso 3 resultados[3] id=prevision_especifica
       …especifica", "type": "ajuste_contable", "label": "prevision especifica", "tokens_matcheados": 1, "resumen_propiedades": …
    paso 4 nodo id=prevision_especifica
       …especifica", "type": "ajuste_contable", "label": "prevision especifica", "properties": {"description": "deduccion contab…
    paso 9 resultados[1] id=prevision_especifica
       …especifica", "type": "ajuste_contable", "label": "prevision especifica", "tokens_matcheados": 2, "resumen_propiedades": …
    paso 9 resultados[4] id=exposicion_en_incumplimiento_con_prevision_especifica_menor_al_20
       …icia", "label": "exposicion en incumplimiento con prevision especifica menor al 20%", "tokens_matcheados": 2, "resumen_p…
    paso 9 resultados[5] id=exposicion_en_incumplimiento_con_prevision_especifica_entre_20_y_50
       …icia", "label": "exposicion en incumplimiento con prevision especifica entre 20% y 50%", "tokens_matcheados": 2, "resume…
    paso 9 resultados[6] id=exposicion_en_incumplimiento_con_prevision_especifica_igual_o_mayor_al_50
       …icia", "label": "exposicion en incumplimiento con prevision especifica igual o mayor al 50%", "tokens_matcheados": 2, "r…
    paso 12 resultados[8] id=prevision_especifica
       …especifica", "type": "ajuste_contable", "label": "prevision especifica", "tokens_matcheados": 1, "resumen_propiedades": …

  ['monto bruto'] exposición en outputs de run_4/CQ-019:
    paso 3 resultados[3] id=prevision_especifica
       … calculo de ksa; el calculo debe efectuarse sobre monto bruto de la exposicion."}…
    paso 4 nodo id=prevision_especifica
       … calculo de ksa; el calculo debe efectuarse sobre monto bruto de la exposicion.", "version": "vigente", "type_r…
    paso 9 resultados[1] id=prevision_especifica
       … calculo de ksa; el calculo debe efectuarse sobre monto bruto de la exposicion."}…
    paso 12 resultados[8] id=prevision_especifica
       … calculo de ksa; el calculo debe efectuarse sobre monto bruto de la exposicion."}…

  ['ksa'] exposición en outputs de run_4/CQ-019:
    paso 3 resultados[3] id=prevision_especifica
       …deduccion contable que no se aplica al calculo de ksa; el calculo debe efectuarse sobre monto bruto de …
    paso 4 nodo id=prevision_especifica
       …deduccion contable que no se aplica al calculo de ksa; el calculo debe efectuarse sobre monto bruto de …
    paso 7 salientes[1] no_se_deduce_en_calculo_de→ksa
       …ion": "no_se_deduce_en_calculo_de", "vecino_id": "ksa", "vecino_label": "ksa", "provenances": [{"source…
    paso 7 salientes[1] no_se_deduce_en_calculo_de→ksa
       …calculo_de", "vecino_id": "ksa", "vecino_label": "ksa", "provenances": [{"source_doc": "to_capitales_mi…
    paso 9 resultados[1] id=prevision_especifica
       …deduccion contable que no se aplica al calculo de ksa; el calculo debe efectuarse sobre monto bruto de …
    paso 12 resultados[8] id=prevision_especifica
       …deduccion contable que no se aplica al calculo de ksa; el calculo debe efectuarse sobre monto bruto de …
    paso 15 nodo id=ksa
       …{"id": "ksa", "type": "variable_de_calculo", "label": "ksa", …
    paso 15 nodo id=ksa
       …: "ksa", "type": "variable_de_calculo", "label": "ksa", "properties": {"description": "exigencia de cap…

  ['previsiones minimas'] exposición en outputs de run_4/CQ-019:
    paso 2 resultados[2] id=prevision_regulatoria_por_riesgo_de_incobrabilidad
       …vision determinada por aplicacion de normas sobre previsiones minimas por riesgo de incobrabilidad, cuya diferencia pos…
    paso 3 resultados[4] id=prevision_regulatoria
       …sumen_propiedades": "prevision segun normas sobre previsiones minimas por riesgo de incobrabilidad, utilizada para comp…
    paso 3 resultados[9] id=diferencia_de_prevision_niif_9
       …f 9 y la prevision regulatoria segun normas sobre previsiones minimas por riesgo de incobrab…"}…
    paso 9 resultados[7] id=prevision_regulatoria
       …sumen_propiedades": "prevision segun normas sobre previsiones minimas por riesgo de incobrabilidad, utilizada para comp…
    paso 10 nodo id=prevision_regulatoria_por_riesgo_de_incobrabilidad
       …vision determinada por aplicacion de normas sobre previsiones minimas por riesgo de incobrabilidad, cuya diferencia pos…
    paso 12 resultados[3] id=prevision_regulatoria_por_riesgo_de_incobrabilidad
       …vision determinada por aplicacion de normas sobre previsiones minimas por riesgo de incobrabilidad, cuya diferencia pos…
    paso 12 resultados[9] id=prevision_regulatoria
       …sumen_propiedades": "prevision segun normas sobre previsiones minimas por riesgo de incobrabilidad, utilizada para comp…

  ['totalidad de las financiaciones'] exposición en outputs de run_4/CQ-019:
    paso 3 resultados[1] id=clasificacion_de_deudores
       …enda a la importancia del deudor, considerando la totalidad de las financiaciones comprendidas, de…"}…
    paso 6 nodo id=clasificacion_de_deudores
       …enda a la importancia del deudor, considerando la totalidad de las financiaciones comprendidas, debiendo documentarse el analisis e…
    paso 9 resultados[2] id=clasificacion_de_deudores
       …enda a la importancia del deudor, considerando la totalidad de las financiaciones comprendidas, de…"}…

  ['cinco categorias|categorias de riesgo'] exposición en outputs de run_4/CQ-019:
    paso 3 resultados[5] id=tarea_de_clasificacion
       … "resumen_propiedades": "proceso de asignacion de categorias de riesgo a deudores, que puede ser encomendada a un area i…
    paso 3 resultados[7] id=categoria_de_clasificacion
       …atcheados": 1, "resumen_propiedades": "una de las cinco categorias en que se clasifica a cada cliente y la totalidad…
    paso 9 resultados[8] id=tarea_de_clasificacion
       … "resumen_propiedades": "proceso de asignacion de categorias de riesgo a deudores, que puede ser encomendada a un area i…
    paso 9 resultados[10] id=categoria_de_clasificacion
       …atcheados": 1, "resumen_propiedades": "una de las cinco categorias en que se clasifica a cada cliente y la totalidad…
    paso 12 resultados[1] id=categoria_de_clasificacion
       …atcheados": 2, "resumen_propiedades": "una de las cinco categorias en que se clasifica a cada cliente y la totalidad…
    paso 12 resultados[10] id=tarea_de_clasificacion
       … "resumen_propiedades": "proceso de asignacion de categorias de riesgo a deudores, que puede ser encomendada a un area i…
    paso 13 nodo id=categoria_de_clasificacion
       …acion", "properties": {"description": "una de las cinco categorias en que se clasifica a cada cliente y la totalidad…

  ['criterios objetivos'] exposición en outputs de run_4/CQ-019:
    AUSENTE en todos los outputs completos

[6b] nodos fuente ÍNTEGROS — con titulizacion/securitizacion/3.1.11/ksa en PROPERTIES vs PROVENANCE (aparte):

  --- categoria_de_clasificacion | titulizacion/securitizacion/3.1.11/ksa: PROPERTIES=False · PROVENANCE=False ---
{
 "id": "categoria_de_clasificacion",
 "type": "nivel_de_riesgo",
 "label": "Categoría de clasificación",
 "properties": {
  "description": "Una de las cinco categorías en que se clasifica a cada cliente y la totalidad de sus financiaciones comprendidas.",
  "version": "vigente",
  "type_raw": [
   "Nivel de riesgo"
  ],
  "type_raw_counts": {
   "Nivel de riesgo": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "p.17-19 / Sección 6, punto 6.5"
  }
 ]
}

  --- clasificacion_de_deudores | titulizacion/securitizacion/3.1.11/ksa: PROPERTIES=False · PROVENANCE=False ---
{
 "id": "clasificacion_de_deudores",
 "type": "tarea_regulatoria",
 "label": "Clasificación de deudores",
 "properties": {
  "description": "Clasificación que debe efectuarse con una periodicidad que atienda a la importancia del deudor, considerando la totalidad de las financiaciones comprendidas, debiendo documentarse el análisis efectuado.",
  "version": "vigente",
  "type_raw": [
   "Proceso regulatorio",
   "Tarea regulatoria"
  ],
  "type_raw_counts": {
   "Proceso regulatorio": 1,
   "Tarea regulatoria": 1
  },
  "name_variants": [],
  "n_observations": 2
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "p.1-8 / Sección 1.1"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "p.9-12 / Punto 3.2"
  }
 ]
}

  --- diferencia_de_prevision_niif_9 | titulizacion/securitizacion/3.1.11/ksa: PROPERTIES=False · PROVENANCE=False ---
{
 "id": "diferencia_de_prevision_niif_9",
 "type": "componente_de_capital_regulatorio",
 "label": "Diferencia de previsión NIIF 9",
 "properties": {
  "description": "Diferencia positiva o negativa entre la previsión contable según NIIF 9 y la previsión regulatoria según normas sobre previsiones mínimas por riesgo de incobrabilidad, tomando la mayor de ambas.",
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
   "location": "p.31-35 / Sección 6.2, código 21300000"
  }
 ]
}

  --- exposicion_en_incumplimiento_con_prevision_especifica_entre_20_y_50 | titulizacion/securitizacion/3.1.11/ksa: PROPERTIES=False · PROVENANCE=False ---
{
 "id": "exposicion_en_incumplimiento_con_prevision_especifica_entre_20_y_50",
 "type": "categoria_de_exposicion_crediticia",
 "label": "Exposición en incumplimiento con previsión específica entre 20% y 50%",
 "properties": {
  "description": "Exposición o tramo en situación de incumplimiento no cubierto por coberturas de riesgo de crédito, con previsiones específicas iguales o mayores al 20% y menores al 50% del saldo pendiente. Se aplica ponderador de riesgo del 100%.",
  "version": "vigente",
  "type_raw": [
   "Categoría de exposición crediticia"
  ],
  "type_raw_counts": {
   "Categoría de exposición crediticia": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.26-28 / Punto 2.12.9.2.ii"
  }
 ]
}

  --- exposicion_en_incumplimiento_con_prevision_especifica_igual_o_mayor_al_50 | titulizacion/securitizacion/3.1.11/ksa: PROPERTIES=False · PROVENANCE=False ---
{
 "id": "exposicion_en_incumplimiento_con_prevision_especifica_igual_o_mayor_al_50",
 "type": "categoria_de_exposicion_crediticia",
 "label": "Exposición en incumplimiento con previsión específica igual o mayor al 50%",
 "properties": {
  "description": "Exposición o tramo en situación de incumplimiento no cubierto por coberturas de riesgo de crédito, con previsiones específicas iguales o mayores al 50% del saldo pendiente. Se aplica ponderador de riesgo del 50%.",
  "version": "vigente",
  "type_raw": [
   "Categoría de exposición crediticia"
  ],
  "type_raw_counts": {
   "Categoría de exposición crediticia": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.26-28 / Punto 2.12.9.2.iii"
  }
 ]
}

  --- exposicion_en_incumplimiento_con_prevision_especifica_menor_al_20 | titulizacion/securitizacion/3.1.11/ksa: PROPERTIES=False · PROVENANCE=False ---
{
 "id": "exposicion_en_incumplimiento_con_prevision_especifica_menor_al_20",
 "type": "categoria_de_exposicion_crediticia",
 "label": "Exposición en incumplimiento con previsión específica menor al 20%",
 "properties": {
  "description": "Exposición o tramo en situación de incumplimiento no cubierto por coberturas de riesgo de crédito, con previsiones específicas menores al 20% del saldo pendiente. Se aplica ponderador de riesgo del 150%.",
  "version": "vigente",
  "type_raw": [
   "Categoría de exposición crediticia"
  ],
  "type_raw_counts": {
   "Categoría de exposición crediticia": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.26-28 / Punto 2.12.9.2.i"
  }
 ]
}

  --- ksa | titulizacion/securitizacion/3.1.11/ksa: PROPERTIES=True · PROVENANCE=True ---
{
 "id": "ksa",
 "type": "variable_de_calculo",
 "label": "KSA",
 "properties": {
  "description": "Exigencia de capital promedio de las exposiciones subyacentes, expresada como ratio entre la suma de exposiciones ponderadas por riesgo y la suma de exposiciones, multiplicado por 8%. Rango: 0% a 100%.",
  "version": "vigente",
  "type_raw": [
   "Variable de cálculo",
   "Variable de cálculo de capital",
   "Parámetro de cálculo"
  ],
  "type_raw_counts": {
   "Variable de cálculo": 1,
   "Variable de cálculo de capital": 1,
   "Parámetro de cálculo": 1
  },
  "name_variants": [],
  "n_observations": 3
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.39-41 / Punto 3.1.11.1.i"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.42-45 / Punto 3.1.11.2, inciso i)"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.46-48 / Punto 3.1.13.2, apartado a)"
  }
 ]
}

  --- prevision_especifica | titulizacion/securitizacion/3.1.11/ksa: PROPERTIES=True · PROVENANCE=True ---
{
 "id": "prevision_especifica",
 "type": "ajuste_contable",
 "label": "Previsión específica",
 "properties": {
  "description": "Deducción contable que no se aplica al cálculo de KSA; el cálculo debe efectuarse sobre monto bruto de la exposición.",
  "version": "vigente",
  "type_raw": [
   "Ajuste contable"
  ],
  "type_raw_counts": {
   "Ajuste contable": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.42-45 / Punto 3.1.11.2, inciso i)"
  }
 ]
}

  --- prevision_regulatoria | titulizacion/securitizacion/3.1.11/ksa: PROPERTIES=False · PROVENANCE=False ---
{
 "id": "prevision_regulatoria",
 "type": "ajuste_de_capital",
 "label": "Previsión regulatoria",
 "properties": {
  "description": "Previsión según normas sobre Previsiones mínimas por riesgo de incobrabilidad, utilizada para comparación con previsión contable.",
  "version": "vigente",
  "type_raw": [
   "Ajuste de capital",
   "Parámetro regulatorio"
  ],
  "type_raw_counts": {
   "Parámetro regulatorio": 1,
   "Ajuste de capital": 1
  },
  "name_variants": [],
  "n_observations": 2
 },
 "provenances": [
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "p.28-30 / Punto 6.1.1, Código 21300000"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.175-178 / Punto 11.4"
  }
 ]
}

  --- prevision_regulatoria_por_riesgo_de_incobrabilidad | titulizacion/securitizacion/3.1.11/ksa: PROPERTIES=False · PROVENANCE=False ---
{
 "id": "prevision_regulatoria_por_riesgo_de_incobrabilidad",
 "type": "concepto_deducible_de_capital",
 "label": "Previsión regulatoria por riesgo de incobrabilidad",
 "properties": {
  "description": "Previsión determinada por aplicación de normas sobre previsiones mínimas por riesgo de incobrabilidad, cuya diferencia positiva respecto de la previsión contable es deducible del capital ordinario de nivel uno.",
  "version": "vigente",
  "type_raw": [
   "Concepto deducible de capital"
  ],
  "type_raw_counts": {
   "Concepto deducible de capital": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.161-163 / Punto 8.4.1.1"
  }
 ]
}

  --- tarea_de_clasificacion | titulizacion/securitizacion/3.1.11/ksa: PROPERTIES=False · PROVENANCE=False ---
{
 "id": "tarea_de_clasificacion",
 "type": "funcion_regulatoria",
 "label": "Tarea de clasificación",
 "properties": {
  "description": "Proceso de asignación de categorías de riesgo a deudores, que puede ser encomendada a un área independiente, al sector de créditos con revisión independiente, o a profesionales externos.",
  "version": "vigente",
  "type_raw": [
   "Función regulatoria"
  ],
  "type_raw_counts": {
   "Función regulatoria": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "p.13-16 / Punto 3.5"
  }
 ]
}

[6c] kg run_4: portador del 2.3.1 correcto:
  [barrido kg run_4: 'sin deducir|no se deduce'] en id/label/properties: 7

  --- prestamo (props) | expuesto en outputs de CQ-019: NO ---
{
 "id": "prestamo",
 "type": "tipo_de_financiacion",
 "label": "Préstamo",
 "properties": {
  "description": "Operación que incluye capitales, diferencias de cotización e intereses devengados a cobrar, sin deducir previsiones por riesgos de incobrabilidad.",
  "version": "vigente",
  "type_raw": [
   "Tipo de financiación"
  ],
  "type_raw_counts": {
   "Tipo de financiación": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "p.1-8 / Sección 2.1.1"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": null, "n_consultas": 37, "top10": []}

  --- credito_por_intermediacion_financiera (props) | expuesto en outputs de CQ-019: NO ---
{
 "id": "credito_por_intermediacion_financiera",
 "type": "tipo_de_financiacion",
 "label": "Crédito por intermediación financiera",
 "properties": {
  "description": "Créditos que incluyen capitales, primas e intereses devengados a cobrar, sin deducir previsiones por riesgos de incobrabilidad y desvalorización.",
  "version": "vigente",
  "type_raw": [
   "Tipo de financiación"
  ],
  "type_raw_counts": {
   "Tipo de financiación": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "p.1-8 / Sección 2.1.2"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 72, "n_consultas": 37, "top10": []}

  --- credito_por_arrendamiento_financiero (props) | expuesto en outputs de CQ-019: NO ---
{
 "id": "credito_por_arrendamiento_financiero",
 "type": "tipo_de_financiacion",
 "label": "Crédito por arrendamiento financiero",
 "properties": {
  "description": "Créditos derivados de operaciones de arrendamiento financiero, sin deducir las correspondientes previsiones.",
  "version": "vigente",
  "type_raw": [
   "Tipo de financiación"
  ],
  "type_raw_counts": {
   "Tipo de financiación": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "p.1-8 / Sección 2.1.3"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 66, "n_consultas": 37, "top10": []}

  --- credito_diverso (props) | expuesto en outputs de CQ-019: NO ---
{
 "id": "credito_diverso",
 "type": "tipo_de_financiacion",
 "label": "Crédito diverso",
 "properties": {
  "description": "Créditos vinculados a la venta de activos inmovilizados, inclusive los tomados en defensa o en pago de créditos, sin deducir previsiones por riesgo de incobrabilidad.",
  "version": "vigente",
  "type_raw": [
   "Tipo de financiación"
  ],
  "type_raw_counts": {
   "Tipo de financiación": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "p.1-8 / Sección 2.1.4"
  }
 ]
}
    D1: {"alcanzable": true, "mejor_rank": 4, "n_consultas": 37, "top10": [{"consulta": "credito prevision", "rank": 4}, {"consulta": "credito prevision incobrabilidad", "rank": 6}]}

  --- deudores_clasificados_en_situacion_normal (props) | expuesto en outputs de CQ-019: NO ---
{
 "id": "deudores_clasificados_en_situacion_normal",
 "type": "clasificacion_de_deudores",
 "label": "Deudores clasificados en situación normal",
 "properties": {
  "description": "Deudores cuya previsión por riesgo de incobrabilidad no se deduce completamente en el cálculo de conceptos comprendidos, conforme a los puntos 6.5.1 y 7.2.1 del TO sobre Clasificación de Deudores.",
  "version": "vigente",
  "type_raw": [
   "Clasificación de deudores"
  ],
  "type_raw_counts": {
   "Clasificación de deudores": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.7-10 / Punto 2.3.1. Cómputo de conceptos"
  }
 ]
}
    D1: {"alcanzable": true, "mejor_rank": 7, "n_consultas": 37, "top10": [{"consulta": "clasificacion deudores", "rank": 7}, {"consulta": "regla clasificacion deudores", "rank": 7}]}

  --- saldo_de_deuda_pendiente (props) | expuesto en outputs de CQ-019: NO ---
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
    D1: {"alcanzable": false, "mejor_rank": 1173, "n_consultas": 37, "top10": []}

  --- descuento_no_reembolsable_en_precio_de_compra (props) | expuesto en outputs de CQ-019: NO ---
{
 "id": "descuento_no_reembolsable_en_precio_de_compra",
 "type": "ajuste_contable",
 "label": "Descuento no reembolsable en precio de compra",
 "properties": {
  "description": "Descuento en la adquisición de exposición al conjunto de activos subyacentes que no se deduce del monto bruto para cálculo de KSA.",
  "version": "vigente",
  "type_raw": [
   "Ajuste contable"
  ],
  "type_raw_counts": {
   "Ajuste contable": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.42-45 / Punto 3.1.11.2, inciso i)"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 79, "n_consultas": 37, "top10": []}
  [barrido kg run_4: 'situacion normal ∧ prevision'] en id/label/properties: 3

  --- previsiones_por_riesgo_de_incobrabilidad (props) | expuesto en outputs de CQ-019: NO ---
{
 "id": "previsiones_por_riesgo_de_incobrabilidad",
 "type": "concepto_regulatorio",
 "label": "Previsiones por riesgo de incobrabilidad",
 "properties": {
  "description": "Previsiones sobre cartera de deudores clasificados en situación normal y financiaciones cubiertas con garantías preferidas A, limitadas al 1,25% de activos ponderados por riesgo de crédito.",
  "version": "vigente",
  "type_raw": [
   "Componente de patrimonio complementario",
   "Componente de Capital Regulatorio",
   "Componente de capital computable",
   "Concepto regulatorio"
  ],
  "type_raw_counts": {
   "Componente de capital computable": 1,
   "Concepto regulatorio": 1,
   "Componente de patrimonio complementario": 1,
   "Componente de Capital Regulatorio": 1
  },
  "name_variants": [],
  "n_observations": 4
 },
 "provenances": [
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "p.28-30 / Punto 6.1.2, Código 26300000"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "p.31-35 / Sección 6.2, código 26300000"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.155-157 / Punto 8.2.3.3"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.164-166 / Puntos 8.4.1.12 y 8.4.1.13"
  }
 ]
}
    D1: {"alcanzable": true, "mejor_rank": 9, "n_consultas": 37, "top10": [{"consulta": "prevision incobrabilidad", "rank": 9}]}

  --- previsiones_por_riesgos_de_incobrabilidad (props) | expuesto en outputs de CQ-019: NO ---
{
 "id": "previsiones_por_riesgos_de_incobrabilidad",
 "type": "ajuste_contable",
 "label": "Previsiones por riesgos de incobrabilidad",
 "properties": {
  "description": "Previsiones que se deducen del cálculo de conceptos comprendidos, incluyendo las contabilizadas en el pasivo, excepto el 100% de la previsión para deudores en situación normal.",
  "version": "vigente",
  "type_raw": [
   "Ajuste contable"
  ],
  "type_raw_counts": {
   "Ajuste contable": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.7-10 / Punto 2.3.1. Cómputo de conceptos"
  }
 ]
}
    D1: {"alcanzable": true, "mejor_rank": 10, "n_consultas": 37, "top10": [{"consulta": "prevision incobrabilidad", "rank": 10}]}

  --- deudores_clasificados_en_situacion_normal (props) | expuesto en outputs de CQ-019: NO ---
{
 "id": "deudores_clasificados_en_situacion_normal",
 "type": "clasificacion_de_deudores",
 "label": "Deudores clasificados en situación normal",
 "properties": {
  "description": "Deudores cuya previsión por riesgo de incobrabilidad no se deduce completamente en el cálculo de conceptos comprendidos, conforme a los puntos 6.5.1 y 7.2.1 del TO sobre Clasificación de Deudores.",
  "version": "vigente",
  "type_raw": [
   "Clasificación de deudores"
  ],
  "type_raw_counts": {
   "Clasificación de deudores": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.7-10 / Punto 2.3.1. Cómputo de conceptos"
  }
 ]
}
    D1: {"alcanzable": true, "mejor_rank": 7, "n_consultas": 37, "top10": [{"consulta": "clasificacion deudores", "rank": 7}, {"consulta": "regla clasificacion deudores", "rank": 7}]}
  [barrido kg run_4: '2.3.1'] en id/label/properties: 0 | SOLO en provenances: 47

  --- usuario_de_servicios_financieros (SOLO provenance) | expuesto en outputs de CQ-019: NO ---
{
 "id": "usuario_de_servicios_financieros",
 "type": "sujeto_regulado",
 "label": "Usuario de servicios financieros",
 "properties": {
  "description": "Personas humanas y jurídicas que utilizan servicios ofrecidos por sujetos obligados en carácter de destinatarios finales, incluyendo deudores de créditos cedidos por entidades financieras.",
  "version": "vigente",
  "type_raw": [
   "Categoría de sujeto regulado",
   "Sujeto regulado",
   "Actor regulado",
   "Sujeto protegido"
  ],
  "type_raw_counts": {
   "Categoría de sujeto regulado": 1,
   "Sujeto regulado": 4,
   "Actor regulado": 1,
   "Sujeto protegido": 1
  },
  "name_variants": [],
  "n_observations": 7
 },
 "provenances": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.1-5 / Punto 1.1.1"
  },
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.9-11 / Punto 2.3.1.1, inciso vii y ss."
  },
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.12-14 / Punto 2.3.2.2 y siguientes"
  },
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.15-17 / Punto 2.3.5 y siguientes"
  },
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.18-20 / Sección 2.3.10, 2.4"
  },
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.25-27 / Punto 3.1.2"
  },
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.28-32 / Punto 3.2.2"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 1516, "n_consultas": 37, "top10": []}

  --- caja_de_ahorros_en_pesos (SOLO provenance) | expuesto en outputs de CQ-019: NO ---
{
 "id": "caja_de_ahorros_en_pesos",
 "type": "producto_financiero",
 "label": "Caja de ahorros en pesos",
 "properties": {
  "description": "Producto de depósito de ahorro en pesos con prestaciones previstas en el punto 1.8. del TO sobre Depósitos de Ahorro, Cuenta Sueldo y Especiales, cuya apertura es gratuita.",
  "version": "vigente",
  "type_raw": [
   "Producto financiero"
  ],
  "type_raw_counts": {
   "Producto financiero": 3
  },
  "name_variants": [
   "Caja de Ahorros en pesos",
   "Caja de ahorros en pesos"
  ],
  "n_observations": 3
 },
 "provenances": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.6-8 / Punto 2.3.1"
  },
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.9-11 / Punto 2.3.1.1, inciso ix"
  },
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.18-20 / Sección 2.3.11"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 1141, "n_consultas": 37, "top10": []}

  --- contrato_financiero (SOLO provenance) | expuesto en outputs de CQ-019: NO ---
{
 "id": "contrato_financiero",
 "type": "documento_contractual",
 "label": "Contrato financiero",
 "properties": {
  "description": "Documento que debe tener clara redacción, tamaño de tipografía mínimo de 1,8 milímetros y ser entregado al usuario en el acto de contratación.",
  "version": "vigente",
  "type_raw": [
   "Documento contractual"
  ],
  "type_raw_counts": {
   "Documento contractual": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.6-8 / Punto 2.3.1.1"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": null, "n_consultas": 37, "top10": []}

  --- tipografia_minima_de_1_8_milimetros (SOLO provenance) | expuesto en outputs de CQ-019: NO ---
{
 "id": "tipografia_minima_de_1_8_milimetros",
 "type": "requisito_de_formato",
 "label": "Tipografía mínima de 1,8 milímetros",
 "properties": {
  "description": "Tamaño mínimo de tipografía requerido en contratos financieros para garantizar legibilidad.",
  "version": "vigente",
  "type_raw": [
   "Requisito de formato"
  ],
  "type_raw_counts": {
   "Requisito de formato": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.6-8 / Punto 2.3.1.1"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 20, "n_consultas": 37, "top10": []}

  --- ejemplar_del_contrato_suscripto_por_el_sujeto_obligado (SOLO provenance) | expuesto en outputs de CQ-019: NO ---
{
 "id": "ejemplar_del_contrato_suscripto_por_el_sujeto_obligado",
 "type": "requisito_contractual",
 "label": "Ejemplar del contrato suscripto por el sujeto obligado",
 "properties": {
  "description": "Ejemplar del contrato que debe ser entregado al usuario debidamente suscripto por el sujeto obligado en el acto de contratación.",
  "version": "vigente",
  "type_raw": [
   "Requisito contractual"
  ],
  "type_raw_counts": {
   "Requisito contractual": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.6-8 / Punto 2.3.1.1"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 2062, "n_consultas": 37, "top10": []}

  --- formularios_de_solicitud_de_productos_o_servicios (SOLO provenance) | expuesto en outputs de CQ-019: NO ---
{
 "id": "formularios_de_solicitud_de_productos_o_servicios",
 "type": "documento_contractual",
 "label": "Formularios de solicitud de productos o servicios",
 "properties": {
  "description": "Formularios que deben ser entregados al usuario cuando la solicitud será sometida a aprobación posterior, intervenidos por el sujeto obligado como constancia de recepción.",
  "version": "vigente",
  "type_raw": [
   "Documento contractual"
  ],
  "type_raw_counts": {
   "Documento contractual": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.6-8 / Punto 2.3.1.1"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 1987, "n_consultas": 37, "top10": []}

  --- notificacion_de_aprobacion_de_solicitud (SOLO provenance) | expuesto en outputs de CQ-019: NO ---
{
 "id": "notificacion_de_aprobacion_de_solicitud",
 "type": "requisito_contractual",
 "label": "Notificación de aprobación de solicitud",
 "properties": {
  "description": "Notificación que debe realizarse al usuario una vez aprobada la solicitud, dentro de diez días hábiles contados a partir de la aprobación o disponibilidad efectiva del producto o servicio.",
  "version": "vigente",
  "type_raw": [
   "Requisito contractual"
  ],
  "type_raw_counts": {
   "Requisito contractual": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.6-8 / Punto 2.3.1.1"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 1757, "n_consultas": 37, "top10": []}

  --- clausulas_comprensibles_y_autosuficientes (SOLO provenance) | expuesto en outputs de CQ-019: NO ---
{
 "id": "clausulas_comprensibles_y_autosuficientes",
 "type": "requisito_contractual",
 "label": "Cláusulas comprensibles y autosuficientes",
 "properties": {
  "description": "Las cláusulas del contrato deben ser comprensibles y autosuficientes, sin remitir a textos o documentos no proporcionados simultáneamente.",
  "version": "vigente",
  "type_raw": [
   "Requisito contractual"
  ],
  "type_raw_counts": {
   "Requisito contractual": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.6-8 / Punto 2.3.1.1"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 1791, "n_consultas": 37, "top10": []}

  --- descripcion_y_especificacion_completa_del_producto_y_o_servicio (SOLO provenance) | expuesto en outputs de CQ-019: NO ---
{
 "id": "descripcion_y_especificacion_completa_del_producto_y_o_servicio",
 "type": "contenido_contractual_obligatorio",
 "label": "Descripción y especificación completa del producto y/o servicio",
 "properties": {
  "description": "Elemento mínimo que debe contener todo contrato financiero.",
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
   "location": "p.6-8 / Punto 2.3.1.1, inciso i)"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 2121, "n_consultas": 37, "top10": []}

  --- razon_social_cuit_y_domicilio_legal_del_sujeto_obligado (SOLO provenance) | expuesto en outputs de CQ-019: NO ---
{
 "id": "razon_social_cuit_y_domicilio_legal_del_sujeto_obligado",
 "type": "contenido_contractual_obligatorio",
 "label": "Razón social, CUIT y domicilio legal del sujeto obligado",
 "properties": {
  "description": "Elemento mínimo que debe contener todo contrato financiero.",
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
   "location": "p.6-8 / Punto 2.3.1.1, inciso ii)"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 2086, "n_consultas": 37, "top10": []}

  --- identificacion_del_usuario_de_servicios_financieros (SOLO provenance) | expuesto en outputs de CQ-019: NO ---
{
 "id": "identificacion_del_usuario_de_servicios_financieros",
 "type": "contenido_contractual_obligatorio",
 "label": "Identificación del usuario de servicios financieros",
 "properties": {
  "description": "Elemento mínimo que debe contener todo contrato financiero, incluyendo nombres, apellidos, tipo y número de documento, CUIT/CUIL/CDI y domicilio para personas humanas, o razón social, CUIT y domicilio legal para personas jurídicas.",
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
   "location": "p.6-8 / Punto 2.3.1.1, inciso iii)"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 2017, "n_consultas": 37, "top10": []}

  --- comisiones_y_cargos (SOLO provenance) | expuesto en outputs de CQ-019: NO ---
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
    D1: {"alcanzable": false, "mejor_rank": 922, "n_consultas": 37, "top10": []}

  --- prestamo_hipotecario_en_pesos_para_compra_de_vivienda (SOLO provenance) | expuesto en outputs de CQ-019: NO ---
{
 "id": "prestamo_hipotecario_en_pesos_para_compra_de_vivienda",
 "type": "producto_financiero",
 "label": "Préstamo hipotecario en pesos para compra de vivienda",
 "properties": {
  "description": "Préstamo hipotecario que permite aplicar fondos al pago de inmuebles en moneda extranjera a través de operación de compraventa de títulos valores con liquidación en moneda extranjera (dólar MEP).",
  "version": "vigente",
  "type_raw": [
   "Producto financiero"
  ],
  "type_raw_counts": {
   "Producto financiero": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.6-8 / Punto 2.3.1.1, inciso iv)"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 642, "n_consultas": 37, "top10": []}

  --- clausula_de_revocacion (SOLO provenance) | expuesto en outputs de CQ-019: NO ---
{
 "id": "clausula_de_revocacion",
 "type": "contenido_contractual_obligatorio",
 "label": "Cláusula de revocación",
 "properties": {
  "description": "Cláusula que debe indicar el derecho del usuario a revocar la aceptación del producto o servicio dentro de diez días hábiles, sin costo ni responsabilidad si no ha hecho uso del producto o servicio.",
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
   "location": "p.6-8 / Punto 2.3.1.1, inciso v)"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 1048, "n_consultas": 37, "top10": []}

  --- plazo_de_revocacion_de_diez_dias_habiles (SOLO provenance) | expuesto en outputs de CQ-019: NO ---
{
 "id": "plazo_de_revocacion_de_diez_dias_habiles",
 "type": "requisito_temporal",
 "label": "Plazo de revocación de diez días hábiles",
 "properties": {
  "description": "Plazo durante el cual el usuario puede revocar la aceptación del producto o servicio, contado a partir de la fecha de recibido el contrato o de la disponibilidad efectiva del producto o servicio.",
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
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.6-8 / Punto 2.3.1.1, inciso v)"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 1779, "n_consultas": 37, "top10": []}

  --- notificacion_de_revocacion (SOLO provenance) | expuesto en outputs de CQ-019: NO ---
{
 "id": "notificacion_de_revocacion",
 "type": "requisito_contractual",
 "label": "Notificación de revocación",
 "properties": {
  "description": "La revocación debe notificarse de manera fehaciente o por el mismo medio en que el servicio o producto fue contratado.",
  "version": "vigente",
  "type_raw": [
   "Requisito contractual"
  ],
  "type_raw_counts": {
   "Requisito contractual": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.6-8 / Punto 2.3.1.1, inciso v)"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 1259, "n_consultas": 37, "top10": []}

  --- derecho_de_precancelacion_total_o_parcial (SOLO provenance) | expuesto en outputs de CQ-019: NO ---
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
    D1: {"alcanzable": false, "mejor_rank": 1795, "n_consultas": 37, "top10": []}

  --- sujeto_obligado (SOLO provenance) | expuesto en outputs de CQ-019: NO ---
{
 "id": "sujeto_obligado",
 "type": "entidad_regulada",
 "label": "Sujeto obligado",
 "properties": {
  "description": "Entidad financiera, empresa no financiera emisora de tarjetas de crédito u otro proveedor no financiero de crédito sujeto a las obligaciones de protección de usuarios establecidas en esta normativa.",
  "version": "vigente",
  "type_raw": [
   "Sujeto regulado",
   "Actor regulado",
   "Entidad regulada",
   "Agente regulado",
   "Categoría de responsable regulatorio"
  ],
  "type_raw_counts": {
   "Sujeto regulado": 1,
   "Actor regulado": 1,
   "Entidad regulada": 3,
   "Agente regulado": 1,
   "Categoría de responsable regulatorio": 1
  },
  "name_variants": [],
  "n_observations": 7
 },
 "provenances": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.9-11 / Punto 2.3.1.1, inciso viii y ss."
  },
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.12-14 / Punto 2.3.2.1 y siguientes"
  },
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.15-17 / Punto 2.3.6"
  },
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.18-20 / Sección 2.3.9.8, 2.3.10, 2.3.12 y siguientes"
  },
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.25-27 / Punto 3.2.1.1"
  },
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.28-32 / Punto 3.2.1.1"
  },
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.33-35 / Párrafo inicial de Sección 5"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": null, "n_consultas": 37, "top10": []}

  --- operacion_por_ventanilla (SOLO provenance) | expuesto en outputs de CQ-019: NO ---
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
    D1: {"alcanzable": false, "mejor_rank": 1161, "n_consultas": 37, "top10": []}

  --- regimen_de_transparencia (SOLO provenance) | expuesto en outputs de CQ-019: NO ---
{
 "id": "regimen_de_transparencia",
 "type": "herramienta_regulatoria",
 "label": "Régimen de Transparencia",
 "properties": {
  "description": "Régimen elaborado por el BCRA sobre la base de información proporcionada por sujetos obligados para que los usuarios comparen costos, características y requisitos de productos y servicios financieros.",
  "version": "vigente",
  "type_raw": [
   "Herramienta regulatoria",
   "Herramienta informativa"
  ],
  "type_raw_counts": {
   "Herramienta regulatoria": 2,
   "Herramienta informativa": 1
  },
  "name_variants": [],
  "n_observations": 3
 },
 "provenances": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.9-11 / Punto 2.3.1.1, inciso viii"
  },
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.12-14 / Punto 2.3.4.iv, leyenda obligatoria"
  },
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.18-20 / Sección 2.3.14"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 1172, "n_consultas": 37, "top10": []}

  --- contrato_multiproducto (SOLO provenance) | expuesto en outputs de CQ-019: NO ---
{
 "id": "contrato_multiproducto",
 "type": "instrumento_contractual",
 "label": "Contrato multiproducto",
 "properties": {
  "description": "Contrato que agrupa múltiples productos o servicios financieros, cuyas secciones deben poder escindirse en contratos individuales autónomos para que el usuario pueda adherir solo a los productos que le interesen.",
  "version": "vigente",
  "type_raw": [
   "Instrumento contractual"
  ],
  "type_raw_counts": {
   "Instrumento contractual": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.9-11 / Punto 2.3.1.2"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": null, "n_consultas": 37, "top10": []}

  --- revocacion_de_producto_o_servicio (SOLO provenance) | expuesto en outputs de CQ-019: NO ---
{
 "id": "revocacion_de_producto_o_servicio",
 "type": "derecho_del_usuario",
 "label": "Revocación de producto o servicio",
 "properties": {
  "description": "Facultad del usuario de revocar o rescindir un producto o servicio integrante de un contrato multiproducto, lo que puede implicar pérdida de beneficios o baja de restantes productos, excepto cajas de ahorros en pesos.",
  "version": "vigente",
  "type_raw": [
   "Derecho del usuario"
  ],
  "type_raw_counts": {
   "Derecho del usuario": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.9-11 / Punto 2.3.1.2"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 1557, "n_consultas": 37, "top10": []}

  --- contratacion_a_distancia (SOLO provenance) | expuesto en outputs de CQ-019: NO ---
{
 "id": "contratacion_a_distancia",
 "type": "modalidad_contractual",
 "label": "Contratación a distancia",
 "properties": {
  "description": "Contratación de productos y servicios financieros realizada por modalidades no presenciales como telefónica, correspondencia, medios electrónicos o promoción a través de terceros.",
  "version": "vigente",
  "type_raw": [
   "Modalidad contractual"
  ],
  "type_raw_counts": {
   "Modalidad contractual": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.9-11 / Punto 2.3.1.3"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": null, "n_consultas": 37, "top10": []}

  --- contrato_presencial (SOLO provenance) | expuesto en outputs de CQ-019: NO ---
{
 "id": "contrato_presencial",
 "type": "modalidad_contractual",
 "label": "Contrato presencial",
 "properties": {
  "description": "Contrato celebrado en forma presencial cuya documentación habitual debe utilizarse también en contratos a distancia.",
  "version": "vigente",
  "type_raw": [
   "Modalidad contractual"
  ],
  "type_raw_counts": {
   "Modalidad contractual": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.9-11 / Punto 2.3.1.3"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": null, "n_consultas": 37, "top10": []}

  --- ejemplar_del_contrato (SOLO provenance) | expuesto en outputs de CQ-019: NO ---
{
 "id": "ejemplar_del_contrato",
 "type": "documento_contractual",
 "label": "Ejemplar del contrato",
 "properties": {
  "description": "Copia del contrato con firma autorizada del sujeto obligado que debe proporcionarse al usuario dentro de diez días hábiles de realizada la contratación o de la disponibilidad efectiva del producto o servicio.",
  "version": "vigente",
  "type_raw": [
   "Documento contractual"
  ],
  "type_raw_counts": {
   "Documento contractual": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.9-11 / Punto 2.3.1.3"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": null, "n_consultas": 37, "top10": []}

  --- contratacion_por_medios_electronicos (SOLO provenance) | expuesto en outputs de CQ-019: NO ---
{
 "id": "contratacion_por_medios_electronicos",
 "type": "modalidad_contractual",
 "label": "Contratación por medios electrónicos",
 "properties": {
  "description": "Contratación realizada a través de medios electrónicos, para la cual los sujetos obligados deben otorgar medios técnicos para detectar errores, proporcionar mecanismo de confirmación expresa y asegurar que los términos sean legibles, descargables y guardables de manera inalterable.",
  "version": "vigente",
  "type_raw": [
   "Modalidad contractual"
  ],
  "type_raw_counts": {
   "Modalidad contractual": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.9-11 / Punto 2.3.1.3"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 1638, "n_consultas": 37, "top10": []}

  --- resumen_informativo_del_contrato (SOLO provenance) | expuesto en outputs de CQ-019: NO ---
{
 "id": "resumen_informativo_del_contrato",
 "type": "documento_informativo",
 "label": "Resumen informativo del contrato",
 "properties": {
  "description": "Documento que debe entregarse al usuario antes de la formalización del contrato, sintetizando en lenguaje llano los términos, alcances, operaciones gratuitas, costos y riesgos asociados a la contratación.",
  "version": "vigente",
  "type_raw": [
   "Documento informativo"
  ],
  "type_raw_counts": {
   "Documento informativo": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.9-11 / Punto 2.3.1.4"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": null, "n_consultas": 37, "top10": []}

  --- operaciones_gratuitas (SOLO provenance) | expuesto en outputs de CQ-019: NO ---
{
 "id": "operaciones_gratuitas",
 "type": "caracteristica_de_producto",
 "label": "Operaciones gratuitas",
 "properties": {
  "description": "Operaciones que pueden realizarse con un producto o servicio sin costo para el usuario, que deben ser especificadas en el resumen informativo del contrato.",
  "version": "vigente",
  "type_raw": [
   "Característica de producto"
  ],
  "type_raw_counts": {
   "Característica de producto": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.9-11 / Punto 2.3.1.4, inciso iii"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": null, "n_consultas": 37, "top10": []}

  --- operacion_de_financiacion (SOLO provenance) | expuesto en outputs de CQ-019: NO ---
{
 "id": "operacion_de_financiacion",
 "type": "operacion_financiera",
 "label": "Operación de financiación",
 "properties": {
  "description": "Operación de crédito cuya información debe incluirse en el resumen informativo del contrato conforme a lo dispuesto en el punto 3.2. del TO sobre Tasas de Interés en las Operaciones de Crédito.",
  "version": "vigente",
  "type_raw": [
   "Operación financiera"
  ],
  "type_raw_counts": {
   "Operación financiera": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.9-11 / Punto 2.3.1.4, inciso v"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 1215, "n_consultas": 37, "top10": []}

  --- prestamo_personal (SOLO provenance) | expuesto en outputs de CQ-019: NO ---
{
 "id": "prestamo_personal",
 "type": "producto_de_credito",
 "label": "Préstamo personal",
 "properties": {
  "description": "Préstamo en cuotas cuya información debe incluir importe del capital, monto total a pagar, cantidad de cuotas, periodicidad, vencimiento y sistema de amortización.",
  "version": "vigente",
  "type_raw": [
   "Producto financiero",
   "Producto de crédito"
  ],
  "type_raw_counts": {
   "Producto de crédito": 1,
   "Producto financiero": 1
  },
  "name_variants": [],
  "n_observations": 2
 },
 "provenances": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.9-11 / Punto 2.3.1.4, inciso vi"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.14-17 / Punto 2.8.3.1"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": null, "n_consultas": 37, "top10": []}

  --- prestamo_prendario (SOLO provenance) | expuesto en outputs de CQ-019: NO ---
{
 "id": "prestamo_prendario",
 "type": "producto_de_credito",
 "label": "Préstamo prendario",
 "properties": {
  "description": "Préstamo garantizado con prenda cuya información debe incluir importe del capital, monto total a pagar, cantidad de cuotas, periodicidad, vencimiento y sistema de amortización.",
  "version": "vigente",
  "type_raw": [
   "Producto financiero",
   "Producto de crédito"
  ],
  "type_raw_counts": {
   "Producto de crédito": 1,
   "Producto financiero": 1
  },
  "name_variants": [],
  "n_observations": 2
 },
 "provenances": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.9-11 / Punto 2.3.1.4, inciso vi"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.14-17 / Punto 2.8.3.1"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": null, "n_consultas": 37, "top10": []}

  --- prestamo_hipotecario (SOLO provenance) | expuesto en outputs de CQ-019: NO ---
{
 "id": "prestamo_hipotecario",
 "type": "producto_financiero",
 "label": "Préstamo hipotecario",
 "properties": {
  "description": "Préstamo garantizado con hipoteca cuya información debe incluir importe del capital, monto total a pagar, cantidad de cuotas, periodicidad, vencimiento y sistema de amortización.",
  "version": "vigente",
  "type_raw": [
   "Producto financiero"
  ],
  "type_raw_counts": {
   "Producto financiero": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.9-11 / Punto 2.3.1.4, inciso vi"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": null, "n_consultas": 37, "top10": []}

  --- tarjeta_de_credito (SOLO provenance) | expuesto en outputs de CQ-019: NO ---
{
 "id": "tarjeta_de_credito",
 "type": "producto_financiero",
 "label": "Tarjeta de crédito",
 "properties": {
  "description": "Producto de crédito cuya información debe incluir límites de compra, compra en cuotas, financiación y adelanto de dinero en efectivo, forma de determinación del pago mínimo y canales para consultar la tasa de interés vigente.",
  "version": "vigente",
  "type_raw": [
   "Producto financiero",
   "Producto crediticio",
   "Instrumento de pago",
   "Producto de crédito"
  ],
  "type_raw_counts": {
   "Producto de crédito": 1,
   "Producto crediticio": 1,
   "Instrumento de pago": 1,
   "Producto financiero": 4
  },
  "name_variants": [],
  "n_observations": 7
 },
 "provenances": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.9-11 / Punto 2.3.1.4, inciso vii"
  },
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.12-14 / Punto 2.3.4.iv, cuadro de comisiones"
  },
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.15-17 / Punto 2.3.6"
  },
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.18-20 / Sección 2.3.14"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "p.9-12 / Punto 3.4.1"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.57-59 / Punto 4.1.3"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.14-17 / Puntos 2.8.2 y 2.8.3.1"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 14, "n_consultas": 37, "top10": []}

  --- cuenta_de_deposito (SOLO provenance) | expuesto en outputs de CQ-019: NO ---
{
 "id": "cuenta_de_deposito",
 "type": "producto_financiero",
 "label": "Cuenta de depósito",
 "properties": {
  "description": "Cuenta de depósito cuya información debe incluir periodicidad de generación del resumen de cuenta, plazo para su envío y mecanismo para reclamar objeciones a movimientos o consumos.",
  "version": "vigente",
  "type_raw": [
   "Producto financiero"
  ],
  "type_raw_counts": {
   "Producto financiero": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.9-11 / Punto 2.3.1.4, inciso viii"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 895, "n_consultas": 37, "top10": []}

  --- resumen_de_cuenta (SOLO provenance) | expuesto en outputs de CQ-019: NO ---
{
 "id": "resumen_de_cuenta",
 "type": "documento_informativo",
 "label": "Resumen de cuenta",
 "properties": {
  "description": "Documento que el sujeto obligado debe enviar al usuario con información sobre su cuenta y que debe incluir leyendas informativas específicas.",
  "version": "vigente",
  "type_raw": [
   "Documento informativo"
  ],
  "type_raw_counts": {
   "Documento informativo": 2
  },
  "name_variants": [],
  "n_observations": 2
 },
 "provenances": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.9-11 / Punto 2.3.1.4, inciso viii"
  },
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.18-20 / Sección 2.3.14"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 883, "n_consultas": 37, "top10": []}

  --- mora (SOLO provenance) | expuesto en outputs de CQ-019: NO ---
{
 "id": "mora",
 "type": "situacion_regulatoria",
 "label": "Mora",
 "properties": {
  "description": "Incumplimiento en el pago de obligaciones de financiación cuyas causales, efectos y procedimientos de ejecución deben informarse en el resumen informativo del contrato.",
  "version": "vigente",
  "type_raw": [
   "Situación regulatoria"
  ],
  "type_raw_counts": {
   "Situación regulatoria": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.9-11 / Punto 2.3.1.4, inciso ix"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": null, "n_consultas": 37, "top10": []}

  --- cierre_de_cuenta (SOLO provenance) | expuesto en outputs de CQ-019: NO ---
{
 "id": "cierre_de_cuenta",
 "type": "operacion_contractual",
 "label": "Cierre de cuenta",
 "properties": {
  "description": "Facultad del usuario de cerrar una cuenta, cuyas facultades, procedimientos y canales de tramitación deben informarse en el resumen informativo del contrato.",
  "version": "vigente",
  "type_raw": [
   "Operación contractual"
  ],
  "type_raw_counts": {
   "Operación contractual": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.9-11 / Punto 2.3.1.4, inciso x"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 835, "n_consultas": 37, "top10": []}

  --- rescision_del_contrato (SOLO provenance) | expuesto en outputs de CQ-019: NO ---
{
 "id": "rescision_del_contrato",
 "type": "operacion_contractual",
 "label": "Rescisión del contrato",
 "properties": {
  "description": "Facultad del usuario de rescindir el contrato, cuyas facultades, procedimientos y canales de tramitación deben informarse en el resumen informativo del contrato.",
  "version": "vigente",
  "type_raw": [
   "Operación contractual"
  ],
  "type_raw_counts": {
   "Operación contractual": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.9-11 / Punto 2.3.1.4, inciso x"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": null, "n_consultas": 37, "top10": []}

  --- paquete_multiproducto (SOLO provenance) | expuesto en outputs de CQ-019: NO ---
{
 "id": "paquete_multiproducto",
 "type": "producto_financiero",
 "label": "Paquete multiproducto",
 "properties": {
  "description": "Conjunto de productos y servicios financieros ofrecidos conjuntamente, cuya información debe especificar cuentas y operaciones gratuitas y costos de productos y servicios adicionales.",
  "version": "vigente",
  "type_raw": [
   "Producto financiero"
  ],
  "type_raw_counts": {
   "Producto financiero": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.9-11 / Punto 2.3.1.4, inciso xii"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": null, "n_consultas": 37, "top10": []}

  --- seguro_ofrecido_por_entidad (SOLO provenance) | expuesto en outputs de CQ-019: NO ---
{
 "id": "seguro_ofrecido_por_entidad",
 "type": "producto_financiero",
 "label": "Seguro ofrecido por entidad",
 "properties": {
  "description": "Seguros ofrecidos por las entidades financieras como parte de paquetes multiproducto, cuya información debe incluirse en el resumen informativo del contrato.",
  "version": "vigente",
  "type_raw": [
   "Producto financiero"
  ],
  "type_raw_counts": {
   "Producto financiero": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.9-11 / Punto 2.3.1.4, inciso xii"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 1313, "n_consultas": 37, "top10": []}

  --- canal_de_reclamo (SOLO provenance) | expuesto en outputs de CQ-019: NO ---
{
 "id": "canal_de_reclamo",
 "type": "mecanismo_regulatorio",
 "label": "Canal de reclamo",
 "properties": {
  "description": "Canales habilitados para la realización de reclamos que deben informarse al usuario en el resumen informativo del contrato.",
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
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.9-11 / Punto 2.3.1.4, inciso xiii"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 834, "n_consultas": 37, "top10": []}

  --- garantias_preferidas_a (SOLO provenance) | expuesto en outputs de CQ-019: NO ---
{
 "id": "garantias_preferidas_a",
 "type": "tipo_de_garantia",
 "label": "Garantías preferidas A",
 "properties": {
  "description": "Garantías que respaldan financiaciones respecto de las cuales no corresponde evaluar la capacidad de repago, y cuyos deudores no deben ser objeto de clasificación.",
  "version": "vigente",
  "type_raw": [
   "Tipo de garantía"
  ],
  "type_raw_counts": {
   "Tipo de garantía": 3
  },
  "name_variants": [],
  "n_observations": 3
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "p.13-16 / Punto 4.4, 4.5"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.7-10 / Punto 2.3.1. Cómputo de conceptos"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.155-157 / Punto 8.2.3.3"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": null, "n_consultas": 37, "top10": []}

  --- coeficiente_de_estabilizacion_de_referencia (SOLO provenance) | expuesto en outputs de CQ-019: NO ---
{
 "id": "coeficiente_de_estabilizacion_de_referencia",
 "type": "indice_de_ajuste",
 "label": "Coeficiente de Estabilización de Referencia",
 "properties": {
  "description": "Índice (CER) utilizado para actualizar capitales, intereses, primas y diferencias de cotización en el cálculo de conceptos comprendidos.",
  "version": "vigente",
  "type_raw": [
   "Índice regulatorio",
   "Activo subyacente",
   "Índice de ajuste",
   "Índice de referencia"
  ],
  "type_raw_counts": {
   "Índice de ajuste": 1,
   "Índice de referencia": 1,
   "Índice regulatorio": 1,
   "Activo subyacente": 1
  },
  "name_variants": [],
  "n_observations": 4
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "p.17-19 / Sección 6, punto 6.2"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "p.19-22 / Sección 4.5.1"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.7-10 / Punto 2.3.1. Cómputo de conceptos"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.116-119 / Punto 6.1.1.4"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 1841, "n_consultas": 37, "top10": []}

  --- base_individual_mensual (SOLO provenance) | expuesto en outputs de CQ-019: NO ---
{
 "id": "base_individual_mensual",
 "type": "base_de_calculo",
 "label": "Base individual mensual",
 "properties": {
  "description": "Base sobre la cual se computan los conceptos comprendidos en el cálculo de capital, considerando saldos al último día de cada mes.",
  "version": "vigente",
  "type_raw": [
   "Base de cálculo"
  ],
  "type_raw_counts": {
   "Base de cálculo": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.7-10 / Punto 2.3.1. Cómputo de conceptos"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": null, "n_consultas": 37, "top10": []}

  --- base_consolidada_mensual (SOLO provenance) | expuesto en outputs de CQ-019: NO ---
{
 "id": "base_consolidada_mensual",
 "type": "base_de_calculo",
 "label": "Base consolidada mensual",
 "properties": {
  "description": "Base consolidada sobre la cual se computan los conceptos comprendidos en el cálculo de capital, considerando saldos al último día de cada mes.",
  "version": "vigente",
  "type_raw": [
   "Base de cálculo"
  ],
  "type_raw_counts": {
   "Base de cálculo": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.7-10 / Punto 2.3.1. Cómputo de conceptos"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": null, "n_consultas": 37, "top10": []}

  --- previsiones_por_riesgos_de_incobrabilidad (SOLO provenance) | expuesto en outputs de CQ-019: NO ---
{
 "id": "previsiones_por_riesgos_de_incobrabilidad",
 "type": "ajuste_contable",
 "label": "Previsiones por riesgos de incobrabilidad",
 "properties": {
  "description": "Previsiones que se deducen del cálculo de conceptos comprendidos, incluyendo las contabilizadas en el pasivo, excepto el 100% de la previsión para deudores en situación normal.",
  "version": "vigente",
  "type_raw": [
   "Ajuste contable"
  ],
  "type_raw_counts": {
   "Ajuste contable": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.7-10 / Punto 2.3.1. Cómputo de conceptos"
  }
 ]
}
    D1: {"alcanzable": true, "mejor_rank": 10, "n_consultas": 37, "top10": [{"consulta": "prevision incobrabilidad", "rank": 10}]}

  --- deudores_clasificados_en_situacion_normal (SOLO provenance) | expuesto en outputs de CQ-019: NO ---
{
 "id": "deudores_clasificados_en_situacion_normal",
 "type": "clasificacion_de_deudores",
 "label": "Deudores clasificados en situación normal",
 "properties": {
  "description": "Deudores cuya previsión por riesgo de incobrabilidad no se deduce completamente en el cálculo de conceptos comprendidos, conforme a los puntos 6.5.1 y 7.2.1 del TO sobre Clasificación de Deudores.",
  "version": "vigente",
  "type_raw": [
   "Clasificación de deudores"
  ],
  "type_raw_counts": {
   "Clasificación de deudores": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.7-10 / Punto 2.3.1. Cómputo de conceptos"
  }
 ]
}
    D1: {"alcanzable": true, "mejor_rank": 7, "n_consultas": 37, "top10": [{"consulta": "clasificacion deudores", "rank": 7}, {"consulta": "regla clasificacion deudores", "rank": 7}]}
```

## Tabla resumen — run_4

| # | Verificación | Resultado (hechos; evidencia arriba) |
|---|---|---|
| 3a | CQ-017: barridos kg | "autorizadas a operar": 2 · "deberan intervenir": **0** · "mercado libre de cambios": 1 · "canje": 24 (8 cruzados íntegros) · "arbitraje": 20 (8 íntegros) · provenances "Punto 1.1" de Exterior: listadas aparte |
| 3b | CQ-017: chequeo 0-aristas | **1 nodo operador-de-cambio** (`operador_de_cambio`, íntegro + todos sus edges arriba); **0 aristas** operador↔(entidad-autorizada\|mercado-de-cambios) sobre **3.434 edges** — réplica del hallazgo de run_3 |
| 3c | CQ-017: exposición/D1 de candidatos | `mercado_libre_de_cambios` EXPUESTO (pasos 3, 10, 11, 12); `personas_juridicas_no_autorizadas_a_operar_en_cambios` EXPUESTO (pasos 13, 15, 16); `transferencia_a_cuenta_de_corresponsalia` no expuesto (D1: inalcanzable, rank 1077) |
| 3d | CQ-017: secundarios | "mercado libre de cambios", "no autorizadas" y "conformidad previa" expuestos en outputs (unidades y nodos fuente arriba) |
| 4a | CQ-020: exposición | "sefyc" y "1,19" EXPUESTOS; **"1,03"/"1,08"/"1,13" AUSENTES** de los 15 outputs; "ponderadores"/"activos computables"/"regimen informativo" expuestos (unidades arriba) |
| 4b | CQ-020: kg frecuencia | freq ∧ credito\|crc: **0 nodos** en run_4; frecuencia general del régimen: 13 candidatos (íntegros arriba) |
| 4c | CQ-020: portadores de escala k y APRC | "1,19": 1 nodo; calificacion ∧ token k: listados con exposición/D1; "ponderadores\|aprc": 37 (10 cruzados íntegros) |
| 6a | CQ-019: exposición de los 7 reprobados | 6 de 7 términos guía con exposición (unidades arriba); **"criterios objetivos" AUSENTE** de los 15 outputs |
| 6b | CQ-019: nodos fuente | íntegros, con la marca titulizacion/securitizacion/3.1.11/ksa separada PROPERTIES vs PROVENANCE por nodo (arriba) |
| 6c | CQ-019: portador del 2.3.1 correcto | "sin deducir\|no se deduce": 7 · "situacion normal ∧ prevision": 3 (íntegros, exposición y D1 arriba) · "2.3.1": **0 props / 47 provenances** |

## git status

```
$ git status --porcelain
(sin cambios en zona tracked — ambas partes viven en posthoc_run/dev_set/, gitignored)
```

---

*Parte 2 de 2. Sin adjudicación: los hechos quedan para la adjudicación de casos_validacion.md.*
