# Reporte D5 — diligencia determinística de causas de ausencia (extensión de capa_deterministica.py)

Fecha: 2026-07-15. Congelados intactos (`git diff` sobre verificador.py, harness.py,
taxonomia.md, casos_control.md: **vacío**, verificado abajo). `gate2_v57/` leído solo para el
dry-run. Sin commits. No se arrancó la especificación ni la corrida consolidada.

## Entregables

- `capa_deterministica.py` (+189 líneas netas): `aplicar_d5` con la semántica pre-registrada
  verbatim en el docstring (gatillo completitud_kg/alucinacion_agente post-D2; regex cerrada
  `RE_LITERALES_D5` como constante; barrido sin provenances; filtro de exposición contra
  outputs completos; D1 sobre candidatos no expuestos; nunca cambia causas ni jerarquías;
  `capa_d5` si ya hay capa_d de otro módulo), integración a `aplicar_capa` con orden
  **D2 → D3 → D5 → D4**, y regla **R5** en D4 (`posible_portador_no_considerado`).
  `version_capa` sin cambio de string: `"v6.0-D(2026-07)"`.
- `test_alcanzabilidad.py` (único cambio permitido, +23 líneas): helper NUEVO
  `outputs_completos_de_trace(trace_path, hasta_paso=None, index=None) -> list[str]`
  (reutiliza la re-ejecución existente; devuelve los JSON serializados por paso), y
  `tokens_expuestos_de_trace` reescrita encima de él con la misma firma y semántica.
- `capa_deterministica_test.py` (+156 líneas): 9 tests nuevos de D5 + helper.

## Decisiones de implementación (documentadas en el docstring)

1. **Regla de "un solo nivel" de la extracción (c):** la regex base `\d+\.\d+(\.\d+)*` con el
   descarte de un nivel equivale a exigir **al menos dos puntos** ("1.1.2" sí; "1.1"/"3.9"
   no) — limitación documentada: referencias de dos componentes no disparan barrido.
2. **R3 vs R5:** R3 queda para los triage de módulos SIN decisión (acciones
   `sin_portador_extraible`/`quote_no_verificable` de D2/D3); el triage de D5 por banderas
   dispara **R5** (D5 con banderas SÍ decidió: encontró candidatos). D4 escanea `capa_d` y
   `capa_d5`.
3. **Insumos:** mismas dos vías que D2, con `outputs_completos` inyectable (lista de str)
   para tests sin disco; con `trace_path` sale de `outputs_completos_de_trace`.
4. Literales barridos tal como se extraen (sin canonicalizar USD/US$/u$s entre sí); blob del
   nodo = id + label + properties (claves y valores), sin provenances.
   `candidatos_evaluados` = candidatos únicos hallados; los expuestos se cuentan aparte en
   `candidatos_expuestos_descartados`.
5. El test del helper `outputs_completos_de_trace` vive en `capa_deterministica_test.py`
   (donde el punto 3 del pedido lista los tests), con traza sintética en `tmp_path`; por eso
   `test_alcanzabilidad_test.py` no cambió (dentro del conjunto de archivos permitidos).

## pytest (verde, 38/38 — D1 a D5 juntos)

```
$ .venv/bin/python -m pytest data/experiment/evaluacion/capa_deterministica_test.py data/experiment/evaluacion/test_alcanzabilidad_test.py
collected 38 items

data/experiment/evaluacion/capa_deterministica_test.py ................. [ 44%]
..............                                                           [ 81%]
data/experiment/evaluacion/test_alcanzabilidad_test.py .......           [100%]

============================== 38 passed in 0.06s ==============================
```

