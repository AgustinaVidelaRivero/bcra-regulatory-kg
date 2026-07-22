# Barrido de verificación sobre kg.json de run_3 — condicionales del gate CQN2

SOLO LECTURA; única escritura: este informe. Sellado por inexistencia VIGENTE (ni
verificador, ni capas, ni S1). Mecánica idéntica al barrido del gate anterior:
existencia por búsqueda por campo (campo indicado por hit, dumps completos), ranking
con `buscar_nodos` REAL (posición con el límite verbatim de la traza + posición global;
NOTA: el harness capea `limite` a 50 — harness.py línea 159 — así que "global N de 50"
es la posición dentro del top-50 real del instrumento, y "global —" significa fuera de
ese top-50), consultas VERBATIM de `posthoc_run/traces/gate_cqn2/run_3/`.


## K-A (CQN2-005) — ARCA / pendientes de uso / originalmente nominada

**[búsqueda 'ARCA (palabra)']** → 7 hit(s)

--- `Operacion_importacion_de_bienes` — matchea en: ['properties.description'] ---

```json
{
 "id": "Operacion_importacion_de_bienes",
 "type": "Operacion",
 "label": "Importación de bienes",
 "properties": {
  "tipo": "importación de bienes",
  "description": "Operación de ingreso aduanero de bienes importados que cuenta con el correspondiente registro ante ARCA"
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 10.2. Definiciones. (parte 1)"
  }
 ]
}
```

--- `Restriccion_la_entidad_debera_contar_con_la_conformidad_previa_del_bcra_en_el_caso_de_que_el` — matchea en: ['label', 'properties.descripcion'] ---

```json
{
 "id": "Restriccion_la_entidad_debera_contar_con_la_conformidad_previa_del_bcra_en_el_caso_de_que_el",
 "type": "Restriccion",
 "label": "Conformidad BCRA para clientes ARCA",
 "properties": {
  "descripcion": "La entidad deberá contar con la conformidad previa del BCRA en el caso de que el cliente sea una persona humana o jurídica incluida por la Agencia de Recaudación y Control Aduanero (ARCA) en la base de facturas o documentos equivalentes calificados como apócrifos",
  "tipo": "prohibicion"
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 3.16. Requisitos complementarios para los egresos por el mercado de cambios. (parte 1)"
  }
 ]
}
```

--- `Operacion_nominacion_de_entidad_para_seguimiento_de_exportacion` — matchea en: ['properties.description'] ---

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

--- `Obligacion_acceso_a_informacion_de_arca` — matchea en: ['label', 'properties.description'] ---

```json
{
 "id": "Obligacion_acceso_a_informacion_de_arca",
 "type": "Obligacion",
 "label": "Acceso a información de ARCA",
 "properties": {
  "tipo": "otra",
  "description": "A través del sistema SECOEXPO, las entidades tendrán acceso a la información disponible en ARCA que resulte pertinente a los efectos de cumplimentar sus responsabilidades como entidad nominada para el seguimiento de un permiso de embarque."
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 8.3. Información de las destinaciones de exportación a disposición de las entidades."
  }
 ]
}
```

--- `Obligacion_considerar_rectificacion_de_informacion` — matchea en: ['properties.description'] ---

```json
{
 "id": "Obligacion_considerar_rectificacion_de_informacion",
 "type": "Obligacion",
 "label": "Considerar rectificación de información",
 "properties": {
  "tipo": "otra",
  "description": "La entidad podrá considerar rectificada la información cuando ella se refleje en el SECOEXPO o cuando la entidad disponga de documentación emitida por la ARCA en la cual se indique expresamente que dicho organismo considera válidos los datos indicados por el exportador en su pedido de rectificación."
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 8.3. Información de las destinaciones de exportación a disposición de las entidades."
  }
 ]
}
```

--- `Operacion_rectificacion_de_datos` — matchea en: ['properties.description'] ---

```json
{
 "id": "Operacion_rectificacion_de_datos",
 "type": "Operacion",
 "label": "Rectificación de permiso de embarque",
 "properties": {
  "tipo": "rectificación de datos",
  "description": "Si el exportador considera que existen errores en la forma en que un permiso de embarque ha sido reportado en el sistema SECOEXPO, deberá tramitar la correspondiente rectificación directamente ante la ARCA."
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 8.3. Información de las destinaciones de exportación a disposición de las entidades."
  }
 ]
}
```

--- `Obligacion_oficializacion_exportacion_ventaja_exponotitoneroso` — matchea en: ['properties.description'] ---

```json
{
 "id": "Obligacion_oficializacion_exportacion_ventaja_exponotitoneroso",
 "type": "Obligacion",
 "label": "Oficialización exportación ventaja EXPONOTITONEROSO",
 "properties": {
  "tipo": "otra",
  "description": "En el permiso de embarque conste que la exportación de los bienes involucrados se oficializó bajo la ventaja aduanera EXPONOTITONEROSO, o acreditación de solicitud de rectificación ante ARCA."
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 8.5. Otras imputaciones admitidas en el cumplimiento del seguimiento. (parte 1)"
  }
 ]
}
```

**[búsqueda 'pendientes de uso']** → 1 hit(s)

--- `Restriccion_prohibicion_de_cambio_sin_certificaciones_pendientes` — matchea en: ['properties.description'] ---

```json
{
 "id": "Restriccion_prohibicion_de_cambio_sin_certificaciones_pendientes",
 "type": "Restriccion",
 "label": "Prohibición de cambio sin certificaciones pendientes",
 "properties": {
  "tipo": "prohibicion",
  "description": "El importador podrá posteriormente modificar la entidad nominada en la medida que, a la fecha de la solicitud de cambio de entidad, no existan certificaciones emitidas de acceso al mercado de cambios que estén pendientes de uso."
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 11.1. Seguimiento de oficializaciones de importación. (parte 1)"
  }
 ]
}
```

**[búsqueda 'originalmente nominada']** → 0 hit(s)

**VEREDICTO K-A:** 8 portador(es): ['Obligacion_acceso_a_informacion_de_arca', 'Obligacion_considerar_rectificacion_de_informacion', 'Obligacion_oficializacion_exportacion_ventaja_exponotitoneroso', 'Operacion_importacion_de_bienes', 'Operacion_nominacion_de_entidad_para_seguimiento_de_exportacion', 'Operacion_rectificacion_de_datos', 'Restriccion_la_entidad_debera_contar_con_la_conformidad_previa_del_bcra_en_el_caso_de_que_el', 'Restriccion_prohibicion_de_cambio_sin_certificaciones_pendientes']

