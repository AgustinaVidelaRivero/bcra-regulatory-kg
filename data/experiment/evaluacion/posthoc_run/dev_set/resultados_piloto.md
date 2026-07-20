# Resultados del piloto v6.0-D — reporte de EXTRACCIÓN (sin scoring)

Fecha: 2026-07-16. **Corrida ÚNICA** del compuesto bajo `docs/protocolo_piloto_v6.md` +
Enmienda v1.1 (§5: se corre una vez y se lee, cualquiera sea el resultado). **Este reporte NO
scorea**: no compara contra la vara del piloto ni menciona sus GTs — el scoring es
adjudicación externa. Los JSONs (originales y `_capa_d`) quedan **congelados** en
`posthoc_run/piloto_v6/`.

## 1. Constancia de la guarda (PASO 0), comandos y costo real

**Guarda (previa a toda ejecución) — PASA:**

```
$ git log --oneline -1 -- .claude/skills/kg-refinement/references/casos_piloto.md
030c4cb vara del piloto v1 (casos_piloto.md, marco post-hoc, taxonomía v2.6.1) — adjudicada ANTES de cualquier corrida (sellado por inexistencia): [...] Habilita la corrida única del compuesto (guarda del protocolo).

$ git log --oneline -1
030c4cb vara del piloto v1 [...]        <- el commit de casos_piloto.md ES HEAD

$ git status
On branch main
nothing to commit, working tree clean
```

**PASO 1 — comando ejecutado (verificador v5.7 congelado, régimen de operación):**

```
$ cd data/experiment/evaluacion
$ python verificador.py --n 3 \
    --casos "off/run_3/CQ-016,off/run_3/CQ-018,off/run_3/CQ-019,off/run_3/CQ-024,off/run_3/CQ-033" \
    --out posthoc_run/piloto_v6/
```

Log completo del runner (corrida única, 5 casos × 3 reps, **cero fallas operativas** — sin
429, sin timeouts, sin formato_invalido; exit 0):

```
[runner] investigando off/run_3/CQ-016 · rep 1/3 (cv=verificador-v5.7-rep1) …
[runner] investigando off/run_3/CQ-016 · rep 2/3 (cv=verificador-v5.7-rep2) …
[runner] investigando off/run_3/CQ-016 · rep 3/3 (cv=verificador-v5.7-rep3) …
[runner]   → off_run_3_CQ-016.json · voto=frontera_no_determinada · dividido=True · ganadores=None · conteo=[1, 1, 1]
[runner] investigando off/run_3/CQ-018 · rep 1/3 (cv=verificador-v5.7-rep1) …
[runner] investigando off/run_3/CQ-018 · rep 2/3 (cv=verificador-v5.7-rep2) …
[runner] investigando off/run_3/CQ-018 · rep 3/3 (cv=verificador-v5.7-rep3) …
[runner]   → off_run_3_CQ-018.json · voto=mayoria · dividido=False · ganadores=[['noise_sensitivity', 'contenido_kg']] · conteo=[2, 1]
[runner] investigando off/run_3/CQ-019 · rep 1/3 (cv=verificador-v5.7-rep1) …
[runner] investigando off/run_3/CQ-019 · rep 2/3 (cv=verificador-v5.7-rep2) …
[runner] investigando off/run_3/CQ-019 · rep 3/3 (cv=verificador-v5.7-rep3) …
[runner]   → off_run_3_CQ-019.json · voto=mayoria · dividido=False · ganadores=[] · conteo=[3]
[runner] investigando off/run_3/CQ-024 · rep 1/3 (cv=verificador-v5.7-rep1) …
[runner] investigando off/run_3/CQ-024 · rep 2/3 (cv=verificador-v5.7-rep2) …
[runner] investigando off/run_3/CQ-024 · rep 3/3 (cv=verificador-v5.7-rep3) …
[runner]   → off_run_3_CQ-024.json · voto=mayoria · dividido=False · ganadores=[['context_recall', 'alcanzabilidad_kg']] · conteo=[2, 1]
[runner] investigando off/run_3/CQ-033 · rep 1/3 (cv=verificador-v5.7-rep1) …
[runner] investigando off/run_3/CQ-033 · rep 2/3 (cv=verificador-v5.7-rep2) …
[runner] investigando off/run_3/CQ-033 · rep 3/3 (cv=verificador-v5.7-rep3) …
[runner]   → off_run_3_CQ-033.json · voto=mayoria · dividido=False · ganadores=[['noise_sensitivity', 'contenido_kg']] · conteo=[2, 1]
```

**PASO 2 — capa determinística (compuesto v6.0-D) sobre cada JSON emitido:**

```
$ python capa_deterministica.py --caso posthoc_run/piloto_v6/off_run_3_<CQ>.json --run run_3 \
    --trace posthoc_run/traces/off/run_3/<CQ>.json --out posthoc_run/piloto_v6/off_run_3_<CQ>_capa_d.json
CQ-016: exit 0 · CQ-018: exit 0 · CQ-019: exit 0 · CQ-024: exit 0 · CQ-033: exit 0
```

**Costo real medido (suma de `detectores.tokens_in/out` de las 15 reps, registrados desde la
API vía la caché de captura):**

| Caso | Tokens in | Tokens out |
|---|---|---|
| CQ-016 | 692.774 | 27.389 |
| CQ-018 | 1.159.166 | 27.019 |
| CQ-019 | 495.524 | 15.072 |
| CQ-024 | 1.438.572 | 32.894 |
| CQ-033 | 393.636 | 18.807 |
| **TOTAL** | **4.179.672** | **121.181** |

(4,18M de input vs. ~6M estimados en el protocolo — la estimación fue conservadora.)

## 2. Extracción por caso (verbatim; sin scoring)

Nota de lectura: las `atribuciones` pegadas por rep son las del JSON `_capa_d` — ÍNTEGRAS,
con las anotaciones `capa_d`/`capa_d5` de los módulos; donde D2 corrigió una causa, la
emisión original del LLM queda en `capa_d.emision_llm`. `formato_invalido`,
`errores_formato` y `detectores` son del JSON original del verificador (idénticos en ambos).

---

## CQ-016 (`piloto_v6/off_run_3_CQ-016.json` + `_capa_d.json`)

**Voto v5.7 original (verbatim):**

```json
{
 "resultado": "frontera_no_determinada",
 "flag_voto_dividido": true,
 "pares_primarios_ganadores": null,
 "votos_ganadores": null,
 "conteo": [
  {
   "pares_primarios": [],
   "votos": 1
  },
  {
   "pares_primarios": [
    [
     "context_recall",
     "estructural_kg"
    ]
   ],
   "votos": 1
  },
  {
   "pares_primarios": [
    [
     "faithfulness",
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
     "estructural_kg"
    ]
   ],
   "formato_invalido": false
  },
  {
   "rep": 3,
   "pares_primarios": [
    [
     "faithfulness",
     "completitud_kg"
    ]
   ],
   "formato_invalido": false
  }
 ]
}
```

**voto_capa_d:**

```json
{
 "resultado": "frontera_no_determinada",
 "flag_voto_dividido": true,
 "pares_primarios_ganadores": null,
 "votos_ganadores": null,
 "reps_validas": [
  1,
  2,
  3
 ],
 "conteo": [
  {
   "pares_primarios": [],
   "votos": 1,
   "reps": [
    1
   ]
  },
  {
   "pares_primarios": [
    [
     "context_recall",
     "estructural_kg"
    ]
   ],
   "votos": 1,
   "reps": [
    2
   ]
  },
  {
   "pares_primarios": [
    [
     "faithfulness",
     "completitud_kg"
    ]
   ],
   "votos": 1,
   "reps": [
    3
   ]
  }
 ]
}
```

**resumen_capa_d:** `{"reps_tocadas": [], "atribuciones_corregidas": 0, "discrepancias": 0, "triage": 0}`

**triage_capa_d:**

```json
{
 "triage": true,
 "motivos": [
  "voto_dividido"
 ],
 "flags": [
  "R4: voto_capa_d.flag_voto_dividido = true"
 ]
}
```

### Rep 1

- `formato_invalido`: `false` · `errores_formato`: `[]`
- `detectores`: `{"flag_encuadre_invertido": false, "flag_contexto": false, "tool_calls_usadas": 6, "max_tool_calls": 40, "tokens_in": 167816, "tokens_out": 5695}`
- longitudes: `razonamiento` = 2332 chars · `extraccion_traza` = 3848 chars

`atribuciones` ÍNTEGRAS (post-capa; incluye `capa_d`/`capa_d5` donde la capa anotó — la emisión original del LLM queda registrada en `capa_d.emision_llm` cuando D2 corrigió):

