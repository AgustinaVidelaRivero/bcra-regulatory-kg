# Reporte D2 — capa_deterministica.py (decisor de frontera navegación/alcanzabilidad)

Fecha: 2026-07-15. Módulo NUEVO; ningún congelado tocado (`git diff` vacío, verificado
abajo). `gate2_v57/` leído SOLO para el dry-run final (sellado levantado formalmente;
veredictos como insumo de trabajo). Sin commits. No se arrancó D3 ni D4.

## Entregables

- `data/experiment/evaluacion/capa_deterministica.py` — `aplicar_d2(caso_json, run)` con la
  semántica pre-registrada verbatim en el docstring, recomputo del voto por regla del
  protocolo (`voto_capa_d`, con el `voto` original intacto), bloque `resumen_capa_d`, y CLI
  (`--caso --run --trace --out`).
- `data/experiment/evaluacion/capa_deterministica_test.py` — 9 tests pytest, sin API y sin
  disco (grafo sintético importado del test de D1 + casos_json sintéticos).

## Decisiones de implementación (documentadas también en el docstring)

1. **Insumos de D1 por dos vías excluyentes:** `trace_path` (de ahí salen pregunta, consultas
   `buscar_nodos` y tokens expuestos vía `tokens_expuestos_de_trace`) o inyección directa de
   la terna (tests sin disco). Falta de ambas → `ValueError`.
2. **"navegación" se reconoce en sus dos grafías** (con/sin acento) al detectar la frontera;
   la decisión de código se emite siempre con la grafía de la taxonomía. La comparación de
   discrepancia contempla la variante sin acento (no cuenta como discrepancia si la decisión
   coincide módulo acento).
3. **Extractor de portador literal a la regla:** substring exacto de ids del kg sobre
   `evidencia.nodo.ubicacion`, fallback `quote`; 0 o >1 ids distintos →
   `sin_portador_extraible` + triage, sin heurísticas de desempate.
4. **Clave del voto** = multiconjunto ordenado de pares primarios corregidos por rep válida
   (la misma noción de clave del voto programático del verificador); mayoría estricta ≥2;
   sin mayoría → `frontera_no_determinada` con `flag_voto_dividido=true`. Reps inválidas no
   votan ni se tocan.
5. **Cache de D1 por portador** dentro del caso (mismos insumos → mismo resultado; evita
   recomputar la simulación por rep).
6. `evidencia_d1` reducida exactamente a lo pedido: `alcanzable`, `n_consultas_simuladas`,
   `consultas_en_top10` (solo las que dan top-10, con su detalle) y `mejor_rank` (mínimo rank
   no nulo sobre todas las consultas simuladas).

## pytest (verde, 16/16 — D2 + D1 juntos)

```
$ .venv/bin/python -m pytest data/experiment/evaluacion/capa_deterministica_test.py data/experiment/evaluacion/test_alcanzabilidad_test.py -v
collected 16 items

capa_deterministica_test.py::test_navegacion_con_portador_inalcanzable_se_corrige PASSED [  6%]
capa_deterministica_test.py::test_alcanzabilidad_con_portador_alcanzable_se_corrige PASSED [ 12%]
capa_deterministica_test.py::test_emision_correcta_sin_discrepancia PASSED [ 18%]
capa_deterministica_test.py::test_sin_portador_extraible_triage_causa_intacta PASSED [ 25%]
capa_deterministica_test.py::test_par_fuera_de_frontera_intacto_sin_capa_d PASSED [ 31%]
capa_deterministica_test.py::test_recomputo_del_voto_cambia_mayoria_y_preserva_original PASSED [ 37%]
capa_deterministica_test.py::test_rep_invalida_no_vota_ni_se_toca PASSED [ 43%]
capa_deterministica_test.py::test_determinismo PASSED [ 50%]
capa_deterministica_test.py::test_insumos_faltantes PASSED [ 56%]
test_alcanzabilidad_test.py::test_alcanzable_por_label PASSED [ 62%]
test_alcanzabilidad_test.py::test_inalcanzable_contenido_solo_en_descripcion PASSED [ 68%]
test_alcanzabilidad_test.py::test_alcanzable_solo_via_token_expuesto PASSED [ 75%]
test_alcanzabilidad_test.py::test_token_truncado_garanti_vs_garantias PASSED [ 81%]
test_alcanzabilidad_test.py::test_determinismo PASSED [ 87%]
test_alcanzabilidad_test.py::test_stopwords_no_generan_ngramas PASSED [ 93%]
test_alcanzabilidad_test.py::test_portador_inexistente PASSED [100%]

============================== 16 passed in 0.03s ===============================
```

## Dry-run — ILUSTRACIÓN CON ASTERISCO, no re-calibración

