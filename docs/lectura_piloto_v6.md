# Lectura del piloto v6.0-D — corrida única sobre 5 casos frescos

**Fecha:** 2026-07-16. **Protocolo:** `docs/protocolo_piloto_v6.md` + Enmienda v1.1 (marco
POST-HOC). **Vara:** `.claude/skills/kg-refinement/references/casos_piloto.md`, adjudicada
ANTES de la corrida (sellado por inexistencia) y commiteada como guarda. **Extracción
completa de la corrida:** `docs/evidencia_piloto/resultados_piloto.md` (votos, atribuciones
íntegras por rep, anotaciones de la capa, costos).

## 1. Qué es

La lectura de la **corrida única** del piloto: el compuesto v6.0-D (verificador v5.7
congelado, N=3 + voto, + capa determinística) sobre **5 casos frescos de run_3** que el
instrumento nunca vio — su primera validación prospectiva. **Costo real: 4.179.672 tokens de
input** (vs ~6M estimados). **15/15 repeticiones válidas, cero fallas operativas.**

## 2. Scoring contra la vara (reglas del gate, sobre `voto_capa_d`)

| Caso | Voto v5.7 original | voto_capa_d (compuesto) | Canal | Scoring |
|---|---|---|---|---|
| CQ-019 | mayoría clave vacía 3-0 | mayoría clave vacía 3-0 | triage (R1) | **ACIERTO** |
| CQ-016 | dividido 1-1-1 | frontera_no_determinada | triage (R4) | **TRIAGE** |
| CQ-024 | mayoría {context_recall, alcanzabilidad_kg} 2-1 | ídem **3-0** (D2 unificó) | triage (R3) | **MISS por voto — derivado** |
| CQ-018 | mayoría {noise_sensitivity, contenido_kg} 2-1 | ídem | **automático** | **MISS — silencioso #1** |
| CQ-033 | mayoría {noise_sensitivity, contenido_kg} 2-1 | ídem | **automático** | **MISS — silencioso #2** |

- **CQ-019 — ACIERTO.** Sin primarias, unánime 3-0: las 3 reps emitieron el caso como
  `sin_defecto` citando el portador correcto. Canal: **triage R1** (`exoneracion_total`) —
  el costo de la política conservadora: una revisión humana pagada por una exoneración
  correcta. **Primer dato de la métrica de la enmienda E4.**
- **CQ-016 — TRIAGE.** Voto dividido 1-1-1 (`flag_voto_dividido=true` → R4): derivación a
  revisión humana por regla del protocolo.
- **CQ-024 — MISS por voto, DERIVADO.** `{context_recall, alcanzabilidad_kg}` 3-0 contra el
  GT de exoneración (control negativo). Canal: **triage R3**
  (`modulo_deterministico_sin_decision`) → el caso llega derivado a revisión humana, **no
  silencioso**.
- **CQ-018 — MISS, canal AUTOMÁTICO: error silencioso #1.** Mayoría
  `{noise_sensitivity, contenido_kg}` como primaria contra el GT sin-primaria (los 4 claims
  reprobados son falsos positivos del juez según la vara). Es **el único desacuerdo
  sustantivo humano-instrumento del piloto**: la lectura des-scoping vs FP sobre el nodo del
  criterio básico — con la vara sellada previa a la corrida.
- **CQ-033 — MISS, canal AUTOMÁTICO: error silencioso #2.** El instrumento emitió la causa y
  el nodo **EXACTOS** de la vara (`{noise_sensitivity, contenido_kg}` sobre el nodo
  des-scopeado del 12.3) — pero como **PRIMARIA**, donde la vara los adjudica secundaria
  (cero centrales reprobados). Error **de jerarquía, no de sustancia**.

**AGREGADO: 1 acierto · 1 triage · 3 miss (2 silenciosos, 1 derivado).**

**Comparación capa vs. v5.7 pelado:** la capa corrigió CQ-024 (D2: 2-1 → 3-0, con 1
discrepancia; más el triage R3), agregó los triage R1/R4, y no alteró los demás votos —
**cero discrepancias D2 en CQ-016/018/019/033**.

## 3. Tablero de la corrida

| Contador | Valor |
|---|---|
| Triage por motivo | R1 ×1 (CQ-019) · R3 ×1 (CQ-024) · R4 ×1 (CQ-016) · R2 ×0 · R5 ×0 |
| Discrepancias D2 | **1** (CQ-024; además 2 atribuciones corregidas y 1 `sin_portador_extraible` → R3) |
| Banderas D5 | **0** |
| Quotes D3 | **0 anotaciones** (cero emisiones `aplicacion_erronea` en la corrida) |
| **Métrica nueva (E4)** | **1 revisión humana pagada por una exoneración correcta** (CQ-019 vía R1) |

