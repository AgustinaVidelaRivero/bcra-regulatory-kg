# Auditoría de truncamiento — trayectorias del AGENTE de run_3 (CQ-017, CQ-020, CQ-031, CQ-034)

Fecha: 2026-07-15. Solo lectura; única escritura: este archivo. **CQ-025 fuera de alcance**
(su GT no depende de afirmaciones de ausencia). **Sellado respetado:** ningún archivo de
`posthoc_run/dev_set/gate2_v57/` fue abierto — esta auditoría es sobre las trayectorias del
agente, nunca sobre los veredictos del verificador (lista completa de archivos abiertos al
final). **Sin adjudicación:** este reporte registra hechos (término → paso/posición o
ausente); las re-adjudicaciones quedan fuera de esta sesión.

---

## 0. Mecanismo de re-ejecución determinística (el mismo de fbb3870 / `ver_paso_completo`)

Se replicó exactamente `verificador.py::_ver_paso_completo` ([verificador.py:816-837](../../verificador.py)):
para cada paso `{n, tool, input}` de la traza post-hoc (`posthoc_run/traces/off/run_3/CQ-XXX.json`,
clave `trace.steps`), se re-ejecuta el mismo tool call con el mismo input sobre el **grafo
congelado** (`loader.load_graph("run_3")` → `kg.json` de `run_3_ppf_core`) con el mismo índice
(`harness.GraphIndex`). Determinístico porque el grafo está congelado y las 3 tools de grafo
son funciones puras del índice. Script: `reexec_run3.py` (scratchpad de sesión, fuera del repo).

**Por qué esto audita el truncamiento:** la traza almacena por paso `output_chars` (largo del
output que el agente recibió en runtime) y `output_truncado` (el string guardado, cap
`TRUNC_TOOL_OUTPUT = 1200` chars — [harness.py:59](../../harness.py) y `_truncate`,
[harness.py:318](../../harness.py)). La traza almacenada NO es el contexto del agente; los
outputs completos se recuperan solo por re-ejecución.

**Verificación de fidelidad de la re-ejecución (56/56 pasos):** para CADA paso de los 4 casos,
el largo del output re-ejecutado coincidió EXACTAMENTE con el `output_chars` registrado en
runtime (igualdad en los 56 pasos; columnas "runtime chars" vs "completo re-ejecutado" del
output del script, pegado abajo). Pasos almacenados truncados en traza (guardado < runtime):
CQ-017 **9/15**, CQ-020 **7/11**, CQ-031 **10/15**, CQ-034 **10/15**.

Output del script de re-ejecución (columna `almacenado` = `output_chars` de runtime;
`completo` = largo re-ejecutado):

```
CQ-017: 15 pasos re-ejecutados
  paso  1 buscar_nodos  almacenado=2577 completo=2577
  paso  2 buscar_nodos  almacenado=3814 completo=3814
  paso  3 buscar_nodos  almacenado=3229 completo=3229
  paso  4 ver_nodo      almacenado=285 completo=285
  paso  5 ver_nodo      almacenado=434 completo=434
  paso  6 ver_vecinos   almacenado=771 completo=771
  paso  7 ver_nodo      almacenado=617 completo=617
  paso  8 buscar_nodos  almacenado=3303 completo=3303
  paso  9 ver_nodo      almacenado=895 completo=895
  paso 10 ver_vecinos   almacenado=11828 completo=11828
  paso 11 buscar_nodos  almacenado=2919 completo=2919
  paso 12 ver_nodo      almacenado=682 completo=682
  paso 13 buscar_nodos  almacenado=3002 completo=3002
  paso 14 buscar_nodos  almacenado=2950 completo=2950
  paso 15 buscar_nodos  almacenado=2593 completo=2593
CQ-020: 11 pasos re-ejecutados
  paso  1 buscar_nodos  almacenado=3395 completo=3395
  paso  2 buscar_nodos  almacenado=3203 completo=3203
  paso  3 buscar_nodos  almacenado=2789 completo=2789
  paso  4 ver_nodo      almacenado=457 completo=457
  paso  5 ver_nodo      almacenado=367 completo=367
  paso  6 ver_nodo      almacenado=564 completo=564
  paso  7 buscar_nodos  almacenado=3421 completo=3421
  paso  8 ver_vecinos   almacenado=5312 completo=5312
  paso  9 ver_nodo      almacenado=521 completo=521
  paso 10 buscar_nodos  almacenado=1795 completo=1795
  paso 11 buscar_nodos  almacenado=1724 completo=1724
CQ-031: 15 pasos re-ejecutados
  paso  1 buscar_nodos  almacenado=3179 completo=3179
  paso  2 buscar_nodos  almacenado=3299 completo=3299
  paso  3 ver_nodo      almacenado=402 completo=402
  paso  4 ver_nodo      almacenado=682 completo=682
  paso  5 ver_vecinos   almacenado=782 completo=782
  paso  6 ver_vecinos   almacenado=835 completo=835
  paso  7 buscar_nodos  almacenado=3037 completo=3037
  paso  8 buscar_nodos  almacenado=3837 completo=3837
  paso  9 buscar_nodos  almacenado=3116 completo=3116
  paso 10 buscar_nodos  almacenado=3617 completo=3617
  paso 11 buscar_nodos  almacenado=3134 completo=3134
  paso 12 buscar_nodos  almacenado=3285 completo=3285
  paso 13 ver_nodo      almacenado=526 completo=526
  paso 14 buscar_nodos  almacenado=3732 completo=3732
  paso 15 buscar_nodos  almacenado=3786 completo=3786
CQ-034: 15 pasos re-ejecutados
  paso  1 buscar_nodos  almacenado=3549 completo=3549
  paso  2 buscar_nodos  almacenado=3196 completo=3196
  paso  3 buscar_nodos  almacenado=3369 completo=3369
  paso  4 ver_nodo      almacenado=619 completo=619
  paso  5 ver_nodo      almacenado=498 completo=498
  paso  6 ver_nodo      almacenado=344 completo=344
  paso  7 ver_vecinos   almacenado=554 completo=554
  paso  8 ver_vecinos   almacenado=3182 completo=3182
  paso  9 buscar_nodos  almacenado=3662 completo=3662
  paso 10 buscar_nodos  almacenado=3490 completo=3490
  paso 11 buscar_nodos  almacenado=3446 completo=3446
  paso 12 ver_nodo      almacenado=443 completo=443
  paso 13 buscar_nodos  almacenado=3110 completo=3110
  paso 14 buscar_nodos  almacenado=3085 completo=3085
  paso 15 buscar_nodos  almacenado=4475 completo=4475
```

Convención de "posición" en todo el reporte: en `buscar_nodos`, índice 1-based en la lista
`resultados`; en `ver_vecinos`, índice 1-based en `salientes`/`entrantes`; en `ver_nodo`, el
nodo íntegro. Los barridos por término corren sobre texto normalizado (lowercase, sin acentos).

---

## 1. CQ-031

**Pregunta (verbatim de la traza):** ¿Qué deudores no deben ser objeto de clasificación y
respecto de qué deudores no corresponde evaluar la capacidad de repago?

**Inventario de la trayectoria (15 pasos):**

| paso | tool | input | runtime chars | almacenado en traza |
|---|---|---|---|---|
| 1 | buscar_nodos | {"consulta": "deudores no deben ser objeto clasificación", "limite": 10} | 3179 | 1215 (TRUNCADO EN TRAZA) |
| 2 | buscar_nodos | {"consulta": "capacidad de repago evaluación deudores", "limite": 10} | 3299 | 1215 (TRUNCADO EN TRAZA) |
| 3 | ver_nodo | {"id": "Restriccion_deudores_que_no_deben_ser_objeto_de_clasificacion"} | 402 | 402 (entero en traza) |
| 4 | ver_nodo | {"id": "Restriccion_no_correspondera_la_evaluacion_de_la_capacidad_de_repago_respecto_de_las_financi"} | 682 | 682 (entero en traza) |
| 5 | ver_vecinos | {"id": "Restriccion_deudores_que_no_deben_ser_objeto_de_clasificacion", "direccion": "salientes"} | 782 | 782 (entero en traza) |
| 6 | ver_vecinos | {"id": "Restriccion_no_correspondera_la_evaluacion_de_la_capacidad_de_repago_respecto_de_las_financi", "direccion": "salientes"} | 835 | 835 (entero en traza) |
| 7 | buscar_nodos | {"consulta": "deudores exclusión clasificación estado nacional provincia municipio", "limite": 10} | 3037 | 1215 (TRUNCADO EN TRAZA) |
| 8 | buscar_nodos | {"consulta": "garantías preferidas A financiaciones", "limite": 10} | 3837 | 1215 (TRUNCADO EN TRAZA) |
| 9 | buscar_nodos | {"consulta": "punto 4.5 deudores no deben clasificación estado nacional", "limite": 10} | 3116 | 1215 (TRUNCADO EN TRAZA) |
| 10 | buscar_nodos | {"consulta": "punto 4.4 garantías preferidas A estado nacional provincia", "limite": 10} | 3617 | 1215 (TRUNCADO EN TRAZA) |
| 11 | buscar_nodos | {"consulta": "estado nacional provincia municipio banco central deudores", "limite": 10} | 3134 | 1215 (TRUNCADO EN TRAZA) |
| 12 | buscar_nodos | {"consulta": "cesión sin responsabilidad cedente deudores", "limite": 10} | 3285 | 1215 (TRUNCADO EN TRAZA) |
| 13 | ver_nodo | {"id": "Restriccion_no_seran_objeto_de_clasificacion_quienes_resulten_deudores_en_operaciones_de_ces"} | 526 | 526 (entero en traza) |
| 14 | buscar_nodos | {"consulta": "garantías preferidas A definición estado nacional provincia", "limite": 10} | 3732 | 1215 (TRUNCADO EN TRAZA) |
| 15 | buscar_nodos | {"consulta": "garantías preferidas A créditos estado nacional provincia municipio", "limite": 10} | 3786 | 1215 (TRUNCADO EN TRAZA) |

Los **outputs COMPLETOS de las 15 llamadas** (re-ejecutados) están pegados íntegros en el
**Apéndice A** de este archivo, identificados por número de paso y tool.

### 1(a) — ¿El portador del 4.5 aparece en algún output completo?

Barrido del id `Restriccion_los_deudores_cuyas_financiaciones_se_encuentren_cubiertas_totalmente_con_garanti`
sobre los outputs completos de los 15 pasos (script `analisis_run3.py`, scratchpad):

```
### (a) nodo portador del 4.5
  [portador_4.5 (id)] AUSENTE en todos los outputs completos
```

**Resultado: AUSENTE en los 15 outputs completos.** El nodo portador del 4.5 no aparece en
ningún paso de la trayectoria (ni como resultado de búsqueda, ni como vecino, ni abierto).

### 1(b) — Inventario del vocabulario ex ante

Términos de búsqueda usados por el agente (10 `buscar_nodos`):

```
  paso  1: "deudores no deben ser objeto clasificación"
  paso  2: "capacidad de repago evaluación deudores"
  paso  7: "deudores exclusión clasificación estado nacional provincia municipio"
  paso  8: "garantías preferidas A financiaciones"
  paso  9: "punto 4.5 deudores no deben clasificación estado nacional"
  paso 10: "punto 4.4 garantías preferidas A estado nacional provincia"
  paso 11: "estado nacional provincia municipio banco central deudores"
  paso 12: "cesión sin responsabilidad cedente deudores"
  paso 14: "garantías preferidas A definición estado nacional provincia"
  paso 15: "garantías preferidas A créditos estado nacional provincia municipio"
```

`garant*` en la PREGUNTA: **AUSENTE** (la pregunta no contiene "garantías" ni variantes).

Presencia de `garant*` en el output COMPLETO de cada paso (unidades donde aparece):

```
  paso  1 (buscar_nodos): ausente
  paso  2 (buscar_nodos): PRESENTE (3 unidades)
       - resultados[4] id=Restriccion_no_correspondera_la_evaluacion_de_la_capacidad_de_repago_respecto_de_las_financi
       - resultados[6] id=Obligacion_las_entidades_financieras_deberan_establecer_politicas_para_el_otorgamiento_de_l
       - resultados[10] id=Obligacion_evaluar_capacidad_de_pago
  paso  3 (ver_nodo    ): ausente
  paso  4 (ver_nodo    ): PRESENTE (1 unidad)
       - nodo id=Restriccion_no_correspondera_la_evaluacion_de_la_capacidad_de_repago_respecto_de_las_financi
  paso  5 (ver_vecinos ): ausente
  paso  6 (ver_vecinos ): PRESENTE (2 unidades)
       - salientes[1] establecida_en -> TextoOrdenado_to_clasificacion_deudores_actual_pdf
       - salientes[2] prohibe -> Operacion_evaluacion_crediticia
  paso  7 (buscar_nodos): ausente
  paso  8 (buscar_nodos): PRESENTE (6 unidades)
  paso  9 (buscar_nodos): PRESENTE (1 unidad)
  paso 10 (buscar_nodos): PRESENTE (7 unidades)
  paso 11 (buscar_nodos): PRESENTE (1 unidad)
  paso 12 (buscar_nodos): ausente
  paso 13 (ver_nodo    ): ausente
  paso 14 (buscar_nodos): PRESENTE (7 unidades)
  paso 15 (buscar_nodos): PRESENTE (9 unidades)
```

(El detalle unidad por unidad de los pasos 8–15 está en el Apéndice A, donde los outputs van
íntegros.)

**Primer paso cuyo output completo expone `garant*`: paso 2.**

Para cada `buscar_nodos`: ¿`garant*` había sido expuesto en outputs COMPLETOS de pasos previos?

| paso | consulta | pasos previos con `garant*` expuesto |
|---|---|---|
| 1 | "deudores no deben ser objeto clasificación" | NINGUNO |
| 2 | "capacidad de repago evaluación deudores" | NINGUNO |
| 7 | "deudores exclusión clasificación estado nacional provincia municipio" | 2, 4, 6 |
| 8 | "garantías preferidas A financiaciones" | 2, 4, 6 |
| 9 | "punto 4.5 deudores no deben clasificación estado nacional" | 2, 4, 6, 8 |
| 10 | "punto 4.4 garantías preferidas A estado nacional provincia" | 2, 4, 6, 8, 9 |
| 11 | "estado nacional provincia municipio banco central deudores" | 2, 4, 6, 8, 9, 10 |
| 12 | "cesión sin responsabilidad cedente deudores" | 2, 4, 6, 8, 9, 10, 11 |
| 14 | "garantías preferidas A definición estado nacional provincia" | 2, 4, 6, 8, 9, 10, 11 |
| 15 | "garantías preferidas A créditos estado nacional provincia municipio" | 2, 4, 6, 8, 9, 10, 11, 14 |

Hechos, sin adjudicar: el agente usó "garantías preferidas A" por primera vez en el paso 8;
para entonces `garant*` ya había sido expuesto en los outputs completos de los pasos 2, 4 y 6.
Aun con esas 4 búsquedas que contienen "garantías preferidas A" (pasos 8, 10, 14, 15), el
portador del 4.5 no apareció en ningún resultado (ver 1(a)).

---

## 2. CQ-034

**Pregunta (verbatim de la traza):** Una persona humana residente compra moneda extranjera
para atesorar; ¿qué límite mensual aplica si la operación se cursa con débito en cuenta frente
a si se realiza en efectivo, y qué límite general rige para otras modalidades de formación de
activos externos?

**Inventario de la trayectoria (15 pasos):**

