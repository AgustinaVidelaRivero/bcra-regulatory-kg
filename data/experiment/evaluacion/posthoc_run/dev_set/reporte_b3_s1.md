# B3 — Implementación de S1 (v7 = v6.1-D + S1) — reporte

Fecha: 2026-07-16. Conforme a `docs/diseno_v7_s1.md`. Sin commits. **Cero llamadas LLM
en toda la tarea** (fetch puro + tests con mock + dry-run de fetch).

## Guarda del paso 0

`docs/diseno_v7_s1.md` está commiteado en HEAD (`fbdb8db` — "diseño de v7 = v6.1-D + S1
(segunda pasada con fuentes forzadas), pre-registrado antes de implementar…"), verificado
con `git ls-tree HEAD` antes de escribir una línea de código; working tree limpio al
arrancar.

## Archivos nuevos (los únicos del working tree)

1. **`data/experiment/evaluacion/s1_fuentes.py`** — el módulo S1, con la semántica del
   diseño §2 verbatim-parafraseada en el docstring y DOS componentes separados:
   - `construir_paquete_fuentes(caso_json_capa_d, run, trace_path | sintoma_F/P)` — fetch
     determinístico puro. Gatillo: causas finales en {contenido_kg, aplicacion_erronea,
     estructural_kg, completitud_kg} en reps válidas + (exoneración con síntoma: si
     `voto_capa_d` tiene clave ganadora vacía Y el síntoma F/P de `_sintoma_de_trace` no
     está vacío, gatilla las atribuciones `sin_defecto` con tipo_gatillo
     "exoneracion_con_sintoma"). Reutiliza `_extraer_portador` y `_sintoma_de_trace` de
     capa_deterministica (imports, sin tocar el módulo). Provenance: la PRIMERA parseable
     por `pdf_locate.parse_point` (se registran índice usado y total). Comparativos por la
     regla determinística del diseño: `seccion_madre` (primer nivel del punto, existe con
     ≥2 niveles) y `punto_general_un_nivel_arriba` (mismo prefijo, un nivel arriba; existe
     como comparativo DISTINTO con ≥3 niveles — con 2 niveles coincide con la madre y se
     anota como nota mecánica). Estados explícitos: `sin_portador_extraible`,
     `provenance_no_parseable`, `localizacion_fallida`, `incompleto_localizacion`
     (portador ok pero algún comparativo fallido — lectura ESTRICTA pre-registrada: todo
     fallo de localización → triage), `completo`.
   - `aplicar_s1(caso_json, run, paquete, n=1, client=…)` — juicio LLM (implementado, NO
     ejecutado): S1_PROMPT como constante (presenta atribución emitida + nodo portador +
     pasajes fuente con sus reglas, y EXIGE el esquema del diseño §2 en JSON estricto:
     alcance_declarado_en_fuente / alcance_en_el_nodo / coinciden ∈ {si, no,
     no_determinable} / causa_confirmada_o_corregida / justificacion_breve).
     `S1_VERSION = "s1-v0.1-dev"`. Modelo: `MODEL_VERIF` importado de verificador.py
     (claude-opus-4-8). Anotación `capa_s1` por atribución (version, emision_v61d,
     salidas_s1 íntegras, voto_s1_atrib, corrigio, triage); `voto_s1` recomputado con
     `_recomputar_voto` (la regla del protocolo) sobre causas post-S1; `voto`,
     `voto_capa_d` y `voto_pre_d6` (si existe) PRESERVADOS intactos; `triage_s1` con
     motivo `fuente_no_verificable` para estados de fetch fallidos y `no_determinable`
     (incluye sin-mayoría-propia con n>1); `version_capa_s1` y `resumen_s1` en la salida.
     `--n` implementado (voto propio de S1: mayoría estricta ≥ n//2+1 sobre la causa de
     las salidas decididas) — la política de N queda para B4, como pide el diseño.
   - CLI: `python s1_fuentes.py --caso <_capa_d> --run <run> --out <_s1> [--n 1]
     [--solo-fetch] [--trace <path>]` — `--solo-fetch` corre SOLO el fetch (sin API);
     `--trace` es opcional (default: derivado de `id_falla` al layout canónico
     `traces/off/{run}/{qid}.json`, override explícito disponible).
2. **`data/experiment/evaluacion/s1_fuentes_test.py`** — 16 tests nuevos (fetch con kg
   sintético cuyas provenances apuntan al corpus REAL read-only, verificación contra
   `localize` de verdad; `aplicar_s1` con cliente MOCKEADO de respuestas inyectadas;
   determinismo del fetch por doble corrida + comparación de dumps).

**Congelados intactos:** `git diff HEAD` sobre verificador.py, harness.py,
capa_deterministica.py, test_alcanzabilidad.py, loader.py, pdf_locate.py,
verifier_pilot.py, las varas y docs/ → **vacío**. S1 solo los importa.

## pytest (verde completo, 66/66 = 50 previos + 16 nuevos)

```
$ .venv/bin/python -m pytest data/experiment/evaluacion/s1_fuentes_test.py \
    data/experiment/evaluacion/capa_deterministica_test.py \
    data/experiment/evaluacion/test_alcanzabilidad_test.py -v
============================= test session starts ==============================
platform darwin -- Python 3.10.13, pytest-9.1.1, pluggy-1.6.0 -- /Users/agustinavidelarivero/INGENIERIA IA/TESIS/bcra-regulatory-kg/.venv/bin/python
cachedir: .pytest_cache
rootdir: /Users/agustinavidelarivero/INGENIERIA IA/TESIS/bcra-regulatory-kg
plugins: anyio-4.13.0
collecting ... collected 66 items

data/experiment/evaluacion/s1_fuentes_test.py::test_fetch_portador_dos_niveles_pasaje_y_madre_contra_localize_real PASSED [  1%]
data/experiment/evaluacion/s1_fuentes_test.py::test_fetch_portador_tres_niveles_madre_y_punto_general PASSED [  3%]
data/experiment/evaluacion/s1_fuentes_test.py::test_regla_comparativos_pura PASSED [  4%]
data/experiment/evaluacion/s1_fuentes_test.py::test_fetch_provenance_no_parseable_estado_explicito PASSED [  6%]
data/experiment/evaluacion/s1_fuentes_test.py::test_fetch_sin_provenances_estado_explicito PASSED [  7%]
data/experiment/evaluacion/s1_fuentes_test.py::test_fetch_sin_portador_extraible PASSED [  9%]
data/experiment/evaluacion/s1_fuentes_test.py::test_gatillo_por_causas PASSED [ 10%]
data/experiment/evaluacion/s1_fuentes_test.py::test_gatillo_exoneracion_con_sintoma PASSED [ 12%]
data/experiment/evaluacion/s1_fuentes_test.py::test_reps_invalidas_no_gatillan PASSED [ 13%]
data/experiment/evaluacion/s1_fuentes_test.py::test_fetch_exige_voto_capa_d PASSED [ 15%]
data/experiment/evaluacion/s1_fuentes_test.py::test_aplicar_s1_corrige_y_preserva_votos PASSED [ 16%]
data/experiment/evaluacion/s1_fuentes_test.py::test_aplicar_s1_no_determinable_triage_y_causa_intacta PASSED [ 18%]
data/experiment/evaluacion/s1_fuentes_test.py::test_aplicar_s1_fetch_fallido_triage_sin_llamadas PASSED [ 19%]
data/experiment/evaluacion/s1_fuentes_test.py::test_aplicar_s1_n3_voto_propio PASSED [ 21%]
data/experiment/evaluacion/s1_fuentes_test.py::test_aplicar_s1_confirma_sin_corregir PASSED [ 22%]
data/experiment/evaluacion/s1_fuentes_test.py::test_fetch_deterministico PASSED [ 24%]
data/experiment/evaluacion/capa_deterministica_test.py::test_navegacion_con_portador_inalcanzable_se_corrige PASSED [ 25%]
data/experiment/evaluacion/capa_deterministica_test.py::test_alcanzabilidad_con_portador_alcanzable_se_corrige PASSED [ 27%]
data/experiment/evaluacion/capa_deterministica_test.py::test_emision_correcta_sin_discrepancia PASSED [ 28%]
data/experiment/evaluacion/capa_deterministica_test.py::test_sin_portador_extraible_triage_causa_intacta PASSED [ 30%]
data/experiment/evaluacion/capa_deterministica_test.py::test_par_fuera_de_frontera_intacto_sin_capa_d PASSED [ 31%]
data/experiment/evaluacion/capa_deterministica_test.py::test_recomputo_del_voto_cambia_mayoria_y_preserva_original PASSED [ 33%]
data/experiment/evaluacion/capa_deterministica_test.py::test_rep_invalida_no_vota_ni_se_toca PASSED [ 34%]
data/experiment/evaluacion/capa_deterministica_test.py::test_determinismo PASSED [ 36%]
data/experiment/evaluacion/capa_deterministica_test.py::test_insumos_faltantes PASSED [ 37%]
data/experiment/evaluacion/capa_deterministica_test.py::test_d3_quote_verificable PASSED [ 39%]
data/experiment/evaluacion/capa_deterministica_test.py::test_d3_quote_no_verificable PASSED [ 40%]
data/experiment/evaluacion/capa_deterministica_test.py::test_d3_sin_portador PASSED [ 42%]
data/experiment/evaluacion/capa_deterministica_test.py::test_d3_ignora_otras_causas PASSED [ 43%]
data/experiment/evaluacion/capa_deterministica_test.py::test_d4_r1_exoneracion_total PASSED [ 45%]
data/experiment/evaluacion/capa_deterministica_test.py::test_d4_r2_aplicacion_erronea_presente PASSED [ 46%]
data/experiment/evaluacion/capa_deterministica_test.py::test_d4_r3_propagacion PASSED [ 48%]
data/experiment/evaluacion/capa_deterministica_test.py::test_d4_r4_voto_dividido PASSED [ 50%]
data/experiment/evaluacion/capa_deterministica_test.py::test_d4_sin_disparo PASSED [ 51%]
data/experiment/evaluacion/capa_deterministica_test.py::test_d4_requiere_voto_capa_d PASSED [ 53%]
data/experiment/evaluacion/capa_deterministica_test.py::test_d4_rep_invalida_no_dispara PASSED [ 54%]
data/experiment/evaluacion/capa_deterministica_test.py::test_pipeline_completo_d2_d3_d4 PASSED [ 56%]
data/experiment/evaluacion/capa_deterministica_test.py::test_pipeline_determinismo PASSED [ 57%]
data/experiment/evaluacion/capa_deterministica_test.py::test_d5_candidato_no_expuesto_alcanzable_dispara_r5 PASSED [ 59%]
data/experiment/evaluacion/capa_deterministica_test.py::test_d5_candidato_no_expuesto_inalcanzable_tambien_bandera PASSED [ 60%]
data/experiment/evaluacion/capa_deterministica_test.py::test_d5_candidato_expuesto_sin_bandera PASSED [ 62%]
data/experiment/evaluacion/capa_deterministica_test.py::test_d5_sin_literales PASSED [ 63%]
data/experiment/evaluacion/capa_deterministica_test.py::test_d5_causa_fuera_del_gatillo PASSED [ 65%]
data/experiment/evaluacion/capa_deterministica_test.py::test_d5_no_cambia_causa_ni_pisa_capa_d PASSED [ 66%]
data/experiment/evaluacion/capa_deterministica_test.py::test_d5_un_nivel_no_se_extrae PASSED [ 68%]
data/experiment/evaluacion/capa_deterministica_test.py::test_d5_pipeline_completo_determinismo PASSED [ 69%]
data/experiment/evaluacion/capa_deterministica_test.py::test_d5_coeficiente_decimal_se_extrae PASSED [ 71%]
data/experiment/evaluacion/capa_deterministica_test.py::test_d5_decimal_con_punto_sigue_sin_extraerse PASSED [ 72%]
data/experiment/evaluacion/capa_deterministica_test.py::test_d5_decimal_pegado_a_miles_comportamiento_fijado PASSED [ 74%]
data/experiment/evaluacion/capa_deterministica_test.py::test_outputs_completos_de_trace_helper PASSED [ 75%]
data/experiment/evaluacion/capa_deterministica_test.py::test_sintoma_de_trace PASSED [ 77%]
data/experiment/evaluacion/capa_deterministica_test.py::test_d6_r6a_dispara_con_sintoma_vacio_sin_reescribir PASSED [ 78%]
data/experiment/evaluacion/capa_deterministica_test.py::test_d6_r6a_no_dispara_con_cualquier_sintoma PASSED [ 80%]
data/experiment/evaluacion/capa_deterministica_test.py::test_d6_r6b_degrada_mapeada_solo_a_secundario PASSED [ 81%]
data/experiment/evaluacion/capa_deterministica_test.py::test_d6_r6b_no_degrada_mapeada_a_central PASSED [ 83%]
data/experiment/evaluacion/capa_deterministica_test.py::test_d6_r6b_claim_no_mapeado_triage_sin_degradar PASSED [ 84%]
data/experiment/evaluacion/capa_deterministica_test.py::test_d6_context_recall_intacta_con_pata PASSED [ 86%]
data/experiment/evaluacion/capa_deterministica_test.py::test_d6_recomputo_final_degradacion_a_clave_vacia PASSED [ 87%]
data/experiment/evaluacion/capa_deterministica_test.py::test_d6_pipeline_orden_y_determinismo PASSED [ 89%]
data/experiment/evaluacion/test_alcanzabilidad_test.py::test_alcanzable_por_label PASSED [ 90%]
data/experiment/evaluacion/test_alcanzabilidad_test.py::test_inalcanzable_contenido_solo_en_descripcion PASSED [ 92%]
data/experiment/evaluacion/test_alcanzabilidad_test.py::test_alcanzable_solo_via_token_expuesto PASSED [ 93%]
data/experiment/evaluacion/test_alcanzabilidad_test.py::test_token_truncado_garanti_vs_garantias PASSED [ 95%]
data/experiment/evaluacion/test_alcanzabilidad_test.py::test_determinismo PASSED [ 96%]
data/experiment/evaluacion/test_alcanzabilidad_test.py::test_stopwords_no_generan_ngramas PASSED [ 98%]
data/experiment/evaluacion/test_alcanzabilidad_test.py::test_portador_inexistente PASSED [100%]

============================== 66 passed in 6.17s ==============================
```

Nota de desarrollo (documentada, sin tocar el módulo): la primera versión de 3 tests del
mock usaba como portador el punto 3.9.1 de Exterior; fallaron porque su sección madre "3"
da `localize` FALLIDA en el corpus real (score 4 < 6) → estado `incompleto_localizacion`,
no `completo`. Se cambió el portador de esos TESTS al 2.3.1 de Capitales (cadena 2 / 2.3 /
2.3.1 toda ok, sondeada contra el corpus); el hallazgo del 3.9.1 quedó cubierto por el
test de consistencia contra `localize` real (que acepta ambos estados según el corpus) y
alimenta el hecho (b) del dry-run.

## DRY-RUN DE FETCH — ILUSTRACIÓN (sin API; `--solo-fetch` sobre el congelado del piloto)

```
$ python3 s1_fuentes.py --caso posthoc_run/piloto_v6/off_run_3_CQ-033_capa_d.json \
    --run run_3 --out <scratchpad>/paquete_cq033.json --solo-fetch
```

**Contra la expectativa pre-registrada:**

- ✅ **El pasaje del portador ARRANCA en el encabezado de alcance:** las dos atribuciones
  `contenido_kg` gatilladas (rep1_atrib1, rep2_atrib1; la rep 3 `sin_defecto` NO gatilla —
  el voto del caso no es de clave vacía) traen el 12.3 empezando verbatim en
  "12.3. Para aquellas entidades financieras que sean reclasificadas desde el 01/01/2026…"
  (PDF pág 177), con el 17%/14% y la referencia interna al punto 7.2 dentro del pasaje.
- ❌→**HECHO (a), primer dato de diseño de B4:** la regla determinística **NO captura el
  7.3** (el comparativo semánticamente ideal). Para el punto 12.3 (2 niveles) la regla
  produce SOLO la sección madre "12" (el padre inmediato coincide con la madre, anotado);
  el 7.3 tiene OTRO prefijo (7 ≠ 12) y ninguna regla de prefijo puede alcanzarlo. La
  conexión 12.3→7.x existe en el TEXTO del pasaje ("expresión descripta en el punto 7.2")
  — no en la jerarquía de numeración. NO se "arregló": queda como hecho para B4.
- **HECHO (b), segundo dato de diseño de B4:** el comparativo `seccion_madre` "12" dio
  `localize` **FALLIDA** (mejor score=−65 < 6: el encabezado "12." de primer nivel en
  Capitales es carátula/índice sin prosa) → estado `incompleto_localizacion` → bajo la
  lectura estricta pre-registrada del diseño, estas atribuciones irían a **triage
  fuente_no_verificable en vez de ser juzgadas**. El sondeo contra el corpus (pegado abajo)
  muestra que es un patrón: los encabezados de PRIMER nivel fallan localize con frecuencia
  ("3" de Exterior score 4, "12" de Capitales −65, "4" de Capitales −99, "1"/"2"/"3"/"4"
  de Clasificación todos fallidos), mientras los de 2+ niveles suelen localizar ok.
  Dato curioso del mismo dry-run: el pasaje del 12.3 ya CONTIENE al final la carátula
  "B.C.R.A. CAPITALES MÍNIMOS … Sección 12." — el encabezado de la madre viaja dentro de
  la ventana del portador.

### Paquete ÍNTEGRO

```json
{
 "id_falla": "run_3/CQ-033",
 "run": "run_3",
 "version_s1": "s1-v0.1-dev",
 "gatillo_caso": {
  "exoneracion_con_sintoma": false,
  "sintoma_F_n": 1,
  "sintoma_P_n": 0
 },
 "atribuciones": [
  {
   "id_atribucion": "rep1_atrib1",
   "rep": 1,
   "atrib_idx": 1,
   "tipo_gatillo": "causa_gatillada",
   "sintoma_capa1": "noise_sensitivity",
   "causa_capa2": "contenido_kg",
   "jerarquia": "primaria",
   "portador_id": "Restriccion_la_exigencia_de_capital_por_riesgo_operacional_para_entidades_del_grupo_b_determ",
   "provenances_total": 1,
   "provenance": {
    "source_doc": "TO_capitales_minimos_actual.pdf",
    "location": "Punto 12.3. Para aquellas entidades financieras que sean reclasificadas desde el 01/01/2026"
   },
   "provenance_usada_idx": 0,
   "punto_parseado": "12.3",
   "pasaje_portador": {
    "source_doc": "TO_capitales_minimos_actual.pdf",
    "location_consultada": "Punto 12.3. Para aquellas entidades financieras que sean reclasificadas desde el 01/01/2026",
    "metodo": "punto",
    "ref": "Punto/Sección 12.3 (PDF pág 177)",
    "pasaje": "12.3. Para aquellas entidades financieras que sean reclasificadas desde el 01/01/2026 c omo con-\nsecuencia de lo establecido en el punto 4.1. del TO sobre Autoridades de Entidades Financie-\nras, la exigencia de capital por riesgo operacional para entidades del grupo 2 determinada a\ntravés de la aplicación de la  expresión descripta en el punto 7.2 . hasta el 30/06/26 no podrá\nsuperar:\nEl 17% en el caso de entidades del grupo B y el 14% en el caso de entidades del C –en fun-\nción de lo establecido, con vigencia hasta el 31/12/25, en la Sección 4. del TO sobre Autorida-\ndes de Entidades Financieras –, del promedio de los últimos 36 meses –anteriores al mes a\nque corresponda la determinación de la exigencia – de la exigencia de capital mínimo por ries-\ngo de crédito calculada según lo previsto en la Sección 2., expresada en moneda homogénea\ndel mes anterior al que se efectúa el cálculo.\nLos límites máximos establecidos precedentemente se reducirán a 11% y a 8%, respectiva-\nmente, cuando la entidad financiera cuente con calificación 1, 2 o 3 conforme a la valoración\notorgada por la SEFYC, en oportunidad de la úl tima inspección efectuada, respecto de todos\nlos siguientes aspectos: la entidad en su conjunto, sus sistemas informáticos y la labor de los\nresponsables de la evaluación de sus sistemas de control interno.\nB.C.R.A. CAPITALES MÍNIMOS DE LAS ENTIDADES FINANCIERAS\nSección 12.",
    "localizacion_pdf": "ok"
   },
   "comparativos": [
    {
     "tipo": "seccion_madre",
     "punto": "12",
     "regla": "encabezado de la sección madre: primer nivel del punto del portador",
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location_consultada": "Punto 12",
     "metodo": "punto",
     "ref": "Punto/Sección 12 (mejor score=-65 < 6)",
     "pasaje": null,
     "localizacion_pdf": "fallida"
    }
   ],
   "notas_regla": [
    "padre_inmediato_coincide_con_seccion_madre: el punto tiene 2 niveles; el comparativo 'un nivel arriba' es la propia sección madre (no se duplica)"
   ],
   "estado": "incompleto_localizacion"
  },
  {
   "id_atribucion": "rep2_atrib1",
   "rep": 2,
   "atrib_idx": 1,
   "tipo_gatillo": "causa_gatillada",
   "sintoma_capa1": "noise_sensitivity",
   "causa_capa2": "contenido_kg",
   "jerarquia": "primaria",
   "portador_id": "Restriccion_la_exigencia_de_capital_por_riesgo_operacional_para_entidades_del_grupo_b_determ",
   "provenances_total": 1,
   "provenance": {
    "source_doc": "TO_capitales_minimos_actual.pdf",
    "location": "Punto 12.3. Para aquellas entidades financieras que sean reclasificadas desde el 01/01/2026"
   },
   "provenance_usada_idx": 0,
   "punto_parseado": "12.3",
   "pasaje_portador": {
    "source_doc": "TO_capitales_minimos_actual.pdf",
    "location_consultada": "Punto 12.3. Para aquellas entidades financieras que sean reclasificadas desde el 01/01/2026",
    "metodo": "punto",
    "ref": "Punto/Sección 12.3 (PDF pág 177)",
    "pasaje": "12.3. Para aquellas entidades financieras que sean reclasificadas desde el 01/01/2026 c omo con-\nsecuencia de lo establecido en el punto 4.1. del TO sobre Autoridades de Entidades Financie-\nras, la exigencia de capital por riesgo operacional para entidades del grupo 2 determinada a\ntravés de la aplicación de la  expresión descripta en el punto 7.2 . hasta el 30/06/26 no podrá\nsuperar:\nEl 17% en el caso de entidades del grupo B y el 14% en el caso de entidades del C –en fun-\nción de lo establecido, con vigencia hasta el 31/12/25, en la Sección 4. del TO sobre Autorida-\ndes de Entidades Financieras –, del promedio de los últimos 36 meses –anteriores al mes a\nque corresponda la determinación de la exigencia – de la exigencia de capital mínimo por ries-\ngo de crédito calculada según lo previsto en la Sección 2., expresada en moneda homogénea\ndel mes anterior al que se efectúa el cálculo.\nLos límites máximos establecidos precedentemente se reducirán a 11% y a 8%, respectiva-\nmente, cuando la entidad financiera cuente con calificación 1, 2 o 3 conforme a la valoración\notorgada por la SEFYC, en oportunidad de la úl tima inspección efectuada, respecto de todos\nlos siguientes aspectos: la entidad en su conjunto, sus sistemas informáticos y la labor de los\nresponsables de la evaluación de sus sistemas de control interno.\nB.C.R.A. CAPITALES MÍNIMOS DE LAS ENTIDADES FINANCIERAS\nSección 12.",
    "localizacion_pdf": "ok"
   },
   "comparativos": [
    {
     "tipo": "seccion_madre",
     "punto": "12",
     "regla": "encabezado de la sección madre: primer nivel del punto del portador",
     "source_doc": "TO_capitales_minimos_actual.pdf",
     "location_consultada": "Punto 12",
     "metodo": "punto",
     "ref": "Punto/Sección 12 (mejor score=-65 < 6)",
     "pasaje": null,
     "localizacion_pdf": "fallida"
    }
   ],
   "notas_regla": [
    "padre_inmediato_coincide_con_seccion_madre: el punto tiene 2 niveles; el comparativo 'un nivel arriba' es la propia sección madre (no se duplica)"
   ],
   "estado": "incompleto_localizacion"
  }
 ]
}```

### Sondeo de localize sobre el corpus (apoyo del hecho (b); código puro, sin API)

```
EXT 3 fallida (score 4) · EXT 3.9 ok · EXT 3.9.1 ok · EXT 2 ok · EXT 2.3 ok · EXT 2.3.1 fallida
EXT 1 ok · EXT 1.1 ok · EXT 1.1.1 fallida · EXT 4 ok · EXT 4.1 ok · EXT 4.1.1 ok
CAP 3 fallida (−98) · CAP 2 ok · CAP 2.3 ok · CAP 2.3.1 ok · CAP 1 ok · CAP 1.1 ok
CAP 6 ok · CAP 6.5 ok · CAP 6.5.1 ok · CAP 4 fallida (−99) · CAP 4.1 ok · CAP 12 fallida (−65)
CLA 1/2/3/4 fallidas · CLA 1.1 ok · CLA 6 ok · CLA 6.5 ok · CLA 4.1 ok
PRO 1 ok · PRO 1.1 ok · PRO 1.1.1 ok · PRO 2 ok · PRO 2.3 ok · PRO 2.3.1 ok · PRO 3 ok · PRO 4 ok
```

## Criterios de aceptación

- **pytest verde completo:** 66/66 (pegado arriba).
- **Dry-run con el paquete íntegro:** pegado arriba, rotulado ILUSTRACIÓN, sin API.
- **git status --porcelain:**

```
?? data/experiment/evaluacion/s1_fuentes.py
?? data/experiment/evaluacion/s1_fuentes_test.py
```

- **Diff de congelados vs HEAD: VACÍO** (verificador.py, harness.py,
  capa_deterministica.py, test_alcanzabilidad.py, loader.py, pdf_locate.py,
  verifier_pilot.py, varas, docs/).
- **Cero llamadas LLM:** el modo completo del CLI existe pero no se ejecutó; los tests de
  `aplicar_s1` usan un cliente mock; el dry-run es `--solo-fetch`.

---

*Fin de B3. S1 implementado y testeado, jamás corrido con API. Los dos hechos del dry-run
((a) el comparativo ideal 7.3 está fuera del alcance de la regla de prefijos — la conexión
vive en el texto, no en la numeración; (b) la sección madre de primer nivel frecuentemente
no localiza → triage fuente_no_verificable bajo la lectura estricta) quedan como primeros
datos de diseño para B4. Frenado para revisión.*