## 4. Hallazgos

**a. La frontera semántica del des-scoping concentra los DOS errores silenciosos.** CQ-018
(des-scoping vs FP) y CQ-033 (des-scoping real, jerarquía equivocada) caen ambos en la
frontera `contenido_kg ↔ sin_defecto ↔ jerarquía`. Esa frontera **no es computable** —
decidir si un contenido es general o scopeado exige leer el PDF — y **no está cubierta por la
capa** (R2 cubre solo `aplicacion_erronea`). Lo dejo escrito como **límite medido del enfoque
determinístico**: la capa elimina los errores de frontera computable; los de frontera
semántica persisten.

**b. Sobre-atribución ante síntoma vacío.** En los dos controles negativos el instrumento
**inventó defectos** (2/3 reps en CQ-016; 3/3 en CQ-024) — apuntando, notablemente, a huecos
reales del backlog (el hecho identitario del R.I.C.M.; ver `casos_piloto.md`) — pero atribuir
sin falla declarada es **comportamiento incorrecto para el rol del instrumento**: su tarea es
atribuir la falla que el juez declaró, no auditar el grafo de oficio. El triage los atrapó
**por reglas no diseñadas para esto** (R4 por división de voto; R3 por un portador ilegible):
suerte estructural, no diseño.

**c. Jerarquía en casos de solo-secundarios.** La taxonomía no define la jerarquía cuando el
único claim reprobado es secundario; la convención que apliqué en la vara (la severidad de la
atribución no excede la del síntoma) quedó escrita **después del congelamiento del
instrumento** — el instrumento no podía conocerla. El miss de CQ-033 es, en parte, la factura
de ese hueco normativo.

**d. Lectura de propósito.** Para el enrutamiento del refinamiento — el fin del pipeline —,
CQ-033 **enruta la reparación CORRECTA** (nodo y arreglo exactos; el miss es de etiqueta
jerárquica); **ningún defecto real de grafo se perdió**; y el backlog recibió **3 ítems
verificados**. El error dañino para el propósito (una reparación equivocada enrutada en
silencio) ocurrió **una vez: CQ-018**.

## 5. Correcciones derivadas (por mecanismo — ninguna contra estos 5 casos; regla de frenado respetada)

- **D6 (a implementar; el compuesto pasa a v6.1-D):**
  - **R6a** — síntoma vacío + atribución de defecto ⇒ triage («atribución sin síntoma»).
  - **R6b** — la jerarquía de una atribución queda acotada por la centralidad del claim
    reprobado al que se liga: primaria exige un central reprobado; ligada solo a secundarios
    ⇒ se degrada a secundaria.

  **Justificación estructural, no empírica sobre estos casos:** la severidad de la
  atribución no puede exceder la del síntoma declarado — un hecho del INPUT del instrumento,
  computable por código. Los casos del piloto solo **ilustran** el mecanismo (con asterisco:
  lo motivaron); la **validación empírica queda pre-registrada** sobre fallas de run_2/run_4
  — grafos vírgenes de todas las etapas — y material futuro de anotación humana.

- **Roadmap v7 (post-cierre):** una tool determinística `ver_fuente(provenance)` que entregue
  al LLM el **pasaje verbatim del PDF con su encabezado de sección** — retrieval computable,
  para que el juicio semántico (¿general o scopeado?) se haga **sobre el texto fuente** en
  vez de sobre memoria. Exige instrumento nuevo y calibración con material fresco; queda
  fuera del alcance actual.

## 6. Disclosure

- **Corrida única** conforme al protocolo (§5): sin iteración, sin segunda corrida; guarda
  del paso 0 verificada (commit de la vara en HEAD) antes de ejecutar.
- **Vara sellada por inexistencia:** adjudicada y commiteada antes de que existiera veredicto
  alguno del compuesto sobre estos casos.
- **Estos 5 casos quedan QUEMADOS** — como los del gate: cualquier cambio derivado (D6, v7)
  se valida sobre material que este piloto no tocó.
- El scoring usa las **reglas pre-registradas sin excepción** — incluido que los dos miss
  silenciosos se reportan como tales aunque la lectura de propósito (§4d) los matice.
