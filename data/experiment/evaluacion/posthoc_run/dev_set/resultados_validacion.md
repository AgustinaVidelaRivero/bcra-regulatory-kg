# Resultados de la validación v6.1-D — reporte de EXTRACCIÓN (sin scoring)

Fecha: 2026-07-16. **Corrida ÚNICA** del compuesto v6.1-D bajo
`docs/protocolo_validacion_v61.md` (§5: se corre una vez y se lee). **Este reporte NO
scorea**: no compara contra la vara de la validación ni menciona sus GTs — el scoring es
adjudicación externa. Los 16 JSONs (8 originales + 8 `_capa_d`) quedan **congelados** en
`posthoc_run/validacion_v61/`.

## 1. Constancia de la guarda (PASO 0), comandos y costo real

**Guarda — PASA:**

```
$ git log --oneline -1 -- .claude/skills/kg-refinement/references/casos_validacion.md
94b3487 vara de la validación v1 (casos_validacion.md, marco post-hoc, taxonomía v2.6.1) — adjudicada ANTES de cualquier corrida (sellado por inexistencia): [...] Habilita la corrida única del compuesto v6.1-D (guarda del protocolo).

$ git log --oneline -1
94b3487 [...]        <- el commit de casos_validacion.md ES HEAD

$ git status
nothing to commit, working tree clean
```

**PASO 1 — comando (verificador v5.7 congelado):**

```
$ cd data/experiment/evaluacion
$ python verificador.py --n 3 \
    --casos "off/run_2/CQ-015,off/run_2/CQ-018,off/run_2/CQ-019,off/run_2/CQ-025,off/run_4/CQ-014,off/run_4/CQ-017,off/run_4/CQ-019,off/run_4/CQ-020" \
    --out posthoc_run/validacion_v61/
```

Votos emitidos (log del runner; **8/8 casos, 24/24 reps válidas, cero fallas operativas** —
cero 429/timeouts/formato_invalido; exit 0):

```
[runner]   → off_run_2_CQ-015.json · voto=mayoria · dividido=False · ganadores=[] · conteo=[2, 1]
[runner]   → off_run_2_CQ-018.json · voto=mayoria · dividido=False · ganadores=[['noise_sensitivity', 'contenido_kg']] · conteo=[2, 1]
[runner]   → off_run_2_CQ-019.json · voto=mayoria · dividido=False · ganadores=[['context_recall', 'navegación'], ['context_recall', 'navegación']] · conteo=[2, 1]
[runner]   → off_run_2_CQ-025.json · voto=mayoria · dividido=False · ganadores=[['context_recall', 'navegación']] · conteo=[3]
[runner]   → off_run_4_CQ-014.json · voto=mayoria · dividido=False · ganadores=[] · conteo=[3]
[runner]   → off_run_4_CQ-017.json · voto=mayoria · dividido=False · ganadores=[['context_recall', 'estructural_kg']] · conteo=[2, 1]
[runner]   → off_run_4_CQ-019.json · voto=mayoria · dividido=False · ganadores=[['context_recall', 'navegación'], ['context_recall', 'navegación']] · conteo=[2, 1]
[runner]   → off_run_4_CQ-020.json · voto=mayoria · dividido=False · ganadores=[] · conteo=[2, 1]
```

**PASO 2 — capa v6.1-D completa sobre cada JSON:**

```
$ python capa_deterministica.py --caso posthoc_run/validacion_v61/off_<run>_<CQ>.json --run <run> \
    --trace posthoc_run/traces/off/<run>/<CQ>.json --out ..._capa_d.json
8/8 exit 0 · version_capa verificada en las 8 salidas: v6.1-D(2026-07)
```

Nota operativa (registro honesto): el primer intento del loop del PASO 2 falló en los 8
casos por word-splitting del shell (los parámetros run/CQ no se separaron; ningún archivo
llegó a escribirse con contenido válido); se re-ejecutó el loop corregido con los mismos
comandos unitarios — no es re-corrida del instrumento (la capa es determinística y pura) ni
hubo llamada alguna a la API en el PASO 2.

**Costo real medido (suma de `detectores.tokens_in/out` de las 24 reps):**

| Caso | Tokens in | Tokens out |
|---|---|---|
| run_2/CQ-015 | 261.089 | 12.621 |
| run_2/CQ-018 | 885.646 | 31.062 |
| run_2/CQ-019 | 771.888 | 27.759 |
| run_2/CQ-025 | 770.956 | 23.144 |
| run_4/CQ-014 | 253.095 | 12.113 |
| run_4/CQ-017 | 981.684 | 28.274 |
| run_4/CQ-019 | 1.123.319 | 29.985 |
| run_4/CQ-020 | 849.035 | 22.308 |
| **TOTAL** | **5.896.712** | **187.266** |

(5,90M de input, dentro del rango pre-registrado 6,7-9,6M — por debajo del piso estimado:
los dos controles negativos costaron ~0,26M cada uno.)

## 2. Extracción por caso (verbatim; sin scoring)

Nota de lectura: las `atribuciones` pegadas por rep son las del JSON `_capa_d` — ÍNTEGRAS,
con las anotaciones `capa_d` (D2), `capa_d5` (D5) y `capa_d6` (D6); donde D2 corrigió o D6
degradó, la emisión original del LLM queda en `emision_llm`. `formato_invalido`,
`errores_formato` y `detectores` son del JSON original.

---

## run_2/CQ-015 (`validacion_v61/off_run_2_CQ-015.json` + `_capa_d.json`)

**Voto v5.7 original (verbatim):**

```json
{
 "resultado": "mayoria",
 "flag_voto_dividido": false,
 "pares_primarios_ganadores": [],
 "votos_ganadores": 2,
 "conteo": [
  {
   "pares_primarios": [],
   "votos": 2
  },
  {
   "pares_primarios": [
    [
     "noise_sensitivity",
     "provenance_imprecisa"
    ]
   ],
   "votos": 1
  }
 ],
 "desglose": [
  {
   "rep": 1,
   "pares_primarios": [],
   "formato_invalido": false
  },
  {
   "rep": 2,
   "pares_primarios": [
    [
     "noise_sensitivity",
     "provenance_imprecisa"
    ]
   ],
   "formato_invalido": false
  },
  {
   "rep": 3,
   "pares_primarios": [],
   "formato_invalido": false
  }
 ]
}
```

**voto_pre_d6:**

```json
{
 "resultado": "mayoria",
 "flag_voto_dividido": false,
 "pares_primarios_ganadores": [],
 "votos_ganadores": 2,
 "reps_validas": [
  1,
  2,
  3
 ],
 "conteo": [
  {
   "pares_primarios": [],
   "votos": 2,
   "reps": [
    1,
    3
   ]
  },
  {
   "pares_primarios": [
    [
     "noise_sensitivity",
     "provenance_imprecisa"
    ]
   ],
   "votos": 1,
   "reps": [
    2
   ]
  }
 ]
}
```

**voto_capa_d (final, post-D6):**

```json
{
 "resultado": "mayoria",
 "flag_voto_dividido": false,
 "pares_primarios_ganadores": [],
 "votos_ganadores": 2,
 "reps_validas": [
  1,
  2,
  3
 ],
 "conteo": [
  {
   "pares_primarios": [],
   "votos": 2,
   "reps": [
    1,
    3
   ]
  },
  {
   "pares_primarios": [
    [
     "noise_sensitivity",
     "provenance_imprecisa"
    ]
   ],
   "votos": 1,
   "reps": [
    2
   ]
  }
 ]
}
```

**resumen_capa_d:** `{"reps_tocadas": [], "atribuciones_corregidas": 0, "discrepancias": 0, "triage": 0}`

**triage_capa_d (motivos y flags completos):**

```json
{
 "triage": true,
 "motivos": [
  "exoneracion_total",
  "atribucion_sin_sintoma"
 ],
 "flags": [
  "R1: voto_capa_d con mayoria de clave vacia (2 votos sin primarias)",
  "R6a: rep 1 atrib 2 — atribución con síntoma vacío",
  "R6a: rep 2 atrib 1 — atribución con síntoma vacío",
  "R6a: rep 3 atrib 2 — atribución con síntoma vacío"
 ]
}
```

### Rep 1

- `formato_invalido`: `false` · `errores_formato`: `[]`
- `detectores`: `{"flag_encuadre_invertido": false, "flag_contexto": false, "tool_calls_usadas": 3, "max_tool_calls": 40, "tokens_in": 52527, "tokens_out": 3535}`
- longitudes: `razonamiento` = 1564 chars · `extraccion_traza` = 1713 chars

`atribuciones` ÍNTEGRAS (post-capa, con `capa_d`/`capa_d5`/`capa_d6`; la emisión original del LLM queda en los campos `emision_llm` donde la capa corrigió/degradó):

```json
[
 {
  "sintoma_capa1": "noise_sensitivity",
  "causa_capa2": "sin_defecto",
  "lado": "ninguno",
  "jerarquia": "sin_par",
  "pata": "Definición de 'residente' del país para una persona humana a los fines cambiarios",
  "evidencia": {
   "afirmacion": {
    "quote": "A los fines cambiarios, una persona humana se define como 'residente' del país cuando tiene su centro de interés económico o actividad principal dentro del país, o cuando tiene la intención de permanecer en el país por al menos un año.",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "Persona humana con centro de interés económico o actividad principal dentro de un país, o con intención de permanecer por al menos un año.",
    "ubicacion": "concepto_definido:residente_persona_humana (abierto por el agente en paso 3)"
   },
   "fuente": {
    "quote": "6.5.1. Persona humana. Se considerará que una persona humana es residente del país dentro de cuya frontera tiene su centro de interés económico o actividad principal. En tal sentido, deberá presumirse que una persona humana es residente de un país si permanece o tiene intención de permanecer en él por al menos un año.",
    "ubicacion": "TO_exterior_cambios_actual.pdf, Punto 6.5.1"
   }
  },
  "busquedas": [
   {
    "consulta": "Punto 6.5 (PDF)",
    "resultado": "El pasaje 6.5.1 confirma las tres condiciones exactamente como las afirmó el agente"
   },
   {
    "consulta": "Punto 6.4 (PDF, la provenance del nodo)",
    "resultado": "El 6.4 es 'Operaciones a término', NO contiene la definición de residente"
   }
  ]
 },
 {
  "sintoma_capa1": "noise_sensitivity",
  "causa_capa2": "provenance_imprecisa",
  "lado": "grafo",
  "jerarquia": "secundaria",
  "pata": "Definición de 'residente' del país para una persona humana a los fines cambiarios",
  "evidencia": {
   "afirmacion": {
    "quote": "TO_exterior_cambios_actual.pdf :: Sección 5 > Punto 6.4",
    "ubicacion": "respuesta final (citas)"
   },
   "nodo": {
    "quote": "\"provenances\": [{\"source_doc\": \"TO_exterior_cambios_actual.pdf\", \"location\": \"Sección 5 > Punto 6.4\"}]",
    "ubicacion": "concepto_definido:residente_persona_humana"
   },
   "fuente": {
    "quote": "6.4. Operaciones a término. Comprende las operaciones en las cuales la liquidación está pactada en un plazo mayor a los 2 (dos) días hábiles desde la fecha de su concertación.",
    "ubicacion": "TO_exterior_cambios_actual.pdf, Punto 6.4"
   }
  },
  "busquedas": [
   {
    "consulta": "leer_pasaje_pdf Sección 5 > Punto 6.4",
    "resultado": "El punto 6.4 trata 'Operaciones a término', no la definición de residente; la definición está en 6.5.1"
   },
   {
    "consulta": "leer_pasaje_pdf Punto 6.5",
    "resultado": "6.5.1 Persona humana contiene la definición real de residente"
   }
  ],
  "capa_d6": {
   "regla": "R6a",
   "accion": "atribucion_sin_sintoma"
  }
 }
]
```

### Rep 2

- `formato_invalido`: `false` · `errores_formato`: `[]`
- `detectores`: `{"flag_encuadre_invertido": false, "flag_contexto": false, "tool_calls_usadas": 9, "max_tool_calls": 40, "tokens_in": 136867, "tokens_out": 5321}`
- longitudes: `razonamiento` = 1561 chars · `extraccion_traza` = 1757 chars

`atribuciones` ÍNTEGRAS (post-capa, con `capa_d`/`capa_d5`/`capa_d6`; la emisión original del LLM queda en los campos `emision_llm` donde la capa corrigió/degradó):

```json
[
 {
  "sintoma_capa1": "noise_sensitivity",
  "causa_capa2": "provenance_imprecisa",
  "lado": "grafo",
  "jerarquia": "primaria",
  "pata": "Definición de 'residente' del país para una persona humana a los fines cambiarios",
  "evidencia": {
   "afirmacion": {
    "quote": "A los fines cambiarios, una persona humana se define como 'residente' del país cuando tiene su centro de interés económico o actividad principal dentro del país, o cuando tiene la intención de permanecer en el país por al menos un año.\ncitas: TO_exterior_cambios_actual.pdf :: Sección 5 > Punto 6.4",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "\"description\": \"Persona humana con centro de interés económico o actividad principal dentro de un país, o con intención de permanecer por al menos un año.\" (...) \"provenances\": [{\"source_doc\": \"TO_exterior_cambios_actual.pdf\", \"location\": \"Sección 5 > Punto 6.4\"}]",
    "ubicacion": "concepto_definido:residente_persona_humana (abierto por el agente, paso 3)"
   },
   "fuente": {
    "quote": "6.4. Operaciones a término. Comprende las operaciones en las cuales la liquidación está pactada en un plazo mayor a los 2 (dos) días hábiles (...) 6.5. Residente. 6.5.1. Persona humana. Se considerará que una persona humana es residente del país dentro de cuya frontera tiene su centro de interés económico o actividad principal. En tal sentido, deberá presumirse que una persona humana es residente de un país si permanece o tiene intención de permanecer en él por al menos un año. (...) B.C.R.A. EXTERIOR Y CAMBIOS Sección 6. Definiciones.",
    "ubicacion": "TO_exterior_cambios_actual.pdf, Punto 6.5 (PDF pág 76)"
   }
  },
  "busquedas": [
   {
    "consulta": "leer_pasaje_pdf location 'Sección 5 > Punto 6.4'",
    "resultado": "El Punto 6.4 es 'Operaciones a término', ajeno a la definición de residente; la definición de persona humana residente está en el Punto 6.5.1, dentro de la Sección 6 ('Sección 6. Definiciones.')"
   },
   {
    "consulta": "leer_pasaje_pdf location 'Punto 6.5'",
    "resultado": "Confirma 6.5.1 Persona humana con la definición exacta; footer 'Sección 6. Definiciones.' — la cita del nodo (Sección 5, Punto 6.4) no corresponde"
   },
   {
    "consulta": "leer_pasaje_pdf location 'Sección 5'",
    "resultado": "localizacion_pdf=fallida — la sección citada no ancla; la definición no está en la Sección 5"
   }
  ],
  "capa_d6": {
   "regla": "R6a",
   "accion": "atribucion_sin_sintoma"
  }
 }
]
```

### Rep 3

- `formato_invalido`: `false` · `errores_formato`: `[]`
- `detectores`: `{"flag_encuadre_invertido": false, "flag_contexto": false, "tool_calls_usadas": 4, "max_tool_calls": 40, "tokens_in": 71695, "tokens_out": 3765}`
- longitudes: `razonamiento` = 1643 chars · `extraccion_traza` = 1653 chars

`atribuciones` ÍNTEGRAS (post-capa, con `capa_d`/`capa_d5`/`capa_d6`; la emisión original del LLM queda en los campos `emision_llm` donde la capa corrigió/degradó):

```json
[
 {
  "sintoma_capa1": "noise_sensitivity",
  "causa_capa2": "sin_defecto",
  "lado": "ninguno",
  "jerarquia": "sin_par",
  "pata": "Definición de 'residente' del país para una persona humana a los fines cambiarios",
  "evidencia": {
   "afirmacion": {
    "quote": "A los fines cambiarios, una persona humana se define como 'residente' del país cuando tiene su centro de interés económico o actividad principal dentro del país, o cuando tiene la intención de permanecer en el país por al menos un año.",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "Persona humana con centro de interés económico o actividad principal dentro de un país, o con intención de permanecer por al menos un año.",
    "ubicacion": "concepto_definido:residente_persona_humana"
   },
   "fuente": {
    "quote": "6.5.1. Persona humana. Se considerará que una persona humana es residente del país dentro de cuya frontera tiene su centro de interés económico o actividad principal. En tal sentido, deberá presumirse que una persona humana es residente de un país si permanece o tiene intención de permanecer en él por al menos un año.",
    "ubicacion": "TO_exterior_cambios_actual.pdf, Punto 6.5.1"
   }
  },
  "busquedas": [
   {
    "consulta": "residente fines cambiarios definición",
    "resultado": "nodos de residente/no residente varios"
   },
   {
    "consulta": "persona humana residente país",
    "resultado": "devuelve concepto_definido:residente_persona_humana con la definición exacta"
   }
  ]
 },
 {
  "sintoma_capa1": "noise_sensitivity",
  "causa_capa2": "provenance_imprecisa",
  "lado": "grafo",
  "jerarquia": "secundaria",
  "pata": "Definición de 'residente' del país para una persona humana a los fines cambiarios",
  "evidencia": {
   "afirmacion": {
    "quote": "citas: TO_exterior_cambios_actual.pdf :: Sección 5 > Punto 6.4",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "\"provenances\": [{\"source_doc\": \"TO_exterior_cambios_actual.pdf\", \"location\": \"Sección 5 > Punto 6.4\"}]",
    "ubicacion": "concepto_definido:residente_persona_humana"
   },
   "fuente": {
    "quote": "6.4. Operaciones a término. Comprende las operaciones en las cuales la liquidación está pactada en un plazo mayor a los 2 (dos) días hábiles... 6.5. Residente. 6.5.1. Persona humana. Se considerará que una persona humana es residente del país...",
    "ubicacion": "TO_exterior_cambios_actual.pdf, Punto 6.4 vs 6.5.1"
   }
  },
  "busquedas": [
   {
    "consulta": "leer_pasaje_pdf Sección 5 > Punto 6.4",
    "resultado": "El Punto 6.4 es 'Operaciones a término'; la definición de residente persona humana está en el Punto 6.5.1, no en el 6.4 que cita el nodo"
   }
  ],
  "capa_d6": {
   "regla": "R6a",
   "accion": "atribucion_sin_sintoma"
  }
 }
]
```