D1/ranking (pasos 1, 2, 6, 9, 12 de CQN2-005):
- **paso 1** — `SEPAIMPO seguimiento pagos importaciones` · límite 10:
    - Obligacion_acceso_a_informacion_de_arca: NO en top-10 · global — de 50
    - Obligacion_considerar_rectificacion_de_informacion: NO en top-10 · global — de 50
    - Obligacion_oficializacion_exportacion_ventaja_exponotitoneroso: NO en top-10 · global — de 50
    - Operacion_importacion_de_bienes: NO en top-10 · global — de 50
    - Operacion_nominacion_de_entidad_para_seguimiento_de_exportacion: NO en top-10 · global — de 50
    - Operacion_rectificacion_de_datos: NO en top-10 · global — de 50
    - Restriccion_la_entidad_debera_contar_con_la_conformidad_previa_del_bcra_en_el_caso_de_que_el: NO en top-10 · global — de 50
    - Restriccion_prohibicion_de_cambio_sin_certificaciones_pendientes: NO en top-10 · global — de 50
- **paso 2** — `SEPAIMPO nominación entidad responsable oficialización` · límite 10:
    - Obligacion_acceso_a_informacion_de_arca: NO en top-10 · global — de 50
    - Obligacion_considerar_rectificacion_de_informacion: NO en top-10 · global — de 50
    - Obligacion_oficializacion_exportacion_ventaja_exponotitoneroso: NO en top-10 · global — de 50
    - Operacion_importacion_de_bienes: NO en top-10 · global — de 50
    - Operacion_nominacion_de_entidad_para_seguimiento_de_exportacion: posición 3 de 10 · global 3 de 50
    - Operacion_rectificacion_de_datos: NO en top-10 · global — de 50
    - Restriccion_la_entidad_debera_contar_con_la_conformidad_previa_del_bcra_en_el_caso_de_que_el: NO en top-10 · global — de 50
    - Restriccion_prohibicion_de_cambio_sin_certificaciones_pendientes: NO en top-10 · global — de 50
- **paso 6** — `cambio entidad nominada SEPAIMPO importación` · límite 10:
    - Obligacion_acceso_a_informacion_de_arca: NO en top-10 · global — de 50
    - Obligacion_considerar_rectificacion_de_informacion: NO en top-10 · global — de 50
    - Obligacion_oficializacion_exportacion_ventaja_exponotitoneroso: NO en top-10 · global — de 50
    - Operacion_importacion_de_bienes: NO en top-10 · global — de 50
    - Operacion_nominacion_de_entidad_para_seguimiento_de_exportacion: NO en top-10 · global — de 50
    - Operacion_rectificacion_de_datos: NO en top-10 · global — de 50
    - Restriccion_la_entidad_debera_contar_con_la_conformidad_previa_del_bcra_en_el_caso_de_que_el: NO en top-10 · global — de 50
    - Restriccion_prohibicion_de_cambio_sin_certificaciones_pendientes: NO en top-10 · global — de 50
- **paso 9** — `importador cambio entidad nominada oficialización importación condición` · límite 10:
    - Obligacion_acceso_a_informacion_de_arca: NO en top-10 · global — de 50
    - Obligacion_considerar_rectificacion_de_informacion: NO en top-10 · global — de 50
    - Obligacion_oficializacion_exportacion_ventaja_exponotitoneroso: NO en top-10 · global — de 50
    - Operacion_importacion_de_bienes: NO en top-10 · global — de 50
    - Operacion_nominacion_de_entidad_para_seguimiento_de_exportacion: NO en top-10 · global — de 50
    - Operacion_rectificacion_de_datos: NO en top-10 · global — de 50
    - Restriccion_la_entidad_debera_contar_con_la_conformidad_previa_del_bcra_en_el_caso_de_que_el: NO en top-10 · global — de 50
    - Restriccion_prohibicion_de_cambio_sin_certificaciones_pendientes: NO en top-10 · global — de 50
- **paso 12** — `importador nomina entidad seguimiento oficialización importación cambio` · límite 15:
    - Obligacion_acceso_a_informacion_de_arca: NO en top-15 · global — de 50
    - Obligacion_considerar_rectificacion_de_informacion: NO en top-15 · global — de 50
    - Obligacion_oficializacion_exportacion_ventaja_exponotitoneroso: NO en top-15 · global — de 50
    - Operacion_importacion_de_bienes: NO en top-15 · global — de 50
    - Operacion_nominacion_de_entidad_para_seguimiento_de_exportacion: NO en top-15 · global 23 de 50
    - Operacion_rectificacion_de_datos: NO en top-15 · global — de 50
    - Restriccion_la_entidad_debera_contar_con_la_conformidad_previa_del_bcra_en_el_caso_de_que_el: NO en top-15 · global — de 50
    - Restriccion_prohibicion_de_cambio_sin_certificaciones_pendientes: NO en top-15 · global — de 50


## K-B (CQN2-006) — 'igual a 1' / 'multiplicador de perdida interna' / ILM

**[búsqueda 'igual a 1']** → 0 hit(s)

**[búsqueda 'multiplicador de pérdida interna']** → 0 hit(s)

**[búsqueda 'ILM (palabra)']** → 1 hit(s)

--- `Obligacion_se_determinara_mensualmente_la_exigencia_de_capital_por_riesgo_operacional_cro_m` — matchea en: ['properties.descripcion'] ---

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

**VEREDICTO K-B:** 1 portador(es): ['Obligacion_se_determinara_mensualmente_la_exigencia_de_capital_por_riesgo_operacional_cro_m']

D1/ranking (pasos 3, 5, 6 de CQN2-006):
- **paso 3** — `multiplicador pérdida interna` · límite 10:
    - Obligacion_se_determinara_mensualmente_la_exigencia_de_capital_por_riesgo_operacional_cro_m: NO en top-10 · global — de 15
- **paso 5** — `ILM multiplicador pérdida` · límite 10:
    - Obligacion_se_determinara_mensualmente_la_exigencia_de_capital_por_riesgo_operacional_cro_m: NO en top-10 · global — de 8
- **paso 6** — `BIC ILM CRO` · límite 10:
    - Obligacion_se_determinara_mensualmente_la_exigencia_de_capital_por_riesgo_operacional_cro_m: posición 3 de 6 · global 3 de 6


## K-C (CQN2-010) — fiduciario con provenance de Protección; cedidos / notificados / transferencia

**[fiduciario ∧ provenance Protección/1.1.2.3]** → 0 hit(s)

**[búsqueda 'cedidos']** → 7 hit(s)