| paso | tool | input | runtime chars | almacenado en traza |
|---|---|---|---|---|
| 1 | buscar_nodos | {"consulta": "persona humana residente compra moneda extranjera atesorar límite mensual", "limite": 10} | 3549 | 1215 (TRUNCADO EN TRAZA) |
| 2 | buscar_nodos | {"consulta": "límite compra dólares débito cuenta efectivo", "limite": 10} | 3196 | 1215 (TRUNCADO EN TRAZA) |
| 3 | buscar_nodos | {"consulta": "formación activos externos límite general", "limite": 10} | 3369 | 1215 (TRUNCADO EN TRAZA) |
| 4 | ver_nodo | {"id": "Restriccion_limite_mensual_de_compra_en_efectivo"} | 619 | 619 (entero en traza) |
| 5 | ver_nodo | {"id": "Operacion_compra_de_moneda_extranjera"} | 498 | 498 (entero en traza) |
| 6 | ver_nodo | {"id": "Operacion_formacion_de_activos_externos"} | 344 | 344 (entero en traza) |
| 7 | ver_vecinos | {"id": "Operacion_compra_de_moneda_extranjera", "direccion": "salientes"} | 554 | 554 (entero en traza) |
| 8 | ver_vecinos | {"id": "Operacion_compra_de_moneda_extranjera", "direccion": "entrantes"} | 3182 | 1215 (TRUNCADO EN TRAZA) |
| 9 | buscar_nodos | {"consulta": "límite mensual débito cuenta USD 300", "limite": 10} | 3662 | 1215 (TRUNCADO EN TRAZA) |
| 10 | buscar_nodos | {"consulta": "límite mensual compra moneda extranjera USD 300 débito", "limite": 10} | 3490 | 1215 (TRUNCADO EN TRAZA) |
| 11 | buscar_nodos | {"consulta": "compra moneda extranjera personas humanas residentes atesorar límite", "limite": 10} | 3446 | 1215 (TRUNCADO EN TRAZA) |
| 12 | ver_nodo | {"id": "Obligacion_cursar_operacion_con_debito_en_cuenta"} | 443 | 443 (entero en traza) |
| 13 | buscar_nodos | {"consulta": "USD 300 mensual compra moneda extranjera", "limite": 10} | 3110 | 1215 (TRUNCADO EN TRAZA) |
| 14 | buscar_nodos | {"consulta": "300 dólares límite mensual", "limite": 10} | 3085 | 1215 (TRUNCADO EN TRAZA) |
| 15 | buscar_nodos | {"consulta": "Punto 3.8 compra moneda extranjera personas humanas residentes formación activos externos", "limite": 15} | 4475 | 1215 (TRUNCADO EN TRAZA) |

(Outputs completos por paso: `ver_nodo`/`ver_vecinos` íntegros y `buscar_nodos` como
posición+id en el Apéndice C.)

### Barrido término por término sobre los outputs COMPLETOS

**"USD 100" — PRESENTE, 12 posiciones** (con una precisión, ver nota):

```
paso 1  resultados[3] id=Excepcion_compra_de_billetes_en_moneda_extranjera_de_personas_humanas_no_residentes_en_con
paso 1  resultados[6] id=Restriccion_limite_mensual_de_compra_en_efectivo
paso 2  resultados[1] id=Restriccion_limite_mensual_de_compra_en_efectivo
paso 3  resultados[2] id=Restriccion_no_poseia_activos_externos_liquidos_disponibles_...   <- ver NOTA: es "USD 100.000"
paso 4  ver_nodo      id=Restriccion_limite_mensual_de_compra_en_efectivo (nodo abierto completo)
paso 9  resultados[3] id=Restriccion_limite_mensual_de_compra_en_efectivo
paso 10 resultados[3] id=Excepcion_compra_de_billetes_... ; resultados[6] id=Restriccion_limite_mensual_de_compra_en_efectivo
paso 11 resultados[1] id=Excepcion_compra_de_billetes_...
paso 13 resultados[3] id=Excepcion_compra_de_billetes_...
paso 14 resultados[2] id=Restriccion_limite_mensual_de_compra_en_efectivo
paso 15 resultados[1] id=Excepcion_compra_de_billetes_...
```

**NOTA de precisión:** el hit del paso 3 resultados[2] es un artefacto del regex de frontera:
esa unidad dice "USD 100.000 (dólares estadounidenses cien mil)" (activos externos líquidos),
NO "USD 100". El barrido de "100" como número suelto (excluyendo `100.000`) da **11
posiciones** — las mismas de arriba sin el paso 3.

Textos expuestos (verbatim de la primera aparición y del nodo abierto):

```
paso 1 resultados[6]:
{"id": "Restriccion_limite_mensual_de_compra_en_efectivo", "type": "Restriccion", "label": "Límite mensual de compra en efectivo", "tokens_matcheados": 3, "resumen_propiedades": "Si el cliente utiliza efectivo el monto comprado por el cliente no supere el equivalente a USD 100 (dólares estadounidenses cien) en el mes calendario en el con…"}

paso 4 ver_nodo (nodo COMPLETO abierto por el agente):
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

**"USD 200" / "200" (número suelto) — PRESENTE, 2 posiciones:**

```
paso 2 resultados[2] y paso 9 resultados[2]:
{"id": "Restriccion_el_limite_se_incrementa_a_usd_200_por_operacion_por_los_retiros_de_efectivo_que_", "type": "Restriccion", "label": "Límite adelanto países no limítrofes", "tokens_matcheados": 2, "resumen_propiedades": "El límite se incrementa a USD 200 por operación por los retiros de efectivo que se realicen en países no limítrofes"}
```

Contenido y provenance de ese nodo en el kg de run_3 (lookup directo, para dejar constancia
del alcance del único "USD 200" expuesto):

```
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

Hecho: el literal "USD 200" expuesto en la trayectoria pertenece a un nodo sobre retiros de
efectivo en países no limítrofes (provenance Punto 4.1); **ningún output completo contiene un
límite USD 200 asociado a "otras modalidades" / formación de activos externos / Punto 3.9**.

**Resto de los términos:**

| Término | Resultado |
|---|---|
| "A07" | **AUSENTE** en los 15 outputs completos |
| "A09" | **AUSENTE** en los 15 outputs completos |
| "atesoramiento"/"atesorar" | **AUSENTE** en los 15 outputs completos (aparece solo en las CONSULTAS de los pasos 1 y 11, nunca en un output) |
| "formación de activos externos" | **PRESENTE, 9 posiciones**: paso 1 resultados[1], paso 3 resultados[1], paso 5 ver_nodo (`Operacion_compra_de_moneda_extranjera`), paso 6 ver_nodo (`Operacion_formacion_de_activos_externos`), paso 10 resultados[1], paso 11 resultados[2], paso 13 resultados[1], paso 15 resultados[2] y [5] |

---

## 3. CQ-017

**Pregunta (verbatim de la traza):** Un operador de cambio, ¿está alcanzado por las normas de
Protección de los Usuarios de Servicios Financieros y debe intervenir como entidad autorizada
en el mercado de cambios?

**Inventario de la trayectoria (15 pasos):**

| paso | tool | input | runtime chars | almacenado en traza |
|---|---|---|---|---|
| 1 | buscar_nodos | {"consulta": "operador de cambio", "limite": 10} | 2577 | 1215 (TRUNCADO EN TRAZA) |
| 2 | buscar_nodos | {"consulta": "Protección Usuarios Servicios Financieros", "limite": 10} | 3814 | 1215 (TRUNCADO EN TRAZA) |
| 3 | buscar_nodos | {"consulta": "mercado de cambios entidad autorizada", "limite": 10} | 3229 | 1215 (TRUNCADO EN TRAZA) |
| 4 | ver_nodo | {"id": "EntidadFinanciera_operador_de_cambio"} | 285 | 285 (entero en traza) |
| 5 | ver_nodo | {"id": "TextoOrdenado_to_proteccion_usuarios_servicios_financieros_actual_pdf"} | 434 | 434 (entero en traza) |
| 6 | ver_vecinos | {"id": "EntidadFinanciera_operador_de_cambio", "direccion": "ambas"} | 771 | 771 (entero en traza) |
| 7 | ver_nodo | {"id": "Obligacion_cuando_un_tercero_desarrolle_tareas_relativas_a_servicios_ofrecidos_por_los_suje"} | 617 | 617 (entero en traza) |
| 8 | buscar_nodos | {"consulta": "operador cambio sujeto obligado protección usuarios", "limite": 10} | 3303 | 1215 (TRUNCADO EN TRAZA) |
| 9 | ver_nodo | {"id": "EntidadFinanciera_sujeto_obligado"} | 895 | 895 (entero en traza) |
| 10 | ver_vecinos | {"id": "EntidadFinanciera_sujeto_obligado", "direccion": "salientes"} | 11828 | 1216 (TRUNCADO EN TRAZA) |
| 11 | buscar_nodos | {"consulta": "punto 1.1 partes sujetos obligados operador cambio", "limite": 10} | 2919 | 1215 (TRUNCADO EN TRAZA) |
| 12 | ver_nodo | {"id": "Obligacion_los_sujetos_obligados_enumerados_en_el_punto_1_1_2_en_la_medida_en_que_correspon"} | 682 | 682 (entero en traza) |
| 13 | buscar_nodos | {"consulta": "punto 1.1.2 sujetos obligados enumeración", "limite": 10} | 3002 | 1215 (TRUNCADO EN TRAZA) |
| 14 | buscar_nodos | {"consulta": "1.1.2 bancos entidades financieras", "limite": 10} | 2950 | 1215 (TRUNCADO EN TRAZA) |
| 15 | buscar_nodos | {"consulta": "protección usuarios bancos cajas ahorro cooperativas cambio", "limite": 10} | 2593 | 1215 (TRUNCADO EN TRAZA) |

Nótese el paso 10: **11.828 chars en runtime, 1.216 almacenados** — el paso más truncado de
los 4 casos. (Outputs completos por paso en el Apéndice B.)

### Barrido de conexión Protección 1.1.2.2 ↔ Exterior 1.1 y portadores

```
  ['1.1.2.2' (punto específico de Protección)] AUSENTE en todos los outputs completos
  [id tipo 'intervencion_de_entidades_autorizadas*'] AUSENTE en todos los outputs completos
  [id tipo 'entidades_autorizadas_a_operar*'] AUSENTE en todos los outputs completos
  [id tipo 'entidades_financieras_o_cambiarias*'] AUSENTE en todos los outputs completos
  [texto 'autorizada(s) a operar en (el mercado de) cambios'] AUSENTE en todos los outputs completos
  [texto 'entidad autorizada'] AUSENTE en todos los outputs completos
  [texto 'mercado de cambios'] PRESENTE en 12 posiciones:
    - paso 3 resultados[1]..[10] (los 10 resultados de la búsqueda "mercado de cambios entidad autorizada":
      obligaciones de ingreso/liquidación y operaciones de acceso al mercado de cambios; ninguno
      contiene "entidad autorizada" en su contenido)
    - paso 10 salientes[28] ejecuta -> Operacion_acceso_al_mercado_de_cambios
    - paso 10 salientes[33] ejecuta -> Operacion_acceso_a_mercado_de_cambios
```

**Hechos:** (i) el punto "1.1.2.2" no aparece en ningún output completo; (ii) ningún nodo tipo
portador de la regla de Exterior 1.1 (`intervencion_de_entidades_autorizadas*`,
`entidades_autorizadas_a_operar*`, `entidades_financieras_o_cambiarias*`) aparece en ningún
output completo, ni como texto ("entidad autorizada" no aparece en ningún output); (iii) el
texto "mercado de cambios" sí aparece (12 posiciones, arriba).

### Edges expuestos en los dos `ver_vecinos` (contenido cross-documento visible en runtime)

Paso 6 — `ver_vecinos(EntidadFinanciera_operador_de_cambio, ambas)`: **2 edges, ambos con
provenance de TO_proteccion**:

```
salientes[1]: ejecuta -> Operacion_operacion_de_cambio  [docs: TO_proteccion_usuarios_servicios_financieros_actual.pdf]
entrantes[1]: aplica_a -> Obligacion_cuando_un_tercero_desarrolle_tareas_relativas_a_servicios_ofrecidos_por_los_suje  [docs: TO_proteccion_usuarios_servicios_financieros_actual.pdf]
```

Paso 10 — `ver_vecinos(EntidadFinanciera_sujeto_obligado, salientes)`: **40 edges** (expuestos
completos en runtime; en traza quedó 1.216 de 11.828 chars). Distribución por documento de
provenance: 25 edges TO_capitales_minimos, 2 TO_clasificacion_deudores, 13 TO_exterior_cambios.
Entre los de exterior:

```
salientes[28]: ejecuta -> Operacion_acceso_al_mercado_de_cambios  [TO_exterior_cambios_actual.pdf]
salientes[29]: ejecuta -> Operacion_cambio                        [TO_exterior_cambios_actual.pdf]
salientes[30]: ejecuta -> Operacion_canje                         [TO_exterior_cambios_actual.pdf]
salientes[31]: ejecuta -> Operacion_arbitraje                     [TO_exterior_cambios_actual.pdf]
salientes[33]: ejecuta -> Operacion_acceso_a_mercado_de_cambios   [TO_exterior_cambios_actual.pdf]
(el listado completo de los 40, con docs, va en el Apéndice B)
```

**Hecho (sin adjudicar):** en el output completo del paso 10 el agente tuvo expuestos edges del
nodo `EntidadFinanciera_sujeto_obligado` hacia operaciones del TO de Exterior y Cambios
(incluido "acceso al mercado de cambios"); ninguno de esos edges menciona el punto 1.1.2.2, el
Punto 1.1 de Exterior como texto, ni "entidad autorizada". Los vecinos del nodo
`EntidadFinanciera_operador_de_cambio` (paso 6) son exclusivamente de Protección.

---

## 4. CQ-020

**Pregunta (verbatim de la traza):** ¿Cómo se calcula la exigencia de capital por riesgo de
crédito (CRC) y con qué frecuencia se reporta al BCRA?

**Inventario de la trayectoria (11 pasos):**

| paso | tool | input | runtime chars | almacenado en traza |
|---|---|---|---|---|
| 1 | buscar_nodos | {"consulta": "exigencia capital riesgo crédito CRC", "limite": 10} | 3395 | 1215 (TRUNCADO EN TRAZA) |
| 2 | buscar_nodos | {"consulta": "capital riesgo crédito cálculo", "limite": 10} | 3203 | 1215 (TRUNCADO EN TRAZA) |
| 3 | buscar_nodos | {"consulta": "reporte BCRA capital frecuencia", "limite": 10} | 2789 | 1215 (TRUNCADO EN TRAZA) |
| 4 | ver_nodo | {"id": "Operacion_calculo_de_capital_minimo"} | 457 | 457 (entero en traza) |
| 5 | ver_nodo | {"id": "Operacion_calculo_de_exigencia_de_capital_minimo_por_riesgo_de_credito"} | 367 | 367 (entero en traza) |
| 6 | ver_nodo | {"id": "Operacion_calculo_de_exigencia_por_riesgo"} | 564 | 564 (entero en traza) |
| 7 | buscar_nodos | {"consulta": "reporte mensual capital riesgo crédito", "limite": 10} | 3421 | 1215 (TRUNCADO EN TRAZA) |
| 8 | ver_vecinos | {"id": "Operacion_calculo_de_capital_minimo", "direccion": "ambas"} | 5312 | 1215 (TRUNCADO EN TRAZA) |
| 9 | ver_nodo | {"id": "Obligacion_informar_exigencia_de_capitales_por_riesgo"} | 521 | 521 (entero en traza) |
| 10 | buscar_nodos | {"consulta": "APR_c factor ponderación riesgo", "limite": 5} | 1795 | 1214 (TRUNCADO EN TRAZA) |
| 11 | buscar_nodos | {"consulta": "INC incremento exigencia capital", "limite": 5} | 1724 | 1214 (TRUNCADO EN TRAZA) |

### 4(a) — ¿Aparece en algún output un nodo de frecuencia de reporte PARA riesgo de crédito?

Barrido de términos de frecuencia (`frecuencia|mensual|trimestral|periodicidad`) sobre TODAS
las unidades de los outputs completos — cada match, con qué tema menciona:

```
paso  1 resultados[6]  Obligacion_se_determinara_mensualmente_la_exigencia_de_capital_por_riesgo_operacional_cro_m   -> riesgo OPERACIONAL
paso  4 ver_nodo       Operacion_calculo_de_capital_minimo            -> match SOLO por el nombre del PDF de provenance (ver nota)
paso  6 ver_nodo       Operacion_calculo_de_exigencia_por_riesgo      -> match SOLO por el nombre del PDF de provenance (ver nota)
paso  7 resultados[4]  Restriccion_la_exigencia_mensual_de_capital_minimo_por_riesgo_operacional_...                 -> riesgo OPERACIONAL
paso  7 resultados[8]  Obligacion_se_determinara_mensualmente_la_exigencia_de_capital_por_riesgo_operacional_cro_m   -> riesgo OPERACIONAL
paso  8 (14 unidades de ver_vecinos con matches: "contable_mensual" en filename de provenance,
         CRO mensual —riesgo operacional—, desestimaciones, etc.; ninguna une frecuencia con riesgo de crédito)
paso  9 ver_nodo       Obligacion_informar_exigencia_de_capitales_por_riesgo  -> riesgo de MERCADO, mensual (ver 4(c))
paso 11 resultados[2]  Obligacion_se_determinara_mensualmente_la_exigencia_de_capital_por_riesgo_operacional_cro_m   -> riesgo OPERACIONAL
```

**Nota (verificado):** los matches de los pasos 4 y 6 provienen ÚNICAMENTE del nombre del
archivo en la provenance (`TO_regimen_informativo_contable_mensual_actual.pdf`); quitando el
campo `provenances`, ninguno de los dos nodos contiene término de frecuencia en
id/label/properties:

```
paso 4: freq en propiedades/label/id SIN provenances: False | en provenances: True
paso 6: freq en propiedades/label/id SIN provenances: False | en provenances: True
```

**Resultado: ningún output completo de los 11 pasos expone un nodo que asocie una frecuencia
de reporte al riesgo de crédito.** Los nodos con frecuencia expuestos son de riesgo
operacional (pasos 1, 7, 8, 11) y de riesgo de mercado (paso 9).

### 4(b) — Barrido programático sobre el kg.json de run_3

Comando (vía `loader.load_graph("run_3")`, que carga el `kg.json` congelado de
`run_3_ppf_core`):

```python
kg = loader.load_graph("run_3")   # 4050 nodos
freq = r"frecuencia|mensual|trimestral|periodicidad"
cred = r"riesgo de credito|\bcrc\b"
# match sobre json normalizado (lowercase, sin acentos) de {id, label, properties} de cada nodo
```

Output completo:

```
run_3: 4050 nodos
Nodos con (frecuencia|mensual|trimestral|periodicidad) Y (riesgo de credito|CRC) en id/label/properties: 2

- id: Obligacion_se_informaran_los_incrementos_a_la_exigencia_segun_riesgo_de_credito_generados_p
  label: Informar incrementos exigencia riesgo crédito
  properties: {"descripcion": "Se informarán los incrementos a la exigencia según riesgo de crédito generados por excesos verificados en la relación de activos inmovilizados, límites establecidos en normas sobre Grandes Exposiciones al Riesgo de Crédito, Graduación del crédito, Financiamiento al Sector Público no Financiero y Posiciones de Derivados no Cubiertos", "tipo": "presentacion_informativa", "plazo": "mensual"}

- id: Obligacion_informacion_de_incumplimientos_de_grandes_exposiciones_al_riesgo_de_credito_del_
  label: Informar incumplimientos de Grandes Exposiciones
  properties: {"descripcion": "Información de incumplimientos de Grandes Exposiciones al Riesgo de Crédito del mes bajo informe", "tipo": "presentacion_informativa", "frecuencia": "mensual"}
```

Verificación adicional: **ninguno de esos 2 nodos aparece en ningún output completo de la
trayectoria de CQ-020**:

```
Obligacion_se_informaran_los_incrementos_a_la_exigencia_segun_riesgo_de_credito_... -> AUSENTE en los 11 outputs
Obligacion_informacion_de_incumplimientos_de_grandes_exposiciones_...              -> AUSENTE en los 11 outputs
```

Hecho, sin adjudicar: en los 4.050 nodos de run_3, los únicos 2 que combinan término de
frecuencia con riesgo de crédito son obligaciones informativas mensuales sobre **incrementos a
la exigencia por excesos** y sobre **incumplimientos de Grandes Exposiciones** (contenido
pegado arriba). Ningún nodo del kg enuncia la frecuencia de reporte de la exigencia CRC en sí;
la determinación de si alguno de estos 2 cuenta como "nodo de frecuencia de reporte para
riesgo de crédito" queda para la adjudicación.

### 4(c) — ¿En qué paso y posición apareció el nodo de frecuencia de riesgo de MERCADO?

El nodo es `Obligacion_informar_exigencia_de_capitales_por_riesgo`. Ocurrencias en outputs
completos:

```
1ª exposición — paso 8, ver_vecinos(Operacion_calculo_de_capital_minimo), entrantes[4]:
{"relation": "condiciona", "vecino_id": "Obligacion_informar_exigencia_de_capitales_por_riesgo", "vecino_label": "Informar exigencia de capitales por riesgo", "provenances": [{"source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf", "location": "Punto 4.2. Modelos de información"}]}

2ª exposición (nodo abierto COMPLETO) — paso 9, ver_nodo:
{"id": "Obligacion_informar_exigencia_de_capitales_por_riesgo", "type": "Obligacion", "label": "Informar exigencia de capitales por riesgo", "properties": {"tipo": "presentacion_informativa", "description": "Presentar información sobre exigencia de capitales mínimos por riesgo de mercado con periodicidad mensual, desglosada por código de concepto y día del mes", "plazo": "mensual"}, "provenances": [{"source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf", "location": "Punto 4.2. Modelos de información"}]}
```