**Tokens del caso (suma detectores 3 reps): in=261,089 · out=12,621**


---

## run_2/CQ-018 (`validacion_v61/off_run_2_CQ-018.json` + `_capa_d.json`)

**Voto v5.7 original (verbatim):**

```json
{
 "resultado": "mayoria",
 "flag_voto_dividido": false,
 "pares_primarios_ganadores": [
  [
   "noise_sensitivity",
   "contenido_kg"
  ]
 ],
 "votos_ganadores": 2,
 "conteo": [
  {
   "pares_primarios": [
    [
     "noise_sensitivity",
     "contenido_kg"
    ]
   ],
   "votos": 2
  },
  {
   "pares_primarios": [
    [
     "noise_sensitivity",
     "contenido_kg"
    ],
    [
     "noise_sensitivity",
     "provenance_imprecisa"
    ],
    [
     "noise_sensitivity",
     "provenance_imprecisa"
    ]
   ],
   "votos": 1
  }
 ],
 "desglose": [
  {
   "rep": 1,
   "pares_primarios": [
    [
     "noise_sensitivity",
     "contenido_kg"
    ],
    [
     "noise_sensitivity",
     "provenance_imprecisa"
    ],
    [
     "noise_sensitivity",
     "provenance_imprecisa"
    ]
   ],
   "formato_invalido": false
  },
  {
   "rep": 2,
   "pares_primarios": [
    [
     "noise_sensitivity",
     "contenido_kg"
    ]
   ],
   "formato_invalido": false
  },
  {
   "rep": 3,
   "pares_primarios": [
    [
     "noise_sensitivity",
     "contenido_kg"
    ]
   ],
   "formato_invalido": false
  }
 ]
}
```

**voto_pre_d6:**

```json
{
 "resultado": "mayoria",
 "flag_voto_dividido": false,
 "pares_primarios_ganadores": [
  [
   "noise_sensitivity",
   "contenido_kg"
  ]
 ],
 "votos_ganadores": 2,
 "reps_validas": [
  1,
  2,
  3
 ],
 "conteo": [
  {
   "pares_primarios": [
    [
     "noise_sensitivity",
     "contenido_kg"
    ]
   ],
   "votos": 2,
   "reps": [
    2,
    3
   ]
  },
  {
   "pares_primarios": [
    [
     "noise_sensitivity",
     "contenido_kg"
    ],
    [
     "noise_sensitivity",
     "provenance_imprecisa"
    ],
    [
     "noise_sensitivity",
     "provenance_imprecisa"
    ]
   ],
   "votos": 1,
   "reps": [
    1
   ]
  }
 ]
}
```

**voto_capa_d (final, post-D6):**

```json
{
 "resultado": "mayoria",
 "flag_voto_dividido": false,
 "pares_primarios_ganadores": [
  [
   "noise_sensitivity",
   "contenido_kg"
  ]
 ],
 "votos_ganadores": 2,
 "reps_validas": [
  1,
  2,
  3
 ],
 "conteo": [
  {
   "pares_primarios": [
    [
     "noise_sensitivity",
     "contenido_kg"
    ]
   ],
   "votos": 2,
   "reps": [
    2,
    3
   ]
  },
  {
   "pares_primarios": [
    [
     "noise_sensitivity",
     "contenido_kg"
    ],
    [
     "noise_sensitivity",
     "provenance_imprecisa"
    ],
    [
     "noise_sensitivity",
     "provenance_imprecisa"
    ]
   ],
   "votos": 1,
   "reps": [
    1
   ]
  }
 ]
}
```

**resumen_capa_d:** `{"reps_tocadas": [], "atribuciones_corregidas": 0, "discrepancias": 0, "triage": 0}`

**triage_capa_d (motivos y flags completos):**

```json
{
 "triage": true,
 "motivos": [
  "atribucion_no_verificable"
 ],
 "flags": [
  "R6b: rep 1 atrib 4 — claim_no_mapeado",
  "R6b: rep 2 atrib 1 — claim_no_mapeado",
  "R6b: rep 3 atrib 1 — claim_no_mapeado"
 ]
}
```

### Rep 1

- `formato_invalido`: `false` · `errores_formato`: `[]`
- `detectores`: `{"flag_encuadre_invertido": false, "flag_contexto": false, "tool_calls_usadas": 14, "max_tool_calls": 40, "tokens_in": 189488, "tokens_out": 9881}`
- longitudes: `razonamiento` = 2973 chars · `extraccion_traza` = 4021 chars

`atribuciones` ÍNTEGRAS (post-capa, con `capa_d`/`capa_d5`/`capa_d6`; la emisión original del LLM queda en los campos `emision_llm` donde la capa corrigió/degradó):

```json
[
 {
  "sintoma_capa1": "noise_sensitivity",
  "causa_capa2": "contenido_kg",
  "lado": "grafo",
  "jerarquia": "primaria",
  "pata": "Bajo qué criterio clasifican sus deudores",
  "evidencia": {
   "afirmacion": {
    "quote": "El criterio básico de clasificación de deudores es la capacidad de pago en el futuro de la deuda o de los compromisos objeto de la garantía, medida a través del análisis de flujo de fondos.",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "[\"Criterio básico de clasificación: la capacidad de pago en el futuro de la deuda o de los compromisos objeto de la garantía.\", \"Capacidad del cliente para atender el pago de capital e intereses en las condiciones pactadas, medida a través del análisis de flujo de fondos.\"]",
    "ubicacion": "concepto_definido:capacidad_de_pago (paso 12)"
   },
   "fuente": {
    "quote": "5.1. En situación normal. El análisis del flujo de fondos del cliente demuestra que es capaz de atender adecuadamente todos sus compromisos financieros. (…) CLASIFICACIÓN DE DEUDORES B.C.R.A. Sección 6. Clasificación de los deudores de la cartera comercial.",
    "ubicacion": "TO_clasificacion_deudores_actual.pdf, Sección 6 > Punto 5.1"
   }
  },
  "busquedas": [
   {
    "consulta": "leer_pasaje Sección 6 > Punto 5.1",
    "resultado": "El criterio de flujo de fondos pertenece a la Sección 6 'Clasificación de los deudores de la cartera comercial' — es el criterio de cartera comercial de entidades financieras, no de los proveedores no financieros"
   },
   {
    "consulta": "ver_nodo obligacion:clasificar_deudores_segun_mora_en_cartera_consumo_vivienda",
    "resultado": "Para proveedores no financieros el criterio real es la MORA en cartera consumo/vivienda, no el análisis de flujo de fondos"
   }
  ]
 },
 {
  "sintoma_capa1": "noise_sensitivity",
  "causa_capa2": "contenido_kg",
  "lado": "grafo",
  "jerarquia": "secundaria",
  "pata": "Bajo qué criterio clasifican sus deudores",
  "evidencia": {
   "afirmacion": {
    "quote": "criterios objetivos que incluyen el término de morosidad, la situación jurídica del cliente o sus deudas, y el cumplimiento de refinanciaciones",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "Criterios establecidos en la norma para clasificar deudores, incluyendo término de morosidad, situación jurídica del cliente o sus deudas, cumplimiento de refinanciaciones.",
    "ubicacion": "concepto_definido:criterios_objetivos_de_clasificacion (paso 11)"
   },
   "fuente": {
    "quote": "6.4.1. Modificación de alguno de los criterios objetivos de clasificación que surjan de estas normas (término de morosidad, situación jurídica del cliente o de sus deudas, cumplimiento de refinanciaciones y pedidos de refinanciaciones de obligaciones). (…) Sección 6. Clasificación de los deudores de la cartera comercial.",
    "ubicacion": "TO_clasificacion_deudores_actual.pdf, Sección 6 > Punto 6.4"
   }
  },
  "busquedas": [
   {
    "consulta": "leer_pasaje Sección 6 > Punto 6.4",
    "resultado": "El nodo es FIEL al texto, pero el texto es de la Sección 6 (cartera comercial de entidades financieras); el nodo omite en su contenido/label la marca de alcance, por lo que se aplicó fuera del alcance de los sujetos de la pregunta"
   }
  ]
 },
 {
  "sintoma_capa1": "noise_sensitivity",
  "causa_capa2": "provenance_imprecisa",
  "lado": "grafo",
  "jerarquia": "primaria",
  "pata": "Si los proveedores no financieros de crédito / empresas de tarjetas deben cumplir con Protección al Usuario (resolver reclamos)",
  "evidencia": {
   "afirmacion": {
    "quote": "considerar y resolver fundadamente reclamos de usuarios",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "Los sujetos obligados deben considerar y resolver fundadamente los reclamos de usuarios relacionados con los servicios que ofrecen, contemplando los derechos básicos y las normas aplicables.",
    "ubicacion": "obligacion:considerar_y_resolver_fundadamente_reclamos_de_usuarios (provenance Sección 5 > Punto 1.1)"
   },
   "fuente": {
    "quote": "1.1. Partes. 1.1.1. Usuario de servicios financieros. (…) 1.1.2. Sujetos obligados. 1.1.2.1. Entidades financieras. 1.1.2.2. Operadores de cambio",
    "ubicacion": "TO_proteccion_usuarios_servicios_financieros_actual.pdf, Sección 5 > Punto 1.1"
   }
  },
  "busquedas": [
   {
    "consulta": "leer_pasaje Sección 5 > Punto 1.1",
    "resultado": "El punto 1.1 citado por el nodo/edge es 'Partes / Sujetos obligados' — solo lista sujetos, NO funda la obligación de resolver reclamos"
   },
   {
    "consulta": "leer_pasaje Sección 3 (protección)",
    "resultado": "El contenido real sobre recepción y resolución de reclamos está en Sección 3 > Punto 3.1.6 ('Toda consulta o reclamo deberá ser definitivamente resuelta dentro de 10 días hábiles'), no en el punto citado"
   }
  ]
 },
 {
  "sintoma_capa1": "noise_sensitivity",
  "causa_capa2": "provenance_imprecisa",
  "lado": "grafo",
  "jerarquia": "primaria",
  "pata": "Si las empresas no financieras emisoras de tarjetas deben cumplir con Protección al Usuario (entregar información y publicar contratos)",
  "evidencia": {
   "afirmacion": {
    "quote": "entrega de información sobre productos y servicios, publicación de contratos",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "Deber de publicar modelos de contrato de adhesión bajo el nombre 'Contratos de adhesión – Ley 24.240 de Defensa del Consumidor', discriminando por cada modalidad, plan, producto o servicio.",
    "ubicacion": "obligacion:publicar_contratos_de_adhesion_en_sitio_de_internet_institucional (provenance Sección 2 > Punto 2.4)"
   },
   "fuente": {
    "quote": "2.4. Disposiciones generales. (…) 4.1. La accesibilidad a los puntos de atención al usuario (casas operativas y cajeros automáticos) deberá respetar características apropiadas para cada uno de estos grupos poblacionales (…) eliminación de escalones (…) instalación de rampas",
    "ubicacion": "TO_proteccion_usuarios_servicios_financieros_actual.pdf, Sección 2 > Punto 2.4"
   }
  },
  "busquedas": [
   {
    "consulta": "leer_pasaje Sección 2 > Punto 2.4",
    "resultado": "El punto 2.4 citado por los edges/nodos es sobre accesibilidad física de puntos de atención — NO funda ni 'entregar detalle de productos' ni 'publicar contratos de adhesión'; la cita apunta a otro contenido"
   }
  ],
  "capa_d6": {
   "regla": "R6b",
   "accion": "claim_no_mapeado"
  }
 }
]
```

### Rep 2

- `formato_invalido`: `false` · `errores_formato`: `[]`
- `detectores`: `{"flag_encuadre_invertido": false, "flag_contexto": false, "tool_calls_usadas": 16, "max_tool_calls": 40, "tokens_in": 279475, "tokens_out": 9944}`
- longitudes: `razonamiento` = 3133 chars · `extraccion_traza` = 4202 chars

`atribuciones` ÍNTEGRAS (post-capa, con `capa_d`/`capa_d5`/`capa_d6`; la emisión original del LLM queda en los campos `emision_llm` donde la capa corrigió/degradó):

```json
[
 {
  "sintoma_capa1": "noise_sensitivity",
  "causa_capa2": "contenido_kg",
  "lado": "grafo",
  "jerarquia": "primaria",
  "pata": "Bajo qué criterio clasifican sus deudores",
  "evidencia": {
   "afirmacion": {
    "quote": "el criterio básico: la capacidad de pago en el futuro de la deuda o de los compromisos objeto de la garantía, medida a través del análisis de flujo de fondos), y (2) criterios objetivos que incluyen el término de morosidad, la situación jurídica del cliente o sus deudas, y el cumplimiento de refinanciaciones",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "Criterio básico de clasificación: la capacidad de pago en el futuro de la deuda o de los compromisos objeto de la garantía. Capacidad del cliente para atender el pago de capital e intereses en las condiciones pactadas, medida a través del análisis de flujo de fondos.",
    "ubicacion": "concepto_definido:capacidad_de_pago (label genérico, sin marca de alcance cartera comercial); concepto_definido:criterios_objetivos_de_clasificacion ('Criterios establecidos en la norma para clasificar deudores, incluyendo término de morosidad, situación jurídica del cliente o sus deudas, cumplimiento de refinanciaciones')"
   },
   "fuente": {
    "quote": "5.1. En situación normal. El análisis del flujo de fondos del cliente demuestra que es capaz de atender adecuadamente todos sus compromisos financieros. (...) CLASIFICACIÓN DE DEUDORES B.C.R.A. Sección 6. Clasificación de los deudores de la cartera comercial.",
    "ubicacion": "TO_clasificacion_deudores_actual.pdf, Sección 6 > Punto 5.1 y Punto 6.4"
   }
  },
  "busquedas": [
   {
    "consulta": "criterio clasificación cartera consumo vivienda mora",
    "resultado": "obligacion:clasificar_deudores_segun_mora_en_cartera_consumo_vivienda ('Proveedores no financieros deben clasificar deudores en función de su mora aplicando criterios de cartera consumo o vivienda') y concepto_definido:cartera_de_consumo_o_vivienda ('sujeta a normas especiales de clasificación según mora')"
   },
   {
    "consulta": "cartera consumo cumplimiento normal atraso 31 90 dias situacion",
    "resultado": "umbrales de atraso (31 días, 31-90, 90-180) como criterio objetivo de clasificación de cartera consumo/vivienda — confirma que el criterio de esa cartera es la MORA, no el flujo de fondos"
   }
  ],
  "capa_d6": {
   "regla": "R6b",
   "accion": "claim_no_mapeado"
  }
 },
 {
  "sintoma_capa1": "noise_sensitivity",
  "causa_capa2": "sin_defecto",
  "lado": "ninguno",
  "jerarquia": "sin_par",
  "pata": "Si los proveedores no financieros de crédito deben cumplir con Protección al Usuario / Si las empresas no financieras emisoras de tarjetas deben cumplir con Protección al Usuario",
  "evidencia": {
   "afirmacion": {
    "quote": "considerar y resolver fundadamente reclamos de usuarios (...) Las empresas no financieras emisoras de tarjetas de crédito (...) deben cumplir con obligaciones de Protección al Usuario (cumplimiento de normas de protección, resolución de reclamos, entrega de información sobre productos y servicios, publicación de contratos, etc.)",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "Los sujetos obligados deben considerar y resolver fundadamente los reclamos de usuarios relacionados con los servicios que ofrecen, contemplando los derechos básicos y las normas aplicables.",
    "ubicacion": "obligacion:considerar_y_resolver_fundadamente_reclamos_de_usuarios; edges obligado_a hacia reclamos, entregar_detalle_de_caracteristicas_de_productos_y_servicios y publicar_contratos_de_adhesion, vistos en pasos 7 y 8"
   },
   "fuente": {
    "quote": "Toda consulta o reclamo deberá ser definitivamente resuelta/o dentro del plazo máximo de diez (10) días hábiles",
    "ubicacion": "TO_proteccion_usuarios_servicios_financieros_actual.pdf, Sección 3 > Sección 3 — preámbulo (punto 3.1.6 Recepción de presentaciones y tiempo de respuestas)"
   }
  },
  "busquedas": [
   {
    "consulta": "resolver reclamos usuarios plazo respuesta",
    "resultado": "obligacion:considerar_y_resolver_fundadamente_reclamos_de_usuarios y obligacion:resolver_consulta_o_reclamo_en_plazo_maximo ('Toda consulta o reclamo debe ser definitivamente resuelta dentro del plazo máximo de diez días hábiles') — el dato es fáctico y correcto"
   }
  ]
 },
 {
  "sintoma_capa1": "noise_sensitivity",
  "causa_capa2": "provenance_imprecisa",
  "lado": "grafo",
  "jerarquia": "secundaria",
  "pata": "Si las empresas no financieras emisoras de tarjetas deben cumplir con Protección al Usuario (reclamos / información / contratos)",
  "evidencia": {
   "afirmacion": {
    "quote": "considerar y resolver fundadamente reclamos de usuarios (...) entrega de información sobre productos y servicios, publicación de contratos",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "considerar y resolver fundadamente reclamos de usuarios — provenance: Sección 5 > Punto 1.1; entregar detalle de características de productos y servicios / publicar contratos de adhesión — provenance: Sección 2 > Punto 2.4",
    "ubicacion": "obligacion:considerar_y_resolver_fundadamente_reclamos_de_usuarios; edges hacia entregar_detalle_de_caracteristicas y publicar_contratos_de_adhesion"
   },
   "fuente": {
    "quote": "1.1. Partes. 1.1.1. Usuario de servicios financieros. (...) 1.1.2. Sujetos obligados. — [no menciona resolución de reclamos]; Sección 2 > Punto 2.4: '2.4. Disposiciones generales. (...) La accesibilidad a los puntos de atención al usuario (...)' — [no menciona entrega de información de productos ni publicación de contratos]",
    "ubicacion": "TO_proteccion_usuarios_servicios_financieros_actual.pdf, Sección 5 > Punto 1.1 y Sección 2 > Punto 2.4"
   }
  },
  "busquedas": [
   {
    "consulta": "resolver reclamos usuarios plazo respuesta",
    "resultado": "el contenido de reclamos está realmente en Sección 3 preámbulo (punto 3.1.6), no en Sección 5>1.1 que cita el nodo; confirma que la cita apunta a otra sección"
   }
  ]
 }
]
```

