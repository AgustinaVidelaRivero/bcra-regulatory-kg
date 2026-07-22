# Extracción del head-to-head del ciclo 2 — gate CQN2 (mecánica, CERO scoring)

Fecha: 2026-07-19. Corrida ÚNICA del LLM (verificador v5.7 congelado, `--n 3`,
namespaces `cv=verificador-v5.7-rep{1..3}`) sobre los 11 casos del gate CQN2, input
por caso desde `posthoc_run/traces/gate_cqn2/run_3/`. TRES COLUMNAS del mismo run:
(A) v6.1-D (`capa_deterministica.py` congelada) → `_capa_d`; (B) v6.2-D
(`capa_deterministica_v62.py`) → `_capa_d62`; (C) v7' = S1 v0.4b
(`s1_fuentes_v04.py`, `--n 3`, política conservadora, guarda de dominio por
`tos_fuente` del sellado CQN2) sobre los `_capa_d62` → `_s1v04b_n3`. Las capas son
post-procesamiento determinístico (CERO llamadas LLM); S1 solo llama al LLM en
atribuciones gatilladas con fetch utilizable (tokens por caso abajo). **La vara
(`docs/casos_gate_cqn2.md`) NO entró a ningún contexto de esta corrida ni de esta
extracción — el scoring es externo.**

**Nota de cableado** (idéntica al head-to-head anterior): la whitelist del CLI del
verificador (labels `off|on`, `_parse_casos`) rechaza `gate_cqn2`; la corrida usó un
driver que replica VERBATIM el loop del runner de `main()` en su rama `--n>1`
(`investigar_falla` + `agregar_voto`, namespaces intactos). El instrumento no se tocó
(hashes en el sello).


---

## CQN2-002

**Costo verificador (3 reps):** in 270.069 / 452.312 / 341.854 = **1.064.235** · out 8.004 / 18.526 / 9.909 = **36.439**

**Voto LLM crudo (pre-capa):** **frontera_no_determinada** (dividido) — conteo: [['noise_sensitivity', 'contenido_kg']]×1 / [['context_recall', 'completitud_kg']]×1 / [['noise_sensitivity', 'contenido_kg'], ['noise_sensitivity', 'contenido_kg']]×1
  - desglose por rep: rep1=[['noise_sensitivity', 'contenido_kg']] · rep2=[['context_recall', 'completitud_kg']] · rep3=[['noise_sensitivity', 'contenido_kg'], ['noise_sensitivity', 'contenido_kg']]

### Columna A — v6.1-D (`v6.1-D(2026-07)`)

- voto_capa_d: **frontera_no_determinada** (dividido) — conteo: [['context_recall', 'completitud_kg']]×1 / [['noise_sensitivity', 'contenido_kg']]×1 / [['noise_sensitivity', 'contenido_kg'], ['noise_sensitivity', 'contenido_kg']]×1
- triage: **TRIAGE** motivos=["atribucion_no_verificable", "voto_dividido"] · flags: R6b: rep 1 atrib 1 — claim_no_mapeado | R6b: rep 2 atrib 1 — context_recall_sin_pata | R6b: rep 3 atrib 1 — claim_no_mapeado | R6b: rep 3 atrib 2 — claim_no_mapeado | R4: voto_capa_d.flag_voto_dividido = true
- resumen D2: corregidas=0 · discrepancias=0 · triage_R3=0 · reps_tocadas=[]
- secundarias emitidas: {noise_sensitivity, provenance_imprecisa} (secundaria) ×2; {noise_sensitivity, contenido_kg} (secundaria) ×1

### Columna B — v6.2-D (`v6.2-D(2026-07)`)

- voto_capa_d: **frontera_no_determinada** (dividido) — conteo: [['context_recall', 'completitud_kg']]×1 / [['noise_sensitivity', 'contenido_kg']]×1 / [['noise_sensitivity', 'contenido_kg'], ['noise_sensitivity', 'contenido_kg']]×1
- triage: **TRIAGE** motivos=["atribucion_no_verificable", "voto_dividido"] · flags: R6b: rep 1 atrib 1 — claim_no_mapeado | R6b: rep 2 atrib 1 — context_recall_sin_pata | R6b: rep 3 atrib 1 — claim_no_mapeado | R6b: rep 3 atrib 2 — claim_no_mapeado | R4: voto_capa_d.flag_voto_dividido = true
- resumen D2': corregidas=0 · discrepancias=0 · triage_R3=0 · punteros_estructurales_extraidos=2 · decisiones_con_puntero=0
- anotaciones D7: (ninguna decisión por puntero)
- secundarias emitidas: {noise_sensitivity, provenance_imprecisa} (secundaria) ×2; {noise_sensitivity, contenido_kg} (secundaria) ×1

### Columna C — v7' = v6.2-D + S1 v0.4b (`s1-v0.4b-dev`)

- voto_s1: **frontera_no_determinada** (dividido) — conteo: [['context_recall', 'completitud_kg']]×1 / [['faithfulness', 'contenido_kg'], ['noise_sensitivity', 'contenido_kg']]×1 / [['noise_sensitivity', 'contenido_kg']]×1
- triage_s1: **TRIAGE** motivos=["fuente_cross_doc"] · flags: S1: rep1_atrib1 — fuente_cross_doc (TO_regimen_informativo_contable_mensual_actual.pdf ∉ territorio) | S1: rep2_atrib1 — fuente_cross_doc (TO_capitales_minimos_actual.pdf ∉ territorio) | S1: rep2_atrib2 — fuente_cross_doc (TO_regimen_informativo_contable_mensual_actual.pdf ∉ territorio) | S1: rep3_atrib2 — fuente_cross_doc (TO_regimen_informativo_contable_mensual_actual.pdf ∉ territorio)
- resumen S1: gatilladas=5 · juzgadas_llm=1 · corregidas=1 · no_determinable=0 · fetch_fallido=0 · cross_doc_bloqueadas=4 · fuente_no_funda=0 · exoneracion_con_sintoma=False
- **Costo S1:** 9.924 in / 1.454 out
- estados de fetch por atribución: 
    - rep1_atrib1: estado_fetch=fuente_cross_doc · accion=fuente_cross_doc · corrigio=False · triage=True · guarda_dominio: portador de TO_regimen_informativo_contable_mensual_actual.pdf ∉ territorio ['TO_clasificacion_deudores_actual.pdf']
    - rep2_atrib1: estado_fetch=fuente_cross_doc · accion=fuente_cross_doc · corrigio=False · triage=True · guarda_dominio: portador de TO_capitales_minimos_actual.pdf ∉ territorio ['TO_clasificacion_deudores_actual.pdf']
    - rep2_atrib2: estado_fetch=fuente_cross_doc · accion=fuente_cross_doc · corrigio=False · triage=True · guarda_dominio: portador de TO_regimen_informativo_contable_mensual_actual.pdf ∉ territorio ['TO_clasificacion_deudores_actual.pdf']
    - rep3_atrib1: estado_fetch=completo · accion=None · corrigio=True · triage=False · voto_s1_atrib={"n": 3, "umbral": 2, "esquema": "causa", "decididas": 3, "no_decididas": 0, "resultado": "mayoria", "sintoma_ganador": "faithfulness", "causa_ganadora": "contenido_kg", "votos_ganadores": 3}
    - rep3_atrib2: estado_fetch=fuente_cross_doc · accion=fuente_cross_doc · corrigio=False · triage=True · guarda_dominio: portador de TO_regimen_informativo_contable_mensual_actual.pdf ∉ territorio ['TO_clasificacion_deudores_actual.pdf']
