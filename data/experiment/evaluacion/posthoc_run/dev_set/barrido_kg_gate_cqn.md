# Barrido de verificación sobre kg.json de run_3 — condicionales del gate CQN

SOLO LECTURA; única escritura: este informe. Ni verificador ni S1 corrieron (sellado
por inexistencia vigente). Mecanismo: (a) existencia = búsqueda por campo sobre el kg
congelado cargado vía loader (match por substring normalizado lowercase/sin acentos,
campo indicado por hit); (b) ranking/D1 = `buscar_nodos` REAL del harness (misma
tokenización e índice label+id del runtime), con el límite verbatim de la traza y,
como diagnóstico, la posición global con la MISMA función y límite 10000; (c) consultas
VERBATIM de las trazas del gate (caso y paso citados); (d) hechos, sin interpretación.


## K1 (CQN-001) — ¿'USD 200'/'doscientos' junto a 'mes calendario', o provenance Punto 3.9 Exterior?

Predicados: (contiene 'usd 200' O 'doscientos') Y (contiene 'mes calendario') sobre el
MISMO campo; aparte, provenance con 'exterior' y regex `3\.9` (guarda de dígitos).

Hits por contenido: 0 · hits por provenance 3.9-Exterior: 1

### Comunicacion_a_6796 — matchea en: ['provenances[0]']

```json
{
 "id": "Comunicacion_a_6796",
 "type": "Comunicacion",
 "label": "Com. A 6796",
 "properties": {
  "codigo": "A-6796",
  "tipo": "A",
  "numero": "6796"
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 3.9. A 6770 6."
  }
 ]
}
```

**VEREDICTO K1:** EXISTEN 1 candidato(s): ['Comunicacion_a_6796']


## K2 (CQN-001) — nodos completos de los dos ids pedidos

### Restriccion_limite_mensual_de_compra_en_efectivo (match exacto)

```json
{
 "id": "Restriccion_limite_mensual_de_compra_en_efectivo",
 "type": "Restriccion",
 "label": "Límite mensual de compra en efectivo",
 "properties": {
  "tipo": "limite_cuantitativo",
  "umbral": "USD 100",
  "description": "Si el cliente utiliza efectivo el monto comprado por el cliente no supere el equivalente a USD 100 (dólares estadounidenses cien) en el mes calendario en el conjunto de las entidades y por el conjunto de los conceptos señalados."
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 3.8. Compra de moneda extranjera por parte de personas humanas residentes para la for"
  }
 ]
}
```

### Restriccion_limite_anual_usd_36_000_para_personas_humanas (match exacto)

```json
{
 "id": "Restriccion_limite_anual_usd_36_000_para_personas_humanas",
 "type": "Restriccion",
 "label": "Límite anual USD 36.000 para personas humanas",
 "properties": {
  "tipo": "limite_cuantitativo",
  "umbral": "USD 36.000 anuales",
  "description": "El cliente no ha utilizado este mecanismo por un monto superior al equivalente de USD 36.000 (dólares estadounidenses treinta y seis mil) en el año calendario, en el conjunto de las entidades y por el conjunto de los conceptos comprendidos"
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 2.2. Cobros de exportaciones de servicios. (parte 1)"
  }
 ]
}
```

**VEREDICTO K2:** Restriccion_limite_mensual_de_compra_en_efectivo: existe; Restriccion_limite_anual_usd_36_000_para_personas_humanas: existe


## K3 (CQN-001) — D1/ranking de los candidatos de K1 bajo las consultas verbatim (pasos 1, 8, 9)


**paso 1** — consulta verbatim: `monto máximo persona humana residente compra activos externos` · límite runtime: 10
  - Comunicacion_a_6796: NO aparece en el top-10 · posición global — de 50 (límite 10000)

**paso 8** — consulta verbatim: `límite mensual persona humana residente sin conformidad` · límite runtime: 10
  - Comunicacion_a_6796: NO aparece en el top-10 · posición global — de 50 (límite 10000)

