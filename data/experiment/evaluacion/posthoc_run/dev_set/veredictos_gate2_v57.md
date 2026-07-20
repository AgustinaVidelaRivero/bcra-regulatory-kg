# Veredictos del gate #2 (v5.7, n=3+voto) — extracción para la lectura B

Fecha: 2026-07-15. Solo lectura; única escritura: este archivo. **Este reporte NO compara
contra la vara**: la comparación es adjudicación y ocurre fuera de esta sesión. Solo
extracción verbatim + inventario.

---

## PASO 0 — Guarda del sellado (constancia)

`git log --oneline -3`:

```
f0d651a vara v3: GTs re-expresados en taxonomía v2.6.1 con evidencia re-fundada en re-ejecuciones determinísticas y barridos trackeados (docs/evidencia_vara_v3/). CQ-034 re-scopeado (pata efectivo sana, regla endurecida); secundaria de CQ-020 disuelta -> FP del juez (corrección de barrido documentada); exclusiones v2.2/v2.6 explícitas; cobertura de lados: cero causas lado-agente, disclosure. Historia completa en nota_readjudicacion_vara_v3.md. Sellado de gate2_v57 intacto
c0b96a4 protocolo pre-registrado del gate #2: segunda y ÚLTIMA calibración (v5.7 congelado, N=3+voto, scoring acierto/miss/triage sobre reps válidas), disclosure completo inter-gates (asterisco CQ-025→v2.5; cero corridas contra run_3 verificado por SQL de caché), vara intacta desde 5bb58c0, ambos gates se reportan juntos siempre
32f819e especificación final del verificador v5.7: historia v1→v5.7 con fuentes, dev 5/8 (nuevos 3/3), gate #1 2/5+formato, varianza N=3 tipificada (3 perfiles), régimen --n3+voto+triage, presupuesto medido desde caché (12,7M in v5.x); taxonomia v2.6.1 corrección documental + fragilidad del ensamblador documentada
```

`git status`:

```
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

**Guarda: PASA.** HEAD = `f0d651a`, el commit de la vara v3 (verificado con
`git show --stat f0d651a`: contiene `casos_control.md` re-expresado,
`nota_readjudicacion_vara_v3.md` y los 4 archivos de `docs/evidencia_vara_v3/`). Working
tree limpio. El sellado de `gate2_v57/` se levanta recién a partir de este punto.

---

## 1. LECTURA A, VERBATIM

Fuente: `data/experiment/evaluacion/posthoc_run/dev_set/gate2_v57/resumen.md` (contenido
completo, 2.239 bytes):

````markdown
# Resumen GATE #2 — v5.7 congelado · n=3 + voto (2026-07-15, corrida única pre-registrada)

Protocolo: `docs/protocolo_gate2.md` (commit c0b96a4). 5 casos run_3 × 3 repeticiones (namespaces `verificador-v5.7-rep{1,2,3}`, gfp de run_3). JSON agregado íntegro por caso (las 3 reps + _meta adentro) en esta carpeta. SIN comparación contra vara (lectura externa). El campo `voto` es el programático (informativo); el scoring del protocolo sobre reps válidas lo aplica la revisión.

- **off/run_3/CQ-025** — voto programático: **mayoria** (dividido=False, ganadores={noise_sensitivity, aplicacion_erronea}, conteo=[2, 1]) · desglose: rep1: {context_recall, navegación} ; rep2: {noise_sensitivity, aplicacion_erronea} ; rep3: {noise_sensitivity, aplicacion_erronea} · tokens totales in=912338 out=26560
- **off/run_3/CQ-020** — voto programático: **frontera_no_determinada** (dividido=True, ganadores=—, conteo=[1, 1, 1]) · desglose: rep1: {noise_sensitivity, aplicacion_erronea} + {noise_sensitivity, contenido_kg} ; rep2: {noise_sensitivity, aplicacion_erronea} ; rep3: {noise_sensitivity, aplicacion_erronea} + {noise_sensitivity, provenance_imprecisa} · tokens totales in=1691239 out=36826
- **off/run_3/CQ-017** — voto programático: **mayoria** (dividido=False, ganadores=(clave ganadora VACÍA: sin primarias), conteo=[2, 1]) · desglose: rep1: (sin primarias) ; rep2: {context_recall, completitud_kg} + {noise_sensitivity, provenance_imprecisa} ; rep3: (sin primarias) · tokens totales in=1367127 out=30715
- **off/run_3/CQ-031** — voto programático: **mayoria** (dividido=False, ganadores={context_recall, navegación}, conteo=[3]) · desglose: rep1: {context_recall, navegación} ; rep2: {context_recall, navegación} ; rep3: {context_recall, navegación} · tokens totales in=962849 out=26074
- **off/run_3/CQ-034** — voto programático: **mayoria** (dividido=False, ganadores={context_recall, completitud_kg} + {context_recall, completitud_kg}, conteo=[2, 1]) · desglose: rep1: {context_recall, completitud_kg} + {context_recall, completitud_kg} ; rep2: {context_recall, completitud_kg} ; rep3: {context_recall, completitud_kg} + {context_recall, completitud_kg} · tokens totales in=869020 out=25269
````

---

## 2. REGLAS DE SCORING, VERBATIM

Fuente: `docs/protocolo_gate2.md`, **sección "## 4. Régimen de corrida y scoring"** (copiada
textual, desde el encabezado hasta el inicio de "## 5. Presupuesto estimado"):

````markdown
## 4. Régimen de corrida y scoring

- **Régimen:** `--n 3` con voto de mayoría (el régimen de operación real del instrumento, `docs/especificacion_verificador_v57.md` §4). Comando: `python verificador.py --n 3 --casos "off/run_3/CQ-017,off/run_3/CQ-020,off/run_3/CQ-025,off/run_3/CQ-031,off/run_3/CQ-034" --out <dir del gate #2>`.
- **Scoring de TRES categorías por caso:**
  - **ACIERTO** — el voto (mayoría estricta) coincide con el patrón de acierto del caso según la vara.
  - **MISS** — mayoría en un resultado incorrecto.
  - **TRIAGE** — voto dividido (`flag_voto_dividido=true`): se reporta como **derivación a revisión humana**, no como acierto ni como miss silencioso.
- **`formato_invalido` en una repetición cuenta como repetición SIN voto** (el voto se computa sobre las repeticiones con salida válida; si con ello no hay mayoría estricta sobre el total de K=3, el caso es TRIAGE).
- El voto del protocolo se computa sobre las repeticiones VÁLIDAS (sin `formato_invalido`): mayoría estricta requiere ≥2 reps válidas coincidentes; con <2 reps válidas o sin mayoría entre ellas → TRIAGE. El campo `voto` programático del JSON es informativo; en la lectura externa prevalece esta regla.
````

---

## 3. VEREDICTOS POR CASO

Fuente: los 5 JSONs de `data/experiment/evaluacion/posthoc_run/dev_set/gate2_v57/`
(`off_run_3_CQ-017.json`, `off_run_3_CQ-020.json`, `off_run_3_CQ-025.json`,
`off_run_3_CQ-031.json`, `off_run_3_CQ-034.json`). Por caso: (a) objeto `voto` completo
verbatim; (b) por repetición: `atribuciones` ÍNTEGRO + `formato_invalido` +
`errores_formato` + `detectores` verbatim; (c) `razonamiento` y `extraccion_traza` NO se
incluyen — se reportan solo sus longitudes en caracteres por rep.

### CQ-017 — `gate2_v57/off_run_3_CQ-017.json` (id_falla: run_3/CQ-017, n_reps: 3)

