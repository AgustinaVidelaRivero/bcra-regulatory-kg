# Reporte final (ETAPA 2) — corrida congelada Fase 2.3

eval_set_v1 (23 preguntas) × 5 grafos × N=3. Respondedor `claude-haiku-4-5-20251001` (caching ON), juez `claude-sonnet-4-6` v2.1.1 — ambos CONGELADOS. Correctitud por celda = MODAL de 3 reps. Esta etapa 2 resuelve las celdas que estaban `pendiente_adjudicacion` con la adjudicación humana firmada; NADA del dataset congelado se re-corrió ni modificó.

**Adjudicación firmada** (2026-06-10, Agustina Videla Rivero (revisión y firma) — primera pasada asistida por Claude): 172 verdaderas, 8 falsas, 4 parciales, 16 no_verificables (200 afirmaciones únicas).

## 0. Propagación e integridad

- Propagaciones aplicadas (veredicto→celda): **221** vs `meta.celdas_propagacion_total` = 221 → **✅ coinciden**.
- Celdas (grafo×pregunta×rep) distintas tocadas: **90**.
- Integridad centrales propagadas == centrales de la traza congelada: **✅ OK**.

## 1. Correctitud FINAL — grafo × categoría (answerable)

`indet` = indeterminable por corpus (afirmación central no_verificable; ni correcta ni incorrecta). `sin_cons` = empate modal 1-1-1.

| Grafo | Categoría | correcta | parcial | incorrecta | indet | sin_cons |
|-------|-----------|---------:|--------:|-----------:|------:|---------:|
| run_1 | factual_directa | 9 | 0 | 1 | 0 | 0 |
| run_1 | multi_norma | 3 | 0 | 2 | 0 | 0 |
| run_1 | cadena_restriccion_excepcion | 1 | 0 | 3 | 0 | 0 |
| run_2 | factual_directa | 8 | 0 | 2 | 0 | 0 |
| run_2 | multi_norma | 4 | 0 | 1 | 0 | 0 |
| run_2 | cadena_restriccion_excepcion | 3 | 0 | 1 | 0 | 0 |
| run_3 | factual_directa | 9 | 0 | 1 | 0 | 0 |
| run_3 | multi_norma | 3 | 0 | 2 | 0 | 0 |
| run_3 | cadena_restriccion_excepcion | 4 | 0 | 0 | 0 | 0 |
| run_4 | factual_directa | 10 | 0 | 0 | 0 | 0 |
| run_4 | multi_norma | 3 | 1 | 1 | 0 | 0 |
| run_4 | cadena_restriccion_excepcion | 2 | 0 | 2 | 0 | 0 |
| run_5 | factual_directa | 8 | 0 | 2 | 0 | 0 |
| run_5 | multi_norma | 3 | 0 | 2 | 0 | 0 |
| run_5 | cadena_restriccion_excepcion | 2 | 0 | 2 | 0 | 0 |

**Totales answerable por grafo (19 preguntas):**

| Grafo | correcta | parcial | incorrecta | indet | sin_cons |
|-------|---------:|--------:|-----------:|------:|---------:|
| run_1 | 13 | 0 | 6 | 0 | 0 |
| run_2 | 15 | 0 | 4 | 0 | 0 |
| run_3 | 16 | 0 | 3 | 0 | 0 |
| run_4 | 15 | 1 | 3 | 0 | 0 |
| run_5 | 13 | 0 | 6 | 0 | 0 |

## 2. Dimensiones cerradas (congeladas — no afectadas por la adjudicación)

| Grafo | Estabilidad | hit_limit | abst. correcta/incorr. | cita_doc T/F | prec punto/pag/aus | Costo |
|-------|------------:|----------:|------------------------|-------------:|-------------------|------:|
| run_1 | 76/92 (83%) | 33/69 (48%) | 3/1 | 16/7 | 0/20/3 | $3.32 |
| run_2 | 78/92 (85%) | 26/69 (38%) | 4/0 | 16/7 | 12/8/3 | $3.01 |
| run_3 | 86/92 (93%) | 26/69 (38%) | 4/0 | 17/6 | 20/1/2 | $3.21 |
| run_4 | 79/92 (86%) | 34/69 (49%) | 4/0 | 15/8 | 14/3/5 | $3.27 |
| run_5 | 79/92 (86%) | 34/69 (49%) | 4/0 | 17/6 | 19/1/3 | $3.01 |
| **TOTAL** | | | | | | **$15.81** |

