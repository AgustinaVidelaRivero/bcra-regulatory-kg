# Verificaciones programáticas de la vara — barridos determinísticos sobre run_3

Fecha: 2026-07-15. Solo lectura; única escritura: este archivo. **Sellado respetado:**
`posthoc_run/dev_set/gate2_v57/` no fue abierto (lista de archivos abiertos al final).
**Solo hechos:** no se adjudica, no se clasifica, no se opina si algo "cuenta".

**Mecanismo (el mismo de las auditorías previas):** `loader.load_graph("run_3")` → kg
congelado (4.050 nodos, **6.634 edges**) + `harness.GraphIndex` para simular búsquedas.
Barridos sobre texto normalizado (lowercase, sin acentos). Script completo:
`verificaciones_vara.py` (scratchpad de sesión); el núcleo de cada punto se pega en su
sección junto con el output completo.

**Tokenización del índice (para el punto 2, verbatim de `harness.py`):**

```python
_TOKEN_RE = re.compile(r"[a-z0-9]+")
def _tokens(s):  # sobre lowercase sin acentos (NFKD)
    return _TOKEN_RE.findall(_strip_accents((s or "").lower()))
# GraphIndex.__init__: self._node_tokens = {n.id: set(_tokens(n.label) + _tokens(n.id)) ...}
# buscar_nodos: score = len(tokens(consulta) & _node_tokens[nodo]); orden (-score, len(label), id)
```

---

## 1. CQ-017 — conexión cross-documento y provenance

### 1a. Nodo del operador de cambio — contenido íntegro

Código del barrido de ubicación:

```python
op_nodes = [n for n in kg.nodes
            if "operador de cambio" in props_blob(n) or "operador_de_cambio" in props_blob(n)]
# props_blob(n) = norm(json({id, label, properties}))
```

Output completo:

```
[1a] Nodos con 'operador de cambio'/'operador_de_cambio' en id/label/properties: 1

--- EntidadFinanciera_operador_de_cambio ---
{
 "id": "EntidadFinanciera_operador_de_cambio",
 "type": "EntidadFinanciera",
 "label": "Operadores de cambio",
 "properties": {
  "categoria": "operador de cambio"
 },
 "provenances": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "Punto 1.1. Partes."
  }
 ]
}
```

(Es el nodo que el agente consultó: `ver_nodo` en el paso 4 de la trayectoria de CQ-017,
según el inventario de `auditoria_truncamiento_run3.md` §3.)

### 1b. TODOS los edges de ese nodo — completos

```
--- EntidadFinanciera_operador_de_cambio: 1 salientes, 1 entrantes ---
SALIENTE: {
 "source": "EntidadFinanciera_operador_de_cambio",
 "relation": "ejecuta",
 "target": "Operacion_operacion_de_cambio",
 "properties": {},
 "provenances": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "Punto 1.1. Partes."
  }
 ]
}
ENTRANTE: {
 "source": "Obligacion_cuando_un_tercero_desarrolle_tareas_relativas_a_servicios_ofrecidos_por_los_suje",
 "relation": "aplica_a",
 "target": "EntidadFinanciera_operador_de_cambio",
 "properties": {},
 "provenances": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "Punto 1.1. Partes."
  }
 ]
}
```

El nodo tiene exactamente 2 edges (1 saliente, 1 entrante); ambos con provenance de
`TO_proteccion_usuarios_servicios_financieros_actual.pdf`, "Punto 1.1. Partes.".

### 1c. Candidatos "entidad autorizada" / "autorizadas a operar" / "intervencion de entidades"

```python
pats_c = r"entidad(es)? autorizada|autorizad[ao]s? a operar|intervencion de entidades"
cand_c = [n for n in kg.nodes if re.search(pats_c, props_blob(n))]
# para cada candidato: edges hacia/desde cualquier nodo del conjunto op_ids (1a)
```

Output completo — **3 candidatos, ninguno con edges hacia/desde el nodo del operador de cambio**:

