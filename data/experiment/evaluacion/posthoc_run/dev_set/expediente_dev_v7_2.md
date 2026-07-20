# Expediente reserva v7 — parte 2: trayectorias completas (sección 3 + apéndices)


---

# Sección 3 — run_2/CQ-021

## 3a. Respuesta final del agente (verbatim, `posthoc_run/traces/off/run_2/CQ-021.json`)

`trace.final_json`:

```json
{
 "respuesta": "No se encontró información en el Knowledge Graph sobre casos específicos en que sea optativo para la entidad comunicar cambios negativos en la clasificación del deudor, ni sobre qué régimen determina el umbral para ello. Se identificó que existe una obligación general de comunicar cambios negativos en clasificación dentro de 45 días de realizada la reclasificación, pero los detalles sobre excepciones optativos y los regímenes que establecen umbrales no están disponibles en la documentación consultada.",
 "citas": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 3 > Sección 3 — preámbulo"
  }
 ],
 "respondible": false
}
```

`trace.final_raw` (turno final íntegro):

```
Basándome en la información recolectada del Knowledge Graph, no he encontrado evidencia específica sobre casos en que es optativo para la entidad comunicar cambios negativos en clasificación, ni sobre qué régimen determina el umbral para ello.

Lo que sí encontré es que:
- Existe una obligación general de comunicar cambios negativos en clasificación a los deudores
- Esta comunicación debe realizarse dentro de 45 días de realizada la reclasificación
- La obligación aplica a entidades financieras dadoras
- Se aplica a deudores en situación 3, 4 o 5, y a deudores en gestión judicial o extrajudicial de cobro

Sin embargo, la información específica sobre casos optativos y el régimen que determina el umbral no está disponible en los nodos consultados.

```json
{
  "respuesta": "No se encontró información en el Knowledge Graph sobre casos específicos en que sea optativo para la entidad comunicar cambios negativos en la clasificación del deudor, ni sobre qué régimen determina el umbral para ello. Se identificó que existe una obligación general de comunicar cambios negativos en clasificación dentro de 45 días de realizada la reclasificación, pero los detalles sobre excepciones optativos y los regímenes que establecen umbrales no están disponibles en la documentación consultada.",
  "citas": [
    {
      "source_doc": "TO_clasificacion_deudores_actual.pdf",
      "location": "Sección 3 > Sección 3 — preámbulo"
    }
  ],
  "respondible": false
}
```
```

## 3b. Inventario de pasos (runtime vs. almacenado vs. re-ejecutado)

| paso | tool | input | chars runtime | chars almacenados | re-ejecutado |
|---|---|---|---|---|---|
| 1 | buscar_nodos | `{"consulta": "optativo comunicar deudor cambio clasificación negativo", "limite": 10}` | 3243 | 1215 | = runtime ✓ |
| 2 | buscar_nodos | `{"consulta": "comunicación cambio clasificación deudor umbral", "limite": 10}` | 2915 | 1215 | = runtime ✓ |
| 3 | ver_nodo | `{"id": "procedimiento:comunicacion_de_cambio_negativo_de_clasificacion"}` | 483 | 483 | = runtime ✓ |
| 4 | ver_nodo | `{"id": "obligacion:comunicar_cambios_negativos_en_clasificacion"}` | 466 | 466 | = runtime ✓ |
| 5 | ver_vecinos | `{"id": "procedimiento:comunicacion_de_cambio_negativo_de_clasificacion", "direccion": "ambas"}` | 273 | 273 | = runtime ✓ |
| 6 | ver_vecinos | `{"id": "obligacion:comunicar_cambios_negativos_en_clasificacion", "direccion": "ambas"}` | 1346 | 1214 | = runtime ✓ |
| 7 | buscar_nodos | `{"consulta": "optativo comunicación clasificación umbral régimen", "limite": 10}` | 2206 | 1215 | = runtime ✓ |
| 8 | buscar_nodos | `{"consulta": "comunicación cambio clasificación optativa facultativa", "limite": 10}` | 2967 | 1215 | = runtime ✓ |
| 9 | buscar_nodos | `{"consulta": "comunicación optativa deudor clasificación monto importe", "limite": 10}` | 2944 | 1215 | = runtime ✓ |
| 10 | buscar_nodos | `{"consulta": "régimen clasificación deudor umbral comunicación", "limite": 10}` | 2792 | 1215 | = runtime ✓ |
| 11 | buscar_nodos | `{"consulta": "facultativo no obligatorio comunicación cambio clasificación", "limite": 10}` | 3324 | 1215 | = runtime ✓ |
| 12 | buscar_nodos | `{"consulta": "deudor pequeño monto bajo comunicación clasificación", "limite": 10}` | 2940 | 1215 | = runtime ✓ |
| 13 | buscar_nodos | `{"consulta": "régimen simplificado clasificación deudor comunicación", "limite": 10}` | 2926 | 1215 | = runtime ✓ |
| 14 | buscar_nodos | `{"consulta": "excepción comunicación cambio clasificación deudor", "limite": 10}` | 3102 | 1215 | = runtime ✓ |
| 15 | ver_nodo | `{"id": "concepto_definido:clasificacion_de_deudor"}` | 385 | 385 | = runtime ✓ |

**Fidelidad runtime↔re-ejecución: 15/15 pasos con largo idéntico.**

## 3c. APÉNDICE — outputs completos re-ejecutados (15 pasos)


--- paso 1 · buscar_nodos · input={"consulta": "optativo comunicar deudor cambio clasificación negativo", "limite": 10} · runtime=3243 · re-ejecutado=3243 ---

```json
{
 "consulta": "optativo comunicar deudor cambio clasificación negativo",
 "total_con_match": 180,
 "resultados": [
  {
   "id": "procedimiento:comunicacion_de_cambio_negativo_de_clasificacion",
   "type": "Procedimiento",
   "label": "comunicación de cambio negativo de clasificación",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Procedimiento de notificación a deudores sobre cambios negativos en clasificación a través de resumen impreso o resumen de cuenta mensual."
  },
  {
   "id": "obligacion:comunicar_clasificacion_del_deudor_a_solicitud_del_cliente",
   "type": "Obligacion",
   "label": "comunicar clasificación del deudor a solicitud del cliente",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La entidad financiera debe comunicar al cliente, a su solicitud, la última clasificación asignada, fundamentos, importe total de deudas con el sistema financier…"
  },
  {
   "id": "concepto_definido:clasificacion_de_deudor",
   "type": "ConceptoDefinido",
   "label": "clasificación de deudor",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Categorización del deudor según su situación crediticia y riesgo de incobrabilidad."
  },
  {
   "id": "obligacion:comunicar_cambios_negativos_en_clasificacion",
   "type": "Obligacion",
   "label": "comunicar cambios negativos en clasificación",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Las entidades financieras deben comunicar a los deudores los cambios negativos en la clasificación asignada."
  },
  {
   "id": "obligacion:notificar_cambio_de_clasificacion_con_preaviso",
   "type": "Obligacion",
   "label": "notificar cambio de clasificación con preaviso",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Requisito de notificación previa a la SEFyC con 6 meses de anticipación ante cambios en la opción de clasificación."
  },
  {
   "id": "obligacion:comunicar_a_sefyc_opcion_de_clasificacion_de_exposiciones_minoristas",
   "type": "Obligacion",
   "label": "comunicar a SEFyC opción de clasificación de exposiciones minoristas",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Las entidades financieras deben comunicar a la SEFyC el ejercicio de la opción de clasificar exposiciones minoristas normativas como transaccionales o no transa…"
  },
  {
   "id": "concepto_definido:deudor",
   "type": "ConceptoDefinido",
   "label": "deudor",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Persona física o jurídica con obligaciones crediticias respecto de la entidad."
  },
  {
   "id": "sujeto_regulado:deudor",
   "type": "SujetoRegulado",
   "label": "deudor",
   "tokens_matcheados": 1,
   "resumen_propiedades": "['Persona o entidad respecto de la cual se verifica una situación de incumplimiento crediticio.', 'Persona física o jurídica cuya clasificación se determina con…"
  },
  {
   "id": "concepto_definido:deudor_moroso",
   "type": "ConceptoDefinido",
   "label": "deudor moroso",
   "tokens_matcheados": 1,
   "resumen_propiedades": "['Situación en la que el exportador mantiene acciones judiciales contra el importador u otro obligado al pago.', 'Obligado de pago que incumple sus obligaciones…"
  },
  {
   "id": "sujeto_regulado:casa_de_cambio",
   "type": "SujetoRegulado",
   "label": "casa de cambio",
   "tokens_matcheados": 1,
   "resumen_propiedades": "['Casa de cambio elegible para ser designada por el exportador como responsable del seguimiento de operaciones de exportación.', 'Entidad autorizada para operar…"
  }
 ]
}
```

--- paso 2 · buscar_nodos · input={"consulta": "comunicación cambio clasificación deudor umbral", "limite": 10} · runtime=2915 · re-ejecutado=2915 ---

```json
{
 "consulta": "comunicación cambio clasificación deudor umbral",
 "total_con_match": 938,
 "resultados": [
  {
   "id": "procedimiento:comunicacion_de_cambio_negativo_de_clasificacion",
   "type": "Procedimiento",
   "label": "comunicación de cambio negativo de clasificación",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Procedimiento de notificación a deudores sobre cambios negativos en clasificación a través de resumen impreso o resumen de cuenta mensual."
  },
  {
   "id": "concepto_definido:clasificacion_de_deudor",
   "type": "ConceptoDefinido",
   "label": "clasificación de deudor",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Categorización del deudor según su situación crediticia y riesgo de incobrabilidad."
  },
  {
   "id": "umbral:factor_de_riesgo_tipo_de_cambio",
   "type": "Umbral",
   "label": "factor de riesgo tipo de cambio",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Factor regulatorio aplicable a operaciones sobre tipos de cambio."
  },
  {
   "id": "umbral:concentracion_maxima_por_deudor_1",
   "type": "Umbral",
   "label": "concentración máxima por deudor 1%",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Límite máximo de exposición concentrada en un solo deudor respecto al valor total de la cartera."
  },
  {
   "id": "umbral:limite_del_30_de_ingresos_del_deudor",
   "type": "Umbral",
   "label": "límite del 30% de ingresos del deudor",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Restricción de que las cuotas de financiaciones no excedan el 30% de los ingresos del deudor o codeudores."
  },
  {
   "id": "umbral:factor_de_ponderacion_riesgo_de_cambio",
   "type": "Umbral",
   "label": "factor de ponderación riesgo de cambio",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Factor aplicado al cálculo de exigencia por riesgo de cambio."
  },
  {
   "id": "umbral:monto_maximo_adeudado_por_deudor_moroso",
   "type": "Umbral",
   "label": "monto máximo adeudado por deudor moroso",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Valor máximo de deuda que permite utilizar la alternativa de gestión de cobro mediante agencias de recupero."
  },
  {
   "id": "umbral:diferencia_maxima_de_3_en_tipos_de_cambio",
   "type": "Umbral",
   "label": "diferencia máxima de 3% en tipos de cambio",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Límite máximo permitido de variación entre los tipos de cambio ofrecidos y los operados por el Banco de la Nación Argentina."
  },
  {
   "id": "obligacion:notificar_cambio_de_clasificacion_con_preaviso",
   "type": "Obligacion",
   "label": "notificar cambio de clasificación con preaviso",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Requisito de notificación previa a la SEFyC con 6 meses de anticipación ante cambios en la opción de clasificación."
  },
  {
   "id": "umbral:limites_mensuales_para_conceptos_de_venta_de_cambio",
   "type": "Umbral",
   "label": "límites mensuales para conceptos de venta de cambio",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Límites numéricos mensuales aplicables según el concepto de venta de cambio involucrado."
  }
 ]
}
```

--- paso 3 · ver_nodo · input={"id": "procedimiento:comunicacion_de_cambio_negativo_de_clasificacion"} · runtime=483 · re-ejecutado=483 ---

```json
{
 "id": "procedimiento:comunicacion_de_cambio_negativo_de_clasificacion",
 "type": "Procedimiento",
 "label": "comunicación de cambio negativo de clasificación",
 "properties": {
  "description": "Procedimiento de notificación a deudores sobre cambios negativos en clasificación a través de resumen impreso o resumen de cuenta mensual.",
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 3 > Sección 3 — preámbulo"
  }
 ]
}
```

--- paso 4 · ver_nodo · input={"id": "obligacion:comunicar_cambios_negativos_en_clasificacion"} · runtime=466 · re-ejecutado=466 ---

```json
{
 "id": "obligacion:comunicar_cambios_negativos_en_clasificacion",
 "type": "Obligacion",
 "label": "comunicar cambios negativos en clasificación",
 "properties": {
  "description": "Las entidades financieras deben comunicar a los deudores los cambios negativos en la clasificación asignada.",
  "modalidad": "obligacion",
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 3 > Sección 3 — preámbulo"
  }
 ]
}
```

--- paso 5 · ver_vecinos · input={"id": "procedimiento:comunicacion_de_cambio_negativo_de_clasificacion", "direccion": "ambas"} · runtime=273 · re-ejecutado=273 ---

```json
{
 "id": "procedimiento:comunicacion_de_cambio_negativo_de_clasificacion",
 "label": "comunicación de cambio negativo de clasificación",
 "n_salientes_total": 0,
 "n_entrantes_total": 0,
 "salientes": [],
 "salientes_truncado": false,
 "entrantes": [],
 "entrantes_truncado": false
}
```

--- paso 6 · ver_vecinos · input={"id": "obligacion:comunicar_cambios_negativos_en_clasificacion", "direccion": "ambas"} · runtime=1346 · re-ejecutado=1346 ---

```json
{
 "id": "obligacion:comunicar_cambios_negativos_en_clasificacion",
 "label": "comunicar cambios negativos en clasificación",
 "n_salientes_total": 3,
 "n_entrantes_total": 1,
 "salientes": [
  {
   "relation": "aplica_a",
   "vecino_id": "concepto_definido:deudor_en_situacion_3_4_o_5",
   "vecino_label": "deudor en situación 3, 4 o 5",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "Sección 3 > Sección 3 — preámbulo"
    }
   ]
  },
  {
   "relation": "aplica_a",
   "vecino_id": "concepto_definido:deudor_en_gestion_judicial_o_extrajudicial_de_cobro",
   "vecino_label": "deudor en gestión judicial o extrajudicial de cobro",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "Sección 3 > Sección 3 — preámbulo"
    }
   ]
  },
  {
   "relation": "tiene_plazo",
   "vecino_id": "plazo:45_dias_de_realizada_la_reclasificacion",
   "vecino_label": "45 días de realizada la reclasificación",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "Sección 3 > Sección 3 — preámbulo"
    }
   ]
  }
 ],
 "salientes_truncado": false,
 "entrantes": [
  {
   "relation": "obligado_a",
   "vecino_id": "sujeto_regulado:entidad_financiera_dadora",
   "vecino_label": "entidad financiera dadora",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "Sección 3 > Sección 3 — preámbulo"
    }
   ]
  }
 ],
 "entrantes_truncado": false
}
```

--- paso 7 · buscar_nodos · input={"consulta": "optativo comunicación clasificación umbral régimen", "limite": 10} · runtime=2206 · re-ejecutado=2206 ---

```json
{
 "consulta": "optativo comunicación clasificación umbral régimen",
 "total_con_match": 875,
 "resultados": [
  {
   "id": "procedimiento:comunicacion_de_cambio_negativo_de_clasificacion",
   "type": "Procedimiento",
   "label": "comunicación de cambio negativo de clasificación",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Procedimiento de notificación a deudores sobre cambios negativos en clasificación a través de resumen impreso o resumen de cuenta mensual."
  },
  {
   "id": "umbral:25",
   "type": "Umbral",
   "label": "25%",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Porcentaje mínimo de deudas elegibles mediante suscripción de BOPREAL Serie 1."
  },
  {
   "id": "umbral:50",
   "type": "Umbral",
   "label": "50%",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Porcentaje mínimo de deudas elegibles mediante suscripción de BOPREAL Serie 1."
  },
  {
   "id": "umbral:2_5_rpc",
   "type": "Umbral",
   "label": "2,5% RPC",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Porcentaje de Resultado Patrimonial Computable que determina si aplica la obligación de aprobación."
  },
  {
   "id": "umbral:6_de_apr",
   "type": "Umbral",
   "label": "6% de APR",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Límite mínimo para PNb."
  },
  {
   "id": "umbral:8_de_apr",
   "type": "Umbral",
   "label": "8% de APR",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Límite mínimo para RPC."
  },
  {
   "id": "umbral:25_de_rpc",
   "type": "Umbral",
   "label": "25% de RPC",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Límite cuantitativo para suma de posiciones compradas y vendidas en activos."
  },
  {
   "id": "umbral:usd_25_000",
   "type": "Umbral",
   "label": "USD 25.000",
   "tokens_matcheados": 1,
   "resumen_propiedades": "['Cuando el monto a imputar al permiso supera este equivalente, se requiere certificación de auditor externo.', 'Monto umbral que determina requisitos documenta…"
  },
  {
   "id": "umbral:4_5_de_apr",
   "type": "Umbral",
   "label": "4,5% de APR",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Límite mínimo para CO n1."
  },
  {
   "id": "umbral:usd_100_000",
   "type": "Umbral",
   "label": "USD 100.000",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Valor límite para la suma conjunta de CEDEARs y activos externos líquidos disponibles al inicio del día de solicitud de acceso al mercado."
  }
 ]
}
```

--- paso 8 · buscar_nodos · input={"consulta": "comunicación cambio clasificación optativa facultativa", "limite": 10} · runtime=2967 · re-ejecutado=2967 ---

```json
{
 "consulta": "comunicación cambio clasificación optativa facultativa",
 "total_con_match": 456,
 "resultados": [
  {
   "id": "procedimiento:comunicacion_de_cambio_negativo_de_clasificacion",
   "type": "Procedimiento",
   "label": "comunicación de cambio negativo de clasificación",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Procedimiento de notificación a deudores sobre cambios negativos en clasificación a través de resumen impreso o resumen de cuenta mensual."
  },
  {
   "id": "obligacion:notificar_cambio_de_clasificacion_con_preaviso",
   "type": "Obligacion",
   "label": "notificar cambio de clasificación con preaviso",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Requisito de notificación previa a la SEFyC con 6 meses de anticipación ante cambios en la opción de clasificación."
  },
  {
   "id": "sujeto_regulado:casa_de_cambio",
   "type": "SujetoRegulado",
   "label": "casa de cambio",
   "tokens_matcheados": 1,
   "resumen_propiedades": "['Casa de cambio elegible para ser designada por el exportador como responsable del seguimiento de operaciones de exportación.', 'Entidad autorizada para operar…"
  },
  {
   "id": "concepto_definido:riesgo_de_cambio",
   "type": "ConceptoDefinido",
   "label": "riesgo de cambio",
   "tokens_matcheados": 1,
   "resumen_propiedades": "['Riesgo calculado conforme al punto 6.4.3 de normas sobre Capitales mínimos de entidades financieras.', 'Categoría de riesgo regulatorio asociada a posiciones …"
  },
  {
   "id": "instrumento_financiero:boleto_de_cambio",
   "type": "InstrumentoFinanciero",
   "label": "boleto de cambio",
   "tokens_matcheados": 1,
   "resumen_propiedades": "['Documento que las entidades deben realizar para cada operación de cambio, canje y/o arbitraje.', 'Documento mediante el cual se registra una operación de camb…"
  },
  {
   "id": "norma_referenciada:comunicacion_a_467",
   "type": "NormaReferenciada",
   "label": "Comunicación A 467",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Política de crédito. Normas complementarias."
  },
  {
   "id": "norma_referenciada:comunicacion_a_2264",
   "type": "NormaReferenciada",
   "label": "Comunicación A 2264",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Deuda subordinada. Requisitos y tratamiento a los fines de la responsabilidad patrimonial computable."
  },
  {
   "id": "norma_referenciada:comunicacion_a_2266",
   "type": "NormaReferenciada",
   "label": "Comunicación A 2266",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Comunicación sobre valuación de tenencias de títulos valores públicos nacionales en cuentas de inversión o disponibles para la venta."
  },
  {
   "id": "norma_referenciada:comunicacion_a_2279",
   "type": "NormaReferenciada",
   "label": "Comunicación A 2279",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Responsabilidad patrimonial computable. Tratamiento de la reexpresión de los activos no monetarios."
  },
  {
   "id": "norma_referenciada:comunicacion_a_2290",
   "type": "NormaReferenciada",
   "label": "Comunicación A 2290",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Compra y venta de metales preciosos. Normas complementarias."
  }
 ]
}
```

--- paso 9 · buscar_nodos · input={"consulta": "comunicación optativa deudor clasificación monto importe", "limite": 10} · runtime=2944 · re-ejecutado=2944 ---