- secundarias emitidas: {noise_sensitivity, provenance_imprecisa} (secundaria) ×2; {noise_sensitivity, contenido_kg} (secundaria) ×1

---

## CQN2-004

**Costo verificador (3 reps):** in 273.344 / 360.874 / 236.601 = **870.819** · out 8.759 / 9.176 / 9.075 = **27.010**

**Voto LLM crudo (pre-capa):** **mayoría 2** ganadores=[['noise_sensitivity', 'contenido_kg']] · conteo: [['noise_sensitivity', 'contenido_kg']]×2 / [['noise_sensitivity', 'contenido_kg'], ['noise_sensitivity', 'contenido_kg']]×1
  - desglose por rep: rep1=[['noise_sensitivity', 'contenido_kg'], ['noise_sensitivity', 'contenido_kg']] · rep2=[['noise_sensitivity', 'contenido_kg']] · rep3=[['noise_sensitivity', 'contenido_kg']]

### Columna A — v6.1-D (`v6.1-D(2026-07)`)

- voto_capa_d: **mayoría 2** ganadores=[['noise_sensitivity', 'contenido_kg']] · conteo: [['noise_sensitivity', 'contenido_kg']]×2 / [['noise_sensitivity', 'contenido_kg'], ['noise_sensitivity', 'contenido_kg']]×1
- triage: **TRIAGE** motivos=["atribucion_no_verificable"] · flags: R6b: rep 1 atrib 1 — claim_no_mapeado | R6b: rep 1 atrib 2 — claim_no_mapeado | R6b: rep 2 atrib 1 — claim_no_mapeado | R6b: rep 3 atrib 1 — claim_no_mapeado
- resumen D2: corregidas=0 · discrepancias=0 · triage_R3=0 · reps_tocadas=[]
- secundarias emitidas: {noise_sensitivity, sin_defecto} (sin_par) ×5

### Columna B — v6.2-D (`v6.2-D(2026-07)`)

- voto_capa_d: **mayoría 2** ganadores=[['noise_sensitivity', 'contenido_kg']] · conteo: [['noise_sensitivity', 'contenido_kg']]×2 / [['noise_sensitivity', 'contenido_kg'], ['noise_sensitivity', 'contenido_kg']]×1
- triage: **TRIAGE** motivos=["atribucion_no_verificable"] · flags: R6b: rep 1 atrib 1 — claim_no_mapeado | R6b: rep 1 atrib 2 — claim_no_mapeado | R6b: rep 2 atrib 1 — claim_no_mapeado | R6b: rep 3 atrib 1 — claim_no_mapeado
- resumen D2': corregidas=0 · discrepancias=0 · triage_R3=0 · punteros_estructurales_extraidos=3 · decisiones_con_puntero=0
- anotaciones D7: (ninguna decisión por puntero)
- secundarias emitidas: {noise_sensitivity, sin_defecto} (sin_par) ×5

### Columna C — v7' = v6.2-D + S1 v0.4b (`s1-v0.4b-dev`)

- voto_s1: **mayoría 2** ganadores=[['noise_sensitivity', 'contenido_kg']] · conteo: [['noise_sensitivity', 'contenido_kg']]×2 / [['noise_sensitivity', 'contenido_kg'], ['noise_sensitivity', 'contenido_kg']]×1
- triage_s1: **TRIAGE** motivos=["fuente_no_funda", "fuente_cross_doc"] · flags: S1: rep1_atrib1 — fuente_no_funda (span máx 0) | S1: rep1_atrib2 — fuente_cross_doc (TO_regimen_informativo_contable_mensual_actual.pdf ∉ territorio) | S1: rep2_atrib1 — fuente_cross_doc (TO_regimen_informativo_contable_mensual_actual.pdf ∉ territorio) | S1: rep3_atrib1 — fuente_cross_doc (TO_regimen_informativo_contable_mensual_actual.pdf ∉ territorio)
- resumen S1: gatilladas=4 · juzgadas_llm=0 · corregidas=0 · no_determinable=0 · fetch_fallido=0 · cross_doc_bloqueadas=3 · fuente_no_funda=1 · exoneracion_con_sintoma=False
- **Costo S1:** 0 in / 0 out (cero llamadas LLM)
- estados de fetch por atribución: 
    - rep1_atrib1: estado_fetch=fuente_no_funda · accion=fuente_no_funda · corrigio=False · triage=True · fundamento: span_max=0 (umbral 60)
    - rep1_atrib2: estado_fetch=fuente_cross_doc · accion=fuente_cross_doc · corrigio=False · triage=True · guarda_dominio: portador de TO_regimen_informativo_contable_mensual_actual.pdf ∉ territorio ['TO_capitales_minimos_actual.pdf']
    - rep2_atrib1: estado_fetch=fuente_cross_doc · accion=fuente_cross_doc · corrigio=False · triage=True · guarda_dominio: portador de TO_regimen_informativo_contable_mensual_actual.pdf ∉ territorio ['TO_capitales_minimos_actual.pdf']
    - rep3_atrib1: estado_fetch=fuente_cross_doc · accion=fuente_cross_doc · corrigio=False · triage=True · guarda_dominio: portador de TO_regimen_informativo_contable_mensual_actual.pdf ∉ territorio ['TO_capitales_minimos_actual.pdf']
- secundarias emitidas: {noise_sensitivity, sin_defecto} (sin_par) ×5

---

## CQN2-005

**Costo verificador (3 reps):** in 245.036 / 252.323 / 238.752 = **736.111** · out 7.853 / 7.946 / 7.283 = **23.082**

**Voto LLM crudo (pre-capa):** **mayoría 3** ganadores=[['context_recall', 'alcanzabilidad_kg']] · conteo: [['context_recall', 'alcanzabilidad_kg']]×3
  - desglose por rep: rep1=[['context_recall', 'alcanzabilidad_kg']] · rep2=[['context_recall', 'alcanzabilidad_kg']] · rep3=[['context_recall', 'alcanzabilidad_kg']]

