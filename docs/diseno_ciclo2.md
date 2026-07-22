# Diseño del ciclo 2 — D7 (v6.2-D) + S1 v0.4

**Fecha:** 2026-07-18. **Estado:** SOLO DISEÑO — nada de lo aquí descrito está
implementado ni corrido. **Fuentes:** `docs/lectura_gate_cqn.md` (los tres hallazgos),
`docs/casos_gate_cqn.md` (la vara del gate, `1d4e7a8`),
`docs/especificacion_capa_deterministica.md`, `docs/diseno_v7_s1.md`, el código congelado
(`capa_deterministica.py`, `s1_fuentes.py`) y los 30 JSONs de la corrida del head-to-head.

## 1. Marco

**El gate CQN queda QUEMADO** — sus 10 casos pasan a ser material de DEV del ciclo 2 (los
tres specs de abajo se derivan de sus mecanismos y pueden iterarse contra ellos). **La
evaluación final del ciclo será contra un set fresco (CQN2)** con vara sellada por
inexistencia, con el circuito completo de custodia del gate CQN (generación ciega,
adjudicación previa, guarda paso-0).

**Head-to-head a TRES columnas, del MISMO run del verificador** (una sola corrida v5.7
N=3; las tres capas se computan sobre esos mismos outputs — el costo grande se paga una
vez):

1. **v6.1-D** — baseline CONGELADA, no se toca (el instrumento validado de la lectura).
2. **v6.2-D** — v6.1-D + D7 (puntero estructural).
3. **v7'** — v6.2-D + S1 v0.4 (guarda de dominio + portador robusto).

## 2. Spec D7 — puntero estructural (para v6.2-D)

**Hecho que lo motiva** (lectura §3.iii): en CQN-007 el v5.7 votó **navegación 3-0** y D2
lo corrigió a **alcanzabilidad_kg ×3** (`atribuciones_corregidas: 3, discrepancias: 3` —
extracción, CQN-007) por D1-léxico negativo, **sin ver que el puntero del nodo estuvo en
pantalla vía `ver_vecinos`** (paso 8 de la traza: label, relación `limita`, provenance
8.1). El compuesto emitió confiado donde la vara adjudica navegación.

**(a) Qué extrae D7 de la traza.** Los ids (y labels) de vecinos aparecidos en los
outputs de **`ver_vecinos`** de la traza post-hoc — el conjunto `punteros_estructurales =
{vecino_id}` con su evidencia (paso, relación, id del nodo consultado). **Decisión: los
listados de `buscar_nodos` NO se incluyen.** Justificación: un nodo que apareció en un
top-10 de `buscar_nodos` en runtime apareció por las consultas reales del agente — que
son EXACTAMENTE el insumo de D1 (misma función, mismo índice, mismas consultas, más las
expansiones de la pregunta). Si estuvo en un listado léxico, D1 ya lo declara alcanzable;
sumarlo a D7 duplicaría el canal léxico sin agregar información. D7 existe para el canal
que D1 NO ve: el estructural.

**(b) Interacción con D2 — la regla determinística exacta.** D2 hoy decide la frontera
navegación/alcanzabilidad SOLO por D1. Con D7, la decisión pasa a esta tabla de verdad
(por atribución en la frontera, portador único ya extraído):

| D1 (léxico) | D7 (puntero estructural del portador en la traza) | Decisión de código |
|---|---|---|
| (portador no extraíble) | — | R3 como hoy; D7 NO aplica |
| alcanzable | (cualquiera) | navegación (como hoy) |
| NO alcanzable | puntero PRESENTE | **navegación** (D7 nuevo: el grafo lo señalizó — el agente lo tuvo en pantalla) |
| NO alcanzable | puntero AUSENTE | alcanzabilidad_kg (como hoy) |

La fila 0 existe para que la válvula no se dispare por un no-problema: el caso sin
portador ya está resuelto por la maquinaria existente (R3) y queda fuera del alcance de
D7.

Si el LLM votó navegación y cae en la fila 2, **D2 NO corrige** — el voto del LLM
sobrevive, con anotación `capa_d = {modulo: "D7", puntero_estructural: true,
evidencia: {paso, relacion, nodo_consultado}}`.

