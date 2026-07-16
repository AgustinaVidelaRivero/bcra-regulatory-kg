# Protocolo pre-registrado — piloto del compuesto v6.0-D (2026-07-15)

## 1. Qué es

Primera **validación prospectiva** del instrumento compuesto v6.0-D (verificador v5.7
congelado + capa determinística; `docs/especificacion_capa_deterministica.md`, §7) sobre
fallas de run_3 que el instrumento **nunca vio**: ni en su iteración (dev set), ni en sus
gates, ni en la construcción de la capa. Este protocolo se commitea **ANTES de la
adjudicación humana y ANTES de cualquier corrida** — todo lo que sigue queda fijado ahora,
con los veredictos del compuesto todavía inexistentes.

## 2. Universo

**Definición principista:** un caso de run_3 (frozen eval, eval_set_v1) integra el universo
si exhibe **algún síntoma de capa 1 de la taxonomía del verificador**, mapeados a las
dimensiones que el frozen registra:

| Síntoma capa 1 | Dimensión del frozen | Regla |
|---|---|---|
| `noise_sensitivity` | correctitud FINAL modal (reporte ETAPA 2) | ∈ {incorrecta, parcial} |
| `context_recall` | completitud modal | = parcial (patas no cubiertas) |
| `faithfulness` | afirmaciones **CENTRALES** no soportadas | > 0 en alguna rep |

La justificación la dejo escrita: **el universo del verificador es su propia capa 1** — el
instrumento existe para atribuir causas a los tres síntomas, así que cualquier subconjunto
menor dejaría fuera síntomas que le son propios. El criterio por correctitud/completitud solo
(el del censo previo) habría excluido, por ejemplo, las fallas puras de `faithfulness`
(claims centrales sin soporte dentro de respuestas "correctas"), que son exactamente el
síntoma de entrada de la rama `alucinacion_agente`/`completitud_kg` del árbol.

**Fuentes:** `frozen_run/reporte_final.md` (correctitud FINAL), `frozen_run/agg_run_3.json`
(completitud), `frozen_run/traces/run_3/CQ-*.json` (centrales no soportadas por rep) —
conteos verificados contra las trazas del frozen para este protocolo.

**RESULTADO — universo del piloto: 5 casos.**

| Caso | Categoría | Síntoma que lo incluye | Detalle verificado (por rep) |
|---|---|---|---|
| CQ-016 | factual_directa | `context_recall` | completitud parcial **3/3** (centrales no sop.: 0/0/0; correctitud correcta 3/3) |
| CQ-018 | multi_norma | `faithfulness` | centrales no soportadas **3/0/2** (completitud completa; correctitud correcta) |
| CQ-019 | multi_norma | `faithfulness` | centrales no soportadas **0/0/1** (completitud completa; correctitud correcta) |
| CQ-024 | multi_norma | `faithfulness` | centrales no soportadas **1/0/0** (completitud completa; correctitud correcta) |
| CQ-033 | cadena_restriccion_excepcion | `faithfulness` | centrales no soportadas **1/0/0** (completitud completa; correctitud correcta) |

**EXCLUIDOS:**

- **Los 5 casos del gate** (CQ-017, CQ-020, CQ-025, CQ-031, CQ-034): quemados como material
  de calibración — motivaron la vara, los gates y los módulos de la capa.
- **Las unanswerable CQ-037 y CQ-038** (centrales no soportadas 2/1/1 y 1/0/1, abstención
  correcta 3/3 en ambas): la taxonomía vigente **no tiene categoría para preguntas
  irrespondibles** — su árbol arranca de patas respondibles y sus causas presuponen un dato
  que debió estar. Exclusión documentada como **límite conocido de la taxonomía**, no como
  decisión de conveniencia; si el pipeline necesita atribuir fallas de abstención, eso exige
  una extensión taxonómica propia, fuera de este piloto.

Los 5 casos del universo tienen su traza post-hoc disponible (pre-requisito del compuesto).

## 3. Disclosure por caso — homólogos en el dev set

El dev set de iteración del verificador usó preguntas de eval_set_v1 sobre OTROS grafos
(run_1/run_5). Verificado contra
`.claude/skills/kg-refinement/references/referencias_dev_set.md`:

| Caso del piloto (run_3) | Homólogos en el dev set (otro grafo) | Rol en la iteración |
|---|---|---|
| CQ-016 | `off/run_1/CQ-016` | expansión post-gate #1 (patrón "exoneración integral + secundaria provenance") |
| CQ-018 | `off/run_1/CQ-018` | expansión post-gate #1 (patrón "primaria única + FPs masivos") |
| CQ-019 | `on/run_1/CQ-019` **y** `on/run_5/CQ-019` | dev original + expansión (dos homólogos) |
| CQ-024 | `off/run_1/CQ-024` | dev original |
| CQ-033 | **ninguno** | — |

