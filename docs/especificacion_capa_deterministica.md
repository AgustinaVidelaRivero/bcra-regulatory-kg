# Especificación del instrumento compuesto v6.1-D — verificador v5.7 + capa determinística

**Fecha:** 2026-07-15 (v6.0-D) · actualizada 2026-07-16 (v6.1-D). **Versión vigente de la capa:** `v6.1-D(2026-07)` (constante `VERSION_CAPA` en
`capa_deterministica.py`). **Evidencia:** `docs/evidencia_capa_d/` (reportes de construcción
D1-D5b y corrida consolidada) y `docs/evidencia_vara_v3/` (verificaciones programáticas).

## 1. Qué es

El instrumento compuesto v6.1-D es la suma de dos piezas:

1. **El verificador v5.7, congelado.** Su historia, su gate final y la doble lectura del gate
   están en `docs/especificacion_verificador_v57.md` y `docs/lectura_gate2_AB.md`. No se
   itera más: el gate #2 fue, por pre-registro, su última calibración.
2. **La capa determinística post-hoc** (`data/experiment/evaluacion/capa_deterministica.py` +
   `data/experiment/evaluacion/test_alcanzabilidad.py`): módulos de código puro que corren
   sobre la salida JSON del verificador y deciden, corrigen, verifican o derivan a triage
   todo lo que es computable sin juicio semántico.

**Los módulos de la capa NO tienen score de gate NI lo tendrán.** Su corrección se establece
**por construcción**: cada módulo lleva su semántica pre-registrada verbatim en el docstring
(fuente normativa) y una batería de **50 tests** unitarios y de pipeline (sin API, sin disco,
con grafo sintético) que fijan cada comportamiento, incluidos los casos borde. La validación
**de sistema** del compuesto será **prospectiva**, sobre casos frescos (§7) — nunca sobre los
5 casos del gate, que motivaron los módulos y quedaron quemados como medida.

**El principio rector:** el LLM queda confinado al juicio irreducible (leer semántica,
ponderar pertinencia, decidir alcance); **el código decide todo lo computable** (simular el
índice, verificar un substring, contar una mayoría, aplicar una política de derivación). Una
decisión computable tomada por código es reproducible, auditable y no tiene varianza de
muestreo; la misma decisión tomada por el LLM es una moneda cargada que el gate #2 midió.

## 2. Módulo por módulo

La **fuente normativa de cada módulo es su docstring** (semántica pre-registrada verbatim en
`capa_deterministica.py` y `test_alcanzabilidad.py`); esta sección no la duplica — dice qué
computa cada módulo, POR QUÉ ese mecanismo, y QUÉ NO HACE.

### D1 — prueba ex ante de alcanzabilidad léxica (`test_alcanzabilidad.py`)

- **Qué computa:** dado un nodo portador y una pregunta, simula el índice léxico real
  (`harness.GraphIndex`, réplica exacta del scoring de `buscar_nodos`) sobre un conjunto
  determinístico de consultas y responde si el portador es alcanzable (top-10 de al menos
  una). Expone además, por consulta, rank completo, score y tokens matcheados, y el
  vocabulario ex ante usado. Incluye los helpers de re-ejecución
  (`outputs_completos_de_trace`, `tokens_expuestos_de_trace`).
- **Por qué por mecanismo:** la alcanzabilidad ES una simulación del índice — no hay nada
  semántico en si una búsqueda devuelve un nodo en el top-10. La medición que fundó el módulo
  está en `docs/evidencia_vara_v3/verificaciones_vara_v3.md` §2: el portador de CQ-031 quedó
  0/10 en top-10 con las consultas reales del agente, y el mecanismo (token del id truncado
  en `garanti`, que la búsqueda "garantias" no matchea) es puramente léxico.
- **Qué NO hace — definición operacional de "razonabilidad":** el conjunto de consultas es
  consultas del agente + pregunta entera + bigramas/trigramas de la pregunta. Los tokens
  expuestos NO generan consultas nuevas: generar consultas desde lo expuesto exigiría
  seleccionar cuáles por match contra el objetivo — eso es hindsight, no ex ante. **Sesgo
  residual conservador, documentado:** algún caso de frontera puede caer del lado grafo
  (`alcanzabilidad_kg`) cuando un agente más hábil habría llegado; el costo es esfuerzo de
  refinamiento de más, nunca un defecto escapado.

### D2 — decisor de la frontera navegación/alcanzabilidad (`aplicar_d2`)

