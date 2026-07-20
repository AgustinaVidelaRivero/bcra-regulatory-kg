# Reporte D5b — patrón "coeficiente_decimal" en la regex de D5 (micro-unidad)

Fecha: 2026-07-15. Cambios SOLO en `capa_deterministica.py` y `capa_deterministica_test.py`.
Sin commits. (`test_alcanzabilidad.py` aparece modificado en git status por el helper de la
unidad D5 anterior, aún sin commitear — esta unidad NO lo tocó.)

## Qué se agregó

1. **`RE_LITERALES_D5["coeficiente_decimal"]`** = `(?<!\d)\d+,\d+(?!\d)` — decimales con COMA
   (notación normativa argentina de coeficientes y alícuotas), con guarda de límites por
   dígito adyacente para no capturar dentro de números mayores.
2. **Docstring** — motivación POR MECANISMO (no por un caso del gate): el error documentado
   de barrido léxico en la construcción de la vara — variantes "0.08"/"0,08" dieron
   ausente/presente según la grafía (`docs/evidencia_vara_v3/verificaciones_vara_v3.md` §3b)
   — es la clase de omisión que D5 existe para atajar. **Limitación simétrica documentada:**
   decimales con PUNTO ("0.08") NO se extraen — colisionan con las referencias a puntos
   normativos de un nivel ("3.9") que la extracción (c) descarta por genéricas.
3. **Orden de extracción**: "coeficiente_decimal" al final, después de los tres patrones
   existentes (determinístico).
4. **Comportamiento fijado para números con punto de miles** (documentado en docstring y
   test): la guarda es por dígito adyacente y el punto de miles no es dígito → de
   "1.100,50" se extrae el tramo decimal posterior al último punto: **"100,50"**.

## Tests nuevos (3) y pytest completo

- `test_d5_coeficiente_decimal_se_extrae` — "0,08" y "8,5" se extraen.
- `test_d5_decimal_con_punto_sigue_sin_extraerse` — "0.08"/"3.9" siguen sin extraerse.
- `test_d5_decimal_pegado_a_miles_comportamiento_fijado` — "1.100,50" → ["100,50"].

```
$ .venv/bin/python -m pytest data/experiment/evaluacion/capa_deterministica_test.py data/experiment/evaluacion/test_alcanzabilidad_test.py
collected 41 items

data/experiment/evaluacion/capa_deterministica_test.py ................. [ 41%]
.................                                                        [ 82%]
data/experiment/evaluacion/test_alcanzabilidad_test.py .......           [100%]

============================== 41 passed in 0.07s ===============================
```

(41 = 34 en capa_deterministica_test —31 previos + 3 nuevos— + 7 de D1, todos verdes.)

## Dry-run SOLO CQ-020 (aplicar_capa completa) — expectativas vs. hechos

**Expectativa: "las 5 atribuciones gatilladas ahora extraen '0,08'" → COINCIDE PARCIAL (3 de
5).** Extraen "0,08" las 3 atribuciones cuyo quote ES el claim del 0,08 (rep1 atrib4, rep2
atrib3, rep3 atrib3 — `alucinacion_agente`). Las otras 2 gatilladas siguen `sin_literales`
porque sus quotes no contienen "0,08": rep1 atrib3 (`completitud_kg`, glosas "donde A
representa activos, p los ponderadores...") y rep2 atrib4 (`alucinacion_agente`, misma glosa
A/p/PFB/CCF). Hecho, no falla: la expectativa contaba las 5 gatilladas, pero solo 3 portan el
literal.

**Expectativa: "el barrido encuentra los 4 nodos con '0,08' del kg" → COINCIDE.**
`candidatos_evaluados: 4` en las 3 atribuciones con literal.

**Expectativa: "los 2 abiertos en la trayectoria quedan descartados por exposición" →
COINCIDE Y SE EXCEDE (hecho): descartados son 3, no 2.** Además de
`Operacion_calculo_de_capital_minimo` (abierto paso 4) y
`Operacion_calculo_de_exigencia_por_riesgo` (abierto paso 6), quedó descartada por exposición
`Obligacion_determinar_exigencia_segun_formula_prescrita` — su id aparece en el output
COMPLETO del paso 8 (`ver_vecinos`, entrantes[1] `regula →`), consistente con la auditoría de
truncamiento §4a.

**Cuarto candidato (sin pre-registro — hechos):** `Operacion_calculo_de_activos_ponderados`
**NO expuesto** en ningún output completo de la trayectoria → bandera emitida:
`alcanzable: false`, `mejor_rank: 35` (ninguna de las consultas simuladas de D1 lo pone en
top-10).

### capa_d5 íntegro de una atribución del 0,08 (rep1 atrib4; rep2 atrib3 y rep3 atrib3 son idénticas)

```json
{
 "modulo": "D5",
 "literales": ["0,08"],
 "candidatos_evaluados": 4,
 "candidatos_expuestos_descartados": 3,
 "banderas": [
  {
   "literal": "0,08",
   "candidato_id": "Operacion_calculo_de_activos_ponderados",
   "alcanzable": false,
   "mejor_rank": 35,
   "expuesto": false
  }
 ],
 "triage": true
}
```

(Anotado bajo la clave `capa_d` — estas atribuciones no tenían anotación previa de D2/D3.)

### triage_capa_d final de CQ-020

**R5 se sumó a los motivos, como se anticipó posible; el agregado no cambia (ya estaba en
triage por R2+R4):**

```json
{
 "triage": true,
 "motivos": [
  "aplicacion_erronea_bajo_revision",
  "posible_portador_no_considerado",
  "voto_dividido"
 ],
 "flags": [
  "R2: rep 1 atrib 2 (primaria) causa aplicacion_erronea",
  "R5: rep 1 atrib 4 — 1 bandera(s) D5",
  "R2: rep 2 atrib 1 (primaria) causa aplicacion_erronea",
  "R5: rep 2 atrib 3 — 1 bandera(s) D5",
  "R2: rep 3 atrib 1 (primaria) causa aplicacion_erronea",
  "R5: rep 3 atrib 3 — 1 bandera(s) D5",
  "R4: voto_capa_d.flag_voto_dividido = true"
 ]
}
```

## git status

```
$ git status --porcelain
 M data/experiment/evaluacion/capa_deterministica.py
 M data/experiment/evaluacion/capa_deterministica_test.py
 M data/experiment/evaluacion/test_alcanzabilidad.py
```

Los dos primeros son esta unidad; `test_alcanzabilidad.py` es el helper de la unidad D5
anterior (sin commitear todavía) — **esta unidad no lo modificó**. Congelados intactos.

---

*Fin de D5b. Nada más arrancado. A la espera de revisión.*