### Rep 3

- `formato_invalido`: `false` · `errores_formato`: `[]`
- `detectores`: `{"flag_encuadre_invertido": false, "flag_contexto": false, "tool_calls_usadas": 19, "max_tool_calls": 40, "tokens_in": 416683, "tokens_out": 11237}`
- longitudes: `razonamiento` = 2552 chars · `extraccion_traza` = 3714 chars

`atribuciones` ÍNTEGRAS (post-capa, con `capa_d`/`capa_d5`/`capa_d6`; la emisión original del LLM queda en los campos `emision_llm` donde la capa corrigió/degradó):

```json
[
 {
  "sintoma_capa1": "noise_sensitivity",
  "causa_capa2": "contenido_kg",
  "lado": "grafo",
  "jerarquia": "primaria",
  "pata": "Bajo qué criterio clasifican sus deudores",
  "evidencia": {
   "afirmacion": {
    "quote": "el criterio básico: la capacidad de pago en el futuro de la deuda o de los compromisos objeto de la garantía, medida a través del análisis de flujo de fondos",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "[\"Criterio básico de clasificación: la capacidad de pago en el futuro de la deuda o de los compromisos objeto de la garantía.\", \"Capacidad del cliente para atender el pago de capital e intereses en las condiciones pactadas, medida a través del análisis de flujo de fondos.\"]",
    "ubicacion": "concepto_definido:capacidad_de_pago"
   },
   "fuente": {
    "quote": "7.1. Criterio de clasificación. (...) la clasificación de estos clientes se efectuará considerando -al cabo de cada mes- exclusivamente pautas objetivas vinculadas al grado de cumplimiento de las correspondientes obligaciones o su situación jurídica",
    "ubicacion": "TO_clasificacion_deudores_actual.pdf, Punto 7.1"
   }
  },
  "busquedas": [
   {
    "consulta": "mora cartera consumo vivienda clasificación deudores criterio",
    "resultado": "obligacion:clasificar_deudores_segun_mora_en_cartera_consumo_vivienda: 'Proveedores no financieros deben clasificar deudores en función de su mora aplicando criterios de cartera consumo o vivienda' — el criterio pertinente a proveedores es MORA, no capacidad de pago"
   },
   {
    "consulta": "leer_pasaje Punto 7.1 clasificacion deudores",
    "resultado": "para cartera consumo/vivienda la clasificación es exclusivamente por pautas objetivas (mora/situación jurídica), no por capacidad de pago/flujo de fondos"
   }
  ],
  "capa_d6": {
   "regla": "R6b",
   "accion": "claim_no_mapeado"
  }
 },
 {
  "sintoma_capa1": "noise_sensitivity",
  "causa_capa2": "sin_defecto",
  "lado": "ninguno",
  "jerarquia": "sin_par",
  "pata": "Si los proveedores/tarjetas deben cumplir con Protección al Usuario — resolver reclamos y criterios objetivos",
  "evidencia": {
   "afirmacion": {
    "quote": "Los criterios objetivos de clasificación de deudores incluyen el término de morosidad (...) la situación jurídica del cliente o sus deudas (...) el cumplimiento de refinanciaciones.",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "Criterios establecidos en la norma para clasificar deudores, incluyendo término de morosidad, situación jurídica del cliente o sus deudas, cumplimiento de refinanciaciones.",
    "ubicacion": "concepto_definido:criterios_objetivos_de_clasificacion"
   },
   "fuente": {
    "quote": "6.4.1. Modificación de alguno de los criterios objetivos de clasificación que surjan de estas normas (término de morosidad, situación jurídica del cliente o de sus deudas, cumplimiento de refinanciaciones y pedidos de refinanciaciones de obligaciones).",
    "ubicacion": "TO_clasificacion_deudores_actual.pdf, Punto 6.4"
   }
  },
  "busquedas": [
   {
    "consulta": "leer_pasaje Sección 6 Punto 6.4",
    "resultado": "el PDF confirma verbatim los tres criterios objetivos que el juez marcó no_soportado — están soportados por nodo consultado y son fieles"
   },
   {
    "consulta": "ver_nodo obligacion:considerar_y_resolver_fundadamente_reclamos_de_usuarios",
    "resultado": "obligación genérica de sujetos obligados; edge sale de empresas_tarjetas y de proveedores en la trayectoria (pasos 7 y 8) — claim soportado y correcto"
   }
  ]
 },
 {
  "sintoma_capa1": "noise_sensitivity",
  "causa_capa2": "provenance_imprecisa",
  "lado": "grafo",
  "jerarquia": "secundaria",
  "pata": "Si las empresas no financieras emisoras de tarjetas deben cumplir con Protección al Usuario — entregar información / publicar contratos",
  "evidencia": {
   "afirmacion": {
    "quote": "entrega de información sobre productos y servicios, publicación de contratos",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "empresas no financieras emisoras de tarjetas de crédito —obligado_a→ publicar contratos de adhesión en sitio de Internet institucional [provenance Sección 2 > Punto 2.4]",
    "ubicacion": "EDGE::...--obligado_a-->obligacion:publicar_contratos_de_adhesion_en_sitio_de_internet_institucional"
   },
   "fuente": {
    "quote": "2.4. Disposiciones generales. 2.4.1. La accesibilidad a los puntos de atención al usuario (casas operativas y cajeros automáticos) deberá respetar características apropiadas (...) eliminación de escalones, desniveles (...)",
    "ubicacion": "TO_proteccion_usuarios_servicios_financieros_actual.pdf, Sección 2 > Punto 2.4"
   }
  },
  "busquedas": [
   {
    "consulta": "leer_pasaje Sección 2 Punto 2.4 protección usuarios",
    "resultado": "el Punto 2.4 trata sobre accesibilidad física, NO sobre publicar contratos ni entregar detalle de productos — la provenance del edge no funda su contenido"
   },
   {
    "consulta": "ver_paso_completo 8",
    "resultado": "edges de tarjetas hacia entregar detalle / publicar contratos existen con provenance Sección 2 Punto 2.4"
   }
  ]
 }
]
```

**Tokens del caso (suma detectores 3 reps): in=885,646 · out=31,062**


---

## run_2/CQ-019 (`validacion_v61/off_run_2_CQ-019.json` + `_capa_d.json`)

**Voto v5.7 original (verbatim):**

```json
{
 "resultado": "mayoria",
 "flag_voto_dividido": false,
 "pares_primarios_ganadores": [
  [
   "context_recall",
   "navegación"
  ],
  [
   "context_recall",
   "navegación"
  ]
 ],
 "votos_ganadores": 2,
 "conteo": [
  {
   "pares_primarios": [
    [
     "context_recall",
     "navegación"
    ],
    [
     "context_recall",
     "navegación"
    ]
   ],
   "votos": 2
  },
  {
   "pares_primarios": [
    [
     "faithfulness",
     "alucinacion_agente"
    ],
    [
     "faithfulness",
     "alucinacion_agente"
    ]
   ],
   "votos": 1
  }
 ],
 "desglose": [
  {
   "rep": 1,
   "pares_primarios": [
    [
     "faithfulness",
     "alucinacion_agente"
    ],
    [
     "faithfulness",
     "alucinacion_agente"
    ]
   ],
   "formato_invalido": false
  },
  {
   "rep": 2,
   "pares_primarios": [
    [
     "context_recall",
     "navegación"
    ],
    [
     "context_recall",
     "navegación"
    ]
   ],
   "formato_invalido": false
  },
  {
   "rep": 3,
   "pares_primarios": [
    [
     "context_recall",
     "navegación"
    ],
    [
     "context_recall",
     "navegación"
    ]
   ],
   "formato_invalido": false
  }
 ]
}
```

**voto_pre_d6:**

```json
{
 "resultado": "mayoria",
 "flag_voto_dividido": false,
 "pares_primarios_ganadores": [
  [
   "context_recall",
   "navegación"
  ],
  [
   "context_recall",
   "navegación"
  ]
 ],
 "votos_ganadores": 2,
 "reps_validas": [
  1,
  2,
  3
 ],
 "conteo": [
  {
   "pares_primarios": [
    [
     "context_recall",
     "navegación"
    ],
    [
     "context_recall",
     "navegación"
    ]
   ],
   "votos": 2,
   "reps": [
    2,
    3
   ]
  },
  {
   "pares_primarios": [
    [
     "faithfulness",
     "alucinacion_agente"
    ],
    [
     "faithfulness",
     "alucinacion_agente"
    ]
   ],
   "votos": 1,
   "reps": [
    1
   ]
  }
 ]
}
```

**voto_capa_d (final, post-D6):**

```json
{
 "resultado": "mayoria",
 "flag_voto_dividido": false,
 "pares_primarios_ganadores": [
  [
   "context_recall",
   "navegación"
  ],
  [
   "context_recall",
   "navegación"
  ]
 ],
 "votos_ganadores": 2,
 "reps_validas": [
  1,
  2,
  3
 ],
 "conteo": [
  {
   "pares_primarios": [
    [
     "context_recall",
     "navegación"
    ],
    [
     "context_recall",
     "navegación"
    ]
   ],
   "votos": 2,
   "reps": [
    2,
    3
   ]
  },
  {
   "pares_primarios": [
    [
     "faithfulness",
     "alucinacion_agente"
    ],
    [
     "faithfulness",
     "alucinacion_agente"
    ]
   ],
   "votos": 1,
   "reps": [
    1
   ]
  }
 ]
}
```

**resumen_capa_d:** `{"reps_tocadas": [2, 3], "atribuciones_corregidas": 1, "discrepancias": 0, "triage": 3}`

**triage_capa_d (motivos y flags completos):**

```json
{
 "triage": true,
 "motivos": [
  "atribucion_no_verificable",
  "modulo_deterministico_sin_decision"
 ],
 "flags": [
  "R6b: rep 1 atrib 1 — claim_no_mapeado",
  "R6b: rep 1 atrib 2 — claim_no_mapeado",
  "R3: rep 2 atrib 1 — D2/sin_portador_extraible",
  "R3: rep 3 atrib 1 — D2/sin_portador_extraible",
  "R3: rep 3 atrib 2 — D2/sin_portador_extraible"
 ]
}
```

### Rep 1

- `formato_invalido`: `false` · `errores_formato`: `[]`
- `detectores`: `{"flag_encuadre_invertido": false, "flag_contexto": false, "tool_calls_usadas": 10, "max_tool_calls": 40, "tokens_in": 248193, "tokens_out": 12691}`
- longitudes: `razonamiento` = 2467 chars · `extraccion_traza` = 4066 chars

`atribuciones` ÍNTEGRAS (post-capa, con `capa_d`/`capa_d5`/`capa_d6`; la emisión original del LLM queda en los campos `emision_llm` donde la capa corrigió/degradó):

```json
[
 {
  "sintoma_capa1": "faithfulness",
  "causa_capa2": "alucinacion_agente",
  "lado": "agente",
  "jerarquia": "primaria",
  "pata": "Qué previsión por incobrabilidad no se deduce al computar los activos para la exigencia de capital por riesgo de crédito",
  "evidencia": {
   "afirmacion": {
    "quote": "No se encontró en el Knowledge Graph información específica sobre qué previsión por incobrabilidad no se deduce al computar los activos para la exigencia de capital por riesgo de crédito, ni cómo se vincula esa regla con la clasificación de deudores. El grafo contiene referencias a previsión contable, previsión regulatoria y previsión por riesgo de incobrabilidad, pero no especifica cuál se excluye del cálculo de activos ni su relación con la clasificación de deudores.",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "\"Deducción contable para riesgos de incobrabilidad, incluyendo previsiones en pasivo, aplicable a deudores en situación normal y financiaciones con garantías preferidas.\"",
    "ubicacion": "concepto_definido:prevision_por_riesgo_de_incobrabilidad (abierto por el agente en paso 5)"
   },
   "fuente": {
    "quote": "netos de las previsiones por riesgos de incobrabilidad –incluyendo, de corresponder, las previsiones contabilizadas en el pasivo– y desvalorización (…) sin deducir el 100% del importe de la previsión por riesgo de incobrabilidad correspondiente a la cartera de deudores clasificados “en situación normal” –puntos 6.5.1. y 7.2.1. del TO sobre Clasificación de Deudores– y a las financiaciones que se encuentran cubiertas con garantías preferidas A).",
    "ubicacion": "TO_capitales_minimos_actual.pdf, Punto 2.3.1"
   }
  },
  "busquedas": [
   {
    "consulta": "ver_nodo concepto_definido:prevision_por_riesgo_de_incobrabilidad",
    "resultado": "El nodo porta el dato pertinente: previsión de deudores en situación normal y garantías preferidas; provenance dual a capitales mínimos (2.3) y clasificación de deudores (10.4). El agente lo abrió en el paso 5."
   },
   {
    "consulta": "leer_pasaje_pdf TO_capitales_minimos_actual.pdf Punto 2.3",
    "resultado": "Confirma que la previsión que no se deduce (100%) es la de deudores 'en situación normal' + garantías preferidas A, con remisión a puntos 6.5.1 y 7.2.1 del TO Clasificación de Deudores."
   }
  ],
  "capa_d": {
   "modulo": "D5",
   "accion": "sin_literales",
   "banderas": []
  },
  "capa_d6": {
   "regla": "R6b",
   "accion": "claim_no_mapeado"
  }
 },
 {
  "sintoma_capa1": "faithfulness",
  "causa_capa2": "alucinacion_agente",
  "lado": "agente",
  "jerarquia": "primaria",
  "pata": "Cómo se vincula esa regla con la clasificación de deudores",
  "evidencia": {
   "afirmacion": {
    "quote": "No se encontró en el Knowledge Graph información sobre cómo se vincula esa regla con la clasificación de deudores.",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "Norma externa que define situaciones de deudores y disposiciones sobre clasificación, referenciada en puntos 6.5.1 y 7.2.1.",
    "ubicacion": "norma_referenciada:texto_ordenado_sobre_clasificacion_de_deudores (expuesto en paso 3); y concepto_definido:prevision_por_riesgo_de_incobrabilidad con provenance a TO_clasificacion_deudores_actual.pdf Sección 10 > Punto 10.4 /a (abierto en paso 5)"
   },
   "fuente": {
    "quote": "sin deducir el 100% del importe de la previsión por riesgo de incobrabilidad correspondiente a la cartera de deudores clasificados “en situación normal” –puntos 6.5.1. y 7.2.1. del TO sobre Clasificación de Deudores– y a las financiaciones que se encuentran cubiertas con garantías preferidas A).",
    "ubicacion": "TO_capitales_minimos_actual.pdf, Punto 2.3.1"
   }
  },
  "busquedas": [
   {
    "consulta": "ver_paso_completo paso 3",
    "resultado": "El agente vio 'Texto Ordenado sobre Clasificación de Deudores... referenciada en puntos 6.5.1 y 7.2.1' — exactamente los puntos que el PDF vincula con la regla de no deducción."
   },
   {
    "consulta": "ver_vecinos concepto_definido:prevision_por_riesgo_de_incobrabilidad",
    "resultado": "El nodo conecta con conceptos_comprendidos (Punto 2.3) y su provenance dual liga capitales mínimos con TO clasificación de deudores; el vínculo estaba disponible y alcanzable."
   }
  ],
  "capa_d": {
   "modulo": "D5",
   "accion": "sin_literales",
   "banderas": []
  },
  "capa_d6": {
   "regla": "R6b",
   "accion": "claim_no_mapeado"
  }
 }
]
```

### Rep 2

- `formato_invalido`: `false` · `errores_formato`: `[]`
- `detectores`: `{"flag_encuadre_invertido": false, "flag_contexto": false, "tool_calls_usadas": 14, "max_tool_calls": 40, "tokens_in": 323618, "tokens_out": 8257}`
- longitudes: `razonamiento` = 2415 chars · `extraccion_traza` = 4037 chars

`atribuciones` ÍNTEGRAS (post-capa, con `capa_d`/`capa_d5`/`capa_d6`; la emisión original del LLM queda en los campos `emision_llm` donde la capa corrigió/degradó):

