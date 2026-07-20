# Evidencia complementaria para la adjudicación de CQ-034 (run_3)

Fecha: 2026-07-15. Solo lectura; única escritura: este archivo. **Sellado respetado:**
`posthoc_run/dev_set/gate2_v57/` no fue abierto (lista de archivos abiertos al final).
**Sin adjudicación:** solo material verbatim con rutas de origen y barridos con comando+output.

---

## 1. Respuesta final del agente de run_3 para CQ-034 — verbatim y completa

### 1.1 Fuente: `posthoc_run/traces/off/run_3/CQ-034.json` → `[0].trace.final_json`

(Es la corrida post-hoc thinking-OFF cuya trayectoria de 15 pasos fue la auditada en
`auditoria_truncamiento_run3.md`; en OFF el request es byte-idéntico al frozen.)

```json
{
 "respuesta": "Según la regulación del BCRA, para personas humanas residentes que compran moneda extranjera para atesorar: si la operación se realiza en efectivo, el límite mensual es de USD 100 (dólares estadounidenses cien) en el mes calendario. Sin embargo, la información disponible en el Knowledge Graph no contiene especificaciones sobre el límite mensual diferenciado cuando la operación se cursa con débito en cuenta, ni sobre el límite general que rige para otras modalidades de formación de activos externos.",
 "citas": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 3.8. Compra de moneda extranjera por parte de personas humanas residentes para la formación de activos externos"
  }
 ],
 "respondible": false
}
```

Mismo archivo, `trace.final_raw` (el turno final íntegro del agente, 1.426 chars — incluye la
prosa previa al JSON):

```
Basándome en la información recolectada del Knowledge Graph, he encontrado evidencia sobre el límite de compra en efectivo (USD 100 mensual), pero no he podido localizar en el grafo información específica sobre:

1. El límite mensual para operaciones cursadas con débito en cuenta
2. El límite general para otras modalidades de formación de activos externos

La búsqueda reveló que existe una restricción de USD 100 mensual cuando se utiliza efectivo, y que existe una obligación de cursar la operación con débito en cuenta, pero no encontré nodos que especifiquen el monto límite diferenciado para débito en cuenta ni para otras modalidades.

```json
{
  "respuesta": "Según la regulación del BCRA, para personas humanas residentes que compran moneda extranjera para atesorar: si la operación se realiza en efectivo, el límite mensual es de USD 100 (dólares estadounidenses cien) en el mes calendario. Sin embargo, la información disponible en el Knowledge Graph no contiene especificaciones sobre el límite mensual diferenciado cuando la operación se cursa con débito en cuenta, ni sobre el límite general que rige para otras modalidades de formación de activos externos.",
  "citas": [
    {
      "source_doc": "TO_exterior_cambios_actual.pdf",
      "location": "Punto 3.8. Compra de moneda extranjera por parte de personas humanas residentes para la formación de activos externos"
    }
  ],
  "respondible": false
}
```
```

### 1.2 Fuente: `frozen_run/traces/run_3/CQ-034.json` — las 3 repeticiones del frozen

El frozen registra la respuesta de cada rep en el campo `respuesta` (con `citas` y
`respondible`). Las tres, verbatim:

**Rep 1** (`respondible: false`):

> "Según la regulación del BCRA, para una persona humana residente que compra moneda extranjera para atesorar: si la operación se realiza en efectivo, el límite mensual es de USD 100 (dólares estadounidenses cien) en el mes calendario. Sin embargo, la información disponible en el Knowledge Graph no especifica explícitamente el límite mensual diferenciado para operaciones cursadas con débito en cuenta, ni el límite general que rige para otras modalidades de formación de activos externos. La normativa consultada (Punto 3.8 del Textual Ordenado sobre Operaciones de Cambios) establece estas restricciones, pero los detalles completos de los límites por modalidad no están completamente documentados en los nodos accesibles."

citas: `[{"source_doc": "TO_exterior_cambios_actual.pdf", "location": "Punto 3.8. Compra de moneda extranjera por parte de personas humanas residentes para la formación de activos externos"}]`

**Rep 2** (`respondible: false`):

> "Según la regulación del BCRA, si la operación de compra de moneda extranjera para atesorar se realiza en efectivo, el límite mensual es de USD 100 (dólares estadounidenses cien) en el mes calendario. Sin embargo, la información disponible en el Knowledge Graph no contiene los límites específicos para operaciones cursadas con débito en cuenta ni el límite general que rige para otras modalidades de formación de activos externos."

citas: ídem rep 1.

**Rep 3** (`respondible: false`):

> "Según la regulación del BCRA, para una persona humana residente que compra moneda extranjera para atesorar: si la operación se realiza en efectivo, el límite mensual es de USD 100 (dólares estadounidenses cien) en el mes calendario. Sin embargo, la información disponible en el Knowledge Graph no contiene los límites específicos diferenciados para operaciones cursadas con débito en cuenta ni el límite general que rige para otras modalidades de formación de activos externos. Se requeriría acceso a la normativa completa del Punto 3.8 del Textual Ordenado de Exterior y Cambios para obtener esta información completa."

