# Schema descriptivo emergente — Run 4: Schema-light puro

**Run:** `Run 4 — Schema-light puro`
**Estrategia:** sin vocabulario controlado a priori. Los tipos y predicados emergen completamente de los datos durante la extracción; la canonización es post-procesada y minimalista (normalización superficial + dedup por slug, sin clustering semántico).

---

## 1. Filosofía del schema

El schema de este run es **descriptivo**, no prescriptivo. No diseñé un conjunto cerrado de tipos de entidad ni de predicados antes de la extracción; le pedí al modelo (Claude Haiku 4.5) que **invente los tipos y predicados que considere apropiados** para cada fragmento del Texto Ordenado, con dos únicas restricciones no negociables:

1. **Consistencia within-chunk:** si dos entidades son conceptualmente del mismo tipo dentro del fragmento, deben llevar la misma cadena exacta de tipo. (Esto hace que el modelo invente tipos con cierta coherencia local, sin imponerle un vocabulario global.)
2. **Ningún tipo se asocia a jerarquía documental ni a meta-texto.** Los TOs incluyen secciones de versionado, listas de Comunicaciones A/B de origen y referencias inline a Leyes y Decretos — ninguno de esos identificadores documentales se modela como nodo del KG. (Regla del protocolo + refuerzo del prompt + backstop estructural en el ensamblaje.)

Como resultado, el schema final es lo que el corpus regulatorio del BCRA "le pide al modelo extraer" cuando no se le da ningún molde. Eso permite medir empíricamente, en la FASE 2.3, qué tan útil downstream es un schema que no fue diseñado pero sí cubre con alta granularidad la realidad léxica del corpus.

---

## 2. Tipos de entidad emergentes

### 2.1 Resumen

- **Total tipos canónicos únicos: 858** sobre 3.298 nodos.
- Ratio tipos/nodos: **0,26** (1 tipo nuevo cada ~4 nodos).
- Distribución de frecuencia:

| Frecuencia | Cantidad de tipos |
|---|---:|
| ≥ 50 | 4 |
| 10 – 49 | 49 |
| 5 – 9 | 113 |
| 2 – 4 | 341 |
| 1 (singleton) | 351 |

Más del 40 % de los tipos son singletons (un solo nodo). Eso refleja la decisión del experimento de **NO clusterizar tipos por similitud semántica** (ver sección 4). En estrategias con vocabulario controlado a priori, esos singletons se mapearían contra los tipos predefinidos; aquí se preservan tal como Haiku los inventó.

### 2.2 Top 30 tipos canónicos por frecuencia

```
 170  sujeto_regulado
 103  instrumento_financiero
  83  operacion_regulada
  61  requisito_regulatorio
  48  documento_regulatorio
  43  parametro_regulatorio
  40  categoria_de_activo
  40  tipo_de_operacion
  38  concepto_regulatorio
  37  concepto_deducible_de_capital
  33  categoria_de_exposicion
  30  categoria_de_pasivo
  25  activo_admitido_como_garantia
  24  producto_financiero
  24  tipo_de_financiacion
  24  parametro_de_calculo
  23  requisito_temporal
  23  componente_de_capital_regulatorio
  23  operacion_cambiaria
  22  obligacion_financiera
  19  limite_regulatorio
  18  operacion_financiera
  18  componente_de_calculo
  18  tipo_de_operacion_financiera
  16  instrumento_derivado
  16  regimen_aduanero_exceptuado
  15  procedimiento_regulatorio
  15  tipo_de_riesgo
  15  deduccion_de_capital
  15  regimen_de_exportacion
```

Los tipos top son **anclajes conceptuales generales del dominio regulatorio**: sujetos regulados, instrumentos financieros, operaciones reguladas, requisitos, documentos, parámetros, conceptos. El resto del long-tail son **especializaciones** progresivamente más finas (`tipo_de_riesgo_de_mercado`, `categoria_de_exposicion_minorista`, `componente_de_riesgo_de_opciones`, `regimen_aduanero_exceptuado`, `concepto_deducible_de_capital`, etc.).

