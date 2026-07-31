# Expediente de adjudicación — 18 réplicas flaggeadas del brazo reensamblado_v3 (escalón 1b)

Fecha: 2026-07-31. Unidad de EXTRACCIÓN mecánica: este expediente ordena el material
para la adjudicación humana; no contiene veredicto propio alguno. Fuentes (solo
lectura): trazas `posthoc_run/traces/escalon1b_r{1,2,3}/reensamblado_v3/`,
`EV1_runtime.json` (pregunta y `respuesta_esperada` selladas),
`corridas/resultados_1b_2026-07-30.json` (mayorías mecánicas),
`adjudicacion_humana_2026-07-26.json` (laudos sellados del escalón 1, para el
acarreo). Formato: el del `muestreo_flags.json` del escalón 1, extendido con el
rationale completo del juez (las dos pasadas), que aquel archivo no portaba —
extensión registrada, no había formato único con rationale.

**Motivo mecánico del flag** (criterio del instrumento, idéntico al escalón 1):
`judge.py:244` — `requiere_adjudicacion_humana = len(ns_centrales) > 0`: el juez
v2.1.1 flaggea cuando el paso 2 deja al menos una afirmación CENTRAL con verdict
`no_soportado`. En cada entrada se listan esas afirmaciones centrales no
soportadas (el contenido concreto del flag).

Las 18: EV1-004·r1/r2/r3 · EV1-007·r1 · EV1-011·r1/r2/r3 · EV1-015·r1/r2/r3 ·
EV1-018·r1/r2/r3 · EV1-028·r2 · EV1-034·r1/r2/r3 · EV1-036·r3.


---

## EV1-004 — enumerativa · ['TO_regimen_informativo_contable_mensual_actual.pdf']

**Pregunta (verbatim):** ¿Por qué excesos verificados deben informarse incrementos de exigencia por riesgo de crédito, incluyendo los incrementos que se computan adicionalmente?

**Respuesta esperada (key adjudicada, verbatim):** Se informarán los incrementos generados por excesos verificados en: la relación de activos inmovilizados y otros conceptos (códigos 83100000 a 83400000); los límites de las normas sobre grandes exposiciones al riesgo de crédito (códigos 83500000 a 83800000); los límites de las normas sobre graduación del crédito (códigos 84300000 a 84600000); los límites de las normas sobre financiamiento al sector público no financiero (códigos 87100000 a 87400000); y los límites de las normas sobre posiciones de derivados no cubiertos (códigos 87500000 a 87800000). Adicionalmente se computarán: la exposición crediticia resultante de la sumatoria de posiciones no cubiertas por contratos vendidos para cubrir variaciones de precios de productos básicos - commodities (código 84800000); la utilización de los cupos crediticios ampliados de financiamiento al sector público no financiero por asistencia financiera otorgada y/o tenencias de instrumentos de deuda de fideicomisos financieros o fondos fiduciarios (códigos 85600000 a 85800000); y los incrementos por excesos a los límites de participación en el capital de empresas -individual- y en el total de participaciones en el capital de empresas (código 86300000).

**Estado mecánico de la mayoría en v3:** veredictos ['correcta', 'correcta', 'correcta'] → n_correcta=3, correcto_mayoria=True, patrón 3-0


### EV1-004 · réplica 1 — FLAGGEADA

- Veredicto del juez: correctitud=`correcta`, completitud=`parcial`, cita_documento_correcto=`False`, cita_precision=`punto` | hit_tool_limit=False | pasos=13

- **Motivo mecánico del flag** — afirmaciones CENTRALES `no_soportado` (3):

  - Los incrementos de exigencia por riesgo de crédito generados por excesos verificados forman parte de la fórmula de cálculo de la exigencia de capital por riesgo de crédito.
  - La fórmula de cálculo de la exigencia de capital por riesgo de crédito es: C = (k x 0,08 x APR) + INC.
  - En la fórmula C = (k x 0,08 x APR) + INC, INC representa los incrementos adicionales.

**Respuesta completa del agente (verbatim):**

> Según la regulación del BCRA, los incrementos de exigencia por riesgo de crédito generados por excesos verificados deben informarse porque forman parte de la fórmula de cálculo de la exigencia de capital por riesgo de crédito. La fórmula es: C = (k x 0,08 x APR) + INC, donde INC representa los incrementos adicionales. Estos incrementos se generan por excesos verificados en: (1) relación de activos inmovilizados, (2) límites de grandes exposiciones al riesgo de crédito, (3) graduación del crédito, (4) financiamiento al sector público no financiero, y (5) posiciones de derivados no cubiertos. Las entidades deben informar estos incrementos diferenciando entre información en término, información fuera de término, incumplimientos reiterados, e incrementos determinados por la SEFyC, con una frecuencia mensual. Esta información es requerida para que el BCRA pueda supervisar y controlar que las entidades financieras mantengan los niveles de capital adecuados en función de los riesgos que asumen.

**Citas del agente:**
```json
[
  {
    "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
    "location": "Punto 9.1. Normas de procedimiento"
  },
  {
    "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
    "location": "Punto 9.2. Modelo de Información"
  },
  {
    "source_doc": "TO_capitales_minimos_actual.pdf",
    "location": "Punto 2.1. Exigencia."
  }
]
```

**Justificación del juez (verbatim):**
```json
{
  "correctitud": "Centrales todas verdaderas o no_soportadas; ninguna afirmación falsa.",
  "completitud": "Patas no cubiertas: Razón por la que los excesos verificados deben informarse como incrementos de exigencia por riesgo de crédito; Qué incrementos se computan adicionalmente y por qué deben incluirse en el informe",
  "citas": "Las citas del agente apuntan a TO_regimen_informativo_contable_mensual_actual.pdf (Punto 9.1 y 9.2) y TO_capitales_minimos_actual.pdf (Punto 2.1), pero el ground truth exige el Punto 9.1.1. del TO de régimen informativo contable mensual; ninguna cita alcanza ese nivel de precisión y el documento TO_capitales_minimos no figura en el ground truth."
}
```

**Paso 1 del juez (descomposición, verbatim):**
```json
{
  "afirmaciones_verificables": [
    {
      "enunciado": "Los incrementos de exigencia por riesgo de crédito generados por excesos verificados forman parte de la fórmula de cálculo de la exigencia de capital por riesgo de crédito.",
      "central": true
    },
    {
      "enunciado": "La fórmula de cálculo de la exigencia de capital por riesgo de crédito es: C = (k x 0,08 x APR) + INC.",
      "central": true
    },
    {
      "enunciado": "En la fórmula C = (k x 0,08 x APR) + INC, INC representa los incrementos adicionales.",
      "central": true
    },
    {
      "enunciado": "Los incrementos por excesos verificados se generan por excesos en la relación de activos inmovilizados.",
      "central": true
    },
    {
      "enunciado": "Los incrementos por excesos verificados se generan por excesos en los límites de grandes exposiciones al riesgo de crédito.",
      "central": true
    },
    {
      "enunciado": "Los incrementos por excesos verificados se generan por excesos en la graduación del crédito.",
      "central": true
    },
    {
      "enunciado": "Los incrementos por excesos verificados se generan por excesos en el financiamiento al sector público no financiero.",
      "central": true
    },
    {
      "enunciado": "Los incrementos por excesos verificados se generan por excesos en posiciones de derivados no cubiertos.",
      "central": true
    },
    {
      "enunciado": "Las entidades deben informar los incrementos diferenciando entre información en término, información fuera de término, incumplimientos reiterados e incrementos determinados por la SEFyC.",
      "central": false
    },
    {
      "enunciado": "La frecuencia de reporte de estos incrementos es mensual.",
      "central": false
    },
    {
      "enunciado": "La regulación que establece estos requisitos es del BCRA.",
      "central": false
    },
    {
      "enunciado": "El BCRA utiliza esta información para supervisar y controlar que las entidades financieras mantengan niveles de capital adecuados en función de los riesgos que asumen.",
      "central": false
    }
  ],
  "reportes_de_alcance": [],
  "patas_de_la_pregunta": [
    "Razón por la que los excesos verificados deben informarse como incrementos de exigencia por riesgo de crédito",
    "Qué incrementos se computan adicionalmente y por qué deben incluirse en el informe"
  ]
}
```

**Paso 2 del juez (verificaciones, verbatim):**
```json
{
  "verificaciones": [
    {
      "enunciado": "Los incrementos de exigencia por riesgo de crédito generados por excesos verificados forman parte de la fórmula de cálculo de la exigencia de capital por riesgo de crédito.",
      "central": true,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "La fórmula de cálculo de la exigencia de capital por riesgo de crédito es: C = (k x 0,08 x APR) + INC.",
      "central": true,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "En la fórmula C = (k x 0,08 x APR) + INC, INC representa los incrementos adicionales.",
      "central": true,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "Los incrementos por excesos verificados se generan por excesos en la relación de activos inmovilizados.",
      "central": true,
      "verdict": "verdadero"
    },
    {
      "enunciado": "Los incrementos por excesos verificados se generan por excesos en los límites de grandes exposiciones al riesgo de crédito.",
      "central": true,
      "verdict": "verdadero"
    },
    {
      "enunciado": "Los incrementos por excesos verificados se generan por excesos en la graduación del crédito.",
      "central": true,
      "verdict": "verdadero"
    },
    {
      "enunciado": "Los incrementos por excesos verificados se generan por excesos en el financiamiento al sector público no financiero.",
      "central": true,
      "verdict": "verdadero"
    },
    {
      "enunciado": "Los incrementos por excesos verificados se generan por excesos en posiciones de derivados no cubiertos.",
      "central": true,
      "verdict": "verdadero"
    },
    {
      "enunciado": "Las entidades deben informar los incrementos diferenciando entre información en término, información fuera de término, incumplimientos reiterados e incrementos determinados por la SEFyC.",
      "central": false,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "La frecuencia de reporte de estos incrementos es mensual.",
      "central": false,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "La regulación que establece estos requisitos es del BCRA.",
      "central": false,
      "verdict": "verdadero"
    },
    {
      "enunciado": "El BCRA utiliza esta información para supervisar y controlar que las entidades financieras mantengan niveles de capital adecuados en función de los riesgos que asumen.",
      "central": false,
      "verdict": "no_soportado"
    }
  ],
  "cobertura_patas": [
    {
      "pata": "Razón por la que los excesos verificados deben informarse como incrementos de exigencia por riesgo de crédito",
      "cobertura": "no_cubierta"
    },
    {
      "pata": "Qué incrementos se computan adicionalmente y por qué deben incluirse en el informe",
      "cobertura": "no_cubierta"
    }
  ],
  "cita_documento_correcto": false,
  "cita_precision": "punto",
  "abstencion": null,
  "especulacion_en_prosa": null,
  "justificacion": {
    "citas": "Las citas del agente apuntan a TO_regimen_informativo_contable_mensual_actual.pdf (Punto 9.1 y 9.2) y TO_capitales_minimos_actual.pdf (Punto 2.1), pero el ground truth exige el Punto 9.1.1. del TO de régimen informativo contable mensual; ninguna cita alcanza ese nivel de precisión y el documento TO_capitales_minimos no figura en el ground truth.",
    "abstencion": ""
  }
}
```

### EV1-004 · réplica 2 — FLAGGEADA

- Veredicto del juez: correctitud=`correcta`, completitud=`parcial`, cita_documento_correcto=`True`, cita_precision=`punto` | hit_tool_limit=False | pasos=12

- **Motivo mecánico del flag** — afirmaciones CENTRALES `no_soportado` (2):

  - La fórmula de exigencia de capital por riesgo de crédito es: C = (k x 0,08 x APR) + INC.
  - En la fórmula C = (k x 0,08 x APR) + INC, INC representa los incrementos adicionales por excesos verificados.

**Respuesta completa del agente (verbatim):**

> Según el Régimen Informativo Contable Mensual del BCRA, las entidades deben informar los incrementos a la exigencia según riesgo de crédito generados por excesos verificados en relación de activos inmovilizados, límites de grandes exposiciones al riesgo de crédito, graduación del crédito, financiamiento al sector público no financiero y posiciones de derivados no cubiertos. Estos incrementos se computan como parte de la fórmula de exigencia de capital por riesgo de crédito: C = (k x 0,08 x APR) + INC, donde INC representa precisamente estos incrementos adicionales. La obligación de informar estos incrementos forma parte del régimen informativo que permite al BCRA supervisar el cumplimiento de los requerimientos de capital mínimo de las entidades financieras. Sin embargo, el Knowledge Graph no contiene una explicación explícita sobre la justificación específica de por qué se deben informar estos incrementos en particular.

**Citas del agente:**
```json
[
  {
    "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
    "location": "Punto 9.1. Normas de procedimiento"
  },
  {
    "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
    "location": "Punto 9.2. Modelo de Información"
  }
]
```

**Justificación del juez (verbatim):**
```json
{
  "correctitud": "Centrales todas verdaderas o no_soportadas; ninguna afirmación falsa.",
  "completitud": "Patas no cubiertas: Razón por la cual los excesos verificados deben informarse como incrementos de exigencia por riesgo de crédito",
  "citas": "El agente cita el TO del régimen informativo contable mensual con precisión a nivel punto (Punto 9.1 y 9.2), coincidiendo con el ground truth (Punto 9.1.1.)."
}
```

**Paso 1 del juez (descomposición, verbatim):**
```json
{
  "afirmaciones_verificables": [
    {
      "enunciado": "Las entidades deben informar los incrementos a la exigencia según riesgo de crédito generados por excesos verificados en relación de activos inmovilizados.",
      "central": true
    },
    {
      "enunciado": "Las entidades deben informar los incrementos a la exigencia según riesgo de crédito generados por excesos verificados en límites de grandes exposiciones al riesgo de crédito.",
      "central": true
    },
    {
      "enunciado": "Las entidades deben informar los incrementos a la exigencia según riesgo de crédito generados por excesos verificados en graduación del crédito.",
      "central": true
    },
    {
      "enunciado": "Las entidades deben informar los incrementos a la exigencia según riesgo de crédito generados por excesos verificados en financiamiento al sector público no financiero.",
      "central": true
    },
    {
      "enunciado": "Las entidades deben informar los incrementos a la exigencia según riesgo de crédito generados por excesos verificados en posiciones de derivados no cubiertos.",
      "central": true
    },
    {
      "enunciado": "La fórmula de exigencia de capital por riesgo de crédito es: C = (k x 0,08 x APR) + INC.",
      "central": true
    },
    {
      "enunciado": "En la fórmula C = (k x 0,08 x APR) + INC, INC representa los incrementos adicionales por excesos verificados.",
      "central": true
    },
    {
      "enunciado": "La obligación de informar estos incrementos forma parte del Régimen Informativo Contable Mensual del BCRA.",
      "central": false
    },
    {
      "enunciado": "La obligación de informar estos incrementos permite al BCRA supervisar el cumplimiento de los requerimientos de capital mínimo de las entidades financieras.",
      "central": false
    }
  ],
  "reportes_de_alcance": [
    "El Knowledge Graph no contiene una explicación explícita sobre la justificación específica de por qué se deben informar estos incrementos en particular."
  ],
  "patas_de_la_pregunta": [
    "Razón por la cual los excesos verificados deben informarse como incrementos de exigencia por riesgo de crédito",
    "Qué incrementos se computan adicionalmente y por qué se incluyen en el informe"
  ]
}
```

**Paso 2 del juez (verificaciones, verbatim):**
```json
{
  "verificaciones": [
    {
      "enunciado": "Las entidades deben informar los incrementos a la exigencia según riesgo de crédito generados por excesos verificados en relación de activos inmovilizados.",
      "central": true,
      "verdict": "verdadero"
    },
    {
      "enunciado": "Las entidades deben informar los incrementos a la exigencia según riesgo de crédito generados por excesos verificados en límites de grandes exposiciones al riesgo de crédito.",
      "central": true,
      "verdict": "verdadero"
    },
    {
      "enunciado": "Las entidades deben informar los incrementos a la exigencia según riesgo de crédito generados por excesos verificados en graduación del crédito.",
      "central": true,
      "verdict": "verdadero"
    },
    {
      "enunciado": "Las entidades deben informar los incrementos a la exigencia según riesgo de crédito generados por excesos verificados en financiamiento al sector público no financiero.",
      "central": true,
      "verdict": "verdadero"
    },
    {
      "enunciado": "Las entidades deben informar los incrementos a la exigencia según riesgo de crédito generados por excesos verificados en posiciones de derivados no cubiertos.",
      "central": true,
      "verdict": "verdadero"
    },
    {
      "enunciado": "La fórmula de exigencia de capital por riesgo de crédito es: C = (k x 0,08 x APR) + INC.",
      "central": true,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "En la fórmula C = (k x 0,08 x APR) + INC, INC representa los incrementos adicionales por excesos verificados.",
      "central": true,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "La obligación de informar estos incrementos forma parte del Régimen Informativo Contable Mensual del BCRA.",
      "central": false,
      "verdict": "verdadero"
    },
    {
      "enunciado": "La obligación de informar estos incrementos permite al BCRA supervisar el cumplimiento de los requerimientos de capital mínimo de las entidades financieras.",
      "central": false,
      "verdict": "no_soportado"
    }
  ],
  "cobertura_patas": [
    {
      "pata": "Razón por la cual los excesos verificados deben informarse como incrementos de exigencia por riesgo de crédito",
      "cobertura": "no_cubierta"
    },
    {
      "pata": "Qué incrementos se computan adicionalmente y por qué se incluyen en el informe",
      "cobertura": "cubierta"
    }
  ],
  "cita_documento_correcto": true,
  "cita_precision": "punto",
  "abstencion": null,
  "especulacion_en_prosa": null,
  "justificacion": {
    "citas": "El agente cita el TO del régimen informativo contable mensual con precisión a nivel punto (Punto 9.1 y 9.2), coincidiendo con el ground truth (Punto 9.1.1.).",
    "abstencion": ""
  }
}
```

### EV1-004 · réplica 3 — FLAGGEADA

- Veredicto del juez: correctitud=`correcta`, completitud=`parcial`, cita_documento_correcto=`True`, cita_precision=`punto` | hit_tool_limit=False | pasos=13

