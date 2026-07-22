# Extracción del head-to-head — gate CQN (10 casos) — MECÁNICA, SIN SCORING

Corrida única. v6.1-D = verificador v5.7 congelado N=3 + capa determinística; S1 =
s1-v0.3.1-dev N=3 con triage-por-fetch conservador. **La vara (docs/casos_gate_cqn.md)
y su evidencia NO entraron al contexto de ninguna corrida ni de esta extracción** — el
scoring es externo y posterior. Cero interpretación: votos, triage y costos, literales.


---

## CQN-001

### (a) v6.1-D

- reps válidas: 3/3
- voto v5.7 (original): mayoria · dividido=False · ganadores=[['noise_sensitivity', 'aplicacion_erronea']] (2) · conteo: 2×[['noise_sensitivity', 'aplicacion_erronea']] · 1×[['noise_sensitivity', 'contenido_kg']]
- voto_pre_d6: mayoria · dividido=False · ganadores=[['noise_sensitivity', 'aplicacion_erronea']] (2) · conteo: 2×[['noise_sensitivity', 'aplicacion_erronea']] · 1×[['noise_sensitivity', 'contenido_kg']]
- **voto_capa_d (FINAL v6.1-D): frontera_no_determinada · dividido=True · ganadores=None (None) · conteo: 1×[] · 1×[['noise_sensitivity', 'aplicacion_erronea']] · 1×[['noise_sensitivity', 'contenido_kg']]**
- triage: True · motivos=['aplicacion_erronea_bajo_revision', 'modulo_deterministico_sin_decision', 'atribucion_no_verificable', 'voto_dividido']
  - R2: rep 1 atrib 1 (secundaria) causa aplicacion_erronea
  - R3: rep 1 atrib 1 — D3/sin_portador_extraible
  - R6b: rep 2 atrib 1 — claim_no_mapeado
  - R2: rep 3 atrib 1 (primaria) causa aplicacion_erronea
  - R3: rep 3 atrib 1 — D3/sin_portador_extraible
  - R6b: rep 3 atrib 1 — claim_no_mapeado
  - R4: voto_capa_d.flag_voto_dividido = true
- pares no-primarios emitidos (post-capa; (síntoma, causa, jerarquía) × reps):
  - (noise_sensitivity, aplicacion_erronea) [secundaria] ×1
- resumen_capa_d: {"reps_tocadas": [], "atribuciones_corregidas": 0, "discrepancias": 0, "triage": 0}

### (b) S1 (v0.3.1, N=3)

- **voto_s1 (FINAL S1): frontera_no_determinada · dividido=True · ganadores=None (None) · conteo: 1×[] · 1×[['faithfulness', 'contenido_kg']] · 1×[['noise_sensitivity', 'aplicacion_erronea']]**
- triage_s1: True · motivos=['fuente_no_verificable']
  - S1: rep1_atrib1 — fetch sin_portador_extraible
  - S1: rep3_atrib1 — fetch sin_portador_extraible
- resumen_s1: gatilladas=3 · juzgadas_llm=1 · corregidas=1 · no_determinable=0 · fetch_fallido=2 · exoneracion_con_sintoma=False
- estados de fetch por atribución gatillada: {'sin_portador_extraible': 2, 'completo': 1}

### (c) Costo por caso

- v6.1-D (verificador, 3 reps): **747,240 in / 21,007 out**
- S1 (usage real): **10,908 in / 1,603 out**

---

## CQN-006

### (a) v6.1-D

- reps válidas: 3/3
- voto v5.7 (original): mayoria · dividido=False · ganadores=[] (3) · conteo: 3×[]
- voto_pre_d6: mayoria · dividido=False · ganadores=[] (3) · conteo: 3×[]
- **voto_capa_d (FINAL v6.1-D): mayoria · dividido=False · ganadores=[] (3) · conteo: 3×[]**
- triage: True · motivos=['exoneracion_total']
  - R1: voto_capa_d con mayoria de clave vacia (3 votos sin primarias)
- pares no-primarios emitidos (post-capa; (síntoma, causa, jerarquía) × reps):
  - (noise_sensitivity, provenance_imprecisa) [secundaria] ×2
