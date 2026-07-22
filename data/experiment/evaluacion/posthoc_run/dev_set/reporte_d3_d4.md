# Reporte D3+D4 — extensión de capa_deterministica.py (validador de quotes + política de triage)

Fecha: 2026-07-15. Congelados intactos (`git diff` sobre verificador.py, harness.py,
taxonomia.md, casos_control.md, test_alcanzabilidad.py y su test: **vacío**, verificado
abajo). `gate2_v57/` leído solo para los dry-runs. Sin commits. No se arrancó D5 ni la
especificación.

## Entregables

- `capa_deterministica.py` (extendido, +174 líneas): `aplicar_d3` (semántica pre-registrada
  verbatim en el docstring, con la **limitación documentada**: verifica la condición
  COMPUTABLE necesaria — el quote existe en el nodo — no la suficiente — que el quote sea
  declaración de alcance; eso es semántico y queda para el humano del triage), `aplicar_d4`
  (reglas R1-R4, motivos acumulados sin duplicados, `flags` con procedencia de cada disparo),
  `aplicar_capa` (D2 → D3 → D4, `version_capa: "v6.0-D(2026-07)"`) y CLI extendido
  (`--caso --run --trace --out` corre `aplicar_capa`).
- `capa_deterministica_test.py` (extendido, +160 líneas): 13 tests nuevos — D3 (verificable /
  no verificable / sin portador / ignora otras causas), D4 (R1, R2, R3 y R4 disparando solas;
  sin disparo → triage=false; requiere voto_capa_d; rep inválida no dispara), pipeline
  completo D2+D3+D4 y determinismo del pipeline.

Decisiones de implementación (documentadas en el docstring): el capa_d de D3 incluye además
`portador_id` (mismo criterio informativo que D2); D4 recorre solo reps VÁLIDAS (las
inválidas no votan ni disparan) y exige `voto_capa_d` presente (ValueError si falta); la
normalización de quote es lowercase + sin acentos (vía `harness._strip_accents`) + espacios
colapsados, contra el blob label + valores de properties del nodo.

## pytest (verde, 29/29 — D1+D2+D3+D4 juntos)

```
$ .venv/bin/python -m pytest data/experiment/evaluacion/capa_deterministica_test.py data/experiment/evaluacion/test_alcanzabilidad_test.py -v
collected 29 items

capa_deterministica_test.py::test_navegacion_con_portador_inalcanzable_se_corrige PASSED
capa_deterministica_test.py::test_alcanzabilidad_con_portador_alcanzable_se_corrige PASSED
capa_deterministica_test.py::test_emision_correcta_sin_discrepancia PASSED
capa_deterministica_test.py::test_sin_portador_extraible_triage_causa_intacta PASSED
capa_deterministica_test.py::test_par_fuera_de_frontera_intacto_sin_capa_d PASSED
capa_deterministica_test.py::test_recomputo_del_voto_cambia_mayoria_y_preserva_original PASSED
capa_deterministica_test.py::test_rep_invalida_no_vota_ni_se_toca PASSED
capa_deterministica_test.py::test_determinismo PASSED
capa_deterministica_test.py::test_insumos_faltantes PASSED
capa_deterministica_test.py::test_d3_quote_verificable PASSED
capa_deterministica_test.py::test_d3_quote_no_verificable PASSED
capa_deterministica_test.py::test_d3_sin_portador PASSED
capa_deterministica_test.py::test_d3_ignora_otras_causas PASSED
capa_deterministica_test.py::test_d4_r1_exoneracion_total PASSED
capa_deterministica_test.py::test_d4_r2_aplicacion_erronea_presente PASSED
capa_deterministica_test.py::test_d4_r3_propagacion PASSED
capa_deterministica_test.py::test_d4_r4_voto_dividido PASSED
capa_deterministica_test.py::test_d4_sin_disparo PASSED
capa_deterministica_test.py::test_d4_requiere_voto_capa_d PASSED
capa_deterministica_test.py::test_d4_rep_invalida_no_dispara PASSED
capa_deterministica_test.py::test_pipeline_completo_d2_d3_d4 PASSED
capa_deterministica_test.py::test_pipeline_determinismo PASSED
test_alcanzabilidad_test.py::test_alcanzable_por_label PASSED
test_alcanzabilidad_test.py::test_inalcanzable_contenido_solo_en_descripcion PASSED
test_alcanzabilidad_test.py::test_alcanzable_solo_via_token_expuesto PASSED
test_alcanzabilidad_test.py::test_token_truncado_garanti_vs_garantias PASSED
test_alcanzabilidad_test.py::test_determinismo PASSED
test_alcanzabilidad_test.py::test_stopwords_no_generan_ngramas PASSED
test_alcanzabilidad_test.py::test_portador_inexistente PASSED

============================== 29 passed in 0.04s ===============================
```

## Dry-run — ASTERISCO: ilustración, no re-calibración

`aplicar_capa` sobre los 5 casos del gate #2 con sus trazas. Por caso: expectativa
pre-registrada → **coincide/no-coincide**, con `resumen_capa_d`, `triage_capa_d` y
`voto_capa_d` pegados, más los hechos adicionales que la capa encontró.

### CQ-031 — esperado: D2 corrige 3/3 → voto alcanzabilidad_kg 3-0; sin triage → **COINCIDE**

```json
"resumen_capa_d": {"reps_tocadas": [1, 2, 3], "atribuciones_corregidas": 3, "discrepancias": 3, "triage": 0}
"triage_capa_d": {"triage": false, "motivos": [], "flags": []}
"voto_capa_d":  mayoria | dividido: False | ganadores: [["context_recall", "alcanzabilidad_kg"]] | votos: 3
```