### Columna A — v6.1-D (`v6.1-D(2026-07)`)

- voto_capa_d: **mayoría 3** ganadores=[['context_recall', 'alcanzabilidad_kg']] · conteo: [['context_recall', 'alcanzabilidad_kg']]×3
- triage: sin triage
- resumen D2: corregidas=3 · discrepancias=0 · triage_R3=0 · reps_tocadas=[1, 2, 3]
- secundarias emitidas: (ninguna)

### Columna B — v6.2-D (`v6.2-D(2026-07)`)

- voto_capa_d: **mayoría 3** ganadores=[['context_recall', 'alcanzabilidad_kg']] · conteo: [['context_recall', 'alcanzabilidad_kg']]×3
- triage: sin triage
- resumen D2': corregidas=3 · discrepancias=0 · triage_R3=0 · punteros_estructurales_extraidos=1 · decisiones_con_puntero=0
- anotaciones D7: (ninguna decisión por puntero)
- secundarias emitidas: (ninguna)

### Columna C — v7' = v6.2-D + S1 v0.4b (`s1-v0.4b-dev`)

- voto_s1: **mayoría 3** ganadores=[['context_recall', 'alcanzabilidad_kg']] · conteo: [['context_recall', 'alcanzabilidad_kg']]×3
- triage_s1: sin triage
- resumen S1: gatilladas=0 · juzgadas_llm=0 · corregidas=0 · no_determinable=0 · fetch_fallido=0 · cross_doc_bloqueadas=0 · fuente_no_funda=0 · exoneracion_con_sintoma=False
- **Costo S1:** 0 in / 0 out (cero llamadas LLM)
- estados de fetch por atribución: (ninguna atribución gatillada)
- secundarias emitidas: (ninguna)

---

## CQN2-006

**Costo verificador (3 reps):** in 239.011 / 182.917 / 283.426 = **705.354** · out 6.073 / 5.512 / 6.267 = **17.852**

**Voto LLM crudo (pre-capa):** **mayoría 3** ganadores=[['context_recall', 'completitud_kg']] · conteo: [['context_recall', 'completitud_kg']]×3
  - desglose por rep: rep1=[['context_recall', 'completitud_kg']] · rep2=[['context_recall', 'completitud_kg']] · rep3=[['context_recall', 'completitud_kg']]

### Columna A — v6.1-D (`v6.1-D(2026-07)`)

- voto_capa_d: **mayoría 3** ganadores=[['context_recall', 'completitud_kg']] · conteo: [['context_recall', 'completitud_kg']]×3
- triage: sin triage
- resumen D2: corregidas=0 · discrepancias=0 · triage_R3=0 · reps_tocadas=[]
- secundarias emitidas: (ninguna)

### Columna B — v6.2-D (`v6.2-D(2026-07)`)

- voto_capa_d: **mayoría 3** ganadores=[['context_recall', 'completitud_kg']] · conteo: [['context_recall', 'completitud_kg']]×3
- triage: sin triage
- resumen D2': corregidas=0 · discrepancias=0 · triage_R3=0 · punteros_estructurales_extraidos=4 · decisiones_con_puntero=0
- anotaciones D7: (ninguna decisión por puntero)
- secundarias emitidas: (ninguna)

### Columna C — v7' = v6.2-D + S1 v0.4b (`s1-v0.4b-dev`)

- voto_s1: **mayoría 3** ganadores=[['context_recall', 'completitud_kg']] · conteo: [['context_recall', 'completitud_kg']]×3
- triage_s1: **TRIAGE** motivos=["fuente_no_funda"] · flags: S1: rep1_atrib1 — fuente_no_funda (span máx 0) | S1: rep2_atrib1 — fuente_no_funda (span máx 0) | S1: rep3_atrib1 — fuente_no_funda (span máx 0)
- resumen S1: gatilladas=3 · juzgadas_llm=0 · corregidas=0 · no_determinable=0 · fetch_fallido=0 · cross_doc_bloqueadas=0 · fuente_no_funda=3 · exoneracion_con_sintoma=False
- **Costo S1:** 0 in / 0 out (cero llamadas LLM)
- estados de fetch por atribución: 
    - rep1_atrib1: estado_fetch=fuente_no_funda · accion=fuente_no_funda · corrigio=False · triage=True · fundamento: span_max=0 (umbral 60)
    - rep2_atrib1: estado_fetch=fuente_no_funda · accion=fuente_no_funda · corrigio=False · triage=True · fundamento: span_max=0 (umbral 60)
    - rep3_atrib1: estado_fetch=fuente_no_funda · accion=fuente_no_funda · corrigio=False · triage=True · fundamento: span_max=0 (umbral 60)
- secundarias emitidas: (ninguna)

---

## CQN2-007

**Costo verificador (3 reps):** in 180.070 / 176.306 / 144.811 = **501.187** · out 6.442 / 6.546 / 6.211 = **19.199**

**Voto LLM crudo (pre-capa):** **mayoría 3** ganadores=[] · conteo: []×3
  - desglose por rep: rep1=[] · rep2=[] · rep3=[]

### Columna A — v6.1-D (`v6.1-D(2026-07)`)

- voto_capa_d: **mayoría 3** ganadores=[] · conteo: []×3
- triage: **TRIAGE** motivos=["exoneracion_total"] · flags: R1: voto_capa_d con mayoria de clave vacia (3 votos sin primarias)
- resumen D2: corregidas=0 · discrepancias=0 · triage_R3=0 · reps_tocadas=[]
- secundarias emitidas: {noise_sensitivity, sin_defecto} (sin_par) ×3; {noise_sensitivity, provenance_imprecisa} (secundaria) ×3

### Columna B — v6.2-D (`v6.2-D(2026-07)`)

- voto_capa_d: **mayoría 3** ganadores=[] · conteo: []×3
- triage: **TRIAGE** motivos=["exoneracion_total"] · flags: R1: voto_capa_d con mayoria de clave vacia (3 votos sin primarias)
- resumen D2': corregidas=0 · discrepancias=0 · triage_R3=0 · punteros_estructurales_extraidos=3 · decisiones_con_puntero=0
- anotaciones D7: (ninguna decisión por puntero)
- secundarias emitidas: {noise_sensitivity, sin_defecto} (sin_par) ×3; {noise_sensitivity, provenance_imprecisa} (secundaria) ×3

### Columna C — v7' = v6.2-D + S1 v0.4b (`s1-v0.4b-dev`)