- **Qué computa:** para cada atribución en la frontera `(context_recall, navegación |
  alcanzabilidad_kg)`, extrae el portador de la evidencia (substring exacto de ids del kg),
  corre D1 y fija la causa por el resultado (`alcanzable=False → alcanzabilidad_kg`;
  `True → navegación`). Anota `capa_d` con la emisión del LLM, la decisión del código, la
  discrepancia y la evidencia D1 reducida; recomputa el voto (regla del protocolo) como
  `voto_capa_d`, preservando el voto original.
- **Por qué por mecanismo:** el gate #2 mostró la frontera como el error de etiqueta más
  costoso del v5.7 (CQ-031: navegación 3-0 donde la simulación da inalcanzable —
  `docs/evidencia_vara_v3/verificaciones_vara_v3.md` §2, `docs/lectura_gate2_AB.md` §5). La
  frontera es computable porque su definición taxonómica (v2.1) ES una prueba de índice.
- **Qué NO hace — corrección CONDICIONAL:** D2 decide bien la rama **DADO el portador y el
  síntoma que el LLM eligió**; no valida que la atribución sea apta de raíz. Caso
  ilustrativo: la rep 1 de CQ-025 fue corregida correctamente de rama (navegación →
  alcanzabilidad, el portador citado es genuinamente inalcanzable desde esa pregunta) sobre
  una atribución equivocada de raíz — el GT del caso es `contenido_kg`
  (`docs/evidencia_capa_d/reporte_d3_d4.md`). Sin portador extraíble (0 o >1 ids), D2 no
  corrige: anota triage.

### D3 — validador de quotes de `aplicacion_erronea` (`aplicar_d3`)

- **Qué computa:** para cada atribución `aplicacion_erronea`, verifica que el quote de nodo
  de la evidencia exista verbatim-normalizado (lowercase, sin acentos, espacios colapsados)
  en el contenido del nodo citado (label + properties). Verificado → anotación; no
  verificado o sin portador → triage. **Nunca cambia causas.**
- **Por qué por mecanismo:** un quote es verificable por substring — certificar su
  autenticidad no requiere juicio. `aplicacion_erronea` es la categoría más nueva y con sesgo
  medido (§2(b) del protocolo del gate), así que su evidencia merece certificación automática.
- **Qué NO hace (límite estructural, medido):** verifica la condición computable NECESARIA
  (el quote existe en el nodo), no la SUFICIENTE (que el quote constituya una declaración de
  alcance — test v2.6, semántico). **Hallazgo del dry-run:** los 5 quotes de
  `aplicacion_erronea` del gate verificaron (`docs/evidencia_capa_d/reporte_d3_d4.md`) — el
  modo de falla del verificador en esa frontera es semántico, no de fabricación de evidencia.
  Por eso **la contención de `aplicacion_erronea` es R2 (triage), no D3**.

### D4 — política de triage a nivel caso (`aplicar_d4`, reglas R1-R6)

- **Qué computa:** el bloque `triage_capa_d = {triage, motivos, flags}` sobre el JSON ya
  pasado por D2/D3/D5/D6:
  - **R1 `exoneracion_total`** — mayoría con clave ganadora vacía (sin primarias).
  - **R2 `aplicacion_erronea_bajo_revision`** — cualquier atribución con esa causa. Medida
    TEMPORAL documentada: sesgo medido sin mitigar; revisable con evidencia fresca.
  - **R3 `modulo_deterministico_sin_decision`** — triage propagado de D2/D3 (sin portador,
    quote no verificable).
  - **R4 `voto_dividido`** — `flag_voto_dividido=true`.
  - **R5 `posible_portador_no_considerado`** — cualquier bandera de D5.
  - **R6a `atribucion_sin_sintoma`** / **R6b `atribucion_no_verificable`** — anotaciones de
    D6 (consistencia síntoma↔atribución; sección D6, v6.1-D).
- **Por qué por mecanismo — la asimetría de costos:** un defecto de grafo mal etiquetado o
  exonerado **se escapa del pipeline de refinamiento en silencio** (nadie vuelve a mirar un
  caso "resuelto"); una derivación a revisión humana cuesta minutos. El gate #2 mostró los
  dos modos de escape (sobre-exoneración en CQ-017; etiqueta de frontera en CQ-025/031) —
  las reglas convierten cada modo conocido de escape silencioso en una derivación explícita.
- **Qué NO hace:** no decide el caso — deriva. Los motivos son acumulativos y el humano del
  triage recibe el caso con las anotaciones de D2/D3/D5/D6 como insumo.

### D5 — diligencia determinística de causas de ausencia (`aplicar_d5`)