```
[1c] Candidatos: 3

--- candidato: Obligacion_se_deberan_calcular_los_coeficientes_delta_gamma_y_vega_para_las_posiciones_en_o ---
{
 "id": "Obligacion_se_deberan_calcular_los_coeficientes_delta_gamma_y_vega_para_las_posiciones_en_o",
 "type": "Obligacion",
 "label": "Calcular coeficientes delta gamma vega",
 "properties": {
  "descripcion": "Se deberán calcular los coeficientes delta, gamma y vega para las posiciones en opciones empleando modelos aprobados por mercados de opciones autorizados a operar por la CNV o modelos propios de determinación de precios",
  "tipo": "calculo",
  "plazo": "obligatorio"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Punto 6.6. Exigencia de capital por riesgo de posiciones en opciones. (parte 1)"
  }
 ]
}
EDGES hacia/desde nodos 'operador de cambio': NINGUNO

--- candidato: Restriccion_las_consultas_o_pedidos_de_conformidad_previa_deberan_indefectiblemente_efectuar ---
{
 "id": "Restriccion_las_consultas_o_pedidos_de_conformidad_previa_deberan_indefectiblemente_efectuar",
 "type": "Restriccion",
 "label": "Obligatoriedad gestión mediante entidad autorizada",
 "properties": {
  "descripcion": "Las consultas o pedidos de conformidad previa deberán indefectiblemente efectuarse a través de una entidad que esté autorizada a cursar el tipo de operación",
  "tipo": "limite_cualitativo"
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 1.7. Las entidades deberán cumplir con las normas sobre “Prevención del lavado de act"
  }
 ]
}
EDGES hacia/desde nodos 'operador de cambio': NINGUNO

--- candidato: Restriccion_los_casos_que_no_encuadren_en_lo_expuesto_precedentemente_quedan_sujetos_a_la_co ---
{
 "id": "Restriccion_los_casos_que_no_encuadren_en_lo_expuesto_precedentemente_quedan_sujetos_a_la_co",
 "type": "Restriccion",
 "label": "Conformidad previa BCRA",
 "properties": {
  "descripcion": "Los casos que no encuadren en lo expuesto precedentemente quedan sujetos a la conformidad previa del BCRA, debiendo los pedidos ser canalizados por una entidad autorizada a realizar este tipo de pagos",
  "tipo": "limite_cualitativo"
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 13.1. Disposiciones generales."
  }
 ]
}
EDGES hacia/desde nodos 'operador de cambio': NINGUNO
```

### 1d. Barrido de edges de TODO el grafo (6.634 edges)

```python
pats_d = r"entidad(es)? autorizada|autorizad[ao]s? a operar|mercado de cambios"
# edge matchea si un extremo ∈ op_ids (nodos 'operador de cambio', 1a)
# y el otro extremo matchea pats_d en id/label/properties
```

Output completo:

```
[1d] Edges con un extremo 'operador de cambio' y el otro matcheando
'entidad autorizada'/'autorizadas a operar'/'mercado de cambios': 0
```

**Cero aristas** en los 6.634 edges del grafo cumplen la condición.

---

## 2. CQ-031 — portador del 4.5 y mecanismo de alcanzabilidad

### 2a. Lookup directo del portador — contenido íntegro

```
[2a] Lookup directo de Restriccion_los_deudores_cuyas_financiaciones_se_encuentren_cubiertas_totalmente_con_garanti:
{
 "id": "Restriccion_los_deudores_cuyas_financiaciones_se_encuentren_cubiertas_totalmente_con_garanti",
 "type": "Restriccion",
 "label": "Prohibición de clasificación por cobertura total",
 "properties": {
  "tipo": "prohibicion",
  "descripcion": "Los deudores cuyas financiaciones se encuentren cubiertas totalmente con garantías preferidas A no serán objeto de clasificación",
  "description": "Los deudores cuyas financiaciones se encuentren cubiertas totalmente con garantías preferidas A no serán objeto de clasificación, sin perjuicio de su información según las normas que se establezcan en los regímenes respectivos"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Punto 4.4. Financiaciones cubiertas con garantías preferidas “A”."
  }
 ]
}
```

`properties.descripcion` VERBATIM:

```
'Los deudores cuyas financiaciones se encuentren cubiertas totalmente con garantías preferidas A no serán objeto de clasificación'
```