**paso 9** — consulta verbatim: `formación activos externos persona humana límite` · límite runtime: 10
  - Comunicacion_a_6796: NO aparece en el top-10 · posición global — de 50 (límite 10000)

**VEREDICTO K3:** posiciones arriba, por consulta.


## K4 (CQN-001) — vecindad completa de Restriccion_limite_mensual_de_compra_en_efectivo

(match exacto; `ver_vecinos` REAL del harness)

```json
{
 "id": "Restriccion_limite_mensual_de_compra_en_efectivo",
 "label": "Límite mensual de compra en efectivo",
 "n_salientes_total": 3,
 "n_entrantes_total": 0,
 "salientes": [
  {
   "relation": "establecida_en",
   "vecino_id": "TextoOrdenado_to_exterior_cambios_actual_pdf",
   "vecino_label": "Exterior y Cambios",
   "provenances": [
    {
     "source_doc": "TO_exterior_cambios_actual.pdf",
     "location": "Punto 3.8. Compra de moneda extranjera por parte de personas humanas residentes para la for"
    }
   ]
  },
  {
   "relation": "aplica_a",
   "vecino_id": "EntidadFinanciera_sujeto_obligado",
   "vecino_label": "Sujetos obligados",
   "provenances": [
    {
     "source_doc": "TO_exterior_cambios_actual.pdf",
     "location": "Punto 3.8. Compra de moneda extranjera por parte de personas humanas residentes para la for"
    }
   ]
  },
  {
   "relation": "limita",
   "vecino_id": "Operacion_compra_de_moneda_extranjera",
   "vecino_label": "Compra de moneda extranjera",
   "provenances": [
    {
     "source_doc": "TO_exterior_cambios_actual.pdf",
     "location": "Punto 3.8. Compra de moneda extranjera por parte de personas humanas residentes para la for"
    }
   ]
  }
 ],
 "salientes_truncado": false,
 "entrantes": [],
 "entrantes_truncado": false
}
```

**VEREDICTO K4:** 3 salientes, 0 entrantes.


## K5 (CQN-007) — nodo completo Restriccion_limitacion_eve_sobre_capital_nivel_1

(match exacto)

```json
{
 "id": "Restriccion_limitacion_eve_sobre_capital_nivel_1",
 "type": "Restriccion",
 "label": "Limitación EVE sobre capital nivel 1",
 "properties": {
  "tipo": "limite_cuantitativo",
  "umbral": "15%",
  "description": "Cuando esta medida supere el 15 % del nivel de capital 1, se identificará a la entidad como una 'entidad atípica' y la SEFyC podrá exigirle la adopción de medidas específicas"
 },
 "provenances": [
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Punto 8.1. Normas de procedimiento."
  }
 ]
}
```
**VEREDICTO K5:** existe.


## K6 (CQN-007) — ¿otros nodos con 'atipica' o ('15' y 'capital') en description/properties?

Predicado sobre properties SOLAMENTE (no label/id): 'atipica' O ('15' Y 'capital').

Hits: 8

### Restriccion_exposiciones_a_instrumentos_deuda_subordinada_e_instrumentos_de_capital_que_no_r — matchea en: ['properties.descripcion']

```json
{
 "id": "Restriccion_exposiciones_a_instrumentos_deuda_subordinada_e_instrumentos_de_capital_que_no_r",
 "type": "Restriccion",
 "label": "Ponderador deuda subordinada grupo 1",
 "properties": {
  "descripcion": "Exposiciones a instrumentos: Deuda subordinada e instrumentos de capital que no reúnen las características para ser considerados como acciones: 150",
  "tipo": "limite_cuantitativo",
  "umbral": "150"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Punto 2.12. Tabla de ponderadores de riesgo. (parte 2)"
  }
 ]
}
```

### Restriccion_participacion_en_el_capital_de_cada_empresa_15 — matchea en: ['properties.descripcion']