- **Motivo mecánico del flag** — afirmaciones CENTRALES `no_soportado` (3):

  - Los incrementos de exigencia por riesgo de crédito (INC) forman parte de la fórmula de cálculo de la exigencia de capital por riesgo de crédito.
  - La fórmula de exigencia de capital por riesgo de crédito es: C = (k x 0,08 x APR) + INC.
  - INC representa los incrementos de exigencia que se computan adicionalmente.

**Respuesta completa del agente (verbatim):**

> Según la regulación del BCRA, los excesos verificados deben informarse incrementos de exigencia por riesgo de crédito porque estos incrementos forman parte de la fórmula de cálculo de la exigencia de capital por riesgo de crédito. La fórmula es: C = (k x 0,08 x APR) + INC, donde INC representa los incrementos de exigencia que se computan adicionalmente. Estos incrementos se generan por excesos verificados en: (1) relación de activos inmovilizados, (2) límites de grandes exposiciones al riesgo de crédito, (3) graduación del crédito, (4) financiamiento al sector público no financiero, y (5) posiciones de derivados no cubiertos. Las entidades deben informar estos incrementos diferenciando entre información en término, información fuera de término, incumplimientos reiterados, e incrementos determinados por la SEFyC. Esta información es requerida como parte del régimen informativo contable mensual para permitir la supervisión y control del cumplimiento de los requisitos de capital mínimo por parte del BCRA.

**Citas del agente:**
```json
[
  {
    "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
    "location": "Punto 9.1. Normas de procedimiento"
  },
  {
    "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
    "location": "Punto 9.2. Modelo de Información"
  },
  {
    "source_doc": "TO_capitales_minimos_actual.pdf",
    "location": "Punto 2.1. Exigencia."
  }
]
```

**Justificación del juez (verbatim):**
```json
{
  "correctitud": "Centrales todas verdaderas o no_soportadas; ninguna afirmación falsa.",
  "completitud": "Patas no cubiertas: Razón por la que los excesos verificados deben informarse como incrementos de exigencia por riesgo de crédito; Qué son los incrementos que se computan adicionalmente y por qué se incluyen",
  "citas": "El agente cita el TO_regimen_informativo_contable_mensual_actual.pdf en Punto 9.1, que corresponde al ground truth (Punto 9.1.1.), con precisión a nivel punto."
}
```

**Paso 1 del juez (descomposición, verbatim):**
```json
{
  "afirmaciones_verificables": [
    {
      "enunciado": "Los incrementos de exigencia por riesgo de crédito (INC) forman parte de la fórmula de cálculo de la exigencia de capital por riesgo de crédito.",
      "central": true
    },
    {
      "enunciado": "La fórmula de exigencia de capital por riesgo de crédito es: C = (k x 0,08 x APR) + INC.",
      "central": true
    },
    {
      "enunciado": "INC representa los incrementos de exigencia que se computan adicionalmente.",
      "central": true
    },
    {
      "enunciado": "Los incrementos de exigencia se generan por excesos verificados en la relación de activos inmovilizados.",
      "central": true
    },
    {
      "enunciado": "Los incrementos de exigencia se generan por excesos verificados en los límites de grandes exposiciones al riesgo de crédito.",
      "central": true
    },
    {
      "enunciado": "Los incrementos de exigencia se generan por excesos verificados en la graduación del crédito.",
      "central": true
    },
    {
      "enunciado": "Los incrementos de exigencia se generan por excesos verificados en el financiamiento al sector público no financiero.",
      "central": true
    },
    {
      "enunciado": "Los incrementos de exigencia se generan por excesos verificados en posiciones de derivados no cubiertos.",
      "central": true
    },
    {
      "enunciado": "Las entidades deben informar los incrementos diferenciando entre información en término, información fuera de término, incumplimientos reiterados e incrementos determinados por la SEFyC.",
      "central": false
    },
    {
      "enunciado": "La información sobre incrementos de exigencia es requerida como parte del régimen informativo contable mensual.",
      "central": false
    },
    {
      "enunciado": "El objetivo del reporte es permitir la supervisión y control del cumplimiento de los requisitos de capital mínimo por parte del BCRA.",
      "central": false
    }
  ],
  "reportes_de_alcance": [],
  "patas_de_la_pregunta": [
    "Razón por la que los excesos verificados deben informarse como incrementos de exigencia por riesgo de crédito",
    "Qué son los incrementos que se computan adicionalmente y por qué se incluyen"
  ]
}
```

**Paso 2 del juez (verificaciones, verbatim):**
```json
{
  "verificaciones": [
    {
      "enunciado": "Los incrementos de exigencia por riesgo de crédito (INC) forman parte de la fórmula de cálculo de la exigencia de capital por riesgo de crédito.",
      "central": true,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "La fórmula de exigencia de capital por riesgo de crédito es: C = (k x 0,08 x APR) + INC.",
      "central": true,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "INC representa los incrementos de exigencia que se computan adicionalmente.",
      "central": true,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "Los incrementos de exigencia se generan por excesos verificados en la relación de activos inmovilizados.",
      "central": true,
      "verdict": "verdadero"
    },
    {
      "enunciado": "Los incrementos de exigencia se generan por excesos verificados en los límites de grandes exposiciones al riesgo de crédito.",
      "central": true,
      "verdict": "verdadero"
    },
    {
      "enunciado": "Los incrementos de exigencia se generan por excesos verificados en la graduación del crédito.",
      "central": true,
      "verdict": "verdadero"
    },
    {
      "enunciado": "Los incrementos de exigencia se generan por excesos verificados en el financiamiento al sector público no financiero.",
      "central": true,
      "verdict": "verdadero"
    },
    {
      "enunciado": "Los incrementos de exigencia se generan por excesos verificados en posiciones de derivados no cubiertos.",
      "central": true,
      "verdict": "verdadero"
    },
    {
      "enunciado": "Las entidades deben informar los incrementos diferenciando entre información en término, información fuera de término, incumplimientos reiterados e incrementos determinados por la SEFyC.",
      "central": false,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "La información sobre incrementos de exigencia es requerida como parte del régimen informativo contable mensual.",
      "central": false,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "El objetivo del reporte es permitir la supervisión y control del cumplimiento de los requisitos de capital mínimo por parte del BCRA.",
      "central": false,
      "verdict": "no_soportado"
    }
  ],
  "cobertura_patas": [
    {
      "pata": "Razón por la que los excesos verificados deben informarse como incrementos de exigencia por riesgo de crédito",
      "cobertura": "no_cubierta"
    },
    {
      "pata": "Qué son los incrementos que se computan adicionalmente y por qué se incluyen",
      "cobertura": "no_cubierta"
    }
  ],
  "cita_documento_correcto": true,
  "cita_precision": "punto",
  "abstencion": null,
  "especulacion_en_prosa": null,
  "justificacion": {
    "citas": "El agente cita el TO_regimen_informativo_contable_mensual_actual.pdf en Punto 9.1, que corresponde al ground truth (Punto 9.1.1.), con precisión a nivel punto.",
    "abstencion": ""
  }
}
```

**Contexto de las 3 réplicas de EV1-004 en v3 (sin comentario):** r1: correctitud=`correcta` (flaggeada) · r2: correctitud=`correcta` (flaggeada) · r3: correctitud=`correcta` (flaggeada)


---

## EV1-007 — condicional · ['TO_regimen_informativo_contable_mensual_actual.pdf']

**Pregunta (verbatim):** ¿Alcanza con que una entidad financiera del Grupo 2 pertenezca al Grupo A para informar la reducción de exigencia por riesgo operacional en la partida 36000001?

**Respuesta esperada (key adjudicada, verbatim):** No. Además de ser una entidad del Grupo 2 perteneciente al Grupo A, la entidad no debe ser subsidiaria o sucursal de una entidad de importancia sistémica global (G-SIB). Cumplido ese requisito, la reducción se informará en la partida 36000001 únicamente cuando el límite aplicable (20 % del promedio de las exigencias por riesgo crediticio de los 36 meses anteriores al mes bajo informe) resulte inferior al importe informado en el código 70300000, calculándose como: 70300000 - [0,20 x (suma de ERC(n-1) a ERC(n-36)) / 36].

**Estado mecánico de la mayoría en v3:** veredictos ['correcta', 'correcta', 'correcta'] → n_correcta=3, correcto_mayoria=True, patrón 3-0


### EV1-007 · réplica 1 — FLAGGEADA

- Veredicto del juez: correctitud=`correcta`, completitud=`completa`, cita_documento_correcto=`True`, cita_precision=`punto` | hit_tool_limit=False | pasos=11

- **Motivo mecánico del flag** — afirmaciones CENTRALES `no_soportado` (1):

  - Para informar la reducción de exigencia en la partida 36000001, la entidad debe pertenecer a los Grupos A, B o C.

**Respuesta completa del agente (verbatim):**

> No alcanza con que una entidad financiera del Grupo 2 pertenezca al Grupo A para informar la reducción de exigencia por riesgo operacional en la partida 36000001. Además de pertenecer a los Grupos A, B o C, la entidad no debe ser subsidiaria o sucursal de entidades de importancia sistémica global (G-SIB). La reducción de exigencia no aplica a estas últimas.

**Citas del agente:**
```json
[
  {
    "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
    "location": "Punto 5.1. Normas de procedimiento (parte 1)"
  }
]
```

**Justificación del juez (verbatim):**
```json
{
  "correctitud": "Centrales todas verdaderas o no_soportadas; ninguna afirmación falsa.",
  "completitud": "Todas las patas cubiertas.",
  "citas": "La cita apunta al TO correcto con precisión de punto (Punto 5.1), aunque los puntos exactos del referente son 5.1.3.1 y 5.1.3.2."
}
```

**Paso 1 del juez (descomposición, verbatim):**
```json
{
  "afirmaciones_verificables": [
    {
      "enunciado": "No alcanza con que una entidad financiera del Grupo 2 pertenezca al Grupo A para informar la reducción de exigencia por riesgo operacional en la partida 36000001.",
      "central": true
    },
    {
      "enunciado": "Para informar la reducción de exigencia en la partida 36000001, la entidad debe pertenecer a los Grupos A, B o C.",
      "central": true
    },
    {
      "enunciado": "Para informar la reducción de exigencia en la partida 36000001, la entidad no debe ser subsidiaria o sucursal de entidades de importancia sistémica global (G-SIB).",
      "central": true
    },
    {
      "enunciado": "La reducción de exigencia por riesgo operacional en la partida 36000001 no aplica a subsidiarias o sucursales de entidades de importancia sistémica global (G-SIB).",
      "central": true
    }
  ],
  "reportes_de_alcance": [],
  "patas_de_la_pregunta": [
    "Si es suficiente que una entidad financiera del Grupo 2 pertenezca al Grupo A para informar la reducción de exigencia por riesgo operacional en la partida 36000001"
  ]
}
```

**Paso 2 del juez (verificaciones, verbatim):**
```json
{
  "verificaciones": [
    {
      "enunciado": "No alcanza con que una entidad financiera del Grupo 2 pertenezca al Grupo A para informar la reducción de exigencia por riesgo operacional en la partida 36000001.",
      "central": true,
      "verdict": "verdadero"
    },
    {
      "enunciado": "Para informar la reducción de exigencia en la partida 36000001, la entidad debe pertenecer a los Grupos A, B o C.",
      "central": true,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "Para informar la reducción de exigencia en la partida 36000001, la entidad no debe ser subsidiaria o sucursal de entidades de importancia sistémica global (G-SIB).",
      "central": true,
      "verdict": "verdadero"
    },
    {
      "enunciado": "La reducción de exigencia por riesgo operacional en la partida 36000001 no aplica a subsidiarias o sucursales de entidades de importancia sistémica global (G-SIB).",
      "central": true,
      "verdict": "verdadero"
    }
  ],
  "cobertura_patas": [
    {
      "pata": "Si es suficiente que una entidad financiera del Grupo 2 pertenezca al Grupo A para informar la reducción de exigencia por riesgo operacional en la partida 36000001",
      "cobertura": "cubierta"
    }
  ],
  "cita_documento_correcto": true,
  "cita_precision": "punto",
  "abstencion": null,
  "especulacion_en_prosa": null,
  "justificacion": {
    "citas": "La cita apunta al TO correcto con precisión de punto (Punto 5.1), aunque los puntos exactos del referente son 5.1.3.1 y 5.1.3.2.",
    "abstencion": ""
  }
}
```

**Contexto de las 3 réplicas de EV1-007 en v3 (sin comentario):** r1: correctitud=`correcta` (flaggeada) · r2: correctitud=`correcta` · r3: correctitud=`correcta`


---

## EV1-011 — enumerativa · ['TO_clasificacion_deudores_actual.pdf']

**Pregunta (verbatim):** ¿Cuáles son los niveles de clasificación previstos para los deudores de la cartera comercial, incluyendo las situaciones que integran el nivel con seguimiento especial?

**Respuesta esperada (key adjudicada, verbatim):** Cinco niveles: 1) en situación normal; 2) con seguimiento especial, que comprende las situaciones en observación, en negociación o con acuerdos de refinanciación, y en tratamiento especial; 3) con problemas; 4) con alto riesgo de insolvencia; y 5) irrecuperable.

**Estado mecánico de la mayoría en v3:** veredictos ['incorrecta', 'incorrecta', 'incorrecta'] → n_correcta=0, correcto_mayoria=False, patrón 3-0


### EV1-011 · réplica 1 — FLAGGEADA

- Veredicto del juez: correctitud=`incorrecta`, completitud=`completa`, cita_documento_correcto=`True`, cita_precision=`punto` | hit_tool_limit=True | pasos=15

- **Motivo mecánico del flag** — afirmaciones CENTRALES `no_soportado` (7):

  - El nivel 'Situación Normal' comprende clientes que atienden en forma puntual el pago de sus obligaciones o con atrasos que no superan los 31 días.
  - El nivel 'Riesgo Bajo - En Observación' comprende clientes con incumplimientos ocasionales y atrasos de más de 31 hasta 90 días.
  - El nivel 'Riesgo Bajo - En Tratamiento Especial' requiere reclasificación única tras pago en caso de refinanciaciones otorgadas por primera vez dentro del año calendario.
  - El nivel 'Riesgo Medio' comprende clientes con alguna incapacidad para cancelar sus obligaciones y atrasos de más de 90 hasta 180 días.
  - El nivel 'Riesgo Alto' comprende clientes con atrasos de más de 180 días hasta un año.
  - El nivel 'Irrecuperable' comprende clientes insolventes o en quiebra con nula o escasa posibilidad de recuperación del crédito o con atrasos superiores al año.
  - El nivel 'Riesgo Bajo - En Tratamiento Especial' integra situaciones de refinanciaciones otorgadas por primera vez dentro del año calendario.

**Respuesta completa del agente (verbatim):**

> Según la regulación del BCRA, los niveles de clasificación previstos para los deudores de la cartera comercial son: 1) Situación Normal: comprende los clientes que atienden en forma puntual el pago de sus obligaciones o con atrasos que no superan los 31 días; 2) Riesgo Bajo - En Observación: comprende los clientes que registran incumplimientos ocasionales en la atención de sus obligaciones, con atrasos de más de 31 hasta 90 días; 3) Riesgo Bajo - En Tratamiento Especial: nivel que requiere reclasificación única tras pago en caso de refinanciaciones otorgadas por primera vez dentro del año calendario; 4) Riesgo Medio: comprende los clientes que muestran alguna incapacidad para cancelar sus obligaciones, con atrasos de más de 90 hasta 180 días; 5) Riesgo Alto: comprende a los clientes con atrasos de más de 180 días hasta un año; 6) Irrecuperable: comprende a los clientes insolventes o en quiebra con nula o escasa posibilidad de recuperación del crédito o con atrasos superiores al año. El nivel con seguimiento especial es 'Riesgo Bajo - En Tratamiento Especial', que integra situaciones de refinanciaciones otorgadas por primera vez dentro del año calendario.

**Citas del agente:**
```json
[
  {
    "source_doc": "TO_clasificacion_deudores_actual.pdf",
    "location": "Punto 7.2. Niveles de clasificación. (parte 1)"
  }
]
```

**Justificación del juez (verbatim):**
```json
{
  "correctitud": "Afirmación central falsa: La cartera comercial tiene 6 niveles de clasificación según la regulación del BCRA.; El nivel 2 se denomina 'Riesgo Bajo - En Observación'.; El nivel 3 se denomina 'Riesgo Bajo - En Tratamiento Especial'.; El nivel 4 se denomina 'Riesgo Medio'.; El nivel 5 se denomina 'Riesgo Alto'.; El nivel con seguimiento especial es 'Riesgo Bajo - En Tratamiento Especial'.",
  "completitud": "Todas las patas cubiertas.",
  "citas": "La cita apunta al documento correcto (TO_clasificacion_deudores_actual.pdf) con precisión a nivel punto (Punto 7.2), aunque el referente indica que las secciones relevantes son los Puntos 6.5 a 6.5.5."
}
```

**Paso 1 del juez (descomposición, verbatim):**
```json
{
  "afirmaciones_verificables": [
    {
      "enunciado": "La cartera comercial tiene 6 niveles de clasificación según la regulación del BCRA.",
      "central": true
    },
    {
      "enunciado": "El nivel 1 se denomina 'Situación Normal'.",
      "central": true
    },
    {
      "enunciado": "El nivel 'Situación Normal' comprende clientes que atienden en forma puntual el pago de sus obligaciones o con atrasos que no superan los 31 días.",
      "central": true
    },
    {
      "enunciado": "El nivel 2 se denomina 'Riesgo Bajo - En Observación'.",
      "central": true
    },
    {
      "enunciado": "El nivel 'Riesgo Bajo - En Observación' comprende clientes con incumplimientos ocasionales y atrasos de más de 31 hasta 90 días.",
      "central": true
    },
    {
      "enunciado": "El nivel 3 se denomina 'Riesgo Bajo - En Tratamiento Especial'.",
      "central": true
    },
    {
      "enunciado": "El nivel 'Riesgo Bajo - En Tratamiento Especial' requiere reclasificación única tras pago en caso de refinanciaciones otorgadas por primera vez dentro del año calendario.",
      "central": true
    },
    {
      "enunciado": "El nivel 4 se denomina 'Riesgo Medio'.",
      "central": true
    },
    {
      "enunciado": "El nivel 'Riesgo Medio' comprende clientes con alguna incapacidad para cancelar sus obligaciones y atrasos de más de 90 hasta 180 días.",
      "central": true
    },
    {
      "enunciado": "El nivel 5 se denomina 'Riesgo Alto'.",
      "central": true
    },
    {
      "enunciado": "El nivel 'Riesgo Alto' comprende clientes con atrasos de más de 180 días hasta un año.",
      "central": true
    },
    {
      "enunciado": "El nivel 6 se denomina 'Irrecuperable'.",
      "central": true
    },
    {
      "enunciado": "El nivel 'Irrecuperable' comprende clientes insolventes o en quiebra con nula o escasa posibilidad de recuperación del crédito o con atrasos superiores al año.",
      "central": true
    },
    {
      "enunciado": "El nivel con seguimiento especial es 'Riesgo Bajo - En Tratamiento Especial'.",
      "central": true
    },
    {
      "enunciado": "El nivel 'Riesgo Bajo - En Tratamiento Especial' integra situaciones de refinanciaciones otorgadas por primera vez dentro del año calendario.",
      "central": true
    }
  ],
  "reportes_de_alcance": [],
  "patas_de_la_pregunta": [
    "Niveles de clasificación previstos para los deudores de la cartera comercial",
    "Situaciones que integran el nivel con seguimiento especial"
  ]
}
```

