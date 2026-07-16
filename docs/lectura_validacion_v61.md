# Lectura de la validación de v6.1-D — corrida única sobre run_2 y run_4

**Fecha:** 2026-07-16. **Protocolo:** `docs/protocolo_validacion_v61.md`. **Vara:**
`.claude/skills/kg-refinement/references/casos_validacion.md`, adjudicada antes de la corrida
(sellado por inexistencia) y commiteada como guarda. **Extracción completa:**
`docs/evidencia_validacion/resultados_validacion.md`.

## 1. Qué es

La lectura de la **corrida única** de la validación: el compuesto **v6.1-D** (verificador
v5.7 congelado, N=3 + voto, + capa determinística con D6) sobre **8 casos de run_2 y run_4**
— grafos jamás usados en dev, gates ni piloto. **Costo real: 5.896.712 tokens de input /
187.266 de output. 24/24 repeticiones válidas, cero fallas operativas.**

## 2. Scoring contra la vara (reglas del gate, sobre `voto_capa_d`)

| Caso | Voto v5.7 | voto_pre_d6 | voto_capa_d final | Canal | Scoring |
|---|---|---|---|---|---|
| r2/CQ-015 | clave vacía 2-1 | ídem | ídem | derivado (R1+R6a) | **ACIERTO** |
| r4/CQ-014 | clave vacía 3-0 | ídem | ídem | derivado (R1) | **ACIERTO** |
| r2/CQ-025 | navegación 3-0 | alcanzabilidad 3-0 (D2) | alcanzabilidad 3-0 | derivado | **MISS — derivado** |
| r2/CQ-019 | navegación 2-1 | ídem | ídem | derivado | **MISS — derivado** |
| r2/CQ-018 | contenido_kg 2-1 | ídem | ídem | derivado | **MISS — derivado** |
| r4/CQ-017 | estructural_kg 2-1 | ídem | ídem | **automático** | **MISS — SILENCIOSO** |
| r4/CQ-019 | navegación 2-1 | ídem | ídem | derivado | **MISS — derivado** |
| r4/CQ-020 | clave vacía 2-1 | ídem | ídem | derivado (R1) | **MISS — derivado** |

- **r2/CQ-015 — ACIERTO** (clave vacía 2-1): canal derivado por R1+R6a. **R6a disparó POR
  DISEÑO** sobre las invenciones de la rep minoritaria — el control negativo hizo exactamente
  el trabajo para el que se lo diseñó.
- **r4/CQ-014 — ACIERTO** (clave vacía 3-0): derivado por R1; **cero anotaciones D6** —
  control limpio de punta a punta.
- **r2/CQ-025 — MISS derivado:** `alcanzabilidad_kg` 3-0 — **D2 corrigió las 3 reps de
  navegación citando, entre otros, el portador trimestral real** — contra el GT
  `contenido_kg`; motivos `atribucion_no_verificable` + R2. **Crédito parcial de propósito:**
  el voto enruta la reparación del defecto SECUNDARIO real de la vara.
- **r2/CQ-019 — MISS derivado:** navegación 2-1 contra `alcanzabilidad_kg`; R6b-fallback +
  R3/`sin_portador` — el portador real es léxicamente inalcanzable **también para la
  investigación del propio verificador**.
- **r2/CQ-018 — MISS derivado:** `contenido_kg` 2-1 contra completitud-emisoras;
  R6b-fallback ×3 — **la lectura des-scoping del verificador, idéntica a la del piloto sobre
  la misma pregunta en run_3**.
- **r4/CQ-017 — MISS AUTOMÁTICO, EL ÚNICO ERROR SILENCIOSO:** `estructural_kg` 2-1 contra
  `completitud_kg`; triage vacío. **Frontera de etiqueta estructural/completitud, no
  cubierta por la capa.**
- **r4/CQ-019 — MISS derivado:** navegación 2-1 contra `aplicacion_erronea`;
  R2+R3+R6b/`context_recall_sin_pata` ×5. **LA PERLA: la rep 1 emitió `aplicacion_erronea`
  como primaria** — el primer ejemplar genuino de la categoría fue VISTO por el instrumento
  y **perdido por el voto 2-1**: varianza de sampling decidiendo en contra.
- **r4/CQ-020 — MISS derivado:** clave vacía 2-1 contra completitud-frecuencia; R1 —
  **sobre-exoneración, el patrón del gate reapareciendo.**

**AGREGADO: 2 aciertos · 6 miss (1 silencioso, 5 derivados). Acuerdo compuesto-humano: 2/8.
Sobre los 6 casos con síntoma: 0/6.**

## 3. Tablero con tasas (verificado contra la extracción)