```json
{
 "id": "Restriccion_participacion_en_el_capital_de_cada_empresa_15",
 "type": "Restriccion",
 "label": "Límite de participación por empresa",
 "properties": {
  "descripcion": "participación en el capital de cada empresa: 15%",
  "tipo": "limite_cuantitativo",
  "umbral": "15%"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Punto 4.1. DvP: operaciones de entrega contra pago fallidas (a los efectos de estas normas,"
  }
 ]
}
```

### Restriccion_requerimiento_de_capital_por_riesgo_direccional — matchea en: ['properties.description']

```json
{
 "id": "Restriccion_requerimiento_de_capital_por_riesgo_direccional",
 "type": "Restriccion",
 "label": "Requerimiento de capital por riesgo direccional",
 "properties": {
  "tipo": "limite_cuantitativo",
  "umbral": "15%",
  "description": "Por riesgo direccional: el requerimiento de capital será el 15% de la posición neta, ya sea corta o larga, en cada producto básico"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Punto 6.5. Exigencia de capital por riesgo de posiciones en productos básicos –“commodities"
  }
 ]
}
```

### Obligacion_se_determinara_mensualmente_aplicando_la_siguiente_expresion_c_ro_max_ib_t_12_50 — matchea en: ['properties.descripcion']

```json
{
 "id": "Obligacion_se_determinara_mensualmente_aplicando_la_siguiente_expresion_c_ro_max_ib_t_12_50",
 "type": "Obligacion",
 "label": "Determinar mensualmente exigencia capital operacional",
 "properties": {
  "descripcion": "Se determinará mensualmente aplicando la siguiente expresión: C_RO = máx(IB_t/12.500, K_0) donde C_RO es exigencia de capital por riesgo operacional, con parámetro α = 15%.",
  "tipo": "calculo",
  "plazo": "mensual"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Punto 7.2. Exigencia de capital por riesgo operacional para entidades del grupo 2."
  }
 ]
}
```

### Obligacion_para_financiaciones_de_pago_unico_o_periodos_superiores_a_bimestral_deudor_debe_ — matchea en: ['properties.descripcion']

```json
{
 "id": "Obligacion_para_financiaciones_de_pago_unico_o_periodos_superiores_a_bimestral_deudor_debe_",
 "type": "Obligacion",
 "label": "Cancelación de porcentaje para reclasificación",
 "properties": {
  "tipo": "otra",
  "descripcion": "Para financiaciones de pago único o períodos superiores a bimestral, deudor debe cancelar al menos 10% o 15% de obligaciones refinanciadas por capital",
  "plazo": "según tipo de financiación"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Punto 7.2. Niveles de clasificación. (parte 2)"
  }
 ]
}
```

### Restriccion_participacion_en_capital_de_cada_empresa_no_podra_exceder_el_15 — matchea en: ['properties.descripcion']

```json
{
 "id": "Restriccion_participacion_en_capital_de_cada_empresa_no_podra_exceder_el_15",
 "type": "Restriccion",
 "label": "Límite de participación en capital de empresa",
 "properties": {
  "tipo": "limite_cuantitativo",
  "descripcion": "Participación en capital de cada empresa no podrá exceder el 15%",
  "umbral": "15%"
 },
 "provenances": [
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Punto 3.1. Normas de procedimiento. (parte 1)"
  }
 ]
}
```

### Restriccion_cargo_de_capital_escalonado_segun_dias_habiles_posteriores_a_liquidacion — matchea en: ['properties.description']

```json
{
 "id": "Restriccion_cargo_de_capital_escalonado_segun_dias_habiles_posteriores_a_liquidacion",
 "type": "Restriccion",
 "label": "Cargo de capital por DvP fallidas",
 "properties": {
  "tipo": "limite_cuantitativo",
  "descripcion": "Cargo de capital escalonado según días hábiles posteriores a liquidación",
  "description": "Las operaciones con entrega contra pago tendrán un cargo directo de capital cuando los pagos no se realicen dentro de los cinco días hábiles. El cargo varía: 8% (5-15 días), 50% (16-30 días), 75% (31-45 días), 100% (46+ días)"
 },
 "provenances": [
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Punto 3.1. Normas de procedimiento. (parte 2)"
  }
 ]
}
```