Hecho: en la 1ª exposición (paso 8 entrantes[4]) solo se ven id, label genérico ("Informar
exigencia de capitales por riesgo" — sin la palabra "mercado"), relación y provenance; el
contenido que dice "riesgo de mercado con periodicidad mensual" se expone recién al abrir el
nodo en el paso 9.

---

## Apéndice A — CQ-031: outputs COMPLETOS de las 15 llamadas (re-ejecución determinística)

```

--- paso 1 · buscar_nodos · input={"consulta": "deudores no deben ser objeto clasificación", "limite": 10} ---
{
 "consulta": "deudores no deben ser objeto clasificación",
 "total_con_match": 509,
 "resultados": [
  {
   "id": "Restriccion_deudores_que_no_deben_ser_objeto_de_clasificacion",
   "type": "Restriccion",
   "label": "Exclusión de deudores de clasificación",
   "tokens_matcheados": 6,
   "resumen_propiedades": "Deudores que no deben ser objeto de clasificación"
  },
  {
   "id": "Restriccion_no_seran_objeto_de_clasificacion_quienes_resulten_deudores_en_operaciones_de_ces",
   "type": "Restriccion",
   "label": "Exclusión de deudores en cesión",
   "tokens_matcheados": 4,
   "resumen_propiedades": "No serán objeto de clasificación quienes resulten deudores en operaciones de cesión sin responsabilidad para el cedente"
  },
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
   "id": "Restriccion_los_fondos_excedentes_del_125_deben_ser_ingresados_y_liquidados_en_el_mercado_de",
   "type": "Restriccion",
   "label": "Ingreso de fondos excedentes",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Los fondos excedentes del 125% deben ser ingresados y liquidados en el mercado de cambios dentro de los plazos previstos en las normas generales"
  },
  {
   "id": "Restriccion_aportes_deben_ser_en_efectivo",
   "type": "Restriccion",
   "label": "Aportes deben ser en efectivo",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Los aportes deben ser efectuados en efectivo, sin perjuicio de lo previsto en los puntos 5.1. a 5.3. sobre negociación de acciones o aportes irrevocables para f…"
  },
  {
   "id": "Excepcion_la_clasificacion_se_verifica_a_partir_del_momento_en_que_no_habiendo_sido_rechaz",
   "type": "Excepcion",
   "label": "Excepción por rechazo de reclamo",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La clasificación se verifica a partir del momento en que, no habiendo sido rechazado el reclamo, se verifique la falta de pago del siniestro luego de vencidos l…"
  },
  {
   "id": "Restriccion_los_contratos_deben_ser_de_clara_redaccion_y_con_tamano_de_tipografia_minimo_de_",
   "type": "Restriccion",
   "label": "Tamaño mínimo tipografía contrato",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Los contratos deben ser de clara redacción y con tamaño de tipografía mínimo de 1,8 milímetros de altura."
  },
  {
   "id": "Operacion_clasificacion_de_deudores",
   "type": "Operacion",
   "label": "Tarea de clasificación de deudores",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: clasificación de deudores"
  },
  {
   "id": "Obligacion_deben_ser_asentados_en_el_rccr_aquellos_reclamos_que_representan_una_queja_por_p",
   "type": "Obligacion",
   "label": "Asentar reclamos por incumplimiento",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Deben ser asentados en el RCCR aquellos reclamos que representan una queja por presunto incumplimiento, prestación defectuosa o falta de prestación de un produc…"
  }
 ]
}

--- paso 2 · buscar_nodos · input={"consulta": "capacidad de repago evaluación deudores", "limite": 10} ---
{
 "consulta": "capacidad de repago evaluación deudores",
 "total_con_match": 2417,
 "resultados": [
  {
   "id": "Operacion_evaluacion_crediticia",
   "type": "Operacion",
   "label": "Evaluación de capacidad de repago",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Evaluación de la capacidad de repago respecto de las financiaciones"
  },
  {
   "id": "Operacion_evaluacion_de_capacidad",
   "type": "Operacion",
   "label": "Evaluación de capacidad de repago",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Al evaluar la capacidad de repago, el énfasis deberá ponerse en el análisis de los flujos de fondos realizado por la entidad."
  },
  {
   "id": "Obligacion_no_se_considerara_refinanciacion_la_asistencia_que_se_otorgue_a_los_deudores_cla",
   "type": "Obligacion",
   "label": "Evaluación de capacidad de pago para ampliación",
   "tokens_matcheados": 4,
   "resumen_propiedades": "No se considerará refinanciación la asistencia que se otorgue a los deudores clasificados en esta categoría siempre que implique mayor deuda por capital respect…"
  },
  {
   "id": "Restriccion_no_correspondera_la_evaluacion_de_la_capacidad_de_repago_respecto_de_las_financi",
   "type": "Restriccion",
   "label": "Excención de evaluación por garantías preferidas A",
   "tokens_matcheados": 4,
   "resumen_propiedades": "No corresponderá la evaluación de la capacidad de repago respecto de las financiaciones que se encuentren respaldadas con tales garantías"
  },
  {
   "id": "Obligacion_realizar_respecto_de_los_firmantes_libradores_deudores_codeudores_o_aceptantes_s",
   "type": "Obligacion",
   "label": "Evaluación como sujeto de crédito",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Realizar respecto de los firmantes, libradores, deudores, codeudores o aceptantes su evaluación como sujetos de crédito con la pertinente apertura del legajo"
  },
  {
   "id": "Obligacion_las_entidades_financieras_deberan_establecer_politicas_para_el_otorgamiento_de_l",
   "type": "Obligacion",
   "label": "Políticas evaluación capacidad pago",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Las entidades financieras deberán establecer políticas para el otorgamiento de los préstamos con garantía hipotecaria que permitan una adecuada evaluación de la…"
  },
  {
   "id": "Obligacion_evaluar_capacidad_de_repago_del_deudor",
   "type": "Obligacion",
   "label": "Evaluar capacidad de repago del deudor",
   "tokens_matcheados": 3,
   "resumen_propiedades": "El criterio básico de evaluación es la capacidad de repago del deudor en función del flujo financiero estimado"
  },
  {
   "id": "Operacion_evaluacion_de_deudor_como_sujeto_de_credito",
   "type": "Operacion",
   "label": "Evaluación de deudor",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: evaluación de deudor como sujeto de crédito"
  },
  {
   "id": "Restriccion_incurra_en_atrasos_de_hasta_180_dias_con_exclusion_de_los_deudores_comprendidos_",
   "type": "Restriccion",
   "label": "Atrasos hasta 180 días",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Incurra en atrasos de hasta 180 días, con exclusión de los deudores comprendidos en el punto 6.5.2.2."
  },
  {
   "id": "Obligacion_evaluar_capacidad_de_pago",
   "type": "Obligacion",
   "label": "Evaluar capacidad de pago",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El criterio básico a ser utilizado para efectuar la clasificación es la capacidad de pago en el futuro de la deuda o de los compromisos objeto de la garantía de…"
  }
 ]
}

--- paso 3 · ver_nodo · input={"id": "Restriccion_deudores_que_no_deben_ser_objeto_de_clasificacion"} ---
{
 "id": "Restriccion_deudores_que_no_deben_ser_objeto_de_clasificacion",
 "type": "Restriccion",
 "label": "Exclusión de deudores de clasificación",
 "properties": {
  "descripcion": "Deudores que no deben ser objeto de clasificación",
  "tipo": "prohibicion"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Punto 4.5. Deudores que no deben ser objeto de clasificación."
  }
 ]
}

--- paso 4 · ver_nodo · input={"id": "Restriccion_no_correspondera_la_evaluacion_de_la_capacidad_de_repago_respecto_de_las_financi"} ---
{
 "id": "Restriccion_no_correspondera_la_evaluacion_de_la_capacidad_de_repago_respecto_de_las_financi",
 "type": "Restriccion",
 "label": "Excención de evaluación por garantías preferidas A",
 "properties": {
  "tipo": "prohibicion",
  "descripcion": "No corresponderá la evaluación de la capacidad de repago respecto de las financiaciones respaldadas con garantías preferidas A",
  "description": "No corresponderá la evaluación de la capacidad de repago respecto de las financiaciones que se encuentren respaldadas con tales garantías"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Punto 4.4. Financiaciones cubiertas con garantías preferidas “A”."
  }
 ]
}

--- paso 5 · ver_vecinos · input={"id": "Restriccion_deudores_que_no_deben_ser_objeto_de_clasificacion", "direccion": "salientes"} ---
{
 "id": "Restriccion_deudores_que_no_deben_ser_objeto_de_clasificacion",
 "label": "Exclusión de deudores de clasificación",
 "n_salientes_total": 2,
 "n_entrantes_total": 1,
 "salientes": [
  {
   "relation": "establecida_en",
   "vecino_id": "TextoOrdenado_to_clasificacion_deudores_actual_pdf",
   "vecino_label": "Clasificación de Deudores",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "Punto 4.5. Deudores que no deben ser objeto de clasificación."
    }
   ]
  },
  {
   "relation": "prohibe",
   "vecino_id": "Operacion_clasificacion_de_deudor",
   "vecino_label": "Evaluación grado de inversión",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "Punto 4.5. Deudores que no deben ser objeto de clasificación."
    }
   ]
  }
 ],
 "salientes_truncado": false
}

--- paso 6 · ver_vecinos · input={"id": "Restriccion_no_correspondera_la_evaluacion_de_la_capacidad_de_repago_respecto_de_las_financi", "direccion": "salientes"} ---
{
 "id": "Restriccion_no_correspondera_la_evaluacion_de_la_capacidad_de_repago_respecto_de_las_financi",
 "label": "Excención de evaluación por garantías preferidas A",
 "n_salientes_total": 2,
 "n_entrantes_total": 0,
 "salientes": [
  {
   "relation": "establecida_en",
   "vecino_id": "TextoOrdenado_to_clasificacion_deudores_actual_pdf",
   "vecino_label": "Clasificación de Deudores",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "Punto 4.4. Financiaciones cubiertas con garantías preferidas “A”."
    }
   ]
  },
  {
   "relation": "prohibe",
   "vecino_id": "Operacion_evaluacion_crediticia",
   "vecino_label": "Evaluación de capacidad de repago",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "Punto 4.4. Financiaciones cubiertas con garantías preferidas “A”."
    }
   ]
  }
 ],
 "salientes_truncado": false
}

--- paso 7 · buscar_nodos · input={"consulta": "deudores exclusión clasificación estado nacional provincia municipio", "limite": 10} ---
{
 "consulta": "deudores exclusión clasificación estado nacional provincia municipio",
 "total_con_match": 156,
 "resultados": [
  {
   "id": "Restriccion_no_seran_objeto_de_clasificacion_quienes_resulten_deudores_en_operaciones_de_ces",
   "type": "Restriccion",
   "label": "Exclusión de deudores en cesión",
   "tokens_matcheados": 3,
   "resumen_propiedades": "No serán objeto de clasificación quienes resulten deudores en operaciones de cesión sin responsabilidad para el cedente"
  },
  {
   "id": "Restriccion_deudores_que_no_deben_ser_objeto_de_clasificacion",
   "type": "Restriccion",
   "label": "Exclusión de deudores de clasificación",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Deudores que no deben ser objeto de clasificación"
  },
  {
   "id": "Restriccion_incurra_en_atrasos_de_hasta_180_dias_con_exclusion_de_los_deudores_comprendidos_",
   "type": "Restriccion",
   "label": "Atrasos hasta 180 días",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Incurra en atrasos de hasta 180 días, con exclusión de los deudores comprendidos en el punto 6.5.2.2."
  },
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
   "id": "Operacion_estado_de_situacion_de_deudores",
   "type": "Operacion",
   "label": "Estado de situación de deudores",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Estado de situación de deudores referenciado en punto 6.1. y 6.2."
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
   "id": "Excepcion_los_deudores_por_pases_activos_ventas_a_termino_y_ventas_al_contado_a_liquidar_e",
   "type": "Excepcion",
   "label": "Exclusión de conceptos por intermediación",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Los deudores por pases activos, ventas a término y ventas al contado a liquidar están excluidos de la clasificación"
  }
 ]
}

--- paso 8 · buscar_nodos · input={"consulta": "garantías preferidas A financiaciones", "limite": 10} ---
{
 "consulta": "garantías preferidas A financiaciones",
 "total_con_match": 1220,
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
   "id": "Obligacion_en_el_caso_de_financiaciones_otorgadas_por_entidades_financieras_locales_el_segu",
   "type": "Obligacion",
   "label": "A cargo seguimiento financiaciones",
   "tokens_matcheados": 2,
   "resumen_propiedades": "En el caso de financiaciones otorgadas por entidades financieras locales, el seguimiento estará a cargo de la entidad que otorgó la financiación hasta su cancel…"
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
   "id": "Operacion_financiacion_a_clientes_del_sector_agricola_con_ratio_de_acopio_elevado",
   "type": "Operacion",
   "label": "Financiaciones a clientes agrícolas",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Financiaciones a clientes con actividad agrícola que no sean MIPyMES y tengan un ratio de acopio superior al 5% de su cosecha anual"
  },
  {
   "id": "Restriccion_para_financiaciones_otorgadas_a_partir_del_13_12_23_la_operacion_debe_correspond",
   "type": "Restriccion",
   "label": "Fecha de financiación compatibilidad",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Para financiaciones otorgadas a partir del 13/12/23, la operación debe corresponder a una importación de servicios prestada o devengada a partir del 13/12/23."
  },
  {
   "id": "Restriccion_clientes_cuyas_financiaciones_sumen_entre_el_1_o_el_equivalente_a_dos_veces_el_i",
   "type": "Restriccion",
   "label": "Rango RPC clientes revisión semestral",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Clientes cuyas financiaciones sumen entre el 1% –o el equivalente a dos veces el importe de referencia establecido en el punto 3.7., de ambos el menor– y menos …"
  }
 ]
}

--- paso 9 · buscar_nodos · input={"consulta": "punto 4.5 deudores no deben clasificación estado nacional", "limite": 10} ---
{
 "consulta": "punto 4.5 deudores no deben clasificación estado nacional",
 "total_con_match": 523,
 "resultados": [
  {
   "id": "Restriccion_deudores_que_no_deben_ser_objeto_de_clasificacion",
   "type": "Restriccion",
   "label": "Exclusión de deudores de clasificación",
   "tokens_matcheados": 4,
   "resumen_propiedades": "Deudores que no deben ser objeto de clasificación"
  },
  {
   "id": "Restriccion_no_seran_objeto_de_clasificacion_quienes_resulten_deudores_en_operaciones_de_ces",
   "type": "Restriccion",
   "label": "Exclusión de deudores en cesión",
   "tokens_matcheados": 3,
   "resumen_propiedades": "No serán objeto de clasificación quienes resulten deudores en operaciones de cesión sin responsabilidad para el cedente"
  },
  {
   "id": "Restriccion_los_garantes_admisibles_se_limitan_a_los_estipulados_en_el_punto_5_4_1_los_spe_n",
   "type": "Restriccion",
   "label": "Restricción en garantes admisibles",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Los garantes admisibles se limitan a los estipulados en el punto 5.4.1. Los SPE no son garantes admisibles."
  },
  {
   "id": "Obligacion_ajustar_el_valor_de_la_cobertura_segun_lo_previsto_en_punto_5_4_5",
   "type": "Obligacion",
   "label": "Ajuste valor cobertura método integral",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Para la aplicación del método integral el valor de la cobertura deberá ajustarse conforme a lo establecido en el punto 5.4.5"
  },
  {
   "id": "Excepcion_el_pago_se_concreta_en_el_marco_de_lo_dispuesto_en_el_punto_4_8_5_por_un_cliente",
   "type": "Excepcion",
   "label": "Pago BOPREAL Serie 1 mínimo 25% deudas elegibles",
   "tokens_matcheados": 3,
   "resumen_propiedades": "El pago se concreta en el marco de lo dispuesto en el punto 4.8.5. por un cliente que suscribió BOPREAL Serie 1 por un monto igual o mayor al 25% (veinticinco p…"
  },
  {
   "id": "Restriccion_el_importe_de_co_debera_ser_resultante_de_multiplicar_4_5_por_los_apr",
   "type": "Restriccion",
   "label": "Límite mínimo CO",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El importe de CO deberá ser resultante de multiplicar 4,5% por los APR"
  },
  {
   "id": "Excepcion_con_excepcion_de_los_casos_contemplados_en_el_punto_4_1",
   "type": "Excepcion",
   "label": "Excepción casos punto 4.1",
   "tokens_matcheados": 2,
   "resumen_propiedades": "con excepción de los casos contemplados en el punto 4.1"
  },
  {
   "id": "Excepcion_cuando_la_operacion_se_encuentra_comprendida_en_alguna_de_las_situaciones_detall",
   "type": "Excepcion",
   "label": "Situaciones del punto 8.5",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Cuando la operación se encuentra comprendida en alguna de las situaciones detalladas en el punto 8.5 y se verifiquen las condiciones previstas en cada caso"
  },
  {
   "id": "Excepcion_no_aplicable_punto_3_12_1",
   "type": "Excepcion",
   "label": "No aplicable punto 3.12.1",
   "tokens_matcheados": 2,
   "resumen_propiedades": "En la medida que no encuadre en el punto 3.12.1"
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

--- paso 10 · buscar_nodos · input={"consulta": "punto 4.4 garantías preferidas A estado nacional provincia", "limite": 10} ---
{
 "consulta": "punto 4.4 garantías preferidas A estado nacional provincia",
 "total_con_match": 1220,
 "resultados": [
  {
   "id": "Restriccion_los_garantes_admisibles_se_limitan_a_los_estipulados_en_el_punto_5_4_1_los_spe_n",
   "type": "Restriccion",
   "label": "Restricción en garantes admisibles",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Los garantes admisibles se limitan a los estipulados en el punto 5.4.1. Los SPE no son garantes admisibles."
  },
  {
   "id": "Restriccion_no_correspondera_la_evaluacion_de_la_capacidad_de_repago_respecto_de_las_financi",
   "type": "Restriccion",
   "label": "Excención de evaluación por garantías preferidas A",
   "tokens_matcheados": 3,
   "resumen_propiedades": "No corresponderá la evaluación de la capacidad de repago respecto de las financiaciones que se encuentren respaldadas con tales garantías"
  },
  {
   "id": "Obligacion_aplicar_disposiciones_de_punto_8_3_4_a_deuda_computable_como_ca_o_pnc",
   "type": "Obligacion",
   "label": "Aplicar disposiciones de punto 8.3.4 a deuda computable como CA o PNc",
   "tokens_matcheados": 3,
   "resumen_propiedades": "En el caso de los instrumentos de deuda computables como CA o PNc, al admitir los aportes, se deberá tener en cuenta lo dispuesto en el punto 8.3.4"
  },
  {
   "id": "Excepcion_con_excepcion_de_los_casos_contemplados_en_el_punto_4_1",
   "type": "Excepcion",
   "label": "Excepción casos punto 4.1",
   "tokens_matcheados": 2,
   "resumen_propiedades": "con excepción de los casos contemplados en el punto 4.1"
  },
  {
   "id": "Obligacion_se_incrementara_el_valor_de_los_activos_en_garantia_dados_por_la_entidad_y_se_re",
   "type": "Obligacion",
   "label": "Aplicar aforos a garantías",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Se incrementará el valor de los activos en garantía dados por la entidad y se reducirá el valor de los recibidos, utilizando aforos aplicables a transacciones R…"
  },
  {
   "id": "Obligacion_cuando_el_pago_a_nombre_del_cliente_encuadre_en_el_punto_10_10_2_3_se_debera_dej",
   "type": "Obligacion",
   "label": "Dejar constancia en reporte",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Cuando el pago a nombre del cliente encuadre en el punto 10.10.2.3., se deberá dejar constancia de tal circunstancia al reportar el boleto de venta a nombre del…"
  },
  {
   "id": "Restriccion_el_activo_recibido_en_garantia_se_limitara_a_aquellos_listados_en_el_punto_5_3_1",
   "type": "Restriccion",
   "label": "Activos limitados a listado",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El activo recibido en garantía se limitará a aquellos listados en el punto 5.3.1.2."
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
  }
 ]
}

--- paso 11 · buscar_nodos · input={"consulta": "estado nacional provincia municipio banco central deudores", "limite": 10} ---
{
 "consulta": "estado nacional provincia municipio banco central deudores",
 "total_con_match": 71,
 "resultados": [
  {
   "id": "Operacion_estado_de_situacion_de_deudores",
   "type": "Operacion",
   "label": "Estado de situación de deudores",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Estado de situación de deudores referenciado en punto 6.1. y 6.2."
  },
  {
   "id": "Excepcion_creditos_frente_al_banco_central_de_la_republica_argentina_estan_excluidos",
   "type": "Excepcion",
   "label": "Exclusión de créditos frente al BCRA",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Créditos frente al Banco Central de la República Argentina están excluidos"
  },
  {
   "id": "Obligacion_el_banco_central_de_la_republica_argentina_establecera_las_condiciones_y_plazos_",
   "type": "Obligacion",
   "label": "BCRA establecerá condiciones y plazos",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El BANCO CENTRAL DE LA REPÚBLICA ARGENTINA establecerá las condiciones y plazos para el ingreso de contravalor de exportación"
  },
  {
   "id": "Excepcion_garantias_otorgadas_a_favor_del_banco_central_estan_excluidas",
   "type": "Excepcion",
   "label": "Exclusión de garantías a favor del BCRA",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Garantías otorgadas a favor del Banco Central están excluidas"
  },
  {
   "id": "Obligacion_el_banco_central_de_la_republica_argentina_establecera_los_supuestos_en_los_que_",
   "type": "Obligacion",
   "label": "BCRA establecerá supuestos de autorización",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El BANCO CENTRAL DE LA REPÚBLICA ARGENTINA establecerá los supuestos en los que el acceso al mercado de cambios requerirá autorización previa, con base en pauta…"
  },
  {
   "id": "Excepcion_excepcion_para_todas_las_organizaciones_empresariales_donde_el_estado_nacional_t",
   "type": "Excepcion",
   "label": "Excepción requisito demora empresas estatales",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Excepción para todas las organizaciones empresariales donde el Estado Nacional tenga participación mayoritaria en el capital o en la formación de las decisiones…"
  },
  {
   "id": "Obligacion_el_banco_central_de_la_republica_argentina_establecera_reglamentaciones_que_evit",
   "type": "Obligacion",
   "label": "BCRA establecerá reglamentaciones preventivas",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El BANCO CENTRAL DE LA REPÚBLICA ARGENTINA establecerá reglamentaciones que eviten prácticas y operaciones tendientes a eludir lo dispuesto en esta medida"
  },
  {
   "id": "Excepcion_modificacion_en_forma_negativa_de_la_clasificacion_del_cliente_en_la_central_de_",
   "type": "Excepcion",
   "label": "Excepción por cambio negativo en Central de deudores",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Modificación en forma negativa de la clasificación del cliente en la Central de deudores del sistema financiero, llevándola a un grado inferior al de la entidad…"
  },
  {
   "id": "EntidadFinanciera_banco",
   "type": "EntidadFinanciera",
   "label": "Bancos",
   "tokens_matcheados": 1,
   "resumen_propiedades": "categoria: banco"
  },
  {
   "id": "EntidadFinanciera_deudor",
   "type": "EntidadFinanciera",
   "label": "Deudores",
   "tokens_matcheados": 1,
   "resumen_propiedades": "categoria: deudor"
  }
 ]
}

--- paso 12 · buscar_nodos · input={"consulta": "cesión sin responsabilidad cedente deudores", "limite": 10} ---
{
 "consulta": "cesión sin responsabilidad cedente deudores",
 "total_con_match": 126,
 "resultados": [
  {
   "id": "Operacion_cesion_de_operaciones_sin_responsabilidad_para_el_cedente",
   "type": "Operacion",
   "label": "Cesión sin responsabilidad",
   "tokens_matcheados": 4,
   "resumen_propiedades": "tipo: cesión de operaciones sin responsabilidad para el cedente"
  },
  {
   "id": "Operacion_cesion_de_creditos_sin_responsabilidad",
   "type": "Operacion",
   "label": "Cesión de créditos",
   "tokens_matcheados": 3,
   "resumen_propiedades": "tipo: cesión de créditos sin responsabilidad"
  },
  {
   "id": "Excepcion_financiaciones_sin_responsabilidad_para_el_cedente_amparadas_con_seguros_de_cred",
   "type": "Excepcion",
   "label": "Financiaciones con seguros de crédito",
   "tokens_matcheados": 3,
   "resumen_propiedades": "Financiaciones sin responsabilidad para el cedente amparadas con seguros de crédito por riesgo comercial y con seguros de riesgo de crédito con alcance de compr…"
  },
  {
   "id": "Operacion_operaciones_de_titulizacion_y_venta_o_cesion_de_cartera_con_responsabilidad",
   "type": "Operacion",
   "label": "Titulización cartera",
   "tokens_matcheados": 2,
   "resumen_propiedades": "tipo: Operaciones de titulización y venta o cesión de cartera con responsabilidad"
  },
  {
   "id": "Restriccion_no_seran_objeto_de_clasificacion_quienes_resulten_deudores_en_operaciones_de_ces",
   "type": "Restriccion",
   "label": "Exclusión de deudores en cesión",
   "tokens_matcheados": 2,
   "resumen_propiedades": "No serán objeto de clasificación quienes resulten deudores en operaciones de cesión sin responsabilidad para el cedente"
  },
  {
   "id": "Obligacion_los_creditos_cedidos_a_favor_de_la_entidad_sin_responsabilidad_se_imputaran_al_f",
   "type": "Obligacion",
   "label": "Imputación al firmante o pagador",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Los créditos cedidos a favor de la entidad sin responsabilidad se imputarán al firmante, librador, deudor, codeudor o aceptante de los respectivos instrumentos"
  },
  {
   "id": "Restriccion_la_revocacion_sera_sin_costo_ni_responsabilidad_alguna_para_el_usuario_en_la_med",
   "type": "Restriccion",
   "label": "Revocación sin costo ni responsabilidad",
   "tokens_matcheados": 2,
   "resumen_propiedades": "La revocación será sin costo ni responsabilidad alguna para el usuario en la medida que no haya hecho uso del respectivo producto o servicio y que, en el caso d…"
  },
  {
   "id": "Restriccion_en_caso_de_no_efectuarse_la_evaluacion_de_creditos_cedidos_sin_responsabilidad_c",
   "type": "Restriccion",
   "label": "Clasificación irrecuperable sin evaluación",
   "tokens_matcheados": 2,
   "resumen_propiedades": "En caso de no efectuarse la evaluación de créditos cedidos sin responsabilidad, cualquiera sea el motivo, estos clientes se clasificarán en categoría irrecupera…"
  },
  {
   "id": "Excepcion_las_consultas_o_reclamos_originados_en_cuestiones_suscitadas_con_deudores_de_fid",
   "type": "Excepcion",
   "label": "Atención por cedente en transferencias fiduciarias",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Las consultas o reclamos originados en cuestiones suscitadas con deudores de fideicomisos financieros que no fueron notificados fehacientemente de la transferen…"
  },
  {
   "id": "EntidadFinanciera_deudor",
   "type": "EntidadFinanciera",
   "label": "Deudores",
   "tokens_matcheados": 1,
   "resumen_propiedades": "categoria: deudor"
  }
 ]
}

--- paso 13 · ver_nodo · input={"id": "Restriccion_no_seran_objeto_de_clasificacion_quienes_resulten_deudores_en_operaciones_de_ces"} ---
{
 "id": "Restriccion_no_seran_objeto_de_clasificacion_quienes_resulten_deudores_en_operaciones_de_ces",
 "type": "Restriccion",
 "label": "Exclusión de deudores en cesión",
 "properties": {
  "descripcion": "No serán objeto de clasificación quienes resulten deudores en operaciones de cesión sin responsabilidad para el cedente",
  "tipo": "prohibicion"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Punto 4.6. Financiaciones –sin responsabilidad para el cedente– amparadas con seguros de cr"
  }
 ]
}

--- paso 14 · buscar_nodos · input={"consulta": "garantías preferidas A definición estado nacional provincia", "limite": 10} ---
{
 "consulta": "garantías preferidas A definición estado nacional provincia",
 "total_con_match": 1191,
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
   "id": "Excepcion_garantias_otorgadas_a_favor_del_banco_central_estan_excluidas",
   "type": "Excepcion",
   "label": "Exclusión de garantías a favor del BCRA",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Garantías otorgadas a favor del Banco Central están excluidas"
  },
  {
   "id": "Excepcion_transferencias_a_cuentas_bancarias_en_el_exterior_de_personas_humanas_por_fondos",
   "type": "Excepcion",
   "label": "Transferencias por beneficios del Estado",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Transferencias a cuentas bancarias en el exterior de personas humanas por fondos percibidos en el país asociados a beneficios otorgados por el Estado Nacional e…"
  },
  {
   "id": "Excepcion_excepcion_para_todas_las_organizaciones_empresariales_donde_el_estado_nacional_t",
   "type": "Excepcion",
   "label": "Excepción requisito demora empresas estatales",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Excepción para todas las organizaciones empresariales donde el Estado Nacional tenga participación mayoritaria en el capital o en la formación de las decisiones…"
  },
  {
   "id": "Obligacion_el_sujeto_obligado_se_le_debera_informar_el_estado_del_tramite_cada_vez_que_lo_r",
   "type": "Obligacion",
   "label": "Informar estado de trámite a solicitud de usuario",
   "tokens_matcheados": 2,
   "resumen_propiedades": "El sujeto obligado se le deberá informar el estado del trámite cada vez que lo requiera."
  }
 ]
}

--- paso 15 · buscar_nodos · input={"consulta": "garantías preferidas A créditos estado nacional provincia municipio", "limite": 10} ---
{
 "consulta": "garantías preferidas A créditos estado nacional provincia municipio",
 "total_con_match": 1208,
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
   "id": "Obligacion_a_fin_de_determinar_el_importe_de_la_cancelacion_se_admitira_computar_el_50_de_l",
   "type": "Obligacion",
   "label": "Computar garantías adicionales",
   "tokens_matcheados": 2,
   "resumen_propiedades": "A fin de determinar el importe de la cancelación, se admitirá computar el 50 % de las garantías adicionales a las ofrecidas originalmente, constituidas sobre bi…"
  },
  {
   "id": "Obligacion_los_creditos_cedidos_a_favor_de_la_entidad_sin_responsabilidad_se_imputaran_al_f",
   "type": "Obligacion",
   "label": "Imputación al firmante o pagador",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Los créditos cedidos a favor de la entidad sin responsabilidad se imputarán al firmante, librador, deudor, codeudor o aceptante de los respectivos instrumentos"
  },
  {
   "id": "Obligacion_reportar_en_el_sepaimpo_dentro_de_los_5_cinco_dias_habiles_siguientes_a_la_fecha",
   "type": "Obligacion",
   "label": "Reportar cancelación de garantías",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Reportar en el SEPAIMPO dentro de los 5 (cinco) días hábiles siguientes a la fecha de acceso al mercado de cambios, la CUIT y nombre del cliente por el cual se …"
  },
  {
   "id": "Restriccion_los_creditos_otorgados_a_deudores_en_concurso_preventivo_con_posterioridad_al_pe",
   "type": "Restriccion",
   "label": "Imputación condicional en concurso",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Los créditos otorgados a deudores en concurso preventivo con posterioridad al pedido de concurso sólo podrán imputarse al tercero si cuentan con garantías que p…"
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
   "id": "Obligacion_todos_los_derechos_inherentes_a_los_documentos_a_cobrar_y_creditos_deberan_ser_t",
   "type": "Obligacion",
   "label": "Transferir derechos a la titulización",
   "tokens_matcheados": 2,
   "resumen_propiedades": "Todos los derechos inherentes a los documentos a cobrar y créditos deberán ser transferidos a la titulización, a los efectos de garantizar a los tenedores de lo…"
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

## Apéndice B — CQ-017: outputs por paso (ver_nodo/ver_vecinos íntegros; buscar_nodos como posición+id+label)

```

--- paso 1 · buscar_nodos · input={"consulta": "operador de cambio", "limite": 10} ---
total_con_match=2409; resultados:
  [1] EntidadFinanciera_operador_de_cambio  (label: Operadores de cambio)
  [2] EntidadFinanciera_casa_de_cambio  (label: Casas de cambio)
  [3] EntidadFinanciera_agencia_de_cambio  (label: Agencias de cambio)
  [4] Operacion_cambio  (label: Operación de cambio)
  [5] Operacion_cambio_de_moneda  (label: Operación de cambio)
  [6] Obligacion_el_cambio_de_entidad_debe_quedar_registrado_en_el_bcra  (label: Registrar cambio en BCRA)
  [7] Obligacion_boleto_de_venta_de_cambio  (label: Boleto de venta de cambio)
  [8] Obligacion_comunicar_con_6_meses_de_anticipacion_cambios_de_metodo  (label: Preaviso cambio de método)
  [9] Obligacion_la_entidad_debera_realizar_un_boleto_de_compra_y_o_venta_de_cambio_conforme_a_lo  (label: Realizar boleto de cambio)
  [10] Obligacion_la_entidad_debera_realizar_un_boleto_de_venta_de_cambio_a_nombre_del_importador_  (label: Boleto de venta de cambio)

--- paso 2 · buscar_nodos · input={"consulta": "Protección Usuarios Servicios Financieros", "limite": 10} ---
total_con_match=162; resultados:
  [1] TextoOrdenado_to_proteccion_usuarios_servicios_financieros_actual_pdf  (label: Protección de Usuarios)
  [2] EntidadFinanciera_usuario_de_servicio_financiero  (label: Usuarios de servicios financieros)
  [3] Obligacion_la_gerencia_principal_de_proteccion_al_usuario_de_servicios_financieros_tramitar  (label: Tramitar denuncias de asociaciones)
  [4] Obligacion_los_sujetos_obligados_deberan_ofrecer_a_los_usuarios_de_servicios_financieros_po  (label: Ofrecer mínimo tres compañías aseguradoras)
  [5] Obligacion_las_presentaciones_de_los_usuarios_de_servicios_financieros_deberan_poder_realiz  (label: Habilitar múltiples canales de presentación)
  [6] Obligacion_la_gerencia_principal_de_proteccion_al_usuario_de_servicios_financieros_brindara  (label: Brindar respuesta a consultas sobre normativa)
  [7] Obligacion_dando_orientacion_a_los_usuarios_de_servicios_financieros_sobre_la_manera_de_can  (label: Dar orientación sobre canalización de reclamos)
  [8] Obligacion_se_debe_notificar_en_el_contrato_a_los_usuarios_de_servicios_financieros_sobre_l  (label: Notificar condiciones modificables en contrato)
  [9] Obligacion_los_cajeros_automaticos_destinados_a_los_usuarios_de_servicios_financieros_con_d  (label: Cajeros con funcionalidades para usuarios visuales)
  [10] Obligacion_tambien_se_recibiran_de_los_usuarios_de_servicios_financieros_por_igual_via_come  (label: Recibir comentarios, sugerencias y quejas de usuarios)

--- paso 3 · buscar_nodos · input={"consulta": "mercado de cambios entidad autorizada", "limite": 10} ---
total_con_match=2504; resultados:
  [1] Obligacion_la_entidad_debera_al_momento_de_dar_acceso_al_mercado_de_cambios_contar_con_la_c  (label: Convalidación en sistema online)
  [2] Obligacion_ingreso_y_liquidacion_en_mercado_de_cambios_en_30_dias_corridos_para_exportacion  (label: Ingreso en plazo 30 días)
  [3] Obligacion_ingreso_y_liquidacion_en_mercado_de_cambios_en_60_dias_corridos_para_operaciones  (label: Ingreso en plazo 60 días)
  [4] Obligacion_los_anticipos_deberan_ser_ingresadas_y_liquidadas_en_el_mercado_de_cambios_dentr  (label: Liquidación de anticipos)
  [5] Operacion_endeudamiento_financiero_para_acceso_al_mercado_de_cambios  (label: Endeudamiento financiero)
  [6] Obligacion_ingreso_y_liquidacion_en_mercado_de_cambios_en_180_dias_corridos_para_el_resto_d  (label: Ingreso en plazo 180 días)
  [7] Obligacion_ingreso_y_liquidacion_en_mercado_de_cambios_en_365_dias_corridos_para_operacione  (label: Ingreso en plazo 365 días)
  [8] Operacion_liquidacion_en_el_mercado_de_cambios  (label: Liquidación mercado cambios)
  [9] Operacion_acceso_a_mercado_de_cambios  (label: Acceso al mercado de cambios)
  [10] Operacion_acceso_a_mercado_de_cambios_para_cancelacion_de_lineas_de_credito  (label: Acceso al mercado de cambios)

--- paso 4 · ver_nodo · input={"id": "EntidadFinanciera_operador_de_cambio"} ---
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

--- paso 5 · ver_nodo · input={"id": "TextoOrdenado_to_proteccion_usuarios_servicios_financieros_actual_pdf"} ---
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

--- paso 6 · ver_vecinos · input={"id": "EntidadFinanciera_operador_de_cambio", "direccion": "ambas"} ---
{
 "id": "EntidadFinanciera_operador_de_cambio",
 "label": "Operadores de cambio",
 "n_salientes_total": 1,
 "n_entrantes_total": 1,
 "salientes": [
  {
   "relation": "ejecuta",
   "vecino_id": "Operacion_operacion_de_cambio",
   "vecino_label": "Operaciones de cambio en divisas",
   "provenances": [
    {
     "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
     "location": "Punto 1.1. Partes."
    }
   ]
  }
 ],
 "salientes_truncado": false,
 "entrantes": [
  {
   "relation": "aplica_a",
   "vecino_id": "Obligacion_cuando_un_tercero_desarrolle_tareas_relativas_a_servicios_ofrecidos_por_los_suje",
   "vecino_label": "Responsabilidad de terceros",
   "provenances": [
    {
     "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
     "location": "Punto 1.1. Partes."
    }
   ]
  }
 ],
 "entrantes_truncado": false
}

--- paso 7 · ver_nodo · input={"id": "Obligacion_cuando_un_tercero_desarrolle_tareas_relativas_a_servicios_ofrecidos_por_los_suje"} ---
{
 "id": "Obligacion_cuando_un_tercero_desarrolle_tareas_relativas_a_servicios_ofrecidos_por_los_suje",
 "type": "Obligacion",
 "label": "Responsabilidad de terceros",
 "properties": {
  "descripcion": "Cuando un tercero desarrolle tareas relativas a servicios ofrecidos por los sujetos obligados o en su nombre, ambos serán responsables por el cumplimiento de las presentes normas. Lo anterior deberá establecerse en los instrumentos que acuerden la realización de dichas tareas.",
  "tipo": "otra"
 },
 "provenances": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "Punto 1.1. Partes."
  }
 ]
}

