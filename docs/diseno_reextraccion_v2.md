# Diseño de la re-extracción v2 (issue #8)

Este documento fija el diseño del pipeline de re-extracción del corpus completo
(los 5 Textos Ordenados de `data/experiment/subset/`, congelados por hash en su
manifiesto), partiendo de los PDFs y sin heredar ninguno de los parches manuales
C1–C7 aplicados sobre el grafo v3. Es un documento de diseño para laudo: no
autoriza ninguna corrida ni fija modelos o precios concretos — eso pertenece a
la unidad de implementación y a su corrida de calibración. Todo número citado
lleva la ruta o el comando que lo reproduce.

---

## 1. Objetivo y motivación empírica

El objetivo es re-extraer el corpus con un pipeline v2 diseñado desde los
defectos conocidos, en lugar de seguir corrigiendo a mano el grafo v3. La
motivación tiene dos patas, ambas medidas en este repo.

**(a) La corrección manual no escala.** El ciclo C1–C7 —siete correcciones con
propuesta sellada, aplicación y re-test cada una— consumió una semana de
trabajo: las propuestas y aplicaciones van del 2026-07-31 (C1, C2) al
2026-08-03 (C5, C6, C7), con re-tests documentados en
`data/backlog/retests/C{1..7}_retest_*.md` (siete archivos; `ls
data/backlog/retests/`). Esas siete correcciones tocaron puntos de cuatro de
los cinco TOs (Clasificación de Deudores: C1 y C5; Capitales Mínimos: C2, C3 y
C4; Protección de Usuarios: C6; Régimen Informativo: C7) y resolvieron siete
entradas del backlog. El backlog vigente registra **27 ids únicos**
(reproduce: `python3 -c "import json; print(len({json.loads(l)['id'] for l in
open('data/backlog/backlog.jsonl') if l.strip()}))"` sobre
`data/backlog/backlog.jsonl`). A ese ritmo —una semana por siete defectos, cada
uno con su expediente— agotar el backlog costaría un mes de trabajo artesanal,
y el backlog no está cerrado: sigue creciendo con cada fuente de intake. Peor:
varias entradas quedaron explícitamente adjudicadas como "registro y caso de
prueba para la re-extracción v2, no corrección a aplicar" (por ejemplo
BKL-0024 y BKL-0025 en `data/backlog/backlog.jsonl`), porque restaurar puntos
enteros a mano ya no es una corrección sino una re-extracción encubierta.

**(b) El backlog es especificación y batería de pruebas a la vez.** Los 27 ids
del backlog no son solo deuda: cada defecto diagnosticado —con su especie del
bestiario, su ancla al PDF y su evidencia— define un comportamiento esperado
del extractor v2. Un pipeline que parte de los PDFs debe capturar nativamente
el punto 3.9 que BKL-0024 documenta como ausente, la salvedad que C6 restauró
a mano, los calificadores que C7 repuso. Eso convierte al backlog en una
batería de pruebas de respuesta conocida: el delta entre lo que el grafo
v2-reextraído captura de fábrica y lo que v3 necesitó parchear es el número de
mejora del pipeline (desarrollo en §5).

---

## 2. Principios de diseño

**(a) Cuatro condiciones de viabilidad por etapa.** Cada etapa del pipeline
cumple: output verificable (un artefacto que otro proceso puede chequear sin
confiar en el productor), acción reversible (nada entra al grafo de forma que
no pueda deshacerse), horizonte corto (cada unidad de trabajo termina y se
evalúa antes de encolar la siguiente), y entorno acotado (cada llamada LLM ve
solo el material de su unidad, nunca el corpus entero).

**(b) Split mecánico/juicio.** Lo determinístico va en código; lo
interpretativo va en LLM. Un nodo del pipeline solo es un LLM cuando la tarea
exige juicio (extraer semántica de prosa normativa, detectar una omisión de
sentido); segmentar, ensamblar, contar, validar firmas y verificar provenance
son código puro. Esta regla decide la tecnología de cada etapa de §3.

**(c) Separación worker/verifier.** Ningún verificador comparte contexto con
el productor de lo que verifica. La evidencia del proyecto es directa: hubo
amputaciones que sobrevivieron a extractores que tuvieron el texto completo a
la vista (BKL-0005: el punto 7.1 del Régimen Informativo entró al grafo
despojado de sus dos calificadores, con el texto fuente en el prompt). Un
modelo revisando su propio output en su propio contexto es el juez más débil.

