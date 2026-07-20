# Hoja de adjudicación v2 — dev set (adjudicación CIEGA)

Generada 2026-07-14 desde: `queries/eval_set_v1.json` (pregunta verbatim), `posthoc_run/traces/{label}/{run}/CQ-*.json` (trayectoria del agente, rep 1, y veredictos del juez por claim), `kg.json` congelados de run_1/run_5 (nodos íntegros) y `pdf_locate` sobre `data/experiment/subset/` (pasajes GT).

**Cambio 1 (vs hoja v1):** TODOS los outputs de tool calls de las secciones 3 y 4 provienen de RE-EJECUCIÓN determinística (`GraphIndex` sobre el kg congelado del run), nunca del almacenado en la traza (que trunca a 1.200 chars). Cada paso está marcado: `[RE-EJECUTADO — almacenado truncado]` cuando la traza tenía el output cortado, `[re-ejecutado; almacenado ya completo, verificado idéntico]` cuando no.
**Cambio 2 (vs hoja v1):** cada caso tiene una sección 5b con los provenances VERBATIM (lista completa del kg.json) de los nodos citados en la respuesta final.

Esta hoja NO contiene etiquetas, confianzas ni sugerencias de ningún verificador automático: la adjudicación se hace contra la evidencia cruda de abajo, con la taxonomía v2 (`taxonomia.md`: capa 1 por precedencia POR PATA; capa 2 por el árbol).

---

## Caso off/run_1/CQ-016

### 1. Pregunta (verbatim eval_set_v1) y patas (judge.step1.patas_de_la_pregunta)

> ¿En qué unidad y con qué nivel de decimales deben registrarse los importes en el Régimen Informativo de Exigencia e Integración de Capitales Mínimos?

- Categoría: `factual_directa` · TOs fuente: regimen
- Ground-truth secciones: Punto 1.2 (Sección 1, Instrucciones generales)
- Pata 1: "Unidad en que deben registrarse los importes en el Régimen Informativo de Exigencia e Integración de Capitales Mínimos"
- Pata 2: "Nivel de decimales con que deben registrarse los importes en el Régimen Informativo de Exigencia e Integración de Capitales Mínimos"

### 2. Claims con veredicto negativo del juez (verbatim)
- [no_soportado] secundaria — «Esta disposición proviene del Régimen Informativo Contable Mensual.»
- cobertura_patas: [{"pata": "Unidad en que deben registrarse los importes en el Régimen Informativo de Exigencia e Integración de Capitales Mínimos", "cobertura": "cubierta"}, {"pata": "Nivel de decimales con que deben registrarse los importes en el Régimen Informativo de Exigencia e Integración de Capitales Mínimos", "cobertura": "cubierta"}]
- (juez, otros campos verbatim) cita_documento_correcto: false · cita_precision: "pagina" · abstencion: null

### 3. Trayectoria del agente (tool calls, rep 1) — outputs COMPLETOS por re-ejecución determinística (tool_calls_used: 15 · hit_tool_limit: True)

- paso 1 · `buscar_nodos` · input: `{"consulta": "Régimen Informativo Exigencia Integración Capitales Mínimos", "limite": 10}` **[RE-EJECUTADO — almacenado truncado]**
  ```json
  {"consulta": "Régimen Informativo Exigencia Integración Capitales Mínimos", "total_con_match": 181, "resultados": [{"id": "prc_regimen_informativo_exigencia_e_integracion_de_capitales_minimos", "type": "PROCESS", "label": "Régimen informativo Exigencia e integración de capitales mínimos", "tokens_matcheados": 6, "resumen_propiedades": "Sistema de reporte que contiene nómina de partidas e instrucciones para determinación de exigencias registradas en códigos 70810000 y 70820000."}, {"id": "con_exigencia_e_integracion_de_capitales_minimos", "type": "CONCEPT", "label": "Exigencia e integración de capitales mínimos", "tokens_matcheados": 4, "resumen_propiedades": "Exigencia regulatoria del BCRA relativa al cálculo, composición y cumplimiento de capitales mínimos requeridos a las entidades."}, {"id": "req_exigencia_de_integracion_de_capitales_minimos", "type": "REQUIREMENT", "label": "Exigencia de Integración de Capitales Mínimos", "tokens_matcheados": 4, "resumen_propiedades": "Sección 4 del Régimen Informativo Contable Mensual que establece la obligación de mantener capital computable según componentes definidos."}, {"id": "rep_regimen_informativo_contable_mensual_sobre_capitales_minimos", "type": "REPORT_ITEM", "label": "Régimen Informativo Contable Mensual sobre Capitales Mínimos", "tokens_matcheados": 4, "resumen_propiedades": "Esquema informativo (R.I.-C.M.) que regula la presentación de datos sobre exigencia e integración de capitales mínimos."}, {"id": "req_incremento_de_exigencia_de_capitales_minimos", "type": "REQUIREMENT", "label": "Incremento de exigencia de capitales mínimos", "tokens_matcheados": 3, "resumen_propiedades": "Incremento regulatorio por excesos en activos inmovilizados, grandes exposiciones, financiamiento al sector público no financiero, derivados no cubiertos y otro…"}, {"id": "req_exigencia_de_capitales_minimos_por_riesgo_de_credito", "type": "REQUIREMENT", "label": "Exigencia de Capitales Mínimos por riesgo de crédito", "tokens_matcheados": 3, "resumen_propiedades": "Exigencia regulatoria de capitales mínimos ponderados por riesgo de crédito, medida según factores de ponderación específicos."}, {"id": "req_exigencia_de_capitales_minimos_por_riesgo_de_mercado", "type": "REQUIREMENT", "label": "exigencia de capitales mínimos por riesgo de mercado", "tokens_matcheados": 3, "resumen_propiedades": "Requerimiento de capital regulatorio determinado por la ponderación de posiciones de riesgo de mercado."}, {"id": "req_incumplimientos_en_relaciones_crediticias_generan_incrementos_de_exigencia_de_capitales_minimos", "type": "REQUIREMENT", "label": "Incumplimientos en relaciones crediticias (generan incrementos de exigencia de capitales mínimos)", "tokens_matcheados": 3, "resumen_propiedades": "Incumplimientos en relaciones técnicas crediticias que generan incrementos de exigencia de capitales mínimos por riesgo de crédito."}, {"id": "con_capitales_minimos", "type": "CONCEPT", "label": "Capitales mínimos", "tokens_matcheados": 2, "resumen_propiedades": "Exigencia de capitales mínimos para entidades financieras, calculada con incrementos según porcentajes establecidos en normas sobre capitales mínimos."}, {"id": "req_capitales_minimos", "type": "REQUIREMENT", "label": "Capitales Mínimos", "tokens_matcheados": 2, "resumen_propiedades": "Exigencia regulatoria de integración de capital mínimo para entidades financieras conforme al Régimen Informativo Contable Mensual."}]}
  ```
- paso 2 · `buscar_nodos` · input: `{"consulta": "importes unidad decimales registro", "limite": 10}` **[RE-EJECUTADO — almacenado truncado]**
  ```json
  {"consulta": "importes unidad decimales registro", "total_con_match": 51, "resultados": [{"id": "rep_registro_de_reintegros_de_importes_rri", "type": "REPORT_ITEM", "label": "Registro de Reintegros de Importes (RRI)", "tokens_matcheados": 2, "resumen_propiedades": "Registro donde se asientan montos reintegrados a usuarios, identificando usuario afectado, causal, productos y casas involucradas."}, {"id": "prc_registro_en_sepaimpo", "type": "PROCESS", "label": "Registro en SEPAIMPO", "tokens_matcheados": 1, "resumen_propiedades": "Proceso de efectuar registros correspondientes en el SEPAIMPO, a cargo de la entidad que cursó el pago."}, {"id": "prc_registro_ante_el_bcra", "type": "PROCESS", "label": "Registro ante el BCRA", "tokens_matcheados": 1, "resumen_propiedades": "Procedimiento administrativo mediante el cual el cambio de entidad nominada responsable queda formalizado y efectivo."}, {"id": "con_registro_aduanero_pendiente", "type": "CONCEPT", "label": "Registro aduanero pendiente", "tokens_matcheados": 1, "resumen_propiedades": "Situación de importaciones de bienes que requieren acceso al mercado de cambios sin contar aún con la oficialización del despacho de importación."}, {"id": "prc_registro_de_certificaciones", "type": "PROCESS", "label": "Registro de certificaciones", "tokens_matcheados": 1, "resumen_propiedades": "Proceso de documentación de certificaciones emitidas, anuladas y otros movimientos imputados al despacho."}, {"id": "con_registro_aduanero_de_ingreso", "type": "CONCEPT", "label": "Registro aduanero de ingreso", "tokens_matcheados": 1, "resumen_propiedades": "Documento o registro oficial emitido por aduanas que registra despachos de importación y sus características."}, {"id": "prc_registro_de_ingreso_aduanero", "type": "PROCESS", "label": "registro de ingreso aduanero", "tokens_matcheados": 1, "resumen_propiedades": "Procedimiento administrativo de entrada legal de bienes al país, requisito para acceso al mercado de cambios."}, {"id": "reg_registro_publico_de_comercio", "type": "REGULATOR", "label": "Registro Público de Comercio", "tokens_matcheados": 1, "resumen_propiedades": "Organismo ante el cual se inscribe la decisión de capitalización definitiva de aportes de capital."}, {"id": "req_registro_de_ingreso_aduanero", "type": "REQUIREMENT", "label": "Registro de ingreso aduanero", "tokens_matcheados": 1, "resumen_propiedades": "Procedimiento administrativo mediante el cual se documenta el ingreso de bienes de capital importados, constituyendo fecha clave para registro contable en bolet…"}, {"id": "prc_custodia_y_registro_de_titulos", "type": "PROCESS", "label": "Custodia y registro de títulos", "tokens_matcheados": 1, "resumen_propiedades": "Procedimiento por el cual BCRA, agentes de CNV y depósitos centrales mantienen a cargo la custodia de títulos de crédito."}]}
  ```
- paso 3 · `ver_nodo` · input: `{"id": "prc_regimen_informativo_exigencia_e_integracion_de_capitales_minimos"}` [re-ejecutado; almacenado ya completo, verificado idéntico]
  → nodo prc_regimen_informativo_exigencia_e_integracion_de_capitales_minimos (Régimen informativo Exigencia e integración de capitales mínimos) — contenido íntegro abajo (§4)
- paso 4 · `ver_vecinos` · input: `{"id": "prc_regimen_informativo_exigencia_e_integracion_de_capitales_minimos", "direccion": "ambas"}` [re-ejecutado; almacenado ya completo, verificado idéntico]
  ```json
  {"id": "prc_regimen_informativo_exigencia_e_integracion_de_capitales_minimos", "label": "Régimen informativo Exigencia e integración de capitales mínimos", "n_salientes_total": 2, "n_entrantes_total": 0, "salientes": [{"relation": "contiene_instrucciones_para", "vecino_id": "rep_codigo_70810000", "vecino_label": "Código 70810000", "provenances": [{"source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf", "location": "p. 57"}]}, {"relation": "contiene_instrucciones_para", "vecino_id": "rep_codigo_70820000", "vecino_label": "Código 70820000", "provenances": [{"source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf", "location": "p. 57"}]}], "salientes_truncado": false, "entrantes": [], "entrantes_truncado": false}
  ```
- paso 5 · `buscar_nodos` · input: `{"consulta": "capitales mínimos unidad pesos decimales", "limite": 10}` **[RE-EJECUTADO — almacenado truncado]**
  ```json
  {"consulta": "capitales mínimos unidad pesos decimales", "total_con_match": 44, "resultados": [{"id": "con_capitales_minimos", "type": "CONCEPT", "label": "Capitales mínimos", "tokens_matcheados": 2, "resumen_propiedades": "Exigencia de capitales mínimos para entidades financieras, calculada con incrementos según porcentajes establecidos en normas sobre capitales mínimos."}, {"id": "req_capitales_minimos", "type": "REQUIREMENT", "label": "Capitales Mínimos", "tokens_matcheados": 2, "resumen_propiedades": "Exigencia regulatoria de integración de capital mínimo para entidades financieras conforme al Régimen Informativo Contable Mensual."}, {"id": "req_requisito_de_capitales_minimos", "type": "REQUIREMENT", "label": "Requisito de capitales mínimos", "tokens_matcheados": 2, "resumen_propiedades": "Exigencia cuantitativa de capital mínimo que no puede ser menor al de la cartera de créditos original."}, {"id": "req_capitales_minimos_de_entidades_financieras", "type": "REQUIREMENT", "label": "capitales mínimos de entidades financieras", "tokens_matcheados": 2, "resumen_propiedades": "Exigencia cuantitativa de capital mínimo que deben mantener las entidades financieras, sujeta a actualización y modificaciones normativas."}, {"id": "con_exigencia_e_integracion_de_capitales_minimos", "type": "CONCEPT", "label": "Exigencia e integración de capitales mínimos", "tokens_matcheados": 2, "resumen_propiedades": "Exigencia regulatoria del BCRA relativa al cálculo, composición y cumplimiento de capitales mínimos requeridos a las entidades."}, {"id": "req_incremento_de_exigencia_de_capitales_minimos", "type": "REQUIREMENT", "label": "Incremento de exigencia de capitales mínimos", "tokens_matcheados": 2, "resumen_propiedades": "Incremento regulatorio por excesos en activos inmovilizados, grandes exposiciones, financiamiento al sector público no financiero, derivados no cubiertos y otro…"}, {"id": "rep_partidas_fuera_de_balance_capitales_minimos", "type": "REPORT_ITEM", "label": "Partidas fuera de balance - Capitales Mínimos", "tokens_matcheados": 2, "resumen_propiedades": "Código 1221000/CCF que identifica compromisos y operaciones fuera de balance incluidas en normas de capitales mínimos."}, {"id": "req_exigencia_de_integracion_de_capitales_minimos", "type": "REQUIREMENT", "label": "Exigencia de Integración de Capitales Mínimos", "tokens_matcheados": 2, "resumen_propiedades": "Sección 4 del Régimen Informativo Contable Mensual que establece la obligación de mantener capital computable según componentes definidos."}, {"id": "con_capitales_minimos_de_las_entidades_financieras", "type": "CONCEPT", "label": "Capitales mínimos de las entidades financieras", "tokens_matcheados": 2, "resumen_propiedades": "Normas que regulan los capitales mínimos que deben mantener las entidades financieras según su clasificación."}, {"id": "req_exigencia_de_capitales_minimos_por_riesgo_de_credito", "type": "REQUIREMENT", "label": "Exigencia de Capitales Mínimos por riesgo de crédito", "tokens_matcheados": 2, "resumen_propiedades": "Exigencia regulatoria de capitales mínimos ponderados por riesgo de crédito, medida según factores de ponderación específicos."}]}
  ```