- resumen_capa_d: {"reps_tocadas": [], "atribuciones_corregidas": 0, "discrepancias": 0, "triage": 0}

### (b) S1 (v0.3.1, N=3)

- **voto_s1 (FINAL S1): mayoria · dividido=False · ganadores=[] (3) · conteo: 3×[]**
- triage_s1: True · motivos=['fuente_no_verificable']
  - S1: rep1_atrib1 — no_determinable (0/3 decididas)
  - S1: rep2_atrib1 — no_determinable (0/3 decididas)
  - S1: rep3_atrib1 — no_determinable (0/3 decididas)
- resumen_s1: gatilladas=3 · juzgadas_llm=3 · corregidas=0 · no_determinable=3 · fetch_fallido=0 · exoneracion_con_sintoma=True
- estados de fetch por atribución gatillada: {'completo': 3}

### (c) Costo por caso

- v6.1-D (verificador, 3 reps): **569,892 in / 19,186 out**
- S1 (usage real): **38,994 in / 585 out**

---

## CQN-007

### (a) v6.1-D

- reps válidas: 3/3
- voto v5.7 (original): mayoria · dividido=False · ganadores=[['context_recall', 'navegación']] (3) · conteo: 3×[['context_recall', 'navegación']]
- voto_pre_d6: mayoria · dividido=False · ganadores=[['context_recall', 'alcanzabilidad_kg']] (3) · conteo: 3×[['context_recall', 'alcanzabilidad_kg']]
- **voto_capa_d (FINAL v6.1-D): mayoria · dividido=False · ganadores=[['context_recall', 'alcanzabilidad_kg']] (3) · conteo: 3×[['context_recall', 'alcanzabilidad_kg']]**
- triage: False · motivos=[]
- pares no-primarios emitidos (post-capa; (síntoma, causa, jerarquía) × reps):
  - (noise_sensitivity, provenance_imprecisa) [secundaria] ×1
- resumen_capa_d: {"reps_tocadas": [1, 2, 3], "atribuciones_corregidas": 3, "discrepancias": 3, "triage": 0}

### (b) S1 (v0.3.1, N=3)

- **voto_s1 (FINAL S1): mayoria · dividido=False · ganadores=[['context_recall', 'alcanzabilidad_kg']] (3) · conteo: 3×[['context_recall', 'alcanzabilidad_kg']]**
- triage_s1: False · motivos=[]
- resumen_s1: gatilladas=0 · juzgadas_llm=0 · corregidas=0 · no_determinable=0 · fetch_fallido=0 · exoneracion_con_sintoma=False

### (c) Costo por caso

- v6.1-D (verificador, 3 reps): **900,226 in / 28,602 out**
- S1 (usage real): **0 in / 0 out**

---

## CQN-008  ·  (ilustrativa — se reporta aparte)

### (a) v6.1-D

- reps válidas: 3/3
- voto v5.7 (original): mayoria · dividido=False · ganadores=[['context_recall', 'navegación']] (3) · conteo: 3×[['context_recall', 'navegación']]
- voto_pre_d6: mayoria · dividido=False · ganadores=[['context_recall', 'navegación']] (3) · conteo: 3×[['context_recall', 'navegación']]
- **voto_capa_d (FINAL v6.1-D): mayoria · dividido=False · ganadores=[['context_recall', 'navegación']] (3) · conteo: 3×[['context_recall', 'navegación']]**
- triage: True · motivos=['atribucion_no_verificable', 'modulo_deterministico_sin_decision']
  - R6b: rep 1 atrib 1 — context_recall_sin_pata
  - R6b: rep 2 atrib 1 — context_recall_sin_pata
  - R3: rep 3 atrib 1 — D2/sin_portador_extraible
  - R6b: rep 3 atrib 1 — context_recall_sin_pata
- pares no-primarios emitidos (post-capa; (síntoma, causa, jerarquía) × reps):
  - (faithfulness, alucinacion_agente) [secundaria] ×3
  - (noise_sensitivity, contenido_kg) [secundaria] ×2
- resumen_capa_d: {"reps_tocadas": [1, 2, 3], "atribuciones_corregidas": 2, "discrepancias": 0, "triage": 1}

### (b) S1 (v0.3.1, N=3)