```json
{
 "consulta": "comunicación optativa deudor clasificación monto importe",
 "total_con_match": 517,
 "resultados": [
  {
   "id": "concepto_definido:clasificacion_de_deudor",
   "type": "ConceptoDefinido",
   "label": "clasificación de deudor",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Categorización del deudor según su situación crediticia y riesgo de incobrabilidad."
  },
  {
   "id": "umbral:monto_maximo_adeudado_por_deudor_moroso",
   "type": "Umbral",
   "label": "monto máximo adeudado por deudor moroso",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Valor máximo de deuda que permite utilizar la alternativa de gestión de cobro mediante agencias de recupero."
  },
  {
   "id": "procedimiento:comunicacion_de_cambio_negativo_de_clasificacion",
   "type": "Procedimiento",
   "label": "comunicación de cambio negativo de clasificación",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Procedimiento de notificación a deudores sobre cambios negativos en clasificación a través de resumen impreso o resumen de cuenta mensual."
  },
  {
   "id": "obligacion:comunicar_clasificacion_del_deudor_a_solicitud_del_cliente",
   "type": "Obligacion",
   "label": "comunicar clasificación del deudor a solicitud del cliente",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La entidad financiera debe comunicar al cliente, a su solicitud, la última clasificación asignada, fundamentos, importe total de deudas con el sistema financier…"
  },
  {
   "id": "concepto_definido:deudor",
   "type": "ConceptoDefinido",
   "label": "deudor",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Persona física o jurídica con obligaciones crediticias respecto de la entidad."
  },
  {
   "id": "sujeto_regulado:deudor",
   "type": "SujetoRegulado",
   "label": "deudor",
   "tokens_matcheados": 1,
   "resumen_propiedades": "['Persona o entidad respecto de la cual se verifica una situación de incumplimiento crediticio.', 'Persona física o jurídica cuya clasificación se determina con…"
  },
  {
   "id": "concepto_definido:deudor_moroso",
   "type": "ConceptoDefinido",
   "label": "deudor moroso",
   "tokens_matcheados": 1,
   "resumen_propiedades": "['Situación en la que el exportador mantiene acciones judiciales contra el importador u otro obligado al pago.', 'Obligado de pago que incumple sus obligaciones…"
  },
  {
   "id": "sujeto_regulado:cliente_deudor",
   "type": "SujetoRegulado",
   "label": "cliente deudor",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Persona física o jurídica que ha contraído deuda con entidad financiera y está sujeto a clasificación regulatoria."
  },
  {
   "id": "concepto_definido:deudor_en_concurso",
   "type": "ConceptoDefinido",
   "label": "deudor en concurso",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Deudor que se encuentra en proceso de concurso crediticio."
  },
  {
   "id": "concepto_definido:quiebra_del_deudor",
   "type": "ConceptoDefinido",
   "label": "quiebra del deudor",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Solicitud de quiebra del deudor u otra medida similar que produzca diferimiento o impida el recupero del crédito."
  }
 ]
}
```

--- paso 10 · buscar_nodos · input={"consulta": "régimen clasificación deudor umbral comunicación", "limite": 10} · runtime=2792 · re-ejecutado=2792 ---

```json
{
 "consulta": "régimen clasificación deudor umbral comunicación",
 "total_con_match": 923,
 "resultados": [
  {
   "id": "concepto_definido:clasificacion_de_deudor",
   "type": "ConceptoDefinido",
   "label": "clasificación de deudor",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Categorización del deudor según su situación crediticia y riesgo de incobrabilidad."
  },
  {
   "id": "umbral:concentracion_maxima_por_deudor_1",
   "type": "Umbral",
   "label": "concentración máxima por deudor 1%",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Límite máximo de exposición concentrada en un solo deudor respecto al valor total de la cartera."
  },
  {
   "id": "umbral:limite_del_30_de_ingresos_del_deudor",
   "type": "Umbral",
   "label": "límite del 30% de ingresos del deudor",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Restricción de que las cuotas de financiaciones no excedan el 30% de los ingresos del deudor o codeudores."
  },
  {
   "id": "umbral:monto_maximo_adeudado_por_deudor_moroso",
   "type": "Umbral",
   "label": "monto máximo adeudado por deudor moroso",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Valor máximo de deuda que permite utilizar la alternativa de gestión de cobro mediante agencias de recupero."
  },
  {
   "id": "procedimiento:comunicacion_de_cambio_negativo_de_clasificacion",
   "type": "Procedimiento",
   "label": "comunicación de cambio negativo de clasificación",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Procedimiento de notificación a deudores sobre cambios negativos en clasificación a través de resumen impreso o resumen de cuenta mensual."
  },
  {
   "id": "obligacion:comunicar_clasificacion_del_deudor_a_solicitud_del_cliente",
   "type": "Obligacion",
   "label": "comunicar clasificación del deudor a solicitud del cliente",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La entidad financiera debe comunicar al cliente, a su solicitud, la última clasificación asignada, fundamentos, importe total de deudas con el sistema financier…"
  },
  {
   "id": "umbral:25",
   "type": "Umbral",
   "label": "25%",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Porcentaje mínimo de deudas elegibles mediante suscripción de BOPREAL Serie 1."
  },
  {
   "id": "umbral:50",
   "type": "Umbral",
   "label": "50%",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Porcentaje mínimo de deudas elegibles mediante suscripción de BOPREAL Serie 1."
  },
  {
   "id": "concepto_definido:deudor",
   "type": "ConceptoDefinido",
   "label": "deudor",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Persona física o jurídica con obligaciones crediticias respecto de la entidad."
  },
  {
   "id": "sujeto_regulado:deudor",
   "type": "SujetoRegulado",
   "label": "deudor",
   "tokens_matcheados": 1,
   "resumen_propiedades": "['Persona o entidad respecto de la cual se verifica una situación de incumplimiento crediticio.', 'Persona física o jurídica cuya clasificación se determina con…"
  }
 ]
}
```

--- paso 11 · buscar_nodos · input={"consulta": "facultativo no obligatorio comunicación cambio clasificación", "limite": 10} · runtime=3324 · re-ejecutado=3324 ---

```json
{
 "consulta": "facultativo no obligatorio comunicación cambio clasificación",
 "total_con_match": 759,
 "resultados": [
  {
   "id": "procedimiento:comunicacion_de_cambio_negativo_de_clasificacion",
   "type": "Procedimiento",
   "label": "comunicación de cambio negativo de clasificación",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Procedimiento de notificación a deudores sobre cambios negativos en clasificación a través de resumen impreso o resumen de cuenta mensual."
  },
  {
   "id": "obligacion:notificar_cambio_de_clasificacion_con_preaviso",
   "type": "Obligacion",
   "label": "notificar cambio de clasificación con preaviso",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Requisito de notificación previa a la SEFyC con 6 meses de anticipación ante cambios en la opción de clasificación."
  },
  {
   "id": "obligacion:no_asumir_riesgo_de_cambio_en_monedas_distintas",
   "type": "Obligacion",
   "label": "no asumir riesgo de cambio en monedas distintas",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La entidad local no podrá asumir riesgo de cambio entre pesos, dólares estadounidenses y otras monedas cuando se otorga asistencia en moneda distinta de los rec…"
  },
  {
   "id": "obligacion:no_mejorar_clasificacion_por_razones_de_emergencia",
   "type": "Obligacion",
   "label": "no mejorar clasificación por razones de emergencia",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El tratamiento de emergencia no puede implicar mejoramiento de clasificación preexistente del cliente."
  },
  {
   "id": "obligacion:no_incluir_en_clasificacion_a_deudores_en_cesion_sin_responsabilidad",
   "type": "Obligacion",
   "label": "no incluir en clasificación a deudores en cesión sin responsabilidad",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Excepción: los deudores que resulten de operaciones de cesión sin responsabilidad para el cedente no serán objeto de clasificación."
  },
  {
   "id": "obligacion:no_asumir_riesgo_de_cambio_en_moneda_distinta_a_recursos_del_exterior",
   "type": "Obligacion",
   "label": "no asumir riesgo de cambio en moneda distinta a recursos del exterior",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Prohibición de que la entidad local asuma el riesgo de cambio cuando otorga asistencia en moneda distinta a la de los recursos del exterior."
  },
  {
   "id": "sujeto_regulado:no_residentes",
   "type": "SujetoRegulado",
   "label": "no residentes",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Personas físicas o jurídicas no residentes en Argentina que realizan operaciones de divisas."
  },
  {
   "id": "requisito:no_amortizable",
   "type": "Requisito",
   "label": "no amortizable",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Condición según la cual los resultados se realizan solo mediante venta del instrumento o liquidación del emisor."
  },
  {
   "id": "sujeto_regulado:casa_de_cambio",
   "type": "SujetoRegulado",
   "label": "casa de cambio",
   "tokens_matcheados": 1,
   "resumen_propiedades": "['Casa de cambio elegible para ser designada por el exportador como responsable del seguimiento de operaciones de exportación.', 'Entidad autorizada para operar…"
  },
  {
   "id": "concepto_definido:riesgo_de_cambio",
   "type": "ConceptoDefinido",
   "label": "riesgo de cambio",
   "tokens_matcheados": 1,
   "resumen_propiedades": "['Riesgo calculado conforme al punto 6.4.3 de normas sobre Capitales mínimos de entidades financieras.', 'Categoría de riesgo regulatorio asociada a posiciones …"
  }
 ]
}
```

--- paso 12 · buscar_nodos · input={"consulta": "deudor pequeño monto bajo comunicación clasificación", "limite": 10} · runtime=2940 · re-ejecutado=2940 ---

```json
{
 "consulta": "deudor pequeño monto bajo comunicación clasificación",
 "total_con_match": 524,
 "resultados": [
  {
   "id": "concepto_definido:clasificacion_de_deudor",
   "type": "ConceptoDefinido",
   "label": "clasificación de deudor",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Categorización del deudor según su situación crediticia y riesgo de incobrabilidad."
  },
  {
   "id": "umbral:monto_maximo_adeudado_por_deudor_moroso",
   "type": "Umbral",
   "label": "monto máximo adeudado por deudor moroso",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Valor máximo de deuda que permite utilizar la alternativa de gestión de cobro mediante agencias de recupero."
  },
  {
   "id": "procedimiento:comunicacion_de_cambio_negativo_de_clasificacion",
   "type": "Procedimiento",
   "label": "comunicación de cambio negativo de clasificación",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Procedimiento de notificación a deudores sobre cambios negativos en clasificación a través de resumen impreso o resumen de cuenta mensual."
  },
  {
   "id": "obligacion:comunicar_clasificacion_del_deudor_a_solicitud_del_cliente",
   "type": "Obligacion",
   "label": "comunicar clasificación del deudor a solicitud del cliente",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La entidad financiera debe comunicar al cliente, a su solicitud, la última clasificación asignada, fundamentos, importe total de deudas con el sistema financier…"
  },
  {
   "id": "concepto_definido:deudor",
   "type": "ConceptoDefinido",
   "label": "deudor",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Persona física o jurídica con obligaciones crediticias respecto de la entidad."
  },
  {
   "id": "sujeto_regulado:deudor",
   "type": "SujetoRegulado",
   "label": "deudor",
   "tokens_matcheados": 1,
   "resumen_propiedades": "['Persona o entidad respecto de la cual se verifica una situación de incumplimiento crediticio.', 'Persona física o jurídica cuya clasificación se determina con…"
  },
  {
   "id": "concepto_definido:deudor_moroso",
   "type": "ConceptoDefinido",
   "label": "deudor moroso",
   "tokens_matcheados": 1,
   "resumen_propiedades": "['Situación en la que el exportador mantiene acciones judiciales contra el importador u otro obligado al pago.', 'Obligado de pago que incumple sus obligaciones…"
  },
  {
   "id": "sujeto_regulado:cliente_deudor",
   "type": "SujetoRegulado",
   "label": "cliente deudor",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Persona física o jurídica que ha contraído deuda con entidad financiera y está sujeto a clasificación regulatoria."
  },
  {
   "id": "concepto_definido:deudor_en_concurso",
   "type": "ConceptoDefinido",
   "label": "deudor en concurso",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Deudor que se encuentra en proceso de concurso crediticio."
  },
  {
   "id": "concepto_definido:quiebra_del_deudor",
   "type": "ConceptoDefinido",
   "label": "quiebra del deudor",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Solicitud de quiebra del deudor u otra medida similar que produzca diferimiento o impida el recupero del crédito."
  }
 ]
}
```

--- paso 13 · buscar_nodos · input={"consulta": "régimen simplificado clasificación deudor comunicación", "limite": 10} · runtime=2926 · re-ejecutado=2926 ---

```json
{
 "consulta": "régimen simplificado clasificación deudor comunicación",
 "total_con_match": 492,
 "resultados": [
  {
   "id": "concepto_definido:clasificacion_de_deudor",
   "type": "ConceptoDefinido",
   "label": "clasificación de deudor",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Categorización del deudor según su situación crediticia y riesgo de incobrabilidad."
  },
  {
   "id": "procedimiento:comunicacion_de_cambio_negativo_de_clasificacion",
   "type": "Procedimiento",
   "label": "comunicación de cambio negativo de clasificación",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Procedimiento de notificación a deudores sobre cambios negativos en clasificación a través de resumen impreso o resumen de cuenta mensual."
  },
  {
   "id": "obligacion:comunicar_clasificacion_del_deudor_a_solicitud_del_cliente",
   "type": "Obligacion",
   "label": "comunicar clasificación del deudor a solicitud del cliente",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La entidad financiera debe comunicar al cliente, a su solicitud, la última clasificación asignada, fundamentos, importe total de deudas con el sistema financier…"
  },
  {
   "id": "concepto_definido:deudor",
   "type": "ConceptoDefinido",
   "label": "deudor",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Persona física o jurídica con obligaciones crediticias respecto de la entidad."
  },
  {
   "id": "sujeto_regulado:deudor",
   "type": "SujetoRegulado",
   "label": "deudor",
   "tokens_matcheados": 1,
   "resumen_propiedades": "['Persona o entidad respecto de la cual se verifica una situación de incumplimiento crediticio.', 'Persona física o jurídica cuya clasificación se determina con…"
  },
  {
   "id": "concepto_definido:deudor_moroso",
   "type": "ConceptoDefinido",
   "label": "deudor moroso",
   "tokens_matcheados": 1,
   "resumen_propiedades": "['Situación en la que el exportador mantiene acciones judiciales contra el importador u otro obligado al pago.', 'Obligado de pago que incumple sus obligaciones…"
  },
  {
   "id": "sujeto_regulado:cliente_deudor",
   "type": "SujetoRegulado",
   "label": "cliente deudor",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Persona física o jurídica que ha contraído deuda con entidad financiera y está sujeto a clasificación regulatoria."
  },
  {
   "id": "concepto_definido:regimen_de_rancho",
   "type": "ConceptoDefinido",
   "label": "régimen de rancho",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Régimen aduanal aplicable a medios de transporte de bandera nacional conforme a artículos 506-516 de la Ley 22.415."
  },
  {
   "id": "concepto_definido:deudor_en_concurso",
   "type": "ConceptoDefinido",
   "label": "deudor en concurso",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Deudor que se encuentra en proceso de concurso crediticio."
  },
  {
   "id": "concepto_definido:quiebra_del_deudor",
   "type": "ConceptoDefinido",
   "label": "quiebra del deudor",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Solicitud de quiebra del deudor u otra medida similar que produzca diferimiento o impida el recupero del crédito."
  }
 ]
}
```

--- paso 14 · buscar_nodos · input={"consulta": "excepción comunicación cambio clasificación deudor", "limite": 10} · runtime=3102 · re-ejecutado=3102 ---

```json
{
 "consulta": "excepción comunicación cambio clasificación deudor",
 "total_con_match": 541,
 "resultados": [
  {
   "id": "procedimiento:comunicacion_de_cambio_negativo_de_clasificacion",
   "type": "Procedimiento",
   "label": "comunicación de cambio negativo de clasificación",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Procedimiento de notificación a deudores sobre cambios negativos en clasificación a través de resumen impreso o resumen de cuenta mensual."
  },
  {
   "id": "concepto_definido:clasificacion_de_deudor",
   "type": "ConceptoDefinido",
   "label": "clasificación de deudor",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Categorización del deudor según su situación crediticia y riesgo de incobrabilidad."
  },
  {
   "id": "obligacion:notificar_cambio_de_clasificacion_con_preaviso",
   "type": "Obligacion",
   "label": "notificar cambio de clasificación con preaviso",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Requisito de notificación previa a la SEFyC con 6 meses de anticipación ante cambios en la opción de clasificación."
  },
  {
   "id": "obligacion:comunicar_clasificacion_del_deudor_a_solicitud_del_cliente",
   "type": "Obligacion",
   "label": "comunicar clasificación del deudor a solicitud del cliente",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La entidad financiera debe comunicar al cliente, a su solicitud, la última clasificación asignada, fundamentos, importe total de deudas con el sistema financier…"
  },
  {
   "id": "concepto_definido:deudor",
   "type": "ConceptoDefinido",
   "label": "deudor",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Persona física o jurídica con obligaciones crediticias respecto de la entidad."
  },
  {
   "id": "sujeto_regulado:deudor",
   "type": "SujetoRegulado",
   "label": "deudor",
   "tokens_matcheados": 1,
   "resumen_propiedades": "['Persona o entidad respecto de la cual se verifica una situación de incumplimiento crediticio.', 'Persona física o jurídica cuya clasificación se determina con…"
  },
  {
   "id": "concepto_definido:deudor_moroso",
   "type": "ConceptoDefinido",
   "label": "deudor moroso",
   "tokens_matcheados": 1,
   "resumen_propiedades": "['Situación en la que el exportador mantiene acciones judiciales contra el importador u otro obligado al pago.', 'Obligado de pago que incumple sus obligaciones…"
  },
  {
   "id": "sujeto_regulado:casa_de_cambio",
   "type": "SujetoRegulado",
   "label": "casa de cambio",
   "tokens_matcheados": 1,
   "resumen_propiedades": "['Casa de cambio elegible para ser designada por el exportador como responsable del seguimiento de operaciones de exportación.', 'Entidad autorizada para operar…"
  },
  {
   "id": "sujeto_regulado:cliente_deudor",
   "type": "SujetoRegulado",
   "label": "cliente deudor",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Persona física o jurídica que ha contraído deuda con entidad financiera y está sujeto a clasificación regulatoria."
  },
  {
   "id": "concepto_definido:riesgo_de_cambio",
   "type": "ConceptoDefinido",
   "label": "riesgo de cambio",
   "tokens_matcheados": 1,
   "resumen_propiedades": "['Riesgo calculado conforme al punto 6.4.3 de normas sobre Capitales mínimos de entidades financieras.', 'Categoría de riesgo regulatorio asociada a posiciones …"
  }
 ]
}
```

--- paso 15 · ver_nodo · input={"id": "concepto_definido:clasificacion_de_deudor"} · runtime=385 · re-ejecutado=385 ---

```json
{
 "id": "concepto_definido:clasificacion_de_deudor",
 "type": "ConceptoDefinido",
 "label": "clasificación de deudor",
 "properties": {
  "description": "Categorización del deudor según su situación crediticia y riesgo de incobrabilidad.",
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 6 > Sección 6 — preámbulo"
  }
 ]
}
```

---

# Sección 3 — run_4/CQ-008

## 3a. Respuesta final del agente (verbatim, `posthoc_run/traces/off/run_4/CQ-008.json`)

`trace.final_json`:

```json
{
 "respuesta": "No se encontró en el Knowledge Graph información específica sobre el plazo en el cual la entidad financiera debe comunicar la última clasificación asignada a un cliente cuando este lo solicita. Aunque el grafo contiene normativa sobre clasificación de deudores y obligaciones de las entidades financieras, no incluye la disposición regulatoria que establece este plazo particular.",
 "citas": [],
 "respondible": false
}
```

`trace.final_raw` (turno final íntegro):

```
Basándome en la información recolectada del Knowledge Graph, no he encontrado evidencia específica sobre un plazo regulatorio para que la entidad financiera comunique la última clasificación asignada a un cliente cuando este lo solicita.

He buscado exhaustivamente usando múltiples términos relacionados con:
- Plazos de comunicación de clasificación
- Derechos del deudor a recibir información
- Obligaciones de la entidad de informar clasificaciones
- Plazos específicos (10 días hábiles, 20 días hábiles, etc.)

Aunque el Knowledge Graph contiene información sobre clasificación de deudores, categorías de riesgo y obligaciones de las entidades financieras, no encontré un nodo o relación que especifique explícitamente el plazo en el cual debe comunicarse la clasificación cuando el cliente lo solicita.

```json
{
  "respuesta": "No se encontró en el Knowledge Graph información específica sobre el plazo en el cual la entidad financiera debe comunicar la última clasificación asignada a un cliente cuando este lo solicita. Aunque el grafo contiene normativa sobre clasificación de deudores y obligaciones de las entidades financieras, no incluye la disposición regulatoria que establece este plazo particular.",
  "citas": [],
  "respondible": false
}
```
```

## 3b. Inventario de pasos (runtime vs. almacenado vs. re-ejecutado)

| paso | tool | input | chars runtime | chars almacenados | re-ejecutado |
|---|---|---|---|---|---|
| 1 | buscar_nodos | `{"consulta": "plazo comunicación clasificación cliente entidad financiera", "limite": 10}` | 3023 | 1215 | = runtime ✓ |
| 2 | buscar_nodos | `{"consulta": "comunicar clasificación cliente solicitud", "limite": 10}` | 3117 | 1215 | = runtime ✓ |
| 3 | buscar_nodos | `{"consulta": "comunicación clasificación plazo días solicitud cliente", "limite": 10}` | 3297 | 1215 | = runtime ✓ |
| 4 | buscar_nodos | `{"consulta": "informar clasificación cliente deudor plazo", "limite": 10}` | 2998 | 1215 | = runtime ✓ |
| 5 | buscar_nodos | `{"consulta": "comunicar última clasificación deudor solicitud", "limite": 10}` | 2980 | 1215 | = runtime ✓ |
| 6 | buscar_nodos | `{"consulta": "derecho cliente conocer clasificación información", "limite": 10}` | 2918 | 1215 | = runtime ✓ |
| 7 | buscar_nodos | `{"consulta": "obligación informar clasificación riesgo deudor", "limite": 10}` | 3026 | 1215 | = runtime ✓ |
| 8 | buscar_nodos | `{"consulta": "comunicación información deudor plazo hábiles días", "limite": 10}` | 3292 | 1215 | = runtime ✓ |
| 9 | buscar_nodos | `{"consulta": "deudor derecho información clasificación", "limite": 10}` | 2800 | 1215 | = runtime ✓ |
| 10 | buscar_nodos | `{"consulta": "entidad debe comunicar información deudor", "limite": 10}` | 2893 | 1215 | = runtime ✓ |
| 11 | buscar_nodos | `{"consulta": "comunicación información al deudor 10 días", "limite": 10}` | 2924 | 1215 | = runtime ✓ |
| 12 | buscar_nodos | `{"consulta": "información deudor 10 días hábiles comunicar", "limite": 10}` | 3003 | 1215 | = runtime ✓ |
| 13 | ver_nodo | `{"id": "deudor"}` | 1167 | 1167 | = runtime ✓ |
| 14 | buscar_nodos | `{"consulta": "10 días hábiles comunicación clasificación", "limite": 10}` | 2980 | 1215 | = runtime ✓ |
| 15 | ver_vecinos | `{"id": "deudor", "direccion": "salientes"}` | 6930 | 1215 | = runtime ✓ |

