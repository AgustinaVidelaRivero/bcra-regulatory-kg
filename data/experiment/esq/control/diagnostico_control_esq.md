# Diagnóstico del control fallido — U-ESQ-1c-diag

Lectura pura del material persistido de U-ESQ-1c (commit 45e3752): $0 de API,
cero cambios de código o prompt. Fuentes primarias: `extracciones_control_esq.jsonl`
(control, 40 unidades), `corpus_v2/salida/*/extracciones_e1.jsonl` (producción,
mismas 40 claves, dedup last-wins), y las dos dbs de caché
(`esq/cache/esq_control.db`; `e1_extractor/cache/e1_extraccion.db`, SELECT only).
Todos los conteos de este documento los produce un único script de lectura,
`diag_esq1c.py` (en el paquete de revisión `revision_U-ESQ-1c-diag/`, junto con su
salida íntegra `diag_esq1c.json`); las afirmaciones puntuales llevan además su
one-liner. Este documento diagnostica y lista opciones; **no decide ningún
remedio** (eso es de la autora con la mesa, pre-registro §6).

## e. Comparabilidad de las dos corridas — VEREDICTO (precondición)

**Veredicto en dos partes:**

1. **Identidad de instrumento: VERIFICADA.** Las dos corridas difieren
   únicamente en el prefijo del system y el tool schema. Verificación
   request-por-request: recomputé offline los 40 requests cerrados y los 40
   abiertos (`prompt_e1.build_request_kwargs`, función pura), derivé sus keys
   (`llm_cache.compute_key`) y encontré las 80 filas en las dbs — 40/40 en
   `e1_extraccion|cv=e1-extractor-v1-p4793d6152608|think=0` (producción) y
   40/40 en `...pbca492bbf7c8...` (control). Diff de cada par de
   `request_json`: el system del abierto es el cerrado + `BLOQUE_CANAL_ABIERTO`
   byte a byte (aditividad verificada), el tool schema abierto es el objeto
   canónico `TOOL_SCHEMA_E1_CANAL_ABIERTO`, y **ningún otro campo difiere**:
   - modelo por llamada: `claude-haiku-4-5-20251001` en las 80 filas (columna
     `model` y campo `model` del `raw_json` coinciden). Producción corrió el
     2026-08-11/12 y el control el 2026-08-30, pero ambos con el MISMO snapshot
     pineado — el temor a una versión de modelo distinta queda descartado.
     Comando: `sqlite3 <db> "SELECT namespace, model, count(*) FROM cache GROUP BY 1,2;"`
   - sampling: ninguna de las 80 requests lleva `temperature`, `top_p`, `top_k`,
     `thinking` ni `stop_sequences` (escaneo de claves de `request_json`).
   - `max_tokens`: 8192 en las 80.
   - Además, el usage y el `tool_input_crudo` de cada registro jsonl coinciden
     con la fila de db de su key recomputada (40/40 en las cuatro
     verificaciones): cada registro persistido está atado a exactamente esa
     request. `stop_reason` = `tool_use` y cero bloques de contenido no-tool
     en las 80 respuestas.

2. **Limitación declarada: la lectura pareada unidad-a-unidad está confundida
   con ruido de sampling.** Que ninguna request lleve `temperature` significa
   default de la API (sampling estocástico), en las dos corridas por igual. No
   existe en el material persistido ninguna réplica cerrada-vs-cerrada de una
   misma unidad (las 6 líneas duplicadas de producción son reanudaciones que
   releen la caché — misma key, misma respuesta, no son muestras
   independientes; y ninguna de las 40 unidades aparece en el namespace viejo
   `p4dd055a4c5e8` — verificado matcheando los `messages` de sus 88 filas
   contra los 40 mensajes recomputados). Por lo tanto **no se puede separar
   "el prefijo abierto perturba la extracción cerrada" de "varianza de
   re-muestreo a temperature default"**: todo delta pareado de forma (labels,
   composición) tiene esa segunda explicación disponible. Lo que SÍ es robusto
   a este confound: los ceros absolutos (0/40 unidades con `tipo_propuesto` o
   `predicado_propuesto` en el crudo) y las tasas contra base propia (el canal
   preexistente `sujeto_propuesto` disparó 1/40 en el control vs 29/1.763 =
   1,6 % en producción — tasa base conservada).

   Consecuencia para el brazo B: el 10→3 tiene, además del confound de
   sampling, un sesgo de selección puro — las 10 unidades se eligieron
   PORQUE producción muestreó la firma inválida; re-muestrear unidades
   seleccionadas por un comportamiento extremo produce menos de ese
   comportamiento con CUALQUIER prompt (regresión a la media). El 10→3 no es
   atribuible al prefijo. El 0/10 de `canal_abierto` sí es un dato limpio.

