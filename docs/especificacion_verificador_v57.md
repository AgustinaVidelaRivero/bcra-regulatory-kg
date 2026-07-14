# Especificación final del verificador v5.7 (2026-07-15)

Documento de cierre del loop de calibración del verificador de atribución (Fase 2.5, Paso 3). **Todo número proviene de archivos del repo**; cada cifra cita su fuente. Fuentes usadas: `posthoc_run/dev_set/{salidas_v5,gate_v5_5,v56_run,v57_run,v57_n3}/*.json` y sus `resumen.md`, `cache/verificador.db` (todas las llamadas API reales, por namespace), `.claude/skills/kg-refinement/references/{referencias_dev_set.md,casos_control.md,taxonomia.md}`, `posthoc_run/revision_prompt_v4/tabla_v1_v4.md`, `posthoc_run/reportes_html/20260707-174942_run_3_off/meta.json`, y `git log`.

---

## 1. Historia de versiones v1 → v5.7

Bancos: v1–v4 calibraron contra los **5 casos-control de run_3** (`casos_control.md`); v5–v5.5 iteraron contra el **dev set** de run_1/run_5 (`referencias_dev_set.md`) caso por caso; v5.5 pasó el **gate #1** (los 5 run_3, una sola corrida pre-registrada); v5.6–v5.7 corrieron el **dev set ampliado (8 casos)**.

| Versión | Banco y resultado | Cambio principal | Commit donde vive |
|---|---|---|---|
| v1 | run_3 ×5: **2 aciertos / 3 errores** (sin abstención disponible; unidades de la tabla: aciertos / abstenciones válidas / errores = "2 / – / 3") — `tabla_v1_v4.md` | Primera versión (taxonomía v1, una capa) | Código no commiteado; salidas en `posthoc_run/calibracion_verificador/` [scratch]; resultados tracked en `revision_prompt_v4/tabla_v1_v4.md` (commit `8495710`) |
| v2 | run_3 ×5: **1 / 4** — `tabla_v1_v4.md` | No documentado en archivos del repo (solo salidas en `calibracion_verificador_v2/`) | Código no commiteado |
| v3 | run_3 ×5: **1 / 4** — `tabla_v1_v4.md` | No documentado en archivos del repo (solo salidas en `calibracion_verificador_v3/`) | Código no commiteado |
| v4 | run_3 ×5: **0 / 0 / 4 + 1 falla operativa** (CQ-034: JSON inválido con sustancia correcta) — `tabla_v1_v4.md` | Abstención de primera clase + anclaje textual + procedimiento en fases + esquema/juez/thinking en contexto + ejemplos resueltos (mensaje del commit) | `e35fe21` (namespace `cv=verificador-v4`, ver `reportes_html/20260707-174942_run_3_off/meta.json`) |
| v5 | dev CQ-031 (iteración 1): motivó re-adjudicación de la vara + taxonomía v2.1 (mensaje `5cbc1d7`) | Prompt ensamblado en runtime desde `taxonomia.md` (guard anti-fuga), FASE C partida C1/C2, sin confianza declarativa, validación JSON + retry + `formato_invalido`, detectores programáticos, runner `--casos` | `22beedc` |
| v5.1 | dev CQ-031 (iteración 2): **acierto pleno contra referencia** (mensaje `e2f975f`) | Taxonomía v2.1 (alcanzabilidad ex ante) + tool `ver_paso_completo` | `e2f975f` |
| v5.2 | dev CQ-017 (iteración 3) | Taxonomía C1a/C1b (síntoma por pata vs soporte por claim) | No commiteada (solo namespace `cv=verificador-v5.2` en `cache/verificador.db`) |
| v5.3 | dev CQ-017 (iteración 4) | Validador de caminos síntoma→causa (bug fix) + taxonomía v2.2 ("pertinente" = porta LA RESPUESTA) | `985d651` |
| v5.4 | dev CQ-017 (iteración 5) | Taxonomía v2.3 (soporte incluye `resumen_propiedades` expuestos) | No commiteada (solo namespace `cv=verificador-v5.4`) |
| v5.5 | dev CQ-017 convergido (iteración 6, regla de frenado) + batch final dev 5 casos + **GATE #1: 2/5 + 1 formato_invalido** (§2) | Taxonomía v2.4 (soporte vs pertinencia; verificación obligatoria de pasos truncados) | `dc5d780` |
| v5.6 | dev ampliado ×8 (`v56_run/resumen.md`): **2/8** bajo lectura estricta contra `referencias_dev_set.md` (aciertos: CQ-016 —exoneración vía sin_defecto-primaria— y on/run_1/CQ-019); motivó la v2.6 | Taxonomía v2.5 (`aplicacion_erronea` + bifurcación por pertinencia) + vía de escape a frontera en el retry | Código no commiteado como versión (namespace `cv=verificador-v5.6`; el salto v5.5→v5.7 vive en `9a2786f`) |
| v5.7 | dev ampliado ×8 (`v57_run/resumen.md`): **5/8, con 3/3 en los casos nuevos** (§2) | Taxonomía v2.6 (criterio des-scoping vs aplicación + regla de jerarquía FP-centrales) + contrato `sin_par` para `sin_defecto` | `9a2786f`; modo repeticiones+voto (`--n K`) en `1df95d1` |

