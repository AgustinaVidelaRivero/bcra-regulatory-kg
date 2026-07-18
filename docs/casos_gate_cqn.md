# Casos del GATE CQN — vara de adjudicación (la última vara del proyecto)

Vara del **gate de v7**: las 10 fallas con síntoma no vacío de la corrida CQN sobre run_3
(censo en la zona de trabajo; trazas congeladas de la corrida del gate). **Adjudicada
ANTES de cualquier corrida del verificador o de S1 — sellado por inexistencia: sus
veredictos sobre este material no existen y no existirán hasta el commit de esta vara.**
**Vocabulario:** taxonomía v2.6.1. **Circuito:** el de la vara — expediente con fidelidad
runtime↔re-ejecución verificada (132/132 pasos), barrido determinístico sobre el kg
congelado (`docs/evidencia_gate_cqn/barrido_kg_gate_cqn.md`, ítems K), verificación
contra los PDF del corpus con página, y ramas pre-registradas antes de la exposición.

**Evidencia:** `docs/evidencia_gate_cqn/` (un archivo por caso, `cqn_001.md`…`cqn_014.md`,
con los extractos verbatim que cada sección cita + el barrido íntegro).

**El eval set:** `queries/eval_set_cqn.json` (sellado, `2b8d449`) — 11 primarias, 3
solapadas con disclosure, 1 ilustrativa no puntuable. Corrí el sistema con el derivado
`eval_set_cqn_runtime.json` (`89f693d`), que solo duplica un campo por contrato del juez.

---

## CQN-001 — `factual_directa` · estrato **solapada** (GT compartido con CQ-034)

**1. Perfil y síntoma.** Abstención parcial; correctitud `correcta`, completitud
`parcial`; F = 1 claim secundario `no_soportado` (el límite anual USD 36.000) · P = 4
patas no cubiertas (el monto por concepto y el tope conjunto)
(`expediente_gate_1.md`, CQN-001 §2). `hit_tool_limit: true` (15/15 tools).

**2. Ramas pre-registradas.** (A) completitud_kg — la cláusula del USD 200 mensual no
existe en el grafo; (B) alcanzabilidad/navegación — existe y no se llegó; (D) el dato
estuvo expuesto en outputs y el agente no lo usó; y por separado, el secundario del
36.000: ¿alucinación del agente o FP del juez?

**3. Exposición.**
- **La cláusula no existe.** Barrido K1: **0 hits de contenido** para "USD 200"/"doscientos"
  + "mes calendario" en todo el kg; el único hit del territorio 3.9 es
  `Comunicacion_a_6796`, una cáscara (label "Com. A 6796", sin contenido normativo) cuya
  provenance cita "Punto 3.9. A 6770 6." (`cqn_001.md`, ítem K1).
- **La hermana existe.** `Restriccion_limite_mensual_de_compra_en_efectivo` (umbral
  **USD 100**, provenance 3.8) está completa (K2) con 3 salientes/0 entrantes (K4): el
  pipeline extrajo la cláusula del efectivo y OMITIÓ la principal del mismo territorio
  3.8/3.9 del corpus (`cqn_001.md`, corpus: Punto 3.8 y 3.9 de Exterior).
- **Rama D descartada.** En los 15 outputs re-ejecutados no aparece "3.9" ni el USD 200
  del GT; el único "USD 200" visible es el nodo de retiros en el exterior del 4.1.1 —
  contenido corpus-real de OTRO punto (`cqn_001.md`, pasos y corpus 4.1.1).
- **El secundario del 36.000 es FP del juez, marco gold estrecho:** el nodo real fue
  visto en el paso 13 y su contenido es corpus-real (Exterior, mecanismo de cobros de
  exportaciones de servicios; provenance del nodo "Punto 2.2" — K2). La cita del 3.10 de
  la respuesta es fiel a su nodo (`Operacion_formacion_de_activos_externos`, provenance
  única 3.10 — la pata de "otros residentes").
