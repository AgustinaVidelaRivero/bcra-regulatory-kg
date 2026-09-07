# Mapa de fuentes del capítulo «Diseño y validación del esquema del grafo» (U-CAP-ESQ)

Patrón: `docs/tesis/mapa_fuentes_intro.md`. Regla (main.tex + skill
latex-udesa + CLAUDE.md §4.i): en la prosa del capítulo entra un número solo si
tiene fila acá, con el archivo que lo respalda, el commit que lo sella y el
comando que lo recomputa. Un número sin fila va a §«No verificables» y no se
usa hasta resolverse.

**Estado: tramo 1 TUNEADO (cierre del tuneo 06/09).** Decisiones de estructura
registradas en el tuneo: el capítulo del esquema va ANTES del de construcción
(título «Diseño y validación del esquema del grafo», label `cap:esquema`; el de
construcción queda «Construcción del grafo», label `cap:construccion`); el
tramo 1 queda en tres subsecciones — «La unidad de extracción y la partición
del corpus», «El esquema de partida» y «La elección del paradigma cerrado» —;
en la prosa se usa «relación» / «tipo de relación», con «predicado» solo en la
primera mención como nombre técnico; el experimento de cinco estrategias se
cuenta completo como EVIDENCIA DE DISEÑO (tabla `tab:cinco_estrategias`), no
como resultado de la tesis. Las filas 1–27 son del tramo 1 original; las filas
28–40 entran con el tuneo. Los tramos 2–5 agregan sus filas a esta misma tabla.

**Excepción registrada (heredada del mapa de la Introducción):** los números que
la prosa atribuye a trabajos citados no llevan fila de recómputo propia; se
respaldan en la fuente citada y en su verificación contra PDF registrada en
`docs/mapa_related_work.md`. Se listan igual (filas 26 y 40) para dejar el
origen explícito.

## Convención de recómputo

Todos los comandos de la columna «recómputo» se corren desde la raíz del repo y
no hacen llamadas a la API (costo USD 0).

## Tabla de números citables — tramo 1

### §3.1 — La unidad de extracción y la partición del corpus