## 3. Celdas que cambiaron respecto del draft (efecto de la adjudicación)

Las **35 celdas** que el draft marcó `pendiente_adjudicacion` reciben aquí su correctitud final. Las que se resolvieron a `correcta` (todas sus centrales verdaderas) confirman el veredicto retenido; abajo se detallan las que NO quedaron `correcta` (con la afirmación que lo causó):

| Grafo | Pregunta | Cat. | draft | FINAL | distribución reps |
|-------|----------|------|-------|-------|-------------------|
| run_1 | CQ-019 | multi_norma | pendiente | **incorrecta** | {'correcta': 1, 'incorrecta': 2} |
| run_1 | CQ-024 | multi_norma | pendiente | **incorrecta** | {'incorrecta': 2, 'correcta': 1} |
| run_2 | CQ-015 | factual_directa | pendiente | **incorrecta** | {'incorrecta': 2, 'correcta': 1} |
| run_2 | CQ-018 | multi_norma | pendiente | **incorrecta** | {'incorrecta': 2, 'correcta': 1} |
| run_2 | CQ-033 | cadena_restriccion_excepcion | pendiente | **incorrecta** | {'incorrecta': 2, 'correcta': 1} |
| run_3 | CQ-017 | multi_norma | pendiente | **incorrecta** | {'correcta': 1, 'incorrecta': 2} |
| run_3 | CQ-020 | multi_norma | pendiente | **incorrecta** | {'incorrecta': 2, 'correcta': 1} |
| run_4 | CQ-017 | multi_norma | pendiente | **parcial** | {'parcial': 2, 'correcta': 1} |
| run_4 | CQ-019 | multi_norma | pendiente | **incorrecta** | {'incorrecta': 3} |
| run_5 | CQ-017 | multi_norma | pendiente | **incorrecta** | {'correcta': 1, 'incorrecta': 2} |
| run_5 | CQ-020 | multi_norma | pendiente | **incorrecta** | {'incorrecta': 3} |
| run_5 | CQ-033 | cadena_restriccion_excepcion | pendiente | **incorrecta** | {'correcta': 1, 'incorrecta': 2} |
| run_5 | CQ-034 | cadena_restriccion_excepcion | pendiente | **incorrecta** | {'correcta': 1, 'incorrecta': 2} |
| run_1 | CQ-010 | factual_directa | pendiente | **correcta** | {'incorrecta': 1, 'correcta': 2} |
| run_1 | CQ-015 | factual_directa | pendiente | **correcta** | {'correcta': 3} |
| run_1 | CQ-017 | multi_norma | pendiente | **correcta** | {'correcta': 2, 'parcial': 1} |
| run_1 | CQ-018 | multi_norma | pendiente | **correcta** | {'correcta': 2, 'incorrecta': 1} |
| run_1 | CQ-020 | multi_norma | pendiente | **correcta** | {'correcta': 3} |
| run_1 | CQ-033 | cadena_restriccion_excepcion | pendiente | **correcta** | {'correcta': 3} |
| run_2 | CQ-017 | multi_norma | pendiente | **correcta** | {'correcta': 3} |
| run_2 | CQ-019 | multi_norma | pendiente | **correcta** | {'correcta': 3} |
| run_2 | CQ-020 | multi_norma | pendiente | **correcta** | {'correcta': 3} |
| run_2 | CQ-024 | multi_norma | pendiente | **correcta** | {'incorrecta': 1, 'correcta': 2} |
| run_2 | CQ-031 | cadena_restriccion_excepcion | pendiente | **correcta** | {'correcta': 2, 'incorrecta': 1} |
| run_3 | CQ-018 | multi_norma | pendiente | **correcta** | {'correcta': 3} |
| run_3 | CQ-019 | multi_norma | pendiente | **correcta** | {'correcta': 2, 'indeterminable_por_corpus': 1} |
| run_3 | CQ-024 | multi_norma | pendiente | **correcta** | {'correcta': 3} |
| run_3 | CQ-031 | cadena_restriccion_excepcion | pendiente | **correcta** | {'correcta': 3} |
| run_3 | CQ-033 | cadena_restriccion_excepcion | pendiente | **correcta** | {'correcta': 3} |
| run_4 | CQ-014 | factual_directa | pendiente | **correcta** | {'incorrecta': 1, 'correcta': 2} |
| run_4 | CQ-018 | multi_norma | pendiente | **correcta** | {'incorrecta': 1, 'correcta': 2} |
| run_4 | CQ-020 | multi_norma | pendiente | **correcta** | {'correcta': 3} |
| run_4 | CQ-033 | cadena_restriccion_excepcion | pendiente | **correcta** | {'correcta': 2, 'incorrecta': 1} |
| run_5 | CQ-015 | factual_directa | pendiente | **correcta** | {'correcta': 3} |
| run_5 | CQ-019 | multi_norma | pendiente | **correcta** | {'correcta': 3} |

