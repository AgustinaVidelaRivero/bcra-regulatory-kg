# Inventario U-CITA — insumos para una métrica de exactitud de cita

Unidad de solo lectura, USD 0, sin git. Generado el 2026-09-17. Este
documento es la única escritura de la unidad. Releva qué existe; **no propone
la métrica ni cruza las citas de las respuestas contra nada** (freno del
mandato). Todo conteo se recomputó contra el artefacto citado; los comandos
están en la sección 7 («Reproducción»). Los hashes de commit que aparecen (`9c44516`, `185e042`, etc.)
están transcriptos de documentos del repo y quedan **NO VERIFICADOS** contra
la historia git, porque el mandato prohíbe correr git.

Lecturas del mandato que declaro (regla d):

- El mandato habla de «respuestas de referencia». El set sellado **no tiene**
  respuesta de referencia en prosa, por diseño:
  `docs/diseno_ev2.md:133` («NO se redacta respuesta esperada en prosa»). El
  gold es ancla + criterios (`docs/diseno_ev2.md:125-131`). Mandan los archivos.
- El freno dice «no correr nada sobre las respuestas» y la pregunta 4 pide un
  conteo por expresión regular sobre las respuestas. Corrí **solo** ese
  conteo de formato (pregunta 4) y el relevamiento de campos ya persistidos en
  las trazas; no computé (a), (b) ni (c) de la pregunta 6 sobre ninguna
  respuesta.
- El inventario U-INV-EVAL (d.2) que cita el mandato: **NO ENCONTRADO** en el
  repo (`grep -rIl "INV-EVAL\|INV_EVAL"` sobre el árbol, excluyendo `.git` y
  `.venv`, vacío). No pude leer su texto; ver §8.1.

---

## 1. Conjunto de evaluación sellado

- **Ruta:** `data/experiment/exploracion/ev2_fidelidad/preguntas_ev2_fidelidad.json`
- **sha256:** `1d58733699c325c90510e1ead5f18eac6c3cd970ee3b0ab7ff141da539162b40`
  (`shasum -a 256 <ruta>`). Coincide con el valor esperado en
  `data/experiment/ev2_r1/code/comun_r1.py:103`, con la línea `gold` de
  `data/experiment/ev2_r1/sellos/sellos_cierre_unidad.txt:8` y con
  `data/experiment/ev2_r1/preregistro_ev2_r1.md:13-15` (que lo declara
  idéntico al manifest del sello `9c44516`; commit NO VERIFICADO).
- **Conteo:** 40 preguntas / 164 criterios (comando de
  `docs/protocolo_corrida_ev2.md:34`, re-ejecutado: `40 164`).
- **Forma de cada pregunta** (las 40 idénticas): claves
  `id, to, to_nombre, pregunta, gold`; `gold` = `{ancla, criterios}`; cada
  criterio = `{criterio, cita_textual}`. Ejemplo:
  `preguntas_ev2_fidelidad.json:14-40` (EV2F-001).
- **Respuesta de referencia:** NO ENCONTRADO como campo (por diseño,
  `docs/diseno_ev2.md:133`).

## 2. Puntos de referencia por clave

**40 de 40 claves tienen al menos un punto de referencia**; las 40 tienen
**exactamente uno** (`gold.ancla`, lista de longitud 1, formato
`<to>:<punto>`). Ningún otro campo trae puntos: ni la pregunta ni los
criterios ni las citas textuales mencionan números de punto (barrido de §3).
El identificador de TO se traduce a archivo con
`data/experiment/reextraccion_v2/manifiestos/desarrollo_5tos.json:5-55`
(campos `id` / `archivo`).

Columnas: id → ancla (línea del `id` : línea del ancla en el JSON sellado).