### Obligacion_consignar_cargo_adicional_capital_agricola — matchea en: ['properties.description']

```json
{
 "id": "Obligacion_consignar_cargo_adicional_capital_agricola",
 "type": "Obligacion",
 "label": "Consignar cargo adicional capital agrícola",
 "properties": {
  "tipo": "presentacion_informativa",
  "description": "En el código 15000000 se consignará el cargo adicional de capital resultante de la diferencia entre lo registrado según lo señalado en el apartado anterior y el que resulte de aplicar a dicho importe el factor 4"
 },
 "provenances": [
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Punto 3.1. Normas de procedimiento. (parte 2)"
  }
 ]
}
```

**VEREDICTO K6:** 8 nodo(s) además del de K5.


## K7 (CQN-008, ilustrativo) — ¿el mandato del 10.1 de Clasificación?

Predicados: ('consumo o vivienda' Y 'mora') en un campo; O ('recategorizacion' o regex 7.3)
junto a 'tarjeta'/'proveedor'/'emisora'; O provenance con 'clasificacion' y regex 10.1.

Hits: 7

### Operacion_clasificacion_de_deudor — matchea en: ['properties.description [consumo+mora]']

```json
{
 "id": "Operacion_clasificacion_de_deudor",
 "type": "Operacion",
 "label": "Evaluación grado de inversión",
 "properties": {
  "tipo": "clasificacion de deudor",
  "description": "Clasificar a los respectivos deudores en función de su mora, según los criterios aplicables para la cartera de consumo o vivienda"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Punto 2.7. Exposiciones a empresas."
  }
 ]
}
```

### EntidadFinanciera_proveedor_no_financiero_de_credito — matchea en: ['provenances[0] [prov 10.1]']

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

### Obligacion_clasificar_deudores_por_mora — matchea en: ['properties.description [consumo+mora]', 'provenances[0] [prov 10.1]']

```json
{
 "id": "Obligacion_clasificar_deudores_por_mora",
 "type": "Obligacion",
 "label": "Clasificar deudores por mora",
 "properties": {
  "tipo": "calculo",
  "plazo": "aplicación de disposiciones en punto 7.3",
  "description": "Deberán clasificar a los respectivos deudores en función de su mora, según los criterios aplicables para la cartera de consumo o vivienda y por aplicación de las disposiciones previstas en el punto 7.3"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Punto 10.1. Proveedores no financieros de crédito."
  }
 ]
}
```

### Obligacion_clasificar_mipymes_por_mora — matchea en: ['properties.description [consumo+mora]']

```json
{
 "id": "Obligacion_clasificar_mipymes_por_mora",
 "type": "Obligacion",
 "label": "Clasificar MiPyMEs por mora",
 "properties": {
  "tipo": "asignacion",
  "description": "Deberán clasificar a las MiPyMEs cuyas deudas hayan sido canceladas en cumplimiento de las garantías que respaldaban las respectivas obligaciones. La clasificación se realizará en función de la mora, según los criterios aplicables para la cartera de consumo o vivienda y por aplicación de las disposiciones previstas en el punto 7.3. (reclasificación obligatoria)"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Punto 10.3. Sociedades de garantía recíproca y fondos de garantía de carácter público."
  }
 ]
}
```

### Obligacion_clasificar_deudores_segun_mora — matchea en: ['properties.description [consumo+mora]']