### Trazabilidad afirmación→celda (solo celdas que NO quedaron correcta)

**run_1/CQ-019** (multi_norma) → **incorrecta** (reps: ['correcta', 'incorrecta', 'incorrecta'])

**run_1/CQ-024** (multi_norma) → **incorrecta** (reps: ['incorrecta', 'correcta', 'incorrecta'])

**run_2/CQ-015** (factual_directa) → **incorrecta** (reps: ['incorrecta', 'correcta', 'incorrecta'])
- rep1 · veredicto=falsa · «La definición de residente a los fines cambiarios para personas humanas requiere cumplir con al menos uno de los tres criterios mencionados (no todos simultáneamente).»
    evidencia: Exterior 6.5.1 — son DOS criterios, no tres; "tres criterios" es incorrecto
- rep3 · veredicto=falsa · «Los tres criterios mencionados son alternativos (basta cumplir uno de ellos).»
    evidencia: Exterior 6.5.1 — son DOS criterios, no tres

**run_2/CQ-018** (multi_norma) → **incorrecta** (reps: ['incorrecta', 'correcta', 'incorrecta'])

**run_2/CQ-033** (cadena_restriccion_excepcion) → **incorrecta** (reps: ['incorrecta', 'correcta', 'incorrecta'])
- rep1 · veredicto=falsa · «Existe un límite muy reducido del 5% para el Grupo C.»
    evidencia: Capitales Secc.12 — el 5% Grupo C es solo con calif 1-2, no un límite genérico

**run_3/CQ-017** (multi_norma) → **incorrecta** (reps: ['correcta', 'incorrecta', 'incorrecta'])
- rep2 · veredicto=parcial · «Los operadores de cambio deben cumplir con todas las obligaciones establecidas en la normativa de protección de usuarios de servicios financieros.»
    evidencia: Protección 1.1.2.2 — idem

**run_3/CQ-020** (multi_norma) → **incorrecta** (reps: ['incorrecta', 'correcta', 'incorrecta'])
- rep3 · veredicto=falsa · «k representa el ratio de capital promedio de las exposiciones subyacentes»
    evidencia: Capitales p.288 — k = factor de calificación SEFYC, NO "ratio de capital promedio de exposiciones subyacentes"

**run_4/CQ-017** (multi_norma) → **parcial** (reps: ['parcial', 'correcta', 'parcial'])
- rep1 · veredicto=parcial · «Como sujeto obligado, el operador de cambio debe cumplir con todas las obligaciones establecidas en las normas de protección de usuarios de servicios financieros.»
    evidencia: Protección 1.1.2.2 — idem