| # | Número en la prosa | Archivo (repo) | Commit | Recómputo |
|---|---|---|---|---|
| 1 | Conjunto de desarrollo: **cinco** Textos Ordenados | `data/experiment/escalado_prep/referencia_subset.json` (cinco claves: `pro`, `cla`, `ric`, `cap`, `ext`) | `111ed19` | `python3 -c "import json;print(len(json.load(open('data/experiment/escalado_prep/referencia_subset.json'))))"` |
| 2 | La numeración de puntos llega a **cuatro** niveles en el conjunto de desarrollo | mismo archivo, `censo.nodos_por_profundidad` de cada TO (claves `1`–`4` en los cinco) | `111ed19` | `python3 -c "import json;d=json.load(open('data/experiment/escalado_prep/referencia_subset.json'));print({k:max(map(int,v['censo']['nodos_por_profundidad'])) for k,v in d.items()})"` |
| 3 | El índice oficial registraba **157** Textos Ordenados | `data/experiment/escalado_prep/inventario_resumen.json`, clave `urls_unicas` (158 entradas con 1 duplicado descartado) + `indice_oficial_raw.json` | `111ed19` | `python3 -c "import json;print(json.load(open('data/experiment/escalado_prep/inventario_resumen.json'))['urls_unicas'])"` |
| 4 | Conjunto de desarrollo: **564** páginas | `data/experiment/escalado_prep/referencia_subset.json`, suma de `paginas` | `111ed19` | `python3 -c "import json;d=json.load(open('data/experiment/escalado_prep/referencia_subset.json'));print(sum(v['paginas'] for v in d.values()))"` |
| 5 | Conjunto de desarrollo: **1.763** unidades de extracción | mismo archivo, suma de `unidades_extraccion` (= 1.477 chunks terminales + 286 mini-chunks) | `111ed19` | `python3 -c "import json;d=json.load(open('data/experiment/escalado_prep/referencia_subset.json'));print(sum(v['unidades_extraccion'] for v in d.values()))"` |
| 6 | Universo a escalar: **152** Textos Ordenados | `data/experiment/escalado_prep/inventario_resumen.json`, clave `filas_inventario` (157 − 5 del conjunto de desarrollo, listados en `subset_excluido`) | `111ed19` | `python3 -c "import json;d=json.load(open('data/experiment/escalado_prep/inventario_resumen.json'));print(d['filas_inventario'], d['urls_unicas']-len(d['subset_excluido']))"` |
| 7 | Universo inventariado **con el sha256 de cada archivo** | `data/experiment/escalado_prep/manifest_pdfs.sha256` (152 líneas, una por PDF) | `111ed19` | `wc -l < data/experiment/escalado_prep/manifest_pdfs.sha256` |
| 8 | Universo a escalar: **6.757** páginas | `data/experiment/escalado_prep/inventario_unidades.csv`, columna `paginas` | `111ed19` | `python3 -c "import csv;print(sum(int(r['paginas']) for r in csv.DictReader(open('data/experiment/escalado_prep/inventario_unidades.csv'))))"` |
| 9 | Universo a escalar: **8.010** unidades de extracción | mismo CSV, columna `unidades_extraccion` (= 6.670 chunks terminales + 1.340 mini-chunks) | `111ed19` | `python3 -c "import csv;print(sum(int(r['unidades_extraccion']) for r in csv.DictReader(open('data/experiment/escalado_prep/inventario_unidades.csv'))))"` |
| 10 | **68** Textos Ordenados cuya estructura la segmentación vigente reconoce | `data/experiment/escalado_prep/veredictos_generalizacion.json`, `por_to[*].veredicto == "digerible"`; coincide con la columna `veredicto` del CSV | `111ed19` | `python3 -c "import json,collections;print(collections.Counter(v['veredicto'] for v in json.load(open('data/experiment/escalado_prep/veredictos_generalizacion.json'))['por_to'].values()))"` |
| 11 | Los 68 reúnen **2.009** páginas | `inventario_unidades.csv`, filas con `veredicto == digerible` | `111ed19` | `python3 -c "import csv;print(sum(int(r['paginas']) for r in csv.DictReader(open('data/experiment/escalado_prep/inventario_unidades.csv')) if r['veredicto']=='digerible'))"` |
| 12 | Los 68 reúnen **6.340** unidades de extracción | mismo CSV, mismo filtro | `111ed19` | `python3 -c "import csv;print(sum(int(r['unidades_extraccion']) for r in csv.DictReader(open('data/experiment/escalado_prep/inventario_unidades.csv')) if r['veredicto']=='digerible'))"` |
| 13 | **84** Textos Ordenados requieren reglas de parseo todavía no escritas | `veredictos_generalizacion.json`, `veredicto == "necesita reglas"` (68 + 84 = 152) | `111ed19` | mismo comando de la fila 10 |
| 14 | En **62** de ellos la segmentación no produce ninguna unidad | `inventario_unidades.csv`, filas con `unidades_extraccion == 0` | `111ed19` | `python3 -c "import csv;print(sum(1 for r in csv.DictReader(open('data/experiment/escalado_prep/inventario_unidades.csv')) if int(r['unidades_extraccion'])==0))"` |
| 15 | La partición se resuelve **con criterios mecánicos, sin intervención de un modelo de lenguaje** | `data/experiment/escalado_prep/resumen_escalado.md` (encabezado: «Gasto de esta unidad: **USD 0** (cero llamadas a LLM)») + umbrales `C4`–`C8` de `veredictos_generalizacion.json` | `111ed19` | `python3 -c "import json;print(json.load(open('data/experiment/escalado_prep/veredictos_generalizacion.json'))['umbrales'])"` |
| 28 | **Títulos oficiales de los cinco TOs** del conjunto de desarrollo: «Protección de los usuarios de servicios financieros», «Clasificación de deudores», «Capitales mínimos de las entidades financieras», «Exterior y cambios.» (el índice trae punto final; la prosa lo omite) y «RI Cont. Mensual - Exigencia e integración de capitales mínimos» (grupo `regimenes_informativos`; la prosa lo parafrasea como «el régimen informativo de exigencia e integración de capitales mínimos») | `data/experiment/escalado_prep/indice_oficial_raw.json`, entradas con `archivo` ∈ {t-pusf, t-cladeu, t-capmin, t-excbio, t-ri-cm}.pdf; la correspondencia subset→archivo sale de `data/raw/manifiesto.csv` (`archivo_local` → `url_origen`, commit `27d7090`) | `111ed19` | `python3 -c "import json,csv;idx=json.load(open('data/experiment/escalado_prep/indice_oficial_raw.json'));m={r['archivo_local'].rsplit('/',1)[-1]:r['url_origen'].rsplit('/',1)[-1].lower() for r in csv.DictReader(open('data/raw/manifiesto.csv'))};[print(k,'->',m[k],'->',[e['titulo'] for e in idx['textos_ordenados']+idx['regimenes_informativos'] if e['archivo'].lower()==m[k]]) for k in ['TO_proteccion_usuarios_servicios_financieros_actual.pdf','TO_clasificacion_deudores_actual.pdf','TO_capitales_minimos_actual.pdf','TO_exterior_cambios_actual.pdf','TO_regimen_informativo_contable_mensual_actual.pdf']]"` |
| 29 | Criterio de selección del subset: **cinco dominios regulatorios distintos**, **cuatro** documentos de normativa general y **uno** de régimen informativo (de forma más tabular), tamaños **de 40 a 204 páginas** | `docs/schema/experiment_protocol.md:21-25` («Justificación del subset»: diversidad temática / estructural / de tamaño); el rango 40–204 se recomputa de `referencia_subset.json` | `4c8479d` | `sed -n '21,25p' docs/schema/experiment_protocol.md; python3 -c "import json;p=[v['paginas'] for v in json.load(open('data/experiment/escalado_prep/referencia_subset.json')).values()];print(min(p),max(p))"` |
| 30 | «**El escalado del recurso comienza por esos 68 Textos Ordenados y avanza sobre los restantes a medida que se escriben sus reglas de parseo**» | `docs/laudo_B5.5_alcance_corpus_y_catalogo.md` (línea 22: «Los **68 TOs digeribles primero**…», corpus de extracción de tandas 1–2) + `docs/adenda_laudo_B5.5_segmentacion_universal.md` (los 84 restantes deben volverse segmentables con reglas mecánicas de parseo; commit `a06cdab`) | `c0daef1` | `grep -n 'digeribles primero' docs/laudo_B5.5_alcance_corpus_y_catalogo.md; grep -n 'deben volverse segmentables' docs/adenda_laudo_B5.5_segmentacion_universal.md` |