- paso 6 · `buscar_nodos` · input: `{"consulta": "importes miles pesos decimales", "limite": 10}` **[RE-EJECUTADO — almacenado truncado]**
  ```json
  {"consulta": "importes miles pesos decimales", "total_con_match": 21, "resultados": [{"id": "req_miles_de_pesos", "type": "REQUIREMENT", "label": "Miles de pesos", "tokens_matcheados": 2, "resumen_propiedades": "Unidad de registro de importes, sin decimales."}, {"id": "con_cuenta_en_pesos", "type": "CONCEPT", "label": "Cuenta en pesos", "tokens_matcheados": 1, "resumen_propiedades": "Cuenta local del cliente en moneda nacional que puede ser asociada a tarjetas para operaciones en el exterior."}, {"id": "ope_conversion_a_pesos", "type": "OPERATION", "label": "Conversión a pesos", "tokens_matcheados": 1, "resumen_propiedades": "Conversión de valores expresados en moneda extranjera a moneda local para propósitos de cálculo regulatorio."}, {"id": "cla_posiciones_en_pesos", "type": "CLASSIFICATION", "label": "Posiciones en pesos", "tokens_matcheados": 1, "resumen_propiedades": "Exposiciones denominadas en moneda de curso legal argentina, calculadas por separado en la exigencia de capital por riesgo general de mercado."}, {"id": "rep_posiciones_en_pesos", "type": "REPORT_ITEM", "label": "posiciones en pesos", "tokens_matcheados": 1, "resumen_propiedades": "Información de exposiciones en pesos reportada en cuadros 11.2.1 a) y 11.2.2 a)."}, {"id": "ope_pase_pasivo_en_pesos", "type": "OPERATION", "label": "Pase pasivo en pesos", "tokens_matcheados": 1, "resumen_propiedades": "Operación en la cual se aplica el criterio de posición neta de títulos para exposiciones al sector público no financiero fondeadas con depósitos de títulos públ…"}, {"id": "ins_caja_de_ahorros_en_pesos", "type": "INSTRUMENT", "label": "caja de ahorros en pesos", "tokens_matcheados": 1, "resumen_propiedades": "Producto de depósito de ahorro en moneda nacional con prestaciones previstas en el TO sobre Depósitos de Ahorro, Cuenta Sueldo y Especiales."}, {"id": "ope_prestamo_hipotecario_en_pesos", "type": "OPERATION", "label": "Préstamo hipotecario en pesos", "tokens_matcheados": 1, "resumen_propiedades": "Operación de préstamo en pesos para compra de vivienda que permite canalizar fondos al pago de inmuebles en moneda extranjera mediante compraventa de títulos va…"}, {"id": "ins_boletos_sin_movimiento_de_pesos", "type": "INSTRUMENT", "label": "Boletos sin movimiento de pesos", "tokens_matcheados": 1, "resumen_propiedades": "Documentos operacionales que se confeccionan para registrar operaciones de compra y venta de cambio bajo excepción sin movimiento de pesos."}, {"id": "ope_liquidacion_en_pesos_en_el_pais", "type": "OPERATION", "label": "Liquidación en pesos en el país", "tokens_matcheados": 1, "resumen_propiedades": "Forma de pago de operaciones usando moneda nacional dentro del territorio argentino."}]}
  ```
- paso 7 · `ver_nodo` · input: `{"id": "req_miles_de_pesos"}` [re-ejecutado; almacenado ya completo, verificado idéntico]
  → nodo req_miles_de_pesos (Miles de pesos) — contenido íntegro abajo (§4)
- paso 8 · `ver_vecinos` · input: `{"id": "req_miles_de_pesos", "direccion": "ambas"}` [re-ejecutado; almacenado ya completo, verificado idéntico]
  ```json
  {"id": "req_miles_de_pesos", "label": "Miles de pesos", "n_salientes_total": 0, "n_entrantes_total": 0, "salientes": [], "salientes_truncado": false, "entrantes": [], "entrantes_truncado": false}
  ```
- paso 9 · `buscar_nodos` · input: `{"consulta": "instrucciones registro capitales mínimos 70810000 70820000", "limite": 10}` **[RE-EJECUTADO — almacenado truncado]**
  ```json
  {"consulta": "instrucciones registro capitales mínimos 70810000 70820000", "total_con_match": 69, "resultados": [{"id": "con_capitales_minimos", "type": "CONCEPT", "label": "Capitales mínimos", "tokens_matcheados": 2, "resumen_propiedades": "Exigencia de capitales mínimos para entidades financieras, calculada con incrementos según porcentajes establecidos en normas sobre capitales mínimos."}, {"id": "req_capitales_minimos", "type": "REQUIREMENT", "label": "Capitales Mínimos", "tokens_matcheados": 2, "resumen_propiedades": "Exigencia regulatoria de integración de capital mínimo para entidades financieras conforme al Régimen Informativo Contable Mensual."}, {"id": "req_requisito_de_capitales_minimos", "type": "REQUIREMENT", "label": "Requisito de capitales mínimos", "tokens_matcheados": 2, "resumen_propiedades": "Exigencia cuantitativa de capital mínimo que no puede ser menor al de la cartera de créditos original."}, {"id": "req_capitales_minimos_de_entidades_financieras", "type": "REQUIREMENT", "label": "capitales mínimos de entidades financieras", "tokens_matcheados": 2, "resumen_propiedades": "Exigencia cuantitativa de capital mínimo que deben mantener las entidades financieras, sujeta a actualización y modificaciones normativas."}, {"id": "con_exigencia_e_integracion_de_capitales_minimos", "type": "CONCEPT", "label": "Exigencia e integración de capitales mínimos", "tokens_matcheados": 2, "resumen_propiedades": "Exigencia regulatoria del BCRA relativa al cálculo, composición y cumplimiento de capitales mínimos requeridos a las entidades."}, {"id": "req_incremento_de_exigencia_de_capitales_minimos", "type": "REQUIREMENT", "label": "Incremento de exigencia de capitales mínimos", "tokens_matcheados": 2, "resumen_propiedades": "Incremento regulatorio por excesos en activos inmovilizados, grandes exposiciones, financiamiento al sector público no financiero, derivados no cubiertos y otro…"}, {"id": "rep_partidas_fuera_de_balance_capitales_minimos", "type": "REPORT_ITEM", "label": "Partidas fuera de balance - Capitales Mínimos", "tokens_matcheados": 2, "resumen_propiedades": "Código 1221000/CCF que identifica compromisos y operaciones fuera de balance incluidas en normas de capitales mínimos."}, {"id": "req_exigencia_de_integracion_de_capitales_minimos", "type": "REQUIREMENT", "label": "Exigencia de Integración de Capitales Mínimos", "tokens_matcheados": 2, "resumen_propiedades": "Sección 4 del Régimen Informativo Contable Mensual que establece la obligación de mantener capital computable según componentes definidos."}, {"id": "con_capitales_minimos_de_las_entidades_financieras", "type": "CONCEPT", "label": "Capitales mínimos de las entidades financieras", "tokens_matcheados": 2, "resumen_propiedades": "Normas que regulan los capitales mínimos que deben mantener las entidades financieras según su clasificación."}, {"id": "req_exigencia_de_capitales_minimos_por_riesgo_de_credito", "type": "REQUIREMENT", "label": "Exigencia de Capitales Mínimos por riesgo de crédito", "tokens_matcheados": 2, "resumen_propiedades": "Exigencia regulatoria de capitales mínimos ponderados por riesgo de crédito, medida según factores de ponderación específicos."}]}
  ```
- paso 10 · `ver_nodo` · input: `{"id": "rep_codigo_70810000"}` [re-ejecutado; almacenado ya completo, verificado idéntico]
  → nodo rep_codigo_70810000 (Código 70810000) — contenido íntegro abajo (§4)
- paso 11 · `ver_nodo` · input: `{"id": "rep_codigo_70820000"}` [re-ejecutado; almacenado ya completo, verificado idéntico]
  → nodo rep_codigo_70820000 (Código 70820000) — contenido íntegro abajo (§4)
- paso 12 · `buscar_nodos` · input: `{"consulta": "instrucciones generales registro importes unidad", "limite": 10}` **[RE-EJECUTADO — almacenado truncado]**
  ```json
  {"consulta": "instrucciones generales registro importes unidad", "total_con_match": 56, "resultados": [{"id": "rep_registro_de_reintegros_de_importes_rri", "type": "REPORT_ITEM", "label": "Registro de Reintegros de Importes (RRI)", "tokens_matcheados": 2, "resumen_propiedades": "Registro donde se asientan montos reintegrados a usuarios, identificando usuario afectado, causal, productos y casas involucradas."}, {"id": "prc_registro_en_sepaimpo", "type": "PROCESS", "label": "Registro en SEPAIMPO", "tokens_matcheados": 1, "resumen_propiedades": "Proceso de efectuar registros correspondientes en el SEPAIMPO, a cargo de la entidad que cursó el pago."}, {"id": "prc_registro_ante_el_bcra", "type": "PROCESS", "label": "Registro ante el BCRA", "tokens_matcheados": 1, "resumen_propiedades": "Procedimiento administrativo mediante el cual el cambio de entidad nominada responsable queda formalizado y efectivo."}, {"id": "con_registro_aduanero_pendiente", "type": "CONCEPT", "label": "Registro aduanero pendiente", "tokens_matcheados": 1, "resumen_propiedades": "Situación de importaciones de bienes que requieren acceso al mercado de cambios sin contar aún con la oficialización del despacho de importación."}, {"id": "prc_registro_de_certificaciones", "type": "PROCESS", "label": "Registro de certificaciones", "tokens_matcheados": 1, "resumen_propiedades": "Proceso de documentación de certificaciones emitidas, anuladas y otros movimientos imputados al despacho."}, {"id": "con_registro_aduanero_de_ingreso", "type": "CONCEPT", "label": "Registro aduanero de ingreso", "tokens_matcheados": 1, "resumen_propiedades": "Documento o registro oficial emitido por aduanas que registra despachos de importación y sus características."}, {"id": "prc_registro_de_ingreso_aduanero", "type": "PROCESS", "label": "registro de ingreso aduanero", "tokens_matcheados": 1, "resumen_propiedades": "Procedimiento administrativo de entrada legal de bienes al país, requisito para acceso al mercado de cambios."}, {"id": "reg_registro_publico_de_comercio", "type": "REGULATOR", "label": "Registro Público de Comercio", "tokens_matcheados": 1, "resumen_propiedades": "Organismo ante el cual se inscribe la decisión de capitalización definitiva de aportes de capital."}, {"id": "req_registro_de_ingreso_aduanero", "type": "REQUIREMENT", "label": "Registro de ingreso aduanero", "tokens_matcheados": 1, "resumen_propiedades": "Procedimiento administrativo mediante el cual se documenta el ingreso de bienes de capital importados, constituyendo fecha clave para registro contable en bolet…"}, {"id": "prc_custodia_y_registro_de_titulos", "type": "PROCESS", "label": "Custodia y registro de títulos", "tokens_matcheados": 1, "resumen_propiedades": "Procedimiento por el cual BCRA, agentes de CNV y depósitos centrales mantienen a cargo la custodia de títulos de crédito."}]}
  ```
- paso 13 · `buscar_nodos` · input: `{"consulta": "régimen informativo contable mensual instrucciones generales", "limite": 10}` **[RE-EJECUTADO — almacenado truncado]**
  ```json
  {"consulta": "régimen informativo contable mensual instrucciones generales", "total_con_match": 81, "resultados": [{"id": "ins_regimen_informativo_contable_mensual", "type": "INSTRUMENT", "label": "Régimen Informativo Contable Mensual", "tokens_matcheados": 4, "resumen_propiedades": "Proceso de información periódica mensual obligatoria mediante el cual las entidades financieras reportan indicadores de negocio y componentes al BCRA."}, {"id": "rep_regimen_informativo_contable_mensual_sobre_capitales_minimos", "type": "REPORT_ITEM", "label": "Régimen Informativo Contable Mensual sobre Capitales Mínimos", "tokens_matcheados": 4, "resumen_propiedades": "Esquema informativo (R.I.-C.M.) que regula la presentación de datos sobre exigencia e integración de capitales mínimos."}, {"id": "rep_regimen_informativo_sepaimpo", "type": "REPORT_ITEM", "label": "Régimen Informativo SEPAIMPO", "tokens_matcheados": 2, "resumen_propiedades": "Sistema de reporte electrónico mediante el cual las entidades comunican al BCRA circunstancias que modifiquen obligaciones del importador con el exterior."}, {"id": "prc_regimen_informativo_para_supervision", "type": "PROCESS", "label": "Régimen informativo para Supervisión", "tokens_matcheados": 2, "resumen_propiedades": "Proceso de información supervisoria que establece los plazos de presentación para la base consolidada trimestral."}, {"id": "req_regimen_informativo_para_supervision", "type": "REQUIREMENT", "label": "Régimen Informativo para Supervisión", "tokens_matcheados": 2, "resumen_propiedades": "Régimen normativo que establece vencimientos y requisitos informativos para supervisión consolidada."}, {"id": "rep_codigo_de_concepto_del_regimen_informativo", "type": "REPORT_ITEM", "label": "Código de concepto del régimen informativo", "tokens_matcheados": 2, "resumen_propiedades": "Código identificador utilizado en el régimen informativo de operaciones de cambio para clasificar la transacción."}, {"id": "req_atraso_en_validacion_del_regimen_informativo", "type": "REQUIREMENT", "label": "Atraso en validación del régimen informativo", "tokens_matcheados": 2, "resumen_propiedades": "Obligación de validar puntualmente los apartados del régimen informativo de operaciones cambiarias, con tolerancia de máximo 4 días hábiles."}, {"id": "cla_regimen_informativo_de_operaciones_de_cambios_rioc", "type": "CLASSIFICATION", "label": "Régimen Informativo de Operaciones de Cambios (RIOC)", "tokens_matcheados": 2, "resumen_propiedades": "Sistema de registro informativo ante el BCRA mediante el cual se registran las operaciones comprendidas en el mecanismo de seguimiento de financiaciones."}, {"id": "req_suministro_de_informacion_a_sefyc_conforme_regimen_informativo", "type": "REQUIREMENT", "label": "Suministro de información a SEFyC conforme régimen informativo", "tokens_matcheados": 2, "resumen_propiedades": "Obligación de entregar información en tiempo y forma conforme al régimen informativo que establezca la materia."}, {"id": "prc_regimen_informativo_exigencia_e_integracion_de_capitales_minimos", "type": "PROCESS", "label": "Régimen informativo Exigencia e integración de capitales mínimos", "tokens_matcheados": 2, "resumen_propiedades": "Sistema de reporte que contiene nómina de partidas e instrucciones para determinación de exigencias registradas en códigos 70810000 y 70820000."}]}
  ```
- paso 14 · `ver_nodo` · input: `{"id": "ins_regimen_informativo_contable_mensual"}` [re-ejecutado; almacenado ya completo, verificado idéntico]
  → nodo ins_regimen_informativo_contable_mensual (Régimen Informativo Contable Mensual) — contenido íntegro abajo (§4)
- paso 15 · `ver_vecinos` · input: `{"id": "ins_regimen_informativo_contable_mensual", "direccion": "salientes"}` [re-ejecutado; almacenado ya completo, verificado idéntico]
  ```json
  {"id": "ins_regimen_informativo_contable_mensual", "label": "Régimen Informativo Contable Mensual", "n_salientes_total": 2, "n_entrantes_total": 1, "salientes": [{"relation": "establece_exigencias_de", "vecino_id": "req_incremento_de_exigencia_de_capitales_minimos", "vecino_label": "Incremento de exigencia de capitales mínimos", "provenances": [{"source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf", "location": "p. 4"}]}, {"relation": "define_umbral_para", "vecino_id": "req_comunicacion_de_cambios_negativos_en_clasificacion_de_deudores_dentro_de_45_dias", "vecino_label": "comunicación de cambios negativos en clasificación de deudores dentro de 45 días", "provenances": [{"source_doc": "TO_clasificacion_deudores_actual.pdf", "location": "p. 11"}]}], "salientes_truncado": false}
  ```
- **Respuesta final** (respondible: true)**:** «Según el Régimen Informativo Contable Mensual, los importes en el Régimen Informativo de Exigencia e Integración de Capitales Mínimos deben registrarse en miles de pesos, sin decimales.»
- **Citas:** [{"source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf", "location": "pp. 2-3"}]

### 4. Nodos abiertos con `ver_nodo` — contenido ÍNTEGRO (re-ejecución sobre kg.json congelado)

**prc_regimen_informativo_exigencia_e_integracion_de_capitales_minimos** (abierto en paso 3):
```json
{
 "id": "prc_regimen_informativo_exigencia_e_integracion_de_capitales_minimos",
 "type": "PROCESS",
 "label": "Régimen informativo Exigencia e integración de capitales mínimos",
 "properties": {
  "version": "A 6561",
  "description": "Sistema de reporte que contiene nómina de partidas e instrucciones para determinación de exigencias registradas en códigos 70810000 y 70820000.",
  "aliases": [
   "Régimen informativo Exigencia e integración de capitales mínimos"
  ],
  "source_to": "regimen_informativo_cm",
  "mention_count": 1
 },
 "provenances": [
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "p. 57"
  }
 ]
}
```

**req_miles_de_pesos** (abierto en paso 7):
```json
{
 "id": "req_miles_de_pesos",
 "type": "REQUIREMENT",
 "label": "Miles de pesos",
 "properties": {
  "version": "A 6561",
  "description": "Unidad de registro de importes, sin decimales.",
  "aliases": [
   "Miles de pesos"
  ],
  "source_to": "regimen_informativo_cm",
  "mention_count": 1
 },
 "provenances": [
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "pp. 2-3"
  }
 ]
}
```