- **Hechos registrados:** hubs con 0 salientes en los pasos 11 y 15; el nodo
  `Operacion_compra_de_moneda_extranjera` lleva description del título del 3.8 con
  provenance 3.11 (paso 6); dos pasos quemados en sondas de montos inexistentes
  (USD 300/1000).

**4. VEREDICTO: {context_recall, completitud_kg} PRIMARIA.** Omisión de la cláusula
principal del territorio 3.8/3.9 — no amputación: la cláusula entera falta, no está
recortada. El secundario del 36.000 NO es defecto (FP del juez, marco estrecho). La
abstención del agente fue honesta sobre un grafo incompleto.

---

## CQN-006 — `factual_directa` · estrato **primaria**

**1. Perfil y síntoma.** Respondida; `correcta` + `completa`; F = 1 claim secundario
`no_soportado` (el alcance del reintegro a tasas/comisiones/cargos) · P = 0
(`expediente_gate_1.md`, CQN-006 §2). Tres pasos de trayectoria.

**2. Ramas pre-registradas.** ¿alucinacion_agente (la respuesta agregó el alcance) o
sin_defecto (FP del juez)?

**3. Exposición.** El claim secundario está **VERBATIM en el nodo abierto en el paso 3**
(`cqn_006.md`, paso 3) Y es **corpus-real**: el 2.3.5.1.i de Protección lo dice — página
15 del documento (verificado además por tesseract sobre esa página) — dentro del propio
punto 2.3 del GT, fuera SOLO de la `cita_textual` del eval set. La respuesta dio las dos
ramas del plazo (10 días tras reclamo / 5 tras constatación), exactamente lo que la
disclosure de la vara exige.

**4. VEREDICTO: SIN_DEFECTO.** FP del juez, **variante cita-estrecha** — el juez midió
contra la cita del eval set, no contra el punto del GT; el contenido reprobado es fiel al
nodo y al corpus. **Queda registrado como ejemplo canónico de la variante.**

---

## CQN-007 — `factual_directa` · estrato **primaria**

**1. Perfil y síntoma.** Abstención; `correcta` + `parcial`; F = 0 · P = 1 (la
circunstancia de "entidad atípica") (`expediente_gate_1.md`, CQN-007 §2). 13/15 tools.

**2. Ramas pre-registradas.** (A) completitud_kg — el umbral no existe; (B)
alcanzabilidad_kg — existe pero inalcanzable por léxico; (C) navegación — existe,
alcanzable o señalizado, y el agente no lo abrió.

**3. Exposición.**
- **El nodo existe, sano y completo:** `Restriccion_limitacion_eve_sobre_capital_nivel_1`
  — umbral 15%, base capital nivel 1, la designación "entidad atípica" en su contenido,
  provenance 8.1 (barrido K5, dump íntegro en `cqn_007.md`). Corpus: página 37 del RI.
- **Su puntero ESTUVO EN PANTALLA en el paso 8:** el `ver_vecinos` mostró label, la
  relación `limita` y la provenance 8.1 (`cqn_007.md`, paso 8), con presupuesto disponible
  (13/15 tools usados). **Contrafáctico:** un `ver_nodo` sobre ese id respondía la pata
  entera.
- **El D1 léxico negativo es real y lo ejecutó el propio agente:** paso 3, consulta con
  "atípica" → `total_con_match: 0` (`cqn_007.md`, paso 3). Y "atípica" no vive en ningún
  otro nodo (K6: los 8 hits restantes son del substring "15", no de la designación). Pero
  la vía ESTRUCTURAL entregó el puntero — no es alcanzabilidad.

**4. VEREDICTO: {context_recall, navegación} PRIMARIA.** El grafo tenía la pieza y la
señalizó por la vía estructural; el agente no la abrió teniendo presupuesto.

---

## CQN-008 — `multi_norma` · estrato **ilustrativa_no_puntuable** — lectura DESCRIPTIVA