Descripción de la unidad de extracción (punto terminal + cadena de herencia
estructural; mini-chunk para los contenedores con prosa propia) y del mecanismo
«chapeau perdido» que la motiva: `docs/diseno_reextraccion_v2.md` §3, etapa E0
(`a8fa053`). No aporta números a la prosa.

Encuadre desarrollo/test («cinco Textos Ordenados … sobre el que se construyó y
se validó el método»): `docs/plan_tesis.md`, laudo D-g firmado 27/08/2026
(`c0daef1`). No aporta números a la prosa; ya declarado en la Introducción.

### §3.2 — El esquema de partida

| # | Número en la prosa | Archivo (repo) | Commit | Recómputo |
|---|---|---|---|---|
| 16 | **Seis** tipos de entidad que el extractor puede emitir, con el desglose 3 deónticos + 1 acto regulado + 2 de anclaje documental | `data/experiment/grafo_v2/code/schema.py`, `ENTITY_TYPES`; el desglose se lee de `DOMAIN_RANGE` (`TextoOrdenado`/`Comunicacion` son los extremos de `establecida_en`, `referencia` y `modificada_por`) | `fac503f` | `python3 -c "import sys;sys.path.insert(0,'data/experiment/grafo_v2/code');import schema;print(len(schema.ENTITY_TYPES), schema.ENTITY_TYPES)"` |
| 17 | Un **séptimo** tipo, `Sujeto`, en el grafo pero no en el vocabulario del extractor | mismo archivo: `Sujeto` aparece en `DOMAIN_RANGE` y NO en `ENTITY_TYPES`; procedencia del catálogo en `docs/spec_extraccion_v2.md` §2 y §4.1 (`29c40ce`) | `fac503f` | `python3 -c "import sys;sys.path.insert(0,'data/experiment/grafo_v2/code');import schema;t=set();[t.update(d|r) for d,r in schema.DOMAIN_RANGE.values()];print(len(t), sorted(t-set(schema.ENTITY_TYPES)))"` |
| 18 | **Doce** tipos de relación (lista completa en la prosa) y su matriz de dominio y rango | mismo archivo: `PREDICATES` (12) y `DOMAIN_RANGE` (12 firmas) | `fac503f` | `python3 -c "import sys;sys.path.insert(0,'data/experiment/grafo_v2/code');import schema;print(len(schema.PREDICATES), len(schema.DOMAIN_RANGE));print(schema.DOMAIN_RANGE['aplica_a'], schema.DOMAIN_RANGE['exceptua'], schema.DOMAIN_RANGE['establecida_en'])"` |
| 31 | El **68 %** de las relaciones que vinculan una norma con su sujeto apuntaba a un único nodo genérico (censo de la versión anterior del esquema: **991 de 1.464** aristas `aplica_a` al nodo «Sujetos obligados») | `docs/esquema_v2_diseño.md:23` (censo del 14/07/2026); recomputable directo del grafo sellado `data/experiment/run_3_ppf_core/kg.json` | `29c40ce` | `python3 -c "import json,collections;kg=json.load(open('data/experiment/run_3_ppf_core/kg.json'));a=[e for e in kg['edges'] if e['relation']=='aplica_a'];t=collections.Counter(e['target'] for e in a).most_common(1)[0];print(t, len(a), round(100*t[1]/len(a)))"` |
| 32 | Análisis de corpus **sin modelo de lenguaje** sobre una muestra de comunicaciones y **tres** Textos Ordenados completos (muestra exacta: 100 Comunicaciones A + 50 Comunicaciones B + 3 TOs; la prosa lo dice en cualitativo) | `docs/schema/corpus_analysis_for_schema.md:8-14` («Sample base»; «Cero LLM, todo análisis local») | `27d7090` | `sed -n '3,14p' docs/schema/corpus_analysis_for_schema.md` |
| 33 | La matriz rechazó **304** relaciones sobre el conjunto de desarrollo; **196** de ellas con la misma forma (**142** `Operacion --aplica_a--> Sujeto` + **54** `Excepcion --aplica_a--> Sujeto`) | `data/experiment/esq/scoping_esq1.md:362-369` (304) y `:391-401` (desglose), commit `94bb7a7`; artefacto primario: `data/experiment/reextraccion_v2/corpus_v2/salida/*/extracciones_e1.jsonl` (`5273c0c`). RECONCILIACIÓN 1.769 vs 1.763 (verificada 06/09): el jsonl tiene 1.769 líneas = **1.763 chunk_ids únicos** (iguales por TO a `referencia_subset.json`: pro 101, cla 143, ric 84, cap 462, ext 973) **+ 6 líneas de reintento** del ratchet para `cap::3.1.14.1`, `cap::4.2.1.2`, `cap::4.3.3.1`, `cla::9.2`, `ext::4.7.1`, `ext::8.5.20.3` (primer intento con rechazo de validación o `max_tokens`, segundo intento adosado al archivo). El **304 es idéntico bajo ambas definiciones** (todas las líneas, o solo el último intento por unidad); los 6 rechazos de los intentos superados son todos del motivo `entities_o_relations_invalidos` (7 con todas las líneas vs 1 con solo el último intento) | `94bb7a7` | `python3 -c "import json,glob,collections,re;F=[json.loads(l) for p in glob.glob('data/experiment/reextraccion_v2/corpus_v2/salida/*/extracciones_e1.jsonl') for l in open(p)];print(len(F),len({d['chunk_id'] for d in F}));R=[r for d in F for r in (d.get('validacion') or {}).get('rechazos',[]) if r['motivo']=='firma_invalida'];C=collections.Counter(re.search(r':\\s*(\\S+) --(\\S+)--> (\\S+)',r['detalle']).groups() for r in R);print(len(R), C[('Operacion','aplica_a','Sujeto')], C[('Excepcion','aplica_a','Sujeto')])"` |
| 34 | Figura F1 (`fig:esquema_partida`): **7** cajas (6 tipos + pseudo-tipo `Sujeto`) y **17** flechas = expansión exacta de las **12** firmas de `DOMAIN_RANGE`; generada por script desde `schema.py`, con freno por `AssertionError` si los conteos no son los sellados | `docs/tesis/figuras/LEEME_figura_esquema_partida.md` §4 y §6 + `docs/tesis/figuras/generar_figuras_esquema.py` (ambos entran con este commit); fuente importada: `schema.py` sha256 `cc98e435…` | `fac503f` | `python3 -c "import re;print(sorted(__import__('collections').Counter(re.findall(r'data-pred=\"([^\"]+)\"', open('docs/tesis/figuras/figura_esquema_partida.svg').read())).items()))"` (17 en total, 12 predicados) |

