# Informe — Corridas escalón 1: run_3 vs grafo_v2 sobre EV1 (2026-07-26)

**Resultado: las 216 corridas (36 preguntas × 2 grafos × 3 réplicas frescas) completadas bajo el protocolo sellado, juzgadas por el juez v2.1.1 ciego contra `key_adjudicada`, con anti-fuga 0/216 y tablas primaria y secundaria computadas de las trazas reales. Verificador diagnóstico corrido SOLO sobre las 3 fallas de run_3 (guarda de dominio limpia); las 6 fallas de v2 quedan en fichas sin veredicto causal. Costo total de la unidad: USD 19.24 (corridas 10.88 + preflights 0.03 + verificador ≈8.33), bajo el tope de USD 25.** Sin commits. Se reportan números; la lectura contra P1–P5 y todo veredicto de ganador son de la autora.

---

## PASO 0 — Precondiciones (verificadas antes de gastar)

- (a) Vara sellada: commit `d91b832` (protocolo + EV1 + answer key adjudicada + actas).
- (b) `protocolo_escalon1.md` §0 contiene el hash del brazo v2: `11f0d4a`.
- (c) Congelamiento del cuarteto+runner, sha256[:12] y fecha de modificación:
  `loader.py 5aba8b7a0aa4` (2026-07-17) · `harness.py fd267e833866` (2026-06-10) · `judge.py 7169145aaeb3` (2026-06-09) · `llm_cache.py fc86b0e48df4` (2026-06-23) · `runners/run_posthoc.py 0918f63c30bd` (2026-07-22) · `verificador.py 084b2db8efe4` (2026-07-14). Ninguno se editó en esta unidad.
- (d) Brazos presentes: `run_3_ppf_core/kg.json` (4.843.199 bytes) y `grafo_v2/kg.json` (5.056.690 bytes, commit `11f0d4a`). Credencial presente en `evaluacion/.env`.

## Cableado (sin tocar el cuarteto) y validación offline

- **`grafo_v2` en el loader:** registrado EN MEMORIA por [code/run_escalon1.py](../../evaluacion_escalon1/code/run_escalon1.py) (patrón "módulo aparte que importa al loader"; `code_version` no rota, cachés previas intactas). Adaptador `{node_extra: None, edge_extra: None}` (el assemble v2 emite un `provenance` dict único; ids ya deduplicados).
- Checks de carga (offline): 3.872 nodos / 7.231 aristas (== crudo), 0 merges, ids únicos, todo nodo y arista con ≥1 provenance normalizada, endpoints existentes, esqueleto visible (78 nodos `Sujeto`, 57 `subclase_de`). Selftest del runner: **14/14 PASS**.
- **Derivado de corrida `EV1_runtime.json`** (la key sellada no se modificó): `respuesta_esperada = key_adjudicada`, `ground_truth_secciones = puntos_citados`, `categoria = familia`, `cita_textual = None`. Orden de preguntas barajado con **semilla 20260726**, registrado en el `_meta` del archivo:
  `011 001 025 020 032 022 008 016 012 039 038 029 004 036 034 023 006 042 028 027 002 021 015 005 019 031 035 018 003 010 024 013 017 026 030 007`.

**Desviación documentada (contrato del juez):** el formato sellado del protocolo §2 no porta cita verbatim separada (la cita vive dentro de la respuesta adjudicada y en `puntos_citados`), por lo que el referente del juez va sin `cita_textual`. No se fabricó una cita ni se disfrazó la key. Es **simétrico entre brazos** (variable única intacta) y, por el mapping v2.1, `no_soportado` nunca baja correctitud — el costo es solo menor capacidad de confirmar afirmaciones granulares, igual para ambos grafos. (El gate de completitud de referente de la skill eval-pipeline se registró como no aplicado; gobierna el protocolo sellado.)

## PASO 1 — Proyección de costos (gate USD 25: PASÓ)

Con tokens reales del histórico `off/run_3` (23 preguntas): agente Haiku $0.03022/pregunta + juez $0.02093/pregunta → **USD 11.05** proyectados para 216 corridas (USD 16.57 con margen +50%). El runner tarifa el juez a precios reales de `claude-sonnet-4-6` ($3/$15 por MTok, `run_posthoc.py:73-79`) — la distorsión "tracker a precios Haiku" de B1b no aplica: el único tracker Haiku es el del agente, que ES Haiku. Control reportado: si el juez se tarifara a precios Haiku daría $0.007/pregunta; no es lo que computa el pipeline.