**1. Perfil y síntoma.** Respondida; `correcta` + `completa` según el juez pero con F = 9
claims `no_soportado` (7 centrales) · P = 0 (`expediente_gate_1.md`, CQN-008 §2).
Reformulación del territorio de CQ-017/CQ-018 (quemado en 3 grafos) — **se corre y
reporta aparte, no integra métricas** (disclosure del sellado).

**2. Ramas pre-registradas.** Lectura descriptiva por pata (sin scoring): ¿qué soporta el
grafo, qué agregó el agente, qué reprobó el juez de más?

**3. Exposición (descriptiva).**
- **Pata 1 correcta:** el "Directivo Responsable" está soportado VERBATIM por el nodo del
  paso 10 (provenance 3.2; corpus Protección 3.2 en `cqn_008.md`); "todas las
  obligaciones" es una generalización sin soporte.
- **Pata 2, el desvío:** la respuesta citó el 10.1 pero respondió con contenido del 6.4
  (nodo del paso 15) y tramos de la cartera COMERCIAL 6.5.4.x (nodos de tramos; corpus
  6.5.4.6/.7/.8 de Clasificación en `cqn_008.md`). **El mandato del 10.1** (mora + cartera
  de consumo/vivienda + recategorización del 7.3) **nunca apareció como contenido** (0
  hits en outputs; corpus 10.1 en página 43).
- **De los 9 reprobados: 7 = FP del juez de marco estrecho** (tienen soporte real en
  3.2/6.4/6.5.4, corpus-reales), de los cuales 2 con deformación leve (un nodo
  descompuesto en dos criterios); **1 sin soporte** (la generalización).
- El ítem K7 del barrido queda al pie como inventario de lo que el grafo SÍ porta del
  territorio 10.1 (`cqn_008.md`, ítem K7).

**4. VEREDICTO: lectura descriptiva — NO PUNTÚA.** El caso ilustra a la vez el marco
estrecho del juez y el desvío de dominio del agente sobre territorio quemado; nada de
esto entra al head-to-head.

---

## CQN-009 — `multi_norma` · estrato **primaria** (disclosure leve: GT compartido con CQ-010)

**1. Perfil y síntoma.** Abstención; `correcta` + `parcial`; F = 0 · P = 1 (el importe
del total de control) (`expediente_gate_1.md`, CQN-009 §2). 15/15 tools.

**2. Ramas pre-registradas.** (A) completitud_kg — el puente 8.1.3→1.2 no existe; (B)
alcanzabilidad/navegación; (D) expuesto en outputs. **Criterio de lectura pre-registrado
antes de la exposición:** la respuesta que NIEGA el puente explícitamente no es FP de
cobertura.

**3. Exposición.**
- **El puente del GT no existe en run_3.** El 8.1.3 del corpus (código 70700000 → remite
  al 1.2 de Capitales; página 37 del RI, extracto en `cqn_009.md`) no tiene portador:
  barrido K8 — **cero hits de "70700000" y de provenance 8.1.3**; los únicos portadores
  de "total de control" son los dos nodos EVE (partida 70500000 — el total de control
  EQUIVOCADO para esta pregunta).
- **Rama D muerta:** 0 apariciones del código/puente en los 15 outputs; los 6 hits de
  "total de control" en outputs son ecos de las propias consultas (`cqn_009.md`).
- **La búsqueda del agente fue de alta calidad:** 11 consultas directas al blanco
  (inventario en `cqn_009.md`; una con límite 15). K9: los candidatos EVE ni siquiera
  rankean para la mayoría de esas consultas — no había nada que encontrar.
- **Sin FP de cobertura:** la respuesta niega el puente explícitamente; el criterio quedó
  pre-registrado antes de la exposición.

**4. VEREDICTO: {context_recall, completitud_kg} PRIMARIA.** El puente 8.1.3 no fue
extraído; abstención honesta con búsqueda ejemplar.

---

## CQN-010 — `multi_norma` · estrato **primaria**

**1. Perfil y síntoma.** Respondida; `correcta` (del juez) + `completa`; F = 1 secundario
`no_soportado` ("proviene del BCRA") · P = 0 (`expediente_gate_1.md`, CQN-010 §2).