Dirección de ejemplo «el punto 3.17.1.4»: es la misma dirección del ejemplo de
la Introducción (Figura `fig:norma_a_grafo`, TO de Exterior y cambios; LEEME en
`docs/tesis/figuras/LEEME_figura_norma_a_grafo.md`). Es una dirección del
corpus, no un tally; no lleva fila de recómputo.

### §3.3 — La elección del paradigma cerrado

| # | Número en la prosa | Archivo (repo) | Commit | Recómputo |
|---|---|---|---|---|
| 19 | El experimento construyó **cinco** grafos en paralelo, variando solo la estrategia de esquema | `data/experiment/evaluacion/frozen_run/reporte_final.md`, encabezado («eval\_set\_v1 (23 preguntas) × 5 grafos × N=3») y tabla §1 (`run_1`…`run_5`) | `d56020e` | `grep -n '5 grafos' data/experiment/evaluacion/frozen_run/reporte_final.md` |
| 20 | **23** preguntas | mismo archivo, mismo encabezado | `d56020e` | `grep -n '23 preguntas' data/experiment/evaluacion/frozen_run/reporte_final.md` |
| 21 | **19** preguntas con respuesta | mismo archivo, §1 («Totales answerable por grafo (19 preguntas)») | `d56020e` | `grep -n 'answerable por grafo' data/experiment/evaluacion/frozen_run/reporte_final.md` |
| 22 | **15** correctas (schema-light, `run_4`) contra **16** (esquema cerrado, `run_3`) | mismo archivo, tabla de totales answerable de §1 | `d56020e` | `grep -A 9 'Totales answerable' data/experiment/evaluacion/frozen_run/reporte_final.md` |
| 23 | Estabilidad **86 %** (schema-light) contra **93 %** (cerrado) | mismo archivo, §2, columna «Estabilidad»: `run_4` 79/92 (86 %), `run_3` 86/92 (93 %) | `d56020e` | `sed -n '/## 2. Dimensiones cerradas/,/TOTAL/p' data/experiment/evaluacion/frozen_run/reporte_final.md` |
| 24 | **14** citas a nivel de punto contra **20** | mismo archivo, §2, columna «prec punto/pag/aus»: `run_4` 14/3/5, `run_3` 20/1/2 | `d56020e` | mismo comando de la fila 23 |
| 25 | Agotamiento del límite de consultas **49 %** contra **38 %** | mismo archivo, §2, columna `hit_limit`: `run_4` 34/69 (49 %), `run_3` 26/69 (38 %) | `d56020e` | mismo comando de la fila 23 |
| 26 | TextMineX: **160** tipos de entidad y **86** relaciones | `docs/mapa_related_work.md`, fila R5 (ampliación verificada contra el PDF, v4 27/01/2026) — número de terceros, cubierto por la excepción registrada. TUNEO 06/09: la prosa ya NO afirma «el error se desplaza a la elección de la relación» — esa lectura quedó marcada como INTERPRETACIÓN de la mesa (no hallazgo del paper) en la propia fila R5; los porcentajes del abstract entran por la fila 40 | `d2a32ef` | `grep -n 'TextMineX' docs/mapa_related_work.md` |
| 27 | Menú de **cinco** ampliaciones evaluadas, con el reparto **dos** admitidas / **una** diferida / **dos** rechazadas | `data/experiment/esq/laudo_ESQ-3a_retoques.md` §1 («Decisión madre»): escalones 1 y 2 SÍ, 3 DIFERIDO, 4 y 5 RECHAZADOS | `0a76549` | `sed -n '/## §1. Decisión madre/,/## §2/p' data/experiment/esq/laudo_ESQ-3a_retoques.md` |
| 35 | Tamaños de los cinco esquemas de la tabla: **10 / libres** (receta genérica), **12 / 23** (vocabulario controlado), **7 / 12** (esquema cerrado), **858 / 1.578** (emergente), **20 / 511** (híbrido, núcleo **4 / 5**) | `run_1_cookbook/schema.md` («Tipos de entidad (10)» + §3 predicados sin tipado cerrado; `e4de649`), `run_2_papers/schema.md:27,117` («Tipos de entidad (12)», «Total: 23 predicados»; `9e363a9`), `run_3_ppf_core/schema.md:3` («7 tipos de entidad, 12 tipos de relación»; `58581b6`), `run_4_schema_light/schema.md:23,90` («858» tipos canónicos, «1.578» predicados normalizados; `689fe3b`), `run_5_hybrid/schema.md:11` (núcleo 4/5) + `run_5_hybrid/report.md:181-182` («20 (4 core + 16 emergentes)», «511 (5 core + 506 emergentes)»; `199649c`) | ver fila | `grep -n 'Tipos de entidad (10)' data/experiment/run_1_cookbook/schema.md; grep -n 'Total: 23 predicados' data/experiment/run_2_papers/schema.md; grep -n '7 tipos de entidad, 12 tipos' data/experiment/run_3_ppf_core/schema.md; grep -n '858\|1.578' data/experiment/run_4_schema_light/schema.md | head -3; sed -n '181,182p' data/experiment/run_5_hybrid/report.md` |
| 36 | De las 23 preguntas, **10** de dato directo + **5** que combinan varias normas + **4** de restricción→excepción + **4** sin respuesta en el corpus; redactadas sin mirar los grafos y fijadas antes de correr la evaluación | `data/experiment/evaluacion/queries/eval_set_v1.json` (categorías `factual_directa` / `multi_norma` / `cadena_restriccion_excepcion` / `unanswerable`); el mensaje del commit sellador registra «diseño ciego a los KGs, ground truth verificado contra PDFs, pre-primera corrida del harness» | `7d118ee` | `python3 -c "import json,collections;print(dict(collections.Counter(q['categoria'] for q in json.load(open('data/experiment/evaluacion/queries/eval_set_v1.json'))['preguntas'])))"` |
| 37 | Protocolo detrás de la prosa sin número propio: cada pregunta se corrió **tres** veces por grafo (N=3); «límite de consultas» = 15 tool calls; «adjudicación humana de las afirmaciones que el juez no pudo verificar» (200 afirmaciones adjudicadas y firmadas); juez calibrado contra lectura humana en 12 trazas sin desacuerdos (25 celdas comparadas, 0 ❌) | `reporte_final.md:3` (× N=3; adjudicación firmada en `:5`), `data/experiment/evaluacion/harness.py:50` (`MAX_TOOL_CALLS = 15`; `7e8b91e`), `data/experiment/evaluacion/02_calibracion_juez.md` (tabla juez-vs-humano) | `d56020e` | `grep -n 'N=3' data/experiment/evaluacion/frozen_run/reporte_final.md; grep -n 'MAX_TOOL_CALLS' data/experiment/evaluacion/harness.py; grep -c '^| CQ-\|^| dev_unans' data/experiment/evaluacion/02_calibracion_juez.md; grep -o '❌' data/experiment/evaluacion/02_calibracion_juez.md | wc -l` (el único ❌ del doc es la leyenda) |
| 38 | TODAS las celdas de `tab:cinco_estrategias` — Correctas **13/15/16/15/13** (sobre 19); Estables **76/78/86/79/79** de **92** (**83/85/93/86/86 %**); Citas a punto **0/12/20/14/19** (sobre 23); Límite agotado **33/26/26/34/34** de **69** (**48/38/38/49/49 %**) | `reporte_final.md` §1 (totales answerable) y §2 (dimensiones cerradas). Recomputadas 06/09: sumas por categoría de §1 (9+3+1, 8+4+3, 9+3+4, 10+3+2, 8+3+2) cierran contra los totales; porcentajes redondeados verificados (76/92=82,6→83 … 34/69=49,3→49). 92 = 23 preguntas × 4 dimensiones; 69 = 23 × 3 repeticiones | `d56020e` | `sed -n '/Totales answerable/,/run_5/p' data/experiment/evaluacion/frozen_run/reporte_final.md; sed -n '/## 2. Dimensiones cerradas/,/TOTAL/p' data/experiment/evaluacion/frozen_run/reporte_final.md` |
| 39 | Por categoría: el emergente acertó las **10** de dato directo frente a **9** del cerrado; multi-norma débil en las cinco (**3 de 5** correctas para el ganador); el cerrado único sin errores en restricción→excepción (4/4) | `reporte_final.md` §1 (tabla grafo × categoría: `run_4` factual\_directa 10, `run_3` 9; `run_3` multi\_norma 3, cadena 4/4 y §5 salvedad) | `d56020e` | `sed -n '/## 1. Correctitud FINAL/,/Totales answerable/p' data/experiment/evaluacion/frozen_run/reporte_final.md` |
| 40 | TextMineX: mejoras de **44,2 %** (exactitud), **22,5 %** (alucinaciones), **20,9 %** (adherencia al formato) — números de terceros, cubiertos por la excepción registrada. Fuente: el ABSTRACT de arXiv:2509.15098 los afirma verbatim («improve extraction accuracy by up to 44.2%, reduce hallucinations by 22.5%, and enhance format adherence by 20.9%»; verificado en vivo por la mesa de tuneo 06/09 y re-verificado al sellar esta fila). NOTA: el 160/86 de la fila 26 NO está en el abstract; lo respalda la fila R5 del mapa RW contra el PDF (v4) | `docs/mapa_related_work.md`, fila R5 | `d2a32ef` | `grep -n '44,2' docs/mapa_related_work.md` |