## PASO 2 — Corridas (216/216 completas)

- Preflights de ambos brazos: PASS (`end_turn`, tokens poblados; el de `grafo_v2` valida el cableado contra la API). Costo $0.0273.
- **Orden de las 6 corridas sorteado con semilla 20260726:** v2·r1 → v2·r3 → run_3·r3 → run_3·r2 → v2·r2 → run_3·r1.
- **Réplicas frescas:** una db de caché nueva por réplica (`posthoc_run/escalon1_r{1,2,3}.db`); hit_rate del agente **0.0 en las 6 corridas** (la reparación de v2·r2 repuso de su propia db, ver abajo). Labels `escalon1_r{N}`; trazas en `evaluacion/posthoc_run/traces/escalon1_r{N}/{run_3,grafo_v2}/`.
- Costos por corrida (summaries reales): v2·r1 $1.8180 · v2·r3 $1.8233 · run_3·r3 $1.8169 · run_3·r2 $1.8152 · v2·r2 $1.7971 · run_3·r1 $1.8067 → **total corridas $10.8772** (por grafo: run_3 $5.4388, grafo_v2 $5.4384).
- Copias por corrida derivadas a `evaluacion_escalon1/corridas/<grafo>/<id>_r<N>.json` (216 archivos: respuesta final, traza de tools truncada, pasos, tokens, costo).

### Fallas técnicas (reparadas, registradas, pregunta re-corrida completa — protocolo §1)

1. **Word-splitting de zsh en el lanzador** (19:59): las 6 corridas abortaron ANTES de tocar la API (`--run "grafo_v2 1"` inválido). $0 perdidos. Reparado el split y relanzado completo. Registrado en `logs/corridas_2026-07-26.log`.
2. **`APITimeoutError` de red en el juez** de EV1-018 (v2·r2, 20:35), tras los reintentos nativos del SDK. El error no se cachea (llm_cache propaga sin guardar) → relanzamiento de la corrida con la misma db: las 27 preguntas completas repusieron de caché byte-idénticas (hit_rate 0.8192, $0 re-pagado) y las 9 restantes (incluida EV1-018 completa) corrieron frescas.

### Fallas del sistema bajo evaluación (NO se reintentan, por diseño)

2 réplicas con `failed_trace: true` (parse del JSON final), ambas del brazo v2: **EV1-016·r3** y **EV1-010·r2**. Cuentan como no-correcta en su mayoría (ninguna de las dos alteró el veredicto por mayoría de su pregunta: ambas quedaron 2-1 correcta).

## PASO 3 — Anti-fuga (0 casos)

Escaneadas las 216 respuestas (lo que el juez ve: respuesta + citas) buscando prefijo `Sujeto_`, los 70 ids del catálogo, "esqueleto", `subclase_de`/`miembro_de`/`instancia_de` y `nivel: rol/clase/instancia`, simétrico en ambos brazos: **0 respuestas con identificadores de esquema**. Registro: `corridas/antifuga_2026-07-26.json`. Ninguna respuesta fue editada. *(Desviación de secuencia documentada: el runner congelado juzga inline, así que el escaneo corrió después del juez; el resultado es idéntico porque las respuestas no se editan en ningún caso — el chequeo registra riesgo, no filtra.)*

## PASO 4 — Juez ciego y mayorías

- **Ceguera estructural:** el payload del juez (judge.py:274-297) contiene pregunta, categoría, referente, descomposición, citas y respuesta — **nunca la identidad del grafo**. No hizo falta pasada separada de anonimización; el mapping A/B por pregunta (semilla 20260726) quedó igual generado como registro auditable en `corridas/mapping_anonimizacion.json`.
- Regla de mayoría: correcto si `correctitud == "correcta"` en ≥2 de 3 réplicas; `failed_trace` cuenta como no-correcta.

## PASO 5 — Tablas (números; sin lectura contra P1–P5)

### Primaria — % correcto por mayoría