(Hecho registrado sin clasificar: el nodo tiene DOS campos de texto — `descripcion` y
`description`, este último con la coda "sin perjuicio de su información..." —; la provenance
del nodo dice `location: "Punto 4.4. Financiaciones cubiertas con garantías preferidas 'A'."`.)

### 2b. Tokens exactos del índice (post-normalización, `harness._tokens`)

```
tokens(label): ['prohibicion', 'de', 'clasificacion', 'por', 'cobertura', 'total']
tokens(id):    ['restriccion', 'los', 'deudores', 'cuyas', 'financiaciones', 'se', 'encuentren', 'cubiertas', 'totalmente', 'con', 'garanti']
set indexado (_node_tokens): ['clasificacion', 'cobertura', 'con', 'cubiertas', 'cuyas', 'de', 'deudores', 'encuentren', 'financiaciones', 'garanti', 'los', 'por', 'prohibicion', 'restriccion', 'se', 'total', 'totalmente']
```

Hecho: el id del nodo está truncado en "...con_garanti", por lo que el token indexado es
**`garanti`** (no `garantias`); la palabra "garantías" de la `descripcion` NO se indexa
(el índice toma solo label + id).

### 2c. Simulación de las 10 consultas `buscar_nodos` de la trayectoria (verbatim de la traza, limite=10)

Código (réplica exacta del scoring de `GraphIndex.buscar_nodos`):

```python
q = set(_tokens(consulta))
scored = [(len(q & idx._node_tokens[n.id]), len(n.label or ""), n.id) for n in kg.nodes si score > 0]
scored.sort(key=lambda t: (-t[0], t[1], t[2]))   # rank completo; top-`limite` es lo devuelto
```

Output completo:

```
  paso 1: "deudores no deben ser objeto clasificación"  (limite=10, total_con_match=509)
    tokens de la consulta ∩ tokens del portador: ['clasificacion', 'deudores'] (2)
    portador: rank 47 de 509 (score 2; 51 nodos con ese score) -> en top-10: NO

  paso 2: "capacidad de repago evaluación deudores"  (limite=10, total_con_match=2417)
    tokens de la consulta ∩ tokens del portador: ['de', 'deudores'] (2)
    portador: rank 44 de 2417 (score 2; 46 nodos con ese score) -> en top-10: NO

  paso 7: "deudores exclusión clasificación estado nacional provincia municipio"  (limite=10, total_con_match=156)
    tokens de la consulta ∩ tokens del portador: ['clasificacion', 'deudores'] (2)
    portador: rank 13 de 156 (score 2; 12 nodos con ese score) -> en top-10: NO

  paso 8: "garantías preferidas A financiaciones"  (limite=10, total_con_match=1220)
    tokens de la consulta ∩ tokens del portador: ['financiaciones'] (1)
    portador: rank 1141 de 1220 (score 1; 1195 nodos con ese score) -> en top-10: NO

  paso 9: "punto 4.5 deudores no deben clasificación estado nacional"  (limite=10, total_con_match=523)
    tokens de la consulta ∩ tokens del portador: ['clasificacion', 'deudores'] (2)
    portador: rank 46 de 523 (score 2; 47 nodos con ese score) -> en top-10: NO

  paso 10: "punto 4.4 garantías preferidas A estado nacional provincia"  (limite=10, total_con_match=1220)
    tokens de la consulta ∩ tokens del portador: [] (0)
    portador: SIN MATCH (score 0) -> fuera del ranking por completo

  paso 11: "estado nacional provincia municipio banco central deudores"  (limite=10, total_con_match=71)
    tokens de la consulta ∩ tokens del portador: ['deudores'] (1)
    portador: rank 63 de 71 (score 1; 63 nodos con ese score) -> en top-10: NO

  paso 12: "cesión sin responsabilidad cedente deudores"  (limite=10, total_con_match=126)
    tokens de la consulta ∩ tokens del portador: ['deudores'] (1)
    portador: rank 104 de 126 (score 1; 117 nodos con ese score) -> en top-10: NO

  paso 14: "garantías preferidas A definición estado nacional provincia"  (limite=10, total_con_match=1191)
    tokens de la consulta ∩ tokens del portador: [] (0)
    portador: SIN MATCH (score 0) -> fuera del ranking por completo

  paso 15: "garantías preferidas A créditos estado nacional provincia municipio"  (limite=10, total_con_match=1208)
    tokens de la consulta ∩ tokens del portador: [] (0)
    portador: SIN MATCH (score 0) -> fuera del ranking por completo
```

