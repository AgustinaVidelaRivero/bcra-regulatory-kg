# Lectura final del ciclo 2 — head-to-head a tres columnas (v6.1-D / v6.2-D / v7')

**Fecha:** 2026-07-19. **Vara:** `docs/casos_gate_cqn2.md` (commit `65bea99`, sellada por
inexistencia ANTES de toda corrida). **Extracción de la corrida:**
`posthoc_run/dev_set/extraccion_h2h_ciclo2.md` (mecánica, sin scoring — el scoring de
este documento es mío, contra la vara). Los 44 JSONs congelados:
`posthoc_run/gate2_h2h/`. **Diseño del ciclo:** `docs/diseno_ciclo2.md`. Todo número de
este documento está copiado de esas fuentes, no recalculado.

## 1. El ciclo completo en custodia

- **Diseño pre-registrado:** `docs/diseno_ciclo2.md` (commit `b84668e`: D7 con tabla de
  verdad de 4 filas y válvula, guarda de dominio por `tos_fuente`, portador robusto por
  contenido, criterios de éxito (a)-(d)) + **enmienda §4bis** (`56bc5aa`: requisito de
  fundamento del pasaje, `fuente_no_funda`, criterio (e)) — ambos commiteados ANTES de
  implementar.
- **Dev contra material QUEMADO** (los 30 JSONs del gate CQN, jamás material fresco):
  unidad 1 (v6.2-D/D7: un solo cambio — CQN-007 a navegación, criterio a — cero
  regresiones, 0 punteros espurios en decisiones, test sintético del camino c;
  `7cef0ba`); unidad 2 (S1 v0.4: guarda de dominio + portador por contenido, criterios
  b/c cumplidos, residuo en d); unidad 2b (v0.4b/§4bis: criterio e cumplido, con el
  residuo de varianza pre-registrado; `6aa9a3e`).
- **El set CQN2:** generado A CIEGAS por instancia sin repo (semilla 20260719, sorteo
  reproducido), custodia con **corpus byte-idéntico 5/5** y 13/15 citas verbatim + 2
  fórmulas por convención documentada; **sellado en `df29525`** con estratos
  adjudicados: **12 primarias / 3 solapadas (010, 012, 013) con disclosures / 0
  ilustrativas**.
- **Corrida agente+juez:** única, bajo guarda con hashes (15/15 trazas, USD 0,8146;
  censo mecánico → 11 fallas con síntoma). Expediente con **fidelidad
  runtime↔re-ejecución 156/156 pasos**; barridos determinísticos K-A..K-I + K-E2.
- **La vara:** adjudicada sobre ese expediente y commiteada (`65bea99`) ANTES de que
  existiera veredicto alguno de verificador, capas o S1 sobre este material —
  **sellado por inexistencia cumplido de punta a punta**.
- **La corrida del head-to-head:** guarda del paso 0 **4/4** (status limpio; vara =
  HEAD; hashes del set/runtime idénticos al sellado; congelados con cero diff, hashes
  en el sello de la extracción). Un solo run del verificador v5.7 (`--n 3`); las tres
  columnas son post-procesamiento del MISMO run.

## 2. Scoring por estratos (contra la vara, reglas de acierto de la vara §c)

**Primaria (8 casos):**

- **CQN2-002:** acierto-por-triage ×3 (C con `fuente_cross_doc` — la guarda disparando
  en el trasplante exacto).
- **CQN2-004:** miss-con-flag ×3.
- **CQN2-005:** acierto 3-0 ×3.
- **CQN2-006:** acierto ×3 (C +`fuente_no_funda`).
- **CQN2-007:** acierto ×3 (C sin flag: exoneración sostenida con la fuente — §4bis
  confirmando).
- **CQN2-011:** triage ×3.
- **CQN2-014:** acierto ×3.
- **CQN2-015:** acierto ×3 (+flag en C).

**Tabla resumen primaria: A = B = C = 6 aciertos / 1 miss-con-flag / 1 triage — CERO
silenciosos en las tres columnas.**

**Solapadas (aparte, con su disclosure):**

- **CQN2-010:** acierto ×3.
- **CQN2-012:** acierto ×3.
- **CQN2-013:** miss-con-flag ×3 (alcanzabilidad donde la vara adjudica
  quimera-contenido; S1 gatilló solo la minoritaria, `corrigió=0`, flags R6b de la capa
  persisten).

## 3. Los cinco titulares

**(i) Contención perfecta: cero misses silenciosos en las tres columnas** — contra
**1 silencioso de v6.1-D y 2 de v7-v0.3.1 en el gate anterior**
(`docs/lectura_gate_cqn.md` §2: CQN-007 silencioso en ambos; CQN-013 silencioso solo en
v7). Cada miss de este gate (004, 013) salió CON flag: `atribucion_no_verificable` (R6b)
en A/B, más `fuente_cross_doc`/`fuente_no_funda` en C (extracción, secciones CQN2-004 y
CQN2-013).

**(ii) S1 v0.4b PASÓ su gate.** Los dos mecanismos que voltearon a v0.3.1 no
reaparecieron: la **guarda de dominio** bloqueó los fetch cross-doc en 002 (4 bloqueos:
portadores del RI y de Capitales ∉ territorio Clasificación — el patrón EXACTO del
hallazgo (i) del gate anterior) y en 004 (3 bloqueos) — **bloqueos determinísticos, cero
tokens en cada bloqueo, cero flips del voto**; `fuente_no_funda` contuvo en 5 casos
(004/006/010/011/012); en **007 S1 mejoró al compuesto** (juzgó 3, sostuvo la
exoneración con la fuente en la mano y APAGÓ el flag R1 de A/B — `exoneracion_con_sintoma`
registrado); y **cero degradaciones**: las 2 correcciones que S1 sí ejecutó (002
rep3_atrib1 y 011 rep3_atrib4, ambas → contenido_kg con fetch `completo` y 3-0 del
juicio) no alteraron ningún resultado de columna. El fantasma de CQN-013-anterior (flip
confiado por fuente de otro dominio) no reapareció.