### 2.3 Tipos por TO

Los tipos emergen específicos al dominio de cada TO. Ejemplos representativos:

- **Capitales Mínimos:** `componente_de_capital_regulatorio`, `concepto_deducible_de_capital`, `categoria_de_exposicion`, `categoria_de_activo`, `tipo_de_riesgo_de_mercado`, `parametro_de_calculo`, `metodologia_de_calculo`.
- **Exterior y Cambios:** `operacion_cambiaria`, `regimen_aduanero_exceptuado`, `regimen_de_exportacion`, `mercado_de_cambios`, `declaracion_jurada_del_exportador`, `permiso_de_embarque`, `conformidad_previa_del_bcra`.
- **Clasificación de Deudores:** `categoria_de_deudor`, `producto_crediticio`, `categoria_de_exposicion_crediticia`, `tipo_de_proteccion_crediticia`, `mecanismo_de_proteccion`.
- **Protección al Usuario:** `derecho_basico_del_usuario`, `categoria_especial_de_usuario`, `cargo_regulatorio`, `comision_prohibida`, `comision_sujeta_a_comparacion`, `casa_operativa`.
- **RI Contable Mensual:** `regimen_regulatorio`, `documento_requerido`, `codigo_de_operacion`, `requisito_documental`, `registro_obligatorio`.

---

## 3. Predicados emergentes

### 3.1 Resumen

- **Total predicados únicos normalizados: 1.578** sobre 3.434 edges.
- Ratio predicados/edges: **0,46** (un predicado nuevo cada ~2 edges).
- 1.038 predicados son singletons (66 %).

La normalización superficial (lowercase + strip acentos + snake_case) **solo logró colapsar 25 grupos** de predicados crudos. Es decir: en 1.578 predicados normalizados únicos, 1.553 ya eran únicos en su forma cruda. La verbosidad léxica de los predicados es alta y casi enteramente semántica, no superficial.

### 3.2 Top 30 predicados normalizados

```
 185  incluye
  66  requiere
  41  se_aplica_a
  39  comprende
  34  deduce
  31  se_compone_de
  29  debe_cumplir
  28  admite_como_garantia
  24  debe_contar_con
  22  es_tipo_de
  22  esta_sujeta_a
  19  realiza
  18  es_indicador_de
  17  otorga
  17  se_calcula_a_partir_de
  16  excluye
  16  emite
  15  financia
  13  se_imputa_a
  13  puede_incluir
  12  recibe
  12  aplica
  12  requiere_conformidad_previa_de
  12  requiere_parametro
  11  aplica_a
  11  debe_evaluar
  10  debe_mantener
  10  puede_depositarse_en
  10  requiere_conformidad_previa_del_bcra_para_acceder_a
  10  genera
```

El predicado más usado es genérico (`incluye`, 185). Aparecen formas más específicas en la cola (`requiere_conformidad_previa_del_bcra_para_acceder_a`) que son tan finas que se vuelven singletons. Esa es la firma de schema-light puro: el modelo no abstrae el predicado a una familia común, lo escribe casi literal del texto.

### 3.3 Ejemplos de redundancia que **no** se fusionó

Decisión consciente de la estrategia: predicados que difieren en aspecto, voz, tiempo o modalidad quedan como predicados distintos. Por ejemplo, todos estos están separados en el KG:

- `aplica`, `aplica_a`, `se_aplica_a`, `es_de_aplicacion_para` — semánticamente el mismo concepto.
- `requiere`, `debe_contar_con`, `debe_cumplir`, `debe_mantener`, `requiere_parametro`, `requiere_aprobacion_de`, `requiere_conformidad_previa_de` — todos formas de exigencia regulatoria con matiz distinto.
- `incluye`, `comprende`, `puede_incluir`, `se_compone_de` — todos relaciones parte-de con matiz distinto.

