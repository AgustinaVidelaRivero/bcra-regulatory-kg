# Expediente validación — parte 2: trayectorias run_2 (sección 3 + apéndices)


---

# Sección 3 — run_2/CQ-015

## 3a. Respuesta final del agente (verbatim, `posthoc_run/traces/off/run_2/CQ-015.json`)

`trace.final_json`:

```json
{
 "respuesta": "A los fines cambiarios, una persona humana se define como 'residente' del país cuando tiene su centro de interés económico o actividad principal dentro del país, o cuando tiene la intención de permanecer en el país por al menos un año.",
 "citas": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 5 > Punto 6.4"
  }
 ],
 "respondible": true
}
```

`trace.final_raw` (turno final íntegro):

```
Tengo la respuesta completa. Basándome en la información del Knowledge Graph:

```json
{
  "respuesta": "A los fines cambiarios, una persona humana se define como 'residente' del país cuando tiene su centro de interés económico o actividad principal dentro del país, o cuando tiene la intención de permanecer en el país por al menos un año.",
  "citas": [
    {
      "source_doc": "TO_exterior_cambios_actual.pdf",
      "location": "Sección 5 > Punto 6.4"
    }
  ],
  "respondible": true
}
```
```

## 3b. Inventario de pasos (runtime vs. almacenado vs. re-ejecutado)

| paso | tool | input | chars runtime | chars almacenados | re-ejecutado |
|---|---|---|---|---|---|
| 1 | buscar_nodos | `{"consulta": "residente fines cambiarios definición", "limite": 10}` | 2919 | 1215 | = runtime ✓ |
| 2 | buscar_nodos | `{"consulta": "persona humana residente país", "limite": 10}` | 3388 | 1215 | = runtime ✓ |
| 3 | ver_nodo | `{"id": "concepto_definido:residente_persona_humana"}` | 425 | 425 | = runtime ✓ |
| 4 | ver_vecinos | `{"id": "concepto_definido:residente_persona_humana", "direccion": "ambas"}` | 230 | 230 | = runtime ✓ |

**Fidelidad runtime↔re-ejecución: 4/4 pasos con largo idéntico.**

## 3c. APÉNDICE — outputs completos re-ejecutados (4 pasos)


--- paso 1 · buscar_nodos · input={"consulta": "residente fines cambiarios definición", "limite": 10} · runtime=2919 · re-ejecutado=2919 ---

```json
{
 "consulta": "residente fines cambiarios definición",
 "total_con_match": 39,
 "resultados": [
  {
   "id": "sujeto_regulado:residente",
   "type": "SujetoRegulado",
   "label": "residente",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Persona física o jurídica residente sujeta a las obligaciones de cambios."
  },
  {
   "id": "sujeto_regulado:cliente_residente",
   "type": "SujetoRegulado",
   "label": "cliente residente",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Empresa residente que puede suscribir bonos BOPREAL por utilidades y dividendos pendientes de pago."
  },
  {
   "id": "sujeto_regulado:deudor_no_residente",
   "type": "SujetoRegulado",
   "label": "deudor no residente",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Persona o entidad no residente que debe pagar el crédito al exportador."
  },
  {
   "id": "sujeto_regulado:cliente_no_residente",
   "type": "SujetoRegulado",
   "label": "cliente no residente",
   "tokens_matcheados": 1,
   "resumen_propiedades": "['Cliente no residente que puede suscribir bonos BOPREAL por utilidades y dividendos cobrados desde 01/09/19.', 'Persona física o jurídica no residente que part…"
  },
  {
   "id": "sujeto_regulado:exportador_residente",
   "type": "SujetoRegulado",
   "label": "exportador residente",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Persona residente con endeudamientos financieros que puede solicitar prórroga en plazo de liquidación de divisas."
  },
  {
   "id": "concepto_definido:accionista_no_residente",
   "type": "ConceptoDefinido",
   "label": "accionista no residente",
   "tokens_matcheados": 1,
   "resumen_propiedades": "['Accionista que no reside en el país y que recibe distribuciones de utilidades y dividendos.', 'Persona que posee participación accionaria en un VPU y no resid…"
  },
  {
   "id": "sujeto_regulado:accionista_no_residente",
   "type": "SujetoRegulado",
   "label": "accionista no residente",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Persona física o jurídica que posee acciones y no reside en el país, beneficiaria de utilidades y dividendos pendientes de pago."
  },
  {
   "id": "sujeto_regulado:persona_humana_residente",
   "type": "SujetoRegulado",
   "label": "persona humana residente",
   "tokens_matcheados": 1,
   "resumen_propiedades": "['Cliente persona física residente que realiza la compra de moneda extranjera.', 'Persona natural residente que actúa en carácter de apoderado de un no resident…"
  },
  {
   "id": "concepto_definido:residente_persona_humana",
   "type": "ConceptoDefinido",
   "label": "residente: persona humana",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Persona humana con centro de interés económico o actividad principal dentro de un país, o con intención de permanecer por al menos un año."
  },
  {
   "id": "concepto_definido:persona_humana_no_residente",
   "type": "ConceptoDefinido",
   "label": "persona humana no residente",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Persona que no reside en el país, identificable mediante pasaporte u otro documento habilitante para ingreso al país."
  }
 ]
}
```

--- paso 2 · buscar_nodos · input={"consulta": "persona humana residente país", "limite": 10} · runtime=3388 · re-ejecutado=3388 ---

```json
{
 "consulta": "persona humana residente país",
 "total_con_match": 75,
 "resultados": [
  {
   "id": "sujeto_regulado:persona_humana_residente",
   "type": "SujetoRegulado",
   "label": "persona humana residente",
   "tokens_matcheados": 3,
   "resumen_propiedades": "['Cliente persona física residente que realiza la compra de moneda extranjera.', 'Persona natural residente que actúa en carácter de apoderado de un no resident…"
  },
  {
   "id": "concepto_definido:residente_persona_humana",
   "type": "ConceptoDefinido",
   "label": "residente: persona humana",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Persona humana con centro de interés económico o actividad principal dentro de un país, o con intención de permanecer por al menos un año."
  },
  {
   "id": "concepto_definido:persona_humana_no_residente",
   "type": "ConceptoDefinido",
   "label": "persona humana no residente",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Persona que no reside en el país, identificable mediante pasaporte u otro documento habilitante para ingreso al país."
  },
  {
   "id": "sujeto_regulado:cliente_no_persona_humana_residente",
   "type": "SujetoRegulado",
   "label": "cliente no persona humana residente",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Cliente que no es una persona humana residente y requiere conformidad previa del BCRA o declaración jurada para acceder al mercado de cambios."
  },
  {
   "id": "obligacion:consignar_cuit_o_cuil_de_persona_humana_residente_apoderada",
   "type": "Obligacion",
   "label": "consignar CUIT o CUIL de persona humana residente apoderada",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Cuando una persona humana residente actúa como apoderado de un no residente en operaciones de cambios, debe consignarse su CUIT o CUIL en el registro de la oper…"
  },
  {
   "id": "concepto_definido:residente_persona_juridica",
   "type": "ConceptoDefinido",
   "label": "residente: persona jurídica",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Persona jurídica constituida en un país, o sucursal de persona jurídica extranjera inscripta para realizar actividades de manera habitual en el país."
  },
  {
   "id": "requisito:factura_emitida_en_pais_por_residente",
   "type": "Requisito",
   "label": "factura emitida en país por residente",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Factura emitida en el país por la persona humana o jurídica residente que figura como comprador, con cantidad, descripción, precio unitario y total."
  },
  {
   "id": "sujeto_regulado:persona_humana_o_juridica_clasificada_como_mipyme",
   "type": "SujetoRegulado",
   "label": "persona humana o jurídica clasificada como MiPyMe",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Persona física o jurídica que clasifica como micro, pequeña o mediana empresa según normas de determinación de condición MiPyMe."
  },
  {
   "id": "sujeto_regulado:persona_humana_o_persona_juridica_clasificada_como_mipyme",
   "type": "SujetoRegulado",
   "label": "persona humana o persona jurídica clasificada como MiPyMe",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Persona humana o persona jurídica que clasifica como MiPyMe según normas aplicables."
  },
  {
   "id": "requisito:acuerdo_entre_persona_juridica_residente_y_empresa_del_exterior",
   "type": "Requisito",
   "label": "acuerdo entre persona jurídica residente y empresa del exterior",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Debe existir un acuerdo que autorice a la persona jurídica residente a actuar como agente de pago en Argentina."
  }
 ]
}
```

--- paso 3 · ver_nodo · input={"id": "concepto_definido:residente_persona_humana"} · runtime=425 · re-ejecutado=425 ---

```json
{
 "id": "concepto_definido:residente_persona_humana",
 "type": "ConceptoDefinido",
 "label": "residente: persona humana",
 "properties": {
  "description": "Persona humana con centro de interés económico o actividad principal dentro de un país, o con intención de permanecer por al menos un año.",
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 5 > Punto 6.4"
  }
 ]
}
```

--- paso 4 · ver_vecinos · input={"id": "concepto_definido:residente_persona_humana", "direccion": "ambas"} · runtime=230 · re-ejecutado=230 ---

```json
{
 "id": "concepto_definido:residente_persona_humana",
 "label": "residente: persona humana",
 "n_salientes_total": 0,
 "n_entrantes_total": 0,
 "salientes": [],
 "salientes_truncado": false,
 "entrantes": [],
 "entrantes_truncado": false
}
```

---

# Sección 3 — run_2/CQ-018

## 3a. Respuesta final del agente (verbatim, `posthoc_run/traces/off/run_2/CQ-018.json`)

`trace.final_json`:

```json
{
 "respuesta": "Los proveedores no financieros de crédito deben cumplir tanto con obligaciones de Protección al Usuario como con obligaciones de clasificación de deudores. Específicamente, están obligados a: (1) cumplir con normas de protección de usuarios, (2) considerar y resolver fundadamente reclamos de usuarios, y (3) clasificar deudores según mora en cartera de consumo/vivienda.\n\nLas empresas no financieras emisoras de tarjetas de crédito, por su parte, deben cumplir con obligaciones de Protección al Usuario (cumplimiento de normas de protección, resolución de reclamos, entrega de información sobre productos y servicios, publicación de contratos, etc.). Sin embargo, en la información disponible en el grafo no se encontró una obligación explícita de clasificación de deudores para estas empresas.\n\nRespecto a los criterios de clasificación de deudores, estos se basan en: (1) la capacidad de pago (criterio básico: la capacidad de pago en el futuro de la deuda o de los compromisos objeto de la garantía, medida a través del análisis de flujo de fondos), y (2) criterios objetivos que incluyen el término de morosidad, la situación jurídica del cliente o sus deudas, y el cumplimiento de refinanciaciones.",
 "citas": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 7 > Sección 7 — preámbulo"
  },
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "Sección 5 > Punto 1.1"
  },
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "Sección 3 > Sección 3 — preámbulo"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 3 > Punto 3.6"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 6 > Punto 5.1"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 6 > Punto 6.4"
  }
 ],
 "respondible": true
}
```

`trace.final_raw` (turno final íntegro):

```
```json
{
  "respuesta": "Los proveedores no financieros de crédito deben cumplir tanto con obligaciones de Protección al Usuario como con obligaciones de clasificación de deudores. Específicamente, están obligados a: (1) cumplir con normas de protección de usuarios, (2) considerar y resolver fundadamente reclamos de usuarios, y (3) clasificar deudores según mora en cartera de consumo/vivienda.\n\nLas empresas no financieras emisoras de tarjetas de crédito, por su parte, deben cumplir con obligaciones de Protección al Usuario (cumplimiento de normas de protección, resolución de reclamos, entrega de información sobre productos y servicios, publicación de contratos, etc.). Sin embargo, en la información disponible en el grafo no se encontró una obligación explícita de clasificación de deudores para estas empresas.\n\nRespecto a los criterios de clasificación de deudores, estos se basan en: (1) la capacidad de pago (criterio básico: la capacidad de pago en el futuro de la deuda o de los compromisos objeto de la garantía, medida a través del análisis de flujo de fondos), y (2) criterios objetivos que incluyen el término de morosidad, la situación jurídica del cliente o sus deudas, y el cumplimiento de refinanciaciones.",
  "citas": [
    {
      "source_doc": "TO_clasificacion_deudores_actual.pdf",
      "location": "Sección 7 > Sección 7 — preámbulo"
    },
    {
      "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
      "location": "Sección 5 > Punto 1.1"
    },
    {
      "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
      "location": "Sección 3 > Sección 3 — preámbulo"
    },
    {
      "source_doc": "TO_clasificacion_deudores_actual.pdf",
      "location": "Sección 3 > Punto 3.6"
    },
    {
      "source_doc": "TO_clasificacion_deudores_actual.pdf",
      "location": "Sección 6 > Punto 5.1"
    },
    {
      "source_doc": "TO_clasificacion_deudores_actual.pdf",
      "location": "Sección 6 > Punto 6.4"
    }
  ],
  "respondible": true
}
```
```

## 3b. Inventario de pasos (runtime vs. almacenado vs. re-ejecutado)

