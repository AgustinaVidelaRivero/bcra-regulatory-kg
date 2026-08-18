# Agente v2 — tools v2 sobre Neo4j (U-A1.2, plan de tesis carril A / bloque A1)

Módulo APARTE del harness congelado: define SUS tools (`tools_v2.py`), SU spec
(`specs_tools_v2.json`, los textos que lee el modelo) y SU agente
(`agente_v2.py`, `GraphAgentV2`), importando lo reutilizable del cuarteto
hasheado (`data/experiment/evaluacion/`, sin editar) y del backend Neo4j de
U-A1.1 (`data/experiment/neo4j/`, sin reescribir). Costo de API: USD 0
(construcción + selftests determinísticos; el agente real NO corre acá — es
A1.4, y exigirá namespace de caché propio).

Contexto vinculante: `data/experiment/neo4j/README.md` (§ Estado post-A1.1,
en especial §D modos y §G qué cambia/qué no); `docs/decision_backend_grafo.md`
§1/§5; backlog BKL-0027 (asimetría direccional) y BKL-0022 (huérfano léxico
bajo la ventana de 40) — los dos defectos que estas tools resuelven POR DISEÑO;
mapa causal de U-A0 (techo alcanzabilidad+vista 14/7/6). Grafos: KG-Refinado
(`26fac8b4`) y KG-Reextraído (`8e2eadee`), servidos por el contenedor de A1.1.

**Regla dura cumplida (principio 7):** ningún material EV2 (preguntas,
criterios, pares sintéticos, trazas de `ev2_corrida`) se abrió ni se usó. La
verdad-terreno de `buscar_nodos_v2` es la designada fuera de EV2: CQ-031,
CQN2-015, BKL-0003, BKL-0022 (§E), y solo como registro informativo.

## A. Prerrequisito y comandos (desde la raíz del repo)

```bash
# contenedor de A1.1 levantado con los dos grafos (ver data/experiment/neo4j/README.md §A)
docker compose -f data/experiment/neo4j/docker-compose.yml ps        # healthy
.venv/bin/python data/experiment/neo4j/cargar_kg.py --solo-verificar # VERIFICACIÓN: OK
# selftest determinístico (exit 0 = todos los tests que rigen pasan)
.venv/bin/python data/experiment/agente_v2/selftest_tools_v2.py
# diff de specs v1 vs v2 (+ diff del prompt propuesto)
.venv/bin/python data/experiment/agente_v2/specs_diff.py
# latencia informativa v1 vs v2
.venv/bin/python data/experiment/agente_v2/latencia_tools_v2.py
# verificación textual del loop copiado + impresión del prompt propuesto
.venv/bin/python data/experiment/agente_v2/agente_v2.py
```

Doble corrida del selftest (2026-08-17): `selftest_tools_v2_resultados.json`
sha256 `b07a459a57641e896b26cd6ed72dc2756aa1d619203c4c103cfeea0c380afbc0` en
ambas corridas; stdout sha256 `ee49df20f0025dab843d2ce9ed0aeaef54858682cf5271d7c085ebe96d3b9fcb` en ambas → byte-idénticas
(copias `selftest_run{1,2}.{json,txt}` en el paquete de revisión).

## B. Módulos

| Archivo | Qué hace |
|---|---|
| `specs_tools_v2.json` | Las 3 specs que lee el modelo (`buscar_nodos`, `ver_nodo`, `ver_vecinos`), separadas del harness. Redactadas neutras (descriptivas; sin inducir estrategia). |
| `tools_v2.py` | `ToolsV2(driver, grafo)`: `buscar_nodos_v2` (= `Neo4jIndex(modo='fulltext').buscar_nodos`), `ver_vecinos_v2` (bidireccional, filtro por relación, paginación por offset), `ver_nodo_v2` (adaptador fino, sin cambio), `contexto_de` (punto de extensión, `NotImplementedError`), `despachar(name, args)`. Carga y valida `specs_tools_v2.json` (`TOOLS_V2`). |
| `agente_v2.py` | `GraphAgentV2(driver, grafo, client, cache_conversation, prompt='harness')`: subclase de `GraphAgent`; `_run_tool` → `ToolsV2`; `ask` COPIADO del harness con exactamente dos sustituciones (`system=`, `tools=`), verificable con `verificar_ask_copiado()`. `SYSTEM_PROMPT_V2_PROPUESTO` (inerte). |
| `selftest_tools_v2.py` | Tests de respuesta conocida (§E), valores esperados DERIVADOS del kg.json en el propio test. Salida `selftest_tools_v2_resultados.json`. |
| `specs_diff.py` | Genera `specs_diff_v1_v2.txt`: diff `harness.TOOLS` vs `specs_tools_v2.json` por tool + diff del prompt propuesto. |
| `latencia_tools_v2.py` | Latencia informativa v1 (in-memory / Neo4j paridad) vs v2 sobre los casos del selftest → `latencia_tools_v2_resultados.json`. |