## a. Brazo A (20 unidades con `omisiones_no_prosa`): la omisión ocurre ANTES del tipado

Qué hizo el modelo en el control con el contenido que en producción declaró
como omisión: **volvió a declararlo como omisión, igual**. Cruce pareado
(tabla completa por unidad en `diag_esq1c.json`, clave `a_brazo_A`):

- **19/20 unidades re-declararon `omisiones_no_prosa` en el control** (la
  única sin omisión, `ext::11.1.5.5`, es la unidad donde producción había
  extraído solo el nodo TextoOrdenado con 295 tok de salida y el control
  extrajo 4 entidades/4 relaciones — variación de muestreo, no un canal).
- Conteos de omisiones por unidad casi idénticos (prod 35, ctrl 43 en total;
  por unidad difieren en ±1); los TEXTOS se reformulan (0/20 listas
  byte-idénticas) pero describen el mismo contenido: tablas de ponderadores,
  fórmulas, cronogramas. Ejemplo pareado en `diag_esq1c.json`
  (`a_brazo_A.por_unidad["cap::2.1"]`).
- **Las 20 unidades del brazo son chunks flaggeados por E0** (contenido
  tabular/fórmula). One-liner del insumo: las omisiones nacen de la regla
  CONTENIDO NO-PROSA (`prompt_e1.py:156-164`), que ordena omitir y registrar
  porque el contenido está "DECLARADO NO-CONFIABLE" — no porque no encaje en
  los 6 tipos.
- Ninguna salida del control menciona ni roza los canales nuevos: escaneo de
  todos los strings del crudo de las 40 unidades con
  `tipo_propuesto|predicado_propuesto|canal|no encaja|fuera del esquema|EXPERIMENTAL`
  → 0 hallazgos en A, B y C (`diag_esq1c.py`, función `menciona_canal`).
- Extracción cerrada pareada: ents 141→158, rels 249→255 (totales del brazo),
  0/20 crudos idénticos, Jaccard exacto de (type, label) media 0,06 — misma
  inestabilidad de forma que en C (ver §c).

**Lectura:** la capa extra hipotetizada se confirma en los datos. Para estas
unidades la cadena causal de la omisión es «contenido tabular → regla NO-PROSA
→ omitir y registrar», y esa regla opera ANTES de cualquier decisión de tipado.
El bloque del canal abierto exige además "contenido normativo CLARO"
(`prompt_e1.py:213`), y el mismo prompt declara ese contenido no-confiable: las
dos instrucciones NO compiten — coinciden en omitir. El brazo A, tal como se
operacionalizó, no mide el canal: mide la estabilidad de la regla NO-PROSA (que
resultó altísima: 19/20). La debilidad estaba pre-declarada en el fundamento de
P1 («que el extractor haya declarado una omisión en prosa no garantiza que...
la emita como tipo_propuesto», `prerregistro_esq1.md:35-38`); lo que este
diagnóstico agrega es que no es solo «dos comportamientos distintos»: para
contenido tabular, el propio prompt ordena el primero y bloquea el segundo.

## b. Brazo B (10 unidades con presión dominio/rango): la presión se resolvió DENTRO del esquema

Las 10 unidades tenían en producción ≥1 relación rechazada por
`firma_invalida` con firma `Operacion|Excepcion --aplica_a--> Sujeto`. Destino
de esa relación en el control, unidad por unidad (detalle verbatim en
`diag_esq1c.json`, clave `b_brazo_B`; relaciones lado a lado reproducibles con
`diag_esq1c.py`):