```json
[
 {
  "sintoma_capa1": "context_recall",
  "causa_capa2": "navegación",
  "lado": "agente",
  "jerarquia": "primaria",
  "pata": "Qué previsión por incobrabilidad no se deduce al computar los activos para la exigencia de capital por riesgo de crédito",
  "evidencia": {
   "afirmacion": {
    "quote": "No se encontró en el Knowledge Graph información específica sobre qué previsión por incobrabilidad no se deduce al computar los activos para la exigencia de capital por riesgo de crédito",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "Clasificación de deudor según normativa de clasificación de deudores del BCRA, cuya cartera no será deducida al 100% de la previsión por riesgo de incobrabilidad.",
    "ubicacion": "concepto_definido:deudor_en_situacion_normal"
   },
   "fuente": {
    "quote": "sin deducir el 100% del importe de la previsión por riesgo de incobrabilidad correspondiente a la cartera de deudores clasificados “en situación normal” –puntos 6.5.1. y 7.2.1. del TO sobre Clasificación de Deudores– y a las financiaciones que se encuentran cubiertas con garantías preferidas A).",
    "ubicacion": "TO_capitales_minimos_actual.pdf, Sección 2 > Punto 2.3"
   }
  },
  "busquedas": [
   {
    "consulta": "deudor situación normal cartera",
    "resultado": "devuelve PRIMERO concepto_definido:deudor_en_situacion_normal ('cuya cartera no será deducida al 100% de la previsión por riesgo de incobrabilidad') — nodo portador de la respuesta, alcanzable con vocabulario ex ante ('en situación normal' ya expuesto al agente en el resumen del nodo abierto en paso 5)"
   },
   {
    "consulta": "activos no se deduce previsión situación normal cómputo",
    "resultado": "devuelve deudor_en_situacion_normal y prevision_por_riesgo_de_incobrabilidad_cartera_situacion_normal — el dato pertinente es alcanzable"
   }
  ],
  "capa_d": {
   "modulo": "D2",
   "accion": "sin_portador_extraible",
   "triage": true
  }
 },
 {
  "sintoma_capa1": "context_recall",
  "causa_capa2": "navegación",
  "lado": "agente",
  "jerarquia": "primaria",
  "pata": "Cómo se vincula esa regla con la clasificación de deudores",
  "evidencia": {
   "afirmacion": {
    "quote": "No se encontró en el Knowledge Graph información sobre cómo se vincula esa regla con la clasificación de deudores.",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "Norma externa que define situaciones de deudores y disposiciones sobre clasificación, referenciada en puntos 6.5.1 y 7.2.1.",
    "ubicacion": "norma_referenciada:texto_ordenado_sobre_clasificacion_de_deudores (expuesto al agente en el output completo del paso 3)"
   },
   "fuente": {
    "quote": "correspondiente a la cartera de deudores clasificados “en situación normal” –puntos 6.5.1. y 7.2.1. del TO sobre Clasificación de Deudores–",
    "ubicacion": "TO_capitales_minimos_actual.pdf, Sección 2 > Punto 2.3"
   }
  },
  "busquedas": [
   {
    "consulta": "clasificación deudores previsión (paso 3 del agente, re-ejecutado)",
    "resultado": "el output completo del paso 3 YA le expuso al agente texto_ordenado_sobre_clasificacion_de_deudores con resumen 'referenciada en puntos 6.5.1 y 7.2.1' — la vinculación exacta estaba disponible en su propia trayectoria"
   },
   {
    "consulta": "deudor situación normal cartera",
    "resultado": "deudor_en_situacion_normal explicita que la clasificación 'en situación normal' es el nexo con la regla de no deducción"
   }
  ],
  "capa_d": {
   "modulo": "D2",
   "portador_id": "norma_referenciada:texto_ordenado_sobre_clasificacion_de_deudores",
   "emision_llm": "navegación",
   "decision_codigo": "navegación",
   "discrepancia": false,
   "alcanzable": true,
   "evidencia_d1": {
    "alcanzable": true,
    "n_consultas_simuladas": 41,
    "consultas_en_top10": [
     {
      "consulta": "clasificación deudores previsión",
      "origen": "agente",
      "tokens_fuera_vocabulario": [],
      "total_con_match": 82,
      "rank": 7,
      "score": 2,
      "tokens_matcheados": [
       "clasificacion",
       "deudores"
      ],
      "en_top10": true
     },
     {
      "consulta": "clasificacion deudores",
      "origen": "ngrama_pregunta",
      "tokens_fuera_vocabulario": [],
      "total_con_match": 73,
      "rank": 6,
      "score": 2,
      "tokens_matcheados": [
       "clasificacion",
       "deudores"
      ],
      "en_top10": true
     },
     {
      "consulta": "regla clasificacion deudores",
      "origen": "ngrama_pregunta",
      "tokens_fuera_vocabulario": [],
      "total_con_match": 73,
      "rank": 6,
      "score": 2,
      "tokens_matcheados": [
       "clasificacion",
       "deudores"
      ],
      "en_top10": true
     }
    ],
    "mejor_rank": 6
   }
  }
 }
]
```

### Rep 3

- `formato_invalido`: `false` · `errores_formato`: `[]`
- `detectores`: `{"flag_encuadre_invertido": false, "flag_contexto": false, "tool_calls_usadas": 9, "max_tool_calls": 40, "tokens_in": 200077, "tokens_out": 6811}`
- longitudes: `razonamiento` = 2391 chars · `extraccion_traza` = 4063 chars

`atribuciones` ÍNTEGRAS (post-capa, con `capa_d`/`capa_d5`/`capa_d6`; la emisión original del LLM queda en los campos `emision_llm` donde la capa corrigió/degradó):

```json
[
 {
  "sintoma_capa1": "context_recall",
  "causa_capa2": "navegación",
  "lado": "agente",
  "jerarquia": "primaria",
  "pata": "Qué previsión por incobrabilidad no se deduce al computar los activos para la exigencia de capital por riesgo de crédito",
  "evidencia": {
   "afirmacion": {
    "quote": "No se encontró en el Knowledge Graph información específica sobre qué previsión por incobrabilidad no se deduce al computar los activos para la exigencia de capital por riesgo de crédito",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "Clasificación de deudor según normativa de clasificación de deudores del BCRA, cuya cartera no será deducida al 100% de la previsión por riesgo de incobrabilidad.",
    "ubicacion": "concepto_definido:deudor_en_situacion_normal"
   },
   "fuente": {
    "quote": "sin deducir el 100% del importe de la previsión por riesgo de incobrabilidad correspondiente a la cartera de deudores clasificados “en situación normal” –puntos 6.5.1. y 7.2.1. del TO sobre Clasificación de Deudores– y a las financiaciones que se encuentran cubiertas con garantías preferidas A).",
    "ubicacion": "TO_capitales_minimos_actual.pdf, Punto 2.3.1"
   }
  },
  "busquedas": [
   {
    "consulta": "previsión incobrabilidad situación normal",
    "resultado": "1er y 3er resultado: prevision_por_riesgo_de_incobrabilidad_cartera_situacion_normal y deudor_en_situacion_normal — nodos portadores de la respuesta, alcanzados de inmediato"
   },
   {
    "consulta": "deudores situación normal deducción previsión",
    "resultado": "deudor_en_situacion_normal aparece 4to; vocabulario 'situación normal' ya expuesto al agente en el paso 5"
   },
   {
    "consulta": "situación normal previsión no deducir cómputo conceptos comprendidos",
    "resultado": "devuelve deudor_en_situacion_normal, conceptos_comprendidos y prevision_por_riesgo_de_incobrabilidad_cartera_situacion_normal — todos pertinentes"
   }
  ],
  "capa_d": {
   "modulo": "D2",
   "accion": "sin_portador_extraible",
   "triage": true
  }
 },
 {
  "sintoma_capa1": "context_recall",
  "causa_capa2": "navegación",
  "lado": "agente",
  "jerarquia": "primaria",
  "pata": "Cómo se vincula esa regla con la clasificación de deudores",
  "evidencia": {
   "afirmacion": {
    "quote": "No se encontró en el Knowledge Graph información sobre cómo se vincula esa regla con la clasificación de deudores.",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "Clasificación de deudor según normativa de clasificación de deudores del BCRA, cuya cartera no será deducida al 100% de la previsión por riesgo de incobrabilidad.",
    "ubicacion": "concepto_definido:deudor_en_situacion_normal"
   },
   "fuente": {
    "quote": "sin deducir el 100% del importe de la previsión por riesgo de incobrabilidad correspondiente a la cartera de deudores clasificados “en situación normal” –puntos 6.5.1. y 7.2.1. del TO sobre Clasificación de Deudores–",
    "ubicacion": "TO_capitales_minimos_actual.pdf, Punto 2.3.1"
   }
  },
  "busquedas": [
   {
    "consulta": "previsión incobrabilidad situación normal",
    "resultado": "deudor_en_situacion_normal, cuya descripción vincula explícitamente la regla con la 'normativa de clasificación de deudores del BCRA'"
   },
   {
    "consulta": "deudores situación normal deducción previsión",
    "resultado": "deudor_en_situacion_normal alcanzable; el vínculo con clasificación está en su description y en el PDF Punto 2.3.1 (remite a puntos 6.5.1 y 7.2.1 del TO sobre Clasificación de Deudores)"
   }
  ],
  "capa_d": {
   "modulo": "D2",
   "accion": "sin_portador_extraible",
   "triage": true
  }
 }
]
```

**Tokens del caso (suma detectores 3 reps): in=771,888 · out=27,759**


---

## run_2/CQ-025 (`validacion_v61/off_run_2_CQ-025.json` + `_capa_d.json`)

**Voto v5.7 original (verbatim):**

```json
{
 "resultado": "mayoria",
 "flag_voto_dividido": false,
 "pares_primarios_ganadores": [
  [
   "context_recall",
   "navegación"
  ]
 ],
 "votos_ganadores": 3,
 "conteo": [
  {
   "pares_primarios": [
    [
     "context_recall",
     "navegación"
    ]
   ],
   "votos": 3
  }
 ],
 "desglose": [
  {
   "rep": 1,
   "pares_primarios": [
    [
     "context_recall",
     "navegación"
    ]
   ],
   "formato_invalido": false
  },
  {
   "rep": 2,
   "pares_primarios": [
    [
     "context_recall",
     "navegación"
    ]
   ],
   "formato_invalido": false
  },
  {
   "rep": 3,
   "pares_primarios": [
    [
     "context_recall",
     "navegación"
    ]
   ],
   "formato_invalido": false
  }
 ]
}
```

**voto_pre_d6:**

```json
{
 "resultado": "mayoria",
 "flag_voto_dividido": false,
 "pares_primarios_ganadores": [
  [
   "context_recall",
   "alcanzabilidad_kg"
  ]
 ],
 "votos_ganadores": 3,
 "reps_validas": [
  1,
  2,
  3
 ],
 "conteo": [
  {
   "pares_primarios": [
    [
     "context_recall",
     "alcanzabilidad_kg"
    ]
   ],
   "votos": 3,
   "reps": [
    1,
    2,
    3
   ]
  }
 ]
}
```

**voto_capa_d (final, post-D6):**

```json
{
 "resultado": "mayoria",
 "flag_voto_dividido": false,
 "pares_primarios_ganadores": [
  [
   "context_recall",
   "alcanzabilidad_kg"
  ]
 ],
 "votos_ganadores": 3,
 "reps_validas": [
  1,
  2,
  3
 ],
 "conteo": [
  {
   "pares_primarios": [
    [
     "context_recall",
     "alcanzabilidad_kg"
    ]
   ],
   "votos": 3,
   "reps": [
    1,
    2,
    3
   ]
  }
 ]
}
```

**resumen_capa_d:** `{"reps_tocadas": [1, 2, 3], "atribuciones_corregidas": 3, "discrepancias": 3, "triage": 0}`

**triage_capa_d (motivos y flags completos):**

```json
{
 "triage": true,
 "motivos": [
  "atribucion_no_verificable",
  "aplicacion_erronea_bajo_revision"
 ],
 "flags": [
  "R6b: rep 1 atrib 1 — context_recall_sin_pata",
  "R6b: rep 2 atrib 1 — context_recall_sin_pata",
  "R2: rep 2 atrib 2 (secundaria) causa aplicacion_erronea",
  "R6b: rep 3 atrib 1 — context_recall_sin_pata"
 ]
}
```

### Rep 1

- `formato_invalido`: `false` · `errores_formato`: `[]`
- `detectores`: `{"flag_encuadre_invertido": false, "flag_contexto": false, "tool_calls_usadas": 11, "max_tool_calls": 40, "tokens_in": 182829, "tokens_out": 5969}`
- longitudes: `razonamiento` = 2355 chars · `extraccion_traza` = 2342 chars

`atribuciones` ÍNTEGRAS (post-capa, con `capa_d`/`capa_d5`/`capa_d6`; la emisión original del LLM queda en los campos `emision_llm` donde la capa corrigió/degradó):

```json
[
 {
  "sintoma_capa1": "context_recall",
  "causa_capa2": "alcanzabilidad_kg",
  "lado": "agente",
  "jerarquia": "primaria",
  "pata": "Frecuencia con que se informa la exigencia por riesgo de mercado en el Régimen Informativo de Capitales Mínimos",
  "evidencia": {
   "afirmacion": {
    "quote": "En el Régimen Informativo de Capitales Mínimos, la exigencia por riesgo de mercado se informa con frecuencia mensual.",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "Datos complementarios vinculados al cálculo de la exigencia por riesgo de mercado se presentarán con frecuencia trimestral con datos del último mes de cada trimestre.",
    "ubicacion": "obligacion:presentacion_trimestral_de_datos_complementarios_de_riesgo_de_mercado"
   },
   "fuente": {
    "quote": "1.1. La información tendrá frecuencia mensual y se integrará con datos referidos al mes bajo análisis, excepto las siguientes informaciones que tendrán frecuencia trimestral (...) - Datos complementarios vinculados al cálculo de la exigencia por riesgo de mercado (puntos 4.3., 4.4. y 4.5. de la Sección 4.) (...)",
    "ubicacion": "TO_regimen_informativo_contable_mensual_actual.pdf, Sección 12 > Punto 1.1"
   }
  },
  "busquedas": [
   {
    "consulta": "riesgo de mercado frecuencia trimestral",
    "resultado": "el nodo 'presentacion_trimestral_de_datos_complementarios_de_riesgo_de_mercado' (frecuencia trimestral) aparece PRIMERO — alcanzable"
   },
   {
    "consulta": "datos complementarios exigencia riesgo de mercado",
    "resultado": "el mismo nodo pertinente aparece PRIMERO — alcanzable con términos de la pregunta"
   },
   {
    "consulta": "envío mensual datos riesgo de mercado (réplica del vocabulario del agente)",
    "resultado": "el nodo trimestral aparece en 2º lugar; el agente disponía de vocabulario que lo alcanzaba"
   }
  ],
  "capa_d": {
   "modulo": "D2",
   "portador_id": "obligacion:presentacion_trimestral_de_datos_complementarios_de_riesgo_de_mercado",
   "emision_llm": "navegación",
   "decision_codigo": "alcanzabilidad_kg",
   "discrepancia": true,
   "alcanzable": false,
   "evidencia_d1": {
    "alcanzable": false,
    "n_consultas_simuladas": 27,
    "consultas_en_top10": [],
    "mejor_rank": 22
   }
  },
  "capa_d6": {
   "regla": "R6b",
   "accion": "context_recall_sin_pata"
  }
 }
]
```

### Rep 2

- `formato_invalido`: `false` · `errores_formato`: `[]`
- `detectores`: `{"flag_encuadre_invertido": false, "flag_contexto": false, "tool_calls_usadas": 16, "max_tool_calls": 40, "tokens_in": 323559, "tokens_out": 8705}`
- longitudes: `razonamiento` = 2212 chars · `extraccion_traza` = 2627 chars

`atribuciones` ÍNTEGRAS (post-capa, con `capa_d`/`capa_d5`/`capa_d6`; la emisión original del LLM queda en los campos `emision_llm` donde la capa corrigió/degradó):

```json
[
 {
  "sintoma_capa1": "context_recall",
  "causa_capa2": "alcanzabilidad_kg",
  "lado": "agente",
  "jerarquia": "primaria",
  "pata": "Frecuencia con que se informa la exigencia por riesgo de mercado",
  "evidencia": {
   "afirmacion": {
    "quote": "En el Régimen Informativo de Capitales Mínimos, la exigencia por riesgo de mercado se informa con frecuencia mensual.",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "Datos complementarios vinculados al cálculo de la exigencia por riesgo de mercado se presentarán con frecuencia trimestral con datos del último mes de cada trimestre.",
    "ubicacion": "obligacion:presentacion_trimestral_de_datos_complementarios_de_riesgo_de_mercado (nodo portador, NO consultado por el agente)"
   },
   "fuente": {
    "quote": "1.1. La información tendrá frecuencia mensual y se integrará con datos referidos al mes bajo análisis, excepto las siguientes informaciones que tendrán frecuencia trimestral (…) - Datos complementarios vinculados al cálculo de la exigencia por riesgo de mercado (puntos 4.3., 4.4. y 4.5. de la Sección 4.) (…)",
    "ubicacion": "TO_regimen_informativo_contable_mensual_actual.pdf, Sección 12 > Punto 1.1"
   }
  },
  "busquedas": [
   {
    "consulta": "riesgo de mercado frecuencia (réplica del vocabulario ex ante del agente)",
    "resultado": "top-15 NO incluye el nodo 'presentacion_trimestral_de_datos_complementarios_de_riesgo_de_mercado'; solo conceptos/obligaciones de determinar/informar y 'envío mensual de datos'"
   },
   {
    "consulta": "frecuencia trimestral riesgo de mercado información complementaria",
    "resultado": "el nodo portador aparece PRIMERO (4 tokens)"
   },
   {
    "consulta": "presentación datos complementarios riesgo de mercado",
    "resultado": "el nodo portador aparece PRIMERO con 6 tokens matcheados — alcanzable con vocabulario razonable ex ante (presentación/datos/informa/riesgo de mercado)"
   }
  ],
  "capa_d": {
   "modulo": "D2",
   "portador_id": "obligacion:presentacion_trimestral_de_datos_complementarios_de_riesgo_de_mercado",
   "emision_llm": "navegación",
   "decision_codigo": "alcanzabilidad_kg",
   "discrepancia": true,
   "alcanzable": false,
   "evidencia_d1": {
    "alcanzable": false,
    "n_consultas_simuladas": 27,
    "consultas_en_top10": [],
    "mejor_rank": 22
   }
  },
  "capa_d6": {
   "regla": "R6b",
   "accion": "context_recall_sin_pata"
  }
 },
 {
  "sintoma_capa1": "noise_sensitivity",
  "causa_capa2": "aplicacion_erronea",
  "lado": "agente",
  "jerarquia": "secundaria",
  "pata": "Frecuencia con que se informa la exigencia por riesgo de mercado",
  "evidencia": {
   "afirmacion": {
    "quote": "La exigencia por riesgo de mercado corresponde a las posiciones del último día del mes.",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "Obligación de informar exigencia según riesgo de mercado para posiciones del último día del mes, calculada según punto 4.1.1.",
    "ubicacion": "obligacion:informar_exigencia_por_riesgo_de_mercado (consultado en paso 4)"
   },
   "fuente": {
    "quote": "4.1.1.1. La exigencia por riesgo de mercado se determinará con los valores que se registren al último día del período de información (n)",
    "ubicacion": "TO_regimen_informativo_contable_mensual_actual.pdf, Punto 4.1.1"
   }
  },
  "busquedas": [
   {
    "consulta": "verificación del período de la posición vs frecuencia de envío",
    "resultado": "el nodo describe el PERÍODO de la posición ('último día del mes'), que es fiel al PDF, pero el agente lo usó como sustento de la FRECUENCIA de informe (mensual), alcance distinto; el PDF asigna a estos datos frecuencia TRIMESTRAL"
   }
  ],
  "capa_d": {
   "modulo": "D3",
   "portador_id": "obligacion:informar_exigencia_por_riesgo_de_mercado",
   "quote_verificado": true
  }
 }
]
```