## C. Decisiones de diseño y su porqué

1. **Nombres de API iguales a v1** (`buscar_nodos` / `ver_nodo` / `ver_vecinos`;
   los métodos Python llevan `_v2`). El prompt del harness nombra las tools; con
   los mismos nombres el prompt sigue apuntando a tools existentes sin edición,
   y las herramientas de análisis de trazas que cuentan llamadas por nombre
   siguen aplicando. La distinción v1/v2 queda en `GraphAgentV2.backend`
   (`tools_version: "v2"`) y en los argumentos nuevos (`relacion`, `pagina`,
   `por_pagina`). Alternativa descartada: sufijar `_v2` en la API — obligaría a
   editar el prompt para nombrarlas (confunde la variable tools con la
   variable prompt en A1.4).
2. **`ver_vecinos_v2` sin parámetro `direccion`** (bidireccional SIEMPRE, no
   "por default"). v1 ya tenía default `ambas` y BKL-0027 ocurrió igual porque
   el agente eligió `salientes`, recibió 0 y nunca pidió los 168 entrantes que
   el propio output declaraba. Quitar la elección resuelve el defecto por
   diseño; un default no lo haría. Ambas listas viajan separadas y rotuladas
   en la misma respuesta, cada una con su total, páginas y conteo por relación.
   Un argumento `direccion` que llegue (hábito v1) se ignora (probado en §H).
3. **Paginación por OFFSET** (`pagina` 1-based, `por_pagina` por dirección) sobre
   el orden estable `r.orden` (= posición en `kg.edges`, el mismo orden que el
   in-memory) — no cursor. Con un orden total fijo, sin escrituras concurrentes
   y con la db reconstruible desde el kg.json sellado, el offset es stateless,
   reproducible y auditable a mano; un cursor opaco no aporta nada. Ambas
   direcciones comparten el número de página (una dirección con menos páginas
   devuelve lista vacía y `pagina_siguiente: null` en las páginas siguientes —
   barato y explícito). Total declarado por dirección (`*_total`, `*_paginas`,
   `*_pagina_siguiente`).
4. **`por_pagina` default 40 = máximo 40**, justificado contra la ventana actual
   (40 por dirección): (i) mismo techo de payload por llamada que v1 (`ambas`
   ya devolvía hasta 40+40 filas; chars por ítem de arista serializado como lo
   entrega el harness, sobre TODAS las aristas: mediana 297 / p95 357 / máx 531
   en KG-Refinado y 244 / 305 / 438 en KG-Reextraído — 40 ítems ≈ 11.880 /
   9.760 chars por dirección; `selftest_tools_v2_resultados.json`
   `C_paginacion.chars_por_item_arista`) — la
   variable de A1.4 es el alcance (bidireccionalidad + paginación + filtro),
   no el tamaño de cada respuesta; (ii) la ventana solo actúa en la cola:
   11/4.469 y 12/6.178 nodos superan 40 en alguna dirección (selftest §C,
   `nodos_sobre_40`), así que 40 resuelve en una página el 99,7–99,8 % de los
   nodos y la paginación queda como mecanismo de cola; (iii) el huérfano de
   BKL-0022 está en la posición 7 de 145: con 40 sigue en la página 1 y con
   cualquier ventana menor cae en la página ⌈7/w⌉ (§E.B). No se permite superar
   el techo de v1 por llamada (`por_pagina` > 40 se recorta a 40).
5. **Filtro por relación exacto** (`relacion`), aplicado a ambas listas; los
   totales filtrados van en `*_total`, los sin filtro en `n_*_total` (claves de
   v1) y en `*_por_relacion` (conteo por tipo, sin filtro — el modelo ve qué
   hay aunque filtre). Relación inexistente → listas vacías, totales 0,
   conteos intactos.
6. **Layout plano** (listas `salientes` / `entrantes` en el primer nivel del
   dict, no anidadas): `GraphAgent._collect_provs` (harness, heredado sin
   editar) recorre solo `result.values()` que son listas de dicts con
   `provenances`; un layout anidado dejaría las provenances de `ver_vecinos_v2`
   fuera de `seen_provenances` y toda cita saldría "no vista". Verificado (§G).
   Los ítems tienen las mismas claves y contenido que v1 (`relation`,
   `vecino_id`, `vecino_label`, `provenances`), en el mismo orden.
7. **`buscar_nodos_v2` = modo `fulltext` de A1.1 sin re-implementar** (import):
   misma firma de salida que la tool actual (claves, clamp de `limite` 1..50,
   retorno para consulta sin tokens); cambios de spec DECLARADOS solo
   semánticos: `total_con_match` = hits del índice (≥1 término tras
   stemming/stopwords en label/descripcion/description/id_texto);
   `tokens_matcheados` (fórmula del harness sobre label+id) puede valer 0 en
   hits que entraron solo por descripción. El score de Lucene no se expone.