| paso | tool | input | chars runtime | chars almacenados | re-ejecutado |
|---|---|---|---|---|---|
| 1 | buscar_nodos | `{"consulta": "proveedores no financieros crédito", "limite": 10}` | 3516 | 1215 | = runtime ✓ |
| 2 | buscar_nodos | `{"consulta": "empresas no financieras emisoras tarjetas", "limite": 10}` | 3670 | 1215 | = runtime ✓ |
| 3 | buscar_nodos | `{"consulta": "clasificación deudores criterio", "limite": 10}` | 3514 | 1215 | = runtime ✓ |
| 4 | ver_nodo | `{"id": "sujeto_regulado:proveedores_no_financieros_de_credito"}` | 904 | 904 | = runtime ✓ |
| 5 | ver_nodo | `{"id": "sujeto_regulado:empresas_no_financieras_emisoras_de_tarjetas_de_credito"}` | 659 | 659 | = runtime ✓ |
| 6 | ver_nodo | `{"id": "concepto_definido:clasificacion_de_deudores"}` | 1003 | 1003 | = runtime ✓ |
| 7 | ver_vecinos | `{"id": "sujeto_regulado:proveedores_no_financieros_de_credito", "direccion": "salientes"}` | 1737 | 1214 | = runtime ✓ |
| 8 | ver_vecinos | `{"id": "sujeto_regulado:empresas_no_financieras_emisoras_de_tarjetas_de_credito", "direccion": "salientes"}` | 2837 | 1215 | = runtime ✓ |
| 9 | ver_nodo | `{"id": "obligacion:clasificar_deudores_segun_mora_en_cartera_consumo_vivienda"}` | 511 | 511 | = runtime ✓ |
| 10 | buscar_nodos | `{"consulta": "criterios clasificación deudores mora capacidad pago", "limite": 10}` | 3225 | 1215 | = runtime ✓ |
| 11 | ver_nodo | `{"id": "concepto_definido:criterios_objetivos_de_clasificacion"}` | 488 | 488 | = runtime ✓ |
| 12 | ver_nodo | `{"id": "concepto_definido:capacidad_de_pago"}` | 643 | 643 | = runtime ✓ |
| 13 | buscar_nodos | `{"consulta": "empresas no financieras tarjetas clasificación deudores obligación", "limite": 10}` | 3817 | 1215 | = runtime ✓ |
| 14 | buscar_nodos | `{"consulta": "sección 7 proveedores no financieros clasificación", "limite": 10}` | 3734 | 1215 | = runtime ✓ |
| 15 | ver_vecinos | `{"id": "sujeto_regulado:empresas_no_financieras_emisoras_de_tarjetas", "direccion": "salientes"}` | 1963 | 1214 | = runtime ✓ |

**Fidelidad runtime↔re-ejecución: 15/15 pasos con largo idéntico.**

## 3c. APÉNDICE — outputs completos re-ejecutados (15 pasos)


--- paso 1 · buscar_nodos · input={"consulta": "proveedores no financieros crédito", "limite": 10} · runtime=3516 · re-ejecutado=3516 ---

```json
{
 "consulta": "proveedores no financieros crédito",
 "total_con_match": 539,
 "resultados": [
  {
   "id": "sujeto_regulado:proveedores_no_financieros_de_credito",
   "type": "SujetoRegulado",
   "label": "proveedores no financieros de crédito",
   "tokens_matcheados": 4,
   "resumen_propiedades": "['Empresas no financieras emisoras de tarjetas de crédito y otros proveedores alcanzados por normas especiales.', 'Sujetos obligados alcanzados por normas sobre…"
  },
  {
   "id": "sujeto_regulado:otros_proveedores_no_financieros_de_credito",
   "type": "SujetoRegulado",
   "label": "otros proveedores no financieros de crédito",
   "tokens_matcheados": 4,
   "resumen_propiedades": "['Proveedores no financieros que otorgan crédito y deben cumplir obligaciones de divulgación de información.', 'Proveedores no financieros de crédito que ofrece…"
  },
  {
   "id": "norma_referenciada:normas_sobre_proveedores_no_financieros_de_credito",
   "type": "NormaReferenciada",
   "label": "normas sobre Proveedores no financieros de crédito",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Normas que regulan a los proveedores no financieros de crédito."
  },
  {
   "id": "concepto_definido:credito_no_calificado",
   "type": "ConceptoDefinido",
   "label": "crédito no calificado",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Exposición crediticia que no cuenta con calificación específica de ECAI y recibe ponderador estándar para no calificados."
  },
  {
   "id": "sujeto_regulado:proveedor_no_financiero_de_credito",
   "type": "SujetoRegulado",
   "label": "proveedor no financiero de crédito",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Proveedor no financiero de servicios de crédito sujeto a obligaciones de protección del usuario."
  },
  {
   "id": "concepto_definido:activos_no_financieros_no_producidos",
   "type": "ConceptoDefinido",
   "label": "activos no financieros no producidos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Transacciones de traspaso de activos intangibles como derechos de pesca, derechos minerales, espacio aéreo, pases de deportistas, patentes, derechos de autor, c…"
  },
  {
   "id": "operacion:enajenacion_de_activos_no_financieros_no_producidos",
   "type": "Operacion",
   "label": "enajenación de activos no financieros no producidos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "['Operación de venta o disposición de activos no financieros que no son producidos.', 'Operación de venta de activos no financieros no producidos por residentes…"
  },
  {
   "id": "sujeto_regulado:empresas_no_financieras_emisoras_de_tarjetas_de_credito",
   "type": "SujetoRegulado",
   "label": "empresas no financieras emisoras de tarjetas de crédito",
   "tokens_matcheados": 2,
   "resumen_propiedades": "['Sujetos obligados que emiten tarjetas de crédito y/o compra.', 'Empresas no financieras que emiten tarjetas de crédito y están sujetas a regulaciones de prote…"
  },
  {
   "id": "requisito:caracteristicas_basicas_no_desviantes_del_derivado_de_credito",
   "type": "Requisito",
   "label": "características básicas no desviantes del derivado de crédito",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Las características básicas del derivado de crédito como definiciones de eventos de crédito y mecanismos de liquidación no deben hacer que variaciones de precio…"
  },
  {
   "id": "obligacion:no_incorporar_dividendo_cupon_reajustable_por_riesgo_de_credito",
   "type": "Obligacion",
   "label": "no incorporar dividendo/cupón reajustable por riesgo de crédito",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Prohibición de dividendos o cupones que se reajusten periódicamente en función del riesgo de crédito de la entidad."
  }
 ]
}
```

--- paso 2 · buscar_nodos · input={"consulta": "empresas no financieras emisoras tarjetas", "limite": 10} · runtime=3670 · re-ejecutado=3670 ---

```json
{
 "consulta": "empresas no financieras emisoras tarjetas",
 "total_con_match": 403,
 "resultados": [
  {
   "id": "sujeto_regulado:empresas_no_financieras_emisoras_de_tarjetas",
   "type": "SujetoRegulado",
   "label": "empresas no financieras emisoras de tarjetas",
   "tokens_matcheados": 5,
   "resumen_propiedades": "['Empresas no financieras que emiten tarjetas de crédito y/o compra y están obligadas a informar comisiones.', 'Empresas no financieras emisoras de tarjetas de …"
  },
  {
   "id": "sujeto_regulado:empresas_no_financieras_emisoras_de_tarjetas_de_credito",
   "type": "SujetoRegulado",
   "label": "empresas no financieras emisoras de tarjetas de crédito",
   "tokens_matcheados": 5,
   "resumen_propiedades": "['Sujetos obligados que emiten tarjetas de crédito y/o compra.', 'Empresas no financieras que emiten tarjetas de crédito y están sujetas a regulaciones de prote…"
  },
  {
   "id": "sujeto_regulado:empresa_no_financiera_emisora_de_tarjetas",
   "type": "SujetoRegulado",
   "label": "empresa no financiera emisora de tarjetas",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Empresa no financiera que emite tarjetas de crédito y/o compra."
  },
  {
   "id": "requisito:empresa_no_controlante_de_entidades_financieras_locales",
   "type": "Requisito",
   "label": "empresa no controlante de entidades financieras locales",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La empresa en la cual se realiza la inversión directa no debe ser controlante de entidades financieras locales."
  },
  {
   "id": "requisito:fondos_no_provenientes_de_entidades_financieras_locales",
   "type": "Requisito",
   "label": "fondos no provenientes de entidades financieras locales",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Requisito de que la asistencia crediticia se otorgue con recursos que no provengan, directa o indirectamente, de entidades financieras locales."
  },
  {
   "id": "obligacion:tratamiento_de_ccp_no_calificadas_como_entidades_financieras",
   "type": "Obligacion",
   "label": "tratamiento de CCP no calificadas como entidades financieras",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Obligación de considerar a las CCP que no califican como entidades financieras para el cálculo de exigencias de capital por operaciones de negociación."
  },
  {
   "id": "operacion:cobros_por_consumo_en_pais_de_no_residentes_mediante_tarjetas",
   "type": "Operacion",
   "label": "cobros por consumo en país de no residentes mediante tarjetas",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Cobros por consumos en el país efectuados por no residentes mediante tarjetas de débito, crédito, compra o prepagas emitidas en el exterior."
  },
  {
   "id": "concepto_definido:empresa_que_no_sea_controlante_de_entidades_financieras_locales",
   "type": "ConceptoDefinido",
   "label": "empresa que no sea controlante de entidades financieras locales",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Clasificación de empresas residentes que no ejercen control sobre entidades financieras locales."
  },
  {
   "id": "obligacion:apertura_de_legajo_no_obligatoria_para_servicios_publicos_o_tarjetas",
   "type": "Obligacion",
   "label": "apertura de legajo no obligatoria para servicios públicos o tarjetas",
   "tokens_matcheados": 2,
   "resumen_propiedades": "En casos de deudores por servicios públicos o tarjetas de crédito no será obligatoria la apertura del legajo."
  },
  {
   "id": "obligacion:no_apertura_de_legajo_para_deudores_por_servicios_publicos_o_tarjetas_de_credito",
   "type": "Obligacion",
   "label": "no apertura de legajo para deudores por servicios públicos o tarjetas de crédito",
   "tokens_matcheados": 2,
   "resumen_propiedades": "No es obligatoria la apertura de legajo en casos de deudores por servicios públicos o tarjetas de crédito cedidos por deudores en concurso preventivo."
  }
 ]
}
```

--- paso 3 · buscar_nodos · input={"consulta": "clasificación deudores criterio", "limite": 10} · runtime=3514 · re-ejecutado=3514 ---

```json
{
 "consulta": "clasificación deudores criterio",
 "total_con_match": 76,
 "resultados": [
  {
   "id": "concepto_definido:clasificacion_de_deudores",
   "type": "ConceptoDefinido",
   "label": "clasificación de deudores",
   "tokens_matcheados": 2,
   "resumen_propiedades": "['Concepto central regulatorio que organiza la evaluación y categorización de la situación de los deudores.', 'Sistema de categorización de deudores según crite…"
  },
  {
   "id": "procedimiento:clasificacion_de_deudores",
   "type": "Procedimiento",
   "label": "clasificación de deudores",
   "tokens_matcheados": 2,
   "resumen_propiedades": "['Procedimiento de evaluación y clasificación de clientes según su capacidad de cumplimiento de compromisos financieros.', 'Proceso de asignación de categoría d…"
  },
  {
   "id": "procedimiento:tarea_de_clasificacion_de_deudores",
   "type": "Procedimiento",
   "label": "tarea de clasificación de deudores",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Procedimiento mediante el cual una entidad financiera asigna clasificaciones a sus clientes deudores."
  },
  {
   "id": "norma_referenciada:normas_sobre_clasificacion_de_deudores",
   "type": "NormaReferenciada",
   "label": "normas sobre Clasificación de deudores",
   "tokens_matcheados": 2,
   "resumen_propiedades": "['Normativa referenciada para la clasificación promedio de deudores en información de exposiciones subyacentes.', 'Normas externas que definen la clasificación …"
  },
  {
   "id": "concepto_definido:categorias_de_clasificacion_de_deudores",
   "type": "ConceptoDefinido",
   "label": "categorías de clasificación de deudores",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Categorías 1 a 5 utilizadas para clasificar a los deudores según su evaluación de riesgo."
  },
  {
   "id": "norma_referenciada:texto_ordenado_sobre_clasificacion_de_deudores",
   "type": "NormaReferenciada",
   "label": "Texto Ordenado sobre Clasificación de Deudores",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Norma externa que define situaciones de deudores y disposiciones sobre clasificación, referenciada en puntos 6.5.1 y 7.2.1."
  },
  {
   "id": "obligacion:clasificacion_y_prevision_de_deudores_excluidos",
   "type": "Obligacion",
   "label": "clasificación y previsión de deudores excluidos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Obligación de clasificar y prever deudores excluidos de las categorías especiales conforme a disposiciones de carácter general."
  },
  {
   "id": "obligacion:aprobacion_de_clasificacion_de_deudores_por_directorio",
   "type": "Obligacion",
   "label": "aprobación de clasificación de deudores por directorio",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La clasificación de deudores y cálculo de previsiones por riesgo de incobrabilidad debe contar con previa aprobación del Directorio o Consejo de Administración,…"
  },
  {
   "id": "obligacion:efectuar_clasificacion_de_deudores_con_periodicidad_adecuada",
   "type": "Obligacion",
   "label": "efectuar clasificación de deudores con periodicidad adecuada",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La clasificación de deudores debe efectuarse con periodicidad que atienda a su importancia, considerando la totalidad de financiaciones comprendidas, con docume…"
  },
  {
   "id": "obligacion:informar_a_sefyc_sobre_criterio_de_clasificacion_de_titulizacion",
   "type": "Obligacion",
   "label": "informar a SEFyC sobre criterio de clasificación de titulización",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Cuando exista incertidumbre sobre si una operación debe considerarse como titulización, la entidad deberá informar a la SEFyC los fundamentos del criterio aplic…"
  }
 ]
}
```

--- paso 4 · ver_nodo · input={"id": "sujeto_regulado:proveedores_no_financieros_de_credito"} · runtime=904 · re-ejecutado=904 ---

