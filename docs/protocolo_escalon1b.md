# Protocolo pre-registrado — Escalón 1b: v3 (re-ensamblado) vs v2 sobre EV1

> Este protocolo se commitea ANTES de la primera llamada del escalón 1b. La corrida
> no comienza hasta que esté sellado. La corrida y su lectura son unidades aparte.

## 1. Objeto y diseño

Mido `data/experiment/grafo_v2/reensamblado_v3/kg.json` (v3) contra
`data/experiment/grafo_v2/kg.json` (v2) sobre el set sellado EV1 (36 preguntas,
`EV1_runtime.json` derivado de la key adjudicada, orden barajado con semilla
20260726 — informe `data/experiment/grafo_v2/informes/corridas_escalon1_2026-07-26.md`,
"Cableado"). `run_3` entra como **referencia descriptiva**, no como brazo en
disputa (su caveat va en §6). Variable única: v2 y v3 consumen el MISMO caché de
extracción (biyección 508↔508, verificada en la auditoría de custodia); cambia solo
la lógica de ensamblado. Nada más cambia.

Réplica exacta del setup del escalón 1 (cada parámetro con su fuente):

- **Cuarteto congelado, verificado por hash antes de correr** (sha256[:12] según el
  informe del escalón 1, PASO 0(c)): `loader.py 5aba8b7a0aa4` · `harness.py
  fd267e833866` · `judge.py 7169145aaeb3` · `llm_cache.py fc86b0e48df4` ·
  `runners/run_posthoc.py 0918f63c30bd`.
- **Agente:** `claude-haiku-4-5-20251001`, fijo (`harness.py:47`), `TEMPERATURE = 0`
  (`harness.py:48`), `MAX_TOKENS = 2048` (`harness.py:49`), mismas 3 tools con el
  índice léxico actual y límite de 15 tool calls por pregunta (harness congelado;
  el informe del escalón 1 reporta las réplicas que tocaron ese límite).
- **Juez:** `claude-sonnet-4-6` (`judge.py:87`), `JUDGE_TEMPERATURE = 0`
  (`judge.py:88`), v2.1.1 de dos pasos, **ciego a qué brazo evalúa** (ceguera
  estructural: el payload no contiene la identidad del grafo — `judge.py:274-297`,
  citado por el informe del escalón 1, PASO 4). Mapping A/B por pregunta con semilla
  registrada, como registro auditable (mismo procedimiento).
- **Régimen:** N=3 réplicas frescas por pregunta (una db de caché por réplica, el
  mecanismo que evita que la caché colapse las réplicas — informe, PASO 2),
  veredicto por **mayoría ≥2 de 3**; `failed_trace` cuenta como no-correcta
  (informe, PASO 4). Fallas técnicas se reparan, se registran y la pregunta se
  re-corre completa; fallas del sistema bajo evaluación no se reintentan
  (protocolo del escalón 1, §1 y §3).
- **Anti-fuga:** escaneo de las respuestas por identificadores de esquema, mismo
  procedimiento y misma salvedad de secuencia que el escalón 1 (registra, no
  filtra; PASO 3).
- **Carga de v3 en el loader:** patrón "módulo aparte que importa al loader", igual
  que el cableado de v2 en el escalón 1 (registro EN MEMORIA, `code_version` no
  rota, adaptador nulo — informe, "Cableado"). El loader lee la `provenance`
  primaria; el campo `provenances` de v3 es invisible para el harness (paridad de
  interfaz con v2, documentada en `assemble_v3.py:38-42`).

Baseline heredado (post-adjudicación humana,
`data/experiment/evaluacion_escalon1/resultados_FINALES_2026-07-26.json`):
**v2 = 27/36 (75.0%)** · run_3 = 31/36 (86.1%).

## 2. Laudo de reuso de EV1 (decisión ya tomada; acá se documenta)

1. **El reuso es una excepción argumentada a la regla de material quemado.** La
   regla del proyecto es que un set medido queda quemado. Acá la modificación del
   objeto medido fue **mecánica e independiente del contenido de EV1**: el
   re-ensamblado v3 cambió la lógica de agregación (driver `chunks_all.json`, roles
   documentales, claves de dedup, acumulación de provenances) sin re-extraer nada y
   sin mirar pregunta alguna de EV1 — no hubo iteración del grafo contra el set.
   El delta v2→v3 es reproducible por script desde el caché congelado; no hay
   canal por el que el contenido de EV1 haya influido en qué cambió.
