# Lectura del GATE U5 — verificador sobre la familia v2/v3

**Fecha:** 2026-08-02. **Protocolo:** `docs/protocolo_gate_u5.md` (commit `49721fd`;
Enmienda §8 en `6150971` — techo secundario renovado a USD 30 total, alcance exclusivo
completar el gate). **Corrida:** única en dos fases (fase 1 cortada por el techo
original en G-3·rep3 — el corte es el protocolo funcionando; fase 2 bajo la enmienda),
guarda del paso 0 13/13 y re-verificación pre-fase-2; salidas congeladas en
`data/experiment/evaluacion/posthoc_run/gate_u5/` (13 archivos, votos crudos
verbatim + `estado_corrida.json`). **La vara de cada caso NO entró a ningún contexto de
corrida; el scoring es externo y fue laudado por la adjudicadora — este documento lo
persiste.** Todo número sale de `estado_corrida.json`, de los JSONs de la corrida o de
los chequeos citados junto a cada bloque.

## 1. Objeto y resultado

**EL GATE PASA por el criterio sellado (protocolo §4): cero errores silenciosos +
3 aciertos de 4, con el cuarto caso en rama de lectura pre-registrada.** El verificador
(**v7' = v5.7 + v6.2-D + S1 v0.4b**, congelado, hashes 6/6 verificados contra el sello
del ciclo 2 antes y después de cada fase) **ASCIENDE de exploratorio a
VALIDADO-EN-FAMILIA v2/v3.**

Mecánica de la corrida: 12/12 repeticiones, 0 `formato_invalido`, 0 fallas técnicas,
capa determinística y S1 aplicados a los 4 casos; ningún miss silencioso (todo caso
con desvío quedó con flag o en rama pre-registrada).

## 2. Adjudicación por caso (veredictos laudados, verbatim)

| Caso | Voto final del compuesto | Veredicto |
|---|---|---|
| G-1 · EV1-042 | {context_recall, completitud_kg} 2-1 | **ACIERTO** |
| G-2 · EV1-015 | {context_recall, completitud_kg} ×2, 2-1 | **ACIERTO** |
| G-3 · EV1-029 | {context_recall, navegación} 3-0 | **RAMA DE LECTURA (ii)** |
| G-4 · EV1-039 | {noise_sensitivity, contenido_kg} 3/3 | **ACIERTO (con asterisco)** |

- **G-1 ACIERTO:** regla cumplida en mayoría 2-1; minoría en rama pre-registrada;
  flags S1 consistentes con la vara (RX-03).
- **G-2 ACIERTO:** regla cumplida 2-1; la búsqueda de la mayoría prueba la ausencia
  (1491 matches sin el criterio 1.1); el vecino 7.1 no capturó al instrumento.
- **G-3 RAMA DE LECTURA (ii):** navegación 3-0 CON simulación ex ante aportada —
  manifestación de B′, ni acierto ni miss silencioso. Matiz registrado: la evidencia
  sitúa el caso en la frontera navegación/B′ (queries razonables que lo entierran y
  otras que lo rankean #1); la etiqueta fina (`entierro_por_ranking`, sub-especie de
  lectura externa laudada en
  `data/experiment/evaluacion/calibracion_v2v3/brechas_taxonomia.md`) la pone esta
  lectura, no el contrato. Nota metodológica: el instrumento aportó la evidencia del
  deslinde sin poder nombrarlo — tercer ejemplar de la laguna B′, el de mejor
  expediente (precedentes: CQN-009 pre-registrado, CQN2-015 materializado).
- **G-4 ACIERTO CON EL ASTERISCO del disclosure sellado** (forma ejercitada en el
  prompt, protocolo §3 G-4): regla cumplida 3/3, señalamiento verificado (ambos
  portadores con quote + pasaje del 1.2), S1 `fuente_no_funda` span 0 como
  confirmación por mecanismo, agente exonerado por el propio voto.

## 3. Hallazgo residual del gate — el instrumento diagnosticando dentro de su propio gate