**(a) `voto` completo, verbatim:**

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
   "pares_primarios": [],
   "formato_invalido": false
  },
  {
   "rep": 2,
   "pares_primarios": [
    [
     "context_recall",
     "completitud_kg"
    ],
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

**(b) Rep 1:**

- `formato_invalido`: `false`
- `errores_formato`: `[]`

`atribuciones` (ÍNTEGRO, verbatim):

```json
[
 {
  "sintoma_capa1": "noise_sensitivity",
  "causa_capa2": "sin_defecto",
  "lado": "ninguno",
  "jerarquia": "sin_par",
  "pata": "Alcance por normas de Protección de Usuarios (claim de cita del Punto 1.1)",
  "evidencia": {
   "afirmacion": {
    "quote": "Los operadores de cambio figuran explícitamente como sujetos obligados en el Punto 1.1 (Partes) de la normativa de Protección de Usuarios.",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "\"id\": \"EntidadFinanciera_operador_de_cambio\" (...) \"provenances\": [{\"source_doc\": \"TO_proteccion_usuarios_servicios_financieros_actual.pdf\", \"location\": \"Punto 1.1. Partes.\"}]",
    "ubicacion": "EntidadFinanciera_operador_de_cambio (paso 4)"
   },
   "fuente": {
    "quote": "1.1.2. Sujetos obligados.\n1.1.2.1. Entidades financieras.\n1.1.2.2. Operadores de cambio, por las operaciones comprendidas en las normas sobre “Exterior y cambios”.",
    "ubicacion": "TO_proteccion_usuarios_servicios_financieros_actual.pdf, Punto 1.1.2.2"
   }
  }
 },
 {
  "sintoma_capa1": "noise_sensitivity",
  "causa_capa2": "sin_defecto",
  "lado": "ninguno",
  "jerarquia": "sin_par",
  "pata": "Alcance por normas de Protección de Usuarios (obligaciones sustantivas)",
  "evidencia": {
   "afirmacion": {
    "quote": "deben cumplir con todas las obligaciones establecidas en estas normas, incluyendo la protección de la seguridad e intereses económicos de los usuarios, la información clara y veraz",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "Los usuarios tienen derecho a la protección de su seguridad e intereses económicos",
    "ubicacion": "Obligacion_los_usuarios_tienen_derecho_a_la_proteccion_de_su_seguridad_e_intereses_economic (expuesto en paso 15)"
   },
   "fuente": {
    "quote": "Los usuarios de servicios financieros tienen derecho, en toda relación de consumo, a: − la protección de su seguridad e intereses económicos; − recibir información clara, suficiente, veraz (...) Los sujetos obligados deberán adoptar las acciones necesarias para garantizar estos derechos",
    "ubicacion": "TO_proteccion_usuarios_servicios_financieros_actual.pdf, Punto 2.1"
   }
  }
 },
 {
  "sintoma_capa1": "noise_sensitivity",
  "causa_capa2": "sin_defecto",
  "lado": "ninguno",
  "jerarquia": "sin_par",
  "pata": "Intervención como entidad en el mercado de cambios (ejecuta operaciones de cambio)",
  "evidencia": {
   "afirmacion": {
    "quote": "los operadores de cambio ejecutan operaciones de cambio en divisas conforme a lo establecido en la normativa",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "Operadores de cambio —ejecuta→ Operaciones de cambio en divisas",
    "ubicacion": "EDGE::EntidadFinanciera_operador_de_cambio--ejecuta-->Operacion_operacion_de_cambio (paso 6)"
   },
   "fuente": {
    "quote": "1.1.2.2. Operadores de cambio, por las operaciones comprendidas en las normas sobre “Exterior y cambios”.",
    "ubicacion": "TO_proteccion_usuarios_servicios_financieros_actual.pdf, Punto 1.1.2.2"
   }
  }
 }
]
```

`detectores` (verbatim):

```json
{
 "flag_encuadre_invertido": false,
 "flag_contexto": false,
 "tool_calls_usadas": 12,
 "max_tool_calls": 40,
 "tokens_in": 357340,
 "tokens_out": 9468
}
```

**(c) Longitudes (campos no incluidos):** `razonamiento` = 2677 chars · `extraccion_traza` = 3969 chars (existen ambos)

**(b) Rep 2:**

- `formato_invalido`: `false`
- `errores_formato`: `[]`

`atribuciones` (ÍNTEGRO, verbatim):

```json
[
 {
  "sintoma_capa1": "noise_sensitivity",
  "causa_capa2": "provenance_imprecisa",
  "lado": "grafo",
  "jerarquia": "primaria",
  "pata": "Si el operador de cambio está alcanzado por las normas de Protección de los Usuarios de Servicios Financieros",
  "evidencia": {
   "afirmacion": {
    "quote": "los operadores de cambio figuran explícitamente como sujetos obligados en el Punto 1.1 (Partes) de la normativa",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "\"id\": \"EntidadFinanciera_operador_de_cambio\", ... \"provenances\": [{\"source_doc\": \"TO_proteccion_usuarios_servicios_financieros_actual.pdf\", \"location\": \"Punto 1.1. Partes.\"}]",
    "ubicacion": "EntidadFinanciera_operador_de_cambio (paso 4)"
   },
   "fuente": {
    "quote": "1.1.2.2. Operadores de cambio, por las operaciones comprendidas en las normas sobre “Exterior y cambios”.",
    "ubicacion": "TO_proteccion_usuarios_servicios_financieros_actual.pdf, Punto 1.1.2.2"
   }
  },
  "busquedas": [
   {
    "consulta": "punto 1.1.2 sujetos obligados enumeración (paso 13 del agente)",
    "resultado": "no existe nodo que enumere los sujetos obligados de 1.1.2; el único portador del alcance del operador es su provenance, que apunta a '1.1. Partes.'"
   }
  ]
 },
 {
  "sintoma_capa1": "context_recall",
  "causa_capa2": "completitud_kg",
  "lado": "grafo",
  "jerarquia": "primaria",
  "pata": "Si el operador de cambio debe intervenir como entidad autorizada en el mercado de cambios",
  "evidencia": {
   "afirmacion": {
    "quote": "los operadores de cambio ejecutan operaciones de cambio en divisas conforme a lo establecido en la normativa, aunque la información disponible en el grafo no especifica explícitamente los requisitos de autorización para operar en el mercado de cambios",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "salientes: [{\"relation\": \"ejecuta\", \"vecino_id\": \"Operacion_operacion_de_cambio\", \"vecino_label\": \"Operaciones de cambio en divisas\"}] — ningún nodo/arista sobre condición del operador como entidad autorizada/interviniente en el mercado de cambios",
    "ubicacion": "ver_vecinos EntidadFinanciera_operador_de_cambio (paso 6)"
   },
   "fuente": {
    "quote": "1.1.2.2. Operadores de cambio, por las operaciones comprendidas en las normas sobre “Exterior y cambios”.",
    "ubicacion": "TO_proteccion_usuarios_servicios_financieros_actual.pdf, Punto 1.1.2.2"
   }
  },
  "busquedas": [
   {
    "consulta": "operador cambio autorizado intervenir mercado",
    "resultado": "solo devuelve el nodo operador y operaciones/plazos de liquidación; ningún nodo sobre autorización del operador como interviniente"
   },
   {
    "consulta": "entidad autorizada operar mercado de cambios",
    "resultado": "obligaciones de acceso/plazos de liquidación de exportaciones; nada sobre condición de entidad autorizada del operador"
   },
   {
    "consulta": "autorización previa BCRA operar cambios habilitación",
    "resultado": "restricciones de conformidad previa para clientes que acceden al mercado, no la habilitación del operador como interviniente"
   },
   {
    "consulta": "entidades autorizadas a operar en cambios intervinientes",
    "resultado": "nodos de liquidación/elegibilidad de entidades y casas de cambio, ninguno responde 'el operador debe intervenir como entidad autorizada'"
   }
  ]
 },
 {
  "sintoma_capa1": "context_recall",
  "causa_capa2": "alcanzabilidad_kg",
  "lado": "grafo",
  "jerarquia": "secundaria",
  "pata": "obligación de brindar información clara y veraz (claim no central)",
  "evidencia": {
   "afirmacion": {
    "quote": "deben cumplir con todas las obligaciones establecidas en estas normas, incluyendo la protección de la seguridad e intereses económicos de los usuarios, la información clara y veraz",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "Los sujetos obligados deberán adoptar las acciones necesarias para garantizar derechos de protección de seguridad e intereses económicos, información clara y veraz, libertad de elección, y trato equitativo a todos los actuales y potenciales usuarios",
    "ubicacion": "Obligacion_los_sujetos_obligados_deberan_adoptar_las_acciones_necesarias_para_garantizar_de"
   },
   "fuente": {
    "quote": "recibir información clara, suficiente, veraz y de fácil acceso y visibilidad acerca de los productos y/o servicios que contraten",
    "ubicacion": "TO_proteccion_usuarios_servicios_financieros_actual.pdf, Punto 2.1"
   }
  },
  "busquedas": [
   {
    "consulta": "revisión de outputs completos pasos 2, 8 y 15 (ver_paso_completo)",
    "resultado": "el nodo 'Garantizar derechos de usuarios' (único con la frase 'información clara y veraz') NO aparece en ningún output; su label genérico no matchea las búsquedas del agente ('operador cambio', 'protección usuarios bancos...'), su description no está indexada"
   }
  ]
 },
 {
  "sintoma_capa1": "noise_sensitivity",
  "causa_capa2": "sin_defecto",
  "lado": "ninguno",
  "jerarquia": "sin_par",
  "pata": "protección de seguridad e intereses económicos (claim no central)",
  "evidencia": {
   "afirmacion": {
    "quote": "deben cumplir con ... la protección de la seguridad e intereses económicos de los usuarios",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "Los usuarios tienen derecho a la protección de su seguridad e intereses económicos",
    "ubicacion": "Obligacion_los_usuarios_tienen_derecho_a_la_proteccion_de_su_seguridad_e_intereses_economic (resumen expuesto en paso 15)"
   },
   "fuente": {
    "quote": "Los usuarios de servicios financieros tienen derecho, en toda relación de consumo, a: − la protección de su seguridad e intereses económicos",
    "ubicacion": "TO_proteccion_usuarios_servicios_financieros_actual.pdf, Punto 2.1"
   }
  },
  "busquedas": [
   {
    "consulta": "ver_paso_completo paso 15",
    "resultado": "el resumen del nodo se expuso al agente; el claim está soportado y es fiel al PDF 2.1 — falso positivo del juez al marcarlo 'no_soportado'"
   }
  ]
 }
]
```

`detectores` (verbatim):

```json
{
 "flag_encuadre_invertido": false,
 "flag_contexto": false,
 "tool_calls_usadas": 17,
 "max_tool_calls": 40,
 "tokens_in": 598776,
 "tokens_out": 11988
}
```

**(c) Longitudes (campos no incluidos):** `razonamiento` = 2609 chars · `extraccion_traza` = 3869 chars (existen ambos)

**(b) Rep 3:**

- `formato_invalido`: `false`
- `errores_formato`: `[]`

`atribuciones` (ÍNTEGRO, verbatim):

```json
[
 {
  "sintoma_capa1": "noise_sensitivity",
  "causa_capa2": "sin_defecto",
  "lado": "ninguno",
  "jerarquia": "sin_par",
  "pata": "Si el operador de cambio está alcanzado por las normas de Protección de los Usuarios de Servicios Financieros",
  "evidencia": {
   "afirmacion": {
    "quote": "Los operadores de cambio figuran explícitamente como sujetos obligados en el Punto 1.1 (Partes) de la normativa de Protección de Usuarios.",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "\"id\": \"EntidadFinanciera_operador_de_cambio\", \"label\": \"Operadores de cambio\", \"properties\": {\"categoria\": \"operador de cambio\"}, \"provenances\": [{\"source_doc\": \"TO_proteccion_usuarios_servicios_financieros_actual.pdf\", \"location\": \"Punto 1.1. Partes.\"}]",
    "ubicacion": "EntidadFinanciera_operador_de_cambio (paso 4)"
   },
   "fuente": {
    "quote": "1.1.2. Sujetos obligados.\n1.1.2.1. Entidades financieras.\n1.1.2.2. Operadores de cambio, por las operaciones comprendidas en las normas sobre “Exterior y cambios”.",
    "ubicacion": "TO_proteccion_usuarios_servicios_financieros_actual.pdf, Punto 1.1 (p.3)"
   }
  }
 },
 {
  "sintoma_capa1": "noise_sensitivity",
  "causa_capa2": "sin_defecto",
  "lado": "ninguno",
  "jerarquia": "sin_par",
  "pata": "Si el operador de cambio está alcanzado por las normas de Protección de los Usuarios de Servicios Financieros",
  "evidencia": {
   "afirmacion": {
    "quote": "Los operadores de cambio deben cumplir con la protección de la seguridad e intereses económicos de los usuarios.",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "Los sujetos obligados deberán adoptar las acciones necesarias para garantizar derechos de protección de seguridad e intereses económicos, información clara y veraz, libertad de elección, y trato equitativo a todos los actuales y potenciales usuarios",
    "ubicacion": "Obligacion_los_sujetos_obligados_deberan_adoptar_las_acciones_necesarias_para_garantizar_de (expuesto en pasos 8/15; abierto en verificación)"
   },
   "fuente": {
    "quote": "Los usuarios de servicios financieros tienen derecho, en toda relación de consumo, a: − la protección de su seguridad e intereses económicos; (…) Los sujetos obligados deberán adoptar las acciones necesarias para garantizar estos derechos a todos los actuales y potenciales usuarios",
    "ubicacion": "TO_proteccion_usuarios_servicios_financieros_actual.pdf, Punto 2.1. Concepto."
   }
  }
 },
 {
  "sintoma_capa1": "noise_sensitivity",
  "causa_capa2": "sin_defecto",
  "lado": "ninguno",
  "jerarquia": "sin_par",
  "pata": "Si el operador de cambio está alcanzado por las normas de Protección de los Usuarios de Servicios Financieros",
  "evidencia": {
   "afirmacion": {
    "quote": "Los operadores de cambio deben cumplir con la obligación de brindar información clara y veraz.",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "Los sujetos obligados deberán adoptar las acciones necesarias para garantizar derechos de protección de seguridad e intereses económicos, información clara y veraz, libertad de elección, y trato equitativo a todos los actuales y potenciales usuarios",
    "ubicacion": "Obligacion_los_sujetos_obligados_deberan_adoptar_las_acciones_necesarias_para_garantizar_de"
   },
   "fuente": {
    "quote": "− recibir información clara, suficiente, veraz y de fácil acceso y visibilidad acerca de los productos y/o servicios que contraten",
    "ubicacion": "TO_proteccion_usuarios_servicios_financieros_actual.pdf, Punto 2.1. Concepto."
   }
  }
 },
 {
  "sintoma_capa1": "noise_sensitivity",
  "causa_capa2": "sin_defecto",
  "lado": "ninguno",
  "jerarquia": "sin_par",
  "pata": "Si el operador de cambio debe intervenir como entidad autorizada en el mercado de cambios",
  "evidencia": {
   "afirmacion": {
    "quote": "Los operadores de cambio ejecutan operaciones de cambio en divisas conforme a lo establecido en la normativa.",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "Operadores de cambio —ejecuta→ Operaciones de cambio en divisas",
    "ubicacion": "EDGE::EntidadFinanciera_operador_de_cambio--ejecuta-->Operacion_operacion_de_cambio (paso 6, provenance Punto 1.1. Partes.)"
   },
   "fuente": {
    "quote": "1.1.2.2. Operadores de cambio, por las operaciones comprendidas en las normas sobre “Exterior y cambios”.",
    "ubicacion": "TO_proteccion_usuarios_servicios_financieros_actual.pdf, Punto 1.1 (p.3)"
   }
  }
 }
]
```

`detectores` (verbatim):

```json
{
 "flag_encuadre_invertido": false,
 "flag_contexto": false,
 "tool_calls_usadas": 13,
 "max_tool_calls": 40,
 "tokens_in": 411011,
 "tokens_out": 9259
}
```

**(c) Longitudes (campos no incluidos):** `razonamiento` = 2486 chars · `extraccion_traza` = 4446 chars (existen ambos)


### CQ-020 — `gate2_v57/off_run_3_CQ-020.json` (id_falla: run_3/CQ-020, n_reps: 3)

**(a) `voto` completo, verbatim:**

```json
{
 "resultado": "frontera_no_determinada",
 "flag_voto_dividido": true,
 "pares_primarios_ganadores": null,
 "votos_ganadores": null,
 "conteo": [
  {
   "pares_primarios": [
    [
     "noise_sensitivity",
     "aplicacion_erronea"
    ],
    [
     "noise_sensitivity",
     "contenido_kg"
    ]
   ],
   "votos": 1
  },
  {
   "pares_primarios": [
    [
     "noise_sensitivity",
     "aplicacion_erronea"
    ]
   ],
   "votos": 1
  },
  {
   "pares_primarios": [
    [
     "noise_sensitivity",
     "aplicacion_erronea"
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
     "aplicacion_erronea"
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
     "aplicacion_erronea"
    ]
   ],
   "formato_invalido": false
  },
  {
   "rep": 3,
   "pares_primarios": [
    [
     "noise_sensitivity",
     "aplicacion_erronea"
    ],
    [
     "noise_sensitivity",
     "provenance_imprecisa"
    ]
   ],
   "formato_invalido": false
  }
 ]
}
```

**(b) Rep 1:**

- `formato_invalido`: `false`
- `errores_formato`: `[]`

`atribuciones` (ÍNTEGRO, verbatim):

```json
[
 {
  "sintoma_capa1": "noise_sensitivity",
  "causa_capa2": "contenido_kg",
  "lado": "grafo",
  "jerarquia": "primaria",
  "pata": "Cómo se calcula la exigencia de capital por riesgo de crédito (CRC)",
  "evidencia": {
   "afirmacion": {
    "quote": "Alternativamente, sin incluir el término INC, se utiliza la fórmula: Código 70100000 (n) = k x 0,08 [ ∑(A x p) + ∑ (PFB x CCF x p) + ∑ (12300000 x p) + (∑ 13X00000 + 14000000 + 86300000) x 12,5 + 15000000 ]",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "Cálculo de la exigencia por riesgo de crédito sin incluir el término INC mediante la fórmula: Código 70100000 (n) = k x 0,08 [ ∑(A x p) + ∑ (PFB x CCF x p) + ∑ (12300000 x p) + (∑ 13X00000 + 14000000 + 86300000) x 12,5 + 15000000 ]",
    "ubicacion": "Operacion_calculo_de_exigencia_por_riesgo (abierto en paso 6)"
   },
   "fuente": {
    "quote": "8.2. Modelo de información. Cuadro 8.2.1. Código Concepto 70100000 Exigencia por riesgo de crédito sin incluir el término INC 70500000 Cálculo del riesgo de tasa de interés... Sección 8. Totales de control.",
    "ubicacion": "TO_regimen_informativo_contable_mensual_actual.pdf, Punto 8.2"
   }
  },
  "busquedas": [
   {
    "consulta": "leer_pasaje_pdf Punto 8.1 Normas de procedimiento (la prov del nodo)",
    "resultado": "devuelve el ÍNDICE de secciones 8/9 'Incrementos de exigencia por riesgo de crédito', NO contiene ninguna fórmula 70100000=k x 0,08[...]"
   },
   {
    "consulta": "leer_pasaje_pdf Punto 8.2",
    "resultado": "el código 70100000 es solo el concepto 'Exigencia por riesgo de crédito sin incluir el término INC' en el cuadro de Totales de control; no hay fórmula desarrollada"
   },
   {
    "consulta": "70100000 exigencia riesgo crédito código (buscar_nodos)",
    "resultado": "el único nodo que porta la fórmula desarrollada es Operacion_calculo_de_exigencia_por_riesgo; el PDF no la respalda"
   }
  ]
 },
 {
  "sintoma_capa1": "noise_sensitivity",
  "causa_capa2": "aplicacion_erronea",
  "lado": "agente",
  "jerarquia": "primaria",
  "pata": "Con qué frecuencia se reporta al BCRA",
  "evidencia": {
   "afirmacion": {
    "quote": "Las entidades financieras deben presentar información sobre exigencia de capitales mínimos por riesgo de mercado con periodicidad mensual, desglosada por código de concepto y día del mes.",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "Presentar información sobre exigencia de capitales mínimos por riesgo de mercado con periodicidad mensual, desglosada por código de concepto y día del mes",
    "ubicacion": "Obligacion_informar_exigencia_de_capitales_por_riesgo (abierto en paso 9)"
   },
   "fuente": {
    "quote": "4.2. Modelos de información. Cuadro 4.2.1. Exigencia (...) 313000/xx Exigencia por riesgo de tipo de cambio (...) xx = día del mes a que corresponde la información (...) Sección 4. Exigencia e integración por riesgo de mercado",
    "ubicacion": "TO_regimen_informativo_contable_mensual_actual.pdf, Punto 4.2"
   }
  },
  "busquedas": [
   {
    "consulta": "informar exigencia riesgo crédito periodicidad presentación",
    "resultado": "el nodo que se aplicó es de riesgo de MERCADO; no hay uno que ligue frecuencia de reporte a riesgo de crédito específicamente"
   },
   {
    "consulta": "frecuencia mensual presentación régimen informativo capitales",
    "resultado": "existe Obligacion_presentar_informacion_con_frecuencia_mensual (frecuencia mensual genérica), no consultado por el agente"
   }
  ]
 },
 {
  "sintoma_capa1": "faithfulness",
  "causa_capa2": "completitud_kg",
  "lado": "grafo",
  "jerarquia": "secundaria",
  "pata": "Cómo se calcula la exigencia de capital por riesgo de crédito (CRC)",
  "evidencia": {
   "afirmacion": {
    "quote": "donde A representa activos, p los ponderadores de riesgo, PFB posiciones fuera de balance, y CCF factores de conversión de crédito",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "Cálculo de la exigencia por riesgo de crédito sin incluir el término INC mediante la fórmula: Código 70100000 (n) = k x 0,08 [ ∑(A x p) + ∑ (PFB x CCF x p) + ... ]",
    "ubicacion": "Operacion_calculo_de_exigencia_por_riesgo — porta la fórmula pero NO define A/p/PFB/CCF"
   },
   "fuente": {
    "quote": "PFB: partidas fuera de balance. Sobre los citados conceptos A y PFB se aplicarán los ponderadores de riesgo de contraparte (p) por operación... sus importes deberán multiplicarse por el factor de conversión crediticia (CCF)",
    "ubicacion": "TO_regimen_informativo_contable_mensual_actual.pdf, p. 6 (Punto 3.1.2)"
   }
  },
  "busquedas": [
   {
    "consulta": "APR_c factor ponderación riesgo (paso 10 del agente)",
    "resultado": "255 matches; ningún nodo define A/p/PFB/CCF de la fórmula CRC"
   },
   {
    "consulta": "leer_pasaje_pdf p.6 / Punto 3.1.2",
    "resultado": "el PDF SÍ define A, p, PFB, CCF; el grafo no extrajo esas definiciones en ningún nodo"
   }
  ]
 },
 {
  "sintoma_capa1": "faithfulness",
  "causa_capa2": "alucinacion_agente",
  "lado": "agente",
  "jerarquia": "secundaria",
  "pata": "Cómo se calcula la exigencia de capital por riesgo de crédito (CRC)",
  "evidencia": {
   "afirmacion": {
    "quote": "0,08 es el coeficiente de capital mínimo",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "Determinación de la exigencia de capital por riesgo de crédito conforme a la fórmula C_RC = (k x 0,08 x APR_c) + INC",
    "ubicacion": "Operacion_calculo_de_capital_minimo — expone '0,08' pero NO lo etiqueta 'coeficiente de capital mínimo'"
   },
   "fuente": {
    "quote": "CRC = (k x 0,08 x APRc) + INC donde: CRC = exigencia de capital por riesgo de crédito. k = factor vinculado a la calificación... APRc = activos ponderados por riesgo de crédito",
    "ubicacion": "TO_regimen_informativo_contable_mensual_actual.pdf, Punto 3.1.2 (el PDF define CRC, k y APRc, pero NO glosa el 0,08 como 'coeficiente de capital mínimo')"
   }
  },
  "busquedas": [
   {
    "consulta": "leer_pasaje_pdf Punto 3.1.2",
    "resultado": "el PDF muestra el 0,08 dentro de la fórmula pero no lo denomina 'coeficiente de capital mínimo'; ningún nodo consultado lo etiqueta así — glosa de cosecha propia (modo b)"
   }
  ]
 }
]
```

`detectores` (verbatim):

```json
{
 "flag_encuadre_invertido": true,
 "flag_contexto": false,
 "tool_calls_usadas": 18,
 "max_tool_calls": 40,
 "tokens_in": 368239,
 "tokens_out": 11347
}
```

**(c) Longitudes (campos no incluidos):** `razonamiento` = 1946 chars · `extraccion_traza` = 2942 chars (existen ambos)

**(b) Rep 2:**

- `formato_invalido`: `false`
- `errores_formato`: `[]`

`atribuciones` (ÍNTEGRO, verbatim):

```json
[
 {
  "sintoma_capa1": "noise_sensitivity",
  "causa_capa2": "aplicacion_erronea",
  "lado": "agente",
  "jerarquia": "primaria",
  "pata": "Con qué frecuencia se reporta al BCRA",
  "evidencia": {
   "afirmacion": {
    "quote": "Las entidades financieras deben presentar información sobre exigencia de capitales mínimos por riesgo de mercado con periodicidad mensual, desglosada por código de concepto y día del mes.",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "Presentar información sobre exigencia de capitales mínimos por riesgo de mercado con periodicidad mensual, desglosada por código de concepto y día del mes",
    "ubicacion": "Obligacion_informar_exigencia_de_capitales_por_riesgo (paso 9)"
   },
   "fuente": {
    "quote": "4.2. Modelos de información\nCuadro 4.2.1. Exigencia\nCódigo Concepto 311000/xx Exigencia por riesgo de tasa - Total (...) 313000/xx Exigencia por riesgo de tipo de cambio (...) Sección 4. Exigencia e integración por riesgo de mercado",
    "ubicacion": "TO_regimen_informativo_contable_mensual_actual.pdf, Punto 4.2. Modelos de información"
   }
  },
  "busquedas": [
   {
    "consulta": "presentar información exigencia capitales mínimos mensual",
    "resultado": "encontrado Obligacion_presentar_informacion_con_frecuencia_mensual (Punto 1.1: 'La información tendrá frecuencia mensual') — nodo GENERAL y correcto que el agente NO consultó"
   },
   {
    "consulta": "régimen informativo periodicidad presentación",
    "resultado": "TextoOrdenado RICM y nodo de frecuencia mensual; confirma que la frecuencia general es mensual sin ligarse a riesgo de mercado"
   }
  ]
 },
 {
  "sintoma_capa1": "noise_sensitivity",
  "causa_capa2": "sin_defecto",
  "lado": "ninguno",
  "jerarquia": "sin_par",
  "pata": "Cómo se calcula la exigencia de capital por riesgo de crédito (CRC)",
  "evidencia": {
   "afirmacion": {
    "quote": "Existe una fórmula alternativa sin el término INC identificada como Código 70100000(n) = k x 0,08 [ ∑(A x p) + ∑(PFB x CCF x p) + ∑(12300000 x p) + (∑ 13X00000 + 14000000 + 86300000) x 12,5 + 15000000 ]",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "Cálculo de la exigencia por riesgo de crédito sin incluir el término INC mediante la fórmula: Código 70100000 (n) = k x 0,08 [ ∑(A x p) + ∑ (PFB x CCF x p) + ∑ (12300000 x p) + (∑ 13X00000 + 14000000 + 86300000) x 12,5 + 15000000 ]",
    "ubicacion": "Operacion_calculo_de_exigencia_por_riesgo (paso 6)"
   },
   "fuente": {
    "quote": "8.1.1. Código 70100000. Exigencia por riesgo de crédito sin incluir el término INC: Código 70100000 (n) = k x 0,08 [ ∑(A x p) + ∑ (PFB x CCF x p) + ∑ (12300000 x p) + (∑ 13X00000 + 14000000 + 86300000) x 12,5 + 15000000 ]",
    "ubicacion": "TO_regimen_informativo_contable_mensual_actual.pdf, p. 37 (Punto 8.1.1)"
   }
  },
  "busquedas": [
   {
    "consulta": "70100000 fórmula código riesgo crédito",
    "resultado": "el nodo Operacion_calculo_de_exigencia_por_riesgo contiene la fórmula exacta"
   },
   {
    "consulta": "Punto 8.2 / p.37-38 del PDF",
    "resultado": "el PDF (Punto 8.1.1, p.37) reproduce la fórmula 70100000 idéntica al nodo y a la respuesta del agente; el juez la marcó no_soportado erróneamente"
   }
  ]
 },
 {
  "sintoma_capa1": "faithfulness",
  "causa_capa2": "alucinacion_agente",
  "lado": "agente",
  "jerarquia": "secundaria",
  "pata": "Cómo se calcula la exigencia de capital por riesgo de crédito (CRC)",
  "evidencia": {
   "afirmacion": {
    "quote": "0,08 es el coeficiente de capital mínimo",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "Determinación de la exigencia de capital por riesgo de crédito conforme a la fórmula C_RC = (k x 0,08 x APR_c) + INC",
    "ubicacion": "Operacion_calculo_de_capital_minimo (paso 4)"
   },
   "fuente": {
    "quote": "CRC = (k x 0,08 x APRc) + INC donde: CRC = exigencia de capital por riesgo de crédito. k = factor vinculado a la calificación asignada a la entidad (...)",
    "ubicacion": "TO_regimen_informativo_contable_mensual_actual.pdf, Punto 3.1.2 (p.5) — no etiqueta el 0,08 como 'coeficiente de capital mínimo'"
   }
  },
  "busquedas": [
   {
    "consulta": "leer_pasaje_pdf Punto 3.1 / p.5-6",
    "resultado": "el PDF define CRC, k, APRc, A, PFB, CCF, p, INC pero NO glosa el valor 0,08 con la etiqueta 'coeficiente de capital mínimo'; ningún nodo consultado la aporta — es glosa propia del agente"
   }
  ]
 },
 {
  "sintoma_capa1": "faithfulness",
  "causa_capa2": "alucinacion_agente",
  "lado": "agente",
  "jerarquia": "secundaria",
  "pata": "Cómo se calcula la exigencia de capital por riesgo de crédito (CRC)",
  "evidencia": {
   "afirmacion": {
    "quote": "donde A representa activos, p los ponderadores de riesgo, PFB posiciones fuera de balance, y CCF factores de conversión de crédito",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "Cálculo de la exigencia por riesgo de crédito sin incluir el término INC mediante la fórmula: Código 70100000 (n) = k x 0,08 [ ∑(A x p) + ∑ (PFB x CCF x p) + ... ]",
    "ubicacion": "Operacion_calculo_de_exigencia_por_riesgo (paso 6) — nombra A, PFB, CCF, p pero NO las define"
   },
   "fuente": {
    "quote": "A: activos computables /exposiciones -saldos de deuda-. (...) PFB: partidas fuera de balance. (...) el factor de conversión crediticia (CCF) (...) los ponderadores de riesgo de contraparte (p)",
    "ubicacion": "TO_regimen_informativo_contable_mensual_actual.pdf, p.5-6 (Punto 3.1.2)"
   }
  },
  "busquedas": [
   {
    "consulta": "factor conversión crediticia CCF partidas fuera de balance",
    "resultado": "existen nodos que definen los términos (Obligacion_las_partidas_fuera_de_balance..., Operacion_conversion_crediticia) alcanzables, pero el agente NO los consultó; sus glosas son fácticamente correctas contra el PDF pero sin soporte de un nodo de su trayectoria"
   }
  ]
 }
]
```

`detectores` (verbatim):

```json
{
 "flag_encuadre_invertido": true,
 "flag_contexto": false,
 "tool_calls_usadas": 28,
 "max_tool_calls": 40,
 "tokens_in": 692013,
 "tokens_out": 13540
}
```

**(c) Longitudes (campos no incluidos):** `razonamiento` = 1872 chars · `extraccion_traza` = 2955 chars (existen ambos)

**(b) Rep 3:**

- `formato_invalido`: `false`
- `errores_formato`: `[]`

`atribuciones` (ÍNTEGRO, verbatim):

```json
[
 {
  "sintoma_capa1": "noise_sensitivity",
  "causa_capa2": "aplicacion_erronea",
  "lado": "agente",
  "jerarquia": "primaria",
  "pata": "Con qué frecuencia se reporta al BCRA",
  "evidencia": {
   "afirmacion": {
    "quote": "Las entidades financieras deben presentar información sobre exigencia de capitales mínimos por riesgo de mercado con periodicidad mensual, desglosada por código de concepto y día del mes.",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "Presentar información sobre exigencia de capitales mínimos por riesgo de mercado con periodicidad mensual, desglosada por código de concepto y día del mes",
    "ubicacion": "Obligacion_informar_exigencia_de_capitales_por_riesgo"
   },
   "fuente": {
    "quote": "4.2. Modelos de información \n \nCuadro 4.2.1. Exigencia (…) 311000/xx Exigencia por riesgo de tasa - Total (…) xx = día del mes a que corresponde la información (…) Sección 4. Exigencia e integración por riesgo de mercado",
    "ubicacion": "TO_regimen_informativo_contable_mensual_actual.pdf, Punto 4.2. Modelos de información"
   }
  },
  "busquedas": [
   {
    "consulta": "informar exigencia riesgo crédito periodicidad presentación",
    "resultado": "El único nodo con frecuencia+desglose es Obligacion_informar_exigencia_de_capitales_por_riesgo, que declara EN su contenido 'por riesgo de mercado'; no hay nodo que porte la frecuencia de reporte específica del CRC"
   },
   {
    "consulta": "régimen informativo contable mensual presentación información",
    "resultado": "Nodos genéricos de presentación (contable trimestral, SEPAIMPO), ninguno específico de la frecuencia de reporte de la exigencia por riesgo de crédito"
   }
  ]
 },
 {
  "sintoma_capa1": "noise_sensitivity",
  "causa_capa2": "provenance_imprecisa",
  "lado": "grafo",
  "jerarquia": "primaria",
  "pata": "Cómo se calcula la exigencia de capital por riesgo de crédito (CRC)",
  "evidencia": {
   "afirmacion": {
    "quote": "Alternativamente, sin incluir el término INC, se utiliza la fórmula: Código 70100000 (n) = k x 0,08 [ ∑(A x p) + ∑ (PFB x CCF x p) + ∑ (12300000 x p) + (∑ 13X00000 + 14000000 + 86300000) x 12,5 + 15000000 ], donde A representa activos, p los ponderadores de riesgo, PFB posiciones fuera de balance, y CCF factores de conversión de crédito.",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "Cálculo de la exigencia por riesgo de crédito sin incluir el término INC mediante la fórmula: Código 70100000 (n) = k x 0,08 [ ∑(A x p) + ∑ (PFB x CCF x p) + ∑ (12300000 x p) + (∑ 13X00000 + 14000000 + 86300000) x 12,5 + 15000000 ]",
    "ubicacion": "Operacion_calculo_de_exigencia_por_riesgo (provenance: Punto 8.1. Normas de procedimiento.)"
   },
   "fuente": {
    "quote": "8.1. Normas de procedimiento \n8.2. Modelo de información \nSección 9. Incrementos de exigencia por riesgo de crédito (…) 4 . RÉGIMEN INFORMATIVO SOBRE EXIGENCIA E INTEGRACIÓN DE CAPITALES MÍNIMOS",
    "ubicacion": "TO_regimen_informativo_contable_mensual_actual.pdf, Punto 8.1. Normas de procedimiento."
   }
  },
  "busquedas": [
   {
    "consulta": "70100000 exigencia riesgo crédito código",
    "resultado": "Solo el nodo Operacion_calculo_de_exigencia_por_riesgo porta la cadena; no hay otro nodo con la fórmula fundada"
   },
   {
    "consulta": "Código 70100000 (leer_pasaje_pdf)",
    "resultado": "localizacion_pdf='fallida': el código no se ancla en el PDF"
   },
   {
    "consulta": "Punto 8.1 (leer_pasaje_pdf)",
    "resultado": "El pasaje es un ÍNDICE de secciones (8.1/8.2/Sección 9), no contiene la fórmula 70100000: la provenance no funda el contenido del nodo"
   }
  ]
 },
 {
  "sintoma_capa1": "faithfulness",
  "causa_capa2": "alucinacion_agente",
  "lado": "agente",
  "jerarquia": "secundaria",
  "pata": "Cómo se calcula la exigencia de capital por riesgo de crédito (CRC)",
  "evidencia": {
   "afirmacion": {
    "quote": "0,08 es el coeficiente de capital mínimo",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "Determinación de la exigencia de capital por riesgo de crédito conforme a la fórmula C_RC = (k x 0,08 x APR_c) + INC",
    "ubicacion": "Operacion_calculo_de_capital_minimo (el nodo trae la fórmula pero NO glosa el 0,08 como 'coeficiente de capital mínimo')"
   },
   "fuente": {
    "quote": "CRC = (k x 0,08 x APRc) + INC \ndonde: \nCRC = exigencia de capital por riesgo de crédito. \nk = factor vinculado a la calificación asignada a la entidad (…) APRc = activos ponderados por riesgo de crédito",
    "ubicacion": "TO_regimen_informativo_contable_mensual_actual.pdf, Punto 3.1.2 (el PDF NO etiqueta el 0,08 como 'coeficiente de capital mínimo')"
   }
  },
  "busquedas": [
   {
    "consulta": "INC incremento exigencia capital (paso 11 del agente)",
    "resultado": "Ningún nodo consultado glosa el 0,08 como 'coeficiente de capital mínimo'"
   },
   {
    "consulta": "leer_pasaje_pdf Punto 3.1.2 / 3.1 / 3.1.3",
    "resultado": "El PDF define k, APRc, INC pero no rotula el 0,08: la etiqueta es una glosa agregada por el agente"
   }
  ]
 }
]
```

`detectores` (verbatim):

```json
{
 "flag_encuadre_invertido": false,
 "flag_contexto": false,
 "tool_calls_usadas": 28,
 "max_tool_calls": 40,
 "tokens_in": 630987,
 "tokens_out": 11939
}
```

**(c) Longitudes (campos no incluidos):** `razonamiento` = 2035 chars · `extraccion_traza` = 2963 chars (existen ambos)


### CQ-025 — `gate2_v57/off_run_3_CQ-025.json` (id_falla: run_3/CQ-025, n_reps: 3)

**(a) `voto` completo, verbatim:**

```json
{
 "resultado": "mayoria",
 "flag_voto_dividido": false,
 "pares_primarios_ganadores": [
  [
   "noise_sensitivity",
   "aplicacion_erronea"
  ]
 ],
 "votos_ganadores": 2,
 "conteo": [
  {
   "pares_primarios": [
    [
     "noise_sensitivity",
     "aplicacion_erronea"
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
     "noise_sensitivity",
     "aplicacion_erronea"
    ]
   ],
   "formato_invalido": false
  },
  {
   "rep": 3,
   "pares_primarios": [
    [
     "noise_sensitivity",
     "aplicacion_erronea"
    ]
   ],
   "formato_invalido": false
  }
 ]
}
```

**(b) Rep 1:**

- `formato_invalido`: `false`
- `errores_formato`: `[]`

`atribuciones` (ÍNTEGRO, verbatim):

```json
[
 {
  "sintoma_capa1": "context_recall",
  "causa_capa2": "navegación",
  "lado": "agente",
  "jerarquia": "primaria",
  "pata": "Frecuencia con que se informa la exigencia por riesgo de mercado en el Régimen Informativo de Capitales Mínimos",
  "evidencia": {
   "afirmacion": {
    "quote": "La exigencia por riesgo de mercado se determina en forma diaria, conforme a lo establecido en el punto 1.3 de la normativa de Capitales Mínimos.",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "Presentar información sobre exigencia de capitales mínimos por riesgo de mercado con periodicidad mensual, desglosada por código de concepto y día del mes",
    "ubicacion": "Obligacion_informar_exigencia_de_capitales_por_riesgo (plazo: mensual; NO consultado por el agente)"
   },
   "fuente": {
    "quote": "1.1. La información tendrá frecuencia mensual y se integrará con datos referidos al mes bajo análisis, excepto las siguientes informaciones que tendrán frecuencia trimestral (...) - Datos complementarios vinculados al cálculo de la exigencia por riesgo de mercado (puntos 4.3., 4.4. y 4.5. de la Sección 4.)",
    "ubicacion": "TO_regimen_informativo_contable_mensual_actual.pdf, Punto 1.1"
   }
  },
  "busquedas": [
   {
    "consulta": "informar exigencia riesgo mercado régimen informativo frecuencia",
    "resultado": "DEVUELVE el nodo pertinente 'Obligacion_informar_exigencia_de_capitales_por_riesgo' (label 'Informar exigencia de capitales por riesgo', periodicidad mensual)"
   },
   {
    "consulta": "verificación pasos 2, 7 y 8 del agente (ver_paso_completo)",
    "resultado": "el nodo pertinente NO aparece en las búsquedas del agente ('riesgo de mercado frecuencia informe', 'exigencia riesgo mercado frecuencia mensual trimestral', 'régimen informativo riesgo mercado mensual'); el agente combinó 'riesgo mercado' con 'frecuencia/mensual' pero no con 'informar'"
   }
  ]
 },
 {
  "sintoma_capa1": "noise_sensitivity",
  "causa_capa2": "sin_defecto",
  "lado": "ninguno",
  "jerarquia": "sin_par",
  "pata": "Frecuencia con que se informa la información sobre ratio de apalancamiento en el Régimen Informativo de Capitales Mínimos",
  "evidencia": {
   "afirmacion": {
    "quote": "La información sobre Ratio de apalancamiento se informa con frecuencia trimestral, en base individual y consolidada, según lo dispuesto en el punto 10.1 del Régimen Informativo Contable Mensual. Esta frecuencia trimestral se mantiene incluso en casos de suspensión de consolidación nivel 3, como se especifica en el punto 12.4 de la misma normativa.",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "Se informará el ratio de apalancamiento y sus componentes según el modelo de información previsto en el punto 10.2. (...) Los datos se informarán con frecuencia trimestral, sobre base individual y consolidada trimestral",
    "ubicacion": "Obligacion_informar_ratio_de_apalancamiento_trimestral (prov Punto 10.1); y Excepcion_excepcion_para_ratio_de_apalancamiento: 'La suspensión de consolidación nivel 3 no aplicará al Ratio de apalancamiento, que mantendrá su frecuencia trimestral' (prov Punto 12.4)"
   },
   "fuente": {
    "quote": "Los datos se informarán con frecuencia trimestral, sobre base individual y consolidada trimestral (...)  [Punto 12.4] Ratio de apalancamiento (Sección 10.) a) (...) mantendrá su frecuencia trimestral (...) con la excepción prevista para Ratio de apalancamiento",
    "ubicacion": "TO_regimen_informativo_contable_mensual_actual.pdf, Puntos 10.1 y 12.4"
   }
  },
  "busquedas": [
   {
    "consulta": "leer_pasaje_pdf Punto 10.1 y Punto 12.4 del TO régimen informativo",
    "resultado": "el PDF confirma verbatim: frecuencia trimestral, base individual y consolidada, provenance 10.1; y suspensión nivel 3 con excepción para ratio de apalancamiento en punto 12.4. Los claims marcados 'no_soportado'/'falso' por el juez están SOPORTADOS por nodos consultados (pasos 5 y 6) y son CORRECTOS contra el PDF"
   }
  ]
 }
]
```

`detectores` (verbatim):

```json
{
 "flag_encuadre_invertido": false,
 "flag_contexto": false,
 "tool_calls_usadas": 12,
 "max_tool_calls": 40,
 "tokens_in": 245408,
 "tokens_out": 9162
}
```

**(c) Longitudes (campos no incluidos):** `razonamiento` = 2839 chars · `extraccion_traza` = 4182 chars (existen ambos)

**(b) Rep 2:**

- `formato_invalido`: `false`
- `errores_formato`: `[]`

`atribuciones` (ÍNTEGRO, verbatim):

```json
[
 {
  "sintoma_capa1": "noise_sensitivity",
  "causa_capa2": "aplicacion_erronea",
  "lado": "agente",
  "jerarquia": "primaria",
  "pata": "Frecuencia con que se informa la exigencia por riesgo de mercado en el Régimen Informativo",
  "evidencia": {
   "afirmacion": {
    "quote": "La exigencia por riesgo de mercado se determina en forma diaria, conforme a lo establecido en el punto 1.3 de la normativa de Capitales Mínimos.",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "En el caso de la exigencia de capital mínimo por riesgo de mercado, la integración se determinará en forma diaria de acuerdo con lo establecido en el punto 6.7.1",
    "ubicacion": "Obligacion_determinar_integracion_por_riesgo_de_mercado (abierto por el agente, paso 4; plazo: 'diario')"
   },
   "fuente": {
    "quote": "En el caso de la exigencia de capital mínimo por riesgo de mercado, la integración se determinará en forma diaria de acuerdo con lo establecido en el punto 6.7.1.",
    "ubicacion": "TO_capitales_minimos_actual.pdf, Punto 1.3. Integración."
   }
  },
  "busquedas": [
   {
    "consulta": "exigencia riesgo mercado se informará diariamente régimen informativo",
    "resultado": "ningún nodo dice que la exigencia por riesgo de mercado se INFORME en forma diaria en el RI; el más relevante ('Consignación de exigencia por riesgo mercado') dice 'al último día del período de información'"
   },
   {
    "consulta": "riesgo de mercado se informará con frecuencia diaria",
    "resultado": "ningún nodo asocia 'diaria' a la frecuencia de información del RI; 'diario' solo aparece ligado a integración de capital (punto 1.3) y a valuación de posiciones"
   }
  ]
 },
 {
  "sintoma_capa1": "noise_sensitivity",
  "causa_capa2": "sin_defecto",
  "lado": "ninguno",
  "jerarquia": "sin_par",
  "pata": "Frecuencia con que se informa la información sobre ratio de apalancamiento en el Régimen Informativo",
  "evidencia": {
   "afirmacion": {
    "quote": "La información sobre Ratio de apalancamiento se informa con frecuencia trimestral, en base individual y consolidada, según lo dispuesto en el punto 10.1 del Régimen Informativo Contable Mensual. Esta frecuencia trimestral se mantiene incluso en casos de suspensión de consolidación nivel 3, como se especifica en el punto 12.4 de la misma normativa.",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "Se informará el ratio de apalancamiento y sus componentes según el modelo de información previsto en el punto 10.2. (...) Los datos se informarán con frecuencia trimestral, sobre base individual y consolidada trimestral",
    "ubicacion": "Obligacion_informar_ratio_de_apalancamiento_trimestral (paso 5, provenance Punto 10.1 RICM) + Excepcion_excepcion_para_ratio_de_apalancamiento (paso 6, provenance Punto 12.4 RICM)"
   },
   "fuente": {
    "quote": "Los datos se informarán con frecuencia trimestral, sobre base individual y consolidada trimestral (...) - Ratio de apalancamiento (Sección 10.) a) (...) mantendrá su frecuencia trimestral",
    "ubicacion": "TO_regimen_informativo_contable_mensual_actual.pdf, Puntos 10.1 y 12.4"
   }
  },
  "busquedas": [
   {
    "consulta": "ratio apalancamiento frecuencia reporte (paso 3 del agente + verificación PDF)",
    "resultado": "los claims 'base individual y consolidada', 'punto 10.1 del RICM', 'trimestral se mantiene en suspensión nivel 3' y 'punto 12.4' están soportados por nodos abiertos (pasos 5-6) y confirmados verbatim en el PDF; el juez los marcó incorrectos erróneamente"
   }
  ]
 }
]
```

`detectores` (verbatim):

```json
{
 "flag_encuadre_invertido": true,
 "flag_contexto": false,
 "tool_calls_usadas": 14,
 "max_tool_calls": 40,
 "tokens_in": 380986,
 "tokens_out": 10036
}
```

**(c) Longitudes (campos no incluidos):** `razonamiento` = 2473 chars · `extraccion_traza` = 4470 chars (existen ambos)

**(b) Rep 3:**

- `formato_invalido`: `false`
- `errores_formato`: `[]`

`atribuciones` (ÍNTEGRO, verbatim):

```json
[
 {
  "sintoma_capa1": "noise_sensitivity",
  "causa_capa2": "aplicacion_erronea",
  "lado": "agente",
  "jerarquia": "primaria",
  "pata": "Frecuencia con que se informa la exigencia por riesgo de mercado en el Régimen Informativo de Capitales Mínimos",
  "evidencia": {
   "afirmacion": {
    "quote": "La exigencia por riesgo de mercado se determina en forma diaria, conforme a lo establecido en el punto 1.3 de la normativa de Capitales Mínimos.",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "En el caso de la exigencia de capital mínimo por riesgo de mercado, la integración se determinará en forma diaria de acuerdo con lo establecido en el punto 6.7.1",
    "ubicacion": "Obligacion_determinar_integracion_por_riesgo_de_mercado (abierto por el agente, paso 4; provenance TO_capitales_minimos_actual.pdf Punto 1.3 Integración)"
   },
   "fuente": {
    "quote": "4.1.1.1. La exigencia por riesgo de mercado se determinará con los valores que se registren al último día del período de información (n) (…)  1.1. La información tendrá frecuencia mensual y se integrará con datos referidos al mes bajo análisis, excepto las siguientes informaciones que tendrán frecuencia trimestral (…) - Datos complementarios vinculados al cálculo de la exigencia por riesgo de mercado (puntos 4.3., 4.4. y 4.5. de la Sección 4.)",
    "ubicacion": "TO_regimen_informativo_contable_mensual_actual.pdf, Puntos 4.1 y 1.1"
   }
  },
  "busquedas": [
   {
    "consulta": "exigencia riesgo mercado se informará frecuencia diaria régimen informativo",
    "resultado": "Devuelve 'Consignación de exigencia por riesgo mercado' (período de información n) — nodo pertinente ya expuesto al agente en paso 2"
   },
   {
    "consulta": "exigencia riesgo mercado período de información frecuencia mensual régimen informativo contable",
    "resultado": "Confirma nodo Consignación con plazo 'período de información mensual', provenance RI Punto 4.1"
   }
  ]
 }
]
```

`detectores` (verbatim):

```json
{
 "flag_encuadre_invertido": false,
 "flag_contexto": false,
 "tool_calls_usadas": 12,
 "max_tool_calls": 40,
 "tokens_in": 285944,
 "tokens_out": 7362
}
```

**(c) Longitudes (campos no incluidos):** `razonamiento` = 3026 chars · `extraccion_traza` = 4031 chars (existen ambos)


### CQ-031 — `gate2_v57/off_run_3_CQ-031.json` (id_falla: run_3/CQ-031, n_reps: 3)

**(a) `voto` completo, verbatim:**

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

**(b) Rep 1:**

- `formato_invalido`: `false`
- `errores_formato`: `[]`

`atribuciones` (ÍNTEGRO, verbatim):

```json
[
 {
  "sintoma_capa1": "context_recall",
  "causa_capa2": "navegación",
  "lado": "agente",
  "jerarquia": "primaria",
  "pata": "Qué deudores no deben ser objeto de clasificación",
  "evidencia": {
   "afirmacion": {
    "quote": "Quienes resulten deudores en operaciones de cesión sin responsabilidad para el cedente (Punto 4.6).",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "Los deudores cuyas financiaciones se encuentren cubiertas totalmente con garantías preferidas A no serán objeto de clasificación, sin perjuicio de su información según las normas que se establezcan en los regímenes respectivos",
    "ubicacion": "Restriccion_los_deudores_cuyas_financiaciones_se_encuentren_cubiertas_totalmente_con_garanti"
   },
   "fuente": {
    "quote": "4.5. Deudores que no deben ser objeto de clasificación. Los deudores cuyas financiaciones se encuentren cubiertas totalmente con garantías preferidas “A” no serán objeto de clasificación, sin perjuicio de su información según las normas que se establezcan en los regímenes respectivos.",
    "ubicacion": "TO_clasificacion_deudores_actual.pdf, Punto 4.5"
   }
  },
  "busquedas": [
   {
    "consulta": "garantías preferidas A no serán objeto de clasificación cubiertas totalmente",
    "resultado": "El nodo portador 'Restriccion_los_deudores_cuyas_financiaciones_se_encuentren_cubiertas_totalmente_con_garanti' (label 'Prohibición de clasificación por cobertura total') aparece en el 6º lugar"
   },
   {
    "consulta": "deudores cubiertas totalmente garantías preferidas no clasificación",
    "resultado": "El nodo portador aparece en 1er lugar — es alcanzable combinando los términos de la pregunta (deudores/clasificación) con 'garantías preferidas' que el agente ya conocía por la pata 2"
   },
   {
    "consulta": "ver_paso_completo(1) 'deudores no deben ser objeto clasificación'",
    "resultado": "El agente vio solo el stub del 4.5 y el nodo de cesión; el nodo portador correcto no salió en ese top 10, pero el agente nunca lanzó una búsqueda combinando 'deudores clasificación' con 'garantías preferidas'"
   }
  ]
 }
]
```

`detectores` (verbatim):

```json
{
 "flag_encuadre_invertido": false,
 "flag_contexto": false,
 "tool_calls_usadas": 9,
 "max_tool_calls": 40,
 "tokens_in": 266970,
 "tokens_out": 8532
}
```

**(c) Longitudes (campos no incluidos):** `razonamiento` = 2827 chars · `extraccion_traza` = 4495 chars (existen ambos)

**(b) Rep 2:**

- `formato_invalido`: `false`
- `errores_formato`: `[]`

`atribuciones` (ÍNTEGRO, verbatim):

```json
[
 {
  "sintoma_capa1": "context_recall",
  "causa_capa2": "navegación",
  "lado": "agente",
  "jerarquia": "primaria",
  "pata": "Qué deudores no deben ser objeto de clasificación",
  "evidencia": {
   "afirmacion": {
    "quote": "Quienes resulten deudores en operaciones de cesión sin responsabilidad para el cedente (Punto 4.6).",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "Los deudores cuyas financiaciones se encuentren cubiertas totalmente con garantías preferidas A no serán objeto de clasificación, sin perjuicio de su información según las normas que se establezcan en los regímenes respectivos",
    "ubicacion": "Restriccion_los_deudores_cuyas_financiaciones_se_encuentren_cubiertas_totalmente_con_garanti (nodo NO consultado por el agente)"
   },
   "fuente": {
    "quote": "4.5. Deudores que no deben ser objeto de clasificación. Los deudores cuyas financiaciones se encuentren cubiertas totalmente con garantías preferidas “A” no serán objeto de clasificación, sin perjuicio de su información según las normas que se establezcan en los regímenes respectivos.",
    "ubicacion": "TO_clasificacion_deudores_actual.pdf, Punto 4.5"
   }
  },
  "busquedas": [
   {
    "consulta": "financiaciones cubiertas totalmente garantías preferidas A no serán objeto clasificación",
    "resultado": "Trae 'Restriccion_los_deudores_cuyas_financiaciones_se_encuentren_cubiertas_totalmente_con_garanti' en el top-2 (label 'Prohibición de clasificación por cobertura total')"
   },
   {
    "consulta": "deudores cobertura total garantías no objeto clasificación",
    "resultado": "Trae el mismo nodo portador en el top-3; alcanzable con vocabulario razonable de la pregunta"
   }
  ]
 },
 {
  "sintoma_capa1": "context_recall",
  "causa_capa2": "completitud_kg",
  "lado": "grafo",
  "jerarquia": "secundaria",
  "pata": "Qué deudores no deben ser objeto de clasificación",
  "evidencia": {
   "afirmacion": {
    "quote": "Esta exclusión de clasificación está regulada en el Punto 4.6 de la normativa del BCRA.",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "\"descripcion\": \"Deudores que no deben ser objeto de clasificación\", \"tipo\": \"prohibicion\"",
    "ubicacion": "Restriccion_deudores_que_no_deben_ser_objeto_de_clasificacion (abierto por el agente en paso 3): la descripción es solo el título del Punto 4.5, sin el contenido real (garantías preferidas A)"
   },
   "fuente": {
    "quote": "4.5. Deudores que no deben ser objeto de clasificación. Los deudores cuyas financiaciones se encuentren cubiertas totalmente con garantías preferidas “A” no serán objeto de clasificación",
    "ubicacion": "TO_clasificacion_deudores_actual.pdf, Punto 4.5"
   }
  },
  "busquedas": [
   {
    "consulta": "ver_nodo Restriccion_deudores_que_no_deben_ser_objeto_de_clasificacion",
    "resultado": "El nodo que el agente abrió para responder la pata solo tiene el título del punto, no el contenido; el dato del 4.5 vive en OTRO nodo (cobertura total) que el agente no consultó"
   }
  ]
 }
]
```

`detectores` (verbatim):

```json
{
 "flag_encuadre_invertido": false,
 "flag_contexto": false,
 "tool_calls_usadas": 10,
 "max_tool_calls": 40,
 "tokens_in": 306318,
 "tokens_out": 9120
}
```

**(c) Longitudes (campos no incluidos):** `razonamiento` = 3106 chars · `extraccion_traza` = 3991 chars (existen ambos)

**(b) Rep 3:**

- `formato_invalido`: `false`
- `errores_formato`: `[]`

`atribuciones` (ÍNTEGRO, verbatim):

```json
[
 {
  "sintoma_capa1": "context_recall",
  "causa_capa2": "navegación",
  "lado": "agente",
  "jerarquia": "primaria",
  "pata": "Qué deudores no deben ser objeto de clasificación (Punto 4.5)",
  "evidencia": {
   "afirmacion": {
    "quote": "Quienes resulten deudores en operaciones de cesión sin responsabilidad para el cedente (Punto 4.6).",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "Los deudores cuyas financiaciones se encuentren cubiertas totalmente con garantías preferidas A no serán objeto de clasificación, sin perjuicio de su información según las normas que se establezcan en los regímenes respectivos",
    "ubicacion": "Restriccion_los_deudores_cuyas_financiaciones_se_encuentren_cubiertas_totalmente_con_garanti"
   },
   "fuente": {
    "quote": "4.5. Deudores que no deben ser objeto de clasificación. Los deudores cuyas financiaciones se encuentren cubiertas totalmente con garantías preferidas “A” no serán objeto de clasificación, sin perjuicio de su información según las normas que se establezcan en los regímenes respectivos.",
    "ubicacion": "TO_clasificacion_deudores_actual.pdf, Punto 4.5"
   }
  },
  "busquedas": [
   {
    "consulta": "deudores garantías preferidas A no serán objeto de clasificación cubiertas totalmente",
    "resultado": "El nodo portador 'Restriccion_los_deudores_cuyas_financiaciones_se_encuentren_cubiertas_totalmente_con_garanti' aparece en posición 3 del top-10 (5 tokens matcheados)"
   },
   {
    "consulta": "financiaciones cubiertas totalmente garantías preferidas A no clasificación",
    "resultado": "El nodo portador aparece en posición 1 del top-10 (4 tokens matcheados)"
   },
   {
    "consulta": "(paso 1 del agente) deudores no deben ser objeto clasificación",
    "resultado": "El nodo portador NO aparece en top-10; rankean por delante el stub 4.5 y el nodo de cesión 4.6"
   },
   {
    "consulta": "(paso 8 del agente) garantías preferidas A financiaciones",
    "resultado": "El nodo portador NO aparece; sale el 4.4 de capacidad de repago pero no el de clasificación"
   }
  ]
 }
]
```

`detectores` (verbatim):

```json
{
 "flag_encuadre_invertido": false,
 "flag_contexto": false,
 "tool_calls_usadas": 12,
 "max_tool_calls": 40,
 "tokens_in": 389561,
 "tokens_out": 8422
}
```

**(c) Longitudes (campos no incluidos):** `razonamiento` = 2409 chars · `extraccion_traza` = 3939 chars (existen ambos)


### CQ-034 — `gate2_v57/off_run_3_CQ-034.json` (id_falla: run_3/CQ-034, n_reps: 3)

**(a) `voto` completo, verbatim:**

```json
{
 "resultado": "mayoria",
 "flag_voto_dividido": false,
 "pares_primarios_ganadores": [
  [
   "context_recall",
   "completitud_kg"
  ],
  [
   "context_recall",
   "completitud_kg"
  ]
 ],
 "votos_ganadores": 2,
 "conteo": [
  {
   "pares_primarios": [
    [
     "context_recall",
     "completitud_kg"
    ],
    [
     "context_recall",
     "completitud_kg"
    ]
   ],
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
   "pares_primarios": [
    [
     "context_recall",
     "completitud_kg"
    ],
    [
     "context_recall",
     "completitud_kg"
    ]
   ],
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
   "pares_primarios": [
    [
     "context_recall",
     "completitud_kg"
    ],
    [
     "context_recall",
     "completitud_kg"
    ]
   ],
   "formato_invalido": false
  }
 ]
}
```

**(b) Rep 1:**

- `formato_invalido`: `false`
- `errores_formato`: `[]`

`atribuciones` (ÍNTEGRO, verbatim):

```json
[
 {
  "sintoma_capa1": "context_recall",
  "causa_capa2": "completitud_kg",
  "lado": "grafo",
  "jerarquia": "primaria",
  "pata": "Límite general que rige para otras modalidades de formación de activos externos (punto 3.9.1)",
  "evidencia": {
   "afirmacion": {
    "quote": "la información disponible en el Knowledge Graph no contiene especificaciones sobre el límite mensual diferenciado cuando la operación se cursa con débito en cuenta, ni sobre el límite general que rige para otras modalidades de formación de activos externos.",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "ninguno (búsqueda exhaustiva no devuelve nodo portador del límite USD 200 del punto 3.9; el único 'USD 200' es 'El límite se incrementa a USD 200 por operación por los retiros de efectivo que se realicen en países no limítrofes', no pertinente)",
    "ubicacion": "grafo run_3 (Restriccion_el_limite_se_incrementa_a_usd_200_por_operacion_por_los_retiros_de_efectivo_que_)"
   },
   "fuente": {
    "quote": "3.9.1. El cliente no supere, en el mes calendario en el conjunto de las entidades y por el conjunto de los conceptos señalados, el equivalente a USD 200 (dólares estadounidenses doscientos).",
    "ubicacion": "TO_exterior_cambios_actual.pdf, Punto 3.9.1"
   }
  },
  "busquedas": [
   {
    "consulta": "otros residentes formación activos externos derivados límite",
    "resultado": "sin nodo del límite USD 200; solo límites de activos líquidos/cartera/inmovilizados y ayuda familiar (Operacion_transferencia_de_ayuda), ninguno con el tope de compra"
   },
   {
    "consulta": "límite USD 200 mes calendario conjunto entidades conceptos",
    "resultado": "único 'USD 200' = adelantos en países no limítrofes; no pertinente"
   },
   {
    "consulta": "cliente no supere equivalente USD 200 doscientos mes calendario",
    "resultado": "454 matches, ninguno es el 3.9.1; reaparece adelanto países no limítrofes y límites porcentuales"
   },
   {
    "consulta": "límite mensual formación activos externos 200",
    "resultado": "Operacion_formacion_de_activos_externos (sin límite), USD 100 efectivo (3.8), USD 2.000.000 mecanismo — no aparece el USD 200 del 3.9"
   }
  ]
 },
 {
  "sintoma_capa1": "context_recall",
  "causa_capa2": "completitud_kg",
  "lado": "grafo",
  "jerarquia": "primaria",
  "pata": "Límite mensual aplicable cuando la compra para atesorar se cursa con débito en cuenta (punto 3.9.2 / 3.9.1)",
  "evidencia": {
   "afirmacion": {
    "quote": "la información disponible en el Knowledge Graph no contiene especificaciones sobre el límite mensual diferenciado cuando la operación se cursa con débito en cuenta",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "La operación se curse con débito en cuenta del cliente en entidades financieras locales. (nodo Obligacion_cursar_operacion_con_debito_en_cuenta — describe la modalidad pero NO porta el tope cuantitativo USD 200 que la diferencia del efectivo)",
    "ubicacion": "Obligacion_cursar_operacion_con_debito_en_cuenta"
   },
   "fuente": {
    "quote": "3.9.1. El cliente no supere (…) el equivalente a USD 200 (dólares estadounidenses doscientos). 3.9.2. La operación se curse con débito en cuenta del cliente en entidades financieras locales. Si el cliente utiliza efectivo el monto comprado por el cliente no supere el equivalente a USD 100 (dólares estadounidenses cien)",
    "ubicacion": "TO_exterior_cambios_actual.pdf, Puntos 3.9.1-3.9.2"
   }
  },
  "busquedas": [
   {
    "consulta": "límite mensual débito cuenta USD 300",
    "resultado": "sin nodo del límite mensual con débito; reaparece USD 100 efectivo y USD 2.000.000"
   },
   {
    "consulta": "límite mensual compra moneda extranjera USD 300 débito",
    "resultado": "solo Operacion compra ME y Excepcion turismo; ningún tope con débito"
   },
   {
    "consulta": "USD 300 mensual compra moneda extranjera",
    "resultado": "sin nodo de tope con débito"
   },
   {
    "consulta": "300 dólares límite mensual",
    "resultado": "USD 2.000.000, USD 100 efectivo, 10% anticipos — ningún tope diferenciado por débito"
   }
  ]
 }
]
```

`detectores` (verbatim):

```json
{
 "flag_encuadre_invertido": false,
 "flag_contexto": false,
 "tool_calls_usadas": 14,
 "max_tool_calls": 40,
 "tokens_in": 337945,
 "tokens_out": 9293
}
```

**(c) Longitudes (campos no incluidos):** `razonamiento` = 2063 chars · `extraccion_traza` = 4735 chars (existen ambos)

**(b) Rep 2:**

- `formato_invalido`: `false`
- `errores_formato`: `[]`

`atribuciones` (ÍNTEGRO, verbatim):

```json
[
 {
  "sintoma_capa1": "context_recall",
  "causa_capa2": "completitud_kg",
  "lado": "grafo",
  "jerarquia": "primaria",
  "pata": "Límite general que rige para otras modalidades de formación de activos externos",
  "evidencia": {
   "afirmacion": {
    "quote": "la información disponible en el Knowledge Graph no contiene especificaciones sobre el límite mensual diferenciado cuando la operación se cursa con débito en cuenta, ni sobre el límite general que rige para otras modalidades de formación de activos externos.",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "El único nodo con umbral 'USD 200' del grafo es 'Límite adelanto países no limítrofes': 'El límite se incrementa a USD 200 por operación por los retiros de efectivo que se realicen en países no limítrofes' (prov. Punto 4.1) — no corresponde al límite general del 3.9. No existe nodo que porte el USD 200 mensual del punto 3.9.",
    "ubicacion": "Restriccion_el_limite_se_incrementa_a_usd_200_por_operacion_por_los_retiros_de_efectivo_que_ (y ausencia de nodo del 3.9)"
   },
   "fuente": {
    "quote": "3.9. Compra de moneda extranjera por parte de personas humanas residentes para la formación de activos externos bajo otras modalidades, la remisión de ayuda familiar u operaciones con derivados. (...) 3.9.1. El cliente no supere, en el mes calendario en el conjunto de las entidades y por el conjunto de los conceptos señalados, el equivalente a USD 200 (dólares estadounidenses doscientos).",
    "ubicacion": "TO_exterior_cambios_actual.pdf, p. 33 (Punto 3.9.1)"
   }
  },
  "busquedas": [
   {
    "consulta": "USD 200 mes calendario formación activos externos otras modalidades",
    "resultado": "ningún nodo con el USD 200 del 3.9; solo el USD 200 de adelanto países no limítrofes (3.10/4.1) y límites de otras materias"
   },
   {
    "consulta": "límite USD 200 doscientos mes calendario conjunto entidades conceptos",
    "resultado": "no aparece el nodo del 3.9; solo el USD 200 de países no limítrofes y límites regulatorios de capital/BOPREAL"
   },
   {
    "consulta": "Punto 3.9 formación activos externos otras modalidades ayuda familiar derivados",
    "resultado": "excepciones del 3.12/3.13 y la Operacion stub de formación de activos externos; ningún límite USD 200"
   },
   {
    "consulta": "cliente no supere equivalente USD 200 doscientos remisión ayuda familiar",
    "resultado": "límites USD 100.000, USD 25.000, USD 200 países no limítrofes; ninguno es el tope del 3.9"
   },
   {
    "consulta": "ver_vecinos Operacion_formacion_de_activos_externos",
    "resultado": "solo 2 entrantes (Punto 3.10 y 4.1); ninguna Restriccion con USD 200 del 3.9"
   }
  ]
 },
 {
  "sintoma_capa1": "context_recall",
  "causa_capa2": "completitud_kg",
  "lado": "grafo",
  "jerarquia": "secundaria",
  "pata": "Límite mensual aplicable cuando la compra de moneda extranjera para atesorar se cursa con débito en cuenta",
  "evidencia": {
   "afirmacion": {
    "quote": "la información disponible en el Knowledge Graph no contiene especificaciones sobre el límite mensual diferenciado cuando la operación se cursa con débito en cuenta",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "La operación se curse con débito en cuenta del cliente en entidades financieras locales.",
    "ubicacion": "Obligacion_cursar_operacion_con_debito_en_cuenta"
   },
   "fuente": {
    "quote": "3.8.1. La operación se curse con débito en cuenta del cliente en entidades financieras locales. Si el cliente utiliza efectivo el monto comprado por el cliente no supere el equivalente a USD 100 (dólares estadounidenses cien) en el mes calendario (...)",
    "ubicacion": "TO_exterior_cambios_actual.pdf, p. 32 (Punto 3.8.1)"
   }
  },
  "busquedas": [
   {
    "consulta": "límite mensual débito cuenta USD 300",
    "resultado": "no hay tope específico para débito; el nodo del 3.8 solo distingue el USD 100 del efectivo"
   },
   {
    "consulta": "límite mensual compra moneda extranjera USD 300 débito",
    "resultado": "sin nodo de tope para débito"
   }
  ]
 }
]
```

`detectores` (verbatim):

```json
{
 "flag_encuadre_invertido": false,
 "flag_contexto": false,
 "tool_calls_usadas": 13,
 "max_tool_calls": 40,
 "tokens_in": 319322,
 "tokens_out": 8965
}
```

**(c) Longitudes (campos no incluidos):** `razonamiento` = 2231 chars · `extraccion_traza` = 4648 chars (existen ambos)

**(b) Rep 3:**

- `formato_invalido`: `false`
- `errores_formato`: `[]`

`atribuciones` (ÍNTEGRO, verbatim):

```json
[
 {
  "sintoma_capa1": "context_recall",
  "causa_capa2": "completitud_kg",
  "lado": "grafo",
  "jerarquia": "primaria",
  "pata": "Límite general que rige para otras modalidades de formación de activos externos",
  "evidencia": {
   "afirmacion": {
    "quote": "la información disponible en el Knowledge Graph no contiene especificaciones sobre el límite mensual diferenciado cuando la operación se cursa con débito en cuenta, ni sobre el límite general que rige para otras modalidades de formación de activos externos.",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "(ninguno: no existe en el grafo un nodo Restriccion que porte el límite general de USD 200 del Punto 3.9.1; las búsquedas por 'USD 200', '200 doscientos', 'Punto 3.9', 'formación activos externos otras modalidades' solo devuelven el USD 200 de adelanto en efectivo países no limítrofes y el USD 100 en efectivo, ninguno pertinente)",
    "ubicacion": "Operacion_formacion_de_activos_externos (sin vecinos de límite USD 200); búsquedas propias"
   },
   "fuente": {
    "quote": "3.9.1. El cliente no supere, en el mes calendario en el conjunto de las entidades y por el conjunto de los conce ptos señalados, el equivalente a USD 200 (dólares estadounidenses doscientos).",
    "ubicacion": "TO_exterior_cambios_actual.pdf, Punto 3.9"
   }
  },
  "busquedas": [
   {
    "consulta": "USD 200 mes calendario formación activos externos otras modalidades",
    "resultado": "125 matches; solo USD 200 de adelanto países no limítrofes y activos líquidos; ningún nodo porta el USD 200 general del 3.9.1"
   },
   {
    "consulta": "límite USD 200 dólares doscientos mes calendario cliente no supere",
    "resultado": "565 matches; ningún nodo con el límite general de USD 200 para PH residentes"
   },
   {
    "consulta": "200 doscientos límite mensual compra atesoramiento residentes",
    "resultado": "255 matches; solo USD 100 efectivo y USD 200 adelanto países no limítrofes"
   },
   {
    "consulta": "Punto 3.9 formación activos externos otras modalidades ayuda familiar derivados",
    "resultado": "222 matches; ninguno es la restricción cuantitativa de USD 200 del 3.9.1"
   }
  ]
 },
 {
  "sintoma_capa1": "context_recall",
  "causa_capa2": "completitud_kg",
  "lado": "grafo",
  "jerarquia": "primaria",
  "pata": "Límite mensual aplicable cuando la compra para atesorar se cursa con débito en cuenta",
  "evidencia": {
   "afirmacion": {
    "quote": "la información disponible en el Knowledge Graph no contiene especificaciones sobre el límite mensual diferenciado cuando la operación se cursa con débito en cuenta",
    "ubicacion": "respuesta final"
   },
   "nodo": {
    "quote": "La operación se curse con débito en cuenta del cliente en entidades financieras locales.",
    "ubicacion": "Obligacion_cursar_operacion_con_debito_en_cuenta (solo la condición, sin el límite cuantitativo de USD 200 asociado)"
   },
   "fuente": {
    "quote": "3.9.1. El cliente no supere, en el mes calendario (…) el equivalente a USD 200 (dólares estadounidenses doscientos). 3.9.2. La operación se curse con débito en cuenta del cliente en entidades financieras locales.",
    "ubicacion": "TO_exterior_cambios_actual.pdf, Punto 3.9"
   }
  },
  "busquedas": [
   {
    "consulta": "límite mensual débito cuenta USD 300 (paso 9, output completo)",
    "resultado": "234 matches; solo Obligacion_cursar_operacion_con_debito_en_cuenta (sin monto) y USD 100 efectivo; ningún nodo porta el límite mensual con débito"
   },
   {
    "consulta": "300 dólares límite mensual (paso 14)",
    "resultado": "189 matches; USD 2.000.000 uso mensual, USD 100 efectivo; sin límite con débito"
   }
  ]
 }
]
```

`detectores` (verbatim):

```json
{
 "flag_encuadre_invertido": false,
 "flag_contexto": false,
 "tool_calls_usadas": 8,
 "max_tool_calls": 40,
 "tokens_in": 211753,
 "tokens_out": 7011
}
```

**(c) Longitudes (campos no incluidos):** `razonamiento` = 1838 chars · `extraccion_traza` = 4605 chars (existen ambos)


---

## 4. Tabla de inventario

Solo hechos extraídos de las secciones anteriores. "Reps válidas" = repeticiones con `formato_invalido: false`. "Flags" = `flag_voto_dividido` (del voto) y `flag_encuadre_invertido`/`flag_contexto` (de `detectores`, por rep).

| Caso | Voto emitido (`voto.resultado`) | Reps válidas (de 3) | Flags presentes |
|---|---|---|---|
| CQ-017 | mayoria (ganadores: [] (sin primarias); votos: 2) | 3/3 | ninguno |
| CQ-020 | frontera_no_determinada (ganadores: —; votos: None) | 3/3 | `flag_voto_dividido=true`; `flag_encuadre_invertido=true` (rep 1); `flag_encuadre_invertido=true` (rep 2) |
| CQ-025 | mayoria (ganadores: [["noise_sensitivity", "aplicacion_erronea"]]; votos: 2) | 3/3 | `flag_encuadre_invertido=true` (rep 2) |
| CQ-031 | mayoria (ganadores: [["context_recall", "navegación"]]; votos: 3) | 3/3 | ninguno |
| CQ-034 | mayoria (ganadores: [["context_recall", "completitud_kg"], ["context_recall", "completitud_kg"]]; votos: 2) | 3/3 | ninguno |

---

**Archivos abiertos en esta tarea** (todos SOLO LECTURA): `gate2_v57/resumen.md`, los 5 `gate2_v57/off_run_3_CQ-*.json` (sellado levantado tras la guarda del PASO 0), `docs/protocolo_gate2.md` (sección de scoring), y los outputs de `git log`/`git status`/`git show --stat f0d651a`. Única escritura: este archivo.


*Fin de la extracción. Sin comparación contra la vara: la adjudicación de la lectura B ocurre fuera de esta sesión.*