**Asterisco:** la capa D fue motivada por estos mismos casos; estos dry-runs ilustran el
mecanismo sobre los JSONs reales del gate #2, no constituyen re-calibración ni scoring.

### (a) CQ-031 del gate — esperado pre-registrado: 3 reps corregidas navegación→alcanzabilidad_kg, voto_capa_d = mayoría alcanzabilidad_kg

```
$ python capa_deterministica.py --caso posthoc_run/dev_set/gate2_v57/off_run_3_CQ-031.json \
    --run run_3 --trace posthoc_run/traces/off/run_3/CQ-031.json --out <scratch>/d2_cq031.json
```

`resumen_capa_d` completo:

```json
{
 "reps_tocadas": [1, 2, 3],
 "atribuciones_corregidas": 3,
 "discrepancias": 3,
 "triage": 0
}
```

`voto_capa_d` (el `voto` original del JSON queda intacto — verificado por igualdad contra el
archivo del gate: `True`):

```json
{
 "resultado": "mayoria",
 "flag_voto_dividido": false,
 "pares_primarios_ganadores": [["context_recall", "alcanzabilidad_kg"]],
 "votos_ganadores": 3,
 "reps_validas": [1, 2, 3],
 "conteo": [
  {"pares_primarios": [["context_recall", "alcanzabilidad_kg"]], "votos": 3, "reps": [1, 2, 3]}
 ]
}
```

`capa_d` ÍNTEGRO de la rep 1 (las reps 2 y 3 son análogas — mismo portador, misma decisión):

```json
{
 "modulo": "D2",
 "portador_id": "Restriccion_los_deudores_cuyas_financiaciones_se_encuentren_cubiertas_totalmente_con_garanti",
 "emision_llm": "navegación",
 "decision_codigo": "alcanzabilidad_kg",
 "discrepancia": true,
 "alcanzable": false,
 "evidencia_d1": {
  "alcanzable": false,
  "n_consultas_simuladas": 33,
  "consultas_en_top10": [],
  "mejor_rank": 11
 }
}
```

(Nota fáctica: `mejor_rank: 11` — sobre las 33 consultas simuladas de D1, la mejor posición
del portador en el ranking completo es 11, justo afuera del top-10; ninguna consulta lo pone
en top-10 → `alcanzable=false`.)

**Resultado vs. esperado: COINCIDE** — 3/3 corregidas con `discrepancia=true`,
`voto_capa_d` = mayoría `{context_recall, alcanzabilidad_kg}` 3-0.

### (b) CQ-034 del gate (control negativo) — esperado: cero anotaciones, voto_capa_d = voto original

```
$ python capa_deterministica.py --caso posthoc_run/dev_set/gate2_v57/off_run_3_CQ-034.json \
    --run run_3 --trace posthoc_run/traces/off/run_3/CQ-034.json --out <scratch>/d2_cq034.json
```

`resumen_capa_d` completo:

```json
{
 "reps_tocadas": [],
 "atribuciones_corregidas": 0,
 "discrepancias": 0,
 "triage": 0
}
```

`voto_capa_d`:

```json
{
 "resultado": "mayoria",
 "flag_voto_dividido": false,
 "pares_primarios_ganadores": [["context_recall", "completitud_kg"], ["context_recall", "completitud_kg"]],
 "votos_ganadores": 2,
 "reps_validas": [1, 2, 3],
 "conteo": [
  {"pares_primarios": [["context_recall", "completitud_kg"], ["context_recall", "completitud_kg"]], "votos": 2, "reps": [1, 3]},
  {"pares_primarios": [["context_recall", "completitud_kg"]], "votos": 1, "reps": [2]}
 ]
}
```

**Resultado vs. esperado: COINCIDE** — ninguna atribución de CQ-034 está en la frontera
(verificado: cero claves `capa_d` en el JSON de salida), el `voto` original quedó intacto
(igualdad contra el archivo del gate: `True`) y `voto_capa_d` reproduce el mismo resultado y
la misma clave ganadora que el voto original (mayoría 2-1 con la clave duplicada
`[completitud_kg, completitud_kg]`, tal cual la emite el voto programático del gate).

## git status (solo los 2 archivos nuevos; diff vacío en todo lo demás)

```
$ git status --porcelain
?? data/experiment/evaluacion/capa_deterministica.py
?? data/experiment/evaluacion/capa_deterministica_test.py

$ git diff --stat
(vacío — ningún archivo tracked modificado)
```

(Los outputs de los dry-runs se escribieron al scratchpad de sesión, fuera del repo, para no
ensuciar el working tree; este reporte vive en `posthoc_run/dev_set/`, zona gitignored.)

---

*Fin de D2. No se arrancó D3 ni D4. A la espera de revisión.*