- voto_s1: **mayoría 3** ganadores=[] · conteo: []×3
- triage_s1: sin triage
- resumen S1: gatilladas=3 · juzgadas_llm=3 · corregidas=0 · no_determinable=0 · fetch_fallido=0 · cross_doc_bloqueadas=0 · fuente_no_funda=0 · exoneracion_con_sintoma=True
- **Costo S1:** 33.873 in / 2.432 out
- estados de fetch por atribución: 
    - rep1_atrib1: estado_fetch=completo · accion=None · corrigio=False · triage=False · voto_s1_atrib={"n": 3, "umbral": 2, "esquema": "exoneracion", "decididas": 3, "no_decididas": 0, "resultado": "mayoria", "sintoma_ganador": null, "causa_ganadora": "sin_defecto", "votos_ganadores": 3}
    - rep2_atrib1: estado_fetch=completo · accion=None · corrigio=False · triage=False · voto_s1_atrib={"n": 3, "umbral": 2, "esquema": "exoneracion", "decididas": 3, "no_decididas": 0, "resultado": "mayoria", "sintoma_ganador": null, "causa_ganadora": "sin_defecto", "votos_ganadores": 3}
    - rep3_atrib1: estado_fetch=completo · accion=None · corrigio=False · triage=False · voto_s1_atrib={"n": 3, "umbral": 2, "esquema": "exoneracion", "decididas": 3, "no_decididas": 0, "resultado": "mayoria", "sintoma_ganador": null, "causa_ganadora": "sin_defecto", "votos_ganadores": 3}
- secundarias emitidas: {noise_sensitivity, sin_defecto} (sin_par) ×3; {noise_sensitivity, provenance_imprecisa} (secundaria) ×3

---

## CQN2-010

**Costo verificador (3 reps):** in 313.329 / 385.859 / 321.597 = **1.020.785** · out 7.804 / 8.202 / 7.459 = **23.465**

**Voto LLM crudo (pre-capa):** **mayoría 3** ganadores=[['context_recall', 'completitud_kg'], ['context_recall', 'completitud_kg']] · conteo: [['context_recall', 'completitud_kg'], ['context_recall', 'completitud_kg']]×3
  - desglose por rep: rep1=[['context_recall', 'completitud_kg'], ['context_recall', 'completitud_kg']] · rep2=[['context_recall', 'completitud_kg'], ['context_recall', 'completitud_kg']] · rep3=[['context_recall', 'completitud_kg'], ['context_recall', 'completitud_kg']]

### Columna A — v6.1-D (`v6.1-D(2026-07)`)

- voto_capa_d: **mayoría 3** ganadores=[['context_recall', 'completitud_kg'], ['context_recall', 'completitud_kg']] · conteo: [['context_recall', 'completitud_kg'], ['context_recall', 'completitud_kg']]×3
- triage: sin triage
- resumen D2: corregidas=0 · discrepancias=0 · triage_R3=0 · reps_tocadas=[]
- secundarias emitidas: (ninguna)

### Columna B — v6.2-D (`v6.2-D(2026-07)`)

- voto_capa_d: **mayoría 3** ganadores=[['context_recall', 'completitud_kg'], ['context_recall', 'completitud_kg']] · conteo: [['context_recall', 'completitud_kg'], ['context_recall', 'completitud_kg']]×3
- triage: sin triage
- resumen D2': corregidas=0 · discrepancias=0 · triage_R3=0 · punteros_estructurales_extraidos=46 · decisiones_con_puntero=0
- anotaciones D7: (ninguna decisión por puntero)
- secundarias emitidas: (ninguna)

### Columna C — v7' = v6.2-D + S1 v0.4b (`s1-v0.4b-dev`)

- voto_s1: **mayoría 3** ganadores=[['context_recall', 'completitud_kg'], ['context_recall', 'completitud_kg']] · conteo: [['context_recall', 'completitud_kg'], ['context_recall', 'completitud_kg']]×3
- triage_s1: **TRIAGE** motivos=["fuente_no_verificable", "fuente_no_funda"] · flags: S1: rep1_atrib2 — fetch sin_portador_extraible | S1: rep2_atrib1 — fetch sin_portador_extraible | S1: rep2_atrib2 — fuente_no_funda (span máx 0) | S1: rep3_atrib1 — fetch sin_portador_extraible | S1: rep3_atrib2 — fuente_no_funda (span máx 0)
- resumen S1: gatilladas=6 · juzgadas_llm=1 · corregidas=0 · no_determinable=0 · fetch_fallido=3 · cross_doc_bloqueadas=0 · fuente_no_funda=2 · exoneracion_con_sintoma=False
- **Costo S1:** 12.786 in / 1.569 out
- estados de fetch por atribución: 
    - rep1_atrib1: estado_fetch=completo · accion=None · corrigio=False · triage=False · voto_s1_atrib={"n": 3, "umbral": 2, "esquema": "causa", "decididas": 3, "no_decididas": 0, "resultado": "mayoria", "sintoma_ganador": "context_recall", "causa_ganadora": "completitud_kg", "votos_ganadores": 3}
    - rep1_atrib2: estado_fetch=sin_portador_extraible · accion=fuente_no_verificable · corrigio=False · triage=True
    - rep2_atrib1: estado_fetch=sin_portador_extraible · accion=fuente_no_verificable · corrigio=False · triage=True
    - rep2_atrib2: estado_fetch=fuente_no_funda · accion=fuente_no_funda · corrigio=False · triage=True · fundamento: span_max=0 (umbral 60)
    - rep3_atrib1: estado_fetch=sin_portador_extraible · accion=fuente_no_verificable · corrigio=False · triage=True
    - rep3_atrib2: estado_fetch=fuente_no_funda · accion=fuente_no_funda · corrigio=False · triage=True · fundamento: span_max=0 (umbral 60)
- secundarias emitidas: (ninguna)

---

## CQN2-011

**Costo verificador (3 reps):** in 333.735 / 273.949 / 333.914 = **941.598** · out 9.126 / 10.315 / 10.454 = **29.895**

**Voto LLM crudo (pre-capa):** **frontera_no_determinada** (dividido) — conteo: [['context_recall', 'navegación'], ['context_recall', 'navegación']]×1 / [['context_recall', 'navegación'], ['context_recall', 'navegación'], ['noise_sensitivity', 'aplicacion_erronea'], ['noise_sensitivity', 'contenido_kg']]×1 / [['context_recall', 'navegación'], ['context_recall', 'navegación'], ['noise_sensitivity', 'contenido_kg']]×1
  - desglose por rep: rep1=[['context_recall', 'navegación'], ['context_recall', 'navegación']] · rep2=[['context_recall', 'navegación'], ['context_recall', 'navegación'], ['noise_sensitivity', 'aplicacion_erronea'], ['noise_sensitivity', 'contenido_kg']] · rep3=[['context_recall', 'navegación'], ['context_recall', 'navegación'], ['noise_sensitivity', 'contenido_kg']]

