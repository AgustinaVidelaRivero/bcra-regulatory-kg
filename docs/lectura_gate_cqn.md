# Lectura del gate CQN — head-to-head v6.1-D vs v7 (S1)

**Fecha:** 2026-07-18. **Vara:** `docs/casos_gate_cqn.md` (commit `1d4e7a8`, sellada por
inexistencia ANTES de toda corrida). **Extracción de la corrida:**
`posthoc_run/dev_set/extraccion_head_to_head.md` (mecánica, sin scoring — el scoring de
este documento es mío, contra la vara). Los 30 JSONs congelados: `posthoc_run/gate_h2h/`.
Todo número de este documento está copiado de esas fuentes, no recalculado.

## 1. Diseño y custodia

- **El eval set CQN** fue generado a ciegas por una instancia sin acceso al repo, con
  custodia verificada, y quedó **sellado** en `2b8d449`; la corrida del sistema usó el
  **derivado de corrida** `eval_set_cqn_runtime.json` (`89f693d`, blob
  `7486b2fceb39cb35690a7885ba39a6b60d9b7b96`), que solo duplica un campo por contrato del
  juez.
- **La vara** se adjudicó sobre expediente con fidelidad 132/132 y barrido determinístico
  del kg, y se commiteó (`1d4e7a8`) ANTES de que existiera veredicto alguno del
  verificador o de S1 sobre estos casos.
- **La guarda del paso 0 (4 checks) FUNCIONÓ como evidencia, no solo como rito:** el
  primer lanzamiento del head-to-head **ABORTÓ en el paso 0** porque la vara aún no
  estaba commiteada — cero corridas, cero contaminación. La corrida válida ocurrió
  únicamente con el commit en HEAD, con los 4 checks impresos (status limpio; vara en
  HEAD; igualdad de blob del runtime; congelados sin diff, con hashes en el sello de la
  extracción).

## 2. Scoring por estratos (contra la vara, reglas de acierto de la vara §c)

**Primaria (6 casos):**

| Caso | v6.1-D | v7 (S1) |
|---|---|---|
| CQN-006 | **ACIERTO** (exoneración [] 3-0; R1 = enrutamiento esperado) | **ACIERTO** (ídem; triage_s1 por no_determinable ×3) |
| CQN-007 | **MISS SILENCIOSO** (alcanzabilidad_kg 3-0, sin triage) | **MISS SILENCIOSO** (ídem; S1 sin gatillo) |
| CQN-009 | **ACIERTO** (completitud_kg 3-0) | **ACIERTO** (ídem) |
| CQN-010 | **MISS** (exoneración [] 3-0, con flag R1; nota estructural §4) | **MISS** (ídem) |
| CQN-011 | **TRIAGE** (dividido 1-1-1, R4) | **TRIAGE** (dividido 1-1-1) |
| CQN-013 | **ACIERTO** (aplicacion_erronea 2-1; triage R2 esperado) | **MISS SILENCIOSO** (S1 corrigió 3/3 → {faithfulness, contenido_kg}; triage_s1=False) |

**Tabla resumen primaria: v6.1-D = 3 aciertos, 2 miss, 1 triage (1 silencioso) · v7 = 2
aciertos, 3 miss, 1 triage (2 silenciosos).**

**Solapadas (aparte, con su disclosure):**

- **CQN-001:** triage / triage (dividido 1-1-1 en ambos; R2+R3+R6b+R4 en v6.1-D,
  fuente_no_verificable en S1).
- **CQN-012:** miss / miss — ambos emitieron {context_recall, completitud_kg}: **la causa
  concurrente de la vara con un síntoma que no se manifestó** (la primaria adjudicada es
  aplicacion_erronea).
- **CQN-014:** miss-con-flag / miss-con-flag — la secundaria navegación como voto (2-1);
  D2 `sin_portador_extraible` en v6.1-D / fetch fallido en S1, **con la política
  conservadora sosteniendo** (derivación con motivo, no silencio).

**CQN-008 (ilustrativa, fuera de métrica):** {context_recall, navegación} 3-0 en ambos
sistemas — registro descriptivo, no puntúa.

## 3. Los tres hallazgos

**(i) S1 v0.3.1 NO pasó su gate.** Contra la vara fresca: **cero aciertos nuevos sobre
v6.1-D y una degradación SILENCIOSA** — CQN-013, donde v6.1-D acertó (aplicacion_erronea
2-1, con el triage R2 esperado) y S1 lo dio vuelta con confianza: 9/9 salidas idénticas
`coinciden=no` → {faithfulness, contenido_kg}, corrigió las 3 reps y **apagó el triage**
(triage_s1=False). El mecanismo: el fetch salió `completo` con la fuente en OTRO
documento — pregunta de Protección, portador con provenance de Exterior (el nodo del
art. 41; vara CQN-013 §3) — **sin que ninguna guarda de dominio lo bloqueara**, y el
juicio, leyendo un pasaje real de Exterior que sí contiene el art. 41, re-atribuyó al
grafo un error que la vara adjudica al agente (trasplante de dominio). El 4/4 del dev era
**material iterado**; este es el primer contacto de S1 con casos frescos, y el diseño no
generalizó — el mismo patrón que ya medí con el verificador en la validación de v6.1-D.

