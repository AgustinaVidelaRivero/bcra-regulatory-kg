# Expediente del piloto — APÉNDICES: outputs COMPLETOS re-ejecutados por caso

Parte 2 de 2 (ver `expediente_piloto_1.md`). Mecanismo: re-ejecución determinística
contra el grafo congelado de run_3 (loader + GraphIndex, el de siempre). Por paso se
indica el largo runtime registrado y el re-ejecutado (fidelidad = igualdad).


---

# Apéndice CQ-016 — outputs completos (11 pasos re-ejecutables)


--- paso 1 · buscar_nodos · input={"consulta": "Régimen Informativo Exigencia Integración Capitales Mínimos", "limite": 10} · runtime=3337 chars · re-ejecutado=3337 chars ---

```json
{
 "consulta": "Régimen Informativo Exigencia Integración Capitales Mínimos",
 "total_con_match": 154,
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
   "id": "Obligacion_informar_exigencia_de_capitales_por_riesgo",
   "type": "Obligacion",
   "label": "Informar exigencia de capitales por riesgo",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Presentar información sobre exigencia de capitales mínimos por riesgo de mercado con periodicidad mensual, desglosada por código de concepto y día del mes"
  },
  {
   "id": "Obligacion_las_entidades_financieras_comprendidas_sus_filiales_en_el_pais_y_en_el_exterior_",
   "type": "Obligacion",
   "label": "Observar capitales mínimos en base individual",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Las entidades financieras (comprendidas sus filiales en el país y en el exterior) observarán las normas en materia de capitales mínimos en forma individual."
  }
 ]
}
```

--- paso 2 · buscar_nodos · input={"consulta": "importes unidad decimales registro", "limite": 10} · runtime=2967 chars · re-ejecutado=2967 chars ---

```json
{
 "consulta": "importes unidad decimales registro",
 "total_con_match": 81,
 "resultados": [
  {
   "id": "Restriccion_los_importes_se_registraran_en_miles_de_pesos_sin_decimales",
   "type": "Restriccion",
   "label": "Registro en miles sin decimales",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Los importes se registrarán en miles de pesos, sin decimales"
  },
  {
   "id": "Operacion_registro_contable",
   "type": "Operacion",
   "label": "Registro de importes",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Los importes se registrarán en miles de pesos, sin decimales"
  },
  {
   "id": "Obligacion_en_el_registro_de_reintegros_de_importes_rri_se_deberan_asentar_los_montos_reint",
   "type": "Obligacion",
   "label": "Asentar reintegros en registro",
   "tokens_matcheados": 2,
   "resumen_propiedades": "En el Registro de Reintegros de Importes (RRI) se deberán asentar los montos reintegrados a los usuarios, identificando en cada caso al usuario afectado, la cau…"
  },
  {
   "id": "Obligacion_el_registro_de_reintegros_de_importes_rri_previsto_en_el_punto_3_1_4",
   "type": "Obligacion",
   "label": "Disponibilizar Registro Reintegros Importes",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El Registro de Reintegros de Importes (RRI) previsto en el punto 3.1.4."
  },
  {
   "id": "Obligacion_incrementar_valores_en_una_unidad_cuando_el_primer_digito_de_las_fracciones_sea_",
   "type": "Obligacion",
   "label": "Redondeo de magnitudes",
   "tokens_matcheados": 1,
   "resumen_propiedades": "A los fines del redondeo de las magnitudes se incrementarán los valores en una unidad cuando el primer dígito de las fracciones sea igual o mayor que 5, desecha…"
  },
  {
   "id": "Operacion_registro_informativo",
   "type": "Operacion",
   "label": "Registro de operaciones",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Registrar en bases de datos cualquier circunstancia que implique una reducción del monto del capital adeudado y disponible para aplicación"
  },
  {
   "id": "Restriccion_el_importe_de_esta_rpc_que_sera_admisible_como_pnc_excluye_los_importes_reconoci",
   "type": "Restriccion",
   "label": "Exclusión de RPC en PNc",
   "tokens_matcheados": 1,
   "resumen_propiedades": "El importe de esta RPC que será admisible como PNc excluye los importes reconocidos en el CO conforme a lo establecido en el punto 8.3.5.1. y los importes recon…"
  },
  {
   "id": "Operacion_registro_cambio",
   "type": "Operacion",
   "label": "Boleto de venta de cambio",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Realización de boleto de venta de cambio a nombre del cliente por el código de concepto correspondiente a la adjudicación de bonos BOPREAL"
  },
  {
   "id": "Operacion_registro_de_operacion_de_cambio",
   "type": "Operacion",
   "label": "Registro de aporte en RIOC",
   "tokens_matcheados": 1,
   "resumen_propiedades": "tipo: registro de operación de cambio"
  },
  {
   "id": "Operacion_registro_del_cambio_de_entidad_en_el_bcra",
   "type": "Operacion",
   "label": "Registro de cambio en BCRA",
   "tokens_matcheados": 1,
   "resumen_propiedades": "tipo: registro del cambio de entidad en el BCRA"
  }
 ]
}
```

--- paso 3 · ver_nodo · input={"id": "Restriccion_los_importes_se_registraran_en_miles_de_pesos_sin_decimales"} · runtime=527 chars · re-ejecutado=527 chars ---

```json
{
 "id": "Restriccion_los_importes_se_registraran_en_miles_de_pesos_sin_decimales",
 "type": "Restriccion",
 "label": "Registro en miles sin decimales",
 "properties": {
  "descripcion": "Los importes se registrarán en miles de pesos, sin decimales",
  "tipo": "limite_cualitativo",
  "description": "Los importes se registrarán en miles de pesos, sin decimales"
 },
 "provenances": [
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Punto 1.2. Los importes se registrarán en miles de pesos, sin decimales."
  }
 ]
}
```

--- paso 4 · ver_nodo · input={"id": "TextoOrdenado_to_capitales_minimos_actual_pdf"} · runtime=361 chars · re-ejecutado=361 chars ---

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

--- paso 5 · ver_vecinos · input={"id": "TextoOrdenado_to_capitales_minimos_actual_pdf", "direccion": "salientes"} · runtime=9323 chars · re-ejecutado=9323 chars ---

```json
{
 "id": "TextoOrdenado_to_capitales_minimos_actual_pdf",
 "label": "Capitales Mínimos",
 "n_salientes_total": 154,
 "n_entrantes_total": 815,
 "salientes": [
  {
   "relation": "referencia",
   "vecino_id": "Comunicacion_a_2136",
   "vecino_label": "Com. A 2136",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 1.1. “A” 2136 1. 1° Según Com. “A” 2859, 3558,"
    }
   ]
  },
  {
   "relation": "referencia",
   "vecino_id": "Comunicacion_a_2859",
   "vecino_label": "Com. A 2859",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 1.1. “A” 2136 1. 1° Según Com. “A” 2859, 3558,"
    }
   ]
  },
  {
   "relation": "referencia",
   "vecino_id": "Comunicacion_a_3558",
   "vecino_label": "Com. A 3558",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 1.1. “A” 2136 1. 1° Según Com. “A” 2859, 3558,"
    }
   ]
  },
  {
   "relation": "referencia",
   "vecino_id": "Comunicacion_a_5272",
   "vecino_label": "Com. A 5272",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 1.1. “A” 2136 1. 1° Según Com. “A” 2859, 3558,"
    }
   ]
  },
  {
   "relation": "referencia",
   "vecino_id": "Comunicacion_a_5369",
   "vecino_label": "Com. A 5369",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 1.1. “A” 2136 1. 1° Según Com. “A” 2859, 3558,"
    }
   ]
  },
  {
   "relation": "referencia",
   "vecino_id": "Comunicacion_a_5580",
   "vecino_label": "Com. A 5580",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 1.1. “A” 2136 1. 1° Según Com. “A” 2859, 3558,"
    }
   ]
  },
  {
   "relation": "referencia",
   "vecino_id": "Comunicacion_a_5867",
   "vecino_label": "Com. A 5867",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 1.1. “A” 2136 1. 1° Según Com. “A” 2859, 3558,"
    }
   ]
  },
  {
   "relation": "referencia",
   "vecino_id": "Comunicacion_a_2241",
   "vecino_label": "Com. A 2241",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 1.1. “A” 2136 1. 1° Según Com. “A” 2859, 3558,"
    }
   ]
  },
  {
   "relation": "referencia",
   "vecino_id": "Comunicacion_a_4368",
   "vecino_label": "Com. A 4368",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 1.1. “A” 2136 1. 1° Según Com. “A” 2859, 3558,"
    }
   ]
  },
  {
   "relation": "referencia",
   "vecino_id": "Comunicacion_a_4771",
   "vecino_label": "Com. A 4771",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 1.1. “A” 2136 1. 1° Según Com. “A” 2859, 3558,"
    }
   ]
  },
  {
   "relation": "referencia",
   "vecino_id": "Comunicacion_a_5168",
   "vecino_label": "Com. A 5168",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 1.1. “A” 2136 1. 1° Según Com. “A” 2859, 3558,"
    }
   ]
  },
  {
   "relation": "referencia",
   "vecino_id": "Comunicacion_a_5351",
   "vecino_label": "Com. A 5351",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 1.1. “A” 2136 1. 1° Según Com. “A” 2859, 3558,"
    }
   ]
  },
  {
   "relation": "referencia",
   "vecino_id": "Comunicacion_a_5355",
   "vecino_label": "Com. A 5355",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 1.1. “A” 2136 1. 1° Según Com. “A” 2859, 3558,"
    }
   ]
  },
  {
   "relation": "referencia",
   "vecino_id": "Comunicacion_a_5983",
   "vecino_label": "Com. A 5983",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 1.1. “A” 2136 1. 1° Según Com. “A” 2859, 3558,"
    }
   ]
  },
  {
   "relation": "referencia",
   "vecino_id": "Comunicacion_a_6260",
   "vecino_label": "Com. A 6260",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 1.1. “A” 2136 1. 1° Según Com. “A” 2859, 3558,"
    }
   ]
  },
  {
   "relation": "referencia",
   "vecino_id": "Comunicacion_a_7470",
   "vecino_label": "Com. A 7470",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 1.1. “A” 2136 1. 1° Según Com. “A” 2859, 3558,"
    }
   ]
  },
  {
   "relation": "referencia",
   "vecino_id": "Comunicacion_a_7524",
   "vecino_label": "Com. A 7524",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 1.1. “A” 2136 1. 1° Según Com. “A” 2859, 3558,"
    }
   ]
  },
  {
   "relation": "referencia",
   "vecino_id": "Comunicacion_a_8028",
   "vecino_label": "Com. A 8028",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 1.1. “A” 2136 1. 1° Según Com. “A” 2859, 3558,"
    }
   ]
  },
  {
   "relation": "referencia",
   "vecino_id": "Comunicacion_a_2223",
   "vecino_label": "Com. A 2223",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 1.1. “A” 2136 1. 1° Según Com. “A” 2859, 3558,"
    }
   ]
  },
  {
   "relation": "referencia",
   "vecino_id": "Comunicacion_a_3171",
   "vecino_label": "Com. A 3171",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 1.1. “A” 2136 1. 1° Según Com. “A” 2859, 3558,"
    }
   ]
  },
  {
   "relation": "referencia",
   "vecino_id": "Comunicacion_a_3959",
   "vecino_label": "Com. A 3959",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 1.1. “A” 2136 1. 1° Según Com. “A” 2859, 3558,"
    }
   ]
  },
  {
   "relation": "referencia",
   "vecino_id": "Comunicacion_a_414",
   "vecino_label": "Com. A 414",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 1.1. “A” 2136 1. 1° Según Com. “A” 2859, 3558,"
    }
   ]
  },
  {
   "relation": "referencia",
   "vecino_id": "Comunicacion_a_6275",
   "vecino_label": "Com. A 6275",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 1.1. “A” 2136 1. 1° Según Com. “A” 2859, 3558,"
    }
   ]
  },
  {
   "relation": "referencia",
   "vecino_id": "Comunicacion_a_8067",
   "vecino_label": "Com. A 8067",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 1.1. “A” 2136 1. 1° Según Com. “A” 2859, 3558,"
    }
   ]
  },
  {
   "relation": "referencia",
   "vecino_id": "Comunicacion_a_8171",
   "vecino_label": "Com. A 8171",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 10.3. Consideraciones para su implementación."
    }
   ]
  },
  {
   "relation": "referencia",
   "vecino_id": "Comunicacion_a_6346",
   "vecino_label": "Com. A 6346",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 10.3. Consideraciones para su implementación."
    }
   ]
  },
  {
   "relation": "referencia",
   "vecino_id": "Comunicacion_a_3985",
   "vecino_label": "Com. A 3985",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 11.1. “A” 3985 Según Com. “A” 4172."
    }
   ]
  },
  {
   "relation": "referencia",
   "vecino_id": "Comunicacion_a_4172",
   "vecino_label": "Com. A 4172",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 11.1. “A” 3985 Según Com. “A” 4172."
    }
   ]
  },
  {
   "relation": "referencia",
   "vecino_id": "Comunicacion_a_6938",
   "vecino_label": "Com. A 6938",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 11.1. “A” 3985 Según Com. “A” 4172."
    }
   ]
  },
  {
   "relation": "referencia",
   "vecino_id": "Comunicacion_a_7007",
   "vecino_label": "Com. A 7007",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 11.1. “A” 3985 Según Com. “A” 4172."
    }
   ]
  },
  {
   "relation": "referencia",
   "vecino_id": "Comunicacion_a_7928",
   "vecino_label": "Com. A 7928",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 11.1. “A” 3985 Según Com. “A” 4172."
    }
   ]
  },
  {
   "relation": "referencia",
   "vecino_id": "Comunicacion_a_7018",
   "vecino_label": "Com. A 7018",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 11.1. “A” 3985 Según Com. “A” 4172."
    }
   ]
  },
  {
   "relation": "referencia",
   "vecino_id": "Comunicacion_a_8121",
   "vecino_label": "Com. A 8121",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 11.1. “A” 3985 Según Com. “A” 4172."
    }
   ]
  },
  {
   "relation": "referencia",
   "vecino_id": "Comunicacion_a_8418",
   "vecino_label": "Com. A 8418",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 11.1. “A” 3985 Según Com. “A” 4172."
    }
   ]
  },
  {
   "relation": "referencia",
   "vecino_id": "Comunicacion_a_7545",
   "vecino_label": "Com. A 7545",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 11.1. “A” 3985 Según Com. “A” 4172."
    }
   ]
  },
  {
   "relation": "referencia",
   "vecino_id": "Comunicacion_a_6847",
   "vecino_label": "Com. A 6847",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 11.4. A los efectos de la determinación de la RPC, las entidades financieras podrán co"
    }
   ]
  },
  {
   "relation": "referencia",
   "vecino_id": "Comunicacion_a_8383",
   "vecino_label": "Com. A 8383",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 12.3. Para aquellas entidades financieras que sean reclasificadas desde el 01/01/2026"
    }
   ]
  },
  {
   "relation": "referencia",
   "vecino_id": "Comunicacion_a_8364",
   "vecino_label": "Com. A 8364",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 12. 8028. (parte 2)"
    }
   ]
  },
  {
   "relation": "modificada_por",
   "vecino_id": "Comunicacion_a_8068",
   "vecino_label": "Com. A 8068",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 12. 8028. (parte 2)"
    }
   ]
  },
  {
   "relation": "modificada_por",
   "vecino_id": "Comunicacion_a_8329",
   "vecino_label": "Com. A 8329",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 12. 8028. (parte 2)"
    }
   ]
  }
 ],
 "salientes_truncado": true
}
```

