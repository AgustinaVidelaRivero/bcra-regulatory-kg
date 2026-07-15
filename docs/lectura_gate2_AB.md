# Gate #2 del verificador — doble lectura (A y B)

**Fecha:** 2026-07-15. **Corrida:** única, pre-registrada (protocolo `docs/protocolo_gate2.md`,
commit `c0b96a4`): 5 casos de run_3 × 3 repeticiones, verificador v5.7 congelado, N=3 + voto.

## 1. Qué es este documento

El gate #2 se corrió **UNA sola vez**, contra la vara vigente en ese momento
(`casos_control.md` en `5bb58c0`). Después de esa corrida re-expresé la vara en la taxonomía
v2.6.1 (**vara v3**; historia completa de cambios, GTs anteriores verbatim y evidencia en
`.claude/skills/kg-refinement/references/nota_readjudicacion_vara_v3.md` y
`docs/evidencia_vara_v3/`), manteniendo los **veredictos del verificador sellados durante
todo el proceso** de re-adjudicación. Este documento publica **ambas lecturas juntas**:

- **Lectura A** — los mismos veredictos contra la vara anterior (`5bb58c0`).
- **Lectura B** — los mismos veredictos contra la vara v3.

**Ninguna corrida nueva:** son los mismos 15 veredictos congelados (5 casos × 3 reps), leídos
contra dos varas. Reglas de scoring, verbatim del protocolo pre-registrado
(`docs/protocolo_gate2.md` §4):

> - **ACIERTO** — el voto (mayoría estricta) coincide con el patrón de acierto del caso según la vara.
> - **MISS** — mayoría en un resultado incorrecto.
> - **TRIAGE** — voto dividido (`flag_voto_dividido=true`): se reporta como **derivación a revisión humana**, no como acierto ni como miss silencioso.
> - El voto del protocolo se computa sobre las repeticiones VÁLIDAS (sin `formato_invalido`): mayoría estricta requiere ≥2 reps válidas coincidentes; con <2 reps válidas o sin mayoría entre ellas → TRIAGE.

Las 15 repeticiones fueron válidas (`formato_invalido: false` en todas; inventario en la
extracción de veredictos, `posthoc_run/dev_set/veredictos_gate2_v57.md`).

## 2. Lectura A (vara `5bb58c0`)

Fuente: `posthoc_run/dev_set/gate2_v57/resumen.md` (resumen de la corrida; votos
programáticos y desglose por rep):

| Caso | Voto programático | Desglose por rep (pares primarios) | Scoring A |
|---|---|---|---|
| CQ-034 | mayoría {context_recall, completitud_kg} (2-1) | rep1: completitud ×2 · rep2: completitud · rep3: completitud ×2 | **ACIERTO** |
| CQ-020 | frontera_no_determinada (dividido, 1-1-1) | rep1: aplicacion_erronea + contenido_kg · rep2: aplicacion_erronea · rep3: aplicacion_erronea + provenance_imprecisa | **TRIAGE** |
| CQ-017 | mayoría con clave VACÍA (2-1) | rep1: sin primarias · rep2: completitud_kg + provenance_imprecisa · rep3: sin primarias | **MISS** (la vara exige ambas primarias) |
| CQ-025 | mayoría {noise_sensitivity, aplicacion_erronea} (2-1) | rep1: navegación · rep2: aplicacion_erronea · rep3: aplicacion_erronea | **MISS** (vara: contenido_kg) |
| CQ-031 | mayoría {context_recall, navegación} (3-0) | las 3 reps: navegación | **MISS** (vara: alcanzabilidad_kg) |

**Agregado A: 1 acierto · 1 triage · 3 miss.**

## 3. Lectura B (vara v3) — caso por caso

Mismos 15 veredictos; scoring con las reglas del protocolo (mayoría estricta ≥2 sobre reps
válidas; triage si voto dividido) contra la vara v3.

- **CQ-034 — ACIERTO.** El voto de mayoría (reps 1 y 3) es `{context_recall, completitud_kg}`
  como primaria sobre las dos patas faltantes (débito en cuenta; límite general del 3.9).
  Ninguna rep atribuye defecto a la pata del efectivo, con lo que el voto pasa también la
  **regla endurecida** de la vara v3 (atribuir un defecto a la pata sana invalida el acierto).

- **CQ-020 — TRIAGE.** `flag_voto_dividido=true` (conteo 1-1-1): regla del protocolo,
  independiente de la vara. Observación (no altera el scoring): las 3 reps emitieron
  atribuciones del lado `noise_sensitivity` (`aplicacion_erronea` y variantes); ninguna
  encontró la primaria `{context_recall, completitud_kg}` de la vara.

- **CQ-017 — MISS.** La mayoría (reps 1 y 3) emitió **clave vacía** — exoneración total:
  todas sus atribuciones son `sin_defecto`/`sin_par` —; la vara exige detectar **AMBAS**
  primarias (`estructural_kg` Y `provenance_imprecisa`). La rep 2, minoritaria, encontró una
  de las dos (`{noise_sensitivity, provenance_imprecisa}`).