**Fidelidad runtime↔re-ejecución: 15/15 pasos con largo idéntico.**

## 3c. APÉNDICE — outputs completos re-ejecutados (15 pasos)


--- paso 1 · buscar_nodos · input={"consulta": "plazo comunicación clasificación cliente entidad financiera", "limite": 10} · runtime=3023 · re-ejecutado=3023 ---

```json
{
 "consulta": "plazo comunicación clasificación cliente entidad financiera",
 "total_con_match": 210,
 "resultados": [
  {
   "id": "entidad_financiera",
   "type": "sujeto_regulado",
   "label": "Entidad financiera",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Entidades financieras que deben verificar el listado de CUITs con operaciones inconsistentes y reforzar medidas de control, así como abstenerse de cursar operac…"
  },
  {
   "id": "cliente_de_la_entidad",
   "type": "sujeto_regulado",
   "label": "Cliente de la entidad",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Personas residentes en el país o en el exterior, de sectores público y privado, financieros y no financieros, que reciben financiaciones de la entidad y deben s…"
  },
  {
   "id": "entidad_financiera_local",
   "type": "sujeto_regulado",
   "label": "Entidad financiera local",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Institución financiera que otorga financiaciones en moneda extranjera al VPU a partir de líneas de crédito del exterior y que verifica el cumplimiento de condic…"
  },
  {
   "id": "entidad_financiera_deudora",
   "type": "categoria_de_deudor",
   "label": "Entidad financiera deudora",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Intermediario financiero que actúa como deudor, cuyo análisis debe considerar liquidez y calidad de cartera."
  },
  {
   "id": "entidad_financiera_del_pais",
   "type": "categoria_de_contraparte",
   "label": "Entidad financiera del país",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Entidad financiera doméstica sujeta a regulación y supervisión prudencial."
  },
  {
   "id": "entidad_financiera_originante",
   "type": "sujeto_regulatorio",
   "label": "Entidad financiera originante",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Entidad que origina directa o indirectamente las exposiciones subyacentes incluidas en la titulización, o que patrocina un programa de emisión de títulos valore…"
  },
  {
   "id": "entidad_financiera_controlante",
   "type": "sujeto_regulado",
   "label": "Entidad financiera controlante",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Entidad financiera que ejerce control sobre otras entidades y está sujeta a supervisión consolidada, debiendo observar normas de capitales mínimos en base conso…"
  },
  {
   "id": "entidad_financiera_del_grupo_1",
   "type": "sujeto_regulado",
   "label": "Entidad financiera del grupo 1",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Entidades financieras que deben clasificar exposiciones con garantía hipotecaria en normativas y no normativas."
  },
  {
   "id": "entidad_financiera_del_grupo_2",
   "type": "sujeto_regulado",
   "label": "Entidad financiera del grupo 2",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Entidades financieras que reciben tratamiento de exposiciones con garantía hipotecaria normativas."
  },
  {
   "id": "entidad_financiera_prestamista",
   "type": "sujeto_regulado",
   "label": "Entidad financiera prestamista",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Entidad financiera que otorga financiamiento a otras entidades financieras y debe evaluar y asignar grados de riesgo a sus exposiciones."
  }
 ]
}
```

--- paso 2 · buscar_nodos · input={"consulta": "comunicar clasificación cliente solicitud", "limite": 10} · runtime=3117 · re-ejecutado=3117 ---

```json
{
 "consulta": "comunicar clasificación cliente solicitud",
 "total_con_match": 42,
 "resultados": [
  {
   "id": "cliente",
   "type": "sujeto_regulado",
   "label": "Cliente",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Entidad cuyas operaciones y activos en garantía se mantienen en subcuentas separadas del miembro compensador, con garantías protegidas de la quiebra de la CCP y…"
  },
  {
   "id": "cliente_residente",
   "type": "sujeto_regulado",
   "label": "Cliente residente",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Residente que puede canalizar operaciones a través del Sistema de Monedas Locales implementado por el BCRA."
  },
  {
   "id": "legajo_del_cliente",
   "type": "documento_regulatorio",
   "label": "Legajo del cliente",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Legajo que debe llevar la entidad para cada deudor de su cartera, conteniendo todos los elementos de juicio para realizar evaluaciones y clasificaciones, dejand…"
  },
  {
   "id": "cliente_no_residente",
   "type": "sujeto_regulado",
   "label": "Cliente no residente",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Cliente que no es persona humana residente y debe cumplir con requisitos adicionales de declaración jurada respecto a operaciones con títulos valores y otros ac…"
  },
  {
   "id": "solicitud_particular",
   "type": "tramite_aduanero",
   "label": "Solicitud Particular",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Solicitud Particular autenticada por el Servicio Aduanero interviniente que demuestre la efectiva nacionalización de los bienes, con identificación de factura y…"
  },
  {
   "id": "cliente_de_la_entidad",
   "type": "sujeto_regulado",
   "label": "Cliente de la entidad",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Personas residentes en el país o en el exterior, de sectores público y privado, financieros y no financieros, que reciben financiaciones de la entidad y deben s…"
  },
  {
   "id": "cliente_en_observacion",
   "type": "subcategoria_de_seguimiento_especial",
   "label": "Cliente en observación",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Deudor con buena situación financiera y rentabilidad pero con flujo de fondos sensible a variaciones de una o dos variables, o con atrasos de hasta 90 días en p…"
  },
  {
   "id": "tarea_de_clasificacion",
   "type": "funcion_regulatoria",
   "label": "Tarea de clasificación",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Proceso de asignación de categorías de riesgo a deudores, que puede ser encomendada a un área independiente, al sector de créditos con revisión independiente, o…"
  },
  {
   "id": "transaccion_de_cliente",
   "type": "tipo_de_operacion_financiera",
   "label": "Transacción de cliente",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Transacción realizada por un cliente a través de un miembro compensador que actúa como intermediario. El fragmento establece condiciones para que estas transacc…"
  },
  {
   "id": "clasificacion_de_deudores",
   "type": "tarea_regulatoria",
   "label": "Clasificación de deudores",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Clasificación que debe efectuarse con una periodicidad que atienda a la importancia del deudor, considerando la totalidad de las financiaciones comprendidas, de…"
  }
 ]
}
```

--- paso 3 · buscar_nodos · input={"consulta": "comunicación clasificación plazo días solicitud cliente", "limite": 10} · runtime=3297 · re-ejecutado=3297 ---

```json
{
 "consulta": "comunicación clasificación plazo días solicitud cliente",
 "total_con_match": 123,
 "resultados": [
  {
   "id": "plazo_de_90_dias",
   "type": "restriccion_temporal",
   "label": "Plazo de 90 días",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Período mínimo que debe transcurrir desde la adquisición de títulos valores en suscripción primaria antes de poder venderlos en mercado secundario con liquidaci…"
  },
  {
   "id": "plazo_de_20_dias_habiles",
   "type": "plazo_regulatorio",
   "label": "Plazo de 20 días hábiles",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Plazo máximo dentro del cual debe ingresarse y liquidarse en el mercado de cambios el contravalor de enajenación de activos no financieros no producidos."
  },
  {
   "id": "bien_con_plazo_de_30_dias",
   "type": "categoria_de_bien",
   "label": "Bien con plazo de 30 días",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Bien que tiene asignado un plazo de 30 días corridos conforme al punto 7.1.1.2., con coeficiente del 5% para cálculo de monto máximo."
  },
  {
   "id": "bien_con_plazo_de_60_dias",
   "type": "categoria_de_bien",
   "label": "Bien con plazo de 60 días",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Bien que tiene asignado un plazo de 60 días corridos conforme al punto 7.1.1.3., con coeficiente del 10% para cálculo de monto máximo."
  },
  {
   "id": "plazo_de_90_dias_corridos",
   "type": "requisito_temporal",
   "label": "Plazo de 90 días corridos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Plazo requerido desde la fecha de prestación o devengamiento del servicio para acceso al mercado de cambios en operaciones de contraparte vinculada a partir del…"
  },
  {
   "id": "plazo_de_180_dias_corridos",
   "type": "requisito_temporal",
   "label": "Plazo de 180 días corridos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Plazo requerido desde la fecha de prestación o devengamiento del servicio para acceso al mercado de cambios en operaciones de contraparte vinculada previas al 1…"
  },
  {
   "id": "bien_con_plazo_de_180_o_mas_dias",
   "type": "categoria_de_bien",
   "label": "Bien con plazo de 180 o más días",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Bien que tiene asignado un plazo de 180 o más días corridos conforme a los puntos 7.1.1.4. y 7.1.1.5., con coeficiente del 15% para cálculo de monto máximo."
  },
  {
   "id": "plazo_adicional_de_15_dias_corridos",
   "type": "requisito_temporal",
   "label": "Plazo adicional de 15 días corridos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Plazo adicional aplicable a financiaciones de servicios de fletes de importación o cuando la financiación es anterior a la prestación del servicio."
  },
  {
   "id": "plazo_de_revocacion_de_diez_dias_habiles",
   "type": "requisito_temporal",
   "label": "Plazo de revocación de diez días hábiles",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Plazo durante el cual el usuario puede revocar la aceptación del producto o servicio, contado a partir de la fecha de recibido el contrato o de la disponibilida…"
  },
  {
   "id": "plazo_de_120_dias_corridos_para_aplicacion_de_fondos",
   "type": "requisito_temporal",
   "label": "Plazo de 120 días corridos para aplicación de fondos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Plazo en el cual la totalidad de los fondos obtenidos de emisiones de títulos de deuda deben ser aplicados para concretar pagos de importaciones de bienes o fle…"
  }
 ]
}
```

--- paso 4 · buscar_nodos · input={"consulta": "informar clasificación cliente deudor plazo", "limite": 10} · runtime=2998 · re-ejecutado=2998 ---

```json
{
 "consulta": "informar clasificación cliente deudor plazo",
 "total_con_match": 119,
 "resultados": [
  {
   "id": "deudor",
   "type": "sujeto_regulado",
   "label": "Deudor",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Persona física o jurídica que mantiene financiaciones con la entidad y debe ser objeto de análisis de situación económica y financiera, así como de clasificació…"
  },
  {
   "id": "cliente",
   "type": "sujeto_regulado",
   "label": "Cliente",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Entidad cuyas operaciones y activos en garantía se mantienen en subcuentas separadas del miembro compensador, con garantías protegidas de la quiebra de la CCP y…"
  },
  {
   "id": "deudor_moroso",
   "type": "causal_de_demora",
   "label": "Deudor moroso",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Situación en que el importador u otro obligado al pago incumple sus obligaciones, justificando acciones judiciales por parte del exportador."
  },
  {
   "id": "plazo_de_90_dias",
   "type": "restriccion_temporal",
   "label": "Plazo de 90 días",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Período mínimo que debe transcurrir desde la adquisición de títulos valores en suscripción primaria antes de poder venderlos en mercado secundario con liquidaci…"
  },
  {
   "id": "cliente_residente",
   "type": "sujeto_regulado",
   "label": "Cliente residente",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Residente que puede canalizar operaciones a través del Sistema de Monedas Locales implementado por el BCRA."
  },
  {
   "id": "prorroga_de_plazo",
   "type": "mecanismo_de_regularizacion",
   "label": "Prórroga de plazo",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Extensión del plazo para la demostración del registro de ingreso aduanero, concedida por la entidad a cargo del seguimiento o con conformidad del BCRA."
  },
  {
   "id": "deudor_en_concurso",
   "type": "categoria_de_deudor",
   "label": "Deudor en concurso",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Deudor en concurso o con acuerdo preventivo extrajudicial solicitado o en gestión judicial de cobro que, por un período de hasta 540 días, no haya presentado do…"
  },
  {
   "id": "estructura_a_plazo",
   "type": "tipo_de_titulizacion",
   "label": "Estructura a plazo",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Operación con exposiciones rotativas que contiene cláusulas de amortización anticipada que replican estructuras a plazo, donde el riesgo de las facilidades suby…"
  },
  {
   "id": "legajo_del_cliente",
   "type": "documento_regulatorio",
   "label": "Legajo del cliente",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Legajo que debe llevar la entidad para cada deudor de su cartera, conteniendo todos los elementos de juicio para realizar evaluaciones y clasificaciones, dejand…"
  },
  {
   "id": "ampliacion_de_plazo",
   "type": "procedimiento_administrativo",
   "label": "Ampliación de plazo",
   "tokens_matcheados": 1,
   "resumen_propiedades": "El exportador puede solicitar a la entidad encargada del seguimiento que el plazo para liquidación de divisas sea ampliado hasta la fecha en que se estima se ef…"
  }
 ]
}
```

--- paso 5 · buscar_nodos · input={"consulta": "comunicar última clasificación deudor solicitud", "limite": 10} · runtime=2980 · re-ejecutado=2980 ---

```json
{
 "consulta": "comunicar última clasificación deudor solicitud",
 "total_con_match": 29,
 "resultados": [
  {
   "id": "solicitud_de_quiebra_del_deudor",
   "type": "situacion_de_incumplimiento",
   "label": "Solicitud de quiebra del deudor",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Solicitud de quiebra del deudor u otra medida similar que produzca diferimiento o impida recupero del crédito."
  },
  {
   "id": "deudor",
   "type": "sujeto_regulado",
   "label": "Deudor",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Persona física o jurídica que mantiene financiaciones con la entidad y debe ser objeto de análisis de situación económica y financiera, así como de clasificació…"
  },
  {
   "id": "deudor_moroso",
   "type": "causal_de_demora",
   "label": "Deudor moroso",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Situación en que el importador u otro obligado al pago incumple sus obligaciones, justificando acciones judiciales por parte del exportador."
  },
  {
   "id": "deudor_en_concurso",
   "type": "categoria_de_deudor",
   "label": "Deudor en concurso",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Deudor en concurso o con acuerdo preventivo extrajudicial solicitado o en gestión judicial de cobro que, por un período de hasta 540 días, no haya presentado do…"
  },
  {
   "id": "credito_unico_deudor",
   "type": "subclase_de_derivado_de_credito",
   "label": "Crédito único deudor",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Derivado de crédito referenciado a un único deudor, con factores regulatorios que varían según calificación crediticia (AAA a CCC)."
  },
  {
   "id": "deudor_no_calificado",
   "type": "categoria_de_contraparte",
   "label": "Deudor no calificado",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Contraparte sin calificación de crédito otorgada por ECAI, que recibe ponderador de riesgo no menor al del país de constitución."
  },
  {
   "id": "direccion_del_deudor",
   "type": "componente_organizacional",
   "label": "Dirección del deudor",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Gestión y liderazgo del deudor, evaluados por su capacidad, experiencia y honestidad."
  },
  {
   "id": "solicitud_particular",
   "type": "tramite_aduanero",
   "label": "Solicitud Particular",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Solicitud Particular autenticada por el Servicio Aduanero interviniente que demuestre la efectiva nacionalización de los bienes, con identificación de factura y…"
  },
  {
   "id": "tarea_de_clasificacion",
   "type": "funcion_regulatoria",
   "label": "Tarea de clasificación",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Proceso de asignación de categorías de riesgo a deudores, que puede ser encomendada a un área independiente, al sector de créditos con revisión independiente, o…"
  },
  {
   "id": "clasificacion_de_deudores",
   "type": "tarea_regulatoria",
   "label": "Clasificación de deudores",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Clasificación que debe efectuarse con una periodicidad que atienda a la importancia del deudor, considerando la totalidad de las financiaciones comprendidas, de…"
  }
 ]
}
```

--- paso 6 · buscar_nodos · input={"consulta": "derecho cliente conocer clasificación información", "limite": 10} · runtime=2918 · re-ejecutado=2918 ---

```json
{
 "consulta": "derecho cliente conocer clasificación información",
 "total_con_match": 63,
 "resultados": [
  {
   "id": "cliente",
   "type": "sujeto_regulado",
   "label": "Cliente",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Entidad cuyas operaciones y activos en garantía se mantienen en subcuentas separadas del miembro compensador, con garantías protegidas de la quiebra de la CCP y…"
  },
  {
   "id": "cliente_residente",
   "type": "sujeto_regulado",
   "label": "Cliente residente",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Residente que puede canalizar operaciones a través del Sistema de Monedas Locales implementado por el BCRA."
  },
  {
   "id": "derecho_de_credito",
   "type": "tipo_de_activo_subyacente",
   "label": "Derecho de crédito",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Derecho de crédito de carácter homogéneo que constituye activo subyacente en una titulización."
  },
  {
   "id": "legajo_del_cliente",
   "type": "documento_regulatorio",
   "label": "Legajo del cliente",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Legajo que debe llevar la entidad para cada deudor de su cartera, conteniendo todos los elementos de juicio para realizar evaluaciones y clasificaciones, dejand…"
  },
  {
   "id": "derecho_del_usuario",
   "type": "garantia_regulatoria",
   "label": "Derecho del usuario",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Facultades y derechos reconocidos al usuario por la normativa que no pueden ser dispensados ni renunciados."
  },
  {
   "id": "informacion_externa",
   "type": "fuente_de_validacion",
   "label": "Información externa",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Datos independientes utilizados para validar de modo consistente las valuaciones de exposiciones."
  },
  {
   "id": "cliente_no_residente",
   "type": "sujeto_regulado",
   "label": "Cliente no residente",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Cliente que no es persona humana residente y debe cumplir con requisitos adicionales de declaración jurada respecto a operaciones con títulos valores y otros ac…"
  },
  {
   "id": "derecho_de_rescision",
   "type": "derecho_del_usuario",
   "label": "Derecho de rescisión",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Derecho del usuario a rescindir el contrato en cualquier momento antes de la entrada en vigencia del cambio y sin cargo alguno, manteniendo obligaciones pendien…"
  },
  {
   "id": "cliente_de_la_entidad",
   "type": "sujeto_regulado",
   "label": "Cliente de la entidad",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Personas residentes en el país o en el exterior, de sectores público y privado, financieros y no financieros, que reciben financiaciones de la entidad y deben s…"
  },
  {
   "id": "cliente_en_observacion",
   "type": "subcategoria_de_seguimiento_especial",
   "label": "Cliente en observación",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Deudor con buena situación financiera y rentabilidad pero con flujo de fondos sensible a variaciones de una o dos variables, o con atrasos de hasta 90 días en p…"
  }
 ]
}
```

--- paso 7 · buscar_nodos · input={"consulta": "obligación informar clasificación riesgo deudor", "limite": 10} · runtime=3026 · re-ejecutado=3026 ---

```json
{
 "consulta": "obligación informar clasificación riesgo deudor",
 "total_con_match": 172,
 "resultados": [
  {
   "id": "clasificacion_con_alto_riesgo_de_insolvencia",
   "type": "categoria_de_clasificacion_de_deudores",
   "label": "Clasificación con alto riesgo de insolvencia",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Categoría de riesgo asignada a deudores cuyo análisis de flujo de fondos demuestra que es altamente improbable que puedan atender la totalidad de sus compromiso…"
  },
  {
   "id": "deudor",
   "type": "sujeto_regulado",
   "label": "Deudor",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Persona física o jurídica que mantiene financiaciones con la entidad y debe ser objeto de análisis de situación económica y financiera, así como de clasificació…"
  },
  {
   "id": "riesgo_alto",
   "type": "categoria_de_clasificacion_de_deudores",
   "label": "Riesgo alto",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Comprende clientes con atrasos de más de 180 días hasta un año, o en situaciones de concurso preventivo, acuerdo preventivo extrajudicial no homologado, o quieb…"
  },
  {
   "id": "riesgo_bajo",
   "type": "nivel_de_clasificacion",
   "label": "Riesgo bajo",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Nivel de clasificación para clientes con capacidad de pago normal, mencionado implícitamente como nivel inmediato inferior en contextos de reclasificación."
  },
  {
   "id": "riesgo_pais",
   "type": "factor_de_riesgo",
   "label": "Riesgo país",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Riesgo asociado al país de residencia del deudor, incluyendo situación económica, deuda externa, cuenta corriente e historial financiero."
  },
  {
   "id": "riesgo_vega",
   "type": "tipo_de_riesgo_de_opcion",
   "label": "Riesgo Vega",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Riesgo que mide la sensibilidad del precio de la opción a cambios en la volatilidad del precio del subyacente; requiere exigencia de capital adicional en el mét…"
  },
  {
   "id": "riesgo_gamma",
   "type": "tipo_de_riesgo_de_opcion",
   "label": "Riesgo Gamma",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Riesgo que mide la tasa de cambio del coeficiente delta ante variaciones en el precio del subyacente; requiere exigencia de capital adicional en el método delta…"
  },
  {
   "id": "riesgo_medio",
   "type": "categoria_de_clasificacion_de_deudores",
   "label": "Riesgo medio",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Comprende clientes con alguna incapacidad para cancelar obligaciones, con atrasos de más de 90 hasta 180 días."
  },
  {
   "id": "deudor_moroso",
   "type": "causal_de_demora",
   "label": "Deudor moroso",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Situación en que el importador u otro obligado al pago incumple sus obligaciones, justificando acciones judiciales por parte del exportador."
  },
  {
   "id": "riesgo_de_base",
   "type": "tipo_de_riesgo",
   "label": "Riesgo de base",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Riesgo asociado a diferencias en características como calidad o ubicación de productos dentro de un tipo de commodity. El área de Supervisión puede requerir def…"
  }
 ]
}
```