**(d) Anclas determinísticas no negociables.** Cuatro invariantes se validan en
código y no admiten excepción por juicio de ningún LLM: la validación de
shapes (SHACL vía `scripts/shapes_validator/`), el sistema de sujetos del
esquema v2 (extremos sujeto resueltos contra el esqueleto cerrado, con
cuarentena para lo no resoluble — en las corridas históricas documentadas el
mecanismo operó sin errores: descartes `sujeto_id_invalido: 0` y
`sujeto_propuesto_vacio: 0` en los smokes de
`data/experiment/grafo_v2/informes/U4*_2026-07-18.md`, y la lectura del
escalón 1 registra que el esquema v2 "eliminó por completo las fallas de
mecanismo de sujetos",
`data/experiment/evaluacion_escalon1/lectura_P1P5_escalon1.md`), el sha256 de
todo insumo, y los conteos de control en cada frontera de etapa.

**(e) Invariantes de provenance.** Todo nodo y toda arista llevan fuente a
nivel inciso (documento + punto + rol documental del segmento). Todo merge es
aditivo y reversible: conserva alias, evidencia textual y justificación, y
registra qué se fusionó con qué para poder deshacerlo.

**(f) Presupuesto de complejidad declarado por corrida.** Cada corrida declara
antes de empezar su tope de llamadas, tokens, costo y reintentos. Al agotarse
un tope, el pipeline reporta el trabajo parcial con su frontera exacta (qué
unidades quedaron sin procesar y por qué) en lugar de fallar silenciosamente o
degradar la calidad sin aviso.

---

## 3. Arquitectura: pipeline por etapas

El patrón general es fan-out / reduce / verify / synthesize: fan-out de
extracción por unidad estructural con contexto fresco, reduce determinístico
en código, verificación con contexto separado, y síntesis final bajo anclas
determinísticas.

### E0 — Chunking determinístico (código)

Segmentación anclada a la estructura normativa del TO, derivada del **cuerpo**
del documento — nunca del índice solo. La experiencia del chunker v1
(documentada en `docs/backlog_reextraccion.md`, ítems RX-01 a RX-08, y
auditada en `docs/tesis/auditoria_u0_29-07.md`) muestra que índice y cuerpo
divergen en ambas direcciones: hay puntos anunciados en el índice cuyo cuerpo
nunca obtuvo chunk propio (RX-04: 3 puntos medidos — `clasificacion_deudores`
1.1 y 4.5, `exterior_cambios` 9.2), y hay headers detectados en el cuerpo que
no corresponden a títulos reales (RX-03: 17 chunks espurios por referencias
cruzadas tomadas como títulos). Por eso E0 deriva el mapa estructural del
cuerpo y **reconcilia contra el índice como contraste, fallando ruidosamente
ante cualquier discrepancia** en lugar de resolverla en silencio — la
reconciliación índice↔cuerpo completa que el chunker v1 nunca tuvo.

Cada chunk es un punto numerado **más su cadena de herencia estructural**: el
chapeau de la sección, los párrafos introductorios y de cierre del punto
contenedor, y los encabezados de la jerarquía que lo contiene. Esta decisión
ataca directamente el mecanismo causal con más evidencia de la corrida U6: la
prosa sin numerar (encabezados, cierres, párrafos intersticiales) no
sobrevivió a la extracción v1/v3 mientras los sub-puntos numerados sí
(mecanismo "chapeau perdido", instancias U6-001, 005, 007, 015, 019 y 025 en
`data/experiment/exploracion/adjudicacion/notas_adjudicacion_u6.md` §2).

Cada chunk lleva su sha propio. Las tablas y fórmulas se detectan y rutean de
forma especial: tratamiento dedicado o flag explícito de contenido no-prosa,
nunca extracción ingenua — la evidencia U6 muestra estructura tabular
"visiblemente destrozada ya en extracción del PDF" (U6-022) y fórmulas con
anáfora rota (U6-018: el label dice "la expresión" y el antecedente no
sobrevivió). El alcance exacto del tratamiento dedicado es pregunta abierta
(§7.d).

### E1 — Fan-out de extracción (LLM chico, contexto fresco por chunk)

Un extractor aislado por chunk, con el esquema v2 como contrato de salida
estructurado y un prefijo de sistema estable y cacheado. Cada extractor ve
solo su chunk (con su herencia estructural de E0) — nunca el corpus, nunca los
outputs de otros extractores. Las cinco decisiones vigentes de prompt caching
(`docs/decisiones_caching_extraccion.md`) gobiernan esta etapa y son
vinculantes: prefijo estático con breakpoint explícito, nada variable por
chunk antes del breakpoint.