| unidad | prod (firma inválida) | control: qué pasó con la relación |
|---|---|---|
| ext::7.9.1.8 | Operacion aplica_a | **misma firma inválida repetida** (mismo contenido) |
| ext::2.6.1::intro | Excepcion aplica_a | **misma firma inválida repetida** (label idéntico) |
| ext::5.7.3.3 | Excepcion aplica_a | **firma inválida distinta** (ahora 2× Operacion aplica_a) |
| ext::14.2.2 | Operacion «Acceso mercado cambios — dividendos VPU» | **re-tipada**: mismo contenido como Obligacion → aplica_a VÁLIDA |
| ext::10.10.2.13 | Operacion «Pago a la vista — importaciones» | **cambió a `ejecuta`**: la MISMA Operacion, expresada con el predicado válido del esquema (Sujeto ejecuta Operacion) |
| ext::4.8.5 | Operacion «Pago capital deudas elegibles» | **re-empaquetada**: el contenido aparece como Restriccion/Obligacion → aplica_a válidas (sujetos distintos) |
| ext::4.8.4.2 | Operacion «Liquidación deudas BOPREAL» | **re-empaquetada**: contenido como Restriccion → aplica_a válida |
| ext::7.9.1.9 | Operacion «Pago capital e intereses» | **desapareció** esa aplica_a; quedan las válidas vecinas |
| ext::10.3.7 | 2× Operacion aplica_a | **desaparecieron** ambas; quedan 4 aplica_a válidas (Obligacion) |
| cap::2.9.2.1 | Excepcion aplica_a | **desapareció** la relación; la entidad Excepcion sigue existiendo sin aplica_a |

Resumen: 3 repiten firma inválida (los 3 del conteo sellado), **4 re-expresan
el mismo contenido en forma válida dentro del esquema** (re-tipado de la
entidad fuente o cambio a `ejecuta`), 3 dejan caer la relación. **0 usan
`predicado_propuesto`.**

Cuantificación del cambio de la extracción cerrada, pareado (totales del
brazo; por unidad en el json): ents 53→58, rels 91→96, rechazos 13→5, 0/10
crudos idénticos, Jaccard (type,label) media 0,031. Output 1.198→1.294 tok/u
(+96).

**Lecturas, con su evidencia en contra:**

- A favor de la hipótesis de mesa (el cierre gana): cuando la presión existió,
  el modelo la resolvió con los recursos del esquema cerrado (re-tipar, usar
  `ejecuta`, omitir) — nunca con el canal. Y los tres cierres categóricos
  siguen intactos en el modo abierto, incluido uno que es directamente una
  inconsistencia del instrumento: `_tool_schema_canal_abierto()`
  (`prompt_e1.py:302-333`) hace deepcopy del schema de producción sin tocar la
  `description`, así que el tool de la corrida abierta se auto-describe como
  «schema cerrado v2 (6 entidades, 12 predicados...)» (`prompt_e1.py:234-238`)
  mientras el bloque final del system dice lo contrario.
- En contra (y esto acota el alcance del hallazgo): en ≥4/10 unidades el
  contenido SÍ era expresable en el esquema — la firma inválida de producción
  era una caja mal elegida, no contenido inexpresable (la prueba es que el
  control lo expresó válido: `ejecuta` existe exactamente para
  Sujeto→Operacion). Para esas unidades, la condición del bloque («no encaja
  en NINGÚN predicado», `prompt_e1.py:214`) nunca se cumple legítimamente: un
  modelo que extrae BIEN produce 0 propuestos ahí. Parte del cero del brazo B
  es entonces un problema del POOL (seleccionado por errores de producción,
  no por inexpresabilidad genuina), no solo de obediencia al cierre.
- El 10→3 del conteo sellado no es atribuible al prefijo: regresión a la
  media por selección + sampling estocástico (§e.2) lo explican sin necesidad
  de perturbación. El dato limpio del brazo es el 0/10 del componente
  `canal_abierto`, no el 10→3.

## c. Brazo C (10 limpias): estable en sustancia, inestable en forma — igual que A y B