```json
{
 "id": "Obligacion_clasificar_deudores_segun_mora",
 "type": "Obligacion",
 "label": "Clasificar deudores según mora",
 "properties": {
  "tipo": "asignacion",
  "description": "Los PSCPP deberán clasificar a los deudores de los créditos que administran en función de su mora, según los criterios aplicables para la cartera de consumo o vivienda y por aplicación de las disposiciones previstas en el punto 7.3. (recategorización obligatoria)",
  "plazo": "obligatoria"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Punto 10.4. Proveedores de servicios de créditos entre particulares a través de plataformas."
  }
 ]
}
```

### Operacion_recategorizacion_de_deudor — matchea en: ['properties.description [recateg/7.3+sujeto]']

```json
{
 "id": "Operacion_recategorizacion_de_deudor",
 "type": "Operacion",
 "label": "Recategorización de deudor",
 "properties": {
  "tipo": "recategorización de deudor",
  "description": "Recategorización al deudor cuando exista discrepancia de más de un nivel entre la clasificación dada por la entidad financiera y las otorgadas por al menos otras dos entidades o fideicomisos financieros o entidades no financieras emisoras de tarjetas de crédito"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Punto 7.3. Recategorización obligatoria."
  }
 ]
}
```

### EntidadFinanciera_empresa_no_financiera_emisora — matchea en: ['provenances[1] [prov 10.1]']

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

**VEREDICTO K7:** 7 hit(s) según predicados.


## K8 (CQN-009) — ¿'70700000' / 'total de control' / ('capital minimo basico' con prov RI) / prov 8.1.3?


Hits: 2

### Operacion_calculo_de_riesgo_de_tasa_de_interes — matchea en: ['properties.description [total de control]']

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

### Obligacion_informar_riesgo_tasa_interes_eve — matchea en: ['properties.description [total de control]']

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

**VEREDICTO K8:** 2 candidato(s): ['Operacion_calculo_de_riesgo_de_tasa_de_interes', 'Obligacion_informar_riesgo_tasa_interes_eve']


## K9 (CQN-009) — ranking de los candidatos de K8 (consultas verbatim pasos 2,3,7,9,13,14,15)


**paso 2** — `total de control capital mínimo banco` · límite 10
  - Operacion_calculo_de_riesgo_de_tasa_de_interes: NO aparece en el top-10 · global — de 50
  - Obligacion_informar_riesgo_tasa_interes_eve: NO aparece en el top-10 · global — de 50

**paso 3** — `régimen informativo capital mínimo total control` · límite 10
  - Operacion_calculo_de_riesgo_de_tasa_de_interes: NO aparece en el top-10 · global — de 50
  - Obligacion_informar_riesgo_tasa_interes_eve: NO aparece en el top-10 · global — de 50

**paso 7** — `total de control importe consignar banco` · límite 10
  - Operacion_calculo_de_riesgo_de_tasa_de_interes: NO aparece en el top-10 · global — de 50
  - Obligacion_informar_riesgo_tasa_interes_eve: NO aparece en el top-10 · global — de 50

**paso 9** — `total control reporte información capital` · límite 10
  - Operacion_calculo_de_riesgo_de_tasa_de_interes: NO aparece en el top-10 · global — de 50
  - Obligacion_informar_riesgo_tasa_interes_eve: NO aparece en el top-10 · global — de 50

**paso 13** — `total de control capital mínimo básico banco` · límite 15
  - Operacion_calculo_de_riesgo_de_tasa_de_interes: NO aparece en el top-15 · global — de 50
  - Obligacion_informar_riesgo_tasa_interes_eve: NO aparece en el top-15 · global — de 50

**paso 14** — `total control 5000 millones` · límite 10
  - Operacion_calculo_de_riesgo_de_tasa_de_interes: NO aparece en el top-10 · global — de 45
  - Obligacion_informar_riesgo_tasa_interes_eve: NO aparece en el top-10 · global — de 45

**paso 15** — `consignar total control exigencia capital` · límite 10
  - Operacion_calculo_de_riesgo_de_tasa_de_interes: NO aparece en el top-10 · global — de 50
  - Obligacion_informar_riesgo_tasa_interes_eve: NO aparece en el top-10 · global — de 50