- **Qué computa:** para atribuciones `completitud_kg`/`alucinacion_agente` (post-D2), extrae
  literales por regex cerrada (montos USD, códigos de 5+ dígitos, puntos normativos de 2+
  niveles, decimales con coma), los barre contra id+label+properties de los 4.050 nodos (sin
  provenances), descarta candidatos EXPUESTOS en los outputs completos re-ejecutados de la
  trayectoria, y corre D1 sobre los no expuestos → banderas con alcanzable/mejor_rank.
  **Nunca cambia causas ni jerarquías.**
- **Por qué por mecanismo:** el error documentado de barrido léxico en la construcción de la
  vara — las variantes "0.08"/"0,08" y "APRc"/"APR_c" dieron ausente/presente según la grafía
  (`docs/evidencia_vara_v3/verificaciones_vara_v3.md` §3b) — demuestra que "busqué y no está"
  es frágil incluso con máximo cuidado; una diligencia por regex cerrada + barrido exhaustivo
  no depende de elegir bien la grafía.
- **Qué NO hace (límites documentados):** (i) el filtro de exposición tiene su punto ciego —
  un candidato **expuesto pero mal descartado** por el agente no se flaggea (el agente lo
  tuvo a la vista; ese modo queda para el humano); (ii) **decimales con punto no se extraen**
  (colisión con puntos normativos de un nivel); (iii) **referencias de un solo nivel** tipo
  "1.1"/"3.9" **no disparan** barrido (demasiado genéricas). Las tres limitaciones están en
  el docstring y con casos fijados en tests.

### D6 — consistencia síntoma↔atribución (`aplicar_d6`, v6.1-D)

- **Qué computa (fuente normativa: su docstring en `capa_deterministica.py`):** extrae el
  síntoma del caso desde la traza post-hoc con el MISMO filtro que el input del verificador
  (`_sintoma_de_trace`: F = claims reprobados con centralidad; P = patas no cubiertas) y
  aplica dos reglas: **R6a** — si F y P están vacíos, toda atribución con causa distinta de
  `sin_defecto` se anota "atribución sin síntoma" y el caso va a triage, SIN reescribir
  causas ni jerarquías (el síntoma vacío es información para el humano, no licencia para
  inventar el veredicto correcto); **R6b** — una atribución PRIMARIA de síntoma
  noise_sensitivity/faithfulness se mapea por substring normalizado (bidireccional) contra
  los enunciados de F: si mapea SOLO a claims secundarios se degrada a secundaria; si mapea
  a un central queda intacta; **si no mapea a ninguno, rige el fallback conservador** —
  triage por `atribucion_no_verificable`, sin degradar (sin mapeo no hay hecho que autorice
  reescritura). Tras D6 el voto se recomputa (el previo queda como `voto_pre_d6`; el del
  verificador, intacto). Orden del pipeline v6.1-D: D2 → D3 → D5 → D6 → recomputo → D4.
- **Por qué por mecanismo:** la severidad de la atribución no puede exceder la severidad del
  síntoma declarado — F y P son **hechos del INPUT** del instrumento, computables por código.
  La regla está motivada por los hallazgos b (sobre-atribución ante síntoma vacío) y c
  (jerarquía indefinida en casos de solo-secundarios) de `docs/lectura_piloto_v6.md`, y la
  **regla de frenado está respetada**: D6 se implementó por estructura — semántica
  pre-registrada en el docstring y 9 tests con casos sintéticos — y **jamás se ajustó contra
  los 5 casos quemados del piloto**, que solo ilustran.
- **Hallazgo medido del dry-run (`docs/evidencia_capa_d/reporte_d6.md`):** los quotes de
  afirmación del verificador son **paráfrasis** de los enunciados del juez, no citas —
  **0/16 mapeos por substring** en los casos del piloto. El camino de degradación diseñado
  (R6b con mapeo) **no se ejercita en datos reales**: rige el fallback conservador (triage
  por `atribucion_no_verificable`, sin reescrituras).
- **Trade-off documentado:** bajo v6.1-D la ilustración del piloto queda **sin errores
  silenciosos** al costo de **más canal derivado**. La TASA real de triage por este motivo es
  desconocida y es **métrica pre-registrada de la validación sobre run_2/run_4** (grafos
  vírgenes de todas las etapas): si el motivo domina el canal, el mapeo se rediseña **por
  mecanismo** — nunca contra casos quemados.