citas: ídem rep 1.

Hecho: las 4 respuestas (post-hoc OFF + 3 reps frozen) afirman el límite USD 100 en efectivo
citando el Punto 3.8, y declaran no disponer del límite para débito en cuenta ni del límite
general para otras modalidades; todas con `respondible: false`.

---

## 2. Veredictos del JUEZ para run_3/CQ-034 en el frozen run

### 2.1 Qué registra el frozen (y qué no) — importante para leer esta sección

Los archivos del frozen (`frozen_run/traces/run_3/CQ-034.json`, `frozen_run/agg_run_3.json`,
`frozen_run/checkpoint_run_3.md`, `frozen_run/reporte_final.md`) **NO persisten una lista de
claims con marca individual (verdadero/falso/no_soportado) ni el campo `cobertura_patas`**:
por rep persiste el **veredicto agregado** del juez (con `afirmaciones_no_soportadas` como
lista — vacía en este caso — y `justificacion` que resume las marcas). El registro por claim
y `cobertura_patas` SÍ existe en el juez de la corrida post-hoc (mismo juez v2.1.1 de dos
pasos), que se pega en §2.4 con su ruta, claramente rotulado como post-hoc.

### 2.2 Veredicto del juez por rep — verbatim de `frozen_run/traces/run_3/CQ-034.json` (campo `verdict`)

**Rep 1:**

```json
{
 "correctitud": "correcta",
 "completitud": "parcial",
 "cita_documento_correcto": true,
 "cita_precision": "punto",
 "abstencion": null,
 "especulacion_en_prosa": null,
 "afirmaciones_no_soportadas": {
  "centrales": [],
  "secundarias": [],
  "n_centrales": 0,
  "n_secundarias": 0
 },
 "requiere_adjudicacion_humana": false,
 "justificacion": {
  "correctitud": "Centrales todas verdaderas o no_soportadas; ninguna afirmación falsa.",
  "completitud": "Patas no cubiertas: Límite mensual para compra de moneda extranjera para atesorar cursada con débito en cuenta; Límite general para otras modalidades de formación de activos externos",
  "citas": "La cita apunta correctamente al Punto 3.8 del TO sobre Operaciones de Cambios, que es uno de los documentos del ground truth."
 }
}
```

**Rep 2:**

```json
{
 "correctitud": "correcta",
 "completitud": "parcial",
 "cita_documento_correcto": true,
 "cita_precision": "punto",
 "abstencion": null,
 "especulacion_en_prosa": null,
 "afirmaciones_no_soportadas": {
  "centrales": [],
  "secundarias": [],
  "n_centrales": 0,
  "n_secundarias": 0
 },
 "requiere_adjudicacion_humana": false,
 "justificacion": {
  "correctitud": "Centrales todas verdaderas o no_soportadas; ninguna afirmación falsa.",
  "completitud": "Patas no cubiertas: Límite mensual para compra de moneda extranjera para atesorar con débito en cuenta; Límite general para otras modalidades de formación de activos externos",
  "citas": "La cita apunta correctamente al TO_exterior_cambios_actual.pdf, Punto 3.8, que es uno de los documentos del ground truth."
 }
}
```

**Rep 3:**

```json
{
 "correctitud": "correcta",
 "completitud": "parcial",
 "cita_documento_correcto": true,
 "cita_precision": "punto",
 "abstencion": null,
 "especulacion_en_prosa": null,
 "afirmaciones_no_soportadas": {
  "centrales": [],
  "secundarias": [],
  "n_centrales": 0,
  "n_secundarias": 0
 },
 "requiere_adjudicacion_humana": false,
 "justificacion": {
  "correctitud": "Centrales todas verdaderas o no_soportadas; ninguna afirmación falsa.",
  "completitud": "Patas no cubiertas: Límite mensual aplicable cuando la compra de moneda extranjera para atesorar se cursa con débito en cuenta; Límite general que rige para otras modalidades de formación de activos externos",
  "citas": "La cita apunta al documento correcto (TO_exterior_cambios_actual.pdf) y al Punto 3.8, que es uno de los ground truth sections."
 }
}
```

Hechos del frozen: en las 3 reps `correctitud = "correcta"`, `completitud = "parcial"`,
`afirmaciones_no_soportadas` vacía (0 centrales, 0 secundarias), y la justificación de
completitud nombra en las 3 las mismas dos patas no cubiertas (débito en cuenta; límite
general otras modalidades).

### 2.3 Agregado del frozen — verbatim de `frozen_run/agg_run_3.json` (entrada `qid == "CQ-034"`)

```json
"agg": {
 "n_reps": 3,
 "n_validas": 3,
 "dimensiones": {
  "correctitud":            {"modal": "correcta", "unanime": true, "distribucion": {"\"correcta\"": 3}, "n": 3},
  "completitud":            {"modal": "parcial",  "unanime": true, "distribucion": {"\"parcial\"": 3},  "n": 3},
  "cita_documento_correcto":{"modal": true,       "unanime": true, "distribucion": {"true": 3},         "n": 3},
  "cita_precision":         {"modal": "punto",    "unanime": true, "distribucion": {"\"punto\"": 3},    "n": 3}
 }
}
```