### Columna A — v6.1-D (`v6.1-D(2026-07)`)

- voto_capa_d: **frontera_no_determinada** (dividido) — conteo: [['context_recall', 'alcanzabilidad_kg'], ['context_recall', 'navegación']]×1 / [['context_recall', 'alcanzabilidad_kg'], ['context_recall', 'navegación'], ['noise_sensitivity', 'aplicacion_erronea'], ['noise_sensitivity', 'contenido_kg']]×1 / [['context_recall', 'alcanzabilidad_kg'], ['context_recall', 'navegación'], ['noise_sensitivity', 'contenido_kg']]×1
- triage: **TRIAGE** motivos=["modulo_deterministico_sin_decision", "atribucion_no_verificable", "aplicacion_erronea_bajo_revision", "voto_dividido"] · flags: R3: rep 1 atrib 1 — D2/sin_portador_extraible | R6b: rep 2 atrib 3 — claim_no_mapeado | R2: rep 2 atrib 4 (primaria) causa aplicacion_erronea | R3: rep 3 atrib 1 — D2/sin_portador_extraible | R6b: rep 3 atrib 2 — claim_no_mapeado | R2: rep 3 atrib 4 (secundaria) causa aplicacion_erronea | R4: voto_capa_d.flag_voto_dividido = true
- resumen D2: corregidas=4 · discrepancias=3 · triage_R3=2 · reps_tocadas=[1, 2, 3]
- secundarias emitidas: {noise_sensitivity, contenido_kg} (secundaria) ×1; {noise_sensitivity, aplicacion_erronea} (secundaria) ×1

### Columna B — v6.2-D (`v6.2-D(2026-07)`)

- voto_capa_d: **frontera_no_determinada** (dividido) — conteo: [['context_recall', 'alcanzabilidad_kg'], ['context_recall', 'navegación']]×1 / [['context_recall', 'alcanzabilidad_kg'], ['context_recall', 'navegación'], ['noise_sensitivity', 'aplicacion_erronea'], ['noise_sensitivity', 'contenido_kg']]×1 / [['context_recall', 'alcanzabilidad_kg'], ['context_recall', 'navegación'], ['noise_sensitivity', 'contenido_kg']]×1
- triage: **TRIAGE** motivos=["modulo_deterministico_sin_decision", "atribucion_no_verificable", "aplicacion_erronea_bajo_revision", "voto_dividido"] · flags: R3: rep 1 atrib 1 — D2/sin_portador_extraible | R6b: rep 2 atrib 3 — claim_no_mapeado | R2: rep 2 atrib 4 (primaria) causa aplicacion_erronea | R3: rep 3 atrib 1 — D2/sin_portador_extraible | R6b: rep 3 atrib 2 — claim_no_mapeado | R2: rep 3 atrib 4 (secundaria) causa aplicacion_erronea | R4: voto_capa_d.flag_voto_dividido = true
- resumen D2': corregidas=4 · discrepancias=3 · triage_R3=2 · punteros_estructurales_extraidos=4 · decisiones_con_puntero=0
- anotaciones D7: (ninguna decisión por puntero)
- secundarias emitidas: {noise_sensitivity, contenido_kg} (secundaria) ×1; {noise_sensitivity, aplicacion_erronea} (secundaria) ×1

### Columna C — v7' = v6.2-D + S1 v0.4b (`s1-v0.4b-dev`)

- voto_s1: **frontera_no_determinada** (dividido) — conteo: [['context_recall', 'alcanzabilidad_kg'], ['context_recall', 'navegación']]×1 / [['context_recall', 'alcanzabilidad_kg'], ['context_recall', 'navegación'], ['noise_sensitivity', 'aplicacion_erronea'], ['noise_sensitivity', 'contenido_kg']]×1 / [['context_recall', 'alcanzabilidad_kg'], ['context_recall', 'navegación'], ['noise_sensitivity', 'contenido_kg']]×1
- triage_s1: **TRIAGE** motivos=["fuente_no_verificable", "fuente_no_funda"] · flags: S1: rep1_atrib3 — fetch sin_portador_extraible | S1: rep2_atrib3 — fetch sin_portador_extraible | S1: rep3_atrib2 — fuente_no_funda (span máx 0)
- resumen S1: gatilladas=5 · juzgadas_llm=2 · corregidas=1 · no_determinable=0 · fetch_fallido=2 · cross_doc_bloqueadas=0 · fuente_no_funda=1 · exoneracion_con_sintoma=False
- **Costo S1:** 29.061 in / 3.400 out
- estados de fetch por atribución: 
    - rep1_atrib3: estado_fetch=sin_portador_extraible · accion=fuente_no_verificable · corrigio=False · triage=True
    - rep2_atrib3: estado_fetch=sin_portador_extraible · accion=fuente_no_verificable · corrigio=False · triage=True
    - rep2_atrib4: estado_fetch=completo · accion=None · corrigio=False · triage=False · voto_s1_atrib={"n": 3, "umbral": 2, "esquema": "causa", "decididas": 3, "no_decididas": 0, "resultado": "mayoria", "sintoma_ganador": "noise_sensitivity", "causa_ganadora": "aplicacion_erronea", "votos_ganadores": 3}
    - rep3_atrib2: estado_fetch=fuente_no_funda · accion=fuente_no_funda · corrigio=False · triage=True · fundamento: span_max=0 (umbral 60)
    - rep3_atrib4: estado_fetch=completo · accion=None · corrigio=True · triage=False · voto_s1_atrib={"n": 3, "umbral": 2, "esquema": "causa", "decididas": 3, "no_decididas": 0, "resultado": "mayoria", "sintoma_ganador": "noise_sensitivity", "causa_ganadora": "contenido_kg", "votos_ganadores": 3}
- secundarias emitidas: {noise_sensitivity, contenido_kg} (secundaria) ×2

---

## CQN2-012

**Costo verificador (3 reps):** in 469.157 / 1.109.551 / 1.175.034 = **2.753.742** · out 9.504 / 12.278 / 18.760 = **40.542**

**Voto LLM crudo (pre-capa):** **mayoría 2** ganadores=[['context_recall', 'completitud_kg'], ['context_recall', 'completitud_kg']] · conteo: [['context_recall', 'completitud_kg'], ['context_recall', 'completitud_kg']]×2 / [['context_recall', 'completitud_kg'], ['context_recall', 'frontera_no_determinada']]×1
  - desglose por rep: rep1=[['context_recall', 'completitud_kg'], ['context_recall', 'completitud_kg']] · rep2=[['context_recall', 'completitud_kg'], ['context_recall', 'frontera_no_determinada']] · rep3=[['context_recall', 'completitud_kg'], ['context_recall', 'completitud_kg']]

