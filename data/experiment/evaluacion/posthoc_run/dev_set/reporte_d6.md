# Reporte D6 — consistencia síntoma↔atribución (compuesto v6.1-D)

Fecha: 2026-07-16. Congelados intactos (`git diff` sobre verificador.py, harness.py,
taxonomia.md, casos_control.md, casos_piloto.md, test_alcanzabilidad.py: **vacío**,
verificado). `piloto_v6/` NO se tocó (sigue con sus 10 JSONs congelados; salidas del dry-run
al scratchpad). Sin commits. La especificación no se tocó (pendiente de otra unidad).

## Entregables

- `capa_deterministica.py` (+147 líneas): `_sintoma_de_trace(trace_path)` (replica el filtro
  de `build_falla_context` — verificador.py:547, filtro en líneas 583-591, citado en el
  docstring — devolviendo F = claims reprobados con centralidad y P = patas no_cubiertas),
  `aplicar_d6(caso_json, F, P)` con la semántica pre-registrada verbatim (R6a/R6b, incluida
  la justificación por mecanismo: la severidad de la atribución no puede exceder la del
  síntoma declarado — F y P son hechos del INPUT), pipeline reordenado
  **D2 → D3 → D5 → D6 → recomputo final del voto → D4** (con `voto_pre_d6` informativo y el
  `voto` original intacto), dos motivos nuevos en D4 (R6a → `atribucion_sin_sintoma`;
  R6b claim_no_mapeado / context_recall_sin_pata → `atribucion_no_verificable`), y
  `VERSION_CAPA = "v6.1-D(2026-07)"`. CLI sin cambio de firma.
- `capa_deterministica_test.py` (+157 líneas): 9 tests nuevos de D6 + actualización de los
  helpers de pipeline (inyección de síntoma; los tests previos conservan su comportamiento
  con P no vacío).

Decisiones de implementación (en el docstring): cuando F y P están AMBOS vacíos rige R6a
sola (R6b no corre por separado); la anotación vive bajo `capa_d6` (los módulos no se
pisan); insumos por trace_path (`_sintoma_de_trace`) o inyección `sintoma_F`/`sintoma_P`.

Nota de desarrollo (documentada): tres tests nuevos fallaron en su primera corrida porque
mis quotes sintéticos no eran substring genuino de los enunciados ("el límite..." vs "Ese
límite..."); corregí los QUOTES DE LOS TESTS (no el módulo) para ejercitar el mapeo real.
Ese mismo fenómeno reaparece, ahora como hecho medido, en el dry-run (abajo).

## pytest (verde, 50/50 — todo junto: D1 a D6)

```
$ .venv/bin/python -m pytest data/experiment/evaluacion/capa_deterministica_test.py data/experiment/evaluacion/test_alcanzabilidad_test.py
collected 50 items
..........................                                               [ 86%]
data/experiment/evaluacion/test_alcanzabilidad_test.py .......           [100%]
============================== 50 passed in 0.08s ===============================
```

(50 = 43 en capa_deterministica_test — 34 previos + 9 de D6: `test_sintoma_de_trace`,
`test_d6_r6a_dispara_con_sintoma_vacio_sin_reescribir`,
`test_d6_r6a_no_dispara_con_cualquier_sintoma`,
`test_d6_r6b_degrada_mapeada_solo_a_secundario`, `test_d6_r6b_no_degrada_mapeada_a_central`,
`test_d6_r6b_claim_no_mapeado_triage_sin_degradar`, `test_d6_context_recall_intacta_con_pata`,
`test_d6_recomputo_final_degradacion_a_clave_vacia`, `test_d6_pipeline_orden_y_determinismo`
— + 7 de D1. Los 41 previos siguen verdes.)

## Dry-run — ILUSTRACIÓN CON ASTERISCO (D6 fue motivado por estos casos; NO es scoring ni re-validación)

`aplicar_capa` v6.1-D sobre los 5 JSONs congelados de `piloto_v6/` (originales del
verificador) con sus trazas; salidas al scratchpad. **Resultado: 3/5 COINCIDEN, 2/5 NO
COINCIDEN** — detalle y mecanismo por caso.

### CQ-016 — esperado: R6a dispara → triage `atribucion_sin_sintoma` sumado → **COINCIDE**

```
voto_pre_d6 : frontera_no_determinada / null      voto_capa_d : ídem (dividido)
triage final: {"triage": true, "motivos": ["atribucion_sin_sintoma", "voto_dividido"], ...}
capa_d6 rep2 atrib1 [primaria] causa=estructural_kg:  {"regla": "R6a", "accion": "atribucion_sin_sintoma"}
capa_d6 rep3 atrib1 [primaria] causa=completitud_kg:  {"regla": "R6a", "accion": "atribucion_sin_sintoma"}
```

(Las 2 reps que atribuyeron con síntoma vacío quedan marcadas; la rep exonerante no.)

### CQ-024 — esperado: R6a dispara → **COINCIDE**

```
voto_pre_d6 : mayoría {context_recall, alcanzabilidad_kg} 3-0      voto_capa_d : ídem
triage final: {"triage": true, "motivos": ["atribucion_sin_sintoma", "modulo_deterministico_sin_decision"], ...}
capa_d6 rep1 atrib1 [primaria]  alcanzabilidad_kg:  R6a atribucion_sin_sintoma
capa_d6 rep2 atrib1 [primaria]  alcanzabilidad_kg:  R6a atribucion_sin_sintoma
capa_d6 rep2 atrib2 [secundaria] alucinacion_agente: R6a atribucion_sin_sintoma
capa_d6 rep3 atrib1 [primaria]  alcanzabilidad_kg:  R6a atribucion_sin_sintoma
```

### CQ-019 — esperado: sin cambios → **COINCIDE**

```
voto_pre_d6 = voto_capa_d : mayoría clave vacía 3-0
triage final: {"triage": true, "motivos": ["exoneracion_total"], ...}   (igual que v6.0-D)
```

(F de CQ-019 no está vacío — 1 no_soportado secundario — así que R6a no rige; no hay
primarias que evaluar por R6b.)

### CQ-033 — esperado: R6b degrada las 2 primarias (mapeo al claim secundario) → voto clave vacía → **NO COINCIDE**

```
voto_pre_d6 : mayoría {noise_sensitivity, contenido_kg} 2-1      voto_capa_d : ídem (SIN degradación)
triage final: {"triage": true, "motivos": ["atribucion_no_verificable"], ...}
capa_d6 rep1 atrib1 [primaria] contenido_kg: {"regla": "R6b", "accion": "claim_no_mapeado"}
capa_d6 rep2 atrib1 [primaria] contenido_kg: {"regla": "R6b", "accion": "claim_no_mapeado"}
```

**Mecanismo (medido):** el quote de la atribución fusiona el claim central aprobado con el
reprobado — "El límite ... es del 17% del promedio de los últimos 36 meses, **vigente hasta
el 30/06/26**." — mientras el enunciado del juez es "**Ese** límite del 17% **está** vigente
hasta el 30/06/26": ninguno es substring normalizado del otro (verificado en ambas
direcciones). R6b cayó a su **fallback conservador**: sin mapeo no hay hecho que autorice
reescritura → `claim_no_mapeado` → triage `atribucion_no_verificable`, jerarquía intacta.

