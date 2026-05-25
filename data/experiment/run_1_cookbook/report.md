# Report — Run 1: Cookbook de Anthropic

## Identificación del run
- **Run ID (exacto):** `Run 1 — Cookbook de Anthropic`
- **Carpeta:** `data/experiment/run_1_cookbook/`
- **Schema documentado en:** `schema.md`

## Modelos utilizados por etapa

| Etapa cookbook | Script | Modelo | Justificación |
|---|---|---|---|
| 1. Document Corpus Building | `01_load_corpus.py` | — (sin LLM) | Extracción local de texto con pypdf; sin razonamiento. |
| 2. Entity & Relation Extraction | `02_extract.py` | `claude-haiku-4-5` | Alto volumen (~500 chunks); Haiku es rápido y barato y maneja schema-constrained extraction (cookbook §3). Requisito del protocolo. |
| 3. Entity Resolution | `03_resolve.py` | `claude-sonnet-4-6` | Razonamiento sobre evidencia conflictiva (mismo nombre, distinta función); Sonnet pesa mejor descripciones (cookbook §5). |
| 4. Graph Assembly | `04_assemble.py` | — (sin LLM) | Determinístico: dedup de edges, slug de IDs, ensamblaje JSON. |
| 5. Hub Summarization | `05_hub_summarize.py` | `claude-sonnet-4-6` | Síntesis multi-documento de evidencia (cookbook §6); Sonnet por la misma razón que la resolución. |
| 6. Multi-hop Querying | (no ejecutado) | — | Es evaluación, va a la FASE 2.3 del experimento. |

## Excepciones al protocolo

Esta sección registra cualquier desvío del protocolo experimental (`docs/schema/experiment_protocol.md`) o de la plantilla de instancia (`docs/schema/experiment_instance_template.md`).

### Excepción 1: presupuesto USD 5 → USD 10 (autorizada antes del full run)

- **Regla original:** plantilla de instancia, sección "Restricciones operativas": *"Límite de costo: máximo USD 5 de inferencia para esta instancia."*
- **Cambio aplicado:** `BUDGET_USD_HARD` se elevó a USD 10 (margen de abort: USD 9). Autorizado por la autora tras revisar el smoke test sobre Protección al Usuario.
- **Justificación cuantitativa derivada del smoke test:**
  - El smoke completo sobre 1 TO (36 chunks, 100 % cobertura) costó **USD 0.7217**.
  - Extrapolando al corpus completo (543 chunks): proyección **USD 8.0–9.1**.
  - El proyecto se hubiera quedado en ~60 % de cobertura con el presupuesto original.
- **Por qué la estimación inicial fue ~3× optimista:** el promedio real de tokens de input por chunk (≈ 3.000) y de output (≈ 1.500) es notablemente más alto que el supuesto inicial (≈ 1.000 / 300), porque el dominio regulatorio del BCRA es denso en obligaciones por página y el cookbook pide `description` grounded por entidad (lo que infla el output).
- **Comparabilidad con las otras instancias del experimento:** la autora actualizó el `experiment_instance_template.md` para que los Runs 2-5 también tengan presupuesto USD 10 — ver nota en ese archivo. La comparabilidad entre estrategias se mantiene; sólo cambió la magnitud del experimento.
- **Lecciones para FASE 2.1 (preparación):** futuras réplicas del experimento deberían ejecutar primero un smoke sobre 1 TO antes de fijar el presupuesto.

### Excepción 2: presupuesto USD 10 → USD 11 (autorizada después de la resolución)

- **Cambio aplicado:** `BUDGET_USD_HARD` se elevó a USD 11 (margen de abort: USD 10.80). Autorizado por la autora tras el checkpoint post-resolución.
- **Por qué fue necesario:** la resolución Sonnet costó **USD 4.40** (vs proyección USD 1.30, **+238 %**), dejando solo USD 0.01 de margen al hard budget de USD 10. Hub summarization (etapa 5 del cookbook) no entraba.
- **Causa raíz de la desviación de la resolución:**
  - 4.868 entidades únicas reales (vs 3.500–5.000 estimadas) → 57 batches Sonnet.
  - El **output** por call promedió **4.087 tokens** (no estimado previamente): cada cluster lista `{canonical, aliases:[...]}` y con 100 entidades/batch eso son ≈4 K tokens output × $15/MTok = $0.06 por call × 57 calls ≈ $3.40.
  - 2 warnings de `tool_use con payload vacío` en REQUIREMENT (1.280 entidades) y REPORT_ITEM (340), donde Sonnet truncó la salida con `max_tokens=8000` y se cayó a `fallback_singletons()`. Resultado: agrupó menos de lo posible.
