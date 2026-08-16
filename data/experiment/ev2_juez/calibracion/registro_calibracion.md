# Registro de calibración — juez de fidelidad EV2 (pre-registro §5)

Calibración del juez LLM del eje de fidelidad de EV2 sobre las 25 preguntas de
U6 adjudicadas humanamente, según `docs/preregistro_evaluacion_fidelidad_ev2.md`
(commit be8a84f). Material de EV2: no abierto en ninguna etapa.

## 1. Insumos

- Preguntas: `data/experiment/exploracion/generacion/preguntas_u6.json` (25).
- Respuestas: sesión de la app local
  `app/sessions/local/09beef6a-a147-4417-8a53-cea3da678930.jsonl` (25 turnos,
  apareados por texto exacto de la pregunta) — la fuente sobre la que se hizo
  la adjudicación humana. Las trazas de `posthoc_run/traces/u6_exploracion/`
  (corrida apareada B2) NO son esa fuente: 21/25 respuestas difieren; la
  pasada corrida sobre ellas queda conservada y rotulada NO VÁLIDA para
  calibración (`out/NOTA_fuente_respuestas_pasada1.md`).
- Adjudicación humana: `data/experiment/exploracion/adjudicacion/u6_adjudicacion_humana.jsonl`
  (7 correcta / 15 parcial / 3 incorrecta; commit b337152). Solo se abre del
  lado del análisis (`analisis_acuerdo.py`), nunca en el input del juez.
- Criterios: `data/experiment/exploracion/u6_fidelidad/criterios_u6.json`
  (commit 2ac2fab, sha256 b8d6578902dc…, 25 preguntas / 92 criterios con cita
  textual; 92/92 citas verificadas: 90 en texto lineal del PDF, 2 tabulares de
  U6-022 por columna de tabla — Laudo D del registro de criterios).

## 2. Instrumento

- Modelo `claude-sonnet-4-6`, temperature 0, N=3 por (respuesta, criterio),
  veredicto modal (mayoría estricta; sin mayoría → `sin_consenso`), una db de
  caché y un label por repetición, 0 cross-hits verificados por keys disjuntas
  y por access_log.
- Mapping por pregunta en código (`mapping.py`, 20 tests de respuesta
  conocida): todos cumplido → correcto; cero cumplido → incorrecto; mezcla →
  parcial; cualquier dudoso/sin_consenso → requiere_adjudicacion.
- Orden `random.Random("juez-calibracion-v1").shuffle` sobre ids ordenados.
- Ceguera: el driver no tiene parámetro ni ruta para la adjudicación; el
  selftest verifica estructuralmente que el request contiene solo prompt +
  (pregunta, respuesta, criterios).

## 3. Resultado (pasada válida, prompt v1, sha256 fd446f8e61f46033d7de9b862121c698b2c52dcc2696b7f10993f44e509f5455)

Fuente: `out_app/` (`resumen_corrida.json`, `veredictos_agregados.json`,
`acuerdo_juez_humana.json`, `reporte_desacuerdos.md`,
`clasificacion_desacuerdos_lectura.md`). Costo USD 1,0101 (75 llamadas).

- **Por pregunta: 14 acuerdos + 6 desacuerdos + 5 requiere_adjudicacion**
  → **14/20 sobre las decididas**; 5/25 derivadas a adjudicación humana.
- Matriz humano→juez: correcto→correcto 1, correcto→parcial 5,
  correcto→req.adj. 1; parcial→parcial 10, parcial→incorrecto 1,
  parcial→req.adj. 4; incorrecto→incorrecto 3.
- Por criterio (proxy): humana incorrecta → 13/13 no_cumplido; humana correcta
  → 11/21 cumplido.
- No-determinismo: 87/92 pares unánimes; 0 sin_consenso; los 5 no unánimes
  involucran `dudoso`.
- Fragmentos: 276 = 167 verbatim + 94 null + 14 concatenaciones/puntuación con
  contenido presente + 1 fuga de gold (U6-001 c3, rep 2).

El % de acuerdo se REPORTA como dato; no opera como gate (pre-registro §5).

## 4. Lectura definicional de los desacuerdos (declarada, no corregida)

