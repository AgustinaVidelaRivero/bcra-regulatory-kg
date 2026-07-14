# Protocolo pre-registrado — GATE #2 del verificador (2026-07-15)

> Este protocolo se commitea ANTES de la corrida. La corrida no comienza hasta que el protocolo esté commiteado por la autora.

## 1. Qué es

Segunda y **ÚLTIMA** calibración del verificador (**v5.7, congelado**) contra los **5 casos-control de run_3** (off/run_3: CQ-017, CQ-020, CQ-025, CQ-031, CQ-034). Se corre **UNA vez**. **Nada se ajusta después contra estos casos, cualquiera sea el resultado.** Ambos gates se reportan **SIEMPRE juntos** en la tesis:

- **Gate #1:** 2/5 + 1 `formato_invalido` (2026-07-14, v5.5, N=1 — detalle en `docs/especificacion_verificador_v57.md` §2.2).
- **Gate #2:** el de este protocolo.

## 2. Disclosure completo de lo ocurrido entre gates

- **(a)** Se **vieron los resultados por caso** del gate #1 (comparación externa contra `casos_control.md`, hecha por la autora).
- **(b)** Cambios al instrumento desde entonces:
  - **Taxonomía v2.5** — nueva causa `aplicacion_erronea` + vía de escape a `frontera_no_determinada` en el retry de formato. **ADVERTENCIA EXPLÍCITA: el agujero del árbol que motivó v2.5 fue expuesto por el caso run_3/CQ-025 del propio gate #1; el resultado de CQ-025 en el gate #2 se lee con ese asterisco** (el arreglo deriva de información de ese caso, aunque nunca se re-corrió contra él).
  - **Taxonomía v2.6** — criterio des-scoping vs aplicación (el alcance debe estar declarado EN el nodo para culpar al agente) + regla de jerarquía FP-centrales (si todos los centrales fallidos son FPs del juez, el caso no tiene primaria).
  - **Contrato `sin_par`** — `sin_defecto` deja de llevar primaria/secundaria; validador y retry lo fuerzan.
  - **Modo repeticiones+voto** (`--n K`) — K corridas independientes por namespace + voto de mayoría estricta sobre el multiconjunto de pares primarios.
- **(c)** El **dev set se amplió a 8 casos** motivado por las **FAMILIAS** que el gate #1 expuso (`provenance_imprecisa`, `estructural_kg`, `aplicacion_erronea`) — **nunca por sus casos** (los 3 casos nuevos son de run_1/run_5: off/run_1/CQ-016, on/run_5/CQ-019, off/run_1/CQ-018).
- **(d)** **Cero corridas contra casos del gate entre ambos gates.** Verificable en `data/experiment/evaluacion/cache/verificador.db`: para el graph_fingerprint de run_3 (`gfp=98d3ee73a23c214b`) existen SOLO los namespaces `cv=verificador-v1/v2/v3/v4/v5.5` — **no existen namespaces `cv=verificador-v5.6` ni `cv=verificador-v5.7` para CQs de run_3** previos a esta corrida (verificado 2026-07-15, consulta `SELECT DISTINCT namespace FROM cache WHERE namespace LIKE '%gfp=98d3ee73%'`).

## 3. Vara

`.claude/skills/kg-refinement/references/casos_control.md` en su **estado commiteado actual — INTACTO desde el commit `5bb58c0` (2026-07-13, anterior al gate #1)**; ningún commit posterior lo toca (verificado con `git log`). **Mismos patrones de acierto por caso que el gate #1** (regla 4 de la vara): CQ-020 primaria+secundaria (acierto = la primaria `{context_recall, completitud_kg}`); CQ-017 varias primarias (acierto = AMBAS: `{context_recall, estructural_kg}` y `{noise_sensitivity, provenance_imprecisa}`); CQ-025 primaria de sistema + FP del juez (acierto = `{noise_sensitivity, contenido_kg}`); CQ-031 única primaria `{context_recall, alcanzabilidad_kg}`; CQ-034 `{context_recall, completitud_kg}`. Confundir primaria con secundaria no es acierto.

## 4. Régimen de corrida y scoring

- **Régimen:** `--n 3` con voto de mayoría (el régimen de operación real del instrumento, `docs/especificacion_verificador_v57.md` §4). Comando: `python verificador.py --n 3 --casos "off/run_3/CQ-017,off/run_3/CQ-020,off/run_3/CQ-025,off/run_3/CQ-031,off/run_3/CQ-034" --out <dir del gate #2>`.
- **Scoring de TRES categorías por caso:**
  - **ACIERTO** — el voto (mayoría estricta) coincide con el patrón de acierto del caso según la vara.
  - **MISS** — mayoría en un resultado incorrecto.
  - **TRIAGE** — voto dividido (`flag_voto_dividido=true`): se reporta como **derivación a revisión humana**, no como acierto ni como miss silencioso.
- **`formato_invalido` en una repetición cuenta como repetición SIN voto** (el voto se computa sobre las repeticiones con salida válida; si con ello no hay mayoría estricta sobre el total de K=3, el caso es TRIAGE).
- El voto del protocolo se computa sobre las repeticiones VÁLIDAS (sin `formato_invalido`): mayoría estricta requiere ≥2 reps válidas coincidentes; con <2 reps válidas o sin mayoría entre ellas → TRIAGE. El campo `voto` programático del JSON es informativo; en la lectura externa prevalece esta regla.

## 5. Presupuesto estimado

5 casos × 3 repeticiones × ~400K tokens de input ≈ **6M tokens de input** (base: promedio medido por repetición ≈336.760 in en la medición N=3 de run_1/run_5, `docs/especificacion_verificador_v57.md` §4; los casos de run_3 del gate #1 promediaron ~394K in por caso — `cache/verificador.db`, namespace v5.5/gfp run_3: 1.970.688 in / 5 casos).

## 6. Registro

- **Fecha del protocolo:** 2026-07-15.
- **Instrumento:** verificador **v5.7** (congelado) — código en commits `9a2786f` (v5.7: taxonomía v2.6 + contrato `sin_par`) y `1df95d1` (modo repeticiones+voto `--n K`). Namespaces de la corrida: `cv=verificador-v5.7-rep{1,2,3}` sobre `gfp=98d3ee73a23c214b` (run_3).
- **Autora de la decisión de correr el gate #2 pre-reunión:** Agustina Videla Rivero.