- **Decisión:** se autorizó la excepción 2 para no romper el pipeline del cookbook a la mitad. Hub summarization se ejecutó completo (top 15 hubs con Sonnet, fidelidad al cookbook).
- **Lección para futuras réplicas:** la resolución con batches grandes es costosa porque el output escala con el tamaño del batch. Próximas estrategias podrían (a) usar batches más chicos pero más paralelos con Haiku, (b) hacer una primera pasada de blocking heurístico con embeddings antes de Sonnet, o (c) aceptar agrupar menos a cambio de costo controlado.

## Métricas del protocolo (§d)

- **Tiempo total de construcción:** (no instrumentado en esta corrida)
- **Costo total:** USD 10.5400

### Costo por etapa y modelo

| Etapa | Modelo | Calls | Input | Output | Cache W | Cache R | USD |
|---|---|---:|---:|---:|---:|---:|---:|
| extraction | claude-haiku-4-5 | 527 | 1,584,605 | 801,348 | 0 | 0 | 5.5913 |
| resolution | claude-sonnet-4-6 | 57 | 301,584 | 232,996 | 0 | 0 | 4.3997 |
| summarization | claude-sonnet-4-6 | 15 | 98,541 | 16,891 | 0 | 0 | 0.5490 |

> **Caching:** se declaró `cache_control: ephemeral` en el `SYSTEM_PROMPT` de extracción. 
> El threshold mínimo de Haiku 4.5 para activar prompt caching es ≥2.048 tokens; el `SYSTEM_PROMPT` 
> de este run mide 800 tokens reales, por lo que el caching **no se activó** 
> (`Cache W=0`, `Cache R=0`). El declarador se conserva por si futuras versiones del modelo bajan el threshold.

### Nodos y edges

- **Nodos:** 4014
- **Edges:** 4287
- **Densidad (edges/nodes):** 1.068
- **Tipos de entidad únicos:** 10
- **Tipos de relación únicos:** 1548

### Nodos por tipo

| Tipo | Cantidad |
|---|---:|
| REQUIREMENT | 1076 |
| CONCEPT | 624 |
| OPERATION | 609 |
| INSTRUMENT | 517 |
| CLASSIFICATION | 305 |
| REGULATED_SUBJECT | 295 |
| REPORT_ITEM | 282 |
| PROCESS | 260 |
| REGULATOR | 36 |
| SANCTION | 10 |

### Edges por tipo (top 20)

| Predicado | Cantidad |
|---|---:|
| `aplica_a` | 186 |
| `requiere` | 172 |
| `está_sujeto_a` | 121 |
| `está_sujeta_a` | 110 |
| `incluye` | 95 |
| `debe_cumplir` | 85 |
| `realiza` | 80 |
| `integra` | 63 |
| `utiliza` | 42 |
| `emite` | 39 |
| `es_tipo_de` | 34 |
| `otorga` | 33 |
| `genera` | 26 |
| `determina` | 25 |
| `sujeta_a` | 23 |
| `se_compone_de` | 23 |
| `sujeto_a` | 23 |
| `regula` | 19 |
| `habilita` | 19 |
| `se_aplica_a` | 18 |

### Cobertura por TO

| TO | Chunks total | Chunks productivos | % |
|---|---:|---:|---:|
| clasificacion_deudores | 56 | 41 | 73.21% |
| capitales_minimos | 197 | 175 | 88.83% |
| exterior_cambios | 198 | 175 | 88.38% |
| proteccion_usuarios | 36 | 31 | 86.11% |
| regimen_informativo_cm | 56 | 55 | 98.21% |

> *Productivo* = el chunk generó ≥1 entidad o relación tras la llamada a Haiku.
> Los chunks no-productivos son típicamente: páginas de índice, encabezados del TO, y la
> sección final "Comunicaciones vinculadas". Algunos de éstos son skipeados antes de Haiku
> por la heurística `is_non_productive_chunk()` para ahorrar costo sin perder contenido normativo.

## Análisis post-hoc de predicados

La estrategia "Cookbook de Anthropic" deja los predicados como **verb phrases libres** (cookbook §2.2: `predicate: str` sin enum). Esto genera vocabulario verboso por diseño. Esta sección reporta métricas que permiten comparar la *limpieza* del vocabulario contra otras estrategias del experimento.

- **Edges totales:** 4287
- **Predicados únicos crudos** (tal como salieron de Haiku): **1548**
- **Ratio crudo (predicados / edges):** 0.361
- **Predicados únicos tras normalización trivial:** **1515** 
  *(reducción: 33 predicados fusionados)*