### Columna A — v6.1-D (`v6.1-D(2026-07)`)

- voto_capa_d: **mayoría 2** ganadores=[['context_recall', 'completitud_kg'], ['context_recall', 'completitud_kg']] · conteo: [['context_recall', 'completitud_kg'], ['context_recall', 'completitud_kg']]×2 / [['context_recall', 'completitud_kg'], ['context_recall', 'frontera_no_determinada']]×1
- triage: sin triage
- resumen D2: corregidas=0 · discrepancias=0 · triage_R3=0 · reps_tocadas=[]
- secundarias emitidas: {noise_sensitivity, sin_defecto} (sin_par) ×1

### Columna B — v6.2-D (`v6.2-D(2026-07)`)

- voto_capa_d: **mayoría 2** ganadores=[['context_recall', 'completitud_kg'], ['context_recall', 'completitud_kg']] · conteo: [['context_recall', 'completitud_kg'], ['context_recall', 'completitud_kg']]×2 / [['context_recall', 'completitud_kg'], ['context_recall', 'frontera_no_determinada']]×1
- triage: sin triage
- resumen D2': corregidas=0 · discrepancias=0 · triage_R3=0 · punteros_estructurales_extraidos=0 · decisiones_con_puntero=0
- anotaciones D7: (ninguna decisión por puntero)
- secundarias emitidas: {noise_sensitivity, sin_defecto} (sin_par) ×1

### Columna C — v7' = v6.2-D + S1 v0.4b (`s1-v0.4b-dev`)

- voto_s1: **mayoría 2** ganadores=[['context_recall', 'completitud_kg'], ['context_recall', 'completitud_kg']] · conteo: [['context_recall', 'completitud_kg'], ['context_recall', 'completitud_kg']]×2 / [['context_recall', 'completitud_kg'], ['context_recall', 'frontera_no_determinada']]×1
- triage_s1: **TRIAGE** motivos=["fuente_no_verificable", "fuente_no_funda"] · flags: S1: rep1_atrib1 — fetch sin_portador_extraible | S1: rep3_atrib2 — fuente_no_funda (span máx 0)
- resumen S1: gatilladas=5 · juzgadas_llm=3 · corregidas=0 · no_determinable=0 · fetch_fallido=1 · cross_doc_bloqueadas=0 · fuente_no_funda=1 · exoneracion_con_sintoma=False
- **Costo S1:** 33.111 in / 4.628 out
- estados de fetch por atribución: 
    - rep1_atrib1: estado_fetch=sin_portador_extraible · accion=fuente_no_verificable · corrigio=False · triage=True
    - rep1_atrib2: estado_fetch=completo · accion=None · corrigio=False · triage=False · voto_s1_atrib={"n": 3, "umbral": 2, "esquema": "causa", "decididas": 3, "no_decididas": 0, "resultado": "mayoria", "sintoma_ganador": "context_recall", "causa_ganadora": "completitud_kg", "votos_ganadores": 3}
    - rep2_atrib1: estado_fetch=completo · accion=None · corrigio=False · triage=False · voto_s1_atrib={"n": 3, "umbral": 2, "esquema": "causa", "decididas": 3, "no_decididas": 0, "resultado": "mayoria", "sintoma_ganador": "context_recall", "causa_ganadora": "completitud_kg", "votos_ganadores": 3}
    - rep3_atrib1: estado_fetch=completo · accion=None · corrigio=False · triage=False · voto_s1_atrib={"n": 3, "umbral": 2, "esquema": "causa", "decididas": 3, "no_decididas": 0, "resultado": "mayoria", "sintoma_ganador": "context_recall", "causa_ganadora": "completitud_kg", "votos_ganadores": 3}
    - rep3_atrib2: estado_fetch=fuente_no_funda · accion=fuente_no_funda · corrigio=False · triage=True · fundamento: span_max=0 (umbral 60)
- secundarias emitidas: {noise_sensitivity, sin_defecto} (sin_par) ×1

---

## CQN2-013

**Costo verificador (3 reps):** in 405.257 / 363.321 / 292.880 = **1.061.458** · out 8.977 / 8.656 / 7.553 = **25.186**

**Voto LLM crudo (pre-capa):** **mayoría 2** ganadores=[['context_recall', 'alcanzabilidad_kg']] · conteo: [['context_recall', 'alcanzabilidad_kg']]×2 / [['context_recall', 'completitud_kg']]×1
  - desglose por rep: rep1=[['context_recall', 'alcanzabilidad_kg']] · rep2=[['context_recall', 'alcanzabilidad_kg']] · rep3=[['context_recall', 'completitud_kg']]

### Columna A — v6.1-D (`v6.1-D(2026-07)`)

- voto_capa_d: **mayoría 2** ganadores=[['context_recall', 'alcanzabilidad_kg']] · conteo: [['context_recall', 'alcanzabilidad_kg']]×2 / [['context_recall', 'completitud_kg']]×1
- triage: **TRIAGE** motivos=["atribucion_no_verificable"] · flags: R6b: rep 1 atrib 1 — context_recall_sin_pata | R6b: rep 2 atrib 1 — context_recall_sin_pata | R6b: rep 3 atrib 1 — context_recall_sin_pata
- resumen D2: corregidas=2 · discrepancias=0 · triage_R3=0 · reps_tocadas=[1, 2]
- secundarias emitidas: (ninguna)

### Columna B — v6.2-D (`v6.2-D(2026-07)`)

- voto_capa_d: **mayoría 2** ganadores=[['context_recall', 'alcanzabilidad_kg']] · conteo: [['context_recall', 'alcanzabilidad_kg']]×2 / [['context_recall', 'completitud_kg']]×1
- triage: **TRIAGE** motivos=["atribucion_no_verificable"] · flags: R6b: rep 1 atrib 1 — context_recall_sin_pata | R6b: rep 2 atrib 1 — context_recall_sin_pata | R6b: rep 3 atrib 1 — context_recall_sin_pata
- resumen D2': corregidas=2 · discrepancias=0 · triage_R3=0 · punteros_estructurales_extraidos=0 · decisiones_con_puntero=0
- anotaciones D7: (ninguna decisión por puntero)
- secundarias emitidas: (ninguna)

### Columna C — v7' = v6.2-D + S1 v0.4b (`s1-v0.4b-dev`)