--- paso 8 · buscar_nodos · input={"consulta": "operador cambio sujeto obligado protección usuarios", "limite": 10} ---
total_con_match=140; resultados:
  [1] Restriccion_el_importe_de_los_cargos_que_el_sujeto_obligado_transfiera_a_los_usuarios_no_pod  (label: Cargos no superiores a costo de terceros)
  [2] Obligacion_el_sujeto_obligado_debera_verificar_si_situaciones_que_generan_la_obligacion_de_  (label: Verificar situaciones de reintegro en usuarios)
  [3] Obligacion_recibir_y_dar_curso_a_las_presentaciones_concernientes_al_sujeto_obligado_que_re  (label: Recibir y dar curso a presentaciones de usuarios)
  [4] EntidadFinanciera_sujeto_obligado  (label: Sujetos obligados)
  [5] EntidadFinanciera_operador_de_cambio  (label: Operadores de cambio)
  [6] TextoOrdenado_to_proteccion_usuarios_servicios_financieros_actual_pdf  (label: Protección de Usuarios)
  [7] Excepcion_cuando_medien_causas_ajenas_al_sujeto_obligado_debidamente_justificadas  (label: Causas ajenas justificadas)
  [8] Excepcion_cuando_reglamentariamente_se_hayan_otorgado_al_sujeto_obligado_mayores_plazos_pa  (label: Plazo mayor por reglamentación)
  [9] Obligacion_en_el_caso_de_que_el_sujeto_obligado_pretenda_incorporar_nuevos_conceptos_en_cal  (label: Obtener consentimiento del usuario)
  [10] Obligacion_el_sujeto_obligado_debera_conservar_constancia_de_haber_permitido_el_ejercicio_d  (label: Constancia de ejercicio de derechos)

--- paso 9 · ver_nodo · input={"id": "EntidadFinanciera_sujeto_obligado"} ---
{
 "id": "EntidadFinanciera_sujeto_obligado",
 "type": "EntidadFinanciera",
 "label": "Sujetos obligados",
 "properties": {
  "categoria": "entidades financieras"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Punto 7.2. Niveles de clasificación. (parte 1)"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Punto 1.2. Exigencia básica."
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Punto 1.3. Integración."
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 2.2. Cobros de exportaciones de servicios. (parte 2)"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 4.6. Suscripción de bonos BOPREAL por utilidades y dividendos de accionistas no resid"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 9.7. Operaciones cursadas por el Sistema de Monedas Locales (SML)."
  }
 ]
}