(31 en capa_deterministica_test — los 22 previos de D2/D3/D4/pipeline + 9 nuevos:
`test_d5_candidato_no_expuesto_alcanzable_dispara_r5`,
`test_d5_candidato_no_expuesto_inalcanzable_tambien_bandera`,
`test_d5_candidato_expuesto_sin_bandera`, `test_d5_sin_literales`,
`test_d5_causa_fuera_del_gatillo`, `test_d5_no_cambia_causa_ni_pisa_capa_d`,
`test_d5_un_nivel_no_se_extrae`, `test_d5_pipeline_completo_determinismo`,
`test_outputs_completos_de_trace_helper` — y los 7 de D1 intactos.)

## Dry-run — ASTERISCO: ilustración, no re-calibración

`aplicar_capa` (D2→D3→D5→D4) sobre los 5 casos del gate con sus trazas. Por caso: anotaciones
D5 de cada atribución gatillada y `triage_capa_d` final; expectativa → coincide/no-coincide,
y **todo hecho no anticipado**.

### CQ-034 — expectativa: gatillos completitud_kg en las 3 reps; SIN banderas → **COINCIDE (con matiz factual)**

6 atribuciones gatilladas (todas `completitud_kg`). Anotaciones D5:

```
rep1 atrib1 [primaria]: {"modulo": "D5", "literales": ["3.9.1"], "candidatos_evaluados": 0, "candidatos_expuestos_descartados": 0, "banderas": [], "triage": false}
rep1 atrib2 [primaria]: {"modulo": "D5", "literales": ["3.9.2", "3.9.1"], "candidatos_evaluados": 0, "candidatos_expuestos_descartados": 0, "banderas": [], "triage": false}
rep2 atrib1 [primaria]:  {"modulo": "D5", "accion": "sin_literales", "banderas": []}
rep2 atrib2 [secundaria]:{"modulo": "D5", "accion": "sin_literales", "banderas": []}
rep3 atrib1 [primaria]:  {"modulo": "D5", "accion": "sin_literales", "banderas": []}
rep3 atrib2 [primaria]:  {"modulo": "D5", "accion": "sin_literales", "banderas": []}
```