### E2 — Reduce en código (sin LLM)

Ensamblado determinístico: ids determinísticos (función del contenido y la
provenance, no del orden de llegada), validación de firmas de aristas contra
la matriz vigente de tipos, y **guarda de fan-in**: el conteo de chunks
esperados (del mapa de E0) contra los recibidos se verifica antes de
ensamblar. Jamás se ensambla sobre un conjunto parcial sin flag: un extractor
caído en silencio fabricaría una ausencia — precisamente la especie dominante
del backlog (7 de los 27 ids son `ausencia`; reproduce: agrupar el campo
`especie` de `data/backlog/backlog.jsonl` por id). El precedente es concreto:
el ensamblado v2 descartó 102 resultados de extracción por colisiones de
`chunk_id` (508 leídos − 406 sobrevivientes; RX-01 en
`docs/backlog_reextraccion.md`, cifra cerrada en
`docs/tesis/auditoria_u0_29-07.md`), y nadie lo supo hasta la auditoría.

E2 incluye además el **censo estructural determinístico**: contra el mapa de
E0, toda unidad estructural del documento debe tener al menos un nodo en el
grafo ensamblado. Las ausencias de punto entero solo son detectables contra el
mapa — mirando chunks individuales no se ve lo que falta. El caso de
referencia es BKL-0024: el punto 3.9 completo del TO de Exterior y Cambios
(tope de USD 200, subpuntos 3.9.1–3.9.5) ausente del grafo con cero nodos de
cuerpo, invisible para cualquier verificación por chunk porque ningún chunk lo
reclamaba.

### E3 — Verificador de completitud intra-unidad (LLM fuerte, contexto fresco)

Recibe el texto fuente de la unidad estructural y lo extraído de ella — jamás
el contexto del extractor (principio 2.c). Su blanco son las **amputaciones**:
el punto está presente pero despojado de calificadores, excepciones, ítems de
enumeración o modalidad. Devuelve feedback estructurado por faltante: tipo de
omisión, cita textual del fuente no representada, y ubicación.

Su prompt se calibra con ejemplos resueltos tomados del backlog — la
enumeración amputada (BKL-0004: niveles del 6.5 de Clasificación, restaurados
como C5), la salvedad ausente (BKL-0003: mutuales/cooperativas del 1.1.2.5 de
Protección, restaurada como C6), los calificadores despojados (BKL-0005: el
7.1 del Régimen Informativo, restaurados como C7) — siguiendo el hallazgo H12
del proyecto (`docs/hallazgos_tesis.md`): los jueces LLM honran calibradores
con ejemplos resueltos y circunvalan reglas declarativas equivalentes.

**Política de rechazo (mini-ratchet acotado):** el feedback se inyecta al
prompt del extractor y la unidad se re-extrae una vez (máximo dos; el tope
exacto es pregunta abierta, §7.a). Si el rechazo persiste, la unidad va a cola
humana con flag — **nunca ingreso silencioso al grafo**. El verificador jamás
corrige él mismo: detecta y documenta; corregir es del extractor o del humano.
Todos los veredictos se persisten como artefactos auditables. El precedente
publicado del patrón es FinReflectKG (loop de feedback iterativo con
validación estructural); acá se lo mejora con la separación estricta de
contextos entre productor y verificador.

### E4 — Resolución y deduplicación consciente de variación (LLM fuerte + código)

Resolución de entidades con caché de tipos para consistencia cross-chunk
(préstamo del paper 06, LINK-KG), y una **regla dura anti-fusión**: cláusulas
casi idénticas con valores, calificadores o modalidad distintos JAMÁS se
fusionan. La cláusula repetida en múltiples puntos vive como nodos separados,
cada uno con su provenance. El caso documentado que fija esta regla es U6-008:
la cláusula del límite del 125 % aparece casi textual en al menos 5 puntos del
TO de Exterior y Cambios (7.5.3, 7.8.5.1, 7.9.5, 7.11.5, 3.11.3.2;
`data/experiment/exploracion/adjudicacion/notas_adjudicacion_u6.md`), y la
hipótesis adjudicada es que la sobre-fusión de esas repeticiones rompió la
vecindad local del grafo. La evidencia U6 precisa además la condición del
daño: no es la repetición per se sino la **repetición-con-variación** más una
fusión indiferente al régimen (los controles positivos U6-013 y U6-017
muestran duplicados separados y variantes vecinas que no contaminaron). Todo
merge es aditivo, reversible y con registro (principio 2.e).

### E5 — Anclas finales (código)