```json
{
 "id": "sujeto_regulado:proveedores_no_financieros_de_credito",
 "type": "SujetoRegulado",
 "label": "proveedores no financieros de crédito",
 "properties": {
  "description": [
   "Empresas no financieras emisoras de tarjetas de crédito y otros proveedores alcanzados por normas especiales.",
   "Sujetos obligados alcanzados por normas sobre proveedores no financieros de crédito, excepto asociaciones mutuales o cooperativas.",
   "Otros proveedores no financieros de crédito que atienden a usuarios de servicios financieros."
  ],
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 7 > Sección 7 — preámbulo"
  },
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "Sección 5 > Punto 1.1"
  },
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "Sección 3 > Sección 3 — preámbulo"
  }
 ]
}
```

--- paso 5 · ver_nodo · input={"id": "sujeto_regulado:empresas_no_financieras_emisoras_de_tarjetas_de_credito"} · runtime=659 · re-ejecutado=659 ---

```json
{
 "id": "sujeto_regulado:empresas_no_financieras_emisoras_de_tarjetas_de_credito",
 "type": "SujetoRegulado",
 "label": "empresas no financieras emisoras de tarjetas de crédito",
 "properties": {
  "description": [
   "Sujetos obligados que emiten tarjetas de crédito y/o compra.",
   "Empresas no financieras que emiten tarjetas de crédito y están sujetas a regulaciones de protección de usuarios."
  ],
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "Sección 5 > Punto 1.1"
  },
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "Sección 2 > Punto 2.4"
  }
 ]
}
```

--- paso 6 · ver_nodo · input={"id": "concepto_definido:clasificacion_de_deudores"} · runtime=1003 · re-ejecutado=1003 ---

```json
{
 "id": "concepto_definido:clasificacion_de_deudores",
 "type": "ConceptoDefinido",
 "label": "clasificación de deudores",
 "properties": {
  "description": [
   "Concepto central regulatorio que organiza la evaluación y categorización de la situación de los deudores.",
   "Sistema de categorización de deudores según criterios establecidos por el BCRA.",
   "Concepto técnico regulatorio relativo a la categorización de deudores según su riesgo de incobrabilidad.",
   "Concepto regulatorio que establece la categorización del estado crediticio de los deudores en el sistema financiero."
  ],
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 10 > Punto 1.1"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 10 > Punto 6.5"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 10 > Punto 10.4 /a"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 10 > Punto 5593 /b"
  }
 ]
}
```

--- paso 7 · ver_vecinos · input={"id": "sujeto_regulado:proveedores_no_financieros_de_credito", "direccion": "salientes"} · runtime=1737 · re-ejecutado=1737 ---

```json
{
 "id": "sujeto_regulado:proveedores_no_financieros_de_credito",
 "label": "proveedores no financieros de crédito",
 "n_salientes_total": 5,
 "n_entrantes_total": 0,
 "salientes": [
  {
   "relation": "obligado_a",
   "vecino_id": "obligacion:clasificar_deudores_segun_mora_en_cartera_consumo_vivienda",
   "vecino_label": "clasificar deudores según mora en cartera consumo/vivienda",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "Sección 7 > Sección 7 — preámbulo"
    }
   ]
  },
  {
   "relation": "obligado_a",
   "vecino_id": "obligacion:considerar_y_resolver_fundadamente_reclamos_de_usuarios",
   "vecino_label": "considerar y resolver fundadamente reclamos de usuarios",
   "provenances": [
    {
     "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
     "location": "Sección 5 > Punto 1.1"
    }
   ]
  },
  {
   "relation": "obligado_a",
   "vecino_id": "obligacion:cumplimiento_de_normas_de_proteccion_de_usuarios",
   "vecino_label": "cumplimiento de normas de protección de usuarios",
   "provenances": [
    {
     "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
     "location": "Sección 5 > Punto 1.1"
    }
   ]
  },
  {
   "relation": "supervisado_por",
   "vecino_id": "organismo_regulador:banco_central_de_la_republica_argentina",
   "vecino_label": "Banco Central de la República Argentina",
   "provenances": [
    {
     "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
     "location": "Sección 5 > Punto 1.1"
    }
   ]
  },
  {
   "relation": "obligado_a",
   "vecino_id": "obligacion:designar_directivo_responsable_de_proteccion",
   "vecino_label": "designar directivo responsable de protección",
   "provenances": [
    {
     "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
     "location": "Sección 3 > Sección 3 — preámbulo"
    }
   ]
  }
 ],
 "salientes_truncado": false
}
```

--- paso 8 · ver_vecinos · input={"id": "sujeto_regulado:empresas_no_financieras_emisoras_de_tarjetas_de_credito", "direccion": "salientes"} · runtime=2837 · re-ejecutado=2837 ---

```json
{
 "id": "sujeto_regulado:empresas_no_financieras_emisoras_de_tarjetas_de_credito",
 "label": "empresas no financieras emisoras de tarjetas de crédito",
 "n_salientes_total": 8,
 "n_entrantes_total": 0,
 "salientes": [
  {
   "relation": "obligado_a",
   "vecino_id": "obligacion:considerar_y_resolver_fundadamente_reclamos_de_usuarios",
   "vecino_label": "considerar y resolver fundadamente reclamos de usuarios",
   "provenances": [
    {
     "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
     "location": "Sección 5 > Punto 1.1"
    }
   ]
  },
  {
   "relation": "obligado_a",
   "vecino_id": "obligacion:cumplimiento_de_normas_de_proteccion_de_usuarios",
   "vecino_label": "cumplimiento de normas de protección de usuarios",
   "provenances": [
    {
     "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
     "location": "Sección 5 > Punto 1.1"
    }
   ]
  },
  {
   "relation": "supervisado_por",
   "vecino_id": "organismo_regulador:banco_central_de_la_republica_argentina",
   "vecino_label": "Banco Central de la República Argentina",
   "provenances": [
    {
     "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
     "location": "Sección 5 > Punto 1.1"
    }
   ]
  },
  {
   "relation": "obligado_a",
   "vecino_id": "obligacion:entregar_detalle_de_caracteristicas_de_productos_y_servicios",
   "vecino_label": "entregar detalle de características de productos y servicios",
   "provenances": [
    {
     "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
     "location": "Sección 2 > Punto 2.4"
    }
   ]
  },
  {
   "relation": "obligado_a",
   "vecino_id": "obligacion:publicar_contratos_de_adhesion_en_sitio_de_internet_institucional",
   "vecino_label": "publicar contratos de adhesión en sitio de Internet institucional",
   "provenances": [
    {
     "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
     "location": "Sección 2 > Punto 2.4"
    }
   ]
  },
  {
   "relation": "obligado_a",
   "vecino_id": "obligacion:publicar_promociones_y_bonificaciones_con_fechas_y_modalidades",
   "vecino_label": "publicar promociones y bonificaciones con fechas y modalidades",
   "provenances": [
    {
     "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
     "location": "Sección 2 > Punto 2.4"
    }
   ]
  },
  {
   "relation": "obligado_a",
   "vecino_id": "obligacion:entregar_copia_integra_de_instrumentos_suscritos_al_solicitar_productos",
   "vecino_label": "entregar copia íntegra de instrumentos suscritos al solicitar productos",
   "provenances": [
    {
     "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
     "location": "Sección 2 > Punto 2.4"
    }
   ]
  },
  {
   "relation": "obligado_a",
   "vecino_id": "obligacion:habilitar_consulta_y_descarga_de_contrato_mediante_home_banking_o_sitio",
   "vecino_label": "habilitar consulta y descarga de contrato mediante home banking o sitio",
   "provenances": [
    {
     "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
     "location": "Sección 2 > Punto 2.4"
    }
   ]
  }
 ],
 "salientes_truncado": false
}
```

--- paso 9 · ver_nodo · input={"id": "obligacion:clasificar_deudores_segun_mora_en_cartera_consumo_vivienda"} · runtime=511 · re-ejecutado=511 ---

```json
{
 "id": "obligacion:clasificar_deudores_segun_mora_en_cartera_consumo_vivienda",
 "type": "Obligacion",
 "label": "clasificar deudores según mora en cartera consumo/vivienda",
 "properties": {
  "description": "Proveedores no financieros deben clasificar deudores en función de su mora aplicando criterios de cartera consumo o vivienda.",
  "modalidad": "obligacion",
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 7 > Sección 7 — preámbulo"
  }
 ]
}
```

--- paso 10 · buscar_nodos · input={"consulta": "criterios clasificación deudores mora capacidad pago", "limite": 10} · runtime=3225 · re-ejecutado=3225 ---

```json
{
 "consulta": "criterios clasificación deudores mora capacidad pago",
 "total_con_match": 292,
 "resultados": [
  {
   "id": "concepto_definido:capacidad_de_pago",
   "type": "ConceptoDefinido",
   "label": "capacidad de pago",
   "tokens_matcheados": 2,
   "resumen_propiedades": "['Criterio básico de clasificación: la capacidad de pago en el futuro de la deuda o de los compromisos objeto de la garantía.', 'Capacidad del cliente para aten…"
  },
  {
   "id": "concepto_definido:clasificacion_de_deudores",
   "type": "ConceptoDefinido",
   "label": "clasificación de deudores",
   "tokens_matcheados": 2,
   "resumen_propiedades": "['Concepto central regulatorio que organiza la evaluación y categorización de la situación de los deudores.', 'Sistema de categorización de deudores según crite…"
  },
  {
   "id": "procedimiento:clasificacion_de_deudores",
   "type": "Procedimiento",
   "label": "clasificación de deudores",
   "tokens_matcheados": 2,
   "resumen_propiedades": "['Procedimiento de evaluación y clasificación de clientes según su capacidad de cumplimiento de compromisos financieros.', 'Proceso de asignación de categoría d…"
  },
  {
   "id": "concepto_definido:capacidad_de_pago_del_deudor",
   "type": "ConceptoDefinido",
   "label": "capacidad de pago del deudor",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Evaluación de la afectación de ingresos periódicos por la totalidad de los compromisos de crédito asumidos por el deudor."
  },
  {
   "id": "requisito:mora_en_el_pago_de_hasta_un_ano",
   "type": "Requisito",
   "label": "mora en el pago de hasta un año",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Condición de demanda judicial cuando existe mora en el pago de hasta un año."
  },
  {
   "id": "procedimiento:tarea_de_clasificacion_de_deudores",
   "type": "Procedimiento",
   "label": "tarea de clasificación de deudores",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Procedimiento mediante el cual una entidad financiera asigna clasificaciones a sus clientes deudores."
  },
  {
   "id": "concepto_definido:accion_criterios_de_clasificacion",
   "type": "ConceptoDefinido",
   "label": "acción (criterios de clasificación)",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Definición de qué constituye una acción según criterios económicos y estructurales establecidos en el texto normativo."
  },
  {
   "id": "concepto_definido:criterios_objetivos_de_clasificacion",
   "type": "ConceptoDefinido",
   "label": "criterios objetivos de clasificación",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Criterios establecidos en la norma para clasificar deudores, incluyendo término de morosidad, situación jurídica del cliente o sus deudas, cumplimiento de refin…"
  },
  {
   "id": "norma_referenciada:normas_sobre_clasificacion_de_deudores",
   "type": "NormaReferenciada",
   "label": "normas sobre Clasificación de deudores",
   "tokens_matcheados": 2,
   "resumen_propiedades": "['Normativa referenciada para la clasificación promedio de deudores en información de exposiciones subyacentes.', 'Normas externas que definen la clasificación …"
  },
  {
   "id": "concepto_definido:categorias_de_clasificacion_de_deudores",
   "type": "ConceptoDefinido",
   "label": "categorías de clasificación de deudores",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Categorías 1 a 5 utilizadas para clasificar a los deudores según su evaluación de riesgo."
  }
 ]
}
```

--- paso 11 · ver_nodo · input={"id": "concepto_definido:criterios_objetivos_de_clasificacion"} · runtime=488 · re-ejecutado=488 ---

```json
{
 "id": "concepto_definido:criterios_objetivos_de_clasificacion",
 "type": "ConceptoDefinido",
 "label": "criterios objetivos de clasificación",
 "properties": {
  "description": "Criterios establecidos en la norma para clasificar deudores, incluyendo término de morosidad, situación jurídica del cliente o sus deudas, cumplimiento de refinanciaciones.",
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 6 > Punto 6.4"
  }
 ]
}
```

--- paso 12 · ver_nodo · input={"id": "concepto_definido:capacidad_de_pago"} · runtime=643 · re-ejecutado=643 ---

```json
{
 "id": "concepto_definido:capacidad_de_pago",
 "type": "ConceptoDefinido",
 "label": "capacidad de pago",
 "properties": {
  "description": [
   "Criterio básico de clasificación: la capacidad de pago en el futuro de la deuda o de los compromisos objeto de la garantía.",
   "Capacidad del cliente para atender el pago de capital e intereses en las condiciones pactadas, medida a través del análisis de flujo de fondos."
  ],
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 3 > Punto 3.6"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 6 > Punto 5.1"
  }
 ]
}
```

--- paso 13 · buscar_nodos · input={"consulta": "empresas no financieras tarjetas clasificación deudores obligación", "limite": 10} · runtime=3817 · re-ejecutado=3817 ---

