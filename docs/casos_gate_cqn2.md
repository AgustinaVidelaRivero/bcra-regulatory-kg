# Casos del GATE CQN2 — vara de adjudicación (ciclo 2)

Vara del **gate del ciclo 2** (head-to-head A TRES COLUMNAS: v6.1-D / v6.2-D / v7' con
S1 v0.4b — diseño `docs/diseno_ciclo2.md` §1): las 11 fallas con síntoma no vacío de la
corrida CQN2 sobre run_3 (censo en la zona de trabajo, `censo_gate_cqn2.md`; trazas
congeladas en `posthoc_run/traces/gate_cqn2/run_3/`). **Adjudicada ANTES de cualquier
corrida del verificador (cualquier versión), de las capas o de S1 — sellado por
inexistencia: sus veredictos sobre este material no existen y no existirán hasta el
commit de esta vara.** **Vocabulario:** taxonomía v2.6.1. **Circuito:** el de la vara —
expediente con fidelidad runtime↔re-ejecución verificada (**156/156 pasos**,
`expediente_gate2_1.md`/`_2.md`), barrido determinístico sobre el kg congelado
(`docs/evidencia_gate_cqn2/barrido_kg_gate_cqn2.md`, ítems K-A a K-I + anexo K-E2),
verificación contra los PDF del corpus con página (sondas pdfplumber), y ramas
pre-registradas antes de la exposición.

**Evidencia:** `docs/evidencia_gate_cqn2/` (un archivo por caso, `cqn2_002.md` …
`cqn2_015.md`, con los extractos verbatim que cada sección cita + los dos barridos:
K-A..K-I íntegro y su anexo K-E2).

**El eval set:** `queries/eval_set_cqn2.json` (SELLADO, commit `df29525`) — 12
primarias, 3 solapadas con disclosure (CQN2-010/012/013), 0 ilustrativas. La corrida
única usó el derivado de corrida `eval_set_cqn2_runtime.json` (mismo commit), que solo
duplica un campo por contrato del juez; guarda del paso 0 con hashes verificada
(`censo_gate_cqn2.md`).

---

## CQN2-002 — `factual_directa` · estrato **primaria**

**1. Perfil y síntoma.** Respondida; `correcta` + `completa`; F = 3 secundarios
`no_soportado` (casa-matriz; códigos de consolidación 0/1; código 3) · P = 0
(`expediente_gate2_1.md`, CQN2-002 §2). 14 pasos, sin tope de tools.

**2. Ramas pre-registradas.** Por claim reprobado: ¿alucinacion_agente /
aplicacion_erronea (contenido fiel de otro régimen) / FP del juez (corpus-real)?

**3. Exposición.**
- **El claim casa-matriz es FP del juez:** está VERBATIM en el nodo abierto en el paso 3
  (provenance "Punto 2.2. Exclusiones." de Clasificación) y es **corpus-real** —
  Clasificación 2.2.4.1 (p.8) y su **gemelo de Capitales** 2.2.3.1 (p.9), sondas en
  `cqn2_002.md`.