Esto es **deliberado**: el experimento de la FASE 2.3 va a medir si la utilidad downstream del KG sufre por esta verbosidad o si los usuarios/agentes pueden navegarla. La hipótesis implícita: schema-light puro tiene la **mayor cobertura conceptual de predicados** pero la **menor consistencia**.

---

## 4. Decisiones de canonización (y por qué se tomaron así)

### 4.1 Normalización superficial (aplicada)

Todos los tipos y predicados crudos se pasaron por:

```
lowercase → unicode NFD → strip combining marks (acentos) → [a-z0-9]+ con _ → strip leading/trailing _
```

Esto colapsa **solo** diferencias de casing, acentuación, espacios vs guiones bajos. **Sin** heurística de plurales (decisión explícita del usuario): `banco` y `bancos` quedan como slugs distintos. **Sin** sinónimos: `BCRA` y `Banco Central de la República Argentina` quedan como dos nodos.

Impacto observable:
- Predicados crudos: 1.603 → normalizados: 1.578 (-25 colapsos, todos por casing puro).
- Nodos crudos (entities con duplicados across chunks): 4.393 → nodos únicos (post slug-dedup): 3.298.

### 4.2 Slug-dedup por nombre

Entidades con el mismo `slug_label(name)` cross-chunk se fusionan en un único nodo:
- `id` = el slug.
- `label` = el name más frecuente (desempate: más corto, luego alfabético).
- `type_raw` = lista única de todos los tipos crudos observados across las observaciones.
- `properties.type_raw_counts` = freq de cada tipo crudo dentro del nodo.
- `properties.all_provenances` = lista de cada chunk donde apareció.
- `provenance` (principal) = la del primer chunk donde aparece.
- `properties.n_observations` = cuántas veces apareció.

El `type` canónico mostrado en el campo top-level del nodo es el `type_raw` **más frecuente** para ese nodo (normalizado superficialmente). La lista completa de tipos crudos se preserva en `properties.type_raw` — visible para la FASE 2.3.

438 de 3.298 nodos (13 %) tienen **más de un type_raw observado**. Eso refleja la inconsistencia inherente que el modelo introduce al ver la misma entidad en diferentes contextos. Ejemplos:
- `entidad_financiera` aparece con 8 tipos crudos distintos: `Sujeto obligado`, `Agente regulado`, `Sujeto regulado`, `Institución regulada`, `Sujeto regulador`, `Entidad regulada`, `Categoría de contraparte`, `Tipo de entidad financiera`.
- `sefyc` con 5: `Autoridad regulatoria`, `Órgano regulador`, `Órgano de supervisión`, `Entidad reguladora`, `Autoridad reguladora` — todos legítimas variantes para la misma autoridad.

### 4.3 Clustering semántico de tipos: NO se aplicó

Probé `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` con cosine similarity a umbrales [0.85, 0.88, 0.90, 0.92] y dos estrategias:
- **Connected components (transitive closure):** a 0.85 produjo un cluster de 76 tipos que combina `Sujeto regulado` (177×), `Operación regulada` (85×), `Requisito regulatorio` (67×), `Documento regulatorio` (60×), `Parámetro regulatorio` (51×)… Todos comparten la palabra "regulatorio/regulado" pero los head nouns son conceptualmente distintos. Fusión falsa masiva.
- **Complete linkage (todos los pares dentro del cluster ≥ umbral):** mejoró pero no resolvió. A 0.92 todavía produce clusters como (`Producto financiero` + `Entidad financiera` + `Elemento financiero` + `Métrica financiera`) que son conceptos distintos, y junta `Régimen aduanero` con `Régimen aduanero exceptuado` (que el TO trata como conceptos separados).