```json
{
 "consulta": "empresas no financieras tarjetas clasificación deudores obligación",
 "total_con_match": 1672,
 "resultados": [
  {
   "id": "sujeto_regulado:empresas_no_financieras_emisoras_de_tarjetas",
   "type": "SujetoRegulado",
   "label": "empresas no financieras emisoras de tarjetas",
   "tokens_matcheados": 4,
   "resumen_propiedades": "['Empresas no financieras que emiten tarjetas de crédito y/o compra y están obligadas a informar comisiones.', 'Empresas no financieras emisoras de tarjetas de …"
  },
  {
   "id": "sujeto_regulado:empresas_no_financieras_emisoras_de_tarjetas_de_credito",
   "type": "SujetoRegulado",
   "label": "empresas no financieras emisoras de tarjetas de crédito",
   "tokens_matcheados": 4,
   "resumen_propiedades": "['Sujetos obligados que emiten tarjetas de crédito y/o compra.', 'Empresas no financieras que emiten tarjetas de crédito y están sujetas a regulaciones de prote…"
  },
  {
   "id": "obligacion:no_incluir_en_clasificacion_a_deudores_en_cesion_sin_responsabilidad",
   "type": "Obligacion",
   "label": "no incluir en clasificación a deudores en cesión sin responsabilidad",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Excepción: los deudores que resulten de operaciones de cesión sin responsabilidad para el cedente no serán objeto de clasificación."
  },
  {
   "id": "obligacion:no_apertura_de_legajo_para_deudores_por_servicios_publicos_o_tarjetas_de_credito",
   "type": "Obligacion",
   "label": "no apertura de legajo para deudores por servicios públicos o tarjetas de crédito",
   "tokens_matcheados": 4,
   "resumen_propiedades": "No es obligatoria la apertura de legajo en casos de deudores por servicios públicos o tarjetas de crédito cedidos por deudores en concurso preventivo."
  },
  {
   "id": "obligacion:clasificacion_y_prevision_de_deudores_excluidos",
   "type": "Obligacion",
   "label": "clasificación y previsión de deudores excluidos",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Obligación de clasificar y prever deudores excluidos de las categorías especiales conforme a disposiciones de carácter general."
  },
  {
   "id": "obligacion:no_mejorar_clasificacion_por_razones_de_emergencia",
   "type": "Obligacion",
   "label": "no mejorar clasificación por razones de emergencia",
   "tokens_matcheados": 3,
   "resumen_propiedades": "El tratamiento de emergencia no puede implicar mejoramiento de clasificación preexistente del cliente."
  },
  {
   "id": "obligacion:aprobacion_de_clasificacion_de_deudores_por_directorio",
   "type": "Obligacion",
   "label": "aprobación de clasificación de deudores por directorio",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La clasificación de deudores y cálculo de previsiones por riesgo de incobrabilidad debe contar con previa aprobación del Directorio o Consejo de Administración,…"
  },
  {
   "id": "obligacion:efectuar_clasificacion_de_deudores_con_periodicidad_adecuada",
   "type": "Obligacion",
   "label": "efectuar clasificación de deudores con periodicidad adecuada",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La clasificación de deudores debe efectuarse con periodicidad que atienda a su importancia, considerando la totalidad de financiaciones comprendidas, con docume…"
  },
  {
   "id": "obligacion:tratamiento_de_ccp_no_calificadas_como_entidades_financieras",
   "type": "Obligacion",
   "label": "tratamiento de CCP no calificadas como entidades financieras",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Obligación de considerar a las CCP que no califican como entidades financieras para el cálculo de exigencias de capital por operaciones de negociación."
  },
  {
   "id": "obligacion:apertura_de_legajo_no_obligatoria_para_servicios_publicos_o_tarjetas",
   "type": "Obligacion",
   "label": "apertura de legajo no obligatoria para servicios públicos o tarjetas",
   "tokens_matcheados": 3,
   "resumen_propiedades": "En casos de deudores por servicios públicos o tarjetas de crédito no será obligatoria la apertura del legajo."
  }
 ]
}
```

--- paso 14 · buscar_nodos · input={"consulta": "sección 7 proveedores no financieros clasificación", "limite": 10} · runtime=3734 · re-ejecutado=3734 ---

```json
{
 "consulta": "sección 7 proveedores no financieros clasificación",
 "total_con_match": 428,
 "resultados": [
  {
   "id": "sujeto_regulado:proveedores_no_financieros_de_credito",
   "type": "SujetoRegulado",
   "label": "proveedores no financieros de crédito",
   "tokens_matcheados": 3,
   "resumen_propiedades": "['Empresas no financieras emisoras de tarjetas de crédito y otros proveedores alcanzados por normas especiales.', 'Sujetos obligados alcanzados por normas sobre…"
  },
  {
   "id": "sujeto_regulado:otros_proveedores_no_financieros_de_credito",
   "type": "SujetoRegulado",
   "label": "otros proveedores no financieros de crédito",
   "tokens_matcheados": 3,
   "resumen_propiedades": "['Proveedores no financieros que otorgan crédito y deben cumplir obligaciones de divulgación de información.', 'Proveedores no financieros de crédito que ofrece…"
  },
  {
   "id": "norma_referenciada:normas_sobre_proveedores_no_financieros_de_credito",
   "type": "NormaReferenciada",
   "label": "normas sobre Proveedores no financieros de crédito",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Normas que regulan a los proveedores no financieros de crédito."
  },
  {
   "id": "concepto_definido:activos_no_financieros_no_producidos",
   "type": "ConceptoDefinido",
   "label": "activos no financieros no producidos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Transacciones de traspaso de activos intangibles como derechos de pesca, derechos minerales, espacio aéreo, pases de deportistas, patentes, derechos de autor, c…"
  },
  {
   "id": "obligacion:no_mejorar_clasificacion_por_razones_de_emergencia",
   "type": "Obligacion",
   "label": "no mejorar clasificación por razones de emergencia",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El tratamiento de emergencia no puede implicar mejoramiento de clasificación preexistente del cliente."
  },
  {
   "id": "operacion:enajenacion_de_activos_no_financieros_no_producidos",
   "type": "Operacion",
   "label": "enajenación de activos no financieros no producidos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "['Operación de venta o disposición de activos no financieros que no son producidos.', 'Operación de venta de activos no financieros no producidos por residentes…"
  },
  {
   "id": "operacion:operaciones_de_derivados_financieros_por_residentes_no_autorizados",
   "type": "Operacion",
   "label": "operaciones de derivados financieros por residentes no autorizados",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Operaciones de derivados cursadas por residentes que no son entidades autorizadas a operar en cambios."
  },
  {
   "id": "obligacion:no_incluir_en_clasificacion_a_deudores_en_cesion_sin_responsabilidad",
   "type": "Obligacion",
   "label": "no incluir en clasificación a deudores en cesión sin responsabilidad",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Excepción: los deudores que resulten de operaciones de cesión sin responsabilidad para el cedente no serán objeto de clasificación."
  },
  {
   "id": "obligacion:informar_en_notas_a_estados_financieros_sobre_respaldo_crediticio_no_contractual",
   "type": "Obligacion",
   "label": "informar en notas a estados financieros sobre respaldo crediticio no contractual",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La entidad debe informar en las notas a los estados financieros de publicación que ha prestado respaldo crediticio no contractual y el efecto sobre su exigencia…"
  },
  {
   "id": "obligacion:prohibicion_de_comisiones_por_servicios_financieros_no_solicitados_pactados_o_au",
   "type": "Obligacion",
   "label": "prohibición de comisiones por servicios financieros no solicitados, pactados o autorizados",
   "tokens_matcheados": 2,
   "resumen_propiedades": "No pueden aplicarse comisiones y/o cargos al usuario por servicios financieros que no hayan sido solicitados, pactados y/o autorizados por él, ni cuando no se h…"
  }
 ]
}
```

--- paso 15 · ver_vecinos · input={"id": "sujeto_regulado:empresas_no_financieras_emisoras_de_tarjetas", "direccion": "salientes"} · runtime=1963 · re-ejecutado=1963 ---

```json
{
 "id": "sujeto_regulado:empresas_no_financieras_emisoras_de_tarjetas",
 "label": "empresas no financieras emisoras de tarjetas",
 "n_salientes_total": 6,
 "n_entrantes_total": 0,
 "salientes": [
  {
   "relation": "obligado_a",
   "vecino_id": "obligacion:informar_comisiones_y_cargos",
   "vecino_label": "informar comisiones y cargos",
   "provenances": [
    {
     "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
     "location": "Sección 2 > Punto 2.5"
    }
   ]
  },
  {
   "relation": "obligado_a",
   "vecino_id": "obligacion:informar_altas_de_comisiones_previamente",
   "vecino_label": "informar altas de comisiones previamente",
   "provenances": [
    {
     "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
     "location": "Sección 2 > Punto 2.5"
    }
   ]
  },
  {
   "relation": "obligado_a",
   "vecino_id": "obligacion:informar_aumentos_de_comisiones_previamente",
   "vecino_label": "informar aumentos de comisiones previamente",
   "provenances": [
    {
     "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
     "location": "Sección 2 > Punto 2.5"
    }
   ]
  },
  {
   "relation": "obligado_a",
   "vecino_id": "obligacion:notificar_a_usuarios_sobre_comisiones_y_cargos",
   "vecino_label": "notificar a usuarios sobre comisiones y cargos",
   "provenances": [
    {
     "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
     "location": "Sección 2 > Punto 2.5"
    }
   ]
  },
  {
   "relation": "obligado_a",
   "vecino_id": "obligacion:informar_reducciones_de_comisiones_dentro_de_plazo",
   "vecino_label": "informar reducciones de comisiones dentro de plazo",
   "provenances": [
    {
     "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
     "location": "Sección 2 > Punto 2.5"
    }
   ]
  },
  {
   "relation": "obligado_a",
   "vecino_id": "obligacion:designar_directivo_responsable_de_proteccion",
   "vecino_label": "designar directivo responsable de protección",
   "provenances": [
    {
     "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
     "location": "Sección 3 > Sección 3 — preámbulo"
    }
   ]
  }
 ],
 "salientes_truncado": false
}
```

---

# Sección 3 — run_2/CQ-019

## 3a. Respuesta final del agente (verbatim, `posthoc_run/traces/off/run_2/CQ-019.json`)

`trace.final_json`:

```json
{
 "respuesta": "No se encontró en el Knowledge Graph información específica sobre qué previsión por incobrabilidad no se deduce al computar los activos para la exigencia de capital por riesgo de crédito, ni cómo se vincula esa regla con la clasificación de deudores. El grafo contiene referencias a previsión contable, previsión regulatoria y previsión por riesgo de incobrabilidad, pero no especifica cuál se excluye del cálculo de activos ni su relación con la clasificación de deudores.",
 "citas": [],
 "respondible": false
}
```

`trace.final_raw` (turno final íntegro):

```
Basándome en la información recolectada del Knowledge Graph, no he encontrado evidencia explícita que especifique qué previsión por incobrabilidad NO se deduce al computar los activos para la exigencia de capital por riesgo de crédito, ni cómo se vincula esa regla específicamente con la clasificación de deudores.

He identificado que existen:
- **Previsión por riesgo de incobrabilidad**: deducción contable para riesgos de incobrabilidad, aplicable a deudores en situación normal y financiaciones con garantías preferidas.
- **Previsión regulatoria por riesgo de incobrabilidad**: calculada según normas sobre Previsiones Mínimas por Riesgo de Incobrabilidad.
- **Previsión contable**: según NIIF 9.

Sin embargo, el grafo no contiene información específica sobre cuál de estas previsiones NO se deduce en el cálculo de activos para la exigencia de capital por riesgo de crédito, ni la relación explícita entre esa exclusión y la clasificación de deudores.

```json
{
  "respuesta": "No se encontró en el Knowledge Graph información específica sobre qué previsión por incobrabilidad no se deduce al computar los activos para la exigencia de capital por riesgo de crédito, ni cómo se vincula esa regla con la clasificación de deudores. El grafo contiene referencias a previsión contable, previsión regulatoria y previsión por riesgo de incobrabilidad, pero no especifica cuál se excluye del cálculo de activos ni su relación con la clasificación de deudores.",
  "citas": [],
  "respondible": false
}
```
```

## 3b. Inventario de pasos (runtime vs. almacenado vs. re-ejecutado)

| paso | tool | input | chars runtime | chars almacenados | re-ejecutado |
|---|---|---|---|---|---|
| 1 | buscar_nodos | `{"consulta": "exigencia capital riesgo crédito previsión incobrabilidad", "limite": 10}` | 3863 | 1215 | = runtime ✓ |
| 2 | buscar_nodos | `{"consulta": "previsión incobrabilidad deducción activos", "limite": 10}` | 3270 | 1215 | = runtime ✓ |
| 3 | buscar_nodos | `{"consulta": "clasificación deudores previsión", "limite": 10}` | 3436 | 1215 | = runtime ✓ |
| 4 | ver_nodo | `{"id": "obligacion:exigencia_de_capital_por_riesgo_de_credito"}` | 548 | 548 | = runtime ✓ |
| 5 | ver_nodo | `{"id": "concepto_definido:prevision_por_riesgo_de_incobrabilidad"}` | 703 | 703 | = runtime ✓ |
| 6 | buscar_nodos | `{"consulta": "activos ponderados riesgo crédito cálculo deducción", "limite": 10}` | 3828 | 1215 | = runtime ✓ |
| 7 | buscar_nodos | `{"consulta": "previsión no se deduce activos", "limite": 10}` | 3520 | 1215 | = runtime ✓ |
| 8 | ver_nodo | `{"id": "concepto_definido:activos_ponderados_por_riesgo_de_credito"}` | 614 | 614 | = runtime ✓ |
| 9 | ver_vecinos | `{"id": "concepto_definido:activos_ponderados_por_riesgo_de_credito", "direccion": "salientes"}` | 215 | 215 | = runtime ✓ |
| 10 | buscar_nodos | `{"consulta": "computar activos exigencia capital previsión regulatoria", "limite": 10}` | 3046 | 1215 | = runtime ✓ |
| 11 | buscar_nodos | `{"consulta": "previsión regulatoria incobrabilidad deducción", "limite": 10}` | 3277 | 1215 | = runtime ✓ |
| 12 | ver_nodo | `{"id": "concepto_definido:prevision_regulatoria_por_riesgo_de_incobrabilidad"}` | 429 | 429 | = runtime ✓ |
| 13 | ver_vecinos | `{"id": "concepto_definido:prevision_regulatoria_por_riesgo_de_incobrabilidad", "direccion": "ambas"}` | 572 | 572 | = runtime ✓ |
| 14 | buscar_nodos | `{"consulta": "computación activos riesgo crédito previsión contable regulatoria", "limite": 10}` | 3229 | 1215 | = runtime ✓ |
| 15 | buscar_nodos | `{"consulta": "activos computables riesgo crédito deducción previsión", "limite": 10}` | 3222 | 1215 | = runtime ✓ |