Los 6 desacuerdos son de etiqueta, ninguno de evidencia (fragmentos verbatim o
ausencias reales, 3/3 consistentes). En 5/6 (U6-021, U6-002, U6-017, U6-023 y,
en menor medida, U6-013) el par decisivo es un criterio cuyo contenido la
pregunta no pedía o es cláusula de cierre; en U6-009 es granularidad (un
criterio agrupa tres documentos y la respuesta trae uno).

La brecha es de **vara**, no del juez:
- el **juez** mide la respuesta contra el **gold completo** (todos los criterios
  con cita), y esa es exactamente su instrucción;
- la **humana** adjudicó U6 sin gold previo, informada contra el ancla, con el
  Laudo №1 (no penalizar omisión de lo no preguntado) y el Laudo №3 (matiz de
  cierre no altera el contenido) — un estándar de "núcleo preguntado" aplicado
  sobre un gold redactado **post-hoc**.

Decisión de la autora: la brecha se DECLARA y no se corrige — sin edición de
criterios sellados, sin calibradores de "perdón", sin cambio del mapping.

**No aplicabilidad a EV2:** en EV2 la vara es el gold sellado y pre-registrado
(criterios con cita, escritos a ciegas antes de las respuestas), es decir, el
juez y la vara coinciden por construcción; la lectura "núcleo preguntado" no
existe allí. El residuo observado en U6 no se traslada.

## 5. Limitación registrada: consistencia interna