**VEREDICTO K9:** posiciones arriba.


## K11 (CQN-010) — ¿la nominación del 9.2 de Exterior?


Hits: 13

### Obligacion_la_entidad_nominada_por_el_exportador_antes_de_la_emision_de_cada_certificacion_ — matchea en: ['properties.descripcion [nominada]']

```json
{
 "id": "Obligacion_la_entidad_nominada_por_el_exportador_antes_de_la_emision_de_cada_certificacion_",
 "type": "Obligacion",
 "label": "Constatar información previa a emisión",
 "properties": {
  "descripcion": "La entidad nominada por el exportador, antes de la emisión de cada certificación, deberá constatar en la información suministrada por el BCRA el monto máximo total y que el exportador no tiene permisos en situación de incumplimiento",
  "tipo": "presentacion_informativa"
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 3.18. Acceso con “Certificación de aumento de las exportaciones de bienes”. (parte 1)"
  }
 ]
}
```

### Obligacion_en_el_caso_de_financiaciones_otorgadas_por_entidades_financieras_locales_el_segu — matchea en: ['properties.descripcion [otorgo financiacion]']

```json
{
 "id": "Obligacion_en_el_caso_de_financiaciones_otorgadas_por_entidades_financieras_locales_el_segu",
 "type": "Obligacion",
 "label": "A cargo seguimiento financiaciones",
 "properties": {
  "descripcion": "En el caso de financiaciones otorgadas por entidades financieras locales, el seguimiento estará a cargo de la entidad que otorgó la financiación hasta su cancelación total",
  "tipo": "otra",
  "plazo": "hasta cancelación total"
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 7.10. 9.1.7. Aportes de inversión extranjera directa admitidos en los puntos 7.9. o 7."
  }
 ]
}
```

### Obligacion_incorporar_operacion_al_seguimiento — matchea en: ['properties.description [nominada]']

```json
{
 "id": "Obligacion_incorporar_operacion_al_seguimiento",
 "type": "Obligacion",
 "label": "Incorporar operación al seguimiento",
 "properties": {
  "tipo": "presentacion_informativa",
  "description": "En el caso de operaciones comprendidas en el punto 7.3.8. que no registren liquidaciones en el mercado de cambios, la entidad nominada por el exportador deberá incorporarla al mencionado seguimiento, usando para su identificación el número correlativo que se le asignó a la operación del cliente (número ECO)"
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 7.3. Aplicación de divisas de cobros de exportaciones. (parte 1)"
  }
 ]
}
```

### Obligacion_presentar_pedidos_de_conformidad_ante_bcra — matchea en: ['properties.description [nominada]']

```json
{
 "id": "Obligacion_presentar_pedidos_de_conformidad_ante_bcra",
 "type": "Obligacion",
 "label": "Presentar pedidos de conformidad ante BCRA",
 "properties": {
  "tipo": "presentacion_informativa",
  "description": "Los pedidos de conformidad deberán ser presentados ante el BCRA exclusivamente por la entidad nominada por el exportador"
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 7.3. Aplicación de divisas de cobros de exportaciones. (parte 1)"
  }
 ]
}
```

### Operacion_nominacion_de_entidad_para_seguimiento_de_exportacion — matchea en: ['provenances[0] [nominada]']

```json
{
 "id": "Operacion_nominacion_de_entidad_para_seguimiento_de_exportacion",
 "type": "Operacion",
 "label": "Nominación de entidad responsable",
 "properties": {
  "tipo": "nominación de entidad para seguimiento de exportación",
  "description": "El exportador deberá seleccionar una entidad como responsable del seguimiento de cada operación de exportación. La designación será inicialmente efectuada al momento de realizar la oficialización del permiso de embarque ante ARCA."
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 8.2. Entidad nominada por el exportador."
  }
 ]
}
```

