# Inventario verificado del recurso — insumo previo a la introducción del Informe de PF

Generado el 2026-08-31 sobre HEAD `6cb0121`, en unidad de SOLO LECTURA (este
archivo es la única escritura). Todo número de este documento fue re-parseado
en esta unidad desde el archivo citado; ningún número viene de memoria ni de
resúmenes. Convenciones de conteo:

- Nodos/aristas de un grafo: `python3 -c "import json; kg=json.load(open('<ruta>')); print(len(kg['nodes']), len(kg['edges']))"`.
- Tipos: `collections.Counter` sobre `n['type']` (nodos) y `e['relation']` (aristas).
- Commit de un archivo: `git log -1 --format=%h -- <ruta>`.
- sha256: `shasum -a 256 <ruta>` (acá se citan los 16 primeros hex).

El estado del working tree al generar NO estaba limpio: había 4 archivos
modificados y 10 sin trackear previos a esta unidad (corrida ESQ P1'' y
edición en curso de `main.tex`); ver §C.2 y el `git status` del reporte de
la unidad.

---

## A. Grafos existentes

### A.1 Grafos completos (los nueve `kg.json` de linaje principal)

Los nueve cubren los MISMOS 5 Textos Ordenados del subset
(`data/experiment/subset/`): `TO_capitales_minimos_actual.pdf`,
`TO_clasificacion_deudores_actual.pdf`, `TO_exterior_cambios_actual.pdf`,
`TO_proteccion_usuarios_servicios_financieros_actual.pdf`,
`TO_regimen_informativo_contable_mensual_actual.pdf` (verificado por parseo
del campo `provenance.source_doc` / `provenance.archivo` de cada nodo: 5
documentos únicos por grafo; en `grafo_v2`, `reensamblado_v3` y `salida_r1`
aparece además `esquema_v2_clases.json` como fuente de los nodos de diseño
del esqueleto).

| Ruta (`data/experiment/…`) | Nombre canónico / rol | sha256 (16) | Nodos | Aristas | Commit | Estado |
|---|---|---|---|---|---|---|
| `run_1_cookbook/kg.json` | Run 1 (cookbook), Fase 2.2 | `c47ab1241bbd2e92` | 4.014 | 4.287 | `e4de649` 2026-05-25 | Sellado (zona sellada, CLAUDE.md §3) |
| `run_2_papers/kg.json` | Run 2 (papers), Fase 2.2 | `582fc859934a87b9` | 6.214 | 5.680 | `9e363a9` 2026-05-27 | Sellado (ídem) |
| `run_3_ppf_core/kg.json` | **KG-Base** (`12c226e2`), ganador de la corrida congelada Fase 2.3 | `12c226e22b8fdc8f` | 4.050 | 6.634 | `58581b6` 2026-05-27 (alta); ganador en `d56020e` | Sellado (ídem; Gen. 1) |
| `run_4_schema_light/kg.json` | Run 4 (schema_light), Fase 2.2 | `dc6b23067f97e914` | 3.298 | 3.434 | `9d27d51` 2026-05-27 | Sellado (ídem) |
| `run_5_hybrid/kg.json` | Run 5 (hybrid), Fase 2.2 | `3b6b9e724c45eb15` | 6.095 | 5.764 | `199649c` 2026-06-03 | Sellado (ídem) |
| `grafo_v2/kg.json` | grafo_v2, medición sellada del escalón 1 — alias en colisión con "v2" (`docs/nomenclatura_grafos.md` §4) | `2c7487bb11c8dafe` | 3.872 | 7.231 | `11f0d4a` 2026-07-26 | Medición sellada (CLAUDE.md §3) |
| `grafo_v2/reensamblado_v3/kg.json` | **KG-Refinado** (`26fac8b4`), Gen. 2, ex-vigente hasta U-MIG-r1 | `26fac8b49f6c08c1` | 4.469 | 8.073 | `05984e1` 2026-08-03 (C7, última corrección) | Sellado, medido en EV2 |
| `reextraccion_v2/corpus_v2/salida/kg.json` | **KG-Reextraído** (`8e2eadee`), Gen. 3, pipeline E0–E3 (E4/E5 no ejecutados en esta release) | `8e2eadee57b48e00` | 6.178 | 11.415 | `5273c0c` 2026-08-12 | Sellado, medido en EV2 |
| `reextraccion_v2/corpus_v2/salida_r1/kg.json` | **KG-Reextraído-r1** (`0226e947`), pipeline E0–E5 completo — **grafo VIGENTE** (laudo `docs/laudo_promocion_r1_vigente.md`, commit `81587f9`) | `0226e9477baee02d` | 6.529 | 17.772 | `185e042` 2026-08-23 | Sellado y vigente; medido EV2 en `774acac` |

Nodos por tipo (parseo directo; se lista completo cuando el esquema es
cerrado, y top + cardinalidad cuando el modelo emitió tipos libres):

- `run_1_cookbook` (10 tipos): REQUIREMENT 1.076, CONCEPT 624, OPERATION 609, INSTRUMENT 517, CLASSIFICATION 305, REGULATED_SUBJECT 295, REPORT_ITEM 282, PROCESS 260, REGULATOR 36, SANCTION 10.
- `run_2_papers` (12 tipos): Obligacion 1.346, ConceptoDefinido 1.150, Requisito 1.042, Operacion 659, NormaReferenciada 477, Umbral 435, InstrumentoFinanciero 434, Plazo 265, SujetoRegulado 263, Procedimiento 105, OrganismoRegulador 28, Sancion 10.
- `run_3_ppf_core` = KG-Base (7 tipos): Obligacion 1.248, Operacion 892, Restriccion 818, Comunicacion 699, Excepcion 258, EntidadFinanciera 130, TextoOrdenado 5.
- `run_4_schema_light` (**858 tipos distintos**, esquema no cerrado en la práctica; top 10): sujeto_regulado 170, instrumento_financiero 103, operacion_regulada 83, requisito_regulatorio 61, documento_regulatorio 48, parametro_regulatorio 43, categoria_de_activo 40, tipo_de_operacion 40, concepto_regulatorio 38, concepto_deducible_de_capital 37.
- `run_5_hybrid` (20 tipos; top 10): Restriccion 2.671, Concepto 1.417, Operacion 921, Excepcion 294, Documento 240, InstrumentoFinanciero 210, EntidadFinanciera 123, RegimenInformativo 82, Autoridad 64, Plazo 26.
- `grafo_v2/kg.json` (7 tipos): Obligacion 1.292, Operacion 855, Restriccion 763, Comunicacion 648, Excepcion 231, Sujeto 78, TextoOrdenado 5.
- `reensamblado_v3` = KG-Refinado (7 tipos): Obligacion 1.427, Operacion 1.209, Restriccion 841, Comunicacion 654, Excepcion 252, Sujeto 81, TextoOrdenado 5.
- `salida` = KG-Reextraído (7 tipos): Obligacion 2.383, Operacion 1.837, Restriccion 1.318, Excepcion 506, Sujeto 93, Comunicacion 35, TextoOrdenado 6. *(Nota verificada: tiene SEIS nodos `TextoOrdenado` — «Capitales Mínimos Entidades Financieras» y «Texto Ordenado Capitales Mínimos» coexisten.)*
- `salida_r1` = KG-Reextraído-r1 (7 tipos): Obligacion 2.484, Operacion 1.957, Restriccion 1.397, Excepcion 539, Sujeto 111, Comunicacion 36, TextoOrdenado 5.

Aristas por tipo de relación (ídem):

- `run_1_cookbook`: **1.548 predicados distintos** (relación libre); top: aplica_a 186, requiere 172, está_sujeto_a 121, está_sujeta_a 110, incluye 95.
- `run_2_papers` (23 predicados): obligado_a 1.087, aplica_a 765, requiere 690, usa_concepto 638, condicion_de_aplicabilidad 457, tiene_umbral 368, involucra_instrumento 360, tiene_plazo 304, referencia 265, puede_realizar 230, resto <130 c/u.
- `run_3_ppf_core` = KG-Base (12 predicados, completo): establecida_en 2.453, aplica_a 1.464, regula 716, limita 570, referencia 558, ejecuta 204, condiciona 178, exceptua 174, prohibe 131, exceptua_obligacion 76, modificada_por 57, requiere 53.
- `run_4_schema_light`: **1.578 predicados distintos**; top: incluye 185, requiere 66, se_aplica_a 41, comprende 39, deduce 34.
- `run_5_hybrid`: **511 predicados distintos**; top: aplica_a 1.506, recae_sobre 781, realiza 324, comprende 316, excepciona_a 316.
- `grafo_v2/kg.json` (16 predicados, completo): establecida_en 2.613, aplica_a 1.903, regula 699, referencia 666, limita 530, requiere 221, exceptua 166, prohibe 131, condiciona 95, exceptua_obligacion 71, subclase_de 57, modificada_por 28, ejecuta 26, miembro_de 17, instancia_de 7, y 1 tipo más de frecuencia mínima.
- `reensamblado_v3` = KG-Refinado (16 predicados): establecida_en 3.007, aplica_a 2.077, regula 815, referencia 674, limita 600, requiere 240, exceptua 175, prohibe 141, condiciona 106, exceptua_obligacion 75, subclase_de 65, ejecuta 44, modificada_por 29, miembro_de 17, instancia_de 7, y 1 más de frecuencia mínima.
- `salida` = KG-Reextraído (11 predicados, completo): establecida_en 4.824, aplica_a 3.118, regula 1.249, limita 983, requiere 358, exceptua_obligacion 222, condiciona 212, exceptua 175, prohibe 158, ejecuta 82, referencia 34.
- `salida_r1` = KG-Reextraído-r1 (16 predicados, completo): referencia 5.680, establecida_en 5.082, aplica_a 3.254, regula 1.300, limita 1.041, requiere 375, exceptua_obligacion 236, condiciona 234, exceptua 184, prohibe 176, ejecuta 87, subclase_de 57, padre_sugerido 41, miembro_de 17, instancia_de 7, parte_de 1. *(Nota sobre el «23 relaciones» del mensaje del commit `185e042`: el esquema vigente declara **exactamente 12 predicados** — `data/experiment/reextraccion_v2/e1_extractor/prompt_e1.py`, sección «PREDICADOS VÁLIDOS (exactamente 12, ningún otro)» y constante `PREDICATES` (len 12: aplica_a, condiciona, ejecuta, establecida_en, exceptua, exceptua_obligacion, limita, modificada_por, prohibe, referencia, regula, requiere). El parseo de r1 da 16 tipos presentes: 11 de los 12 del esquema (`modificada_por` está AUSENTE) más 5 fuera del esquema, aportados por ensamblado/esqueleto: subclase_de 57, padre_sugerido 41, miembro_de 17, instancia_de 7, parte_de 1. El 23 del mensaje de commit no coincide ni con la lista del esquema (12) ni con lo emitido (16); no se adjudica acá su origen. `docs/tesis/mapa_fuentes_intro.md` fila 6 registra 16.)*

### A.2 Grafos intermedios y de calibración (no releases)

| Ruta (`data/experiment/…`) | Qué es | Nodos / aristas | Commit |
|---|---|---|---|
| `grafo_v2/smoke/kg_smoke.json` | Smoke de extracción v2 sobre Protección (U4–U4c) | 373 / 636 | `43f241e` 2026-07-18 |
| `grafo_v2/smoke_u4_prompt_8f366a9c1290/kg_smoke.json` | Smoke U4, prompt `8f366a9c1290` | 353 / 631 | `43f241e` |
| `grafo_v2/smoke_u4b_prompt_8c04ad89a8a7/kg_smoke.json` | Smoke U4b, prompt `8c04ad89a8a7` | 358 / 627 | `43f241e` |
| `grafo_v2/piloto/resultados/kg_<modelo>_r{1,2}.json` (6 archivos) | Piloto de selección de modelo (Haiku/Sonnet/Opus × 2 réplicas) | 223–269 / 369–452 | `b36d28f` 2026-07-26 |
| `run_3_ppf_core/code/cache/kg_smoke.json` | Smoke del Run 3 | 344 / 591 | `58581b6` |
| `run_3_ppf_core/code/cache/kg_intermediate.json` | Checkpoint intermedio del Run 3 | 617 / 1.076 | `58581b6` |

### A.3 Estados de grafo que ya NO existen como archivo

- **KG-Refinado pre-C1–C7** (4.458 nodos / 8.044 aristas): fue el estado que
  midió la pasada 1 intrínseca; el archivo `reensamblado_v3/kg.json` fue
  actualizado in-place por las correcciones C1–C7. El número sobrevive solo
  como texto en `data/experiment/metricas_intrinsecas/pasada1_resumen.md`
  (línea 9). No re-computable desde ningún kg.json actual.

---

## B. Corpus

### B.1 Descargado (todo `data/raw/`)

- **PDFs totales bajo `data/raw/`**: 3.171
  (`find data/raw -name "*.pdf" | wc -l`). El manifiesto general
  `data/raw/manifiesto.csv` tiene 3.177 filas de datos
  (`wc -l` → 3.178 con header); commit del scraper/manifiesto: ver
  `git log -- data/raw/manifiesto.csv`. Incluye marco legal, textos
  ordenados, comunicaciones A y B y versiones tachado/negrita
  (subdirectorios `00_marco_legal`, `01_textos_ordenados`,
  `02_comunicaciones_A`, `03_comunicaciones_B`, `06_tachado_negrita`).
- **Textos Ordenados**: `data/raw/01_textos_ordenados/actuales/` lista 161
  entradas (`ls | wc -l`); además hay `historicos/`.
- **Universo de escalado congelado** (`data/experiment/escalado_prep/`,
  commit `111ed19` 2026-08-13): **152 TOs** en `inventario_tos.csv`
  (152 filas de datos; columnas id/categoria/titulo_oficial/archivo/url),
  con PDFs congelados por sha256 en `manifest_pdfs.sha256` y copiados en
  `escalado_prep/pdfs/` (152 archivos, `ls | wc -l`). La cuenta 152 sale de
  `inventario_resumen.json`: 158 entradas del índice oficial − 1 URL
  duplicada − los 5 TOs del subset (excluidos explícitamente, campo
  `subset_excluido`). Por categoría: normativa_general 99,
  regimen_informativo 53. Páginas del universo: **6.757**
  (`resumen_escalado.md` línea 43).

### B.2 Lo que entró a extracción (los 5 TOs del subset)

Fuente por-documento: `data/experiment/escalado_prep/referencia_subset.json`
(commit `111ed19`); las unidades E0 coinciden con
`reextraccion_v2/corpus_v2/salida/estado_corpus.json` (n por fase).

| TO (id) | Archivo | Páginas | Chunks terminales | Mini-chunks | Unidades de extracción (E0) |
|---|---|---|---|---|---|
| pro | TO_proteccion_usuarios_servicios_financieros_actual.pdf | 40 | 88 | 13 | 101 |
| cla | TO_clasificacion_deudores_actual.pdf | 60 | 127 | 16 | 143 |
| ric | TO_regimen_informativo_contable_mensual_actual.pdf | 59 | 78 | 6 | 84 |
| cap | TO_capitales_minimos_actual.pdf | 204 | 401 | 61 | 462 |
| ext | TO_exterior_cambios_actual.pdf | 201 | 783 | 190 | 973 |
| **Total** | | **564** | **1.477** | **286** | **1.763** |

### B.3 Lo que quedó afuera y por qué (documentado)

- Los **152 TOs** del universo de escalado: sin extraer. Razón documentada:
  el laudo D5 (qué corpus se escala) está PENDIENTE
  (`resumen_escalado.md` §6, línea 362; `docs/plan_tesis.md` B5.5) y el
  escalado tiene prerrequisitos abiertos (§C). Dentro de esos 152, el E0
  seco veredicta **68 digeribles / 84 «necesitan reglas»**, 62 de los
  cuales producen **cero unidades** porque E0 no engancha su estructura
  (`resumen_escalado.md` líneas 67 y 73–74; causa del bloque de régimen
  informativo corregida en `docs/fe_erratas_D10_causa_regimen_informativo.md`:
  compuerta de rol de página de E0, no el regex de sección).
- Comunicaciones A/B, marco legal y versiones tachado/negrita de
  `data/raw/`: fuera del alcance de extracción; no encontré en el repo un
  documento que las declare candidatas a extracción (el universo publicado
  del escalado son los 152 TOs: `resumen_escalado.md` §6).

---

## C. Estado del escalado

Regla de esta sección: solo lo escrito en archivos del repo, clasificado
como HECHO (con commit) / PENDIENTE / NO DOCUMENTADO.

### C.1 Documentos que describen el escalado

- `docs/plan_tesis.md` (commit vigente `c6fae14`, 2026-08-31): bloques
  **ESQ** (validación del esquema, T1 BLOQUEANTE de B5/B6, línea ~312),
  **B5** (endurecimiento y prerrequisitos, issue #6/#11, línea 416) y
  **B6** (corrida por tandas + evaluación final B6.3, línea 428).
- `data/experiment/escalado_prep/resumen_escalado.md` (`111ed19`):
  inventario, E0 seco, veredictos de digeribilidad, proyección de costos,
  laudo D5 pendiente.
- `docs/laudo_D-g_alcance_corpus.md`: el escalado es el objeto central de
  la tesis; los cinco TOs pasan a conjunto de DESARROLLO y el corpus
  escalado es el de TEST (principio 10, plan v8 `966253e`).
- `docs/laudo_ESQ-1_diseno.md` (`94bb7a7`) + pre-registro
  `data/experiment/esq/prerregistro_esq1.md` (`38be6e5`) + adendas P1'
  (`e68e861`) y P1'' (`data/experiment/esq/adenda_prerregistro_esq1_P1ter.md`,
  `6cb0121`) + fe de erratas `7072626`.
- `data/experiment/escalado_prep/scoping_b5_6_tabular_reginf.md` y
  `docs/fe_erratas_D10_causa_regimen_informativo.md` (U-B5.6-0,
  `d13fa15` + `fe1fe36`): scoping del módulo tabular y causa real del cero
  del bloque de régimen informativo.
- `docs/cola_mejoras_diferidas.md` (`d3c6782`): defectos hallados y
  diferidos que B5/ESQ-3 deben absorber antes de escalar.
- `docs/laudo_D-f_secuencia_tripletas.md`: B4 se valida sobre r1 y la
  medición que cuenta corre sobre el grafo escalado (B6.3).
- `data/experiment/escalado_prep/{reporte_generalizacion.md, checkpoint_sesion.md}`:
  corrida E0 en seco sobre los 152 TOs (por-TO, causas del cero) y
  checkpoint de la unidad de prep.
- `docs/backlog_reextraccion.md` (`6cca6c9`): backlog RX del instrumento;
  cabecera «Estado: abierto, en acumulación».
- Nota: el texto de los issues #6 y #11 no está copiado en el repo (solo se
  citan por número en el plan y el tablero).

### C.2 Arreglos previos al escalado

**HECHOS (con commit):**

- Prep de fase A del escalado (`111ed19`, 2026-08-13, USD 0): inventario
  152 TOs congelados por sha256, E0 seco 152/152 con paridad exacta contra
  el subset (1.763/1.763 unidades), 8.010 unidades visibles, veredicto
  68/84, proyección de costos, catálogo de sujetos por proxy léxico.
- Encuadre del escalado como objeto central y de los 5 TOs como conjunto
  de desarrollo: plan v8 + principio 10 (`966253e`), D-g/D-h (`5ff8be7`).
- Carril ESQ instalado como T1 bloqueante (laudo `94bb7a7`, pre-registro
  `38be6e5`, fe de erratas `7072626`).
- U-ESQ-1a instrumento de cadenas distintas (`181e262`, selftest 24/24);
  U-ESQ-1a-bis lectura del bloque crudo (`56c601d`, selftest 52/52);
  U-ESQ-1b canal abierto `tipo_propuesto`/`predicado_propuesto`
  (`8f52f3b`).
- U-ESQ-1c control de instrumento: **P1 FALSADA**, resultado NULO
  (`45e3752`; diagnóstico `d6527a6`). Conteos verificados en
  `data/experiment/esq/control/resumen_control_esq.json`: brazo A 0/20
  (umbral ≥10), B 3/10 (≥7), C 0/10 pasa; USD 0,4223.
- U-ESQ-1d control rediseñado: **P1' FALSADA** (adenda `e68e861`, cierre
  `c25273f`). Verificado en `resumen_control_esq_p1bis.json`: A' 0/10
  (tipo 0/5, predicado 0/5, umbral ≥7 y ≥3/5 por mitad), C 0/10 pasa;
  USD 0,1836. Hallazgo de **deformación semántica** registrado en
  `docs/plan_tesis.md` (bloque ESQ) y en la cola de mejoras diferidas.
- Adenda P1'' sellada (`6cb0121`, 2026-08-31): neutralización de los dos
  cierres del system, una sola variable, cierre de escalera declarado.
- E4 (resolución de variación) y E5 (esqueleto de clases) del pipeline:
  EJECUTADOS en la release r1 (`185e042`; artefactos `e4_*.json`,
  `e5_esqueleto.json` en `salida_r1/`); antes de r1 estaban «definidos y no
  corridos». *(Inconsistencia registrada: la fila M-6 del mapa de
  contribución de `docs/plan_tesis.md` todavía los marca «pendiente».)*
- Backend por defecto del escalado laudado: BM25 / Neo4j full-text (A1.6,
  `docs/laudo_promocion_backend.md`, commit `89055c5`).
- U-B5.6-0 scoping tabular + fe de erratas D10 (`d13fa15`, `fe1fe36`):
  causa del cero del bloque RI identificada (compuerta de rol de página,
  `e0_lib.py:206-207`; 47/53 TOs afectados) y secuencia ESQ-RI-1..4
  fijada. Hallazgo registrado: **el modelo de datos no admite hechos con
  valor** (sin tipo para sujetos de fila informativa; relaciones sin
  `properties` — `prompt_e1.py:232-257`).