- **Ratio normalizado:** 0.353
- **Grupos fusionados:** 33 (≥2 variantes); singletons que quedaron solos: 1482

### Heurística de normalización aplicada

Se considera *variación trivial* cualquiera de:
- Diferencia sólo de **casing** (`Debe_cumplir` vs `debe_cumplir`).
- Diferencia sólo de **acentos** (`esta_sujeto_a` vs `está_sujeto_a`).
- Diferencia sólo de **número gramatical** en el verbo auxiliar inicial: `deben/debe`, `tienen/tiene`, `pueden/puede`, `están/está`, `son/es`, `hacen/hace`, `aplican/aplica`, `requieren/requiere` (+ formas en futuro: `deberán/deberá`, etc.).
- Diferencia sólo de **separadores** (espacio vs underscore vs guión).

NO se considera trivial (y por lo tanto NO se fusiona):
- Variantes léxicas con verbos distintos (`debe_cumplir` ≠ `está_obligado_a`).
- Variantes con preposiciones distintas (`aplica_a` ≠ `aplica_para`).

### Grupos fusionados — top 10

| Canónico normalizado | Variantes crudas |
|---|---|
| `aplica` | `aplica`, `aplican` |
| `aplica_a` | `aplica_a`, `aplican_a` |
| `debe_aplicar` | `debe_aplicar`, `deben_aplicar` |
| `debe_asegurar` | `debe_asegurar`, `deben_asegurar` |
| `debe_basarse_en` | `debe_basarse_en`, `deben_basarse_en` |
| `debe_calcular` | `debe_calcular`, `deben_calcular` |
| `debe_considerar` | `debe_considerar`, `deben_considerar` |
| `debe_cumplimentar` | `debe_cumplimentar`, `deben_cumplimentar` |
| `debe_cumplir` | `debe_cumplir`, `deben_cumplir` |
| `debe_cumplir_con` | `debe_cumplir_con`, `deben_cumplir_con` |

> El `kg.json` NO se modificó: los predicados se conservan exactamente como Haiku los emitió (fidelidad al cookbook). Esta sección es **descriptiva**, para comparación post-hoc entre estrategias.

## Muestra de nodos por TO

5 nodos al azar de cada TO (seed=42, basado en `properties.source_to`).

### clasificacion_deudores

- **`req_responsabilidad_de_la_entidad_financiera_por_la_clasificacion_asignada`** · *REQUIREMENT* · «responsabilidad de la entidad financiera por la clasificación asignada»
  - desc: Obligación de la entidad financiera de mantener responsabilidad por la clasificación finalmente asignada, incluso cuando intervienen profesionales externos.
  - prov: `TO_clasificacion_deudores_actual.pdf` · `p. 13` · version `A 8378`
- **`ins_primas_por_opciones_de_compra_y_de_venta`** · *INSTRUMENT* · «Primas por opciones de compra y de venta»
  - desc: Primas asociadas a opciones financieras tomadas, incluidas en las financiaciones comprendidas.
  - prov: `TO_clasificacion_deudores_actual.pdf` · `p. 7` · version `A 8378`
- **`cla_en_tratamiento_especial_clasificacion_de_deudores`** · *CLASSIFICATION* · «En tratamiento especial (clasificación de deudores)»
  - desc: Categoría especial para refinanciaciones otorgadas por primera vez dentro del año calendario, evaluadas únicamente por mora en atraso.
  - prov: `TO_clasificacion_deudores_actual.pdf` · `p. 23` · version `A 8378`
- **`prc_evaluacion_y_clasificacion_de_deudores`** · *PROCESS* · «Evaluación y clasificación de deudores»
  - desc: Procedimiento mediante el cual se asignan clasificaciones a los deudores considerando su capacidad de repago.
  - prov: `TO_clasificacion_deudores_actual.pdf` · `p. 11` · version `A 8378`
- **`req_permanencia_minima_de_180_dias`** · *REQUIREMENT* · «Permanencia mínima de 180 días»
  - desc: Plazo obligatorio de permanencia en esta categoría tras refinanciación y otorgamiento de crédito adicional.
  - prov: `TO_clasificacion_deudores_actual.pdf` · `p. 24` · version `A 8378`

### capitales_minimos

- **`con_incumplimientos_de_capitales_minimos_y_relaciones_tecnicas`** · *CONCEPT* · «Incumplimientos de Capitales Mínimos y Relaciones Técnicas»
  - desc: Sección 2 de normas que establece criterios para evaluar excesos en límites que generan incrementos de exigencia.
  - prov: `TO_capitales_minimos_actual.pdf` · `p. 9` · version `A 8418`