## 2. Resultados finales

### 2.1 Dev set — 8 casos, v5.7 (fuentes: `v57_run/*.json` + `v57_run/resumen.md`; vara: `referencias_dev_set.md`)

Criterio de acierto (regla 3 de `referencias_dev_set.md`): primarias correctas como par `{sintoma, causa}`; en los casos de exoneración, acierto = ninguna primaria de defecto.

| Caso | v5.7 (primarias emitidas) | Vara (primarias requeridas) | Resultado |
|---|---|---|---|
| off/run_1/CQ-016 (nuevo) | ninguna (1 `sin_par` sin_defecto) | exoneración integral — ninguna primaria | **ACIERTO** |
| on/run_5/CQ-019 (nuevo) | ninguna (secundaria `{faithfulness, alucinacion_agente}` + 2 `sin_par`) | exoneración de centrales — ninguna primaria (secundaria modo b en la vara) | **ACIERTO** (secundaria coincide) |
| off/run_1/CQ-018 (nuevo) | `{noise_sensitivity, contenido_kg}` ×2 | `{noise_sensitivity, contenido_kg}` | **ACIERTO** |
| on/run_1/CQ-019 | `{noise_sensitivity, contenido_kg}` | `{noise_sensitivity, contenido_kg}` | **ACIERTO** |
| off/run_1/CQ-024 | `{noise_sensitivity, contenido_kg}` ×2 | `{noise_sensitivity, contenido_kg}` | **ACIERTO** |
| off/run_1/CQ-031 | `{context_recall, navegación}` ×2 | `{context_recall, alcanzabilidad_kg}` (patas 1 y 2) | FALLO (síntoma correcto, causa vecina) |
| off/run_5/CQ-017 | `{noise_sensitivity, aplicacion_erronea}` (+ secundaria `{noise_sensitivity, contenido_kg}`) | DOS primarias: `{context_recall, alcanzabilidad_kg}` + `{noise_sensitivity, contenido_kg}` | FALLO (parcial: detecta contenido_kg pero como secundaria; alcanzabilidad ausente) |
| off/run_1/CQ-020 | ninguna (2 `sin_par`) | `{noise_sensitivity, contenido_kg}` | FALLO (exoneración discrepante de la vara) |

**Total: 5/8 · casos nuevos de la expansión: 3/3.** (Coincide con el mensaje del commit `9a2786f`.)

### 2.2 Gate #1 — 5 casos-control run_3, v5.5, pre-registrado, UNA corrida, sin re-corrida (fuentes: `gate_v5_5/*.json`; vara: `casos_control.md`)