2. **Evidencia positiva de no-contaminación.** La auditoría de custodia (29-07)
   verificó que la pregunta que disparó el diagnóstico (tope mensual de compra de
   moneda extranjera, punto 3.9 de Exterior y Cambios) NO pertenece a EV1 ni a las
   9 fichas del escalón 1: es, carácter por carácter, la `pregunta_original` de
   CQN-001 (`data/experiment/evaluacion/queries/eval_set_cqn.json`), material de la
   familia de gates del verificador. Por eso mismo, **el caso del punto 3.9 queda
   EXCLUIDO de toda lectura del 1b como evidencia de mejora**: es la anécdota de
   descubrimiento del defecto de ensamblado, no un caso medido.
3. **Este es el ÚLTIMO uso de EV1.** Tras el 1b, EV1 queda quemado por completo
   para cualquier medición futura (ya habrá servido dos veces sobre el mismo
   linaje de grafos). El siguiente escalón requiere un EV2 nuevo por generación
   ciega (instancia separada con acceso solo a los PDFs, anti-solapamiento
   determinístico contra los sets quemados — el procedimiento ya usado para EV1,
   `data/experiment/evaluacion_escalon1/protocolo_escalon1.md` §2).

## 3. Predicciones (selladas aparte; acá solo la referencia y el resumen)

Las predicciones NO se re-derivan acá: rigen las del mapeo sellado
`data/experiment/evaluacion_escalon1/mapeo_delta_v2v3.md`, commit **`6c24009`**
(secciones C y D). Transcribo únicamente lo operativo:

- **Banda dura: v3 ∈ [19, 30] sobre 36.** Rama central: **28–29**, techo 30 si
  EV1-018 convierte.
- **8 candidatos a regresión por entierro**, nombrados: EV1-001, EV1-007, EV1-012,
  EV1-013, EV1-021, EV1-023, EV1-032, EV1-036. **EV1-032 es el único sin
  mitigación medida** (contraparte fuera de top-50 para sus queries diluidas, sin
  queries alternativas que la traigan, más un nodo consultado en v2 que v3
  elimina).

## 4. Presupuesto y caché

- **Solo se paga el brazo v3** (agente + veredictos de juez nuevos). Los brazos v2
  y run_3 sobre EV1 ya están pagados bajo el cv vigente (`aa15d9c9b5b7`), en las
  dbs por réplica del escalón 1
  (`evaluacion/posthoc_run/escalon1_r{1,2,3}.db`, réplicas frescas del 26-07).
- **Mecánica de caché obligatoria:** las dbs selladas del escalón 1 NO se abren en
  escritura. La corrida trabaja sobre **copias**: `escalon1_r{N}.db` →
  `escalon1b_r{N}.db` (copia byte a byte antes de correr). La réplica N del 1b usa
  `escalon1b_r{N}.db`: los requests de v2/run_3 son byte-idénticos a los del
  escalón 1 (mismo cuarteto por hash, mismos namespaces
  `agent|gfp=64294e016163a4fb|…` y `agent|gfp=98d3ee73a23c214b|…` con
  `cv=aa15d9c9b5b7|think=0`) → **hit de caché**; las llamadas de v3 (namespace
  nuevo `agent|gfp=224cc48fb0e05cc0|cv=aa15d9c9b5b7|think=0`) son miss y se pagan
  una vez, escribiéndose en la copia.
- **Evidencia obligatoria:** la corrida reporta el **hit-rate de caché por brazo y
  por réplica**. Esperado: v2 = 100%, run_3 = 100%, v3 = 0% en la primera pasada.
  **Un hit-rate < 100% en v2 o run_3 es un desvío que DETIENE la corrida** (indica
  request no byte-idéntico: cuarteto o parámetros cambiados) — se reporta antes de
  seguir gastando.
- **Proyección:** una corrida de 36 preguntas (agente Haiku + juez Sonnet) costó
  USD 1.79–1.82 en el escalón 1 (informe, PASO 2: seis corridas entre $1.7971 y
  $1.8233). El brazo v3 son 3 corridas ≈ **USD 5.5** proyectados; v2/run_3
  repuestos por caché ≈ $0.
- **Tope duro: USD 14 según tracker.** Si el acumulado lo alcanza, la corrida se
  corta donde esté y se reporta lo corrido y lo pendiente.

## 5. Congelamiento

Antes de la primera llamada, y como precondición bloqueante:

1. `git status --porcelain=v1 -uall` **vacío**.
2. **sha256 de ambos brazos contra los blobs commiteados** (obtenidos con
   `git cat-file blob HEAD:<path> | shasum -a 256`):
   - `data/experiment/grafo_v2/kg.json` →
     `2c7487bb11c8dafee702a27d6558f1dc643f481bb6656ec5e19e3b11f9ae49c1`
   - `data/experiment/grafo_v2/reensamblado_v3/kg.json` →
     `8cda499dfea0a55d91afe0791b60d0f14ab42105907aed561393471ab031ccc5`