--- paso 8 · buscar_nodos · input={"consulta": "comunicación información deudor plazo hábiles días", "limite": 10} · runtime=3292 · re-ejecutado=3292 ---

```json
{
 "consulta": "comunicación información deudor plazo hábiles días",
 "total_con_match": 118,
 "resultados": [
  {
   "id": "plazo_de_20_dias_habiles",
   "type": "plazo_regulatorio",
   "label": "Plazo de 20 días hábiles",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Plazo máximo dentro del cual debe ingresarse y liquidarse en el mercado de cambios el contravalor de enajenación de activos no financieros no producidos."
  },
  {
   "id": "plazo_de_revocacion_de_diez_dias_habiles",
   "type": "requisito_temporal",
   "label": "Plazo de revocación de diez días hábiles",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Plazo durante el cual el usuario puede revocar la aceptación del producto o servicio, contado a partir de la fecha de recibido el contrato o de la disponibilida…"
  },
  {
   "id": "plazo_de_90_dias",
   "type": "restriccion_temporal",
   "label": "Plazo de 90 días",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Período mínimo que debe transcurrir desde la adquisición de títulos valores en suscripción primaria antes de poder venderlos en mercado secundario con liquidaci…"
  },
  {
   "id": "bien_con_plazo_de_30_dias",
   "type": "categoria_de_bien",
   "label": "Bien con plazo de 30 días",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Bien que tiene asignado un plazo de 30 días corridos conforme al punto 7.1.1.2., con coeficiente del 5% para cálculo de monto máximo."
  },
  {
   "id": "bien_con_plazo_de_60_dias",
   "type": "categoria_de_bien",
   "label": "Bien con plazo de 60 días",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Bien que tiene asignado un plazo de 60 días corridos conforme al punto 7.1.1.3., con coeficiente del 10% para cálculo de monto máximo."
  },
  {
   "id": "plazo_de_90_dias_corridos",
   "type": "requisito_temporal",
   "label": "Plazo de 90 días corridos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Plazo requerido desde la fecha de prestación o devengamiento del servicio para acceso al mercado de cambios en operaciones de contraparte vinculada a partir del…"
  },
  {
   "id": "plazo_de_180_dias_corridos",
   "type": "requisito_temporal",
   "label": "Plazo de 180 días corridos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Plazo requerido desde la fecha de prestación o devengamiento del servicio para acceso al mercado de cambios en operaciones de contraparte vinculada previas al 1…"
  },
  {
   "id": "bien_con_plazo_de_180_o_mas_dias",
   "type": "categoria_de_bien",
   "label": "Bien con plazo de 180 o más días",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Bien que tiene asignado un plazo de 180 o más días corridos conforme a los puntos 7.1.1.4. y 7.1.1.5., con coeficiente del 15% para cálculo de monto máximo."
  },
  {
   "id": "plazo_adicional_de_15_dias_corridos",
   "type": "requisito_temporal",
   "label": "Plazo adicional de 15 días corridos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Plazo adicional aplicable a financiaciones de servicios de fletes de importación o cuando la financiación es anterior a la prestación del servicio."
  },
  {
   "id": "plazo_de_120_dias_corridos_para_aplicacion_de_fondos",
   "type": "requisito_temporal",
   "label": "Plazo de 120 días corridos para aplicación de fondos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Plazo en el cual la totalidad de los fondos obtenidos de emisiones de títulos de deuda deben ser aplicados para concretar pagos de importaciones de bienes o fle…"
  }
 ]
}
```

--- paso 9 · buscar_nodos · input={"consulta": "deudor derecho información clasificación", "limite": 10} · runtime=2800 · re-ejecutado=2800 ---

```json
{
 "consulta": "deudor derecho información clasificación",
 "total_con_match": 50,
 "resultados": [
  {
   "id": "deudor",
   "type": "sujeto_regulado",
   "label": "Deudor",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Persona física o jurídica que mantiene financiaciones con la entidad y debe ser objeto de análisis de situación económica y financiera, así como de clasificació…"
  },
  {
   "id": "deudor_moroso",
   "type": "causal_de_demora",
   "label": "Deudor moroso",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Situación en que el importador u otro obligado al pago incumple sus obligaciones, justificando acciones judiciales por parte del exportador."
  },
  {
   "id": "derecho_de_credito",
   "type": "tipo_de_activo_subyacente",
   "label": "Derecho de crédito",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Derecho de crédito de carácter homogéneo que constituye activo subyacente en una titulización."
  },
  {
   "id": "deudor_en_concurso",
   "type": "categoria_de_deudor",
   "label": "Deudor en concurso",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Deudor en concurso o con acuerdo preventivo extrajudicial solicitado o en gestión judicial de cobro que, por un período de hasta 540 días, no haya presentado do…"
  },
  {
   "id": "derecho_del_usuario",
   "type": "garantia_regulatoria",
   "label": "Derecho del usuario",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Facultades y derechos reconocidos al usuario por la normativa que no pueden ser dispensados ni renunciados."
  },
  {
   "id": "informacion_externa",
   "type": "fuente_de_validacion",
   "label": "Información externa",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Datos independientes utilizados para validar de modo consistente las valuaciones de exposiciones."
  },
  {
   "id": "credito_unico_deudor",
   "type": "subclase_de_derivado_de_credito",
   "label": "Crédito único deudor",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Derivado de crédito referenciado a un único deudor, con factores regulatorios que varían según calificación crediticia (AAA a CCC)."
  },
  {
   "id": "derecho_de_rescision",
   "type": "derecho_del_usuario",
   "label": "Derecho de rescisión",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Derecho del usuario a rescindir el contrato en cualquier momento antes de la entrada en vigencia del cambio y sin cargo alguno, manteniendo obligaciones pendien…"
  },
  {
   "id": "deudor_no_calificado",
   "type": "categoria_de_contraparte",
   "label": "Deudor no calificado",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Contraparte sin calificación de crédito otorgada por ECAI, que recibe ponderador de riesgo no menor al del país de constitución."
  },
  {
   "id": "direccion_del_deudor",
   "type": "componente_organizacional",
   "label": "Dirección del deudor",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Gestión y liderazgo del deudor, evaluados por su capacidad, experiencia y honestidad."
  }
 ]
}
```

--- paso 10 · buscar_nodos · input={"consulta": "entidad debe comunicar información deudor", "limite": 10} · runtime=2893 · re-ejecutado=2893 ---

```json
{
 "consulta": "entidad debe comunicar información deudor",
 "total_con_match": 122,
 "resultados": [
  {
   "id": "deudor",
   "type": "sujeto_regulado",
   "label": "Deudor",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Persona física o jurídica que mantiene financiaciones con la entidad y debe ser objeto de análisis de situación económica y financiera, así como de clasificació…"
  },
  {
   "id": "entidad",
   "type": "sujeto_regulado",
   "label": "Entidad",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Institución autorizada a dar acceso al mercado de cambios para pagos de servicios prestados por no residentes, sujeta a verificaciones y requisitos normativos."
  },
  {
   "id": "deudor_moroso",
   "type": "causal_de_demora",
   "label": "Deudor moroso",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Situación en que el importador u otro obligado al pago incumple sus obligaciones, justificando acciones judiciales por parte del exportador."
  },
  {
   "id": "nueva_entidad",
   "type": "categoria_de_entidad",
   "label": "Nueva entidad",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Entidad financiera que no ha integrado el capital mínimo exigido dentro de los 60 días corridos de su otorgamiento de autorización."
  },
  {
   "id": "entidad_atipica",
   "type": "clasificacion_de_entidad_financiera",
   "label": "Entidad atípica",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Entidad financiera cuya medida de riesgo EVE supera el 15% del nivel de capital 1, sujeta a medidas específicas por la SEFyC."
  },
  {
   "id": "entidad_cedente",
   "type": "participante_en_titulizacion",
   "label": "Entidad cedente",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Entidad que transfiere exposiciones en una operación de titulización y que no debe mantener control directo ni indirecto sobre las exposiciones transferidas."
  },
  {
   "id": "entidad_bursatil",
   "type": "tipo_de_entidad_financiera",
   "label": "Entidad bursátil",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Entidad que opera en el mercado de valores, incluida en la categoría de exposiciones a empresas."
  },
  {
   "id": "entidad_nominada",
   "type": "sujeto_regulado",
   "label": "Entidad nominada",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Entidad financiera o casa de cambio designada por el importador para hacerse responsable del seguimiento de la oficialización y verificar el cumplimiento de con…"
  },
  {
   "id": "entidad_cambiaria",
   "type": "sujeto_regulado",
   "label": "Entidad cambiaria",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Instituciones especializadas en operaciones de cambio que deben suspender sus operaciones en caso de atraso en la validación del régimen informativo."
  },
  {
   "id": "deudor_en_concurso",
   "type": "categoria_de_deudor",
   "label": "Deudor en concurso",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Deudor en concurso o con acuerdo preventivo extrajudicial solicitado o en gestión judicial de cobro que, por un período de hasta 540 días, no haya presentado do…"
  }
 ]
}
```

--- paso 11 · buscar_nodos · input={"consulta": "comunicación información al deudor 10 días", "limite": 10} · runtime=2924 · re-ejecutado=2924 ---

```json
{
 "consulta": "comunicación información al deudor 10 días",
 "total_con_match": 153,
 "resultados": [
  {
   "id": "deudor",
   "type": "sujeto_regulado",
   "label": "Deudor",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Persona física o jurídica que mantiene financiaciones con la entidad y debe ser objeto de análisis de situación económica y financiera, así como de clasificació…"
  },
  {
   "id": "deudor_moroso",
   "type": "causal_de_demora",
   "label": "Deudor moroso",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Situación en que el importador u otro obligado al pago incumple sus obligaciones, justificando acciones judiciales por parte del exportador."
  },
  {
   "id": "umbral_del_10",
   "type": "limite_regulatorio",
   "label": "Umbral del 10%",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Porcentaje de participación en capital social ordinario que determina la aplicación de ajustes regulatorios en inversiones en otras entidades financieras."
  },
  {
   "id": "obligado_al_pago",
   "type": "sujeto_regulado",
   "label": "Obligado al pago",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Deudor cuya situación crediticia debe cumplir con condiciones específicas para que su obligación sea incluida en la titulización."
  },
  {
   "id": "plazo_de_90_dias",
   "type": "restriccion_temporal",
   "label": "Plazo de 90 días",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Período mínimo que debe transcurrir desde la adquisición de títulos valores en suscripción primaria antes de poder venderlos en mercado secundario con liquidaci…"
  },
  {
   "id": "deudor_en_concurso",
   "type": "categoria_de_deudor",
   "label": "Deudor en concurso",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Deudor en concurso o con acuerdo preventivo extrajudicial solicitado o en gestión judicial de cobro que, por un período de hasta 540 días, no haya presentado do…"
  },
  {
   "id": "periodo_de_45_dias",
   "type": "plazo_regulatorio",
   "label": "Período de 45 días",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Plazo máximo previo a la transferencia de activos dentro del cual el originante o fiduciario debe analizar las condiciones de cumplimiento."
  },
  {
   "id": "informacion_externa",
   "type": "fuente_de_validacion",
   "label": "Información externa",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Datos independientes utilizados para validar de modo consistente las valuaciones de exposiciones."
  },
  {
   "id": "posicion_al_contado",
   "type": "tipo_de_posicion_financiera",
   "label": "Posición al contado",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Posición subyacente que puede ser cubierta con derivados de crédito o swaps de rendimiento total, requiriendo coincidencia exacta de obligación de referencia."
  },
  {
   "id": "credito_unico_deudor",
   "type": "subclase_de_derivado_de_credito",
   "label": "Crédito único deudor",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Derivado de crédito referenciado a un único deudor, con factores regulatorios que varían según calificación crediticia (AAA a CCC)."
  }
 ]
}
```

--- paso 12 · buscar_nodos · input={"consulta": "información deudor 10 días hábiles comunicar", "limite": 10} · runtime=3003 · re-ejecutado=3003 ---

```json
{
 "consulta": "información deudor 10 días hábiles comunicar",
 "total_con_match": 84,
 "resultados": [
  {
   "id": "plazo_de_20_dias_habiles",
   "type": "plazo_regulatorio",
   "label": "Plazo de 20 días hábiles",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Plazo máximo dentro del cual debe ingresarse y liquidarse en el mercado de cambios el contravalor de enajenación de activos no financieros no producidos."
  },
  {
   "id": "plazo_de_revocacion_de_diez_dias_habiles",
   "type": "requisito_temporal",
   "label": "Plazo de revocación de diez días hábiles",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Plazo durante el cual el usuario puede revocar la aceptación del producto o servicio, contado a partir de la fecha de recibido el contrato o de la disponibilida…"
  },
  {
   "id": "deudor",
   "type": "sujeto_regulado",
   "label": "Deudor",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Persona física o jurídica que mantiene financiaciones con la entidad y debe ser objeto de análisis de situación económica y financiera, así como de clasificació…"
  },
  {
   "id": "deudor_moroso",
   "type": "causal_de_demora",
   "label": "Deudor moroso",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Situación en que el importador u otro obligado al pago incumple sus obligaciones, justificando acciones judiciales por parte del exportador."
  },
  {
   "id": "umbral_del_10",
   "type": "limite_regulatorio",
   "label": "Umbral del 10%",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Porcentaje de participación en capital social ordinario que determina la aplicación de ajustes regulatorios en inversiones en otras entidades financieras."
  },
  {
   "id": "plazo_de_90_dias",
   "type": "restriccion_temporal",
   "label": "Plazo de 90 días",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Período mínimo que debe transcurrir desde la adquisición de títulos valores en suscripción primaria antes de poder venderlos en mercado secundario con liquidaci…"
  },
  {
   "id": "deudor_en_concurso",
   "type": "categoria_de_deudor",
   "label": "Deudor en concurso",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Deudor en concurso o con acuerdo preventivo extrajudicial solicitado o en gestión judicial de cobro que, por un período de hasta 540 días, no haya presentado do…"
  },
  {
   "id": "periodo_de_45_dias",
   "type": "plazo_regulatorio",
   "label": "Período de 45 días",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Plazo máximo previo a la transferencia de activos dentro del cual el originante o fiduciario debe analizar las condiciones de cumplimiento."
  },
  {
   "id": "informacion_externa",
   "type": "fuente_de_validacion",
   "label": "Información externa",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Datos independientes utilizados para validar de modo consistente las valuaciones de exposiciones."
  },
  {
   "id": "credito_unico_deudor",
   "type": "subclase_de_derivado_de_credito",
   "label": "Crédito único deudor",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Derivado de crédito referenciado a un único deudor, con factores regulatorios que varían según calificación crediticia (AAA a CCC)."
  }
 ]
}
```

--- paso 13 · ver_nodo · input={"id": "deudor"} · runtime=1167 · re-ejecutado=1167 ---

```json
{
 "id": "deudor",
 "type": "sujeto_regulado",
 "label": "Deudor",
 "properties": {
  "description": "Persona física o jurídica que mantiene financiaciones con la entidad y debe ser objeto de análisis de situación económica y financiera, así como de clasificación periódica.",
  "version": "vigente",
  "type_raw": [
   "Sujeto regulado"
  ],
  "type_raw_counts": {
   "Sujeto regulado": 7
  },
  "name_variants": [],
  "n_observations": 7
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "p.1-8 / Sección 1.2.1"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "p.9-12 / Puntos 3.1, 3.2, 3.4"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "p.17-19 / Sección 6, punto 6.2"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "p.23-25 / Múltiples referencias a lo largo del fragmento"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "p.26-28 / Punto 6.5.4 y siguientes"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "p.33-35 / Punto 7.1, 7.2"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "p.39-43 / Sección 7, punto 7.3 y siguientes"
  }
 ]
}
```

--- paso 14 · buscar_nodos · input={"consulta": "10 días hábiles comunicación clasificación", "limite": 10} · runtime=2980 · re-ejecutado=2980 ---

```json
{
 "consulta": "10 días hábiles comunicación clasificación",
 "total_con_match": 54,
 "resultados": [
  {
   "id": "plazo_de_20_dias_habiles",
   "type": "plazo_regulatorio",
   "label": "Plazo de 20 días hábiles",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Plazo máximo dentro del cual debe ingresarse y liquidarse en el mercado de cambios el contravalor de enajenación de activos no financieros no producidos."
  },
  {
   "id": "plazo_de_revocacion_de_diez_dias_habiles",
   "type": "requisito_temporal",
   "label": "Plazo de revocación de diez días hábiles",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Plazo durante el cual el usuario puede revocar la aceptación del producto o servicio, contado a partir de la fecha de recibido el contrato o de la disponibilida…"
  },
  {
   "id": "umbral_del_10",
   "type": "limite_regulatorio",
   "label": "Umbral del 10%",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Porcentaje de participación en capital social ordinario que determina la aplicación de ajustes regulatorios en inversiones en otras entidades financieras."
  },
  {
   "id": "plazo_de_90_dias",
   "type": "restriccion_temporal",
   "label": "Plazo de 90 días",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Período mínimo que debe transcurrir desde la adquisición de títulos valores en suscripción primaria antes de poder venderlos en mercado secundario con liquidaci…"
  },
  {
   "id": "periodo_de_45_dias",
   "type": "plazo_regulatorio",
   "label": "Período de 45 días",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Plazo máximo previo a la transferencia de activos dentro del cual el originante o fiduciario debe analizar las condiciones de cumplimiento."
  },
  {
   "id": "ponderador_minimo_10",
   "type": "limite_regulatorio",
   "label": "Ponderador mínimo 10%",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Ponderador mínimo aplicable a tramos de máxima preferencia de titulizaciones que cumplen criterios STC."
  },
  {
   "id": "atraso_mayor_a_31_dias",
   "type": "condicion_de_pago",
   "label": "Atraso mayor a 31 días",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Retraso en el pago de servicios de deuda refinanciada que supera los 31 días, generando reclasificación inmediata."
  },
  {
   "id": "tarea_de_clasificacion",
   "type": "funcion_regulatoria",
   "label": "Tarea de clasificación",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Proceso de asignación de categorías de riesgo a deudores, que puede ser encomendada a un área independiente, al sector de créditos con revisión independiente, o…"
  },
  {
   "id": "atraso_de_hasta_31_dias",
   "type": "condicion_de_pago",
   "label": "Atraso de hasta 31 días",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Retraso en el pago que no supera los 31 días, permitiendo reclasificación en nivel superior bajo ciertas condiciones."
  },
  {
   "id": "atraso_de_hasta_540_dias",
   "type": "condicion_de_pago",
   "label": "Atraso de hasta 540 días",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Retraso de hasta 540 días para deudores en concurso preventivo, acuerdo preventivo extrajudicial o gestión judicial."
  }
 ]
}
```

--- paso 15 · ver_vecinos · input={"id": "deudor", "direccion": "salientes"} · runtime=6930 · re-ejecutado=6930 ---