--- `Restriccion_restriccion_de_uso_de_calificacion_de_emisor_a_creditos_quirografarios` — matchea en: ['properties.description'] ---

```json
{
 "id": "Restriccion_restriccion_de_uso_de_calificacion_de_emisor_a_creditos_quirografarios",
 "type": "Restriccion",
 "label": "Restricción de uso de calificación de emisor a créditos quirografarios",
 "properties": {
  "tipo": "limite_cualitativo",
  "description": "Cuando el prestatario haya sido evaluado como emisor, esa calificación se podrá aplicar a los créditos quirografarios no subordinados que le hayan sido concedidos y no hayan sido evaluados. Las otras exposiciones crediticias no calificadas del emisor serán tratadas como no calificadas."
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Punto 10.3. Consideraciones para su implementación."
  }
 ]
}
```

--- `Restriccion_en_caso_de_no_efectuarse_la_evaluacion_de_creditos_cedidos_sin_responsabilidad_c` — matchea en: ['id', 'properties.descripcion'] ---

```json
{
 "id": "Restriccion_en_caso_de_no_efectuarse_la_evaluacion_de_creditos_cedidos_sin_responsabilidad_c",
 "type": "Restriccion",
 "label": "Clasificación irrecuperable sin evaluación",
 "properties": {
  "descripcion": "En caso de no efectuarse la evaluación de créditos cedidos sin responsabilidad, cualquiera sea el motivo, estos clientes se clasificarán en categoría irrecuperable",
  "tipo": "prohibicion"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Punto 1.2. Criterios especiales de imputación."
  }
 ]
}
```

--- `Obligacion_los_creditos_cedidos_a_favor_de_la_entidad_sin_responsabilidad_se_imputaran_al_f` — matchea en: ['id', 'properties.descripcion'] ---

```json
{
 "id": "Obligacion_los_creditos_cedidos_a_favor_de_la_entidad_sin_responsabilidad_se_imputaran_al_f",
 "type": "Obligacion",
 "label": "Imputación al firmante o pagador",
 "properties": {
  "descripcion": "Los créditos cedidos a favor de la entidad sin responsabilidad se imputarán al firmante, librador, deudor, codeudor o aceptante de los respectivos instrumentos",
  "tipo": "asignacion"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Punto 1.2. Criterios especiales de imputación."
  }
 ]
}
```

--- `Obligacion_proporcionar_informacion_a_sefyc` — matchea en: ['properties.description'] ---

```json
{
 "id": "Obligacion_proporcionar_informacion_a_sefyc",
 "type": "Obligacion",
 "label": "Proporcionar información a SEFyC",
 "properties": {
  "tipo": "presentacion_informativa",
  "description": "Deberán proporcionar a la SEFyC toda la información que ésta les requiera, para calcular las previsiones que deberán computar las entidades financieras –sean o no las originantes de los créditos cedidos– sobre sus tenencias de certificados de participación y/o títulos de deuda de los respectivos fideicomisos.",
  "plazo": "según requerimiento"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Punto 10.2. Fiduciarios de fideicomisos financieros comprendidos en la Ley de Entidades Fina"
  }
 ]
}
```

--- `Obligacion_abrir_legajo_de_firmante_librador_deudor` — matchea en: ['properties.description'] ---

```json
{
 "id": "Obligacion_abrir_legajo_de_firmante_librador_deudor",
 "type": "Obligacion",
 "label": "Abrir legajo de firmante/librador/deudor",
 "properties": {
  "tipo": "otra",
  "description": "En los casos de créditos cedidos a favor de la entidad sin responsabilidad para el cedente, deberá abrirse el legajo del firmante, librador, deudor, codeudor o aceptante de los respectivos instrumentos"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Punto 3.4. Legajo del cliente. (parte 1)"
  }
 ]
}
```

--- `Excepcion_excepcion_apertura_legajo_deudores_de_servicios_publicos` — matchea en: ['properties.description'] ---

```json
{
 "id": "Excepcion_excepcion_apertura_legajo_deudores_de_servicios_publicos",
 "type": "Excepcion",
 "label": "Excepción apertura legajo deudores de servicios públicos",
 "properties": {
  "description": "No será obligatoria la apertura del legajo en los casos de deudores por servicios públicos o por tarjetas de crédito considerados a los fines de la clasificación por haber sido cedidos los respectivos créditos por deudores en concurso preventivo"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Punto 3.4. Legajo del cliente. (parte 1)"
  }
 ]
}
```

--- `Excepcion_beneficios_cedidos_a_proveedores_directos_con_convalidacion_de_la_secretaria_de_` — matchea en: ['id', 'properties.descripcion'] ---

```json
{
 "id": "Excepcion_beneficios_cedidos_a_proveedores_directos_con_convalidacion_de_la_secretaria_de_",
 "type": "Excepcion",
 "label": "Excepción por cesión con convalidación",
 "properties": {
  "descripcion": "Beneficios cedidos a proveedores directos con convalidación de la Secretaría de Energía no se descuentan del monto disponible"
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 3.17. Acceso con “Certificación por los regímenes de acceso a divisas para la producci"
  }
 ]
}
```

**[búsqueda 'notificados fehacientemente']** → 1 hit(s)

--- `Excepcion_las_consultas_o_reclamos_originados_en_cuestiones_suscitadas_con_deudores_de_fid` — matchea en: ['properties.descripcion'] ---

```json
{
 "id": "Excepcion_las_consultas_o_reclamos_originados_en_cuestiones_suscitadas_con_deudores_de_fid",
 "type": "Excepcion",
 "label": "Atención por cedente en transferencias fiduciarias",
 "properties": {
  "descripcion": "Las consultas o reclamos originados en cuestiones suscitadas con deudores de fideicomisos financieros que no fueron notificados fehacientemente de la transferencia fiduciaria de su obligación deberán ser atendidos por el responsable de atención al usuario de servicios financieros de la entidad financiera cedente"
 },
 "provenances": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "Punto 3.1. Requisitos mínimos. (parte 1)"
  }
 ]
}
```

**[búsqueda 'transferencia de su obligación']** → 0 hit(s)

**VEREDICTO K-C:** fiduciario-Protección: 0 · otros términos: 8 · total portadores: ['Excepcion_beneficios_cedidos_a_proveedores_directos_con_convalidacion_de_la_secretaria_de_', 'Excepcion_excepcion_apertura_legajo_deudores_de_servicios_publicos', 'Excepcion_las_consultas_o_reclamos_originados_en_cuestiones_suscitadas_con_deudores_de_fid', 'Obligacion_abrir_legajo_de_firmante_librador_deudor', 'Obligacion_los_creditos_cedidos_a_favor_de_la_entidad_sin_responsabilidad_se_imputaran_al_f', 'Obligacion_proporcionar_informacion_a_sefyc', 'Restriccion_en_caso_de_no_efectuarse_la_evaluacion_de_creditos_cedidos_sin_responsabilidad_c', 'Restriccion_restriccion_de_uso_de_calificacion_de_emisor_a_creditos_quirografarios']

