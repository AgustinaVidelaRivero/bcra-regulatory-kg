# Pre-registro — ablación de retrieval sobre KG-Refinado (U-A1.3 · plan de tesis A1.3 → corrida en A1.4)

Estado: **LAUDADO por la autora (2026-08-17) — umbrales y decisiones SELLADOS; fase B
autorizada y ejecutada** (fase A de U-A1.3 sobre HEAD `49f82b7`). Las marcas
**[LAUDO]** registran la decisión tomada; el borrador previo con las alternativas
queda en el paquete de revisión de la fase A. El commit de la autora con este
archivo + los pares sellados (`pares/`) es el sello. A1.4 es unidad aparte con
mandato propio y NO puede modificar nada de lo que este documento fija.

Pregunta que responde la ablación (sub-pregunta (ii) de la tesis, "retrieval ≠
estructura"): sobre el MISMO grafo, ¿cuánto de la brecha literal→anti-léxica de
navegabilidad (KG-Refinado en EV2: recall consultada micro 0,958 → 0,620,
`data/experiment/ev2_corrida/navegabilidad/reporte_navegabilidad.md` §4) se debe
al algoritmo de búsqueda (booleano por label/id vs BM25 sobre label+descripción+id)
y cuánto a la expresividad de las tools de navegación (v1 vs v2)?

Todo número de este documento tiene su comando o archivo reproducible; los
scripts viven en `data/experiment/ablacion_retrieval/` y se corren desde la raíz
del repo con `.venv/bin/python -B data/experiment/ablacion_retrieval/<script>.py`.

---

## §1 Diseño: factorial 2×2 sobre KG-Refinado

**Grafo:** KG-Refinado (`data/experiment/grafo_v2/reensamblado_v3/kg.json`, sha256
`26fac8b49f6c08c1aa364b47273d36958d831f240d4e6b4ee7700b6a0bff3571`), servido por el
contenedor Neo4j de U-A1.1 (label `:KG_Refinado`, `KG_Meta.kg_sha256` verificado
por `neo4j/cargar_kg.py --solo-verificar` antes de cada celda).

**[LAUDO 1 — ratificado] Alcance de grafos: solo KG-Refinado.** Correr ambos grafos
duplica el costo de A1.4 (§6) sin cambiar la sub-pregunta (ii); KG-Reextraído entra
recién en A1.5/B1.8 con la configuración ganadora.

**Factores.** Cada factor es un PAQUETE {función + spec que lee el modelo + línea
del prompt del sistema}, no tres factores sueltos (laudo de cierre de U-A1.2). Las
dos líneas de prompt son EXACTAMENTE las aprobadas en U-A1.2
(`agente_v2._REEMPLAZOS_PROMPT`, importadas por `celdas.py`, no re-tipeadas):

| Factor | nivel 0 | nivel 1 |
|---|---|---|
| **R** — retriever de `buscar_nodos` | `booleano`: `Neo4jIndex(modo='paridad').buscar_nodos` (réplica byte-idéntica del `GraphIndex.buscar_nodos` del harness, 322/322 en U-A1.1) + spec `harness.TOOLS['buscar_nodos']` + línea 1 del prompt del harness | `bm25`: `Neo4jIndex(modo='fulltext').buscar_nodos` (= `ToolsV2.buscar_nodos_v2`) + spec `specs_tools_v2.json['buscar_nodos']` + línea 1 del prompt v2 ("búsqueda de texto completo (BM25) de nodos por label, id y descripción") |
| **T** — tools de navegación (`ver_vecinos`; `ver_nodo` es byte-idéntica en todas) | `v1`: `Neo4jIndex.ver_vecinos(id, direccion)` (byte-idéntico al harness) + spec `harness.TOOLS['ver_vecinos']` + línea 3 del prompt del harness | `v2`: `ToolsV2.ver_vecinos_v2(id, relacion, pagina, por_pagina)` (bidireccional siempre, paginación offset, filtro por relación) + spec `specs_tools_v2.json['ver_vecinos']` + línea 3 del prompt v2 |

**Celdas** (id, orden de corrida pre-registrado; archivos `celdas/celda_<id>.json`
con el prompt y las specs EXACTOS que verá el modelo, generados por `celdas.py`
desde las piezas selladas y verificables con `celdas.py --check`):

| celda | R | T | rol | sha256 prompt del sistema | sha256 specs (json canónico) | sha256 archivo |
|---|---|---|---|---|---|---|
| `C00_booleano_v1` | booleano | v1 | **CONTROL** = harness VERBATIM (prompt y `TOOLS` byte a byte; aserción en `celdas.py`) | `001a5eee6fedbdba…` | `3f2e3263ca72ce00…` | `029a4ea62d2ed2d0…` |
| `C10_bm25_v1` | bm25 | v1 | efecto principal de R | `8e80984bffe5047e…` | `22f07517c32a63ed…` | `41881363348a8c14…` |
| `C01_booleano_v2` | booleano | v2 | efecto principal de T | `21e3f09181dce040…` | `1dc2ca96edd55f2e…` | `a934161be92ea5fe…` |
| `C11_bm25_v2` | bm25 | v2 | **paquete sellado de U-A1.2 VERBATIM** (`SYSTEM_PROMPT_V2_PROPUESTO` y `TOOLS_V2` byte a byte; aserción) | `85617ef3d98954fc…` | `cda004e5fe4d71a2…` | `803ed12d47b4d322…` |

sha completos: `celdas/manifest_celdas.json` (sha `380547439d8da67b…`). Comando:
`.venv/bin/python -B data/experiment/ablacion_retrieval/celdas.py --check` (exit 0).

**[LAUDO 3 — ratificado] Descomposición del paquete v2 en las celdas mixtas (cada
spec y línea de prompt viaja con su factor).** El paquete sellado de U-A1.2 describe BM25 en la spec y en la
línea 1 del prompt de `buscar_nodos`. Un 2×2 cruzable exige que en `C01_booleano_v2`
el modelo NO lea "BM25 … descripción" cuando el retriever es booleano (mentirle al
modelo sobre su tool contaminaría la celda), y que en `C10_bm25_v1` sí lo lea. Por
eso cada texto viaja con la función que describe: la spec y la línea 1 de
`buscar_nodos` siguen al factor R; la spec y la línea 3 de `ver_vecinos` siguen al
factor T. Consecuencias: (i) `C11_bm25_v2` == paquete A1.2 verbatim y
`C00_booleano_v1` == harness verbatim (verificado); (ii) el "factor tools v2" de
A1.4 es el sub-paquete `{ver_vecinos_v2 + su spec + su línea de prompt}` — sigue
siendo UN factor (función+spec+prompt), no tres. Alternativa descartada: usar el
paquete verbatim en las dos celdas v2 (la celda `{booleano, v2}` quedaría con una
spec falsa; se declararía como confusor conocido).

**Piezas selladas por sha256** (`comun_ablacion.PIEZAS_SELLADAS`; todo script de
este directorio y de A1.4 aborta si alguna cambia — `comun_ablacion.py` exit 0):

| pieza | sha256 |
|---|---|
| `data/experiment/evaluacion/loader.py` | `5aba8b7a0aa46e8d5c4c83b33884b8cae7d0a099884a7d3bc935de4d3097af8b` |
| `data/experiment/evaluacion/harness.py` | `fd267e833866f86850e43130e627b08d78e05523b97484696de0ab0c8c9fba9e` |
| `data/experiment/evaluacion/judge.py` | `7169145aaeb3f2d90a7e3873964378aa6520c5688fed136cf5a79ea63b589eaa` |
| `data/experiment/evaluacion/llm_cache.py` | `fc86b0e48df464d01d87aa1d8067168d2d522f66ead53f594092a16484c22752` |
| `data/experiment/grafo_v2/reensamblado_v3/kg.json` (KG-Refinado) | `26fac8b49f6c08c1aa364b47273d36958d831f240d4e6b4ee7700b6a0bff3571` |
| `data/experiment/neo4j/indices.py` (CAMPOS_FULLTEXT, ANALYZER) | `215b4b8783345479f2b9e730c6e6b6e0be740163ba9a5796377b4672335ace26` |
| `data/experiment/neo4j/neo4j_index.py` (modos paridad/fulltext, clamps) | `5f38db1b915caf8a4cd71e0f7f0d281ba5a9ca6867d327a9e0f4aac67cd2d0c1` |
| `data/experiment/neo4j/grafos.py` | `eb78280b1358db095be0ab08bfa8ff934bf881f86b80c9b00a40e06d9cec8d57` |
| `data/experiment/neo4j/agente_neo4j.py` | `403a9b4295961f461c73a35b46ccc4d973a20cefdddf2ae97b50231dd7a3576a` |
| `data/experiment/agente_v2/tools_v2.py` | `22d672709a59678cf070c1af9f1ee6240bf0cdb860a5d23600fd7a51ff9cf16e` |
| `data/experiment/agente_v2/specs_tools_v2.json` | `88b696258b69eaee1b047b235b026763380ea9f14707d31398e6ab2f4d598a55` |
| `data/experiment/agente_v2/agente_v2.py` (las 2 líneas de prompt: `_REEMPLAZOS_PROMPT`; `GraphAgentV2.ask`) | `7beb0037d45b317cc8b0e03fa996b54d21fdda9110ceebcc3ee4ef0d1f3e88a4` |
| `data/experiment/agente_v2/specs_diff_v1_v2.txt` (diff citado) | `28bad98fb67b5b710c4cef7fda8a9eaec0ababda56ef74d1e8eb98d1b5772f32` |
| pipeline de sintéticas: `comun.py` / `sampler.py` / `generador.py` / `validador.py` / `resolucion.py` / `metrica.py` / `estimacion.py` / `runner_faseB.py` / `cliente_faseB.py` | `94c1d4fe…` / `01b0f0e6…` / `45f72fa4…` / `6791996e…` / `afe66ee9…` / `059f411b…` / `0ffad2ad…` / `0818d340…` / `e2191ca6…` (completos en `celdas/manifest_celdas.json`) |
| `data/experiment/exploracion/validar_anclas.py` / `mapa_territorio_quemado_5TOs_5sets.json` | `9efda31a…` / `d94f1c99…` |
| `data/experiment/ev2_corrida/code/metrica_ev2.py` (replay fuerte) | `5c629c00e993bd3a0e7b1aafdf95ae5fcf1cd695dff1c8018f1b16a766b99c75` |

Prompt del harness (texto en runtime) sha `001a5eee6fedbdba…`; prompt v2 propuesto
sha `85617ef3d98954fc…`; `harness.TOOLS` sha `3f2e3263ca72ce00…`; `TOOLS_V2` sha
`cda004e5fe4d71a2…` (`celdas/manifest_celdas.json`).

## §2 Configuración del retriever CONGELADA (no se ajusta mirando resultados)

Todo por referencia a archivos commiteados con sha (§1):

| parámetro | valor congelado | dónde |
|---|---|---|
| campos indexados (BM25) | `CAMPOS_FULLTEXT = ["label", "descripcion", "description", "id_texto"]` — `id_texto` laudado en U-A1.1 (decisión B.5 del README de neo4j) | `neo4j/indices.py:77` |
| analyzer | `ANALYZER = "spanish"` (stemming + stopwords de Lucene) | `neo4j/indices.py:78` |
| índice | `nodos_fulltext_kg_refinado` (uno por grafo; estadísticas BM25 sin mezcla) | `neo4j/grafos.py` |
| ranking BM25 | `score DESC, size(label) ASC, id ASC`; score NO expuesto; `tokens_matcheados` con la fórmula del harness (puede ser 0); `total_con_match` = hits Lucene | `neo4j/neo4j_index.py:169–204` |
| tokenización de la consulta | `harness._tokens` (lowercase, sin acentos, `[a-z0-9]+`), unida por espacios → query OR | ídem |
| retriever booleano | `\|tokens(consulta) ∩ tokens(label+id)\|`, orden `(-score, len(label), id)` (réplica en `modo='paridad'`, byte-idéntica) | `neo4j/neo4j_index.py:130–167` |
| top-K | `limite` default 10; clamp 1..50; no entero → 10 (igual en ambos retrievers) | `harness.py`, `neo4j_index.py:113–116`, `tools_v2.LIMITE_DEFAULT` |
| `ver_vecinos` v1 | `(id, direccion='ambas')`, ventana 40 por dirección, orden de `kg.edges` (`r.orden`), flags `*_truncado` | `neo4j_index.py:226–272` |
| `ver_vecinos` v2 | `(id, relacion=None, pagina=1, por_pagina=40)`, `POR_PAGINA_MAX = 40`, bidireccional siempre, paginación offset sobre `r.orden`, filtro exacto | `agente_v2/tools_v2.py:115–117, 175–245` |
| agente | `MODEL = claude-haiku-4-5-20251001`, `TEMPERATURE = 0`, `MAX_TOKENS = 2048`, `MAX_TOOL_CALLS = 15`, `TRUNC_TOOL_OUTPUT = 1200`, prompt/`_collect_provs`/`_cita_fiel`/`QuestionTrace` del harness | `evaluacion/harness.py:47–59` |
| loop del agente | `GraphAgentV2.ask` = copia de `GraphAgent.ask` con exactamente 2 sustituciones (`system=self.system_prompt`, `tools=self.tools`), verificada textualmente (116 líneas, U-A1.2 §H) | `agente_v2/agente_v2.py` |

**Regla:** ninguno de estos valores se modifica antes, durante ni después de la
corrida de A1.4 en función de resultados. Si A1.4 encuentra un defecto de
implementación (no de configuración), lo declara y frena; no lo corrige en silencio.

## §3 Material: pares sintéticos NUEVOS con el pipeline reusado

**Pipeline importado sin editar** (`data/experiment/exploracion/sinteticas/`,
fase A `a611ed2` selftest 37/37, fase B `5ceb816` 98 → 64 aptos, 810 llamadas,
USD 2,20): sampler estratificado E-A…E-E (20 por estrato; E-B mitad `entrante`;
E-D 15 intra + 5 inter-TO), generador literal + evolución anti-léxica, validador de
4 puertas (a resolución/censo, b auto-contención incl. `b_fuga_ancla`, c quemado
5 sets, d solape léxico ≤ 0,15 y mismo gold), checks LLM V1/V2/V3, reintento único
de descartadas, métrica por replay. **Único cambio: la semilla**
`sinteticas-faseA-v3` (`comun_ablacion.SEMILLA_V3`). El grafo muestreado es
KG-Refinado (sha `26fac8b4` verificado por `comun.load_kg_raw` antes de muestrear).
Gold = anclas de provenance de los nodos respuesta (`gold.anclas`), invariante
entre grafos. Reuso por inyección de atributos de módulo (`runner_faseB.SAMPLES_PATH`
/ `OUT_*`, `cliente_faseB.TOPE_USD`, `ClienteFaseB(db_path=…)`): ningún archivo del
pipeline se edita (`generar_pares_v3.py`, docstring).

**Muestreo en seco (fase A, $0, hecho):** `muestreo_v3.py` →
`muestreo/samples_v3.json` (sha `e72c5d21b6412f5d57501ba3cc867cbfb8b935c89ced249f3f096eb8f00667aa`;
doble corrida byte-idéntica), `muestreo/resumen_muestreo_v3.json`
(sha `38e902d7…`), `muestreo/estimacion_faseB_v3.json` (sha `4605e6b0…`).

| | E-A | E-B | E-C | E-D | E-E | total |
|---|---|---|---|---|---|---|
| samples (semilla v3) | 20 | 20 (10 saliente / 10 entrante) | 18 | 20 (15 intra / 5 inter) | 20 | **98** |
| población de la que se muestrea (antes del gate de quemado) | 2.167 aristas elegibles | 3.740 nodos de inicio | **29 hubs** (grado ≥ 10, elegibles, todos con familia 3–25) | 699 pares (600 intra / 99 inter) | 4.463 nodos con ancla | |
| descartes del sampler (quemado 5 sets) | 12 | 16 | 11 | 118 (+3 nodo repetido) | 15 | 175 |
| anclas gold por TO (samples) | cap 7 / ext 14 / ric 1 | cap 4 / ext 15 / pro 2 | cap 6 / ext 17 | cap 4 / cla 3 / ext 12 / ric 1 | cap 8 / ext 10 / pro 1 / ric 1 | 62 anclas únicas (cap 29 / cla 3 / ext 68 / pro 3 / ric 3 sobre 106 menciones) |
| huérfanos de label entre los nodos gold (definición en §5 P6) | 5/20 nodos (5 samples) | 4/20 (4) | 19/155 (10) | 4/20 (4) | 1/20 (1) | 33/235 nodos, 24 samples |

Censo de las 106 anclas gold en KG-Refinado (`AnclaIndex`, 20 contenedores
excluidos): **0 ausentes** (esperado: se muestreó de este grafo); nodos gold por
sample min 4 / mediana 29 / máx 212 (granularidad de ancla gruesa, misma que en
EV2 → la métrica agrega POR ANCLA); puertas mecánicas (a) y (c) OK en 98/98;
selftest del runner con cliente stub sobre `samples_v3.json`: PASS (18 llamadas
esperadas = 18). El sesgo por TO (ext/cap dominan) es el del grafo (nodos con ancla:
ext 1.798, cap 1.504, cla 508, ric 357, pro 339) más el quemado, idéntico al de la
corrida de EV2 por construcción.

**HALLAZGO (detectado SIN abrir material EV2) — colisión estructural: E-C es
idéntico a EV2 bajo cualquier semilla.**
La población de hubs es de 29; el gate de quemado deja pasar 18; el sampler
recorre TODOS los hubs hasta juntar 20 y elige por hub la familia enumerable
mayor de forma determinística. Con cualquier semilla, E-C = los mismos 18 hubs
con la misma familia (cambia solo la numeración `EC-nnn`). Medido sin abrir
material EV2 (solo poblaciones): E-C solapa al 100 % con el estrato E-C de EV2 a
nivel de ancla y de subgrafo, y el prompt de generación sería el mismo (misma
pregunta esperable). Los otros estratos tienen solapamiento esperado bajo
(E-A ≈ 20·20/2.167 ≈ 0,2 samples; E-D ≈ 0,6; E-E ≈ 0,1; E-B ≈ 0). Solo 7 de los 18
hubs tienen una segunda familia enumerable apta; bajar el umbral de grado
(diagnóstico: ≥ 8 → 25 hubs aptos, ≥ 7 → 41, ≥ 6 → 57) sería un cambio de diseño.
La causa es estructural: población chica (29 hubs) + gate de quemado + selección
determinística del sampler ⇒ identidad con EV2 a nivel de ancla y de subgrafo bajo
cualquier semilla. **[LAUDO 2 — ratificada la opción O1]: la fase B se corre SIN
E-C** (`generar_pares_v3.py --preparar --estratos E-A,E-B,E-D,E-E` → 80 samples).
E-C queda fuera del material nuevo de la ablación por identidad estructural con
EV2 (no por defecto del estrato); **P4 se mide sobre E-B/entrantes**
(bidireccionalidad, blanco de BKL-0027) **y sobre la clase `hit_tool_limit`** —
los hubs de E-C tienen grado 10–32, por debajo de la ventana de 40, así que E-C
tampoco ejercitaba la paginación. Alternativas descartadas: incluir E-C como
cohorte "compartida con EV2" reportada aparte; ampliar la población de hubs
(umbral ≥ 6, 57 aptos) — cambio de diseño.

**N.** Con el laudo 2, **N = 80 samples** (los 98 de la semilla v3 menos los 18 de
E-C; ~52 aptos al rendimiento conocido 64/98). Alternativas medidas
(`muestreo/estimacion_faseB_v3.json`, `escenarios_N`): 46 → ~30 aptos, USD 1,03–1,35;
60 → ~39, USD 1,35–1,77; 98 → ~64, USD 2,20–2,89. Con O1 el N efectivo es 80
(~52 aptos, USD ≈ 1,80–2,36). La estimación con la fórmula del pipeline
(`estimacion.estimar`, supuestos S1–S5, 816.716 tokens de entrada / 125.176 de
salida para 98 samples con factor 1,6 de descarte) da **USD 2,885** al precio
de Sonnet 5 (2 / 10 USD por MTok); el estimador empírico de `5ceb816`
(2,20 USD / 98 samples) da **USD 2,20**; para N = 80: 2,36 / 1,80. Todos bajo el
**tope de USD 3,00** de la fase B de esta unidad; la fórmula sobre-estimó también
aquella corrida (2,55 vs 2,20). **Re-verificación previa a la primera llamada
(2026-08-17, `https://platform.claude.com/docs/en/about-claude/pricing`): modelo
`claude-sonnet-5` = USD 2 / MTok entrada, 10 / MTok salida — el precio introductorio
pasó a ser el estándar (la suba a 3/15 del 1/9/2026 no ocurrirá); coincide con lo
estimado, sin recálculo.**

**Procedimiento de la fase B (solo con autorización explícita con precios y tope):**
`--preparar [--estratos …]` (escribe `muestreo/samples_v3_faseB.json`, $0) →
`export ABLACION_TOPE_USD=3.00` → `--todo --autorizado` = calibración (2 samples por
estrato: 8 sin E-C) + gate de cordura (≥ 3 aptos, si no frena y reporta) + resto con
reintento único; db propia `cache/ablacion_faseB_v3.db` (gitignore local),
`run_label ablacion_faseB_v3`, modelo `claude-sonnet-5` sin `temperature` y con
thinking deshabilitado (peculiaridades verificadas en `5ceb816`), tope duro en el
cliente. Luego `validar_pares_v3.py` → `pares/pares_v3.json` (SET a sellar: aptos
con literal, anti-léxica, gold en anclas, tokens prohibidos, solapes),
`registro_generacion_v3.json` (todos los intentos con motivo),
`censo_kg_refinado_v3.json`, `validacion_v3.json` (re-verificación de las 4 puertas,
distribución por estrato/sub-estrato/TO, solape), `manifest_pares_v3.txt` (sha256 de
todo). FRENO con el manifest; el commit de la autora sella. Selftests con stub (0
API): `generar_pares_v3.py --selftest` PASS; `validar_pares_v3.py --selftest` PASS.

El chequeo de solapamiento de anclas de los pares nuevos contra EV2 lo hace la mesa
en revisión (material EV2 no abierto en esta unidad). **Resultado de la mesa:**
solapamiento de anclas con el eje sintético de EV2: 28/37, dentro del esperado por
la estructura del pool (175 anclas elegibles, concentrado) — análisis en
`anexo_solapamiento_anclas.md`; identidad de pares verificada: 0.

**Resultado de la fase B (ejecutada 2026-08-17, `pares/`):** 80 samples (sin E-C) →
**50 pares aptos** (E-A 13/20 · E-B 18/20 [9 entrante / 9 saliente] · E-D 8/20
[7 intra / 1 inter] · E-E 11/20; rendimiento 62,5 % vs 65 % en `5ceb816`), 128
intentos, 18 rescatados por el reintento único; descartes por motivo (sobre
intentos): V2 gold no único 46, V1 no auto-contenida 37 lit. / 36 anti-léx.,
`b_fuga_ancla` 22, V3 par divergente 16, largo 1. Re-verificación mecánica de las 4
puertas sobre los 50 aptos: OK; censo en KG-Refinado: 0 anclas ausentes, nodos gold
por par min 5 / mediana 29 / máx 212; anclas gold por TO cap 16 / ext 34 / pro 2 /
ric 1; solape léxico literal mediana 0,177 (máx 0,69), anti-léxica mediana 0,000
(máx 0,12 ≤ 0,15). **Huérfanos de label (P6) entre los aptos: 11 pares** (E-A 4,
E-B 4, E-D 2, E-E 1; lista en `pares/validacion_v3.json` → `huerfanos_p6`).
**Gasto real desde la db** (`cache/ablacion_faseB_v3.db`, tabla `cache`, una fila por
llamada pagada): 768 llamadas a `claude-sonnet-5`, 455.887 tokens de entrada +
78.388 de salida = **USD 1,6957** (2 / 10 por MTok), contador del cliente 1,6956,
tope 3,00 respetado; `stop_reason` `end_turn` en 768/768. Set a sellar:
`pares/pares_v3.json` (sha en `pares/manifest_pares_v3.txt`).

*Desvíos declarados de la fase B:* (1) la corrida `--todo` (calibración 7/8 aptos,
gate superado; resto en curso) **abortó en ED-008 reintento 2**: el modelo devolvió
dos bloques ```json``` con un comentario intermedio y `generador._parse_pregunta`
(estricto) lanzó `JSONDecodeError`; el runner no persiste `preguntas_faseB` hasta el
final, así que los registros del resto se perdieron en memoria — pero TODAS las
llamadas pagadas quedaron en la db (never-pay-twice). (2) Corrección en la capa de
esta unidad, sin editar el pipeline: cliente `ClienteFaseBTolerante` que, solo para
prompts de generación/evolución y solo si el texto entero no parsea, toma el
PRIMER objeto `{"pregunta": …}` completo (crudo íntegro en la db; registro en
`pares/gasto_cliente_faseB_v3.json` → `parseos_tolerados`); afectó **1 respuesta**
(la literal de ED-008 reintento 2, que resultó apto — la mesa puede excluir ese par
si lo considera). (3) **Reanudación** con `--resto --autorizado --gasto-previo 1.0101`
(el tope duro pasa a ser acumulado): 702 accesos, **379 hits de caché** (lo ya pagado)
+ 323 misses nuevos; gasto acumulado 1,0101 + 0,6855 = 1,6956. Los hits de esta
reanudación son legítimos y declarados (no son cross-hits: una sola db, mismos
prompts). (4) La calibración fue de 8 samples (2 por estrato, sin E-C), no 10.

## §4 Métrica y corrida (de A1.4; acá solo se pre-registra)

- **Métrica primaria (determinística, sin juez):** recall de gold **por ancla**,
  `vista` (algún nodo del censo del ancla apareció en un `buscar_nodos`) y
  `consultada` (recibió `ver_nodo` o llegó por `ver_vecinos`), y brecha
  vista-sin-consultar, con `metrica.evaluar_por_anclas` (pipeline, sin editar) y
  el censo local en KG-Refinado (`AnclaIndex` sin contenedores). Agregados micro
  (pooled por ancla) y macro (promedio por caso) por celda × variante × estrato,
  exactamente como `ev2_corrida/navegabilidad/agregados_navegabilidad_ev2.py`.
  Resultado primario pre-registrado: **recall consultada micro, anti-léxica, por
  celda**, y la **brecha** `Δ_c = recall_c(literal) − recall_c(anti-léxica)` por celda.
- **Replay determinístico de TODA traza, estándar y fuerte** (0 divergencias
  exigidas): celdas v1 con `metrica.evaluar_por_anclas(index=Neo4jIndex(grafo,
  modo))` tal cual — para el control además se cruza con `GraphIndex` in-memory
  (paridad sobre trazas reales); celdas v2 con un re-ejecutor v2-aware inyectado por
  atributo de módulo (`metrica._reejecutar_step`; `ver_vecinos` con
  `relacion/pagina/por_pagina`), sin editar `metrica.py`; replay fuerte contra
  `steps_full` (outputs íntegros persistidos por el runner, patrón `runner_ev2.py`)
  con igualdad exacta. Cualquier divergencia invalida la celda.
- **Agente:** Haiku congelado del harness (`claude-haiku-4-5-20251001`, T=0, 15
  tool calls), `GraphAgentV2.ask` verificado, subclase por celda que carga
  `celdas/celda_<id>.json`, verifica su sha contra `manifest_celdas.json` y
  despacha `_run_tool` según el backend de la celda (§1). Trazas persistidas con
  `steps_full`, `raw_turns_agent` y metadatos (celda, sha de prompt/specs,
  `graph_fingerprint`, `code_version`).
- **N = 1 por par por celda** (2 variantes × ~52–64 pares × 4 celdas ≈ 416–512
  trazas). Justificación: la métrica es determinística dado la traza y el agente
  corre a T=0 (EV2 base también fue N=1 con replay 336/336); N=3 triplicaría el
  costo sin cambiar el estimador de la brecha, y el diseño APAREADO (mismo par en
  las 4 celdas) absorbe la varianza entre pares. Análisis: diferencias apareadas por
  par entre celdas con IC bootstrap 95 % (semilla `bootstrap-ablacion-v1`, 10.000
  remuestreos, determinístico); ningún test se agrega después de ver los datos.
- **Cachés/labels por celda:** una db por celda (`ablacion_<celda>.db`),
  namespace `agent|gfp=<KG-Refinado>|cv=<sha del harness + sha de la celda>|think=0`;
  **0 cross-hits exigido**: al cierre, `cache_stats.hits == 0` en cada db (una
  db fresca por celda; toda reanudación tras interrupción se declara con su
  conteo de hits, nunca se calla). Payloads del control byte-idénticos al harness
  (paridad) ⇒ el control replica el fenómeno conocido con el mismo modelo, prompt
  y tools que EV2.
- **Orden de corrida:** celdas en el orden `C00, C10, C01, C11`; dentro de cada
  celda los (par, variante) en orden aleatorio con semilla `orden-ablacion-v1`
  (mismo orden en las 4 celdas). Reanudación por caso (idempotente); freno por
  proyección de gasto (§6).
- **Latencia end-to-end por pregunta** (p50/p95 desde `latency_s` de las trazas y
  latencia de tools por llamada) se registra como secundaria, sin predicción.
- **Clases medibles por replay** (definiciones fijadas acá):
  `hit_tool_limit` = campo `hit_tool_limit` de `QuestionTrace` (True cuando
  `tool_calls_used ≥ 15`; en EV2 base sobre KG-Refinado, 46/128 trazas de
  navegabilidad tuvieron `tools ≥ 15`, `resumen_ev2_base_v3.json`);
  `vista_no_consultada` = par×variante cuyo control (`C00`) tiene alguna ancla
  vista y no consultada (`n_brecha > 0` en la traza de `C00`);
  `huérfano_de_label` (§5 P6) fijado ANTES de generar, sobre los samples.

## §5 PREDICCIONES — umbrales SELLADOS [LAUDO 4]

Referencia conocida (EV2 base, KG-Refinado, control equivalente): recall
consultada micro literal 0,958 → anti-léxica 0,620 (Δ_c = 0,338; macro 0,359);
recall vista 1,000 → 0,845; brecha v-s-c 3 → 17 anclas de 71.

- **P1 (control / gate de validez del material).** `C00_booleano_v1` reproduce el
  fenómeno: caída literal→anti-léxica del recall consultada **`Δ_c ≥ 0,15`** (esperada
  ≈ 0,3). Si no se cumple, el material nuevo no mide lo mismo que EV2 y la corrida se
  declara inválida para P2–P6 (se reporta igual, sin re-correr).
- **P2 (central).** Con BM25 y las mismas tools (`C10` vs `C00`), la brecha se
  reduce **al menos a la mitad**: `Δ_c(C10) ≤ 0,5 · Δ_c(C00)`; y la reducción de la
  brecha en `C11` vs `C01` cumple lo mismo.
- **P3 (no regresión literal).** En las variantes literales, BM25 no reduce el
  recall consultada respecto del booleano más allá de **0,05**:
  `recall_c,lit(C10) ≥ recall_c,lit(C00) − 0,05` (ídem `C11` vs `C01`); y el recall
  vista literal no baja más de 0,05.
- **P4 (tools — direccional, sobre E-B/entrantes y `hit_tool_limit`).** Tools v2
  mejora la consultada: (i) en el sub-estrato **E-B/entrante** (bidireccionalidad,
  blanco de BKL-0027), `recall_c(C01) > recall_c(C00)` y `recall_c(C11) > recall_c(C10)`
  (dirección, sin umbral de magnitud); (ii) la proporción de trazas con
  `hit_tool_limit` baja de v1 a v2 con el mismo retriever, y entre los (par,
  variante) con `hit_tool_limit` o `n_brecha > 0` en `C00`, la fracción que pasa a
  consultada en `C01` es mayor que en el resto; (iii) el efecto de T sobre el recall
  consultada anti-léxico (`C01 − C00`) es menor que el de R (`C10 − C00`).
- **P5 (interacción).** La mejor celda es `C11_bm25_v2` en recall consultada
  anti-léxico, y la ganancia es ≈ aditiva: `|conjunto − suma| =
  |(C11 − C00) − [(C10 − C00) + (C01 − C00)]| ≤ 0,10` (micro, anti-léxica).
- **P6 (negativa, huérfanos de label tipo BKL-0022).** Definición pre-registrada y
  ya medida sobre los samples ANTES de generar (`muestreo/resumen_muestreo_v3.json`
  → `huerfanos_label`): un nodo gold es huérfano de label si NINGÚN token de
  contenido de su label, buscado solo con `buscar_nodos(token, 10)` booleano, lo
  trae al top-10 (33/235 nodos gold en los 98 samples; los que caen en los pares
  aptos sin E-C se listan en `pares/validacion_v3.json` → `huerfanos_p6`).
  Predicción sobre esos gold huérfanos: (i) **BM25 NO mejora** su `vista` respecto
  del booleano (fracción vista en `C10` ≤ `C00` + 0,10; evidencia previa fuera del
  agente en U-A1.2: BKL-0022 2/7 → 2/7 en top-10); (ii) **SÍ resultan alcanzables
  con tools v2 vía paginación/bidireccionalidad**: fracción `consultada` en las
  celdas v2 mayor que en v1 (vía `ver_vecinos` desde un vecino), condicionada a que
  el agente pagine (se reporta la tasa de llamadas con `pagina > 1`).

Regla de lectura: cada predicción se declara **cumplida / no cumplida / no
evaluable** (n insuficiente declarado a priori: una clase con < 8 pares se reporta
como no evaluable). Las cohortes (E-E núcleo limpio; E-A…E-D dirigida) se reportan
por separado y jamás promediadas entre sí (protocolo EV2 §1).

## §6 Presupuesto de A1.4

Fórmula (la del harness, sin precios): `costo = Σ_trazas [tokens_in·P_in +
cache_write·1,25·P_in + cache_read·0,10·P_in + tokens_out·P_out] / 10⁶`
(`harness.py:576–579`; P_in/P_out del modelo del agente). Referencia publicada:
EV2 base = 456 trazas = USD 14,88 (`resumen_ev2_base_{run3,v2,v3}.json`, suma de
`costo_usd`), es decir USD 0,0326 por traza; sobre KG-Refinado solo navegabilidad,
128 trazas = USD 3,742 → USD 0,0292 por traza. Estimación:

| escenario | pares aptos | trazas (4 celdas × 2 variantes) | USD @0,0292 | USD @0,0326 |
|---|---|---|---|---|
| O1 (sin E-C, 80 samples) | ~52 | ~416 | 12,2 | 13,6 |
| 98 samples (mesa) | ~64 | ~512 | 15,0 | 16,7 |
| **tope de A1.4 [LAUDO 5]: USD 20** (autorización de gasto en la unidad A1.4) | | | (≈ +20 % sobre 16,7: payload v2 ≈ +1–2 %, trazas BM25 de largo desconocido) | |

Freno por proyección: si el gasto acumulado proyectado al total de la celda supera
la cuota de la celda (tope/4), la corrida se detiene y reporta (protocolo EV2 §5).
El plan estimaba A1.4 en ~USD 12; la diferencia viene de 4 celdas × 2 variantes.
Tope de la **fase B de ESTA unidad: USD 3,00** (§3).

## §7 Reglas

1. **Una sola corrida** de la factorial (4 celdas × todas las (par, variante)).
   Nada se ajusta mirando sus resultados para re-correrla; una re-corrida solo por
   defecto de implementación declarado, con laudo, y se rotula como corrida 2.
2. **EV2 jamás entra**: ni preguntas, ni criterios, ni pares sintéticos de EV2, ni
   trazas de `ev2_corrida`; los agregados publicados se citan como referencia.
   La configuración ganadora se elige con ESTE material y se mide en EV2 una sola
   vez en A1.5 (principio 7).
3. **Desvíos se declaran, no se corrigen en silencio** (mensaje de commit + reporte).
4. Las predicciones y umbrales se leen tal como quedaron sellados; ningún umbral
   se toca después de ver una traza.
5. Piezas selladas por sha (§1): cualquier cambio en harness, backend, tools v2,
   pipeline de sintéticas o kg.json invalida el pre-registro (`comun_ablacion.py`
   lo detecta).
6. Nombres de personas: ninguno; toda decisión se documenta por su justificación técnica.
7. Al cerrar A1.4: reporte pegable + paquete de revisión con manifest sha256 +
   propuesta de actualización de `docs/plan_tesis.md`.

---

## Anexo — inventario del directorio `data/experiment/ablacion_retrieval/` (fase A)

| archivo | qué es |
|---|---|
| `preregistro_ablacion.md` | este documento |
| `README.md` | comandos y mapa del directorio |
| `comun_ablacion.py` | rutas, piezas selladas por sha, `verificar_piezas()` |
| `celdas.py` → `celdas/celda_*.json`, `celdas/manifest_celdas.json` | las 4 celdas (prompt + specs + backend) selladas |
| `muestreo_v3.py` → `muestreo/samples_v3.json`, `resumen_muestreo_v3.json`, `estimacion_faseB_v3.json` | muestreo en seco, censo, huérfanos, selftest stub, estimación |
| `generar_pares_v3.py` | fase B (runner reusado por inyección; gating de autorización y tope) |
| `validar_pares_v3.py` → `pares/…` | validación completa + set a sellar + manifest |
| `.gitignore` | local: `cache/`, `__pycache__/` |
