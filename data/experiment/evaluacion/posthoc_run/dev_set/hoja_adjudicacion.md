# Hoja de adjudicación — dev set v5 (adjudicación CIEGA)

Generada 2026-07-13 desde: `queries/eval_set_v1.json` (pregunta verbatim), `posthoc_run/traces/{label}/{run}/CQ-*.json` (trayectoria del agente, rep 1, y veredictos del juez por claim), `kg.json` congelados de run_1/run_5 (nodos íntegros) y `pdf_locate` sobre `data/experiment/subset/` (pasajes GT).

Esta hoja NO contiene etiquetas, confianzas ni sugerencias de ningún verificador automático: la adjudicación se hace contra la evidencia cruda de abajo, con la taxonomía v2 (`taxonomia.md`: capa 1 por precedencia POR PATA; capa 2 por el árbol).

---

## Caso off/run_5/CQ-017

### 1. Pregunta (verbatim eval_set_v1) y patas (judge.step1.patas_de_la_pregunta)

> Un operador de cambio, ¿está alcanzado por las normas de Protección de los Usuarios de Servicios Financieros y debe intervenir como entidad autorizada en el mercado de cambios?

- Categoría: `multi_norma` · TOs fuente: proteccion, exterior
- Ground-truth secciones: Protección, Punto 1.1.2.2 · Exterior y Cambios, Punto 1.1
- Pata 1: "Si un operador de cambio está alcanzado por las normas de Protección de los Usuarios de Servicios Financieros"
- Pata 2: "Si un operador de cambio debe intervenir como entidad autorizada en el mercado de cambios"

### 2. Claims con veredicto negativo del juez (verbatim)
- [no_soportado] secundaria — «La categoría de 'sujetos obligados' agrupa a entidades financieras, operadores de cambio, fiduciarios, empresas emisoras de tarjetas y proveedores no financieros de crédito.»
- [no_soportado] secundaria — «Como sujeto obligado, el operador de cambio debe garantizar información clara y suficiente a los usuarios.»
- [no_soportado] secundaria — «Como sujeto obligado, el operador de cambio debe garantizar trato equitativo y digno a los usuarios.»
- [no_soportado] secundaria — «Como sujeto obligado, el operador de cambio debe garantizar acceso igualitario a servicios.»
- [no_soportado] secundaria — «Como sujeto obligado, el operador de cambio debe garantizar consideración y resolución fundada de reclamos.»
- [falso] CENTRAL — «Los operadores de cambio son entidades financieras autorizadas a operar en el mercado de cambios.»
- [no_soportado] secundaria — «Existen entidades denominadas 'entidades operadoras en mercado de cambios' que son entidades financieras autorizadas a operar en el mercado de cambios local.»
- cobertura_patas: [{"pata": "Si un operador de cambio está alcanzado por las normas de Protección de los Usuarios de Servicios Financieros", "cobertura": "cubierta"}, {"pata": "Si un operador de cambio debe intervenir como entidad autorizada en el mercado de cambios", "cobertura": "cubierta"}]