Pareado por unidad (tabla en `diag_esq1c.json`, clave `c_brazo_C`): ents
49→50, rels 66→75 (totales), 0 rechazos en las dos corridas, 0/10 crudos
idénticos, Jaccard (type,label) media 0,076, output 977→1.025 tok/u (+47).
Los conteos por unidad se mueven ±1-3; los labels se reformulan casi todos
(ejemplo lado a lado de `cap::1.4.2.1` reproducible con `diag_esq1c.py`).

- El control negativo del canal se sostiene: 0/10 emiten propuestos; el único
  evento de canal en las 40 unidades es un `sujeto_propuesto` (canal
  PREEXISTENTE, descrito en el cuerpo principal del prompt) en
  `ext::7.5.7::intro` — consistente con su tasa base de producción (1,6 %).
- ¿«C también cambió mucho»? En forma sí, en la MISMA magnitud que A (0,06) y
  B (0,031): no hay señal de perturbación específica de los brazos con
  presión. Pero por §e.2 esta inestabilidad de forma NO es separable de la
  varianza de re-muestreo a temperature default: con los datos persistidos no
  se puede afirmar ni descartar que el prefijo abierto perturbe la extracción
  cerrada. Lo único que este brazo permite afirmar: la perturbación
  ADICIONAL atribuible al prefijo, si existe, no se distingue del ruido, y la
  sustancia (conteos, cero rechazos, tipos) quedó estable.

## d. Síntesis para la decisión (§6 del pre-registro) — sin decidir

**Clasificación del fallo: MEZCLA**, con tres componentes separables:

1. **Falla de diseño del control en el brazo A** (variante de «falla de
   implementación» de §6): su premisa «omisión declarada → propuesta emitida»
   era mala para este pool. Las 20 unidades son chunks flaggeados; su omisión
   la ordena la regla NO-PROSA antes del tipado, y el propio bloque del canal
   la excluye al exigir contenido «CLARO». El 0/20 no informa sobre el canal.
   Evidencia: §a (19/20 re-declaran, 0 menciones, las 20 flaggeadas).
2. **Hallazgo genuino, con alcance acotado, en B** (la rama «el modelo no lo
   usó teniéndolo disponible» de §6, insumo de ESQ-3): con el canal declarado
   en el system y en el tool schema, y con presión real de dominio/rango, el
   modelo resolvió el 100 % de los casos dentro del esquema cerrado (repetir
   la firma, re-tipar, `ejecuta`, omitir) y usó el canal nuevo 0 veces,
   mientras el canal preexistente análogo disparó a su tasa base. El alcance
   acotado: parte del pool B no contenía inexpresabilidad genuina (§b,
   evidencia en contra), así que el cero mezcla «obedeció al cierre» con «no
   había nada que proponer legítimamente».
3. **Limitación de instrumento transversal**: sin `temperature` fijada ni
   réplicas cerradas, toda lectura pareada de forma queda confundida con el
   sampling (§e.2). Cualquier rediseño hereda esto si no lo resuelve.

**Opciones de remedio, con su evidencia, costo y riesgo (evaluación, no
decisión):**

- **O1 — Reforzar la instrucción del bloque** (sin ejemplos de valores, que
  contaminarían la normalización ciega). Evidencia a favor: los tres cierres
  categóricos están intactos y el bloque es una posdata rotulada EXPERIMENTAL;
  el modelo usa canales de escape integrados al cuerpo (sujeto_propuesto, tasa
  base conservada) pero no la posdata. Evidencia en contra: en el brazo A el
  refuerzo no puede cambiar nada (la omisión es pre-tipado) y en parte del B
  no hay nada que proponer — un refuerzo podría solo mover C (falsos
  positivos). Rompe: prefijo nuevo → re-correr el control, ~USD 0,42
  (`resumen_final_control_esq.md` §4). Riesgo: medio — sobre-inducción del
  canal en unidades limpias (C es el único brazo que hoy aprueba).