- **`rsj_entidad_financiera_miembro_compensador`** · *REGULATED_SUBJECT* · «entidad financiera miembro compensador»
  - desc: Entidades financieras que son miembros compensadores y aplican ponderadores de riesgo en relación con aportes a fondos de garantía de CCP.
  - prov: `TO_capitales_minimos_actual.pdf` · `p. 93` · version `A 8418`
- **`cla_programa_de_pagares_respaldados_por_activos_abcp`** · *CLASSIFICATION* · «Programa de Pagarés Respaldados por Activos (ABCP)»
  - desc: Programa por el que se emiten principalmente títulos valores con vencimiento original de hasta un año, respaldados por activos u exposiciones en un SPE.
  - prov: `TO_capitales_minimos_actual.pdf` · `p. 31` · version `A 8418`
- **`req_aforo_por_tipo_de_cambio_h_fx`** · *REQUIREMENT* · «Aforo por tipo de cambio (H fx)»
  - desc: Ajuste aplicado al valor del activo en garantía para considerar fluctuaciones futuras en tipos de cambio bajo método integral.
  - prov: `TO_capitales_minimos_actual.pdf` · `p. 98` · version `A 8418`
- **`ope_posiciones_en_titulos_de_deuda`** · *OPERATION* · «Posiciones en títulos de deuda»
  - desc: Posiciones compradas y vendidas en títulos de deuda que se imputarán a escalas de vencimientos según cupón.
  - prov: `TO_capitales_minimos_actual.pdf` · `p. 124` · version `A 8418`

### exterior_cambios

- **`ins_depositos_francos`** · *INSTRUMENT* · «Depósitos francos»
  - desc: Depósitos habilitados de acuerdo con la Resolución 2.676/79 de la Administración Nacional de Aduanas para ingreso de bienes.
  - prov: `TO_exterior_cambios_actual.pdf` · `p. 133` · version `A 8307`
- **`req_declaracion_jurada_del_exportador`** · *REQUIREMENT* · «Declaración jurada del exportador»
  - desc: Documento obligatorio en el que el exportador detalla el monto pendiente de deuda al 31/08/19 y cancelaciones realizadas.
  - prov: `TO_exterior_cambios_actual.pdf` · `p. 125` · version `A 8307`
- **`ins_declaracion_jurada_del_exportador`** · *INSTRUMENT* · «declaración jurada del exportador»
  - desc: Documento que el exportador debe presentar describiendo la operatoria de entrega gratuita de bienes y justificando que no genera contravalor en divisas.
  - prov: `TO_exterior_cambios_actual.pdf` · `p. 113` · version `A 8307`
- **`ins_contrato_de_obras_o_provision_de_bienes_y_o_servicios`** · *INSTRUMENT* · «Contrato de obras o provisión de bienes y/o servicios»
  - desc: Contrato que implica directa o indirectamente la realización de exportaciones de bienes y/o servicios de residentes argentinos, para cuyo cumplimiento se requiere garantía finan…
  - prov: `TO_exterior_cambios_actual.pdf` · `p. 42` · version `A 8307`
- **`ins_certificaciones_de_exportacion`** · *INSTRUMENT* · «Certificaciones de exportación»
  - desc: Documentos emitidos por la entidad nominada que acreditan las operaciones de exportación del cliente.
  - prov: `TO_exterior_cambios_actual.pdf` · `p. 14` · version `A 8307`

### proteccion_usuarios

- **`ope_seguros_como_contratacion_no_accesoria`** · *OPERATION* · «Seguros como contratación no accesoria»
  - desc: Contratación de seguros de manera independiente, no como producto vinculado a un servicio financiero principal.
  - prov: `TO_proteccion_usuarios_servicios_financieros_actual.pdf` · `p. 38` · version `A 8433`
- **`req_oferta_de_tres_companias_aseguradoras_no_vinculadas_para_seguros_accesorios`** · *REQUIREMENT* · «oferta de tres compañías aseguradoras no vinculadas para seguros accesorios»
  - desc: Obligación de ofrecer al usuario al menos tres compañías aseguradoras no vinculadas entre sí para contratar otros seguros accesoriosa servicios financieros.
  - prov: `TO_proteccion_usuarios_servicios_financieros_actual.pdf` · `p. 18` · version `A 8433`