Cierre determinístico: validación SHACL, chequeo del sistema de sujetos,
invariantes de provenance, labels con el contenido distintivo front-loadeado
(anti-colisión por truncamiento: U6-020 documenta tres nodos hermanos con
prefijo idéntico cuya diferenciación quedaba pasada la truncación del label),
conteos finales contra el censo de E2, y sha256 sellado del grafo resultante.

---

## 4. Decisiones de diseño y alternativas descartadas

### D1 — Chunking: punto + herencia estructural

**Adoptado:** el chunk de E0 (punto numerado + cadena de herencia).
**Descartado:**

- *(i) Chunks de tamaño fijo* — el default de la literatura (el paper 06 y
  GraphRAG segmentan en el orden de los 300 tokens). La fragmentación
  arbitraria disuelve las referencias cruzadas, y la evidencia propia del
  proyecto muestra que la prosa no numerada muere en los cortes: el mecanismo
  chapeau (§3-E0) es exactamente lo que un corte ciego a la estructura
  produce. Además el chunker v1 ya midió el costo de cortar por tope de
  caracteres: 51 chunks partidos por `HARD_CAP_CHARS` con relaciones cuyo
  antecedente quedó en otra parte (RX-06, `docs/backlog_reextraccion.md`).
- *(ii) Sección entera como chunk* — degradación de atención sobre contexto
  largo y re-extracciones caras: cualquier rechazo de E3 obligaría a re-pagar
  la sección completa en vez de un punto.
- *(iii) Ventanas con overlap* — rompen el anclaje estructural y la
  provenance: un hecho extraído de una ventana solapada no tiene un punto
  único al que atribuirse, y la provenance a nivel inciso (principio 2.e) es
  no negociable.

### D2 — Verificación: dos niveles, nunca auto-reflexión

**Adoptado:** censo determinístico (E2) + verificador LLM intra-unidad con
contexto separado (E3). **Descartado:** el gleaning / auto-reflexión del
propio extractor — el default de GraphRAG y su familia, donde el mismo modelo
que extrajo revisa su propio output en su propio contexto. Dos razones: es el
juez más débil (principio 2.c), y la evidencia del proyecto muestra
amputaciones que sobrevivieron a extractores con el texto completo a la vista
(BKL-0005). Si el extractor no vio la omisión al extraer, no hay motivo para
esperar que la vea al releerse.

### D3 — Modelos por etapa

Extracción (E1) con modelo chico y prefijo cacheado; verificación (E3) y
resolución (E4) con modelo fuerte. El precedente es el patrón
extractor-chico/resolutor-fuerte del Anthropic Knowledge Graph Construction
Cookbook. La elección puntual de modelos y sus precios NO se fija en este
documento: se fija contra la documentación oficial vigente en la corrida de
calibración de la unidad de implementación.

### D4 — Estrategia de corrida

Backfill del corpus vía Batch API con warm-then-parallel: una llamada inicial
puebla el caché del prefijo y recién entonces se lanza el fan-out en paralelo.
**Adopción condicional:** la unidad de implementación verifica contra la
documentación oficial vigente que los descuentos de batch y de caching
efectivamente se acumulan; si no se confirma, esta decisión vuelve a revisión
con números reales. Las cinco decisiones de caching vigentes
(`docs/decisiones_caching_extraccion.md`) gobiernan E1 en cualquier variante.

---

## 5. El backlog como especificación y batería de pruebas

El backlog (`data/backlog/backlog.jsonl`, 27 ids únicos) funciona como
especificación ejecutable del pipeline: cada especie de defecto mapea a la
etapa que la previene, y cada defecto concreto es un test de respuesta
conocida sobre el grafo v2-reextraído.

- **BKL-0024 → test del censo E2.** El punto 3.9 del TO de Exterior y Cambios
  (compra de moneda extranjera por personas humanas residentes, tope USD 200
  mensual, subpuntos 3.9.1–3.9.5) está ausente del grafo v3: cero nodos de
  cuerpo con provenance 3.9, con los puntos linderos 3.8 y 3.10 presentes
  (evento `triaged` de BKL-0024 en `data/backlog/backlog.jsonl`). El test: el
  censo estructural de E2 debe detectar cualquier unidad del mapa de E0 sin
  nodos, y el grafo v2 debe contener el 3.9 con provenance correcta.
- **Familia chapeau → test de la herencia E0.** Las seis instancias U6 del
  mecanismo "chapeau perdido" (U6-001, 005, 007, 015, 019, 025;
  `data/experiment/exploracion/adjudicacion/notas_adjudicacion_u6.md` §2)
  definen el test: el contenido de párrafos sin numerar (encabezados, cierres,
  intersticiales) debe aparecer en el grafo v2 anclado a su punto contenedor.