**2. Ramas pre-registradas.** Sobre la segunda central aprobada (la emisora del
certificado): ¿es materialmente verdadera? — con la decisión de alcance pre-registrada de
adjudicar por VERDAD MATERIAL (el caso completo, no solo el síntoma del censo),
consistente con cómo la vara v3 corrigió al juez en la dirección inversa.

**3. Exposición.**
- **La segunda central es materialmente FALSA por conflación:** el corpus dice que la
  emisora es la entidad NOMINADA para el seguimiento de la operación/financiación —
  9.2 de Exterior, con su antecedente "Por cada operación… deberá seleccionar una
  entidad… Esta entidad será la única responsable…" (`cqn_010.md`, corpus 9.2).
- **Los dos nodos portadores amputan el antecedente y reescriben "Esta entidad"→"La
  entidad"** (pasos 10 y 12: `Operacion_emision_de_certificado` y
  `Obligacion_la_entidad_sera_la_unica_responsable_de_emitir_los_certificados_qu…`,
  dumps verbatim en `cqn_010.md`) — **amputación de cláusulas, variante ANTECEDENTE
  ANAFÓRICO**: sin el antecedente, "la entidad" queda flotando y habilita la conflación
  con la entidad encargada del permiso de embarque.
- **Provenance de ambos = rebanada del listado 9.1.6/9.1.7 precedente** ("Punto 7.10.
  9.1.7. Aportes de inversión extranjera…") — **provenance desplazada por ventana de
  extracción**; explica la cita de la respuesta.
- **Nota de conexión (K11):** los fragmentos del 9.2 SÍ existen en el grafo (incluido "el
  seguimiento estará a cargo de la entidad que otorgó la financiación") y el fragmento
  clave porta LA MISMA provenance corrupta — el 9.2 fue extraído FRAGMENTADO con la
  ventana corrida. La primaria no cambia por esto.
- **FN del juez, registrado como hallazgo:** marcó `verdadero` la segunda central por
  solapamiento superficial con la cita — mecanismo nuevo (el inverso del FP de marco
  estrecho), documentado para la serie del juez.
- **El secundario "proviene del BCRA" = FP del juez:** soportado por múltiples outputs.

**4. VEREDICTO: {noise_sensitivity, contenido_kg} PRIMARIA + {noise_sensitivity,
provenance_imprecisa} SECUNDARIA.** El FN del juez queda como hallazgo; el secundario
reprobado no es defecto. Adjudiqué por verdad material bajo la decisión de alcance
pre-registrada.

---

## CQN-011 — `multi_norma` · estrato **primaria**

**1. Perfil y síntoma.** Respondida; `incorrecta` + `parcial`; F = 2 centrales `falso`
(el código de consolidación 3) · P = 1 (el caso de entidad) (`expediente_gate_1.md`,
CQN-011 §2).

**2. Ramas pre-registradas.** Claims falsos: ¿contenido_kg (nodo infiel) o
aplicacion_erronea (nodo fiel de otro régimen, alcance declarado)? Pata 2: ¿completitud o
alcanzabilidad?

**3. Exposición.**
- **El agente tuvo la pieza correcta en la mano:** paso 3 — el nodo EVE con "códigos de
  consolidación 0 o 1 y 2" (`cqn_011.md`, paso 3).
- **Basó la respuesta en el nodo de OTRO régimen:** paso 4 — nodo con provenance 10.1
  (coeficiente de apalancamiento) que dice código 3 (`cqn_011.md`, paso 4). Y **ignoró
  DOS VECES el nodo de la suspensión del código 3 desde abril/24** (pasos 6-7).
  Grounded≠correct, lado agente: contenido fiel usado fuera de su alcance declarado.
- **Pata 2 — el mapeo no existe:** barrido K12, **0 hits** del mapeo de la Sección 2
  (código 2 → consolidado mensual → filiales y subsidiarias significativas país y
  exterior). **Contrafáctico:** usando bien lo visto, el agente decía "código 2" — pero el
  caso de entidad era inalcanzable. Corpus: Sección 2 en página 4 del RI (donde además el
  código 3 figura suspendido), 11.1 en página 46 (`cqn_011.md`).
- **Provenances desplazadas en los tres nodos abiertos** (títulos de otra cosa; dumps en
  `cqn_011.md`).

**4. VEREDICTO: {noise_sensitivity, aplicacion_erronea} PRIMARIA (los claims) +
{context_recall, completitud_kg} (la pata 2) + {noise_sensitivity, provenance_imprecisa}
SECUNDARIA.**

---

## CQN-012 — `multi_norma` · estrato **solapada** (GT 1.1 compartido con CQ-020, quemado ×2; pata 7.4 virgen)

**1. Perfil y síntoma.** Respondida; `incorrecta` + `completa`; F = 1 central `falso`
(la regla de determinación como "suma… junto con otras exigencias") + 1 secundario
`no_soportado` · P = 0 (`expediente_gate_1.md`, CQN-012 §2).

**2. Ramas pre-registradas.** El central falso: ¿contenido_kg (nodo que dice la regla
mal) o aplicacion_erronea (el agente estiró un nodo fiel)? ¿Existe la regla del 1.1 en
el grafo?

**3. Exposición.**
- **Génesis del claim falso:** el agente estiró el nodo del RI 7.1
  (`Operacion_calculo_de_exigencia`, paso 9 — una LISTA de componentes con provenance
  "Punto 7.1. Normas de procedimiento") a regla de determinación ("suma… junto con otras
  exigencias regulatorias") (`cqn_012.md`, paso 9).
- **Sospechó la estructura correcta y no se abstuvo:** la consulta del paso 15
  ("exigencia capital máximo mayor entre riesgo crédito mercado operacional") muestra que
  buscaba el mayor-valor; no lo encontró y AFIRMÓ la suma en vez de abstenerse
  (`cqn_012.md`, paso 15).
- **La regla del 1.1 no existe en run_3:** barrido K13 — el único hit de "mayor valor" es
  un FALSO AMIGO (RI 12.2: "mayor valor entre códigos 70810000/70820000", otra cosa).
  Corpus: 1.1 y 7.4 de Capitales verbatim en `cqn_012.md`.
- **Sin FP en el central** (la respuesta no menciona básica/mayor-valor en ninguna
  frase); **el secundario "metodologías específicas" = FP del juez** (soporte difuso real
  en los outputs).
- **La pata 7.4 (virgen) salió PERFECTA** — la falla vive íntegra en el territorio 1.1
  quemado (dato para la lectura del estrato solapado).

**4. VEREDICTO: {noise_sensitivity, aplicacion_erronea} PRIMARIA + completitud_kg
SECUNDARIA (causa concurrente, sin síntoma propio: condición habilitante del claim falso
— la regla del 1.1 no existe en run_3, K13); el secundario reprobado = FP del juez.**

---

## CQN-013 — `cadena_restriccion_excepcion` · estrato **primaria**

**1. Perfil y síntoma.** Respondida; `correcta` + `completa`; F = 1 **central**
`no_soportado` (el artículo 41) · P = 0 (`expediente_gate_1.md`, CQN-013 §2).
**CORRECCIÓN AL CENSO** (registrada en la sección b): el único fallido es CENTRAL, no
"secundario suelto".

**2. Ramas pre-registradas.** ¿alucinacion_agente (glosa) / aplicacion_erronea
(contenido fiel de otro dominio) / contenido_kg (nodo infiel)? ¿El juez acertó?

**3. Exposición.**
- **El claim del art. 41 es VERBATIM de un nodo real abierto por el agente** (paso 11:
  `Restriccion_los_incumplimientos_en_el_envio_de_la_informacion_estaran_sujetos_a_la_aplicacio…`,
  dump en `cqn_013.md`) **cuyo contenido pertenece a Exterior 1.6** (régimen informativo
  CAMBIARIO).
- **Protección NO contiene ninguna cláusula del art. 41:** grep exhaustivo del documento
  completo — **CERO apariciones** de "artículo 41"/"art. 41" (`cqn_013.md`, grep
  negativo). La respuesta lo presenta como consecuencia sancionatoria de las normas de
  PROTECCIÓN: **salto de alcance del agente — trasplante de dominio.**
- **Provenances desplazadas ×2:** el nodo del art-41 lleva provenance 1.5 (contenido del
  1.6); el nodo de la cadena (paso 5, `Obligacion_aplicacion_de_sanciones_por_incumplimiento`)
  lleva contenido de la Sección 5 VERBATIM con provenance "Punto 4.4" — explica la cita
  de la respuesta (`cqn_013.md`, pasos 5 y 11; corpus Exterior 1.5/1.6).
- **El juez, sin FP y con flag humano acertado:** el `no_soportado` es correcto y
  `requiere_adjudicacion_humana: true` se levantó exactamente donde correspondía.
- Par de capa 1 por el árbol v2.6.1: claim anclado verbatim en nodo consultado (rama
  noise_sensitivity), nodo fiel a su PDF, alcance declarado EN el nodo (la provenance con
  source_doc Exterior fue visible en el ver_nodo del paso 11) → aplicacion_erronea por la
  desambiguación v2.6.

**4. VEREDICTO: {noise_sensitivity, aplicacion_erronea} PRIMARIA (trasplante de dominio) +
{noise_sensitivity, provenance_imprecisa} ×2 SECUNDARIA.**

---

## CQN-014 — `cadena_restriccion_excepcion` · estrato **solapada** (GT 7.3 compartido con CQ-033; familia 12.3)

**1. Perfil y síntoma.** Abstención; `correcta` + `parcial`; F = 0 · P = 1 (la exigencia
con n=0) (`expediente_gate_1.md`, CQN-014 §2).

**2. Ramas pre-registradas.** Bifurcación registrada antes de la exposición: **(E)
contenido_kg** — el agente alcanzó contenido DEFECTUOSO de la familia 12.3 y eso deterió
la respuesta — **vs (C/D′) navegación** — los nodos sanos del 7.3 estaban al alcance y no
los abrió.

**3. Exposición.**
- **La mejor consulta del agente le entregó — y el agente ABRIÓ (paso 8) — el nodo de la
  variante transitoria del 12.3** disfrazado de límite del 7.3: "hasta el 30/06/26… 17%",
  provenance "entidades reclasificadas desde el 01/01/2026" (`cqn_014.md`, paso 8). Es
  **el defecto adjudicado de la familia que la disclosure selló**, materializado en el
  punto de contacto: su contenido condicionado ("hasta el 30/06/26", "reclasificadas")
  deterió LEGÍTIMAMENTE la afirmación — un lector honesto de ese nodo no afirma el límite
  general.
- **Los nodos sanos existen y surfearon:** K14 — los dos nodos del 7.3.1/7.3.2 con
  descriptions completas (20%/17%) y provenance correcta "Punto 7.3. Límite para las
  entidades del grupo 2" (`cqn_014.md`, ítem K14); aparecieron repetidas veces en
  listados con los porcentajes visibles y NO fueron abiertos.
- **Ruido del territorio registrado:** los nodos sosías de "límite de reducción 17/11/7"
  (otros porcentajes del mismo campo léxico). Corpus: 7.3 y 12.3 de Capitales en
  `cqn_014.md`.
- **Decisión E vs C/D′:** decidí **E** por el contrafáctico del lado grafo (con el 12.3
  no-defectuoso — o correctamente scopeado — la abstención no ocurre: el agente ya había
  alcanzado "17%" y lo descartó por el condicionamiento espurio del nodo) y por el
  tratamiento taxonómico de "agente alcanza contenido defectuoso".

**4. VEREDICTO: {context_recall, contenido_kg} PRIMARIA (familia 12.3) +
{context_recall, navegación} SECUNDARIA (los nodos sanos del 7.3, señalizados y no
abiertos).**

---

## (a) Patrones transversales

1. **Provenance desplazada (por ventana de extracción):** 7 nodos en 3 casos —
  CQN-010 ×2 (rebanada del listado 9.1.6/9.1.7), CQN-011 ×3 (títulos de otra cosa),
  CQN-013 ×2 (1.5 por 1.6; 4.4 por Sección 5) — más los fragmentos del 9.2 de K11 con la
  MISMA provenance corrupta. Mecanismo: la ventana de extracción corrida respecto del
  punto que el contenido realmente funda.
2. **Grounded≠correct, lado agente ×3:** CQN-011 (código 3 de otro régimen, con la pieza
  correcta ya vista), CQN-012 (lista de componentes estirada a regla), CQN-013
  (trasplante de dominio del art. 41). En los tres, el contenido citado es fiel a su
  nodo; el error es de aplicación.
3. **FP del juez:** marco estrecho en CQN-001/008/010/012 + la **variante cita-estrecha
  canónica** en CQN-006 (fiel al nodo Y al corpus del punto del GT, fuera solo de la
  cita del eval set).
4. **FN del juez ×1 (mecanismo nuevo):** CQN-010 — un `verdadero` otorgado por
  solapamiento superficial con la cita, sobre un claim materialmente falso.
5. **Amputación de cláusulas +1:** CQN-010, variante ANTECEDENTE ANAFÓRICO ("Esta
  entidad"→"La entidad" sin el antecedente) — séptima aparición del patrón bautizado en
  la vara de dev.

## (b) Correcciones al censo

- **CQN-013:** el censo listó el fallido del art. 41 como secundario suelto; la
  descomposición del juez lo marca **CENTRAL** (`expediente_gate_1.md`, CQN-013 §2). El
  conteo correcto del caso es F = 1 central `no_soportado`.

## (c) Reglas de acierto por caso — para el head-to-head v6.1-D vs v7

Acierto = el voto final del sistema compuesto coincide con la PRIMARIA adjudicada (regla
del gate de siempre: pares primarios, mayoría; triage derivado se lee aparte con su
motivo). Por caso:

| Caso | Estrato | Acierto = | Nota |
|---|---|---|---|
| CQN-001 | solapada | {context_recall, completitud_kg} | atribuir defecto al secundario del 36.000 invalida |
| CQN-006 | primaria | exoneración total (sin_defecto) | cualquier defecto = miss; triage por R1/R6a = enrutamiento esperado |
| CQN-007 | primaria | {context_recall, navegación} | alcanzabilidad_kg NO es acierto (el puntero estructural estuvo en pantalla) |
| CQN-008 | ilustrativa | — NO PUNTÚA | se corre y reporta aparte |
| CQN-009 | primaria | {context_recall, completitud_kg} | atribuir FP de cobertura a la negación explícita invalida |
| CQN-010 | primaria | {noise_sensitivity, contenido_kg} | la secundaria de provenance suma, no se exige |
| CQN-011 | primaria | {noise_sensitivity, aplicacion_erronea} | completitud de la pata 2 como acompañante es válida; sola NO es acierto |
| CQN-012 | solapada | {noise_sensitivity, aplicacion_erronea} | contenido_kg no es acierto (el nodo es fiel; el estiramiento es del agente) |
| CQN-013 | primaria | {noise_sensitivity, aplicacion_erronea} | alucinacion_agente NO es acierto (el claim es verbatim de un nodo real) |
| CQN-014 | solapada | {context_recall, contenido_kg} | navegación como PRIMARIA no es acierto (es la secundaria) |

Las tres solapadas (CQN-001/012/014) se reportan además por separado con su disclosure
(territorio compartido con CQ-034/CQ-020/CQ-033); CQN-008 queda fuera de toda métrica.

---

**Versión:** vara del gate CQN v1 — 2026-07-18. **Sellado por inexistencia:** al momento
de escribir esto, ningún veredicto del verificador (ninguna versión) ni de S1 existe
sobre estos 10 casos; el head-to-head pre-registrado (v6.1-D vs v7, mismo material,
estratos del sellado) recién puede correr después del commit de esta vara.