Diagnóstico: **MiniLM multilingüe está dominado por los adjetivos del dominio regulatorio en español** ("regulatorio", "financiero", "de capital", "aduanero", "crediticio") y produce sim ≥ 0.85 a pares con head nouns distintos siempre que compartan ese adjetivo. Cualquier umbral entre 0.85 y 0.92 deja varias fusiones falsas que comprometen la utilidad del schema.

**Decisión:** la canonización semántica vía MiniLM se descarta para este run. El schema se queda con normalización superficial pura. Los 858 tipos canónicos y los 1.578 predicados normalizados son la firma léxica cruda del corpus tal como el modelo la produjo. La FASE 2.3 evaluará si esa cruda granularidad sirve o estorba a las preguntas downstream.

### 4.4 Backstop estructural (definido, no necesitó actuar)

Como guardarraíl frente a violaciones residuales de la regla 1 del protocolo (no modelar jerarquía documental), antes del ensamblaje se aplica un filtro determinístico: cualquier nodo cuyo `type_raw` normalizado matchee uno de los siguientes 5 patrones se descarta, junto con sus edges:

```
^comunicacion_(a|b)
^ley(_nacional)?$
^decreto
^resolucion
^circular
```

Resultado: **0 nodos dropeados**, **0 edges dropeados**. El refuerzo del SYSTEM_PROMPT (regla 2, sección de versionado y marco normativo) ya había eliminado al 100 % las violaciones; el backstop existe como red de seguridad en caso de variantes léxicas no anticipadas.

(La iteración previa del SYSTEM_PROMPT sin esa regla había producido ~58 nodos `Comunicación BCRA` solo en el TO de Protección. Tras refinar el prompt y re-correr el smoke, el conteo cayó a 0. Detalle en `report.md`, sección de iteraciones.)

---

## 5. Decisiones más generales bajo la estrategia

1. **Una entidad por nodo, label como identificador corto** (reglas 5 y 6 del SYSTEM_PROMPT): las enumeraciones se desagregan ("los bancos públicos, privados y cooperativos" → 3 entidades) y los labels son frases nominales cortas (mediana = 4 palabras, p90 = 8, máx = 18). La elaboración va en `description`.
2. **Provenance obligatorio en cada nodo y cada edge** (regla del protocolo). En nodos se preserva además `properties.all_provenances` con todas las observaciones cross-chunk. La `location` es `p.<página>` o `p.<a>-<b>` cuando el chunk abarca varias páginas; `pypdf` no produce estructura de secciones limpia, por lo que el detalle interno del chunk solo aparece cuando Haiku lo identificó explícitamente en `location_hint`.
3. **Predicados crudos preservados** en `edges[].properties.predicate_raw`. La métrica comparativa del experimento es justamente la verbosidad léxica del vocabulario de relaciones; truncarla en la normalización superficial la habría arruinado.
4. **`properties.version = "vigente"`** en todos los nodos. Para este experimento se modela solo la versión vigente de cada TO (regla 2 del protocolo).
5. **Modelo de extracción: Claude Haiku 4.5** (`claude-haiku-4-5`), temperature 0, max_tokens_out 16 384. Concurrency 3 (lección Run 1), backoff conservador (3 reintentos, base 2.0).

---

## 6. Tamaño del schema (resumen para comparación FASE 2.3)

| Métrica | Valor |
|---|---:|
| Tipos canónicos únicos | 858 |
| Predicados normalizados únicos | 1.578 |
| Predicados crudos únicos | 1.603 |
| Singletons en tipos | 351 |
| Singletons en predicados | 1.038 |
| Nodos con > 1 type_raw | 438 (13 %) |
| Nodos cross-TO (mismo slug en ≥ 2 TOs) | 110 |

La estrategia produce un schema mucho más grande que cualquier vocabulario controlado típico. La hipótesis del experimento es que **alta cobertura** se paga con **baja consistencia**, y la FASE 2.3 medirá en qué proporción.