```json
{
 "id": "deudor",
 "label": "Deudor",
 "n_salientes_total": 28,
 "n_entrantes_total": 20,
 "salientes": [
  {
   "relation": "es_evaluado_segun",
   "vecino_id": "capacidad_de_repago",
   "vecino_label": "Capacidad de repago",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "p.17-19 / Sección 6, punto 6.2"
    }
   ]
  },
  {
   "relation": "puede_presentar",
   "vecino_id": "exposicion_en_moneda_extranjera",
   "vecino_label": "Exposición en moneda extranjera",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "p.17-19 / Sección 6, punto 6.2"
    }
   ]
  },
  {
   "relation": "tiene_ingresos_y_egresos_vinculados_a",
   "vecino_id": "coeficiente_de_estabilizacion_de_referencia",
   "vecino_label": "Coeficiente de Estabilización de Referencia",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "p.17-19 / Sección 6, punto 6.2"
    }
   ]
  },
  {
   "relation": "se_clasifica_segun_umbral_de",
   "vecino_id": "responsabilidad_patrimonial_computable_rpc",
   "vecino_label": "Responsabilidad patrimonial computable (RPC)",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "p.17-19 / Sección 6, punto 6.3.1"
    }
   ]
  },
  {
   "relation": "es_registrado_en",
   "vecino_id": "central_de_deudores_del_sistema_financiero",
   "vecino_label": "Central de deudores del sistema financiero",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "p.17-19 / Sección 6, punto 6.4.2"
    }
   ]
  },
  {
   "relation": "se_incluye_en",
   "vecino_id": "categoria_de_clasificacion",
   "vecino_label": "Categoría de clasificación",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "p.17-19 / Sección 6, punto 6.5"
    }
   ]
  },
  {
   "relation": "debe_concertar_acuerdo_con",
   "vecino_id": "entidad_financiera",
   "vecino_label": "Entidad financiera",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "p.23-25 / Párrafo inicial sobre plazo de 90 o 180 días"
    }
   ]
  },
  {
   "relation": "incurre_en",
   "vecino_id": "mora_en_el_pago",
   "vecino_label": "Mora en el pago",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "p.23-25 / Múltiples puntos 6.5.3.x"
    }
   ]
  },
  {
   "relation": "recibe",
   "vecino_id": "refinanciacion",
   "vecino_label": "Refinanciación",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "p.23-25 / Múltiples referencias a lo largo del fragmento"
    }
   ]
  },
  {
   "relation": "puede_ser_clasificado_en",
   "vecino_id": "situacion_normal",
   "vecino_label": "Situación normal",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "p.23-25 / Párrafo sobre cancelación de intereses devengados"
    }
   ]
  },
  {
   "relation": "debe_ser_reclasificado_en",
   "vecino_id": "con_alto_riesgo_de_insolvencia",
   "vecino_label": "Con alto riesgo de insolvencia",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "p.23-25 / Párrafo sobre no cancelación de intereses en 180 días"
    }
   ]
  },
  {
   "relation": "puede_ser_clasificado_en",
   "vecino_id": "con_problemas",
   "vecino_label": "Con problemas",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "p.23-25 / Punto 6.5.3"
    }
   ]
  },
  {
   "relation": "puede_ser_reclasificado_en",
   "vecino_id": "en_observacion",
   "vecino_label": "En observación",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "p.23-25 / Punto 6.5.3.5"
    }
   ]
  },
  {
   "relation": "recibe",
   "vecino_id": "credito_adicional",
   "vecino_label": "Crédito adicional",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "p.23-25 / Párrafos sobre permanencia en categoría por 180 días"
    }
   ]
  },
  {
   "relation": "puede_ser_reclasificado_en",
   "vecino_id": "en_tratamiento_especial",
   "vecino_label": "En tratamiento especial",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "p.23-25 / Punto 6.5.2.3"
    }
   ]
  },
  {
   "relation": "es_analizado_mediante",
   "vecino_id": "flujo_de_fondos",
   "vecino_label": "Flujo de fondos",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "p.23-25 / Punto 6.5.3"
    }
   ]
  },
  {
   "relation": "pertenece_a",
   "vecino_id": "grupo_de_contrapartes_conectadas",
   "vecino_label": "Grupo de contrapartes conectadas",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "p.23-25 / Punto 6.5.3.1"
    }
   ]
  },
  {
   "relation": "posee",
   "vecino_id": "direccion_del_deudor",
   "vecino_label": "Dirección del deudor",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "p.23-25 / Punto 6.5.3.3"
    }
   ]
  },
  {
   "relation": "mantiene",
   "vecino_id": "sistema_de_control_interno",
   "vecino_label": "Sistema de control interno",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "p.23-25 / Punto 6.5.3.3"
    }
   ]
  },
  {
   "relation": "cuenta_con",
   "vecino_id": "sistema_de_informacion",
   "vecino_label": "Sistema de información",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "p.23-25 / Punto 6.5.3.4"
    }
   ]
  },
  {
   "relation": "pertenece_a",
   "vecino_id": "sector_de_actividad_economica",
   "vecino_label": "Sector de actividad económica",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "p.23-25 / Punto 6.5.3.8"
    }
   ]
  },
  {
   "relation": "puede_ser_sujeto_de",
   "vecino_id": "demanda_judicial",
   "vecino_label": "Demanda judicial",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "p.23-25 / Punto 6.5.3.11"
    }
   ]
  },
  {
   "relation": "puede_ser_asignado_a",
   "vecino_id": "clasificacion_con_alto_riesgo_de_insolvencia",
   "vecino_label": "Clasificación con alto riesgo de insolvencia",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "p.26-28 / Punto 6.5.4"
    }
   ]
  },
  {
   "relation": "puede_ser_asignado_a",
   "vecino_id": "clasificacion_irrecuperable",
   "vecino_label": "Clasificación irrecuperable",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "p.26-28 / Punto 6.5.5"
    }
   ]
  },
  {
   "relation": "asume",
   "vecino_id": "obligacion_de_credito",
   "vecino_label": "Obligación de crédito",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "p.33-35 / Punto 7.1"
    }
   ]
  },
  {
   "relation": "es_clasificado_por",
   "vecino_id": "entidad_financiera",
   "vecino_label": "Entidad financiera",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "p.39-43 / Sección 7, punto 7.3"
    }
   ]
  },
  {
   "relation": "es_registrado_en",
   "vecino_id": "central_de_deudores_del_sistema_financiero",
   "vecino_label": "Central de deudores del sistema financiero",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "p.39-43 / Sección 7, punto 7.3"
    }
   ]
  },
  {
   "relation": "es_sujeto_de",
   "vecino_id": "refinanciacion_de_deuda",
   "vecino_label": "Refinanciación de deuda",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "p.39-43 / Sección 7, párrafo inicial"
    }
   ]
  }
 ],
 "salientes_truncado": false
}
```

---

# Sección 3 — run_4/CQ-021

## 3a. Respuesta final del agente (verbatim, `posthoc_run/traces/off/run_4/CQ-021.json`)

`trace.final_json`:

```json
{
 "respuesta": "Según la regulación del BCRA, la entidad financiera debe comunicar al deudor un cambio negativo en su clasificación dentro de 45 días mediante medios especificados. Sin embargo, existen excepciones según el saldo de deuda del deudor. La información disponible en el Knowledge Graph indica que hay casos en que esta comunicación es optativa dependiendo del saldo de deuda, y que el umbral depende de un régimen específico, pero los detalles concretos sobre cuáles son esos casos optativos y de qué régimen exactamente depende el umbral no están completamente desarrollados en los nodos consultados.",
 "citas": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "p.9-12 / Punto 3.4.2"
  }
 ],
 "respondible": false
}
```

`trace.final_raw` (turno final íntegro):

```
Basándome en la información recolectada del Knowledge Graph, he encontrado que existe un nodo sobre "Cambio negativo en clasificación" que menciona excepciones según el saldo de deuda, pero no he podido acceder a los detalles específicos sobre los casos optativos ni sobre el régimen que determina el umbral, ya que la información completa no está disponible en los nodos que pude consultar.

```json
{
  "respuesta": "Según la regulación del BCRA, la entidad financiera debe comunicar al deudor un cambio negativo en su clasificación dentro de 45 días mediante medios especificados. Sin embargo, existen excepciones según el saldo de deuda del deudor. La información disponible en el Knowledge Graph indica que hay casos en que esta comunicación es optativa dependiendo del saldo de deuda, y que el umbral depende de un régimen específico, pero los detalles concretos sobre cuáles son esos casos optativos y de qué régimen exactamente depende el umbral no están completamente desarrollados en los nodos consultados.",
  "citas": [
    {
      "source_doc": "TO_clasificacion_deudores_actual.pdf",
      "location": "p.9-12 / Punto 3.4.2"
    }
  ],
  "respondible": false
}
```
```

## 3b. Inventario de pasos (runtime vs. almacenado vs. re-ejecutado)

| paso | tool | input | chars runtime | chars almacenados | re-ejecutado |
|---|---|---|---|---|---|
| 1 | buscar_nodos | `{"consulta": "optativo comunicar deudor cambio clasificación", "limite": 10}` | 2743 | 1215 | = runtime ✓ |
| 2 | buscar_nodos | `{"consulta": "comunicación cambio negativo clasificación deudor", "limite": 10}` | 2746 | 1215 | = runtime ✓ |
| 3 | ver_nodo | `{"id": "cambio_negativo_en_clasificacion"}` | 570 | 570 | = runtime ✓ |
| 4 | ver_vecinos | `{"id": "cambio_negativo_en_clasificacion", "direccion": "ambas"}` | 737 | 737 | = runtime ✓ |
| 5 | buscar_nodos | `{"consulta": "optativo saldo deuda umbral comunicación", "limite": 10}` | 2825 | 1215 | = runtime ✓ |
| 6 | buscar_nodos | `{"consulta": "excepción comunicación clasificación saldo", "limite": 10}` | 2956 | 1215 | = runtime ✓ |
| 7 | buscar_nodos | `{"consulta": "régimen comunicación optativa deudor", "limite": 10}` | 2799 | 1215 | = runtime ✓ |
| 8 | buscar_nodos | `{"consulta": "comunicación optativa cambio clasificación régimen", "limite": 10}` | 2912 | 1215 | = runtime ✓ |
| 9 | buscar_nodos | `{"consulta": "régimen clasificación deudores excepciones", "limite": 10}` | 2918 | 1215 | = runtime ✓ |
| 10 | buscar_nodos | `{"consulta": "pequeño deudor comunicación clasificación", "limite": 10}` | 2959 | 1215 | = runtime ✓ |
| 11 | buscar_nodos | `{"consulta": "régimen simplificado pequeños deudores", "limite": 10}` | 2907 | 1215 | = runtime ✓ |
| 12 | buscar_nodos | `{"consulta": "45 días comunicación deudor saldo", "limite": 10}` | 2941 | 1215 | = runtime ✓ |
| 13 | ver_nodo | `{"id": "periodo_de_45_dias"}` | 512 | 512 | = runtime ✓ |
| 14 | ver_vecinos | `{"id": "periodo_de_45_dias", "direccion": "ambas"}` | 605 | 605 | = runtime ✓ |
| 15 | buscar_nodos | `{"consulta": "pequeño deudor régimen", "limite": 10}` | 2785 | 1215 | = runtime ✓ |
| 16 | buscar_nodos | `{"consulta": "comunicación cambio clasificación 45 días optativo", "limite": 10}` | 2898 | 1215 | = runtime ✓ |

**Fidelidad runtime↔re-ejecución: 16/16 pasos con largo idéntico.**

## 3c. APÉNDICE — outputs completos re-ejecutados (16 pasos)


--- paso 1 · buscar_nodos · input={"consulta": "optativo comunicar deudor cambio clasificación", "limite": 10} · runtime=2743 · re-ejecutado=2743 ---

```json
{
 "consulta": "optativo comunicar deudor cambio clasificación",
 "total_con_match": 59,
 "resultados": [
  {
   "id": "cambio_negativo_en_clasificacion",
   "type": "evento_regulatorio",
   "label": "Cambio negativo en clasificación",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Reclasificación desfavorable del deudor que debe ser comunicada al deudor dentro de 45 días mediante medios especificados, con excepciones según el saldo de deu…"
  },
  {
   "id": "deudor",
   "type": "sujeto_regulado",
   "label": "Deudor",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Persona física o jurídica que mantiene financiaciones con la entidad y debe ser objeto de análisis de situación económica y financiera, así como de clasificació…"
  },
  {
   "id": "deudor_moroso",
   "type": "causal_de_demora",
   "label": "Deudor moroso",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Situación en que el importador u otro obligado al pago incumple sus obligaciones, justificando acciones judiciales por parte del exportador."
  },
  {
   "id": "casa_de_cambio",
   "type": "sujeto_regulado",
   "label": "Casa de cambio",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Entidad cambiaria que opera en el mercado de cambios, sujeta a requisitos operativos mínimos de tecnología y sistemas de información."
  },
  {
   "id": "tipo_de_cambio",
   "type": "clase_de_activo",
   "label": "Tipo de cambio",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Clase de activo subyacente en derivados, con factor regulatorio de 4%, correlación N/A y volatilidad de opción de 15%."
  },
  {
   "id": "venta_de_cambio",
   "type": "operacion_regulada",
   "label": "Venta de cambio",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Operación de cambio para transferencias a personas humanas en el exterior."
  },
  {
   "id": "boleto_de_cambio",
   "type": "documento_regulado",
   "label": "Boleto de cambio",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Documento que debe constar el carácter de declaración jurada del ordenante sobre todos los datos contenidos, incluyendo el concepto de la operación y cumplimien…"
  },
  {
   "id": "compra_de_cambio",
   "type": "operacion_regulada",
   "label": "Compra de cambio",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Operación de cambio para transferencias a personas humanas residentes en el país."
  },
  {
   "id": "riesgo_de_cambio",
   "type": "tipo_de_riesgo",
   "label": "Riesgo de cambio",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Riesgo calculado conforme al punto 6.4.3 de las normas sobre Capitales mínimos, utilizando códigos de partida específicos y un factor de ponderación del 0.08."
  },
  {
   "id": "agencia_de_cambio",
   "type": "sujeto_regulado",
   "label": "Agencia de cambio",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Entidad cambiaria cuyas tenencias en moneda extranjera están limitadas por regulación del BCRA."
  }
 ]
}
```

--- paso 2 · buscar_nodos · input={"consulta": "comunicación cambio negativo clasificación deudor", "limite": 10} · runtime=2746 · re-ejecutado=2746 ---

```json
{
 "consulta": "comunicación cambio negativo clasificación deudor",
 "total_con_match": 60,
 "resultados": [
  {
   "id": "cambio_negativo_en_clasificacion",
   "type": "evento_regulatorio",
   "label": "Cambio negativo en clasificación",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Reclasificación desfavorable del deudor que debe ser comunicada al deudor dentro de 45 días mediante medios especificados, con excepciones según el saldo de deu…"
  },
  {
   "id": "deudor",
   "type": "sujeto_regulado",
   "label": "Deudor",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Persona física o jurídica que mantiene financiaciones con la entidad y debe ser objeto de análisis de situación económica y financiera, así como de clasificació…"
  },
  {
   "id": "deudor_moroso",
   "type": "causal_de_demora",
   "label": "Deudor moroso",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Situación en que el importador u otro obligado al pago incumple sus obligaciones, justificando acciones judiciales por parte del exportador."
  },
  {
   "id": "casa_de_cambio",
   "type": "sujeto_regulado",
   "label": "Casa de cambio",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Entidad cambiaria que opera en el mercado de cambios, sujeta a requisitos operativos mínimos de tecnología y sistemas de información."
  },
  {
   "id": "tipo_de_cambio",
   "type": "clase_de_activo",
   "label": "Tipo de cambio",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Clase de activo subyacente en derivados, con factor regulatorio de 4%, correlación N/A y volatilidad de opción de 15%."
  },
  {
   "id": "venta_de_cambio",
   "type": "operacion_regulada",
   "label": "Venta de cambio",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Operación de cambio para transferencias a personas humanas en el exterior."
  },
  {
   "id": "boleto_de_cambio",
   "type": "documento_regulado",
   "label": "Boleto de cambio",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Documento que debe constar el carácter de declaración jurada del ordenante sobre todos los datos contenidos, incluyendo el concepto de la operación y cumplimien…"
  },
  {
   "id": "compra_de_cambio",
   "type": "operacion_regulada",
   "label": "Compra de cambio",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Operación de cambio para transferencias a personas humanas residentes en el país."
  },
  {
   "id": "riesgo_de_cambio",
   "type": "tipo_de_riesgo",
   "label": "Riesgo de cambio",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Riesgo calculado conforme al punto 6.4.3 de las normas sobre Capitales mínimos, utilizando códigos de partida específicos y un factor de ponderación del 0.08."
  },
  {
   "id": "agencia_de_cambio",
   "type": "sujeto_regulado",
   "label": "Agencia de cambio",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Entidad cambiaria cuyas tenencias en moneda extranjera están limitadas por regulación del BCRA."
  }
 ]
}
```

--- paso 3 · ver_nodo · input={"id": "cambio_negativo_en_clasificacion"} · runtime=570 · re-ejecutado=570 ---

```json
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
```

--- paso 4 · ver_vecinos · input={"id": "cambio_negativo_en_clasificacion", "direccion": "ambas"} · runtime=737 · re-ejecutado=737 ---

```json
{
 "id": "cambio_negativo_en_clasificacion",
 "label": "Cambio negativo en clasificación",
 "n_salientes_total": 0,
 "n_entrantes_total": 2,
 "salientes": [],
 "salientes_truncado": false,
 "entrantes": [
  {
   "relation": "debe_comunicar_al_deudor",
   "vecino_id": "entidad_financiera",
   "vecino_label": "Entidad financiera",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "p.9-12 / Punto 3.4.2"
    }
   ]
  },
  {
   "relation": "debe_ser_notificado_de",
   "vecino_id": "deudor_en_gestion_judicial_o_extrajudicial_de_cobro",
   "vecino_label": "Deudor en gestión judicial o extrajudicial de cobro",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "p.9-12 / Punto 3.4.2"
    }
   ]
  }
 ],
 "entrantes_truncado": false
}
```

--- paso 5 · buscar_nodos · input={"consulta": "optativo saldo deuda umbral comunicación", "limite": 10} · runtime=2825 · re-ejecutado=2825 ---

```json
{
 "consulta": "optativo saldo deuda umbral comunicación",
 "total_con_match": 89,
 "resultados": [
  {
   "id": "saldo_de_deuda",
   "type": "componente_de_exposicion",
   "label": "Saldo de deuda",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Importe adeudado por la contraparte, incluido en el cálculo de exposición."
  },
  {
   "id": "saldo_de_deuda_pendiente",
   "type": "componente_de_ltv",
   "label": "Saldo de deuda pendiente",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Saldo de deuda sin deducir previsiones por riesgo de incobrabilidad ni coberturas del riesgo de crédito."
  },
  {
   "id": "declaracion_jurada_de_saldo_de_deuda_pendiente",
   "type": "requisito_de_verificacion",
   "label": "Declaración jurada de saldo de deuda pendiente",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Para importaciones oficializadas con anterioridad al 01/11/19, declaración jurada consignando el saldo de deuda pendiente a la fecha, firmada por el importador …"
  },
  {
   "id": "saldo_bruto",
   "type": "medida_de_exposicion",
   "label": "Saldo bruto",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Monto bruto de exposiciones minoristas sin computar coberturas del riesgo de crédito."
  },
  {
   "id": "deuda_elegible",
   "type": "obligacion_financiera",
   "label": "Deuda elegible",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Deuda comercial por importación que cumple con los requisitos de los puntos 4.4 y 4.5, respecto de la cual se pueden suscribir BOPREAL."
  },
  {
   "id": "umbral_del_10",
   "type": "limite_regulatorio",
   "label": "Umbral del 10%",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Porcentaje de participación en capital social ordinario que determina la aplicación de ajustes regulatorios en inversiones en otras entidades financieras."
  },
  {
   "id": "deuda_comercial",
   "type": "categoria_regulatoria",
   "label": "Deuda comercial",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Categoría de obligación que debe cumplir la línea de crédito del exterior para que la entidad financiera pueda acceder al mercado de cambios."
  },
  {
   "id": "titulo_de_deuda",
   "type": "instrumento_financiero",
   "label": "Título de deuda",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Valor mobiliario emitido por residentes en moneda extranjera, sujeto a recompra, rescate o precancelación de capital e intereses."
  },
  {
   "id": "emision_de_deuda",
   "type": "instrumento_financiero",
   "label": "Emisión de deuda",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Deuda emitida por un prestatario que puede contar con calificación específica utilizada para determinar ponderador de riesgo de exposiciones crediticias."
  },
  {
   "id": "titulos_de_deuda",
   "type": "instrumento_financiero",
   "label": "Títulos de deuda",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Instrumentos imputados a cartera de negociación respecto de los cuales se calcula exigencia de capital por riesgo de tasa de interés."
  }
 ]
}
```

--- paso 6 · buscar_nodos · input={"consulta": "excepción comunicación clasificación saldo", "limite": 10} · runtime=2956 · re-ejecutado=2956 ---

```json
{
 "consulta": "excepción comunicación clasificación saldo",
 "total_con_match": 17,
 "resultados": [
  {
   "id": "saldo_bruto",
   "type": "medida_de_exposicion",
   "label": "Saldo bruto",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Monto bruto de exposiciones minoristas sin computar coberturas del riesgo de crédito."
  },
  {
   "id": "saldo_de_deuda",
   "type": "componente_de_exposicion",
   "label": "Saldo de deuda",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Importe adeudado por la contraparte, incluido en el cálculo de exposición."
  },
  {
   "id": "tarea_de_clasificacion",
   "type": "funcion_regulatoria",
   "label": "Tarea de clasificación",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Proceso de asignación de categorías de riesgo a deudores, que puede ser encomendada a un área independiente, al sector de créditos con revisión independiente, o…"
  },
  {
   "id": "saldo_de_deuda_pendiente",
   "type": "componente_de_ltv",
   "label": "Saldo de deuda pendiente",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Saldo de deuda sin deducir previsiones por riesgo de incobrabilidad ni coberturas del riesgo de crédito."
  },
  {
   "id": "clasificacion_de_deudores",
   "type": "tarea_regulatoria",
   "label": "Clasificación de deudores",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Clasificación que debe efectuarse con una periodicidad que atienda a la importancia del deudor, considerando la totalidad de las financiaciones comprendidas, de…"
  },
  {
   "id": "categoria_de_clasificacion",
   "type": "nivel_de_riesgo",
   "label": "Categoría de clasificación",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Una de las cinco categorías en que se clasifica a cada cliente y la totalidad de sus financiaciones comprendidas."
  },
  {
   "id": "saldo_pendiente_de_entrega",
   "type": "excepcion_a_regularizacion",
   "label": "Saldo pendiente de entrega",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Situación en la cual el importador puede optar por no demostrar la oficialización del ingreso de bienes o divisas, dentro de límites establecidos."
  },
  {
   "id": "clasificacion_irrecuperable",
   "type": "categoria_de_clasificacion_de_deudores",
   "label": "Clasificación irrecuperable",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Categoría de riesgo para deudas consideradas incobrables, donde la incobrabilidad es evidente al momento del análisis, aunque podrían tener algún valor de recup…"
  },
  {
   "id": "cambio_negativo_en_clasificacion",
   "type": "evento_regulatorio",
   "label": "Cambio negativo en clasificación",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Reclasificación desfavorable del deudor que debe ser comunicada al deudor dentro de 45 días mediante medios especificados, con excepciones según el saldo de deu…"
  },
  {
   "id": "saldo_pendiente_de_regularizacion",
   "type": "concepto_regulatorio",
   "label": "Saldo pendiente de regularización",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Monto de pagos anticipados de importaciones que aún no han sido regularizados mediante el registro de ingreso aduanero."
  }
 ]
}
```

--- paso 7 · buscar_nodos · input={"consulta": "régimen comunicación optativa deudor", "limite": 10} · runtime=2799 · re-ejecutado=2799 ---