- **Ilustración con asterisco — dry-run de D6 sobre los 5 JSONs congelados del piloto**
  (D6 fue motivado por estos casos; no es scoring ni re-validación; detalle completo en
  `docs/evidencia_capa_d/reporte_d6.md`):

| Caso | Acción de D6 | Voto final | Triage final |
|---|---|---|---|
| CQ-016 | R6a ×2 (atribuciones con síntoma vacío) | sin cambio (dividido) | + `atribucion_sin_sintoma` |
| CQ-024 | R6a ×4 | sin cambio | + `atribucion_sin_sintoma` |
| CQ-018 | R6b fallback ×4 (`claim_no_mapeado`) | sin cambio | + `atribucion_no_verificable` |
| CQ-033 | R6b fallback ×2 (`claim_no_mapeado`) | sin cambio | + `atribucion_no_verificable` |
| CQ-019 | ninguna | sin cambio | igual (R1) |

## 3. Nota de sensibilidad del umbral (top-10)

El umbral de alcanzabilidad de D1 es **top-10 por principio, no por tuning**: 10 es el
`limite` real con el que el harness sirve `buscar_nodos` al agente — lo que cae afuera del
top-10 es literalmente lo que el agente no vio. No se ajustó contra ningún caso.

Dicho eso, la sensibilidad medida queda anotada: **dos portadores reales quedaron en rank 11,
justo afuera del umbral** — el de CQ-031 (mejor rank **13** sobre las 10 consultas reales del
agente; **11** al sumar la pregunta entera y los n-gramas — dos conjuntos distintos: el
segundo es el que D1 simula) y el de la frecuencia de mercado en CQ-025/rep1 (mejor rank
**11**). El candidato de D5 en CQ-020 quedó en **35** (lejos). Los casos casi-umbral se leen
con esa conciencia: un rank 11 no es un rank 500, y el humano del triage tiene el
`mejor_rank` en la anotación para verlo.

## 4. Historia de construcción — hipótesis refutadas en el proceso

Dejo registradas las tres hipótesis mías que el propio proceso refutó, porque son parte de la
evidencia de cómo quedó calibrado el diseño:

- **(a)** Anticipé que el validador de quotes (D3) bloquearía el miss de CQ-025 — que el
  verificador fabricaba o distorsionaba evidencia al emitir `aplicacion_erronea`. El dry-run
  lo refutó: **los 5 quotes del gate eran reales** (verificaron por substring); el error era
  semántico (leer un quote fiel como declaración de alcance). Por eso la contención pasó de
  D3 a R2 (`docs/evidencia_capa_d/reporte_d3_d4.md`).
- **(b)** Pre-registré que CQ-020 "no emitió causas de ausencia" — tenía **5 atribuciones
  secundarias gatillables** (`completitud_kg`/`alucinacion_agente`) que mi expectativa pasó
  por alto (`docs/evidencia_capa_d/reporte_d5.md`).
- **(c)** Mi regex inicial de D5 **no extraía "0,08"** — precisamente el literal del error de
  barrido que fundó el módulo. Corregido por mecanismo (patrón `coeficiente_decimal`, con su
  limitación simétrica documentada) en D5b (`docs/evidencia_capa_d/reporte_d5b.md`).

## 5. Corrida consolidada sobre los 5 casos del gate

**ASTERISCO:** ilustración, no re-calibración — los módulos fueron **motivados por estos
casos**; ningún número de esta tabla es una medida de desempeño. JSONs completos en
`docs/evidencia_capa_d/corrida_consolidada/` (determinismo verificado: re-corrida de CQ-031
byte-idéntica).

| Caso | Voto v5.7 | Acción de la capa | voto_capa_d | Triage y motivos |
|---|---|---|---|---|
| CQ-031 | mayoría {context_recall, navegación} 3-0 | D2 corrige 3/3 (portador inalcanzable, mejor rank 11) | **mayoría {context_recall, alcanzabilidad_kg} 3-0** | sin triage |
| CQ-034 | mayoría {context_recall, completitud_kg} 2-1 | D5 gatilla 6 atribuciones; literales "3.9.1"/"3.9.2", 0 candidatos → sin banderas | igual al v5.7 | sin triage |
| CQ-017 | mayoría clave VACÍA 2-1 | D2 corrige 1 secundaria (rep 2); D5 sin literales | mayoría clave vacía 2-1 | **TRIAGE** — `exoneracion_total` (R1) |
| CQ-020 | dividido 1-1-1 | D3 verifica 3 quotes; D5 extrae "0,08": 4 candidatos, 3 descartados por exposición, 1 bandera (rank 35) | dividido 1-1-1 | **TRIAGE** — `aplicacion_erronea_bajo_revision` (R2) + `posible_portador_no_considerado` (R5) + `voto_dividido` (R4) |
| CQ-025 | mayoría {noise_sensitivity, aplicacion_erronea} 2-1 | D2 corrige rep 1 (nav→alc); D3 verifica 2 quotes | igual al v5.7 | **TRIAGE** — `aplicacion_erronea_bajo_revision` (R2) |