**Paso 2 del juez (verificaciones, verbatim):**
```json
{
  "verificaciones": [
    {
      "enunciado": "La cartera comercial tiene 6 niveles de clasificación según la regulación del BCRA.",
      "central": true,
      "verdict": "falso"
    },
    {
      "enunciado": "El nivel 1 se denomina 'Situación Normal'.",
      "central": true,
      "verdict": "verdadero"
    },
    {
      "enunciado": "El nivel 'Situación Normal' comprende clientes que atienden en forma puntual el pago de sus obligaciones o con atrasos que no superan los 31 días.",
      "central": true,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "El nivel 2 se denomina 'Riesgo Bajo - En Observación'.",
      "central": true,
      "verdict": "falso"
    },
    {
      "enunciado": "El nivel 'Riesgo Bajo - En Observación' comprende clientes con incumplimientos ocasionales y atrasos de más de 31 hasta 90 días.",
      "central": true,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "El nivel 3 se denomina 'Riesgo Bajo - En Tratamiento Especial'.",
      "central": true,
      "verdict": "falso"
    },
    {
      "enunciado": "El nivel 'Riesgo Bajo - En Tratamiento Especial' requiere reclasificación única tras pago en caso de refinanciaciones otorgadas por primera vez dentro del año calendario.",
      "central": true,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "El nivel 4 se denomina 'Riesgo Medio'.",
      "central": true,
      "verdict": "falso"
    },
    {
      "enunciado": "El nivel 'Riesgo Medio' comprende clientes con alguna incapacidad para cancelar sus obligaciones y atrasos de más de 90 hasta 180 días.",
      "central": true,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "El nivel 5 se denomina 'Riesgo Alto'.",
      "central": true,
      "verdict": "falso"
    },
    {
      "enunciado": "El nivel 'Riesgo Alto' comprende clientes con atrasos de más de 180 días hasta un año.",
      "central": true,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "El nivel 6 se denomina 'Irrecuperable'.",
      "central": true,
      "verdict": "verdadero"
    },
    {
      "enunciado": "El nivel 'Irrecuperable' comprende clientes insolventes o en quiebra con nula o escasa posibilidad de recuperación del crédito o con atrasos superiores al año.",
      "central": true,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "El nivel con seguimiento especial es 'Riesgo Bajo - En Tratamiento Especial'.",
      "central": true,
      "verdict": "falso"
    },
    {
      "enunciado": "El nivel 'Riesgo Bajo - En Tratamiento Especial' integra situaciones de refinanciaciones otorgadas por primera vez dentro del año calendario.",
      "central": true,
      "verdict": "no_soportado"
    }
  ],
  "cobertura_patas": [
    {
      "pata": "Niveles de clasificación previstos para los deudores de la cartera comercial",
      "cobertura": "cubierta"
    },
    {
      "pata": "Situaciones que integran el nivel con seguimiento especial",
      "cobertura": "cubierta"
    }
  ],
  "cita_documento_correcto": true,
  "cita_precision": "punto",
  "abstencion": null,
  "especulacion_en_prosa": null,
  "justificacion": {
    "citas": "La cita apunta al documento correcto (TO_clasificacion_deudores_actual.pdf) con precisión a nivel punto (Punto 7.2), aunque el referente indica que las secciones relevantes son los Puntos 6.5 a 6.5.5.",
    "abstencion": ""
  }
}
```

### EV1-011 · réplica 2 — FLAGGEADA

- Veredicto del juez: correctitud=`incorrecta`, completitud=`completa`, cita_documento_correcto=`True`, cita_precision=`punto` | hit_tool_limit=True | pasos=15

- **Motivo mecánico del flag** — afirmaciones CENTRALES `no_soportado` (6):

  - El nivel 'Situación Normal' comprende clientes que atienden en forma puntual el pago de sus obligaciones o con atrasos que no superan los 31 días.
  - El nivel 'Riesgo Bajo - En Observación' comprende clientes que registran incumplimientos ocasionales con atrasos de más de 31 hasta 90 días.
  - El nivel 'Riesgo Bajo - En Tratamiento Especial' requiere reclasificación única tras pago en caso de refinanciaciones otorgadas por primera vez dentro del año calendario.
  - El nivel 'Riesgo Medio' comprende clientes que muestran alguna incapacidad para cancelar sus obligaciones, con atrasos de más de 90 hasta 180 días.
  - El nivel 'Riesgo Alto' comprende clientes con atrasos de más de 180 días hasta un año.
  - El nivel 'Irrecuperable' comprende clientes insolventes o en quiebra con nula o escasa posibilidad de recuperación del crédito o con atrasos superiores al año.

**Respuesta completa del agente (verbatim):**

> Según la regulación del BCRA, los niveles de clasificación previstos para los deudores de la cartera comercial son: 1) Situación Normal: comprende los clientes que atienden en forma puntual el pago de sus obligaciones o con atrasos que no superan los 31 días; 2) Riesgo Bajo - En Observación: comprende los clientes que registran incumplimientos ocasionales en la atención de sus obligaciones, con atrasos de más de 31 hasta 90 días; 3) Riesgo Bajo - En Tratamiento Especial: nivel que requiere reclasificación única tras pago en caso de refinanciaciones otorgadas por primera vez dentro del año calendario; 4) Riesgo Medio: comprende los clientes que muestran alguna incapacidad para cancelar sus obligaciones, con atrasos de más de 90 hasta 180 días; 5) Riesgo Alto: comprende a los clientes con atrasos de más de 180 días hasta un año; 6) Irrecuperable: comprende a los clientes insolventes o en quiebra con nula o escasa posibilidad de recuperación del crédito o con atrasos superiores al año. El nivel con seguimiento especial es 'Riesgo Bajo - En Tratamiento Especial', que integra situaciones de refinanciaciones otorgadas por primera vez dentro del año calendario.

**Citas del agente:**
```json
[
  {
    "source_doc": "TO_clasificacion_deudores_actual.pdf",
    "location": "Punto 7.2. Niveles de clasificación. (parte 1)"
  }
]
```

**Justificación del juez (verbatim):**
```json
{
  "correctitud": "Afirmación central falsa: Los niveles de clasificación para deudores de la cartera comercial según el BCRA son: Situación Normal, Riesgo Bajo - En Observación, Riesgo Bajo - En Tratamiento Especial, Riesgo Medio, Riesgo Alto e Irrecuperable.; El nivel con seguimiento especial es 'Riesgo Bajo - En Tratamiento Especial'.; Las situaciones que integran el nivel 'Riesgo Bajo - En Tratamiento Especial' son refinanciaciones otorgadas por primera vez dentro del año calendario.",
  "completitud": "Todas las patas cubiertas.",
  "citas": "El agente cita el documento correcto (TO_clasificacion_deudores_actual.pdf) pero apunta al Punto 7.2 en lugar de los Puntos 6.5 a 6.5.5 indicados en el referente."
}
```

**Paso 1 del juez (descomposición, verbatim):**
```json
{
  "afirmaciones_verificables": [
    {
      "enunciado": "Los niveles de clasificación para deudores de la cartera comercial según el BCRA son: Situación Normal, Riesgo Bajo - En Observación, Riesgo Bajo - En Tratamiento Especial, Riesgo Medio, Riesgo Alto e Irrecuperable.",
      "central": true
    },
    {
      "enunciado": "El nivel 'Situación Normal' comprende clientes que atienden en forma puntual el pago de sus obligaciones o con atrasos que no superan los 31 días.",
      "central": true
    },
    {
      "enunciado": "El nivel 'Riesgo Bajo - En Observación' comprende clientes que registran incumplimientos ocasionales con atrasos de más de 31 hasta 90 días.",
      "central": true
    },
    {
      "enunciado": "El nivel 'Riesgo Bajo - En Tratamiento Especial' requiere reclasificación única tras pago en caso de refinanciaciones otorgadas por primera vez dentro del año calendario.",
      "central": true
    },
    {
      "enunciado": "El nivel 'Riesgo Medio' comprende clientes que muestran alguna incapacidad para cancelar sus obligaciones, con atrasos de más de 90 hasta 180 días.",
      "central": true
    },
    {
      "enunciado": "El nivel 'Riesgo Alto' comprende clientes con atrasos de más de 180 días hasta un año.",
      "central": true
    },
    {
      "enunciado": "El nivel 'Irrecuperable' comprende clientes insolventes o en quiebra con nula o escasa posibilidad de recuperación del crédito o con atrasos superiores al año.",
      "central": true
    },
    {
      "enunciado": "El nivel con seguimiento especial es 'Riesgo Bajo - En Tratamiento Especial'.",
      "central": true
    },
    {
      "enunciado": "Las situaciones que integran el nivel 'Riesgo Bajo - En Tratamiento Especial' son refinanciaciones otorgadas por primera vez dentro del año calendario.",
      "central": true
    }
  ],
  "reportes_de_alcance": [],
  "patas_de_la_pregunta": [
    "Niveles de clasificación previstos para los deudores de la cartera comercial",
    "Situaciones que integran el nivel con seguimiento especial"
  ]
}
```

**Paso 2 del juez (verificaciones, verbatim):**
```json
{
  "verificaciones": [
    {
      "enunciado": "Los niveles de clasificación para deudores de la cartera comercial según el BCRA son: Situación Normal, Riesgo Bajo - En Observación, Riesgo Bajo - En Tratamiento Especial, Riesgo Medio, Riesgo Alto e Irrecuperable.",
      "central": true,
      "verdict": "falso"
    },
    {
      "enunciado": "El nivel 'Situación Normal' comprende clientes que atienden en forma puntual el pago de sus obligaciones o con atrasos que no superan los 31 días.",
      "central": true,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "El nivel 'Riesgo Bajo - En Observación' comprende clientes que registran incumplimientos ocasionales con atrasos de más de 31 hasta 90 días.",
      "central": true,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "El nivel 'Riesgo Bajo - En Tratamiento Especial' requiere reclasificación única tras pago en caso de refinanciaciones otorgadas por primera vez dentro del año calendario.",
      "central": true,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "El nivel 'Riesgo Medio' comprende clientes que muestran alguna incapacidad para cancelar sus obligaciones, con atrasos de más de 90 hasta 180 días.",
      "central": true,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "El nivel 'Riesgo Alto' comprende clientes con atrasos de más de 180 días hasta un año.",
      "central": true,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "El nivel 'Irrecuperable' comprende clientes insolventes o en quiebra con nula o escasa posibilidad de recuperación del crédito o con atrasos superiores al año.",
      "central": true,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "El nivel con seguimiento especial es 'Riesgo Bajo - En Tratamiento Especial'.",
      "central": true,
      "verdict": "falso"
    },
    {
      "enunciado": "Las situaciones que integran el nivel 'Riesgo Bajo - En Tratamiento Especial' son refinanciaciones otorgadas por primera vez dentro del año calendario.",
      "central": true,
      "verdict": "falso"
    }
  ],
  "cobertura_patas": [
    {
      "pata": "Niveles de clasificación previstos para los deudores de la cartera comercial",
      "cobertura": "cubierta"
    },
    {
      "pata": "Situaciones que integran el nivel con seguimiento especial",
      "cobertura": "cubierta"
    }
  ],
  "cita_documento_correcto": true,
  "cita_precision": "punto",
  "abstencion": null,
  "especulacion_en_prosa": null,
  "justificacion": {
    "citas": "El agente cita el documento correcto (TO_clasificacion_deudores_actual.pdf) pero apunta al Punto 7.2 en lugar de los Puntos 6.5 a 6.5.5 indicados en el referente.",
    "abstencion": ""
  }
}
```

### EV1-011 · réplica 3 — FLAGGEADA

- Veredicto del juez: correctitud=`incorrecta`, completitud=`completa`, cita_documento_correcto=`True`, cita_precision=`punto` | hit_tool_limit=True | pasos=15

- **Motivo mecánico del flag** — afirmaciones CENTRALES `no_soportado` (6):

  - El nivel 'Situación Normal' comprende clientes que atienden puntualmente sus obligaciones o con atrasos que no superan los 31 días.
  - El nivel 'Riesgo Bajo - En Observación' comprende clientes con atrasos de más de 31 hasta 90 días.
  - El nivel 'Riesgo Bajo - En Tratamiento Especial' requiere reclasificación única tras pago en caso de refinanciaciones otorgadas por primera vez dentro del año calendario.
  - El nivel 'Riesgo Medio' comprende clientes con atrasos de más de 90 hasta 180 días.
  - El nivel 'Riesgo Alto' comprende clientes con atrasos de más de 180 días hasta un año.
  - El nivel 'Irrecuperable' comprende clientes insolventes o en quiebra con nula o escasa posibilidad de recuperación del crédito o con atrasos superiores al año.

**Respuesta completa del agente (verbatim):**

> Según la regulación del BCRA, los niveles de clasificación previstos para los deudores de la cartera comercial son: 1) Situación Normal: comprende los clientes que atienden en forma puntual el pago de sus obligaciones o con atrasos que no superan los 31 días; 2) Riesgo Bajo - En Observación: comprende los clientes que registran incumplimientos ocasionales en la atención de sus obligaciones, con atrasos de más de 31 hasta 90 días; 3) Riesgo Bajo - En Tratamiento Especial: nivel que requiere reclasificación única tras pago en caso de refinanciaciones otorgadas por primera vez dentro del año calendario; 4) Riesgo Medio: comprende los clientes que muestran alguna incapacidad para cancelar sus obligaciones, con atrasos de más de 90 hasta 180 días; 5) Riesgo Alto: comprende a los clientes con atrasos de más de 180 días hasta un año; 6) Irrecuperable: comprende a los clientes insolventes o en quiebra con nula o escasa posibilidad de recuperación del crédito o con atrasos superiores al año. El nivel con seguimiento especial es 'Riesgo Bajo - En Tratamiento Especial', que integra situaciones de refinanciaciones otorgadas por primera vez dentro del año calendario.

**Citas del agente:**
```json
[
  {
    "source_doc": "TO_clasificacion_deudores_actual.pdf",
    "location": "Punto 7.2. Niveles de clasificación. (parte 1)"
  }
]
```

**Justificación del juez (verbatim):**
```json
{
  "correctitud": "Afirmación central falsa: La cartera comercial tiene 6 niveles de clasificación de deudores según la regulación del BCRA.; El nivel 2 se denomina 'Riesgo Bajo - En Observación'.; El nivel 3 se denomina 'Riesgo Bajo - En Tratamiento Especial'.; El nivel 4 se denomina 'Riesgo Medio'.; El nivel 5 se denomina 'Riesgo Alto'.; El nivel con seguimiento especial es 'Riesgo Bajo - En Tratamiento Especial'.; Las situaciones que integran el nivel 'Riesgo Bajo - En Tratamiento Especial' son refinanciaciones otorgadas por primera vez dentro del año calendario.",
  "completitud": "Todas las patas cubiertas.",
  "citas": "La cita apunta al documento correcto (TO_clasificacion_deudores_actual.pdf) pero a un punto incorrecto (7.2 en lugar de 6.5 y subsecciones), lo que no invalida el documento pero sí la precisión del punto."
}
```

**Paso 1 del juez (descomposición, verbatim):**
```json
{
  "afirmaciones_verificables": [
    {
      "enunciado": "La cartera comercial tiene 6 niveles de clasificación de deudores según la regulación del BCRA.",
      "central": true
    },
    {
      "enunciado": "El nivel 1 se denomina 'Situación Normal'.",
      "central": true
    },
    {
      "enunciado": "El nivel 'Situación Normal' comprende clientes que atienden puntualmente sus obligaciones o con atrasos que no superan los 31 días.",
      "central": true
    },
    {
      "enunciado": "El nivel 2 se denomina 'Riesgo Bajo - En Observación'.",
      "central": true
    },
    {
      "enunciado": "El nivel 'Riesgo Bajo - En Observación' comprende clientes con atrasos de más de 31 hasta 90 días.",
      "central": true
    },
    {
      "enunciado": "El nivel 3 se denomina 'Riesgo Bajo - En Tratamiento Especial'.",
      "central": true
    },
    {
      "enunciado": "El nivel 'Riesgo Bajo - En Tratamiento Especial' requiere reclasificación única tras pago en caso de refinanciaciones otorgadas por primera vez dentro del año calendario.",
      "central": true
    },
    {
      "enunciado": "El nivel 4 se denomina 'Riesgo Medio'.",
      "central": true
    },
    {
      "enunciado": "El nivel 'Riesgo Medio' comprende clientes con atrasos de más de 90 hasta 180 días.",
      "central": true
    },
    {
      "enunciado": "El nivel 5 se denomina 'Riesgo Alto'.",
      "central": true
    },
    {
      "enunciado": "El nivel 'Riesgo Alto' comprende clientes con atrasos de más de 180 días hasta un año.",
      "central": true
    },
    {
      "enunciado": "El nivel 6 se denomina 'Irrecuperable'.",
      "central": true
    },
    {
      "enunciado": "El nivel 'Irrecuperable' comprende clientes insolventes o en quiebra con nula o escasa posibilidad de recuperación del crédito o con atrasos superiores al año.",
      "central": true
    },
    {
      "enunciado": "El nivel con seguimiento especial es 'Riesgo Bajo - En Tratamiento Especial'.",
      "central": true
    },
    {
      "enunciado": "Las situaciones que integran el nivel 'Riesgo Bajo - En Tratamiento Especial' son refinanciaciones otorgadas por primera vez dentro del año calendario.",
      "central": true
    }
  ],
  "reportes_de_alcance": [],
  "patas_de_la_pregunta": [
    "Niveles de clasificación previstos para los deudores de la cartera comercial",
    "Situaciones que integran el nivel con seguimiento especial"
  ]
}
```