| Contador | Valor | Tasa |
|---|---|---|
| Triage por motivo | R1 ×3 (CQ-015, CQ-014, r4/CQ-020) · R2 ×2 (r2/CQ-025, r4/CQ-019) · R3 ×2 (r2/CQ-019, r4/CQ-019) · R6a ×1 (CQ-015) · `atribucion_no_verificable` ×4 (r2/CQ-018, r2/CQ-019, r2/CQ-025, r4/CQ-019) | triage en 7/8 casos |
| `atribucion_no_verificable` | **4 de los 6 casos con síntoma** | 4/6 |
| Discrepancias D2 | **3** (r2/CQ-025 ×3 — navegación→alcanzabilidad, portador trimestral real) | — |
| `sin_portador_extraible` (D2, → R3) | **7 anotaciones** (r2/CQ-019 ×3; r4/CQ-019 ×4) | — |
| Banderas D5 | **0** | — |
| Anotaciones D3 | **3** (0 quotes no verificados) | — |
| **Costo de política (E4)** | **2 revisiones humanas pagadas por exoneraciones correctas** (los dos controles, vía R1/R6a) | 2/8 |

## 4. Hallazgos

**a. El instrumento LLM no generaliza entre esquemas de grafo.** Calibrado sobre material de
run_1/run_3/run_5, su precisión de atribución sobre run_2/run_4 fue **0/6**. Y sus modos de
error son los MISMOS que medí en el gate: sesgo a `navegación` (3 de los 6 votos),
sobre-exoneración (r4/CQ-020), lectura des-scoping (r2/CQ-018) — es decir, **limitaciones
consistentes del componente LLM que, fuera de la distribución de calibración, dominan el
resultado**. Lo dejo escrito como hallazgo central para el uso de LLM-as-judge en
atribución de fallas.

**b. La contención sostuvo.** 5 de los 6 errores salieron **derivados con motivo explícito**;
**R6a quedó VALIDADA POR DISEÑO** en los dos controles (disparó sobre las invenciones de
CQ-015 y no tuvo nada que anotar en CQ-014); `context_recall_sin_pata` cazó atribuciones
sintomáticamente imposibles en dos casos. **Un solo silencioso en ocho.**

**c. El silencioso es una frontera parcialmente computable.** `estructural_kg` vs
`completitud_kg` (¿faltan las piezas o falta el puente?) se decide en parte con un barrido:
**verificar la existencia de las piezas es computable** — candidata a **módulo D7**, por
mecanismo, a diseñar después y validar sobre material fresco (**nunca contra estos 8**).

**d. La tasa de `atribucion_no_verificable` es alta (4/6): se cumple la condición
pre-registrada.** El mapeo quote↔claim de R6b **se rediseña POR MECANISMO** (matching por
contención flexible u otro método determinístico, diseñado sobre material sintético o
fresco); va al roadmap.

**e. Límite de uso, escrito:** v6.1-D es confiable como **ENRUTADOR** sobre grafos de la
familia de calibración y como **DERIVADOR CONSERVADOR** fuera de ella; **el canal automático
sobre esquemas nuevos exige recalibración del componente LLM (o v7)**. La cobertura del
pipeline a escala queda condicionada a esa recalibración.

**f. Para el refinamiento de run_3** — el grafo ganador, el objetivo real del pipeline — la
entrada ya existe con calidad superior a cualquier salida automática: las varas adjudicadas
del gate y el piloto, más el backlog acumulado de hallazgos verificados contra PDF.

## 5. Correcciones derivadas y roadmap (por mecanismo; regla de frenado respetada)

Nada se ajusta contra estos 8 casos. Derivado de esta lectura:

- **Rediseño del mapeo de R6b** (condición pre-registrada cumplida) — determinístico, sobre
  material sintético/fresco.
- **D7 candidata:** existencia de piezas para la frontera estructural/completitud.
- **v7 con `ver_fuente`** — ahora con **DOS motivaciones medidas**: la frontera semántica del
  piloto y la falla de generalización de esta validación.
- **Recalibración multi-esquema** como requisito de uso del canal automático fuera de la
  familia de calibración.
- **La reserva v7 (r2/CQ-021, r4/CQ-008, r4/CQ-021, r4/CQ-028) permanece INTOCADA.**

## 6. Disclosure

- **Corrida única** conforme al protocolo, con la guarda del paso 0 verificada (commit de la
  vara en HEAD) antes de ejecutar.
- **Vara sellada por inexistencia**, commiteada antes de que existiera veredicto alguno.
- **Los 8 casos quedan QUEMADOS** — cualquier corrección derivada se valida sobre material
  que esta validación no tocó.
- El scoring usa las **reglas pre-registradas sin excepción** — los cinco miss derivados se
  reportan como miss aunque la lectura por canal los matice.
- Nota operativa: el loop de shell del PASO 2 se re-ejecutó corregido tras un error de
  word-splitting (la capa es determinística y pura, sin API — no constituye re-corrida del
  instrumento); registrado en la extracción.