D1/ranking (pasos 1, 2, 8, 9, 10, 11, 14 de CQN2-010):
- **paso 1** — `fideicomiso financiero fiduciario acreedor usuarios` · límite 10:
    - Excepcion_beneficios_cedidos_a_proveedores_directos_con_convalidacion_de_la_secretaria_de_: NO en top-10 · global — de 50
    - Excepcion_excepcion_apertura_legajo_deudores_de_servicios_publicos: NO en top-10 · global — de 50
    - Excepcion_las_consultas_o_reclamos_originados_en_cuestiones_suscitadas_con_deudores_de_fid: NO en top-10 · global — de 50
    - Obligacion_abrir_legajo_de_firmante_librador_deudor: NO en top-10 · global — de 50
    - Obligacion_los_creditos_cedidos_a_favor_de_la_entidad_sin_responsabilidad_se_imputaran_al_f: NO en top-10 · global — de 50
    - Obligacion_proporcionar_informacion_a_sefyc: NO en top-10 · global — de 50
    - Restriccion_en_caso_de_no_efectuarse_la_evaluacion_de_creditos_cedidos_sin_responsabilidad_c: NO en top-10 · global — de 50
    - Restriccion_restriccion_de_uso_de_calificacion_de_emisor_a_creditos_quirografarios: NO en top-10 · global — de 50
- **paso 2** — `protección usuarios servicios financieros sujeto obligado` · límite 10:
    - Excepcion_beneficios_cedidos_a_proveedores_directos_con_convalidacion_de_la_secretaria_de_: NO en top-10 · global — de 50
    - Excepcion_excepcion_apertura_legajo_deudores_de_servicios_publicos: NO en top-10 · global — de 50
    - Excepcion_las_consultas_o_reclamos_originados_en_cuestiones_suscitadas_con_deudores_de_fid: NO en top-10 · global — de 50
    - Obligacion_abrir_legajo_de_firmante_librador_deudor: NO en top-10 · global — de 50
    - Obligacion_los_creditos_cedidos_a_favor_de_la_entidad_sin_responsabilidad_se_imputaran_al_f: NO en top-10 · global — de 50
    - Obligacion_proporcionar_informacion_a_sefyc: NO en top-10 · global — de 50
    - Restriccion_en_caso_de_no_efectuarse_la_evaluacion_de_creditos_cedidos_sin_responsabilidad_c: NO en top-10 · global — de 50
    - Restriccion_restriccion_de_uso_de_calificacion_de_emisor_a_creditos_quirografarios: NO en top-10 · global — de 50
- **paso 8** — `fiduciario sujeto obligado protección usuarios` · límite 10:
    - Excepcion_beneficios_cedidos_a_proveedores_directos_con_convalidacion_de_la_secretaria_de_: NO en top-10 · global — de 50
    - Excepcion_excepcion_apertura_legajo_deudores_de_servicios_publicos: NO en top-10 · global — de 50
    - Excepcion_las_consultas_o_reclamos_originados_en_cuestiones_suscitadas_con_deudores_de_fid: NO en top-10 · global — de 50
    - Obligacion_abrir_legajo_de_firmante_librador_deudor: NO en top-10 · global — de 50
    - Obligacion_los_creditos_cedidos_a_favor_de_la_entidad_sin_responsabilidad_se_imputaran_al_f: NO en top-10 · global — de 50
    - Obligacion_proporcionar_informacion_a_sefyc: NO en top-10 · global — de 50
    - Restriccion_en_caso_de_no_efectuarse_la_evaluacion_de_creditos_cedidos_sin_responsabilidad_c: NO en top-10 · global — de 50
    - Restriccion_restriccion_de_uso_de_calificacion_de_emisor_a_creditos_quirografarios: NO en top-10 · global — de 50
- **paso 9** — `deudor cedido usuario notificación cesión` · límite 10:
    - Excepcion_beneficios_cedidos_a_proveedores_directos_con_convalidacion_de_la_secretaria_de_: NO en top-10 · global — de 50
    - Excepcion_excepcion_apertura_legajo_deudores_de_servicios_publicos: NO en top-10 · global — de 50
    - Excepcion_las_consultas_o_reclamos_originados_en_cuestiones_suscitadas_con_deudores_de_fid: NO en top-10 · global — de 50
    - Obligacion_abrir_legajo_de_firmante_librador_deudor: NO en top-10 · global — de 50
    - Obligacion_los_creditos_cedidos_a_favor_de_la_entidad_sin_responsabilidad_se_imputaran_al_f: NO en top-10 · global — de 50
    - Obligacion_proporcionar_informacion_a_sefyc: NO en top-10 · global — de 50
    - Restriccion_en_caso_de_no_efectuarse_la_evaluacion_de_creditos_cedidos_sin_responsabilidad_c: NO en top-10 · global — de 50
    - Restriccion_restriccion_de_uso_de_calificacion_de_emisor_a_creditos_quirografarios: NO en top-10 · global — de 50
- **paso 10** — `fiduciario fideicomiso financiero sujeto obligado` · límite 10:
    - Excepcion_beneficios_cedidos_a_proveedores_directos_con_convalidacion_de_la_secretaria_de_: NO en top-10 · global — de 50
    - Excepcion_excepcion_apertura_legajo_deudores_de_servicios_publicos: NO en top-10 · global — de 50
    - Excepcion_las_consultas_o_reclamos_originados_en_cuestiones_suscitadas_con_deudores_de_fid: NO en top-10 · global — de 50
    - Obligacion_abrir_legajo_de_firmante_librador_deudor: NO en top-10 · global — de 50
    - Obligacion_los_creditos_cedidos_a_favor_de_la_entidad_sin_responsabilidad_se_imputaran_al_f: NO en top-10 · global — de 50
    - Obligacion_proporcionar_informacion_a_sefyc: NO en top-10 · global — de 50
    - Restriccion_en_caso_de_no_efectuarse_la_evaluacion_de_creditos_cedidos_sin_responsabilidad_c: NO en top-10 · global — de 50
    - Restriccion_restriccion_de_uso_de_calificacion_de_emisor_a_creditos_quirografarios: NO en top-10 · global — de 50