**Fidelidad runtime↔re-ejecución: 15/15 pasos con largo idéntico.**

## 3c. APÉNDICE — outputs completos re-ejecutados (15 pasos)


--- paso 1 · buscar_nodos · input={"consulta": "exigencia capital riesgo crédito previsión incobrabilidad", "limite": 10} · runtime=3863 · re-ejecutado=3863 ---

```json
{
 "consulta": "exigencia capital riesgo crédito previsión incobrabilidad",
 "total_con_match": 716,
 "resultados": [
  {
   "id": "concepto_definido:exigencia_de_capital_por_riesgo_de_credito",
   "type": "ConceptoDefinido",
   "label": "exigencia de capital por riesgo de crédito",
   "tokens_matcheados": 4,
   "resumen_propiedades": "CRC: medida de capital regulatorio calculada mediante fórmula que incorpora factor de calificación y activos ponderados por riesgo de crédito."
  },
  {
   "id": "obligacion:exigencia_de_capital_por_riesgo_de_credito",
   "type": "Obligacion",
   "label": "exigencia de capital por riesgo de crédito",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Las entidades financieras deben determinar la exigencia de capital por riesgo de crédito (CRC) aplicando una fórmula específica que incorpora un factor de calif…"
  },
  {
   "id": "concepto_definido:exigencia_de_capital_minimo_por_riesgo_de_credito",
   "type": "ConceptoDefinido",
   "label": "exigencia de capital mínimo por riesgo de crédito",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Magnitud de capital regulatorio que las entidades deben mantener por exposición a riesgo de crédito."
  },
  {
   "id": "concepto_definido:exigencia_de_capital_por_riesgo_de_credito_en_derivados",
   "type": "ConceptoDefinido",
   "label": "exigencia de capital por riesgo de crédito en derivados",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Exigencia de capital (RCD) por operaciones con derivados OTC o negociados en mercados regulados con liquidación diferida."
  },
  {
   "id": "obligacion:exigencia_de_capital_por_riesgo_de_credito_de_contraparte",
   "type": "Obligacion",
   "label": "exigencia de capital por riesgo de crédito de contraparte",
   "tokens_matcheados": 4,
   "resumen_propiedades": "['Deber de las entidades de calcular y mantener capital mínimo para cubrir la exposición al riesgo de crédito de contraparte en operaciones pendientes de liquid…"
  },
  {
   "id": "operacion:disminucion_de_exigencia_de_capital_minimo_por_riesgo_de_credito",
   "type": "Operacion",
   "label": "disminución de exigencia de capital mínimo por riesgo de crédito",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Operación regulada bajo código 60100000 que reduce la exigencia de capital mínimo por riesgo de crédito mediante franquicia."
  },
  {
   "id": "obligacion:aplicar_exigencia_adicional_de_capital_por_riesgo_de_credito_agricola",
   "type": "Obligacion",
   "label": "aplicar exigencia adicional de capital por riesgo de crédito agrícola",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Obligación de aplicar metodología específica para computar exigencia adicional por financiaciones a clientes agrícolas no MIPyMES."
  },
  {
   "id": "obligacion:calcular_exigencia_de_capital_por_riesgo_de_credito_de_contraparte_en_derivados",
   "type": "Obligacion",
   "label": "calcular exigencia de capital por riesgo de crédito de contraparte en derivados",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Calcular exigencia de capital por riesgo de crédito de contraparte en operaciones con derivados registradas en cartera de negociación."
  },
  {
   "id": "obligacion:incremento_de_exigencia_por_riesgo_de_credito_por_excesos_en_participaciones_en_",
   "type": "Obligacion",
   "label": "incremento de exigencia por riesgo de crédito por excesos en participaciones en capital",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Obligación de incrementar la exigencia de capital por riesgo de crédito por excesos en inversiones significativas en empresas."
  },
  {
   "id": "obligacion:calcular_exigencia_de_capital_por_riesgo_especifico_para_derivado_de_credito_de_",
   "type": "Obligacion",
   "label": "calcular exigencia de capital por riesgo específico para derivado de crédito de enésimo incumplimiento",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Las entidades deben calcular la exigencia de capital por cada posición neta en derivados de crédito de enésimo incumplimiento independientemente de si obtienen …"
  }
 ]
}
```

--- paso 2 · buscar_nodos · input={"consulta": "previsión incobrabilidad deducción activos", "limite": 10} · runtime=3270 · re-ejecutado=3270 ---

```json
{
 "consulta": "previsión incobrabilidad deducción activos",
 "total_con_match": 157,
 "resultados": [
  {
   "id": "concepto_definido:prevision_por_riesgo_de_incobrabilidad",
   "type": "ConceptoDefinido",
   "label": "previsión por riesgo de incobrabilidad",
   "tokens_matcheados": 2,
   "resumen_propiedades": "['Deducción contable para riesgos de incobrabilidad, incluyendo previsiones en pasivo, aplicable a deudores en situación normal y financiaciones con garantías p…"
  },
  {
   "id": "concepto_definido:prevision_regulatoria_por_riesgo_de_incobrabilidad",
   "type": "ConceptoDefinido",
   "label": "previsión regulatoria por riesgo de incobrabilidad",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Previsión calculada según normas sobre Previsiones Mínimas por Riesgo de Incobrabilidad."
  },
  {
   "id": "obligacion:deduccion_de_importes_de_activos_registrados_incorrectamente",
   "type": "Obligacion",
   "label": "deducción de importes de activos registrados incorrectamente",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Obligación de las entidades financieras de deducir importes de activos u otros conceptos cuando la contabilidad no refleje la realidad económica y jurídica de l…"
  },
  {
   "id": "concepto_definido:prevision_por_riesgo_de_incobrabilidad_cartera_situacion_normal",
   "type": "ConceptoDefinido",
   "label": "previsión por riesgo de incobrabilidad cartera situación normal",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Importe de previsión por riesgo de incobrabilidad correspondiente a cartera en situación normal, computado como patrimonio neto complementario."
  },
  {
   "id": "concepto_definido:activos_fijos",
   "type": "ConceptoDefinido",
   "label": "activos fijos",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Activos fijos, clasificados como concepto excluido del régimen informativo."
  },
  {
   "id": "concepto_definido:activos_rotativos",
   "type": "ConceptoDefinido",
   "label": "activos rotativos",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Estructuras sobre activos de tipo rotativo como tarjetas de crédito, facturas y otras exposiciones cancelables en un solo pago."
  },
  {
   "id": "concepto_definido:canasta_de_activos",
   "type": "ConceptoDefinido",
   "label": "canasta de activos",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Conjunto de varios activos recibidos en garantía, cuyo aforo agregado se calcula como suma ponderada de los aforos individuales."
  },
  {
   "id": "concepto_definido:prevision_contable",
   "type": "ConceptoDefinido",
   "label": "previsión contable",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Previsión contable correspondiente al balance de saldos al 30.11.19 o por aplicación de NIIF 9 punto 5.5 sobre deterioro de valor."
  },
  {
   "id": "concepto_definido:activos_intangibles",
   "type": "ConceptoDefinido",
   "label": "activos intangibles",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Incluye llave de negocio de inversiones significativas en entidades financieras no sujetas a supervisión consolidada y valor llave de participaciones en otras s…"
  },
  {
   "id": "concepto_definido:activos_subyacentes",
   "type": "ConceptoDefinido",
   "label": "activos subyacentes",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Conjunto de activos que conforman la base de una titulización, incluidos activos en los que ha invertido el SPE, reservas, cuentas de efectivo en garantía y der…"
  }
 ]
}
```

--- paso 3 · buscar_nodos · input={"consulta": "clasificación deudores previsión", "limite": 10} · runtime=3436 · re-ejecutado=3436 ---

```json
{
 "consulta": "clasificación deudores previsión",
 "total_con_match": 82,
 "resultados": [
  {
   "id": "obligacion:clasificacion_y_prevision_de_deudores_excluidos",
   "type": "Obligacion",
   "label": "clasificación y previsión de deudores excluidos",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Obligación de clasificar y prever deudores excluidos de las categorías especiales conforme a disposiciones de carácter general."
  },
  {
   "id": "concepto_definido:clasificacion_de_deudores",
   "type": "ConceptoDefinido",
   "label": "clasificación de deudores",
   "tokens_matcheados": 2,
   "resumen_propiedades": "['Concepto central regulatorio que organiza la evaluación y categorización de la situación de los deudores.', 'Sistema de categorización de deudores según crite…"
  },
  {
   "id": "procedimiento:clasificacion_de_deudores",
   "type": "Procedimiento",
   "label": "clasificación de deudores",
   "tokens_matcheados": 2,
   "resumen_propiedades": "['Procedimiento de evaluación y clasificación de clientes según su capacidad de cumplimiento de compromisos financieros.', 'Proceso de asignación de categoría d…"
  },
  {
   "id": "procedimiento:tarea_de_clasificacion_de_deudores",
   "type": "Procedimiento",
   "label": "tarea de clasificación de deudores",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Procedimiento mediante el cual una entidad financiera asigna clasificaciones a sus clientes deudores."
  },
  {
   "id": "norma_referenciada:normas_sobre_clasificacion_de_deudores",
   "type": "NormaReferenciada",
   "label": "normas sobre Clasificación de deudores",
   "tokens_matcheados": 2,
   "resumen_propiedades": "['Normativa referenciada para la clasificación promedio de deudores en información de exposiciones subyacentes.', 'Normas externas que definen la clasificación …"
  },
  {
   "id": "concepto_definido:categorias_de_clasificacion_de_deudores",
   "type": "ConceptoDefinido",
   "label": "categorías de clasificación de deudores",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Categorías 1 a 5 utilizadas para clasificar a los deudores según su evaluación de riesgo."
  },
  {
   "id": "norma_referenciada:texto_ordenado_sobre_clasificacion_de_deudores",
   "type": "NormaReferenciada",
   "label": "Texto Ordenado sobre Clasificación de Deudores",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Norma externa que define situaciones de deudores y disposiciones sobre clasificación, referenciada en puntos 6.5.1 y 7.2.1."
  },
  {
   "id": "concepto_definido:manual_de_procedimientos_de_clasificacion_y_prevision",
   "type": "ConceptoDefinido",
   "label": "Manual de procedimientos de clasificación y previsión",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Documento que debe prever la intervención de profesionales externos en el proceso de clasificación."
  },
  {
   "id": "procedimiento:manual_de_procedimientos_de_clasificacion_y_prevision",
   "type": "Procedimiento",
   "label": "manual de procedimientos de clasificación y previsión",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Documento que documenta los procedimientos implementados para clasificación de deudores y previsionamiento de acreencias, incluyendo niveles de análisis, decisi…"
  },
  {
   "id": "obligacion:aprobacion_de_clasificacion_de_deudores_por_directorio",
   "type": "Obligacion",
   "label": "aprobación de clasificación de deudores por directorio",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La clasificación de deudores y cálculo de previsiones por riesgo de incobrabilidad debe contar con previa aprobación del Directorio o Consejo de Administración,…"
  }
 ]
}
```

--- paso 4 · ver_nodo · input={"id": "obligacion:exigencia_de_capital_por_riesgo_de_credito"} · runtime=548 · re-ejecutado=548 ---

```json
{
 "id": "obligacion:exigencia_de_capital_por_riesgo_de_credito",
 "type": "Obligacion",
 "label": "exigencia de capital por riesgo de crédito",
 "properties": {
  "description": "Las entidades financieras deben determinar la exigencia de capital por riesgo de crédito (CRC) aplicando una fórmula específica que incorpora un factor de calificación y activos ponderados por riesgo de crédito.",
  "modalidad": "obligacion",
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 1 > Punto 2.1"
  }
 ]
}
```

--- paso 5 · ver_nodo · input={"id": "concepto_definido:prevision_por_riesgo_de_incobrabilidad"} · runtime=703 · re-ejecutado=703 ---

```json
{
 "id": "concepto_definido:prevision_por_riesgo_de_incobrabilidad",
 "type": "ConceptoDefinido",
 "label": "previsión por riesgo de incobrabilidad",
 "properties": {
  "description": [
   "Deducción contable para riesgos de incobrabilidad, incluyendo previsiones en pasivo, aplicable a deudores en situación normal y financiaciones con garantías preferidas.",
   "Concepto técnico regulatorio referido a las previsiones mínimas que deben constituirse por riesgo de incobrabilidad."
  ],
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 2 > Punto 2.3"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 10 > Punto 10.4 /a"
  }
 ]
}
```