| | run_3 | grafo_v2 |
|---|---|---|
| **Global (36)** | **33 (91.7%)** | **30 (83.3%)** |
| puntual (10) | 9 | 8 |
| enumerativa (12) | 11 | 10 |
| condicional (8) | 8 | 8 |
| sujeto (6) | 5 | 4 |

**Pares discordantes (McNemar descriptivo):** b = run_3✗→v2✓ = **1** (EV1-023) · c = run_3✓→v2✗ = **4** (EV1-039, EV1-029, EV1-042, EV1-005). Ambos fallan: EV1-011, EV1-028. *(Nota de registro, sin veredicto: EV1-039 es la pregunta de la observación pre-corrida del acta de adjudicación — control P3; la adjudicación de la vía de falla es humana.)*

### Secundaria

| | run_3 | grafo_v2 |
|---|---|---|
| Mayorías 3-0 | 31 | 29 |
| Mayorías 2-1 | 5 | 7 |
| Pasos promedio (tool calls/rep) | 9.60 | 9.71 |
| Réplicas que tocaron el límite de 15 tools | 38/108 | 36/108 |

**Uso del esqueleto en trazas v2 (108 trazas):** 26 tool calls con nodos `Sujeto_` en el input, concentrados en **9/108 trazas** (8.3%); **7/108 trazas** (6.5%) exhiben aristas `subclase_de`/`miembro_de` en outputs de tools.

**Réplicas con `requiere_adjudicacion_humana: true` (30):**
- run_3 (12): EV1-007r3 · EV1-011r1/r2/r3 · EV1-015r1/r2/r3 · EV1-018r2/r3 · EV1-034r1 · EV1-035r1/r2
- grafo_v2 (18): EV1-007r1/r2/r3 · EV1-011r1/r3 · EV1-015r1/r2/r3 · EV1-018r1/r2/r3 · EV1-027r1 · EV1-029r2/r3 · EV1-031r1/r2 · EV1-034r2/r3

Detalle completo por pregunta×grafo (veredictos por réplica, patrones 3-0/2-1) en `corridas/resultados_2026-07-26.json`.

## PASO 6 — Diagnóstico de fallas

### Fallas de run_3 (3) — verificador diagnóstico CON peso de evidencia

Corrido sobre la réplica 1 de cada falla (las 3 fallaron en r1; EV1-023 y EV1-028 fallaron 3-0, EV1-011 2-1). Salidas por caso en `evaluacion_escalon1/verificador/`. **Guarda de dominio: limpia en los 3** — toda la evidencia (nodos + PDF) dentro del `tos_fuente` de cada pregunta.

| Caso | Atribución primaria | Secundarias | Flags del detector |
|---|---|---|---|
| EV1-023 (Protección; precancelación) | `context_recall → completitud_kg` (grafo): el nodo `Restriccion_…precancelacion…` no porta el criterio de resolución temporal completo ("lo que ocurra primero") | `faithfulness → alucinacion_agente` | encuadre_invertido=True |
| EV1-011 (Clasificación; niveles cartera comercial) | `context_recall → completitud_kg` (grafo): faltan los niveles nominados de la cartera comercial | `faithfulness → alucinacion_agente` (nombres 'Potencial/Deficiente/Vencido' no existen en ningún nodo) · `noise_sensitivity → sin_defecto` | encuadre_invertido=True |
| EV1-028 (Protección; mutual PNFC) | `context_recall → completitud_kg` (grafo): no existe nodo/contenido que capture la salvedad del punto 1.1.2.5 | — | — |

*(El flag `encuadre_invertido` es un detector post-proceso del propio verificador; queda para la lectura humana de esos dos casos.)*

**Desviación operativa documentada:** el runner interno del verificador congelado (`_parse_casos`) solo acepta los labels históricos `off`/`on`; se usó un driver externo ([code/verificador_escalon1.py](../../evaluacion_escalon1/code/verificador_escalon1.py)) que llama `investigar_falla` directamente (import en lectura, verificador sin editar). Además, `recover_seen` lee hardcodeado `cache/calls.db`: para no degradar la evidencia (nodos vistos), se copiaron las 524 filas `agent` de `escalon1_r1.db` a `calls.db` (solo agrega filas de caché con claves nuevas; n_seen pasó de 0 a 18/92/98). Primer intento del runner (rechazo de label) registrado en `logs/verificador_2026-07-26.log`.