`triage_capa_d`: `{"triage": false, "motivos": [], "flags": []}` — sin banderas, como se
esperaba. **Matiz factual (hecho, no falla):** los literales anticipados eran tipo
"USD 200"/"3.9.1"; los realmente extraídos fueron **solo "3.9.1"/"3.9.2"**, y provienen del
campo `pata` (p. ej. "Límite general que rige para otras modalidades de formación de activos
externos (punto 3.9.1)") — los `afirmacion.quote` de las atribuciones no contienen "USD 200"
(declaran la ausencia sin montos), así que el escenario "candidato del USD 200 expuesto →
descartado" no llegó a ejercitarse: el barrido de "3.9.1"/"3.9.2" dio **0 candidatos** en los
4.050 nodos (consistente con el barrido previo del kg: "3.9" con sufijos no aparece en
id/label/properties de ningún nodo).

### CQ-017 — expectativa: gatillo en rep 2 (completitud_kg); hechos completos, sin expectativa fuerte → **COINCIDE**

```
rep2 atrib2 [primaria] causa=completitud_kg: {"modulo": "D5", "accion": "sin_literales", "banderas": []}
```

Literales extraídos: **ninguno** — el `afirmacion.quote` ("...la información disponible en el
grafo no especifica explícitamente los requisitos de autorización...") y la `pata` no
contienen montos, códigos ni puntos de dos+ niveles. `triage_capa_d` mantiene su motivo
previo: `{"triage": true, "motivos": ["exoneracion_total"], "flags": ["R1: ..."]}`. ✓

### CQ-020 — expectativa: "no emitió causas de ausencia" → **NO COINCIDE (hecho no anticipado, sin efecto)**

La expectativa pre-registrada era que CQ-020 no tuviera gatillos; **sí los tiene**: 5
atribuciones SECUNDARIAS gatilladas (1 `completitud_kg` — rep1 atrib3, las glosas A/p/PFB/CCF
— y 4 `alucinacion_agente` — el claim del 0,08 en las 3 reps y una glosa más en rep2). Las 5
dieron **`sin_literales`** ("0,08" no matchea la regex de montos —exige USD/US$— ni la de
códigos ni la de puntos):

```
rep1 atrib3 [secundaria] completitud_kg:    sin_literales
rep1 atrib4 [secundaria] alucinacion_agente: sin_literales
rep2 atrib3 [secundaria] alucinacion_agente: sin_literales
rep2 atrib4 [secundaria] alucinacion_agente: sin_literales
rep3 atrib3 [secundaria] alucinacion_agente: sin_literales
```

Sin banderas → sin R5 → `triage_capa_d` conserva exactamente sus motivos previos:
`{"triage": true, "motivos": ["aplicacion_erronea_bajo_revision", "voto_dividido"], ...}`. ✓

### CQ-025 — expectativa: post-D2 sin gatillo → **COINCIDE**

Cero atribuciones gatilladas (la primaria de rep 1 quedó en `alcanzabilidad_kg` tras D2; las
de reps 2-3 son `aplicacion_erronea`). Sin anotaciones D5. `triage_capa_d` mantiene su motivo
previo: `{"triage": true, "motivos": ["aplicacion_erronea_bajo_revision"], ...}`. ✓

### CQ-031 — expectativa: post-D2 sin gatillo → **COINCIDE en las primarias; hecho no anticipado en una secundaria**

Las 3 primarias post-D2 quedaron en `alcanzabilidad_kg` (sin gatillo), como se esperaba.
**Hecho no anticipado:** la rep 2 tiene una atribución SECUNDARIA `completitud_kg` que sí
gatilló:

```
rep2 atrib2 [secundaria] causa=completitud_kg: {"modulo": "D5", "accion": "sin_literales", "banderas": []}
```

Sin literales → sin banderas → sin efecto. `triage_capa_d`:
`{"triage": false, "motivos": [], "flags": []}` — CQ-031 sigue sin triage. ✓

### Síntesis del dry-run

| Caso | Gatillos D5 | Literales | Banderas | triage_capa_d final |
|---|---|---|---|---|
| CQ-031 | 1 (secundaria, no anticipada) | — | 0 | sin triage (igual que antes) |
| CQ-034 | 6 | "3.9.1", "3.9.2" (de `pata`) | 0 (0 candidatos) | sin triage |
| CQ-017 | 1 (rep 2) | — | 0 | exoneracion_total (igual) |
| CQ-020 | 5 (secundarias, no anticipadas) | — | 0 | R2 + R4 (igual) |
| CQ-025 | 0 | — | 0 | R2 (igual) |

Ninguna bandera en los 5 casos → R5 no disparó en ningún caso y todos los `triage_capa_d`
mantienen exactamente sus motivos previos.

## git status (solo los archivos esperados; congelados intactos)

```
$ git status --porcelain
 M data/experiment/evaluacion/capa_deterministica.py
 M data/experiment/evaluacion/capa_deterministica_test.py
 M data/experiment/evaluacion/test_alcanzabilidad.py

$ git diff --stat
 data/experiment/evaluacion/capa_deterministica.py  | 189 +++++++++++++++++++--
 .../evaluacion/capa_deterministica_test.py         | 156 ++++++++++++++++-
 data/experiment/evaluacion/test_alcanzabilidad.py  |  23 ++-
 3 files changed, 350 insertions(+), 18 deletions(-)

$ git diff --stat verificador.py harness.py taxonomia.md casos_control.md
(vacío — congelados intactos)
```

(`test_alcanzabilidad_test.py` no cambió: el test del helper vive en
`capa_deterministica_test.py`, donde el pedido lista los tests — dentro del conjunto de
archivos permitidos. Salidas del dry-run en el scratchpad de sesión, fuera del repo.)

---

*Fin de D5. No se arrancó la especificación ni la corrida consolidada. A la espera de revisión.*