**(ii) La provenance desplazada del grafo NEUTRALIZA el fetch de S1.** El defecto que la
vara documenta como patrón transversal (7 nodos en 3 casos) es también la razón de que la
verificación por fuentes no pueda operar: `sin_portador_extraible` en CQN-014 (fetch
fallido → S1 mudo sobre el caso de la familia 12.3) y `no_determinable` ×3 en CQN-006
(fetch completo pero juicios que no deciden). **La política de triage-por-fetch
conservadora sostuvo: cero acciones silenciosas por fetch fallido** — todos los fallos
derivaron con motivo `fuente_no_verificable` (extracción, casos CQN-001/009/014).

**(iii) Punto ciego NUEVO de v6.1-D: el puntero estructural (CQN-007).** D1/D2 modelan
alcanzabilidad LÉXICA (réplica de buscar_nodos); un puntero entregado por `ver_vecinos`
— el caso exacto de CQN-007, donde el vecino con su label, relación y provenance estuvo
en pantalla — **no existe para la capa**. Resultado: D2 corrigió navegación →
`alcanzabilidad_kg` 3-0 con discrepancia en las 3 reps (extracción, CQN-007:
`atribuciones_corregidas: 3, discrepancias: 3`) y el compuesto emitió CONFIADO, sin
triage, donde la vara adjudica navegación por el puntero estructural. Limitación de
instrumento — D1/D2 no ven la vía estructural — visible recién con casos frescos.

## 4. Nota estructural de CQN-010 (pre-registrada en la vara)

El verificador corre sobre el SÍNTOMA que el juez declaró; en CQN-010 el juez marcó
`verdadero` (FN, mecanismo de solapamiento superficial — vara §3 y patrón transversal 4)
el claim materialmente falso, así que aguas abajo no hubo síntoma central que investigar:
ambos sistemas exoneraron ([] 3-0) con flag R1. **El miss es por construcción del
pipeline (el FN del juez es invisible para todo lo que viene después), no del
instrumento.** Queda como límite arquitectural documentado del enfoque
juez-primero.

## 5. Notas operativas y fe de erratas

- **(a) Cableado del driver:** la whitelist del parseo del CLI del verificador (línea
  1037, `off|on`) rechaza el label `gate_cqn`; la corrida usó un driver que replica
  VERBATIM el loop del runner de `main()` (líneas 1088-1112: `investigar_falla` +
  `agregar_voto`, namespaces `cv=verificador-v5.7-rep{i}`) pasando el label por
  parámetro. **El instrumento no se tocó** — hashes de los congelados en el sello de la
  extracción.
- **(b) Fe de erratas:** el mensaje del commit `89f693d` contiene el literal
  `/bin/zsh.79` donde iba el costo `$0.79` (expansión accidental de shell al escribir el
  mensaje). Sin efecto sobre la guarda: el ancla verifica CONTENIDO por igualdad de blob,
  no el mensaje.
- **(c) Costos reales medidos:** corrida 1 (verificador N=3, 10 casos) =
  **9.838.669 in / 259.846 out**; corrida 2 (S1 N=3) = **220.212 in / 25.556 out**
  (≈2,2% de la corrida 1).

## 6. Qué queda abierto (sin decidirlo acá)

Dos caminos, decisión externa a este documento:

- **Rediseñar S1** — como mínimo: guarda de dominio pregunta↔fuente en el fetch (el
  mecanismo del hallazgo i) y extracción de portador robusta a provenance desplazada (el
  mecanismo del hallazgo ii) — lo que exige un **ciclo dev-eval NUEVO con material
  fresco**: estos 10 casos quedaron quemados hoy.
- **Cerrar con v6.1-D como instrumento validado** — con su mapa de límites completo
  (frontera semántica, no-generalización del LLM, y ahora el puntero estructural) — **y
  S1 como resultado negativo documentado**: la verificación por fuentes forzadas no
  superó a la capa determinística en su primer contacto con casos frescos, y falla
  con los mismos mecanismos (provenance corrupta, dominio) que pretendía corregir.

---

*Registro final: la vara quedó commiteada antes de la corrida, la corrida fue única, el
scoring usa las reglas pre-registradas sin excepción, y los 10 casos del gate quedan
QUEMADOS para cualquier iteración futura de cualquier componente.*
