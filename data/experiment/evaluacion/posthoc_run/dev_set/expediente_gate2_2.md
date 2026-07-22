# Expediente de adjudicación — GATE CQN2 — parte 2 (trayectorias)

Por caso: respuesta final íntegra, inventario de pasos con fidelidad runtime↔re-ejecución
(igualdad de largos: `len(json(re-ejecutado)) == output_chars`), apéndice de outputs
completos re-ejecutados. Grafo: run_3 congelado vía loader+GraphIndex.


---

# CQN2-002

## Respuesta final íntegra (trace.final_json)

```json
{
 "respuesta": "Una entidad financiera controlante sujeta a supervisión consolidada debe observar las normas sobre clasificación de deudores sobre base consolidada. Específicamente, las normas del país donde esté situada la casa matriz o entidad controlante deberán abarcar la supervisión sobre base consolidada de las filiales o subsidiarias locales. Adicionalmente, los datos de clasificación de deudores se informarán sobre base individual (código de consolidación 0 ó 1) y consolidada trimestral (código de consolidación 3).",
 "citas": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Punto 2.2. Exclusiones."
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Punto 10.1. Normas de procedimiento"
  }
 ],
 "respondible": true
}
```

(`respondible`: true · tool_calls: 14 · hit_tool_limit: False)

## Inventario de pasos + fidelidad runtime↔re-ejecución

| paso | tool | input | output_chars (runtime) | re-ejecutado | fiel |
|---|---|---|---|---|---|
| 1 | buscar_nodos | `{"consulta": "clasificación de deudores supervisión consolidada", "limite": 10}` | 3110 | 3110 | SÍ |
| 2 | buscar_nodos | `{"consulta": "entidad financiera controlante supervisión consolidada", "limite": 10}` | 3566 | 3566 | SÍ |
| 3 | ver_nodo | `{"id": "Obligacion_las_normas_del_pais_donde_este_situada_la_casa_matriz_o_entidad_co` | 501 | 501 | SÍ |
| 4 | ver_nodo | `{"id": "TextoOrdenado_to_clasificacion_deudores_actual_pdf"}` | 397 | 397 | SÍ |
| 5 | buscar_nodos | `{"consulta": "bases observar normas clasificación deudores consolidada", "limite": 10` | 3305 | 3305 | SÍ |
| 6 | buscar_nodos | `{"consulta": "entidad controlante bases consolidadas individual", "limite": 10}` | 2483 | 2483 | SÍ |
| 7 | ver_vecinos | `{"id": "Obligacion_las_normas_del_pais_donde_este_situada_la_casa_matriz_o_entidad_co` | 843 | 843 | SÍ |
| 8 | buscar_nodos | `{"consulta": "observar normas base consolidada individual controlante", "limite": 10}` | 3356 | 3356 | SÍ |
| 9 | ver_nodo | `{"id": "Obligacion_las_entidades_financieras_controlantes_sujetas_a_supervision_conso` | 581 | 581 | SÍ |
| 10 | buscar_nodos | `{"consulta": "entidades controlantes sujetas supervisión consolidada observar clasifi` | 2967 | 2967 | SÍ |
| 11 | buscar_nodos | `{"consulta": "clasificación deudores base consolidada individual punto 2", "limite": ` | 3312 | 3312 | SÍ |
| 12 | ver_nodo | `{"id": "Obligacion_informacion_base_individual_y_consolidada"}` | 610 | 610 | SÍ |
| 13 | buscar_nodos | `{"consulta": "observarán normas clasificación deudores base consolidada", "limite": 1` | 3268 | 3268 | SÍ |
| 14 | ver_nodo | `{"id": "Restriccion_las_normas_del_pais_donde_este_situada_la_casa_matriz_o_entidad_c` | 525 | 525 | SÍ |

**Fidelidad: 14/14**.

## Apéndice — outputs completos re-ejecutados

### paso 1 — buscar_nodos {"consulta": "clasificación de deudores supervisión consolidada", "limite": 10}

```json
{
 "consulta": "clasificación de deudores supervisión consolidada",
 "total_con_match": 2428,
 "resultados": [
  {
   "id": "TextoOrdenado_to_clasificacion_deudores_actual_pdf",
   "type": "TextoOrdenado",
   "label": "Clasificación de Deudores",
   "tokens_matcheados": 3,
   "resumen_propiedades": "materia: clasificacion_deudores; archivo: TO_clasificacion_deudores_actual.pdf; version: vigente"
  },
  {
   "id": "Operacion_clasificacion_de_deudores_en_situacion_irregular",
   "type": "Operacion",
   "label": "Incremento cartera irregular",
   "tokens_matcheados": 3,
   "resumen_propiedades": "tipo: clasificación de deudores en situación irregular"
  },
  {
   "id": "Restriccion_no_seran_objeto_de_clasificacion_quienes_resulten_deudores_en_operaciones_de_ces",
   "type": "Restriccion",
   "label": "Exclusión de deudores en cesión",
   "tokens_matcheados": 3,
   "resumen_propiedades": "No serán objeto de clasificación quienes resulten deudores en operaciones de cesión sin responsabilidad para el cedente"
  },
  {
   "id": "Operacion_clasificacion_de_deudores",
   "type": "Operacion",
   "label": "Tarea de clasificación de deudores",
   "tokens_matcheados": 3,
   "resumen_propiedades": "tipo: clasificación de deudores"
  },
  {
   "id": "Operacion_revision_de_clasificacion_de_deudores",
   "type": "Operacion",
   "label": "Revisión de clasificación trimestral",
   "tokens_matcheados": 3,
   "resumen_propiedades": "En el curso de cada trimestre calendario, respecto de clientes individualmente considerados cuyas financiaciones comprendidas en algún momento sean equivalentes…"
  },
  {
   "id": "Obligacion_la_clasificacion_de_los_deudores_debera_efectuarse_con_una_periodicidad_que_atie",
   "type": "Obligacion",
   "label": "Efectuar clasificación periódicamente",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La clasificación de los deudores deberá efectuarse con una periodicidad que atienda a su importancia, considerando la totalidad de las financiaciones comprendid…"
  },
  {
   "id": "Restriccion_deudores_que_no_deben_ser_objeto_de_clasificacion",
   "type": "Restriccion",
   "label": "Exclusión de deudores de clasificación",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Deudores que no deben ser objeto de clasificación"
  },
  {
   "id": "Restriccion_los_deudores_cuyas_financiaciones_se_encuentren_cubiertas_totalmente_con_garanti",
   "type": "Restriccion",
   "label": "Prohibición de clasificación por cobertura total",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Los deudores cuyas financiaciones se encuentren cubiertas totalmente con garantías preferidas A no serán objeto de clasificación, sin perjuicio de su informació…"
  },
  {
   "id": "Excepcion_modificacion_en_forma_negativa_de_la_clasificacion_del_cliente_en_la_central_de_",
   "type": "Excepcion",
   "label": "Excepción por cambio negativo en Central de deudores",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Modificación en forma negativa de la clasificación del cliente en la Central de deudores del sistema financiero, llevándola a un grado inferior al de la entidad…"
  },
  {
   "id": "Operacion_clasificacion_de_cartera",
   "type": "Operacion",
   "label": "Agrupación de cartera",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: clasificación de cartera"
  }
 ]
}
```

### paso 2 — buscar_nodos {"consulta": "entidad financiera controlante supervisión consolidada", "limite": 10}

```json
{
 "consulta": "entidad financiera controlante supervisión consolidada",
 "total_con_match": 247,
 "resultados": [
  {
   "id": "Obligacion_las_normas_del_pais_donde_este_situada_la_casa_matriz_o_entidad_controlante_debe",
   "type": "Obligacion",
   "label": "Supervisión sobre base consolidada",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Las normas del país donde esté situada la casa matriz o entidad controlante deberán abarcar la supervisión sobre base consolidada de las filiales o subsidiarias…"
  },
  {
   "id": "Restriccion_las_normas_del_pais_donde_este_situada_la_casa_matriz_o_entidad_controlante_debe",
   "type": "Restriccion",
   "label": "Requisito: supervisión sobre base consolidada",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Las normas del país donde esté situada la casa matriz o entidad controlante deberán abarcar la supervisión sobre base consolidada de las sucursales o subsidiari…"
  },
  {
   "id": "EntidadFinanciera_entidad_controlante",
   "type": "EntidadFinanciera",
   "label": "Entidades controlantes",
   "tokens_matcheados": 2,
   "resumen_propiedades": "categoria: entidad financiera controlante"
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
  },
  {
   "id": "Obligacion_la_entidad_financiera_encargada_del_seguimiento_de_anticipos_y_otras_financiacio",
   "type": "Obligacion",
   "label": "Registrar operación ante BCRA",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La entidad financiera encargada del Seguimiento de anticipos y otras financiaciones de exportación de bienes de las operaciones deberá concretar su registro ant…"
  },
  {
   "id": "Restriccion_cuando_la_suma_de_los_requisitos_de_capital_de_una_entidad_financiera_por_las_ex",
   "type": "Restriccion",
   "label": "Límite requisito capital QCCP",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Cuando la suma de los requisitos de capital de una entidad financiera por las exposiciones con una QCCP sea mayor que la exigencia resultante de la aplicación d…"
  },
  {
   "id": "Obligacion_la_ccp_la_entidad_financiera_la_autoridad_de_control_de_la_ccp_u_otro_organismo_",
   "type": "Obligacion",
   "label": "Calcular requerimiento capital",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La CCP, la entidad financiera, la autoridad de control de la CCP u otro organismo con acceso a los datos requeridos deberá calcular K_CMi, DF_pref y DF_CCP de f…"
  },
  {
   "id": "Obligacion_la_entidad_financiera_designada_debera_notificar_su_nombramiento_a_la_gerencia_p",
   "type": "Obligacion",
   "label": "Notificar nombramiento al BCRA",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La entidad financiera designada deberá notificar su nombramiento a la Gerencia Principal de Exterior y Cambios del BCRA dentro de los 10 (diez) días corridos de…"
  },
  {
   "id": "Obligacion_la_entidad_financiera_ha_concretado_el_registro_de_la_financiacion_ante_el_bcra_",
   "type": "Obligacion",
   "label": "Registrar financiación en RIOC",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La entidad financiera ha concretado el registro de la financiación ante el BCRA a través del régimen informativo de operaciones de cambio (RIOC), una vez verifi…"
  }
 ]
}
```

### paso 3 — ver_nodo {"id": "Obligacion_las_normas_del_pais_donde_este_situada_la_casa_matriz_o_entidad_controlante_debe"}

```json
{
 "id": "Obligacion_las_normas_del_pais_donde_este_situada_la_casa_matriz_o_entidad_controlante_debe",
 "type": "Obligacion",
 "label": "Supervisión sobre base consolidada",
 "properties": {
  "descripcion": "Las normas del país donde esté situada la casa matriz o entidad controlante deberán abarcar la supervisión sobre base consolidada de las filiales o subsidiarias locales",
  "tipo": "otra"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Punto 2.2. Exclusiones."
  }
 ]
}
```

### paso 4 — ver_nodo {"id": "TextoOrdenado_to_clasificacion_deudores_actual_pdf"}

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

### paso 5 — buscar_nodos {"consulta": "bases observar normas clasificación deudores consolidada", "limite": 10}

```json
{
 "consulta": "bases observar normas clasificación deudores consolidada",
 "total_con_match": 102,
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
   "id": "Obligacion_las_normas_del_pais_donde_este_situada_la_casa_matriz_o_entidad_controlante_debe",
   "type": "Obligacion",
   "label": "Supervisión sobre base consolidada",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Las normas del país donde esté situada la casa matriz o entidad controlante deberán abarcar la supervisión sobre base consolidada de las filiales o subsidiarias…"
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
   "id": "Restriccion_las_normas_del_pais_donde_este_situada_la_casa_matriz_o_entidad_controlante_debe",
   "type": "Restriccion",
   "label": "Requisito: supervisión sobre base consolidada",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Las normas del país donde esté situada la casa matriz o entidad controlante deberán abarcar la supervisión sobre base consolidada de las sucursales o subsidiari…"
  }
 ]
}
```

### paso 6 — buscar_nodos {"consulta": "entidad controlante bases consolidadas individual", "limite": 10}

```json
{
 "consulta": "entidad controlante bases consolidadas individual",
 "total_con_match": 234,
 "resultados": [
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
   "id": "Restriccion_las_normas_del_pais_donde_este_situada_la_casa_matriz_o_entidad_controlante_debe",
   "type": "Restriccion",
   "label": "Requisito: supervisión sobre base consolidada",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Las normas del país donde esté situada la casa matriz o entidad controlante deberán abarcar la supervisión sobre base consolidada de las sucursales o subsidiari…"
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

### paso 7 — ver_vecinos {"id": "Obligacion_las_normas_del_pais_donde_este_situada_la_casa_matriz_o_entidad_controlante_debe", "direccion": "ambas"}

```json
{
 "id": "Obligacion_las_normas_del_pais_donde_este_situada_la_casa_matriz_o_entidad_controlante_debe",
 "label": "Supervisión sobre base consolidada",
 "n_salientes_total": 2,
 "n_entrantes_total": 0,
 "salientes": [
  {
   "relation": "establecida_en",
   "vecino_id": "TextoOrdenado_to_clasificacion_deudores_actual_pdf",
   "vecino_label": "Clasificación de Deudores",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "Punto 2.2. Exclusiones."
    }
   ]
  },
  {
   "relation": "aplica_a",
   "vecino_id": "EntidadFinanciera_sucursal_y_subsidiaria_local_de_entidad_financiera",
   "vecino_label": "Sucursales y subsidiarias locales de entidades financieras",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "Punto 2.2. Exclusiones."
    }
   ]
  }
 ],
 "salientes_truncado": false,
 "entrantes": [],
 "entrantes_truncado": false
}
```

### paso 8 — buscar_nodos {"consulta": "observar normas base consolidada individual controlante", "limite": 10}

```json
{
 "consulta": "observar normas base consolidada individual controlante",
 "total_con_match": 35,
 "resultados": [
  {
   "id": "Obligacion_las_normas_del_pais_donde_este_situada_la_casa_matriz_o_entidad_controlante_debe",
   "type": "Obligacion",
   "label": "Supervisión sobre base consolidada",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Las normas del país donde esté situada la casa matriz o entidad controlante deberán abarcar la supervisión sobre base consolidada de las filiales o subsidiarias…"
  },
  {
   "id": "Restriccion_las_normas_del_pais_donde_este_situada_la_casa_matriz_o_entidad_controlante_debe",
   "type": "Restriccion",
   "label": "Requisito: supervisión sobre base consolidada",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Las normas del país donde esté situada la casa matriz o entidad controlante deberán abarcar la supervisión sobre base consolidada de las sucursales o subsidiari…"
  },
  {
   "id": "Obligacion_informacion_base_individual_y_consolidada",
   "type": "Obligacion",
   "label": "Información base individual y consolidada",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Los datos se informarán sobre base individual (código de consolidación 0 ó 1) y consolidada trimestral (código de consolidación 3). Se regirán por los plazos de…"
  },
  {
   "id": "Obligacion_las_entidades_financieras_comprendidas_sus_filiales_en_el_pais_y_en_el_exterior_",
   "type": "Obligacion",
   "label": "Observar capitales mínimos en base individual",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Las entidades financieras (comprendidas sus filiales en el país y en el exterior) observarán las normas en materia de capitales mínimos en forma individual."
  },
  {
   "id": "Obligacion_las_entidades_financieras_controlantes_sujetas_a_supervision_consolidada_observa",
   "type": "Obligacion",
   "label": "Observar capitales mínimos en base consolidada",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Las entidades financieras controlantes sujetas a supervisión consolidada observarán las normas en materia de capitales mínimos sobre base consolidada mensual y,…"
  },
  {
   "id": "Operacion_observancia_de_requisitos_de_capitales_minimos_en_base_individual",
   "type": "Operacion",
   "label": "Observancia capitales mínimos base individual",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: Observancia de requisitos de capitales mínimos en base individual"
  },
  {
   "id": "Operacion_observancia_de_requisitos_de_capitales_minimos_en_base_consolidada_mensual_y_tri",
   "type": "Operacion",
   "label": "Observancia capitales mínimos base consolidada",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: Observancia de requisitos de capitales mínimos en base consolidada mensual y trimestral"
  },
  {
   "id": "EntidadFinanciera_entidad_controlante",
   "type": "EntidadFinanciera",
   "label": "Entidades controlantes",
   "tokens_matcheados": 1,
   "resumen_propiedades": "categoria: entidad financiera controlante"
  },
  {
   "id": "Operacion_basis_transactions",
   "type": "Operacion",
   "label": "Operaciones sobre base",
   "tokens_matcheados": 1,
   "resumen_propiedades": "derivados que referencian la base entre dos factores de riesgo y están denominados en una sola moneda"
  },
  {
   "id": "Obligacion_aplicar_normas_generales",
   "type": "Obligacion",
   "label": "Aplicar normas generales",
   "tokens_matcheados": 1,
   "resumen_propiedades": "A partir de su incorporación al seguimiento resultarán de aplicación las normas generales en la materia"
  }
 ]
}
```

### paso 9 — ver_nodo {"id": "Obligacion_las_entidades_financieras_controlantes_sujetas_a_supervision_consolidada_observa"}

```json
{
 "id": "Obligacion_las_entidades_financieras_controlantes_sujetas_a_supervision_consolidada_observa",
 "type": "Obligacion",
 "label": "Observar capitales mínimos en base consolidada",
 "properties": {
  "descripcion": "Las entidades financieras controlantes sujetas a supervisión consolidada observarán las normas en materia de capitales mínimos sobre base consolidada mensual y, adicional e independientemente, trimestral.",
  "tipo": "otra",
  "plazo": "mensual y trimestral"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Punto 9.1. Base individual."
  }
 ]
}
```

### paso 10 — buscar_nodos {"consulta": "entidades controlantes sujetas supervisión consolidada observar clasificación deudores", "limite": 10}

```json
{
 "consulta": "entidades controlantes sujetas supervisión consolidada observar clasificación deudores",
 "total_con_match": 224,
 "resultados": [
  {
   "id": "Obligacion_las_entidades_financieras_controlantes_sujetas_a_supervision_consolidada_observa",
   "type": "Obligacion",
   "label": "Observar capitales mínimos en base consolidada",
   "tokens_matcheados": 6,
   "resumen_propiedades": "Las entidades financieras controlantes sujetas a supervisión consolidada observarán las normas en materia de capitales mínimos sobre base consolidada mensual y,…"
  },
  {
   "id": "Operacion_inversiones_en_el_capital_de_entidades_financieras_sujetas_a_supervision_consoli",
   "type": "Operacion",
   "label": "Inversiones en capital entidades financieras",
   "tokens_matcheados": 3,
   "resumen_propiedades": "tipo: Inversiones en el capital de entidades financieras sujetas a supervisión consolidada"
  },
  {
   "id": "EntidadFinanciera_subsidiaria_sujeta_a_supervision_consolidada",
   "type": "EntidadFinanciera",
   "label": "Subsidiarias sujetas a supervisión consolidada",
   "tokens_matcheados": 3,
   "resumen_propiedades": "categoria: subsidiaria"
  },
  {
   "id": "EntidadFinanciera_entidad_controlante",
   "type": "EntidadFinanciera",
   "label": "Entidades controlantes",
   "tokens_matcheados": 2,
   "resumen_propiedades": "categoria: entidad financiera controlante"
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
   "id": "EntidadFinanciera_empresa_no_sujeta_supervision",
   "type": "EntidadFinanciera",
   "label": "Empresas no sujetas supervisión",
   "tokens_matcheados": 2,
   "resumen_propiedades": "categoria: empresa no sujeta a supervisión consolidada"
  },
  {
   "id": "Restriccion_no_seran_objeto_de_clasificacion_quienes_resulten_deudores_en_operaciones_de_ces",
   "type": "Restriccion",
   "label": "Exclusión de deudores en cesión",
   "tokens_matcheados": 2,
   "resumen_propiedades": "No serán objeto de clasificación quienes resulten deudores en operaciones de cesión sin responsabilidad para el cedente"
  },
  {
   "id": "Obligacion_las_normas_del_pais_donde_este_situada_la_casa_matriz_o_entidad_controlante_debe",
   "type": "Obligacion",
   "label": "Supervisión sobre base consolidada",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Las normas del país donde esté situada la casa matriz o entidad controlante deberán abarcar la supervisión sobre base consolidada de las filiales o subsidiarias…"
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

### paso 11 — buscar_nodos {"consulta": "clasificación deudores base consolidada individual punto 2", "limite": 10}

```json
{
 "consulta": "clasificación deudores base consolidada individual punto 2",
 "total_con_match": 165,
 "resultados": [
  {
   "id": "Obligacion_informacion_base_individual_y_consolidada",
   "type": "Obligacion",
   "label": "Información base individual y consolidada",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Los datos se informarán sobre base individual (código de consolidación 0 ó 1) y consolidada trimestral (código de consolidación 3). Se regirán por los plazos de…"
  },
  {
   "id": "Obligacion_a_los_fines_de_asignar_los_ponderadores_de_riesgo_previstos_en_el_punto_2_12_las",
   "type": "Obligacion",
   "label": "Considerar definiciones clasificación empresas",
   "tokens_matcheados": 3,
   "resumen_propiedades": "A los fines de asignar los ponderadores de riesgo previstos en el punto 2.12., las entidades financieras deberán considerar las siguientes definiciones"
  },
  {
   "id": "Restriccion_los_deudores_que_hayan_recibido_credito_adicional_en_los_terminos_del_punto_2_2_",
   "type": "Restriccion",
   "label": "Permanencia en categoría por crédito adicional",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Los deudores que hayan recibido crédito adicional en los términos del punto 2.2.5. y en la medida en que dicha financiación no hubiese sido cancelada, deberán p…"
  },
  {
   "id": "TextoOrdenado_to_clasificacion_deudores_actual_pdf",
   "type": "TextoOrdenado",
   "label": "Clasificación de Deudores",
   "tokens_matcheados": 2,
   "resumen_propiedades": "materia: clasificacion_deudores; archivo: TO_clasificacion_deudores_actual.pdf; version: vigente"
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
   "id": "Operacion_clasificacion_de_deudores_en_situacion_irregular",
   "type": "Operacion",
   "label": "Incremento cartera irregular",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: clasificación de deudores en situación irregular"
  },
  {
   "id": "Excepcion_salvo_que_la_operacion_quedase_comprendida_en_lo_previsto_en_el_punto_10_10_2_11",
   "type": "Excepcion",
   "label": "Excepción por punto 10.10.2.11",
   "tokens_matcheados": 2,
   "resumen_propiedades": "salvo que la operación quedase comprendida en lo previsto en el punto 10.10.2.11"
  },
  {
   "id": "Obligacion_la_facultad_de_revocacion_segun_lo_establecido_en_el_apartado_v_del_punto_2_3_1_",
   "type": "Obligacion",
   "label": "Informar facultad de revocación",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La facultad de revocación según lo establecido en el apartado v) del punto 2.3.1.1"
  },
  {
   "id": "Restriccion_no_seran_objeto_de_clasificacion_quienes_resulten_deudores_en_operaciones_de_ces",
   "type": "Restriccion",
   "label": "Exclusión de deudores en cesión",
   "tokens_matcheados": 2,
   "resumen_propiedades": "No serán objeto de clasificación quienes resulten deudores en operaciones de cesión sin responsabilidad para el cedente"
  }
 ]
}
```

### paso 12 — ver_nodo {"id": "Obligacion_informacion_base_individual_y_consolidada"}

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

### paso 13 — buscar_nodos {"consulta": "observarán normas clasificación deudores base consolidada", "limite": 10}

```json
{
 "consulta": "observarán normas clasificación deudores base consolidada",
 "total_con_match": 103,
 "resultados": [
  {
   "id": "Obligacion_las_normas_del_pais_donde_este_situada_la_casa_matriz_o_entidad_controlante_debe",
   "type": "Obligacion",
   "label": "Supervisión sobre base consolidada",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Las normas del país donde esté situada la casa matriz o entidad controlante deberán abarcar la supervisión sobre base consolidada de las filiales o subsidiarias…"
  },
  {
   "id": "Restriccion_las_normas_del_pais_donde_este_situada_la_casa_matriz_o_entidad_controlante_debe",
   "type": "Restriccion",
   "label": "Requisito: supervisión sobre base consolidada",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Las normas del país donde esté situada la casa matriz o entidad controlante deberán abarcar la supervisión sobre base consolidada de las sucursales o subsidiari…"
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
   "id": "Restriccion_deudores_que_no_deben_ser_objeto_de_clasificacion",
   "type": "Restriccion",
   "label": "Exclusión de deudores de clasificación",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Deudores que no deben ser objeto de clasificación"
  },
  {
   "id": "Obligacion_informacion_base_individual_y_consolidada",
   "type": "Obligacion",
   "label": "Información base individual y consolidada",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Los datos se informarán sobre base individual (código de consolidación 0 ó 1) y consolidada trimestral (código de consolidación 3). Se regirán por los plazos de…"
  }
 ]
}
```

### paso 14 — ver_nodo {"id": "Restriccion_las_normas_del_pais_donde_este_situada_la_casa_matriz_o_entidad_controlante_debe"}

```json
{
 "id": "Restriccion_las_normas_del_pais_donde_este_situada_la_casa_matriz_o_entidad_controlante_debe",
 "type": "Restriccion",
 "label": "Requisito: supervisión sobre base consolidada",
 "properties": {
  "descripcion": "Las normas del país donde esté situada la casa matriz o entidad controlante deberán abarcar la supervisión sobre base consolidada de las sucursales o subsidiarias locales",
  "tipo": "limite_cualitativo"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Punto 2.2. Exclusiones."
  }
 ]
}
```



---

# CQN2-004

## Respuesta final íntegra (trace.final_json)

```json
{
 "respuesta": "La exigencia de capital mínimo por riesgo de mercado de una entidad financiera se determina mediante el Método de Medición Estándar previsto en el punto 6.1.4 de la normativa de Capitales Mínimos del BCRA. Para el cálculo de la exigencia de capital por riesgo general de mercado, se utiliza el método de plazos residuales, que obtiene la exigencia como la suma de: el valor absoluto de la posición ponderada neta, un porcentaje de desestimación vertical, porcentajes de desestimación horizontal, y el cambio neto en opciones. Adicionalmente, la exigencia por riesgo de mercado se determina computando el mayor valor entre dos códigos de cálculo específicos (70810000 y 70820000). Para posiciones en opciones, las entidades pueden utilizar un método simplificado si cumplen ciertos límites, o alternativamente pueden informar la exigencia mediante cálculos de Gamma y Vega.",
 "citas": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Punto 6.1. Exigencia."
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Punto 6.2. Exigencia de capital por riesgo de tasa de interés. (parte 2)"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Punto 12.2. Determinación de la exigencia por riesgo de mercado según punto 5. de la Comunic"
  }
 ],
 "respondible": true
}
```

(`respondible`: true · tool_calls: 15 · hit_tool_limit: True)

## Inventario de pasos + fidelidad runtime↔re-ejecución

| paso | tool | input | output_chars (runtime) | re-ejecutado | fiel |
|---|---|---|---|---|---|
| 1 | buscar_nodos | `{"consulta": "capital mínimo riesgo de mercado", "limite": 10}` | 3333 | 3333 | SÍ |
| 2 | buscar_nodos | `{"consulta": "exigencia capital riesgo mercado método cálculo", "limite": 10}` | 3200 | 3200 | SÍ |
| 3 | ver_nodo | `{"id": "Operacion_medicion_de_capital_minimo"}` | 397 | 397 | SÍ |
| 4 | ver_nodo | `{"id": "Operacion_determinacion_de_exigencia_por_riesgo_de_mercado"}` | 580 | 580 | SÍ |
| 5 | ver_nodo | `{"id": "Operacion_calculo_de_riesgo_de_mercado"}` | 589 | 589 | SÍ |
| 6 | buscar_nodos | `{"consulta": "método plazos residuales riesgo mercado", "limite": 10}` | 3678 | 3678 | SÍ |
| 7 | buscar_nodos | `{"consulta": "método valor en riesgo VaR riesgo mercado", "limite": 10}` | 3694 | 3694 | SÍ |
| 8 | ver_nodo | `{"id": "Operacion_calculo_de_capital_por_metodo_de_plazos_residuales"}` | 614 | 614 | SÍ |
| 9 | ver_vecinos | `{"id": "Operacion_calculo_de_capital_por_metodo_de_plazos_residuales", "direccion": "` | 507 | 507 | SÍ |
| 10 | buscar_nodos | `{"consulta": "método estándar riesgo mercado opciones", "limite": 10}` | 3572 | 3572 | SÍ |
| 11 | buscar_nodos | `{"consulta": "punto 6 riesgo mercado exigencia capital", "limite": 10}` | 3447 | 3447 | SÍ |
| 12 | buscar_nodos | `{"consulta": "Método Medición Estándar punto 6.1.4", "limite": 10}` | 3233 | 3233 | SÍ |
| 13 | ver_vecinos | `{"id": "Operacion_medicion_de_capital_minimo", "direccion": "salientes"}` | 196 | 196 | SÍ |
| 14 | ver_nodo | `{"id": "Obligacion_emplear_metodo_medicion_estandar"}` | 387 | 387 | SÍ |
| 15 | ver_vecinos | `{"id": "Obligacion_emplear_metodo_medicion_estandar", "direccion": "salientes"}` | 871 | 871 | SÍ |

**Fidelidad: 15/15**.

## Apéndice — outputs completos re-ejecutados

### paso 1 — buscar_nodos {"consulta": "capital mínimo riesgo de mercado", "limite": 10}

```json
{
 "consulta": "capital mínimo riesgo de mercado",
 "total_con_match": 2481,
 "resultados": [
  {
   "id": "Operacion_medicion_de_capital_minimo",
   "type": "Operacion",
   "label": "Medición de exigencia por riesgo de mercado",
   "tokens_matcheados": 5,
   "resumen_propiedades": "Medición de la exigencia por riesgo de mercado conforme a lo dispuesto en el punto 6.10"
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
   "id": "Operacion_calculo_de_capital_minimo_por_riesgo_operacional",
   "type": "Operacion",
   "label": "Cálculo exigencia capital mínimo operacional",
   "tokens_matcheados": 4,
   "resumen_propiedades": "tipo: cálculo de capital mínimo por riesgo operacional"
  },
  {
   "id": "Operacion_calculo_de_capital_por_metodo_de_plazos_residuales",
   "type": "Operacion",
   "label": "Cálculo capital por riesgo general de mercado",
   "tokens_matcheados": 4,
   "resumen_propiedades": "La exigencia de capital se obtendrá como la suma de: el valor absoluto de la posición ponderada neta, un porcentaje de desestimación vertical, porcentajes de de…"
  },
  {
   "id": "Restriccion_la_exigencia_mensual_de_capital_minimo_por_riesgo_operacional_de_las_entidades_f",
   "type": "Restriccion",
   "label": "Exigencia capital mínimo por riesgo operacional",
   "tokens_matcheados": 4,
   "resumen_propiedades": "La exigencia mensual de capital mínimo por riesgo operacional de las entidades financieras de los grupos 1 y 2 correspondiente al primer mes será equivalente al…"
  },
  {
   "id": "Restriccion_exigencia_de_capital_por_riesgo_general_de_mercado",
   "type": "Restriccion",
   "label": "Exigencia de capital por riesgo general de mercado",
   "tokens_matcheados": 4,
   "resumen_propiedades": "La exigencia de capital por riesgo general de mercado es la diferencia entre el total de posiciones compradas y el total de posiciones vendidas en cada mercado …"
  },
  {
   "id": "Restriccion_la_parte_de_la_exposicion_cubierta_recibira_el_ponderador_de_riesgo_correspondie",
   "type": "Restriccion",
   "label": "Ponderador mínimo 20%",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La parte de la exposición cubierta recibirá el ponderador de riesgo correspondiente al activo recibido en garantía, pero estará sujeta a un mínimo del 20% –salv…"
  },
  {
   "id": "Restriccion_los_bancos_deberan_mantener_una_exigencia_basica_de_capital_minimo_de_5_000_mill",
   "type": "Restriccion",
   "label": "Exigencia básica bancos",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Los bancos deberán mantener una exigencia básica de capital mínimo de 5.000 millones de pesos"
  },
  {
   "id": "Obligacion_se_determinara_mensualmente_la_exigencia_de_capital_por_riesgo_operacional_cro_m",
   "type": "Obligacion",
   "label": "Informar CRO mensualmente",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Se determinará mensualmente la exigencia de capital por riesgo operacional (CRO) mediante la expresión CRO = BIC x ILM para entidades del Grupo 1"
  }
 ]
}
```

### paso 2 — buscar_nodos {"consulta": "exigencia capital riesgo mercado método cálculo", "limite": 10}

```json
{
 "consulta": "exigencia capital riesgo mercado método cálculo",
 "total_con_match": 532,
 "resultados": [
  {
   "id": "Obligacion_aplicar_exigencia_capital_por_riesgo_general_mercado_a_todas_posiciones_derivado",
   "type": "Obligacion",
   "label": "Cálculo riesgo general mercado",
   "tokens_matcheados": 5,
   "resumen_propiedades": "La exigencia de capital por el riesgo general de mercado alcanza a todas las posiciones en instrumentos derivados -de la misma manera que también alcanza a las …"
  },
  {
   "id": "Operacion_calculo_de_capital_por_metodo_de_plazos_residuales",
   "type": "Operacion",
   "label": "Cálculo capital por riesgo general de mercado",
   "tokens_matcheados": 5,
   "resumen_propiedades": "La exigencia de capital se obtendrá como la suma de: el valor absoluto de la posición ponderada neta, un porcentaje de desestimación vertical, porcentajes de de…"
  },
  {
   "id": "Operacion_calculo_de_exigencia_de_capital_minimo_por_riesgo_de_credito",
   "type": "Operacion",
   "label": "Cálculo exigencia capital mínimo",
   "tokens_matcheados": 4,
   "resumen_propiedades": "tipo: cálculo de exigencia de capital mínimo por riesgo de crédito"
  },
  {
   "id": "Operacion_determinacion_de_exigencia_por_riesgo_de_mercado",
   "type": "Operacion",
   "label": "Cálculo exigencia riesgo mercado",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Determinación del importe a consignar en la partida 70800000 (exigencia por riesgo de mercado) computando el mayor valor entre el código 70810000 y 70820000"
  },
  {
   "id": "Operacion_calculo_de_riesgo_de_mercado",
   "type": "Operacion",
   "label": "Cálculo exigencia riesgo de mercado",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Datos complementarios vinculados al cálculo de la exigencia por riesgo de mercado (puntos 4.3., 4.4. y 4.5. de la Sección 4.) en base individual y consolidado m…"
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
  }
 ]
}
```

### paso 3 — ver_nodo {"id": "Operacion_medicion_de_capital_minimo"}

```json
{
 "id": "Operacion_medicion_de_capital_minimo",
 "type": "Operacion",
 "label": "Medición de exigencia por riesgo de mercado",
 "properties": {
  "tipo": "medición de capital mínimo",
  "description": "Medición de la exigencia por riesgo de mercado conforme a lo dispuesto en el punto 6.10"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Punto 6.12. Auditoría interna."
  }
 ]
}
```

### paso 4 — ver_nodo {"id": "Operacion_determinacion_de_exigencia_por_riesgo_de_mercado"}

```json
{
 "id": "Operacion_determinacion_de_exigencia_por_riesgo_de_mercado",
 "type": "Operacion",
 "label": "Cálculo exigencia riesgo mercado",
 "properties": {
  "tipo": "determinación de exigencia por riesgo de mercado",
  "description": "Determinación del importe a consignar en la partida 70800000 (exigencia por riesgo de mercado) computando el mayor valor entre el código 70810000 y 70820000"
 },
 "provenances": [
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Punto 12.2. Determinación de la exigencia por riesgo de mercado según punto 5. de la Comunic"
  }
 ]
}
```

### paso 5 — ver_nodo {"id": "Operacion_calculo_de_riesgo_de_mercado"}

```json
{
 "id": "Operacion_calculo_de_riesgo_de_mercado",
 "type": "Operacion",
 "label": "Cálculo exigencia riesgo de mercado",
 "properties": {
  "tipo": "cálculo de riesgo de mercado",
  "description": "Datos complementarios vinculados al cálculo de la exigencia por riesgo de mercado (puntos 4.3., 4.4. y 4.5. de la Sección 4.) en base individual y consolidado mensual (códigos de consolidación 0 o 1 y 2)"
 },
 "provenances": [
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Punto 1.1. La información tendrá frecuencia mensual y se integrará con datos referidos al m"
  }
 ]
}
```

### paso 6 — buscar_nodos {"consulta": "método plazos residuales riesgo mercado", "limite": 10}

```json
{
 "consulta": "método plazos residuales riesgo mercado",
 "total_con_match": 319,
 "resultados": [
  {
   "id": "Operacion_calculo_de_capital_por_metodo_de_plazos_residuales",
   "type": "Operacion",
   "label": "Cálculo capital por riesgo general de mercado",
   "tokens_matcheados": 5,
   "resumen_propiedades": "La exigencia de capital se obtendrá como la suma de: el valor absoluto de la posición ponderada neta, un porcentaje de desestimación vertical, porcentajes de de…"
  },
  {
   "id": "Obligacion_aplicar_exigencia_capital_por_riesgo_general_mercado_a_todas_posiciones_derivado",
   "type": "Obligacion",
   "label": "Cálculo riesgo general mercado",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La exigencia de capital por el riesgo general de mercado alcanza a todas las posiciones en instrumentos derivados -de la misma manera que también alcanza a las …"
  },
  {
   "id": "Operacion_determinacion_de_exigencia_por_riesgo_de_mercado",
   "type": "Operacion",
   "label": "Cálculo exigencia riesgo mercado",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Determinación del importe a consignar en la partida 70800000 (exigencia por riesgo de mercado) computando el mayor valor entre el código 70810000 y 70820000"
  },
  {
   "id": "Operacion_acceso_al_mercado_de_cambios_para_pago_de_servicios_con_antelacion_a_plazos_prev",
   "type": "Operacion",
   "label": "Pago de servicios con anticipación",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: acceso al mercado de cambios para pago de servicios con antelación a plazos previstos"
  },
  {
   "id": "Operacion_calculo_de_riesgo_de_mercado",
   "type": "Operacion",
   "label": "Cálculo exigencia riesgo de mercado",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Datos complementarios vinculados al cálculo de la exigencia por riesgo de mercado (puntos 4.3., 4.4. y 4.5. de la Sección 4.) en base individual y consolidado m…"
  },
  {
   "id": "Obligacion_la_reduccion_o_transferencia_del_riesgo_de_credito_a_traves_del_uso_de_tecnicas_",
   "type": "Obligacion",
   "label": "Control de riesgos residuales en CRC",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La reducción o transferencia del riesgo de crédito a través del uso de técnicas de CRC puede incrementar –al mismo tiempo– otros riesgos residuales, tales como …"
  },
  {
   "id": "Obligacion_las_reglas_de_neteo_offseting_rules_para_el_riesgo_de_mercado_se_aplicaran_en_ba",
   "type": "Obligacion",
   "label": "Aplicar reglas de neteo consolidadas",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Las reglas de neteo ('offseting rules') para el riesgo de mercado se aplicarán en base consolidada o subconsolidada, según corresponda."
  },
  {
   "id": "Obligacion_los_importes_por_debajo_del_umbral_que_no_se_deducen_se_ponderan_en_funcion_del_",
   "type": "Obligacion",
   "label": "Ponderar importes por riesgo o mercado",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Los importes por debajo del umbral, que no se deducen, se ponderan en función del riesgo o se consideran para el cómputo de la exigencia por riesgo de mercado, …"
  },
  {
   "id": "Obligacion_este_riesgo_se_discriminara_por_mercado_entendido_a_estos_efectos_como_el_pais_e",
   "type": "Obligacion",
   "label": "Discriminación de riesgo por mercado país",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Este riesgo se discriminará por mercado, entendido a estos efectos como el país en que se negocien posiciones compradas o vendidas en acciones. El país se ident…"
  },
  {
   "id": "Obligacion_los_divisas_deben_haber_ingresado_por_el_mercado_de_cambios_en_los_plazos_establ",
   "type": "Obligacion",
   "label": "Ingreso de divisas en plazos establecidos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Los divisas deben haber ingresado por el mercado de cambios en los plazos establecidos en cada caso"
  }
 ]
}
```

### paso 7 — buscar_nodos {"consulta": "método valor en riesgo VaR riesgo mercado", "limite": 10}

```json
{
 "consulta": "método valor en riesgo VaR riesgo mercado",
 "total_con_match": 1068,
 "resultados": [
  {
   "id": "Restriccion_el_valor_de_mercado_de_la_totalidad_de_las_opciones_en_cartera_no_podra_superar_",
   "type": "Restriccion",
   "label": "Límite valor opciones compradas",
   "tokens_matcheados": 3,
   "resumen_propiedades": "El valor de mercado de la totalidad de las opciones en cartera no podrá superar el 5% de su RPC del mes anterior"
  },
  {
   "id": "Operacion_transferencia_de_garantias_por_cambios_en_valor_de_mercado",
   "type": "Operacion",
   "label": "Intercambio de margen de variación",
   "tokens_matcheados": 3,
   "resumen_propiedades": "tipo: transferencia de garantías por cambios en valor de mercado"
  },
  {
   "id": "Obligacion_cuando_se_trate_de_una_operacion_con_derivados_concertada_en_un_mercado_de_valor",
   "type": "Obligacion",
   "label": "Aplicar tratamiento de derivado OTC",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Cuando se trate de una operación con derivados concertada en un mercado de valores y la transacción entre el miembro compensador y la entidad financiera cliente…"
  },
  {
   "id": "Obligacion_las_reglas_de_neteo_offseting_rules_para_el_riesgo_de_mercado_se_aplicaran_en_ba",
   "type": "Obligacion",
   "label": "Aplicar reglas de neteo consolidadas",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Las reglas de neteo ('offseting rules') para el riesgo de mercado se aplicarán en base consolidada o subconsolidada, según corresponda."
  },
  {
   "id": "Obligacion_ajustar_el_valor_de_la_cobertura_segun_lo_previsto_en_punto_5_4_5",
   "type": "Obligacion",
   "label": "Ajuste valor cobertura método integral",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Para la aplicación del método integral el valor de la cobertura deberá ajustarse conforme a lo establecido en el punto 5.4.5"
  },
  {
   "id": "Obligacion_los_importes_por_debajo_del_umbral_que_no_se_deducen_se_ponderan_en_funcion_del_",
   "type": "Obligacion",
   "label": "Ponderar importes por riesgo o mercado",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Los importes por debajo del umbral, que no se deducen, se ponderan en función del riesgo o se consideran para el cómputo de la exigencia por riesgo de mercado, …"
  },
  {
   "id": "Operacion_calculo_de_capital_por_metodo_de_plazos_residuales",
   "type": "Operacion",
   "label": "Cálculo capital por riesgo general de mercado",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La exigencia de capital se obtendrá como la suma de: el valor absoluto de la posición ponderada neta, un porcentaje de desestimación vertical, porcentajes de de…"
  },
  {
   "id": "Restriccion_en_el_caso_de_pasivos_por_instrumentos_derivados_contabilizados_a_valor_razonabl",
   "type": "Restriccion",
   "label": "Prohibición compensación riesgo crédito derivados",
   "tokens_matcheados": 3,
   "resumen_propiedades": "En el caso de pasivos por instrumentos derivados contabilizados a valor razonable, no se permite la compensación de ajustes de valuación por riesgo de crédito p…"
  },
  {
   "id": "Obligacion_se_consignara_el_valor_de_la_exigencia_por_riesgo_de_posiciones_en_opciones_para",
   "type": "Obligacion",
   "label": "Consignación de exigencia riesgo posiciones opciones",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Se consignará el valor de la exigencia por riesgo de posiciones en opciones para el último día del período (n) determinada conforme a las disposiciones del punt…"
  },
  {
   "id": "Obligacion_exigencia_por_riesgo_de_credito_de_contraparte_en_operaciones_con_derivados_extr",
   "type": "Obligacion",
   "label": "Cálculo de RCD",
   "tokens_matcheados": 2,
   "resumen_propiedades": "exigencia por riesgo de crédito de contraparte en operaciones con derivados extrabursátiles (over-the-counter, OTC), determinada conforme a lo establecido en el…"
  }
 ]
}
```

### paso 8 — ver_nodo {"id": "Operacion_calculo_de_capital_por_metodo_de_plazos_residuales"}

```json
{
 "id": "Operacion_calculo_de_capital_por_metodo_de_plazos_residuales",
 "type": "Operacion",
 "label": "Cálculo capital por riesgo general de mercado",
 "properties": {
  "tipo": "cálculo de capital por método de plazos residuales",
  "description": "La exigencia de capital se obtendrá como la suma de: el valor absoluto de la posición ponderada neta, un porcentaje de desestimación vertical, porcentajes de desestimación horizontal, y el cambio neto en opciones"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Punto 6.2. Exigencia de capital por riesgo de tasa de interés. (parte 2)"
  }
 ]
}
```

### paso 9 — ver_vecinos {"id": "Operacion_calculo_de_capital_por_metodo_de_plazos_residuales", "direccion": "salientes"}

```json
{
 "id": "Operacion_calculo_de_capital_por_metodo_de_plazos_residuales",
 "label": "Cálculo capital por riesgo general de mercado",
 "n_salientes_total": 1,
 "n_entrantes_total": 2,
 "salientes": [
  {
   "relation": "establecida_en",
   "vecino_id": "TextoOrdenado_to_capitales_minimos_actual_pdf",
   "vecino_label": "Capitales Mínimos",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 6.2. Exigencia de capital por riesgo de tasa de interés. (parte 2)"
    }
   ]
  }
 ],
 "salientes_truncado": false
}
```

### paso 10 — buscar_nodos {"consulta": "método estándar riesgo mercado opciones", "limite": 10}

```json
{
 "consulta": "método estándar riesgo mercado opciones",
 "total_con_match": 319,
 "resultados": [
  {
   "id": "Operacion_calculo_de_capital_por_metodo_de_plazos_residuales",
   "type": "Operacion",
   "label": "Cálculo capital por riesgo general de mercado",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La exigencia de capital se obtendrá como la suma de: el valor absoluto de la posición ponderada neta, un porcentaje de desestimación vertical, porcentajes de de…"
  },
  {
   "id": "Obligacion_las_entidades_que_solo_compren_opciones_y_que_cumplan_con_los_limites_podran_usa",
   "type": "Obligacion",
   "label": "Usar método simplificado",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Las entidades que sólo compren opciones y que cumplan con los límites podrán usar el método simplificado previsto en el punto 6.6.2"
  },
  {
   "id": "Obligacion_las_entidades_deberan_informar_exigencia_por_riesgo_en_posiciones_de_opciones_me",
   "type": "Obligacion",
   "label": "Informar riesgo en opciones",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Las entidades deberán informar exigencia por riesgo en posiciones de opciones, mediante método simplificado o cálculos de Gamma y Vega"
  },
  {
   "id": "Obligacion_aplicar_exigencia_capital_por_riesgo_general_mercado_a_todas_posiciones_derivado",
   "type": "Obligacion",
   "label": "Cálculo riesgo general mercado",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La exigencia de capital por el riesgo general de mercado alcanza a todas las posiciones en instrumentos derivados -de la misma manera que también alcanza a las …"
  },
  {
   "id": "Restriccion_el_valor_de_mercado_de_la_totalidad_de_las_opciones_en_cartera_no_podra_superar_",
   "type": "Restriccion",
   "label": "Límite valor opciones compradas",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El valor de mercado de la totalidad de las opciones en cartera no podrá superar el 5% de su RPC del mes anterior"
  },
  {
   "id": "Obligacion_emplear_metodo_medicion_estandar",
   "type": "Obligacion",
   "label": "Emplear Método Medición Estándar",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Para su determinación, las entidades deberán emplear el Método de Medición Estándar previsto en el punto 6.1.4."
  },
  {
   "id": "Operacion_determinacion_de_exigencia_por_riesgo_de_mercado",
   "type": "Operacion",
   "label": "Cálculo exigencia riesgo mercado",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Determinación del importe a consignar en la partida 70800000 (exigencia por riesgo de mercado) computando el mayor valor entre el código 70810000 y 70820000"
  },
  {
   "id": "Operacion_calculo_de_riesgo_de_mercado",
   "type": "Operacion",
   "label": "Cálculo exigencia riesgo de mercado",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Datos complementarios vinculados al cálculo de la exigencia por riesgo de mercado (puntos 4.3., 4.4. y 4.5. de la Sección 4.) en base individual y consolidado m…"
  },
  {
   "id": "Obligacion_las_reglas_de_neteo_offseting_rules_para_el_riesgo_de_mercado_se_aplicaran_en_ba",
   "type": "Obligacion",
   "label": "Aplicar reglas de neteo consolidadas",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Las reglas de neteo ('offseting rules') para el riesgo de mercado se aplicarán en base consolidada o subconsolidada, según corresponda."
  },
  {
   "id": "Obligacion_los_importes_por_debajo_del_umbral_que_no_se_deducen_se_ponderan_en_funcion_del_",
   "type": "Obligacion",
   "label": "Ponderar importes por riesgo o mercado",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Los importes por debajo del umbral, que no se deducen, se ponderan en función del riesgo o se consideran para el cómputo de la exigencia por riesgo de mercado, …"
  }
 ]
}
```

### paso 11 — buscar_nodos {"consulta": "punto 6 riesgo mercado exigencia capital", "limite": 10}

```json
{
 "consulta": "punto 6 riesgo mercado exigencia capital",
 "total_con_match": 525,
 "resultados": [
  {
   "id": "Obligacion_aplicar_exigencia_capital_por_riesgo_general_mercado_a_todas_posiciones_derivado",
   "type": "Obligacion",
   "label": "Cálculo riesgo general mercado",
   "tokens_matcheados": 4,
   "resumen_propiedades": "La exigencia de capital por el riesgo general de mercado alcanza a todas las posiciones en instrumentos derivados -de la misma manera que también alcanza a las …"
  },
  {
   "id": "Operacion_medicion_de_capital_minimo",
   "type": "Operacion",
   "label": "Medición de exigencia por riesgo de mercado",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Medición de la exigencia por riesgo de mercado conforme a lo dispuesto en el punto 6.10"
  },
  {
   "id": "Restriccion_exigencia_de_capital_por_riesgo_general_de_mercado",
   "type": "Restriccion",
   "label": "Exigencia de capital por riesgo general de mercado",
   "tokens_matcheados": 4,
   "resumen_propiedades": "La exigencia de capital por riesgo general de mercado es la diferencia entre el total de posiciones compradas y el total de posiciones vendidas en cada mercado …"
  },
  {
   "id": "Obligacion_se_determinara_mensualmente_la_exigencia_de_capital_por_riesgo_operacional_cro_m",
   "type": "Obligacion",
   "label": "Informar CRO mensualmente",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Se determinará mensualmente la exigencia de capital por riesgo operacional (CRO) mediante la expresión CRO = BIC x ILM para entidades del Grupo 1"
  },
  {
   "id": "Operacion_calculo_de_exigencia_de_capital_minimo_por_riesgo_de_credito",
   "type": "Operacion",
   "label": "Cálculo exigencia capital mínimo",
   "tokens_matcheados": 3,
   "resumen_propiedades": "tipo: cálculo de exigencia de capital mínimo por riesgo de crédito"
  },
  {
   "id": "Operacion_determinacion_de_exigencia_por_riesgo_de_mercado",
   "type": "Operacion",
   "label": "Cálculo exigencia riesgo mercado",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Determinación del importe a consignar en la partida 70800000 (exigencia por riesgo de mercado) computando el mayor valor entre el código 70810000 y 70820000"
  },
  {
   "id": "Operacion_calculo_de_riesgo_de_mercado",
   "type": "Operacion",
   "label": "Cálculo exigencia riesgo de mercado",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Datos complementarios vinculados al cálculo de la exigencia por riesgo de mercado (puntos 4.3., 4.4. y 4.5. de la Sección 4.) en base individual y consolidado m…"
  },
  {
   "id": "Obligacion_calcular_exigencia_capital_por_riesgo",
   "type": "Obligacion",
   "label": "Calcular exigencia capital por riesgo",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La exigencia de capital por riesgo específico para un derivado de crédito de primer incumplimiento será el menor de la suma de las exigencias de capital por rie…"
  },
  {
   "id": "Obligacion_calcular_exigencia_capital_riesgo_vega",
   "type": "Obligacion",
   "label": "Calcular exigencia capital riesgo vega",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La exigencia de capital por el riesgo vega se obtendrá multiplicando la suma de los coeficientes vega de todas las opciones sobre el mismo subyacente por un cam…"
  },
  {
   "id": "Obligacion_calcular_exigencia_capital_riesgo_gamma",
   "type": "Obligacion",
   "label": "Calcular exigencia capital riesgo gamma",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La exigencia de capital total por el riesgo gamma será la suma del valor absoluto de los efectos gamma negativos netos calculados conforme a lo previsto precede…"
  }
 ]
}
```

### paso 12 — buscar_nodos {"consulta": "Método Medición Estándar punto 6.1.4", "limite": 10}

```json
{
 "consulta": "Método Medición Estándar punto 6.1.4",
 "total_con_match": 101,
 "resultados": [
  {
   "id": "Excepcion_con_excepcion_de_los_casos_contemplados_en_el_punto_4_1",
   "type": "Excepcion",
   "label": "Excepción casos punto 4.1",
   "tokens_matcheados": 3,
   "resumen_propiedades": "con excepción de los casos contemplados en el punto 4.1"
  },
  {
   "id": "Obligacion_emplear_metodo_medicion_estandar",
   "type": "Obligacion",
   "label": "Emplear Método Medición Estándar",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Para su determinación, las entidades deberán emplear el Método de Medición Estándar previsto en el punto 6.1.4."
  },
  {
   "id": "Restriccion_los_garantes_admisibles_se_limitan_a_los_estipulados_en_el_punto_5_4_1_los_spe_n",
   "type": "Restriccion",
   "label": "Restricción en garantes admisibles",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Los garantes admisibles se limitan a los estipulados en el punto 5.4.1. Los SPE no son garantes admisibles."
  },
  {
   "id": "Obligacion_ajustar_el_valor_de_la_cobertura_segun_lo_previsto_en_punto_5_4_5",
   "type": "Obligacion",
   "label": "Ajuste valor cobertura método integral",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Para la aplicación del método integral el valor de la cobertura deberá ajustarse conforme a lo establecido en el punto 5.4.5"
  },
  {
   "id": "Obligacion_el_registro_de_reintegros_de_importes_rri_previsto_en_el_punto_3_1_4",
   "type": "Obligacion",
   "label": "Disponibilizar Registro Reintegros Importes",
   "tokens_matcheados": 3,
   "resumen_propiedades": "El Registro de Reintegros de Importes (RRI) previsto en el punto 3.1.4."
  },
  {
   "id": "Excepcion_en_el_caso_de_operaciones_comprendidas_en_el_punto_7_11_1_6_se_admitira_la_cance",
   "type": "Excepcion",
   "label": "Cancelación de intereses por cobros posteriores",
   "tokens_matcheados": 3,
   "resumen_propiedades": "En el caso de operaciones comprendidas en el punto 7.11.1.6, se admitirá la cancelación de intereses mediante la aplicación de cobros de exportaciones de bienes…"
  },
  {
   "id": "Excepcion_el_pago_se_concreta_en_el_marco_de_lo_dispuesto_en_el_punto_4_8_4_por_un_cliente",
   "type": "Excepcion",
   "label": "Pago BOPREAL Serie 1 mínimo 50% deudas elegibles",
   "tokens_matcheados": 3,
   "resumen_propiedades": "El pago se concreta en el marco de lo dispuesto en el punto 4.8.4. por un cliente que suscribió BOPREAL Serie 1 por un monto igual o mayor al 50% (cincuenta por…"
  },
  {
   "id": "Excepcion_el_pago_se_concreta_en_el_marco_de_lo_dispuesto_en_el_punto_4_8_5_por_un_cliente",
   "type": "Excepcion",
   "label": "Pago BOPREAL Serie 1 mínimo 25% deudas elegibles",
   "tokens_matcheados": 3,
   "resumen_propiedades": "El pago se concreta en el marco de lo dispuesto en el punto 4.8.5. por un cliente que suscribió BOPREAL Serie 1 por un monto igual o mayor al 25% (veinticinco p…"
  },
  {
   "id": "Excepcion_no_aplicable_punto_3_12_1",
   "type": "Excepcion",
   "label": "No aplicable punto 3.12.1",
   "tokens_matcheados": 2,
   "resumen_propiedades": "En la medida que no encuadre en el punto 3.12.1"
  },
  {
   "id": "Obligacion_comunicar_con_6_meses_de_anticipacion_cambios_de_metodo",
   "type": "Obligacion",
   "label": "Preaviso cambio de método",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Solo podrán cambiar el método empleado con un preaviso de 6 meses a la SEFYC"
  }
 ]
}
```

### paso 13 — ver_vecinos {"id": "Operacion_medicion_de_capital_minimo", "direccion": "salientes"}

```json
{
 "id": "Operacion_medicion_de_capital_minimo",
 "label": "Medición de exigencia por riesgo de mercado",
 "n_salientes_total": 0,
 "n_entrantes_total": 0,
 "salientes": [],
 "salientes_truncado": false
}
```

### paso 14 — ver_nodo {"id": "Obligacion_emplear_metodo_medicion_estandar"}

```json
{
 "id": "Obligacion_emplear_metodo_medicion_estandar",
 "type": "Obligacion",
 "label": "Emplear Método Medición Estándar",
 "properties": {
  "tipo": "otra",
  "description": "Para su determinación, las entidades deberán emplear el Método de Medición Estándar previsto en el punto 6.1.4."
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Punto 6.1. Exigencia."
  }
 ]
}
```

### paso 15 — ver_vecinos {"id": "Obligacion_emplear_metodo_medicion_estandar", "direccion": "salientes"}

```json
{
 "id": "Obligacion_emplear_metodo_medicion_estandar",
 "label": "Emplear Método Medición Estándar",
 "n_salientes_total": 3,
 "n_entrantes_total": 0,
 "salientes": [
  {
   "relation": "establecida_en",
   "vecino_id": "TextoOrdenado_to_capitales_minimos_actual_pdf",
   "vecino_label": "Capitales Mínimos",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 6.1. Exigencia."
    }
   ]
  },
  {
   "relation": "aplica_a",
   "vecino_id": "EntidadFinanciera_sujeto_obligado",
   "vecino_label": "Sujetos obligados",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 6.1. Exigencia."
    }
   ]
  },
  {
   "relation": "regula",
   "vecino_id": "Operacion_calculo",
   "vecino_label": "Cálculo exigencia capital riesgo operacional",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 6.1. Exigencia."
    }
   ]
  }
 ],
 "salientes_truncado": false
}
```



---

# CQN2-005

## Respuesta final íntegra (trace.final_json)

```json
{
 "respuesta": "En el sistema SEPAIMPO, por cada oficialización del despacho de importación, el importador nomina originalmente una entidad para que se haga responsable del seguimiento de la oficialización. Sin embargo, en la información disponible en el Knowledge Graph no se especifican las condiciones bajo las cuales el importador puede cambiar posteriormente esa entidad nominada. La documentación consultada establece la obligación de nominación inicial, pero no detalla los supuestos o requisitos para modificarla.",
 "citas": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 11.1. Seguimiento de oficializaciones de importación. (parte 1)"
  }
 ],
 "respondible": false
}
```

(`respondible`: false · tool_calls: 16 · hit_tool_limit: True)

## Inventario de pasos + fidelidad runtime↔re-ejecución

| paso | tool | input | output_chars (runtime) | re-ejecutado | fiel |
|---|---|---|---|---|---|
| 1 | buscar_nodos | `{"consulta": "SEPAIMPO seguimiento pagos importaciones", "limite": 10}` | 3353 | 3353 | SÍ |
| 2 | buscar_nodos | `{"consulta": "SEPAIMPO nominación entidad responsable oficialización", "limite": 10}` | 3287 | 3287 | SÍ |
| 3 | ver_nodo | `{"id": "Operacion_nominacion_de_entidad_responsable_del_seguimiento_de_oficializacion` | 585 | 585 | SÍ |
| 4 | ver_nodo | `{"id": "Obligacion_nominar_entidad_responsable"}` | 479 | 479 | SÍ |
| 5 | ver_vecinos | `{"id": "Operacion_nominacion_de_entidad_responsable_del_seguimiento_de_oficializacion` | 278 | 278 | SÍ |
| 6 | buscar_nodos | `{"consulta": "cambio entidad nominada SEPAIMPO importación", "limite": 10}` | 3110 | 3110 | SÍ |
| 7 | buscar_nodos | `{"consulta": "cambiar entidad seguimiento oficialización importación", "limite": 10}` | 3432 | 3432 | SÍ |
| 8 | ver_nodo | `{"id": "Restriccion_procedimiento_de_cambio_cuando_la_entidad_nominada_opto_por_no_op` | 695 | 695 | SÍ |
| 9 | buscar_nodos | `{"consulta": "importador cambio entidad nominada oficialización importación condición` | 3130 | 3130 | SÍ |
| 10 | buscar_nodos | `{"consulta": "modificar entidad nominada importación SEPAIMPO", "limite": 10}` | 3272 | 3272 | SÍ |
| 11 | ver_nodo | `{"id": "Obligacion_cuando_el_beneficiario_desee_modificar_la_entidad_nominada_la_enti` | 577 | 577 | SÍ |
| 12 | buscar_nodos | `{"consulta": "importador nomina entidad seguimiento oficialización importación cambio` | 4953 | 4953 | SÍ |
| 13 | ver_nodo | `{"id": "Operacion_cambio_de_entidad_responsable_del_seguimiento_de_exportacion"}` | 484 | 484 | SÍ |
| 14 | buscar_nodos | `{"consulta": "punto 11.1 seguimiento oficializaciones importación", "limite": 10}` | 2994 | 2994 | SÍ |
| 15 | ver_nodo | `{"id": "Operacion_seguimiento_de_tramites_de_comercio_exterior"}` | 428 | 428 | SÍ |
| 16 | ver_vecinos | `{"id": "Operacion_seguimiento_de_tramites_de_comercio_exterior", "direccion": "ambas"` | 525 | 525 | SÍ |

**Fidelidad: 16/16**.

## Apéndice — outputs completos re-ejecutados

### paso 1 — buscar_nodos {"consulta": "SEPAIMPO seguimiento pagos importaciones", "limite": 10}

```json
{
 "consulta": "SEPAIMPO seguimiento pagos importaciones",
 "total_con_match": 142,
 "resultados": [
  {
   "id": "Operacion_seguimiento_informativo",
   "type": "Operacion",
   "label": "Seguimiento de pagos SEPAIMPO",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Sistema de seguimiento de pagos de importaciones (SEPAIMPO)"
  },
  {
   "id": "Operacion_monitoreo_y_seguimiento",
   "type": "Operacion",
   "label": "Sistema SEPAIMPO",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Sistema de Seguimiento de Pagos de Importaciones que permite monitorear los pagos asociados a una oficialización de importación y la demostración del ingreso de…"
  },
  {
   "id": "Obligacion_por_los_pagos_que_se_realicen_la_entidad_debera_informar_en_el_sepaimpo_dentro_d",
   "type": "Obligacion",
   "label": "Informar CUIT en SEPAIMPO",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Por los pagos que se realicen, la entidad deberá informar en el SEPAIMPO dentro de los 5 (cinco) días hábiles, la CUIT del importador por el cual se ha efectuad…"
  },
  {
   "id": "Obligacion_en_los_casos_de_devoluciones_de_pagos_anticipados_de_importaciones_de_bienes_se_",
   "type": "Obligacion",
   "label": "Identificar pagos devueltos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "En los casos de devoluciones de pagos anticipados de importaciones de bienes se deberá identificar el pago al exterior al que corresponden las divisas devueltas"
  },
  {
   "id": "Restriccion_pagos_sujetos_a_seguimiento",
   "type": "Restriccion",
   "label": "Pagos sujetos a seguimiento",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Los pagos cursados por importaciones con registro de ingreso aduanero pendiente quedarán sujetos a un seguimiento para verificar que se efectúe el registro de i…"
  },
  {
   "id": "EntidadFinanciera_entidad_de_seguimiento_sepaimpo",
   "type": "EntidadFinanciera",
   "label": "Entidad de seguimiento SEPAIMPO",
   "tokens_matcheados": 2,
   "resumen_propiedades": "categoria: entidad de seguimiento de oficializaciones"
  },
  {
   "id": "Obligacion_en_el_caso_de_cancelaciones_del_capital_de_deudas_comerciales_por_importaciones_",
   "type": "Obligacion",
   "label": "Certificación de afectación SEPAIMPO",
   "tokens_matcheados": 2,
   "resumen_propiedades": "En el caso de cancelaciones del capital de deudas comerciales por importaciones de bienes, la entidad deberá contar con la correspondiente certificación de afec…"
  },
  {
   "id": "Obligacion_por_todo_acceso_al_mercado_de_cambios_por_pagos_de_importaciones_de_bienes_argen",
   "type": "Obligacion",
   "label": "Generar número clave de identificación",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Por todo acceso al mercado de cambios por pagos de importaciones de bienes argentinas con registro de ingreso aduanero pendiente, incluyendo las cancelaciones d…"
  },
  {
   "id": "Obligacion_la_entidad_a_cargo_del_seguimiento_de_los_pagos_con_registro_de_ingreso_aduanero",
   "type": "Obligacion",
   "label": "Denuncia de incumplimiento en regularización",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La entidad a cargo del seguimiento de los pagos con registro de ingreso aduanero pendiente deberá, dentro de los 5 (cinco) días hábiles siguientes a la fecha de…"
  },
  {
   "id": "Operacion_pago_de_importaciones",
   "type": "Operacion",
   "label": "Pagos de importaciones con registro aduanero",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Pagos de importaciones de bienes que cuentan con registro de ingreso aduanero"
  }
 ]
}
```

### paso 2 — buscar_nodos {"consulta": "SEPAIMPO nominación entidad responsable oficialización", "limite": 10}

```json
{
 "consulta": "SEPAIMPO nominación entidad responsable oficialización",
 "total_con_match": 249,
 "resultados": [
  {
   "id": "Operacion_nominacion_de_entidad_responsable_del_seguimiento_de_oficializacion",
   "type": "Operacion",
   "label": "Nominación de entidad para seguimiento",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Por cada oficialización del despacho de importación, el importador deberá nominar una entidad para que se haga responsable del seguimiento de la oficialización."
  },
  {
   "id": "Operacion_nominacion_de_responsable",
   "type": "Operacion",
   "label": "Nominación de entidad financiera",
   "tokens_matcheados": 3,
   "resumen_propiedades": "tipo: nominación de responsable"
  },
  {
   "id": "Operacion_nominacion_de_entidad_para_seguimiento_de_exportacion",
   "type": "Operacion",
   "label": "Nominación de entidad responsable",
   "tokens_matcheados": 3,
   "resumen_propiedades": "El exportador deberá seleccionar una entidad como responsable del seguimiento de cada operación de exportación. La designación será inicialmente efectuada al mo…"
  },
  {
   "id": "Obligacion_por_los_pagos_que_se_realicen_la_entidad_debera_informar_en_el_sepaimpo_dentro_d",
   "type": "Obligacion",
   "label": "Informar CUIT en SEPAIMPO",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Por los pagos que se realicen, la entidad deberá informar en el SEPAIMPO dentro de los 5 (cinco) días hábiles, la CUIT del importador por el cual se ha efectuad…"
  },
  {
   "id": "Obligacion_nominar_entidad_responsable",
   "type": "Obligacion",
   "label": "Nominar entidad responsable",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Por cada oficialización del despacho de importación, el importador deberá nominar una entidad para que se haga responsable del seguimiento de la oficialización."
  },
  {
   "id": "EntidadFinanciera_entidad_de_seguimiento_sepaimpo",
   "type": "EntidadFinanciera",
   "label": "Entidad de seguimiento SEPAIMPO",
   "tokens_matcheados": 2,
   "resumen_propiedades": "categoria: entidad de seguimiento de oficializaciones"
  },
  {
   "id": "Obligacion_el_exportador_debera_seleccionar_una_entidad_como_responsable_de_su_seguimiento",
   "type": "Obligacion",
   "label": "Seleccionar entidad responsable",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El exportador deberá seleccionar una entidad como responsable de su seguimiento"
  },
  {
   "id": "Operacion_seleccion_de_entidad",
   "type": "Operacion",
   "label": "Selección de entidad responsable",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Por cada operación comprendida el exportador deberá seleccionar una entidad como responsable de su seguimiento"
  },
  {
   "id": "Obligacion_la_entidad_debera_contar_con_la_correspondiente_certificacion_de_la_entidad_enca",
   "type": "Obligacion",
   "label": "Obtener certificación de SEPAIMPO",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La entidad deberá contar con la correspondiente certificación de la entidad encargada del seguimiento de pago de importaciones de bienes (SEPAIMPO)."
  },
  {
   "id": "Obligacion_la_entidad_sera_la_unica_responsable_de_emitir_los_certificados_de_aplicacion_qu",
   "type": "Obligacion",
   "label": "Emitir certificados de aplicación",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La entidad será la única responsable de emitir los certificados de aplicación que habilitan que los cobros de exportaciones puedan ser imputados a los permisos …"
  }
 ]
}
```

### paso 3 — ver_nodo {"id": "Operacion_nominacion_de_entidad_responsable_del_seguimiento_de_oficializacion"}

```json
{
 "id": "Operacion_nominacion_de_entidad_responsable_del_seguimiento_de_oficializacion",
 "type": "Operacion",
 "label": "Nominación de entidad para seguimiento",
 "properties": {
  "tipo": "nominación de entidad responsable del seguimiento de oficialización",
  "description": "Por cada oficialización del despacho de importación, el importador deberá nominar una entidad para que se haga responsable del seguimiento de la oficialización."
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 11.1. Seguimiento de oficializaciones de importación. (parte 1)"
  }
 ]
}
```

### paso 4 — ver_nodo {"id": "Obligacion_nominar_entidad_responsable"}

```json
{
 "id": "Obligacion_nominar_entidad_responsable",
 "type": "Obligacion",
 "label": "Nominar entidad responsable",
 "properties": {
  "tipo": "asignacion",
  "description": "Por cada oficialización del despacho de importación, el importador deberá nominar una entidad para que se haga responsable del seguimiento de la oficialización."
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 11.1. Seguimiento de oficializaciones de importación. (parte 1)"
  }
 ]
}
```

### paso 5 — ver_vecinos {"id": "Operacion_nominacion_de_entidad_responsable_del_seguimiento_de_oficializacion", "direccion": "ambas"}

```json
{
 "id": "Operacion_nominacion_de_entidad_responsable_del_seguimiento_de_oficializacion",
 "label": "Nominación de entidad para seguimiento",
 "n_salientes_total": 0,
 "n_entrantes_total": 0,
 "salientes": [],
 "salientes_truncado": false,
 "entrantes": [],
 "entrantes_truncado": false
}
```

### paso 6 — buscar_nodos {"consulta": "cambio entidad nominada SEPAIMPO importación", "limite": 10}

```json
{
 "consulta": "cambio entidad nominada SEPAIMPO importación",
 "total_con_match": 318,
 "resultados": [
  {
   "id": "Restriccion_procedimiento_de_cambio_cuando_la_entidad_nominada_opto_por_no_operar_en_comerci",
   "type": "Restriccion",
   "label": "Cambio por opt-out de entidad",
   "tokens_matcheados": 3,
   "resumen_propiedades": "El exportador podrá modificar la entidad cuando la entidad nominada haya optado por no operar en comercio exterior y su última operación de ese tipo sea previa …"
  },
  {
   "id": "Operacion_cambio_de_entidad_nominada_para_emision_de_certificaciones",
   "type": "Operacion",
   "label": "Modificación de entidad nominada",
   "tokens_matcheados": 3,
   "resumen_propiedades": "tipo: cambio de entidad nominada para emisión de certificaciones"
  },
  {
   "id": "Obligacion_cuando_el_beneficiario_desee_modificar_la_entidad_nominada_la_entidad_a_cargo_de",
   "type": "Obligacion",
   "label": "Notificar cambio de entidad nominada",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Cuando el beneficiario desee modificar la entidad nominada, la entidad a cargo del seguimiento deberá notificarle la voluntad del beneficiario a la nueva entida…"
  },
  {
   "id": "EntidadFinanciera_entidad_nominada",
   "type": "EntidadFinanciera",
   "label": "Entidad nominada",
   "tokens_matcheados": 2,
   "resumen_propiedades": "categoria: entidad nominada para seguimiento de permiso"
  },
  {
   "id": "Obligacion_el_cambio_de_entidad_debe_quedar_registrado_en_el_bcra",
   "type": "Obligacion",
   "label": "Registrar cambio en BCRA",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El cambio de entidad debe quedar registrado en el BCRA"
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
   "id": "Obligacion_por_los_pagos_que_se_realicen_la_entidad_debera_informar_en_el_sepaimpo_dentro_d",
   "type": "Obligacion",
   "label": "Informar CUIT en SEPAIMPO",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Por los pagos que se realicen, la entidad deberá informar en el SEPAIMPO dentro de los 5 (cinco) días hábiles, la CUIT del importador por el cual se ha efectuad…"
  },
  {
   "id": "Operacion_registro_del_cambio_de_entidad_en_el_bcra",
   "type": "Operacion",
   "label": "Registro de cambio en BCRA",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: registro del cambio de entidad en el BCRA"
  },
  {
   "id": "EntidadFinanciera_entidad_de_seguimiento_sepaimpo",
   "type": "EntidadFinanciera",
   "label": "Entidad de seguimiento SEPAIMPO",
   "tokens_matcheados": 2,
   "resumen_propiedades": "categoria: entidad de seguimiento de oficializaciones"
  }
 ]
}
```

### paso 7 — buscar_nodos {"consulta": "cambiar entidad seguimiento oficialización importación", "limite": 10}

```json
{
 "consulta": "cambiar entidad seguimiento oficialización importación",
 "total_con_match": 291,
 "resultados": [
  {
   "id": "Operacion_nominacion_de_entidad_responsable_del_seguimiento_de_oficializacion",
   "type": "Operacion",
   "label": "Nominación de entidad para seguimiento",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Por cada oficialización del despacho de importación, el importador deberá nominar una entidad para que se haga responsable del seguimiento de la oficialización."
  },
  {
   "id": "Obligacion_la_entidad_a_cargo_del_seguimiento_debera_notificarle_la_voluntad_del_exportador",
   "type": "Obligacion",
   "label": "Notificar a nueva entidad",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La entidad a cargo del seguimiento deberá notificarle la voluntad del exportador a la nueva entidad"
  },
  {
   "id": "Obligacion_la_entidad_debera_informar_la_asuncion_de_la_tarea_de_seguimiento_al_bcra",
   "type": "Obligacion",
   "label": "Informar asunción al BCRA",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La entidad deberá informar la asunción al BCRA cuando el exportador haya acordado con la entidad la responsabilidad del seguimiento."
  },
  {
   "id": "Operacion_seguimiento_y_registro_de_pago",
   "type": "Operacion",
   "label": "Seguimiento pago importación",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Seguimiento de pagos de importaciones con registro de ingreso aduanero pendiente y efectuar los registros correspondientes en el SEPAIMPO"
  },
  {
   "id": "Obligacion_la_entidad_financiera_encargada_del_seguimiento_de_anticipos_y_otras_financiacio",
   "type": "Obligacion",
   "label": "Registrar operación ante BCRA",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La entidad financiera encargada del Seguimiento de anticipos y otras financiaciones de exportación de bienes de las operaciones deberá concretar su registro ant…"
  },
  {
   "id": "Obligacion_la_entidad_encargada_del_seguimiento_del_permiso_podra_conceder_extensiones_en_e",
   "type": "Obligacion",
   "label": "Conceder extensiones del plazo",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La entidad encargada del seguimiento del permiso podrá conceder extensiones en el plazo de ingreso y liquidación en las circunstancias especificadas"
  },
  {
   "id": "EntidadFinanciera_entidad_de_seguimiento_sepaimpo",
   "type": "EntidadFinanciera",
   "label": "Entidad de seguimiento SEPAIMPO",
   "tokens_matcheados": 2,
   "resumen_propiedades": "categoria: entidad de seguimiento de oficializaciones"
  },
  {
   "id": "Obligacion_el_exportador_debera_seleccionar_una_entidad_como_responsable_de_su_seguimiento",
   "type": "Obligacion",
   "label": "Seleccionar entidad responsable",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El exportador deberá seleccionar una entidad como responsable de su seguimiento"
  },
  {
   "id": "Excepcion_la_entidad_encargada_del_seguimiento_del_permiso_de_embarque_podra_extender_el_p",
   "type": "Excepcion",
   "label": "Prórroga de plazo de liquidación",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La entidad encargada del seguimiento del permiso de embarque podrá extender el plazo de liquidación cuando el cliente haya utilizado el mecanismo de acumulación…"
  },
  {
   "id": "Obligacion_nominar_entidad_para_seguimiento",
   "type": "Obligacion",
   "label": "Nominar entidad para seguimiento",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Los exportadores que pretendan aplicar estas operaciones a embarques oficializados a partir del 02/09/19 deberán nominar una única entidad para que realice el s…"
  }
 ]
}
```

### paso 8 — ver_nodo {"id": "Restriccion_procedimiento_de_cambio_cuando_la_entidad_nominada_opto_por_no_operar_en_comerci"}

```json
{
 "id": "Restriccion_procedimiento_de_cambio_cuando_la_entidad_nominada_opto_por_no_operar_en_comerci",
 "type": "Restriccion",
 "label": "Cambio por opt-out de entidad",
 "properties": {
  "tipo": "limite_cualitativo",
  "descripcion": "Procedimiento de cambio cuando la entidad nominada optó por no operar en comercio exterior",
  "description": "El exportador podrá modificar la entidad cuando la entidad nominada haya optado por no operar en comercio exterior y su última operación de ese tipo sea previa a la fecha de oficialización del permiso de embarque involucrado."
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 8.2. Entidad nominada por el exportador."
  }
 ]
}
```

### paso 9 — buscar_nodos {"consulta": "importador cambio entidad nominada oficialización importación condición", "limite": 10}

```json
{
 "consulta": "importador cambio entidad nominada oficialización importación condición",
 "total_con_match": 326,
 "resultados": [
  {
   "id": "Obligacion_la_entidad_debera_realizar_un_boleto_de_venta_de_cambio_a_nombre_del_importador_",
   "type": "Obligacion",
   "label": "Boleto de venta de cambio",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La entidad deberá realizar un boleto de venta de cambio a nombre del importador por el código de concepto S33. Registro de importaciones de servicios por adjudi…"
  },
  {
   "id": "Restriccion_procedimiento_de_cambio_cuando_la_entidad_nominada_opto_por_no_operar_en_comerci",
   "type": "Restriccion",
   "label": "Cambio por opt-out de entidad",
   "tokens_matcheados": 3,
   "resumen_propiedades": "El exportador podrá modificar la entidad cuando la entidad nominada haya optado por no operar en comercio exterior y su última operación de ese tipo sea previa …"
  },
  {
   "id": "Operacion_cambio_de_entidad_nominada_para_emision_de_certificaciones",
   "type": "Operacion",
   "label": "Modificación de entidad nominada",
   "tokens_matcheados": 3,
   "resumen_propiedades": "tipo: cambio de entidad nominada para emisión de certificaciones"
  },
  {
   "id": "Obligacion_cuando_el_beneficiario_desee_modificar_la_entidad_nominada_la_entidad_a_cargo_de",
   "type": "Obligacion",
   "label": "Notificar cambio de entidad nominada",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Cuando el beneficiario desee modificar la entidad nominada, la entidad a cargo del seguimiento deberá notificarle la voluntad del beneficiario a la nueva entida…"
  },
  {
   "id": "EntidadFinanciera_entidad_nominada",
   "type": "EntidadFinanciera",
   "label": "Entidad nominada",
   "tokens_matcheados": 2,
   "resumen_propiedades": "categoria: entidad nominada para seguimiento de permiso"
  },
  {
   "id": "Obligacion_el_cambio_de_entidad_debe_quedar_registrado_en_el_bcra",
   "type": "Obligacion",
   "label": "Registrar cambio en BCRA",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El cambio de entidad debe quedar registrado en el BCRA"
  },
  {
   "id": "Obligacion_la_entidad_debera_realizar_un_boleto_de_compra_y_o_venta_de_cambio_conforme_a_lo",
   "type": "Obligacion",
   "label": "Realizar boleto de cambio",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La entidad deberá realizar un boleto de compra y/o venta de cambio, conforme a lo estipulado en el punto 5.3"
  },
  {
   "id": "Operacion_registro_del_cambio_de_entidad_en_el_bcra",
   "type": "Operacion",
   "label": "Registro de cambio en BCRA",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: registro del cambio de entidad en el BCRA"
  },
  {
   "id": "Obligacion_la_entidad_interviniente_debera_requerir_al_importador_una_declaracion_jurada_en",
   "type": "Obligacion",
   "label": "Requerir declaración jurada",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La entidad interviniente deberá requerir al importador una declaración jurada en la que identifique la entidad por la cual realizó el pago con registro aduanero…"
  },
  {
   "id": "EntidadFinanciera_entidad_nominada_por_exportador",
   "type": "EntidadFinanciera",
   "label": "Entidad nominada por exportador",
   "tokens_matcheados": 2,
   "resumen_propiedades": "categoria: entidad nominada para seguimiento"
  }
 ]
}
```

### paso 10 — buscar_nodos {"consulta": "modificar entidad nominada importación SEPAIMPO", "limite": 10}

```json
{
 "consulta": "modificar entidad nominada importación SEPAIMPO",
 "total_con_match": 268,
 "resultados": [
  {
   "id": "Obligacion_cuando_el_beneficiario_desee_modificar_la_entidad_nominada_la_entidad_a_cargo_de",
   "type": "Obligacion",
   "label": "Notificar cambio de entidad nominada",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Cuando el beneficiario desee modificar la entidad nominada, la entidad a cargo del seguimiento deberá notificarle la voluntad del beneficiario a la nueva entida…"
  },
  {
   "id": "EntidadFinanciera_entidad_nominada",
   "type": "EntidadFinanciera",
   "label": "Entidad nominada",
   "tokens_matcheados": 2,
   "resumen_propiedades": "categoria: entidad nominada para seguimiento de permiso"
  },
  {
   "id": "Obligacion_por_los_pagos_que_se_realicen_la_entidad_debera_informar_en_el_sepaimpo_dentro_d",
   "type": "Obligacion",
   "label": "Informar CUIT en SEPAIMPO",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Por los pagos que se realicen, la entidad deberá informar en el SEPAIMPO dentro de los 5 (cinco) días hábiles, la CUIT del importador por el cual se ha efectuad…"
  },
  {
   "id": "Restriccion_procedimiento_de_cambio_cuando_la_entidad_nominada_opto_por_no_operar_en_comerci",
   "type": "Restriccion",
   "label": "Cambio por opt-out de entidad",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El exportador podrá modificar la entidad cuando la entidad nominada haya optado por no operar en comercio exterior y su última operación de ese tipo sea previa …"
  },
  {
   "id": "EntidadFinanciera_entidad_de_seguimiento_sepaimpo",
   "type": "EntidadFinanciera",
   "label": "Entidad de seguimiento SEPAIMPO",
   "tokens_matcheados": 2,
   "resumen_propiedades": "categoria: entidad de seguimiento de oficializaciones"
  },
  {
   "id": "EntidadFinanciera_entidad_nominada_por_exportador",
   "type": "EntidadFinanciera",
   "label": "Entidad nominada por exportador",
   "tokens_matcheados": 2,
   "resumen_propiedades": "categoria: entidad nominada para seguimiento"
  },
  {
   "id": "Operacion_cambio_de_entidad_nominada_para_emision_de_certificaciones",
   "type": "Operacion",
   "label": "Modificación de entidad nominada",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: cambio de entidad nominada para emisión de certificaciones"
  },
  {
   "id": "Obligacion_la_entidad_debera_contar_con_la_correspondiente_certificacion_de_la_entidad_enca",
   "type": "Obligacion",
   "label": "Obtener certificación de SEPAIMPO",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La entidad deberá contar con la correspondiente certificación de la entidad encargada del seguimiento de pago de importaciones de bienes (SEPAIMPO)."
  },
  {
   "id": "Obligacion_la_entidad_nominada_podra_emitir_una_certificacion_cuando_se_verifiquen_la_total",
   "type": "Obligacion",
   "label": "Verificar requisitos para emisión",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La entidad nominada podrá emitir una Certificación cuando se verifiquen la totalidad de los siguientes requisitos"
  },
  {
   "id": "Obligacion_la_entidad_nominada_por_un_exportador_debera_notificar_tal_situacion_al_bcra_med",
   "type": "Obligacion",
   "label": "Notificación de nominación al BCRA",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La entidad nominada por un exportador deberá notificar tal situación al BCRA mediante nota dirigida a la Gerencia Principal de Exterior y Cambios dentro de los …"
  }
 ]
}
```

### paso 11 — ver_nodo {"id": "Obligacion_cuando_el_beneficiario_desee_modificar_la_entidad_nominada_la_entidad_a_cargo_de"}

```json
{
 "id": "Obligacion_cuando_el_beneficiario_desee_modificar_la_entidad_nominada_la_entidad_a_cargo_de",
 "type": "Obligacion",
 "label": "Notificar cambio de entidad nominada",
 "properties": {
  "descripcion": "Cuando el beneficiario desee modificar la entidad nominada, la entidad a cargo del seguimiento deberá notificarle la voluntad del beneficiario a la nueva entidad",
  "tipo": "comunicacion_a_cliente"
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 3.17. Acceso con “Certificación por los regímenes de acceso a divisas para la producci"
  }
 ]
}
```

### paso 12 — buscar_nodos {"consulta": "importador nomina entidad seguimiento oficialización importación cambio", "limite": 15}

```json
{
 "consulta": "importador nomina entidad seguimiento oficialización importación cambio",
 "total_con_match": 352,
 "resultados": [
  {
   "id": "Obligacion_la_entidad_debera_realizar_un_boleto_de_venta_de_cambio_a_nombre_del_importador_",
   "type": "Obligacion",
   "label": "Boleto de venta de cambio",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La entidad deberá realizar un boleto de venta de cambio a nombre del importador por el código de concepto S33. Registro de importaciones de servicios por adjudi…"
  },
  {
   "id": "Operacion_cambio_de_entidad_responsable_del_seguimiento_de_exportacion",
   "type": "Operacion",
   "label": "Modificación de entidad de seguimiento",
   "tokens_matcheados": 3,
   "resumen_propiedades": "El exportador podrá modificar la entidad encargada del seguimiento en ciertos casos específicos."
  },
  {
   "id": "Operacion_nominacion_de_entidad_responsable_del_seguimiento_de_oficializacion",
   "type": "Operacion",
   "label": "Nominación de entidad para seguimiento",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Por cada oficialización del despacho de importación, el importador deberá nominar una entidad para que se haga responsable del seguimiento de la oficialización."
  },
  {
   "id": "Obligacion_el_cambio_de_entidad_debe_quedar_registrado_en_el_bcra",
   "type": "Obligacion",
   "label": "Registrar cambio en BCRA",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El cambio de entidad debe quedar registrado en el BCRA"
  },
  {
   "id": "Obligacion_la_entidad_a_cargo_del_seguimiento_debera_notificarle_la_voluntad_del_exportador",
   "type": "Obligacion",
   "label": "Notificar a nueva entidad",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La entidad a cargo del seguimiento deberá notificarle la voluntad del exportador a la nueva entidad"
  },
  {
   "id": "Obligacion_la_entidad_debera_informar_la_asuncion_de_la_tarea_de_seguimiento_al_bcra",
   "type": "Obligacion",
   "label": "Informar asunción al BCRA",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La entidad deberá informar la asunción al BCRA cuando el exportador haya acordado con la entidad la responsabilidad del seguimiento."
  },
  {
   "id": "Obligacion_la_entidad_debera_realizar_un_boleto_de_compra_y_o_venta_de_cambio_conforme_a_lo",
   "type": "Obligacion",
   "label": "Realizar boleto de cambio",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La entidad deberá realizar un boleto de compra y/o venta de cambio, conforme a lo estipulado en el punto 5.3"
  },
  {
   "id": "Operacion_registro_del_cambio_de_entidad_en_el_bcra",
   "type": "Operacion",
   "label": "Registro de cambio en BCRA",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: registro del cambio de entidad en el BCRA"
  },
  {
   "id": "Obligacion_la_entidad_interviniente_debera_requerir_al_importador_una_declaracion_jurada_en",
   "type": "Obligacion",
   "label": "Requerir declaración jurada",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La entidad interviniente deberá requerir al importador una declaración jurada en la que identifique la entidad por la cual realizó el pago con registro aduanero…"
  },
  {
   "id": "Operacion_seguimiento_y_registro_de_pago",
   "type": "Operacion",
   "label": "Seguimiento pago importación",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Seguimiento de pagos de importaciones con registro de ingreso aduanero pendiente y efectuar los registros correspondientes en el SEPAIMPO"
  },
  {
   "id": "Obligacion_la_entidad_financiera_encargada_del_seguimiento_de_anticipos_y_otras_financiacio",
   "type": "Obligacion",
   "label": "Registrar operación ante BCRA",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La entidad financiera encargada del Seguimiento de anticipos y otras financiaciones de exportación de bienes de las operaciones deberá concretar su registro ant…"
  },
  {
   "id": "Restriccion_procedimiento_de_cambio_cuando_la_entidad_nominada_opto_por_no_operar_en_comerci",
   "type": "Restriccion",
   "label": "Cambio por opt-out de entidad",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El exportador podrá modificar la entidad cuando la entidad nominada haya optado por no operar en comercio exterior y su última operación de ese tipo sea previa …"
  },
  {
   "id": "Obligacion_la_entidad_encargada_del_seguimiento_del_permiso_podra_conceder_extensiones_en_e",
   "type": "Obligacion",
   "label": "Conceder extensiones del plazo",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La entidad encargada del seguimiento del permiso podrá conceder extensiones en el plazo de ingreso y liquidación en las circunstancias especificadas"
  },
  {
   "id": "EntidadFinanciera_entidad_de_seguimiento_sepaimpo",
   "type": "EntidadFinanciera",
   "label": "Entidad de seguimiento SEPAIMPO",
   "tokens_matcheados": 2,
   "resumen_propiedades": "categoria: entidad de seguimiento de oficializaciones"
  },
  {
   "id": "Obligacion_el_exportador_debera_seleccionar_una_entidad_como_responsable_de_su_seguimiento",
   "type": "Obligacion",
   "label": "Seleccionar entidad responsable",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El exportador deberá seleccionar una entidad como responsable de su seguimiento"
  }
 ]
}
```

### paso 13 — ver_nodo {"id": "Operacion_cambio_de_entidad_responsable_del_seguimiento_de_exportacion"}

```json
{
 "id": "Operacion_cambio_de_entidad_responsable_del_seguimiento_de_exportacion",
 "type": "Operacion",
 "label": "Modificación de entidad de seguimiento",
 "properties": {
  "tipo": "cambio de entidad responsable del seguimiento de exportación",
  "description": "El exportador podrá modificar la entidad encargada del seguimiento en ciertos casos específicos."
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 8.2. Entidad nominada por el exportador."
  }
 ]
}
```

### paso 14 — buscar_nodos {"consulta": "punto 11.1 seguimiento oficializaciones importación", "limite": 10}

```json
{
 "consulta": "punto 11.1 seguimiento oficializaciones importación",
 "total_con_match": 167,
 "resultados": [
  {
   "id": "Restriccion_acciones_definidas_conforme_al_punto_2_11_3_250",
   "type": "Restriccion",
   "label": "Ponderador acciones grupo 1",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Acciones (definidas conforme al punto 2.11.3.): 250"
  },
  {
   "id": "Operacion_seguimiento_de_tramites_de_comercio_exterior",
   "type": "Operacion",
   "label": "Seguimiento de oficializaciones de importación",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Seguimiento de las oficializaciones de importación en el marco del SEPAIMPO"
  },
  {
   "id": "Excepcion_en_el_caso_de_operaciones_comprendidas_en_el_punto_7_11_1_6_se_admitira_la_cance",
   "type": "Excepcion",
   "label": "Cancelación de intereses por cobros posteriores",
   "tokens_matcheados": 3,
   "resumen_propiedades": "En el caso de operaciones comprendidas en el punto 7.11.1.6, se admitirá la cancelación de intereses mediante la aplicación de cobros de exportaciones de bienes…"
  },
  {
   "id": "Excepcion_con_excepcion_de_los_casos_contemplados_en_el_punto_4_1",
   "type": "Excepcion",
   "label": "Excepción casos punto 4.1",
   "tokens_matcheados": 2,
   "resumen_propiedades": "con excepción de los casos contemplados en el punto 4.1"
  },
  {
   "id": "Excepcion_no_aplicable_punto_3_12_1",
   "type": "Excepcion",
   "label": "No aplicable punto 3.12.1",
   "tokens_matcheados": 2,
   "resumen_propiedades": "En la medida que no encuadre en el punto 3.12.1"
  },
  {
   "id": "Restriccion_el_activo_recibido_en_garantia_se_limitara_a_aquellos_listados_en_el_punto_5_3_1",
   "type": "Restriccion",
   "label": "Activos limitados a listado",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El activo recibido en garantía se limitará a aquellos listados en el punto 5.3.1.2."
  },
  {
   "id": "Operacion_seguimiento_y_registro_de_pago",
   "type": "Operacion",
   "label": "Seguimiento pago importación",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Seguimiento de pagos de importaciones con registro de ingreso aduanero pendiente y efectuar los registros correspondientes en el SEPAIMPO"
  },
  {
   "id": "Excepcion_salvo_que_la_operacion_quedase_comprendida_en_lo_previsto_en_el_punto_10_10_2_11",
   "type": "Excepcion",
   "label": "Excepción por punto 10.10.2.11",
   "tokens_matcheados": 2,
   "resumen_propiedades": "salvo que la operación quedase comprendida en lo previsto en el punto 10.10.2.11"
  },
  {
   "id": "Obligacion_la_facultad_de_revocacion_segun_lo_establecido_en_el_apartado_v_del_punto_2_3_1_",
   "type": "Obligacion",
   "label": "Informar facultad de revocación",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La facultad de revocación según lo establecido en el apartado v) del punto 2.3.1.1"
  },
  {
   "id": "Obligacion_cumplir_las_condiciones_previstas_en_el_punto_3_11_3_para_acceder_al_mercado_par",
   "type": "Obligacion",
   "label": "Cumplir condiciones acceso mercado",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Cumplir las condiciones previstas en el punto 3.11.3. para acceder al mercado para la compra de moneda extranjera"
  }
 ]
}
```

### paso 15 — ver_nodo {"id": "Operacion_seguimiento_de_tramites_de_comercio_exterior"}

```json
{
 "id": "Operacion_seguimiento_de_tramites_de_comercio_exterior",
 "type": "Operacion",
 "label": "Seguimiento de oficializaciones de importación",
 "properties": {
  "tipo": "seguimiento de trámites de comercio exterior",
  "description": "Seguimiento de las oficializaciones de importación en el marco del SEPAIMPO"
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 10.2. Definiciones. (parte 2)"
  }
 ]
}
```

### paso 16 — ver_vecinos {"id": "Operacion_seguimiento_de_tramites_de_comercio_exterior", "direccion": "ambas"}

```json
{
 "id": "Operacion_seguimiento_de_tramites_de_comercio_exterior",
 "label": "Seguimiento de oficializaciones de importación",
 "n_salientes_total": 0,
 "n_entrantes_total": 1,
 "salientes": [],
 "salientes_truncado": false,
 "entrantes": [
  {
   "relation": "regula",
   "vecino_id": "Obligacion_verificar_cumplimiento_de_condiciones",
   "vecino_label": "Verificar cumplimiento de condiciones",
   "provenances": [
    {
     "source_doc": "TO_exterior_cambios_actual.pdf",
     "location": "Punto 10.2. Definiciones. (parte 2)"
    }
   ]
  }
 ],
 "entrantes_truncado": false
}
```



---

# CQN2-006

## Respuesta final íntegra (trace.final_json)

```json
{
 "respuesta": "En el régimen informativo sobre exigencia e integración de capitales mínimos, la exigencia de capital por riesgo operacional de las entidades del Grupo 1 se determina con frecuencia mensual mediante la expresión CRO = BIC x ILM. Sin embargo, en la información disponible en el Knowledge Graph no se especifica el valor numérico que toma el multiplicador de pérdida interna (ILM).",
 "citas": [
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Punto 5.1. Normas de procedimiento (parte 1)"
  }
 ],
 "respondible": false
}
```

(`respondible`: false · tool_calls: 15 · hit_tool_limit: True)

## Inventario de pasos + fidelidad runtime↔re-ejecución

| paso | tool | input | output_chars (runtime) | re-ejecutado | fiel |
|---|---|---|---|---|---|
| 1 | buscar_nodos | `{"consulta": "régimen informativo capitales mínimos riesgo operacional", "limite": 10` | 3197 | 3197 | SÍ |
| 2 | buscar_nodos | `{"consulta": "Grupo 1 exigencia capital riesgo operacional", "limite": 10}` | 3639 | 3639 | SÍ |
| 3 | buscar_nodos | `{"consulta": "multiplicador pérdida interna", "limite": 10}` | 3621 | 3621 | SÍ |
| 4 | ver_nodo | `{"id": "Obligacion_se_determinara_mensualmente_la_exigencia_de_capital_por_riesgo_ope` | 544 | 544 | SÍ |
| 5 | buscar_nodos | `{"consulta": "ILM multiplicador pérdida", "limite": 10}` | 2949 | 2949 | SÍ |
| 6 | buscar_nodos | `{"consulta": "BIC ILM CRO", "limite": 10}` | 1894 | 1894 | SÍ |
| 7 | buscar_nodos | `{"consulta": "ILM valor 1.5", "limite": 10}` | 3520 | 3520 | SÍ |
| 8 | buscar_nodos | `{"consulta": "Internal Loss Multiplier", "limite": 10}` | 80 | 80 | SÍ |
| 9 | ver_vecinos | `{"id": "Obligacion_se_determinara_mensualmente_la_exigencia_de_capital_por_riesgo_ope` | 1429 | 1429 | SÍ |
| 10 | ver_nodo | `{"id": "Operacion_calculo_mensual_de_exigencia_operacional"}` | 334 | 334 | SÍ |
| 11 | buscar_nodos | `{"consulta": "régimen informativo contable mensual punto 5.1", "limite": 10}` | 3193 | 3193 | SÍ |
| 12 | buscar_nodos | `{"consulta": "ILM 1.5 riesgo operacional", "limite": 10}` | 3340 | 3340 | SÍ |
| 13 | buscar_nodos | `{"consulta": "multiplicador pérdida interna 1.5", "limite": 10}` | 3250 | 3250 | SÍ |
| 14 | buscar_nodos | `{"consulta": "ILM", "limite": 15}` | 59 | 59 | SÍ |
| 15 | ver_nodo | `{"id": "TextoOrdenado_to_capitales_minimos_actual_pdf"}` | 361 | 361 | SÍ |

**Fidelidad: 15/15**.

## Apéndice — outputs completos re-ejecutados

### paso 1 — buscar_nodos {"consulta": "régimen informativo capitales mínimos riesgo operacional", "limite": 10}

```json
{
 "consulta": "régimen informativo capitales mínimos riesgo operacional",
 "total_con_match": 211,
 "resultados": [
  {
   "id": "TextoOrdenado_to_capitales_minimos_actual_pdf",
   "type": "TextoOrdenado",
   "label": "Capitales Mínimos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "materia: capitales minimos; archivo: TO_capitales_minimos_actual.pdf; version: actual"
  },
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
   "id": "Obligacion_las_entidades_deberan_consultar_en_el_apartado_regimen_informativo_sepaimpo_del_",
   "type": "Obligacion",
   "label": "Consultar situación del cliente",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Las entidades deberán consultar en el apartado 'Régimen Informativo SEPAIMPO' del sitio www3.bcra.gob.ar, si el cliente se encuentra en la situación de condena …"
  },
  {
   "id": "Operacion_integracion_de_capitales",
   "type": "Operacion",
   "label": "Integración de capitales mínimos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: integración de capitales"
  },
  {
   "id": "Operacion_presentacion_informativa_de_operaciones_cambiarias",
   "type": "Operacion",
   "label": "Validación en régimen informativo",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: presentación informativa de operaciones cambiarias"
  },
  {
   "id": "Restriccion_las_exigencias_a_ser_incluidas_dentro_del_calculo_del_promedio_de_erc_se_extiend",
   "type": "Restriccion",
   "label": "Límite exigencia riesgo operacional",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Las exigencias a ser incluidas dentro del cálculo del promedio de ERC se extienden únicamente hasta la que correspondió ser integrada en febrero 2013 (promedios…"
  },
  {
   "id": "TextoOrdenado_to_regimen_informativo_contable_mensual_actual_pdf",
   "type": "TextoOrdenado",
   "label": "Régimen Informativo Contable Mensual",
   "tokens_matcheados": 2,
   "resumen_propiedades": "materia: Información contable y regulatoria mensual; archivo: TO_regimen_informativo_contable_mensual_actual.pdf; version: actual"
  },
  {
   "id": "Obligacion_la_entidad_debera_dar_cumplimiento_a_las_disposiciones_dadas_a_conocer_por_el_re",
   "type": "Obligacion",
   "label": "Cumplimiento régimen informativo BCRA",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La entidad deberá dar cumplimiento a las disposiciones dadas a conocer por el régimen informativo asociado a este seguimiento."
  },
  {
   "id": "Obligacion_consultar_regimen_informativo_sepaimpo",
   "type": "Obligacion",
   "label": "Consultar régimen informativo SEPAIMPO",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Las entidades deberán consultar en el apartado Régimen Informativo SEPAIMPO del sitio www3.bcra.gob.ar el saldo pendiente de regularización por pagos anticipado…"
  }
 ]
}
```

### paso 2 — buscar_nodos {"consulta": "Grupo 1 exigencia capital riesgo operacional", "limite": 10}

```json
{
 "consulta": "Grupo 1 exigencia capital riesgo operacional",
 "total_con_match": 436,
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
   "id": "Restriccion_la_exigencia_determinada_a_traves_de_la_aplicacion_de_la_expresion_descripta_en_",
   "type": "Restriccion",
   "label": "Límite 20% grupo A capital mínimo",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La exigencia determinada a través de la aplicación de la expresión descripta en el punto 7.2. no podrá superar el 20% en el caso de entidades del grupo A del pr…"
  },
  {
   "id": "Restriccion_las_exigencias_a_ser_incluidas_dentro_del_calculo_del_promedio_de_erc_se_extiend",
   "type": "Restriccion",
   "label": "Límite exigencia riesgo operacional",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Las exigencias a ser incluidas dentro del cálculo del promedio de ERC se extienden únicamente hasta la que correspondió ser integrada en febrero 2013 (promedios…"
  }
 ]
}
```

### paso 3 — buscar_nodos {"consulta": "multiplicador pérdida interna", "limite": 10}

```json
{
 "consulta": "multiplicador pérdida interna",
 "total_con_match": 15,
 "resultados": [
  {
   "id": "Restriccion_el_multiplicador_que_reduce_la_garantia_en_exceso_esta_sujeto_a_un_minimo_del_5_",
   "type": "Restriccion",
   "label": "Multiplicador mínimo EPF",
   "tokens_matcheados": 1,
   "resumen_propiedades": "El multiplicador que reduce la garantía en exceso está sujeto a un mínimo del 5% de la EPF"
  },
  {
   "id": "Obligacion_la_epf_resultara_del_producto_entre_la_suma_de_adicionales_por_clase_de_activos_",
   "type": "Obligacion",
   "label": "Calcular EPF multiplicador",
   "tokens_matcheados": 1,
   "resumen_propiedades": "La EPF resultará del producto entre la suma de adicionales por clase de activos y un multiplicador que reconoce garantía en exceso o valor de mercado negativo"
  },
  {
   "id": "Operacion_auditoria_interna",
   "type": "Operacion",
   "label": "Revisión de esquema de medición",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Revisión exhaustiva del esquema que adopte la entidad para la medición de la exigencia por riesgo de mercado"
  },
  {
   "id": "Operacion_multiplicacion_de_exposicion_al_riesgo_de_contraparte_por_factor_1_5",
   "type": "Operacion",
   "label": "Aplicación de factor multiplicador",
   "tokens_matcheados": 1,
   "resumen_propiedades": "tipo: multiplicación de exposición al riesgo de contraparte por factor 1,5"
  },
  {
   "id": "Obligacion_auditoria_interna_revision_exhaustiva",
   "type": "Obligacion",
   "label": "Auditoría interna revisión exhaustiva",
   "tokens_matcheados": 1,
   "resumen_propiedades": "La auditoría interna deberá llevar a cabo una revisión exhaustiva del esquema que adopte la entidad para la medición de la exigencia por riesgo de mercado, deja…"
  },
  {
   "id": "Obligacion_en_lugar_de_calcular_el_ajuste_de_valuacion_del_credito_cva_se_debera_multiplica",
   "type": "Obligacion",
   "label": "Aplicación de factor multiplicador para CVA",
   "tokens_matcheados": 1,
   "resumen_propiedades": "En lugar de calcular el ajuste de valuación del crédito (CVA), se deberá multiplicar la exposición al riesgo de crédito de contraparte por un factor de 1,5 ante…"
  },
  {
   "id": "Obligacion_la_entidad_debera_contar_con_una_declaracion_jurada_del_exportador_indicando_que",
   "type": "Obligacion",
   "label": "Contar con documentación técnica de pérdida",
   "tokens_matcheados": 1,
   "resumen_propiedades": "La entidad deberá contar con una declaración jurada del exportador indicando que por los bienes no reimportados no ha recibido ni recibirá algún tipo de contrap…"
  },
  {
   "id": "Restriccion_la_revocacion_o_rescision_de_un_producto_o_servicio_integrante_de_un_contrato_mu",
   "type": "Restriccion",
   "label": "Pérdida beneficios revocación multiproducto",
   "tokens_matcheados": 1,
   "resumen_propiedades": "La revocación o rescisión de un producto o servicio integrante de un contrato multiproducto podrá implicar la pérdida de beneficios y/o la baja de los restantes…"
  },
  {
   "id": "Obligacion_evaluar_los_informes_emitidos_por_la_auditoria_interna_la_auditoria_externa_y_la",
   "type": "Obligacion",
   "label": "Evaluar informes de auditoría e indicaciones",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Evaluar los informes emitidos por la auditoría interna, la auditoría externa y las observaciones e indicaciones comunicadas por la SEFyC con relación al proceso…"
  },
  {
   "id": "Obligacion_la_auditoria_interna_debe_verificar_que_se_proporciona_a_los_usuarios_de_servici",
   "type": "Obligacion",
   "label": "Verificar entrega de formularios y contratos",
   "tokens_matcheados": 1,
   "resumen_propiedades": "La auditoría interna debe verificar que se proporciona a los usuarios de servicios financieros copia de los formularios que firman y ejemplares de los contratos…"
  }
 ]
}
```

### paso 4 — ver_nodo {"id": "Obligacion_se_determinara_mensualmente_la_exigencia_de_capital_por_riesgo_operacional_cro_m"}

```json
{
 "id": "Obligacion_se_determinara_mensualmente_la_exigencia_de_capital_por_riesgo_operacional_cro_m",
 "type": "Obligacion",
 "label": "Informar CRO mensualmente",
 "properties": {
  "descripcion": "Se determinará mensualmente la exigencia de capital por riesgo operacional (CRO) mediante la expresión CRO = BIC x ILM para entidades del Grupo 1",
  "tipo": "presentacion_informativa",
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

### paso 5 — buscar_nodos {"consulta": "ILM multiplicador pérdida", "limite": 10}

```json
{
 "consulta": "ILM multiplicador pérdida",
 "total_con_match": 8,
 "resultados": [
  {
   "id": "Restriccion_el_multiplicador_que_reduce_la_garantia_en_exceso_esta_sujeto_a_un_minimo_del_5_",
   "type": "Restriccion",
   "label": "Multiplicador mínimo EPF",
   "tokens_matcheados": 1,
   "resumen_propiedades": "El multiplicador que reduce la garantía en exceso está sujeto a un mínimo del 5% de la EPF"
  },
  {
   "id": "Obligacion_la_epf_resultara_del_producto_entre_la_suma_de_adicionales_por_clase_de_activos_",
   "type": "Obligacion",
   "label": "Calcular EPF multiplicador",
   "tokens_matcheados": 1,
   "resumen_propiedades": "La EPF resultará del producto entre la suma de adicionales por clase de activos y un multiplicador que reconoce garantía en exceso o valor de mercado negativo"
  },
  {
   "id": "Operacion_multiplicacion_de_exposicion_al_riesgo_de_contraparte_por_factor_1_5",
   "type": "Operacion",
   "label": "Aplicación de factor multiplicador",
   "tokens_matcheados": 1,
   "resumen_propiedades": "tipo: multiplicación de exposición al riesgo de contraparte por factor 1,5"
  },
  {
   "id": "Obligacion_en_lugar_de_calcular_el_ajuste_de_valuacion_del_credito_cva_se_debera_multiplica",
   "type": "Obligacion",
   "label": "Aplicación de factor multiplicador para CVA",
   "tokens_matcheados": 1,
   "resumen_propiedades": "En lugar de calcular el ajuste de valuación del crédito (CVA), se deberá multiplicar la exposición al riesgo de crédito de contraparte por un factor de 1,5 ante…"
  },
  {
   "id": "Obligacion_la_entidad_debera_contar_con_una_declaracion_jurada_del_exportador_indicando_que",
   "type": "Obligacion",
   "label": "Contar con documentación técnica de pérdida",
   "tokens_matcheados": 1,
   "resumen_propiedades": "La entidad deberá contar con una declaración jurada del exportador indicando que por los bienes no reimportados no ha recibido ni recibirá algún tipo de contrap…"
  },
  {
   "id": "Restriccion_la_revocacion_o_rescision_de_un_producto_o_servicio_integrante_de_un_contrato_mu",
   "type": "Restriccion",
   "label": "Pérdida beneficios revocación multiproducto",
   "tokens_matcheados": 1,
   "resumen_propiedades": "La revocación o rescisión de un producto o servicio integrante de un contrato multiproducto podrá implicar la pérdida de beneficios y/o la baja de los restantes…"
  },
  {
   "id": "Restriccion_por_el_valor_de_los_bienes_que_fueron_exportados_temporariamente_con_o_sin_trans",
   "type": "Restriccion",
   "label": "Restricción de reimportación por pérdida de valor",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Por el valor de los bienes que fueron exportados temporariamente, con o sin transformación, cuya reimportación al país no resulte razonable ante la pérdida del …"
  },
  {
   "id": "Restriccion_el_importe_resultante_de_la_seccion_2_debera_ser_multiplicado_por_un_factor_igua",
   "type": "Restriccion",
   "label": "Factor multiplicador 4 para capital mínimo agrícola",
   "tokens_matcheados": 1,
   "resumen_propiedades": "El importe resultante de la Sección 2 deberá ser multiplicado por un factor igual a 4"
  }
 ]
}
```

### paso 6 — buscar_nodos {"consulta": "BIC ILM CRO", "limite": 10}

```json
{
 "consulta": "BIC ILM CRO",
 "total_con_match": 6,
 "resultados": [
  {
   "id": "Obligacion_informar_bic_calculado",
   "type": "Obligacion",
   "label": "Informar BIC calculado",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Se informará el BIC calculado"
  },
  {
   "id": "Obligacion_la_partida_correspondiente_al_bic_se_informara_por_el_importe_calculado_en_funci",
   "type": "Obligacion",
   "label": "Informar componentes BIC",
   "tokens_matcheados": 1,
   "resumen_propiedades": "La partida correspondiente al BIC se informará por el importe calculado en función de los coeficientes marginales que corresponda"
  },
  {
   "id": "Obligacion_se_determinara_mensualmente_la_exigencia_de_capital_por_riesgo_operacional_cro_m",
   "type": "Obligacion",
   "label": "Informar CRO mensualmente",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Se determinará mensualmente la exigencia de capital por riesgo operacional (CRO) mediante la expresión CRO = BIC x ILM para entidades del Grupo 1"
  },
  {
   "id": "Operacion_calculo_mensual_de_exigencia_operacional",
   "type": "Operacion",
   "label": "Determinación mensual CRO",
   "tokens_matcheados": 1,
   "resumen_propiedades": "tipo: cálculo mensual de exigencia operacional"
  },
  {
   "id": "Obligacion_se_determinara_mensualmente_por_la_expresion_cro_a_ib_n_donde_a_es_15_n_es_numer",
   "type": "Obligacion",
   "label": "Determinar CRO mensualmente Grupo 2",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Se determinará mensualmente por la expresión: CRO = (a*IB) / n, donde a es 15%, n es número de períodos de 12 meses consecutivos con IB positivo, máximo 3"
  },
  {
   "id": "Restriccion_limite_cuantitativo_de_coeficientes_bic",
   "type": "Restriccion",
   "label": "Límite cuantitativo de coeficientes BIC",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Los coeficientes marginales (α) para el cálculo del BIC varían según tramos: Categoría 1 (BI ≤ €1.000 millones): 12%; Categoría 2 (1 < BI ≤ 30 mil millones euro…"
  }
 ]
}
```

### paso 7 — buscar_nodos {"consulta": "ILM valor 1.5", "limite": 10}

```json
{
 "consulta": "ILM valor 1.5",
 "total_con_match": 139,
 "resultados": [
  {
   "id": "Restriccion_el_activo_recibido_en_garantia_se_limitara_a_aquellos_listados_en_el_punto_5_3_1",
   "type": "Restriccion",
   "label": "Activos limitados a listado",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El activo recibido en garantía se limitará a aquellos listados en el punto 5.3.1.2."
  },
  {
   "id": "Operacion_multiplicacion_de_exposicion_al_riesgo_de_contraparte_por_factor_1_5",
   "type": "Operacion",
   "label": "Aplicación de factor multiplicador",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: multiplicación de exposición al riesgo de contraparte por factor 1,5"
  },
  {
   "id": "Restriccion_los_garantes_admisibles_se_limitan_a_los_estipulados_en_el_punto_5_4_1_los_spe_n",
   "type": "Restriccion",
   "label": "Restricción en garantes admisibles",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Los garantes admisibles se limitan a los estipulados en el punto 5.4.1. Los SPE no son garantes admisibles."
  },
  {
   "id": "Restriccion_clientes_que_mantengan_un_acopio_de_su_produccion_por_un_valor_superior_al_5_de_",
   "type": "Restriccion",
   "label": "Requisito acopio producción agrícola",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Clientes que mantengan un acopio de su producción por un valor superior al 5% de su capacidad de cosecha anual"
  },
  {
   "id": "Obligacion_ajustar_el_valor_de_la_cobertura_segun_lo_previsto_en_punto_5_4_5",
   "type": "Obligacion",
   "label": "Ajuste valor cobertura método integral",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Para la aplicación del método integral el valor de la cobertura deberá ajustarse conforme a lo establecido en el punto 5.4.5"
  },
  {
   "id": "Restriccion_el_valor_nominal_de_los_nuevos_titulos_entregados_en_concepto_de_prima_de_partic",
   "type": "Restriccion",
   "label": "Prima participación recompra máximo 5%",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El valor nominal de los nuevos títulos entregados en concepto de prima de participación, recompra o rescate anticipado no supere el equivalente al 5% (cinco por…"
  },
  {
   "id": "Restriccion_capital_ordinario_de_nivel_1_con1_70210000_70220000_4_5_s_70900000",
   "type": "Restriccion",
   "label": "Límite mínimo Capital Ordinario Nivel 1",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Capital Ordinario de Nivel 1 (COn1) = 70210000 – 70220000 ≥ 4,5 % s/70900000"
  },
  {
   "id": "Excepcion_emisiones_de_valores_comprendidos_en_puntos_3_6_1_3_a_3_6_1_5_que_no_generaron_d",
   "type": "Excepcion",
   "label": "Reestructuraciones deuda sin desembolsos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Emisiones de valores comprendidos en puntos 3.6.1.3 a 3.6.1.5 que no generaron desembolsos por ser reestructuraciones de deudas, en medida que refinanciaciones …"
  },
  {
   "id": "Obligacion_el_sujeto_obligado_debera_aplicar_1_5_veces_la_tasa_promedio_correspondiente_al_",
   "type": "Obligacion",
   "label": "Aplicar intereses compensatorios en reintegros",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El sujeto obligado deberá aplicar 1,5 veces la tasa promedio correspondiente al período comprendido entre el momento en que la diferencia hubiera sido exigible …"
  },
  {
   "id": "Excepcion_el_pago_se_concreta_en_el_marco_de_lo_dispuesto_en_el_punto_4_8_5_por_un_cliente",
   "type": "Excepcion",
   "label": "Pago BOPREAL Serie 1 mínimo 25% deudas elegibles",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El pago se concreta en el marco de lo dispuesto en el punto 4.8.5. por un cliente que suscribió BOPREAL Serie 1 por un monto igual o mayor al 25% (veinticinco p…"
  }
 ]
}
```

### paso 8 — buscar_nodos {"consulta": "Internal Loss Multiplier", "limite": 10}

```json
{
 "consulta": "Internal Loss Multiplier",
 "total_con_match": 0,
 "resultados": []
}
```

### paso 9 — ver_vecinos {"id": "Obligacion_se_determinara_mensualmente_la_exigencia_de_capital_por_riesgo_operacional_cro_m", "direccion": "ambas"}

```json
{
 "id": "Obligacion_se_determinara_mensualmente_la_exigencia_de_capital_por_riesgo_operacional_cro_m",
 "label": "Informar CRO mensualmente",
 "n_salientes_total": 4,
 "n_entrantes_total": 0,
 "salientes": [
  {
   "relation": "establecida_en",
   "vecino_id": "TextoOrdenado_to_regimen_informativo_contable_mensual_actual_pdf",
   "vecino_label": "Régimen Informativo Contable Mensual",
   "provenances": [
    {
     "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
     "location": "Punto 5.1. Normas de procedimiento (parte 1)"
    }
   ]
  },
  {
   "relation": "aplica_a",
   "vecino_id": "EntidadFinanciera_entidad_del_grupo_1",
   "vecino_label": "Entidades del grupo 1",
   "provenances": [
    {
     "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
     "location": "Punto 5.1. Normas de procedimiento (parte 1)"
    }
   ]
  },
  {
   "relation": "regula",
   "vecino_id": "Operacion_calculo_de_capital_minimo",
   "vecino_label": "Cálculo de exigencia por riesgo de crédito",
   "provenances": [
    {
     "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
     "location": "Punto 5.1. Normas de procedimiento (parte 1)"
    }
   ]
  },
  {
   "relation": "regula",
   "vecino_id": "Operacion_calculo_mensual_de_exigencia_operacional",
   "vecino_label": "Determinación mensual CRO",
   "provenances": [
    {
     "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
     "location": "Punto 5.1. Normas de procedimiento (parte 1)"
    }
   ]
  }
 ],
 "salientes_truncado": false,
 "entrantes": [],
 "entrantes_truncado": false
}
```

### paso 10 — ver_nodo {"id": "Operacion_calculo_mensual_de_exigencia_operacional"}

```json
{
 "id": "Operacion_calculo_mensual_de_exigencia_operacional",
 "type": "Operacion",
 "label": "Determinación mensual CRO",
 "properties": {
  "tipo": "cálculo mensual de exigencia operacional"
 },
 "provenances": [
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Punto 5.1. Normas de procedimiento (parte 1)"
  }
 ]
}
```

### paso 11 — buscar_nodos {"consulta": "régimen informativo contable mensual punto 5.1", "limite": 10}

```json
{
 "consulta": "régimen informativo contable mensual punto 5.1",
 "total_con_match": 145,
 "resultados": [
  {
   "id": "TextoOrdenado_to_regimen_informativo_contable_mensual_actual_pdf",
   "type": "TextoOrdenado",
   "label": "Régimen Informativo Contable Mensual",
   "tokens_matcheados": 4,
   "resumen_propiedades": "materia: Información contable y regulatoria mensual; archivo: TO_regimen_informativo_contable_mensual_actual.pdf; version: actual"
  },
  {
   "id": "Restriccion_el_activo_recibido_en_garantia_se_limitara_a_aquellos_listados_en_el_punto_5_3_1",
   "type": "Restriccion",
   "label": "Activos limitados a listado",
   "tokens_matcheados": 3,
   "resumen_propiedades": "El activo recibido en garantía se limitará a aquellos listados en el punto 5.3.1.2."
  },
  {
   "id": "Restriccion_los_garantes_admisibles_se_limitan_a_los_estipulados_en_el_punto_5_4_1_los_spe_n",
   "type": "Restriccion",
   "label": "Restricción en garantes admisibles",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Los garantes admisibles se limitan a los estipulados en el punto 5.4.1. Los SPE no son garantes admisibles."
  },
  {
   "id": "Excepcion_el_pago_se_concreta_en_el_marco_de_lo_dispuesto_en_el_punto_4_8_5_por_un_cliente",
   "type": "Excepcion",
   "label": "Pago BOPREAL Serie 1 mínimo 25% deudas elegibles",
   "tokens_matcheados": 3,
   "resumen_propiedades": "El pago se concreta en el marco de lo dispuesto en el punto 4.8.5. por un cliente que suscribió BOPREAL Serie 1 por un monto igual o mayor al 25% (veinticinco p…"
  },
  {
   "id": "Excepcion_con_excepcion_de_los_casos_contemplados_en_el_punto_4_1",
   "type": "Excepcion",
   "label": "Excepción casos punto 4.1",
   "tokens_matcheados": 2,
   "resumen_propiedades": "con excepción de los casos contemplados en el punto 4.1"
  },
  {
   "id": "Excepcion_cuando_la_operacion_se_encuentra_comprendida_en_alguna_de_las_situaciones_detall",
   "type": "Excepcion",
   "label": "Situaciones del punto 8.5",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Cuando la operación se encuentra comprendida en alguna de las situaciones detalladas en el punto 8.5 y se verifiquen las condiciones previstas en cada caso"
  },
  {
   "id": "Excepcion_no_aplicable_punto_3_12_1",
   "type": "Excepcion",
   "label": "No aplicable punto 3.12.1",
   "tokens_matcheados": 2,
   "resumen_propiedades": "En la medida que no encuadre en el punto 3.12.1"
  },
  {
   "id": "Restriccion_acciones_definidas_conforme_al_punto_2_11_3_250",
   "type": "Restriccion",
   "label": "Ponderador acciones grupo 1",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Acciones (definidas conforme al punto 2.11.3.): 250"
  },
  {
   "id": "Obligacion_la_facultad_de_revocacion_segun_lo_establecido_en_el_apartado_v_del_punto_2_3_1_",
   "type": "Obligacion",
   "label": "Informar facultad de revocación",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La facultad de revocación según lo establecido en el apartado v) del punto 2.3.1.1"
  },
  {
   "id": "Obligacion_las_entidades_deberan_consultar_en_el_apartado_regimen_informativo_sepaimpo_del_",
   "type": "Obligacion",
   "label": "Consultar situación del cliente",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Las entidades deberán consultar en el apartado 'Régimen Informativo SEPAIMPO' del sitio www3.bcra.gob.ar, si el cliente se encuentra en la situación de condena …"
  }
 ]
}
```

### paso 12 — buscar_nodos {"consulta": "ILM 1.5 riesgo operacional", "limite": 10}

```json
{
 "consulta": "ILM 1.5 riesgo operacional",
 "total_con_match": 258,
 "resultados": [
  {
   "id": "Operacion_multiplicacion_de_exposicion_al_riesgo_de_contraparte_por_factor_1_5",
   "type": "Operacion",
   "label": "Aplicación de factor multiplicador",
   "tokens_matcheados": 3,
   "resumen_propiedades": "tipo: multiplicación de exposición al riesgo de contraparte por factor 1,5"
  },
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
   "id": "Restriccion_el_activo_recibido_en_garantia_se_limitara_a_aquellos_listados_en_el_punto_5_3_1",
   "type": "Restriccion",
   "label": "Activos limitados a listado",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El activo recibido en garantía se limitará a aquellos listados en el punto 5.3.1.2."
  },
  {
   "id": "Restriccion_los_garantes_admisibles_se_limitan_a_los_estipulados_en_el_punto_5_4_1_los_spe_n",
   "type": "Restriccion",
   "label": "Restricción en garantes admisibles",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Los garantes admisibles se limitan a los estipulados en el punto 5.4.1. Los SPE no son garantes admisibles."
  },
  {
   "id": "Restriccion_las_exigencias_a_ser_incluidas_dentro_del_calculo_del_promedio_de_erc_se_extiend",
   "type": "Restriccion",
   "label": "Límite exigencia riesgo operacional",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Las exigencias a ser incluidas dentro del cálculo del promedio de ERC se extienden únicamente hasta la que correspondió ser integrada en febrero 2013 (promedios…"
  },
  {
   "id": "Restriccion_capital_ordinario_de_nivel_1_con1_70210000_70220000_4_5_s_70900000",
   "type": "Restriccion",
   "label": "Límite mínimo Capital Ordinario Nivel 1",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Capital Ordinario de Nivel 1 (COn1) = 70210000 – 70220000 ≥ 4,5 % s/70900000"
  },
  {
   "id": "Excepcion_emisiones_de_valores_comprendidos_en_puntos_3_6_1_3_a_3_6_1_5_que_no_generaron_d",
   "type": "Excepcion",
   "label": "Reestructuraciones deuda sin desembolsos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Emisiones de valores comprendidos en puntos 3.6.1.3 a 3.6.1.5 que no generaron desembolsos por ser reestructuraciones de deudas, en medida que refinanciaciones …"
  },
  {
   "id": "Restriccion_periodo_de_riesgo_de_margen_minimo_5_dias",
   "type": "Restriccion",
   "label": "Período de riesgo de margen mínimo 5 días",
   "tokens_matcheados": 2,
   "resumen_propiedades": "5 días hábiles para las operaciones de derivados que se liquidan en forma centralizada y están sujetas a acuerdos de márgenes diarios entre el miembro compensad…"
  },
  {
   "id": "Operacion_calculo",
   "type": "Operacion",
   "label": "Cálculo exigencia capital riesgo operacional",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Cálculo de K (exigencia de capital promedio de las exposiciones subyacentes); es decir, el ratio entre la suma de las exposiciones subyacentes ponderadas por ri…"
  }
 ]
}
```

### paso 13 — buscar_nodos {"consulta": "multiplicador pérdida interna 1.5", "limite": 10}

```json
{
 "consulta": "multiplicador pérdida interna 1.5",
 "total_con_match": 96,
 "resultados": [
  {
   "id": "Operacion_multiplicacion_de_exposicion_al_riesgo_de_contraparte_por_factor_1_5",
   "type": "Operacion",
   "label": "Aplicación de factor multiplicador",
   "tokens_matcheados": 3,
   "resumen_propiedades": "tipo: multiplicación de exposición al riesgo de contraparte por factor 1,5"
  },
  {
   "id": "Restriccion_el_multiplicador_que_reduce_la_garantia_en_exceso_esta_sujeto_a_un_minimo_del_5_",
   "type": "Restriccion",
   "label": "Multiplicador mínimo EPF",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El multiplicador que reduce la garantía en exceso está sujeto a un mínimo del 5% de la EPF"
  },
  {
   "id": "Restriccion_el_activo_recibido_en_garantia_se_limitara_a_aquellos_listados_en_el_punto_5_3_1",
   "type": "Restriccion",
   "label": "Activos limitados a listado",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El activo recibido en garantía se limitará a aquellos listados en el punto 5.3.1.2."
  },
  {
   "id": "Restriccion_los_garantes_admisibles_se_limitan_a_los_estipulados_en_el_punto_5_4_1_los_spe_n",
   "type": "Restriccion",
   "label": "Restricción en garantes admisibles",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Los garantes admisibles se limitan a los estipulados en el punto 5.4.1. Los SPE no son garantes admisibles."
  },
  {
   "id": "Restriccion_capital_ordinario_de_nivel_1_con1_70210000_70220000_4_5_s_70900000",
   "type": "Restriccion",
   "label": "Límite mínimo Capital Ordinario Nivel 1",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Capital Ordinario de Nivel 1 (COn1) = 70210000 – 70220000 ≥ 4,5 % s/70900000"
  },
  {
   "id": "Excepcion_emisiones_de_valores_comprendidos_en_puntos_3_6_1_3_a_3_6_1_5_que_no_generaron_d",
   "type": "Excepcion",
   "label": "Reestructuraciones deuda sin desembolsos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Emisiones de valores comprendidos en puntos 3.6.1.3 a 3.6.1.5 que no generaron desembolsos por ser reestructuraciones de deudas, en medida que refinanciaciones …"
  },
  {
   "id": "Obligacion_el_sujeto_obligado_debera_aplicar_1_5_veces_la_tasa_promedio_correspondiente_al_",
   "type": "Obligacion",
   "label": "Aplicar intereses compensatorios en reintegros",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El sujeto obligado deberá aplicar 1,5 veces la tasa promedio correspondiente al período comprendido entre el momento en que la diferencia hubiera sido exigible …"
  },
  {
   "id": "Excepcion_el_pago_se_concreta_en_el_marco_de_lo_dispuesto_en_el_punto_4_8_5_por_un_cliente",
   "type": "Excepcion",
   "label": "Pago BOPREAL Serie 1 mínimo 25% deudas elegibles",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El pago se concreta en el marco de lo dispuesto en el punto 4.8.5. por un cliente que suscribió BOPREAL Serie 1 por un monto igual o mayor al 25% (veinticinco p…"
  },
  {
   "id": "Restriccion_el_importe_de_co_debera_ser_resultante_de_multiplicar_4_5_por_los_apr",
   "type": "Restriccion",
   "label": "Límite mínimo CO",
   "tokens_matcheados": 1,
   "resumen_propiedades": "El importe de CO deberá ser resultante de multiplicar 4,5% por los APR"
  },
  {
   "id": "EntidadFinanciera_entidad_del_grupo_1",
   "type": "EntidadFinanciera",
   "label": "Entidades del grupo 1",
   "tokens_matcheados": 1,
   "resumen_propiedades": "categoria: entidades financieras grupo 1"
  }
 ]
}
```

### paso 14 — buscar_nodos {"consulta": "ILM", "limite": 15}

```json
{
 "consulta": "ILM",
 "total_con_match": 0,
 "resultados": []
}
```

### paso 15 — ver_nodo {"id": "TextoOrdenado_to_capitales_minimos_actual_pdf"}

```json
{
 "id": "TextoOrdenado_to_capitales_minimos_actual_pdf",
 "type": "TextoOrdenado",
 "label": "Capitales Mínimos",
 "properties": {
  "materia": "capitales minimos",
  "archivo": "TO_capitales_minimos_actual.pdf",
  "version": "actual"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Punto 1.1. “A” 2136 1. 1° Según Com. “A” 2859, 3558,"
  }
 ]
}
```



---

# CQN2-007

## Respuesta final íntegra (trace.final_json)

```json
{
 "respuesta": "Para que la metodología de evaluación de un agente de calificación externa (ECAI) pueda ser reconocida a los fines de la determinación de ponderadores de riesgo, debe cumplir con los siguientes requisitos: (1) Antigüedad mínima: la metodología deberá haber sido utilizada durante al menos un año, siendo preferible que haya sido utilizada durante tres años. (2) Comprobación: la metodología debe haber estado sujeta a la comprobación rigurosa de su precisión mediante pruebas retrospectivas (backtesting). Adicionalmente, la metodología debe ser rigurosa, sistemática y estar sujeta a algún tipo de validación basada en la experiencia histórica, y las evaluaciones deberán ser objeto de un control constante y responder a los cambios en la coyuntura financiera.",
 "citas": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Punto 10.2. Criterios de elegibilidad."
  }
 ],
 "respondible": true
}
```

(`respondible`: true · tool_calls: 10 · hit_tool_limit: False)

## Inventario de pasos + fidelidad runtime↔re-ejecución

| paso | tool | input | output_chars (runtime) | re-ejecutado | fiel |
|---|---|---|---|---|---|
| 1 | buscar_nodos | `{"consulta": "ECAI agente calificación externa metodología antigüedad reconocida pond` | 3385 | 3385 | SÍ |
| 2 | buscar_nodos | `{"consulta": "ECAI metodología evaluación comprobación requisitos", "limite": 10}` | 3104 | 3104 | SÍ |
| 3 | buscar_nodos | `{"consulta": "ECAI antigüedad años uso metodología comprobación", "limite": 10}` | 2774 | 2774 | SÍ |
| 4 | buscar_nodos | `{"consulta": "metodología ECAI reconocimiento ponderadores requisitos", "limite": 10}` | 3281 | 3281 | SÍ |
| 5 | ver_nodo | `{"id": "Obligacion_las_ecai_deberan_divulgar_su_codigo_de_conducta_el_caracter_genera` | 747 | 747 | SÍ |
| 6 | buscar_nodos | `{"consulta": "ECAI tres años antigüedad metodología", "limite": 10}` | 3131 | 3131 | SÍ |
| 7 | buscar_nodos | `{"consulta": "ECAI metodología reconocida acreditada requisitos elegibilidad", "limit` | 3286 | 3286 | SÍ |
| 8 | buscar_nodos | `{"consulta": "ECAI comprobación validación metodología histórico", "limite": 10}` | 3221 | 3221 | SÍ |
| 9 | ver_nodo | `{"id": "Obligacion_la_metodologia_utilizada_para_asignar_las_calificaciones_creditici` | 855 | 855 | SÍ |
| 10 | ver_vecinos | `{"id": "Obligacion_la_metodologia_utilizada_para_asignar_las_calificaciones_creditici` | 1029 | 1029 | SÍ |

**Fidelidad: 10/10**.

## Apéndice — outputs completos re-ejecutados

### paso 1 — buscar_nodos {"consulta": "ECAI agente calificación externa metodología antigüedad reconocida ponderadores riesgo", "limite": 10}

```json
{
 "consulta": "ECAI agente calificación externa metodología antigüedad reconocida ponderadores riesgo",
 "total_con_match": 223,
 "resultados": [
  {
   "id": "Obligacion_ecai_nacionales_deberan_estar_registradas_como_agentes_de_calificacion_de_riesgo",
   "type": "Obligacion",
   "label": "Registrarse ante autoridades competentes",
   "tokens_matcheados": 3,
   "resumen_propiedades": "ECAI nacionales deberán estar registradas como agentes de calificación de riesgos ante la Comisión Nacional de Valores (CNV). ECAI internacionales deberán estar…"
  },
  {
   "id": "Operacion_asignacion",
   "type": "Operacion",
   "label": "Asignación ponderadores riesgo",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El ponderador de riesgo RW a asignar a una posición de titulización se calculará conforme a criterios que varían según la relación entre D, K y K."
  },
  {
   "id": "Operacion_calculo_de_ponderadores_de_riesgo_para_inversiones_en_fondos",
   "type": "Operacion",
   "label": "Ponderación de riesgo en fondos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: cálculo de ponderadores de riesgo para inversiones en fondos"
  },
  {
   "id": "Operacion_asignacion_de_ponderadores",
   "type": "Operacion",
   "label": "Asignación de ponderadores de riesgo",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Asignación de ponderadores de riesgo específicos a exposiciones según cálculos previstos en normas de capitales mínimos"
  },
  {
   "id": "Operacion_calculo_de_activos_ponderados_por_riesgo",
   "type": "Operacion",
   "label": "Aplicación de ponderadores de riesgo",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Se aplicarán los ponderadores de riesgo establecidos en el punto 2.12. según el grupo al que pertenezca la entidad financiera"
  },
  {
   "id": "Obligacion_utilizar_calificacion_de_ecai_admitida",
   "type": "Obligacion",
   "label": "Utilizar calificación de ECAI admitida",
   "tokens_matcheados": 2,
   "resumen_propiedades": "A los efectos de determinar el ponderador de riesgo a aplicar a las exposiciones a que se refieren los puntos 2.12.2.4., 2.12.2.5., 2.12.2.6. y 2.12.2.8., se de…"
  },
  {
   "id": "Obligacion_informar_ecai_utilizadas_y_ponderadores",
   "type": "Obligacion",
   "label": "Informar ECAI utilizadas y ponderadores",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Las entidades financieras deberán informar las ECAI que utilizan para ponderar el riesgo de sus activos por tipo de crédito, los ponderadores de riesgo asociado…"
  },
  {
   "id": "Obligacion_comunicar_ponderadores_de_riesgo_a_sefyc",
   "type": "Obligacion",
   "label": "Comunicar ponderadores de riesgo a SEFyC",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Las entidades financieras del grupo 1 deberán comunicar a la SEFyC cuando sus ponderadores de riesgo, surgidos del proceso de debida diligencia, sean mayores a …"
  },
  {
   "id": "Obligacion_las_entidades_financieras_deberan_demostrar_a_la_sefyc_que_los_ponderadores_de_r",
   "type": "Obligacion",
   "label": "Demostrar adecuación ponderadores riesgo",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Las entidades financieras deberán demostrar a la SEFYC que los ponderadores de riesgo asignados son adecuados a los perfiles de riesgo de sus contrapartes."
  },
  {
   "id": "Operacion_calculo_de_ponderadores",
   "type": "Operacion",
   "label": "Cálculo de activos ponderados por riesgo",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Cálculo de APR_c conforme a fórmula: APR_c = A x p + PFB x CCF x p + no DVP + (DVP + RCD + INC) x 12,5"
  }
 ]
}
```

### paso 2 — buscar_nodos {"consulta": "ECAI metodología evaluación comprobación requisitos", "limite": 10}

```json
{
 "consulta": "ECAI metodología evaluación comprobación requisitos",
 "total_con_match": 98,
 "resultados": [
  {
   "id": "EntidadFinanciera_ecai_nacional",
   "type": "EntidadFinanciera",
   "label": "ECAI nacionales",
   "tokens_matcheados": 1,
   "resumen_propiedades": "categoria: Entidad de Calificación Acreditada Internacional"
  },
  {
   "id": "Operacion_evaluacion_de_deudor_como_sujeto_de_credito",
   "type": "Operacion",
   "label": "Evaluación de deudor",
   "tokens_matcheados": 1,
   "resumen_propiedades": "tipo: evaluación de deudor como sujeto de crédito"
  },
  {
   "id": "Obligacion_informar_ecai_elegidas",
   "type": "Obligacion",
   "label": "Informar ECAI elegidas",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Las entidades financieras, a través de sus responsables del área de riesgos, deberán informar las ECAI elegidas a la Gerencia de Supervisión de Entidades Financ…"
  },
  {
   "id": "Obligacion_las_entidades_deberan_dar_cumplimiento_a_los_requisitos_de_identificacion_de_sus",
   "type": "Obligacion",
   "label": "Identificación de clientes",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Las entidades deberán dar cumplimiento a los requisitos de identificación de sus clientes y registro de las operaciones ante el BCRA según el régimen informativ…"
  },
  {
   "id": "Operacion_verificacion_de_cumplimiento",
   "type": "Operacion",
   "label": "Verificación de requisitos",
   "tokens_matcheados": 1,
   "resumen_propiedades": "La entidad que concrete la oferta de suscripción deberá verificar el cumplimiento de requisitos para la suscripción de BOPREAL"
  },
  {
   "id": "Obligacion_debera_verificar_previamente_que_se_cumplen_la_totalidad_de_los_requisitos_estab",
   "type": "Obligacion",
   "label": "Verificar requisitos previos",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Deberá verificar previamente que se cumplen la totalidad de los requisitos establecidos para dar acceso al mercado de cambios"
  },
  {
   "id": "Operacion_cambio_de_ecai",
   "type": "Operacion",
   "label": "Selección arbitraria de ECAI",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Cambio arbitrario de ECAI para evaluación de créditos"
  },
  {
   "id": "Obligacion_correspondera_clasificar_en_esta_categoria_a_los_clientes_que_cualquiera_sea_el_",
   "type": "Obligacion",
   "label": "Evaluación periódica deudores",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Corresponderá clasificar en esta categoría a los clientes que, cualquiera sea el motivo (entre ellos por no contar con legajo o por no haber proporcionado infor…"
  },
  {
   "id": "Operacion_clasificacion_de_deudor",
   "type": "Operacion",
   "label": "Evaluación grado de inversión",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Clasificar a los respectivos deudores en función de su mora, según los criterios aplicables para la cartera de consumo o vivienda"
  },
  {
   "id": "Restriccion_cuando_la_suma_de_los_requisitos_de_capital_de_una_entidad_financiera_por_las_ex",
   "type": "Restriccion",
   "label": "Límite requisito capital QCCP",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Cuando la suma de los requisitos de capital de una entidad financiera por las exposiciones con una QCCP sea mayor que la exigencia resultante de la aplicación d…"
  }
 ]
}
```

### paso 3 — buscar_nodos {"consulta": "ECAI antigüedad años uso metodología comprobación", "limite": 10}

```json
{
 "consulta": "ECAI antigüedad años uso metodología comprobación",
 "total_con_match": 56,
 "resultados": [
  {
   "id": "EntidadFinanciera_ecai_nacional",
   "type": "EntidadFinanciera",
   "label": "ECAI nacionales",
   "tokens_matcheados": 1,
   "resumen_propiedades": "categoria: Entidad de Calificación Acreditada Internacional"
  },
  {
   "id": "Obligacion_informar_ecai_elegidas",
   "type": "Obligacion",
   "label": "Informar ECAI elegidas",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Las entidades financieras, a través de sus responsables del área de riesgos, deberán informar las ECAI elegidas a la Gerencia de Supervisión de Entidades Financ…"
  },
  {
   "id": "Operacion_aprovechamiento_de_beneficio",
   "type": "Operacion",
   "label": "Uso del beneficio ampliado",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Los casos previstos en el punto 1) del artículo 8° bis podrán aplicar durante 2 (dos) años calendario consecutivos por cada año calendario en que no se hiciera …"
  },
  {
   "id": "Operacion_uso_de_cajeros_automaticos",
   "type": "Operacion",
   "label": "Uso de cajeros automáticos",
   "tokens_matcheados": 1,
   "resumen_propiedades": "tipo: uso de cajeros automáticos"
  },
  {
   "id": "Restriccion_la_vida_promedio_de_los_titulos_de_deuda_no_sea_menor_a_los_5_cinco_anos",
   "type": "Restriccion",
   "label": "Vida promedio mínimo 5 años",
   "tokens_matcheados": 1,
   "resumen_propiedades": "La vida promedio de los títulos de deuda no sea menor a los 5 (cinco) años"
  },
  {
   "id": "Restriccion_plazo_de_vencimiento_original_no_inferior_a_cinco_anos",
   "type": "Restriccion",
   "label": "Plazo mínimo de vencimiento",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Plazo de vencimiento original no inferior a cinco años."
  },
  {
   "id": "Operacion_aprovechamiento_combinado_de_beneficios",
   "type": "Operacion",
   "label": "Uso de mecanismos combinados",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Los exportadores podrán utilizar los mecanismos previstos en el punto 7.9. en adición a lo previsto en los puntos 7.10.1. y 7.10.3."
  },
  {
   "id": "Operacion_cambio_de_ecai",
   "type": "Operacion",
   "label": "Selección arbitraria de ECAI",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Cambio arbitrario de ECAI para evaluación de créditos"
  },
  {
   "id": "Restriccion_el_agente_local_no_ha_utilizado_este_mecanismo_por_un_monto_superior_al_equivale",
   "type": "Restriccion",
   "label": "Límite máximo de uso mensual",
   "tokens_matcheados": 1,
   "resumen_propiedades": "El agente local no ha utilizado este mecanismo por un monto superior al equivalente de USD 2.000.000 (dólares estadounidenses dos millones) en el mes calendario…"
  },
  {
   "id": "Restriccion_prohibicion_de_uso_reiterado",
   "type": "Restriccion",
   "label": "Prohibición de uso reiterado",
   "tokens_matcheados": 1,
   "resumen_propiedades": "No ha utilizado ya este mecanismo por esta deuda"
  }
 ]
}
```

### paso 4 — buscar_nodos {"consulta": "metodología ECAI reconocimiento ponderadores requisitos", "limite": 10}

```json
{
 "consulta": "metodología ECAI reconocimiento ponderadores requisitos",
 "total_con_match": 103,
 "resultados": [
  {
   "id": "Obligacion_informar_ecai_utilizadas_y_ponderadores",
   "type": "Obligacion",
   "label": "Informar ECAI utilizadas y ponderadores",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Las entidades financieras deberán informar las ECAI que utilizan para ponderar el riesgo de sus activos por tipo de crédito, los ponderadores de riesgo asociado…"
  },
  {
   "id": "EntidadFinanciera_ecai_nacional",
   "type": "EntidadFinanciera",
   "label": "ECAI nacionales",
   "tokens_matcheados": 1,
   "resumen_propiedades": "categoria: Entidad de Calificación Acreditada Internacional"
  },
  {
   "id": "Obligacion_informar_ecai_elegidas",
   "type": "Obligacion",
   "label": "Informar ECAI elegidas",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Las entidades financieras, a través de sus responsables del área de riesgos, deberán informar las ECAI elegidas a la Gerencia de Supervisión de Entidades Financ…"
  },
  {
   "id": "Obligacion_las_entidades_deberan_dar_cumplimiento_a_los_requisitos_de_identificacion_de_sus",
   "type": "Obligacion",
   "label": "Identificación de clientes",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Las entidades deberán dar cumplimiento a los requisitos de identificación de sus clientes y registro de las operaciones ante el BCRA según el régimen informativ…"
  },
  {
   "id": "Operacion_verificacion_de_cumplimiento",
   "type": "Operacion",
   "label": "Verificación de requisitos",
   "tokens_matcheados": 1,
   "resumen_propiedades": "La entidad que concrete la oferta de suscripción deberá verificar el cumplimiento de requisitos para la suscripción de BOPREAL"
  },
  {
   "id": "Obligacion_debera_verificar_previamente_que_se_cumplen_la_totalidad_de_los_requisitos_estab",
   "type": "Obligacion",
   "label": "Verificar requisitos previos",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Deberá verificar previamente que se cumplen la totalidad de los requisitos establecidos para dar acceso al mercado de cambios"
  },
  {
   "id": "Operacion_cambio_de_ecai",
   "type": "Operacion",
   "label": "Selección arbitraria de ECAI",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Cambio arbitrario de ECAI para evaluación de créditos"
  },
  {
   "id": "Restriccion_cuando_la_suma_de_los_requisitos_de_capital_de_una_entidad_financiera_por_las_ex",
   "type": "Restriccion",
   "label": "Límite requisito capital QCCP",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Cuando la suma de los requisitos de capital de una entidad financiera por las exposiciones con una QCCP sea mayor que la exigencia resultante de la aplicación d…"
  },
  {
   "id": "Obligacion_cumplir_requisitos_de_custodio",
   "type": "Obligacion",
   "label": "Cumplir requisitos de custodio",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Se entiende por custodio a un fiduciario o agente que mantenga los activos bajo un título que no le acuerde ni al custodio ni a sus acreedores un derecho o part…"
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

### paso 5 — ver_nodo {"id": "Obligacion_las_ecai_deberan_divulgar_su_codigo_de_conducta_el_caracter_general_de_sus_acuer"}

```json
{
 "id": "Obligacion_las_ecai_deberan_divulgar_su_codigo_de_conducta_el_caracter_general_de_sus_acuer",
 "type": "Obligacion",
 "label": "Divulgar información requerida",
 "properties": {
  "descripcion": "Las ECAI deberán divulgar: su código de conducta; el carácter general de sus acuerdos de remuneración con las entidades evaluadas; sus métodos de evaluación, incluida la definición de incumplimiento, el horizonte temporal y el significado de cada calificación; las tasas de incumplimiento efectivamente registradas en cada categoría de evaluación y la transición entre las calificaciones.",
  "tipo": "presentacion_informativa"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Punto 10.2. Criterios de elegibilidad."
  }
 ]
}
```

### paso 6 — buscar_nodos {"consulta": "ECAI tres años antigüedad metodología", "limite": 10}

```json
{
 "consulta": "ECAI tres años antigüedad metodología",
 "total_con_match": 40,
 "resultados": [
  {
   "id": "Restriccion_el_primer_pago_de_capital_no_se_registre_antes_de_los_3_tres_anos_de_la_fecha_de",
   "type": "Restriccion",
   "label": "Primer pago capital después 3 años",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El primer pago de capital no se registre antes de los 3 (tres) años de la fecha de emisión"
  },
  {
   "id": "Restriccion_su_vida_promedio_sea_no_inferior_a_3_tres_anos_y_el_primer_pago_de_capital_no_se",
   "type": "Restriccion",
   "label": "Vida promedio mínima 3 años endeudamiento",
   "tokens_matcheados": 2,
   "resumen_propiedades": "su vida promedio sea no inferior a 3 (tres) años y el primer pago de capital no se registre antes de cumplirse el año del ingreso de los fondos"
  },
  {
   "id": "EntidadFinanciera_ecai_nacional",
   "type": "EntidadFinanciera",
   "label": "ECAI nacionales",
   "tokens_matcheados": 1,
   "resumen_propiedades": "categoria: Entidad de Calificación Acreditada Internacional"
  },
  {
   "id": "Obligacion_informar_ecai_elegidas",
   "type": "Obligacion",
   "label": "Informar ECAI elegidas",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Las entidades financieras, a través de sus responsables del área de riesgos, deberán informar las ECAI elegidas a la Gerencia de Supervisión de Entidades Financ…"
  },
  {
   "id": "Restriccion_la_vida_promedio_de_los_titulos_de_deuda_no_sea_menor_a_los_5_cinco_anos",
   "type": "Restriccion",
   "label": "Vida promedio mínimo 5 años",
   "tokens_matcheados": 1,
   "resumen_propiedades": "La vida promedio de los títulos de deuda no sea menor a los 5 (cinco) años"
  },
  {
   "id": "Restriccion_plazo_de_vencimiento_original_no_inferior_a_cinco_anos",
   "type": "Restriccion",
   "label": "Plazo mínimo de vencimiento",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Plazo de vencimiento original no inferior a cinco años."
  },
  {
   "id": "Operacion_cambio_de_ecai",
   "type": "Operacion",
   "label": "Selección arbitraria de ECAI",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Cambio arbitrario de ECAI para evaluación de créditos"
  },
  {
   "id": "Obligacion_las_ecai_deberan_divulgar_su_codigo_de_conducta_el_caracter_general_de_sus_acuer",
   "type": "Obligacion",
   "label": "Divulgar información requerida",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Las ECAI deberán divulgar: su código de conducta; el carácter general de sus acuerdos de remuneración con las entidades evaluadas; sus métodos de evaluación, in…"
  },
  {
   "id": "Obligacion_usar_ecai_en_forma_consistente",
   "type": "Obligacion",
   "label": "Usar ECAI en forma consistente",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Las entidades financieras utilizarán las ECAI seleccionadas y sus calificaciones para cada tipo de crédito en forma consistente, tanto para fines de ponderación…"
  },
  {
   "id": "Restriccion_a_partir_del_comienzo_de_cada_uno_de_los_ultimos_cinco_anos_de_vida_de_cada_emis",
   "type": "Restriccion",
   "label": "Disminución de monto computable",
   "tokens_matcheados": 1,
   "resumen_propiedades": "A partir del comienzo de cada uno de los últimos cinco años de vida de cada emisión, el importe computable será disminuido en el 20 % del valor nominal emitido."
  }
 ]
}
```

### paso 7 — buscar_nodos {"consulta": "ECAI metodología reconocida acreditada requisitos elegibilidad", "limite": 10}

```json
{
 "consulta": "ECAI metodología reconocida acreditada requisitos elegibilidad",
 "total_con_match": 84,
 "resultados": [
  {
   "id": "EntidadFinanciera_ecai_nacional",
   "type": "EntidadFinanciera",
   "label": "ECAI nacionales",
   "tokens_matcheados": 1,
   "resumen_propiedades": "categoria: Entidad de Calificación Acreditada Internacional"
  },
  {
   "id": "Operacion_seleccion_de_subyacentes_mediante_criterios_de_elegibilidad",
   "type": "Operacion",
   "label": "Selección de activos",
   "tokens_matcheados": 1,
   "resumen_propiedades": "La selección de los activos deberá estar sujeta a criterios de elegibilidad claramente definidos, tales como el tamaño de la obligación, la edad del sujeto de c…"
  },
  {
   "id": "Obligacion_informar_ecai_elegidas",
   "type": "Obligacion",
   "label": "Informar ECAI elegidas",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Las entidades financieras, a través de sus responsables del área de riesgos, deberán informar las ECAI elegidas a la Gerencia de Supervisión de Entidades Financ…"
  },
  {
   "id": "Obligacion_las_entidades_deberan_dar_cumplimiento_a_los_requisitos_de_identificacion_de_sus",
   "type": "Obligacion",
   "label": "Identificación de clientes",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Las entidades deberán dar cumplimiento a los requisitos de identificación de sus clientes y registro de las operaciones ante el BCRA según el régimen informativ…"
  },
  {
   "id": "Operacion_verificacion_de_cumplimiento",
   "type": "Operacion",
   "label": "Verificación de requisitos",
   "tokens_matcheados": 1,
   "resumen_propiedades": "La entidad que concrete la oferta de suscripción deberá verificar el cumplimiento de requisitos para la suscripción de BOPREAL"
  },
  {
   "id": "Obligacion_debera_verificar_previamente_que_se_cumplen_la_totalidad_de_los_requisitos_estab",
   "type": "Obligacion",
   "label": "Verificar requisitos previos",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Deberá verificar previamente que se cumplen la totalidad de los requisitos establecidos para dar acceso al mercado de cambios"
  },
  {
   "id": "Operacion_cambio_de_ecai",
   "type": "Operacion",
   "label": "Selección arbitraria de ECAI",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Cambio arbitrario de ECAI para evaluación de créditos"
  },
  {
   "id": "Restriccion_cuando_la_suma_de_los_requisitos_de_capital_de_una_entidad_financiera_por_las_ex",
   "type": "Restriccion",
   "label": "Límite requisito capital QCCP",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Cuando la suma de los requisitos de capital de una entidad financiera por las exposiciones con una QCCP sea mayor que la exigencia resultante de la aplicación d…"
  },
  {
   "id": "Obligacion_cumplir_requisitos_de_custodio",
   "type": "Obligacion",
   "label": "Cumplir requisitos de custodio",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Se entiende por custodio a un fiduciario o agente que mantenga los activos bajo un título que no le acuerde ni al custodio ni a sus acreedores un derecho o part…"
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

### paso 8 — buscar_nodos {"consulta": "ECAI comprobación validación metodología histórico", "limite": 10}

```json
{
 "consulta": "ECAI comprobación validación metodología histórico",
 "total_con_match": 25,
 "resultados": [
  {
   "id": "EntidadFinanciera_ecai_nacional",
   "type": "EntidadFinanciera",
   "label": "ECAI nacionales",
   "tokens_matcheados": 1,
   "resumen_propiedades": "categoria: Entidad de Calificación Acreditada Internacional"
  },
  {
   "id": "Obligacion_informar_ecai_elegidas",
   "type": "Obligacion",
   "label": "Informar ECAI elegidas",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Las entidades financieras, a través de sus responsables del área de riesgos, deberán informar las ECAI elegidas a la Gerencia de Supervisión de Entidades Financ…"
  },
  {
   "id": "Operacion_cambio_de_ecai",
   "type": "Operacion",
   "label": "Selección arbitraria de ECAI",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Cambio arbitrario de ECAI para evaluación de créditos"
  },
  {
   "id": "Obligacion_las_ecai_deberan_divulgar_su_codigo_de_conducta_el_caracter_general_de_sus_acuer",
   "type": "Obligacion",
   "label": "Divulgar información requerida",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Las ECAI deberán divulgar: su código de conducta; el carácter general de sus acuerdos de remuneración con las entidades evaluadas; sus métodos de evaluación, in…"
  },
  {
   "id": "Obligacion_usar_ecai_en_forma_consistente",
   "type": "Obligacion",
   "label": "Usar ECAI en forma consistente",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Las entidades financieras utilizarán las ECAI seleccionadas y sus calificaciones para cada tipo de crédito en forma consistente, tanto para fines de ponderación…"
  },
  {
   "id": "Obligacion_aplicar_metodologia_anexo_a_5867",
   "type": "Obligacion",
   "label": "Aplicar metodología Anexo A 5867",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Exigencia por riesgo de mercado calculada conforme a la metodología aplicable según Anexo a la Comunicación A 5867"
  },
  {
   "id": "Obligacion_la_metodologia_utilizada_para_asignar_las_calificaciones_crediticias_debera_ser_",
   "type": "Obligacion",
   "label": "Cumplir criterios de objetividad",
   "tokens_matcheados": 1,
   "resumen_propiedades": "La metodología utilizada para asignar las calificaciones crediticias deberá ser rigurosa, sistemática y estar sujeta a algún tipo de validación basada en la exp…"
  },
  {
   "id": "Obligacion_las_ecai_deberan_contar_con_recursos_suficientes_para_poder_realizar_evaluacione",
   "type": "Obligacion",
   "label": "Disponer de recursos suficientes",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Las ECAI deberán contar con recursos suficientes para poder realizar evaluaciones crediticias de alta calidad. Estos recursos deberán permitirles estar en conta…"
  },
  {
   "id": "Obligacion_el_importe_por_encima_de_este_10_debera_deducirse_de_cada_uno_de_los_niveles_de_",
   "type": "Obligacion",
   "label": "Deducir según metodología capital",
   "tokens_matcheados": 1,
   "resumen_propiedades": "El importe por encima de este 10 % deberá deducirse de cada uno de los niveles de capital en función de la siguiente metodología: Monto a deducir del CON1: tota…"
  },
  {
   "id": "Operacion_presentacion_informativa_de_operaciones_cambiarias",
   "type": "Operacion",
   "label": "Validación en régimen informativo",
   "tokens_matcheados": 1,
   "resumen_propiedades": "tipo: presentación informativa de operaciones cambiarias"
  }
 ]
}
```

### paso 9 — ver_nodo {"id": "Obligacion_la_metodologia_utilizada_para_asignar_las_calificaciones_crediticias_debera_ser_"}

```json
{
 "id": "Obligacion_la_metodologia_utilizada_para_asignar_las_calificaciones_crediticias_debera_ser_",
 "type": "Obligacion",
 "label": "Cumplir criterios de objetividad",
 "properties": {
  "descripcion": "La metodología utilizada para asignar las calificaciones crediticias deberá ser rigurosa, sistemática y estar sujeta a algún tipo de validación basada en la experiencia histórica. Las evaluaciones deberán ser objeto de un control constante y responder a los cambios en la coyuntura financiera. La metodología de evaluación deberá haber sido utilizada durante al menos un año –preferiblemente tres años– y haber estado sujeta a la comprobación rigurosa de su precisión mediante pruebas retrospectivas (backtesting).",
  "tipo": "otra"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Punto 10.2. Criterios de elegibilidad."
  }
 ]
}
```

### paso 10 — ver_vecinos {"id": "Obligacion_la_metodologia_utilizada_para_asignar_las_calificaciones_crediticias_debera_ser_"}

```json
{
 "id": "Obligacion_la_metodologia_utilizada_para_asignar_las_calificaciones_crediticias_debera_ser_",
 "label": "Cumplir criterios de objetividad",
 "n_salientes_total": 3,
 "n_entrantes_total": 0,
 "salientes": [
  {
   "relation": "establecida_en",
   "vecino_id": "TextoOrdenado_to_capitales_minimos_actual_pdf",
   "vecino_label": "Capitales Mínimos",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 10.2. Criterios de elegibilidad."
    }
   ]
  },
  {
   "relation": "aplica_a",
   "vecino_id": "EntidadFinanciera_ecai_nacional",
   "vecino_label": "ECAI nacionales",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 10.2. Criterios de elegibilidad."
    }
   ]
  },
  {
   "relation": "regula",
   "vecino_id": "Operacion_asignacion_de_calificaciones",
   "vecino_label": "Asignación de calificaciones crediticias",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 10.2. Criterios de elegibilidad."
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

# CQN2-010

## Respuesta final íntegra (trace.final_json)

```json
{
 "respuesta": "(a) No se encontró en el Knowledge Graph información explícita que confirme si el fiduciario de un fideicomiso financiero es sujeto obligado bajo la normativa de protección de usuarios de servicios financieros, ni si los deudores cedidos revisten carácter de usuarios aunque no hayan sido notificados de la cesión. (b) Según la normativa de clasificación de deudores, cuando un cliente registra financiaciones equivalentes al 5% o más del activo del fideicomiso financiero, su clasificación debe revisarse con una periodicidad mínima trimestral (en el curso de cada trimestre calendario).",
 "citas": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Punto 6.3. Periodicidad mínima de clasificación."
  }
 ],
 "respondible": false
}
```

(`respondible`: false · tool_calls: 16 · hit_tool_limit: True)

## Inventario de pasos + fidelidad runtime↔re-ejecución

| paso | tool | input | output_chars (runtime) | re-ejecutado | fiel |
|---|---|---|---|---|---|
| 1 | buscar_nodos | `{"consulta": "fideicomiso financiero fiduciario acreedor usuarios", "limite": 10}` | 2336 | 2336 | SÍ |
| 2 | buscar_nodos | `{"consulta": "protección usuarios servicios financieros sujeto obligado", "limite": 1` | 3808 | 3808 | SÍ |
| 3 | buscar_nodos | `{"consulta": "clasificación créditos cartera comercial periodicidad revisión", "limit` | 2881 | 2881 | SÍ |
| 4 | ver_nodo | `{"id": "TextoOrdenado_to_proteccion_usuarios_servicios_financieros_actual_pdf"}` | 434 | 434 | SÍ |
| 5 | ver_nodo | `{"id": "EntidadFinanciera_fiduciario_de_fideicomiso_financiero"}` | 395 | 395 | SÍ |
| 6 | ver_nodo | `{"id": "Operacion_revision_de_clasificacion_de_deudores"}` | 622 | 622 | SÍ |
| 7 | ver_vecinos | `{"id": "EntidadFinanciera_fiduciario_de_fideicomiso_financiero", "direccion": "salien` | 210 | 210 | SÍ |
| 8 | buscar_nodos | `{"consulta": "fiduciario sujeto obligado protección usuarios", "limite": 10}` | 3468 | 3468 | SÍ |
| 9 | buscar_nodos | `{"consulta": "deudor cedido usuario notificación cesión", "limite": 10}` | 2475 | 2475 | SÍ |
| 10 | buscar_nodos | `{"consulta": "fiduciario fideicomiso financiero sujeto obligado", "limite": 10}` | 3025 | 3025 | SÍ |
| 11 | buscar_nodos | `{"consulta": "deudor usuario cartera cedida fideicomiso", "limite": 10}` | 2398 | 2398 | SÍ |
| 12 | ver_vecinos | `{"id": "Operacion_revision_de_clasificacion_de_deudores", "direccion": "entrantes"}` | 2184 | 2184 | SÍ |
| 13 | ver_vecinos | `{"id": "EntidadFinanciera_sujeto_obligado", "direccion": "entrantes"}` | 12972 | 12972 | SÍ |
| 14 | buscar_nodos | `{"consulta": "deudor cedido usuario aunque no notificado", "limite": 10}` | 3433 | 3433 | SÍ |
| 15 | buscar_nodos | `{"consulta": "sujetos obligados protección usuarios punto 1.1 partes", "limite": 10}` | 3371 | 3371 | SÍ |
| 16 | buscar_nodos | `{"consulta": "deudor usuario cartera cedida aunque no notificado", "limite": 10}` | 3529 | 3529 | SÍ |

**Fidelidad: 16/16**.

## Apéndice — outputs completos re-ejecutados

### paso 1 — buscar_nodos {"consulta": "fideicomiso financiero fiduciario acreedor usuarios", "limite": 10}

```json
{
 "consulta": "fideicomiso financiero fiduciario acreedor usuarios",
 "total_con_match": 85,
 "resultados": [
  {
   "id": "EntidadFinanciera_fiduciario_fideicomiso_financiero",
   "type": "EntidadFinanciera",
   "label": "Fiduciarios fideicomisos financieros",
   "tokens_matcheados": 3,
   "resumen_propiedades": "categoria: fiduciario fideicomiso financiero"
  },
  {
   "id": "EntidadFinanciera_fiduciario_de_fideicomiso_financiero",
   "type": "EntidadFinanciera",
   "label": "Fiduciarios de fideicomisos financieros",
   "tokens_matcheados": 3,
   "resumen_propiedades": "categoria: fiduciario de fideicomiso financiero"
  },
  {
   "id": "EntidadFinanciera_fideicomiso_financiero",
   "type": "EntidadFinanciera",
   "label": "Fideicomisos financieros",
   "tokens_matcheados": 2,
   "resumen_propiedades": "categoria: fideicomiso financiero"
  },
  {
   "id": "EntidadFinanciera_usuario_de_servicio_financiero",
   "type": "EntidadFinanciera",
   "label": "Usuarios de servicios financieros",
   "tokens_matcheados": 2,
   "resumen_propiedades": "categoria: usuario de servicio financiero"
  },
  {
   "id": "Obligacion_el_contrato_de_fideicomiso_debera_incluir_el_modo_de_sustitucion_del_fiduciario_",
   "type": "Obligacion",
   "label": "Incluir modo de sustitución del fiduciario",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El contrato de fideicomiso deberá incluir el modo de sustitución del fiduciario en el caso de que cese por algunas de las causales previstas en el Código Civil …"
  },
  {
   "id": "EntidadFinanciera_fiduciario",
   "type": "EntidadFinanciera",
   "label": "Fiduciarios",
   "tokens_matcheados": 1,
   "resumen_propiedades": "categoria: fiduciario"
  },
  {
   "id": "EntidadFinanciera_fideicomiso",
   "type": "EntidadFinanciera",
   "label": "Fideicomisos",
   "tokens_matcheados": 1,
   "resumen_propiedades": "categoria: fideicomiso"
  },
  {
   "id": "EntidadFinanciera_acreedor_inicial",
   "type": "EntidadFinanciera",
   "label": "Acreedor inicial",
   "tokens_matcheados": 1,
   "resumen_propiedades": "categoria: acreedor inicial"
  },
  {
   "id": "EntidadFinanciera_usuario_del_rigi",
   "type": "EntidadFinanciera",
   "label": "Usuarios del RIGI",
   "tokens_matcheados": 1,
   "resumen_propiedades": "categoria: VPU (Personas Usuarias del Régimen)"
  },
  {
   "id": "Operacion_derivado_financiero",
   "type": "Operacion",
   "label": "Operaciones derivadas",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Cualquier otro tipo de derivado instrumentado bajo ley argentina"
  }
 ]
}
```

### paso 2 — buscar_nodos {"consulta": "protección usuarios servicios financieros sujeto obligado", "limite": 10}

```json
{
 "consulta": "protección usuarios servicios financieros sujeto obligado",
 "total_con_match": 189,
 "resultados": [
  {
   "id": "TextoOrdenado_to_proteccion_usuarios_servicios_financieros_actual_pdf",
   "type": "TextoOrdenado",
   "label": "Protección de Usuarios",
   "tokens_matcheados": 4,
   "resumen_propiedades": "materia: Protección de los usuarios de servicios financieros; archivo: TO_proteccion_usuarios_servicios_financieros_actual.pdf; version: 8a"
  },
  {
   "id": "Obligacion_el_sujeto_obligado_debera_ante_la_solicitud_del_usuario_de_servicios_financieros",
   "type": "Obligacion",
   "label": "Extender constancia de consulta o reclamo",
   "tokens_matcheados": 4,
   "resumen_propiedades": "El sujeto obligado deberá, ante la solicitud del usuario de servicios financieros, extender una constancia con la identificación de su consulta o reclamo y el e…"
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
   "id": "Restriccion_el_importe_de_los_cargos_que_el_sujeto_obligado_transfiera_a_los_usuarios_no_pod",
   "type": "Restriccion",
   "label": "Cargos no superiores a costo de terceros",
   "tokens_matcheados": 3,
   "resumen_propiedades": "El importe de los cargos que el sujeto obligado transfiera a los usuarios no podrá ser superior al que el tercero prestador perciba de particulares, sin interme…"
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
   "id": "Obligacion_el_sujeto_obligado_debera_verificar_si_situaciones_que_generan_la_obligacion_de_",
   "type": "Obligacion",
   "label": "Verificar situaciones de reintegro en usuarios",
   "tokens_matcheados": 3,
   "resumen_propiedades": "El sujeto obligado deberá verificar si situaciones que generan la obligación de reintegros ha ocurrido respecto de los usuarios que se encuentren en la misma si…"
  }
 ]
}
```

### paso 3 — buscar_nodos {"consulta": "clasificación créditos cartera comercial periodicidad revisión", "limite": 10}

```json
{
 "consulta": "clasificación créditos cartera comercial periodicidad revisión",
 "total_con_match": 143,
 "resultados": [
  {
   "id": "Operacion_revision_de_cartera",
   "type": "Operacion",
   "label": "Revisión cartera comercial",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La revisión de la cartera comercial se practicará sobre la base de la información financiera actualizada"
  },
  {
   "id": "Obligacion_de_optar_por_encargar_la_clasificacion_al_sector_de_creditos_la_entidad_financie",
   "type": "Obligacion",
   "label": "Contar con oficina independiente de revisión",
   "tokens_matcheados": 3,
   "resumen_propiedades": "De optar por encargar la clasificación al sector de créditos, la entidad financiera deberá contar con una oficina independiente que tendrá como función efectuar…"
  },
  {
   "id": "Operacion_clasificacion_de_cartera",
   "type": "Operacion",
   "label": "Agrupación de cartera",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: clasificación de cartera"
  },
  {
   "id": "EntidadFinanciera_deudor_cartera_comercial",
   "type": "EntidadFinanciera",
   "label": "Deudores cartera comercial",
   "tokens_matcheados": 2,
   "resumen_propiedades": "categoria: deudor cartera comercial"
  },
  {
   "id": "Operacion_clasificacion_de_deudores_en_situacion_irregular",
   "type": "Operacion",
   "label": "Incremento cartera irregular",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: clasificación de deudores en situación irregular"
  },
  {
   "id": "Operacion_compra_de_cartera",
   "type": "Operacion",
   "label": "Compra de cartera de créditos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: compra de cartera"
  },
  {
   "id": "Obligacion_en_el_curso_del_ejercicio_economico_en_los_demas_casos_por_lo_que_a_su_finalizac",
   "type": "Obligacion",
   "label": "Revisión totalidad cartera anual",
   "tokens_matcheados": 2,
   "resumen_propiedades": "En el curso del ejercicio económico, en los demás casos, por lo que a su finalización la revisión deberá haber alcanzado a la totalidad de la cartera comercial …"
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
   "id": "Operacion_revision_de_clasificacion",
   "type": "Operacion",
   "label": "Revisión de clasificaciones asignadas",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: revisión de clasificación"
  }
 ]
}
```

### paso 4 — ver_nodo {"id": "TextoOrdenado_to_proteccion_usuarios_servicios_financieros_actual_pdf"}

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

### paso 5 — ver_nodo {"id": "EntidadFinanciera_fiduciario_de_fideicomiso_financiero"}

```json
{
 "id": "EntidadFinanciera_fiduciario_de_fideicomiso_financiero",
 "type": "EntidadFinanciera",
 "label": "Fiduciarios de fideicomisos financieros",
 "properties": {
  "categoria": "fiduciario de fideicomiso financiero"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Punto 10.2. Fiduciarios de fideicomisos financieros comprendidos en la Ley de Entidades Fina"
  }
 ]
}
```

### paso 6 — ver_nodo {"id": "Operacion_revision_de_clasificacion_de_deudores"}

```json
{
 "id": "Operacion_revision_de_clasificacion_de_deudores",
 "type": "Operacion",
 "label": "Revisión de clasificación trimestral",
 "properties": {
  "tipo": "revisión de clasificación de deudores",
  "description": "En el curso de cada trimestre calendario, respecto de clientes individualmente considerados cuyas financiaciones comprendidas en algún momento sean equivalentes al 5% o más de la RPC o del activo del fideicomiso financiero del mes anterior a la finalización de dicho período"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Punto 6.3. Periodicidad mínima de clasificación."
  }
 ]
}
```

### paso 7 — ver_vecinos {"id": "EntidadFinanciera_fiduciario_de_fideicomiso_financiero", "direccion": "salientes"}

```json
{
 "id": "EntidadFinanciera_fiduciario_de_fideicomiso_financiero",
 "label": "Fiduciarios de fideicomisos financieros",
 "n_salientes_total": 0,
 "n_entrantes_total": 2,
 "salientes": [],
 "salientes_truncado": false
}
```

### paso 8 — buscar_nodos {"consulta": "fiduciario sujeto obligado protección usuarios", "limite": 10}

```json
{
 "consulta": "fiduciario sujeto obligado protección usuarios",
 "total_con_match": 87,
 "resultados": [
  {
   "id": "Restriccion_el_importe_de_los_cargos_que_el_sujeto_obligado_transfiera_a_los_usuarios_no_pod",
   "type": "Restriccion",
   "label": "Cargos no superiores a costo de terceros",
   "tokens_matcheados": 3,
   "resumen_propiedades": "El importe de los cargos que el sujeto obligado transfiera a los usuarios no podrá ser superior al que el tercero prestador perciba de particulares, sin interme…"
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
   "id": "Obligacion_en_el_caso_de_que_el_sujeto_obligado_pretenda_incorporar_nuevos_conceptos_en_cal",
   "type": "Obligacion",
   "label": "Obtener consentimiento del usuario",
   "tokens_matcheados": 2,
   "resumen_propiedades": "En el caso de que el sujeto obligado pretenda incorporar nuevos conceptos en calidad de comisiones y/o cargos que no hubiesen sido previstos en el contrato o re…"
  },
  {
   "id": "Obligacion_el_sujeto_obligado_debera_conservar_constancia_de_haber_permitido_el_ejercicio_d",
   "type": "Obligacion",
   "label": "Constancia de ejercicio de derechos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El sujeto obligado deberá conservar constancia de haber permitido el ejercicio de este derecho."
  },
  {
   "id": "Obligacion_a_los_fines_de_la_comparacion_el_sujeto_obligado_debera_informarle_al_usuario_la",
   "type": "Obligacion",
   "label": "Informar cobertura mínima del seguro",
   "tokens_matcheados": 2,
   "resumen_propiedades": "A los fines de la comparación, el sujeto obligado deberá informarle al usuario la cobertura mínima que debe prever el seguro en cuestión"
  }
 ]
}
```

### paso 9 — buscar_nodos {"consulta": "deudor cedido usuario notificación cesión", "limite": 10}

```json
{
 "consulta": "deudor cedido usuario notificación cesión",
 "total_con_match": 102,
 "resultados": [
  {
   "id": "EntidadFinanciera_deudor",
   "type": "EntidadFinanciera",
   "label": "Deudores",
   "tokens_matcheados": 1,
   "resumen_propiedades": "categoria: deudor"
  },
  {
   "id": "Excepcion_importador_demuestra_gestion_de_cobro_a_traves_de_reclamos_a_companias_de_seguro",
   "type": "Excepcion",
   "label": "Deudor moroso",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Importador demuestra gestión de cobro a través de reclamos a compañías de seguro de crédito o agencias de recupero, o mantiene acciones judiciales contra el pro…"
  },
  {
   "id": "EntidadFinanciera_usuario_del_rigi",
   "type": "EntidadFinanciera",
   "label": "Usuarios del RIGI",
   "tokens_matcheados": 1,
   "resumen_propiedades": "categoria: VPU (Personas Usuarias del Régimen)"
  },
  {
   "id": "Operacion_cesion_de_creditos_sin_responsabilidad",
   "type": "Operacion",
   "label": "Cesión de créditos",
   "tokens_matcheados": 1,
   "resumen_propiedades": "tipo: cesión de créditos sin responsabilidad"
  },
  {
   "id": "Operacion_evaluacion_de_deudor_como_sujeto_de_credito",
   "type": "Operacion",
   "label": "Evaluación de deudor",
   "tokens_matcheados": 1,
   "resumen_propiedades": "tipo: evaluación de deudor como sujeto de crédito"
  },
  {
   "id": "Operacion_operaciones_de_titulizacion_y_venta_o_cesion_de_cartera_con_responsabilidad",
   "type": "Operacion",
   "label": "Titulización cartera",
   "tokens_matcheados": 1,
   "resumen_propiedades": "tipo: Operaciones de titulización y venta o cesión de cartera con responsabilidad"
  },
  {
   "id": "Obligacion_llevar_legajo_de_deudor",
   "type": "Obligacion",
   "label": "Llevar legajo de deudor",
   "tokens_matcheados": 1,
   "resumen_propiedades": "La entidad deberá llevar un legajo de cada deudor de su cartera, así como de cada uno de sus corresponsales, de acuerdo con lo establecido en las normas sobre C…"
  },
  {
   "id": "Operacion_clasificacion_de_deudor_en_categoria",
   "type": "Operacion",
   "label": "Clasificación de deudor",
   "tokens_matcheados": 1,
   "resumen_propiedades": "tipo: clasificación de deudor en categoría"
  },
  {
   "id": "Operacion_clasificacion_de_deudor_segun_mora",
   "type": "Operacion",
   "label": "Clasificación de deudor",
   "tokens_matcheados": 1,
   "resumen_propiedades": "tipo: clasificación de deudor según mora"
  },
  {
   "id": "Operacion_otorgamiento_de_credito_a_deudor_en_concurso",
   "type": "Operacion",
   "label": "Otorgamiento de crédito",
   "tokens_matcheados": 1,
   "resumen_propiedades": "tipo: otorgamiento de crédito a deudor en concurso"
  }
 ]
}
```

### paso 10 — buscar_nodos {"consulta": "fiduciario fideicomiso financiero sujeto obligado", "limite": 10}

```json
{
 "consulta": "fiduciario fideicomiso financiero sujeto obligado",
 "total_con_match": 76,
 "resultados": [
  {
   "id": "EntidadFinanciera_fiduciario_fideicomiso_financiero",
   "type": "EntidadFinanciera",
   "label": "Fiduciarios fideicomisos financieros",
   "tokens_matcheados": 3,
   "resumen_propiedades": "categoria: fiduciario fideicomiso financiero"
  },
  {
   "id": "EntidadFinanciera_fiduciario_de_fideicomiso_financiero",
   "type": "EntidadFinanciera",
   "label": "Fiduciarios de fideicomisos financieros",
   "tokens_matcheados": 3,
   "resumen_propiedades": "categoria: fiduciario de fideicomiso financiero"
  },
  {
   "id": "EntidadFinanciera_sujeto_obligado",
   "type": "EntidadFinanciera",
   "label": "Sujetos obligados",
   "tokens_matcheados": 2,
   "resumen_propiedades": "categoria: entidades financieras"
  },
  {
   "id": "EntidadFinanciera_fideicomiso_financiero",
   "type": "EntidadFinanciera",
   "label": "Fideicomisos financieros",
   "tokens_matcheados": 2,
   "resumen_propiedades": "categoria: fideicomiso financiero"
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
   "id": "Obligacion_en_el_caso_de_que_el_sujeto_obligado_pretenda_incorporar_nuevos_conceptos_en_cal",
   "type": "Obligacion",
   "label": "Obtener consentimiento del usuario",
   "tokens_matcheados": 2,
   "resumen_propiedades": "En el caso de que el sujeto obligado pretenda incorporar nuevos conceptos en calidad de comisiones y/o cargos que no hubiesen sido previstos en el contrato o re…"
  },
  {
   "id": "Obligacion_el_sujeto_obligado_debera_conservar_constancia_de_haber_permitido_el_ejercicio_d",
   "type": "Obligacion",
   "label": "Constancia de ejercicio de derechos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El sujeto obligado deberá conservar constancia de haber permitido el ejercicio de este derecho."
  },
  {
   "id": "Obligacion_a_los_fines_de_la_comparacion_el_sujeto_obligado_debera_informarle_al_usuario_la",
   "type": "Obligacion",
   "label": "Informar cobertura mínima del seguro",
   "tokens_matcheados": 2,
   "resumen_propiedades": "A los fines de la comparación, el sujeto obligado deberá informarle al usuario la cobertura mínima que debe prever el seguro en cuestión"
  },
  {
   "id": "Restriccion_el_cargo_que_el_sujeto_obligado_aplique_al_usuario_no_podra_ser_superior_al_que_",
   "type": "Restriccion",
   "label": "Límite de cargo por seguro accesorio",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El cargo que el sujeto obligado aplique al usuario no podrá ser superior al que la compañía de seguros elegida perciba por operaciones con particulares y sin la…"
  }
 ]
}
```

### paso 11 — buscar_nodos {"consulta": "deudor usuario cartera cedida fideicomiso", "limite": 10}

```json
{
 "consulta": "deudor usuario cartera cedida fideicomiso",
 "total_con_match": 122,
 "resultados": [
  {
   "id": "EntidadFinanciera_deudor_cartera_comercial",
   "type": "EntidadFinanciera",
   "label": "Deudores cartera comercial",
   "tokens_matcheados": 2,
   "resumen_propiedades": "categoria: deudor cartera comercial"
  },
  {
   "id": "EntidadFinanciera_deudor",
   "type": "EntidadFinanciera",
   "label": "Deudores",
   "tokens_matcheados": 1,
   "resumen_propiedades": "categoria: deudor"
  },
  {
   "id": "EntidadFinanciera_fideicomiso",
   "type": "EntidadFinanciera",
   "label": "Fideicomisos",
   "tokens_matcheados": 1,
   "resumen_propiedades": "categoria: fideicomiso"
  },
  {
   "id": "Excepcion_importador_demuestra_gestion_de_cobro_a_traves_de_reclamos_a_companias_de_seguro",
   "type": "Excepcion",
   "label": "Deudor moroso",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Importador demuestra gestión de cobro a través de reclamos a compañías de seguro de crédito o agencias de recupero, o mantiene acciones judiciales contra el pro…"
  },
  {
   "id": "EntidadFinanciera_usuario_del_rigi",
   "type": "EntidadFinanciera",
   "label": "Usuarios del RIGI",
   "tokens_matcheados": 1,
   "resumen_propiedades": "categoria: VPU (Personas Usuarias del Régimen)"
  },
  {
   "id": "Operacion_evaluacion_de_deudor_como_sujeto_de_credito",
   "type": "Operacion",
   "label": "Evaluación de deudor",
   "tokens_matcheados": 1,
   "resumen_propiedades": "tipo: evaluación de deudor como sujeto de crédito"
  },
  {
   "id": "Operacion_operaciones_de_titulizacion_y_venta_o_cesion_de_cartera_con_responsabilidad",
   "type": "Operacion",
   "label": "Titulización cartera",
   "tokens_matcheados": 1,
   "resumen_propiedades": "tipo: Operaciones de titulización y venta o cesión de cartera con responsabilidad"
  },
  {
   "id": "Operacion_clasificacion_de_cartera",
   "type": "Operacion",
   "label": "Agrupación de cartera",
   "tokens_matcheados": 1,
   "resumen_propiedades": "tipo: clasificación de cartera"
  },
  {
   "id": "Obligacion_llevar_legajo_de_deudor",
   "type": "Obligacion",
   "label": "Llevar legajo de deudor",
   "tokens_matcheados": 1,
   "resumen_propiedades": "La entidad deberá llevar un legajo de cada deudor de su cartera, así como de cada uno de sus corresponsales, de acuerdo con lo establecido en las normas sobre C…"
  },
  {
   "id": "Operacion_clasificacion_de_deudor_en_categoria",
   "type": "Operacion",
   "label": "Clasificación de deudor",
   "tokens_matcheados": 1,
   "resumen_propiedades": "tipo: clasificación de deudor en categoría"
  }
 ]
}
```

### paso 12 — ver_vecinos {"id": "Operacion_revision_de_clasificacion_de_deudores", "direccion": "entrantes"}

```json
{
 "id": "Operacion_revision_de_clasificacion_de_deudores",
 "label": "Revisión de clasificación trimestral",
 "n_salientes_total": 0,
 "n_entrantes_total": 6,
 "entrantes": [
  {
   "relation": "limita",
   "vecino_id": "Restriccion_clientes_cuyas_financiaciones_sean_equivalentes_al_5_o_mas_de_la_rpc_o_del_activ",
   "vecino_label": "Límite mínimo RPC clientes revisión trimestral",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "Punto 6.3. Periodicidad mínima de clasificación."
    }
   ]
  },
  {
   "relation": "limita",
   "vecino_id": "Restriccion_clientes_cuyas_financiaciones_sumen_entre_el_1_o_el_equivalente_a_dos_veces_el_i",
   "vecino_label": "Rango RPC clientes revisión semestral",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "Punto 6.3. Periodicidad mínima de clasificación."
    }
   ]
  },
  {
   "relation": "condiciona",
   "vecino_id": "Obligacion_la_revision_debera_efectuarse_como_minimo_con_la_periodicidad_que_se_indica_segu",
   "vecino_label": "Revisión trimestral clientes mayor riesgo",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "Punto 6.3. Periodicidad mínima de clasificación."
    }
   ]
  },
  {
   "relation": "condiciona",
   "vecino_id": "Obligacion_revision_en_el_curso_de_cada_semestre_calendario_respecto_de_clientes_cuyas_fina",
   "vecino_label": "Revisión semestral clientes medio riesgo",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "Punto 6.3. Periodicidad mínima de clasificación."
    }
   ]
  },
  {
   "relation": "condiciona",
   "vecino_id": "Obligacion_al_cierre_del_primer_semestre_calendario_el_examen_debera_haber_alcanzado_no_men",
   "vecino_label": "Cobertura mínima 50% cartera semestral",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "Punto 6.3. Periodicidad mínima de clasificación."
    }
   ]
  },
  {
   "relation": "condiciona",
   "vecino_id": "Obligacion_en_el_curso_del_ejercicio_economico_en_los_demas_casos_por_lo_que_a_su_finalizac",
   "vecino_label": "Revisión totalidad cartera anual",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "Punto 6.3. Periodicidad mínima de clasificación."
    }
   ]
  }
 ],
 "entrantes_truncado": false
}
```

### paso 13 — ver_vecinos {"id": "EntidadFinanciera_sujeto_obligado", "direccion": "entrantes"}

```json
{
 "id": "EntidadFinanciera_sujeto_obligado",
 "label": "Sujetos obligados",
 "n_salientes_total": 104,
 "n_entrantes_total": 991,
 "entrantes": [
  {
   "relation": "aplica_a",
   "vecino_id": "Restriccion_las_restantes_entidades_deberan_mantener_una_exigencia_basica_de_capital_minimo_",
   "vecino_label": "Exigencia básica restantes entidades",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 1.2. Exigencia básica."
    }
   ]
  },
  {
   "relation": "aplica_a",
   "vecino_id": "Obligacion_calcular_responsabilidad_patrimonial_computable",
   "vecino_label": "Calcular responsabilidad patrimonial computable",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 1.3. Integración."
    }
   ]
  },
  {
   "relation": "aplica_a",
   "vecino_id": "Obligacion_determinar_integracion_por_riesgo_de_mercado",
   "vecino_label": "Determinar integración por riesgo de mercado",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 1.3. Integración."
    }
   ]
  },
  {
   "relation": "aplica_a",
   "vecino_id": "Obligacion_informar_ecai_elegidas",
   "vecino_label": "Informar ECAI elegidas",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 10.1. Disposiciones generales."
    }
   ]
  },
  {
   "relation": "aplica_a",
   "vecino_id": "Obligacion_establecer_correspondencia_entre_calificaciones_y_ponderadores",
   "vecino_label": "Establecer correspondencia entre calificaciones y ponderadores",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 10.3. Consideraciones para su implementación."
    }
   ]
  },
  {
   "relation": "aplica_a",
   "vecino_id": "Obligacion_informar_ecai_utilizadas_y_ponderadores",
   "vecino_label": "Informar ECAI utilizadas y ponderadores",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 10.3. Consideraciones para su implementación."
    }
   ]
  },
  {
   "relation": "aplica_a",
   "vecino_id": "Obligacion_usar_ecai_en_forma_consistente",
   "vecino_label": "Usar ECAI en forma consistente",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 10.3. Consideraciones para su implementación."
    }
   ]
  },
  {
   "relation": "aplica_a",
   "vecino_id": "Restriccion_prohibicion_de_cherry_picking_de_ecai",
   "vecino_label": "Prohibición de cherry-picking de ECAI",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 10.3. Consideraciones para su implementación."
    }
   ]
  },
  {
   "relation": "aplica_a",
   "vecino_id": "Restriccion_distribucion_coherente_de_ponderadores",
   "vecino_label": "Distribución coherente de ponderadores",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 10.3. Consideraciones para su implementación."
    }
   ]
  },
  {
   "relation": "aplica_a",
   "vecino_id": "Restriccion_objetivo_en_asignacion_de_calificaciones",
   "vecino_label": "Objetivo en asignación de calificaciones",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 10.3. Consideraciones para su implementación."
    }
   ]
  },
  {
   "relation": "aplica_a",
   "vecino_id": "Restriccion_ponderador_por_calificacion_unica",
   "vecino_label": "Ponderador por calificación única",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 10.3. Consideraciones para su implementación."
    }
   ]
  },
  {
   "relation": "aplica_a",
   "vecino_id": "Restriccion_ponderador_superior_con_dos_calificaciones",
   "vecino_label": "Ponderador superior con dos calificaciones",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 10.3. Consideraciones para su implementación."
    }
   ]
  },
  {
   "relation": "aplica_a",
   "vecino_id": "Restriccion_dos_menores_ponderadores_con_multiples_calificaciones",
   "vecino_label": "Dos menores ponderadores con múltiples calificaciones",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 10.3. Consideraciones para su implementación."
    }
   ]
  },
  {
   "relation": "aplica_a",
   "vecino_id": "Restriccion_restriccion_de_uso_de_calificacion_de_emisor_a_creditos_quirografarios",
   "vecino_label": "Restricción de uso de calificación de emisor a créditos quirografarios",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 10.3. Consideraciones para su implementación."
    }
   ]
  },
  {
   "relation": "aplica_a",
   "vecino_id": "Restriccion_restriccion_de_calificacion_senior_o_equivalente",
   "vecino_label": "Restricción de calificación senior o equivalente",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 10.3. Consideraciones para su implementación."
    }
   ]
  },
  {
   "relation": "aplica_a",
   "vecino_id": "Restriccion_prohibicion_doble_computo_de_mejoras_crediticias",
   "vecino_label": "Prohibición doble cómputo de mejoras crediticias",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 10.3. Consideraciones para su implementación."
    }
   ]
  },
  {
   "relation": "aplica_a",
   "vecino_id": "Restriccion_calificaciones_en_moneda_extranjera_para_exposiciones_en_me",
   "vecino_label": "Calificaciones en moneda extranjera para exposiciones en ME",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 10.3. Consideraciones para su implementación."
    }
   ]
  },
  {
   "relation": "aplica_a",
   "vecino_id": "Restriccion_prohibicion_de_uso_de_evaluaciones_entre_entidades_del_grupo",
   "vecino_label": "Prohibición de uso de evaluaciones entre entidades del grupo",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 10.3. Consideraciones para su implementación."
    }
   ]
  },
  {
   "relation": "aplica_a",
   "vecino_id": "Obligacion_computar_diferencia_positiva_de_prevision",
   "vecino_label": "Computar diferencia positiva de previsión",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 11.4. A los efectos de la determinación de la RPC, las entidades financieras podrán co"
    }
   ]
  },
  {
   "relation": "aplica_a",
   "vecino_id": "Restriccion_las_entidades_financieras_en_funcionamiento_al_01_06_24_deberan_observar_la_exig",
   "vecino_label": "Exigencia básica capital desde 01/01/25",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 12.1. Las entidades financieras en funcionamiento al 01/06/24 deberán observar la exig"
    }
   ]
  },
  {
   "relation": "aplica_a",
   "vecino_id": "Obligacion_las_entidades_financieras_en_funcionamiento_al_01_06_24_que_no_cumplan_con_la_in",
   "vecino_label": "Presentar programa de encuadramiento",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 12.1. Las entidades financieras en funcionamiento al 01/06/24 deberán observar la exig"
    }
   ]
  },
  {
   "relation": "aplica_a",
   "vecino_id": "Obligacion_el_programa_de_encuadramiento_no_debera_superar_los_6_meses_de_plazo_para_cumpli",
   "vecino_label": "Cumplimiento de exigencia en plazo máximo",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 12.1. Las entidades financieras en funcionamiento al 01/06/24 deberán observar la exig"
    }
   ]
  },
  {
   "relation": "aplica_a",
   "vecino_id": "Restriccion_aplicacion_de_ccf_del_0_desde_01_01_25_al_30_06_25_y_del_5_desde_01_07_25_al_31_",
   "vecino_label": "Aplicación de CCF por período",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 12.2. Desde el 01/01/25 y hasta el 31/12/25, las entidades financieras clasificadas en"
    }
   ]
  },
  {
   "relation": "aplica_a",
   "vecino_id": "Obligacion_convertir_compromisos_en_equivalentes",
   "vecino_label": "Convertir compromisos en equivalentes",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 12.2. Desde el 01/01/25 y hasta el 31/12/25, las entidades financieras clasificadas en"
    }
   ]
  },
  {
   "relation": "aplica_a",
   "vecino_id": "Obligacion_determinacion_de_nocional_efectivo",
   "vecino_label": "Determinación de nocional efectivo",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 1. Todos los derivados de crédito que hagan referencia a una misma enti-"
    }
   ]
  },
  {
   "relation": "aplica_a",
   "vecino_id": "Obligacion_calculo_de_factor_sf_regulatorio",
   "vecino_label": "Cálculo de factor SF regulatorio",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 1. Todos los derivados de crédito que hagan referencia a una misma enti-"
    }
   ]
  },
  {
   "relation": "aplica_a",
   "vecino_id": "Restriccion_las_contrapartes_individuales_cuyo_saldo_de_exposiciones_computables_a_fin_del_m",
   "vecino_label": "Límite de exposición a contraparte minorista",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 2.10. A los fines de calcular el límite definido en el párrafo precedente, se aplicará"
    }
   ]
  },
  {
   "relation": "aplica_a",
   "vecino_id": "Restriccion_la_exposicion_maxima_frente_a_una_misma_contraparte_individual_no_debera_superar",
   "vecino_label": "Límite máximo exposición personas humanas consumo",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 2.10. A los fines de calcular el límite definido en el párrafo precedente, se aplicará"
    }
   ]
  },
  {
   "relation": "aplica_a",
   "vecino_id": "Restriccion_la_exposicion_maxima_frente_a_una_misma_contraparte_individual_mipyme_no_debera_",
   "vecino_label": "Límite máximo exposición Mipyme",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 2.10. A los fines de calcular el límite definido en el párrafo precedente, se aplicará"
    }
   ]
  },
  {
   "relation": "aplica_a",
   "vecino_id": "Restriccion_el_total_de_los_vencimientos_por_las_cuotas_de_todas_las_financiaciones_de_la_en",
   "vecino_label": "Límite cuota-ingreso financiaciones",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 2.10. A los fines de calcular el límite definido en el párrafo precedente, se aplicará"
    }
   ]
  },
  {
   "relation": "aplica_a",
   "vecino_id": "Restriccion_se_aplicara_el_ponderador_de_riesgo_del_75_para_las_exposiciones_a_personas_huma",
   "vecino_label": "Ponderador riesgo personas humanas",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 2.12. Tabla de ponderadores de riesgo. (parte 2)"
    }
   ]
  },
  {
   "relation": "aplica_a",
   "vecino_id": "Restriccion_se_aplicara_el_ponderador_de_riesgo_del_85_para_las_exposiciones_a_mipyme",
   "vecino_label": "Ponderador riesgo MIPYME",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 2.12. Tabla de ponderadores de riesgo. (parte 2)"
    }
   ]
  },
  {
   "relation": "aplica_a",
   "vecino_id": "Restriccion_exposiciones_en_situacion_de_incumplimiento_con_garantia_hipotecaria_normativas_",
   "vecino_label": "Ponderador exposiciones incumplimiento hipotecario",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 2.12. Tabla de ponderadores de riesgo. (parte 2)"
    }
   ]
  },
  {
   "relation": "aplica_a",
   "vecino_id": "Restriccion_exposiciones_o_tramos_no_cubiertos_por_coberturas_del_riesgo_de_credito_con_prev",
   "vecino_label": "Ponderador exposiciones sin cobertura previsión menor 20%",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 2.12. Tabla de ponderadores de riesgo. (parte 2)"
    }
   ]
  },
  {
   "relation": "aplica_a",
   "vecino_id": "Restriccion_con_previsiones_especificas_iguales_o_mayores_al_20_y_menores_al_50_del_saldo_pe",
   "vecino_label": "Ponderador exposiciones sin cobertura previsión 20-50%",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 2.12. Tabla de ponderadores de riesgo. (parte 2)"
    }
   ]
  },
  {
   "relation": "aplica_a",
   "vecino_id": "Restriccion_con_previsiones_especificas_iguales_o_mayores_al_50_del_saldo_pendiente_50",
   "vecino_label": "Ponderador exposiciones sin cobertura previsión mayor 50%",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 2.12. Tabla de ponderadores de riesgo. (parte 2)"
    }
   ]
  },
  {
   "relation": "aplica_a",
   "vecino_id": "Restriccion_exposiciones_a_instrumentos_deuda_subordinada_e_instrumentos_de_capital_que_no_r",
   "vecino_label": "Ponderador deuda subordinada grupo 1",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 2.12. Tabla de ponderadores de riesgo. (parte 2)"
    }
   ]
  },
  {
   "relation": "aplica_a",
   "vecino_id": "Restriccion_acciones_definidas_conforme_al_punto_2_11_3_250",
   "vecino_label": "Ponderador acciones grupo 1",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 2.12. Tabla de ponderadores de riesgo. (parte 2)"
    }
   ]
  },
  {
   "relation": "aplica_a",
   "vecino_id": "Restriccion_exposiciones_a_instrumentos_por_parte_de_entidades_financieras_del_grupo_2_deuda",
   "vecino_label": "Ponderador deuda subordinada grupo 2",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 2.12. Tabla de ponderadores de riesgo. (parte 2)"
    }
   ]
  },
  {
   "relation": "aplica_a",
   "vecino_id": "Restriccion_participaciones_en_el_capital_250",
   "vecino_label": "Ponderador participaciones capital grupo 2",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 2.12. Tabla de ponderadores de riesgo. (parte 2)"
    }
   ]
  }
 ],
 "entrantes_truncado": true
}
```

### paso 14 — buscar_nodos {"consulta": "deudor cedido usuario aunque no notificado", "limite": 10}

```json
{
 "consulta": "deudor cedido usuario aunque no notificado",
 "total_con_match": 429,
 "resultados": [
  {
   "id": "Obligacion_el_usuario_de_servicios_financieros_debe_ser_notificado_de_las_modificaciones_qu",
   "type": "Obligacion",
   "label": "Notificar cambios de condiciones",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El usuario de servicios financieros debe ser notificado de las modificaciones que aplicará el sujeto obligado con una antelación mínima de sesenta (60) días cor…"
  },
  {
   "id": "Restriccion_el_cargo_que_el_sujeto_obligado_aplique_al_usuario_no_podra_ser_superior_al_que_",
   "type": "Restriccion",
   "label": "Límite de cargo por seguro accesorio",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El cargo que el sujeto obligado aplique al usuario no podrá ser superior al que la compañía de seguros elegida perciba por operaciones con particulares y sin la…"
  },
  {
   "id": "Restriccion_entidades_que_han_notificado_al_bcra_que_optaron_por_no_operar_en_comercio_exter",
   "type": "Restriccion",
   "label": "Exclusión de entidades sin operatoria",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Serán elegibles todas las entidades financieras y casas de cambio salvo aquellas que hayan notificado al BCRA que han optado por no operar en comercio exterior."
  },
  {
   "id": "Restriccion_el_premio_que_el_sujeto_obligado_reciba_del_usuario_no_podra_ser_superior_al_imp",
   "type": "Restriccion",
   "label": "Límite de premio por seguro no accesorio",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El premio que el sujeto obligado reciba del usuario no podrá ser superior al importe que la compañía de seguros elegida perciba por operaciones con particulares…"
  },
  {
   "id": "Restriccion_los_derechos_y_o_facultades_reconocidos_al_usuario_por_estas_normas_no_pueden_en",
   "type": "Restriccion",
   "label": "Irrenunciabilidad de derechos del usuario",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Los derechos y/o facultades reconocidos al usuario por estas normas no pueden en ningún caso ser dispensados ni renunciados"
  },
  {
   "id": "Restriccion_cuotas_de_financiaciones_no_deben_exceder_del_30_de_ingresos_del_deudor_al_momen",
   "type": "Restriccion",
   "label": "Límite cuota financiaciones sector público",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Cuotas de financiaciones no deben exceder del 30% de ingresos del deudor al momento de acuerdos"
  },
  {
   "id": "Restriccion_en_ningun_caso_podran_aplicarse_comisiones_y_o_cargos_al_usuario_por_servicios_f",
   "type": "Restriccion",
   "label": "Prohibición de comisiones por servicios no solicitados",
   "tokens_matcheados": 2,
   "resumen_propiedades": "En ningún caso podrán aplicarse comisiones y/o cargos al usuario por servicios financieros que no hayan sido solicitados, pactados y/o autorizados por él y, aun…"
  },
  {
   "id": "EntidadFinanciera_deudor",
   "type": "EntidadFinanciera",
   "label": "Deudores",
   "tokens_matcheados": 1,
   "resumen_propiedades": "categoria: deudor"
  },
  {
   "id": "EntidadFinanciera_no_residente",
   "type": "EntidadFinanciera",
   "label": "No residentes",
   "tokens_matcheados": 1,
   "resumen_propiedades": "categoria: clientes no residentes"
  },
  {
   "id": "Excepcion_importador_demuestra_gestion_de_cobro_a_traves_de_reclamos_a_companias_de_seguro",
   "type": "Excepcion",
   "label": "Deudor moroso",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Importador demuestra gestión de cobro a través de reclamos a compañías de seguro de crédito o agencias de recupero, o mantiene acciones judiciales contra el pro…"
  }
 ]
}
```

### paso 15 — buscar_nodos {"consulta": "sujetos obligados protección usuarios punto 1.1 partes", "limite": 10}

```json
{
 "consulta": "sujetos obligados protección usuarios punto 1.1 partes",
 "total_con_match": 145,
 "resultados": [
  {
   "id": "Obligacion_los_sujetos_obligados_enumerados_en_el_punto_1_1_2_en_la_medida_en_que_correspon",
   "type": "Obligacion",
   "label": "Cobertura mínima de cajeros accesibles",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Los sujetos obligados enumerados en el punto 1.1.2., en la medida en que corresponda, deberán alcanzar la cobertura del servicio con esos cajeros automáticos en…"
  },
  {
   "id": "Obligacion_los_sujetos_obligados_deberan_adoptar_las_acciones_necesarias_para_garantizar_de",
   "type": "Obligacion",
   "label": "Garantizar derechos de usuarios",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Los sujetos obligados deberán adoptar las acciones necesarias para garantizar derechos de protección de seguridad e intereses económicos, información clara y ve…"
  },
  {
   "id": "Obligacion_los_sujetos_obligados_deberan_ofrecer_a_los_usuarios_de_servicios_financieros_po",
   "type": "Obligacion",
   "label": "Ofrecer mínimo tres compañías aseguradoras",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Los sujetos obligados deberán ofrecer a los usuarios de servicios financieros por lo menos tres compañías aseguradoras no vinculadas entre sí entre las que debe…"
  },
  {
   "id": "Restriccion_los_sujetos_obligados_no_podran_percibir_de_los_usuarios_ningun_tipo_de_comision",
   "type": "Restriccion",
   "label": "Prohibición de comisiones por seguros vida",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Los sujetos obligados no podrán percibir de los usuarios ningún tipo de comisión y/o cargo vinculado con seguros de vida sobre saldo deudor"
  },
  {
   "id": "Obligacion_los_sujetos_obligados_deberan_asegurar_a_los_usuarios_condiciones_igualitarias_d",
   "type": "Obligacion",
   "label": "Asegurar condiciones igualitarias de acceso",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Los sujetos obligados deberán asegurar a los usuarios condiciones igualitarias de acceso a los servicios que ofrecen y prestan"
  },
  {
   "id": "Restriccion_los_sujetos_obligados_no_podran_percibir_de_los_usuarios_ningun_tipo_de_retribuc",
   "type": "Restriccion",
   "label": "Prohibición de retribuciones por seguros no accesorios",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Los sujetos obligados no podrán percibir de los usuarios ningún tipo de retribución –comisión y/o cargo– adicional al premio determinado por la aseguradora, vin…"
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
   "id": "Excepcion_con_excepcion_de_los_casos_contemplados_en_el_punto_4_1",
   "type": "Excepcion",
   "label": "Excepción casos punto 4.1",
   "tokens_matcheados": 2,
   "resumen_propiedades": "con excepción de los casos contemplados en el punto 4.1"
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

### paso 16 — buscar_nodos {"consulta": "deudor usuario cartera cedida aunque no notificado", "limite": 10}

```json
{
 "consulta": "deudor usuario cartera cedida aunque no notificado",
 "total_con_match": 459,
 "resultados": [
  {
   "id": "EntidadFinanciera_deudor_cartera_comercial",
   "type": "EntidadFinanciera",
   "label": "Deudores cartera comercial",
   "tokens_matcheados": 2,
   "resumen_propiedades": "categoria: deudor cartera comercial"
  },
  {
   "id": "Restriccion_el_valor_de_mercado_de_la_totalidad_de_las_opciones_en_cartera_no_podra_superar_",
   "type": "Restriccion",
   "label": "Límite valor opciones compradas",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El valor de mercado de la totalidad de las opciones en cartera no podrá superar el 5% de su RPC del mes anterior"
  },
  {
   "id": "Obligacion_el_usuario_de_servicios_financieros_debe_ser_notificado_de_las_modificaciones_qu",
   "type": "Obligacion",
   "label": "Notificar cambios de condiciones",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El usuario de servicios financieros debe ser notificado de las modificaciones que aplicará el sujeto obligado con una antelación mínima de sesenta (60) días cor…"
  },
  {
   "id": "Restriccion_no_se_incluiran_posiciones_en_acciones_en_la_cartera_de_inversion",
   "type": "Restriccion",
   "label": "Exclusión de posiciones en acciones",
   "tokens_matcheados": 2,
   "resumen_propiedades": "No se incluirán posiciones en acciones en la cartera de inversión"
  },
  {
   "id": "Restriccion_el_cargo_que_el_sujeto_obligado_aplique_al_usuario_no_podra_ser_superior_al_que_",
   "type": "Restriccion",
   "label": "Límite de cargo por seguro accesorio",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El cargo que el sujeto obligado aplique al usuario no podrá ser superior al que la compañía de seguros elegida perciba por operaciones con particulares y sin la…"
  },
  {
   "id": "Restriccion_entidades_que_han_notificado_al_bcra_que_optaron_por_no_operar_en_comercio_exter",
   "type": "Restriccion",
   "label": "Exclusión de entidades sin operatoria",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Serán elegibles todas las entidades financieras y casas de cambio salvo aquellas que hayan notificado al BCRA que han optado por no operar en comercio exterior."
  },
  {
   "id": "Obligacion_al_cierre_del_primer_semestre_calendario_el_examen_debera_haber_alcanzado_no_men",
   "type": "Obligacion",
   "label": "Cobertura mínima 50% cartera semestral",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Al cierre del primer semestre calendario, el examen deberá haber alcanzado no menos del 50% del importe total de la cartera comercial comprendida"
  },
  {
   "id": "Restriccion_el_premio_que_el_sujeto_obligado_reciba_del_usuario_no_podra_ser_superior_al_imp",
   "type": "Restriccion",
   "label": "Límite de premio por seguro no accesorio",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El premio que el sujeto obligado reciba del usuario no podrá ser superior al importe que la compañía de seguros elegida perciba por operaciones con particulares…"
  },
  {
   "id": "Restriccion_los_derechos_y_o_facultades_reconocidos_al_usuario_por_estas_normas_no_pueden_en",
   "type": "Restriccion",
   "label": "Irrenunciabilidad de derechos del usuario",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Los derechos y/o facultades reconocidos al usuario por estas normas no pueden en ningún caso ser dispensados ni renunciados"
  },
  {
   "id": "Restriccion_cuotas_de_financiaciones_no_deben_exceder_del_30_de_ingresos_del_deudor_al_momen",
   "type": "Restriccion",
   "label": "Límite cuota financiaciones sector público",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Cuotas de financiaciones no deben exceder del 30% de ingresos del deudor al momento de acuerdos"
  }
 ]
}
```



---

# CQN2-011

## Respuesta final íntegra (trace.final_json)

```json
{
 "respuesta": "(a) No se encontró en el Knowledge Graph información específica sobre qué debe presentar una entidad financiera que proyecta no alcanzar la integración de la exigencia básica de capital, ante quién, en qué plazo y con qué duración máxima. Se identificó una obligación de presentar un plan de regularización y saneamiento dentro de los 30 días corridos siguientes al último día del mes al que corresponda el incumplimiento, pero no se cuenta con detalles completos sobre la duración máxima de ese plan ni la autoridad específica ante la cual presentarlo.\n\n(b) Respecto a la importación de aeronaves NCM 8802: (1) La posición arancelaria NCM 8802 (incluyendo sus subpartidas 8802.11.00, 8802.12.10, 8802.12.90, 8802.20.10, 8802.20.21, 8802.20.22, 8802.20.90, 8802.30.10, 8802.30.21, 8802.30.29, 8802.30.31, 8802.30.39, 8802.30.90, 8802.40.10, 8802.40.90) está sujeta a arancel. (2) Para operaciones embarcadas después del 14/04/25, existe una excepción que permite que el pago a la vista se concrete a partir de la fecha estimada de embarque más 15 días corridos cuando corresponde a porción de operación con pagos a la vista. Sin embargo, no se encontró en el grafo información específica sobre si esta excepción aplica a MiPyMe ni sobre la posibilidad de pagar a la vista con registro de ingreso aduanero pendiente para este tipo de bienes.",
 "citas": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Punto 12.1. Las entidades financieras en funcionamiento al 01/06/24 deberán observar la exigencia básica de capital"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 12.1. Posiciones arancelarias referidas en los puntos 10.10.2.1. y 10.10.2.2."
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 10.3. Pagos de importaciones de bienes que cuentan con registro de ingreso aduanero. (parte 2)"
  }
 ],
 "respondible": false
}
```

(`respondible`: false · tool_calls: 15 · hit_tool_limit: True)

## Inventario de pasos + fidelidad runtime↔re-ejecución

| paso | tool | input | output_chars (runtime) | re-ejecutado | fiel |
|---|---|---|---|---|---|
| 1 | buscar_nodos | `{"consulta": "integración exigencia básica capital plan", "limite": 10}` | 3322 | 3322 | SÍ |
| 2 | buscar_nodos | `{"consulta": "importación aeronave NCM 8802 pago a la vista", "limite": 10}` | 3385 | 3385 | SÍ |
| 3 | buscar_nodos | `{"consulta": "MiPyMe importación aeronave excepción", "limite": 10}` | 3326 | 3326 | SÍ |
| 4 | ver_nodo | `{"id": "Restriccion_las_entidades_financieras_en_funcionamiento_al_01_06_24_deberan_o` | 614 | 614 | SÍ |
| 5 | ver_nodo | `{"id": "Restriccion_posiciones_arancelarias_ncm_8802_11_00_8802_12_10_8802_12_90_8802` | 629 | 629 | SÍ |
| 6 | ver_nodo | `{"id": "Excepcion_pago_por_mipyme_con_condiciones_especificas"}` | 606 | 606 | SÍ |
| 7 | ver_vecinos | `{"id": "Restriccion_las_entidades_financieras_en_funcionamiento_al_01_06_24_deberan_o` | 1151 | 1151 | SÍ |
| 8 | ver_vecinos | `{"id": "Excepcion_pago_por_mipyme_con_condiciones_especificas", "direccion": "salient` | 584 | 584 | SÍ |
| 9 | buscar_nodos | `{"consulta": "plan integración capital no alcanzar plazo duración", "limite": 10}` | 3198 | 3198 | SÍ |
| 10 | buscar_nodos | `{"consulta": "plan integración capital BCRA presentar plazo máximo duración", "limite` | 3116 | 3116 | SÍ |
| 11 | buscar_nodos | `{"consulta": "aeronave NCM 8802 pago a la vista registro ingreso aduanero pendiente",` | 3641 | 3641 | SÍ |
| 12 | buscar_nodos | `{"consulta": "plan integración capital no alcanzar exigencia básica presentar", "limi` | 3400 | 3400 | SÍ |
| 13 | buscar_nodos | `{"consulta": "pago a la vista sin registro ingreso aduanero 14/04/25", "limite": 10}` | 3626 | 3626 | SÍ |
| 14 | ver_nodo | `{"id": "Excepcion_para_cartas_de_credito_o_letras_avaladas_emitidas_u_otorgadas_a_par` | 654 | 654 | SÍ |
| 15 | buscar_nodos | `{"consulta": "punto 12 plan integración capital BCRA presentar", "limite": 10}` | 3008 | 3008 | SÍ |

**Fidelidad: 15/15**.

## Apéndice — outputs completos re-ejecutados

### paso 1 — buscar_nodos {"consulta": "integración exigencia básica capital plan", "limite": 10}

```json
{
 "consulta": "integración exigencia básica capital plan",
 "total_con_match": 263,
 "resultados": [
  {
   "id": "Restriccion_los_bancos_deberan_mantener_una_exigencia_basica_de_capital_minimo_de_5_000_mill",
   "type": "Restriccion",
   "label": "Exigencia básica bancos",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Los bancos deberán mantener una exigencia básica de capital mínimo de 5.000 millones de pesos"
  },
  {
   "id": "Restriccion_las_restantes_entidades_deberan_mantener_una_exigencia_basica_de_capital_minimo_",
   "type": "Restriccion",
   "label": "Exigencia básica restantes entidades",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Las restantes entidades deberán mantener una exigencia básica de capital mínimo de 2.500 millones de pesos"
  },
  {
   "id": "Restriccion_las_entidades_financieras_en_funcionamiento_al_01_06_24_deberan_observar_la_exig",
   "type": "Restriccion",
   "label": "Exigencia básica capital desde 01/01/25",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Las entidades financieras en funcionamiento al 01/06/24 deberán observar la exigencia básica de capital prevista en la tabla del punto 1.2 según la categoría qu…"
  },
  {
   "id": "Operacion_observancia_de_exigencia_de_capital",
   "type": "Operacion",
   "label": "Observancia de exigencia básica de capital",
   "tokens_matcheados": 3,
   "resumen_propiedades": "tipo: observancia de exigencia de capital"
  },
  {
   "id": "Restriccion_desde_el_01_06_24_y_hasta_el_31_12_24_las_entidades_en_funcionamiento_deberan_ap",
   "type": "Restriccion",
   "label": "Exigencia básica de capital período transición",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Desde el 01/06/24 y hasta el 31/12/24 las entidades en funcionamiento deberán aplicar exigencias de capital de 1.500 millones de pesos para Bancos y 700 millone…"
  },
  {
   "id": "Operacion_integracion_de_capital",
   "type": "Operacion",
   "label": "Integración de capital",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La integración se determinará en forma diaria considerando la RPC del último día del mes anterior y el cambio de valor diario del portafolio de activos"
  },
  {
   "id": "Obligacion_se_determinara_mensualmente_la_exigencia_de_capital_por_riesgo_operacional_cro_m",
   "type": "Obligacion",
   "label": "Informar CRO mensualmente",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Se determinará mensualmente la exigencia de capital por riesgo operacional (CRO) mediante la expresión CRO = BIC x ILM para entidades del Grupo 1"
  },
  {
   "id": "Operacion_integracion_de_capital_minimo",
   "type": "Operacion",
   "label": "Integración de capital mínimo",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: integración de capital mínimo"
  },
  {
   "id": "Obligacion_aplicar_exigencia_capital_por_riesgo_general_mercado_a_todas_posiciones_derivado",
   "type": "Obligacion",
   "label": "Cálculo riesgo general mercado",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La exigencia de capital por el riesgo general de mercado alcanza a todas las posiciones en instrumentos derivados -de la misma manera que también alcanza a las …"
  },
  {
   "id": "Obligacion_observar_exigencia_capital_cva",
   "type": "Obligacion",
   "label": "Observar exigencia capital CVA",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Las entidades financieras deberán observar una exigencia de capital por el riesgo de pérdidas derivadas de valuar a precios de mercado el riesgo de contraparte …"
  }
 ]
}
```

### paso 2 — buscar_nodos {"consulta": "importación aeronave NCM 8802 pago a la vista", "limite": 10}

```json
{
 "consulta": "importación aeronave NCM 8802 pago a la vista",
 "total_con_match": 1700,
 "resultados": [
  {
   "id": "Operacion_pago_a_la_vista_contra_presentacion_de_documentacion",
   "type": "Operacion",
   "label": "Pago a la vista de importación",
   "tokens_matcheados": 5,
   "resumen_propiedades": "Pagos a la vista contra la presentación de la documentación de embarque"
  },
  {
   "id": "Operacion_pago_a_la_vista_de_importaciones_de_bienes",
   "type": "Operacion",
   "label": "Pago a la vista de importaciones",
   "tokens_matcheados": 4,
   "resumen_propiedades": "tipo: pago a la vista de importaciones de bienes"
  },
  {
   "id": "Obligacion_el_pago_garantizado_debia_ser_concretado_por_el_cliente_a_partir_de_la_fecha_que",
   "type": "Obligacion",
   "label": "Verificación de fecha de pago",
   "tokens_matcheados": 3,
   "resumen_propiedades": "El pago garantizado debía ser concretado por el cliente a partir de la fecha que resultaba de adicionar el plazo en días corridos que le corresponde al servicio…"
  },
  {
   "id": "Operacion_apertura_de_cuenta",
   "type": "Operacion",
   "label": "Apertura de cuenta a la vista",
   "tokens_matcheados": 3,
   "resumen_propiedades": "tipo: apertura de cuenta"
  },
  {
   "id": "Restriccion_la_suma_de_los_pagos_anticipados_a_la_vista_y_de_deuda_comercial_sin_registro_de",
   "type": "Restriccion",
   "label": "Límite de pagos totales al 80%",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La suma de los pagos anticipados, a la vista y de deuda comercial sin registro de ingreso aduanero cursados en el marco de este punto no supera el 80% (ochenta …"
  },
  {
   "id": "Obligacion_las_entidades_financieras_ante_requerimientos_de_apertura_de_cuentas_a_la_vista_",
   "type": "Obligacion",
   "label": "Ofrecer caja de ahorros en pesos",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Las entidades financieras, ante requerimientos de apertura de cuentas a la vista, deberán ofrecer la Caja de ahorros en pesos con las prestaciones previstas en …"
  },
  {
   "id": "Restriccion_posiciones_arancelarias_ncm_8802_11_00_8802_12_10_8802_12_90_8802_20_10_8802_20_",
   "type": "Restriccion",
   "label": "Arancel a importaciones de aeronaves",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Posiciones arancelarias NCM 8802.11.00, 8802.12.10, 8802.12.90, 8802.20.10, 8802.20.21, 8802.20.22, 8802.20.90, 8802.30.10, 8802.30.21, 8802.30.29, 8802.30.31, …"
  },
  {
   "id": "Obligacion_la_entidad_financiera_podra_en_todo_momento_y_a_su_entera_discrecion_cancelar_pa",
   "type": "Obligacion",
   "label": "Discrecionalidad en pago de dividendos",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La entidad financiera podrá –en todo momento y a su entera discreción– cancelar pagos en concepto de dividendos o intereses."
  },
  {
   "id": "Obligacion_la_operacion_financiada_correspondia_a_una_importacion_de_bienes_con_registro_de",
   "type": "Obligacion",
   "label": "Demostrar registro de ingreso aduanero",
   "tokens_matcheados": 3,
   "resumen_propiedades": "la operación financiada correspondía a una importación de bienes con registro de ingreso aduanero a partir del 13/12/23"
  },
  {
   "id": "Excepcion_pagar_a_la_fecha_de_cierre_de_la_operacion_de_recompra_y_o_rescate_sin_necesidad",
   "type": "Excepcion",
   "label": "Excepción para pago de gastos de emisión",
   "tokens_matcheados": 3,
   "resumen_propiedades": "pagar a la fecha de cierre de la operación de recompra y/o rescate, sin necesidad de que exista una liquidación de fondos por el monto equivalente, los gastos d…"
  }
 ]
}
```

### paso 3 — buscar_nodos {"consulta": "MiPyMe importación aeronave excepción", "limite": 10}

```json
{
 "consulta": "MiPyMe importación aeronave excepción",
 "total_con_match": 299,
 "resultados": [
  {
   "id": "Excepcion_pago_por_mipyme_con_condiciones_especificas",
   "type": "Excepcion",
   "label": "Pago por MiPyMe con condiciones específicas",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El pago es concretado por una persona humana o una persona jurídica que clasifique como MiPyMe según lo dispuesto en las normas de 'Determinación de la condició…"
  },
  {
   "id": "Excepcion_excepcion_fletes_de_importacion_desde_embarque",
   "type": "Excepcion",
   "label": "Excepción: fletes de importación desde embarque",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Para fletes de operación de importación encuadrada en punto 10.10.2.1., el pago podrá realizarse a partir del embarque de los bienes en origen"
  },
  {
   "id": "Excepcion_el_pago_es_concretado_a_partir_del_10_02_24_por_una_persona_humana_o_una_persona",
   "type": "Excepcion",
   "label": "Pago MiPyMe deudas importaciones anterior 13/12/23",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El pago es concretado a partir del 10/02/24 por una persona humana o una persona jurídica que clasifique como MiPyMe según lo dispuesto en las normas de 'Determ…"
  },
  {
   "id": "EntidadFinanciera_mipyme",
   "type": "EntidadFinanciera",
   "label": "Mipyme",
   "tokens_matcheados": 1,
   "resumen_propiedades": "categoria: micro, pequeña y mediana empresa"
  },
  {
   "id": "Excepcion_importador_demuestra_gestion_de_cobro_a_traves_de_reclamos_a_companias_de_seguro",
   "type": "Excepcion",
   "label": "Deudor moroso",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Importador demuestra gestión de cobro a través de reclamos a compañías de seguro de crédito o agencias de recupero, o mantiene acciones judiciales contra el pro…"
  },
  {
   "id": "Excepcion_no_aplica_si_el_cliente_es_un_vehiculo_de_proyecto_unico_vpu_adherido_al_rigi_qu",
   "type": "Excepcion",
   "label": "Excepción VPU RIGI",
   "tokens_matcheados": 1,
   "resumen_propiedades": "No aplica si el cliente es un Vehículo de Proyecto Único (VPU) adherido al RIGI que concreta el pago conforme punto 14.2.1"
  },
  {
   "id": "Excepcion_no_resultara_aplicable_cuando_el_cliente_es_un_vehiculo_de_proyecto_unico_vpu_ad",
   "type": "Excepcion",
   "label": "Excepción VPU RIGI",
   "tokens_matcheados": 1,
   "resumen_propiedades": "No resultará aplicable cuando el cliente es un Vehículo de Proyecto Único (VPU) adherido al Régimen de Incentivo para Grandes Inversiones (RIGI) que cancela cap…"
  },
  {
   "id": "Excepcion_exclusion_de_opciones",
   "type": "Excepcion",
   "label": "Exclusión de opciones",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Las opciones sobre acciones e índices bursátiles se excluyen del tratamiento de derivados sobre acciones, siendo tratadas en el punto 6.6"
  },
  {
   "id": "Excepcion_si_n_0_ningun_periodo_con_ib_positivo_debera_observarse_una_exigencia_equivalent",
   "type": "Excepcion",
   "label": "Excepción N=0 Grupo 2",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Si n = 0 (ningún período con IB positivo), deberá observarse una exigencia equivalente al límite previsto en el punto 7.3 de las normas sobre Capitales mínimos …"
  },
  {
   "id": "Operacion_importacion_de_bienes",
   "type": "Operacion",
   "label": "Importación de bienes",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Operación de ingreso aduanero de bienes importados que cuenta con el correspondiente registro ante ARCA"
  }
 ]
}
```

### paso 4 — ver_nodo {"id": "Restriccion_las_entidades_financieras_en_funcionamiento_al_01_06_24_deberan_observar_la_exig"}

```json
{
 "id": "Restriccion_las_entidades_financieras_en_funcionamiento_al_01_06_24_deberan_observar_la_exig",
 "type": "Restriccion",
 "label": "Exigencia básica capital desde 01/01/25",
 "properties": {
  "descripcion": "Las entidades financieras en funcionamiento al 01/06/24 deberán observar la exigencia básica de capital prevista en la tabla del punto 1.2 según la categoría que corresponda a partir del 01/01/25",
  "tipo": "limite_cuantitativo"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Punto 12.1. Las entidades financieras en funcionamiento al 01/06/24 deberán observar la exig"
  }
 ]
}
```

### paso 5 — ver_nodo {"id": "Restriccion_posiciones_arancelarias_ncm_8802_11_00_8802_12_10_8802_12_90_8802_20_10_8802_20_"}

```json
{
 "id": "Restriccion_posiciones_arancelarias_ncm_8802_11_00_8802_12_10_8802_12_90_8802_20_10_8802_20_",
 "type": "Restriccion",
 "label": "Arancel a importaciones de aeronaves",
 "properties": {
  "descripcion": "Posiciones arancelarias NCM 8802.11.00, 8802.12.10, 8802.12.90, 8802.20.10, 8802.20.21, 8802.20.22, 8802.20.90, 8802.30.10, 8802.30.21, 8802.30.29, 8802.30.31, 8802.30.39, 8802.30.90, 8802.40.10, 8802.40.90 sujetas a arancel",
  "tipo": "limite_cualitativo"
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 12.1. Posiciones arancelarias referidas en los puntos 10.10.2.1. y 10.10.2.2."
  }
 ]
}
```

### paso 6 — ver_nodo {"id": "Excepcion_pago_por_mipyme_con_condiciones_especificas"}

```json
{
 "id": "Excepcion_pago_por_mipyme_con_condiciones_especificas",
 "type": "Excepcion",
 "label": "Pago por MiPyMe con condiciones específicas",
 "properties": {
  "description": "El pago es concretado por una persona humana o una persona jurídica que clasifique como MiPyMe según lo dispuesto en las normas de 'Determinación de la condición de micro, pequeña y mediana empresa' y se cumple la totalidad de las condiciones establecidas"
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 10.11. Disposiciones complementarias para importaciones de bienes con registro de ingre"
  }
 ]
}
```

### paso 7 — ver_vecinos {"id": "Restriccion_las_entidades_financieras_en_funcionamiento_al_01_06_24_deberan_observar_la_exig", "direccion": "salientes"}

```json
{
 "id": "Restriccion_las_entidades_financieras_en_funcionamiento_al_01_06_24_deberan_observar_la_exig",
 "label": "Exigencia básica capital desde 01/01/25",
 "n_salientes_total": 3,
 "n_entrantes_total": 0,
 "salientes": [
  {
   "relation": "establecida_en",
   "vecino_id": "TextoOrdenado_to_capitales_minimos_actual_pdf",
   "vecino_label": "Capitales Mínimos",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 12.1. Las entidades financieras en funcionamiento al 01/06/24 deberán observar la exig"
    }
   ]
  },
  {
   "relation": "aplica_a",
   "vecino_id": "EntidadFinanciera_sujeto_obligado",
   "vecino_label": "Sujetos obligados",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 12.1. Las entidades financieras en funcionamiento al 01/06/24 deberán observar la exig"
    }
   ]
  },
  {
   "relation": "limita",
   "vecino_id": "Operacion_cumplimiento_de_capital",
   "vecino_label": "Cumplimiento integración capital mínimo",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 12.1. Las entidades financieras en funcionamiento al 01/06/24 deberán observar la exig"
    }
   ]
  }
 ],
 "salientes_truncado": false
}
```

### paso 8 — ver_vecinos {"id": "Excepcion_pago_por_mipyme_con_condiciones_especificas", "direccion": "salientes"}

```json
{
 "id": "Excepcion_pago_por_mipyme_con_condiciones_especificas",
 "label": "Pago por MiPyMe con condiciones específicas",
 "n_salientes_total": 1,
 "n_entrantes_total": 0,
 "salientes": [
  {
   "relation": "exceptua",
   "vecino_id": "Restriccion_conformidad_previa_del_bcra_para_acceso_al_mercado_de_cambios",
   "vecino_label": "Conformidad previa del BCRA para acceso al mercado de cambios",
   "provenances": [
    {
     "source_doc": "TO_exterior_cambios_actual.pdf",
     "location": "Punto 10.11. Disposiciones complementarias para importaciones de bienes con registro de ingre"
    }
   ]
  }
 ],
 "salientes_truncado": false
}
```

### paso 9 — buscar_nodos {"consulta": "plan integración capital no alcanzar plazo duración", "limite": 10}

```json
{
 "consulta": "plan integración capital no alcanzar plazo duración",
 "total_con_match": 612,
 "resultados": [
  {
   "id": "Excepcion_no_resultara_aplicable_cuando_se_cumpla_la_totalidad_de_las_siguientes_condicion",
   "type": "Excepcion",
   "label": "Excepción por Plan Gas",
   "tokens_matcheados": 2,
   "resumen_propiedades": "No resultará aplicable cuando se cumpla la totalidad de las siguientes condiciones: (1) el destino de los fondos haya sido la financiación de proyectos enmarcad…"
  },
  {
   "id": "Operacion_integracion_de_capital",
   "type": "Operacion",
   "label": "Integración de capital",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La integración se determinará en forma diaria considerando la RPC del último día del mes anterior y el cambio de valor diario del portafolio de activos"
  },
  {
   "id": "Restriccion_operaciones_comerciales_con_brasil_no_podran_tener_plazo_de_pago_que_exceda_360_",
   "type": "Restriccion",
   "label": "Límite plazo pago Brasil",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Operaciones comerciales con Brasil no podrán tener plazo de pago que exceda 360 días"
  },
  {
   "id": "Restriccion_el_monto_acumulado_de_las_repatriaciones_de_capital_del_no_residente_sea_menor_o",
   "type": "Restriccion",
   "label": "Límite repatriación capital",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El monto acumulado de las repatriaciones de capital del no residente sea menor o igual a la suma de los aportes de inversión directa ingresados por mercado de c…"
  },
  {
   "id": "Restriccion_plazo_de_vencimiento_original_no_inferior_a_cinco_anos",
   "type": "Restriccion",
   "label": "Plazo mínimo de vencimiento",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Plazo de vencimiento original no inferior a cinco años."
  },
  {
   "id": "Operacion_integracion_de_capital_minimo",
   "type": "Operacion",
   "label": "Integración de capital mínimo",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: integración de capital mínimo"
  },
  {
   "id": "Obligacion_informar_al_beneficiario_la_recepcion_de_los_fondos_en_un_plazo_no_mayor_a_un_di",
   "type": "Obligacion",
   "label": "Notificar acreditación de fondos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Informar al beneficiario la recepción de los fondos en un plazo no mayor a un día hábil siguiente de la fecha de acreditación"
  },
  {
   "id": "Restriccion_el_primer_pago_de_capital_no_se_registre_antes_de_los_3_tres_anos_de_la_fecha_de",
   "type": "Restriccion",
   "label": "Primer pago capital después 3 años",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El primer pago de capital no se registre antes de los 3 (tres) años de la fecha de emisión"
  },
  {
   "id": "Operacion_suscripcion_e_integracion_de_instrumentos_capital",
   "type": "Operacion",
   "label": "Suscripción de instrumentos capital",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: suscripción e integración de instrumentos capital"
  },
  {
   "id": "Restriccion_el_plazo_para_la_liquidacion_de_divisas_no_debe_ser_posterior_a_la_fecha_hasta_l",
   "type": "Restriccion",
   "label": "Plazo máximo liquidación de divisas",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El plazo para la liquidación de divisas no debe ser posterior a la fecha hasta la cual los cobros deben permanecer depositados según el contrato de financiamien…"
  }
 ]
}
```

### paso 10 — buscar_nodos {"consulta": "plan integración capital BCRA presentar plazo máximo duración", "limite": 10}

```json
{
 "consulta": "plan integración capital BCRA presentar plazo máximo duración",
 "total_con_match": 427,
 "resultados": [
  {
   "id": "Restriccion_el_usuario_puede_informar_al_bcra_si_transcurre_el_plazo_de_diez_10_dias_habiles",
   "type": "Restriccion",
   "label": "Plazo máximo de respuesta a reclamo",
   "tokens_matcheados": 3,
   "resumen_propiedades": "El usuario puede informar al BCRA si transcurre el plazo de diez (10) días hábiles desde el momento de haber presentado su reclamo sin haber recibido respuesta …"
  },
  {
   "id": "Operacion_integracion_de_capital",
   "type": "Operacion",
   "label": "Integración de capital",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La integración se determinará en forma diaria considerando la RPC del último día del mes anterior y el cambio de valor diario del portafolio de activos"
  },
  {
   "id": "Restriccion_plazo_maximo_liquidacion",
   "type": "Restriccion",
   "label": "Plazo máximo liquidación",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La liquidación en el mercado de cambios deberá realizarse dentro de los 20 (veinte) días hábiles de la fecha de percepción en el exterior o en el país o de su a…"
  },
  {
   "id": "Restriccion_no_se_pueden_cobrar_comisiones_en_exceso_de_las_maximas_fijadas_por_el_bcra",
   "type": "Restriccion",
   "label": "Límite máximo de comisiones",
   "tokens_matcheados": 2,
   "resumen_propiedades": "No se pueden cobrar comisiones en exceso de las máximas fijadas por el BCRA"
  },
  {
   "id": "Operacion_integracion_de_capital_minimo",
   "type": "Operacion",
   "label": "Integración de capital mínimo",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: integración de capital mínimo"
  },
  {
   "id": "Restriccion_hasta_cinco_prorrogas_sucesivas_de_hasta_180_dias_corridos",
   "type": "Restriccion",
   "label": "Plazo máximo gestión de cobro",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Hasta cinco prórrogas sucesivas de hasta 180 días corridos"
  },
  {
   "id": "Operacion_suscripcion_e_integracion_de_instrumentos_capital",
   "type": "Operacion",
   "label": "Suscripción de instrumentos capital",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: suscripción e integración de instrumentos capital"
  },
  {
   "id": "Restriccion_el_plazo_para_la_liquidacion_de_divisas_no_debe_ser_posterior_a_la_fecha_hasta_l",
   "type": "Restriccion",
   "label": "Plazo máximo liquidación de divisas",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El plazo para la liquidación de divisas no debe ser posterior a la fecha hasta la cual los cobros deben permanecer depositados según el contrato de financiamien…"
  },
  {
   "id": "Restriccion_plazo_maximo_de_liquidacion_contado",
   "type": "Restriccion",
   "label": "Plazo máximo de liquidación contado",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La liquidación por parte de ambas partes está pactada dentro de un plazo de hasta 2 (dos) días hábiles desde la fecha de su concertación"
  },
  {
   "id": "Obligacion_integracion_de_capital_por_posiciones",
   "type": "Obligacion",
   "label": "Integración de capital por posiciones",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La entidad deberá integrar capital por las posiciones de titulización que conserve vinculadas con dicha operación"
  }
 ]
}
```

### paso 11 — buscar_nodos {"consulta": "aeronave NCM 8802 pago a la vista registro ingreso aduanero pendiente", "limite": 10}

```json
{
 "consulta": "aeronave NCM 8802 pago a la vista registro ingreso aduanero pendiente",
 "total_con_match": 1774,
 "resultados": [
  {
   "id": "Obligacion_la_operacion_financiada_correspondia_a_una_importacion_de_bienes_con_registro_de",
   "type": "Obligacion",
   "label": "Demostrar registro de ingreso aduanero",
   "tokens_matcheados": 5,
   "resumen_propiedades": "la operación financiada correspondía a una importación de bienes con registro de ingreso aduanero a partir del 13/12/23"
  },
  {
   "id": "Obligacion_la_entidad_a_cargo_del_seguimiento_de_los_pagos_con_registro_de_ingreso_aduanero",
   "type": "Obligacion",
   "label": "Denuncia de incumplimiento en regularización",
   "tokens_matcheados": 5,
   "resumen_propiedades": "La entidad a cargo del seguimiento de los pagos con registro de ingreso aduanero pendiente deberá, dentro de los 5 (cinco) días hábiles siguientes a la fecha de…"
  },
  {
   "id": "Restriccion_el_cliente_se_compromete_a_demostrar_el_registro_de_ingreso_aduanero_de_los_bien",
   "type": "Restriccion",
   "label": "Límite temporal de 90 días",
   "tokens_matcheados": 4,
   "resumen_propiedades": "El cliente se compromete a demostrar el registro de ingreso aduanero de los bienes dentro de los 90 (noventa) días corridos de la fecha de acceso al mercado de …"
  },
  {
   "id": "Operacion_pago_a_la_vista_contra_presentacion_de_documentacion",
   "type": "Operacion",
   "label": "Pago a la vista de importación",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Pagos a la vista contra la presentación de la documentación de embarque"
  },
  {
   "id": "Restriccion_la_suma_de_los_pagos_anticipados_a_la_vista_y_de_deuda_comercial_sin_registro_de",
   "type": "Restriccion",
   "label": "Límite de pagos totales al 80%",
   "tokens_matcheados": 4,
   "resumen_propiedades": "La suma de los pagos anticipados, a la vista y de deuda comercial sin registro de ingreso aduanero cursados en el marco de este punto no supera el 80% (ochenta …"
  },
  {
   "id": "Operacion_pago_a_la_vista_de_importaciones_de_bienes",
   "type": "Operacion",
   "label": "Pago a la vista de importaciones",
   "tokens_matcheados": 4,
   "resumen_propiedades": "tipo: pago a la vista de importaciones de bienes"
  },
  {
   "id": "Restriccion_pago_de_deudas_comerciales_por_importaciones_de_bienes_con_registro_de_ingreso_a",
   "type": "Restriccion",
   "label": "Deudas elegibles hasta fecha límite",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Pago de deudas comerciales por importaciones de bienes con registro de ingreso aduanero hasta el 12/12/23, que resultaban elegibles"
  },
  {
   "id": "Obligacion_cuenta_con_la_declaracion_jurada_del_cliente_de_que_se_compromete_a_demostrar_el",
   "type": "Obligacion",
   "label": "Declaración jurada de ingreso aduanero",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Cuenta con la declaración jurada del cliente de que se compromete a demostrar el registro de ingreso aduanero de los bienes dentro de los 90 (noventa) días corr…"
  },
  {
   "id": "Excepcion_demoras_en_registro_de_ingreso_aduanero_por_causales_ajenas_a_voluntad_del_impor",
   "type": "Excepcion",
   "label": "Causales ajenas a decisión del importador",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Demoras en registro de ingreso aduanero por causales ajenas a voluntad del importador como problemas de producción, embarque, transporte u obtención de certific…"
  },
  {
   "id": "Obligacion_reemplazando_el_requisito_de_registro_de_ingreso_aduanero_por_la_demostracion_de",
   "type": "Obligacion",
   "label": "Demostración sometimiento régimen aduanero",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Reemplazando el requisito de registro de ingreso aduanero por la demostración del sometimiento de los bienes abonados al régimen aduanero que corresponda por su…"
  }
 ]
}
```

### paso 12 — buscar_nodos {"consulta": "plan integración capital no alcanzar exigencia básica presentar", "limite": 10}

```json
{
 "consulta": "plan integración capital no alcanzar exigencia básica presentar",
 "total_con_match": 620,
 "resultados": [
  {
   "id": "Restriccion_los_bancos_deberan_mantener_una_exigencia_basica_de_capital_minimo_de_5_000_mill",
   "type": "Restriccion",
   "label": "Exigencia básica bancos",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Los bancos deberán mantener una exigencia básica de capital mínimo de 5.000 millones de pesos"
  },
  {
   "id": "Restriccion_las_restantes_entidades_deberan_mantener_una_exigencia_basica_de_capital_minimo_",
   "type": "Restriccion",
   "label": "Exigencia básica restantes entidades",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Las restantes entidades deberán mantener una exigencia básica de capital mínimo de 2.500 millones de pesos"
  },
  {
   "id": "Restriccion_las_entidades_financieras_en_funcionamiento_al_01_06_24_deberan_observar_la_exig",
   "type": "Restriccion",
   "label": "Exigencia básica capital desde 01/01/25",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Las entidades financieras en funcionamiento al 01/06/24 deberán observar la exigencia básica de capital prevista en la tabla del punto 1.2 según la categoría qu…"
  },
  {
   "id": "Restriccion_la_presencia_de_una_opcion_de_exclusion_no_originara_exigencia_de_capital_alguna",
   "type": "Restriccion",
   "label": "Opción de exclusión sin exigencia capital",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La presencia de una opción de exclusión no originará exigencia de capital alguna siempre que se cumpla con la totalidad de los requisitos especificados"
  },
  {
   "id": "Operacion_observancia_de_exigencia_de_capital",
   "type": "Operacion",
   "label": "Observancia de exigencia básica de capital",
   "tokens_matcheados": 3,
   "resumen_propiedades": "tipo: observancia de exigencia de capital"
  },
  {
   "id": "Restriccion_la_exigencia_maxima_de_capital_para_las_entidades_financieras_originantes_no_ser",
   "type": "Restriccion",
   "label": "Exclusión retitulizaciones exigencia máxima",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La exigencia máxima de capital para las entidades financieras originantes no será de aplicación para el caso de retitulizaciones"
  },
  {
   "id": "Restriccion_desde_el_01_06_24_y_hasta_el_31_12_24_las_entidades_en_funcionamiento_deberan_ap",
   "type": "Restriccion",
   "label": "Exigencia básica de capital período transición",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Desde el 01/06/24 y hasta el 31/12/24 las entidades en funcionamiento deberán aplicar exigencias de capital de 1.500 millones de pesos para Bancos y 700 millone…"
  },
  {
   "id": "Restriccion_exigencia_capital_sector_privado_no_financiero",
   "type": "Restriccion",
   "label": "Exigencia capital sector privado no financiero",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Sector privado no financiero. Demás: 12%"
  },
  {
   "id": "Restriccion_exigencia_capital_sector_publico_no_financiero_demas",
   "type": "Restriccion",
   "label": "Exigencia capital sector público no financiero demás",
   "tokens_matcheados": 3,
   "resumen_propiedades": "BCRA y sector público no financiero. Demás: 8%"
  },
  {
   "id": "Restriccion_exigencia_capital_bcra_y_sector_publico_no_financiero",
   "type": "Restriccion",
   "label": "Exigencia capital BCRA y sector público no financiero",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Para BCRA, Gobierno Nacional, gobiernos provinciales, municipales y de la CABA en pesos, cuando su fuente de fondos sea en esa moneda: 0,25% plazo residual ≤ 6 …"
  }
 ]
}
```

### paso 13 — buscar_nodos {"consulta": "pago a la vista sin registro ingreso aduanero 14/04/25", "limite": 10}

```json
{
 "consulta": "pago a la vista sin registro ingreso aduanero 14/04/25",
 "total_con_match": 1815,
 "resultados": [
  {
   "id": "Excepcion_para_cartas_de_credito_o_letras_avaladas_emitidas_u_otorgadas_a_partir_del_14_04",
   "type": "Excepcion",
   "label": "Excepción por pagos a la vista desde 14/04/25",
   "tokens_matcheados": 6,
   "resumen_propiedades": "Para cartas de crédito o letras avaladas emitidas u otorgadas a partir del 14/04/25, también se admitirá que el pago se concretara a partir de la fecha estimada…"
  },
  {
   "id": "Restriccion_la_suma_de_los_pagos_anticipados_a_la_vista_y_de_deuda_comercial_sin_registro_de",
   "type": "Restriccion",
   "label": "Límite de pagos totales al 80%",
   "tokens_matcheados": 5,
   "resumen_propiedades": "La suma de los pagos anticipados, a la vista y de deuda comercial sin registro de ingreso aduanero cursados en el marco de este punto no supera el 80% (ochenta …"
  },
  {
   "id": "Obligacion_la_operacion_financiada_correspondia_a_una_importacion_de_bienes_con_registro_de",
   "type": "Obligacion",
   "label": "Demostrar registro de ingreso aduanero",
   "tokens_matcheados": 5,
   "resumen_propiedades": "la operación financiada correspondía a una importación de bienes con registro de ingreso aduanero a partir del 13/12/23"
  },
  {
   "id": "Obligacion_la_entidad_a_cargo_del_seguimiento_de_los_pagos_con_registro_de_ingreso_aduanero",
   "type": "Obligacion",
   "label": "Denuncia de incumplimiento en regularización",
   "tokens_matcheados": 5,
   "resumen_propiedades": "La entidad a cargo del seguimiento de los pagos con registro de ingreso aduanero pendiente deberá, dentro de los 5 (cinco) días hábiles siguientes a la fecha de…"
  },
  {
   "id": "Restriccion_el_cliente_se_compromete_a_demostrar_el_registro_de_ingreso_aduanero_de_los_bien",
   "type": "Restriccion",
   "label": "Límite temporal de 90 días",
   "tokens_matcheados": 4,
   "resumen_propiedades": "El cliente se compromete a demostrar el registro de ingreso aduanero de los bienes dentro de los 90 (noventa) días corridos de la fecha de acceso al mercado de …"
  },
  {
   "id": "Operacion_pago_a_la_vista_contra_presentacion_de_documentacion",
   "type": "Operacion",
   "label": "Pago a la vista de importación",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Pagos a la vista contra la presentación de la documentación de embarque"
  },
  {
   "id": "Operacion_pago_a_la_vista_de_importaciones_de_bienes",
   "type": "Operacion",
   "label": "Pago a la vista de importaciones",
   "tokens_matcheados": 4,
   "resumen_propiedades": "tipo: pago a la vista de importaciones de bienes"
  },
  {
   "id": "Restriccion_pago_de_deudas_comerciales_por_importaciones_de_bienes_con_registro_de_ingreso_a",
   "type": "Restriccion",
   "label": "Deudas elegibles hasta fecha límite",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Pago de deudas comerciales por importaciones de bienes con registro de ingreso aduanero hasta el 12/12/23, que resultaban elegibles"
  },
  {
   "id": "Obligacion_cuenta_con_la_declaracion_jurada_del_cliente_de_que_se_compromete_a_demostrar_el",
   "type": "Obligacion",
   "label": "Declaración jurada de ingreso aduanero",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Cuenta con la declaración jurada del cliente de que se compromete a demostrar el registro de ingreso aduanero de los bienes dentro de los 90 (noventa) días corr…"
  },
  {
   "id": "Excepcion_pagar_a_la_fecha_de_cierre_de_la_operacion_de_recompra_y_o_rescate_sin_necesidad",
   "type": "Excepcion",
   "label": "Excepción para pago de gastos de emisión",
   "tokens_matcheados": 4,
   "resumen_propiedades": "pagar a la fecha de cierre de la operación de recompra y/o rescate, sin necesidad de que exista una liquidación de fondos por el monto equivalente, los gastos d…"
  }
 ]
}
```

### paso 14 — ver_nodo {"id": "Excepcion_para_cartas_de_credito_o_letras_avaladas_emitidas_u_otorgadas_a_partir_del_14_04"}

```json
{
 "id": "Excepcion_para_cartas_de_credito_o_letras_avaladas_emitidas_u_otorgadas_a_partir_del_14_04",
 "type": "Excepcion",
 "label": "Excepción por pagos a la vista desde 14/04/25",
 "properties": {
  "descripcion": "Para cartas de crédito o letras avaladas emitidas u otorgadas a partir del 14/04/25, también se admitirá que el pago se concretara a partir de la fecha estimada de embarque más 15 días corridos cuando correspondía a porción de operación con pagos a la vista"
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 10.3. Pagos de importaciones de bienes que cuentan con registro de ingreso aduanero. (parte 2)"
  }
 ]
}
```

### paso 15 — buscar_nodos {"consulta": "punto 12 plan integración capital BCRA presentar", "limite": 10}

```json
{
 "consulta": "punto 12 plan integración capital BCRA presentar",
 "total_con_match": 376,
 "resultados": [
  {
   "id": "Operacion_integracion_de_capital",
   "type": "Operacion",
   "label": "Integración de capital",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La integración se determinará en forma diaria considerando la RPC del último día del mes anterior y el cambio de valor diario del portafolio de activos"
  },
  {
   "id": "Excepcion_no_aplicable_punto_3_12_1",
   "type": "Excepcion",
   "label": "No aplicable punto 3.12.1",
   "tokens_matcheados": 2,
   "resumen_propiedades": "En la medida que no encuadre en el punto 3.12.1"
  },
  {
   "id": "Operacion_integracion_de_capital_minimo",
   "type": "Operacion",
   "label": "Integración de capital mínimo",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: integración de capital mínimo"
  },
  {
   "id": "Operacion_suscripcion_e_integracion_de_instrumentos_capital",
   "type": "Operacion",
   "label": "Suscripción de instrumentos capital",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: suscripción e integración de instrumentos capital"
  },
  {
   "id": "Obligacion_integracion_de_capital_por_posiciones",
   "type": "Obligacion",
   "label": "Integración de capital por posiciones",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La entidad deberá integrar capital por las posiciones de titulización que conserve vinculadas con dicha operación"
  },
  {
   "id": "Obligacion_presentar_estado_financiero_ante_bcra",
   "type": "Obligacion",
   "label": "Presentar estado financiero ante BCRA",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El estado financiero debe haber sido previamente presentado ante el BCRA y estar acompañado de un informe especial del auditor, elaborado según lo establecido e…"
  },
  {
   "id": "Operacion_cumplimiento_de_capital",
   "type": "Operacion",
   "label": "Cumplimiento integración capital mínimo",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: cumplimiento de capital"
  },
  {
   "id": "Restriccion_el_monto_de_capital_por_el_cual_se_accedio_al_mercado_de_cambios_hasta_el_31_12_",
   "type": "Restriccion",
   "label": "Límite monto capital en mercado cambios",
   "tokens_matcheados": 2,
   "resumen_propiedades": "el monto de capital por el cual se accedió al mercado de cambios hasta el 31/12/23 no superó el 40% (cuarenta por ciento) del monto del capital que vencía"
  },
  {
   "id": "Obligacion_calculo_diario_de_integracion_de_capital",
   "type": "Obligacion",
   "label": "Cálculo diario de integración de capital",
   "tokens_matcheados": 2,
   "resumen_propiedades": "A los fines del cumplimiento de lo establecido en el punto 1.1., la integración se determinará en forma diaria considerando: la RPC del último día del mes anter…"
  },
  {
   "id": "Obligacion_presentar_un_plan_de_regularizacion_y_saneamiento_dentro_de_los_30_dias_corridos",
   "type": "Obligacion",
   "label": "Presentar plan regularización saneamiento",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Presentar un plan de regularización y saneamiento dentro de los 30 días corridos siguientes al último día del mes al que corresponda el incumplimiento"
  }
 ]
}
```



---

# CQN2-012

## Respuesta final íntegra (trace.final_json)

```json
{
 "respuesta": "No se encontró información en el Knowledge Graph que responda específicamente a las preguntas formuladas. Aunque se localizaron nodos relacionados con la responsabilidad patrimonial computable (RPC), la integración de capitales mínimos y operaciones de fusión de entidades financieras, no se identificaron disposiciones que especifiquen: (a) qué importe puede adicionarse a los efectos de la determinación de la RPC tras una fusión de entidades financieras, ni (b) cómo se calcula el total de integración (RPC) que la entidad informa como total de control en el régimen informativo sobre exigencia e integración de capitales mínimos. La información disponible en el grafo describe cómo se calcula la RPC en general (en función de saldos de partidas admitidas al último día del mes) y cómo se determina la integración diaria de capital (considerando la RPC del último día del mes anterior y cambios de valor del portafolio), pero no aborda específicamente los efectos de fusiones en estos cálculos.",
 "citas": [],
 "respondible": false
}
```

(`respondible`: false · tool_calls: 15 · hit_tool_limit: True)

## Inventario de pasos + fidelidad runtime↔re-ejecución

| paso | tool | input | output_chars (runtime) | re-ejecutado | fiel |
|---|---|---|---|---|---|
| 1 | buscar_nodos | `{"consulta": "responsabilidad patrimonial computable RPC fusión", "limite": 10}` | 3095 | 3095 | SÍ |
| 2 | buscar_nodos | `{"consulta": "RPC integración capitales mínimos", "limite": 10}` | 3094 | 3094 | SÍ |
| 3 | buscar_nodos | `{"consulta": "fusión entidades financieras adición importe", "limite": 10}` | 3255 | 3255 | SÍ |
| 4 | buscar_nodos | `{"consulta": "fusión absorción integración RPC", "limite": 10}` | 2754 | 2754 | SÍ |
| 5 | ver_nodo | `{"id": "Operacion_integracion_de_capital"}` | 421 | 421 | SÍ |
| 6 | ver_nodo | `{"id": "Obligacion_calcular_responsabilidad_patrimonial_computable"}` | 523 | 523 | SÍ |
| 7 | buscar_nodos | `{"consulta": "adición RPC fusión absorción", "limite": 10}` | 3182 | 3182 | SÍ |
| 8 | buscar_nodos | `{"consulta": "total control régimen informativo exigencia integración", "limite": 10}` | 3666 | 3666 | SÍ |
| 9 | buscar_nodos | `{"consulta": "fusión cambio RPC patrimonio", "limite": 10}` | 2486 | 2486 | SÍ |
| 10 | buscar_nodos | `{"consulta": "adición importe patrimonio capital", "limite": 10}` | 3475 | 3475 | SÍ |
| 11 | buscar_nodos | `{"consulta": "fusión absorción entidad financiera operación", "limite": 10}` | 2966 | 2966 | SÍ |
| 12 | buscar_nodos | `{"consulta": "importe adicionarse RPC determinación", "limite": 10}` | 2991 | 2991 | SÍ |
| 13 | buscar_nodos | `{"consulta": "fusión absorción cambio RPC", "limite": 10}` | 2485 | 2485 | SÍ |
| 14 | buscar_nodos | `{"consulta": "total integración control régimen informativo capitales", "limite": 10}` | 3185 | 3185 | SÍ |
| 15 | ver_nodo | `{"id": "TextoOrdenado_to_capitales_minimos_actual_pdf"}` | 361 | 361 | SÍ |

**Fidelidad: 15/15**.

## Apéndice — outputs completos re-ejecutados

### paso 1 — buscar_nodos {"consulta": "responsabilidad patrimonial computable RPC fusión", "limite": 10}

```json
{
 "consulta": "responsabilidad patrimonial computable RPC fusión",
 "total_con_match": 35,
 "resultados": [
  {
   "id": "Restriccion_responsabilidad_patrimonial_computable_rpc_70200000_8_s_70900000",
   "type": "Restriccion",
   "label": "Límite mínimo Responsabilidad Patrimonial Computable",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Responsabilidad Patrimonial Computable (RPC) = 70200000 ≥ 8% s/70900000"
  },
  {
   "id": "Restriccion_los_limites_maximos_se_aplicaran_sobre_la_responsabilidad_patrimonial_computable",
   "type": "Restriccion",
   "label": "Base de cálculo de límites máximos",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Los límites máximos se aplicarán sobre la responsabilidad patrimonial computable de la entidad financiera del último día anterior al que corresponda"
  },
  {
   "id": "Obligacion_calcular_responsabilidad_patrimonial_computable",
   "type": "Obligacion",
   "label": "Calcular responsabilidad patrimonial computable",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La integración a considerar será la responsabilidad patrimonial computable, que se determinará en función de los saldos de las partidas admitidas registrados al…"
  },
  {
   "id": "Excepcion_activos_que_deben_deducirse_a_los_fines_del_calculo_de_la_responsabilidad_patrim",
   "type": "Excepcion",
   "label": "Exclusión de activos para cálculo RPC",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Activos que deben deducirse a los fines del cálculo de la responsabilidad patrimonial computable"
  },
  {
   "id": "Operacion_reconocimiento_contable_de_capital_regulatorio_computable",
   "type": "Operacion",
   "label": "Reconocimiento de RPC de subsidiarias",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: reconocimiento contable de capital regulatorio computable"
  },
  {
   "id": "Obligacion_los_limites_maximos_establecidos_se_aplicaran_sobre_la_responsabilidad_patrimoni",
   "type": "Obligacion",
   "label": "Aplicación sobre responsabilidad patrimonial",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Los límites máximos establecidos se aplicarán sobre la responsabilidad patrimonial computable (RPC) de la entidad financiera del último día anterior al que corr…"
  },
  {
   "id": "Restriccion_el_importe_de_rpc_debera_ser_resultante_de_multiplicar_8_por_los_apr",
   "type": "Restriccion",
   "label": "Límite mínimo RPC",
   "tokens_matcheados": 1,
   "resumen_propiedades": "El importe de RPC deberá ser resultante de multiplicar 8% por los APR"
  },
  {
   "id": "Operacion_cesion_de_creditos_sin_responsabilidad",
   "type": "Operacion",
   "label": "Cesión de créditos",
   "tokens_matcheados": 1,
   "resumen_propiedades": "tipo: cesión de créditos sin responsabilidad"
  },
  {
   "id": "Operacion_determinacion_de_ratio_de_capital_regulatorio",
   "type": "Operacion",
   "label": "Determinación de RPC",
   "tokens_matcheados": 1,
   "resumen_propiedades": "tipo: determinación de ratio de capital regulatorio"
  },
  {
   "id": "Operacion_operaciones_de_titulizacion_y_venta_o_cesion_de_cartera_con_responsabilidad",
   "type": "Operacion",
   "label": "Titulización cartera",
   "tokens_matcheados": 1,
   "resumen_propiedades": "tipo: Operaciones de titulización y venta o cesión de cartera con responsabilidad"
  }
 ]
}
```

### paso 2 — buscar_nodos {"consulta": "RPC integración capitales mínimos", "limite": 10}

```json
{
 "consulta": "RPC integración capitales mínimos",
 "total_con_match": 36,
 "resultados": [
  {
   "id": "Operacion_integracion_de_capitales",
   "type": "Operacion",
   "label": "Integración de capitales mínimos",
   "tokens_matcheados": 3,
   "resumen_propiedades": "tipo: integración de capitales"
  },
  {
   "id": "TextoOrdenado_to_capitales_minimos_actual_pdf",
   "type": "TextoOrdenado",
   "label": "Capitales Mínimos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "materia: capitales minimos; archivo: TO_capitales_minimos_actual.pdf; version: actual"
  },
  {
   "id": "Obligacion_las_entidades_financieras_comprendidas_sus_filiales_en_el_pais_y_en_el_exterior_",
   "type": "Obligacion",
   "label": "Observar capitales mínimos en base individual",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Las entidades financieras (comprendidas sus filiales en el país y en el exterior) observarán las normas en materia de capitales mínimos en forma individual."
  },
  {
   "id": "Operacion_observancia_de_requisitos_de_capitales_minimos_en_base_individual",
   "type": "Operacion",
   "label": "Observancia capitales mínimos base individual",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: Observancia de requisitos de capitales mínimos en base individual"
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
   "id": "Restriccion_el_importe_de_rpc_debera_ser_resultante_de_multiplicar_8_por_los_apr",
   "type": "Restriccion",
   "label": "Límite mínimo RPC",
   "tokens_matcheados": 1,
   "resumen_propiedades": "El importe de RPC deberá ser resultante de multiplicar 8% por los APR"
  },
  {
   "id": "Operacion_determinacion_de_ratio_de_capital_regulatorio",
   "type": "Operacion",
   "label": "Determinación de RPC",
   "tokens_matcheados": 1,
   "resumen_propiedades": "tipo: determinación de ratio de capital regulatorio"
  },
  {
   "id": "Operacion_integracion_de_capital",
   "type": "Operacion",
   "label": "Integración de capital",
   "tokens_matcheados": 1,
   "resumen_propiedades": "La integración se determinará en forma diaria considerando la RPC del último día del mes anterior y el cambio de valor diario del portafolio de activos"
  },
  {
   "id": "Restriccion_el_importe_de_esta_rpc_que_sera_admisible_como_pnc_excluye_los_importes_reconoci",
   "type": "Restriccion",
   "label": "Exclusión de RPC en PNc",
   "tokens_matcheados": 1,
   "resumen_propiedades": "El importe de esta RPC que será admisible como PNc excluye los importes reconocidos en el CO conforme a lo establecido en el punto 8.3.5.1. y los importes recon…"
  }
 ]
}
```

### paso 3 — buscar_nodos {"consulta": "fusión entidades financieras adición importe", "limite": 10}

```json
{
 "consulta": "fusión entidades financieras adición importe",
 "total_con_match": 166,
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

### paso 4 — buscar_nodos {"consulta": "fusión absorción integración RPC", "limite": 10}

```json
{
 "consulta": "fusión absorción integración RPC",
 "total_con_match": 27,
 "resultados": [
  {
   "id": "Restriccion_el_importe_de_rpc_debera_ser_resultante_de_multiplicar_8_por_los_apr",
   "type": "Restriccion",
   "label": "Límite mínimo RPC",
   "tokens_matcheados": 1,
   "resumen_propiedades": "El importe de RPC deberá ser resultante de multiplicar 8% por los APR"
  },
  {
   "id": "Operacion_determinacion_de_ratio_de_capital_regulatorio",
   "type": "Operacion",
   "label": "Determinación de RPC",
   "tokens_matcheados": 1,
   "resumen_propiedades": "tipo: determinación de ratio de capital regulatorio"
  },
  {
   "id": "Operacion_integracion_de_capital",
   "type": "Operacion",
   "label": "Integración de capital",
   "tokens_matcheados": 1,
   "resumen_propiedades": "La integración se determinará en forma diaria considerando la RPC del último día del mes anterior y el cambio de valor diario del portafolio de activos"
  },
  {
   "id": "Restriccion_el_importe_de_esta_rpc_que_sera_admisible_como_pnc_excluye_los_importes_reconoci",
   "type": "Restriccion",
   "label": "Exclusión de RPC en PNc",
   "tokens_matcheados": 1,
   "resumen_propiedades": "El importe de esta RPC que será admisible como PNc excluye los importes reconocidos en el CO conforme a lo establecido en el punto 8.3.5.1. y los importes recon…"
  },
  {
   "id": "Operacion_integracion_de_capital_minimo",
   "type": "Operacion",
   "label": "Integración de capital mínimo",
   "tokens_matcheados": 1,
   "resumen_propiedades": "tipo: integración de capital mínimo"
  },
  {
   "id": "Operacion_computacion_de_capital",
   "type": "Operacion",
   "label": "Inclusión de instrumentos en RPC",
   "tokens_matcheados": 1,
   "resumen_propiedades": "tipo: computación de capital"
  },
  {
   "id": "Operacion_integracion_de_capitales",
   "type": "Operacion",
   "label": "Integración de capitales mínimos",
   "tokens_matcheados": 1,
   "resumen_propiedades": "tipo: integración de capitales"
  },
  {
   "id": "Operacion_otra",
   "type": "Operacion",
   "label": "Regularizar defectos integración",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Acciones conducentes a regularizar los defectos de integración diaria de capital mínimo"
  },
  {
   "id": "Obligacion_el_importe_que_se_reconocera_en_la_rpc_de_la_entidad_financiera_sera_el_importe_",
   "type": "Obligacion",
   "label": "Cálculo de RPC neto de excedentes",
   "tokens_matcheados": 1,
   "resumen_propiedades": "El importe que se reconocerá en la RPC de la entidad financiera será el importe de la participación minoritaria en la RPC de la subsidiaria neto del excedente d…"
  },
  {
   "id": "Restriccion_umbral_de_2_5_rpc_para_aprobacion",
   "type": "Restriccion",
   "label": "Umbral de 2,5% RPC para aprobación",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Las financiaciones que excedan del 2,5 % de la RPC de la entidad financiera del mes anterior deberán contar con aprobación previa"
  }
 ]
}
```

### paso 5 — ver_nodo {"id": "Operacion_integracion_de_capital"}

```json
{
 "id": "Operacion_integracion_de_capital",
 "type": "Operacion",
 "label": "Integración de capital",
 "properties": {
  "tipo": "integración de capital",
  "description": "La integración se determinará en forma diaria considerando la RPC del último día del mes anterior y el cambio de valor diario del portafolio de activos"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Punto 6.7. Cómputo."
  }
 ]
}
```

### paso 6 — ver_nodo {"id": "Obligacion_calcular_responsabilidad_patrimonial_computable"}

```json
{
 "id": "Obligacion_calcular_responsabilidad_patrimonial_computable",
 "type": "Obligacion",
 "label": "Calcular responsabilidad patrimonial computable",
 "properties": {
  "tipo": "calculo",
  "description": "La integración a considerar será la responsabilidad patrimonial computable, que se determinará en función de los saldos de las partidas admitidas registrados al último día del mes bajo informe",
  "plazo": "mensual"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Punto 1.3. Integración."
  }
 ]
}
```

### paso 7 — buscar_nodos {"consulta": "adición RPC fusión absorción", "limite": 10}

```json
{
 "consulta": "adición RPC fusión absorción",
 "total_con_match": 18,
 "resultados": [
  {
   "id": "Restriccion_el_importe_de_rpc_debera_ser_resultante_de_multiplicar_8_por_los_apr",
   "type": "Restriccion",
   "label": "Límite mínimo RPC",
   "tokens_matcheados": 1,
   "resumen_propiedades": "El importe de RPC deberá ser resultante de multiplicar 8% por los APR"
  },
  {
   "id": "Operacion_determinacion_de_ratio_de_capital_regulatorio",
   "type": "Operacion",
   "label": "Determinación de RPC",
   "tokens_matcheados": 1,
   "resumen_propiedades": "tipo: determinación de ratio de capital regulatorio"
  },
  {
   "id": "Restriccion_el_importe_de_esta_rpc_que_sera_admisible_como_pnc_excluye_los_importes_reconoci",
   "type": "Restriccion",
   "label": "Exclusión de RPC en PNc",
   "tokens_matcheados": 1,
   "resumen_propiedades": "El importe de esta RPC que será admisible como PNc excluye los importes reconocidos en el CO conforme a lo establecido en el punto 8.3.5.1. y los importes recon…"
  },
  {
   "id": "Operacion_computacion_de_capital",
   "type": "Operacion",
   "label": "Inclusión de instrumentos en RPC",
   "tokens_matcheados": 1,
   "resumen_propiedades": "tipo: computación de capital"
  },
  {
   "id": "Obligacion_el_importe_que_se_reconocera_en_la_rpc_de_la_entidad_financiera_sera_el_importe_",
   "type": "Obligacion",
   "label": "Cálculo de RPC neto de excedentes",
   "tokens_matcheados": 1,
   "resumen_propiedades": "El importe que se reconocerá en la RPC de la entidad financiera será el importe de la participación minoritaria en la RPC de la subsidiaria neto del excedente d…"
  },
  {
   "id": "Restriccion_umbral_de_2_5_rpc_para_aprobacion",
   "type": "Restriccion",
   "label": "Umbral de 2,5% RPC para aprobación",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Las financiaciones que excedan del 2,5 % de la RPC de la entidad financiera del mes anterior deberán contar con aprobación previa"
  },
  {
   "id": "Obligacion_los_instrumentos_que_son_parte_del_pasivo_deberan_absorber_perdidas_cuando_el_co",
   "type": "Obligacion",
   "label": "Absorción de pérdidas al nivel de CO",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Los instrumentos que son parte del pasivo deberán absorber pérdidas cuando el coeficiente de CO sea inferior al 5,125 % de los APR a través de su conversión en …"
  },
  {
   "id": "Excepcion_activos_que_deben_deducirse_a_los_fines_del_calculo_de_la_responsabilidad_patrim",
   "type": "Excepcion",
   "label": "Exclusión de activos para cálculo RPC",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Activos que deben deducirse a los fines del cálculo de la responsabilidad patrimonial computable"
  },
  {
   "id": "Obligacion_sus_terminos_y_condiciones_deberan_incluir_una_disposicion_en_virtud_de_la_cual_",
   "type": "Obligacion",
   "label": "Absorción de pérdidas en instrumentos",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Sus términos y condiciones deberán incluir una disposición en virtud de la cual los instrumentos deberán absorber pérdidas –a través de una quita definitiva o m…"
  },
  {
   "id": "Operacion_reconocimiento_contable_de_capital_regulatorio_computable",
   "type": "Operacion",
   "label": "Reconocimiento de RPC de subsidiarias",
   "tokens_matcheados": 1,
   "resumen_propiedades": "tipo: reconocimiento contable de capital regulatorio computable"
  }
 ]
}
```

### paso 8 — buscar_nodos {"consulta": "total control régimen informativo exigencia integración", "limite": 10}

```json
{
 "consulta": "total control régimen informativo exigencia integración",
 "total_con_match": 184,
 "resultados": [
  {
   "id": "Obligacion_las_entidades_deberan_consultar_en_el_apartado_regimen_informativo_sepaimpo_del_",
   "type": "Obligacion",
   "label": "Consultar situación del cliente",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Las entidades deberán consultar en el apartado 'Régimen Informativo SEPAIMPO' del sitio www3.bcra.gob.ar, si el cliente se encuentra en la situación de condena …"
  },
  {
   "id": "Operacion_presentacion_informativa_de_operaciones_cambiarias",
   "type": "Operacion",
   "label": "Validación en régimen informativo",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: presentación informativa de operaciones cambiarias"
  },
  {
   "id": "TextoOrdenado_to_regimen_informativo_contable_mensual_actual_pdf",
   "type": "TextoOrdenado",
   "label": "Régimen Informativo Contable Mensual",
   "tokens_matcheados": 2,
   "resumen_propiedades": "materia: Información contable y regulatoria mensual; archivo: TO_regimen_informativo_contable_mensual_actual.pdf; version: actual"
  },
  {
   "id": "Obligacion_la_entidad_debera_dar_cumplimiento_a_las_disposiciones_dadas_a_conocer_por_el_re",
   "type": "Obligacion",
   "label": "Cumplimiento régimen informativo BCRA",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La entidad deberá dar cumplimiento a las disposiciones dadas a conocer por el régimen informativo asociado a este seguimiento."
  },
  {
   "id": "Obligacion_para_la_determinacion_de_la_exigencia_total_computable_del_periodo_n_se_consider",
   "type": "Obligacion",
   "label": "Determinar exigencia total computable",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Para la determinación de la exigencia total computable del período (n) se considerará el esquema especificado con los códigos de rubros contables"
  },
  {
   "id": "Obligacion_consultar_regimen_informativo_sepaimpo",
   "type": "Obligacion",
   "label": "Consultar régimen informativo SEPAIMPO",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Las entidades deberán consultar en el apartado Régimen Informativo SEPAIMPO del sitio www3.bcra.gob.ar el saldo pendiente de regularización por pagos anticipado…"
  },
  {
   "id": "Obligacion_deberan_mantenerse_actualizados_e_informarse_por_medio_del_regimen_informativo_e",
   "type": "Obligacion",
   "label": "Mantener actualizados datos de contacto",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Deberán mantenerse actualizados e informarse por medio del régimen informativo establecido al efecto los números de teléfonos, fax y dirección/es postales y de …"
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
  },
  {
   "id": "Obligacion_cuando_una_entidad_provea_proteccion_crediticia_total_o_proporcional_a_una_posic",
   "type": "Obligacion",
   "label": "Calcular exigencia proveedor protección total",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Cuando una entidad provea protección crediticia total o proporcional a una posición de titulización, la entidad proveedora deberá calcular su exigencia de capit…"
  }
 ]
}
```

### paso 9 — buscar_nodos {"consulta": "fusión cambio RPC patrimonio", "limite": 10}

```json
{
 "consulta": "fusión cambio RPC patrimonio",
 "total_con_match": 83,
 "resultados": [
  {
   "id": "EntidadFinanciera_casa_de_cambio",
   "type": "EntidadFinanciera",
   "label": "Casas de cambio",
   "tokens_matcheados": 1,
   "resumen_propiedades": "categoria: casa de cambio"
  },
  {
   "id": "Restriccion_el_importe_de_rpc_debera_ser_resultante_de_multiplicar_8_por_los_apr",
   "type": "Restriccion",
   "label": "Límite mínimo RPC",
   "tokens_matcheados": 1,
   "resumen_propiedades": "El importe de RPC deberá ser resultante de multiplicar 8% por los APR"
  },
  {
   "id": "EntidadFinanciera_agencia_de_cambio",
   "type": "EntidadFinanciera",
   "label": "Agencias de cambio",
   "tokens_matcheados": 1,
   "resumen_propiedades": "categoria: agencia de cambio"
  },
  {
   "id": "Operacion_cambio",
   "type": "Operacion",
   "label": "Operación de cambio",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Operación de cambio realizada entre partes a tipo de cambio libremente pactado"
  },
  {
   "id": "Operacion_cambio_de_moneda",
   "type": "Operacion",
   "label": "Operación de cambio",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Operación de cambio realizada por un cliente con una entidad interviniente"
  },
  {
   "id": "EntidadFinanciera_operador_de_cambio",
   "type": "EntidadFinanciera",
   "label": "Operadores de cambio",
   "tokens_matcheados": 1,
   "resumen_propiedades": "categoria: operador de cambio"
  },
  {
   "id": "Operacion_determinacion_de_ratio_de_capital_regulatorio",
   "type": "Operacion",
   "label": "Determinación de RPC",
   "tokens_matcheados": 1,
   "resumen_propiedades": "tipo: determinación de ratio de capital regulatorio"
  },
  {
   "id": "Restriccion_el_importe_de_esta_rpc_que_sera_admisible_como_pnc_excluye_los_importes_reconoci",
   "type": "Restriccion",
   "label": "Exclusión de RPC en PNc",
   "tokens_matcheados": 1,
   "resumen_propiedades": "El importe de esta RPC que será admisible como PNc excluye los importes reconocidos en el CO conforme a lo establecido en el punto 8.3.5.1. y los importes recon…"
  },
  {
   "id": "Obligacion_el_cambio_de_entidad_debe_quedar_registrado_en_el_bcra",
   "type": "Obligacion",
   "label": "Registrar cambio en BCRA",
   "tokens_matcheados": 1,
   "resumen_propiedades": "El cambio de entidad debe quedar registrado en el BCRA"
  },
  {
   "id": "Obligacion_boleto_de_venta_de_cambio",
   "type": "Obligacion",
   "label": "Boleto de venta de cambio",
   "tokens_matcheados": 1,
   "resumen_propiedades": "La mencionada entidad deberá realizar un boleto de venta de cambio a nombre del cliente por el código de concepto que identifique el tipo de operación consignan…"
  }
 ]
}
```

### paso 10 — buscar_nodos {"consulta": "adición importe patrimonio capital", "limite": 10}

```json
{
 "consulta": "adición importe patrimonio capital",
 "total_con_match": 234,
 "resultados": [
  {
   "id": "Obligacion_consignar_importe_patrimonio_neto",
   "type": "Obligacion",
   "label": "Consignar importe patrimonio neto",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Se consignará el importe total del Patrimonio Neto (rubro 400000 del balance), excluyendo las acciones con preferencia patrimonial y la reserva especial para in…"
  },
  {
   "id": "Obligacion_el_importe_por_encima_de_este_10_debera_deducirse_de_cada_uno_de_los_niveles_de_",
   "type": "Obligacion",
   "label": "Deducir según metodología capital",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El importe por encima de este 10 % deberá deducirse de cada uno de los niveles de capital en función de la siguiente metodología: Monto a deducir del CON1: tota…"
  },
  {
   "id": "Obligacion_el_importe_del_capital_prestado_el_monto_total_a_pagar_la_cantidad_de_cuotas_per",
   "type": "Obligacion",
   "label": "Informar detalles de préstamos en cuotas",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El importe del capital prestado, el monto total a pagar, la cantidad de cuotas, periodicidad y fecha de vencimiento, el sistema de amortización de capital y can…"
  },
  {
   "id": "Restriccion_el_importe_de_estas_participaciones_debera_deducirse_de_cada_uno_de_los_correspo",
   "type": "Restriccion",
   "label": "Deducción de participaciones del capital",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El importe de estas participaciones deberá deducirse de cada uno de los correspondientes niveles de capital de la entidad financiera"
  },
  {
   "id": "Obligacion_debera_deducir_del_capital_ordinario_de_nivel_uno_con1_el_importe_total_en_conce",
   "type": "Obligacion",
   "label": "Deducción ganancia venta respaldo implícito",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Deberá deducir del capital ordinario de nivel uno (COn1) el importe total en concepto de ganancia por venta resultante de la operación de titulización, de acuer…"
  },
  {
   "id": "Obligacion_el_importe_que_se_reconocera_en_el_co_de_la_entidad_sera_el_importe_de_la_partic",
   "type": "Obligacion",
   "label": "Cálculo de capital ordinario neto de excedentes",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El importe que se reconocerá en el CO de la entidad será el importe de la participación minoritaria en el CO de la subsidiaria neto del excedente de CO de la su…"
  },
  {
   "id": "Restriccion_el_importe_resultante_de_la_seccion_2_debera_ser_multiplicado_por_un_factor_igua",
   "type": "Restriccion",
   "label": "Factor multiplicador 4 para capital mínimo agrícola",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El importe resultante de la Sección 2 deberá ser multiplicado por un factor igual a 4"
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
  },
  {
   "id": "Restriccion_el_importe_de_rpc_debera_ser_resultante_de_multiplicar_8_por_los_apr",
   "type": "Restriccion",
   "label": "Límite mínimo RPC",
   "tokens_matcheados": 1,
   "resumen_propiedades": "El importe de RPC deberá ser resultante de multiplicar 8% por los APR"
  }
 ]
}
```

### paso 11 — buscar_nodos {"consulta": "fusión absorción entidad financiera operación", "limite": 10}

```json
{
 "consulta": "fusión absorción entidad financiera operación",
 "total_con_match": 1161,
 "resultados": [
  {
   "id": "Obligacion_la_entidad_financiera_encargada_del_seguimiento_de_anticipos_y_otras_financiacio",
   "type": "Obligacion",
   "label": "Registrar operación ante BCRA",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La entidad financiera encargada del Seguimiento de anticipos y otras financiaciones de exportación de bienes de las operaciones deberá concretar su registro ant…"
  },
  {
   "id": "Obligacion_la_entidad_financiera_designada_debera_remitir_por_nota_dirigida_a_la_gerencia_p",
   "type": "Obligacion",
   "label": "Remitir certificación operación",
   "tokens_matcheados": 3,
   "resumen_propiedades": "la entidad financiera designada deberá remitir, por nota dirigida a la Gerencia Principal de Exterior y Cambios dentro de los 90 (noventa) días corridos posteri…"
  },
  {
   "id": "Operacion_nominacion_de_responsable",
   "type": "Operacion",
   "label": "Nominación de entidad financiera",
   "tokens_matcheados": 3,
   "resumen_propiedades": "tipo: nominación de responsable"
  },
  {
   "id": "Operacion_reclasificacion",
   "type": "Operacion",
   "label": "Reclasificación de entidad financiera",
   "tokens_matcheados": 3,
   "resumen_propiedades": "tipo: reclasificación"
  },
  {
   "id": "Operacion_financiacion_de_importaciones_de_bienes_otorgada_por_entidad_financiera_local_co",
   "type": "Operacion",
   "label": "Financiación de importaciones con línea exterior",
   "tokens_matcheados": 3,
   "resumen_propiedades": "tipo: financiación de importaciones de bienes otorgada por entidad financiera local con línea de crédito del exterior"
  },
  {
   "id": "Operacion_asistencia_financiera_mediante_operaciones_de_arrendamiento_financiero_de_bienes",
   "type": "Operacion",
   "label": "Arrendamiento financiero",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: Asistencia financiera mediante operaciones de arrendamiento financiero de bienes de capital, durables e inmuebles, adquiridos con tal objeto (leasing)"
  },
  {
   "id": "Operacion_registro_del_cambio_de_entidad_en_el_bcra",
   "type": "Operacion",
   "label": "Registro de cambio en BCRA",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: registro del cambio de entidad en el BCRA"
  },
  {
   "id": "Obligacion_cuando_la_entidad_financiera_realice_operaciones_con_una_qccp_debera_determinar_",
   "type": "Obligacion",
   "label": "Determinar exposición a QCCP",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Cuando la entidad financiera realice operaciones con una QCCP deberá determinar su exposición aplicando las disposiciones del punto 4.3.3."
  },
  {
   "id": "Operacion_notificacion_de_voluntad_del_exportador",
   "type": "Operacion",
   "label": "Notificación a nueva entidad",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: notificación de voluntad del exportador"
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

### paso 12 — buscar_nodos {"consulta": "importe adicionarse RPC determinación", "limite": 10}

```json
{
 "consulta": "importe adicionarse RPC determinación",
 "total_con_match": 65,
 "resultados": [
  {
   "id": "Restriccion_el_importe_de_rpc_debera_ser_resultante_de_multiplicar_8_por_los_apr",
   "type": "Restriccion",
   "label": "Límite mínimo RPC",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El importe de RPC deberá ser resultante de multiplicar 8% por los APR"
  },
  {
   "id": "Operacion_determinacion_de_ratio_de_capital_regulatorio",
   "type": "Operacion",
   "label": "Determinación de RPC",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: determinación de ratio de capital regulatorio"
  },
  {
   "id": "Restriccion_el_importe_de_esta_rpc_que_sera_admisible_como_pnc_excluye_los_importes_reconoci",
   "type": "Restriccion",
   "label": "Exclusión de RPC en PNc",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El importe de esta RPC que será admisible como PNc excluye los importes reconocidos en el CO conforme a lo establecido en el punto 8.3.5.1. y los importes recon…"
  },
  {
   "id": "Obligacion_el_importe_que_se_reconocera_en_la_rpc_de_la_entidad_financiera_sera_el_importe_",
   "type": "Obligacion",
   "label": "Cálculo de RPC neto de excedentes",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El importe que se reconocerá en la RPC de la entidad financiera será el importe de la participación minoritaria en la RPC de la subsidiaria neto del excedente d…"
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
  },
  {
   "id": "Obligacion_importe_determinado_mediante_la_suma_de_los_valores_obtenidos_luego_de_multiplic",
   "type": "Obligacion",
   "label": "Cálculo de exigencia DvP",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Importe determinado mediante la suma de los valores obtenidos luego de multiplicar la exposición actual positiva por la exigencia de capital aplicable estableci…"
  },
  {
   "id": "Obligacion_la_partida_correspondiente_al_bic_se_informara_por_el_importe_calculado_en_funci",
   "type": "Obligacion",
   "label": "Informar componentes BIC",
   "tokens_matcheados": 1,
   "resumen_propiedades": "La partida correspondiente al BIC se informará por el importe calculado en función de los coeficientes marginales que corresponda"
  },
  {
   "id": "Operacion_calculo_mensual_de_exigencia_operacional",
   "type": "Operacion",
   "label": "Determinación mensual CRO",
   "tokens_matcheados": 1,
   "resumen_propiedades": "tipo: cálculo mensual de exigencia operacional"
  },
  {
   "id": "Operacion_calculo_de_ingreso_bruto",
   "type": "Operacion",
   "label": "Determinación ingreso bruto",
   "tokens_matcheados": 1,
   "resumen_propiedades": "tipo: calculo de ingreso bruto"
  }
 ]
}
```

### paso 13 — buscar_nodos {"consulta": "fusión absorción cambio RPC", "limite": 10}

```json
{
 "consulta": "fusión absorción cambio RPC",
 "total_con_match": 77,
 "resultados": [
  {
   "id": "EntidadFinanciera_casa_de_cambio",
   "type": "EntidadFinanciera",
   "label": "Casas de cambio",
   "tokens_matcheados": 1,
   "resumen_propiedades": "categoria: casa de cambio"
  },
  {
   "id": "Restriccion_el_importe_de_rpc_debera_ser_resultante_de_multiplicar_8_por_los_apr",
   "type": "Restriccion",
   "label": "Límite mínimo RPC",
   "tokens_matcheados": 1,
   "resumen_propiedades": "El importe de RPC deberá ser resultante de multiplicar 8% por los APR"
  },
  {
   "id": "EntidadFinanciera_agencia_de_cambio",
   "type": "EntidadFinanciera",
   "label": "Agencias de cambio",
   "tokens_matcheados": 1,
   "resumen_propiedades": "categoria: agencia de cambio"
  },
  {
   "id": "Operacion_cambio",
   "type": "Operacion",
   "label": "Operación de cambio",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Operación de cambio realizada entre partes a tipo de cambio libremente pactado"
  },
  {
   "id": "Operacion_cambio_de_moneda",
   "type": "Operacion",
   "label": "Operación de cambio",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Operación de cambio realizada por un cliente con una entidad interviniente"
  },
  {
   "id": "EntidadFinanciera_operador_de_cambio",
   "type": "EntidadFinanciera",
   "label": "Operadores de cambio",
   "tokens_matcheados": 1,
   "resumen_propiedades": "categoria: operador de cambio"
  },
  {
   "id": "Operacion_determinacion_de_ratio_de_capital_regulatorio",
   "type": "Operacion",
   "label": "Determinación de RPC",
   "tokens_matcheados": 1,
   "resumen_propiedades": "tipo: determinación de ratio de capital regulatorio"
  },
  {
   "id": "Restriccion_el_importe_de_esta_rpc_que_sera_admisible_como_pnc_excluye_los_importes_reconoci",
   "type": "Restriccion",
   "label": "Exclusión de RPC en PNc",
   "tokens_matcheados": 1,
   "resumen_propiedades": "El importe de esta RPC que será admisible como PNc excluye los importes reconocidos en el CO conforme a lo establecido en el punto 8.3.5.1. y los importes recon…"
  },
  {
   "id": "Obligacion_el_cambio_de_entidad_debe_quedar_registrado_en_el_bcra",
   "type": "Obligacion",
   "label": "Registrar cambio en BCRA",
   "tokens_matcheados": 1,
   "resumen_propiedades": "El cambio de entidad debe quedar registrado en el BCRA"
  },
  {
   "id": "Obligacion_boleto_de_venta_de_cambio",
   "type": "Obligacion",
   "label": "Boleto de venta de cambio",
   "tokens_matcheados": 1,
   "resumen_propiedades": "La mencionada entidad deberá realizar un boleto de venta de cambio a nombre del cliente por el código de concepto que identifique el tipo de operación consignan…"
  }
 ]
}
```

### paso 14 — buscar_nodos {"consulta": "total integración control régimen informativo capitales", "limite": 10}

```json
{
 "consulta": "total integración control régimen informativo capitales",
 "total_con_match": 84,
 "resultados": [
  {
   "id": "Obligacion_las_entidades_deberan_consultar_en_el_apartado_regimen_informativo_sepaimpo_del_",
   "type": "Obligacion",
   "label": "Consultar situación del cliente",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Las entidades deberán consultar en el apartado 'Régimen Informativo SEPAIMPO' del sitio www3.bcra.gob.ar, si el cliente se encuentra en la situación de condena …"
  },
  {
   "id": "Operacion_integracion_de_capitales",
   "type": "Operacion",
   "label": "Integración de capitales mínimos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: integración de capitales"
  },
  {
   "id": "Operacion_presentacion_informativa_de_operaciones_cambiarias",
   "type": "Operacion",
   "label": "Validación en régimen informativo",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: presentación informativa de operaciones cambiarias"
  },
  {
   "id": "TextoOrdenado_to_regimen_informativo_contable_mensual_actual_pdf",
   "type": "TextoOrdenado",
   "label": "Régimen Informativo Contable Mensual",
   "tokens_matcheados": 2,
   "resumen_propiedades": "materia: Información contable y regulatoria mensual; archivo: TO_regimen_informativo_contable_mensual_actual.pdf; version: actual"
  },
  {
   "id": "Obligacion_la_entidad_debera_dar_cumplimiento_a_las_disposiciones_dadas_a_conocer_por_el_re",
   "type": "Obligacion",
   "label": "Cumplimiento régimen informativo BCRA",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La entidad deberá dar cumplimiento a las disposiciones dadas a conocer por el régimen informativo asociado a este seguimiento."
  },
  {
   "id": "Obligacion_consultar_regimen_informativo_sepaimpo",
   "type": "Obligacion",
   "label": "Consultar régimen informativo SEPAIMPO",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Las entidades deberán consultar en el apartado Régimen Informativo SEPAIMPO del sitio www3.bcra.gob.ar el saldo pendiente de regularización por pagos anticipado…"
  },
  {
   "id": "Obligacion_deberan_mantenerse_actualizados_e_informarse_por_medio_del_regimen_informativo_e",
   "type": "Obligacion",
   "label": "Mantener actualizados datos de contacto",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Deberán mantenerse actualizados e informarse por medio del régimen informativo establecido al efecto los números de teléfonos, fax y dirección/es postales y de …"
  },
  {
   "id": "TextoOrdenado_to_capitales_minimos_actual_pdf",
   "type": "TextoOrdenado",
   "label": "Capitales Mínimos",
   "tokens_matcheados": 1,
   "resumen_propiedades": "materia: capitales minimos; archivo: TO_capitales_minimos_actual.pdf; version: actual"
  },
  {
   "id": "Operacion_integracion_de_capital",
   "type": "Operacion",
   "label": "Integración de capital",
   "tokens_matcheados": 1,
   "resumen_propiedades": "La integración se determinará en forma diaria considerando la RPC del último día del mes anterior y el cambio de valor diario del portafolio de activos"
  },
  {
   "id": "Operacion_registro_informativo",
   "type": "Operacion",
   "label": "Registro de operaciones",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Registrar en bases de datos cualquier circunstancia que implique una reducción del monto del capital adeudado y disponible para aplicación"
  }
 ]
}
```

### paso 15 — ver_nodo {"id": "TextoOrdenado_to_capitales_minimos_actual_pdf"}

```json
{
 "id": "TextoOrdenado_to_capitales_minimos_actual_pdf",
 "type": "TextoOrdenado",
 "label": "Capitales Mínimos",
 "properties": {
  "materia": "capitales minimos",
  "archivo": "TO_capitales_minimos_actual.pdf",
  "version": "actual"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Punto 1.1. “A” 2136 1. 1° Según Com. “A” 2859, 3558,"
  }
 ]
}
```



---

# CQN2-013

## Respuesta final íntegra (trace.final_json)

```json
{
 "respuesta": "(a) En el régimen informativo sobre exigencia e integración de capitales mínimos, la exigencia de capital por riesgo de crédito se calcula mediante la expresión: C_RC = (k x 0,08 x APR_c) + INC\n\n(b) Un residente que debe pagar un servicio de asesoramiento (no comprendido en los conceptos con tratamiento especial) prestado a partir del 14/04/25 por una contraparte vinculada del exterior debe esperar 180 días corridos desde la prestación o devengamiento del servicio para poder acceder al mercado de cambios. Esto se deduce de que los servicios no comprendidos en los puntos 13.2.1 a 13.2.5 (que incluyen tratamientos especiales) requieren un plazo de 90 días para contrapartes no vinculadas, y la regulación establece plazos de 180 días para el resto de los bienes y servicios.",
 "citas": [
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Punto 3.1. Normas de procedimiento. (parte 1)"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 13.2. Pagos de servicios que fueron o serán prestados o devengados a partir del 13/12/"
  }
 ],
 "respondible": false
}
```

(`respondible`: false · tool_calls: 16 · hit_tool_limit: True)

## Inventario de pasos + fidelidad runtime↔re-ejecución

| paso | tool | input | output_chars (runtime) | re-ejecutado | fiel |
|---|---|---|---|---|---|
| 1 | buscar_nodos | `{"consulta": "exigencia capital riesgo crédito", "limite": 10}` | 3349 | 3349 | SÍ |
| 2 | buscar_nodos | `{"consulta": "residente servicio asesoramiento contraparte vinculada mercado cambios ` | 3368 | 3368 | SÍ |
| 3 | ver_nodo | `{"id": "Operacion_calculo_de_capital_minimo"}` | 457 | 457 | SÍ |
| 4 | buscar_nodos | `{"consulta": "servicio asesoramiento contraparte vinculada 14 abril 2025", "limite": ` | 3602 | 3602 | SÍ |
| 5 | buscar_nodos | `{"consulta": "asesoramiento plazo acceso mercado cambios", "limite": 10}` | 3127 | 3127 | SÍ |
| 6 | ver_nodo | `{"id": "Restriccion_requisito_servicios_personales_de_contraparte_vinculada"}` | 641 | 641 | SÍ |
| 7 | buscar_nodos | `{"consulta": "asesoramiento 14 abril 2025 contraparte vinculada plazo", "limite": 10}` | 3600 | 3600 | SÍ |
| 8 | buscar_nodos | `{"consulta": "servicios asesoramiento a partir 14 abril", "limite": 10}` | 3942 | 3942 | SÍ |
| 9 | buscar_nodos | `{"consulta": "asesoramiento concepto S tratamiento especial plazo", "limite": 10}` | 3685 | 3685 | SÍ |
| 10 | buscar_nodos | `{"consulta": "servicios no comprendidos tratamiento especial plazo 180 días", "limite` | 3522 | 3522 | SÍ |
| 11 | ver_nodo | `{"id": "Restriccion_requisito_plazo_90_dias_para_servicio_no_comprendido"}` | 585 | 585 | SÍ |
| 12 | buscar_nodos | `{"consulta": "servicio no comprendido puntos 13.2.1 13.2.5 contraparte vinculada", "l` | 3545 | 3545 | SÍ |
| 13 | buscar_nodos | `{"consulta": "asesoramiento contraparte vinculada 14 abril 2025 180 días", "limite": ` | 3507 | 3507 | SÍ |
| 14 | buscar_nodos | `{"consulta": "servicios prestados a partir 14 abril 2025 contraparte vinculada", "lim` | 3745 | 3745 | SÍ |
| 15 | buscar_nodos | `{"consulta": "asesoramiento 180 días corridos prestación devengamiento", "limite": 10` | 3532 | 3532 | SÍ |
| 16 | buscar_nodos | `{"consulta": "concepto S asesoramiento plazo acceso cambios", "limite": 10}` | 3374 | 3374 | SÍ |

**Fidelidad: 16/16**.

## Apéndice — outputs completos re-ejecutados

### paso 1 — buscar_nodos {"consulta": "exigencia capital riesgo crédito", "limite": 10}

```json
{
 "consulta": "exigencia capital riesgo crédito",
 "total_con_match": 452,
 "resultados": [
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
   "id": "Obligacion_calcular_exigencia_capital_riesgo_credito_contraparte",
   "type": "Obligacion",
   "label": "Calcular exigencia capital riesgo crédito contraparte",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Las entidades deberán calcular la exigencia de capital por riesgo de crédito de contraparte de las operaciones con derivados –ya sean extrabursátiles (over-the-…"
  },
  {
   "id": "Obligacion_exigencia_por_riesgo_de_credito_de_contraparte_en_operaciones_con_derivados_extr",
   "type": "Obligacion",
   "label": "Cálculo de RCD",
   "tokens_matcheados": 3,
   "resumen_propiedades": "exigencia por riesgo de crédito de contraparte en operaciones con derivados extrabursátiles (over-the-counter, OTC), determinada conforme a lo establecido en el…"
  },
  {
   "id": "Obligacion_se_determinara_mensualmente_la_exigencia_de_capital_por_riesgo_operacional_cro_m",
   "type": "Obligacion",
   "label": "Informar CRO mensualmente",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Se determinará mensualmente la exigencia de capital por riesgo operacional (CRO) mediante la expresión CRO = BIC x ILM para entidades del Grupo 1"
  },
  {
   "id": "Obligacion_aplicar_exigencia_capital_por_riesgo_general_mercado_a_todas_posiciones_derivado",
   "type": "Obligacion",
   "label": "Cálculo riesgo general mercado",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La exigencia de capital por el riesgo general de mercado alcanza a todas las posiciones en instrumentos derivados -de la misma manera que también alcanza a las …"
  },
  {
   "id": "Operacion_calculo_de_exigencia_por_riesgo",
   "type": "Operacion",
   "label": "Cálculo exigencia riesgo crédito",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Cálculo de la exigencia por riesgo de crédito sin incluir el término INC mediante la fórmula: Código 70100000 (n) = k x 0,08 [ ∑(A x p) + ∑ (PFB x CCF x p) + ∑ …"
  },
  {
   "id": "Operacion_calculo_de_incrementos_de_exigencia_por_riesgo_de_credito",
   "type": "Operacion",
   "label": "Cálculo de incrementos de exigencia",
   "tokens_matcheados": 3,
   "resumen_propiedades": "tipo: cálculo de incrementos de exigencia por riesgo de crédito"
  },
  {
   "id": "Obligacion_calcular_exigencia_capital_por_riesgo",
   "type": "Obligacion",
   "label": "Calcular exigencia capital por riesgo",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La exigencia de capital por riesgo específico para un derivado de crédito de primer incumplimiento será el menor de la suma de las exigencias de capital por rie…"
  }
 ]
}
```

### paso 2 — buscar_nodos {"consulta": "residente servicio asesoramiento contraparte vinculada mercado cambios plazo", "limite": 10}

```json
{
 "consulta": "residente servicio asesoramiento contraparte vinculada mercado cambios plazo",
 "total_con_match": 296,
 "resultados": [
  {
   "id": "Obligacion_ingreso_y_liquidacion_en_mercado_de_cambios_en_30_dias_corridos_para_exportacion",
   "type": "Obligacion",
   "label": "Ingreso en plazo 30 días",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Ingreso y liquidación en mercado de cambios en 30 días corridos para exportaciones de bienes de posiciones arancelarias 1001.19.00, 1001.99.00, 1005.90.10, 1201…"
  },
  {
   "id": "Obligacion_ingreso_y_liquidacion_en_mercado_de_cambios_en_60_dias_corridos_para_operaciones",
   "type": "Obligacion",
   "label": "Ingreso en plazo 60 días",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Ingreso y liquidación en mercado de cambios en 60 días corridos para operaciones con contrapartes vinculadas y exportaciones de capítulos 26 y 71 según especifi…"
  },
  {
   "id": "Obligacion_ingreso_y_liquidacion_en_mercado_de_cambios_en_180_dias_corridos_para_el_resto_d",
   "type": "Obligacion",
   "label": "Ingreso en plazo 180 días",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Ingreso y liquidación en mercado de cambios en 180 días corridos para el resto de los bienes"
  },
  {
   "id": "Obligacion_ingreso_y_liquidacion_en_mercado_de_cambios_en_365_dias_corridos_para_operacione",
   "type": "Obligacion",
   "label": "Ingreso en plazo 365 días",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Ingreso y liquidación en mercado de cambios en 365 días corridos para operaciones en marco del régimen EXPORTA SIMPLE, independientemente del tipo de bien expor…"
  },
  {
   "id": "Restriccion_contraparte_no_residente_no_vinculada",
   "type": "Restriccion",
   "label": "Contraparte no residente no vinculada",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La contraparte del mencionado contrato es un no residente no vinculado con el residente que exportará los bienes y/o servicios"
  },
  {
   "id": "Restriccion_plazo_para_acceso_al_mercado_de_cambios",
   "type": "Restriccion",
   "label": "Plazo para acceso al mercado de cambios",
   "tokens_matcheados": 3,
   "resumen_propiedades": "El acceso al mercado de cambios se concrete dentro de los 10 (diez) días hábiles siguientes a la disponibilidad de los fondos por parte del no residente"
  },
  {
   "id": "Obligacion_los_anticipos_deberan_ser_ingresadas_y_liquidadas_en_el_mercado_de_cambios_dentr",
   "type": "Obligacion",
   "label": "Liquidación de anticipos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Los anticipos deberán ser ingresadas y liquidadas en el mercado de cambios dentro de los 20 días hábiles de la fecha de cobro o desembolso en el exterior"
  },
  {
   "id": "Operacion_endeudamiento_financiero_para_acceso_al_mercado_de_cambios",
   "type": "Operacion",
   "label": "Endeudamiento financiero",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: endeudamiento financiero para acceso al mercado de cambios"
  },
  {
   "id": "Obligacion_liquidar_en_mercado_cambios",
   "type": "Obligacion",
   "label": "Liquidar en mercado cambios",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El contravalor percibido deberá liquidarse en el mercado de cambios dentro de los 20 (veinte) días hábiles de la fecha de percepción en el exterior o en el país…"
  },
  {
   "id": "Operacion_liquidacion_en_el_mercado_de_cambios",
   "type": "Operacion",
   "label": "Liquidación mercado cambios",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: liquidación en el mercado de cambios"
  }
 ]
}
```

### paso 3 — ver_nodo {"id": "Operacion_calculo_de_capital_minimo"}

```json
{
 "id": "Operacion_calculo_de_capital_minimo",
 "type": "Operacion",
 "label": "Cálculo de exigencia por riesgo de crédito",
 "properties": {
  "tipo": "calculo de capital minimo",
  "description": "Determinación de la exigencia de capital por riesgo de crédito conforme a la fórmula C_RC = (k x 0,08 x APR_c) + INC"
 },
 "provenances": [
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Punto 3.1. Normas de procedimiento. (parte 1)"
  }
 ]
}
```

### paso 4 — buscar_nodos {"consulta": "servicio asesoramiento contraparte vinculada 14 abril 2025", "limite": 10}

```json
{
 "consulta": "servicio asesoramiento contraparte vinculada 14 abril 2025",
 "total_con_match": 65,
 "resultados": [
  {
   "id": "Restriccion_contraparte_no_residente_no_vinculada",
   "type": "Restriccion",
   "label": "Contraparte no residente no vinculada",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La contraparte del mencionado contrato es un no residente no vinculado con el residente que exportará los bienes y/o servicios"
  },
  {
   "id": "Operacion_operacion_con_contraparte_vinculada",
   "type": "Operacion",
   "label": "Operaciones con contrapartes vinculadas",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Operaciones en las que participan un residente y una contraparte que mantienen entre ellos los tipos de relaciones descriptos en el punto 1.2.2. de las normas '…"
  },
  {
   "id": "Obligacion_conformidad_previa_contraparte_vinculada",
   "type": "Obligacion",
   "label": "Conformidad previa contraparte vinculada",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Se requerirá la conformidad previa del BCRA cuando el acreedor sea una contraparte vinculada al deudor y el vencimiento de los intereses a pagar haya tenido lug…"
  },
  {
   "id": "Excepcion_pagos_a_contraparte_vinculada_sin_la_conformidad_previa_requerida_en_el_punto_3_",
   "type": "Excepcion",
   "label": "Excepción de conformidad previa para vinculadas",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Pagos a contraparte vinculada sin la conformidad previa requerida en el punto 3.3.3"
  },
  {
   "id": "Excepcion_pagos_de_endeudamiento_cuyo_acreedor_sea_contraparte_vinculada_sin_la_conformida",
   "type": "Excepcion",
   "label": "Excepción de conformidad para endeudamiento vinculado",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Pagos de endeudamiento cuyo acreedor sea contraparte vinculada sin la conformidad previa requerida en el punto 3.5.6"
  },
  {
   "id": "Restriccion_requisito_servicios_personales_de_contraparte_vinculada",
   "type": "Restriccion",
   "label": "Requisito: servicios personales de contraparte vinculada",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Concepto S24 - Otros servicios personales, culturales y recreativos prestado por contraparte vinculada al residente hasta 13/04/25, se concreta una vez transcur…"
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
  },
  {
   "id": "Obligacion_exigencia_por_riesgo_de_credito_de_contraparte_en_operaciones_con_derivados_extr",
   "type": "Obligacion",
   "label": "Cálculo de RCD",
   "tokens_matcheados": 1,
   "resumen_propiedades": "exigencia por riesgo de crédito de contraparte en operaciones con derivados extrabursátiles (over-the-counter, OTC), determinada conforme a lo establecido en el…"
  },
  {
   "id": "Operacion_operaciones_con_entidades_de_contraparte_central_calificadas",
   "type": "Operacion",
   "label": "Operaciones con QCCP",
   "tokens_matcheados": 1,
   "resumen_propiedades": "tipo: operaciones con entidades de contraparte central calificadas"
  }
 ]
}
```

### paso 5 — buscar_nodos {"consulta": "asesoramiento plazo acceso mercado cambios", "limite": 10}

```json
{
 "consulta": "asesoramiento plazo acceso mercado cambios",
 "total_con_match": 245,
 "resultados": [
  {
   "id": "Restriccion_plazo_para_acceso_al_mercado_de_cambios",
   "type": "Restriccion",
   "label": "Plazo para acceso al mercado de cambios",
   "tokens_matcheados": 4,
   "resumen_propiedades": "El acceso al mercado de cambios se concrete dentro de los 10 (diez) días hábiles siguientes a la disponibilidad de los fondos por parte del no residente"
  },
  {
   "id": "Obligacion_ingreso_y_liquidacion_en_mercado_de_cambios_en_30_dias_corridos_para_exportacion",
   "type": "Obligacion",
   "label": "Ingreso en plazo 30 días",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Ingreso y liquidación en mercado de cambios en 30 días corridos para exportaciones de bienes de posiciones arancelarias 1001.19.00, 1001.99.00, 1005.90.10, 1201…"
  },
  {
   "id": "Obligacion_ingreso_y_liquidacion_en_mercado_de_cambios_en_60_dias_corridos_para_operaciones",
   "type": "Obligacion",
   "label": "Ingreso en plazo 60 días",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Ingreso y liquidación en mercado de cambios en 60 días corridos para operaciones con contrapartes vinculadas y exportaciones de capítulos 26 y 71 según especifi…"
  },
  {
   "id": "Operacion_endeudamiento_financiero_para_acceso_al_mercado_de_cambios",
   "type": "Operacion",
   "label": "Endeudamiento financiero",
   "tokens_matcheados": 3,
   "resumen_propiedades": "tipo: endeudamiento financiero para acceso al mercado de cambios"
  },
  {
   "id": "Obligacion_ingreso_y_liquidacion_en_mercado_de_cambios_en_180_dias_corridos_para_el_resto_d",
   "type": "Obligacion",
   "label": "Ingreso en plazo 180 días",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Ingreso y liquidación en mercado de cambios en 180 días corridos para el resto de los bienes"
  },
  {
   "id": "Obligacion_ingreso_y_liquidacion_en_mercado_de_cambios_en_365_dias_corridos_para_operacione",
   "type": "Obligacion",
   "label": "Ingreso en plazo 365 días",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Ingreso y liquidación en mercado de cambios en 365 días corridos para operaciones en marco del régimen EXPORTA SIMPLE, independientemente del tipo de bien expor…"
  },
  {
   "id": "Operacion_acceso_a_mercado_de_cambios",
   "type": "Operacion",
   "label": "Acceso al mercado de cambios",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Acceder al mercado de cambios para realizar pagos al exterior"
  },
  {
   "id": "Operacion_acceso_a_mercado_de_cambios_para_cancelacion_de_lineas_de_credito",
   "type": "Operacion",
   "label": "Acceso al mercado de cambios",
   "tokens_matcheados": 3,
   "resumen_propiedades": "tipo: acceso a mercado de cambios para cancelación de líneas de crédito"
  },
  {
   "id": "Operacion_acceso_a_mercado_de_cambios_para_operaciones_de_egreso",
   "type": "Operacion",
   "label": "Acceso al mercado de cambios",
   "tokens_matcheados": 3,
   "resumen_propiedades": "tipo: acceso a mercado de cambios para operaciones de egreso"
  },
  {
   "id": "Operacion_acceso_al_mercado_de_cambios",
   "type": "Operacion",
   "label": "Acceso al mercado de cambios",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Dar acceso al mercado de cambios a personas humanas o jurídicas, patrimonios y otras universalidades"
  }
 ]
}
```

### paso 6 — ver_nodo {"id": "Restriccion_requisito_servicios_personales_de_contraparte_vinculada"}

```json
{
 "id": "Restriccion_requisito_servicios_personales_de_contraparte_vinculada",
 "type": "Restriccion",
 "label": "Requisito: servicios personales de contraparte vinculada",
 "properties": {
  "tipo": "limite_cualitativo",
  "description": "Concepto S24 - Otros servicios personales, culturales y recreativos prestado por contraparte vinculada al residente hasta 13/04/25, se concreta una vez transcurrido plazo de 90 días corridos desde fecha de prestación o devengamiento"
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 13.2. Pagos de servicios que fueron o serán prestados o devengados a partir del 13/12/"
  }
 ]
}
```

### paso 7 — buscar_nodos {"consulta": "asesoramiento 14 abril 2025 contraparte vinculada plazo", "limite": 10}

```json
{
 "consulta": "asesoramiento 14 abril 2025 contraparte vinculada plazo",
 "total_con_match": 134,
 "resultados": [
  {
   "id": "Restriccion_contraparte_no_residente_no_vinculada",
   "type": "Restriccion",
   "label": "Contraparte no residente no vinculada",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La contraparte del mencionado contrato es un no residente no vinculado con el residente que exportará los bienes y/o servicios"
  },
  {
   "id": "Operacion_operacion_con_contraparte_vinculada",
   "type": "Operacion",
   "label": "Operaciones con contrapartes vinculadas",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Operaciones en las que participan un residente y una contraparte que mantienen entre ellos los tipos de relaciones descriptos en el punto 1.2.2. de las normas '…"
  },
  {
   "id": "Obligacion_conformidad_previa_contraparte_vinculada",
   "type": "Obligacion",
   "label": "Conformidad previa contraparte vinculada",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Se requerirá la conformidad previa del BCRA cuando el acreedor sea una contraparte vinculada al deudor y el vencimiento de los intereses a pagar haya tenido lug…"
  },
  {
   "id": "Excepcion_pagos_a_contraparte_vinculada_sin_la_conformidad_previa_requerida_en_el_punto_3_",
   "type": "Excepcion",
   "label": "Excepción de conformidad previa para vinculadas",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Pagos a contraparte vinculada sin la conformidad previa requerida en el punto 3.3.3"
  },
  {
   "id": "Excepcion_pagos_de_endeudamiento_cuyo_acreedor_sea_contraparte_vinculada_sin_la_conformida",
   "type": "Excepcion",
   "label": "Excepción de conformidad para endeudamiento vinculado",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Pagos de endeudamiento cuyo acreedor sea contraparte vinculada sin la conformidad previa requerida en el punto 3.5.6"
  },
  {
   "id": "Restriccion_requisito_servicios_personales_de_contraparte_vinculada",
   "type": "Restriccion",
   "label": "Requisito: servicios personales de contraparte vinculada",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Concepto S24 - Otros servicios personales, culturales y recreativos prestado por contraparte vinculada al residente hasta 13/04/25, se concreta una vez transcur…"
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
  },
  {
   "id": "Obligacion_exigencia_por_riesgo_de_credito_de_contraparte_en_operaciones_con_derivados_extr",
   "type": "Obligacion",
   "label": "Cálculo de RCD",
   "tokens_matcheados": 1,
   "resumen_propiedades": "exigencia por riesgo de crédito de contraparte en operaciones con derivados extrabursátiles (over-the-counter, OTC), determinada conforme a lo establecido en el…"
  },
  {
   "id": "Operacion_operaciones_con_entidades_de_contraparte_central_calificadas",
   "type": "Operacion",
   "label": "Operaciones con QCCP",
   "tokens_matcheados": 1,
   "resumen_propiedades": "tipo: operaciones con entidades de contraparte central calificadas"
  }
 ]
}
```

### paso 8 — buscar_nodos {"consulta": "servicios asesoramiento a partir 14 abril", "limite": 10}

```json
{
 "consulta": "servicios asesoramiento a partir 14 abril",
 "total_con_match": 1228,
 "resultados": [
  {
   "id": "Restriccion_si_se_trata_de_servicios_que_fueron_o_seran_prestados_o_devengados_a_partir_del_",
   "type": "Restriccion",
   "label": "Servicios a partir de 13/12/23",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Si se trata de servicios que fueron o serán prestados o devengados a partir del 13/12/23, la entidad deberá constatar adicionalmente que el pago cumple las cond…"
  },
  {
   "id": "Restriccion_en_el_caso_de_deudas_comerciales_por_servicios_el_acceso_se_produce_a_partir_de_",
   "type": "Restriccion",
   "label": "Acceso a partir de fecha de vencimiento",
   "tokens_matcheados": 3,
   "resumen_propiedades": "En el caso de deudas comerciales por servicios el acceso se produce a partir de la fecha de vencimiento, en la medida que se verifique que la operación se encue…"
  },
  {
   "id": "Excepcion_para_cartas_de_credito_o_letras_avaladas_emitidas_u_otorgadas_a_partir_del_14_04",
   "type": "Excepcion",
   "label": "Excepción por pagos a la vista desde 14/04/25",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Para cartas de crédito o letras avaladas emitidas u otorgadas a partir del 14/04/25, también se admitirá que el pago se concretara a partir de la fecha estimada…"
  },
  {
   "id": "Excepcion_para_aquellas_otorgadas_a_partir_del_14_04_25_tambien_se_admitira_que_el_vencimi",
   "type": "Excepcion",
   "label": "Excepción para operaciones a partir del 14/04/25",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Para aquellas otorgadas a partir del 14/04/25, también se admitirá que el vencimiento sea compatible con la fecha estimada de embarque cuando corresponde a porc…"
  },
  {
   "id": "Obligacion_cuando_un_tercero_desarrolle_tareas_relativas_a_servicios_ofrecidos_por_los_suje",
   "type": "Obligacion",
   "label": "Responsabilidad de terceros",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Cuando un tercero desarrolle tareas relativas a servicios ofrecidos por los sujetos obligados o en su nombre, ambos serán responsables por el cumplimiento de la…"
  },
  {
   "id": "Obligacion_el_pago_garantizado_debia_ser_concretado_por_el_cliente_a_partir_de_la_fecha_que",
   "type": "Obligacion",
   "label": "Verificación de fecha de pago",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El pago garantizado debía ser concretado por el cliente a partir de la fecha que resultaba de adicionar el plazo en días corridos que le corresponde al servicio…"
  },
  {
   "id": "Restriccion_a_partir_del_comienzo_de_cada_uno_de_los_ultimos_cinco_anos_de_vida_de_cada_emis",
   "type": "Restriccion",
   "label": "Disminución de monto computable",
   "tokens_matcheados": 2,
   "resumen_propiedades": "A partir del comienzo de cada uno de los últimos cinco años de vida de cada emisión, el importe computable será disminuido en el 20 % del valor nominal emitido."
  },
  {
   "id": "Excepcion_la_clasificacion_se_verifica_a_partir_del_momento_en_que_no_habiendo_sido_rechaz",
   "type": "Excepcion",
   "label": "Excepción por rechazo de reclamo",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La clasificación se verifica a partir del momento en que, no habiendo sido rechazado el reclamo, se verifique la falta de pago del siniestro luego de vencidos l…"
  },
  {
   "id": "Obligacion_computo_como_inc_del_uso_del_cupo_ampliado_en_de_dicha_utilizacion_a_partir_de_q",
   "type": "Obligacion",
   "label": "Cómputo gradual de cupo ampliado",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Cómputo como INC del uso del cupo ampliado –en % de dicha utilización– a partir de que se hayan comenzado a utilizar económicamente las obras o el equipamiento …"
  },
  {
   "id": "Excepcion_cobros_por_prestacion_de_servicios_a_no_residente_por_vpu_rigi_quedan_exceptuado",
   "type": "Excepcion",
   "label": "Excepción servicios a no residente",
   "tokens_matcheados": 2,
   "resumen_propiedades": "cobros por prestación de servicios a no residente por VPU RIGI quedan exceptuados por totalidad del contravalor si servicio prestado o devengado a partir de pue…"
  }
 ]
}
```

### paso 9 — buscar_nodos {"consulta": "asesoramiento concepto S tratamiento especial plazo", "limite": 10}

```json
{
 "consulta": "asesoramiento concepto S tratamiento especial plazo",
 "total_con_match": 152,
 "resultados": [
  {
   "id": "Obligacion_en_caso_de_tratarse_una_operacion_del_concepto_s30_debia_ser_concretado_por_el_c",
   "type": "Obligacion",
   "label": "Plazo de pago para fletes",
   "tokens_matcheados": 2,
   "resumen_propiedades": "En caso de tratarse una operación del concepto S30, debía ser concretado por el cliente a partir de la fecha que resultaba de adicionar 15 (quince) días corrido…"
  },
  {
   "id": "Excepcion_en_los_casos_en_que_una_ccp_deje_de_calificar_como_qccp_durante_los_tres_meses_s",
   "type": "Excepcion",
   "label": "Excepción de mantenimiento de tratamiento",
   "tokens_matcheados": 2,
   "resumen_propiedades": "En los casos en que una CCP deje de calificar como QCCP, durante los tres meses siguientes las operaciones podrán mantener el tratamiento del punto 4.3.3.; fina…"
  },
  {
   "id": "Obligacion_para_las_refinanciaciones_otorgadas_por_primera_vez_dentro_del_ano_calendario_y_",
   "type": "Obligacion",
   "label": "Reclasificación única en tratamiento especial",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Para las refinanciaciones otorgadas por primera vez dentro del año calendario y una vez que se haya cancelado la primera cuota de dicha refinanciación, el clien…"
  },
  {
   "id": "Obligacion_en_el_caso_de_la_compra_se_utilizara_el_concepto_p12_otras_financiaciones_locale",
   "type": "Obligacion",
   "label": "Utilizar concepto P12",
   "tokens_matcheados": 1,
   "resumen_propiedades": "En el caso de la compra se utilizará el concepto 'P12. Otras financiaciones locales otorgadas por la entidad (excluida la financiación de exportaciones y tarjet…"
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

### paso 10 — buscar_nodos {"consulta": "servicios no comprendidos tratamiento especial plazo 180 días", "limite": 10}

```json
{
 "consulta": "servicios no comprendidos tratamiento especial plazo 180 días",
 "total_con_match": 560,
 "resultados": [
  {
   "id": "Restriccion_incurra_en_atrasos_de_hasta_180_dias_con_exclusion_de_los_deudores_comprendidos_",
   "type": "Restriccion",
   "label": "Atrasos hasta 180 días",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Incurra en atrasos de hasta 180 días, con exclusión de los deudores comprendidos en el punto 6.5.2.2."
  },
  {
   "id": "Obligacion_ingreso_y_liquidacion_en_mercado_de_cambios_en_180_dias_corridos_para_el_resto_d",
   "type": "Obligacion",
   "label": "Ingreso en plazo 180 días",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Ingreso y liquidación en mercado de cambios en 180 días corridos para el resto de los bienes"
  },
  {
   "id": "Restriccion_hasta_cinco_prorrogas_sucesivas_de_hasta_180_dias_corridos",
   "type": "Restriccion",
   "label": "Plazo máximo gestión de cobro",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Hasta cinco prórrogas sucesivas de hasta 180 días corridos"
  },
  {
   "id": "Restriccion_no_se_aplicara_el_plazo_minimo_de_veinte_dias_habiles_para_el_calculo_del_period",
   "type": "Restriccion",
   "label": "Límite de período de riesgo de margen",
   "tokens_matcheados": 3,
   "resumen_propiedades": "No se aplicará el plazo mínimo de veinte días hábiles para el cálculo del período de riesgo de margen (MPOR) de los conjuntos de neteo en los que se verifiquen …"
  },
  {
   "id": "Restriccion_extension_de_plazos_no_superior_a_545_dias_corridos_para_pagos_anticipados_de_bi",
   "type": "Restriccion",
   "label": "Plazo máximo ampliación causales ajenas",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Extensión de plazos no superior a 545 días corridos para pagos anticipados de bienes de capital o 365 días corridos para restantes pagos"
  },
  {
   "id": "Restriccion_plazo_vigencia_garantia_maximo_180_dias",
   "type": "Restriccion",
   "label": "Plazo vigencia garantía máximo 180 días",
   "tokens_matcheados": 3,
   "resumen_propiedades": "El plazo de vigencia de la garantía no excede los 180 (ciento ochenta) días corridos de la fecha de embarque de bienes locales o finalización de la prestación d…"
  },
  {
   "id": "Restriccion_requisito_plazo_90_dias_para_servicio_no_comprendido",
   "type": "Restriccion",
   "label": "Requisito: plazo 90 días para servicio no comprendido",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Servicio no comprendido en puntos 13.2.1 a 13.2.5 provisto por contraparte no vinculada al residente, pago se concreta a partir de la fecha de prestación o deve…"
  },
  {
   "id": "Obligacion_ingreso_y_liquidacion_en_mercado_de_cambios_en_30_dias_corridos_para_exportacion",
   "type": "Obligacion",
   "label": "Ingreso en plazo 30 días",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Ingreso y liquidación en mercado de cambios en 30 días corridos para exportaciones de bienes de posiciones arancelarias 1001.19.00, 1001.99.00, 1005.90.10, 1201…"
  },
  {
   "id": "Obligacion_ingreso_y_liquidacion_en_mercado_de_cambios_en_60_dias_corridos_para_operaciones",
   "type": "Obligacion",
   "label": "Ingreso en plazo 60 días",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Ingreso y liquidación en mercado de cambios en 60 días corridos para operaciones con contrapartes vinculadas y exportaciones de capítulos 26 y 71 según especifi…"
  },
  {
   "id": "Restriccion_operaciones_comerciales_con_brasil_no_podran_tener_plazo_de_pago_que_exceda_360_",
   "type": "Restriccion",
   "label": "Límite plazo pago Brasil",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Operaciones comerciales con Brasil no podrán tener plazo de pago que exceda 360 días"
  }
 ]
}
```

### paso 11 — ver_nodo {"id": "Restriccion_requisito_plazo_90_dias_para_servicio_no_comprendido"}

```json
{
 "id": "Restriccion_requisito_plazo_90_dias_para_servicio_no_comprendido",
 "type": "Restriccion",
 "label": "Requisito: plazo 90 días para servicio no comprendido",
 "properties": {
  "tipo": "limite_cualitativo",
  "description": "Servicio no comprendido en puntos 13.2.1 a 13.2.5 provisto por contraparte no vinculada al residente, pago se concreta a partir de la fecha de prestación o devengamiento del servicio"
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 13.2. Pagos de servicios que fueron o serán prestados o devengados a partir del 13/12/"
  }
 ]
}
```

### paso 12 — buscar_nodos {"consulta": "servicio no comprendido puntos 13.2.1 13.2.5 contraparte vinculada", "limite": 10}

```json
{
 "consulta": "servicio no comprendido puntos 13.2.1 13.2.5 contraparte vinculada",
 "total_con_match": 515,
 "resultados": [
  {
   "id": "Excepcion_emisiones_de_valores_comprendidos_en_puntos_3_6_1_3_a_3_6_1_5_que_no_generaron_d",
   "type": "Excepcion",
   "label": "Reestructuraciones deuda sin desembolsos",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Emisiones de valores comprendidos en puntos 3.6.1.3 a 3.6.1.5 que no generaron desembolsos por ser reestructuraciones de deudas, en medida que refinanciaciones …"
  },
  {
   "id": "Excepcion_el_pago_corresponde_a_servicios_comprendidos_en_los_puntos_13_2_1_o_13_2_2",
   "type": "Excepcion",
   "label": "Pago servicios comprendidos en puntos 13.2.1 o 13.2.2",
   "tokens_matcheados": 4,
   "resumen_propiedades": "El pago corresponde a servicios comprendidos en los puntos 13.2.1. o 13.2.2."
  },
  {
   "id": "Operacion_multiplicacion_de_exposicion_al_riesgo_de_contraparte_por_factor_1_5",
   "type": "Operacion",
   "label": "Aplicación de factor multiplicador",
   "tokens_matcheados": 3,
   "resumen_propiedades": "tipo: multiplicación de exposición al riesgo de contraparte por factor 1,5"
  },
  {
   "id": "Restriccion_contraparte_no_residente_no_vinculada",
   "type": "Restriccion",
   "label": "Contraparte no residente no vinculada",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La contraparte del mencionado contrato es un no residente no vinculado con el residente que exportará los bienes y/o servicios"
  },
  {
   "id": "Restriccion_titulos_valores_e_instrumentos_de_deuda_no_contemplados_en_los_puntos_8_4_1_19_y",
   "type": "Restriccion",
   "label": "Deducción títulos subordinados entidades",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Títulos valores e instrumentos de deuda no contemplados en los puntos 8.4.1.19. y 8.4.2., contractualmente subordinados a los demás pasivos, emitidos por otras …"
  },
  {
   "id": "Excepcion_exportaciones_de_bienes_de_proyecto_no_exportacion_estrategica_embarcadas_dentro",
   "type": "Excepcion",
   "label": "Excepción exportación no estratégica años 1-2",
   "tokens_matcheados": 3,
   "resumen_propiedades": "exportaciones de bienes de proyecto no Exportación Estratégica embarcadas dentro de 2 años quedan exceptuadas por 0% del contravalor"
  },
  {
   "id": "Obligacion_las_financiaciones_enunciadas_en_los_puntos_14_2_1_8_al_14_2_1_11_podran_ser_com",
   "type": "Obligacion",
   "label": "Verificación de condiciones para financiaciones",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Las financiaciones enunciadas en los puntos 14.2.1.8. al 14.2.1.11. podrán ser computadas como ingresadas y liquidadas en el mercado de cambios por un VPU adher…"
  },
  {
   "id": "Obligacion_tambien_se_podran_considerar_comprendidos_en_los_puntos_4_8_1_1_y_4_8_1_2_a_aque",
   "type": "Obligacion",
   "label": "Considerar pagos SML en disposiciones complementarias",
   "tokens_matcheados": 3,
   "resumen_propiedades": "También se podrán considerar comprendidos en los puntos 4.8.1.1. y 4.8.1.2. a aquellos pagos elegibles que se cursen por el Sistema de Moneda Locales (SML)"
  },
  {
   "id": "Restriccion_requisito_plazo_90_dias_para_servicio_no_comprendido",
   "type": "Restriccion",
   "label": "Requisito: plazo 90 días para servicio no comprendido",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Servicio no comprendido en puntos 13.2.1 a 13.2.5 provisto por contraparte no vinculada al residente, pago se concreta a partir de la fecha de prestación o deve…"
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

### paso 13 — buscar_nodos {"consulta": "asesoramiento contraparte vinculada 14 abril 2025 180 días", "limite": 10}

```json
{
 "consulta": "asesoramiento contraparte vinculada 14 abril 2025 180 días",
 "total_con_match": 96,
 "resultados": [
  {
   "id": "Restriccion_incurra_en_atrasos_de_hasta_180_dias_con_exclusion_de_los_deudores_comprendidos_",
   "type": "Restriccion",
   "label": "Atrasos hasta 180 días",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Incurra en atrasos de hasta 180 días, con exclusión de los deudores comprendidos en el punto 6.5.2.2."
  },
  {
   "id": "Obligacion_ingreso_y_liquidacion_en_mercado_de_cambios_en_180_dias_corridos_para_el_resto_d",
   "type": "Obligacion",
   "label": "Ingreso en plazo 180 días",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Ingreso y liquidación en mercado de cambios en 180 días corridos para el resto de los bienes"
  },
  {
   "id": "Restriccion_el_deudor_que_encontrandose_clasificado_en_esta_categoria_haya_refinanciado_su_d",
   "type": "Restriccion",
   "label": "Permanencia mínima 180 días",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El deudor que, encontrándose clasificado en esta categoría, haya refinanciado su deuda y recibido crédito adicional deberá permanecer en esta categoría por lo m…"
  },
  {
   "id": "Restriccion_hasta_cinco_prorrogas_sucesivas_de_hasta_180_dias_corridos",
   "type": "Restriccion",
   "label": "Plazo máximo gestión de cobro",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Hasta cinco prórrogas sucesivas de hasta 180 días corridos"
  },
  {
   "id": "Obligacion_permanecer_en_categoria_180_dias",
   "type": "Obligacion",
   "label": "Permanecer en categoría 180 días",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El deudor que, encontrándose clasificado en esta categoría, haya refinanciado su deuda y recibido crédito adicional deberá permanecer en esta categoría por lo m…"
  },
  {
   "id": "Restriccion_incurra_en_atrasos_recurrentes_incumplimiento_de_hasta_180_dias_respecto_de_cond",
   "type": "Restriccion",
   "label": "Atrasos recurrentes incumplimiento",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Incurra en atrasos recurrentes, incumplimiento de hasta 180 días respecto de condiciones contractuales o nulo movimiento en las cuentas."
  },
  {
   "id": "Obligacion_el_deudor_debera_permanecer_en_esta_categoria_por_lo_menos_180_dias_contados_des",
   "type": "Obligacion",
   "label": "Permanecer en categoría por 180 días",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El deudor deberá permanecer en esta categoría por lo menos 180 días contados desde la fecha en que se otorgó crédito adicional o desde que se celebró el acuerdo…"
  },
  {
   "id": "Restriccion_contraparte_no_residente_no_vinculada",
   "type": "Restriccion",
   "label": "Contraparte no residente no vinculada",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La contraparte del mencionado contrato es un no residente no vinculado con el residente que exportará los bienes y/o servicios"
  },
  {
   "id": "Restriccion_deudor_refinanciado_con_credito_adicional_debe_permanecer_minimo_180_dias_en_la_",
   "type": "Restriccion",
   "label": "Permanencia en categoría por 180 días",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Deudor refinanciado con crédito adicional debe permanecer mínimo 180 días en la categoría desde otorgamiento del crédito o celebración del acuerdo"
  },
  {
   "id": "Restriccion_el_cliente_se_encuentre_permanentemente_atrasado_en_el_pago_con_incumplimientos_",
   "type": "Restriccion",
   "label": "Atraso permanente superior a 180 días",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El cliente se encuentre permanentemente atrasado en el pago, con incumplimientos superiores a 180 días respecto de las condiciones contractuales."
  }
 ]
}
```

### paso 14 — buscar_nodos {"consulta": "servicios prestados a partir 14 abril 2025 contraparte vinculada", "limite": 10}

```json
{
 "consulta": "servicios prestados a partir 14 abril 2025 contraparte vinculada",
 "total_con_match": 1257,
 "resultados": [
  {
   "id": "Restriccion_si_se_trata_de_servicios_que_fueron_o_seran_prestados_o_devengados_a_partir_del_",
   "type": "Restriccion",
   "label": "Servicios a partir de 13/12/23",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Si se trata de servicios que fueron o serán prestados o devengados a partir del 13/12/23, la entidad deberá constatar adicionalmente que el pago cumple las cond…"
  },
  {
   "id": "Restriccion_en_el_caso_de_deudas_comerciales_por_servicios_el_acceso_se_produce_a_partir_de_",
   "type": "Restriccion",
   "label": "Acceso a partir de fecha de vencimiento",
   "tokens_matcheados": 3,
   "resumen_propiedades": "En el caso de deudas comerciales por servicios el acceso se produce a partir de la fecha de vencimiento, en la medida que se verifique que la operación se encue…"
  },
  {
   "id": "Excepcion_para_cartas_de_credito_o_letras_avaladas_emitidas_u_otorgadas_a_partir_del_14_04",
   "type": "Excepcion",
   "label": "Excepción por pagos a la vista desde 14/04/25",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Para cartas de crédito o letras avaladas emitidas u otorgadas a partir del 14/04/25, también se admitirá que el pago se concretara a partir de la fecha estimada…"
  },
  {
   "id": "Excepcion_pagos_a_contraparte_vinculada_sin_la_conformidad_previa_requerida_en_el_punto_3_",
   "type": "Excepcion",
   "label": "Excepción de conformidad previa para vinculadas",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Pagos a contraparte vinculada sin la conformidad previa requerida en el punto 3.3.3"
  },
  {
   "id": "Excepcion_para_aquellas_otorgadas_a_partir_del_14_04_25_tambien_se_admitira_que_el_vencimi",
   "type": "Excepcion",
   "label": "Excepción para operaciones a partir del 14/04/25",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Para aquellas otorgadas a partir del 14/04/25, también se admitirá que el vencimiento sea compatible con la fecha estimada de embarque cuando corresponde a porc…"
  },
  {
   "id": "Restriccion_garantia_vinculada_a_exportaciones_de_bienes_servicios",
   "type": "Restriccion",
   "label": "Garantía vinculada a exportaciones de bienes/servicios",
   "tokens_matcheados": 3,
   "resumen_propiedades": "El otorgamiento de la garantía fue un requisito para la concreción de un contrato de obras o provisión de bienes y/o servicios que implicaba, en forma directa o…"
  },
  {
   "id": "Restriccion_requisito_servicios_personales_de_contraparte_vinculada",
   "type": "Restriccion",
   "label": "Requisito: servicios personales de contraparte vinculada",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Concepto S24 - Otros servicios personales, culturales y recreativos prestado por contraparte vinculada al residente hasta 13/04/25, se concreta una vez transcur…"
  },
  {
   "id": "Obligacion_cuando_un_tercero_desarrolle_tareas_relativas_a_servicios_ofrecidos_por_los_suje",
   "type": "Obligacion",
   "label": "Responsabilidad de terceros",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Cuando un tercero desarrolle tareas relativas a servicios ofrecidos por los sujetos obligados o en su nombre, ambos serán responsables por el cumplimiento de la…"
  },
  {
   "id": "Obligacion_el_pago_garantizado_debia_ser_concretado_por_el_cliente_a_partir_de_la_fecha_que",
   "type": "Obligacion",
   "label": "Verificación de fecha de pago",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El pago garantizado debía ser concretado por el cliente a partir de la fecha que resultaba de adicionar el plazo en días corridos que le corresponde al servicio…"
  },
  {
   "id": "Operacion_financiacion_vinculada_a_comercio_exterior",
   "type": "Operacion",
   "label": "Operaciones comercio exterior",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: financiación vinculada a comercio exterior"
  }
 ]
}
```

### paso 15 — buscar_nodos {"consulta": "asesoramiento 180 días corridos prestación devengamiento", "limite": 10}

```json
{
 "consulta": "asesoramiento 180 días corridos prestación devengamiento",
 "total_con_match": 60,
 "resultados": [
  {
   "id": "Obligacion_ingreso_y_liquidacion_en_mercado_de_cambios_en_180_dias_corridos_para_el_resto_d",
   "type": "Obligacion",
   "label": "Ingreso en plazo 180 días",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Ingreso y liquidación en mercado de cambios en 180 días corridos para el resto de los bienes"
  },
  {
   "id": "Restriccion_hasta_cinco_prorrogas_sucesivas_de_hasta_180_dias_corridos",
   "type": "Restriccion",
   "label": "Plazo máximo gestión de cobro",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Hasta cinco prórrogas sucesivas de hasta 180 días corridos"
  },
  {
   "id": "Restriccion_incurra_en_atrasos_de_hasta_180_dias_con_exclusion_de_los_deudores_comprendidos_",
   "type": "Restriccion",
   "label": "Atrasos hasta 180 días",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Incurra en atrasos de hasta 180 días, con exclusión de los deudores comprendidos en el punto 6.5.2.2."
  },
  {
   "id": "Obligacion_ingreso_y_liquidacion_en_mercado_de_cambios_en_30_dias_corridos_para_exportacion",
   "type": "Obligacion",
   "label": "Ingreso en plazo 30 días",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Ingreso y liquidación en mercado de cambios en 30 días corridos para exportaciones de bienes de posiciones arancelarias 1001.19.00, 1001.99.00, 1005.90.10, 1201…"
  },
  {
   "id": "Obligacion_ingreso_y_liquidacion_en_mercado_de_cambios_en_60_dias_corridos_para_operaciones",
   "type": "Obligacion",
   "label": "Ingreso en plazo 60 días",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Ingreso y liquidación en mercado de cambios en 60 días corridos para operaciones con contrapartes vinculadas y exportaciones de capítulos 26 y 71 según especifi…"
  },
  {
   "id": "Obligacion_ingreso_y_liquidacion_en_mercado_de_cambios_en_365_dias_corridos_para_operacione",
   "type": "Obligacion",
   "label": "Ingreso en plazo 365 días",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Ingreso y liquidación en mercado de cambios en 365 días corridos para operaciones en marco del régimen EXPORTA SIMPLE, independientemente del tipo de bien expor…"
  },
  {
   "id": "Restriccion_el_deudor_que_encontrandose_clasificado_en_esta_categoria_haya_refinanciado_su_d",
   "type": "Restriccion",
   "label": "Permanencia mínima 180 días",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El deudor que, encontrándose clasificado en esta categoría, haya refinanciado su deuda y recibido crédito adicional deberá permanecer en esta categoría por lo m…"
  },
  {
   "id": "Obligacion_la_entidad_dispondra_de_30_dias_corridos_contados_desde_la_notificacion_para_for",
   "type": "Obligacion",
   "label": "Formular descargo ante SEFyC",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La entidad dispondrá de 30 días corridos contados desde la notificación para formular su descargo ante la SEFyC"
  },
  {
   "id": "Restriccion_se_concreta_dentro_de_los_60_sesenta_dias_corridos_previos_a_la_fecha_de_vencimi",
   "type": "Restriccion",
   "label": "Límite acceso 60 días previos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Se concreta dentro de los 60 (sesenta) días corridos previos a la fecha de vencimiento por un monto diario que no supere el 10% (diez por ciento) del monto que …"
  },
  {
   "id": "Obligacion_permanecer_en_categoria_180_dias",
   "type": "Obligacion",
   "label": "Permanecer en categoría 180 días",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El deudor que, encontrándose clasificado en esta categoría, haya refinanciado su deuda y recibido crédito adicional deberá permanecer en esta categoría por lo m…"
  }
 ]
}
```

### paso 16 — buscar_nodos {"consulta": "concepto S asesoramiento plazo acceso cambios", "limite": 10}

```json
{
 "consulta": "concepto S asesoramiento plazo acceso cambios",
 "total_con_match": 243,
 "resultados": [
  {
   "id": "Restriccion_plazo_para_acceso_al_mercado_de_cambios",
   "type": "Restriccion",
   "label": "Plazo para acceso al mercado de cambios",
   "tokens_matcheados": 3,
   "resumen_propiedades": "El acceso al mercado de cambios se concrete dentro de los 10 (diez) días hábiles siguientes a la disponibilidad de los fondos por parte del no residente"
  },
  {
   "id": "Operacion_acceso_al_mercado_de_cambios_simultaneo_con_liquidacion_de_fondos_en_concepto_de",
   "type": "Operacion",
   "label": "Acceso simultáneo con liquidación de anticipos de exportación",
   "tokens_matcheados": 3,
   "resumen_propiedades": "tipo: acceso al mercado de cambios simultáneo con liquidación de fondos en concepto de anticipos o prefinanciaciones de exportaciones"
  },
  {
   "id": "Obligacion_ingreso_y_liquidacion_en_mercado_de_cambios_en_30_dias_corridos_para_exportacion",
   "type": "Obligacion",
   "label": "Ingreso en plazo 30 días",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Ingreso y liquidación en mercado de cambios en 30 días corridos para exportaciones de bienes de posiciones arancelarias 1001.19.00, 1001.99.00, 1005.90.10, 1201…"
  },
  {
   "id": "Obligacion_ingreso_y_liquidacion_en_mercado_de_cambios_en_60_dias_corridos_para_operaciones",
   "type": "Obligacion",
   "label": "Ingreso en plazo 60 días",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Ingreso y liquidación en mercado de cambios en 60 días corridos para operaciones con contrapartes vinculadas y exportaciones de capítulos 26 y 71 según especifi…"
  },
  {
   "id": "Operacion_endeudamiento_financiero_para_acceso_al_mercado_de_cambios",
   "type": "Operacion",
   "label": "Endeudamiento financiero",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: endeudamiento financiero para acceso al mercado de cambios"
  },
  {
   "id": "Obligacion_en_caso_de_tratarse_una_operacion_del_concepto_s30_debia_ser_concretado_por_el_c",
   "type": "Obligacion",
   "label": "Plazo de pago para fletes",
   "tokens_matcheados": 2,
   "resumen_propiedades": "En caso de tratarse una operación del concepto S30, debía ser concretado por el cliente a partir de la fecha que resultaba de adicionar 15 (quince) días corrido…"
  },
  {
   "id": "Obligacion_ingreso_y_liquidacion_en_mercado_de_cambios_en_180_dias_corridos_para_el_resto_d",
   "type": "Obligacion",
   "label": "Ingreso en plazo 180 días",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Ingreso y liquidación en mercado de cambios en 180 días corridos para el resto de los bienes"
  },
  {
   "id": "Obligacion_ingreso_y_liquidacion_en_mercado_de_cambios_en_365_dias_corridos_para_operacione",
   "type": "Obligacion",
   "label": "Ingreso en plazo 365 días",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Ingreso y liquidación en mercado de cambios en 365 días corridos para operaciones en marco del régimen EXPORTA SIMPLE, independientemente del tipo de bien expor…"
  },
  {
   "id": "Operacion_acceso_a_mercado_de_cambios",
   "type": "Operacion",
   "label": "Acceso al mercado de cambios",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Acceder al mercado de cambios para realizar pagos al exterior"
  },
  {
   "id": "Operacion_acceso_a_mercado_de_cambios_para_cancelacion_de_lineas_de_credito",
   "type": "Operacion",
   "label": "Acceso al mercado de cambios",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: acceso a mercado de cambios para cancelación de líneas de crédito"
  }
 ]
}
```



---

# CQN2-014

## Respuesta final íntegra (trace.final_json)

```json
{
 "respuesta": "La excepción que rige para las refinanciaciones otorgadas a productores en el marco de la Ley de Emergencia Agropecuaria es que **no se considerarán como refinanciación** las refinanciaciones otorgadas a productores cuando ello resulte de la aplicación de disposiciones vinculadas a la Ley de Emergencia Agropecuaria. Esto significa que estas refinanciaciones quedan exceptuadas de la prohibición general de recurrir a nuevas financiaciones o refinanciaciones para cancelar obligaciones preexistentes.\n\nSin embargo, esta excepción tiene un límite importante: **a los fines de la clasificación, deberá tenerse en cuenta la mora en el atraso de sus obligaciones para el momento en que concluya la vigencia de la emergencia declarada en materia de Ley de Emergencia Agropecuaria**. Esto significa que aunque durante la vigencia de la emergencia estas refinanciaciones no se consideren como tales para efectos de clasificación, una vez que la emergencia concluya, se evaluará la mora existente en ese momento para determinar la clasificación del deudor.",
 "citas": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Punto 7.1. Criterio de clasificación."
  }
 ],
 "respondible": true
}
```

(`respondible`: true · tool_calls: 9 · hit_tool_limit: False)

## Inventario de pasos + fidelidad runtime↔re-ejecución

| paso | tool | input | output_chars (runtime) | re-ejecutado | fiel |
|---|---|---|---|---|---|
| 1 | buscar_nodos | `{"consulta": "clasificación deudores cartera consumo vivienda refinanciación", "limit` | 2796 | 2796 | SÍ |
| 2 | buscar_nodos | `{"consulta": "Ley Emergencia Agropecuaria refinanciación productores", "limite": 10}` | 3195 | 3195 | SÍ |
| 3 | ver_nodo | `{"id": "Excepcion_no_se_consideraran_como_refinanciacion_las_refinanciaciones_otorgad` | 733 | 733 | SÍ |
| 4 | ver_nodo | `{"id": "Excepcion_no_se_consideraran_dentro_de_ese_concepto_las_refinanciaciones_otor` | 547 | 547 | SÍ |
| 5 | ver_vecinos | `{"id": "Excepcion_no_se_consideraran_como_refinanciacion_las_refinanciaciones_otorgad` | 911 | 911 | SÍ |
| 6 | buscar_nodos | `{"consulta": "mora atraso obligaciones emergencia agropecuaria vigencia", "limite": 5` | 1857 | 1857 | SÍ |
| 7 | ver_nodo | `{"id": "Obligacion_a_los_fines_de_la_clasificacion_debera_tenerse_en_cuenta_la_mora_e` | 582 | 582 | SÍ |
| 8 | ver_nodo | `{"id": "Restriccion_no_se_podra_recurrir_a_nuevas_financiaciones_o_refinanciaciones_d` | 656 | 656 | SÍ |
| 9 | ver_vecinos | `{"id": "Obligacion_a_los_fines_de_la_clasificacion_debera_tenerse_en_cuenta_la_mora_e` | 576 | 576 | SÍ |

**Fidelidad: 9/9**.

## Apéndice — outputs completos re-ejecutados

### paso 1 — buscar_nodos {"consulta": "clasificación deudores cartera consumo vivienda refinanciación", "limite": 10}

```json
{
 "consulta": "clasificación deudores cartera consumo vivienda refinanciación",
 "total_con_match": 141,
 "resultados": [
  {
   "id": "Operacion_refinanciacion_de_los_deudores_de_cartera_de_consumo_o_vivienda",
   "type": "Operacion",
   "label": "Refinanciación de deudores",
   "tokens_matcheados": 5,
   "resumen_propiedades": "tipo: Refinanciación de los deudores de cartera de consumo o vivienda"
  },
  {
   "id": "Operacion_clasificacion_de_deudores_en_situacion_irregular",
   "type": "Operacion",
   "label": "Incremento cartera irregular",
   "tokens_matcheados": 3,
   "resumen_propiedades": "tipo: clasificación de deudores en situación irregular"
  },
  {
   "id": "Operacion_clasificacion_de_cartera",
   "type": "Operacion",
   "label": "Agrupación de cartera",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: clasificación de cartera"
  },
  {
   "id": "TextoOrdenado_to_clasificacion_deudores_actual_pdf",
   "type": "TextoOrdenado",
   "label": "Clasificación de Deudores",
   "tokens_matcheados": 2,
   "resumen_propiedades": "materia: clasificacion_deudores; archivo: TO_clasificacion_deudores_actual.pdf; version: vigente"
  },
  {
   "id": "EntidadFinanciera_deudor_cartera_comercial",
   "type": "EntidadFinanciera",
   "label": "Deudores cartera comercial",
   "tokens_matcheados": 2,
   "resumen_propiedades": "categoria: deudor cartera comercial"
  },
  {
   "id": "Operacion_otorgamiento_de_financiaciones_de_consumo_o_vivienda",
   "type": "Operacion",
   "label": "Financiaciones consumo vivienda",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: otorgamiento de financiaciones de consumo o vivienda"
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
  }
 ]
}
```

### paso 2 — buscar_nodos {"consulta": "Ley Emergencia Agropecuaria refinanciación productores", "limite": 10}

```json
{
 "consulta": "Ley Emergencia Agropecuaria refinanciación productores",
 "total_con_match": 30,
 "resultados": [
  {
   "id": "Excepcion_no_se_consideraran_como_refinanciacion_las_refinanciaciones_otorgadas_a_producto",
   "type": "Excepcion",
   "label": "Excepción refinanciación por Ley Emergencia Agropecuaria",
   "tokens_matcheados": 4,
   "resumen_propiedades": "No se considerarán como refinanciación las refinanciaciones otorgadas a productores cuando ello resulte de la aplicación de disposiciones vinculadas a la Ley de…"
  },
  {
   "id": "Excepcion_no_se_consideraran_dentro_de_ese_concepto_las_refinanciaciones_otorgadas_a_los_p",
   "type": "Excepcion",
   "label": "Excepción Ley Emergencia Agropecuaria",
   "tokens_matcheados": 3,
   "resumen_propiedades": "No se considerarán dentro de ese concepto las refinanciaciones otorgadas a los productores agropecuarios cuando ello resulte de la aplicación de disposiciones v…"
  },
  {
   "id": "Obligacion_a_los_fines_de_la_clasificacion_debera_tenerse_en_cuenta_la_mora_en_el_atraso_de",
   "type": "Obligacion",
   "label": "Considerar mora al vencimiento emergencia agropecuaria",
   "tokens_matcheados": 2,
   "resumen_propiedades": "A los fines de la clasificación, deberá tenerse en cuenta la mora en el atraso de sus obligaciones para el momento en que concluya la vigencia de la emergencia …"
  },
  {
   "id": "Comunicacion_ley_27444",
   "type": "Comunicacion",
   "label": "Com. Ley 27444",
   "tokens_matcheados": 1,
   "resumen_propiedades": "codigo: Ley-27444; tipo: normativa modificatoria; numero: 27444"
  },
  {
   "id": "Operacion_refinanciacion",
   "type": "Operacion",
   "label": "Refinanciación",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Acuerdo de refinanciación de obligaciones de pago periódico o de pago único"
  },
  {
   "id": "Operacion_acuerdo_de_refinanciacion",
   "type": "Operacion",
   "label": "Acuerdo de refinanciación",
   "tokens_matcheados": 1,
   "resumen_propiedades": "tipo: acuerdo de refinanciación"
  },
  {
   "id": "Restriccion_el_cliente_cuente_con_refinanciaciones_del_capital_adeudado_y_de_los_intereses_d",
   "type": "Restriccion",
   "label": "Refinanciación con quitas",
   "tokens_matcheados": 1,
   "resumen_propiedades": "El cliente cuente con refinanciaciones del capital adeudado y de los intereses devengados vinculadas a una insuficiente capacidad para su pago, con otorgamiento…"
  },
  {
   "id": "Operacion_refinanciacion_de_los_deudores_de_cartera_de_consumo_o_vivienda",
   "type": "Operacion",
   "label": "Refinanciación de deudores",
   "tokens_matcheados": 1,
   "resumen_propiedades": "tipo: Refinanciación de los deudores de cartera de consumo o vivienda"
  },
  {
   "id": "Restriccion_el_cliente_incurra_en_atrasos_superiores_a_un_ano_cuente_con_refinanciacion_del_",
   "type": "Restriccion",
   "label": "Atrasos superiores a un año",
   "tokens_matcheados": 1,
   "resumen_propiedades": "El cliente incurra en atrasos superiores a un año, cuente con refinanciación del capital y sus intereses."
  },
  {
   "id": "Restriccion_haya_refinanciado_su_deuda_con_otorgamiento_de_quitas_de_capital_de_acuerdo_con_",
   "type": "Restriccion",
   "label": "Refinanciación con quitas capital",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Haya refinanciado su deuda con otorgamiento de quitas de capital de acuerdo con la metodología establecida."
  }
 ]
}
```

### paso 3 — ver_nodo {"id": "Excepcion_no_se_consideraran_como_refinanciacion_las_refinanciaciones_otorgadas_a_producto"}

```json
{
 "id": "Excepcion_no_se_consideraran_como_refinanciacion_las_refinanciaciones_otorgadas_a_producto",
 "type": "Excepcion",
 "label": "Excepción refinanciación por Ley Emergencia Agropecuaria",
 "properties": {
  "descripcion": "No se considerarán como refinanciación las refinanciaciones otorgadas a productores cuando ello resulte de la aplicación de disposiciones vinculadas a la Ley de Emergencia Agropecuaria, sin perjuicio de lo cual, a los fines de la clasificación, deberá tenerse en cuenta la mora en el atraso de sus obligaciones para el momento en que concluya la vigencia de la emergencia declarada."
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Punto 7.1. Criterio de clasificación."
  }
 ]
}
```

### paso 4 — ver_nodo {"id": "Excepcion_no_se_consideraran_dentro_de_ese_concepto_las_refinanciaciones_otorgadas_a_los_p"}

```json
{
 "id": "Excepcion_no_se_consideraran_dentro_de_ese_concepto_las_refinanciaciones_otorgadas_a_los_p",
 "type": "Excepcion",
 "label": "Excepción Ley Emergencia Agropecuaria",
 "properties": {
  "descripcion": "No se considerarán dentro de ese concepto las refinanciaciones otorgadas a los productores agropecuarios cuando ello resulte de la aplicación de disposiciones vinculadas a la Ley de Emergencia Agropecuaria."
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Punto 6.5. Niveles de clasificación. (parte 1)"
  }
 ]
}
```

### paso 5 — ver_vecinos {"id": "Excepcion_no_se_consideraran_como_refinanciacion_las_refinanciaciones_otorgadas_a_producto", "direccion": "ambas"}

```json
{
 "id": "Excepcion_no_se_consideraran_como_refinanciacion_las_refinanciaciones_otorgadas_a_producto",
 "label": "Excepción refinanciación por Ley Emergencia Agropecuaria",
 "n_salientes_total": 2,
 "n_entrantes_total": 0,
 "salientes": [
  {
   "relation": "establecida_en",
   "vecino_id": "TextoOrdenado_to_clasificacion_deudores_actual_pdf",
   "vecino_label": "Clasificación de Deudores",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "Punto 7.1. Criterio de clasificación."
    }
   ]
  },
  {
   "relation": "exceptua",
   "vecino_id": "Restriccion_no_se_podra_recurrir_a_nuevas_financiaciones_o_refinanciaciones_destinadas_a_can",
   "vecino_label": "Prohibición refinanciación para cancelar obligaciones",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "Punto 7.1. Criterio de clasificación."
    }
   ]
  }
 ],
 "salientes_truncado": false,
 "entrantes": [],
 "entrantes_truncado": false
}
```

### paso 6 — buscar_nodos {"consulta": "mora atraso obligaciones emergencia agropecuaria vigencia", "limite": 5}

```json
{
 "consulta": "mora atraso obligaciones emergencia agropecuaria vigencia",
 "total_con_match": 46,
 "resultados": [
  {
   "id": "Obligacion_a_los_fines_de_la_clasificacion_debera_tenerse_en_cuenta_la_mora_en_el_atraso_de",
   "type": "Obligacion",
   "label": "Considerar mora al vencimiento emergencia agropecuaria",
   "tokens_matcheados": 4,
   "resumen_propiedades": "A los fines de la clasificación, deberá tenerse en cuenta la mora en el atraso de sus obligaciones para el momento en que concluya la vigencia de la emergencia …"
  },
  {
   "id": "Restriccion_comprende_los_clientes_que_atienden_en_forma_puntual_el_pago_de_sus_obligaciones",
   "type": "Restriccion",
   "label": "Límite de atraso en situación normal",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Comprende los clientes que atienden en forma puntual el pago de sus obligaciones o con atrasos que no superan los 31 días"
  },
  {
   "id": "Excepcion_no_se_consideraran_dentro_de_ese_concepto_las_refinanciaciones_otorgadas_a_los_p",
   "type": "Excepcion",
   "label": "Excepción Ley Emergencia Agropecuaria",
   "tokens_matcheados": 2,
   "resumen_propiedades": "No se considerarán dentro de ese concepto las refinanciaciones otorgadas a los productores agropecuarios cuando ello resulte de la aplicación de disposiciones v…"
  },
  {
   "id": "Excepcion_no_se_consideraran_como_refinanciacion_las_refinanciaciones_otorgadas_a_producto",
   "type": "Excepcion",
   "label": "Excepción refinanciación por Ley Emergencia Agropecuaria",
   "tokens_matcheados": 2,
   "resumen_propiedades": "No se considerarán como refinanciación las refinanciaciones otorgadas a productores cuando ello resulte de la aplicación de disposiciones vinculadas a la Ley de…"
  },
  {
   "id": "Operacion_clasificacion_de_deudor_segun_mora",
   "type": "Operacion",
   "label": "Clasificación de deudor",
   "tokens_matcheados": 1,
   "resumen_propiedades": "tipo: clasificación de deudor según mora"
  }
 ]
}
```

### paso 7 — ver_nodo {"id": "Obligacion_a_los_fines_de_la_clasificacion_debera_tenerse_en_cuenta_la_mora_en_el_atraso_de"}

```json
{
 "id": "Obligacion_a_los_fines_de_la_clasificacion_debera_tenerse_en_cuenta_la_mora_en_el_atraso_de",
 "type": "Obligacion",
 "label": "Considerar mora al vencimiento emergencia agropecuaria",
 "properties": {
  "descripcion": "A los fines de la clasificación, deberá tenerse en cuenta la mora en el atraso de sus obligaciones para el momento en que concluya la vigencia de la emergencia declarada en materia de Ley de Emergencia Agropecuaria.",
  "tipo": "otra"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Punto 7.1. Criterio de clasificación."
  }
 ]
}
```

### paso 8 — ver_nodo {"id": "Restriccion_no_se_podra_recurrir_a_nuevas_financiaciones_o_refinanciaciones_destinadas_a_can"}

```json
{
 "id": "Restriccion_no_se_podra_recurrir_a_nuevas_financiaciones_o_refinanciaciones_destinadas_a_can",
 "type": "Restriccion",
 "label": "Prohibición refinanciación para cancelar obligaciones",
 "properties": {
  "descripcion": "No se podrá recurrir a nuevas financiaciones o refinanciaciones destinadas a cancelar obligaciones preexistentes, cualquiera sea la modalidad (prórrogas, esperas, ampliaciones de plazo o márgenes, disminuciones en importes de cuotas o pagos, renovaciones, reestructuraciones, etc.)",
  "tipo": "prohibicion"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Punto 7.1. Criterio de clasificación."
  }
 ]
}
```

### paso 9 — ver_vecinos {"id": "Obligacion_a_los_fines_de_la_clasificacion_debera_tenerse_en_cuenta_la_mora_en_el_atraso_de", "direccion": "ambas"}

```json
{
 "id": "Obligacion_a_los_fines_de_la_clasificacion_debera_tenerse_en_cuenta_la_mora_en_el_atraso_de",
 "label": "Considerar mora al vencimiento emergencia agropecuaria",
 "n_salientes_total": 1,
 "n_entrantes_total": 0,
 "salientes": [
  {
   "relation": "establecida_en",
   "vecino_id": "TextoOrdenado_to_clasificacion_deudores_actual_pdf",
   "vecino_label": "Clasificación de Deudores",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "Punto 7.1. Criterio de clasificación."
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

# CQN2-015

## Respuesta final íntegra (trace.final_json)

```json
{
 "respuesta": "No se encontró en el Knowledge Graph información que especifique explícitamente cuál es el piso de ponderador de riesgo que rige para exposiciones con deudores no calificados, ni qué exposiciones están exceptuadas de ese piso. Aunque se identificaron múltiples restricciones sobre ponderadores de riesgo para diferentes tipos de exposiciones (MIPYME, personas humanas, entidades financieras, titulizaciones, etc.), no se localizó la regla general aplicable a deudores sin calificación crediticia.",
 "citas": [],
 "respondible": false
}
```

(`respondible`: false · tool_calls: 15 · hit_tool_limit: True)

## Inventario de pasos + fidelidad runtime↔re-ejecución

| paso | tool | input | output_chars (runtime) | re-ejecutado | fiel |
|---|---|---|---|---|---|
| 1 | buscar_nodos | `{"consulta": "capital mínimo riesgo crédito ponderador deudor no calificado", "limite` | 3458 | 3458 | SÍ |
| 2 | buscar_nodos | `{"consulta": "piso ponderador riesgo exposición deudor", "limite": 10}` | 2938 | 2938 | SÍ |
| 3 | buscar_nodos | `{"consulta": "deudor no calificado ponderador piso", "limite": 10}` | 3520 | 3520 | SÍ |
| 4 | buscar_nodos | `{"consulta": "exposición deudor no calificado 100%", "limite": 10}` | 3356 | 3356 | SÍ |
| 5 | buscar_nodos | `{"consulta": "ponderador riesgo 100 deudor calificado", "limite": 10}` | 3055 | 3055 | SÍ |
| 6 | buscar_nodos | `{"consulta": "ponderador 100% exposición crédito", "limite": 10}` | 2889 | 2889 | SÍ |
| 7 | buscar_nodos | `{"consulta": "no calificado ponderador", "limite": 10}` | 3567 | 3567 | SÍ |
| 8 | ver_nodo | `{"id": "Operacion_calculo_de_exigencia_de_capital_minimo_por_riesgo_de_credito"}` | 367 | 367 | SÍ |
| 9 | buscar_nodos | `{"consulta": "ponderador riesgo exposición deudor sin calificación", "limite": 10}` | 3140 | 3140 | SÍ |
| 10 | buscar_nodos | `{"consulta": "piso 100 ponderador riesgo", "limite": 10}` | 3042 | 3042 | SÍ |
| 11 | buscar_nodos | `{"consulta": "ponderador mínimo 100 exposición", "limite": 10}` | 3151 | 3151 | SÍ |
| 12 | buscar_nodos | `{"consulta": "exposición sin rating calificación ponderador", "limite": 10}` | 3230 | 3230 | SÍ |
| 13 | buscar_nodos | `{"consulta": "deudor sin calificación 100", "limite": 10}` | 2580 | 2580 | SÍ |
| 14 | buscar_nodos | `{"consulta": "ponderador por defecto estándar riesgo crédito", "limite": 10}` | 3163 | 3163 | SÍ |
| 15 | buscar_nodos | `{"consulta": "ponderador 100% empresas personas", "limite": 10}` | 2570 | 2570 | SÍ |

**Fidelidad: 15/15**.

## Apéndice — outputs completos re-ejecutados

### paso 1 — buscar_nodos {"consulta": "capital mínimo riesgo crédito ponderador deudor no calificado", "limite": 10}

```json
{
 "consulta": "capital mínimo riesgo crédito ponderador deudor no calificado",
 "total_con_match": 838,
 "resultados": [
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
   "id": "Restriccion_exposiciones_o_tramos_no_cubiertos_por_coberturas_del_riesgo_de_credito_con_prev",
   "type": "Restriccion",
   "label": "Ponderador exposiciones sin cobertura previsión menor 20%",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Exposiciones o tramos no cubiertos por coberturas del riesgo de crédito con previsiones específicas menores al 20% del saldo pendiente: 150"
  },
  {
   "id": "Restriccion_la_parte_de_la_exposicion_cubierta_recibira_el_ponderador_de_riesgo_correspondie",
   "type": "Restriccion",
   "label": "Ponderador mínimo 20%",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La parte de la exposición cubierta recibirá el ponderador de riesgo correspondiente al activo recibido en garantía, pero estará sujeta a un mínimo del 20% –salv…"
  },
  {
   "id": "Restriccion_la_exposicion_presente_respecto_de_la_contraparte_no_puede_tener_un_valor_negati",
   "type": "Restriccion",
   "label": "Crédito de riesgo no negativo",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La exposición presente respecto de la contraparte no puede tener un valor negativo"
  },
  {
   "id": "Excepcion_el_ponderador_de_riesgo_de_la_parte_de_la_exposicion_cubierta_podra_ser_inferior",
   "type": "Excepcion",
   "label": "Excepción ponderador mínimo 20%",
   "tokens_matcheados": 3,
   "resumen_propiedades": "El ponderador de riesgo de la parte de la exposición cubierta podrá ser inferior al 20% en los siguientes casos: operaciones de pase con participante esencial, …"
  },
  {
   "id": "Restriccion_el_computo_del_requerimiento_de_capital_por_aporte_al_fondo_de_garantia_utiliza_",
   "type": "Restriccion",
   "label": "Ponderador riesgo fondo garantía",
   "tokens_matcheados": 3,
   "resumen_propiedades": "El cómputo del requerimiento de capital por aporte al fondo de garantía utiliza un ponderador de riesgo del 2%"
  },
  {
   "id": "Restriccion_capital_minimo_riesgo_tipo_cambio",
   "type": "Restriccion",
   "label": "Capital mínimo riesgo tipo cambio",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La exigencia de capital será el 8% de la posición neta total"
  },
  {
   "id": "Restriccion_las_entidades_financieras_deberan_aplicar_un_ponderador_de_riesgo_del_1250_a_sus",
   "type": "Restriccion",
   "label": "Ponderador riesgo CCP no calificada",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Las entidades financieras deberán aplicar un ponderador de riesgo del 1250% a sus aportes a los fondos de garantía para incumplimientos de las CCP que no califi…"
  },
  {
   "id": "Restriccion_el_periodo_de_vigencia_del_derivado_de_credito_no_podra_ser_inferior_a_cualquier",
   "type": "Restriccion",
   "label": "Período mínimo de vigencia derivados",
   "tokens_matcheados": 3,
   "resumen_propiedades": "El período de vigencia del derivado de crédito no podrá ser inferior a cualquier período de gracia necesario para poder determinar que efectivamente se ha produ…"
  }
 ]
}
```

### paso 2 — buscar_nodos {"consulta": "piso ponderador riesgo exposición deudor", "limite": 10}

```json
{
 "consulta": "piso ponderador riesgo exposición deudor",
 "total_con_match": 283,
 "resultados": [
  {
   "id": "Restriccion_la_parte_de_la_exposicion_cubierta_recibira_el_ponderador_de_riesgo_correspondie",
   "type": "Restriccion",
   "label": "Ponderador mínimo 20%",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La parte de la exposición cubierta recibirá el ponderador de riesgo correspondiente al activo recibido en garantía, pero estará sujeta a un mínimo del 20% –salv…"
  },
  {
   "id": "Excepcion_el_ponderador_de_riesgo_de_la_parte_de_la_exposicion_cubierta_podra_ser_inferior",
   "type": "Excepcion",
   "label": "Excepción ponderador mínimo 20%",
   "tokens_matcheados": 3,
   "resumen_propiedades": "El ponderador de riesgo de la parte de la exposición cubierta podrá ser inferior al 20% en los siguientes casos: operaciones de pase con participante esencial, …"
  },
  {
   "id": "Restriccion_exposicion_al_bcra_en_pesos_con_ponderador_de_riesgo_0",
   "type": "Restriccion",
   "label": "Ponderador exposición BCRA pesos",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Exposición al BCRA en pesos con ponderador de riesgo 0%"
  },
  {
   "id": "Restriccion_exposicion_a_gobiernos_locales_en_pesos_con_ponderador_de_riesgo_0",
   "type": "Restriccion",
   "label": "Ponderador exposición gobiernos pesos",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Exposición a gobiernos locales en pesos con ponderador de riesgo 0%"
  },
  {
   "id": "Restriccion_oro_amonedado_o_en_barras_con_ponderador_de_riesgo_0",
   "type": "Restriccion",
   "label": "Ponderador riesgo oro",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Oro amonedado o en barras con ponderador de riesgo 0%"
  },
  {
   "id": "Restriccion_exposicion_a_bmd_que_cumplen_criterios_basilea_con_ponderador_0",
   "type": "Restriccion",
   "label": "Ponderador BMD Basilea",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Exposición a BMD que cumplen criterios Basilea con ponderador 0%"
  },
  {
   "id": "Restriccion_se_aplicara_el_ponderador_de_riesgo_del_85_para_las_exposiciones_a_mipyme",
   "type": "Restriccion",
   "label": "Ponderador riesgo MIPYME",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Se aplicará el ponderador de riesgo del 85% para las exposiciones a Mipyme"
  },
  {
   "id": "Restriccion_ponderador_de_riesgo_1250",
   "type": "Restriccion",
   "label": "Ponderador de riesgo 1250%",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Si D es menor o igual a K, el ponderador será de 1250%."
  },
  {
   "id": "Restriccion_empresas_con_grado_de_inversion_con_ponderador_de_riesgo_65",
   "type": "Restriccion",
   "label": "Ponderador empresas inversión",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Empresas con grado de inversión con ponderador de riesgo 65%"
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

### paso 3 — buscar_nodos {"consulta": "deudor no calificado ponderador piso", "limite": 10}

```json
{
 "consulta": "deudor no calificado ponderador piso",
 "total_con_match": 449,
 "resultados": [
  {
   "id": "Restriccion_las_entidades_financieras_deberan_aplicar_un_ponderador_de_riesgo_del_1250_a_sus",
   "type": "Restriccion",
   "label": "Ponderador riesgo CCP no calificada",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Las entidades financieras deberán aplicar un ponderador de riesgo del 1250% a sus aportes a los fondos de garantía para incumplimientos de las CCP que no califi…"
  },
  {
   "id": "Restriccion_exposiciones_a_instrumentos_deuda_subordinada_e_instrumentos_de_capital_que_no_r",
   "type": "Restriccion",
   "label": "Ponderador deuda subordinada grupo 1",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Exposiciones a instrumentos: Deuda subordinada e instrumentos de capital que no reúnen las características para ser considerados como acciones: 150"
  },
  {
   "id": "Restriccion_apoyo_crediticio_que_no_supere_55_del_valor_del_inmueble_residencial_con_pondera",
   "type": "Restriccion",
   "label": "Ponderador hipotecario residencial 55%",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Apoyo crediticio que no supere 55% del valor del inmueble residencial con ponderador 20%"
  },
  {
   "id": "Restriccion_financiaciones_a_sector_publico_no_financiero_con_ponderador_de_riesgo_0",
   "type": "Restriccion",
   "label": "Ponderador financiación sector público",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Financiaciones a sector público no financiero con ponderador de riesgo 0%"
  },
  {
   "id": "Restriccion_el_ponderador_resultante_estara_sujeto_a_un_minimo_de_15_para_titulizaciones_que",
   "type": "Restriccion",
   "label": "Ponderador mínimo titulizaciones no STC",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El ponderador resultante estará sujeto a un mínimo de 15% para titulizaciones que no cumplan con los criterios STC"
  },
  {
   "id": "Restriccion_cuotas_de_financiaciones_no_deben_exceder_del_30_de_ingresos_del_deudor_al_momen",
   "type": "Restriccion",
   "label": "Límite cuota financiaciones sector público",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Cuotas de financiaciones no deben exceder del 30% de ingresos del deudor al momento de acuerdos"
  },
  {
   "id": "Obligacion_el_ponderador_de_riesgo_de_exposiciones_a_entidades_financieras_no_puede_ser_inf",
   "type": "Obligacion",
   "label": "Aplicar ponderador jurisdicción contraparte",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El ponderador de riesgo de exposiciones a entidades financieras no puede ser inferior al ponderador aplicable a jurisdicción de constitución de contraparte cuan…"
  },
  {
   "id": "Restriccion_no_prorrateo_de_ponderador_en_fondos_mixtos",
   "type": "Restriccion",
   "label": "No prorrateo de ponderador en fondos mixtos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Si un fondo de garantía constituido para hacer frente a incumplimientos respalda a productos sujetos a riesgo de liquidación y a productos expuestos a riesgo de…"
  },
  {
   "id": "Restriccion_operaciones_al_contado_a_liquidar_no_fallidas_0",
   "type": "Restriccion",
   "label": "Ponderador operaciones contado liquidar no fallidas",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Operaciones al contado a liquidar no fallidas: 0"
  },
  {
   "id": "Restriccion_ponderador_de_riesgo_para_exposiciones_no_protegidas",
   "type": "Restriccion",
   "label": "Ponderador de riesgo para exposiciones no protegidas",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Cuando la entidad financiera sea cliente del miembro compensador y no se cumplan los requisitos de protección, la exposición con el miembro compensador, incluid…"
  }
 ]
}
```

### paso 4 — buscar_nodos {"consulta": "exposición deudor no calificado 100%", "limite": 10}

```json
{
 "consulta": "exposición deudor no calificado 100%",
 "total_con_match": 436,
 "resultados": [
  {
   "id": "Restriccion_la_exposicion_presente_respecto_de_la_contraparte_no_puede_tener_un_valor_negati",
   "type": "Restriccion",
   "label": "Crédito de riesgo no negativo",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La exposición presente respecto de la contraparte no puede tener un valor negativo"
  },
  {
   "id": "Restriccion_la_exposicion_maxima_frente_a_una_misma_contraparte_individual_mipyme_no_debera_",
   "type": "Restriccion",
   "label": "Límite máximo exposición Mipyme",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La exposición máxima frente a una misma contraparte individual Mipyme no deberá superar, al momento del acuerdo, el importe equivalente en pesos a €1.000.000 al…"
  },
  {
   "id": "Restriccion_cuotas_de_financiaciones_no_deben_exceder_del_30_de_ingresos_del_deudor_al_momen",
   "type": "Restriccion",
   "label": "Límite cuota financiaciones sector público",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Cuotas de financiaciones no deben exceder del 30% de ingresos del deudor al momento de acuerdos"
  },
  {
   "id": "Restriccion_valor_adeudado_no_supere_equivalente_de_usd_100_000_cuando_se_usa_companias_de_s",
   "type": "Restriccion",
   "label": "Límite monto para gestión sin entidad recupero",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Valor adeudado no supere equivalente de USD 100.000 cuando se usa compañías de seguro o agencias de recupero"
  },
  {
   "id": "Obligacion_el_cr_para_operaciones_con_margen_se_define_como_la_mayor_exposicion_que_no_alca",
   "type": "Obligacion",
   "label": "Calcular crédito de riesgo operaciones con margen",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El CR para operaciones con margen se define como la mayor exposición que no alcanza a activar un aumento del VM, determinada por la expresión CR = máx. (V - C; …"
  },
  {
   "id": "Restriccion_la_exposicion_maxima_frente_a_una_misma_contraparte_individual_no_debera_superar",
   "type": "Restriccion",
   "label": "Límite máximo exposición personas humanas consumo",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La exposición máxima frente a una misma contraparte individual no deberá superar, al momento del acuerdo, el importe equivalente a 75 veces el Salario Mínimo, V…"
  },
  {
   "id": "Excepcion_el_tratamiento_otorgado_a_la_exposicion_al_sector_publico_no_financiero_no_sera_",
   "type": "Excepcion",
   "label": "No aplicación para contrapartes con tratamiento sector privado",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El tratamiento otorgado a la exposición al sector público no financiero no será de aplicación en las operaciones con contrapartes a las cuales el BCRA les haya …"
  },
  {
   "id": "EntidadFinanciera_deudor",
   "type": "EntidadFinanciera",
   "label": "Deudores",
   "tokens_matcheados": 1,
   "resumen_propiedades": "categoria: deudor"
  },
  {
   "id": "EntidadFinanciera_no_residente",
   "type": "EntidadFinanciera",
   "label": "No residentes",
   "tokens_matcheados": 1,
   "resumen_propiedades": "categoria: clientes no residentes"
  },
  {
   "id": "Excepcion_importador_demuestra_gestion_de_cobro_a_traves_de_reclamos_a_companias_de_seguro",
   "type": "Excepcion",
   "label": "Deudor moroso",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Importador demuestra gestión de cobro a través de reclamos a compañías de seguro de crédito o agencias de recupero, o mantiene acciones judiciales contra el pro…"
  }
 ]
}
```

### paso 5 — buscar_nodos {"consulta": "ponderador riesgo 100 deudor calificado", "limite": 10}

```json
{
 "consulta": "ponderador riesgo 100 deudor calificado",
 "total_con_match": 255,
 "resultados": [
  {
   "id": "Restriccion_la_parte_de_la_exposicion_cubierta_recibira_el_ponderador_de_riesgo_correspondie",
   "type": "Restriccion",
   "label": "Ponderador mínimo 20%",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La parte de la exposición cubierta recibirá el ponderador de riesgo correspondiente al activo recibido en garantía, pero estará sujeta a un mínimo del 20% –salv…"
  },
  {
   "id": "Restriccion_oro_amonedado_o_en_barras_con_ponderador_de_riesgo_0",
   "type": "Restriccion",
   "label": "Ponderador riesgo oro",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Oro amonedado o en barras con ponderador de riesgo 0%"
  },
  {
   "id": "Restriccion_se_aplicara_el_ponderador_de_riesgo_del_85_para_las_exposiciones_a_mipyme",
   "type": "Restriccion",
   "label": "Ponderador riesgo MIPYME",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Se aplicará el ponderador de riesgo del 85% para las exposiciones a Mipyme"
  },
  {
   "id": "Restriccion_ponderador_de_riesgo_1250",
   "type": "Restriccion",
   "label": "Ponderador de riesgo 1250%",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Si D es menor o igual a K, el ponderador será de 1250%."
  },
  {
   "id": "Restriccion_empresas_con_grado_de_inversion_con_ponderador_de_riesgo_65",
   "type": "Restriccion",
   "label": "Ponderador empresas inversión",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Empresas con grado de inversión con ponderador de riesgo 65%"
  },
  {
   "id": "Restriccion_cuentas_corrientes_y_especiales_en_bcra_con_ponderador_de_riesgo_0",
   "type": "Restriccion",
   "label": "Ponderador riesgo cuentas BCRA",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Cuentas corrientes y especiales en BCRA con ponderador de riesgo 0%"
  },
  {
   "id": "Excepcion_el_ponderador_de_riesgo_de_la_parte_de_la_exposicion_cubierta_podra_ser_inferior",
   "type": "Excepcion",
   "label": "Excepción ponderador mínimo 20%",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El ponderador de riesgo de la parte de la exposición cubierta podrá ser inferior al 20% en los siguientes casos: operaciones de pase con participante esencial, …"
  },
  {
   "id": "Obligacion_asignar_ponderador_riesgo_1250",
   "type": "Obligacion",
   "label": "Asignar ponderador riesgo 1250%",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Cuando la entidad no pueda determinar la exigencia de capital por riesgo específico conforme a la metodología establecida o el ratio de concentración sea igual …"
  },
  {
   "id": "Restriccion_las_operaciones_de_pase_estaran_sujetas_a_un_ponderador_de_riesgo_del_0_cuando_l",
   "type": "Restriccion",
   "label": "Operaciones pase: ponderador 0%",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Las operaciones de pase estarán sujetas a un ponderador de riesgo del 0% cuando la contraparte sea un participante esencial del mercado y se satisfagan condicio…"
  },
  {
   "id": "Restriccion_demas_activos_y_partidas_fuera_de_balance",
   "type": "Restriccion",
   "label": "Coeficiente de riesgo 100 puntos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Demás activos y partidas fuera de balance"
  }
 ]
}
```

### paso 6 — buscar_nodos {"consulta": "ponderador 100% exposición crédito", "limite": 10}

```json
{
 "consulta": "ponderador 100% exposición crédito",
 "total_con_match": 230,
 "resultados": [
  {
   "id": "Restriccion_la_parte_de_la_exposicion_cubierta_recibira_el_ponderador_de_riesgo_correspondie",
   "type": "Restriccion",
   "label": "Ponderador mínimo 20%",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La parte de la exposición cubierta recibirá el ponderador de riesgo correspondiente al activo recibido en garantía, pero estará sujeta a un mínimo del 20% –salv…"
  },
  {
   "id": "Restriccion_exposicion_a_bmd_que_cumplen_criterios_basilea_con_ponderador_0",
   "type": "Restriccion",
   "label": "Ponderador BMD Basilea",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Exposición a BMD que cumplen criterios Basilea con ponderador 0%"
  },
  {
   "id": "Restriccion_la_exposicion_presente_respecto_de_la_contraparte_no_puede_tener_un_valor_negati",
   "type": "Restriccion",
   "label": "Crédito de riesgo no negativo",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La exposición presente respecto de la contraparte no puede tener un valor negativo"
  },
  {
   "id": "Excepcion_el_ponderador_de_riesgo_de_la_parte_de_la_exposicion_cubierta_podra_ser_inferior",
   "type": "Excepcion",
   "label": "Excepción ponderador mínimo 20%",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El ponderador de riesgo de la parte de la exposición cubierta podrá ser inferior al 20% en los siguientes casos: operaciones de pase con participante esencial, …"
  },
  {
   "id": "Restriccion_exposicion_al_bcra_en_pesos_con_ponderador_de_riesgo_0",
   "type": "Restriccion",
   "label": "Ponderador exposición BCRA pesos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Exposición al BCRA en pesos con ponderador de riesgo 0%"
  },
  {
   "id": "Restriccion_100_para_retitulizaciones",
   "type": "Restriccion",
   "label": "Ponderador mínimo retitulizaciones",
   "tokens_matcheados": 2,
   "resumen_propiedades": "100% para retitulizaciones"
  },
  {
   "id": "Restriccion_exposicion_a_entidades_grupo_1_grado_a_con_ponderador_general_40",
   "type": "Restriccion",
   "label": "Ponderador exposición grupo 1 grado A",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Exposición a entidades grupo 1 grado A con ponderador general 40%"
  },
  {
   "id": "Restriccion_exposicion_a_gobiernos_locales_en_pesos_con_ponderador_de_riesgo_0",
   "type": "Restriccion",
   "label": "Ponderador exposición gobiernos pesos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Exposición a gobiernos locales en pesos con ponderador de riesgo 0%"
  },
  {
   "id": "Operacion_exposicion_sin_cobertura",
   "type": "Operacion",
   "label": "Exposición sin cobertura riesgo crédito",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: exposicion_sin_cobertura"
  },
  {
   "id": "Restriccion_exposicion_de_corto_plazo_a_entidades_grupo_1_con_ponderador_20",
   "type": "Restriccion",
   "label": "Ponderador exposición grupo 1 corto plazo",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Exposición de corto plazo a entidades grupo 1 con ponderador 20%"
  }
 ]
}
```

### paso 7 — buscar_nodos {"consulta": "no calificado ponderador", "limite": 10}

```json
{
 "consulta": "no calificado ponderador",
 "total_con_match": 410,
 "resultados": [
  {
   "id": "Restriccion_las_entidades_financieras_deberan_aplicar_un_ponderador_de_riesgo_del_1250_a_sus",
   "type": "Restriccion",
   "label": "Ponderador riesgo CCP no calificada",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Las entidades financieras deberán aplicar un ponderador de riesgo del 1250% a sus aportes a los fondos de garantía para incumplimientos de las CCP que no califi…"
  },
  {
   "id": "Restriccion_exposiciones_a_instrumentos_deuda_subordinada_e_instrumentos_de_capital_que_no_r",
   "type": "Restriccion",
   "label": "Ponderador deuda subordinada grupo 1",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Exposiciones a instrumentos: Deuda subordinada e instrumentos de capital que no reúnen las características para ser considerados como acciones: 150"
  },
  {
   "id": "Restriccion_apoyo_crediticio_que_no_supere_55_del_valor_del_inmueble_residencial_con_pondera",
   "type": "Restriccion",
   "label": "Ponderador hipotecario residencial 55%",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Apoyo crediticio que no supere 55% del valor del inmueble residencial con ponderador 20%"
  },
  {
   "id": "Restriccion_financiaciones_a_sector_publico_no_financiero_con_ponderador_de_riesgo_0",
   "type": "Restriccion",
   "label": "Ponderador financiación sector público",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Financiaciones a sector público no financiero con ponderador de riesgo 0%"
  },
  {
   "id": "Restriccion_el_ponderador_resultante_estara_sujeto_a_un_minimo_de_15_para_titulizaciones_que",
   "type": "Restriccion",
   "label": "Ponderador mínimo titulizaciones no STC",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El ponderador resultante estará sujeto a un mínimo de 15% para titulizaciones que no cumplan con los criterios STC"
  },
  {
   "id": "Obligacion_el_ponderador_de_riesgo_de_exposiciones_a_entidades_financieras_no_puede_ser_inf",
   "type": "Obligacion",
   "label": "Aplicar ponderador jurisdicción contraparte",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El ponderador de riesgo de exposiciones a entidades financieras no puede ser inferior al ponderador aplicable a jurisdicción de constitución de contraparte cuan…"
  },
  {
   "id": "Restriccion_no_prorrateo_de_ponderador_en_fondos_mixtos",
   "type": "Restriccion",
   "label": "No prorrateo de ponderador en fondos mixtos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Si un fondo de garantía constituido para hacer frente a incumplimientos respalda a productos sujetos a riesgo de liquidación y a productos expuestos a riesgo de…"
  },
  {
   "id": "Restriccion_operaciones_al_contado_a_liquidar_no_fallidas_0",
   "type": "Restriccion",
   "label": "Ponderador operaciones contado liquidar no fallidas",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Operaciones al contado a liquidar no fallidas: 0"
  },
  {
   "id": "Restriccion_ponderador_de_riesgo_para_exposiciones_no_protegidas",
   "type": "Restriccion",
   "label": "Ponderador de riesgo para exposiciones no protegidas",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Cuando la entidad financiera sea cliente del miembro compensador y no se cumplan los requisitos de protección, la exposición con el miembro compensador, incluid…"
  },
  {
   "id": "Restriccion_exposiciones_o_tramos_no_cubiertos_por_coberturas_del_riesgo_de_credito_con_prev",
   "type": "Restriccion",
   "label": "Ponderador exposiciones sin cobertura previsión menor 20%",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Exposiciones o tramos no cubiertos por coberturas del riesgo de crédito con previsiones específicas menores al 20% del saldo pendiente: 150"
  }
 ]
}
```

### paso 8 — ver_nodo {"id": "Operacion_calculo_de_exigencia_de_capital_minimo_por_riesgo_de_credito"}

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

### paso 9 — buscar_nodos {"consulta": "ponderador riesgo exposición deudor sin calificación", "limite": 10}

```json
{
 "consulta": "ponderador riesgo exposición deudor sin calificación",
 "total_con_match": 353,
 "resultados": [
  {
   "id": "Restriccion_la_parte_de_la_exposicion_cubierta_recibira_el_ponderador_de_riesgo_correspondie",
   "type": "Restriccion",
   "label": "Ponderador mínimo 20%",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La parte de la exposición cubierta recibirá el ponderador de riesgo correspondiente al activo recibido en garantía, pero estará sujeta a un mínimo del 20% –salv…"
  },
  {
   "id": "Excepcion_el_ponderador_de_riesgo_de_la_parte_de_la_exposicion_cubierta_podra_ser_inferior",
   "type": "Excepcion",
   "label": "Excepción ponderador mínimo 20%",
   "tokens_matcheados": 3,
   "resumen_propiedades": "El ponderador de riesgo de la parte de la exposición cubierta podrá ser inferior al 20% en los siguientes casos: operaciones de pase con participante esencial, …"
  },
  {
   "id": "Restriccion_exposicion_al_bcra_en_pesos_con_ponderador_de_riesgo_0",
   "type": "Restriccion",
   "label": "Ponderador exposición BCRA pesos",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Exposición al BCRA en pesos con ponderador de riesgo 0%"
  },
  {
   "id": "Obligacion_la_exposicion_total_sera_el_monto_bruto_sin_computar_las_coberturas_del_riesgo_d",
   "type": "Obligacion",
   "label": "Cálculo de exposición total bruta",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La exposición total será el monto bruto –sin computar las coberturas del riesgo de crédito de la Sección 5.– de las exposiciones minoristas con la contraparte."
  },
  {
   "id": "Restriccion_exposicion_a_gobiernos_locales_en_pesos_con_ponderador_de_riesgo_0",
   "type": "Restriccion",
   "label": "Ponderador exposición gobiernos pesos",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Exposición a gobiernos locales en pesos con ponderador de riesgo 0%"
  },
  {
   "id": "Operacion_exposicion_sin_cobertura",
   "type": "Operacion",
   "label": "Exposición sin cobertura riesgo crédito",
   "tokens_matcheados": 3,
   "resumen_propiedades": "tipo: exposicion_sin_cobertura"
  },
  {
   "id": "Restriccion_exposiciones_o_tramos_no_cubiertos_por_coberturas_del_riesgo_de_credito_con_prev",
   "type": "Restriccion",
   "label": "Ponderador exposiciones sin cobertura previsión menor 20%",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Exposiciones o tramos no cubiertos por coberturas del riesgo de crédito con previsiones específicas menores al 20% del saldo pendiente: 150"
  },
  {
   "id": "Restriccion_oro_amonedado_o_en_barras_con_ponderador_de_riesgo_0",
   "type": "Restriccion",
   "label": "Ponderador riesgo oro",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Oro amonedado o en barras con ponderador de riesgo 0%"
  },
  {
   "id": "Restriccion_exposicion_a_bmd_que_cumplen_criterios_basilea_con_ponderador_0",
   "type": "Restriccion",
   "label": "Ponderador BMD Basilea",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Exposición a BMD que cumplen criterios Basilea con ponderador 0%"
  },
  {
   "id": "Restriccion_se_aplicara_el_ponderador_de_riesgo_del_85_para_las_exposiciones_a_mipyme",
   "type": "Restriccion",
   "label": "Ponderador riesgo MIPYME",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Se aplicará el ponderador de riesgo del 85% para las exposiciones a Mipyme"
  }
 ]
}
```

### paso 10 — buscar_nodos {"consulta": "piso 100 ponderador riesgo", "limite": 10}

```json
{
 "consulta": "piso 100 ponderador riesgo",
 "total_con_match": 216,
 "resultados": [
  {
   "id": "Restriccion_la_parte_de_la_exposicion_cubierta_recibira_el_ponderador_de_riesgo_correspondie",
   "type": "Restriccion",
   "label": "Ponderador mínimo 20%",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La parte de la exposición cubierta recibirá el ponderador de riesgo correspondiente al activo recibido en garantía, pero estará sujeta a un mínimo del 20% –salv…"
  },
  {
   "id": "Restriccion_oro_amonedado_o_en_barras_con_ponderador_de_riesgo_0",
   "type": "Restriccion",
   "label": "Ponderador riesgo oro",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Oro amonedado o en barras con ponderador de riesgo 0%"
  },
  {
   "id": "Restriccion_se_aplicara_el_ponderador_de_riesgo_del_85_para_las_exposiciones_a_mipyme",
   "type": "Restriccion",
   "label": "Ponderador riesgo MIPYME",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Se aplicará el ponderador de riesgo del 85% para las exposiciones a Mipyme"
  },
  {
   "id": "Restriccion_ponderador_de_riesgo_1250",
   "type": "Restriccion",
   "label": "Ponderador de riesgo 1250%",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Si D es menor o igual a K, el ponderador será de 1250%."
  },
  {
   "id": "Restriccion_empresas_con_grado_de_inversion_con_ponderador_de_riesgo_65",
   "type": "Restriccion",
   "label": "Ponderador empresas inversión",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Empresas con grado de inversión con ponderador de riesgo 65%"
  },
  {
   "id": "Restriccion_cuentas_corrientes_y_especiales_en_bcra_con_ponderador_de_riesgo_0",
   "type": "Restriccion",
   "label": "Ponderador riesgo cuentas BCRA",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Cuentas corrientes y especiales en BCRA con ponderador de riesgo 0%"
  },
  {
   "id": "Excepcion_el_ponderador_de_riesgo_de_la_parte_de_la_exposicion_cubierta_podra_ser_inferior",
   "type": "Excepcion",
   "label": "Excepción ponderador mínimo 20%",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El ponderador de riesgo de la parte de la exposición cubierta podrá ser inferior al 20% en los siguientes casos: operaciones de pase con participante esencial, …"
  },
  {
   "id": "Obligacion_asignar_ponderador_riesgo_1250",
   "type": "Obligacion",
   "label": "Asignar ponderador riesgo 1250%",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Cuando la entidad no pueda determinar la exigencia de capital por riesgo específico conforme a la metodología establecida o el ratio de concentración sea igual …"
  },
  {
   "id": "Restriccion_las_operaciones_de_pase_estaran_sujetas_a_un_ponderador_de_riesgo_del_0_cuando_l",
   "type": "Restriccion",
   "label": "Operaciones pase: ponderador 0%",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Las operaciones de pase estarán sujetas a un ponderador de riesgo del 0% cuando la contraparte sea un participante esencial del mercado y se satisfagan condicio…"
  },
  {
   "id": "Restriccion_demas_activos_y_partidas_fuera_de_balance",
   "type": "Restriccion",
   "label": "Coeficiente de riesgo 100 puntos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Demás activos y partidas fuera de balance"
  }
 ]
}
```

### paso 11 — buscar_nodos {"consulta": "ponderador mínimo 100 exposición", "limite": 10}

```json
{
 "consulta": "ponderador mínimo 100 exposición",
 "total_con_match": 186,
 "resultados": [
  {
   "id": "Restriccion_la_parte_de_la_exposicion_cubierta_recibira_el_ponderador_de_riesgo_correspondie",
   "type": "Restriccion",
   "label": "Ponderador mínimo 20%",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La parte de la exposición cubierta recibirá el ponderador de riesgo correspondiente al activo recibido en garantía, pero estará sujeta a un mínimo del 20% –salv…"
  },
  {
   "id": "Excepcion_el_ponderador_de_riesgo_de_la_parte_de_la_exposicion_cubierta_podra_ser_inferior",
   "type": "Excepcion",
   "label": "Excepción ponderador mínimo 20%",
   "tokens_matcheados": 3,
   "resumen_propiedades": "El ponderador de riesgo de la parte de la exposición cubierta podrá ser inferior al 20% en los siguientes casos: operaciones de pase con participante esencial, …"
  },
  {
   "id": "Restriccion_100_para_retitulizaciones",
   "type": "Restriccion",
   "label": "Ponderador mínimo retitulizaciones",
   "tokens_matcheados": 3,
   "resumen_propiedades": "100% para retitulizaciones"
  },
  {
   "id": "Restriccion_exposicion_a_bmd_que_cumplen_criterios_basilea_con_ponderador_0",
   "type": "Restriccion",
   "label": "Ponderador BMD Basilea",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Exposición a BMD que cumplen criterios Basilea con ponderador 0%"
  },
  {
   "id": "Restriccion_exposicion_al_bcra_en_pesos_con_ponderador_de_riesgo_0",
   "type": "Restriccion",
   "label": "Ponderador exposición BCRA pesos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Exposición al BCRA en pesos con ponderador de riesgo 0%"
  },
  {
   "id": "Restriccion_exposicion_a_entidades_grupo_1_grado_a_con_ponderador_general_40",
   "type": "Restriccion",
   "label": "Ponderador exposición grupo 1 grado A",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Exposición a entidades grupo 1 grado A con ponderador general 40%"
  },
  {
   "id": "Restriccion_exposicion_a_gobiernos_locales_en_pesos_con_ponderador_de_riesgo_0",
   "type": "Restriccion",
   "label": "Ponderador exposición gobiernos pesos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Exposición a gobiernos locales en pesos con ponderador de riesgo 0%"
  },
  {
   "id": "Restriccion_el_ponderador_resultante_estara_sujeto_a_un_minimo_de_15_para_titulizaciones_que",
   "type": "Restriccion",
   "label": "Ponderador mínimo titulizaciones no STC",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El ponderador resultante estará sujeto a un mínimo de 15% para titulizaciones que no cumplan con los criterios STC"
  },
  {
   "id": "Obligacion_los_miembros_compensadores_podran_calcular_la_exigencia_por_la_exposicion_a_sus_",
   "type": "Obligacion",
   "label": "Aplicar MPOR mínimo de 5 días a clientes",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Los miembros compensadores podrán calcular la exigencia por la exposición a sus clientes aplicando un período de riesgo de margen que sea, como mínimo, de 5 día…"
  },
  {
   "id": "Restriccion_15_para_los_tramos_subordinados_de_titulizaciones_que_cumplan_con_criterios_stc",
   "type": "Restriccion",
   "label": "Ponderador mínimo tramos subordinados STC",
   "tokens_matcheados": 2,
   "resumen_propiedades": "15% para los tramos subordinados de titulizaciones que cumplan con criterios STC"
  }
 ]
}
```

### paso 12 — buscar_nodos {"consulta": "exposición sin rating calificación ponderador", "limite": 10}

```json
{
 "consulta": "exposición sin rating calificación ponderador",
 "total_con_match": 183,
 "resultados": [
  {
   "id": "Restriccion_la_parte_de_la_exposicion_cubierta_recibira_el_ponderador_de_riesgo_correspondie",
   "type": "Restriccion",
   "label": "Ponderador mínimo 20%",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La parte de la exposición cubierta recibirá el ponderador de riesgo correspondiente al activo recibido en garantía, pero estará sujeta a un mínimo del 20% –salv…"
  },
  {
   "id": "Restriccion_exposicion_a_bmd_que_cumplen_criterios_basilea_con_ponderador_0",
   "type": "Restriccion",
   "label": "Ponderador BMD Basilea",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Exposición a BMD que cumplen criterios Basilea con ponderador 0%"
  },
  {
   "id": "Excepcion_el_ponderador_de_riesgo_de_la_parte_de_la_exposicion_cubierta_podra_ser_inferior",
   "type": "Excepcion",
   "label": "Excepción ponderador mínimo 20%",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El ponderador de riesgo de la parte de la exposición cubierta podrá ser inferior al 20% en los siguientes casos: operaciones de pase con participante esencial, …"
  },
  {
   "id": "Restriccion_exposicion_al_bcra_en_pesos_con_ponderador_de_riesgo_0",
   "type": "Restriccion",
   "label": "Ponderador exposición BCRA pesos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Exposición al BCRA en pesos con ponderador de riesgo 0%"
  },
  {
   "id": "Obligacion_la_exposicion_total_sera_el_monto_bruto_sin_computar_las_coberturas_del_riesgo_d",
   "type": "Obligacion",
   "label": "Cálculo de exposición total bruta",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La exposición total será el monto bruto –sin computar las coberturas del riesgo de crédito de la Sección 5.– de las exposiciones minoristas con la contraparte."
  },
  {
   "id": "Restriccion_ponderador_por_calificacion_unica",
   "type": "Restriccion",
   "label": "Ponderador por calificación única",
   "tokens_matcheados": 2,
   "resumen_propiedades": "En los casos en que para una exposición sólo exista una calificación crediticia efectuada por la ECAI seleccionada, se utilizará esa calificación para determina…"
  },
  {
   "id": "Restriccion_las_entidades_que_titulicen_sinteticamente_las_exposiciones_a_traves_de_compra_d",
   "type": "Restriccion",
   "label": "Ponderador 1250% sin descalce plazos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Las entidades que titulicen sintéticamente las exposiciones a través de compra de protección por tramos no deberán tener en cuenta los descalces de plazos de ve…"
  },
  {
   "id": "Restriccion_exposicion_a_entidades_grupo_1_grado_a_con_ponderador_general_40",
   "type": "Restriccion",
   "label": "Ponderador exposición grupo 1 grado A",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Exposición a entidades grupo 1 grado A con ponderador general 40%"
  },
  {
   "id": "Restriccion_exposicion_a_gobiernos_locales_en_pesos_con_ponderador_de_riesgo_0",
   "type": "Restriccion",
   "label": "Ponderador exposición gobiernos pesos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Exposición a gobiernos locales en pesos con ponderador de riesgo 0%"
  },
  {
   "id": "Operacion_exposicion_sin_cobertura",
   "type": "Operacion",
   "label": "Exposición sin cobertura riesgo crédito",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: exposicion_sin_cobertura"
  }
 ]
}
```

### paso 13 — buscar_nodos {"consulta": "deudor sin calificación 100", "limite": 10}

```json
{
 "consulta": "deudor sin calificación 100",
 "total_con_match": 124,
 "resultados": [
  {
   "id": "Restriccion_valor_adeudado_no_supere_equivalente_de_usd_100_000_cuando_se_usa_companias_de_s",
   "type": "Restriccion",
   "label": "Límite monto para gestión sin entidad recupero",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Valor adeudado no supere equivalente de USD 100.000 cuando se usa compañías de seguro o agencias de recupero"
  },
  {
   "id": "EntidadFinanciera_deudor",
   "type": "EntidadFinanciera",
   "label": "Deudores",
   "tokens_matcheados": 1,
   "resumen_propiedades": "categoria: deudor"
  },
  {
   "id": "Excepcion_importador_demuestra_gestion_de_cobro_a_traves_de_reclamos_a_companias_de_seguro",
   "type": "Excepcion",
   "label": "Deudor moroso",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Importador demuestra gestión de cobro a través de reclamos a compañías de seguro de crédito o agencias de recupero, o mantiene acciones judiciales contra el pro…"
  },
  {
   "id": "Operacion_cesion_de_creditos_sin_responsabilidad",
   "type": "Operacion",
   "label": "Cesión de créditos",
   "tokens_matcheados": 1,
   "resumen_propiedades": "tipo: cesión de créditos sin responsabilidad"
  },
  {
   "id": "Operacion_evaluacion_de_deudor_como_sujeto_de_credito",
   "type": "Operacion",
   "label": "Evaluación de deudor",
   "tokens_matcheados": 1,
   "resumen_propiedades": "tipo: evaluación de deudor como sujeto de crédito"
  },
  {
   "id": "Operacion_operacion_con_derivados_sin_intercambio_de_margen_de_variacion",
   "type": "Operacion",
   "label": "Operaciones sin margen",
   "tokens_matcheados": 1,
   "resumen_propiedades": "tipo: operación con derivados sin intercambio de margen de variación"
  },
  {
   "id": "Obligacion_llevar_legajo_de_deudor",
   "type": "Obligacion",
   "label": "Llevar legajo de deudor",
   "tokens_matcheados": 1,
   "resumen_propiedades": "La entidad deberá llevar un legajo de cada deudor de su cartera, así como de cada uno de sus corresponsales, de acuerdo con lo establecido en las normas sobre C…"
  },
  {
   "id": "Operacion_clasificacion_de_deudor_en_categoria",
   "type": "Operacion",
   "label": "Clasificación de deudor",
   "tokens_matcheados": 1,
   "resumen_propiedades": "tipo: clasificación de deudor en categoría"
  },
  {
   "id": "Operacion_clasificacion_de_deudor_segun_mora",
   "type": "Operacion",
   "label": "Clasificación de deudor",
   "tokens_matcheados": 1,
   "resumen_propiedades": "tipo: clasificación de deudor según mora"
  },
  {
   "id": "Operacion_otorgamiento_de_credito_a_deudor_en_concurso",
   "type": "Operacion",
   "label": "Otorgamiento de crédito",
   "tokens_matcheados": 1,
   "resumen_propiedades": "tipo: otorgamiento de crédito a deudor en concurso"
  }
 ]
}
```

### paso 14 — buscar_nodos {"consulta": "ponderador por defecto estándar riesgo crédito", "limite": 10}

```json
{
 "consulta": "ponderador por defecto estándar riesgo crédito",
 "total_con_match": 715,
 "resultados": [
  {
   "id": "Restriccion_exposiciones_o_tramos_no_cubiertos_por_coberturas_del_riesgo_de_credito_con_prev",
   "type": "Restriccion",
   "label": "Ponderador exposiciones sin cobertura previsión menor 20%",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Exposiciones o tramos no cubiertos por coberturas del riesgo de crédito con previsiones específicas menores al 20% del saldo pendiente: 150"
  },
  {
   "id": "Obligacion_exigencia_por_riesgo_de_credito_de_contraparte_en_operaciones_con_derivados_extr",
   "type": "Obligacion",
   "label": "Cálculo de RCD",
   "tokens_matcheados": 3,
   "resumen_propiedades": "exigencia por riesgo de crédito de contraparte en operaciones con derivados extrabursátiles (over-the-counter, OTC), determinada conforme a lo establecido en el…"
  },
  {
   "id": "Operacion_calculo_de_exigencia_de_capital_minimo_por_riesgo_de_credito",
   "type": "Operacion",
   "label": "Cálculo exigencia capital mínimo",
   "tokens_matcheados": 3,
   "resumen_propiedades": "tipo: cálculo de exigencia de capital mínimo por riesgo de crédito"
  },
  {
   "id": "Operacion_calculo_de_exigencia_por_riesgo",
   "type": "Operacion",
   "label": "Cálculo exigencia riesgo crédito",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Cálculo de la exigencia por riesgo de crédito sin incluir el término INC mediante la fórmula: Código 70100000 (n) = k x 0,08 [ ∑(A x p) + ∑ (PFB x CCF x p) + ∑ …"
  },
  {
   "id": "Restriccion_el_computo_del_requerimiento_de_capital_por_aporte_al_fondo_de_garantia_utiliza_",
   "type": "Restriccion",
   "label": "Ponderador riesgo fondo garantía",
   "tokens_matcheados": 3,
   "resumen_propiedades": "El cómputo del requerimiento de capital por aporte al fondo de garantía utiliza un ponderador de riesgo del 2%"
  },
  {
   "id": "Restriccion_exposiciones_por_compras_en_cuotas_con_tarjeta_credito_hasta_25_11_21",
   "type": "Restriccion",
   "label": "Coeficiente de riesgo 1250 puntos",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Exposiciones por compras en cuotas con tarjeta crédito hasta 25/11/21"
  },
  {
   "id": "Operacion_financiacion_amparada_con_seguro_de_credito_por_riesgo_comercial",
   "type": "Operacion",
   "label": "Financiación con seguro de crédito",
   "tokens_matcheados": 3,
   "resumen_propiedades": "tipo: financiación amparada con seguro de crédito por riesgo comercial"
  },
  {
   "id": "Operacion_calculo_de_incrementos_de_exigencia_por_riesgo_de_credito",
   "type": "Operacion",
   "label": "Cálculo de incrementos de exigencia",
   "tokens_matcheados": 3,
   "resumen_propiedades": "tipo: cálculo de incrementos de exigencia por riesgo de crédito"
  },
  {
   "id": "Operacion_sustitucion_de_ponderador_de_riesgo_de_contraparte_por_garante",
   "type": "Operacion",
   "label": "Sustitución de ponderador de riesgo",
   "tokens_matcheados": 3,
   "resumen_propiedades": "tipo: sustitución de ponderador de riesgo de contraparte por garante"
  },
  {
   "id": "Operacion_calculo_de_exigencia_de_capital_por_riesgo_de_credito_de_contraparte",
   "type": "Operacion",
   "label": "Operación de cálculo de exigencia capital",
   "tokens_matcheados": 3,
   "resumen_propiedades": "tipo: cálculo de exigencia de capital por riesgo de crédito de contraparte"
  }
 ]
}
```

### paso 15 — buscar_nodos {"consulta": "ponderador 100% empresas personas", "limite": 10}

```json
{
 "consulta": "ponderador 100% empresas personas",
 "total_con_match": 119,
 "resultados": [
  {
   "id": "Restriccion_empresas_con_grado_de_inversion_con_ponderador_de_riesgo_65",
   "type": "Restriccion",
   "label": "Ponderador empresas inversión",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Empresas con grado de inversión con ponderador de riesgo 65%"
  },
  {
   "id": "Restriccion_100_para_retitulizaciones",
   "type": "Restriccion",
   "label": "Ponderador mínimo retitulizaciones",
   "tokens_matcheados": 2,
   "resumen_propiedades": "100% para retitulizaciones"
  },
  {
   "id": "Restriccion_se_aplicara_el_ponderador_de_riesgo_del_75_para_las_exposiciones_a_personas_huma",
   "type": "Restriccion",
   "label": "Ponderador riesgo personas humanas",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Se aplicará el ponderador de riesgo del 75% para las exposiciones a personas humanas"
  },
  {
   "id": "EntidadFinanciera_persona_humana",
   "type": "EntidadFinanciera",
   "label": "Personas humanas",
   "tokens_matcheados": 1,
   "resumen_propiedades": "categoria: personas humanas"
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
   "id": "Restriccion_la_parte_de_la_exposicion_cubierta_recibira_el_ponderador_de_riesgo_correspondie",
   "type": "Restriccion",
   "label": "Ponderador mínimo 20%",
   "tokens_matcheados": 1,
   "resumen_propiedades": "La parte de la exposición cubierta recibirá el ponderador de riesgo correspondiente al activo recibido en garantía, pero estará sujeta a un mínimo del 20% –salv…"
  },
  {
   "id": "Restriccion_oro_amonedado_o_en_barras_con_ponderador_de_riesgo_0",
   "type": "Restriccion",
   "label": "Ponderador riesgo oro",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Oro amonedado o en barras con ponderador de riesgo 0%"
  },
  {
   "id": "Restriccion_exposicion_a_bmd_que_cumplen_criterios_basilea_con_ponderador_0",
   "type": "Restriccion",
   "label": "Ponderador BMD Basilea",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Exposición a BMD que cumplen criterios Basilea con ponderador 0%"
  },
  {
   "id": "Restriccion_se_aplicara_el_ponderador_de_riesgo_del_85_para_las_exposiciones_a_mipyme",
   "type": "Restriccion",
   "label": "Ponderador riesgo MIPYME",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Se aplicará el ponderador de riesgo del 85% para las exposiciones a Mipyme"
  }
 ]
}
```