U6-010: la humana señaló una interpolación contradictoria dentro de la
respuesta ("intereses devengados antes del vencimiento" junto a "a partir del
vencimiento"). Ningún criterio la cubre y el juez evalúa criterio por criterio:
**el instrumento no mide consistencia interna de la respuesta**. Queda como
limitación conocida del método, no como defecto a parchear en esta unidad.

## 6. Iteración única v1.1 (autorizada)

Un calibrador de ejemplo resuelto contra la fuga de gold observada en U6-001 c3
(contenido ausente → fragmento null + no_cumplido; el fragmento solo puede ser
texto de la respuesta), sin ningún otro cambio. Prompt `prompt_juez_v1_1.md`,
sha256 6c3f1cb38542e4dac7c7c2502e9cefff4bbab3bf320f615ef1b3ac54584b95fd.
Criterio de aceptación: fuga eliminada en U6-001 c3 y cero cambios de veredicto
modal en los 91 pares restantes. Resultado: ver §7.

## 7. Resultado de v1.1 — aceptación NO cumplida (a laudo)

Re-corrida completa sobre fuente app (`out_app_v11/`, dbs
`cache_app_v11/juez_calibracion_app_v11_r{1,2,3}.db`): 75/75 llamadas, USD
1,1461 (183.948 in / 39.616 out; el calibrador agrega ~600 tokens de entrada
por llamada), 0 cross-hits.

- **Fuga eliminada**: U6-001 c3 → `no_cumplido` 3/3 con fragmento null 3/3.
  Auditoría global de fragmentos v1.1 (276): 155 verbatim + 109 null + 12
  marcados mecánicamente (U6-011 c1, U6-013 c3, U6-015 c4 = concatenaciones/
  puntuación; U6-019 c1 marcado "fuga_gold" por una coma pero el texto está en
  la respuesta — mismo falso positivo que en v1); **0 fugas reales de gold**.
- **Pares con cambio de veredicto modal respecto de v1: 3 de 91** (criterio de
  aceptación: 0) → la iteración NO cumple la aceptación y queda a laudo:
  - U6-004 c1: no_cumplido ×3 → **cumplido ×3** (unánime en ambas versiones;
    v1.1 reconoce como equivalente "umbral + si declara que no posee, no se
    requiere conformidad" a la estructura regla/excepción). Coincide con la
    humana (correcta), pero es un cambio de comportamiento fuera del alcance
    del calibrador.
  - U6-011 c2: dudoso/nc/dudoso → **no_cumplido ×3** (omisión de "mientras
    persista" y "saldos al último día de cada mes" pasa de duda a
    incumplimiento; probable derrame de la frase del calibrador "dudoso
    tampoco corresponde acá").
  - U6-019 c2: c/d/d → **d/c/c** — misma distribución de valores en ambas
    versiones; el cambio de modal está en el borde del no-determinismo, no es
    atribuible al prompt con confianza.
  Además, 2 pares cambian distribución sin cambiar modal (U6-004 c2 y U6-010
  c3, ambos hacia `dudoso` unánime) y U6-001 c3 (el objetivo).
- Efecto por pregunta: U6-011 y U6-019 pasan de requiere_adjudicacion a
  parcial (= humana); acuerdo 16 · desacuerdo 6 · req.adj. 3 (16/22).
  No-determinismo: 91/92 unánimes (v1: 87/92); 0 sin_consenso; modales
  {no_cumplido 55, cumplido 33, dudoso 4}.

Lectura: el ejemplo resuelto corrigió exactamente lo que apuntaba (la fuga);
la cola declarativa del calibrador ("dudoso tampoco corresponde acá") derramó
sobre fronteras dudosas ajenas al caso (U6-011 c2, y el corrimiento hacia
`dudoso` unánime en U6-004 c2 / U6-010 c3). Es consistente con el hallazgo
histórico del proyecto sobre jueces LLM: los ejemplos resueltos se honran con
precisión; las reglas declarativas se generalizan más allá de su caso.

## 8. Laudo final y cierre de la calibración

**Prompt congelado: v1** — `prompt_juez_v1.md`, sha256
`fd446f8e61f46033d7de9b862121c698b2c52dcc2696b7f10993f44e509f5455`, según §5
del pre-registro. **v1.1 NO se adopta**: la aceptación pre-declarada no se
cumplió, y adoptarlo por la dirección favorable de sus cambios sería
seleccionar el instrumento contra el conjunto de calibración (candado de
ajuste, §5). v1.1 (`prompt_juez_v1_1.md`), sus dbs (`cache_app_v11/`) y sus
salidas (`out_app_v11/`) se conservan rotulados como **iteración descartada**.
(El archivo `prompt_juez_v1_1.md` lleva el rótulo de descarte en su encabezado,
por lo que su sha256 actual difiere del `6c3f1cb3…` con que corrió; ese sha
original queda registrado en el campo `meta.prompt_sha256` de cada veredicto
de `out_app_v11/veredictos_r{1,2,3}.jsonl`.)

**Resultado final del instrumento (v1, sobre las 25 de U6):** 14/20 acuerdos
sobre las decididas + 5 preguntas derivadas a adjudicación humana; 3/3
incorrectas humanas detectadas; residuo de 6 desacuerdos, todos de etiqueta y
5/6 de vara (§4). Criterio de frenado del §5 alcanzado: residuo pequeño y de
etiqueta, no de evidencia.

**Limitaciones documentadas del instrumento v1:**
1. *Fuga de gold al fragmento* (U6-001 c3: 1/276 fragmentos en la pasada
   válida; 3/276 sobre la respuesta B2 del mismo par). Modo de falla
   **benigno**: en todos los casos observados el veredicto asociado fue
   `dudoso`, que el mapping §2 convierte en `requiere_adjudicacion` — la
   fuga deriva a la humana, jamás produce un veredicto falso silencioso. La
   auditoría de fragmentos (`analisis_acuerdo.py`: verbatim / null /
   no_verbatim / fuga_gold) se corre sobre toda salida del juez y detecta el
   patrón de forma mecánica.
2. *Sensibilidad de equivalencias* (U6-004 c1): ante una formulación
   normativamente equivalente pero con estructura distinta (regla/excepción
   vs umbral+condición), v1 exige la estructura y marca `no_cumplido`; v1.1
   la aceptó. Característica conocida: v1 es estricto con la forma en
   fronteras de equivalencia; el sentido del error es hacia el rigor.
3. *Consistencia interna no medida* (§5).
4. *Brecha de vara en U6* (§4), no aplicable a EV2.

**La calibración queda CERRADA.** La evaluación de las 120 respuestas de EV2
es una unidad nueva con mandato y autorización propios; usa `prompt_juez_v1.md`
sin cambios y `mapping.py` tal cual.