**Paso 2 del juez (verificaciones, verbatim):**
```json
{
  "verificaciones": [
    {
      "enunciado": "La cartera comercial tiene 6 niveles de clasificación de deudores según la regulación del BCRA.",
      "central": true,
      "verdict": "falso"
    },
    {
      "enunciado": "El nivel 1 se denomina 'Situación Normal'.",
      "central": true,
      "verdict": "verdadero"
    },
    {
      "enunciado": "El nivel 'Situación Normal' comprende clientes que atienden puntualmente sus obligaciones o con atrasos que no superan los 31 días.",
      "central": true,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "El nivel 2 se denomina 'Riesgo Bajo - En Observación'.",
      "central": true,
      "verdict": "falso"
    },
    {
      "enunciado": "El nivel 'Riesgo Bajo - En Observación' comprende clientes con atrasos de más de 31 hasta 90 días.",
      "central": true,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "El nivel 3 se denomina 'Riesgo Bajo - En Tratamiento Especial'.",
      "central": true,
      "verdict": "falso"
    },
    {
      "enunciado": "El nivel 'Riesgo Bajo - En Tratamiento Especial' requiere reclasificación única tras pago en caso de refinanciaciones otorgadas por primera vez dentro del año calendario.",
      "central": true,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "El nivel 4 se denomina 'Riesgo Medio'.",
      "central": true,
      "verdict": "falso"
    },
    {
      "enunciado": "El nivel 'Riesgo Medio' comprende clientes con atrasos de más de 90 hasta 180 días.",
      "central": true,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "El nivel 5 se denomina 'Riesgo Alto'.",
      "central": true,
      "verdict": "falso"
    },
    {
      "enunciado": "El nivel 'Riesgo Alto' comprende clientes con atrasos de más de 180 días hasta un año.",
      "central": true,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "El nivel 6 se denomina 'Irrecuperable'.",
      "central": true,
      "verdict": "verdadero"
    },
    {
      "enunciado": "El nivel 'Irrecuperable' comprende clientes insolventes o en quiebra con nula o escasa posibilidad de recuperación del crédito o con atrasos superiores al año.",
      "central": true,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "El nivel con seguimiento especial es 'Riesgo Bajo - En Tratamiento Especial'.",
      "central": true,
      "verdict": "falso"
    },
    {
      "enunciado": "Las situaciones que integran el nivel 'Riesgo Bajo - En Tratamiento Especial' son refinanciaciones otorgadas por primera vez dentro del año calendario.",
      "central": true,
      "verdict": "falso"
    }
  ],
  "cobertura_patas": [
    {
      "pata": "Niveles de clasificación previstos para los deudores de la cartera comercial",
      "cobertura": "cubierta"
    },
    {
      "pata": "Situaciones que integran el nivel con seguimiento especial",
      "cobertura": "cubierta"
    }
  ],
  "cita_documento_correcto": true,
  "cita_precision": "punto",
  "abstencion": null,
  "especulacion_en_prosa": null,
  "justificacion": {
    "citas": "La cita apunta al documento correcto (TO_clasificacion_deudores_actual.pdf) pero a un punto incorrecto (7.2 en lugar de 6.5 y subsecciones), lo que no invalida el documento pero sí la precisión del punto.",
    "abstencion": ""
  }
}
```

**Contexto de las 3 réplicas de EV1-011 en v3 (sin comentario):** r1: correctitud=`incorrecta` (flaggeada) · r2: correctitud=`incorrecta` (flaggeada) · r3: correctitud=`incorrecta` (flaggeada)


---

## EV1-015 — sujeto · ['TO_clasificacion_deudores_actual.pdf']

**Pregunta (verbatim):** Según el criterio general, ¿qué clientes deben ser clasificados por la entidad financiera? ¿Alcanza la obligación a los residentes en el exterior?

**Respuesta esperada (key adjudicada, verbatim):** Deben clasificarse todos los clientes de la entidad por las financiaciones comprendidas: tanto los residentes en el país —de los sectores público y privado, financieros y no financieros— como los residentes en el exterior, desde el punto de vista de la calidad de los obligados en orden al cumplimiento de sus compromisos.

**Estado mecánico de la mayoría en v3:** veredictos ['correcta', 'correcta', 'correcta'] → n_correcta=3, correcto_mayoria=True, patrón 3-0


### EV1-015 · réplica 1 — FLAGGEADA

- Veredicto del juez: correctitud=`correcta`, completitud=`parcial`, cita_documento_correcto=`True`, cita_precision=`punto` | hit_tool_limit=False | pasos=8

- **Motivo mecánico del flag** — afirmaciones CENTRALES `no_soportado` (6):

  - Las entidades financieras deben clasificar a los deudores considerando pautas objetivas vinculadas al grado de cumplimiento de obligaciones.
  - Las entidades financieras deben clasificar a los deudores considerando la situación jurídica del deudor.
  - Las entidades financieras deben clasificar a los deudores considerando informaciones de la Central de deudores del sistema financiero.
  - Las entidades financieras deben clasificar a los deudores considerando la base de Deudores en situación irregular de ex entidades financieras.
  - Las entidades financieras deben clasificar a los deudores considerando la situación de aplicación de pautas de refinanciación.
  - Para clientes residentes en el exterior, además de los criterios generales, debe tenerse en cuenta el 'riesgo país'.

**Respuesta completa del agente (verbatim):**

> Según el criterio general, las entidades financieras deben clasificar a los deudores considerando pautas objetivas vinculadas al grado de cumplimiento de obligaciones, situación jurídica, informaciones de la Central de deudores del sistema financiero, base de Deudores en situación irregular de ex entidades financieras y situación de aplicación de pautas de refinanciación. Esta clasificación debe efectuarse mensualmente.
> 
> Respecto a los residentes en el exterior, la obligación SÍ alcanza a estos clientes. Las entidades financieras (comprendidas sus filiales en el país y en el exterior) deben observar las normas de clasificación de deudores en forma individual. Para los casos de clientes residentes en el exterior, además de los criterios generales, deberá tenerse en cuenta también los criterios relacionados con el 'riesgo país', considerando aspectos como: i) la situación económica del país de residencia; ii) el tamaño y la estructura de la deuda externa en relación con la economía; iii) las debilidades implícitas en la cuenta corriente del país y iv) la evaluación del historial financiero del país.

**Citas del agente:**
```json
[
  {
    "source_doc": "TO_clasificacion_deudores_actual.pdf",
    "location": "Punto 7.1. Criterio de clasificación."
  },
  {
    "source_doc": "TO_clasificacion_deudores_actual.pdf",
    "location": "Punto 9.1. Base individual."
  },
  {
    "source_doc": "TO_clasificacion_deudores_actual.pdf",
    "location": "Punto 6.2. Criterio de clasificación."
  }
]
```

**Justificación del juez (verbatim):**
```json
{
  "correctitud": "Centrales todas verdaderas o no_soportadas; ninguna afirmación falsa.",
  "completitud": "Patas no cubiertas: Qué clientes deben ser clasificados por la entidad financiera según el criterio general",
  "citas": "El agente cita el documento correcto (TO_clasificacion_deudores_actual.pdf) con precisión a nivel punto, pero apunta a los puntos 7.1, 9.1 y 6.2, mientras que el referente indica que la información relevante se encuentra en el Punto 1.1."
}
```

**Paso 1 del juez (descomposición, verbatim):**
```json
{
  "afirmaciones_verificables": [
    {
      "enunciado": "Las entidades financieras deben clasificar a los deudores considerando pautas objetivas vinculadas al grado de cumplimiento de obligaciones.",
      "central": true
    },
    {
      "enunciado": "Las entidades financieras deben clasificar a los deudores considerando la situación jurídica del deudor.",
      "central": true
    },
    {
      "enunciado": "Las entidades financieras deben clasificar a los deudores considerando informaciones de la Central de deudores del sistema financiero.",
      "central": true
    },
    {
      "enunciado": "Las entidades financieras deben clasificar a los deudores considerando la base de Deudores en situación irregular de ex entidades financieras.",
      "central": true
    },
    {
      "enunciado": "Las entidades financieras deben clasificar a los deudores considerando la situación de aplicación de pautas de refinanciación.",
      "central": true
    },
    {
      "enunciado": "La clasificación de deudores debe efectuarse mensualmente.",
      "central": false
    },
    {
      "enunciado": "La obligación de clasificar deudores alcanza a los clientes residentes en el exterior.",
      "central": true
    },
    {
      "enunciado": "Las entidades financieras, comprendidas sus filiales en el país y en el exterior, deben observar las normas de clasificación de deudores en forma individual.",
      "central": false
    },
    {
      "enunciado": "Para clientes residentes en el exterior, además de los criterios generales, debe tenerse en cuenta el 'riesgo país'.",
      "central": true
    },
    {
      "enunciado": "El criterio de riesgo país para clientes residentes en el exterior incluye la situación económica del país de residencia.",
      "central": false
    },
    {
      "enunciado": "El criterio de riesgo país para clientes residentes en el exterior incluye el tamaño y la estructura de la deuda externa en relación con la economía.",
      "central": false
    },
    {
      "enunciado": "El criterio de riesgo país para clientes residentes en el exterior incluye las debilidades implícitas en la cuenta corriente del país.",
      "central": false
    },
    {
      "enunciado": "El criterio de riesgo país para clientes residentes en el exterior incluye la evaluación del historial financiero del país.",
      "central": false
    }
  ],
  "reportes_de_alcance": [],
  "patas_de_la_pregunta": [
    "Qué clientes deben ser clasificados por la entidad financiera según el criterio general",
    "Si la obligación de clasificación alcanza a los residentes en el exterior"
  ]
}
```

**Paso 2 del juez (verificaciones, verbatim):**
```json
{
  "verificaciones": [
    {
      "enunciado": "Las entidades financieras deben clasificar a los deudores considerando pautas objetivas vinculadas al grado de cumplimiento de obligaciones.",
      "central": true,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "Las entidades financieras deben clasificar a los deudores considerando la situación jurídica del deudor.",
      "central": true,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "Las entidades financieras deben clasificar a los deudores considerando informaciones de la Central de deudores del sistema financiero.",
      "central": true,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "Las entidades financieras deben clasificar a los deudores considerando la base de Deudores en situación irregular de ex entidades financieras.",
      "central": true,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "Las entidades financieras deben clasificar a los deudores considerando la situación de aplicación de pautas de refinanciación.",
      "central": true,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "La clasificación de deudores debe efectuarse mensualmente.",
      "central": false,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "La obligación de clasificar deudores alcanza a los clientes residentes en el exterior.",
      "central": true,
      "verdict": "verdadero"
    },
    {
      "enunciado": "Las entidades financieras, comprendidas sus filiales en el país y en el exterior, deben observar las normas de clasificación de deudores en forma individual.",
      "central": false,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "Para clientes residentes en el exterior, además de los criterios generales, debe tenerse en cuenta el 'riesgo país'.",
      "central": true,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "El criterio de riesgo país para clientes residentes en el exterior incluye la situación económica del país de residencia.",
      "central": false,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "El criterio de riesgo país para clientes residentes en el exterior incluye el tamaño y la estructura de la deuda externa en relación con la economía.",
      "central": false,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "El criterio de riesgo país para clientes residentes en el exterior incluye las debilidades implícitas en la cuenta corriente del país.",
      "central": false,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "El criterio de riesgo país para clientes residentes en el exterior incluye la evaluación del historial financiero del país.",
      "central": false,
      "verdict": "no_soportado"
    }
  ],
  "cobertura_patas": [
    {
      "pata": "Qué clientes deben ser clasificados por la entidad financiera según el criterio general",
      "cobertura": "no_cubierta"
    },
    {
      "pata": "Si la obligación de clasificación alcanza a los residentes en el exterior",
      "cobertura": "cubierta"
    }
  ],
  "cita_documento_correcto": true,
  "cita_precision": "punto",
  "abstencion": null,
  "especulacion_en_prosa": null,
  "justificacion": {
    "citas": "El agente cita el documento correcto (TO_clasificacion_deudores_actual.pdf) con precisión a nivel punto, pero apunta a los puntos 7.1, 9.1 y 6.2, mientras que el referente indica que la información relevante se encuentra en el Punto 1.1.",
    "abstencion": ""
  }
}
```

### EV1-015 · réplica 2 — FLAGGEADA

- Veredicto del juez: correctitud=`correcta`, completitud=`parcial`, cita_documento_correcto=`True`, cita_precision=`punto` | hit_tool_limit=False | pasos=10

- **Motivo mecánico del flag** — afirmaciones CENTRALES `no_soportado` (9):

  - La clasificación de clientes debe efectuarse al cabo de cada mes.
  - La clasificación de clientes se basa exclusivamente en pautas objetivas.
  - Las pautas objetivas incluyen el grado de cumplimiento de obligaciones.
  - Las pautas objetivas incluyen la situación jurídica del cliente.
  - Las pautas objetivas incluyen informaciones de la Central de deudores del sistema financiero.
  - Las pautas objetivas incluyen la base de Deudores en situación irregular de ex entidades financieras.
  - Las pautas objetivas incluyen la situación de aplicación de pautas de refinanciación.
  - Las entidades financieras, comprendidas sus filiales en el país y en el exterior, deben observar las normas de clasificación de deudores en forma individual.
  - Para clientes residentes en el exterior se debe tener en cuenta el criterio de 'riesgo país'.

**Respuesta completa del agente (verbatim):**

> Según el criterio general, la clasificación de clientes debe efectuarse considerando al cabo de cada mes exclusivamente pautas objetivas vinculadas al grado de cumplimiento de obligaciones, situación jurídica, informaciones de Central de deudores del sistema financiero, base de Deudores en situación irregular de ex entidades financieras y situación de aplicación de pautas de refinanciación.
> 
> Respecto a los residentes en el exterior, la obligación SÍ alcanza a estos clientes. Las entidades financieras (comprendidas sus filiales en el país y en el exterior) deben observar las normas en materia de clasificación de deudores en forma individual. Específicamente, en los casos de clientes residentes en el exterior, deberá tenerse en cuenta también los criterios relacionados con el 'riesgo país', considerando aspectos como: i) la situación económica del país de residencia; ii) el tamaño y la estructura de la deuda externa en relación con la economía; iii) las debilidades implícitas en la cuenta corriente del país y iv) la evaluación del historial financiero del país.

**Citas del agente:**
```json
[
  {
    "source_doc": "TO_clasificacion_deudores_actual.pdf",
    "location": "Punto 7.1. Criterio de clasificación."
  },
  {
    "source_doc": "TO_clasificacion_deudores_actual.pdf",
    "location": "Punto 6.2. Criterio de clasificación."
  },
  {
    "source_doc": "TO_clasificacion_deudores_actual.pdf",
    "location": "Punto 9.1. Base individual."
  }
]
```

**Justificación del juez (verbatim):**
```json
{
  "correctitud": "Centrales todas verdaderas o no_soportadas; ninguna afirmación falsa.",
  "completitud": "Patas no cubiertas: Qué clientes deben ser clasificados por la entidad financiera según el criterio general",
  "citas": "El agente cita el documento correcto (TO_clasificacion_deudores_actual.pdf) con precisión a nivel de punto, pero apunta a los Puntos 7.1, 6.2 y 9.1 en lugar del Punto 1.1 que es el referente de verdad; la mayoría de las afirmaciones no pueden verificarse contra el referente disponible (Punto 1.1), que solo confirma que la obligación alcanza a residentes en el exterior."
}
```

**Paso 1 del juez (descomposición, verbatim):**
```json
{
  "afirmaciones_verificables": [
    {
      "enunciado": "La clasificación de clientes debe efectuarse al cabo de cada mes.",
      "central": true
    },
    {
      "enunciado": "La clasificación de clientes se basa exclusivamente en pautas objetivas.",
      "central": true
    },
    {
      "enunciado": "Las pautas objetivas incluyen el grado de cumplimiento de obligaciones.",
      "central": true
    },
    {
      "enunciado": "Las pautas objetivas incluyen la situación jurídica del cliente.",
      "central": true
    },
    {
      "enunciado": "Las pautas objetivas incluyen informaciones de la Central de deudores del sistema financiero.",
      "central": true
    },
    {
      "enunciado": "Las pautas objetivas incluyen la base de Deudores en situación irregular de ex entidades financieras.",
      "central": true
    },
    {
      "enunciado": "Las pautas objetivas incluyen la situación de aplicación de pautas de refinanciación.",
      "central": true
    },
    {
      "enunciado": "La obligación de clasificación de clientes alcanza a los residentes en el exterior.",
      "central": true
    },
    {
      "enunciado": "Las entidades financieras, comprendidas sus filiales en el país y en el exterior, deben observar las normas de clasificación de deudores en forma individual.",
      "central": true
    },
    {
      "enunciado": "Para clientes residentes en el exterior se debe tener en cuenta el criterio de 'riesgo país'.",
      "central": true
    },
    {
      "enunciado": "El criterio de riesgo país incluye la situación económica del país de residencia.",
      "central": false
    },
    {
      "enunciado": "El criterio de riesgo país incluye el tamaño y la estructura de la deuda externa en relación con la economía.",
      "central": false
    },
    {
      "enunciado": "El criterio de riesgo país incluye las debilidades implícitas en la cuenta corriente del país.",
      "central": false
    },
    {
      "enunciado": "El criterio de riesgo país incluye la evaluación del historial financiero del país.",
      "central": false
    }
  ],
  "reportes_de_alcance": [],
  "patas_de_la_pregunta": [
    "Qué clientes deben ser clasificados por la entidad financiera según el criterio general",
    "Si la obligación de clasificación alcanza a los residentes en el exterior"
  ]
}
```