### Rep 3

- `formato_invalido`: `false` · `errores_formato`: `[]`
- `detectores`: `{"flag_encuadre_invertido": false, "flag_contexto": false, "tool_calls_usadas": 15, "max_tool_calls": 40, "tokens_in": 264568, "tokens_out": 8470}`
- longitudes: `razonamiento` = 2637 chars · `extraccion_traza` = 2576 chars

`atribuciones` ÍNTEGRAS (post-capa, con `capa_d`/`capa_d5`/`capa_d6`; la emisión original del LLM queda en los campos `emision_llm` donde la capa corrigió/degradó):

```json
[
 {
  "sintoma_capa1": "context_recall",
  "causa_capa2": "alcanzabilidad_kg",
  "lado": "agente",
  "jerarquia": "primaria",
  "pata": "Frecuencia con que se informa la exigencia por riesgo de mercado",
  "evidencia": {
   "afirmacion": {
    "quote": "En el Régimen Informativo de Capitales Mínimos, la exigencia por riesgo de mercado se informa con frecuencia mensual (para posiciones del último día del mes)",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "Datos complementarios vinculados al cálculo de la exigencia por riesgo de mercado se presentarán con frecuencia trimestral con datos del último mes de cada trimestre.",
    "ubicacion": "obligacion:presentacion_trimestral_de_datos_complementarios_de_riesgo_de_mercado"
   },
   "fuente": {
    "quote": "1.1. La información tendrá frecuencia mensual y se integrará con datos referidos al mes bajo análisis, excepto las siguientes informaciones que tendrán frecuencia trimestral y se integrarán de la siguiente manera: Con los datos correspondientes al último mes de cada trimestre (marzo, junio, septiembre y diciembre): - Datos complementarios vinculados al cálculo de la exigencia por riesgo de mercado (puntos 4.3., 4.4. y 4.5. de la Sección 4.)",
    "ubicacion": "TO_regimen_informativo_contable_mensual_actual.pdf, Sección 12 > Punto 1.1"
   }
  },
  "busquedas": [
   {
    "consulta": "riesgo de mercado frecuencia informe (búsqueda exacta del agente, ampliada a 20)",
    "resultado": "El nodo portador 'presentacion_trimestral_de_datos_complementarios_de_riesgo_de_mercado' NO aparece entre los 20 primeros (3774 matches, el ranking léxico lo empuja fuera)."
   },
   {
    "consulta": "presentación datos complementarios riesgo de mercado",
    "resultado": "El nodo portador aparece 1º (6 tokens matcheados) — alcanzable con una reformulación razonable desde el vocabulario de la pregunta ('presentación'/'informa' + 'riesgo de mercado')."
   },
   {
    "consulta": "información riesgo de mercado frecuencia trimestral vencimiento",
    "resultado": "El nodo portador aparece 1º — confirma que existe y es fiel al PDF."
   }
  ],
  "capa_d": {
   "modulo": "D2",
   "portador_id": "obligacion:presentacion_trimestral_de_datos_complementarios_de_riesgo_de_mercado",
   "emision_llm": "navegación",
   "decision_codigo": "alcanzabilidad_kg",
   "discrepancia": true,
   "alcanzable": false,
   "evidencia_d1": {
    "alcanzable": false,
    "n_consultas_simuladas": 27,
    "consultas_en_top10": [],
    "mejor_rank": 22
   }
  },
  "capa_d6": {
   "regla": "R6b",
   "accion": "context_recall_sin_pata"
  }
 }
]
```

**Tokens del caso (suma detectores 3 reps): in=770,956 · out=23,144**


---

## run_4/CQ-014 (`validacion_v61/off_run_4_CQ-014.json` + `_capa_d.json`)

**Voto v5.7 original (verbatim):**

```json
{
 "resultado": "mayoria",
 "flag_voto_dividido": false,
 "pares_primarios_ganadores": [],
 "votos_ganadores": 3,
 "conteo": [
  {
   "pares_primarios": [],
   "votos": 3
  }
 ],
 "desglose": [
  {
   "rep": 1,
   "pares_primarios": [],
   "formato_invalido": false
  },
  {
   "rep": 2,
   "pares_primarios": [],
   "formato_invalido": false
  },
  {
   "rep": 3,
   "pares_primarios": [],
   "formato_invalido": false
  }
 ]
}
```

**voto_pre_d6:**

```json
{
 "resultado": "mayoria",
 "flag_voto_dividido": false,
 "pares_primarios_ganadores": [],
 "votos_ganadores": 3,
 "reps_validas": [
  1,
  2,
  3
 ],
 "conteo": [
  {
   "pares_primarios": [],
   "votos": 3,
   "reps": [
    1,
    2,
    3
   ]
  }
 ]
}
```

**voto_capa_d (final, post-D6):**

```json
{
 "resultado": "mayoria",
 "flag_voto_dividido": false,
 "pares_primarios_ganadores": [],
 "votos_ganadores": 3,
 "reps_validas": [
  1,
  2,
  3
 ],
 "conteo": [
  {
   "pares_primarios": [],
   "votos": 3,
   "reps": [
    1,
    2,
    3
   ]
  }
 ]
}
```

**resumen_capa_d:** `{"reps_tocadas": [], "atribuciones_corregidas": 0, "discrepancias": 0, "triage": 0}`

**triage_capa_d (motivos y flags completos):**

```json
{
 "triage": true,
 "motivos": [
  "exoneracion_total"
 ],
 "flags": [
  "R1: voto_capa_d con mayoria de clave vacia (3 votos sin primarias)"
 ]
}
```

### Rep 1

- `formato_invalido`: `false` · `errores_formato`: `[]`
- `detectores`: `{"flag_encuadre_invertido": false, "flag_contexto": false, "tool_calls_usadas": 3, "max_tool_calls": 40, "tokens_in": 68027, "tokens_out": 3809}`
- longitudes: `razonamiento` = 1557 chars · `extraccion_traza` = 2620 chars

`atribuciones` ÍNTEGRAS (post-capa, con `capa_d`/`capa_d5`/`capa_d6`; la emisión original del LLM queda en los campos `emision_llm` donde la capa corrigió/degradó):

```json
[
 {
  "sintoma_capa1": "noise_sensitivity",
  "causa_capa2": "sin_defecto",
  "lado": "ninguno",
  "jerarquia": "sin_par",
  "pata": "plazo para ingresar y liquidar en el mercado de cambios los cobros de exportaciones de servicios",
  "evidencia": {
   "afirmacion": {
    "quote": "Los cobros de exportaciones de servicios deben ingresarse y liquidarse en el mercado de cambios en un plazo no mayor a 20 días hábiles.",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "Operación de ingreso de divisas por prestación de servicios por residentes a no residentes, que debe ser ingresada y liquidada en el mercado de cambios en plazo no mayor a 20 días hábiles.",
    "ubicacion": "cobro_de_exportacion_de_servicios (abierto por el agente en paso 8)"
   },
   "fuente": {
    "quote": "2.2.1. Los cobros por la prestación de servicios por parte de residentes a no residentes deberán ser ingresados y liquidados en el mercado de cambios en un plazo no mayor a los 20 (veinte) días hábiles a partir de la fecha de su percepción en el exterior o en el país o de su acreditación en cuentas del exterior.",
    "ubicacion": "TO_exterior_cambios_actual.pdf, Punto 2.2.1"
   }
  },
  "busquedas": [
   {
    "consulta": "leer_pasaje_pdf Punto 2.2.1",
    "resultado": "El PDF confirma 'plazo no mayor a los 20 (veinte) días hábiles' — coincide verbatim con el nodo y la respuesta"
   },
   {
    "consulta": "verificación del nodo cobro_de_exportacion_de_servicios",
    "resultado": "nodo fiel, pertinente, provenance Punto 2.2.1 que efectivamente funda su contenido"
   }
  ]
 }
]
```

### Rep 2

- `formato_invalido`: `false` · `errores_formato`: `[]`
- `detectores`: `{"flag_encuadre_invertido": false, "flag_contexto": false, "tool_calls_usadas": 4, "max_tool_calls": 40, "tokens_in": 92616, "tokens_out": 4004}`
- longitudes: `razonamiento` = 1652 chars · `extraccion_traza` = 2533 chars

`atribuciones` ÍNTEGRAS (post-capa, con `capa_d`/`capa_d5`/`capa_d6`; la emisión original del LLM queda en los campos `emision_llm` donde la capa corrigió/degradó):

```json
[
 {
  "sintoma_capa1": "noise_sensitivity",
  "causa_capa2": "sin_defecto",
  "lado": "ninguno",
  "jerarquia": "sin_par",
  "pata": "plazo para ingresar y liquidar en el mercado de cambios los cobros de exportaciones de servicios",
  "evidencia": {
   "afirmacion": {
    "quote": "Los cobros de exportaciones de servicios deben ingresarse y liquidarse en el mercado de cambios en un plazo no mayor a 20 días hábiles.",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "Operación de ingreso de divisas por prestación de servicios por residentes a no residentes, que debe ser ingresada y liquidada en el mercado de cambios en plazo no mayor a 20 días hábiles.",
    "ubicacion": "cobro_de_exportacion_de_servicios (abierto por el agente en paso 8)"
   },
   "fuente": {
    "quote": "2.2.1. Los cobros por la prestación de servicios por parte de residentes a no residentes deberán ser ingresados y liquidados en el mercado de cambios en un plazo no mayor a los 20 (veinte) días hábiles a partir de la fecha de su percepción en el exterior o en el país o de su acreditación en cuentas del exterior.",
    "ubicacion": "TO_exterior_cambios_actual.pdf, Punto 2.2.1 (PDF pág 8)"
   }
  },
  "busquedas": [
   {
    "consulta": "leer_pasaje_pdf Punto 2.2.1",
    "resultado": "El PDF confirma verbatim '20 (veinte) días hábiles' para cobros por prestación de servicios de residentes a no residentes"
   },
   {
    "consulta": "leer_pasaje_pdf p.5-8",
    "resultado": "Resuelve a índice; el anclaje que funda el contenido es el Punto 2.2.1, que sí contiene el plazo"
   }
  ]
 }
]
```

### Rep 3

- `formato_invalido`: `false` · `errores_formato`: `[]`
- `detectores`: `{"flag_encuadre_invertido": false, "flag_contexto": false, "tool_calls_usadas": 4, "max_tool_calls": 40, "tokens_in": 92452, "tokens_out": 4300}`
- longitudes: `razonamiento` = 1536 chars · `extraccion_traza` = 2959 chars

`atribuciones` ÍNTEGRAS (post-capa, con `capa_d`/`capa_d5`/`capa_d6`; la emisión original del LLM queda en los campos `emision_llm` donde la capa corrigió/degradó):

```json
[
 {
  "sintoma_capa1": "noise_sensitivity",
  "causa_capa2": "sin_defecto",
  "lado": "ninguno",
  "jerarquia": "sin_par",
  "pata": "plazo para ingresar y liquidar en el mercado de cambios los cobros de exportaciones de servicios",
  "evidencia": {
   "afirmacion": {
    "quote": "Los cobros de exportaciones de servicios deben ingresarse y liquidarse en el mercado de cambios en un plazo no mayor a 20 días hábiles.",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "Operación de ingreso de divisas por prestación de servicios por residentes a no residentes, que debe ser ingresada y liquidada en el mercado de cambios en plazo no mayor a 20 días hábiles.",
    "ubicacion": "cobro_de_exportacion_de_servicios (abierto por el agente en paso 8)"
   },
   "fuente": {
    "quote": "2.2.1. Los cobros por la prestación de servicios por parte de residentes a no residentes deberán ser ingresados y liquidados en el mercado de cambios en un plazo no mayor a los 20 (veinte) días hábiles a partir de la fecha de su percepción en el exterior o en el país o de su acreditación en cuentas del exterior.",
    "ubicacion": "TO_exterior_cambios_actual.pdf, Punto 2.2.1 (PDF pág 8)"
   }
  },
  "busquedas": [
   {
    "consulta": "leer_pasaje_pdf Punto 2.2.1",
    "resultado": "El PDF dice exactamente 'plazo no mayor a los 20 (veinte) días hábiles' para cobros de servicios por residentes a no residentes: la afirmación es correcta"
   },
   {
    "consulta": "ver_nodo plazo_de_20_dias_habiles",
    "resultado": "Nodo homónimo de otro alcance (enajenación de activos no financieros no producidos, punto 2.3/7.6); el agente NO lo usó — usó el nodo correcto, sin contaminación"
   }
  ]
 }
]
```

**Tokens del caso (suma detectores 3 reps): in=253,095 · out=12,113**


---

## run_4/CQ-017 (`validacion_v61/off_run_4_CQ-017.json` + `_capa_d.json`)

**Voto v5.7 original (verbatim):**

```json
{
 "resultado": "mayoria",
 "flag_voto_dividido": false,
 "pares_primarios_ganadores": [
  [
   "context_recall",
   "estructural_kg"
  ]
 ],
 "votos_ganadores": 2,
 "conteo": [
  {
   "pares_primarios": [
    [
     "context_recall",
     "estructural_kg"
    ]
   ],
   "votos": 2
  },
  {
   "pares_primarios": [],
   "votos": 1
  }
 ],
 "desglose": [
  {
   "rep": 1,
   "pares_primarios": [],
   "formato_invalido": false
  },
  {
   "rep": 2,
   "pares_primarios": [
    [
     "context_recall",
     "estructural_kg"
    ]
   ],
   "formato_invalido": false
  },
  {
   "rep": 3,
   "pares_primarios": [
    [
     "context_recall",
     "estructural_kg"
    ]
   ],
   "formato_invalido": false
  }
 ]
}
```

**voto_pre_d6:**

```json
{
 "resultado": "mayoria",
 "flag_voto_dividido": false,
 "pares_primarios_ganadores": [
  [
   "context_recall",
   "estructural_kg"
  ]
 ],
 "votos_ganadores": 2,
 "reps_validas": [
  1,
  2,
  3
 ],
 "conteo": [
  {
   "pares_primarios": [
    [
     "context_recall",
     "estructural_kg"
    ]
   ],
   "votos": 2,
   "reps": [
    2,
    3
   ]
  },
  {
   "pares_primarios": [],
   "votos": 1,
   "reps": [
    1
   ]
  }
 ]
}
```

**voto_capa_d (final, post-D6):**

```json
{
 "resultado": "mayoria",
 "flag_voto_dividido": false,
 "pares_primarios_ganadores": [
  [
   "context_recall",
   "estructural_kg"
  ]
 ],
 "votos_ganadores": 2,
 "reps_validas": [
  1,
  2,
  3
 ],
 "conteo": [
  {
   "pares_primarios": [
    [
     "context_recall",
     "estructural_kg"
    ]
   ],
   "votos": 2,
   "reps": [
    2,
    3
   ]
  },
  {
   "pares_primarios": [],
   "votos": 1,
   "reps": [
    1
   ]
  }
 ]
}
```

**resumen_capa_d:** `{"reps_tocadas": [], "atribuciones_corregidas": 0, "discrepancias": 0, "triage": 0}`

**triage_capa_d (motivos y flags completos):**

```json
{
 "triage": false,
 "motivos": [],
 "flags": []
}
```

### Rep 1

- `formato_invalido`: `false` · `errores_formato`: `[]`
- `detectores`: `{"flag_encuadre_invertido": false, "flag_contexto": false, "tool_calls_usadas": 10, "max_tool_calls": 40, "tokens_in": 289636, "tokens_out": 7550}`
- longitudes: `razonamiento` = 2418 chars · `extraccion_traza` = 4128 chars

`atribuciones` ÍNTEGRAS (post-capa, con `capa_d`/`capa_d5`/`capa_d6`; la emisión original del LLM queda en los campos `emision_llm` donde la capa corrigió/degradó):