--- paso 6 · buscar_nodos · input={"consulta": "capitales mínimos importes miles decimales", "limite": 10} · runtime=3123 chars · re-ejecutado=3123 chars ---

```json
{
 "consulta": "capitales mínimos importes miles decimales",
 "total_con_match": 29,
 "resultados": [
  {
   "id": "Restriccion_los_importes_se_registraran_en_miles_de_pesos_sin_decimales",
   "type": "Restriccion",
   "label": "Registro en miles sin decimales",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Los importes se registrarán en miles de pesos, sin decimales"
  },
  {
   "id": "TextoOrdenado_to_capitales_minimos_actual_pdf",
   "type": "TextoOrdenado",
   "label": "Capitales Mínimos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "materia: capitales minimos; archivo: TO_capitales_minimos_actual.pdf; version: actual"
  },
  {
   "id": "Operacion_integracion_de_capitales",
   "type": "Operacion",
   "label": "Integración de capitales mínimos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: integración de capitales"
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
   "id": "Obligacion_convertir_importes_en_moneda_extranjera_a_pesos",
   "type": "Obligacion",
   "label": "Conversión moneda extranjera",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Los importes en moneda extranjera se convertirán a pesos utilizando el tipo de cambio de referencia publicado por el BCRA para el dólar estadounidense, previa a…"
  }
 ]
}
```

--- paso 7 · buscar_nodos · input={"consulta": "régimen informativo capitales mínimos exigencia integración", "limite": 10} · runtime=3337 chars · re-ejecutado=3337 chars ---

```json
{
 "consulta": "régimen informativo capitales mínimos exigencia integración",
 "total_con_match": 154,
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
   "id": "Obligacion_informar_exigencia_de_capitales_por_riesgo",
   "type": "Obligacion",
   "label": "Informar exigencia de capitales por riesgo",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Presentar información sobre exigencia de capitales mínimos por riesgo de mercado con periodicidad mensual, desglosada por código de concepto y día del mes"
  },
  {
   "id": "Obligacion_las_entidades_financieras_comprendidas_sus_filiales_en_el_pais_y_en_el_exterior_",
   "type": "Obligacion",
   "label": "Observar capitales mínimos en base individual",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Las entidades financieras (comprendidas sus filiales en el país y en el exterior) observarán las normas en materia de capitales mínimos en forma individual."
  }
 ]
}
```

--- paso 8 · ver_nodo · input={"id": "Obligacion_informar_exigencia_de_capitales_por_riesgo"} · runtime=521 chars · re-ejecutado=521 chars ---

```json
{
 "id": "Obligacion_informar_exigencia_de_capitales_por_riesgo",
 "type": "Obligacion",
 "label": "Informar exigencia de capitales por riesgo",
 "properties": {
  "tipo": "presentacion_informativa",
  "description": "Presentar información sobre exigencia de capitales mínimos por riesgo de mercado con periodicidad mensual, desglosada por código de concepto y día del mes",
  "plazo": "mensual"
 },
 "provenances": [
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Punto 4.2. Modelos de información"
  }
 ]
}
```

--- paso 9 · ver_vecinos · input={"id": "Restriccion_los_importes_se_registraran_en_miles_de_pesos_sin_decimales", "direccion": "entrantes"} · runtime=219 chars · re-ejecutado=219 chars ---

```json
{
 "id": "Restriccion_los_importes_se_registraran_en_miles_de_pesos_sin_decimales",
 "label": "Registro en miles sin decimales",
 "n_salientes_total": 3,
 "n_entrantes_total": 0,
 "entrantes": [],
 "entrantes_truncado": false
}
```

--- paso 10 · buscar_nodos · input={"consulta": "punto 1.2 importes miles pesos decimales", "limite": 5} · runtime=1574 chars · re-ejecutado=1574 chars ---

```json
{
 "consulta": "punto 1.2 importes miles pesos decimales",
 "total_con_match": 126,
 "resultados": [
  {
   "id": "Restriccion_los_importes_se_registraran_en_miles_de_pesos_sin_decimales",
   "type": "Restriccion",
   "label": "Registro en miles sin decimales",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Los importes se registrarán en miles de pesos, sin decimales"
  },
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
   "id": "Obligacion_los_sujetos_obligados_enumerados_en_el_punto_1_1_2_en_la_medida_en_que_correspon",
   "type": "Obligacion",
   "label": "Cobertura mínima de cajeros accesibles",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Los sujetos obligados enumerados en el punto 1.1.2., en la medida en que corresponda, deberán alcanzar la cobertura del servicio con esos cajeros automáticos en…"
  },
  {
   "id": "Obligacion_el_registro_de_reintegros_de_importes_rri_previsto_en_el_punto_3_1_4",
   "type": "Obligacion",
   "label": "Disponibilizar Registro Reintegros Importes",
   "tokens_matcheados": 3,
   "resumen_propiedades": "El Registro de Reintegros de Importes (RRI) previsto en el punto 3.1.4."
  }
 ]
}
```

--- paso 11 · buscar_nodos · input={"consulta": "TO_capitales_minimos formato unidad registro", "limite": 10} · runtime=3164 chars · re-ejecutado=3164 chars ---

```json
{
 "consulta": "TO_capitales_minimos formato unidad registro",
 "total_con_match": 91,
 "resultados": [
  {
   "id": "TextoOrdenado_to_capitales_minimos_actual_pdf",
   "type": "TextoOrdenado",
   "label": "Capitales Mínimos",
   "tokens_matcheados": 3,
   "resumen_propiedades": "materia: capitales minimos; archivo: TO_capitales_minimos_actual.pdf; version: actual"
  },
  {
   "id": "Operacion_integracion_de_capitales",
   "type": "Operacion",
   "label": "Integración de capitales mínimos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: integración de capitales"
  },
  {
   "id": "Obligacion_deberan_consignarse_como_minimo_los_siguientes_datos_numero_de_consulta_o_reclam",
   "type": "Obligacion",
   "label": "Consignar datos mínimos en registro",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Deberán consignarse como mínimo los siguientes datos: número de consulta o reclamo; fecha, canal y motivo de la presentación; tipo y número de documento de iden…"
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
   "id": "TextoOrdenado_to_exterior_cambios_actual_pdf",
   "type": "TextoOrdenado",
   "label": "Exterior y Cambios",
   "tokens_matcheados": 1,
   "resumen_propiedades": "materia: Operaciones de exterior y cambios; archivo: TO_exterior_cambios_actual.pdf; version: actual"
  },
  {
   "id": "Operacion_registro_contable",
   "type": "Operacion",
   "label": "Registro de importes",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Los importes se registrarán en miles de pesos, sin decimales"
  },
  {
   "id": "Obligacion_incrementar_valores_en_una_unidad_cuando_el_primer_digito_de_las_fracciones_sea_",
   "type": "Obligacion",
   "label": "Redondeo de magnitudes",
   "tokens_matcheados": 1,
   "resumen_propiedades": "A los fines del redondeo de las magnitudes se incrementarán los valores en una unidad cuando el primer dígito de las fracciones sea igual o mayor que 5, desecha…"
  }
 ]
}
```

---

# Apéndice CQ-018 — outputs completos (15 pasos re-ejecutables)


--- paso 1 · buscar_nodos · input={"consulta": "proveedores no financieros crédito", "limite": 10} · runtime=3293 chars · re-ejecutado=3293 chars ---

```json
{
 "consulta": "proveedores no financieros crédito",
 "total_con_match": 506,
 "resultados": [
  {
   "id": "EntidadFinanciera_proveedor_no_financiero_de_credito",
   "type": "EntidadFinanciera",
   "label": "Proveedores no financieros de crédito",
   "tokens_matcheados": 4,
   "resumen_propiedades": "categoria: proveedor no financiero de crédito"
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
   "id": "Operacion_enajenacion_de_activos_no_financieros_no_producidos",
   "type": "Operacion",
   "label": "Enajenación de activos no producidos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Enajenación a no residentes de activos no financieros no producidos por parte de residentes"
  },
  {
   "id": "Restriccion_el_periodo_de_vigencia_del_derivado_de_credito_no_podra_ser_inferior_a_cualquier",
   "type": "Restriccion",
   "label": "Período mínimo de vigencia derivados",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El período de vigencia del derivado de crédito no podrá ser inferior a cualquier período de gracia necesario para poder determinar que efectivamente se ha produ…"
  },
  {
   "id": "Operacion_enajenacion_de_activos",
   "type": "Operacion",
   "label": "Enajenación de activos no financieros",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Enajenación de activos no financieros no producidos"
  },
  {
   "id": "Restriccion_titulos_de_credito_titulos_valores_certificados_de_depositos_a_plazo_fijo_y_otro",
   "type": "Restriccion",
   "label": "Deducción títulos no en poder entidad",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Títulos de crédito (títulos valores, certificados de depósitos a plazo fijo y otros) que físicamente no se encuentren en poder de la entidad, salvo que su regis…"
  },
  {
   "id": "Obligacion_debera_informar_en_las_notas_a_los_estados_financieros_de_publicacion_que_ha_pre",
   "type": "Obligacion",
   "label": "Informar respaldo crediticio no contractual",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Deberá informar en las notas a los estados financieros de publicación que ha prestado respaldo crediticio no contractual y el efecto sobre su exigencia de capit…"
  },
  {
   "id": "Restriccion_riesgo_de_credito_en_garantias_no_protegidas",
   "type": "Restriccion",
   "label": "Riesgo de crédito en garantías no protegidas",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Cuando los activos de un miembro compensador o cliente se coloquen en garantía a favor de una CCP o miembro compensador, pero de modo que no queden protegidos d…"
  },
  {
   "id": "Excepcion_a_fin_de_verificar_el_cumplimiento_de_obligaciones_de_naturaleza_comercial_no_se",
   "type": "Excepcion",
   "label": "Excepción renovación crédito capital de trabajo",
   "tokens_matcheados": 2,
   "resumen_propiedades": "A fin de verificar el cumplimiento de obligaciones de naturaleza comercial, no se considerarán comprendidas en refinanciaciones las renovaciones periódicas de c…"
  }
 ]
}
```

--- paso 2 · buscar_nodos · input={"consulta": "empresas no financieras emisoras tarjetas", "limite": 10} · runtime=3125 chars · re-ejecutado=3125 chars ---

```json
{
 "consulta": "empresas no financieras emisoras tarjetas",
 "total_con_match": 422,
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
   "id": "EntidadFinanciera_entidad_no_financiera_emisora_de_tarjeta",
   "type": "EntidadFinanciera",
   "label": "Entidades no financieras emisoras de tarjetas",
   "tokens_matcheados": 4,
   "resumen_propiedades": "categoria: entidad no financiera emisora de tarjetas de crédito"
  },
  {
   "id": "EntidadFinanciera_empresa_emisora_de_tarjeta",
   "type": "EntidadFinanciera",
   "label": "Empresas emisoras de tarjetas",
   "tokens_matcheados": 3,
   "resumen_propiedades": "categoria: empresa emisora de tarjetas de crédito"
  },
  {
   "id": "Restriccion_las_entidades_financieras_y_otras_emisoras_de_tarjetas_locales_de_credito_y_o_co",
   "type": "Restriccion",
   "label": "Límite adelanto en efectivo exterior",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Las entidades financieras y otras emisoras de tarjetas locales de crédito y/o compra podrán otorgar como adelanto en efectivo a los tarjetahabientes en el exter…"
  },
  {
   "id": "EntidadFinanciera_entidad_financiera_emisora_de_tarjeta_de_credito",
   "type": "EntidadFinanciera",
   "label": "Entidades financieras emisoras de tarjetas de crédito",
   "tokens_matcheados": 3,
   "resumen_propiedades": "categoria: emisora de tarjeta de crédito"
  },
  {
   "id": "EntidadFinanciera_emisora_de_tarjeta_local",
   "type": "EntidadFinanciera",
   "label": "Emisoras de tarjetas locales",
   "tokens_matcheados": 2,
   "resumen_propiedades": "categoria: emisora de tarjetas de crédito y/o compra"
  },
  {
   "id": "EntidadFinanciera_empresa_no_sujeta_supervision",
   "type": "EntidadFinanciera",
   "label": "Empresas no sujetas supervisión",
   "tokens_matcheados": 2,
   "resumen_propiedades": "categoria: empresa no sujeta a supervisión consolidada"
  }
 ]
}
```

--- paso 3 · buscar_nodos · input={"consulta": "clasificación deudores criterio", "limite": 10} · runtime=3298 chars · re-ejecutado=3298 chars ---