Resumen fáctico: **0 de las 10 consultas ponen al portador en el top-10**. Mejor rank: 13
(paso 7). En las 3 consultas que contienen "garantías preferidas A" sin otra palabra del
portador (pasos 10, 14, 15) el portador tiene **score 0** — el token de consulta `garantias`
no matchea el token indexado `garanti` (id truncado, §2b) —; en el paso 8 matchea solo por
`financiaciones` (rank 1141).

### 2d. Simulación inversa (palabras del propio nodo)

```
  consulta: "Prohibición de clasificación por cobertura total"   [= label verbatim]
    total_con_match=2560; portador en top-10: posicion 1; rank completo: 1; tokens matcheados: ['clasificacion', 'cobertura', 'de', 'por', 'prohibicion', 'total'] (6)
    top-10 devuelto: ['Restriccion_los_deudores_cuyas_financiaciones_se_encuentren_cubiertas_totalmente_con_garanti', 'Obligacion_seleccionar_un_unico_metodo_para_aplicar_la_tecnica_de_cobertura', 'Operacion_cobertura_de_pagos_por_garante', 'Operacion_transferencia_de_riesgo_en_tramos_con_proteccion_crediticia', 'Restriccion_las_posiciones_en_opciones_vendidas_deberan_estar_cubiertas_por_posiciones_compr', 'Excepcion_la_clasificacion_se_verifica_a_partir_del_momento_en_que_no_habiendo_sido_rechaz', 'Restriccion_las_acreencias_en_conjunto_deben_representar_el_40_o_mas_del_total_informado_por', 'Excepcion_cuando_el_monto_pendiente_de_ingreso_de_las_operaciones_haya_sido_prefinanciado_', 'Restriccion_el_total_de_los_vencimientos_por_las_cuotas_de_todas_las_financiaciones_de_la_en', 'Restriccion_se_requerira_la_conformidad_previa_del_bcra_cuando_el_cliente_registre_por_opera']

  consulta: "financiaciones cubiertas totalmente garantías preferidas"
    total_con_match=100; portador en top-10: posicion 1; rank completo: 1; tokens matcheados: ['cubiertas', 'financiaciones', 'totalmente'] (3)
    top-10 devuelto: ['Restriccion_los_deudores_cuyas_financiaciones_se_encuentren_cubiertas_totalmente_con_garanti', 'Restriccion_no_correspondera_la_evaluacion_de_la_capacidad_de_repago_respecto_de_las_financi', 'Obligacion_en_el_caso_de_la_compra_se_utilizara_el_concepto_p12_otras_financiaciones_locale', 'Operacion_constitucion_de_garantias_en_cuentas', 'Operacion_garantia', 'Operacion_otorgamiento_de_garantia', 'Operacion_pago_de_capital_adeudado_en_emisiones_de_titulos_y_financiaciones', 'Obligacion_se_incrementara_el_valor_de_los_activos_en_garantia_dados_por_la_entidad_y_se_re', 'Operacion_analisis_crediticio', 'Operacion_transferencia_de_garantias']
```

Ambas consultas con palabras del propio nodo lo devuelven en **posición 1**.

---

## 3. CQ-020 — frecuencia general del régimen y barrido de la secundaria

### 3a. Frecuencia/periodicidad GENERAL del R.I.-C.M.

```python
rx_a = r"r\.i\.-c\.m\.|regimen informativo|presentacion de las informaciones|periodicidad"
cand_a = [n for n in kg.nodes if re.search(rx_a, props_blob(n)) and "mensual" in props_blob(n)]
# props_blob NO incluye provenances -> excluye por construcción los matches solo-filename
```

Output completo — **5 candidatos**:

```
--- Obligacion_verificacion_mensual_precios_periodicidad ---
{
 "id": "Obligacion_verificacion_mensual_precios_periodicidad",
 "type": "Obligacion",
 "label": "Verificación mensual precios periodicidad",
 "properties": {
  "tipo": "otra",
  "plazo": "al menos mensual",
  "description": "Dicha verificación se debe llevar a cabo al menos con periodicidad mensual, o de forma más frecuente, en función de la naturaleza del mercado o la actividad de negociación"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Punto 6.10. Tratamiento para las posiciones de menor liquidez. (parte 1)"
  }
 ]
}

--- Obligacion_comunicar_cambios_negativos_de_clasificacion ---
{
 "id": "Obligacion_comunicar_cambios_negativos_de_clasificacion",
 "type": "Obligacion",
 "label": "Comunicar cambios negativos de clasificación",
 "properties": {
  "tipo": "comunicacion_a_cliente",
  "description": "Las entidades financieras deberán comunicar a los deudores los cambios negativos en la clasificación que se les asigne, siendo optativo cuando el saldo de deuda sea inferior al monto establecido en el punto 2 de la Sección 3 del Régimen Informativo Contable Mensual"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Punto 3.4. Legajo del cliente. (parte 1)"
  }
 ]
}

--- TextoOrdenado_to_regimen_informativo_contable_mensual_actual_pdf ---
{
 "id": "TextoOrdenado_to_regimen_informativo_contable_mensual_actual_pdf",
 "type": "TextoOrdenado",
 "label": "Régimen Informativo Contable Mensual",
 "properties": {
  "materia": "Información contable y regulatoria mensual",
  "archivo": "TO_regimen_informativo_contable_mensual_actual.pdf",
  "version": "actual"
 },
 "provenances": [
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Punto 1.1. La información tendrá frecuencia mensual y se integrará con datos referidos al m"
  }
 ]
}

--- Obligacion_informacion_base_individual_y_consolidada ---
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

--- Obligacion_informar_exigencia_de_capitales_por_riesgo ---
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

Hecho registrado sin clasificar: entre los 5, el nodo `TextoOrdenado_to_regimen_informativo_contable_mensual_actual_pdf`
matchea por su label/materia; el texto "La información tendrá frecuencia mensual..." aparece
en la **location de su provenance**, no en sus properties.

### 3b. Barrido de "0,08" / "0.08" / "70100000" / "APRc" / "APR_c" sobre TODOS los campos

```python
# full_blob(n) = norm(json({id, label, properties, provenances}))  <- TODOS los campos
[("'0,08'", r"0,08"), ("'0.08'", r"0\.08"), ("'70100000'", r"70100000"),
 ("'APRc'", r"aprc"), ("'APR_c'", r"apr_c")]
```

Output término por término:

**"0,08" — 4 matches:**

```
--- Operacion_calculo_de_capital_minimo ---
{
 "id": "Operacion_calculo_de_capital_minimo",
 "type": "Operacion",
 "label": "Cálculo de exigencia por riesgo de crédito",
 "properties": {
  "tipo": "calculo de capital minimo",
  "description": "Determinación de la exigencia de capital por riesgo de crédito conforme a la fórmula C_RC = (k x 0,08 x APR_c) + INC"
 },
 "provenances": [
  {"source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Punto 3.1. Normas de procedimiento. (parte 1)"}
 ]
}

--- Obligacion_determinar_exigencia_segun_formula_prescrita ---
{
 "id": "Obligacion_determinar_exigencia_segun_formula_prescrita",
 "type": "Obligacion",
 "label": "Determinar exigencia según fórmula prescrita",
 "properties": {
  "tipo": "calculo",
  "description": "Se determinará la exigencia de capital por riesgo de crédito de acuerdo con la expresión C_RC = (k x 0,08 x APR_c) + INC"
 },
 "provenances": [
  {"source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Punto 3.1. Normas de procedimiento. (parte 1)"}
 ]
}