- **`ins_texto_ordenado_sobre_depositos_e_inversiones_a_plazo`** · *INSTRUMENT* · «Texto Ordenado sobre Depósitos e Inversiones a Plazo»
  - desc: Normativa especial del BCRA que regula las operaciones de captación de fondos y que rige excepcionalmente la aplicabilidad de la cláusula de revocación.
  - prov: `TO_proteccion_usuarios_servicios_financieros_actual.pdf` · `p. 8` · version `A 8433`
- **`req_designacion_de_funcionario_responsable_de_atencion_al_usuario`** · *REQUIREMENT* · «designación de funcionario responsable de atención al usuario»
  - desc: Obligación del Directorio de nombrar funcionarios titular y suplente como responsables de atención al usuario.
  - prov: `TO_proteccion_usuarios_servicios_financieros_actual.pdf` · `p. 23` · version `A 8433`
- **`req_trato_digno_y_no_discriminatorio_a_usuarios_de_servicios_financieros`** · *REQUIREMENT* · «trato digno y no discriminatorio a usuarios de servicios financieros»
  - desc: Obligación de los sujetos obligados de adoptar recaudos para prevenir actos u omisiones discriminatorios por motivos de raza, religión, nacionalidad, edad, sexo, condición econó…
  - prov: `TO_proteccion_usuarios_servicios_financieros_actual.pdf` · `p. 21` · version `A 8433`

### regimen_informativo_cm

- **`rep_codigo_83800000`** · *REPORT_ITEM* · «Código 83800000»
  - desc: Código contable para registrar incremento de exigencia por Grandes Exposiciones determinado por la SEFyC.
  - prov: `TO_regimen_informativo_contable_mensual_actual.pdf` · `p. 41` · version `A 6561`
- **`req_informacion_fuera_de_termino_presentacion_despues_del_plazo_regulatorio`** · *REQUIREMENT* · «Información fuera de término (presentación después del plazo regulatorio)»
  - desc: Situación de incumplimiento cuando la información se presenta después del plazo regulatorio.
  - prov: `TO_regimen_informativo_contable_mensual_actual.pdf` · `p. 42` · version `A 6561`
- **`rep_codigo_70700000`** · *REPORT_ITEM* · «Código 70700000»
  - desc: Código contable para registrar Capital Mínimo Básico.
  - prov: `TO_regimen_informativo_contable_mensual_actual.pdf` · `p. 37` · version `A 6561`
- **`con_otros_resultados_integrales`** · *CONCEPT* · «Otros Resultados Integrales»
  - desc: Saldos registrados en cuentas de otros resultados integrales u otros resultados integrales acumulados conforme a lo previsto en puntos 8.2.1.5 u 8.2.1.6.
  - prov: `TO_regimen_informativo_contable_mensual_actual.pdf` · `p. 28` · version `A 6561`
- **`req_limite_del_14`** · *REQUIREMENT* · «Límite del 14%»
  - desc: Porcentaje máximo de reducción de exigencia aplicable a determinadas entidades.
  - prov: `TO_regimen_informativo_contable_mensual_actual.pdf` · `p. 27` · version `A 6561`

## Validación del KG

✅ Sin errores de validación.

## Inventario del directorio `code/`

| Archivo | Descripción |
|---|---|
| `common.py` | Constantes (subset, tipos), schemas Pydantic, helpers de I/O y accounting de costo. |
| `01_load_corpus.py` | Etapa 1. Extrae texto de los 5 PDFs con pypdf y emite `cache/chunks.jsonl` (chunk = página, fusión de páginas chicas). |
| `02_extract.py` | Etapa 2. Una llamada a Haiku por chunk con structured output (`ExtractedGraph`); persiste `cache/raw_extractions.jsonl` + ledger. |
| `03_resolve.py` | Etapa 3. Por cada tipo de entidad, clusterización con Sonnet; emite `alias_to_canonical.json` y `canonical_info.json`. |
| `04_assemble.py` | Etapa 4. Construye el KG (NetworkX) y lo serializa a `kg.json` en el formato obligatorio. |
| `05_hub_summarize.py` | Etapa 5. Resume los top-degree hubs con Sonnet y enriquece `kg.json` con `summary`/`key_facts`/`time_range`. |
| `06_validate_and_report.py` | Validación + cálculo de métricas + emisión de `report.md`. |
| `07_visualize.py` | Visualización interactiva del KG con pyvis (force-directed, colores por type, hover con metadata). Output: `../kg_visual.html`. Fuera del cookbook; sirve para inspección rápida sin Gephi. |
| `requirements.txt` | Dependencias Python. |
| `README.md` | Cómo correr el pipeline. |
| `cache/` | Outputs intermedios (chunks, extracciones crudas, alias map, ledgers de costo). |