Fundamento del rechazo del escalón 5 (schema-light pleno) y del escalón 4 (zona
de extensión): `laudo_ESQ-3a_retoques.md` §1 (`0a76549`), que remite a la misma
corrida congelada de las filas 19–25 y a la escalera de falsación. La prosa del
tramo 1 no cita números de la escalera: los aporta el tramo 3.

## No verificables

(vacía en el tramo 1 tuneado — todo número de la prosa tiene fila arriba.)

## Huecos declarados del tramo 1

Cosas que las fuentes del tramo respaldan pero que NO entraron a la prosa, con
el motivo:

1. **RAGulating y el KG legal como apoyos externos del rechazo del
   schema-light.** `laudo_ESQ-3a_retoques.md` §1 los invoca («mejora marginal y
   dependiente del umbral»; «solo logra T-Box sin instancias en su brazo LLM»),
   pero esas lecturas provienen de resúmenes internos y no de una fila
   verificada contra PDF en `docs/mapa_related_work.md`. Quedan fuera de la
   prosa hasta que exista esa verificación; el apoyo externo del tramo se
   sostiene solo en R5 (filas 26 y 40). Ambas entradas ya existen en
   `bibliografia.bib` (`agarwal2025ragulating`, `damato2025legalkgvaw`), de modo
   que promoverlas cuesta solo la verificación de la afirmación.