(Los `reps_meta` registran además `respondible: false` y `hit_tool_limit: true` en las 3 reps.)

En `frozen_run/reporte_final.md`, "CQ-034" aparece solo en filas de **run_5**
(líneas 74 y 144: `run_5 | CQ-034 | ... | incorrecta`); no hay fila de run_3/CQ-034 entre las
destacadas. `frozen_run/checkpoint_run_3.md` no menciona CQ-034 (grep sin matches).

### 2.4 Registro por claim y `cobertura_patas` — juez POST-HOC (v2.1.1, dos pasos)

Fuente: `posthoc_run/traces/off/run_3/CQ-034.json` → `[0].judge.step1` / `[0].judge.step2`.
(NO es el frozen; se pega porque es el único archivo donde el juez registra claims con marca
y `cobertura_patas` para run_3/CQ-034. El veredicto agregado de este juez post-hoc,
`[0].judge.verdict`, es idéntico en dimensiones al de las reps del frozen: correcta / parcial /
true / punto.)

`judge.step1` (descomposición):

```json
{
 "afirmaciones_verificables": [
  {
   "enunciado": "Para personas humanas residentes que compran moneda extranjera para atesorar en efectivo, el límite mensual es de USD 100 en el mes calendario.",
   "central": true
  }
 ],
 "reportes_de_alcance": [
  "La información disponible en el Knowledge Graph no contiene especificaciones sobre el límite mensual diferenciado cuando la operación se cursa con débito en cuenta.",
  "La información disponible en el Knowledge Graph no contiene especificaciones sobre el límite general que rige para otras modalidades de formación de activos externos."
 ],
 "patas_de_la_pregunta": [
  "Límite mensual aplicable cuando la compra de moneda extranjera para atesorar se cursa con débito en cuenta",
  "Límite mensual aplicable cuando la compra de moneda extranjera para atesorar se realiza en efectivo",
  "Límite general que rige para otras modalidades de formación de activos externos"
 ]
}
```

`judge.step2` (marcas por claim + cobertura de patas):

```json
{
 "verificaciones": [
  {
   "enunciado": "Para personas humanas residentes que compran moneda extranjera para atesorar en efectivo, el límite mensual es de USD 100 en el mes calendario.",
   "central": true,
   "verdict": "verdadero"
  }
 ],
 "cobertura_patas": [
  {"pata": "Límite mensual aplicable cuando la compra de moneda extranjera para atesorar se cursa con débito en cuenta", "cobertura": "no_cubierta"},
  {"pata": "Límite mensual aplicable cuando la compra de moneda extranjera para atesorar se realiza en efectivo", "cobertura": "cubierta"},
  {"pata": "Límite general que rige para otras modalidades de formación de activos externos", "cobertura": "no_cubierta"}
 ],
 "cita_documento_correcto": true,
 "cita_precision": "punto",
 "abstencion": "correcta",
 "especulacion_en_prosa": false,
 "justificacion": {
  "citas": "La cita apunta al documento correcto (TO_exterior_cambios_actual.pdf) y al Punto 3.8, que es uno de los ground truth sections.",
  "abstencion": "El agente responde parcialmente la pregunta (USD 100 en efectivo) y reporta correctamente que no dispone de información sobre las otras dos patas, sin inventar valores ni citas."
 }
}
```

Hechos del post-hoc: **un único claim verificable**, marcado **"verdadero"** (el USD 100 en
efectivo); las declaraciones de no-disponibilidad se clasificaron como `reportes_de_alcance`
(no como claims); `cobertura_patas`: **efectivo = cubierta; débito en cuenta = no_cubierta;
otras modalidades = no_cubierta**.

---

## 3. Barrido programático sobre el kg.json de run_3 — ¿existe un portador del límite del Punto 3.9?

Mismo mecanismo del punto 4(b) de `auditoria_truncamiento_run3.md`:
`loader.load_graph("run_3")` (4.050 nodos) y match por regex sobre el JSON normalizado
(lowercase, sin acentos) de `{id, label, properties}` de cada nodo, con pasada separada sobre
`provenances` (se reporta si el match es SOLO de provenance).

Comando (núcleo del script):

```python
kg = loader.load_graph("run_3")   # 4050 nodos
TERMS = {
    "'200' numero suelto": r"(?<![\d.,])200(?![\d.,])",   # excluye 100.000/200.000/1.200 etc.
    "'3.9' punto":         r"(?<![\d.])3\.9(?!\d)",       # excluye 13.9 / 3.90 etc.
    "'otras modalidades'": r"otras modalidades",
    "'activos externos'":  r"activos externos",
    "'ayuda familiar'":    r"ayuda familiar",
    "'derivados'":         r"derivados",
}
# por nodo: props_blob = norm(json({id,label,properties})); prov_blob = norm(json(provenances))
# match en props_blob -> candidato "P"; si no, match en prov_blob -> candidato "v"
```

