# Protocolo pre-registrado — validación empírica de v6.1-D (2026-07-16)

## 1. Qué es

Validación empírica pre-registrada del **compuesto v6.1-D** (verificador v5.7 congelado +
capa determinística con D6; `docs/especificacion_capa_deterministica.md`) sobre fallas de
**run_2 y run_4** — grafos jamás usados en dev, gates ni piloto. Este protocolo se commitea
**ANTES de la adjudicación humana y de cualquier corrida**.

La métrica que motiva el ciclo: las **tasas reales del canal derivado bajo D6** — en
particular `atribucion_no_verificable`, cuya tasa quedó como **incógnita declarada** en la
especificación (los quotes del verificador resultaron paráfrasis y el mapeo de R6b cayó a su
fallback en el 100% de la ilustración del piloto) — y el **comportamiento de R6a sobre
controles negativos, esta vez por diseño** (en el piloto los controles fueron atrapados por
reglas no diseñadas para eso).

**Fuente del universo:** censo de 23 candidatos en
`docs/evidencia_validacion/censo_run2_run4.md` (criterio de capa 1 del protocolo del piloto;
23/23 con traza post-hoc; síntoma post-hoc relevado por caso).

## 2. Partición pre-registrada del material (23 candidatos del censo)

- **RESERVA INTOCABLE PARA v7 (calibración futura):** `run_2/CQ-021`, `run_4/CQ-008`,
  `run_4/CQ-021`, `run_4/CQ-028` — los **únicos candidatos cuya pregunta no fue vista en
  NINGUNA etapa previa** (sin homólogo en dev, gates ni piloto). Quedan fuera de este ciclo
  **y de cualquier uso** hasta el desarrollo de v7; la reserva es parte del pre-registro:
  el material más limpio se gasta último, en el instrumento que más lo necesita.
- **VALIDACIÓN v6.1-D: K=8**, composición fijada en §3.
- **El resto (11 casos) queda sin asignar** — utilizable a futuro solo con protocolo propio.

## 3. Selección (K=8): controles por diseño + deliberados por severidad + sorteo

**a. CONTROLES NEGATIVOS por diseño (2): `run_2/CQ-015` y `run_4/CQ-014`.** Fallas del
frozen NO reproducidas en el marco post-hoc (síntoma vacío: correcta/completa, cero claims
reprobados — censo §3). Prueban **R6a por diseño**, no por accidente como en el piloto.

**b. DELIBERADOS POR SEVERIDAD (2), criterio escrito:** incluyo el caso con **más claims
centrales reprobados** del universo post-hoc (`run_2/CQ-018`, 6 centrales) y el **único con
veredictos "falso" centrales múltiples** (`run_4/CQ-019`, 2 falso + 2 no_soportado
centrales) — cobertura de los extremos de severidad que un sorteo chico podría no capturar.
El criterio quedó fijado sobre los **METADATOS del síntoma** (los conteos del censo), sin
haber leído el contenido de los casos.

**c. SORTEO (4): estratificado 2 por run, semilla fija 20260716**, sobre el pool restante =
candidatos con síntoma post-hoc no vacío, excluidos la reserva v7, los controles y los
deliberados. Método determinístico y reproducible — código ejecutado y su output, verbatim:

```python
import random

POOL_RUN_2 = ["CQ-017", "CQ-019", "CQ-020", "CQ-024", "CQ-025", "CQ-031", "CQ-033", "CQ-034"]
POOL_RUN_4 = ["CQ-017", "CQ-018", "CQ-020", "CQ-024", "CQ-031", "CQ-033", "CQ-034"]

rng = random.Random(20260716)
sel_run_2 = rng.sample(sorted(POOL_RUN_2), 2)
sel_run_4 = rng.sample(sorted(POOL_RUN_4), 2)
print("sorteo run_2:", sel_run_2)
print("sorteo run_4:", sel_run_4)
```

```
sorteo run_2: ['CQ-025', 'CQ-019']
sorteo run_4: ['CQ-017', 'CQ-020']
```

**Selección resultante del sorteo:** `run_2/CQ-025`, `run_2/CQ-019`, `run_4/CQ-017`,
`run_4/CQ-020`. El sorteo es mecánico: no re-decidí nada.

**Los 8 de la validación, con disclosure de homólogos (del censo; otras etapas vieron la
PREGUNTA en OTRO grafo — precedente taxonómico, no evidencia del caso):**