- **paso 11** — `deudor usuario cartera cedida fideicomiso` · límite 10:
    - Excepcion_beneficios_cedidos_a_proveedores_directos_con_convalidacion_de_la_secretaria_de_: NO en top-10 · global — de 50
    - Excepcion_excepcion_apertura_legajo_deudores_de_servicios_publicos: NO en top-10 · global — de 50
    - Excepcion_las_consultas_o_reclamos_originados_en_cuestiones_suscitadas_con_deudores_de_fid: NO en top-10 · global — de 50
    - Obligacion_abrir_legajo_de_firmante_librador_deudor: NO en top-10 · global — de 50
    - Obligacion_los_creditos_cedidos_a_favor_de_la_entidad_sin_responsabilidad_se_imputaran_al_f: NO en top-10 · global — de 50
    - Obligacion_proporcionar_informacion_a_sefyc: NO en top-10 · global — de 50
    - Restriccion_en_caso_de_no_efectuarse_la_evaluacion_de_creditos_cedidos_sin_responsabilidad_c: NO en top-10 · global — de 50
    - Restriccion_restriccion_de_uso_de_calificacion_de_emisor_a_creditos_quirografarios: NO en top-10 · global — de 50
- **paso 14** — `deudor cedido usuario aunque no notificado` · límite 10:
    - Excepcion_beneficios_cedidos_a_proveedores_directos_con_convalidacion_de_la_secretaria_de_: NO en top-10 · global — de 50
    - Excepcion_excepcion_apertura_legajo_deudores_de_servicios_publicos: NO en top-10 · global — de 50
    - Excepcion_las_consultas_o_reclamos_originados_en_cuestiones_suscitadas_con_deudores_de_fid: NO en top-10 · global — de 50
    - Obligacion_abrir_legajo_de_firmante_librador_deudor: NO en top-10 · global — de 50
    - Obligacion_los_creditos_cedidos_a_favor_de_la_entidad_sin_responsabilidad_se_imputaran_al_f: NO en top-10 · global — de 50
    - Obligacion_proporcionar_informacion_a_sefyc: NO en top-10 · global — de 50
    - Restriccion_en_caso_de_no_efectuarse_la_evaluacion_de_creditos_cedidos_sin_responsabilidad_c: NO en top-10 · global — de 50
    - Restriccion_restriccion_de_uso_de_calificacion_de_emisor_a_creditos_quirografarios: NO en top-10 · global — de 50


## K-D (CQN2-011, patas a) — programa de encuadramiento / cumplimiento en plazo máximo