```json
[
 {
  "sintoma_capa1": "noise_sensitivity",
  "causa_capa2": "sin_defecto",
  "lado": "ninguno",
  "jerarquia": "sin_par",
  "pata": "Ambas patas (unidad y decimales)",
  "evidencia": {
   "afirmacion": {
    "quote": "los importes en el régimen informativo se registran en miles de pesos, sin decimales. (...) La norma sobre registro en miles de pesos sin decimales está documentada en el Régimen Informativo Contable Mensual (Punto 1.2).",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "Los importes se registrarán en miles de pesos, sin decimales",
    "ubicacion": "Restriccion_los_importes_se_registraran_en_miles_de_pesos_sin_decimales (abierto por el agente en paso 3)"
   },
   "fuente": {
    "quote": "1.2. Los importes se registrarán en miles de pesos, sin decimales. (...) REGIMEN INFORMATIVO CONTABLE MENSUAL B.C.R.A. 4. EXIGENCIA E INTEGRACIÓN DE CAPITALES MÍNIMOS (R.I.-C.M.) Sección 1. Instrucciones generales",
    "ubicacion": "TO_regimen_informativo_contable_mensual_actual.pdf, Punto 1.2"
   }
  },
  "busquedas": [
   {
    "consulta": "exigencia integración capitales mínimos régimen informativo importes",
    "resultado": "El nodo Restriccion...miles_de_pesos_sin_decimales y el TextoOrdenado del RICM aparecen; el dato pertinente es alcanzable"
   },
   {
    "consulta": "leer_pasaje_pdf Punto 1.2 y Sección 1 del RICM",
    "resultado": "Confirma que el Punto 1.2 es la instrucción general del capítulo '4. EXIGENCIA E INTEGRACIÓN DE CAPITALES MÍNIMOS (R.I.-C.M.)' — o sea, el régimen exacto de la pregunta"
   }
  ]
 }
]
```

### Rep 2

- `formato_invalido`: `false` · `errores_formato`: `[]`
- `detectores`: `{"flag_encuadre_invertido": false, "flag_contexto": false, "tool_calls_usadas": 9, "max_tool_calls": 40, "tokens_in": 267159, "tokens_out": 13198}`
- longitudes: `razonamiento` = 2465 chars · `extraccion_traza` = 3448 chars

`atribuciones` ÍNTEGRAS (post-capa; incluye `capa_d`/`capa_d5` donde la capa anotó — la emisión original del LLM queda registrada en `capa_d.emision_llm` cuando D2 corrigió):

```json
[
 {
  "sintoma_capa1": "context_recall",
  "causa_capa2": "estructural_kg",
  "lado": "grafo",
  "jerarquia": "primaria",
  "pata": "Identificación del régimen consultado como 'Régimen Informativo de Exigencia e Integración de Capitales Mínimos'",
  "evidencia": {
   "afirmacion": {
    "quote": "no se encontró en el grafo una especificación explícita y separada para un 'Régimen Informativo de Exigencia e Integración de Capitales Mínimos' como entidad diferenciada",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "label=\"Régimen Informativo Contable Mensual\"; materia: Información contable y regulatoria mensual; archivo: TO_regimen_informativo_contable_mensual_actual.pdf",
    "ubicacion": "TextoOrdenado_to_regimen_informativo_contable_mensual_actual_pdf"
   },
   "fuente": {
    "quote": "REGIMEN INFORMATIVO CONTABLE MENSUAL B.C.R.A. 4. EXIGENCIA E INTEGRACIÓN DE CAPITALES MÍNIMOS (R.I.-C.M.) Sección 1. Instrucciones generales",
    "ubicacion": "TO_regimen_informativo_contable_mensual_actual.pdf, Punto 1.2 / Sección 1"
   }
  },
  "busquedas": [
   {
    "consulta": "R.I.-C.M. exigencia integración capitales mínimos régimen informativo instrucciones generales",
    "resultado": "236 matches; TO 'Régimen Informativo Contable Mensual' con label genérico y nodos de operaciones/obligaciones de capitales, pero NINGÚN nodo/arista que declare que ese régimen = 'Régimen Informativo de Exigencia e Integración de Capitales Mínimos (R.I.-C.M.)'"
   },
   {
    "consulta": "informar exigencia integración capitales mínimos mensual",
    "resultado": "233 matches; obligaciones de informar exigencia por riesgo, CRO, etc., pero ninguna conecta la unidad/decimales del Punto 1.2 con el régimen de capitales mínimos"
   },
   {
    "consulta": "régimen informativo exigencia integración capitales mínimos importes",
    "resultado": "171 matches; sin nodo puente que identifique el R.I.-C.M. como el régimen de la pregunta"
   }
  ]
 },
 {
  "sintoma_capa1": "noise_sensitivity",
  "causa_capa2": "sin_defecto",
  "lado": "ninguno",
  "jerarquia": "sin_par",
  "pata": "Unidad (miles de pesos) y decimales (sin decimales)",
  "evidencia": {
   "afirmacion": {
    "quote": "los importes en el régimen informativo se registran en miles de pesos, sin decimales",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "Los importes se registrarán en miles de pesos, sin decimales",
    "ubicacion": "Restriccion_los_importes_se_registraran_en_miles_de_pesos_sin_decimales"
   },
   "fuente": {
    "quote": "1.2. Los importes se registrarán en miles de pesos, sin decimales.",
    "ubicacion": "TO_regimen_informativo_contable_mensual_actual.pdf, Punto 1.2"
   }
  },
  "busquedas": [
   {
    "consulta": "leer Punto 1.2 del régimen informativo contable mensual",
    "resultado": "El Punto 1.2 pertenece a la Sección 1 'Instrucciones generales' del régimen titulado '4. EXIGENCIA E INTEGRACIÓN DE CAPITALES MÍNIMOS (R.I.-C.M.)' — el dato es exactamente el pertinente a la pregunta; ambas patas centrales son correctas y el juez las aprobó"
   }
  ]
 }
]
```

### Rep 3

- `formato_invalido`: `false` · `errores_formato`: `[]`
- `detectores`: `{"flag_encuadre_invertido": false, "flag_contexto": false, "tool_calls_usadas": 10, "max_tool_calls": 40, "tokens_in": 257799, "tokens_out": 8496}`
- longitudes: `razonamiento` = 2302 chars · `extraccion_traza` = 3270 chars

`atribuciones` ÍNTEGRAS (post-capa; incluye `capa_d`/`capa_d5` donde la capa anotó — la emisión original del LLM queda registrada en `capa_d.emision_llm` cuando D2 corrigió):

```json
[
 {
  "sintoma_capa1": "faithfulness",
  "causa_capa2": "completitud_kg",
  "lado": "grafo",
  "jerarquia": "primaria",
  "pata": "Ambas patas (unidad y decimales) referidas al 'Régimen Informativo de Exigencia e Integración de Capitales Mínimos'",
  "evidencia": {
   "afirmacion": {
    "quote": "no se encontró en el grafo una especificación explícita y separada para un 'Régimen Informativo de Exigencia e Integración de Capitales Mínimos' como entidad diferenciada",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "materia: Información contable y regulatoria mensual; archivo: TO_regimen_informativo_contable_mensual_actual.pdf; version: actual",
    "ubicacion": "TextoOrdenado_to_regimen_informativo_contable_mensual_actual_pdf"
   },
   "fuente": {
    "quote": "REGIMEN INFORMATIVO CONTABLE MENSUAL B.C.R.A. 4. EXIGENCIA E INTEGRACIÓN DE CAPITALES MÍNIMOS (R.I.-C.M.) Sección 1. Instrucciones generales",
    "ubicacion": "TO_regimen_informativo_contable_mensual_actual.pdf, Punto 1.2 (pág 3)"
   }
  },
  "busquedas": [
   {
    "consulta": "R.I.-C.M. exigencia integración capitales mínimos instrucciones generales",
    "resultado": "No aparece ningún nodo que declare que el Régimen Informativo Contable Mensual (o su Sección/capítulo de Instrucciones generales) corresponde a 'Exigencia e Integración de Capitales Mínimos'; solo el TextoOrdenado con materia genérica y nodos de exigencia por riesgo"
   },
   {
    "consulta": "exigencia integración capitales mínimos régimen informativo miles pesos",
    "resultado": "La Restriccion de miles/decimales y el TextoOrdenado del régimen aparecen por separado; ninguna arista ni nodo los vincula con 'capitales mínimos'"
   },
   {
    "consulta": "ver_vecinos Restriccion_...miles_de_pesos_sin_decimales (salientes/entrantes)",
    "resultado": "salientes: establecida_en→Régimen Informativo Contable Mensual, aplica_a→Sujetos obligados, limita→Registro de importes; entrantes: 0. Ninguna conexión con capitales mínimos / R.I.-C.M."
   }
  ],
  "capa_d": {
   "modulo": "D5",
   "accion": "sin_literales",
   "banderas": []
  }
 },
 {
  "sintoma_capa1": "noise_sensitivity",
  "causa_capa2": "sin_defecto",
  "lado": "ninguno",
  "jerarquia": "sin_par",
  "pata": "Claims centrales de unidad ('miles de pesos') y decimales ('sin decimales')",
  "evidencia": {
   "afirmacion": {
    "quote": "los importes en el régimen informativo se registran en miles de pesos, sin decimales",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "Los importes se registrarán en miles de pesos, sin decimales",
    "ubicacion": "Restriccion_los_importes_se_registraran_en_miles_de_pesos_sin_decimales"
   },
   "fuente": {
    "quote": "1.2. Los importes se registrarán en miles de pesos, sin decimales.",
    "ubicacion": "TO_regimen_informativo_contable_mensual_actual.pdf, Punto 1.2 (pág 3)"
   }
  },
  "busquedas": []
 }
]
```