8. **`ver_nodo_v2` sin cambio** (adaptador fino sobre `Neo4jIndex.ver_nodo`,
   byte-idéntico al harness — verificado en A1.1 y re-verificado en §F).
9. **`ask` copiado con dos sustituciones y verificación textual.** `GraphAgent.ask`
   lee `TOOLS` y `SYSTEM_PROMPT` como globales del módulo harness; no hay
   inyección posible sin editar el cuarteto o copiar el loop. La copia se
   verifica en el selftest contra `inspect.getsource(GraphAgent.ask)` (116
   líneas; única diferencia: `system=self.system_prompt`, `tools=self.tools`).
   MODEL, TEMPERATURE, MAX_TOKENS, MAX_TOOL_CALLS, mensajes, precios,
   `_collect_provs`, `_cita_fiel`, `QuestionTrace`: por import.
10. **Prompt del sistema: harness VERBATIM por default.** Su lista de tools
    describe la semántica v1 en dos frases ("búsqueda léxica de nodos por
    label/id"; "ver_vecinos(id, direccion)… entrantes/salientes"). El ajuste
    mínimo (dos frases, ver §D) se entrega como `SYSTEM_PROMPT_V2_PROPUESTO`,
    activable solo con `prompt='propuesto'`, y queda **pendiente de laudo** —
    esta unidad no lo da por bueno.
11. **`contexto_de` NO se implementa**: firma `contexto_de(id, saltos<=2,
    presupuesto_tokens)` y semántica del presupuesto (BFS bidireccional
    determinístico por salto y `r.orden`; costo por ítem con estimador fijo
    declarado, p. ej. ⌈chars/4⌉, sin tokenizer remoto; corte al primer ítem
    que no entra; salida que declara presupuesto, tokens estimados, estimador,
    incluidos/omitidos/truncado, provenances en listas de primer nivel)
    quedan en el docstring de `ToolsV2.contexto_de` para que A1.4 decida.

## D. Specs v1 vs v2 (texto que lee el modelo) y diff del prompt

Diff completo generado: `specs_diff_v1_v2.txt` (`specs_diff.py`). Resumen:
`ver_nodo` byte-idéntico; `buscar_nodos` cambia la descripción (texto
completo/BM25 sobre label, id y descripción; semántica de `tokens_matcheados` y
`total_con_match`; "máx. 50" explícito en `limite`); `ver_vecinos` reemplaza
`direccion` (enum) por `relacion` (string), `pagina` (integer) y `por_pagina`
(integer) y describe la respuesta bidireccional paginada.

Prompt (INERTE, pendiente de laudo) — únicas dos líneas que cambiarían:

```
- - buscar_nodos(consulta, limite): búsqueda léxica de nodos por label/id. Empezá siempre por acá para encontrar puntos de entrada.
+ - buscar_nodos(consulta, limite): búsqueda de texto completo (BM25) de nodos por label, id y descripción. Empezá siempre por acá para encontrar puntos de entrada.
- - ver_vecinos(id, direccion): devuelve los edges (relaciones) entrantes/salientes de un nodo, con el vecino y las provenances del edge.
+ - ver_vecinos(id, relacion, pagina): devuelve los edges (relaciones) entrantes y salientes de un nodo en una sola llamada, paginados y filtrables por relación, con el vecino y las provenances del edge.
```

## E. Selftest — tests de respuesta conocida (`selftest_tools_v2.py`, exit 0)

Valores esperados derivados del kg.json (vista runtime del loader) dentro del
test. **231/231 tests que rigen pasan; 12 informativos** (`resumen` del JSON).

| grafo | sección | rigen (pasan/total) | informativos |
|---|---|---|---|
| KG_Refinado | 0.integridad | 3/3 | 0 |
| KG_Refinado | A.BKL-0027 | 10/10 | 0 |
| KG_Refinado | B.BKL-0022 | 8/8 | 0 |
| KG_Refinado | C.paginacion | 30/30 | 0 |
| KG_Refinado | D.filtro | 14/14 | 0 |
| KG_Refinado | E.busqueda | 32/32 | 4 |
| KG_Refinado | F.ver_nodo | 6/6 | 0 |
| KG_Refinado | G.provenances | 6/6 | 0 |
| KG_Refinado | H.agente | 13/13 | 1 |
| KG_Reextraido | 0.integridad | 3/3 | 0 |
| KG_Reextraido | A.BKL-0027 | 10/10 | 0 |
| KG_Reextraido | B.BKL-0022 | 0/0 | 1 (N/A: el nodo no existe en este grafo) |
| KG_Reextraido | C.paginacion | 30/30 | 0 |
| KG_Reextraido | D.filtro | 12/12 | 0 |
| KG_Reextraido | E.busqueda | 31/31 | 5 |
| KG_Reextraido | F.ver_nodo | 4/4 | 0 |
| KG_Reextraido | G.provenances | 6/6 | 0 |
| KG_Reextraido | H.agente | 13/13 | 1 |

**0. Integridad:** sha256 de ambos kg.json == sellado; `KG_Meta.kg_sha256` y
conteos en Neo4j == sellados (4.469/8.073; 6.178/11.415).

**A. BKL-0027 (asimetría direccional).** Derivado de `kg.json`:
- KG-Refinado: `Sujeto_rol_sujeto_obligado_proteccion` — 0 salientes, **168
  entrantes** (`aplica_a` 161, `miembro_de` **7**). v1 `ver_vecinos(rol,
  'salientes')` reproduce la llamada de RT-C6-3: `salientes` = [] y sin clave
  `entrantes` (solo `n_entrantes_total: 168`). v2 en UNA llamada:
  `salientes_total 0`, `entrantes_total 168`, ambas listas presentes,
  `entrantes_por_relacion {aplica_a: 161, miembro_de: 7}`; unión de las 5
  páginas de 40 == los 168 ítems derivados byte a byte y en orden; filtro
  `relacion='miembro_de'` → exactamente los 7 (byte a byte). Coincide con lo
  que cita el backlog (7 miembro_de / 168 entrantes).
- KG-Reextraído: mismo id — **2 salientes** (`ejecuta` 2), **242 entrantes**;
  `miembro_de` no existe en su esquema → filtro devuelve 0 (derivado 0); unión
  de 7 páginas == 242 ítems exactos.

**B. BKL-0022 (huérfano léxico bajo la ventana de 40)** — solo KG-Refinado (el
nodo no existe en KG-Reextraído): `Sujeto_propuesto_entidades_financieras_del_grupo_2`
aparece exactamente una vez entre los **145** entrantes de
`Sujeto_entidad_financiera`, en la **posición 7** (relación `subclase_de`;
entre los 7 `subclase_de` es también el 7.º). v1: visible en la ventana de 40
en la posición 7 (== derivada). v2 por paginación, todo derivado:

| por_pagina | página | posición en la página | páginas totales |
|---|---|---|---|
| 40 (default) | 1 | 7 | 4 |
| 10 | 1 | 7 | 15 |
| 5 | 2 | 2 | 29 |
| 1 | 7 | 1 | 145 |

Con filtro `relacion='subclase_de'`: posición 7 de 7. Desde el propio
huérfano, `salientes` == derivado (1 arista al hub). **Posición actual
registrada para la nota del backlog: 7** (la nota del 2026-08-02 decía 6 sobre
el grafo post-C4; A1.1 midió 7 sobre `26fac8b4`; acá vuelve a dar 7 en ambos
backends — la fragilidad orden-dependiente que la nota describe, no una
discrepancia).

**C. Paginación** — hub máximo entrante (`TextoOrdenado_to_exterior_cambios_actual_pdf`:
196/1.316 en KG-Refinado; 13/2.167 en KG-Reextraído), hub máximo saliente
(`TextoOrdenado_to_capitales_minimos_actual_pdf` 253/980; `Sujeto_rol_entidad_autorizada_exterior`
27/948), más el rol de A y el hub de B: para ventanas 40 y 7, la unión de
páginas == lista exacta de vecinos (mismo orden, multiconjunto idéntico —
sin pérdida ni duplicado) y los metadatos de la página 1 (totales, páginas,
siguiente) == derivados; página fuera de rango → listas vacías, siguiente
null, totales intactos; parámetros inválidos (`pagina` 0/−3/'x'/None,
`por_pagina` 0/999/'abc'/None, `relacion` '') → defaults/clamps; id
inexistente → mismo error que v1. Nodos con >40 en alguna dirección: 11 (KG-Refinado) / 12 (KG-Reextraído).

**D. Filtro por relación** — para el hub máximo entrante, el rol de A y el hub
de B: por cada relación presente, filtrado == subconjunto exacto del
sin-filtro (byte a byte, en ambas direcciones) y == derivado; suma de
`por_relacion` == grado; relación inexistente → 0 con conteos intactos.

**E. `buscar_nodos_v2` (INFORMATIVO, sin conclusiones — la medición es A1.4).**
Los ids de run_3 citados en los docs para CQ-031 y CQN2-015 **no existen** en
KG-Refinado ni en KG-Reextraído (el pipeline v2 re-hashea ids); el portador
equivalente se localizó por contenido (substring normalizado en
label+properties) — es lo derivado de los archivos, y difiere de los ids que
citan los docs (se reporta). "v1 rank" = rank global con réplica del scoring del
harness (la misma réplica de `verificaciones_vara_v3.md` §2c); "v2 top10" =
posición en el output de la tool con `limite=10`; "v2 rank" = rank global BM25
(réplica del `ORDER BY` de A1.1). Los totales v1 difieren de los citados en los
docs porque el grafo es otro (run_3 ≠ KG-Refinado).

**KG_Refinado / CQ-031** — portador `Restriccion_los_deudores_cuyas_financiaciones_se_encuentren_cubiertas_totalmente_con_garanti_7799cb` (label «Exclusión de clasificación de deudores»)

| consulta | total v1 | total v2 | v1 rank / v2 top10 / v2 rank |
|---|---|---|---|
| deudores no deben ser objeto clasificación | 617 | 516 | 16 / 2 / 2 |
| capacidad de repago evaluación deudores | 2949 | 252 | 23 / None / 35 |
| deudores exclusión clasificación estado nacional provincia municipio | 218 | 361 | 1 / 3 / 3 |
| garantías preferidas A financiaciones | 1367 | 381 | 780 / 2 / 2 |
| punto 4.5 deudores no deben clasificación estado nacional | 650 | 796 | 28 / 6 / 6 |
| punto 4.4 garantías preferidas A estado nacional provincia | 1373 | 605 | None / None / 29 |
| estado nacional provincia municipio banco central deudores | 89 | 270 | 28 / None / 37 |
| cesión sin responsabilidad cedente deudores | 162 | 238 | 36 / None / 31 |
| garantías preferidas A definición estado nacional provincia | 1331 | 213 | None / None / 15 |
| garantías preferidas A créditos estado nacional provincia municipio | 1348 | 463 | None / None / 14 |
| ¿Qué deudores no deben ser objeto de clasificación y respecto de qué deudores no corresponde evaluar la capacidad de repago? | 3246 | 703 | 215 / 6 / 6 |

→ en top-10: v1 1/11 · v2 5/11.

**KG_Refinado / CQN2-015** — portador `Restriccion_limite_minimo_de_ponderador_para_deudores_no_calificados_81f003` (label «Límite mínimo de ponderador para deudores no calificados»)

| consulta | total v1 | total v2 | v1 rank / v2 top10 / v2 rank |
|---|---|---|---|
| capital mínimo riesgo crédito ponderador deudor no calificado | 966 | 1120 | 25 / 1 / 1 |
| piso ponderador riesgo exposición deudor | 345 | 696 | 313 / 5 / 5 |
| deudor no calificado ponderador piso | 500 | 273 | 12 / 1 / 1 |
| no calificado ponderador | 438 | 101 | 9 / 1 / 1 |
| ponderador riesgo exposición deudor sin calificación | 432 | 724 | 386 / 8 / 8 |
| exposición deudor no calificado 100% | 521 | 413 | 456 / 1 / 1 |
| ponderador riesgo 100 deudor calificado | 307 | 579 | 277 / 1 / 1 |
| deudor sin calificación 100 | 176 | 242 | None / None / 32 |

→ en top-10: v1 1/8 · v2 7/8.

**KG_Refinado / BKL-0003** — portador `Excepcion_otros_proveedores_no_financieros_de_credito_alcanzados_por_las_normas_sobre_prov_5f95b9` (por id)

| consulta | total v1 | total v2 | v1 rank / v2 top10 / v2 rank |
|---|---|---|---|
| asociación mutual | 1 | 3 | 1 / 1 / 1 |
| asociacion mutual | 1 | 3 | 1 / 1 / 1 |
| asociaciones mutuales | 2 | 3 | 1 / 1 / 1 |
| mutual cooperativa crédito | 115 | 286 | 1 / 1 / 1 |
| excepto que se trate de asociaciones mutuales | 3080 | 111 | 5 / 1 / 1 |
| otros proveedores no financieros de crédito | 3034 | 830 | 1 / 2 / 2 |

→ en top-10: v1 6/6 · v2 6/6 (el label de este nodo ya fue enriquecido en capa KG por C6; ver README de neo4j, E3).

**KG_Refinado / BKL-0022** — portador `Sujeto_propuesto_entidades_financieras_del_grupo_2` (por id); consultas = tokens del label (derivados) + label completo + "grupo 2"

| consulta | total v1 | total v2 | v1 rank / v2 top10 / v2 rank |
|---|---|---|---|
| entidades | 170 | 966 | 20 / None / 76 |
| financieras | 84 | 576 | 13 / None / 57 |
| del | 502 | 0 | 60 / None / None |
| grupo | 30 | 49 | 12 / None / 19 |
| 2 | 69 | 100 | 13 / None / 17 |
| Entidades financieras del grupo 2 | 710 | 1247 | 3 / 3 / 3 |
| grupo 2 | 90 | 138 | 5 / 7 / 7 |

→ en top-10: v1 2/7 · v2 2/7 (sigue siendo huérfano léxico por token suelto en ambos; la vía de A1.2 para él es la navegación paginada de §B).

**KG_Reextraido / CQ-031** — portador `Restriccion_los_deudores_cuyas_financiaciones_se_encuentren_cubiertas_totalmente_con_garanti_7799cb` (label «Deudores con garantías preferidas A no clasificables»)

| consulta | total v1 | total v2 | v1 rank / v2 top10 / v2 rank |
|---|---|---|---|
| deudores no deben ser objeto clasificación | 1107 | 681 | 56 / 3 / 3 |
| capacidad de repago evaluación deudores | 4386 | 322 | 2878 / None / 44 |
| deudores exclusión clasificación estado nacional provincia municipio | 321 | 503 | 204 / None / 24 |
| garantías preferidas A financiaciones | 1646 | 577 | 1 / 3 / 3 |
| punto 4.5 deudores no deben clasificación estado nacional | 1276 | 1266 | 130 / None / 29 |
| punto 4.4 garantías preferidas A estado nacional provincia | 1756 | 1084 | 7 / 6 / 6 |
| estado nacional provincia municipio banco central deudores | 121 | 364 | 73 / None / 56 |
| cesión sin responsabilidad cedente deudores | 260 | 281 | 135 / None / 35 |
| garantías preferidas A definición estado nacional provincia | 1604 | 353 | 1 / 3 / 3 |
| garantías preferidas A créditos estado nacional provincia municipio | 1628 | 701 | 3 / 5 / 5 |
| ¿Qué deudores no deben ser objeto de clasificación y respecto de qué deudores no corresponde evaluar la capacidad de repago? | 5184 | 979 | 2332 / 6 / 6 |

→ en top-10: v1 4/11 · v2 6/11.

**KG_Reextraido / CQN2-015** — portador `Restriccion_ninguna_exposicion_con_deudores_no_calificados_podra_recibir_un_ponderador_de_ri_2e92f4` (label «Prohibición ponderador menor deudores no calificados»)

| consulta | total v1 | total v2 | v1 rank / v2 top10 / v2 rank |
|---|---|---|---|
| capital mínimo riesgo crédito ponderador deudor no calificado | 1657 | 1591 | 247 / 2 / 2 |
| piso ponderador riesgo exposición deudor | 620 | 1032 | 84 / 1 / 1 |
| deudor no calificado ponderador piso | 965 | 414 | 27 / 1 / 1 |
| no calificado ponderador | 890 | 219 | 24 / 1 / 1 |
| ponderador riesgo exposición deudor sin calificación | 797 | 1068 | 96 / 9 / 9 |
| exposición deudor no calificado 100% | 992 | 617 | 30 / 1 / 1 |
| ponderador riesgo 100 deudor calificado | 557 | 850 | 390 / 1 / 1 |
| deudor sin calificación 100 | 331 | 321 | None / None / 52 |

→ en top-10: v1 0/8 · v2 7/8.

**KG_Reextraido / BKL-0003** — dos portadores por contenido: `Excepcion_no_aplican_estas_normas_a_las_asociaciones_mutuales_o_cooperativas_a0051e` («Excepción asociaciones mutuales y cooperativas») y `Obligacion_otros_proveedores_no_financieros_de_credito_alcanzados_por_las_normas_sobre_prov_5f95b9` («Sujeción a normas protección usuarios — PNFC»)

| consulta | total v1 | total v2 | Excepcion…a0051e: v1 rank / v2 top10 / v2 rank | Obligacion…5f95b9: v1 rank / v2 top10 / v2 rank |
|---|---|---|---|---|
| asociación mutual | 1 | 4 | None / 1 / 1 | None / 2 / 2 |
| asociacion mutual | 1 | 4 | None / 1 / 1 | None / 2 / 2 |
| asociaciones mutuales | 1 | 4 | 1 / 1 / 1 | None / 2 / 2 |
| mutual cooperativa crédito | 204 | 416 | None / 1 / 1 | 58 / 3 / 3 |
| excepto que se trate de asociaciones mutuales | 4800 | 157 | 636 / 1 / 1 | 2619 / 2 / 2 |
| otros proveedores no financieros de crédito | 4655 | 1203 | 2397 / None / None | 1 / 3 / 3 |

→ en top-10: Excepcion v1 1/6 · v2 5/6; Obligacion v1 1/6 · v2 6/6.

**KG_Reextraido / BKL-0022**: N/A (sin portador).

Test que RIGE en §E: la posición en el top-10 de la tool coincide con el rank
global BM25 replicado cuando este es ≤10 (consistencia interna) — 32/32 y 31/31.

**F.** `ver_nodo_v2` byte-idéntico a `GraphIndex.ver_nodo` (5+1 ids / 3+1 ids,
incl. inexistente). **G.** `GraphAgent._collect_provs` recoge exactamente las
provenances de ambas listas de `ver_vecinos_v2` y las de `ver_nodo_v2` (3
nodos por grafo). **H.** `GraphAgentV2.ask` == `GraphAgent.ask` salvo las 2
sustituciones (116 líneas); prompt default == `SYSTEM_PROMPT` verbatim; tools
del request == `specs_tools_v2.json`; `_run_tool` == `ToolsV2` byte a byte en
7 llamadas (incl. `direccion` v1 ignorado y tool desconocida); nombres v2 ==
v1 y parámetros declarados; `contexto_de` → `NotImplementedError`.

## F. Latencia informativa — `latencia_tools_v2.py` (solo registro; 20 reps, 2 warmup, MacBook local, Docker)

Mediana de medianas por caso (ms) / p95 máximo / payload mediana (chars):

| grafo | tool | backend | casos | mediana | p95 | payload |
|---|---|---|---|---|---|---|
| KG_Refinado | buscar_nodos | v1 in-memory | 32 | 0.651 | 2.649 | 3471 |
| KG_Refinado | buscar_nodos | v1 neo4j paridad | 32 | 17.216 | 140.656 | 3471 |
| KG_Refinado | buscar_nodos | v2 fulltext | 32 | 1.321 | 19.468 | 3476.5 |
| KG_Refinado | ver_nodo | v1 in-memory | 5 | 0.000 | 0.000 | 359 |
| KG_Refinado | ver_nodo | v1 neo4j | 5 | 0.502 | 4.730 | 359 |
| KG_Refinado | ver_nodo | v2 | 5 | 0.544 | 0.970 | 359 |
| KG_Refinado | ver_vecinos | v1 in-memory 'ambas' | 4 | 0.130 | 0.336 | 18602.5 |
| KG_Refinado | ver_vecinos | v1 neo4j 'ambas' | 4 | 16.341 | 72.324 | 18602.5 |
| KG_Refinado | ver_vecinos | v2 bidireccional p.1 | 4 | 4.790 | 14.369 | 18887.5 |
| KG_Refinado | ver_vecinos | v2 con filtro | 2 | 2.673 | 3.574 | 2307.5 |
| KG_Reextraido | buscar_nodos | v1 in-memory | 25 | 1.109 | 18.399 | 3656 |
| KG_Reextraido | buscar_nodos | v1 neo4j paridad | 25 | 39.596 | 234.287 | 3656 |
| KG_Reextraido | buscar_nodos | v2 fulltext | 25 | 1.472 | 6.909 | 3508 |
| KG_Reextraido | ver_nodo | v1 in-memory | 3 | 0.000 | 0.000 | 271 |
| KG_Reextraido | ver_nodo | v1 neo4j | 3 | 0.516 | 1.955 | 271 |
| KG_Reextraido | ver_nodo | v2 | 3 | 0.509 | 1.606 | 271 |
| KG_Reextraido | ver_vecinos | v1 in-memory 'ambas' | 4 | 0.131 | 0.430 | 15668 |
| KG_Reextraido | ver_vecinos | v1 neo4j 'ambas' | 4 | 14.802 | 50.916 | 15668 |
| KG_Reextraido | ver_vecinos | v2 bidireccional p.1 | 4 | 4.059 | 7.084 | 15925 |
| KG_Reextraido | ver_vecinos | v2 con filtro | 2 | 2.525 | 4.144 | 486 |

Registro del mecanismo (no conclusión): los casos de `ver_vecinos` son hubs
(hasta 2.167 aristas) — v1 sobre Neo4j trae todas las filas y recorta en
Python; v2 pagina en Cypher (`SKIP/LIMIT`) y trae solo la ventana. Los tiempos
varían run a run (~±20 %); el orden de magnitud es el dato. Los payloads de
`ver_vecinos` v2 son ~1–2 % mayores que v1 'ambas' por los metadatos de
paginación y `*_por_relacion`.

## G. Tabla "tools v1 vs v2" (para la Metodología)

| Tool | Firma v1 (harness) | Firma v2 (`tools_v2.py`) | Semántica v1 | Semántica v2 | Defaults v1 → v2 | Defecto que resuelve | Qué NO cambia |
|---|---|---|---|---|---|---|---|
| `buscar_nodos` | `(consulta, limite=10)` | `buscar_nodos_v2(consulta, limite=10)` | intersección de tokens con label+id; orden (−score, len(label), id) | BM25 Lucene (analyzer `spanish`: stemming + stopwords) sobre label + descripcion + description + id_texto; orden score desc, desempate (len(label), id) | `limite` 10, clamp 1..50 → **igual** | alcanzabilidad léxica por label/id (CQ-031, CQN2-015, BKL-0003; huérfanos como BKL-0022 solo si el vocabulario está en la descripción) | claves del payload (`consulta`, `total_con_match`, `resultados[{id,type,label,tokens_matcheados,resumen_propiedades}]`), clamp, retorno sin tokens, `_short_props`, nombre de API; el score no se expone |
| `ver_nodo` | `(id)` | `ver_nodo_v2(id)` | dict por id | **idéntica** (adaptador fino sobre `Neo4jIndex.ver_nodo`) | — | — | todo (byte-idéntico, incl. errores) |
| `ver_vecinos` | `(id, direccion='ambas', limite=40)` — `limite` no expuesto al modelo | `ver_vecinos_v2(id, relacion=None, pagina=1, por_pagina=40)` | una o dos direcciones según `direccion`; ventana fija 40 por dirección; `*_truncado` como única señal de resto | SIEMPRE ambas direcciones, separadas y rotuladas; filtro por relación exacto; paginación por offset sobre `r.orden` con total/páginas/siguiente por dirección; conteo por relación | `direccion='ambas'`, ventana 40 → sin `direccion`; `pagina=1`, `por_pagina=40` (máx. 40) | BKL-0027 (dirección equivocada → 0) y BKL-0022 (visibilidad dependiente de la posición bajo la ventana de 40) | ítems (`relation`, `vecino_id`, `vecino_label`, `provenances`), su orden (`kg.edges` = `r.orden`), claves `n_salientes_total`/`n_entrantes_total`, error de id inexistente, techo de 40 filas por dirección y por llamada, nombre de API |
| `contexto_de` | — | `contexto_de(id, saltos<=2, presupuesto_tokens)` → `NotImplementedError` | — | punto de extensión declarado (docstring) | — | (A1.4 decide) | — |

Comunes a las tres: MODEL, prompt del sistema (default verbatim), MAX_TOOL_CALLS,
truncado de trazas, `_collect_provs`, `_cita_fiel`, juez, verificador, capa
determinística: sin cambio. Nombres de API sin cambio.

## H. Nota al backlog (BKL-0022) — línea JSON exacta, la aplica la autora (esta unidad NO toca el backlog)

```json
{"evento": "nota", "id": "BKL-0022", "ts": "2026-08-17", "nota": "medición U-A1.2 (tools v2 sobre Neo4j) sobre el sha vigente 26fac8b4: el huérfano Sujeto_propuesto_entidades_financieras_del_grupo_2 está en la posición 7 de los 145 entrantes de Sujeto_entidad_financiera (relación subclase_de; 7.º de 7 subclase_de), derivado del kg.json y coincidente en los DOS backends (GraphIndex in-memory y Neo4j, byte a byte) — igual que en U-A1.1 (9e131bf); la nota post-C4 (2026-08-02) registraba posición 6 sobre el grafo previo a C5-C7. Fragilidad orden-dependiente CONFIRMADA en ambos backends: la visibilidad bajo la ventana de 40 de ver_vecinos v1 depende del orden de kg.edges. Con ver_vecinos_v2 (paginación por offset sobre ese mismo orden) el nodo es alcanzable en alguna página cualquiera sea su posición (medido: pagina 1 pos 7 con ventana 40; 1/7 con 10; 2/2 con 5; 7/1 con 1) y en la posición 7 de 7 con filtro relacion=subclase_de. Sigue siendo huérfano léxico por token suelto también en BM25 (ningún token del label lo trae al top-10; el label completo pos 3, 'grupo 2' pos 7). BKL-0022 sigue VIGENTE: la verificación propia queda a cargo de A1.4 con el agente real", "referencia": "data/experiment/agente_v2/selftest_tools_v2_resultados.json (secciones B.BKL-0022 y E.busqueda) + data/experiment/neo4j/test_equivalencia_resultados_A11.json"}
```

## I. Inventario del directorio

Commiteable: `README.md`, `specs_tools_v2.json`, `tools_v2.py`, `agente_v2.py`,
`selftest_tools_v2.py`, `selftest_tools_v2_resultados.json` (determinístico),
`specs_diff.py`, `specs_diff_v1_v2.txt`, `latencia_tools_v2.py`,
`latencia_tools_v2_resultados.json` (tiempos no determinísticos; registro),
`.gitignore` (local). Gitignorado: `__pycache__/`.

## J. Limitaciones y pendientes

- El agente v2 NO corrió con API: `GraphAgentV2` está definido y su despacho
  probado con cliente dummy. Correrlo (A1.4) exige namespace de caché propio.
- El prompt del sistema default sigue describiendo la semántica v1 en dos
  frases; el ajuste mínimo está propuesto (§D) y pendiente de laudo. Mientras
  tanto, si el modelo pasa `direccion` por hábito, se ignora (bidireccional).
- `por_pagina` comparte el número de página entre direcciones: cuando una
  dirección se agota antes, sus páginas posteriores llegan vacías (explícito,
  barato).
- `buscar_nodos_v2` hereda de A1.1 la semántica de `total_con_match` (hits del
  índice) y `tokens_matcheados` (puede ser 0): son cambios semánticos
  declarados en la spec, sin cambio de claves.
- Los portadores de CQ-031 / CQN2-015 en los grafos vigentes se localizaron por
  contenido (los ids de run_3 no existen); toda comparación con los ranks
  citados en los docs es entre grafos distintos — por eso §E es solo registro.