**(c) Si el LLM votó alcanzabilidad y D7 detecta puntero.** **Decisión: se CORRIGE a
navegación** (no triage). Justificación: es el simétrico exacto de lo que D2 ya hace en
la otra dirección (LLM dice alcanzabilidad, D1 positivo → corrige a navegación, con
`discrepancia: true`); el puntero-en-pantalla es un hecho computable del MISMO tipo que
el rank de D1 — y más fuerte: no dice "podría haberse encontrado" sino "APARECIÓ en esta
traza". La taxonomía define alcanzabilidad_kg como "existe con contenido correcto pero
inalcanzable"; un nodo cuyo puntero se mostró no es inalcanzable en los hechos. La
discrepancia queda anotada como siempre (emisión LLM preservada en `capa_d`).

**(d) Casos borde.**
- **Puntero en tramo truncado del output runtime:** la detección corre sobre los outputs
  COMPLETOS re-ejecutados (`outputs_completos_de_trace`, regla de la casa desde D5, con
  fidelidad por igualdad de largos) — nunca sobre `output_truncado`. Un puntero que vivía
  en el tramo truncado del registro pero que el agente SÍ vio, cuenta.
- **`ver_vecinos` con error (nodo inexistente) o 0 vecinos:** no aporta punteros; sin
  caso especial.
- **Presupuesto:** D7 NO razona sobre cuántas tools le quedaban al agente al momento del
  puntero (limitación documentada: un puntero en el paso 15/15 cuenta igual — la lectura
  humana del triage puede matizarlo, el código no).
- **Múltiples apariciones:** se registra la primera (paso mínimo); las demás,
  informativas.

**VÁLVULA PRE-REGISTRADA:** la regla cabe en la tabla de verdad de 3 filas de (b) — si al
implementarla apareciera ambigüedad que no cabe en esa tabla (p. ej. interacción con
`sin_portador_extraible` que exija heurísticas nuevas), **D7 se DESCARTA y el ciclo
degrada a solo-S1**: lo declaro ahora para no estirar la regla a fuerza de parches.

## 3. Spec guarda de dominio — S1 v0.4

**Hecho que la motiva** (lectura §3.i): la degradación silenciosa de CQN-013 — fetch
`completo` con la fuente en OTRO documento (pregunta de Protección, portador con
provenance de Exterior), 9/9 salidas idénticas re-atribuyendo al grafo un error del
agente, triage apagado.

**Cómo se determina el territorio de la pregunta. Decisión: `tos_fuente` del eval set
(el sellado).** Justificación: (a) es metadato de la PREGUNTA, no del GT — no revela ni
la respuesta esperada ni la cita (la prohibición de GT-como-input de S1 queda intacta);
(b) es determinístico y existe en cualquier corrida del pipeline (el eval set siempre
está); (c) la alternativa — inferir el territorio de las citas del GT — sí tocaría
material prohibido, y la de inferirlo del texto de la pregunta metería un clasificador
donde va un lookup. Para preguntas multi-documento, `tos_fuente` es un CONJUNTO y la
guarda es por pertenencia — el cross-doc legítimo de una multi_norma con dos TOs
declarados no dispara.

**La regla:** para cada atribución gatillada con fetch completo, si
`source_doc(provenance usada del portador) ∉ tos_fuente(pregunta)` →
- **PROHIBIDO exonerar** y **PROHIBIDO re-atribuir** con ese material;
- única salida: **triage con motivo nuevo `fuente_cross_doc`** (anotación con el par
  documento-portador / territorio, verbatim);
- la llamada LLM NO se hace (la guarda es del fetch: cero tokens, cero oportunidad de
  flip).

**Aplicación retrospectiva en el papel — CQN-013:** `tos_fuente = ["proteccion"]`
(eval set sellado); el portador del claim del art. 41 tiene provenance con
`source_doc = TO_exterior_cambios` (vara CQN-013 §3; extracción: fetch `completo` ×3).
Con la guarda: las 3 atribuciones caen en `fuente_cross_doc` ANTES de llamar al modelo →
**el flip a {faithfulness, contenido_kg} no ocurre** (no hay juicio), voto_s1 = voto de
v6.1-D → **el acierto de v6.1-D (aplicacion_erronea 2-1) sobrevive**, con triage
informativo en vez de silencio.

