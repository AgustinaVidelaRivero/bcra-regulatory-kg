# Report — Run 4: Schema-light puro

**Run:** `Run 4 — Schema-light puro`
**Carpeta:** `data/experiment/run_4_schema_light/`
**Estrategia:** Cero vocabulario controlado a priori. Tipos y predicados emergen de los datos durante la extracción; canonización post-procesada = normalización superficial + slug-dedup, sin clustering semántico.
**Modelo de extracción:** `claude-haiku-4-5` (Claude Haiku 4.5).
**Fecha de ejecución:** 2026-05-27.

---

## 1. Métricas del protocolo (sección d)

### 1.1 Tiempo y costo

| Concepto | Valor |
|---|---:|
| Tiempo de extracción Haiku (wall clock, los 5 TOs) | ≈ 27 min con concurrency 3 |
| Tiempo de post-procesamiento (preprocess + assemble + viz) | ≈ 3 min |
| Tiempo total de construcción del KG | ≈ 30 min |
| Tokens input (extracción producción) | 732 576 |
| Tokens output (extracción producción) | 687 959 |
| **Costo de producción (Haiku 4.5: $1/MTok in, $5/MTok out)** | **$4.17** |
| Costo iterativo (smoke #1 invalidado por bug Comuns A, borrado del cache) | $0.40 |
| **Costo total del experimento (producción + iterativo)** | **$4.57** |
| Límite presupuestario del protocolo | $11.00 |
| Margen final al presupuesto | $6.43 (58 % del presupuesto sin gastar) |

La estrategia salió **menos del 50 % del presupuesto del protocolo** porque NO requiere una etapa de resolución de entidades con Sonnet (a diferencia de la `cookbook` del Run 1). Para schema-light puro la canonización es determinística y gratuita.

### 1.2 Estructura del grafo

| Métrica | Valor |
|---|---:|
| Nodos | 3 298 |
| Edges | 3 434 |
| **Densidad (edges/nodes)** | **1,04** |
| Tipos de entidad únicos (canónicos) | 858 |
| Tipos de relación únicos (normalizados) | 1 578 |
| Tipos de relación únicos (crudos, antes de normalización superficial) | 1 603 |
| Nodos cross-TO (mismo slug en ≥ 2 TOs) | 110 |
| Nodos con > 1 type_raw observado | 438 (13 %) |
| Mediana de longitud de label (palabras) | 4 |
| p90 de longitud de label (palabras) | 8 |
| Máximo de longitud de label (palabras) | 18 |

La densidad 1,04 es baja pero esperada en KGs construidos chunk-a-chunk: cada relación que el modelo extrae tiene typically ambas puntas dentro del mismo chunk; las relaciones cross-chunk se pierden a menos que las puntas se dedup-een a un mismo slug. Las únicas 110 entidades cross-TO actúan como puntos de "soldadura" entre los TOs.

### 1.3 Nodos por tipo (top 30 + cola)

| # | Tipo canónico | Conteo |
|---:|---|---:|
| 1 | sujeto_regulado | 170 |
| 2 | instrumento_financiero | 103 |
| 3 | operacion_regulada | 83 |
| 4 | requisito_regulatorio | 61 |
| 5 | documento_regulatorio | 48 |
| 6 | parametro_regulatorio | 43 |
| 7 | categoria_de_activo | 40 |
| 8 | tipo_de_operacion | 40 |
| 9 | concepto_regulatorio | 38 |
| 10 | concepto_deducible_de_capital | 37 |
| 11 | categoria_de_exposicion | 33 |
| 12 | categoria_de_pasivo | 30 |
| 13 | activo_admitido_como_garantia | 25 |
| 14 | producto_financiero | 24 |
| 15 | tipo_de_financiacion | 24 |
| 16 | parametro_de_calculo | 24 |
| 17 | requisito_temporal | 23 |
| 18 | componente_de_capital_regulatorio | 23 |
| 19 | operacion_cambiaria | 23 |
| 20 | obligacion_financiera | 22 |
| 21 | limite_regulatorio | 19 |
| 22 | operacion_financiera | 18 |
| 23 | componente_de_calculo | 18 |
| 24 | tipo_de_operacion_financiera | 18 |
| 25 | instrumento_derivado | 16 |
| 26 | regimen_aduanero_exceptuado | 16 |
| 27 | procedimiento_regulatorio | 15 |
| 28 | tipo_de_riesgo | 15 |
| 29 | deduccion_de_capital | 15 |
| 30 | regimen_de_exportacion | 15 |

Cola larga:

| Frecuencia | # tipos |
|---|---:|
| ≥ 50 | 4 |
| 10–49 | 49 |
| 5–9 | 113 |
| 2–4 | 341 |
| 1 (singleton) | 351 |

### 1.4 Edges por tipo de relación (top 30 + cola)

| # | Predicado normalizado | Conteo |
|---:|---|---:|
| 1 | incluye | 185 |
| 2 | requiere | 66 |
| 3 | se_aplica_a | 41 |
| 4 | comprende | 39 |
| 5 | deduce | 34 |
| 6 | se_compone_de | 31 |
| 7 | debe_cumplir | 29 |
| 8 | admite_como_garantia | 28 |
| 9 | debe_contar_con | 24 |
| 10 | es_tipo_de | 22 |
| 11 | esta_sujeta_a | 22 |
| 12 | realiza | 19 |
| 13 | es_indicador_de | 18 |
| 14 | otorga | 17 |
| 15 | se_calcula_a_partir_de | 17 |
| 16 | excluye | 16 |
| 17 | emite | 16 |
| 18 | financia | 15 |
| 19 | se_imputa_a | 13 |
| 20 | puede_incluir | 13 |
| 21 | recibe | 12 |
| 22 | aplica | 12 |
| 23 | requiere_conformidad_previa_de | 12 |
| 24 | requiere_parametro | 12 |
| 25 | aplica_a | 11 |
| 26 | debe_evaluar | 11 |
| 27 | debe_mantener | 10 |
| 28 | puede_depositarse_en | 10 |
| 29 | requiere_conformidad_previa_del_bcra_para_acceder_a | 10 |
| 30 | genera | 10 |

Cola larga: **1 038 predicados son singletons** (66 % de los 1 578 únicos).

### 1.5 Cobertura por TO

| TO | Páginas | Chunks | ok | empty | failed | Nodos primary | Edges primary | Cobertura |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Protección Usuarios | 40 | 12 | 10 | 2 | 0 | 211 | 245 | 100 % de chunks no-versionado |
| Clasificación Deudores | 60 | 17 | 11 | 6 | 0 | 255 | 268 | 100 % |
| RI Cont. Mensual | 59 | 14 | 14 | 0 | 0 | 389 | 307 | 100 % |
| Exterior y Cambios | 201 | 60 | 55 | 5 | 0 | 1 197 | 1 268 | 100 % |
| Capitales Mínimos | 204 | 56 | 48 | 8 | 0 | 1 246 | 1 346 | 100 % |
| **Total** | **564** | **159** | **138** | **21** | **0** | **3 298** | **3 434** | — |

Cobertura interpretada como "porcentaje de chunks que aportaron al menos una tripleta": **138 / 159 = 86,8 %** del corpus. Los 21 chunks restantes son **legítimamente** secciones de versionado y listas de Comunicaciones de origen (verificación manual), correctamente clasificadas como `status=empty` por el SYSTEM_PROMPT v2.

---

## 2. Iteraciones del SYSTEM_PROMPT (lección operativa del run)

El SYSTEM_PROMPT pasó por **dos iteraciones** durante el smoke. La v1 produjo 58 entidades `Comunicación BCRA` en el TO de Protección (de un total de 414 entities, 14 %) — todas ellas Comunicaciones A listadas en la sección final del TO (`Comunicaciones que dieron origen y/o actualizaron esta norma`). Eso viola la regla 1 del protocolo ("Los nodos representan entidades regulatorias REALES, no jerarquía documental").

La v2 agregó una regla explícita sobre **secciones de versionado y marco normativo como metadato completo** (regla 2 del SYSTEM_PROMPT final). Tras re-correr el smoke con v2:
- Entities tipo Comunicación A bajaron de 58 a **0** (-100 %).
- Chunks empty subieron de 0 a 2 (los chunks de versionado, correcto).
- Costo bajó 31 % (menos output).
- Calidad de extracción del cuerpo del TO se mantuvo o mejoró (consolidación de tipos, no pérdida).

Sobre los 4 TOs nuevos extraídos con SYSTEM_PROMPT v2: **0 entidades violan el protocolo**. El backstop estructural (que verifica `^comunicacion_(a|b) | ^ley | ^decreto | ^resolucion | ^circular`) tuvo 0 matches.

Costo del aprendizaje iterativo: $0.40 del smoke v1 (borrado del cache). Inversión bien gastada.

---

## 3. Análisis post-hoc de predicados

### 3.1 Estadísticas

- **Predicados únicos crudos:** 1 603
- **Predicados únicos normalizados (lowercase + sin acentos + snake_case):** 1 578
- **Predicados normalizados singletons:** 1 038 (66 %)
- **Edges con esos singletons:** 1 038 (30 % de los edges totales)
- **Predicados con freq ≥ 10:** 30 (representan ~25 % de los edges)
- **Ratio predicados/edges:** 0,46

### 3.2 Grupos colapsados por la normalización superficial

La normalización superficial fusionó **solo 25 grupos** de predicados crudos (1 603 → 1 578, -1,6 %). Todas las fusiones son por casing/acentos/espacios, no por semántica. Ejemplos:

- `aplica_a` ← `'aplica a'`, `'aplica_a'`
- `debe_cumplir` ← `'debe_cumplir'`, `'debe cumplir'`
- `requiere_aprobacion_de` ← `'requiere_aprobación_de'`, `'requiere aprobación de'`
- `se_compone_de` ← `'se compone de'`, `'se_compone_de'`

Esto confirma que **Haiku ya produce predicados con cierta consistencia léxica superficial**: el casing y los acentos son la única fuente real de duplicación superficial.

### 3.3 Grupos fusionables semánticamente (que esta estrategia NO fusionó)

La cola larga contiene casos que cualquier canonización semántica (manual, vía LLM o vía embeddings) probablemente fusionaría:

**Variantes de "aplica":**
`aplica`, `aplica_a`, `se_aplica_a`, `aplica_para`, `es_de_aplicacion_para`, `se_aplica_para`, `se_aplican_a`, `aplica_para_calcular`, `se_aplica_segun`, …

**Variantes de "exigencia regulatoria":**
`requiere`, `debe_cumplir`, `debe_cumplir_con`, `debe_mantener`, `debe_contar_con`, `debe_observar`, `debe_garantizar`, `debe_realizar`, `requiere_aprobacion_de`, `requiere_conformidad_previa_de`, `requiere_conformidad_previa_del_bcra`, …

**Variantes de "composición / parte-de":**
`incluye`, `comprende`, `se_compone_de`, `se_descompone_en`, `puede_incluir`, `es_componente_de`, `forma_parte_de`, `consiste_en`, `incluye_los`, `incluye_la`, …

**Variantes de "exclusión":**
`excluye`, `no_incluye`, `esta_excluido_de`, `no_comprende`, `no_se_aplica_a`, `no_corresponde_a`, …

La estrategia schema-light puro **deliberadamente** preserva estas variantes. La hipótesis es que la fragmentación léxica es una métrica útil del experimento y que la utilidad downstream se mide en FASE 2.3, no se asume a priori.

### 3.4 Predicados largos (sospechosos de granularidad excesiva)

Cinco predicados de la cola tienen forma de oración casi completa:
- `requiere_conformidad_previa_del_bcra_para_acceder_a` (10×)
- `requiere_conformidad_previa_para_alcanzar` (3×)
- `se_calcula_incluyendo_riesgo_inherente_a` (2×)
- `requiere_evaluacion_minima_de_riesgo_de_credito_de` (1×)
- `puede_oponerse_al_cliente_solo_si` (1×)

El modelo, sin guía, prefiere capturar el matiz preciso del texto que abstraer a un predicado genérico. Eso es la firma de schema-light puro.

---

## 4. Inventario del directorio `code/`

Estructura:

```
code/
├── .env                          (no versionado; contiene ANTHROPIC_API_KEY)
├── .venv/                        (no versionado; venv aislado del run)
├── requirements.txt              Dependencias del run.
├── system_prompt.py              SYSTEM_PROMPT v2 final usado en extracción.
├── chunk.py                      Chunker: pypdf → bloques de ~3K tokens respetando límites de página.
├── filters.py                    Filtros meta-textuales (8 patrones máx). Self-test incluido.
├── slug.py                       Normalización superficial + patrones del backstop estructural.
├── extract.py                    Extracción Haiku 4.5, concurrency 3, Pydantic strict, cache por chunk, separación empty / failure.
├── preprocess.py                 Pasos 1-3 post-extracción: dedup por slug, backstop, normalización de predicados. Persiste staging.json.
├── cluster_types.py              Probe de clustering connected-components (NO se aplicó al KG final).
├── cluster_complete_probe.py     Probe de clustering complete-linkage a 4 umbrales (NO se aplicó al KG final).
├── smoke_report.py               Reporte estructurado del smoke test (control point 2).
├── preassembly_report.py         Checkpoint pre-ensamblaje: tipos nuevos, backstop, costos.
├── assemble.py                   Ensamblaje final del kg.json con formato del protocolo.
├── visualize.py                  pyvis: kg_visual.html con top 400 nodos por grado.
└── cache/
    ├── chunks/                   Output de chunk.py (1 JSON por TO).
    ├── extract/                  Output de extract.py (1 JSON por chunk + _failures.jsonl).
    ├── staging.json              Output de preprocess.py (KG previo al ensamblaje final).
    ├── dedup_report.json         Top 30 slugs más mergeados con type_raw.
    ├── backstop_report.json      Reporte del backstop estructural (0 drops).
    ├── preassembly_checkpoint.json   Snapshot estructurado del checkpoint pre-ensamblaje.
    ├── types_cluster_proposal.json   Propuesta de clustering que NO se aplicó (queda como evidencia).
    └── smoke_report_*.json       Snapshots estructurados de los smokes.
```

Decisión de aislamiento: el `.env` con la API key fue copiado por la autora a `code/` (no se reutilizó de carpetas de otros runs). El `.venv` es propio del run y no se modifican entornos compartidos.

---

## 5. Hallazgos clave para FASE 2.3

1. **Schema-light puro NO requiere etapa de resolución LLM costosa.** Costo final $4.57 vs $10.54 del Run 1 (cookbook con resolución Sonnet). La ausencia de clustering semántico explica el ahorro y también la mayor cardinalidad del schema.
2. **MiniLM multilingüe no es adecuado para canonizar tipos en español regulatorio.** A umbrales en [0.85, 0.92] produce fusiones falsas masivas dominadas por los adjetivos del dominio ("regulatorio", "financiero", "de capital"). Si una estrategia downstream necesita canonización semántica, debería evaluarse:
   - umbrales ≥ 0.94 (recupera solo casing/género/plural pero pierde el resto),
   - reglas heurísticas determinísticas (singular/plural, masculino/femenino),
   - o algún reordenamiento por head-noun antes del embedding.
3. **La regla 2 del SYSTEM_PROMPT (secciones de versionado como metadato) es crítica** y debería estar en cualquier estrategia futura. Sin ella, ~14 % de las entities de cualquier TO terminan siendo Comunicaciones A o referencias inline a otras normas.
4. **La fragmentación léxica de predicados es enorme** (1 578 únicos sobre 3 434 edges). El KG es navegable nodo-por-nodo pero hacer queries por relación específica requiere conocer la verbalización exacta. Esa es la principal debilidad esperada de la estrategia para evaluación downstream.
5. **86,8 % de cobertura por chunk del corpus** (138 / 159 chunks aportaron tripletas). Los 21 empties son legítimamente metadato de versionado.
6. **0 violaciones residuales del protocolo:** 0 nodos representan jerarquía documental, 0 nodos meta-textuales, 0 entidades inventadas no grounded en el corpus.

---

## 6. Entregables finales

| Archivo | Tamaño | Descripción |
|---|---:|---|
| `schema.md` | — | Documentación del schema descriptivo emergente. |
| `kg.json` | 4,5 MB | KG en formato del protocolo (3.298 nodes + 3.434 edges, provenance obligatorio en ambos). |
| `kg_visual.html` | 1,1 MB | Visualización pyvis interactiva: top 400 nodos por grado, coloreados por tipo canónico. |
| `report.md` | — | Este archivo. |
| `code/` | — | Scripts de extracción, post-procesamiento y ensamblaje. |