| id | puntos_referencia | líneas | id | puntos_referencia | líneas |
|---|---|---|---|---|---|
| EV2F-001 | ext:6.11 | 14 : 20 | EV2F-021 | cap:8.6 | 614 : 620 |
| EV2F-002 | ext:5.10 | 43 : 49 | EV2F-022 | cap:6.11 | 647 : 653 |
| EV2F-003 | ext:5.3 | 72 : 78 | EV2F-023 | cap:8.3.2 | 676 : 682 |
| EV2F-004 | ext:2.6 | 101 : 107 | EV2F-024 | cap:2.11 | 709 : 715 |
| EV2F-005 | ext:4.6.1 | 130 : 136 | EV2F-025 | cla:2.1 | 738 : 744 |
| EV2F-006 | ext:7.7 | 163 : 169 | EV2F-026 | cla:3.5 | 767 : 773 |
| EV2F-007 | ext:13.3 | 192 : 198 | EV2F-027 | cla:6.1 | 796 : 802 |
| EV2F-008 | ext:10.6.2 | 225 : 231 | EV2F-028 | cla:3.1 | 825 : 831 |
| EV2F-009 | ext:5.7 | 250 : 256 | EV2F-029 | cla:4.1 | 846 : 852 |
| EV2F-010 | ext:6.10 | 283 : 289 | EV2F-030 | cla:10.3 | 867 : 873 |
| EV2F-011 | ext:5.8 | 312 : 318 | EV2F-031 | ric:7.2 | 896 : 902 |
| EV2F-012 | ext:10.8 | 345 : 351 | EV2F-032 | ric:9.2 | 925 : 931 |
| EV2F-013 | ext:3.17 | 370 : 376 | EV2F-033 | ric:12.4 | 958 : 964 |
| EV2F-014 | ext:13.5 | 399 : 405 | EV2F-034 | ric:4.2 | 987 : 993 |
| EV2F-015 | ext:3.13.1 | 428 : 434 | EV2F-035 | ric:5.2 | 1020 : 1026 |
| EV2F-016 | ext:9.5 | 457 : 463 | EV2F-036 | pro:1.3 | 1053 : 1059 |
| EV2F-017 | cap:5.2.1 | 486 : 492 | EV2F-037 | pro:2.1 | 1078 : 1084 |
| EV2F-018 | cap:6.5 | 519 : 525 | EV2F-038 | pro:2.4 | 1111 : 1117 |
| EV2F-019 | cap:4.2 | 552 : 558 | EV2F-039 | pro:2.5 | 1140 : 1146 |
| EV2F-020 | cap:2.4 | 581 : 587 | EV2F-040 | pro:4.4 | 1169 : 1175 |

Desglose por TO: ext 16 + cap 8 + cla 6 + ric 5 + pro 5 = 40 (coincide con
`dosificacion` del propio archivo).

Dato que condiciona la pregunta 6(b): el censo de anclas sobre r1
(`data/experiment/ev2_r1/censo/censo_anclas_fidelidad_r1.md:15`, sha256
`527e860b…`) da **31 resueltas / 9 no resueltas**: 7 por granularidad (el
punto existe en r1 solo como sub-puntos: EV2F-002, 009, 017, 024, 025, 032,
035) y 2 porque el portador es contenedor de más de 10 anclas (EV2F-013,
031) — filas `:21-29` del mismo archivo.

## 3. Criterios que exigen citar un punto o una fuente

**0 de 164.** Ningún criterio menciona un número de punto ni las palabras
«punto», «cita», «fuente» o «Texto Ordenado». Expresiones usadas sobre el
campo `criterio` (insensibles a mayúsculas):

- palabras: `\bpuntos?\b|\bcitas?\b|\bcitar\b|\bfuentes?\b|texto ordenado|\bT\.?O\.?\b`
- número de punto: `(?<![\d,\.])\d{1,2}\.\d{1,2}(?:\.\d{1,2}){0,3}\.?(?![\d%])`

Control por subcadena laxa (`punt|cit|fuent|ordenad`): un único acierto,
falso positivo — EV2F-008 c1, por «Soli**cit**ud Particular»
(`preguntas_ev2_fidelidad.json`, bloque de EV2F-008 desde `:225`).

**Dudosos (3)** — mencionan normas o leyes como *contenido* de la respuesta,
no como exigencia de citar el punto del TO:

| id | línea | texto literal |
|---|---|---|
| EV2F-012 c1 | `:355` | «Debe indicar que además de las condiciones de acceso aplicables se cumplen las normas de cancelación de deudas financieras.» |
| EV2F-036 c1 | `:1063` | «Debe indicar que las normas son complementarias de la legislación aplicable a las relaciones de consumo.» |
| EV2F-036 c2 | `:1067` | «Debe mencionar el Código Civil y Comercial, la Ley 24.240 de Defensa del Consumidor y la Ley 25.065 de Tarjetas de Crédito.» |