```json
{
 "consulta": "clasificación deudores criterio",
 "total_con_match": 86,
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
   "id": "Restriccion_los_deudores_cuyas_financiaciones_se_encuentren_cubiertas_totalmente_con_garanti",
   "type": "Restriccion",
   "label": "Prohibición de clasificación por cobertura total",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Los deudores cuyas financiaciones se encuentren cubiertas totalmente con garantías preferidas A no serán objeto de clasificación, sin perjuicio de su informació…"
  },
  {
   "id": "Excepcion_modificacion_en_forma_negativa_de_la_clasificacion_del_cliente_en_la_central_de_",
   "type": "Excepcion",
   "label": "Excepción por cambio negativo en Central de deudores",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Modificación en forma negativa de la clasificación del cliente en la Central de deudores del sistema financiero, llevándola a un grado inferior al de la entidad…"
  }
 ]
}
```

--- paso 4 · ver_nodo · input={"id": "Obligacion_las_entidades_financieras_las_empresas_no_financieras_emisoras_de_tarjetas_de_cr"} · runtime=688 chars · re-ejecutado=688 chars ---

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

--- paso 5 · ver_nodo · input={"id": "TextoOrdenado_to_clasificacion_deudores_actual_pdf"} · runtime=397 chars · re-ejecutado=397 chars ---

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

--- paso 6 · buscar_nodos · input={"consulta": "protección usuario proveedores no financieros", "limite": 10} · runtime=3197 chars · re-ejecutado=3197 chars ---

```json
{
 "consulta": "protección usuario proveedores no financieros",
 "total_con_match": 443,
 "resultados": [
  {
   "id": "Obligacion_la_gerencia_principal_de_proteccion_al_usuario_de_servicios_financieros_tramitar",
   "type": "Obligacion",
   "label": "Tramitar denuncias de asociaciones",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La Gerencia Principal de Protección al Usuario de Servicios Financieros tramitará las denuncias que presenten las asociaciones de consumidores y usuarios recono…"
  },
  {
   "id": "EntidadFinanciera_proveedor_no_financiero_de_credito",
   "type": "EntidadFinanciera",
   "label": "Proveedores no financieros de crédito",
   "tokens_matcheados": 3,
   "resumen_propiedades": "categoria: proveedor no financiero de crédito"
  },
  {
   "id": "Obligacion_la_gerencia_principal_de_proteccion_al_usuario_de_servicios_financieros_brindara",
   "type": "Obligacion",
   "label": "Brindar respuesta a consultas sobre normativa",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La Gerencia Principal de Protección al Usuario de Servicios Financieros brindará respuesta por los medios habilitados a las consultas del público sobre la norma…"
  },
  {
   "id": "TextoOrdenado_to_proteccion_usuarios_servicios_financieros_actual_pdf",
   "type": "TextoOrdenado",
   "label": "Protección de Usuarios",
   "tokens_matcheados": 2,
   "resumen_propiedades": "materia: Protección de los usuarios de servicios financieros; archivo: TO_proteccion_usuarios_servicios_financieros_actual.pdf; version: 8a"
  },
  {
   "id": "EntidadFinanciera_cliente_privado_no_financiero",
   "type": "EntidadFinanciera",
   "label": "Clientes privados no financieros",
   "tokens_matcheados": 2,
   "resumen_propiedades": "categoria: cliente del sector privado no financiero"
  },
  {
   "id": "Obligacion_el_usuario_de_servicios_financieros_debe_ser_notificado_de_las_modificaciones_qu",
   "type": "Obligacion",
   "label": "Notificar cambios de condiciones",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El usuario de servicios financieros debe ser notificado de las modificaciones que aplicará el sujeto obligado con una antelación mínima de sesenta (60) días cor…"
  },
  {
   "id": "Operacion_atencion_al_usuario_de_servicios_financieros",
   "type": "Operacion",
   "label": "Atención de consultas y reclamos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: atención al usuario de servicios financieros"
  },
  {
   "id": "EntidadFinanciera_usuario_de_servicio_financiero",
   "type": "EntidadFinanciera",
   "label": "Usuarios de servicios financieros",
   "tokens_matcheados": 2,
   "resumen_propiedades": "categoria: usuario de servicio financiero"
  },
  {
   "id": "Restriccion_en_los_contratos_celebrados_entre_el_usuario_de_servicios_financieros_y_los_suje",
   "type": "Restriccion",
   "label": "Prohibición de cláusulas abusivas",
   "tokens_matcheados": 2,
   "resumen_propiedades": "En los contratos celebrados entre el usuario de servicios financieros y los sujetos obligados, se tendrán por no escritas las cláusulas que desnaturalicen las o…"
  },
  {
   "id": "Operacion_enajenacion_de_activos_no_financieros_no_producidos",
   "type": "Operacion",
   "label": "Enajenación de activos no producidos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Enajenación a no residentes de activos no financieros no producidos por parte de residentes"
  }
 ]
}
```

--- paso 7 · ver_nodo · input={"id": "TextoOrdenado_to_proteccion_usuarios_servicios_financieros_actual_pdf"} · runtime=434 chars · re-ejecutado=434 chars ---

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

--- paso 8 · buscar_nodos · input={"consulta": "clasificación deudores proveedores no financieros empresas emisoras tarjetas", "limite": 10} · runtime=3143 chars · re-ejecutado=3143 chars ---

```json
{
 "consulta": "clasificación deudores proveedores no financieros empresas emisoras tarjetas",
 "total_con_match": 492,
 "resultados": [
  {
   "id": "Obligacion_las_entidades_financieras_las_empresas_no_financieras_emisoras_de_tarjetas_de_cr",
   "type": "Obligacion",
   "label": "Designar Directivo Responsable de Protección",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Las entidades financieras, las empresas no financieras emisoras de tarjetas de crédito y/o compra y los otros proveedores no financieros de crédito deberán desi…"
  },
  {
   "id": "Restriccion_las_entidades_financieras_y_las_empresas_no_financieras_emisoras_de_tarjetas_loc",
   "type": "Restriccion",
   "label": "Conformidad previa BCRA acceso mercado cambios",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Las entidades financieras y las empresas no financieras emisoras de tarjetas locales deberán contar con la conformidad previa del BCRA para acceder al mercado d…"
  },
  {
   "id": "EntidadFinanciera_empresa_emisora_de_tarjeta",
   "type": "EntidadFinanciera",
   "label": "Empresas emisoras de tarjetas",
   "tokens_matcheados": 3,
   "resumen_propiedades": "categoria: empresa emisora de tarjetas de crédito"
  },
  {
   "id": "Restriccion_no_seran_objeto_de_clasificacion_quienes_resulten_deudores_en_operaciones_de_ces",
   "type": "Restriccion",
   "label": "Exclusión de deudores en cesión",
   "tokens_matcheados": 3,
   "resumen_propiedades": "No serán objeto de clasificación quienes resulten deudores en operaciones de cesión sin responsabilidad para el cedente"
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
   "id": "EntidadFinanciera_proveedor_no_financiero_de_credito",
   "type": "EntidadFinanciera",
   "label": "Proveedores no financieros de crédito",
   "tokens_matcheados": 3,
   "resumen_propiedades": "categoria: proveedor no financiero de crédito"
  },
  {
   "id": "Restriccion_deudores_que_no_deben_ser_objeto_de_clasificacion",
   "type": "Restriccion",
   "label": "Exclusión de deudores de clasificación",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Deudores que no deben ser objeto de clasificación"
  },
  {
   "id": "EntidadFinanciera_entidad_no_financiera_emisora_de_tarjeta",
   "type": "EntidadFinanciera",
   "label": "Entidades no financieras emisoras de tarjetas",
   "tokens_matcheados": 3,
   "resumen_propiedades": "categoria: entidad no financiera emisora de tarjetas de crédito"
  },
  {
   "id": "TextoOrdenado_to_clasificacion_deudores_actual_pdf",
   "type": "TextoOrdenado",
   "label": "Clasificación de Deudores",
   "tokens_matcheados": 2,
   "resumen_propiedades": "materia: clasificacion_deudores; archivo: TO_clasificacion_deudores_actual.pdf; version: vigente"
  }
 ]
}
```

--- paso 9 · buscar_nodos · input={"consulta": "criterios clasificación deudores situación categoría", "limite": 10} · runtime=3089 chars · re-ejecutado=3089 chars ---

```json
{
 "consulta": "criterios clasificación deudores situación categoría",
 "total_con_match": 114,
 "resultados": [
  {
   "id": "Operacion_clasificacion_de_deudores_en_situacion_irregular",
   "type": "Operacion",
   "label": "Incremento cartera irregular",
   "tokens_matcheados": 3,
   "resumen_propiedades": "tipo: clasificación de deudores en situación irregular"
  },
  {
   "id": "Operacion_clasificacion_de_deudor_en_categoria",
   "type": "Operacion",
   "label": "Clasificación de deudor",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: clasificación de deudor en categoría"
  },
  {
   "id": "TextoOrdenado_to_clasificacion_deudores_actual_pdf",
   "type": "TextoOrdenado",
   "label": "Clasificación de Deudores",
   "tokens_matcheados": 2,
   "resumen_propiedades": "materia: clasificacion_deudores; archivo: TO_clasificacion_deudores_actual.pdf; version: vigente"
  },
  {
   "id": "Obligacion_correspondera_clasificar_en_esta_categoria_a_los_clientes_que_cualquiera_sea_el_",
   "type": "Obligacion",
   "label": "Evaluación periódica deudores",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Corresponderá clasificar en esta categoría a los clientes que, cualquiera sea el motivo (entre ellos por no contar con legajo o por no haber proporcionado infor…"
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
  }
 ]
}
```

--- paso 10 · ver_vecinos · input={"id": "TextoOrdenado_to_clasificacion_deudores_actual_pdf", "direccion": "salientes"} · runtime=9756 chars · re-ejecutado=9756 chars ---