- voto_s1: **mayoría 2** ganadores=[['context_recall', 'alcanzabilidad_kg']] · conteo: [['context_recall', 'alcanzabilidad_kg']]×2 / [['context_recall', 'completitud_kg']]×1
- triage_s1: sin triage
- resumen S1: gatilladas=1 · juzgadas_llm=1 · corregidas=0 · no_determinable=0 · fetch_fallido=0 · cross_doc_bloqueadas=0 · fuente_no_funda=0 · exoneracion_con_sintoma=False
- **Costo S1:** 11.682 in / 1.542 out
- estados de fetch por atribución: 
    - rep3_atrib1: estado_fetch=completo · accion=None · corrigio=False · triage=False · voto_s1_atrib={"n": 3, "umbral": 2, "esquema": "causa", "decididas": 3, "no_decididas": 0, "resultado": "mayoria", "sintoma_ganador": "context_recall", "causa_ganadora": "completitud_kg", "votos_ganadores": 3}
- secundarias emitidas: (ninguna)

---

## CQN2-014

**Costo verificador (3 reps):** in 251.276 / 174.877 / 212.680 = **638.833** · out 7.153 / 6.232 / 6.745 = **20.130**

**Voto LLM crudo (pre-capa):** **mayoría 3** ganadores=[['context_recall', 'completitud_kg']] · conteo: [['context_recall', 'completitud_kg']]×3
  - desglose por rep: rep1=[['context_recall', 'completitud_kg']] · rep2=[['context_recall', 'completitud_kg']] · rep3=[['context_recall', 'completitud_kg']]

### Columna A — v6.1-D (`v6.1-D(2026-07)`)

- voto_capa_d: **mayoría 3** ganadores=[['context_recall', 'completitud_kg']] · conteo: [['context_recall', 'completitud_kg']]×3
- triage: sin triage
- resumen D2: corregidas=0 · discrepancias=0 · triage_R3=0 · reps_tocadas=[]
- secundarias emitidas: (ninguna)

### Columna B — v6.2-D (`v6.2-D(2026-07)`)

- voto_capa_d: **mayoría 3** ganadores=[['context_recall', 'completitud_kg']] · conteo: [['context_recall', 'completitud_kg']]×3
- triage: sin triage
- resumen D2': corregidas=0 · discrepancias=0 · triage_R3=0 · punteros_estructurales_extraidos=2 · decisiones_con_puntero=0
- anotaciones D7: (ninguna decisión por puntero)
- secundarias emitidas: (ninguna)

### Columna C — v7' = v6.2-D + S1 v0.4b (`s1-v0.4b-dev`)

- voto_s1: **mayoría 3** ganadores=[['context_recall', 'completitud_kg']] · conteo: [['context_recall', 'completitud_kg']]×3
- triage_s1: sin triage
- resumen S1: gatilladas=3 · juzgadas_llm=3 · corregidas=0 · no_determinable=0 · fetch_fallido=0 · cross_doc_bloqueadas=0 · fuente_no_funda=0 · exoneracion_con_sintoma=False
- **Costo S1:** 28.113 in / 5.653 out
- estados de fetch por atribución: 
    - rep1_atrib1: estado_fetch=completo · accion=None · corrigio=False · triage=False · voto_s1_atrib={"n": 3, "umbral": 2, "esquema": "causa", "decididas": 3, "no_decididas": 0, "resultado": "mayoria", "sintoma_ganador": "context_recall", "causa_ganadora": "completitud_kg", "votos_ganadores": 3}
    - rep2_atrib1: estado_fetch=completo · accion=None · corrigio=False · triage=False · voto_s1_atrib={"n": 3, "umbral": 2, "esquema": "causa", "decididas": 3, "no_decididas": 0, "resultado": "mayoria", "sintoma_ganador": "context_recall", "causa_ganadora": "completitud_kg", "votos_ganadores": 3}
    - rep3_atrib1: estado_fetch=completo · accion=None · corrigio=False · triage=False · voto_s1_atrib={"n": 3, "umbral": 2, "esquema": "causa", "decididas": 3, "no_decididas": 0, "resultado": "mayoria", "sintoma_ganador": "context_recall", "causa_ganadora": "completitud_kg", "votos_ganadores": 3}
- secundarias emitidas: (ninguna)

---

## CQN2-015

**Costo verificador (3 reps):** in 1.235.037 / 429.536 / 911.291 = **2.575.864** · out 15.710 / 8.196 / 13.406 = **37.312**

**Voto LLM crudo (pre-capa):** **mayoría 2** ganadores=[['context_recall', 'completitud_kg'], ['context_recall', 'completitud_kg']] · conteo: [['context_recall', 'completitud_kg'], ['context_recall', 'completitud_kg']]×2 / [['context_recall', 'navegación'], ['context_recall', 'navegación']]×1
  - desglose por rep: rep1=[['context_recall', 'completitud_kg'], ['context_recall', 'completitud_kg']] · rep2=[['context_recall', 'navegación'], ['context_recall', 'navegación']] · rep3=[['context_recall', 'completitud_kg'], ['context_recall', 'completitud_kg']]

### Columna A — v6.1-D (`v6.1-D(2026-07)`)

- voto_capa_d: **mayoría 2** ganadores=[['context_recall', 'completitud_kg'], ['context_recall', 'completitud_kg']] · conteo: [['context_recall', 'completitud_kg'], ['context_recall', 'completitud_kg']]×2 / [['context_recall', 'alcanzabilidad_kg'], ['context_recall', 'alcanzabilidad_kg']]×1
- triage: sin triage
- resumen D2: corregidas=2 · discrepancias=2 · triage_R3=0 · reps_tocadas=[2]
- secundarias emitidas: (ninguna)

### Columna B — v6.2-D (`v6.2-D(2026-07)`)

- voto_capa_d: **mayoría 2** ganadores=[['context_recall', 'completitud_kg'], ['context_recall', 'completitud_kg']] · conteo: [['context_recall', 'completitud_kg'], ['context_recall', 'completitud_kg']]×2 / [['context_recall', 'alcanzabilidad_kg'], ['context_recall', 'alcanzabilidad_kg']]×1
- triage: sin triage
- resumen D2': corregidas=2 · discrepancias=2 · triage_R3=0 · punteros_estructurales_extraidos=0 · decisiones_con_puntero=0
- anotaciones D7: (ninguna decisión por puntero)
- secundarias emitidas: (ninguna)

### Columna C — v7' = v6.2-D + S1 v0.4b (`s1-v0.4b-dev`)