--- paso 10 · ver_vecinos · input={"id": "EntidadFinanciera_sujeto_obligado", "direccion": "salientes"} ---
{
 "id": "EntidadFinanciera_sujeto_obligado",
 "label": "Sujetos obligados",
 "n_salientes_total": 104,
 "n_entrantes_total": 991,
 "salientes": [
  {
   "relation": "ejecuta",
   "vecino_id": "Operacion_asignacion_de_calificaciones",
   "vecino_label": "Asignación de calificaciones crediticias",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 10.3. Consideraciones para su implementación."
    }
   ]
  },
  {
   "relation": "ejecuta",
   "vecino_id": "Operacion_aplicacion_de_ponderador_con_multiples_calificaciones",
   "vecino_label": "Tratamiento de múltiples calificaciones",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 10.3. Consideraciones para su implementación."
    }
   ]
  },
  {
   "relation": "ejecuta",
   "vecino_id": "Operacion_inversion_en_emision",
   "vecino_label": "Inversión en emisión calificada",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 10.3. Consideraciones para su implementación."
    }
   ]
  },
  {
   "relation": "ejecuta",
   "vecino_id": "Operacion_uso_de_evaluacion_entre_entidades_del_grupo",
   "vecino_label": "Uso de evaluación de unidad de grupo",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 10.3. Consideraciones para su implementación."
    }
   ]
  },
  {
   "relation": "ejecuta",
   "vecino_id": "Operacion_financiacion",
   "vecino_label": "Financiación a actividad agrícola",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 2.10. A los fines de calcular el límite definido en el párrafo precedente, se aplicará"
    }
   ]
  },
  {
   "relation": "ejecuta",
   "vecino_id": "Operacion_clasificacion_de_exposiciones",
   "vecino_label": "Clasificación de exposiciones a instrumentos",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 2.9. Exposiciones con garantía hipotecaria."
    }
   ]
  },
  {
   "relation": "ejecuta",
   "vecino_id": "Operacion_titulizacion_de_exposiciones_subyacentes",
   "vecino_label": "Titulización de exposiciones",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 3.1. Tratamiento de las titulizaciones. (parte 2)"
    }
   ]
  },
  {
   "relation": "ejecuta",
   "vecino_id": "Operacion_metodo_de_calculo_de_ponderador_de_riesgo",
   "vecino_label": "Tratamiento de transparencia (look-through)",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 3.1. Tratamiento de las titulizaciones. (parte 4)"
    }
   ]
  },
  {
   "relation": "ejecuta",
   "vecino_id": "Operacion_operacion_de_titulizacion_sintetica",
   "vecino_label": "Titulización sintética",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 3.1. Tratamiento de las titulizaciones. (parte 4)"
    }
   ]
  },
  {
   "relation": "ejecuta",
   "vecino_id": "Operacion_operacion_con_derivados_otc",
   "vecino_label": "Operaciones con derivados OTC",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 4.3. Exigencia de capital por riesgo de crédito de contraparte en operaciones con ent (parte 1)"
    }
   ]
  },
  {
   "relation": "ejecuta",
   "vecino_id": "Operacion_operacion_negociada_en_mercados_de_valores",
   "vecino_label": "Operaciones en mercados de valores",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 4.3. Exigencia de capital por riesgo de crédito de contraparte en operaciones con ent (parte 1)"
    }
   ]
  },
  {
   "relation": "ejecuta",
   "vecino_id": "Operacion_securities_financing_transactions_sft",
   "vecino_label": "Operaciones de financiación con títulos valores",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 4.3. Exigencia de capital por riesgo de crédito de contraparte en operaciones con ent (parte 1)"
    }
   ]
  },
  {
   "relation": "ejecuta",
   "vecino_id": "Operacion_operacion_de_liquidacion_diferida",
   "vecino_label": "Operaciones de liquidación diferida",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 4.3. Exigencia de capital por riesgo de crédito de contraparte en operaciones con ent (parte 1)"
    }
   ]
  },
  {
   "relation": "ejecuta",
   "vecino_id": "Operacion_operaciones_de_negociacion_con_ccp",
   "vecino_label": "Operaciones de negociación",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 4.3. Exigencia de capital por riesgo de crédito de contraparte en operaciones con ent (parte 5)"
    }
   ]
  },
  {
   "relation": "ejecuta",
   "vecino_id": "Operacion_operaciones_de_financiacion_con_titulos_valores",
   "vecino_label": "Operaciones con SFT",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 4.3. Exigencia de capital por riesgo de crédito de contraparte en operaciones con ent (parte 5)"
    }
   ]
  },
  {
   "relation": "ejecuta",
   "vecino_id": "Operacion_liquidacion_en_efectivo",
   "vecino_label": "Liquidación en efectivo de derivados",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 5.2. Requisitos para la aplicación de técnicas de coberturas del riesgo de crédito. (parte 2)"
    }
   ]
  },
  {
   "relation": "ejecuta",
   "vecino_id": "Operacion_ajuste_de_exposicion",
   "vecino_label": "Ajuste de exposición por volatilidad",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 5.3. Operaciones cubiertas con activos admitidos como garantía. (parte 2)"
    }
   ]
  },
  {
   "relation": "ejecuta",
   "vecino_id": "Operacion_calculo",
   "vecino_label": "Cálculo exigencia capital riesgo operacional",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 5.3. Operaciones cubiertas con activos admitidos como garantía. (parte 2)"
    }
   ]
  },
  {
   "relation": "ejecuta",
   "vecino_id": "Operacion_posicion_en_acciones",
   "vecino_label": "Tenencia de posiciones en acciones",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 6.3. Exigencia de capital por riesgo de posiciones en acciones."
    }
   ]
  },
  {
   "relation": "ejecuta",
   "vecino_id": "Operacion_posicion_neta_al_contado",
   "vecino_label": "Posición neta contado en moneda",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 6.4. Exigencia de capital por riesgo de tipo de cambio."
    }
   ]
  },
  {
   "relation": "ejecuta",
   "vecino_id": "Operacion_posicion_neta_a_plazo",
   "vecino_label": "Posición neta a plazo en divisas",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 6.4. Exigencia de capital por riesgo de tipo de cambio."
    }
   ]
  },
  {
   "relation": "ejecuta",
   "vecino_id": "Operacion_operacion_cambio_a_termino",
   "vecino_label": "Operaciones cambio a término",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 6.4. Exigencia de capital por riesgo de tipo de cambio."
    }
   ]
  },
  {
   "relation": "ejecuta",
   "vecino_id": "Operacion_cobertura_derivados",
   "vecino_label": "Cobertura de ingresos egresos futuros",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 6.4. Exigencia de capital por riesgo de tipo de cambio."
    }
   ]
  },
  {
   "relation": "ejecuta",
   "vecino_id": "Operacion_posicion_opciones_sobre_divisas",
   "vecino_label": "Cartera opciones sobre divisas",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 6.4. Exigencia de capital por riesgo de tipo de cambio."
    }
   ]
  },
  {
   "relation": "ejecuta",
   "vecino_id": "Operacion_contrato_a_termino",
   "vecino_label": "Contrato a término divisas o oro",
   "provenances": [
    {
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location": "Punto 6.4. Exigencia de capital por riesgo de tipo de cambio."
    }
   ]
  },
  {
   "relation": "ejecuta",
   "vecino_id": "Operacion_clasificacion_de_deudor",
   "vecino_label": "Evaluación grado de inversión",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "Punto 7.3. Recategorización obligatoria."
    }
   ]
  },
  {
   "relation": "ejecuta",
   "vecino_id": "Operacion_otorgamiento_de_financiaciones_de_consumo_o_vivienda",
   "vecino_label": "Financiaciones consumo vivienda",
   "provenances": [
    {
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location": "Punto 7.4. Información a la SEFyC sobre incrementos de la cartera irregular."
    }
   ]
  },
  {
   "relation": "ejecuta",
   "vecino_id": "Operacion_acceso_al_mercado_de_cambios",
   "vecino_label": "Acceso al mercado de cambios",
   "provenances": [
    {
     "source_doc": "TO_exterior_cambios_actual.pdf",
     "location": "Punto 1.2. Las entidades podrán dar acceso al mercado de cambios a las personas humanas o j"
    }
   ]
  },
  {
   "relation": "ejecuta",
   "vecino_id": "Operacion_cambio",
   "vecino_label": "Operación de cambio",
   "provenances": [
    {
     "source_doc": "TO_exterior_cambios_actual.pdf",
     "location": "Punto 1.3. Las operaciones de cambio serán realizadas al tipo de cambio que sea libremente"
    }
   ]
  },
  {
   "relation": "ejecuta",
   "vecino_id": "Operacion_canje",
   "vecino_label": "Canje",
   "provenances": [
    {
     "source_doc": "TO_exterior_cambios_actual.pdf",
     "location": "Punto 1.3. Las operaciones de cambio serán realizadas al tipo de cambio que sea libremente"
    }
   ]
  },
  {
   "relation": "ejecuta",
   "vecino_id": "Operacion_arbitraje",
   "vecino_label": "Arbitraje",
   "provenances": [
    {
     "source_doc": "TO_exterior_cambios_actual.pdf",
     "location": "Punto 1.3. Las operaciones de cambio serán realizadas al tipo de cambio que sea libremente"
    }
   ]
  },
  {
   "relation": "ejecuta",
   "vecino_id": "Operacion_financiacion_de_importaciones_de_bienes_otorgada_por_entidad_financiera_local_co",
   "vecino_label": "Financiación de importaciones con línea exterior",
   "provenances": [
    {
     "source_doc": "TO_exterior_cambios_actual.pdf",
     "location": "Punto 10.10. Disposiciones complementarias para importaciones de bienes que tuvieron o tendrá"
    }
   ]
  },
  {
   "relation": "ejecuta",
   "vecino_id": "Operacion_acceso_a_mercado_de_cambios",
   "vecino_label": "Acceso al mercado de cambios",
   "provenances": [
    {
     "source_doc": "TO_exterior_cambios_actual.pdf",
     "location": "Punto 10.1. Disposiciones generales."
    }
   ]
  },
  {
   "relation": "ejecuta",
   "vecino_id": "Operacion_pago_exterior",
   "vecino_label": "Pago de importaciones argentinas",
   "provenances": [
    {
     "source_doc": "TO_exterior_cambios_actual.pdf",
     "location": "Punto 10.1. Disposiciones generales."
    }
   ]
  },
  {
   "relation": "ejecuta",
   "vecino_id": "Operacion_financiacion_de_importaciones",
   "vecino_label": "Financiación de importaciones de bienes",
   "provenances": [
    {
     "source_doc": "TO_exterior_cambios_actual.pdf",
     "location": "Punto 10.2. Definiciones. (parte 2)"
    }
   ]
  },
  {
   "relation": "ejecuta",
   "vecino_id": "Operacion_pago_de_importaciones",
   "vecino_label": "Pagos de importaciones con registro aduanero",
   "provenances": [
    {
     "source_doc": "TO_exterior_cambios_actual.pdf",
     "location": "Punto 10.3. Pagos de importaciones de bienes que cuentan con registro de ingreso aduanero. (parte 1)"
    }
   ]
  },
  {
   "relation": "ejecuta",
   "vecino_id": "Operacion_pago_contra_documentacion",
   "vecino_label": "Pagos contra documentación de embarque",
   "provenances": [
    {
     "source_doc": "TO_exterior_cambios_actual.pdf",
     "location": "Punto 10.3. Pagos de importaciones de bienes que cuentan con registro de ingreso aduanero. (parte 1)"
    }
   ]
  },
  {
   "relation": "ejecuta",
   "vecino_id": "Operacion_pago_de_deuda_comercial",
   "vecino_label": "Pagos de deudas comerciales importación",
   "provenances": [
    {
     "source_doc": "TO_exterior_cambios_actual.pdf",
     "location": "Punto 10.3. Pagos de importaciones de bienes que cuentan con registro de ingreso aduanero. (parte 1)"
    }
   ]
  },
  {
   "relation": "ejecuta",
   "vecino_id": "Operacion_cancelacion_de_garantia",
   "vecino_label": "Cancelación de garantías comerciales",
   "provenances": [
    {
     "source_doc": "TO_exterior_cambios_actual.pdf",
     "location": "Punto 10.3. Pagos de importaciones de bienes que cuentan con registro de ingreso aduanero. (parte 1)"
    }
   ]
  },
  {
   "relation": "ejecuta",
   "vecino_id": "Operacion_pago_de_garantia_comercial",
   "vecino_label": "Cancelación de carta de crédito o letra avalada",
   "provenances": [
    {
     "source_doc": "TO_exterior_cambios_actual.pdf",
     "location": "Punto 10.3. Pagos de importaciones de bienes que cuentan con registro de ingreso aduanero. (parte 2)"
    }
   ]
  }
 ],
 "salientes_truncado": true
}

--- paso 11 · buscar_nodos · input={"consulta": "punto 1.1 partes sujetos obligados operador cambio", "limite": 10} ---
total_con_match=157; resultados:
  [1] Obligacion_los_sujetos_obligados_enumerados_en_el_punto_1_1_2_en_la_medida_en_que_correspon  (label: Cobertura mínima de cajeros accesibles)
  [2] EntidadFinanciera_sujeto_obligado  (label: Sujetos obligados)
  [3] EntidadFinanciera_operador_de_cambio  (label: Operadores de cambio)
  [4] Excepcion_con_excepcion_de_los_casos_contemplados_en_el_punto_4_1  (label: Excepción casos punto 4.1)
  [5] Excepcion_no_aplicable_punto_3_12_1  (label: No aplicable punto 3.12.1)
  [6] Restriccion_acciones_definidas_conforme_al_punto_2_11_3_250  (label: Ponderador acciones grupo 1)
  [7] Restriccion_el_activo_recibido_en_garantia_se_limitara_a_aquellos_listados_en_el_punto_5_3_1  (label: Activos limitados a listado)
  [8] Obligacion_la_facultad_de_revocacion_segun_lo_establecido_en_el_apartado_v_del_punto_2_3_1_  (label: Informar facultad de revocación)
  [9] Obligacion_los_sujetos_obligados_deberan_adoptar_las_acciones_necesarias_para_garantizar_de  (label: Garantizar derechos de usuarios)
  [10] Obligacion_los_sujetos_obligados_deberan_explicitar_en_un_manual_de_procedimiento_los_pasos  (label: Elaborar manual de procedimiento)

--- paso 12 · ver_nodo · input={"id": "Obligacion_los_sujetos_obligados_enumerados_en_el_punto_1_1_2_en_la_medida_en_que_correspon"} ---
{
 "id": "Obligacion_los_sujetos_obligados_enumerados_en_el_punto_1_1_2_en_la_medida_en_que_correspon",
 "type": "Obligacion",
 "label": "Cobertura mínima de cajeros accesibles",
 "properties": {
  "descripcion": "Los sujetos obligados enumerados en el punto 1.1.2., en la medida en que corresponda, deberán alcanzar la cobertura del servicio con esos cajeros automáticos en al menos el 10 % del total de los equipos instalados, comenzando con aquellos emplazados en las localidades de mayor población.",
  "tipo": "otra",
  "plazo": "sin plazo específico"
 },
 "provenances": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "Punto 2.2. Casos especiales."
  }
 ]
}