**Paso 2 del juez (verificaciones, verbatim):**
```json
{
  "verificaciones": [
    {
      "enunciado": "La clasificación de clientes debe efectuarse al cabo de cada mes.",
      "central": true,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "La clasificación de clientes se basa exclusivamente en pautas objetivas.",
      "central": true,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "Las pautas objetivas incluyen el grado de cumplimiento de obligaciones.",
      "central": true,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "Las pautas objetivas incluyen la situación jurídica del cliente.",
      "central": true,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "Las pautas objetivas incluyen informaciones de la Central de deudores del sistema financiero.",
      "central": true,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "Las pautas objetivas incluyen la base de Deudores en situación irregular de ex entidades financieras.",
      "central": true,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "Las pautas objetivas incluyen la situación de aplicación de pautas de refinanciación.",
      "central": true,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "La obligación de clasificación de clientes alcanza a los residentes en el exterior.",
      "central": true,
      "verdict": "verdadero"
    },
    {
      "enunciado": "Las entidades financieras, comprendidas sus filiales en el país y en el exterior, deben observar las normas de clasificación de deudores en forma individual.",
      "central": true,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "Para clientes residentes en el exterior se debe tener en cuenta el criterio de 'riesgo país'.",
      "central": true,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "El criterio de riesgo país incluye la situación económica del país de residencia.",
      "central": false,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "El criterio de riesgo país incluye el tamaño y la estructura de la deuda externa en relación con la economía.",
      "central": false,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "El criterio de riesgo país incluye las debilidades implícitas en la cuenta corriente del país.",
      "central": false,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "El criterio de riesgo país incluye la evaluación del historial financiero del país.",
      "central": false,
      "verdict": "no_soportado"
    }
  ],
  "cobertura_patas": [
    {
      "pata": "Qué clientes deben ser clasificados por la entidad financiera según el criterio general",
      "cobertura": "no_cubierta"
    },
    {
      "pata": "Si la obligación de clasificación alcanza a los residentes en el exterior",
      "cobertura": "cubierta"
    }
  ],
  "cita_documento_correcto": true,
  "cita_precision": "punto",
  "abstencion": null,
  "especulacion_en_prosa": null,
  "justificacion": {
    "citas": "El agente cita el documento correcto (TO_clasificacion_deudores_actual.pdf) con precisión a nivel de punto, pero apunta a los Puntos 7.1, 6.2 y 9.1 en lugar del Punto 1.1 que es el referente de verdad; la mayoría de las afirmaciones no pueden verificarse contra el referente disponible (Punto 1.1), que solo confirma que la obligación alcanza a residentes en el exterior.",
    "abstencion": ""
  }
}
```

### EV1-015 · réplica 3 — FLAGGEADA

- Veredicto del juez: correctitud=`correcta`, completitud=`completa`, cita_documento_correcto=`True`, cita_precision=`punto` | hit_tool_limit=False | pasos=11

- **Motivo mecánico del flag** — afirmaciones CENTRALES `no_soportado` (1):

  - Para clientes residentes en el exterior debe tenerse en cuenta el criterio de 'riesgo país'.

**Respuesta completa del agente (verbatim):**

> Según el criterio general, las entidades financieras deben clasificar a todos los clientes considerando pautas objetivas vinculadas al grado de cumplimiento de obligaciones, situación jurídica, informaciones de Central de deudores del sistema financiero, base de Deudores en situación irregular de ex entidades financieras y situación de aplicación de pautas de refinanciación. Esta clasificación debe efectuarse mensualmente.
> 
> Respecto de los residentes en el exterior, la obligación SÍ alcanza a estos clientes. Las entidades financieras (comprendidas sus filiales en el país y en el exterior) observarán las normas en materia de clasificación de deudores en forma individual. Además, en los casos de clientes residentes en el exterior, deberá tenerse en cuenta también los criterios relacionados con el 'riesgo país', considerando aspectos como: i) la situación económica del país de residencia; ii) el tamaño y la estructura de la deuda externa en relación con la economía; iii) las debilidades implícitas en la cuenta corriente del país y iv) la evaluación del historial financiero del país.

**Citas del agente:**
```json
[
  {
    "source_doc": "TO_clasificacion_deudores_actual.pdf",
    "location": "Punto 7.1. Criterio de clasificación."
  },
  {
    "source_doc": "TO_clasificacion_deudores_actual.pdf",
    "location": "Punto 9.1. Base individual."
  },
  {
    "source_doc": "TO_clasificacion_deudores_actual.pdf",
    "location": "Punto 6.2. Criterio de clasificación."
  }
]
```

**Justificación del juez (verbatim):**
```json
{
  "correctitud": "Centrales todas verdaderas o no_soportadas; ninguna afirmación falsa.",
  "completitud": "Todas las patas cubiertas.",
  "citas": "El agente cita TO_clasificacion_deudores_actual.pdf con precisión a nivel punto (7.1, 9.1, 6.2), aunque el referente indica que la información corresponde al Punto 1.1; el documento es correcto."
}
```

**Paso 1 del juez (descomposición, verbatim):**
```json
{
  "afirmaciones_verificables": [
    {
      "enunciado": "Las entidades financieras deben clasificar a todos los clientes.",
      "central": true
    },
    {
      "enunciado": "La clasificación considera pautas objetivas vinculadas al grado de cumplimiento de obligaciones.",
      "central": false
    },
    {
      "enunciado": "La clasificación considera la situación jurídica del cliente.",
      "central": false
    },
    {
      "enunciado": "La clasificación considera informaciones de la Central de deudores del sistema financiero.",
      "central": false
    },
    {
      "enunciado": "La clasificación considera la base de Deudores en situación irregular de ex entidades financieras.",
      "central": false
    },
    {
      "enunciado": "La clasificación considera la situación de aplicación de pautas de refinanciación.",
      "central": false
    },
    {
      "enunciado": "La clasificación de clientes debe efectuarse mensualmente.",
      "central": false
    },
    {
      "enunciado": "La obligación de clasificar clientes alcanza a los residentes en el exterior.",
      "central": true
    },
    {
      "enunciado": "Las entidades financieras, comprendidas sus filiales en el país y en el exterior, observarán las normas en materia de clasificación de deudores en forma individual.",
      "central": false
    },
    {
      "enunciado": "Para clientes residentes en el exterior debe tenerse en cuenta el criterio de 'riesgo país'.",
      "central": true
    },
    {
      "enunciado": "El criterio de riesgo país incluye la situación económica del país de residencia.",
      "central": false
    },
    {
      "enunciado": "El criterio de riesgo país incluye el tamaño y la estructura de la deuda externa en relación con la economía.",
      "central": false
    },
    {
      "enunciado": "El criterio de riesgo país incluye las debilidades implícitas en la cuenta corriente del país.",
      "central": false
    },
    {
      "enunciado": "El criterio de riesgo país incluye la evaluación del historial financiero del país.",
      "central": false
    }
  ],
  "reportes_de_alcance": [],
  "patas_de_la_pregunta": [
    "Qué clientes deben ser clasificados por la entidad financiera según el criterio general",
    "Si la obligación de clasificación alcanza a los residentes en el exterior"
  ]
}
```

**Paso 2 del juez (verificaciones, verbatim):**
```json
{
  "verificaciones": [
    {
      "enunciado": "Las entidades financieras deben clasificar a todos los clientes.",
      "central": true,
      "verdict": "verdadero"
    },
    {
      "enunciado": "La clasificación considera pautas objetivas vinculadas al grado de cumplimiento de obligaciones.",
      "central": false,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "La clasificación considera la situación jurídica del cliente.",
      "central": false,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "La clasificación considera informaciones de la Central de deudores del sistema financiero.",
      "central": false,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "La clasificación considera la base de Deudores en situación irregular de ex entidades financieras.",
      "central": false,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "La clasificación considera la situación de aplicación de pautas de refinanciación.",
      "central": false,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "La clasificación de clientes debe efectuarse mensualmente.",
      "central": false,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "La obligación de clasificar clientes alcanza a los residentes en el exterior.",
      "central": true,
      "verdict": "verdadero"
    },
    {
      "enunciado": "Las entidades financieras, comprendidas sus filiales en el país y en el exterior, observarán las normas en materia de clasificación de deudores en forma individual.",
      "central": false,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "Para clientes residentes en el exterior debe tenerse en cuenta el criterio de 'riesgo país'.",
      "central": true,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "El criterio de riesgo país incluye la situación económica del país de residencia.",
      "central": false,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "El criterio de riesgo país incluye el tamaño y la estructura de la deuda externa en relación con la economía.",
      "central": false,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "El criterio de riesgo país incluye las debilidades implícitas en la cuenta corriente del país.",
      "central": false,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "El criterio de riesgo país incluye la evaluación del historial financiero del país.",
      "central": false,
      "verdict": "no_soportado"
    }
  ],
  "cobertura_patas": [
    {
      "pata": "Qué clientes deben ser clasificados por la entidad financiera según el criterio general",
      "cobertura": "cubierta"
    },
    {
      "pata": "Si la obligación de clasificación alcanza a los residentes en el exterior",
      "cobertura": "cubierta"
    }
  ],
  "cita_documento_correcto": true,
  "cita_precision": "punto",
  "abstencion": null,
  "especulacion_en_prosa": null,
  "justificacion": {
    "citas": "El agente cita TO_clasificacion_deudores_actual.pdf con precisión a nivel punto (7.1, 9.1, 6.2), aunque el referente indica que la información corresponde al Punto 1.1; el documento es correcto.",
    "abstencion": ""
  }
}
```

**Contexto de las 3 réplicas de EV1-015 en v3 (sin comentario):** r1: correctitud=`correcta` (flaggeada) · r2: correctitud=`correcta` (flaggeada) · r3: correctitud=`correcta` (flaggeada)


---

## EV1-018 — enumerativa · ['TO_exterior_cambios_actual.pdf']

**Pregunta (verbatim):** ¿Para qué operaciones deben contar las entidades financieras y las empresas no financieras emisoras de tarjetas locales con la conformidad previa del BCRA a fin de acceder al mercado de cambios para realizar pagos al exterior por el uso de tarjetas emitidas en el país?

**Respuesta esperada (key adjudicada, verbatim):** Cuando los pagos se originen, en forma directa o indirecta a través del uso de redes de pagos internacionales, en: 1) la participación en juegos de azar y apuestas de distinto tipo; 2) la transferencia de fondos a cuentas en Proveedores de Servicios de Pago; 3) la transferencia de fondos a cuentas de inversión en administradores de inversiones radicados en el exterior; 4) la realización de operaciones cambiarias en el exterior; 5) la adquisición de criptoactivos en sus distintas modalidades; 6) la adquisición de joyas, piedras preciosas y metales preciosos; y 7) la adquisición de tarjetas de regalo o equivalentes de tiendas o locales radicados en el exterior.

**Estado mecánico de la mayoría en v3:** veredictos ['correcta', 'correcta', 'correcta'] → n_correcta=3, correcto_mayoria=True, patrón 3-0


### EV1-018 · réplica 1 — FLAGGEADA

- Veredicto del juez: correctitud=`correcta`, completitud=`parcial`, cita_documento_correcto=`True`, cita_precision=`punto` | hit_tool_limit=False | pasos=5

- **Motivo mecánico del flag** — afirmaciones CENTRALES `no_soportado` (1):

  - La conformidad previa del BCRA también es requerida para operaciones que impliquen un débito inmediato en una cuenta en una entidad financiera local.

**Respuesta completa del agente (verbatim):**

> Las entidades financieras y las empresas no financieras emisoras de tarjetas locales deberán contar con la conformidad previa del BCRA para acceder al mercado de cambios para realizar pagos al exterior por el uso de dichas tarjetas o cualquier modalidad que implique un débito inmediato en una cuenta en una entidad financiera local.

**Citas del agente:**
```json
[
  {
    "source_doc": "TO_exterior_cambios_actual.pdf",
    "location": "Punto 4.1. Operaciones con débito en una cuenta en una entidad financiera local y/o con tar"
  }
]
```

**Justificación del juez (verbatim):**
```json
{
  "correctitud": "Centrales todas verdaderas o no_soportadas; ninguna afirmación falsa.",
  "completitud": "Patas no cubiertas: Operaciones para las cuales las entidades financieras y empresas no financieras emisoras de tarjetas locales deben contar con conformidad previa del BCRA para acceder al mercado de cambios y realizar pagos al exterior por uso de tarjetas emitidas en el país",
  "citas": "La cita apunta al documento correcto (TO_exterior_cambios_actual.pdf) con precisión a nivel punto (Punto 4.1.), aunque el referente indica que la información relevante está en el Punto 4.1.4."
}
```

**Paso 1 del juez (descomposición, verbatim):**
```json
{
  "afirmaciones_verificables": [
    {
      "enunciado": "Las entidades financieras deben contar con la conformidad previa del BCRA para acceder al mercado de cambios para realizar pagos al exterior por el uso de tarjetas emitidas en el país.",
      "central": true
    },
    {
      "enunciado": "Las empresas no financieras emisoras de tarjetas locales deben contar con la conformidad previa del BCRA para acceder al mercado de cambios para realizar pagos al exterior por el uso de tarjetas emitidas en el país.",
      "central": true
    },
    {
      "enunciado": "La conformidad previa del BCRA también es requerida para operaciones que impliquen un débito inmediato en una cuenta en una entidad financiera local.",
      "central": true
    }
  ],
  "reportes_de_alcance": [],
  "patas_de_la_pregunta": [
    "Operaciones para las cuales las entidades financieras y empresas no financieras emisoras de tarjetas locales deben contar con conformidad previa del BCRA para acceder al mercado de cambios y realizar pagos al exterior por uso de tarjetas emitidas en el país"
  ]
}
```

**Paso 2 del juez (verificaciones, verbatim):**
```json
{
  "verificaciones": [
    {
      "enunciado": "Las entidades financieras deben contar con la conformidad previa del BCRA para acceder al mercado de cambios para realizar pagos al exterior por el uso de tarjetas emitidas en el país.",
      "central": true,
      "verdict": "verdadero"
    },
    {
      "enunciado": "Las empresas no financieras emisoras de tarjetas locales deben contar con la conformidad previa del BCRA para acceder al mercado de cambios para realizar pagos al exterior por el uso de tarjetas emitidas en el país.",
      "central": true,
      "verdict": "verdadero"
    },
    {
      "enunciado": "La conformidad previa del BCRA también es requerida para operaciones que impliquen un débito inmediato en una cuenta en una entidad financiera local.",
      "central": true,
      "verdict": "no_soportado"
    }
  ],
  "cobertura_patas": [
    {
      "pata": "Operaciones para las cuales las entidades financieras y empresas no financieras emisoras de tarjetas locales deben contar con conformidad previa del BCRA para acceder al mercado de cambios y realizar pagos al exterior por uso de tarjetas emitidas en el país",
      "cobertura": "no_cubierta"
    }
  ],
  "cita_documento_correcto": true,
  "cita_precision": "punto",
  "abstencion": null,
  "especulacion_en_prosa": null,
  "justificacion": {
    "citas": "La cita apunta al documento correcto (TO_exterior_cambios_actual.pdf) con precisión a nivel punto (Punto 4.1.), aunque el referente indica que la información relevante está en el Punto 4.1.4.",
    "abstencion": ""
  }
}
```

### EV1-018 · réplica 2 — FLAGGEADA

- Veredicto del juez: correctitud=`correcta`, completitud=`parcial`, cita_documento_correcto=`True`, cita_precision=`punto` | hit_tool_limit=False | pasos=3

- **Motivo mecánico del flag** — afirmaciones CENTRALES `no_soportado` (1):

  - La conformidad previa del BCRA también es requerida para operaciones que impliquen un débito inmediato en una cuenta en una entidad financiera local.

**Respuesta completa del agente (verbatim):**

> Las entidades financieras y las empresas no financieras emisoras de tarjetas locales deben contar con la conformidad previa del BCRA para acceder al mercado de cambios a fin de realizar pagos al exterior por el uso de dichas tarjetas o cualquier modalidad que implique un débito inmediato en una cuenta en una entidad financiera local.

**Citas del agente:**
```json
[
  {
    "source_doc": "TO_exterior_cambios_actual.pdf",
    "location": "Punto 4.1. Operaciones con débito en una cuenta en una entidad financiera local y/o con tar"
  }
]
```

**Justificación del juez (verbatim):**
```json
{
  "correctitud": "Centrales todas verdaderas o no_soportadas; ninguna afirmación falsa.",
  "completitud": "Patas no cubiertas: Operaciones para las cuales las entidades financieras y empresas no financieras emisoras de tarjetas locales deben contar con conformidad previa del BCRA para acceder al mercado de cambios y realizar pagos al exterior por uso de tarjetas emitidas en el país",
  "citas": "La cita apunta al documento correcto (TO_exterior_cambios_actual.pdf) con precisión a nivel punto (Punto 4.1.), aunque el referente indica que la información relevante está en el Punto 4.1.4."
}
```

**Paso 1 del juez (descomposición, verbatim):**
```json
{
  "afirmaciones_verificables": [
    {
      "enunciado": "Las entidades financieras deben contar con la conformidad previa del BCRA para acceder al mercado de cambios para realizar pagos al exterior por el uso de tarjetas emitidas en el país.",
      "central": true
    },
    {
      "enunciado": "Las empresas no financieras emisoras de tarjetas locales deben contar con la conformidad previa del BCRA para acceder al mercado de cambios para realizar pagos al exterior por el uso de tarjetas emitidas en el país.",
      "central": true
    },
    {
      "enunciado": "La conformidad previa del BCRA también es requerida para operaciones que impliquen un débito inmediato en una cuenta en una entidad financiera local.",
      "central": true
    }
  ],
  "reportes_de_alcance": [],
  "patas_de_la_pregunta": [
    "Operaciones para las cuales las entidades financieras y empresas no financieras emisoras de tarjetas locales deben contar con conformidad previa del BCRA para acceder al mercado de cambios y realizar pagos al exterior por uso de tarjetas emitidas en el país"
  ]
}
```