**rep_codigo_70810000** (abierto en paso 10):
```json
{
 "id": "rep_codigo_70810000",
 "type": "REPORT_ITEM",
 "label": "Código 70810000",
 "properties": {
  "version": "A 6561",
  "description": "Partida de reporte para exigencia por riesgo de mercado calculada conforme a la metodología aplicable hasta 29.02.16 sobre Capitales mínimos.",
  "aliases": [
   "Código 70810000"
  ],
  "source_to": "regimen_informativo_cm",
  "mention_count": 1
 },
 "provenances": [
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "p. 57"
  }
 ]
}
```

**rep_codigo_70820000** (abierto en paso 11):
```json
{
 "id": "rep_codigo_70820000",
 "type": "REPORT_ITEM",
 "label": "Código 70820000",
 "properties": {
  "version": "A 6561",
  "description": "Partida de reporte para exigencia por riesgo de mercado calculada conforme a la metodología del Anexo a Comunicación A 5867.",
  "aliases": [
   "Código 70820000"
  ],
  "source_to": "regimen_informativo_cm",
  "mention_count": 1
 },
 "provenances": [
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "p. 57"
  }
 ]
}
```

**ins_regimen_informativo_contable_mensual** (abierto en paso 14):
```json
{
 "id": "ins_regimen_informativo_contable_mensual",
 "type": "INSTRUMENT",
 "label": "Régimen Informativo Contable Mensual",
 "properties": {
  "version": "A 6561",
  "description": "Proceso de información periódica mensual obligatoria mediante el cual las entidades financieras reportan indicadores de negocio y componentes al BCRA.",
  "aliases": [
   "Régimen Informativo Contable Mensual",
   "Régimen informativo contable mensual"
  ],
  "source_to": "regimen_informativo_cm",
  "mention_count": 6
 },
 "provenances": [
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "p. 4"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "p. 11"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "p. 25"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "p. 31"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "p. 39"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "p. 43"
  }
 ]
}
```

### 5. Pasaje(s) del PDF — secciones ground-truth (máx ~1.500 chars por pata)

**Punto 1.2 (Sección 1, Instrucciones generales) → Punto 1.2:**
[TO_regimen_informativo_contable_mensual_actual.pdf · Punto/Sección 1.2 (PDF pág 3) · localizacion: ok]
> 1.2. Los importes se registrarán en miles de pesos, sin decimales. A los fines del redondeo de las magnitudes se incrementarán los valores en una unidad cuando el primer dígito de las fracciones sea igual o mayor que 5, desechando estas últimas si resultan inferiores. Los importes en moneda extranjera se convertirán a pesos utilizando el tipo de cambio de re- ferencia publicado por el BCRA para el dólar estadounidense, previa aplicación del tipo de pase correspondiente para las otras monedas comunicado por la Mesa de Operaciones. Versión: 7a. COMUNICACIÓN “A” 7149 Vigencia: 30/10/2020 Página 1 REGIMEN INFORMATIVO CONTABLE MENSUAL B.C.R.A. 4. EXIGENCIA E INTEGRACIÓN DE CAPITALES MÍNIMOS (R.I.-C.M.) Sección 1. Instrucciones generales

**Cita textual GT (eval_set_v1, verbatim):** «Los importes se registrarán en miles de pesos, sin decimales. A los fines del redondeo de las magnitudes se incrementarán los valores en una unidad cuando el primer dígito de las fracciones sea igual o mayor que 5, desechando estas últimas si resultan inferiores.»

### 5b. Provenances VERBATIM (kg.json, lista completa) de los nodos citados en la respuesta final

**req_miles_de_pesos** (Miles de pesos) — ✓ provenance COINCIDE con una cita de la respuesta final · abierto con ver_nodo
```json
[
 {
  "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
  "location": "pp. 2-3"
 }
]
```

**ins_regimen_informativo_contable_mensual** (Régimen Informativo Contable Mensual) — abierto con ver_nodo
```json
[
 {
  "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
  "location": "p. 4"
 },
 {
  "source_doc": "TO_clasificacion_deudores_actual.pdf",
  "location": "p. 11"
 },
 {
  "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
  "location": "p. 25"
 },
 {
  "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
  "location": "p. 31"
 },
 {
  "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
  "location": "p. 39"
 },
 {
  "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
  "location": "p. 43"
 }
]
```

**prc_regimen_informativo_exigencia_e_integracion_de_capitales_minimos** (Régimen informativo Exigencia e integración de capitales mínimos) — abierto con ver_nodo
```json
[
 {
  "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
  "location": "p. 57"
 }
]
```

**rep_codigo_70810000** (Código 70810000) — abierto con ver_nodo
```json
[
 {
  "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
  "location": "p. 57"
 }
]
```

**rep_codigo_70820000** (Código 70820000) — abierto con ver_nodo
```json
[
 {
  "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
  "location": "p. 57"
 }
]
```

### 6. ADJUDICACIÓN (Agustina):
```
Adjudicación de la autora, 2026-07-15, asistida por revisión.

CASO SIN DEFECTO DEL SISTEMA (exoneración integral).

- pata / claim: claim secundario «Esta disposición proviene del Régimen Informativo
  Contable Mensual» (único claim negativo del caso)
- sintoma_capa1: —        causa_capa2: — (FALSO POSITIVO DEL JUEZ, sin par)
- primaria/secundaria: —
- evidencia (1 línea): Soportado (resumen de req_exigencia_de_integracion_de_capitales_minimos
  expuesto en paso 1: "Sección 4 del Régimen Informativo Contable Mensual") y correcto contra
  el PDF (el R.I. de Exigencia e Integración es el apartado 4 del RICM — encabezado verbatim
  del propio pasaje GT). La dimensión cita_documento_correcto=false es artefacto de metadatos
  (el ground_truth_secciones no nombra documento; el juez defaulteó a false sobre una cita al
  documento correcto) y NO participa del criterio de falla (verifier_pilot.scale_specs: solo
  claims falso/no_soportado).

- pata / claim: cita del agente (granularidad de página, cita_precision="pagina")
- sintoma_capa1: noise_sensitivity        causa_capa2: provenance_imprecisa
- primaria/secundaria: SECUNDARIA — lado grafo, no decisiva
- evidencia (1 línea): La provenance de req_miles_de_pesos es "pp. 2-3" (página sin punto;
  el contenido vive en el Punto 1.2, pág. 3), lo que limita la cita del agente a granularidad
  de página. Real, documentada, sin efecto en el veredicto.

Patrón de calibración: "exoneración integral + secundaria" — acierto = declarar el caso
sin defecto del sistema (ninguna primaria).
```

---

## Caso on/run_5/CQ-019

### 1. Pregunta (verbatim eval_set_v1) y patas (judge.step1.patas_de_la_pregunta)

> Al computar los activos para la exigencia de capital por riesgo de crédito, ¿qué previsión por incobrabilidad no se deduce, y cómo se vincula esa regla con la clasificación de deudores?

- Categoría: `multi_norma` · TOs fuente: capitales, clasificacion
- Ground-truth secciones: Capitales, Punto 2.3.1 · Clasificación, Puntos 6.5.1 y 7.2.1
- Pata 1: "Qué previsión por incobrabilidad no se deduce al computar los activos para la exigencia de capital por riesgo de crédito"
- Pata 2: "Cómo se vincula esa regla con la clasificación de deudores"

### 2. Claims con veredicto negativo del juez (verbatim)
- [no_soportado] CENTRAL — «La situación normal comprende a clientes que atienden puntualmente sus obligaciones o con atrasos que no superan 31 días.»
- [no_soportado] CENTRAL — «La previsión por incobrabilidad de la cartera en situación normal se computa como patrimonio neto complementario en lugar de deducirse del monto de activos expuestos.»
- [no_soportado] secundaria — «La excepción de no deducción para deudores en situación normal responde a que esos deudores presentan menor riesgo de incumplimiento.»
- cobertura_patas: [{"pata": "Qué previsión por incobrabilidad no se deduce al computar los activos para la exigencia de capital por riesgo de crédito", "cobertura": "cubierta"}, {"pata": "Cómo se vincula esa regla con la clasificación de deudores", "cobertura": "cubierta"}]
- (juez, otros campos verbatim) cita_documento_correcto: true · cita_precision: "punto" · abstencion: null

### 3. Trayectoria del agente (tool calls, rep 1) — outputs COMPLETOS por re-ejecución determinística (tool_calls_used: 16 · hit_tool_limit: True)

- paso 1 · `buscar_nodos` · input: `{"consulta": "exigencia capital riesgo crédito previsión incobrabilidad", "limite": 10}` **[RE-EJECUTADO — almacenado truncado]**
  ```json
  {"consulta": "exigencia capital riesgo crédito previsión incobrabilidad", "total_con_match": 646, "resultados": [{"id": "exigencia_de_capital_por_riesgo_de_credito", "type": "Restriccion", "label": "Exigencia de capital por riesgo de crédito", "tokens_matcheados": 4, "resumen_propiedades": "Se calcula aplicando la fórmula CRC = (k x 0,08 x APRC) + INC, donde k es un factor vinculado a la calificación asignada por la SEFYC, APRC son activos ponderad…"}, {"id": "exigencia_de_capital_minimo_por_riesgo_de_credito", "type": "Concepto", "label": "Exigencia de capital mínimo por riesgo de crédito", "tokens_matcheados": 4, "resumen_propiedades": "Exigencia regulatoria de capital calculada según lo previsto en la Sección 2."}, {"id": "metodologia_calculo_exigencia_capital_riesgo_credito", "type": "Restriccion", "label": "Metodología cálculo exigencia capital riesgo crédito", "tokens_matcheados": 4, "resumen_propiedades": "Metodología de cálculo de la exigencia de capital mínimo por riesgo de crédito con modificaciones."}, {"id": "exigencia_de_capital_por_riesgo_de_credito_en_derivados", "type": "Restriccion", "label": "Exigencia de capital por riesgo de crédito en derivados", "tokens_matcheados": 4, "resumen_propiedades": "RCD: exigencia en operaciones con derivados OTC o negociados en mercados regulados, con liquidación diferida."}, {"id": "exigencia_de_capital_por_riesgo_de_credito_de_contraparte", "type": "Restriccion", "label": "Exigencia de capital por riesgo de crédito de contraparte", "tokens_matcheados": 4, "resumen_propiedades": "Capital mínimo requerido para cubrir el riesgo de crédito de contraparte en operaciones con derivados."}, {"id": "disminucion_de_exigencia_de_capital_minimo_por_riesgo_de_cre", "type": "Restriccion", "label": "Disminución de exigencia de capital mínimo por riesgo de crédito", "tokens_matcheados": 4, "resumen_propiedades": "Facilidad que reduce la exigencia de capital mínimo vinculada al riesgo de crédito."}, {"id": "exigencia_de_capital_por_riesgo_de_credito_de_contraparte_ce", "type": "Restriccion", "label": "Exigencia de capital por riesgo de crédito de contraparte central", "tokens_matcheados": 4, "resumen_propiedades": "Requisito de capital mínimo para exposiciones con entidades de contraparte central según punto 4.3."}, {"id": "exigencia_capital_riesgo_vega", "type": "Restriccion", "label": "Exigencia capital riesgo vega", "tokens_matcheados": 3, "resumen_propiedades": "Para riesgo vega, la exigencia de capital se obtiene multiplicando la suma de coeficientes vega de todas las opciones sobre el mismo subyacente por un cambio de…"}, {"id": "exigencia_por_riesgo_de_credito", "type": "Restriccion", "label": "Exigencia por riesgo de crédito", "tokens_matcheados": 3, "resumen_propiedades": "Aplicación de ponderadores de riesgo de contraparte a conceptos de activos y partidas fuera de balance para determinar la exposición crediticia."}, {"id": "exigencia_capital_total_riesgo_vega", "type": "Restriccion", "label": "Exigencia capital total riesgo vega", "tokens_matcheados": 3, "resumen_propiedades": "La exigencia total de capital por riesgo vega es la suma del valor absoluto de las exigencias de capital individual calculadas para dicho riesgo."}]}
  ```
- paso 2 · `buscar_nodos` · input: `{"consulta": "activos computar capital riesgo crédito", "limite": 10}` **[RE-EJECUTADO — almacenado truncado]**
  ```json
  {"consulta": "activos computar capital riesgo crédito", "total_con_match": 708, "resultados": [{"id": "capital_minimo_por_riesgo_de_credito", "type": "Restriccion", "label": "Capital mínimo por riesgo de crédito", "tokens_matcheados": 3, "resumen_propiedades": "Requerimiento de capital para cubrir exposiciones y riesgo de crédito."}, {"id": "activos_ponderados_por_riesgo_de_credito", "type": "Concepto", "label": "Activos ponderados por riesgo de crédito", "tokens_matcheados": 3, "resumen_propiedades": "APRC determinados mediante suma de valores obtenidos aplicando: A x p + PFB x CCF x p + no DvP + (DVP + RCD + INC inversiones significativas) x 12,5"}, {"id": "cobertura_riesgo_credito_activos_garantia", "type": "Operacion", "label": "Cobertura riesgo crédito activos garantía", "tokens_matcheados": 3, "resumen_propiedades": "Operaciones cubiertas con activos admitidos como garantía para cobertura del riesgo de crédito."}, {"id": "exigencia_de_capital_por_riesgo_de_credito", "type": "Restriccion", "label": "Exigencia de capital por riesgo de crédito", "tokens_matcheados": 3, "resumen_propiedades": "Se calcula aplicando la fórmula CRC = (k x 0,08 x APRC) + INC, donde k es un factor vinculado a la calificación asignada por la SEFYC, APRC son activos ponderad…"}, {"id": "exigencia_de_capital_minimo_por_riesgo_de_credito", "type": "Concepto", "label": "Exigencia de capital mínimo por riesgo de crédito", "tokens_matcheados": 3, "resumen_propiedades": "Exigencia regulatoria de capital calculada según lo previsto en la Sección 2."}, {"id": "capital_minimo_por_riesgo_de_credito_de_contraparte", "type": "Restriccion", "label": "Capital mínimo por riesgo de crédito de contraparte", "tokens_matcheados": 3, "resumen_propiedades": "Requerimiento de capital para operaciones con derivados OTC o negociados en mercados regulados, equivalente a la suma del requerimiento de EAD vigente y el capi…"}, {"id": "metodologia_calculo_exigencia_capital_riesgo_credito", "type": "Restriccion", "label": "Metodología cálculo exigencia capital riesgo crédito", "tokens_matcheados": 3, "resumen_propiedades": "Metodología de cálculo de la exigencia de capital mínimo por riesgo de crédito con modificaciones."}, {"id": "exigencia_de_capital_por_riesgo_de_credito_en_derivados", "type": "Restriccion", "label": "Exigencia de capital por riesgo de crédito en derivados", "tokens_matcheados": 3, "resumen_propiedades": "RCD: exigencia en operaciones con derivados OTC o negociados en mercados regulados, con liquidación diferida."}, {"id": "exigencia_de_capital_por_riesgo_de_credito_de_contraparte", "type": "Restriccion", "label": "Exigencia de capital por riesgo de crédito de contraparte", "tokens_matcheados": 3, "resumen_propiedades": "Capital mínimo requerido para cubrir el riesgo de crédito de contraparte en operaciones con derivados."}, {"id": "aumento_de_integracion_de_capital_minimo_por_riesgo_de_credi", "type": "Restriccion", "label": "Aumento de integración de capital mínimo por riesgo de crédito", "tokens_matcheados": 3, "resumen_propiedades": "Facilidad que incrementa la integración de capital mínimo vinculada al riesgo de crédito."}]}
  ```