| Caso | v5.5 (primarias) | Vara | Resultado |
|---|---|---|---|
| off/run_3/CQ-031 | `{context_recall, alcanzabilidad_kg}` | `{context_recall, alcanzabilidad_kg}` única primaria | **ACIERTO** |
| off/run_3/CQ-034 | `{context_recall, completitud_kg}` ×2 | `{context_recall, completitud_kg}` | **ACIERTO** |
| off/run_3/CQ-020 | `{noise_sensitivity, provenance_imprecisa}` + `{faithfulness, completitud_kg}` + `{context_recall, completitud_kg}` | primaria `{context_recall, completitud_kg}` (+ secundaria no exigida) | FALLO (la primaria correcta está, pero acompañada de 2 primarias espurias — "la jerarquía importa", regla 4 de `casos_control.md`) |
| off/run_3/CQ-017 | `{context_recall, completitud_kg}` + `{faithfulness, alucinacion_agente}` | DOS primarias: `{context_recall, estructural_kg}` + `{noise_sensitivity, provenance_imprecisa}` | FALLO |
| off/run_3/CQ-025 | — (`formato_invalido: true`) | `{noise_sensitivity, contenido_kg}` | FALLA DE FORMATO (motivó taxonomía v2.5: el árbol no tenía salida para "nodo fiel mal aplicado") |

**Total gate: 2/5 + 1 formato_invalido.** El gate no se re-corrió (regla de pre-registro); v2.5–v2.6 corrigieron las causas raíz detectadas (vía de escape en retry + `aplicacion_erronea` + criterio des-scoping) y se validaron sobre el dev set, no sobre el gate.

### 2.3 Medición de varianza N=3 — v5.7, voto de mayoría (fuente: `v57_n3/resumen.md`, desgloses verbatim)

- **off/run_1/CQ-031** — voto: **frontera_no_determinada** (dividido=True, conteo=[1, 1, 1]) · desglose: rep1: {context_recall, completitud_kg} ; rep2: {context_recall, navegación} ×2 ; rep3: {context_recall, alcanzabilidad_kg} ×2 → **varianza genuina entre las tres causas vecinas de la rama context_recall; auto-flaggeada**.
- **off/run_5/CQ-017** — voto: **mayoria** (conteo=[3]) · rep1/rep2/rep3: {noise_sensitivity, contenido_kg} → **detección parcial ESTABLE** (una de las dos primarias de la vara, 3/3).
- **off/run_1/CQ-020** — voto: **mayoria** (conteo=[3], clave VACÍA) · rep1/rep2/rep3: sin primarias → **exoneración ESTABLE, discrepante de la vara** (3/3).

## 3. Hoja de especificaciones del instrumento

### Familias FIABLES (evidencia de reproducibilidad)

- **`{noise_sensitivity, contenido_kg}` por eco de nodo defectuoso / des-scoping:** 3/3 de aciertos frescos en v5.7 (CQ-018, CQ-024, on/run_1/CQ-019 — §2.1) y estabilidad 3/3 en N=3 (off/run_5/CQ-017 emite ese par en las 3 reps — §2.3).
- **Exoneración con `sin_par` (falsos positivos del juez):** CQ-016 y on/run_5/CQ-019 aciertan contra vara (§2.1) y el patrón es estable bajo repetición (off/run_1/CQ-020: 3/3 sin primarias — §2.3; la discrepancia de ESE caso con su vara es una limitación aparte, abajo).
- **`{context_recall, alcanzabilidad_kg}` sobre run_3:** acierto en el gate (CQ-031 — §2.2). Sobre run_1 la misma familia cae en la zona de varianza (§2.3, CQ-031) — fiable solo con voto.

### Zona de TRIAGE AUTOMÁTICO (flags programáticos → revisión humana)

- **`flag_voto_dividido`** (modo `--n K`): sin mayoría estricta → salida agregada `frontera_no_determinada`. Caso demostrado: off/run_1/CQ-031, conteo 1/1/1 (§2.3).
- **`flag_encuadre_invertido`**: atribución lado agente cuyo respaldo son búsquedas sin hallazgo. Disparos reales: on/run_5/CQ-019 en `v56_run/resumen.md` y `v57_run/resumen.md`.
- **`formato_invalido`**: JSON fuera de contrato tras un retry. Disparo real: gate CQ-025 (`gate_v5_5/off_run_3_CQ-025.json`).