## 4. Spec portador robusto — S1 v0.4

**Hecho que lo motiva** (lectura §3.ii): la provenance desplazada neutraliza el fetch —
`sin_portador_extraible` en CQN-014 (S1 mudo sobre la familia 12.3) y `no_determinable`
×3 en CQN-006 (pasajes por numeral que no fundan la cláusula juzgada).

**Mecanismo (fallback por CONTENIDO, determinístico):**
1. **Cuándo corre:** (i) el fetch por numeral falló (`sin_portador_extraible` con
   portador citado pero ids anidados irresolubles, `provenance_no_parseable`,
   `localizacion_fallida`); (ii) el fetch por numeral localizó pero se quiere el pasaje
   que FUNDA el contenido: el fallback agrega SIEMPRE un pasaje extra
   `portador_por_contenido` cuando localiza único y distinto del pasaje por numeral (sin
   lógica de reintento: un solo fetch, más material, misma llamada).
2. **Búsqueda:** los K literales más largos del contenido del nodo (label + values de
   properties, normalización de la casa: lowercase, sin acentos, espacios colapsados;
   des-hifenado del corpus como en la custodia CQN) se buscan por substring sobre el
   texto por página de los TOs del TERRITORIO de la pregunta (la guarda del §3 aplica
   también acá: no se busca fuera de `tos_fuente`). El pasaje = ventana alrededor del
   mejor match, con página.
3. **Guardas anti-falso-portador:** (i) longitud mínima del match (umbral en chars
   normalizados contiguos — a calibrar en dev, del orden de una cláusula, no de una
   frase suelta); (ii) UNICIDAD: si el literal matchea en más de un documento del
   territorio o en más de k ubicaciones, no funda → `contenido_no_unico`, triage;
   (iii) el pasaje se rotula `portador_por_contenido` en el prompt (transparencia) y
   **nunca habilita exoneración por sí solo** — decide causa o deriva, no exonera.