Las 3 reps: `emision_llm: "navegación"` → `decision_codigo: "alcanzabilidad_kg"`,
`alcanzable: false`, `mejor_rank: 11` sobre 33 consultas, 0 en top-10.

### CQ-034 (control negativo) — esperado: nada dispara; sin triage → **COINCIDE**

```json
"resumen_capa_d": {"reps_tocadas": [], "atribuciones_corregidas": 0, "discrepancias": 0, "triage": 0}
"triage_capa_d": {"triage": false, "motivos": [], "flags": []}
"voto_capa_d":  mayoria | dividido: False | ganadores: [["context_recall", "completitud_kg"], ["context_recall", "completitud_kg"]] | votos: 2
```

Cero anotaciones capa_d; `voto_capa_d` reproduce el voto original.

### CQ-017 — esperado: clave ganadora vacía → triage por exoneracion_total → **COINCIDE**

```json
"resumen_capa_d": {"reps_tocadas": [2], "atribuciones_corregidas": 1, "discrepancias": 1, "triage": 0}
"triage_capa_d": {"triage": true, "motivos": ["exoneracion_total"], "flags": ["R1: voto_capa_d con mayoria de clave vacia (2 votos sin primarias)"]}
"voto_capa_d":  mayoria | dividido: False | ganadores: [] | votos: 2
```

**Hecho adicional (reportado, no estaba en la expectativa):** D2 también tocó una
**SECUNDARIA** de la rep 2 — el par `{context_recall, alcanzabilidad_kg}` sobre el portador
`Obligacion_los_sujetos_obligados_deberan_adoptar_las_acciones_necesarias_para_garantizar_de`
fue corregido a `navegación` (D1: `alcanzable=true`, mejor_rank 7, 36 consultas; llega en
top-10 p. ej. vía "punto 1.1 partes sujetos obligados operador cambio"). No cambia el voto
(la clave del voto usa solo primarias) ni el triage.

### CQ-020 — esperado: voto dividido → R4; emisiones aplicacion_erronea → R2; reportar qué encontró D3 → **COINCIDE**

```json
"resumen_capa_d": {"reps_tocadas": [], "atribuciones_corregidas": 0, "discrepancias": 0, "triage": 0}
"triage_capa_d": {"triage": true, "motivos": ["aplicacion_erronea_bajo_revision", "voto_dividido"], "flags": ["R2: rep 1 atrib 2 (primaria) causa aplicacion_erronea", "R2: rep 2 atrib 1 (primaria) causa aplicacion_erronea", "R2: rep 3 atrib 1 (primaria) causa aplicacion_erronea", "R4: voto_capa_d.flag_voto_dividido = true"]}
"voto_capa_d":  frontera_no_determinada | dividido: True | ganadores: null | votos: None
```

**Resultado D3 sobre los quotes:** las 3 emisiones `aplicacion_erronea` (una por rep, todas
sobre el portador `Obligacion_informar_exigencia_de_capitales_por_riesgo`) dieron
**`quote_verificado: true`** — el quote existe verbatim-normalizado en el contenido del nodo;
la lectura de si constituye declaración de alcance queda para el humano del triage
(limitación documentada de D3). Ningún disparo de R3.

### CQ-025 — esperado: mayoría aplicacion_erronea → R2; reportar resultado D3 → **COINCIDE**

```json
"resumen_capa_d": {"reps_tocadas": [1], "atribuciones_corregidas": 1, "discrepancias": 1, "triage": 0}
"triage_capa_d": {"triage": true, "motivos": ["aplicacion_erronea_bajo_revision"], "flags": ["R2: rep 2 atrib 1 (primaria) causa aplicacion_erronea", "R2: rep 3 atrib 1 (primaria) causa aplicacion_erronea"]}
"voto_capa_d":  mayoria | dividido: False | ganadores: [["noise_sensitivity", "aplicacion_erronea"]] | votos: 2
```

**Resultado D3 sobre los quotes:** las 2 emisiones `aplicacion_erronea` (reps 2 y 3, portador
`Obligacion_determinar_integracion_por_riesgo_de_mercado`) dieron **`quote_verificado: true`**.

**Hecho adicional (reportado, no estaba en la expectativa):** D2 corrigió la primaria de la
rep 1 — `{context_recall, navegación}` sobre el portador
`Obligacion_informar_exigencia_de_capitales_por_riesgo` pasó a **`alcanzabilidad_kg`**
(D1: `alcanzable=false`, mejor_rank 11 sobre 32 consultas, 0 en top-10: ni las consultas del
agente ni la pregunta/n-gramas de CQ-025 lo ponen en top-10). No cambia el voto (la rep 1 es
minoría 1 contra 2) ni agrega motivos de triage.

## git status (solo los 2 archivos esperados; congelados intactos)

```
$ git status --porcelain
 M data/experiment/evaluacion/capa_deterministica.py
 M data/experiment/evaluacion/capa_deterministica_test.py

$ git diff --stat
 data/experiment/evaluacion/capa_deterministica.py  | 174 ++++++++++++++++++++-
 .../evaluacion/capa_deterministica_test.py         | 160 ++++++++++++++++++-
 2 files changed, 326 insertions(+), 8 deletions(-)

$ git diff --stat verificador.py harness.py taxonomia.md casos_control.md test_alcanzabilidad.py test_alcanzabilidad_test.py
(vacío — congelados intactos)
```

(Salidas de los dry-runs en el scratchpad de sesión, fuera del repo.)

---

*Fin de D3+D4. No se arrancó D5 ni la especificación. A la espera de revisión.*