- **voto_s1 (FINAL S1): mayoria · dividido=False · ganadores=[['context_recall', 'navegación']] (3) · conteo: 3×[['context_recall', 'navegación']]**
- triage_s1: False · motivos=[]
- resumen_s1: gatilladas=2 · juzgadas_llm=2 · corregidas=2 · no_determinable=0 · fetch_fallido=0 · exoneracion_con_sintoma=False
- estados de fetch por atribución gatillada: {'completo': 2}

### (c) Costo por caso

- v6.1-D (verificador, 3 reps): **1,511,595 in / 42,945 out**
- S1 (usage real): **20,958 in / 2,845 out**

---

## CQN-009

### (a) v6.1-D

- reps válidas: 3/3
- voto v5.7 (original): mayoria · dividido=False · ganadores=[['context_recall', 'completitud_kg']] (3) · conteo: 3×[['context_recall', 'completitud_kg']]
- voto_pre_d6: mayoria · dividido=False · ganadores=[['context_recall', 'completitud_kg']] (3) · conteo: 3×[['context_recall', 'completitud_kg']]
- **voto_capa_d (FINAL v6.1-D): mayoria · dividido=False · ganadores=[['context_recall', 'completitud_kg']] (3) · conteo: 3×[['context_recall', 'completitud_kg']]**
- triage: False · motivos=[]
- resumen_capa_d: {"reps_tocadas": [], "atribuciones_corregidas": 0, "discrepancias": 0, "triage": 0}

### (b) S1 (v0.3.1, N=3)

- **voto_s1 (FINAL S1): mayoria · dividido=False · ganadores=[['context_recall', 'completitud_kg']] (3) · conteo: 3×[['context_recall', 'completitud_kg']]**
- triage_s1: True · motivos=['fuente_no_verificable']
  - S1: rep1_atrib1 — fetch sin_portador_extraible
- resumen_s1: gatilladas=3 · juzgadas_llm=2 · corregidas=0 · no_determinable=0 · fetch_fallido=1 · exoneracion_con_sintoma=False
- estados de fetch por atribución gatillada: {'sin_portador_extraible': 1, 'completo': 2}

### (c) Costo por caso

- v6.1-D (verificador, 3 reps): **2,328,879 in / 33,713 out**
- S1 (usage real): **18,615 in / 2,713 out**

---

## CQN-010

### (a) v6.1-D

- reps válidas: 3/3
- voto v5.7 (original): mayoria · dividido=False · ganadores=[] (3) · conteo: 3×[]
- voto_pre_d6: mayoria · dividido=False · ganadores=[] (3) · conteo: 3×[]
- **voto_capa_d (FINAL v6.1-D): mayoria · dividido=False · ganadores=[] (3) · conteo: 3×[]**
- triage: True · motivos=['exoneracion_total']
  - R1: voto_capa_d con mayoria de clave vacia (3 votos sin primarias)
- pares no-primarios emitidos (post-capa; (síntoma, causa, jerarquía) × reps):
  - (faithfulness, alucinacion_agente) [secundaria] ×3
- resumen_capa_d: {"reps_tocadas": [], "atribuciones_corregidas": 0, "discrepancias": 0, "triage": 0}

### (b) S1 (v0.3.1, N=3)

- **voto_s1 (FINAL S1): mayoria · dividido=False · ganadores=[] (3) · conteo: 3×[]**
- triage_s1: False · motivos=[]
- resumen_s1: gatilladas=0 · juzgadas_llm=0 · corregidas=0 · no_determinable=0 · fetch_fallido=0 · exoneracion_con_sintoma=True

### (c) Costo por caso

- v6.1-D (verificador, 3 reps): **576,458 in / 17,932 out**
- S1 (usage real): **0 in / 0 out**

---

## CQN-011

### (a) v6.1-D