Resumen de conteos (output del barrido):

```
run_3: 4050 nodos
['200' numero suelto]  en id/label/properties: 1  | SOLO en provenances: 0
['3.9' punto]          en id/label/properties: 1  | SOLO en provenances: 1
['otras modalidades']  en id/label/properties: 0  | SOLO en provenances: 0
['activos externos']   en id/label/properties: 12 | SOLO en provenances: 0
['ayuda familiar']     en id/label/properties: 1  | SOLO en provenances: 0
['derivados']          en id/label/properties: 97 | SOLO en provenances: 27
```

### 3.1 "200" como número suelto — 1 candidato, contenido completo

```json
{
 "id": "Restriccion_el_limite_se_incrementa_a_usd_200_por_operacion_por_los_retiros_de_efectivo_que_",
 "type": "Restriccion",
 "label": "Límite adelanto países no limítrofes",
 "properties": {
  "descripcion": "El límite se incrementa a USD 200 por operación por los retiros de efectivo que se realicen en países no limítrofes",
  "tipo": "limite_cuantitativo",
  "umbral": "USD 200"
 },
 "provenances": [
  {"source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 4.1. Operaciones con débito en una cuenta en una entidad financiera local y/o con tar"}
 ]
}
```

### 3.2 "3.9" — 2 candidatos, contenido completo

Match en properties (la descripción menciona "3.9." dentro de una lista de puntos):

```json
{
 "id": "Excepcion_este_requisito_no_resultara_a_aplicacion_para_aquellas_operaciones_de_egresos_qu",
 "type": "Excepcion",
 "label": "Excepción operaciones específicas",
 "properties": {
  "descripcion": "Este requisito no resultará a aplicación para aquellas operaciones de egresos que correspondan a: operaciones de clientes realizadas en el marco de los puntos 3.8., 3.9., 3.13., 3.14.1. y 3.14.2.; operaciones propias de una entidad en carácter de cliente; cancelaciones de financiaciones en moneda extranjera otorgadas por entidades financieras locales por los consumos en moneda extranjera efectuados mediante tarjetas de crédito o de compra; o pagos al exterior de las empresas no financieras emisoras de tarjetas"
 },
 "provenances": [
  {"source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 3.16. Requisitos complementarios para los egresos por el mercado de cambios. (parte 1)"}
 ]
}
```