```json
[
 {
  "sintoma_capa1": "noise_sensitivity",
  "causa_capa2": "sin_defecto",
  "lado": "ninguno",
  "jerarquia": "sin_par",
  "pata": "¿Un operador de cambio debe intervenir como entidad autorizada en el mercado de cambios? (glosa contextual)",
  "evidencia": {
   "afirmacion": {
    "quote": "El mercado libre de cambios está definido como aquel por el cual se cursan operaciones realizadas por 'entidades financieras y demás personas autorizadas por el BCRA' para dedicarse al comercio de compra y venta de monedas extranjeras.",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "Mercado por el cual se cursan las operaciones de cambio realizadas por entidades financieras y demás personas autorizadas por el BCRA para dedicarse al comercio de compra y venta de monedas y billetes extranjeros, oro amonedado o en barra, cheques de viajero, giros, transferencias u operaciones análogas en moneda extranjera.",
    "ubicacion": "mercado_libre_de_cambios (abierto por el agente en paso 11)"
   },
   "fuente": {
    "quote": "Establécese un mercado libre de cambios por el cual se cursarán las operaciones de cambio que sean realizadas por las entidades financieras y las demás personas autorizadas por el Banco Central de la República Argentina para dedicarse de manera permanente o habitual al comercio de la compra y venta de monedas y billetes extranjeros, oro amonedado o en barra de buena entrega y cheques de viajero, giros, transferencias u operaciones análogas en moneda extranjera.",
    "ubicacion": "TO_exterior_cambios_actual.pdf, p.184 (Sección 15.1, Art. 1° Decreto 260/02)"
   }
  },
  "busquedas": [
   {
    "consulta": "leer_pasaje_pdf p.184 TO_exterior_cambios",
    "resultado": "El PDF confirma verbatim la definición de mercado libre de cambios del Decreto 260/02 Art. 1° — el claim del agente es fiel"
   }
  ]
 },
 {
  "sintoma_capa1": "noise_sensitivity",
  "causa_capa2": "sin_defecto",
  "lado": "ninguno",
  "jerarquia": "sin_par",
  "pata": "¿Un operador de cambio debe intervenir como entidad autorizada en el mercado de cambios? (glosa contextual)",
  "evidencia": {
   "afirmacion": {
    "quote": "Existe una categoría de 'personas jurídicas no autorizadas a operar en cambios' que requieren conformidad previa del BCRA para acceder al mercado de cambios.",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "Personas jurídicas que no sean entidades autorizadas a operar en cambios, que requieren conformidad previa del BCRA para acceder al mercado de cambios para formación de activos externos y operaciones con derivados.",
    "ubicacion": "personas_juridicas_no_autorizadas_a_operar_en_cambios (abierto por el agente en paso 15)"
   },
   "fuente": {
    "quote": "El acceso al mercado de cambios por parte de personas jurídicas que no sean entidades autorizadas a operar en cambios, gobiernos locales, Fondos Comunes de Inversión, Fideicomisos y otras universalidades constituidas en el país, requerirá la conformidad previa del BCRA para la formación de activos externos (...) y para la operatoria con derivados (...)",
    "ubicacion": "TO_exterior_cambios_actual.pdf, p.34 (Punto 3.10)"
   }
  },
  "busquedas": [
   {
    "consulta": "leer_pasaje_pdf p.34 TO_exterior_cambios Punto 3.10",
    "resultado": "El PDF confirma verbatim el contenido del nodo — el claim del agente es fiel y correcto"
   }
  ]
 }
]
```

### Rep 2

- `formato_invalido`: `false` · `errores_formato`: `[]`
- `detectores`: `{"flag_encuadre_invertido": false, "flag_contexto": false, "tool_calls_usadas": 11, "max_tool_calls": 40, "tokens_in": 285904, "tokens_out": 7262}`
- longitudes: `razonamiento` = 2270 chars · `extraccion_traza` = 4424 chars

`atribuciones` ÍNTEGRAS (post-capa, con `capa_d`/`capa_d5`/`capa_d6`; la emisión original del LLM queda en los campos `emision_llm` donde la capa corrigió/degradó):

```json
[
 {
  "sintoma_capa1": "context_recall",
  "causa_capa2": "estructural_kg",
  "lado": "grafo",
  "jerarquia": "primaria",
  "pata": "¿Un operador de cambio debe intervenir como entidad autorizada en el mercado de cambios?",
  "evidencia": {
   "afirmacion": {
    "quote": "El mercado libre de cambios está definido como aquel por el cual se cursan operaciones realizadas por 'entidades financieras y demás personas autorizadas por el BCRA' para dedicarse al comercio de compra y venta de monedas extranjeras. Existe una categoría de 'personas jurídicas no autorizadas a operar en cambios' que requieren conformidad previa del BCRA para acceder al mercado de cambios. Sin embargo, no hay información explícita en el grafo que determine si los operadores de cambio deben o no intervenir como entidades autorizadas en el mercado de cambios.",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "n_salientes_total: 0, n_entrantes_total: 2, entrantes: [{relation: utiliza_servicios_de, vecino_id: usuario_de_servicios_financieros, provenances: TO_proteccion_usuarios...}, {relation: supervisa, vecino_id: banco_central_de_la_republica_argentina, provenances: TO_proteccion_usuarios...}]",
    "ubicacion": "operador_de_cambio (ver_vecinos, paso 5) — sus únicas aristas son al TO de protección de usuarios; ninguna arista lo conecta con el régimen de cambios ni con 'entidad autorizada'"
   },
   "fuente": {
    "quote": "Establécese un mercado libre de cambios por el cual se cursarán las operaciones de cambio que sean realizadas por las entidades financieras y las demás personas autorizadas por el Banco Central de la República Argentina para dedicarse de manera permanente o habitual al comercio de la compra y venta de monedas",
    "ubicacion": "TO_exterior_cambios_actual.pdf, p.183-185 / Sección 15.1"
   }
  },
  "busquedas": [
   {
    "consulta": "operador de cambio autorizado mercado interviene",
    "resultado": "operador_de_cambio, mercado_de_opciones_autorizado, casa_de_cambio — ningún nodo vincula al operador con la condición de entidad autorizada a intervenir"
   },
   {
    "consulta": "entidad autorizada operar en cambios",
    "resultado": "personas_juridicas_no_autorizadas_a_operar_en_cambios, entidad_autorizada (solo 'pagos anticipados de importaciones y acceder al mercado de cambios') — ninguno conecta con operador de cambio"
   },
   {
    "consulta": "operador cambio requisitos habilitacion registro",
    "resultado": "operador_de_cambio, casa_de_cambio — sin arista ni atributo que responda si el operador es entidad autorizada a intervenir"
   },
   {
    "consulta": "ver_vecinos operador_de_cambio ambas (paso 5)",
    "resultado": "0 aristas salientes; 2 entrantes, ambas del TO de protección de usuarios — no existe conexión estructural con el TO de Exterior y cambios"
   },
   {
    "consulta": "ver_vecinos mercado_libre_de_cambios ambas (paso 12) y personas_juridicas_no_autorizadas ambas (paso 16)",
    "resultado": "ninguna arista vincula esas categorías cambiarias con el operador de cambio"
   }
  ]
 }
]
```

### Rep 3

- `formato_invalido`: `false` · `errores_formato`: `[]`
- `detectores`: `{"flag_encuadre_invertido": false, "flag_contexto": false, "tool_calls_usadas": 12, "max_tool_calls": 40, "tokens_in": 406144, "tokens_out": 13462}`
- longitudes: `razonamiento` = 2425 chars · `extraccion_traza` = 4613 chars

`atribuciones` ÍNTEGRAS (post-capa, con `capa_d`/`capa_d5`/`capa_d6`; la emisión original del LLM queda en los campos `emision_llm` donde la capa corrigió/degradó):

```json
[
 {
  "sintoma_capa1": "context_recall",
  "causa_capa2": "estructural_kg",
  "lado": "grafo",
  "jerarquia": "primaria",
  "pata": "¿Un operador de cambio debe intervenir como entidad autorizada en el mercado de cambios?",
  "evidencia": {
   "afirmacion": {
    "quote": "Sin embargo, respecto a si debe intervenir como entidad autorizada en el mercado de cambios, la información disponible en el grafo no es concluyente. El mercado libre de cambios está definido como aquel por el cual se cursan operaciones realizadas por 'entidades financieras y demás personas autorizadas por el BCRA' para dedicarse al comercio de compra y venta de monedas extranjeras. Existe una categoría de 'personas jurídicas no autorizadas a operar en cambios' que requieren conformidad previa del BCRA para acceder al mercado de cambios.",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "Entidad autorizada a realizar pagos anticipados de importaciones y acceder al mercado de cambios. [aristas: accede_a mercado_de_cambios; realiza pago_anticipado; reporta_en SEPAIMPO — todas con provenance p.140-142/Punto 10.4.2; 0 aristas entrantes desde operador_de_cambio] | Sujeto obligado que realiza operaciones comprendidas en las normas sobre Exterior y cambios. [operador_de_cambio: aristas utiliza_servicios_de usuario y supervisa BCRA; ninguna hacia entidad_autorizada ni mercado_de_cambios]",
    "ubicacion": "entidad_autorizada y operador_de_cambio (ver_vecinos): no existe arista que los conecte"
   },
   "fuente": {
    "quote": "Establécese un mercado libre de cambios por el cual se cursarán las operaciones de cambio que sean realizadas por las entidades financieras y las demás personas autorizadas por el Banco Central de la República Argentina para dedicarse de manera permanente o habitual al comercio de la compra y venta de monedas",
    "ubicacion": "TO_exterior_cambios_actual.pdf, p.183-185 (Sección 15.1, Art 1° Dec 260/02)"
   }
  },
  "busquedas": [
   {
    "consulta": "operador de cambio entidad autorizada operar en cambios",
    "resultado": "operador_de_cambio aparece pero sin dato sobre su rol como entidad autorizada; ningún nodo conecta ambos conceptos"
   },
   {
    "consulta": "operador de cambio interviene entidad autorizada mercado",
    "resultado": "operador_de_cambio, casa_de_cambio, tipo_de_cambio... ningún nodo responde si el operador debe intervenir como entidad autorizada"
   },
   {
    "consulta": "quienes pueden operar en el mercado de cambios personas autorizadas BCRA",
    "resultado": "solo aparecen nodos de liquidación de fondos y 'personas jurídicas no autorizadas'; ninguno afirma que el operador de cambio sea/deba ser entidad autorizada"
   },
   {
    "consulta": "ver_vecinos entidad_autorizada",
    "resultado": "6 aristas (accede_a mercado_de_cambios, realiza pago_anticipado, SEPAIMPO...) con alcance de pagos anticipados de importaciones (p.140-142/Punto 10.4.2); 0 entrantes desde operador_de_cambio — no existe conexión"
   }
  ]
 }
]
```

**Tokens del caso (suma detectores 3 reps): in=981,684 · out=28,274**


---

## run_4/CQ-019 (`validacion_v61/off_run_4_CQ-019.json` + `_capa_d.json`)

**Voto v5.7 original (verbatim):**

```json
{
 "resultado": "mayoria",
 "flag_voto_dividido": false,
 "pares_primarios_ganadores": [
  [
   "context_recall",
   "navegación"
  ],
  [
   "context_recall",
   "navegación"
  ]
 ],
 "votos_ganadores": 2,
 "conteo": [
  {
   "pares_primarios": [
    [
     "context_recall",
     "navegación"
    ],
    [
     "context_recall",
     "navegación"
    ]
   ],
   "votos": 2
  },
  {
   "pares_primarios": [
    [
     "context_recall",
     "completitud_kg"
    ],
    [
     "noise_sensitivity",
     "aplicacion_erronea"
    ]
   ],
   "votos": 1
  }
 ],
 "desglose": [
  {
   "rep": 1,
   "pares_primarios": [
    [
     "context_recall",
     "completitud_kg"
    ],
    [
     "noise_sensitivity",
     "aplicacion_erronea"
    ]
   ],
   "formato_invalido": false
  },
  {
   "rep": 2,
   "pares_primarios": [
    [
     "context_recall",
     "navegación"
    ],
    [
     "context_recall",
     "navegación"
    ]
   ],
   "formato_invalido": false
  },
  {
   "rep": 3,
   "pares_primarios": [
    [
     "context_recall",
     "navegación"
    ],
    [
     "context_recall",
     "navegación"
    ]
   ],
   "formato_invalido": false
  }
 ]
}
```

**voto_pre_d6:**

```json
{
 "resultado": "mayoria",
 "flag_voto_dividido": false,
 "pares_primarios_ganadores": [
  [
   "context_recall",
   "navegación"
  ],
  [
   "context_recall",
   "navegación"
  ]
 ],
 "votos_ganadores": 2,
 "reps_validas": [
  1,
  2,
  3
 ],
 "conteo": [
  {
   "pares_primarios": [
    [
     "context_recall",
     "navegación"
    ],
    [
     "context_recall",
     "navegación"
    ]
   ],
   "votos": 2,
   "reps": [
    2,
    3
   ]
  },
  {
   "pares_primarios": [
    [
     "context_recall",
     "completitud_kg"
    ],
    [
     "noise_sensitivity",
     "aplicacion_erronea"
    ]
   ],
   "votos": 1,
   "reps": [
    1
   ]
  }
 ]
}
```

**voto_capa_d (final, post-D6):**

```json
{
 "resultado": "mayoria",
 "flag_voto_dividido": false,
 "pares_primarios_ganadores": [
  [
   "context_recall",
   "navegación"
  ],
  [
   "context_recall",
   "navegación"
  ]
 ],
 "votos_ganadores": 2,
 "reps_validas": [
  1,
  2,
  3
 ],
 "conteo": [
  {
   "pares_primarios": [
    [
     "context_recall",
     "navegación"
    ],
    [
     "context_recall",
     "navegación"
    ]
   ],
   "votos": 2,
   "reps": [
    2,
    3
   ]
  },
  {
   "pares_primarios": [
    [
     "context_recall",
     "completitud_kg"
    ],
    [
     "noise_sensitivity",
     "aplicacion_erronea"
    ]
   ],
   "votos": 1,
   "reps": [
    1
   ]
  }
 ]
}
```

**resumen_capa_d:** `{"reps_tocadas": [2, 3], "atribuciones_corregidas": 0, "discrepancias": 0, "triage": 4}`

**triage_capa_d (motivos y flags completos):**

```json
{
 "triage": true,
 "motivos": [
  "aplicacion_erronea_bajo_revision",
  "modulo_deterministico_sin_decision",
  "atribucion_no_verificable"
 ],
 "flags": [
  "R2: rep 1 atrib 1 (primaria) causa aplicacion_erronea",
  "R3: rep 1 atrib 1 — D3/sin_portador_extraible",
  "R6b: rep 1 atrib 2 — context_recall_sin_pata",
  "R3: rep 2 atrib 1 — D2/sin_portador_extraible",
  "R6b: rep 2 atrib 1 — context_recall_sin_pata",
  "R3: rep 2 atrib 2 — D2/sin_portador_extraible",
  "R6b: rep 2 atrib 2 — context_recall_sin_pata",
  "R2: rep 2 atrib 3 (secundaria) causa aplicacion_erronea",
  "R3: rep 2 atrib 3 — D3/sin_portador_extraible",
  "R3: rep 3 atrib 1 — D2/sin_portador_extraible",
  "R6b: rep 3 atrib 1 — context_recall_sin_pata",
  "R3: rep 3 atrib 2 — D2/sin_portador_extraible",
  "R6b: rep 3 atrib 2 — context_recall_sin_pata"
 ]
}
```

### Rep 1

- `formato_invalido`: `false` · `errores_formato`: `[]`
- `detectores`: `{"flag_encuadre_invertido": false, "flag_contexto": false, "tool_calls_usadas": 13, "max_tool_calls": 40, "tokens_in": 268108, "tokens_out": 8728}`
- longitudes: `razonamiento` = 3004 chars · `extraccion_traza` = 3928 chars

`atribuciones` ÍNTEGRAS (post-capa, con `capa_d`/`capa_d5`/`capa_d6`; la emisión original del LLM queda en los campos `emision_llm` donde la capa corrigió/degradó):