**Paso 2 del juez (verificaciones, verbatim):**
```json
{
  "verificaciones": [
    {
      "enunciado": "Las entidades financieras deben contar con la conformidad previa del BCRA para acceder al mercado de cambios para realizar pagos al exterior por el uso de tarjetas emitidas en el país.",
      "central": true,
      "verdict": "verdadero"
    },
    {
      "enunciado": "Las empresas no financieras emisoras de tarjetas locales deben contar con la conformidad previa del BCRA para acceder al mercado de cambios para realizar pagos al exterior por el uso de tarjetas emitidas en el país.",
      "central": true,
      "verdict": "verdadero"
    },
    {
      "enunciado": "La conformidad previa del BCRA también es requerida para operaciones que impliquen un débito inmediato en una cuenta en una entidad financiera local.",
      "central": true,
      "verdict": "no_soportado"
    }
  ],
  "cobertura_patas": [
    {
      "pata": "Operaciones para las cuales las entidades financieras y empresas no financieras emisoras de tarjetas locales deben contar con conformidad previa del BCRA para acceder al mercado de cambios y realizar pagos al exterior por uso de tarjetas emitidas en el país",
      "cobertura": "no_cubierta"
    }
  ],
  "cita_documento_correcto": true,
  "cita_precision": "punto",
  "abstencion": null,
  "especulacion_en_prosa": null,
  "justificacion": {
    "citas": "La cita apunta al documento correcto (TO_exterior_cambios_actual.pdf) con precisión a nivel punto (Punto 4.1.), aunque el referente indica que la información relevante está en el Punto 4.1.4.",
    "abstencion": ""
  }
}
```

### EV1-018 · réplica 3 — FLAGGEADA

- Veredicto del juez: correctitud=`correcta`, completitud=`parcial`, cita_documento_correcto=`True`, cita_precision=`punto` | hit_tool_limit=False | pasos=3

- **Motivo mecánico del flag** — afirmaciones CENTRALES `no_soportado` (1):

  - La conformidad previa del BCRA también es requerida para cualquier modalidad que implique un débito inmediato en una cuenta en una entidad financiera local.

**Respuesta completa del agente (verbatim):**

> Las entidades financieras y las empresas no financieras emisoras de tarjetas locales deben contar con la conformidad previa del BCRA para acceder al mercado de cambios a fin de realizar pagos al exterior por el uso de dichas tarjetas o cualquier modalidad que implique un débito inmediato en una cuenta en una entidad financiera local.

**Citas del agente:**
```json
[
  {
    "source_doc": "TO_exterior_cambios_actual.pdf",
    "location": "Punto 4.1. Operaciones con débito en una cuenta en una entidad financiera local y/o con tar"
  }
]
```

**Justificación del juez (verbatim):**
```json
{
  "correctitud": "Centrales todas verdaderas o no_soportadas; ninguna afirmación falsa.",
  "completitud": "Patas no cubiertas: Operaciones para las cuales las entidades financieras y empresas no financieras emisoras de tarjetas locales deben contar con conformidad previa del BCRA para acceder al mercado de cambios y realizar pagos al exterior por uso de tarjetas emitidas en el país",
  "citas": "La cita apunta al documento correcto (TO_exterior_cambios_actual.pdf) con precisión a nivel punto (Punto 4.1.), aunque el referente indica que la información relevante está en el Punto 4.1.4."
}
```

**Paso 1 del juez (descomposición, verbatim):**
```json
{
  "afirmaciones_verificables": [
    {
      "enunciado": "Las entidades financieras deben contar con la conformidad previa del BCRA para acceder al mercado de cambios para realizar pagos al exterior por el uso de tarjetas emitidas en el país.",
      "central": true
    },
    {
      "enunciado": "Las empresas no financieras emisoras de tarjetas locales deben contar con la conformidad previa del BCRA para acceder al mercado de cambios para realizar pagos al exterior por el uso de tarjetas emitidas en el país.",
      "central": true
    },
    {
      "enunciado": "La conformidad previa del BCRA también es requerida para cualquier modalidad que implique un débito inmediato en una cuenta en una entidad financiera local.",
      "central": true
    }
  ],
  "reportes_de_alcance": [],
  "patas_de_la_pregunta": [
    "Operaciones para las cuales las entidades financieras y empresas no financieras emisoras de tarjetas locales deben contar con conformidad previa del BCRA para acceder al mercado de cambios y realizar pagos al exterior por uso de tarjetas emitidas en el país"
  ]
}
```

**Paso 2 del juez (verificaciones, verbatim):**
```json
{
  "verificaciones": [
    {
      "enunciado": "Las entidades financieras deben contar con la conformidad previa del BCRA para acceder al mercado de cambios para realizar pagos al exterior por el uso de tarjetas emitidas en el país.",
      "central": true,
      "verdict": "verdadero"
    },
    {
      "enunciado": "Las empresas no financieras emisoras de tarjetas locales deben contar con la conformidad previa del BCRA para acceder al mercado de cambios para realizar pagos al exterior por el uso de tarjetas emitidas en el país.",
      "central": true,
      "verdict": "verdadero"
    },
    {
      "enunciado": "La conformidad previa del BCRA también es requerida para cualquier modalidad que implique un débito inmediato en una cuenta en una entidad financiera local.",
      "central": true,
      "verdict": "no_soportado"
    }
  ],
  "cobertura_patas": [
    {
      "pata": "Operaciones para las cuales las entidades financieras y empresas no financieras emisoras de tarjetas locales deben contar con conformidad previa del BCRA para acceder al mercado de cambios y realizar pagos al exterior por uso de tarjetas emitidas en el país",
      "cobertura": "no_cubierta"
    }
  ],
  "cita_documento_correcto": true,
  "cita_precision": "punto",
  "abstencion": null,
  "especulacion_en_prosa": null,
  "justificacion": {
    "citas": "La cita apunta al documento correcto (TO_exterior_cambios_actual.pdf) con precisión a nivel punto (Punto 4.1.), aunque el referente indica que la información relevante está en el Punto 4.1.4.",
    "abstencion": ""
  }
}
```

**Contexto de las 3 réplicas de EV1-018 en v3 (sin comentario):** r1: correctitud=`correcta` (flaggeada) · r2: correctitud=`correcta` (flaggeada) · r3: correctitud=`correcta` (flaggeada)


---

## EV1-028 — sujeto · ['TO_proteccion_usuarios_servicios_financieros_actual.pdf']

**Pregunta (verbatim):** Una asociación mutual que otorga financiaciones y se encuentra alcanzada por las normas sobre proveedores no financieros de crédito, ¿reviste el carácter de sujeto obligado de las normas de protección de los usuarios de servicios financieros por esas financiaciones?

**Respuesta esperada (key adjudicada, verbatim):** No. Si bien los otros proveedores no financieros de crédito alcanzados por las normas sobre proveedores no financieros de crédito son sujetos obligados, están expresamente exceptuadas las asociaciones mutuales o cooperativas por las financiaciones que otorguen.

**Estado mecánico de la mayoría en v3:** veredictos ['incorrecta', 'incorrecta', 'incorrecta'] → n_correcta=0, correcto_mayoria=False, patrón 3-0


### EV1-028 · réplica 2 — FLAGGEADA

- Veredicto del juez: correctitud=`incorrecta`, completitud=`completa`, cita_documento_correcto=`True`, cita_precision=`punto` | hit_tool_limit=False | pasos=11

- **Motivo mecánico del flag** — afirmaciones CENTRALES `no_soportado` (1):

  - Los proveedores no financieros de crédito (PNFC) son explícitamente incluidos como miembros del rol de 'Sujetos obligados (Protección de usuarios)' en el Punto 1.1.2 de las normas sobre Protección de Usuarios de Servicios Financieros del BCRA.

**Respuesta completa del agente (verbatim):**

> Sí. Una asociación mutual que otorga financiaciones y se encuentra alcanzada por las normas sobre proveedores no financieros de crédito reviste el carácter de sujeto obligado de las normas de protección de los usuarios de servicios financieros por esas financiaciones. Los proveedores no financieros de crédito (PNFC) son explícitamente incluidos como miembros del rol de 'Sujetos obligados (Protección de usuarios)' en el Punto 1.1.2 de las normas sobre Protección de Usuarios de Servicios Financieros del BCRA. En consecuencia, están sujetos a todas las obligaciones establecidas en esas normas respecto a las financiaciones que otorguen.

**Citas del agente:**
```json
[
  {
    "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
    "location": "Punto 1.1.2"
  }
]
```

**Justificación del juez (verbatim):**
```json
{
  "correctitud": "Afirmación central falsa: Una asociación mutual que otorga financiaciones y se encuentra alcanzada por las normas sobre proveedores no financieros de crédito reviste el carácter de sujeto obligado de las normas de protección de los usuarios de servicios financieros por esas financiaciones.; Los proveedores no financieros de crédito están sujetos a todas las obligaciones establecidas en las normas de protección de usuarios de servicios financieros respecto a las financiaciones que otorguen.",
  "completitud": "Todas las patas cubiertas.",
  "citas": "El agente cita el documento correcto (TO protección usuarios) con precisión a nivel punto (1.1.2), aunque el referente señala el Punto 1.1.2.5 como sección específica."
}
```

**Paso 1 del juez (descomposición, verbatim):**
```json
{
  "afirmaciones_verificables": [
    {
      "enunciado": "Una asociación mutual que otorga financiaciones y se encuentra alcanzada por las normas sobre proveedores no financieros de crédito reviste el carácter de sujeto obligado de las normas de protección de los usuarios de servicios financieros por esas financiaciones.",
      "central": true
    },
    {
      "enunciado": "Los proveedores no financieros de crédito (PNFC) son explícitamente incluidos como miembros del rol de 'Sujetos obligados (Protección de usuarios)' en el Punto 1.1.2 de las normas sobre Protección de Usuarios de Servicios Financieros del BCRA.",
      "central": true
    },
    {
      "enunciado": "Los proveedores no financieros de crédito están sujetos a todas las obligaciones establecidas en las normas de protección de usuarios de servicios financieros respecto a las financiaciones que otorguen.",
      "central": false
    }
  ],
  "reportes_de_alcance": [],
  "patas_de_la_pregunta": [
    "Si una asociación mutual que otorga financiaciones y está alcanzada por las normas sobre proveedores no financieros de crédito reviste el carácter de sujeto obligado de las normas de protección de los usuarios de servicios financieros por esas financiaciones"
  ]
}
```

**Paso 2 del juez (verificaciones, verbatim):**
```json
{
  "verificaciones": [
    {
      "enunciado": "Una asociación mutual que otorga financiaciones y se encuentra alcanzada por las normas sobre proveedores no financieros de crédito reviste el carácter de sujeto obligado de las normas de protección de los usuarios de servicios financieros por esas financiaciones.",
      "central": true,
      "verdict": "falso"
    },
    {
      "enunciado": "Los proveedores no financieros de crédito (PNFC) son explícitamente incluidos como miembros del rol de 'Sujetos obligados (Protección de usuarios)' en el Punto 1.1.2 de las normas sobre Protección de Usuarios de Servicios Financieros del BCRA.",
      "central": true,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "Los proveedores no financieros de crédito están sujetos a todas las obligaciones establecidas en las normas de protección de usuarios de servicios financieros respecto a las financiaciones que otorguen.",
      "central": false,
      "verdict": "falso"
    }
  ],
  "cobertura_patas": [
    {
      "pata": "Si una asociación mutual que otorga financiaciones y está alcanzada por las normas sobre proveedores no financieros de crédito reviste el carácter de sujeto obligado de las normas de protección de los usuarios de servicios financieros por esas financiaciones",
      "cobertura": "cubierta"
    }
  ],
  "cita_documento_correcto": true,
  "cita_precision": "punto",
  "abstencion": null,
  "especulacion_en_prosa": null,
  "justificacion": {
    "citas": "El agente cita el documento correcto (TO protección usuarios) con precisión a nivel punto (1.1.2), aunque el referente señala el Punto 1.1.2.5 como sección específica.",
    "abstencion": ""
  }
}
```

**Contexto de las 3 réplicas de EV1-028 en v3 (sin comentario):** r1: correctitud=`incorrecta` · r2: correctitud=`incorrecta` (flaggeada) · r3: correctitud=`incorrecta`


---

## EV1-034 — enumerativa · ['TO_capitales_minimos_actual.pdf']

**Pregunta (verbatim):** Enumere la totalidad de los rubros del patrimonio neto que comprende el capital ordinario de nivel uno (COn1) como conceptos computables de la responsabilidad patrimonial computable.

**Respuesta esperada (key adjudicada, verbatim):** El COn1 comprende: 1) capital social, excluyendo acciones con preferencia patrimonial; 2) aportes no capitalizados, excluyendo primas de emisión; 3) ajustes al patrimonio; 4) reservas de utilidades, excluyendo la reserva especial para instrumentos de deuda; 5) resultados no asignados; 6) otros resultados, positivos y negativos, según los porcentajes y condiciones de cómputo previstos; 7) otros resultados integrales; 8) primas de emisión resultantes de instrumentos incluidos en el COn1; y, en los casos de consolidación, 9) participaciones minoritarias (acciones ordinarias emitidas por subsidiarias sujetas a supervisión consolidada y en poder de terceros que cumplan los criterios establecidos).

**Estado mecánico de la mayoría en v3:** veredictos ['correcta', 'correcta', 'correcta'] → n_correcta=3, correcto_mayoria=True, patrón 3-0


### EV1-034 · réplica 1 — FLAGGEADA

- Veredicto del juez: correctitud=`correcta`, completitud=`completa`, cita_documento_correcto=`True`, cita_precision=`punto` | hit_tool_limit=True | pasos=15

- **Motivo mecánico del flag** — afirmaciones CENTRALES `no_soportado` (9):

  - El Capital Ordinario de Nivel Uno (COn1) comprende como rubro otros resultados integrales al 100%.
  - Dentro de otros resultados integrales se incluyen los resultados registrados en revaluación de propiedad, planta, equipo e intangibles.
  - Dentro de otros resultados integrales se incluyen las ganancias o pérdidas por instrumentos financieros a valor razonable con cambios en otros resultados integrales.
  - Dentro de otros resultados integrales se incluye el saldo deudor de partidas de otros resultados integrales no mencionadas.
  - El Capital Ordinario de Nivel Uno (COn1) comprende como rubro los resultados del último ejercicio cerrado, una vez que se cuente con dictamen del auditor.
  - El Capital Ordinario de Nivel Uno (COn1) comprende como rubro los resultados de balances trimestrales.
  - El Capital Ordinario de Nivel Uno (COn1) comprende como rubro los resultados del ejercicio en curso.
  - El Capital Ordinario de Nivel Uno (COn1) comprende como rubro los resultados mensuales posteriores a últimos balances auditados.
  - El Capital Ordinario de Nivel Uno (COn1) comprende como rubro los quebrantos contabilizados y no contabilizados.

**Respuesta completa del agente (verbatim):**

> Según la regulación del BCRA, el Capital Ordinario de Nivel Uno (COn1) como concepto computable de la responsabilidad patrimonial computable comprende los siguientes rubros del patrimonio neto: 1) Capital social (excluyendo acciones con preferencia patrimonial); 2) Aportes no capitalizados (excluyendo primas de emisión); 3) Ajustes al patrimonio y reservas de utilidades (excluyendo la reserva especial para instrumentos de deuda); 4) Otros resultados integrales al 100%, incluyendo: a) Resultados registrados en revaluación de propiedad, planta, equipo e intangibles; b) Ganancias o pérdidas por instrumentos financieros a valor razonable con cambios en otros resultados integrales; c) Saldo deudor de partidas de otros resultados integrales no mencionadas; 5) Resultados del último ejercicio cerrado (una vez que se cuente con dictamen del auditor); 6) Resultados de balances trimestrales; 7) Resultados del ejercicio en curso; 8) Resultados mensuales posteriores a últimos balances auditados; 9) Quebrantos contabilizados y no contabilizados.

**Citas del agente:**
```json
[
  {
    "source_doc": "TO_capitales_minimos_actual.pdf",
    "location": "Punto 8.2. Conceptos computables."
  },
  {
    "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
    "location": "Punto 6.2. Modelo de Información (parte 1)"
  }
]
```

**Justificación del juez (verbatim):**
```json
{
  "correctitud": "Centrales todas verdaderas o no_soportadas; ninguna afirmación falsa.",
  "completitud": "Todas las patas cubiertas.",
  "citas": "El agente cita 'TO_capitales_minimos_actual.pdf, Punto 8.2. Conceptos computables', que corresponde al documento del ground truth (Punto 8.2.1.), con precisión a nivel punto/sección."
}
```

**Paso 1 del juez (descomposición, verbatim):**
```json
{
  "afirmaciones_verificables": [
    {
      "enunciado": "El Capital Ordinario de Nivel Uno (COn1) comprende como rubro el capital social, excluyendo acciones con preferencia patrimonial.",
      "central": true
    },
    {
      "enunciado": "El Capital Ordinario de Nivel Uno (COn1) comprende como rubro los aportes no capitalizados, excluyendo primas de emisión.",
      "central": true
    },
    {
      "enunciado": "El Capital Ordinario de Nivel Uno (COn1) comprende como rubro los ajustes al patrimonio y reservas de utilidades, excluyendo la reserva especial para instrumentos de deuda.",
      "central": true
    },
    {
      "enunciado": "El Capital Ordinario de Nivel Uno (COn1) comprende como rubro otros resultados integrales al 100%.",
      "central": true
    },
    {
      "enunciado": "Dentro de otros resultados integrales se incluyen los resultados registrados en revaluación de propiedad, planta, equipo e intangibles.",
      "central": true
    },
    {
      "enunciado": "Dentro de otros resultados integrales se incluyen las ganancias o pérdidas por instrumentos financieros a valor razonable con cambios en otros resultados integrales.",
      "central": true
    },
    {
      "enunciado": "Dentro de otros resultados integrales se incluye el saldo deudor de partidas de otros resultados integrales no mencionadas.",
      "central": true
    },
    {
      "enunciado": "El Capital Ordinario de Nivel Uno (COn1) comprende como rubro los resultados del último ejercicio cerrado, una vez que se cuente con dictamen del auditor.",
      "central": true
    },
    {
      "enunciado": "El Capital Ordinario de Nivel Uno (COn1) comprende como rubro los resultados de balances trimestrales.",
      "central": true
    },
    {
      "enunciado": "El Capital Ordinario de Nivel Uno (COn1) comprende como rubro los resultados del ejercicio en curso.",
      "central": true
    },
    {
      "enunciado": "El Capital Ordinario de Nivel Uno (COn1) comprende como rubro los resultados mensuales posteriores a últimos balances auditados.",
      "central": true
    },
    {
      "enunciado": "El Capital Ordinario de Nivel Uno (COn1) comprende como rubro los quebrantos contabilizados y no contabilizados.",
      "central": true
    },
    {
      "enunciado": "La regulación del COn1 es emitida por el BCRA.",
      "central": false
    }
  ],
  "reportes_de_alcance": [],
  "patas_de_la_pregunta": [
    "Totalidad de los rubros del patrimonio neto que comprende el Capital Ordinario de Nivel Uno (COn1) como conceptos computables de la responsabilidad patrimonial computable"
  ]
}
```

