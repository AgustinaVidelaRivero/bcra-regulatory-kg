# Expediente de adjudicación — GATE CQN — parte 2 (trayectorias)

Por caso: respuesta final íntegra, inventario de pasos con fidelidad runtime↔re-ejecución
(igualdad de largos: `len(json(re-ejecutado)) == output_chars` de la traza), apéndice de
outputs completos re-ejecutados. Grafo: run_3 congelado vía loader+GraphIndex.


---

# CQN-001

## Respuesta final íntegra (trace.final_json)

```json
{
 "respuesta": "No se encontró en el Knowledge Graph información específica que detalle un monto mensual máximo único para que una persona humana residente pueda comprar sin conformidad previa del BCRA para las tres operaciones mencionadas (formación de activos externos, remisión de ayuda familiar y operatoria con derivados). Se identificaron referencias a estas operaciones en el grafo, pero los detalles de los límites mensuales específicos no fueron accesibles en las búsquedas realizadas. Se encontró que existe un límite mensual de USD 100 para compra en efectivo en ciertos casos, y un límite anual de USD 36.000 para personas humanas en algunos mecanismos, pero no se pudo confirmar un monto mensual máximo único que aplique a las tres operaciones solicitadas sin conformidad previa del BCRA.",
 "citas": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 3.10. Compra de moneda extranjera por parte de otros residentes"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 4.2. Operaciones cursadas a través del Sistema de Monedas Locales (SML)"
  }
 ],
 "respondible": false
}
```

(`respondible`: false · tool_calls_used: 15 · hit_tool_limit: True)

## Inventario de pasos + fidelidad runtime↔re-ejecución

| paso | tool | input | output_chars (runtime) | re-ejecutado | fiel |
|---|---|---|---|---|---|
| 1 | buscar_nodos | `{"consulta": "monto máximo persona humana residente compra activos externos", "limite": 10` | 3222 | 3222 | SÍ |
| 2 | buscar_nodos | `{"consulta": "remisión ayuda familiar monto máximo", "limite": 10}` | 3451 | 3451 | SÍ |
| 3 | buscar_nodos | `{"consulta": "derivados operatoria monto máximo persona residente", "limite": 10}` | 3253 | 3253 | SÍ |
| 4 | buscar_nodos | `{"consulta": "USD 300 persona humana residente mensual", "limite": 10}` | 2494 | 2494 | SÍ |
| 5 | buscar_nodos | `{"consulta": "conformidad previa BCRA compra moneda extranjera", "limite": 10}` | 3501 | 3501 | SÍ |
| 6 | ver_nodo | `{"id": "Operacion_compra_de_moneda_extranjera"}` | 498 | 498 | SÍ |
| 7 | ver_vecinos | `{"id": "Operacion_compra_de_moneda_extranjera", "direccion": "salientes"}` | 554 | 554 | SÍ |
| 8 | buscar_nodos | `{"consulta": "límite mensual persona humana residente sin conformidad", "limite": 10}` | 3547 | 3547 | SÍ |
| 9 | buscar_nodos | `{"consulta": "formación activos externos persona humana límite", "limite": 10}` | 3091 | 3091 | SÍ |
| 10 | ver_nodo | `{"id": "Operacion_formacion_de_activos_externos"}` | 344 | 344 | SÍ |
| 11 | ver_vecinos | `{"id": "Operacion_formacion_de_activos_externos", "direccion": "salientes"}` | 185 | 185 | SÍ |
| 12 | buscar_nodos | `{"consulta": "USD 1000 mensual persona humana", "limite": 10}` | 2763 | 2763 | SÍ |
| 13 | buscar_nodos | `{"consulta": "remisión ayuda familiar USD límite", "limite": 10}` | 3450 | 3450 | SÍ |
| 14 | ver_nodo | `{"id": "Operacion_transferencia_de_ayuda"}` | 404 | 404 | SÍ |
| 15 | ver_vecinos | `{"id": "Operacion_transferencia_de_ayuda", "direccion": "salientes"}` | 181 | 181 | SÍ |

**Fidelidad: 15/15** (igualdad de largos del output completo).

## Apéndice — outputs completos re-ejecutados

### paso 1 — buscar_nodos {"consulta": "monto máximo persona humana residente compra activos externos", "limite": 10}

```json
{
 "consulta": "monto máximo persona humana residente compra activos externos",
 "total_con_match": 242,
 "resultados": [
  {
   "id": "Excepcion_excepcion_apoderado_persona_humana_residente",
   "type": "Excepcion",
   "label": "Excepción: apoderado persona humana residente",
   "tokens_matcheados": 3,
   "resumen_propiedades": "CUIT o CUIL de la persona humana residente que actúe en carácter de apoderado de un no residente. En el registro debe consignarse el nombre y apellido completos…"
  },
  {
   "id": "EntidadFinanciera_persona_humana",
   "type": "EntidadFinanciera",
   "label": "Personas humanas",
   "tokens_matcheados": 2,
   "resumen_propiedades": "categoria: personas humanas"
  },
  {
   "id": "Restriccion_el_monto_acumulado_de_las_repatriaciones_de_capital_del_no_residente_sea_menor_o",
   "type": "Restriccion",
   "label": "Límite repatriación capital",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El monto acumulado de las repatriaciones de capital del no residente sea menor o igual a la suma de los aportes de inversión directa ingresados por mercado de c…"
  },
  {
   "id": "Restriccion_el_monto_maximo_sera_el_menor_entre_el_aumento_total_y_el_equivalente_al_30_del_",
   "type": "Restriccion",
   "label": "Límite de 30% del valor FOB",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El monto máximo será el menor entre el aumento total y el equivalente al 30% del valor FOB de las exportaciones computables para el año t-1"
  },
  {
   "id": "Restriccion_el_agente_local_no_ha_utilizado_este_mecanismo_por_un_monto_superior_al_equivale",
   "type": "Restriccion",
   "label": "Límite máximo de uso mensual",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El agente local no ha utilizado este mecanismo por un monto superior al equivalente de USD 2.000.000 (dólares estadounidenses dos millones) en el mes calendario…"
  },
  {
   "id": "Operacion_formacion_de_activos_externos",
   "type": "Operacion",
   "label": "Formación de activos externos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: formación de activos externos"
  },
  {
   "id": "Restriccion_los_importadores_de_servicios_podran_suscribir_bonos_para_la_reconstruccion_de_u",
   "type": "Restriccion",
   "label": "Monto máximo de suscripción BOPREAL",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Los importadores de servicios podrán suscribir Bonos para la Reconstrucción de una Argentina Libre (BOPREAL) por hasta el monto de la deuda pendiente de pago po…"
  },
  {
   "id": "Restriccion_no_poseia_activos_externos_liquidos_disponibles_que_conjuntamente_tengan_un_valo",
   "type": "Restriccion",
   "label": "Límite de activos externos líquidos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "No poseía activos externos líquidos disponibles que conjuntamente tengan un valor superior al equivalente de USD 100.000 (dólares estadounidenses cien mil)"
  },
  {
   "id": "Obligacion_clasificar_persona_juridica_residente",
   "type": "Obligacion",
   "label": "Clasificar persona jurídica residente",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Una persona jurídica se considerará residente del país donde está constituida"
  },
  {
   "id": "Operacion_tenencia_de_activos_externos_liquidos",
   "type": "Operacion",
   "label": "Tenencia de activos externos líquidos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: tenencia de activos externos liquidos"
  }
 ]
}
```

### paso 2 — buscar_nodos {"consulta": "remisión ayuda familiar monto máximo", "limite": 10}

```json
{
 "consulta": "remisión ayuda familiar monto máximo",
 "total_con_match": 98,
 "resultados": [
  {
   "id": "Restriccion_el_monto_maximo_sera_el_menor_entre_el_aumento_total_y_el_equivalente_al_30_del_",
   "type": "Restriccion",
   "label": "Límite de 30% del valor FOB",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El monto máximo será el menor entre el aumento total y el equivalente al 30% del valor FOB de las exportaciones computables para el año t-1"
  },
  {
   "id": "Restriccion_el_agente_local_no_ha_utilizado_este_mecanismo_por_un_monto_superior_al_equivale",
   "type": "Restriccion",
   "label": "Límite máximo de uso mensual",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El agente local no ha utilizado este mecanismo por un monto superior al equivalente de USD 2.000.000 (dólares estadounidenses dos millones) en el mes calendario…"
  },
  {
   "id": "Operacion_transferencia_de_ayuda",
   "type": "Operacion",
   "label": "Transferencias de ayuda familiar",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Ingreso y remisión de transferencias en concepto de ayuda familiar"
  },
  {
   "id": "Restriccion_los_importadores_de_servicios_podran_suscribir_bonos_para_la_reconstruccion_de_u",
   "type": "Restriccion",
   "label": "Monto máximo de suscripción BOPREAL",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Los importadores de servicios podrán suscribir Bonos para la Reconstrucción de una Argentina Libre (BOPREAL) por hasta el monto de la deuda pendiente de pago po…"
  },
  {
   "id": "Restriccion_monto_maximo_de_suscripcion_de_bopreal",
   "type": "Restriccion",
   "label": "Monto máximo de suscripción de BOPREAL",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Los importadores de bienes podrán suscribir Bonos BOPREAL por hasta el monto de la deuda pendiente de pago por sus importaciones de bienes con registro de ingre…"
  },
  {
   "id": "Restriccion_maximo_mensual_equivalente_al_10_del_monto_total_de_los_anticipos_que_se_encuadr",
   "type": "Restriccion",
   "label": "Límite cobros anticipados máximo mensual",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Máximo mensual equivalente al 10% del monto total de los anticipos que se encuadraron en este mecanismo"
  },
  {
   "id": "Restriccion_el_monto_diario_de_acceso_no_supere_el_20_veinte_por_ciento_del_monto_previsto_e",
   "type": "Restriccion",
   "label": "Límite de acceso diario",
   "tokens_matcheados": 1,
   "resumen_propiedades": "El monto diario de acceso no supere el 20% (veinte por ciento) del monto previsto en el punto anterior."
  },
  {
   "id": "Restriccion_plazo_maximo_liquidacion",
   "type": "Restriccion",
   "label": "Plazo máximo liquidación",
   "tokens_matcheados": 1,
   "resumen_propiedades": "La liquidación en el mercado de cambios deberá realizarse dentro de los 20 (veinte) días hábiles de la fecha de percepción en el exterior o en el país o de su a…"
  },
  {
   "id": "Restriccion_limite_de_monto_a_superar",
   "type": "Restriccion",
   "label": "Límite de monto a superar",
   "tokens_matcheados": 1,
   "resumen_propiedades": "El monto de los pagos y otros movimientos registrados con imputación al despacho no podrá superar el monto facturado según la condición de compra pactada."
  },
  {
   "id": "Excepcion_el_requisito_se_considera_cumplimentado_por_el_monto_de_los_gastos_de_otorgamien",
   "type": "Excepcion",
   "label": "Gastos otorgamiento emisión",
   "tokens_matcheados": 1,
   "resumen_propiedades": "El requisito se considera cumplimentado por el monto de los gastos de otorgamiento y/o emisión que resulten aplicables y otros gastos debitados en el exterior p…"
  }
 ]
}
```

### paso 3 — buscar_nodos {"consulta": "derivados operatoria monto máximo persona residente", "limite": 10}

```json
{
 "consulta": "derivados operatoria monto máximo persona residente",
 "total_con_match": 187,
 "resultados": [
  {
   "id": "Restriccion_el_monto_acumulado_de_las_repatriaciones_de_capital_del_no_residente_sea_menor_o",
   "type": "Restriccion",
   "label": "Límite repatriación capital",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El monto acumulado de las repatriaciones de capital del no residente sea menor o igual a la suma de los aportes de inversión directa ingresados por mercado de c…"
  },
  {
   "id": "Restriccion_el_monto_maximo_sera_el_menor_entre_el_aumento_total_y_el_equivalente_al_30_del_",
   "type": "Restriccion",
   "label": "Límite de 30% del valor FOB",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El monto máximo será el menor entre el aumento total y el equivalente al 30% del valor FOB de las exportaciones computables para el año t-1"
  },
  {
   "id": "Restriccion_el_agente_local_no_ha_utilizado_este_mecanismo_por_un_monto_superior_al_equivale",
   "type": "Restriccion",
   "label": "Límite máximo de uso mensual",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El agente local no ha utilizado este mecanismo por un monto superior al equivalente de USD 2.000.000 (dólares estadounidenses dos millones) en el mes calendario…"
  },
  {
   "id": "Restriccion_los_importadores_de_servicios_podran_suscribir_bonos_para_la_reconstruccion_de_u",
   "type": "Restriccion",
   "label": "Monto máximo de suscripción BOPREAL",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Los importadores de servicios podrán suscribir Bonos para la Reconstrucción de una Argentina Libre (BOPREAL) por hasta el monto de la deuda pendiente de pago po…"
  },
  {
   "id": "Obligacion_clasificar_persona_juridica_residente",
   "type": "Obligacion",
   "label": "Clasificar persona jurídica residente",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Una persona jurídica se considerará residente del país donde está constituida"
  },
  {
   "id": "Restriccion_monto_maximo_de_suscripcion_de_bopreal",
   "type": "Restriccion",
   "label": "Monto máximo de suscripción de BOPREAL",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Los importadores de bienes podrán suscribir Bonos BOPREAL por hasta el monto de la deuda pendiente de pago por sus importaciones de bienes con registro de ingre…"
  },
  {
   "id": "Restriccion_maximo_mensual_equivalente_al_10_del_monto_total_de_los_anticipos_que_se_encuadr",
   "type": "Restriccion",
   "label": "Límite cobros anticipados máximo mensual",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Máximo mensual equivalente al 10% del monto total de los anticipos que se encuadraron en este mecanismo"
  },
  {
   "id": "Excepcion_excepcion_apoderado_persona_humana_residente",
   "type": "Excepcion",
   "label": "Excepción: apoderado persona humana residente",
   "tokens_matcheados": 2,
   "resumen_propiedades": "CUIT o CUIL de la persona humana residente que actúe en carácter de apoderado de un no residente. En el registro debe consignarse el nombre y apellido completos…"
  },
  {
   "id": "EntidadFinanciera_residente",
   "type": "EntidadFinanciera",
   "label": "Residentes",
   "tokens_matcheados": 1,
   "resumen_propiedades": "categoria: residentes"
  },
  {
   "id": "EntidadFinanciera_no_residente",
   "type": "EntidadFinanciera",
   "label": "No residentes",
   "tokens_matcheados": 1,
   "resumen_propiedades": "categoria: clientes no residentes"
  }
 ]
}
```

### paso 4 — buscar_nodos {"consulta": "USD 300 persona humana residente mensual", "limite": 10}

```json
{
 "consulta": "USD 300 persona humana residente mensual",
 "total_con_match": 45,
 "resultados": [
  {
   "id": "Excepcion_excepcion_apoderado_persona_humana_residente",
   "type": "Excepcion",
   "label": "Excepción: apoderado persona humana residente",
   "tokens_matcheados": 3,
   "resumen_propiedades": "CUIT o CUIL de la persona humana residente que actúe en carácter de apoderado de un no residente. En el registro debe consignarse el nombre y apellido completos…"
  },
  {
   "id": "EntidadFinanciera_persona_humana",
   "type": "EntidadFinanciera",
   "label": "Personas humanas",
   "tokens_matcheados": 2,
   "resumen_propiedades": "categoria: personas humanas"
  },
  {
   "id": "Obligacion_clasificar_persona_juridica_residente",
   "type": "Obligacion",
   "label": "Clasificar persona jurídica residente",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Una persona jurídica se considerará residente del país donde está constituida"
  },
  {
   "id": "Operacion_clasificacion_de_residencia",
   "type": "Operacion",
   "label": "Determinación residencia persona humana",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Establecer si una persona humana es residente de un país según su centro de interés económico o actividad principal"
  },
  {
   "id": "Excepcion_el_pago_es_concretado_a_partir_del_10_02_24_por_una_persona_humana_o_una_persona",
   "type": "Excepcion",
   "label": "Pago MiPyMe deudas importaciones anterior 13/12/23",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El pago es concretado a partir del 10/02/24 por una persona humana o una persona jurídica que clasifique como MiPyMe según lo dispuesto en las normas de 'Determ…"
  },
  {
   "id": "EntidadFinanciera_residente",
   "type": "EntidadFinanciera",
   "label": "Residentes",
   "tokens_matcheados": 1,
   "resumen_propiedades": "categoria: residentes"
  },
  {
   "id": "EntidadFinanciera_no_residente",
   "type": "EntidadFinanciera",
   "label": "No residentes",
   "tokens_matcheados": 1,
   "resumen_propiedades": "categoria: clientes no residentes"
  },
  {
   "id": "EntidadFinanciera_persona_juridica",
   "type": "EntidadFinanciera",
   "label": "Personas jurídicas",
   "tokens_matcheados": 1,
   "resumen_propiedades": "categoria: persona jurídica"
  },
  {
   "id": "EntidadFinanciera_cliente_residente",
   "type": "EntidadFinanciera",
   "label": "Clientes residentes",
   "tokens_matcheados": 1,
   "resumen_propiedades": "categoria: cliente residente"
  },
  {
   "id": "EntidadFinanciera_persona_autorizada",
   "type": "EntidadFinanciera",
   "label": "Personas autorizadas",
   "tokens_matcheados": 1,
   "resumen_propiedades": "categoria: personas autorizadas por BCRA"
  }
 ]
}
```

### paso 5 — buscar_nodos {"consulta": "conformidad previa BCRA compra moneda extranjera", "limite": 10}

```json
{
 "consulta": "conformidad previa BCRA compra moneda extranjera",
 "total_con_match": 216,
 "resultados": [
  {
   "id": "Excepcion_si_no_se_cumplen_las_condiciones_de_exportaciones_previas_o_destino_de_fondos_la",
   "type": "Excepcion",
   "label": "Conformidad previa BCRA suscripción moneda extranjera",
   "tokens_matcheados": 5,
   "resumen_propiedades": "Si no se cumplen las condiciones de exportaciones previas o destino de fondos, la emisión debe contar con la conformidad previa del BCRA"
  },
  {
   "id": "Restriccion_el_acceso_al_mercado_de_cambios_para_compra_de_moneda_extranjera_metales_precios",
   "type": "Restriccion",
   "label": "Requerimiento de autorización previa",
   "tokens_matcheados": 4,
   "resumen_propiedades": "El acceso al mercado de cambios para compra de moneda extranjera, metales preciosos amonedados y transferencias al exterior requerirán autorización previa con b…"
  },
  {
   "id": "Restriccion_los_casos_que_no_encuadren_en_lo_expuesto_precedentemente_quedan_sujetos_a_la_co",
   "type": "Restriccion",
   "label": "Conformidad previa BCRA",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Los casos que no encuadren en lo expuesto precedentemente quedan sujetos a la conformidad previa del BCRA, debiendo los pedidos ser canalizados por una entidad …"
  },
  {
   "id": "Excepcion_los_casos_que_no_cumplan_las_condiciones_requeridas_quedaran_sujetos_a_la_confor",
   "type": "Excepcion",
   "label": "Conformidad previa del BCRA",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Los casos que no cumplan las condiciones requeridas quedarán sujetos a la conformidad previa del BCRA"
  },
  {
   "id": "Operacion_compra_de_moneda_extranjera",
   "type": "Operacion",
   "label": "Compra de moneda extranjera",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Compra de moneda extranjera por parte de personas humanas residentes para la formación de activos externos en forma de billetes y/o depósitos"
  },
  {
   "id": "Operacion_compra_de_moneda_extranjera_para_constituir_garantias",
   "type": "Operacion",
   "label": "Compra de moneda extranjera",
   "tokens_matcheados": 3,
   "resumen_propiedades": "tipo: compra de moneda extranjera para constituir garantías"
  },
  {
   "id": "Excepcion_compra_de_billetes_en_moneda_extranjera_de_personas_humanas_no_residentes_en_con",
   "type": "Excepcion",
   "label": "Compra de billetes por turismo",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Compra de billetes en moneda extranjera de personas humanas no residentes en concepto de turismo por hasta USD 100 máximo, sujeto a verificación en sistema onli…"
  },
  {
   "id": "Obligacion_obtener_conformidad_previa_bcra",
   "type": "Obligacion",
   "label": "Obtener conformidad previa BCRA",
   "tokens_matcheados": 3,
   "resumen_propiedades": "El acceso al mercado de cambios requerirá la conformidad previa del BCRA para la formación de activos externos y para la operatoria con derivados"
  },
  {
   "id": "Obligacion_obtener_conformidad_previa_del_bcra_para_acceso_al_mercado_de_cambios_con_anteri",
   "type": "Obligacion",
   "label": "Obtener conformidad previa BCRA",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Obtener conformidad previa del BCRA para acceso al mercado de cambios con anterioridad al vencimiento"
  },
  {
   "id": "Excepcion_no_se_requerira_la_conformidad_previa_del_bcra_cuando_la_entidad_constate_que_el",
   "type": "Excepcion",
   "label": "Excepción por encuadre normativo",
   "tokens_matcheados": 3,
   "resumen_propiedades": "No se requerirá la conformidad previa del BCRA cuando la entidad constate que el pago encuadra en alguna de las situaciones previstas en el punto 10.10.2. o en …"
  }
 ]
}
```

### paso 6 — ver_nodo {"id": "Operacion_compra_de_moneda_extranjera"}

```json
{
 "id": "Operacion_compra_de_moneda_extranjera",
 "type": "Operacion",
 "label": "Compra de moneda extranjera",
 "properties": {
  "tipo": "compra de moneda extranjera",
  "description": "Compra de moneda extranjera por parte de personas humanas residentes para la formación de activos externos en forma de billetes y/o depósitos"
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 3.11. Otras compras de moneda extranjera por parte de residentes con aplicación especí"
  }
 ]
}
```

### paso 7 — ver_vecinos {"id": "Operacion_compra_de_moneda_extranjera", "direccion": "salientes"}

```json
{
 "id": "Operacion_compra_de_moneda_extranjera",
 "label": "Compra de moneda extranjera",
 "n_salientes_total": 1,
 "n_entrantes_total": 9,
 "salientes": [
  {
   "relation": "requiere",
   "vecino_id": "Obligacion_la_entidad_interviniente_haya_verificado_la_documentacion_del_endeudamiento_y_cu",
   "vecino_label": "Verificación de documentación de endeudamiento",
   "provenances": [
    {
     "source_doc": "TO_exterior_cambios_actual.pdf",
     "location": "Punto 3.11. Otras compras de moneda extranjera por parte de residentes con aplicación especí"
    }
   ]
  }
 ],
 "salientes_truncado": false
}
```

### paso 8 — buscar_nodos {"consulta": "límite mensual persona humana residente sin conformidad", "limite": 10}

```json
{
 "consulta": "límite mensual persona humana residente sin conformidad",
 "total_con_match": 298,
 "resultados": [
  {
   "id": "Excepcion_excepcion_apoderado_persona_humana_residente",
   "type": "Excepcion",
   "label": "Excepción: apoderado persona humana residente",
   "tokens_matcheados": 3,
   "resumen_propiedades": "CUIT o CUIL de la persona humana residente que actúe en carácter de apoderado de un no residente. En el registro debe consignarse el nombre y apellido completos…"
  },
  {
   "id": "EntidadFinanciera_persona_humana",
   "type": "EntidadFinanciera",
   "label": "Personas humanas",
   "tokens_matcheados": 2,
   "resumen_propiedades": "categoria: personas humanas"
  },
  {
   "id": "Restriccion_el_monto_acumulado_de_las_repatriaciones_de_capital_del_no_residente_sea_menor_o",
   "type": "Restriccion",
   "label": "Límite repatriación capital",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El monto acumulado de las repatriaciones de capital del no residente sea menor o igual a la suma de los aportes de inversión directa ingresados por mercado de c…"
  },
  {
   "id": "Restriccion_el_agente_local_no_ha_utilizado_este_mecanismo_por_un_monto_superior_al_equivale",
   "type": "Restriccion",
   "label": "Límite máximo de uso mensual",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El agente local no ha utilizado este mecanismo por un monto superior al equivalente de USD 2.000.000 (dólares estadounidenses dos millones) en el mes calendario…"
  },
  {
   "id": "Restriccion_la_suma_de_los_pagos_anticipados_a_la_vista_y_de_deuda_comercial_sin_registro_de",
   "type": "Restriccion",
   "label": "Límite de pagos totales al 80%",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La suma de los pagos anticipados, a la vista y de deuda comercial sin registro de ingreso aduanero cursados en el marco de este punto no supera el 80% (ochenta …"
  },
  {
   "id": "Excepcion_sin_necesidad_de_contar_con_conformidad_previa_del_bcra_si_tal_requisito_estuvie",
   "type": "Excepcion",
   "label": "Exceptuación de conformidad BCRA",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Sin necesidad de contar con conformidad previa del BCRA si tal requisito estuviese vigente, para pagar intereses y capital de financiaciones/aportes de inversió…"
  },
  {
   "id": "Restriccion_operaciones_sin_margen_de_variacion_horizonte_temporal_minimo_sera_el_menor_entr",
   "type": "Restriccion",
   "label": "Límite de horizonte temporal mínimo",
   "tokens_matcheados": 2,
   "resumen_propiedades": "operaciones sin margen de variación: horizonte temporal mínimo será el menor entre un año y el plazo residual del contrato de derivados, con un mínimo de 10 día…"
  },
  {
   "id": "Restriccion_se_requerira_la_conformidad_previa_del_bcra_cuando_el_cliente_registre_por_opera",
   "type": "Restriccion",
   "label": "Prohibición de pago sin conformidad",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Se requerirá la conformidad previa del BCRA cuando el cliente registre por operaciones anteriores al 02/09/19, una condena o un sumario en materia penal cambiar…"
  },
  {
   "id": "Restriccion_limite_mensual_de_compra_en_efectivo",
   "type": "Restriccion",
   "label": "Límite mensual de compra en efectivo",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Si el cliente utiliza efectivo el monto comprado por el cliente no supere el equivalente a USD 100 (dólares estadounidenses cien) en el mes calendario en el con…"
  },
  {
   "id": "Obligacion_clasificar_persona_juridica_residente",
   "type": "Obligacion",
   "label": "Clasificar persona jurídica residente",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Una persona jurídica se considerará residente del país donde está constituida"
  }
 ]
}
```

### paso 9 — buscar_nodos {"consulta": "formación activos externos persona humana límite", "limite": 10}

```json
{
 "consulta": "formación activos externos persona humana límite",
 "total_con_match": 264,
 "resultados": [
  {
   "id": "Operacion_formacion_de_activos_externos",
   "type": "Operacion",
   "label": "Formación de activos externos",
   "tokens_matcheados": 3,
   "resumen_propiedades": "tipo: formación de activos externos"
  },
  {
   "id": "Restriccion_no_poseia_activos_externos_liquidos_disponibles_que_conjuntamente_tengan_un_valo",
   "type": "Restriccion",
   "label": "Límite de activos externos líquidos",
   "tokens_matcheados": 3,
   "resumen_propiedades": "No poseía activos externos líquidos disponibles que conjuntamente tengan un valor superior al equivalente de USD 100.000 (dólares estadounidenses cien mil)"
  },
  {
   "id": "EntidadFinanciera_persona_humana",
   "type": "EntidadFinanciera",
   "label": "Personas humanas",
   "tokens_matcheados": 2,
   "resumen_propiedades": "categoria: personas humanas"
  },
  {
   "id": "Restriccion_limite_de_activos_en_cartera",
   "type": "Restriccion",
   "label": "Límite de activos en cartera",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Aquéllas que en cualquiera de los días de un mes registren activos (suma de las posiciones compradas y vendidas de los activos comprendidos) que en conjunto sup…"
  },
  {
   "id": "Restriccion_en_la_relacion_de_activos_inmovilizados_y_otros_conceptos_seccion_4_del_respecti",
   "type": "Restriccion",
   "label": "Límite de activos inmovilizados",
   "tokens_matcheados": 2,
   "resumen_propiedades": "en la relación de activos inmovilizados y otros conceptos (Sección 4. del respectivo TO), excluidos los computados para la determinación del INC(inversiones sig…"
  },
  {
   "id": "Operacion_tenencia_de_activos_externos_liquidos",
   "type": "Operacion",
   "label": "Tenencia de activos externos líquidos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: tenencia de activos externos liquidos"
  },
  {
   "id": "Restriccion_el_exceso_a_los_limites_para_la_afectacion_de_activos_en_garantia_segun_lo_dispu",
   "type": "Restriccion",
   "label": "Límite de afectación activos garantía",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El exceso a los límites para la afectación de activos en garantía, según lo dispuesto en la Sección 3 de las normas sobre Afectación de activos en garantía"
  },
  {
   "id": "Operacion_clasificacion_de_residencia",
   "type": "Operacion",
   "label": "Determinación residencia persona humana",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Establecer si una persona humana es residente de un país según su centro de interés económico o actividad principal"
  },
  {
   "id": "Operacion_presentacion_informativa_de_activos_y_pasivos_externos",
   "type": "Operacion",
   "label": "Relevamiento de activos y pasivos externos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: presentación informativa de activos y pasivos externos"
  },
  {
   "id": "Excepcion_excepcion_apoderado_persona_humana_residente",
   "type": "Excepcion",
   "label": "Excepción: apoderado persona humana residente",
   "tokens_matcheados": 2,
   "resumen_propiedades": "CUIT o CUIL de la persona humana residente que actúe en carácter de apoderado de un no residente. En el registro debe consignarse el nombre y apellido completos…"
  }
 ]
}
```

### paso 10 — ver_nodo {"id": "Operacion_formacion_de_activos_externos"}

```json
{
 "id": "Operacion_formacion_de_activos_externos",
 "type": "Operacion",
 "label": "Formación de activos externos",
 "properties": {
  "tipo": "formación de activos externos"
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 3.10. Compra de moneda extranjera por parte de otros residentes –excluidas las entidad"
  }
 ]
}
```

### paso 11 — ver_vecinos {"id": "Operacion_formacion_de_activos_externos", "direccion": "salientes"}

```json
{
 "id": "Operacion_formacion_de_activos_externos",
 "label": "Formación de activos externos",
 "n_salientes_total": 0,
 "n_entrantes_total": 2,
 "salientes": [],
 "salientes_truncado": false
}
```

### paso 12 — buscar_nodos {"consulta": "USD 1000 mensual persona humana", "limite": 10}

```json
{
 "consulta": "USD 1000 mensual persona humana",
 "total_con_match": 32,
 "resultados": [
  {
   "id": "EntidadFinanciera_persona_humana",
   "type": "EntidadFinanciera",
   "label": "Personas humanas",
   "tokens_matcheados": 2,
   "resumen_propiedades": "categoria: personas humanas"
  },
  {
   "id": "Operacion_clasificacion_de_residencia",
   "type": "Operacion",
   "label": "Determinación residencia persona humana",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Establecer si una persona humana es residente de un país según su centro de interés económico o actividad principal"
  },
  {
   "id": "Excepcion_excepcion_apoderado_persona_humana_residente",
   "type": "Excepcion",
   "label": "Excepción: apoderado persona humana residente",
   "tokens_matcheados": 2,
   "resumen_propiedades": "CUIT o CUIL de la persona humana residente que actúe en carácter de apoderado de un no residente. En el registro debe consignarse el nombre y apellido completos…"
  },
  {
   "id": "Excepcion_el_pago_es_concretado_a_partir_del_10_02_24_por_una_persona_humana_o_una_persona",
   "type": "Excepcion",
   "label": "Pago MiPyMe deudas importaciones anterior 13/12/23",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El pago es concretado a partir del 10/02/24 por una persona humana o una persona jurídica que clasifique como MiPyMe según lo dispuesto en las normas de 'Determ…"
  },
  {
   "id": "EntidadFinanciera_persona_juridica",
   "type": "EntidadFinanciera",
   "label": "Personas jurídicas",
   "tokens_matcheados": 1,
   "resumen_propiedades": "categoria: persona jurídica"
  },
  {
   "id": "EntidadFinanciera_persona_autorizada",
   "type": "EntidadFinanciera",
   "label": "Personas autorizadas",
   "tokens_matcheados": 1,
   "resumen_propiedades": "categoria: personas autorizadas por BCRA"
  },
  {
   "id": "Operacion_calculo_mensual_de_exigencia_operacional",
   "type": "Operacion",
   "label": "Determinación mensual CRO",
   "tokens_matcheados": 1,
   "resumen_propiedades": "tipo: cálculo mensual de exigencia operacional"
  },
  {
   "id": "Restriccion_el_agente_local_no_ha_utilizado_este_mecanismo_por_un_monto_superior_al_equivale",
   "type": "Restriccion",
   "label": "Límite máximo de uso mensual",
   "tokens_matcheados": 1,
   "resumen_propiedades": "El agente local no ha utilizado este mecanismo por un monto superior al equivalente de USD 2.000.000 (dólares estadounidenses dos millones) en el mes calendario…"
  },
  {
   "id": "EntidadFinanciera_persona_juridica_no_autorizada",
   "type": "EntidadFinanciera",
   "label": "Personas jurídicas no autorizadas",
   "tokens_matcheados": 1,
   "resumen_propiedades": "categoria: personas jurídicas no autorizadas en cambios"
  },
  {
   "id": "Operacion_cancelacion_de_giros_en_descubierto_en_usd",
   "type": "Operacion",
   "label": "Cancelación giros descubierto USD",
   "tokens_matcheados": 1,
   "resumen_propiedades": "tipo: cancelación de giros en descubierto en USD"
  }
 ]
}
```

### paso 13 — buscar_nodos {"consulta": "remisión ayuda familiar USD límite", "limite": 10}

```json
{
 "consulta": "remisión ayuda familiar USD límite",
 "total_con_match": 182,
 "resultados": [
  {
   "id": "Operacion_transferencia_de_ayuda",
   "type": "Operacion",
   "label": "Transferencias de ayuda familiar",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Ingreso y remisión de transferencias en concepto de ayuda familiar"
  },
  {
   "id": "Restriccion_el_limite_se_incrementa_a_usd_200_por_operacion_por_los_retiros_de_efectivo_que_",
   "type": "Restriccion",
   "label": "Límite adelanto países no limítrofes",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El límite se incrementa a USD 200 por operación por los retiros de efectivo que se realicen en países no limítrofes"
  },
  {
   "id": "Restriccion_si_el_monto_total_a_imputar_al_permiso_no_supera_el_equivalente_de_usd_25_000_do",
   "type": "Restriccion",
   "label": "Límite para documentación simplificada",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Si el monto total a imputar al permiso no supera el equivalente de USD 25.000 (dólares estadounidenses veinticinco mil), será suficiente que la entidad cuente c…"
  },
  {
   "id": "Restriccion_exportaciones_de_bienes_enviados_al_exterior_con_fines_promocionales_amparadas_p",
   "type": "Restriccion",
   "label": "Límite de USD 5000 en exportación promocional",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Exportaciones de bienes enviados al exterior con fines promocionales amparadas por la Resolución 772/92 de Administración Nacional de Aduanas, hasta un tope de …"
  },
  {
   "id": "Restriccion_limite_anual_usd_36_000_para_personas_humanas",
   "type": "Restriccion",
   "label": "Límite anual USD 36.000 para personas humanas",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El cliente no ha utilizado este mecanismo por un monto superior al equivalente de USD 36.000 (dólares estadounidenses treinta y seis mil) en el año calendario, …"
  },
  {
   "id": "Restriccion_limite_usd_25_000_para_imputacion_sin_divisas",
   "type": "Restriccion",
   "label": "Límite USD 25.000 para imputación sin divisas",
   "tokens_matcheados": 2,
   "resumen_propiedades": "En la medida que el monto a imputar al permiso por este mecanismo supere el equivalente a USD 25.000 (dólares estadounidenses veinticinco mil), la entidad deber…"
  },
  {
   "id": "Restriccion_valor_adeudado_no_supere_equivalente_de_usd_100_000_cuando_se_usa_companias_de_s",
   "type": "Restriccion",
   "label": "Límite monto para gestión sin entidad recupero",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Valor adeudado no supere equivalente de USD 100.000 cuando se usa compañías de seguro o agencias de recupero"
  },
  {
   "id": "Restriccion_el_monto_total_de_sus_deudas_por_importaciones_de_bienes_y_servicios_previas_al_",
   "type": "Restriccion",
   "label": "Límite monto deudas importaciones MiPyMe USD 500.000",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El monto total de sus deudas por importaciones de bienes y servicios previas al 13/12/23 pendiente de pago sea menor o igual al equivalente a USD 500.000 (dólar…"
  },
  {
   "id": "Restriccion_el_importe_de_co_debera_ser_resultante_de_multiplicar_4_5_por_los_apr",
   "type": "Restriccion",
   "label": "Límite mínimo CO",
   "tokens_matcheados": 1,
   "resumen_propiedades": "El importe de CO deberá ser resultante de multiplicar 4,5% por los APR"
  },
  {
   "id": "Restriccion_el_importe_de_pnb_debera_ser_resultante_de_multiplicar_6_por_los_apr",
   "type": "Restriccion",
   "label": "Límite mínimo PNb",
   "tokens_matcheados": 1,
   "resumen_propiedades": "El importe de PNb deberá ser resultante de multiplicar 6% por los APR"
  }
 ]
}
```

### paso 14 — ver_nodo {"id": "Operacion_transferencia_de_ayuda"}

```json
{
 "id": "Operacion_transferencia_de_ayuda",
 "type": "Operacion",
 "label": "Transferencias de ayuda familiar",
 "properties": {
  "tipo": "transferencia de ayuda",
  "description": "Ingreso y remisión de transferencias en concepto de ayuda familiar"
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 4.2. Operaciones cursadas a través del Sistema de Monedas Locales (SML)."
  }
 ]
}
```

### paso 15 — ver_vecinos {"id": "Operacion_transferencia_de_ayuda", "direccion": "salientes"}

```json
{
 "id": "Operacion_transferencia_de_ayuda",
 "label": "Transferencias de ayuda familiar",
 "n_salientes_total": 0,
 "n_entrantes_total": 1,
 "salientes": [],
 "salientes_truncado": false
}
```



---

# CQN-006

## Respuesta final íntegra (trace.final_json)

```json
{
 "respuesta": "Un sujeto obligado debe reintegrar al usuario de servicios financieros los importes que le cobró indebidamente dentro de los diez (10) días hábiles siguientes al momento de la presentación del reclamo ante el sujeto obligado, o dentro de los cinco (5) días hábiles siguientes al momento de constatarse tal circunstancia por el sujeto obligado o por la fiscalización de la SEFYC. Esta obligación aplica a importes cobrados o adeudados de cualquier forma por conceptos como tasas de interés, comisiones y/o cargos sin cumplimiento de lo previsto.",
 "citas": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "Punto 2.3. Recaudos mínimos de la relación de consumo. (parte 4)"
  }
 ],
 "respondible": true
}
```

(`respondible`: true · tool_calls_used: 3 · hit_tool_limit: False)

## Inventario de pasos + fidelidad runtime↔re-ejecución

| paso | tool | input | output_chars (runtime) | re-ejecutado | fiel |
|---|---|---|---|---|---|
| 1 | buscar_nodos | `{"consulta": "reintegrar importes cobrados indebidamente plazo", "limite": 10}` | 3500 | 3500 | SÍ |
| 2 | buscar_nodos | `{"consulta": "sujeto obligado reintegro usuario servicios financieros", "limite": 10}` | 3635 | 3635 | SÍ |
| 3 | ver_nodo | `{"id": "Obligacion_todo_importe_cobrado_o_adeudado_de_cualquier_forma_al_usuario_por_conce` | 901 | 901 | SÍ |

**Fidelidad: 3/3** (igualdad de largos del output completo).

## Apéndice — outputs completos re-ejecutados

### paso 1 — buscar_nodos {"consulta": "reintegrar importes cobrados indebidamente plazo", "limite": 10}

```json
{
 "consulta": "reintegrar importes cobrados indebidamente plazo",
 "total_con_match": 109,
 "resultados": [
  {
   "id": "Obligacion_todo_importe_cobrado_o_adeudado_de_cualquier_forma_al_usuario_por_conceptos_como",
   "type": "Obligacion",
   "label": "Reintegro de importes cobrados indebidamente",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Todo importe cobrado o adeudado de cualquier forma al usuario por conceptos como tasas de interés, comisiones y/o cargos sin cumplimiento de lo previsto, deberá…"
  },
  {
   "id": "Operacion_registro_contable",
   "type": "Operacion",
   "label": "Registro de importes",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Los importes se registrarán en miles de pesos, sin decimales"
  },
  {
   "id": "Restriccion_el_importe_de_esta_rpc_que_sera_admisible_como_pnc_excluye_los_importes_reconoci",
   "type": "Restriccion",
   "label": "Exclusión de RPC en PNc",
   "tokens_matcheados": 1,
   "resumen_propiedades": "El importe de esta RPC que será admisible como PNc excluye los importes reconocidos en el CO conforme a lo establecido en el punto 8.3.5.1. y los importes recon…"
  },
  {
   "id": "Obligacion_ingreso_y_liquidacion_en_mercado_de_cambios_en_30_dias_corridos_para_exportacion",
   "type": "Obligacion",
   "label": "Ingreso en plazo 30 días",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Ingreso y liquidación en mercado de cambios en 30 días corridos para exportaciones de bienes de posiciones arancelarias 1001.19.00, 1001.99.00, 1005.90.10, 1201…"
  },
  {
   "id": "Obligacion_ingreso_y_liquidacion_en_mercado_de_cambios_en_60_dias_corridos_para_operaciones",
   "type": "Obligacion",
   "label": "Ingreso en plazo 60 días",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Ingreso y liquidación en mercado de cambios en 60 días corridos para operaciones con contrapartes vinculadas y exportaciones de capítulos 26 y 71 según especifi…"
  },
  {
   "id": "Restriccion_operaciones_comerciales_con_brasil_no_podran_tener_plazo_de_pago_que_exceda_360_",
   "type": "Restriccion",
   "label": "Límite plazo pago Brasil",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Operaciones comerciales con Brasil no podrán tener plazo de pago que exceda 360 días"
  },
  {
   "id": "Restriccion_plazo_maximo_liquidacion",
   "type": "Restriccion",
   "label": "Plazo máximo liquidación",
   "tokens_matcheados": 1,
   "resumen_propiedades": "La liquidación en el mercado de cambios deberá realizarse dentro de los 20 (veinte) días hábiles de la fecha de percepción en el exterior o en el país o de su a…"
  },
  {
   "id": "Obligacion_en_caso_de_tratarse_una_operacion_del_concepto_s30_debia_ser_concretado_por_el_c",
   "type": "Obligacion",
   "label": "Plazo de pago para fletes",
   "tokens_matcheados": 1,
   "resumen_propiedades": "En caso de tratarse una operación del concepto S30, debía ser concretado por el cliente a partir de la fecha que resultaba de adicionar 15 (quince) días corrido…"
  },
  {
   "id": "Obligacion_ingreso_y_liquidacion_en_mercado_de_cambios_en_180_dias_corridos_para_el_resto_d",
   "type": "Obligacion",
   "label": "Ingreso en plazo 180 días",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Ingreso y liquidación en mercado de cambios en 180 días corridos para el resto de los bienes"
  },
  {
   "id": "Obligacion_ingreso_y_liquidacion_en_mercado_de_cambios_en_365_dias_corridos_para_operacione",
   "type": "Obligacion",
   "label": "Ingreso en plazo 365 días",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Ingreso y liquidación en mercado de cambios en 365 días corridos para operaciones en marco del régimen EXPORTA SIMPLE, independientemente del tipo de bien expor…"
  }
 ]
}
```

### paso 2 — buscar_nodos {"consulta": "sujeto obligado reintegro usuario servicios financieros", "limite": 10}

```json
{
 "consulta": "sujeto obligado reintegro usuario servicios financieros",
 "total_con_match": 177,
 "resultados": [
  {
   "id": "Obligacion_el_sujeto_obligado_debera_ante_la_solicitud_del_usuario_de_servicios_financieros",
   "type": "Obligacion",
   "label": "Extender constancia de consulta o reclamo",
   "tokens_matcheados": 5,
   "resumen_propiedades": "El sujeto obligado deberá, ante la solicitud del usuario de servicios financieros, extender una constancia con la identificación de su consulta o reclamo y el e…"
  },
  {
   "id": "Obligacion_el_usuario_de_servicios_financieros_debe_ser_notificado_de_las_modificaciones_qu",
   "type": "Obligacion",
   "label": "Notificar cambios de condiciones",
   "tokens_matcheados": 3,
   "resumen_propiedades": "El usuario de servicios financieros debe ser notificado de las modificaciones que aplicará el sujeto obligado con una antelación mínima de sesenta (60) días cor…"
  },
  {
   "id": "Operacion_atencion_al_usuario_de_servicios_financieros",
   "type": "Operacion",
   "label": "Atención de consultas y reclamos",
   "tokens_matcheados": 3,
   "resumen_propiedades": "tipo: atención al usuario de servicios financieros"
  },
  {
   "id": "EntidadFinanciera_usuario_de_servicio_financiero",
   "type": "EntidadFinanciera",
   "label": "Usuarios de servicios financieros",
   "tokens_matcheados": 3,
   "resumen_propiedades": "categoria: usuario de servicio financiero"
  },
  {
   "id": "Restriccion_en_los_contratos_celebrados_entre_el_usuario_de_servicios_financieros_y_los_suje",
   "type": "Restriccion",
   "label": "Prohibición de cláusulas abusivas",
   "tokens_matcheados": 3,
   "resumen_propiedades": "En los contratos celebrados entre el usuario de servicios financieros y los sujetos obligados, se tendrán por no escritas las cláusulas que desnaturalicen las o…"
  },
  {
   "id": "Obligacion_en_el_caso_de_que_el_sujeto_obligado_pretenda_incorporar_nuevos_conceptos_en_cal",
   "type": "Obligacion",
   "label": "Obtener consentimiento del usuario",
   "tokens_matcheados": 3,
   "resumen_propiedades": "En el caso de que el sujeto obligado pretenda incorporar nuevos conceptos en calidad de comisiones y/o cargos que no hubiesen sido previstos en el contrato o re…"
  },
  {
   "id": "Obligacion_la_gerencia_principal_de_proteccion_al_usuario_de_servicios_financieros_tramitar",
   "type": "Obligacion",
   "label": "Tramitar denuncias de asociaciones",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La Gerencia Principal de Protección al Usuario de Servicios Financieros tramitará las denuncias que presenten las asociaciones de consumidores y usuarios recono…"
  },
  {
   "id": "Obligacion_a_los_fines_de_la_comparacion_el_sujeto_obligado_debera_informarle_al_usuario_la",
   "type": "Obligacion",
   "label": "Informar cobertura mínima del seguro",
   "tokens_matcheados": 3,
   "resumen_propiedades": "A los fines de la comparación, el sujeto obligado deberá informarle al usuario la cobertura mínima que debe prever el seguro en cuestión"
  },
  {
   "id": "Restriccion_el_cargo_que_el_sujeto_obligado_aplique_al_usuario_no_podra_ser_superior_al_que_",
   "type": "Restriccion",
   "label": "Límite de cargo por seguro accesorio",
   "tokens_matcheados": 3,
   "resumen_propiedades": "El cargo que el sujeto obligado aplique al usuario no podrá ser superior al que la compañía de seguros elegida perciba por operaciones con particulares y sin la…"
  },
  {
   "id": "Obligacion_si_el_tramite_ha_finalizado_el_usuario_de_servicios_financieros_tendra_derecho_a",
   "type": "Obligacion",
   "label": "Proporcionar nota escrita de resolución",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Si el trámite ha finalizado, el usuario de servicios financieros tendrá derecho a solicitar una nota escrita, suscripta por el responsable de atención o por fun…"
  }
 ]
}
```

### paso 3 — ver_nodo {"id": "Obligacion_todo_importe_cobrado_o_adeudado_de_cualquier_forma_al_usuario_por_conceptos_como"}

```json
{
 "id": "Obligacion_todo_importe_cobrado_o_adeudado_de_cualquier_forma_al_usuario_por_conceptos_como",
 "type": "Obligacion",
 "label": "Reintegro de importes cobrados indebidamente",
 "properties": {
  "descripcion": "Todo importe cobrado o adeudado de cualquier forma al usuario por conceptos como tasas de interés, comisiones y/o cargos sin cumplimiento de lo previsto, deberá serle reintegrado dentro de los diez (10) días hábiles siguientes al momento de la presentación del reclamo ante el sujeto obligado, o los cinco (5) días hábiles siguientes al momento de constatarse tal circunstancia por el sujeto obligado o por la fiscalización de la SEFYC",
  "tipo": "otra",
  "plazo": "10 días hábiles o 5 días hábiles según corresponda"
 },
 "provenances": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "Punto 2.3. Recaudos mínimos de la relación de consumo. (parte 4)"
  }
 ]
}
```



---

# CQN-007

## Respuesta final íntegra (trace.final_json)

```json
{
 "respuesta": "No se encontró información en el Knowledge Graph sobre las circunstancias específicas que identifican a una entidad financiera como 'entidad atípica' en relación con el riesgo de tasa de interés en la cartera de inversión. Aunque el grafo contiene regulaciones sobre el cálculo del riesgo de tasa de interés (EVE) y diversas obligaciones de las entidades financieras, no incluye la definición o criterios de identificación de entidades atípicas en este contexto.",
 "citas": [],
 "respondible": false
}
```

(`respondible`: false · tool_calls_used: 13 · hit_tool_limit: False)

## Inventario de pasos + fidelidad runtime↔re-ejecución

| paso | tool | input | output_chars (runtime) | re-ejecutado | fiel |
|---|---|---|---|---|---|
| 1 | buscar_nodos | `{"consulta": "entidad atípica riesgo tasa interés cartera inversión", "limite": 10}` | 3333 | 3333 | SÍ |
| 2 | buscar_nodos | `{"consulta": "entidad atípica", "limite": 10}` | 2051 | 2051 | SÍ |
| 3 | buscar_nodos | `{"consulta": "atípica", "limite": 15}` | 63 | 63 | SÍ |
| 4 | buscar_nodos | `{"consulta": "circunstancia identificación entidad atípica", "limite": 10}` | 2237 | 2237 | SÍ |
| 5 | buscar_nodos | `{"consulta": "riesgo tasa interés cartera inversión características", "limite": 10}` | 3333 | 3333 | SÍ |
| 6 | buscar_nodos | `{"consulta": "entidad financiera riesgo tasa interés EVE", "limite": 10}` | 3391 | 3391 | SÍ |
| 7 | ver_nodo | `{"id": "Operacion_calculo_de_riesgo_de_tasa_de_interes"}` | 643 | 643 | SÍ |
| 8 | ver_vecinos | `{"id": "Operacion_calculo_de_riesgo_de_tasa_de_interes", "direccion": "ambas"}` | 1756 | 1756 | SÍ |
| 9 | buscar_nodos | `{"consulta": "excepción entidad riesgo tasa interés", "limite": 10}` | 3570 | 3570 | SÍ |
| 10 | buscar_nodos | `{"consulta": "entidad pequeña riesgo tasa interés", "limite": 10}` | 3583 | 3583 | SÍ |
| 11 | buscar_nodos | `{"consulta": "EVE excepción entidad atípica", "limite": 10}` | 3952 | 3952 | SÍ |
| 12 | buscar_nodos | `{"consulta": "EVE cartera inversión entidad", "limite": 10}` | 2399 | 2399 | SÍ |
| 13 | buscar_nodos | `{"consulta": "sección 11 riesgo tasa interés", "limite": 10}` | 3478 | 3478 | SÍ |

**Fidelidad: 13/13** (igualdad de largos del output completo).

## Apéndice — outputs completos re-ejecutados

### paso 1 — buscar_nodos {"consulta": "entidad atípica riesgo tasa interés cartera inversión", "limite": 10}

```json
{
 "consulta": "entidad atípica riesgo tasa interés cartera inversión",
 "total_con_match": 486,
 "resultados": [
  {
   "id": "Operacion_calculo_de_riesgo_de_tasa_de_interes",
   "type": "Operacion",
   "label": "Cálculo riesgo tasa interés EVE",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Cálculo del riesgo de tasa de interés en la cartera de inversión - Medida de riesgo EVE estandarizada (Sección 11.) en base individual y consolidado mensual (có…"
  },
  {
   "id": "Obligacion_informar_riesgo_tasa_interes_eve",
   "type": "Obligacion",
   "label": "Informar riesgo tasa interés EVE",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Cálculo del riesgo de tasa de interés en la cartera de inversión - Medida de riesgo EVE estandarizada (Sección 11.) en base individual y consolidado mensual (có…"
  },
  {
   "id": "Obligacion_se_consignara_el_valor_de_la_exigencia_por_riesgo_general_de_tasa_de_interes_par",
   "type": "Obligacion",
   "label": "Consignación de exigencia riesgo general tasa",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Se consignará el valor de la exigencia por riesgo general de tasa de interés para el último día del período (n) determinada conforme a las disposiciones del pun…"
  },
  {
   "id": "Obligacion_se_consignara_el_valor_de_la_exigencia_por_riesgo_especifico_de_tasa_de_interes_",
   "type": "Obligacion",
   "label": "Consignación de exigencia riesgo específico tasa",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Se consignará el valor de la exigencia por riesgo específico de tasa de interés para el último día del período (n) determinada conforme a las disposiciones del …"
  },
  {
   "id": "Operacion_calculo_de_capital_requerido",
   "type": "Operacion",
   "label": "Cálculo exigencia capital por riesgo tasa interés",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La exigencia de capital por el riesgo de tasa de interés se deberá calcular respecto de los títulos de deuda y otros instrumentos imputados a la cartera de nego…"
  },
  {
   "id": "Operacion_calculo_de_exigencia_capital_por_riesgo_general",
   "type": "Operacion",
   "label": "Determinación de exigencia riesgo general tasa interés",
   "tokens_matcheados": 3,
   "resumen_propiedades": "tipo: cálculo de exigencia capital por riesgo general"
  },
  {
   "id": "Operacion_calculo_de_exigencia_capital_por_riesgo_especifico",
   "type": "Operacion",
   "label": "Determinación de exigencia riesgo específico tasa interés",
   "tokens_matcheados": 3,
   "resumen_propiedades": "tipo: cálculo de exigencia capital por riesgo específico"
  },
  {
   "id": "Operacion_registro_de_operaciones",
   "type": "Operacion",
   "label": "Registro en cartera inversión",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Registro de operaciones de activos admitidos como garantía en la cartera de inversión"
  },
  {
   "id": "Restriccion_empresas_con_grado_de_inversion_con_ponderador_de_riesgo_65",
   "type": "Restriccion",
   "label": "Ponderador empresas inversión",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Empresas con grado de inversión con ponderador de riesgo 65%"
  },
  {
   "id": "Obligacion_los_riesgos_de_tasa_de_interes_y_de_moneda_extranjera_deberan_mitigarse_en_forma",
   "type": "Obligacion",
   "label": "Mitigar descalce de tasa y moneda",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Los riesgos de tasa de interés y de moneda extranjera deberán mitigarse en forma adecuada, sin que esto implique que deba obtenerse una cobertura perfecta y com…"
  }
 ]
}
```

### paso 2 — buscar_nodos {"consulta": "entidad atípica", "limite": 10}

```json
{
 "consulta": "entidad atípica",
 "total_con_match": 224,
 "resultados": [
  {
   "id": "EntidadFinanciera_entidad_nominada",
   "type": "EntidadFinanciera",
   "label": "Entidad nominada",
   "tokens_matcheados": 1,
   "resumen_propiedades": "categoria: entidad nominada para seguimiento de permiso"
  },
  {
   "id": "EntidadFinanciera_nueva_entidad",
   "type": "EntidadFinanciera",
   "label": "Nuevas entidades",
   "tokens_matcheados": 1,
   "resumen_propiedades": "categoria: entidades financieras nuevas"
  },
  {
   "id": "EntidadFinanciera_entidad_encargada",
   "type": "EntidadFinanciera",
   "label": "Entidad encargada",
   "tokens_matcheados": 1,
   "resumen_propiedades": "categoria: entidad encargada de administración de permisos de embarque"
  },
  {
   "id": "EntidadFinanciera_entidad_grupo_a",
   "type": "EntidadFinanciera",
   "label": "Entidades Grupo A",
   "tokens_matcheados": 1,
   "resumen_propiedades": "categoria: entidad financiera grupo A"
  },
  {
   "id": "EntidadFinanciera_entidad_grupo_b",
   "type": "EntidadFinanciera",
   "label": "Entidades grupo B",
   "tokens_matcheados": 1,
   "resumen_propiedades": "categoria: entidad financiera grupo B"
  },
  {
   "id": "EntidadFinanciera_entidad_grupo_c",
   "type": "EntidadFinanciera",
   "label": "Entidades grupo C",
   "tokens_matcheados": 1,
   "resumen_propiedades": "categoria: entidad financiera grupo C"
  },
  {
   "id": "EntidadFinanciera_entidad_local",
   "type": "EntidadFinanciera",
   "label": "Entidades locales",
   "tokens_matcheados": 1,
   "resumen_propiedades": "categoria: entidad financiera local"
  },
  {
   "id": "EntidadFinanciera_entidad_cedente",
   "type": "EntidadFinanciera",
   "label": "Entidades cedentes",
   "tokens_matcheados": 1,
   "resumen_propiedades": "categoria: cedente"
  },
  {
   "id": "EntidadFinanciera_entidad_deudora",
   "type": "EntidadFinanciera",
   "label": "Entidades deudoras",
   "tokens_matcheados": 1,
   "resumen_propiedades": "categoria: entidad emisora de títulos de deuda"
  },
  {
   "id": "EntidadFinanciera_entidad_adherida",
   "type": "EntidadFinanciera",
   "label": "Entidades adheridas",
   "tokens_matcheados": 1,
   "resumen_propiedades": "categoria: entidad adherida al sistema de cotizaciones"
  }
 ]
}
```

### paso 3 — buscar_nodos {"consulta": "atípica", "limite": 15}

```json
{
 "consulta": "atípica",
 "total_con_match": 0,
 "resultados": []
}
```

### paso 4 — buscar_nodos {"consulta": "circunstancia identificación entidad atípica", "limite": 10}

```json
{
 "consulta": "circunstancia identificación entidad atípica",
 "total_con_match": 240,
 "resultados": [
  {
   "id": "Obligacion_la_entidad_financiera_debera_informar_el_origen_de_dicha_circunstancia_a_la_sefy",
   "type": "Obligacion",
   "label": "Informar incrementos irregulares a SEFyC",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La entidad financiera deberá informar el origen de dicha circunstancia a la SEFyC debiendo brindar las explicaciones que les sean requeridas"
  },
  {
   "id": "EntidadFinanciera_entidad_nominada",
   "type": "EntidadFinanciera",
   "label": "Entidad nominada",
   "tokens_matcheados": 1,
   "resumen_propiedades": "categoria: entidad nominada para seguimiento de permiso"
  },
  {
   "id": "EntidadFinanciera_nueva_entidad",
   "type": "EntidadFinanciera",
   "label": "Nuevas entidades",
   "tokens_matcheados": 1,
   "resumen_propiedades": "categoria: entidades financieras nuevas"
  },
  {
   "id": "EntidadFinanciera_entidad_encargada",
   "type": "EntidadFinanciera",
   "label": "Entidad encargada",
   "tokens_matcheados": 1,
   "resumen_propiedades": "categoria: entidad encargada de administración de permisos de embarque"
  },
  {
   "id": "EntidadFinanciera_entidad_grupo_a",
   "type": "EntidadFinanciera",
   "label": "Entidades Grupo A",
   "tokens_matcheados": 1,
   "resumen_propiedades": "categoria: entidad financiera grupo A"
  },
  {
   "id": "EntidadFinanciera_entidad_grupo_b",
   "type": "EntidadFinanciera",
   "label": "Entidades grupo B",
   "tokens_matcheados": 1,
   "resumen_propiedades": "categoria: entidad financiera grupo B"
  },
  {
   "id": "EntidadFinanciera_entidad_grupo_c",
   "type": "EntidadFinanciera",
   "label": "Entidades grupo C",
   "tokens_matcheados": 1,
   "resumen_propiedades": "categoria: entidad financiera grupo C"
  },
  {
   "id": "EntidadFinanciera_entidad_local",
   "type": "EntidadFinanciera",
   "label": "Entidades locales",
   "tokens_matcheados": 1,
   "resumen_propiedades": "categoria: entidad financiera local"
  },
  {
   "id": "EntidadFinanciera_entidad_cedente",
   "type": "EntidadFinanciera",
   "label": "Entidades cedentes",
   "tokens_matcheados": 1,
   "resumen_propiedades": "categoria: cedente"
  },
  {
   "id": "EntidadFinanciera_entidad_deudora",
   "type": "EntidadFinanciera",
   "label": "Entidades deudoras",
   "tokens_matcheados": 1,
   "resumen_propiedades": "categoria: entidad emisora de títulos de deuda"
  }
 ]
}
```

### paso 5 — buscar_nodos {"consulta": "riesgo tasa interés cartera inversión características", "limite": 10}

```json
{
 "consulta": "riesgo tasa interés cartera inversión características",
 "total_con_match": 276,
 "resultados": [
  {
   "id": "Operacion_calculo_de_riesgo_de_tasa_de_interes",
   "type": "Operacion",
   "label": "Cálculo riesgo tasa interés EVE",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Cálculo del riesgo de tasa de interés en la cartera de inversión - Medida de riesgo EVE estandarizada (Sección 11.) en base individual y consolidado mensual (có…"
  },
  {
   "id": "Obligacion_informar_riesgo_tasa_interes_eve",
   "type": "Obligacion",
   "label": "Informar riesgo tasa interés EVE",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Cálculo del riesgo de tasa de interés en la cartera de inversión - Medida de riesgo EVE estandarizada (Sección 11.) en base individual y consolidado mensual (có…"
  },
  {
   "id": "Obligacion_se_consignara_el_valor_de_la_exigencia_por_riesgo_general_de_tasa_de_interes_par",
   "type": "Obligacion",
   "label": "Consignación de exigencia riesgo general tasa",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Se consignará el valor de la exigencia por riesgo general de tasa de interés para el último día del período (n) determinada conforme a las disposiciones del pun…"
  },
  {
   "id": "Obligacion_se_consignara_el_valor_de_la_exigencia_por_riesgo_especifico_de_tasa_de_interes_",
   "type": "Obligacion",
   "label": "Consignación de exigencia riesgo específico tasa",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Se consignará el valor de la exigencia por riesgo específico de tasa de interés para el último día del período (n) determinada conforme a las disposiciones del …"
  },
  {
   "id": "Operacion_calculo_de_capital_requerido",
   "type": "Operacion",
   "label": "Cálculo exigencia capital por riesgo tasa interés",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La exigencia de capital por el riesgo de tasa de interés se deberá calcular respecto de los títulos de deuda y otros instrumentos imputados a la cartera de nego…"
  },
  {
   "id": "Operacion_calculo_de_exigencia_capital_por_riesgo_general",
   "type": "Operacion",
   "label": "Determinación de exigencia riesgo general tasa interés",
   "tokens_matcheados": 3,
   "resumen_propiedades": "tipo: cálculo de exigencia capital por riesgo general"
  },
  {
   "id": "Operacion_calculo_de_exigencia_capital_por_riesgo_especifico",
   "type": "Operacion",
   "label": "Determinación de exigencia riesgo específico tasa interés",
   "tokens_matcheados": 3,
   "resumen_propiedades": "tipo: cálculo de exigencia capital por riesgo específico"
  },
  {
   "id": "Operacion_registro_de_operaciones",
   "type": "Operacion",
   "label": "Registro en cartera inversión",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Registro de operaciones de activos admitidos como garantía en la cartera de inversión"
  },
  {
   "id": "Restriccion_empresas_con_grado_de_inversion_con_ponderador_de_riesgo_65",
   "type": "Restriccion",
   "label": "Ponderador empresas inversión",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Empresas con grado de inversión con ponderador de riesgo 65%"
  },
  {
   "id": "Obligacion_los_riesgos_de_tasa_de_interes_y_de_moneda_extranjera_deberan_mitigarse_en_forma",
   "type": "Obligacion",
   "label": "Mitigar descalce de tasa y moneda",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Los riesgos de tasa de interés y de moneda extranjera deberán mitigarse en forma adecuada, sin que esto implique que deba obtenerse una cobertura perfecta y com…"
  }
 ]
}
```

### paso 6 — buscar_nodos {"consulta": "entidad financiera riesgo tasa interés EVE", "limite": 10}

```json
{
 "consulta": "entidad financiera riesgo tasa interés EVE",
 "total_con_match": 427,
 "resultados": [
  {
   "id": "Operacion_calculo_de_riesgo_de_tasa_de_interes",
   "type": "Operacion",
   "label": "Cálculo riesgo tasa interés EVE",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Cálculo del riesgo de tasa de interés en la cartera de inversión - Medida de riesgo EVE estandarizada (Sección 11.) en base individual y consolidado mensual (có…"
  },
  {
   "id": "Obligacion_informar_riesgo_tasa_interes_eve",
   "type": "Obligacion",
   "label": "Informar riesgo tasa interés EVE",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Cálculo del riesgo de tasa de interés en la cartera de inversión - Medida de riesgo EVE estandarizada (Sección 11.) en base individual y consolidado mensual (có…"
  },
  {
   "id": "Obligacion_la_entidad_financiera_que_actue_en_caracter_de_miembro_compensador_de_una_ccp_po",
   "type": "Obligacion",
   "label": "Aplicar ponderador de riesgo del 2%",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La entidad financiera que actúe en carácter de miembro compensador de una CCP por operaciones propias deberá aplicar un ponderador de riesgo del 2% a sus exposi…"
  },
  {
   "id": "Obligacion_se_consignara_el_valor_de_la_exigencia_por_riesgo_general_de_tasa_de_interes_par",
   "type": "Obligacion",
   "label": "Consignación de exigencia riesgo general tasa",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Se consignará el valor de la exigencia por riesgo general de tasa de interés para el último día del período (n) determinada conforme a las disposiciones del pun…"
  },
  {
   "id": "Obligacion_se_consignara_el_valor_de_la_exigencia_por_riesgo_especifico_de_tasa_de_interes_",
   "type": "Obligacion",
   "label": "Consignación de exigencia riesgo específico tasa",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Se consignará el valor de la exigencia por riesgo específico de tasa de interés para el último día del período (n) determinada conforme a las disposiciones del …"
  },
  {
   "id": "Operacion_calculo_de_capital_requerido",
   "type": "Operacion",
   "label": "Cálculo exigencia capital por riesgo tasa interés",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La exigencia de capital por el riesgo de tasa de interés se deberá calcular respecto de los títulos de deuda y otros instrumentos imputados a la cartera de nego…"
  },
  {
   "id": "Operacion_calculo_de_exigencia_capital_por_riesgo_general",
   "type": "Operacion",
   "label": "Determinación de exigencia riesgo general tasa interés",
   "tokens_matcheados": 3,
   "resumen_propiedades": "tipo: cálculo de exigencia capital por riesgo general"
  },
  {
   "id": "Operacion_calculo_de_exigencia_capital_por_riesgo_especifico",
   "type": "Operacion",
   "label": "Determinación de exigencia riesgo específico tasa interés",
   "tokens_matcheados": 3,
   "resumen_propiedades": "tipo: cálculo de exigencia capital por riesgo específico"
  },
  {
   "id": "Obligacion_cuando_la_entidad_financiera_realice_operaciones_con_una_qccp_debera_determinar_",
   "type": "Obligacion",
   "label": "Determinar exposición a QCCP",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Cuando la entidad financiera realice operaciones con una QCCP deberá determinar su exposición aplicando las disposiciones del punto 4.3.3."
  },
  {
   "id": "EntidadFinanciera_entidad_financiera_grupo_2",
   "type": "EntidadFinanciera",
   "label": "Entidades financieras grupo 2",
   "tokens_matcheados": 2,
   "resumen_propiedades": "categoria: entidad financiera grupo 2"
  }
 ]
}
```

### paso 7 — ver_nodo {"id": "Operacion_calculo_de_riesgo_de_tasa_de_interes"}

```json
{
 "id": "Operacion_calculo_de_riesgo_de_tasa_de_interes",
 "type": "Operacion",
 "label": "Cálculo riesgo tasa interés EVE",
 "properties": {
  "tipo": "cálculo de riesgo de tasa de interés",
  "description": "Cálculo del riesgo de tasa de interés en la cartera de inversión - Medida de riesgo EVE estandarizada (Sección 11.) en base individual y consolidado mensual (códigos de consolidación 0 o 1 y 2) y su respectivo total de control (partida 70500000)"
 },
 "provenances": [
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Punto 1.1. La información tendrá frecuencia mensual y se integrará con datos referidos al m"
  }
 ]
}
```

### paso 8 — ver_vecinos {"id": "Operacion_calculo_de_riesgo_de_tasa_de_interes", "direccion": "ambas"}

```json
{
 "id": "Operacion_calculo_de_riesgo_de_tasa_de_interes",
 "label": "Cálculo riesgo tasa interés EVE",
 "n_salientes_total": 1,
 "n_entrantes_total": 4,
 "salientes": [
  {
   "relation": "establecida_en",
   "vecino_id": "TextoOrdenado_to_regimen_informativo_contable_mensual_actual_pdf",
   "vecino_label": "Régimen Informativo Contable Mensual",
   "provenances": [
    {
     "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
     "location": "Punto 8.1. Normas de procedimiento."
    }
   ]
  }
 ],
 "salientes_truncado": false,
 "entrantes": [
  {
   "relation": "regula",
   "vecino_id": "Obligacion_informar_ratio_de_apalancamiento",
   "vecino_label": "Informar ratio de apalancamiento",
   "provenances": [
    {
     "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
     "location": "Punto 1.1. La información tendrá frecuencia mensual y se integrará con datos referidos al m"
    }
   ]
  },
  {
   "relation": "regula",
   "vecino_id": "Obligacion_informar_riesgo_tasa_interes_eve",
   "vecino_label": "Informar riesgo tasa interés EVE",
   "provenances": [
    {
     "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
     "location": "Punto 1.1. La información tendrá frecuencia mensual y se integrará con datos referidos al m"
    }
   ]
  },
  {
   "relation": "limita",
   "vecino_id": "Restriccion_limitacion_eve_sobre_capital_nivel_1",
   "vecino_label": "Limitación EVE sobre capital nivel 1",
   "provenances": [
    {
     "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
     "location": "Punto 8.1. Normas de procedimiento."
    }
   ]
  },
  {
   "relation": "regula",
   "vecino_id": "Obligacion_informar_riesgo_eve_trimestral",
   "vecino_label": "Informar riesgo EVE trimestral",
   "provenances": [
    {
     "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
     "location": "Punto 8.1. Normas de procedimiento."
    }
   ]
  }
 ],
 "entrantes_truncado": false
}
```

### paso 9 — buscar_nodos {"consulta": "excepción entidad riesgo tasa interés", "limite": 10}

```json
{
 "consulta": "excepción entidad riesgo tasa interés",
 "total_con_match": 661,
 "resultados": [
  {
   "id": "Operacion_calculo_de_riesgo_de_tasa_de_interes",
   "type": "Operacion",
   "label": "Cálculo riesgo tasa interés EVE",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Cálculo del riesgo de tasa de interés en la cartera de inversión - Medida de riesgo EVE estandarizada (Sección 11.) en base individual y consolidado mensual (có…"
  },
  {
   "id": "Obligacion_informar_riesgo_tasa_interes_eve",
   "type": "Obligacion",
   "label": "Informar riesgo tasa interés EVE",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Cálculo del riesgo de tasa de interés en la cartera de inversión - Medida de riesgo EVE estandarizada (Sección 11.) en base individual y consolidado mensual (có…"
  },
  {
   "id": "Obligacion_se_consignara_el_valor_de_la_exigencia_por_riesgo_general_de_tasa_de_interes_par",
   "type": "Obligacion",
   "label": "Consignación de exigencia riesgo general tasa",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Se consignará el valor de la exigencia por riesgo general de tasa de interés para el último día del período (n) determinada conforme a las disposiciones del pun…"
  },
  {
   "id": "Obligacion_se_consignara_el_valor_de_la_exigencia_por_riesgo_especifico_de_tasa_de_interes_",
   "type": "Obligacion",
   "label": "Consignación de exigencia riesgo específico tasa",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Se consignará el valor de la exigencia por riesgo específico de tasa de interés para el último día del período (n) determinada conforme a las disposiciones del …"
  },
  {
   "id": "Operacion_calculo_de_capital_requerido",
   "type": "Operacion",
   "label": "Cálculo exigencia capital por riesgo tasa interés",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La exigencia de capital por el riesgo de tasa de interés se deberá calcular respecto de los títulos de deuda y otros instrumentos imputados a la cartera de nego…"
  },
  {
   "id": "Operacion_calculo_de_exigencia_capital_por_riesgo_general",
   "type": "Operacion",
   "label": "Determinación de exigencia riesgo general tasa interés",
   "tokens_matcheados": 3,
   "resumen_propiedades": "tipo: cálculo de exigencia capital por riesgo general"
  },
  {
   "id": "Operacion_calculo_de_exigencia_capital_por_riesgo_especifico",
   "type": "Operacion",
   "label": "Determinación de exigencia riesgo específico tasa interés",
   "tokens_matcheados": 3,
   "resumen_propiedades": "tipo: cálculo de exigencia capital por riesgo específico"
  },
  {
   "id": "Excepcion_el_ponderador_de_riesgo_de_la_parte_de_la_exposicion_cubierta_podra_ser_inferior",
   "type": "Excepcion",
   "label": "Excepción ponderador mínimo 20%",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El ponderador de riesgo de la parte de la exposición cubierta podrá ser inferior al 20% en los siguientes casos: operaciones de pase con participante esencial, …"
  },
  {
   "id": "Excepcion_la_entidad_encargada_del_seguimiento_del_permiso_de_embarque_podra_extender_el_p",
   "type": "Excepcion",
   "label": "Prórroga de plazo de liquidación",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La entidad encargada del seguimiento del permiso de embarque podrá extender el plazo de liquidación cuando el cliente haya utilizado el mecanismo de acumulación…"
  },
  {
   "id": "Excepcion_no_se_requerira_la_conformidad_previa_del_bcra_cuando_la_entidad_constate_que_el",
   "type": "Excepcion",
   "label": "Excepción por encuadre normativo",
   "tokens_matcheados": 2,
   "resumen_propiedades": "No se requerirá la conformidad previa del BCRA cuando la entidad constate que el pago encuadra en alguna de las situaciones previstas en el punto 10.10.2. o en …"
  }
 ]
}
```

### paso 10 — buscar_nodos {"consulta": "entidad pequeña riesgo tasa interés", "limite": 10}

```json
{
 "consulta": "entidad pequeña riesgo tasa interés",
 "total_con_match": 413,
 "resultados": [
  {
   "id": "Operacion_calculo_de_riesgo_de_tasa_de_interes",
   "type": "Operacion",
   "label": "Cálculo riesgo tasa interés EVE",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Cálculo del riesgo de tasa de interés en la cartera de inversión - Medida de riesgo EVE estandarizada (Sección 11.) en base individual y consolidado mensual (có…"
  },
  {
   "id": "Obligacion_informar_riesgo_tasa_interes_eve",
   "type": "Obligacion",
   "label": "Informar riesgo tasa interés EVE",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Cálculo del riesgo de tasa de interés en la cartera de inversión - Medida de riesgo EVE estandarizada (Sección 11.) en base individual y consolidado mensual (có…"
  },
  {
   "id": "Obligacion_se_consignara_el_valor_de_la_exigencia_por_riesgo_general_de_tasa_de_interes_par",
   "type": "Obligacion",
   "label": "Consignación de exigencia riesgo general tasa",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Se consignará el valor de la exigencia por riesgo general de tasa de interés para el último día del período (n) determinada conforme a las disposiciones del pun…"
  },
  {
   "id": "Obligacion_se_consignara_el_valor_de_la_exigencia_por_riesgo_especifico_de_tasa_de_interes_",
   "type": "Obligacion",
   "label": "Consignación de exigencia riesgo específico tasa",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Se consignará el valor de la exigencia por riesgo específico de tasa de interés para el último día del período (n) determinada conforme a las disposiciones del …"
  },
  {
   "id": "Operacion_calculo_de_capital_requerido",
   "type": "Operacion",
   "label": "Cálculo exigencia capital por riesgo tasa interés",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La exigencia de capital por el riesgo de tasa de interés se deberá calcular respecto de los títulos de deuda y otros instrumentos imputados a la cartera de nego…"
  },
  {
   "id": "Operacion_calculo_de_exigencia_capital_por_riesgo_general",
   "type": "Operacion",
   "label": "Determinación de exigencia riesgo general tasa interés",
   "tokens_matcheados": 3,
   "resumen_propiedades": "tipo: cálculo de exigencia capital por riesgo general"
  },
  {
   "id": "Operacion_calculo_de_exigencia_capital_por_riesgo_especifico",
   "type": "Operacion",
   "label": "Determinación de exigencia riesgo específico tasa interés",
   "tokens_matcheados": 3,
   "resumen_propiedades": "tipo: cálculo de exigencia capital por riesgo específico"
  },
  {
   "id": "Obligacion_los_riesgos_de_tasa_de_interes_y_de_moneda_extranjera_deberan_mitigarse_en_forma",
   "type": "Obligacion",
   "label": "Mitigar descalce de tasa y moneda",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Los riesgos de tasa de interés y de moneda extranjera deberán mitigarse en forma adecuada, sin que esto implique que deba obtenerse una cobertura perfecta y com…"
  },
  {
   "id": "Obligacion_la_entidad_financiera_que_actue_en_caracter_de_miembro_compensador_de_una_ccp_po",
   "type": "Obligacion",
   "label": "Aplicar ponderador de riesgo del 2%",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La entidad financiera que actúe en carácter de miembro compensador de una CCP por operaciones propias deberá aplicar un ponderador de riesgo del 2% a sus exposi…"
  },
  {
   "id": "Obligacion_la_entidad_que_posee_la_posicion_de_titulizacion_debera_comprender_en_todo_momen",
   "type": "Obligacion",
   "label": "Comprender características de riesgo",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La entidad que posee la posición de titulización deberá comprender en todo momento las características de su riesgo, independientemente de estar registradas en …"
  }
 ]
}
```

### paso 11 — buscar_nodos {"consulta": "EVE excepción entidad atípica", "limite": 10}

```json
{
 "consulta": "EVE excepción entidad atípica",
 "total_con_match": 481,
 "resultados": [
  {
   "id": "Excepcion_la_entidad_encargada_del_seguimiento_del_permiso_de_embarque_podra_extender_el_p",
   "type": "Excepcion",
   "label": "Prórroga de plazo de liquidación",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La entidad encargada del seguimiento del permiso de embarque podrá extender el plazo de liquidación cuando el cliente haya utilizado el mecanismo de acumulación…"
  },
  {
   "id": "Excepcion_no_se_requerira_la_conformidad_previa_del_bcra_cuando_la_entidad_constate_que_el",
   "type": "Excepcion",
   "label": "Excepción por encuadre normativo",
   "tokens_matcheados": 2,
   "resumen_propiedades": "No se requerirá la conformidad previa del BCRA cuando la entidad constate que el pago encuadra en alguna de las situaciones previstas en el punto 10.10.2. o en …"
  },
  {
   "id": "Excepcion_si_la_entidad_financiera_carece_de_suficiente_capital_para_efectuar_la_deduccion",
   "type": "Excepcion",
   "label": "Remanente trasferido a nivel superior",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Si la entidad financiera carece de suficiente capital para efectuar la deducción de un nivel particular de capital, el remanente se deducirá del nivel inmediato…"
  },
  {
   "id": "Excepcion_el_limite_maximo_establecido_precedentemente_se_reducira_a_11_cuando_la_entidad_",
   "type": "Excepcion",
   "label": "Reducción a 11% por calificación SEFYC",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El límite máximo establecido precedentemente se reducirá a 11% cuando la entidad financiera cuente con calificación 1, 2 o 3 conforme a la valoración otorgada p…"
  },
  {
   "id": "Excepcion_la_constancia_de_aceptacion_por_parte_de_la_nueva_entidad_libera_a_la_entidad_pr",
   "type": "Excepcion",
   "label": "Liberación por aceptación nueva entidad",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La constancia de aceptación por parte de la nueva entidad liberará a la entidad previa de sus obligaciones hacia adelante."
  },
  {
   "id": "Excepcion_en_los_casos_en_que_la_entidad_financiera_cuente_en_todos_los_citados_aspectos_c",
   "type": "Excepcion",
   "label": "Reducción límite con calificación SEFYC 1-2",
   "tokens_matcheados": 2,
   "resumen_propiedades": "En los casos en que la entidad financiera cuente en todos los citados aspectos con calificación 1 o 2, el límite máximo disminuirá a 7% o 5%, según pertenezca a…"
  },
  {
   "id": "Excepcion_los_limites_maximos_se_reduciran_a_11_y_8_respectivamente_cuando_la_entidad_fina",
   "type": "Excepcion",
   "label": "Reducción límite con calificación SEFYC 1-3",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Los límites máximos se reducirán a 11% y 8%, respectivamente, cuando la entidad financiera cuente con calificación 1, 2 o 3 conforme a la valoración otorgada po…"
  },
  {
   "id": "Excepcion_la_entidad_podra_emitir_certificaciones_de_aplicacion_con_imputacion_a_una_opera",
   "type": "Excepcion",
   "label": "Excepción por deuda cedida a acreedor externo",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La entidad podrá emitir certificaciones de aplicación con imputación a una operación bajo su seguimiento si el exportador demuestra fehacientemente que las divi…"
  },
  {
   "id": "Excepcion_cuando_la_entidad_haya_verificado_que_la_destinacion_fue_declarada_erroneamente_",
   "type": "Excepcion",
   "label": "Excepción por declaración errónea de contraparte vinculada",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Cuando la entidad haya verificado que la destinación fue declarada erróneamente ante Aduana como operación con contraparte vinculada, se podrá extender el plazo"
  },
  {
   "id": "Excepcion_cuando_la_entidad_haya_verificado_que_la_destinacion_de_exportacion_corresponde_",
   "type": "Excepcion",
   "label": "Excepción por operación con contraparte vinculada verificada",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Cuando la entidad haya verificado que la destinación de exportación corresponde a operación que cumple condiciones de contraparte vinculada elegible, podrá exte…"
  }
 ]
}
```

### paso 12 — buscar_nodos {"consulta": "EVE cartera inversión entidad", "limite": 10}

```json
{
 "consulta": "EVE cartera inversión entidad",
 "total_con_match": 304,
 "resultados": [
  {
   "id": "Operacion_registro_de_operaciones",
   "type": "Operacion",
   "label": "Registro en cartera inversión",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Registro de operaciones de activos admitidos como garantía en la cartera de inversión"
  },
  {
   "id": "Restriccion_no_se_incluiran_posiciones_en_acciones_en_la_cartera_de_inversion",
   "type": "Restriccion",
   "label": "Exclusión de posiciones en acciones",
   "tokens_matcheados": 2,
   "resumen_propiedades": "No se incluirán posiciones en acciones en la cartera de inversión"
  },
  {
   "id": "Obligacion_cuando_una_entidad_financiera_tenga_una_inversion_en_un_fondo_que_a_su_vez_tiene",
   "type": "Obligacion",
   "label": "Determinación de ponderador para fondos internidados",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Cuando una entidad financiera tenga una inversión en un fondo que a su vez tiene inversión en otro fondo, el ponderador de riesgo se determinará mediante alguno…"
  },
  {
   "id": "EntidadFinanciera_entidad_nominada",
   "type": "EntidadFinanciera",
   "label": "Entidad nominada",
   "tokens_matcheados": 1,
   "resumen_propiedades": "categoria: entidad nominada para seguimiento de permiso"
  },
  {
   "id": "EntidadFinanciera_nueva_entidad",
   "type": "EntidadFinanciera",
   "label": "Nuevas entidades",
   "tokens_matcheados": 1,
   "resumen_propiedades": "categoria: entidades financieras nuevas"
  },
  {
   "id": "EntidadFinanciera_entidad_encargada",
   "type": "EntidadFinanciera",
   "label": "Entidad encargada",
   "tokens_matcheados": 1,
   "resumen_propiedades": "categoria: entidad encargada de administración de permisos de embarque"
  },
  {
   "id": "EntidadFinanciera_entidad_grupo_a",
   "type": "EntidadFinanciera",
   "label": "Entidades Grupo A",
   "tokens_matcheados": 1,
   "resumen_propiedades": "categoria: entidad financiera grupo A"
  },
  {
   "id": "EntidadFinanciera_entidad_grupo_b",
   "type": "EntidadFinanciera",
   "label": "Entidades grupo B",
   "tokens_matcheados": 1,
   "resumen_propiedades": "categoria: entidad financiera grupo B"
  },
  {
   "id": "EntidadFinanciera_entidad_grupo_c",
   "type": "EntidadFinanciera",
   "label": "Entidades grupo C",
   "tokens_matcheados": 1,
   "resumen_propiedades": "categoria: entidad financiera grupo C"
  },
  {
   "id": "EntidadFinanciera_entidad_local",
   "type": "EntidadFinanciera",
   "label": "Entidades locales",
   "tokens_matcheados": 1,
   "resumen_propiedades": "categoria: entidad financiera local"
  }
 ]
}
```

### paso 13 — buscar_nodos {"consulta": "sección 11 riesgo tasa interés", "limite": 10}

```json
{
 "consulta": "sección 11 riesgo tasa interés",
 "total_con_match": 209,
 "resultados": [
  {
   "id": "Operacion_calculo_de_riesgo_de_tasa_de_interes",
   "type": "Operacion",
   "label": "Cálculo riesgo tasa interés EVE",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Cálculo del riesgo de tasa de interés en la cartera de inversión - Medida de riesgo EVE estandarizada (Sección 11.) en base individual y consolidado mensual (có…"
  },
  {
   "id": "Obligacion_informar_riesgo_tasa_interes_eve",
   "type": "Obligacion",
   "label": "Informar riesgo tasa interés EVE",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Cálculo del riesgo de tasa de interés en la cartera de inversión - Medida de riesgo EVE estandarizada (Sección 11.) en base individual y consolidado mensual (có…"
  },
  {
   "id": "Obligacion_se_consignara_el_valor_de_la_exigencia_por_riesgo_general_de_tasa_de_interes_par",
   "type": "Obligacion",
   "label": "Consignación de exigencia riesgo general tasa",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Se consignará el valor de la exigencia por riesgo general de tasa de interés para el último día del período (n) determinada conforme a las disposiciones del pun…"
  },
  {
   "id": "Obligacion_se_consignara_el_valor_de_la_exigencia_por_riesgo_especifico_de_tasa_de_interes_",
   "type": "Obligacion",
   "label": "Consignación de exigencia riesgo específico tasa",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Se consignará el valor de la exigencia por riesgo específico de tasa de interés para el último día del período (n) determinada conforme a las disposiciones del …"
  },
  {
   "id": "Operacion_calculo_de_capital_requerido",
   "type": "Operacion",
   "label": "Cálculo exigencia capital por riesgo tasa interés",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La exigencia de capital por el riesgo de tasa de interés se deberá calcular respecto de los títulos de deuda y otros instrumentos imputados a la cartera de nego…"
  },
  {
   "id": "Operacion_calculo_de_exigencia_capital_por_riesgo_general",
   "type": "Operacion",
   "label": "Determinación de exigencia riesgo general tasa interés",
   "tokens_matcheados": 3,
   "resumen_propiedades": "tipo: cálculo de exigencia capital por riesgo general"
  },
  {
   "id": "Operacion_calculo_de_exigencia_capital_por_riesgo_especifico",
   "type": "Operacion",
   "label": "Determinación de exigencia riesgo específico tasa interés",
   "tokens_matcheados": 3,
   "resumen_propiedades": "tipo: cálculo de exigencia capital por riesgo específico"
  },
  {
   "id": "Obligacion_los_riesgos_de_tasa_de_interes_y_de_moneda_extranjera_deberan_mitigarse_en_forma",
   "type": "Obligacion",
   "label": "Mitigar descalce de tasa y moneda",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Los riesgos de tasa de interés y de moneda extranjera deberán mitigarse en forma adecuada, sin que esto implique que deba obtenerse una cobertura perfecta y com…"
  },
  {
   "id": "Restriccion_exposiciones_por_compras_en_cuotas_con_tarjeta_credito_hasta_25_11_21",
   "type": "Restriccion",
   "label": "Coeficiente de riesgo 1250 puntos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Exposiciones por compras en cuotas con tarjeta crédito hasta 25/11/21"
  },
  {
   "id": "Restriccion_los_swaps_de_monedas_y_tasas_de_interes_los_fras_los_forwards_de_moneda_y_los_fu",
   "type": "Restriccion",
   "label": "Exclusión riesgo específico derivados",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Los swaps de monedas y tasas de interés, los FRAs, los forwards de moneda y los futuros de tasa de interés o sobre un índice de tasa de interés no estarán sujet…"
  }
 ]
}
```



---

# CQN-008

## Respuesta final íntegra (trace.final_json)

```json
{
 "respuesta": "Sí, las empresas no financieras emisoras de tarjetas de crédito están alcanzadas por las normas de protección de los usuarios de servicios financieros. Según la normativa, estas empresas deben designar a un miembro del Directorio o autoridad equivalente como Directivo Responsable de Protección de los Usuarios de Servicios Financieros ante el BCRA, y están sujetas a todas las obligaciones de los sujetos obligados en materia de protección de usuarios.\n\nRespecto a la clasificación de deudores, las empresas no financieras emisoras de tarjetas de crédito se consideran proveedores no financieros de crédito y, como tales, están alcanzadas por las normas sobre clasificación de deudores. Los criterios que deben aplicar para clasificar a sus deudores son los criterios objetivos de clasificación establecidos en la normativa, que incluyen: (1) el término de morosidad (atrasos de hasta 180 días, atrasos superiores a 180 días hasta un año, atrasos superiores a 540 días); (2) la situación jurídica del cliente o de sus deudas (gestión judicial, concurso preventivo, acuerdo extrajudicial); y (3) el cumplimiento de refinanciaciones y pedidos de refinanciaciones de obligaciones.",
 "citas": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "Punto 3.2. Controles. (parte 1)"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Punto 10.1. Proveedores no financieros de crédito."
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Punto 6.4. Reconsideración obligatoria de la clasificación."
  }
 ],
 "respondible": true
}
```

(`respondible`: true · tool_calls_used: 16 · hit_tool_limit: True)

## Inventario de pasos + fidelidad runtime↔re-ejecución

| paso | tool | input | output_chars (runtime) | re-ejecutado | fiel |
|---|---|---|---|---|---|
| 1 | buscar_nodos | `{"consulta": "empresas no financieras emisoras tarjetas crédito", "limite": 10}` | 3198 | 3198 | SÍ |
| 2 | buscar_nodos | `{"consulta": "protección usuarios servicios financieros", "limite": 10}` | 3814 | 3814 | SÍ |
| 3 | buscar_nodos | `{"consulta": "clasificación deudores criterios", "limite": 10}` | 3281 | 3281 | SÍ |
| 4 | ver_nodo | `{"id": "EntidadFinanciera_empresa_no_financiera_emisora"}` | 656 | 656 | SÍ |
| 5 | ver_nodo | `{"id": "TextoOrdenado_to_proteccion_usuarios_servicios_financieros_actual_pdf"}` | 434 | 434 | SÍ |
| 6 | ver_nodo | `{"id": "TextoOrdenado_to_clasificacion_deudores_actual_pdf"}` | 397 | 397 | SÍ |
| 7 | ver_vecinos | `{"id": "EntidadFinanciera_empresa_no_financiera_emisora", "direccion": "salientes"}` | 1911 | 1911 | SÍ |
| 8 | buscar_nodos | `{"consulta": "sujetos obligados protección usuarios empresas no financieras", "limite": 10` | 3792 | 3792 | SÍ |
| 9 | buscar_nodos | `{"consulta": "proveedores no financieros crédito clasificación deudores", "limite": 10}` | 2942 | 2942 | SÍ |
| 10 | ver_nodo | `{"id": "Obligacion_las_entidades_financieras_las_empresas_no_financieras_emisoras_de_tarje` | 688 | 688 | SÍ |
| 11 | buscar_nodos | `{"consulta": "criterios clasificación deudores situación jurídica morosidad", "limite": 10` | 3288 | 3288 | SÍ |
| 12 | buscar_nodos | `{"consulta": "punto 10 proveedores no financieros crédito clasificación", "limite": 10}` | 3064 | 3064 | SÍ |
| 13 | ver_nodo | `{"id": "EntidadFinanciera_proveedor_no_financiero_de_credito"}` | 469 | 469 | SÍ |
| 14 | buscar_nodos | `{"consulta": "criterios objetivos clasificación morosidad días vencimiento", "limite": 10}` | 3380 | 3380 | SÍ |
| 15 | ver_nodo | `{"id": "Excepcion_modificacion_de_alguno_de_los_criterios_objetivos_de_clasificacion_que_s` | 606 | 606 | SÍ |
| 16 | buscar_nodos | `{"consulta": "punto 10.1 proveedores no financieros criterios clasificación", "limite": 10` | 3102 | 3102 | SÍ |

**Fidelidad: 16/16** (igualdad de largos del output completo).

## Apéndice — outputs completos re-ejecutados

### paso 1 — buscar_nodos {"consulta": "empresas no financieras emisoras tarjetas crédito", "limite": 10}

```json
{
 "consulta": "empresas no financieras emisoras tarjetas crédito",
 "total_con_match": 524,
 "resultados": [
  {
   "id": "Obligacion_las_entidades_financieras_las_empresas_no_financieras_emisoras_de_tarjetas_de_cr",
   "type": "Obligacion",
   "label": "Designar Directivo Responsable de Protección",
   "tokens_matcheados": 5,
   "resumen_propiedades": "Las entidades financieras, las empresas no financieras emisoras de tarjetas de crédito y/o compra y los otros proveedores no financieros de crédito deberán desi…"
  },
  {
   "id": "Restriccion_las_entidades_financieras_y_las_empresas_no_financieras_emisoras_de_tarjetas_loc",
   "type": "Restriccion",
   "label": "Conformidad previa BCRA acceso mercado cambios",
   "tokens_matcheados": 5,
   "resumen_propiedades": "Las entidades financieras y las empresas no financieras emisoras de tarjetas locales deberán contar con la conformidad previa del BCRA para acceder al mercado d…"
  },
  {
   "id": "EntidadFinanciera_empresa_no_financiera_emisora",
   "type": "EntidadFinanciera",
   "label": "Empresas no financieras emisoras",
   "tokens_matcheados": 4,
   "resumen_propiedades": "categoria: empresa no financiera emisora de tarjetas"
  },
  {
   "id": "Obligacion_las_entidades_financieras_los_pspcp_las_empresas_no_financieras_emisoras_de_tarj",
   "type": "Obligacion",
   "label": "Informar comisiones y cargos al BCRA",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Las entidades financieras, los PSPCP, las empresas no financieras emisoras de tarjetas de crédito y/o compra y los otros proveedores no financieros de crédito d…"
  },
  {
   "id": "Restriccion_las_entidades_financieras_y_otras_emisoras_de_tarjetas_locales_de_credito_y_o_co",
   "type": "Restriccion",
   "label": "Límite adelanto en efectivo exterior",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Las entidades financieras y otras emisoras de tarjetas locales de crédito y/o compra podrán otorgar como adelanto en efectivo a los tarjetahabientes en el exter…"
  },
  {
   "id": "EntidadFinanciera_entidad_no_financiera_emisora_de_tarjeta",
   "type": "EntidadFinanciera",
   "label": "Entidades no financieras emisoras de tarjetas",
   "tokens_matcheados": 4,
   "resumen_propiedades": "categoria: entidad no financiera emisora de tarjetas de crédito"
  },
  {
   "id": "EntidadFinanciera_entidad_financiera_emisora_de_tarjeta_de_credito",
   "type": "EntidadFinanciera",
   "label": "Entidades financieras emisoras de tarjetas de crédito",
   "tokens_matcheados": 4,
   "resumen_propiedades": "categoria: emisora de tarjeta de crédito"
  },
  {
   "id": "EntidadFinanciera_empresa_emisora_de_tarjeta",
   "type": "EntidadFinanciera",
   "label": "Empresas emisoras de tarjetas",
   "tokens_matcheados": 3,
   "resumen_propiedades": "categoria: empresa emisora de tarjetas de crédito"
  },
  {
   "id": "EntidadFinanciera_emisora_de_tarjeta_local",
   "type": "EntidadFinanciera",
   "label": "Emisoras de tarjetas locales",
   "tokens_matcheados": 2,
   "resumen_propiedades": "categoria: emisora de tarjetas de crédito y/o compra"
  },
  {
   "id": "Restriccion_la_exposicion_presente_respecto_de_la_contraparte_no_puede_tener_un_valor_negati",
   "type": "Restriccion",
   "label": "Crédito de riesgo no negativo",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La exposición presente respecto de la contraparte no puede tener un valor negativo"
  }
 ]
}
```

### paso 2 — buscar_nodos {"consulta": "protección usuarios servicios financieros", "limite": 10}

```json
{
 "consulta": "protección usuarios servicios financieros",
 "total_con_match": 162,
 "resultados": [
  {
   "id": "TextoOrdenado_to_proteccion_usuarios_servicios_financieros_actual_pdf",
   "type": "TextoOrdenado",
   "label": "Protección de Usuarios",
   "tokens_matcheados": 4,
   "resumen_propiedades": "materia: Protección de los usuarios de servicios financieros; archivo: TO_proteccion_usuarios_servicios_financieros_actual.pdf; version: 8a"
  },
  {
   "id": "EntidadFinanciera_usuario_de_servicio_financiero",
   "type": "EntidadFinanciera",
   "label": "Usuarios de servicios financieros",
   "tokens_matcheados": 3,
   "resumen_propiedades": "categoria: usuario de servicio financiero"
  },
  {
   "id": "Obligacion_la_gerencia_principal_de_proteccion_al_usuario_de_servicios_financieros_tramitar",
   "type": "Obligacion",
   "label": "Tramitar denuncias de asociaciones",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La Gerencia Principal de Protección al Usuario de Servicios Financieros tramitará las denuncias que presenten las asociaciones de consumidores y usuarios recono…"
  },
  {
   "id": "Obligacion_los_sujetos_obligados_deberan_ofrecer_a_los_usuarios_de_servicios_financieros_po",
   "type": "Obligacion",
   "label": "Ofrecer mínimo tres compañías aseguradoras",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Los sujetos obligados deberán ofrecer a los usuarios de servicios financieros por lo menos tres compañías aseguradoras no vinculadas entre sí entre las que debe…"
  },
  {
   "id": "Obligacion_las_presentaciones_de_los_usuarios_de_servicios_financieros_deberan_poder_realiz",
   "type": "Obligacion",
   "label": "Habilitar múltiples canales de presentación",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Las presentaciones de los usuarios de servicios financieros deberán poder realizarse por teléfono, Internet, por escrito, fax, correo postal y electrónico (e-ma…"
  },
  {
   "id": "Obligacion_la_gerencia_principal_de_proteccion_al_usuario_de_servicios_financieros_brindara",
   "type": "Obligacion",
   "label": "Brindar respuesta a consultas sobre normativa",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La Gerencia Principal de Protección al Usuario de Servicios Financieros brindará respuesta por los medios habilitados a las consultas del público sobre la norma…"
  },
  {
   "id": "Obligacion_dando_orientacion_a_los_usuarios_de_servicios_financieros_sobre_la_manera_de_can",
   "type": "Obligacion",
   "label": "Dar orientación sobre canalización de reclamos",
   "tokens_matcheados": 3,
   "resumen_propiedades": "dando orientación a los usuarios de servicios financieros sobre la manera de canalizar los reclamos por la actuación de los sujetos previstos en el punto 1.1.2"
  },
  {
   "id": "Obligacion_se_debe_notificar_en_el_contrato_a_los_usuarios_de_servicios_financieros_sobre_l",
   "type": "Obligacion",
   "label": "Notificar condiciones modificables en contrato",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Se debe notificar en el contrato a los usuarios de servicios financieros sobre las condiciones que pueden ser objeto de modificación, así como de la facultad de…"
  },
  {
   "id": "Obligacion_los_cajeros_automaticos_destinados_a_los_usuarios_de_servicios_financieros_con_d",
   "type": "Obligacion",
   "label": "Cajeros con funcionalidades para usuarios visuales",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Los cajeros automáticos destinados a los usuarios de servicios financieros con dificultades visuales deberán contar con \"software\" reproductor de texto-a-voz, a…"
  },
  {
   "id": "Obligacion_tambien_se_recibiran_de_los_usuarios_de_servicios_financieros_por_igual_via_come",
   "type": "Obligacion",
   "label": "Recibir comentarios, sugerencias y quejas de usuarios",
   "tokens_matcheados": 3,
   "resumen_propiedades": "También se recibirán de los usuarios de servicios financieros –por igual vía– comentarios, sugerencias y quejas en relación con la actuación de los sujetos obli…"
  }
 ]
}
```

### paso 3 — buscar_nodos {"consulta": "clasificación deudores criterios", "limite": 10}

```json
{
 "consulta": "clasificación deudores criterios",
 "total_con_match": 96,
 "resultados": [
  {
   "id": "TextoOrdenado_to_clasificacion_deudores_actual_pdf",
   "type": "TextoOrdenado",
   "label": "Clasificación de Deudores",
   "tokens_matcheados": 2,
   "resumen_propiedades": "materia: clasificacion_deudores; archivo: TO_clasificacion_deudores_actual.pdf; version: vigente"
  },
  {
   "id": "Operacion_clasificacion_de_deudores_en_situacion_irregular",
   "type": "Operacion",
   "label": "Incremento cartera irregular",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: clasificación de deudores en situación irregular"
  },
  {
   "id": "Restriccion_no_seran_objeto_de_clasificacion_quienes_resulten_deudores_en_operaciones_de_ces",
   "type": "Restriccion",
   "label": "Exclusión de deudores en cesión",
   "tokens_matcheados": 2,
   "resumen_propiedades": "No serán objeto de clasificación quienes resulten deudores en operaciones de cesión sin responsabilidad para el cedente"
  },
  {
   "id": "Operacion_clasificacion_de_deudores",
   "type": "Operacion",
   "label": "Tarea de clasificación de deudores",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: clasificación de deudores"
  },
  {
   "id": "Operacion_revision_de_clasificacion_de_deudores",
   "type": "Operacion",
   "label": "Revisión de clasificación trimestral",
   "tokens_matcheados": 2,
   "resumen_propiedades": "En el curso de cada trimestre calendario, respecto de clientes individualmente considerados cuyas financiaciones comprendidas en algún momento sean equivalentes…"
  },
  {
   "id": "Obligacion_la_clasificacion_de_los_deudores_debera_efectuarse_con_una_periodicidad_que_atie",
   "type": "Obligacion",
   "label": "Efectuar clasificación periódicamente",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La clasificación de los deudores deberá efectuarse con una periodicidad que atienda a su importancia, considerando la totalidad de las financiaciones comprendid…"
  },
  {
   "id": "Restriccion_las_inversiones_en_instrumentos_de_capital_que_no_cumplan_con_los_criterios_para",
   "type": "Restriccion",
   "label": "Clasificación de instrumentos capital",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Las inversiones en instrumentos de capital que no cumplan con los criterios para ser clasificados como CO, CA o PN de la entidad financiera serán considerados c…"
  },
  {
   "id": "Restriccion_deudores_que_no_deben_ser_objeto_de_clasificacion",
   "type": "Restriccion",
   "label": "Exclusión de deudores de clasificación",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Deudores que no deben ser objeto de clasificación"
  },
  {
   "id": "Restriccion_incluye_deudores_con_obligaciones_iguales_o_superiores_al_20_del_patrimonio_o_en",
   "type": "Restriccion",
   "label": "Clasificación por obligaciones insolventes",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Incluye deudores con obligaciones iguales o superiores al 20% del patrimonio, o entre 5% y menos del 20% cuando persista pedido de quiebra después de 90 días"
  },
  {
   "id": "Excepcion_modificacion_de_alguno_de_los_criterios_objetivos_de_clasificacion_que_surjan_de",
   "type": "Excepcion",
   "label": "Excepción por criterios objetivos modificados",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Modificación de alguno de los criterios objetivos de clasificación que surjan de estas normas (término de morosidad, situación jurídica del cliente o de sus deu…"
  }
 ]
}
```

### paso 4 — ver_nodo {"id": "EntidadFinanciera_empresa_no_financiera_emisora"}

```json
{
 "id": "EntidadFinanciera_empresa_no_financiera_emisora",
 "type": "EntidadFinanciera",
 "label": "Empresas no financieras emisoras",
 "properties": {
  "categoria": "empresa no financiera emisora de tarjetas"
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 4.1. Operaciones con débito en una cuenta en una entidad financiera local y/o con tar"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Punto 10.1. Proveedores no financieros de crédito."
  },
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "Punto 2.3. Recaudos mínimos de la relación de consumo. (parte 6)"
  }
 ]
}
```

### paso 5 — ver_nodo {"id": "TextoOrdenado_to_proteccion_usuarios_servicios_financieros_actual_pdf"}

```json
{
 "id": "TextoOrdenado_to_proteccion_usuarios_servicios_financieros_actual_pdf",
 "type": "TextoOrdenado",
 "label": "Protección de Usuarios",
 "properties": {
  "materia": "Protección de los usuarios de servicios financieros",
  "archivo": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
  "version": "8a"
 },
 "provenances": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "Punto 1.1. Partes."
  }
 ]
}
```

### paso 6 — ver_nodo {"id": "TextoOrdenado_to_clasificacion_deudores_actual_pdf"}

```json
{
 "id": "TextoOrdenado_to_clasificacion_deudores_actual_pdf",
 "type": "TextoOrdenado",
 "label": "Clasificación de Deudores",
 "properties": {
  "materia": "clasificacion_deudores",
  "archivo": "TO_clasificacion_deudores_actual.pdf",
  "version": "vigente"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Punto 1.1. “A” 2216 I 1° Incluye aclaración interpretativa."
  }
 ]
}
```

### paso 7 — ver_vecinos {"id": "EntidadFinanciera_empresa_no_financiera_emisora", "direccion": "salientes"}

```json
{
 "id": "EntidadFinanciera_empresa_no_financiera_emisora",
 "label": "Empresas no financieras emisoras",
 "n_salientes_total": 6,
 "n_entrantes_total": 22,
 "salientes": [
  {
   "relation": "ejecuta",
   "vecino_id": "Operacion_clasificacion_de_deudor",
   "vecino_label": "Evaluación grado de inversión",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "Punto 10.1. Proveedores no financieros de crédito."
    }
   ]
  },
  {
   "relation": "ejecuta",
   "vecino_id": "Operacion_pago_al_exterior_por_uso_de_tarjetas",
   "vecino_label": "Pagos al exterior por uso de tarjetas",
   "provenances": [
    {
     "source_doc": "TO_exterior_cambios_actual.pdf",
     "location": "Punto 3.16. Requisitos complementarios para los egresos por el mercado de cambios. (parte 1)"
    }
   ]
  },
  {
   "relation": "ejecuta",
   "vecino_id": "Operacion_emision_de_tarjetas_de_credito_y_o_compra",
   "vecino_label": "Emisión de tarjetas de crédito",
   "provenances": [
    {
     "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
     "location": "Punto 1.1. Partes."
    }
   ]
  },
  {
   "relation": "ejecuta",
   "vecino_id": "Operacion_contratacion_de_productos_y_servicios_financieros",
   "vecino_label": "Contratación de productos y servicios",
   "provenances": [
    {
     "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
     "location": "Punto 3.2. Controles. (parte 1)"
    }
   ]
  },
  {
   "relation": "ejecuta",
   "vecino_id": "Operacion_aplicacion_de_comisiones_y_cargos",
   "vecino_label": "Aplicación de comisiones y cargos",
   "provenances": [
    {
     "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
     "location": "Punto 3.2. Controles. (parte 1)"
    }
   ]
  },
  {
   "relation": "ejecuta",
   "vecino_id": "Operacion_presentacion_de_consulta_o_reclamo_de_usuario",
   "vecino_label": "Presentación de consulta o reclamo",
   "provenances": [
    {
     "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
     "location": "Punto 3.2. Controles. (parte 1)"
    }
   ]
  }
 ],
 "salientes_truncado": false
}
```

### paso 8 — buscar_nodos {"consulta": "sujetos obligados protección usuarios empresas no financieras", "limite": 10}

```json
{
 "consulta": "sujetos obligados protección usuarios empresas no financieras",
 "total_con_match": 470,
 "resultados": [
  {
   "id": "Restriccion_los_sujetos_obligados_no_podran_percibir_de_los_usuarios_ningun_tipo_de_comision",
   "type": "Restriccion",
   "label": "Prohibición de comisiones por seguros vida",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Los sujetos obligados no podrán percibir de los usuarios ningún tipo de comisión y/o cargo vinculado con seguros de vida sobre saldo deudor"
  },
  {
   "id": "Obligacion_las_entidades_financieras_las_empresas_no_financieras_emisoras_de_tarjetas_de_cr",
   "type": "Obligacion",
   "label": "Designar Directivo Responsable de Protección",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Las entidades financieras, las empresas no financieras emisoras de tarjetas de crédito y/o compra y los otros proveedores no financieros de crédito deberán desi…"
  },
  {
   "id": "Restriccion_los_sujetos_obligados_no_podran_percibir_de_los_usuarios_ningun_tipo_de_retribuc",
   "type": "Restriccion",
   "label": "Prohibición de retribuciones por seguros no accesorios",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Los sujetos obligados no podrán percibir de los usuarios ningún tipo de retribución –comisión y/o cargo– adicional al premio determinado por la aseguradora, vin…"
  },
  {
   "id": "Obligacion_los_sujetos_obligados_deberan_adoptar_las_acciones_necesarias_para_garantizar_de",
   "type": "Obligacion",
   "label": "Garantizar derechos de usuarios",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Los sujetos obligados deberán adoptar las acciones necesarias para garantizar derechos de protección de seguridad e intereses económicos, información clara y ve…"
  },
  {
   "id": "EntidadFinanciera_empresa_no_financiera_emisora",
   "type": "EntidadFinanciera",
   "label": "Empresas no financieras emisoras",
   "tokens_matcheados": 3,
   "resumen_propiedades": "categoria: empresa no financiera emisora de tarjetas"
  },
  {
   "id": "Obligacion_las_entidades_financieras_los_pspcp_las_empresas_no_financieras_emisoras_de_tarj",
   "type": "Obligacion",
   "label": "Informar comisiones y cargos al BCRA",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Las entidades financieras, los PSPCP, las empresas no financieras emisoras de tarjetas de crédito y/o compra y los otros proveedores no financieros de crédito d…"
  },
  {
   "id": "Restriccion_las_politicas_practicas_y_procedimientos_de_los_sujetos_obligados_no_podran_repr",
   "type": "Restriccion",
   "label": "Prohibición de trato discriminatorio",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Las políticas, prácticas y procedimientos de los sujetos obligados no podrán representar un trato discriminatorio de los usuarios."
  },
  {
   "id": "Obligacion_los_sujetos_obligados_deberan_ofrecer_a_los_usuarios_de_servicios_financieros_po",
   "type": "Obligacion",
   "label": "Ofrecer mínimo tres compañías aseguradoras",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Los sujetos obligados deberán ofrecer a los usuarios de servicios financieros por lo menos tres compañías aseguradoras no vinculadas entre sí entre las que debe…"
  },
  {
   "id": "Obligacion_los_sujetos_obligados_deberan_asegurar_a_los_usuarios_condiciones_igualitarias_d",
   "type": "Obligacion",
   "label": "Asegurar condiciones igualitarias de acceso",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Los sujetos obligados deberán asegurar a los usuarios condiciones igualitarias de acceso a los servicios que ofrecen y prestan"
  },
  {
   "id": "Obligacion_para_el_caso_de_los_sujetos_obligados_no_alcanzados_por_la_obligacion_prevista_e",
   "type": "Obligacion",
   "label": "Evaluar reportes de otros sujetos obligados",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Para el caso de los sujetos obligados no alcanzados por la obligación prevista en el punto 3.2.1.1., el Directorio o autoridad equivalente deberá evaluar los re…"
  }
 ]
}
```

### paso 9 — buscar_nodos {"consulta": "proveedores no financieros crédito clasificación deudores", "limite": 10}

```json
{
 "consulta": "proveedores no financieros crédito clasificación deudores",
 "total_con_match": 573,
 "resultados": [
  {
   "id": "EntidadFinanciera_proveedor_no_financiero_de_credito",
   "type": "EntidadFinanciera",
   "label": "Proveedores no financieros de crédito",
   "tokens_matcheados": 4,
   "resumen_propiedades": "categoria: proveedor no financiero de crédito"
  },
  {
   "id": "Restriccion_no_seran_objeto_de_clasificacion_quienes_resulten_deudores_en_operaciones_de_ces",
   "type": "Restriccion",
   "label": "Exclusión de deudores en cesión",
   "tokens_matcheados": 3,
   "resumen_propiedades": "No serán objeto de clasificación quienes resulten deudores en operaciones de cesión sin responsabilidad para el cedente"
  },
  {
   "id": "Restriccion_deudores_que_no_deben_ser_objeto_de_clasificacion",
   "type": "Restriccion",
   "label": "Exclusión de deudores de clasificación",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Deudores que no deben ser objeto de clasificación"
  },
  {
   "id": "TextoOrdenado_to_clasificacion_deudores_actual_pdf",
   "type": "TextoOrdenado",
   "label": "Clasificación de Deudores",
   "tokens_matcheados": 2,
   "resumen_propiedades": "materia: clasificacion_deudores; archivo: TO_clasificacion_deudores_actual.pdf; version: vigente"
  },
  {
   "id": "Operacion_clasificacion_de_deudores_en_situacion_irregular",
   "type": "Operacion",
   "label": "Incremento cartera irregular",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: clasificación de deudores en situación irregular"
  },
  {
   "id": "Restriccion_la_exposicion_presente_respecto_de_la_contraparte_no_puede_tener_un_valor_negati",
   "type": "Restriccion",
   "label": "Crédito de riesgo no negativo",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La exposición presente respecto de la contraparte no puede tener un valor negativo"
  },
  {
   "id": "EntidadFinanciera_cliente_privado_no_financiero",
   "type": "EntidadFinanciera",
   "label": "Clientes privados no financieros",
   "tokens_matcheados": 2,
   "resumen_propiedades": "categoria: cliente del sector privado no financiero"
  },
  {
   "id": "Excepcion_la_clasificacion_se_verifica_a_partir_del_momento_en_que_no_habiendo_sido_rechaz",
   "type": "Excepcion",
   "label": "Excepción por rechazo de reclamo",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La clasificación se verifica a partir del momento en que, no habiendo sido rechazado el reclamo, se verifique la falta de pago del siniestro luego de vencidos l…"
  },
  {
   "id": "Obligacion_realizar_respecto_de_los_firmantes_libradores_deudores_codeudores_o_aceptantes_s",
   "type": "Obligacion",
   "label": "Evaluación como sujeto de crédito",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Realizar respecto de los firmantes, libradores, deudores, codeudores o aceptantes su evaluación como sujetos de crédito con la pertinente apertura del legajo"
  },
  {
   "id": "Operacion_clasificacion_de_deudores",
   "type": "Operacion",
   "label": "Tarea de clasificación de deudores",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: clasificación de deudores"
  }
 ]
}
```

### paso 10 — ver_nodo {"id": "Obligacion_las_entidades_financieras_las_empresas_no_financieras_emisoras_de_tarjetas_de_cr"}

```json
{
 "id": "Obligacion_las_entidades_financieras_las_empresas_no_financieras_emisoras_de_tarjetas_de_cr",
 "type": "Obligacion",
 "label": "Designar Directivo Responsable de Protección",
 "properties": {
  "descripcion": "Las entidades financieras, las empresas no financieras emisoras de tarjetas de crédito y/o compra y los otros proveedores no financieros de crédito deberán designar a un miembro del Directorio o autoridad equivalente como Directivo Responsable de Protección de los Usuarios de Servicios Financieros ante el BCRA.",
  "tipo": "asignacion"
 },
 "provenances": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "Punto 3.2. Controles. (parte 1)"
  }
 ]
}
```

### paso 11 — buscar_nodos {"consulta": "criterios clasificación deudores situación jurídica morosidad", "limite": 10}

```json
{
 "consulta": "criterios clasificación deudores situación jurídica morosidad",
 "total_con_match": 111,
 "resultados": [
  {
   "id": "Operacion_clasificacion_de_deudores_en_situacion_irregular",
   "type": "Operacion",
   "label": "Incremento cartera irregular",
   "tokens_matcheados": 3,
   "resumen_propiedades": "tipo: clasificación de deudores en situación irregular"
  },
  {
   "id": "TextoOrdenado_to_clasificacion_deudores_actual_pdf",
   "type": "TextoOrdenado",
   "label": "Clasificación de Deudores",
   "tokens_matcheados": 2,
   "resumen_propiedades": "materia: clasificacion_deudores; archivo: TO_clasificacion_deudores_actual.pdf; version: vigente"
  },
  {
   "id": "Operacion_estado_de_situacion_de_deudores",
   "type": "Operacion",
   "label": "Estado de situación de deudores",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Estado de situación de deudores referenciado en punto 6.1. y 6.2."
  },
  {
   "id": "Restriccion_no_seran_objeto_de_clasificacion_quienes_resulten_deudores_en_operaciones_de_ces",
   "type": "Restriccion",
   "label": "Exclusión de deudores en cesión",
   "tokens_matcheados": 2,
   "resumen_propiedades": "No serán objeto de clasificación quienes resulten deudores en operaciones de cesión sin responsabilidad para el cedente"
  },
  {
   "id": "Operacion_clasificacion_de_deudores",
   "type": "Operacion",
   "label": "Tarea de clasificación de deudores",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: clasificación de deudores"
  },
  {
   "id": "Obligacion_para_clasificacion_con_seguimiento_especial_en_observacion_el_analisis_del_flujo",
   "type": "Obligacion",
   "label": "Evaluación situación en observación",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Para clasificación con seguimiento especial en observación: El análisis del flujo de fondos del cliente demuestra que puede atender la totalidad de sus compromi…"
  },
  {
   "id": "Operacion_revision_de_clasificacion_de_deudores",
   "type": "Operacion",
   "label": "Revisión de clasificación trimestral",
   "tokens_matcheados": 2,
   "resumen_propiedades": "En el curso de cada trimestre calendario, respecto de clientes individualmente considerados cuyas financiaciones comprendidas en algún momento sean equivalentes…"
  },
  {
   "id": "Obligacion_la_clasificacion_de_los_deudores_debera_efectuarse_con_una_periodicidad_que_atie",
   "type": "Obligacion",
   "label": "Efectuar clasificación periódicamente",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La clasificación de los deudores deberá efectuarse con una periodicidad que atienda a su importancia, considerando la totalidad de las financiaciones comprendid…"
  },
  {
   "id": "Restriccion_las_inversiones_en_instrumentos_de_capital_que_no_cumplan_con_los_criterios_para",
   "type": "Restriccion",
   "label": "Clasificación de instrumentos capital",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Las inversiones en instrumentos de capital que no cumplan con los criterios para ser clasificados como CO, CA o PN de la entidad financiera serán considerados c…"
  },
  {
   "id": "Obligacion_para_clasificacion_en_situacion_normal_el_analisis_del_flujo_de_fondos_del_clien",
   "type": "Obligacion",
   "label": "Evaluación situación financiera normal",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Para clasificación en situación normal: El análisis del flujo de fondos del cliente demuestra que es capaz de atender adecuadamente todos sus compromisos financ…"
  }
 ]
}
```

### paso 12 — buscar_nodos {"consulta": "punto 10 proveedores no financieros crédito clasificación", "limite": 10}

```json
{
 "consulta": "punto 10 proveedores no financieros crédito clasificación",
 "total_con_match": 604,
 "resultados": [
  {
   "id": "EntidadFinanciera_proveedor_no_financiero_de_credito",
   "type": "EntidadFinanciera",
   "label": "Proveedores no financieros de crédito",
   "tokens_matcheados": 4,
   "resumen_propiedades": "categoria: proveedor no financiero de crédito"
  },
  {
   "id": "Restriccion_las_operaciones_no_comprendidas_en_el_punto_10_6_6",
   "type": "Restriccion",
   "label": "Exclusión de operaciones del punto 10.6.6",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Las operaciones no comprendidas en el punto 10.6.6."
  },
  {
   "id": "Excepcion_no_aplicable_punto_3_12_1",
   "type": "Excepcion",
   "label": "No aplicable punto 3.12.1",
   "tokens_matcheados": 2,
   "resumen_propiedades": "En la medida que no encuadre en el punto 3.12.1"
  },
  {
   "id": "Obligacion_cuando_el_pago_a_nombre_del_cliente_encuadre_en_el_punto_10_10_2_3_se_debera_dej",
   "type": "Obligacion",
   "label": "Dejar constancia en reporte",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Cuando el pago a nombre del cliente encuadre en el punto 10.10.2.3., se deberá dejar constancia de tal circunstancia al reportar el boleto de venta a nombre del…"
  },
  {
   "id": "Restriccion_la_exposicion_presente_respecto_de_la_contraparte_no_puede_tener_un_valor_negati",
   "type": "Restriccion",
   "label": "Crédito de riesgo no negativo",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La exposición presente respecto de la contraparte no puede tener un valor negativo"
  },
  {
   "id": "Excepcion_salvo_que_la_operacion_quedase_comprendida_en_lo_previsto_en_el_punto_10_10_2_11",
   "type": "Excepcion",
   "label": "Excepción por punto 10.10.2.11",
   "tokens_matcheados": 2,
   "resumen_propiedades": "salvo que la operación quedase comprendida en lo previsto en el punto 10.10.2.11"
  },
  {
   "id": "Restriccion_no_seran_objeto_de_clasificacion_quienes_resulten_deudores_en_operaciones_de_ces",
   "type": "Restriccion",
   "label": "Exclusión de deudores en cesión",
   "tokens_matcheados": 2,
   "resumen_propiedades": "No serán objeto de clasificación quienes resulten deudores en operaciones de cesión sin responsabilidad para el cedente"
  },
  {
   "id": "EntidadFinanciera_cliente_privado_no_financiero",
   "type": "EntidadFinanciera",
   "label": "Clientes privados no financieros",
   "tokens_matcheados": 2,
   "resumen_propiedades": "categoria: cliente del sector privado no financiero"
  },
  {
   "id": "Excepcion_la_clasificacion_se_verifica_a_partir_del_momento_en_que_no_habiendo_sido_rechaz",
   "type": "Excepcion",
   "label": "Excepción por rechazo de reclamo",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La clasificación se verifica a partir del momento en que, no habiendo sido rechazado el reclamo, se verifique la falta de pago del siniestro luego de vencidos l…"
  },
  {
   "id": "Obligacion_debera_verificar_previamente_que_se_cumplen_la_totalidad_de_requisitos_detallado",
   "type": "Obligacion",
   "label": "Verificar requisitos punto 10.3.2",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Deberá verificar previamente que se cumplen la totalidad de requisitos detallados en el punto 10.3.2."
  }
 ]
}
```

### paso 13 — ver_nodo {"id": "EntidadFinanciera_proveedor_no_financiero_de_credito"}

```json
{
 "id": "EntidadFinanciera_proveedor_no_financiero_de_credito",
 "type": "EntidadFinanciera",
 "label": "Proveedores no financieros de crédito",
 "properties": {
  "categoria": "proveedor no financiero de crédito"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Punto 10.1. Proveedores no financieros de crédito."
  },
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "Punto 3.2. Controles. (parte 1)"
  }
 ]
}
```

### paso 14 — buscar_nodos {"consulta": "criterios objetivos clasificación morosidad días vencimiento", "limite": 10}

```json
{
 "consulta": "criterios objetivos clasificación morosidad días vencimiento",
 "total_con_match": 145,
 "resultados": [
  {
   "id": "Excepcion_modificacion_de_alguno_de_los_criterios_objetivos_de_clasificacion_que_surjan_de",
   "type": "Excepcion",
   "label": "Excepción por criterios objetivos modificados",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Modificación de alguno de los criterios objetivos de clasificación que surjan de estas normas (término de morosidad, situación jurídica del cliente o de sus deu…"
  },
  {
   "id": "Restriccion_vencimiento_final_minimo_de_365_dias",
   "type": "Restriccion",
   "label": "Vencimiento final mínimo de 365 días",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El vencimiento final tenga lugar, como mínimo, una vez transcurrido 365 (trescientos sesenta y cinco) días corridos desde el registro de ingreso aduanero de los…"
  },
  {
   "id": "Restriccion_las_inversiones_en_instrumentos_de_capital_que_no_cumplan_con_los_criterios_para",
   "type": "Restriccion",
   "label": "Clasificación de instrumentos capital",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Las inversiones en instrumentos de capital que no cumplan con los criterios para ser clasificados como CO, CA o PN de la entidad financiera serán considerados c…"
  },
  {
   "id": "Restriccion_clientes_en_gestion_judicial_concurso_preventivo_o_acuerdo_extrajudicial_con_atr",
   "type": "Restriccion",
   "label": "Clasificación por atrasos superiores a 540 días",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Clientes en gestión judicial, concurso preventivo o acuerdo extrajudicial con atrasos superiores a 540 días"
  },
  {
   "id": "Restriccion_comprende_a_clientes_con_atrasos_de_mas_de_180_dias_hasta_un_ano",
   "type": "Restriccion",
   "label": "Clasificación por atrasos superiores a 180 días",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Comprende a clientes con atrasos de más de 180 días hasta un año"
  },
  {
   "id": "Obligacion_a_los_fines_de_la_clasificacion_debera_tenerse_en_cuenta_la_mora_en_el_atraso_de",
   "type": "Obligacion",
   "label": "Considerar mora al vencimiento emergencia agropecuaria",
   "tokens_matcheados": 2,
   "resumen_propiedades": "A los fines de la clasificación, deberá tenerse en cuenta la mora en el atraso de sus obligaciones para el momento en que concluya la vigencia de la emergencia …"
  },
  {
   "id": "Operacion_seleccion_de_subyacentes_mediante_criterios_de_elegibilidad",
   "type": "Operacion",
   "label": "Selección de activos",
   "tokens_matcheados": 1,
   "resumen_propiedades": "La selección de los activos deberá estar sujeta a criterios de elegibilidad claramente definidos, tales como el tamaño de la obligación, la edad del sujeto de c…"
  },
  {
   "id": "Operacion_clasificacion_de_cartera",
   "type": "Operacion",
   "label": "Agrupación de cartera",
   "tokens_matcheados": 1,
   "resumen_propiedades": "tipo: clasificación de cartera"
  },
  {
   "id": "Restriccion_exposicion_a_bmd_que_cumplen_criterios_basilea_con_ponderador_0",
   "type": "Restriccion",
   "label": "Ponderador BMD Basilea",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Exposición a BMD que cumplen criterios Basilea con ponderador 0%"
  },
  {
   "id": "Restriccion_incurra_en_atrasos_de_hasta_180_dias_con_exclusion_de_los_deudores_comprendidos_",
   "type": "Restriccion",
   "label": "Atrasos hasta 180 días",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Incurra en atrasos de hasta 180 días, con exclusión de los deudores comprendidos en el punto 6.5.2.2."
  }
 ]
}
```

### paso 15 — ver_nodo {"id": "Excepcion_modificacion_de_alguno_de_los_criterios_objetivos_de_clasificacion_que_surjan_de"}

```json
{
 "id": "Excepcion_modificacion_de_alguno_de_los_criterios_objetivos_de_clasificacion_que_surjan_de",
 "type": "Excepcion",
 "label": "Excepción por criterios objetivos modificados",
 "properties": {
  "descripcion": "Modificación de alguno de los criterios objetivos de clasificación que surjan de estas normas (término de morosidad, situación jurídica del cliente o de sus deudas, cumplimiento de refinanciaciones y pedidos de refinanciaciones de obligaciones)"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Punto 6.4. Reconsideración obligatoria de la clasificación."
  }
 ]
}
```

### paso 16 — buscar_nodos {"consulta": "punto 10.1 proveedores no financieros criterios clasificación", "limite": 10}

```json
{
 "consulta": "punto 10.1 proveedores no financieros criterios clasificación",
 "total_con_match": 538,
 "resultados": [
  {
   "id": "Excepcion_no_aplicable_punto_3_12_1",
   "type": "Excepcion",
   "label": "No aplicable punto 3.12.1",
   "tokens_matcheados": 3,
   "resumen_propiedades": "En la medida que no encuadre en el punto 3.12.1"
  },
  {
   "id": "EntidadFinanciera_proveedor_no_financiero_de_credito",
   "type": "EntidadFinanciera",
   "label": "Proveedores no financieros de crédito",
   "tokens_matcheados": 3,
   "resumen_propiedades": "categoria: proveedor no financiero de crédito"
  },
  {
   "id": "Restriccion_las_inversiones_en_instrumentos_de_capital_que_no_cumplan_con_los_criterios_para",
   "type": "Restriccion",
   "label": "Clasificación de instrumentos capital",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Las inversiones en instrumentos de capital que no cumplan con los criterios para ser clasificados como CO, CA o PN de la entidad financiera serán considerados c…"
  },
  {
   "id": "Restriccion_las_operaciones_no_comprendidas_en_el_punto_10_6_6",
   "type": "Restriccion",
   "label": "Exclusión de operaciones del punto 10.6.6",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Las operaciones no comprendidas en el punto 10.6.6."
  },
  {
   "id": "Restriccion_las_posiciones_arancelarias_de_los_bienes_no_correspondan_a_aquellas_comprendida",
   "type": "Restriccion",
   "label": "Exclusión de posiciones arancelarias del punto 12.1",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Las posiciones arancelarias de los bienes no correspondan a aquellas comprendidas en el punto 12.1"
  },
  {
   "id": "Obligacion_la_entidad_debera_verificar_las_condiciones_indicadas_en_el_punto_9_3_1_constata",
   "type": "Obligacion",
   "label": "Verificación cumplimiento requisitos puntos 7.9 o 7.10",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La entidad deberá verificar las condiciones indicadas en el punto 9.3.1., constatar que la cancelación tuvo lugar a partir de la fecha de vencimiento y contar c…"
  },
  {
   "id": "Excepcion_con_excepcion_de_los_casos_contemplados_en_el_punto_4_1",
   "type": "Excepcion",
   "label": "Excepción casos punto 4.1",
   "tokens_matcheados": 2,
   "resumen_propiedades": "con excepción de los casos contemplados en el punto 4.1"
  },
  {
   "id": "Obligacion_cuando_el_pago_a_nombre_del_cliente_encuadre_en_el_punto_10_10_2_3_se_debera_dej",
   "type": "Obligacion",
   "label": "Dejar constancia en reporte",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Cuando el pago a nombre del cliente encuadre en el punto 10.10.2.3., se deberá dejar constancia de tal circunstancia al reportar el boleto de venta a nombre del…"
  },
  {
   "id": "Restriccion_acciones_definidas_conforme_al_punto_2_11_3_250",
   "type": "Restriccion",
   "label": "Ponderador acciones grupo 1",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Acciones (definidas conforme al punto 2.11.3.): 250"
  },
  {
   "id": "Restriccion_el_activo_recibido_en_garantia_se_limitara_a_aquellos_listados_en_el_punto_5_3_1",
   "type": "Restriccion",
   "label": "Activos limitados a listado",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El activo recibido en garantía se limitará a aquellos listados en el punto 5.3.1.2."
  }
 ]
}
```



---

# CQN-009

## Respuesta final íntegra (trace.final_json)

```json
{
 "respuesta": "No se encontró en el Knowledge Graph información específica sobre qué importe debe consignarse en el 'total de control' correspondiente al capital mínimo básico del régimen informativo sobre exigencia e integración de capitales mínimos para bancos que no sean cajas de crédito cooperativa. Si bien se confirma que los bancos deben mantener una exigencia básica de capital mínimo de 5.000 millones de pesos, la documentación disponible no especifica cómo debe reportarse este importe en un campo denominado 'total de control' en el régimen informativo.",
 "citas": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Punto 1.2. Exigencia básica."
  }
 ],
 "respondible": false
}
```

(`respondible`: false · tool_calls_used: 15 · hit_tool_limit: True)

## Inventario de pasos + fidelidad runtime↔re-ejecución

| paso | tool | input | output_chars (runtime) | re-ejecutado | fiel |
|---|---|---|---|---|---|
| 1 | buscar_nodos | `{"consulta": "capital mínimo básico régimen informativo exigencia integración", "limite": ` | 3012 | 3012 | SÍ |
| 2 | buscar_nodos | `{"consulta": "total de control capital mínimo banco", "limite": 10}` | 3226 | 3226 | SÍ |
| 3 | buscar_nodos | `{"consulta": "régimen informativo capital mínimo total control", "limite": 10}` | 3093 | 3093 | SÍ |
| 4 | buscar_nodos | `{"consulta": "caja de crédito cooperativa capital mínimo básico", "limite": 10}` | 2780 | 2780 | SÍ |
| 5 | ver_nodo | `{"id": "Restriccion_los_bancos_deberan_mantener_una_exigencia_basica_de_capital_minimo_de_` | 469 | 469 | SÍ |
| 6 | ver_vecinos | `{"id": "Restriccion_los_bancos_deberan_mantener_una_exigencia_basica_de_capital_minimo_de_` | 1270 | 1270 | SÍ |
| 7 | buscar_nodos | `{"consulta": "total de control importe consignar banco", "limite": 10}` | 3411 | 3411 | SÍ |
| 8 | buscar_nodos | `{"consulta": "5000 millones pesos capital mínimo básico", "limite": 10}` | 3093 | 3093 | SÍ |
| 9 | buscar_nodos | `{"consulta": "total control reporte información capital", "limite": 10}` | 3716 | 3716 | SÍ |
| 10 | buscar_nodos | `{"consulta": "importe consignar banco no caja crédito cooperativa", "limite": 10}` | 3320 | 3320 | SÍ |
| 11 | ver_nodo | `{"id": "Obligacion_consignar_importe_patrimonio_neto"}` | 520 | 520 | SÍ |
| 12 | ver_vecinos | `{"id": "Obligacion_consignar_importe_patrimonio_neto"}` | 1083 | 1083 | SÍ |
| 13 | buscar_nodos | `{"consulta": "total de control capital mínimo básico banco", "limite": 15}` | 4694 | 4694 | SÍ |
| 14 | buscar_nodos | `{"consulta": "total control 5000 millones", "limite": 10}` | 3403 | 3403 | SÍ |
| 15 | buscar_nodos | `{"consulta": "consignar total control exigencia capital", "limite": 10}` | 3557 | 3557 | SÍ |

**Fidelidad: 15/15** (igualdad de largos del output completo).

## Apéndice — outputs completos re-ejecutados

### paso 1 — buscar_nodos {"consulta": "capital mínimo básico régimen informativo exigencia integración", "limite": 10}

```json
{
 "consulta": "capital mínimo básico régimen informativo exigencia integración",
 "total_con_match": 340,
 "resultados": [
  {
   "id": "Restriccion_los_bancos_deberan_mantener_una_exigencia_basica_de_capital_minimo_de_5_000_mill",
   "type": "Restriccion",
   "label": "Exigencia básica bancos",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Los bancos deberán mantener una exigencia básica de capital mínimo de 5.000 millones de pesos"
  },
  {
   "id": "Operacion_integracion_de_capital_minimo",
   "type": "Operacion",
   "label": "Integración de capital mínimo",
   "tokens_matcheados": 3,
   "resumen_propiedades": "tipo: integración de capital mínimo"
  },
  {
   "id": "Operacion_calculo_de_exigencia_de_capital_minimo_por_riesgo_de_credito",
   "type": "Operacion",
   "label": "Cálculo exigencia capital mínimo",
   "tokens_matcheados": 3,
   "resumen_propiedades": "tipo: cálculo de exigencia de capital mínimo por riesgo de crédito"
  },
  {
   "id": "Restriccion_la_exigencia_determinada_a_traves_de_la_aplicacion_de_la_expresion_descripta_en_",
   "type": "Restriccion",
   "label": "Límite 20% grupo A capital mínimo",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La exigencia determinada a través de la aplicación de la expresión descripta en el punto 7.2. no podrá superar el 20% en el caso de entidades del grupo A del pr…"
  },
  {
   "id": "Restriccion_las_restantes_entidades_deberan_mantener_una_exigencia_basica_de_capital_minimo_",
   "type": "Restriccion",
   "label": "Exigencia básica restantes entidades",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Las restantes entidades deberán mantener una exigencia básica de capital mínimo de 2.500 millones de pesos"
  },
  {
   "id": "Operacion_cumplimiento_de_capital",
   "type": "Operacion",
   "label": "Cumplimiento integración capital mínimo",
   "tokens_matcheados": 3,
   "resumen_propiedades": "tipo: cumplimiento de capital"
  },
  {
   "id": "Operacion_calculo_de_capital_minimo",
   "type": "Operacion",
   "label": "Cálculo de exigencia por riesgo de crédito",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Determinación de la exigencia de capital por riesgo de crédito conforme a la fórmula C_RC = (k x 0,08 x APR_c) + INC"
  },
  {
   "id": "Operacion_medicion_de_capital_minimo",
   "type": "Operacion",
   "label": "Medición de exigencia por riesgo de mercado",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Medición de la exigencia por riesgo de mercado conforme a lo dispuesto en el punto 6.10"
  },
  {
   "id": "Operacion_calculo_de_capital_minimo_por_riesgo_operacional",
   "type": "Operacion",
   "label": "Cálculo exigencia capital mínimo operacional",
   "tokens_matcheados": 3,
   "resumen_propiedades": "tipo: cálculo de capital mínimo por riesgo operacional"
  },
  {
   "id": "Restriccion_la_exigencia_mensual_de_capital_minimo_por_riesgo_operacional_de_las_entidades_f",
   "type": "Restriccion",
   "label": "Exigencia capital mínimo por riesgo operacional",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La exigencia mensual de capital mínimo por riesgo operacional de las entidades financieras de los grupos 1 y 2 correspondiente al primer mes será equivalente al…"
  }
 ]
}
```

### paso 2 — buscar_nodos {"consulta": "total de control capital mínimo banco", "limite": 10}

```json
{
 "consulta": "total de control capital mínimo banco",
 "total_con_match": 2470,
 "resultados": [
  {
   "id": "Restriccion_los_bancos_deberan_mantener_una_exigencia_basica_de_capital_minimo_de_5_000_mill",
   "type": "Restriccion",
   "label": "Exigencia básica bancos",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Los bancos deberán mantener una exigencia básica de capital mínimo de 5.000 millones de pesos"
  },
  {
   "id": "Restriccion_cuando_el_total_de_participaciones_en_el_capital_de_entidades_financieras_empres",
   "type": "Restriccion",
   "label": "Límite tenencias capital 10%",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Cuando el total de participaciones en el capital de entidades financieras, empresas de servicios complementarios de la actividad financiera y compañías de segur…"
  },
  {
   "id": "Operacion_integracion_de_capital_minimo",
   "type": "Operacion",
   "label": "Integración de capital mínimo",
   "tokens_matcheados": 3,
   "resumen_propiedades": "tipo: integración de capital mínimo"
  },
  {
   "id": "Restriccion_vencimiento_minimo_de_capital",
   "type": "Restriccion",
   "label": "Vencimiento mínimo de capital",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Las financiaciones no tengan vencimientos de capital y/o intereses hasta que hayan transcurrido 240 días corridos desde el registro de ingreso aduanero de los b…"
  },
  {
   "id": "Obligacion_la_ccp_la_entidad_financiera_la_autoridad_de_control_de_la_ccp_u_otro_organismo_",
   "type": "Obligacion",
   "label": "Calcular requerimiento capital",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La CCP, la entidad financiera, la autoridad de control de la CCP u otro organismo con acceso a los datos requeridos deberá calcular K_CMi, DF_pref y DF_CCP de f…"
  },
  {
   "id": "Operacion_calculo_de_requerimiento_regulatorio",
   "type": "Operacion",
   "label": "Determinación de capital mínimo",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Determinación del cumplimiento de la exigencia de capital mínimo en función de la responsabilidad patrimonial computable"
  },
  {
   "id": "Operacion_mantenimiento_de_capital_minimo",
   "type": "Operacion",
   "label": "Mantenimiento de capital mínimo",
   "tokens_matcheados": 3,
   "resumen_propiedades": "tipo: mantenimiento de capital mínimo"
  },
  {
   "id": "Operacion_calculo_de_exigencia_de_capital_minimo_por_riesgo_de_credito",
   "type": "Operacion",
   "label": "Cálculo exigencia capital mínimo",
   "tokens_matcheados": 3,
   "resumen_propiedades": "tipo: cálculo de exigencia de capital mínimo por riesgo de crédito"
  },
  {
   "id": "Restriccion_el_17_en_el_caso_de_entidades_del_grupo_b_del_promedio_de_los_ultimos_36_meses_a",
   "type": "Restriccion",
   "label": "Límite 17% grupo B capital mínimo",
   "tokens_matcheados": 3,
   "resumen_propiedades": "El 17% en el caso de entidades del grupo B del promedio de los últimos 36 meses –anteriores al mes a que corresponda la determinación de la exigencia– de la exi…"
  },
  {
   "id": "Restriccion_la_exigencia_determinada_a_traves_de_la_aplicacion_de_la_expresion_descripta_en_",
   "type": "Restriccion",
   "label": "Límite 20% grupo A capital mínimo",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La exigencia determinada a través de la aplicación de la expresión descripta en el punto 7.2. no podrá superar el 20% en el caso de entidades del grupo A del pr…"
  }
 ]
}
```

### paso 3 — buscar_nodos {"consulta": "régimen informativo capital mínimo total control", "limite": 10}

```json
{
 "consulta": "régimen informativo capital mínimo total control",
 "total_con_match": 318,
 "resultados": [
  {
   "id": "Restriccion_los_bancos_deberan_mantener_una_exigencia_basica_de_capital_minimo_de_5_000_mill",
   "type": "Restriccion",
   "label": "Exigencia básica bancos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Los bancos deberán mantener una exigencia básica de capital mínimo de 5.000 millones de pesos"
  },
  {
   "id": "Restriccion_cuando_el_total_de_participaciones_en_el_capital_de_entidades_financieras_empres",
   "type": "Restriccion",
   "label": "Límite tenencias capital 10%",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Cuando el total de participaciones en el capital de entidades financieras, empresas de servicios complementarios de la actividad financiera y compañías de segur…"
  },
  {
   "id": "Operacion_integracion_de_capital_minimo",
   "type": "Operacion",
   "label": "Integración de capital mínimo",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: integración de capital mínimo"
  },
  {
   "id": "Restriccion_vencimiento_minimo_de_capital",
   "type": "Restriccion",
   "label": "Vencimiento mínimo de capital",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Las financiaciones no tengan vencimientos de capital y/o intereses hasta que hayan transcurrido 240 días corridos desde el registro de ingreso aduanero de los b…"
  },
  {
   "id": "Obligacion_la_ccp_la_entidad_financiera_la_autoridad_de_control_de_la_ccp_u_otro_organismo_",
   "type": "Obligacion",
   "label": "Calcular requerimiento capital",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La CCP, la entidad financiera, la autoridad de control de la CCP u otro organismo con acceso a los datos requeridos deberá calcular K_CMi, DF_pref y DF_CCP de f…"
  },
  {
   "id": "Obligacion_las_entidades_deberan_consultar_en_el_apartado_regimen_informativo_sepaimpo_del_",
   "type": "Obligacion",
   "label": "Consultar situación del cliente",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Las entidades deberán consultar en el apartado 'Régimen Informativo SEPAIMPO' del sitio www3.bcra.gob.ar, si el cliente se encuentra en la situación de condena …"
  },
  {
   "id": "Operacion_calculo_de_requerimiento_regulatorio",
   "type": "Operacion",
   "label": "Determinación de capital mínimo",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Determinación del cumplimiento de la exigencia de capital mínimo en función de la responsabilidad patrimonial computable"
  },
  {
   "id": "Operacion_mantenimiento_de_capital_minimo",
   "type": "Operacion",
   "label": "Mantenimiento de capital mínimo",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: mantenimiento de capital mínimo"
  },
  {
   "id": "Operacion_calculo_de_exigencia_de_capital_minimo_por_riesgo_de_credito",
   "type": "Operacion",
   "label": "Cálculo exigencia capital mínimo",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: cálculo de exigencia de capital mínimo por riesgo de crédito"
  },
  {
   "id": "Operacion_presentacion_informativa_de_operaciones_cambiarias",
   "type": "Operacion",
   "label": "Validación en régimen informativo",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: presentación informativa de operaciones cambiarias"
  }
 ]
}
```

### paso 4 — buscar_nodos {"consulta": "caja de crédito cooperativa capital mínimo básico", "limite": 10}

```json
{
 "consulta": "caja de crédito cooperativa capital mínimo básico",
 "total_con_match": 2466,
 "resultados": [
  {
   "id": "EntidadFinanciera_caja_de_credito_cooperativa",
   "type": "EntidadFinanciera",
   "label": "Cajas de Crédito Cooperativas",
   "tokens_matcheados": 4,
   "resumen_propiedades": "categoria: caja de crédito cooperativa"
  },
  {
   "id": "Operacion_calculo_de_exigencia_de_capital_minimo_por_riesgo_de_credito",
   "type": "Operacion",
   "label": "Cálculo exigencia capital mínimo",
   "tokens_matcheados": 4,
   "resumen_propiedades": "tipo: cálculo de exigencia de capital mínimo por riesgo de crédito"
  },
  {
   "id": "Operacion_calculo_de_capital_minimo",
   "type": "Operacion",
   "label": "Cálculo de exigencia por riesgo de crédito",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Determinación de la exigencia de capital por riesgo de crédito conforme a la fórmula C_RC = (k x 0,08 x APR_c) + INC"
  },
  {
   "id": "EntidadFinanciera_caja_de_credito",
   "type": "EntidadFinanciera",
   "label": "Cajas de Crédito",
   "tokens_matcheados": 3,
   "resumen_propiedades": "categoria: caja de crédito"
  },
  {
   "id": "Restriccion_los_bancos_deberan_mantener_una_exigencia_basica_de_capital_minimo_de_5_000_mill",
   "type": "Restriccion",
   "label": "Exigencia básica bancos",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Los bancos deberán mantener una exigencia básica de capital mínimo de 5.000 millones de pesos"
  },
  {
   "id": "Operacion_integracion_de_capital_minimo",
   "type": "Operacion",
   "label": "Integración de capital mínimo",
   "tokens_matcheados": 3,
   "resumen_propiedades": "tipo: integración de capital mínimo"
  },
  {
   "id": "Restriccion_vencimiento_minimo_de_capital",
   "type": "Restriccion",
   "label": "Vencimiento mínimo de capital",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Las financiaciones no tengan vencimientos de capital y/o intereses hasta que hayan transcurrido 240 días corridos desde el registro de ingreso aduanero de los b…"
  },
  {
   "id": "Operacion_calculo_de_requerimiento_regulatorio",
   "type": "Operacion",
   "label": "Determinación de capital mínimo",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Determinación del cumplimiento de la exigencia de capital mínimo en función de la responsabilidad patrimonial computable"
  },
  {
   "id": "Operacion_mantenimiento_de_capital_minimo",
   "type": "Operacion",
   "label": "Mantenimiento de capital mínimo",
   "tokens_matcheados": 3,
   "resumen_propiedades": "tipo: mantenimiento de capital mínimo"
  },
  {
   "id": "Restriccion_el_17_en_el_caso_de_entidades_del_grupo_b_del_promedio_de_los_ultimos_36_meses_a",
   "type": "Restriccion",
   "label": "Límite 17% grupo B capital mínimo",
   "tokens_matcheados": 3,
   "resumen_propiedades": "El 17% en el caso de entidades del grupo B del promedio de los últimos 36 meses –anteriores al mes a que corresponda la determinación de la exigencia– de la exi…"
  }
 ]
}
```

### paso 5 — ver_nodo {"id": "Restriccion_los_bancos_deberan_mantener_una_exigencia_basica_de_capital_minimo_de_5_000_mill"}

```json
{
 "id": "Restriccion_los_bancos_deberan_mantener_una_exigencia_basica_de_capital_minimo_de_5_000_mill",
 "type": "Restriccion",
 "label": "Exigencia básica bancos",
 "properties": {
  "descripcion": "Los bancos deberán mantener una exigencia básica de capital mínimo de 5.000 millones de pesos",
  "tipo": "limite_cuantitativo",
  "umbral": "5.000 millones de pesos"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Punto 1.2. Exigencia básica."
  }
 ]
}
```

### paso 6 — ver_vecinos {"id": "Restriccion_los_bancos_deberan_mantener_una_exigencia_basica_de_capital_minimo_de_5_000_mill"}

```json
{
 "id": "Restriccion_los_bancos_deberan_mantener_una_exigencia_basica_de_capital_minimo_de_5_000_mill",
 "label": "Exigencia básica bancos",
 "n_salientes_total": 3,
 "n_entrantes_total": 1,
 "salientes": [
  {
   "relation": "establecida_en",
   "vecino_id": "TextoOrdenado_to_capitales_minimos_actual_pdf",
   "vecino_label": "Capitales Mínimos",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 1.2. Exigencia básica."
    }
   ]
  },
  {
   "relation": "aplica_a",
   "vecino_id": "EntidadFinanciera_banco",
   "vecino_label": "Bancos",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 1.2. Exigencia básica."
    }
   ]
  },
  {
   "relation": "limita",
   "vecino_id": "Operacion_mantenimiento_de_capital_minimo",
   "vecino_label": "Mantenimiento de capital mínimo",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 1.2. Exigencia básica."
    }
   ]
  }
 ],
 "salientes_truncado": false,
 "entrantes": [
  {
   "relation": "exceptua",
   "vecino_id": "Excepcion_las_cajas_de_credito_cooperativas_quedan_exceptuadas_de_la_exigencia_basica_de_5",
   "vecino_label": "Excepción Cajas de Crédito Cooperativas",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 1.2. Exigencia básica."
    }
   ]
  }
 ],
 "entrantes_truncado": false
}
```

### paso 7 — buscar_nodos {"consulta": "total de control importe consignar banco", "limite": 10}

```json
{
 "consulta": "total de control importe consignar banco",
 "total_con_match": 2426,
 "resultados": [
  {
   "id": "Obligacion_el_importe_del_capital_prestado_el_monto_total_a_pagar_la_cantidad_de_cuotas_per",
   "type": "Obligacion",
   "label": "Informar detalles de préstamos en cuotas",
   "tokens_matcheados": 3,
   "resumen_propiedades": "El importe del capital prestado, el monto total a pagar, la cantidad de cuotas, periodicidad y fecha de vencimiento, el sistema de amortización de capital y can…"
  },
  {
   "id": "Obligacion_debera_deducir_del_capital_ordinario_de_nivel_uno_con1_el_importe_total_en_conce",
   "type": "Obligacion",
   "label": "Deducción ganancia venta respaldo implícito",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Deberá deducir del capital ordinario de nivel uno (COn1) el importe total en concepto de ganancia por venta resultante de la operación de titulización, de acuer…"
  },
  {
   "id": "Restriccion_el_importe_de_co_debera_ser_resultante_de_multiplicar_4_5_por_los_apr",
   "type": "Restriccion",
   "label": "Límite mínimo CO",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El importe de CO deberá ser resultante de multiplicar 4,5% por los APR"
  },
  {
   "id": "Restriccion_el_importe_de_pnb_debera_ser_resultante_de_multiplicar_6_por_los_apr",
   "type": "Restriccion",
   "label": "Límite mínimo PNb",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El importe de PNb deberá ser resultante de multiplicar 6% por los APR"
  },
  {
   "id": "Restriccion_el_importe_de_rpc_debera_ser_resultante_de_multiplicar_8_por_los_apr",
   "type": "Restriccion",
   "label": "Límite mínimo RPC",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El importe de RPC deberá ser resultante de multiplicar 8% por los APR"
  },
  {
   "id": "Restriccion_el_importe_de_esta_rpc_que_sera_admisible_como_pnc_excluye_los_importes_reconoci",
   "type": "Restriccion",
   "label": "Exclusión de RPC en PNc",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El importe de esta RPC que será admisible como PNc excluye los importes reconocidos en el CO conforme a lo establecido en el punto 8.3.5.1. y los importes recon…"
  },
  {
   "id": "Obligacion_importe_determinado_mediante_la_suma_de_los_valores_obtenidos_luego_de_multiplic",
   "type": "Obligacion",
   "label": "Cálculo de exigencia DvP",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Importe determinado mediante la suma de los valores obtenidos luego de multiplicar la exposición actual positiva por la exigencia de capital aplicable estableci…"
  },
  {
   "id": "Restriccion_control_de_montos_en_exceso",
   "type": "Restriccion",
   "label": "Control de montos en exceso",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Cuando la utilización de los mecanismos del punto 7.9. redunde en un monto que exceda lo previsto en el presente punto, la entidad encargada del seguimiento deb…"
  },
  {
   "id": "Restriccion_el_monto_maximo_sera_el_menor_entre_el_aumento_total_y_el_equivalente_al_30_del_",
   "type": "Restriccion",
   "label": "Límite de 30% del valor FOB",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El monto máximo será el menor entre el aumento total y el equivalente al 30% del valor FOB de las exportaciones computables para el año t-1"
  },
  {
   "id": "Operacion_control",
   "type": "Operacion",
   "label": "Control de montos facturados",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Controlar que el monto de los pagos y otros movimientos registrados con imputación al despacho no supere el monto facturado según la condición de compra pactada…"
  }
 ]
}
```

### paso 8 — buscar_nodos {"consulta": "5000 millones pesos capital mínimo básico", "limite": 10}

```json
{
 "consulta": "5000 millones pesos capital mínimo básico",
 "total_con_match": 279,
 "resultados": [
  {
   "id": "Restriccion_los_bancos_deberan_mantener_una_exigencia_basica_de_capital_minimo_de_5_000_mill",
   "type": "Restriccion",
   "label": "Exigencia básica bancos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Los bancos deberán mantener una exigencia básica de capital mínimo de 5.000 millones de pesos"
  },
  {
   "id": "Operacion_integracion_de_capital_minimo",
   "type": "Operacion",
   "label": "Integración de capital mínimo",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: integración de capital mínimo"
  },
  {
   "id": "Restriccion_vencimiento_minimo_de_capital",
   "type": "Restriccion",
   "label": "Vencimiento mínimo de capital",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Las financiaciones no tengan vencimientos de capital y/o intereses hasta que hayan transcurrido 240 días corridos desde el registro de ingreso aduanero de los b…"
  },
  {
   "id": "Operacion_calculo_de_requerimiento_regulatorio",
   "type": "Operacion",
   "label": "Determinación de capital mínimo",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Determinación del cumplimiento de la exigencia de capital mínimo en función de la responsabilidad patrimonial computable"
  },
  {
   "id": "Operacion_mantenimiento_de_capital_minimo",
   "type": "Operacion",
   "label": "Mantenimiento de capital mínimo",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: mantenimiento de capital mínimo"
  },
  {
   "id": "Operacion_calculo_de_exigencia_de_capital_minimo_por_riesgo_de_credito",
   "type": "Operacion",
   "label": "Cálculo exigencia capital mínimo",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: cálculo de exigencia de capital mínimo por riesgo de crédito"
  },
  {
   "id": "Restriccion_capital_minimo_riesgo_tipo_cambio",
   "type": "Restriccion",
   "label": "Capital mínimo riesgo tipo cambio",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La exigencia de capital será el 8% de la posición neta total"
  },
  {
   "id": "Restriccion_el_17_en_el_caso_de_entidades_del_grupo_b_del_promedio_de_los_ultimos_36_meses_a",
   "type": "Restriccion",
   "label": "Límite 17% grupo B capital mínimo",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El 17% en el caso de entidades del grupo B del promedio de los últimos 36 meses –anteriores al mes a que corresponda la determinación de la exigencia– de la exi…"
  },
  {
   "id": "Restriccion_la_exigencia_determinada_a_traves_de_la_aplicacion_de_la_expresion_descripta_en_",
   "type": "Restriccion",
   "label": "Límite 20% grupo A capital mínimo",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La exigencia determinada a través de la aplicación de la expresión descripta en el punto 7.2. no podrá superar el 20% en el caso de entidades del grupo A del pr…"
  },
  {
   "id": "Restriccion_el_resto_del_capital_que_vencia_fue_como_minimo_refinanciado_con_un_nuevo_endeud",
   "type": "Restriccion",
   "label": "Refinanciación vida promedio mínima",
   "tokens_matcheados": 2,
   "resumen_propiedades": "el resto del capital que vencía fue, como mínimo, refinanciado con un nuevo endeudamiento con el exterior con una vida promedio de 2 (dos) años mayor a la vida …"
  }
 ]
}
```

### paso 9 — buscar_nodos {"consulta": "total control reporte información capital", "limite": 10}

```json
{
 "consulta": "total control reporte información capital",
 "total_con_match": 312,
 "resultados": [
  {
   "id": "Restriccion_cuando_el_total_de_participaciones_en_el_capital_de_entidades_financieras_empres",
   "type": "Restriccion",
   "label": "Límite tenencias capital 10%",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Cuando el total de participaciones en el capital de entidades financieras, empresas de servicios complementarios de la actividad financiera y compañías de segur…"
  },
  {
   "id": "Obligacion_la_ccp_la_entidad_financiera_la_autoridad_de_control_de_la_ccp_u_otro_organismo_",
   "type": "Obligacion",
   "label": "Calcular requerimiento capital",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La CCP, la entidad financiera, la autoridad de control de la CCP u otro organismo con acceso a los datos requeridos deberá calcular K_CMi, DF_pref y DF_CCP de f…"
  },
  {
   "id": "Restriccion_total_de_participaciones_en_el_capital_de_empresas_60",
   "type": "Restriccion",
   "label": "Límite de participaciones totales",
   "tokens_matcheados": 2,
   "resumen_propiedades": "total de participaciones en el capital de empresas: 60%"
  },
  {
   "id": "Obligacion_el_importe_del_capital_prestado_el_monto_total_a_pagar_la_cantidad_de_cuotas_per",
   "type": "Obligacion",
   "label": "Informar detalles de préstamos en cuotas",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El importe del capital prestado, el monto total a pagar, la cantidad de cuotas, periodicidad y fecha de vencimiento, el sistema de amortización de capital y can…"
  },
  {
   "id": "Obligacion_se_debera_evaluar_si_los_sistemas_de_informacion_y_las_funciones_de_reporte_son_",
   "type": "Obligacion",
   "label": "Evaluar sistemas de información y reporte",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Se deberá evaluar si los sistemas de información y las funciones de reporte son adecuados, pudiéndose basar en revisiones de terceros independientes en el caso …"
  },
  {
   "id": "Obligacion_debera_deducir_del_capital_ordinario_de_nivel_uno_con1_el_importe_total_en_conce",
   "type": "Obligacion",
   "label": "Deducción ganancia venta respaldo implícito",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Deberá deducir del capital ordinario de nivel uno (COn1) el importe total en concepto de ganancia por venta resultante de la operación de titulización, de acuer…"
  },
  {
   "id": "Obligacion_la_ccp_debera_brindar_la_informacion_necesaria_para_el_computo_de_la_exigencia_d",
   "type": "Obligacion",
   "label": "Brindar información para cómputo de capital",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La CCP deberá brindar la información necesaria para el cómputo de la exigencia de capital por riesgo de crédito de contraparte por la exposición de las entidade…"
  },
  {
   "id": "Restriccion_total_de_participaciones_en_capital_de_empresas_no_podra_exceder_el_60",
   "type": "Restriccion",
   "label": "Límite total de participaciones en empresas",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Total de participaciones en capital de empresas no podrá exceder el 60%"
  },
  {
   "id": "Obligacion_calcular_exigencia_total_capital_riesgo_vega",
   "type": "Obligacion",
   "label": "Calcular exigencia total capital riesgo vega",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La exigencia total de capital por riesgo vega será la suma del valor absoluto de las exigencias de capital individual que se hayan calculado para dicho riesgo"
  },
  {
   "id": "Obligacion_al_calcular_la_exigencia_maxima_de_capital_se_deducira_el_total_de_las_ganancias",
   "type": "Obligacion",
   "label": "Deducir ganancias ventas y cupones crediticia",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Al calcular la exigencia máxima de capital, se deducirá el total de las ganancias por ventas y cupones de mejora crediticia relacionadas con la titulización"
  }
 ]
}
```

### paso 10 — buscar_nodos {"consulta": "importe consignar banco no caja crédito cooperativa", "limite": 10}

```json
{
 "consulta": "importe consignar banco no caja crédito cooperativa",
 "total_con_match": 516,
 "resultados": [
  {
   "id": "EntidadFinanciera_caja_de_credito_cooperativa",
   "type": "EntidadFinanciera",
   "label": "Cajas de Crédito Cooperativas",
   "tokens_matcheados": 3,
   "resumen_propiedades": "categoria: caja de crédito cooperativa"
  },
  {
   "id": "EntidadFinanciera_caja_de_credito",
   "type": "EntidadFinanciera",
   "label": "Cajas de Crédito",
   "tokens_matcheados": 2,
   "resumen_propiedades": "categoria: caja de crédito"
  },
  {
   "id": "Restriccion_la_exposicion_presente_respecto_de_la_contraparte_no_puede_tener_un_valor_negati",
   "type": "Restriccion",
   "label": "Crédito de riesgo no negativo",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La exposición presente respecto de la contraparte no puede tener un valor negativo"
  },
  {
   "id": "Restriccion_financiaciones_que_no_superen_el_importe_resultante_de_aplicar_sobre_el_saldo_de",
   "type": "Restriccion",
   "label": "Límite monto financiación nueva",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Financiaciones que no superen el importe resultante de aplicar sobre el saldo de deuda registrado en el sistema financiero el porcentaje establecido en punto 2.…"
  },
  {
   "id": "Obligacion_consignar_importe_patrimonio_neto",
   "type": "Obligacion",
   "label": "Consignar importe patrimonio neto",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Se consignará el importe total del Patrimonio Neto (rubro 400000 del balance), excluyendo las acciones con preferencia patrimonial y la reserva especial para in…"
  },
  {
   "id": "Restriccion_el_periodo_de_vigencia_del_derivado_de_credito_no_podra_ser_inferior_a_cualquier",
   "type": "Restriccion",
   "label": "Período mínimo de vigencia derivados",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El período de vigencia del derivado de crédito no podrá ser inferior a cualquier período de gracia necesario para poder determinar que efectivamente se ha produ…"
  },
  {
   "id": "EntidadFinanciera_proveedor_no_financiero_de_credito",
   "type": "EntidadFinanciera",
   "label": "Proveedores no financieros de crédito",
   "tokens_matcheados": 2,
   "resumen_propiedades": "categoria: proveedor no financiero de crédito"
  },
  {
   "id": "Restriccion_titulos_de_credito_titulos_valores_certificados_de_depositos_a_plazo_fijo_y_otro",
   "type": "Restriccion",
   "label": "Deducción títulos no en poder entidad",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Títulos de crédito (títulos valores, certificados de depósitos a plazo fijo y otros) que físicamente no se encuentren en poder de la entidad, salvo que su regis…"
  },
  {
   "id": "Restriccion_el_importe_de_los_depositos_en_moneda_nacional_y_extranjera_no_podra_exceder_del",
   "type": "Restriccion",
   "label": "Límite de depósitos por incumplimiento",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El importe de los depósitos –en moneda nacional y extranjera– no podrá exceder del nivel que haya alcanzado durante el mes en que se originó el incumplimiento"
  },
  {
   "id": "Restriccion_el_importe_de_los_cargos_que_el_sujeto_obligado_transfiera_a_los_usuarios_no_pod",
   "type": "Restriccion",
   "label": "Cargos no superiores a costo de terceros",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El importe de los cargos que el sujeto obligado transfiera a los usuarios no podrá ser superior al que el tercero prestador perciba de particulares, sin interme…"
  }
 ]
}
```

### paso 11 — ver_nodo {"id": "Obligacion_consignar_importe_patrimonio_neto"}

```json
{
 "id": "Obligacion_consignar_importe_patrimonio_neto",
 "type": "Obligacion",
 "label": "Consignar importe patrimonio neto",
 "properties": {
  "tipo": "presentacion_informativa",
  "description": "Se consignará el importe total del Patrimonio Neto (rubro 400000 del balance), excluyendo las acciones con preferencia patrimonial y la reserva especial para instrumentos de deuda."
 },
 "provenances": [
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Punto 6.1. Normas de procedimiento (parte 1)"
  }
 ]
}
```

### paso 12 — ver_vecinos {"id": "Obligacion_consignar_importe_patrimonio_neto"}

```json
{
 "id": "Obligacion_consignar_importe_patrimonio_neto",
 "label": "Consignar importe patrimonio neto",
 "n_salientes_total": 3,
 "n_entrantes_total": 0,
 "salientes": [
  {
   "relation": "establecida_en",
   "vecino_id": "TextoOrdenado_to_regimen_informativo_contable_mensual_actual_pdf",
   "vecino_label": "Régimen Informativo Contable Mensual",
   "provenances": [
    {
     "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
     "location": "Punto 6.1. Normas de procedimiento (parte 1)"
    }
   ]
  },
  {
   "relation": "aplica_a",
   "vecino_id": "EntidadFinanciera_sujeto_obligado",
   "vecino_label": "Sujetos obligados",
   "provenances": [
    {
     "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
     "location": "Punto 6.1. Normas de procedimiento (parte 1)"
    }
   ]
  },
  {
   "relation": "regula",
   "vecino_id": "Operacion_calculo",
   "vecino_label": "Cálculo exigencia capital riesgo operacional",
   "provenances": [
    {
     "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
     "location": "Punto 6.1. Normas de procedimiento (parte 1)"
    }
   ]
  }
 ],
 "salientes_truncado": false,
 "entrantes": [],
 "entrantes_truncado": false
}
```

### paso 13 — buscar_nodos {"consulta": "total de control capital mínimo básico banco", "limite": 15}

```json
{
 "consulta": "total de control capital mínimo básico banco",
 "total_con_match": 2470,
 "resultados": [
  {
   "id": "Restriccion_los_bancos_deberan_mantener_una_exigencia_basica_de_capital_minimo_de_5_000_mill",
   "type": "Restriccion",
   "label": "Exigencia básica bancos",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Los bancos deberán mantener una exigencia básica de capital mínimo de 5.000 millones de pesos"
  },
  {
   "id": "Restriccion_cuando_el_total_de_participaciones_en_el_capital_de_entidades_financieras_empres",
   "type": "Restriccion",
   "label": "Límite tenencias capital 10%",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Cuando el total de participaciones en el capital de entidades financieras, empresas de servicios complementarios de la actividad financiera y compañías de segur…"
  },
  {
   "id": "Operacion_integracion_de_capital_minimo",
   "type": "Operacion",
   "label": "Integración de capital mínimo",
   "tokens_matcheados": 3,
   "resumen_propiedades": "tipo: integración de capital mínimo"
  },
  {
   "id": "Restriccion_vencimiento_minimo_de_capital",
   "type": "Restriccion",
   "label": "Vencimiento mínimo de capital",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Las financiaciones no tengan vencimientos de capital y/o intereses hasta que hayan transcurrido 240 días corridos desde el registro de ingreso aduanero de los b…"
  },
  {
   "id": "Obligacion_la_ccp_la_entidad_financiera_la_autoridad_de_control_de_la_ccp_u_otro_organismo_",
   "type": "Obligacion",
   "label": "Calcular requerimiento capital",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La CCP, la entidad financiera, la autoridad de control de la CCP u otro organismo con acceso a los datos requeridos deberá calcular K_CMi, DF_pref y DF_CCP de f…"
  },
  {
   "id": "Operacion_calculo_de_requerimiento_regulatorio",
   "type": "Operacion",
   "label": "Determinación de capital mínimo",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Determinación del cumplimiento de la exigencia de capital mínimo en función de la responsabilidad patrimonial computable"
  },
  {
   "id": "Operacion_mantenimiento_de_capital_minimo",
   "type": "Operacion",
   "label": "Mantenimiento de capital mínimo",
   "tokens_matcheados": 3,
   "resumen_propiedades": "tipo: mantenimiento de capital mínimo"
  },
  {
   "id": "Operacion_calculo_de_exigencia_de_capital_minimo_por_riesgo_de_credito",
   "type": "Operacion",
   "label": "Cálculo exigencia capital mínimo",
   "tokens_matcheados": 3,
   "resumen_propiedades": "tipo: cálculo de exigencia de capital mínimo por riesgo de crédito"
  },
  {
   "id": "Restriccion_el_17_en_el_caso_de_entidades_del_grupo_b_del_promedio_de_los_ultimos_36_meses_a",
   "type": "Restriccion",
   "label": "Límite 17% grupo B capital mínimo",
   "tokens_matcheados": 3,
   "resumen_propiedades": "El 17% en el caso de entidades del grupo B del promedio de los últimos 36 meses –anteriores al mes a que corresponda la determinación de la exigencia– de la exi…"
  },
  {
   "id": "Restriccion_la_exigencia_determinada_a_traves_de_la_aplicacion_de_la_expresion_descripta_en_",
   "type": "Restriccion",
   "label": "Límite 20% grupo A capital mínimo",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La exigencia determinada a través de la aplicación de la expresión descripta en el punto 7.2. no podrá superar el 20% en el caso de entidades del grupo A del pr…"
  },
  {
   "id": "Restriccion_total_de_participaciones_en_el_capital_de_empresas_60",
   "type": "Restriccion",
   "label": "Límite de participaciones totales",
   "tokens_matcheados": 3,
   "resumen_propiedades": "total de participaciones en el capital de empresas: 60%"
  },
  {
   "id": "Restriccion_las_acreencias_en_conjunto_deben_representar_el_40_o_mas_del_total_informado_por",
   "type": "Restriccion",
   "label": "Umbral mínimo de 40% en acreencias",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Las acreencias de al menos dos entidades u otros acreedores deben representar el 40 % o más del total informado por todos los acreedores según la última informa…"
  },
  {
   "id": "Restriccion_las_restantes_entidades_deberan_mantener_una_exigencia_basica_de_capital_minimo_",
   "type": "Restriccion",
   "label": "Exigencia básica restantes entidades",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Las restantes entidades deberán mantener una exigencia básica de capital mínimo de 2.500 millones de pesos"
  },
  {
   "id": "Operacion_cumplimiento_de_capital",
   "type": "Operacion",
   "label": "Cumplimiento integración capital mínimo",
   "tokens_matcheados": 3,
   "resumen_propiedades": "tipo: cumplimiento de capital"
  },
  {
   "id": "Restriccion_capital_ordinario_de_nivel_1_con1_70210000_70220000_4_5_s_70900000",
   "type": "Restriccion",
   "label": "Límite mínimo Capital Ordinario Nivel 1",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Capital Ordinario de Nivel 1 (COn1) = 70210000 – 70220000 ≥ 4,5 % s/70900000"
  }
 ]
}
```

### paso 14 — buscar_nodos {"consulta": "total control 5000 millones", "limite": 10}

```json
{
 "consulta": "total control 5000 millones",
 "total_con_match": 45,
 "resultados": [
  {
   "id": "Operacion_cobertura_crediticia_total_o_proporcional",
   "type": "Operacion",
   "label": "Cobertura crediticia total",
   "tokens_matcheados": 1,
   "resumen_propiedades": "tipo: cobertura crediticia total o proporcional"
  },
  {
   "id": "Restriccion_control_de_montos_en_exceso",
   "type": "Restriccion",
   "label": "Control de montos en exceso",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Cuando la utilización de los mecanismos del punto 7.9. redunde en un monto que exceda lo previsto en el presente punto, la entidad encargada del seguimiento deb…"
  },
  {
   "id": "Restriccion_el_monto_maximo_sera_el_menor_entre_el_aumento_total_y_el_equivalente_al_30_del_",
   "type": "Restriccion",
   "label": "Límite de 30% del valor FOB",
   "tokens_matcheados": 1,
   "resumen_propiedades": "El monto máximo será el menor entre el aumento total y el equivalente al 30% del valor FOB de las exportaciones computables para el año t-1"
  },
  {
   "id": "Operacion_control",
   "type": "Operacion",
   "label": "Control de montos facturados",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Controlar que el monto de los pagos y otros movimientos registrados con imputación al despacho no supere el monto facturado según la condición de compra pactada…"
  },
  {
   "id": "Restriccion_cuando_el_total_de_participaciones_en_el_capital_de_entidades_financieras_empres",
   "type": "Restriccion",
   "label": "Límite tenencias capital 10%",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Cuando el total de participaciones en el capital de entidades financieras, empresas de servicios complementarios de la actividad financiera y compañías de segur…"
  },
  {
   "id": "Obligacion_la_ccp_la_entidad_financiera_la_autoridad_de_control_de_la_ccp_u_otro_organismo_",
   "type": "Obligacion",
   "label": "Calcular requerimiento capital",
   "tokens_matcheados": 1,
   "resumen_propiedades": "La CCP, la entidad financiera, la autoridad de control de la CCP u otro organismo con acceso a los datos requeridos deberá calcular K_CMi, DF_pref y DF_CCP de f…"
  },
  {
   "id": "Obligacion_la_entidad_nominada_podra_emitir_una_certificacion_cuando_se_verifiquen_la_total",
   "type": "Obligacion",
   "label": "Verificar requisitos para emisión",
   "tokens_matcheados": 1,
   "resumen_propiedades": "La entidad nominada podrá emitir una Certificación cuando se verifiquen la totalidad de los siguientes requisitos"
  },
  {
   "id": "Obligacion_la_exposicion_total_sera_el_monto_bruto_sin_computar_las_coberturas_del_riesgo_d",
   "type": "Obligacion",
   "label": "Cálculo de exposición total bruta",
   "tokens_matcheados": 1,
   "resumen_propiedades": "La exposición total será el monto bruto –sin computar las coberturas del riesgo de crédito de la Sección 5.– de las exposiciones minoristas con la contraparte."
  },
  {
   "id": "Restriccion_total_de_participaciones_en_el_capital_de_empresas_60",
   "type": "Restriccion",
   "label": "Límite de participaciones totales",
   "tokens_matcheados": 1,
   "resumen_propiedades": "total de participaciones en el capital de empresas: 60%"
  },
  {
   "id": "Restriccion_las_acreencias_en_conjunto_deben_representar_el_40_o_mas_del_total_informado_por",
   "type": "Restriccion",
   "label": "Umbral mínimo de 40% en acreencias",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Las acreencias de al menos dos entidades u otros acreedores deben representar el 40 % o más del total informado por todos los acreedores según la última informa…"
  }
 ]
}
```

### paso 15 — buscar_nodos {"consulta": "consignar total control exigencia capital", "limite": 10}

```json
{
 "consulta": "consignar total control exigencia capital",
 "total_con_match": 297,
 "resultados": [
  {
   "id": "Obligacion_calcular_exigencia_total_capital_riesgo_vega",
   "type": "Obligacion",
   "label": "Calcular exigencia total capital riesgo vega",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La exigencia total de capital por riesgo vega será la suma del valor absoluto de las exigencias de capital individual que se hayan calculado para dicho riesgo"
  },
  {
   "id": "Obligacion_al_calcular_la_exigencia_maxima_de_capital_se_deducira_el_total_de_las_ganancias",
   "type": "Obligacion",
   "label": "Deducir ganancias ventas y cupones crediticia",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Al calcular la exigencia máxima de capital, se deducirá el total de las ganancias por ventas y cupones de mejora crediticia relacionadas con la titulización"
  },
  {
   "id": "Restriccion_los_bancos_deberan_mantener_una_exigencia_basica_de_capital_minimo_de_5_000_mill",
   "type": "Restriccion",
   "label": "Exigencia básica bancos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Los bancos deberán mantener una exigencia básica de capital mínimo de 5.000 millones de pesos"
  },
  {
   "id": "Obligacion_se_determinara_mensualmente_la_exigencia_de_capital_por_riesgo_operacional_cro_m",
   "type": "Obligacion",
   "label": "Informar CRO mensualmente",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Se determinará mensualmente la exigencia de capital por riesgo operacional (CRO) mediante la expresión CRO = BIC x ILM para entidades del Grupo 1"
  },
  {
   "id": "Restriccion_cuando_el_total_de_participaciones_en_el_capital_de_entidades_financieras_empres",
   "type": "Restriccion",
   "label": "Límite tenencias capital 10%",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Cuando el total de participaciones en el capital de entidades financieras, empresas de servicios complementarios de la actividad financiera y compañías de segur…"
  },
  {
   "id": "Obligacion_aplicar_exigencia_capital_por_riesgo_general_mercado_a_todas_posiciones_derivado",
   "type": "Obligacion",
   "label": "Cálculo riesgo general mercado",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La exigencia de capital por el riesgo general de mercado alcanza a todas las posiciones en instrumentos derivados -de la misma manera que también alcanza a las …"
  },
  {
   "id": "Obligacion_la_ccp_la_entidad_financiera_la_autoridad_de_control_de_la_ccp_u_otro_organismo_",
   "type": "Obligacion",
   "label": "Calcular requerimiento capital",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La CCP, la entidad financiera, la autoridad de control de la CCP u otro organismo con acceso a los datos requeridos deberá calcular K_CMi, DF_pref y DF_CCP de f…"
  },
  {
   "id": "Obligacion_observar_exigencia_capital_cva",
   "type": "Obligacion",
   "label": "Observar exigencia capital CVA",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Las entidades financieras deberán observar una exigencia de capital por el riesgo de pérdidas derivadas de valuar a precios de mercado el riesgo de contraparte …"
  },
  {
   "id": "Operacion_calculo_de_capital",
   "type": "Operacion",
   "label": "Cálculo de exigencia de capital",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Cálculo de las exigencias de capital para posiciones de titulización utilizando el enfoque estandarizado"
  },
  {
   "id": "Operacion_calculo_de_exigencia",
   "type": "Operacion",
   "label": "Cálculo de exigencia de capital",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Cálculo del importe correspondiente al mes n considerando exigencia de riesgo de crédito, riesgo de mercado, riesgo operacional, responsabilidad patrimonial com…"
  }
 ]
}
```



---

# CQN-010

## Respuesta final íntegra (trace.final_json)

```json
{
 "respuesta": "Según la regulación del BCRA, cuando las divisas del cobro de una exportación se aplican a cancelar una prefinanciación, la entidad encargada del seguimiento del permiso de embarque necesita un certificado de aplicación para registrar esa imputación. La entidad financiera encargada del seguimiento es la única habilitada para emitir estos certificados de aplicación que habilitan que los cobros de exportaciones puedan ser imputados a los permisos correspondientes.",
 "citas": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 7.10. 9.1.7. Aportes de inversión extranjera directa admitidos en los puntos 7.9. o 7."
  }
 ],
 "respondible": true
}
```

(`respondible`: true · tool_calls_used: 15 · hit_tool_limit: True)

## Inventario de pasos + fidelidad runtime↔re-ejecución

| paso | tool | input | output_chars (runtime) | re-ejecutado | fiel |
|---|---|---|---|---|---|
| 1 | buscar_nodos | `{"consulta": "divisas cobro exportación prefinanciación", "limite": 10}` | 2842 | 2842 | SÍ |
| 2 | buscar_nodos | `{"consulta": "permiso embarque seguimiento imputación", "limite": 10}` | 3317 | 3317 | SÍ |
| 3 | buscar_nodos | `{"consulta": "cancelar prefinanciación divisas", "limite": 10}` | 3285 | 3285 | SÍ |
| 4 | ver_nodo | `{"id": "Operacion_imputacion_de_ingresos_de_divisas"}` | 357 | 357 | SÍ |
| 5 | buscar_nodos | `{"consulta": "certificado BCRA imputación divisas prefinanciación", "limite": 10}` | 2726 | 2726 | SÍ |
| 6 | buscar_nodos | `{"consulta": "certificado divisas cobro exportación imputación", "limite": 10}` | 2817 | 2817 | SÍ |
| 7 | buscar_nodos | `{"consulta": "documento imputación seguimiento embarque divisas", "limite": 10}` | 3286 | 3286 | SÍ |
| 8 | buscar_nodos | `{"consulta": "Certificado DECRETO 929/13", "limite": 10}` | 3408 | 3408 | SÍ |
| 9 | ver_vecinos | `{"id": "Operacion_seguimiento_de_permiso_de_embarque", "direccion": "ambas"}` | 556 | 556 | SÍ |
| 10 | ver_nodo | `{"id": "Operacion_emision_de_certificado"}` | 533 | 533 | SÍ |
| 11 | ver_vecinos | `{"id": "Operacion_emision_de_certificado", "direccion": "ambas"}` | 894 | 894 | SÍ |
| 12 | ver_nodo | `{"id": "Obligacion_la_entidad_sera_la_unica_responsable_de_emitir_los_certificados_de_apli` | 591 | 591 | SÍ |
| 13 | buscar_nodos | `{"consulta": "certificado aplicación cobro exportación prefinanciación", "limite": 10}` | 2716 | 2716 | SÍ |
| 14 | buscar_nodos | `{"consulta": "boleto venta divisas prefinanciación imputación", "limite": 10}` | 3403 | 3403 | SÍ |
| 15 | buscar_nodos | `{"consulta": "entidad encargada seguimiento permiso embarque registrar imputación", "limit` | 3598 | 3598 | SÍ |

**Fidelidad: 15/15** (igualdad de largos del output completo).

## Apéndice — outputs completos re-ejecutados

### paso 1 — buscar_nodos {"consulta": "divisas cobro exportación prefinanciación", "limite": 10}

```json
{
 "consulta": "divisas cobro exportación prefinanciación",
 "total_con_match": 168,
 "resultados": [
  {
   "id": "Operacion_cobro_local_por_exportacion_de_ranchos_a_medios_de_transporte_de_bandera_extranj",
   "type": "Operacion",
   "label": "Cobro local de exportación",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: cobro local por exportación de ranchos a medios de transporte de bandera extranjera"
  },
  {
   "id": "Operacion_prefinanciacion",
   "type": "Operacion",
   "label": "Prefinanciación de exportación",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Prefinanciaciones y financiaciones de exportaciones pendientes al 31/08/19 que fueron otorgadas o garantizadas por entidades financieras locales"
  },
  {
   "id": "Obligacion_el_contravalor_en_divisas_de_la_exportacion_hasta_alcanzar_el_valor_facturado_de",
   "type": "Obligacion",
   "label": "Ingreso y liquidación en plazos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El contravalor en divisas de la exportación hasta alcanzar el valor facturado deberá ingresarse al país y liquidarse en el mercado de cambios en los plazos esta…"
  },
  {
   "id": "Operacion_cobro_anticipado",
   "type": "Operacion",
   "label": "Cobros anticipados de exportación",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: cobro anticipado"
  },
  {
   "id": "Operacion_cobro_de_exportacion",
   "type": "Operacion",
   "label": "Cobros de exportaciones de bienes",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Cobros de exportaciones de bienes"
  },
  {
   "id": "Operacion_ingreso_de_divisas_por_exportacion_de_bienes",
   "type": "Operacion",
   "label": "Ingreso de divisas de exportación",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: ingreso de divisas por exportación de bienes"
  },
  {
   "id": "Operacion_cobro_de_exportacion_percibido_luego_del_embarque_no_liquidado",
   "type": "Operacion",
   "label": "Cobro de exportación post-embarque",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: cobro de exportación percibido luego del embarque no liquidado"
  },
  {
   "id": "Operacion_anticipo_y_cobro_de_exportacion",
   "type": "Operacion",
   "label": "Anticipos y cobros de exportaciones",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Anticipos y cobros de exportaciones argentinas de bienes y servicios conexos documentadas en pesos argentinos"
  },
  {
   "id": "Operacion_cobro_de_exportacion_de_servicios",
   "type": "Operacion",
   "label": "Cobro de exportaciones de servicios",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Cobros por la prestación de servicios por parte de residentes a no residentes"
  },
  {
   "id": "Restriccion_el_contravalor_de_la_exportacion_de_bienes_y_servicios_debera_ingresarse_al_pais",
   "type": "Restriccion",
   "label": "Obligatoriedad de ingreso en divisas",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El contravalor de la exportación de bienes y servicios deberá ingresarse al país en divisas o negociarse en el mercado de cambios"
  }
 ]
}
```

### paso 2 — buscar_nodos {"consulta": "permiso embarque seguimiento imputación", "limite": 10}

```json
{
 "consulta": "permiso embarque seguimiento imputación",
 "total_con_match": 101,
 "resultados": [
  {
   "id": "Operacion_seguimiento_de_permiso_de_embarque",
   "type": "Operacion",
   "label": "Seguimiento permiso de embarque",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Seguimiento de un permiso de embarque por la parte amparada por un Certificado DECRETO 929/13"
  },
  {
   "id": "Excepcion_la_entidad_encargada_del_seguimiento_del_permiso_de_embarque_podra_extender_el_p",
   "type": "Excepcion",
   "label": "Prórroga de plazo de liquidación",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La entidad encargada del seguimiento del permiso de embarque podrá extender el plazo de liquidación cuando el cliente haya utilizado el mecanismo de acumulación…"
  },
  {
   "id": "Restriccion_la_entidad_podra_considerar_cumplimentado_el_seguimiento_de_un_permiso_de_embarq",
   "type": "Restriccion",
   "label": "Límite de imputación por porcentaje de facturación",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La entidad podrá considerar cumplimentado el seguimiento de un permiso de embarque por el equivalente de hasta el 25% (veinticinco por ciento) del valor factura…"
  },
  {
   "id": "Operacion_solicitud_de_cumplimentacion_de_seguimiento_de_permiso_de_embarque",
   "type": "Operacion",
   "label": "Solicitud cumplimentación seguimiento permiso embarque",
   "tokens_matcheados": 3,
   "resumen_propiedades": "tipo: solicitud de cumplimentación de seguimiento de permiso de embarque"
  },
  {
   "id": "Obligacion_la_entidad_encargada_del_seguimiento_del_permiso_podra_conceder_extensiones_en_e",
   "type": "Obligacion",
   "label": "Conceder extensiones del plazo",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La entidad encargada del seguimiento del permiso podrá conceder extensiones en el plazo de ingreso y liquidación en las circunstancias especificadas"
  },
  {
   "id": "Obligacion_efectuar_el_seguimiento_de_los_permisos_de_embarques_cuyos_cobros_se_pretenda_ap",
   "type": "Obligacion",
   "label": "Seguimiento de permisos de embarque",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Efectuar el seguimiento de los permisos de embarques cuyos cobros se pretenda aplicar acorde a lo previsto en el presente punto"
  },
  {
   "id": "Operacion_rectificacion_de_datos",
   "type": "Operacion",
   "label": "Rectificación de permiso de embarque",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Si el exportador considera que existen errores en la forma en que un permiso de embarque ha sido reportado en el sistema SECOEXPO, deberá tramitar la correspond…"
  },
  {
   "id": "Obligacion_seguimiento_de_permiso_de_exportacion",
   "type": "Obligacion",
   "label": "Seguimiento de permiso de exportación",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La entidad encargada del seguimiento del permiso debe registrar y controlar las solicitudes de ampliación de plazo y el cumplimiento de los requisitos del mecan…"
  },
  {
   "id": "Operacion_designacion_de_entidad_nominada",
   "type": "Operacion",
   "label": "Designación para seguimiento de embarque",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Designación de una entidad por un exportador para el seguimiento de un permiso de embarque"
  },
  {
   "id": "Operacion_imputacion_de_ingresos_de_divisas",
   "type": "Operacion",
   "label": "Imputación al cumplimiento de seguimiento",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: imputación de ingresos de divisas"
  }
 ]
}
```

### paso 3 — buscar_nodos {"consulta": "cancelar prefinanciación divisas", "limite": 10}

```json
{
 "consulta": "cancelar prefinanciación divisas",
 "total_con_match": 82,
 "resultados": [
  {
   "id": "Operacion_venta_de_moneda_extranjera",
   "type": "Operacion",
   "label": "Venta de divisas",
   "tokens_matcheados": 1,
   "resumen_propiedades": "La venta de las divisas será cursada con débito en cuentas del cliente en entidades financieras locales por alguna de las modalidades de medios de pago vigentes"
  },
  {
   "id": "Operacion_ingreso_de_divisas",
   "type": "Operacion",
   "label": "Ingreso en divisas",
   "tokens_matcheados": 1,
   "resumen_propiedades": "El contravalor percibido deberá ingresarse en divisas"
  },
  {
   "id": "Operacion_liquidacion_de_divisas",
   "type": "Operacion",
   "label": "Liquidación de divisas",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Todas las liquidaciones de divisas en el mercado de cambios a partir del 02/09/19 que correspondan a cobros de anticipos, prefinanciaciones u otras financiacion…"
  },
  {
   "id": "Operacion_operacion_con_moneda_extranjera",
   "type": "Operacion",
   "label": "Liquidación de divisas",
   "tokens_matcheados": 1,
   "resumen_propiedades": "tipo: operación con moneda extranjera"
  },
  {
   "id": "Obligacion_la_venta_de_las_divisas_es_cursada_con_debito_en_cuentas_del_cliente_en_entidade",
   "type": "Obligacion",
   "label": "Débito en cuentas locales",
   "tokens_matcheados": 1,
   "resumen_propiedades": "La venta de las divisas es cursada con débito en cuentas del cliente en entidades financieras locales por alguna de las modalidades de medios de pago vigentes"
  },
  {
   "id": "Obligacion_corresponde_efectuar_un_boleto_de_venta_por_el_concepto_lineas_de_credito_del_ex",
   "type": "Obligacion",
   "label": "Registrar venta de divisas",
   "tokens_matcheados": 1,
   "resumen_propiedades": "corresponde efectuar un boleto de venta por el concepto 'Líneas de crédito del exterior' a nombre de la propia entidad en calidad de cliente"
  },
  {
   "id": "Obligacion_debera_reflejarse_como_una_compra_de_divisas_por_el_concepto_lineas_de_credito_d",
   "type": "Obligacion",
   "label": "Registrar compra de divisas",
   "tokens_matcheados": 1,
   "resumen_propiedades": "deberá reflejarse como una compra de divisas por el concepto 'Líneas de crédito del exterior' a nombre de la propia entidad en calidad de cliente"
  },
  {
   "id": "Obligacion_correspondera_registrar_boletos_simultaneos_de_compra_y_venta_de_divisas_a_nombr",
   "type": "Obligacion",
   "label": "Registrar boletos simultáneos",
   "tokens_matcheados": 1,
   "resumen_propiedades": "corresponderá registrar boletos simultáneos de compra y venta de divisas a nombre del cliente que recibe la financiación"
  },
  {
   "id": "Obligacion_cuando_al_menos_se_haya_cumplido_con_el_pago_sin_haber_incurrido_en_atrasos_supe",
   "type": "Obligacion",
   "label": "Cancelar intereses devengados",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Cuando al menos se haya cumplido con el pago, sin haber incurrido en atrasos superiores a 31 días, de la totalidad de los intereses devengados, podrá reclasific…"
  },
  {
   "id": "Obligacion_que_a_la_entidad_interviniente_le_conste_que_el_comprador_argentino_ha_liquidado",
   "type": "Obligacion",
   "label": "Verificar liquidación divisas",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Que a la entidad interviniente le conste que el comprador argentino ha liquidado divisas en el mercado de cambios asociadas a la venta de la mercadería por un m…"
  }
 ]
}
```

### paso 4 — ver_nodo {"id": "Operacion_imputacion_de_ingresos_de_divisas"}

```json
{
 "id": "Operacion_imputacion_de_ingresos_de_divisas",
 "type": "Operacion",
 "label": "Imputación al cumplimiento de seguimiento",
 "properties": {
  "tipo": "imputación de ingresos de divisas"
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 8.5. Otras imputaciones admitidas en el cumplimiento del seguimiento. (parte 3)"
  }
 ]
}
```

### paso 5 — buscar_nodos {"consulta": "certificado BCRA imputación divisas prefinanciación", "limite": 10}

```json
{
 "consulta": "certificado BCRA imputación divisas prefinanciación",
 "total_con_match": 186,
 "resultados": [
  {
   "id": "Operacion_imputacion_de_ingresos_de_divisas",
   "type": "Operacion",
   "label": "Imputación al cumplimiento de seguimiento",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: imputación de ingresos de divisas"
  },
  {
   "id": "Restriccion_limite_usd_25_000_para_imputacion_sin_divisas",
   "type": "Restriccion",
   "label": "Límite USD 25.000 para imputación sin divisas",
   "tokens_matcheados": 2,
   "resumen_propiedades": "En la medida que el monto a imputar al permiso por este mecanismo supere el equivalente a USD 25.000 (dólares estadounidenses veinticinco mil), la entidad deber…"
  },
  {
   "id": "Operacion_imputacion_de_exportacion_de_bienes_sin_contravalor_en_divisas",
   "type": "Operacion",
   "label": "Imputación exportación sin contravalor divisas",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: imputación de exportación de bienes sin contravalor en divisas"
  },
  {
   "id": "Operacion_imputacion_de_exportacion_con_bienes_importados_temporalmente_sin_uso_de_divisas",
   "type": "Operacion",
   "label": "Imputación exportación bienes importados temporalmente",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: imputación de exportación con bienes importados temporalmente sin uso de divisas"
  },
  {
   "id": "EntidadFinanciera_bcra",
   "type": "EntidadFinanciera",
   "label": "BCRA",
   "tokens_matcheados": 1,
   "resumen_propiedades": "categoria: banco central"
  },
  {
   "id": "Operacion_venta_de_moneda_extranjera",
   "type": "Operacion",
   "label": "Venta de divisas",
   "tokens_matcheados": 1,
   "resumen_propiedades": "La venta de las divisas será cursada con débito en cuentas del cliente en entidades financieras locales por alguna de las modalidades de medios de pago vigentes"
  },
  {
   "id": "Operacion_ingreso_de_divisas",
   "type": "Operacion",
   "label": "Ingreso en divisas",
   "tokens_matcheados": 1,
   "resumen_propiedades": "El contravalor percibido deberá ingresarse en divisas"
  },
  {
   "id": "Obligacion_supervision_del_bcra",
   "type": "Obligacion",
   "label": "Supervisión del BCRA",
   "tokens_matcheados": 1,
   "resumen_propiedades": "El Banco Central de la República Argentina (BCRA) supervisará la actuación de los sujetos obligados"
  },
  {
   "id": "Operacion_imputacion_de_credito_al_pagador",
   "type": "Operacion",
   "label": "Imputación de crédito",
   "tokens_matcheados": 1,
   "resumen_propiedades": "tipo: imputación de crédito al pagador"
  },
  {
   "id": "Obligacion_archivar_a_disposicion_del_bcra_toda_la_documentacion_utilizada_en_el_marco_del_",
   "type": "Obligacion",
   "label": "Archivar documentación",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Archivar a disposición del BCRA toda la documentación utilizada en el marco del seguimiento del pago realizado"
  }
 ]
}
```

### paso 6 — buscar_nodos {"consulta": "certificado divisas cobro exportación imputación", "limite": 10}

```json
{
 "consulta": "certificado divisas cobro exportación imputación",
 "total_con_match": 186,
 "resultados": [
  {
   "id": "Operacion_imputacion_de_gastos_bancarios_de_ejecucion_de_cobro",
   "type": "Operacion",
   "label": "Imputación gastos bancarios cobro exportación",
   "tokens_matcheados": 3,
   "resumen_propiedades": "tipo: imputación de gastos bancarios de ejecución de cobro"
  },
  {
   "id": "Operacion_imputacion_de_exportacion_de_bienes_sin_contravalor_en_divisas",
   "type": "Operacion",
   "label": "Imputación exportación sin contravalor divisas",
   "tokens_matcheados": 3,
   "resumen_propiedades": "tipo: imputación de exportación de bienes sin contravalor en divisas"
  },
  {
   "id": "Operacion_imputacion_de_exportacion_con_bienes_importados_temporalmente_sin_uso_de_divisas",
   "type": "Operacion",
   "label": "Imputación exportación bienes importados temporalmente",
   "tokens_matcheados": 3,
   "resumen_propiedades": "tipo: imputación de exportación con bienes importados temporalmente sin uso de divisas"
  },
  {
   "id": "Operacion_cobro_local_por_exportacion_de_ranchos_a_medios_de_transporte_de_bandera_extranj",
   "type": "Operacion",
   "label": "Cobro local de exportación",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: cobro local por exportación de ranchos a medios de transporte de bandera extranjera"
  },
  {
   "id": "Obligacion_el_contravalor_en_divisas_de_la_exportacion_hasta_alcanzar_el_valor_facturado_de",
   "type": "Obligacion",
   "label": "Ingreso y liquidación en plazos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El contravalor en divisas de la exportación hasta alcanzar el valor facturado deberá ingresarse al país y liquidarse en el mercado de cambios en los plazos esta…"
  },
  {
   "id": "Operacion_cobro_anticipado",
   "type": "Operacion",
   "label": "Cobros anticipados de exportación",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: cobro anticipado"
  },
  {
   "id": "Operacion_cobro_de_exportacion",
   "type": "Operacion",
   "label": "Cobros de exportaciones de bienes",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Cobros de exportaciones de bienes"
  },
  {
   "id": "Operacion_ingreso_de_divisas_por_exportacion_de_bienes",
   "type": "Operacion",
   "label": "Ingreso de divisas de exportación",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: ingreso de divisas por exportación de bienes"
  },
  {
   "id": "Operacion_cobro_de_exportacion_percibido_luego_del_embarque_no_liquidado",
   "type": "Operacion",
   "label": "Cobro de exportación post-embarque",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: cobro de exportación percibido luego del embarque no liquidado"
  },
  {
   "id": "Operacion_anticipo_y_cobro_de_exportacion",
   "type": "Operacion",
   "label": "Anticipos y cobros de exportaciones",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Anticipos y cobros de exportaciones argentinas de bienes y servicios conexos documentadas en pesos argentinos"
  }
 ]
}
```

### paso 7 — buscar_nodos {"consulta": "documento imputación seguimiento embarque divisas", "limite": 10}

```json
{
 "consulta": "documento imputación seguimiento embarque divisas",
 "total_con_match": 166,
 "resultados": [
  {
   "id": "Operacion_imputacion_de_ingresos_de_divisas",
   "type": "Operacion",
   "label": "Imputación al cumplimiento de seguimiento",
   "tokens_matcheados": 3,
   "resumen_propiedades": "tipo: imputación de ingresos de divisas"
  },
  {
   "id": "Operacion_seguimiento_de_permiso_de_embarque",
   "type": "Operacion",
   "label": "Seguimiento permiso de embarque",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Seguimiento de un permiso de embarque por la parte amparada por un Certificado DECRETO 929/13"
  },
  {
   "id": "Excepcion_la_entidad_encargada_del_seguimiento_del_permiso_de_embarque_podra_extender_el_p",
   "type": "Excepcion",
   "label": "Prórroga de plazo de liquidación",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La entidad encargada del seguimiento del permiso de embarque podrá extender el plazo de liquidación cuando el cliente haya utilizado el mecanismo de acumulación…"
  },
  {
   "id": "Obligacion_cuenta_con_copia_del_documento_de_transporte_conocimiento_de_embarque_carta_de_p",
   "type": "Obligacion",
   "label": "Verificar documento de transporte",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Cuenta con copia del Documento de Transporte (Conocimiento de Embarque – Carta de Porte – Guía Aérea)"
  },
  {
   "id": "Obligacion_efectuar_el_seguimiento_de_los_permisos_de_embarques_cuyos_cobros_se_pretenda_ap",
   "type": "Obligacion",
   "label": "Seguimiento de permisos de embarque",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Efectuar el seguimiento de los permisos de embarques cuyos cobros se pretenda aplicar acorde a lo previsto en el presente punto"
  },
  {
   "id": "Operacion_designacion_de_entidad_nominada",
   "type": "Operacion",
   "label": "Designación para seguimiento de embarque",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Designación de una entidad por un exportador para el seguimiento de un permiso de embarque"
  },
  {
   "id": "Restriccion_limite_usd_25_000_para_imputacion_sin_divisas",
   "type": "Restriccion",
   "label": "Límite USD 25.000 para imputación sin divisas",
   "tokens_matcheados": 2,
   "resumen_propiedades": "En la medida que el monto a imputar al permiso por este mecanismo supere el equivalente a USD 25.000 (dólares estadounidenses veinticinco mil), la entidad deber…"
  },
  {
   "id": "Operacion_imputacion_de_exportacion_de_bienes_sin_contravalor_en_divisas",
   "type": "Operacion",
   "label": "Imputación exportación sin contravalor divisas",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: imputación de exportación de bienes sin contravalor en divisas"
  },
  {
   "id": "Restriccion_la_entidad_podra_considerar_cumplimentado_el_seguimiento_de_un_permiso_de_embarq",
   "type": "Restriccion",
   "label": "Límite de imputación por porcentaje de facturación",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La entidad podrá considerar cumplimentado el seguimiento de un permiso de embarque por el equivalente de hasta el 25% (veinticinco por ciento) del valor factura…"
  },
  {
   "id": "Operacion_imputacion_de_exportacion_con_bienes_importados_temporalmente_sin_uso_de_divisas",
   "type": "Operacion",
   "label": "Imputación exportación bienes importados temporalmente",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: imputación de exportación con bienes importados temporalmente sin uso de divisas"
  }
 ]
}
```

### paso 8 — buscar_nodos {"consulta": "Certificado DECRETO 929/13", "limite": 10}

```json
{
 "consulta": "Certificado DECRETO 929/13",
 "total_con_match": 24,
 "resultados": [
  {
   "id": "Operacion_exportacion_alcanzada_por_beneficios_cambiarios_del_decreto_929_13",
   "type": "Operacion",
   "label": "Exportación en régimen de hidrocarburos",
   "tokens_matcheados": 3,
   "resumen_propiedades": "tipo: exportación alcanzada por beneficios cambiarios del Decreto 929/13"
  },
  {
   "id": "Comunicacion_decreto_91_19",
   "type": "Comunicacion",
   "label": "Com. Decreto 91/19",
   "tokens_matcheados": 1,
   "resumen_propiedades": "codigo: Decreto-91/19; tipo: Decreto; numero: 91"
  },
  {
   "id": "Excepcion_excepcion_por_punto_3_13",
   "type": "Excepcion",
   "label": "Excepción por punto 3.13",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Las entidades podrán también en el marco del punto 3.13., sin conformidad previa del BCRA si el requisito estuviese vigente"
  },
  {
   "id": "Restriccion_si_se_trata_de_servicios_que_fueron_o_seran_prestados_o_devengados_a_partir_del_",
   "type": "Restriccion",
   "label": "Servicios a partir de 13/12/23",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Si se trata de servicios que fueron o serán prestados o devengados a partir del 13/12/23, la entidad deberá constatar adicionalmente que el pago cumple las cond…"
  },
  {
   "id": "Restriccion_para_financiaciones_otorgadas_a_partir_del_13_12_23_la_operacion_debe_correspond",
   "type": "Restriccion",
   "label": "Fecha de financiación compatibilidad",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Para financiaciones otorgadas a partir del 13/12/23, la operación debe corresponder a una importación de servicios prestada o devengada a partir del 13/12/23."
  },
  {
   "id": "Operacion_emision_de_certificado",
   "type": "Operacion",
   "label": "Emisión de certificados de aplicación",
   "tokens_matcheados": 1,
   "resumen_propiedades": "La entidad será la única responsable de emitir los certificados de aplicación que habilitan que los cobros de exportaciones puedan ser imputados a los permisos …"
  },
  {
   "id": "Restriccion_para_financiaciones_otorgadas_a_partir_del_13_12_23_debe_cumplirse_con_requisito",
   "type": "Restriccion",
   "label": "Restricción de cumplimiento por fecha",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Para financiaciones otorgadas a partir del 13/12/23, debe cumplirse con requisitos específicos de registro aduanero y plazos"
  },
  {
   "id": "Restriccion_este_mecanismo_no_podra_ser_utilizado_por_los_aumentos_de_exportaciones_de_biene",
   "type": "Restriccion",
   "label": "Exclusión beneficiarios decreto 679/22",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Este mecanismo no podrá ser utilizado por los aumentos de exportaciones de bienes del año 2023 por las personas jurídicas que sean beneficiarias del régimen de …"
  },
  {
   "id": "Restriccion_cuando_el_cliente_sea_beneficiario_del_decreto_277_22_los_montos_de_certificacio",
   "type": "Restriccion",
   "label": "Restricción por deuda de Decreto 277/22",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Cuando el cliente sea beneficiario del Decreto 277/22, los montos de certificaciones por régimen incremental de petróleo/gas deberán ser deducidas del monto de …"
  },
  {
   "id": "Obligacion_constatar_que_el_exportador_posee_un_certificado_de_inversion_para_exportacion_e",
   "type": "Obligacion",
   "label": "Constatación de Certificado de Inversión",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Constatar que el exportador posee un Certificado de Inversión para Exportación emitido por la Autoridad de Aplicación"
  }
 ]
}
```

### paso 9 — ver_vecinos {"id": "Operacion_seguimiento_de_permiso_de_embarque", "direccion": "ambas"}

```json
{
 "id": "Operacion_seguimiento_de_permiso_de_embarque",
 "label": "Seguimiento permiso de embarque",
 "n_salientes_total": 0,
 "n_entrantes_total": 1,
 "salientes": [],
 "salientes_truncado": false,
 "entrantes": [
  {
   "relation": "condiciona",
   "vecino_id": "Obligacion_consideracion_cumplimiento_seguimiento",
   "vecino_label": "Consideración cumplimiento seguimiento",
   "provenances": [
    {
     "source_doc": "TO_exterior_cambios_actual.pdf",
     "location": "Punto 8.5. Otras imputaciones admitidas en el cumplimiento del seguimiento. (parte 5)"
    }
   ]
  }
 ],
 "entrantes_truncado": false
}
```

### paso 10 — ver_nodo {"id": "Operacion_emision_de_certificado"}

```json
{
 "id": "Operacion_emision_de_certificado",
 "type": "Operacion",
 "label": "Emisión de certificados de aplicación",
 "properties": {
  "tipo": "emisión de certificado",
  "description": "La entidad será la única responsable de emitir los certificados de aplicación que habilitan que los cobros de exportaciones puedan ser imputados a los permisos correspondientes"
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 7.10. 9.1.7. Aportes de inversión extranjera directa admitidos en los puntos 7.9. o 7."
  }
 ]
}
```

### paso 11 — ver_vecinos {"id": "Operacion_emision_de_certificado", "direccion": "ambas"}

```json
{
 "id": "Operacion_emision_de_certificado",
 "label": "Emisión de certificados de aplicación",
 "n_salientes_total": 1,
 "n_entrantes_total": 1,
 "salientes": [
  {
   "relation": "establecida_en",
   "vecino_id": "TextoOrdenado_to_exterior_cambios_actual_pdf",
   "vecino_label": "Exterior y Cambios",
   "provenances": [
    {
     "source_doc": "TO_exterior_cambios_actual.pdf",
     "location": "Punto 7.10. 9.1.7. Aportes de inversión extranjera directa admitidos en los puntos 7.9. o 7."
    }
   ]
  }
 ],
 "salientes_truncado": false,
 "entrantes": [
  {
   "relation": "regula",
   "vecino_id": "Obligacion_la_entidad_sera_la_unica_responsable_de_emitir_los_certificados_de_aplicacion_qu",
   "vecino_label": "Emitir certificados de aplicación",
   "provenances": [
    {
     "source_doc": "TO_exterior_cambios_actual.pdf",
     "location": "Punto 7.10. 9.1.7. Aportes de inversión extranjera directa admitidos en los puntos 7.9. o 7."
    }
   ]
  }
 ],
 "entrantes_truncado": false
}
```

### paso 12 — ver_nodo {"id": "Obligacion_la_entidad_sera_la_unica_responsable_de_emitir_los_certificados_de_aplicacion_qu"}

```json
{
 "id": "Obligacion_la_entidad_sera_la_unica_responsable_de_emitir_los_certificados_de_aplicacion_qu",
 "type": "Obligacion",
 "label": "Emitir certificados de aplicación",
 "properties": {
  "descripcion": "La entidad será la única responsable de emitir los certificados de aplicación que habilitan que los cobros de exportaciones puedan ser imputados a los permisos correspondientes",
  "tipo": "presentacion_informativa"
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 7.10. 9.1.7. Aportes de inversión extranjera directa admitidos en los puntos 7.9. o 7."
  }
 ]
}
```

### paso 13 — buscar_nodos {"consulta": "certificado aplicación cobro exportación prefinanciación", "limite": 10}

```json
{
 "consulta": "certificado aplicación cobro exportación prefinanciación",
 "total_con_match": 175,
 "resultados": [
  {
   "id": "Operacion_cobro_local_por_exportacion_de_ranchos_a_medios_de_transporte_de_bandera_extranj",
   "type": "Operacion",
   "label": "Cobro local de exportación",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: cobro local por exportación de ranchos a medios de transporte de bandera extranjera"
  },
  {
   "id": "Operacion_prefinanciacion",
   "type": "Operacion",
   "label": "Prefinanciación de exportación",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Prefinanciaciones y financiaciones de exportaciones pendientes al 31/08/19 que fueron otorgadas o garantizadas por entidades financieras locales"
  },
  {
   "id": "Operacion_cobro_anticipado",
   "type": "Operacion",
   "label": "Cobros anticipados de exportación",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: cobro anticipado"
  },
  {
   "id": "Operacion_cobro_de_exportacion",
   "type": "Operacion",
   "label": "Cobros de exportaciones de bienes",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Cobros de exportaciones de bienes"
  },
  {
   "id": "Operacion_cobro_de_exportacion_percibido_luego_del_embarque_no_liquidado",
   "type": "Operacion",
   "label": "Cobro de exportación post-embarque",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: cobro de exportación percibido luego del embarque no liquidado"
  },
  {
   "id": "Operacion_anticipo_y_cobro_de_exportacion",
   "type": "Operacion",
   "label": "Anticipos y cobros de exportaciones",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Anticipos y cobros de exportaciones argentinas de bienes y servicios conexos documentadas en pesos argentinos"
  },
  {
   "id": "Operacion_aplicacion_de_fondos",
   "type": "Operacion",
   "label": "Aplicación de cobros de exportación",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Aplicación de cobros de exportación a usos admitidos"
  },
  {
   "id": "Operacion_cobro_de_exportacion_de_servicios",
   "type": "Operacion",
   "label": "Cobro de exportaciones de servicios",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Cobros por la prestación de servicios por parte de residentes a no residentes"
  },
  {
   "id": "Operacion_aplicacion_de_cobros_de_exportaciones_de_bienes_y_servicios",
   "type": "Operacion",
   "label": "Cobro exportaciones bienes servicios",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: aplicación de cobros de exportaciones de bienes y servicios"
  },
  {
   "id": "Restriccion_el_monto_aplicado_no_supere_el_20_del_monto_en_divisas_que_corresponden_al_permi",
   "type": "Restriccion",
   "label": "Límite de aplicación por exportación",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El monto aplicado no supere el 20% del monto en divisas que corresponden al permiso de exportación cuyos cobros se aplican"
  }
 ]
}
```

### paso 14 — buscar_nodos {"consulta": "boleto venta divisas prefinanciación imputación", "limite": 10}

```json
{
 "consulta": "boleto venta divisas prefinanciación imputación",
 "total_con_match": 152,
 "resultados": [
  {
   "id": "Obligacion_corresponde_efectuar_un_boleto_de_venta_por_el_concepto_lineas_de_credito_del_ex",
   "type": "Obligacion",
   "label": "Registrar venta de divisas",
   "tokens_matcheados": 3,
   "resumen_propiedades": "corresponde efectuar un boleto de venta por el concepto 'Líneas de crédito del exterior' a nombre de la propia entidad en calidad de cliente"
  },
  {
   "id": "Operacion_venta_de_moneda_extranjera",
   "type": "Operacion",
   "label": "Venta de divisas",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La venta de las divisas será cursada con débito en cuentas del cliente en entidades financieras locales por alguna de las modalidades de medios de pago vigentes"
  },
  {
   "id": "Obligacion_boleto_de_venta_de_cambio",
   "type": "Obligacion",
   "label": "Boleto de venta de cambio",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La mencionada entidad deberá realizar un boleto de venta de cambio a nombre del cliente por el código de concepto que identifique el tipo de operación consignan…"
  },
  {
   "id": "Obligacion_la_entidad_debera_realizar_un_boleto_de_compra_y_o_venta_de_cambio_conforme_a_lo",
   "type": "Obligacion",
   "label": "Realizar boleto de cambio",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La entidad deberá realizar un boleto de compra y/o venta de cambio, conforme a lo estipulado en el punto 5.3"
  },
  {
   "id": "Obligacion_la_entidad_debera_realizar_un_boleto_de_venta_de_cambio_a_nombre_del_importador_",
   "type": "Obligacion",
   "label": "Boleto de venta de cambio",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La entidad deberá realizar un boleto de venta de cambio a nombre del importador por el código de concepto S33. Registro de importaciones de servicios por adjudi…"
  },
  {
   "id": "Obligacion_la_venta_de_las_divisas_es_cursada_con_debito_en_cuentas_del_cliente_en_entidade",
   "type": "Obligacion",
   "label": "Débito en cuentas locales",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La venta de las divisas es cursada con débito en cuentas del cliente en entidades financieras locales por alguna de las modalidades de medios de pago vigentes"
  },
  {
   "id": "Operacion_boleto_de_cambio",
   "type": "Operacion",
   "label": "Boleto de venta de cambio",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Boleto de venta de cambio a nombre del importador por el código de concepto 'B26. Registro de importaciones de bienes por adjudicación de bonos BOPREAL'"
  },
  {
   "id": "Operacion_registro_cambio",
   "type": "Operacion",
   "label": "Boleto de venta de cambio",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Realización de boleto de venta de cambio a nombre del cliente por el código de concepto correspondiente a la adjudicación de bonos BOPREAL"
  },
  {
   "id": "Obligacion_correspondera_registrar_boletos_simultaneos_de_compra_y_venta_de_divisas_a_nombr",
   "type": "Obligacion",
   "label": "Registrar boletos simultáneos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "corresponderá registrar boletos simultáneos de compra y venta de divisas a nombre del cliente que recibe la financiación"
  },
  {
   "id": "Operacion_compra_venta_de_divisas",
   "type": "Operacion",
   "label": "Operación con divisas extranjeras",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Instrumentos de pago expresados en una moneda emitida por un estado extranjero y generalmente aceptados en transacciones transnacionales: transferencia bancaria…"
  }
 ]
}
```

### paso 15 — buscar_nodos {"consulta": "entidad encargada seguimiento permiso embarque registrar imputación", "limite": 10}

```json
{
 "consulta": "entidad encargada seguimiento permiso embarque registrar imputación",
 "total_con_match": 324,
 "resultados": [
  {
   "id": "Excepcion_la_entidad_encargada_del_seguimiento_del_permiso_de_embarque_podra_extender_el_p",
   "type": "Excepcion",
   "label": "Prórroga de plazo de liquidación",
   "tokens_matcheados": 5,
   "resumen_propiedades": "La entidad encargada del seguimiento del permiso de embarque podrá extender el plazo de liquidación cuando el cliente haya utilizado el mecanismo de acumulación…"
  },
  {
   "id": "Obligacion_la_entidad_financiera_encargada_del_seguimiento_de_anticipos_y_otras_financiacio",
   "type": "Obligacion",
   "label": "Registrar operación ante BCRA",
   "tokens_matcheados": 4,
   "resumen_propiedades": "La entidad financiera encargada del Seguimiento de anticipos y otras financiaciones de exportación de bienes de las operaciones deberá concretar su registro ant…"
  },
  {
   "id": "Obligacion_la_entidad_encargada_del_seguimiento_del_permiso_podra_conceder_extensiones_en_e",
   "type": "Obligacion",
   "label": "Conceder extensiones del plazo",
   "tokens_matcheados": 4,
   "resumen_propiedades": "La entidad encargada del seguimiento del permiso podrá conceder extensiones en el plazo de ingreso y liquidación en las circunstancias especificadas"
  },
  {
   "id": "Restriccion_la_entidad_podra_considerar_cumplimentado_el_seguimiento_de_un_permiso_de_embarq",
   "type": "Restriccion",
   "label": "Límite de imputación por porcentaje de facturación",
   "tokens_matcheados": 4,
   "resumen_propiedades": "La entidad podrá considerar cumplimentado el seguimiento de un permiso de embarque por el equivalente de hasta el 25% (veinticinco por ciento) del valor factura…"
  },
  {
   "id": "Operacion_seguimiento_de_permiso_de_embarque",
   "type": "Operacion",
   "label": "Seguimiento permiso de embarque",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Seguimiento de un permiso de embarque por la parte amparada por un Certificado DECRETO 929/13"
  },
  {
   "id": "EntidadFinanciera_entidad_encargada_del_seguimiento",
   "type": "EntidadFinanciera",
   "label": "Entidad encargada del seguimiento",
   "tokens_matcheados": 3,
   "resumen_propiedades": "categoria: entidad financiera encargada del seguimiento"
  },
  {
   "id": "Obligacion_la_certificacion_de_afectacion_emitida_por_la_entidad_encargada_del_seguimiento_",
   "type": "Obligacion",
   "label": "Contar con certificación de afectación",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La certificación de afectación emitida por la entidad encargada del seguimiento en el SEPAIMPO (Sección 11.) del despacho de importación temporal para transform…"
  },
  {
   "id": "Operacion_designacion_de_entidad_nominada",
   "type": "Operacion",
   "label": "Designación para seguimiento de embarque",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Designación de una entidad por un exportador para el seguimiento de un permiso de embarque"
  },
  {
   "id": "Obligacion_el_exportador_debera_presentar_ante_la_entidad_encargada_de_seguimiento_document",
   "type": "Obligacion",
   "label": "Presentar documentación de transferencias",
   "tokens_matcheados": 3,
   "resumen_propiedades": "El exportador deberá presentar ante la entidad encargada de seguimiento documentación que demuestre que se registraron transferencias en moneda extranjera desde…"
  },
  {
   "id": "Obligacion_la_entidad_encargada_del_seguimiento_del_pago_debera_considerar_los_tipos_de_pas",
   "type": "Obligacion",
   "label": "Considerar tipos de pase correspondientes",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La entidad encargada del seguimiento del pago deberá considerar los tipos de pase correspondientes a la fecha de transferencia al beneficiario de los fondos par…"
  }
 ]
}
```



---

# CQN-011

## Respuesta final íntegra (trace.final_json)

```json
{
 "respuesta": "La información complementaria vinculada al riesgo de tasa de interés en la cartera de inversión se informa con frecuencia trimestral. El código de consolidación 3 corresponde a la presentación en base consolidada trimestral, y se aplica a entidades controlantes que deben presentar información consolidada de sus filiales o subsidiarias.",
 "citas": [
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Punto 1.1. La información tendrá frecuencia mensual y se integrará con datos referidos al m"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Punto 10.1. Normas de procedimiento"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Punto 1.2. Los importes se registrarán en miles de pesos, sin decimales"
  }
 ],
 "respondible": true
}
```

(`respondible`: true · tool_calls_used: 10 · hit_tool_limit: False)

## Inventario de pasos + fidelidad runtime↔re-ejecución

| paso | tool | input | output_chars (runtime) | re-ejecutado | fiel |
|---|---|---|---|---|---|
| 1 | buscar_nodos | `{"consulta": "información complementaria riesgo tasa de interés cartera inversión", "limit` | 3348 | 3348 | SÍ |
| 2 | buscar_nodos | `{"consulta": "código consolidación base consolidada", "limite": 10}` | 3449 | 3449 | SÍ |
| 3 | ver_nodo | `{"id": "Obligacion_informar_riesgo_tasa_interes_eve"}` | 653 | 653 | SÍ |
| 4 | ver_nodo | `{"id": "Obligacion_informacion_base_individual_y_consolidada"}` | 610 | 610 | SÍ |
| 5 | ver_vecinos | `{"id": "Obligacion_informar_riesgo_tasa_interes_eve", "direccion": "ambas"}` | 931 | 931 | SÍ |
| 6 | buscar_nodos | `{"consulta": "código consolidación 3 caso entidad", "limite": 5}` | 1895 | 1895 | SÍ |
| 7 | buscar_nodos | `{"consulta": "código consolidación 3 entidad controlante filial subsidiaria", "limite": 5}` | 1753 | 1753 | SÍ |
| 8 | ver_nodo | `{"id": "Restriccion_la_informacion_tendra_frecuencia_trimestral_para_codigo_3"}` | 572 | 572 | SÍ |
| 9 | buscar_nodos | `{"consulta": "consolidación 3 entidad controlante grupo económico", "limite": 5}` | 1081 | 1081 | SÍ |
| 10 | buscar_nodos | `{"consulta": "código consolidación 0 1 2 3 definición significado", "limite": 5}` | 1527 | 1527 | SÍ |

**Fidelidad: 10/10** (igualdad de largos del output completo).

## Apéndice — outputs completos re-ejecutados

### paso 1 — buscar_nodos {"consulta": "información complementaria riesgo tasa de interés cartera inversión", "limite": 10}

```json
{
 "consulta": "información complementaria riesgo tasa de interés cartera inversión",
 "total_con_match": 2472,
 "resultados": [
  {
   "id": "Operacion_calculo_de_riesgo_de_tasa_de_interes",
   "type": "Operacion",
   "label": "Cálculo riesgo tasa interés EVE",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Cálculo del riesgo de tasa de interés en la cartera de inversión - Medida de riesgo EVE estandarizada (Sección 11.) en base individual y consolidado mensual (có…"
  },
  {
   "id": "Obligacion_se_consignara_el_valor_de_la_exigencia_por_riesgo_general_de_tasa_de_interes_par",
   "type": "Obligacion",
   "label": "Consignación de exigencia riesgo general tasa",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Se consignará el valor de la exigencia por riesgo general de tasa de interés para el último día del período (n) determinada conforme a las disposiciones del pun…"
  },
  {
   "id": "Obligacion_se_consignara_el_valor_de_la_exigencia_por_riesgo_especifico_de_tasa_de_interes_",
   "type": "Obligacion",
   "label": "Consignación de exigencia riesgo específico tasa",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Se consignará el valor de la exigencia por riesgo específico de tasa de interés para el último día del período (n) determinada conforme a las disposiciones del …"
  },
  {
   "id": "Operacion_calculo_de_capital_requerido",
   "type": "Operacion",
   "label": "Cálculo exigencia capital por riesgo tasa interés",
   "tokens_matcheados": 4,
   "resumen_propiedades": "La exigencia de capital por el riesgo de tasa de interés se deberá calcular respecto de los títulos de deuda y otros instrumentos imputados a la cartera de nego…"
  },
  {
   "id": "Operacion_calculo_de_exigencia_capital_por_riesgo_general",
   "type": "Operacion",
   "label": "Determinación de exigencia riesgo general tasa interés",
   "tokens_matcheados": 4,
   "resumen_propiedades": "tipo: cálculo de exigencia capital por riesgo general"
  },
  {
   "id": "Operacion_calculo_de_exigencia_capital_por_riesgo_especifico",
   "type": "Operacion",
   "label": "Determinación de exigencia riesgo específico tasa interés",
   "tokens_matcheados": 4,
   "resumen_propiedades": "tipo: cálculo de exigencia capital por riesgo específico"
  },
  {
   "id": "Operacion_registro_de_operaciones",
   "type": "Operacion",
   "label": "Registro en cartera inversión",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Registro de operaciones de activos admitidos como garantía en la cartera de inversión"
  },
  {
   "id": "Restriccion_empresas_con_grado_de_inversion_con_ponderador_de_riesgo_65",
   "type": "Restriccion",
   "label": "Ponderador empresas inversión",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Empresas con grado de inversión con ponderador de riesgo 65%"
  },
  {
   "id": "Obligacion_informar_riesgo_tasa_interes_eve",
   "type": "Obligacion",
   "label": "Informar riesgo tasa interés EVE",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Cálculo del riesgo de tasa de interés en la cartera de inversión - Medida de riesgo EVE estandarizada (Sección 11.) en base individual y consolidado mensual (có…"
  },
  {
   "id": "Obligacion_los_riesgos_de_tasa_de_interes_y_de_moneda_extranjera_deberan_mitigarse_en_forma",
   "type": "Obligacion",
   "label": "Mitigar descalce de tasa y moneda",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Los riesgos de tasa de interés y de moneda extranjera deberán mitigarse en forma adecuada, sin que esto implique que deba obtenerse una cobertura perfecta y com…"
  }
 ]
}
```

### paso 2 — buscar_nodos {"consulta": "código consolidación base consolidada", "limite": 10}

```json
{
 "consulta": "código consolidación base consolidada",
 "total_con_match": 30,
 "resultados": [
  {
   "id": "Obligacion_las_normas_del_pais_donde_este_situada_la_casa_matriz_o_entidad_controlante_debe",
   "type": "Obligacion",
   "label": "Supervisión sobre base consolidada",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Las normas del país donde esté situada la casa matriz o entidad controlante deberán abarcar la supervisión sobre base consolidada de las filiales o subsidiarias…"
  },
  {
   "id": "Restriccion_la_informacion_tendra_frecuencia_trimestral_para_codigo_3",
   "type": "Restriccion",
   "label": "Frecuencia consolidación trimestral",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La información tendrá frecuencia trimestral y se integrará con saldos al cierre del trimestre bajo informe"
  },
  {
   "id": "Obligacion_informacion_base_individual_y_consolidada",
   "type": "Obligacion",
   "label": "Información base individual y consolidada",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Los datos se informarán sobre base individual (código de consolidación 0 ó 1) y consolidada trimestral (código de consolidación 3). Se regirán por los plazos de…"
  },
  {
   "id": "Restriccion_las_normas_del_pais_donde_este_situada_la_casa_matriz_o_entidad_controlante_debe",
   "type": "Restriccion",
   "label": "Requisito: supervisión sobre base consolidada",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Las normas del país donde esté situada la casa matriz o entidad controlante deberán abarcar la supervisión sobre base consolidada de las sucursales o subsidiari…"
  },
  {
   "id": "Obligacion_las_entidades_financieras_controlantes_sujetas_a_supervision_consolidada_observa",
   "type": "Obligacion",
   "label": "Observar capitales mínimos en base consolidada",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Las entidades financieras controlantes sujetas a supervisión consolidada observarán las normas en materia de capitales mínimos sobre base consolidada mensual y,…"
  },
  {
   "id": "Operacion_observancia_de_requisitos_de_capitales_minimos_en_base_consolidada_mensual_y_tri",
   "type": "Operacion",
   "label": "Observancia capitales mínimos base consolidada",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: Observancia de requisitos de capitales mínimos en base consolidada mensual y trimestral"
  },
  {
   "id": "Operacion_basis_transactions",
   "type": "Operacion",
   "label": "Operaciones sobre base",
   "tokens_matcheados": 1,
   "resumen_propiedades": "derivados que referencian la base entre dos factores de riesgo y están denominados en una sola moneda"
  },
  {
   "id": "Operacion_consolidacion_contable",
   "type": "Operacion",
   "label": "Consolidación de información",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Consolidación de información financiera según códigos de consolidación (0, 1, 2, 3, 9)"
  },
  {
   "id": "Operacion_consolidacion_y_reporte_en_terminos_netos_de_posiciones_vendidas_y_compradas_en_",
   "type": "Operacion",
   "label": "Consolidación neta posiciones",
   "tokens_matcheados": 1,
   "resumen_propiedades": "tipo: Consolidación y reporte en términos netos de posiciones vendidas y compradas en un mismo instrumento"
  },
  {
   "id": "Obligacion_las_ecai_deberan_divulgar_su_codigo_de_conducta_el_caracter_general_de_sus_acuer",
   "type": "Obligacion",
   "label": "Divulgar información requerida",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Las ECAI deberán divulgar: su código de conducta; el carácter general de sus acuerdos de remuneración con las entidades evaluadas; sus métodos de evaluación, in…"
  }
 ]
}
```

### paso 3 — ver_nodo {"id": "Obligacion_informar_riesgo_tasa_interes_eve"}

```json
{
 "id": "Obligacion_informar_riesgo_tasa_interes_eve",
 "type": "Obligacion",
 "label": "Informar riesgo tasa interés EVE",
 "properties": {
  "description": "Cálculo del riesgo de tasa de interés en la cartera de inversión - Medida de riesgo EVE estandarizada (Sección 11.) en base individual y consolidado mensual (códigos de consolidación 0 o 1 y 2) y su respectivo total de control (partida 70500000)",
  "tipo": "presentacion_informativa",
  "plazo": "trimestral"
 },
 "provenances": [
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Punto 1.1. La información tendrá frecuencia mensual y se integrará con datos referidos al m"
  }
 ]
}
```

### paso 4 — ver_nodo {"id": "Obligacion_informacion_base_individual_y_consolidada"}

```json
{
 "id": "Obligacion_informacion_base_individual_y_consolidada",
 "type": "Obligacion",
 "label": "Información base individual y consolidada",
 "properties": {
  "tipo": "presentacion_informativa",
  "description": "Los datos se informarán sobre base individual (código de consolidación 0 ó 1) y consolidada trimestral (código de consolidación 3). Se regirán por los plazos de presentación previstos para el régimen informativo contable mensual y para Supervisión respectivamente"
 },
 "provenances": [
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Punto 10.1. Normas de procedimiento"
  }
 ]
}
```

### paso 5 — ver_vecinos {"id": "Obligacion_informar_riesgo_tasa_interes_eve", "direccion": "ambas"}

```json
{
 "id": "Obligacion_informar_riesgo_tasa_interes_eve",
 "label": "Informar riesgo tasa interés EVE",
 "n_salientes_total": 2,
 "n_entrantes_total": 0,
 "salientes": [
  {
   "relation": "establecida_en",
   "vecino_id": "TextoOrdenado_to_regimen_informativo_contable_mensual_actual_pdf",
   "vecino_label": "Régimen Informativo Contable Mensual",
   "provenances": [
    {
     "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
     "location": "Punto 1.1. La información tendrá frecuencia mensual y se integrará con datos referidos al m"
    }
   ]
  },
  {
   "relation": "regula",
   "vecino_id": "Operacion_calculo_de_riesgo_de_tasa_de_interes",
   "vecino_label": "Cálculo riesgo tasa interés EVE",
   "provenances": [
    {
     "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
     "location": "Punto 1.1. La información tendrá frecuencia mensual y se integrará con datos referidos al m"
    }
   ]
  }
 ],
 "salientes_truncado": false,
 "entrantes": [],
 "entrantes_truncado": false
}
```

### paso 6 — buscar_nodos {"consulta": "código consolidación 3 caso entidad", "limite": 5}

```json
{
 "consulta": "código consolidación 3 caso entidad",
 "total_con_match": 318,
 "resultados": [
  {
   "id": "Restriccion_la_informacion_tendra_frecuencia_trimestral_para_codigo_3",
   "type": "Restriccion",
   "label": "Frecuencia consolidación trimestral",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La información tendrá frecuencia trimestral y se integrará con saldos al cierre del trimestre bajo informe"
  },
  {
   "id": "Restriccion_en_caso_de_que_el_monto_a_imputar_sea_superior_al_valor_indicado_la_entidad_debe",
   "type": "Restriccion",
   "label": "Límite para auditoría externa",
   "tokens_matcheados": 2,
   "resumen_propiedades": "En caso de que el monto a imputar sea superior al valor indicado, la entidad deberá contar con documentación adicional que le permita certificar el carácter gen…"
  },
  {
   "id": "Restriccion_la_entidad_debera_contar_con_la_conformidad_previa_del_bcra_en_el_caso_de_que_el",
   "type": "Restriccion",
   "label": "Conformidad BCRA para clientes ARCA",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La entidad deberá contar con la conformidad previa del BCRA en el caso de que el cliente sea una persona humana o jurídica incluida por la Agencia de Recaudació…"
  },
  {
   "id": "Restriccion_en_caso_de_cesion_del_beneficiario_original_la_entidad_debera_contar_con_una_cer",
   "type": "Restriccion",
   "label": "Requisito de certificación para cesión",
   "tokens_matcheados": 2,
   "resumen_propiedades": "En caso de cesión del beneficiario original, la entidad deberá contar con una certificación de la entidad encargada del seguimiento del Decreto 277/22"
  },
  {
   "id": "Restriccion_suspension_envio_consolidacion_nivel_3",
   "type": "Restriccion",
   "label": "Suspensión envío consolidación nivel 3",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Se suspende el envío de informaciones con código de consolidación 3 -con la excepción prevista para Ratio de apalancamiento-, siendo marzo/24 el último período …"
  }
 ]
}
```

### paso 7 — buscar_nodos {"consulta": "código consolidación 3 entidad controlante filial subsidiaria", "limite": 5}

```json
{
 "consulta": "código consolidación 3 entidad controlante filial subsidiaria",
 "total_con_match": 269,
 "resultados": [
  {
   "id": "Restriccion_la_informacion_tendra_frecuencia_trimestral_para_codigo_3",
   "type": "Restriccion",
   "label": "Frecuencia consolidación trimestral",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La información tendrá frecuencia trimestral y se integrará con saldos al cierre del trimestre bajo informe"
  },
  {
   "id": "EntidadFinanciera_entidad_controlante",
   "type": "EntidadFinanciera",
   "label": "Entidades controlantes",
   "tokens_matcheados": 2,
   "resumen_propiedades": "categoria: entidad financiera controlante"
  },
  {
   "id": "Obligacion_las_normas_del_pais_donde_este_situada_la_casa_matriz_o_entidad_controlante_debe",
   "type": "Obligacion",
   "label": "Supervisión sobre base consolidada",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Las normas del país donde esté situada la casa matriz o entidad controlante deberán abarcar la supervisión sobre base consolidada de las filiales o subsidiarias…"
  },
  {
   "id": "Restriccion_suspension_envio_consolidacion_nivel_3",
   "type": "Restriccion",
   "label": "Suspensión envío consolidación nivel 3",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Se suspende el envío de informaciones con código de consolidación 3 -con la excepción prevista para Ratio de apalancamiento-, siendo marzo/24 el último período …"
  },
  {
   "id": "Obligacion_la_entidad_debera_cumplir_con_lo_previsto_en_el_punto_3_1_de_las_normas_sobre_ev",
   "type": "Obligacion",
   "label": "Cumplimiento de evaluaciones crediticias",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La entidad deberá cumplir con lo previsto en el punto 3.1. de las normas sobre Evaluaciones crediticias, requiriendo calificación internacional de riesgo compre…"
  }
 ]
}
```

### paso 8 — ver_nodo {"id": "Restriccion_la_informacion_tendra_frecuencia_trimestral_para_codigo_3"}

```json
{
 "id": "Restriccion_la_informacion_tendra_frecuencia_trimestral_para_codigo_3",
 "type": "Restriccion",
 "label": "Frecuencia consolidación trimestral",
 "properties": {
  "descripcion": "La información tendrá frecuencia trimestral para código 3",
  "tipo": "limite_cualitativo",
  "description": "La información tendrá frecuencia trimestral y se integrará con saldos al cierre del trimestre bajo informe"
 },
 "provenances": [
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Punto 1.2. Los importes se registrarán en miles de pesos, sin decimales."
  }
 ]
}
```

### paso 9 — buscar_nodos {"consulta": "consolidación 3 entidad controlante grupo económico", "limite": 5}

```json
{
 "consulta": "consolidación 3 entidad controlante grupo económico",
 "total_con_match": 285,
 "resultados": [
  {
   "id": "EntidadFinanciera_entidad_grupo_a",
   "type": "EntidadFinanciera",
   "label": "Entidades Grupo A",
   "tokens_matcheados": 2,
   "resumen_propiedades": "categoria: entidad financiera grupo A"
  },
  {
   "id": "EntidadFinanciera_entidad_grupo_b",
   "type": "EntidadFinanciera",
   "label": "Entidades grupo B",
   "tokens_matcheados": 2,
   "resumen_propiedades": "categoria: entidad financiera grupo B"
  },
  {
   "id": "EntidadFinanciera_entidad_grupo_c",
   "type": "EntidadFinanciera",
   "label": "Entidades grupo C",
   "tokens_matcheados": 2,
   "resumen_propiedades": "categoria: entidad financiera grupo C"
  },
  {
   "id": "EntidadFinanciera_entidad_del_grupo_1",
   "type": "EntidadFinanciera",
   "label": "Entidades del grupo 1",
   "tokens_matcheados": 2,
   "resumen_propiedades": "categoria: entidades financieras grupo 1"
  },
  {
   "id": "EntidadFinanciera_entidad_del_grupo_2",
   "type": "EntidadFinanciera",
   "label": "Entidades del grupo 2",
   "tokens_matcheados": 2,
   "resumen_propiedades": "categoria: entidades del grupo 2"
  }
 ]
}
```

### paso 10 — buscar_nodos {"consulta": "código consolidación 0 1 2 3 definición significado", "limite": 5}

```json
{
 "consulta": "código consolidación 0 1 2 3 definición significado",
 "total_con_match": 129,
 "resultados": [
  {
   "id": "Restriccion_acciones_definidas_conforme_al_punto_2_11_3_250",
   "type": "Restriccion",
   "label": "Ponderador acciones grupo 1",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Acciones (definidas conforme al punto 2.11.3.): 250"
  },
  {
   "id": "Obligacion_la_facultad_de_revocacion_segun_lo_establecido_en_el_apartado_v_del_punto_2_3_1_",
   "type": "Obligacion",
   "label": "Informar facultad de revocación",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La facultad de revocación según lo establecido en el apartado v) del punto 2.3.1.1"
  },
  {
   "id": "Restriccion_la_informacion_tendra_frecuencia_trimestral_para_codigo_3",
   "type": "Restriccion",
   "label": "Frecuencia consolidación trimestral",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La información tendrá frecuencia trimestral y se integrará con saldos al cierre del trimestre bajo informe"
  },
  {
   "id": "Excepcion_si_n_0_ningun_periodo_con_ib_positivo_debera_observarse_una_exigencia_equivalent",
   "type": "Excepcion",
   "label": "Excepción N=0 Grupo 2",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Si n = 0 (ningún período con IB positivo), deberá observarse una exigencia equivalente al límite previsto en el punto 7.3 de las normas sobre Capitales mínimos …"
  },
  {
   "id": "Excepcion_no_aplicable_punto_3_12_1",
   "type": "Excepcion",
   "label": "No aplicable punto 3.12.1",
   "tokens_matcheados": 2,
   "resumen_propiedades": "En la medida que no encuadre en el punto 3.12.1"
  }
 ]
}
```



---

# CQN-012

## Respuesta final íntegra (trace.final_json)

```json
{
 "respuesta": "La exigencia de capital mínimo que debe integrar una entidad financiera se determina como la suma de los componentes por riesgo de crédito, riesgo de mercado y riesgo operacional, junto con otras exigencias regulatorias. Cada componente se calcula conforme a metodologías específicas establecidas en la normativa.\n\nPara el primer mes de funcionamiento de una nueva entidad, el componente de la exigencia correspondiente al riesgo operacional se calcula de manera especial: equivale al 10% de la sumatoria de las exigencias determinadas por los riesgos de crédito y de mercado de ese mes (considerando para el riesgo de mercado las posiciones del último día del mes).",
 "citas": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Punto 7.4. Nuevas entidades."
  }
 ],
 "respondible": true
}
```

(`respondible`: true · tool_calls_used: 15 · hit_tool_limit: True)

## Inventario de pasos + fidelidad runtime↔re-ejecución

| paso | tool | input | output_chars (runtime) | re-ejecutado | fiel |
|---|---|---|---|---|---|
| 1 | buscar_nodos | `{"consulta": "capital mínimo exigencia entidad financiera", "limite": 10}` | 3652 | 3652 | SÍ |
| 2 | buscar_nodos | `{"consulta": "riesgo operacional cálculo componente", "limite": 10}` | 3215 | 3215 | SÍ |
| 3 | ver_nodo | `{"id": "Operacion_calculo_de_exigencia_de_capital_minimo_por_riesgo_de_credito"}` | 367 | 367 | SÍ |
| 4 | ver_nodo | `{"id": "Operacion_calculo_de_capital_minimo_por_riesgo_operacional"}` | 334 | 334 | SÍ |
| 5 | buscar_nodos | `{"consulta": "primer mes funcionamiento riesgo operacional", "limite": 10}` | 3589 | 3589 | SÍ |
| 6 | ver_nodo | `{"id": "Restriccion_la_exigencia_mensual_de_capital_minimo_por_riesgo_operacional_de_las_e` | 694 | 694 | SÍ |
| 7 | ver_vecinos | `{"id": "Operacion_calculo_de_capital_minimo_por_riesgo_operacional", "direccion": "ambas"}` | 1199 | 1199 | SÍ |
| 8 | buscar_nodos | `{"consulta": "exigencia capital total determinación cálculo", "limite": 10}` | 2875 | 2875 | SÍ |
| 9 | ver_nodo | `{"id": "Operacion_calculo_de_exigencia"}` | 499 | 499 | SÍ |
| 10 | ver_vecinos | `{"id": "Operacion_calculo_de_exigencia", "direccion": "ambas"}` | 497 | 497 | SÍ |
| 11 | buscar_nodos | `{"consulta": "exigencia capital riesgo crédito mercado operacional suma", "limite": 10}` | 3324 | 3324 | SÍ |
| 12 | ver_nodo | `{"id": "Obligacion_descripcion_detallada_del_calculo"}` | 517 | 517 | SÍ |
| 13 | buscar_nodos | `{"consulta": "exigencia capital total componentes riesgo crédito mercado operacional", "li` | 3296 | 3296 | SÍ |
| 14 | buscar_nodos | `{"consulta": "determinación exigencia capital mínimo metodología", "limite": 10}` | 3154 | 3154 | SÍ |
| 15 | buscar_nodos | `{"consulta": "exigencia capital máximo mayor entre riesgo crédito mercado operacional", "l` | 3338 | 3338 | SÍ |

**Fidelidad: 15/15** (igualdad de largos del output completo).

## Apéndice — outputs completos re-ejecutados

### paso 1 — buscar_nodos {"consulta": "capital mínimo exigencia entidad financiera", "limite": 10}

```json
{
 "consulta": "capital mínimo exigencia entidad financiera",
 "total_con_match": 539,
 "resultados": [
  {
   "id": "Restriccion_los_bancos_deberan_mantener_una_exigencia_basica_de_capital_minimo_de_5_000_mill",
   "type": "Restriccion",
   "label": "Exigencia básica bancos",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Los bancos deberán mantener una exigencia básica de capital mínimo de 5.000 millones de pesos"
  },
  {
   "id": "Restriccion_cuando_la_suma_de_los_requisitos_de_capital_de_una_entidad_financiera_por_las_ex",
   "type": "Restriccion",
   "label": "Límite requisito capital QCCP",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Cuando la suma de los requisitos de capital de una entidad financiera por las exposiciones con una QCCP sea mayor que la exigencia resultante de la aplicación d…"
  },
  {
   "id": "Obligacion_la_ccp_la_entidad_financiera_la_autoridad_de_control_de_la_ccp_u_otro_organismo_",
   "type": "Obligacion",
   "label": "Calcular requerimiento capital",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La CCP, la entidad financiera, la autoridad de control de la CCP u otro organismo con acceso a los datos requeridos deberá calcular K_CMi, DF_pref y DF_CCP de f…"
  },
  {
   "id": "Obligacion_la_entidad_debera_encuadrarse_en_la_exigencia_a_mas_tardar_en_el_segundo_mes_sig",
   "type": "Obligacion",
   "label": "Encuadrarse en exigencia capital",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La entidad deberá encuadrarse en la exigencia a más tardar en el segundo mes siguiente a aquel en que se registre el incumplimiento"
  },
  {
   "id": "Obligacion_si_la_entidad_financiera_carece_de_suficiente_capital_para_efectuar_la_deduccion",
   "type": "Obligacion",
   "label": "Deducir remanente nivel superior",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Si la entidad financiera carece de suficiente capital para efectuar la deducción de un nivel particular de capital, el remanente se deducirá del nivel inmediato…"
  },
  {
   "id": "Operacion_calculo_de_exigencia_de_capital_minimo_por_riesgo_de_credito",
   "type": "Operacion",
   "label": "Cálculo exigencia capital mínimo",
   "tokens_matcheados": 3,
   "resumen_propiedades": "tipo: cálculo de exigencia de capital mínimo por riesgo de crédito"
  },
  {
   "id": "Obligacion_la_entidad_financiera_podra_rescatarlos_transcurridos_un_minimo_de_cinco_anos_de",
   "type": "Obligacion",
   "label": "Obtener autorización para rescate",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La entidad financiera podrá rescatarlos –transcurridos un mínimo de cinco años desde su emisión–, siempre que cuente con autorización de la SEFyC en forma previ…"
  },
  {
   "id": "Restriccion_la_exigencia_determinada_a_traves_de_la_aplicacion_de_la_expresion_descripta_en_",
   "type": "Restriccion",
   "label": "Límite 20% grupo A capital mínimo",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La exigencia determinada a través de la aplicación de la expresión descripta en el punto 7.2. no podrá superar el 20% en el caso de entidades del grupo A del pr…"
  },
  {
   "id": "Restriccion_las_restantes_entidades_deberan_mantener_una_exigencia_basica_de_capital_minimo_",
   "type": "Restriccion",
   "label": "Exigencia básica restantes entidades",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Las restantes entidades deberán mantener una exigencia básica de capital mínimo de 2.500 millones de pesos"
  },
  {
   "id": "Excepcion_si_la_entidad_financiera_carece_de_suficiente_capital_para_efectuar_la_deduccion",
   "type": "Excepcion",
   "label": "Remanente trasferido a nivel superior",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Si la entidad financiera carece de suficiente capital para efectuar la deducción de un nivel particular de capital, el remanente se deducirá del nivel inmediato…"
  }
 ]
}
```

### paso 2 — buscar_nodos {"consulta": "riesgo operacional cálculo componente", "limite": 10}

```json
{
 "consulta": "riesgo operacional cálculo componente",
 "total_con_match": 236,
 "resultados": [
  {
   "id": "Operacion_calculo_de_promedio_de_exigencias_de_riesgo_operacional",
   "type": "Operacion",
   "label": "Cálculo promedio ERC",
   "tokens_matcheados": 3,
   "resumen_propiedades": "tipo: cálculo de promedio de exigencias de riesgo operacional"
  },
  {
   "id": "Restriccion_las_exigencias_a_ser_incluidas_dentro_del_calculo_del_promedio_de_erc_se_extiend",
   "type": "Restriccion",
   "label": "Límite exigencia riesgo operacional",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Las exigencias a ser incluidas dentro del cálculo del promedio de ERC se extienden únicamente hasta la que correspondió ser integrada en febrero 2013 (promedios…"
  },
  {
   "id": "Operacion_calculo",
   "type": "Operacion",
   "label": "Cálculo exigencia capital riesgo operacional",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Cálculo de K (exigencia de capital promedio de las exposiciones subyacentes); es decir, el ratio entre la suma de las exposiciones subyacentes ponderadas por ri…"
  },
  {
   "id": "Operacion_calculo_de_capital_minimo_por_riesgo_operacional",
   "type": "Operacion",
   "label": "Cálculo exigencia capital mínimo operacional",
   "tokens_matcheados": 3,
   "resumen_propiedades": "tipo: cálculo de capital mínimo por riesgo operacional"
  },
  {
   "id": "Obligacion_exigencia_por_riesgo_de_credito_de_contraparte_en_operaciones_con_derivados_extr",
   "type": "Obligacion",
   "label": "Cálculo de RCD",
   "tokens_matcheados": 2,
   "resumen_propiedades": "exigencia por riesgo de crédito de contraparte en operaciones con derivados extrabursátiles (over-the-counter, OTC), determinada conforme a lo establecido en el…"
  },
  {
   "id": "Obligacion_se_determinara_mensualmente_la_exigencia_de_capital_por_riesgo_operacional_cro_m",
   "type": "Obligacion",
   "label": "Informar CRO mensualmente",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Se determinará mensualmente la exigencia de capital por riesgo operacional (CRO) mediante la expresión CRO = BIC x ILM para entidades del Grupo 1"
  },
  {
   "id": "Operacion_calculo_mensual_de_exigencia_operacional",
   "type": "Operacion",
   "label": "Determinación mensual CRO",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: cálculo mensual de exigencia operacional"
  },
  {
   "id": "Obligacion_aplicar_exigencia_capital_por_riesgo_general_mercado_a_todas_posiciones_derivado",
   "type": "Obligacion",
   "label": "Cálculo riesgo general mercado",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La exigencia de capital por el riesgo general de mercado alcanza a todas las posiciones en instrumentos derivados -de la misma manera que también alcanza a las …"
  },
  {
   "id": "Operacion_calculo_de_ponderadores_de_riesgo_para_inversiones_en_fondos",
   "type": "Operacion",
   "label": "Ponderación de riesgo en fondos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: cálculo de ponderadores de riesgo para inversiones en fondos"
  },
  {
   "id": "Operacion_calculo_de_riesgo_de_tasa_de_interes",
   "type": "Operacion",
   "label": "Cálculo riesgo tasa interés EVE",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Cálculo del riesgo de tasa de interés en la cartera de inversión - Medida de riesgo EVE estandarizada (Sección 11.) en base individual y consolidado mensual (có…"
  }
 ]
}
```

### paso 3 — ver_nodo {"id": "Operacion_calculo_de_exigencia_de_capital_minimo_por_riesgo_de_credito"}

```json
{
 "id": "Operacion_calculo_de_exigencia_de_capital_minimo_por_riesgo_de_credito",
 "type": "Operacion",
 "label": "Cálculo exigencia capital mínimo",
 "properties": {
  "tipo": "cálculo de exigencia de capital mínimo por riesgo de crédito"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Punto 7.3. Límite para las entidades del grupo 2."
  }
 ]
}
```

### paso 4 — ver_nodo {"id": "Operacion_calculo_de_capital_minimo_por_riesgo_operacional"}

```json
{
 "id": "Operacion_calculo_de_capital_minimo_por_riesgo_operacional",
 "type": "Operacion",
 "label": "Cálculo exigencia capital mínimo operacional",
 "properties": {
  "tipo": "cálculo de capital mínimo por riesgo operacional"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Punto 7.4. Nuevas entidades."
  }
 ]
}
```

### paso 5 — buscar_nodos {"consulta": "primer mes funcionamiento riesgo operacional", "limite": 10}

```json
{
 "consulta": "primer mes funcionamiento riesgo operacional",
 "total_con_match": 202,
 "resultados": [
  {
   "id": "Operacion_calculo_de_promedio_de_exigencias_de_riesgo_operacional",
   "type": "Operacion",
   "label": "Cálculo promedio ERC",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: cálculo de promedio de exigencias de riesgo operacional"
  },
  {
   "id": "Obligacion_se_determinara_mensualmente_la_exigencia_de_capital_por_riesgo_operacional_cro_m",
   "type": "Obligacion",
   "label": "Informar CRO mensualmente",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Se determinará mensualmente la exigencia de capital por riesgo operacional (CRO) mediante la expresión CRO = BIC x ILM para entidades del Grupo 1"
  },
  {
   "id": "Restriccion_las_exigencias_a_ser_incluidas_dentro_del_calculo_del_promedio_de_erc_se_extiend",
   "type": "Restriccion",
   "label": "Límite exigencia riesgo operacional",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Las exigencias a ser incluidas dentro del cálculo del promedio de ERC se extienden únicamente hasta la que correspondió ser integrada en febrero 2013 (promedios…"
  },
  {
   "id": "Operacion_calculo",
   "type": "Operacion",
   "label": "Cálculo exigencia capital riesgo operacional",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Cálculo de K (exigencia de capital promedio de las exposiciones subyacentes); es decir, el ratio entre la suma de las exposiciones subyacentes ponderadas por ri…"
  },
  {
   "id": "Operacion_calculo_de_capital_minimo_por_riesgo_operacional",
   "type": "Operacion",
   "label": "Cálculo exigencia capital mínimo operacional",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: cálculo de capital mínimo por riesgo operacional"
  },
  {
   "id": "Restriccion_la_exigencia_de_capital_por_riesgo_operacional_para_entidades_del_grupo_b_determ",
   "type": "Restriccion",
   "label": "Límite exigencia capital operacional grupo B",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La exigencia de capital por riesgo operacional para entidades del grupo B determinada a través de la aplicación de la expresión descripta en el punto 7.2. hasta…"
  },
  {
   "id": "Restriccion_la_exigencia_de_capital_por_riesgo_operacional_para_entidades_del_grupo_c_determ",
   "type": "Restriccion",
   "label": "Límite exigencia capital operacional grupo C",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La exigencia de capital por riesgo operacional para entidades del grupo C determinada a través de la aplicación de la expresión descripta en el punto 7.2. hasta…"
  },
  {
   "id": "Restriccion_la_exigencia_mensual_de_capital_minimo_por_riesgo_operacional_de_las_entidades_f",
   "type": "Restriccion",
   "label": "Exigencia capital mínimo por riesgo operacional",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La exigencia mensual de capital mínimo por riesgo operacional de las entidades financieras de los grupos 1 y 2 correspondiente al primer mes será equivalente al…"
  },
  {
   "id": "Obligacion_exigencia_por_riesgo_de_credito_de_contraparte_en_operaciones_con_derivados_extr",
   "type": "Obligacion",
   "label": "Cálculo de RCD",
   "tokens_matcheados": 1,
   "resumen_propiedades": "exigencia por riesgo de crédito de contraparte en operaciones con derivados extrabursátiles (over-the-counter, OTC), determinada conforme a lo establecido en el…"
  },
  {
   "id": "Restriccion_la_parte_de_la_exposicion_cubierta_recibira_el_ponderador_de_riesgo_correspondie",
   "type": "Restriccion",
   "label": "Ponderador mínimo 20%",
   "tokens_matcheados": 1,
   "resumen_propiedades": "La parte de la exposición cubierta recibirá el ponderador de riesgo correspondiente al activo recibido en garantía, pero estará sujeta a un mínimo del 20% –salv…"
  }
 ]
}
```

### paso 6 — ver_nodo {"id": "Restriccion_la_exigencia_mensual_de_capital_minimo_por_riesgo_operacional_de_las_entidades_f"}

```json
{
 "id": "Restriccion_la_exigencia_mensual_de_capital_minimo_por_riesgo_operacional_de_las_entidades_f",
 "type": "Restriccion",
 "label": "Exigencia capital mínimo por riesgo operacional",
 "properties": {
  "descripcion": "La exigencia mensual de capital mínimo por riesgo operacional de las entidades financieras de los grupos 1 y 2 correspondiente al primer mes será equivalente al 10% de la sumatoria de las exigencias determinadas por los riesgos de crédito y de mercado –en este caso, para las posiciones del último día– de ese mes.",
  "tipo": "limite_cuantitativo",
  "umbral": "10%"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Punto 7.4. Nuevas entidades."
  }
 ]
}
```

### paso 7 — ver_vecinos {"id": "Operacion_calculo_de_capital_minimo_por_riesgo_operacional", "direccion": "ambas"}

```json
{
 "id": "Operacion_calculo_de_capital_minimo_por_riesgo_operacional",
 "label": "Cálculo exigencia capital mínimo operacional",
 "n_salientes_total": 0,
 "n_entrantes_total": 3,
 "salientes": [],
 "salientes_truncado": false,
 "entrantes": [
  {
   "relation": "limita",
   "vecino_id": "Restriccion_la_exigencia_mensual_de_capital_minimo_por_riesgo_operacional_de_las_entidades_f",
   "vecino_label": "Exigencia capital mínimo por riesgo operacional",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 7.4. Nuevas entidades."
    }
   ]
  },
  {
   "relation": "limita",
   "vecino_id": "Restriccion_a_partir_del_segundo_y_hasta_el_trigesimo_sexto_mes_la_exigencia_mensual_sera_eq",
   "vecino_label": "Exigencia capital segundo a trigésimo sexto mes",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 7.4. Nuevas entidades."
    }
   ]
  },
  {
   "relation": "limita",
   "vecino_id": "Restriccion_desde_el_trigesimo_septimo_mes_la_exigencia_mensual_se_calculara_de_acuerdo_con_",
   "vecino_label": "Metodología cálculo desde trigésimo séptimo mes",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 7.4. Nuevas entidades."
    }
   ]
  }
 ],
 "entrantes_truncado": false
}
```

### paso 8 — buscar_nodos {"consulta": "exigencia capital total determinación cálculo", "limite": 10}

```json
{
 "consulta": "exigencia capital total determinación cálculo",
 "total_con_match": 341,
 "resultados": [
  {
   "id": "Operacion_calculo_de_exigencia_capital_por_riesgo_cambiario",
   "type": "Operacion",
   "label": "Determinación de exigencia riesgo tipo de cambio",
   "tokens_matcheados": 4,
   "resumen_propiedades": "tipo: cálculo de exigencia capital por riesgo cambiario"
  },
  {
   "id": "Operacion_calculo_de_exigencia_capital_por_opciones",
   "type": "Operacion",
   "label": "Determinación de exigencia riesgo posiciones opciones",
   "tokens_matcheados": 4,
   "resumen_propiedades": "tipo: cálculo de exigencia capital por opciones"
  },
  {
   "id": "Operacion_calculo_de_exigencia_capital_por_riesgo_general",
   "type": "Operacion",
   "label": "Determinación de exigencia riesgo general tasa interés",
   "tokens_matcheados": 4,
   "resumen_propiedades": "tipo: cálculo de exigencia capital por riesgo general"
  },
  {
   "id": "Operacion_calculo_de_exigencia_capital_por_riesgo_especifico",
   "type": "Operacion",
   "label": "Determinación de exigencia riesgo específico tasa interés",
   "tokens_matcheados": 4,
   "resumen_propiedades": "tipo: cálculo de exigencia capital por riesgo específico"
  },
  {
   "id": "Operacion_calculo_mensual_de_exigencia_operacional",
   "type": "Operacion",
   "label": "Determinación mensual CRO",
   "tokens_matcheados": 3,
   "resumen_propiedades": "tipo: cálculo mensual de exigencia operacional"
  },
  {
   "id": "Obligacion_aplicar_exigencia_capital_por_riesgo_general_mercado_a_todas_posiciones_derivado",
   "type": "Obligacion",
   "label": "Cálculo riesgo general mercado",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La exigencia de capital por el riesgo general de mercado alcanza a todas las posiciones en instrumentos derivados -de la misma manera que también alcanza a las …"
  },
  {
   "id": "Operacion_calculo_de_capital",
   "type": "Operacion",
   "label": "Cálculo de exigencia de capital",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Cálculo de las exigencias de capital para posiciones de titulización utilizando el enfoque estandarizado"
  },
  {
   "id": "Operacion_calculo_de_exigencia",
   "type": "Operacion",
   "label": "Cálculo de exigencia de capital",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Cálculo del importe correspondiente al mes n considerando exigencia de riesgo de crédito, riesgo de mercado, riesgo operacional, responsabilidad patrimonial com…"
  },
  {
   "id": "Operacion_calculo_de_requerimiento_regulatorio",
   "type": "Operacion",
   "label": "Determinación de capital mínimo",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Determinación del cumplimiento de la exigencia de capital mínimo en función de la responsabilidad patrimonial computable"
  },
  {
   "id": "Operacion_calculo_de_exigencia_de_capital_minimo_por_riesgo_de_credito",
   "type": "Operacion",
   "label": "Cálculo exigencia capital mínimo",
   "tokens_matcheados": 3,
   "resumen_propiedades": "tipo: cálculo de exigencia de capital mínimo por riesgo de crédito"
  }
 ]
}
```

### paso 9 — ver_nodo {"id": "Operacion_calculo_de_exigencia"}

```json
{
 "id": "Operacion_calculo_de_exigencia",
 "type": "Operacion",
 "label": "Cálculo de exigencia de capital",
 "properties": {
  "tipo": "cálculo de exigencia",
  "description": "Cálculo del importe correspondiente al mes n considerando exigencia de riesgo de crédito, riesgo de mercado, riesgo operacional, responsabilidad patrimonial computable y franquicia informada"
 },
 "provenances": [
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Punto 7.1. Normas de procedimiento"
  }
 ]
}
```

### paso 10 — ver_vecinos {"id": "Operacion_calculo_de_exigencia", "direccion": "ambas"}

```json
{
 "id": "Operacion_calculo_de_exigencia",
 "label": "Cálculo de exigencia de capital",
 "n_salientes_total": 0,
 "n_entrantes_total": 1,
 "salientes": [],
 "salientes_truncado": false,
 "entrantes": [
  {
   "relation": "regula",
   "vecino_id": "Obligacion_descripcion_detallada_del_calculo",
   "vecino_label": "Descripción detallada del cálculo",
   "provenances": [
    {
     "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
     "location": "Punto 7.1. Normas de procedimiento"
    }
   ]
  }
 ],
 "entrantes_truncado": false
}
```

### paso 11 — buscar_nodos {"consulta": "exigencia capital riesgo crédito mercado operacional suma", "limite": 10}

```json
{
 "consulta": "exigencia capital riesgo crédito mercado operacional suma",
 "total_con_match": 563,
 "resultados": [
  {
   "id": "Obligacion_se_determinara_mensualmente_la_exigencia_de_capital_por_riesgo_operacional_cro_m",
   "type": "Obligacion",
   "label": "Informar CRO mensualmente",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Se determinará mensualmente la exigencia de capital por riesgo operacional (CRO) mediante la expresión CRO = BIC x ILM para entidades del Grupo 1"
  },
  {
   "id": "Obligacion_aplicar_exigencia_capital_por_riesgo_general_mercado_a_todas_posiciones_derivado",
   "type": "Obligacion",
   "label": "Cálculo riesgo general mercado",
   "tokens_matcheados": 4,
   "resumen_propiedades": "La exigencia de capital por el riesgo general de mercado alcanza a todas las posiciones en instrumentos derivados -de la misma manera que también alcanza a las …"
  },
  {
   "id": "Operacion_calculo_de_exigencia_de_capital_minimo_por_riesgo_de_credito",
   "type": "Operacion",
   "label": "Cálculo exigencia capital mínimo",
   "tokens_matcheados": 4,
   "resumen_propiedades": "tipo: cálculo de exigencia de capital mínimo por riesgo de crédito"
  },
  {
   "id": "Operacion_calculo_de_exigencia_de_capital_por_riesgo_de_credito_de_contraparte",
   "type": "Operacion",
   "label": "Operación de cálculo de exigencia capital",
   "tokens_matcheados": 4,
   "resumen_propiedades": "tipo: cálculo de exigencia de capital por riesgo de crédito de contraparte"
  },
  {
   "id": "Operacion_calculo_de_capital_minimo",
   "type": "Operacion",
   "label": "Cálculo de exigencia por riesgo de crédito",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Determinación de la exigencia de capital por riesgo de crédito conforme a la fórmula C_RC = (k x 0,08 x APR_c) + INC"
  },
  {
   "id": "Operacion_medicion_de_capital_minimo",
   "type": "Operacion",
   "label": "Medición de exigencia por riesgo de mercado",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Medición de la exigencia por riesgo de mercado conforme a lo dispuesto en el punto 6.10"
  },
  {
   "id": "Operacion_calculo",
   "type": "Operacion",
   "label": "Cálculo exigencia capital riesgo operacional",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Cálculo de K (exigencia de capital promedio de las exposiciones subyacentes); es decir, el ratio entre la suma de las exposiciones subyacentes ponderadas por ri…"
  },
  {
   "id": "Operacion_calculo_de_capital_minimo_por_riesgo_operacional",
   "type": "Operacion",
   "label": "Cálculo exigencia capital mínimo operacional",
   "tokens_matcheados": 4,
   "resumen_propiedades": "tipo: cálculo de capital mínimo por riesgo operacional"
  },
  {
   "id": "Restriccion_la_exigencia_de_capital_por_riesgo_operacional_para_entidades_del_grupo_b_determ",
   "type": "Restriccion",
   "label": "Límite exigencia capital operacional grupo B",
   "tokens_matcheados": 4,
   "resumen_propiedades": "La exigencia de capital por riesgo operacional para entidades del grupo B determinada a través de la aplicación de la expresión descripta en el punto 7.2. hasta…"
  },
  {
   "id": "Restriccion_la_exigencia_de_capital_por_riesgo_operacional_para_entidades_del_grupo_c_determ",
   "type": "Restriccion",
   "label": "Límite exigencia capital operacional grupo C",
   "tokens_matcheados": 4,
   "resumen_propiedades": "La exigencia de capital por riesgo operacional para entidades del grupo C determinada a través de la aplicación de la expresión descripta en el punto 7.2. hasta…"
  }
 ]
}
```

### paso 12 — ver_nodo {"id": "Obligacion_descripcion_detallada_del_calculo"}

```json
{
 "id": "Obligacion_descripcion_detallada_del_calculo",
 "type": "Obligacion",
 "label": "Descripción detallada del cálculo",
 "properties": {
  "tipo": "presentacion_informativa",
  "description": "Se agregará una descripción detallada del cálculo de la franquicia para el período informado, a partir de lo dispuesto en la Resolución o nota a que se hace referencia",
  "plazo": "mensual"
 },
 "provenances": [
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Punto 7.1. Normas de procedimiento"
  }
 ]
}
```

### paso 13 — buscar_nodos {"consulta": "exigencia capital total componentes riesgo crédito mercado operacional", "limite": 10}

```json
{
 "consulta": "exigencia capital total componentes riesgo crédito mercado operacional",
 "total_con_match": 590,
 "resultados": [
  {
   "id": "Obligacion_se_determinara_mensualmente_la_exigencia_de_capital_por_riesgo_operacional_cro_m",
   "type": "Obligacion",
   "label": "Informar CRO mensualmente",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Se determinará mensualmente la exigencia de capital por riesgo operacional (CRO) mediante la expresión CRO = BIC x ILM para entidades del Grupo 1"
  },
  {
   "id": "Obligacion_aplicar_exigencia_capital_por_riesgo_general_mercado_a_todas_posiciones_derivado",
   "type": "Obligacion",
   "label": "Cálculo riesgo general mercado",
   "tokens_matcheados": 4,
   "resumen_propiedades": "La exigencia de capital por el riesgo general de mercado alcanza a todas las posiciones en instrumentos derivados -de la misma manera que también alcanza a las …"
  },
  {
   "id": "Operacion_calculo_de_exigencia_de_capital_minimo_por_riesgo_de_credito",
   "type": "Operacion",
   "label": "Cálculo exigencia capital mínimo",
   "tokens_matcheados": 4,
   "resumen_propiedades": "tipo: cálculo de exigencia de capital mínimo por riesgo de crédito"
  },
  {
   "id": "Operacion_calculo_de_exigencia_de_capital_por_riesgo_de_credito_de_contraparte",
   "type": "Operacion",
   "label": "Operación de cálculo de exigencia capital",
   "tokens_matcheados": 4,
   "resumen_propiedades": "tipo: cálculo de exigencia de capital por riesgo de crédito de contraparte"
  },
  {
   "id": "Operacion_calculo_de_capital_minimo",
   "type": "Operacion",
   "label": "Cálculo de exigencia por riesgo de crédito",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Determinación de la exigencia de capital por riesgo de crédito conforme a la fórmula C_RC = (k x 0,08 x APR_c) + INC"
  },
  {
   "id": "Operacion_medicion_de_capital_minimo",
   "type": "Operacion",
   "label": "Medición de exigencia por riesgo de mercado",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Medición de la exigencia por riesgo de mercado conforme a lo dispuesto en el punto 6.10"
  },
  {
   "id": "Obligacion_calcular_exigencia_total_capital_riesgo_vega",
   "type": "Obligacion",
   "label": "Calcular exigencia total capital riesgo vega",
   "tokens_matcheados": 4,
   "resumen_propiedades": "La exigencia total de capital por riesgo vega será la suma del valor absoluto de las exigencias de capital individual que se hayan calculado para dicho riesgo"
  },
  {
   "id": "Operacion_calculo",
   "type": "Operacion",
   "label": "Cálculo exigencia capital riesgo operacional",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Cálculo de K (exigencia de capital promedio de las exposiciones subyacentes); es decir, el ratio entre la suma de las exposiciones subyacentes ponderadas por ri…"
  },
  {
   "id": "Operacion_calculo_de_capital_minimo_por_riesgo_operacional",
   "type": "Operacion",
   "label": "Cálculo exigencia capital mínimo operacional",
   "tokens_matcheados": 4,
   "resumen_propiedades": "tipo: cálculo de capital mínimo por riesgo operacional"
  },
  {
   "id": "Restriccion_la_exigencia_de_capital_por_riesgo_operacional_para_entidades_del_grupo_b_determ",
   "type": "Restriccion",
   "label": "Límite exigencia capital operacional grupo B",
   "tokens_matcheados": 4,
   "resumen_propiedades": "La exigencia de capital por riesgo operacional para entidades del grupo B determinada a través de la aplicación de la expresión descripta en el punto 7.2. hasta…"
  }
 ]
}
```

### paso 14 — buscar_nodos {"consulta": "determinación exigencia capital mínimo metodología", "limite": 10}

```json
{
 "consulta": "determinación exigencia capital mínimo metodología",
 "total_con_match": 332,
 "resultados": [
  {
   "id": "Restriccion_los_bancos_deberan_mantener_una_exigencia_basica_de_capital_minimo_de_5_000_mill",
   "type": "Restriccion",
   "label": "Exigencia básica bancos",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Los bancos deberán mantener una exigencia básica de capital mínimo de 5.000 millones de pesos"
  },
  {
   "id": "Operacion_calculo_de_requerimiento_regulatorio",
   "type": "Operacion",
   "label": "Determinación de capital mínimo",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Determinación del cumplimiento de la exigencia de capital mínimo en función de la responsabilidad patrimonial computable"
  },
  {
   "id": "Operacion_calculo_de_exigencia_de_capital_minimo_por_riesgo_de_credito",
   "type": "Operacion",
   "label": "Cálculo exigencia capital mínimo",
   "tokens_matcheados": 3,
   "resumen_propiedades": "tipo: cálculo de exigencia de capital mínimo por riesgo de crédito"
  },
  {
   "id": "Restriccion_la_exigencia_determinada_a_traves_de_la_aplicacion_de_la_expresion_descripta_en_",
   "type": "Restriccion",
   "label": "Límite 20% grupo A capital mínimo",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La exigencia determinada a través de la aplicación de la expresión descripta en el punto 7.2. no podrá superar el 20% en el caso de entidades del grupo A del pr…"
  },
  {
   "id": "Restriccion_las_restantes_entidades_deberan_mantener_una_exigencia_basica_de_capital_minimo_",
   "type": "Restriccion",
   "label": "Exigencia básica restantes entidades",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Las restantes entidades deberán mantener una exigencia básica de capital mínimo de 2.500 millones de pesos"
  },
  {
   "id": "Operacion_calculo_de_capital_minimo",
   "type": "Operacion",
   "label": "Cálculo de exigencia por riesgo de crédito",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Determinación de la exigencia de capital por riesgo de crédito conforme a la fórmula C_RC = (k x 0,08 x APR_c) + INC"
  },
  {
   "id": "Operacion_medicion_de_capital_minimo",
   "type": "Operacion",
   "label": "Medición de exigencia por riesgo de mercado",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Medición de la exigencia por riesgo de mercado conforme a lo dispuesto en el punto 6.10"
  },
  {
   "id": "Operacion_calculo_de_capital_minimo_por_riesgo_operacional",
   "type": "Operacion",
   "label": "Cálculo exigencia capital mínimo operacional",
   "tokens_matcheados": 3,
   "resumen_propiedades": "tipo: cálculo de capital mínimo por riesgo operacional"
  },
  {
   "id": "Restriccion_la_exigencia_mensual_de_capital_minimo_por_riesgo_operacional_de_las_entidades_f",
   "type": "Restriccion",
   "label": "Exigencia capital mínimo por riesgo operacional",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La exigencia mensual de capital mínimo por riesgo operacional de las entidades financieras de los grupos 1 y 2 correspondiente al primer mes será equivalente al…"
  },
  {
   "id": "Operacion_calculo_de_exigencia_capital_por_riesgo_cambiario",
   "type": "Operacion",
   "label": "Determinación de exigencia riesgo tipo de cambio",
   "tokens_matcheados": 3,
   "resumen_propiedades": "tipo: cálculo de exigencia capital por riesgo cambiario"
  }
 ]
}
```

### paso 15 — buscar_nodos {"consulta": "exigencia capital máximo mayor entre riesgo crédito mercado operacional", "limite": 10}

```json
{
 "consulta": "exigencia capital máximo mayor entre riesgo crédito mercado operacional",
 "total_con_match": 637,
 "resultados": [
  {
   "id": "Obligacion_se_determinara_mensualmente_la_exigencia_de_capital_por_riesgo_operacional_cro_m",
   "type": "Obligacion",
   "label": "Informar CRO mensualmente",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Se determinará mensualmente la exigencia de capital por riesgo operacional (CRO) mediante la expresión CRO = BIC x ILM para entidades del Grupo 1"
  },
  {
   "id": "Obligacion_aplicar_exigencia_capital_por_riesgo_general_mercado_a_todas_posiciones_derivado",
   "type": "Obligacion",
   "label": "Cálculo riesgo general mercado",
   "tokens_matcheados": 4,
   "resumen_propiedades": "La exigencia de capital por el riesgo general de mercado alcanza a todas las posiciones en instrumentos derivados -de la misma manera que también alcanza a las …"
  },
  {
   "id": "Operacion_calculo_de_exigencia_de_capital_minimo_por_riesgo_de_credito",
   "type": "Operacion",
   "label": "Cálculo exigencia capital mínimo",
   "tokens_matcheados": 4,
   "resumen_propiedades": "tipo: cálculo de exigencia de capital mínimo por riesgo de crédito"
  },
  {
   "id": "Operacion_calculo_de_exigencia_de_capital_por_riesgo_de_credito_de_contraparte",
   "type": "Operacion",
   "label": "Operación de cálculo de exigencia capital",
   "tokens_matcheados": 4,
   "resumen_propiedades": "tipo: cálculo de exigencia de capital por riesgo de crédito de contraparte"
  },
  {
   "id": "Operacion_calculo_de_capital_minimo",
   "type": "Operacion",
   "label": "Cálculo de exigencia por riesgo de crédito",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Determinación de la exigencia de capital por riesgo de crédito conforme a la fórmula C_RC = (k x 0,08 x APR_c) + INC"
  },
  {
   "id": "Operacion_medicion_de_capital_minimo",
   "type": "Operacion",
   "label": "Medición de exigencia por riesgo de mercado",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Medición de la exigencia por riesgo de mercado conforme a lo dispuesto en el punto 6.10"
  },
  {
   "id": "Operacion_calculo",
   "type": "Operacion",
   "label": "Cálculo exigencia capital riesgo operacional",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Cálculo de K (exigencia de capital promedio de las exposiciones subyacentes); es decir, el ratio entre la suma de las exposiciones subyacentes ponderadas por ri…"
  },
  {
   "id": "Operacion_calculo_de_capital_minimo_por_riesgo_operacional",
   "type": "Operacion",
   "label": "Cálculo exigencia capital mínimo operacional",
   "tokens_matcheados": 4,
   "resumen_propiedades": "tipo: cálculo de capital mínimo por riesgo operacional"
  },
  {
   "id": "Restriccion_la_exigencia_de_capital_por_riesgo_operacional_para_entidades_del_grupo_b_determ",
   "type": "Restriccion",
   "label": "Límite exigencia capital operacional grupo B",
   "tokens_matcheados": 4,
   "resumen_propiedades": "La exigencia de capital por riesgo operacional para entidades del grupo B determinada a través de la aplicación de la expresión descripta en el punto 7.2. hasta…"
  },
  {
   "id": "Restriccion_la_exigencia_de_capital_por_riesgo_operacional_para_entidades_del_grupo_c_determ",
   "type": "Restriccion",
   "label": "Límite exigencia capital operacional grupo C",
   "tokens_matcheados": 4,
   "resumen_propiedades": "La exigencia de capital por riesgo operacional para entidades del grupo C determinada a través de la aplicación de la expresión descripta en el punto 7.2. hasta…"
  }
 ]
}
```



---

# CQN-013

## Respuesta final íntegra (trace.final_json)

```json
{
 "respuesta": "Un sujeto obligado que incumple las normas sobre protección de los usuarios de servicios financieros enfrenta las siguientes consecuencias sancionatorias: será pasible de la aplicación de las sanciones previstas en las normas sobre 'Régimen disciplinario a cargo del Banco Central de la República Argentina' conforme a las Leyes 21.526 y 25.065, así como en la tramitación de sumarios cambiarios según la Ley 19.359. Adicionalmente, los incumplimientos en el envío de información estarán sujetos a la aplicación del artículo 41 de la Ley de Entidades Financieras.",
 "citas": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "Punto 4.4. Actuaciones de oficio."
  }
 ],
 "respondible": true
}
```

(`respondible`: true · tool_calls_used: 15 · hit_tool_limit: True)

## Inventario de pasos + fidelidad runtime↔re-ejecución

| paso | tool | input | output_chars (runtime) | re-ejecutado | fiel |
|---|---|---|---|---|---|
| 1 | buscar_nodos | `{"consulta": "consecuencias sancionatorias incumplimiento protección usuarios servicios fi` | 3858 | 3858 | SÍ |
| 2 | buscar_nodos | `{"consulta": "sanciones sujeto obligado usuarios financieros", "limite": 10}` | 3407 | 3407 | SÍ |
| 3 | buscar_nodos | `{"consulta": "sanciones régimen sancionatorio incumplimiento", "limite": 10}` | 3327 | 3327 | SÍ |
| 4 | buscar_nodos | `{"consulta": "multa apercibimiento sanción BCRA", "limite": 10}` | 2903 | 2903 | SÍ |
| 5 | ver_nodo | `{"id": "Obligacion_aplicacion_de_sanciones_por_incumplimiento"}` | 783 | 783 | SÍ |
| 6 | buscar_nodos | `{"consulta": "régimen disciplinario Banco Central", "limite": 10}` | 2836 | 2836 | SÍ |
| 7 | buscar_nodos | `{"consulta": "Leyes 21.526 25.065 régimen disciplinario", "limite": 10}` | 3367 | 3367 | SÍ |
| 8 | buscar_nodos | `{"consulta": "multa apercibimiento amonestación sanción disciplinaria", "limite": 10}` | 800 | 800 | SÍ |
| 9 | buscar_nodos | `{"consulta": "sumarios cambiarios Ley 19.359", "limite": 10}` | 2974 | 2974 | SÍ |
| 10 | ver_nodo | `{"id": "Restriccion_los_incumplimientos_a_esta_normativa_se_encontraran_alcanzados_por_la_` | 508 | 508 | SÍ |
| 11 | ver_nodo | `{"id": "Restriccion_los_incumplimientos_en_el_envio_de_la_informacion_estaran_sujetos_a_la` | 541 | 541 | SÍ |
| 12 | buscar_nodos | `{"consulta": "artículo 41 Ley Entidades Financieras", "limite": 10}` | 3248 | 3248 | SÍ |
| 13 | buscar_nodos | `{"consulta": "protección usuarios financieros sanciones consecuencias", "limite": 10}` | 3736 | 3736 | SÍ |
| 14 | ver_nodo | `{"id": "TextoOrdenado_to_proteccion_usuarios_servicios_financieros_actual_pdf"}` | 434 | 434 | SÍ |
| 15 | ver_vecinos | `{"id": "Obligacion_aplicacion_de_sanciones_por_incumplimiento", "direccion": "ambas"}` | 811 | 811 | SÍ |

**Fidelidad: 15/15** (igualdad de largos del output completo).

## Apéndice — outputs completos re-ejecutados

### paso 1 — buscar_nodos {"consulta": "consecuencias sancionatorias incumplimiento protección usuarios servicios financieros", "limite": 10}

```json
{
 "consulta": "consecuencias sancionatorias incumplimiento protección usuarios servicios financieros",
 "total_con_match": 188,
 "resultados": [
  {
   "id": "TextoOrdenado_to_proteccion_usuarios_servicios_financieros_actual_pdf",
   "type": "TextoOrdenado",
   "label": "Protección de Usuarios",
   "tokens_matcheados": 4,
   "resumen_propiedades": "materia: Protección de los usuarios de servicios financieros; archivo: TO_proteccion_usuarios_servicios_financieros_actual.pdf; version: 8a"
  },
  {
   "id": "EntidadFinanciera_usuario_de_servicio_financiero",
   "type": "EntidadFinanciera",
   "label": "Usuarios de servicios financieros",
   "tokens_matcheados": 3,
   "resumen_propiedades": "categoria: usuario de servicio financiero"
  },
  {
   "id": "Obligacion_la_gerencia_principal_de_proteccion_al_usuario_de_servicios_financieros_tramitar",
   "type": "Obligacion",
   "label": "Tramitar denuncias de asociaciones",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La Gerencia Principal de Protección al Usuario de Servicios Financieros tramitará las denuncias que presenten las asociaciones de consumidores y usuarios recono…"
  },
  {
   "id": "Obligacion_los_sujetos_obligados_deberan_ofrecer_a_los_usuarios_de_servicios_financieros_po",
   "type": "Obligacion",
   "label": "Ofrecer mínimo tres compañías aseguradoras",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Los sujetos obligados deberán ofrecer a los usuarios de servicios financieros por lo menos tres compañías aseguradoras no vinculadas entre sí entre las que debe…"
  },
  {
   "id": "Obligacion_las_presentaciones_de_los_usuarios_de_servicios_financieros_deberan_poder_realiz",
   "type": "Obligacion",
   "label": "Habilitar múltiples canales de presentación",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Las presentaciones de los usuarios de servicios financieros deberán poder realizarse por teléfono, Internet, por escrito, fax, correo postal y electrónico (e-ma…"
  },
  {
   "id": "Obligacion_la_gerencia_principal_de_proteccion_al_usuario_de_servicios_financieros_brindara",
   "type": "Obligacion",
   "label": "Brindar respuesta a consultas sobre normativa",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La Gerencia Principal de Protección al Usuario de Servicios Financieros brindará respuesta por los medios habilitados a las consultas del público sobre la norma…"
  },
  {
   "id": "Obligacion_dando_orientacion_a_los_usuarios_de_servicios_financieros_sobre_la_manera_de_can",
   "type": "Obligacion",
   "label": "Dar orientación sobre canalización de reclamos",
   "tokens_matcheados": 3,
   "resumen_propiedades": "dando orientación a los usuarios de servicios financieros sobre la manera de canalizar los reclamos por la actuación de los sujetos previstos en el punto 1.1.2"
  },
  {
   "id": "Obligacion_se_debe_notificar_en_el_contrato_a_los_usuarios_de_servicios_financieros_sobre_l",
   "type": "Obligacion",
   "label": "Notificar condiciones modificables en contrato",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Se debe notificar en el contrato a los usuarios de servicios financieros sobre las condiciones que pueden ser objeto de modificación, así como de la facultad de…"
  },
  {
   "id": "Obligacion_los_cajeros_automaticos_destinados_a_los_usuarios_de_servicios_financieros_con_d",
   "type": "Obligacion",
   "label": "Cajeros con funcionalidades para usuarios visuales",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Los cajeros automáticos destinados a los usuarios de servicios financieros con dificultades visuales deberán contar con \"software\" reproductor de texto-a-voz, a…"
  },
  {
   "id": "Obligacion_tambien_se_recibiran_de_los_usuarios_de_servicios_financieros_por_igual_via_come",
   "type": "Obligacion",
   "label": "Recibir comentarios, sugerencias y quejas de usuarios",
   "tokens_matcheados": 3,
   "resumen_propiedades": "También se recibirán de los usuarios de servicios financieros –por igual vía– comentarios, sugerencias y quejas en relación con la actuación de los sujetos obli…"
  }
 ]
}
```

### paso 2 — buscar_nodos {"consulta": "sanciones sujeto obligado usuarios financieros", "limite": 10}

```json
{
 "consulta": "sanciones sujeto obligado usuarios financieros",
 "total_con_match": 100,
 "resultados": [
  {
   "id": "Restriccion_el_importe_de_los_cargos_que_el_sujeto_obligado_transfiera_a_los_usuarios_no_pod",
   "type": "Restriccion",
   "label": "Cargos no superiores a costo de terceros",
   "tokens_matcheados": 3,
   "resumen_propiedades": "El importe de los cargos que el sujeto obligado transfiera a los usuarios no podrá ser superior al que el tercero prestador perciba de particulares, sin interme…"
  },
  {
   "id": "Obligacion_el_sujeto_obligado_debera_ante_la_solicitud_del_usuario_de_servicios_financieros",
   "type": "Obligacion",
   "label": "Extender constancia de consulta o reclamo",
   "tokens_matcheados": 3,
   "resumen_propiedades": "El sujeto obligado deberá, ante la solicitud del usuario de servicios financieros, extender una constancia con la identificación de su consulta o reclamo y el e…"
  },
  {
   "id": "Obligacion_el_sujeto_obligado_debera_verificar_si_situaciones_que_generan_la_obligacion_de_",
   "type": "Obligacion",
   "label": "Verificar situaciones de reintegro en usuarios",
   "tokens_matcheados": 3,
   "resumen_propiedades": "El sujeto obligado deberá verificar si situaciones que generan la obligación de reintegros ha ocurrido respecto de los usuarios que se encuentren en la misma si…"
  },
  {
   "id": "Obligacion_recibir_y_dar_curso_a_las_presentaciones_concernientes_al_sujeto_obligado_que_re",
   "type": "Obligacion",
   "label": "Recibir y dar curso a presentaciones de usuarios",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Recibir y dar curso a las presentaciones –concernientes al sujeto obligado que representan– que inicien los usuarios de servicios financieros, así como las que …"
  },
  {
   "id": "EntidadFinanciera_sujeto_obligado",
   "type": "EntidadFinanciera",
   "label": "Sujetos obligados",
   "tokens_matcheados": 2,
   "resumen_propiedades": "categoria: entidades financieras"
  },
  {
   "id": "TextoOrdenado_to_proteccion_usuarios_servicios_financieros_actual_pdf",
   "type": "TextoOrdenado",
   "label": "Protección de Usuarios",
   "tokens_matcheados": 2,
   "resumen_propiedades": "materia: Protección de los usuarios de servicios financieros; archivo: TO_proteccion_usuarios_servicios_financieros_actual.pdf; version: 8a"
  },
  {
   "id": "Excepcion_cuando_medien_causas_ajenas_al_sujeto_obligado_debidamente_justificadas",
   "type": "Excepcion",
   "label": "Causas ajenas justificadas",
   "tokens_matcheados": 2,
   "resumen_propiedades": "cuando medien causas ajenas al sujeto obligado debidamente justificadas"
  },
  {
   "id": "Excepcion_cuando_reglamentariamente_se_hayan_otorgado_al_sujeto_obligado_mayores_plazos_pa",
   "type": "Excepcion",
   "label": "Plazo mayor por reglamentación",
   "tokens_matcheados": 2,
   "resumen_propiedades": "cuando reglamentariamente se hayan otorgado al sujeto obligado mayores plazos para adecuarse normativamente"
  },
  {
   "id": "EntidadFinanciera_usuario_de_servicio_financiero",
   "type": "EntidadFinanciera",
   "label": "Usuarios de servicios financieros",
   "tokens_matcheados": 2,
   "resumen_propiedades": "categoria: usuario de servicio financiero"
  },
  {
   "id": "Obligacion_en_el_caso_de_que_el_sujeto_obligado_pretenda_incorporar_nuevos_conceptos_en_cal",
   "type": "Obligacion",
   "label": "Obtener consentimiento del usuario",
   "tokens_matcheados": 2,
   "resumen_propiedades": "En el caso de que el sujeto obligado pretenda incorporar nuevos conceptos en calidad de comisiones y/o cargos que no hubiesen sido previstos en el contrato o re…"
  }
 ]
}
```

### paso 3 — buscar_nodos {"consulta": "sanciones régimen sancionatorio incumplimiento", "limite": 10}

```json
{
 "consulta": "sanciones régimen sancionatorio incumplimiento",
 "total_con_match": 42,
 "resultados": [
  {
   "id": "Obligacion_aplicacion_de_sanciones_por_incumplimiento",
   "type": "Obligacion",
   "label": "Aplicación de sanciones por incumplimiento",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El sujeto obligado y quienes resulten responsables serán pasibles de la aplicación de las sanciones previstas en las normas sobre 'Régimen disciplinario a cargo…"
  },
  {
   "id": "Operacion_gestion_de_cobro_por_incumplimiento",
   "type": "Operacion",
   "label": "Gestión de cobro",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Operaciones en gestión de cobro por incumplimiento del proveedor, imputadas en SEPAIMPO cuando se verifican condiciones específicas"
  },
  {
   "id": "Operacion_incumplimiento_de_condiciones_contractuales",
   "type": "Operacion",
   "label": "Incumplimiento de pago",
   "tokens_matcheados": 1,
   "resumen_propiedades": "tipo: incumplimiento de condiciones contractuales"
  },
  {
   "id": "Operacion_operacion_con_entrega_contra_pago_con_incumplimiento_de_pago",
   "type": "Operacion",
   "label": "Operaciones DvP fallidas",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Operaciones con entrega contra pago que tendrán un cargo directo de capital cuando los pagos no se realicen dentro de los cinco días hábiles desde la fecha de l…"
  },
  {
   "id": "Operacion_exportacion_alcanzada_por_beneficios_cambiarios_del_rigi",
   "type": "Operacion",
   "label": "Exportación en régimen RIGI",
   "tokens_matcheados": 1,
   "resumen_propiedades": "tipo: exportación alcanzada por beneficios cambiarios del RIGI"
  },
  {
   "id": "Obligacion_las_entidades_deberan_consultar_en_el_apartado_regimen_informativo_sepaimpo_del_",
   "type": "Obligacion",
   "label": "Consultar situación del cliente",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Las entidades deberán consultar en el apartado 'Régimen Informativo SEPAIMPO' del sitio www3.bcra.gob.ar, si el cliente se encuentra en la situación de condena …"
  },
  {
   "id": "Operacion_presentacion_informativa_de_operaciones_cambiarias",
   "type": "Operacion",
   "label": "Validación en régimen informativo",
   "tokens_matcheados": 1,
   "resumen_propiedades": "tipo: presentación informativa de operaciones cambiarias"
  },
  {
   "id": "Restriccion_incurra_en_atrasos_recurrentes_incumplimiento_de_hasta_180_dias_respecto_de_cond",
   "type": "Restriccion",
   "label": "Atrasos recurrentes incumplimiento",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Incurra en atrasos recurrentes, incumplimiento de hasta 180 días respecto de condiciones contractuales o nulo movimiento en las cuentas."
  },
  {
   "id": "Obligacion_deben_ser_asentados_en_el_rccr_aquellos_reclamos_que_representan_una_queja_por_p",
   "type": "Obligacion",
   "label": "Asentar reclamos por incumplimiento",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Deben ser asentados en el RCCR aquellos reclamos que representan una queja por presunto incumplimiento, prestación defectuosa o falta de prestación de un produc…"
  },
  {
   "id": "Obligacion_luego_de_la_ocurrencia_de_un_incumplimiento_u_otro_evento_desencadenante_de_la_a",
   "type": "Obligacion",
   "label": "Cancelar posiciones secuencialmente",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Luego de la ocurrencia de un incumplimiento u otro evento desencadenante de la aceleración de los reembolsos, las posiciones deberán ser canceladas en forma sec…"
  }
 ]
}
```

### paso 4 — buscar_nodos {"consulta": "multa apercibimiento sanción BCRA", "limite": 10}

```json
{
 "consulta": "multa apercibimiento sanción BCRA",
 "total_con_match": 85,
 "resultados": [
  {
   "id": "EntidadFinanciera_bcra",
   "type": "EntidadFinanciera",
   "label": "BCRA",
   "tokens_matcheados": 1,
   "resumen_propiedades": "categoria: banco central"
  },
  {
   "id": "Obligacion_supervision_del_bcra",
   "type": "Obligacion",
   "label": "Supervisión del BCRA",
   "tokens_matcheados": 1,
   "resumen_propiedades": "El Banco Central de la República Argentina (BCRA) supervisará la actuación de los sujetos obligados"
  },
  {
   "id": "Obligacion_archivar_a_disposicion_del_bcra_toda_la_documentacion_utilizada_en_el_marco_del_",
   "type": "Obligacion",
   "label": "Archivar documentación",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Archivar a disposición del BCRA toda la documentación utilizada en el marco del seguimiento del pago realizado"
  },
  {
   "id": "Restriccion_los_casos_que_no_encuadren_en_lo_expuesto_precedentemente_quedan_sujetos_a_la_co",
   "type": "Restriccion",
   "label": "Conformidad previa BCRA",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Los casos que no encuadren en lo expuesto precedentemente quedan sujetos a la conformidad previa del BCRA, debiendo los pedidos ser canalizados por una entidad …"
  },
  {
   "id": "Obligacion_el_cambio_de_entidad_debe_quedar_registrado_en_el_bcra",
   "type": "Obligacion",
   "label": "Registrar cambio en BCRA",
   "tokens_matcheados": 1,
   "resumen_propiedades": "El cambio de entidad debe quedar registrado en el BCRA"
  },
  {
   "id": "Obligacion_la_entidad_debera_informar_la_asuncion_de_la_tarea_de_seguimiento_al_bcra",
   "type": "Obligacion",
   "label": "Informar asunción al BCRA",
   "tokens_matcheados": 1,
   "resumen_propiedades": "La entidad deberá informar la asunción al BCRA cuando el exportador haya acordado con la entidad la responsabilidad del seguimiento."
  },
  {
   "id": "Obligacion_solicitar_conformidad_bcra",
   "type": "Obligacion",
   "label": "Solicitar conformidad BCRA",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Si el proveedor del exterior es una contraparte vinculada con el importador o se necesiten plazos mayores para la oficialización del despacho de importación, se…"
  },
  {
   "id": "Operacion_deposito",
   "type": "Operacion",
   "label": "Cuentas corrientes en BCRA",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Cuentas corrientes y especiales en el BCRA y órdenes de pago a cargo del BCRA"
  },
  {
   "id": "Operacion_registro_del_cambio_de_entidad_en_el_bcra",
   "type": "Operacion",
   "label": "Registro de cambio en BCRA",
   "tokens_matcheados": 1,
   "resumen_propiedades": "tipo: registro del cambio de entidad en el BCRA"
  },
  {
   "id": "Excepcion_el_bcra_establezca_que_se_debe_hacer_una_reduccion_generalizada_del_valor_si_pos",
   "type": "Excepcion",
   "label": "Reducción generalizada BCRA",
   "tokens_matcheados": 1,
   "resumen_propiedades": "El BCRA establezca que se debe hacer una reducción generalizada del valor. Si posteriormente se autorizan incrementos, el valor ajustado del inmueble no podrá s…"
  }
 ]
}
```

### paso 5 — ver_nodo {"id": "Obligacion_aplicacion_de_sanciones_por_incumplimiento"}

```json
{
 "id": "Obligacion_aplicacion_de_sanciones_por_incumplimiento",
 "type": "Obligacion",
 "label": "Aplicación de sanciones por incumplimiento",
 "properties": {
  "tipo": "otra",
  "description": "El sujeto obligado y quienes resulten responsables serán pasibles de la aplicación de las sanciones previstas en las normas sobre 'Régimen disciplinario a cargo del Banco Central de la República Argentina (Leyes 21.526 y 25.065) y tramitación de sumarios cambiarios (Ley 19.359)', por los incumplimientos que se constaten respecto de estas normas y respecto de los contenidos desarrollados en los manuales de procedimiento interno con motivo de ellas."
 },
 "provenances": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "Punto 4.4. Actuaciones de oficio."
  }
 ]
}
```

### paso 6 — buscar_nodos {"consulta": "régimen disciplinario Banco Central", "limite": 10}

```json
{
 "consulta": "régimen disciplinario Banco Central",
 "total_con_match": 38,
 "resultados": [
  {
   "id": "Excepcion_creditos_frente_al_banco_central_de_la_republica_argentina_estan_excluidos",
   "type": "Excepcion",
   "label": "Exclusión de créditos frente al BCRA",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Créditos frente al Banco Central de la República Argentina están excluidos"
  },
  {
   "id": "Obligacion_el_banco_central_de_la_republica_argentina_establecera_las_condiciones_y_plazos_",
   "type": "Obligacion",
   "label": "BCRA establecerá condiciones y plazos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El BANCO CENTRAL DE LA REPÚBLICA ARGENTINA establecerá las condiciones y plazos para el ingreso de contravalor de exportación"
  },
  {
   "id": "Excepcion_garantias_otorgadas_a_favor_del_banco_central_estan_excluidas",
   "type": "Excepcion",
   "label": "Exclusión de garantías a favor del BCRA",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Garantías otorgadas a favor del Banco Central están excluidas"
  },
  {
   "id": "Obligacion_el_banco_central_de_la_republica_argentina_establecera_los_supuestos_en_los_que_",
   "type": "Obligacion",
   "label": "BCRA establecerá supuestos de autorización",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El BANCO CENTRAL DE LA REPÚBLICA ARGENTINA establecerá los supuestos en los que el acceso al mercado de cambios requerirá autorización previa, con base en pauta…"
  },
  {
   "id": "Obligacion_el_banco_central_de_la_republica_argentina_establecera_reglamentaciones_que_evit",
   "type": "Obligacion",
   "label": "BCRA establecerá reglamentaciones preventivas",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El BANCO CENTRAL DE LA REPÚBLICA ARGENTINA establecerá reglamentaciones que eviten prácticas y operaciones tendientes a eludir lo dispuesto en esta medida"
  },
  {
   "id": "EntidadFinanciera_banco",
   "type": "EntidadFinanciera",
   "label": "Bancos",
   "tokens_matcheados": 1,
   "resumen_propiedades": "categoria: banco"
  },
  {
   "id": "EntidadFinanciera_banco_comercial",
   "type": "EntidadFinanciera",
   "label": "Bancos comerciales",
   "tokens_matcheados": 1,
   "resumen_propiedades": "categoria: banco comercial"
  },
  {
   "id": "Operacion_operaciones_con_entidades_de_contraparte_central_calificadas",
   "type": "Operacion",
   "label": "Operaciones con QCCP",
   "tokens_matcheados": 1,
   "resumen_propiedades": "tipo: operaciones con entidades de contraparte central calificadas"
  },
  {
   "id": "Operacion_exportacion_alcanzada_por_beneficios_cambiarios_del_rigi",
   "type": "Operacion",
   "label": "Exportación en régimen RIGI",
   "tokens_matcheados": 1,
   "resumen_propiedades": "tipo: exportación alcanzada por beneficios cambiarios del RIGI"
  },
  {
   "id": "EntidadFinanciera_sucursal_de_banco_oficial",
   "type": "EntidadFinanciera",
   "label": "Sucursales de bancos oficiales",
   "tokens_matcheados": 1,
   "resumen_propiedades": "categoria: sucursal o agencia en exterior"
  }
 ]
}
```

### paso 7 — buscar_nodos {"consulta": "Leyes 21.526 25.065 régimen disciplinario", "limite": 10}

```json
{
 "consulta": "Leyes 21.526 25.065 régimen disciplinario",
 "total_con_match": 37,
 "resultados": [
  {
   "id": "Restriccion_exposiciones_por_compras_en_cuotas_con_tarjeta_credito_hasta_25_11_21",
   "type": "Restriccion",
   "label": "Coeficiente de riesgo 1250 puntos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Exposiciones por compras en cuotas con tarjeta crédito hasta 25/11/21"
  },
  {
   "id": "Operacion_exportacion_alcanzada_por_beneficios_cambiarios_del_rigi",
   "type": "Operacion",
   "label": "Exportación en régimen RIGI",
   "tokens_matcheados": 1,
   "resumen_propiedades": "tipo: exportación alcanzada por beneficios cambiarios del RIGI"
  },
  {
   "id": "Restriccion_la_suscripcion_local_no_supere_el_25_veinticinco_por_ciento_de_la_suscripcion_to",
   "type": "Restriccion",
   "label": "Suscripción local máximo 25%",
   "tokens_matcheados": 1,
   "resumen_propiedades": "La suscripción local no supere el 25% (veinticinco por ciento) de la suscripción total"
  },
  {
   "id": "Restriccion_aplicacion_de_ccf_del_0_desde_01_01_25_al_30_06_25_y_del_5_desde_01_07_25_al_31_",
   "type": "Restriccion",
   "label": "Aplicación de CCF por período",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Desde el 01/01/25 y hasta el 31/12/25, las entidades financieras clasificadas en el grupo 2 que al 01/01/25 pertenezcan a los grupos B y C deberán convertir los…"
  },
  {
   "id": "Obligacion_las_entidades_deberan_consultar_en_el_apartado_regimen_informativo_sepaimpo_del_",
   "type": "Obligacion",
   "label": "Consultar situación del cliente",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Las entidades deberán consultar en el apartado 'Régimen Informativo SEPAIMPO' del sitio www3.bcra.gob.ar, si el cliente se encuentra en la situación de condena …"
  },
  {
   "id": "Operacion_presentacion_informativa_de_operaciones_cambiarias",
   "type": "Operacion",
   "label": "Validación en régimen informativo",
   "tokens_matcheados": 1,
   "resumen_propiedades": "tipo: presentación informativa de operaciones cambiarias"
  },
  {
   "id": "Restriccion_los_punitorios_u_otros_equivalentes_que_se_devenguen_desde_el_01_01_25_continuar",
   "type": "Restriccion",
   "label": "Conformidad previa para punitorios",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Los punitorios u otros equivalentes que se devenguen desde el 01/01/25 continuarán alcanzados por el requisito de conformidad previa."
  },
  {
   "id": "Excepcion_excepto_cuando_el_deudor_contaba_con_una_certificacion_por_los_regimenes_de_acce",
   "type": "Excepcion",
   "label": "Excepción por régimen petróleo y gas",
   "tokens_matcheados": 1,
   "resumen_propiedades": "excepto cuando el deudor contaba con una Certificación por los regímenes de acceso a divisas para la producción incremental de petróleo y/o gas natural (Decreto…"
  },
  {
   "id": "TextoOrdenado_to_regimen_informativo_contable_mensual_actual_pdf",
   "type": "TextoOrdenado",
   "label": "Régimen Informativo Contable Mensual",
   "tokens_matcheados": 1,
   "resumen_propiedades": "materia: Información contable y regulatoria mensual; archivo: TO_regimen_informativo_contable_mensual_actual.pdf; version: actual"
  },
  {
   "id": "Obligacion_la_entidad_debera_dar_cumplimiento_a_las_disposiciones_dadas_a_conocer_por_el_re",
   "type": "Obligacion",
   "label": "Cumplimiento régimen informativo BCRA",
   "tokens_matcheados": 1,
   "resumen_propiedades": "La entidad deberá dar cumplimiento a las disposiciones dadas a conocer por el régimen informativo asociado a este seguimiento."
  }
 ]
}
```

### paso 8 — buscar_nodos {"consulta": "multa apercibimiento amonestación sanción disciplinaria", "limite": 10}

```json
{
 "consulta": "multa apercibimiento amonestación sanción disciplinaria",
 "total_con_match": 2,
 "resultados": [
  {
   "id": "Restriccion_los_incumplimientos_a_esta_normativa_se_encontraran_alcanzados_por_la_ley_del_re",
   "type": "Restriccion",
   "label": "Sanción por incumplimiento normativo",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Los incumplimientos a esta normativa se encontrarán alcanzados por la Ley del Régimen Penal Cambiario."
  },
  {
   "id": "Restriccion_los_incumplimientos_en_el_envio_de_la_informacion_estaran_sujetos_a_la_aplicacio",
   "type": "Restriccion",
   "label": "Sanción por falta de envío informativo",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Los incumplimientos en el envío de la información estarán sujetos a la aplicación del artículo 41 de la Ley de Entidades Financieras."
  }
 ]
}
```

### paso 9 — buscar_nodos {"consulta": "sumarios cambiarios Ley 19.359", "limite": 10}

```json
{
 "consulta": "sumarios cambiarios Ley 19.359",
 "total_con_match": 27,
 "resultados": [
  {
   "id": "Comunicacion_ley_27444",
   "type": "Comunicacion",
   "label": "Com. Ley 27444",
   "tokens_matcheados": 1,
   "resumen_propiedades": "codigo: Ley-27444; tipo: normativa modificatoria; numero: 27444"
  },
  {
   "id": "Comunicacion_decreto_91_19",
   "type": "Comunicacion",
   "label": "Com. Decreto 91/19",
   "tokens_matcheados": 1,
   "resumen_propiedades": "codigo: Decreto-91/19; tipo: Decreto; numero: 91"
  },
  {
   "id": "Operacion_exportacion_alcanzada_por_beneficios_cambiarios_del_rigi",
   "type": "Operacion",
   "label": "Exportación en régimen RIGI",
   "tokens_matcheados": 1,
   "resumen_propiedades": "tipo: exportación alcanzada por beneficios cambiarios del RIGI"
  },
  {
   "id": "Operacion_acumulacion_de_incentivos_cambiarios",
   "type": "Operacion",
   "label": "Acumulación de beneficios cambiarios",
   "tokens_matcheados": 1,
   "resumen_propiedades": "tipo: acumulación de incentivos cambiarios"
  },
  {
   "id": "Restriccion_los_incumplimientos_a_esta_normativa_se_encontraran_alcanzados_por_la_ley_del_re",
   "type": "Restriccion",
   "label": "Sanción por incumplimiento normativo",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Los incumplimientos a esta normativa se encontrarán alcanzados por la Ley del Régimen Penal Cambiario."
  },
  {
   "id": "Excepcion_no_se_consideraran_dentro_de_ese_concepto_las_refinanciaciones_otorgadas_a_los_p",
   "type": "Excepcion",
   "label": "Excepción Ley Emergencia Agropecuaria",
   "tokens_matcheados": 1,
   "resumen_propiedades": "No se considerarán dentro de ese concepto las refinanciaciones otorgadas a los productores agropecuarios cuando ello resulte de la aplicación de disposiciones v…"
  },
  {
   "id": "Obligacion_la_entidad_emisora_de_la_certificacion_debera_previamente_verificar_el_cumplimie",
   "type": "Obligacion",
   "label": "Verificación de requisitos cambiarios",
   "tokens_matcheados": 1,
   "resumen_propiedades": "La entidad emisora de la certificación deberá previamente verificar el cumplimiento de todos los requisitos establecidos por la normativa cambiaria para el acce…"
  },
  {
   "id": "Operacion_cancelacion_de_financiaciones_pendientes_al_30_08_19",
   "type": "Operacion",
   "label": "Cancelación financiaciones pendientes",
   "tokens_matcheados": 1,
   "resumen_propiedades": "tipo: cancelación de financiaciones pendientes al 30/08/19"
  },
  {
   "id": "Excepcion_emisiones_de_titulos_de_deuda_realizadas_a_partir_del_01_09_19_con_objeto_de_ref",
   "type": "Excepcion",
   "label": "Emisiones títulos refinanciación deudas",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Emisiones de títulos de deuda realizadas a partir del 01/09/19 con objeto de refinanciar deudas que conlleven incremento de la vida promedio de las obligaciones"
  },
  {
   "id": "Operacion_exportacion_alcanzada_por_beneficios_cambiarios_del_decreto_929_13",
   "type": "Operacion",
   "label": "Exportación en régimen de hidrocarburos",
   "tokens_matcheados": 1,
   "resumen_propiedades": "tipo: exportación alcanzada por beneficios cambiarios del Decreto 929/13"
  }
 ]
}
```

### paso 10 — ver_nodo {"id": "Restriccion_los_incumplimientos_a_esta_normativa_se_encontraran_alcanzados_por_la_ley_del_re"}

```json
{
 "id": "Restriccion_los_incumplimientos_a_esta_normativa_se_encontraran_alcanzados_por_la_ley_del_re",
 "type": "Restriccion",
 "label": "Sanción por incumplimiento normativo",
 "properties": {
  "descripcion": "Los incumplimientos a esta normativa se encontrarán alcanzados por la Ley del Régimen Penal Cambiario.",
  "tipo": "prohibicion"
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 1.5. Los incumplimientos a esta normativa se encontrarán alcanzados por la Ley del Ré"
  }
 ]
}
```

### paso 11 — ver_nodo {"id": "Restriccion_los_incumplimientos_en_el_envio_de_la_informacion_estaran_sujetos_a_la_aplicacio"}

```json
{
 "id": "Restriccion_los_incumplimientos_en_el_envio_de_la_informacion_estaran_sujetos_a_la_aplicacio",
 "type": "Restriccion",
 "label": "Sanción por falta de envío informativo",
 "properties": {
  "descripcion": "Los incumplimientos en el envío de la información estarán sujetos a la aplicación del artículo 41 de la Ley de Entidades Financieras.",
  "tipo": "prohibicion"
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 1.5. Los incumplimientos a esta normativa se encontrarán alcanzados por la Ley del Ré"
  }
 ]
}
```

### paso 12 — buscar_nodos {"consulta": "artículo 41 Ley Entidades Financieras", "limite": 10}

```json
{
 "consulta": "artículo 41 Ley Entidades Financieras",
 "total_con_match": 140,
 "resultados": [
  {
   "id": "Operacion_transformacion_de_entidades_financieras",
   "type": "Operacion",
   "label": "Transformación de entidades",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: transformación de entidades financieras"
  },
  {
   "id": "Obligacion_las_entidades_financieras_del_grupo_1_deberan_llevar_a_cabo_un_proceso_de_debida",
   "type": "Obligacion",
   "label": "Proceso de debida diligencia",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Las entidades financieras del grupo 1 deberán llevar a cabo un proceso de debida diligencia –al momento del otorgamiento del crédito y con frecuencia mínima anu…"
  },
  {
   "id": "Restriccion_cuando_el_total_de_participaciones_en_el_capital_de_entidades_financieras_empres",
   "type": "Restriccion",
   "label": "Límite tenencias capital 10%",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Cuando el total de participaciones en el capital de entidades financieras, empresas de servicios complementarios de la actividad financiera y compañías de segur…"
  },
  {
   "id": "EntidadFinanciera_entidad_financiera_grupo_2",
   "type": "EntidadFinanciera",
   "label": "Entidades financieras grupo 2",
   "tokens_matcheados": 2,
   "resumen_propiedades": "categoria: entidad financiera grupo 2"
  },
  {
   "id": "Restriccion_impedimento_para_transformacion_de_entidades_financieras_cuando_exista_obligacio",
   "type": "Restriccion",
   "label": "Impedimento de transformación",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Impedimento para transformación de entidades financieras cuando exista obligación de presentar planes de regularización"
  },
  {
   "id": "Obligacion_las_entidades_financieras_ante_requerimientos_de_apertura_de_cuentas_a_la_vista_",
   "type": "Obligacion",
   "label": "Ofrecer caja de ahorros en pesos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Las entidades financieras, ante requerimientos de apertura de cuentas a la vista, deberán ofrecer la Caja de ahorros en pesos con las prestaciones previstas en …"
  },
  {
   "id": "Obligacion_las_entidades_financieras_que_pertenezcan_al_grupo_a_cuya_sociedad_controlante_s",
   "type": "Obligacion",
   "label": "Cumplimiento consolidado Grupo A",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Las entidades financieras que pertenezcan al grupo A, cuya sociedad controlante sea una 'compañía holding' (no entidad financiera), deberán dar cumplimiento a l…"
  },
  {
   "id": "Operacion_participacion_en_entidades_financieras_del_exterior",
   "type": "Operacion",
   "label": "Participación entidades exterior",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: participación en entidades financieras del exterior"
  },
  {
   "id": "EntidadFinanciera_entidad_financiera_del_exterior",
   "type": "EntidadFinanciera",
   "label": "Entidades financieras del exterior",
   "tokens_matcheados": 2,
   "resumen_propiedades": "categoria: entidad financiera del exterior"
  },
  {
   "id": "Obligacion_en_el_caso_de_financiaciones_otorgadas_por_entidades_financieras_locales_el_segu",
   "type": "Obligacion",
   "label": "A cargo seguimiento financiaciones",
   "tokens_matcheados": 2,
   "resumen_propiedades": "En el caso de financiaciones otorgadas por entidades financieras locales, el seguimiento estará a cargo de la entidad que otorgó la financiación hasta su cancel…"
  }
 ]
}
```

### paso 13 — buscar_nodos {"consulta": "protección usuarios financieros sanciones consecuencias", "limite": 10}

```json
{
 "consulta": "protección usuarios financieros sanciones consecuencias",
 "total_con_match": 91,
 "resultados": [
  {
   "id": "TextoOrdenado_to_proteccion_usuarios_servicios_financieros_actual_pdf",
   "type": "TextoOrdenado",
   "label": "Protección de Usuarios",
   "tokens_matcheados": 3,
   "resumen_propiedades": "materia: Protección de los usuarios de servicios financieros; archivo: TO_proteccion_usuarios_servicios_financieros_actual.pdf; version: 8a"
  },
  {
   "id": "EntidadFinanciera_usuario_de_servicio_financiero",
   "type": "EntidadFinanciera",
   "label": "Usuarios de servicios financieros",
   "tokens_matcheados": 2,
   "resumen_propiedades": "categoria: usuario de servicio financiero"
  },
  {
   "id": "Obligacion_la_gerencia_principal_de_proteccion_al_usuario_de_servicios_financieros_tramitar",
   "type": "Obligacion",
   "label": "Tramitar denuncias de asociaciones",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La Gerencia Principal de Protección al Usuario de Servicios Financieros tramitará las denuncias que presenten las asociaciones de consumidores y usuarios recono…"
  },
  {
   "id": "Obligacion_los_usuarios_tienen_derecho_a_la_proteccion_de_su_seguridad_e_intereses_economic",
   "type": "Obligacion",
   "label": "Proteger seguridad e intereses económicos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Los usuarios tienen derecho a la protección de su seguridad e intereses económicos"
  },
  {
   "id": "Obligacion_los_sujetos_obligados_deberan_ofrecer_a_los_usuarios_de_servicios_financieros_po",
   "type": "Obligacion",
   "label": "Ofrecer mínimo tres compañías aseguradoras",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Los sujetos obligados deberán ofrecer a los usuarios de servicios financieros por lo menos tres compañías aseguradoras no vinculadas entre sí entre las que debe…"
  },
  {
   "id": "Obligacion_las_presentaciones_de_los_usuarios_de_servicios_financieros_deberan_poder_realiz",
   "type": "Obligacion",
   "label": "Habilitar múltiples canales de presentación",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Las presentaciones de los usuarios de servicios financieros deberán poder realizarse por teléfono, Internet, por escrito, fax, correo postal y electrónico (e-ma…"
  },
  {
   "id": "Obligacion_la_gerencia_principal_de_proteccion_al_usuario_de_servicios_financieros_brindara",
   "type": "Obligacion",
   "label": "Brindar respuesta a consultas sobre normativa",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La Gerencia Principal de Protección al Usuario de Servicios Financieros brindará respuesta por los medios habilitados a las consultas del público sobre la norma…"
  },
  {
   "id": "Obligacion_dando_orientacion_a_los_usuarios_de_servicios_financieros_sobre_la_manera_de_can",
   "type": "Obligacion",
   "label": "Dar orientación sobre canalización de reclamos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "dando orientación a los usuarios de servicios financieros sobre la manera de canalizar los reclamos por la actuación de los sujetos previstos en el punto 1.1.2"
  },
  {
   "id": "Obligacion_se_debe_notificar_en_el_contrato_a_los_usuarios_de_servicios_financieros_sobre_l",
   "type": "Obligacion",
   "label": "Notificar condiciones modificables en contrato",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Se debe notificar en el contrato a los usuarios de servicios financieros sobre las condiciones que pueden ser objeto de modificación, así como de la facultad de…"
  },
  {
   "id": "Obligacion_los_cajeros_automaticos_destinados_a_los_usuarios_de_servicios_financieros_con_d",
   "type": "Obligacion",
   "label": "Cajeros con funcionalidades para usuarios visuales",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Los cajeros automáticos destinados a los usuarios de servicios financieros con dificultades visuales deberán contar con \"software\" reproductor de texto-a-voz, a…"
  }
 ]
}
```

### paso 14 — ver_nodo {"id": "TextoOrdenado_to_proteccion_usuarios_servicios_financieros_actual_pdf"}

```json
{
 "id": "TextoOrdenado_to_proteccion_usuarios_servicios_financieros_actual_pdf",
 "type": "TextoOrdenado",
 "label": "Protección de Usuarios",
 "properties": {
  "materia": "Protección de los usuarios de servicios financieros",
  "archivo": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
  "version": "8a"
 },
 "provenances": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "Punto 1.1. Partes."
  }
 ]
}
```

### paso 15 — ver_vecinos {"id": "Obligacion_aplicacion_de_sanciones_por_incumplimiento", "direccion": "ambas"}

```json
{
 "id": "Obligacion_aplicacion_de_sanciones_por_incumplimiento",
 "label": "Aplicación de sanciones por incumplimiento",
 "n_salientes_total": 2,
 "n_entrantes_total": 0,
 "salientes": [
  {
   "relation": "establecida_en",
   "vecino_id": "TextoOrdenado_to_proteccion_usuarios_servicios_financieros_actual_pdf",
   "vecino_label": "Protección de Usuarios",
   "provenances": [
    {
     "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
     "location": "Punto 4.4. Actuaciones de oficio."
    }
   ]
  },
  {
   "relation": "aplica_a",
   "vecino_id": "EntidadFinanciera_sujeto_obligado",
   "vecino_label": "Sujetos obligados",
   "provenances": [
    {
     "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
     "location": "Punto 4.4. Actuaciones de oficio."
    }
   ]
  }
 ],
 "salientes_truncado": false,
 "entrantes": [],
 "entrantes_truncado": false
}
```



---

# CQN-014

## Respuesta final íntegra (trace.final_json)

```json
{
 "respuesta": "Si una entidad financiera del grupo 2 no registró ingreso bruto positivo en ninguno de los períodos de 12 meses de los últimos 36 meses (n=0), deberá observar una exigencia de capital por riesgo operacional equivalente al límite previsto en el punto 7.3 de las normas sobre Capitales mínimos de las entidades financieras.",
 "citas": [
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Punto 5.1. Normas de procedimiento (parte 1)"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Punto 7.2. Exigencia de capital por riesgo operacional para entidades del grupo 2."
  }
 ],
 "respondible": false
}
```

(`respondible`: false · tool_calls_used: 15 · hit_tool_limit: True)

## Inventario de pasos + fidelidad runtime↔re-ejecución

| paso | tool | input | output_chars (runtime) | re-ejecutado | fiel |
|---|---|---|---|---|---|
| 1 | buscar_nodos | `{"consulta": "grupo 2 ingreso bruto riesgo operacional capital", "limite": 10}` | 3253 | 3253 | SÍ |
| 2 | buscar_nodos | `{"consulta": "exigencia capital riesgo operacional grupo 2", "limite": 10}` | 3610 | 3610 | SÍ |
| 3 | ver_nodo | `{"id": "Excepcion_si_n_0_ningun_periodo_con_ib_positivo_debera_observarse_una_exigencia_eq` | 525 | 525 | SÍ |
| 4 | buscar_nodos | `{"consulta": "punto 7.3 capitales mínimos límite", "limite": 10}` | 2878 | 2878 | SÍ |
| 5 | buscar_nodos | `{"consulta": "7.3 normas capitales mínimos entidades financieras", "limite": 10}` | 3434 | 3434 | SÍ |
| 6 | buscar_nodos | `{"consulta": "7.3 exigencia capital riesgo operacional límite máximo", "limite": 10}` | 3570 | 3570 | SÍ |
| 7 | buscar_nodos | `{"consulta": "límite exigencia capital operacional 7.3", "limite": 10}` | 3569 | 3569 | SÍ |
| 8 | ver_nodo | `{"id": "Restriccion_la_exigencia_de_capital_por_riesgo_operacional_para_entidades_del_grup` | 673 | 673 | SÍ |
| 9 | buscar_nodos | `{"consulta": "punto 7.3 capital mínimo grupo 2", "limite": 10}` | 3347 | 3347 | SÍ |
| 10 | buscar_nodos | `{"consulta": "n=0 ningún período ingreso bruto positivo exigencia", "limite": 10}` | 3483 | 3483 | SÍ |
| 11 | ver_nodo | `{"id": "Excepcion_cuando_n_sea_igual_a_cero_n_0_debera_observarse_una_exigencia_equivalent` | 484 | 484 | SÍ |
| 12 | buscar_nodos | `{"consulta": "7.3 límite máximo capital operacional grupo 2", "limite": 10}` | 3484 | 3484 | SÍ |
| 13 | buscar_nodos | `{"consulta": "punto 7.3 máximo 17 por ciento grupo 2", "limite": 10}` | 3187 | 3187 | SÍ |
| 14 | ver_nodo | `{"id": "Obligacion_se_determinara_mensualmente_por_la_expresion_cro_a_ib_n_donde_a_es_15_n` | 546 | 546 | SÍ |
| 15 | buscar_nodos | `{"consulta": "7.3 máximo exigencia capital operacional 17 por ciento", "limite": 10}` | 3602 | 3602 | SÍ |

**Fidelidad: 15/15** (igualdad de largos del output completo).

## Apéndice — outputs completos re-ejecutados

### paso 1 — buscar_nodos {"consulta": "grupo 2 ingreso bruto riesgo operacional capital", "limite": 10}

```json
{
 "consulta": "grupo 2 ingreso bruto riesgo operacional capital",
 "total_con_match": 463,
 "resultados": [
  {
   "id": "Restriccion_la_exigencia_de_capital_por_riesgo_operacional_para_entidades_del_grupo_b_determ",
   "type": "Restriccion",
   "label": "Límite exigencia capital operacional grupo B",
   "tokens_matcheados": 4,
   "resumen_propiedades": "La exigencia de capital por riesgo operacional para entidades del grupo B determinada a través de la aplicación de la expresión descripta en el punto 7.2. hasta…"
  },
  {
   "id": "Restriccion_la_exigencia_de_capital_por_riesgo_operacional_para_entidades_del_grupo_c_determ",
   "type": "Restriccion",
   "label": "Límite exigencia capital operacional grupo C",
   "tokens_matcheados": 4,
   "resumen_propiedades": "La exigencia de capital por riesgo operacional para entidades del grupo C determinada a través de la aplicación de la expresión descripta en el punto 7.2. hasta…"
  },
  {
   "id": "Obligacion_se_determinara_mensualmente_la_exigencia_de_capital_por_riesgo_operacional_cro_m",
   "type": "Obligacion",
   "label": "Informar CRO mensualmente",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Se determinará mensualmente la exigencia de capital por riesgo operacional (CRO) mediante la expresión CRO = BIC x ILM para entidades del Grupo 1"
  },
  {
   "id": "Restriccion_participaciones_en_el_capital_250",
   "type": "Restriccion",
   "label": "Ponderador participaciones capital grupo 2",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Participaciones en el capital: 250"
  },
  {
   "id": "Operacion_calculo",
   "type": "Operacion",
   "label": "Cálculo exigencia capital riesgo operacional",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Cálculo de K (exigencia de capital promedio de las exposiciones subyacentes); es decir, el ratio entre la suma de las exposiciones subyacentes ponderadas por ri…"
  },
  {
   "id": "Operacion_calculo_de_capital_minimo_por_riesgo_operacional",
   "type": "Operacion",
   "label": "Cálculo exigencia capital mínimo operacional",
   "tokens_matcheados": 3,
   "resumen_propiedades": "tipo: cálculo de capital mínimo por riesgo operacional"
  },
  {
   "id": "Restriccion_la_exigencia_mensual_de_capital_minimo_por_riesgo_operacional_de_las_entidades_f",
   "type": "Restriccion",
   "label": "Exigencia capital mínimo por riesgo operacional",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La exigencia mensual de capital mínimo por riesgo operacional de las entidades financieras de los grupos 1 y 2 correspondiente al primer mes será equivalente al…"
  },
  {
   "id": "Operacion_calculo_de_promedio_de_exigencias_de_riesgo_operacional",
   "type": "Operacion",
   "label": "Cálculo promedio ERC",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: cálculo de promedio de exigencias de riesgo operacional"
  },
  {
   "id": "EntidadFinanciera_entidad_del_grupo_2",
   "type": "EntidadFinanciera",
   "label": "Entidades del grupo 2",
   "tokens_matcheados": 2,
   "resumen_propiedades": "categoria: entidades del grupo 2"
  },
  {
   "id": "Excepcion_si_n_0_ningun_periodo_con_ib_positivo_debera_observarse_una_exigencia_equivalent",
   "type": "Excepcion",
   "label": "Excepción N=0 Grupo 2",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Si n = 0 (ningún período con IB positivo), deberá observarse una exigencia equivalente al límite previsto en el punto 7.3 de las normas sobre Capitales mínimos …"
  }
 ]
}
```

### paso 2 — buscar_nodos {"consulta": "exigencia capital riesgo operacional grupo 2", "limite": 10}

```json
{
 "consulta": "exigencia capital riesgo operacional grupo 2",
 "total_con_match": 422,
 "resultados": [
  {
   "id": "Restriccion_la_exigencia_de_capital_por_riesgo_operacional_para_entidades_del_grupo_b_determ",
   "type": "Restriccion",
   "label": "Límite exigencia capital operacional grupo B",
   "tokens_matcheados": 5,
   "resumen_propiedades": "La exigencia de capital por riesgo operacional para entidades del grupo B determinada a través de la aplicación de la expresión descripta en el punto 7.2. hasta…"
  },
  {
   "id": "Restriccion_la_exigencia_de_capital_por_riesgo_operacional_para_entidades_del_grupo_c_determ",
   "type": "Restriccion",
   "label": "Límite exigencia capital operacional grupo C",
   "tokens_matcheados": 5,
   "resumen_propiedades": "La exigencia de capital por riesgo operacional para entidades del grupo C determinada a través de la aplicación de la expresión descripta en el punto 7.2. hasta…"
  },
  {
   "id": "Obligacion_se_determinara_mensualmente_la_exigencia_de_capital_por_riesgo_operacional_cro_m",
   "type": "Obligacion",
   "label": "Informar CRO mensualmente",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Se determinará mensualmente la exigencia de capital por riesgo operacional (CRO) mediante la expresión CRO = BIC x ILM para entidades del Grupo 1"
  },
  {
   "id": "Operacion_calculo",
   "type": "Operacion",
   "label": "Cálculo exigencia capital riesgo operacional",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Cálculo de K (exigencia de capital promedio de las exposiciones subyacentes); es decir, el ratio entre la suma de las exposiciones subyacentes ponderadas por ri…"
  },
  {
   "id": "Operacion_calculo_de_capital_minimo_por_riesgo_operacional",
   "type": "Operacion",
   "label": "Cálculo exigencia capital mínimo operacional",
   "tokens_matcheados": 4,
   "resumen_propiedades": "tipo: cálculo de capital mínimo por riesgo operacional"
  },
  {
   "id": "Restriccion_la_exigencia_mensual_de_capital_minimo_por_riesgo_operacional_de_las_entidades_f",
   "type": "Restriccion",
   "label": "Exigencia capital mínimo por riesgo operacional",
   "tokens_matcheados": 4,
   "resumen_propiedades": "La exigencia mensual de capital mínimo por riesgo operacional de las entidades financieras de los grupos 1 y 2 correspondiente al primer mes será equivalente al…"
  },
  {
   "id": "Excepcion_si_n_0_ningun_periodo_con_ib_positivo_debera_observarse_una_exigencia_equivalent",
   "type": "Excepcion",
   "label": "Excepción N=0 Grupo 2",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Si n = 0 (ningún período con IB positivo), deberá observarse una exigencia equivalente al límite previsto en el punto 7.3 de las normas sobre Capitales mínimos …"
  },
  {
   "id": "Excepcion_la_presente_reduccion_de_exigencia_no_rige_para_entidades_del_grupo_2_que_sean_s",
   "type": "Excepcion",
   "label": "Excepción G-SIB para reducción",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La presente reducción de exigencia no rige para entidades del Grupo 2 que sean subsidiarias o sucursales de entidades de importancia sistémica global (G-SIB)"
  },
  {
   "id": "Obligacion_aplicar_exigencia_capital_por_riesgo_general_mercado_a_todas_posiciones_derivado",
   "type": "Obligacion",
   "label": "Cálculo riesgo general mercado",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La exigencia de capital por el riesgo general de mercado alcanza a todas las posiciones en instrumentos derivados -de la misma manera que también alcanza a las …"
  },
  {
   "id": "Operacion_calculo_de_exigencia_de_capital_minimo_por_riesgo_de_credito",
   "type": "Operacion",
   "label": "Cálculo exigencia capital mínimo",
   "tokens_matcheados": 3,
   "resumen_propiedades": "tipo: cálculo de exigencia de capital mínimo por riesgo de crédito"
  }
 ]
}
```

### paso 3 — ver_nodo {"id": "Excepcion_si_n_0_ningun_periodo_con_ib_positivo_debera_observarse_una_exigencia_equivalent"}

```json
{
 "id": "Excepcion_si_n_0_ningun_periodo_con_ib_positivo_debera_observarse_una_exigencia_equivalent",
 "type": "Excepcion",
 "label": "Excepción N=0 Grupo 2",
 "properties": {
  "descripcion": "Si n = 0 (ningún período con IB positivo), deberá observarse una exigencia equivalente al límite previsto en el punto 7.3 de las normas sobre Capitales mínimos de las entidades financieras"
 },
 "provenances": [
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Punto 5.1. Normas de procedimiento (parte 1)"
  }
 ]
}
```

### paso 4 — buscar_nodos {"consulta": "punto 7.3 capitales mínimos límite", "limite": 10}

```json
{
 "consulta": "punto 7.3 capitales mínimos límite",
 "total_con_match": 243,
 "resultados": [
  {
   "id": "Obligacion_la_entidad_debera_verificar_las_condiciones_indicadas_en_el_punto_9_3_1_constata",
   "type": "Obligacion",
   "label": "Verificación cumplimiento requisitos puntos 7.9 o 7.10",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La entidad deberá verificar las condiciones indicadas en el punto 9.3.1., constatar que la cancelación tuvo lugar a partir de la fecha de vencimiento y contar c…"
  },
  {
   "id": "TextoOrdenado_to_capitales_minimos_actual_pdf",
   "type": "TextoOrdenado",
   "label": "Capitales Mínimos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "materia: capitales minimos; archivo: TO_capitales_minimos_actual.pdf; version: actual"
  },
  {
   "id": "Excepcion_excepcion_por_punto_3_13",
   "type": "Excepcion",
   "label": "Excepción por punto 3.13",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Las entidades podrán también en el marco del punto 3.13., sin conformidad previa del BCRA si el requisito estuviese vigente"
  },
  {
   "id": "Excepcion_no_aplicable_punto_3_12_1",
   "type": "Excepcion",
   "label": "No aplicable punto 3.12.1",
   "tokens_matcheados": 2,
   "resumen_propiedades": "En la medida que no encuadre en el punto 3.12.1"
  },
  {
   "id": "Obligacion_cuando_el_pago_a_nombre_del_cliente_encuadre_en_el_punto_10_10_2_3_se_debera_dej",
   "type": "Obligacion",
   "label": "Dejar constancia en reporte",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Cuando el pago a nombre del cliente encuadre en el punto 10.10.2.3., se deberá dejar constancia de tal circunstancia al reportar el boleto de venta a nombre del…"
  },
  {
   "id": "Restriccion_acciones_definidas_conforme_al_punto_2_11_3_250",
   "type": "Restriccion",
   "label": "Ponderador acciones grupo 1",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Acciones (definidas conforme al punto 2.11.3.): 250"
  },
  {
   "id": "Restriccion_el_activo_recibido_en_garantia_se_limitara_a_aquellos_listados_en_el_punto_5_3_1",
   "type": "Restriccion",
   "label": "Activos limitados a listado",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El activo recibido en garantía se limitará a aquellos listados en el punto 5.3.1.2."
  },
  {
   "id": "Obligacion_la_facultad_de_revocacion_segun_lo_establecido_en_el_apartado_v_del_punto_2_3_1_",
   "type": "Obligacion",
   "label": "Informar facultad de revocación",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La facultad de revocación según lo establecido en el apartado v) del punto 2.3.1.1"
  },
  {
   "id": "Operacion_integracion_de_capitales",
   "type": "Operacion",
   "label": "Integración de capitales mínimos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: integración de capitales"
  },
  {
   "id": "Obligacion_cumplan_las_condiciones_previstas_en_el_punto_7_9_2",
   "type": "Obligacion",
   "label": "Cumplimiento condiciones proyecto",
   "tokens_matcheados": 2,
   "resumen_propiedades": "cumplan las condiciones previstas en el punto 7.9.2."
  }
 ]
}
```

### paso 5 — buscar_nodos {"consulta": "7.3 normas capitales mínimos entidades financieras", "limite": 10}

```json
{
 "consulta": "7.3 normas capitales mínimos entidades financieras",
 "total_con_match": 192,
 "resultados": [
  {
   "id": "Obligacion_las_entidades_financieras_comprendidas_sus_filiales_en_el_pais_y_en_el_exterior_",
   "type": "Obligacion",
   "label": "Observar capitales mínimos en base individual",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Las entidades financieras (comprendidas sus filiales en el país y en el exterior) observarán las normas en materia de capitales mínimos en forma individual."
  },
  {
   "id": "Obligacion_las_entidades_financieras_controlantes_sujetas_a_supervision_consolidada_observa",
   "type": "Obligacion",
   "label": "Observar capitales mínimos en base consolidada",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Las entidades financieras controlantes sujetas a supervisión consolidada observarán las normas en materia de capitales mínimos sobre base consolidada mensual y,…"
  },
  {
   "id": "TextoOrdenado_to_capitales_minimos_actual_pdf",
   "type": "TextoOrdenado",
   "label": "Capitales Mínimos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "materia: capitales minimos; archivo: TO_capitales_minimos_actual.pdf; version: actual"
  },
  {
   "id": "Operacion_transformacion_de_entidades_financieras",
   "type": "Operacion",
   "label": "Transformación de entidades",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: transformación de entidades financieras"
  },
  {
   "id": "Obligacion_las_entidades_financieras_del_grupo_1_deberan_llevar_a_cabo_un_proceso_de_debida",
   "type": "Obligacion",
   "label": "Proceso de debida diligencia",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Las entidades financieras del grupo 1 deberán llevar a cabo un proceso de debida diligencia –al momento del otorgamiento del crédito y con frecuencia mínima anu…"
  },
  {
   "id": "Restriccion_cuando_el_total_de_participaciones_en_el_capital_de_entidades_financieras_empres",
   "type": "Restriccion",
   "label": "Límite tenencias capital 10%",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Cuando el total de participaciones en el capital de entidades financieras, empresas de servicios complementarios de la actividad financiera y compañías de segur…"
  },
  {
   "id": "EntidadFinanciera_entidad_financiera_grupo_2",
   "type": "EntidadFinanciera",
   "label": "Entidades financieras grupo 2",
   "tokens_matcheados": 2,
   "resumen_propiedades": "categoria: entidad financiera grupo 2"
  },
  {
   "id": "Restriccion_impedimento_para_transformacion_de_entidades_financieras_cuando_exista_obligacio",
   "type": "Restriccion",
   "label": "Impedimento de transformación",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Impedimento para transformación de entidades financieras cuando exista obligación de presentar planes de regularización"
  },
  {
   "id": "Obligacion_las_entidades_financieras_ante_requerimientos_de_apertura_de_cuentas_a_la_vista_",
   "type": "Obligacion",
   "label": "Ofrecer caja de ahorros en pesos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Las entidades financieras, ante requerimientos de apertura de cuentas a la vista, deberán ofrecer la Caja de ahorros en pesos con las prestaciones previstas en …"
  },
  {
   "id": "Obligacion_las_entidades_financieras_que_pertenezcan_al_grupo_a_cuya_sociedad_controlante_s",
   "type": "Obligacion",
   "label": "Cumplimiento consolidado Grupo A",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Las entidades financieras que pertenezcan al grupo A, cuya sociedad controlante sea una 'compañía holding' (no entidad financiera), deberán dar cumplimiento a l…"
  }
 ]
}
```

### paso 6 — buscar_nodos {"consulta": "7.3 exigencia capital riesgo operacional límite máximo", "limite": 10}

```json
{
 "consulta": "7.3 exigencia capital riesgo operacional límite máximo",
 "total_con_match": 574,
 "resultados": [
  {
   "id": "Restriccion_la_exigencia_de_capital_por_riesgo_operacional_para_entidades_del_grupo_b_determ",
   "type": "Restriccion",
   "label": "Límite exigencia capital operacional grupo B",
   "tokens_matcheados": 5,
   "resumen_propiedades": "La exigencia de capital por riesgo operacional para entidades del grupo B determinada a través de la aplicación de la expresión descripta en el punto 7.2. hasta…"
  },
  {
   "id": "Restriccion_la_exigencia_de_capital_por_riesgo_operacional_para_entidades_del_grupo_c_determ",
   "type": "Restriccion",
   "label": "Límite exigencia capital operacional grupo C",
   "tokens_matcheados": 5,
   "resumen_propiedades": "La exigencia de capital por riesgo operacional para entidades del grupo C determinada a través de la aplicación de la expresión descripta en el punto 7.2. hasta…"
  },
  {
   "id": "Obligacion_se_determinara_mensualmente_la_exigencia_de_capital_por_riesgo_operacional_cro_m",
   "type": "Obligacion",
   "label": "Informar CRO mensualmente",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Se determinará mensualmente la exigencia de capital por riesgo operacional (CRO) mediante la expresión CRO = BIC x ILM para entidades del Grupo 1"
  },
  {
   "id": "Restriccion_las_exigencias_a_ser_incluidas_dentro_del_calculo_del_promedio_de_erc_se_extiend",
   "type": "Restriccion",
   "label": "Límite exigencia riesgo operacional",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Las exigencias a ser incluidas dentro del cálculo del promedio de ERC se extienden únicamente hasta la que correspondió ser integrada en febrero 2013 (promedios…"
  },
  {
   "id": "Restriccion_limite_maximo_para_la_exigencia_de_capital_de_entidades_financieras_originantes",
   "type": "Restriccion",
   "label": "Límite máximo de exigencia de capital",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Límite máximo para la exigencia de capital de entidades financieras originantes"
  },
  {
   "id": "Operacion_calculo",
   "type": "Operacion",
   "label": "Cálculo exigencia capital riesgo operacional",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Cálculo de K (exigencia de capital promedio de las exposiciones subyacentes); es decir, el ratio entre la suma de las exposiciones subyacentes ponderadas por ri…"
  },
  {
   "id": "Operacion_calculo_de_capital_minimo_por_riesgo_operacional",
   "type": "Operacion",
   "label": "Cálculo exigencia capital mínimo operacional",
   "tokens_matcheados": 4,
   "resumen_propiedades": "tipo: cálculo de capital mínimo por riesgo operacional"
  },
  {
   "id": "Restriccion_la_exigencia_mensual_de_capital_minimo_por_riesgo_operacional_de_las_entidades_f",
   "type": "Restriccion",
   "label": "Exigencia capital mínimo por riesgo operacional",
   "tokens_matcheados": 4,
   "resumen_propiedades": "La exigencia mensual de capital mínimo por riesgo operacional de las entidades financieras de los grupos 1 y 2 correspondiente al primer mes será equivalente al…"
  },
  {
   "id": "Obligacion_aplicar_exigencia_capital_por_riesgo_general_mercado_a_todas_posiciones_derivado",
   "type": "Obligacion",
   "label": "Cálculo riesgo general mercado",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La exigencia de capital por el riesgo general de mercado alcanza a todas las posiciones en instrumentos derivados -de la misma manera que también alcanza a las …"
  },
  {
   "id": "Operacion_calculo_de_exigencia_de_capital_minimo_por_riesgo_de_credito",
   "type": "Operacion",
   "label": "Cálculo exigencia capital mínimo",
   "tokens_matcheados": 3,
   "resumen_propiedades": "tipo: cálculo de exigencia de capital mínimo por riesgo de crédito"
  }
 ]
}
```

### paso 7 — buscar_nodos {"consulta": "límite exigencia capital operacional 7.3", "limite": 10}

```json
{
 "consulta": "límite exigencia capital operacional 7.3",
 "total_con_match": 442,
 "resultados": [
  {
   "id": "Restriccion_la_exigencia_de_capital_por_riesgo_operacional_para_entidades_del_grupo_b_determ",
   "type": "Restriccion",
   "label": "Límite exigencia capital operacional grupo B",
   "tokens_matcheados": 4,
   "resumen_propiedades": "La exigencia de capital por riesgo operacional para entidades del grupo B determinada a través de la aplicación de la expresión descripta en el punto 7.2. hasta…"
  },
  {
   "id": "Restriccion_la_exigencia_de_capital_por_riesgo_operacional_para_entidades_del_grupo_c_determ",
   "type": "Restriccion",
   "label": "Límite exigencia capital operacional grupo C",
   "tokens_matcheados": 4,
   "resumen_propiedades": "La exigencia de capital por riesgo operacional para entidades del grupo C determinada a través de la aplicación de la expresión descripta en el punto 7.2. hasta…"
  },
  {
   "id": "Obligacion_se_determinara_mensualmente_la_exigencia_de_capital_por_riesgo_operacional_cro_m",
   "type": "Obligacion",
   "label": "Informar CRO mensualmente",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Se determinará mensualmente la exigencia de capital por riesgo operacional (CRO) mediante la expresión CRO = BIC x ILM para entidades del Grupo 1"
  },
  {
   "id": "Restriccion_la_exigencia_determinada_a_traves_de_la_aplicacion_de_la_expresion_descripta_en_",
   "type": "Restriccion",
   "label": "Límite 20% grupo A capital mínimo",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La exigencia determinada a través de la aplicación de la expresión descripta en el punto 7.2. no podrá superar el 20% en el caso de entidades del grupo A del pr…"
  },
  {
   "id": "Restriccion_limite_de_reduccion_para_entidades_del_grupo_b_17_en_condicion_general_11_o_7_en",
   "type": "Restriccion",
   "label": "Límite reducción exigencia Grupo B",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Límite de reducción para entidades del Grupo B: 17% en condición general, 11% o 7% en condiciones especiales según calificación"
  },
  {
   "id": "Restriccion_las_exigencias_a_ser_incluidas_dentro_del_calculo_del_promedio_de_erc_se_extiend",
   "type": "Restriccion",
   "label": "Límite exigencia riesgo operacional",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Las exigencias a ser incluidas dentro del cálculo del promedio de ERC se extienden únicamente hasta la que correspondió ser integrada en febrero 2013 (promedios…"
  },
  {
   "id": "Restriccion_limite_maximo_para_la_exigencia_de_capital_de_entidades_financieras_originantes",
   "type": "Restriccion",
   "label": "Límite máximo de exigencia de capital",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Límite máximo para la exigencia de capital de entidades financieras originantes"
  },
  {
   "id": "Restriccion_reduccion_de_exigencia_limitada_a_17_11_7_segun_subcategoria_para_entidades_del_",
   "type": "Restriccion",
   "label": "Límite de reducción exigencia Grupo B",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Reducción de exigencia limitada a 17%, 11%, 7% según subcategoría para entidades del Grupo B"
  },
  {
   "id": "Operacion_calculo",
   "type": "Operacion",
   "label": "Cálculo exigencia capital riesgo operacional",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Cálculo de K (exigencia de capital promedio de las exposiciones subyacentes); es decir, el ratio entre la suma de las exposiciones subyacentes ponderadas por ri…"
  },
  {
   "id": "Operacion_calculo_de_capital_minimo_por_riesgo_operacional",
   "type": "Operacion",
   "label": "Cálculo exigencia capital mínimo operacional",
   "tokens_matcheados": 3,
   "resumen_propiedades": "tipo: cálculo de capital mínimo por riesgo operacional"
  }
 ]
}
```

### paso 8 — ver_nodo {"id": "Restriccion_la_exigencia_de_capital_por_riesgo_operacional_para_entidades_del_grupo_b_determ"}

```json
{
 "id": "Restriccion_la_exigencia_de_capital_por_riesgo_operacional_para_entidades_del_grupo_b_determ",
 "type": "Restriccion",
 "label": "Límite exigencia capital operacional grupo B",
 "properties": {
  "descripcion": "La exigencia de capital por riesgo operacional para entidades del grupo B determinada a través de la aplicación de la expresión descripta en el punto 7.2. hasta el 30/06/26 no podrá superar el 17% del promedio de los últimos 36 meses",
  "tipo": "limite_cuantitativo",
  "umbral": "17%"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Punto 12.3. Para aquellas entidades financieras que sean reclasificadas desde el 01/01/2026"
  }
 ]
}
```

### paso 9 — buscar_nodos {"consulta": "punto 7.3 capital mínimo grupo 2", "limite": 10}

```json
{
 "consulta": "punto 7.3 capital mínimo grupo 2",
 "total_con_match": 360,
 "resultados": [
  {
   "id": "Restriccion_acciones_definidas_conforme_al_punto_2_11_3_250",
   "type": "Restriccion",
   "label": "Ponderador acciones grupo 1",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Acciones (definidas conforme al punto 2.11.3.): 250"
  },
  {
   "id": "Obligacion_cuando_el_pago_a_nombre_del_cliente_encuadre_en_el_punto_10_10_2_3_se_debera_dej",
   "type": "Obligacion",
   "label": "Dejar constancia en reporte",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Cuando el pago a nombre del cliente encuadre en el punto 10.10.2.3., se deberá dejar constancia de tal circunstancia al reportar el boleto de venta a nombre del…"
  },
  {
   "id": "Obligacion_la_facultad_de_revocacion_segun_lo_establecido_en_el_apartado_v_del_punto_2_3_1_",
   "type": "Obligacion",
   "label": "Informar facultad de revocación",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La facultad de revocación según lo establecido en el apartado v) del punto 2.3.1.1"
  },
  {
   "id": "Obligacion_cumplan_las_condiciones_previstas_en_el_punto_7_9_2",
   "type": "Obligacion",
   "label": "Cumplimiento condiciones proyecto",
   "tokens_matcheados": 3,
   "resumen_propiedades": "cumplan las condiciones previstas en el punto 7.9.2."
  },
  {
   "id": "Obligacion_debera_verificar_previamente_que_se_cumplen_la_totalidad_de_requisitos_detallado",
   "type": "Obligacion",
   "label": "Verificar requisitos punto 10.3.2",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Deberá verificar previamente que se cumplen la totalidad de requisitos detallados en el punto 10.3.2."
  },
  {
   "id": "Restriccion_el_17_en_el_caso_de_entidades_del_grupo_b_del_promedio_de_los_ultimos_36_meses_a",
   "type": "Restriccion",
   "label": "Límite 17% grupo B capital mínimo",
   "tokens_matcheados": 3,
   "resumen_propiedades": "El 17% en el caso de entidades del grupo B del promedio de los últimos 36 meses –anteriores al mes a que corresponda la determinación de la exigencia– de la exi…"
  },
  {
   "id": "Restriccion_la_exigencia_determinada_a_traves_de_la_aplicacion_de_la_expresion_descripta_en_",
   "type": "Restriccion",
   "label": "Límite 20% grupo A capital mínimo",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La exigencia determinada a través de la aplicación de la expresión descripta en el punto 7.2. no podrá superar el 20% en el caso de entidades del grupo A del pr…"
  },
  {
   "id": "Excepcion_precancelacion_de_capital_e_intereses_de_titulo_de_deuda_comprendido_en_punto_3_",
   "type": "Excepcion",
   "label": "Precancelación simultánea nuevo título 3.5",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Precancelación de capital e intereses de título de deuda comprendido en punto 3.6 con liquidación de fondos ingresados desde exterior por emisión de nuevo títul…"
  },
  {
   "id": "Restriccion_participaciones_en_el_capital_250",
   "type": "Restriccion",
   "label": "Ponderador participaciones capital grupo 2",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Participaciones en el capital: 250"
  },
  {
   "id": "Obligacion_para_el_registro_de_las_operaciones_del_punto_7_10_2_2_ii_en_el_regimen_informat",
   "type": "Obligacion",
   "label": "Confección de boletos sin movimiento de fondos",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Para el registro de las operaciones del punto 7.10.2.2.ii) en el régimen informativo de operaciones de cambios (RIOC), la entidad encargada del seguimiento debe…"
  }
 ]
}
```

### paso 10 — buscar_nodos {"consulta": "n=0 ningún período ingreso bruto positivo exigencia", "limite": 10}

```json
{
 "consulta": "n=0 ningún período ingreso bruto positivo exigencia",
 "total_con_match": 223,
 "resultados": [
  {
   "id": "Excepcion_si_n_0_ningun_periodo_con_ib_positivo_debera_observarse_una_exigencia_equivalent",
   "type": "Excepcion",
   "label": "Excepción N=0 Grupo 2",
   "tokens_matcheados": 6,
   "resumen_propiedades": "Si n = 0 (ningún período con IB positivo), deberá observarse una exigencia equivalente al límite previsto en el punto 7.3 de las normas sobre Capitales mínimos …"
  },
  {
   "id": "Excepcion_cuando_n_sea_igual_a_cero_n_0_debera_observarse_una_exigencia_equivalente_al_lim",
   "type": "Excepcion",
   "label": "Exigencia de capital cuando n es cero",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Cuando n sea igual a cero (n=0), deberá observarse una exigencia equivalente al límite previsto en el punto 7.3."
  },
  {
   "id": "Obligacion_para_la_determinacion_de_la_exigencia_total_computable_del_periodo_n_se_consider",
   "type": "Obligacion",
   "label": "Determinar exigencia total computable",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Para la determinación de la exigencia total computable del período (n) se considerará el esquema especificado con los códigos de rubros contables"
  },
  {
   "id": "Obligacion_ib_ingreso_bruto_de_periodos_de_12_meses_consecutivos_siempre_que_sea_positivo_c",
   "type": "Obligacion",
   "label": "Calcular ingreso bruto períodos de 12 meses",
   "tokens_matcheados": 3,
   "resumen_propiedades": "IB: ingreso bruto de períodos de 12 meses consecutivos –siempre que sea positivo–, correspondientes a los últimos 36 meses anteriores al mes en que se efectúa e…"
  },
  {
   "id": "Obligacion_reportar_ingreso_bruto",
   "type": "Obligacion",
   "label": "Reportar ingreso bruto",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Se informará el ingreso bruto del período X"
  },
  {
   "id": "Operacion_calculo_de_ingreso_bruto",
   "type": "Operacion",
   "label": "Determinación ingreso bruto",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: calculo de ingreso bruto"
  },
  {
   "id": "Restriccion_aplicacion_de_ccf_del_0_desde_01_01_25_al_30_06_25_y_del_5_desde_01_07_25_al_31_",
   "type": "Restriccion",
   "label": "Aplicación de CCF por período",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Desde el 01/01/25 y hasta el 31/12/25, las entidades financieras clasificadas en el grupo 2 que al 01/01/25 pertenezcan a los grupos B y C deberán convertir los…"
  },
  {
   "id": "Restriccion_n_numero_de_periodos_de_12_meses_consecutivos_en_los_cuales_el_ib_es_positivo_to",
   "type": "Restriccion",
   "label": "Límite máximo de períodos para n",
   "tokens_matcheados": 2,
   "resumen_propiedades": "n: número de períodos de 12 meses consecutivos en los cuales el IB es positivo, tomando en cuenta los últimos 36 meses anteriores al mes en que se efectúa el cá…"
  },
  {
   "id": "Obligacion_calcular_exigencia_enesimo_incumplimiento_n_1",
   "type": "Obligacion",
   "label": "Calcular exigencia enésimo incumplimiento n>1",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La exigencia de capital por riesgo específico para un derivado de crédito de enésimo incumplimiento con n mayor que 1 es el menor entre la suma de las exigencia…"
  },
  {
   "id": "Restriccion_desde_el_01_06_24_y_hasta_el_31_12_24_las_entidades_en_funcionamiento_deberan_ap",
   "type": "Restriccion",
   "label": "Exigencia básica de capital período transición",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Desde el 01/06/24 y hasta el 31/12/24 las entidades en funcionamiento deberán aplicar exigencias de capital de 1.500 millones de pesos para Bancos y 700 millone…"
  }
 ]
}
```

### paso 11 — ver_nodo {"id": "Excepcion_cuando_n_sea_igual_a_cero_n_0_debera_observarse_una_exigencia_equivalente_al_lim"}

```json
{
 "id": "Excepcion_cuando_n_sea_igual_a_cero_n_0_debera_observarse_una_exigencia_equivalente_al_lim",
 "type": "Excepcion",
 "label": "Exigencia de capital cuando n es cero",
 "properties": {
  "descripcion": "Cuando n sea igual a cero (n=0), deberá observarse una exigencia equivalente al límite previsto en el punto 7.3."
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Punto 7.2. Exigencia de capital por riesgo operacional para entidades del grupo 2."
  }
 ]
}
```

### paso 12 — buscar_nodos {"consulta": "7.3 límite máximo capital operacional grupo 2", "limite": 10}

```json
{
 "consulta": "7.3 límite máximo capital operacional grupo 2",
 "total_con_match": 457,
 "resultados": [
  {
   "id": "Restriccion_la_exigencia_de_capital_por_riesgo_operacional_para_entidades_del_grupo_b_determ",
   "type": "Restriccion",
   "label": "Límite exigencia capital operacional grupo B",
   "tokens_matcheados": 4,
   "resumen_propiedades": "La exigencia de capital por riesgo operacional para entidades del grupo B determinada a través de la aplicación de la expresión descripta en el punto 7.2. hasta…"
  },
  {
   "id": "Restriccion_la_exigencia_de_capital_por_riesgo_operacional_para_entidades_del_grupo_c_determ",
   "type": "Restriccion",
   "label": "Límite exigencia capital operacional grupo C",
   "tokens_matcheados": 4,
   "resumen_propiedades": "La exigencia de capital por riesgo operacional para entidades del grupo C determinada a través de la aplicación de la expresión descripta en el punto 7.2. hasta…"
  },
  {
   "id": "Restriccion_acciones_definidas_conforme_al_punto_2_11_3_250",
   "type": "Restriccion",
   "label": "Ponderador acciones grupo 1",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Acciones (definidas conforme al punto 2.11.3.): 250"
  },
  {
   "id": "Restriccion_el_17_en_el_caso_de_entidades_del_grupo_b_del_promedio_de_los_ultimos_36_meses_a",
   "type": "Restriccion",
   "label": "Límite 17% grupo B capital mínimo",
   "tokens_matcheados": 3,
   "resumen_propiedades": "El 17% en el caso de entidades del grupo B del promedio de los últimos 36 meses –anteriores al mes a que corresponda la determinación de la exigencia– de la exi…"
  },
  {
   "id": "Restriccion_la_exigencia_determinada_a_traves_de_la_aplicacion_de_la_expresion_descripta_en_",
   "type": "Restriccion",
   "label": "Límite 20% grupo A capital mínimo",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La exigencia determinada a través de la aplicación de la expresión descripta en el punto 7.2. no podrá superar el 20% en el caso de entidades del grupo A del pr…"
  },
  {
   "id": "Restriccion_limite_de_reduccion_para_entidades_del_grupo_b_17_en_condicion_general_11_o_7_en",
   "type": "Restriccion",
   "label": "Límite reducción exigencia Grupo B",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Límite de reducción para entidades del Grupo B: 17% en condición general, 11% o 7% en condiciones especiales según calificación"
  },
  {
   "id": "Restriccion_numero_de_periodos_de_12_meses_consecutivos_en_los_cuales_el_ib_es_positivo_toma",
   "type": "Restriccion",
   "label": "Máximo períodos IB positivo Grupo 2",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Número de períodos de 12 meses consecutivos en los cuales el IB es positivo, tomando en cuenta los últimos 36 meses anteriores al mes de cálculo. Máximo de n = …"
  },
  {
   "id": "Restriccion_limite_maximo_para_la_exigencia_de_capital_de_entidades_financieras_originantes",
   "type": "Restriccion",
   "label": "Límite máximo de exigencia de capital",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Límite máximo para la exigencia de capital de entidades financieras originantes"
  },
  {
   "id": "Restriccion_reduccion_de_exigencia_limitada_a_17_11_7_segun_subcategoria_para_entidades_del_",
   "type": "Restriccion",
   "label": "Límite de reducción exigencia Grupo B",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Reducción de exigencia limitada a 17%, 11%, 7% según subcategoría para entidades del Grupo B"
  },
  {
   "id": "Restriccion_participaciones_en_el_capital_250",
   "type": "Restriccion",
   "label": "Ponderador participaciones capital grupo 2",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Participaciones en el capital: 250"
  }
 ]
}
```

### paso 13 — buscar_nodos {"consulta": "punto 7.3 máximo 17 por ciento grupo 2", "limite": 10}

```json
{
 "consulta": "punto 7.3 máximo 17 por ciento grupo 2",
 "total_con_match": 634,
 "resultados": [
  {
   "id": "Restriccion_acciones_definidas_conforme_al_punto_2_11_3_250",
   "type": "Restriccion",
   "label": "Ponderador acciones grupo 1",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Acciones (definidas conforme al punto 2.11.3.): 250"
  },
  {
   "id": "Excepcion_excepcion_por_punto_3_13",
   "type": "Excepcion",
   "label": "Excepción por punto 3.13",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Las entidades podrán también en el marco del punto 3.13., sin conformidad previa del BCRA si el requisito estuviese vigente"
  },
  {
   "id": "Obligacion_cuando_el_pago_a_nombre_del_cliente_encuadre_en_el_punto_10_10_2_3_se_debera_dej",
   "type": "Obligacion",
   "label": "Dejar constancia en reporte",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Cuando el pago a nombre del cliente encuadre en el punto 10.10.2.3., se deberá dejar constancia de tal circunstancia al reportar el boleto de venta a nombre del…"
  },
  {
   "id": "Restriccion_la_suscripcion_local_no_supere_el_25_veinticinco_por_ciento_de_la_suscripcion_to",
   "type": "Restriccion",
   "label": "Suscripción local máximo 25%",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La suscripción local no supere el 25% (veinticinco por ciento) de la suscripción total"
  },
  {
   "id": "Excepcion_salvo_que_la_operacion_quedase_comprendida_en_lo_previsto_en_el_punto_10_10_2_11",
   "type": "Excepcion",
   "label": "Excepción por punto 10.10.2.11",
   "tokens_matcheados": 3,
   "resumen_propiedades": "salvo que la operación quedase comprendida en lo previsto en el punto 10.10.2.11"
  },
  {
   "id": "Obligacion_la_facultad_de_revocacion_segun_lo_establecido_en_el_apartado_v_del_punto_2_3_1_",
   "type": "Obligacion",
   "label": "Informar facultad de revocación",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La facultad de revocación según lo establecido en el apartado v) del punto 2.3.1.1"
  },
  {
   "id": "Obligacion_cumplan_las_condiciones_previstas_en_el_punto_7_9_2",
   "type": "Obligacion",
   "label": "Cumplimiento condiciones proyecto",
   "tokens_matcheados": 3,
   "resumen_propiedades": "cumplan las condiciones previstas en el punto 7.9.2."
  },
  {
   "id": "Obligacion_debera_verificar_previamente_que_se_cumplen_la_totalidad_de_requisitos_detallado",
   "type": "Obligacion",
   "label": "Verificar requisitos punto 10.3.2",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Deberá verificar previamente que se cumplen la totalidad de requisitos detallados en el punto 10.3.2."
  },
  {
   "id": "Restriccion_limite_de_reduccion_para_entidades_del_grupo_b_17_en_condicion_general_11_o_7_en",
   "type": "Restriccion",
   "label": "Límite reducción exigencia Grupo B",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Límite de reducción para entidades del Grupo B: 17% en condición general, 11% o 7% en condiciones especiales según calificación"
  },
  {
   "id": "Obligacion_se_determinara_mensualmente_por_la_expresion_cro_a_ib_n_donde_a_es_15_n_es_numer",
   "type": "Obligacion",
   "label": "Determinar CRO mensualmente Grupo 2",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Se determinará mensualmente por la expresión: CRO = (a*IB) / n, donde a es 15%, n es número de períodos de 12 meses consecutivos con IB positivo, máximo 3"
  }
 ]
}
```

### paso 14 — ver_nodo {"id": "Obligacion_se_determinara_mensualmente_por_la_expresion_cro_a_ib_n_donde_a_es_15_n_es_numer"}

```json
{
 "id": "Obligacion_se_determinara_mensualmente_por_la_expresion_cro_a_ib_n_donde_a_es_15_n_es_numer",
 "type": "Obligacion",
 "label": "Determinar CRO mensualmente Grupo 2",
 "properties": {
  "descripcion": "Se determinará mensualmente por la expresión: CRO = (a*IB) / n, donde a es 15%, n es número de períodos de 12 meses consecutivos con IB positivo, máximo 3",
  "tipo": "calculo",
  "plazo": "mensual"
 },
 "provenances": [
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Punto 5.1. Normas de procedimiento (parte 1)"
  }
 ]
}
```

### paso 15 — buscar_nodos {"consulta": "7.3 máximo exigencia capital operacional 17 por ciento", "limite": 10}

```json
{
 "consulta": "7.3 máximo exigencia capital operacional 17 por ciento",
 "total_con_match": 751,
 "resultados": [
  {
   "id": "Obligacion_se_determinara_mensualmente_la_exigencia_de_capital_por_riesgo_operacional_cro_m",
   "type": "Obligacion",
   "label": "Informar CRO mensualmente",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Se determinará mensualmente la exigencia de capital por riesgo operacional (CRO) mediante la expresión CRO = BIC x ILM para entidades del Grupo 1"
  },
  {
   "id": "Operacion_calculo_de_capital_minimo_por_riesgo_operacional",
   "type": "Operacion",
   "label": "Cálculo exigencia capital mínimo operacional",
   "tokens_matcheados": 4,
   "resumen_propiedades": "tipo: cálculo de capital mínimo por riesgo operacional"
  },
  {
   "id": "Restriccion_la_exigencia_de_capital_por_riesgo_operacional_para_entidades_del_grupo_b_determ",
   "type": "Restriccion",
   "label": "Límite exigencia capital operacional grupo B",
   "tokens_matcheados": 4,
   "resumen_propiedades": "La exigencia de capital por riesgo operacional para entidades del grupo B determinada a través de la aplicación de la expresión descripta en el punto 7.2. hasta…"
  },
  {
   "id": "Restriccion_la_exigencia_de_capital_por_riesgo_operacional_para_entidades_del_grupo_c_determ",
   "type": "Restriccion",
   "label": "Límite exigencia capital operacional grupo C",
   "tokens_matcheados": 4,
   "resumen_propiedades": "La exigencia de capital por riesgo operacional para entidades del grupo C determinada a través de la aplicación de la expresión descripta en el punto 7.2. hasta…"
  },
  {
   "id": "Restriccion_la_exigencia_mensual_de_capital_minimo_por_riesgo_operacional_de_las_entidades_f",
   "type": "Restriccion",
   "label": "Exigencia capital mínimo por riesgo operacional",
   "tokens_matcheados": 4,
   "resumen_propiedades": "La exigencia mensual de capital mínimo por riesgo operacional de las entidades financieras de los grupos 1 y 2 correspondiente al primer mes será equivalente al…"
  },
  {
   "id": "Restriccion_la_suscripcion_local_no_supere_el_25_veinticinco_por_ciento_de_la_suscripcion_to",
   "type": "Restriccion",
   "label": "Suscripción local máximo 25%",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La suscripción local no supere el 25% (veinticinco por ciento) de la suscripción total"
  },
  {
   "id": "Obligacion_aplicar_exigencia_capital_por_riesgo_general_mercado_a_todas_posiciones_derivado",
   "type": "Obligacion",
   "label": "Cálculo riesgo general mercado",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La exigencia de capital por el riesgo general de mercado alcanza a todas las posiciones en instrumentos derivados -de la misma manera que también alcanza a las …"
  },
  {
   "id": "Operacion_calculo_de_exigencia_de_capital_minimo_por_riesgo_de_credito",
   "type": "Operacion",
   "label": "Cálculo exigencia capital mínimo",
   "tokens_matcheados": 3,
   "resumen_propiedades": "tipo: cálculo de exigencia de capital mínimo por riesgo de crédito"
  },
  {
   "id": "Restriccion_limite_de_reduccion_para_entidades_del_grupo_b_17_en_condicion_general_11_o_7_en",
   "type": "Restriccion",
   "label": "Límite reducción exigencia Grupo B",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Límite de reducción para entidades del Grupo B: 17% en condición general, 11% o 7% en condiciones especiales según calificación"
  },
  {
   "id": "Restriccion_la_exigencia_de_capital_por_posiciones_de_titulizacion_retenidas_o_recompradas_p",
   "type": "Restriccion",
   "label": "Exigencia máxima capital originante",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La exigencia de capital por posiciones de titulización retenidas o recompradas por la entidad originante no será mayor a la que le correspondería si mantuviera …"
  }
 ]
}
```