- **Los claims de códigos 0/1 y 3 son un trasplante:** el nodo del paso 12
  (`Obligacion_informacion_base_individual_y_consolidada`) es FIEL a su fuente — el
  **10.1 del régimen informativo, la sección del RATIO DE APALANCAMIENTO** (corpus p.43
  en `cqn2_002.md`) — con el alcance declarado EN el nodo (provenance "Punto 10.1.
  Normas de procedimiento", visible en el `ver_nodo` del paso 12); la respuesta lo
  presentó como régimen de "datos de clasificación de deudores". Grounded≠correct, lado
  agente.
- **La cita "Punto 2.2. Exclusiones" es fiel a su nodo** (paso 3).
- **Registros:** la cobertura fue juzgada con vara generosa (la pata quedó "cubierta"
  con la respuesta desviada) — queda como NOTA, no como FN del juez. Y el nodo del paso
  9 lleva contenido del 9.2 de Capitales con provenance "Punto 9.1. Base individual."
  — **provenance desplazada, backlog** (`cqn2_002.md`, paso 9).

**4. VEREDICTO: SIN PRIMARIA (cero centrales fallidos). Secundarias
{noise_sensitivity, aplicacion_erronea} ×2** — trasplante del régimen del ratio de
apalancamiento a "datos de clasificación de deudores". El claim casa-matriz NO es
defecto (FP del juez).

---

## CQN2-004 — `factual_directa` · estrato **primaria**

**1. Perfil y síntoma.** Respondida; `correcta` + `completa`; F = 5 (3 CENTRALES
`no_soportado`) · P = 0; `requiere_adjudicacion_humana: true`
(`expediente_gate2_1.md`, CQN2-004 §2). 15/15 tools.

**2. Ramas pre-registradas.** Por claim: ¿FP del juez (corpus-real fuera de la cita del
GT) o defecto real (des-scope / trasplante)?

**3. Exposición.**
- **Claims 1-2 (plazos residuales) = FP del juez:** el método de los plazos residuales
  es **corpus-real** — Capitales **6.2.2/6.2.2.1**, p.123 (sonda en `cqn2_004.md`) — y
  el nodo del paso 8 es fiel con **provenance correcta** ("Punto 6.2 … (parte 2)"); la
  respuesta citó el 6.2. Marco estrecho del juez contra la cita del 6.1.
- **El claim 3 es el defecto real:** la respuesta **des-scopeó el nodo RI-12.2** — el
  nodo del paso 4 dice "Determinación del **importe a consignar en la partida
  70800000** … computando el mayor valor entre el código 70810000 y 70820000", con el
  alcance declarado EN el nodo (provenance "Punto 12.2. Determinación de la exigencia …
  Comunicación 'A' 5867"), y la respuesta lo enunció como LA regla de determinación de
  la exigencia por riesgo de mercado, **borrando "importe a consignar en la partida"**
  (`cqn2_004.md`, paso 4 + respuesta final; corpus RI p.57).
- **Los 2 secundarios de opciones = FP ×2:** método simplificado y Gamma/Vega son
  corpus-reales de la Sección **6.6.x** de Capitales (pp.135-137, sonda en
  `cqn2_004.md`).
- **Balance: 4 de los 5 reprobados son FPs; el quinto es el defecto real.**

**4. VEREDICTO: {noise_sensitivity, aplicacion_erronea} PRIMARIA** — claim 3: nodo fiel
de otro alcance (partida del régimen informativo 2016) presentado des-scopeado como
regla general.

---

## CQN2-005 — `factual_directa` · estrato **primaria**

**1. Perfil y síntoma.** Abstención; `correcta` + `parcial`; F = 0 · P = 2 (ante quién
se nomina; condición del cambio) (`expediente_gate2_1.md`, CQN2-005 §2). 16/16 tools.

**2. Ramas pre-registradas.** Por pata: (A) completitud_kg — el contenido no existe;
(B) alcanzabilidad_kg — existe y no rankea; (C) navegación — existe, alcanzable o
señalizado, no abierto; (D) expuesto en outputs y no usado.

**3. Exposición.**
- **Pata-ARCA: la nominación-ante-ARCA no existe en ningún nodo.** Barrido K-A:
  "originalmente nominada" → 0 hits; los nodos de la nominación del 11.1 (pasos 3 y 4)
  portan la obligación de nominar SIN el "ante la ARCA" del corpus (Exterior 11.1,
  p.160 — sonda en `cqn2_005.md`); los hits de "ARCA" son de otros territorios (8.x,
  3.16).
- **Pata-condición: el portador existe, fiel y enterrado.** El nodo
  `Restriccion_prohibicion_de_cambio_sin_certificaciones_pendientes` porta la condición
  completa ("no existan certificaciones emitidas … pendientes de uso"), con provenance
  11.1 CORRECTA — pero **con el antecedente amputado**: su description arranca en "El
  importador podrá posteriormente modificar…", cortando "La entidad será originalmente
  nominada por el importador ante la ARCA, pudiendo…" — **segunda amputación de
  antecedente del historial** (la primera: CQN-010 del gate CQN). Y está **léxicamente
  enterrado**: jamás entró a un top-N en los 16 pasos de la traza (ranking K-A: 5
  consultas verificadas, nunca en top; dump en `cqn2_005.md`).
- **Rama D muerta:** el contenido de la condición no aparece en ningún output de la
  traza (la abstención del agente lo confirma: "no se especifican las condiciones").
- **Backlog: gemelos duplicados de la nominación** — pasos 3 y 4 abren DOS nodos con la
  MISMA description verbatim (ids y types distintos), más un tercer gemelo del régimen
  de exportaciones (8.2) en K-A.

**4. VEREDICTO (por pata): pata-ARCA {context_recall, completitud_kg} ·
pata-condición {context_recall, alcanzabilidad_kg}.**

---

## CQN2-006 — `factual_directa` · estrato **primaria**

**1. Perfil y síntoma.** Abstención; `correcta` + `parcial`; F = 0 · P = 1 (el valor
del ILM) (`expediente_gate2_1.md`, CQN2-006 §2). 15/15 tools.

**2. Ramas pre-registradas.** (A) completitud_kg — el glosario "ILM = 1" no existe;
(B) alcanzabilidad/navegación — existe y no se llegó; (D) expuesto y no usado.

**3. Exposición.**
- **El glosario "ILM = 1" no existe en ningún campo del kg.** Barrido K-B: "igual a 1"
  → 0 hits; "multiplicador de pérdida interna" → 0 hits; el único hit de "ILM" es la
  sigla dentro de la fórmula del portador (`CRO = BIC x ILM`, paso 4) — el nodo porta
  la fórmula SIN el renglón del glosario que el corpus tiene a continuación (RI 5.1.1,
  p.21: "ILM: multiplicador de pérdida interna igual a 1." — sonda en `cqn2_006.md`).
- **El D1 lo ejecutó el propio agente en runtime:** paso 14, consulta "ILM" (límite 15)
  → `total_con_match: 0` (`buscar_nodos` busca sobre label e id; la sigla vive solo en
  una description). Cinco sondas más al valor (pasos 5/7/8/12/13) sin resultado.
- **Backlog:** el nodo del paso 10 (`Operacion_calculo_mensual_de_exigencia_operacional`)
  es una cáscara SIN description con provenance correcta 5.1.

**4. VEREDICTO: {context_recall, completitud_kg}.**

---

## CQN2-007 — `factual_directa` · estrato **primaria**

**1. Perfil y síntoma.** Respondida; `correcta` + `completa`; F = 4 secundarios
`no_soportado` · P = 0 (`expediente_gate2_1.md`, CQN2-007 §2). 10 pasos.

**2. Ramas pre-registradas.** ¿alucinacion_agente (la respuesta agregó los criterios) o
sin_defecto (FP del juez)?

**3. Exposición.** Las cuatro frases reprobadas están **VERBATIM en un solo nodo fiel
abierto en el paso 9** (`Obligacion_la_metodologia_utilizada_para_asignar_…`, provenance
"Punto 10.2. Criterios de elegibilidad.") **cuyo texto es contiguo-PRECEDENTE a la cita
del GT dentro del mismo 10.2.2**: en el corpus (Capitales p.172, sonda en
`cqn2_007.md`) las oraciones de "rigurosa, sistemática … control constante … coyuntura
financiera" van inmediatamente antes de "Para poder ser reconocida, la metodología …
un año … backtesting" — la oración de la cita sellada. El juez midió contra la cita del
eval set, no contra el punto del GT.

**4. VEREDICTO: SIN_DEFECTO** — FP del juez ×4, **variante cita-estrecha (segundo
ejemplar canónico**; el primero: CQN-006 de la vara del gate CQN).

---

## CQN2-010 — `multi_norma` · estrato **solapada** (disclosure: pata 6.3.1 = CQ-024; hermanas 1.1.x quemadas; el 1.1.2.3 puntual virgen)

**1. Perfil y síntoma.** Abstención; `correcta` + `parcial`; F = 0 · P = 2 (fiduciario
sujeto obligado; deudores cedidos como usuarios) (`expediente_gate2_1.md`, CQN2-010
§2). 16/16 tools.

**2. Ramas pre-registradas.** Por pata de Protección: (A) completitud_kg; (B/C)
alcanzabilidad/navegación. Pata (b) de Clasificación: lectura descriptiva (territorio
CQ-024, disclosure).

**3. Exposición.**
- **Las cláusulas de Protección no existen en el kg.** Barrido K-C: fiduciario ∧
  provenance Protección/1.1.2.3 → **0 hits**; "cedidos"/"notificados fehacientemente" →
  8 portadores, TODOS con provenance de otros TOs, y ninguno entra a ningún top-N en
  los 7 pasos verificados. El corpus las tiene íntegras (Protección p.3, 1.1.2.3 y
  1.1.1 — sondas en `cqn2_010.md`).
- **Pata (b) (6.3.1, territorio CQ-024): PERFECTA, sin atribución** — la central del
  trimestre calendario salió `verdadero` y cubierta.
- **Registro estructural (backlog):** `EntidadFinanciera_sujeto_obligado` tiene **991
  entrantes / 104 salientes**, con entrantes de los CINCO documentos (374 de Capitales,
  272 de Exterior, 128 de Protección — recuento determinístico en `cqn2_010.md`) —
  **contaminación inter-régimen de la entidad-clase**. Y el único nodo-fiduciario que
  el agente abrió (paso 5) es un **huérfano de OTRO régimen** (provenance Clasificación
  10.2; 0 salientes, paso 7) — **no trasplantado por el agente**: la respuesta no lo
  afirmó como sujeto obligado de Protección.

**4. VEREDICTO: {context_recall, completitud_kg}.**

---

## CQN2-011 — `multi_norma` · estrato **primaria** (disclosure: 12.1 de Capitales virgen, familia Sección 12 del defecto de CQN-014)

**1. Perfil y síntoma.** Abstención parcial (`respondible: false` con contenido
afirmado); `incorrecta` + `parcial`; F = 5 (4 CENTRALES `falso`) · P = 6
(`expediente_gate2_1.md`, CQN2-011 §2). 15/15 tools.

**2. Ramas pre-registradas.** Por claim: ¿contenido_kg (nodo infiel) /
aplicacion_erronea (nodo fiel de otro alcance) / FP? Por pata: (A) completitud, (B)
alcanzabilidad, (C) navegación — con la vía estructural chequeada aparte (punteros).

**3. Exposición.**
- **Claims 1-2 (los centrales del plan): trasplante del régimen general.** El "plan de
  regularización y saneamiento / 30 días corridos" es el nodo del **1.4
  (Incumplimientos)** de Capitales — visto por el agente en el listado del paso 15 —
  presentado para el supuesto del 12.1 (integración de la exigencia básica), **con
  hedge** ("No se encontró información específica… Se identificó una obligación de…") —
  **atenuante registrado** (dump y respuesta en `cqn2_011.md`).
- **Claim 4 (la excepción +15 días): trasplante con alcance declarado.** El nodo del
  paso 14 dice EN su description "Para cartas de crédito o letras avaladas emitidas u
  otorgadas a partir del 14/04/25…" y la respuesta lo presentó como excepción general
  de operaciones embarcadas después del 14/04/25.
- **Claim 3 ("sujeta a arancel"): FABRICACIÓN DEL EXTRACTOR.** La coletilla "sujetas a
  arancel" tiene **0 hits en el corpus** (las 13 apariciones de "arancel" en Exterior
  son "posiciones arancelarias"/aduana — sonda en `cqn2_011.md`); el nodo del paso 5
  inventó la coletilla y el label **"Arancel a importaciones de aeronaves"** sobre el
  listado del 12.1. El agente fue FIEL al nodo deformado → **causa concurrente
  {noise_sensitivity, contenido_kg}**.
- **El secundario de la lista 8802 = FP del juez:** el listado es verbatim del nodo y
  corpus-real (cita sellada del 12.1).
- **Patas (a) ×4: los nodos existen y no llegaron.** K-D: el programa de encuadramiento
  vive en DOS nodos localizados POR LABEL (el id directo no existe) que portan
  **SEFYC + 20 días** (uno) y **6 meses** (otro) — la cláusula única del 12.1
  FRAGMENTADA — sin top-10 en las 5 consultas verificadas, **sin puntero estructural**
  (el extractor D7 real da 4 punteros en toda la traza, ninguno a estos nodos —
  `cqn2_011.md`), con 0 entrantes y colgados por `aplica_a` del **hub contaminado**
  (991 entrantes). La fragmentación y el colgado del hub quedan como **mecanismo
  estructural concurrente**.
- **Patas (b):** b1 — el contenido del 10.10.2.1 (MiPyMe + embarcados desde 14/04/25 +
  exclusión 12.1) **no existe** (K-E: 0 hits; el nodo MiPyMe del paso 6 es del 10.11).
  b2 — la excepción de aeronavegación **existe y es D1-NEGATIVA**: mejor_rank 25, 0
  consultas en top-10 de 105 simuladas, jamás en un top-N en los pasos 2/3/11 (anexo
  K-E2 del barrido).

**4. VEREDICTO: PRIMARIA {noise_sensitivity, aplicacion_erronea}** (claims 1-2 y 4) **+
CONCURRENTE {noise_sensitivity, contenido_kg}** (claim 3, fabricación). **Patas (a) ×4:
{context_recall, alcanzabilidad_kg}** con lo estructural como mecanismo concurrente.
**Patas (b): b1 {context_recall, completitud_kg} · b2 {context_recall,
alcanzabilidad_kg}.**

---

## CQN2-012 — `multi_norma` · estrato **solapada** (disclosure: 8.1.6 ⊂ Sección 8 del RI, cobertura conocida-parcial; 11.2 de Capitales virgen)

**1. Perfil y síntoma.** Abstención; `correcta` + `parcial`; F = 2 secundarios
`no_soportado` · P = 2 (`expediente_gate2_1.md`, CQN2-012 §2). 15/15 tools, sin citas.

**2. Ramas pre-registradas.** Por pata: (A) completitud_kg; (B/C)
alcanzabilidad/navegación. Por secundario: ¿defecto o FP?

**3. Exposición.**
- **La llave de negocio negativa no existe:** barrido K-F — "llave de negocio negativa"
  → 0 hits, "Previsiones del Pasivo" → 0 hits, contenido del 11.2 → 0 hits. El corpus la
  tiene (Capitales 11.2, p.176 — sonda en `cqn2_012.md`).
- **La fórmula del 8.1.6 no existe:** el único portador de "CDCOn1" en todo el kg es
  una CÁSCARA (`Operacion_calculo_de_deductibles_de_capital`, sin la fórmula); el
  rank-1 de la primera consulta del agente
  (`Restriccion_responsabilidad_patrimonial_computable_rpc_70200000_8_s_70900000`)
  porta SOLO el ratio "≥ 8% s/70900000" con provenance 6.3 — no la fórmula del 8.1.6
  (RI p.37, sonda). **Tercer agujero en serie de la Sección 8 del RI:** 70700000
  (CQN-009), mapeo de la Sección 2 (CQN-011 del gate CQN), fórmula 70200000 (acá).
- **Los 2 secundarios = FP ×2:** ambos están verbatim en nodos fieles con provenance
  correcta — Capitales 1.3 (paso 6) y la integración diaria del 6.7.1 (paso 5);
  corpus p.4 en `cqn2_012.md`.

**4. VEREDICTO: {context_recall, completitud_kg} PRIMARIA.**

---

## CQN2-013 — `multi_norma` · estrato **solapada** (disclosure: pata RI 3.1.2 = CQ-020 quemado ×2 varas ×2 grafos; pata 13.2.7.1 virgen)

**1. Perfil y síntoma.** Abstención parcial (`respondible: false` con respuesta
sustantiva); `incorrecta` + `completa`; F = 3 (1 CENTRAL `falso`: los 180 días para
vinculadas) · P = 0 (`expediente_gate2_1.md`, CQN2-013 §2). 16/16 tools.

**2. Ramas pre-registradas.** El central falso: ¿contenido_kg (nodo infiel indujo) /
aplicacion_erronea (el agente dedujo mal sobre nodos fieles) / alucinación?

**3. Exposición.**
- **El nodo quimérico indujo la inversión 90↔180.** El agente abrió en el paso 11
  `Restriccion_requisito_plazo_90_dias_para_servicio_no_comprendido`: **label del
  13.2.7.1** ("plazo 90 días para servicio no comprendido") con **description del
  13.2.6** ("contraparte NO vinculada … pago se concreta a partir de la fecha de
  prestación") — **quimera label↔description**. Leyendo "90 días" como el plazo de las
  NO vinculadas, el agente invirtió: dedujo 180 para las vinculadas. El corpus dice lo
  contrario (Exterior 13.2.7.1, p.170: **90 días para VINCULADAS desde el 14/04/25** —
  sonda en `cqn2_013.md`).
- **Contrafáctico limpio (consultas exactas del agente, paso 12):** bajo la consulta
  verbatim del paso 12, el quimérico rankea **9 de 50** (y ya estaba abierto); el
  **hermano SANO** (`Restriccion_requisito_plazo_contrapartes_vinculadas`, que porta
  vinculada + 90 + 14/04/25 en una sola description — K-G) queda **FUERA del top-50**:
  con las mismas consultas y el nodo no-deformado en su lugar, la respuesta salía.
- **CONCURRENTE (secundaria): el nodo-180 exportador trasplantado.** El "180 días para
  el resto de los bienes" es del régimen de EXPORTACIONES (corpus 7.1.1.4, p.81), con
  el alcance declarado EN la description del nodo, y fue usado para pagos de servicios.
  **Doble hedge del agente** (`respondible: false` + "se deduce por inferencia…, no de
  una norma explícita") — **atenuante registrado**.
- **El secundario "90 no-vinculadas" es manifestación del mismo contenido_kg** (el
  quimérico), no defecto aparte.
- **K-G, agravante del mapa:** el 13.2.7.1 sano EXISTE como hermano invisible del
  quimérico (mismo territorio 13.2, dumps en `cqn2_013.md`).
- **Pata (a) (CRC, territorio CQ-020): PERFECTA** — central `verdadero`, cubierta.

**4. VEREDICTO: {noise_sensitivity, contenido_kg} PRIMARIA** (el quimérico indujo la
inversión) **+ {noise_sensitivity, aplicacion_erronea} CONCURRENTE secundaria** (el
nodo-180 trasplantado).

---

## CQN2-014 — `cadena_restriccion_excepcion` · estrato **primaria** (disclosure: Clas 7.1 hermana de 7.2.1/10.1 quemados; punto propio virgen)

**1. Perfil y síntoma.** Respondida; `correcta` + `parcial`; F = 0 · P = 1 (los límites
del tratamiento) (`expediente_gate2_1.md`, CQN2-014 §2). 9 pasos.

**2. Ramas pre-registradas.** (A) completitud_kg — la oración de límites no existe;
(B/C) alcanzabilidad/navegación; (D) expuesta y no usada.

**3. Exposición.**
- **La oración final de límites no existe en el kg.** Barrido K-H: "mejoramiento" → 0
  hits; "extenderse" → 0 hits; "situación individual" → 0 hits. El corpus la tiene
  entera (Clasificación 7.1, p.33: "El tratamiento … no podrá implicar mejoramiento de
  la clasificación … ni su aplicación extenderse más allá de la vigencia…" — sonda en
  `cqn2_014.md`).
- **Las tres hermanas fueron extraídas FIELMENTE:** la excepción (paso 3), la regla de
  la mora al concluir la emergencia (paso 7) y la regla general (paso 8) — todas con
  provenance 7.1 correcta; la respuesta las usó bien y hasta ahí llegó. **Tercera
  cláusula-hermana del gate** (con CQN2-006 y CQN2-015): el pipeline extrae las
  oraciones vecinas y omite una del mismo bloque.
- **Backlog: gemelos duplicados de la excepción** — pasos 3 y 4 abren dos nodos
  Excepcion casi idénticos (provenances 7.1 y 6.5).

**4. VEREDICTO: {context_recall, completitud_kg}.**

---

## CQN2-015 — `cadena_restriccion_excepcion` · estrato **primaria** (disclosure: Cap 2.5.4/2.12.2.x hermanas de 2.1/2.3.1 quemados; puntos propios vírgenes)

**1. Perfil y síntoma.** Abstención; `correcta` + `parcial`; F = 0 · P = 2 (el piso;
las excepciones) (`expediente_gate2_1.md`, CQN2-015 §2). 15/15 tools, sin citas.

**2. Ramas pre-registradas.** Por pata: (A) completitud_kg; (B) alcanzabilidad_kg —
con la sub-rama B′ (entierro por ranking) pre-registrada desde CQN-009; (C) navegación.

**3. Exposición.**
- **Pata-piso: el portador existe, fiel y ENTERRADO POR RANKING (mecanismo B′).**
  `Restriccion_prohibicion_de_ponderador_menor_para_deudores_no_calificados` porta la
  regla del 2.5.4 (corpus p.12); en las consultas del agente quedó en **posición
  global 11 de 50 con límite 10** (paso 7; 12 de 50 en el paso 3 — barrido K-I): match
  léxico positivo, nunca visible. **Primera materialización del caso pre-registrado en
  CQN-009.** El D1 formal medido da negativo por UN SOLO puesto (mejor_rank 11 contra
  el corte top-10; medición verbatim en `cqn2_015.md`). **Nota de instrumento
  (laguna de D2):** la regla D2 decide por el corte binario top-10 y no contempla el
  entierro-por-ranking como mecanismo propio. Predicción pre-registrada (original): v6.2-D
  probablemente emita navegación. CORRECCIÓN PRE-CORRIDA (determinística, previa a todo
  head-to-head): la medición del D1 formal (alcanzable=False, mejor_rank 11) implica que
  la ruta D2/D7 de v6.2-D emitirá alcanzabilidad_kg — coincidiendo con la vara, pero por
  colapso de mecanismo: D2 no distingue el entierro-por-ranking (B′) de la
  inalcanzabilidad léxica. La laguna de instrumento subsiste como incapacidad de nombrar
  B′, no como error de veredicto esperado.
- **Pata-excepciones: el contenido de 2.12.2.2-.3 no existe** — K-I: "código de
  descuento" → 0 hits; "seguridad social" ∧ 30 → 0 hits (el corpus los tiene, p.23 —
  sonda en `cqn2_015.md`).
- **Conducta del agente: abstención disciplinada** — 13 sondas de valores (100%, piso,
  "sin calificación") sin afirmar jamás un valor no visto (pasos 4/5/13 en
  `cqn2_015.md`).

**4. VEREDICTO (por pata): pata-piso {context_recall, alcanzabilidad_kg} vía B′ ·
pata-excepciones {context_recall, completitud_kg}.**

---

## (a) Patrones transversales

1. **Bestiario de extracción — las cuatro especies del gate:**
   - **Amputación de cláusulas:** CQN2-005 (antecedente "ante la ARCA" — **segunda
     amputación de antecedente** del historial, tras CQN-010) y las **tres
     cláusulas-hermanas** del gate: CQN2-006 (la fórmula sin el glosario contiguo
     "ILM = 1"), CQN2-014 (las hermanas del 7.1 sin la oración final de límites),
     CQN2-015 (la regla del 2.5.4 presente y las excepciones 2.12.2.2-.3 ausentes).
   - **Provenance desplazada:** CQN2-002 (contenido del 9.2 de Capitales con provenance
     "9.1. Base individual") y el nodo-180 de CQN2-013 (contenido del 7.1.1.4 con
     provenance "6.12. Gobiernos locales") — backlog, sin síntoma propio en este gate.
   - **Fabricación de coletilla:** CQN2-011 — "sujetas a arancel" + label "Arancel a
     importaciones de aeronaves", 0 hits en corpus.
   - **Quimera label↔description:** CQN2-013 — label del 13.2.7.1 con description del
     13.2.6, con el hermano sano invisible al lado.
2. **Serie Sección 8 del RI ×3:** 70700000 (CQN-009), mapeo de la Sección 2 (CQN-011
   del gate CQN), fórmula 70200000 (CQN2-012) — tres agujeros consecutivos del mismo
   territorio en dos gates.
3. **Duplicación de gemelos ×2:** CQN2-005 (la nominación, dos nodos con la misma
   description + un tercero del 8.2) y CQN2-014 (la excepción, provenances 7.1 y 6.5).
4. **Hub contaminado:** `EntidadFinanciera_sujeto_obligado`, 991 entrantes de los cinco
   documentos — la entidad-clase como punto de contaminación inter-régimen (CQN2-010
   registro estructural; CQN2-011 los nodos del programa cuelgan de él).
5. **Contraste con el gate anterior:** las provenances salieron mayormente CORRECTAS
   (dos desplazadas, ambas sin síntoma propio); los defectos migraron a
   **contenido** (fabricación, quimera) **y alcanzabilidad** (entierro léxico, entierro
   por ranking, fragmentación).
6. **Conducta del agente — dos poblaciones:** 5 abstenciones disciplinadas
   (CQN2-005/006/010/012/015 — sondas de valores nunca afirmadas) contra 4 trasplantes
   (CQN2-002/004/011, y CQN2-013 inducido por el quimérico, con doble hedge).

## (b) FPs del juez — recuento por variante

De los 22 claims reprobados del censo, **12 son FP del juez**:

- **Cita-estrecha (ejemplar canónico #2): CQN2-007 ×4** — fiel al nodo Y al corpus del
  punto del GT, fuera solo de la `cita_textual` del eval set.
- **Marco estrecho: CQN2-002 ×1** (casa-matriz, con gemelo en dos TOs), **CQN2-004 ×4**
  (plazos residuales ×2 + opciones ×2), **CQN2-011 ×1** (la lista 8802, verbatim del
  nodo y del corpus), **CQN2-012 ×2** (Cap 1.3 e integración diaria 6.7.1, nodos fieles
  con provenance correcta).

Los 10 restantes son defectos reales adjudicados arriba (o manifestaciones del mismo
defecto, CQN2-013).

## (c) Reglas de acierto por caso — para el head-to-head A TRES COLUMNAS (v6.1-D / v6.2-D / v7')

Acierto = el voto final del sistema compuesto coincide con la PRIMARIA adjudicada
(pares primarios, mayoría; triage derivado se lee aparte con su motivo). Los casos "por
pata" aceptan cualquiera de sus dos claves como acierto de la pata correspondiente.

| Caso | Estrato | Acierto = | Nota |
|---|---|---|---|
| CQN2-002 | primaria | exoneración-con-secundarias {ns, aplicacion_erronea} o triage | sin primaria: cualquier PRIMARIA confiada = miss |
| CQN2-004 | primaria | {noise_sensitivity, aplicacion_erronea} | contenido_kg NO es acierto (el nodo RI-12.2 es fiel) |
| CQN2-005 | primaria | por pata: {cr, completitud_kg} (ARCA) · {cr, alcanzabilidad_kg} (condición) | navegación NO es acierto (sin top-N en 16 pasos) |
| CQN2-006 | primaria | {context_recall, completitud_kg} | el D1 en runtime del propio agente (paso 14) respalda |
| CQN2-007 | primaria | exoneración total (sin_defecto) | cualquier defecto = miss; triage por enrutamiento se lee aparte |
| CQN2-010 | solapada | {context_recall, completitud_kg} | atribuir a la pata 6.3.1 (perfecta) invalida |
| CQN2-011 | primaria | {noise_sensitivity, aplicacion_erronea} | la concurrente {ns, contenido_kg} suma, no se exige; patas con sus claves |
| CQN2-012 | solapada | {context_recall, completitud_kg} | atribuir defecto a los secundarios (FPs) invalida |
| CQN2-013 | solapada | {noise_sensitivity, contenido_kg} | aplicacion_erronea SOLA no es acierto (es la concurrente secundaria) |
| CQN2-014 | primaria | {context_recall, completitud_kg} | las hermanas fieles descartan contenido_kg |
| CQN2-015 | primaria | por pata: {cr, alcanzabilidad_kg} (piso, vía B′) · {cr, completitud_kg} (excepciones) | predicción corregida pre-corrida: v6.2-D emitirá alcanzabilidad en la pata-piso por colapso de mecanismo (D1 formal negativo); acierto = la clave, no el mecanismo |

Las tres solapadas (CQN2-010/012/013) se reportan además por separado con su disclosure
del sellado.

## (d) Correcciones al censo

**Ninguna.** Verifiqué los conteos F/P y la marca de centralidad de los 11 casos contra
la descomposición verbatim del juez en `expediente_gate2_1.md` §2/§5: coinciden en los
11.

---

**Versión:** vara del gate CQN2 v1 — 2026-07-19. **Sellado por inexistencia:** al
momento de escribir esto, ningún veredicto del verificador (ninguna versión), de las
capas (v6.1-D/v6.2-D) ni de S1 (ninguna versión) existe sobre estos 11 casos; el
head-to-head a tres columnas pre-registrado (diseño ciclo 2 §1, mismo material,
estratos del sellado) recién puede correr después del commit de esta vara.