**Paso 2 del juez (verificaciones, verbatim):**
```json
{
  "verificaciones": [
    {
      "enunciado": "El Capital Ordinario de Nivel Uno (COn1) comprende como rubro el capital social, excluyendo acciones con preferencia patrimonial.",
      "central": true,
      "verdict": "verdadero"
    },
    {
      "enunciado": "El Capital Ordinario de Nivel Uno (COn1) comprende como rubro los aportes no capitalizados, excluyendo primas de emisión.",
      "central": true,
      "verdict": "verdadero"
    },
    {
      "enunciado": "El Capital Ordinario de Nivel Uno (COn1) comprende como rubro los ajustes al patrimonio y reservas de utilidades, excluyendo la reserva especial para instrumentos de deuda.",
      "central": true,
      "verdict": "verdadero"
    },
    {
      "enunciado": "El Capital Ordinario de Nivel Uno (COn1) comprende como rubro otros resultados integrales al 100%.",
      "central": true,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "Dentro de otros resultados integrales se incluyen los resultados registrados en revaluación de propiedad, planta, equipo e intangibles.",
      "central": true,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "Dentro de otros resultados integrales se incluyen las ganancias o pérdidas por instrumentos financieros a valor razonable con cambios en otros resultados integrales.",
      "central": true,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "Dentro de otros resultados integrales se incluye el saldo deudor de partidas de otros resultados integrales no mencionadas.",
      "central": true,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "El Capital Ordinario de Nivel Uno (COn1) comprende como rubro los resultados del último ejercicio cerrado, una vez que se cuente con dictamen del auditor.",
      "central": true,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "El Capital Ordinario de Nivel Uno (COn1) comprende como rubro los resultados de balances trimestrales.",
      "central": true,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "El Capital Ordinario de Nivel Uno (COn1) comprende como rubro los resultados del ejercicio en curso.",
      "central": true,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "El Capital Ordinario de Nivel Uno (COn1) comprende como rubro los resultados mensuales posteriores a últimos balances auditados.",
      "central": true,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "El Capital Ordinario de Nivel Uno (COn1) comprende como rubro los quebrantos contabilizados y no contabilizados.",
      "central": true,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "La regulación del COn1 es emitida por el BCRA.",
      "central": false,
      "verdict": "no_soportado"
    }
  ],
  "cobertura_patas": [
    {
      "pata": "Totalidad de los rubros del patrimonio neto que comprende el Capital Ordinario de Nivel Uno (COn1) como conceptos computables de la responsabilidad patrimonial computable",
      "cobertura": "cubierta"
    }
  ],
  "cita_documento_correcto": true,
  "cita_precision": "punto",
  "abstencion": null,
  "especulacion_en_prosa": null,
  "justificacion": {
    "citas": "El agente cita 'TO_capitales_minimos_actual.pdf, Punto 8.2. Conceptos computables', que corresponde al documento del ground truth (Punto 8.2.1.), con precisión a nivel punto/sección.",
    "abstencion": ""
  }
}
```

### EV1-034 · réplica 2 — FLAGGEADA

- Veredicto del juez: correctitud=`correcta`, completitud=`completa`, cita_documento_correcto=`True`, cita_precision=`punto` | hit_tool_limit=True | pasos=15

- **Motivo mecánico del flag** — afirmaciones CENTRALES `no_soportado` (3):

  - El Capital Ordinario de Nivel Uno (COn1) incluye resultados registrados en revaluación de propiedad, planta, equipo e intangibles al 100%.
  - El Capital Ordinario de Nivel Uno (COn1) incluye ganancias o pérdidas por instrumentos financieros a valor razonable con cambios en otros resultados integrales al 100%.
  - El Capital Ordinario de Nivel Uno (COn1) incluye el saldo deudor de partidas de otros resultados integrales no mencionadas al 100%.

**Respuesta completa del agente (verbatim):**

> El Capital Ordinario de Nivel Uno (COn1) como concepto computable de la responsabilidad patrimonial computable comprende los siguientes rubros del patrimonio neto:
> 
> 1. Capital social (excluyendo acciones con preferencia patrimonial)
> 2. Aportes no capitalizados (excluyendo primas de emisión)
> 3. Primas de emisión resultantes de instrumentos incluidos en CO_n1
> 4. Ajustes al patrimonio
> 5. Reservas de utilidades (excluyendo la reserva especial para instrumentos de deuda)
> 6. Resultados registrados en revaluación de propiedad, planta, equipo e intangibles (al 100%)
> 7. Ganancias o pérdidas por instrumentos financieros a valor razonable con cambios en otros resultados integrales (al 100%)
> 8. Saldo deudor de partidas de otros resultados integrales no mencionadas (al 100%)
> 9. Otros resultados (positivos y negativos) computados según porcentajes graduales: 100% de resultados hasta último estado trimestral con informe auditor del ejercicio cerrado; 100% del ejercicio en curso desde último estado trimestral con informe; 50% de ganancias o 100% de pérdidas desde último estado trimestral/anual con informe; 100% de quebrantos no registrados según informes de auditoría
> 10. Participaciones minoritarias en casos de consolidación (acciones ordinarias emitidas por subsidiarias sujetas a supervisión consolidada)

**Citas del agente:**
```json
[
  {
    "source_doc": "TO_capitales_minimos_actual.pdf",
    "location": "Punto 8.2. Conceptos computables."
  }
]
```

**Justificación del juez (verbatim):**
```json
{
  "correctitud": "Centrales todas verdaderas o no_soportadas; ninguna afirmación falsa.",
  "completitud": "Todas las patas cubiertas.",
  "citas": "La cita apunta a 'TO_capitales_minimos_actual.pdf, Punto 8.2. Conceptos computables', que corresponde al documento del ground truth (Punto 8.2.1.), con precisión a nivel punto."
}
```

**Paso 1 del juez (descomposición, verbatim):**
```json
{
  "afirmaciones_verificables": [
    {
      "enunciado": "El Capital Ordinario de Nivel Uno (COn1) incluye el capital social, excluyendo acciones con preferencia patrimonial.",
      "central": true
    },
    {
      "enunciado": "El Capital Ordinario de Nivel Uno (COn1) incluye aportes no capitalizados, excluyendo primas de emisión.",
      "central": true
    },
    {
      "enunciado": "El Capital Ordinario de Nivel Uno (COn1) incluye primas de emisión resultantes de instrumentos incluidos en COn1.",
      "central": true
    },
    {
      "enunciado": "El Capital Ordinario de Nivel Uno (COn1) incluye ajustes al patrimonio.",
      "central": true
    },
    {
      "enunciado": "El Capital Ordinario de Nivel Uno (COn1) incluye reservas de utilidades, excluyendo la reserva especial para instrumentos de deuda.",
      "central": true
    },
    {
      "enunciado": "El Capital Ordinario de Nivel Uno (COn1) incluye resultados registrados en revaluación de propiedad, planta, equipo e intangibles al 100%.",
      "central": true
    },
    {
      "enunciado": "El Capital Ordinario de Nivel Uno (COn1) incluye ganancias o pérdidas por instrumentos financieros a valor razonable con cambios en otros resultados integrales al 100%.",
      "central": true
    },
    {
      "enunciado": "El Capital Ordinario de Nivel Uno (COn1) incluye el saldo deudor de partidas de otros resultados integrales no mencionadas al 100%.",
      "central": true
    },
    {
      "enunciado": "El Capital Ordinario de Nivel Uno (COn1) incluye otros resultados (positivos y negativos) computados según porcentajes graduales.",
      "central": true
    },
    {
      "enunciado": "Se computa el 100% de resultados hasta el último estado trimestral con informe auditor del ejercicio cerrado.",
      "central": false
    },
    {
      "enunciado": "Se computa el 100% del ejercicio en curso desde el último estado trimestral con informe de auditor.",
      "central": false
    },
    {
      "enunciado": "Se computa el 50% de ganancias o el 100% de pérdidas desde el último estado trimestral/anual con informe de auditor.",
      "central": false
    },
    {
      "enunciado": "Se computa el 100% de quebrantos no registrados según informes de auditoría.",
      "central": false
    },
    {
      "enunciado": "El Capital Ordinario de Nivel Uno (COn1) incluye participaciones minoritarias en casos de consolidación, correspondientes a acciones ordinarias emitidas por subsidiarias sujetas a supervisión consolidada.",
      "central": true
    }
  ],
  "reportes_de_alcance": [],
  "patas_de_la_pregunta": [
    "Totalidad de los rubros del patrimonio neto que comprende el Capital Ordinario de Nivel Uno (COn1) como conceptos computables de la responsabilidad patrimonial computable"
  ]
}
```

**Paso 2 del juez (verificaciones, verbatim):**
```json
{
  "verificaciones": [
    {
      "enunciado": "El Capital Ordinario de Nivel Uno (COn1) incluye el capital social, excluyendo acciones con preferencia patrimonial.",
      "central": true,
      "verdict": "verdadero"
    },
    {
      "enunciado": "El Capital Ordinario de Nivel Uno (COn1) incluye aportes no capitalizados, excluyendo primas de emisión.",
      "central": true,
      "verdict": "verdadero"
    },
    {
      "enunciado": "El Capital Ordinario de Nivel Uno (COn1) incluye primas de emisión resultantes de instrumentos incluidos en COn1.",
      "central": true,
      "verdict": "verdadero"
    },
    {
      "enunciado": "El Capital Ordinario de Nivel Uno (COn1) incluye ajustes al patrimonio.",
      "central": true,
      "verdict": "verdadero"
    },
    {
      "enunciado": "El Capital Ordinario de Nivel Uno (COn1) incluye reservas de utilidades, excluyendo la reserva especial para instrumentos de deuda.",
      "central": true,
      "verdict": "verdadero"
    },
    {
      "enunciado": "El Capital Ordinario de Nivel Uno (COn1) incluye resultados registrados en revaluación de propiedad, planta, equipo e intangibles al 100%.",
      "central": true,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "El Capital Ordinario de Nivel Uno (COn1) incluye ganancias o pérdidas por instrumentos financieros a valor razonable con cambios en otros resultados integrales al 100%.",
      "central": true,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "El Capital Ordinario de Nivel Uno (COn1) incluye el saldo deudor de partidas de otros resultados integrales no mencionadas al 100%.",
      "central": true,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "El Capital Ordinario de Nivel Uno (COn1) incluye otros resultados (positivos y negativos) computados según porcentajes graduales.",
      "central": true,
      "verdict": "verdadero"
    },
    {
      "enunciado": "Se computa el 100% de resultados hasta el último estado trimestral con informe auditor del ejercicio cerrado.",
      "central": false,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "Se computa el 100% del ejercicio en curso desde el último estado trimestral con informe de auditor.",
      "central": false,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "Se computa el 50% de ganancias o el 100% de pérdidas desde el último estado trimestral/anual con informe de auditor.",
      "central": false,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "Se computa el 100% de quebrantos no registrados según informes de auditoría.",
      "central": false,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "El Capital Ordinario de Nivel Uno (COn1) incluye participaciones minoritarias en casos de consolidación, correspondientes a acciones ordinarias emitidas por subsidiarias sujetas a supervisión consolidada.",
      "central": true,
      "verdict": "verdadero"
    }
  ],
  "cobertura_patas": [
    {
      "pata": "Totalidad de los rubros del patrimonio neto que comprende el Capital Ordinario de Nivel Uno (COn1) como conceptos computables de la responsabilidad patrimonial computable",
      "cobertura": "cubierta"
    }
  ],
  "cita_documento_correcto": true,
  "cita_precision": "punto",
  "abstencion": null,
  "especulacion_en_prosa": null,
  "justificacion": {
    "citas": "La cita apunta a 'TO_capitales_minimos_actual.pdf, Punto 8.2. Conceptos computables', que corresponde al documento del ground truth (Punto 8.2.1.), con precisión a nivel punto.",
    "abstencion": ""
  }
}
```

### EV1-034 · réplica 3 — FLAGGEADA

- Veredicto del juez: correctitud=`correcta`, completitud=`completa`, cita_documento_correcto=`True`, cita_precision=`punto` | hit_tool_limit=False | pasos=13

- **Motivo mecánico del flag** — afirmaciones CENTRALES `no_soportado` (1):

  - El saldo deudor de partidas de otros resultados integrales no mencionadas (al 100%) es un rubro del patrimonio neto computable en el COn1.

**Respuesta completa del agente (verbatim):**

> Los rubros del patrimonio neto que comprende el capital ordinario de nivel uno (COn1) como conceptos computables de la responsabilidad patrimonial computable son los siguientes:
> 
> 1. Capital social (excluyendo acciones con preferencia patrimonial)
> 2. Aportes no capitalizados (excluyendo primas de emisión)
> 3. Ajustes al patrimonio
> 4. Reservas de utilidades (excluyendo la reserva especial para instrumentos de deuda)
> 5. Resultado positivo del último ejercicio cerrado (una vez disponible el dictamen del auditor)
> 6. Otros resultados positivos y negativos (según porcentajes graduales: 100% de resultados hasta último estado trimestral con informe auditor del ejercicio cerrado; 100% del ejercicio en curso desde último estado trimestral con informe; 50% de ganancias o 100% de pérdidas desde último estado trimestral/anual con informe; 100% de quebrantos no registrados según informes de auditoría)
> 7. Resultados registrados en revaluación de propiedad, planta, equipo e intangibles (al 100%)
> 8. Ganancias o pérdidas por instrumentos financieros a valor razonable con cambios en otros resultados integrales (al 100%)
> 9. Saldo deudor de partidas de otros resultados integrales no mencionadas (al 100%)
> 10. Primas de emisión resultantes de instrumentos incluidos en CO_n1
> 11. Participaciones minoritarias (en casos de consolidación: acciones ordinarias emitidas por subsidiarias sujetas a supervisión consolidada y en poder de terceros que cumplan criterios regulatorios)
> 
> De estos conceptos se deben restar los conceptos deducibles previstos en la normativa.

**Citas del agente:**
```json
[
  {
    "source_doc": "TO_capitales_minimos_actual.pdf",
    "location": "Punto 8.2. Conceptos computables."
  }
]
```

**Justificación del juez (verbatim):**
```json
{
  "correctitud": "Centrales todas verdaderas o no_soportadas; ninguna afirmación falsa.",
  "completitud": "Todas las patas cubiertas.",
  "citas": "La cita apunta a 'TO_capitales_minimos_actual.pdf, Punto 8.2. Conceptos computables', que corresponde al documento del ground truth (Punto 8.2.1.), con precisión a nivel punto/sección."
}
```

**Paso 1 del juez (descomposición, verbatim):**
```json
{
  "afirmaciones_verificables": [
    {
      "enunciado": "El capital social (excluyendo acciones con preferencia patrimonial) es un rubro del patrimonio neto computable en el COn1.",
      "central": true
    },
    {
      "enunciado": "Los aportes no capitalizados (excluyendo primas de emisión) son un rubro del patrimonio neto computable en el COn1.",
      "central": true
    },
    {
      "enunciado": "Los ajustes al patrimonio son un rubro del patrimonio neto computable en el COn1.",
      "central": true
    },
    {
      "enunciado": "Las reservas de utilidades (excluyendo la reserva especial para instrumentos de deuda) son un rubro del patrimonio neto computable en el COn1.",
      "central": true
    },
    {
      "enunciado": "El resultado positivo del último ejercicio cerrado (una vez disponible el dictamen del auditor) es un rubro del patrimonio neto computable en el COn1.",
      "central": true
    },
    {
      "enunciado": "Los otros resultados positivos y negativos son un rubro del patrimonio neto computable en el COn1.",
      "central": true
    },
    {
      "enunciado": "Los otros resultados integrales se computan al 100% cuando corresponden a resultados hasta el último estado trimestral con informe auditor del ejercicio cerrado.",
      "central": false
    },
    {
      "enunciado": "Los otros resultados integrales se computan al 100% del ejercicio en curso desde el último estado trimestral con informe.",
      "central": false
    },
    {
      "enunciado": "Las ganancias de otros resultados integrales se computan al 50% y las pérdidas al 100% desde el último estado trimestral/anual con informe.",
      "central": false
    },
    {
      "enunciado": "Los quebrantos no registrados según informes de auditoría se computan al 100%.",
      "central": false
    },
    {
      "enunciado": "Los resultados registrados en revaluación de propiedad, planta, equipo e intangibles (al 100%) son un rubro del patrimonio neto computable en el COn1.",
      "central": true
    },
    {
      "enunciado": "Las ganancias o pérdidas por instrumentos financieros a valor razonable con cambios en otros resultados integrales (al 100%) son un rubro del patrimonio neto computable en el COn1.",
      "central": true
    },
    {
      "enunciado": "El saldo deudor de partidas de otros resultados integrales no mencionadas (al 100%) es un rubro del patrimonio neto computable en el COn1.",
      "central": true
    },
    {
      "enunciado": "Las primas de emisión resultantes de instrumentos incluidos en COn1 son un rubro del patrimonio neto computable en el COn1.",
      "central": true
    },
    {
      "enunciado": "Las participaciones minoritarias (acciones ordinarias emitidas por subsidiarias sujetas a supervisión consolidada y en poder de terceros que cumplan criterios regulatorios) son un rubro del patrimonio neto computable en el COn1 en casos de consolidación.",
      "central": true
    },
    {
      "enunciado": "De los conceptos del COn1 se deben restar los conceptos deducibles previstos en la normativa.",
      "central": false
    }
  ],
  "reportes_de_alcance": [],
  "patas_de_la_pregunta": [
    "Totalidad de los rubros del patrimonio neto que comprende el capital ordinario de nivel uno (COn1) como conceptos computables de la responsabilidad patrimonial computable"
  ]
}
```