| # | Caso | Componente | Síntoma post-hoc (censo) | Homólogos previos |
|---|---|---|---|---|
| 1 | run_2/CQ-015 | control negativo | vacío (falla frozen no reproducida) | **ninguno** |
| 2 | run_4/CQ-014 | control negativo | vacío (falla frozen no reproducida) | **ninguno** |
| 3 | run_2/CQ-018 | deliberado (severidad) | 8 reprobados, 6 centrales | dev off/run_1/CQ-018 · piloto run_3/CQ-018 |
| 4 | run_4/CQ-019 | deliberado (severidad) | 7 reprobados, 4 centrales (2 falso) | dev on/run_1/CQ-019 y on/run_5/CQ-019 · piloto run_3/CQ-019 |
| 5 | run_2/CQ-025 | sorteo | 2 reprobados (1 falso central) | gate run_3/CQ-025 (además: caso que motivó `aplicacion_erronea` v2.5 — asterisco heredado) |
| 6 | run_2/CQ-019 | sorteo | 0 reprobados; 2 patas no cubiertas | dev on/run_1/CQ-019 y on/run_5/CQ-019 · piloto run_3/CQ-019 |
| 7 | run_4/CQ-017 | sorteo | 2 reprobados (0 centrales); 1 pata no cubierta | dev off/run_5/CQ-017 · gate run_3/CQ-017 |
| 8 | run_4/CQ-020 | sorteo | 4 reprobados (3 centrales); 1 pata no cubierta | dev off/run_1/CQ-020 · gate run_3/CQ-020 |

## 4. Adjudicación humana ciega (ANTES de la corrida)

Adjudico los 8 yo, ANTES de que el compuesto corra sobre ellos — **sellado por
inexistencia**: los veredictos que podrían sesgarme no existen al momento de adjudicar.
**Marco POST-HOC** (los claims que el juez post-hoc reprobó y lo que la respuesta post-hoc
afirma — el input real del instrumento). **Circuito de la vara**: re-ejecuciones
determinísticas de outputs completos, barridos programáticos sobre cada kg congelado,
verificación contra los PDF del corpus, y D1 como instrumento de adjudicación.

**Producto:** GTs en pares `{sintoma_capa1, causa_capa2}` (taxonomía v2.6.1), con
jerarquías, patas, regla de acierto por caso y evidencia citada, en un archivo NUEVO:
`.claude/skills/kg-refinement/references/casos_validacion.md`, **commiteado antes de
correr**. Para los controles negativos: **GT = exoneración total**, con la **regla E4
heredada** del piloto: el triage por R1/R6a sobre una exoneración correcta es enrutamiento
esperado de la política conservadora, no error — su costo se mide.

## 5. Corrida — ÚNICA

- **Instrumento:** verificador v5.7 congelado, `--n 3` + voto, seguido de la capa
  determinística **v6.1-D completa** (`aplicar_capa`: D2→D3→D5→D6→recomputo→D4).
- **Guarda paso-0:** antes de ejecutar, verificar que el commit de `casos_validacion.md`
  esté en HEAD. Sin ese commit, no se corre.
- **Sin iteración:** se corre UNA vez y se lee, cualquiera sea el resultado.
- **Presupuesto:** 8 casos × 0,84-1,2M (promedio medido del piloto / estimación
  conservadora) ≈ **6,7-9,6M tokens de input**.

## 6. Scoring y métricas (pre-registradas)

- **Scoring por caso** contra `casos_validacion.md` con las reglas del gate
  (`docs/protocolo_gate2.md` §4: acierto/miss/triage, mayoría estricta ≥2 sobre reps
  válidas), sobre **`voto_capa_d` post-D6** — con el voto v5.7 original y el `voto_pre_d6`
  reportados al lado (cuánto cambia cada capa y en qué dirección).
- **Lectura por canal:** automático vs. derivado con motivo; **error grave = solo el
  veredicto automático incorrecto**; un triage se reporta como derivación.
- **Tablero completo por motivo R1-R6 con TASAS**: n/8 por caso y por atribución
  (discrepancias D2, quotes D3, banderas D5, R6a, R6b-fallback).
- **Métrica principal:** acuerdo compuesto-humano sobre los 8.
- **Métricas declaradas de lectura:**
  - **tasa de `atribucion_no_verificable`** — si domina el canal derivado, el mapeo de R6b
    se rediseña **por mecanismo** (nunca contra estos casos);
  - **comportamiento de R6a en los 2 controles** (¿derivan por diseño?);
  - **costo de política**: revisiones humanas pagadas por veredictos correctos (métrica E4).

## 7. Regla de frenado

Corrida única; **los 8 quedan QUEMADOS al correr**; ningún módulo de la capa ni prompt del
verificador se ajusta contra ellos; los hallazgos van al documento de lectura de la
validación, que se publica con este protocolo citado. La reserva v7 (§2) permanece intocable
independientemente del resultado.