**EJECUTADO PERO SIN COMMITEAR (estado del working tree al generar este
inventario):** la corrida del control P1'' (U-ESQ-1e) existe como archivos
sin trackear (`data/experiment/esq/control/*_p1ter.*` + código). Su
resumen (`resumen_control_esq_p1ter.json`, generado 2026-08-31T20:03)
da **A' 0/10 (tipo 0/5, predicado 0/5) — P1'' FALSADA**, C 0/10 pasa,
USD 0,18396; re-presupuesto D7: global USD 6,52 / pareado USD 5,74.
`docs/plan_tesis.md` (commit `c6fae14`) todavía lista U-ESQ-1e como
«POR DESPACHAR»: el plan está un paso detrás del working tree. No existe
`resumen_final_control_esq_p1ter.md` (sí existen los análogos de P1 y
P1'): no hay lectura escrita de O2, y la consecuencia declarada en la
adenda P1'' para el caso «O2 da cero» (canal declarativo inviable;
alternativas: modo (ii) de U-ESQ-0 o protocolizar en ESQ-2) no tiene
todavía laudo commiteado.

**PENDIENTES (todas `[ ]` en `docs/plan_tesis.md`):**

- Corrida ESQ-1 propiamente dicha (tras control aprobado — la escalera de
  controles quedó cerrada sin control aprobado, ver arriba).
- ESQ-2 (cobertura del esquema sobre otros 10 documentos) y ESQ-3 (gate y
  laudo de esquema congelado — «Ningún ítem de B5/B6 arranca sin este
  laudo»).
- ESQ-RI-1..4 (bloque de régimen informativo).
- B5.1 parametrización por manifiesto; B5.2 regex E0 + health-check;
  B5.3 `max_tokens`/sub-chunking; B5.4 catálogo de sujetos v3; **B5.5
  laudo D5 (corpus a escalar — «T1, NO RECORTABLE»)**; B5.6 módulo de
  tablas; B5.7 documento de costos (issue #6).
- B6.1 tanda 1 (20 TOs, ~USD 40); B6.2 tanda 2 (48 TOs, ~USD 85);
  **B6.3 evaluación final de la tesis sobre el grafo escalado** (eval set
  fresco sobre TOs disjuntos, pre-registro propio); B6.4 reporte de
  cierre.
- `data/experiment/esq/documentos_excluidos_esq.json` (registro
  obligatorio de los 10+10 documentos de ESQ-1/ESQ-2): **citado en el
  plan, no existe en el filesystem** (`ls` falla). Bloquea la
  construcción del eval set de B6.3 tal como está escrita.
- Checkboxes de los laudos: los 7 de `docs/laudo_ESQ-1_diseno.md`
  (líneas 132–141) están todos `[ ]` (incluidos «control ejecutado y
  aprobado ANTES de ESQ-1» y «frontera RI a mentores ANTES de laudar
  D5»); de los 4 de `docs/laudo_D-g_alcance_corpus.md` solo el primero
  está `[x]` (sello `5ff8be7`).
- C0.5 (plan): reconciliación de `docs/backlog_reextraccion.md` con el
  pipeline nuevo (RX-01..09 cerrados con evidencia; RX-10 → B5.6) — el
  archivo del backlog RX sigue con cabecera «abierto, en acumulación».
- Entradas 1–7 y 9 de `docs/cola_mejoras_diferidas.md` (destinos
  declarados: B5.1, B5.3, ESQ-3, ESQ-RI-3/C1.7, release r2).

**NO DOCUMENTADO:** el documento de costos de B5.7 / issue #6 no existe
como archivo (solo la fila del plan; el «laudo D4 warm-then-parallel» se
menciona sin archivo propio); no hay pre-registro de B6.3 (solo su diseño
dentro del plan); no hay fecha objetivo de corrida del escalado ni laudo
que resuelva la alternativa post-P1'' — todo queda, por lo escrito, en
laudos futuros de la autora (D5, ESQ-3, y la decisión modo (ii) /
protocolizar).

### C.3 Pruebas previas al escalado documentadas, con resultado

| Prueba | Resultado escrito | Fuente |
|---|---|---|
| E0 seco sobre los 152 TOs | 152/152 corrido; paridad exacta 1.763/1.763 unidades contra el subset sellado | `resumen_escalado.md` (commit `111ed19`) |
| Veredicto de digeribilidad | 68 TOs digeribles / 84 necesitan reglas (62 con cero unidades); RI 0/53 digeribles | `resumen_escalado.md` líneas 67, 73–74 |
| Proyección de costo | E1 56,57 + E3 99,13 = **USD 155,70** sobre 8.010 unidades visibles (banda 130–179); techo ~USD 269 sobre ~13.800 unidades; 68 digeribles solos: 2.009 pág., 6.340 unidades, USD 123,24 | `resumen_escalado.md` líneas 55–56, 73; `proyeccion_costo.json` |
| Control de instrumento ESQ-1 (P1) | FALSADO: A 0/20, B 3/10, C pasa | `esq/control/resumen_control_esq.json`; commits `45e3752`/`d6527a6` |
| Control rediseñado (P1') | FALSADO: A' 0/10, C pasa; las 10 cláusulas plantadas extraídas TODAS forzadas dentro del esquema (deformación semántica) | `esq/control/resumen_control_esq_p1bis.json`; commit `c25273f` |
| Control con cierres neutralizados (P1'') | FALSADO: A' 0/10, C pasa — sin commitear aún | `esq/control/resumen_control_esq_p1ter.json` (untracked) |
| Generalización léxica del catálogo de sujetos | Presión de fusión cross-TO medida por proxy léxico (no adjudicación) | `resumen_escalado.md`; `veredictos_generalizacion.json` |

---

## D. Conjuntos de evaluación

Todos los sets existentes están definidos sobre los 5 TOs del subset (o
sobre nodos/anclas de grafos construidos desde ellos), salvo las dopadas
de ESQ (documentos del universo de escalado). Bajo el principio 10
(`docs/laudo_D-g_alcance_corpus.md`), TODO este material es conjunto de
desarrollo; el eval set de test (B6.3) no existe todavía.

| Set | Archivo(s) | Ítems (re-contados) | Sellado / quemado | TOs |
|---|---|---|---|---|
| CQ v1 (Fase 2.3, corrida congelada) | `data/experiment/evaluacion/queries/eval_set_v1.json` | 23 preguntas | Sellado `7d118ee` (2026-06-09); QUEMADO (`docs/tablero.md` §7) | pro 5, cla 7, cap 4, ext 4, ric 3, 4 sin TO (unanswerable) |
| CQ v2 (unión v1+8) | `queries/eval_set_v2.json` (+ `eval_set_v2_nuevas.json`) | 31 (23+8) | Sellado `7cfe143` (2026-07-06); QUEMADO | los 5 |
| CQN | `queries/eval_set_cqn.json` (+ runtime) | 15 | Sellado `2b8d449` (2026-07-17); QUEMADO | los 5 |
| CQN2 | `queries/eval_set_cqn2.json` (+ runtime) | 15 | Sellado `df29525` (2026-07-19); QUEMADO | los 5 |
| EV1 (escalón 1/1b) | `data/experiment/evaluacion_escalon1/EV1_preguntas.json`, `answer_key_EV1.json`, `EV1_runtime.json` | 36 preguntas | Sellado `d91b832` (2026-07-26); QUEMADO por completo (`docs/lectura_escalon1b.md`, commit `e77b11f`) | los 5 (7–8 c/u) |
| U6 exploración dirigida | `data/experiment/exploracion/generacion/preguntas_u6.json`; criterios `u6_fidelidad/criterios_u6.json`; adjudicación `adjudicacion/u6_adjudicacion_humana.jsonl` | 25 preguntas / 92 criterios / 25 adjudicadas | Set `c3ce221`, criterios `2ac2fab`, adjudicación `b337152`; anclas QUEMADAS (mapa `63cc420`) | ext 10, cap 5, cla 4, ric 3, pro 3 |
| EV2 — fidelidad | `data/experiment/exploracion/ev2_fidelidad/preguntas_ev2_fidelidad.json`; manifest `exploracion/ev2_sellado/manifest_ev2.txt` | 40 preguntas / 164 criterios (recuento: `len(preguntas)`, `sum(len(gold.criterios))`) | Sellado `9c44516` (2026-08-13) ANTES de toda corrida; EV2 CERRADO `64de678`; declarado material de desarrollo quemado (`plan_tesis.md` B6.3) — aún NO volcado al mapa de territorio | dosificación ext 16 / cap 8 / cla 6 / ric 5 / pro 5 |
| EV2 — navegabilidad (queries sintéticas) | `data/experiment/exploracion/sinteticas/out/{samples,preguntas_faseB,calibracion_faseB}.json` | 98 samples → 147 registros → **64 pares aptos** literal/anti-léxica | Commits `a611ed2`/`5ceb816`; sha256 en el manifest de `9c44516` | gold por anclas de provenance de KG-Refinado (sin campo TO) |
| Ablación de retrieval (A1.3/A1.4) | `data/experiment/ablacion_retrieval/pares/pares_v3.json` (+ muestreo y manifest) | 50 pares × 2 variantes | Pre-registro sellado `68c79dc`; corrida `ffc6ff6`; no figura la palabra «quemado» | anclas de provenance (sin campo TO) |
| Bake-off de embeddings (A2.0b) | `data/experiment/bakeoff_embeddings/resultados/casos_gold.json` | 100 casos (50 literal + 50 anti-léxica) | Laudo `df9da34`; sin declaración de sellado del archivo | pasajes de E0 |
| Tests de respuesta conocida (regression del pipeline) | `reextraccion_v2/corpus_v2/salida_r1/tests_respuesta_conocida_r1.json` | 7 tests (T1–T7) | Sellado con r1, `185e042` | los 5 |
| Dopadas ESQ (control de instrumento) | `data/experiment/esq/control/dopadas_p1bis.json` | 10 unidades (5 tipo + 5 predicado) | Adenda `e68e861`, sello `c25273f`; P1'' las reusa idénticas por sha (`6cb0121`) | documentos del universo de escalado, NO los 5 TOs |
| Answer key del piloto de extracción | `grafo_v2/piloto/{muestra_piloto,answer_key}.json` | 18 chunks | Commit `b36d28f`; gold de extracción, no de QA | subset |
| Smoke del banco MCP | `data/experiment/banco_mcp/smoke/preguntas_smoke.json` | 4 preguntas «PROPIAS, nunca EV2» | Commit `1fa79de` | subset |
| Mapa de territorio quemado | `exploracion/mapa_territorio_quemado_5TOs_4sets.json` y `_5sets.json` | 246 unidades censadas; 5 sets: 60 quemadas enteras + 43 parciales, 143 disponibles | `ff0e6ec` (4 sets) y `63cc420` (5 sets) | los 5 |

**Sets que NO existen (verificado):**

- **Tripletas B4** (evaluación intrínseca a nivel tripleta): no hay set.
  `docs/preregistro_evaluacion_tripletas.md` citado en el plan (B4.1) no
  existe en el filesystem. Solo existe el laudo de secuencia
  `docs/laudo_D-f_secuencia_tripletas.md` (firmado 27/08/2026): instrumento
  sobre r1, medición confirmatoria sobre el grafo escalado (B6.3).
  Volúmenes planeados: 100 tripletas de precisión, top-100 de recall.
- **Comparación KG-RAG vs RAG tradicional** (issue #12 / A2.1–A2.2): sin
  set propio; el plan declara que reutiliza «mismo juez de fidelidad EV2,
  mismas 40 preguntas». Pre-registro y corrida sin marcar (`[ ]`).
- **Eval set fresco de B6.3** (el del conjunto de test): no existe; su
  precondición (`documentos_excluidos_esq.json`) tampoco.

---

## E. Números principales ya reportados

Todos re-verificados en esta unidad. «Reproducible hoy: sí» significa que
el número se re-obtuvo parseando el archivo citado con el comando de la
cabecera (o el indicado). `docs/tesis/mapa_fuentes_intro.md` (commit
`5ff8be7`) ya impone esta misma disciplina para la prosa de la intro; esta
tabla lo extiende y re-verifica.

| # | Número | Qué mide | Archivo de origen | Corrida / commit | ¿Reproducible hoy? |
|---|---|---|---|---|---|
| 1 | 4.050/6.634 · 4.469/8.073 · 6.178/11.415 · 6.529/17.772 | Tamaños de KG-Base / KG-Refinado / KG-Reextraído / r1 | los cuatro `kg.json` (§A.1) | `58581b6`/`05984e1`/`5273c0c`/`185e042` | Sí (parseo directo, §A.1) |
| 2 | 27/36 · 29/36 · 31/36 | EV1 1b: correctas de grafo_v2 / KG-Refinado(pre-C) / KG-Base | `evaluacion_escalon1/corridas/resultados_1b_FINALES_2026-07-31.json` (clave `primaria`) | corrida 1b; lectura `e77b11f` | Sí (parseado: 27/29/31) |
| 3 | 3/20/17 · 5/26/9 · 4/27/9 | Fidelidad EV2 definitiva (correcto/parcial/incorrecto sobre 40): KG-Base / KG-Refinado / KG-Reextraído | `ev2_adjudicacion/adjudicacion_SOLO_MESA/cruce_definitivo_por_grafo_SOLO_MESA.json` (`cruce_por_grafo`) | cierre EV2 `64de678` | Sí (parseado) |
| 4 | 6/26/8 | Fidelidad EV2 de KG-Reextraído-r1 (banda de no-señal vs 5/26/9) | `ev2_r1/cierre/reporte_final_r1.md` | U-B1.8, `774acac`; laudo de promoción `81587f9` | Sí (tabla presente en el archivo) |
| 5 | 17 / 25 / 21 (generación, clase modal) y techo de retrieval 14 / 7 / 6 | Atribución causal de fallas EV2 por grafo (base 120 trazas) | `ev2_reporte/salida/atribucion_fallas.md` §1.a | regla `40603a9`, salida `85d9fdb` | Sí (tabla re-leída: 6/11/3/17/3 · 4/6/1/25/4 · 9/1/5/21/4) |
| 6 | 0,716→0,493 (KG-Base) · 0,958→0,620 (KG-Refinado) · 0,396→0,271 (KG-Reextraído) | Recall consultada micro, literal → anti-léxica (navegabilidad EV2; denominadores 60/64/44) | `ev2_corrida/navegabilidad/reporte_navegabilidad.md` §4 | `5b02d22` (+ fix `2c84069`) | Sí (tabla re-leída: 0.7164→0.4925, 0.9577→0.6197, 0.3958→0.2708) |
| 7 | 11/12 y 52/53 (98,1 %) | Validación del juez de fidelidad EV2 contra adjudicación humana (muestra simétrica) | `ev2_adjudicacion/adjudicacion/reporte_muestra_simetrica.md` (línea 6: «acuerdo exacto: 11 / 12»; línea 11: `n_criterios: 53, en_acuerdo: 52, tasa: 0.9811…`) | `64de678` | Sí (líneas re-leídas del archivo) |
| 8 | 172 V / 8 F / 4 P / 16 NV (200 afirmaciones) | Grounded ≠ correct en la corrida congelada (adjudicación firmada 2026-06-10) | `evaluacion/frozen_run/reporte_final.md` (cabecera) | tandas `fb685a7`/`7942ead` | Sí (línea re-leída) |
| 9 | eval_set_v1 23 × 5 grafos × N=3 | Diseño de la corrida congelada Fase 2.3 | `evaluacion/frozen_run/reporte_final.md` línea 3 | `d56020e` | Sí |
| 10 | M7 = 577/4.469 | Nodos con rol `tabla_norma_origen` sobre KG-Refinado (laudo M7) | `grafo_v2/reensamblado_v3/kg.json`, Counter de `rol_fuente` | laudo en `docs/tablero.md` §6 | Sí (recomputado: esqueleto 70, cuerpo 3.811, tabla_norma_origen 577, restauracion_manual 11) |
| 11 | 0.637730 vs 0.600981 (M1) | Inversión P-b de la pasada 1 intrínseca (v3 pre-C vs grafo_v2) | `metricas_intrinsecas/pasada1_resumen.md` §1 | pasada 1, USD 0 | Sí como texto del doc; el estado v3 pre-C ya no existe como grafo (§A.3) |
| 12 | 152 TOs · 6.757 páginas · 8.010 unidades · 68/84 · USD 155,70 (banda 130–179) / techo ~269 / digeribles solos 123,24 | Prep de fase A del escalado | `escalado_prep/resumen_escalado.md` + `proyeccion_costo.json` + `inventario_resumen.json` | `111ed19` | Sí (re-leídos/parseados) |
| 13 | A 0/20, B 3/10, C 0/10 → P1 FALSADA; A' 0/10 → P1' FALSADA; A' 0/10 → P1'' FALSADA | Controles del instrumento ESQ-1 | `esq/control/resumen_control_esq{,_p1bis,_p1ter}.json` | `45e3752`/`c25273f`/(sin commitear) | Sí (parseados los tres) |
| 14 | USD 0,4223 · 0,1836 · 0,18396; re-presupuesto D7 6,52 global / 5,74 pareado (tope laudado 9,00) | Gasto de los tres controles ESQ y re-presupuesto de la corrida ESQ-1 | ídem fila 13 (`cliente.gasto_usd_real`, `re_presupuesto_esq1_D7`) | ídem | Sí |
| 15 | USD 32,97 (de tope 48,50) | Costo de la re-extracción v2 del corpus 5 TOs | `reextraccion_v2/corpus_v2/salida/estado_corpus.json` (suma de `gasto_usd` de `fases_cerradas` = 32,9659) | `5273c0c` | Sí (recomputado) |
| 16 | USD 35,62 | Costo total del período EV2 | `ev2_reporte/reporte_ev2.md` §9 («Total EV2») | `40603a9` | Sí (línea re-leída) |
| 17 | 0,887→0,981 (recall consultada literal, booleano→BM25); brecha anti-léxica NO se cierra; de 20 fallas: 7 búsqueda / 13 selección | Ablación de retrieval A1.4 (celdas C00→C10/C11) | `ablacion_retrieval/corrida/resultados/analisis_ablacion.json` (`tabla_central`, `predicciones`); lectura en `plan_tesis.md` C0.3 | `ffc6ff6` | Sí (parseado: 0.8868→0.9811) |
| 18 | BM25 72 %/16 % vs harrier 52 %/36 % (literal@1 / anti-léxica@1) | Bake-off de embeddings A2.0b, regla principal R2 | `bakeoff_embeddings/bakeoff_embeddings.md` §3 | `df9da34` | Sí (tabla re-leída) |
| 19 | 5.680 aristas `referencia` (totales) / 5.645 nuevas con evidencia | Referencias norma→norma de r1 (E4) | `salida_r1/kg.json` (parseo) / `salida_r1/reporte_ensamblado_r1.json` (`referencias.aristas_referencia_nuevas`) | `185e042` | Sí (ambos parseados). Los dos 5.645 cuentan el MISMO conjunto: las 5.645 aristas `referencia` de r1 con `rol_fuente: "referencia_cruzada"` son exactamente las `aristas_referencia_nuevas` del reporte, y no se solapan con las selladas (intersección 0 por pares source/target). Las 35 restantes sin `rol_fuente` son las 34 `referencia` del grafo sellado (`salida/kg.json`, contenidas 34/34) más 1 nueva sin marca (`TextoOrdenado_to_exterior_cambios_actual_pdf` → `Comunicacion_a_7348`), consistente con el `delta: 5.646` de `diff_vs_sellado` |
| 20 | 31/40 anclas presentes en r1 | Censo de anclas de fidelidad EV2 sobre r1 (umbral P1 «≥31/40»: dentro) | `ev2_r1/censo/censo_anclas_fidelidad_r1.json` (`propuesta_umbral_p1.observado`) | `6c5507b` | Sí (parseado) |
| 21 | 1.683/1.763 unidades aceptadas (80 en cola humana) | Aceptación de la extracción E0–E3 del corpus 5 TOs | `salida/estado_corpus.json`: Counter sobre los `estados` de las fases e3 más los `desenlaces` de `reextraccion_dirigida` → completo_ok_directo 816 + aceptado_tras_reintento 330 + aceptado_con_residuales 537 = **1.683**; cola_humana 76 + veredicto_inutilizable 3 + reextraccion_invalida 1 = **80**; total 1.763 | `5273c0c` | Sí (recomputado; coincide con el mensaje del commit) |
| 22 | 4.458/8.044 | Tamaño de KG-Refinado PRE-C1–C7 (lo que midió la pasada 1) | `metricas_intrinsecas/pasada1_resumen.md` línea 9 | pasada 1 | **No reproducible desde grafo** (§A.3); sí como cita del doc |

---

## F. Glosario de variantes

Conceptos con más de un nombre en los documentos del repo. NO se elige acá
cuál es la forma correcta; para los grafos ya existe canonización por laudo
(`docs/nomenclatura_grafos.md`, commit `237fb8f`). Dos archivos funcionan
como registro de alias: `docs/nomenclatura_grafos.md` (§1 columna de alias,
§4 regla de uso) y `docs/ARQUITECTURA.md` §5 (inconsistencias detectadas).

1. **KG-Reextraído-r1 (vigente, sha `0226e947`)** — variantes: `KG-Reextraído-r1` (nomenclatura_grafos.md, tablero.md, laudo_promocion_r1_vigente.md); `r1` / «grafo r1» / «release r1» (plan_tesis.md, ev2_r1/README.md); `salida_r1` (nomenclatura_grafos.md, neo4j/plan_carga_r1.md); `r1_vigente` (app/main.py, app/README.md); `KG_Reextraido_r1` (label Neo4j; neo4j/README.md); `r1_vista_runtime` (adapter, tablero.md §1); «grafo vigente» a secas (referente móvil: CLAUDE.md §6 aún dice «reensamblado_v3, vigente»; tablero.md §1 ya dice r1).
2. **KG-Base (sha `12c226e2`)** — `KG-Base` (nomenclatura_grafos.md, reporte_ev2.md); `run_3` (skills, hallazgos_tesis.md, frozen_run/reporte_final.md); `run_3_ppf_core` (README.md, ARQUITECTURA.md); `run3` (labels de dbs EV2, reporte_navegabilidad.md); «baseline» / «baseline congelado» (spec_backlog_refinamiento.md, skill kg-refinement); «PPF-core» / «ganador de la Fase 2.3» (nomenclatura_grafos.md, INDICE.md).
3. **KG-Refinado (sha `26fac8b4`)** — `KG-Refinado` (nomenclatura_grafos.md, tablero.md); `v3` (backlog_reextraccion.md, protocolo_escalon1b.md); `reensamblado_v3` (CLAUDE.md, informes de grafo_v2); «re-ensamblado v3» (diseno_reextraccion_v2.md); `v3_vigente` (app/README.md, protocolo_corrida_ev2.md); `ev2_base_v3` (label de db, reporte_ev2.md); `:KG_Refinado` (Neo4j, tablero.md §1); «ex-vigente» (tablero.md §1.b).
4. **KG-Reextraído (sha `8e2eadee`)** — `KG-Reextraído` (nomenclatura_grafos.md, regla_atribucion.md); `v2` (reporte_navegabilidad.md, reporte_ev2.md); `corpus_v2` (laudo_promocion_r1_vigente.md, scoping_esq1.md); «grafo v2 FINAL» (tablero.md, mensaje de `5273c0c`); «v2-reextraído» (diseno_ev2.md); `ev2_base_v2` (label de db).
5. **grafo_v2 del escalón 1 (sha `2c7487bb`) — colisión del alias «v2»** — forma prescrita «grafo_v2 (medición sellada del escalón 1, sha 2c7487bb)» (nomenclatura_grafos.md §4, tablero.md §1.b); `grafo_v2` como directorio ambiguo (CLAUDE.md §3, protocolo_escalon1b.md); «v2» histórico con este referente (pasada1_resumen.md, mapeo_delta_v2v3.md). Tercer sentido de «v2»: el **esquema** v2 (esquema_v2_diseño.md, spec_extraccion_v2.md).
6. **Juez vs verificador (y «Motor 3»)** — CLAUDE.md §1 los separa: el juez evalúa contra clave; el verificador atribuye causas. Variantes del juez de la evaluación KG-RAG: «juez» a secas, «juez v2.1.1» / «juez Sonnet de dos pasos», «juez congelado», `judge.py` (cuarteto hasheado), «LLM-as-judge». Juez de fidelidad EV2 (OTRO juez, numeración propia): «juez de fidelidad», «juez v1» (prompt sha `fd446f8e…`), «prompt v1.1» (descartado). Verificador: «verificador», «verificador v5.7» / «taxonomía v5.7», «verificador agéntico v4», «Motor 3» (verificador como diagnóstico automático + laudo humano; lectura_gate_u5.md, resultado_piloto_singold_u6.md), «validado-en-familia v2/v3». Además existe «E3 / verificador de la re-extracción» (otro verificador, del pipeline E0–E5). «Motor 2» nombra al circuito de intake de feedback.
7. **EV2 / evaluación de fidelidad** — `EV2` (diseno_ev2.md, tablero.md); «set sellado de medición de la re-extracción (issue #4)» (título de diseno_ev2.md); «evaluación de fidelidad» (preregistro_evaluacion_fidelidad_ev2.md); «eje de fidelidad» vs «eje sintético» (diseno_ev2.md §4–5); «preguntas de generación ciega solo-PDFs» / «corrida ciega» / «reporte ciego» (protocolo_corrida_ev2.md, ev2_fidelidad_eval/out/).
8. **EV1 / escalón 1 / escalón 1b** — `EV1` (CLAUDE.md §3, acta_adjudicacion_EV1.md); «escalón 1» (protocolo_escalon1.md); «escalón 1b» / `1b` (lectura_escalon1b.md, protocolo_escalon1b.md); «material QUEMADO» (CLAUDE.md §3, tablero.md §7). INDICE.md equipara «escalón 1b (EV1, 36 preguntas)».
9. **Refinamiento / Fase 2.5 / Fase 2.4** — «Fase 2.5» = refinamiento (skill kg-refinement, ARQUITECTURA.md); «Fase 2.4» = verificador (ARQUITECTURA.md, hallazgos_tesis.md); la skill registra que docs previos llamaban «2.4» al refinamiento por error; ARQUITECTURA.md §5.1 afirma que no queda ningún archivo con la numeración vieja. «Fase 2.3» / «corrida congelada» / «frozen» / `frozen_run` nombran la misma evaluación (skill frozen-eval-audit).
10. **Unidades de extracción / chunks / bloques estructurales** — «unidad de extracción» (enmienda_01, nomenclatura_grafos.md §3.a); «chunk» (spec_extraccion_v2.md, decisiones_caching_extraccion.md); «bloques estructurales» (chapeau_seccion, encabezado, intro, intersticial, cierre — enmienda_01); «mini-chunk» (INFORME_E0.md, scoping_esq1.md); «unidades E0» / «1.763 unidades E0» (nomenclatura_grafos.md §3.a); «chunker v1» vs «E0» (diseno_reextraccion_v2.md).
11. **Eval set / queries / CQ** — «eval set» (CLAUDE.md §3); `eval_set_v1/v2` (ARQUITECTURA.md §4); «queries» (directorio); «CQ/CQs» (casos_gate_cqn.md, frozen_run); «preguntas de competencia» / «competency questions» (spec_evaluacion_intrinseca.md, literatura); «CQN/CQN2» (casos_gate_cqn{,2}.md); «queries sintéticas» / «eje sintético» (diseno_queries_sinteticas.md, reporte_navegabilidad.md).
12. **Pipeline / generaciones** — «Gen. 1/2/3» (nomenclatura_grafos.md §1, tablero.md §1.b); «pipeline E0–E5» / «E0–E3» (laudo_promocion_r1_vigente.md); «re-extracción v2» (diseno_reextraccion_v2.md); «linaje viejo» / «trío de run_3» / «extracción esquema v2» (nomenclatura_grafos.md §2); «Enmienda 01» (enmienda_01_diseno_reextraccion_v2.md).
13. **Trazas / traces** — colisión castellano-inglés registrada como inconsistencia abierta en ARQUITECTURA.md §5.9: `evaluacion/trazas/` vs `frozen_run/traces/` y `posthoc_run/traces/`; «trazas juzgadas» (skill eval-pipeline); «crudos» / «raw» / «captura de crudos» (skill llm-capture).
14. **Backlogs (tres cosas distintas con nombre parecido)** — «backlog unificado de refinamiento» / `backlog.jsonl` / «backlog de nodos» (spec_backlog_refinamiento.md, tablero.md §3); «backlog RX» (defectos del instrumento, backlog_reextraccion.md); las colas: «cola de intake» (intake de la app), «cola humana» (E3), «cola de mejoras diferidas» (docs/cola_mejoras_diferidas.md).
15. **Tablero / estado** — «tablero» / «Tablero de estado» (docs/tablero.md); «estado vigente y cola de unidades» (CLAUDE.md §2); definición alternativa «el estado real es git log + backlog.jsonl» (tablero.md líneas 3–5); `checkpoint_sesion.md` como estado por corrida (ev2_juez/, escalado_prep/).
16. **Vara / gold / clave / ground truth** — «vara» / «vara sellada» / «vara v3» (protocolo_gate_u5.md, evidencia_vara_v3/); «gold» / «gold por anclas» (diseno_ev2.md §5); «clave» (CLAUDE.md §1); «ground truth» (ARQUITECTURA.md §4); «criterios» / «164 criterios» (plan_tesis.md, INDICE.md); «sin-gold» (resultado_piloto_singold_u6.md).
17. **Agente / harness / tools** — «agente Haiku» / «agente RAG» (CLAUDE.md §1, README.md); «harness» (cuarteto hasheado, CLAUDE.md §3); «tools v1» / «tools v2» / `GraphAgentV2` (agente_v2/README.md, plan_tesis.md); «app» / «app web de chat» (CLAUDE.md §6); «capa determinística» / «capa D» (especificacion_capa_deterministica.md).

Observaciones (sin adjudicar): los conceptos 1–5 ya tienen canonización por
laudo; 6 (juez/verificador/Motor 3) y 16 (vara/gold/clave) NO tienen
documento canónico de nombres; 13 (trazas/traces) está registrado como
inconsistencia abierta; en 9, la skill y ARQUITECTURA.md §5.1 no dicen lo
mismo con el mismo alcance.

## G. Verificaciones para la Introducción

Unidad de solo lectura (2026-09-01). Cinco datos puntuales verificados contra
el repo; cada uno con ruta, comando o línea, y resultado. Ninguna decisión.

### G.1 Tipos de entidad del esquema — Sujeto NO está en la lista

- La constante análoga a `PREDICATES` es `ENTITY_TYPES`, que
  `data/experiment/reextraccion_v2/e1_extractor/prompt_e1.py` importa (líneas
  32–39, `from schema import ENTITY_TYPES, PREDICATES, ...`) desde su fuente
  única `data/experiment/grafo_v2/code/schema.py` (el path lo inserta
  `comun_e1.py`, líneas 7 y 27–30).
- Definición: `data/experiment/grafo_v2/code/schema.py` líneas 24–31 —
  `ENTITY_TYPES = ("Comunicacion", "TextoOrdenado", "Operacion",
  "Restriccion", "Excepcion", "Obligacion")`. **Conteo: 6.**
- En el prompt, la sección que los enumera es «# TIPOS DE ENTIDAD VÁLIDOS
  (exactamente 6, ningún otro)» (`prompt_e1.py` línea 57; enumeración en
  líneas 61–77).
- **Sujeto NO figura en la lista.** El propio prompt lo excluye dos veces:
  línea 59 («Los SUJETOS … NO son un tipo de entidad: NO crees entidades
  para ellos. El sujeto se elige de un CATÁLOGO CERRADO dentro de las
  relaciones aplica_a/ejecuta») y línea 172 («❌ Entidad de tipo
  "EntidadFinanciera" o "Sujeto" → los sujetos NO son entidades del chunk:
  van en sujeto_id/sujeto_propuesto de aplica_a/ejecuta»).
- Vías de entrada de los nodos `type: "Sujeto"` al grafo:
  1. Ensamblado desde el catálogo: `data/experiment/reextraccion_v2/e2_reduce/e2_lib.py`
     líneas 344–356, función `nodo_sujeto(sujeto_id, prov)` — materializa el
     nodo `{"id": sujeto_id, "type": "Sujeto", ...}` a partir del `sujeto_id`
     de las relaciones `aplica_a`/`ejecuta` contra `labels_cat` (catálogo).
  2. Esqueleto E5: `data/experiment/reextraccion_v2/corpus_v2/r1_e5_esqueleto.py`
     línea 67 — crea `{"id": sid, "type": "Sujeto", ..., "rol_fuente":
     "esqueleto"}` para las entradas del catálogo ausentes del grafo (vía
     `build_skeleton()` importado de `grafo_v2/code/assemble.py`).

### G.2 Clases de la atribución causal

- Cabecera de la tabla 1.a de
  `data/experiment/ev2_reporte/salida/atribucion_fallas.md` (líneas 11–14):
  `| grafo | ausencia_kg | alcanzabilidad | vista_no_consultada | generacion | correcto (no atribuible) | n |`
- Documento de la regla (commit `40603a9`):
  `data/experiment/ev2_reporte/regla_atribucion.md`. Definiciones textuales
  (§4, líneas 150–155, tabla «orden | clase | condición operativa»):
  - **ausencia_kg** (orden 1): «`ancla_presente == false` (el ancla no
    resuelve a ningún nodo en ese grafo bajo la regla del censo). … al grafo
    le falta el contenido; nada que el agente haga cambia la clase.»
  - **generacion** (orden 2): «`ancla_presente && ancla_consultada`: el
    agente tuvo el contenido del ancla (ver_nodo) o llegó a él por vecindad,
    y la respuesta igual salió parcial/incorrecta.»
  - **vista_no_consultada** (orden 3): «`ancla_presente && !ancla_consultada
    && ancla_vista`: un nodo-ancla apareció en resultados de `buscar_nodos` y
    el agente no lo abrió ni lo alcanzó».
  - **alcanzabilidad** (orden 4): «`ancla_presente && !ancla_vista &&
    !ancla_consultada`: el ancla está en el grafo pero ningún nodo-ancla
    apareció jamás en un `buscar_nodos` ni fue alcanzado por navegación.»
  - «correcto (no atribuible)» no es clase: «Los veredictos `correcto` NO se
    atribuyen: la traza queda con `clase = null` y se reporta en el
    denominador (columna "correcto (no atribuible)" de toda tabla)»
    (regla_atribucion.md, líneas 50–52).
- Confirmación de la fila 5 de la tabla E (este documento, §E): los tres
  quintetos corresponden, en el orden de la cabecera, a
  ausencia_kg / alcanzabilidad / vista_no_consultada / generacion /
  correcto (no atribuible): KG-Base 6/11/3/17/3 · KG-Refinado 4/6/1/25/4 ·
  KG-Reextraído 9/1/5/21/4 (tabla 1.a, filas de datos, líneas 15–17).

### G.3 Cobertura de procedencia en el grafo de desarrollo (salida_r1)

- Archivo: `data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json`
  (6.529 nodos / 17.772 aristas). Comando (parseo Python sobre
  `provenances`/`provenance`; «unidad de extracción» = campo `chunk_id`):
  con procedencia completa = algún provenance con `punto`, `chunk_id` y
  `paginas` no vacíos; esqueleto = algún provenance con
  `rol_documental == "esqueleto"`.
- Resultado: **nodos 6.510/6.529** con punto+unidad+páginas; **70** con
  provenance de esqueleto (de los cuales **19** SOLO esqueleto, sin
  procedencia completa); **0** sin ninguna de las dos.
  **Aristas 17.690/17.772** con punto+unidad+páginas; **82** de esqueleto
  (las mismas 82 sin procedencia completa); **0** sin ninguna. Es decir:
  6.510 + 19 = 6.529 y 17.690 + 82 = 17.772 — partición exacta.
- Comparación pedida contra `docs/tesis/mapa_fuentes_intro.md` fila 6: los
  conteos recomputados COINCIDEN con los valores citados en el mandato de
  esta unidad (6.510/6.529 nodos, 17.690/17.772 aristas, 19 nodos y 82
  aristas de esqueleto). PERO la fila 6 del mapa NO registra esa apertura:
  su texto (línea 23) solo registra los tamaños totales «KG-Reextraído-r1
  6.529/17.772 (16)». Los valores 6.510/17.690/19/82 no aparecen en ninguna
  fila del mapa (grep de `6.510|17.690` sobre docs/ da vacío). Si la prosa
  de la Introducción va a usar la apertura de cobertura, necesita fila
  propia en el mapa de fuentes (regla del propio mapa, líneas 3–5).

### G.4 Textos Ordenados: 161 contra 158

- 161 = `ls data/raw/01_textos_ordenados/actuales/ | wc -l` → 161 PDFs,
  todos con fila en `data/raw/manifiesto.csv` (join por `archivo_local`).
- 158 = `entradas_indice` de
  `data/experiment/escalado_prep/inventario_resumen.json`; el detalle por
  entrada está en `data/experiment/escalado_prep/indice_oficial_raw.json`
  (103 `textos_ordenados` + 55 `regimenes_informativos` = 158, con 157 URLs
  únicas: `t-optico.pdf` figura DOS veces con el mismo título
  «Presentación de informaciones al BCRA» — duplicado registrado en
  `inventario_resumen.json.duplicados_descartados`).
- Diff (join por nombre de archivo de la URL, manifiesto ↔ índice):
  - Índice → local: las 157 URLs únicas del índice tienen su PDF en
    `actuales/` (conjunto «en índice y no en actuales» = vacío).
  - Local → índice: 4 archivos cuya URL de origen NO está en el índice
    oficial del momento del relevamiento:
    1. `TO_fraccionamiento_riesgo_crediticio_actual.pdf` ← `t-fdrc.pdf`
       (manifiesto: «FRACCIONAMIENTO DEL RIESGO CREDITICIO»,
       fecha_documento 2018-09-05).
    2. `TO_regimen_informativo_contable_operaciones_cambios_actual.pdf` ←
       `t-ri-coc.pdf` (manifiesto: «RÉGIMEN INFORMATIVO CONTABLE MENSUAL -
       OPERACIONES DE CAMBIOS»).
    3. `TO_regimen_informativo_pld_ft_actual.pdf` ← `t-ri-pl.pdf`
       (manifiesto: «REGIMEN INFORMATIVO CONTABLE MENSUAL»).
    4. `TO_regimen_informativo_niif_plan_cuentas_actual.pdf` ←
       `RI-planNIIF.pdf` (manifiesto: «CAPITULO – DEFINICIONES GENERALES»,
       fecha_documento 2019-12-31).
- Aritmética: 161 archivos locales = 157 URLs únicas del índice + 4 no
  indexadas; 158 entradas del índice = 157 únicas + 1 duplicada. La
  diferencia 161−158=3 es el neto de (+4 locales fuera del índice, −1
  duplicado del índice). Qué SON los 4 según el repo: PDFs descargados en
  2026-05 (manifiesto) cuyas URLs ya no aparecen en el índice oficial
  relevado por escalado_prep; el repo no registra la causa de su salida del
  índice (no determinable desde el repo — no se adjudica acá).

### G.5 Bibliografía (`docs/tesis/bibliografia.bib`, working tree)

Claves existentes (`grep -c '^@' docs/tesis/bibliografia.bib` = 11; dos
entradas con año en TODO):

| clave | título | año |
|---|---|---|
| `agarwal2025ragulating` | RAGulating Compliance: A Multi-Agent Knowledge Graph for Regulatory QA | 2025 |
| `khetan2021kganchored` | Knowledge Graph Anchored Information Extraction for Domain-Specific Insights | 2021 |
| `carta2023iterative` | Iterative Zero-Shot LLM Prompting for Knowledge Graph Construction | 2023 |
| `li_legal_kg_mdpi` | Construction of Legal Knowledge Graph Based on Knowledge-Enhanced Large Language Models | (vacío, TODO) |
| `legalkg_vaw_2025` | Automated Creation of the Legal Knowledge Graph Addressing Legislation on Violence Against Women… | 2025 |
| `meher_corekg` | CORE-KG: An LLM-Driven Knowledge Graph Construction Framework for Human Smuggling Networks | (vacío, TODO) |
| `meher2025linkkg` | LINK-KG: LLM-Driven Coreference-Resolved Knowledge Graphs for Human Smuggling Networks | 2025 |
| `graphs_agents_survey2025` | Graphs Meet AI Agents: Taxonomy, Progress, and Future Opportunities | 2025 |
| `lu2026karma` | KARMA: Leveraging Multi-Agent LLMs for Automated Knowledge Graph Enrichment | 2026 |
| `suchanek2007yago` | YAGO: A Core of Semantic Knowledge Unifying WordNet and Wikipedia (WWW) | 2007 |
| `mahdisoltani2015yago3` | YAGO3: A Knowledge Base from Multilingual Wikipedias (CIDR) | 2015 |

Las cinco consultas:
1. Lewis et al. (Retrieval-Augmented Generation, 2020): **AUSENTE**.
2. «RAGulating Compliance»: **PRESENTE** — clave `agarwal2025ragulating`.
3. Khetan et al. sobre el Federal Register: **PRESENTE** una entrada de
   Khetan et al. — clave `khetan2021kganchored` (2021, «Knowledge Graph
   Anchored Information Extraction for Domain-Specific Insights»); el .bib
   no menciona «Federal Register», de modo que la equivalencia con «el
   paper del Federal Register» no es determinable desde el repo.
4. Suchanek, Kasneci y Weikum (YAGO, WWW 2007): **PRESENTE** — clave
   `suchanek2007yago`.
5. Hoffart et al. (YAGO2, Artificial Intelligence 2013): **AUSENTE** (la
   entrada YAGO adicional es `mahdisoltani2015yago3`, YAGO3/CIDR 2015 —
   otro paper).

No se agregó ninguna entrada al .bib.

## H. El agente y el acceso al grafo

Unidad de solo lectura (2026-09-01). Cuatro puntos con evidencia pegada;
ninguna decisión sobre cuál de las dos configuraciones debe describir la
tesis.

### H.1 El agente de la evaluación EV2 (el que produjo la fidelidad de la fila 3 y la atribución de la fila 5)

Las 120 trazas base de EV2 (3 grafos × 40 preguntas; filas 3 y 5 de §E) las
produjo `data/experiment/ev2_corrida/code/runner_ev2.py` (commit `bb89a8e`),
que instancia `FullCaptureAgent(GraphAgent)` (líneas 64–84 y 143: subclase de
captura que NO altera el comportamiento — `_run_tool` delega en `super()` y
solo anota el output íntegro). `GraphAgent` es el agente del cuarteto
congelado `data/experiment/evaluacion/harness.py` (commit `7e8b91e`). La
medición de r1 (fila 4, sello `774acac`) reutiliza el mismo runner y el mismo
harness vía `data/experiment/ev2_r1/code/comun_r1.py` (registra el grafo "r1"
en memoria y replica la vista runtime con las dataclasses del loader
congelado, líneas 9–21).

**Modelo y parámetros** (`harness.py` líneas 47–50):

```
MODEL = "claude-haiku-4-5-20251001"   # FIJO para los 5 grafos
TEMPERATURE = 0
MAX_TOKENS = 2048
MAX_TOOL_CALLS = 15
```

El runner persiste estos valores en la meta de cada traza
(`runner_ev2.py:170-173`: `"model": harness.MODEL`, etc.).

**Prompt del agente**: es la constante `SYSTEM_PROMPT` de `harness.py`
(líneas 61–92), embebida en el archivo — no hay archivo de prompt separado.
Su sello es el sha256 del harness completo, que integra el cuarteto hasheado
(CLAUDE.md §3). Verificación de esta unidad:
`shasum -a 256 data/experiment/evaluacion/harness.py` →
`fd267e833866f86850e43130e627b08d78e05523b97484696de0ab0c8c9fba9e`, cuyo
prefijo coincide con el sellado en `docs/protocolo_escalon1b.md:20-21`
(«`harness.py fd267e833866`»). Texto del prompt (verbatim, `harness.py:61-92`):

```
Sos un asistente que responde preguntas sobre regulación del BCRA usando \
EXCLUSIVAMENTE un Knowledge Graph, al que accedés mediante tres tools. No tenés \
otro conocimiento disponible: si algo no está en el grafo, no lo sabés.

Tools disponibles:
- buscar_nodos(consulta, limite): búsqueda léxica de nodos por label/id. Empezá \
siempre por acá para encontrar puntos de entrada.
- ver_nodo(id): devuelve type, label, properties y provenances de un nodo.
- ver_vecinos(id, direccion): devuelve los edges (relaciones) entrantes/salientes \
de un nodo, con el vecino y las provenances del edge.

Estrategia: buscá nodos relevantes, abrí los que parezcan pertinentes con \
ver_nodo, y explorá relaciones con ver_vecinos hasta tener evidencia suficiente. \
Tenés un máximo de 15 tool calls por pregunta: usalas con criterio.

REGLAS DURAS:
1. Solo afirmá lo que esté respaldado por lo que devolvieron las tools. No \
inventes obligaciones, plazos, montos ni entidades que no viste en el grafo.
2. Si la información necesaria no está en el grafo, respondé con \
"respondible": false y explicá brevemente en "respuesta" qué falta. No inventes.
3. Las citas deben salir de las provenances que viste en ver_nodo / ver_vecinos \
(campos source_doc y location). No cites provenances que no observaste.

FORMATO DE SALIDA: cuando tengas la respuesta final, respondé con UN ÚNICO objeto \
JSON válido, sin texto adicional ni markdown, con exactamente estas claves:
{
  "respuesta": "<texto de la respuesta en español>",
  "citas": [{"source_doc": "<archivo>", "location": "<ubicación>"}, ...],
  "respondible": true|false
}
Si "respondible" es false, "citas" puede ser una lista vacía.
```

**Schema de tools tal como lo ve el modelo** (constante `TOOLS`,
`harness.py:240-286`, verbatim; es lo que viaja en el parámetro `tools` de
cada request — `harness.py:479`):

```python
TOOLS = [
    {
        "name": "buscar_nodos",
        "description": ("Búsqueda léxica de nodos del grafo por coincidencia de "
                        "palabras en su label o id (normalizada, sin acentos). "
                        "Devuelve id, type, label y un resumen corto de "
                        "propiedades. Es el punto de entrada habitual."),
        "input_schema": {
            "type": "object",
            "properties": {
                "consulta": {"type": "string",
                             "description": "Palabras clave a buscar."},
                "limite": {"type": "integer",
                           "description": "Máximo de resultados (def. 10)."},
            },
            "required": ["consulta"],
        },
    },
    {
        "name": "ver_nodo",
        "description": ("Devuelve un nodo completo por su id exacto: type, label, "
                        "properties y provenances (source_doc + location)."),
        "input_schema": {
            "type": "object",
            "properties": {
                "id": {"type": "string", "description": "id exacto del nodo."},
            },
            "required": ["id"],
        },
    },
    {
        "name": "ver_vecinos",
        "description": ("Devuelve las relaciones (edges) de un nodo: relation, "
                        "vecino y provenances del edge. 'direccion' puede ser "
                        "'salientes', 'entrantes' o 'ambas'."),
        "input_schema": {
            "type": "object",
            "properties": {
                "id": {"type": "string", "description": "id exacto del nodo."},
                "direccion": {"type": "string",
                              "enum": ["ambas", "salientes", "entrantes"],
                              "description": "Dirección de los edges (def. ambas)."},
            },
            "required": ["id"],
        },
    },
]
```

**Estructura sobre la que corren las tools**: índice EN MEMORIA sobre el
`KnowledgeGraph` del loader congelado — clase `GraphIndex`
(`harness.py:130-146`): dict `by_id`, un set de tokens por nodo
(`label` + `id`) y listas de adyacencia `out_edges`/`in_edges` construidas
recorriendo `kg.edges`. No hay base de datos: en EV2 cada grafo se cargó con
su vista runtime (`comun_ev2.py:179-186` — `loader.load_graph("run_3")` para
KG-Base, `load_graph_from_path` para KG-Refinado, adaptador en memoria para
KG-Reextraído; los tres verificados por sha256 antes de correr,
`comun_ev2.py:116-128`).

**Búsqueda por texto: léxica exacta por tokens, sin BM25 y sin embeddings.**
El propio docstring lo declara («Sin embeddings (decisión explícita
revisable)», `harness.py:13`). Normalización: lowercase + sin acentos +
tokenización `[a-z0-9]+` (`harness.py:98-107`). La línea del score
(`harness.py:154-157`):

```python
        for n in self.kg.nodes:
            score = len(q & self._node_tokens[n.id])
            if score:
                scored.append((score, len(n.label or ""), n))
        scored.sort(key=lambda t: (-t[0], t[1], t[2].id))
```

— es decir, ranking por número de tokens de la consulta presentes en
label/id, desempate por label más corto y luego id.

**Límites**: 15 tool calls por pregunta (`MAX_TOOL_CALLS`, `harness.py:50`;
al alcanzarlo se fuerza la respuesta final con `tool_choice: none`,
`harness.py:527-536` y 481–484); `buscar_nodos` devuelve `limite` resultados,
default 10, recortado a 1..50 (`harness.py:158-160`); `ver_vecinos` trunca a
40 vecinos por dirección con flag `*_truncado` (`limite: int = 40`,
`harness.py:197`, 231–235); respuesta final `MAX_TOKENS = 2048`
(`harness.py:49`). No hay límite de "pasos" separado del de tool calls: el
loop corre hasta `stop_reason != "tool_use"` (`harness.py:474-537`).

### H.2 El runtime actual (app, vista `r1_vista_runtime`, carga en Neo4j)

- **Backend**: Neo4j Community con índice full-text Lucene (BM25). El agente
  de la app es `_ChatAgentNeo4j(_ToolLogMixin, GraphAgentNeo4j)`
  (`app/main.py:337-343`) construido con
  `Neo4jIndex(NEO4J_DRIVER, grafo="KG_Reextraido_r1", modo="fulltext")`
  (`app/main.py:352-356`, `NEO4J_GRAFOS` en 242–245). `GraphAgentNeo4j`
  (`data/experiment/neo4j/agente_neo4j.py:56-65`, commit `9e131bf`) es
  subclase del `GraphAgent` del harness que reemplaza `self.index` por el
  `Neo4jIndex` «sin tocar `ask` ni el resto del loop (prompt del sistema,
  TOOLS, MODEL, límite de tool calls, truncado de trazas, colección de
  provenances vistas: todo idéntico)» (docstring, `agente_neo4j.py:8-12`).
  La búsqueda ejecuta en el servidor
  (`neo4j_index.py:176-186`):

  ```python
            rec = session.run(
                f"CALL db.index.fulltext.queryNodes('{self.indice}', $q) "
                "YIELD node, score "
                "WITH node, score "
                "ORDER BY score DESC, size(node.label) ASC, node.id ASC "
  ```

  El grafo vigente está cargado bajo el label `:KG_Reextraido_r1` con índice
  `nodos_fulltext_kg_reextraido_r1` (docs/tablero.md §1, líneas 46–51;
  paridad de carga 454/454 en
  `data/experiment/neo4j/test_equivalencia_resultados_UMIGr1.json`). Si el
  driver no abre, la app degrada declaradamente a `GraphIndex` in-memory
  sobre la vista `r1_vista_runtime` (`app/main.py:223-236` y 346–361; el
  adapter despacha a `grafos.cargar_vista_runtime`, que es la vista in-memory
  del registro `data/experiment/neo4j/grafos.py:79`, precedente U-B1.8).
- **Herramientas**: las mismas 3 tools con firma v1 (`buscar_nodos`,
  `ver_nodo`, `ver_vecinos(id, direccion)`) — las tools v2 NO fueron
  promovidas (`docs/laudo_promocion_backend.md` §2.2). `Neo4jIndex` replica
  los límites del harness: recorte de `limite` a 1..50
  (`neo4j_index.py:113-116`) y paridad byte-idéntica 322/322 de
  `ver_nodo`/`ver_vecinos` contra el índice in-memory (laudo §1).
- **Prompt**: el MISMO `SYSTEM_PROMPT` de H.1 — la subclase no lo toca
  (`agente_neo4j.py:8-12`); el modelo también es `harness.MODEL` salvo backend
  Bedrock, donde un `ModelOverrideClient` reescribe el model id
  (`app/llm_backend.py:1-33`).
- **Laudo que lo estableció**: `docs/laudo_promocion_backend.md` (A1.6,
  commit `89055c5`), decisión §2.1 («BM25 (Neo4j full-text, modo `fulltext`
  de `Neo4jIndex`) pasa a ser el retriever por defecto de la app y del
  escalado») y alcance §3 («el agente de la app pasa a `GraphAgentNeo4j` con
  `modo='fulltext'` como default, manteniendo el `GraphIndex` in-memory como
  fallback declarado»).
- **¿Alguna corrida de evaluación con número reportado se hizo sobre este
  runtime? NO.** Ninguno de los números de §E salió de la app ni del grafo
  vigente r1 servido por Neo4j: las filas 3 y 5 (fidelidad y atribución EV2)
  corrieron sobre el `GraphIndex` in-memory (H.1), y la fila 4 (r1 6/26/8,
  sello `774acac`) también — `comun_r1.py` construye la vista runtime de r1
  en memoria con las dataclasses del loader congelado (líneas 16–21), no
  contra Neo4j. Matiz que corresponde declarar: la ablación A1.4 (fila 17,
  0,887→0,981) SÍ corrió sobre el backend Neo4j — `Neo4jIndex` en modos
  `paridad`/`fulltext` sobre KG-Refinado
  (`data/experiment/ablacion_retrieval/corrida/agente_celda.py:49,64-67`,
  corrida `ffc6ff6`) — pero con su harness propio de celdas, sobre KG-Refinado
  (no r1) y ANTES del laudo (es la evidencia que el laudo cita), no sobre la
  app ni sobre la configuración vigente. El BM25 del bake-off (fila 18) no es
  Neo4j: es Okapi BM25 propio, k1=1.2 b=0.75
  (`data/experiment/bakeoff_embeddings/code/e3_medicion.py:51-62`).

### H.3 El head-to-head contra RAG por fragmentos (issue #12) — solo lo escrito

- **Documentos que lo describen**: `docs/plan_tesis.md` bloque A2 («A2 ·
  Baseline RAG tradicional y head-to-head (issue #12, pregunta rectora)»,
  línea 213; diseño detallado en A2.0-banco línea 215, A2.1 línea 218, A2.2
  línea 219); `data/experiment/banco_mcp/README.md` (commit `1fa79de`);
  `docs/laudo_gate_trazabilidad.md` (requisitos R1–R10 del banco);
  `docs/decision_modelo_embeddings.md` §7–§8 (modelo del brazo denso);
  `docs/tablero.md:468-470` («pendiente; habilitada por EV2 cerrado y por el
  mapa causal de fallas»); `docs/tesis/esqueleto_intro.md:438` (OE5: «sin
  corrida (issue #12, §D)»); y §D de este documento («sin set propio; el plan
  declara que reutiliza "mismo juez de fidelidad EV2, mismas 40 preguntas".
  Pre-registro y corrida sin marcar»).
- **Harness previsto**: NO el harness congelado de H.1 — «el mismo agente del
  banco A2.0 en los dos brazos (no el harness congelado) con una sola tool de
  recuperación por brazo» (`plan_tesis.md:218`). El banco es Claude Code
  (`claude -p`, no interactivo, `--model` fijo, prompt custom por argumento)
  con el brazo como variable declarada = qué servidor MCP se enchufa
  (`plan_tesis.md:215`; `banco_mcp/README.md`).
- **Servidores MCP previstos** (`plan_tesis.md:215`): (i) servidor MCP del KG
  que reusa `Neo4jIndex` y expone la firma v1 de las tools
  (`buscar_nodos` BM25, `ver_nodo`, `ver_vecinos(id, direccion)`); (ii)
  servidor MCP vectorial sobre los chunks de E0 con
  `microsoft/harrier-oss-v1-0.6b` (índice local determinístico, sin servicio
  externo). Brazos declarados de la medición A2.2: RAG-BM25 · KG puro en su
  mejor config · híbrido B1.9 (`plan_tesis.md:219`).
- **¿Existe código?** SÍ, el banco: `data/experiment/banco_mcp/` (commit
  `1fa79de`) con `mcp_kg/servidor_mcp_kg.py`, `mcp_vector/servidor_mcp_vector.py`
  + `construir_indice.py`, `agentes/lanzar_agente.py`, tests de paridad y
  aislamiento. Su README declara el alcance: «Este directorio construye el
  banco; no diseña ni corre la evaluación (eso es A2.1/A2.2) y no abre
  material EV2».
- **¿Existe corrida?** NO la del head-to-head: A2.1 (pre-registro) y A2.2
  (corrida, ~$15) están `[ ]` en `docs/plan_tesis.md:218-219`. Lo único
  corrido es el smoke del banco: 12/12 sesiones de fase B sobre 4 preguntas
  «PROPIAS, nunca EV2» (`banco_mcp/smoke/preguntas_smoke.json`, §D de este
  documento), USD 0,534, que valida el instrumento y no mide fidelidad de
  ningún grafo. Prerrequisito abierto declarado: caracterizar la semántica de
  `num_turns` vs `--max-turns` (hallazgo H-B2) antes de sellar A2.1
  (`plan_tesis.md:218`).

### H.4 Diferencias entre H.1 y H.2 (sin adjudicar cuál describe la tesis)

| Aspecto | Agente de EV2 (H.1) | Runtime actual (H.2) |
|---|---|---|
| Clase / código | `GraphAgent` de `harness.py` (cuarteto hasheado, sha `fd267e833866…`), envuelto por `FullCaptureAgent` del runner | `_ChatAgentNeo4j(_ToolLogMixin, GraphAgentNeo4j)` — subclase del mismo `GraphAgent` (`app/main.py:337-343`) |
| Estructura de datos | Índice in-memory `GraphIndex` sobre el kg.json cargado por el loader (`harness.py:130-146`) | Neo4j Community, label `:KG_Reextraido_r1`, índice full-text Lucene; fallback declarado a `GraphIndex` in-memory |
| Búsqueda (`buscar_nodos`) | Léxica exacta por intersección de tokens, sin acentos, ranking por nº de tokens matcheados (`harness.py:154-157`); sin embeddings | BM25 (Lucene, `CALL db.index.fulltext.queryNodes`, analyzer spanish, `ORDER BY score DESC`; `neo4j_index.py:176-186`) |
| Tools y firma | 3 tools firma v1 (`TOOLS`, `harness.py:240-286`) | Las mismas 3 tools firma v1 (tools v2 no promovidas, laudo A1.6 §2.2); paridad 322/322 en `ver_nodo`/`ver_vecinos` |
| Prompt del sistema | `SYSTEM_PROMPT` de `harness.py:61-92` | El mismo, sin edición (`agente_neo4j.py:8-12`) |
| Modelo | `claude-haiku-4-5-20251001` fijo (`harness.py:47`) | El mismo por default; override posible solo en backend Bedrock (`app/llm_backend.py`) |
| Límites | 15 tool calls, `limite` 1..50 (def. 10), 40 vecinos/dirección, 2048 max_tokens | Idénticos (heredados del harness; recorte replicado en `neo4j_index.py:113-116`) |
| Grafos sobre los que operó | KG-Base, KG-Refinado, KG-Reextraído (EV2) y r1 (U-B1.8), vistas in-memory verificadas por sha | KG-Reextraído-r1 vigente (y `v3_vigente`) servidos por Neo4j |
| Caché de llamadas | `CachingClient` con namespace por grafo + `cache_conversation=True` (`runner_ev2.py:97-102,143`) | Cliente directo (`LLM_CLIENT`), sin `CachingClient`; usage crudo por turno en la sesión |
| Números reportados en §E | Filas 3, 4, 5 y 6 salen de este agente | Ninguno (ver H.2; la ablación fila 17 usó el backend Neo4j con harness propio, no la app) |


## I. Candidatos para la figura de la Introducción

Agregado el 2026-09-01 en unidad de SOLO LECTURA (esta sección es la única
escritura). Objetivo: candidatos para una figura «de la norma al grafo» —
a la izquierda el texto de dos puntos de un Texto Ordenado, uno de los
cuales remite al otro; a la derecha los nodos y aristas extraídos de ellos,
con la arista que sigue la remisión resaltada. Esta sección reporta datos;
no recomienda ningún candidato: la elección es de la autora.

### I.1 Método del barrido y resultado global

- **Universo (criterio 1)**: las 40 preguntas del conjunto de evaluación de
  fidelidad (`data/experiment/exploracion/ev2_fidelidad/preguntas_ev2_fidelidad.json`;
  conteo: `python3 -c "import json; print(len(json.load(open('data/experiment/exploracion/ev2_fidelidad/preguntas_ev2_fidelidad.json'))['preguntas']))"` → 40),
  con ancla en `gold.ancla` (formato `to:punto`).
- **Criterio 2, operacionalización declarada**: «nodos que resuelven el
  ancla» = nodos de contenido (`Obligacion`/`Restriccion`/`Excepcion`/
  `Operacion`) del grafo de desarrollo
  (`data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json`, 6.529
  nodos / 17.772 aristas, fila 1 de §A.1) con provenance de rol
  `punto_propio` en el punto ancla o en un subpunto suyo; «remisión» = fila
  con `estado == "resuelta"` de
  `data/experiment/reextraccion_v2/corpus_v2/salida_r1/referencias_remisiones.json`
  (1.089 filas) con origen en esos puntos y destino en OTRO punto,
  materializada en `kg.json` como aristas `referencia` del nodo remitente
  hacia nodos de contenido del punto destino. Detectar el par directamente
  sobre las aristas del `kg.json` sin exigir la fila de remisión textual
  produce falsos pares (nodos multi-anclados y hubs de catálogo remiten
  «desde» puntos que no los mencionan); por eso el barrido exige la
  evidencia textual. Con este criterio ningún par de las 40 preguntas usa
  `exceptua` ni `exceptua_obligacion` entre puntos distintos (0 de 26):
  todas las remisiones halladas son `referencia`.
- **Resultado**: 26 pares (pregunta, punto A, punto B) sobre 11 preguntas
  cumplen los criterios 1 y 2 a la vez (EV2F-004, -007, -012, -013, -014,
  -015, -019, -023, -026, -030, -033). NINGÚN par cumple los cinco
  criterios simultáneamente: los pares con textos cortos y subgrafo chico
  (los de EV2F-013) no tienen veredicto correcto en ningún grafo, y el
  único par cuya pregunta tiene veredicto correcto (EV2F-033, correcto en
  los tres grafos) tiene textos de 1.834 y 992 caracteres.
- **Orden declarado**: un candidato por pregunta (el par mejor puntuado de
  esa pregunta) y preguntas ordenadas por un puntaje que sigue la prioridad
  de los criterios: primero longitud de ambos textos (criterio 3), después
  tamaño del subgrafo 5–9 nodos y etiquetas ≤ 60 caracteres (criterio 4),
  por último veredicto correcto con traza (criterio 5); pesos exactos en
  `analisis_v5.py` del paquete de revisión de la unidad.
- **Definición de subgrafo usada** (para el criterio 4 y las listas de
  abajo): nodos con provenance en el punto A o en el punto B, más las
  aristas del `kg.json` cuya provenance cae en A o B, más los extremos de
  esas aristas. Reproducible por parseo de `provenance`/`provenances` de
  `salida_r1/kg.json`.
- **Veredictos — contradicción del insumo, reportada**: el archivo indicado
  (`data/experiment/ev2_adjudicacion/adjudicacion_SOLO_MESA/cruce_definitivo_por_grafo_SOLO_MESA.json`)
  trae SOLO agregados por grafo, no veredictos por pregunta. El veredicto
  definitivo por pregunta se recompone de
  `data/experiment/ev2_adjudicacion/adjudicacion/veredictos_definitivos_ciego.json`
  (campo `definitivo`) desanonimizado con
  `data/experiment/ev2_fidelidad_eval/desanonimizacion/tabla_id_opaco.json`;
  los agregados recomputados coinciden exactamente con el cruce definitivo:
  KG-Base 3/20/17, KG-Reextraído 4/27/9, KG-Refinado 5/26/9
  (correcto/parcial/incorrecto sobre 40). Alias de grafos según §F.2–F.4:
  `run_3` = KG-Base, `v2` = KG-Reextraído, `v3` = KG-Refinado.
- **Trazas**: una por (pregunta, grafo) en
  `data/experiment/ev2_corrida/trazas/ev2_base_{run3,v2,v3}/EV2F-NNN.json`;
  la existencia de cada traza citada abajo fue verificada con
  `os.path.exists`.

Resumen de los cinco candidatos (detalle completo en I.2–I.6):

| # | Pregunta | Par (A → B) | chars A/B | Nodos | Aristas | Etiqueta máx. | Veredictos Base/Reext/Refin | ¿Traza correcta? |
|---|---|---|---|---|---|---|---|---|
| 1 | EV2F-013 | ext:3.17.1.4 → ext:3.4.3 | 156/231 | 10 | 12 | 70 | parcial/parcial/incorrecto | no |
| 2 | EV2F-015 | ext:3.13.1.11 → ext:14.2.3 | 211/613 | 13 | 18 | 64 | parcial/parcial/parcial | no |
| 3 | EV2F-026 | cla:3.5.2 → cla:3.7 | 1.160/253 | 10 | 17 | 64 | parcial/incorrecto/parcial | no |
| 4 | EV2F-014 | ext:13.5 → ext:10.10.2.1 | 1.443/434 | 18 | 35 | 77 | parcial/incorrecto/parcial | no |
| 5 | EV2F-033 | ric:12.4 → ric:1.1 | 1.834/992 | 23 | 36 | 52 | correcto/correcto/correcto | sí (los tres grafos) |

Las otras seis preguntas con pares que cumplen 1+2, con su mejor par
(quedaron fuera del top 5 por el puntaje declarado):
EV2F-030 `cla:10.3 → cla:7.3` (588/1.326, 11 nodos) ·
EV2F-007 `ext:13.3.1 → ext:10.10.2.1` (1.077/434, 19 nodos) ·
EV2F-004 `ext:2.6.1.3 → ext:2.2.2.2` (120/1.713, 30 nodos) ·
EV2F-023 `cap:8.3.2.12 → cap:8.3.4.4` (1.115/1.249, 16 nodos) ·
EV2F-012 `ext:10.8 → ext:10.3.3` (931/1.072, 29 nodos) ·
EV2F-019 `cap:4.2.4 → cap:4.2.2` (719/4.560, 27 nodos).

### I.2 Candidato 1 — EV2F-013, par ext:3.17.1.4 → ext:3.4.3

- **Pregunta** (`EV2F-013`): «Una petrolera beneficiaria del régimen de acceso a divisas por producción incremental obtuvo la certificación correspondiente. ¿Qué operaciones puede cursar con esa certificación y quién es responsable de emitirla?»
- **Ancla** (`gold.ancla`): `ext:3.17`. Punto de origen del par: `ext:3.17.1.4` (subpunto del ancla).
- **Punto referido**: `ext:3.4.3`. Evidencia textual de la remisión (`referencias_remisiones.json`, campo `evidencia`): «Requisitos puntos 3.4.1 a 3.4.3 — utilidades divide»; «la medida que se verifiquen los requisitos previstos en los puntos 3.4.1. a 3.4.3.»
- **Texto verbatim de ambos puntos**:
  - Unidad E0 `ext::3.17.1.4` — `TO_exterior_cambios_actual.pdf`, página(s) [50], 156 caracteres propios (`data/experiment/reextraccion_v2/e0_chunking/salida/chunks_ext.json`, campo `texto`):

    ```
    3.17.1.4. Pagos de utilidades y dividendos a accionistas no residentes en la medida
    que se verifiquen los requisitos previstos en los puntos 3.4.1. a 3.4.3.
    ```
  - Unidad E0 `ext::3.4.3` — `TO_exterior_cambios_actual.pdf`, página(s) [17], 231 caracteres propios (`data/experiment/reextraccion_v2/e0_chunking/salida/chunks_ext.json`, campo `texto`):

    ```
    3.4.3. La entidad deberá verificar que el cliente haya dado cumplimiento en caso de
    corresponder, a la declaración de la última presentación vencida del “Relevamiento de
    activos y pasivos externos” por las operaciones involucradas.
    ```
- **Arista(s) que siguen la remisión** (2):
  - `Restriccion_pagos_de_utilidades_y_dividendos_a_accionistas_no_residentes_en_la_medida_que_se_8355c7` —`referencia`→ `Obligacion_la_entidad_debera_verificar_que_el_cliente_haya_dado_cumplimiento_en_caso_de_cor_6514f0`
  - `Restriccion_pagos_de_utilidades_y_dividendos_a_accionistas_no_residentes_en_la_medida_que_se_8355c7` —`referencia`→ `Operacion_giro_de_utilidades_y_dividendos_al_exterior_31f15a`
- **Nodos del subgrafo** (10; tipo | etiqueta | id):
  - Obligacion | Declaración jurada representante legal | `Obligacion_la_entidad_debera_contar_con_una_declaracion_jurada_firmada_por_el_representante_ed6cf9`
  - Obligacion | Verificación de cumplimiento declaración de activos y pasivos externos | `Obligacion_la_entidad_debera_verificar_que_el_cliente_haya_dado_cumplimiento_en_caso_de_cor_6514f0`
  - Obligacion | Balances cerrados y auditados | `Obligacion_las_utilidades_y_dividendos_deben_corresponder_a_balances_cerrados_y_auditados_999fbd`
  - Operacion | Giro de utilidades y dividendos al exterior | `Operacion_giro_de_utilidades_y_dividendos_al_exterior_31f15a`
  - Operacion | Giro divisas utilidades dividendos exterior | `Operacion_giro_divisas_utilidades_dividendos_exterior_c53c4e`
  - Operacion | Pagos utilidades dividendos accionistas no residentes | `Operacion_pagos_utilidades_dividendos_accionistas_no_residentes_59fccf`
  - Restriccion | Monto total no supere distribución asamblea | `Restriccion_el_monto_total_abonado_por_este_concepto_a_accionistas_no_residentes_incluido_el_459761`
  - Restriccion | Requisitos puntos 3.4.1 a 3.4.3 — utilidades dividendos | `Restriccion_pagos_de_utilidades_y_dividendos_a_accionistas_no_residentes_en_la_medida_que_se_8355c7`
  - Sujeto | Entidades autorizadas a operar en cambios (Exterior) | `Sujeto_rol_entidad_autorizada_exterior`
  - TextoOrdenado | Texto Ordenado de Exterior y Cambios | `TextoOrdenado_to_exterior_cambios_actual_pdf`
- **Aristas del subgrafo** (12; origen —predicado→ destino):
  - `Restriccion_pagos_de_utilidades_y_dividendos_a_accionistas_no_residentes_en_la_medida_que_se_8355c7` —`aplica_a`→ `Sujeto_rol_entidad_autorizada_exterior`
  - `Restriccion_pagos_de_utilidades_y_dividendos_a_accionistas_no_residentes_en_la_medida_que_se_8355c7` —`establecida_en`→ `TextoOrdenado_to_exterior_cambios_actual_pdf`
  - `Restriccion_pagos_de_utilidades_y_dividendos_a_accionistas_no_residentes_en_la_medida_que_se_8355c7` —`limita`→ `Operacion_pagos_utilidades_dividendos_accionistas_no_residentes_59fccf`
  - `Restriccion_pagos_de_utilidades_y_dividendos_a_accionistas_no_residentes_en_la_medida_que_se_8355c7` —`referencia`→ `Obligacion_la_entidad_debera_contar_con_una_declaracion_jurada_firmada_por_el_representante_ed6cf9`
  - `Restriccion_pagos_de_utilidades_y_dividendos_a_accionistas_no_residentes_en_la_medida_que_se_8355c7` —`referencia`→ `Obligacion_la_entidad_debera_verificar_que_el_cliente_haya_dado_cumplimiento_en_caso_de_cor_6514f0`
  - `Restriccion_pagos_de_utilidades_y_dividendos_a_accionistas_no_residentes_en_la_medida_que_se_8355c7` —`referencia`→ `Obligacion_las_utilidades_y_dividendos_deben_corresponder_a_balances_cerrados_y_auditados_999fbd`
  - `Restriccion_pagos_de_utilidades_y_dividendos_a_accionistas_no_residentes_en_la_medida_que_se_8355c7` —`referencia`→ `Operacion_giro_de_utilidades_y_dividendos_al_exterior_31f15a`
  - `Restriccion_pagos_de_utilidades_y_dividendos_a_accionistas_no_residentes_en_la_medida_que_se_8355c7` —`referencia`→ `Operacion_giro_divisas_utilidades_dividendos_exterior_c53c4e`
  - `Restriccion_pagos_de_utilidades_y_dividendos_a_accionistas_no_residentes_en_la_medida_que_se_8355c7` —`referencia`→ `Restriccion_el_monto_total_abonado_por_este_concepto_a_accionistas_no_residentes_incluido_el_459761`
  - `Obligacion_la_entidad_debera_verificar_que_el_cliente_haya_dado_cumplimiento_en_caso_de_cor_6514f0` —`aplica_a`→ `Sujeto_rol_entidad_autorizada_exterior`
  - `Obligacion_la_entidad_debera_verificar_que_el_cliente_haya_dado_cumplimiento_en_caso_de_cor_6514f0` —`establecida_en`→ `TextoOrdenado_to_exterior_cambios_actual_pdf`
  - `Obligacion_la_entidad_debera_verificar_que_el_cliente_haya_dado_cumplimiento_en_caso_de_cor_6514f0` —`regula`→ `Operacion_giro_de_utilidades_y_dividendos_al_exterior_31f15a`
- **Cantidad**: 10 nodos, 12 aristas.
- **Veredicto definitivo por grafo**: KG-Base (`run_3`): **parcial** · KG-Reextraído (`v2`): **parcial** · KG-Refinado (`v3`): **incorrecto**.
- **Traza correcta**: no existe (ningún grafo con veredicto correcto). Las trazas de los tres veredictos están persistidas en `data/experiment/ev2_corrida/trazas/ev2_base_run3/EV2F-013.json`, `data/experiment/ev2_corrida/trazas/ev2_base_v2/EV2F-013.json`, `data/experiment/ev2_corrida/trazas/ev2_base_v3/EV2F-013.json`.

### I.3 Candidato 2 — EV2F-015, par ext:3.13.1.11 → ext:14.2.3

- **Pregunta** (`EV2F-015`): «Un inversor no residente quiere repatriar una inversión directa en una empresa argentina. ¿Requiere conformidad previa del BCRA y qué excepciones contempla la norma?»
- **Ancla** (`gold.ancla`): `ext:3.13.1`. Punto de origen del par: `ext:3.13.1.11` (subpunto del ancla).
- **Punto referido**: `ext:14.2.3`. Evidencia textual de la remisión (`referencias_remisiones.json`, campo `evidencia`): «no residentes en una VPU adherida al RIGI encuadradas en el punto 14.2.3 requieren la confor»
- **Texto verbatim de ambos puntos**:
  - Unidad E0 `ext::3.13.1.11` — `TO_exterior_cambios_actual.pdf`, página(s) [39], 211 caracteres propios (`data/experiment/reextraccion_v2/e0_chunking/salida/chunks_ext.json`, campo `texto`):

    ```
    3.13.1.11. Repatriaciones de aportes de inversión directa de no residentes en una
    Vehículo de Proyecto Único (VPU) adherido al Régimen de Incentivo para
    Grandes Inversiones (RIGI) encuadradas en el punto 14.2.3.
    ```
  - Unidad E0 `ext::14.2.3` — `TO_exterior_cambios_actual.pdf`, página(s) [178], 613 caracteres propios (`data/experiment/reextraccion_v2/e0_chunking/salida/chunks_ext.json`, campo `texto`):

    ```
    14.2.3. En el marco de lo dispuesto en el punto 3.13., las entidades también podrán dar
    acceso a un VPU adherido al RIGI para concretar, sin necesidad de contar con la
    conformidad previa del BCRA ni respetar plazos mínimos de permanencia si alguno
    de estos requisitos estuviese vigente, la repatriación de los aportes de inversión
    directa de sus accionistas no residentes que fueron destinados a financiar el
    proyecto en la medida que el monto acumulado de las repatriaciones de capital del
    no residente sea menor o igual a la suma de los aportes contemplados en los
    incisos i) y ii) del punto 14.2.2. precedente.
    ```
- **Arista(s) que siguen la remisión** (4):
  - `Restriccion_las_repatriaciones_de_aportes_de_inversion_directa_de_no_residentes_en_una_vpu_a_727e07` —`referencia`→ `Excepcion_sin_necesidad_de_contar_con_la_conformidad_previa_del_bcra_ni_respetar_plazos_mi_3414fc`
  - `Restriccion_las_repatriaciones_de_aportes_de_inversion_directa_de_no_residentes_en_una_vpu_a_727e07` —`referencia`→ `Obligacion_las_entidades_podran_dar_acceso_a_un_vpu_adherido_al_rigi_para_concretar_la_repa_085d51`
  - `Restriccion_las_repatriaciones_de_aportes_de_inversion_directa_de_no_residentes_en_una_vpu_a_727e07` —`referencia`→ `Operacion_repatriacion_aportes_inversion_directa_accionistas_no_residentes_ab7287`
  - `Restriccion_las_repatriaciones_de_aportes_de_inversion_directa_de_no_residentes_en_una_vpu_a_727e07` —`referencia`→ `Restriccion_el_monto_acumulado_de_las_repatriaciones_de_capital_del_no_residente_sea_menor_o_dc861b`
- **Nodos del subgrafo** (13; tipo | etiqueta | id):
  - Excepcion | Excepción conformidad previa BCRA y plazos mínimos permanencia | `Excepcion_sin_necesidad_de_contar_con_la_conformidad_previa_del_bcra_ni_respetar_plazos_mi_3414fc`
  - Excepcion | Exención conformidad previa BCRA — utilidades/dividendos | `Excepcion_sin_necesidad_de_contar_con_la_conformidad_previa_del_bcra_si_este_requisito_est_220071`
  - Obligacion | Acceso mercado cambios VPU RIGI repatriación capital | `Obligacion_las_entidades_podran_dar_acceso_a_un_vpu_adherido_al_rigi_para_concretar_la_repa_085d51`
  - Obligacion | Cumplimiento requisitos — acceso cambios utilidades/dividendos | `Obligacion_las_entidades_podran_darle_acceso_al_mercado_de_cambios_al_vpu_para_pagar_utilid_0661f8`
  - Operacion | Acceso mercado cambios — pago utilidades/dividendos VPU | `Operacion_acceso_mercado_cambios_pago_utilidades_dividendos_vpu_c8b402`
  - Operacion | Repatriación aportes inversión directa accionistas no residentes | `Operacion_repatriacion_aportes_inversion_directa_accionistas_no_residentes_ab7287`
  - Operacion | Repatriación de aportes inversión directa VPU-RIGI | `Operacion_repatriacion_de_aportes_inversion_directa_vpu_rigi_aea171`
  - Restriccion | Límite cualitativo — aportes inversión directa en especie | `Restriccion_aportes_de_inversion_directa_en_especie_instrumentados_mediante_la_entrega_al_vp_12842e`
  - Restriccion | Límite monto acumulado repatriaciones menor o igual suma aportes | `Restriccion_el_monto_acumulado_de_las_repatriaciones_de_capital_del_no_residente_sea_menor_o_dc861b`
  - Restriccion | Límite cualitativo — proporción aportes inversión directa | `Restriccion_la_proporcion_de_aportes_de_inversion_directa_en_el_vpu_que_fue_ingresada_y_liqu_3fe70a`
  - Restriccion | Conformidad previa BCRA — repatriación VPU-RIGI | `Restriccion_las_repatriaciones_de_aportes_de_inversion_directa_de_no_residentes_en_una_vpu_a_727e07`
  - Sujeto | Entidades autorizadas a operar en cambios (Exterior) | `Sujeto_rol_entidad_autorizada_exterior`
  - TextoOrdenado | Texto Ordenado de Exterior y Cambios | `TextoOrdenado_to_exterior_cambios_actual_pdf`
- **Aristas del subgrafo** (18; origen —predicado→ destino):
  - `Restriccion_las_repatriaciones_de_aportes_de_inversion_directa_de_no_residentes_en_una_vpu_a_727e07` —`aplica_a`→ `Sujeto_rol_entidad_autorizada_exterior`
  - `Restriccion_las_repatriaciones_de_aportes_de_inversion_directa_de_no_residentes_en_una_vpu_a_727e07` —`establecida_en`→ `TextoOrdenado_to_exterior_cambios_actual_pdf`
  - `Restriccion_las_repatriaciones_de_aportes_de_inversion_directa_de_no_residentes_en_una_vpu_a_727e07` —`referencia`→ `Excepcion_sin_necesidad_de_contar_con_la_conformidad_previa_del_bcra_ni_respetar_plazos_mi_3414fc`
  - `Restriccion_las_repatriaciones_de_aportes_de_inversion_directa_de_no_residentes_en_una_vpu_a_727e07` —`referencia`→ `Obligacion_las_entidades_podran_dar_acceso_a_un_vpu_adherido_al_rigi_para_concretar_la_repa_085d51`
  - `Restriccion_las_repatriaciones_de_aportes_de_inversion_directa_de_no_residentes_en_una_vpu_a_727e07` —`referencia`→ `Operacion_repatriacion_aportes_inversion_directa_accionistas_no_residentes_ab7287`
  - `Restriccion_las_repatriaciones_de_aportes_de_inversion_directa_de_no_residentes_en_una_vpu_a_727e07` —`referencia`→ `Restriccion_el_monto_acumulado_de_las_repatriaciones_de_capital_del_no_residente_sea_menor_o_dc861b`
  - `Restriccion_las_repatriaciones_de_aportes_de_inversion_directa_de_no_residentes_en_una_vpu_a_727e07` —`regula`→ `Operacion_repatriacion_de_aportes_inversion_directa_vpu_rigi_aea171`
  - `Excepcion_sin_necesidad_de_contar_con_la_conformidad_previa_del_bcra_ni_respetar_plazos_mi_3414fc` —`establecida_en`→ `TextoOrdenado_to_exterior_cambios_actual_pdf`
  - `Excepcion_sin_necesidad_de_contar_con_la_conformidad_previa_del_bcra_ni_respetar_plazos_mi_3414fc` —`exceptua_obligacion`→ `Obligacion_las_entidades_podran_dar_acceso_a_un_vpu_adherido_al_rigi_para_concretar_la_repa_085d51`
  - `Obligacion_las_entidades_podran_dar_acceso_a_un_vpu_adherido_al_rigi_para_concretar_la_repa_085d51` —`aplica_a`→ `Sujeto_rol_entidad_autorizada_exterior`
  - `Obligacion_las_entidades_podran_dar_acceso_a_un_vpu_adherido_al_rigi_para_concretar_la_repa_085d51` —`establecida_en`→ `TextoOrdenado_to_exterior_cambios_actual_pdf`
  - `Restriccion_el_monto_acumulado_de_las_repatriaciones_de_capital_del_no_residente_sea_menor_o_dc861b` —`establecida_en`→ `TextoOrdenado_to_exterior_cambios_actual_pdf`
  - `Restriccion_el_monto_acumulado_de_las_repatriaciones_de_capital_del_no_residente_sea_menor_o_dc861b` —`limita`→ `Operacion_repatriacion_aportes_inversion_directa_accionistas_no_residentes_ab7287`
  - `Restriccion_el_monto_acumulado_de_las_repatriaciones_de_capital_del_no_residente_sea_menor_o_dc861b` —`referencia`→ `Excepcion_sin_necesidad_de_contar_con_la_conformidad_previa_del_bcra_si_este_requisito_est_220071`
  - `Restriccion_el_monto_acumulado_de_las_repatriaciones_de_capital_del_no_residente_sea_menor_o_dc861b` —`referencia`→ `Obligacion_las_entidades_podran_darle_acceso_al_mercado_de_cambios_al_vpu_para_pagar_utilid_0661f8`
  - `Restriccion_el_monto_acumulado_de_las_repatriaciones_de_capital_del_no_residente_sea_menor_o_dc861b` —`referencia`→ `Operacion_acceso_mercado_cambios_pago_utilidades_dividendos_vpu_c8b402`
  - `Restriccion_el_monto_acumulado_de_las_repatriaciones_de_capital_del_no_residente_sea_menor_o_dc861b` —`referencia`→ `Restriccion_aportes_de_inversion_directa_en_especie_instrumentados_mediante_la_entrega_al_vp_12842e`
  - `Restriccion_el_monto_acumulado_de_las_repatriaciones_de_capital_del_no_residente_sea_menor_o_dc861b` —`referencia`→ `Restriccion_la_proporcion_de_aportes_de_inversion_directa_en_el_vpu_que_fue_ingresada_y_liqu_3fe70a`
- **Cantidad**: 13 nodos, 18 aristas.
- **Veredicto definitivo por grafo**: KG-Base (`run_3`): **parcial** · KG-Reextraído (`v2`): **parcial** · KG-Refinado (`v3`): **parcial**.
- **Traza correcta**: no existe (ningún grafo con veredicto correcto). Las trazas de los tres veredictos están persistidas en `data/experiment/ev2_corrida/trazas/ev2_base_run3/EV2F-015.json`, `data/experiment/ev2_corrida/trazas/ev2_base_v2/EV2F-015.json`, `data/experiment/ev2_corrida/trazas/ev2_base_v3/EV2F-015.json`.

### I.4 Candidato 3 — EV2F-026, par cla:3.5.2 → cla:3.7

- **Pregunta** (`EV2F-026`): «¿A quién puede encomendar una entidad financiera la tarea de clasificar a sus deudores y qué recaudos exige cada alternativa?»
- **Ancla** (`gold.ancla`): `cla:3.5`. Punto de origen del par: `cla:3.5.2` (subpunto del ancla).
- **Punto referido**: `cla:3.7`. Evidencia textual de la remisión (`referencias_remisiones.json`, campo `evidencia`): «o el equivalente al importe de referencia establecido en el punto 3.7., de ambos el menor»
- **Texto verbatim de ambos puntos**:
  - Unidad E0 `cla::3.5.2` — `TO_clasificacion_deudores_actual.pdf`, página(s) [13], 1160 caracteres propios (`data/experiment/reextraccion_v2/e0_chunking/salida/chunks_cla.json`, campo `texto`):

    ```
    3.5.2. Al sector encargado del otorgamiento de créditos y garantías.
    De optar por esta posibilidad, la entidad financiera deberá contar con una oficina inde-
    pendiente que tendrá como función efectuar la revisión de las clasificaciones asignadas a
    los clientes por el sector de créditos.
    Dicha revisión –que podrá estar a cargo de la auditoría interna de la entidad– deberá
    comprender obligatoriamente a los clientes cuyo endeudamiento total en pesos y en mo-
    neda extranjera (por las financiaciones comprendidas) supere el 1 % de la responsabili-
    dad patrimonial computable de la entidad del mes anterior al de la clasificación o el equi-
    valente al importe de referencia establecido en el punto 3.7., de ambos el menor, y alcan-
    zar como mínimo el 20 % de la cartera activa total, que se completará, en caso de co-
    rresponder, incorporando a clientes cuyo endeudamiento total –en orden decreciente–
    sea inferior a aquellos márgenes.
    La revisión deberá estar concluida antes de presentarse a la Superintendencia de Enti-
    dades Financieras y Cambiarias el “Estado de situación de deudores” cuya información
    incluya la clasificación de los mencionados clientes.
    ```
  - Unidad E0 `cla::3.7` — `TO_clasificacion_deudores_actual.pdf`, página(s) [14], 253 caracteres propios (`data/experiment/reextraccion_v2/e0_chunking/salida/chunks_cla.json`, campo `texto`):

    ```
    3.7. Importe de referencia.
    El importe a considerar será el nivel máximo del valor de ventas totales anuales para la
    categoría “Micro” correspondiente al sector “Comercio” que determine la autoridad de
    aplicación de la Ley 24.467 (y sus modificatorias).
    ```
- **Arista(s) que siguen la remisión** (1):
  - `Obligacion_la_revision_debera_comprender_obligatoriamente_a_los_clientes_cuyo_endeudamiento_3e3311` —`referencia`→ `Obligacion_el_importe_a_considerar_sera_el_nivel_maximo_del_valor_de_ventas_totales_anuales_7f1ae2`
- **Nodos del subgrafo** (10; tipo | etiqueta | id):
  - Excepcion | Revisión interna a cargo de auditoría interna | `Excepcion_la_revision_podra_estar_a_cargo_de_la_auditoria_interna_de_la_entidad_51e745`
  - Obligacion | Considerar importe de referencia — ventas anuales Micro Comercio | `Obligacion_el_importe_a_considerar_sera_el_nivel_maximo_del_valor_de_ventas_totales_anuales_7f1ae2`
  - Obligacion | Contar con oficina independiente para revisión | `Obligacion_la_entidad_financiera_debera_contar_con_una_oficina_independiente_que_tendra_com_01e407`
  - Obligacion | Revisión obligatoria clientes con endeudamiento superior a 1% | `Obligacion_la_revision_debera_comprender_obligatoriamente_a_los_clientes_cuyo_endeudamiento_3e3311`
  - Obligacion | Presentar revisión antes de reportar Estado de situación | `Obligacion_la_revision_debera_estar_concluida_antes_de_presentarse_a_la_superintendencia_de_6ff192`
  - Operacion | Revisión de clasificaciones de clientes | `Operacion_revision_de_clasificaciones_de_clientes_da6b89`
  - Restriccion | Límite mínimo cobertura cartera activa revisión | `Restriccion_la_revision_alcanzara_como_minimo_el_20_de_la_cartera_activa_total_67ea08`
  - Sujeto | Entidades financieras | `Sujeto_entidad_financiera`
  - Sujeto | Obligados a clasificar deudores (Clasificación) | `Sujeto_rol_obligado_a_clasificar_clasificacion`
  - TextoOrdenado | Clasificación de Deudores | `TextoOrdenado_to_clasificacion_deudores_actual_pdf`
- **Aristas del subgrafo** (17; origen —predicado→ destino):
  - `Excepcion_la_revision_podra_estar_a_cargo_de_la_auditoria_interna_de_la_entidad_51e745` —`establecida_en`→ `TextoOrdenado_to_clasificacion_deudores_actual_pdf`
  - `Obligacion_la_entidad_financiera_debera_contar_con_una_oficina_independiente_que_tendra_com_01e407` —`aplica_a`→ `Sujeto_entidad_financiera`
  - `Obligacion_la_entidad_financiera_debera_contar_con_una_oficina_independiente_que_tendra_com_01e407` —`establecida_en`→ `TextoOrdenado_to_clasificacion_deudores_actual_pdf`
  - `Obligacion_la_entidad_financiera_debera_contar_con_una_oficina_independiente_que_tendra_com_01e407` —`regula`→ `Operacion_revision_de_clasificaciones_de_clientes_da6b89`
  - `Obligacion_la_revision_debera_comprender_obligatoriamente_a_los_clientes_cuyo_endeudamiento_3e3311` —`aplica_a`→ `Sujeto_rol_obligado_a_clasificar_clasificacion`
  - `Obligacion_la_revision_debera_comprender_obligatoriamente_a_los_clientes_cuyo_endeudamiento_3e3311` —`establecida_en`→ `TextoOrdenado_to_clasificacion_deudores_actual_pdf`
  - `Obligacion_la_revision_debera_comprender_obligatoriamente_a_los_clientes_cuyo_endeudamiento_3e3311` —`referencia`→ `Obligacion_el_importe_a_considerar_sera_el_nivel_maximo_del_valor_de_ventas_totales_anuales_7f1ae2`
  - `Obligacion_la_revision_debera_comprender_obligatoriamente_a_los_clientes_cuyo_endeudamiento_3e3311` —`regula`→ `Operacion_revision_de_clasificaciones_de_clientes_da6b89`
  - `Obligacion_la_revision_debera_estar_concluida_antes_de_presentarse_a_la_superintendencia_de_6ff192` —`aplica_a`→ `Sujeto_entidad_financiera`
  - `Obligacion_la_revision_debera_estar_concluida_antes_de_presentarse_a_la_superintendencia_de_6ff192` —`condiciona`→ `Operacion_revision_de_clasificaciones_de_clientes_da6b89`
  - `Obligacion_la_revision_debera_estar_concluida_antes_de_presentarse_a_la_superintendencia_de_6ff192` —`establecida_en`→ `TextoOrdenado_to_clasificacion_deudores_actual_pdf`
  - `Obligacion_la_revision_debera_estar_concluida_antes_de_presentarse_a_la_superintendencia_de_6ff192` —`regula`→ `Operacion_revision_de_clasificaciones_de_clientes_da6b89`
  - `Restriccion_la_revision_alcanzara_como_minimo_el_20_de_la_cartera_activa_total_67ea08` —`aplica_a`→ `Sujeto_rol_obligado_a_clasificar_clasificacion`
  - `Restriccion_la_revision_alcanzara_como_minimo_el_20_de_la_cartera_activa_total_67ea08` —`establecida_en`→ `TextoOrdenado_to_clasificacion_deudores_actual_pdf`
  - `Restriccion_la_revision_alcanzara_como_minimo_el_20_de_la_cartera_activa_total_67ea08` —`limita`→ `Operacion_revision_de_clasificaciones_de_clientes_da6b89`
  - `Obligacion_el_importe_a_considerar_sera_el_nivel_maximo_del_valor_de_ventas_totales_anuales_7f1ae2` —`aplica_a`→ `Sujeto_rol_obligado_a_clasificar_clasificacion`
  - `Obligacion_el_importe_a_considerar_sera_el_nivel_maximo_del_valor_de_ventas_totales_anuales_7f1ae2` —`establecida_en`→ `TextoOrdenado_to_clasificacion_deudores_actual_pdf`
- **Cantidad**: 10 nodos, 17 aristas.
- **Veredicto definitivo por grafo**: KG-Base (`run_3`): **parcial** · KG-Reextraído (`v2`): **incorrecto** · KG-Refinado (`v3`): **parcial**.
- **Traza correcta**: no existe (ningún grafo con veredicto correcto). Las trazas de los tres veredictos están persistidas en `data/experiment/ev2_corrida/trazas/ev2_base_run3/EV2F-026.json`, `data/experiment/ev2_corrida/trazas/ev2_base_v2/EV2F-026.json`, `data/experiment/ev2_corrida/trazas/ev2_base_v3/EV2F-026.json`.

### I.5 Candidato 4 — EV2F-014, par ext:13.5 → ext:10.10.2.1

- **Pregunta** (`EV2F-014`): «Un banco emitió una carta de crédito para garantizar una importación de servicios y ahora debe afrontar el pago. ¿Qué condiciones tiene que verificar para su propio acceso al mercado de cambios?»
- **Ancla** (`gold.ancla`): `ext:13.5`. Punto de origen del par: `ext:13.5` (el ancla misma).
- **Punto referido**: `ext:10.10.2.1`. Evidencia textual de la remisión (`referencias_remisiones.json`, campo `evidencia`): «importaciones de bienes' que encuadra en lo previsto en el punto 10.10.2.1., el pago garantizad»
- **Texto verbatim de ambos puntos**:
  - Unidad E0 `ext::13.5` — `TO_exterior_cambios_actual.pdf`, página(s) [173, 174], 1443 caracteres propios (`data/experiment/reextraccion_v2/e0_chunking/salida/chunks_ext.json`, campo `texto`):

    ```
    13.5. Cancelación de cartas de crédito o letras avaladas emitidas u otorgadas por entidades
    financieras para garantizar importaciones de servicios.
    Las entidades financieras tendrán acceso al mercado de cambios para cursar pagos propios
    por cartas de crédito o letras avaladas emitidas u otorgadas para garantizar operaciones de
    importaciones de servicios, en la medida que se verifique que cumplían las condiciones que
    resultaban aplicables según la fecha en que se emitió u otorgó la carta de crédito o letra
    avalada.
    En particular, en el caso de cartas de crédito o letras avaladas emitidas u otorgadas a partir
    del 13/12/23, la entidad deberá contar con la documentación que demuestre que, al
    momento de la apertura o emisión, la operación garantizada correspondía a un servicio
    prestado o devengado a partir del 13/12/23 y el pago garantizado debía ser concretado por
    el cliente a partir de la fecha que resultaba de adicionar el plazo en días corridos que le
    corresponde al servicio por el punto 13.2. más otros 15 (quince) días corridos a la fecha
    estimada de prestación o devengamiento del servicio.
    En caso de tratarse una operación del concepto “S30. Servicios de fletes por operaciones de
    importaciones de bienes” que encuadra en lo previsto en el punto 10.10.2.1., debía ser
    concretado por el cliente a partir de la fecha que resultaba de adicionar 15 (quince) días
    corridos a la fecha estimada de embarque de los bienes en origen.
    ```
  - Unidad E0 `ext::10.10.2.1` — `TO_exterior_cambios_actual.pdf`, página(s) [154], 434 caracteres propios (`data/experiment/reextraccion_v2/e0_chunking/salida/chunks_ext.json`, campo `texto`):

    ```
    10.10.2.1. Pagos a la vista de importaciones de bienes cursados por personas
    humanas o personas jurídicas que clasifiquen como MiPyMe según lo
    dispuesto en las normas de "Determinación de la condición de micro,
    pequeña y mediana empresa", en la medida que se trate de bienes
    que hayan sido embarcados en origen a partir del 14/04/25 y las
    posiciones arancelarias de los bienes no correspondan a aquellas
    comprendidas en el punto 12.1.
    ```
- **Arista(s) que siguen la remisión** (4):
  - `Obligacion_en_caso_de_tratarse_una_operacion_del_concepto_s30_servicios_de_fletes_por_opera_69475a` —`referencia`→ `Operacion_pago_a_la_vista_de_importacion_de_bienes_45f1f9`
  - `Obligacion_en_caso_de_tratarse_una_operacion_del_concepto_s30_servicios_de_fletes_por_opera_69475a` —`referencia`→ `Restriccion_bienes_que_hayan_sido_embarcados_en_origen_a_partir_del_14_04_25_8dd261`
  - `Obligacion_en_caso_de_tratarse_una_operacion_del_concepto_s30_servicios_de_fletes_por_opera_69475a` —`referencia`→ `Restriccion_cursados_por_personas_humanas_o_personas_juridicas_que_clasifiquen_como_mipyme_s_479976`
  - `Obligacion_en_caso_de_tratarse_una_operacion_del_concepto_s30_servicios_de_fletes_por_opera_69475a` —`referencia`→ `Restriccion_las_posiciones_arancelarias_de_los_bienes_no_correspondan_a_aquellas_comprendida_40b22e`
- **Nodos del subgrafo** (18; tipo | etiqueta | id):
  - Excepcion | Facultad condicionada — acceso a cambios para servicios a partir del 13/12/23 | `Excepcion_las_entidades_podran_dar_acceso_al_mercado_de_cambios_para_cursar_pagos_de_servi_eeb5ea`
  - Excepcion | Excepción servicios de aeronavegación | `Excepcion_quedan_exceptuadas_las_importaciones_realizadas_por_empresas_que_presten_servici_e227f4`
  - Obligacion | Plazo para fletes en importaciones de bienes | `Obligacion_en_caso_de_tratarse_una_operacion_del_concepto_s30_servicios_de_fletes_por_opera_69475a`
  - Obligacion | Documentación comprobante operación de servicio | `Obligacion_la_entidad_debera_contar_con_la_documentacion_que_demuestre_que_al_momento_de_la_7ec7bb`
  - Obligacion | Cumplimiento de requisitos normativos para acceso a cambios | `Obligacion_la_operacion_debe_cumplir_con_los_restantes_requisitos_normativos_aplicables_y_q_59e1bd`
  - Obligacion | Acceso al mercado de cambios para cartas de crédito | `Obligacion_las_entidades_financieras_tendran_acceso_al_mercado_de_cambios_para_cursar_pagos_3e7ec6`
  - Operacion | Cancelación de cartas de crédito | `Operacion_cancelacion_de_cartas_de_credito_fda215`
  - Operacion | Importación de aeronaves y partes | `Operacion_importacion_de_aeronaves_y_partes_70d94c`
  - Operacion | Pago a la vista de importación de bienes | `Operacion_pago_a_la_vista_de_importacion_de_bienes_45f1f9`
  - Operacion | Pago de servicios de no residentes | `Operacion_pago_de_servicios_de_no_residentes_8c6a60`
  - Restriccion | Fecha de embarque mínima — 14/04/25 | `Restriccion_bienes_que_hayan_sido_embarcados_en_origen_a_partir_del_14_04_25_8dd261`
  - Restriccion | Sujeto: personas humanas o jurídicas MiPyMe | `Restriccion_cursados_por_personas_humanas_o_personas_juridicas_que_clasifiquen_como_mipyme_s_479976`
  - Restriccion | Exclusión posiciones arancelarias punto 12.1 | `Restriccion_las_posiciones_arancelarias_de_los_bienes_no_correspondan_a_aquellas_comprendida_40b22e`
  - Sujeto | Entidades financieras | `Sujeto_entidad_financiera`
  - Sujeto | MiPyMEs | `Sujeto_mipyme`
  - Sujeto | Personas humanas | `Sujeto_persona_humana`
  - Sujeto | Personas jurídicas | `Sujeto_persona_juridica`
  - TextoOrdenado | Texto Ordenado de Exterior y Cambios | `TextoOrdenado_to_exterior_cambios_actual_pdf`
- **Aristas del subgrafo** (35; origen —predicado→ destino):
  - `Obligacion_en_caso_de_tratarse_una_operacion_del_concepto_s30_servicios_de_fletes_por_opera_69475a` —`aplica_a`→ `Sujeto_entidad_financiera`
  - `Obligacion_en_caso_de_tratarse_una_operacion_del_concepto_s30_servicios_de_fletes_por_opera_69475a` —`establecida_en`→ `TextoOrdenado_to_exterior_cambios_actual_pdf`
  - `Obligacion_en_caso_de_tratarse_una_operacion_del_concepto_s30_servicios_de_fletes_por_opera_69475a` —`referencia`→ `Operacion_pago_a_la_vista_de_importacion_de_bienes_45f1f9`
  - `Obligacion_en_caso_de_tratarse_una_operacion_del_concepto_s30_servicios_de_fletes_por_opera_69475a` —`referencia`→ `Restriccion_bienes_que_hayan_sido_embarcados_en_origen_a_partir_del_14_04_25_8dd261`
  - `Obligacion_en_caso_de_tratarse_una_operacion_del_concepto_s30_servicios_de_fletes_por_opera_69475a` —`referencia`→ `Restriccion_cursados_por_personas_humanas_o_personas_juridicas_que_clasifiquen_como_mipyme_s_479976`
  - `Obligacion_en_caso_de_tratarse_una_operacion_del_concepto_s30_servicios_de_fletes_por_opera_69475a` —`referencia`→ `Restriccion_las_posiciones_arancelarias_de_los_bienes_no_correspondan_a_aquellas_comprendida_40b22e`
  - `Obligacion_en_caso_de_tratarse_una_operacion_del_concepto_s30_servicios_de_fletes_por_opera_69475a` —`regula`→ `Operacion_cancelacion_de_cartas_de_credito_fda215`
  - `Obligacion_la_entidad_debera_contar_con_la_documentacion_que_demuestre_que_al_momento_de_la_7ec7bb` —`aplica_a`→ `Sujeto_entidad_financiera`
  - `Obligacion_la_entidad_debera_contar_con_la_documentacion_que_demuestre_que_al_momento_de_la_7ec7bb` —`establecida_en`→ `TextoOrdenado_to_exterior_cambios_actual_pdf`
  - `Obligacion_la_entidad_debera_contar_con_la_documentacion_que_demuestre_que_al_momento_de_la_7ec7bb` —`referencia`→ `Excepcion_las_entidades_podran_dar_acceso_al_mercado_de_cambios_para_cursar_pagos_de_servi_eeb5ea`
  - `Obligacion_la_entidad_debera_contar_con_la_documentacion_que_demuestre_que_al_momento_de_la_7ec7bb` —`referencia`→ `Obligacion_la_operacion_debe_cumplir_con_los_restantes_requisitos_normativos_aplicables_y_q_59e1bd`
  - `Obligacion_la_entidad_debera_contar_con_la_documentacion_que_demuestre_que_al_momento_de_la_7ec7bb` —`referencia`→ `Operacion_pago_de_servicios_de_no_residentes_8c6a60`
  - `Obligacion_la_entidad_debera_contar_con_la_documentacion_que_demuestre_que_al_momento_de_la_7ec7bb` —`regula`→ `Operacion_cancelacion_de_cartas_de_credito_fda215`
  - `Obligacion_las_entidades_financieras_tendran_acceso_al_mercado_de_cambios_para_cursar_pagos_3e7ec6` —`aplica_a`→ `Sujeto_entidad_financiera`
  - `Obligacion_las_entidades_financieras_tendran_acceso_al_mercado_de_cambios_para_cursar_pagos_3e7ec6` —`establecida_en`→ `TextoOrdenado_to_exterior_cambios_actual_pdf`
  - `Obligacion_las_entidades_financieras_tendran_acceso_al_mercado_de_cambios_para_cursar_pagos_3e7ec6` —`regula`→ `Operacion_cancelacion_de_cartas_de_credito_fda215`
  - `Operacion_cancelacion_de_cartas_de_credito_fda215` —`establecida_en`→ `TextoOrdenado_to_exterior_cambios_actual_pdf`
  - `Operacion_pago_a_la_vista_de_importacion_de_bienes_45f1f9` —`establecida_en`→ `TextoOrdenado_to_exterior_cambios_actual_pdf`
  - `Restriccion_bienes_que_hayan_sido_embarcados_en_origen_a_partir_del_14_04_25_8dd261` —`aplica_a`→ `Sujeto_mipyme`
  - `Restriccion_bienes_que_hayan_sido_embarcados_en_origen_a_partir_del_14_04_25_8dd261` —`aplica_a`→ `Sujeto_persona_humana`
  - `Restriccion_bienes_que_hayan_sido_embarcados_en_origen_a_partir_del_14_04_25_8dd261` —`aplica_a`→ `Sujeto_persona_juridica`
  - `Restriccion_bienes_que_hayan_sido_embarcados_en_origen_a_partir_del_14_04_25_8dd261` —`establecida_en`→ `TextoOrdenado_to_exterior_cambios_actual_pdf`
  - `Restriccion_bienes_que_hayan_sido_embarcados_en_origen_a_partir_del_14_04_25_8dd261` —`limita`→ `Operacion_pago_a_la_vista_de_importacion_de_bienes_45f1f9`
  - `Restriccion_cursados_por_personas_humanas_o_personas_juridicas_que_clasifiquen_como_mipyme_s_479976` —`aplica_a`→ `Sujeto_mipyme`
  - `Restriccion_cursados_por_personas_humanas_o_personas_juridicas_que_clasifiquen_como_mipyme_s_479976` —`aplica_a`→ `Sujeto_persona_humana`
  - `Restriccion_cursados_por_personas_humanas_o_personas_juridicas_que_clasifiquen_como_mipyme_s_479976` —`aplica_a`→ `Sujeto_persona_juridica`
  - `Restriccion_cursados_por_personas_humanas_o_personas_juridicas_que_clasifiquen_como_mipyme_s_479976` —`establecida_en`→ `TextoOrdenado_to_exterior_cambios_actual_pdf`
  - `Restriccion_cursados_por_personas_humanas_o_personas_juridicas_que_clasifiquen_como_mipyme_s_479976` —`limita`→ `Operacion_pago_a_la_vista_de_importacion_de_bienes_45f1f9`
  - `Restriccion_las_posiciones_arancelarias_de_los_bienes_no_correspondan_a_aquellas_comprendida_40b22e` —`aplica_a`→ `Sujeto_mipyme`
  - `Restriccion_las_posiciones_arancelarias_de_los_bienes_no_correspondan_a_aquellas_comprendida_40b22e` —`aplica_a`→ `Sujeto_persona_humana`
  - `Restriccion_las_posiciones_arancelarias_de_los_bienes_no_correspondan_a_aquellas_comprendida_40b22e` —`aplica_a`→ `Sujeto_persona_juridica`
  - `Restriccion_las_posiciones_arancelarias_de_los_bienes_no_correspondan_a_aquellas_comprendida_40b22e` —`establecida_en`→ `TextoOrdenado_to_exterior_cambios_actual_pdf`
  - `Restriccion_las_posiciones_arancelarias_de_los_bienes_no_correspondan_a_aquellas_comprendida_40b22e` —`limita`→ `Operacion_pago_a_la_vista_de_importacion_de_bienes_45f1f9`
  - `Restriccion_las_posiciones_arancelarias_de_los_bienes_no_correspondan_a_aquellas_comprendida_40b22e` —`referencia`→ `Excepcion_quedan_exceptuadas_las_importaciones_realizadas_por_empresas_que_presten_servici_e227f4`
  - `Restriccion_las_posiciones_arancelarias_de_los_bienes_no_correspondan_a_aquellas_comprendida_40b22e` —`referencia`→ `Operacion_importacion_de_aeronaves_y_partes_70d94c`
- **Cantidad**: 18 nodos, 35 aristas.
- **Veredicto definitivo por grafo**: KG-Base (`run_3`): **parcial** · KG-Reextraído (`v2`): **incorrecto** · KG-Refinado (`v3`): **parcial**.
- **Traza correcta**: no existe (ningún grafo con veredicto correcto). Las trazas de los tres veredictos están persistidas en `data/experiment/ev2_corrida/trazas/ev2_base_run3/EV2F-014.json`, `data/experiment/ev2_corrida/trazas/ev2_base_v2/EV2F-014.json`, `data/experiment/ev2_corrida/trazas/ev2_base_v3/EV2F-014.json`.

### I.6 Candidato 5 — EV2F-033, par ric:12.4 → ric:1.1

- **Pregunta** (`EV2F-033`): «Desde el período de información de abril de 2024, ¿qué cambió en el envío de información consolidada con código de consolidación 3 y qué tratamiento particular recibe el ratio de apalancamiento?»
- **Ancla** (`gold.ancla`): `ric:12.4`. Punto de origen del par: `ric:12.4` (el ancla misma).
- **Punto referido**: `ric:1.1`. Evidencia textual de la remisión (`referencias_remisiones.json`, campo `evidencia`): «atos del mes de cierre de trimestre) y su vencimiento según punto 1.1. del Régimen Informa»
- **Texto verbatim de ambos puntos**:
  - Unidad E0 `ric::12.4` — `TO_regimen_informativo_contable_mensual_actual.pdf`, página(s) [58, 59], 1834 caracteres propios (`data/experiment/reextraccion_v2/e0_chunking/salida/chunks_ric.json`, campo `texto`):

    ```
    12.4. Suspensión de la observancia de las regulaciones técnicas sobre base consolidada
    trimestral (punto 6.1. de las normas sobre “Supervisión consolidada”).
    A partir del período de información abril/24:
    - Se suspende el envío de informaciones con código de consolidación 3 -con la ex-
    cepción prevista para Ratio de apalancamiento-, siendo marzo/24 el último período
    trimestral que corresponde informar con este nivel de consolidación;
    - En la información sobre base consolidada mensual (códigos de consolidación 2 ó 9)
    se incluirán -de corresponder- las operaciones de los entes a que refieren los incisos
    i), ii) y iii) del primer párrafo del punto 6.2. de las normas sobre “Supervisión conso-
    lidada.
    - Las entidades financieras que hasta el 31/03/24 informaban únicamente códigos de
    consolidación 1 y 3, de mantenerse esta situación de consolidación, pasarán a in-
    formar:
    a) códigos 1 y 9 sólo si consolidan con alguno de los entes a que refieren los incisos
    i), ii) y iii) del punto 6.2. de las normas citadas;
    b) en caso contrario, código 0.
    - Ratio de apalancamiento (Sección 10.)
    a) Conforme a lo dispuesto en el punto 6.2. último párrafo de las normas sobre
    “Supervisión consolidada”, mantendrá su frecuencia trimestral (datos del mes
    de cierre de trimestre) y su vencimiento según punto 1.1. del Régimen Informa-
    tivo para Supervisión;
    b) Se continuará informando código de consolidación 3; no obstante, las opera-
    ciones a incluir serán las que correspondan al perímetro de consolidación men-
    sual, considerando de corresponder, los sujetos previstos en el punto 6.2. de
    las normas citadas.
    (Sección 11.)
    De corresponder, la consolidación mensual (código 2) considerará las operaciones
    de los entes a que refieren los incisos i), ii) y iii) del primer párrafo del punto 6.2. de
    las normas sobre “Supervisión consolidada”.
    ```
  - Unidad E0 `ric::1.1` — `TO_regimen_informativo_contable_mensual_actual.pdf`, página(s) [3], 992 caracteres propios (`data/experiment/reextraccion_v2/e0_chunking/salida/chunks_ric.json`, campo `texto`):

    ```
    1.1. La información tendrá frecuencia mensual y se integrará con datos referidos al mes bajo aná-
    lisis, excepto las siguientes informaciones que tendrán frecuencia trimestral y se integrarán de
    la siguiente manera:
    Con los datos correspondientes al último mes de cada trimestre (marzo, junio, septiembre y
    diciembre):
    - Datos complementarios vinculados al cálculo de la exigencia por riesgo de mercado (puntos
    4.3., 4.4. y 4.5. de la Sección 4.) en base individual y consolidado mensual (códigos de con-
    solidación 0 o 1 y 2);
    - La información sobre Ratio de apalancamiento (Sección 10.) en base individual (códigos de
    consolidación 0 o 1);
    Con los datos correspondientes al mes siguiente de cada trimestre (abril, julio, octubre
    y enero)
    - Cálculo del riesgo de tasa de interés en la cartera de inversión - Medida de riesgo EVE es-
    tandarizada (Sección 11.) en base individual y consolidado mensual (códigos de consolida-
    ción 0 o 1 y 2) y su respectivo total de control (partida 70500000).
    ```
- **Arista(s) que siguen la remisión** (4):
  - `Obligacion_conforme_a_lo_dispuesto_en_el_punto_6_2_ultimo_parrafo_de_las_normas_sobre_super_e980e7` —`referencia`→ `Obligacion_calculo_del_riesgo_de_tasa_de_interes_en_la_cartera_de_inversion_medida_de_riesg_7329f8`
  - `Obligacion_conforme_a_lo_dispuesto_en_el_punto_6_2_ultimo_parrafo_de_las_normas_sobre_super_e980e7` —`referencia`→ `Obligacion_datos_complementarios_vinculados_al_calculo_de_la_exigencia_por_riesgo_de_mercad_86301c`
  - `Obligacion_conforme_a_lo_dispuesto_en_el_punto_6_2_ultimo_parrafo_de_las_normas_sobre_super_e980e7` —`referencia`→ `Obligacion_la_informacion_sobre_ratio_de_apalancamiento_seccion_10_en_base_individual_codig_5d28f7`
  - `Obligacion_conforme_a_lo_dispuesto_en_el_punto_6_2_ultimo_parrafo_de_las_normas_sobre_super_e980e7` —`referencia`→ `Obligacion_la_informacion_tendra_frecuencia_mensual_y_se_integrara_con_datos_referidos_al_m_9721ae`
- **Nodos del subgrafo** (23; tipo | etiqueta | id):
  - Excepcion | Excepción — importes con signo negativo permitidos | `Excepcion_aquellos_casos_en_que_expresamente_se_prevea_la_posibilidad_de_que_se_informen_c_40cb46`
  - Obligacion | Cálculo riesgo tasa de interés trimestral | `Obligacion_calculo_del_riesgo_de_tasa_de_interes_en_la_cartera_de_inversion_medida_de_riesg_7329f8`
  - Obligacion | Ratio apalancamiento frecuencia trimestral | `Obligacion_conforme_a_lo_dispuesto_en_el_punto_6_2_ultimo_parrafo_de_las_normas_sobre_super_e980e7`
  - Obligacion | Datos complementarios riesgo de mercado trimestral | `Obligacion_datos_complementarios_vinculados_al_calculo_de_la_exigencia_por_riesgo_de_mercad_86301c`
  - Obligacion | Consolidación mensual código 2 Sección 11 | `Obligacion_de_corresponder_la_consolidacion_mensual_codigo_2_considerara_las_operaciones_de_2d461b`
  - Obligacion | Aplicación de instrucciones de cómputo | `Obligacion_deberan_tenerse_en_cuenta_las_instrucciones_de_computo_del_presente_punto_y_los__373b06`
  - Obligacion | Custodia de datos en base — disponibilidad SEFyC | `Obligacion_el_resto_de_los_dias_permaneceran_en_una_base_a_disposicion_de_la_sefyc_9577d6`
  - Obligacion | Incluir operaciones entes consolidación mensual | `Obligacion_en_la_informacion_sobre_base_consolidada_mensual_codigos_de_consolidacion_2_o_9__025ef4`
  - Obligacion | Información Ratio de apalancamiento trimestral | `Obligacion_la_informacion_sobre_ratio_de_apalancamiento_seccion_10_en_base_individual_codig_5d28f7`
  - Obligacion | Información con frecuencia mensual | `Obligacion_la_informacion_tendra_frecuencia_mensual_y_se_integrara_con_datos_referidos_al_m_9721ae`
  - Obligacion | Transición códigos consolidación para EF | `Obligacion_las_entidades_financieras_que_hasta_el_31_03_24_informaban_unicamente_codigos_de_6eb3d2`
  - Obligacion | Envío mensual de datos por riesgo de mercado | `Obligacion_se_complementara_con_el_envio_mensual_de_los_datos_que_se_explicitan_en_el_prese_08b2b8`
  - Obligacion | Informar código consolidación 3 Ratio apalancamiento | `Obligacion_se_continuara_informando_codigo_de_consolidacion_3_no_obstante_las_operaciones_a_4d209f`
  - Obligacion | Informe de últimos días — información mensual | `Obligacion_se_informaran_unicamente_los_correspondientes_al_ultimo_dia_de_cada_periodo_de_i_ae0199`
  - Operacion | Cálculo diario de posiciones e integración | `Operacion_calculo_diario_de_posiciones_e_integracion_56ed8f`
  - Operacion | Presentación información consolidación mensual | `Operacion_presentacion_informacion_consolidacion_mensual_357d63`
  - Operacion | Presentación información consolidación trimestral | `Operacion_presentacion_informacion_consolidacion_trimestral_19a490`
  - Operacion | Presentación Ratio apalancamiento | `Operacion_presentacion_ratio_apalancamiento_2e14d6`
  - Restriccion | Consignación de importes sin signo | `Restriccion_los_importes_se_consignaran_sin_signo_excepto_para_aquellos_casos_en_que_expresa_e79e8a`
  - Restriccion | Suspensión envío consolidación 3 desde abril/24 | `Restriccion_se_suspende_el_envio_de_informaciones_con_codigo_de_consolidacion_3_con_la_excep_bd1f83`
  - Sujeto | Entidades financieras | `Sujeto_entidad_financiera`
  - Sujeto | Entidades comprendidas (Régimen Informativo) | `Sujeto_rol_entidad_comprendida_reginf`
  - TextoOrdenado | Texto Ordenado Régimen Informativo Contable | `TextoOrdenado_to_regimen_informativo_contable_mensual_actual_pdf`
- **Aristas del subgrafo** (36; origen —predicado→ destino):
  - `Obligacion_conforme_a_lo_dispuesto_en_el_punto_6_2_ultimo_parrafo_de_las_normas_sobre_super_e980e7` —`aplica_a`→ `Sujeto_rol_entidad_comprendida_reginf`
  - `Obligacion_conforme_a_lo_dispuesto_en_el_punto_6_2_ultimo_parrafo_de_las_normas_sobre_super_e980e7` —`establecida_en`→ `TextoOrdenado_to_regimen_informativo_contable_mensual_actual_pdf`
  - `Obligacion_conforme_a_lo_dispuesto_en_el_punto_6_2_ultimo_parrafo_de_las_normas_sobre_super_e980e7` —`referencia`→ `Obligacion_calculo_del_riesgo_de_tasa_de_interes_en_la_cartera_de_inversion_medida_de_riesg_7329f8`
  - `Obligacion_conforme_a_lo_dispuesto_en_el_punto_6_2_ultimo_parrafo_de_las_normas_sobre_super_e980e7` —`referencia`→ `Obligacion_datos_complementarios_vinculados_al_calculo_de_la_exigencia_por_riesgo_de_mercad_86301c`
  - `Obligacion_conforme_a_lo_dispuesto_en_el_punto_6_2_ultimo_parrafo_de_las_normas_sobre_super_e980e7` —`referencia`→ `Obligacion_la_informacion_sobre_ratio_de_apalancamiento_seccion_10_en_base_individual_codig_5d28f7`
  - `Obligacion_conforme_a_lo_dispuesto_en_el_punto_6_2_ultimo_parrafo_de_las_normas_sobre_super_e980e7` —`referencia`→ `Obligacion_la_informacion_tendra_frecuencia_mensual_y_se_integrara_con_datos_referidos_al_m_9721ae`
  - `Obligacion_de_corresponder_la_consolidacion_mensual_codigo_2_considerara_las_operaciones_de_2d461b` —`aplica_a`→ `Sujeto_rol_entidad_comprendida_reginf`
  - `Obligacion_de_corresponder_la_consolidacion_mensual_codigo_2_considerara_las_operaciones_de_2d461b` —`establecida_en`→ `TextoOrdenado_to_regimen_informativo_contable_mensual_actual_pdf`
  - `Obligacion_en_la_informacion_sobre_base_consolidada_mensual_codigos_de_consolidacion_2_o_9__025ef4` —`aplica_a`→ `Sujeto_rol_entidad_comprendida_reginf`
  - `Obligacion_en_la_informacion_sobre_base_consolidada_mensual_codigos_de_consolidacion_2_o_9__025ef4` —`establecida_en`→ `TextoOrdenado_to_regimen_informativo_contable_mensual_actual_pdf`
  - `Obligacion_las_entidades_financieras_que_hasta_el_31_03_24_informaban_unicamente_codigos_de_6eb3d2` —`aplica_a`→ `Sujeto_entidad_financiera`
  - `Obligacion_las_entidades_financieras_que_hasta_el_31_03_24_informaban_unicamente_codigos_de_6eb3d2` —`establecida_en`→ `TextoOrdenado_to_regimen_informativo_contable_mensual_actual_pdf`
  - `Obligacion_se_continuara_informando_codigo_de_consolidacion_3_no_obstante_las_operaciones_a_4d209f` —`aplica_a`→ `Sujeto_rol_entidad_comprendida_reginf`
  - `Obligacion_se_continuara_informando_codigo_de_consolidacion_3_no_obstante_las_operaciones_a_4d209f` —`establecida_en`→ `TextoOrdenado_to_regimen_informativo_contable_mensual_actual_pdf`
  - `Operacion_presentacion_informacion_consolidacion_mensual_357d63` —`requiere`→ `Obligacion_de_corresponder_la_consolidacion_mensual_codigo_2_considerara_las_operaciones_de_2d461b`
  - `Operacion_presentacion_informacion_consolidacion_mensual_357d63` —`requiere`→ `Obligacion_en_la_informacion_sobre_base_consolidada_mensual_codigos_de_consolidacion_2_o_9__025ef4`
  - `Operacion_presentacion_informacion_consolidacion_trimestral_19a490` —`establecida_en`→ `TextoOrdenado_to_regimen_informativo_contable_mensual_actual_pdf`
  - `Operacion_presentacion_ratio_apalancamiento_2e14d6` —`requiere`→ `Obligacion_conforme_a_lo_dispuesto_en_el_punto_6_2_ultimo_parrafo_de_las_normas_sobre_super_e980e7`
  - `Restriccion_se_suspende_el_envio_de_informaciones_con_codigo_de_consolidacion_3_con_la_excep_bd1f83` —`aplica_a`→ `Sujeto_rol_entidad_comprendida_reginf`
  - `Restriccion_se_suspende_el_envio_de_informaciones_con_codigo_de_consolidacion_3_con_la_excep_bd1f83` —`establecida_en`→ `TextoOrdenado_to_regimen_informativo_contable_mensual_actual_pdf`
  - `Restriccion_se_suspende_el_envio_de_informaciones_con_codigo_de_consolidacion_3_con_la_excep_bd1f83` —`prohibe`→ `Operacion_presentacion_informacion_consolidacion_trimestral_19a490`
  - `Obligacion_calculo_del_riesgo_de_tasa_de_interes_en_la_cartera_de_inversion_medida_de_riesg_7329f8` —`aplica_a`→ `Sujeto_rol_entidad_comprendida_reginf`
  - `Obligacion_calculo_del_riesgo_de_tasa_de_interes_en_la_cartera_de_inversion_medida_de_riesg_7329f8` —`establecida_en`→ `TextoOrdenado_to_regimen_informativo_contable_mensual_actual_pdf`
  - `Obligacion_datos_complementarios_vinculados_al_calculo_de_la_exigencia_por_riesgo_de_mercad_86301c` —`aplica_a`→ `Sujeto_rol_entidad_comprendida_reginf`
  - `Obligacion_datos_complementarios_vinculados_al_calculo_de_la_exigencia_por_riesgo_de_mercad_86301c` —`establecida_en`→ `TextoOrdenado_to_regimen_informativo_contable_mensual_actual_pdf`
  - `Obligacion_datos_complementarios_vinculados_al_calculo_de_la_exigencia_por_riesgo_de_mercad_86301c` —`referencia`→ `Excepcion_aquellos_casos_en_que_expresamente_se_prevea_la_posibilidad_de_que_se_informen_c_40cb46`
  - `Obligacion_datos_complementarios_vinculados_al_calculo_de_la_exigencia_por_riesgo_de_mercad_86301c` —`referencia`→ `Obligacion_deberan_tenerse_en_cuenta_las_instrucciones_de_computo_del_presente_punto_y_los__373b06`
  - `Obligacion_datos_complementarios_vinculados_al_calculo_de_la_exigencia_por_riesgo_de_mercad_86301c` —`referencia`→ `Obligacion_el_resto_de_los_dias_permaneceran_en_una_base_a_disposicion_de_la_sefyc_9577d6`
  - `Obligacion_datos_complementarios_vinculados_al_calculo_de_la_exigencia_por_riesgo_de_mercad_86301c` —`referencia`→ `Obligacion_se_complementara_con_el_envio_mensual_de_los_datos_que_se_explicitan_en_el_prese_08b2b8`
  - `Obligacion_datos_complementarios_vinculados_al_calculo_de_la_exigencia_por_riesgo_de_mercad_86301c` —`referencia`→ `Obligacion_se_informaran_unicamente_los_correspondientes_al_ultimo_dia_de_cada_periodo_de_i_ae0199`
  - `Obligacion_datos_complementarios_vinculados_al_calculo_de_la_exigencia_por_riesgo_de_mercad_86301c` —`referencia`→ `Operacion_calculo_diario_de_posiciones_e_integracion_56ed8f`
  - `Obligacion_datos_complementarios_vinculados_al_calculo_de_la_exigencia_por_riesgo_de_mercad_86301c` —`referencia`→ `Restriccion_los_importes_se_consignaran_sin_signo_excepto_para_aquellos_casos_en_que_expresa_e79e8a`
  - `Obligacion_la_informacion_sobre_ratio_de_apalancamiento_seccion_10_en_base_individual_codig_5d28f7` —`aplica_a`→ `Sujeto_rol_entidad_comprendida_reginf`
  - `Obligacion_la_informacion_sobre_ratio_de_apalancamiento_seccion_10_en_base_individual_codig_5d28f7` —`establecida_en`→ `TextoOrdenado_to_regimen_informativo_contable_mensual_actual_pdf`
  - `Obligacion_la_informacion_tendra_frecuencia_mensual_y_se_integrara_con_datos_referidos_al_m_9721ae` —`aplica_a`→ `Sujeto_rol_entidad_comprendida_reginf`
  - `Obligacion_la_informacion_tendra_frecuencia_mensual_y_se_integrara_con_datos_referidos_al_m_9721ae` —`establecida_en`→ `TextoOrdenado_to_regimen_informativo_contable_mensual_actual_pdf`
- **Cantidad**: 23 nodos, 36 aristas.
- **Veredicto definitivo por grafo**: KG-Base (`run_3`): **correcto** · KG-Reextraído (`v2`): **correcto** · KG-Refinado (`v3`): **correcto**.
- **Traza(s) de la(s) corrida(s) con veredicto correcto**:
  - KG-Base: `data/experiment/ev2_corrida/trazas/ev2_base_run3/EV2F-033.json` (existe: sí)
  - KG-Reextraído: `data/experiment/ev2_corrida/trazas/ev2_base_v2/EV2F-033.json` (existe: sí)
  - KG-Refinado: `data/experiment/ev2_corrida/trazas/ev2_base_v3/EV2F-033.json` (existe: sí)

### I.7 Referencia para comparar — caso actual de la figura (las seis variantes de la cláusula del 125 %)

Caso hoy en `docs/tesis/main.tex` (Figura `fig:clausula125`,
`docs/tesis/figuras/figura_125_r1.{svg,png}`): los 6 nodos del test de
respuesta conocida T2
(`data/experiment/reextraccion_v2/corpus_v2/salida_r1/tests_respuesta_conocida_r1.json`,
clave `T2_clausula_125`) en 5 puntos del TO de Exterior y Cambios.

- **Pregunta asociada**: no tiene. Ninguna de las 40 preguntas EV2 tiene
  ancla en `ext:3.11.3.2`, `ext:7.5.3`, `ext:7.8.5.1`, `ext:7.9.5` ni
  `ext:7.11.5` (verificado sobre `gold.ancla` de las 40). En consecuencia
  no hay veredicto por grafo ni traza asociada (campos no aplicables).
- **Puntos y texto verbatim** (unidades E0, mismas rutas que arriba):
  - Unidad E0 `ext::3.11.3.2` — `TO_exterior_cambios_actual.pdf`, página(s) [35], 327 caracteres propios:

    ```
    3.11.3.2. las garantías acumuladas en moneda extranjera no superen el equivalente
    al 125% (ciento veinticinco por ciento) de los servicios por capital e
    intereses a abonar en el mes corriente y los siguientes 6 (seis) meses
    calendario, de acuerdo con el cronograma de vencimientos de los servicios
    acordados con los acreedores.
    ```
  - Unidad E0 `ext::7.5.3` — `TO_exterior_cambios_actual.pdf`, página(s) [87], 771 caracteres propios:

    ```
    7.5.3. Permisos cuyos fondos se encuentran retenidos en las cuentas asociadas a los
    endeudamientos financieros referidas en los puntos 7.3.5., 7.9. y 7.11. y las
    prefinanciaciones de exportaciones comprendidas en el punto 7.8.5.
    En caso de que la fecha hasta la cual los cobros de un permiso deben permanecer
    depositados en virtud de lo exigido en el contrato del financiamiento fuese posterior al
    vencimiento del plazo para la liquidación de divisas del permiso, el exportador podrá
    solicitar que este plazo sea ampliado hasta el quinto día hábil posterior a dicha fecha.
    Esta opción estará disponible hasta alcanzar el 125% (ciento veinticinco por ciento) de
    los servicios por capital e intereses a abonar en el mes corriente y los siguientes 6
    (seis) meses calendario.
    ```
  - Unidad E0 `ext::7.8.5.1` — `TO_exterior_cambios_actual.pdf`, página(s) [94], 1095 caracteres propios:

    ```
    7.8.5.1. acumular los fondos originados en el cobro de exportaciones de bienes y
    servicios del deudor en cuentas en moneda extranjera abiertas en entidades
    financieras locales o en el exterior destinadas a garantizar la cancelación de
    los vencimientos de dicha prefinanciación según lo previsto en el contrato de
    financiamiento.
    Esta opción estará disponible hasta alcanzar el 125% (ciento veinticinco por
    ciento) de los servicios por capital e intereses a abonar en el mes corriente y
    los siguientes 6 (seis) meses calendario, de acuerdo con el cronograma de
    vencimientos de los servicios acordados con los acreedores, debiendo los
    fondos excedentes ser ingresados y liquidados en el mercado de cambios
    dentro de los plazos previstos en las normas generales en la materia.
    En caso de que la fecha hasta la cual los cobros deben permanecer deposi-
    tados en virtud de lo exigido en el contrato del financiamiento fuese posterior
    al vencimiento del plazo para la liquidación de divisas, el exportador podrá
    solicitar que este plazo sea ampliado hasta el quinto día hábil posterior a di-
    cha fecha.
    ```
  - Unidad E0 `ext::7.9.5` — `TO_exterior_cambios_actual.pdf`, página(s) [99], 1245 caracteres propios:

    ```
    7.9.5. Por los endeudamientos financieros comprendidos en el punto 3.5. que hayan sido
    ingresadas y liquidadas por el mercado de cambios a partir del 07/01/21 (únicamente a
    partir del 08/08/25 en el caso de aquellos comprendidos en el punto 7.9.1.4.) se
    admitirá que los fondos originados en el cobro de exportaciones de bienes y servicios
    del deudor sean acumulados en cuentas del exterior y/o el país destinadas a garantizar
    la cancelación de los vencimientos de la deuda emitida.
    Esta opción estará disponible hasta alcanzar el 125% (ciento veinticinco por ciento) de
    los servicios por capital e intereses a abonar en el mes corriente y los siguientes 6
    (seis) meses calendario, de acuerdo con el cronograma de vencimientos de los
    servicios acordados con los acreedores, debiendo los fondos excedentes ser
    ingresados y liquidados en el mercado de cambios dentro de los plazos previstos en
    las normas generales en la materia.
    En caso de que la fecha hasta la cual los cobros deben permanecer depositados en
    virtud de lo exigido en el contrato del financiamiento fuese posterior al vencimiento del
    plazo para la liquidación de divisas, el exportador podrá solicitar que este plazo sea
    ampliado hasta el quinto día hábil posterior a dicha fecha.
    ```
  - Unidad E0 `ext::7.11.5` — `TO_exterior_cambios_actual.pdf`, página(s) [107], 1073 caracteres propios:

    ```
    7.11.5. Por las emisiones de títulos de deudas comprendidas en los puntos 7.11.1.5. y
    7.11.1.6. se admitirá que los fondos originados en el cobro de exportaciones de
    bienes y servicios del deudor sean acumulados en cuentas del exterior y/o el país
    destinadas a garantizar la cancelación de los vencimientos de la deuda emitida.
    Esta opción estará disponible hasta alcanzar el 125% (ciento veinticinco por ciento)
    del capital e intereses a abonar en el mes corriente y los siguientes 6 (seis) meses
    calendario, de acuerdo con el cronograma de vencimientos de los servicios
    acordados con los acreedores, debiendo los fondos excedentes ser ingresados y
    liquidados en el mercado de cambios dentro de los plazos previstos en las normas
    generales en la materia.
    En caso de que la fecha hasta la cual los cobros deben permanecer depositados en
    virtud de lo exigido en el contrato del financiamiento fuese posterior al vencimiento
    del plazo para la liquidación de divisas, el exportador podrá solicitar que este plazo
    sea ampliado hasta el quinto día hábil posterior a dicha fecha.
    ```
- **Subgrafo** (reconstrucción determinística desde `salida_r1/kg.json`:
  los 6 nodos de T2 más todas sus aristas salientes y los nodos destino;
  coincide con la leyenda de la figura, que muestra «las relaciones
  extraídas de cada variante»):
- **Nodos del subgrafo** (15; tipo | etiqueta | id):
  - Excepcion | Ampliación disponible hasta 125% servicios 6 meses | `Excepcion_la_opcion_de_ampliacion_estara_disponible_hasta_alcanzar_el_125_ciento_veinticin_6d94e9`
  - Obligacion | Ampliación hasta quinto día hábil posterior a fecha | `Obligacion_en_caso_de_que_la_fecha_hasta_la_cual_los_cobros_de_un_permiso_deben_permanecer__38b169`
  - Operacion | Acumulación de fondos de exportación en cuentas del exterior | `Operacion_acumulacion_de_fondos_de_exportacion_en_cuentas_del_exterior_8b4b6b`
  - Operacion | Acumulación de fondos exportaciones en cuenta extranjera | `Operacion_acumulacion_de_fondos_exportaciones_en_cuenta_extranjera_68ac15`
  - Operacion | Acumulación fondos cobro exportaciones | `Operacion_acumulacion_fondos_cobro_exportaciones_52a866`
  - Operacion | Constitución de garantías en moneda extranjera | `Operacion_constitucion_de_garantias_en_moneda_extranjera_984924`
  - Operacion | Solicitud de ampliación de plazo de liquidación | `Operacion_solicitud_de_ampliacion_de_plazo_de_liquidacion_ba5826`
  - Restriccion | Tope 125% servicios garantía prefinanciación | `Restriccion_esta_opcion_estara_disponible_hasta_alcanzar_el_125_ciento_veinticinco_por_cient_66fe20`
  - Restriccion | Tope 125% servicios capital intereses | `Restriccion_la_ampliacion_no_podra_exceder_el_125_ciento_veinticinco_por_ciento_de_los_servi_4af187`
  - Restriccion | Tope 125% servicios capital e intereses — garantías acumuladas | `Restriccion_las_garantias_acumuladas_en_moneda_extranjera_no_superen_el_equivalente_al_125_c_7e9ae0`
  - Restriccion | Límite acumulación fondos 125% capital e intereses | `Restriccion_los_fondos_originados_en_el_cobro_de_exportaciones_de_bienes_y_servicios_del_deu_dc9339`
  - Restriccion | Tope acumulación 125% servicios deuda | `Restriccion_los_fondos_originados_en_el_cobro_de_exportaciones_podran_ser_acumulados_hasta_a_3d8566`
  - Sujeto | Emisores de títulos de deuda | `Sujeto_emisor_de_titulos_de_deuda`
  - Sujeto | Entidades autorizadas a operar en cambios (Exterior) | `Sujeto_rol_entidad_autorizada_exterior`
  - TextoOrdenado | Texto Ordenado de Exterior y Cambios | `TextoOrdenado_to_exterior_cambios_actual_pdf`
- **Aristas del subgrafo** (14; origen —predicado→ destino):
  - `Excepcion_la_opcion_de_ampliacion_estara_disponible_hasta_alcanzar_el_125_ciento_veinticin_6d94e9` —`exceptua_obligacion`→ `Obligacion_en_caso_de_que_la_fecha_hasta_la_cual_los_cobros_de_un_permiso_deben_permanecer__38b169`
  - `Restriccion_esta_opcion_estara_disponible_hasta_alcanzar_el_125_ciento_veinticinco_por_cient_66fe20` —`establecida_en`→ `TextoOrdenado_to_exterior_cambios_actual_pdf`
  - `Restriccion_esta_opcion_estara_disponible_hasta_alcanzar_el_125_ciento_veinticinco_por_cient_66fe20` —`limita`→ `Operacion_acumulacion_de_fondos_exportaciones_en_cuenta_extranjera_68ac15`
  - `Restriccion_la_ampliacion_no_podra_exceder_el_125_ciento_veinticinco_por_ciento_de_los_servi_4af187` —`establecida_en`→ `TextoOrdenado_to_exterior_cambios_actual_pdf`
  - `Restriccion_la_ampliacion_no_podra_exceder_el_125_ciento_veinticinco_por_ciento_de_los_servi_4af187` —`limita`→ `Operacion_solicitud_de_ampliacion_de_plazo_de_liquidacion_ba5826`
  - `Restriccion_las_garantias_acumuladas_en_moneda_extranjera_no_superen_el_equivalente_al_125_c_7e9ae0` —`aplica_a`→ `Sujeto_rol_entidad_autorizada_exterior`
  - `Restriccion_las_garantias_acumuladas_en_moneda_extranjera_no_superen_el_equivalente_al_125_c_7e9ae0` —`establecida_en`→ `TextoOrdenado_to_exterior_cambios_actual_pdf`
  - `Restriccion_las_garantias_acumuladas_en_moneda_extranjera_no_superen_el_equivalente_al_125_c_7e9ae0` —`limita`→ `Operacion_constitucion_de_garantias_en_moneda_extranjera_984924`
  - `Restriccion_los_fondos_originados_en_el_cobro_de_exportaciones_de_bienes_y_servicios_del_deu_dc9339` —`aplica_a`→ `Sujeto_emisor_de_titulos_de_deuda`
  - `Restriccion_los_fondos_originados_en_el_cobro_de_exportaciones_de_bienes_y_servicios_del_deu_dc9339` —`establecida_en`→ `TextoOrdenado_to_exterior_cambios_actual_pdf`
  - `Restriccion_los_fondos_originados_en_el_cobro_de_exportaciones_de_bienes_y_servicios_del_deu_dc9339` —`limita`→ `Operacion_acumulacion_de_fondos_de_exportacion_en_cuentas_del_exterior_8b4b6b`
  - `Restriccion_los_fondos_originados_en_el_cobro_de_exportaciones_podran_ser_acumulados_hasta_a_3d8566` —`aplica_a`→ `Sujeto_rol_entidad_autorizada_exterior`
  - `Restriccion_los_fondos_originados_en_el_cobro_de_exportaciones_podran_ser_acumulados_hasta_a_3d8566` —`establecida_en`→ `TextoOrdenado_to_exterior_cambios_actual_pdf`
  - `Restriccion_los_fondos_originados_en_el_cobro_de_exportaciones_podran_ser_acumulados_hasta_a_3d8566` —`limita`→ `Operacion_acumulacion_fondos_cobro_exportaciones_52a866`
- **Cantidad**: 15 nodos, 14 aristas. Predicados presentes: `aplica_a` (3), `establecida_en` (5), `exceptua_obligacion` (1), `limita` (5).
- **Dato para la comparación**: este subgrafo no contiene ninguna arista
  `referencia` — la arista que la figura nueva quiere resaltar (la que
  sigue una remisión entre los dos puntos mostrados) no existe en el caso
  actual, cuyo eje es la anti-fusión de variantes, no la remisión.

## J. Verificación del párrafo de construcción

Unidad de solo lectura (2026-09-01). Verifico contra el repo las cinco
afirmaciones del párrafo de la Introducción que describe cómo se construye el
grafo, en el orden en que las enuncia: (a) cada Texto Ordenado se divide
siguiendo su estructura de secciones y puntos; (b) un modelo de lenguaje
extrae de cada parte las entidades y relaciones que admite un esquema fijo de
seis tipos de entidad y doce de relación; (c) un paso de control revisa cada
extracción y aparta las que requieren revisión humana; (d) las referencias que
un punto hace a otro se convierten en aristas entre los nodos
correspondientes; (e) por último las partes se unen en un único grafo mediante
un procedimiento fijo, de modo que la misma entrada produce siempre el mismo
grafo. No propongo redacción: solo verifico. El grafo de referencia es el
vigente, KG-Reextraído-r1 (`data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json`,
sha256 `0226e947…`), construido sobre los 5 TOs del conjunto de desarrollo.

### J.1 Orden real de las etapas

Las etapas llevan los nombres E0–E5 en `docs/diseno_reextraccion_v2.md` §3
(«Arquitectura: pipeline por etapas», línea 98). La oración de cada una es
copia textual de ese documento (no inferida). El orden de EJECUCIÓN real no es
el orden de numeración: lo fija el docstring de `runner_corpus.py` («pipeline
E1→E3», línea 2) para las etapas con LLM y la constante `ETAPAS` de
`ensamblar_r1.py` (línea 40) para las de código.

| # ejec. | Etapa (nombre del repo) | Código | Qué hace (verbatim del repo) |
|---|---|---|---|
| 1 | **E0 — Chunking determinístico (código)** | `data/experiment/reextraccion_v2/e0_chunking/e0_lib.py` (driver `correr_e0.py`) | «Segmentación anclada a la estructura normativa del TO, derivada del **cuerpo** del documento — nunca del índice solo.» (`docs/diseno_reextraccion_v2.md:107`) |
| 2 | **E1 — Fan-out de extracción (LLM chico, contexto fresco por chunk)** | `data/experiment/reextraccion_v2/e1_extractor/{prompt_e1,cliente_e1,validador_e1}.py` | «Un extractor aislado por chunk, con el esquema v2 como contrato de salida estructurado y un prefijo de sistema estable y cacheado.» (`…:139`) |
| 3 | **E3 — Verificador de completitud intra-unidad (LLM fuerte, contexto fresco)** | `data/experiment/reextraccion_v2/e3_verificador/{prompt_e3,cliente_e3,ratchet_e3}.py` | «Recibe el texto fuente de la unidad estructural y lo extraído de ella — jamás el contexto del extractor (principio 2.c). Su blanco son las **amputaciones**.» (`…:173`) |
| 4 | **E2 — Reduce en código (sin LLM)** | `data/experiment/reextraccion_v2/e2_reduce/e2_lib.py` (invocado por `ensamblar_r1.etapa_e2`) | «Ensamblado determinístico: ids determinísticos (función del contenido y la provenance, no del orden de llegada), validación de firmas de aristas contra la matriz vigente de tipos, y **guarda de fan-in**.» (`…:149`) |
| 5 | *merge cross-TO* | `data/experiment/reextraccion_v2/corpus_v2/r1_invariantes.py` (`merge_grafos_guardado`) | «B1.5 merge cross-TO GUARDADO» (`ensamblar_r1.py:11`) — une los 5 grafos por TO en uno solo. |
| 6 | **E4 — Resolución y deduplicación consciente de variación** | `data/experiment/reextraccion_v2/corpus_v2/r1_e4.py` | Diseño: «Resolución de entidades con caché de tipos para consistencia cross-chunk …, y una **regla dura anti-fusión**» (`…:199`). Implementación en r1: «E4 **DETERMINÍSTICO (sin LLM)** sobre el grafo ya fusionado cross-TO» (`r1_e4.py:2`). |
| 7 | **E5 esqueleto** | `data/experiment/reextraccion_v2/corpus_v2/r1_e5_esqueleto.py` | «Inyecta clases, instancias y roles del catálogo (`esquema_v2_clases.json`) y las aristas subclase_de / instancia_de / parte_de / miembro_de» (`r1_e5_esqueleto.py:2`). |
| 8 | *referencias norma→norma* | `data/experiment/reextraccion_v2/corpus_v2/r1_referencias.py` | «referencias cruzadas norma→norma, detector **DETERMINÍSTICO (regex)** sobre label + properties de texto de cada nodo de contenido, con resolución contra (a) el inventario de TOs del subset y (b) las unidades estructurales de E0» (`r1_referencias.py:2`). |
| 9 | *provenance rica* | `data/experiment/reextraccion_v2/corpus_v2/r1_provenance.py` | «A cada provenance de nodo y arista … se le AGREGAN, sin quitar ningún campo existente: `chunk_id`, `paginas`, `ancestros`» (`r1_provenance.py:2`). |
| 10 | **cierre / E5 anclas finales (código)** | `ensamblar_r1.cerrar()` (líneas 197–283) | «Cierre determinístico: validación SHACL, chequeo del sistema de sujetos, invariantes de provenance, labels …, conteos finales contra el censo de E2, y sha256 sellado del grafo resultante.» (`…:216`) |

Nota sobre la numeración: `docs/diseno_reextraccion_v2.md` §3 lista E2 antes
que E3, pero en la corrida real E3 corre sobre la salida de E1 y E2 consume lo
que E3 dio por final. Verbatim del docstring de `ensamblar_r1.py` (líneas 6–14):
«1. B1.6 cola humana flaggeada … 2. E2 por TO con `e2_lib.ensamblar` … 3. B1.5
merge cross-TO … 4. B1.2 E4 determinístico … 5. B1.1 E5 esqueleto … 6. B1.3
referencias norma→norma … 7. B1.4 provenance rica … 8. cierre». La carga de
entrada de E2 es `C.cargar_extracciones_finales(to)` (`ensamblar_r1.py:57`),
es decir `finales.jsonl`, que es la salida terminal de E3.

Ubicación de cada afirmación en el orden real:

| Afirmación | Etapa real | Posición de ejecución |
|---|---|---|
| (a) división por estructura de secciones y puntos | E0 | 1 |
| (b) LLM extrae bajo esquema de 6 entidades / 12 relaciones | E1 | 2 |
| (c) paso de control que revisa y aparta | E3 | 3 |
| (d) referencias punto→punto convertidas en aristas | referencias (`r1_referencias.py`) | **8** |
| (e) unión en un único grafo por procedimiento fijo | E2 + merge + E4 + E5 + cierre | 4–7 y 10 |

**¿Coincide el orden del párrafo con el del pipeline? NO del todo: (a), (b) y
(c) están en el orden correcto; (d) y (e) están invertidos.** Las referencias
no se resuelven antes del ensamblado sino después: el detector corre sobre el
grafo ya ensamblado y fusionado cross-TO (posición 8, tras E2/merge/E4/E5), y
no podría correr antes, porque resuelve el destino contra los nodos ya
anclados al punto destino — «punto/sección resoluble en E0 y con nodos de
contenido anclados (`provenance.punto == destino`, cualquier rol) → una arista
por nodo destino» y «punto existente en E0 sin nodos anclados → irresoluble
`punto_sin_nodos`» (`r1_referencias.py:26–30`). Con el orden del párrafo, el
paso (d) no tendría contra qué resolver.

Dato adicional verificado de la afirmación (b): el esquema que ve el LLM tiene
exactamente 6 tipos de entidad y 12 predicados. Reproduce:

```
python3 -c "import sys; sys.path.insert(0,'data/experiment/grafo_v2/code'); import schema; print(len(schema.ENTITY_TYPES), schema.ENTITY_TYPES); print(len(schema.PREDICATES), schema.PREDICATES)"
6 ('Comunicacion', 'TextoOrdenado', 'Operacion', 'Restriccion', 'Excepcion', 'Obligacion')
12 ('establecida_en', 'referencia', 'modificada_por', 'aplica_a', 'regula', 'exceptua', 'exceptua_obligacion', 'prohibe', 'limita', 'ejecuta', 'requiere', 'condiciona')
```

El grafo final tiene además el séptimo tipo `Sujeto` (111 nodos) y 5
relaciones de ensamblado que el LLM no emite (`subclase_de` 57,
`padre_sugerido` 41, `miembro_de` 17, `instancia_de` 7, `parte_de` 1;
`reporte_ensamblado_r1.json → nodes_by_type` / `edges_by_relation`). Eso es
consistente con §G.1 y con lo que el párrafo siguiente del texto ya declara.

### J.2 El paso de control (E3)

**La etapa NO solo aparta: también reintenta la extracción.** El reintento es
parte de E3, no de otra etapa. Verbatim del docstring de
`data/experiment/reextraccion_v2/e3_verificador/ratchet_e3.py` (líneas 7–16):

```
  veredicto E3 con faltantes
    → prompt de RE-EXTRACCIÓN: el prompt E1 del chunk, ÍNTEGRO, + bloque de
      feedback estructurado, marcado como reintento. …
    → re-extracción (cliente E1) → re-validación E1 → re-verificación E3.
  tope: 1 reintento. Si persisten faltantes → el chunk va a COLA HUMANA con
  flag y TODO persistido. NUNCA ingreso silencioso al grafo.
```

`TOPE_REINTENTOS = 1` (`ratchet_e3.py:70`). La re-extracción se dispara desde
dentro de E3 llamando al cliente de E1 (`reextraer_chunk(cliente_extractor,
…)`, `ratchet_e3.py:393–396`), y el propio módulo importa `prompt_e1`,
`validador_e1` y `cliente_e1` «solo import (mecánica de re-inyección)»
(`ratchet_e3.py:65–68`). El verificador nunca corrige por su cuenta: «El
verificador JAMÁS corrige: este módulo solo transporta su feedback al
extractor» (`ratchet_e3.py:18`).

**Estados posibles**, con su definición operativa (constante y línea de
asignación en `ratchet_e3.py`) y su conteo medido sobre las 1.763 unidades del
corpus de desarrollo:

```
ESTADOS = ("completo_ok_directo", "aceptado_con_residuales",
           "aceptado_tras_reintento",
           "cola_humana", "cola_humana_veredicto_inutilizable",
           "cola_humana_reextraccion_invalida")
                                            (ratchet_e3.py:74–77)
```

| Estado | Definición (código) | Línea | n |
|---|---|---|---|
| `completo_ok_directo` | el veredicto inicial es «completo ok»: la unidad se acepta sin faltantes | 373 | 816 |
| `aceptado_con_residuales` | el veredicto inicial no tiene faltantes **bloqueantes**; se acepta con los media/baja declarados como residuales (LAUDO A: `SEVERIDAD_BLOQUEANTE = ("alta",)`, línea 72) | 376 | 537 |
| `aceptado_tras_reintento` | tras la re-extracción con feedback, la re-verificación da «completo ok» o «aceptable» | 414 | **330** |
| `cola_humana` | tope de reintentos agotado con bloqueantes persistentes | 417 | 75 |
| `cola_humana_veredicto_inutilizable` | ningún faltante bloqueante tiene cita verificada contra el fuente: «no se re-extrae sobre citas fabricadas» | 384 | 3 |
| `cola_humana_reextraccion_invalida` | la re-extracción falló o fue rechazada a nivel chunk por `validador_e1` | 399 | 1 |
| `cola_humana_reextraccion_dirigida` | estado observado en los datos, fuera de la constante `ESTADOS`; lo escribe `corpus_v2/reextraccion_dirigida.py` | — | 1 |

Reproduce (los `finales.jsonl` son append-only con last-wins por `chunk_id`):

```
python3 -c "
import json,collections
tot=collections.Counter()
for to in ('pro','cla','ric','cap','ext'):
    v={}
    for l in open(f'data/experiment/reextraccion_v2/corpus_v2/salida/{to}/finales.jsonl'):
        r=json.loads(l); v[r['chunk_id']]=r
    tot.update(collections.Counter(r['estado'] for r in v.values()))
print(sum(tot.values()), dict(tot))"
1763 {'completo_ok_directo': 816, 'cola_humana': 75, 'aceptado_tras_reintento': 330, 'aceptado_con_residuales': 537, 'cola_humana_veredicto_inutilizable': 3, 'cola_humana_reextraccion_invalida': 1, 'cola_humana_reextraccion_dirigida': 1}
```

**330 de 1.763 unidades (18,7 %) fueron re-extraídas y aceptadas recién en el
segundo intento.** Ese trabajo es de E3 y no está descrito por «revisa cada
extracción y aparta las que requieren revisión humana».

**La re-extracción DIRIGIDA sí es de otra etapa.** `corpus_v2/reextraccion_dirigida.py`
es un paso post-corrida, por laudo, sobre 6 unidades **rechazadas en E1** (no
en E3): «re-extracción dirigida de las 6 unidades rechazadas en E1 durante la
corrida del corpus, previa al re-ensamblado final» y «Lo que pasa validación
entra por el circuito normal (E3 + ratchet, política A+B)»
(`reextraccion_dirigida.py:2–4` y 14). Es decir: el reintento del ratchet vive
DENTRO de E3; la re-extracción dirigida es una etapa aparte que alimenta a E3.

**Salvedad sobre «aparta»**, que corresponde declarar: en el grafo vigente r1
las unidades de cola humana **sí ingresan al grafo, marcadas**, no quedan
afuera. Verbatim de `corpus_v2/r1_cola_flaggeada.py:2–16`: «B1.6: la cola
humana ingresa al grafo FLAGGEADA. (1) … las unidades de cola humana
(`finales.jsonl` con `validacion_final=None`; 80 en el corpus) ingresan con
sus elementos E1 VÁLIDOS … (2) `flaggear_grafo(...)`: todo nodo/arista con
alguna provenance emitida por un chunk de cola recibe `properties.estado_e3`
…, `properties.cola_humana="true"` y `properties.cola_chunks`». Conteo del
reporte (`salida_r1/reporte_ensamblado_r1.json → cola_flaggeada`): 80 unidades
de cola, 79 ingresadas (la única excluida es `cap::4.2.1.2`, sin E1 válido),
394 nodos y 646 aristas flaggeados. En el grafo sellado anterior
(`corpus_v2/salida/kg.json`) la cola no ingresaba: «La cola humana NO ingresa
al grafo (`validacion_final=None` — principio "nunca ingreso silencioso")»
(`runner_corpus.py:35–36`). En r1 el principio se cumple por marcado explícito,
no por exclusión.

### J.3 Alcance del determinismo

**Etapas con LLM (no determinísticas): E1 y E3. Todas las demás son código
puro.** El principio está declarado en `docs/diseno_reextraccion_v2.md:59`
(«**(b) Split mecánico/juicio.** Lo determinístico va en código; lo
interpretativo va en LLM»), y en la implementación de r1 se verifica que el
ensamblado no llama a la API:

```
grep -rn "anthropic\|cliente_e\|messages.create" data/experiment/reextraccion_v2/corpus_v2/r1_*.py data/experiment/reextraccion_v2/corpus_v2/ensamblar_r1.py
(sin salida)
```

Cabecera de `ensamblar_r1.py:2–3`: «re-ensamblado determinístico →
KG-Reextraído-r1 …. Código puro, **cero LLM**, cero escrituras bajo `salida/`
(sellada)». E4, que en el diseño era «LLM fuerte + código»
(`docs/diseno_reextraccion_v2.md:197`), en r1 se implementó sin LLM
(`r1_e4.py:2`), de modo que en el grafo vigente el juicio del modelo está
confinado a E1 y E3.

**Modelo y temperatura de la extracción.** `corpus_v2/runner_corpus.py`:

```
MODEL_E1 = "claude-haiku-4-5"      (línea 76)
MODEL_E3 = "claude-sonnet-5"       (línea 79)
```

La temperatura **no se fija en ninguna parte del pipeline**: el request
canónico de E1 es

```
    return {
        "model": model,
        "max_tokens": max_tokens,
        "system": bloques_sistema(canal_abierto),
        "tools": [tool_schema_e1(canal_abierto)],
        "tool_choice": {"type": "tool", "name": NOMBRE_TOOL},
        "messages": [{"role": "user", "content": build_user_message(chunk)}],
    }
                    (e1_extractor/prompt_e1.py:533–540, build_request_kwargs)
```

sin campo `temperature`, y el grep sobre las cinco carpetas del pipeline no
encuentra ninguna asignación:

```
grep -rn "temperature" data/experiment/reextraccion_v2/{e0_chunking,e1_extractor,e2_reduce,e3_verificador,corpus_v2}
(sin salida; exit 1)
```

Es decir: **E1 y E3 corren con la temperatura por defecto de la API, no con
temperatura 0**. No hay en el repo ningún mecanismo que fuerce la
reproducibilidad del muestreo del modelo.

**Caché de llamadas y su alcance.** E1 y E3 envuelven `llm_cache.CachingClient`
(cuarteto sellado, «se ENVUELVE, jamás se edita», `cliente_e1.py:13`), con una
`.db` propia por etapa (`e1_extractor/cache/e1_extraccion.db`,
`cliente_e1.py:52`). La key es
`sha256(namespace + "\n" + request canónico)` (`llm_cache.compute_key`, líneas
120–126), donde el request canónico «hashea TODO lo que va en kwargs —model,
system, messages, tools, tool_choice, temperature, max_tokens, thinking…»
(`llm_cache.py:110–115`) y el namespace es «dominio + code-version propio +
hash del prefijo estable + flag de thinking» (`cliente_e1.py:56–63`). Alcance
declarado: «Nunca se paga dos veces la misma llamada» (`llm_cache.py:16`).
Consecuencia para el determinismo: **una re-corrida con la caché caliente
devuelve exactamente el mismo crudo** (es una lectura de disco); una re-corrida
con caché fría, o tras cualquier cambio de prompt, tool schema, modelo o
`max_tokens`, vuelve a llamar al modelo y no hay garantía de igualdad.

**Qué afirma el repo sobre reproducibilidad, y sobre qué exactamente.** La
única afirmación explícita es `docs/laudo_promocion_r1_vigente.md:22–24`:
«KG-Refinado es Gen. 2 con correcciones manuales laudadas (C1–C7); r1 es la
primera release **reproducible de punta a punta (doble corrida byte-idéntica,
`185e042`)**, que es lo que la tesis entrega como método». La evidencia detrás
de esa frase es el campo `doble_corrida_byte_identica: true` de
`salida_r1/reporte_ensamblado_r1.json`, y ese campo se computa así:

```
    # corrida 1 y 2 (doble corrida byte-idéntica)
    e1 = correr(con_cola=True, escribir_salida=True)
    e2 = correr(con_cola=True, escribir_salida=False)
    doble = e1["sha256"] == e2["sha256"] and e1["kg_json"] == e2["kg_json"]
                                    (ensamblar_r1.py:201–206)
```

`correr()` parte de las extracciones YA PERSISTIDAS
(`C.cargar_extracciones_finales(to)`, línea 57) y no emite ninguna llamada a
la API. **La doble corrida byte-idéntica prueba el determinismo del
ensamblado, no el del pipeline completo.** Otras dos verificaciones de
determinismo, también de etapas de código: E0, «`python3 selftest_e0.py`
# 2 corridas + cobertura + T4 (30 checks)» con «corrida: 30/30 PASS»
(`e0_chunking/INFORME_E0.md:161` y 252); y E2, «**Determinismo por orden
documental.** … El selftest baraja el jsonl y verifica grafo bit-idéntico; la
doble corrida de `reducir()` da el mismo sha256»
(`e2_reduce/INFORME_E2.md:49–52`).

**¿Es verdadera «la misma entrada produce siempre el mismo grafo» para el
pipeline completo? NO.** Con los PDFs como entrada y la caché fría, E1 y E3
son llamadas a un modelo de lenguaje sin temperatura fijada, y nada en el repo
demuestra ni afirma que dos corridas de esas dos etapas den el mismo
resultado. La afirmación **sí es verdadera** para: (i) el ensamblado —
etapas 4 a 10 de J.1, E2 + merge + E4 + E5 + referencias + provenance +
cierre — tomando como entrada las extracciones persistidas, con la doble
corrida byte-idéntica y el sha256 `0226e947…` como evidencia; (ii) E0 por
separado (selftest de 2 corridas, 30/30); y (iii) una re-corrida completa cuyos
requests de E1/E3 sean todos hits de la caché local, que por construcción
devuelve los mismos crudos.

### J.4 Resolución de referencias

Conteos sobre el corpus de desarrollo (5 TOs), de
`salida_r1/reporte_ensamblado_r1.json → referencias`:

| Magnitud | Valor |
|---|---|
| Nodos con al menos una remisión | 835 |
| Menciones (remisiones) detectadas | **1.089** |
| `resueltas` (campo del reporte; incluye las parciales) | 837 |
| de las cuales `parciales` | 20 |
| `irresolubles` | **252** |
| Aristas `referencia` nuevas | 5.645 |
| de ellas, aristas al nodo TextoOrdenado | 6 |
| de ellas, cross-TO | 188 |

Los **estados posibles del archivo de remisiones** son tres —`resuelta`,
`parcial`, `irresoluble` (asignados en `r1_referencias.py:260`, 270, 274, 296,
299)— y su conteo estricto sobre `salida_r1/referencias_remisiones.json` es:

```
python3 -c "
import json,collections
rem=json.load(open('data/experiment/reextraccion_v2/corpus_v2/salida_r1/referencias_remisiones.json'))
print(len(rem), dict(collections.Counter(r['estado'] for r in rem)))"
1089 {'resuelta': 817, 'irresoluble': 252, 'parcial': 20}
```

(El 837 del reporte es `resuelta + parcial`: `"resueltas": sum(1 for r in
remisiones if r["estado"] in ("resuelta", "parcial"))`, `r1_referencias.py:326`.)

Motivos de las 252 irresolubles (`reporte_ensamblado_r1.json →
referencias.irresolubles_por_motivo`):

```
 "punto_sin_nodos (existe en E0; contenido solo en descendientes/contenedor — frontera ancla/chunk)": 115,
 "norma fuera del inventario del subset": 106,
 "punto inexistente en E0 de ric": 9,
 "punto inexistente en E0 de ext": 7,
 "punto inexistente en E0 de cap": 5,
 "autorreferencia al punto propio": 4,
 "punto inexistente en E0 de cla": 4,
 "anáfora sin norma previa resoluble": 1,
 "punto inexistente en E0 de pro": 1
```

**¿Vale «las referencias que un punto hace a otro se convierten en aristas»
para todas? NO: solo para las resueltas.** La regla está declarada en la
cabecera del módulo: «Nada se inventa: remisión sin destino resoluble =
registro en `irresolubles`, **no arista**» (`r1_referencias.py:6–7`). Las 252
irresolubles quedan en `salida_r1/referencias_irresolubles.json` y no producen
ninguna arista. Las 20 `parciales` producen aristas solo hacia los destinos
que sí resolvieron, y sus destinos no resueltos quedan registrados en el campo
`irresolubles_parciales` de la remisión (`r1_referencias.py:294–296`). En
porcentaje sobre menciones: 837/1.089 = 76,9 % generan al menos una arista;
252/1.089 = 23,1 % no generan ninguna.

**Precisión sobre el total de 5.680.** El grafo tiene 5.680 aristas
`referencia`, pero no todas son remisiones punto→punto: 5.645 llevan
`rol_fuente = "referencia_cruzada"` (las que produce esta etapa) y las 35
restantes vienen de la extracción E1 y son todas TextoOrdenado→Comunicacion,
no punto→punto. Reproduce:

```
python3 -c "
import json,collections
kg=json.load(open('data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json'))
ref=[e for e in kg['edges'] if e['relation']=='referencia']
print(len(ref), dict(collections.Counter(e.get('rol_fuente') for e in ref)))
print(collections.Counter((e['source'].split('_')[0], e['target'].split('_')[0]) for e in ref if e.get('rol_fuente') is None))"
5680 {'referencia_cruzada': 5645, None: 35}
Counter({('TextoOrdenado', 'Comunicacion'): 35})
```

Esto es consistente con la fila 19 de `docs/tesis/mapa_fuentes_intro.md`
(«5.680 aristas `referencia` totales (5.645 nuevas con evidencia + 35
previas)»), y conviene tenerlo presente porque el cuerpo del texto llama a las
5.680 «remisiones entre puntos».

### J.5 Resumen de la verificación

| Afirmación | Veredicto |
|---|---|
| (a) división por estructura de secciones y puntos | Verificada — E0, posición 1. |
| (b) LLM, esquema fijo de 6 tipos de entidad y 12 de relación | Verificada — E1, posición 2; `ENTITY_TYPES` = 6, `PREDICATES` = 12. |
| (c) un paso de control revisa y aparta lo dudoso | **Incompleta** — E3 revisa, pero además re-extrae con feedback (330/1.763 aceptadas recién tras el reintento); y en r1 la cola humana ingresa marcada (79 unidades), no queda afuera. |
| (d) las referencias se convierten en aristas | **Solo las resueltas** (837 de 1.089 menciones); 252 quedan registradas como irresolubles sin arista. |
| (e) unión final por procedimiento fijo; misma entrada → mismo grafo | **Parcial** — el procedimiento fijo y la reproducibilidad valen para el ensamblado (doble corrida byte-idéntica) y para E0, no para el pipeline completo: E1 y E3 son llamadas LLM sin temperatura fijada. |
| Orden del párrafo vs. orden real | (a)(b)(c) correctos; **(d) y (e) invertidos** — las referencias se resuelven sobre el grafo ya ensamblado (posición 8). |