Consecuencia verificable: el juez de EV2 recibe pregunta, respuesta y
criterios (`data/experiment/ev2_fidelidad_eval/code/pipeline_fidelidad.py:137`)
y la respuesta que se le pasa es solo `trace.final_json.respuesta`
(`…/code/comun_fidelidad.py:143-152`): el campo `citas` del agente no llega
al juez y ningún criterio lo exige.

## 4. Corrida más reciente de fidelidad sobre r1

**Localización.** Unidad U-B1.8, `data/experiment/ev2_r1/` — declarada
«única medición» de r1 sobre EV2 (`data/experiment/ev2_r1/README.md:3-6`).
Grafo: `data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json`, sha256
`0226e947…196a` (en `meta.kg_sha256` de cada traza). Busqué otras corridas de
fidelidad sobre r1 por `grep -rln "salida_r1|KG_Reextraido_r1|r1_vigente"`
en `data/experiment` fuera de `ev2_r1/`: ninguna es corrida de evaluación.
La unidad tiene cuatro tandas de trazas de agente:

| tanda | ruta | trazas | fecha (`resumen_*.json:5`) | digest del directorio |
|---|---|---|---|---|
| base (N=1, las 40) | `ev2_r1/trazas/ev2_r1_base/` | 40 | 2026-08-23T18:02:50 | `d53316edd5082b562d542923d8c799c6355d5e2146f597741c77d5c035b5c25f` |
| encadenamiento rep 1 | `ev2_r1/trazas/ev2_r1_enc_r1/` | 24 | 2026-08-24T12:27:27 | `4b9499e91bb0b1e186d39ee478e5df23d31d8259e8ec8fff2449c009aba1fadd` |
| encadenamiento rep 2 | `ev2_r1/trazas/ev2_r1_enc_r2/` | 24 | 2026-08-24T13:13:36 | `de644c9295bd82918b1bd45b4e3c4e078e8c24503f779bee0031e154f984c437` |
| encadenamiento rep 3 | `ev2_r1/trazas/ev2_r1_enc_r3/` | 24 | 2026-08-24T12:50:22 | `a80cc1fb907d5aaeb510dedde1eac707c6206423033cce408aba10073b772ce7` |

Una corrida es un directorio, no un archivo: el «digest del directorio» es
sha256 sobre las líneas `<sha256 del archivo>  <nombre>\n` de los
`EV2F-*.json` ordenados por nombre (definición mía, reproducible con la sección 7; no
es un sello preexistente del repo). Shas de archivo individuales:
`resumen_ev2_r1_base.json` `eda00662…e488`; reporte de cierre
`ev2_r1/cierre/reporte_final_r1.md` `d8fb1994…3e82`. Tomo la **base** como
corrida de referencia (es la única que cubre las 40); las re-corridas de encadenamiento (§7 del protocolo de EV2) son
más recientes pero cubren 24 preguntas cada una.

**¿Las respuestas contienen citas de punto? Sí, en dos formas.**

1. **Cita estructurada** — campo `trace.final_json.citas`, lista de
   `{source_doc, location}`, exigida por el contrato de salida del harness
   congelado (`data/experiment/evaluacion/harness.py:85-92`; regla 3 del
   prompt, `:82-83`: las citas deben salir de provenances observadas).
2. **Mención en prosa** dentro de `final_json.respuesta` («…regulada en el
   Punto 6.11 del Texto Ordenado de Exterior y Cambios…»,
   `ev2_r1_base/EV2F-001.json:265`).

**Tres ejemplos literales (cita estructurada):**

- `ev2_r1_base/EV2F-001.json:266-271` (respondible=false, y aun así cita):
  `{"source_doc": "TO_exterior_cambios_actual.pdf", "location": "Punto 6.11"}`
- `ev2_r1_base/EV2F-014.json:266-283` (4 citas):
  `{"source_doc": "TO_exterior_cambios_actual.pdf", "location": "Punto 13.1.2"}`,
  `… "Punto 13.3.1"`, `… "Punto 13.3.2"`, `… "Punto 10.1"`
- `ev2_r1_base/EV2F-038.json:200-229` (7 citas):
  `{"source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf", "location": "Punto 2.4.2"}`,
  `… "Punto 2.3.1.1"`, `… "Punto 3.2.1.3"` (entre otras)