- reps válidas: 3/3
- voto v5.7 (original): frontera_no_determinada · dividido=True · ganadores=None (None) · conteo: 1×[['context_recall', 'completitud_kg']] · 1×[['context_recall', 'completitud_kg'], ['noise_sensitivity', 'contenido_kg']] · 1×[['context_recall', 'completitud_kg'], ['noise_sensitivity', 'aplicacion_erronea']]
- voto_pre_d6: frontera_no_determinada · dividido=True · ganadores=None (None) · conteo: 1×[['context_recall', 'completitud_kg']] · 1×[['context_recall', 'completitud_kg'], ['noise_sensitivity', 'aplicacion_erronea']] · 1×[['context_recall', 'completitud_kg'], ['noise_sensitivity', 'contenido_kg']]
- **voto_capa_d (FINAL v6.1-D): frontera_no_determinada · dividido=True · ganadores=None (None) · conteo: 1×[['context_recall', 'completitud_kg']] · 1×[['context_recall', 'completitud_kg'], ['noise_sensitivity', 'aplicacion_erronea']] · 1×[['context_recall', 'completitud_kg'], ['noise_sensitivity', 'contenido_kg']]**
- triage: True · motivos=['atribucion_no_verificable', 'aplicacion_erronea_bajo_revision', 'voto_dividido']
  - R6b: rep 2 atrib 1 — claim_no_mapeado
  - R2: rep 3 atrib 2 (primaria) causa aplicacion_erronea
  - R4: voto_capa_d.flag_voto_dividido = true
- pares no-primarios emitidos (post-capa; (síntoma, causa, jerarquía) × reps):
  - (faithfulness, alucinacion_agente) [secundaria] ×1
- resumen_capa_d: {"reps_tocadas": [], "atribuciones_corregidas": 0, "discrepancias": 0, "triage": 0}

### (b) S1 (v0.3.1, N=3)

- **voto_s1 (FINAL S1): frontera_no_determinada · dividido=True · ganadores=None (None) · conteo: 1×[['context_recall', 'completitud_kg'], ['noise_sensitivity', 'aplicacion_erronea']] · 1×[['context_recall', 'completitud_kg'], ['noise_sensitivity', 'contenido_kg']] · 1×[['noise_sensitivity', 'contenido_kg']]**
- triage_s1: True · motivos=['fuente_no_verificable']
  - S1: rep3_atrib2 — no_determinable (3/3 decididas)
- resumen_s1: gatilladas=5 · juzgadas_llm=5 · corregidas=1 · no_determinable=1 · fetch_fallido=0 · exoneracion_con_sintoma=False
- estados de fetch por atribución gatillada: {'completo': 5}

### (c) Costo por caso

- v6.1-D (verificador, 3 reps): **1,220,839 in / 31,894 out**
- S1 (usage real): **69,339 in / 7,340 out**

---

## CQN-012

### (a) v6.1-D

- reps válidas: 3/3
- voto v5.7 (original): mayoria · dividido=False · ganadores=[['context_recall', 'completitud_kg']] (3) · conteo: 3×[['context_recall', 'completitud_kg']]
- voto_pre_d6: mayoria · dividido=False · ganadores=[['context_recall', 'completitud_kg']] (3) · conteo: 3×[['context_recall', 'completitud_kg']]
- **voto_capa_d (FINAL v6.1-D): mayoria · dividido=False · ganadores=[['context_recall', 'completitud_kg']] (3) · conteo: 3×[['context_recall', 'completitud_kg']]**
- triage: True · motivos=['atribucion_no_verificable']
  - R6b: rep 1 atrib 1 — context_recall_sin_pata
  - R6b: rep 2 atrib 1 — context_recall_sin_pata
  - R6b: rep 3 atrib 1 — context_recall_sin_pata
- pares no-primarios emitidos (post-capa; (síntoma, causa, jerarquía) × reps):
  - (context_recall, completitud_kg) [secundaria] ×1
  - (faithfulness, alucinacion_agente) [secundaria] ×2
- resumen_capa_d: {"reps_tocadas": [], "atribuciones_corregidas": 0, "discrepancias": 0, "triage": 0}

### (b) S1 (v0.3.1, N=3)

- **voto_s1 (FINAL S1): mayoria · dividido=False · ganadores=[['context_recall', 'completitud_kg']] (2) · conteo: 2×[['context_recall', 'completitud_kg']] · 1×[['noise_sensitivity', 'completitud_kg']]**
- triage_s1: False · motivos=[]
- resumen_s1: gatilladas=4 · juzgadas_llm=4 · corregidas=2 · no_determinable=0 · fetch_fallido=0 · exoneracion_con_sintoma=False
- estados de fetch por atribución gatillada: {'completo': 4}