```json
[
 {
  "sintoma_capa1": "noise_sensitivity",
  "causa_capa2": "aplicacion_erronea",
  "lado": "agente",
  "jerarquia": "primaria",
  "pata": "Qué previsión no se deduce al computar los activos para la exigencia de capital por riesgo de crédito",
  "evidencia": {
   "afirmacion": {
    "quote": "La previsión específica es la que no se deduce al computar los activos para la exigencia de capital por riesgo de crédito. Según la normativa, el cálculo debe efectuarse sobre el monto bruto de la exposición, sin aplicar esta deducción contable.",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "Deducción contable que no se aplica al cálculo de KSA; el cálculo debe efectuarse sobre monto bruto de la exposición.",
    "ubicacion": "prevision_especifica (abierto por el agente, paso 4)"
   },
   "fuente": {
    "quote": "En los casos en los que la entidad haya constituido una previsión específica o tenga un descuento no reembolsable en el precio de compra de su exposición al conjunto de activos subyacentes, el cálculo de KSA deberá efectuarse usando el monto bruto de la exposición (…) Sección 3. Capital mínimo por riesgo de crédito. Titulizaciones e inversiones en fondos.",
    "ubicacion": "TO_capitales_minimos_actual.pdf, Punto 3.1.11.2, p.42"
   }
  },
  "busquedas": [
   {
    "consulta": "ver_nodo ksa",
    "resultado": "KSA = 'exigencia de capital promedio de las exposiciones subyacentes' — marcador explícito de titulizaciones que el agente abrió en paso 15 e ignoró"
   },
   {
    "consulta": "leer_pasaje_pdf Punto 3.1.11.2 y p.42",
    "resultado": "El punto pertenece a la Sección 3 'Capital mínimo por riesgo de crédito. Titulizaciones e inversiones en fondos'; la regla de no deducir la previsión específica aplica al cálculo de KSA en titulizaciones, no a la exigencia general por riesgo de crédito"
   }
  ],
  "capa_d": {
   "modulo": "D3",
   "accion": "sin_portador_extraible",
   "triage": true
  }
 },
 {
  "sintoma_capa1": "context_recall",
  "causa_capa2": "completitud_kg",
  "lado": "grafo",
  "jerarquia": "primaria",
  "pata": "Cómo se vincula esa regla con la clasificación de deudores (afirmación central: previsiones mínimas se determinan en función de la categoría)",
  "evidencia": {
   "afirmacion": {
    "quote": "las previsiones mínimas por riesgo de incobrabilidad se determinan en función de la categoría de clasificación asignada a cada deudor",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "Una de las cinco categorías en que se clasifica a cada cliente y la totalidad de sus financiaciones comprendidas.",
    "ubicacion": "categoria_de_clasificacion (paso 13) — no vincula categoría con determinación de previsiones mínimas"
   },
   "fuente": {
    "quote": "6.5. Niveles de clasificación. Cada cliente, y la totalidad de sus financiaciones comprendidas, se incluirá en una de las siguientes cinco categorías (…) el porcentaje establecido en el punto 2.2.5. de las normas sobre 'Previsiones mínimas por riesgo de incobrabilidad' correspondiente a la peor clasificación asignada",
    "ubicacion": "TO_clasificacion_deudores_actual.pdf, Punto 6.5, p.19"
   }
  },
  "busquedas": [
   {
    "consulta": "previsión mínima incobrabilidad categoría clasificación (paso 12, output completo)",
    "resultado": "categoria_de_clasificacion, prevision_por_riesgo_de_incobrabilidad (titulización), prevision_regulatoria, manual — NINGUNO porta la relación categoría→previsión mínima"
   },
   {
    "consulta": "previsiones mínimas por riesgo de incobrabilidad",
    "resultado": "previsiones_por_riesgo_de_incobrabilidad (cartera situación normal, límite 1,25% APR), insuficiencia_de_previsiones_minimas, prevision_regulatoria_por_riesgo_de_incobrabilidad — ninguno declara que la categoría determina el porcentaje de previsión mínima"
   },
   {
    "consulta": "porcentaje previsión según situación categoría normal riesgo",
    "resultado": "deudores_clasificados_en_situacion_normal (previsión no se deduce completamente), situacion_normal — no hay nodo que exprese la tabla/regla categoría→porcentaje de previsión mínima; el dato del PDF (norma 'Previsiones mínimas por riesgo de incobrabilidad', punto 2.2.5) no está representado como nodo alcanzable"
   }
  ],
  "capa_d": {
   "modulo": "D5",
   "accion": "sin_literales",
   "banderas": []
  },
  "capa_d6": {
   "regla": "R6b",
   "accion": "context_recall_sin_pata"
  }
 },
 {
  "sintoma_capa1": "faithfulness",
  "causa_capa2": "alucinacion_agente",
  "lado": "agente",
  "jerarquia": "secundaria",
  "pata": "Qué previsión no se deduce (glosa 'no se deduce del cálculo de capital (KSA)')",
  "evidencia": {
   "afirmacion": {
    "quote": "La previsión específica, aunque no se deduce en el cálculo de KSA (exigencia de capital promedio de exposiciones subyacentes) (…) aunque la previsión específica contable no se deduzca del cálculo de capital.",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "Exigencia de capital promedio de las exposiciones subyacentes, expresada como ratio entre la suma de exposiciones ponderadas por riesgo y la suma de exposiciones, multiplicado por 8%. Rango: 0% a 100%.",
    "ubicacion": "ksa (paso 15)"
   },
   "fuente": {
    "quote": "i) KSA. Es la exigencia de capital promedio de las exposiciones subyacentes (…) CAPITALES MÍNIMOS (…) Sección 3. Capital mínimo por riesgo de crédito. Titulizaciones e inversiones en fondos.",
    "ubicacion": "TO_capitales_minimos_actual.pdf, Punto 3.1.11.2, p.42"
   }
  },
  "busquedas": [
   {
    "consulta": "verificación KSA vs 'cálculo de capital' general",
    "resultado": "El agente equipara KSA (variable exclusiva de titulizaciones) con 'el cálculo de capital' por riesgo de crédito en general; el nodo ksa y el PDF acotan KSA a exposiciones subyacentes de titulizaciones, no soportan la generalización"
   }
  ],
  "capa_d": {
   "modulo": "D5",
   "accion": "sin_literales",
   "banderas": []
  }
 }
]
```

### Rep 2

- `formato_invalido`: `false` · `errores_formato`: `[]`
- `detectores`: `{"flag_encuadre_invertido": false, "flag_contexto": false, "tool_calls_usadas": 17, "max_tool_calls": 40, "tokens_in": 365749, "tokens_out": 10631}`
- longitudes: `razonamiento` = 2639 chars · `extraccion_traza` = 4224 chars

`atribuciones` ÍNTEGRAS (post-capa, con `capa_d`/`capa_d5`/`capa_d6`; la emisión original del LLM queda en los campos `emision_llm` donde la capa corrigió/degradó):

```json
[
 {
  "sintoma_capa1": "context_recall",
  "causa_capa2": "navegación",
  "lado": "agente",
  "jerarquia": "primaria",
  "pata": "Qué previsión por incobrabilidad no se deduce al computar los activos para la exigencia de capital por riesgo de crédito",
  "evidencia": {
   "afirmacion": {
    "quote": "Al computar los activos para la exigencia de capital por riesgo de crédito, la previsión específica es la que no se deduce. Según la normativa, el cálculo debe efectuarse sobre el monto bruto de la exposición, sin aplicar esta deducción contable.",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "Deudores cuya previsión por riesgo de incobrabilidad no se deduce completamente en el cálculo de conceptos comprendidos, conforme a los puntos 6.5.1 y 7.2.1 del TO sobre Clasificación de Deudores.",
    "ubicacion": "deudores_clasificados_en_situacion_normal (nodo portador de la respuesta; NUNCA apareció en la trayectoria del agente)"
   },
   "fuente": {
    "quote": "netos de las previsiones por riesgos de incobrabilidad ... y demás cuentas regularizadoras, sin deducir el 100% del importe de la previsión por riesgo de incobrabilidad correspondiente a la cartera de deudores clasificados “en situación normal” –puntos 6.5.1. y 7.2.1. del TO sobre Clasificación de Deudores– y a las financiaciones que se encuentran cubiertas con garantías preferidas A).",
    "ubicacion": "TO_capitales_minimos_actual.pdf, Punto 2.3.1 (p.7-10)"
   }
  },
  "busquedas": [
   {
    "consulta": "previsión situación normal cartera deudores no se deduce",
    "resultado": "PRIMER resultado: deudores_clasificados_en_situacion_normal (nodo portador de la respuesta correcta) — alcanzable con vocabulario ex ante de la pregunta"
   },
   {
    "consulta": "cómputo conceptos comprendidos previsión incobrabilidad",
    "resultado": "trae prevision_por_riesgo_de_incobrabilidad y prevision_regulatoria; el agente en paso 2 usó 'previsión incobrabilidad deducción activos' sin llegar a 'situación normal'"
   },
   {
    "consulta": "ver_paso_completo(2)",
    "resultado": "output íntegro del paso 2 confirma que deudores_clasificados_en_situacion_normal NO estaba entre los 10 resultados que vio el agente con su consulta"
   }
  ],
  "capa_d": {
   "modulo": "D2",
   "accion": "sin_portador_extraible",
   "triage": true
  },
  "capa_d6": {
   "regla": "R6b",
   "accion": "context_recall_sin_pata"
  }
 },
 {
  "sintoma_capa1": "context_recall",
  "causa_capa2": "navegación",
  "lado": "agente",
  "jerarquia": "primaria",
  "pata": "Cómo se vincula esa regla con la clasificación de deudores",
  "evidencia": {
   "afirmacion": {
    "quote": "las previsiones mínimas por riesgo de incobrabilidad se determinan en función de la categoría de clasificación asignada a cada deudor. De esta manera, la clasificación de deudores determina qué previsiones regulatorias mínimas deben constituirse, aunque la previsión específica contable no se deduzca del cálculo de capital.",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "Deudores cuya previsión por riesgo de incobrabilidad no se deduce completamente en el cálculo de conceptos comprendidos, conforme a los puntos 6.5.1 y 7.2.1 del TO sobre Clasificación de Deudores.",
    "ubicacion": "deudores_clasificados_en_situacion_normal (la vinculación correcta es directa: la categoría 'situación normal' es la que define qué previsión no se deduce; el agente nunca alcanzó este nodo)"
   },
   "fuente": {
    "quote": "sin deducir el 100% del importe de la previsión por riesgo de incobrabilidad correspondiente a la cartera de deudores clasificados “en situación normal” –puntos 6.5.1. y 7.2.1. del TO sobre Clasificación de Deudores–",
    "ubicacion": "TO_capitales_minimos_actual.pdf, Punto 2.3.1 (p.7-10)"
   }
  },
  "busquedas": [
   {
    "consulta": "previsión situación normal cartera deudores no se deduce",
    "resultado": "deudores_clasificados_en_situacion_normal — vincula explícitamente la no-deducción con la categoría de clasificación 'situación normal'; era alcanzable"
   }
  ],
  "capa_d": {
   "modulo": "D2",
   "accion": "sin_portador_extraible",
   "triage": true
  },
  "capa_d6": {
   "regla": "R6b",
   "accion": "context_recall_sin_pata"
  }
 },
 {
  "sintoma_capa1": "noise_sensitivity",
  "causa_capa2": "aplicacion_erronea",
  "lado": "agente",
  "jerarquia": "secundaria",
  "pata": "Qué previsión por incobrabilidad no se deduce al computar los activos para la exigencia de capital por riesgo de crédito",
  "evidencia": {
   "afirmacion": {
    "quote": "La previsión específica, aunque no se deduce en el cálculo de KSA (exigencia de capital promedio de exposiciones subyacentes) ... aunque la previsión específica contable no se deduzca del cálculo de capital.",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "Deducción contable que no se aplica al cálculo de KSA; el cálculo debe efectuarse sobre monto bruto de la exposición.",
    "ubicacion": "prevision_especifica (fiel al PDF pero su alcance es el régimen de titulizaciones/KSA, declarado en su propio contenido mediante 'KSA')"
   },
   "fuente": {
    "quote": "En los casos en los que la entidad haya constituido una previsión específica o tenga un descuento no reembolsable en el precio de compra de su exposición al conjunto de activos subyacentes, el cálculo de KSA deberá efectuarse usando el monto bruto de la exposición –es decir, sin deducir la previsión específica y/o el descuento no reembolsable en el precio de compra–.",
    "ubicacion": "TO_capitales_minimos_actual.pdf, Punto 3.1.11.2, inciso i) — Sección 3 'Capital mínimo por riesgo de crédito. Titulizaciones e inversiones en fondos'"
   }
  },
  "busquedas": [
   {
    "consulta": "leer_pasaje_pdf Punto 3.1.11.2",
    "resultado": "confirma que el 'no deducir previsión específica' es una regla del cálculo de KSA en titulizaciones, no del régimen general del Punto 2.3.1; el nodo prevision_especifica declara 'KSA' en su contenido, avisando su alcance"
   }
  ],
  "capa_d": {
   "modulo": "D3",
   "accion": "sin_portador_extraible",
   "triage": true
  }
 }
]
```

### Rep 3

- `formato_invalido`: `false` · `errores_formato`: `[]`
- `detectores`: `{"flag_encuadre_invertido": false, "flag_contexto": false, "tool_calls_usadas": 24, "max_tool_calls": 40, "tokens_in": 489462, "tokens_out": 10626}`
- longitudes: `razonamiento` = 2778 chars · `extraccion_traza` = 4021 chars

`atribuciones` ÍNTEGRAS (post-capa, con `capa_d`/`capa_d5`/`capa_d6`; la emisión original del LLM queda en los campos `emision_llm` donde la capa corrigió/degradó):

```json
[
 {
  "sintoma_capa1": "context_recall",
  "causa_capa2": "navegación",
  "lado": "agente",
  "jerarquia": "primaria",
  "pata": "Qué previsión por incobrabilidad no se deduce al computar los activos para la exigencia de capital por riesgo de crédito",
  "evidencia": {
   "afirmacion": {
    "quote": "La previsión específica es la que no se deduce al computar los activos para la exigencia de capital por riesgo de crédito.",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "Deudores cuya previsión por riesgo de incobrabilidad no se deduce completamente en el cálculo de conceptos comprendidos, conforme a los puntos 6.5.1 y 7.2.1 del TO sobre Clasificación de Deudores.",
    "ubicacion": "deudores_clasificados_en_situacion_normal (NO consultado por el agente; provenance: TO_capitales_minimos_actual.pdf p.7-10 / Punto 2.3.1)"
   },
   "fuente": {
    "quote": "netos de las previsiones por riesgos de incobrabilidad ... sin deducir el 100% del importe de la previsión por riesgo de incobrabilidad correspondiente a la cartera de deudores clasificados “en situación normal” –puntos 6.5.1. y 7.2.1. del TO sobre Clasificación de Deudores– y a las financiaciones que se encuentran cubiertas con garantías preferidas A).",
    "ubicacion": "TO_capitales_minimos_actual.pdf, Punto 2.3.1"
   }
  },
  "busquedas": [
   {
    "consulta": "deudores clasificados previsión incobrabilidad deducir",
    "resultado": "deudores_clasificados_en_situacion_normal aparece en 2º lugar; también previsiones_por_riesgos_de_incobrabilidad — nodos portadores de la respuesta correcta, alcanzables con vocabulario ex ante de la pregunta"
   },
   {
    "consulta": "situación normal previsión",
    "resultado": "deudores_clasificados_en_situacion_normal en 3er lugar"
   },
   {
    "consulta": "previsión incobrabilidad no se deduce exigencia capital riesgo crédito clasificación deudores",
    "resultado": "el nodo correcto NO aparece en top-15 con vocabulario literal de la pregunta (el label contiene 'situación normal', no presente literal en la pregunta), pero SÍ con los verbos 'deducir/incobrabilidad' de la propia pregunta"
   }
  ],
  "capa_d": {
   "modulo": "D2",
   "accion": "sin_portador_extraible",
   "triage": true
  },
  "capa_d6": {
   "regla": "R6b",
   "accion": "context_recall_sin_pata"
  }
 },
 {
  "sintoma_capa1": "context_recall",
  "causa_capa2": "navegación",
  "lado": "agente",
  "jerarquia": "primaria",
  "pata": "Cómo se vincula esa regla con la clasificación de deudores",
  "evidencia": {
   "afirmacion": {
    "quote": "las previsiones mínimas por riesgo de incobrabilidad se determinan en función de la categoría de clasificación asignada a cada deudor",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "Previsiones que se deducen del cálculo de conceptos comprendidos, incluyendo las contabilizadas en el pasivo, excepto el 100% de la previsión para deudores en situación normal.",
    "ubicacion": "previsiones_por_riesgos_de_incobrabilidad (NO consultado; provenance TO_capitales_minimos_actual.pdf p.7-10 / Punto 2.3.1)"
   },
   "fuente": {
    "quote": "sin deducir el 100% del importe de la previsión por riesgo de incobrabilidad correspondiente a la cartera de deudores clasificados “en situación normal” –puntos 6.5.1. y 7.2.1. del TO sobre Clasificación de Deudores–",
    "ubicacion": "TO_capitales_minimos_actual.pdf, Punto 2.3.1"
   }
  },
  "busquedas": [
   {
    "consulta": "deudores clasificados previsión incobrabilidad deducir",
    "resultado": "el vínculo real (la no-deducción se ancla en la clasificación 'en situación normal', puntos 6.5.1/7.2.1) está en nodos alcanzables no consultados; el agente construyó un vínculo genérico distinto (categoría → previsiones mínimas) que el PDF no funda para esta regla"
   }
  ],
  "capa_d": {
   "modulo": "D2",
   "accion": "sin_portador_extraible",
   "triage": true
  },
  "capa_d6": {
   "regla": "R6b",
   "accion": "context_recall_sin_pata"
  }
 }
]
```

**Tokens del caso (suma detectores 3 reps): in=1,123,319 · out=29,985**


---

## run_4/CQ-020 (`validacion_v61/off_run_4_CQ-020.json` + `_capa_d.json`)

**Voto v5.7 original (verbatim):**

```json
{
 "resultado": "mayoria",
 "flag_voto_dividido": false,
 "pares_primarios_ganadores": [],
 "votos_ganadores": 2,
 "conteo": [
  {
   "pares_primarios": [],
   "votos": 2
  },
  {
   "pares_primarios": [
    [
     "context_recall",
     "completitud_kg"
    ]
   ],
   "votos": 1
  }
 ],
 "desglose": [
  {
   "rep": 1,
   "pares_primarios": [],
   "formato_invalido": false
  },
  {
   "rep": 2,
   "pares_primarios": [
    [
     "context_recall",
     "completitud_kg"
    ]
   ],
   "formato_invalido": false
  },
  {
   "rep": 3,
   "pares_primarios": [],
   "formato_invalido": false
  }
 ]
}
```

**voto_pre_d6:**

```json
{
 "resultado": "mayoria",
 "flag_voto_dividido": false,
 "pares_primarios_ganadores": [],
 "votos_ganadores": 2,
 "reps_validas": [
  1,
  2,
  3
 ],
 "conteo": [
  {
   "pares_primarios": [],
   "votos": 2,
   "reps": [
    1,
    3
   ]
  },
  {
   "pares_primarios": [
    [
     "context_recall",
     "completitud_kg"
    ]
   ],
   "votos": 1,
   "reps": [
    2
   ]
  }
 ]
}
```

**voto_capa_d (final, post-D6):**

```json
{
 "resultado": "mayoria",
 "flag_voto_dividido": false,
 "pares_primarios_ganadores": [],
 "votos_ganadores": 2,
 "reps_validas": [
  1,
  2,
  3
 ],
 "conteo": [
  {
   "pares_primarios": [],
   "votos": 2,
   "reps": [
    1,
    3
   ]
  },
  {
   "pares_primarios": [
    [
     "context_recall",
     "completitud_kg"
    ]
   ],
   "votos": 1,
   "reps": [
    2
   ]
  }
 ]
}
```

**resumen_capa_d:** `{"reps_tocadas": [], "atribuciones_corregidas": 0, "discrepancias": 0, "triage": 0}`

**triage_capa_d (motivos y flags completos):**

```json
{
 "triage": true,
 "motivos": [
  "exoneracion_total"
 ],
 "flags": [
  "R1: voto_capa_d con mayoria de clave vacia (2 votos sin primarias)"
 ]
}
```

### Rep 1

- `formato_invalido`: `false` · `errores_formato`: `[]`
- `detectores`: `{"flag_encuadre_invertido": false, "flag_contexto": false, "tool_calls_usadas": 13, "max_tool_calls": 40, "tokens_in": 286393, "tokens_out": 7393}`
- longitudes: `razonamiento` = 2187 chars · `extraccion_traza` = 3725 chars

`atribuciones` ÍNTEGRAS (post-capa, con `capa_d`/`capa_d5`/`capa_d6`; la emisión original del LLM queda en los campos `emision_llm` donde la capa corrigió/degradó):