**Expresiones regulares declaradas:**

- cita estructurada parseable: `location` ~ `^Punto (\d+(?:\.\d+)*)\.?$` **y**
  `source_doc` ~ `^TO_[a-z_]+_actual\.pdf$`
- mención en prosa: `\b[Pp]untos?\s+(\d+(?:\.\d+)+)` sobre `respuesta`

**Conteos (corrida base, 40 respuestas, `parse_ok` 40/40):**

| medida | valor |
|---|---|
| respuestas con ≥ 1 cita estructurada parseable | **40 de 40** |
| citas estructuradas totales / parseables | 98 / 98 (0 no parseables) |
| desglose por archivo | ext 47 + cap 16 + pro 14 + cla 11 + ric 10 = 98 |
| `location` distintas | 90, todas de forma `Punto N(.N)*`; ninguna `Sección N` |
| respuestas con ≥ 1 mención en prosa | 17 de 40 (30 menciones) |
| respuestas con `respondible: false` | 9 de 40 — las 9 igual traen ≥ 1 cita |

Re-corridas de encadenamiento (72 trazas = 24 + 24 + 24): citas 67 + 63 + 62 = 192, todas
parseables; respuestas con ≥ 1 cita parseable 24 + 23 + 24 = 71 de 72 (la
única sin citas: `ev2_r1_enc_r2/EV2F-026.json`, `respondible: false`).

## 5. Procedencia en el registro de traza

**Sí, con una salvedad de forma.** Cada traza guarda `steps_full` con el
output íntegro de cada tool. En la base: 541 tool calls = 288 `buscar_nodos`
+ 181 `ver_nodo` + 72 `ver_vecinos`. De los 181 `ver_nodo`, 1 devolvió error
y **180 de 180 exitosos traen `provenances` con exactamente 1 entrada**, las
180 de forma `Punto N(.N)*`. Las 208 aristas listadas por `ver_vecinos`
traen también 1 provenance cada una. `buscar_nodos` no expone procedencia
(claves del ítem: `id, type, label, tokens_matcheados, resumen_propiedades`).

Ejemplo — `ev2_r1_base/EV2F-014.json:591-613` (step 4; `provenances` en
`:605-610`; transcripción abreviada, sin `properties`):

```json
{"n": 4, "tool": "ver_nodo",
 "input": {"id": "Obligacion_las_entidades_podran_dar_acceso_al_mercado_de_cambios_para_realizar_pagos_al_ext_4ecd09"},
 "output": {"id": "…_4ecd09", "type": "Obligacion",
  "label": "Cumplimiento condiciones para pagos importaciones",
  "provenances": [{"source_doc": "TO_exterior_cambios_actual.pdf", "location": "Punto 10.1"}]}}
```

Salvedad: la traza conserva la procedencia **ya adaptada** a
`{source_doc, location}`, no el campo crudo del grafo. El mismo nodo en
`salida_r1/kg.json` trae `provenance = {to: "ext", archivo, punto: "10.1",
rol_documental: "punto_propio", chunk_id: "ext::10.1", paginas: [130],
ancestros: ["S10"]}`. La vista runtime expone solo la procedencia
**primaria** (`ev2_r1/code/comun_r1.py:106-119`), mapeada por
`ev2_corrida/code/comun_ev2.py:134-145` (`punto` → `"Punto <punto>"`, o
`"Sección <n>"` si el punto es `S<n>`). En el kg crudo, 233 de 6.529 nodos
tienen más de una entrada en `provenances`; esas adicionales no llegan a la
traza, pero son recuperables por `id` de nodo desde el kg sellado.

Además, el harness ya persiste por traza (`harness.py:306-308`):
`seen_provenances` (unión deduplicada de las procedencias de **nodos y
aristas** vistas en `ver_nodo`/`ver_vecinos`, `:445-465`, `:511`),
`citations_unseen_raw` y `citations_unseen_normalized` (citas emitidas que no
están entre las vistas, `:551-560`, con la definición congelada de «cita
fiel» en `:323-375`). En la base: 3 citas no vistas sobre 98, en 2 trazas
(EV2F-014: 1, `:315-326`; EV2F-023: 2); en las 72 re-corridas de encadenamiento: 0. Estos
campos no los consume el pipeline de EV2 (grep de `citations_unseen` fuera de
trazas: solo `evaluacion/harness.py`, `evaluacion/judge.py:180,294`,
`evaluacion/analisis/run_manual.py`, `agente_v2/agente_v2.py` y dos docs de
tesis).