**Tokens del caso (suma de detectores de las 3 reps): in=692,774 · out=27,389**


---

## CQ-018 (`piloto_v6/off_run_3_CQ-018.json` + `_capa_d.json`)

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
     "contenido_kg"
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
     "contenido_kg"
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

**voto_capa_d:**

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
     "contenido_kg"
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

**triage_capa_d:**

```json
{
 "triage": false,
 "motivos": [],
 "flags": []
}
```

### Rep 1

- `formato_invalido`: `false` · `errores_formato`: `[]`
- `detectores`: `{"flag_encuadre_invertido": false, "flag_contexto": false, "tool_calls_usadas": 13, "max_tool_calls": 40, "tokens_in": 351556, "tokens_out": 9021}`
- longitudes: `razonamiento` = 2227 chars · `extraccion_traza` = 3679 chars

`atribuciones` ÍNTEGRAS (post-capa; incluye `capa_d`/`capa_d5` donde la capa anotó — la emisión original del LLM queda registrada en `capa_d.emision_llm` cuando D2 corrigió):

```json
[
 {
  "sintoma_capa1": "noise_sensitivity",
  "causa_capa2": "contenido_kg",
  "lado": "grafo",
  "jerarquia": "primaria",
  "pata": "¿Bajo qué criterio clasifican a sus deudores? (proveedores no financieros)",
  "evidencia": {
   "afirmacion": {
    "quote": "El criterio básico utilizado para efectuar la clasificación es la capacidad de pago en el futuro de la deuda o de los compromisos objeto de la garantía.",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "El criterio básico a ser utilizado para efectuar la clasificación es la capacidad de pago en el futuro de la deuda o de los compromisos objeto de la garantía de la entidad financiera",
    "ubicacion": "Obligacion_evaluar_capacidad_de_pago (abierto por el agente en paso 13)"
   },
   "fuente": {
    "quote": "10.1. Proveedores no financieros de crédito. Las empresas no financieras emisoras de tarjetas de crédito y/o compra y los otros proveedores no financieros de crédito (…) deberán clasificar a los respectivos deudores en función de su mora, según los criterios aplicables para la cartera de 'consumo o vivienda' (…). 7.1. Criterio de clasificación. (…) la clasificación de estos clientes se efectuará considerando -al cabo de cada mes- exclusivamente pautas objetivas vinculadas al grado de cumplimiento de las correspondientes obligaciones (…)",
    "ubicacion": "TO_clasificacion_deudores_actual.pdf, Puntos 10.1 y 7.1"
   }
  },
  "busquedas": [
   {
    "consulta": "leer_pasaje 4.2 criterio básico de clasificación",
    "resultado": "el criterio de capacidad de pago futuro pertenece al criterio general/cartera comercial, no al régimen de proveedores no financieros"
   },
   {
    "consulta": "leer_pasaje 7.1 criterio de clasificación cartera consumo/vivienda",
    "resultado": "la clasificación de la cartera consumo/vivienda (aplicable a proveedores no financieros vía 10.1) se hace exclusivamente por pautas objetivas de mora, no por capacidad de pago futuro"
   }
  ]
 },
 {
  "sintoma_capa1": "noise_sensitivity",
  "causa_capa2": "contenido_kg",
  "lado": "grafo",
  "jerarquia": "primaria",
  "pata": "¿Bajo qué criterio clasifican a sus deudores? (proveedores no financieros)",
  "evidencia": {
   "afirmacion": {
    "quote": "El énfasis se pone en el análisis de los flujos de fondos del cliente, evaluando si es capaz de atender adecuadamente todos sus compromisos financieros.",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "Al evaluar la capacidad de repago, el énfasis deberá ponerse en el análisis de los flujos de fondos realizado por la entidad.",
    "ubicacion": "Obligacion_analisis_de_flujos_de_fondos (prov Punto 4.3)"
   },
   "fuente": {
    "quote": "7.1. Criterio de clasificación. (…) la clasificación de estos clientes se efectuará considerando -al cabo de cada mes- exclusivamente pautas objetivas vinculadas al grado de cumplimiento de las correspondientes obligaciones o su situación jurídica (…)",
    "ubicacion": "TO_clasificacion_deudores_actual.pdf, Punto 7.1 (cartera consumo/vivienda) y 6.5 (cartera comercial, alcance real del nodo 'situación normal')"
   }
  },
  "busquedas": [
   {
    "consulta": "leer_pasaje 6.5 niveles de clasificación",
    "resultado": "el nodo 'Evaluación situación financiera normal' (flujo de fondos que atiende todos sus compromisos) pertenece a Sección 6 = cartera comercial, no a proveedores no financieros"
   },
   {
    "consulta": "ver_nodo Obligacion_analisis_de_flujos_de_fondos",
    "resultado": "el nodo NO declara en su contenido que su alcance sea la cartera comercial; leído solo no avisa que no aplica al criterio de mora de proveedores no financieros"
   }
  ]
 },
 {
  "sintoma_capa1": "noise_sensitivity",
  "causa_capa2": "provenance_imprecisa",
  "lado": "grafo",
  "jerarquia": "secundaria",
  "pata": "¿deben cumplir con Protección al Usuario? (afirmación Directivo Responsable)",
  "evidencia": {
   "afirmacion": {
    "quote": "Las entidades financieras, las empresas no financieras emisoras de tarjetas de crédito y/o compra y los otros proveedores no financieros de crédito deberán designar a un miembro del Directorio o autoridad equivalente como Directivo Responsable de Protección de los Usuarios de Servicios Financieros ante el BCRA.",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "Las entidades financieras, las empresas no financieras emisoras de tarjetas de crédito y/o compra y los otros proveedores no financieros de crédito deberán designar a un miembro del Directorio o autoridad equivalente como Directivo Responsable de Protección de los Usuarios de Servicios Financieros ante el BCRA.",
    "ubicacion": "Obligacion_las_entidades_financieras_las_empresas_no_financieras_emisoras_de_tarjetas_de_cr (paso 4)"
   },
   "fuente": {
    "quote": "3.2. Controles. 3.2.1. De los sujetos obligados. 3.2.1.1. Directivo Responsable de Protección de los Usuarios de Servicios Financieros/Comité de Protección de los Usuarios de Servicios Financieros.",
    "ubicacion": "TO_proteccion_usuarios_servicios_financieros_actual.pdf, Punto 3.2. Controles. (parte 1) — resuelve a índice/subtítulos, no al contenido de la obligación"
   }
  },
  "busquedas": [
   {
    "consulta": "leer_pasaje Punto 3.2 (parte 1) protección usuarios",
    "resultado": "la location del nodo devuelve el índice de subtítulos (3.2.1.1), no el texto del deber de designar; la cita no funda literalmente el contenido"
   },
   {
    "consulta": "leer_pasaje Punto 3.2.1.1",
    "resultado": "localizacion_pdf='fallida' (no anclable): confirma que la provenance no resuelve al contenido"
   }
  ]
 }
]
```

### Rep 2

- `formato_invalido`: `false` · `errores_formato`: `[]`
- `detectores`: `{"flag_encuadre_invertido": false, "flag_contexto": false, "tool_calls_usadas": 14, "max_tool_calls": 40, "tokens_in": 449733, "tokens_out": 9184}`
- longitudes: `razonamiento` = 2410 chars · `extraccion_traza` = 3920 chars

`atribuciones` ÍNTEGRAS (post-capa; incluye `capa_d`/`capa_d5` donde la capa anotó — la emisión original del LLM queda registrada en `capa_d.emision_llm` cuando D2 corrigió):