**Paso 2 del juez (verificaciones, verbatim):**
```json
{
  "verificaciones": [
    {
      "enunciado": "El capital social (excluyendo acciones con preferencia patrimonial) es un rubro del patrimonio neto computable en el COn1.",
      "central": true,
      "verdict": "verdadero"
    },
    {
      "enunciado": "Los aportes no capitalizados (excluyendo primas de emisión) son un rubro del patrimonio neto computable en el COn1.",
      "central": true,
      "verdict": "verdadero"
    },
    {
      "enunciado": "Los ajustes al patrimonio son un rubro del patrimonio neto computable en el COn1.",
      "central": true,
      "verdict": "verdadero"
    },
    {
      "enunciado": "Las reservas de utilidades (excluyendo la reserva especial para instrumentos de deuda) son un rubro del patrimonio neto computable en el COn1.",
      "central": true,
      "verdict": "verdadero"
    },
    {
      "enunciado": "El resultado positivo del último ejercicio cerrado (una vez disponible el dictamen del auditor) es un rubro del patrimonio neto computable en el COn1.",
      "central": true,
      "verdict": "verdadero"
    },
    {
      "enunciado": "Los otros resultados positivos y negativos son un rubro del patrimonio neto computable en el COn1.",
      "central": true,
      "verdict": "verdadero"
    },
    {
      "enunciado": "Los otros resultados integrales se computan al 100% cuando corresponden a resultados hasta el último estado trimestral con informe auditor del ejercicio cerrado.",
      "central": false,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "Los otros resultados integrales se computan al 100% del ejercicio en curso desde el último estado trimestral con informe.",
      "central": false,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "Las ganancias de otros resultados integrales se computan al 50% y las pérdidas al 100% desde el último estado trimestral/anual con informe.",
      "central": false,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "Los quebrantos no registrados según informes de auditoría se computan al 100%.",
      "central": false,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "Los resultados registrados en revaluación de propiedad, planta, equipo e intangibles (al 100%) son un rubro del patrimonio neto computable en el COn1.",
      "central": true,
      "verdict": "verdadero"
    },
    {
      "enunciado": "Las ganancias o pérdidas por instrumentos financieros a valor razonable con cambios en otros resultados integrales (al 100%) son un rubro del patrimonio neto computable en el COn1.",
      "central": true,
      "verdict": "verdadero"
    },
    {
      "enunciado": "El saldo deudor de partidas de otros resultados integrales no mencionadas (al 100%) es un rubro del patrimonio neto computable en el COn1.",
      "central": true,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "Las primas de emisión resultantes de instrumentos incluidos en COn1 son un rubro del patrimonio neto computable en el COn1.",
      "central": true,
      "verdict": "verdadero"
    },
    {
      "enunciado": "Las participaciones minoritarias (acciones ordinarias emitidas por subsidiarias sujetas a supervisión consolidada y en poder de terceros que cumplan criterios regulatorios) son un rubro del patrimonio neto computable en el COn1 en casos de consolidación.",
      "central": true,
      "verdict": "verdadero"
    },
    {
      "enunciado": "De los conceptos del COn1 se deben restar los conceptos deducibles previstos en la normativa.",
      "central": false,
      "verdict": "no_soportado"
    }
  ],
  "cobertura_patas": [
    {
      "pata": "Totalidad de los rubros del patrimonio neto que comprende el capital ordinario de nivel uno (COn1) como conceptos computables de la responsabilidad patrimonial computable",
      "cobertura": "cubierta"
    }
  ],
  "cita_documento_correcto": true,
  "cita_precision": "punto",
  "abstencion": null,
  "especulacion_en_prosa": null,
  "justificacion": {
    "citas": "La cita apunta a 'TO_capitales_minimos_actual.pdf, Punto 8.2. Conceptos computables', que corresponde al documento del ground truth (Punto 8.2.1.), con precisión a nivel punto/sección.",
    "abstencion": ""
  }
}
```

**Contexto de las 3 réplicas de EV1-034 en v3 (sin comentario):** r1: correctitud=`correcta` (flaggeada) · r2: correctitud=`correcta` (flaggeada) · r3: correctitud=`correcta` (flaggeada)


---

## EV1-036 — sujeto · ['TO_capitales_minimos_actual.pdf']

**Pregunta (verbatim):** ¿Están las entidades financieras del grupo 2 alcanzadas por la obligación de clasificar sus exposiciones con garantía hipotecaria en normativas y no normativas? ¿Qué tratamiento les corresponde?

**Respuesta esperada (key adjudicada, verbatim):** No; la obligación de clasificar las exposiciones con garantía hipotecaria en normativas y no normativas alcanza a las entidades financieras del grupo 1. Las exposiciones con garantía hipotecaria de las entidades del grupo 2 reciben directamente el tratamiento previsto para las exposiciones normativas, aplicando los ponderadores de riesgo correspondientes, siempre que la garantía hipotecaria sea en primer grado o, cualquiera sea su grado de prelación, la entidad sea la acreedora en todos los grados.

**Estado mecánico de la mayoría en v3:** veredictos ['correcta', 'correcta', 'correcta'] → n_correcta=3, correcto_mayoria=True, patrón 3-0


### EV1-036 · réplica 3 — FLAGGEADA

- Veredicto del juez: correctitud=`correcta`, completitud=`parcial`, cita_documento_correcto=`True`, cita_precision=`punto` | hit_tool_limit=False | pasos=14

- **Motivo mecánico del flag** — afirmaciones CENTRALES `no_soportado` (1):

  - La obligación de clasificación para el grupo 2 se refiere exclusivamente a exposiciones a instrumentos (deuda subordinada emitida por empresas y/o entidades financieras, y participaciones en el capital emitido por empresas y/o entidades financieras).

**Respuesta completa del agente (verbatim):**

> No. Según la información disponible en el Knowledge Graph, las entidades financieras del grupo 2 NO están alcanzadas por una obligación específica de clasificar sus exposiciones con garantía hipotecaria en normativas y no normativas. La obligación de clasificación que existe para el grupo 2 se refiere exclusivamente a exposiciones a instrumentos (deuda subordinada emitida por empresas y/o entidades financieras, y participaciones en el capital emitido por empresas y/o entidades financieras). Por el contrario, las exposiciones con garantía hipotecaria sobre vivienda residencial están excluidas de las exposiciones minoristas, y las restricciones específicas sobre ponderadores para exposiciones minoristas con garantía hipotecaria se aplican únicamente a las entidades financieras del grupo 1.

**Citas del agente:**
```json
[
  {
    "source_doc": "TO_capitales_minimos_actual.pdf",
    "location": "Punto 2.11. Exposiciones a instrumentos."
  },
  {
    "source_doc": "TO_capitales_minimos_actual.pdf",
    "location": "Punto 2.8. Exposiciones minoristas."
  }
]
```

**Justificación del juez (verbatim):**
```json
{
  "correctitud": "Centrales todas verdaderas o no_soportadas; ninguna afirmación falsa.",
  "completitud": "Patas no cubiertas: Qué tratamiento les corresponde a las entidades financieras del grupo 2 respecto de esas exposiciones",
  "citas": "El agente cita TO_capitales_minimos_actual.pdf en puntos específicos (2.11 y 2.8), que corresponden al documento del ground truth, aunque no coinciden exactamente con los puntos 2.9.1 y 2.9.2.1 del referente."
}
```

**Paso 1 del juez (descomposición, verbatim):**
```json
{
  "afirmaciones_verificables": [
    {
      "enunciado": "Las entidades financieras del grupo 2 NO están alcanzadas por una obligación específica de clasificar sus exposiciones con garantía hipotecaria en normativas y no normativas.",
      "central": true
    },
    {
      "enunciado": "La obligación de clasificación para el grupo 2 se refiere exclusivamente a exposiciones a instrumentos (deuda subordinada emitida por empresas y/o entidades financieras, y participaciones en el capital emitido por empresas y/o entidades financieras).",
      "central": true
    },
    {
      "enunciado": "Las exposiciones con garantía hipotecaria sobre vivienda residencial están excluidas de las exposiciones minoristas.",
      "central": false
    },
    {
      "enunciado": "Las restricciones específicas sobre ponderadores para exposiciones minoristas con garantía hipotecaria se aplican únicamente a las entidades financieras del grupo 1.",
      "central": true
    }
  ],
  "reportes_de_alcance": [
    "Según la información disponible en el Knowledge Graph, las entidades financieras del grupo 2 no tienen una obligación específica de clasificar sus exposiciones con garantía hipotecaria en normativas y no normativas."
  ],
  "patas_de_la_pregunta": [
    "Si las entidades financieras del grupo 2 están alcanzadas por la obligación de clasificar sus exposiciones con garantía hipotecaria en normativas y no normativas",
    "Qué tratamiento les corresponde a las entidades financieras del grupo 2 respecto de esas exposiciones"
  ]
}
```

**Paso 2 del juez (verificaciones, verbatim):**
```json
{
  "verificaciones": [
    {
      "enunciado": "Las entidades financieras del grupo 2 NO están alcanzadas por una obligación específica de clasificar sus exposiciones con garantía hipotecaria en normativas y no normativas.",
      "central": true,
      "verdict": "verdadero"
    },
    {
      "enunciado": "La obligación de clasificación para el grupo 2 se refiere exclusivamente a exposiciones a instrumentos (deuda subordinada emitida por empresas y/o entidades financieras, y participaciones en el capital emitido por empresas y/o entidades financieras).",
      "central": true,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "Las exposiciones con garantía hipotecaria sobre vivienda residencial están excluidas de las exposiciones minoristas.",
      "central": false,
      "verdict": "no_soportado"
    },
    {
      "enunciado": "Las restricciones específicas sobre ponderadores para exposiciones minoristas con garantía hipotecaria se aplican únicamente a las entidades financieras del grupo 1.",
      "central": true,
      "verdict": "verdadero"
    }
  ],
  "cobertura_patas": [
    {
      "pata": "Si las entidades financieras del grupo 2 están alcanzadas por la obligación de clasificar sus exposiciones con garantía hipotecaria en normativas y no normativas",
      "cobertura": "cubierta"
    },
    {
      "pata": "Qué tratamiento les corresponde a las entidades financieras del grupo 2 respecto de esas exposiciones",
      "cobertura": "no_cubierta"
    }
  ],
  "cita_documento_correcto": true,
  "cita_precision": "punto",
  "abstencion": null,
  "especulacion_en_prosa": null,
  "justificacion": {
    "citas": "El agente cita TO_capitales_minimos_actual.pdf en puntos específicos (2.11 y 2.8), que corresponden al documento del ground truth, aunque no coinciden exactamente con los puntos 2.9.1 y 2.9.2.1 del referente.",
    "abstencion": ""
  }
}
```

**Contexto de las 3 réplicas de EV1-036 en v3 (sin comentario):** r1: correctitud=`correcta` · r2: correctitud=`correcta` · r3: correctitud=`correcta` (flaggeada)


---

## Acarreo de adjudicaciones selladas (v2 / run_3)

Las 30 réplicas flaggeadas de los brazos grafo_v2 y run_3 del 1b son las mismas
del escalón 1 (replay byte-idéntico). Sus laudos NO se re-abren: se acarrean del
archivo sellado `adjudicacion_humana_2026-07-26.json` (y su nota `sin_cambios`).
Tabla id → laudo:

| Réplica flaggeada | Veredicto del juez | Laudo humano sellado | Causa registrada |
|---|---|---|---|
| grafo_v2/EV1-007·r1 | correcta | correcta | correcta ratificada |
| grafo_v2/EV1-007·r2 | correcta | correcta | correcta ratificada |
| grafo_v2/EV1-007·r3 | correcta | correcta | correcta ratificada |
| grafo_v2/EV1-011·r1 | — | (subsumida en fichas) | nota sin_cambios del archivo |
| grafo_v2/EV1-011·r3 | — | (subsumida en fichas) | nota sin_cambios del archivo |
| grafo_v2/EV1-015·r1 | correcta | incorrecta | niegan/eluden el dato que la key afirma; el 1.1 no alcanzado, capturado el vecino 7.1 |
| grafo_v2/EV1-015·r2 | correcta | incorrecta | niegan/eluden el dato que la key afirma; el 1.1 no alcanzado, capturado el vecino 7.1 |
| grafo_v2/EV1-015·r3 | correcta | incorrecta | niegan/eluden el dato que la key afirma; el 1.1 no alcanzado, capturado el vecino 7.1 |
| grafo_v2/EV1-018·r1 | correcta | incorrecta | no-respuesta: repiten la premisa sin listar operación alguna del 4.1.4; completitud compartida |
| grafo_v2/EV1-018·r2 | correcta | incorrecta | no-respuesta: repiten la premisa sin listar operación alguna del 4.1.4; completitud compartida |
| grafo_v2/EV1-018·r3 | correcta | incorrecta | no-respuesta: repiten la premisa sin listar operación alguna del 4.1.4; completitud compartida |
| grafo_v2/EV1-027·r1 | correcta | correcta | correcta ratificada |
| grafo_v2/EV1-029·r2 | — | (subsumida en fichas) | nota sin_cambios del archivo |
| grafo_v2/EV1-029·r3 | — | (subsumida en fichas) | nota sin_cambios del archivo |
| grafo_v2/EV1-031·r1 | correcta | incorrecta | evasivas: dato real ajeno + "el KG no contiene" |
| grafo_v2/EV1-031·r2 | correcta | incorrecta | evasivas: dato real ajeno + "el KG no contiene" |
| grafo_v2/EV1-034·r2 | correcta | correcta | correcta ratificada; nota: omisión menor especular — minoritarias/no-asignados |
| grafo_v2/EV1-034·r3 | correcta | correcta | correcta ratificada; nota: omisión menor especular — minoritarias/no-asignados |
| run_3/EV1-007·r3 | correcta | incorrecta | evasiva aprobada |
| run_3/EV1-011·r1 | — | (subsumida en fichas) | nota sin_cambios del archivo |
| run_3/EV1-011·r2 | — | (subsumida en fichas) | nota sin_cambios del archivo |
| run_3/EV1-011·r3 | — | (subsumida en fichas) | nota sin_cambios del archivo |
| run_3/EV1-015·r1 | correcta | correcta | correcta ratificada |
| run_3/EV1-015·r2 | correcta | correcta | correcta ratificada |
| run_3/EV1-015·r3 | correcta | correcta | correcta ratificada |
| run_3/EV1-018·r2 | correcta | incorrecta | no-respuesta: repiten la premisa sin listar operación alguna del 4.1.4; completitud compartida |
| run_3/EV1-018·r3 | correcta | incorrecta | no-respuesta: repiten la premisa sin listar operación alguna del 4.1.4; completitud compartida |
| run_3/EV1-034·r1 | correcta | correcta | correcta ratificada; nota: omisión menor especular — minoritarias/no-asignados |
| run_3/EV1-035·r1 | correcta | incorrecta | excepción enunciada sin sus condiciones esenciales — sobre-ampliación |
| run_3/EV1-035·r2 | correcta | incorrecta | excepción enunciada sin sus condiciones esenciales — sobre-ampliación |

---

## Contexto de mayoría (aritmética pura, sin recomendación)

Regla: correcto por mayoría si n_correcta ≥ 2 de 3. Para cada pregunta, el
estado mecánico actual en v3 y el efecto aritmético de laudar cada réplica
flaggeada en el sentido contrario al veredicto del juez (un laudo que ratifica
al juez no mueve nada).


**EV1-004** — veredictos actuales ['correcta', 'correcta', 'correcta'], n_correcta=3, mayoría=correcta.
  - si r1 se lauda incorrecta, n_correcta pasa a 2 → mayoría correcta
  - si r2 se lauda incorrecta, n_correcta pasa a 2 → mayoría correcta
  - si r3 se lauda incorrecta, n_correcta pasa a 2 → mayoría correcta

**EV1-007** — veredictos actuales ['correcta', 'correcta', 'correcta'], n_correcta=3, mayoría=correcta.
  - si r1 se lauda incorrecta, n_correcta pasa a 2 → mayoría correcta

**EV1-011** — veredictos actuales ['incorrecta', 'incorrecta', 'incorrecta'], n_correcta=0, mayoría=no-correcta.
  - si r1 se lauda correcta, n_correcta pasa a 1 → mayoría no-correcta
  - si r2 se lauda correcta, n_correcta pasa a 1 → mayoría no-correcta
  - si r3 se lauda correcta, n_correcta pasa a 1 → mayoría no-correcta

**EV1-015** — veredictos actuales ['correcta', 'correcta', 'correcta'], n_correcta=3, mayoría=correcta.
  - si r1 se lauda incorrecta, n_correcta pasa a 2 → mayoría correcta
  - si r2 se lauda incorrecta, n_correcta pasa a 2 → mayoría correcta
  - si r3 se lauda incorrecta, n_correcta pasa a 2 → mayoría correcta

**EV1-018** — veredictos actuales ['correcta', 'correcta', 'correcta'], n_correcta=3, mayoría=correcta.
  - si r1 se lauda incorrecta, n_correcta pasa a 2 → mayoría correcta
  - si r2 se lauda incorrecta, n_correcta pasa a 2 → mayoría correcta
  - si r3 se lauda incorrecta, n_correcta pasa a 2 → mayoría correcta

**EV1-028** — veredictos actuales ['incorrecta', 'incorrecta', 'incorrecta'], n_correcta=0, mayoría=no-correcta.
  - si r2 se lauda correcta, n_correcta pasa a 1 → mayoría no-correcta

**EV1-034** — veredictos actuales ['correcta', 'correcta', 'correcta'], n_correcta=3, mayoría=correcta.
  - si r1 se lauda incorrecta, n_correcta pasa a 2 → mayoría correcta
  - si r2 se lauda incorrecta, n_correcta pasa a 2 → mayoría correcta
  - si r3 se lauda incorrecta, n_correcta pasa a 2 → mayoría correcta

**EV1-036** — veredictos actuales ['correcta', 'correcta', 'correcta'], n_correcta=3, mayoría=correcta.
  - si r3 se lauda incorrecta, n_correcta pasa a 2 → mayoría correcta


— Fin del expediente. Los laudos son de la adjudicación humana. —