- paso 3 · `buscar_nodos` · input: `{"consulta": "previsión incobrabilidad deducción clasificación deudores", "limite": 10}` **[RE-EJECUTADO — almacenado truncado]**
  ```json
  {"consulta": "previsión incobrabilidad deducción clasificación deudores", "total_con_match": 143, "resultados": [{"id": "prevision_por_riesgo_de_incobrabilidad_deudores_normales", "type": "Restriccion", "label": "Previsión por riesgo de incobrabilidad deudores normales", "tokens_matcheados": 3, "resumen_propiedades": "Tratamiento especial de la previsión por riesgo de incobrabilidad para deudores en situación normal."}, {"id": "clasificacion_de_deudores", "type": "Operacion", "label": "Clasificación de deudores", "tokens_matcheados": 2, "resumen_propiedades": "Proceso mensual de clasificación de clientes considerando pautas objetivas vinculadas al cumplimiento de obligaciones y situación jurídica."}, {"id": "tarea_de_clasificacion_de_deudores", "type": "Operacion", "label": "Tarea de clasificación de deudores", "tokens_matcheados": 2, "resumen_propiedades": "Proceso de asignación de clasificación a clientes según su situación de endeudamiento."}, {"id": "to_sobre_clasificacion_de_deudores", "type": "Documento", "label": "TO sobre Clasificación de Deudores", "tokens_matcheados": 2, "resumen_propiedades": "Texto Ordenado que regula la clasificación de deudores, puntos 6.5.1 y 7.2.1."}, {"id": "clasificacion_de_deudores_de_cartera", "type": "Operacion", "label": "Clasificación de deudores de cartera", "tokens_matcheados": 2, "resumen_propiedades": "Operación de clasificación de deudores en la cartera de créditos para consumo o vivienda"}, {"id": "clasificacion_de_deudores_segun_mora", "type": "Operacion", "label": "Clasificación de deudores según mora", "tokens_matcheados": 2, "resumen_propiedades": "Clasificación de deudores en función de su situación de mora aplicando criterios de cartera de consumo o vivienda."}, {"id": "niveles_de_clasificacion_de_deudores", "type": "Restriccion", "label": "Niveles de clasificación de deudores", "tokens_matcheados": 2, "resumen_propiedades": "Agrupamiento de clientes en orden decreciente de calidad en razón directa al riesgo de incobrabilidad."}, {"id": "regimen_de_clasificacion_de_deudores", "type": "RegimenInformativo", "label": "Régimen de clasificación de deudores", "tokens_matcheados": 2, "resumen_propiedades": "Régimen de clasificación de deudores del BCRA que define conceptos excluidos y condiciones especiales."}, {"id": "clasificacion_de_deudores_comerciales", "type": "Restriccion", "label": "Clasificación de deudores comerciales", "tokens_matcheados": 2, "resumen_propiedades": "Norma específica para categorización de deudores vinculados al sector comercial."}, {"id": "clasificacion_obligatoria_de_deudores", "type": "Restriccion", "label": "Clasificación obligatoria de deudores", "tokens_matcheados": 2, "resumen_propiedades": "Los proveedores no financieros de crédito deben clasificar a sus deudores en función de la mora según criterios de cartera de consumo o vivienda, con recategori…"}]}
  ```
- paso 4 · `ver_nodo` · input: `{"id": "exigencia_de_capital_por_riesgo_de_credito"}` [re-ejecutado; almacenado ya completo, verificado idéntico]
  → nodo exigencia_de_capital_por_riesgo_de_credito (Exigencia de capital por riesgo de crédito) — contenido íntegro abajo (§4)
- paso 5 · `ver_nodo` · input: `{"id": "prevision_por_riesgo_de_incobrabilidad_deudores_normales"}` [re-ejecutado; almacenado ya completo, verificado idéntico]
  → nodo prevision_por_riesgo_de_incobrabilidad_deudores_normales (Previsión por riesgo de incobrabilidad deudores normales) — contenido íntegro abajo (§4)
- paso 6 · `ver_nodo` · input: `{"id": "activos_ponderados_por_riesgo_de_credito"}` [re-ejecutado; almacenado ya completo, verificado idéntico]
  → nodo activos_ponderados_por_riesgo_de_credito (Activos ponderados por riesgo de crédito) — contenido íntegro abajo (§4)
- paso 7 · `ver_vecinos` · input: `{"id": "exigencia_de_capital_por_riesgo_de_credito", "direccion": "salientes"}` **[RE-EJECUTADO — almacenado truncado]**
  ```json
  {"id": "exigencia_de_capital_por_riesgo_de_credito", "label": "Exigencia de capital por riesgo de crédito", "n_salientes_total": 7, "n_entrantes_total": 0, "salientes": [{"relation": "incorpora", "vecino_id": "factor_k_segun_calificacion_de_la_sefyc", "vecino_label": "Factor k según calificación de la SEFYC", "provenances": [{"source_doc": "TO_capitales_minimos_actual.pdf", "location": "Punto 2.1 — Exigencia."}]}, {"relation": "incorpora", "vecino_id": "activos_ponderados_por_riesgo_de_credito", "vecino_label": "Activos ponderados por riesgo de crédito", "provenances": [{"source_doc": "TO_capitales_minimos_actual.pdf", "location": "Punto 2.1 — Exigencia."}]}, {"relation": "requiere", "vecino_id": "datos_computados_por_saldos_fin_periodo", "vecino_label": "Datos computados por saldos fin período", "provenances": [{"source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf", "location": "Punto 4 — EXIGENCIA E INTEGRACIÓN DE CAPITALES MÍNIMOS (R.I.-C.M.) + Punto 3.1 — Normas de procedimiento."}]}, {"relation": "depende_de", "vecino_id": "activos_ponderados_por_riesgo_de_credito", "vecino_label": "Activos ponderados por riesgo de crédito", "provenances": [{"source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf", "location": "Punto 4 — EXIGENCIA E INTEGRACIÓN DE CAPITALES MÍNIMOS (R.I.-C.M.) + Punto 3.1 — Normas de procedimiento."}]}, {"relation": "depende_de", "vecino_id": "factor_vinculado_a_calificacion_de_entidad", "vecino_label": "Factor vinculado a calificación de entidad", "provenances": [{"source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf", "location": "Punto 4 — EXIGENCIA E INTEGRACIÓN DE CAPITALES MÍNIMOS (R.I.-C.M.) + Punto 3.1 — Normas de procedimiento."}]}, {"relation": "utiliza", "vecino_id": "ead_exposure_at_default", "vecino_label": "EAD (Exposure at Default)", "provenances": [{"source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf", "location": "Punto 4 — EXIGENCIA E INTEGRACIÓN DE CAPITALES MÍNIMOS (R.I.-C.M.)"}]}, {"relation": "utiliza", "vecino_id": "ponderador_de_riesgo", "vecino_label": "Ponderador de riesgo", "provenances": [{"source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf", "location": "Punto 4 — EXIGENCIA E INTEGRACIÓN DE CAPITALES MÍNIMOS (R.I.-C.M.)"}]}], "salientes_truncado": false}
  ```
- paso 8 · `ver_vecinos` · input: `{"id": "prevision_por_riesgo_de_incobrabilidad_deudores_normales", "direccion": "ambas"}` [re-ejecutado; almacenado ya completo, verificado idéntico]
  ```json
  {"id": "prevision_por_riesgo_de_incobrabilidad_deudores_normales", "label": "Previsión por riesgo de incobrabilidad deudores normales", "n_salientes_total": 0, "n_entrantes_total": 0, "salientes": [], "salientes_truncado": false, "entrantes": [], "entrantes_truncado": false}
  ```
- paso 9 · `ver_vecinos` · input: `{"id": "activos_ponderados_por_riesgo_de_credito", "direccion": "salientes"}` **[RE-EJECUTADO — almacenado truncado]**
  ```json
  {"id": "activos_ponderados_por_riesgo_de_credito", "label": "Activos ponderados por riesgo de crédito", "n_salientes_total": 4, "n_entrantes_total": 5, "salientes": [{"relation": "comprende", "vecino_id": "exposiciones_crediticias", "vecino_label": "Exposiciones crediticias", "provenances": [{"source_doc": "TO_capitales_minimos_actual.pdf", "location": "Punto 2.1 — Exigencia."}]}, {"relation": "comprende", "vecino_id": "partidas_fuera_de_balance", "vecino_label": "Partidas fuera de balance", "provenances": [{"source_doc": "TO_capitales_minimos_actual.pdf", "location": "Punto 2.1 — Exigencia."}]}, {"relation": "comprende", "vecino_id": "operaciones_sin_entrega_contra_pago", "vecino_label": "Operaciones sin entrega contra pago", "provenances": [{"source_doc": "TO_capitales_minimos_actual.pdf", "location": "Punto 2.1 — Exigencia."}]}, {"relation": "comprende", "vecino_id": "activos_computables_exposiciones_saldos_deuda", "vecino_label": "Activos computables exposiciones saldos deuda", "provenances": [{"source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf", "location": "Punto 4 — EXIGENCIA E INTEGRACIÓN DE CAPITALES MÍNIMOS (R.I.-C.M.) + Punto 3.1 — Normas de procedimiento."}]}], "salientes_truncado": false}
  ```
- paso 10 · `buscar_nodos` · input: `{"consulta": "previsión deducción activos computables", "limite": 10}` **[RE-EJECUTADO — almacenado truncado]**
  ```json
  {"consulta": "previsión deducción activos computables", "total_con_match": 170, "resultados": [{"id": "deduccion_activos_intangibles", "type": "Restriccion", "label": "Deducción activos intangibles", "tokens_matcheados": 2, "resumen_propiedades": "Activos intangibles netos de depreciación acumulada, incluyendo llave de negocio en valuaciones de inversiones significativas."}, {"id": "activos_computables_exposiciones_saldos_deuda", "type": "Concepto", "label": "Activos computables exposiciones saldos deuda", "tokens_matcheados": 2, "resumen_propiedades": "Saldos de deuda a considerarse conforme disposiciones contenidas en Secciones 2 a 5 y punto 11.5 de normas sobre Capitales mínimos, incluyendo ajustes NIIF."}, {"id": "deduccion_de_previsiones_en_activos_ponderados", "type": "Restriccion", "label": "Deducción de previsiones en activos ponderados", "tokens_matcheados": 2, "resumen_propiedades": "Entidades originantes pueden deducir de posiciones ponderadas al 1250% tanto previsiones específicas como descuentos no reembolsables en precio de adquisición d…"}, {"id": "deduccion_de_activos_y_conceptos_por_requerimiento_sefyc", "type": "Restriccion", "label": "Deducción de activos y conceptos por requerimiento SEFyC", "tokens_matcheados": 2, "resumen_propiedades": "Las entidades financieras deben deducir importes de activos u otros conceptos cuando las registraciones contables no reflejen la realidad económica y jurídica d…"}, {"id": "activos_fijos", "type": "Concepto", "label": "Activos fijos", "tokens_matcheados": 1, "resumen_propiedades": ""}, {"id": "otros_activos", "type": "InstrumentoFinanciero", "label": "Otros activos", "tokens_matcheados": 1, "resumen_propiedades": "Exposición clasificada con factor de ponderación 75%."}, {"id": "activos_rotativos", "type": "Concepto", "label": "Activos rotativos", "tokens_matcheados": 1, "resumen_propiedades": "Activos de tipo rotativo como tarjetas de crédito, facturas y otras exposiciones cancelables en un solo pago."}, {"id": "canasta_de_activos", "type": "Concepto", "label": "Canasta de activos", "tokens_matcheados": 1, "resumen_propiedades": "Conjunto de múltiples activos utilizados conjuntamente como garantía de una operación."}, {"id": "activos_en_garantia", "type": "Concepto", "label": "Activos en garantía", "tokens_matcheados": 1, "resumen_propiedades": "Bienes que la CCP puede utilizar en caso de incumplimiento del miembro compensador o cliente"}, {"id": "activos_intangibles", "type": "Concepto", "label": "Activos intangibles", "tokens_matcheados": 1, "resumen_propiedades": "Activos intangibles deducibles del Capital Ordinario de Nivel 1."}]}
  ```
- paso 11 · `buscar_nodos` · input: `{"consulta": "activos brutos neto previsiones exposiciones crediticias", "limite": 10}` **[RE-EJECUTADO — almacenado truncado]**
  ```json
  {"consulta": "activos brutos neto previsiones exposiciones crediticias", "total_con_match": 268, "resultados": [{"id": "exposiciones_crediticias", "type": "Concepto", "label": "Exposiciones crediticias", "tokens_matcheados": 2, "resumen_propiedades": "Activos computables y exposiciones incluidas en el cálculo de activos ponderados por riesgo de crédito."}, {"id": "computo_neto_de_previsiones_por_riesgo", "type": "Restriccion", "label": "Cómputo neto de previsiones por riesgo", "tokens_matcheados": 2, "resumen_propiedades": "Los conceptos se computarán netos de previsiones por riesgos de incobrabilidad, depreciaciones y amortizaciones acumuladas."}, {"id": "activos_computables_exposiciones_saldos_deuda", "type": "Concepto", "label": "Activos computables exposiciones saldos deuda", "tokens_matcheados": 2, "resumen_propiedades": "Saldos de deuda a considerarse conforme disposiciones contenidas en Secciones 2 a 5 y punto 11.5 de normas sobre Capitales mínimos, incluyendo ajustes NIIF."}, {"id": "deduccion_de_previsiones_en_activos_ponderados", "type": "Restriccion", "label": "Deducción de previsiones en activos ponderados", "tokens_matcheados": 2, "resumen_propiedades": "Entidades originantes pueden deducir de posiciones ponderadas al 1250% tanto previsiones específicas como descuentos no reembolsables en precio de adquisición d…"}, {"id": "exclusion_de_exposiciones_titulizadas_del_calculo_de_activos", "type": "Restriccion", "label": "Exclusión de exposiciones titulizadas del cálculo de activos ponderados", "tokens_matcheados": 2, "resumen_propiedades": "La entidad originante podrá excluir exposiciones de titulización tradicional del cálculo de activos ponderados por riesgo solo si se cumplen requisitos operativ…"}, {"id": "activos_fijos", "type": "Concepto", "label": "Activos fijos", "tokens_matcheados": 1, "resumen_propiedades": ""}, {"id": "otros_activos", "type": "InstrumentoFinanciero", "label": "Otros activos", "tokens_matcheados": 1, "resumen_propiedades": "Exposición clasificada con factor de ponderación 75%."}, {"id": "ingresos_brutos", "type": "Concepto", "label": "Ingresos brutos", "tokens_matcheados": 1, "resumen_propiedades": "Base de cálculo BI determinada como valor absoluto de la suma de componentes: intereses/arrendamientos/dividendos, servicios, financiero y resultado monetario t…"}, {"id": "patrimonio_neto", "type": "Concepto", "label": "Patrimonio Neto", "tokens_matcheados": 1, "resumen_propiedades": "Rubro 400000 del balance, base para determinar el Capital Ordinario de Nivel 1."}, {"id": "activos_rotativos", "type": "Concepto", "label": "Activos rotativos", "tokens_matcheados": 1, "resumen_propiedades": "Activos de tipo rotativo como tarjetas de crédito, facturas y otras exposiciones cancelables en un solo pago."}]}
  ```
- paso 12 · `ver_nodo` · input: `{"id": "computo_neto_de_previsiones_por_riesgo"}` [re-ejecutado; almacenado ya completo, verificado idéntico]
  → nodo computo_neto_de_previsiones_por_riesgo (Cómputo neto de previsiones por riesgo) — contenido íntegro abajo (§4)
- paso 13 · `ver_nodo` · input: `{"id": "deduccion_de_previsiones_en_activos_ponderados"}` [re-ejecutado; almacenado ya completo, verificado idéntico]
  → nodo deduccion_de_previsiones_en_activos_ponderados (Deducción de previsiones en activos ponderados) — contenido íntegro abajo (§4)
- paso 14 · `ver_nodo` · input: `{"id": "exposiciones_crediticias"}` [re-ejecutado; almacenado ya completo, verificado idéntico]
  → nodo exposiciones_crediticias (Exposiciones crediticias) — contenido íntegro abajo (§4)
- paso 15 · `ver_vecinos` · input: `{"id": "computo_neto_de_previsiones_por_riesgo", "direccion": "ambas"}` [re-ejecutado; almacenado ya completo, verificado idéntico]
  ```json
  {"id": "computo_neto_de_previsiones_por_riesgo", "label": "Cómputo neto de previsiones por riesgo", "n_salientes_total": 1, "n_entrantes_total": 0, "salientes": [{"relation": "aplica_a", "vecino_id": "conceptos_comprendidos", "vecino_label": "Conceptos comprendidos", "provenances": [{"source_doc": "TO_capitales_minimos_actual.pdf", "location": "Punto 2.3 — Cómputo de los conceptos comprendidos."}]}], "salientes_truncado": false, "entrantes": [], "entrantes_truncado": false}
  ```