### (c) Costo por caso

- v6.1-D (verificador, 3 reps): **712,015 in / 23,469 out**
- S1 (usage real): **35,676 in / 6,235 out**

---

## CQN-013

### (a) v6.1-D

- reps válidas: 3/3
- voto v5.7 (original): mayoria · dividido=False · ganadores=[['noise_sensitivity', 'aplicacion_erronea']] (2) · conteo: 2×[['noise_sensitivity', 'aplicacion_erronea']] · 1×[['noise_sensitivity', 'contenido_kg']]
- voto_pre_d6: mayoria · dividido=False · ganadores=[['noise_sensitivity', 'aplicacion_erronea']] (2) · conteo: 2×[['noise_sensitivity', 'aplicacion_erronea']] · 1×[['noise_sensitivity', 'contenido_kg']]
- **voto_capa_d (FINAL v6.1-D): mayoria · dividido=False · ganadores=[['noise_sensitivity', 'aplicacion_erronea']] (2) · conteo: 2×[['noise_sensitivity', 'aplicacion_erronea']] · 1×[['noise_sensitivity', 'contenido_kg']]**
- triage: True · motivos=['atribucion_no_verificable', 'aplicacion_erronea_bajo_revision', 'modulo_deterministico_sin_decision']
  - R6b: rep 1 atrib 1 — claim_no_mapeado
  - R2: rep 2 atrib 1 (primaria) causa aplicacion_erronea
  - R3: rep 2 atrib 1 — D3/quote_no_verificable
  - R6b: rep 2 atrib 1 — claim_no_mapeado
  - R2: rep 3 atrib 1 (primaria) causa aplicacion_erronea
  - R3: rep 3 atrib 1 — D3/quote_no_verificable
  - R6b: rep 3 atrib 1 — claim_no_mapeado
- resumen_capa_d: {"reps_tocadas": [], "atribuciones_corregidas": 0, "discrepancias": 0, "triage": 0}

### (b) S1 (v0.3.1, N=3)

- **voto_s1 (FINAL S1): mayoria · dividido=False · ganadores=[['faithfulness', 'contenido_kg']] (3) · conteo: 3×[['faithfulness', 'contenido_kg']]**
- triage_s1: False · motivos=[]
- resumen_s1: gatilladas=3 · juzgadas_llm=3 · corregidas=3 · no_determinable=0 · fetch_fallido=0 · exoneracion_con_sintoma=False
- estados de fetch por atribución gatillada: {'completo': 3}

### (c) Costo por caso

- v6.1-D (verificador, 3 reps): **445,847 in / 15,822 out**
- S1 (usage real): **25,722 in / 4,235 out**

---

## CQN-014

### (a) v6.1-D

- reps válidas: 3/3
- voto v5.7 (original): mayoria · dividido=False · ganadores=[['context_recall', 'navegación']] (2) · conteo: 2×[['context_recall', 'navegación']] · 1×[['context_recall', 'estructural_kg']]
- voto_pre_d6: mayoria · dividido=False · ganadores=[['context_recall', 'navegación']] (2) · conteo: 2×[['context_recall', 'navegación']] · 1×[['context_recall', 'estructural_kg']]
- **voto_capa_d (FINAL v6.1-D): mayoria · dividido=False · ganadores=[['context_recall', 'navegación']] (2) · conteo: 2×[['context_recall', 'navegación']] · 1×[['context_recall', 'estructural_kg']]**
- triage: True · motivos=['modulo_deterministico_sin_decision']
  - R3: rep 2 atrib 1 — D2/sin_portador_extraible
  - R3: rep 3 atrib 1 — D2/sin_portador_extraible
- resumen_capa_d: {"reps_tocadas": [2, 3], "atribuciones_corregidas": 0, "discrepancias": 0, "triage": 2}

### (b) S1 (v0.3.1, N=3)

- **voto_s1 (FINAL S1): mayoria · dividido=False · ganadores=[['context_recall', 'navegación']] (2) · conteo: 2×[['context_recall', 'navegación']] · 1×[['context_recall', 'estructural_kg']]**
- triage_s1: True · motivos=['fuente_no_verificable']
  - S1: rep1_atrib1 — fetch sin_portador_extraible