### 3. Trayectoria del agente (tool calls, rep 1)
- paso 1 · `buscar_nodos` · input: `{"consulta": "operador de cambio", "limite": 10}`
  → {"consulta": "operador de cambio", "total_con_match": 3390, "resultados": [{"id": "operador_de_cambio__agencia_cambio", "type": "EntidadFinanciera", "label": "O …(no-JSON)
- paso 2 · `buscar_nodos` · input: `{"consulta": "protección usuarios servicios financieros", "limite": 10}`
  → {"consulta": "protección usuarios servicios financieros", "total_con_match": 199, "resultados": [{"id": "proteccion_de_usuarios_de_servicios_financieros", "type …(no-JSON)
- paso 3 · `buscar_nodos` · input: `{"consulta": "mercado de cambios entidad autorizada", "limite": 10}`
  → {"consulta": "mercado de cambios entidad autorizada", "total_con_match": 3492, "resultados": [{"id": "entidad_con_acceso_a_mercado_de_cambios__otra", "type": "E …(no-JSON)
- paso 4 · `ver_nodo` · input: `{"id": "operador_de_cambio__agencia_cambio"}`
  → nodo operador_de_cambio__agencia_cambio (Operador de cambio) — contenido íntegro abajo (§4)
- paso 5 · `ver_nodo` · input: `{"id": "normas_de_proteccion_de_usuarios_de_servicios_financieros"}`
  → nodo normas_de_proteccion_de_usuarios_de_servicios_financieros (Normas de protección de usuarios de servicios financieros) — contenido íntegro abajo (§4)
- paso 6 · `ver_nodo` · input: `{"id": "entidad_operadora_en_mercado_de_cambios__otra"}`
  → nodo entidad_operadora_en_mercado_de_cambios__otra (Entidad operadora en mercado de cambios) — contenido íntegro abajo (§4)
- paso 7 · `ver_vecinos` · input: `{"id": "operador_de_cambio__agencia_cambio", "direccion": "ambas"}`
  → salientes=0 entrantes=0 → 
- paso 8 · `ver_vecinos` · input: `{"id": "normas_de_proteccion_de_usuarios_de_servicios_financieros", "direccion": "salientes"}`
  → salientes=3 entrantes=0 → recae_sobre→sujetos_obligados; protege_a→usuarios_de_servicios_financieros; complementa_a→legislacion_sobre_relaciones_de_consumo
- paso 9 · `ver_nodo` · input: `{"id": "sujetos_obligados"}`
  → nodo sujetos_obligados (Sujetos obligados) — contenido íntegro abajo (§4)
- paso 10 · `ver_vecinos` · input: `{"id": "sujetos_obligados", "direccion": "salientes"}`
  → {"id": "sujetos_obligados", "label": "Sujetos obligados", "n_salientes_total": 16, "n_entrantes_total": 22, "salientes": [{"relation": "recae_sobre", "vecino_id …(no-JSON)
- paso 11 · `buscar_nodos` · input: `{"consulta": "operador cambio sujeto obligado", "limite": 10}`
  → {"consulta": "operador cambio sujeto obligado", "total_con_match": 81, "resultados": [{"id": "sujeto_obligado", "type": "Concepto", "label": "Sujeto obligado",  …(no-JSON)
- paso 12 · `buscar_nodos` · input: `{"consulta": "operador cambio entidad autorizada mercado cambios", "limite": 10}`
  → {"consulta": "operador cambio entidad autorizada mercado cambios", "total_con_match": 394, "resultados": [{"id": "entidad_con_acceso_a_mercado_de_cambios__otra" …(no-JSON)
- paso 13 · `ver_nodo` · input: `{"id": "sujeto_obligado"}`
  → nodo sujeto_obligado (Sujeto obligado) — contenido íntegro abajo (§4)
- paso 14 · `ver_vecinos` · input: `{"id": "sujeto_obligado", "direccion": "entrantes"}`
  → {"id": "sujeto_obligado", "label": "Sujeto obligado", "n_salientes_total": 12, "n_entrantes_total": 44, "entrantes": [{"relation": "consume_de", "vecino_id": "u …(no-JSON)
- paso 15 · `buscar_nodos` · input: `{"consulta": "operador cambio autorizado intervenir mercado", "limite": 10}`
  → {"consulta": "operador cambio autorizado intervenir mercado", "total_con_match": 215, "resultados": [{"id": "operador_de_cambio__agencia_cambio", "type": "Entid …(no-JSON)
- **Respuesta final:** «Sí, un operador de cambio está alcanzado por las normas de Protección de los Usuarios de Servicios Financieros. Según la regulación del BCRA, los operadores de cambio son expresamente incluidos en la categoría de "sujetos obligados", que agrupa a entidades financieras, operadores de cambio, fiduciarios, empresas emisoras de tarjetas y proveedores no financieros de crédito. Como sujeto obligado, el operador de cambio debe cumplir con todas las disposiciones de protección de usuarios de servicios financieros, incluyendo garantizar información clara y suficiente, trato equitativo y digno, acceso igualitario a servicios, consideración y resolución fundada de reclamos, y otras obligaciones establecidas en la normativa. Respecto a intervenir como entidad autorizada en el mercado de cambios, la regulación establece que existen entidades operadoras en mercado de cambios que son entidades financieras autorizadas a operar en el mercado de cambios local, y los operadores de cambio son entidades financieras autorizadas a operar en el mercado de cambios.»
- **Citas:** [{"source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf", "location": "Punto 1.1 — Partes."}, {"source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf", "location": "Punto 1.3 — Encuadre y alcance normativo."}, {"source_doc": "TO_exterior_cambios_actual.pdf", "location": "Punto 3.16 — Requisitos complementarios para los egresos por el mercado de cambios. (parte 1/4)"}]

### 4. Nodos abiertos con `ver_nodo` — contenido ÍNTEGRO (kg.json congelado)

**operador_de_cambio__agencia_cambio**:
```json
{
 "id": "operador_de_cambio__agencia_cambio",
 "type": "EntidadFinanciera",
 "label": "Operador de cambio",
 "properties": {
  "description": "Sujeto obligado por las operaciones comprendidas en normas sobre exterior y cambios.",
  "categoria": "agencia_cambio"
 },
 "provenance": {
  "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
  "location": "Punto 1.1 — Partes."
 }
}
```

**normas_de_proteccion_de_usuarios_de_servicios_financieros**:
```json
{
 "id": "normas_de_proteccion_de_usuarios_de_servicios_financieros",
 "type": "Restriccion",
 "label": "Normas de protección de usuarios de servicios financieros",
 "properties": {
  "description": "Disposiciones de aplicación a todos los sujetos obligados según tipos y funcionalidades de su operatoria y modalidades de transacciones, relaciones y contratos con usuarios."
 },
 "provenance": {
  "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
  "location": "Punto 1.3 — Encuadre y alcance normativo."
 }
}
```

**entidad_operadora_en_mercado_de_cambios__otra**:
```json
{
 "id": "entidad_operadora_en_mercado_de_cambios__otra",
 "type": "EntidadFinanciera",
 "label": "Entidad operadora en mercado de cambios",
 "properties": {
  "description": "Entidad financiera autorizada a operar en el mercado de cambios local",
  "categoria": "otra"
 },
 "provenance": {
  "source_doc": "TO_exterior_cambios_actual.pdf",
  "location": "Punto 3.16 — Requisitos complementarios para los egresos por el mercado de cambios. (parte 1/4)"
 }
}
```

**sujetos_obligados**:
```json
{
 "id": "sujetos_obligados",
 "type": "Concepto",
 "label": "Sujetos obligados",
 "properties": {
  "description": "Personas jurídicas comprendidas en la regulación del BCRA sujetas a cumplir obligaciones de protección de usuarios de servicios financieros."
 },
 "provenance": {
  "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
  "location": "Punto 1 + Punto 1"
 }
}
```

**sujeto_obligado**:
```json
{
 "id": "sujeto_obligado",
 "type": "Concepto",
 "label": "Sujeto obligado",
 "properties": {
  "description": "Categoría que agrupa entidades financieras, operadores de cambio, fiduciarios, empresas emisoras de tarjetas y proveedores no financieros de crédito."
 },
 "provenance": {
  "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
  "location": "Punto 1.1 — Partes."
 }
}
```

### 5. Pasaje(s) del PDF — secciones ground-truth (máx ~1.500 chars por pata)

**Protección, Punto 1.1.2.2:**
[TO_proteccion_usuarios_servicios_financieros_actual.pdf · Punto/Sección 1.1.2.2 (PDF pág 3)]
> 1.1.2.2. Operadores de cambio, por las operaciones comprendidas en las normas sobre “Exterior y cambios”. 1.1.2.3. Fiduciari os de fideicomisos acreedor es de créditos cedidos por entidades fina n- cieras. 1.1.2.4. Empresas no financieras emisoras de tarjetas de crédito y/o compra. 1.1.2.5. Otros proveedores no financieros de crédito alcanzados por las normas sobre “Proveedores no  financieros de crédito”, e xcepto que se trate de asociaciones mutuales o cooperativas, por las financiaciones que otorguen. 1. 1.2.6. Proveedores de servicios de pago que ofrecen cuentas de pago (PSPCP). 1. 1.2.7. Proveedores de servicios de pago que cumplen la función de iniciaci ón (PSI) y prestan el servicio de billetera digital. C uando un tercero desarrolle tareas relativas a servicios ofrecidos por los sujetos oblig a- dos o en su nombre, ambos serán responsables por el cumplimiento de las presentes normas. Lo anterior deberá est ablecerse en los instrumentos que acuerden la realización de dichas tareas. B.C.R.A. PROTECCIÓN DE LOS USUARIOS DE SERVICIOS FINANCIEROS Sección 1. Disposiciones generales. Versión: 8a. COMUNICACIÓN  “A”  7744 Vigencia: 28/02/2023 Página 1

**Exterior y Cambios, Punto 1.1:**
[TO_exterior_cambios_actual.pdf · Punto/Sección 1.1 (PDF pág 7)]
> 1.1. En todas las operaciones de cambio, canje y /o arbitraje que se cursen por el mercado libre de  cambios, establecido por el artículo 1° del Decreto 260/02 según el texto establecido por el  artículo 132 de la Ley 27.444, en adelante “mercado de cambios”, deberán intervenir  entidades financieras o camb iarias autorizadas a operar en cambios por el Banco Central de  la República Argentina (BCRA), en adelante “entidades”.  1.2. Las entidades podrán dar acceso al mercado de cambios a las personas hum anas o jurídicas  y los patrimonios y otras universalidades,  en adelante “clientes”, cuando verifiquen el  cumplimiento de las disposiciones generales y, en caso de corresponder, aquellas específicas  previstas para el concepto pertinente en el presente texto ordenado.  En todos los casos, la entidad deberá contar co n los elementos que le permitan constatar el  carácter genuino de la operación a cursar y su correcto encuadramiento en el concepto  declarado.  1.3. Las operaciones de cambio serán realizadas al tip o de cambio que sea libremente pactado  entre las partes.  1.4. Por cada operación de cambio, canje y/o arbitraje, las entidades deberán realizar un boleto de  compra y/o venta de cambio, según corresponda, conforme a lo estipulado en el punto 5.3.  1.5. Los incumplimientos a esta normativa se encontrarán alcanzados  por la Ley del Régimen  Penal Cambiario.  1.6. Las en

### 6. ADJUDICACIÓN (Agustina):
```
Adjudicación de la autora, 2026-07-13, asistida por revisión.

- pata / claim: Pata 2 — "Si un operador de cambio debe intervenir como entidad autorizada en el mercado de cambios"
- sintoma_capa1: context_recall        causa_capa2: alcanzabilidad_kg
- primaria/secundaria: PRIMARIA
- evidencia (1 línea): Los portadores de la regla de Exterior 1.1 existen
  (intervencion_de_entidades_autorizadas_en_operaciones_de_camb,
  entidades_financieras_o_cambiarias_autorizadas__agencia_cambio,
  entidades_autorizadas_a_operar_en_cambios__otra) pero ninguno apareció en las búsquedas
  del agente (pasos 3/12/15, re-ejecutados determinísticamente); por la regla de precedencia,
  el nodo entidad_operadora usado para rellenar no cuenta como contexto de la pata.

- pata / claim: Pata 2 — claim central "Los operadores de cambio son entidades financieras autorizadas a operar en el mercado de cambios"
- sintoma_capa1: faithfulness        causa_capa2: alucinacion_agente (modo b)
- primaria/secundaria: SECUNDARIA
- evidencia (1 línea): Ningún nodo consultado ni el PDF lo afirman (Exterior 1.1: "financieras
  o cambiarias"). Atenuante documentado: el grafo aportó ingredientes (type EntidadFinanciera
  del nodo operador_de_cambio__agencia_cambio; nodo entidad_operadora defectuoso).

- pata / claim: Pata 2 — claim "Existen entidades denominadas 'entidades operadoras en mercado de cambios' que son entidades financieras autorizadas a operar en el mercado de cambios local"
- sintoma_capa1: noise_sensitivity        causa_capa2: contenido_kg
- primaria/secundaria: SECUNDARIA
- evidencia (1 línea): Soportado por entidad_operadora_en_mercado_de_cambios__otra, cuyo
  contenido omite "o cambiarias" (contra Exterior 1.1) y cuya provenance (Punto 3.16) no
  funda el contenido (verificado: el 3.16 es requisitos de egresos/ARCA).

- pata / claim: Pata 1 — claim de la enumeración de sujetos obligados
- sintoma_capa1: —        causa_capa2: — (FALSO POSITIVO DEL JUEZ, sin par — la pata 1 no tiene defecto en su núcleo)
- primaria/secundaria: —
- evidencia (1 línea): Soportado por el nodo sujeto_obligado (abierto en el paso 13) y
  correcto contra Protección 1.1.2.x.

- pata / claim: Pata 1 — las 4 glosas de obligaciones (información clara, trato equitativo, acceso igualitario, resolución de reclamos)
- sintoma_capa1: faithfulness        causa_capa2: alucinacion_agente (modo a)
- primaria/secundaria: SECUNDARIA
- evidencia (1 línea): Sin soporte en los nodos abiertos por el agente; el grafo las porta en
  nodos alcanzables por label (trato_equitativo_y_digno, derecho_a_informacion_clara_y_suficiente,
  acceso_igualitario_a_servicios_financieros, consideracion_y_resolucion_fundada_de_reclamos)
  que el agente no consultó — exhibibles.
```

---

## Caso off/run_1/CQ-020

### 1. Pregunta (verbatim eval_set_v1) y patas (judge.step1.patas_de_la_pregunta)

> ¿Cómo se calcula la exigencia de capital por riesgo de crédito (CRC) y con qué frecuencia se reporta al BCRA?

- Categoría: `multi_norma` · TOs fuente: capitales, regimen
- Ground-truth secciones: Capitales, Punto 2.1 · Régimen Informativo, Punto 3.1.2 · Régimen Informativo, Punto 1.1 (frecuencia)
- Pata 1: "Cómo se calcula la exigencia de capital por riesgo de crédito (CRC)"
- Pata 2: "Con qué frecuencia se reporta la CRC al BCRA"

### 2. Claims con veredicto negativo del juez (verbatim)
- [no_soportado] CENTRAL — «El Factor k toma valores en una escala entre 1 y 1,19»
- [no_soportado] CENTRAL — «El Factor k es asignado por SEFyC»
- [no_soportado] CENTRAL — «Los APRC se determinan mediante la suma de valores aplicando una expresión específica con ponderadores de crédito»
- [no_soportado] CENTRAL — «INC es el Incremento de exigencia por riesgo de crédito por excesos en participaciones en capital de empresas»
- [no_soportado] CENTRAL — «El reporte se realiza a través del Régimen Informativo Contable Mensual (R.I.-C.M.)»
- [no_soportado] secundaria — «El R.I.-C.M. es un proceso de información periódica mensual obligatoria»
- [no_soportado] secundaria — «A través del R.I.-C.M. las entidades financieras reportan indicadores de negocio y componentes al BCRA»
- [no_soportado] secundaria — «El R.I.-C.M. incluye datos sobre exigencia e integración de capitales mínimos»
- cobertura_patas: [{"pata": "Cómo se calcula la exigencia de capital por riesgo de crédito (CRC)", "cobertura": "cubierta"}, {"pata": "Con qué frecuencia se reporta la CRC al BCRA", "cobertura": "cubierta"}]

### 3. Trayectoria del agente (tool calls, rep 1)
- paso 1 · `buscar_nodos` · input: `{"consulta": "exigencia capital riesgo crédito CRC cálculo", "limite": 10}`
  → {"consulta": "exigencia capital riesgo crédito CRC cálculo", "total_con_match": 544, "resultados": [{"id": "req_exigencia_de_capital_por_riesgo_de_credito_crc", …(no-JSON)
- paso 2 · `buscar_nodos` · input: `{"consulta": "capital riesgo crédito reporte BCRA frecuencia", "limite": 10}`
  → {"consulta": "capital riesgo crédito reporte BCRA frecuencia", "total_con_match": 563, "resultados": [{"id": "req_capital_minimo_por_riesgo_de_credito", "type": …(no-JSON)
- paso 3 · `ver_nodo` · input: `{"id": "req_exigencia_de_capital_por_riesgo_de_credito_crc"}`
  → nodo req_exigencia_de_capital_por_riesgo_de_credito_crc (Exigencia de capital por riesgo de crédito (CRC)) — contenido íntegro abajo (§4)
- paso 4 · `ver_vecinos` · input: `{"id": "req_exigencia_de_capital_por_riesgo_de_credito_crc", "direccion": "ambas"}`
  → salientes=2 entrantes=1 → utiliza→req_factor_k; utiliza→con_activos_ponderados_por_riesgo_de_credito_aprc
- paso 5 · `buscar_nodos` · input: `{"consulta": "reporte mensual capital riesgo crédito BCRA frecuencia", "limite": 10}`
  → {"consulta": "reporte mensual capital riesgo crédito BCRA frecuencia", "total_con_match": 574, "resultados": [{"id": "req_capital_minimo_por_riesgo_de_credito", …(no-JSON)
- paso 6 · `buscar_nodos` · input: `{"consulta": "régimen informativo capital mínimo riesgo crédito", "limite": 10}`
  → {"consulta": "régimen informativo capital mínimo riesgo crédito", "total_con_match": 595, "resultados": [{"id": "req_capital_minimo_por_riesgo_de_credito", "typ …(no-JSON)
- paso 7 · `ver_nodo` · input: `{"id": "rep_disminucion_de_la_exigencia_de_capital_minimo_por_riesgo_de_credito"}`
  → nodo rep_disminucion_de_la_exigencia_de_capital_minimo_por_riesgo_de_credito (Disminución de la exigencia de capital mínimo por riesgo de crédito) — contenido íntegro abajo (§4)
- paso 8 · `buscar_nodos` · input: `{"consulta": "régimen informativo mensual BCRA", "limite": 5}`
  → {"consulta": "régimen informativo mensual BCRA", "total_con_match": 112, "resultados": [{"id": "ins_regimen_informativo_contable_mensual", "type": "INSTRUMENT", …(no-JSON)
- paso 9 · `ver_nodo` · input: `{"id": "ins_regimen_informativo_contable_mensual"}`
  → nodo ins_regimen_informativo_contable_mensual (Régimen Informativo Contable Mensual) — contenido íntegro abajo (§4)
- paso 10 · `ver_nodo` · input: `{"id": "rep_regimen_informativo_contable_mensual_sobre_capitales_minimos"}`
  → nodo rep_regimen_informativo_contable_mensual_sobre_capitales_minimos (Régimen Informativo Contable Mensual sobre Capitales Mínimos) — contenido íntegro abajo (§4)
- paso 11 · `ver_nodo` · input: `{"id": "req_factor_k"}`
  → nodo req_factor_k (Factor k) — contenido íntegro abajo (§4)
- paso 12 · `ver_nodo` · input: `{"id": "con_activos_ponderados_por_riesgo_de_credito_aprc"}`
  → nodo con_activos_ponderados_por_riesgo_de_credito_aprc (Activos ponderados por riesgo de crédito (APRC)) — contenido íntegro abajo (§4)
- **Respuesta final:** «La exigencia de capital por riesgo de crédito (CRC) se calcula mediante la siguiente fórmula: CRC = (k × 0,08 × APRC) + INC, donde: (1) k es el Factor k, un ponderador vinculado a la calificación de la entidad según una escala de valores entre 1 y 1,19, asignado por SEFyC; (2) 0,08 es un factor fijo; (3) APRC son los Activos Ponderados por Riesgo de Crédito, determinados mediante la suma de valores aplicando una expresión específica con ponderadores de crédito; e (4) INC es el Incremento de exigencia por riesgo de crédito por excesos en participaciones en capital de empresas. La fórmula se determina según la calificación de la entidad. En cuanto a la frecuencia de reporte, la exigencia de capital por riesgo de crédito se reporta al BCRA de forma mensual, a través del Régimen Informativo Contable Mensual (R.I.-C.M.), que es un proceso de información periódica mensual obligatoria mediante el cual las entidades financieras reportan indicadores de negocio y componentes al BCRA, incluyendo datos sobre exigencia e integración de capitales mínimos.»
- **Citas:** [{"source_doc": "TO_capitales_minimos_actual.pdf", "location": "pp. 6-7"}, {"source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf", "location": "p. 4"}, {"source_doc": "TO_capitales_minimos_actual.pdf", "location": "p. 194"}]

### 4. Nodos abiertos con `ver_nodo` — contenido ÍNTEGRO (kg.json congelado)

**req_exigencia_de_capital_por_riesgo_de_credito_crc**:
```json
{
 "id": "req_exigencia_de_capital_por_riesgo_de_credito_crc",
 "type": "REQUIREMENT",
 "label": "Exigencia de capital por riesgo de crédito (CRC)",
 "properties": {
  "version": "A 8418",
  "description": "Fórmula de cálculo: CRC = (k × 0,08 × APRC) + INC, determinada según calificación de la entidad.",
  "aliases": [
   "Exigencia de capital por riesgo de crédito (CRC)"
  ],
  "source_to": "capitales_minimos",
  "mention_count": 1
 },
 "provenance": {
  "source_doc": "TO_capitales_minimos_actual.pdf",
  "location": "pp. 6-7"
 }
}
```

**rep_disminucion_de_la_exigencia_de_capital_minimo_por_riesgo_de_credito**:
```json
{
 "id": "rep_disminucion_de_la_exigencia_de_capital_minimo_por_riesgo_de_credito",
 "type": "REPORT_ITEM",
 "label": "Disminución de la exigencia de capital mínimo por riesgo de crédito",
 "properties": {
  "version": "A 6561",
  "description": "Código 60100000 que registra disminuciones en el requerimiento de capital mínimo por riesgo de crédito en el régimen informativo mensual.",
  "aliases": [
   "Disminución de la exigencia de capital mínimo por riesgo de crédito"
  ],
  "source_to": "regimen_informativo_cm",
  "mention_count": 1
 },
 "provenance": {
  "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
  "location": "p. 36"
 }
}
```

**ins_regimen_informativo_contable_mensual**:
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
  "mention_count": 6,
  "other_locations": [
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
 },
 "provenance": {
  "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
  "location": "p. 4"
 }
}
```

**rep_regimen_informativo_contable_mensual_sobre_capitales_minimos**:
```json
{
 "id": "rep_regimen_informativo_contable_mensual_sobre_capitales_minimos",
 "type": "REPORT_ITEM",
 "label": "Régimen Informativo Contable Mensual sobre Capitales Mínimos",
 "properties": {
  "version": "A 8418",
  "description": "Esquema informativo (R.I.-C.M.) que regula la presentación de datos sobre exigencia e integración de capitales mínimos.",
  "aliases": [
   "Régimen Informativo Contable Mensual sobre Capitales Mínimos"
  ],
  "source_to": "capitales_minimos",
  "mention_count": 1
 },
 "provenance": {
  "source_doc": "TO_capitales_minimos_actual.pdf",
  "location": "p. 194"
 }
}
```

**req_factor_k**:
```json
{
 "id": "req_factor_k",
 "type": "REQUIREMENT",
 "label": "Factor k",
 "properties": {
  "version": "A 8418",
  "description": "Ponderador vinculado a calificación de entidad según escala (valores 1 a 1,19), asignado por SEFyC.",
  "aliases": [
   "Factor k"
  ],
  "source_to": "capitales_minimos",
  "mention_count": 1
 },
 "provenance": {
  "source_doc": "TO_capitales_minimos_actual.pdf",
  "location": "pp. 6-7"
 }
}
```

**con_activos_ponderados_por_riesgo_de_credito_aprc**:
```json
{
 "id": "con_activos_ponderados_por_riesgo_de_credito_aprc",
 "type": "CONCEPT",
 "label": "Activos ponderados por riesgo de crédito (APRC)",
 "properties": {
  "version": "A 8418",
  "description": "Activos determinados mediante suma de valores aplicando expresión específica con ponderadores de crédito.",
  "aliases": [
   "Activos ponderados por riesgo de crédito (APRC)",
   "Activos ponderados por riesgo de crédito (APRc)"
  ],
  "source_to": "capitales_minimos",
  "mention_count": 2,
  "other_locations": [
   {
    "source_doc": "TO_capitales_minimos_actual.pdf",
    "location": "p. 168"
   }
  ]
 },
 "provenance": {
  "source_doc": "TO_capitales_minimos_actual.pdf",
  "location": "pp. 6-7"
 }
}
```

### 5. Pasaje(s) del PDF — secciones ground-truth (máx ~1.500 chars por pata)

**Capitales, Punto 2.1:**
[TO_capitales_minimos_actual.pdf · Punto/Sección 2.1 (PDF pág 2)]
> 2.1. Exigencia. 2.2. Exclusiones. 2.3. Cómputo de los conceptos comprendidos. 2.4. Requisitos de debida diligencia. 2.5. Criterios para la determinación de los activos ponderados por riesgo. 2.6. Exposiciones a entidades financieras. 2.7. Exposiciones a empresas. 2.8. Exposiciones minoristas. 2.9. Exposiciones con garantía hipotecaria. 2.10. Exposiciones en situación de incumplimiento. 2.11. Exposiciones a instrumentos. 2.12. Tabla de ponderadores de riesgo. 2.13. Partidas fuera de balance. Factores de conversión crediticia (CCF). Sección 3.   Capital mínimo por riesgo de crédito. Titulizaciones e inversiones en fondos. 3.1. Tratamiento de las titulizaciones. 3.2. Tratamiento de las posiciones en fondos. Sección 4.   Capital mínimo por riesgo de crédito de contraparte. 4.1. Exigencia de capital por riesgo de crédito de contraparte para operaciones DvP  fallidas y no DvP. 4.2. Exigencia de capital por riesgo de crédito de contraparte en operaciones con de- rivados –OTC o negociados en mercados regulados– y con liquidación diferida. 4.3. Exigencia de capital por riesgo de crédito de contraparte en operaciones con en- tidades de contraparte central. Sección 5.   Cobertura del riesgo de crédito. 5.1. Técnicas de cobertura del riesgo de crédito. 5.2. Requisitos para la aplicación de técnicas de coberturas del riesgo de crédito. 5.3. Operaciones cubiertas con activos admitidos como g

**Régimen Informativo, Punto 3.1.2:**
[TO_regimen_informativo_contable_mensual_actual.pdf · Punto/Sección 3.1.2 (PDF pág 5)]
> 3.1.2. Cálculo de la exigencia.  Se determinará de acuerdo con la siguiente expresión:  CRC = (k x 0,08 x APRc) + INC  donde:  CRC = exigencia de capital por riesgo de crédito.  k = factor vinculado a la calificación asignada a la entidad teniendo en cuenta la es- cala prevista en el punto 2.1. de las normas sobre “Capitales  mínimos de las entida- des financieras”.  APRc = activos ponderados por riesgo de crédito calculados conforme a la siguiente  fórmula:  APRc = A x p + PFB x CCF x p + no DVP + (DVP + RCD + INC (Inv. signif. en emp.)) x 12,5  donde:   A: activos computables /exposiciones -saldos de deuda-.  A efectos de la determinación d e los importes a computar, se tendrán en cuenta las  disposiciones contenidas en las Secciones 2. a 5. y en el punto 11.5.,  de las normas  sobre “Capitales mínimos de las entidades financieras”,  incluyendo en su caso los  ajustes por aplicación de las NIIF.   Solo para las partidas 12100000 y 1222000/CCF, se permitirá la asignación de un  ponderador de riesgo específico que surja de los cálculos previstos en los puntos 3.1  y 3.2. de las normas sobre “Capitales mínimos de las entidades financieras”.  Si como resultado del proceso de debida diligencia  llevado a cabo por las enti- dades financieras del grupo 1 , surgen ponderadores mayores a los estableci- dos normativamente, deberán aplicar el mayor de amb os, previa comunicación  a la S

**Régimen Informativo, Punto 1.1 (frecuencia):**
[TO_regimen_informativo_contable_mensual_actual.pdf · Punto/Sección 1.1 (PDF pág 3)]
> 1.1. La información tendrá frecuencia mensual y se integrará con datos referidos al mes bajo aná- lisis, excepto las siguientes informaciones que tendrán frecuencia trimestral y se integrarán de  la siguiente manera:  Con los datos correspondientes al último mes de cada trimestre (marzo, junio, septiembre y  diciembre):  - Datos complementarios vinculados al cálculo de la exigencia por riesgo de mercado (puntos 4.3., 4.4. y 4.5. de la Sección 4.) en base individual y consolidado mensual (códigos de con- solidación 0 o 1 y 2); - La información sobre Ratio de apalancamiento (Sección 10.) en base individual (códigos de consolidación 0 o 1); Con los datos correspondientes al mes siguiente de cada trimestre (abril, julio, octubre  y enero)  - Cálculo del riesgo de tasa de interés en la cartera de inversión - Medida de riesgo EVE es- tandarizada (Sección 11.) en base individual y consolidado mensual (códigos de consolida- ción 0 o 1 y 2) y su respectivo total de control (partida 70500000). 1.2. Los importes se registrarán en miles de pesos, sin decimales.  A los fines del redondeo de las magnitudes se incrementarán los valores en una unidad  cuando el primer dígito de las fracciones sea igual o mayor que 5, desechando estas últimas  si resultan inferiores.  Los importes en moneda extranjera se convertirán a pesos utilizando el tipo de cambio de re- ferencia publicado por el BCRA para

### 6. ADJUDICACIÓN (Agustina):
```
Adjudicación de la autora, 2026-07-13, asistida por revisión.

- pata / claim: Pata 1 (cálculo) — claim central "INC es el Incremento de exigencia por riesgo de crédito por excesos en participaciones en capital de empresas"
- sintoma_capa1: noise_sensitivity        causa_capa2: contenido_kg
- primaria/secundaria: PRIMARIA
- evidencia (1 línea): El claim reproduce casi verbatim el label del nodo
  req_incremento_de_exigencia_por_riesgo_de_credito_por_excesos_en_participaciones_en_capital_de_empresas_inc,
  visible en los resultados del paso 1 (re-ejecutado determinísticamente: 5º resultado);
  ese label conflata INC(inversiones significativas, límites 15%/60% dentro de APRC) con el
  INC de la fórmula CRC (excesos en activos inmovilizados etc., Capitales 2.1) — soporte
  infiel al PDF.

- pata / claim: Los otros 7 claims negativos (k escala 1-1,19; k asignado por SEFyC; APRC suma con ponderadores; reporte vía R.I.-C.M.; y las 3 secundarias del R.I.-C.M.)
- sintoma_capa1: —        causa_capa2: — (FALSOS POSITIVOS DEL JUEZ, sin par — no es defecto del sistema)
- primaria/secundaria: —
- evidencia (1 línea): Soportados por los nodos abiertos (req_factor_k,
  con_activos_ponderados_por_riesgo_de_credito_aprc, ins_regimen_informativo_contable_mensual,
  rep_regimen_informativo_contable_mensual_sobre_capitales_minimos) y correctos contra el PDF
  (Capitales 2.1: escala k 1/1,03/1,08/1,13/1,19, calificación SEFYC, expresión de APRC;
  Régimen 1.1: frecuencia mensual por defecto).

- pata / claim: Pata 2 (frecuencia) — "mensual vía R.I.-C.M."
- sintoma_capa1: —        causa_capa2: — (sin defecto)
- primaria/secundaria: —
- evidencia (1 línea): Soportado por ins_regimen_informativo_contable_mensual (abierto en el
  paso 9) y correcto contra Régimen 1.1 (la exigencia por riesgo de crédito no está en las
  excepciones trimestrales).
```

---

## Caso on/run_1/CQ-019

### 1. Pregunta (verbatim eval_set_v1) y patas (judge.step1.patas_de_la_pregunta)

> Al computar los activos para la exigencia de capital por riesgo de crédito, ¿qué previsión por incobrabilidad no se deduce, y cómo se vincula esa regla con la clasificación de deudores?

- Categoría: `multi_norma` · TOs fuente: capitales, clasificacion
- Ground-truth secciones: Capitales, Punto 2.3.1 · Clasificación, Puntos 6.5.1 y 7.2.1
- Pata 1: "Qué previsión por incobrabilidad no se deduce al computar los activos para la exigencia de capital por riesgo de crédito"
- Pata 2: "Cómo se vincula esa regla con la clasificación de deudores"

### 2. Claims con veredicto negativo del juez (verbatim)
- [no_soportado] secundaria — «La provisión específica para cartera clasificada como situación normal debe absorberse antes de la deducción de otros conceptos deducibles del capital.»
- [no_soportado] secundaria — «La categoría 'situación normal' corresponde a clientes que demuestran capacidad de atender adecuadamente todos sus compromisos financieros.»
- [falso] secundaria — «La previsión por riesgo de incobrabilidad sí se deduce para activos cubiertos con garantías preferidas A.»
- cobertura_patas: [{"pata": "Qué previsión por incobrabilidad no se deduce al computar los activos para la exigencia de capital por riesgo de crédito", "cobertura": "cubierta"}, {"pata": "Cómo se vincula esa regla con la clasificación de deudores", "cobertura": "cubierta"}]

### 3. Trayectoria del agente (tool calls, rep 1)
- paso 1 · `buscar_nodos` · input: `{"consulta": "exigencia capital riesgo crédito previsión incobrabilidad", "limite": 10}`
  → {"consulta": "exigencia capital riesgo crédito previsión incobrabilidad", "total_con_match": 542, "resultados": [{"id": "req_exigencia_de_capital_por_riesgo_de_ …(no-JSON)
- paso 2 · `buscar_nodos` · input: `{"consulta": "clasificación deudores categorías", "limite": 10}`
  → {"consulta": "clasificación deudores categorías", "total_con_match": 62, "resultados": [{"id": "ope_clasificacion_de_deudores", "type": "OPERATION", "label": "C …(no-JSON)
- paso 3 · `ver_nodo` · input: `{"id": "req_exigencia_de_capital_por_riesgo_de_credito_crc"}`
  → nodo req_exigencia_de_capital_por_riesgo_de_credito_crc (Exigencia de capital por riesgo de crédito (CRC)) — contenido íntegro abajo (§4)
- paso 4 · `ver_nodo` · input: `{"id": "req_prevision_por_riesgo_de_incobrabilidad"}`
  → nodo req_prevision_por_riesgo_de_incobrabilidad (Previsión por riesgo de incobrabilidad) — contenido íntegro abajo (§4)
- paso 5 · `buscar_nodos` · input: `{"consulta": "activos ponderados riesgo crédito APRC deducción previsión", "limite": 10}`
  → {"consulta": "activos ponderados riesgo crédito APRC deducción previsión", "total_con_match": 459, "resultados": [{"id": "con_activos_ponderados_por_riesgo_de_c …(no-JSON)
- paso 6 · `ver_vecinos` · input: `{"id": "req_exigencia_de_capital_por_riesgo_de_credito_crc"}`
  → salientes=2 entrantes=1 → utiliza→req_factor_k; utiliza→con_activos_ponderados_por_riesgo_de_credito_aprc
- paso 7 · `ver_nodo` · input: `{"id": "con_activos_ponderados_por_riesgo_de_credito_aprc"}`
  → nodo con_activos_ponderados_por_riesgo_de_credito_aprc (Activos ponderados por riesgo de crédito (APRC)) — contenido íntegro abajo (§4)
- paso 8 · `ver_vecinos` · input: `{"id": "con_activos_ponderados_por_riesgo_de_credito_aprc"}`
  → salientes=0 entrantes=2 → 
- paso 9 · `buscar_nodos` · input: `{"consulta": "previsión general específica deducción activos normal observación", "limite": 10}`
  → {"consulta": "previsión general específica deducción activos normal observación", "total_con_match": 141, "resultados": [{"id": "req_prevision_especifica", "typ …(no-JSON)
- paso 10 · `ver_nodo` · input: `{"id": "req_prevision_por_riesgo_de_incobrabilidad_en_cartera_en_situacion_normal"}`
  → nodo req_prevision_por_riesgo_de_incobrabilidad_en_cartera_en_situacion_normal (Previsión por riesgo de incobrabilidad en cartera en situación normal) — contenido íntegro abajo (§4)
- paso 11 · `ver_vecinos` · input: `{"id": "req_prevision_por_riesgo_de_incobrabilidad_en_cartera_en_situacion_normal"}`
  → salientes=0 entrantes=2 → 
- paso 12 · `buscar_nodos` · input: `{"consulta": "previsión activos brutos neto descuento garantías preferidas", "limite": 10}`
  → {"consulta": "previsión activos brutos neto descuento garantías preferidas", "total_con_match": 174, "resultados": [{"id": "con_garantias_preferidas", "type": " …(no-JSON)
- paso 13 · `buscar_nodos` · input: `{"consulta": "activos brutos menos previsión general específica calculado neto", "limite": 10}`
  → {"consulta": "activos brutos menos previsión general específica calculado neto", "total_con_match": 153, "resultados": [{"id": "req_prevision_especifica", "type …(no-JSON)
- paso 14 · `ver_nodo` · input: `{"id": "req_prevision_especifica"}`
  → nodo req_prevision_especifica (previsión específica) — contenido íntegro abajo (§4)
- paso 15 · `ver_vecinos` · input: `{"id": "req_prevision_especifica"}`
  → salientes=1 entrantes=0 → afecta_cálculo_de→con_exigencia_de_capital_sobre_exposiciones_subyacentes_sin_titulizar_ksa
- **Respuesta final:** «Al computar los activos para la exigencia de capital por riesgo de crédito, la previsión por riesgo de incobrabilidad en cartera en situación normal es la que no se deduce. Según la regulación, esta provisión específica para cartera clasificada como situación normal debe absorberse antes de la deducción de otros conceptos deducibles del capital. Esta regla se vincula directamente con la clasificación de deudores: la previsión no deducible corresponde específicamente a los activos clasificados en la categoría de 'situación normal' (donde el cliente demuestra capacidad de atender adecuadamente todos sus compromisos financieros). En contraste, la previsión por riesgo de incobrabilidad sí se deduce para activos clasificados en otras categorías de riesgo o cuando están cubiertos con garantías preferidas A.»
- **Citas:** [{"source_doc": "TO_capitales_minimos_actual.pdf", "location": "p. 162"}, {"source_doc": "TO_capitales_minimos_actual.pdf", "location": "p. 10"}, {"source_doc": "TO_clasificacion_deudores_actual.pdf", "location": "pp. 5-6"}]

### 4. Nodos abiertos con `ver_nodo` — contenido ÍNTEGRO (kg.json congelado)

**req_exigencia_de_capital_por_riesgo_de_credito_crc**:
```json
{
 "id": "req_exigencia_de_capital_por_riesgo_de_credito_crc",
 "type": "REQUIREMENT",
 "label": "Exigencia de capital por riesgo de crédito (CRC)",
 "properties": {
  "version": "A 8418",
  "description": "Fórmula de cálculo: CRC = (k × 0,08 × APRC) + INC, determinada según calificación de la entidad.",
  "aliases": [
   "Exigencia de capital por riesgo de crédito (CRC)"
  ],
  "source_to": "capitales_minimos",
  "mention_count": 1
 },
 "provenance": {
  "source_doc": "TO_capitales_minimos_actual.pdf",
  "location": "pp. 6-7"
 }
}
```

**req_prevision_por_riesgo_de_incobrabilidad**:
```json
{
 "id": "req_prevision_por_riesgo_de_incobrabilidad",
 "type": "REQUIREMENT",
 "label": "Previsión por riesgo de incobrabilidad",
 "properties": {
  "version": "A 8418",
  "description": "Deducción por deterioro de activos clasificados en situación normal o cubiertos con garantías preferidas A.",
  "aliases": [
   "Previsión por riesgo de incobrabilidad"
  ],
  "source_to": "capitales_minimos",
  "mention_count": 2,
  "other_locations": [
   {
    "source_doc": "TO_clasificacion_deudores_actual.pdf",
    "location": "pp. 5-6"
   }
  ]
 },
 "provenance": {
  "source_doc": "TO_capitales_minimos_actual.pdf",
  "location": "p. 10"
 }
}
```

**con_activos_ponderados_por_riesgo_de_credito_aprc**:
```json
{
 "id": "con_activos_ponderados_por_riesgo_de_credito_aprc",
 "type": "CONCEPT",
 "label": "Activos ponderados por riesgo de crédito (APRC)",
 "properties": {
  "version": "A 8418",
  "description": "Activos determinados mediante suma de valores aplicando expresión específica con ponderadores de crédito.",
  "aliases": [
   "Activos ponderados por riesgo de crédito (APRC)",
   "Activos ponderados por riesgo de crédito (APRc)"
  ],
  "source_to": "capitales_minimos",
  "mention_count": 2,
  "other_locations": [
   {
    "source_doc": "TO_capitales_minimos_actual.pdf",
    "location": "p. 168"
   }
  ]
 },
 "provenance": {
  "source_doc": "TO_capitales_minimos_actual.pdf",
  "location": "pp. 6-7"
 }
}
```

**req_prevision_por_riesgo_de_incobrabilidad_en_cartera_en_situacion_normal**:
```json
{
 "id": "req_prevision_por_riesgo_de_incobrabilidad_en_cartera_en_situacion_normal",
 "type": "REQUIREMENT",
 "label": "Previsión por riesgo de incobrabilidad en cartera en situación normal",
 "properties": {
  "version": "A 8418",
  "description": "Provisión específica para cartera clasificada como situación normal que debe absorberse antes de deducción de conceptos.",
  "aliases": [
   "Previsión por riesgo de incobrabilidad - cartera en situación normal"
  ],
  "source_to": "capitales_minimos",
  "mention_count": 1
 },
 "provenance": {
  "source_doc": "TO_capitales_minimos_actual.pdf",
  "location": "p. 162"
 }
}
```

**req_prevision_especifica**:
```json
{
 "id": "req_prevision_especifica",
 "type": "REQUIREMENT",
 "label": "previsión específica",
 "properties": {
  "version": "A 8418",
  "description": "Descuento contable constituido sobre una exposición que debe ser excluido del cálculo bruto de KSA.",
  "aliases": [
   "previsión específica"
  ],
  "source_to": "capitales_minimos",
  "mention_count": 1
 },
 "provenance": {
  "source_doc": "TO_capitales_minimos_actual.pdf",
  "location": "p. 42"
 }
}
```

### 5. Pasaje(s) del PDF — secciones ground-truth (máx ~1.500 chars por pata)

**Capitales, Punto 2.3.1:**
[TO_capitales_minimos_actual.pdf · Punto/Sección 2.3.1 (PDF pág 10)]
> 2.3.1. Bases individual y consolidada mensual. Los conceptos comprendidos se computarán sobre la base de los saldos al último día de cada mes (capitales, intereses, primas, actualizaciones –por el Coeficiente de Estabilización de Referencia CER– y diferencias de cotización, según corresponda, netos de las previsiones por riesgos de incobrabilidad  –incluyendo, de corresponder, las previsiones contabilizadas en el pasivo – y desvalorización y de las depreciaci ones y amortizaciones acumuladas que  les sean atribuibles y demás cuentas regulariz adoras, sin deducir el 100% del importe de la previsión por riesgo de incobrabilidad correspondiente a la cartera de deudores clasificados “en situación normal” –puntos 6.5.1. y 7.2.1. del TO sobre Clasificaci ón de Deudores– y a las financiaciones que se encuentran cubiertas con garantías preferidas A). 2.3.2. Base consolidada trimestral. Se considerarán los saldos al cierre del trimestre, aplicando en los demás aspectos las correspondientes disposiciones establecidas. 2.4. Requisitos de debida diligencia. Las entidades financieras del grupo 1 deberán llevar a cabo un proceso de debida diligencia –al momento del otorgamiento del crédito y con frecuencia mínima anual– a fin de que puedan con- tar con una adecuada comprensión del perfil de riesgo y las características de sus contrapartes. El grado de sofisticación de las evaluaciones de deb

**Clasificación, Puntos 6.5.1 y 7.2.1:**
[TO_clasificacion_deudores_actual.pdf · Punto 6.5.1 (localize=fallida; mejor ocurrencia cruda, PDF pág 46, prose_score=-76)]
> 6.5.1. “A” 2216 I I.d.1. Según Com. “A” 2932 (punto 1 6.), 3339 y  5671.  6.5.1.1. “A” 2216 I I.d.1.a) Según Com. “A” 3955 y 6639.  6.5.1.2. “A” 2216 I I.d.1.b) Según Com. “A” 3339.  6.5.1.3. “A” 2216 I I.d.1.c) 6.5.1.4. “A” 2216 I I.d.1.d) Según Com. “A” 2932 (punto 5.).  6.5.1.5. “A” 2216 I I.d.1.e) 6.5.1.6. “A” 2216 I I.d.1.f) Según Com. “A” 3339.  6.5.2. “A” 2216 I I.d.2. Según Com. “A” 3339.  6.5.2.1. “A” 2216 I I.d.2. 1°, 2°  y 3°  Según Com. “A” 3339. i) “A” 2216 I I.d.2.a) Según Com. “A” 3339 y 3955.  ii) “A” 2216 I.d.2.b) Según Com. “A” 3339 y 6639.  iii) “A” 2216 I I.d.2.c) Según Com. “A” 3339.
[TO_clasificacion_deudores_actual.pdf · Punto/Sección 7.2.1 (PDF pág 35)]
> 7.2.1. Situación normal.  Comprende los clientes que atienden en forma puntual el pago de sus obligaciones o con  atrasos que no superan los 31 días.  Los adelantos transitorios en cuenta corriente se considerarán de cumplimiento normal  hasta los 61 días contados desde su otorgamiento.  A los fines de establecer los días de atraso, en el caso de las financiaciones instrumenta- das mediante tarjetas de crédito, se considerarán los que resulten luego de imputar el  pago mínimo exigido en cada liquidación a cancelar la deuda en orden decreciente de an- tigüedad.  Los deudores que hayan accedido a refinanciaciones de deudas encontrándose clasifica- dos en niveles inferiores, sólo podrán incluirse en esta categoría en la medida en que se  hayan observado las pautas establecidas para cada uno de los correspondientes niveles  y, además, que el resto de sus deudas reúnan las condiciones para que el cliente pueda  ser recategorizado en este nivel.  Los deudores que hayan refinanciado sus deudas, aun no habiendo incurrido en atrasos  en el pago de sus servicios, podrán permanecer en esta categoría, cuando hayan accedi- do, como máximo, a dos refinanciaciones, en el término de 12 meses, contados desde la  última refinanciación otorgada.  A esos efectos, no se considerará refinanciación la asistencia que se otorgue a los deu- dores clasificados en esta categoría siempre que implique mayor

### 6. ADJUDICACIÓN (Agustina):
```
Adjudicación de la autora, 2026-07-13, asistida por revisión.

- pata / claim: Claim "La previsión por riesgo de incobrabilidad sí se deduce para activos cubiertos con garantías preferidas A" [falso]
- sintoma_capa1: noise_sensitivity        causa_capa2: contenido_kg
- primaria/secundaria: PRIMARIA
- evidencia (1 línea): Soportado por req_prevision_por_riesgo_de_incobrabilidad ("Deducción por
  deterioro de activos... situación normal o cubiertos con garantías preferidas A"), cuyo
  contenido invierte el PDF (Capitales 2.3.1: "sin deducir el 100%... 'en situación normal'...
  y a las financiaciones que se encuentran cubiertas con garantías preferidas A" — ambas
  categorías son no-deducibles). Nota: ningún claim central falló; la primaria del caso
  descansa en la única secundaria [falso], decisión de la autora.

- pata / claim: Claim "La categoría 'situación normal' corresponde a clientes que demuestran capacidad de atender adecuadamente todos sus compromisos financieros" [no_soportado]
- sintoma_capa1: faithfulness        causa_capa2: alucinacion_agente (modo a)
- primaria/secundaria: SECUNDARIA
- evidencia (1 línea): Sin soporte en los nodos abiertos por el agente; el grafo SÍ porta la
  definición en un nodo exhibible y alcanzable por label —
  cla_situacion_normal_clasificacion_de_deudores ("Categoría de clasificación de deudores
  donde el cliente demuestra capacidad de atender adecuadamente todos sus compromisos
  financieros a través del análisis de flujo de fondos") — que el agente no consultó
  (barrido del 2026-07-13 como constancia).

- pata / claim: Claim "La provisión específica para cartera clasificada como situación normal debe absorberse antes de la deducción de otros conceptos deducibles del capital" [no_soportado]
- sintoma_capa1: —        causa_capa2: — (FALSO POSITIVO DEL JUEZ, sin par — no es defecto del sistema)
- primaria/secundaria: —
- evidencia (1 línea): Soportado casi verbatim por
  req_prevision_por_riesgo_de_incobrabilidad_en_cartera_en_situacion_normal (abierto por el
  agente en el paso 10) y correcto contra el PDF (Capitales, punto 8.4.1.1
  —conceptos deducibles del COn1—: "Previo a su deducción deberá absorberse el importe de la
  previsión por riesgo de incobrabilidad correspondiente a la cartera en 'situación normal'
  computado como patrimonio neto complementario (punto 8.2.3.3.).").
```

---

## Caso off/run_1/CQ-024

### 1. Pregunta (verbatim eval_set_v1) y patas (judge.step1.patas_de_la_pregunta)

> ¿Con qué periodicidad mínima debe clasificarse un deudor de cartera comercial cuyas financiaciones alcanzan el 5% o más de la RPC, y en qué casos la reevaluación debe ser inmediata?

- Categoría: `multi_norma` · TOs fuente: clasificacion
- Ground-truth secciones: Punto 6.3.1 (Periodicidad mínima) · Punto 6.4 (Reconsideración obligatoria, último párrafo)
- Pata 1: "Periodicidad mínima de clasificación de un deudor de cartera comercial cuyas financiaciones alcanzan el 5% o más de la RPC"
- Pata 2: "Casos en que la reevaluación debe ser inmediata"

### 2. Claims con veredicto negativo del juez (verbatim)
- [falso] CENTRAL — «La reevaluación debe ser inmediata cuando existe discrepancia de más de un nivel en clasificaciones y las financiaciones superan el 1% de la RPC.»
- [no_soportado] CENTRAL — «La reevaluación debe ser inmediata cuando se producen atrasos mayores a 31 días.»
- [no_soportado] secundaria — «Los atrasos mayores a 31 días generan reclasificación inmediata del deudor al nivel resultante de sumar días de atraso efectivo y atraso normativo.»
- cobertura_patas: [{"pata": "Periodicidad mínima de clasificación de un deudor de cartera comercial cuyas financiaciones alcanzan el 5% o más de la RPC", "cobertura": "cubierta"}, {"pata": "Casos en que la reevaluación debe ser inmediata", "cobertura": "cubierta"}]

### 3. Trayectoria del agente (tool calls, rep 1)
- paso 1 · `buscar_nodos` · input: `{"consulta": "clasificación deudor cartera comercial RPC periodicidad", "limite": 10}`
  → {"consulta": "clasificación deudor cartera comercial RPC periodicidad", "total_con_match": 154, "resultados": [{"id": "con_cartera_comercial", "type": "CONCEPT" …(no-JSON)
- paso 2 · `buscar_nodos` · input: `{"consulta": "reevaluación inmediata deudor comercial", "limite": 10}`
  → {"consulta": "reevaluación inmediata deudor comercial", "total_con_match": 56, "resultados": [{"id": "req_reevaluacion_inmediata_por_discrepancia_de_mas_de_un_n …(no-JSON)
- paso 3 · `ver_nodo` · input: `{"id": "req_periodicidad_minima_de_clasificacion_de_deudores"}`
  → nodo req_periodicidad_minima_de_clasificacion_de_deudores (periodicidad mínima de clasificación de deudores) — contenido íntegro abajo (§4)
- paso 4 · `ver_nodo` · input: `{"id": "req_reevaluacion_inmediata_por_discrepancia_de_mas_de_un_nivel_en_clasificaciones"}`
  → nodo req_reevaluacion_inmediata_por_discrepancia_de_mas_de_un_nivel_en_clasificaciones (reevaluación inmediata por discrepancia de más de un nivel en clasificaciones) — contenido íntegro abajo (§4)
- paso 5 · `ver_vecinos` · input: `{"id": "req_periodicidad_minima_de_clasificacion_de_deudores", "direccion": "ambas"}`
  → salientes=1 entrantes=0 → rige_la→prc_revision_de_cartera_comercial
- paso 6 · `buscar_nodos` · input: `{"consulta": "5% RPC financiaciones cartera comercial", "limite": 10}`
  → {"consulta": "5% RPC financiaciones cartera comercial", "total_con_match": 155, "resultados": [{"id": "con_cartera_comercial", "type": "CONCEPT", "label": "Cart …(no-JSON)
- paso 7 · `ver_nodo` · input: `{"id": "req_analisis_trimestral_de_clientes_con_financiaciones_que_alcanzan_el_5_o_mas_de_la_responsabilidad_patrimonial_computable"}`
  → nodo req_analisis_trimestral_de_clientes_con_financiaciones_que_alcanzan_el_5_o_mas_de_la_responsabilidad_patrimonial_computable (análisis trimestral de clientes con financiaciones que alcanzan el 5% o más de la responsabilidad patrimonial computable) — contenido íntegro abajo (§4)
- paso 8 · `ver_vecinos` · input: `{"id": "req_analisis_trimestral_de_clientes_con_financiaciones_que_alcanzan_el_5_o_mas_de_la_responsabilidad_patrimonial_computable", "direccion": "ambas"}`
  → salientes=1 entrantes=0 → es_parte_de→ope_clasificacion_de_deudores
- paso 9 · `ver_vecinos` · input: `{"id": "req_reevaluacion_inmediata_por_discrepancia_de_mas_de_un_nivel_en_clasificaciones", "direccion": "ambas"}`
  → salientes=0 entrantes=0 → 
- paso 10 · `buscar_nodos` · input: `{"consulta": "reevaluación inmediata casos situaciones", "limite": 10}`
  → {"consulta": "reevaluación inmediata casos situaciones", "total_con_match": 10, "resultados": [{"id": "req_reevaluacion_inmediata_por_discrepancia_de_mas_de_un_ …(no-JSON)
- paso 11 · `buscar_nodos` · input: `{"consulta": "reevaluación inmediata atrasos incumplimiento cambio clasificación", "limite": 10}`
  → {"consulta": "reevaluación inmediata atrasos incumplimiento cambio clasificación", "total_con_match": 138, "resultados": [{"id": "req_atrasos_superiores_al_ano_ …(no-JSON)
- paso 12 · `buscar_nodos` · input: `{"consulta": "reevaluación inmediata deudor cartera comercial casos", "limite": 15}`
  → {"consulta": "reevaluación inmediata deudor cartera comercial casos", "total_con_match": 100, "resultados": [{"id": "req_analisis_anual_de_los_demas_casos_de_ca …(no-JSON)
- paso 13 · `buscar_nodos` · input: `{"consulta": "cambio de clasificación reclasificación inmediata deudor", "limite": 15}`
  → {"consulta": "cambio de clasificación reclasificación inmediata deudor", "total_con_match": 2500, "resultados": [{"id": "con_clasificacion_de_deudor", "type": " …(no-JSON)
- paso 14 · `buscar_nodos` · input: `{"consulta": "reevaluación inmediata atrasos 90 días 180 días", "limite": 10}`
  → {"consulta": "reevaluación inmediata atrasos 90 días 180 días", "total_con_match": 101, "resultados": [{"id": "req_atrasos_de_hasta_180_dias", "type": "REQUIREM …(no-JSON)
- paso 15 · `ver_nodo` · input: `{"id": "req_atrasos_mayores_a_31_dias"}`
  → nodo req_atrasos_mayores_a_31_dias (Atrasos mayores a 31 días) — contenido íntegro abajo (§4)
- **Respuesta final:** «Para un deudor de cartera comercial cuyas financiaciones alcanzan el 5% o más de la Responsabilidad Patrimonial Computable (RPC), la periodicidad mínima de clasificación es trimestral. Esto significa que debe realizarse un análisis en el curso de cada trimestre calendario.

Los casos en los que la reevaluación debe ser inmediata incluyen:

1. Discrepancia de más de un nivel en clasificaciones: Cuando concurren condiciones de discrepancia de más de un nivel en clasificaciones y las financiaciones superan umbrales de 1% de responsabilidad patrimonial computable.

2. Atrasos mayores a 31 días: Genera reclasificación inmediata del deudor al nivel resultante de sumar días de atraso efectivo y atraso normativo.»
- **Citas:** [{"source_doc": "TO_clasificacion_deudores_actual.pdf", "location": "p. 18"}, {"source_doc": "TO_clasificacion_deudores_actual.pdf", "location": "p. 19"}, {"source_doc": "TO_clasificacion_deudores_actual.pdf", "location": "p. 38"}]

### 4. Nodos abiertos con `ver_nodo` — contenido ÍNTEGRO (kg.json congelado)

**req_periodicidad_minima_de_clasificacion_de_deudores**:
```json
{
 "id": "req_periodicidad_minima_de_clasificacion_de_deudores",
 "type": "REQUIREMENT",
 "label": "periodicidad mínima de clasificación de deudores",
 "properties": {
  "version": "A 8378",
  "description": "Frecuencia obligatoria con la que debe efectuarse la revisión y clasificación de deudores, con registro en el legajo del cliente.",
  "aliases": [
   "Periodicidad mínima de clasificación"
  ],
  "source_to": "clasificacion_deudores",
  "mention_count": 1
 },
 "provenance": {
  "source_doc": "TO_clasificacion_deudores_actual.pdf",
  "location": "p. 17"
 }
}
```

**req_reevaluacion_inmediata_por_discrepancia_de_mas_de_un_nivel_en_clasificaciones**:
```json
{
 "id": "req_reevaluacion_inmediata_por_discrepancia_de_mas_de_un_nivel_en_clasificaciones",
 "type": "REQUIREMENT",
 "label": "reevaluación inmediata por discrepancia de más de un nivel en clasificaciones",
 "properties": {
  "version": "A 8378",
  "description": "Obligación de recategorizar al cliente cuando concurren condiciones de discrepancia de más de un nivel en clasificaciones y las financiaciones superan umbrales de 1% de responsabilidad patrimonial computable.",
  "aliases": [
   "reevaluación inmediata",
   "discrepancia de más de un nivel"
  ],
  "source_to": "clasificacion_deudores",
  "mention_count": 2,
  "other_locations": [
   {
    "source_doc": "TO_clasificacion_deudores_actual.pdf",
    "location": "p. 19"
   }
  ]
 },
 "provenance": {
  "source_doc": "TO_clasificacion_deudores_actual.pdf",
  "location": "p. 19"
 }
}
```

**req_analisis_trimestral_de_clientes_con_financiaciones_que_alcanzan_el_5_o_mas_de_la_responsabilidad_patrimonial_computable**:
```json
{
 "id": "req_analisis_trimestral_de_clientes_con_financiaciones_que_alcanzan_el_5_o_mas_de_la_responsabilidad_patrimonial_computable",
 "type": "REQUIREMENT",
 "label": "análisis trimestral de clientes con financiaciones que alcanzan el 5% o más de la responsabilidad patrimonial computable",
 "properties": {
  "version": "A 8378",
  "description": "Obligación de examinar en el curso de cada trimestre calendario a clientes cuyas financiaciones alcancen el 5% o más de la RPC.",
  "aliases": [
   "Análisis trimestral"
  ],
  "source_to": "clasificacion_deudores",
  "mention_count": 1
 },
 "provenance": {
  "source_doc": "TO_clasificacion_deudores_actual.pdf",
  "location": "p. 18"
 }
}
```

**req_atrasos_mayores_a_31_dias**:
```json
{
 "id": "req_atrasos_mayores_a_31_dias",
 "type": "REQUIREMENT",
 "label": "Atrasos mayores a 31 días",
 "properties": {
  "version": "A 8378",
  "description": "Condición que genera reclasificación inmediata del deudor a nivel resultante de sumar días de atraso efectivo y atraso normativo.",
  "aliases": [
   "Atrasos mayores a 31 días"
  ],
  "source_to": "clasificacion_deudores",
  "mention_count": 1
 },
 "provenance": {
  "source_doc": "TO_clasificacion_deudores_actual.pdf",
  "location": "p. 38"
 }
}
```

### 5. Pasaje(s) del PDF — secciones ground-truth (máx ~1.500 chars por pata)

**Punto 6.3.1 (Periodicidad mínima):**
[TO_clasificacion_deudores_actual.pdf · Punto/Sección 6.3.1 (PDF pág 18)]
> 6.3.1. En el curso de cada trimestre calendario, respecto de clientes individualmente considera- dos cuyas financiaciones comprendidas en algún momento sean equivalentes al 5 % o  más de la RPC o del activo del fideicomiso financiero del mes anterior a la finalización de  dicho período según se trate de entidades o fideicomisos financieros, respectivamente. A  estos fines, el grupo de contrapartes conectadas se tratará como un solo cliente.  6.3.2. En el curso de cada semestre calendario, respecto de clientes individualmente conside- rados cuyas financiaciones comprendidas sumen en algún momento entre el 1 % –o el  equivalente a dos veces el importe de referencia establecido en el punto 3.7., de ambos  el menor– y menos del 5 % de la RPC o del activo del fideicomiso financiero del mes an- terior a la finalización de dicho período según se trate de entidades o fideicomisos finan- cieros, respectivamente. A estos fines, el grupo de contrapartes conectadas se tratará  como un solo cliente.  Al cierre del primer semestre calendario, el examen deberá haber alcanzado no menos  del 50 % del importe total de la cartera comercial comprendida, computando los clientes  a que se refiere el punto 6.3.1., por lo que, de ser necesario para llegar a ese valor, se  completará con la revisión de clientes cuyas financiaciones comprendidas sean inferiores  al 1 % de la citada RPC o del activo del

**Punto 6.4 (Reconsideración obligatoria, último párrafo):**
[TO_clasificacion_deudores_actual.pdf · Punto/Sección 6.4 (PDF pág 18)]
> 6.4. Reconsideración obligatoria de la clasificación.  En forma adicional a la periodicidad mínima expuesta precedentemente, se deberá analizar de- jando constancia fundamentada de la decisión adoptada en el legajo del cliente– y, de ser ne- cesario, modificar la clasificación cada vez que tenga lugar alguna de las siguientes circunstan- cias:  6.4.1. Modificación de alguno de los criterios objetivos de clasificación que surjan de estas nor- mas (término de morosidad, situación jurídica del cliente o de sus deudas, cumplimiento  de refinanciaciones y pedidos de refinanciaciones de obligaciones).  6.4.2. Modificación en forma negativa de la clasificación del cliente en la “Central de deudores  del sistema financiero”, llevándola a un grado inferior al de la entidad, por al menos otra  entidad financiera o fideicomiso financiero cuyas acreencias representen como mínimo el  10 % del total informado por todos los acreedores.  6.4.3. Notificación de la determinación final de la SEFyC del ajuste de previsiones, según lo  previsto en la materia como consecuencia de tareas de inspección.  CLASIFICACIÓN DE DEUDORES  B.C.R.A. S ección 6. Clasificación de los deudores de la cartera comercial.  Versión: 9a. C OMUNICACIÓN  “A”  7024 Vigencia:  20/03/2020 Página 2

### 6. ADJUDICACIÓN (Agustina):
```
Adjudicación de la autora, 2026-07-13, asistida por revisión.

- pata / claim: Pata 2 — claims "La reevaluación debe ser inmediata cuando se producen atrasos mayores a 31 días" [no_soportado] y "Los atrasos mayores a 31 días generan reclasificación inmediata del deudor al nivel resultante de sumar días de atraso efectivo y atraso normativo" [no_soportado]
- sintoma_capa1: noise_sensitivity        causa_capa2: contenido_kg
- primaria/secundaria: PRIMARIA
- evidencia (1 línea): Soportados por req_atrasos_mayores_a_31_dias (abierto por el agente en
  el paso 15), cuyo contenido no existe en el TO — "atraso efectivo", "atraso normativo" y la
  fórmula de suma dan 0 matches en el documento completo; la regla real es la recategorización
  por atrasos >31 días en obligaciones REFINANCIADAS (6.5.x), sin fórmula de suma y sin
  alcance general — nodo con regla deformada/des-scopeada.

- pata / claim: Pata 2 — claim "La reevaluación debe ser inmediata cuando existe discrepancia de más de un nivel en clasificaciones y las financiaciones superan el 1% de la RPC" [falso]
- sintoma_capa1: —        causa_capa2: — (FALSO POSITIVO DEL JUEZ, sin par — no es defecto del sistema)
- primaria/secundaria: —
- evidencia (1 línea): Soportado por
  req_reevaluacion_inmediata_por_discrepancia_de_mas_de_un_nivel_en_clasificaciones (abierto
  en el paso 4) y correcto contra el PDF (Clasificación 6.4.4 + último párrafo del 6.4: "La
  reevaluación deberá ser inmediata cuando... igualen o superen el 1% de la responsabilidad
  patrimonial computable...") — condensado pero sustancialmente correcto.

- pata / claim: Pata 1 (periodicidad mínima) — "trimestral"
- sintoma_capa1: —        causa_capa2: — (sin defecto)
- primaria/secundaria: —
- evidencia (1 línea): Soportado por
  req_analisis_trimestral_de_clientes_con_financiaciones_que_alcanzan_el_5_o_mas_de_la_responsabilidad_patrimonial_computable
  (abierto en el paso 7) y correcto contra el Punto 6.3.1.
```

---

## Caso off/run_1/CQ-031

### 1. Pregunta (verbatim eval_set_v1) y patas (judge.step1.patas_de_la_pregunta)

> ¿Qué deudores no deben ser objeto de clasificación y respecto de qué deudores no corresponde evaluar la capacidad de repago?

- Categoría: `cadena_restriccion_excepcion` · TOs fuente: clasificacion
- Ground-truth secciones: Punto 4.5 (Deudores que no deben ser clasificados) · Punto 4.4 (Financiaciones cubiertas con garantías preferidas 'A')
- Pata 1: "Qué deudores no deben ser objeto de clasificación"
- Pata 2: "Respecto de qué deudores no corresponde evaluar la capacidad de repago"

### 2. Claims con veredicto negativo del juez (verbatim)
- [falso] CENTRAL — «Respecto de los deudores por préstamos de monto reducido no corresponde evaluar obligatoriamente la capacidad de repago por ingresos.»
- [falso] CENTRAL — «Los prestatarios cuyos préstamos son de monto reducido están eximidos de la evaluación obligatoria de capacidad de pago.»
- cobertura_patas: [{"pata": "Qué deudores no deben ser objeto de clasificación", "cobertura": "no_cubierta"}, {"pata": "Respecto de qué deudores no corresponde evaluar la capacidad de repago", "cobertura": "no_cubierta"}]

### 3. Trayectoria del agente (tool calls, rep 1)
- paso 1 · `buscar_nodos` · input: `{"consulta": "deudores no deben ser objeto clasificación", "limite": 10}`
  → {"consulta": "deudores no deben ser objeto clasificación", "total_con_match": 218, "resultados": [{"id": "ope_clasificacion_de_deudores", "type": "OPERATION", " …(no-JSON)
- paso 2 · `buscar_nodos` · input: `{"consulta": "capacidad de repago evaluación deudores", "limite": 10}`
  → {"consulta": "capacidad de repago evaluación deudores", "total_con_match": 2481, "resultados": [{"id": "con_capacidad_de_repago_del_deudor", "type": "CONCEPT",  …(no-JSON)
- paso 3 · `ver_nodo` · input: `{"id": "prc_clasificacion_de_deudores"}`
  → nodo prc_clasificacion_de_deudores (Clasificación de Deudores) — contenido íntegro abajo (§4)
- paso 4 · `ver_nodo` · input: `{"id": "prc_evaluacion_de_capacidad_de_pago"}`
  → nodo prc_evaluacion_de_capacidad_de_pago (Evaluación de capacidad de pago) — contenido íntegro abajo (§4)
- paso 5 · `ver_vecinos` · input: `{"id": "prc_clasificacion_de_deudores", "direccion": "ambas"}`
  → {"id": "prc_clasificacion_de_deudores", "label": "Clasificación de Deudores", "n_salientes_total": 3, "n_entrantes_total": 13, "salientes": [{"relation": "regul …(no-JSON)
- paso 6 · `ver_vecinos` · input: `{"id": "prc_evaluacion_de_capacidad_de_pago", "direccion": "ambas"}`
  → salientes=1 entrantes=2 → no_obligatoria_cuando→con_metodos_especificos_de_evaluacion
- paso 7 · `ver_nodo` · input: `{"id": "cla_deudores_por_prestamos_de_monto_reducido"}`
  → nodo cla_deudores_por_prestamos_de_monto_reducido (Deudores por préstamos de monto reducido) — contenido íntegro abajo (§4)
- paso 8 · `buscar_nodos` · input: `{"consulta": "deudores excepción no clasificación exención", "limite": 10}`
  → {"consulta": "deudores excepción no clasificación exención", "total_con_match": 225, "resultados": [{"id": "ope_clasificacion_de_deudores", "type": "OPERATION", …(no-JSON)
- paso 9 · `buscar_nodos` · input: `{"consulta": "no deben ser objeto clasificación deudores", "limite": 10}`
  → {"consulta": "no deben ser objeto clasificación deudores", "total_con_match": 218, "resultados": [{"id": "ope_clasificacion_de_deudores", "type": "OPERATION", " …(no-JSON)
- paso 10 · `buscar_nodos` · input: `{"consulta": "deudores estado gobierno soberano", "limite": 10}`
  → {"consulta": "deudores estado gobierno soberano", "total_con_match": 47, "resultados": [{"id": "rep_estado_de_situacion_de_deudores", "type": "REPORT_ITEM", "la …(no-JSON)
- paso 11 · `buscar_nodos` · input: `{"consulta": "deudores no clasificación estado nacional provincial municipal", "limite": 10}`
  → {"consulta": "deudores no clasificación estado nacional provincial municipal", "total_con_match": 252, "resultados": [{"id": "rsj_sector_publico_no_financiero_p …(no-JSON)
- paso 12 · `buscar_nodos` · input: `{"consulta": "no corresponde evaluar capacidad repago", "limite": 10}`
  → {"consulta": "no corresponde evaluar capacidad repago", "total_con_match": 165, "resultados": [{"id": "con_capacidad_de_repago_del_deudor", "type": "CONCEPT", " …(no-JSON)
- paso 13 · `buscar_nodos` · input: `{"consulta": "excepción clasificación deudores estado nacional", "limite": 10}`
  → {"consulta": "excepción clasificación deudores estado nacional", "total_con_match": 100, "resultados": [{"id": "ope_clasificacion_de_deudores", "type": "OPERATI …(no-JSON)
- paso 14 · `ver_nodo` · input: `{"id": "ope_clasificacion_de_deudores"}`
  → {"id": "ope_clasificacion_de_deudores", "type": "OPERATION", "label": "Clasificación de deudores", "properties": {"version": "A 8433", "description": "Procedimi …(no-JSON)
- paso 15 · `ver_vecinos` · input: `{"id": "ope_clasificacion_de_deudores", "direccion": "ambas"}`
  → {"id": "ope_clasificacion_de_deudores", "label": "Clasificación de deudores", "n_salientes_total": 11, "n_entrantes_total": 20, "salientes": [{"relation": "requ …(no-JSON)
- **Respuesta final:** «Según la regulación del BCRA, respecto de los deudores por préstamos de monto reducido no corresponde evaluar obligatoriamente la capacidad de repago por ingresos. Esta categoría de prestatarios cuyos préstamos son de monto reducido está eximida de la evaluación obligatoria de capacidad de pago. Sin embargo, en el Knowledge Graph no se encontró información específica sobre qué deudores no deben ser objeto de clasificación en general.»
- **Citas:** [{"source_doc": "TO_clasificacion_deudores_actual.pdf", "location": "p. 34"}]

### 4. Nodos abiertos con `ver_nodo` — contenido ÍNTEGRO (kg.json congelado)

**prc_clasificacion_de_deudores**:
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
  "mention_count": 7,
  "other_locations": [
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
 },
 "provenance": {
  "source_doc": "TO_clasificacion_deudores_actual.pdf",
  "location": "pp. 1-2"
 }
}
```

**prc_evaluacion_de_capacidad_de_pago**:
```json
{
 "id": "prc_evaluacion_de_capacidad_de_pago",
 "type": "PROCESS",
 "label": "Evaluación de capacidad de pago",
 "properties": {
  "version": "A 8378",
  "description": "Proceso de evaluación periódica de deudores para asegurar la actualización de su clasificación.",
  "aliases": [
   "evaluación de capacidad de pago",
   "Evaluación con periodicidad correspondiente"
  ],
  "source_to": "clasificacion_deudores",
  "mention_count": 2,
  "other_locations": [
   {
    "source_doc": "TO_clasificacion_deudores_actual.pdf",
    "location": "p. 34"
   }
  ]
 },
 "provenance": {
  "source_doc": "TO_clasificacion_deudores_actual.pdf",
  "location": "p. 31"
 }
}
```

**cla_deudores_por_prestamos_de_monto_reducido**:
```json
{
 "id": "cla_deudores_por_prestamos_de_monto_reducido",
 "type": "CLASSIFICATION",
 "label": "Deudores por préstamos de monto reducido",
 "properties": {
  "version": "A 8378",
  "description": "Categoría de prestatarios cuyos préstamos son de monto reducido, exentos de evaluación obligatoria de capacidad de pago por ingresos.",
  "aliases": [
   "deudores por préstamos de monto reducido"
  ],
  "source_to": "clasificacion_deudores",
  "mention_count": 1
 },
 "provenance": {
  "source_doc": "TO_clasificacion_deudores_actual.pdf",
  "location": "p. 34"
 }
}
```

**ope_clasificacion_de_deudores**:
```json
{
 "id": "ope_clasificacion_de_deudores",
 "type": "OPERATION",
 "label": "Clasificación de deudores",
 "properties": {
  "version": "A 8433",
  "description": "Procedimiento administrativo de categorización de deudores según su mora y situación crediticia, observado por entidades financieras de forma individual o consolidada.",
  "aliases": [
   "Clasificación de deudores",
   "clasificación de deudores",
   "Clasificación de deudores: Proceso de categorización y evaluación de la situación crediticia de los deudores.",
   "Clasificación de Deudores: Procedimiento administrativo de análisis y categorización del riesgo crediticio de los deudores.",
   "clasificación de deudores: Tarea de actualización y mantenimiento de la clasificación asignada a cada cliente en legajos separados identificables.",
   "Evaluación y clasificación de deudores: Procedimiento mediante el cual se asignan clasificaciones a los deudores considerando su capacidad de repago.",
   "Tarea de clasificación: Proceso de clasificación de deudores que puede ser encomendado a un área independiente, al sector de créditos con revisión independiente, o a profesionales externos.",
   "Reconsideración obligatoria de la clasificación: Procedimiento de análisis adicional y modificación de clasificación cuando se modifican criterios objetivos, varía la clasificación en la Central de deudores, o se notifica ajuste de previsiones por inspección."
  ],
  "source_to": "proteccion_usuarios",
  "mention_count": 14,
  "other_locations": [
   {
    "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
    "location": "p. 39"
   },
   {
    "source_doc": "TO_clasificacion_deudores_actual.pdf",
    "location": "p. 9"
   },
   {
    "source_doc": "TO_clasificacion_deudores_actual.pdf",
    "location": "p. 14"
   },
   {
    "source_doc": "TO_clasificacion_deudores_actual.pdf",
    "location": "p. 18"
   },
   {
    "source_doc": "TO_clasificacion_deudores_actual.pdf",
    "location": "p. 33"
   },
   {
    "source_doc": "TO_clasificacion_deudores_actual.pdf",
    "location": "p. 40"
   },
   {
    "source_doc": "TO_clasificacion_deudores_actual.pdf",
    "location": "pp. 42-43"
   },
   {
    "source_doc": "TO_clasificacion_deudores_actual.pdf",
    "location": "p. 54"
   },
   {
    "source_doc": "TO_clasificacion_deudores_actual.pdf",
    "location": "p. 55"
   },
   {
    "source_doc": "TO_capitales_minimos_actual.pdf",
    "location": "p. 194"
   },
   {
    "source_doc": "TO_capitales_minimos_actual.pdf",
    "location": "p. 197"
   },
   {
    "source_doc": "TO_capitales_minimos_actual.pdf",
    "location": "p. 198"
   },
   {
    "source_doc": "TO_capitales_minimos_actual.pdf",
    "location": "p. 199"
   }
  ]
 },
 "provenance": {
  "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
  "location": "p. 38"
 }
}
```

### 5. Pasaje(s) del PDF — secciones ground-truth (máx ~1.500 chars por pata)

**Punto 4.5 (Deudores que no deben ser clasificados):**
[TO_clasificacion_deudores_actual.pdf · Punto/Sección 4.5 (PDF pág 15)]
> 4.5. Deudores que no deben ser objeto de clasificación.  Los deudores cuyas financiaciones se encuentren cubiertas totalmente con garantías preferidas  “A” no serán objeto de clasificación, sin perjuicio de su información según las normas que se  establezcan en los regímenes respectivos.  4.6. Financiaciones –sin responsabilidad para el cedente– amparadas con seguros de crédito por  riesgo comercial y con seguros de riesgo de crédito “con alcance de comprador público”.  Se procederá a clasificar a la compañía de seguros en función de la mora según los criterios  aplicables para la cartera de consumo, teniendo en cuenta la fecha de vencimiento de la prime- ra obligación vencida impaga, a partir del momento en que, no habiendo sido rechazado el re- clamo, se verifique la falta de pago del siniestro luego de vencidos los plazos comprometidos  en la póliza (180 o 270 días, según corresponda).  No serán objeto de clasificación quiene s resulten deudore s en operacione s de cesión sin res- ponsabilidad para el cedente.  Sólo se aplicarán lo s criterios precedentes cuando se trate de operacione s del título que, en  origen, hayan reunido los requisitos pertinentes establecidos en las normas sobre “Garantías”.  CLASIFICACIÓN DE DEUDORES B.C.R.A. S ección 4. Criterios de clasificación.  Versión: 5a. COMUNICACIÓN  “A”  6558 V igencia:  5/9/2018 Página 1

**Punto 4.4 (Financiaciones cubiertas con garantías preferidas 'A'):**
[TO_clasificacion_deudores_actual.pdf · Punto/Sección 4.4 (PDF pág 2)]
> 4.4. Financiaciones cubiertas con garantías preferidas “A”.  4.5. Deudores que no deben ser objeto de clasificación.  4.6. Financiaciones –sin responsabilidad para el cedente– amparadas con seguros de  crédito por riesgo comercial y con seguros de riesgo de crédito “con alcance de  comprador público”.  Sección 5. Categorías de carteras.  5.1. Categorías.  Sección 6. Clasificación de los deudores de la cartera comercial.  6.1. Información básica.  6.2. Criterio de clasificación.  6.3. Periodicidad mínima de clasificación.  6.4. Reconsideración obligatoria de la clasificación.  6.5. Niveles de clasificación.  6.6. Recategorización obligatoria.  B.C.R.A. TEXTO ORDENADO DE LAS NORMAS SOBRE  “CLASIFICACION DE DEUDORES”  Versión: 6a. COMUNICACIÓN  “A”  6558 Vig encia:  5/9/2018 Página 1

### 6. ADJUDICACIÓN (Agustina):
```
Adjudicación de la autora, 2026-07-13, asistida por revisión.

- pata / claim: Pata 1 — "Qué deudores no deben ser objeto de clasificación"
- sintoma_capa1: context_recall        causa_capa2: alcanzabilidad_kg
- primaria/secundaria: PRIMARIA
- evidencia (1 línea): Los portadores del 4.5 y 4.6 existen (rsj_deudor_con_garantias_preferidas_a;
  ope_creditos_cedidos_sin_responsabilidad_para_el_cedente) con labels sin vocabulario de la
  pregunta; ninguno apareció en los resultados de las 8 buscar_nodos de la traza (verificado
  sobre los outputs completos, re-ejecutados determinísticamente con el harness).

- pata / claim: Pata 2 — "Respecto de qué deudores no corresponde evaluar la capacidad de repago"
- sintoma_capa1: context_recall        causa_capa2: alcanzabilidad_kg
- primaria/secundaria: PRIMARIA
- evidencia (1 línea): El dato GT (4.4) nunca apareció en la trayectoria; los portadores
  cla_garantias_preferidas_a y cla_financiaciones_con_garantias_preferidas_a son alcanzables
  solo por vocabulario propio ("garantías preferidas"), no por los términos de la pregunta.

- pata / claim: Los 2 claims de "monto reducido" marcados falso por el juez
- sintoma_capa1: —        causa_capa2: — (FALSOS POSITIVOS DEL JUEZ, sin par — no es defecto del sistema)
- primaria/secundaria: —
- evidencia (1 línea): Claim 1 soportado por cla_deudores_por_prestamos_de_monto_reducido y
  correcto contra el PDF (TO Clasificación, Sección 7: "No será obligatoria la evaluación de la
  capacidad de pago en función de los ingresos [...] préstamos de monto reducido"); claim 2
  ídem con salvedad (generaliza sin el calificador "por ingresos").
```