**(iii) v6.2-D = v6.1-D en las 11 filas.** `decisiones_con_puntero = 0` en los 11 casos
(extracción, resúmenes D2'): D7 no decidió ninguna frontera en este material — el punto
ciego del puntero estructural (CQN-007 del gate anterior) **no recurrió en fresco**. La
validación positiva de D7 queda donde estaba: el material quemado de la unidad 1 (el
cambio único en CQN-007) y el test sintético del camino c (`test_d7_camino_c.py`).

**(iv) Los 2 misses comparten mecanismo — sub-especie de defecto KG mal nombrada.** En
004 el compuesto emitió `{ns, contenido_kg}` 2-1 donde la vara adjudica des-scoping del
agente sobre nodo fiel; en 013 emitió `{cr, alcanzabilidad_kg}` 2-1 donde la vara
adjudica quimera label↔description (contenido). En ambos, el instrumento detectó QUE hay
defecto y erró CUÁL sub-especie — y ambos quedaron flaggeados (R6b persistente; en 004
además la cadena S1). Es el límite residual del instrumento, ahora caracterizado: la
frontera fina dentro de la familia KG (des-scoping↔contenido, quimera↔alcanzabilidad).

**(v) Honestidad de predicción en 015.** La predicción corregida-pre-corrida (vara,
caso CQN2-015) decía que v6.2-D emitiría alcanzabilidad en la pata-piso; el detalle la
refutó: la clave GANADORA fue `{cr, completitud_kg}` 2-1 — **la de la otra pata** — con
la corrección D2 navegación→alcanzabilidad ocurriendo solo en la rep minoritaria (rep2,
`discrepancias=2`; extracción, CQN2-015). El caso queda como acierto POR REGLA (la vara
acepta cualquiera de las dos claves de las patas), con el mecanismo B′ NO nombrado por
el instrumento — coherente con la laguna documentada en la vara: D2 no distingue el
entierro-por-ranking de la inalcanzabilidad léxica, y ninguna columna emite "B′".

## 4. Comparación inter-gate (con advertencia metodológica)

**Advertencia explícita: los materiales difieren.** CQN2 salió **completitud-pesado**
— 6 de las 11 primarias adjudicadas del lado grafo son completitud/alcanzabilidad
(005/006/010/012/014/015) — donde el gate CQN cargaba más des-scoping de agente
(aplicacion_erronea en 3 de sus 6 primarias). Los números **no son comparables punto a
punto**: parte de la mejora refleja la mezcla de casos, no solo los arreglos. Lo que SÍ
es comparable: (a) la **propiedad de contención** — de 1 silencioso (v6.1-D) y 2 (v7)
en el gate anterior a **0 en las tres columnas** acá; y (b) el **comportamiento de los
arreglos en sus casos-test**: la guarda de dominio disparó exactamente sobre
trasplantes cross-doc (002/004), §4bis contuvo sin apagar aciertos (006/010/012), y la
política conservadora siguió derivando con motivo en vez de callar (011/015).

## 5. Notas operativas

- **(a) Cableado del driver:** idéntico al head-to-head anterior — la whitelist del CLI
  del verificador (labels `off|on`) rechaza `gate_cqn2`; driver que replica VERBATIM el
  loop del runner de `main()` (rama `--n>1`: `investigar_falla` + `agregar_voto`,
  namespaces `cv=verificador-v5.7-rep{i}` intactos). El instrumento no se tocó — hashes
  de los congelados en el sello de la extracción.
- **(b) Semántica de triage en la columna C:** S1 reporta su triage propio
  (`triage_s1`); los motivos de la capa (R1/R4/R6b) persisten en la cadena `_capa_d62`
  sobre la que S1 corre. Esta lectura los cuenta como flag del COMPUESTO: un caso es
  "silencioso" solo si NINGUNA etapa de su cadena dejó flag.
- **(c) Costos reales medidos:** verificador **12.869.986 in / 300.112 out**; S1
  **186.531 in / 23.640 out** (≈1,4% del verificador; en 4 de los 11 casos S1 no hizo
  ninguna llamada LLM); capas A/B: **cero LLM**.

## 6. Cierre del ciclo y estado del instrumento

**v7' (v6.2-D + S1 v0.4b) queda como el instrumento del proyecto.** Está validado
contra **cuatro varas humanas selladas** (v3, gate CQN, dev-v7, gate CQN2), con
**contención perfecta en el último gate fresco** (cero silenciosos; todo miss con flag
y todo triage con motivo) y **límites caracterizados**: la frontera fina de
sub-especies del lado KG (des-scoping↔contenido en 004, quimera↔alcanzabilidad en 013),
la laguna B′ (entierro-por-ranking sin nombre propio, 015), y D7 validado solo contra
material quemado + test sintético (sin evidencia fresca, porque el mecanismo no
recurrió).

**Queda abierto, sin decidirlo acá:** si los misses 004/013 motivan un ciclo 3 (afinar
la distinción de sub-especies del lado KG) o quedan como límite documentado del
instrumento — decisión externa, con calendario en la mano.

---

*Registro final: la vara quedó commiteada antes de la corrida, la corrida fue única con
guarda 4/4, el scoring usa las reglas pre-registradas de la vara §c sin excepción, y
los 11 casos del gate CQN2 quedan QUEMADOS para cualquier iteración futura de cualquier
componente.*