3. Hashes del cuarteto + runner idénticos a los listados en §1.
4. **Ninguna edición de grafo, instrumento o backlog de nodos entre el sellado de
   este protocolo y la lectura del 1b.** En particular, las correcciones de
   contenido ya detectadas — los montos invertidos del punto 1.2 de capitales
   mínimos (RX-10) y la pérdida del criterio general 1.1 (precisión a RX-07/RX-05)
   — quedan explícitamente **DIFERIDAS a post-1b**: corregirlas ahora rompería la
   variable única (el 1b mide el re-ensamblado tal como quedó sellado, con sus
   defectos conocidos incluidos).

## 6. Lectura y válvula

- La lectura es **caso por caso contra las ramas del mapeo sellado (§C)**: cada
  delta v2→v3 (acierto nuevo, regresión, cambio de patrón 3-0/2-1) recibe una
  **ficha nueva** con el formato de las 9 existentes
  (`corridas/fichas_fallas_v2.json`: id, pregunta, familia, tos_fuente,
  ground_truth_secciones, veredictos por réplica, traza, veredicto causal).
- **Rige la válvula del mapeo (§D):** un acierto nuevo en una ficha clasificada
  `no_recuperable_por_v3`, una regresión en cualquiera de los 17 casos declarados
  estables, o un global fuera de [19, 30] **detienen la lectura** y la devuelven a
  discusión antes de escribir conclusión alguna. Un acierto nuevo en EV1-018
  (mejora_posible) y una regresión en los 8 candidatos nombrados están dentro de
  las ramas.
- **El titular del resultado es v2→v3.** Toda mención de run_3 lleva el caveat
  registrado: run_3 exhibe el mismo síntoma de provenance imprecisa, su mecanismo
  interno no fue verificado con la profundidad con que se auditó v2/v3, y su
  baseline sellado (31/36 post-adjudicación) vale como medido — la referencia es
  descriptiva, no un tercer brazo en disputa.
- Las **locations imperfectas** de los nodos que fundan las predicciones de
  acierto de EV1-031 y EV1-042 (falsos headers RX-03: "Punto 2.10…", "Punto 1.2…",
  "Punto 3.17. ii)…" contra GT 2.8.3.3 y 3.5.3) se leen como **calidad de cita
  esperada por debajo del GT, ya predicha** en el mapeo (§F.3) — no como hallazgo
  nuevo ni como descuento sorpresivo del acierto.

## 7. Salidas de la corrida

Respetando la estructura del escalón 1 (informe, "Archivos producidos"):

- **Dbs:** `evaluacion/posthoc_run/escalon1b_r{1,2,3}.db` (copias de
  `escalon1_r{N}.db` + filas nuevas de v3). Las originales quedan intactas.
- **Trazas y summaries:** `evaluacion/posthoc_run/traces/escalon1b_r{N}/…` +
  `summary_escalon1b_r{N}_*.json` (los tres brazos; v2/run_3 regenerados de caché,
  v3 fresco).
- **Copias por corrida:** `evaluacion_escalon1/corridas/reensamblado_v3/<id>_r<N>.json`
  (36 × 3, mismo formato que las 216 del escalón 1).
- **Resultados:** `evaluacion_escalon1/corridas/resultados_1b_<fecha>.json`
  (mayorías por pregunta × brazo, pares discordantes v2→v3) — la tabla final se
  computa tras la adjudicación humana de las réplicas flaggeadas, como en el
  escalón 1.
- **Evidencias de régimen:** hit-rate por brazo y réplica (§4), anti-fuga
  (`corridas/antifuga_1b_<fecha>.json`), mapping de anonimización con semilla
  (`corridas/mapping_anonimizacion_1b.json`), log
  (`evaluacion_escalon1/logs/corridas_1b_<fecha>.log`), costo acumulado del
  tracker contra el tope de §4.
- **Registro de queries nuevas del agente sobre v3** (insumo del re-screen de
  entierro en la lectura): `evaluacion_escalon1/corridas/queries_v3_<fecha>.json`
  — todas las llamadas a `buscar_nodos` (consulta + límite) y `ver_nodo`/
  `ver_vecinos` (ids) por caso y réplica, extraídas de las trazas de v3; la
  lectura las cruza contra el screen del mapeo (§B) para cerrar el circuito de
  candidatos a regresión.
- **Fichas nuevas** por cada delta (formato §6), en
  `evaluacion_escalon1/corridas/fichas_delta_1b.json`.

— Fin del protocolo. Sellar por commit antes de la primera llamada del 1b. —