--- paso 13 · buscar_nodos · input={"consulta": "punto 1.1.2 sujetos obligados enumeración", "limite": 10} ---
total_con_match=118; resultados:
  [1] Obligacion_los_sujetos_obligados_enumerados_en_el_punto_1_1_2_en_la_medida_en_que_correspon  (label: Cobertura mínima de cajeros accesibles)
  [2] Restriccion_acciones_definidas_conforme_al_punto_2_11_3_250  (label: Ponderador acciones grupo 1)
  [3] Obligacion_la_facultad_de_revocacion_segun_lo_establecido_en_el_apartado_v_del_punto_2_3_1_  (label: Informar facultad de revocación)
  [4] EntidadFinanciera_sujeto_obligado  (label: Sujetos obligados)
  [5] Excepcion_con_excepcion_de_los_casos_contemplados_en_el_punto_4_1  (label: Excepción casos punto 4.1)
  [6] Excepcion_no_aplicable_punto_3_12_1  (label: No aplicable punto 3.12.1)
  [7] Obligacion_cuando_el_pago_a_nombre_del_cliente_encuadre_en_el_punto_10_10_2_3_se_debera_dej  (label: Dejar constancia en reporte)
  [8] Restriccion_el_activo_recibido_en_garantia_se_limitara_a_aquellos_listados_en_el_punto_5_3_1  (label: Activos limitados a listado)
  [9] Excepcion_salvo_que_la_operacion_quedase_comprendida_en_lo_previsto_en_el_punto_10_10_2_11  (label: Excepción por punto 10.10.2.11)
  [10] Obligacion_las_entidades_podran_dar_acceso_en_las_situaciones_previstas_en_14_2_1_en_la_med  (label: Cumplir requisitos de operación)

--- paso 14 · buscar_nodos · input={"consulta": "1.1.2 bancos entidades financieras", "limite": 10} ---
total_con_match=223; resultados:
  [1] Obligacion_las_entidades_financieras_del_grupo_1_deberan_llevar_a_cabo_un_proceso_de_debida  (label: Proceso de debida diligencia)
  [2] EntidadFinanciera_entidad_financiera_grupo_2  (label: Entidades financieras grupo 2)
  [3] Obligacion_las_entidades_podran_dar_acceso_en_las_situaciones_previstas_en_14_2_1_en_la_med  (label: Cumplir requisitos de operación)
  [4] Restriccion_exposiciones_a_instrumentos_por_parte_de_entidades_financieras_del_grupo_2_deuda  (label: Ponderador deuda subordinada grupo 2)
  [5] EntidadFinanciera_entidad_del_grupo_1  (label: Entidades del grupo 1)
  [6] EntidadFinanciera_entidad_del_grupo_2  (label: Entidades del grupo 2)
  [7] Operacion_transformacion_de_entidades_financieras  (label: Transformación de entidades)
  [8] Restriccion_acciones_definidas_conforme_al_punto_2_11_3_250  (label: Ponderador acciones grupo 1)
  [9] Restriccion_cuando_el_total_de_participaciones_en_el_capital_de_entidades_financieras_empres  (label: Límite tenencias capital 10%)
  [10] Restriccion_impedimento_para_transformacion_de_entidades_financieras_cuando_exista_obligacio  (label: Impedimento de transformación)

--- paso 15 · buscar_nodos · input={"consulta": "protección usuarios bancos cajas ahorro cooperativas cambio", "limite": 10} ---
total_con_match=132; resultados:
  [1] TextoOrdenado_to_proteccion_usuarios_servicios_financieros_actual_pdf  (label: Protección de Usuarios)
  [2] EntidadFinanciera_caja_de_credito_cooperativa  (label: Cajas de Crédito Cooperativas)
  [3] Excepcion_las_cajas_de_credito_cooperativas_quedan_exceptuadas_de_la_exigencia_basica_de_5  (label: Excepción Cajas de Crédito Cooperativas)
  [4] Obligacion_los_usuarios_tienen_derecho_a_la_proteccion_de_su_seguridad_e_intereses_economic  (label: Proteger seguridad e intereses económicos)
  [5] Obligacion_los_reportes_del_directivo_responsable_de_proteccion_de_los_usuarios_de_servicio  (label: Disponibilizar reportes Directivo Protección Usuarios)
  [6] EntidadFinanciera_banco  (label: Bancos)
  [7] EntidadFinanciera_cooperativa  (label: Cooperativas)
  [8] EntidadFinanciera_casa_de_cambio  (label: Casas de cambio)
  [9] EntidadFinanciera_caja_de_credito  (label: Cajas de Crédito)
  [10] EntidadFinanciera_usuario_del_rigi  (label: Usuarios del RIGI)
```

## Apéndice C — CQ-034: outputs por paso (ver_nodo/ver_vecinos íntegros; buscar_nodos como posición+id+label)

```

--- paso 1 · buscar_nodos · input={"consulta": "persona humana residente compra moneda extranjera atesorar límite mensual", "limite": 10} ---
total_con_match=323; resultados:
  [1] Operacion_compra_de_moneda_extranjera  (label: Compra de moneda extranjera)
  [2] Operacion_compra_de_moneda_extranjera_para_constituir_garantias  (label: Compra de moneda extranjera)
  [3] Excepcion_compra_de_billetes_en_moneda_extranjera_de_personas_humanas_no_residentes_en_con  (label: Compra de billetes por turismo)
  [4] Restriccion_las_garantias_acumuladas_en_moneda_extranjera_que_podran_ser_utilizadas_para_el_  (label: Límite de acumulación de garantías)
  [5] Restriccion_el_acceso_al_mercado_de_cambios_para_compra_de_moneda_extranjera_metales_precios  (label: Requerimiento de autorización previa)
  [6] Restriccion_limite_mensual_de_compra_en_efectivo  (label: Límite mensual de compra en efectivo)
  [7] Operacion_compra_venta_de_moneda_extranjera  (label: Compra y venta de monedas extranjeras)
  [8] Restriccion_el_importe_de_los_depositos_en_moneda_nacional_y_extranjera_no_podra_exceder_del  (label: Límite de depósitos por incumplimiento)
  [9] Excepcion_excepcion_apoderado_persona_humana_residente  (label: Excepción: apoderado persona humana residente)
  [10] Restriccion_las_ventas_con_liquidacion_en_moneda_extranjera_o_transferencias_de_bonos_boprea  (label: Límite monto suscripción primaria bonos BOPREAL)

--- paso 2 · buscar_nodos · input={"consulta": "límite compra dólares débito cuenta efectivo", "limite": 10} ---
total_con_match=282; resultados:
  [1] Restriccion_limite_mensual_de_compra_en_efectivo  (label: Límite mensual de compra en efectivo)
  [2] Restriccion_el_limite_se_incrementa_a_usd_200_por_operacion_por_los_retiros_de_efectivo_que_  (label: Límite adelanto países no limítrofes)
  [3] Restriccion_las_entidades_financieras_y_otras_emisoras_de_tarjetas_locales_de_credito_y_o_co  (label: Límite adelanto en efectivo exterior)
  [4] Obligacion_cursar_operacion_con_debito_en_cuenta  (label: Cursar operación con débito en cuenta)
  [5] Obligacion_las_entidades_financieras_deberan_ofrecer_a_sus_clientes_la_posibilidad_de_selec  (label: Ofrecer selección cuenta débito remota)
  [6] Excepcion_los_margenes_acordados_para_descubiertos_en_cuenta_corriente_y_limites_de_compra  (label: Exclusión de márgenes descubiertos y límites tarjeta)
  [7] Restriccion_el_importe_de_co_debera_ser_resultante_de_multiplicar_4_5_por_los_apr  (label: Límite mínimo CO)
  [8] Restriccion_el_importe_de_pnb_debera_ser_resultante_de_multiplicar_6_por_los_apr  (label: Límite mínimo PNb)
  [9] Restriccion_el_importe_de_rpc_debera_ser_resultante_de_multiplicar_8_por_los_apr  (label: Límite mínimo RPC)
  [10] Operacion_compra_de_opciones  (label: Compra de opciones)

--- paso 3 · buscar_nodos · input={"consulta": "formación activos externos límite general", "limite": 10} ---
total_con_match=270; resultados:
  [1] Operacion_formacion_de_activos_externos  (label: Formación de activos externos)
  [2] Restriccion_no_poseia_activos_externos_liquidos_disponibles_que_conjuntamente_tengan_un_valo  (label: Límite de activos externos líquidos)
  [3] Restriccion_limite_de_activos_en_cartera  (label: Límite de activos en cartera)
  [4] Restriccion_en_la_relacion_de_activos_inmovilizados_y_otros_conceptos_seccion_4_del_respecti  (label: Límite de activos inmovilizados)
  [5] Restriccion_limite_de_reduccion_para_entidades_del_grupo_b_17_en_condicion_general_11_o_7_en  (label: Límite reducción exigencia Grupo B)
  [6] Restriccion_limite_de_reduccion_para_entidades_del_grupo_c_14_en_condicion_general_8_o_5_en_  (label: Límite reducción exigencia Grupo C)
  [7] Operacion_tenencia_de_activos_externos_liquidos  (label: Tenencia de activos externos líquidos)
  [8] Restriccion_el_exceso_a_los_limites_para_la_afectacion_de_activos_en_garantia_segun_lo_dispu  (label: Límite de afectación activos garantía)
  [9] Operacion_presentacion_informativa_de_activos_y_pasivos_externos  (label: Relevamiento de activos y pasivos externos)
  [10] Obligacion_los_sujetos_alcanzados_deberan_cumplimentar_el_relevamiento_de_activos_y_pasivos  (label: Cumplimentar Relevamiento de activos y pasivos externos)

--- paso 4 · ver_nodo · input={"id": "Restriccion_limite_mensual_de_compra_en_efectivo"} ---
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

--- paso 5 · ver_nodo · input={"id": "Operacion_compra_de_moneda_extranjera"} ---
{
 "id": "Operacion_compra_de_moneda_extranjera",
 "type": "Operacion",
 "label": "Compra de moneda extranjera",
 "properties": {
  "tipo": "compra de moneda extranjera",
  "description": "Compra de moneda extranjera por parte de personas humanas residentes para la formación de activos externos en forma de billetes y/o depósitos"
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 3.11. Otras compras de moneda extranjera por parte de residentes con aplicación especí"
  }
 ]
}

--- paso 6 · ver_nodo · input={"id": "Operacion_formacion_de_activos_externos"} ---
{
 "id": "Operacion_formacion_de_activos_externos",
 "type": "Operacion",
 "label": "Formación de activos externos",
 "properties": {
  "tipo": "formación de activos externos"
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Punto 3.10. Compra de moneda extranjera por parte de otros residentes –excluidas las entidad"
  }
 ]
}

--- paso 7 · ver_vecinos · input={"id": "Operacion_compra_de_moneda_extranjera", "direccion": "salientes"} ---
{
 "id": "Operacion_compra_de_moneda_extranjera",
 "label": "Compra de moneda extranjera",
 "n_salientes_total": 1,
 "n_entrantes_total": 9,
 "salientes": [
  {
   "relation": "requiere",
   "vecino_id": "Obligacion_la_entidad_interviniente_haya_verificado_la_documentacion_del_endeudamiento_y_cu",
   "vecino_label": "Verificación de documentación de endeudamiento",
   "provenances": [
    {
     "source_doc": "TO_exterior_cambios_actual.pdf",
     "location": "Punto 3.11. Otras compras de moneda extranjera por parte de residentes con aplicación especí"
    }
   ]
  }
 ],
 "salientes_truncado": false
}

--- paso 8 · ver_vecinos · input={"id": "Operacion_compra_de_moneda_extranjera", "direccion": "entrantes"} ---
{
 "id": "Operacion_compra_de_moneda_extranjera",
 "label": "Compra de moneda extranjera",
 "n_salientes_total": 1,
 "n_entrantes_total": 9,
 "entrantes": [
  {
   "relation": "limita",
   "vecino_id": "Restriccion_el_monto_diario_de_acceso_no_supere_el_20_veinte_por_ciento_del_monto_previsto_e",
   "vecino_label": "Límite de acceso diario",
   "provenances": [
    {
     "source_doc": "TO_exterior_cambios_actual.pdf",
     "location": "Punto 3.11. Otras compras de moneda extranjera por parte de residentes con aplicación especí"
    }
   ]
  },
  {
   "relation": "limita",
   "vecino_id": "Restriccion_se_concreta_dentro_de_los_60_sesenta_dias_corridos_previos_a_la_fecha_de_vencimi",
   "vecino_label": "Límite acceso 60 días previos",
   "provenances": [
    {
     "source_doc": "TO_exterior_cambios_actual.pdf",
     "location": "Punto 3.11. Otras compras de moneda extranjera por parte de residentes con aplicación especí"
    }
   ]
  },
  {
   "relation": "limita",
   "vecino_id": "Restriccion_se_concreta_dentro_de_los_5_cinco_dias_habiles_previos_al_plazo_normativo_admiti",
   "vecino_label": "Límite acceso 5 días hábiles previos",
   "provenances": [
    {
     "source_doc": "TO_exterior_cambios_actual.pdf",
     "location": "Punto 3.11. Otras compras de moneda extranjera por parte de residentes con aplicación especí"
    }
   ]
  },
  {
   "relation": "limita",
   "vecino_id": "Restriccion_limite_mensual_de_compra_en_efectivo",
   "vecino_label": "Límite mensual de compra en efectivo",
   "provenances": [
    {
     "source_doc": "TO_exterior_cambios_actual.pdf",
     "location": "Punto 3.8. Compra de moneda extranjera por parte de personas humanas residentes para la for"
    }
   ]
  },
  {
   "relation": "condiciona",
   "vecino_id": "Obligacion_obtener_declaracion_jurada_de_cumplimiento",
   "vecino_label": "Obtener declaración jurada de cumplimiento",
   "provenances": [
    {
     "source_doc": "TO_exterior_cambios_actual.pdf",
     "location": "Punto 3.8. Compra de moneda extranjera por parte de personas humanas residentes para la for"
    }
   ]
  },
  {
   "relation": "regula",
   "vecino_id": "Obligacion_cursar_operacion_con_debito_en_cuenta",
   "vecino_label": "Cursar operación con débito en cuenta",
   "provenances": [
    {
     "source_doc": "TO_exterior_cambios_actual.pdf",
     "location": "Punto 3.8. Compra de moneda extranjera por parte de personas humanas residentes para la for"
    }
   ]
  },
  {
   "relation": "regula",
   "vecino_id": "Obligacion_entregar_billetes_o_acreditar_fondos",
   "vecino_label": "Entregar billetes o acreditar fondos",
   "provenances": [
    {
     "source_doc": "TO_exterior_cambios_actual.pdf",
     "location": "Punto 3.8. Compra de moneda extranjera por parte de personas humanas residentes para la for"
    }
   ]
  },
  {
   "relation": "regula",
   "vecino_id": "Obligacion_registrar_operacion_en_sistema_bcra",
   "vecino_label": "Registrar operación en sistema BCRA",
   "provenances": [
    {
     "source_doc": "TO_exterior_cambios_actual.pdf",
     "location": "Punto 3.8. Compra de moneda extranjera por parte de personas humanas residentes para la for"
    }
   ]
  },
  {
   "relation": "regula",
   "vecino_id": "Obligacion_obtener_evidencia_de_ingresos_o_activos",
   "vecino_label": "Obtener evidencia de ingresos o activos",
   "provenances": [
    {
     "source_doc": "TO_exterior_cambios_actual.pdf",
     "location": "Punto 3.8. Compra de moneda extranjera por parte de personas humanas residentes para la for"
    }
   ]
  }
 ],
 "entrantes_truncado": false
}

--- paso 9 · buscar_nodos · input={"consulta": "límite mensual débito cuenta USD 300", "limite": 10} ---
total_con_match=234; resultados:
  [1] Restriccion_el_agente_local_no_ha_utilizado_este_mecanismo_por_un_monto_superior_al_equivale  (label: Límite máximo de uso mensual)
  [2] Restriccion_el_limite_se_incrementa_a_usd_200_por_operacion_por_los_retiros_de_efectivo_que_  (label: Límite adelanto países no limítrofes)
  [3] Restriccion_limite_mensual_de_compra_en_efectivo  (label: Límite mensual de compra en efectivo)
  [4] Obligacion_cursar_operacion_con_debito_en_cuenta  (label: Cursar operación con débito en cuenta)
  [5] Obligacion_las_entidades_financieras_deberan_ofrecer_a_sus_clientes_la_posibilidad_de_selec  (label: Ofrecer selección cuenta débito remota)
  [6] Restriccion_si_el_monto_total_a_imputar_al_permiso_no_supera_el_equivalente_de_usd_25_000_do  (label: Límite para documentación simplificada)
  [7] Restriccion_maximo_mensual_equivalente_al_10_del_monto_total_de_los_anticipos_que_se_encuadr  (label: Límite cobros anticipados máximo mensual)
  [8] Restriccion_exportaciones_de_bienes_enviados_al_exterior_con_fines_promocionales_amparadas_p  (label: Límite de USD 5000 en exportación promocional)
  [9] Restriccion_limite_anual_usd_36_000_para_personas_humanas  (label: Límite anual USD 36.000 para personas humanas)
  [10] Restriccion_limite_usd_25_000_para_imputacion_sin_divisas  (label: Límite USD 25.000 para imputación sin divisas)