### CQ-018 — esperado: SIN cambios de D6 (primarias mapean al central) → **NO COINCIDE**

```
voto_pre_d6 = voto_capa_d : mayoría {noise_sensitivity, contenido_kg} 2-1
triage final: {"triage": true, "motivos": ["atribucion_no_verificable"], ...}
capa_d6 en las 4 primarias: {"regla": "R6b", "accion": "claim_no_mapeado"}
```

**Mecanismo (medido):** los quotes de las atribuciones son paráfrasis de los enunciados del
juez — "El criterio básico **utilizado** para efectuar la clasificación..." vs el enunciado
"El criterio básico **para efectuar la clasificación de deudores**..."; "El énfasis se pone
en..." vs "El énfasis **en la clasificación** se pone en..." — cero mapeos por substring en
las 16 comparaciones (verificado). Mismo fallback: `claim_no_mapeado` → triage, sin tocar
voto ni jerarquías.

### Observación factual del dry-run (sin scoring)

La expectativa del mapeo por substring falló en las dos direcciones previstas: ni degradó
CQ-033 (donde el mapeo habría autorizado degradar) ni dejó intacto CQ-018 (donde el mapeo al
central lo habría eximido). En ambos, el fallback conservador convirtió el caso en
**derivación a triage** (`atribucion_no_verificable`) sin reescribir nada — es decir, bajo
v6.1-D los dos veredictos automáticos del piloto pasarían al canal derivado, pero **por la
vía del fallback, no por la del mapeo diseñado**. El hecho medido: los quotes reales del
verificador son paráfrasis, no citas verbatim de los enunciados del juez — el mapeo por
substring es más frágil de lo pre-registrado. Queda como hecho para la lectura y la
especificación; ningún ajuste se hizo contra estos casos.

## git status (solo los 2 archivos esperados; congelados y piloto_v6/ intactos)

```
$ git status --porcelain
 M data/experiment/evaluacion/capa_deterministica.py
 M data/experiment/evaluacion/capa_deterministica_test.py

$ git diff --stat verificador.py harness.py taxonomia.md casos_control.md casos_piloto.md test_alcanzabilidad.py
(vacío — congelados intactos)

$ ls posthoc_run/piloto_v6/ | wc -l
10   (los congelados de la corrida única, sin tocar; salidas del dry-run en el scratchpad)
```

---

*Fin de D6. La especificación no se tocó. A la espera de revisión.*