El id `Obligacion_presentar_programa_de_encuadramiento` NO EXISTE en el kg por id
exacto; localización POR LABEL (la instrucción del ítem): 'Presentar programa de
encuadramiento' y 'Cumplimiento de exigencia en plazo máximo'. Se incluye además un
tercer nodo cuyo label también refiere al programa ('Presentación programa
encuadramiento'), hallado en el mismo barrido por label.

--- `Obligacion_las_entidades_financieras_en_funcionamiento_al_01_06_24_que_no_cumplan_con_la_in` (por label exacto: 'Presentar programa de encuadramiento') ---

```json
{
 "id": "Obligacion_las_entidades_financieras_en_funcionamiento_al_01_06_24_que_no_cumplan_con_la_in",
 "type": "Obligacion",
 "label": "Presentar programa de encuadramiento",
 "properties": {
  "descripcion": "Las entidades financieras en funcionamiento al 01/06/24 que no cumplan con la integración de la exigencia básica de capital deberán presentar a la SEFYC un programa de encuadramiento dentro de los 20 días corridos siguientes a la registración o proyección de incumplimiento",
  "tipo": "presentacion_informativa",
  "plazo": "20 días corridos"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Punto 12.1. Las entidades financieras en funcionamiento al 01/06/24 deberán observar la exig"
  }
 ]
}
```
```
edges de Obligacion_las_entidades_financieras_en_funcionamiento_al_01_06_24_que_no_cumplan_con_la_in: 3 salientes, 0 entrantes
SALIENTE: {"relation": "establecida_en", "target": "TextoOrdenado_to_capitales_minimos_actual_pdf"}
SALIENTE: {"relation": "aplica_a", "target": "EntidadFinanciera_sujeto_obligado"}
SALIENTE: {"relation": "regula", "target": "Operacion_presentacion_informativa"}
```

**¿Porta SEFYC / 20 días / 6 meses?** sefyc: SÍ · '20 dias': SÍ · '6 meses': NO · 'seis meses': NO

--- `Obligacion_el_programa_de_encuadramiento_no_debera_superar_los_6_meses_de_plazo_para_cumpli` (por label exacto: 'Cumplimiento de exigencia en plazo máximo') ---

```json
{
 "id": "Obligacion_el_programa_de_encuadramiento_no_debera_superar_los_6_meses_de_plazo_para_cumpli",
 "type": "Obligacion",
 "label": "Cumplimiento de exigencia en plazo máximo",
 "properties": {
  "descripcion": "El programa de encuadramiento no deberá superar los 6 meses de plazo para cumplir con la exigencia básica",
  "tipo": "otra",
  "plazo": "6 meses máximo"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Punto 12.1. Las entidades financieras en funcionamiento al 01/06/24 deberán observar la exig"
  }
 ]
}
```
```
edges de Obligacion_el_programa_de_encuadramiento_no_debera_superar_los_6_meses_de_plazo_para_cumpli: 2 salientes, 0 entrantes
SALIENTE: {"relation": "establecida_en", "target": "TextoOrdenado_to_capitales_minimos_actual_pdf"}
SALIENTE: {"relation": "aplica_a", "target": "EntidadFinanciera_sujeto_obligado"}
```

**¿Porta SEFYC / 20 días / 6 meses?** sefyc: NO · '20 dias': NO · '6 meses': SÍ · 'seis meses': NO

--- `Operacion_presentacion_informativa` (por label exacto (nodo adicional relacionado): 'Presentación programa encuadramiento') ---

```json
{
 "id": "Operacion_presentacion_informativa",
 "type": "Operacion",
 "label": "Presentación programa encuadramiento",
 "properties": {
  "tipo": "presentación informativa",
  "description": "Provisión de información a la SEFyC sobre tenencias de certificados de participación y/o títulos de deuda de fideicomisos"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Punto 12.1. Las entidades financieras en funcionamiento al 01/06/24 deberán observar la exig"
  }
 ]
}
```
```
edges de Operacion_presentacion_informativa: 2 salientes, 31 entrantes
SALIENTE: {"relation": "establecida_en", "target": "TextoOrdenado_to_exterior_cambios_actual_pdf"}
SALIENTE: {"relation": "establecida_en", "target": "TextoOrdenado_to_proteccion_usuarios_servicios_financieros_actual_pdf"}
ENTRANTE: {"relation": "regula", "source": "Obligacion_las_entidades_financieras_en_funcionamiento_al_01_06_24_que_no_cumplan_con_la_in"}
ENTRANTE: {"relation": "regula", "source": "Obligacion_proporcionar_informacion_a_sefyc"}
ENTRANTE: {"relation": "condiciona", "source": "Obligacion_la_revision_debera_estar_concluida_antes_de_presentarse_a_la_superintendencia_de"}
ENTRANTE: {"relation": "regula", "source": "Obligacion_obtener_declaracion_jurada_de_importador"}
ENTRANTE: {"relation": "regula", "source": "Obligacion_reportar_circunstancias"}
ENTRANTE: {"relation": "regula", "source": "Obligacion_registrar_diferencia_aduanera"}
ENTRANTE: {"relation": "regula", "source": "Obligacion_mantener_registro_de_certificaciones"}
ENTRANTE: {"relation": "regula", "source": "Obligacion_archivar_documentacion"}
ENTRANTE: {"relation": "condiciona", "source": "Obligacion_obligacion_de_reportar_circunstancias_modificatorias"}
ENTRANTE: {"relation": "regula", "source": "Restriccion_condiciones_previas_para_cesion_de_seguimiento"}
ENTRANTE: {"relation": "ejecuta", "source": "EntidadFinanciera_sujeto_obligado"}
ENTRANTE: {"relation": "regula", "source": "Obligacion_asumir_seguimiento_de_anticipos"}
ENTRANTE: {"relation": "regula", "source": "Obligacion_entregar_detalle_de_caracteristicas_y_comisiones"}
ENTRANTE: {"relation": "regula", "source": "Obligacion_publicar_modelos_de_contrato_de_adhesion"}
ENTRANTE: {"relation": "regula", "source": "Obligacion_garantizar_acceso_facil_a_informacion_en_sitio_web"}
ENTRANTE: {"relation": "regula", "source": "Obligacion_entregar_copia_integra_de_instrumentos_contractuales"}
ENTRANTE: {"relation": "regula", "source": "Obligacion_tambien_se_recibiran_de_los_usuarios_de_servicios_financieros_por_igual_via_come"}
ENTRANTE: {"relation": "condiciona", "source": "Obligacion_indicar_datos_de_identificacion_en_reclamo"}
ENTRANTE: {"relation": "condiciona", "source": "Obligacion_adjuntar_documentacion_de_identificacion"}
ENTRANTE: {"relation": "condiciona", "source": "Obligacion_relatar_hechos_y_reclamo_previo"}
ENTRANTE: {"relation": "condiciona", "source": "Obligacion_proveer_datos_de_identificacion_del_reclamo"}
ENTRANTE: {"relation": "condiciona", "source": "Obligacion_acompanar_documentacion_del_reclamo"}
ENTRANTE: {"relation": "limita", "source": "Restriccion_el_usuario_puede_informar_al_bcra_si_transcurre_el_plazo_de_diez_10_dias_habiles"}
ENTRANTE: {"relation": "regula", "source": "Obligacion_informar_ratio_de_apalancamiento_trimestral"}
ENTRANTE: {"relation": "regula", "source": "Obligacion_informar_modelos_de_informacion"}
ENTRANTE: {"relation": "prohibe", "source": "Restriccion_suspension_envio_consolidacion_nivel_3"}
ENTRANTE: {"relation": "regula", "source": "Obligacion_incluir_operaciones_entes_consolidados"}
ENTRANTE: {"relation": "limita", "source": "Restriccion_codigos_1_y_9_condicional_a_consolidacion"}
ENTRANTE: {"relation": "regula", "source": "Obligacion_los_datos_se_informaran_con_frecuencia_trimestral_y_se_integraran_con_los_datos_"}
ENTRANTE: {"relation": "regula", "source": "Obligacion_reportar_ingreso_bruto"}
ENTRANTE: {"relation": "regula", "source": "Obligacion_correlacionar_con_partidas_de_balance"}
```

**¿Porta SEFYC / 20 días / 6 meses?** sefyc: SÍ · '20 dias': NO · '6 meses': NO · 'seis meses': NO

**VEREDICTO K-D:** nodos hallados por label: ['Obligacion_las_entidades_financieras_en_funcionamiento_al_01_06_24_que_no_cumplan_con_la_in', 'Obligacion_el_programa_de_encuadramiento_no_debera_superar_los_6_meses_de_plazo_para_cumpli', 'Operacion_presentacion_informativa']. El nodo 'Presentar
programa de encuadramiento' porta SEFYC y 20 días; el nodo 'Cumplimiento de exigencia
en plazo máximo' porta 6 meses (sin SEFYC ni 20 días); el nodo adicional 'Presentación
programa encuadramiento' porta SEFyC pero su description habla de fideicomisos (ni 20
días ni 6 meses). Los dos nodos Obligacion no tienen vecinos entrantes y sus salientes
son solo `establecida_en`/`aplica_a` genéricos; `Operacion_presentacion_informativa`
tiene 31 entrantes (dumps de edges arriba).

D1/ranking (pasos 1, 9, 10, 12, 15 de CQN2-011):
- **paso 1** — `integración exigencia básica capital plan` · límite 10:
    - Obligacion_las_entidades_financieras_en_funcionamiento_al_01_06_24_que_no_cumplan_con_la_in: NO en top-10 · global — de 50
    - Obligacion_el_programa_de_encuadramiento_no_debera_superar_los_6_meses_de_plazo_para_cumpli: NO en top-10 · global — de 50
    - Operacion_presentacion_informativa: NO en top-10 · global — de 50
- **paso 9** — `plan integración capital no alcanzar plazo duración` · límite 10:
    - Obligacion_las_entidades_financieras_en_funcionamiento_al_01_06_24_que_no_cumplan_con_la_in: NO en top-10 · global — de 50
    - Obligacion_el_programa_de_encuadramiento_no_debera_superar_los_6_meses_de_plazo_para_cumpli: NO en top-10 · global 24 de 50
    - Operacion_presentacion_informativa: NO en top-10 · global — de 50
- **paso 10** — `plan integración capital BCRA presentar plazo máximo duración` · límite 10:
    - Obligacion_las_entidades_financieras_en_funcionamiento_al_01_06_24_que_no_cumplan_con_la_in: NO en top-10 · global — de 50
    - Obligacion_el_programa_de_encuadramiento_no_debera_superar_los_6_meses_de_plazo_para_cumpli: NO en top-10 · global 20 de 50
    - Operacion_presentacion_informativa: NO en top-10 · global — de 50