```json
{
 "consulta": "régimen comunicación optativa deudor",
 "total_con_match": 58,
 "resultados": [
  {
   "id": "deudor",
   "type": "sujeto_regulado",
   "label": "Deudor",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Persona física o jurídica que mantiene financiaciones con la entidad y debe ser objeto de análisis de situación económica y financiera, así como de clasificació…"
  },
  {
   "id": "deudor_moroso",
   "type": "causal_de_demora",
   "label": "Deudor moroso",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Situación en que el importador u otro obligado al pago incumple sus obligaciones, justificando acciones judiciales por parte del exportador."
  },
  {
   "id": "regimen_de_rancho",
   "type": "regimen_aduanero_exceptuado",
   "label": "Régimen de rancho",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Régimen aduanero exceptuado del seguimiento conforme a los artículos 506 al 516 de la Ley 22.415, aplicable a medios de transporte de bandera nacional."
  },
  {
   "id": "deudor_en_concurso",
   "type": "categoria_de_deudor",
   "label": "Deudor en concurso",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Deudor en concurso o con acuerdo preventivo extrajudicial solicitado o en gestión judicial de cobro que, por un período de hasta 540 días, no haya presentado do…"
  },
  {
   "id": "regimen_de_equipaje",
   "type": "regimen_aduanero_exceptuado",
   "label": "Régimen de equipaje",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Régimen aduanero exceptuado del seguimiento conforme a los artículos 488 al 505 de la Ley 22.415."
  },
  {
   "id": "regimen_de_muestras",
   "type": "regimen_aduanero_exceptuado",
   "label": "Régimen de muestras",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Régimen aduanero exceptuado del seguimiento conforme a los artículos 560 al 565 de la Ley 22.415."
  },
  {
   "id": "regimen_de_removido",
   "type": "regimen_aduanero_exceptuado",
   "label": "Régimen de removido",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Régimen aduanero exceptuado del seguimiento conforme a los artículos 386 al 396 de la Ley 22.415."
  },
  {
   "id": "credito_unico_deudor",
   "type": "subclase_de_derivado_de_credito",
   "label": "Crédito único deudor",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Derivado de crédito referenciado a un único deudor, con factores regulatorios que varían según calificación crediticia (AAA a CCC)."
  },
  {
   "id": "deudor_no_calificado",
   "type": "categoria_de_contraparte",
   "label": "Deudor no calificado",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Contraparte sin calificación de crédito otorgada por ECAI, que recibe ponderador de riesgo no menor al del país de constitución."
  },
  {
   "id": "direccion_del_deudor",
   "type": "componente_organizacional",
   "label": "Dirección del deudor",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Gestión y liderazgo del deudor, evaluados por su capacidad, experiencia y honestidad."
  }
 ]
}
```

--- paso 8 · buscar_nodos · input={"consulta": "comunicación optativa cambio clasificación régimen", "limite": 10} · runtime=2912 · re-ejecutado=2912 ---

```json
{
 "consulta": "comunicación optativa cambio clasificación régimen",
 "total_con_match": 81,
 "resultados": [
  {
   "id": "cambio_negativo_en_clasificacion",
   "type": "evento_regulatorio",
   "label": "Cambio negativo en clasificación",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Reclasificación desfavorable del deudor que debe ser comunicada al deudor dentro de 45 días mediante medios especificados, con excepciones según el saldo de deu…"
  },
  {
   "id": "regimen_informatico_de_operaciones_de_cambio_rioc",
   "type": "sistema_regulatorio",
   "label": "Régimen informático de operaciones de cambio (RIOC)",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Sistema mediante el cual la entidad financiera debe registrar el aporte de capital confeccionando dos boletos de cambio sin movimiento de fondos."
  },
  {
   "id": "regimen_informativo_de_operaciones_de_cambio_rioc",
   "type": "mecanismo_de_registro",
   "label": "Régimen informativo de operaciones de cambio (RIOC)",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Sistema ante el BCRA mediante el cual la entidad financiera registra la financiación una vez verificado el registro de ingreso aduanero de los bienes."
  },
  {
   "id": "casa_de_cambio",
   "type": "sujeto_regulado",
   "label": "Casa de cambio",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Entidad cambiaria que opera en el mercado de cambios, sujeta a requisitos operativos mínimos de tecnología y sistemas de información."
  },
  {
   "id": "tipo_de_cambio",
   "type": "clase_de_activo",
   "label": "Tipo de cambio",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Clase de activo subyacente en derivados, con factor regulatorio de 4%, correlación N/A y volatilidad de opción de 15%."
  },
  {
   "id": "venta_de_cambio",
   "type": "operacion_regulada",
   "label": "Venta de cambio",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Operación de cambio para transferencias a personas humanas en el exterior."
  },
  {
   "id": "boleto_de_cambio",
   "type": "documento_regulado",
   "label": "Boleto de cambio",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Documento que debe constar el carácter de declaración jurada del ordenante sobre todos los datos contenidos, incluyendo el concepto de la operación y cumplimien…"
  },
  {
   "id": "compra_de_cambio",
   "type": "operacion_regulada",
   "label": "Compra de cambio",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Operación de cambio para transferencias a personas humanas residentes en el país."
  },
  {
   "id": "riesgo_de_cambio",
   "type": "tipo_de_riesgo",
   "label": "Riesgo de cambio",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Riesgo calculado conforme al punto 6.4.3 de las normas sobre Capitales mínimos, utilizando códigos de partida específicos y un factor de ponderación del 0.08."
  },
  {
   "id": "agencia_de_cambio",
   "type": "sujeto_regulado",
   "label": "Agencia de cambio",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Entidad cambiaria cuyas tenencias en moneda extranjera están limitadas por regulación del BCRA."
  }
 ]
}
```

--- paso 9 · buscar_nodos · input={"consulta": "régimen clasificación deudores excepciones", "limite": 10} · runtime=2918 · re-ejecutado=2918 ---

```json
{
 "consulta": "régimen clasificación deudores excepciones",
 "total_con_match": 54,
 "resultados": [
  {
   "id": "clasificacion_de_deudores",
   "type": "tarea_regulatoria",
   "label": "Clasificación de deudores",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Clasificación que debe efectuarse con una periodicidad que atienda a la importancia del deudor, considerando la totalidad de las financiaciones comprendidas, de…"
  },
  {
   "id": "regimen_de_rancho",
   "type": "regimen_aduanero_exceptuado",
   "label": "Régimen de rancho",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Régimen aduanero exceptuado del seguimiento conforme a los artículos 506 al 516 de la Ley 22.415, aplicable a medios de transporte de bandera nacional."
  },
  {
   "id": "regimen_de_equipaje",
   "type": "regimen_aduanero_exceptuado",
   "label": "Régimen de equipaje",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Régimen aduanero exceptuado del seguimiento conforme a los artículos 488 al 505 de la Ley 22.415."
  },
  {
   "id": "regimen_de_muestras",
   "type": "regimen_aduanero_exceptuado",
   "label": "Régimen de muestras",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Régimen aduanero exceptuado del seguimiento conforme a los artículos 560 al 565 de la Ley 22.415."
  },
  {
   "id": "regimen_de_removido",
   "type": "regimen_aduanero_exceptuado",
   "label": "Régimen de removido",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Régimen aduanero exceptuado del seguimiento conforme a los artículos 386 al 396 de la Ley 22.415."
  },
  {
   "id": "regimen_de_pacotilla",
   "type": "regimen_aduanero_exceptuado",
   "label": "Régimen de pacotilla",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Régimen aduanero exceptuado del seguimiento conforme a los artículos 517 al 528 de la Ley 22.415."
  },
  {
   "id": "regimen_exporta_simple",
   "type": "regimen_regulatorio",
   "label": "Régimen EXPORTA SIMPLE",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Régimen especial para exportaciones con plazo de 365 días corridos para ingreso y liquidación de divisas, independientemente del tipo de bien exportado."
  },
  {
   "id": "tarea_de_clasificacion",
   "type": "funcion_regulatoria",
   "label": "Tarea de clasificación",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Proceso de asignación de categorías de riesgo a deudores, que puede ser encomendada a un área independiente, al sector de créditos con revisión independiente, o…"
  },
  {
   "id": "regimen_de_transparencia",
   "type": "herramienta_regulatoria",
   "label": "Régimen de Transparencia",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Régimen elaborado por el BCRA sobre la base de información proporcionada por sujetos obligados para que los usuarios comparen costos, características y requisit…"
  },
  {
   "id": "categoria_de_clasificacion",
   "type": "nivel_de_riesgo",
   "label": "Categoría de clasificación",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Una de las cinco categorías en que se clasifica a cada cliente y la totalidad de sus financiaciones comprendidas."
  }
 ]
}
```

--- paso 10 · buscar_nodos · input={"consulta": "pequeño deudor comunicación clasificación", "limite": 10} · runtime=2959 · re-ejecutado=2959 ---

```json
{
 "consulta": "pequeño deudor comunicación clasificación",
 "total_con_match": 24,
 "resultados": [
  {
   "id": "deudor",
   "type": "sujeto_regulado",
   "label": "Deudor",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Persona física o jurídica que mantiene financiaciones con la entidad y debe ser objeto de análisis de situación económica y financiera, así como de clasificació…"
  },
  {
   "id": "deudor_moroso",
   "type": "causal_de_demora",
   "label": "Deudor moroso",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Situación en que el importador u otro obligado al pago incumple sus obligaciones, justificando acciones judiciales por parte del exportador."
  },
  {
   "id": "deudor_en_concurso",
   "type": "categoria_de_deudor",
   "label": "Deudor en concurso",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Deudor en concurso o con acuerdo preventivo extrajudicial solicitado o en gestión judicial de cobro que, por un período de hasta 540 días, no haya presentado do…"
  },
  {
   "id": "credito_unico_deudor",
   "type": "subclase_de_derivado_de_credito",
   "label": "Crédito único deudor",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Derivado de crédito referenciado a un único deudor, con factores regulatorios que varían según calificación crediticia (AAA a CCC)."
  },
  {
   "id": "deudor_no_calificado",
   "type": "categoria_de_contraparte",
   "label": "Deudor no calificado",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Contraparte sin calificación de crédito otorgada por ECAI, que recibe ponderador de riesgo no menor al del país de constitución."
  },
  {
   "id": "direccion_del_deudor",
   "type": "componente_organizacional",
   "label": "Dirección del deudor",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Gestión y liderazgo del deudor, evaluados por su capacidad, experiencia y honestidad."
  },
  {
   "id": "tarea_de_clasificacion",
   "type": "funcion_regulatoria",
   "label": "Tarea de clasificación",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Proceso de asignación de categorías de riesgo a deudores, que puede ser encomendada a un área independiente, al sector de créditos con revisión independiente, o…"
  },
  {
   "id": "clasificacion_de_deudores",
   "type": "tarea_regulatoria",
   "label": "Clasificación de deudores",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Clasificación que debe efectuarse con una periodicidad que atienda a la importancia del deudor, considerando la totalidad de las financiaciones comprendidas, de…"
  },
  {
   "id": "categoria_de_clasificacion",
   "type": "nivel_de_riesgo",
   "label": "Categoría de clasificación",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Una de las cinco categorías en que se clasifica a cada cliente y la totalidad de sus financiaciones comprendidas."
  },
  {
   "id": "resto_de_deudas_del_deudor",
   "type": "elemento_de_evaluacion",
   "label": "Resto de deudas del deudor",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Otras obligaciones del deudor refinanciado que deben reunir como mínimo las condiciones del nivel inmediato superior para permitir reclasificación."
  }
 ]
}
```

--- paso 11 · buscar_nodos · input={"consulta": "régimen simplificado pequeños deudores", "limite": 10} · runtime=2907 · re-ejecutado=2907 ---

```json
{
 "consulta": "régimen simplificado pequeños deudores",
 "total_con_match": 50,
 "resultados": [
  {
   "id": "regimen_de_rancho",
   "type": "regimen_aduanero_exceptuado",
   "label": "Régimen de rancho",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Régimen aduanero exceptuado del seguimiento conforme a los artículos 506 al 516 de la Ley 22.415, aplicable a medios de transporte de bandera nacional."
  },
  {
   "id": "metodo_simplificado",
   "type": "metodologia_de_calculo",
   "label": "Método simplificado",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Método para calcular exigencias de capital en opciones aplicable cuando la entidad solo compra opciones o sus posiciones vendidas están cubiertas por posiciones…"
  },
  {
   "id": "regimen_de_equipaje",
   "type": "regimen_aduanero_exceptuado",
   "label": "Régimen de equipaje",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Régimen aduanero exceptuado del seguimiento conforme a los artículos 488 al 505 de la Ley 22.415."
  },
  {
   "id": "regimen_de_muestras",
   "type": "regimen_aduanero_exceptuado",
   "label": "Régimen de muestras",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Régimen aduanero exceptuado del seguimiento conforme a los artículos 560 al 565 de la Ley 22.415."
  },
  {
   "id": "regimen_de_removido",
   "type": "regimen_aduanero_exceptuado",
   "label": "Régimen de removido",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Régimen aduanero exceptuado del seguimiento conforme a los artículos 386 al 396 de la Ley 22.415."
  },
  {
   "id": "enfoque_simplificado",
   "type": "metodologia_de_calculo",
   "label": "Enfoque simplificado",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Enfoque simplificado para calcular exigencia de capital por riesgo de precio de opciones, previsto en punto 6.6.2."
  },
  {
   "id": "regimen_de_pacotilla",
   "type": "regimen_aduanero_exceptuado",
   "label": "Régimen de pacotilla",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Régimen aduanero exceptuado del seguimiento conforme a los artículos 517 al 528 de la Ley 22.415."
  },
  {
   "id": "regimen_exporta_simple",
   "type": "regimen_regulatorio",
   "label": "Régimen EXPORTA SIMPLE",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Régimen especial para exportaciones con plazo de 365 días corridos para ingreso y liquidación de divisas, independientemente del tipo de bien exportado."
  },
  {
   "id": "regimen_de_transparencia",
   "type": "herramienta_regulatoria",
   "label": "Régimen de Transparencia",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Régimen elaborado por el BCRA sobre la base de información proporcionada por sujetos obligados para que los usuarios comparen costos, características y requisit…"
  },
  {
   "id": "clasificacion_de_deudores",
   "type": "tarea_regulatoria",
   "label": "Clasificación de deudores",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Clasificación que debe efectuarse con una periodicidad que atienda a la importancia del deudor, considerando la totalidad de las financiaciones comprendidas, de…"
  }
 ]
}
```

--- paso 12 · buscar_nodos · input={"consulta": "45 días comunicación deudor saldo", "limite": 10} · runtime=2941 · re-ejecutado=2941 ---

```json
{
 "consulta": "45 días comunicación deudor saldo",
 "total_con_match": 52,
 "resultados": [
  {
   "id": "periodo_de_45_dias",
   "type": "plazo_regulatorio",
   "label": "Período de 45 días",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Plazo máximo previo a la transferencia de activos dentro del cual el originante o fiduciario debe analizar las condiciones de cumplimiento."
  },
  {
   "id": "seguro_de_vida_sobre_saldo_deudor",
   "type": "producto_financiero",
   "label": "Seguro de vida sobre saldo deudor",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Seguro que puede contratarse para tomar cobertura por riesgo de muerte del deudor, cuya contratación es decisión del sujeto obligado."
  },
  {
   "id": "operaciones_dvp_fallidas_entre_31_y_45_dias",
   "type": "categoria_de_exposicion",
   "label": "Operaciones DvP fallidas entre 31 y 45 días",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Operaciones con entrega contra pago fallidas con código 1330000 y cargo de capital del 75% cuando el pago no se realiza dentro de 31 a 45 días hábiles."
  },
  {
   "id": "saldo_deudor_de_otros_resultados_integrales",
   "type": "componente_de_capital_regulatorio",
   "label": "Saldo deudor de otros resultados integrales",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Saldo deudor proveniente del resto de los conceptos componentes de los otros resultados integrales no contemplados en revaluaciones."
  },
  {
   "id": "deudor",
   "type": "sujeto_regulado",
   "label": "Deudor",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Persona física o jurídica que mantiene financiaciones con la entidad y debe ser objeto de análisis de situación económica y financiera, así como de clasificació…"
  },
  {
   "id": "saldo_bruto",
   "type": "medida_de_exposicion",
   "label": "Saldo bruto",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Monto bruto de exposiciones minoristas sin computar coberturas del riesgo de crédito."
  },
  {
   "id": "deudor_moroso",
   "type": "causal_de_demora",
   "label": "Deudor moroso",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Situación en que el importador u otro obligado al pago incumple sus obligaciones, justificando acciones judiciales por parte del exportador."
  },
  {
   "id": "saldo_de_deuda",
   "type": "componente_de_exposicion",
   "label": "Saldo de deuda",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Importe adeudado por la contraparte, incluido en el cálculo de exposición."
  },
  {
   "id": "plazo_de_90_dias",
   "type": "restriccion_temporal",
   "label": "Plazo de 90 días",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Período mínimo que debe transcurrir desde la adquisición de títulos valores en suscripción primaria antes de poder venderlos en mercado secundario con liquidaci…"
  },
  {
   "id": "deudor_en_concurso",
   "type": "categoria_de_deudor",
   "label": "Deudor en concurso",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Deudor en concurso o con acuerdo preventivo extrajudicial solicitado o en gestión judicial de cobro que, por un período de hasta 540 días, no haya presentado do…"
  }
 ]
}
```

--- paso 13 · ver_nodo · input={"id": "periodo_de_45_dias"} · runtime=512 · re-ejecutado=512 ---

```json
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
```

--- paso 14 · ver_vecinos · input={"id": "periodo_de_45_dias", "direccion": "ambas"} · runtime=605 · re-ejecutado=605 ---

```json
{
 "id": "periodo_de_45_dias",
 "label": "Período de 45 días",
 "n_salientes_total": 0,
 "n_entrantes_total": 2,
 "salientes": [],
 "salientes_truncado": false,
 "entrantes": [
  {
   "relation": "debe_analizar_dentro_de",
   "vecino_id": "originante",
   "vecino_label": "Originante",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "p.49-51 / Sección iii)"
    }
   ]
  },
  {
   "relation": "debe_analizar_dentro_de",
   "vecino_id": "fiduciario",
   "vecino_label": "Fiduciario",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "p.49-51 / Sección iii)"
    }
   ]
  }
 ],
 "entrantes_truncado": false
}
```

--- paso 15 · buscar_nodos · input={"consulta": "pequeño deudor régimen", "limite": 10} · runtime=2785 · re-ejecutado=2785 ---

```json
{
 "consulta": "pequeño deudor régimen",
 "total_con_match": 58,
 "resultados": [
  {
   "id": "deudor",
   "type": "sujeto_regulado",
   "label": "Deudor",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Persona física o jurídica que mantiene financiaciones con la entidad y debe ser objeto de análisis de situación económica y financiera, así como de clasificació…"
  },
  {
   "id": "deudor_moroso",
   "type": "causal_de_demora",
   "label": "Deudor moroso",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Situación en que el importador u otro obligado al pago incumple sus obligaciones, justificando acciones judiciales por parte del exportador."
  },
  {
   "id": "regimen_de_rancho",
   "type": "regimen_aduanero_exceptuado",
   "label": "Régimen de rancho",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Régimen aduanero exceptuado del seguimiento conforme a los artículos 506 al 516 de la Ley 22.415, aplicable a medios de transporte de bandera nacional."
  },
  {
   "id": "deudor_en_concurso",
   "type": "categoria_de_deudor",
   "label": "Deudor en concurso",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Deudor en concurso o con acuerdo preventivo extrajudicial solicitado o en gestión judicial de cobro que, por un período de hasta 540 días, no haya presentado do…"
  },
  {
   "id": "regimen_de_equipaje",
   "type": "regimen_aduanero_exceptuado",
   "label": "Régimen de equipaje",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Régimen aduanero exceptuado del seguimiento conforme a los artículos 488 al 505 de la Ley 22.415."
  },
  {
   "id": "regimen_de_muestras",
   "type": "regimen_aduanero_exceptuado",
   "label": "Régimen de muestras",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Régimen aduanero exceptuado del seguimiento conforme a los artículos 560 al 565 de la Ley 22.415."
  },
  {
   "id": "regimen_de_removido",
   "type": "regimen_aduanero_exceptuado",
   "label": "Régimen de removido",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Régimen aduanero exceptuado del seguimiento conforme a los artículos 386 al 396 de la Ley 22.415."
  },
  {
   "id": "credito_unico_deudor",
   "type": "subclase_de_derivado_de_credito",
   "label": "Crédito único deudor",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Derivado de crédito referenciado a un único deudor, con factores regulatorios que varían según calificación crediticia (AAA a CCC)."
  },
  {
   "id": "deudor_no_calificado",
   "type": "categoria_de_contraparte",
   "label": "Deudor no calificado",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Contraparte sin calificación de crédito otorgada por ECAI, que recibe ponderador de riesgo no menor al del país de constitución."
  },
  {
   "id": "direccion_del_deudor",
   "type": "componente_organizacional",
   "label": "Dirección del deudor",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Gestión y liderazgo del deudor, evaluados por su capacidad, experiencia y honestidad."
  }
 ]
}
```

--- paso 16 · buscar_nodos · input={"consulta": "comunicación cambio clasificación 45 días optativo", "limite": 10} · runtime=2898 · re-ejecutado=2898 ---