### Obligacion_la_entidad_debera_informar_la_asuncion_de_la_tarea_de_seguimiento_al_bcra — matchea en: ['provenances[0] [nominada]']

```json
{
 "id": "Obligacion_la_entidad_debera_informar_la_asuncion_de_la_tarea_de_seguimiento_al_bcra",
 "type": "Obligacion",
 "label": "Informar asunción al BCRA",
 "properties": {
  "tipo": "comunicacion_a_cliente",
  "descripcion": "La entidad deberá informar la asunción de la tarea de seguimiento al BCRA",
  "description": "La entidad deberá informar la asunción al BCRA cuando el exportador haya acordado con la entidad la responsabilidad del seguimiento."
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 8.2. Entidad nominada por el exportador."
  }
 ]
}
```

### Obligacion_llevar_responsabilidades_asociadas — matchea en: ['provenances[0] [nominada]']

```json
{
 "id": "Obligacion_llevar_responsabilidades_asociadas",
 "type": "Obligacion",
 "label": "Llevar responsabilidades asociadas",
 "properties": {
  "tipo": "otra",
  "description": "Las entidades financieras y casas de cambio quedan obligadas a llevar a cabo las responsabilidades asociadas al seguimiento de la exportación."
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 8.2. Entidad nominada por el exportador."
  }
 ]
}
```

### Restriccion_entidades_que_han_notificado_al_bcra_que_optaron_por_no_operar_en_comercio_exter — matchea en: ['provenances[0] [nominada]']

```json
{
 "id": "Restriccion_entidades_que_han_notificado_al_bcra_que_optaron_por_no_operar_en_comercio_exter",
 "type": "Restriccion",
 "label": "Exclusión de entidades sin operatoria",
 "properties": {
  "tipo": "limite_cualitativo",
  "descripcion": "Entidades que han notificado al BCRA que optaron por no operar en comercio exterior no son elegibles",
  "description": "Serán elegibles todas las entidades financieras y casas de cambio salvo aquellas que hayan notificado al BCRA que han optado por no operar en comercio exterior."
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 8.2. Entidad nominada por el exportador."
  }
 ]
}
```

### Operacion_cambio_de_entidad_responsable_del_seguimiento_de_exportacion — matchea en: ['provenances[0] [nominada]']

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

### Restriccion_no_podra_modificarse_voluntariamente_si_se_ha_producido_vencimiento_del_plazo_pa — matchea en: ['provenances[0] [nominada]']

```json
{
 "id": "Restriccion_no_podra_modificarse_voluntariamente_si_se_ha_producido_vencimiento_del_plazo_pa",
 "type": "Restriccion",
 "label": "Límite temporal para cambio voluntario",
 "properties": {
  "tipo": "limite_cualitativo",
  "descripcion": "No podrá modificarse voluntariamente si se ha producido vencimiento del plazo para liquidación",
  "description": "El exportador podrá modificar a voluntad la entidad encargada del seguimiento siempre que no se haya producido el vencimiento del plazo previsto para la liquidación de los cobros del permiso."
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 8.2. Entidad nominada por el exportador."
  }
 ]
}
```

### Restriccion_procedimiento_de_cambio_cuando_la_entidad_nominada_opto_por_no_operar_en_comerci — matchea en: ['provenances[0] [nominada]']

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

### Obligacion_notificar_cambio_a_nueva_entidad — matchea en: ['provenances[0] [nominada]']

```json
{
 "id": "Obligacion_notificar_cambio_a_nueva_entidad",
 "type": "Obligacion",
 "label": "Notificar cambio a nueva entidad",
 "properties": {
  "tipo": "comunicacion_a_cliente",
  "description": "La entidad a cargo del seguimiento deberá notificarle la voluntad del exportador a la nueva entidad designada."
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 8.2. Entidad nominada por el exportador."
  }
 ]
}
```