- paso 16 · `buscar_nodos` · input: `{"consulta": "previsión genérica normal no se deduce", "limite": 10}` **[RE-EJECUTADO — almacenado truncado]**
  ```json
  {"consulta": "previsión genérica normal no se deduce", "total_con_match": 222, "resultados": [{"id": "pago_no_se_realiza_anterior_a_vencimiento", "type": "Restriccion", "label": "Pago no se realiza anterior a vencimiento", "tokens_matcheados": 2, "resumen_propiedades": "El pago no se realiza con anterioridad a la fecha de vencimiento de la obligación con el exterior."}, {"id": "prevision_por_cartera_en_situacion_normal", "type": "Concepto", "label": "Previsión por cartera en situación normal", "tokens_matcheados": 2, "resumen_propiedades": "Previsión por riesgo de incobrabilidad de la cartera en situación normal computada como patrimonio neto complementario."}, {"id": "rotacion_y_sustitucion_no_se_considera_gestion_activa", "type": "Excepcion", "label": "Rotación y sustitución no se considera gestión activa", "tokens_matcheados": 2, "resumen_propiedades": "Incorporación de créditos en períodos de rotación o sustitución por incumplimiento de cláusulas contractuales no se considera gestión activa de cartera."}, {"id": "exclusion_de_prevision_para_deudores_clasificados_en_situaci", "type": "Restriccion", "label": "Exclusión de previsión para deudores clasificados en situación normal", "tokens_matcheados": 2, "resumen_propiedades": "No se deducirá el 100% de la previsión por riesgo de incobrabilidad de deudores clasificados en situación normal."}, {"id": "no_residente", "type": "Concepto", "label": "No residente", "tokens_matcheados": 1, "resumen_propiedades": "Persona o entidad sin residencia en territorio argentino que realiza operaciones de inversión y repatriación."}, {"id": "situacion_normal", "type": "Restriccion", "label": "Situación normal", "tokens_matcheados": 1, "resumen_propiedades": "Clientes que atienden puntualmente sus obligaciones o con atrasos que no superan 31 días. Adelantos transitorios en cuenta corriente se consideran de cumplimien…"}, {"id": "ccp_no_calificada", "type": "Concepto", "label": "CCP no calificada", "tokens_matcheados": 1, "resumen_propiedades": "Entidad de contraparte central que no cumple con requisitos para ser considerada QCCP."}, {"id": "decreto_n_512_21", "type": "Documento", "label": "Decreto Nº 512/21", "tokens_matcheados": 1, "resumen_propiedades": "Decreto que establece el régimen de Créditos a Tasa Cero 2021."}, {"id": "operaciones_no_dvp", "type": "Operacion", "label": "Operaciones no DvP", "tokens_matcheados": 1, "resumen_propiedades": "Operaciones en las que se entrega efectivo sin recibir contrapartida o se entregan efectos sin pago de efectivo."}, {"id": "decreto_n_260_2020", "type": "Documento", "label": "Decreto Nº 260/2020", "tokens_matcheados": 1, "resumen_propiedades": "Decreto que declara la emergencia sanitaria por Coronavirus (COVID-19)."}]}
  ```
- **Respuesta final** (respondible: true)**:** «Al computar los activos para la exigencia de capital por riesgo de crédito, la previsión por riesgo de incobrabilidad de deudores clasificados en situación normal no se deduce. Específicamente, el 100% de la previsión por riesgo de incobrabilidad correspondiente a deudores en situación normal se excluye del cómputo neto. Esta regla se vincula directamente con la clasificación de deudores: la situación normal comprende a clientes que atienden puntualmente sus obligaciones o con atrasos que no superan 31 días. En contraste, los conceptos en general se computarán netos de previsiones por riesgos de incobrabilidad, pero esta excepción aplicable a la cartera en situación normal responde a que esos deudores presentan menor riesgo de incumplimiento, por lo que su previsión se computa como patrimonio neto complementario en lugar de deducirse del monto de activos expuestos.»
- **Citas:** [{"source_doc": "TO_capitales_minimos_actual.pdf", "location": "Punto 2.3 — Cómputo de los conceptos comprendidos."}]

### 4. Nodos abiertos con `ver_nodo` — contenido ÍNTEGRO (re-ejecución sobre kg.json congelado)

**exigencia_de_capital_por_riesgo_de_credito** (abierto en paso 4):
```json
{
 "id": "exigencia_de_capital_por_riesgo_de_credito",
 "type": "Restriccion",
 "label": "Exigencia de capital por riesgo de crédito",
 "properties": {
  "description": "Se calcula aplicando la fórmula CRC = (k x 0,08 x APRC) + INC, donde k es un factor vinculado a la calificación asignada por la SEFYC, APRC son activos ponderados por riesgo de crédito, e INC es inversiones no computables."
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Punto 2.1 — Exigencia."
  }
 ]
}
```

**prevision_por_riesgo_de_incobrabilidad_deudores_normales** (abierto en paso 5):
```json
{
 "id": "prevision_por_riesgo_de_incobrabilidad_deudores_normales",
 "type": "Restriccion",
 "label": "Previsión por riesgo de incobrabilidad deudores normales",
 "properties": {
  "description": "Tratamiento especial de la previsión por riesgo de incobrabilidad para deudores en situación normal."
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Punto 8.6 — “A” 414 + Punto 9.2 + Punto 12.1 + Punto 8028 + Punto 12.3 — “A” 8364  5. (parte 5/6)"
  }
 ]
}
```

**activos_ponderados_por_riesgo_de_credito** (abierto en paso 6):
```json
{
 "id": "activos_ponderados_por_riesgo_de_credito",
 "type": "Concepto",
 "label": "Activos ponderados por riesgo de crédito",
 "properties": {
  "description": "APRC determinados mediante suma de valores obtenidos aplicando: A x p + PFB x CCF x p + no DvP + (DVP + RCD + INC inversiones significativas) x 12,5"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Punto 2.1 — Exigencia."
  }
 ]
}
```

**computo_neto_de_previsiones_por_riesgo** (abierto en paso 12):
```json
{
 "id": "computo_neto_de_previsiones_por_riesgo",
 "type": "Restriccion",
 "label": "Cómputo neto de previsiones por riesgo",
 "properties": {
  "description": "Los conceptos se computarán netos de previsiones por riesgos de incobrabilidad, depreciaciones y amortizaciones acumuladas."
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Punto 2.3 — Cómputo de los conceptos comprendidos."
  }
 ]
}
```

**deduccion_de_previsiones_en_activos_ponderados** (abierto en paso 13):
```json
{
 "id": "deduccion_de_previsiones_en_activos_ponderados",
 "type": "Restriccion",
 "label": "Deducción de previsiones en activos ponderados",
 "properties": {
  "description": "Entidades originantes pueden deducir de posiciones ponderadas al 1250% tanto previsiones específicas como descuentos no reembolsables en precio de adquisición de activos subyacentes."
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Punto 3.1 — Tratamiento de las titulizaciones. (parte 4/15)"
  }
 ]
}
```

**exposiciones_crediticias** (abierto en paso 14):
```json
{
 "id": "exposiciones_crediticias",
 "type": "Concepto",
 "label": "Exposiciones crediticias",
 "properties": {
  "description": "Activos computables y exposiciones incluidas en el cálculo de activos ponderados por riesgo de crédito."
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Punto 2.1 — Exigencia."
  }
 ]
}
```

### 5. Pasaje(s) del PDF — secciones ground-truth (máx ~1.500 chars por pata)

**Capitales, Punto 2.3.1 → Punto 2.3.1:**
[TO_capitales_minimos_actual.pdf · Punto/Sección 2.3.1 (PDF pág 10) · localizacion: ok]
> 2.3.1. Bases individual y consolidada mensual. Los conceptos comprendidos se computarán sobre la base de los saldos al último día de cada mes (capitales, intereses, primas, actualizaciones –por el Coeficiente de Estabilización de Referencia CER– y diferencias de cotización, según corresponda, netos de las previsiones por riesgos de incobrabilidad –incluyendo, de corresponder, las previsiones contabilizadas en el pasivo – y desvalorización y de las depreciaci ones y amortizaciones acumuladas que les sean atribuibles y demás cuentas regulariz adoras, sin deducir el 100% del importe de la previsión por riesgo de incobrabilidad correspondiente a la cartera de deudores clasificados “en situación normal” –puntos 6.5.1. y 7.2.1. del TO sobre Clasificaci ón de Deudores– y a las financiaciones que se encuentran cubiertas con garantías preferidas A). 2.3.2. Base consolidada trimestral. Se considerarán los saldos al cierre del trimestre, aplicando en los demás aspectos las correspondientes disposiciones establecidas. 2.4. Requisitos de debida diligencia. Las entidades financieras del grupo 1 deberán llevar a cabo un proceso de debida diligencia –al momento del otorgamiento del crédito y con frecuencia mínima anual– a fin de que puedan con- tar con una adecuada comprensión del perfil de riesgo y las características de sus contrapartes. El grado de sofisticación de las evaluaciones de deb

**Clasificación, Puntos 6.5.1 y 7.2.1 → Punto 6.5.1:**
[TO_clasificacion_deudores_actual.pdf · Punto/Sección 6.5.1 (PDF pág 20) · localizacion: manual — pdf_locate falló porque la extracción parte el marcador ('6. 5.1.'); pasaje extraído determinísticamente de la pág 20]
> 6. 5.1. En situación normal. E l análisis del flu jo de fondos del cliente demuestra que es capaz de atender adecuada- mente todos sus compromisos financieros. E ntre los indicadores que pueden reflejar esta situación se destacan que el cliente: 6. 5.1.1. presente una situación financiera líquida, con bajo nivel y adecuada estructura de endeudamiento en relación con su capacidad de ganancia, y muestre una al- ta capacidad de pago de las deudas (capital e intereses) en las condiciones pac- tadas generando fondos -medido a través del análisis de su flujo- en grado acep- table. El flujo de fondos no es susceptible de variaciones significativas ante m o- dificaciones importantes en el comportamiento de las variables tanto propias como vinculadas a su sector de actividad. E n el análisis que se lleve a cabo deberá tenerse en cuenta, de corresponder, la eventual incidencia que en su capacidad de pago pueda tener la situación en la que se encuentran los demás integrantes del grupo de contrapartes conectadas al cual pertenece. 6. 5.1.2. cumpla regularmente con el pago de sus obligaciones, aun cuando incurra en atrasos de hasta 31 días, entendiéndose que ello sucede cuando el cliente can- cela las obligaciones sin recurrir a nueva financiación directa o indirecta de la entidad. 6. 5.1.3. cuente con una dirección calificada y honesta, muy profesional y técnica, con adecuados sistemas de

**Clasificación, Puntos 6.5.1 y 7.2.1 → Punto 7.2.1:**
[TO_clasificacion_deudores_actual.pdf · Punto/Sección 7.2.1 (PDF pág 35) · localizacion: ok]
> 7.2.1. Situación normal. Comprende los clientes que atienden en forma puntual el pago de sus obligaciones o con atrasos que no superan los 31 días. Los adelantos transitorios en cuenta corriente se considerarán de cumplimiento normal hasta los 61 días contados desde su otorgamiento. A los fines de establecer los días de atraso, en el caso de las financiaciones instrumenta- das mediante tarjetas de crédito, se considerarán los que resulten luego de imputar el pago mínimo exigido en cada liquidación a cancelar la deuda en orden decreciente de an- tigüedad. Los deudores que hayan accedido a refinanciaciones de deudas encontrándose clasifica- dos en niveles inferiores, sólo podrán incluirse en esta categoría en la medida en que se hayan observado las pautas establecidas para cada uno de los correspondientes niveles y, además, que el resto de sus deudas reúnan las condiciones para que el cliente pueda ser recategorizado en este nivel. Los deudores que hayan refinanciado sus deudas, aun no habiendo incurrido en atrasos en el pago de sus servicios, podrán permanecer en esta categoría, cuando hayan accedi- do, como máximo, a dos refinanciaciones, en el término de 12 meses, contados desde la última refinanciación otorgada. A esos efectos, no se considerará refinanciación la asistencia que se otorgue a los deu- dores clasificados en esta categoría siempre que implique mayor

**Cita textual GT (eval_set_v1, verbatim):** «[Capitales 2.3.1] [...] netos de las previsiones por riesgos de incobrabilidad [...] sin deducir el 100% del importe de la previsión por riesgo de incobrabilidad correspondiente a la cartera de deudores clasificados 'en situación normal' –puntos 6.5.1. y 7.2.1. del TO sobre Clasificación de Deudores– y a las financiaciones que se encuentran cubiertas con garantías preferidas A).»

### 5b. Provenances VERBATIM (kg.json, lista completa) de los nodos citados en la respuesta final

**exigencia_de_capital_por_riesgo_de_credito** (Exigencia de capital por riesgo de crédito) — abierto con ver_nodo
```json
[
 {
  "source_doc": "TO_capitales_minimos_actual.pdf",
  "location": "Punto 2.1 — Exigencia."
 }
]
```

**activos_ponderados_por_riesgo_de_credito** (Activos ponderados por riesgo de crédito) — abierto con ver_nodo
```json
[
 {
  "source_doc": "TO_capitales_minimos_actual.pdf",
  "location": "Punto 2.1 — Exigencia."
 }
]
```

**exposiciones_crediticias** (Exposiciones crediticias) — abierto con ver_nodo
```json
[
 {
  "source_doc": "TO_capitales_minimos_actual.pdf",
  "location": "Punto 2.1 — Exigencia."
 }
]
```

**conceptos_comprendidos** (Conceptos comprendidos) — ✓ provenance COINCIDE con una cita de la respuesta final · expuesto en la trayectoria (buscar_nodos/ver_vecinos), no abierto
```json
[
 {
  "source_doc": "TO_capitales_minimos_actual.pdf",
  "location": "Punto 2.3 — Cómputo de los conceptos comprendidos."
 }
]
```

**computo_neto_de_previsiones_por_riesgo** (Cómputo neto de previsiones por riesgo) — ✓ provenance COINCIDE con una cita de la respuesta final · abierto con ver_nodo
```json
[
 {
  "source_doc": "TO_capitales_minimos_actual.pdf",
  "location": "Punto 2.3 — Cómputo de los conceptos comprendidos."
 }
]
```

**exclusion_de_prevision_para_deudores_clasificados_en_situaci** (Exclusión de previsión para deudores clasificados en situación normal) — ✓ provenance COINCIDE con una cita de la respuesta final · expuesto en la trayectoria (buscar_nodos/ver_vecinos), no abierto
```json
[
 {
  "source_doc": "TO_capitales_minimos_actual.pdf",
  "location": "Punto 2.3 — Cómputo de los conceptos comprendidos."
 }
]
```

**to_sobre_clasificacion_de_deudores** (TO sobre Clasificación de Deudores) — ✓ provenance COINCIDE con una cita de la respuesta final · expuesto en la trayectoria (buscar_nodos/ver_vecinos), no abierto
```json
[
 {
  "source_doc": "TO_capitales_minimos_actual.pdf",
  "location": "Punto 2.3 — Cómputo de los conceptos comprendidos."
 }
]
```

**deduccion_de_previsiones_en_activos_ponderados** (Deducción de previsiones en activos ponderados) — abierto con ver_nodo
```json
[
 {
  "source_doc": "TO_capitales_minimos_actual.pdf",
  "location": "Punto 3.1 — Tratamiento de las titulizaciones. (parte 4/15)"
 }
]
```

**prevision_por_riesgo_de_incobrabilidad_deudores_normales** (Previsión por riesgo de incobrabilidad deudores normales) — abierto con ver_nodo
```json
[
 {
  "source_doc": "TO_capitales_minimos_actual.pdf",
  "location": "Punto 8.6 — “A” 414 + Punto 9.2 + Punto 12.1 + Punto 8028 + Punto 12.3 — “A” 8364  5. (parte 5/6)"
 }
]
```