--- Operacion_calculo_de_exigencia_por_riesgo ---
{
 "id": "Operacion_calculo_de_exigencia_por_riesgo",
 "type": "Operacion",
 "label": "Cálculo exigencia riesgo crédito",
 "properties": {
  "tipo": "cálculo de exigencia por riesgo",
  "description": "Cálculo de la exigencia por riesgo de crédito sin incluir el término INC mediante la fórmula: Código 70100000 (n) = k x 0,08 [ ∑(A x p) + ∑ (PFB x CCF x p) + ∑ (12300000 x p) + (∑ 13X00000 + 14000000 + 86300000) x 12,5 + 15000000 ]"
 },
 "provenances": [
  {"source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Punto 8.1. Normas de procedimiento."}
 ]
}

--- Operacion_calculo_de_activos_ponderados ---
{
 "id": "Operacion_calculo_de_activos_ponderados",
 "type": "Operacion",
 "label": "Cálculo activos ponderados riesgo",
 "properties": {
  "tipo": "cálculo de activos ponderados",
  "description": "Se informarán los activos ponderados por riesgo (parámetro para el cálculo de los límites mínimos aplicables a los componentes de la RPC), determinados según la expresión: APR = 70100000 /(k * 0,08) + (70300000 - 3600000Y + 70800000 ) * 12,5"
 },
 "provenances": [
  {"source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Punto 8.1. Normas de procedimiento."}
 ]
}
```

**"0.08" (con punto) — AUSENTE en los 4.050 nodos.**

**"70100000" — 2 matches:** `Operacion_calculo_de_exigencia_por_riesgo` y
`Operacion_calculo_de_activos_ponderados` (contenidos íntegros ya pegados arriba, idénticos).

**"APRc" (sin guion bajo) — AUSENTE en los 4.050 nodos.**

**"APR_c" — 3 matches:** `Operacion_calculo_de_capital_minimo` y
`Obligacion_determinar_exigencia_segun_formula_prescrita` (pegados arriba) más:

```
--- Operacion_calculo_de_ponderadores ---
{
 "id": "Operacion_calculo_de_ponderadores",
 "type": "Operacion",
 "label": "Cálculo de activos ponderados por riesgo",
 "properties": {
  "tipo": "calculo de ponderadores",
  "description": "Cálculo de APR_c conforme a fórmula: APR_c = A x p + PFB x CCF x p + no DVP + (DVP + RCD + INC) x 12,5"
 },
 "provenances": [
  {"source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Punto 3.1. Normas de procedimiento. (parte 1)"}
 ]
}
```

---

## 4. CQ-034 — portador del límite para débito en cuenta

### 4a. Lookup directo de `Obligacion_cursar_operacion_con_debito_en_cuenta`

```
{
 "id": "Obligacion_cursar_operacion_con_debito_en_cuenta",
 "type": "Obligacion",
 "label": "Cursar operación con débito en cuenta",
 "properties": {
  "tipo": "otra",
  "description": "La operación se curse con débito en cuenta del cliente en entidades financieras locales."
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 3.8. Compra de moneda extranjera por parte de personas humanas residentes para la for"
  }
 ]
}
```

### 4b. Barrido: "debito" + {"limite","monto","umbral","usd","mensual"}

```python
cand_b = [n for n in kg.nodes
          if "debito" in props_blob(n) and re.search(r"limite|monto|umbral|usd|mensual", props_blob(n))]