```json
[
 {
  "sintoma_capa1": "noise_sensitivity",
  "causa_capa2": "contenido_kg",
  "lado": "grafo",
  "jerarquia": "primaria",
  "pata": "¿Bajo qué criterio clasifican a sus deudores?",
  "evidencia": {
   "afirmacion": {
    "quote": "El criterio básico utilizado para efectuar la clasificación es la capacidad de pago en el futuro de la deuda o de los compromisos objeto de la garantía. El énfasis se pone en el análisis de los flujos de fondos del cliente, evaluando si es capaz de atender adecuadamente todos sus compromisos financieros.",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "El criterio básico a ser utilizado para efectuar la clasificación es la capacidad de pago en el futuro de la deuda o de los compromisos objeto de la garantía de la entidad financiera",
    "ubicacion": "Obligacion_evaluar_capacidad_de_pago (abierto por el agente, paso 13); provenance Punto 4.1"
   },
   "fuente": {
    "quote": "7.1. Criterio de clasificación. (…) la clasificación de estos clientes se efectuará considerando -al cabo de cada mes- exclusivamente pautas objetivas vinculadas al grado de cumplimiento de las correspondientes obligaciones o su situación jurídica",
    "ubicacion": "TO_clasificacion_deudores_actual.pdf, Punto 7.1"
   }
  },
  "busquedas": [
   {
    "consulta": "leer_pasaje_pdf Punto 10.1 Proveedores no financieros de crédito",
    "resultado": "los proveedores no financieros clasifican 'según los criterios aplicables para la cartera de consumo o vivienda' (Sección 7), NO la cartera comercial"
   },
   {
    "consulta": "leer_pasaje_pdf Punto 7.1 Criterio de clasificación",
    "resultado": "el criterio de consumo/vivienda es 'exclusivamente pautas objetivas vinculadas al grado de cumplimiento' (mora), no el análisis de flujo de fondos ni capacidad de pago futuro"
   },
   {
    "consulta": "leer_pasaje_pdf Punto 4.2 / 4.3",
    "resultado": "el criterio 'capacidad de pago futuro' y 'énfasis en flujos de fondos' es el de la cartera comercial (Sección 6), no aplicable a proveedores no financieros"
   }
  ]
 },
 {
  "sintoma_capa1": "noise_sensitivity",
  "causa_capa2": "contenido_kg",
  "lado": "grafo",
  "jerarquia": "secundaria",
  "pata": "¿Bajo qué criterio clasifican a sus deudores?",
  "evidencia": {
   "afirmacion": {
    "quote": "El énfasis se pone en el análisis de los flujos de fondos del cliente, evaluando si es capaz de atender adecuadamente todos sus compromisos financieros.",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "Para clasificación en situación normal: El análisis del flujo de fondos del cliente demuestra que es capaz de atender adecuadamente todos sus compromisos financ…",
    "ubicacion": "Obligacion_para_clasificacion_en_situacion_normal_el_analisis_del_flujo_de_fondos_del_clien (expuesto en paso 11); Obligacion_analisis_de_flujos_de_fondos"
   },
   "fuente": {
    "quote": "6.5.1. En situación normal. El análisis del flujo de fondos del cliente demuestra que es capaz de atender adecuadamente todos sus compromisos financieros.",
    "ubicacion": "TO_clasificacion_deudores_actual.pdf, Sección 6 (cartera comercial), Punto 6.5.1"
   }
  },
  "busquedas": [
   {
    "consulta": "leer_pasaje_pdf Sección 6",
    "resultado": "el texto 'El análisis del flujo de fondos del cliente demuestra que es capaz de atender adecuadamente todos sus compromisos financieros' es el criterio 6.5.1 de la cartera COMERCIAL; el nodo lo reproduce sin declarar ese alcance"
   }
  ]
 },
 {
  "sintoma_capa1": "noise_sensitivity",
  "causa_capa2": "sin_defecto",
  "lado": "ninguno",
  "jerarquia": "sin_par",
  "pata": "¿Los proveedores no financieros de crédito y las empresas no financieras emisoras de tarjetas deben cumplir con Protección al Usuario?",
  "evidencia": {
   "afirmacion": {
    "quote": "Las entidades financieras, las empresas no financieras emisoras de tarjetas de crédito y/o compra y los otros proveedores no financieros de crédito deberán designar a un miembro del Directorio o autoridad equivalente como Directivo Responsable de Protección de los Usuarios de Servicios Financieros ante el BCRA.",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "Las entidades financieras, las empresas no financieras emisoras de tarjetas de crédito y/o compra y los otros proveedores no financieros de crédito deberán designar a un miembro del Directorio o autoridad equivalente como Directivo Responsable de Protección de los Usuarios de Servicios Financieros ante el BCRA.",
    "ubicacion": "Obligacion_las_entidades_financieras_las_empresas_no_financieras_emisoras_de_tarjetas_de_cr (abierto por el agente, paso 4)"
   },
   "fuente": {
    "quote": "3.2. Controles. 3.2.1. De los sujetos obligados. 3.2.1.1. Directivo Responsable de Protección de los Usuarios de Servicios Financieros/Comité de Protección de los Usuarios de Servicios Financieros.",
    "ubicacion": "TO_proteccion_usuarios_servicios_financieros_actual.pdf, Punto 3.2. Controles. (parte 1)"
   }
  },
  "busquedas": [
   {
    "consulta": "leer_pasaje_pdf Punto 3.2 Controles Protección",
    "resultado": "el punto 3.2.1.1 trata efectivamente del 'Directivo Responsable de Protección de los Usuarios de Servicios Financieros', consistente con el contenido del nodo"
   }
  ]
 }
]
```

### Rep 3

- `formato_invalido`: `false` · `errores_formato`: `[]`
- `detectores`: `{"flag_encuadre_invertido": false, "flag_contexto": false, "tool_calls_usadas": 12, "max_tool_calls": 40, "tokens_in": 357877, "tokens_out": 8814}`
- longitudes: `razonamiento` = 2501 chars · `extraccion_traza` = 3651 chars

`atribuciones` ÍNTEGRAS (post-capa; incluye `capa_d`/`capa_d5` donde la capa anotó — la emisión original del LLM queda registrada en `capa_d.emision_llm` cuando D2 corrigió):

```json
[
 {
  "sintoma_capa1": "noise_sensitivity",
  "causa_capa2": "contenido_kg",
  "lado": "grafo",
  "jerarquia": "primaria",
  "pata": "¿Bajo qué criterio clasifican a sus deudores?",
  "evidencia": {
   "afirmacion": {
    "quote": "El criterio básico utilizado para efectuar la clasificación es la capacidad de pago en el futuro de la deuda o de los compromisos objeto de la garantía. El énfasis se pone en el análisis de los flujos de fondos del cliente, evaluando si es capaz de atender adecuadamente todos sus compromisos financieros.",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "El criterio básico a ser utilizado para efectuar la clasificación es la capacidad de pago en el futuro de la deuda o de los compromisos objeto de la garantía de la entidad financiera",
    "ubicacion": "Obligacion_evaluar_capacidad_de_pago (abierto por el agente, paso 13); complementado por Obligacion_analisis_de_flujos_de_fondos: 'Al evaluar la capacidad de repago, el énfasis deberá ponerse en el análisis de los flujos de fondos realizado por la entidad.'"
   },
   "fuente": {
    "quote": "10.1. Proveedores no financieros de crédito. Las empresas no financieras emisoras de tarjetas de crédito y/o compra y los otros proveedores no financieros de crédito (…) deberán clasificar a los respectivos deudores en función de su mora, según los criterios aplicables para la cartera de \"consumo o vivienda\" y por aplicación de las disposiciones previstas en el punto 7.3.",
    "ubicacion": "TO_clasificacion_deudores_actual.pdf, Punto 10.1"
   }
  },
  "busquedas": [
   {
    "consulta": "leer_pasaje_pdf Punto 4.2 clasificacion deudores",
    "resultado": "'4.2. Criterio básico de clasificación. El criterio básico (…) es la capacidad de pago en el futuro (…)' — pertenece a la Sección 4/6 de cartera COMERCIAL, no a proveedores no financieros"
   },
   {
    "consulta": "leer_pasaje_pdf Punto 4.3",
    "resultado": "'4.3.1. Al evaluar la capacidad de repago, el énfasis deberá ponerse en el análisis de los flujos de fondos' — cartera comercial"
   },
   {
    "consulta": "leer_pasaje_pdf Punto 7.2",
    "resultado": "Para cartera consumo/vivienda la clasificación es por MORA: 'Situación normal. Comprende los clientes que atienden en forma puntual el pago de sus obligaciones o con atrasos que no superan los 31 días' — criterio pertinente para proveedores no financieros"
   },
   {
    "consulta": "ver_nodo Obligacion_analisis_de_flujos_de_fondos",
    "resultado": "description genérica sin marca de cartera: 'Al evaluar la capacidad de repago, el énfasis deberá ponerse en el análisis de los flujos de fondos realizado por la entidad.' — el nodo NO declara que su alcance es la cartera comercial"
   }
  ]
 },
 {
  "sintoma_capa1": "noise_sensitivity",
  "causa_capa2": "sin_defecto",
  "lado": "ninguno",
  "jerarquia": "sin_par",
  "pata": "¿Deben cumplir con Protección al Usuario? (claim no central del Directivo Responsable)",
  "evidencia": {
   "afirmacion": {
    "quote": "Las entidades financieras, las empresas no financieras emisoras de tarjetas de crédito y/o compra y los otros proveedores no financieros de crédito deberán designar a un miembro del Directorio o autoridad equivalente como Directivo Responsable de Protección de los Usuarios de Servicios Financieros ante el BCRA.",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "Las entidades financieras, las empresas no financieras emisoras de tarjetas de crédito y/o compra y los otros proveedores no financieros de crédito deberán designar a un miembro del Directorio o autoridad equivalente como Directivo Responsable de Protección de los Usuarios de Servicios Financieros ante el BCRA.",
    "ubicacion": "Obligacion_las_entidades_financieras_las_empresas_no_financieras_emisoras_de_tarjetas_de_cr (abierto por el agente, paso 4)"
   },
   "fuente": {
    "quote": "3.2. Controles. 3.2.1. De los sujetos obligados. 3.2.1.1. Directivo Responsable de Protección de los Usuarios de Servicios Financieros/Comité de Protección de los Usuarios de Servicios Financieros.",
    "ubicacion": "TO_proteccion_usuarios_servicios_financieros_actual.pdf, Punto 3.2 (pág 26)"
   }
  },
  "busquedas": [
   {
    "consulta": "leer_pasaje_pdf Punto 3.2 Controles Protección",
    "resultado": "confirma existencia de la figura 'Directivo Responsable de Protección de los Usuarios de Servicios Financieros' entre los controles de los sujetos obligados — el claim del agente reproduce verbatim el nodo, que es fiel al PDF"
   },
   {
    "consulta": "leer_pasaje_pdf Punto 1.1. Partes Protección",
    "resultado": "confirma que los sujetos obligados incluyen entidades financieras y otras categorías, sustentando que la designación aplica a los sujetos regulados por Protección al Usuario"
   }
  ]
 }
]
```