### 6. ADJUDICACIÓN (Agustina):
```
Adjudicación de la autora, 2026-07-15, asistida por revisión.

- pata / claim: claims centrales «situación normal ≤31 días» y «se computa como
  patrimonio neto complementario»
- sintoma_capa1: —        causa_capa2: — (FALSOS POSITIVOS DEL JUEZ, sin par)
- primaria/secundaria: —
- evidencia (1 línea): Ambos EXPUESTOS en el paso 16 (resúmenes de situacion_normal y
  prevision_por_cartera_en_situacion_normal, re-ejecución determinística 2026-07-15) y
  correctos contra el PDF (Clasificación 7.2.1 verbatim; Capitales 8.2.3.3/8.4.1.1).
  Mecanismo del FP: el juez verifica contra ground_truth_secciones (2.3.1/6.5.1/7.2.1)
  y el PNc cae fuera de ese marco aunque sea corpus verdadero — mismo patrón que la
  fórmula 70100000 en run_3/CQ-020.

- pata / claim: la racionalización «responde a que esos deudores presentan menor riesgo
  de incumplimiento»
- sintoma_capa1: faithfulness        causa_capa2: alucinacion_agente (modo b)
- primaria/secundaria: SECUNDARIA
- evidencia (1 línea): Ni los nodos expuestos ni el PDF dan esa justificación (barrido
  2026-07-15; el 2.3.1 establece la regla sin fundamentarla).

SIN PRIMARIA. Nota: la hipótesis estructural del inventario (familia B) queda refutada
para este caso — el dato-puente (la referencia cruzada a 6.5.1/7.2.1) existe como
portador textual (to_sobre_clasificacion_de_deudores) y estuvo expuesto en la
trayectoria; los extremos sin arista no impidieron el vínculo.

Patrón de calibración: "exoneración de centrales + secundaria lado agente" — acierto =
ninguna primaria emitida.
```

---

## Caso off/run_1/CQ-018

### 1. Pregunta (verbatim eval_set_v1) y patas (judge.step1.patas_de_la_pregunta)

> Los proveedores no financieros de crédito y las empresas no financieras emisoras de tarjetas, ¿deben cumplir con Protección al Usuario y, además, clasificar a sus deudores? ¿Bajo qué criterio clasifican?

- Categoría: `multi_norma` · TOs fuente: proteccion, clasificacion
- Ground-truth secciones: Protección, Puntos 1.1.2.4 y 1.1.2.5 · Clasificación, Punto 10.1
- Pata 1: "Si los proveedores no financieros de crédito deben cumplir con Protección al Usuario"
- Pata 2: "Si las empresas no financieras emisoras de tarjetas deben cumplir con Protección al Usuario"
- Pata 3: "Si deben clasificar a sus deudores"
- Pata 4: "Bajo qué criterio clasifican a sus deudores"

### 2. Claims con veredicto negativo del juez (verbatim)
- [no_soportado] secundaria — «Los proveedores no financieros de crédito están obligados a designar un Directivo Responsable de Protección de los Usuarios de Servicios Financieros.»
- [no_soportado] secundaria — «Las empresas no financieras emisoras de tarjetas de crédito y/o compra están obligadas a designar un Directivo Responsable de Protección de los Usuarios de Servicios Financieros.»
- [no_soportado] CENTRAL — «La categoría 'Situación normal' corresponde a clientes que demuestran capacidad de atender adecuadamente todos sus compromisos financieros a través del análisis de flujo de fondos.»
- [no_soportado] CENTRAL — «La categoría 'Riesgo bajo' corresponde a deudores con cumplimiento puntual o atrasos no mayores a 31 días en refinanciaciones periódicas.»
- [no_soportado] CENTRAL — «La categoría 'Riesgo medio' corresponde a clientes con incapacidad parcial de cancelar obligaciones, con atrasos de más de 90 hasta 180 días.»
- [no_soportado] CENTRAL — «La categoría 'Riesgo alto' corresponde a clientes con atrasos de más de 180 días hasta un año.»
- [no_soportado] CENTRAL — «La categoría 'Irrecuperable' corresponde a clientes insolventes, en quiebra, con atrasos superiores al año o en gestión judicial con más de 540 días de atraso.»
- cobertura_patas: [{"pata": "Si los proveedores no financieros de crédito deben cumplir con Protección al Usuario", "cobertura": "cubierta"}, {"pata": "Si las empresas no financieras emisoras de tarjetas deben cumplir con Protección al Usuario", "cobertura": "cubierta"}, {"pata": "Si deben clasificar a sus deudores", "cobertura": "cubierta"}, {"pata": "Bajo qué criterio clasifican a sus deudores", "cobertura": "cubierta"}]
- (juez, otros campos verbatim) cita_documento_correcto: true · cita_precision: "pagina" · abstencion: null

### 3. Trayectoria del agente (tool calls, rep 1) — outputs COMPLETOS por re-ejecución determinística (tool_calls_used: 15 · hit_tool_limit: True)

- paso 1 · `buscar_nodos` · input: `{"consulta": "proveedores no financieros crédito", "limite": 10}` **[RE-EJECUTADO — almacenado truncado]**
  ```json
  {"consulta": "proveedores no financieros crédito", "total_con_match": 353, "resultados": [{"id": "ope_asistencia_crediticia_a_proveedores_no_financieros_de_credito", "type": "OPERATION", "label": "Asistencia crediticia a proveedores no financieros de crédito", "tokens_matcheados": 4, "resumen_propiedades": "Operación de financiamiento directo a personas no financieras proveedoras de crédito."}, {"id": "cla_credito_no_calificado", "type": "CLASSIFICATION", "label": "Crédito no calificado", "tokens_matcheados": 2, "resumen_propiedades": "Exposición crediticia que no cuenta con calificación de ECAI y recibe ponderador de riesgo por defecto."}, {"id": "con_margenes_de_credito_no_percibidos", "type": "CONCEPT", "label": "Márgenes de crédito no percibidos", "tokens_matcheados": 2, "resumen_propiedades": "Componente de ajuste de valuación que refleja spreads de crédito no realizados en la operación."}, {"id": "rsj_proveedor_no_financiero_de_credito", "type": "REGULATED_SUBJECT", "label": "proveedor no financiero de crédito", "tokens_matcheados": 2, "resumen_propiedades": "Sujeto obligado que otorga financiaciones regulado por normas sobre proveedores no financieros, excluidas asociaciones mutuales y cooperativas."}, {"id": "con_activos_no_financieros_no_producidos", "type": "CONCEPT", "label": "activos no financieros no producidos", "tokens_matcheados": 2, "resumen_propiedades": "Transacciones de traspaso de activos intangibles como derechos de propiedad económica, derechos de pesca, minerales, espacio aéreo, pases de deportistas, patent…"}, {"id": "ins_credito_quirografario_no_subordinado", "type": "INSTRUMENT", "label": "Crédito quirografario no subordinado", "tokens_matcheados": 2, "resumen_propiedades": "Exposición crediticia sin garantía real y sin prioridad subordinada en caso de insolvencia."}, {"id": "con_credito_impago_del_importador_no_residente", "type": "CONCEPT", "label": "crédito impago del importador no residente", "tokens_matcheados": 2, "resumen_propiedades": "Monto adeudado por el importador no residente que no ha sido pagado conforme a la operación de exportación."}, {"id": "req_no_contar_con_historial_de_credito_desfavorable", "type": "REQUIREMENT", "label": "no contar con historial de crédito desfavorable", "tokens_matcheados": 2, "resumen_propiedades": "Condición de que el obligado al pago no tenga antecedentes desfavorables en registros públicos de crédito."}, {"id": "con_quebrantos_no_considerados_en_estados_financieros", "type": "CONCEPT", "label": "Quebrantos no considerados en estados financieros", "tokens_matcheados": 2, "resumen_propiedades": "Hechos y circunstancias informados por el auditor conforme a normas mínimas sobre auditorías externas respecto de revisiones limitadas de estados financieros."}, {"id": "ope_enajenacion_de_activos_no_financieros_no_producidos", "type": "OPERATION", "label": "Enajenación de activos no financieros no producidos", "tokens_matcheados": 2, "resumen_propiedades": "Venta por residentes a no residentes de activos no financieros no producidos, cuyo contravalor debe ingresar en divisas."}]}
  ```
- paso 2 · `buscar_nodos` · input: `{"consulta": "empresas no financieras emisoras tarjetas", "limite": 10}` **[RE-EJECUTADO — almacenado truncado]**
  ```json
  {"consulta": "empresas no financieras emisoras tarjetas", "total_con_match": 243, "resultados": [{"id": "ins_participaciones_en_entidades_financieras_y_empresas", "type": "INSTRUMENT", "label": "Participaciones en entidades financieras y empresas", "tokens_matcheados": 2, "resumen_propiedades": "Resultados excluidos del ingreso bruto cuando sean deducibles de la responsabilidad patrimonial computable."}, {"id": "rsj_entidad_no_financiera_emisora_de_tarjetas_de_credito", "type": "REGULATED_SUBJECT", "label": "entidad no financiera emisora de tarjetas de crédito", "tokens_matcheados": 2, "resumen_propiedades": "Sujetos no financieros que emiten tarjetas de crédito en modalidad de sistema cerrado y reportan clasificaciones de deudores."}, {"id": "cla_grupo_2_entidades_financieras_no_comprendidas_en_el_grupo_1", "type": "CLASSIFICATION", "label": "Grupo 2 (entidades financieras no comprendidas en el Grupo 1)", "tokens_matcheados": 2, "resumen_propiedades": "Categoría de clasificación de entidades financieras conforme a la Sección 2, aplicable para determinar el capital mínimo por riesgo operacional."}, {"id": "rsj_empresa_no_financiera_emisora_de_tarjetas_de_credito_y_o_compra", "type": "REGULATED_SUBJECT", "label": "empresa no financiera emisora de tarjetas de crédito y/o compra", "tokens_matcheados": 2, "resumen_propiedades": "Empresas no financieras que emiten tarjetas de crédito o compra y atienden usuarios de servicios financieros."}, {"id": "cla_codigo_de_concepto_s35_compra_venta_no_presencial_de_bienes_tarjetas_debito", "type": "CLASSIFICATION", "label": "Código de concepto S35 (compra/venta no presencial de bienes - tarjetas/débito)", "tokens_matcheados": 2, "resumen_propiedades": "Clasificación para operaciones de consumos con tarjetas o débito en cuenta por compra/venta no presencial de bienes."}, {"id": "req_recursos_que_no_provengan_de_fondos_provistos_por_entidades_financieras_locales", "type": "REQUIREMENT", "label": "Recursos que no provengan de fondos provistos por entidades financieras locales", "tokens_matcheados": 2, "resumen_propiedades": "Exigencia de que la asistencia crediticia en el exterior se otorgue sin fondos directa o indirectamente provistos por las entidades locales."}, {"id": "rep_inversiones_en_capital_regulatorio_de_entidades_financieras_no_consolidadas_hasta_10", "type": "REPORT_ITEM", "label": "Inversiones en capital regulatorio de entidades financieras no consolidadas hasta 10%", "tokens_matcheados": 2, "resumen_propiedades": "Partida contable Código 23100000 para inversiones hasta el 10% del capital ordinario de emisoras no bajo supervisión consolidada."}, {"id": "req_inversiones_en_instrumentos_computables_como_capital_regulatorio_de_entidades_financieras_no_sujetas_a_supervision_consolidada_hasta_10", "type": "REQUIREMENT", "label": "Inversiones en instrumentos computables como capital regulatorio de entidades financieras no sujetas a supervisión consolidada (hasta 10%)", "tokens_matcheados": 2, "resumen_propiedades": "Inversiones en capital regulatorio de entidades financieras no supervisadas consolidadamente, limitadas al 10% del capital social ordinario de la emisora."}, {"id": "req_inversiones_en_instrumentos_computables_como_capital_regulatorio_de_empresas_de_servicios_complementarios_y_companias_de_seguro_no_supervisadas_consolidadamente_hasta_10", "type": "REQUIREMENT", "label": "Inversiones en instrumentos computables como capital regulatorio de empresas de servicios complementarios y compañías de seguro no supervisadas consolidadamente (hasta 10%)", "tokens_matcheados": 2, "resumen_propiedades": "Inversiones en capital regulatorio de empresas de servicios complementarios y aseguradoras no supervisadas consolidadamente, limitadas al 10% del capital social…"}, {"id": "rsj_no_residente", "type": "REGULATED_SUBJECT", "label": "No residente", "tokens_matcheados": 1, "resumen_propiedades": "Persona física o jurídica extranjera que invierte directamente en empresas residentes argentinas y accede al mercado de cambios para repatriar fondos."}]}
  ```
- paso 3 · `buscar_nodos` · input: `{"consulta": "clasificación deudores criterio", "limite": 10}` **[RE-EJECUTADO — almacenado truncado]**
  ```json
  {"consulta": "clasificación deudores criterio", "total_con_match": 63, "resultados": [{"id": "ope_clasificacion_de_deudores", "type": "OPERATION", "label": "Clasificación de deudores", "tokens_matcheados": 2, "resumen_propiedades": "Procedimiento administrativo de categorización de deudores según su mora y situación crediticia, observado por entidades financieras de forma individual o conso…"}, {"id": "prc_clasificacion_de_deudores", "type": "PROCESS", "label": "Clasificación de Deudores", "tokens_matcheados": 2, "resumen_propiedades": "Procedimiento administrativo de evaluación y asignación de categoría de riesgo crediticio a clientes según su situación financiera."}, {"id": "cla_niveles_de_clasificacion_de_deudores", "type": "CLASSIFICATION", "label": "Niveles de clasificación de deudores", "tokens_matcheados": 2, "resumen_propiedades": "Categorías de clasificación de deudores según evaluación de entidades financieras, siendo la categoría 2 equivalente a 'en observación'."}, {"id": "prc_evaluacion_y_clasificacion_de_deudores", "type": "PROCESS", "label": "Evaluación y clasificación de deudores", "tokens_matcheados": 2, "resumen_propiedades": "Procedimiento mediante el cual se asignan clasificaciones a los deudores considerando su capacidad de repago."}, {"id": "cla_riesgo_alto_clasificacion_de_deudores", "type": "CLASSIFICATION", "label": "Riesgo alto (clasificación de deudores)", "tokens_matcheados": 2, "resumen_propiedades": "Categoría que comprende a clientes con atrasos de más de 180 días hasta un año."}, {"id": "cla_riesgo_bajo_clasificacion_de_deudores", "type": "CLASSIFICATION", "label": "Riesgo bajo (clasificación de deudores)", "tokens_matcheados": 2, "resumen_propiedades": "Categoría de clasificación para deudores con cumplimiento puntual o atrasos no mayores a 31 días en refinanciaciones periódicas."}, {"id": "cla_riesgo_medio_clasificacion_de_deudores", "type": "CLASSIFICATION", "label": "Riesgo medio (clasificación de deudores)", "tokens_matcheados": 2, "resumen_propiedades": "Categoría de clasificación para clientes con incapacidad parcial de cancelar obligaciones, con atrasos de más de 90 hasta 180 días."}, {"id": "cla_con_problemas_clasificacion_de_deudores", "type": "CLASSIFICATION", "label": "Con problemas (clasificación de deudores)", "tokens_matcheados": 2, "resumen_propiedades": "Nivel de clasificación superior a los que pueden acceder los deudores recategorizados según la metodología de previsiones."}, {"id": "cla_irrecuperable_clasificacion_de_deudores", "type": "CLASSIFICATION", "label": "Irrecuperable (clasificación de deudores)", "tokens_matcheados": 2, "resumen_propiedades": "Categoría de clasificación que comprende clientes insolventes, en quiebra, con atrasos superiores al año o en gestión judicial con más de 540 días de atraso."}, {"id": "cla_situacion_normal_clasificacion_de_deudores", "type": "CLASSIFICATION", "label": "Situación normal (clasificación de deudores)", "tokens_matcheados": 2, "resumen_propiedades": "Categoría de clasificación de deudores donde el cliente demuestra capacidad de atender adecuadamente todos sus compromisos financieros a través del análisis de …"}]}
  ```
- paso 4 · `ver_nodo` · input: `{"id": "rsj_proveedor_no_financiero_de_credito"}` [re-ejecutado; almacenado ya completo, verificado idéntico]
  → nodo rsj_proveedor_no_financiero_de_credito (proveedor no financiero de crédito) — contenido íntegro abajo (§4)