- **Cláusula repetida → test anti-fusión E4.** Los 5 portadores de la cláusula
  del 125 % (U6-008) deben existir como nodos separados con provenance
  propia; una fusión de cualquiera de ellos es un FAIL del pipeline.
- **Amputaciones → test del verificador E3.** BKL-0005 (calificadores del 7.1
  de RegInf), BKL-0003 (salvedad del 1.1.2.5 de Protección) y BKL-0004
  (enumeración del 6.5 de Clasificación) definen omisiones que E3 debe
  rechazar si el extractor las repite.

Además, **cada corrección histórica C1–C7 es un test de respuesta conocida**:
el pipeline v2 parte de los PDFs y debe capturar nativamente lo que v3
necesitó parchear a mano. Los re-tests sellados
(`data/backlog/retests/C{1..7}_retest_*.md`) ya contienen los chequeos
chunk-contra-PDF, estructurales y de alcanzabilidad que definen el PASS de
cada caso; correrlos contra el grafo v2-reextraído no requiere diseñar nada
nuevo. El delta —cuántos de estos casos el v2 captura de fábrica contra
cuántos v3 necesitó a mano— es el número de mejora del pipeline.

---

## 6. Evaluación y secuencia

La corrida del pipeline queda **gateada por el sellado previo de EV2** (issues
#3 y #4): el set de evaluación se diseña y se sella ANTES de que exista el
grafo nuevo, para que ninguna decisión de extracción pueda contaminarse con
conocimiento de las preguntas. La lección viene del material quemado del
proyecto (EV1/CQ/CQN/CQN2): un eval set que se conoce durante el desarrollo
deja de servir como medición.

La medición central (issue #10) compara tres sistemas sobre el mismo set
sellado: el grafo v2-reextraído, el grafo v3 vigente
(`data/experiment/grafo_v2/reensamblado_v3/kg.json`, 4.469 nodos / 8.073
aristas post-C7, sha256 `26fac8b4…`; `docs/tablero.md` §1), y el baseline
congelado.

El reporte de la corrida incluye la **contabilidad completa de costos por
capa** (extracción, verificación, resolución, re-extracciones del ratchet,
cola humana), con tope declarado ex ante (principio 2.f). La literatura del
área no reporta costos; este proyecto sí, y ese reporte es parte del aporte.

---

## 7. Preguntas abiertas para laudo externo

- **(a)** Tope de reintentos del mini-ratchet de E3: ¿1 o 2 re-extracciones
  antes de derivar a cola humana? Y el presupuesto de esa cola: ¿cuántas
  unidades flaggeadas son aceptables antes de frenar la corrida?
- **(b)** Presupuesto de la corrida de calibración previa al corpus completo
  (la que fija modelos, precios y verifica la acumulación batch+caching de D4).
- **(c)** Si EV2 absorbe las 25 preguntas de U6 ya adjudicadas
  (`data/experiment/exploracion/adjudicacion/notas_adjudicacion_u6.md`, U6-001
  a U6-025) como gold semilla, o se genera íntegramente fresco.
- **(d)** Alcance del tratamiento dedicado de tablas y fórmulas en E0:
  ¿extracción estructurada propia o flag de contenido no-confiable?

---

## Referencias

Por identificador, según la biblioteca del proyecto
(`docs/literatura/resumenes/`):

- **Paper 00** (RAGulating Compliance): se toma la arquitectura multiagente;
  NO se adopta su filosofía schema-light ni sus números, cuya fragilidad está
  documentada en el análisis comparativo del proyecto.
- **Paper 06** (LINK-KG): pipeline multietapa con esquema y caché de tipos
  para consistencia cross-chunk (adoptado en E4).
- **FinReflectKG**: loop de feedback iterativo con validación estructural —
  precedente del mini-ratchet de E3, mejorado aquí con separación de
  contextos.
- **arXiv 2505.24478** (Markovic et al.): sensibilidad de la construcción de
  KGs a los parámetros de construcción; respalda el protocolo uniforme de
  extracción (mismo prompt, mismo esquema, mismo presupuesto para todo chunk).
- **Anthropic Knowledge Graph Construction Cookbook**: patrón de
  extracción/resolución por niveles de modelo (adoptado en D3).
- **Tamašauskaitė & Groth**: marco de seis pasos del desarrollo de KGs — el
  encuadre general del ciclo identificar/extraer/construir/evaluar que este
  pipeline instancia.