La nota que acompaña: **las fallas de grafo son específicas de cada grafo** — otros nodos,
otras trayectorias, otros defectos. El instrumento conoció estas PREGUNTAS en otros grafos,
no estos casos: lo que se transfirió por el dev set es, a lo sumo, familiaridad con el tema
de la pregunta, no con la falla a atribuir. **CQ-033, sin ningún homólogo en ninguna etapa,
es la medición más limpia del piloto.**

## 4. Adjudicación humana ciega (ANTES de cualquier corrida)

Adjudico los 5 casos yo, ANTES de que el compuesto corra sobre ellos. El sellado acá es
**por inexistencia**: como el compuesto no ha corrido sobre estos casos, los veredictos que
podrían sesgarme no existen al momento de adjudicar.

**Circuito de adjudicación:** el mismo con el que re-fundé la vara v3 —

- evidencia de ausencia/presencia por **re-ejecuciones determinísticas de las trazas**
  (outputs COMPLETOS; nunca la traza truncada almacenada);
- **barridos programáticos** sobre el kg congelado (ids, labels, properties);
- verificación de contenido **contra los PDF** del corpus;
- las herramientas **D1** (prueba de alcanzabilidad) y **D5** (diligencia de literales) como
  **instrumentos de adjudicación** — el mismo código que usará el compuesto, usado acá como
  lupa del humano.

**Producto:** GTs en pares `{sintoma_capa1, causa_capa2}` de la **taxonomía v2.6.1**, con
jerarquías (primarias/secundarias), patas, **regla de acierto por caso** y evidencia citada —
en un archivo NUEVO, `.claude/skills/kg-refinement/references/casos_piloto.md`, **commiteado
ANTES de la corrida**.

## 5. Corrida — ÚNICA

- **Instrumento:** verificador v5.7 congelado, `--n 3` + voto, seguido de la capa
  determinística completa (`aplicar_capa`, v6.0-D) — el compuesto, no el v5.7 pelado.
- **Casos:** los 5 del universo, con sus trazas post-hoc.
- **Guarda previa (tipo paso-0):** antes de ejecutar, la corrida verifica que el commit de
  `casos_piloto.md` esté en HEAD (`git log` sobre el archivo). Sin ese commit, no se corre.
- **Sin iteración:** se corre UNA vez y se lee, cualquiera sea el resultado. No hay segunda
  corrida, no hay ajuste intermedio.
- **Presupuesto estimado:** ~6M tokens de input (base medida del gate #2: ~394K de input por
  caso-rep → ~1,2M por caso × 5 casos).

## 6. Scoring y métricas (pre-registradas)

**Scoring por caso** contra `casos_piloto.md`, con las reglas del gate — verbatim de
`docs/protocolo_gate2.md` §4:

> - **ACIERTO** — el voto (mayoría estricta) coincide con el patrón de acierto del caso según la vara.
> - **MISS** — mayoría en un resultado incorrecto.
> - **TRIAGE** — voto dividido (`flag_voto_dividido=true`): se reporta como **derivación a revisión humana**, no como acierto ni como miss silencioso.
> - **`formato_invalido` en una repetición cuenta como repetición SIN voto** (el voto se computa sobre las repeticiones con salida válida; si con ello no hay mayoría estricta sobre el total de K=3, el caso es TRIAGE).
> - El voto del protocolo se computa sobre las repeticiones VÁLIDAS (sin `formato_invalido`): mayoría estricta requiere ≥2 reps válidas coincidentes; con <2 reps válidas o sin mayoría entre ellas → TRIAGE.

con una precisión propia de este piloto: el voto que se scorea es **`voto_capa_d`** — el
veredicto del COMPUESTO, después de las correcciones de la capa —; el voto v5.7 original se
reporta **al lado**, como comparación (cuántos casos cambia la capa y en qué dirección).

**Lectura por canal del compuesto:** cada caso se reporta por el canal en que salió —
**veredicto automático** (sin triage) o **triage con motivo** (R1-R5). Un caso en triage se
reporta como derivación a revisión humana, no como miss silencioso; el error grave del
compuesto es solo el veredicto automático incorrecto.

**Tablero (los contadores de la especificación §6):** discrepancias D2, quotes D3 no
verificados, banderas D5, triage por motivo (R1-R5).

**Métrica principal:** acuerdo compuesto-vs-humano sobre los 5 casos (voto_capa_d contra el
GT de `casos_piloto.md`, canal por canal).

## 7. Regla de frenado

**Ningún módulo de la capa ni prompt del verificador se ajusta contra estos 5 casos** —
cualquiera sea el resultado del piloto. Los hallazgos (aciertos, misses, límites nuevos del
compuesto, huecos de la taxonomía) van al **documento de lectura del piloto**, que se publica
con este protocolo citado. Si un hallazgo motiva un cambio del instrumento, ese cambio se
valida sobre casos que este piloto no tocó — estos 5 quedan quemados en el momento en que el
compuesto los corre, igual que los del gate.