--- paso 6 · buscar_nodos · input={"consulta": "activos ponderados riesgo crédito cálculo deducción", "limite": 10} · runtime=3828 · re-ejecutado=3828 ---

```json
{
 "consulta": "activos ponderados riesgo crédito cálculo deducción",
 "total_con_match": 616,
 "resultados": [
  {
   "id": "concepto_definido:activos_ponderados_por_riesgo_de_credito",
   "type": "ConceptoDefinido",
   "label": "activos ponderados por riesgo de crédito",
   "tokens_matcheados": 4,
   "resumen_propiedades": "['APRc: componente del cálculo de APR determinado conforme a las normas sobre riesgo de crédito.', 'APRc: activos computables ponderados por factores de riesgo …"
  },
  {
   "id": "concepto_definido:activos_ponderados_por_riesgo_de_credito_aprc",
   "type": "ConceptoDefinido",
   "label": "activos ponderados por riesgo de crédito (APRC)",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Suma de valores obtenidos aplicando una expresión que incluye activos con ponderaciones de riesgo, factores de conversión de crédito y componentes de riesgo de …"
  },
  {
   "id": "obligacion:calculo_de_activos_ponderados_por_riesgo_para_posiciones_superpuestas",
   "type": "Obligacion",
   "label": "cálculo de activos ponderados por riesgo para posiciones superpuestas",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Cuando existe superposición de posiciones y la entidad demuestra que el cumplimiento de obligaciones de una evita pérdidas de otra, no es necesario calcular act…"
  },
  {
   "id": "obligacion:exclusion_de_exposiciones_en_calculo_de_activos_ponderados_por_riesgo",
   "type": "Obligacion",
   "label": "exclusión de exposiciones en cálculo de activos ponderados por riesgo",
   "tokens_matcheados": 4,
   "resumen_propiedades": "La entidad originante puede excluir exposiciones objeto de titulización tradicional del cálculo de activos ponderados por riesgo si se cumplen requisitos operat…"
  },
  {
   "id": "obligacion:exclusion_de_exposiciones_del_calculo_de_activos_ponderados_por_riesgo",
   "type": "Obligacion",
   "label": "exclusión de exposiciones del cálculo de activos ponderados por riesgo",
   "tokens_matcheados": 4,
   "resumen_propiedades": "La entidad originante puede excluir del cálculo de activos ponderados por riesgo a las exposiciones subyacentes titulizadas, siempre que cumpla requisitos espec…"
  },
  {
   "id": "concepto_definido:activos_ponderados_por_riesgo",
   "type": "ConceptoDefinido",
   "label": "activos ponderados por riesgo",
   "tokens_matcheados": 3,
   "resumen_propiedades": "APR resulta de aplicar la expresión: APR = APRc + [(RM+RO) x 12,5], donde APRc son activos ponderados por riesgo de crédito, RM es exigencia por riesgo de merca…"
  },
  {
   "id": "concepto_definido:activos_ponderados_por_riesgo_apr",
   "type": "ConceptoDefinido",
   "label": "activos ponderados por riesgo (APR)",
   "tokens_matcheados": 3,
   "resumen_propiedades": "['Base de cálculo para el coeficiente de COn1 que determina eventos desencadenantes de absorción de pérdidas.', 'Parámetro calculado para determinar los límites…"
  },
  {
   "id": "obligacion:informar_activos_ponderados_por_riesgo",
   "type": "Obligacion",
   "label": "informar activos ponderados por riesgo",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Se deben informar los activos ponderados por riesgo (parámetro para cálculo de límites mínimos de componentes RPC) determinados según fórmula específica."
  },
  {
   "id": "requisito:reflejar_coberturas_de_riesgo_de_credito_en_calculo_ksa",
   "type": "Requisito",
   "label": "reflejar coberturas de riesgo de crédito en cálculo KSA",
   "tokens_matcheados": 3,
   "resumen_propiedades": "El cálculo de KSA debe reflejar los efectos de cualquier cobertura del riesgo de crédito aplicable a las exposiciones subyacentes individual o conjuntamente."
  },
  {
   "id": "concepto_definido:activos_ponderados_por_riesgo_atribuibles_a_la_inversion",
   "type": "ConceptoDefinido",
   "label": "activos ponderados por riesgo atribuibles a la inversión",
   "tokens_matcheados": 3,
   "resumen_propiedades": "APRinversión se calcula como el producto del ponderador de riesgo promedio del fondo, el apalancamiento y la inversión."
  }
 ]
}
```

--- paso 7 · buscar_nodos · input={"consulta": "previsión no se deduce activos", "limite": 10} · runtime=3520 · re-ejecutado=3520 ---

```json
{
 "consulta": "previsión no se deduce activos",
 "total_con_match": 438,
 "resultados": [
  {
   "id": "concepto_definido:perdidas_de_activos_no_corrientes",
   "type": "ConceptoDefinido",
   "label": "pérdidas de activos no corrientes",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Pérdidas que produzcan los activos no corrientes y grupos de activos mantenidos para la venta que no califiquen como operaciones discontinuadas."
  },
  {
   "id": "concepto_definido:activos_no_financieros_no_producidos",
   "type": "ConceptoDefinido",
   "label": "activos no financieros no producidos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Transacciones de traspaso de activos intangibles como derechos de pesca, derechos minerales, espacio aéreo, pases de deportistas, patentes, derechos de autor, c…"
  },
  {
   "id": "obligacion:no_transferir_activos_en_mora_o_incumplimiento",
   "type": "Obligacion",
   "label": "no transferir activos en mora o incumplimiento",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Prohibición de transferir activos que estén en situación de incumplimiento o mora a una titulización."
  },
  {
   "id": "operacion:enajenacion_de_activos_no_financieros_no_producidos",
   "type": "Operacion",
   "label": "enajenación de activos no financieros no producidos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "['Operación de venta o disposición de activos no financieros que no son producidos.', 'Operación de venta de activos no financieros no producidos por residentes…"
  },
  {
   "id": "operacion:compromiso_de_adquisicion_de_activos_no_contabilizados",
   "type": "Operacion",
   "label": "compromiso de adquisición de activos no contabilizados",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Compromisos de adquisición de activos no contabilizados en el balance de saldos."
  },
  {
   "id": "requisito:no_entregar_fondos_locales_recibiendo_activos_externos",
   "type": "Requisito",
   "label": "no entregar fondos locales recibiendo activos externos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Condición que el cliente debe acreditar: no ha entregado fondos en moneda local u otros activos locales a cambio de activos externos, criptoactivos o títulos va…"
  },
  {
   "id": "concepto_definido:activos_que_se_deducen_del_capital_ordinario_del_nivel_1",
   "type": "ConceptoDefinido",
   "label": "activos que se deducen del capital ordinario del nivel 1",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Activos que se deducen del capital ordinario del nivel 1 (COn1), clasificados como concepto excluido del régimen."
  },
  {
   "id": "obligacion:consideracion_de_liquidacion_de_activos_no_imprescindibles",
   "type": "Obligacion",
   "label": "consideración de liquidación de activos no imprescindibles",
   "tokens_matcheados": 2,
   "resumen_propiedades": "En segundo lugar en la evaluación de capacidad de repago, debe considerarse la posibilidad de liquidación de activos no imprescindibles para la operatoria de la…"
  },
  {
   "id": "obligacion:no_realizar_canjes_de_titulos_valores_por_activos_externos",
   "type": "Obligacion",
   "label": "no realizar canjes de títulos valores por activos externos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Prohibición de realizar canjes de títulos valores emitidos por residentes por activos externos."
  },
  {
   "id": "requisito:no_realizar_canjes_de_titulos_valores_por_activos_externos",
   "type": "Requisito",
   "label": "no realizar canjes de títulos valores por activos externos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Condición que el cliente debe acreditar: no ha realizado canjes de títulos valores emitidos por residentes por activos externos."
  }
 ]
}
```

--- paso 8 · ver_nodo · input={"id": "concepto_definido:activos_ponderados_por_riesgo_de_credito"} · runtime=614 · re-ejecutado=614 ---

```json
{
 "id": "concepto_definido:activos_ponderados_por_riesgo_de_credito",
 "type": "ConceptoDefinido",
 "label": "activos ponderados por riesgo de crédito",
 "properties": {
  "description": [
   "APRc: componente del cálculo de APR determinado conforme a las normas sobre riesgo de crédito.",
   "APRc: activos computables ponderados por factores de riesgo según exposiciones de deuda."
  ],
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 8 > Punto 8.5"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Sección 2 > Punto 3.1"
  }
 ]
}
```

--- paso 9 · ver_vecinos · input={"id": "concepto_definido:activos_ponderados_por_riesgo_de_credito", "direccion": "salientes"} · runtime=215 · re-ejecutado=215 ---

```json
{
 "id": "concepto_definido:activos_ponderados_por_riesgo_de_credito",
 "label": "activos ponderados por riesgo de crédito",
 "n_salientes_total": 0,
 "n_entrantes_total": 2,
 "salientes": [],
 "salientes_truncado": false
}
```

--- paso 10 · buscar_nodos · input={"consulta": "computar activos exigencia capital previsión regulatoria", "limite": 10} · runtime=3046 · re-ejecutado=3046 ---

```json
{
 "consulta": "computar activos exigencia capital previsión regulatoria",
 "total_con_match": 488,
 "resultados": [
  {
   "id": "concepto_definido:exigencia_de_capital",
   "type": "ConceptoDefinido",
   "label": "exigencia de capital",
   "tokens_matcheados": 2,
   "resumen_propiedades": "['Requerimiento de capital que se calcula considerando vínculos entre CCPs y su exposición a miembros compensadores.', 'Requerimiento de capital cuyo cálculo de…"
  },
  {
   "id": "concepto_definido:prevision_regulatoria",
   "type": "ConceptoDefinido",
   "label": "previsión regulatoria",
   "tokens_matcheados": 2,
   "resumen_propiedades": "['Importe resultante de la aplicación de normas sobre previsiones mínimas por riesgo de incobrabilidad.', 'Previsión según normas sobre provisiones mínimas por …"
  },
  {
   "id": "concepto_definido:ksa_exigencia_de_capital",
   "type": "ConceptoDefinido",
   "label": "KSA exigencia de capital",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Exigencia de capital que hubiera correspondido a las exposiciones subyacentes de no haber sido titulizadas."
  },
  {
   "id": "umbral:3_de_exigencia_de_capital",
   "type": "Umbral",
   "label": "3% de exigencia de capital",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Límite que activa acciones para regularizar defectos de integración diaria."
  },
  {
   "id": "umbral:8_de_exigencia_de_capital",
   "type": "Umbral",
   "label": "8% de exigencia de capital",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Porcentaje aplicable en el cálculo de la exigencia final de capital por riesgo de crédito de contrapartida."
  },
  {
   "id": "umbral:exigencia_de_capital_de_4",
   "type": "Umbral",
   "label": "exigencia de capital de 4%",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Porcentaje que refleja riesgos de divergencia y ejecución en arbitraje índice-canasta."
  },
  {
   "id": "obligacion:exigencia_de_capital_por_riesgo_vega",
   "type": "Obligacion",
   "label": "exigencia de capital por riesgo vega",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La entidad debe calcular la exigencia de capital multiplicando la suma de los coeficientes vega de todas las opciones sobre el mismo subyacente por un cambio de…"
  },
  {
   "id": "obligacion:exigencia_de_capital_por_riesgo_gamma",
   "type": "Obligacion",
   "label": "exigencia de capital por riesgo gamma",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La entidad debe computar la exigencia de capital total por riesgo gamma sumando el valor absoluto de los efectos gamma negativos netos."
  },
  {
   "id": "procedimiento:determinacion_de_exigencia_de_capital",
   "type": "Procedimiento",
   "label": "determinación de exigencia de capital",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Procedimiento de cálculo del requerimiento de capital considerando riesgo direccional y otros riesgos."
  },
  {
   "id": "obligacion:computar_capital_ordinario_de_nivel_uno",
   "type": "Obligacion",
   "label": "computar capital ordinario de nivel uno",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Obligación de las entidades financieras de computar el COn1 incluyendo los rubros del patrimonio neto establecidos, menos los conceptos deducibles."
  }
 ]
}
```

--- paso 11 · buscar_nodos · input={"consulta": "previsión regulatoria incobrabilidad deducción", "limite": 10} · runtime=3277 · re-ejecutado=3277 ---