- voto_s1: **mayoría 2** ganadores=[['context_recall', 'completitud_kg'], ['context_recall', 'completitud_kg']] · conteo: [['context_recall', 'completitud_kg'], ['context_recall', 'completitud_kg']]×2 / [['context_recall', 'alcanzabilidad_kg'], ['context_recall', 'alcanzabilidad_kg']]×1
- triage_s1: **TRIAGE** motivos=["fuente_no_verificable"] · flags: S1: rep1_atrib1 — fetch contenido_no_unico | S1: rep3_atrib1 — fetch sin_portador_extraible
- resumen S1: gatilladas=4 · juzgadas_llm=2 · corregidas=0 · no_determinable=0 · fetch_fallido=2 · cross_doc_bloqueadas=0 · fuente_no_funda=0 · exoneracion_con_sintoma=False
- **Costo S1:** 27.981 in / 2.962 out
- estados de fetch por atribución: 
    - rep1_atrib1: estado_fetch=contenido_no_unico · accion=fuente_no_verificable · corrigio=False · triage=True
    - rep1_atrib2: estado_fetch=completo · accion=None · corrigio=False · triage=False · voto_s1_atrib={"n": 3, "umbral": 2, "esquema": "causa", "decididas": 3, "no_decididas": 0, "resultado": "mayoria", "sintoma_ganador": "context_recall", "causa_ganadora": "completitud_kg", "votos_ganadores": 3}
    - rep3_atrib1: estado_fetch=sin_portador_extraible · accion=fuente_no_verificable · corrigio=False · triage=True
    - rep3_atrib2: estado_fetch=completo · accion=None · corrigio=False · triage=False · voto_s1_atrib={"n": 3, "umbral": 2, "esquema": "causa", "decididas": 3, "no_decididas": 0, "resultado": "mayoria", "sintoma_ganador": "context_recall", "causa_ganadora": "completitud_kg", "votos_ganadores": 3}
- secundarias emitidas: (ninguna)

---

## Tabla resumen (11 filas × 3 columnas — SIN columna de acierto; el scoring es externo)

| Caso | (A) v6.1-D | (B) v6.2-D | (C) v7' (v6.2-D + S1 v0.4b) |
|---|---|---|---|
| CQN2-002 | DIVIDIDO 1-1-1 · TRIAGE(atribucion_no_verificable,voto_dividido) | DIVIDIDO 1-1-1 · TRIAGE(atribucion_no_verificable,voto_dividido) | DIVIDIDO 1-1-1 · TRIAGE(fuente_cross_doc) |
| CQN2-004 | {noise_sensitivity, contenido_kg} 2-1 · TRIAGE(atribucion_no_verificable) | {noise_sensitivity, contenido_kg} 2-1 · TRIAGE(atribucion_no_verificable) | {noise_sensitivity, contenido_kg} 2-1 · TRIAGE(fuente_cross_doc,fuente_no_funda) |
| CQN2-005 | {context_recall, alcanzabilidad_kg} 3-0 | {context_recall, alcanzabilidad_kg} 3-0 | {context_recall, alcanzabilidad_kg} 3-0 |
| CQN2-006 | {context_recall, completitud_kg} 3-0 | {context_recall, completitud_kg} 3-0 | {context_recall, completitud_kg} 3-0 · TRIAGE(fuente_no_funda) |
| CQN2-007 | exoneración [] 3-0 · TRIAGE(exoneracion_total) | exoneración [] 3-0 · TRIAGE(exoneracion_total) | exoneración [] 3-0 |
| CQN2-010 | {context_recall, completitud_kg} 3-0 | {context_recall, completitud_kg} 3-0 | {context_recall, completitud_kg} 3-0 · TRIAGE(fuente_no_funda,fuente_no_verificable) |
| CQN2-011 | DIVIDIDO 1-1-1 · TRIAGE(aplicacion_erronea_bajo_revision,atribucion_no_verificable,modulo_deterministico_sin_decision,voto_dividido) | DIVIDIDO 1-1-1 · TRIAGE(aplicacion_erronea_bajo_revision,atribucion_no_verificable,modulo_deterministico_sin_decision,voto_dividido) | DIVIDIDO 1-1-1 · TRIAGE(fuente_no_funda,fuente_no_verificable) |
| CQN2-012 | {context_recall, completitud_kg} 2-1 | {context_recall, completitud_kg} 2-1 | {context_recall, completitud_kg} 2-1 · TRIAGE(fuente_no_funda,fuente_no_verificable) |
| CQN2-013 | {context_recall, alcanzabilidad_kg} 2-1 · TRIAGE(atribucion_no_verificable) | {context_recall, alcanzabilidad_kg} 2-1 · TRIAGE(atribucion_no_verificable) | {context_recall, alcanzabilidad_kg} 2-1 |
| CQN2-014 | {context_recall, completitud_kg} 3-0 | {context_recall, completitud_kg} 3-0 | {context_recall, completitud_kg} 3-0 |
| CQN2-015 | {context_recall, completitud_kg} 2-1 | {context_recall, completitud_kg} 2-1 | {context_recall, completitud_kg} 2-1 · TRIAGE(fuente_no_verificable) |

**Costos totales:** verificador **12.869.986 in / 300.112 out** · S1 **186.531 in / 23.640 out**
(capas A/B: cero llamadas LLM).


---

## Sello

Fecha: 2026-07-19 · HEAD: `65bea991b0dd4180f6746e40a4641af32142dccb` · Corrida única; JSONs congelados en `posthoc_run/gate2_h2h/`.

Guarda del paso 0 (los 4 checks, verificados ANTES de la corrida):
1. `git status` LIMPIO.
2. Último commit que toca `docs/casos_gate_cqn2.md` = `65bea991b0dd4180f6746e40a4641af32142dccb` = HEAD (vara commiteada antes de toda corrida).
3. SHA-256 del set sellado = `f3de487a46f53868725dc645ba6478ee03021bafd785295ced0f06f94b15485d` y del runtime = `18e178c81ffbf6d8d6f9220639e8c6fa9bb09a76403da9a0aa3e0066c1468084` — idénticos a los del sellado.
4. Congelados con CERO diff pendiente; hashes: `verificador.py` `084b2db8efe4228828dfc4a47c777859238e5c3b7d10c49b7525b59b6763744a` · prompt v5.7 ensamblado `d031913d580278df833c125df7d8469bc1dd19bc9775082d0b6cb64a77442659` · `taxonomia.md` `fc9a4962a222867a9ff7bd66cfd5962285139352d50b257355e14bec803b34ad` · `capa_deterministica.py` `35b248b266764414da468458c1191511ca6dd9336972fee95d4e4377fb86db3c` · `capa_deterministica_v62.py` `d43f76b1fe69327913db8950490a9695458d05d78d77162b8c6df0de10fb958a` · `s1_fuentes.py` `3263985ca022ee341f65a43a3ed193b2f5175ede2b87d5cf73dddc44a253c0cd` · `s1_fuentes_v04.py` `ce423fab664f5c62a56f7143d66ca8e430403c8f934da945570eb74c038d039b` (TRACKED, `S1_VERSION_V04="s1-v0.4b-dev"`).