## 6. ¿Se puede computar sin juez?

| chequeo | veredicto | con qué | qué falta |
|---|---|---|---|
| **(a)** el punto citado existe en el corpus | **SÍ** | Índice estructural E0 por TO, `data/experiment/reextraccion_v2/e0_chunking/salida_enm01/estructura_<to>.json` (el que usó r1: `corpus_v2/r1_comun.py:29`): 1.864 nodos = ext 963 + cap 519 + cla 162 + ric 107 + pro 113. Mapa archivo↔TO en el manifiesto (§2). Citas 98/98 parseables. Controles hechos sobre clave y grafo, no sobre respuestas: las 40 anclas están en el índice (40/40) y los 1.706 pares (to, punto) distintos de r1 también (0 fuera; 70 entradas con `to` nulo, de nodos esqueleto). | Declarar la normalización (`Punto X` → `X`; forma `Sección N`) y qué cuenta como «existe» (nodo de la estructura vs. unidad de chunk: 7 de las 40 anclas son nodo de estructura pero no unidad de chunk). El índice tiene 4 niveles de profundidad como máximo; ver §8.2. Nota: para citas que ya están entre las procedencias vistas el chequeo es casi tautológico (r1 ⊂ índice); solo discrimina sobre citas no vistas. |
| **(b)** el punto citado está entre los puntos de referencia de la clave | **PARCIAL** | Ancla por clave 40/40 (§2) + citas parseables 40/40 (§4). El cómputo literal (igualdad exacta TO + punto) es posible hoy. | Tres decisiones que el repo no resuelve: (i) **granularidad** — 7 anclas no tienen en r1 ningún nodo con ese punto exacto (solo sub-puntos) y 2 caen en contenedores (§2): con igualdad exacta el acierto es inalcanzable para esas claves citando solo lo visto; (ii) **ancla única** — cada clave trae un solo punto, sin puntos secundarios admisibles, así que una cita complementaria legítima no se distingue de una errónea; (iii) **unidad de análisis** — por cita o por respuesta, y qué respuesta representa a cada pregunta (40 base vs. 72 re-corridas; las vías definitivas mezclan ambas: `ev2_r1/cierre/reporte_final_r1.md:14`), más el trato de las 9 abstenciones que igual citan. |
| **(c)** el punto citado está entre las procedencias de los nodos que el agente abrió | **SÍ** | Ya existe computado por traza contra `seen_provenances` (`citations_unseen_raw` / `_normalized`, §5). La versión estricta «nodos abiertos» se recomputa desde `steps_full` (180/180 `ver_nodo` exitosos con procedencia). | Elegir el universo: `seen_provenances` mezcla nodos **y aristas** (`ver_vecinos`); «nodos abiertos» a secas exige filtrar `steps_full` por `ver_nodo`. Solo procedencia primaria en traza (233 nodos de r1 tienen adicionales, recuperables del kg por `id`). Cobertura: 40/40 con `parse_ok`; una traza sin JSON final no tendría `citas`. |

## 7. Reproducción

Todos con `PYTHONDONTWRITEBYTECODE=1 python3 -B`, desde la raíz del repo.