## Enmienda §8 (2026-07-30)

Registro esta enmienda con la corrida detenida por la guarda de §4 (log
`data/experiment/evaluacion_escalon1/logs/corridas_1b_2026-07-30.log`). Las
secciones 1–7 quedan intactas; esta sección solo agrega el tratamiento de los
huecos de caché que la guarda detectó.

### a) El hallazgo (mecánico)

`llm_cache` no almacena errores por diseño (write-through de éxitos; un error se
propaga sin guardarse). Por lo tanto **la caché reproduce éxitos, no fracasos**:
las `failed_trace` del escalón 1 que murieron en una llamada fallida dejaron
huecos irrellenables exactamente en su punto de falla — el último turno
almacenado termina en `stop_reason=tool_use` y el turno siguiente no existe en
ninguna db. Un replay 100% byte-idéntico del brazo v2 es **imposible por
construcción**. La guarda de §4 detectó el primer hueco al primer request
(evidencia: el log de la corrida detenida — miss único del turno 3 de EV1-010,
réplica 2, brazo v2; el replay pagó ese turno y produjo una traza con
`failed_trace=False`, divergente del sellado `failed_trace=True`).

### b) Regla de exención acotada

Pre-scan exhaustivo (2026-07-30, determinístico, solo lectura) sobre las TRES
dbs selladas `escalon1_r{1,2,3}.db` y los DOS brazos cacheados: 216
combinaciones (pregunta × réplica × brazo) reconstruidas turno a turno.
Huecos detectados — la lista completa es:

| Pregunta | Réplica | Brazo | Turnos cacheados | stop_reason del último | Error sellado registrado |
|---|---|---|---|---|---|
| EV1-010 | r2 | grafo_v2 | 2 | `tool_use` | `APIConnectionError: Connection error.` |
| EV1-016 | r3 | grafo_v2 | 3 | `tool_use` | `BadRequestError 400: messages.6: user messages must have non-empty content` |

Cero huecos en run_3; cero anomalías de secuencia en las 214 combinaciones
restantes (patrón sano: historias impares consecutivas con cierre opcional de
límite de tools). La lista concilia 1:1 con las `failed_trace` selladas del
escalón 1: todo hueco tiene su `failed_trace` y toda `failed_trace` tiene su
hueco.

**Regla:** las dos combinaciones enumeradas — **EV1-010·r2·grafo_v2 y
EV1-016·r3·grafo_v2** — quedan **EXENTAS del replay**: no se re-corren, no se
pagan, y su resultado sellado (`failed_trace=True` → no-correcta dentro del
baseline adjudicado) se **ACARREA** a los artefactos del 1b con la marca
`origen=sellado_escalon1_hueco_cache`. La guarda de §4 permanece **totalmente
armada** para cualquier otro request: un miss fuera de esta lista enumerada
sigue abortando la corrida.

### c) Artefactos del desvío del 2026-07-30

- La fila pagada del turno 3 de EV1-010 ($0.0061) queda en `escalon1b_r2.db`
  como crudo **INERTE**: la pregunta exenta no se re-corre, así que esa entrada
  no vuelve a consultarse.
- Las trazas divergentes de v2·r2 generadas por la corrida detenida se mueven a
  `posthoc_run/traces/escalon1b_r2/grafo_v2_DIVERGENTE_NO_USAR/` y quedan como
  **evidencia del hallazgo, excluidas de todo insumo de lectura**. El
  directorio `escalon1b_r2/grafo_v2/` queda libre para regenerarse en el
  relanzamiento.

### d) Invariante que la enmienda preserva

El baseline v2 = **27/36 vale como medido y adjudicado, incluidas sus dos
`failed_trace`**; ninguna regla de §1–§7 cambia; esta enmienda solo gobierna el
tratamiento de los dos huecos enumerados durante el replay. El brazo v2 del 1b
queda así definido como: 34 preguntas × 3 réplicas por replay byte-idéntico +
las 2 combinaciones exentas acarreadas del sellado (las otras réplicas de
EV1-010 y EV1-016 SÍ se replican; la exención es por combinación, no por
pregunta).

### e) Registro metodológico (para la discusión de la tesis)

El replay por caché tiene un punto ciego sistemático: reproduce el
comportamiento exitoso pero no las fallas de infraestructura, porque el error
nunca se almacena — el registro de lo medido y el registro de lo reproducible
no coinciden exactamente donde el sistema falló. Toda arquitectura de
re-medición barata por caché hereda este sesgo de supervivencia y necesita, como
acá, un inventario explícito de huecos y una regla de acarreo pre-registrada
(evidencia: `logs/corridas_1b_2026-07-30.log`).