--- paso 10 · buscar_nodos · input={"consulta": "límite mensual compra moneda extranjera USD 300 débito", "limite": 10} ---
total_con_match=313; resultados:
  [1] Operacion_compra_de_moneda_extranjera  (label: Compra de moneda extranjera)
  [2] Operacion_compra_de_moneda_extranjera_para_constituir_garantias  (label: Compra de moneda extranjera)
  [3] Excepcion_compra_de_billetes_en_moneda_extranjera_de_personas_humanas_no_residentes_en_con  (label: Compra de billetes por turismo)
  [4] Restriccion_las_garantias_acumuladas_en_moneda_extranjera_que_podran_ser_utilizadas_para_el_  (label: Límite de acumulación de garantías)
  [5] Restriccion_el_acceso_al_mercado_de_cambios_para_compra_de_moneda_extranjera_metales_precios  (label: Requerimiento de autorización previa)
  [6] Restriccion_limite_mensual_de_compra_en_efectivo  (label: Límite mensual de compra en efectivo)
  [7] Operacion_compra_venta_de_moneda_extranjera  (label: Compra y venta de monedas extranjeras)
  [8] Restriccion_el_importe_de_los_depositos_en_moneda_nacional_y_extranjera_no_podra_exceder_del  (label: Límite de depósitos por incumplimiento)
  [9] Restriccion_las_ventas_con_liquidacion_en_moneda_extranjera_o_transferencias_de_bonos_boprea  (label: Límite monto suscripción primaria bonos BOPREAL)
  [10] Operacion_financiacion_en_moneda_extranjera_por_consumos_en_tarjeta_de_credito_o_compra  (label: Financiación moneda extranjera por tarjeta crédito)

--- paso 11 · buscar_nodos · input={"consulta": "compra moneda extranjera personas humanas residentes atesorar límite", "limite": 10} ---
total_con_match=335; resultados:
  [1] Excepcion_compra_de_billetes_en_moneda_extranjera_de_personas_humanas_no_residentes_en_con  (label: Compra de billetes por turismo)
  [2] Operacion_compra_de_moneda_extranjera  (label: Compra de moneda extranjera)
  [3] Operacion_compra_de_moneda_extranjera_para_constituir_garantias  (label: Compra de moneda extranjera)
  [4] Restriccion_las_garantias_acumuladas_en_moneda_extranjera_que_podran_ser_utilizadas_para_el_  (label: Límite de acumulación de garantías)
  [5] Restriccion_el_acceso_al_mercado_de_cambios_para_compra_de_moneda_extranjera_metales_precios  (label: Requerimiento de autorización previa)
  [6] Operacion_compra_venta_de_moneda_extranjera  (label: Compra y venta de monedas extranjeras)
  [7] Restriccion_el_importe_de_los_depositos_en_moneda_nacional_y_extranjera_no_podra_exceder_del  (label: Límite de depósitos por incumplimiento)
  [8] Restriccion_limite_anual_usd_36_000_para_personas_humanas  (label: Límite anual USD 36.000 para personas humanas)
  [9] Operacion_pago_de_obligaciones_en_moneda_extranjera  (label: Pago deudas moneda extranjera entre residentes)
  [10] Restriccion_las_ventas_con_liquidacion_en_moneda_extranjera_o_transferencias_de_bonos_boprea  (label: Límite monto suscripción primaria bonos BOPREAL)

--- paso 12 · ver_nodo · input={"id": "Obligacion_cursar_operacion_con_debito_en_cuenta"} ---
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

--- paso 13 · buscar_nodos · input={"consulta": "USD 300 mensual compra moneda extranjera", "limite": 10} ---
total_con_match=142; resultados:
  [1] Operacion_compra_de_moneda_extranjera  (label: Compra de moneda extranjera)
  [2] Operacion_compra_de_moneda_extranjera_para_constituir_garantias  (label: Compra de moneda extranjera)
  [3] Excepcion_compra_de_billetes_en_moneda_extranjera_de_personas_humanas_no_residentes_en_con  (label: Compra de billetes por turismo)
  [4] Restriccion_el_acceso_al_mercado_de_cambios_para_compra_de_moneda_extranjera_metales_precios  (label: Requerimiento de autorización previa)
  [5] Operacion_compra_venta_de_moneda_extranjera  (label: Compra y venta de monedas extranjeras)
  [6] Operacion_financiacion_en_moneda_extranjera_por_consumos_en_tarjeta_de_credito_o_compra  (label: Financiación moneda extranjera por tarjeta crédito)
  [7] Restriccion_sujecion_a_disposiciones_de_compra_de_moneda_extranjera  (label: Sujeción a disposiciones de compra de moneda extranjera)
  [8] Operacion_venta_de_moneda_extranjera  (label: Venta de divisas)
  [9] Operacion_recepcion_de_depositos_en_moneda_nacional_y_extranjera  (label: Recepción y depósitos)
  [10] Operacion_operacion_con_moneda_extranjera  (label: Liquidación de divisas)

--- paso 14 · buscar_nodos · input={"consulta": "300 dólares límite mensual", "limite": 10} ---
total_con_match=189; resultados:
  [1] Restriccion_el_agente_local_no_ha_utilizado_este_mecanismo_por_un_monto_superior_al_equivale  (label: Límite máximo de uso mensual)
  [2] Restriccion_limite_mensual_de_compra_en_efectivo  (label: Límite mensual de compra en efectivo)
  [3] Restriccion_maximo_mensual_equivalente_al_10_del_monto_total_de_los_anticipos_que_se_encuadr  (label: Límite cobros anticipados máximo mensual)
  [4] Restriccion_el_importe_de_co_debera_ser_resultante_de_multiplicar_4_5_por_los_apr  (label: Límite mínimo CO)
  [5] Restriccion_el_importe_de_pnb_debera_ser_resultante_de_multiplicar_6_por_los_apr  (label: Límite mínimo PNb)
  [6] Restriccion_el_importe_de_rpc_debera_ser_resultante_de_multiplicar_8_por_los_apr  (label: Límite mínimo RPC)
  [7] Restriccion_el_monto_diario_de_acceso_no_supere_el_20_veinte_por_ciento_del_monto_previsto_e  (label: Límite de acceso diario)
  [8] Restriccion_operaciones_comerciales_con_brasil_no_podran_tener_plazo_de_pago_que_exceda_360_  (label: Límite plazo pago Brasil)
  [9] Operacion_calculo_mensual_de_exigencia_operacional  (label: Determinación mensual CRO)
  [10] Restriccion_limite_de_monto_a_superar  (label: Límite de monto a superar)

--- paso 15 · buscar_nodos · input={"consulta": "Punto 3.8 compra moneda extranjera personas humanas residentes formación activos externos", "limite": 15} ---
total_con_match=309; resultados:
  [1] Excepcion_compra_de_billetes_en_moneda_extranjera_de_personas_humanas_no_residentes_en_con  (label: Compra de billetes por turismo)
  [2] Operacion_compra_de_moneda_extranjera  (label: Compra de moneda extranjera)
  [3] Operacion_compra_de_moneda_extranjera_para_constituir_garantias  (label: Compra de moneda extranjera)
  [4] Restriccion_el_activo_recibido_en_garantia_se_limitara_a_aquellos_listados_en_el_punto_5_3_1  (label: Activos limitados a listado)
  [5] Operacion_formacion_de_activos_externos  (label: Formación de activos externos)
  [6] Restriccion_el_acceso_al_mercado_de_cambios_para_compra_de_moneda_extranjera_metales_precios  (label: Requerimiento de autorización previa)
  [7] Operacion_compra_venta_de_moneda_extranjera  (label: Compra y venta de monedas extranjeras)
  [8] Operacion_pago_de_obligaciones_en_moneda_extranjera  (label: Pago deudas moneda extranjera entre residentes)
  [9] Operacion_financiacion_en_moneda_extranjera_por_consumos_en_tarjeta_de_credito_o_compra  (label: Financiación moneda extranjera por tarjeta crédito)
  [10] Restriccion_sujecion_a_disposiciones_de_compra_de_moneda_extranjera  (label: Sujeción a disposiciones de compra de moneda extranjera)
  [11] Obligacion_aplicar_disposiciones_de_punto_8_3_4_a_deuda_computable_como_ca_o_pnc  (label: Aplicar disposiciones de punto 8.3.4 a deuda computable como CA o PNc)
  [12] EntidadFinanciera_persona_humana  (label: Personas humanas)
  [13] Operacion_venta_de_moneda_extranjera  (label: Venta de divisas)
  [14] Operacion_recepcion_de_depositos_en_moneda_nacional_y_extranjera  (label: Recepción y depósitos)
  [15] Operacion_operacion_con_moneda_extranjera  (label: Liquidación de divisas)
```

---

## Tabla resumen — caso × afirmación de ausencia del GT × resultado de la auditoría

Cada celda remite a su evidencia en la sección del caso (barrido pegado y/o apéndice).

| Caso | Afirmación de ausencia del GT (vara) | Resultado de la auditoría (sobre outputs COMPLETOS re-ejecutados) |
|---|---|---|
| CQ-031 | "las búsquedas del agente en la traza no alcanzaron" el nodo portador del 4.5 (`Restriccion_los_deudores_cuyas_financiaciones_..._con_garanti`) | **CONFIRMADA con outputs completos** — el portador está AUSENTE en los 15 outputs (§1(a)); ausente incluso en los resultados de las 4 búsquedas que usaron "garantías preferidas A" (pasos 8, 10, 14, 15) |
| CQ-031 | (insumo para la prueba ex ante, no afirmación del GT) vocabulario "garantías" | Hechos (§1(b)): AUSENTE en la pregunta; EXPUESTO en outputs completos desde el paso 2 (pasos 2, 4, 6, 8, 9, 10, 11, 14, 15); la primera búsqueda del agente con "garantías preferidas A" es el paso 8, posterior a esa exposición |
| CQ-034 | "el dato pertinente nunca apareció en la trayectoria" — límite **USD 100 con efectivo (3.8)** | **REFUTADA: expuesto en paso 1 resultados[6]** (resumen con "USD 100 ... en el mes calendario") y **ABIERTO COMPLETO en paso 4 (ver_nodo)** con `umbral: "USD 100"` y provenance Punto 3.8; re-expuesto en pasos 2, 9, 10, 14 (§2) |
| CQ-034 | "el dato pertinente nunca apareció en la trayectoria" — límite **USD 200 otras modalidades (3.9)** | **CONFIRMADA para el dato del 3.9** — ningún output asocia USD 200 a otras modalidades/formación de activos externos/3.9. Hecho adicional: el literal "USD 200" SÍ está expuesto (pasos 2 y 9, resultados[2]) en un nodo de otro alcance (retiros de efectivo en países no limítrofes, provenance Punto 4.1) (§2) |
| CQ-034 | conceptos **A07 / A09** ausentes | **CONFIRMADA** — "A07" y "A09" AUSENTES en los 15 outputs completos (§2) |
| CQ-017 | "el contexto que conecta" Protección 1.1.2.2 con Exterior 1.1 "nunca apareció en la trayectoria" (arista cross-documento faltante) | **CONFIRMADA con outputs completos** — "1.1.2.2" AUSENTE en los 15 outputs; "entidad autorizada" AUSENTE como texto. Hecho adicional (sin adjudicar): el paso 10 (11.828 chars en runtime, 1.216 en traza) expone 13 edges de `EntidadFinanciera_sujeto_obligado` hacia operaciones del TO Exterior (incl. "acceso al mercado de cambios"); ninguno menciona 1.1.2.2, el Punto 1.1 ni "entidad autorizada"; los vecinos de `EntidadFinanciera_operador_de_cambio` (paso 6) son solo de Protección (§3) |
| CQ-017 | portadores de la regla de Exterior 1.1 no expuestos | **CONFIRMADA** — ids tipo `intervencion_de_entidades_autorizadas*` / `entidades_autorizadas_a_operar*` / `entidades_financieras_o_cambiarias*` AUSENTES en los 15 outputs completos (§3) |
| CQ-020 | "falta el nodo de frecuencia de reporte para riesgo de crédito" / "el dato pertinente nunca apareció en la trayectoria" | **CONFIRMADA en la trayectoria** — ningún output de los 11 pasos asocia frecuencia de reporte a riesgo de crédito (los matches de frecuencia son riesgo operacional, riesgo de mercado, o el filename del PDF en provenances — §4(a)). **Barrido del kg (4.050 nodos):** ningún nodo enuncia la frecuencia de reporte de la exigencia CRC; existen 2 nodos informativos mensuales vinculados a riesgo de crédito (incrementos por excesos; incumplimientos de Grandes Exposiciones), NINGUNO expuesto en la trayectoria — contenido pegado en §4(b), su estatus queda a adjudicación |
| CQ-020 | el agente usó el nodo de frecuencia de riesgo de MERCADO | Verificado (§4(c)): 1ª exposición en **paso 8 entrantes[4]** (solo id + label genérico "Informar exigencia de capitales por riesgo" + provenance); contenido completo ("riesgo de mercado con periodicidad mensual") expuesto al abrirlo en **paso 9 (ver_nodo)** |

Ninguna celda de esta tabla se respalda en la traza almacenada: todas las afirmaciones de
presencia/ausencia salen de los outputs COMPLETOS re-ejecutados determinísticamente
(fidelidad verificada por igualdad de largos runtime↔re-ejecución en 56/56 pasos, §0).

---

## Archivos abiertos durante esta auditoría

Del repo (todos SOLO LECTURA):

- `data/experiment/evaluacion/verificador.py` (lectura parcial: mecanismo `_ver_paso_completo`, líneas ~795-870)
- `data/experiment/evaluacion/harness.py` (lectura parcial: `GraphIndex`/tools líneas 130-232, `TRUNC_TOOL_OUTPUT`/`_truncate`, docstring)
- `data/experiment/evaluacion/loader.py` (docstring; `load_graph` vía import)
- `data/experiment/evaluacion/posthoc_run/traces/off/run_3/CQ-017.json` (lectura programática)
- `data/experiment/evaluacion/posthoc_run/traces/off/run_3/CQ-020.json` (lectura programática)
- `data/experiment/evaluacion/posthoc_run/traces/off/run_3/CQ-031.json` (lectura programática)
- `data/experiment/evaluacion/posthoc_run/traces/off/run_3/CQ-034.json` (lectura programática)
- `data/experiment/run_3_ppf_core/kg.json` (lectura programática vía `loader.load_graph("run_3")`)
- Listado de directorio: `posthoc_run/traces/off/run_3/` (`ls`, sin abrir otros archivos)

Fuera del repo (scratchpad de sesión): `reexec_run3.py`, `analisis_run3.py`,
`full_CQ-{017,020,031,034}.json`, `dump_reporte.txt` (artefactos intermedios de esta auditoría).

**`posthoc_run/dev_set/gate2_v57/` NO fue abierto** (ni listado ni leído ningún archivo suyo
en esta tarea). La traza post-hoc consumida es la del AGENTE (`traces/off/run_3/`), que no
contiene veredictos del verificador.

---

*Fin de la auditoría. Sin re-adjudicaciones ni análisis: los hechos quedan a disposición de la
adjudicación externa.*