- paso 5 · `ver_nodo` · input: `{"id": "rsj_empresa_no_financiera_emisora_de_tarjetas_de_credito_y_o_compra"}` [re-ejecutado; almacenado ya completo, verificado idéntico]
  → nodo rsj_empresa_no_financiera_emisora_de_tarjetas_de_credito_y_o_compra (empresa no financiera emisora de tarjetas de crédito y/o compra) — contenido íntegro abajo (§4)
- paso 6 · `ver_nodo` · input: `{"id": "prc_clasificacion_de_deudores"}` [re-ejecutado; almacenado ya completo, verificado idéntico]
  → nodo prc_clasificacion_de_deudores (Clasificación de Deudores) — contenido íntegro abajo (§4)
- paso 7 · `ver_vecinos` · input: `{"id": "rsj_proveedor_no_financiero_de_credito", "direccion": "salientes"}` [re-ejecutado; almacenado ya completo, verificado idéntico]
  ```json
  {"id": "rsj_proveedor_no_financiero_de_credito", "label": "proveedor no financiero de crédito", "n_salientes_total": 1, "n_entrantes_total": 1, "salientes": [{"relation": "debe_designar", "vecino_id": "rsj_directivo_responsable_de_proteccion_de_los_usuarios_de_servicios_financieros", "vecino_label": "Directivo Responsable de Protección de los Usuarios de Servicios Financieros", "provenances": [{"source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf", "location": "p. 27"}]}], "salientes_truncado": false}
  ```
- paso 8 · `ver_vecinos` · input: `{"id": "rsj_empresa_no_financiera_emisora_de_tarjetas_de_credito_y_o_compra", "direccion": "salientes"}` [re-ejecutado; almacenado ya completo, verificado idéntico]
  ```json
  {"id": "rsj_empresa_no_financiera_emisora_de_tarjetas_de_credito_y_o_compra", "label": "empresa no financiera emisora de tarjetas de crédito y/o compra", "n_salientes_total": 1, "n_entrantes_total": 0, "salientes": [{"relation": "debe_designar", "vecino_id": "rsj_directivo_responsable_de_proteccion_de_los_usuarios_de_servicios_financieros", "vecino_label": "Directivo Responsable de Protección de los Usuarios de Servicios Financieros", "provenances": [{"source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf", "location": "p. 27"}]}], "salientes_truncado": false}
  ```
- paso 9 · `buscar_nodos` · input: `{"consulta": "proveedor no financiero clasificación deudores obligación", "limite": 10}` **[RE-EJECUTADO — almacenado truncado]**
  ```json
  {"consulta": "proveedor no financiero clasificación deudores obligación", "total_con_match": 291, "resultados": [{"id": "rsj_proveedor_no_financiero_de_credito", "type": "REGULATED_SUBJECT", "label": "proveedor no financiero de crédito", "tokens_matcheados": 3, "resumen_propiedades": "Sujeto obligado que otorga financiaciones regulado por normas sobre proveedores no financieros, excluidas asociaciones mutuales y cooperativas."}, {"id": "ope_clasificacion_de_deudores", "type": "OPERATION", "label": "Clasificación de deudores", "tokens_matcheados": 2, "resumen_propiedades": "Procedimiento administrativo de categorización de deudores según su mora y situación crediticia, observado por entidades financieras de forma individual o conso…"}, {"id": "prc_clasificacion_de_deudores", "type": "PROCESS", "label": "Clasificación de Deudores", "tokens_matcheados": 2, "resumen_propiedades": "Procedimiento administrativo de evaluación y asignación de categoría de riesgo crediticio a clientes según su situación financiera."}, {"id": "rsj_sector_privado_no_financiero", "type": "REGULATED_SUBJECT", "label": "sector privado no financiero", "tokens_matcheados": 2, "resumen_propiedades": "Categoría de contrapartes a las cuales el BCRA puede otorgar un tratamiento específico, cuyas operaciones se consideran exposiciones a empresas."}, {"id": "rsj_sector_publico_no_financiero", "type": "REGULATED_SUBJECT", "label": "Sector Público no Financiero", "tokens_matcheados": 2, "resumen_propiedades": "Categoría de emisor con exigencias de capital diferenciadas, definida en la Sección 1 del TO sobre Financiamiento al Sector Público no Financiero."}, {"id": "cla_niveles_de_clasificacion_de_deudores", "type": "CLASSIFICATION", "label": "Niveles de clasificación de deudores", "tokens_matcheados": 2, "resumen_propiedades": "Categorías de clasificación de deudores según evaluación de entidades financieras, siendo la categoría 2 equivalente a 'en observación'."}, {"id": "prc_evaluacion_y_clasificacion_de_deudores", "type": "PROCESS", "label": "Evaluación y clasificación de deudores", "tokens_matcheados": 2, "resumen_propiedades": "Procedimiento mediante el cual se asignan clasificaciones a los deudores considerando su capacidad de repago."}, {"id": "cla_riesgo_alto_clasificacion_de_deudores", "type": "CLASSIFICATION", "label": "Riesgo alto (clasificación de deudores)", "tokens_matcheados": 2, "resumen_propiedades": "Categoría que comprende a clientes con atrasos de más de 180 días hasta un año."}, {"id": "cla_riesgo_bajo_clasificacion_de_deudores", "type": "CLASSIFICATION", "label": "Riesgo bajo (clasificación de deudores)", "tokens_matcheados": 2, "resumen_propiedades": "Categoría de clasificación para deudores con cumplimiento puntual o atrasos no mayores a 31 días en refinanciaciones periódicas."}, {"id": "cla_riesgo_medio_clasificacion_de_deudores", "type": "CLASSIFICATION", "label": "Riesgo medio (clasificación de deudores)", "tokens_matcheados": 2, "resumen_propiedades": "Categoría de clasificación para clientes con incapacidad parcial de cancelar obligaciones, con atrasos de más de 90 hasta 180 días."}]}
  ```
- paso 10 · `buscar_nodos` · input: `{"consulta": "empresa no financiera emisora tarjetas clasificación deudores reportar", "limite": 10}` **[RE-EJECUTADO — almacenado truncado]**
  ```json
  {"consulta": "empresa no financiera emisora tarjetas clasificación deudores reportar", "total_con_match": 323, "resultados": [{"id": "rsj_empresa_no_financiera_emisora_de_tarjetas_de_credito_y_o_compra", "type": "REGULATED_SUBJECT", "label": "empresa no financiera emisora de tarjetas de crédito y/o compra", "tokens_matcheados": 5, "resumen_propiedades": "Empresas no financieras que emiten tarjetas de crédito o compra y atienden usuarios de servicios financieros."}, {"id": "rsj_empresa_no_financiera_emisora_de_tarjeta", "type": "REGULATED_SUBJECT", "label": "Empresa no financiera emisora de tarjeta", "tokens_matcheados": 4, "resumen_propiedades": "Persona jurídica emisora de tarjetas que realiza pagos al exterior por el uso de tarjetas emitidas en el país."}, {"id": "rsj_entidad_no_financiera_emisora_de_tarjetas_de_credito", "type": "REGULATED_SUBJECT", "label": "entidad no financiera emisora de tarjetas de crédito", "tokens_matcheados": 4, "resumen_propiedades": "Sujetos no financieros que emiten tarjetas de crédito en modalidad de sistema cerrado y reportan clasificaciones de deudores."}, {"id": "ope_clasificacion_de_deudores", "type": "OPERATION", "label": "Clasificación de deudores", "tokens_matcheados": 2, "resumen_propiedades": "Procedimiento administrativo de categorización de deudores según su mora y situación crediticia, observado por entidades financieras de forma individual o conso…"}, {"id": "prc_clasificacion_de_deudores", "type": "PROCESS", "label": "Clasificación de Deudores", "tokens_matcheados": 2, "resumen_propiedades": "Procedimiento administrativo de evaluación y asignación de categoría de riesgo crediticio a clientes según su situación financiera."}, {"id": "rsj_entidad_financiera_emisora", "type": "REGULATED_SUBJECT", "label": "Entidad financiera emisora", "tokens_matcheados": 2, "resumen_propiedades": "Entidad encargada de emitir las certificaciones de pago de importación según los requisitos reglamentarios."}, {"id": "cla_niveles_de_clasificacion_de_deudores", "type": "CLASSIFICATION", "label": "Niveles de clasificación de deudores", "tokens_matcheados": 2, "resumen_propiedades": "Categorías de clasificación de deudores según evaluación de entidades financieras, siendo la categoría 2 equivalente a 'en observación'."}, {"id": "rsj_entidad_financiera_emisora_de_tarjeta", "type": "REGULATED_SUBJECT", "label": "Entidad financiera emisora de tarjeta", "tokens_matcheados": 2, "resumen_propiedades": "Institución financiera que emite tarjetas de crédito y/o de compra."}, {"id": "prc_evaluacion_y_clasificacion_de_deudores", "type": "PROCESS", "label": "Evaluación y clasificación de deudores", "tokens_matcheados": 2, "resumen_propiedades": "Procedimiento mediante el cual se asignan clasificaciones a los deudores considerando su capacidad de repago."}, {"id": "rsj_compania_holding_no_entidad_financiera", "type": "REGULATED_SUBJECT", "label": "Compañía holding no entidad financiera", "tokens_matcheados": 2, "resumen_propiedades": "Entidades holding que controlan entidades financieras y están sujetas a ratio de fondeo neto estable."}]}
  ```
- paso 11 · `ver_nodo` · input: `{"id": "rsj_entidad_no_financiera_emisora_de_tarjetas_de_credito"}` [re-ejecutado; almacenado ya completo, verificado idéntico]
  → nodo rsj_entidad_no_financiera_emisora_de_tarjetas_de_credito (entidad no financiera emisora de tarjetas de crédito) — contenido íntegro abajo (§4)
- paso 12 · `buscar_nodos` · input: `{"consulta": "criterio clasificación deudores mora atraso", "limite": 10}` **[RE-EJECUTADO — almacenado truncado]**
  ```json
  {"consulta": "criterio clasificación deudores mora atraso", "total_con_match": 81, "resultados": [{"id": "ope_clasificacion_de_deudores", "type": "OPERATION", "label": "Clasificación de deudores", "tokens_matcheados": 2, "resumen_propiedades": "Procedimiento administrativo de categorización de deudores según su mora y situación crediticia, observado por entidades financieras de forma individual o conso…"}, {"id": "prc_clasificacion_de_deudores", "type": "PROCESS", "label": "Clasificación de Deudores", "tokens_matcheados": 2, "resumen_propiedades": "Procedimiento administrativo de evaluación y asignación de categoría de riesgo crediticio a clientes según su situación financiera."}, {"id": "cla_niveles_de_clasificacion_de_deudores", "type": "CLASSIFICATION", "label": "Niveles de clasificación de deudores", "tokens_matcheados": 2, "resumen_propiedades": "Categorías de clasificación de deudores según evaluación de entidades financieras, siendo la categoría 2 equivalente a 'en observación'."}, {"id": "prc_evaluacion_y_clasificacion_de_deudores", "type": "PROCESS", "label": "Evaluación y clasificación de deudores", "tokens_matcheados": 2, "resumen_propiedades": "Procedimiento mediante el cual se asignan clasificaciones a los deudores considerando su capacidad de repago."}, {"id": "cla_riesgo_alto_clasificacion_de_deudores", "type": "CLASSIFICATION", "label": "Riesgo alto (clasificación de deudores)", "tokens_matcheados": 2, "resumen_propiedades": "Categoría que comprende a clientes con atrasos de más de 180 días hasta un año."}, {"id": "cla_riesgo_bajo_clasificacion_de_deudores", "type": "CLASSIFICATION", "label": "Riesgo bajo (clasificación de deudores)", "tokens_matcheados": 2, "resumen_propiedades": "Categoría de clasificación para deudores con cumplimiento puntual o atrasos no mayores a 31 días en refinanciaciones periódicas."}, {"id": "cla_riesgo_medio_clasificacion_de_deudores", "type": "CLASSIFICATION", "label": "Riesgo medio (clasificación de deudores)", "tokens_matcheados": 2, "resumen_propiedades": "Categoría de clasificación para clientes con incapacidad parcial de cancelar obligaciones, con atrasos de más de 90 hasta 180 días."}, {"id": "cla_con_problemas_clasificacion_de_deudores", "type": "CLASSIFICATION", "label": "Con problemas (clasificación de deudores)", "tokens_matcheados": 2, "resumen_propiedades": "Nivel de clasificación superior a los que pueden acceder los deudores recategorizados según la metodología de previsiones."}, {"id": "cla_irrecuperable_clasificacion_de_deudores", "type": "CLASSIFICATION", "label": "Irrecuperable (clasificación de deudores)", "tokens_matcheados": 2, "resumen_propiedades": "Categoría de clasificación que comprende clientes insolventes, en quiebra, con atrasos superiores al año o en gestión judicial con más de 540 días de atraso."}, {"id": "cla_situacion_normal_clasificacion_de_deudores", "type": "CLASSIFICATION", "label": "Situación normal (clasificación de deudores)", "tokens_matcheados": 2, "resumen_propiedades": "Categoría de clasificación de deudores donde el cliente demuestra capacidad de atender adecuadamente todos sus compromisos financieros a través del análisis de …"}]}
  ```
- paso 13 · `ver_nodo` · input: `{"id": "cla_situacion_normal_clasificacion_de_deudores"}` [re-ejecutado; almacenado ya completo, verificado idéntico]
  → nodo cla_situacion_normal_clasificacion_de_deudores (Situación normal (clasificación de deudores)) — contenido íntegro abajo (§4)
- paso 14 · `ver_nodo` · input: `{"id": "cla_riesgo_bajo_clasificacion_de_deudores"}` [re-ejecutado; almacenado ya completo, verificado idéntico]
  → nodo cla_riesgo_bajo_clasificacion_de_deudores (Riesgo bajo (clasificación de deudores)) — contenido íntegro abajo (§4)
- paso 15 · `ver_nodo` · input: `{"id": "cla_riesgo_medio_clasificacion_de_deudores"}` [re-ejecutado; almacenado ya completo, verificado idéntico]
  → nodo cla_riesgo_medio_clasificacion_de_deudores (Riesgo medio (clasificación de deudores)) — contenido íntegro abajo (§4)
- **Respuesta final** (respondible: true)**:** «Sí, tanto los proveedores no financieros de crédito como las empresas no financieras emisoras de tarjetas de crédito y/o compra deben cumplir con Protección al Usuario. Ambos sujetos están obligados a designar un Directivo Responsable de Protección de los Usuarios de Servicios Financieros. Respecto a la clasificación de deudores, específicamente las entidades no financieras emisoras de tarjetas de crédito reportan clasificaciones de deudores. Los criterios de clasificación se basan en la situación crediticia y mora del deudor, utilizando las siguientes categorías: (1) Situación normal: cuando el cliente demuestra capacidad de atender adecuadamente todos sus compromisos financieros a través del análisis de flujo de fondos; (2) Riesgo bajo: para deudores con cumplimiento puntual o atrasos no mayores a 31 días en refinanciaciones periódicas; (3) Riesgo medio: para clientes con incapacidad parcial de cancelar obligaciones, con atrasos de más de 90 hasta 180 días; (4) Riesgo alto: para clientes con atrasos de más de 180 días hasta un año; e (5) Irrecuperable: para clientes insolventes, en quiebra, con atrasos superiores al año o en gestión judicial con más de 540 días de atraso.»
- **Citas:** [{"source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf", "location": "p. 27"}, {"source_doc": "TO_clasificacion_deudores_actual.pdf", "location": "p. 39"}, {"source_doc": "TO_clasificacion_deudores_actual.pdf", "location": "p. 20"}, {"source_doc": "TO_clasificacion_deudores_actual.pdf", "location": "p. 35"}, {"source_doc": "TO_clasificacion_deudores_actual.pdf", "location": "p. 36"}]

### 4. Nodos abiertos con `ver_nodo` — contenido ÍNTEGRO (re-ejecución sobre kg.json congelado)