```json
{
 "consulta": "previsión regulatoria incobrabilidad deducción",
 "total_con_match": 39,
 "resultados": [
  {
   "id": "concepto_definido:prevision_regulatoria_por_riesgo_de_incobrabilidad",
   "type": "ConceptoDefinido",
   "label": "previsión regulatoria por riesgo de incobrabilidad",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Previsión calculada según normas sobre Previsiones Mínimas por Riesgo de Incobrabilidad."
  },
  {
   "id": "concepto_definido:prevision_regulatoria",
   "type": "ConceptoDefinido",
   "label": "previsión regulatoria",
   "tokens_matcheados": 2,
   "resumen_propiedades": "['Importe resultante de la aplicación de normas sobre previsiones mínimas por riesgo de incobrabilidad.', 'Previsión según normas sobre provisiones mínimas por …"
  },
  {
   "id": "concepto_definido:prevision_por_riesgo_de_incobrabilidad",
   "type": "ConceptoDefinido",
   "label": "previsión por riesgo de incobrabilidad",
   "tokens_matcheados": 2,
   "resumen_propiedades": "['Deducción contable para riesgos de incobrabilidad, incluyendo previsiones en pasivo, aplicable a deudores en situación normal y financiaciones con garantías p…"
  },
  {
   "id": "concepto_definido:prevision_por_riesgo_de_incobrabilidad_cartera_situacion_normal",
   "type": "ConceptoDefinido",
   "label": "previsión por riesgo de incobrabilidad cartera situación normal",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Importe de previsión por riesgo de incobrabilidad correspondiente a cartera en situación normal, computado como patrimonio neto complementario."
  },
  {
   "id": "concepto_definido:prevision_contable",
   "type": "ConceptoDefinido",
   "label": "previsión contable",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Previsión contable correspondiente al balance de saldos al 30.11.19 o por aplicación de NIIF 9 punto 5.5 sobre deterioro de valor."
  },
  {
   "id": "concepto_definido:prevision_especifica",
   "type": "ConceptoDefinido",
   "label": "previsión específica",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Provisión contable constituida por la entidad financiera contra una exposición crediticia específica en incumplimiento."
  },
  {
   "id": "concepto_definido:prevision_contable_segun_niif_9",
   "type": "ConceptoDefinido",
   "label": "previsión contable según NIIF 9",
   "tokens_matcheados": 1,
   "resumen_propiedades": "['Previsión calculada según normativa NIIF 9, considerando metodología de prorrateo establecida.', 'Diferencia entre previsión contable conforme punto 5.5 de NI…"
  },
  {
   "id": "umbral:deduccion_inmuebles_sin_registro",
   "type": "Umbral",
   "label": "deducción inmuebles sin registro",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Porcentaje de deducción aplicable a inmuebles sin registro de propiedad desde su incorporación al patrimonio."
  },
  {
   "id": "requisito:deduccion_por_mayor_saldo_mensual",
   "type": "Requisito",
   "label": "deducción por mayor saldo mensual",
   "tokens_matcheados": 1,
   "resumen_propiedades": "La deducción se realiza por el mayor saldo en cada banco del exterior registrado durante el mes de determinación de RPC."
  },
  {
   "id": "concepto_definido:deudor_con_riesgo_de_incobrabilidad",
   "type": "ConceptoDefinido",
   "label": "deudor con riesgo de incobrabilidad",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Deudor clasificado en categoría de riesgo según criterios de flujo de fondos, atrasos e incumplimientos contractuales."
  }
 ]
}
```

--- paso 12 · ver_nodo · input={"id": "concepto_definido:prevision_regulatoria_por_riesgo_de_incobrabilidad"} · runtime=429 · re-ejecutado=429 ---

```json
{
 "id": "concepto_definido:prevision_regulatoria_por_riesgo_de_incobrabilidad",
 "type": "ConceptoDefinido",
 "label": "previsión regulatoria por riesgo de incobrabilidad",
 "properties": {
  "description": "Previsión calculada según normas sobre Previsiones Mínimas por Riesgo de Incobrabilidad.",
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 10 > Punto 11.3"
  }
 ]
}
```

--- paso 13 · ver_vecinos · input={"id": "concepto_definido:prevision_regulatoria_por_riesgo_de_incobrabilidad", "direccion": "ambas"} · runtime=572 · re-ejecutado=572 ---

```json
{
 "id": "concepto_definido:prevision_regulatoria_por_riesgo_de_incobrabilidad",
 "label": "previsión regulatoria por riesgo de incobrabilidad",
 "n_salientes_total": 0,
 "n_entrantes_total": 1,
 "salientes": [],
 "salientes_truncado": false,
 "entrantes": [
  {
   "relation": "usa_concepto",
   "vecino_id": "obligacion:computacion_de_diferencia_positiva_prevision_como_con1",
   "vecino_label": "computación de diferencia positiva previsión como COn1",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Sección 10 > Punto 11.3"
    }
   ]
  }
 ],
 "entrantes_truncado": false
}
```

--- paso 14 · buscar_nodos · input={"consulta": "computación activos riesgo crédito previsión contable regulatoria", "limite": 10} · runtime=3229 · re-ejecutado=3229 ---

```json
{
 "consulta": "computación activos riesgo crédito previsión contable regulatoria",
 "total_con_match": 581,
 "resultados": [
  {
   "id": "concepto_definido:activos_ponderados_por_riesgo_de_credito",
   "type": "ConceptoDefinido",
   "label": "activos ponderados por riesgo de crédito",
   "tokens_matcheados": 3,
   "resumen_propiedades": "['APRc: componente del cálculo de APR determinado conforme a las normas sobre riesgo de crédito.', 'APRc: activos computables ponderados por factores de riesgo …"
  },
  {
   "id": "concepto_definido:activos_ponderados_por_riesgo_de_credito_aprc",
   "type": "ConceptoDefinido",
   "label": "activos ponderados por riesgo de crédito (APRC)",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Suma de valores obtenidos aplicando una expresión que incluye activos con ponderaciones de riesgo, factores de conversión de crédito y componentes de riesgo de …"
  },
  {
   "id": "concepto_definido:prevision_regulatoria_por_riesgo_de_incobrabilidad",
   "type": "ConceptoDefinido",
   "label": "previsión regulatoria por riesgo de incobrabilidad",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Previsión calculada según normas sobre Previsiones Mínimas por Riesgo de Incobrabilidad."
  },
  {
   "id": "obligacion:incremento_de_exigencia_por_riesgo_de_credito_por_exceso_en_activos_inmovilizado",
   "type": "Obligacion",
   "label": "incremento de exigencia por riesgo de crédito por exceso en activos inmovilizados",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Obligación de incrementar la exigencia de capital por riesgo de crédito cuando existe exceso en la relación de activos inmovilizados."
  },
  {
   "id": "concepto_definido:riesgo_de_credito",
   "type": "ConceptoDefinido",
   "label": "riesgo de crédito",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Categoría de riesgo que forma parte del cálculo de la exigencia de capital mínimo total."
  },
  {
   "id": "concepto_definido:prevision_contable",
   "type": "ConceptoDefinido",
   "label": "previsión contable",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Previsión contable correspondiente al balance de saldos al 30.11.19 o por aplicación de NIIF 9 punto 5.5 sobre deterioro de valor."
  },
  {
   "id": "concepto_definido:prevision_regulatoria",
   "type": "ConceptoDefinido",
   "label": "previsión regulatoria",
   "tokens_matcheados": 2,
   "resumen_propiedades": "['Importe resultante de la aplicación de normas sobre previsiones mínimas por riesgo de incobrabilidad.', 'Previsión según normas sobre provisiones mínimas por …"
  },
  {
   "id": "concepto_definido:riesgo_de_credito_cr",
   "type": "ConceptoDefinido",
   "label": "riesgo de crédito (cr)",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La pérdida que ocurriría ante el incumplimiento de la contraparte en el presente o en el futuro, si la liquidación y reposición de las operaciones fueran instan…"
  },
  {
   "id": "umbral:factor_de_riesgo_credito_bb",
   "type": "Umbral",
   "label": "factor de riesgo crédito BB",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Factor de riesgo aplicable a operaciones de crédito con rating BB."
  },
  {
   "id": "concepto_definido:riesgo_de_credito_del_emisor",
   "type": "ConceptoDefinido",
   "label": "riesgo de crédito del emisor",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Concepto regulatorio aplicable a futuros con subyacente en títulos de deuda."
  }
 ]
}
```

--- paso 15 · buscar_nodos · input={"consulta": "activos computables riesgo crédito deducción previsión", "limite": 10} · runtime=3222 · re-ejecutado=3222 ---

```json
{
 "consulta": "activos computables riesgo crédito deducción previsión",
 "total_con_match": 587,
 "resultados": [
  {
   "id": "concepto_definido:activos_ponderados_por_riesgo_de_credito",
   "type": "ConceptoDefinido",
   "label": "activos ponderados por riesgo de crédito",
   "tokens_matcheados": 3,
   "resumen_propiedades": "['APRc: componente del cálculo de APR determinado conforme a las normas sobre riesgo de crédito.', 'APRc: activos computables ponderados por factores de riesgo …"
  },
  {
   "id": "concepto_definido:activos_ponderados_por_riesgo_de_credito_aprc",
   "type": "ConceptoDefinido",
   "label": "activos ponderados por riesgo de crédito (APRC)",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Suma de valores obtenidos aplicando una expresión que incluye activos con ponderaciones de riesgo, factores de conversión de crédito y componentes de riesgo de …"
  },
  {
   "id": "requisito:deduccion_de_ajustes_de_valuacion_por_riesgo_de_credito_propio",
   "type": "Requisito",
   "label": "deducción de ajustes de valuación por riesgo de crédito propio",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Se deducen exclusivamente los ajustes de valuación por el riesgo de crédito propio de la entidad financiera, sin compensación con riesgo de crédito de la contra…"
  },
  {
   "id": "obligacion:incremento_de_exigencia_por_riesgo_de_credito_por_exceso_en_activos_inmovilizado",
   "type": "Obligacion",
   "label": "incremento de exigencia por riesgo de crédito por exceso en activos inmovilizados",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Obligación de incrementar la exigencia de capital por riesgo de crédito cuando existe exceso en la relación de activos inmovilizados."
  },
  {
   "id": "concepto_definido:riesgo_de_credito",
   "type": "ConceptoDefinido",
   "label": "riesgo de crédito",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Categoría de riesgo que forma parte del cálculo de la exigencia de capital mínimo total."
  },
  {
   "id": "concepto_definido:riesgo_de_credito_cr",
   "type": "ConceptoDefinido",
   "label": "riesgo de crédito (cr)",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La pérdida que ocurriría ante el incumplimiento de la contraparte en el presente o en el futuro, si la liquidación y reposición de las operaciones fueran instan…"
  },
  {
   "id": "umbral:factor_de_riesgo_credito_bb",
   "type": "Umbral",
   "label": "factor de riesgo crédito BB",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Factor de riesgo aplicable a operaciones de crédito con rating BB."
  },
  {
   "id": "concepto_definido:riesgo_de_credito_del_emisor",
   "type": "ConceptoDefinido",
   "label": "riesgo de crédito del emisor",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Concepto regulatorio aplicable a futuros con subyacente en títulos de deuda."
  },
  {
   "id": "concepto_definido:riesgo_de_credito_sustancial",
   "type": "ConceptoDefinido",
   "label": "riesgo de crédito sustancial",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Riesgo evaluado en entidades financieras cuya capacidad de pago depende de condiciones económicas o de negocio favorables o estables."
  },
  {
   "id": "umbral:factor_de_riesgo_credito_aaa",
   "type": "Umbral",
   "label": "factor de riesgo crédito AAA",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Factor de riesgo aplicable a operaciones de crédito con rating AAA."
  }
 ]
}
```

---

# Sección 3 — run_2/CQ-025

## 3a. Respuesta final del agente (verbatim, `posthoc_run/traces/off/run_2/CQ-025.json`)

`trace.final_json`:

```json
{
 "respuesta": "En el Régimen Informativo de Capitales Mínimos, la exigencia por riesgo de mercado se informa con frecuencia mensual (para posiciones del último día del mes), mientras que la información sobre el ratio de apalancamiento se informa con frecuencia trimestral (con datos del mes de cierre de trimestre).",
 "citas": [
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Sección 7 > Punto 8.1"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Sección 12 > Punto 12.4"
  }
 ],
 "respondible": true
}
```

`trace.final_raw` (turno final íntegro):

```
Tengo la información necesaria. Basándome en lo que encontré en el Knowledge Graph:

- **Exigencia por riesgo de mercado**: Se informa con **frecuencia mensual** (para posiciones del último día del mes)
- **Ratio de apalancamiento**: Se informa con **frecuencia trimestral** (con datos del mes de cierre de trimestre)

```json
{
  "respuesta": "En el Régimen Informativo de Capitales Mínimos, la exigencia por riesgo de mercado se informa con frecuencia mensual (para posiciones del último día del mes), mientras que la información sobre el ratio de apalancamiento se informa con frecuencia trimestral (con datos del mes de cierre de trimestre).",
  "citas": [
    {
      "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
      "location": "Sección 7 > Punto 8.1"
    },
    {
      "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
      "location": "Sección 12 > Punto 12.4"
    }
  ],
  "respondible": true
}
```
```

## 3b. Inventario de pasos (runtime vs. almacenado vs. re-ejecutado)

| paso | tool | input | chars runtime | chars almacenados | re-ejecutado |
|---|---|---|---|---|---|
| 1 | buscar_nodos | `{"consulta": "Régimen Informativo Capitales Mínimos", "limite": 10}` | 3508 | 1215 | = runtime ✓ |
| 2 | buscar_nodos | `{"consulta": "riesgo de mercado frecuencia informe", "limite": 10}` | 3242 | 1215 | = runtime ✓ |
| 3 | buscar_nodos | `{"consulta": "ratio apalancamiento frecuencia reporte", "limite": 10}` | 3440 | 1215 | = runtime ✓ |
| 4 | ver_nodo | `{"id": "obligacion:informar_exigencia_por_riesgo_de_mercado"}` | 477 | 477 | = runtime ✓ |
| 5 | ver_nodo | `{"id": "obligacion:mantenimiento_de_frecuencia_trimestral_del_ratio_de_apalancamiento"}` | 572 | 572 | = runtime ✓ |
| 6 | ver_nodo | `{"id": "procedimiento:regimen_informativo_sobre_exigencia_e_integracion_de_capitales_minimos"}` | 509 | 509 | = runtime ✓ |
| 7 | ver_vecinos | `{"id": "obligacion:informar_exigencia_por_riesgo_de_mercado"}` | 596 | 596 | = runtime ✓ |

**Fidelidad runtime↔re-ejecución: 7/7 pasos con largo idéntico.**

## 3c. APÉNDICE — outputs completos re-ejecutados (7 pasos)