**Tokens del caso (suma de detectores de las 3 reps): in=1,159,166 · out=27,019**


---

## CQ-019 (`piloto_v6/off_run_3_CQ-019.json` + `_capa_d.json`)

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

**voto_capa_d:**

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

**triage_capa_d:**

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
- `detectores`: `{"flag_encuadre_invertido": false, "flag_contexto": false, "tool_calls_usadas": 9, "max_tool_calls": 40, "tokens_in": 242592, "tokens_out": 6113}`
- longitudes: `razonamiento` = 2355 chars · `extraccion_traza` = 2949 chars

`atribuciones` ÍNTEGRAS (post-capa; incluye `capa_d`/`capa_d5` donde la capa anotó — la emisión original del LLM queda registrada en `capa_d.emision_llm` cuando D2 corrigió):

```json
[
 {
  "sintoma_capa1": "noise_sensitivity",
  "causa_capa2": "sin_defecto",
  "lado": "ninguno",
  "jerarquia": "sin_par",
  "pata": "Cómo se vincula esa regla con la clasificación de deudores",
  "evidencia": {
   "afirmacion": {
    "quote": "la clasificación de un deudor como 'en situación normal' (que comprende clientes que atienden puntualmente el pago de sus obligaciones o con atrasos que no superan los 31 días)",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "Comprende los clientes que atienden en forma puntual el pago de sus obligaciones o con atrasos que no superan los 31 días",
    "ubicacion": "Restriccion_comprende_los_clientes_que_atienden_en_forma_puntual_el_pago_de_sus_obligaciones (expuesto en resumen_propiedades del paso 7)"
   },
   "fuente": {
    "quote": "7.2.1. Situación normal. \nComprende los clientes que atienden en forma puntual el pago de sus obligaciones o con atrasos que no superan los 31 días.",
    "ubicacion": "TO_clasificacion_deudores_actual.pdf, Punto 7.2. Niveles de clasificación (7.2.1)"
   }
  },
  "busquedas": [
   {
    "consulta": "situación normal capacidad de pago comercial flujo de fondos",
    "resultado": "Confirma que la cartera comercial (6.5.1) usa criterio de flujo de fondos/capacidad de pago; el criterio de 'atrasos ≤31 días' corresponde a la cartera de consumo (7.2.1). El nodo de deducción cita AMBOS puntos, por lo que la definición literal de 7.2.1 es válida como respuesta genérica."
   },
   {
    "consulta": "TO_capitales_minimos_actual.pdf Punto 2.3 (leer_pasaje_pdf)",
    "resultado": "El punto 2.3 cita textualmente 'puntos 6.5.1. y 7.2.1. del TO sobre Clasificación de Deudores', confirmando que 7.2.1 es fuente válida de la definición de 'situación normal' invocada por la regla."
   }
  ]
 }
]
```

### Rep 2

- `formato_invalido`: `false` · `errores_formato`: `[]`
- `detectores`: `{"flag_encuadre_invertido": false, "flag_contexto": false, "tool_calls_usadas": 6, "max_tool_calls": 40, "tokens_in": 142753, "tokens_out": 4940}`
- longitudes: `razonamiento` = 1786 chars · `extraccion_traza` = 2968 chars

`atribuciones` ÍNTEGRAS (post-capa; incluye `capa_d`/`capa_d5` donde la capa anotó — la emisión original del LLM queda registrada en `capa_d.emision_llm` cuando D2 corrigió):

```json
[
 {
  "sintoma_capa1": "noise_sensitivity",
  "causa_capa2": "sin_defecto",
  "lado": "ninguno",
  "jerarquia": "sin_par",
  "pata": "Cómo se vincula esa regla con la clasificación de deudores",
  "evidencia": {
   "afirmacion": {
    "quote": "La clasificación 'en situación normal' comprende clientes que atienden puntualmente el pago de sus obligaciones o con atrasos que no superan los 31 días.",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "Comprende los clientes que atienden en forma puntual el pago de sus obligaciones o con atrasos que no superan los 31 días",
    "ubicacion": "Restriccion_comprende_los_clientes_que_atienden_en_forma_puntual_el_pago_de_sus_obligaciones (expuesto en resumen_propiedades del paso 7; confirmado con ver_nodo)"
   },
   "fuente": {
    "quote": "7.2.1. Situación normal. \nComprende los clientes que atienden en forma puntual el pago de sus obligaciones o con atrasos que no superan los 31 días.",
    "ubicacion": "TO_clasificacion_deudores_actual.pdf, Punto 7.2.1"
   }
  },
  "busquedas": [
   {
    "consulta": "ver_nodo Restriccion_comprende_los_clientes_que_atienden_en_forma_puntual_el_pago_de_sus_obligaciones",
    "resultado": "Nodo existe, tipo limite_cuantitativo, umbral '31 días', provenance Punto 7.2 del TO Clasificación de Deudores; contenido idéntico al claim"
   },
   {
    "consulta": "ver_paso_completo paso 7",
    "resultado": "El resumen_propiedades del nodo en la lista de resultados expone verbatim 'Comprende los clientes que atienden en forma puntual el pago de sus obligaciones o con atrasos que no superan los 31 días' — el agente vio el texto completo"
   },
   {
    "consulta": "leer_pasaje_pdf Punto 7.2.1 TO_clasificacion_deudores",
    "resultado": "El PDF confirma la definición exacta de situación normal con atrasos que no superan 31 días"
   }
  ]
 }
]
```

### Rep 3

- `formato_invalido`: `false` · `errores_formato`: `[]`
- `detectores`: `{"flag_encuadre_invertido": false, "flag_contexto": false, "tool_calls_usadas": 5, "max_tool_calls": 40, "tokens_in": 110179, "tokens_out": 4019}`
- longitudes: `razonamiento` = 1707 chars · `extraccion_traza` = 2901 chars

`atribuciones` ÍNTEGRAS (post-capa; incluye `capa_d`/`capa_d5` donde la capa anotó — la emisión original del LLM queda registrada en `capa_d.emision_llm` cuando D2 corrigió):

```json
[
 {
  "sintoma_capa1": "noise_sensitivity",
  "causa_capa2": "sin_defecto",
  "lado": "ninguno",
  "jerarquia": "sin_par",
  "pata": "Cómo se vincula esa regla con la clasificación de deudores (glosa sobre 'situación normal')",
  "evidencia": {
   "afirmacion": {
    "quote": "la clasificación de un deudor como 'en situación normal' (que comprende clientes que atienden puntualmente el pago de sus obligaciones o con atrasos que no superan los 31 días)",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "Comprende los clientes que atienden en forma puntual el pago de sus obligaciones o con atrasos que no superan los 31 días",
    "ubicacion": "Restriccion_comprende_los_clientes_que_atienden_en_forma_puntual_el_pago_de_sus_obligaciones (label 'Límite de atraso en situación normal'; expuesto en paso 7)"
   },
   "fuente": {
    "quote": "7.2.1. Situación normal. Comprende los clientes que atienden en forma puntual el pago de sus obligaciones o con atrasos que no superan los 31 días.",
    "ubicacion": "TO_clasificacion_deudores_actual.pdf, Punto 7.2"
   }
  },
  "busquedas": [
   {
    "consulta": "ver_paso_completo(7)",
    "resultado": "El nodo 'Límite de atraso en situación normal' figura entre los resultados con su resumen íntegro 'Comprende los clientes que atienden en forma puntual el pago de sus obligaciones o con atrasos que no superan los 31 días' — es decir, el contenido de la glosa estuvo EXPUESTO al agente en su trayectoria."
   },
   {
    "consulta": "ver_nodo del nodo portador",
    "resultado": "Confirma descripcion, tipo limite_cuantitativo, umbral '31 días', provenance TO_clasificacion_deudores_actual.pdf Punto 7.2 (Situación normal) — provenance correcta"
   },
   {
    "consulta": "leer_pasaje_pdf TO_clasificacion_deudores Punto 7.2",
    "resultado": "El PDF dice verbatim lo mismo: '7.2.1. Situación normal. Comprende los clientes que atienden en forma puntual el pago de sus obligaciones o con atrasos que no superan los 31 días.' — la glosa es correcta y fiel"
   }
  ]
 }
]
```