- **CQ-025 — MISS.** Mayoría `{noise_sensitivity, aplicacion_erronea}` (2-1) contra la
  primaria `{noise_sensitivity, contenido_kg}` de la vara; la vara v3 documenta
  explícitamente la **exclusión de `aplicacion_erronea` por el test v2.6** (la rama "nodo
  fiel" no se alcanza: el nodo contradice al PDF; el defecto es de contenido, no de
  aplicación). Este resultado se lee con el **asterisco del protocolo**
  (`docs/protocolo_gate2.md` §2(b)): este mismo caso expuso en el gate #1 el hueco que motivó
  la creación de `aplicacion_erronea` (v2.5).

- **CQ-031 — MISS.** Mayoría unánime 3-0 `{context_recall, navegación}` contra la primaria
  `{context_recall, alcanzabilidad_kg}` de la vara; la vara v3 excluye `navegación`
  **EMPÍRICAMENTE** (simulación completa del índice léxico,
  `docs/evidencia_vara_v3/verificaciones_vara_v3.md` §2: el portador nunca entra al top-10 —
  0/10 consultas, mejor rank 13 —; el mecanismo es el token del id truncado en `garanti`, que
  la búsqueda "garantias" no matchea).

## 4. Agregado y conclusión

**Lectura B: 1 acierto · 1 triage · 3 miss — IDÉNTICO a la lectura A.**

| Caso | Lectura A (vara 5bb58c0) | Lectura B (vara v3) |
|---|---|---|
| CQ-034 | ACIERTO | ACIERTO |
| CQ-020 | TRIAGE | TRIAGE |
| CQ-017 | MISS | MISS |
| CQ-025 | MISS | MISS |
| CQ-031 | MISS | MISS |

La conclusión que me llevo: la hipótesis de que los miss del gate medían, en parte, la
**desincronización entre la vara y la taxonomía** queda **REFUTADA**. Re-expresé la vara en
el vocabulario vigente (v2.6.1), re-fundé su evidencia en re-ejecuciones determinísticas y
barridos programáticos, y los miss **persisten idénticos**: son errores genuinos del
instrumento v5.7, no artefactos de medición de una vara desactualizada.

## 5. Caracterización de los miss: evidencia vs. etiqueta

Los tres miss no son del mismo tipo, y la distinción importa para decidir qué se hace con
ellos:

- **CQ-031 y CQ-025 son errores de ETIQUETA en fronteras taxonómicas**, con la evidencia
  correcta identificada: en CQ-031 las 3 reps encontraron el portador correcto del 4.5 y
  documentaron que el agente no lo alcanzó — eligieron `navegación` donde la frontera
  navegación/alcanzabilidad exigía `alcanzabilidad_kg`; en CQ-025 la mayoría identificó el
  nodo y el desvío correctos — eligió `aplicacion_erronea` donde la frontera
  aplicación/contenido exigía `contenido_kg`.
- **CQ-017 es un error de EVIDENCIA (sobre-exoneración):** la mayoría declaró el caso sin
  defecto del sistema; no es una etiqueta mal elegida sobre la evidencia correcta sino
  evidencia no encontrada (la arista cross-documento faltante y la provenance gruesa).

El cierre que me importa dejar escrito: **las fronteras de etiqueta estables resultaron
computables**. La prueba de alcanzabilidad es una simulación determinística del índice; la
verificación de un quote contra el contenido de un nodo es un substring normalizado. La
respuesta a estos miss NO es iterar el prompt — el instrumento está congelado y el gate #2
fue, por pre-registro, la última calibración — sino **decidir esas fronteras en código**,
donde la decisión es reproducible y auditable. Ese trabajo ya está implementado como capa
determinística sobre la salida del verificador (módulos D1-D5, versión `v6.0-D(2026-07)`:
decisor de la frontera navegación/alcanzabilidad, validador de quotes de `aplicacion_erronea`,
diligencia de causas de ausencia y política de triage); su especificación se documenta por
separado (`docs/especificacion_capa_deterministica.md`).

## 6. Disclosure

- La re-adjudicación de la vara (v3) ocurrió **después** de ver el **agregado** del gate #2,
  pero con los **veredictos por caso sellados** durante todo el proceso: la constancia está
  en la guarda del paso 0 de la extracción de veredictos
  (`posthoc_run/dev_set/veredictos_gate2_v57.md`), que verificó el commit de la vara v3 en
  HEAD antes de abrir cualquier veredicto.
- **Ambas lecturas se publican siempre juntas** — este documento es esa publicación.
- El instrumento **no se re-corrió ni se re-correrá** contra estos 5 casos: la corrida del
  gate #2 es única y final (protocolo `c0b96a4`), y sus 15 veredictos quedan congelados como
  se emitieron.
