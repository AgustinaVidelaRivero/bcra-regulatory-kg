# Expediente validación — parte 3: trayectorias run_4 (sección 3 + apéndices)


---

# Sección 3 — run_4/CQ-014

## 3a. Respuesta final del agente (verbatim, `posthoc_run/traces/off/run_4/CQ-014.json`)

`trace.final_json`:

```json
{
 "respuesta": "Los cobros de exportaciones de servicios deben ingresarse y liquidarse en el mercado de cambios en un plazo no mayor a 20 días hábiles.",
 "citas": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.5-8 / Punto 2.2.1"
  }
 ],
 "respondible": true
}
```

`trace.final_raw` (turno final íntegro):

```
Perfecto. Tengo la información completa. Según el Knowledge Graph, los cobros de exportaciones de servicios deben ingresarse y liquidarse en el mercado de cambios en un plazo no mayor a **20 días hábiles**.

```json
{
  "respuesta": "Los cobros de exportaciones de servicios deben ingresarse y liquidarse en el mercado de cambios en un plazo no mayor a 20 días hábiles.",
  "citas": [
    {
      "source_doc": "TO_exterior_cambios_actual.pdf",
      "location": "p.5-8 / Punto 2.2.1"
    }
  ],
  "respondible": true
}
```
```

## 3b. Inventario de pasos (runtime vs. almacenado vs. re-ejecutado)

| paso | tool | input | chars runtime | chars almacenados | re-ejecutado |
|---|---|---|---|---|---|
| 1 | buscar_nodos | `{"consulta": "exportaciones servicios plazo ingreso liquidación mercado cambios", "limite": 10}` | 3460 | 1215 | = runtime ✓ |
| 2 | buscar_nodos | `{"consulta": "cobros exportaciones servicios plazo", "limite": 10}` | 3424 | 1215 | = runtime ✓ |
| 3 | ver_nodo | `{"id": "plazo_de_ingreso_y_liquidacion_de_divisas"}` | 602 | 602 | = runtime ✓ |
| 4 | ver_nodo | `{"id": "cobros_de_exportaciones_de_bienes_y_servicios"}` | 1156 | 1156 | = runtime ✓ |
| 5 | ver_vecinos | `{"id": "plazo_de_ingreso_y_liquidacion_de_divisas", "direccion": "ambas"}` | 486 | 486 | = runtime ✓ |
| 6 | buscar_nodos | `{"consulta": "servicios plazo días ingreso liquidación", "limite": 10}` | 3242 | 1215 | = runtime ✓ |
| 7 | buscar_nodos | `{"consulta": "exportación servicios 90 días plazo", "limite": 10}` | 3134 | 1215 | = runtime ✓ |
| 8 | ver_nodo | `{"id": "cobro_de_exportacion_de_servicios"}` | 590 | 590 | = runtime ✓ |
| 9 | ver_vecinos | `{"id": "cobro_de_exportacion_de_servicios", "direccion": "ambas"}` | 453 | 453 | = runtime ✓ |

**Fidelidad runtime↔re-ejecución: 9/9 pasos con largo idéntico.**

## 3c. APÉNDICE — outputs completos re-ejecutados (9 pasos)


--- paso 1 · buscar_nodos · input={"consulta": "exportaciones servicios plazo ingreso liquidación mercado cambios", "limite": 10} · runtime=3460 · re-ejecutado=3460 ---

```json
{
 "consulta": "exportaciones servicios plazo ingreso liquidación mercado cambios",
 "total_con_match": 329,
 "resultados": [
  {
   "id": "plazo_de_ingreso_y_liquidacion_de_divisas",
   "type": "requisito_regulatorio",
   "label": "Plazo de ingreso y liquidación de divisas",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Plazo establecido para que los exportadores ingresen y liquiden las divisas de sus exportaciones, contado desde la fecha de cumplido de embarque."
  },
  {
   "id": "liquidacion_de_fondos_en_mercado_de_cambios",
   "type": "requisito_regulatorio",
   "label": "Liquidación de fondos en mercado de cambios",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Compromiso del cliente de liquidar en el mercado de cambios, dentro de 5 días hábiles de su puesta a disposición, fondos recibidos en el exterior originados en …"
  },
  {
   "id": "liquidacion_de_divisas_en_mercado_de_cambios",
   "type": "operacion_regulada",
   "label": "Liquidación de divisas en mercado de cambios",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Operación de cambio de divisas realizada en el mercado de cambios a partir del 02/09/19 que corresponde a cobros de anticipos, prefinanciaciones u otras financi…"
  },
  {
   "id": "liquidacion_de_fondos_en_el_mercado_de_cambios",
   "type": "operacion_de_cambio",
   "label": "Liquidación de fondos en el mercado de cambios",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Conversión y transferencia de fondos en moneda extranjera a través del mercado de cambios, requisito para acceso a ciertas excepciones de pago."
  },
  {
   "id": "liquidacion_en_mercado_de_cambios_de_fondos_locales",
   "type": "requisito_regulatorio",
   "label": "Liquidación en mercado de cambios de fondos locales",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La totalidad de los fondos suscriptos en el país debe ser liquidada en el mercado de cambios."
  },
  {
   "id": "acceso_al_mercado_de_cambios_para_servicios_de_deuda",
   "type": "requisito_regulatorio",
   "label": "Acceso al mercado de cambios para servicios de deuda",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Requisito de haber ingresado y liquidado títulos de deuda y endeudamientos financieros en el mercado de cambios como condición para posterior acceso al mismo pa…"
  },
  {
   "id": "liquidacion_en_mercado_de_cambios_por_emisiones_de_titulos",
   "type": "operacion_de_cambios",
   "label": "Liquidación en mercado de cambios por emisiones de títulos",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Liquidaciones en mercado de cambios a partir de 09/10/20 por emisiones de títulos de deuda con registro público en el exterior u otros endeudamientos financiero…"
  },
  {
   "id": "certificacion_de_liquidacion_del_cobro_en_mercado_de_cambios",
   "type": "documento_de_validacion",
   "label": "Certificación de liquidación del cobro en mercado de cambios",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Certificación requerida cuando el siniestro fue liquidado en moneda extranjera."
  },
  {
   "id": "mercado_de_cambios",
   "type": "mercado_regulado",
   "label": "Mercado de cambios",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Mercado donde se realizan operaciones de cambio de divisas, regulado por el BCRA con pautas operativas, horarios de funcionamiento, y requisitos de identificaci…"
  },
  {
   "id": "plazo_de_liquidacion",
   "type": "requisito_temporal_regulatorio",
   "label": "Plazo de liquidación",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Período establecido para que el exportador ingrese y liquide las divisas correspondientes a una exportación de bienes."
  }
 ]
}
```

--- paso 2 · buscar_nodos · input={"consulta": "cobros exportaciones servicios plazo", "limite": 10} · runtime=3424 · re-ejecutado=3424 ---

```json
{
 "consulta": "cobros exportaciones servicios plazo",
 "total_con_match": 213,
 "resultados": [
  {
   "id": "cobros_de_exportaciones_de_bienes_y_servicios",
   "type": "concepto_de_pago",
   "label": "Cobros de exportaciones de bienes y servicios",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Fondos depositados en cuentas bancarias en el exterior originados en cobros de exportaciones de bienes y/o servicios o anticipos, prefinanciaciones o posfinanci…"
  },
  {
   "id": "cobros_de_exportaciones",
   "type": "flujo_de_divisas",
   "label": "Cobros de exportaciones",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Aplicaciones de ingresos por exportaciones que pueden destinarse al pago de intereses de financiaciones y que quedan incorporadas en el sistema online del BCRA."
  },
  {
   "id": "cobros_de_servicios_no_conexos",
   "type": "operacion_regulada",
   "label": "Cobros de servicios no conexos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Operación de cobro de servicios no conexos al comercio exterior de bienes, excepto servicios financieros, prestados por residentes argentinos a residentes parag…"
  },
  {
   "id": "cobros_de_exportaciones_de_bienes",
   "type": "flujo_de_divisas",
   "label": "Cobros de exportaciones de bienes",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Ingresos en divisas provenientes de la venta de bienes al exterior, que deben ser liquidados conforme a la normativa."
  },
  {
   "id": "divisas_de_cobros_de_exportaciones",
   "type": "concepto_de_ingreso",
   "label": "Divisas de cobros de exportaciones",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Divisas provenientes de cobros de exportaciones de bienes que pueden ser aplicadas a diversos conceptos regulados."
  },
  {
   "id": "anticipos_y_cobros_de_exportaciones",
   "type": "operacion_regulada",
   "label": "Anticipos y cobros de exportaciones",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Operación de anticipos y cobros de exportaciones argentinas de bienes y servicios conexos documentadas en pesos argentinos o en moneda del país de destino, cana…"
  },
  {
   "id": "cobros_anticipados_de_exportaciones",
   "type": "tipo_de_operacion",
   "label": "Cobros anticipados de exportaciones",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Prefinanciaciones de exportaciones del exterior o prefinanciaciones otorgadas por entidades financieras locales con fondeo en líneas de crédito del exterior."
  },
  {
   "id": "cobros_diferidos_de_exportaciones_de_bienes",
   "type": "operacion_de_comercio_exterior",
   "label": "Cobros diferidos de exportaciones de bienes",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Ingresos por exportaciones de bienes cuya liquidación se realiza con posterioridad a la fecha de embarque, conforme a plazos normativos establecidos a partir de…"
  },
  {
   "id": "cobros_locales_por_exportaciones_de_ranchos",
   "type": "mecanismo_de_cumplimiento_de_seguimiento",
   "label": "Cobros locales por exportaciones de ranchos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Cobros locales en pesos y/o moneda extranjera realizados por agentes locales de empresas propietarias de medios de transporte de bandera extranjera al exportado…"
  },
  {
   "id": "cobro_de_exportaciones_de_bienes_y_servicios",
   "type": "operacion_regulada",
   "label": "Cobro de exportaciones de bienes y servicios",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Cobros de exportaciones de bienes y servicios sujetos a obligación de ingreso y liquidación en el mercado de cambios, que pueden ser aplicados a pagos de intere…"
  }
 ]
}
```

--- paso 3 · ver_nodo · input={"id": "plazo_de_ingreso_y_liquidacion_de_divisas"} · runtime=602 · re-ejecutado=602 ---

```json
{
 "id": "plazo_de_ingreso_y_liquidacion_de_divisas",
 "type": "requisito_regulatorio",
 "label": "Plazo de ingreso y liquidación de divisas",
 "properties": {
  "description": "Plazo establecido para que los exportadores ingresen y liquiden las divisas de sus exportaciones, contado desde la fecha de cumplido de embarque.",
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
   "location": "p.91-93 / Punto 7.8.2.1 y referencias posteriores"
  }
 ]
}
```

--- paso 4 · ver_nodo · input={"id": "cobros_de_exportaciones_de_bienes_y_servicios"} · runtime=1156 · re-ejecutado=1156 ---

```json
{
 "id": "cobros_de_exportaciones_de_bienes_y_servicios",
 "type": "concepto_de_pago",
 "label": "Cobros de exportaciones de bienes y servicios",
 "properties": {
  "description": "Fondos depositados en cuentas bancarias en el exterior originados en cobros de exportaciones de bienes y/o servicios o anticipos, prefinanciaciones o posfinanciaciones de exportaciones.",
  "version": "vigente",
  "type_raw": [
   "Operación cambiaria",
   "Mecanismo de pago",
   "Concepto de pago",
   "Flujo financiero",
   "Operación comercial"
  ],
  "type_raw_counts": {
   "Operación cambiaria": 1,
   "Mecanismo de pago": 1,
   "Concepto de pago": 1,
   "Flujo financiero": 1,
   "Operación comercial": 1
  },
  "name_variants": [],
  "n_observations": 5
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.12-15 / Punto 2.6"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.25-27 / Punto 3.5.5"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.31-33 / Punto 3.6.5"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.37-39 / Punto 3.13.2"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.43-46 / Punto 3.16.2.1, inciso iii)"
  }
 ]
}
```

--- paso 5 · ver_vecinos · input={"id": "plazo_de_ingreso_y_liquidacion_de_divisas", "direccion": "ambas"} · runtime=486 · re-ejecutado=486 ---

```json
{
 "id": "plazo_de_ingreso_y_liquidacion_de_divisas",
 "label": "Plazo de ingreso y liquidación de divisas",
 "n_salientes_total": 0,
 "n_entrantes_total": 1,
 "salientes": [],
 "salientes_truncado": false,
 "entrantes": [
  {
   "relation": "determina_el_inicio_de",
   "vecino_id": "permiso_de_embarque_provisorio",
   "vecino_label": "Permiso de embarque provisorio",
   "provenances": [
    {
     "source_doc": "TO_exterior_cambios_actual.pdf",
     "location": "p.91-93 / Punto 7.8.2.1"
    }
   ]
  }
 ],
 "entrantes_truncado": false
}
```

--- paso 6 · buscar_nodos · input={"consulta": "servicios plazo días ingreso liquidación", "limite": 10} · runtime=3242 · re-ejecutado=3242 ---

```json
{
 "consulta": "servicios plazo días ingreso liquidación",
 "total_con_match": 227,
 "resultados": [
  {
   "id": "plazo_de_ingreso_y_liquidacion_de_divisas",
   "type": "requisito_regulatorio",
   "label": "Plazo de ingreso y liquidación de divisas",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Plazo establecido para que los exportadores ingresen y liquiden las divisas de sus exportaciones, contado desde la fecha de cumplido de embarque."
  },
  {
   "id": "plazo_de_240_dias_corridos_desde_registro_de_ingreso_aduanero",
   "type": "requisito_temporal",
   "label": "Plazo de 240 días corridos desde registro de ingreso aduanero",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Plazo mínimo que deben respetar las financiaciones de los puntos 7.11.1.1 a 7.11.1.4 sin vencimientos de capital y/o intereses desde el registro de ingreso adua…"
  },
  {
   "id": "plazo_de_90_dias",
   "type": "restriccion_temporal",
   "label": "Plazo de 90 días",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Período mínimo que debe transcurrir desde la adquisición de títulos valores en suscripción primaria antes de poder venderlos en mercado secundario con liquidaci…"
  },
  {
   "id": "plazo_de_liquidacion",
   "type": "requisito_temporal_regulatorio",
   "label": "Plazo de liquidación",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Período establecido para que el exportador ingrese y liquide las divisas correspondientes a una exportación de bienes."
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
  }
 ]
}
```

--- paso 7 · buscar_nodos · input={"consulta": "exportación servicios 90 días plazo", "limite": 10} · runtime=3134 · re-ejecutado=3134 ---

```json
{
 "consulta": "exportación servicios 90 días plazo",
 "total_con_match": 216,
 "resultados": [
  {
   "id": "plazo_de_90_dias",
   "type": "restriccion_temporal",
   "label": "Plazo de 90 días",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Período mínimo que debe transcurrir desde la adquisición de títulos valores en suscripción primaria antes de poder venderlos en mercado secundario con liquidaci…"
  },
  {
   "id": "plazo_de_90_dias_corridos",
   "type": "requisito_temporal",
   "label": "Plazo de 90 días corridos",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Plazo requerido desde la fecha de prestación o devengamiento del servicio para acceso al mercado de cambios en operaciones de contraparte vinculada a partir del…"
  },
  {
   "id": "exportacion_de_servicios",
   "type": "operacion_comercial",
   "label": "Exportación de servicios",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Operación de comercio exterior de servicios realizados por residentes argentinos."
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
   "id": "cobro_de_exportacion_de_servicios",
   "type": "operacion_regulada",
   "label": "Cobro de exportación de servicios",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Operación de ingreso de divisas por prestación de servicios por residentes a no residentes, que debe ser ingresada y liquidada en el mercado de cambios en plazo…"
  },
  {
   "id": "credito_en_mora_de_mas_de_90_dias",
   "type": "situacion_de_incumplimiento",
   "label": "Crédito en mora de más de 90 días",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Crédito respecto del cual el deudor posee una mora superior a 90 días, incluyendo descubiertos en cuenta corriente que exceden el límite autorizado."
  }
 ]
}
```