**rsj_proveedor_no_financiero_de_credito** (abierto en paso 4):
```json
{
 "id": "rsj_proveedor_no_financiero_de_credito",
 "type": "REGULATED_SUBJECT",
 "label": "proveedor no financiero de crédito",
 "properties": {
  "version": "A 8433",
  "description": "Sujeto obligado que otorga financiaciones regulado por normas sobre proveedores no financieros, excluidas asociaciones mutuales y cooperativas.",
  "aliases": [
   "Proveedores no financieros de crédito",
   "Otros proveedores no financieros de crédito",
   "Proveedor no financiero de crédito"
  ],
  "source_to": "proteccion_usuarios",
  "mention_count": 5
 },
 "provenances": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p. 27"
  },
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p. 39"
  },
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p. 21"
  },
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p. 3"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "pp. 42-43"
  }
 ]
}
```

**rsj_empresa_no_financiera_emisora_de_tarjetas_de_credito_y_o_compra** (abierto en paso 5):
```json
{
 "id": "rsj_empresa_no_financiera_emisora_de_tarjetas_de_credito_y_o_compra",
 "type": "REGULATED_SUBJECT",
 "label": "empresa no financiera emisora de tarjetas de crédito y/o compra",
 "properties": {
  "version": "A 8433",
  "description": "Empresas no financieras que emiten tarjetas de crédito o compra y atienden usuarios de servicios financieros.",
  "aliases": [
   "Empresas no financieras emisoras de tarjetas de crédito",
   "Empresas no financieras emisoras de tarjetas de crédito y/o compra",
   "Empresa no financiera emisora de tarjetas de crédito y/o compra"
  ],
  "source_to": "proteccion_usuarios",
  "mention_count": 3
 },
 "provenances": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p. 27"
  },
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p. 21"
  },
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p. 3"
  }
 ]
}
```

**prc_clasificacion_de_deudores** (abierto en paso 6):
```json
{
 "id": "prc_clasificacion_de_deudores",
 "type": "PROCESS",
 "label": "Clasificación de Deudores",
 "properties": {
  "version": "A 8378",
  "description": "Procedimiento administrativo de evaluación y asignación de categoría de riesgo crediticio a clientes según su situación financiera.",
  "aliases": [
   "Clasificación de Deudores",
   "clasificación de deudores"
  ],
  "source_to": "clasificacion_deudores",
  "mention_count": 7
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "pp. 1-2"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p. 193"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p. 196"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p. 33"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "p. 10"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "p. 19"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "p. 26"
  }
 ]
}
```

**rsj_entidad_no_financiera_emisora_de_tarjetas_de_credito** (abierto en paso 11):
```json
{
 "id": "rsj_entidad_no_financiera_emisora_de_tarjetas_de_credito",
 "type": "REGULATED_SUBJECT",
 "label": "entidad no financiera emisora de tarjetas de crédito",
 "properties": {
  "version": "A 8378",
  "description": "Sujetos no financieros que emiten tarjetas de crédito en modalidad de sistema cerrado y reportan clasificaciones de deudores.",
  "aliases": [
   "Entidades no financieras emisoras de tarjetas de crédito"
  ],
  "source_to": "clasificacion_deudores",
  "mention_count": 1
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "p. 39"
  }
 ]
}
```

**cla_situacion_normal_clasificacion_de_deudores** (abierto en paso 13):
```json
{
 "id": "cla_situacion_normal_clasificacion_de_deudores",
 "type": "CLASSIFICATION",
 "label": "Situación normal (clasificación de deudores)",
 "properties": {
  "version": "A 8378",
  "description": "Categoría de clasificación de deudores donde el cliente demuestra capacidad de atender adecuadamente todos sus compromisos financieros a través del análisis de flujo de fondos.",
  "aliases": [
   "Situación normal",
   "en situación normal"
  ],
  "source_to": "clasificacion_deudores",
  "mention_count": 4
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "p. 20"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "p. 22"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "p. 23"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "p. 35"
  }
 ]
}
```

**cla_riesgo_bajo_clasificacion_de_deudores** (abierto en paso 14):
```json
{
 "id": "cla_riesgo_bajo_clasificacion_de_deudores",
 "type": "CLASSIFICATION",
 "label": "Riesgo bajo (clasificación de deudores)",
 "properties": {
  "version": "A 8378",
  "description": "Categoría de clasificación para deudores con cumplimiento puntual o atrasos no mayores a 31 días en refinanciaciones periódicas.",
  "aliases": [
   "Riesgo bajo"
  ],
  "source_to": "clasificacion_deudores",
  "mention_count": 2
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "p. 35"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "p. 36"
  }
 ]
}
```

**cla_riesgo_medio_clasificacion_de_deudores** (abierto en paso 15):
```json
{
 "id": "cla_riesgo_medio_clasificacion_de_deudores",
 "type": "CLASSIFICATION",
 "label": "Riesgo medio (clasificación de deudores)",
 "properties": {
  "version": "A 8378",
  "description": "Categoría de clasificación para clientes con incapacidad parcial de cancelar obligaciones, con atrasos de más de 90 hasta 180 días.",
  "aliases": [
   "Riesgo medio"
  ],
  "source_to": "clasificacion_deudores",
  "mention_count": 1
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "p. 36"
  }
 ]
}
```

### 5. Pasaje(s) del PDF — secciones ground-truth (máx ~1.500 chars por pata)

**Protección, Puntos 1.1.2.4 y 1.1.2.5 → Punto 1.1.2.4:**
[TO_proteccion_usuarios_servicios_financieros_actual.pdf · Punto/Sección 1.1.2.4 (PDF pág 3) · localizacion: ok]
> 1.1.2.4. Empresas no financieras emisoras de tarjetas de crédito y/o compra. 1.1.2.5. Otros proveedores no financieros de crédito alcanzados por las normas sobre “Proveedores no financieros de crédito”, e xcepto que se trate de asociaciones mutuales o cooperativas, por las financiaciones que otorguen. 1. 1.2.6. Proveedores de servicios de pago que ofrecen cuentas de pago (PSPCP). 1. 1.2.7. Proveedores de servicios de pago que cumplen la función de iniciaci ón (PSI) y prestan el servicio de billetera digital. C uando un tercero desarrolle tareas relativas a servicios ofrecidos por los sujetos oblig a- dos o en su nombre, ambos serán responsables por el cumplimiento de las presentes normas. Lo anterior deberá est ablecerse en los instrumentos que acuerden la realización de dichas tareas. B.C.R.A. PROTECCIÓN DE LOS USUARIOS DE SERVICIOS FINANCIEROS Sección 1. Disposiciones generales. Versión: 8a. COMUNICACIÓN “A” 7744 Vigencia: 28/02/2023 Página 1

**Protección, Puntos 1.1.2.4 y 1.1.2.5 → Punto 1.1.2.5:**
[TO_proteccion_usuarios_servicios_financieros_actual.pdf · Punto/Sección 1.1.2.5 (PDF pág 3) · localizacion: ok]
> 1.1.2.5. Otros proveedores no financieros de crédito alcanzados por las normas sobre “Proveedores no financieros de crédito”, e xcepto que se trate de asociaciones mutuales o cooperativas, por las financiaciones que otorguen. 1. 1.2.6. Proveedores de servicios de pago que ofrecen cuentas de pago (PSPCP). 1. 1.2.7. Proveedores de servicios de pago que cumplen la función de iniciaci ón (PSI) y prestan el servicio de billetera digital. C uando un tercero desarrolle tareas relativas a servicios ofrecidos por los sujetos oblig a- dos o en su nombre, ambos serán responsables por el cumplimiento de las presentes normas. Lo anterior deberá est ablecerse en los instrumentos que acuerden la realización de dichas tareas. B.C.R.A. PROTECCIÓN DE LOS USUARIOS DE SERVICIOS FINANCIEROS Sección 1. Disposiciones generales. Versión: 8a. COMUNICACIÓN “A” 7744 Vigencia: 28/02/2023 Página 1

**Clasificación, Punto 10.1 → Punto 10.1:**
[TO_clasificacion_deudores_actual.pdf · Punto/Sección 10.1 (PDF pág 43) · localizacion: ok]
> 10.1. Proveedores no financieros de crédito. Las empresas no financieras emisoras de tarjetas de crédito y/o compra y los otros proveed o- res no financieros de crédito alcanzados por las normas sobre “Proveedores no financieros de crédito”, deberán clasificar a los respectivos deudores en función de su mora, según los crit e- rios aplicables para la ca rtera de “consumo o vivienda” y por aplica ción de las disposiciones previstas en el punto 7.3. (recategorización obligatoria). 10.2. Fiduciarios de fideicomisos financieros comprendidos en la Ley de Entidades Financieras. 10.2.1. Clasificación de deudores de créditos fideicomitidos. Deberán clasificar a los deudores de los créditos fideicomitidos de acuerdo con la p e- riodicidad y demás condiciones establecidas para las carteras “comercial” o “para co n- sumo o vivienda”, según corresponda. 10.2.2. Requerimientos de la Superintendencia de Entidades Financieras y Cambiarias. Deberán proporcionar a la SEFyC toda la información que ésta les requiera, para ca l- cular las previsiones que deberán computar las entidades financieras –sean o no las originantes de los créditos cedidos – sobre sus tenencias de certificados de particip a- ción y/o títulos de deuda de los respectivos fideicomisos. 10.3. Sociedades de garantía recíproca y fondos de garantía de carácter público. Las sociedades de garantía recíproca y los fondos de garantía

**Cita textual GT (eval_set_v1, verbatim):** «[Protección 1.1.2.4/1.1.2.5] Empresas no financieras emisoras de tarjetas de crédito y/o compra [...] Otros proveedores no financieros de crédito [...] | [Clasificación 10.1] Las empresas no financieras emisoras de tarjetas de crédito y/o compra y los otros proveedores no financieros de crédito [...] deberán clasificar a los respectivos deudores en función de su mora, según los criterios aplicables para la cartera de 'consumo o vivienda' y por aplicación de las disposiciones previstas en el punto 7.3.»

### 5b. Provenances VERBATIM (kg.json, lista completa) de los nodos citados en la respuesta final

**rsj_directivo_responsable_de_proteccion_de_los_usuarios_de_servicios_financieros** (Directivo Responsable de Protección de los Usuarios de Servicios Financieros) — ✓ provenance COINCIDE con una cita de la respuesta final · expuesto en la trayectoria (buscar_nodos/ver_vecinos), no abierto
```json
[
 {
  "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
  "location": "p. 24"
 },
 {
  "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
  "location": "p. 25"
 },
 {
  "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
  "location": "p. 26"
 },
 {
  "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
  "location": "p. 27"
 }
]
```

**rsj_proveedor_no_financiero_de_credito** (proveedor no financiero de crédito) — ✓ provenance COINCIDE con una cita de la respuesta final · abierto con ver_nodo
```json
[
 {
  "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
  "location": "p. 27"
 },
 {
  "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
  "location": "p. 39"
 },
 {
  "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
  "location": "p. 21"
 },
 {
  "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
  "location": "p. 3"
 },
 {
  "source_doc": "TO_clasificacion_deudores_actual.pdf",
  "location": "pp. 42-43"
 }
]
```

**rsj_empresa_no_financiera_emisora_de_tarjetas_de_credito_y_o_compra** (empresa no financiera emisora de tarjetas de crédito y/o compra) — ✓ provenance COINCIDE con una cita de la respuesta final · abierto con ver_nodo
```json
[
 {
  "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
  "location": "p. 27"
 },
 {
  "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
  "location": "p. 21"
 },
 {
  "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
  "location": "p. 3"
 }
]
```

**rsj_entidad_no_financiera_emisora_de_tarjetas_de_credito** (entidad no financiera emisora de tarjetas de crédito) — ✓ provenance COINCIDE con una cita de la respuesta final · abierto con ver_nodo
```json
[
 {
  "source_doc": "TO_clasificacion_deudores_actual.pdf",
  "location": "p. 39"
 }
]
```

**cla_situacion_normal_clasificacion_de_deudores** (Situación normal (clasificación de deudores)) — ✓ provenance COINCIDE con una cita de la respuesta final · abierto con ver_nodo
```json
[
 {
  "source_doc": "TO_clasificacion_deudores_actual.pdf",
  "location": "p. 20"
 },
 {
  "source_doc": "TO_clasificacion_deudores_actual.pdf",
  "location": "p. 22"
 },
 {
  "source_doc": "TO_clasificacion_deudores_actual.pdf",
  "location": "p. 23"
 },
 {
  "source_doc": "TO_clasificacion_deudores_actual.pdf",
  "location": "p. 35"
 }
]
```

**cla_riesgo_bajo_clasificacion_de_deudores** (Riesgo bajo (clasificación de deudores)) — ✓ provenance COINCIDE con una cita de la respuesta final · abierto con ver_nodo
```json
[
 {
  "source_doc": "TO_clasificacion_deudores_actual.pdf",
  "location": "p. 35"
 },
 {
  "source_doc": "TO_clasificacion_deudores_actual.pdf",
  "location": "p. 36"
 }
]
```

**cla_riesgo_medio_clasificacion_de_deudores** (Riesgo medio (clasificación de deudores)) — ✓ provenance COINCIDE con una cita de la respuesta final · abierto con ver_nodo
```json
[
 {
  "source_doc": "TO_clasificacion_deudores_actual.pdf",
  "location": "p. 36"
 }
]
```

**prc_clasificacion_de_deudores** (Clasificación de Deudores) — abierto con ver_nodo
```json
[
 {
  "source_doc": "TO_clasificacion_deudores_actual.pdf",
  "location": "pp. 1-2"
 },
 {
  "source_doc": "TO_capitales_minimos_actual.pdf",
  "location": "p. 193"
 },
 {
  "source_doc": "TO_capitales_minimos_actual.pdf",
  "location": "p. 196"
 },
 {
  "source_doc": "TO_capitales_minimos_actual.pdf",
  "location": "p. 33"
 },
 {
  "source_doc": "TO_clasificacion_deudores_actual.pdf",
  "location": "p. 10"
 },
 {
  "source_doc": "TO_clasificacion_deudores_actual.pdf",
  "location": "p. 19"
 },
 {
  "source_doc": "TO_clasificacion_deudores_actual.pdf",
  "location": "p. 26"
 }
]
```

### 6. ADJUDICACIÓN (Agustina):
```
Adjudicación de la autora, 2026-07-15, asistida por revisión.

- pata / claim: claims de "Situación normal" y "Riesgo bajo"
- sintoma_capa1: noise_sensitivity        causa_capa2: contenido_kg
- primaria/secundaria: PRIMARIA
- evidencia (1 línea): Ambos ecos verbatim de nodos defectuosos.
  cla_situacion_normal_clasificacion_de_deudores porta la definición COMERCIAL (6.5.1,
  "flujo de fondos") sin marca de alcance bajo label genérico — la definición pertinente
  al criterio de los PNFC es la de consumo (7.2.1, "puntual ≤31 días"); nodo des-scopeado
  (precedente: CQ-024 dev). cla_riesgo_bajo_... define riesgo bajo como "puntual o ≤31
  días en refinanciaciones periódicas", que contradice el 7.2.2 ("atrasos de más de 31
  hasta 90 días") — definición errónea.

- pata / claim: riesgo medio / riesgo alto / irrecuperable + los dos claims del
  Directivo Responsable
- sintoma_capa1: —        causa_capa2: — (FALSOS POSITIVOS DEL JUEZ, sin par, ×5)
- primaria/secundaria: —
- evidencia (1 línea): Los 3 de categorías son ecos de nodos expuestos, correctos contra
  7.2.3/7.2.4/7.2.5 verbatim; los 2 del Directivo Responsable están soportados por
  rsj_directivo_... expuesto y los edges debe_designar de los pasos 7-8, correctos contra
  Protección 3.2.1.1 ("las empresas no financieras emisoras... y los otros proveedores
  no financieros de crédito... deberán designar"). Mecanismo de los 3 de categorías:
  contenido verdadero del corpus fuera de ground_truth_secciones — tercer caso del patrón
  (con run_3/CQ-020 y on/run_5/CQ-019).

Observación sin par: cla_riesgo_alto y cla_irrecuperable tienen provenances VACÍAS ([])
— imperfección real del grafo, sin efecto en este veredicto (las citas de la respuesta
salieron de otros nodos).

Patrón de calibración: "primaria única + FPs masivos" — acierto = la primaria
{noise_sensitivity, contenido_kg}.
```