```json
{
 "consulta": "comunicación cambio clasificación 45 días optativo",
 "total_con_match": 70,
 "resultados": [
  {
   "id": "periodo_de_45_dias",
   "type": "plazo_regulatorio",
   "label": "Período de 45 días",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Plazo máximo previo a la transferencia de activos dentro del cual el originante o fiduciario debe analizar las condiciones de cumplimiento."
  },
  {
   "id": "cambio_negativo_en_clasificacion",
   "type": "evento_regulatorio",
   "label": "Cambio negativo en clasificación",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Reclasificación desfavorable del deudor que debe ser comunicada al deudor dentro de 45 días mediante medios especificados, con excepciones según el saldo de deu…"
  },
  {
   "id": "operaciones_dvp_fallidas_entre_31_y_45_dias",
   "type": "categoria_de_exposicion",
   "label": "Operaciones DvP fallidas entre 31 y 45 días",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Operaciones con entrega contra pago fallidas con código 1330000 y cargo de capital del 75% cuando el pago no se realiza dentro de 31 a 45 días hábiles."
  },
  {
   "id": "casa_de_cambio",
   "type": "sujeto_regulado",
   "label": "Casa de cambio",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Entidad cambiaria que opera en el mercado de cambios, sujeta a requisitos operativos mínimos de tecnología y sistemas de información."
  },
  {
   "id": "tipo_de_cambio",
   "type": "clase_de_activo",
   "label": "Tipo de cambio",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Clase de activo subyacente en derivados, con factor regulatorio de 4%, correlación N/A y volatilidad de opción de 15%."
  },
  {
   "id": "venta_de_cambio",
   "type": "operacion_regulada",
   "label": "Venta de cambio",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Operación de cambio para transferencias a personas humanas en el exterior."
  },
  {
   "id": "boleto_de_cambio",
   "type": "documento_regulado",
   "label": "Boleto de cambio",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Documento que debe constar el carácter de declaración jurada del ordenante sobre todos los datos contenidos, incluyendo el concepto de la operación y cumplimien…"
  },
  {
   "id": "compra_de_cambio",
   "type": "operacion_regulada",
   "label": "Compra de cambio",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Operación de cambio para transferencias a personas humanas residentes en el país."
  },
  {
   "id": "plazo_de_90_dias",
   "type": "restriccion_temporal",
   "label": "Plazo de 90 días",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Período mínimo que debe transcurrir desde la adquisición de títulos valores en suscripción primaria antes de poder venderlos en mercado secundario con liquidaci…"
  },
  {
   "id": "riesgo_de_cambio",
   "type": "tipo_de_riesgo",
   "label": "Riesgo de cambio",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Riesgo calculado conforme al punto 6.4.3 de las normas sobre Capitales mínimos, utilizando códigos de partida específicos y un factor de ponderación del 0.08."
  }
 ]
}
```

---

# Sección 3 — run_4/CQ-028

## 3a. Respuesta final del agente (verbatim, `posthoc_run/traces/off/run_4/CQ-028.json`)

`trace.final_json`:

```json
{
 "respuesta": "Sí, un sujeto obligado puede cobrar comisión por precancelación total de una financiación, pero con una restricción importante: no se admite comisión por precancelación total cuando haya transcurrido al menos la cuarta parte del plazo original o 180 días, lo que ocurra primero. En cambio, la comisión por precancelación parcial sí se permite sin esta restricción temporal.",
 "citas": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.12-14 / Punto 2.3.2.1, párrafo segundo"
  }
 ],
 "respondible": true
}
```

`trace.final_raw` (turno final íntegro):

```
```json
{
  "respuesta": "Sí, un sujeto obligado puede cobrar comisión por precancelación total de una financiación, pero con una restricción importante: no se admite comisión por precancelación total cuando haya transcurrido al menos la cuarta parte del plazo original o 180 días, lo que ocurra primero. En cambio, la comisión por precancelación parcial sí se permite sin esta restricción temporal.",
  "citas": [
    {
      "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
      "location": "p.12-14 / Punto 2.3.2.1, párrafo segundo"
    }
  ],
  "respondible": true
}
```
```

## 3b. Inventario de pasos (runtime vs. almacenado vs. re-ejecutado)

| paso | tool | input | chars runtime | chars almacenados | re-ejecutado |
|---|---|---|---|---|---|
| 1 | buscar_nodos | `{"consulta": "precancelación comisión financiación", "limite": 10}` | 3092 | 1215 | = runtime ✓ |
| 2 | buscar_nodos | `{"consulta": "precancelación total sujeto obligado", "limite": 10}` | 3002 | 1215 | = runtime ✓ |
| 3 | ver_nodo | `{"id": "comision_por_precancelacion"}` | 639 | 639 | = runtime ✓ |
| 4 | ver_vecinos | `{"id": "comision_por_precancelacion", "direccion": "ambas"}` | 723 | 723 | = runtime ✓ |
| 5 | buscar_nodos | `{"consulta": "precancelación total restricción cuarta parte plazo", "limite": 10}` | 3044 | 1215 | = runtime ✓ |
| 6 | buscar_nodos | `{"consulta": "comisión precancelación no se admite prohibida", "limite": 10}` | 3026 | 1215 | = runtime ✓ |
| 7 | buscar_nodos | `{"consulta": "precancelación sin comisión crédito hipotecario consumo", "limite": 10}` | 3010 | 1215 | = runtime ✓ |
| 8 | buscar_nodos | `{"consulta": "operación de crédito hipotecario precancelación", "limite": 10}` | 2849 | 1215 | = runtime ✓ |
| 9 | buscar_nodos | `{"consulta": "crédito hipotecario vivienda comisión", "limite": 10}` | 2911 | 1215 | = runtime ✓ |
| 10 | ver_nodo | `{"id": "prestamo_hipotecario_en_pesos_para_compra_de_vivienda"}` | 679 | 679 | = runtime ✓ |
| 11 | buscar_nodos | `{"consulta": "operación de crédito no se admite comisión precancelación", "limite": 10}` | 3400 | 1215 | = runtime ✓ |
| 12 | buscar_nodos | `{"consulta": "operación de crédito no se admite", "limite": 10}` | 3366 | 1215 | = runtime ✓ |
| 13 | buscar_nodos | `{"consulta": "operación crédito no se admite comisión", "limite": 10}` | 3274 | 1215 | = runtime ✓ |
| 14 | buscar_nodos | `{"consulta": "operación de crédito donde no se admite comisión", "limite": 10}` | 3381 | 1215 | = runtime ✓ |
| 15 | buscar_nodos | `{"consulta": "operación de crédito donde no se admite", "limite": 10}` | 3372 | 1215 | = runtime ✓ |

**Fidelidad runtime↔re-ejecución: 15/15 pasos con largo idéntico.**

## 3c. APÉNDICE — outputs completos re-ejecutados (15 pasos)


--- paso 1 · buscar_nodos · input={"consulta": "precancelación comisión financiación", "limite": 10} · runtime=3092 · re-ejecutado=3092 ---

```json
{
 "consulta": "precancelación comisión financiación",
 "total_con_match": 60,
 "resultados": [
  {
   "id": "comision_por_precancelacion",
   "type": "comision_permitida",
   "label": "Comisión por precancelación",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Comisión que puede aplicarse por precancelación total o parcial de financiaciones, con restricción en precancelación total cuando haya transcurrido al menos la …"
  },
  {
   "id": "comision",
   "type": "tipo_de_costo",
   "label": "Comisión",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Retribución que obedece a servicios prestados por los sujetos obligados y puede incluir retribuciones que excedan el costo de la prestación."
  },
  {
   "id": "financiacion",
   "type": "producto_crediticio",
   "label": "Financiación",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Créditos, préstamos y otras operaciones de intermediación financiera otorgadas por la entidad a sus clientes, sujetas a clasificación de riesgo."
  },
  {
   "id": "cuota_de_financiacion",
   "type": "componente_de_obligacion_crediticia",
   "label": "Cuota de financiación",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Pago periódico de una financiación con amortización periódica, incluyendo cuotas por compras financiadas en tarjeta de crédito."
  },
  {
   "id": "precancelacion_de_deudas",
   "type": "operacion_de_pago_anticipado",
   "label": "Precancelación de deudas",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Cancelación de obligaciones en moneda extranjera con anterioridad al vencimiento, que requiere conformidad previa del BCRA excepto en situaciones específicas."
  },
  {
   "id": "operacion_de_financiacion",
   "type": "operacion_financiera",
   "label": "Operación de financiación",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Operación de crédito cuya información debe incluirse en el resumen informativo del contrato conforme a lo dispuesto en el punto 3.2. del TO sobre Tasas de Inter…"
  },
  {
   "id": "financiacion_de_exportacion",
   "type": "instrumento_financiero",
   "label": "Financiación de exportación",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Financiamiento para operaciones de exportación de bienes que admite la aplicación de divisas de cobros de exportaciones."
  },
  {
   "id": "solicitudes_de_financiacion",
   "type": "tramite_regulado",
   "label": "Solicitudes de financiación",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Solicitudes de financiación que no pueden ser rechazadas por el solo dato de la edad del solicitante cuando su nivel de ingresos proyectados sea suficiente."
  },
  {
   "id": "comision_nacional_de_valores",
   "type": "organismo_regulador",
   "label": "Comisión Nacional de Valores",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Autoridad que regula la emisión de pagarés con oferta pública y valores de deuda fiduciaria mediante disposiciones específicas."
  },
  {
   "id": "financiacion_de_exportaciones",
   "type": "operacion_financiera",
   "label": "Financiación de exportaciones",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Anticipos o prefinanciaciones de exportaciones del exterior o prefinanciaciones de exportaciones otorgadas por entidades financieras locales con fondeo en línea…"
  }
 ]
}
```

--- paso 2 · buscar_nodos · input={"consulta": "precancelación total sujeto obligado", "limite": 10} · runtime=3002 · re-ejecutado=3002 ---

```json
{
 "consulta": "precancelación total sujeto obligado",
 "total_con_match": 32,
 "resultados": [
  {
   "id": "sujeto_obligado",
   "type": "entidad_regulada",
   "label": "Sujeto obligado",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Entidad financiera, empresa no financiera emisora de tarjetas de crédito u otro proveedor no financiero de crédito sujeto a las obligaciones de protección de us…"
  },
  {
   "id": "reclamo_ante_sujeto_obligado",
   "type": "procedimiento_regulatorio",
   "label": "Reclamo ante sujeto obligado",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Presentación formal de un reclamo por cobro indebido que inicia el plazo de 10 días hábiles para reintegro."
  },
  {
   "id": "derecho_de_precancelacion_total_o_parcial",
   "type": "contenido_contractual_obligatorio",
   "label": "Derecho de precancelación total o parcial",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Derecho del usuario a efectuar en cualquier momento del plazo del crédito la precancelación total o precancelaciones parciales."
  },
  {
   "id": "ejemplar_del_contrato_suscripto_por_el_sujeto_obligado",
   "type": "requisito_contractual",
   "label": "Ejemplar del contrato suscripto por el sujeto obligado",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Ejemplar del contrato que debe ser entregado al usuario debidamente suscripto por el sujeto obligado en el acto de contratación."
  },
  {
   "id": "razon_social_cuit_y_domicilio_legal_del_sujeto_obligado",
   "type": "contenido_contractual_obligatorio",
   "label": "Razón social, CUIT y domicilio legal del sujeto obligado",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Elemento mínimo que debe contener todo contrato financiero."
  },
  {
   "id": "cobertura_total",
   "type": "tipo_de_proteccion_crediticia",
   "label": "Cobertura total",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Protección crediticia que cubre la totalidad de una posición de titulización, conforme a lo previsto en el punto 5.4.2."
  },
  {
   "id": "valor_fob_total",
   "type": "parametro_de_calculo",
   "label": "Valor FOB total",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Valor total de la operación de importación expresado en términos FOB, utilizado para determinar si bienes de capital representan al menos el 90% del total."
  },
  {
   "id": "obligado_al_pago",
   "type": "sujeto_regulado",
   "label": "Obligado al pago",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Deudor cuya situación crediticia debe cumplir con condiciones específicas para que su obligación sea incluida en la titulización."
  },
  {
   "id": "total_integracion",
   "type": "concepto_de_informacion_regulatoria",
   "label": "Total integración",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Integración total de capital mínimo del mes bajo informe."
  },
  {
   "id": "posicion_neta_total",
   "type": "medida_agregada_de_exposicion_en_moneda_extranjera",
   "label": "Posición neta total",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Suma del mayor entre los valores absolutos de posiciones netas vendidas y compradas, más el valor absoluto de la posición neta en oro, utilizada para calcular l…"
  }
 ]
}
```

--- paso 3 · ver_nodo · input={"id": "comision_por_precancelacion"} · runtime=639 · re-ejecutado=639 ---

```json
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
```

--- paso 4 · ver_vecinos · input={"id": "comision_por_precancelacion", "direccion": "ambas"} · runtime=723 · re-ejecutado=723 ---

```json
{
 "id": "comision_por_precancelacion",
 "label": "Comisión por precancelación",
 "n_salientes_total": 0,
 "n_entrantes_total": 2,
 "salientes": [],
 "salientes_truncado": false,
 "entrantes": [
  {
   "relation": "puede_aplicar",
   "vecino_id": "sujeto_obligado",
   "vecino_label": "Sujeto obligado",
   "provenances": [
    {
     "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
     "location": "p.12-14 / Punto 2.3.2.1, párrafo segundo"
    }
   ]
  },
  {
   "relation": "incluye",
   "vecino_id": "costo_financiero_total_cft",
   "vecino_label": "Costo financiero total (CFT)",
   "provenances": [
    {
     "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
     "location": "p.12-14 / Punto 2.3.3, párrafo tercero"
    }
   ]
  }
 ],
 "entrantes_truncado": false
}
```

--- paso 5 · buscar_nodos · input={"consulta": "precancelación total restricción cuarta parte plazo", "limite": 10} · runtime=3044 · re-ejecutado=3044 ---

```json
{
 "consulta": "precancelación total restricción cuarta parte plazo",
 "total_con_match": 91,
 "resultados": [
  {
   "id": "derecho_de_precancelacion_total_o_parcial",
   "type": "contenido_contractual_obligatorio",
   "label": "Derecho de precancelación total o parcial",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Derecho del usuario a efectuar en cualquier momento del plazo del crédito la precancelación total o precancelaciones parciales."
  },
  {
   "id": "cobertura_total",
   "type": "tipo_de_proteccion_crediticia",
   "label": "Cobertura total",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Protección crediticia que cubre la totalidad de una posición de titulización, conforme a lo previsto en el punto 5.4.2."
  },
  {
   "id": "valor_fob_total",
   "type": "parametro_de_calculo",
   "label": "Valor FOB total",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Valor total de la operación de importación expresado en términos FOB, utilizado para determinar si bienes de capital representan al menos el 90% del total."
  },
  {
   "id": "plazo_de_90_dias",
   "type": "restriccion_temporal",
   "label": "Plazo de 90 días",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Período mínimo que debe transcurrir desde la adquisición de títulos valores en suscripción primaria antes de poder venderlos en mercado secundario con liquidaci…"
  },
  {
   "id": "prorroga_de_plazo",
   "type": "mecanismo_de_regularizacion",
   "label": "Prórroga de plazo",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Extensión del plazo para la demostración del registro de ingreso aduanero, concedida por la entidad a cargo del seguimiento o con conformidad del BCRA."
  },
  {
   "id": "total_integracion",
   "type": "concepto_de_informacion_regulatoria",
   "label": "Total integración",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Integración total de capital mínimo del mes bajo informe."
  },
  {
   "id": "estructura_a_plazo",
   "type": "tipo_de_titulizacion",
   "label": "Estructura a plazo",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Operación con exposiciones rotativas que contiene cláusulas de amortización anticipada que replican estructuras a plazo, donde el riesgo de las facilidades suby…"
  },
  {
   "id": "ampliacion_de_plazo",
   "type": "procedimiento_administrativo",
   "label": "Ampliación de plazo",
   "tokens_matcheados": 1,
   "resumen_propiedades": "El exportador puede solicitar a la entidad encargada del seguimiento que el plazo para liquidación de divisas sea ampliado hasta la fecha en que se estima se ef…"
  },
  {
   "id": "posicion_neta_total",
   "type": "medida_agregada_de_exposicion_en_moneda_extranjera",
   "label": "Posición neta total",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Suma del mayor entre los valores absolutos de posiciones netas vendidas y compradas, más el valor absoluto de la posición neta en oro, utilizada para calcular l…"
  },
  {
   "id": "reduccion_del_plazo",
   "type": "modificacion_regulatoria_de_plazo",
   "label": "Reducción del plazo",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Acortamiento del plazo de liquidación que rige únicamente para operaciones que se oficialicen a partir de su vigencia."
  }
 ]
}
```

--- paso 6 · buscar_nodos · input={"consulta": "comisión precancelación no se admite prohibida", "limite": 10} · runtime=3026 · re-ejecutado=3026 ---

```json
{
 "consulta": "comisión precancelación no se admite prohibida",
 "total_con_match": 159,
 "resultados": [
  {
   "id": "comision_por_precancelacion",
   "type": "comision_permitida",
   "label": "Comisión por precancelación",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Comisión que puede aplicarse por precancelación total o parcial de financiaciones, con restricción en precancelación total cuando haya transcurrido al menos la …"
  },
  {
   "id": "comision_sobre_importes_no_utilizados",
   "type": "comision_permitida",
   "label": "Comisión sobre importes no utilizados",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Comisión que los sujetos obligados pueden aplicar sobre los importes no utilizados de acuerdos de asignación de fondos, dado que su puesta a disposición configu…"
  },
  {
   "id": "derivados_que_no_se_liquidan_en_forma_centralizada",
   "type": "categoria_de_derivado",
   "label": "Derivados que no se liquidan en forma centralizada",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Operaciones de derivados sujetas a acuerdos de márgenes diarios con período de riesgo de margen mínimo de 10 días hábiles."
  },
  {
   "id": "comision",
   "type": "tipo_de_costo",
   "label": "Comisión",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Retribución que obedece a servicios prestados por los sujetos obligados y puede incluir retribuciones que excedan el costo de la prestación."
  },
  {
   "id": "no_residente",
   "type": "sujeto",
   "label": "No residente",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Persona o entidad que no reside en Argentina y puede ser contraparte de contratos de obras o provisión de bienes y servicios."
  },
  {
   "id": "operacion_no_dvp",
   "type": "tipo_de_operacion_financiera",
   "label": "Operación no DvP",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Operación en la que se entrega efectivo sin recibir la correspondiente contrapartida o se entregan efectos sin el correspondiente pago de efectivo, exponiendo a…"
  },
  {
   "id": "ccp_que_no_califica",
   "type": "entidad_de_contraparte_central",
   "label": "CCP que no califica",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Entidad de contraparte central que no cumple con los criterios de calificación y se trata como entidad financiera."
  },
  {
   "id": "cobros_no_aplicados",
   "type": "concepto_de_imputacion",
   "label": "Cobros no aplicados",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Pagos recibidos que no han sido imputados a la cancelación de la deuda y que reducen el importe sujeto a refinanciación."
  },
  {
   "id": "cliente_no_residente",
   "type": "sujeto_regulado",
   "label": "Cliente no residente",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Cliente que no es persona humana residente y debe cumplir con requisitos adicionales de declaración jurada respecto a operaciones con títulos valores y otros ac…"
  },
  {
   "id": "deudor_no_calificado",
   "type": "categoria_de_contraparte",
   "label": "Deudor no calificado",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Contraparte sin calificación de crédito otorgada por ECAI, que recibe ponderador de riesgo no menor al del país de constitución."
  }
 ]
}
```

--- paso 7 · buscar_nodos · input={"consulta": "precancelación sin comisión crédito hipotecario consumo", "limite": 10} · runtime=3010 · re-ejecutado=3010 ---

```json
{
 "consulta": "precancelación sin comisión crédito hipotecario consumo",
 "total_con_match": 168,
 "resultados": [
  {
   "id": "comision_por_precancelacion",
   "type": "comision_permitida",
   "label": "Comisión por precancelación",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Comisión que puede aplicarse por precancelación total o parcial de financiaciones, con restricción en precancelación total cuando haya transcurrido al menos la …"
  },
  {
   "id": "credito_cedido_sin_responsabilidad",
   "type": "tipo_de_financiacion",
   "label": "Crédito cedido sin responsabilidad",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Créditos cedidos a favor de la entidad sin responsabilidad para el cedente, que se imputan al firmante, librador, deudor o aceptante del instrumento."
  },
  {
   "id": "precancelacion_de_linea_de_credito",
   "type": "operacion_cambiaria",
   "label": "Precancelación de línea de crédito",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Cancelación anticipada de una línea de crédito del exterior antes de su vencimiento."
  },
  {
   "id": "exigencia_por_riesgo_de_credito_sin_incluir_el_termino_inc",
   "type": "concepto_de_exigencia_de_capital",
   "label": "Exigencia por riesgo de crédito sin incluir el término INC",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Exigencia de capital mínimo calculada según riesgo de crédito, excluyendo el término INC, determinada mediante fórmula específica que incluye códigos de partida…"
  },
  {
   "id": "credito",
   "type": "clase_de_activo",
   "label": "Crédito",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Clase de activo a la que se asignan derivados cuyo factor de riesgo principal es el riesgo de crédito."
  },
  {
   "id": "comision",
   "type": "tipo_de_costo",
   "label": "Comisión",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Retribución que obedece a servicios prestados por los sujetos obligados y puede incluir retribuciones que excedan el costo de la prestación."
  },
  {
   "id": "credito_cedido",
   "type": "operacion_crediticia",
   "label": "Crédito cedido",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Crédito cedido a favor de la entidad sin responsabilidad para el cedente, respecto del cual debe abrirse legajo del firmante, librador, deudor, codeudor o acept…"
  },
  {
   "id": "credito_senior",
   "type": "categoria_de_exposicion",
   "label": "Crédito senior",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Exposición crediticia que es igual o preferente respecto de un crédito evaluado, permitiendo uso de calificación de ese crédito evaluado."
  },
  {
   "id": "credito_diverso",
   "type": "tipo_de_financiacion",
   "label": "Crédito diverso",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Créditos vinculados a la venta de activos inmovilizados, inclusive los tomados en defensa o en pago de créditos, sin deducir previsiones por riesgo de incobrabi…"
  },
  {
   "id": "nota_de_credito",
   "type": "circunstancia_modificatoria",
   "label": "Nota de crédito",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Circunstancia que modifica las obligaciones con el exterior del importador y debe ser reportada al BCRA."
  }
 ]
}
```

--- paso 8 · buscar_nodos · input={"consulta": "operación de crédito hipotecario precancelación", "limite": 10} · runtime=2849 · re-ejecutado=2849 ---