- **O2 — Neutralizar los tres cierres en modo abierto** (condicionar
  `prompt_e1.py:57`, la regla 4 de la línea 135 y la description del tool a
  `canal_abierto=True`; con flag apagado, byte-idéntico a producción — el
  mecanismo aditivo actual ya garantiza eso y habría que preservarlo con
  edición condicional, no aditiva). Evidencia a favor: la description del tool
  en modo abierto hoy CONTRADICE al bloque (dice «schema cerrado v2»,
  §b) — eso es un defecto objetivo del instrumento, no una interpretación.
  Evidencia en contra: igual que O1, no toca la causa del brazo A. Rompe:
  prefijo y tool schema nuevos → re-correr el control (~USD 0,42) y re-sellar
  la aditividad (el selftest verifica `startswith`; una edición condicional
  del cuerpo lo rompe y exige rediseñar esa guarda). Riesgo: medio-alto — el
  modo abierto deja de ser «producción + posdata» y la comparabilidad
  producción/abierto (recargo D7 pareado) se re-negocia; más superficie de
  cambio que O1.
- **O3 — Rediseñar el brazo A** (premisa nueva: unidades con contenido en
  PROSA clara que no encaja en el esquema — p. ej. los `RECHAZO_PREDECLARADO`
  de V3 que §6 ya ordena reportar como categoría, o unidades con
  `type_invalido`/predicados inventados en producción — sin sembrar valores).
  Evidencia a favor: todo §a; además el pool actual (74 unidades con omisión)
  está dominado por tablas de ponderadores (observación §4 del pre-registro:
  esas unidades «no produjeron un solo type_invalido»). Evidencia en contra:
  ninguna en estos datos. Rompe: selección nueva (semilla y regla a re-sellar)
  + re-correr al menos el brazo A (~USD 0,21, 20/40 del costo medido).
  Riesgo: bajo en instrumento, medio en proceso — es un cambio del control
  post-resultado y debe declararse como tal (fe de erratas de P1-A, no
  recomposición silenciosa).
- **O4 — Separar prefijo de sampling antes de re-diseñar**: una re-corrida
  CERRADA de las mismas 40 unidades (prompt de producción intacto, namespace
  nuevo) daría la línea base cerrado-vs-cerrado que hoy no existe y
  convertiría §c en un test real de perturbación. Evidencia a favor: §e.2
  (hoy es inseparable); costo ≈ el pareado de producción, ~USD 0,39
  (`r_prod_40 = 0,00967 × 40`, resumen final §2). Evidencia en contra: si la
  decisión de la mesa no depende de si hay perturbación (p. ej. si se
  rediseña el brazo A de todos modos), este gasto no cambia nada. Riesgo:
  bajo (no toca prompt ni schema); fijar `temperature=0` en cambio SÍ rompería
  la comparabilidad con producción y no es esta opción.
- **O5 — Re-operacionalizar el conteo del brazo B** para que el re-expresado
  válido (re-tipado, `ejecuta`) cuente como «vuelve a reportar la relación»
  (hoy 3/10 sellado; con re-expresión ≥7/10 según §b). Evidencia a favor: la
  operacionalización sellada no anticipó la resolución intra-esquema, que es
  la mayoritaria. Riesgo: ALTO — es ajustar un umbral sellado después de ver
  el dato (exactamente lo que el pre-registro prohíbe: «no se ajustan
  post-hoc»). Se lista porque los datos la sugieren; si se tomara, sería
  redefinir el brazo en un pre-registro nuevo, no re-leer el actual.

Nota final sobre §6: la distinción sellada «canal-no-poblado vs
modelo-no-lo-usó» resuelve hacia la segunda rama para el brazo B (con el
alcance acotado del §b) y hacia «pregunta mal planteada» para el brazo A: allí
el canal no estaba realmente disponible para ese contenido, porque otra regla
del mismo prompt (NO-PROSA) ya había capturado la decisión antes.

---
Generado por U-ESQ-1c-diag (lectura pura). Reproducción íntegra:
`diag_esq1c.py` del paquete de revisión, corrido desde la raíz del repo con
`.venv/bin/python3 -B diag_esq1c.py` (solo lee; escribe únicamente
`diag_esq1c.json` en su propio directorio).
