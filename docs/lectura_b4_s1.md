# Lectura de B4 — el desarrollo de S1 contra la vara de dev

**Fecha:** 2026-07-17. **Diseño:** `docs/diseno_v7_s1.md` (§4: DEV = la reserva
pre-registrada, iterable). **Vara de dev:** `.claude/skills/kg-refinement/references/casos_dev_v7.md`
(adjudicada y commiteada ANTES de correr nada sobre estos casos). **Evidencia completa:**
`docs/evidencia_v7/` (resultados_s1_v01.md, resultados_s1_v01b.md, resultados_s1_v02.md,
resultados_s1_v03.md, resultados_s1_n3.md, resultados_s1_v031.md).

## 1. Qué es

La fase de DESARROLLO de S1 contra la vara de dev — el material que el diseño §4 declaró
iterable: los 4 casos de la reserva (run_2/CQ-021, run_4/{CQ-008, CQ-021, CQ-028}),
incluida la corrida v6.1-D de entrada que les dio su primera pasada.

**Punto de partida (v6.1-D sobre el dev, leído contra la vara):** 2 aciertos de
confirmación (r2/CQ-021 y r4/CQ-008, completitud primaria) + 2 miss derivados —
**sobre-exoneración** en r4/CQ-021 (clave vacía 3-0 con síntoma, atrapada por R1) y
**síntoma equivocado de raíz** en r4/CQ-028 ({context_recall, completitud_kg} 2-1 donde la
vara adjudica {noise_sensitivity, contenido_kg}, atrapada por R6b). **Cero silenciosos**:
la contención de v6.1-D volvió a sostener.

## 2. Historia B4.1 → B4.5 (una entrada por unidad, con su hallazgo)

- **B4.1 — primera corrida de s1-v0.1 (la versión commiteada, sin iterar).** El mecanismo
  completo funcionó de punta a punta DONDE EL FETCH LLEGÓ (4 llamadas: 1 confirmación de
  completitud, 3 confirmaciones de exoneración). Hallazgo: **11 de 15 gatilladas cayeron
  en fetch fallido** por dos mecanismos del corpus/vocabulario — ids ANIDADOS del kg
  (run_4 tiene un nodo `comision` ⊂ `comision_por_precancelacion`; la regla heredada de
  D2 "más de un id → sin desempate" mataba portadores claramente citados) y provenances
  de PREÁMBULO que parsean pero no localizan ("Sección 3 — preámbulo" → carátula).
  (`docs/evidencia_v7/resultados_s1_v01.md`)
- **B4.2 — correcciones determinísticas al fetch** (match MAXIMAL para anidación — resuelve
  anidación, no ambigüedad real —; provenances en CASCADA; usage real persistido). Fetch
  fallidos **11 → 7**, juzgadas 4 → 8, **CQ-028 desbloqueada** y con ella las primeras
  correcciones de la frontera semántica. Costo medido: 27.990/3.642 tokens.
  (`docs/evidencia_v7/resultados_s1_v01b.md`)
- **B4.3 ronda 1 — síntoma en el input y en el esquema + rama de exoneración**
  (s1-v0.2-dev). Con las marcas del juez a la vista, CQ-028 emite el **PAR COMPLETO**
  {noise_sensitivity, contenido_kg} y su voto pasa de dividido a mayoría 2-1; las 3
  exoneraciones de r4/CQ-021 salen corregidas sin_defecto → completitud_kg **citando
  verbatim la cláusula que el nodo amputó** ("…siendo optativo cuando el saldo de deuda
  sea inferior…") — **sin ver jamás el GT del eval set** (el prompt de la rama recibe
  pata + respuesta del agente + portador + pasajes del fetch, nada más).
  (`docs/evidencia_v7/resultados_s1_v02.md`)
- **B4.3 ronda 2 — regla mecánica de jerarquía para exoneraciones corregidas**
  (s1-v0.3-dev; espejo estructural de R6b: la severidad acotada por el síntoma). Replay
  puro sobre las salidas congeladas — **cero tokens**: el voto de r4/CQ-021 pasa de vacío
  a {context_recall, completitud_kg} 3-0. (`docs/evidencia_v7/resultados_s1_v03.md`)
- **B4.4 — medición de varianza (N=3, 24 llamadas frescas, 90.429/11.102 tokens).**
  Fetch determinístico **byte-idéntico 4/4** (SHA-256, doble corrida) — toda la varianza
  es del componente LLM, y vive **SOLO en la frontera semántica** (CQ-028: dos 2/1 y una
  dispersa; el resto 3/3 estable, incluida una **abstención estable** 3× no_determinable
  en CQ-008). **Votos por caso idénticos entre N=1 y N=3 en los 4 casos.**
  (`docs/evidencia_v7/resultados_s1_n3.md`)