**Tokens del caso (suma de detectores de las 3 reps): in=495,524 · out=15,072**


---

## CQ-024 (`piloto_v6/off_run_3_CQ-024.json` + `_capa_d.json`)

**Voto v5.7 original (verbatim):**

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
 "votos_ganadores": 2,
 "conteo": [
  {
   "pares_primarios": [
    [
     "context_recall",
     "alcanzabilidad_kg"
    ]
   ],
   "votos": 2
  },
  {
   "pares_primarios": [
    [
     "context_recall",
     "navegación"
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
     "alcanzabilidad_kg"
    ]
   ],
   "formato_invalido": false
  },
  {
   "rep": 3,
   "pares_primarios": [
    [
     "context_recall",
     "alcanzabilidad_kg"
    ]
   ],
   "formato_invalido": false
  }
 ]
}
```

**voto_capa_d:**

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

**resumen_capa_d:** `{"reps_tocadas": [1, 2, 3], "atribuciones_corregidas": 2, "discrepancias": 1, "triage": 1}`

**triage_capa_d:**

```json
{
 "triage": true,
 "motivos": [
  "modulo_deterministico_sin_decision"
 ],
 "flags": [
  "R3: rep 2 atrib 1 — D2/sin_portador_extraible"
 ]
}
```

### Rep 1

- `formato_invalido`: `false` · `errores_formato`: `[]`
- `detectores`: `{"flag_encuadre_invertido": false, "flag_contexto": false, "tool_calls_usadas": 19, "max_tool_calls": 40, "tokens_in": 485925, "tokens_out": 10702}`
- longitudes: `razonamiento` = 2956 chars · `extraccion_traza` = 3939 chars

`atribuciones` ÍNTEGRAS (post-capa; incluye `capa_d`/`capa_d5` donde la capa anotó — la emisión original del LLM queda registrada en `capa_d.emision_llm` cuando D2 corrigió):

```json
[
 {
  "sintoma_capa1": "context_recall",
  "causa_capa2": "alcanzabilidad_kg",
  "lado": "agente",
  "jerarquia": "primaria",
  "pata": "Casos en que la reevaluación debe ser inmediata",
  "evidencia": {
   "afirmacion": {
    "quote": "la información disponible en el grafo no especifica detalladamente todos los casos particulares en los que la reevaluación debe ser inmediata para deudores de cartera comercial con financiaciones del 5% de RPC.",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "Se deberá analizar dejando constancia fundamentada de la decisión adoptada en el legajo del cliente y, de ser necesario, modificar la clasificación cada vez que tenga lugar alguna de las circunstancias mencionadas | (vecinos entrantes vía exceptua_obligacion:) 'Modificación de alguno de los criterios objetivos de clasificación...' ; 'Modificación en forma negativa de la clasificación del cliente en la Central de deudores...' ; 'Notificación de la determinación final de la SEFyC del ajuste de previsiones...' ; 'Cuando exista una discrepancia de más de un nivel entre la clasificación dada por la entidad financiera...'",
    "ubicacion": "Obligacion_se_debera_analizar_dejando_constancia_fundamentada_de_la_decision_adoptada_en_el (bisagra) + Excepcion_modificacion_de_alguno_de_los_criterios_objetivos... + Excepcion_modificacion_en_forma_negativa... + Excepcion_notificacion_de_la_determinacion_final_de_la_sefyc... + Excepcion_cuando_exista_una_discrepancia_de_mas_de_un_nivel..."
   },
   "fuente": {
    "quote": "6.4. Reconsideración obligatoria de la clasificación. ... modificar la clasificación cada vez que tenga lugar alguna de las siguientes circunstancias: 6.4.1. Modificación de alguno de los criterios objetivos de clasificación... 6.4.2. Modificación en forma negativa de la clasificación del cliente en la 'Central de deudores del sistema financiero'... 6.4.3. Notificación de la determinación final de la SEFyC del ajuste de previsiones... 6.4.4. Cuando exista una discrepancia de más de un nivel... La reevaluación deberá ser inmediata cuando se trate de clientes cuyas financiaciones comprendidas igualen o superen el 1 % de la responsabilidad patrimonial computable...",
    "ubicacion": "TO_clasificacion_deudores_actual.pdf, Punto 6.4 (pp. 18-19)"
   }
  },
  "busquedas": [
   {
    "consulta": "modificación criterios objetivos clasificación morosidad situación jurídica",
    "resultado": "1º resultado = Excepcion_modificacion_de_alguno_de_los_criterios_objetivos... (caso 6.4.1), alcanzable"
   },
   {
    "consulta": "notificación SEFyC ajuste previsiones inspección",
    "resultado": "1º resultado = Excepcion_notificacion_de_la_determinacion_final_de_la_sefyc... (caso 6.4.3), alcanzable"
   },
   {
    "consulta": "discrepancia más de un nivel clasificación 20% 40% acreedores",
    "resultado": "1º resultado = Excepcion_cuando_exista_una_discrepancia_de_mas_de_un_nivel... (caso 6.4.4), alcanzable"
   },
   {
    "consulta": "reconsideración obligatoria clasificación casos inmediata (mismo del paso 11 del agente)",
    "resultado": "1º resultado = Operacion_reconsideracion_de_clasificacion; sus vecinos llevan a la Obligacion bisagra y de ahí a los 4 casos Excepcion — el agente encontró el nodo pero no exploró sus vecinos"
   },
   {
    "consulta": "cambio situación financiera deterioro información negativa reevaluación (mismo del paso 15 del agente)",
    "resultado": "el resumen expone 'Excepción por cambio negativo en Central de deudores' (caso 6.4.2); el agente lo tuvo a la vista y no lo abrió"
   }
  ],
  "capa_d": {
   "modulo": "D2",
   "portador_id": "Obligacion_se_debera_analizar_dejando_constancia_fundamentada_de_la_decision_adoptada_en_el",
   "emision_llm": "navegación",
   "decision_codigo": "alcanzabilidad_kg",
   "discrepancia": true,
   "alcanzable": false,
   "evidencia_d1": {
    "alcanzable": false,
    "n_consultas_simuladas": 43,
    "consultas_en_top10": [],
    "mejor_rank": 71
   }
  }
 }
]
```

### Rep 2

- `formato_invalido`: `false` · `errores_formato`: `[]`
- `detectores`: `{"flag_encuadre_invertido": false, "flag_contexto": false, "tool_calls_usadas": 15, "max_tool_calls": 40, "tokens_in": 420655, "tokens_out": 11074}`
- longitudes: `razonamiento` = 2757 chars · `extraccion_traza` = 4315 chars

`atribuciones` ÍNTEGRAS (post-capa; incluye `capa_d`/`capa_d5` donde la capa anotó — la emisión original del LLM queda registrada en `capa_d.emision_llm` cuando D2 corrigió):

```json
[
 {
  "sintoma_capa1": "context_recall",
  "causa_capa2": "alcanzabilidad_kg",
  "lado": "grafo",
  "jerarquia": "primaria",
  "pata": "Casos en que la reevaluación debe ser inmediata",
  "evidencia": {
   "afirmacion": {
    "quote": "Sin embargo, la información disponible en el grafo no especifica detalladamente todos los casos particulares en los que la reevaluación debe ser inmediata para deudores de cartera comercial con financiaciones del 5% de RPC.",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "Modificación de alguno de los criterios objetivos de clasificación que surjan de estas normas (término de morosidad, situación jurídica del cliente o de sus deudas, cumplimiento de refinanciaciones y pedidos de refinanciaciones de obligaciones)",
    "ubicacion": "Excepcion_modificacion_de_alguno_de_los_criterios_objetivos_de_clasificacion_que_surjan_de (label 'Excepción por criterios objetivos modificados', provenance Punto 6.4); análogos: Excepcion_notificacion_de_la_determinacion_final_de_la_sefyc_del_ajuste_de_previsiones_seg (label 'Excepción por notificación de SEFyC') y Excepcion_modificacion_en_forma_negativa_de_la_clasificacion_del_cliente_en_la_central_de_ (label 'Excepción por cambio negativo en Central de deudores')"
   },
   "fuente": {
    "quote": "6.4. Reconsideración obligatoria de la clasificación. (...) modificar la clasificación cada vez que tenga lugar alguna de las siguientes circunstancias: 6.4.1. Modificación de alguno de los criterios objetivos de clasificación (...) 6.4.2. Modificación en forma negativa de la clasificación del cliente en la 'Central de deudores del sistema financiero' (...) 6.4.3. Notificación de la determinación final de la SEFyC del ajuste de previsiones (...) 6.4.4. Cuando exista una discrepancia de más de un nivel entre la clasificación (...). La reevaluación deberá ser inmediata cuando se trate de clientes cuyas financiaciones comprendidas igualen o superen el 1 % de la responsabilidad patrimonial computable de la entidad o del activo del fideicomiso financiero (...) y dentro de los tres meses respecto de los demás clientes comprendidos.",
    "ubicacion": "TO_clasificacion_deudores_actual.pdf, Punto 6.4 (pp. 18-19)"
   }
  },
  "busquedas": [
   {
    "consulta": "reconsideración obligatoria clasificación casos inmediata (paso 11 del agente)",
    "resultado": "NO trae ningún nodo-caso 6.4.x; solo genéricos con 'casos'/'clasificación'"
   },
   {
    "consulta": "punto 6.4 reconsideración obligatoria casos reevaluación (paso 13 del agente)",
    "resultado": "NO trae los nodos-caso; resultados irrelevantes (BOPREAL, garantes) por compartir 'punto'/'casos'"
   },
   {
    "consulta": "modificación criterios objetivos clasificación morosidad situación jurídica (mía, con vocabulario del PDF)",
    "resultado": "SÍ trae 6.4.1 y 6.4.2 como primeros resultados — pero con términos del propio contenido del nodo, no ex ante"
   },
   {
    "consulta": "discrepancia clasificación entidades central deudores notificación SEFyC ajuste previsiones (mía, con vocabulario del PDF)",
    "resultado": "SÍ trae 6.4.3 y 6.4.2 — de nuevo con términos del propio nodo, aprendidos del PDF"
   }
  ],
  "capa_d": {
   "modulo": "D2",
   "accion": "sin_portador_extraible",
   "triage": true
  }
 },
 {
  "sintoma_capa1": "faithfulness",
  "causa_capa2": "alucinacion_agente",
  "lado": "agente",
  "jerarquia": "secundaria",
  "pata": "Casos en que la reevaluación debe ser inmediata",
  "evidencia": {
   "afirmacion": {
    "quote": "la información disponible en el grafo no especifica detalladamente todos los casos particulares en los que la reevaluación debe ser inmediata",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "Modificación en forma negativa de la clasificación del cliente en la Central de deudores del sistema financiero, llevándola a un grado inferior al de la entidad… (este nodo-caso 6.4.2 fue EXPUESTO al agente en el paso 15 y NO fue usado)",
    "ubicacion": "Excepcion_modificacion_en_forma_negativa_de_la_clasificacion_del_cliente_en_la_central_de_ (visto por el agente en paso 15)"
   },
   "fuente": {
    "quote": "6.4.1. Modificación de alguno de los criterios objetivos (...) 6.4.2. (...) Central de deudores (...) 6.4.3. Notificación de la determinación final de la SEFyC (...) 6.4.4. (...) discrepancia de más de un nivel",
    "ubicacion": "TO_clasificacion_deudores_actual.pdf, Punto 6.4 (pp. 18-19)"
   }
  },
  "busquedas": [
   {
    "consulta": "cambio situación financiera deterioro información negativa reevaluación (paso 15 del agente)",
    "resultado": "expuso al agente el caso 6.4.2 ('Excepción por cambio negativo en Central de deudores'); aun así el agente afirmó que el grafo no los especifica"
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
- `detectores`: `{"flag_encuadre_invertido": false, "flag_contexto": false, "tool_calls_usadas": 20, "max_tool_calls": 40, "tokens_in": 531992, "tokens_out": 11118}`
- longitudes: `razonamiento` = 2660 chars · `extraccion_traza` = 4093 chars

`atribuciones` ÍNTEGRAS (post-capa; incluye `capa_d`/`capa_d5` donde la capa anotó — la emisión original del LLM queda registrada en `capa_d.emision_llm` cuando D2 corrigió):

```json
[
 {
  "sintoma_capa1": "context_recall",
  "causa_capa2": "alcanzabilidad_kg",
  "lado": "grafo",
  "jerarquia": "primaria",
  "pata": "Casos en que la reevaluación debe ser inmediata",
  "evidencia": {
   "afirmacion": {
    "quote": "la normativa establece que la reevaluación deberá ser inmediata cuando se trate de clientes cuyas financiaciones comprendidas igualen o superen el 1% de la responsabilidad patrimonial computable de la entidad o del activo del fideicomiso financiero. Sin embargo, la información disponible en el grafo no especifica detalladamente todos los casos particulares en los que la reevaluación debe ser inmediata",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "Modificación de alguno de los criterios objetivos de clasificación que surjan de estas normas (término de morosidad, situación jurídica del cliente o de sus deudas, cumplimiento de refinanciaciones y pedidos de refinanciaciones de obligaciones)",
    "ubicacion": "Excepcion_modificacion_de_alguno_de_los_criterios_objetivos_de_clasificacion_que_surjan_de (portador del caso 6.4.1, provenance Punto 6.4; nunca apareció en la trayectoria del agente)"
   },
   "fuente": {
    "quote": "6.4. Reconsideración obligatoria de la clasificación. (…) modificar la clasificación cada vez que tenga lugar alguna de las siguientes circunstancias: 6.4.1. Modificación de alguno de los criterios objetivos de clasificación (…) 6.4.2. Modificación en forma negativa de la clasificación del cliente en la 'Central de deudores del sistema financiero' (…) 6.4.3. Notificación de la determinación final de la SEFyC del ajuste de previsiones (…) La reevaluación deberá ser inmediata cuando se trate de clientes cuyas financiaciones comprendidas igualen o superen el 1 % de la responsabilidad patrimonial computable (…) del mes anterior al de presentación de alguna de las circunstancias mencionadas (…) y dentro de los tres meses respecto de los demás clientes comprendidos.",
    "ubicacion": "TO_clasificacion_deudores_actual.pdf, Punto 6.4 (pp. 18-19)"
   }
  },
  "busquedas": [
   {
    "consulta": "reevaluación inmediata deudor comercial (vocab ex ante, = paso 2 del agente)",
    "resultado": "aparece solo el nodo del umbral 1%; ninguno de los nodos-caso 6.4.1-6.4.4"
   },
   {
    "consulta": "casos reevaluación inmediata clasificación deudor comercial circunstancias (vocab ex ante)",
    "resultado": "no aparece ningún nodo-caso 6.4.1-6.4.4"
   },
   {
    "consulta": "excepción clasificación deudor cartera comercial reevaluar modificar (vocab ex ante)",
    "resultado": "no aparece ningún nodo-caso 6.4.1-6.4.4"
   },
   {
    "consulta": "reconsideración obligatoria clasificación circunstancias reevaluar (vocab ex ante)",
    "resultado": "no aparece ningún nodo-caso 6.4.1-6.4.4"
   },
   {
    "consulta": "modificación criterios objetivos clasificación morosidad situación jurídica (vocab del PDF, NO ex ante)",
    "resultado": "Excepcion_modificacion_de_alguno_de_los_criterios_objetivos... (caso 6.4.1) en 1ª posición — solo se alcanza con palabras del propio nodo"
   },
   {
    "consulta": "notificación SEFyC ajuste previsiones inspección (vocab del PDF, NO ex ante)",
    "resultado": "Excepcion_notificacion_de_la_determinacion_final_de_la_sefyc... (caso 6.4.3) en 1ª posición — solo se alcanza con palabras del propio nodo"
   }
  ],
  "capa_d": {
   "modulo": "D2",
   "portador_id": "Excepcion_modificacion_de_alguno_de_los_criterios_objetivos_de_clasificacion_que_surjan_de",
   "emision_llm": "alcanzabilidad_kg",
   "decision_codigo": "alcanzabilidad_kg",
   "discrepancia": false,
   "alcanzable": false,
   "evidencia_d1": {
    "alcanzable": false,
    "n_consultas_simuladas": 43,
    "consultas_en_top10": [],
    "mejor_rank": 59
   }
  }
 }
]
```

**Tokens del caso (suma de detectores de las 3 reps): in=1,438,572 · out=32,894**


---

## CQ-033 (`piloto_v6/off_run_3_CQ-033.json` + `_capa_d.json`)

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
   "pares_primarios": [],
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
   "pares_primarios": [],
   "formato_invalido": false
  }
 ]
}
```

**voto_capa_d:**

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
    1,
    2
   ]
  },
  {
   "pares_primarios": [],
   "votos": 1,
   "reps": [
    3
   ]
  }
 ]
}
```

**resumen_capa_d:** `{"reps_tocadas": [], "atribuciones_corregidas": 0, "discrepancias": 0, "triage": 0}`

**triage_capa_d:**

```json
{
 "triage": false,
 "motivos": [],
 "flags": []
}
```

### Rep 1

- `formato_invalido`: `false` · `errores_formato`: `[]`
- `detectores`: `{"flag_encuadre_invertido": false, "flag_contexto": false, "tool_calls_usadas": 7, "max_tool_calls": 40, "tokens_in": 165565, "tokens_out": 7410}`
- longitudes: `razonamiento` = 2261 chars · `extraccion_traza` = 2176 chars

`atribuciones` ÍNTEGRAS (post-capa; incluye `capa_d`/`capa_d5` donde la capa anotó — la emisión original del LLM queda registrada en `capa_d.emision_llm` cuando D2 corrigió):

```json
[
 {
  "sintoma_capa1": "noise_sensitivity",
  "causa_capa2": "contenido_kg",
  "lado": "grafo",
  "jerarquia": "primaria",
  "pata": "Cuál es el límite a la exigencia de capital por riesgo operacional para una entidad del Grupo 2",
  "evidencia": {
   "afirmacion": {
    "quote": "El límite a la exigencia de capital por riesgo operacional para una entidad del Grupo 2 (Grupo B) es del 17% del promedio de los últimos 36 meses, vigente hasta el 30/06/26.",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "La exigencia de capital por riesgo operacional para entidades del grupo B determinada a través de la aplicación de la expresión descripta en el punto 7.2. hasta el 30/06/26 no podrá superar el 17% del promedio de los últimos 36 meses",
    "ubicacion": "Restriccion_la_exigencia_de_capital_por_riesgo_operacional_para_entidades_del_grupo_b_determ (paso 3)"
   },
   "fuente": {
    "quote": "12.3. Para aquellas entidades financieras que sean reclasificadas desde el 01/01/2026 como consecuencia de lo establecido en el punto 4.1. del TO sobre Autoridades de Entidades Financieras, la exigencia de capital por riesgo operacional para entidades del grupo 2 determinada a través de la aplicación de la expresión descripta en el punto 7.2. hasta el 30/06/26 no podrá superar: El 17% en el caso de entidades del grupo B (...)",
    "ubicacion": "TO_capitales_minimos_actual.pdf, Punto 12.3"
   }
  },
  "busquedas": [
   {
    "consulta": "17% grupo B promedio 36 meses límite",
    "resultado": "devuelve el nodo 'Restriccion_el_17_en_el_caso_de_entidades_del_grupo_b...' (Punto 7.3.2) con el 17% del Grupo B SIN fecha de vigencia — el límite general permanente del Grupo 2, nodo pertinente a la pata"
   },
   {
    "consulta": "ver_nodo Restriccion_el_17_...grupo_b (Punto 7.3.2)",
    "resultado": "descripcion: 'El 17% en el caso de entidades del grupo B del promedio de los últimos 36 meses...' — sin fecha 30/06/26; provenance Punto 7.3"
   }
  ]
 }
]
```

### Rep 2

- `formato_invalido`: `false` · `errores_formato`: `[]`
- `detectores`: `{"flag_encuadre_invertido": false, "flag_contexto": false, "tool_calls_usadas": 6, "max_tool_calls": 40, "tokens_in": 130238, "tokens_out": 6453}`
- longitudes: `razonamiento` = 2689 chars · `extraccion_traza` = 2269 chars

`atribuciones` ÍNTEGRAS (post-capa; incluye `capa_d`/`capa_d5` donde la capa anotó — la emisión original del LLM queda registrada en `capa_d.emision_llm` cuando D2 corrigió):

```json
[
 {
  "sintoma_capa1": "noise_sensitivity",
  "causa_capa2": "contenido_kg",
  "lado": "grafo",
  "jerarquia": "primaria",
  "pata": "Cuál es el límite a la exigencia de capital por riesgo operacional para una entidad del Grupo 2",
  "evidencia": {
   "afirmacion": {
    "quote": "El límite a la exigencia de capital por riesgo operacional para una entidad del Grupo 2 (Grupo B) es del 17% del promedio de los últimos 36 meses, vigente hasta el 30/06/26.",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "La exigencia de capital por riesgo operacional para entidades del grupo B determinada a través de la aplicación de la expresión descripta en el punto 7.2. hasta el 30/06/26 no podrá superar el 17% del promedio de los últimos 36 meses",
    "ubicacion": "Restriccion_la_exigencia_de_capital_por_riesgo_operacional_para_entidades_del_grupo_b_determ (label 'Límite exigencia capital operacional grupo B', abierto por el agente en paso 3)"
   },
   "fuente": {
    "quote": "12.3. Para aquellas entidades financieras que sean reclasificadas desde el 01/01/2026 como consecuencia de lo establecido en el punto 4.1. del TO sobre Autoridades de Entidades Financieras, la exigencia de capital por riesgo operacional para entidades del grupo 2 determinada a través de la aplicación de la expresión descripta en el punto 7.2. hasta el 30/06/26 no podrá superar: El 17% en el caso de entidades del grupo B [...] Los límites máximos establecidos precedentemente se reducirán a 11% y a 8%",
    "ubicacion": "TO_capitales_minimos_actual.pdf, Punto 12.3"
   }
  },
  "busquedas": [
   {
    "consulta": "17% grupo B vigencia límite riesgo operacional transitorio",
    "resultado": "aparece el nodo usado (grupo B, 12.3, con 'hasta 30/06/26') y también 'Restriccion_limite_de_reduccion_para_entidades_del_grupo_b_17_en_condicion_general...' cuyo resumen dice '17% en condición general, 11% o 7% en condiciones especiales' — este último captura el límite general SIN fecha, confirmando que el 17% general no vence"
   }
  ]
 }
]
```

### Rep 3

- `formato_invalido`: `false` · `errores_formato`: `[]`
- `detectores`: `{"flag_encuadre_invertido": false, "flag_contexto": false, "tool_calls_usadas": 4, "max_tool_calls": 40, "tokens_in": 97833, "tokens_out": 4944}`
- longitudes: `razonamiento` = 1382 chars · `extraccion_traza` = 2585 chars

`atribuciones` ÍNTEGRAS (post-capa; incluye `capa_d`/`capa_d5` donde la capa anotó — la emisión original del LLM queda registrada en `capa_d.emision_llm` cuando D2 corrigió):

```json
[
 {
  "sintoma_capa1": "noise_sensitivity",
  "causa_capa2": "sin_defecto",
  "lado": "ninguno",
  "jerarquia": "sin_par",
  "pata": "Cuál es el límite a la exigencia de capital por riesgo operacional para una entidad del Grupo 2 (matiz de vigencia temporal)",
  "evidencia": {
   "afirmacion": {
    "quote": "El límite a la exigencia de capital por riesgo operacional para una entidad del Grupo 2 (Grupo B) es del 17% del promedio de los últimos 36 meses, vigente hasta el 30/06/26.",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "La exigencia de capital por riesgo operacional para entidades del grupo B determinada a través de la aplicación de la expresión descripta en el punto 7.2. hasta el 30/06/26 no podrá superar el 17% del promedio de los últimos 36 meses",
    "ubicacion": "Restriccion_la_exigencia_de_capital_por_riesgo_operacional_para_entidades_del_grupo_b_determ (abierto por el agente en paso 3)"
   },
   "fuente": {
    "quote": "la exigencia de capital por riesgo operacional para entidades del grupo 2 determinada a través de la aplicación de la expresión descripta en el punto 7.2. hasta el 30/06/26 no podrá superar: El 17% en el caso de entidades del grupo B (...) del promedio de los últimos 36 meses",
    "ubicacion": "TO_capitales_minimos_actual.pdf, Punto 12.3"
   }
  },
  "busquedas": [
   {
    "consulta": "leer_pasaje_pdf Punto 12.3",
    "resultado": "El PDF confirma verbatim 'hasta el 30/06/26 no podrá superar: El 17% en el caso de entidades del grupo B' — la fecha 30/06/26 SÍ funda el límite del 17% del grupo B."
   },
   {
    "consulta": "leer_pasaje_pdf Punto 7.3",
    "resultado": "Régimen permanente del 17% grupo B SIN fecha; existe además el régimen transitorio del 12.3 CON la fecha 30/06/26 — el agente citó el 12.3, que es donde vive la fecha."
   },
   {
    "consulta": "ver_paso_completo paso 3",
    "resultado": "Confirma que el nodo abierto por el agente contiene íntegro 'hasta el 30/06/26 no podrá superar el 17%'; el claim está soportado por lo consultado."
   }
  ]
 }
]
```

**Tokens del caso (suma de detectores de las 3 reps): in=393,636 · out=18,807**


---

## Tabla de inventario

| Caso | Reps válidas | voto_capa_d emitido | Flags (detectores/voto) | Motivos de triage | Tokens in |
|---|---|---|---|---|---|
| CQ-016 | 3/3 | frontera_no_determinada / ganadores=null / votos=None | voto_dividido | ["voto_dividido"] | 692,774 |
| CQ-018 | 3/3 | mayoria / ganadores=[["noise_sensitivity", "contenido_kg"]] / votos=2 | ninguno | [] | 1,159,166 |
| CQ-019 | 3/3 | mayoria / ganadores=[] / votos=3 | ninguno | ["exoneracion_total"] | 495,524 |
| CQ-024 | 3/3 | mayoria / ganadores=[["context_recall", "alcanzabilidad_kg"]] / votos=3 | ninguno | ["modulo_deterministico_sin_decision"] | 1,438,572 |
| CQ-033 | 3/3 | mayoria / ganadores=[["noise_sensitivity", "contenido_kg"]] / votos=2 | ninguno | [] | 393,636 |

**Costo real total de la corrida (suma de `detectores` de las 15 reps): input = 4,179,672 tokens · output = 121,181 tokens.**

---

*Fin de la extracción. Los 10 JSONs quedan congelados en `posthoc_run/piloto_v6/`. El scoring
contra la vara del piloto es adjudicación externa. Frenado para revisión.*