- **paso 12** — `plan integración capital no alcanzar exigencia básica presentar` · límite 10:
    - Obligacion_las_entidades_financieras_en_funcionamiento_al_01_06_24_que_no_cumplan_con_la_in: NO en top-10 · global 27 de 50
    - Obligacion_el_programa_de_encuadramiento_no_debera_superar_los_6_meses_de_plazo_para_cumpli: NO en top-10 · global 42 de 50
    - Operacion_presentacion_informativa: NO en top-10 · global — de 50
- **paso 15** — `punto 12 plan integración capital BCRA presentar` · límite 10:
    - Obligacion_las_entidades_financieras_en_funcionamiento_al_01_06_24_que_no_cumplan_con_la_in: NO en top-10 · global — de 50
    - Obligacion_el_programa_de_encuadramiento_no_debera_superar_los_6_meses_de_plazo_para_cumpli: NO en top-10 · global — de 50
    - Operacion_presentacion_informativa: NO en top-10 · global — de 50


## K-E (CQN2-011, patas b) — 10.10.2.1 de Exterior / excepción aeronavegación

**[búsqueda 'MiPyMe ∧ (14/04/25 | embarcad*)']** → 0 hit(s)

**[búsqueda '12.1 ∧ posicion*']** → 5 hit(s)

--- `Restriccion_las_posiciones_arancelarias_de_los_bienes_no_correspondan_a_aquellas_comprendida` — matchea en: ['label', 'properties.descripcion'] ---

```json
{
 "id": "Restriccion_las_posiciones_arancelarias_de_los_bienes_no_correspondan_a_aquellas_comprendida",
 "type": "Restriccion",
 "label": "Exclusión de posiciones arancelarias del punto 12.1",
 "properties": {
  "tipo": "limite_cualitativo",
  "descripcion": "Las posiciones arancelarias de los bienes no correspondan a aquellas comprendidas en el punto 12.1"
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 10.10. Disposiciones complementarias para importaciones de bienes que tuvieron o tendrá"
  }
 ]
}
```

--- `Restriccion_posiciones_arancelarias_ncm_8802_11_00_8802_12_10_8802_12_90_8802_20_10_8802_20_` — matchea en: ['provenances[0]'] ---

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

--- `Excepcion_quedan_exceptuadas_las_importaciones_realizadas_por_empresas_que_presten_servici` — matchea en: ['provenances[0]'] ---

```json
{
 "id": "Excepcion_quedan_exceptuadas_las_importaciones_realizadas_por_empresas_que_presten_servici",
 "type": "Excepcion",
 "label": "Excepción para aeronavegación",
 "properties": {
  "descripcion": "Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación"
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 12.1. Posiciones arancelarias referidas en los puntos 10.10.2.1. y 10.10.2.2."
  }
 ]
}
```

--- `EntidadFinanciera_empresa_de_aeronavegacion` — matchea en: ['provenances[0]'] ---

```json
{
 "id": "EntidadFinanciera_empresa_de_aeronavegacion",
 "type": "EntidadFinanciera",
 "label": "Empresas de aeronavegación",
 "properties": {
  "categoria": "empresa que presta servicios de aeronavegación"
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 12.1. Posiciones arancelarias referidas en los puntos 10.10.2.1. y 10.10.2.2."
  }
 ]
}
```

--- `Operacion_importacion_de_bienes_aeronaves` — matchea en: ['provenances[0]'] ---

```json
{
 "id": "Operacion_importacion_de_bienes_aeronaves",
 "type": "Operacion",
 "label": "Importación de aeronaves",
 "properties": {
  "tipo": "importación de bienes (aeronaves)"
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 12.1. Posiciones arancelarias referidas en los puntos 10.10.2.1. y 10.10.2.2."
  }
 ]
}
```

**[búsqueda 'aeronavegación']** → 2 hit(s)

--- `Excepcion_quedan_exceptuadas_las_importaciones_realizadas_por_empresas_que_presten_servici` — matchea en: ['label', 'properties.descripcion'] ---

```json
{
 "id": "Excepcion_quedan_exceptuadas_las_importaciones_realizadas_por_empresas_que_presten_servici",
 "type": "Excepcion",
 "label": "Excepción para aeronavegación",
 "properties": {
  "descripcion": "Quedan exceptuadas las importaciones realizadas por empresas que presten servicios de aeronavegación"
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 12.1. Posiciones arancelarias referidas en los puntos 10.10.2.1. y 10.10.2.2."
  }
 ]
}
```

--- `EntidadFinanciera_empresa_de_aeronavegacion` — matchea en: ['id', 'label', 'properties.categoria'] ---

```json
{
 "id": "EntidadFinanciera_empresa_de_aeronavegacion",
 "type": "EntidadFinanciera",
 "label": "Empresas de aeronavegación",
 "properties": {
  "categoria": "empresa que presta servicios de aeronavegación"
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 12.1. Posiciones arancelarias referidas en los puntos 10.10.2.1. y 10.10.2.2."
  }
 ]
}
```

**VEREDICTO K-E:** MiPyMe-10.10.2.1: 0 · exclusión-12.1: 5 · aeronavegación: 2


## K-F (CQN2-012) — llave negativa / 11.2 / fórmula 70200000

**[búsqueda 'llave de negocio negativa']** → 0 hit(s)

**[búsqueda 'Previsiones del Pasivo']** → 0 hit(s)

**[búsqueda '11.2: fusion ∧ (adicion|absorc) ∧ rpc']** → 0 hit(s)

**[búsqueda 'CDCOn1 | (COn1-']** → 1 hit(s)

--- `Operacion_calculo_de_deductibles_de_capital` — matchea en: ['properties.description'] ---

```json
{
 "id": "Operacion_calculo_de_deductibles_de_capital",
 "type": "Operacion",
 "label": "Cálculo de conceptos deducibles",
 "properties": {
  "tipo": "cálculo de deductibles de capital",
  "description": "Determinación de Conceptos deducibles del Capital Ordinario de Nivel 1 (CDCoN1)"
 },
 "provenances": [
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Punto 6.2. Modelo de Información (parte 1)"
  }
 ]
}
```

--- `Restriccion_responsabilidad_patrimonial_computable_rpc_70200000_8_s_70900000` (por id exacto) ---
```json
{
 "id": "Restriccion_responsabilidad_patrimonial_computable_rpc_70200000_8_s_70900000",
 "type": "Restriccion",
 "label": "Límite mínimo Responsabilidad Patrimonial Computable",
 "properties": {
  "descripcion": "Responsabilidad Patrimonial Computable (RPC) = 70200000 ≥ 8% s/70900000",
  "tipo": "limite_cuantitativo",
  "umbral": "8%"
 },
 "provenances": [
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Punto 6.3. Límites mínimos:"
  }
 ]
}
```