--- paso 8 · ver_nodo · input={"id": "cobro_de_exportacion_de_servicios"} · runtime=590 · re-ejecutado=590 ---

```json
{
 "id": "cobro_de_exportacion_de_servicios",
 "type": "operacion_regulada",
 "label": "Cobro de exportación de servicios",
 "properties": {
  "description": "Operación de ingreso de divisas por prestación de servicios por residentes a no residentes, que debe ser ingresada y liquidada en el mercado de cambios en plazo no mayor a 20 días hábiles.",
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
   "location": "p.5-8 / Punto 2.2.1"
  }
 ]
}
```

--- paso 9 · ver_vecinos · input={"id": "cobro_de_exportacion_de_servicios", "direccion": "ambas"} · runtime=453 · re-ejecutado=453 ---

```json
{
 "id": "cobro_de_exportacion_de_servicios",
 "label": "Cobro de exportación de servicios",
 "n_salientes_total": 1,
 "n_entrantes_total": 0,
 "salientes": [
  {
   "relation": "debe_ser_ingresado_y_liquidado_en",
   "vecino_id": "mercado_de_cambios",
   "vecino_label": "Mercado de cambios",
   "provenances": [
    {
     "source_doc": "TO_exterior_cambios_actual.pdf",
     "location": "p.5-8 / Punto 2.2.1"
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

# Sección 3 — run_4/CQ-019

## 3a. Respuesta final del agente (verbatim, `posthoc_run/traces/off/run_4/CQ-019.json`)

`trace.final_json`:

```json
{
 "respuesta": "Al computar los activos para la exigencia de capital por riesgo de crédito, la previsión específica es la que no se deduce. Según la normativa, el cálculo debe efectuarse sobre el monto bruto de la exposición, sin aplicar esta deducción contable.\n\nLa vinculación con la clasificación de deudores es la siguiente: la clasificación de deudores es una tarea regulatoria que debe efectuarse considerando la totalidad de las financiaciones comprendidas. Esta clasificación determina la categoría de clasificación en que se incluye cada deudor (una de cinco categorías de riesgo). A su vez, la categoría de clasificación es criterio objetivo para modificar aspectos como el término de morosidad, la situación jurídica del cliente y la refinanciación.\n\nLa previsión específica, aunque no se deduce en el cálculo de KSA (exigencia de capital promedio de exposiciones subyacentes), está directamente vinculada a la clasificación de deudores en tanto que las previsiones mínimas por riesgo de incobrabilidad se determinan en función de la categoría de clasificación asignada a cada deudor. De esta manera, la clasificación de deudores determina qué previsiones regulatorias mínimas deben constituirse, aunque la previsión específica contable no se deduzca del cálculo de capital.",
 "citas": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.42-45 / Punto 3.1.11.2, inciso i)"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "p.1-8 / Sección 1.1"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "p.17-19 / Sección 6, punto 6.5"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "p.17-19 / Sección 6, punto 6.4.1"
  }
 ],
 "respondible": true
}
```

`trace.final_raw` (turno final íntegro):

```
```json
{
  "respuesta": "Al computar los activos para la exigencia de capital por riesgo de crédito, la previsión específica es la que no se deduce. Según la normativa, el cálculo debe efectuarse sobre el monto bruto de la exposición, sin aplicar esta deducción contable.\n\nLa vinculación con la clasificación de deudores es la siguiente: la clasificación de deudores es una tarea regulatoria que debe efectuarse considerando la totalidad de las financiaciones comprendidas. Esta clasificación determina la categoría de clasificación en que se incluye cada deudor (una de cinco categorías de riesgo). A su vez, la categoría de clasificación es criterio objetivo para modificar aspectos como el término de morosidad, la situación jurídica del cliente y la refinanciación.\n\nLa previsión específica, aunque no se deduce en el cálculo de KSA (exigencia de capital promedio de exposiciones subyacentes), está directamente vinculada a la clasificación de deudores en tanto que las previsiones mínimas por riesgo de incobrabilidad se determinan en función de la categoría de clasificación asignada a cada deudor. De esta manera, la clasificación de deudores determina qué previsiones regulatorias mínimas deben constituirse, aunque la previsión específica contable no se deduzca del cálculo de capital.",
  "citas": [
    {
      "source_doc": "TO_capitales_minimos_actual.pdf",
      "location": "p.42-45 / Punto 3.1.11.2, inciso i)"
    },
    {
      "source_doc": "TO_clasificacion_deudores_actual.pdf",
      "location": "p.1-8 / Sección 1.1"
    },
    {
      "source_doc": "TO_clasificacion_deudores_actual.pdf",
      "location": "p.17-19 / Sección 6, punto 6.5"
    },
    {
      "source_doc": "TO_clasificacion_deudores_actual.pdf",
      "location": "p.17-19 / Sección 6, punto 6.4.1"
    }
  ],
  "respondible": true
}
```
```

## 3b. Inventario de pasos (runtime vs. almacenado vs. re-ejecutado)

| paso | tool | input | chars runtime | chars almacenados | re-ejecutado |
|---|---|---|---|---|---|
| 1 | buscar_nodos | `{"consulta": "exigencia capital riesgo crédito previsión incobrabilidad", "limite": 10}` | 3667 | 1215 | = runtime ✓ |
| 2 | buscar_nodos | `{"consulta": "previsión incobrabilidad deducción activos", "limite": 10}` | 2926 | 1215 | = runtime ✓ |
| 3 | buscar_nodos | `{"consulta": "clasificación deudores previsión", "limite": 10}` | 3090 | 1215 | = runtime ✓ |
| 4 | ver_nodo | `{"id": "prevision_especifica"}` | 501 | 501 | = runtime ✓ |
| 5 | ver_nodo | `{"id": "exigencia_por_riesgo_de_credito"}` | 835 | 835 | = runtime ✓ |
| 6 | ver_nodo | `{"id": "clasificacion_de_deudores"}` | 730 | 730 | = runtime ✓ |
| 7 | ver_vecinos | `{"id": "prevision_especifica", "direccion": "ambas"}` | 407 | 407 | = runtime ✓ |
| 8 | ver_vecinos | `{"id": "exigencia_por_riesgo_de_credito", "direccion": "salientes"}` | 739 | 739 | = runtime ✓ |
| 9 | buscar_nodos | `{"consulta": "previsión específica clasificación deudores", "limite": 10}` | 3412 | 1215 | = runtime ✓ |
| 10 | ver_nodo | `{"id": "prevision_regulatoria_por_riesgo_de_incobrabilidad"}` | 686 | 686 | = runtime ✓ |
| 11 | ver_vecinos | `{"id": "prevision_regulatoria_por_riesgo_de_incobrabilidad", "direccion": "ambas"}` | 785 | 785 | = runtime ✓ |
| 12 | buscar_nodos | `{"consulta": "previsión mínima incobrabilidad categoría clasificación", "limite": 10}` | 3038 | 1215 | = runtime ✓ |
| 13 | ver_nodo | `{"id": "categoria_de_clasificacion"}` | 509 | 509 | = runtime ✓ |
| 14 | ver_vecinos | `{"id": "categoria_de_clasificacion", "direccion": "ambas"}` | 1173 | 1173 | = runtime ✓ |
| 15 | ver_nodo | `{"id": "ksa"}` | 882 | 882 | = runtime ✓ |

**Fidelidad runtime↔re-ejecución: 15/15 pasos con largo idéntico.**

## 3c. APÉNDICE — outputs completos re-ejecutados (15 pasos)


--- paso 1 · buscar_nodos · input={"consulta": "exigencia capital riesgo crédito previsión incobrabilidad", "limite": 10} · runtime=3667 · re-ejecutado=3667 ---

```json
{
 "consulta": "exigencia capital riesgo crédito previsión incobrabilidad",
 "total_con_match": 325,
 "resultados": [
  {
   "id": "disminucion_de_exigencia_de_capital_minimo_por_riesgo_de_credito",
   "type": "concepto_de_facilidad_regulatoria",
   "label": "Disminución de exigencia de capital mínimo por riesgo de crédito",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Facilidad otorgada por el BCRA que reduce la exigencia de capital mínimo asociada al riesgo de crédito."
  },
  {
   "id": "promedio_de_36_meses_de_exigencia_de_capital_por_riesgo_de_credito",
   "type": "parametro_regulatorio",
   "label": "Promedio de 36 meses de exigencia de capital por riesgo de crédito",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Promedio de los últimos 36 meses de exigencia de capital mínimo por riesgo de crédito, utilizado como base para límites máximos de exigencia operacional."
  },
  {
   "id": "exigencia_por_riesgo_de_credito",
   "type": "requisito_regulatorio_de_capital",
   "label": "Exigencia por riesgo de crédito",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Exigencia de capital que las entidades financieras deben mantener, calculada mediante una fórmula que considera activos ponderados por riesgo de crédito e incre…"
  },
  {
   "id": "prevision_por_riesgo_de_incobrabilidad",
   "type": "calculo_regulatorio",
   "label": "Previsión por riesgo de incobrabilidad",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Previsiones generales y específicas que se computan para determinar la exigencia de capital en operaciones de titulización, con tratamiento diferenciado según s…"
  },
  {
   "id": "exigencia_de_capital_por_riesgo_de_mercado",
   "type": "requisito_de_capital",
   "label": "Exigencia de capital por riesgo de mercado",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Suma aritmética de las exigencias de capital por riesgos de tasa de interés, acciones, tipo de cambio, productos básicos y opciones."
  },
  {
   "id": "exigencia_de_capital_por_riesgo_especifico",
   "type": "requisito_regulatorio",
   "label": "Exigencia de capital por riesgo específico",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Exigencia de capital calculada para posiciones de titulización, derivados de crédito y posiciones cubiertas, expresada como porcentaje del importe ponderado por…"
  },
  {
   "id": "exigencia_de_capital_por_riesgo_operacional",
   "type": "requisito_regulatorio",
   "label": "Exigencia de capital por riesgo operacional",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Requerimiento de capital que las entidades financieras deben mantener para cubrir riesgos operacionales, calculado mensualmente según fórmulas específicas para …"
  },
  {
   "id": "incrementos_de_exigencia_por_riesgo_de_credito",
   "type": "ajuste_regulatorio",
   "label": "Incrementos de exigencia por riesgo de crédito",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Incrementos a la exigencia de capitales mínimos por excesos en activos inmovilizados, grandes exposiciones, financiamiento al sector público, derivados no cubie…"
  },
  {
   "id": "exigencia_de_capital_por_riesgo_de_tipo_de_cambio",
   "type": "requisito_regulatorio",
   "label": "Exigencia de capital por riesgo de tipo de cambio",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Capital mínimo necesario para cubrir el riesgo de mantener posiciones en moneda extranjera, incluido el oro, calculado como el 8% de la posición neta total."
  },
  {
   "id": "exigencia_de_capital_por_riesgo_operacional_cro",
   "type": "requisito_de_capital",
   "label": "Exigencia de capital por riesgo operacional (CRO)",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Exigencia de capital determinada mensualmente para entidades del grupo 2, calculada aplicando una expresión que considera el ingreso bruto positivo de los últim…"
  }
 ]
}
```

--- paso 2 · buscar_nodos · input={"consulta": "previsión incobrabilidad deducción activos", "limite": 10} · runtime=2926 · re-ejecutado=2926 ---

```json
{
 "consulta": "previsión incobrabilidad deducción activos",
 "total_con_match": 89,
 "resultados": [
  {
   "id": "prevision_por_riesgo_de_incobrabilidad",
   "type": "calculo_regulatorio",
   "label": "Previsión por riesgo de incobrabilidad",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Previsiones generales y específicas que se computan para determinar la exigencia de capital en operaciones de titulización, con tratamiento diferenciado según s…"
  },
  {
   "id": "prevision_regulatoria_por_riesgo_de_incobrabilidad",
   "type": "concepto_deducible_de_capital",
   "label": "Previsión regulatoria por riesgo de incobrabilidad",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Previsión determinada por aplicación de normas sobre previsiones mínimas por riesgo de incobrabilidad, cuya diferencia positiva respecto de la previsión contabl…"
  },
  {
   "id": "activos_fijos",
   "type": "concepto_excluido",
   "label": "Activos fijos",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Activos fijos excluidos del cálculo de información complementaria vinculada al riesgo de tasa de interés."
  },
  {
   "id": "otros_activos",
   "type": "categoria_de_activo",
   "label": "Otros activos",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Exposición con código 12000000 y ponderador de riesgo del 75%."
  },
  {
   "id": "venta_de_activos",
   "type": "operacion_de_cartera",
   "label": "Venta de activos",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Cierre de posiciones mediante venta, cuya ganancia o pérdida se calcula entre el precio de venta y el último precio de valuación."
  },
  {
   "id": "activos_rotativos",
   "type": "tipo_de_activo",
   "label": "Activos rotativos",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Activos como tarjetas de crédito, facturas y otras exposiciones cancelables en un solo pago, exentos del requisito de pago previo registrado."
  },
  {
   "id": "activos_segregados",
   "type": "tipo_de_garantia",
   "label": "Activos segregados",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Activos aportados por la contraparte que se encuentran segregados, fuera del alcance del procedimiento de quiebra y que se presume serán devueltos en caso de qu…"
  },
  {
   "id": "canasta_de_activos",
   "type": "estructura_de_garantia",
   "label": "Canasta de activos",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Conjunto de varios activos recibidos en garantía, cuyo aforo se calcula como la suma ponderada de los aforos individuales según la participación de cada activo …"
  },
  {
   "id": "cartera_de_activos",
   "type": "conjunto_de_activos",
   "label": "Cartera de activos",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Conjunto de documentos a cobrar y derechos de crédito que respaldan una titulización y cuyo riesgo crediticio debe ser evaluable por los inversores."
  },
  {
   "id": "activos_computables",
   "type": "componente_de_aprc",
   "label": "Activos computables",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Exposiciones que se incluyen en el cálculo de activos ponderados por riesgo de crédito."
  }
 ]
}
```

--- paso 3 · buscar_nodos · input={"consulta": "clasificación deudores previsión", "limite": 10} · runtime=3090 · re-ejecutado=3090 ---

```json
{
 "consulta": "clasificación deudores previsión",
 "total_con_match": 24,
 "resultados": [
  {
   "id": "clasificacion_de_deudores",
   "type": "tarea_regulatoria",
   "label": "Clasificación de deudores",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Clasificación que debe efectuarse con una periodicidad que atienda a la importancia del deudor, considerando la totalidad de las financiaciones comprendidas, de…"
  },
  {
   "id": "manual_de_procedimientos_de_clasificacion_y_prevision",
   "type": "documento_regulatorio",
   "label": "Manual de procedimientos de clasificación y previsión",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Manual que debe contener los procedimientos implementados, los niveles que intervienen en el análisis y decisión, y debe estar a disposición permanente de la Su…"
  },
  {
   "id": "prevision_especifica",
   "type": "ajuste_contable",
   "label": "Previsión específica",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Deducción contable que no se aplica al cálculo de KSA; el cálculo debe efectuarse sobre monto bruto de la exposición."
  },
  {
   "id": "prevision_regulatoria",
   "type": "ajuste_de_capital",
   "label": "Previsión regulatoria",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Previsión según normas sobre Previsiones mínimas por riesgo de incobrabilidad, utilizada para comparación con previsión contable."
  },
  {
   "id": "tarea_de_clasificacion",
   "type": "funcion_regulatoria",
   "label": "Tarea de clasificación",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Proceso de asignación de categorías de riesgo a deudores, que puede ser encomendada a un área independiente, al sector de créditos con revisión independiente, o…"
  },
  {
   "id": "prevision_contable_niif_9",
   "type": "parametro_contable",
   "label": "Previsión contable NIIF 9",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Previsión por pérdida crediticia esperada calculada conforme al punto 5.5 de la NIIF 9."
  },
  {
   "id": "categoria_de_clasificacion",
   "type": "nivel_de_riesgo",
   "label": "Categoría de clasificación",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Una de las cinco categorías en que se clasifica a cada cliente y la totalidad de sus financiaciones comprendidas."
  },
  {
   "id": "clasificacion_irrecuperable",
   "type": "categoria_de_clasificacion_de_deudores",
   "label": "Clasificación irrecuperable",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Categoría de riesgo para deudas consideradas incobrables, donde la incobrabilidad es evidente al momento del análisis, aunque podrían tener algún valor de recup…"
  },
  {
   "id": "diferencia_de_prevision_niif_9",
   "type": "componente_de_capital_regulatorio",
   "label": "Diferencia de previsión NIIF 9",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Diferencia positiva o negativa entre la previsión contable según NIIF 9 y la previsión regulatoria según normas sobre previsiones mínimas por riesgo de incobrab…"
  },
  {
   "id": "fondo_compensador_de_prevision",
   "type": "sujeto_regulado",
   "label": "Fondo compensador de previsión",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Fondo que realiza transferencias de fondos compensadores de previsión elegibles para boleto global diario."
  }
 ]
}
```

--- paso 4 · ver_nodo · input={"id": "prevision_especifica"} · runtime=501 · re-ejecutado=501 ---

```json
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
```

--- paso 5 · ver_nodo · input={"id": "exigencia_por_riesgo_de_credito"} · runtime=835 · re-ejecutado=835 ---

```json
{
 "id": "exigencia_por_riesgo_de_credito",
 "type": "requisito_regulatorio_de_capital",
 "label": "Exigencia por riesgo de crédito",
 "properties": {
  "description": "Exigencia de capital que las entidades financieras deben mantener, calculada mediante una fórmula que considera activos ponderados por riesgo de crédito e incrementos normativos.",
  "version": "vigente",
  "type_raw": [
   "Requisito regulatorio de capital",
   "Componente de Exigencia de Capital"
  ],
  "type_raw_counts": {
   "Requisito regulatorio de capital": 1,
   "Componente de Exigencia de Capital": 1
  },
  "name_variants": [],
  "n_observations": 2
 },
 "provenances": [
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "p.1-5 / Sección 3, punto 3.1.2"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "p.31-35 / Sección 7.1"
  }
 ]
}
```

--- paso 6 · ver_nodo · input={"id": "clasificacion_de_deudores"} · runtime=730 · re-ejecutado=730 ---

```json
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
```

--- paso 7 · ver_vecinos · input={"id": "prevision_especifica", "direccion": "ambas"} · runtime=407 · re-ejecutado=407 ---

```json
{
 "id": "prevision_especifica",
 "label": "Previsión específica",
 "n_salientes_total": 1,
 "n_entrantes_total": 0,
 "salientes": [
  {
   "relation": "no_se_deduce_en_calculo_de",
   "vecino_id": "ksa",
   "vecino_label": "KSA",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "p.42-45 / Punto 3.1.11.2, inciso i)"
    }
   ]
  }
 ],
 "salientes_truncado": false,
 "entrantes": [],
 "entrantes_truncado": false
}
```

--- paso 8 · ver_vecinos · input={"id": "exigencia_por_riesgo_de_credito", "direccion": "salientes"} · runtime=739 · re-ejecutado=739 ---

```json
{
 "id": "exigencia_por_riesgo_de_credito",
 "label": "Exigencia por riesgo de crédito",
 "n_salientes_total": 2,
 "n_entrantes_total": 2,
 "salientes": [
  {
   "relation": "se_calcula_mediante",
   "vecino_id": "activos_ponderados_por_riesgo_de_credito",
   "vecino_label": "Activos ponderados por riesgo de crédito",
   "provenances": [
    {
     "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
     "location": "p.1-5 / Sección 3, punto 3.1.2"
    }
   ]
  },
  {
   "relation": "utiliza_en_su_calculo",
   "vecino_id": "factor_de_calificacion_de_entidad",
   "vecino_label": "Factor de calificación de entidad",
   "provenances": [
    {
     "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
     "location": "p.1-5 / Sección 3, punto 3.1.2"
    }
   ]
  }
 ],
 "salientes_truncado": false
}
```

--- paso 9 · buscar_nodos · input={"consulta": "previsión específica clasificación deudores", "limite": 10} · runtime=3412 · re-ejecutado=3412 ---

```json
{
 "consulta": "previsión específica clasificación deudores",
 "total_con_match": 24,
 "resultados": [
  {
   "id": "prevision_especifica",
   "type": "ajuste_contable",
   "label": "Previsión específica",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Deducción contable que no se aplica al cálculo de KSA; el cálculo debe efectuarse sobre monto bruto de la exposición."
  },
  {
   "id": "clasificacion_de_deudores",
   "type": "tarea_regulatoria",
   "label": "Clasificación de deudores",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Clasificación que debe efectuarse con una periodicidad que atienda a la importancia del deudor, considerando la totalidad de las financiaciones comprendidas, de…"
  },
  {
   "id": "manual_de_procedimientos_de_clasificacion_y_prevision",
   "type": "documento_regulatorio",
   "label": "Manual de procedimientos de clasificación y previsión",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Manual que debe contener los procedimientos implementados, los niveles que intervienen en el análisis y decisión, y debe estar a disposición permanente de la Su…"
  },
  {
   "id": "exposicion_en_incumplimiento_con_prevision_especifica_menor_al_20",
   "type": "categoria_de_exposicion_crediticia",
   "label": "Exposición en incumplimiento con previsión específica menor al 20%",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Exposición o tramo en situación de incumplimiento no cubierto por coberturas de riesgo de crédito, con previsiones específicas menores al 20% del saldo pendient…"
  },
  {
   "id": "exposicion_en_incumplimiento_con_prevision_especifica_entre_20_y_50",
   "type": "categoria_de_exposicion_crediticia",
   "label": "Exposición en incumplimiento con previsión específica entre 20% y 50%",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Exposición o tramo en situación de incumplimiento no cubierto por coberturas de riesgo de crédito, con previsiones específicas iguales o mayores al 20% y menore…"
  },
  {
   "id": "exposicion_en_incumplimiento_con_prevision_especifica_igual_o_mayor_al_50",
   "type": "categoria_de_exposicion_crediticia",
   "label": "Exposición en incumplimiento con previsión específica igual o mayor al 50%",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Exposición o tramo en situación de incumplimiento no cubierto por coberturas de riesgo de crédito, con previsiones específicas iguales o mayores al 50% del sald…"
  },
  {
   "id": "prevision_regulatoria",
   "type": "ajuste_de_capital",
   "label": "Previsión regulatoria",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Previsión según normas sobre Previsiones mínimas por riesgo de incobrabilidad, utilizada para comparación con previsión contable."
  },
  {
   "id": "tarea_de_clasificacion",
   "type": "funcion_regulatoria",
   "label": "Tarea de clasificación",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Proceso de asignación de categorías de riesgo a deudores, que puede ser encomendada a un área independiente, al sector de créditos con revisión independiente, o…"
  },
  {
   "id": "prevision_contable_niif_9",
   "type": "parametro_contable",
   "label": "Previsión contable NIIF 9",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Previsión por pérdida crediticia esperada calculada conforme al punto 5.5 de la NIIF 9."
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

--- paso 10 · ver_nodo · input={"id": "prevision_regulatoria_por_riesgo_de_incobrabilidad"} · runtime=686 · re-ejecutado=686 ---

```json
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
```

--- paso 11 · ver_vecinos · input={"id": "prevision_regulatoria_por_riesgo_de_incobrabilidad", "direccion": "ambas"} · runtime=785 · re-ejecutado=785 ---

```json
{
 "id": "prevision_regulatoria_por_riesgo_de_incobrabilidad",
 "label": "Previsión regulatoria por riesgo de incobrabilidad",
 "n_salientes_total": 1,
 "n_entrantes_total": 1,
 "salientes": [
  {
   "relation": "deducible_de",
   "vecino_id": "capital_ordinario_de_nivel_uno_co_n1",
   "vecino_label": "Capital ordinario de nivel uno (CO n1)",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "p.161-163 / Punto 8.4.1.1"
    }
   ]
  }
 ],
 "salientes_truncado": false,
 "entrantes": [
  {
   "relation": "se_compara_con",
   "vecino_id": "prevision_contable_por_deterioro_de_valor_niif_9",
   "vecino_label": "Previsión contable por deterioro de valor (NIIF 9)",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "p.161-163 / Punto 8.4.1.1"
    }
   ]
  }
 ],
 "entrantes_truncado": false
}
```

--- paso 12 · buscar_nodos · input={"consulta": "previsión mínima incobrabilidad categoría clasificación", "limite": 10} · runtime=3038 · re-ejecutado=3038 ---

```json
{
 "consulta": "previsión mínima incobrabilidad categoría clasificación",
 "total_con_match": 29,
 "resultados": [
  {
   "id": "categoria_de_clasificacion",
   "type": "nivel_de_riesgo",
   "label": "Categoría de clasificación",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Una de las cinco categorías en que se clasifica a cada cliente y la totalidad de sus financiaciones comprendidas."
  },
  {
   "id": "prevision_por_riesgo_de_incobrabilidad",
   "type": "calculo_regulatorio",
   "label": "Previsión por riesgo de incobrabilidad",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Previsiones generales y específicas que se computan para determinar la exigencia de capital en operaciones de titulización, con tratamiento diferenciado según s…"
  },
  {
   "id": "prevision_regulatoria_por_riesgo_de_incobrabilidad",
   "type": "concepto_deducible_de_capital",
   "label": "Previsión regulatoria por riesgo de incobrabilidad",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Previsión determinada por aplicación de normas sobre previsiones mínimas por riesgo de incobrabilidad, cuya diferencia positiva respecto de la previsión contabl…"
  },
  {
   "id": "manual_de_procedimientos_de_clasificacion_y_prevision",
   "type": "documento_regulatorio",
   "label": "Manual de procedimientos de clasificación y previsión",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Manual que debe contener los procedimientos implementados, los niveles que intervienen en el análisis y decisión, y debe estar a disposición permanente de la Su…"
  },
  {
   "id": "categoria_1_de_bi",
   "type": "categoria_de_tamano",
   "label": "Categoría 1 de BI",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Tramo de BI igual o inferior al equivalente en pesos de €1.000 millones, con coeficiente marginal del 12%."
  },
  {
   "id": "categoria_2_de_bi",
   "type": "categoria_de_tamano",
   "label": "Categoría 2 de BI",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Tramo de BI superior a €1.000 millones e inferior o igual a €30.000 millones, con coeficiente marginal del 15%."
  },
  {
   "id": "categoria_3_de_bi",
   "type": "categoria_de_tamano",
   "label": "Categoría 3 de BI",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Tramo de BI superior a €30.000 millones, con coeficiente marginal del 18%."
  },
  {
   "id": "prevision_especifica",
   "type": "ajuste_contable",
   "label": "Previsión específica",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Deducción contable que no se aplica al cálculo de KSA; el cálculo debe efectuarse sobre monto bruto de la exposición."
  },
  {
   "id": "prevision_regulatoria",
   "type": "ajuste_de_capital",
   "label": "Previsión regulatoria",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Previsión según normas sobre Previsiones mínimas por riesgo de incobrabilidad, utilizada para comparación con previsión contable."
  },
  {
   "id": "tarea_de_clasificacion",
   "type": "funcion_regulatoria",
   "label": "Tarea de clasificación",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Proceso de asignación de categorías de riesgo a deudores, que puede ser encomendada a un área independiente, al sector de créditos con revisión independiente, o…"
  }
 ]
}
```

--- paso 13 · ver_nodo · input={"id": "categoria_de_clasificacion"} · runtime=509 · re-ejecutado=509 ---

```json
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
```

--- paso 14 · ver_vecinos · input={"id": "categoria_de_clasificacion", "direccion": "ambas"} · runtime=1173 · re-ejecutado=1173 ---

```json
{
 "id": "categoria_de_clasificacion",
 "label": "Categoría de clasificación",
 "n_salientes_total": 0,
 "n_entrantes_total": 4,
 "salientes": [],
 "salientes_truncado": false,
 "entrantes": [
  {
   "relation": "es_criterio_objetivo_para_modificar",
   "vecino_id": "termino_de_morosidad",
   "vecino_label": "Término de morosidad",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "p.17-19 / Sección 6, punto 6.4.1"
    }
   ]
  },
  {
   "relation": "es_criterio_objetivo_para_modificar",
   "vecino_id": "situacion_juridica_del_cliente",
   "vecino_label": "Situación jurídica del cliente",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "p.17-19 / Sección 6, punto 6.4.1"
    }
   ]
  },
  {
   "relation": "es_criterio_objetivo_para_modificar",
   "vecino_id": "refinanciacion",
   "vecino_label": "Refinanciación",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "p.17-19 / Sección 6, punto 6.4.1"
    }
   ]
  },
  {
   "relation": "se_incluye_en",
   "vecino_id": "deudor",
   "vecino_label": "Deudor",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "p.17-19 / Sección 6, punto 6.5"
    }
   ]
  }
 ],
 "entrantes_truncado": false
}
```

--- paso 15 · ver_nodo · input={"id": "ksa"} · runtime=882 · re-ejecutado=882 ---

```json
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
```

---

# Sección 3 — run_4/CQ-017

## 3a. Respuesta final del agente (verbatim, `posthoc_run/traces/off/run_4/CQ-017.json`)

`trace.final_json`:

```json
{
 "respuesta": "Sí, un operador de cambio está alcanzado por las normas de Protección de los Usuarios de Servicios Financieros. El operador de cambio es clasificado como un 'sujeto obligado' conforme a la normativa de protección de usuarios, lo que significa que debe cumplir con todas las obligaciones establecidas en esas normas, incluyendo la protección de usuarios de servicios financieros. Sin embargo, respecto a si debe intervenir como entidad autorizada en el mercado de cambios, la información disponible en el grafo no es concluyente. El mercado libre de cambios está definido como aquel por el cual se cursan operaciones realizadas por 'entidades financieras y demás personas autorizadas por el BCRA' para dedicarse al comercio de compra y venta de monedas extranjeras. Existe una categoría de 'personas jurídicas no autorizadas a operar en cambios' que requieren conformidad previa del BCRA para acceder al mercado de cambios. Sin embargo, no hay información explícita en el grafo que determine si los operadores de cambio deben o no intervenir como entidades autorizadas en el mercado de cambios.",
 "citas": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.1-5 / Punto 1.1.2.2"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.183-185 / Sección 15.1, Artículo 1° del Decreto 260/02"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.34-36 / Punto 3.10"
  }
 ],
 "respondible": false
}
```

`trace.final_raw` (turno final íntegro):

```
```json
{
  "respuesta": "Sí, un operador de cambio está alcanzado por las normas de Protección de los Usuarios de Servicios Financieros. El operador de cambio es clasificado como un 'sujeto obligado' conforme a la normativa de protección de usuarios, lo que significa que debe cumplir con todas las obligaciones establecidas en esas normas, incluyendo la protección de usuarios de servicios financieros. Sin embargo, respecto a si debe intervenir como entidad autorizada en el mercado de cambios, la información disponible en el grafo no es concluyente. El mercado libre de cambios está definido como aquel por el cual se cursan operaciones realizadas por 'entidades financieras y demás personas autorizadas por el BCRA' para dedicarse al comercio de compra y venta de monedas extranjeras. Existe una categoría de 'personas jurídicas no autorizadas a operar en cambios' que requieren conformidad previa del BCRA para acceder al mercado de cambios. Sin embargo, no hay información explícita en el grafo que determine si los operadores de cambio deben o no intervenir como entidades autorizadas en el mercado de cambios.",
  "citas": [
    {
      "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
      "location": "p.1-5 / Punto 1.1.2.2"
    },
    {
      "source_doc": "TO_exterior_cambios_actual.pdf",
      "location": "p.183-185 / Sección 15.1, Artículo 1° del Decreto 260/02"
    },
    {
      "source_doc": "TO_exterior_cambios_actual.pdf",
      "location": "p.34-36 / Punto 3.10"
    }
  ],
  "respondible": false
}
```
```

## 3b. Inventario de pasos (runtime vs. almacenado vs. re-ejecutado)

| paso | tool | input | chars runtime | chars almacenados | re-ejecutado |
|---|---|---|---|---|---|
| 1 | buscar_nodos | `{"consulta": "operador de cambio", "limite": 10}` | 2629 | 1215 | = runtime ✓ |
| 2 | buscar_nodos | `{"consulta": "protección usuarios servicios financieros", "limite": 10}` | 3555 | 1215 | = runtime ✓ |
| 3 | buscar_nodos | `{"consulta": "mercado de cambios entidad autorizada", "limite": 10}` | 3405 | 1215 | = runtime ✓ |
| 4 | ver_nodo | `{"id": "operador_de_cambio"}` | 482 | 482 | = runtime ✓ |
| 5 | ver_vecinos | `{"id": "operador_de_cambio", "direccion": "ambas"}` | 730 | 730 | = runtime ✓ |
| 6 | buscar_nodos | `{"consulta": "operador cambio protección usuarios alcanzado", "limite": 10}` | 2900 | 1215 | = runtime ✓ |
| 7 | buscar_nodos | `{"consulta": "sujeto obligado protección usuarios servicios financieros", "limite": 10}` | 3377 | 1215 | = runtime ✓ |
| 8 | ver_nodo | `{"id": "sujeto_obligado"}` | 1550 | 1214 | = runtime ✓ |
| 9 | ver_vecinos | `{"id": "sujeto_obligado", "direccion": "salientes"}` | 11006 | 1215 | = runtime ✓ |
| 10 | buscar_nodos | `{"consulta": "entidad autorizada mercado cambios intervenir", "limite": 10}` | 3306 | 1215 | = runtime ✓ |
| 11 | ver_nodo | `{"id": "mercado_libre_de_cambios"}` | 750 | 750 | = runtime ✓ |
| 12 | ver_vecinos | `{"id": "mercado_libre_de_cambios", "direccion": "ambas"}` | 461 | 461 | = runtime ✓ |
| 13 | buscar_nodos | `{"consulta": "personas autorizadas comercio compra venta monedas extranjeras", "limite": 10}` | 3011 | 1215 | = runtime ✓ |
| 14 | buscar_nodos | `{"consulta": "operador cambio exclusión no alcanzado", "limite": 10}` | 2642 | 1215 | = runtime ✓ |
| 15 | ver_nodo | `{"id": "personas_juridicas_no_autorizadas_a_operar_en_cambios"}` | 648 | 648 | = runtime ✓ |
| 16 | ver_vecinos | `{"id": "personas_juridicas_no_autorizadas_a_operar_en_cambios", "direccion": "ambas"}` | 791 | 791 | = runtime ✓ |

**Fidelidad runtime↔re-ejecución: 16/16 pasos con largo idéntico.**

## 3c. APÉNDICE — outputs completos re-ejecutados (16 pasos)


--- paso 1 · buscar_nodos · input={"consulta": "operador de cambio", "limite": 10} · runtime=2629 · re-ejecutado=2629 ---

```json
{
 "consulta": "operador de cambio",
 "total_con_match": 1748,
 "resultados": [
  {
   "id": "operador_de_cambio",
   "type": "sujeto_obligado",
   "label": "Operador de cambio",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Sujeto obligado que realiza operaciones comprendidas en las normas sobre Exterior y cambios."
  },
  {
   "id": "casa_de_cambio",
   "type": "sujeto_regulado",
   "label": "Casa de cambio",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Entidad cambiaria que opera en el mercado de cambios, sujeta a requisitos operativos mínimos de tecnología y sistemas de información."
  },
  {
   "id": "tipo_de_cambio",
   "type": "clase_de_activo",
   "label": "Tipo de cambio",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Clase de activo subyacente en derivados, con factor regulatorio de 4%, correlación N/A y volatilidad de opción de 15%."
  },
  {
   "id": "venta_de_cambio",
   "type": "operacion_regulada",
   "label": "Venta de cambio",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Operación de cambio para transferencias a personas humanas en el exterior."
  },
  {
   "id": "boleto_de_cambio",
   "type": "documento_regulado",
   "label": "Boleto de cambio",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Documento que debe constar el carácter de declaración jurada del ordenante sobre todos los datos contenidos, incluyendo el concepto de la operación y cumplimien…"
  },
  {
   "id": "compra_de_cambio",
   "type": "operacion_regulada",
   "label": "Compra de cambio",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Operación de cambio para transferencias a personas humanas residentes en el país."
  },
  {
   "id": "riesgo_de_cambio",
   "type": "tipo_de_riesgo",
   "label": "Riesgo de cambio",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Riesgo calculado conforme al punto 6.4.3 de las normas sobre Capitales mínimos, utilizando códigos de partida específicos y un factor de ponderación del 0.08."
  },
  {
   "id": "agencia_de_cambio",
   "type": "sujeto_regulado",
   "label": "Agencia de cambio",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Entidad cambiaria cuyas tenencias en moneda extranjera están limitadas por regulación del BCRA."
  },
  {
   "id": "operacion_de_cambio",
   "type": "operacion_regulada",
   "label": "Operación de cambio",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Operación de cambio, canje y/o arbitraje que se cursa en el mercado de cambios y requiere boleto de compra y/o venta conforme a lo estipulado en el TO."
  },
  {
   "id": "concertacion_de_cambio",
   "type": "operacion_regulada",
   "label": "Concertación de cambio",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Operación de cambio que el beneficiario puede realizar con los fondos acreditados en su cuenta de corresponsalía."
  }
 ]
}
```

--- paso 2 · buscar_nodos · input={"consulta": "protección usuarios servicios financieros", "limite": 10} · runtime=3555 · re-ejecutado=3555 ---

```json
{
 "consulta": "protección usuarios servicios financieros",
 "total_con_match": 120,
 "resultados": [
  {
   "id": "comite_de_proteccion_de_los_usuarios_de_servicios_financieros",
   "type": "organo_regulado",
   "label": "Comité de Protección de los Usuarios de Servicios Financieros",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Órgano alternativo integrado por al menos un miembro del Directorio y responsables de cumplimiento normativo, gestión de riesgo operativo y asuntos legales, con…"
  },
  {
   "id": "directivo_responsable_de_proteccion_de_los_usuarios_de_servicios_financieros",
   "type": "cargo_regulatorio",
   "label": "Directivo Responsable de Protección de los Usuarios de Servicios Financieros",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Funcionario responsable de elevar reportes trimestrales al Directorio sobre acciones realizadas en protección de usuarios y evaluación de informes del Responsab…"
  },
  {
   "id": "usuarios_de_servicios_financieros",
   "type": "sujeto_regulado",
   "label": "Usuarios de servicios financieros",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Personas humanas que contratan productos y/o servicios financieros con los sujetos obligados."
  },
  {
   "id": "gerencia_principal_de_proteccion_al_usuario_de_servicios_financieros",
   "type": "organo_del_bcra",
   "label": "Gerencia Principal de Protección al Usuario de Servicios Financieros",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Órgano del BCRA que brinda respuesta a consultas sobre normativa, recibe comentarios y sugerencias de usuarios, y tramita reclamos no respondidos o con respuest…"
  },
  {
   "id": "servicios_financieros",
   "type": "categoria_de_servicios",
   "label": "Servicios financieros",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Servicios financieros comprendidos en las transacciones de servicios internacionales."
  },
  {
   "id": "usuario_de_servicios_financieros",
   "type": "sujeto_regulado",
   "label": "Usuario de servicios financieros",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Personas humanas y jurídicas que utilizan servicios ofrecidos por sujetos obligados en carácter de destinatarios finales, incluyendo deudores de créditos cedido…"
  },
  {
   "id": "contrato_de_servicios_financieros",
   "type": "instrumento_legal",
   "label": "Contrato de servicios financieros",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Documento que debe ser formalizado con el usuario, quien tiene derecho a recibir copia, y que debe contener notificación de comisiones, cargos, derechos, obliga…"
  },
  {
   "id": "productos_y_servicios_financieros",
   "type": "oferta_regulada",
   "label": "Productos y servicios financieros",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Productos y servicios que ofrecen los sujetos obligados y que deben ser diseñados y modificados con participación del responsable de atención al usuario para su…"
  },
  {
   "id": "identificacion_del_usuario_de_servicios_financieros",
   "type": "contenido_contractual_obligatorio",
   "label": "Identificación del usuario de servicios financieros",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Elemento mínimo que debe contener todo contrato financiero, incluyendo nombres, apellidos, tipo y número de documento, CUIT/CUIL/CDI y domicilio para personas h…"
  },
  {
   "id": "servicio_de_atencion_al_usuario_de_servicios_financieros",
   "type": "servicio_obligatorio",
   "label": "Servicio de Atención al Usuario de Servicios Financieros",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Servicio que debe ser objeto de evaluación integral anual por la auditoría interna y debe cumplir con obligaciones de atención y registro de consultas y reclamo…"
  }
 ]
}
```

--- paso 3 · buscar_nodos · input={"consulta": "mercado de cambios entidad autorizada", "limite": 10} · runtime=3405 · re-ejecutado=3405 ---

```json
{
 "consulta": "mercado de cambios entidad autorizada",
 "total_con_match": 1800,
 "resultados": [
  {
   "id": "mercado_de_cambios",
   "type": "mercado_regulado",
   "label": "Mercado de cambios",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Mercado donde se realizan operaciones de cambio de divisas, regulado por el BCRA con pautas operativas, horarios de funcionamiento, y requisitos de identificaci…"
  },
  {
   "id": "mercado_libre_de_cambios",
   "type": "sistema_regulatorio",
   "label": "Mercado libre de cambios",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Mercado por el cual se cursan las operaciones de cambio realizadas por entidades financieras y demás personas autorizadas por el BCRA para dedicarse al comercio…"
  },
  {
   "id": "mercado_local_de_cambios",
   "type": "mercado_regulado",
   "label": "Mercado local de cambios",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Mercado donde se realizan operaciones de cambio para cancelar anticipos u otras financiaciones de exportaciones, sujeto a regulación del BCRA."
  },
  {
   "id": "acceso_al_mercado_de_cambios",
   "type": "operacion_de_cambios",
   "label": "Acceso al mercado de cambios",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Acceso que debe producirse con anterioridad no mayor a 3 días hábiles a la fecha de vencimiento del servicio de capital o interés."
  },
  {
   "id": "periodo_de_acceso_al_mercado_de_cambios",
   "type": "requisito_temporal",
   "label": "Período de acceso al mercado de cambios",
   "tokens_matcheados": 3,
   "resumen_propiedades": "El acceso al mercado de cambios se produce no antes de los 2 años corridos contados desde la fecha de liquidación en el mercado de cambios del aporte que permit…"
  },
  {
   "id": "liquidacion_de_fondos_en_mercado_de_cambios",
   "type": "requisito_regulatorio",
   "label": "Liquidación de fondos en mercado de cambios",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Compromiso del cliente de liquidar en el mercado de cambios, dentro de 5 días hábiles de su puesta a disposición, fondos recibidos en el exterior originados en …"
  },
  {
   "id": "liquidacion_de_divisas_en_mercado_de_cambios",
   "type": "operacion_regulada",
   "label": "Liquidación de divisas en mercado de cambios",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Operación de cambio de divisas realizada en el mercado de cambios a partir del 02/09/19 que corresponde a cobros de anticipos, prefinanciaciones u otras financi…"
  },
  {
   "id": "certificacion_de_acceso_al_mercado_de_cambios",
   "type": "documento_regulatorio",
   "label": "Certificación de acceso al mercado de cambios",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Certificado emitido por la entidad nominada que habilita al importador para acceder al mercado de cambios y realizar pagos de deudas de importación."
  },
  {
   "id": "limite_del_40_de_acceso_al_mercado_de_cambios",
   "type": "parametro_regulatorio",
   "label": "Límite del 40% de acceso al mercado de cambios",
   "tokens_matcheados": 3,
   "resumen_propiedades": "El monto de capital por el cual se accedió al mercado de cambios hasta 31/12/23 no debe superar el 40% del monto del capital que vencía, con excepciones especif…"
  },
  {
   "id": "liquidacion_de_fondos_en_el_mercado_de_cambios",
   "type": "operacion_de_cambio",
   "label": "Liquidación de fondos en el mercado de cambios",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Conversión y transferencia de fondos en moneda extranjera a través del mercado de cambios, requisito para acceso a ciertas excepciones de pago."
  }
 ]
}
```

--- paso 4 · ver_nodo · input={"id": "operador_de_cambio"} · runtime=482 · re-ejecutado=482 ---

```json
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
```

--- paso 5 · ver_vecinos · input={"id": "operador_de_cambio", "direccion": "ambas"} · runtime=730 · re-ejecutado=730 ---

```json
{
 "id": "operador_de_cambio",
 "label": "Operador de cambio",
 "n_salientes_total": 0,
 "n_entrantes_total": 2,
 "salientes": [],
 "salientes_truncado": false,
 "entrantes": [
  {
   "relation": "utiliza_servicios_de",
   "vecino_id": "usuario_de_servicios_financieros",
   "vecino_label": "Usuario de servicios financieros",
   "provenances": [
    {
     "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
     "location": "p.1-5 / Punto 1.1.1"
    }
   ]
  },
  {
   "relation": "supervisa",
   "vecino_id": "banco_central_de_la_republica_argentina",
   "vecino_label": "Banco Central de la República Argentina",
   "provenances": [
    {
     "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
     "location": "p.1-5 / Punto 1.2"
    }
   ]
  }
 ],
 "entrantes_truncado": false
}
```

--- paso 6 · buscar_nodos · input={"consulta": "operador cambio protección usuarios alcanzado", "limite": 10} · runtime=2900 · re-ejecutado=2900 ---

```json
{
 "consulta": "operador cambio protección usuarios alcanzado",
 "total_con_match": 47,
 "resultados": [
  {
   "id": "operador_de_cambio",
   "type": "sujeto_obligado",
   "label": "Operador de cambio",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Sujeto obligado que realiza operaciones comprendidas en las normas sobre Exterior y cambios."
  },
  {
   "id": "comite_de_proteccion_de_los_usuarios_de_servicios_financieros",
   "type": "organo_regulado",
   "label": "Comité de Protección de los Usuarios de Servicios Financieros",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Órgano alternativo integrado por al menos un miembro del Directorio y responsables de cumplimiento normativo, gestión de riesgo operativo y asuntos legales, con…"
  },
  {
   "id": "directivo_responsable_de_proteccion_de_los_usuarios_de_servicios_financieros",
   "type": "cargo_regulatorio",
   "label": "Directivo Responsable de Protección de los Usuarios de Servicios Financieros",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Funcionario responsable de elevar reportes trimestrales al Directorio sobre acciones realizadas en protección de usuarios y evaluación de informes del Responsab…"
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

--- paso 7 · buscar_nodos · input={"consulta": "sujeto obligado protección usuarios servicios financieros", "limite": 10} · runtime=3377 · re-ejecutado=3377 ---

```json
{
 "consulta": "sujeto obligado protección usuarios servicios financieros",
 "total_con_match": 126,
 "resultados": [
  {
   "id": "comite_de_proteccion_de_los_usuarios_de_servicios_financieros",
   "type": "organo_regulado",
   "label": "Comité de Protección de los Usuarios de Servicios Financieros",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Órgano alternativo integrado por al menos un miembro del Directorio y responsables de cumplimiento normativo, gestión de riesgo operativo y asuntos legales, con…"
  },
  {
   "id": "directivo_responsable_de_proteccion_de_los_usuarios_de_servicios_financieros",
   "type": "cargo_regulatorio",
   "label": "Directivo Responsable de Protección de los Usuarios de Servicios Financieros",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Funcionario responsable de elevar reportes trimestrales al Directorio sobre acciones realizadas en protección de usuarios y evaluación de informes del Responsab…"
  },
  {
   "id": "usuarios_de_servicios_financieros",
   "type": "sujeto_regulado",
   "label": "Usuarios de servicios financieros",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Personas humanas que contratan productos y/o servicios financieros con los sujetos obligados."
  },
  {
   "id": "gerencia_principal_de_proteccion_al_usuario_de_servicios_financieros",
   "type": "organo_del_bcra",
   "label": "Gerencia Principal de Protección al Usuario de Servicios Financieros",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Órgano del BCRA que brinda respuesta a consultas sobre normativa, recibe comentarios y sugerencias de usuarios, y tramita reclamos no respondidos o con respuest…"
  },
  {
   "id": "sujeto_obligado",
   "type": "entidad_regulada",
   "label": "Sujeto obligado",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Entidad financiera, empresa no financiera emisora de tarjetas de crédito u otro proveedor no financiero de crédito sujeto a las obligaciones de protección de us…"
  },
  {
   "id": "servicios_financieros",
   "type": "categoria_de_servicios",
   "label": "Servicios financieros",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Servicios financieros comprendidos en las transacciones de servicios internacionales."
  },
  {
   "id": "reclamo_ante_sujeto_obligado",
   "type": "procedimiento_regulatorio",
   "label": "Reclamo ante sujeto obligado",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Presentación formal de un reclamo por cobro indebido que inicia el plazo de 10 días hábiles para reintegro."
  },
  {
   "id": "usuario_de_servicios_financieros",
   "type": "sujeto_regulado",
   "label": "Usuario de servicios financieros",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Personas humanas y jurídicas que utilizan servicios ofrecidos por sujetos obligados en carácter de destinatarios finales, incluyendo deudores de créditos cedido…"
  },
  {
   "id": "contrato_de_servicios_financieros",
   "type": "instrumento_legal",
   "label": "Contrato de servicios financieros",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Documento que debe ser formalizado con el usuario, quien tiene derecho a recibir copia, y que debe contener notificación de comisiones, cargos, derechos, obliga…"
  },
  {
   "id": "productos_y_servicios_financieros",
   "type": "oferta_regulada",
   "label": "Productos y servicios financieros",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Productos y servicios que ofrecen los sujetos obligados y que deben ser diseñados y modificados con participación del responsable de atención al usuario para su…"
  }
 ]
}
```

--- paso 8 · ver_nodo · input={"id": "sujeto_obligado"} · runtime=1550 · re-ejecutado=1550 ---

```json
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
```

--- paso 9 · ver_vecinos · input={"id": "sujeto_obligado", "direccion": "salientes"} · runtime=11006 · re-ejecutado=11006 ---

```json
{
 "id": "sujeto_obligado",
 "label": "Sujeto obligado",
 "n_salientes_total": 57,
 "n_entrantes_total": 3,
 "salientes": [
  {
   "relation": "es_responsable_conjuntamente_con",
   "vecino_id": "tercero_que_desarrolla_tareas_de_servicios",
   "vecino_label": "Tercero que desarrolla tareas de servicios",
   "provenances": [
    {
     "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
     "location": "p.1-5 / Punto 1.1.2"
    }
   ]
  },
  {
   "relation": "proporciona_informacion_a",
   "vecino_id": "regimen_de_transparencia",
   "vecino_label": "Régimen de Transparencia",
   "provenances": [
    {
     "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
     "location": "p.9-11 / Punto 2.3.1.1, inciso viii"
    }
   ]
  },
  {
   "relation": "debe_proporcionar",
   "vecino_id": "ejemplar_del_contrato",
   "vecino_label": "Ejemplar del contrato",
   "provenances": [
    {
     "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
     "location": "p.9-11 / Punto 2.3.1.3"
    }
   ]
  },
  {
   "relation": "debe_entregar",
   "vecino_id": "resumen_informativo_del_contrato",
   "vecino_label": "Resumen informativo del contrato",
   "provenances": [
    {
     "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
     "location": "p.9-11 / Punto 2.3.1.4"
    }
   ]
  },
  {
   "relation": "transfiere_al_usuario_costo_de",
   "vecino_id": "cargo",
   "vecino_label": "Cargo",
   "provenances": [
    {
     "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
     "location": "p.9-11 / Punto 2.3.2.1"
    }
   ]
  },
  {
   "relation": "puede_aplicar",
   "vecino_id": "comision_sobre_importes_no_utilizados",
   "vecino_label": "Comisión sobre importes no utilizados",
   "provenances": [
    {
     "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
     "location": "p.12-14 / Punto 2.3.2.1, párrafo inicial"
    }
   ]
  },
  {
   "relation": "puede_aplicar",
   "vecino_id": "comision_por_precancelacion",
   "vecino_label": "Comisión por precancelación",
   "provenances": [
    {
     "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
     "location": "p.12-14 / Punto 2.3.2.1, párrafo segundo"
    }
   ]
  },
  {
   "relation": "no_puede_cobrar_comisiones_por_servicios_no_solicitados_a",
   "vecino_id": "usuario_de_servicios_financieros",
   "vecino_label": "Usuario de servicios financieros",
   "provenances": [
    {
     "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
     "location": "p.12-14 / Punto 2.3.2.2.i, párrafo segundo"
    }
   ]
  },
  {
   "relation": "no_puede_cobrar_comisiones_por",
   "vecino_id": "operacion_por_ventanilla",
   "vecino_label": "Operación por ventanilla",
   "provenances": [
    {
     "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
     "location": "p.12-14 / Punto 2.3.2.2.ii.a"
    }
   ]
  },
  {
   "relation": "no_puede_cobrar_comisiones_por",
   "vecino_id": "deposito_de_efectivo_en_pesos",
   "vecino_label": "Depósito de efectivo en pesos",
   "provenances": [
    {
     "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
     "location": "p.12-14 / Punto 2.3.2.2.ii.b"
    }
   ]
  },
  {
   "relation": "no_puede_cobrar_comisiones_por",
   "vecino_id": "contratacion_y_administracion_de_seguros",
   "vecino_label": "Contratación y administración de seguros",
   "provenances": [
    {
     "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
     "location": "p.12-14 / Punto 2.3.2.2.ii.c"
    }
   ]
  },
  {
   "relation": "no_puede_cobrar_comisiones_por",
   "vecino_id": "generacion_y_envio_de_resumenes_de_cuenta",
   "vecino_label": "Generación y envío de resúmenes de cuenta",
   "provenances": [
    {
     "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
     "location": "p.12-14 / Punto 2.3.2.2.ii.d"
    }
   ]
  },
  {
   "relation": "no_puede_cobrar_comisiones_por",
   "vecino_id": "evaluacion_otorgamiento_y_administracion_de_financiaciones",
   "vecino_label": "Evaluación, otorgamiento y administración de financiaciones",
   "provenances": [
    {
     "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
     "location": "p.12-14 / Punto 2.3.2.2.ii.e"
    }
   ]
  },
  {
   "relation": "no_puede_cobrar_comisiones_por",
   "vecino_id": "gastos_de_tasacion_notariales_o_de_escribania",
   "vecino_label": "Gastos de tasación, notariales o de escribanía",
   "provenances": [
    {
     "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
     "location": "p.12-14 / Punto 2.3.2.2.ii.f"
    }
   ]
  },
  {
   "relation": "debe_cumplir_requisitos_para_realizar",
   "vecino_id": "modificacion_de_condiciones_pactadas",
   "vecino_label": "Modificación de condiciones pactadas",
   "provenances": [
    {
     "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
     "location": "p.12-14 / Punto 2.3.4"
    }
   ]
  },
  {
   "relation": "debe_efectuar",
   "vecino_id": "notificacion_de_cambios_de_condiciones",
   "vecino_label": "Notificación de cambios de condiciones",
   "provenances": [
    {
     "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
     "location": "p.12-14 / Punto 2.3.4.iv"
    }
   ]
  },
  {
   "relation": "tiene_obligacion_de_realizar",
   "vecino_id": "reintegro_de_importes",
   "vecino_label": "Reintegro de importes",
   "provenances": [
    {
     "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
     "location": "p.15-17 / Punto 2.3.5.1"
    }
   ]
  },
  {
   "relation": "debe_acreditar_reintegro_en",
   "vecino_id": "cuenta_a_la_vista",
   "vecino_label": "Cuenta a la vista",
   "provenances": [
    {
     "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
     "location": "p.15-17 / Punto 2.3.5.1"
    }
   ]
  },
  {
   "relation": "puede_acreditar_reintegro_en",
   "vecino_id": "tarjeta_de_credito",
   "vecino_label": "Tarjeta de crédito",
   "provenances": [
    {
     "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
     "location": "p.15-17 / Punto 2.3.5.1"
    }
   ]
  },
  {
   "relation": "implementa_para_proteger_usuario",
   "vecino_id": "medida_de_seguridad",
   "vecino_label": "Medida de seguridad",
   "provenances": [
    {
     "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
     "location": "p.15-17 / Punto 2.3.6"
    }
   ]
  },
  {
   "relation": "debe_efectuar",
   "vecino_id": "notificacion_de_reintegro",
   "vecino_label": "Notificación de reintegro",
   "provenances": [
    {
     "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
     "location": "p.15-17 / Punto 2.3.5.1"
    }
   ]
  },
  {
   "relation": "notifica_a",
   "vecino_id": "responsable_de_atencion_al_usuario_de_servicios_financieros",
   "vecino_label": "Responsable de atención al usuario de servicios financieros",
   "provenances": [
    {
     "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
     "location": "p.15-17 / Punto 2.3.5.1"
    }
   ]
  },
  {
   "relation": "debe_posibilitar",
   "vecino_id": "rehabilitacion_de_producto_servicio",
   "vecino_label": "Rehabilitación de producto/servicio",
   "provenances": [
    {
     "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
     "location": "p.15-17 / Punto 2.3.6.2"
    }
   ]
  },
  {
   "relation": "celebra_con_usuario",
   "vecino_id": "contrato_de_servicios_financieros",
   "vecino_label": "Contrato de servicios financieros",
   "provenances": [
    {
     "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
     "location": "p.15-17 / Punto 2.3.8"
    }
   ]
  },
  {
   "relation": "debe_informar_al_usuario_sobre",
   "vecino_id": "medida_de_seguridad",
   "vecino_label": "Medida de seguridad",
   "provenances": [
    {
     "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
     "location": "p.15-17 / Punto 2.3.6.1"
    }
   ]
  },
  {
   "relation": "no_puede_alterar_unilateralmente",
   "vecino_id": "tasa",
   "vecino_label": "Tasa",
   "provenances": [
    {
     "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
     "location": "p.18-20 / Sección 2.3.9.8"
    }
   ]
  },
  {
   "relation": "no_puede_alterar_unilateralmente",
   "vecino_id": "comision",
   "vecino_label": "Comisión",
   "provenances": [
    {
     "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
     "location": "p.18-20 / Sección 2.3.9.8"
    }
   ]
  },
  {
   "relation": "no_puede_alterar_unilateralmente",
   "vecino_id": "cargo",
   "vecino_label": "Cargo",
   "provenances": [
    {
     "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
     "location": "p.18-20 / Sección 2.3.9.8"
    }
   ]
  },
  {
   "relation": "debe_denominar_conforme_a_normas_del_bcra",
   "vecino_id": "caja_de_ahorros_en_pesos",
   "vecino_label": "Caja de ahorros en pesos",
   "provenances": [
    {
     "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
     "location": "p.18-20 / Sección 2.3.11"
    }
   ]
  },
  {
   "relation": "debe_denominar_conforme_a_normas_del_bcra",
   "vecino_id": "caja_de_ahorros_en_dolares",
   "vecino_label": "Caja de ahorros en dólares",
   "provenances": [
    {
     "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
     "location": "p.18-20 / Sección 2.3.11"
    }
   ]
  },
  {
   "relation": "debe_denominar_conforme_a_normas_del_bcra",
   "vecino_id": "cuenta_corriente_bancaria",
   "vecino_label": "Cuenta corriente bancaria",
   "provenances": [
    {
     "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
     "location": "p.18-20 / Sección 2.3.11"
    }
   ]
  },
  {
   "relation": "debe_denominar_conforme_a_normas_del_bcra",
   "vecino_id": "cuenta_sueldo",
   "vecino_label": "Cuenta sueldo",
   "provenances": [
    {
     "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
     "location": "p.18-20 / Sección 2.3.11"
    }
   ]
  },
  {
   "relation": "debe_contratar_para_financiaciones_a_personas_humanas",
   "vecino_id": "seguro_de_vida_sobre_saldo_deudor",
   "vecino_label": "Seguro de vida sobre saldo deudor",
   "provenances": [
    {
     "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
     "location": "p.18-20 / Sección 2.3.12.1"
    }
   ]
  },
  {
   "relation": "no_puede_percibir_vinculada_a_seguros_sobre_saldo_deudor",
   "vecino_id": "comision",
   "vecino_label": "Comisión",
   "provenances": [
    {
     "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
     "location": "p.18-20 / Sección 2.3.12.1"
    }
   ]
  },
  {
   "relation": "puede_optar_por",
   "vecino_id": "autoaseguramiento_de_riesgos",
   "vecino_label": "Autoaseguramiento de riesgos",
   "provenances": [
    {
     "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
     "location": "p.18-20 / Sección 2.3.12.1"
    }
   ]
  },
  {
   "relation": "debe_ofrecer_al_menos_tres_opciones_no_vinculadas",
   "vecino_id": "compania_aseguradora",
   "vecino_label": "Compañía aseguradora",
   "provenances": [
    {
     "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
     "location": "p.18-20 / Sección 2.3.12.2"
    }
   ]
  },
  {
   "relation": "no_puede_superar_el_de_la_compania_aseguradora",
   "vecino_id": "cargo",
   "vecino_label": "Cargo",
   "provenances": [
    {
     "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
     "location": "p.18-20 / Sección 2.3.12.2"
    }
   ]
  },
  {
   "relation": "no_puede_percibir_retribucion_adicional_al_premio",
   "vecino_id": "seguro_general",
   "vecino_label": "Seguro general",
   "provenances": [
    {
     "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
     "location": "p.18-20 / Sección 2.3.13"
    }
   ]
  },
  {
   "relation": "debe_incluir_leyendas_informativas_en",
   "vecino_id": "resumen_de_cuenta",
   "vecino_label": "Resumen de cuenta",
   "provenances": [
    {
     "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
     "location": "p.18-20 / Sección 2.3.14"
    }
   ]
  },
  {
   "relation": "debe_informar_comision_de_operacion_mep",
   "vecino_id": "prestamo_hipotecario_en_pesos",
   "vecino_label": "Préstamo hipotecario en pesos",
   "provenances": [
    {
     "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
     "location": "p.18-20 / Sección 2.4.1"
    }
   ]
  }
 ],
 "salientes_truncado": true
}
```

--- paso 10 · buscar_nodos · input={"consulta": "entidad autorizada mercado cambios intervenir", "limite": 10} · runtime=3306 · re-ejecutado=3306 ---

```json
{
 "consulta": "entidad autorizada mercado cambios intervenir",
 "total_con_match": 162,
 "resultados": [
  {
   "id": "entidad_autorizada",
   "type": "sujeto_regulado",
   "label": "Entidad autorizada",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Entidad autorizada a realizar pagos anticipados de importaciones y acceder al mercado de cambios."
  },
  {
   "id": "mercado_de_cambios",
   "type": "mercado_regulado",
   "label": "Mercado de cambios",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Mercado donde se realizan operaciones de cambio de divisas, regulado por el BCRA con pautas operativas, horarios de funcionamiento, y requisitos de identificaci…"
  },
  {
   "id": "mercado_libre_de_cambios",
   "type": "sistema_regulatorio",
   "label": "Mercado libre de cambios",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Mercado por el cual se cursan las operaciones de cambio realizadas por entidades financieras y demás personas autorizadas por el BCRA para dedicarse al comercio…"
  },
  {
   "id": "mercado_local_de_cambios",
   "type": "mercado_regulado",
   "label": "Mercado local de cambios",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Mercado donde se realizan operaciones de cambio para cancelar anticipos u otras financiaciones de exportaciones, sujeto a regulación del BCRA."
  },
  {
   "id": "acceso_al_mercado_de_cambios",
   "type": "operacion_de_cambios",
   "label": "Acceso al mercado de cambios",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Acceso que debe producirse con anterioridad no mayor a 3 días hábiles a la fecha de vencimiento del servicio de capital o interés."
  },
  {
   "id": "periodo_de_acceso_al_mercado_de_cambios",
   "type": "requisito_temporal",
   "label": "Período de acceso al mercado de cambios",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El acceso al mercado de cambios se produce no antes de los 2 años corridos contados desde la fecha de liquidación en el mercado de cambios del aporte que permit…"
  },
  {
   "id": "liquidacion_de_fondos_en_mercado_de_cambios",
   "type": "requisito_regulatorio",
   "label": "Liquidación de fondos en mercado de cambios",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Compromiso del cliente de liquidar en el mercado de cambios, dentro de 5 días hábiles de su puesta a disposición, fondos recibidos en el exterior originados en …"
  },
  {
   "id": "liquidacion_de_divisas_en_mercado_de_cambios",
   "type": "operacion_regulada",
   "label": "Liquidación de divisas en mercado de cambios",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Operación de cambio de divisas realizada en el mercado de cambios a partir del 02/09/19 que corresponde a cobros de anticipos, prefinanciaciones u otras financi…"
  },
  {
   "id": "certificacion_de_acceso_al_mercado_de_cambios",
   "type": "documento_regulatorio",
   "label": "Certificación de acceso al mercado de cambios",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Certificado emitido por la entidad nominada que habilita al importador para acceder al mercado de cambios y realizar pagos de deudas de importación."
  },
  {
   "id": "limite_del_40_de_acceso_al_mercado_de_cambios",
   "type": "parametro_regulatorio",
   "label": "Límite del 40% de acceso al mercado de cambios",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El monto de capital por el cual se accedió al mercado de cambios hasta 31/12/23 no debe superar el 40% del monto del capital que vencía, con excepciones especif…"
  }
 ]
}
```

--- paso 11 · ver_nodo · input={"id": "mercado_libre_de_cambios"} · runtime=750 · re-ejecutado=750 ---

```json
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
```

--- paso 12 · ver_vecinos · input={"id": "mercado_libre_de_cambios", "direccion": "ambas"} · runtime=461 · re-ejecutado=461 ---

```json
{
 "id": "mercado_libre_de_cambios",
 "label": "Mercado libre de cambios",
 "n_salientes_total": 0,
 "n_entrantes_total": 1,
 "salientes": [],
 "salientes_truncado": false,
 "entrantes": [
  {
   "relation": "realiza_operaciones_en",
   "vecino_id": "entidad_financiera",
   "vecino_label": "Entidad financiera",
   "provenances": [
    {
     "source_doc": "TO_exterior_cambios_actual.pdf",
     "location": "p.183-185 / Sección 15.1, Artículo 1° del Decreto 260/02"
    }
   ]
  }
 ],
 "entrantes_truncado": false
}
```

--- paso 13 · buscar_nodos · input={"consulta": "personas autorizadas comercio compra venta monedas extranjeras", "limite": 10} · runtime=3011 · re-ejecutado=3011 ---

```json
{
 "consulta": "personas autorizadas comercio compra venta monedas extranjeras",
 "total_con_match": 69,
 "resultados": [
  {
   "id": "monedas_extranjeras",
   "type": "activo_regulado",
   "label": "Monedas extranjeras",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Posiciones sujetas a exigencia de capital por riesgo de tipo de cambio, cualquiera sea la cartera a la que se imputen."
  },
  {
   "id": "precios_de_compra_venta",
   "type": "dato_de_mercado",
   "label": "Precios de compra/venta",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Intervalo de precios en el mercado, del cual debe utilizarse el valor más prudente para valuación."
  },
  {
   "id": "boleto_de_compra_y_venta_de_cambio",
   "type": "documento_regulatorio",
   "label": "Boleto de compra y venta de cambio",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Documento que la entidad debe realizar conforme a lo estipulado en el punto 5.3 para operaciones cursadas a través del Sistema de Monedas Locales."
  },
  {
   "id": "personas_juridicas_no_autorizadas_a_operar_en_cambios",
   "type": "sujeto_regulado",
   "label": "Personas jurídicas no autorizadas a operar en cambios",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Personas jurídicas que no sean entidades autorizadas a operar en cambios, que requieren conformidad previa del BCRA para acceder al mercado de cambios para form…"
  },
  {
   "id": "compra_venta_de_cambio_con_liquidacion_en_moneda_local",
   "type": "tipo_de_operacion",
   "label": "Compra-venta de cambio con liquidación en moneda local",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Operación en la cual se entrega o recibe moneda local a cambio de instrumentos operados en el mercado de cambios."
  },
  {
   "id": "par_de_monedas",
   "type": "concepto_regulatorio",
   "label": "Par de monedas",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Cada par de monedas que conforma una opción se considera como un mismo subyacente para fines de cálculo de riesgo gamma y vega."
  },
  {
   "id": "boleto_de_venta",
   "type": "instrumento_de_registro",
   "label": "Boleto de venta",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Documento que debe efectuarse a nombre de la entidad cliente por el concepto de cancelación de garantías comerciales de entidades financieras por importaciones …"
  },
  {
   "id": "opcion_de_venta",
   "type": "tipo_de_opcion",
   "label": "Opción de venta",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Opción que otorga el derecho de vender el activo subyacente; sujeta a exigencias de capital según el método simplificado o delta-plus."
  },
  {
   "id": "swap_de_monedas",
   "type": "instrumento_derivado",
   "label": "Swap de monedas",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Contrato de intercambio de flujos en diferentes monedas, cuyos lados se tratan como posiciones nocionales en instrumentos pertinentes."
  },
  {
   "id": "venta_de_activo",
   "type": "operacion_de_activos",
   "label": "Venta de activo",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Fondos recibidos en el exterior originados en la venta de cualquier tipo de activo, sujetos a liquidación en mercado de cambios."
  }
 ]
}
```

--- paso 14 · buscar_nodos · input={"consulta": "operador cambio exclusión no alcanzado", "limite": 10} · runtime=2642 · re-ejecutado=2642 ---

```json
{
 "consulta": "operador cambio exclusión no alcanzado",
 "total_con_match": 181,
 "resultados": [
  {
   "id": "operador_de_cambio",
   "type": "sujeto_obligado",
   "label": "Operador de cambio",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Sujeto obligado que realiza operaciones comprendidas en las normas sobre Exterior y cambios."
  },
  {
   "id": "no_residente",
   "type": "sujeto",
   "label": "No residente",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Persona o entidad que no reside en Argentina y puede ser contraparte de contratos de obras o provisión de bienes y servicios."
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
   "id": "operacion_no_dvp",
   "type": "tipo_de_operacion_financiera",
   "label": "Operación no DvP",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Operación en la que se entrega efectivo sin recibir la correspondiente contrapartida o se entregan efectos sin el correspondiente pago de efectivo, exponiendo a…"
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

--- paso 15 · ver_nodo · input={"id": "personas_juridicas_no_autorizadas_a_operar_en_cambios"} · runtime=648 · re-ejecutado=648 ---

```json
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
```

--- paso 16 · ver_vecinos · input={"id": "personas_juridicas_no_autorizadas_a_operar_en_cambios", "direccion": "ambas"} · runtime=791 · re-ejecutado=791 ---

```json
{
 "id": "personas_juridicas_no_autorizadas_a_operar_en_cambios",
 "label": "Personas jurídicas no autorizadas a operar en cambios",
 "n_salientes_total": 2,
 "n_entrantes_total": 0,
 "salientes": [
  {
   "relation": "requiere_conformidad_previa_del_bcra_para_acceder_a",
   "vecino_id": "formacion_de_activos_externos",
   "vecino_label": "Formación de activos externos",
   "provenances": [
    {
     "source_doc": "TO_exterior_cambios_actual.pdf",
     "location": "p.34-36 / Punto 3.10"
    }
   ]
  },
  {
   "relation": "requiere_conformidad_previa_del_bcra_para_acceder_a",
   "vecino_id": "operatoria_con_derivados",
   "vecino_label": "Operatoria con derivados",
   "provenances": [
    {
     "source_doc": "TO_exterior_cambios_actual.pdf",
     "location": "p.34-36 / Punto 3.10"
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

# Sección 3 — run_4/CQ-020

## 3a. Respuesta final del agente (verbatim, `posthoc_run/traces/off/run_4/CQ-020.json`)

`trace.final_json`:

```json
{
 "respuesta": "La exigencia de capital por riesgo de crédito (CRC) se calcula mediante la fórmula: CRC = (k × 0,08 × APRC) + INC, donde k es el factor de calificación de entidad (vinculado a la calificación asignada por la SEFYC, con valores entre 1 y 1,19), 0,08 es el factor de exigencia de capital, APRC son los activos ponderados por riesgo de crédito (determinados mediante la suma de valores obtenidos aplicando ponderadores de riesgo a activos computables), e INC representa los incrementos normativos. Los activos ponderados por riesgo de crédito se calculan ponderando activos computables según factores de riesgo específicos. Respecto a la frecuencia de reporte, la información disponible en el grafo indica que las entidades deben reportar información de capital en el régimen informativo contable mensual del BCRA, aunque no se especifica explícitamente si el reporte de la exigencia de CRC es mensual, trimestral u otra periodicidad.",
 "citas": [
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "p.1-5 / Sección 3, punto 3.1.2"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.107-111 / Punto 5.3.2.1 y siguientes"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.155-157 / Punto 8.2.3.3"
  }
 ],
 "respondible": false
}
```

`trace.final_raw` (turno final íntegro):

```
```json
{
  "respuesta": "La exigencia de capital por riesgo de crédito (CRC) se calcula mediante la fórmula: CRC = (k × 0,08 × APRC) + INC, donde k es el factor de calificación de entidad (vinculado a la calificación asignada por la SEFYC, con valores entre 1 y 1,19), 0,08 es el factor de exigencia de capital, APRC son los activos ponderados por riesgo de crédito (determinados mediante la suma de valores obtenidos aplicando ponderadores de riesgo a activos computables), e INC representa los incrementos normativos. Los activos ponderados por riesgo de crédito se calculan ponderando activos computables según factores de riesgo específicos. Respecto a la frecuencia de reporte, la información disponible en el grafo indica que las entidades deben reportar información de capital en el régimen informativo contable mensual del BCRA, aunque no se especifica explícitamente si el reporte de la exigencia de CRC es mensual, trimestral u otra periodicidad.",
  "citas": [
    {
      "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
      "location": "p.1-5 / Sección 3, punto 3.1.2"
    },
    {
      "source_doc": "TO_capitales_minimos_actual.pdf",
      "location": "p.107-111 / Punto 5.3.2.1 y siguientes"
    },
    {
      "source_doc": "TO_capitales_minimos_actual.pdf",
      "location": "p.155-157 / Punto 8.2.3.3"
    }
  ],
  "respondible": false
}
```
```

## 3b. Inventario de pasos (runtime vs. almacenado vs. re-ejecutado)

| paso | tool | input | chars runtime | chars almacenados | re-ejecutado |
|---|---|---|---|---|---|
| 1 | buscar_nodos | `{"consulta": "exigencia capital riesgo crédito CRC", "limite": 10}` | 3644 | 1215 | = runtime ✓ |
| 2 | buscar_nodos | `{"consulta": "capital riesgo crédito cálculo", "limite": 10}` | 3496 | 1215 | = runtime ✓ |
| 3 | buscar_nodos | `{"consulta": "reporte capital BCRA frecuencia", "limite": 10}` | 2837 | 1215 | = runtime ✓ |
| 4 | ver_nodo | `{"id": "exigencia_por_riesgo_de_credito"}` | 835 | 835 | = runtime ✓ |
| 5 | ver_nodo | `{"id": "cobertura_del_riesgo_de_credito_crc"}` | 618 | 618 | = runtime ✓ |
| 6 | ver_vecinos | `{"id": "exigencia_por_riesgo_de_credito", "direccion": "salientes"}` | 739 | 739 | = runtime ✓ |
| 7 | buscar_nodos | `{"consulta": "activos ponderados riesgo crédito APR", "limite": 10}` | 3210 | 1215 | = runtime ✓ |
| 8 | ver_nodo | `{"id": "activos_ponderados_por_riesgo_de_credito"}` | 878 | 878 | = runtime ✓ |
| 9 | buscar_nodos | `{"consulta": "reporte mensual capital exigencia", "limite": 10}` | 3231 | 1215 | = runtime ✓ |
| 10 | buscar_nodos | `{"consulta": "régimen informativo contable mensual", "limite": 10}` | 3227 | 1215 | = runtime ✓ |
| 11 | buscar_nodos | `{"consulta": "8% activos ponderados riesgo", "limite": 10}` | 3262 | 1215 | = runtime ✓ |
| 12 | ver_nodo | `{"id": "activos_ponderados_por_riesgo"}` | 1226 | 1213 | = runtime ✓ |
| 13 | buscar_nodos | `{"consulta": "periodicidad reporte mensual trimestral capital", "limite": 10}` | 2866 | 1215 | = runtime ✓ |
| 14 | buscar_nodos | `{"consulta": "CRC 8% APRc factor calificación", "limite": 10}` | 2894 | 1215 | = runtime ✓ |
| 15 | ver_vecinos | `{"id": "factor_de_calificacion_de_entidad", "direccion": "salientes"}` | 183 | 183 | = runtime ✓ |

**Fidelidad runtime↔re-ejecución: 15/15 pasos con largo idéntico.**

## 3c. APÉNDICE — outputs completos re-ejecutados (15 pasos)


--- paso 1 · buscar_nodos · input={"consulta": "exigencia capital riesgo crédito CRC", "limite": 10} · runtime=3644 · re-ejecutado=3644 ---

```json
{
 "consulta": "exigencia capital riesgo crédito CRC",
 "total_con_match": 314,
 "resultados": [
  {
   "id": "disminucion_de_exigencia_de_capital_minimo_por_riesgo_de_credito",
   "type": "concepto_de_facilidad_regulatoria",
   "label": "Disminución de exigencia de capital mínimo por riesgo de crédito",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Facilidad otorgada por el BCRA que reduce la exigencia de capital mínimo asociada al riesgo de crédito."
  },
  {
   "id": "promedio_de_36_meses_de_exigencia_de_capital_por_riesgo_de_credito",
   "type": "parametro_regulatorio",
   "label": "Promedio de 36 meses de exigencia de capital por riesgo de crédito",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Promedio de los últimos 36 meses de exigencia de capital mínimo por riesgo de crédito, utilizado como base para límites máximos de exigencia operacional."
  },
  {
   "id": "exigencia_por_riesgo_de_credito",
   "type": "requisito_regulatorio_de_capital",
   "label": "Exigencia por riesgo de crédito",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Exigencia de capital que las entidades financieras deben mantener, calculada mediante una fórmula que considera activos ponderados por riesgo de crédito e incre…"
  },
  {
   "id": "cobertura_del_riesgo_de_credito_crc",
   "type": "mecanismo_regulatorio",
   "label": "Cobertura del riesgo de crédito (CRC)",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Mecanismo de cobertura del riesgo de crédito que ajusta el valor de la exposición mediante activos admitidos como garantía, sujeto a aforos regulatorios y requi…"
  },
  {
   "id": "exigencia_de_capital_por_riesgo_de_mercado",
   "type": "requisito_de_capital",
   "label": "Exigencia de capital por riesgo de mercado",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Suma aritmética de las exigencias de capital por riesgos de tasa de interés, acciones, tipo de cambio, productos básicos y opciones."
  },
  {
   "id": "exigencia_de_capital_por_riesgo_especifico",
   "type": "requisito_regulatorio",
   "label": "Exigencia de capital por riesgo específico",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Exigencia de capital calculada para posiciones de titulización, derivados de crédito y posiciones cubiertas, expresada como porcentaje del importe ponderado por…"
  },
  {
   "id": "exigencia_de_capital_por_riesgo_operacional",
   "type": "requisito_regulatorio",
   "label": "Exigencia de capital por riesgo operacional",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Requerimiento de capital que las entidades financieras deben mantener para cubrir riesgos operacionales, calculado mensualmente según fórmulas específicas para …"
  },
  {
   "id": "incrementos_de_exigencia_por_riesgo_de_credito",
   "type": "ajuste_regulatorio",
   "label": "Incrementos de exigencia por riesgo de crédito",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Incrementos a la exigencia de capitales mínimos por excesos en activos inmovilizados, grandes exposiciones, financiamiento al sector público, derivados no cubie…"
  },
  {
   "id": "exigencia_de_capital_por_riesgo_de_tipo_de_cambio",
   "type": "requisito_regulatorio",
   "label": "Exigencia de capital por riesgo de tipo de cambio",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Capital mínimo necesario para cubrir el riesgo de mantener posiciones en moneda extranjera, incluido el oro, calculado como el 8% de la posición neta total."
  },
  {
   "id": "exigencia_de_capital_por_riesgo_operacional_cro",
   "type": "requisito_de_capital",
   "label": "Exigencia de capital por riesgo operacional (CRO)",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Exigencia de capital determinada mensualmente para entidades del grupo 2, calculada aplicando una expresión que considera el ingreso bruto positivo de los últim…"
  }
 ]
}
```

--- paso 2 · buscar_nodos · input={"consulta": "capital riesgo crédito cálculo", "limite": 10} · runtime=3496 · re-ejecutado=3496 ---

```json
{
 "consulta": "capital riesgo crédito cálculo",
 "total_con_match": 308,
 "resultados": [
  {
   "id": "requerimiento_de_capital_por_riesgo_de_credito_de_contraparte",
   "type": "exigencia_regulatoria_de_capital",
   "label": "Requerimiento de capital por riesgo de crédito de contraparte",
   "tokens_matcheados": 3,
   "resumen_propiedades": "RCD equivalente a la suma de la exigencia correspondiente a la EAD vigente de todas las contrapartes y el requerimiento de capital por CVA."
  },
  {
   "id": "aumento_de_integracion_de_capital_minimo_por_riesgo_de_credito",
   "type": "concepto_de_facilidad_regulatoria",
   "label": "Aumento de integración de capital mínimo por riesgo de crédito",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Facilidad otorgada por el BCRA que incrementa la integración de capital mínimo requerido por riesgo de crédito."
  },
  {
   "id": "disminucion_de_exigencia_de_capital_minimo_por_riesgo_de_credito",
   "type": "concepto_de_facilidad_regulatoria",
   "label": "Disminución de exigencia de capital mínimo por riesgo de crédito",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Facilidad otorgada por el BCRA que reduce la exigencia de capital mínimo asociada al riesgo de crédito."
  },
  {
   "id": "promedio_de_36_meses_de_exigencia_de_capital_por_riesgo_de_credito",
   "type": "parametro_regulatorio",
   "label": "Promedio de 36 meses de exigencia de capital por riesgo de crédito",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Promedio de los últimos 36 meses de exigencia de capital mínimo por riesgo de crédito, utilizado como base para límites máximos de exigencia operacional."
  },
  {
   "id": "disminucion_del_defecto_de_integracion_de_capital_minimo_por_riesgo_de_credito_y_operacional",
   "type": "concepto_de_facilidad_regulatoria",
   "label": "Disminución del defecto de integración de capital mínimo por riesgo de crédito y operacional",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Facilidad otorgada por el BCRA que reduce el defecto de integración de capital mínimo por riesgos de crédito y operacional."
  },
  {
   "id": "riesgo_de_credito",
   "type": "tipo_de_riesgo",
   "label": "Riesgo de crédito",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Riesgo de incumplimiento de la contraparte en sus obligaciones financieras, sujeto a evaluación y ponderación."
  },
  {
   "id": "riesgo_de_credito_propio",
   "type": "ajuste_regulatorio",
   "label": "Riesgo de crédito propio",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Ajustes de valuación por el riesgo de crédito de la entidad financiera, deducibles de la RPC sin compensación con riesgo de crédito de contraparte."
  },
  {
   "id": "riesgo_de_credito_sustancial",
   "type": "tipo_de_riesgo",
   "label": "Riesgo de crédito sustancial",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Riesgo evidenciado por entidades financieras prestatarias cuya capacidad de pago está supeditada a coyuntura económica o condiciones de negocio favorables o est…"
  },
  {
   "id": "cobertura_de_riesgo_de_credito",
   "type": "mecanismo_regulatorio",
   "label": "Cobertura de riesgo de crédito",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Conjunto de métodos y requisitos para reconocer garantías, contragarantías y derivados de crédito que reducen la exigencia de capital por riesgo de crédito."
  },
  {
   "id": "cobertura_del_riesgo_de_credito",
   "type": "mecanismo_de_mitigacion",
   "label": "Cobertura del riesgo de crédito",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Mejora crediticia que ya se encuentra reflejada en la calificación específica de la emisión, cuyo efecto no debe computarse doblemente."
  }
 ]
}
```

--- paso 3 · buscar_nodos · input={"consulta": "reporte capital BCRA frecuencia", "limite": 10} · runtime=2837 · re-ejecutado=2837 ---

```json
{
 "consulta": "reporte capital BCRA frecuencia",
 "total_con_match": 136,
 "resultados": [
  {
   "id": "bcra",
   "type": "autoridad_regulatoria",
   "label": "BCRA",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Banco Central de la República Argentina, autoridad que regula el mercado de cambios, publica cotizaciones de referencia, y otorga conformidad previa para cierta…"
  },
  {
   "id": "capital_minimo",
   "type": "requisito_regulatorio",
   "label": "Capital mínimo",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Exigencia de capital que las entidades financieras deben tener integrada, equivalente al mayor valor entre la exigencia básica y la suma de las determinadas por…"
  },
  {
   "id": "capital_social",
   "type": "rubro_patrimonial",
   "label": "Capital social",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Rubro del patrimonio neto que forma parte del capital ordinario de nivel uno, excluyendo acciones con preferencia patrimonial."
  },
  {
   "id": "capital_vencido",
   "type": "obligacion_financiera",
   "label": "Capital vencido",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Capital vencido de deudas financieras con contrapartes vinculadas, elegible para suscripción de bonos BOPREAL."
  },
  {
   "id": "bienes_de_capital",
   "type": "categoria_de_bien",
   "label": "Bienes de capital",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Bienes clasificados como BK (Bien de Capital) en la Nomenclatura Común del MERCOSUR, con plazo de 270 días corridos para demostrar registro de ingreso aduanero."
  },
  {
   "id": "capital_economico",
   "type": "concepto_regulatorio",
   "label": "Capital económico",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Evaluación del capital necesario para cubrir riesgos, que debe ser consistente con los análisis de debida diligencia."
  },
  {
   "id": "medida_del_capital",
   "type": "componente_de_ratio",
   "label": "Medida del capital",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Componente del ratio de apalancamiento calculado como PNb (CN1) según códigos 70210000, 70220000, 70230000 y 70240000."
  },
  {
   "id": "reporte_trimestral",
   "type": "documento_obligatorio",
   "label": "Reporte trimestral",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Reporte que debe elaborar y elevar el responsable de atención al usuario con periodicidad mínima trimestral, conteniendo información sobre consultas, reclamos, …"
  },
  {
   "id": "notificacion_al_bcra",
   "type": "procedimiento_administrativo",
   "label": "Notificación al BCRA",
   "tokens_matcheados": 1,
   "resumen_propiedades": "La entidad nominada por un exportador debe notificar al BCRA mediante nota dirigida a la Gerencia Principal de Exterior y Cambios dentro de los 30 días corridos…"
  },
  {
   "id": "reduccion_de_capital",
   "type": "operacion_corporativa",
   "label": "Reducción de capital",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Mecanismo legal mediante el cual se reduce el capital de una empresa local."
  }
 ]
}
```

--- paso 4 · ver_nodo · input={"id": "exigencia_por_riesgo_de_credito"} · runtime=835 · re-ejecutado=835 ---

```json
{
 "id": "exigencia_por_riesgo_de_credito",
 "type": "requisito_regulatorio_de_capital",
 "label": "Exigencia por riesgo de crédito",
 "properties": {
  "description": "Exigencia de capital que las entidades financieras deben mantener, calculada mediante una fórmula que considera activos ponderados por riesgo de crédito e incrementos normativos.",
  "version": "vigente",
  "type_raw": [
   "Requisito regulatorio de capital",
   "Componente de Exigencia de Capital"
  ],
  "type_raw_counts": {
   "Requisito regulatorio de capital": 1,
   "Componente de Exigencia de Capital": 1
  },
  "name_variants": [],
  "n_observations": 2
 },
 "provenances": [
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "p.1-5 / Sección 3, punto 3.1.2"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "p.31-35 / Sección 7.1"
  }
 ]
}
```

--- paso 5 · ver_nodo · input={"id": "cobertura_del_riesgo_de_credito_crc"} · runtime=618 · re-ejecutado=618 ---

```json
{
 "id": "cobertura_del_riesgo_de_credito_crc",
 "type": "mecanismo_regulatorio",
 "label": "Cobertura del riesgo de crédito (CRC)",
 "properties": {
  "description": "Mecanismo de cobertura del riesgo de crédito que ajusta el valor de la exposición mediante activos admitidos como garantía, sujeto a aforos regulatorios y requisitos de vencimiento.",
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
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.107-111 / Punto 5.3.2.1 y siguientes"
  }
 ]
}
```

--- paso 6 · ver_vecinos · input={"id": "exigencia_por_riesgo_de_credito", "direccion": "salientes"} · runtime=739 · re-ejecutado=739 ---

```json
{
 "id": "exigencia_por_riesgo_de_credito",
 "label": "Exigencia por riesgo de crédito",
 "n_salientes_total": 2,
 "n_entrantes_total": 2,
 "salientes": [
  {
   "relation": "se_calcula_mediante",
   "vecino_id": "activos_ponderados_por_riesgo_de_credito",
   "vecino_label": "Activos ponderados por riesgo de crédito",
   "provenances": [
    {
     "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
     "location": "p.1-5 / Sección 3, punto 3.1.2"
    }
   ]
  },
  {
   "relation": "utiliza_en_su_calculo",
   "vecino_id": "factor_de_calificacion_de_entidad",
   "vecino_label": "Factor de calificación de entidad",
   "provenances": [
    {
     "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
     "location": "p.1-5 / Sección 3, punto 3.1.2"
    }
   ]
  }
 ],
 "salientes_truncado": false
}
```

--- paso 7 · buscar_nodos · input={"consulta": "activos ponderados riesgo crédito APR", "limite": 10} · runtime=3210 · re-ejecutado=3210 ---

```json
{
 "consulta": "activos ponderados riesgo crédito APR",
 "total_con_match": 289,
 "resultados": [
  {
   "id": "activos_ponderados_por_riesgo_de_credito",
   "type": "componente_de_apr",
   "label": "Activos ponderados por riesgo de crédito",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Activos computables ponderados según factores de riesgo, utilizados en la fórmula de exigencia de capital por riesgo de crédito."
  },
  {
   "id": "activos_ponderados_por_riesgo_del_fondo_apr_fondo",
   "type": "metrica_de_capital",
   "label": "Activos ponderados por riesgo del fondo (APR fondo)",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Total de activos ponderados por riesgo del fondo calculado en función del LTA o MBA, utilizado para determinar ponderador de riesgo promedio."
  },
  {
   "id": "activos_ponderados_por_riesgo_de_la_inversion_apr_inversion",
   "type": "metrica_de_capital",
   "label": "Activos ponderados por riesgo de la inversión (APR inversión)",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Activos ponderados por riesgo atribuibles a la inversión de la entidad en un fondo, calculados como producto del ponderador promedio, apalancamiento e inversión…"
  },
  {
   "id": "activos_ponderados_por_riesgo",
   "type": "medida_de_riesgo",
   "label": "Activos ponderados por riesgo",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Resultado de aplicar la fórmula APR = APRc + [(RM+RO) x 12,5], donde APRc es activos ponderados por riesgo de crédito, RM es exigencia por riesgo de mercado y R…"
  },
  {
   "id": "activos_ponderados_por_riesgo_operacional",
   "type": "componente_de_capital",
   "label": "Activos ponderados por riesgo operacional",
   "tokens_matcheados": 3,
   "resumen_propiedades": "APR para riesgo operacional, iguales a 12,5 veces el CRO."
  },
  {
   "id": "riesgo_de_credito",
   "type": "tipo_de_riesgo",
   "label": "Riesgo de crédito",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Riesgo de incumplimiento de la contraparte en sus obligaciones financieras, sujeto a evaluación y ponderación."
  },
  {
   "id": "riesgo_de_credito_propio",
   "type": "ajuste_regulatorio",
   "label": "Riesgo de crédito propio",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Ajustes de valuación por el riesgo de crédito de la entidad financiera, deducibles de la RPC sin compensación con riesgo de crédito de contraparte."
  },
  {
   "id": "riesgo_de_credito_sustancial",
   "type": "tipo_de_riesgo",
   "label": "Riesgo de crédito sustancial",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Riesgo evidenciado por entidades financieras prestatarias cuya capacidad de pago está supeditada a coyuntura económica o condiciones de negocio favorables o est…"
  },
  {
   "id": "cobertura_de_riesgo_de_credito",
   "type": "mecanismo_regulatorio",
   "label": "Cobertura de riesgo de crédito",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Conjunto de métodos y requisitos para reconocer garantías, contragarantías y derivados de crédito que reducen la exigencia de capital por riesgo de crédito."
  },
  {
   "id": "cobertura_del_riesgo_de_credito",
   "type": "mecanismo_de_mitigacion",
   "label": "Cobertura del riesgo de crédito",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Mejora crediticia que ya se encuentra reflejada en la calificación específica de la emisión, cuyo efecto no debe computarse doblemente."
  }
 ]
}
```

--- paso 8 · ver_nodo · input={"id": "activos_ponderados_por_riesgo_de_credito"} · runtime=878 · re-ejecutado=878 ---

```json
{
 "id": "activos_ponderados_por_riesgo_de_credito",
 "type": "componente_de_apr",
 "label": "Activos ponderados por riesgo de crédito",
 "properties": {
  "description": "Activos computables ponderados según factores de riesgo, utilizados en la fórmula de exigencia de capital por riesgo de crédito.",
  "version": "vigente",
  "type_raw": [
   "Componente de cálculo regulatorio",
   "Métrica regulatoria",
   "Componente de APR"
  ],
  "type_raw_counts": {
   "Métrica regulatoria": 1,
   "Componente de APR": 1,
   "Componente de cálculo regulatorio": 1
  },
  "name_variants": [],
  "n_observations": 3
 },
 "provenances": [
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "p.1-5 / Sección 3, punto 3.1.2"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.155-157 / Punto 8.2.3.3"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.167-170 / Punto 8.5"
  }
 ]
}
```

--- paso 9 · buscar_nodos · input={"consulta": "reporte mensual capital exigencia", "limite": 10} · runtime=3231 · re-ejecutado=3231 ---

```json
{
 "consulta": "reporte mensual capital exigencia",
 "total_con_match": 138,
 "resultados": [
  {
   "id": "exigencia_basica_de_capital",
   "type": "requisito_regulatorio",
   "label": "Exigencia básica de capital",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Monto mínimo de capital que deben mantener las entidades financieras según su categoría, con vigencia desde el 01/01/25."
  },
  {
   "id": "factor_de_exigencia_de_capital_8",
   "type": "factor_regulatorio",
   "label": "Factor de exigencia de capital 8%",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Factor aplicable a operaciones DvP fallidas entre 5 y 15 días hábiles posteriores a la fecha de liquidación acordada."
  },
  {
   "id": "factor_de_exigencia_de_capital_50",
   "type": "factor_regulatorio",
   "label": "Factor de exigencia de capital 50%",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Factor aplicable a operaciones DvP fallidas entre 16 y 30 días hábiles posteriores a la fecha de liquidación acordada."
  },
  {
   "id": "factor_de_exigencia_de_capital_75",
   "type": "factor_regulatorio",
   "label": "Factor de exigencia de capital 75%",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Factor aplicable a operaciones DvP fallidas entre 31 y 45 días hábiles posteriores a la fecha de liquidación acordada."
  },
  {
   "id": "factor_de_exigencia_de_capital_100",
   "type": "factor_regulatorio",
   "label": "Factor de exigencia de capital 100%",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Factor aplicable a operaciones DvP fallidas 46 o más días hábiles posteriores a la fecha de liquidación acordada."
  },
  {
   "id": "activos_sujetos_a_exigencia_de_capital",
   "type": "categoria_de_activos",
   "label": "Activos sujetos a exigencia de capital",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Suma de posiciones compradas y vendidas de activos comprendidos en la exigencia de capital mínimo por riesgo de mercado."
  },
  {
   "id": "exigencia_de_capital_por_riesgo_de_mercado",
   "type": "requisito_de_capital",
   "label": "Exigencia de capital por riesgo de mercado",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Suma aritmética de las exigencias de capital por riesgos de tasa de interés, acciones, tipo de cambio, productos básicos y opciones."
  },
  {
   "id": "exigencia_de_capital_por_riesgo_especifico",
   "type": "requisito_regulatorio",
   "label": "Exigencia de capital por riesgo específico",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Exigencia de capital calculada para posiciones de titulización, derivados de crédito y posiciones cubiertas, expresada como porcentaje del importe ponderado por…"
  },
  {
   "id": "exigencia_de_capital_por_riesgo_operacional",
   "type": "requisito_regulatorio",
   "label": "Exigencia de capital por riesgo operacional",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Requerimiento de capital que las entidades financieras deben mantener para cubrir riesgos operacionales, calculado mensualmente según fórmulas específicas para …"
  },
  {
   "id": "exigencia_de_capital_por_riesgo_de_tipo_de_cambio",
   "type": "requisito_regulatorio",
   "label": "Exigencia de capital por riesgo de tipo de cambio",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Capital mínimo necesario para cubrir el riesgo de mantener posiciones en moneda extranjera, incluido el oro, calculado como el 8% de la posición neta total."
  }
 ]
}
```

--- paso 10 · buscar_nodos · input={"consulta": "régimen informativo contable mensual", "limite": 10} · runtime=3227 · re-ejecutado=3227 ---

```json
{
 "consulta": "régimen informativo contable mensual",
 "total_con_match": 57,
 "resultados": [
  {
   "id": "regimen_informativo_del_bcra",
   "type": "requisito_regulatorio",
   "label": "Régimen informativo del BCRA",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Conjunto de disposiciones que las entidades deben cumplir en relación con el seguimiento de anticipos y financiaciones de exportación."
  },
  {
   "id": "regimen_informativo_de_operaciones_cambiarias",
   "type": "requisito_regulatorio",
   "label": "Régimen informativo de operaciones cambiarias",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Sistema de validación y reporte de operaciones cambiarias ante el BCRA, cuyo incumplimiento por más de 4 días hábiles genera suspensión de operaciones."
  },
  {
   "id": "regimen_informativo_de_operaciones_de_cambios",
   "type": "sistema_informatico_regulatorio",
   "label": "Régimen Informativo de Operaciones de Cambios",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Régimen mediante el cual se reportan operaciones de cambio y del cual surgen datos asociados a pagos de importación incorporados al SEPAIMPO."
  },
  {
   "id": "regimen_informativo_de_operaciones_de_cambio_rioc",
   "type": "mecanismo_de_registro",
   "label": "Régimen informativo de operaciones de cambio (RIOC)",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Sistema ante el BCRA mediante el cual la entidad financiera registra la financiación una vez verificado el registro de ingreso aduanero de los bienes."
  },
  {
   "id": "regimen_informativo_de_operaciones_de_cambios_rioc",
   "type": "sistema_de_registro",
   "label": "Régimen informativo de operaciones de cambios (RIOC)",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Sistema a través del cual las entidades financieras deben registrar operaciones de seguimiento de anticipos y otras financiaciones de exportación de bienes ante…"
  },
  {
   "id": "balance_mensual",
   "type": "documento_regulatorio",
   "label": "Balance mensual",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Balance mensual cuya fecha de presentación obligatoria al BCRA determina cuándo debe estar presentado el estado financiero trimestral o anual con informe del au…"
  },
  {
   "id": "regimen_de_rancho",
   "type": "regimen_aduanero_exceptuado",
   "label": "Régimen de rancho",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Régimen aduanero exceptuado del seguimiento conforme a los artículos 506 al 516 de la Ley 22.415, aplicable a medios de transporte de bandera nacional."
  },
  {
   "id": "consolidado_mensual",
   "type": "tipo_de_entidad_financiera",
   "label": "Consolidado mensual",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Entidad financiera con filiales y subsidiarias significativas en el país y en el exterior que reporta consolidación mensual, identificada con códigos 2 o 9."
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
  }
 ]
}
```

--- paso 11 · buscar_nodos · input={"consulta": "8% activos ponderados riesgo", "limite": 10} · runtime=3262 · re-ejecutado=3262 ---

```json
{
 "consulta": "8% activos ponderados riesgo",
 "total_con_match": 203,
 "resultados": [
  {
   "id": "activos_ponderados_por_riesgo",
   "type": "medida_de_riesgo",
   "label": "Activos ponderados por riesgo",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Resultado de aplicar la fórmula APR = APRc + [(RM+RO) x 12,5], donde APRc es activos ponderados por riesgo de crédito, RM es exigencia por riesgo de mercado y R…"
  },
  {
   "id": "activos_ponderados_por_riesgo_de_credito",
   "type": "componente_de_apr",
   "label": "Activos ponderados por riesgo de crédito",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Activos computables ponderados según factores de riesgo, utilizados en la fórmula de exigencia de capital por riesgo de crédito."
  },
  {
   "id": "activos_ponderados_por_riesgo_operacional",
   "type": "componente_de_capital",
   "label": "Activos ponderados por riesgo operacional",
   "tokens_matcheados": 3,
   "resumen_propiedades": "APR para riesgo operacional, iguales a 12,5 veces el CRO."
  },
  {
   "id": "activos_ponderados_por_riesgo_del_fondo_apr_fondo",
   "type": "metrica_de_capital",
   "label": "Activos ponderados por riesgo del fondo (APR fondo)",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Total de activos ponderados por riesgo del fondo calculado en función del LTA o MBA, utilizado para determinar ponderador de riesgo promedio."
  },
  {
   "id": "activos_ponderados_por_riesgo_de_la_inversion_apr_inversion",
   "type": "metrica_de_capital",
   "label": "Activos ponderados por riesgo de la inversión (APR inversión)",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Activos ponderados por riesgo atribuibles a la inversión de la entidad en un fondo, calculados como producto del ponderador promedio, apalancamiento e inversión…"
  },
  {
   "id": "posicion_neta_vendedora_de_activos_financieros_no_sujetos_a_riesgo_de_mercado",
   "type": "categoria_de_pasivo",
   "label": "Posición neta vendedora de activos financieros no sujetos a riesgo de mercado",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Posición neta vendedora de activos financieros que no están sujetos a riesgo de mercado."
  },
  {
   "id": "posicion_neta_compradora_de_activos_financieros_no_sujetos_a_riesgo_de_mercado",
   "type": "categoria_de_activo",
   "label": "Posición neta compradora de activos financieros no sujetos a riesgo de mercado",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Posición neta compradora de activos financieros que no están sujetos a riesgo de mercado."
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
  }
 ]
}
```

--- paso 12 · ver_nodo · input={"id": "activos_ponderados_por_riesgo"} · runtime=1226 · re-ejecutado=1226 ---

```json
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
```

--- paso 13 · buscar_nodos · input={"consulta": "periodicidad reporte mensual trimestral capital", "limite": 10} · runtime=2866 · re-ejecutado=2866 ---

```json
{
 "consulta": "periodicidad reporte mensual trimestral capital",
 "total_con_match": 125,
 "resultados": [
  {
   "id": "reporte_trimestral",
   "type": "documento_obligatorio",
   "label": "Reporte trimestral",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Reporte que debe elaborar y elevar el responsable de atención al usuario con periodicidad mínima trimestral, conteniendo información sobre consultas, reclamos, …"
  },
  {
   "id": "capital_minimo",
   "type": "requisito_regulatorio",
   "label": "Capital mínimo",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Exigencia de capital que las entidades financieras deben tener integrada, equivalente al mayor valor entre la exigencia básica y la suma de las determinadas por…"
  },
  {
   "id": "capital_social",
   "type": "rubro_patrimonial",
   "label": "Capital social",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Rubro del patrimonio neto que forma parte del capital ordinario de nivel uno, excluyendo acciones con preferencia patrimonial."
  },
  {
   "id": "balance_mensual",
   "type": "documento_regulatorio",
   "label": "Balance mensual",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Balance mensual cuya fecha de presentación obligatoria al BCRA determina cuándo debe estar presentado el estado financiero trimestral o anual con informe del au…"
  },
  {
   "id": "capital_vencido",
   "type": "obligacion_financiera",
   "label": "Capital vencido",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Capital vencido de deudas financieras con contrapartes vinculadas, elegible para suscripción de bonos BOPREAL."
  },
  {
   "id": "bienes_de_capital",
   "type": "categoria_de_bien",
   "label": "Bienes de capital",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Bienes clasificados como BK (Bien de Capital) en la Nomenclatura Común del MERCOSUR, con plazo de 270 días corridos para demostrar registro de ingreso aduanero."
  },
  {
   "id": "capital_economico",
   "type": "concepto_regulatorio",
   "label": "Capital económico",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Evaluación del capital necesario para cubrir riesgos, que debe ser consistente con los análisis de debida diligencia."
  },
  {
   "id": "medida_del_capital",
   "type": "componente_de_ratio",
   "label": "Medida del capital",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Componente del ratio de apalancamiento calculado como PNb (CN1) según códigos 70210000, 70220000, 70230000 y 70240000."
  },
  {
   "id": "consolidado_mensual",
   "type": "tipo_de_entidad_financiera",
   "label": "Consolidado mensual",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Entidad financiera con filiales y subsidiarias significativas en el país y en el exterior que reporta consolidación mensual, identificada con códigos 2 o 9."
  },
  {
   "id": "reduccion_de_capital",
   "type": "operacion_corporativa",
   "label": "Reducción de capital",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Mecanismo legal mediante el cual se reduce el capital de una empresa local."
  }
 ]
}
```

--- paso 14 · buscar_nodos · input={"consulta": "CRC 8% APRc factor calificación", "limite": 10} · runtime=2894 · re-ejecutado=2894 ---

```json
{
 "consulta": "CRC 8% APRc factor calificación",
 "total_con_match": 41,
 "resultados": [
  {
   "id": "factor_de_calificacion_de_entidad",
   "type": "parametro_de_calculo",
   "label": "Factor de calificación de entidad",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Factor k vinculado a la calificación asignada a la entidad según escala prevista en normas sobre capitales mínimos, utilizado en el cálculo de exigencia por rie…"
  },
  {
   "id": "factor_de_exigencia_de_capital_8",
   "type": "factor_regulatorio",
   "label": "Factor de exigencia de capital 8%",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Factor aplicable a operaciones DvP fallidas entre 5 y 15 días hábiles posteriores a la fecha de liquidación acordada."
  },
  {
   "id": "crc",
   "type": "exigencia_de_capital",
   "label": "CRC",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Exigencia de capital por riesgo de crédito, determinada mediante la fórmula CRC = (k x 0,08 x APRC) + INC."
  },
  {
   "id": "aprc",
   "type": "componente_de_calculo_de_capital",
   "label": "APRC",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Activos ponderados por riesgo de crédito, determinados mediante suma de valores obtenidos aplicando ponderadores de riesgo a activos computables, partidas fuera…"
  },
  {
   "id": "factor_k",
   "type": "componente_de_calculo_de_capital",
   "label": "Factor k",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Factor vinculado a la calificación asignada a la entidad según la evaluación efectuada por la SEFYC, con valores que varían de 1 a 1,19 según la calificación (1…"
  },
  {
   "id": "factor_de_1_15",
   "type": "parametro_de_calculo",
   "label": "Factor de 1,15",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Factor conservador aplicado al valor nocional cuando no se conoce ni el costo de reposición ni el factor de exposición potencial futura."
  },
  {
   "id": "calificacion_sefyc",
   "type": "evaluacion_regulatoria",
   "label": "Calificación SEFYC",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Calificación otorgada por la SEFYC en inspección respecto de la entidad, sistemas informáticos y responsables de evaluación de control interno."
  },
  {
   "id": "factor_regulatorio",
   "type": "parametro_de_riesgo",
   "label": "Factor regulatorio",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Multiplicador idéntico para todos los conjuntos de cobertura de tipo de cambio, aplicado al valor absoluto del nocional efectivo para obtener el adicional."
  },
  {
   "id": "factor_de_volatilidad",
   "type": "parametro_de_calculo",
   "label": "Factor de volatilidad",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Factor que refleja la volatilidad aplicado a cada nocional efectivo."
  },
  {
   "id": "calificacion_crediticia",
   "type": "atributo_de_entidad",
   "label": "Calificación crediticia",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Evaluación efectuada por una ECAI elegible que determina el ponderador de riesgo de una exposición, debiendo ser calificación global (internacional)."
  }
 ]
}
```

--- paso 15 · ver_vecinos · input={"id": "factor_de_calificacion_de_entidad", "direccion": "salientes"} · runtime=183 · re-ejecutado=183 ---

```json
{
 "id": "factor_de_calificacion_de_entidad",
 "label": "Factor de calificación de entidad",
 "n_salientes_total": 0,
 "n_entrantes_total": 2,
 "salientes": [],
 "salientes_truncado": false
}
```