- resumen_s1: gatilladas=1 · juzgadas_llm=0 · corregidas=0 · no_determinable=0 · fetch_fallido=1 · exoneracion_con_sintoma=False
- estados de fetch por atribución gatillada: {'sin_portador_extraible': 1}

### (c) Costo por caso

- v6.1-D (verificador, 3 reps): **825,678 in / 25,276 out**
- S1 (usage real): **0 in / 0 out**

---

## Tabla resumen (10 filas, votos lado a lado — SIN columna de acierto)

| Caso | voto FINAL v6.1-D | triage v6.1-D | voto FINAL S1 | triage S1 | tok_in v6.1-D | tok_in S1 |
|---|---|---|---|---|---|---|
| CQN-001 | DIVIDIDO [1, 1, 1] | aplicacion_erronea_bajo_revision,modulo_deterministico_sin_decision,atribucion_no_verificable,voto_dividido | DIVIDIDO [1, 1, 1] | fuente_no_verificable | 747,240 | 10,908 |
| CQN-006 | [] (3-0) | exoneracion_total | [] (3-0) | fuente_no_verificable | 569,892 | 38,994 |
| CQN-007 | [['context_recall', 'alcanzabilidad_kg']] (3-0) | — | [['context_recall', 'alcanzabilidad_kg']] (3-0) | — | 900,226 | 0 |
| CQN-008 (ilustrativa) | [['context_recall', 'navegación']] (3-0) | atribucion_no_verificable,modulo_deterministico_sin_decision | [['context_recall', 'navegación']] (3-0) | — | 1,511,595 | 20,958 |
| CQN-009 | [['context_recall', 'completitud_kg']] (3-0) | — | [['context_recall', 'completitud_kg']] (3-0) | fuente_no_verificable | 2,328,879 | 18,615 |
| CQN-010 | [] (3-0) | exoneracion_total | [] (3-0) | — | 576,458 | 0 |
| CQN-011 | DIVIDIDO [1, 1, 1] | atribucion_no_verificable,aplicacion_erronea_bajo_revision,voto_dividido | DIVIDIDO [1, 1, 1] | fuente_no_verificable | 1,220,839 | 69,339 |
| CQN-012 | [['context_recall', 'completitud_kg']] (3-0) | atribucion_no_verificable | [['context_recall', 'completitud_kg']] (2-1) | — | 712,015 | 35,676 |
| CQN-013 | [['noise_sensitivity', 'aplicacion_erronea']] (2-1) | atribucion_no_verificable,aplicacion_erronea_bajo_revision,modulo_deterministico_sin_decision | [['faithfulness', 'contenido_kg']] (3-0) | — | 445,847 | 25,722 |
| CQN-014 | [['context_recall', 'navegación']] (2-1) | modulo_deterministico_sin_decision | [['context_recall', 'navegación']] (2-1) | fuente_no_verificable | 825,678 | 0 |

**Costos totales:** corrida 1 (verificador): **9,838,669 in / 259,846 out** · corrida 2 (S1): **220,212 in / 25,556 out**.

## Sello

- Fecha: 2026-07-18 · HEAD: `1d4e7a87d5095375b418e79fba97ea329eaebc6c`
- Checks del paso 0 (los 4, verificados antes de correr): (1) git status LIMPIO; (2) vara
  commiteada `1d4e7a87d5095375b418e79fba97ea329eaebc6c`, en HEAD; (3) blob del runtime =
  `7486b2fceb39cb35690a7885ba39a6b60d9b7b96`; (4) congelados sin diff — verificador.py
  `3b06dff4…`, capa_deterministica.py `1f9ccc66…`, s1_fuentes.py `cf723258…`.
- Nota de cableado (instrumento intacto): la whitelist del parseo del CLI del verificador
  (línea 1037, `off|on`) rechaza el label `gate_cqn`; la corrida usó un driver que replica
  VERBATIM el loop del runner de main() (líneas 1088-1112: investigar_falla + agregar_voto,
  namespaces cv=verificador-v5.7-rep{i}) pasando el label por parámetro. Cero cambios al archivo.
- S1 con `--trace` explícito a las trazas del gate (el default del CLI deriva a off/).