El señalamiento de G-4 no se agotó en el caso: las tres repeticiones citaron también el
nodo de compañías financieras de comercio exterior con `umbral: '2.500 millones de
pesos'`. Chequeo determinístico de esta lectura sobre el grafo **VIGENTE**
(`data/experiment/grafo_v2/reensamblado_v3/kg.json`, 4.459/8.046, post-C1/C2):

- Nodo `Restriccion_las_companias_financieras_que_realicen_en_forma_directa_operaciones_de_comercio__7bb7bb`,
  properties verbatim: `descripcion: "Las compañías financieras que realicen, en forma
  directa, operaciones de comercio exterior deberán observar las exigencias
  establecidas para los bancos"` · `tipo: "limite_cuantitativo"` ·
  **`umbral: "2.500 millones de pesos"`** · provenance "Punto 1.2. Exigencia básica.".
- El PDF es el árbitro (`data/backlog/propuestas/C2_montos_12.md`): las compañías
  observan "las exigencias establecidas para los bancos" = **5.000**. El umbral del
  nodo es **rastro residual de la inversión del 1.2 que C2/BKL-0006 no alcanzó** (C2
  corrigió los dos nodos de montos; este tercer portador conservó el valor invertido).

**Consecuencia: alta BKL-0023** en `data/backlog/backlog.jsonl` (`fuente: verificador`,
`diagnostico: verificador_validado`, especie `quimera`, estado **`nuevo`** — el triage
es de la autora). Es el instrumento haciendo trabajo de diagnóstico a escala DENTRO de
su propio gate: el voto que acertó la clave del caso dejó, de paso, el próximo defecto
localizado con su evidencia.

## 4. Alcance de la validación

**Intra-familia v2/v3 exclusivamente** (la lección 0/6 fuera de familia rige —
`docs/lectura_validacion_v61.md`: calibrado en run_1/run_3/run_5, la precisión sobre
run_2/run_4 fue 0/6); **un esquema nuevo exigirá su propio gate.** Los veredictos del
verificador sobre v2/v3 pasan a fundar refinamiento CON adjudicación humana del laudo
final (**Motor 3: diagnóstico automático, laudo humano**). La regla operativa queda en
`.claude/skills/kg-refinement/SKILL.md` (alcance por grafo, editado por esta unidad):
sobre la familia v2/v3 el veredicto del verificador validado habilita el diagnóstico de
entradas de backlog; la adjudicación del laudo final y toda aplicación siguen siendo
humanas; fuera de la familia, el verificador sigue exploratorio.

## 5. Deudas que el gate deja registradas

- **Canal de abstenciones-aprobadas** (falso negativo del juez): fuera del universo de
  entrada del instrumento — candidata de cola ("screening de aprobadas /
  re-calibración del juez"), protocolo §7 y `brechas_taxonomia.md` §2.
- **Las sub-especies de lectura externa laudadas** (`perdida_en_ensamblado`,
  `falla_de_juez` con subtipos, `entierro_por_ranking`): viven en la adjudicación
  humana y el backlog, nunca en el contrato del instrumento sellado.
- **El asterisco de G-4**: la forma del caso está ejercitada en los ejemplos del prompt
  congelado (disclosure sellado en el protocolo §3); acompaña a ese acierto en toda
  cita futura.

## 6. Costo y evidencia

- **Costo real: USD 23,22 de 30** (enmienda §8), 4.058.818 tokens in (68% del tope
  primario de 6M) / 117.036 out (59% de 200K), a la referencia USD 5/25 por MTok
  registrada en `estado_corrida.json`. **12/12 reps, 0 `formato_invalido`,
  cross-check del tracker contra las filas nuevas de `cache/verificador.db` exacto al
  token** (104 filas de verificador en 6 namespaces + instrumentación `resumen_s1` de
  los 4 casos).
- Evidencia: protocolo `49721fd` · enmienda `6150971` · salidas y votos crudos en
  `posthoc_run/gate_u5/` (13 archivos) · `estado_corrida.json` (gasto, topes, fases,
  corte de fase 1) · preflight y logs de corrida en el scratchpad de sesión,
  reproducibles desde los archivos citados.

— Fin de la lectura del gate U5. —