**VEREDICTO K-F:** llave-negativa: 0 · previsiones-pasivo: 0 · 11.2-fusión: 0 · fórmula-CDCOn1: 1 · nodo 70200000: existe

D1/ranking (pasos 1, 8, 14 de CQN2-012) sobre los portadores hallados:
- **paso 1** — `responsabilidad patrimonial computable RPC fusión` · límite 10:
    - Operacion_calculo_de_deductibles_de_capital: NO en top-10 · global — de 35
    - Restriccion_responsabilidad_patrimonial_computable_rpc_70200000_8_s_70900000: posición 1 de 10 · global 1 de 35
- **paso 8** — `total control régimen informativo exigencia integración` · límite 10:
    - Operacion_calculo_de_deductibles_de_capital: NO en top-10 · global — de 50
    - Restriccion_responsabilidad_patrimonial_computable_rpc_70200000_8_s_70900000: NO en top-10 · global — de 50
- **paso 14** — `total integración control régimen informativo capitales` · límite 10:
    - Operacion_calculo_de_deductibles_de_capital: NO en top-10 · global — de 50
    - Restriccion_responsabilidad_patrimonial_computable_rpc_70200000_8_s_70900000: NO en top-10 · global — de 50


## K-G (CQN2-013) — 13.2.7.1 verdadero / nodo quimérico

**[búsqueda 'vinculada ∧ 90 ∧ 14/04/25 (mismo nodo)']** → 1 hit(s)

--- `Restriccion_requisito_plazo_contrapartes_vinculadas` — matchea en: ['properties.description'] ---

```json
{
 "id": "Restriccion_requisito_plazo_contrapartes_vinculadas",
 "type": "Restriccion",
 "label": "Requisito: plazo contrapartes vinculadas",
 "properties": {
  "tipo": "limite_cualitativo",
  "description": "Servicio no comprendido en puntos 13.2.1 a 13.2.5 provisto por contraparte vinculada: 90 días corridos si prestación a partir del 14/04/25, o 180 días corridos si prestación previa al 14/04/25"
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 13.2. Pagos de servicios que fueron o serán prestados o devengados a partir del 13/12/"
  }
 ]
}
```

--- `Restriccion_requisito_plazo_90_dias_para_servicio_no_comprendido` (el quimérico, por id exacto — para el archivo de evidencia) ---
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

**VEREDICTO K-G:** nodos con el 13.2.7.1 VERDADERO completo: 1 · quimérico: existe (dump arriba)


## K-H (CQN2-014) — mejoramiento / extenderse / situación individual (emergencia)

**[búsqueda 'mejoramiento']** → 0 hit(s)

**[búsqueda 'extenderse']** → 0 hit(s)

**[búsqueda 'situación individual']** → 0 hit(s)

**VEREDICTO K-H:** 0 portador(es): NINGUNO

D1/ranking (pasos 2, 6 de CQN2-014):
  (sin portadores → ranking NO aplica)


## K-I (CQN2-015) — país de constitución / no calificados podrá recibir / 2.12.2.2-.3

**[búsqueda 'país de constitución']** → 1 hit(s)

--- `Restriccion_prohibicion_de_ponderador_menor_para_deudores_no_calificados` — matchea en: ['properties.description'] ---

```json
{
 "id": "Restriccion_prohibicion_de_ponderador_menor_para_deudores_no_calificados",
 "type": "Restriccion",
 "label": "Prohibición de ponderador menor para deudores no calificados",
 "properties": {
  "tipo": "prohibicion",
  "description": "Ninguna exposición con deudores no calificados podrá recibir un ponderador de riesgo menor que el que se aplica al país de constitución, excepto que se trate de las exposiciones a que se refieren los puntos 2.12.2.2. y 2.12.2.3"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Punto 2.5. Criterios para la determinación de los activos ponderados por riesgo."
  }
 ]
}
```

**[búsqueda 'no calificado(s) podrá recibir']** → 1 hit(s)

--- `Restriccion_prohibicion_de_ponderador_menor_para_deudores_no_calificados` — matchea en: ['properties.description'] ---

```json
{
 "id": "Restriccion_prohibicion_de_ponderador_menor_para_deudores_no_calificados",
 "type": "Restriccion",
 "label": "Prohibición de ponderador menor para deudores no calificados",
 "properties": {
  "tipo": "prohibicion",
  "description": "Ninguna exposición con deudores no calificados podrá recibir un ponderador de riesgo menor que el que se aplica al país de constitución, excepto que se trate de las exposiciones a que se refieren los puntos 2.12.2.2. y 2.12.2.3"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Punto 2.5. Criterios para la determinación de los activos ponderados por riesgo."
  }
 ]
}
```

**[búsqueda 'código de descuento']** → 0 hit(s)

**[búsqueda 'seguridad social ∧ 30']** → 0 hit(s)

**VEREDICTO K-I:** 1 portador(es): ['Restriccion_prohibicion_de_ponderador_menor_para_deudores_no_calificados']

D1/ranking (pasos 1, 2, 3, 7, 9 de CQN2-015):
- **paso 1** — `capital mínimo riesgo crédito ponderador deudor no calificado` · límite 10:
    - Restriccion_prohibicion_de_ponderador_menor_para_deudores_no_calificados: NO en top-10 · global — de 50
- **paso 2** — `piso ponderador riesgo exposición deudor` · límite 10:
    - Restriccion_prohibicion_de_ponderador_menor_para_deudores_no_calificados: NO en top-10 · global — de 50
- **paso 3** — `deudor no calificado ponderador piso` · límite 10:
    - Restriccion_prohibicion_de_ponderador_menor_para_deudores_no_calificados: NO en top-10 · global 12 de 50
- **paso 7** — `no calificado ponderador` · límite 10:
    - Restriccion_prohibicion_de_ponderador_menor_para_deudores_no_calificados: NO en top-10 · global 11 de 50
- **paso 9** — `ponderador riesgo exposición deudor sin calificación` · límite 10:
    - Restriccion_prohibicion_de_ponderador_menor_para_deudores_no_calificados: NO en top-10 · global — de 50


---

**Sello:** 2026-07-19 · HEAD: `df295255dad7202c39931e8e79eb7def688f1c04` · grafo run_3 congelado (4050 nodos). Sellado por inexistencia vigente.