```json
{
 "id": "TextoOrdenado_to_clasificacion_deudores_actual_pdf",
 "label": "Clasificación de Deudores",
 "n_salientes_total": 189,
 "n_entrantes_total": 235,
 "salientes": [
  {
   "relation": "referencia",
   "vecino_id": "Comunicacion_a_5067",
   "vecino_label": "Com. A 5067",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "Punto 1.1. “A” 2216 I 1° Incluye aclaración interpretativa."
    }
   ]
  },
  {
   "relation": "modificada_por",
   "vecino_id": "Comunicacion_a_2514",
   "vecino_label": "Com. A 2514",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "Punto 1.1. “A” 2216 I 1° Incluye aclaración interpretativa."
    }
   ]
  },
  {
   "relation": "modificada_por",
   "vecino_id": "Comunicacion_a_6428",
   "vecino_label": "Com. A 6428",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "Punto 1.1. “A” 2216 I 1° Incluye aclaración interpretativa."
    }
   ]
  },
  {
   "relation": "modificada_por",
   "vecino_id": "Comunicacion_a_2421",
   "vecino_label": "Com. A 2421",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "Punto 1.1. “A” 2216 I 1° Incluye aclaración interpretativa."
    }
   ]
  },
  {
   "relation": "referencia",
   "vecino_id": "Comunicacion_a_6396",
   "vecino_label": "Com. A 6396",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "Punto 1.1. “A” 2216 I 1° Incluye aclaración interpretativa."
    }
   ]
  },
  {
   "relation": "referencia",
   "vecino_id": "Comunicacion_a_2729",
   "vecino_label": "Com. A 2729",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "Punto 1.2. Criterios especiales de imputación."
    }
   ]
  },
  {
   "relation": "modificada_por",
   "vecino_id": "Comunicacion_a_2950",
   "vecino_label": "Com. A 2950",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "Punto 1.2. Criterios especiales de imputación."
    }
   ]
  },
  {
   "relation": "referencia",
   "vecino_id": "Comunicacion_a_5275",
   "vecino_label": "Com. A 5275",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "Punto 10.3. “A” 3141 4. Según Com. “A” 5275. (parte 1)"
    }
   ]
  },
  {
   "relation": "referencia",
   "vecino_id": "Comunicacion_a_7406",
   "vecino_label": "Com. A 7406",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "Punto 10.3. “A” 3141 4. Según Com. “A” 5275. (parte 2)"
    }
   ]
  },
  {
   "relation": "referencia",
   "vecino_id": "Comunicacion_a_7423",
   "vecino_label": "Com. A 7423",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "Punto 10.3. “A” 3141 4. Según Com. “A” 5275. (parte 2)"
    }
   ]
  },
  {
   "relation": "modificada_por",
   "vecino_id": "Comunicacion_a_7687",
   "vecino_label": "Com. A 7687",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "Punto 10.3. “A” 3141 4. Según Com. “A” 5275. (parte 2)"
    }
   ]
  },
  {
   "relation": "modificada_por",
   "vecino_id": "Comunicacion_a_7928",
   "vecino_label": "Com. A 7928",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "Punto 10.3. “A” 3141 4. Según Com. “A” 5275. (parte 2)"
    }
   ]
  },
  {
   "relation": "modificada_por",
   "vecino_id": "Comunicacion_a_7937",
   "vecino_label": "Com. A 7937",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "Punto 10.3. “A” 3141 4. Según Com. “A” 5275. (parte 2)"
    }
   ]
  },
  {
   "relation": "modificada_por",
   "vecino_id": "Comunicacion_a_8215",
   "vecino_label": "Com. A 8215",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "Punto 10.3. “A” 3141 4. Según Com. “A” 5275. (parte 2)"
    }
   ]
  },
  {
   "relation": "modificada_por",
   "vecino_id": "Comunicacion_a_8378",
   "vecino_label": "Com. A 8378",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "Punto 10.3. “A” 3141 4. Según Com. “A” 5275. (parte 2)"
    }
   ]
  },
  {
   "relation": "referencia",
   "vecino_id": "Comunicacion_a_467",
   "vecino_label": "Com. A 467",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "Punto 10.3. “A” 3141 4. Según Com. “A” 5275. (parte 2)"
    }
   ]
  },
  {
   "relation": "referencia",
   "vecino_id": "Comunicacion_a_2216",
   "vecino_label": "Com. A 2216",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "Punto 10.3. “A” 3141 4. Según Com. “A” 5275. (parte 2)"
    }
   ]
  },
  {
   "relation": "referencia",
   "vecino_id": "Comunicacion_a_2223",
   "vecino_label": "Com. A 2223",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "Punto 10.3. “A” 3141 4. Según Com. “A” 5275. (parte 2)"
    }
   ]
  },
  {
   "relation": "referencia",
   "vecino_id": "Comunicacion_a_2227",
   "vecino_label": "Com. A 2227",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "Punto 10.3. “A” 3141 4. Según Com. “A” 5275. (parte 2)"
    }
   ]
  },
  {
   "relation": "referencia",
   "vecino_id": "Comunicacion_a_2287",
   "vecino_label": "Com. A 2287",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "Punto 10.3. “A” 3141 4. Según Com. “A” 5275. (parte 2)"
    }
   ]
  },
  {
   "relation": "referencia",
   "vecino_id": "Comunicacion_a_2358",
   "vecino_label": "Com. A 2358",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "Punto 10.3. “A” 3141 4. Según Com. “A” 5275. (parte 2)"
    }
   ]
  },
  {
   "relation": "referencia",
   "vecino_id": "Comunicacion_a_2373",
   "vecino_label": "Com. A 2373",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "Punto 10.3. “A” 3141 4. Según Com. “A” 5275. (parte 2)"
    }
   ]
  },
  {
   "relation": "referencia",
   "vecino_id": "Comunicacion_a_2389",
   "vecino_label": "Com. A 2389",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "Punto 10.3. “A” 3141 4. Según Com. “A” 5275. (parte 2)"
    }
   ]
  },
  {
   "relation": "referencia",
   "vecino_id": "Comunicacion_a_2410",
   "vecino_label": "Com. A 2410",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "Punto 10.3. “A” 3141 4. Según Com. “A” 5275. (parte 2)"
    }
   ]
  },
  {
   "relation": "referencia",
   "vecino_id": "Comunicacion_a_2412",
   "vecino_label": "Com. A 2412",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "Punto 10.3. “A” 3141 4. Según Com. “A” 5275. (parte 2)"
    }
   ]
  },
  {
   "relation": "referencia",
   "vecino_id": "Comunicacion_a_2414",
   "vecino_label": "Com. A 2414",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "Punto 10.3. “A” 3141 4. Según Com. “A” 5275. (parte 2)"
    }
   ]
  },
  {
   "relation": "referencia",
   "vecino_id": "Comunicacion_a_2427",
   "vecino_label": "Com. A 2427",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "Punto 10.3. “A” 3141 4. Según Com. “A” 5275. (parte 2)"
    }
   ]
  },
  {
   "relation": "referencia",
   "vecino_id": "Comunicacion_a_2440",
   "vecino_label": "Com. A 2440",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "Punto 10.3. “A” 3141 4. Según Com. “A” 5275. (parte 2)"
    }
   ]
  },
  {
   "relation": "referencia",
   "vecino_id": "Comunicacion_a_2448",
   "vecino_label": "Com. A 2448",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "Punto 10.3. “A” 3141 4. Según Com. “A” 5275. (parte 2)"
    }
   ]
  },
  {
   "relation": "referencia",
   "vecino_id": "Comunicacion_a_2497",
   "vecino_label": "Com. A 2497",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "Punto 10.3. “A” 3141 4. Según Com. “A” 5275. (parte 2)"
    }
   ]
  },
  {
   "relation": "referencia",
   "vecino_id": "Comunicacion_a_2562",
   "vecino_label": "Com. A 2562",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "Punto 10.3. “A” 3141 4. Según Com. “A” 5275. (parte 2)"
    }
   ]
  },
  {
   "relation": "referencia",
   "vecino_id": "Comunicacion_a_2563",
   "vecino_label": "Com. A 2563",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "Punto 10.3. “A” 3141 4. Según Com. “A” 5275. (parte 2)"
    }
   ]
  },
  {
   "relation": "referencia",
   "vecino_id": "Comunicacion_a_2573",
   "vecino_label": "Com. A 2573",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "Punto 10.3. “A” 3141 4. Según Com. “A” 5275. (parte 2)"
    }
   ]
  },
  {
   "relation": "referencia",
   "vecino_id": "Comunicacion_a_2580",
   "vecino_label": "Com. A 2580",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "Punto 10.3. “A” 3141 4. Según Com. “A” 5275. (parte 2)"
    }
   ]
  },
  {
   "relation": "referencia",
   "vecino_id": "Comunicacion_a_2586",
   "vecino_label": "Com. A 2586",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "Punto 10.3. “A” 3141 4. Según Com. “A” 5275. (parte 2)"
    }
   ]
  },
  {
   "relation": "referencia",
   "vecino_id": "Comunicacion_a_2587",
   "vecino_label": "Com. A 2587",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "Punto 10.3. “A” 3141 4. Según Com. “A” 5275. (parte 2)"
    }
   ]
  },
  {
   "relation": "referencia",
   "vecino_id": "Comunicacion_a_2649",
   "vecino_label": "Com. A 2649",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "Punto 10.3. “A” 3141 4. Según Com. “A” 5275. (parte 2)"
    }
   ]
  },
  {
   "relation": "referencia",
   "vecino_id": "Comunicacion_a_2677",
   "vecino_label": "Com. A 2677",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "Punto 10.3. “A” 3141 4. Según Com. “A” 5275. (parte 2)"
    }
   ]
  },
  {
   "relation": "referencia",
   "vecino_id": "Comunicacion_a_2703",
   "vecino_label": "Com. A 2703",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "Punto 10.3. “A” 3141 4. Según Com. “A” 5275. (parte 2)"
    }
   ]
  },
  {
   "relation": "referencia",
   "vecino_id": "Comunicacion_a_2736",
   "vecino_label": "Com. A 2736",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "Punto 10.3. “A” 3141 4. Según Com. “A” 5275. (parte 2)"
    }
   ]
  }
 ],
 "salientes_truncado": true
}
```

--- paso 11 · buscar_nodos · input={"consulta": "normal riesgo deficiente irrecuperable clasificación", "limite": 10} · runtime=3095 chars · re-ejecutado=3095 chars ---

```json
{
 "consulta": "normal riesgo deficiente irrecuperable clasificación",
 "total_con_match": 229,
 "resultados": [
  {
   "id": "Operacion_clasificacion_de_riesgo_de_deudor",
   "type": "Operacion",
   "label": "Clasificación deudor nivel riesgo",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: clasificación de riesgo de deudor"
  },
  {
   "id": "Obligacion_para_clasificacion_en_situacion_normal_el_analisis_del_flujo_de_fondos_del_clien",
   "type": "Obligacion",
   "label": "Evaluación situación financiera normal",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Para clasificación en situación normal: El análisis del flujo de fondos del cliente demuestra que es capaz de atender adecuadamente todos sus compromisos financ…"
  },
  {
   "id": "Restriccion_en_caso_de_no_efectuarse_la_evaluacion_de_creditos_cedidos_sin_responsabilidad_c",
   "type": "Restriccion",
   "label": "Clasificación irrecuperable sin evaluación",
   "tokens_matcheados": 2,
   "resumen_propiedades": "En caso de no efectuarse la evaluación de créditos cedidos sin responsabilidad, cualquiera sea el motivo, estos clientes se clasificarán en categoría irrecupera…"
  },
  {
   "id": "Obligacion_a_los_fines_de_asignar_los_ponderadores_de_riesgo_previstos_en_el_punto_2_12_las",
   "type": "Obligacion",
   "label": "Considerar definiciones clasificación empresas",
   "tokens_matcheados": 2,
   "resumen_propiedades": "A los fines de asignar los ponderadores de riesgo previstos en el punto 2.12., las entidades financieras deberán considerar las siguientes definiciones"
  },
  {
   "id": "Obligacion_exigencia_por_riesgo_de_credito_de_contraparte_en_operaciones_con_derivados_extr",
   "type": "Obligacion",
   "label": "Cálculo de RCD",
   "tokens_matcheados": 1,
   "resumen_propiedades": "exigencia por riesgo de crédito de contraparte en operaciones con derivados extrabursátiles (over-the-counter, OTC), determinada conforme a lo establecido en el…"
  },
  {
   "id": "Operacion_calculo_de_promedio_de_exigencias_de_riesgo_operacional",
   "type": "Operacion",
   "label": "Cálculo promedio ERC",
   "tokens_matcheados": 1,
   "resumen_propiedades": "tipo: cálculo de promedio de exigencias de riesgo operacional"
  },
  {
   "id": "Operacion_clasificacion_de_cartera",
   "type": "Operacion",
   "label": "Agrupación de cartera",
   "tokens_matcheados": 1,
   "resumen_propiedades": "tipo: clasificación de cartera"
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
   "id": "Operacion_clasificacion_de_deudor_en_categoria",
   "type": "Operacion",
   "label": "Clasificación de deudor",
   "tokens_matcheados": 1,
   "resumen_propiedades": "tipo: clasificación de deudor en categoría"
  }
 ]
}
```

--- paso 12 · buscar_nodos · input={"consulta": "análisis flujo fondos capacidad pago deudor", "limite": 10} · runtime=3354 chars · re-ejecutado=3354 chars ---

```json
{
 "consulta": "análisis flujo fondos capacidad pago deudor",
 "total_con_match": 285,
 "resultados": [
  {
   "id": "Operacion_analisis_de_capacidad_de_pago",
   "type": "Operacion",
   "label": "Análisis de flujo de fondos del deudor",
   "tokens_matcheados": 6,
   "resumen_propiedades": "tipo: análisis de capacidad de pago"
  },
  {
   "id": "Operacion_analisis_de_flujo_de_fondos_del_cliente",
   "type": "Operacion",
   "label": "Análisis de flujo de fondos",
   "tokens_matcheados": 3,
   "resumen_propiedades": "tipo: análisis de flujo de fondos del cliente"
  },
  {
   "id": "Obligacion_la_entidad_debera_analizar_el_flujo_de_fondos_proyectado_para_clasificar_cliente",
   "type": "Obligacion",
   "label": "Análisis flujo fondos proyectado",
   "tokens_matcheados": 3,
   "resumen_propiedades": "La entidad deberá analizar el flujo de fondos proyectado para clasificar clientes que no registren asistencia crediticia previa."
  },
  {
   "id": "Obligacion_para_clasificacion_en_situacion_normal_el_analisis_del_flujo_de_fondos_del_clien",
   "type": "Obligacion",
   "label": "Evaluación situación financiera normal",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Para clasificación en situación normal: El análisis del flujo de fondos del cliente demuestra que es capaz de atender adecuadamente todos sus compromisos financ…"
  },
  {
   "id": "Obligacion_los_analisis_previos_al_otorgamiento_de_las_financiaciones_y_refinanciaciones_ta",
   "type": "Obligacion",
   "label": "Considerar capacidad de pago en financiaciones",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Los análisis previos al otorgamiento de las financiaciones y refinanciaciones también deben guardar relación con la capacidad de pago de los deudores, evaluando…"
  },
  {
   "id": "Obligacion_evaluar_capacidad_de_pago",
   "type": "Obligacion",
   "label": "Evaluar capacidad de pago",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El criterio básico a ser utilizado para efectuar la clasificación es la capacidad de pago en el futuro de la deuda o de los compromisos objeto de la garantía de…"
  },
  {
   "id": "Obligacion_analisis_de_flujos_de_fondos",
   "type": "Obligacion",
   "label": "Análisis de flujos de fondos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Al evaluar la capacidad de repago, el énfasis deberá ponerse en el análisis de los flujos de fondos realizado por la entidad."
  },
  {
   "id": "Restriccion_presente_una_situacion_financiera_iliquida_y_un_nivel_de_flujo_de_fondos_que_no_",
   "type": "Restriccion",
   "label": "Situación financiera ilíquida",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Presente una situación financiera ilíquida y un nivel de flujo de fondos que no le permita atender el pago de la totalidad del capital y de los intereses de las…"
  },
  {
   "id": "Restriccion_el_flujo_de_fondos_es_manifiestamente_insuficiente_no_alcanzando_a_cubrir_el_pag",
   "type": "Restriccion",
   "label": "Insuficiencia de flujo de fondos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El flujo de fondos es manifiestamente insuficiente, no alcanzando a cubrir el pago de intereses."
  },
  {
   "id": "Obligacion_las_entidades_financieras_deberan_establecer_politicas_para_el_otorgamiento_de_l",
   "type": "Obligacion",
   "label": "Políticas evaluación capacidad pago",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Las entidades financieras deberán establecer políticas para el otorgamiento de los préstamos con garantía hipotecaria que permitan una adecuada evaluación de la…"
  }
 ]
}
```

--- paso 13 · ver_nodo · input={"id": "Obligacion_evaluar_capacidad_de_pago"} · runtime=486 chars · re-ejecutado=486 chars ---

```json
{
 "id": "Obligacion_evaluar_capacidad_de_pago",
 "type": "Obligacion",
 "label": "Evaluar capacidad de pago",
 "properties": {
  "tipo": "calculo",
  "description": "El criterio básico a ser utilizado para efectuar la clasificación es la capacidad de pago en el futuro de la deuda o de los compromisos objeto de la garantía de la entidad financiera",
  "plazo": "futuro"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Punto 4.1. Niveles de clasificación."
  }
 ]
}
```

--- paso 14 · buscar_nodos · input={"consulta": "proveedores no financieros obligación clasificar deudores", "limite": 10} · runtime=3587 chars · re-ejecutado=3587 chars ---