**El titular:** sobre los 5 casos del gate, el compuesto emite **2 veredictos correctos**
(CQ-031 — por construcción: el módulo nació de ese mecanismo — y CQ-034) y **deriva 3 a
revisión humana con motivo explícito**; **CERO veredictos incorrectos en silencio**. Contra
el v5.7 solo: 1 correcto, 1 triage y **3 miss silenciosos**.

## 6. Contadores a escala — el tablero de salud del instrumento

Cada corrida del compuesto produce, por construcción, contadores agregables y comparables
entre corridas y entre grafos:

| Contador | Qué mide | Valor en la corrida consolidada |
|---|---|---|
| **Discrepancias D2** (`capa_d.discrepancia=true`) | Tasa de error del LLM en la frontera navegación/alcanzabilidad | 5 (CQ-031 ×3, CQ-025 ×1, CQ-017 ×1 secundaria) |
| **Quotes no verificados D3** | Evidencia de `aplicacion_erronea` no auténtica | 0 (5/5 verificados) |
| **Banderas D5** | Posibles portadores no considerados en causas de ausencia | 3 emisiones / 1 candidato único (CQ-020) |
| **Triage por motivo** (R1..R6) | Dónde se concentra la derivación humana | R1: 1 caso · R2: 2 · R4: 1 · R5: 1 · R3: 0 (corrida pre-D6: R6 no existía) |
| **Anotaciones R6a** (atribución sin síntoma) | Sobre-atribución ante síntoma vacío | no aplica (D6 es posterior a esa corrida; en el dry-run del piloto: 6 — CQ-016 ×2, CQ-024 ×4) |
| **Fallbacks R6b** (`claim_no_mapeado`/`context_recall_sin_pata`) | Atribuciones no verificables contra el síntoma — su tasa es la métrica que decide si el mapeo se rediseña | no aplica (ídem; en el dry-run del piloto: 6 — CQ-018 ×4, CQ-033 ×2) |

Un instrumento sano a escala se ve así: discrepancias D2 estables o bajando entre versiones
del grafo, quotes no verificados en cero, banderas D5 raras y triage concentrado en pocos
motivos. Cualquier salto en un contador es una señal de dónde mirar, sin releer trazas.

## 7. Validación prospectiva (plan)

La validación de sistema del compuesto es **prospectiva** (protocolo detallado por separado,
en preparación): corrida del compuesto sobre las **fallas frescas de run_3** — fuera de los 5
casos quemados del gate — con **adjudicación humana ciega de una muestra pre-registrada**
(tamaño y selección fijados antes de correr). Métricas: acuerdo compuesto↔humano en la
muestra, y las tasas del tablero (§6) como descriptores de la corrida completa. Ningún caso
del gate participa.

## 8. Cómo correr

**Compuesto completo (D2 → D3 → D5 → D6 → recomputo → D4) sobre un caso del verificador:**

```bash
cd data/experiment/evaluacion
python capa_deterministica.py \
  --caso <salida_del_verificador>.json \
  --run run_3 \
  --trace <ruta_a_la_traza_posthoc_del_caso>.json \
  --out <salida_compuesto>.json
# stdout: version_capa + resumen_capa_d + triage_capa_d + voto_capa_d; el JSON completo (con voto_pre_d6) va a --out
```

**D1 suelto (prueba de alcanzabilidad de un portador):**

```bash
cd data/experiment/evaluacion
python test_alcanzabilidad.py \
  --run run_3 \
  --trace <ruta_a_la_traza_posthoc_del_caso>.json \
  --portador Restriccion_los_deudores_cuyas_financiaciones_se_encuentren_cubiertas_totalmente_con_garanti \
  [--hasta-paso N]
# imprime el dict completo (veredicto alcanzable, vocabulario ex ante, rank por consulta) como JSON
# (las trazas post-hoc del agente viven en la zona de trabajo de la evaluación, fuera de docs/)
```

**Tests (41, sin API):**

```bash
.venv/bin/python -m pytest data/experiment/evaluacion/capa_deterministica_test.py \
                           data/experiment/evaluacion/test_alcanzabilidad_test.py
```