--- paso 1 · buscar_nodos · input={"consulta": "Régimen Informativo Capitales Mínimos", "limite": 10} · runtime=3508 · re-ejecutado=3508 ---

```json
{
 "consulta": "Régimen Informativo Capitales Mínimos",
 "total_con_match": 77,
 "resultados": [
  {
   "id": "procedimiento:regimen_informativo_exigencia_e_integracion_de_capitales_minimos",
   "type": "Procedimiento",
   "label": "régimen informativo exigencia e integración de capitales mínimos",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Procedimiento que contiene nómina de partidas e instrucciones para determinación de exigencias en partidas 70810000 y 70820000."
  },
  {
   "id": "procedimiento:regimen_informativo_sobre_exigencia_e_integracion_de_capitales_minimos",
   "type": "Procedimiento",
   "label": "régimen informativo sobre exigencia e integración de capitales mínimos",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Procedimiento mediante el cual se establece y supervisa la exigencia e integración de capitales mínimos en entidades financieras."
  },
  {
   "id": "norma_referenciada:regimen_informativo_para_supervision",
   "type": "NormaReferenciada",
   "label": "Régimen Informativo para Supervisión",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Norma que establece los vencimientos de presentación de información regulatoria."
  },
  {
   "id": "procedimiento:regimen_informativo_contable_mensual",
   "type": "Procedimiento",
   "label": "régimen informativo contable mensual",
   "tokens_matcheados": 2,
   "resumen_propiedades": "['Procedimiento de información mensual sobre exigencia e integración de capitales mínimos bajo el Régimen Informativo Contable Mensual (R.I.-C.M.).', 'Proceso d…"
  },
  {
   "id": "umbral:5_de_exigencia_de_capitales_minimos",
   "type": "Umbral",
   "label": "5% de exigencia de capitales mínimos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Umbral que activa restricción de crecimiento de pasivos cuando se supera en incrementos de exigencia por riesgo de crédito."
  },
  {
   "id": "procedimiento:consulta_en_regimen_informativo_sepaimpo",
   "type": "Procedimiento",
   "label": "consulta en régimen informativo SEPAIMPO",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Las entidades deben consultar en el apartado de Régimen Informativo SEPAIMPO del sitio www3.bcra.gob.ar para verificar antecedentes penales del cliente."
  },
  {
   "id": "concepto_definido:capitales_minimos_de_entidades_financieras",
   "type": "ConceptoDefinido",
   "label": "capitales mínimos de entidades financieras",
   "tokens_matcheados": 2,
   "resumen_propiedades": "['Concepto regulatorio que establece los requisitos de capital que las entidades financieras deben mantener.', 'Requerimiento regulatorio sobre el nivel mínimo …"
  },
  {
   "id": "obligacion:reduccion_de_exigencia_de_capitales_minimos",
   "type": "Obligacion",
   "label": "reducción de exigencia de capitales mínimos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Reducción de exigencia de capitales mínimos para entidades de los Grupos A, B y C, código 3600000Y."
  },
  {
   "id": "concepto_definido:exigencia_e_integracion_de_capitales_minimos",
   "type": "ConceptoDefinido",
   "label": "exigencia e integración de capitales mínimos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "['Concepto regulatorio que designa los requisitos de capital mínimo que las entidades financieras deben mantener conforme al régimen informativo contable mensua…"
  },
  {
   "id": "procedimiento:exigencia_e_integracion_de_capitales_minimos",
   "type": "Procedimiento",
   "label": "exigencia e integración de capitales mínimos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "['Régimen informativo contable mensual que requiere el cálculo y reporte de capitales mínimos conforme a las partidas y ponderadores especificados.', 'Procedimi…"
  }
 ]
}
```

--- paso 2 · buscar_nodos · input={"consulta": "riesgo de mercado frecuencia informe", "limite": 10} · runtime=3242 · re-ejecutado=3242 ---

```json
{
 "consulta": "riesgo de mercado frecuencia informe",
 "total_con_match": 3774,
 "resultados": [
  {
   "id": "concepto_definido:riesgo_de_mercado",
   "type": "ConceptoDefinido",
   "label": "riesgo de mercado",
   "tokens_matcheados": 3,
   "resumen_propiedades": "['Riesgo determinado por las posiciones diarias de activos comprendidos, componente de la exigencia de capital mínimo.', 'Posibilidad de sufrir pérdidas en posi…"
  },
  {
   "id": "concepto_definido:riesgo_general_de_mercado",
   "type": "ConceptoDefinido",
   "label": "riesgo general de mercado",
   "tokens_matcheados": 3,
   "resumen_propiedades": "['Componente de riesgo de mercado capturado separadamente por el Método de Medición Estándar.', 'Riesgo vinculado al efecto de cambios en la tasa de interés sob…"
  },
  {
   "id": "concepto_definido:exigencia_por_riesgo_de_mercado",
   "type": "ConceptoDefinido",
   "label": "exigencia por riesgo de mercado",
   "tokens_matcheados": 3,
   "resumen_propiedades": "['RM: componente del cálculo de APR que refleja el riesgo de mercado.', 'Importe que representa el requerimiento de capital mínimo por exposición al riesgo de m…"
  },
  {
   "id": "obligacion:informar_exigencia_por_riesgo_de_mercado",
   "type": "Obligacion",
   "label": "informar exigencia por riesgo de mercado",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Obligación de informar exigencia según riesgo de mercado para posiciones del último día del mes, calculada según punto 4.1.1."
  },
  {
   "id": "obligacion:determinar_exigencia_por_riesgo_de_mercado",
   "type": "Obligacion",
   "label": "determinar exigencia por riesgo de mercado",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Obligación de determinar la exigencia por riesgo de mercado con los valores registrados al último día del período de información, mediante suma de códigos espec…"
  },
  {
   "id": "obligacion:exigencia_de_capital_por_riesgo_de_mercado",
   "type": "Obligacion",
   "label": "exigencia de capital por riesgo de mercado",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Suma aritmética de exigencias de capital por riesgos de tasa de interés, acciones, tipo de cambio, productos básicos y opciones."
  },
  {
   "id": "umbral:8_por_riesgo_especifico_y_general_de_mercado",
   "type": "Umbral",
   "label": "8% por riesgo específico y general de mercado",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Exigencia de capital equivalente al 8% de cada riesgo (específico y general de mercado)."
  },
  {
   "id": "obligacion:envio_mensual_de_datos_sobre_riesgo_de_mercado",
   "type": "Obligacion",
   "label": "envío mensual de datos sobre riesgo de mercado",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Complementar información con envío mensual de datos según riesgo considerado."
  },
  {
   "id": "requisito:exigencia_por_riesgo_de_mercado_codigo_70800000",
   "type": "Requisito",
   "label": "exigencia por riesgo de mercado código 70800000",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Exigencia por riesgo de mercado para posiciones del último día del mes, código 70800000."
  },
  {
   "id": "concepto_definido:exigencia_de_capital_minimo_por_riesgo_de_mercado",
   "type": "ConceptoDefinido",
   "label": "exigencia de capital mínimo por riesgo de mercado",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Magnitud de capital regulatorio que las entidades deben mantener por exposición a riesgo de mercado."
  }
 ]
}
```

--- paso 3 · buscar_nodos · input={"consulta": "ratio apalancamiento frecuencia reporte", "limite": 10} · runtime=3440 · re-ejecutado=3440 ---

```json
{
 "consulta": "ratio apalancamiento frecuencia reporte",
 "total_con_match": 39,
 "resultados": [
  {
   "id": "obligacion:reporte_del_ratio_de_apalancamiento_con_codigo_de_consolidacion_3",
   "type": "Obligacion",
   "label": "reporte del Ratio de apalancamiento con código de consolidación 3",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Se continuará informando código de consolidación 3 para el Ratio de apalancamiento, pero las operaciones a incluir serán las del perímetro de consolidación mens…"
  },
  {
   "id": "obligacion:mantenimiento_de_frecuencia_trimestral_del_ratio_de_apalancamiento",
   "type": "Obligacion",
   "label": "mantenimiento de frecuencia trimestral del Ratio de apalancamiento",
   "tokens_matcheados": 3,
   "resumen_propiedades": "El Ratio de apalancamiento mantendrá su frecuencia trimestral con datos del mes de cierre de trimestre y su vencimiento según el Régimen Informativo para Superv…"
  },
  {
   "id": "concepto_definido:ratio_de_apalancamiento",
   "type": "ConceptoDefinido",
   "label": "ratio de apalancamiento",
   "tokens_matcheados": 2,
   "resumen_propiedades": "['Medida regulatoria presentada en base individual con códigos de consolidación 0 o 1.', 'Ratio calculado como [Medida del capital / Medida de la exposición] * …"
  },
  {
   "id": "procedimiento:calculo_del_ratio_de_apalancamiento",
   "type": "Procedimiento",
   "label": "cálculo del ratio de apalancamiento",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Procedimiento que aplica la expresión [Medida del capital / Medida de la exposición] * 100 según las normas sobre Ratio de apalancamiento."
  },
  {
   "id": "norma_referenciada:normas_sobre_ratio_de_apalancamiento",
   "type": "NormaReferenciada",
   "label": "normas sobre Ratio de apalancamiento",
   "tokens_matcheados": 2,
   "resumen_propiedades": "['Norma externa que define el modelo de información y la fórmula de cálculo del ratio de apalancamiento.', 'Norma que establece los puntos 2.1, 2.2.1, 2.2.2, 2.…"
  },
  {
   "id": "obligacion:informar_ratio_de_apalancamiento_y_sus_componentes",
   "type": "Obligacion",
   "label": "informar ratio de apalancamiento y sus componentes",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Se informará el ratio de apalancamiento y sus componentes según el modelo de información previsto en el punto 10.2."
  },
  {
   "id": "obligacion:presentacion_trimestral_de_ratio_de_apalancamiento",
   "type": "Obligacion",
   "label": "presentación trimestral de ratio de apalancamiento",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Información sobre Ratio de apalancamiento en base individual se presentará con datos del último mes de cada trimestre."
  },
  {
   "id": "concepto_definido:apalancamiento",
   "type": "ConceptoDefinido",
   "label": "apalancamiento",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Cociente entre el total de los activos (A) respecto del patrimonio neto (PN) del fideicomiso, calculado como A / PN."
  },
  {
   "id": "procedimiento:reporte_en_sepaimpo",
   "type": "Procedimiento",
   "label": "reporte en SEPAIMPO",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Procedimiento de reporte al BCRA mediante el cual la entidad comunica certificaciones, circunstancias modificatorias y cambios de entidad responsable."
  },
  {
   "id": "concepto_definido:ratio_de_concentracion",
   "type": "ConceptoDefinido",
   "label": "ratio de concentración",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Suma de valores nominales de todos los tramos dividida por suma de valores nominales de tramos subordinados o pari passu con el tramo de la posición."
  }
 ]
}
```

--- paso 4 · ver_nodo · input={"id": "obligacion:informar_exigencia_por_riesgo_de_mercado"} · runtime=477 · re-ejecutado=477 ---

```json
{
 "id": "obligacion:informar_exigencia_por_riesgo_de_mercado",
 "type": "Obligacion",
 "label": "informar exigencia por riesgo de mercado",
 "properties": {
  "description": "Obligación de informar exigencia según riesgo de mercado para posiciones del último día del mes, calculada según punto 4.1.1.",
  "modalidad": "obligacion",
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Sección 7 > Punto 8.1"
  }
 ]
}
```

--- paso 5 · ver_nodo · input={"id": "obligacion:mantenimiento_de_frecuencia_trimestral_del_ratio_de_apalancamiento"} · runtime=572 · re-ejecutado=572 ---

```json
{
 "id": "obligacion:mantenimiento_de_frecuencia_trimestral_del_ratio_de_apalancamiento",
 "type": "Obligacion",
 "label": "mantenimiento de frecuencia trimestral del Ratio de apalancamiento",
 "properties": {
  "description": "El Ratio de apalancamiento mantendrá su frecuencia trimestral con datos del mes de cierre de trimestre y su vencimiento según el Régimen Informativo para Supervisión.",
  "modalidad": "obligacion",
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Sección 12 > Punto 12.4"
  }
 ]
}
```

--- paso 6 · ver_nodo · input={"id": "procedimiento:regimen_informativo_sobre_exigencia_e_integracion_de_capitales_minimos"} · runtime=509 · re-ejecutado=509 ---

```json
{
 "id": "procedimiento:regimen_informativo_sobre_exigencia_e_integracion_de_capitales_minimos",
 "type": "Procedimiento",
 "label": "régimen informativo sobre exigencia e integración de capitales mínimos",
 "properties": {
  "description": "Procedimiento mediante el cual se establece y supervisa la exigencia e integración de capitales mínimos en entidades financieras.",
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Encabezado"
  }
 ]
}
```

--- paso 7 · ver_vecinos · input={"id": "obligacion:informar_exigencia_por_riesgo_de_mercado"} · runtime=596 · re-ejecutado=596 ---

```json
{
 "id": "obligacion:informar_exigencia_por_riesgo_de_mercado",
 "label": "informar exigencia por riesgo de mercado",
 "n_salientes_total": 1,
 "n_entrantes_total": 0,
 "salientes": [
  {
   "relation": "referencia",
   "vecino_id": "norma_referenciada:lineamientos_para_la_gestion_de_riesgos_en_las_entidades_financieras",
   "vecino_label": "Lineamientos para la Gestión de Riesgos en las Entidades Financieras",
   "provenances": [
    {
     "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
     "location": "Sección 7 > Punto 8.1"
    }
   ]
  }
 ],
 "salientes_truncado": false,
 "entrantes": [],
 "entrantes_truncado": false
}
```