Match SOLO en provenances (la location contiene "Punto 3.9"; las properties del nodo son solo
los metadatos de la comunicación):

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
  {"source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 3.9. A 6770 6."}
 ]
}
```

### 3.3 "otras modalidades" — 0 candidatos

```
['otras modalidades'] en id/label/properties: 0 | SOLO en provenances: 0
```

### 3.4 "activos externos" — 12 candidatos, contenido completo

```json
{
 "id": "Operacion_formacion_de_activos_externos",
 "type": "Operacion",
 "label": "Formación de activos externos",
 "properties": {"tipo": "formación de activos externos"},
 "provenances": [
  {"source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 3.10. Compra de moneda extranjera por parte de otros residentes –excluidas las entidad"}
 ]
}
```

```json
{
 "id": "Obligacion_obtener_conformidad_previa_bcra",
 "type": "Obligacion",
 "label": "Obtener conformidad previa BCRA",
 "properties": {
  "tipo": "otra",
  "description": "El acceso al mercado de cambios requerirá la conformidad previa del BCRA para la formación de activos externos y para la operatoria con derivados"
 },
 "provenances": [
  {"source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 3.10. Compra de moneda extranjera por parte de otros residentes –excluidas las entidad"}
 ]
}
```

```json
{
 "id": "Operacion_compra_de_moneda_extranjera",
 "type": "Operacion",
 "label": "Compra de moneda extranjera",
 "properties": {
  "tipo": "compra de moneda extranjera",
  "description": "Compra de moneda extranjera por parte de personas humanas residentes para la formación de activos externos en forma de billetes y/o depósitos"
 },
 "provenances": [
  {"source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 3.11. Otras compras de moneda extranjera por parte de residentes con aplicación especí"}
 ]
}
```

```json
{
 "id": "Obligacion_la_entidad_debera_contar_con_una_declaracion_jurada_del_cliente_en_la_que_deje_c",
 "type": "Obligacion",
 "label": "Declaración jurada de tenencias de activos",
 "properties": {
  "descripcion": "La entidad deberá contar con una declaración jurada del cliente en la que deje constancia de sus tenencias de activos externos líquidos y/o certificados de depósitos argentinos representativos de acciones extranjeras",
  "tipo": "presentacion_informativa"
 },
 "provenances": [
  {"source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 3.16. Requisitos complementarios para los egresos por el mercado de cambios. (parte 1)"}
 ]
}
```

```json
{
 "id": "Restriccion_no_poseia_activos_externos_liquidos_disponibles_que_conjuntamente_tengan_un_valo",
 "type": "Restriccion",
 "label": "Límite de activos externos líquidos",
 "properties": {
  "descripcion": "No poseía activos externos líquidos disponibles que conjuntamente tengan un valor superior al equivalente de USD 100.000 (dólares estadounidenses cien mil)",
  "tipo": "limite_cuantitativo",
  "umbral": "USD 100.000"
 },
 "provenances": [
  {"source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 3.16. Requisitos complementarios para los egresos por el mercado de cambios. (parte 1)"}
 ]
}
```

```json
{
 "id": "Operacion_tenencia_de_activos_externos_liquidos",
 "type": "Operacion",
 "label": "Tenencia de activos externos líquidos",
 "properties": {"tipo": "tenencia de activos externos liquidos"},
 "provenances": [
  {"source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 3.16. Requisitos complementarios para los egresos por el mercado de cambios. (parte 1)"}
 ]
}
```

```json
{
 "id": "Restriccion_no_ha_realizado_canjes_de_titulos_valores_emitidos_por_residentes_por_activos_ex",
 "type": "Restriccion",
 "label": "Prohibición de canje de títulos valores",
 "properties": {
  "descripcion": "no ha realizado canjes de títulos valores emitidos por residentes por activos externos",
  "tipo": "prohibicion"
 },
 "provenances": [
  {"source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 3.16. Requisitos complementarios para los egresos por el mercado de cambios. (parte 2)"}
 ]
}
```

```json
{
 "id": "Restriccion_no_ha_entregado_fondos_en_moneda_local_ni_otros_activos_locales_a_cambio_de_acti",
 "type": "Restriccion",
 "label": "Prohibición de entrega de fondos locales",
 "properties": {
  "descripcion": "no ha entregado fondos en moneda local ni otros activos locales a cambio de activos externos, criptoactivos o títulos valores depositados en el exterior",
  "tipo": "prohibicion"
 },
 "provenances": [
  {"source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 3.16. Requisitos complementarios para los egresos por el mercado de cambios. (parte 2)"}
 ]
}
```

```json
{
 "id": "Obligacion_se_compromete_a_no_realizara_canjes_de_titulos_valores_emitidos_por_residentes_p",
 "type": "Obligacion",
 "label": "Compromiso de no canje de títulos",
 "properties": {
  "descripcion": "se compromete a no realizará canjes de títulos valores emitidos por residentes por activos externos",
  "tipo": "otra"
 },
 "provenances": [
  {"source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 3.16. Requisitos complementarios para los egresos por el mercado de cambios. (parte 2)"}
 ]
}
```

```json
{
 "id": "Obligacion_se_compromete_a_no_entregara_fondos_en_moneda_local_ni_otros_activos_locales_par",
 "type": "Obligacion",
 "label": "Compromiso de no entrega de fondos",
 "properties": {
  "descripcion": "se compromete a no entregará fondos en moneda local ni otros activos locales para recibir activos externos, criptoactivos o títulos valores depositados en el exterior",
  "tipo": "otra"
 },
 "provenances": [
  {"source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 3.16. Requisitos complementarios para los egresos por el mercado de cambios. (parte 2)"}
 ]
}
```

```json
{
 "id": "Operacion_posicion_de_cambios",
 "type": "Operacion",
 "label": "Posición general de cambios",
 "properties": {
  "tipo": "posicion de cambios",
  "description": "Totalidad de los activos externos líquidos de la entidad, netos de los saldos deudores de corresponsalía originados en la operatoria del mercado de cambios. Incluye compras y ventas concertadas en el mercado de cambios pendientes de liquidación."
 },
 "provenances": [
  {"source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 6.7. Posición general de cambios (PGC)."}
 ]
}
```

```json
{
 "id": "Restriccion_exclusion_de_activos_de_la_pgc",
 "type": "Restriccion",
 "label": "Exclusión de activos de la PGC",
 "properties": {
  "tipo": "limite_cualitativo",
  "description": "No formarán parte de la PGC: inversiones directas en el exterior, activos externos de terceros en custodia, ventas y compras a término de divisas o valores externos, depósitos en el BCRA en moneda extranjera en cuentas a nombre de la entidad y demás activos locales en moneda extranjera."
 },
 "provenances": [
  {"source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 6.7. Posición general de cambios (PGC)."}
 ]
}
```

### 3.5 "ayuda familiar" — 1 candidato, contenido completo

```json
{
 "id": "Operacion_transferencia_de_ayuda",
 "type": "Operacion",
 "label": "Transferencias de ayuda familiar",
 "properties": {
  "tipo": "transferencia de ayuda",
  "description": "Ingreso y remisión de transferencias en concepto de ayuda familiar"
 },
 "provenances": [
  {"source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 4.2. Operaciones cursadas a través del Sistema de Monedas Locales (SML)."}
 ]
}
```

### 3.6 "derivados" — 97 + 27 candidatos (decisión de alcance, declarada)

El término devuelve **124 nodos**, en su inmensa mayoría del TO de Capitales Mínimos
(instrumentos derivados: OTC, nocional, márgenes, CVA, coberturas, etc.). Pegar el contenido
completo de los 124 no aporta al objetivo del barrido (portador del límite del 3.9), así que
se aplica un recorte declarado: la **lista completa de los 124 ids queda registrada** (abajo)
y el contenido completo se pega **solo para el subconjunto con provenance del TO de Exterior
y Cambios** (el espacio donde podría vivir un portador del 3.9): **3 nodos**.

Lista completa de ids (P = match en id/label/properties; v = match solo en provenances):

```
P Operacion_derivados_de_credito
P Operacion_compensacion
P Operacion_inversion_estructurada
P Excepcion_se_excluye_de_este_tratamiento_a_los_titulos_entregados_en_garantia_de_las_opera
P Operacion_pasivos_por_instrumentos_derivados_contabilizados_a_valor_razonable
P Restriccion_en_el_caso_de_pasivos_por_instrumentos_derivados_contabilizados_a_valor_razonabl
P Operacion_inversion_en_instrumento_cuyo_valor_esta_relacionado_al_capital
P Restriccion_no_se_podran_hacer_coberturas_entre_las_cuatro_grandes_categorias_de_derivados_s
P Operacion_compensacion_de_adicionales_en_derivados
P Operacion_operacion_con_derivados_sobre_indices_de_credito
P Operacion_operacion_con_derivados_sobre_acciones
P Operacion_operacion_con_derivados_sobre_commodities
P Obligacion_los_derivados_que_hagan_referencia_a_indices_de_credito_se_consideraran_como_si_
P Obligacion_se_utilizara_un_modelo_de_factor_unico_para_dividir_el_riesgo_de_cada_entidad_de
P Obligacion_la_compensacion_o_cobertura_total_estaran_permitidas_entre_todas_las_operaciones
P Operacion_operacion_con_derivados_otc
P Operacion_derivado_de_credito
P Obligacion_la_documentacion_provisional_inicial_oferta_o_prospecto_provisional_y_de_apoyo_t
P Obligacion_tambien_deberian_incluirse_disposiciones_que_contemplen_el_reemplazo_de_los_admi
P Restriccion_las_tasas_de_interes_o_de_descuento_de_referencia_deberan_ser_tasas_de_interes_d
P Restriccion_los_unicos_derivados_admisibles_son_los_que_se_toman_para_la_genuina_cobertura_d
P Restriccion_las_coberturas_que_no_se_realicen_a_traves_de_derivados_solo_seran_admisibles_si
P Operacion_calculo_de_cva_para_derivados_realizados_por_el_fondo
P Operacion_derivados_otc
P Operacion_derivados_sobre_materias_primas
P Restriccion_al_limite_de_derivados_sobre_materias_primas_o_productos_basicos_commodities_pre
P Obligacion_exigencia_por_riesgo_de_credito_de_contraparte_en_operaciones_con_derivados_extr
P Operacion_operaciones_con_derivados_otc
P Operacion_operaciones_con_derivados_en_mercados_regulados
P Operacion_operacion_con_derivados_sin_intercambio_de_margen_de_variacion
P Operacion_operacion_con_derivados_con_acuerdo_de_margen_de_variacion
P Obligacion_para_operaciones_sin_margen_el_cr_se_define_como_v_c_donde_v_es_el_valor_actual_
P Obligacion_las_operaciones_se_ajustaran_a_procedimientos_de_asignacion_de_cada_derivado_a_u
P Obligacion_para_derivados_de_tasa_de_interes_y_creditos_el_nocional_ajustado_sera_el_produc
P Operacion_operacion_con_nocional_variable
P Obligacion_emplear_promedio_ponderado_de_nocional
P Excepcion_esta_regla_no_sera_aplicable_a_las_operaciones_en_las_que_el_nocional_varia_debi
P Operacion_derivados_que_no_son_opciones_ni_segmentos_de_cdo
P Restriccion_operaciones_sin_margen_de_variacion_horizonte_temporal_minimo_sera_el_menor_entr
P Operacion_derivados
P Operacion_basis_transactions
P Restriccion_cuando_se_aplique_a_conjuntos_de_cobertura_de_derivados_sobre_bases_el_sf_corres
P Operacion_derivados_fx
P Operacion_operaciones_sobre_volatilidad
P Operacion_operacion_con_derivado
P Restriccion_periodo_de_riesgo_de_margen_minimo_10_dias
P Restriccion_periodo_de_riesgo_de_margen_minimo_5_dias
P Restriccion_no_aplicacion_parametros_correlacion_a_derivados_tasa
P Obligacion_division_derivados_en_categorias_de_plazo
P Operacion_operacion_con_derivados
P Operacion_derivados_over_the_counter
P Operacion_transacciones_bilaterales_con_derivados
P Obligacion_cuando_se_trate_de_una_operacion_con_derivados_concertada_en_un_mercado_de_valor
P Obligacion_la_entidad_financiera_que_actue_en_caracter_de_miembro_compensador_de_una_ccp_po
P Obligacion_la_exposicion_debida_a_dichas_operaciones_se_calculara_conforme_al_enfoque_estan
P Obligacion_en_todos_los_casos_se_utilizara_un_mpor_minimo_de_10_dias_para_el_calculo_de_las
P Obligacion_calculo_de_exposicion_para_derivados
P Obligacion_aplicacion_de_periodos_de_mantenimiento_minimo
P Restriccion_extension_de_periodo_minimo_por_iliquidez
P Restriccion_el_periodo_de_vigencia_del_derivado_de_credito_no_podra_ser_inferior_a_cualquier
P Operacion_liquidacion_en_efectivo
P Restriccion_si_el_importe_del_derivado_fuera_inferior_o_igual_al_de_la_obligacion_subyacente
P Restriccion_no_podran_reconocerse_como_crc_otros_tipos_de_derivados_de_credito_incluyendo_a_
P Operacion_derivados_de_incumplimiento_multiple
P Operacion_operaciones_en_mercado_de_capitales
P Obligacion_los_acuerdos_deben_tener_validez_legal_en_toda_jurisdiccion_pertinente_ante_even
P Restriccion_se_reconoceran_solo_las_garantias_emitidas_o_proteccion_provista_en_el_caso_de_d
P Obligacion_se_reconocera_la_proteccion_crediticia_provista_por_entes_admisibles_cuando_las_
P Operacion_compra_venta_de_derivados
P Obligacion_calcular_exigencia_capital_riesgo_credito_contraparte
P Obligacion_calcular_exigencia_capital_riesgo_especifico
P Restriccion_limite_neteamiento_posiciones_mismo_instrumento
P Operacion_calculo_de_cobertura
P Operacion_cobertura_con_instrumentos_derivados_de_credito
P Obligacion_calcular_independientemente_posiciones_netas
P Operacion_clasificacion_de_titulos_de_deuda
P Operacion_exclusion_de_posiciones
P Obligacion_el_sistema_de_medicion_debera_abarcar_a_todos_los_derivados_de_tasas_de_interes_
P Obligacion_los_derivados_se_deberan_convertir_a_posiciones_en_el_correspondiente_subyacente
P Restriccion_los_swaps_de_monedas_y_tasas_de_interes_los_fras_los_forwards_de_moneda_y_los_fu
P Obligacion_aplicar_exigencia_capital_por_riesgo_general_mercado_a_todas_posiciones_derivado
P Obligacion_incluir_derivados_en_computo
P Excepcion_exclusion_de_opciones
P Obligacion_convertir_derivados_a_posiciones_nocionales
P Operacion_cobertura_derivados
P Operacion_pago_por_servicios_derivados_de_operacion_de_recompra_y_o_rescate_de_deudas
P Obligacion_obtener_conformidad_previa_bcra
P Excepcion_excepcion_de_derivados_instrumentados_bajo_ley_argentina
P Obligacion_los_sujetos_obligados_deberan_contratar_un_seguro_sobre_saldo_deudor_con_cobertu
P Operacion_operaciones_con_derivados_otc_o_negociados_en_mercados_regulados_con_liquidacion
P Obligacion_se_consignara_el_valor_de_la_exigencia_por_riesgo_general_de_acciones_adicional_
P Operacion_instrumentos_derivados
P Obligacion_se_informaran_los_incrementos_a_la_exigencia_segun_riesgo_de_credito_generados_p
P Operacion_verificacion_de_limites_en_posiciones_de_derivados_no_cubiertos
P Operacion_derivados_financieros
P Restriccion_incremento_de_la_exigencia_por_riesgo_de_credito_por_exceso_en_posiciones_de_der
P Obligacion_informacion_de_incumplimientos_de_posiciones_de_derivados_sobre_commodities_del_
v Obligacion_determinacion_de_nocional_efectivo
v Obligacion_calculo_de_factor_sf_regulatorio
v Restriccion_las_franquicias_por_debajo_de_las_cuales_no_se_recibira_compensacion_en_caso_de_
v Restriccion_de_haber_descalce_de_plazos_de_vencimiento_la_crc_que_tenga_un_plazo_de_vencimie
v Restriccion_cuando_la_proteccion_crediticia_y_la_exposicion_esten_denominadas_en_distintas_m
v Operacion_sustitucion_de_ponderador_de_riesgo_de_contraparte_por_garante
v Operacion_cobertura_proporcional_de_riesgo_con_reduccion_de_capital
v Operacion_transferencia_de_riesgo_en_tramos_con_proteccion_crediticia
v Operacion_calculo_de_mayor_plazo_de_vencimiento_residual_posible
v Operacion_calculo_de_menor_plazo_de_vencimiento_por_opciones
v Operacion_aplicacion_de_formula_de_ajuste_por_descalce_de_plazos
v Operacion_aplicacion_de_aforo_por_descalce_de_monedas
v Obligacion_se_reconocera_la_proteccion_crediticia_en_la_medida_de_que_el_ponderador_de_ries
v Obligacion_los_plazos_de_vencimiento_deberan_medirse_en_forma_conservadora_considerando_el_
v Obligacion_con_relacion_a_la_crc_se_debera_tener_en_cuenta_las_opciones_incorporadas_que_pu
v Obligacion_el_aforo_por_descalce_de_monedas_debera_incrementarse_proporcionalmente_utilizan
v EntidadFinanciera_sociedad_de_garantia_reciproca
v EntidadFinanciera_fondo_de_garantia_publico
v EntidadFinanciera_banco_multilateral_de_desarrollo
v EntidadFinanciera_organismo_internacional
v EntidadFinanciera_empresa_con_grado_inversion
v Operacion_swap
v Operacion_futuros_y_contratos_a_termino
v Operacion_opciones
v Obligacion_reportar_el_activo_subyacente_activos_comprados_y_vendidos_valores_nocionales_co
v Obligacion_reportar_descripcion_del_activo_comprado_o_vendido_a_futuro_plazo_residual_valor
v Obligacion_reportar_descripcion_del_activo_subyacente_plazo_residual_cantidad_de_activos_cu
```

Contenido completo del subconjunto con provenance de `TO_exterior_cambios_actual.pdf` (3 nodos):

```json
{
 "id": "Operacion_pago_por_servicios_derivados_de_operacion_de_recompra_y_o_rescate_de_deudas",
 "type": "Operacion",
 "label": "Pago servicios recompra/rescate deudas",
 "properties": {"tipo": "pago por servicios derivados de operación de recompra y/o rescate de deudas"},
 "provenances": [
  {"source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 13.3. Pagos de servicios que fueron o serán prestados o devengados a partir del 13/12/"}
 ]
}
```

```json
{
 "id": "Obligacion_obtener_conformidad_previa_bcra",
 "type": "Obligacion",
 "label": "Obtener conformidad previa BCRA",
 "properties": {
  "tipo": "otra",
  "description": "El acceso al mercado de cambios requerirá la conformidad previa del BCRA para la formación de activos externos y para la operatoria con derivados"
 },
 "provenances": [
  {"source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 3.10. Compra de moneda extranjera por parte de otros residentes –excluidas las entidad"}
 ]
}
```

```json
{
 "id": "Excepcion_excepcion_de_derivados_instrumentados_bajo_ley_argentina",
 "type": "Excepcion",
 "label": "Excepción de derivados instrumentados bajo ley argentina",
 "properties": {
  "description": "No están sujetas a estas normas las concertaciones y cancelaciones de operaciones de futuros en mercados regulados, forwards, opciones y cualquier otro tipo de derivado en la medida que estén instrumentadas bajo ley argentina y su liquidación se efectúe en el país por compensación en moneda doméstica, sin que pueda generar obligaciones presentes o futuras de realizar pagos en moneda extranjera"
 },
 "provenances": [
  {"source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 6.4. Operaciones a término."}
 ]
}
```

### 3.7 Resultado del barrido (hechos)

Sobre los 4.050 nodos de run_3, **ningún candidato de ningún término porta un límite de
USD 200 para "otras modalidades de formación de activos externos" (Punto 3.9)**:

- El único "200" suelto es el límite de retiros de efectivo en países no limítrofes (Punto 4.1).
- "3.9" aparece solo (i) citado dentro de una lista de puntos en una excepción del 3.16 y
  (ii) en la location de provenance de la Com. A 6796 ("Punto 3.9. A 6770 6."), un nodo de
  metadatos de comunicación sin contenido normativo.
- "otras modalidades": 0 matches en todo el grafo.
- Los 12 nodos de "activos externos" son operaciones/DDJJ/prohibiciones del 3.10, 3.11, 3.16
  y 6.7; ninguno porta un límite mensual del 3.9.
- "ayuda familiar" da 1 nodo (transferencias vía SML, Punto 4.2), sin límite.
- De los 124 nodos de "derivados", solo 3 tienen provenance de Exterior y ninguno refiere un
  límite del 3.9.

---

## Archivos abiertos durante esta tarea

Del repo (todos SOLO LECTURA):

- `data/experiment/evaluacion/posthoc_run/traces/off/run_3/CQ-034.json` (lectura programática: `final_json`, `final_raw`, `judge`)
- `data/experiment/evaluacion/frozen_run/traces/run_3/CQ-034.json` (lectura programática: respuestas y verdicts de las 3 reps)
- `data/experiment/evaluacion/frozen_run/agg_run_3.json` (lectura programática: entrada CQ-034)
- `data/experiment/evaluacion/frozen_run/reporte_final.md` (grep "CQ-034")
- `data/experiment/evaluacion/frozen_run/checkpoint_run_3.md` (grep "CQ-034", sin matches)
- `data/experiment/run_3_ppf_core/kg.json` (lectura programática vía `loader.load_graph("run_3")`)
- Listados de directorio: `frozen_run/`, `frozen_run/traces/run_3/` (`ls`)

Fuera del repo (scratchpad de sesión): `barrido_cq034.txt` (artefacto intermedio del barrido).

**`posthoc_run/dev_set/gate2_v57/` NO fue abierto** (ni listado ni leído ningún archivo suyo
en esta tarea).

---

*Fin de la evidencia. Sin re-adjudicaciones ni análisis: el material queda a disposición de la
adjudicación externa.*