```
# §1 — sha y conteo
shasum -a 256 data/experiment/exploracion/ev2_fidelidad/preguntas_ev2_fidelidad.json
python3 -B -c "import json; f=json.load(open('data/experiment/exploracion/ev2_fidelidad/preguntas_ev2_fidelidad.json')); ps=f['preguntas']; print(len(ps), sum(len(p['gold']['criterios']) for p in ps))"

# §2 — anclas por clave
python3 -B -c "import json,collections; ps=json.load(open('data/experiment/exploracion/ev2_fidelidad/preguntas_ev2_fidelidad.json'))['preguntas']; print(collections.Counter(len(p['gold']['ancla']) for p in ps)); [print(p['id'],p['gold']['ancla']) for p in ps]"

# §3 — barrido de criterios (R_KW y R_NUM = las dos expresiones de §3)
python3 -B -c "import json,re; R_KW=re.compile(r'\bpuntos?\b|\bcitas?\b|\bcitar\b|\bfuentes?\b|texto ordenado|\bT\.?O\.?\b',re.I); R_NUM=re.compile(r'(?<![\d,\.])\d{1,2}\.\d{1,2}(?:\.\d{1,2}){0,3}\.?(?![\d%])'); ps=json.load(open('data/experiment/exploracion/ev2_fidelidad/preguntas_ev2_fidelidad.json'))['preguntas']; cs=[c['criterio'] for p in ps for c in p['gold']['criterios']]; print(len(cs), sum(1 for t in cs if R_KW.search(t) or R_NUM.search(t)))"

# §4 — citas parseables por tanda (cambiar LAB)
python3 -B -c "import json,glob,re; LAB='ev2_r1_base'; RL=re.compile(r'^Punto (\d+(?:\.\d+)*)\.?$'); RD=re.compile(r'^TO_[a-z_]+_actual\.pdf$'); fs=sorted(glob.glob(f'data/experiment/ev2_r1/trazas/{LAB}/EV2F-*.json')); cs=[(json.load(open(f))['trace'].get('final_json') or {}).get('citas') or [] for f in fs]; ok=lambda c: bool(RL.match(c.get('location') or '') and RD.match(c.get('source_doc') or '')); print(len(fs), sum(map(len,cs)), sum(ok(c) for l in cs for c in l), sum(1 for l in cs if any(ok(c) for c in l)))"

# §4 — digest de directorio (cambiar LAB)
python3 -B -c "import glob,os,hashlib; LAB='ev2_r1_base'; h=hashlib.sha256(); [h.update((hashlib.sha256(open(f,'rb').read()).hexdigest()+'  '+os.path.basename(f)+'\n').encode()) for f in sorted(glob.glob(f'data/experiment/ev2_r1/trazas/{LAB}/EV2F-*.json'))]; print(h.hexdigest())"

# §5 — procedencia en ver_nodo de la base
python3 -B -c "import json,glob,collections; c=collections.Counter(); [c.update([(s['tool'], 'error' in s['output'], len(s['output'].get('provenances') or []) if s['tool']=='ver_nodo' else -1)]) for f in sorted(glob.glob('data/experiment/ev2_r1/trazas/ev2_r1_base/EV2F-*.json')) for s in json.load(open(f))['steps_full']]; print(c)"
```

## 8. Lo que no pude determinar

1. **El texto de U-INV-EVAL (d.2).** No está en el repo bajo ese nombre. La
   premisa «ningún componente mide la exactitud de cita» la contrasté solo
   contra lo que encontré: existe una medición de *cita vista vs. no vista*
   en el harness congelado (§5), que no es exactitud contra la clave; no sé
   si d.2 ya la registraba.
2. **Profundidad del índice E0.** La estructura llega a 4 niveles
   (`N.N.N.N`); las citas observadas también tienen 4 como máximo. No
   verifiqué contra los PDFs si existen sub-puntos más profundos que el
   índice no enumera.
3. **Coincidencia entre menciones en prosa y citas estructuradas.** Conté
   ambas por separado; cruzarlas es correr algo sobre las respuestas, fuera
   del freno.
4. **Naturaleza de las 3 citas no vistas** (EV2F-014, EV2F-023): si existen
   en el corpus o son fabricadas. Requiere el chequeo (a), no corrido.
5. **Hashes de commit** citados de documentos (`9c44516`, `185e042`,
   `774acac`, `bb89a8e`): NO VERIFICADOS (sin git). Los sha256 de archivo sí
   están recomputados.
6. **Que no exista otra corrida de fidelidad sobre r1 fuera de
   `data/experiment/`** (por ejemplo sesiones de la app en
   `sessions_server/`): no las relevé porque no son corridas sobre el set
   sellado; la afirmación «más reciente» vale dentro de `data/experiment/`.
7. **Estado de sellado por commit de las trazas de `ev2_r1/trazas/`**: los
   archivos de `sellos/` cubren instrumento, gold y grafos
   (`sellos_cierre_unidad.txt:1-20`), no las trazas; sin git no pude
   confirmar que estén commiteadas sin cambios.

---

Grep de convenciones (nombres propios de personas y referencias a origen
conversacional) sobre este archivo: pegado en el reporte de cierre de la
unidad.