2. ~~La survey schema-based vs schema-free sin entrada bibliográfica
   posible.~~ **RESUELTO en el tuneo (06/09):** la mesa de tuneo verificó
   arXiv:2510.20345 en vivo (autor, título, v1 23/10/2025, abstract con la
   dicotomía schema-based/schema-free); `bian2025survey` entró a
   `bibliografia.bib` y la prosa la cita en la primera oración de §3.3.
3. ~~La decisión de alcance del corpus a escalar fuera de las fuentes de
   §1.~~ **RESUELTO en el tuneo (06/09):** la oración del escalado por los 68
   entró a la prosa de §3.1 con la fila 30 (laudo B5.5 + adenda). La autora
   amplió además el alcance a los 84 (adenda a B5.5, segmentación universal);
   la prosa de §3.1 queda con la versión verdadera de hoy y se reescribe
   cuando esa unidad selle.

## Entradas nuevas en `bibliografia.bib` (tramo 1)

| clave | trabajo | fila de origen | verificación |
|---|---|---|---|
| `zhou2025textminex` | Zhou, Solmaz, Cirillo, Gashteovski y Fürst, *TextMineX: Data, Evaluation Framework and Ontology-guided LLM Pipeline for Humanitarian Mine Action*, arXiv:2509.15098 | `docs/mapa_related_work.md`, fila **R5** (`d2a32ef`) | metadatos verificados contra PDF por la mesa revisora (03/09); la fila registra v1 18/09/2025 y v4 27/01/2026, y la lectura citada corresponde a v4. Tuneo 06/09: entrada reformulada por la mesa de tuneo (una sola versión, con `note` de versión consultada), idéntica en repo y Overleaf |
| `bian2025survey` | Bian, *LLM-Empowered Knowledge Graph Construction: A Survey*, arXiv:2510.20345 | exigencia 10 del mapa RW | verificada por la mesa de tuneo contra arXiv en vivo (06/09): autor Haonan Bian, v1 23/10/2025, abstract con los paradigmas schema-based/schema-free; re-verificada al sellar este mapa |

## Figuras del capítulo

Decisión del tuneo (06/09): **F1 = esquema de PARTIDA**, insertada en §3.2
(`fig:esquema_partida`, `figuras/figura_esquema_partida.png`); **F1b = esquema
CONGELADO** con los agregados resaltados, reservada para la sección del
congelado (todavía no se inserta). Ambas generadas por
`docs/tesis/figuras/generar_figuras_esquema.py` desde los artefactos sellados,
con LEEME propio (`LEEME_figura_esquema_partida.md`,
`LEEME_figura_esquema_congelado.md`) y freno por `AssertionError` si los
conteos difieren de los sellados. El comentario `% [TODO: figura F1 …]` del
esqueleto queda superado. Conteos de F1: fila 34. F2 (árbol del catálogo de
sujetos) corresponde al tramo 2; F3–F5: sin cambios respecto del esqueleto
aprobado.