**Aplicación retrospectiva en el papel:**
- **CQN-014** (`sin_portador_extraible` — extracción): el nodo de la variante transitoria
  porta texto levantado del 12.3 ("hasta el 30/06/26", "17%", "reclasificadas desde el
  01/01/2026" — vara CQN-014 §3). La búsqueda por contenido sobre Capitales localiza el
  12.3 real (la página y su encabezado de alcance ya verificados en el ciclo B3) →
  **S1 deja de estar mudo**: el juicio recibe el 12.3 CON su declaración de alcance —
  exactamente el material que confirma contenido_kg de la familia 12.3.
- **CQN-006** (`no_determinable` ×3 — extracción): el contenido del nodo del claim es
  verbatim del 2.3.5.1.i de Protección (vara CQN-006 §3, página 15). El pasaje por
  contenido trae esa cláusula → la rama de exoneración pasa a tener el texto que
  RESPONDE lo juzgado → **decidible** (esperado: `presente_en_grafo=si` → sin_defecto
  sostenida con evidencia, en vez de tres abstenciones).

### §4bis — Requisito de fundamento del pasaje (enmienda post-unidad 2)

**Hecho que la motiva** (reporte de la unidad 2 §6d y los verbatim de la verificación
dirigida): en CQN-011, el fetch por numeral pasó la guarda de dominio LEGÍTIMAMENTE
(portador del RI, territorio RI) pero el pasaje provino de la **provenance desplazada**
del nodo (el título genérico del 1.1); el juicio leyó un pasaje que NO funda el contenido
del nodo, concluyó "el grafo no define el código 3" y re-atribuyó
`aplicacion_erronea → contenido_kg` (rep3_atrib2), convirtiendo un voto dividido — un
triage honesto — en mayoría 2-1: **una regresión real contra el material quemado**. Es el
mecanismo de CQN-013 en versión INTRA-dominio: la guarda de dominio no lo ve porque el
documento es correcto.

**La regla.** Para habilitar re-atribución o exoneración, el pasaje fetcheado por numeral
debe **FUNDAR el contenido del nodo portador**, verificado con la MISMA maquinaria del
portador por contenido (ancla + extensión + umbral `UMBRAL_CONTENIDO`, ya calibrada en la
unidad 2): el contenido del nodo debe localizar DENTRO del pasaje (o de su página) con
span ≥ umbral. Si no funda → estado **`fuente_no_funda`**, triage con ese motivo, **sin
llamada LLM** (la misma filosofía de la guarda de dominio: a nivel fetch, cero tokens,
cero oportunidad de flip). El pasaje extra `portador_por_contenido` de un fetch completo
satisface el requisito POR CONSTRUCCIÓN (localizó por contenido).

**Criterio de éxito nuevo (e), pre-registrado:** CQN-011 vuelve a **DIVIDIDO/triage** (la
corrección de rep3_atrib2 no ocurre: su pasaje no funda); y **sin regresiones nuevas**:
CQN-006 sigue decidible (sus pasajes fundan — se verifica, no se asume), CQN-009/014
conservan sus confirmaciones, CQN-012/013 conservan sus bloqueos cross-doc, CQN-007
conserva el flip de D7.

**Riesgo documentado:** endurecer el fundamento puede convertir decisiones legítimas en
triages — precisión sobre rescate, coherente con la filosofía del umbral del §4. El
árbitro es CQN2.

**Nota de medición (post-unidad 2b):** la premisa fáctica del "hecho que la motiva" quedó
corregida por la medición de la unidad 2b — el pasaje de rep3_atrib2 SÍ funda (span 245;
la description de ese nodo es el texto del listado del 1.1, provenance no desplazada); el
mecanismo real de la regresión de u2 era MIXTO: 4 atribuciones con pasajes que no fundan
(bloqueadas por esta regla) más una fundante con juicio en la frontera (varianza,
contenida por N y triage — residuo pre-registrado en el reporte u2b §5). La regla se
sostiene por las atribuciones no-fundantes reales (5 en el material quemado: 4 en
CQN-011, 1 en CQN-012). Ver `posthoc_run/dev_set/dev_ciclo2_u2b_fundamento.md`.

## 5. Criterios de éxito sobre el material quemado (pre-registrados; se evalúan en DEV — el veredicto real es el gate CQN2)

- **(a) CQN-007:** v6.2-D emite **navegación** — el voto original del LLM (3-0) sobrevive
  a la capa vía D7.
- **(b) CQN-013:** v7' **no degrada** — triage `fuente_cross_doc`, o voto de v6.1-D
  intacto. Nunca el flip.
- **(c) CQN-014 y CQN-006:** de fetch-fallido/no-determinable a **decisión o triage
  informativo** (portador por contenido operando).
- **(d) CERO regresiones:** los aciertos de v6.1-D (CQN-006, CQN-009) y los triages
  (CQN-001, CQN-011) no cambian de categoría en v6.2-D ni en v7'.

## 6. Riesgos y no-objetivos

- **v6.1-D queda CONGELADA como baseline** — v6.2-D es una capa NUEVA al lado, no una
  edición; la comparación a tres columnas exige el baseline intacto.
- **El juez y el harness no se tocan** (congelados de siempre).
- **El FN-del-juez (nota estructural de CQN-010, lectura §4) queda explícitamente FUERA
  del alcance del ciclo 2:** es un límite del pipeline juez-primero, no de los
  instrumentos de este ciclo; mezclarlo acá diluiría ambas cosas.
- **Riesgo de D7:** que el puntero-en-pantalla resulte demasiado laxo (todo vecino
  cuenta, sin noción de pertinencia) — mitigación: la evidencia por anotación permite
  leer en dev cuántos punteros espurios habilita; si el ruido domina, rige la válvula
  del §2.
- **Riesgo del portador por contenido:** falso portador por texto repetido en el corpus
  — mitigación: las guardas de longitud y unicidad, calibradas en dev (nunca contra
  CQN2).
- **Riesgo de proceso:** iterar de más sobre material quemado — mitigación: los
  criterios §5 son de dev; la única cifra que contará es CQN2, con su vara sellada antes
  de que ninguna versión del ciclo 2 la vea.