### Excepcion_la_constancia_de_aceptacion_por_parte_de_la_nueva_entidad_libera_a_la_entidad_pr — matchea en: ['provenances[0] [nominada]']

```json
{
 "id": "Excepcion_la_constancia_de_aceptacion_por_parte_de_la_nueva_entidad_libera_a_la_entidad_pr",
 "type": "Excepcion",
 "label": "Liberación por aceptación nueva entidad",
 "properties": {
  "descripcion": "La constancia de aceptación por parte de la nueva entidad libera a la entidad previa de sus obligaciones hacia adelante.",
  "description": "La constancia de aceptación por parte de la nueva entidad liberará a la entidad previa de sus obligaciones hacia adelante."
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 8.2. Entidad nominada por el exportador."
  }
 ]
}
```

**VEREDICTO K11:** 13 hit(s).


## K12 (CQN-011) — ¿el mapeo de la Sección 2 del RI (código 2 / consolidado mensual + filiales)?


Hits: 0

**VEREDICTO K12:** 0 hit(s).


## K13 (CQN-012) — ¿la regla del 1.1 de Capitales ('mayor valor' + básica vs suma de riesgos)?


Hits: 1

### Operacion_determinacion_de_exigencia_por_riesgo_de_mercado — matchea en: ['properties.description [mayor valor+riesgos]']

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


**paso 15** — `exigencia capital máximo mayor entre riesgo crédito mercado operacional` · límite 10
  - Operacion_determinacion_de_exigencia_por_riesgo_de_mercado: NO aparece en el top-10 · global 16 de 50
**VEREDICTO K13:** 1 hit(s); ranking arriba.


## K14 (CQN-014) — nodos completos de los dos ids pedidos

### Restriccion_la_exigencia_determinada_a_traves_de_la_aplicacion_de_la_expresion_descripta_en_ (match exacto)

```json
{
 "id": "Restriccion_la_exigencia_determinada_a_traves_de_la_aplicacion_de_la_expresion_descripta_en_",
 "type": "Restriccion",
 "label": "Límite 20% grupo A capital mínimo",
 "properties": {
  "descripcion": "La exigencia determinada a través de la aplicación de la expresión descripta en el punto 7.2. no podrá superar el 20% en el caso de entidades del grupo A del promedio de los últimos 36 meses –anteriores al mes a que corresponda la determinación de la exigencia– de la exigencia de capital mínimo por riesgo de crédito calculada según lo previsto en la Sección 2., expresada en moneda homogénea del mes anterior al que se efectúa el cálculo.",
  "tipo": "limite_cuantitativo",
  "umbral": "20%"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Punto 7.3. Límite para las entidades del grupo 2."
  }
 ]
}
```

### Restriccion_el_17_en_el_caso_de_entidades_del_grupo_b_del_promedio_de_los_ultimos_36_meses_a (match exacto)

```json
{
 "id": "Restriccion_el_17_en_el_caso_de_entidades_del_grupo_b_del_promedio_de_los_ultimos_36_meses_a",
 "type": "Restriccion",
 "label": "Límite 17% grupo B capital mínimo",
 "properties": {
  "descripcion": "El 17% en el caso de entidades del grupo B del promedio de los últimos 36 meses –anteriores al mes a que corresponda la determinación de la exigencia– de la exigencia de capital mínimo por riesgo de crédito calculada según lo previsto en la Sección 2., expresada en moneda homogénea del mes anterior al que se efectúa el cálculo.",
  "tipo": "limite_cuantitativo",
  "umbral": "17%"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Punto 7.3. Límite para las entidades del grupo 2."
  }
 ]
}
```

**VEREDICTO K14:** ver dumps arriba (existencia por id).


---

**Sello:** 2026-07-17 · HEAD = `1bf666e6ebcf21a384206a7edd35e63cf0e4e9b3` · grafo: run_3 congelado (loader+GraphIndex; 4050 nodos). Ni verificador ni S1 corrieron.