```json
{
 "consulta": "proveedores no financieros obligación clasificar deudores",
 "total_con_match": 1621,
 "resultados": [
  {
   "id": "Obligacion_clasificar_deudores_por_mora",
   "type": "Obligacion",
   "label": "Clasificar deudores por mora",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Deberán clasificar a los respectivos deudores en función de su mora, según los criterios aplicables para la cartera de consumo o vivienda y por aplicación de la…"
  },
  {
   "id": "Obligacion_correspondera_clasificar_en_esta_categoria_a_los_clientes_que_cualquiera_sea_el_",
   "type": "Obligacion",
   "label": "Evaluación periódica deudores",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Corresponderá clasificar en esta categoría a los clientes que, cualquiera sea el motivo (entre ellos por no contar con legajo o por no haber proporcionado infor…"
  },
  {
   "id": "Obligacion_clasificar_deudores_segun_mora",
   "type": "Obligacion",
   "label": "Clasificar deudores según mora",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Los PSCPP deberán clasificar a los deudores de los créditos que administran en función de su mora, según los criterios aplicables para la cartera de consumo o v…"
  },
  {
   "id": "EntidadFinanciera_proveedor_no_financiero_de_credito",
   "type": "EntidadFinanciera",
   "label": "Proveedores no financieros de crédito",
   "tokens_matcheados": 3,
   "resumen_propiedades": "categoria: proveedor no financiero de crédito"
  },
  {
   "id": "Obligacion_debera_informar_en_las_notas_a_los_estados_financieros_de_publicacion_que_ha_pre",
   "type": "Obligacion",
   "label": "Informar respaldo crediticio no contractual",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Deberá informar en las notas a los estados financieros de publicación que ha prestado respaldo crediticio no contractual y el efecto sobre su exigencia de capit…"
  },
  {
   "id": "Obligacion_clasificar_deudores_de_creditos_fideicomitidos",
   "type": "Obligacion",
   "label": "Clasificar deudores de créditos fideicomitidos",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Deberán clasificar a los deudores de los créditos fideicomitidos de acuerdo con la periodicidad y demás condiciones establecidas para las carteras \"comercial\" o…"
  },
  {
   "id": "Obligacion_no_se_considerara_refinanciacion_la_asistencia_que_se_otorgue_a_los_deudores_cla",
   "type": "Obligacion",
   "label": "Evaluación de capacidad de pago para ampliación",
   "tokens_matcheados": 3,
   "resumen_propiedades": "No se considerará refinanciación la asistencia que se otorgue a los deudores clasificados en esta categoría siempre que implique mayor deuda por capital respect…"
  },
  {
   "id": "Obligacion_clasificar_mipymes_por_mora",
   "type": "Obligacion",
   "label": "Clasificar MiPyMEs por mora",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Deberán clasificar a las MiPyMEs cuyas deudas hayan sido canceladas en cumplimiento de las garantías que respaldaban las respectivas obligaciones. La clasificac…"
  },
  {
   "id": "Obligacion_se_procedera_a_clasificar_a_la_compania_de_seguros_en_funcion_de_la_mora_segun_l",
   "type": "Obligacion",
   "label": "Clasificar compañía según mora",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Se procederá a clasificar a la compañía de seguros en función de la mora según los criterios aplicables para la cartera de consumo, teniendo en cuenta la fecha …"
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

--- paso 15 · ver_nodo · input={"id": "Obligacion_clasificar_deudores_por_mora"} · runtime=559 chars · re-ejecutado=559 chars ---

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

---

# Apéndice CQ-019 — outputs completos (9 pasos re-ejecutables)


--- paso 1 · buscar_nodos · input={"consulta": "exigencia capital riesgo crédito previsión incobrabilidad", "limite": 10} · runtime=3374 chars · re-ejecutado=3374 chars ---

```json
{
 "consulta": "exigencia capital riesgo crédito previsión incobrabilidad",
 "total_con_match": 462,
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

--- paso 2 · buscar_nodos · input={"consulta": "previsión incobrabilidad deducción activos", "limite": 10} · runtime=3257 chars · re-ejecutado=3257 chars ---

```json
{
 "consulta": "previsión incobrabilidad deducción activos",
 "total_con_match": 115,
 "resultados": [
  {
   "id": "Restriccion_activos_intangibles_netos_de_la_respectiva_depreciacion_acumulada_incluye_la_lla",
   "type": "Restriccion",
   "label": "Deducción activos intangibles",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Activos intangibles, netos de la respectiva depreciación acumulada. Incluye la llave de negocio integrante de la valuación de inversiones significativas en el c…"
  },
  {
   "id": "Restriccion_la_diferencia_positiva_resultante_de_comparar_el_importe_de_la_prevision_regulat",
   "type": "Restriccion",
   "label": "Deducción de previsión NIIF 9",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La diferencia positiva resultante de comparar el importe de la previsión regulatoria o la contable correspondiente al balance de saldos al 30.11.19, la mayor de…"
  },
  {
   "id": "Restriccion_limite_de_deduccion_de_prevision_normal",
   "type": "Restriccion",
   "label": "Límite de deducción de previsión normal",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Sin deducir el 100% del importe de la previsión por riesgo de incobrabilidad correspondiente a la cartera de deudores clasificados 'en situación normal' –puntos…"
  },
  {
   "id": "Operacion_venta_de_activos_de_importancia_para_la_actividad_desarrollada",
   "type": "Operacion",
   "label": "Venta de activos",
   "tokens_matcheados": 1,
   "resumen_propiedades": "tipo: venta de activos de importancia para la actividad desarrollada"
  },
  {
   "id": "Operacion_seleccion_de_subyacentes_mediante_criterios_de_elegibilidad",
   "type": "Operacion",
   "label": "Selección de activos",
   "tokens_matcheados": 1,
   "resumen_propiedades": "La selección de los activos deberá estar sujeta a criterios de elegibilidad claramente definidos, tales como el tamaño de la obligación, la edad del sujeto de c…"
  },
  {
   "id": "Restriccion_accionistas",
   "type": "Restriccion",
   "label": "Deducción accionistas",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Accionistas"
  },
  {
   "id": "Operacion_transferencia_de_documentos_a_cobrar_y_derechos_de_credito",
   "type": "Operacion",
   "label": "Transferencia de activos",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Transferencia de activos (documentos a cobrar o derechos de crédito) en el contexto de una titulización."
  },
  {
   "id": "Operacion_tenencia_de_activos",
   "type": "Operacion",
   "label": "Tenencia de oro amonedado",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Oro amonedado o en barras de buena entrega conforme TO Exterior y Cambios, individualizado on an allocated basis, respaldado por pasivos en estas especies"
  },
  {
   "id": "Restriccion_condiciones_pases_activos",
   "type": "Restriccion",
   "label": "Condiciones pases activos",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Pases activos de dólares estadounidenses y de títulos valores públicos nacionales, siempre que: las especies transadas cuenten con un mercado de operaciones hab…"
  },
  {
   "id": "Obligacion_la_epf_resultara_del_producto_entre_la_suma_de_adicionales_por_clase_de_activos_",
   "type": "Obligacion",
   "label": "Calcular EPF multiplicador",
   "tokens_matcheados": 1,
   "resumen_propiedades": "La EPF resultará del producto entre la suma de adicionales por clase de activos y un multiplicador que reconoce garantía en exceso o valor de mercado negativo"
  }
 ]
}
```

--- paso 3 · buscar_nodos · input={"consulta": "clasificación deudores previsión", "limite": 10} · runtime=3280 chars · re-ejecutado=3280 chars ---

```json
{
 "consulta": "clasificación deudores previsión",
 "total_con_match": 88,
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
   "id": "Obligacion_se_volcaran_en_un_manual_de_procedimientos_de_clasificacion_y_prevision_los_proc",
   "type": "Obligacion",
   "label": "Volcar procedimientos en Manual",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Se volcarán en un 'Manual de procedimientos de clasificación y previsión' los procedimientos implementados, los niveles que intervienen en el análisis y decisió…"
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
   "id": "Restriccion_incluye_deudores_con_obligaciones_iguales_o_superiores_al_20_del_patrimonio_o_en",
   "type": "Restriccion",
   "label": "Clasificación por obligaciones insolventes",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Incluye deudores con obligaciones iguales o superiores al 20% del patrimonio, o entre 5% y menos del 20% cuando persista pedido de quiebra después de 90 días"
  },
  {
   "id": "Restriccion_los_deudores_cuyas_financiaciones_se_encuentren_cubiertas_totalmente_con_garanti",
   "type": "Restriccion",
   "label": "Prohibición de clasificación por cobertura total",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Los deudores cuyas financiaciones se encuentren cubiertas totalmente con garantías preferidas A no serán objeto de clasificación, sin perjuicio de su informació…"
  }
 ]
}
```

--- paso 4 · ver_nodo · input={"id": "Restriccion_limite_de_deduccion_de_prevision_normal"} · runtime=630 chars · re-ejecutado=630 chars ---

```json
{
 "id": "Restriccion_limite_de_deduccion_de_prevision_normal",
 "type": "Restriccion",
 "label": "Límite de deducción de previsión normal",
 "properties": {
  "tipo": "limite_cualitativo",
  "description": "Sin deducir el 100% del importe de la previsión por riesgo de incobrabilidad correspondiente a la cartera de deudores clasificados 'en situación normal' –puntos 6.5.1. y 7.2.1. del TO sobre Clasificación de Deudores– y a las financiaciones que se encuentran cubiertas con garantías preferidas A)."
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Punto 2.3. Cómputo de los conceptos comprendidos."
  }
 ]
}
```

--- paso 5 · ver_nodo · input={"id": "Operacion_calculo_de_exigencia_de_capital_minimo_por_riesgo_de_credito"} · runtime=367 chars · re-ejecutado=367 chars ---

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

--- paso 6 · ver_vecinos · input={"id": "Restriccion_limite_de_deduccion_de_prevision_normal", "direccion": "ambas"} · runtime=762 chars · re-ejecutado=762 chars ---

```json
{
 "id": "Restriccion_limite_de_deduccion_de_prevision_normal",
 "label": "Límite de deducción de previsión normal",
 "n_salientes_total": 2,
 "n_entrantes_total": 0,
 "salientes": [
  {
   "relation": "establecida_en",
   "vecino_id": "TextoOrdenado_to_capitales_minimos_actual_pdf",
   "vecino_label": "Capitales Mínimos",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 2.3. Cómputo de los conceptos comprendidos."
    }
   ]
  },
  {
   "relation": "limita",
   "vecino_id": "Operacion_computo",
   "vecino_label": "Cómputo de conceptos en base mensual",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 2.3. Cómputo de los conceptos comprendidos."
    }
   ]
  }
 ],
 "salientes_truncado": false,
 "entrantes": [],
 "entrantes_truncado": false
}
```

--- paso 7 · buscar_nodos · input={"consulta": "deudores situación normal previsión", "limite": 10} · runtime=3230 chars · re-ejecutado=3230 chars ---

```json
{
 "consulta": "deudores situación normal previsión",
 "total_con_match": 60,
 "resultados": [
  {
   "id": "Restriccion_los_deudores_que_hayan_cancelado_la_totalidad_de_los_intereses_devengados_podran",
   "type": "Restriccion",
   "label": "Cancelación de intereses para situación normal",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Los deudores que hayan cancelado la totalidad de los intereses devengados, podrán ser clasificados en 'situación normal' si además observan las otras condicione…"
  },
  {
   "id": "Operacion_clasificacion_de_deudores_en_situacion_irregular",
   "type": "Operacion",
   "label": "Incremento cartera irregular",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: clasificación de deudores en situación irregular"
  },
  {
   "id": "Operacion_estado_de_situacion_de_deudores",
   "type": "Operacion",
   "label": "Estado de situación de deudores",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Estado de situación de deudores referenciado en punto 6.1. y 6.2."
  },
  {
   "id": "Restriccion_comprende_los_clientes_que_atienden_en_forma_puntual_el_pago_de_sus_obligaciones",
   "type": "Restriccion",
   "label": "Límite de atraso en situación normal",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Comprende los clientes que atienden en forma puntual el pago de sus obligaciones o con atrasos que no superan los 31 días"
  },
  {
   "id": "Obligacion_para_clasificacion_en_situacion_normal_el_analisis_del_flujo_de_fondos_del_clien",
   "type": "Obligacion",
   "label": "Evaluación situación financiera normal",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Para clasificación en situación normal: El análisis del flujo de fondos del cliente demuestra que es capaz de atender adecuadamente todos sus compromisos financ…"
  },
  {
   "id": "Restriccion_limite_de_deduccion_de_prevision_normal",
   "type": "Restriccion",
   "label": "Límite de deducción de previsión normal",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Sin deducir el 100% del importe de la previsión por riesgo de incobrabilidad correspondiente a la cartera de deudores clasificados 'en situación normal' –puntos…"
  },
  {
   "id": "Obligacion_informar_cambios_negativos_a_deudores_en_situacion_3_5",
   "type": "Obligacion",
   "label": "Informar cambios negativos a deudores en situación 3-5",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Deberán informarse los cambios negativos en la clasificación a los deudores que sean clasificados en las situaciones 3, 4 o 5 y de los deudores en gestión judic…"
  },
  {
   "id": "EntidadFinanciera_deudor",
   "type": "EntidadFinanciera",
   "label": "Deudores",
   "tokens_matcheados": 1,
   "resumen_propiedades": "categoria: deudor"
  },
  {
   "id": "Restriccion_incurra_en_atrasos_de_hasta_180_dias_con_exclusion_de_los_deudores_comprendidos_",
   "type": "Restriccion",
   "label": "Atrasos hasta 180 días",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Incurra en atrasos de hasta 180 días, con exclusión de los deudores comprendidos en el punto 6.5.2.2."
  },
  {
   "id": "Restriccion_el_cliente_presente_una_situacion_financiera_mala_con_suspension_de_pagos_quiebr",
   "type": "Restriccion",
   "label": "Situación financiera mala",
   "tokens_matcheados": 1,
   "resumen_propiedades": "El cliente presente una situación financiera mala con suspensión de pagos, quiebra decretada o pedido de su propia quiebra."
  }
 ]
}
```

--- paso 8 · buscar_nodos · input={"consulta": "garantías preferidas A previsión deducción", "limite": 10} · runtime=3763 chars · re-ejecutado=3763 chars ---

```json
{
 "consulta": "garantías preferidas A previsión deducción",
 "total_con_match": 1204,
 "resultados": [
  {
   "id": "Restriccion_no_correspondera_la_evaluacion_de_la_capacidad_de_repago_respecto_de_las_financi",
   "type": "Restriccion",
   "label": "Excención de evaluación por garantías preferidas A",
   "tokens_matcheados": 3,
   "resumen_propiedades": "No corresponderá la evaluación de la capacidad de repago respecto de las financiaciones que se encuentren respaldadas con tales garantías"
  },
  {
   "id": "Obligacion_se_incrementara_el_valor_de_los_activos_en_garantia_dados_por_la_entidad_y_se_re",
   "type": "Obligacion",
   "label": "Aplicar aforos a garantías",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Se incrementará el valor de los activos en garantía dados por la entidad y se reducirá el valor de los recibidos, utilizando aforos aplicables a transacciones R…"
  },
  {
   "id": "Restriccion_la_diferencia_positiva_resultante_de_comparar_el_importe_de_la_prevision_regulat",
   "type": "Restriccion",
   "label": "Deducción de previsión NIIF 9",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La diferencia positiva resultante de comparar el importe de la previsión regulatoria o la contable correspondiente al balance de saldos al 30.11.19, la mayor de…"
  },
  {
   "id": "Obligacion_a_fin_de_determinar_el_importe_de_la_cancelacion_se_admitira_computar_el_50_de_l",
   "type": "Obligacion",
   "label": "Computar garantías adicionales",
   "tokens_matcheados": 2,
   "resumen_propiedades": "A fin de determinar el importe de la cancelación, se admitirá computar el 50 % de las garantías adicionales a las ofrecidas originalmente, constituidas sobre bi…"
  },
  {
   "id": "Obligacion_reportar_en_el_sepaimpo_dentro_de_los_5_cinco_dias_habiles_siguientes_a_la_fecha",
   "type": "Obligacion",
   "label": "Reportar cancelación de garantías",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Reportar en el SEPAIMPO dentro de los 5 (cinco) días hábiles siguientes a la fecha de acceso al mercado de cambios, la CUIT y nombre del cliente por el cual se …"
  },
  {
   "id": "Restriccion_ponderador_2_para_garantias_a_ccp",
   "type": "Restriccion",
   "label": "Ponderador 2% para garantías a CCP",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Cuando la entidad que reciba los activos en garantía sea la CCP, se aplicará un ponderador del 2% a las garantías incluidas en la definición de exposición por o…"
  },
  {
   "id": "Obligacion_si_un_miembro_compensador_recibe_activos_en_garantia_por_las_operaciones_a_compe",
   "type": "Obligacion",
   "label": "Reconocer garantías en ambos tramos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Si un miembro compensador recibe activos en garantía por las operaciones a compensar del cliente y las transfiere a la CCP, el miembro compensador podrá reconoc…"
  },
  {
   "id": "Excepcion_si_la_entidad_financiera_carece_de_suficiente_capital_para_efectuar_la_deduccion",
   "type": "Excepcion",
   "label": "Remanente trasferido a nivel superior",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Si la entidad financiera carece de suficiente capital para efectuar la deducción de un nivel particular de capital, el remanente se deducirá del nivel inmediato…"
  },
  {
   "id": "Restriccion_titulos_de_credito_titulos_valores_certificados_de_depositos_a_plazo_fijo_y_otro",
   "type": "Restriccion",
   "label": "Deducción títulos no en poder entidad",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Títulos de crédito (títulos valores, certificados de depósitos a plazo fijo y otros) que físicamente no se encuentren en poder de la entidad, salvo que su regis…"
  },
  {
   "id": "Excepcion_garantias_otorgadas_a_favor_del_banco_central_estan_excluidas",
   "type": "Excepcion",
   "label": "Exclusión de garantías a favor del BCRA",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Garantías otorgadas a favor del Banco Central están excluidas"
  }
 ]
}
```

--- paso 9 · ver_nodo · input={"id": "Operacion_computo"} · runtime=459 chars · re-ejecutado=459 chars ---

```json
{
 "id": "Operacion_computo",
 "type": "Operacion",
 "label": "Cómputo de conceptos en base mensual",
 "properties": {
  "tipo": "cómputo",
  "description": "Cómputo de los conceptos comprendidos sobre la base de los saldos al último día de cada mes (capitales, intereses, primas, actualizaciones por CER y diferencias de cotización)"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Punto 2.3. Cómputo de los conceptos comprendidos."
  }
 ]
}
```

---

# Apéndice CQ-024 — outputs completos (15 pasos re-ejecutables)


--- paso 1 · buscar_nodos · input={"consulta": "clasificación deudor cartera comercial RPC periodicidad", "limite": 10} · runtime=2629 chars · re-ejecutado=2629 chars ---

```json
{
 "consulta": "clasificación deudor cartera comercial RPC periodicidad",
 "total_con_match": 159,
 "resultados": [
  {
   "id": "EntidadFinanciera_deudor_cartera_comercial",
   "type": "EntidadFinanciera",
   "label": "Deudores cartera comercial",
   "tokens_matcheados": 3,
   "resumen_propiedades": "categoria: deudor cartera comercial"
  },
  {
   "id": "Operacion_clasificacion_de_cartera",
   "type": "Operacion",
   "label": "Agrupación de cartera",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: clasificación de cartera"
  },
  {
   "id": "Operacion_clasificacion_de_deudor_en_categoria",
   "type": "Operacion",
   "label": "Clasificación de deudor",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: clasificación de deudor en categoría"
  },
  {
   "id": "Operacion_clasificacion_de_deudor_segun_mora",
   "type": "Operacion",
   "label": "Clasificación de deudor",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: clasificación de deudor según mora"
  },
  {
   "id": "Operacion_revision_de_cartera",
   "type": "Operacion",
   "label": "Revisión cartera comercial",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La revisión de la cartera comercial se practicará sobre la base de la información financiera actualizada"
  },
  {
   "id": "Operacion_clasificacion_de_deudores_en_situacion_irregular",
   "type": "Operacion",
   "label": "Incremento cartera irregular",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: clasificación de deudores en situación irregular"
  },
  {
   "id": "Operacion_clasificacion_de_deudor",
   "type": "Operacion",
   "label": "Evaluación grado de inversión",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Clasificar a los respectivos deudores en función de su mora, según los criterios aplicables para la cartera de consumo o vivienda"
  },
  {
   "id": "Obligacion_comunicar_clasificacion_de_deudor",
   "type": "Obligacion",
   "label": "Comunicar clasificación de deudor",
   "tokens_matcheados": 2,
   "resumen_propiedades": "A solicitud de cada cliente, dentro de los 10 días corridos del pedido, la entidad financiera deberá comunicarle la última clasificación que le ha asignado, jun…"
  },
  {
   "id": "Operacion_clasificacion_de_riesgo_de_deudor",
   "type": "Operacion",
   "label": "Clasificación deudor nivel riesgo",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: clasificación de riesgo de deudor"
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

--- paso 2 · buscar_nodos · input={"consulta": "reevaluación inmediata deudor comercial", "limite": 10} · runtime=2724 chars · re-ejecutado=2724 chars ---

```json
{
 "consulta": "reevaluación inmediata deudor comercial",
 "total_con_match": 71,
 "resultados": [
  {
   "id": "EntidadFinanciera_deudor_cartera_comercial",
   "type": "EntidadFinanciera",
   "label": "Deudores cartera comercial",
   "tokens_matcheados": 2,
   "resumen_propiedades": "categoria: deudor cartera comercial"
  },
  {
   "id": "Obligacion_corresponde_reclasificacion_inmediata_del_deudor_en_nivel_determinado_por_sumato",
   "type": "Obligacion",
   "label": "Reclasificación inmediata por atrasos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Corresponde reclasificación inmediata del deudor en nivel determinado por sumatoria de días de atraso efectivamente registrados más atraso mínimo normativo"
  },
  {
   "id": "Obligacion_la_reevaluacion_debera_ser_inmediata_cuando_se_trate_de_clientes_cuyas_financiac",
   "type": "Obligacion",
   "label": "Reevaluación inmediata para clientes grandes",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La reevaluación deberá ser inmediata cuando se trate de clientes cuyas financiaciones comprendidas igualen o superen el 1% de la responsabilidad patrimonial com…"
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
   "id": "EntidadFinanciera_banco_comercial",
   "type": "EntidadFinanciera",
   "label": "Bancos comerciales",
   "tokens_matcheados": 1,
   "resumen_propiedades": "categoria: banco comercial"
  },
  {
   "id": "Operacion_evaluacion_de_deudor_como_sujeto_de_credito",
   "type": "Operacion",
   "label": "Evaluación de deudor",
   "tokens_matcheados": 1,
   "resumen_propiedades": "tipo: evaluación de deudor como sujeto de crédito"
  },
  {
   "id": "Operacion_financiacion_de_naturaleza_comercial",
   "type": "Operacion",
   "label": "Financiación comercial",
   "tokens_matcheados": 1,
   "resumen_propiedades": "tipo: financiación de naturaleza comercial"
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

--- paso 3 · ver_nodo · input={"id": "Obligacion_la_clasificacion_de_los_deudores_debera_efectuarse_con_una_periodicidad_que_atie"} · runtime=560 chars · re-ejecutado=560 chars ---

```json
{
 "id": "Obligacion_la_clasificacion_de_los_deudores_debera_efectuarse_con_una_periodicidad_que_atie",
 "type": "Obligacion",
 "label": "Efectuar clasificación periódicamente",
 "properties": {
  "descripcion": "La clasificación de los deudores deberá efectuarse con una periodicidad que atienda a su importancia, considerando la totalidad de las financiaciones comprendidas.",
  "tipo": "calculo",
  "plazo": "periódica según importancia"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Punto 3.2. Periodicidad de clasificación."
  }
 ]
}
```

--- paso 4 · ver_nodo · input={"id": "Obligacion_la_reevaluacion_debera_ser_inmediata_cuando_se_trate_de_clientes_cuyas_financiac"} · runtime=622 chars · re-ejecutado=622 chars ---

```json
{
 "id": "Obligacion_la_reevaluacion_debera_ser_inmediata_cuando_se_trate_de_clientes_cuyas_financiac",
 "type": "Obligacion",
 "label": "Reevaluación inmediata para clientes grandes",
 "properties": {
  "descripcion": "La reevaluación deberá ser inmediata cuando se trate de clientes cuyas financiaciones comprendidas igualen o superen el 1% de la responsabilidad patrimonial computable de la entidad o del activo del fideicomiso financiero",
  "tipo": "otra",
  "plazo": "inmediata"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Punto 6.4. Reconsideración obligatoria de la clasificación."
  }
 ]
}
```

--- paso 5 · buscar_nodos · input={"consulta": "5% RPC responsabilidad patrimonial computable", "limite": 10} · runtime=3297 chars · re-ejecutado=3297 chars ---

```json
{
 "consulta": "5% RPC responsabilidad patrimonial computable",
 "total_con_match": 70,
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
   "id": "Restriccion_umbral_de_2_5_rpc_para_aprobacion",
   "type": "Restriccion",
   "label": "Umbral de 2,5% RPC para aprobación",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Las financiaciones que excedan del 2,5 % de la RPC de la entidad financiera del mes anterior deberán contar con aprobación previa"
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
   "id": "Restriccion_clientes_cuyas_financiaciones_sean_equivalentes_al_5_o_mas_de_la_rpc_o_del_activ",
   "type": "Restriccion",
   "label": "Límite mínimo RPC clientes revisión trimestral",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Clientes cuyas financiaciones sean equivalentes al 5% o más de la RPC o del activo del fideicomiso financiero"
  },
  {
   "id": "Restriccion_el_importe_de_co_debera_ser_resultante_de_multiplicar_4_5_por_los_apr",
   "type": "Restriccion",
   "label": "Límite mínimo CO",
   "tokens_matcheados": 1,
   "resumen_propiedades": "El importe de CO deberá ser resultante de multiplicar 4,5% por los APR"
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

--- paso 6 · buscar_nodos · input={"consulta": "periodicidad trimestral semestral deudor comercial", "limite": 10} · runtime=2545 chars · re-ejecutado=2545 chars ---

```json
{
 "consulta": "periodicidad trimestral semestral deudor comercial",
 "total_con_match": 87,
 "resultados": [
  {
   "id": "EntidadFinanciera_deudor_cartera_comercial",
   "type": "EntidadFinanciera",
   "label": "Deudores cartera comercial",
   "tokens_matcheados": 2,
   "resumen_propiedades": "categoria: deudor cartera comercial"
  },
  {
   "id": "Obligacion_la_revision_debera_efectuarse_como_minimo_con_la_periodicidad_que_se_indica_segu",
   "type": "Obligacion",
   "label": "Revisión trimestral clientes mayor riesgo",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La revisión deberá efectuarse como mínimo con la periodicidad que se indica seguidamente, dejando constancia de ello en el legajo del cliente analizado"
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
   "id": "EntidadFinanciera_banco_comercial",
   "type": "EntidadFinanciera",
   "label": "Bancos comerciales",
   "tokens_matcheados": 1,
   "resumen_propiedades": "categoria: banco comercial"
  },
  {
   "id": "Operacion_evaluacion_de_deudor_como_sujeto_de_credito",
   "type": "Operacion",
   "label": "Evaluación de deudor",
   "tokens_matcheados": 1,
   "resumen_propiedades": "tipo: evaluación de deudor como sujeto de crédito"
  },
  {
   "id": "Operacion_financiacion_de_naturaleza_comercial",
   "type": "Operacion",
   "label": "Financiación comercial",
   "tokens_matcheados": 1,
   "resumen_propiedades": "tipo: financiación de naturaleza comercial"
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
  }
 ]
}
```

--- paso 7 · ver_nodo · input={"id": "Restriccion_clientes_cuyas_financiaciones_sean_equivalentes_al_5_o_mas_de_la_rpc_o_del_activ"} · runtime=512 chars · re-ejecutado=512 chars ---

```json
{
 "id": "Restriccion_clientes_cuyas_financiaciones_sean_equivalentes_al_5_o_mas_de_la_rpc_o_del_activ",
 "type": "Restriccion",
 "label": "Límite mínimo RPC clientes revisión trimestral",
 "properties": {
  "tipo": "limite_cuantitativo",
  "descripcion": "Clientes cuyas financiaciones sean equivalentes al 5% o más de la RPC o del activo del fideicomiso financiero",
  "umbral": "5%"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Punto 6.3. Periodicidad mínima de clasificación."
  }
 ]
}
```

--- paso 8 · ver_nodo · input={"id": "Obligacion_la_revision_debera_efectuarse_como_minimo_con_la_periodicidad_que_se_indica_segu"} · runtime=559 chars · re-ejecutado=559 chars ---

```json
{
 "id": "Obligacion_la_revision_debera_efectuarse_como_minimo_con_la_periodicidad_que_se_indica_segu",
 "type": "Obligacion",
 "label": "Revisión trimestral clientes mayor riesgo",
 "properties": {
  "tipo": "presentacion_informativa",
  "descripcion": "La revisión deberá efectuarse como mínimo con la periodicidad que se indica seguidamente, dejando constancia de ello en el legajo del cliente analizado",
  "plazo": "trimestral"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Punto 6.3. Periodicidad mínima de clasificación."
  }
 ]
}
```

--- paso 9 · ver_vecinos · input={"id": "Restriccion_clientes_cuyas_financiaciones_sean_equivalentes_al_5_o_mas_de_la_rpc_o_del_activ", "direccion": "ambas"} · runtime=1375 chars · re-ejecutado=1375 chars ---

```json
{
 "id": "Restriccion_clientes_cuyas_financiaciones_sean_equivalentes_al_5_o_mas_de_la_rpc_o_del_activ",
 "label": "Límite mínimo RPC clientes revisión trimestral",
 "n_salientes_total": 4,
 "n_entrantes_total": 0,
 "salientes": [
  {
   "relation": "establecida_en",
   "vecino_id": "TextoOrdenado_to_clasificacion_deudores_actual_pdf",
   "vecino_label": "Clasificación de Deudores",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "Punto 6.3. Periodicidad mínima de clasificación."
    }
   ]
  },
  {
   "relation": "aplica_a",
   "vecino_id": "EntidadFinanciera_sujeto_obligado",
   "vecino_label": "Sujetos obligados",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "Punto 6.3. Periodicidad mínima de clasificación."
    }
   ]
  },
  {
   "relation": "aplica_a",
   "vecino_id": "EntidadFinanciera_fideicomiso_financiero",
   "vecino_label": "Fideicomisos financieros",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "Punto 6.3. Periodicidad mínima de clasificación."
    }
   ]
  },
  {
   "relation": "limita",
   "vecino_id": "Operacion_revision_de_clasificacion_de_deudores",
   "vecino_label": "Revisión de clasificación trimestral",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "Punto 6.3. Periodicidad mínima de clasificación."
    }
   ]
  }
 ],
 "salientes_truncado": false,
 "entrantes": [],
 "entrantes_truncado": false
}
```

--- paso 10 · ver_vecinos · input={"id": "Obligacion_la_reevaluacion_debera_ser_inmediata_cuando_se_trate_de_clientes_cuyas_financiac", "direccion": "ambas"} · runtime=1124 chars · re-ejecutado=1124 chars ---

```json
{
 "id": "Obligacion_la_reevaluacion_debera_ser_inmediata_cuando_se_trate_de_clientes_cuyas_financiac",
 "label": "Reevaluación inmediata para clientes grandes",
 "n_salientes_total": 3,
 "n_entrantes_total": 0,
 "salientes": [
  {
   "relation": "establecida_en",
   "vecino_id": "TextoOrdenado_to_clasificacion_deudores_actual_pdf",
   "vecino_label": "Clasificación de Deudores",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "Punto 6.4. Reconsideración obligatoria de la clasificación."
    }
   ]
  },
  {
   "relation": "aplica_a",
   "vecino_id": "EntidadFinanciera_sujeto_obligado",
   "vecino_label": "Sujetos obligados",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "Punto 6.4. Reconsideración obligatoria de la clasificación."
    }
   ]
  },
  {
   "relation": "aplica_a",
   "vecino_id": "EntidadFinanciera_fideicomiso_financiero",
   "vecino_label": "Fideicomisos financieros",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "Punto 6.4. Reconsideración obligatoria de la clasificación."
    }
   ]
  }
 ],
 "salientes_truncado": false,
 "entrantes": [],
 "entrantes_truncado": false
}
```

--- paso 11 · buscar_nodos · input={"consulta": "reconsideración obligatoria clasificación casos inmediata", "limite": 10} · runtime=2719 chars · re-ejecutado=2719 chars ---

```json
{
 "consulta": "reconsideración obligatoria clasificación casos inmediata",
 "total_con_match": 82,
 "resultados": [
  {
   "id": "Operacion_reconsideracion_de_clasificacion",
   "type": "Operacion",
   "label": "Reconsideración de clasificación",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: reconsideración de clasificación"
  },
  {
   "id": "Obligacion_en_todos_los_casos_debera_documentarse_el_analisis_efectuado",
   "type": "Obligacion",
   "label": "Documentar análisis de clasificación",
   "tokens_matcheados": 2,
   "resumen_propiedades": "En todos los casos deberá documentarse el análisis efectuado."
  },
  {
   "id": "Operacion_clasificacion_de_cartera",
   "type": "Operacion",
   "label": "Agrupación de cartera",
   "tokens_matcheados": 1,
   "resumen_propiedades": "tipo: clasificación de cartera"
  },
  {
   "id": "Obligacion_en_el_resto_de_los_casos_las_entidades_deberan_usar_el_metodo_delta_plus_contemp",
   "type": "Obligacion",
   "label": "Usar método delta-plus",
   "tokens_matcheados": 1,
   "resumen_propiedades": "En el resto de los casos, las entidades deberán usar el método delta-plus contemplado en el punto 6.6.3"
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
   "id": "Restriccion_los_casos_que_no_encuadren_en_lo_expuesto_precedentemente_quedan_sujetos_a_la_co",
   "type": "Restriccion",
   "label": "Conformidad previa BCRA",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Los casos que no encuadren en lo expuesto precedentemente quedan sujetos a la conformidad previa del BCRA, debiendo los pedidos ser canalizados por una entidad …"
  },
  {
   "id": "Excepcion_con_excepcion_de_los_casos_contemplados_en_el_punto_4_1",
   "type": "Excepcion",
   "label": "Excepción casos punto 4.1",
   "tokens_matcheados": 1,
   "resumen_propiedades": "con excepción de los casos contemplados en el punto 4.1"
  },
  {
   "id": "Operacion_clasificacion_de_partidas_fuera_de_balance",
   "type": "Operacion",
   "label": "Partidas fuera de balance",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Partidas fuera de balance incluidos los compromisos por financiaciones y líneas de corresponsalía a entidades del exterior, las garantías otorgadas, los avales …"
  },
  {
   "id": "TextoOrdenado_to_clasificacion_deudores_actual_pdf",
   "type": "TextoOrdenado",
   "label": "Clasificación de Deudores",
   "tokens_matcheados": 1,
   "resumen_propiedades": "materia: clasificacion_deudores; archivo: TO_clasificacion_deudores_actual.pdf; version: vigente"
  }
 ]
}
```

--- paso 12 · buscar_nodos · input={"consulta": "reevaluación inmediata atraso incumplimiento cambio situación", "limite": 10} · runtime=2703 chars · re-ejecutado=2703 chars ---

```json
{
 "consulta": "reevaluación inmediata atraso incumplimiento cambio situación",
 "total_con_match": 114,
 "resultados": [
  {
   "id": "Restriccion_comprende_los_clientes_que_atienden_en_forma_puntual_el_pago_de_sus_obligaciones",
   "type": "Restriccion",
   "label": "Límite de atraso en situación normal",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Comprende los clientes que atienden en forma puntual el pago de sus obligaciones o con atrasos que no superan los 31 días"
  },
  {
   "id": "Obligacion_la_reevaluacion_debera_ser_inmediata_cuando_se_trate_de_clientes_cuyas_financiac",
   "type": "Obligacion",
   "label": "Reevaluación inmediata para clientes grandes",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La reevaluación deberá ser inmediata cuando se trate de clientes cuyas financiaciones comprendidas igualen o superen el 1% de la responsabilidad patrimonial com…"
  },
  {
   "id": "Restriccion_exposiciones_en_situacion_de_incumplimiento_con_garantia_hipotecaria_normativas_",
   "type": "Restriccion",
   "label": "Ponderador exposiciones incumplimiento hipotecario",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Exposiciones en situación de incumplimiento con garantía hipotecaria normativas sobre inmuebles residenciales: 100"
  },
  {
   "id": "EntidadFinanciera_casa_de_cambio",
   "type": "EntidadFinanciera",
   "label": "Casas de cambio",
   "tokens_matcheados": 1,
   "resumen_propiedades": "categoria: casa de cambio"
  },
  {
   "id": "Operacion_gestion_de_cobro_por_incumplimiento",
   "type": "Operacion",
   "label": "Gestión de cobro",
   "tokens_matcheados": 1,
   "resumen_propiedades": "Operaciones en gestión de cobro por incumplimiento del proveedor, imputadas en SEPAIMPO cuando se verifican condiciones específicas"
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
   "id": "Operacion_incumplimiento_de_condiciones_contractuales",
   "type": "Operacion",
   "label": "Incumplimiento de pago",
   "tokens_matcheados": 1,
   "resumen_propiedades": "tipo: incumplimiento de condiciones contractuales"
  }
 ]
}
```

--- paso 13 · buscar_nodos · input={"consulta": "punto 6.4 reconsideración obligatoria casos reevaluación", "limite": 10} · runtime=3412 chars · re-ejecutado=3412 chars ---

```json
{
 "consulta": "punto 6.4 reconsideración obligatoria casos reevaluación",
 "total_con_match": 82,
 "resultados": [
  {
   "id": "Excepcion_con_excepcion_de_los_casos_contemplados_en_el_punto_4_1",
   "type": "Excepcion",
   "label": "Excepción casos punto 4.1",
   "tokens_matcheados": 3,
   "resumen_propiedades": "con excepción de los casos contemplados en el punto 4.1"
  },
  {
   "id": "Restriccion_los_garantes_admisibles_se_limitan_a_los_estipulados_en_el_punto_5_4_1_los_spe_n",
   "type": "Restriccion",
   "label": "Restricción en garantes admisibles",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Los garantes admisibles se limitan a los estipulados en el punto 5.4.1. Los SPE no son garantes admisibles."
  },
  {
   "id": "Obligacion_ajustar_el_valor_de_la_cobertura_segun_lo_previsto_en_punto_5_4_5",
   "type": "Obligacion",
   "label": "Ajuste valor cobertura método integral",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Para la aplicación del método integral el valor de la cobertura deberá ajustarse conforme a lo establecido en el punto 5.4.5"
  },
  {
   "id": "Restriccion_las_operaciones_no_comprendidas_en_el_punto_10_6_6",
   "type": "Restriccion",
   "label": "Exclusión de operaciones del punto 10.6.6",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Las operaciones no comprendidas en el punto 10.6.6."
  },
  {
   "id": "Obligacion_el_registro_de_reintegros_de_importes_rri_previsto_en_el_punto_3_1_4",
   "type": "Obligacion",
   "label": "Disponibilizar Registro Reintegros Importes",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El Registro de Reintegros de Importes (RRI) previsto en el punto 3.1.4."
  },
  {
   "id": "Excepcion_en_el_caso_de_operaciones_comprendidas_en_el_punto_7_11_1_6_se_admitira_la_cance",
   "type": "Excepcion",
   "label": "Cancelación de intereses por cobros posteriores",
   "tokens_matcheados": 2,
   "resumen_propiedades": "En el caso de operaciones comprendidas en el punto 7.11.1.6, se admitirá la cancelación de intereses mediante la aplicación de cobros de exportaciones de bienes…"
  },
  {
   "id": "Excepcion_el_pago_se_concreta_en_el_marco_de_lo_dispuesto_en_el_punto_4_8_4_por_un_cliente",
   "type": "Excepcion",
   "label": "Pago BOPREAL Serie 1 mínimo 50% deudas elegibles",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El pago se concreta en el marco de lo dispuesto en el punto 4.8.4. por un cliente que suscribió BOPREAL Serie 1 por un monto igual o mayor al 50% (cincuenta por…"
  },
  {
   "id": "Excepcion_el_pago_se_concreta_en_el_marco_de_lo_dispuesto_en_el_punto_4_8_5_por_un_cliente",
   "type": "Excepcion",
   "label": "Pago BOPREAL Serie 1 mínimo 25% deudas elegibles",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El pago se concreta en el marco de lo dispuesto en el punto 4.8.5. por un cliente que suscribió BOPREAL Serie 1 por un monto igual o mayor al 25% (veinticinco p…"
  },
  {
   "id": "Obligacion_aplicar_disposiciones_de_punto_8_3_4_a_deuda_computable_como_ca_o_pnc",
   "type": "Obligacion",
   "label": "Aplicar disposiciones de punto 8.3.4 a deuda computable como CA o PNc",
   "tokens_matcheados": 2,
   "resumen_propiedades": "En el caso de los instrumentos de deuda computables como CA o PNc, al admitir los aportes, se deberá tener en cuenta lo dispuesto en el punto 8.3.4"
  },
  {
   "id": "Restriccion_el_importe_de_co_debera_ser_resultante_de_multiplicar_4_5_por_los_apr",
   "type": "Restriccion",
   "label": "Límite mínimo CO",
   "tokens_matcheados": 1,
   "resumen_propiedades": "El importe de CO deberá ser resultante de multiplicar 4,5% por los APR"
  }
 ]
}
```

--- paso 14 · buscar_nodos · input={"consulta": "reevaluación inmediata mora atraso 60 días incumplimiento", "limite": 10} · runtime=3699 chars · re-ejecutado=3699 chars ---

```json
{
 "consulta": "reevaluación inmediata mora atraso 60 días incumplimiento",
 "total_con_match": 99,
 "resultados": [
  {
   "id": "Obligacion_ingreso_y_liquidacion_en_mercado_de_cambios_en_60_dias_corridos_para_operaciones",
   "type": "Obligacion",
   "label": "Ingreso en plazo 60 días",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Ingreso y liquidación en mercado de cambios en 60 días corridos para operaciones con contrapartes vinculadas y exportaciones de capítulos 26 y 71 según especifi…"
  },
  {
   "id": "Restriccion_se_concreta_dentro_de_los_60_sesenta_dias_corridos_previos_a_la_fecha_de_vencimi",
   "type": "Restriccion",
   "label": "Límite acceso 60 días previos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Se concreta dentro de los 60 (sesenta) días corridos previos a la fecha de vencimiento por un monto diario que no supere el 10% (diez por ciento) del monto que …"
  },
  {
   "id": "Restriccion_incurra_en_atrasos_recurrentes_incumplimiento_de_hasta_180_dias_respecto_de_cond",
   "type": "Restriccion",
   "label": "Atrasos recurrentes incumplimiento",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Incurra en atrasos recurrentes, incumplimiento de hasta 180 días respecto de condiciones contractuales o nulo movimiento en las cuentas."
  },
  {
   "id": "Restriccion_el_cliente_se_encuentre_permanentemente_atrasado_en_el_pago_con_incumplimientos_",
   "type": "Restriccion",
   "label": "Atraso permanente superior a 180 días",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El cliente se encuentre permanentemente atrasado en el pago, con incumplimientos superiores a 180 días respecto de las condiciones contractuales."
  },
  {
   "id": "Obligacion_en_caso_de_verificarse_atrasos_mayores_a_31_dias_en_el_pago_de_los_servicios_de_",
   "type": "Obligacion",
   "label": "Reclasificación tras atraso mayor a 31 días",
   "tokens_matcheados": 2,
   "resumen_propiedades": "En caso de verificarse atrasos mayores a 31 días en el pago de los servicios de la deuda refinanciada contados a partir de la inclusión del deudor en esta categ…"
  },
  {
   "id": "Obligacion_la_reevaluacion_debera_ser_inmediata_cuando_se_trate_de_clientes_cuyas_financiac",
   "type": "Obligacion",
   "label": "Reevaluación inmediata para clientes grandes",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La reevaluación deberá ser inmediata cuando se trate de clientes cuyas financiaciones comprendidas igualen o superen el 1% de la responsabilidad patrimonial com…"
  },
  {
   "id": "Obligacion_a_los_fines_de_establecer_los_dias_de_atraso_en_el_caso_de_las_financiaciones_in",
   "type": "Obligacion",
   "label": "Imputación de pago mínimo en tarjeta de crédito",
   "tokens_matcheados": 2,
   "resumen_propiedades": "A los fines de establecer los días de atraso, en el caso de las financiaciones instrumentadas mediante tarjetas de crédito, se considerarán los que resulten lue…"
  },
  {
   "id": "Obligacion_a_los_fines_de_la_clasificacion_debera_tenerse_en_cuenta_la_mora_en_el_atraso_de",
   "type": "Obligacion",
   "label": "Considerar mora al vencimiento emergencia agropecuaria",
   "tokens_matcheados": 2,
   "resumen_propiedades": "A los fines de la clasificación, deberá tenerse en cuenta la mora en el atraso de sus obligaciones para el momento en que concluya la vigencia de la emergencia …"
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
  }
 ]
}
```

--- paso 15 · buscar_nodos · input={"consulta": "cambio situación financiera deterioro información negativa reevaluación", "limite": 10} · runtime=3494 chars · re-ejecutado=3494 chars ---

```json
{
 "consulta": "cambio situación financiera deterioro información negativa reevaluación",
 "total_con_match": 205,
 "resultados": [
  {
   "id": "Restriccion_el_cliente_presente_una_situacion_financiera_mala_con_suspension_de_pagos_quiebr",
   "type": "Restriccion",
   "label": "Situación financiera mala",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El cliente presente una situación financiera mala con suspensión de pagos, quiebra decretada o pedido de su propia quiebra."
  },
  {
   "id": "Restriccion_el_cliente_debe_presentar_una_situacion_financiera_iliquida_y_muy_alto_nivel_de_",
   "type": "Restriccion",
   "label": "Situación financiera ilíquida",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El cliente debe presentar una situación financiera ilíquida y muy alto nivel de endeudamiento, con resultados negativos en la explotación y obligación de vender…"
  },
  {
   "id": "Restriccion_presente_una_situacion_financiera_iliquida_y_un_nivel_de_flujo_de_fondos_que_no_",
   "type": "Restriccion",
   "label": "Situación financiera ilíquida",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Presente una situación financiera ilíquida y un nivel de flujo de fondos que no le permita atender el pago de la totalidad del capital y de los intereses de las…"
  },
  {
   "id": "Restriccion_el_fondo_debera_proveer_informacion_financiera_con_una_frecuencia_minima_trimest",
   "type": "Restriccion",
   "label": "Frecuencia mínima de información",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El fondo deberá proveer información financiera con una frecuencia mínima trimestral y el grado de detalle suficiente para el cálculo de ponderadores de riesgo"
  },
  {
   "id": "Obligacion_proporcionar_informacion_financiera",
   "type": "Obligacion",
   "label": "Proporcionar información financiera",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Los clientes deberán proporcionar información financiera actualizada (estados financieros o contables e información complementaria, proyectos de inversión, etc.…"
  },
  {
   "id": "Obligacion_para_clasificacion_en_situacion_normal_el_analisis_del_flujo_de_fondos_del_clien",
   "type": "Obligacion",
   "label": "Evaluación situación financiera normal",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Para clasificación en situación normal: El análisis del flujo de fondos del cliente demuestra que es capaz de atender adecuadamente todos sus compromisos financ…"
  },
  {
   "id": "Restriccion_cuando_el_emisor_de_la_tarjeta_sea_una_entidad_financiera_el_titular_podra_cance",
   "type": "Restriccion",
   "label": "Tipo de cambio máximo cancelación consumos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Cuando el emisor de la tarjeta sea una entidad financiera, el titular podrá cancelar los consumos realizados en moneda extranjera en esta última moneda o en pes…"
  },
  {
   "id": "Excepcion_modificacion_en_forma_negativa_de_la_clasificacion_del_cliente_en_la_central_de_",
   "type": "Excepcion",
   "label": "Excepción por cambio negativo en Central de deudores",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Modificación en forma negativa de la clasificación del cliente en la Central de deudores del sistema financiero, llevándola a un grado inferior al de la entidad…"
  },
  {
   "id": "EntidadFinanciera_casa_de_cambio",
   "type": "EntidadFinanciera",
   "label": "Casas de cambio",
   "tokens_matcheados": 1,
   "resumen_propiedades": "categoria: casa de cambio"
  },
  {
   "id": "EntidadFinanciera_agencia_de_cambio",
   "type": "EntidadFinanciera",
   "label": "Agencias de cambio",
   "tokens_matcheados": 1,
   "resumen_propiedades": "categoria: agencia de cambio"
  }
 ]
}
```

---

# Apéndice CQ-033 — outputs completos (7 pasos re-ejecutables)


--- paso 1 · buscar_nodos · input={"consulta": "capital riesgo operacional Grupo 2", "limite": 10} · runtime=3239 chars · re-ejecutado=3239 chars ---

```json
{
 "consulta": "capital riesgo operacional Grupo 2",
 "total_con_match": 402,
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

--- paso 2 · buscar_nodos · input={"consulta": "límite exigencia capital operacional", "limite": 10} · runtime=3695 chars · re-ejecutado=3695 chars ---

```json
{
 "consulta": "límite exigencia capital operacional",
 "total_con_match": 407,
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
   "id": "Obligacion_se_determinara_mensualmente_aplicando_la_siguiente_expresion_c_ro_max_ib_t_12_50",
   "type": "Obligacion",
   "label": "Determinar mensualmente exigencia capital operacional",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Se determinará mensualmente aplicando la siguiente expresión: C_RO = máx(IB_t/12.500, K_0) donde C_RO es exigencia de capital por riesgo operacional, con paráme…"
  }
 ]
}
```

--- paso 3 · ver_nodo · input={"id": "Restriccion_la_exigencia_de_capital_por_riesgo_operacional_para_entidades_del_grupo_b_determ"} · runtime=673 chars · re-ejecutado=673 chars ---

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

--- paso 4 · ver_vecinos · input={"id": "Restriccion_la_exigencia_de_capital_por_riesgo_operacional_para_entidades_del_grupo_b_determ", "direccion": "ambas"} · runtime=1936 chars · re-ejecutado=1936 chars ---

```json
{
 "id": "Restriccion_la_exigencia_de_capital_por_riesgo_operacional_para_entidades_del_grupo_b_determ",
 "label": "Límite exigencia capital operacional grupo B",
 "n_salientes_total": 3,
 "n_entrantes_total": 2,
 "salientes": [
  {
   "relation": "establecida_en",
   "vecino_id": "TextoOrdenado_to_capitales_minimos_actual_pdf",
   "vecino_label": "Capitales Mínimos",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 12.3. Para aquellas entidades financieras que sean reclasificadas desde el 01/01/2026"
    }
   ]
  },
  {
   "relation": "aplica_a",
   "vecino_id": "EntidadFinanciera_entidad_del_grupo_b",
   "vecino_label": "Entidades del grupo B",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 12.3. Para aquellas entidades financieras que sean reclasificadas desde el 01/01/2026"
    }
   ]
  },
  {
   "relation": "limita",
   "vecino_id": "Operacion_calculo",
   "vecino_label": "Cálculo exigencia capital riesgo operacional",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 12.3. Para aquellas entidades financieras que sean reclasificadas desde el 01/01/2026"
    }
   ]
  }
 ],
 "salientes_truncado": false,
 "entrantes": [
  {
   "relation": "exceptua",
   "vecino_id": "Excepcion_los_limites_maximos_se_reduciran_a_11_y_8_respectivamente_cuando_la_entidad_fina",
   "vecino_label": "Reducción límite con calificación SEFYC 1-3",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 12.3. Para aquellas entidades financieras que sean reclasificadas desde el 01/01/2026"
    }
   ]
  },
  {
   "relation": "exceptua",
   "vecino_id": "Excepcion_en_los_casos_en_que_la_entidad_financiera_cuente_en_todos_los_citados_aspectos_c",
   "vecino_label": "Reducción límite con calificación SEFYC 1-2",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 12.3. Para aquellas entidades financieras que sean reclasificadas desde el 01/01/2026"
    }
   ]
  }
 ],
 "entrantes_truncado": false
}
```

--- paso 5 · ver_nodo · input={"id": "Excepcion_los_limites_maximos_se_reduciran_a_11_y_8_respectivamente_cuando_la_entidad_fina"} · runtime=557 chars · re-ejecutado=557 chars ---

```json
{
 "id": "Excepcion_los_limites_maximos_se_reduciran_a_11_y_8_respectivamente_cuando_la_entidad_fina",
 "type": "Excepcion",
 "label": "Reducción límite con calificación SEFYC 1-3",
 "properties": {
  "descripcion": "Los límites máximos se reducirán a 11% y 8%, respectivamente, cuando la entidad financiera cuente con calificación 1, 2 o 3 conforme a la valoración otorgada por la SEFYC"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Punto 12.3. Para aquellas entidades financieras que sean reclasificadas desde el 01/01/2026"
  }
 ]
}
```

--- paso 6 · ver_nodo · input={"id": "Excepcion_en_los_casos_en_que_la_entidad_financiera_cuente_en_todos_los_citados_aspectos_c"} · runtime=560 chars · re-ejecutado=560 chars ---

```json
{
 "id": "Excepcion_en_los_casos_en_que_la_entidad_financiera_cuente_en_todos_los_citados_aspectos_c",
 "type": "Excepcion",
 "label": "Reducción límite con calificación SEFYC 1-2",
 "properties": {
  "descripcion": "En los casos en que la entidad financiera cuente en todos los citados aspectos con calificación 1 o 2, el límite máximo disminuirá a 7% o 5%, según pertenezca al grupo B o C"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Punto 12.3. Para aquellas entidades financieras que sean reclasificadas desde el 01/01/2026"
  }
 ]
}
```

--- paso 7 · ver_vecinos · input={"id": "Excepcion_en_los_casos_en_que_la_entidad_financiera_cuente_en_todos_los_citados_aspectos_c", "direccion": "ambas"} · runtime=1669 chars · re-ejecutado=1669 chars ---

```json
{
 "id": "Excepcion_en_los_casos_en_que_la_entidad_financiera_cuente_en_todos_los_citados_aspectos_c",
 "label": "Reducción límite con calificación SEFYC 1-2",
 "n_salientes_total": 4,
 "n_entrantes_total": 0,
 "salientes": [
  {
   "relation": "establecida_en",
   "vecino_id": "TextoOrdenado_to_capitales_minimos_actual_pdf",
   "vecino_label": "Capitales Mínimos",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 12.3. Para aquellas entidades financieras que sean reclasificadas desde el 01/01/2026"
    }
   ]
  },
  {
   "relation": "exceptua",
   "vecino_id": "Restriccion_la_exigencia_de_capital_por_riesgo_operacional_para_entidades_del_grupo_b_determ",
   "vecino_label": "Límite exigencia capital operacional grupo B",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 12.3. Para aquellas entidades financieras que sean reclasificadas desde el 01/01/2026"
    }
   ]
  },
  {
   "relation": "exceptua",
   "vecino_id": "Restriccion_la_exigencia_de_capital_por_riesgo_operacional_para_entidades_del_grupo_c_determ",
   "vecino_label": "Límite exigencia capital operacional grupo C",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 12.3. Para aquellas entidades financieras que sean reclasificadas desde el 01/01/2026"
    }
   ]
  },
  {
   "relation": "exceptua",
   "vecino_id": "Restriccion_el_17_en_el_caso_de_entidades_del_grupo_b_del_promedio_de_los_ultimos_36_meses_a",
   "vecino_label": "Límite 17% grupo B capital mínimo",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 7.3. Límite para las entidades del grupo 2."
    }
   ]
  }
 ],
 "salientes_truncado": false,
 "entrantes": [],
 "entrantes_truncado": false
}
```