### Fallas de grafo_v2 (6) — fichas SIN veredicto causal (adjudicación humana)

El verificador NO se corrió sobre este brazo (calibración intra-run_3; lección 0/6 fuera de familia — protocolo §6). Fichas completas (pregunta, familia, `tos_fuente`, `ground_truth_secciones`, veredictos por réplica, respuesta final, claims reprobados por el juez, traza de tools) en `corridas/fichas_fallas_v2.json`:

| Id | Familia | TO fuente | Veredictos (r1/r2/r3) |
|---|---|---|---|
| EV1-005 | enumerativa | RegInf | incorrecta / incorrecta / incorrecta |
| EV1-011 | enumerativa | Clasificación | incorrecta / incorrecta / incorrecta |
| EV1-028 | sujeto | Protección | incorrecta / incorrecta / incorrecta |
| EV1-029 | sujeto | Protección | correcta / incorrecta / incorrecta |
| EV1-039 | puntual | CapMin | incorrecta / incorrecta / incorrecta |
| EV1-042 | puntual | Exterior | correcta / incorrecta / incorrecta |

## Costos reales de la unidad

| Paso | Costo (USD) |
|---|---|
| Preflights (2 × 3 llamadas Haiku) | 0.0273 |
| Corridas 216 (agente Haiku $1/$5 + juez Sonnet $3/$15) | 10.8772 |
| Verificador (3 casos, `claude-opus-4-8`, 37 llamadas; in=1.482.989 tok, out=36.701 tok) | ≈ 8.33 |
| **Total** | **≈ 19.24** |

**Nota de tarifa del verificador (transparencia):** el ≈8.33 usa la tarifa vigente de Opus ≥4.5 ($5/$25 por MTok). Si se tarifara a la tarifa legacy de Opus ≤4.1 ($15/$75) daría $25.00 y el total de la unidad sería ≈$35.90 — sobre el tope. Los conteos de tokens quedan registrados arriba para recomputar con la tarifa que corresponda; el gate del PASO 1 (proyección → USD 11.05 < 25) cubría las corridas, y el verificador se lanzó después de confirmar el costo real de aquellas ($10.88).

## Desviaciones documentadas (resumen)

1. Referente del juez sin `cita_textual` (formato sellado §2; simétrico entre brazos).
2. Anti-fuga posterior al juez (el runner juzga inline; las respuestas no se editan en ningún caso — resultado idéntico).
3. Anonimización: no hizo falta pasada separada (ceguera estructural del juez); mapping A/B con semilla generado como registro.
4. Verificador vía driver externo + merge de filas de caché para reponer nodos vistos (verificador y cuarteto sin editar).

## Archivos producidos (todo en `data/experiment/evaluacion_escalon1/` salvo trazas)

- `EV1_runtime.json` (derivado; key sellada intacta) · `code/{run_escalon1, build_runtime_EV1, derivar_corridas, antifuga, mayorias_tablas, mapping_anonimizacion, fichas_fallas_v2, verificador_escalon1}.py`
- `corridas/{run_3,grafo_v2}/` (216 copias) · `corridas/resultados_2026-07-26.json` · `corridas/antifuga_2026-07-26.json` · `corridas/mapping_anonimizacion.json` · `corridas/fichas_fallas_v2.json`
- `verificador/escalon1_r1_run_3_{EV1-011,EV1-023,EV1-028}.json`
- `logs/{corridas,verificador}_2026-07-26.log`
- Trazas y summaries del runner: `evaluacion/posthoc_run/traces/escalon1_r{1,2,3}/` + `summary_escalon1_r{N}_{run}.json` + dbs `escalon1_r{N}.db`, `escalon1_preflight.db`.

**FRENO acá.** Pendientes tuyos: lectura de la tabla primaria/secundaria contra P1–P5 (sellado — no lo leí para redactar), adjudicación manual de las 6 fichas de v2 (incl. EV1-039, la del control P3) y de las 30 réplicas con `requiere_adjudicacion_humana`, laudo sobre los 2 casos del verificador con flag `encuadre_invertido`, y el commit del paquete.