- **B4.5 — guardas determinísticas de salida** (s1-v0.3.1-dev): validación de dominio
  contra el vocabulario cerrado de la taxonomía (con la muestra real de "síntoma en el
  campo de causa" re-clasificada `fuera_de_dominio`) y tope de salida 2× el máximo
  observado. Replay sin API; ningún voto cambió. (`docs/evidencia_v7/resultados_s1_v031.md`)

## 3. Diagnóstico final de dev — CON ASTERISCO GRANDE

Bajo s1-v0.3.1-dev con N=3, el voto de S1 coincide con la vara de dev en **4/4 casos**:
2 confirmados (r2/CQ-021 vía triage de fetch + voto v6.1-D intacto; r4/CQ-008 confirmado
3/3) + 2 corregidos (r4/CQ-021 sobre-exoneración → completitud primaria 3-0; r4/CQ-028
síntoma y causa → {noise_sensitivity, contenido_kg} 2-1).

**EL ASTERISCO:** este material fue ITERADO — el prompt, el esquema y las reglas se
ajustaron mirando estos 4 casos, que es exactamente lo que el diseño §4 permite y por lo
que este número NO es evaluación. **El juicio de v7 es el gate CQN, sellado y pendiente.**

## 4. El mecanismo de dos capas, confirmado terapéuticamente

El diagnóstico de B1c dijo: (capa 1) fuera de la familia de calibración el instrumento no
llega a leer el pasaje decisivo; (capa 2) dentro de la familia lo lee y no lo usa. B4 lo
validó POR SU TRATAMIENTO: la capa 1 la resolvió el **fetch determinístico** (el pasaje
decisivo llega por código, no por elección del LLM — r4/CQ-021 corrigió porque el 3.4.2
completo viajó en el paquete), y la capa 2 la resolvió el **esquema que obliga la
comparación** (CQ-028 corrigió cuando el síntoma y los alcances quedaron uno al lado del
otro). Un diagnóstico que su terapia confirma.

## 5. Políticas de cierre (ratificadas)

- **N=3 con voto para el gate.** Costo medido ~23K tok de input por caso (~2% del costo
  del verificador por caso); la varianza vive exactamente en la frontera semántica que el
  head-to-head quiere medir — N=3 compra estabilidad donde importa.
- **Triage-por-fetch conservador.** Los 7 fallos remanentes de fetch son ambigüedad REAL
  del vocabulario o ausencia genuina de portador (r2/CQ-021: ubicaciones "negativas" y
  múltiples nodos citados de verdad) — se derivan con motivo `fuente_no_verificable`, no
  se adivinan. Costo documentado de la política: veredictos automáticos correctos pagando
  revisión (el patrón E4 de siempre).
- **Guardas de dominio activas** (vocabulario cerrado + tope de salida).

## 6. Costos medidos de B4 completo

| Unidad | Tokens (in/out) |
|---|---|
| Corrida v6.1-D del dev (12 reps) | 5.495.370 / 103.285 |
| B4.1 (4 llamadas S1; usage no instrumentado aún — estimación) | ~7,8K / ~1,1K |
| B4.2 re-corrida (8 juzgadas, usage medido) | 27.990 / 3.642 |
| B4.3 r1 re-corrida | 30.143 / 3.434 |
| B4.3 r2 + B4.5 (replays) | **0 / 0** |
| B4.4 (N=3, 24 llamadas) | 90.429 / 11.102 |

S1 completo costó **~156K tokens de input** — el 2,8% de la corrida del verificador que lo
alimenta. **Rondas de iteración usadas: 1,5 de las 3 previstas** (la ronda 2 fue regla
mecánica a costo cero) **+ la micro-ronda de guardas** — la regla de frenado se respetó:
todo lo motivado por el dev se valida sobre material que el dev no tocó.

## 7. Lo que B4 NO prueba

- **Generalización.** El dev son 4 casos sobre 2 grafos, y fue iterado. Nada de lo de
  arriba dice cómo le va a S1 sobre fallas frescas.
- **La frontera semántica sigue siendo el lugar de la varianza** (CQ-028: 2/1, 2/1 y una
  dispersión 1/1/1). El esquema la estabilizó lo suficiente para votar; no la eliminó.
- **El único número que cuenta es el gate CQN:** fallas frescas de run_3 sobre el eval set
  de generación ciega (`queries/eval_set_cqn.json`), **adjudicadas y selladas antes de que
  NINGUNA versión del verificador o de S1 las vea**, con head-to-head pre-registrado
  v6.1-D vs v7 sobre el mismo material y estratos pre-registrados (11 primarias / 3
  solapadas con disclosure / 1 ilustrativa fuera de métricas).