```json
[
 {
  "sintoma_capa1": "noise_sensitivity",
  "causa_capa2": "sin_defecto",
  "lado": "ninguno",
  "jerarquia": "sin_par",
  "pata": "Cómo se calcula la CRC (k vinculado a SEFYC)",
  "evidencia": {
   "afirmacion": {
    "quote": "k está vinculado a la calificación asignada por la SEFYC",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "Factor vinculado a la calificación asignada a la entidad según la evaluación efectuada por la SEFYC, con valores que varían de 1 a 1,19 según la calificación (1 a 5).",
    "ubicacion": "factor_k (resumen expuesto en paso 14; abierto en verificación)"
   },
   "fuente": {
    "quote": "k: factor vinculado a la calificación asignada a la entidad según la evaluación efectuada por la SEFYC, teniendo en cuenta la siguiente escala: Calificación asignada Valor de \"k\" 1 1  2 1,03  3 1,08  4 1,13  5 1,19",
    "ubicacion": "TO_capitales_minimos_actual.pdf, p.7-10 / Punto 2.1 Exigencia (Comunicación A 8171)"
   }
  }
 },
 {
  "sintoma_capa1": "noise_sensitivity",
  "causa_capa2": "sin_defecto",
  "lado": "ninguno",
  "jerarquia": "sin_par",
  "pata": "Cómo se calcula la CRC (valores de k)",
  "evidencia": {
   "afirmacion": {
    "quote": "k toma valores entre 1 y 1,19",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "Factor vinculado a la calificación asignada a la entidad según la evaluación efectuada por la SEFYC, con valores que varían de 1 a 1,19 según la calificación (1 a 5).",
    "ubicacion": "factor_k (resumen expuesto en paso 14)"
   },
   "fuente": {
    "quote": "Calificación asignada Valor de \"k\" 1 1  2 1,03  3 1,08  4 1,13  5 1,19",
    "ubicacion": "TO_capitales_minimos_actual.pdf, p.7-10 / Punto 2.1"
   }
  }
 },
 {
  "sintoma_capa1": "noise_sensitivity",
  "causa_capa2": "sin_defecto",
  "lado": "ninguno",
  "jerarquia": "sin_par",
  "pata": "Cómo se calcula la CRC (definición de APRC)",
  "evidencia": {
   "afirmacion": {
    "quote": "Los APRC se determinan mediante la suma de valores obtenidos aplicando ponderadores de riesgo a activos computables",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "Activos ponderados por riesgo de crédito, determinados mediante suma de valores obtenidos aplicando ponderadores de riesgo a activos computables, partidas fuera de balance, operaciones sin entrega contra pago...",
    "ubicacion": "aprc (resumen expuesto en paso 14; abierto en verificación)"
   },
   "fuente": {
    "quote": "APRC: activos ponderados por riesgo de crédito, determinados mediante la suma de los valores obtenidos luego de aplicar la siguiente expresión: A x p + PFB x CCF x p + no DvP + (DVP + RCD + INC(...)) x 12,5 donde: A: activos computables/exposiciones. ... p: ponderador de riesgo, en tanto por uno.",
    "ubicacion": "TO_capitales_minimos_actual.pdf, p.7-10 / Punto 2.1"
   }
  }
 },
 {
  "sintoma_capa1": "context_recall",
  "causa_capa2": "completitud_kg",
  "lado": "grafo",
  "jerarquia": "secundaria",
  "pata": "Con qué frecuencia se reporta la CRC al BCRA",
  "evidencia": {
   "afirmacion": {
    "quote": "Las entidades deben reportar información de capital en el régimen informativo contable mensual del BCRA, aunque no se especifica explícitamente si el reporte de la exigencia de CRC es mensual, trimestral u otra periodicidad",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "Información que se integra con datos referidos al mes bajo análisis, con excepciones para ciertos datos que tienen frecuencia trimestral.",
    "ubicacion": "informacion_de_frecuencia_mensual (genérico; no liga la periodicidad específicamente a la CRC)"
   },
   "fuente": {
    "quote": "REGIMEN INFORMATIVO CONTABLE MENSUAL B.C.R.A. 4. EXIGENCIA E INTEGRACIÓN DE CAPITALES MÍNIMOS (R.I.-C.M.)",
    "ubicacion": "TO_regimen_informativo_contable_mensual_actual.pdf, encabezado del TO (leído en Sección 3)"
   }
  },
  "busquedas": [
   {
    "consulta": "régimen informativo capitales mínimos RI-CM mensual",
    "resultado": "regímenes informativos cambiarios y nodos genéricos; ninguno liga explícitamente la periodicidad de reporte de la CRC"
   },
   {
    "consulta": "frecuencia presentación información contable BCRA",
    "resultado": "informacion_de_frecuencia_mensual / informacion_de_frecuencia_trimestral (genéricos, sin scope a la exigencia de CRC)"
   },
   {
    "consulta": "periodicidad reporte mensual trimestral capital (paso 13 del agente)",
    "resultado": "reporte_trimestral, balance_mensual, capital_minimo; ningún nodo con la periodicidad específica del reporte de la CRC"
   }
  ],
  "capa_d": {
   "modulo": "D5",
   "accion": "sin_literales",
   "banderas": []
  }
 }
]
```

### Rep 2

- `formato_invalido`: `false` · `errores_formato`: `[]`
- `detectores`: `{"flag_encuadre_invertido": false, "flag_contexto": false, "tool_calls_usadas": 11, "max_tool_calls": 40, "tokens_in": 278043, "tokens_out": 7334}`
- longitudes: `razonamiento` = 1986 chars · `extraccion_traza` = 3919 chars

`atribuciones` ÍNTEGRAS (post-capa, con `capa_d`/`capa_d5`/`capa_d6`; la emisión original del LLM queda en los campos `emision_llm` donde la capa corrigió/degradó):

```json
[
 {
  "sintoma_capa1": "noise_sensitivity",
  "causa_capa2": "sin_defecto",
  "lado": "ninguno",
  "jerarquia": "sin_par",
  "pata": "Cómo se calcula la exigencia de capital por riesgo de crédito (CRC)",
  "evidencia": {
   "afirmacion": {
    "quote": "k es el factor de calificación de entidad (vinculado a la calificación asignada por la SEFYC, con valores entre 1 y 1,19) (…) APRC son los activos ponderados por riesgo de crédito (determinados mediante la suma de valores obtenidos aplicando ponderadores de riesgo a activos computables)",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "Factor vinculado a la calificación asignada a la entidad según la evaluación efectuada por la SEFYC, con valores que varían de 1 a 1,19 según la calificación (1 a 5).",
    "ubicacion": "factor_k (expuesto en paso 14; abierto en verificación)"
   },
   "fuente": {
    "quote": "k: factor vinculado a la calificación asignada a la entidad según la evaluación efectuada por la SEFYC, teniendo en cuenta la siguiente escala: Calificación asignada Valor de \"k\" 1 1  2 1,03  3 1,08  4 1,13  5 1,19 (…) APRC: activos ponderados por riesgo de crédito, determinados mediante la suma de los valores obtenidos luego de aplicar la siguiente expresión: A x p + PFB x CCF x p + no DvP + (DVP + RCD + INC(inversiones significativas...)) x 12,5",
    "ubicacion": "TO_capitales_minimos_actual.pdf, p.7-10 / Punto 2.1 (Comunicación A 8171)"
   }
  },
  "busquedas": [
   {
    "consulta": "ver_nodo factor_k / aprc / crc",
    "resultado": "los tres nodos portan literalmente los datos afirmados por el agente"
   },
   {
    "consulta": "leer_pasaje_pdf p.7-10 TO_capitales_minimos",
    "resultado": "el PDF confirma fórmula, k vinculado a SEFYC 1 a 1,19 y APRC como suma de valores aplicando ponderadores a activos computables"
   }
  ]
 },
 {
  "sintoma_capa1": "context_recall",
  "causa_capa2": "completitud_kg",
  "lado": "grafo",
  "jerarquia": "primaria",
  "pata": "Con qué frecuencia se reporta la CRC al BCRA",
  "evidencia": {
   "afirmacion": {
    "quote": "las entidades deben reportar información de capital en el régimen informativo contable mensual del BCRA, aunque no se especifica explícitamente si el reporte de la exigencia de CRC es mensual, trimestral u otra periodicidad",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "Exigencia de capital que las entidades financieras deben mantener, calculada mediante una fórmula que considera activos ponderados por riesgo de crédito e incrementos normativos.",
    "ubicacion": "exigencia_por_riesgo_de_credito (ningún nodo del grafo afirma la periodicidad del reporte del CRC)"
   },
   "fuente": {
    "quote": "REGIMEN INFORMATIVO CONTABLE MENSUAL B.C.R.A. 4. EXIGENCIA E INTEGRACIÓN DE CAPITALES MÍNIMOS (R.I.-C.M.)",
    "ubicacion": "TO_regimen_informativo_contable_mensual_actual.pdf, Sección 3 / p.47 (encabezado del régimen)"
   }
  },
  "busquedas": [
   {
    "consulta": "frecuencia reporte exigencia capital riesgo crédito régimen informativo",
    "resultado": "362 matches; ninguno porta la periodicidad del reporte del CRC"
   },
   {
    "consulta": "presentación mensual capitales mínimos entidades financieras BCRA",
    "resultado": "87 matches; nodos sobre entidades y exposiciones, ninguno con la periodicidad de reporte"
   },
   {
    "consulta": "RI-CM exigencia integración capitales mínimos mensual",
    "resultado": "58 matches; balance_mensual, total_integracion, consolidado_mensual — ninguno afirma que el CRC se reporte con periodicidad mensual"
   }
  ],
  "capa_d": {
   "modulo": "D5",
   "accion": "sin_literales",
   "banderas": []
  }
 }
]
```

### Rep 3

- `formato_invalido`: `false` · `errores_formato`: `[]`
- `detectores`: `{"flag_encuadre_invertido": false, "flag_contexto": false, "tool_calls_usadas": 12, "max_tool_calls": 40, "tokens_in": 284599, "tokens_out": 7581}`
- longitudes: `razonamiento` = 2615 chars · `extraccion_traza` = 4071 chars

`atribuciones` ÍNTEGRAS (post-capa, con `capa_d`/`capa_d5`/`capa_d6`; la emisión original del LLM queda en los campos `emision_llm` donde la capa corrigió/degradó):

```json
[
 {
  "sintoma_capa1": "noise_sensitivity",
  "causa_capa2": "sin_defecto",
  "lado": "ninguno",
  "jerarquia": "sin_par",
  "pata": "Cómo se calcula la exigencia de capital por riesgo de crédito (CRC) — subclaims k↔SEFYC, k∈[1;1,19], APRC",
  "evidencia": {
   "afirmacion": {
    "quote": "k es el factor de calificación de entidad (vinculado a la calificación asignada por la SEFYC, con valores entre 1 y 1,19) (...) APRC son los activos ponderados por riesgo de crédito (determinados mediante la suma de valores obtenidos aplicando ponderadores de riesgo a activos computables)",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "Factor vinculado a la calificación asignada a la entidad según la evaluación efectuada por la SEFYC, con valores que varían de 1 a 1,19 según la calificación (1 a 5).",
    "ubicacion": "factor_k (expuesto en paso 14 buscar_nodos; abierto con ver_nodo)"
   },
   "fuente": {
    "quote": "k: factor vinculado a la calificación asignada a la entidad según la evaluación efectuada por la SEFYC, teniendo en cuenta la siguiente escala: Calificación asignada Valor de \"k\" 1 1  2 1,03  3 1,08  4 1,13  5 1,19 (...) APRC: activos ponderados por riesgo de crédito, determinados mediante la suma de los valores obtenidos luego de aplicar la siguiente expresión: A x p + PFB x CCF x p + no DvP + ...",
    "ubicacion": "TO_capitales_minimos_actual.pdf, p.7-10 / Punto 2.1"
   }
  },
  "busquedas": [
   {
    "consulta": "ver_nodo factor_k",
    "resultado": "contiene textual 'vinculado a la calificación asignada... por la SEFYC, con valores que varían de 1 a 1,19' — soporta los dos claims marcados no_soportado"
   },
   {
    "consulta": "ver_nodo aprc",
    "resultado": "'determinados mediante suma de valores obtenidos aplicando ponderadores de riesgo a activos computables' — soporta el claim de APRC"
   },
   {
    "consulta": "leer_pasaje_pdf p.7-10 Punto 2.1",
    "resultado": "PDF confirma escala k 1→1, 5→1,19, vínculo SEFYC y definición de APRC; los tres claims son fácticamente correctos"
   }
  ]
 },
 {
  "sintoma_capa1": "noise_sensitivity",
  "causa_capa2": "sin_defecto",
  "lado": "ninguno",
  "jerarquia": "sin_par",
  "pata": "Con qué frecuencia se reporta la CRC al BCRA",
  "evidencia": {
   "afirmacion": {
    "quote": "las entidades deben reportar información de capital en el régimen informativo contable mensual del BCRA",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "Exigencia de capital que las entidades financieras deben mantener, calculada mediante una fórmula que considera activos ponderados por riesgo de crédito e incrementos normativos.  provenances: TO_regimen_informativo_contable_mensual_actual.pdf p.1-5 / Sección 3, punto 3.1.2",
    "ubicacion": "exigencia_por_riesgo_de_credito (abierto en paso 4)"
   },
   "fuente": {
    "quote": "REGIMEN INFORMATIVO CONTABLE MENSUAL  B.C.R.A. 4. EXIGENCIA E INTEGRACION DE CAPITALES MINIMOS (R.I. – C.M.) (...) Posición mes n: Datos exigencia riesgo de crédito del mes n (incluyendo INC)",
    "ubicacion": "TO_regimen_informativo_contable_mensual_actual.pdf, Sección 7.1"
   }
  },
  "busquedas": [
   {
    "consulta": "régimen informativo contable mensual capitales mínimos",
    "resultado": "no existe un nodo dedicado que declare la periodicidad de reporte de la CRC; el dato surge del nombre del documento fuente (RI Contable Mensual) y su cap. 4 sobre Exigencia e Integración de Capitales Mínimos"
   },
   {
    "consulta": "leer_pasaje_pdf RI-CM Sección 7.1",
    "resultado": "el régimen informativo contable MENSUAL maneja 'Datos exigencia riesgo de crédito del mes n' — confirma que el reporte de la CRC es mensual; el claim del agente es correcto"
   }
  ]
 }
]
```

**Tokens del caso (suma detectores 3 reps): in=849,035 · out=22,308**


---

## Tabla de inventario

| Caso | Reps válidas | Voto v5.7 | voto_capa_d final | Motivos triage | Reglas D6 por rep | Tokens in |
|---|---|---|---|---|---|---|
| run_2/CQ-015 | 3/3 | mayoria/[] | mayoria/[]/votos=2 | ["exoneracion_total", "atribucion_sin_sintoma"] | r1: ['atribucion_sin_sintoma'] · r2: ['atribucion_sin_sintoma'] · r3: ['atribucion_sin_sintoma'] | 261,089 |
| run_2/CQ-018 | 3/3 | mayoria/[["noise_sensitivity", "contenido_kg"]] | mayoria/[["noise_sensitivity", "contenido_kg"]]/votos=2 | ["atribucion_no_verificable"] | r1: ['claim_no_mapeado'] · r2: ['claim_no_mapeado'] · r3: ['claim_no_mapeado'] | 885,646 |
| run_2/CQ-019 | 3/3 | mayoria/[["context_recall", "navegación"], ["context_recall", "navegación"]] | mayoria/[["context_recall", "navegación"], ["context_recall", "navegación"]]/votos=2 | ["atribucion_no_verificable", "modulo_deterministico_sin_decision"] | r1: ['claim_no_mapeado', 'claim_no_mapeado'] · r2: — · r3: — | 771,888 |
| run_2/CQ-025 | 3/3 | mayoria/[["context_recall", "navegación"]] | mayoria/[["context_recall", "alcanzabilidad_kg"]]/votos=3 | ["atribucion_no_verificable", "aplicacion_erronea_bajo_revision"] | r1: ['context_recall_sin_pata'] · r2: ['context_recall_sin_pata'] · r3: ['context_recall_sin_pata'] | 770,956 |
| run_4/CQ-014 | 3/3 | mayoria/[] | mayoria/[]/votos=3 | ["exoneracion_total"] | r1: — · r2: — · r3: — | 253,095 |
| run_4/CQ-017 | 3/3 | mayoria/[["context_recall", "estructural_kg"]] | mayoria/[["context_recall", "estructural_kg"]]/votos=2 | [] | r1: — · r2: — · r3: — | 981,684 |
| run_4/CQ-019 | 3/3 | mayoria/[["context_recall", "navegación"], ["context_recall", "navegación"]] | mayoria/[["context_recall", "navegación"], ["context_recall", "navegación"]]/votos=2 | ["aplicacion_erronea_bajo_revision", "modulo_deterministico_sin_decision", "atribucion_no_verificable"] | r1: ['context_recall_sin_pata'] · r2: ['context_recall_sin_pata', 'context_recall_sin_pata'] · r3: ['context_recall_sin_pata', 'context_recall_sin_pata'] | 1,123,319 |
| run_4/CQ-020 | 3/3 | mayoria/[] | mayoria/[]/votos=2 | ["exoneracion_total"] | r1: — · r2: — · r3: — | 849,035 |

**Costo real total (suma de `detectores` de las 24 reps): input = 5,896,712 · output = 187,266 tokens.**

**Tokens out por caso:** run_2/CQ-015=12,621 · run_2/CQ-018=31,062 · run_2/CQ-019=27,759 · run_2/CQ-025=23,144 · run_4/CQ-014=12,113 · run_4/CQ-017=28,274 · run_4/CQ-019=29,985 · run_4/CQ-020=22,308

---

*Fin de la extracción. Los 16 JSONs quedan congelados en `posthoc_run/validacion_v61/`. El
scoring contra la vara de la validación es adjudicación externa. Frenado para revisión.*