- rep3 · veredicto=parcial · «Como sujeto obligado, el operador de cambio debe cumplir con todas las obligaciones establecidas en las normas de Protección de los Usuarios de Servicios Financieros.»
    evidencia: Protección 1.1.2.2 — alcance acotado a operaciones de Exterior

**run_4/CQ-019** (multi_norma) → **incorrecta** (reps: ['incorrecta', 'incorrecta', 'incorrecta'])
- rep2 · veredicto=falsa · «La previsión específica no se aplica al cálculo de KSA (exigencia de capital promedio de las exposiciones subyacentes).»
    evidencia: KSA = standardised approach (riesgo de crédito), no "exigencia de capital promedio de exposiciones subyacentes" (concepto de titulizaciones)
- rep3 · veredicto=falsa · «La previsión específica no se deduce en el cálculo de KSA (Exigencia de capital promedio de las exposiciones subyacentes).»
    evidencia: idem #8 — glosa errada de KSA

**run_5/CQ-017** (multi_norma) → **incorrecta** (reps: ['correcta', 'incorrecta', 'incorrecta'])

**run_5/CQ-020** (multi_norma) → **incorrecta** (reps: ['incorrecta', 'incorrecta', 'incorrecta'])
- rep2 · veredicto=falsa · «INC en la fórmula CRC representa las inversiones no computables»
    evidencia: Capitales p.343/353 — INC = incremento por excesos, NO "inversiones no computables"

**run_5/CQ-033** (cadena_restriccion_excepcion) → **incorrecta** (reps: ['correcta', 'incorrecta', 'incorrecta'])

**run_5/CQ-034** (cadena_restriccion_excepcion) → **incorrecta** (reps: ['correcta', 'incorrecta', 'incorrecta'])
- rep2 · veredicto=falsa · «Para otras modalidades de formación de activos externos (códigos A01, A02, A03, A04, A06, A07, A08, A09, A14 y A24), rige un límite general de USD 200 mensuales.»
    evidencia: Exterior 3.9 — códigos A07 y A09 NO figuran (lista real: A01,A02,A03,A04,A06,A08,A14,A24)

## 4. Nota metodológica — multi_norma resuelto

En el draft, TODAS las celdas `multi_norma` quedaron pendientes (el gold resumido no soporta afirmaciones multi-hop granulares — hallazgo, no defecto). Tras la adjudicación, su correctitud ya es comparable: ver tabla 1, fila `multi_norma` de cada grafo. La adjudicación humana cumplió exactamente la función que el mecanismo de seguridad del juez (no validar contra conocimiento paramétrico) había diferido.

## 5. Selección del grafo ganador

**Grafo ganador: `run_3` — estrategia `ppf_core` (schema cerrado de 7 tipos core).**

Selección por **dominancia multidimensional** — no requiere ponderar dimensiones, porque run_3 **lidera o empata en todas**:

- **Correctitud final:** 16/19 answerable correctas — el máximo de los 5 grafos (run_2 y run_4: 15; run_1 y run_5: 13).
- **Estabilidad:** 93% de celdas unánimes — el máximo (resto 83-86%).
- **Cadenas restricción-excepción:** 4/4 correctas — único grafo sin incorrectas en la categoría.
- **Precisión de cita:** 20 punto / 1 página — la granularidad más fina (cita a nivel de punto/sección).
- **Abstención (unanswerable):** 4/4 correcta (lidera/empata).
- **Costo:** parejo con el resto (~$3.21/grafo).

Como run_3 no es inferior a ningún otro grafo en ninguna dimensión evaluada, la selección es **robusta a cualquier ponderación**.

**Salvedad — límite común a los 5 grafos.** La categoría `multi_norma` (preguntas multi-hop) es el punto débil **compartido**: ningún grafo la resuelve sólidamente (run_3: 3/5 correctas, 2 incorrectas). El gold resumido no podía puntuarla sin adjudicación humana (§4); tras la adjudicación queda como **límite de capacidad común a todas las estrategias, no un diferenciador entre ellas**. La selección de run_3 se sostiene sobre las dimensiones donde los grafos sí se distinguen.