```

Output completo — **1 candidato**:

```
--- Restriccion_para_debito_automatico_aplicara_tipo_de_cambio_vendedor_para_operaciones_electro ---
{
 "id": "Restriccion_para_debito_automatico_aplicara_tipo_de_cambio_vendedor_para_operaciones_electro",
 "type": "Restriccion",
 "label": "Especificación de tipo de cambio por canal",
 "properties": {
  "descripcion": "Para débito automático aplicará tipo de cambio vendedor para operaciones electrónicas",
  "tipo": "limite_cualitativo",
  "description": "Si hubiera pactado el débito automático del resumen de la tarjeta, aplicará el tipo de cambio vendedor para operaciones efectuadas a través de medios electrónicos de pago del cierre del mismo día hábil del pago"
 },
 "provenances": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "Punto 2.3. Recaudos mínimos de la relación de consumo. (parte 6)"
  }
 ]
}
```

(Hecho: el nodo del 4a no aparece en este barrido porque su id/label/properties no contienen
ninguno de los términos {limite, monto, umbral, usd, mensual}.)

---

## Tabla resumen — verificación × resultado

| # | Verificación | Resultado (hechos; evidencia arriba) |
|---|---|---|
| 1a | Nodo del operador de cambio | 1 único nodo: `EntidadFinanciera_operador_de_cambio`; properties = `{categoria: "operador de cambio"}`; provenance única: TO_proteccion, **"Punto 1.1. Partes."** (§1a) |
| 1b | Edges de ese nodo | **2 en total** (1 saliente `ejecuta → Operacion_operacion_de_cambio`, 1 entrante `aplica_a`); ambos con provenance de TO_proteccion "Punto 1.1. Partes." (§1b) |
| 1c | Candidatos "entidad autorizada"/"autorizadas a operar"/"intervencion de entidades" | 3 nodos (1 TO_capitales/CNV, 2 TO_exterior 1.7 y 13.1); **ninguno con edge hacia/desde el nodo del operador de cambio** (§1c) |
| 1d | Arista operador-de-cambio ↔ entidad-autorizada/mercado-de-cambios | **0 aristas** sobre los 6.634 edges del grafo (§1d) |
| 2a | Portador del 4.5 (lookup) | Existe; `descripcion` verbatim con la regla ("...no serán objeto de clasificación"); dos campos de texto (`descripcion`/`description`); provenance location = "Punto 4.4. Financiaciones cubiertas con garantías preferidas 'A'." (§2a) |
| 2b | Tokens indexados | 17 tokens (label+id); el id truncado indexa **`garanti`**, no `garantias`; la descripcion no se indexa (§2b) |
| 2c | Las 10 consultas de la trayectoria | **0/10 en top-10**; mejor rank 13 (paso 7); score 0 en las 3 consultas "garantías preferidas A ..." sin otra palabra del portador (`garantias` ≠ `garanti`); rank 1141 en paso 8 (§2c) |
| 2d | Consultas inversas (palabras del nodo) | Ambas devuelven el portador en **posición 1** (§2d) |
| 3a | Frecuencia general del R.I.-C.M. | 5 candidatos con (términos)∧mensual en id/label/properties; el texto "La información tendrá frecuencia mensual..." (1.1) aparece solo en la **location de provenance** del nodo TextoOrdenado, no en properties de ningún nodo (§3a) |
| 3b | "0,08" / "0.08" / "70100000" / "APRc" / "APR_c" | "0,08": 4 nodos · "0.08": AUSENTE · "70100000": 2 nodos · "APRc": AUSENTE · "APR_c": 3 nodos (todos pegados íntegros en §3b) |
| 4a | Nodo débito en cuenta (lookup) | Existe; `description` = "La operación se curse con débito en cuenta del cliente en entidades financieras locales." — **sin monto/umbral**; provenance Punto 3.8 (§4a) |
| 4b | "debito" + {limite,monto,umbral,usd,mensual} | **1 candidato**, y es de otro dominio (tipo de cambio para débito automático de tarjeta, TO_proteccion 2.3); ningún nodo del grafo combina débito-en-cuenta con un monto/límite (§4b) |

---

## Archivos abiertos durante esta tarea

Del repo (todos SOLO LECTURA):

- `data/experiment/evaluacion/harness.py` (lectura parcial: tokenización `_tokens`/`_strip_accents`/`GraphIndex.__init__`, líneas 96-147)
- `data/experiment/evaluacion/posthoc_run/traces/off/run_3/CQ-031.json` (lectura programática: las 10 consultas verbatim de `trace.steps`)
- `data/experiment/run_3_ppf_core/kg.json` (lectura programática vía `loader.load_graph("run_3")`)
- `data/experiment/evaluacion/loader.py`, `data/experiment/evaluacion/harness.py` (vía import del script)

Fuera del repo (scratchpad de sesión): `verificaciones_vara.py` (script) y
`out_verificaciones.txt` (output crudo completo, 492 líneas).

**`posthoc_run/dev_set/gate2_v57/` NO fue abierto** (ni listado ni leído ningún archivo suyo
en esta tarea).

---

*Fin de las verificaciones. Sin adjudicación: los hechos quedan a disposición de la
re-adjudicación externa.*