### Limitaciones documentadas SIN auto-flag (requieren conocimiento de la vara — no autodetectables)

- **Sobredeterminación (varias primarias): detección parcial estable.** off/run_5/CQ-017 emite 3/3 la misma primaria única cuando la vara exige DOS (`referencias_dev_set.md`, caso off/run_5/CQ-017: alcanzabilidad + contenido). El voto NO lo flaggea (hay mayoría). Caso testigo con referencia.
- **Conflación sutil de labels: exoneración estable discrepante de la vara.** off/run_1/CQ-020 emite 3/3 "sin primarias" cuando la vara adjudica `{noise_sensitivity, contenido_kg}` (eco del label INC conflado, expuesto en tramo truncado del paso 1 — `referencias_dev_set.md`, caso off/run_1/CQ-020). El voto NO lo flaggea (unánime). Caso testigo con referencia.

## 4. Régimen de operación a escala recomendado

1. **`--n 3` + voto de mayoría** (implementado en `1df95d1`): la medición N=3 mostró que N=1 es indistinguible de la varianza en la zona de frontera (§2.3, CQ-031: tres respuestas distintas en tres reps).
2. **Todo flag → revisión humana:** `flag_voto_dividido`, `flag_encuadre_invertido`, `formato_invalido` derivan el caso a la cola humana, no se auto-resuelven.
3. **Presupuesto por caso medido** (fuente: suma de `_meta.tokens_in/out` de las 9 repeticiones en `v57_n3/*.json` — 3.030.842 in / 87.618 out en 3 casos):
   - por caso con `--n 3`: **≈1.010.281 tokens in / ≈29.206 tokens out** (promedio de 3 casos);
   - por repetición individual: **≈336.760 in / ≈9.735 out** (promedio de 9 reps).

## 5. Presupuesto total del loop v5.x (medido, no estimado)

Fuente primaria: `cache/verificador.db` (write-through: registra TODAS las llamadas API reales del loop, incluidas las iteraciones cuyas salidas en disco fueron sobrescritas), namespaces `cv=verificador-v5*`:

- **TOTAL v5 → v5.7 (incl. repeticiones N=3): 327 llamadas · 12.713.169 tokens de input · 378.142 tokens de output.**
- Desglose por versión (llamadas · in · out): v5: 8 · 319.093 · 7.905 — v5.1: 19 · 813.405 · 21.318 — v5.2: 9 · 377.717 · 9.616 — v5.3: 8 · 328.062 · 9.027 — v5.4: 10 · 437.444 · 11.621 — v5.5: 75 · 2.864.406 · 93.658 (incluye el gate: 49 · 1.970.688 · 59.450 bajo gfp de run_3) — v5.6: 58 · 2.068.835 · 68.117 — v5.7: 66 · 2.473.365 · 69.262 — v5.7-rep1/2/3: 74 · 3.030.842 · 87.618.
- Control de consistencia con los artefactos en disco (suma de `_meta` de los 35 JSONs existentes): 10.874.936 in / 329.558 out — menor que la caché porque `salidas_v5/` conserva solo la última iteración por caso (las corridas intermedias del loop chico fueron sobrescritas; sus tokens están solo en la caché).
- Contexto (mismas fuente y consulta, versiones previas): v1–v4 sumaron 127 llamadas · 3.703.900 in · 114.436 out. Total todas las versiones: 454 llamadas · 16.417.069 in · 492.578 out.

---

*Edición menor asociada (misma fecha): `taxonomia.md` v2.6.1 — corrección documental de la nota de "Ejemplos resueltos" (el ensamblado por referencia corta antes de las secciones de evidencia/atribución múltiple; la regla de jerarquía viaja en el bloque fijo del prompt). Durante esa corrección se detectó y evitó una fragilidad real del ensamblador: citar los marcadores de corte literalmente (con su prefijo de encabezado) en el changelog adelanta la PRIMERA ocurrencia que usa `find()` y degrada el prompt en silencio (verificado: 22.191 → 12.673 chars; corregido reformulando la cita, prompt restaurado a 22.191 y dry-run PASS).*