```json
{
 "consulta": "operación de crédito hipotecario precancelación",
 "total_con_match": 1787,
 "resultados": [
  {
   "id": "precancelacion_de_linea_de_credito",
   "type": "operacion_cambiaria",
   "label": "Precancelación de línea de crédito",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Cancelación anticipada de una línea de crédito del exterior antes de su vencimiento."
  },
  {
   "id": "nota_de_credito",
   "type": "circunstancia_modificatoria",
   "label": "Nota de crédito",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Circunstancia que modifica las obligaciones con el exterior del importador y debe ser reportada al BCRA."
  },
  {
   "id": "carta_de_credito",
   "type": "instrumento_financiero",
   "label": "Carta de crédito",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Instrumento de garantía comercial emitido u otorgado para operaciones de importación de bienes, sujeto a requisitos de documentación y registro aduanero."
  },
  {
   "id": "linea_de_credito",
   "type": "estructura_de_credito",
   "label": "Línea de crédito",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Límite de crédito dentro del cual los prestatarios pueden realizar giros y cancelaciones en financiaciones rotativas."
  },
  {
   "id": "cartas_de_credito",
   "type": "instrumento_financiero",
   "label": "Cartas de crédito",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Cartas de crédito emitidas u otorgadas por entidades financieras locales para garantizar operaciones de importaciones de bienes con registro aduanero."
  },
  {
   "id": "evento_de_credito",
   "type": "evento_regulatorio",
   "label": "Evento de crédito",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Hecho especificado en derivados de crédito que incluye falta de pago, apertura de concurso, insolvencia, quiebra o reestructuración con condonación o aplazamien…"
  },
  {
   "id": "indice_de_credito",
   "type": "instrumento_de_referencia",
   "label": "Índice de crédito",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Índice que puede ser grado de inversión o especulativo, utilizado como referencia en derivados de crédito. Se trata como si hiciera referencia a entidades deter…"
  },
  {
   "id": "operacion_de_pase",
   "type": "tipo_de_operacion",
   "label": "Operación de pase",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Operación de financiación con títulos valores garantizada con un activo, sujeta a requerimiento de capital cuando la entidad actúa en cualquier posición."
  },
  {
   "id": "riesgo_de_credito",
   "type": "tipo_de_riesgo",
   "label": "Riesgo de crédito",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Riesgo de incumplimiento de la contraparte en sus obligaciones financieras, sujeto a evaluación y ponderación."
  },
  {
   "id": "derecho_de_credito",
   "type": "tipo_de_activo_subyacente",
   "label": "Derecho de crédito",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Derecho de crédito de carácter homogéneo que constituye activo subyacente en una titulización."
  }
 ]
}
```

--- paso 9 · buscar_nodos · input={"consulta": "crédito hipotecario vivienda comisión", "limite": 10} · runtime=2911 · re-ejecutado=2911 ---

```json
{
 "consulta": "crédito hipotecario vivienda comisión",
 "total_con_match": 134,
 "resultados": [
  {
   "id": "prestamo_hipotecario_en_pesos_para_compra_de_vivienda",
   "type": "producto_financiero",
   "label": "Préstamo hipotecario en pesos para compra de vivienda",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Préstamo hipotecario que permite aplicar fondos al pago de inmuebles en moneda extranjera a través de operación de compraventa de títulos valores con liquidació…"
  },
  {
   "id": "credito",
   "type": "clase_de_activo",
   "label": "Crédito",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Clase de activo a la que se asignan derivados cuyo factor de riesgo principal es el riesgo de crédito."
  },
  {
   "id": "comision",
   "type": "tipo_de_costo",
   "label": "Comisión",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Retribución que obedece a servicios prestados por los sujetos obligados y puede incluir retribuciones que excedan el costo de la prestación."
  },
  {
   "id": "credito_cedido",
   "type": "operacion_crediticia",
   "label": "Crédito cedido",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Crédito cedido a favor de la entidad sin responsabilidad para el cedente, respecto del cual debe abrirse legajo del firmante, librador, deudor, codeudor o acept…"
  },
  {
   "id": "credito_senior",
   "type": "categoria_de_exposicion",
   "label": "Crédito senior",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Exposición crediticia que es igual o preferente respecto de un crédito evaluado, permitiendo uso de calificación de ese crédito evaluado."
  },
  {
   "id": "credito_diverso",
   "type": "tipo_de_financiacion",
   "label": "Crédito diverso",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Créditos vinculados a la venta de activos inmovilizados, inclusive los tomados en defensa o en pago de créditos, sin deducir previsiones por riesgo de incobrabi…"
  },
  {
   "id": "nota_de_credito",
   "type": "circunstancia_modificatoria",
   "label": "Nota de crédito",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Circunstancia que modifica las obligaciones con el exterior del importador y debe ser reportada al BCRA."
  },
  {
   "id": "carta_de_credito",
   "type": "instrumento_financiero",
   "label": "Carta de crédito",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Instrumento de garantía comercial emitido u otorgado para operaciones de importación de bienes, sujeto a requisitos de documentación y registro aduanero."
  },
  {
   "id": "linea_de_credito",
   "type": "estructura_de_credito",
   "label": "Línea de crédito",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Límite de crédito dentro del cual los prestatarios pueden realizar giros y cancelaciones en financiaciones rotativas."
  },
  {
   "id": "cartas_de_credito",
   "type": "instrumento_financiero",
   "label": "Cartas de crédito",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Cartas de crédito emitidas u otorgadas por entidades financieras locales para garantizar operaciones de importaciones de bienes con registro aduanero."
  }
 ]
}
```

--- paso 10 · ver_nodo · input={"id": "prestamo_hipotecario_en_pesos_para_compra_de_vivienda"} · runtime=679 · re-ejecutado=679 ---

```json
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
```

--- paso 11 · buscar_nodos · input={"consulta": "operación de crédito no se admite comisión precancelación", "limite": 10} · runtime=3400 · re-ejecutado=3400 ---

```json
{
 "consulta": "operación de crédito no se admite comisión precancelación",
 "total_con_match": 1865,
 "resultados": [
  {
   "id": "margenes_de_credito_no_percibidos",
   "type": "factor_de_ajuste_de_valuacion",
   "label": "Márgenes de crédito no percibidos",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Factor que debe evaluarse para ajuste de valuación en procedimientos a mercado o a modelo."
  },
  {
   "id": "precancelacion_de_linea_de_credito",
   "type": "operacion_cambiaria",
   "label": "Precancelación de línea de crédito",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Cancelación anticipada de una línea de crédito del exterior antes de su vencimiento."
  },
  {
   "id": "proveedor_no_financiero_de_credito",
   "type": "sujeto_regulado",
   "label": "Proveedor no financiero de crédito",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Empresa no financiera que otorga crédito y está alcanzada por normas sobre clasificación de deudores, debiendo aplicar criterios de cartera de consumo o viviend…"
  },
  {
   "id": "otro_proveedor_no_financiero_de_credito",
   "type": "agente_regulado",
   "label": "Otro proveedor no financiero de crédito",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Proveedor no financiero de crédito sujeto a las obligaciones de protección de usuarios y publicidad de información."
  },
  {
   "id": "otros_proveedores_no_financieros_de_credito",
   "type": "entidad_regulada",
   "label": "Otros proveedores no financieros de crédito",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Proveedores no financieros que ofrecen crédito y deben cumplir con las disposiciones de protección de usuarios de servicios financieros."
  },
  {
   "id": "titulos_de_credito_no_custodiados_por_la_entidad",
   "type": "concepto_deducible_de_capital",
   "label": "Títulos de crédito no custodiados por la entidad",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Títulos valores, certificados de depósitos a plazo fijo y otros títulos de crédito que físicamente no se encuentren en poder de la entidad, deducibles del capit…"
  },
  {
   "id": "entidad_no_financiera_emisora_de_tarjetas_de_credito",
   "type": "sujeto_regulado",
   "label": "Entidad no financiera emisora de tarjetas de crédito",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Empresa no financiera que emite tarjetas de crédito en modalidad de sistema cerrado y debe clasificar deudores según normas del BCRA."
  },
  {
   "id": "empresa_no_financiera_emisora_de_tarjetas_de_credito_y_compra",
   "type": "sujeto_regulado",
   "label": "Empresa no financiera emisora de tarjetas de crédito y compra",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Proveedor no financiero de crédito que emite tarjetas de crédito y/o compra y debe clasificar deudores según criterios de cartera de consumo o vivienda."
  },
  {
   "id": "empresa_no_financiera_emisora_de_tarjetas_de_credito_y_o_compra",
   "type": "sujeto_obligado",
   "label": "Empresa no financiera emisora de tarjetas de crédito y/o compra",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Empresa no financiera que emite tarjetas de crédito o compra y está sujeta a estas normas de protección."
  },
  {
   "id": "empresas_no_financieras_emisoras_de_tarjetas_de_credito_y_o_compra",
   "type": "entidad_regulada",
   "label": "Empresas no financieras emisoras de tarjetas de crédito y/o compra",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Empresas que emiten tarjetas de crédito y/o compra y deben cumplir con las disposiciones de protección de usuarios de servicios financieros."
  }
 ]
}
```

--- paso 12 · buscar_nodos · input={"consulta": "operación de crédito no se admite", "limite": 10} · runtime=3366 · re-ejecutado=3366 ---

```json
{
 "consulta": "operación de crédito no se admite",
 "total_con_match": 1863,
 "resultados": [
  {
   "id": "margenes_de_credito_no_percibidos",
   "type": "factor_de_ajuste_de_valuacion",
   "label": "Márgenes de crédito no percibidos",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Factor que debe evaluarse para ajuste de valuación en procedimientos a mercado o a modelo."
  },
  {
   "id": "proveedor_no_financiero_de_credito",
   "type": "sujeto_regulado",
   "label": "Proveedor no financiero de crédito",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Empresa no financiera que otorga crédito y está alcanzada por normas sobre clasificación de deudores, debiendo aplicar criterios de cartera de consumo o viviend…"
  },
  {
   "id": "otro_proveedor_no_financiero_de_credito",
   "type": "agente_regulado",
   "label": "Otro proveedor no financiero de crédito",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Proveedor no financiero de crédito sujeto a las obligaciones de protección de usuarios y publicidad de información."
  },
  {
   "id": "otros_proveedores_no_financieros_de_credito",
   "type": "entidad_regulada",
   "label": "Otros proveedores no financieros de crédito",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Proveedores no financieros que ofrecen crédito y deben cumplir con las disposiciones de protección de usuarios de servicios financieros."
  },
  {
   "id": "titulos_de_credito_no_custodiados_por_la_entidad",
   "type": "concepto_deducible_de_capital",
   "label": "Títulos de crédito no custodiados por la entidad",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Títulos valores, certificados de depósitos a plazo fijo y otros títulos de crédito que físicamente no se encuentren en poder de la entidad, deducibles del capit…"
  },
  {
   "id": "entidad_no_financiera_emisora_de_tarjetas_de_credito",
   "type": "sujeto_regulado",
   "label": "Entidad no financiera emisora de tarjetas de crédito",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Empresa no financiera que emite tarjetas de crédito en modalidad de sistema cerrado y debe clasificar deudores según normas del BCRA."
  },
  {
   "id": "empresa_no_financiera_emisora_de_tarjetas_de_credito_y_compra",
   "type": "sujeto_regulado",
   "label": "Empresa no financiera emisora de tarjetas de crédito y compra",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Proveedor no financiero de crédito que emite tarjetas de crédito y/o compra y debe clasificar deudores según criterios de cartera de consumo o vivienda."
  },
  {
   "id": "empresa_no_financiera_emisora_de_tarjetas_de_credito_y_o_compra",
   "type": "sujeto_obligado",
   "label": "Empresa no financiera emisora de tarjetas de crédito y/o compra",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Empresa no financiera que emite tarjetas de crédito o compra y está sujeta a estas normas de protección."
  },
  {
   "id": "empresas_no_financieras_emisoras_de_tarjetas_de_credito_y_o_compra",
   "type": "entidad_regulada",
   "label": "Empresas no financieras emisoras de tarjetas de crédito y/o compra",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Empresas que emiten tarjetas de crédito y/o compra y deben cumplir con las disposiciones de protección de usuarios de servicios financieros."
  },
  {
   "id": "nota_de_credito",
   "type": "circunstancia_modificatoria",
   "label": "Nota de crédito",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Circunstancia que modifica las obligaciones con el exterior del importador y debe ser reportada al BCRA."
  }
 ]
}
```

--- paso 13 · buscar_nodos · input={"consulta": "operación crédito no se admite comisión", "limite": 10} · runtime=3274 · re-ejecutado=3274 ---

```json
{
 "consulta": "operación crédito no se admite comisión",
 "total_con_match": 308,
 "resultados": [
  {
   "id": "operacion_no_dvp",
   "type": "tipo_de_operacion_financiera",
   "label": "Operación no DvP",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Operación en la que se entrega efectivo sin recibir la correspondiente contrapartida o se entregan efectos sin el correspondiente pago de efectivo, exponiendo a…"
  },
  {
   "id": "credito_no_calificado",
   "type": "categoria_de_exposicion",
   "label": "Crédito no calificado",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Exposición crediticia sin calificación específica de ECAI, que recibe ponderador de riesgo correspondiente a créditos sin evaluación de alta calidad."
  },
  {
   "id": "margenes_de_credito_no_percibidos",
   "type": "factor_de_ajuste_de_valuacion",
   "label": "Márgenes de crédito no percibidos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Factor que debe evaluarse para ajuste de valuación en procedimientos a mercado o a modelo."
  },
  {
   "id": "proveedor_no_financiero_de_credito",
   "type": "sujeto_regulado",
   "label": "Proveedor no financiero de crédito",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Empresa no financiera que otorga crédito y está alcanzada por normas sobre clasificación de deudores, debiendo aplicar criterios de cartera de consumo o viviend…"
  },
  {
   "id": "credito_quirografario_no_subordinado",
   "type": "exposicion_crediticia",
   "label": "Crédito quirografario no subordinado",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Crédito sin garantía real que no tiene carácter subordinado, al cual puede aplicarse la calificación del prestatario como emisor."
  },
  {
   "id": "comision_sobre_importes_no_utilizados",
   "type": "comision_permitida",
   "label": "Comisión sobre importes no utilizados",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Comisión que los sujetos obligados pueden aplicar sobre los importes no utilizados de acuerdos de asignación de fondos, dado que su puesta a disposición configu…"
  },
  {
   "id": "otro_proveedor_no_financiero_de_credito",
   "type": "agente_regulado",
   "label": "Otro proveedor no financiero de crédito",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Proveedor no financiero de crédito sujeto a las obligaciones de protección de usuarios y publicidad de información."
  },
  {
   "id": "operacion_al_contado_a_liquidar_no_fallida",
   "type": "categoria_de_operacion",
   "label": "Operación al contado a liquidar no fallida",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Operación al contado a liquidar que no se encuentra en situación de incumplimiento. Se aplica ponderador de riesgo del 0%."
  },
  {
   "id": "otros_proveedores_no_financieros_de_credito",
   "type": "entidad_regulada",
   "label": "Otros proveedores no financieros de crédito",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Proveedores no financieros que ofrecen crédito y deben cumplir con las disposiciones de protección de usuarios de servicios financieros."
  },
  {
   "id": "titulos_de_credito_no_custodiados_por_la_entidad",
   "type": "concepto_deducible_de_capital",
   "label": "Títulos de crédito no custodiados por la entidad",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Títulos valores, certificados de depósitos a plazo fijo y otros títulos de crédito que físicamente no se encuentren en poder de la entidad, deducibles del capit…"
  }
 ]
}
```

--- paso 14 · buscar_nodos · input={"consulta": "operación de crédito donde no se admite comisión", "limite": 10} · runtime=3381 · re-ejecutado=3381 ---

```json
{
 "consulta": "operación de crédito donde no se admite comisión",
 "total_con_match": 1865,
 "resultados": [
  {
   "id": "margenes_de_credito_no_percibidos",
   "type": "factor_de_ajuste_de_valuacion",
   "label": "Márgenes de crédito no percibidos",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Factor que debe evaluarse para ajuste de valuación en procedimientos a mercado o a modelo."
  },
  {
   "id": "proveedor_no_financiero_de_credito",
   "type": "sujeto_regulado",
   "label": "Proveedor no financiero de crédito",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Empresa no financiera que otorga crédito y está alcanzada por normas sobre clasificación de deudores, debiendo aplicar criterios de cartera de consumo o viviend…"
  },
  {
   "id": "otro_proveedor_no_financiero_de_credito",
   "type": "agente_regulado",
   "label": "Otro proveedor no financiero de crédito",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Proveedor no financiero de crédito sujeto a las obligaciones de protección de usuarios y publicidad de información."
  },
  {
   "id": "otros_proveedores_no_financieros_de_credito",
   "type": "entidad_regulada",
   "label": "Otros proveedores no financieros de crédito",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Proveedores no financieros que ofrecen crédito y deben cumplir con las disposiciones de protección de usuarios de servicios financieros."
  },
  {
   "id": "titulos_de_credito_no_custodiados_por_la_entidad",
   "type": "concepto_deducible_de_capital",
   "label": "Títulos de crédito no custodiados por la entidad",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Títulos valores, certificados de depósitos a plazo fijo y otros títulos de crédito que físicamente no se encuentren en poder de la entidad, deducibles del capit…"
  },
  {
   "id": "entidad_no_financiera_emisora_de_tarjetas_de_credito",
   "type": "sujeto_regulado",
   "label": "Entidad no financiera emisora de tarjetas de crédito",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Empresa no financiera que emite tarjetas de crédito en modalidad de sistema cerrado y debe clasificar deudores según normas del BCRA."
  },
  {
   "id": "empresa_no_financiera_emisora_de_tarjetas_de_credito_y_compra",
   "type": "sujeto_regulado",
   "label": "Empresa no financiera emisora de tarjetas de crédito y compra",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Proveedor no financiero de crédito que emite tarjetas de crédito y/o compra y debe clasificar deudores según criterios de cartera de consumo o vivienda."
  },
  {
   "id": "empresa_no_financiera_emisora_de_tarjetas_de_credito_y_o_compra",
   "type": "sujeto_obligado",
   "label": "Empresa no financiera emisora de tarjetas de crédito y/o compra",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Empresa no financiera que emite tarjetas de crédito o compra y está sujeta a estas normas de protección."
  },
  {
   "id": "empresas_no_financieras_emisoras_de_tarjetas_de_credito_y_o_compra",
   "type": "entidad_regulada",
   "label": "Empresas no financieras emisoras de tarjetas de crédito y/o compra",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Empresas que emiten tarjetas de crédito y/o compra y deben cumplir con las disposiciones de protección de usuarios de servicios financieros."
  },
  {
   "id": "nota_de_credito",
   "type": "circunstancia_modificatoria",
   "label": "Nota de crédito",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Circunstancia que modifica las obligaciones con el exterior del importador y debe ser reportada al BCRA."
  }
 ]
}
```

--- paso 15 · buscar_nodos · input={"consulta": "operación de crédito donde no se admite", "limite": 10} · runtime=3372 · re-ejecutado=3372 ---

```json
{
 "consulta": "operación de crédito donde no se admite",
 "total_con_match": 1863,
 "resultados": [
  {
   "id": "margenes_de_credito_no_percibidos",
   "type": "factor_de_ajuste_de_valuacion",
   "label": "Márgenes de crédito no percibidos",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Factor que debe evaluarse para ajuste de valuación en procedimientos a mercado o a modelo."
  },
  {
   "id": "proveedor_no_financiero_de_credito",
   "type": "sujeto_regulado",
   "label": "Proveedor no financiero de crédito",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Empresa no financiera que otorga crédito y está alcanzada por normas sobre clasificación de deudores, debiendo aplicar criterios de cartera de consumo o viviend…"
  },
  {
   "id": "otro_proveedor_no_financiero_de_credito",
   "type": "agente_regulado",
   "label": "Otro proveedor no financiero de crédito",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Proveedor no financiero de crédito sujeto a las obligaciones de protección de usuarios y publicidad de información."
  },
  {
   "id": "otros_proveedores_no_financieros_de_credito",
   "type": "entidad_regulada",
   "label": "Otros proveedores no financieros de crédito",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Proveedores no financieros que ofrecen crédito y deben cumplir con las disposiciones de protección de usuarios de servicios financieros."
  },
  {
   "id": "titulos_de_credito_no_custodiados_por_la_entidad",
   "type": "concepto_deducible_de_capital",
   "label": "Títulos de crédito no custodiados por la entidad",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Títulos valores, certificados de depósitos a plazo fijo y otros títulos de crédito que físicamente no se encuentren en poder de la entidad, deducibles del capit…"
  },
  {
   "id": "entidad_no_financiera_emisora_de_tarjetas_de_credito",
   "type": "sujeto_regulado",
   "label": "Entidad no financiera emisora de tarjetas de crédito",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Empresa no financiera que emite tarjetas de crédito en modalidad de sistema cerrado y debe clasificar deudores según normas del BCRA."
  },
  {
   "id": "empresa_no_financiera_emisora_de_tarjetas_de_credito_y_compra",
   "type": "sujeto_regulado",
   "label": "Empresa no financiera emisora de tarjetas de crédito y compra",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Proveedor no financiero de crédito que emite tarjetas de crédito y/o compra y debe clasificar deudores según criterios de cartera de consumo o vivienda."
  },
  {
   "id": "empresa_no_financiera_emisora_de_tarjetas_de_credito_y_o_compra",
   "type": "sujeto_obligado",
   "label": "Empresa no financiera emisora de tarjetas de crédito y/o compra",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Empresa no financiera que emite tarjetas de crédito o compra y está sujeta a estas normas de protección."
  },
  {
   "id": "empresas_no_financieras_emisoras_de_tarjetas_de_credito_y_o_compra",
   "type": "entidad_regulada",
   "label": "Empresas no financieras emisoras de tarjetas de crédito y/o compra",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Empresas que emiten tarjetas de crédito y/o compra y deben cumplir con las disposiciones de protección de usuarios de servicios financieros."
  },
  {
   "id": "nota_de_credito",
   "type": "circunstancia_modificatoria",
   "label": "Nota de crédito",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Circunstancia que modifica las obligaciones con el exterior del importador y debe ser reportada al BCRA."
  }
 ]
}
```
