BORRADOR — PENDIENTE DE FIRMA DE LA AUTORA

# Laudo de la release r2 del pipeline

**Estado:** borrador redactado el 2026-09-28, mientras corre la tanda 0. Se firma
al cierre de la tanda 0 (reporte de la fase 2a y lectura de la fase 2b), después
de completar la §4 con los hallazgos de esa lectura.

**Qué es r2.** La primera release del pipeline según el protocolo de B2.6: cada
cambio nace de una entrada de backlog con `capa_pipeline`, se implementa en una
unidad propia con mandato y freno, pasa un gate de release y produce un grafo
versionado (KG-Reextraído-r2). Rige el principio 9: los grafos ya evaluados
(r1 y los ensamblados de la tanda 0) no se corrigen; r2 es una versión
posterior. La tanda 1 (B6.1) corre con r2 y no arranca sin ella.

**Qué no es.** r2 no toca el esquema congelado (laudo `2593d4d`) ni el prefijo
de E1 (prompt congelado `e69feaaa…` y catálogo v3 `35e88c2dd0a2…`). Todo
candidato que los toque queda fuera de este laudo y se marca como tal en la §1. **[30/09/2026] Superado por decisión de la autora:** el ciclo B2.11 del plan decide que r2 incluye el cambio de prompt de E1 y la re-extracción de la tanda 0, con la ventana única del §7 del laudo congelado (enmiendas en borrador `data/experiment/esq/enmienda_uso_ventana_2026-09-30.md` y `docs/enmienda_preregistro_tanda0_2026-09-30_ventana.md`). Este párrafo, la §1.6 y la §3.2 se reescriben antes de la firma; hasta entonces rigen estas notas.

**Regla de implementación común a todos los candidatos.** Ningún cambio
reemplaza el camino actual: entra detrás del perfil o del manifiesto, con el
camino por defecto byte-idéntico al que produjo r1 y la tanda 0. Precedentes:
U-CABLE-V3 (perfil `produccion_dev` byte-idéntico por defecto), U-B5.3 (camino
sin corte byte-idéntico, selftest de manifiesto con 0 misses proyectados) y el
gate 6 (argumentos con default igual al comportamiento actual). Así r1 y la
tanda 0 siguen reproducibles con el código de r2.

---

## §1. Candidatos

Selección. El campo `release_candidata: "r2"` existe hoy solo en `BKL-0030` y
`BKL-0031` (`data/backlog/backlog.jsonl`, recontado el 28/09: dos entradas).
Los candidatos 3 a 5 son los que la autora nombró el 28/09. La §1.6 lista lo
que el repo destina a r2 por escrito sin tener el campo; cada uno lleva una
recomendación y la decisión es de la autora al firmar.

Vocabulario de sellos. «Sellado §3» = zona sellada de CLAUDE.md §3 (incluye el
cuarteto `llm_cache.py`). «Cerrado por el circuito» = módulo del pipeline
commiteado que produjo r1 y la tanda 0; el mandato U-TANDA0-2A (decisión 2)
prohíbe editarlo durante la tanda 0; este laudo, firmado, autoriza editarlo
solo dentro del mandato de su unidad y bajo la regla común de arriba.

Tarifa de referencia para costos: la corrida de E2 de la tanda 0 costó
USD 40,3495 por 2.434 unidades (`ad6d5ad`,
`corpus_tanda0/salida/presupuesto_compartido.json`), es decir USD 0,0166 por
unidad con E1, E3 y reintentos.

### Resumen

| # | Candidato | capa_pipeline | Sellos | Costo de API |
|--:|---|---|---|---|
| 1 | `BKL-0030` reintento por corte y partición | E1, E0 | cerrados por el circuito; `llm_cache.py` no se toca | de 0 a menos de USD 1 |
| 2 | `BKL-0031` detector de duplicados y fusión de forma | ensamblado | script nuevo; el paso 3 toca un módulo cerrado | 0 |
| 3 | `BKL-0006` / RX-10: cablear el parser de tablas | E0 | cerrados por el circuito; el parser no se edita | NO MEDIDO; censo en USD 0 primero |
| 4 | `cuarentena` booleana contra `"true"` | ensamblado (test T7) | cerrado por el circuito | 0 |
| 5 | Cláusula de mutuales (RT-C6) | E1-prompt | el remedio de raíz toca el prefijo | 0 con la opción recomendada |

### §1.1 `BKL-0030` — Reintento por corte y partición de la unidad

- **Defecto.** El reintento de U-B5.3 re-llama a 32.768 (`cliente_e1.py:60`)
  y el SDK 0.100.0 lo rechaza antes de enviarlo (`_base_client.py:731-740`).
  Tres unidades de cap quedaron sin extraer en E2 de la tanda 0; en r1,
  `cap::4.2.1.2` cortó también a 16.384 y es el único chunk mudo (M10 =
  1/1.763).
- **Cambio.** (a) Que el reintento llegue a la API: constante a 16.384
  (460,8 s, bajo la guarda) o timeout explícito en el constructor del cliente
  (`cliente_e1.py:154`; la guarda solo actúa sin timeout explícito,
  `resources/messages/messages.py:984`; la duración real de un request de
  32.768 sin streaming NO ESTÁ VERIFICADA). Streaming descartado: exige tocar
  `llm_cache.py` (sellado §3). (b) Cuando no alcance, partir la unidad con la
  mecánica de sub-chunking de E0 (`correr_e0.py:114-160`), disparada por
  «corte tras reintento» y no por tamaño; `cap::4.2.1.2` mide exactamente el
  umbral C8 de 26.182 caracteres, que se aplica en estricto (`:62`). E2 acepta
  las partes (`<id>::parteK`) en lugar de la unidad; la provenance sigue en la
  unidad documental real.
- **Módulos.** `cliente_e1.py`, `runner_corpus.py` (fase E1, `:469-510`),
  `correr_e0.py`, `e2_lib.py` (fan-in), `selftest_ub53.py`. Rigen
  `docs/decisiones_caching_extraccion.md` decisiones 1 a 3.
- **Prueba de aceptación.** Casos `cap::3.1.14.1`, `cap::4.2.1.2`,
  `cap::4.3.3.1`: las tres llegan a E3 o quedan partidas y ensambladas bajo su
  unidad; cero unidades con error definitivo por corte en la corrida de r2; M10
  en 0 sobre los TOs de desarrollo; camino sin corte byte-idéntico
  (`selftest_manifiesto.py` P3, P4 y P7; `selftest_ub53.py`).
- **Costo.** Con (a) a 16.384 el request del reintento es el mismo que armó la
  re-extracción dirigida de la tanda 0 (mandato U-TANDA0-2A-DIR, `825be18`),
  así que sus respuestas salen de la caché a USD 0 si las claves coinciden
  (verificable con `llm_cache.compute_key`, como D1.c de ese mandato). La
  partición paga solo las partes de `cap::4.2.1.2`: menos de USD 1, NO MEDIDO.

### §1.2 `BKL-0031` — Detector de candidatos a duplicado y fusión solo de forma

- **Defecto.** El ensamblado funde solo por identidad exacta (`e2_lib.py:22`,
  `:247-248`; `ensamblar_corpus.py:9-14`; guarda B1.5 en
  `r1_invariantes.py:16-21`). Cota superior en r1, sin adjudicar: M1 =
  3.538/6.529 y M2 = 1.785/6.529
  (`data/experiment/metricas_intrinsecas/kg_reextraido_r1.json`, sha256
  `d1fa3ee0…`). La duplicación entre cajas ya tiene destino r2 en
  `laudo_esquema_congelado.md:96`.
- **Cambio, en tres pasos con freno entre cada uno.** (1) Detector de solo
  lectura en la etapa de ensamblado: mismo tipo, mismo sujeto, texto similar
  por RapidFuzz (protocolo de M1/M2, `scripts/metricas_intrinsecas.py:96`,
  `:144-160`), mismo documento o documentos unidos por una arista
  `referencia`; reporta pares con su diff y no funde. (2) Adjudicación por
  muestra con semilla, a cargo de la autora, con intervalo de Wilson. (3) Solo
  si la tasa lo justifica (umbral: casilla de la firma), regla de fusión para
  diferencias de forma que nunca actúa si el diff toca números, plazos,
  porcentajes, fechas o sujetos; provenances acumuladas como en la fusión
  exacta.
- **Módulos.** Paso 1: script nuevo, ningún módulo editado. Paso 3:
  `r1_e4.py` (E4 determinístico, `:179-180`) o una etapa nueva del
  ensamblado, en convivencia con la guarda B1.5; cerrados por el circuito.
- **Prueba de aceptación.** Paso 1: reporte reproducible por comando y
  sellado sobre r1 y sobre los ensamblados de la tanda 0. Paso 2: muestra
  adjudicada con precisión de candidatos. Paso 3: M1 y M2 bajan contra la
  línea de base de r1; selftest con pares adversariales en el que ninguna
  fusión toca valores; suite y shapes sin regresiones.
- **Costo.** USD 0 (determinístico) más el tiempo de la autora en el paso 2.

### §1.3 `BKL-0006` / RX-10 — Cablear el parser de tablas a E0

- **Defecto.** La linealización de pdfplumber invierte pares de tablas del
  articulado; en capmin 1.2 quedan Bancos 2.500 / Restantes 5.000 en r1
  (fila B2.1, pendiente (1) y (1bis); `docs/backlog_reextraccion.md:267-284`). **[30/09/2026]** Primera prioridad dentro de U-R2-CODIGO (plan, fila B2.11, unidad 8; decisión de la autora): D2 de U-PRE-R2-DIAG atribuye a tablas las 8 pérdidas reales de contenido de C1 a C4 (EV2F-031 en `ric:7.2`, tabla marcada por E0 y sin extracción; EV2F-032 en `ric:9.2`, cuadro de códigos que E0 no marca), además de la afirmación falsa de `cap::1.2` (§4).
  El parser `e0_tablas.py` (B5.8.3, `d4e4e0a`) reconstruye el testigo
  correctamente (`data/experiment/segmentacion_84/b583_tablas/reporte_b583.md:16`:
  Bancos 5.000 / Restantes 2.500, pérdida 0,0), pero ningún módulo del
  pipeline de extracción lo invoca: hoy lo consumen solo los scripts de censo
  de B5.8.3, B5.8.4, U-COB-A y su selftest.
- **Cambio.** E0 serializa las tablas detectadas por `e0_tablas.py` en el
  texto del chunk con pares por columna. El formato de serialización es
  decisión de diseño de la unidad, con freno.
- **Módulos.** `e0_lib.py` / `correr_e0.py` (cerrados por el circuito);
  `e0_tablas.py` se importa sin editarse.
- **Prueba de aceptación.** El test convertido de C2 en la suite
  (`C2.tabla_1_2`) pasa de «persiste» a «resuelto»; en toda tabla cableada,
  verificación por multiconjunto (regla R-VERIF de B5.8.3) sin pérdida; los
  chunks sin tabla quedan byte-idénticos.
- **Costo.** NO MEDIDO. B5.8.3 midió 30 TOs del escalado y el testigo de
  capmin, no los diez de la tanda 0. Todo chunk cuyo texto cambie paga E1 y E3
  de nuevo (tarifa de referencia USD 0,0166 por unidad). Primer paso de la
  unidad: censo en USD 0 de los chunks de los diez TOs que el cableado
  modifica, y la cuenta de costo con ese número antes de gastar.

### §1.4 `cuarentena` booleana contra `"true"`

- **Defecto.** Generación 2 guarda `cuarentena` como booleano
  (`grafo_v2/code/assemble.py:298`) y generación 3 como string `"true"`
  (`e2_lib.py:388`). El test T7 de r1 compara con la string
  (`r1_tests.py:68`) y marca 11 «sin cuarentena=true» en KG-Refinado que no
  son defecto (`reports/revision_UB21_diag/inventario_B21_fase1.md:262`).
  Las shapes ya aceptan las dos formas (`scripts/shapes_validator.py:360-363`,
  `en_cuarentena`) y la suite las normaliza por generación (B2.1 fase 2,
  decisión 3). La app y los módulos de Neo4j no leen el campo (grep sin
  resultados en `app/` y `data/experiment/neo4j/`).
- **Cambio recomendado.** T7 lee la cuarentena con el mismo criterio que
  `en_cuarentena`. El grafo no cambia. Alternativa descartada: que E2 escriba
  booleano, porque cambia el sha de todos los grafos de generación 3 y rompe
  T7 sobre ellos.
- **Módulos.** `r1_tests.py` (cadena r1, cerrado por el circuito).
- **Prueba de aceptación.** T7 sobre KG-Refinado deja de marcar los 11 por
  formato y conserva las 8 `subclase_de` desde propuestos (contradicción C4/T7
  real, fuera de este cambio); T7 sobre r1 sin cambio de veredicto.
- **Costo.** USD 0.
- **Backlog.** Sin entrada todavía («candidata al backlog», changelog del
  27/09 del re-diagnóstico de B2.1). La entrada se escribe al firmar.

### §1.5 Cláusula de mutuales (RT-C6)

- **Defecto.** El punto 1.1.2.5 de protección dice «excepto que se trate de
  asociaciones mutuales o cooperativas, por las financiaciones que otorguen»
  (`e0_chunking/salida_tanda0/chunks_pro.json`, `pro::1.1.2.5`). En r1 la
  Excepción dice «No aplican estas normas a las asociaciones mutuales o
  cooperativas», sin la cláusula
  (`Excepcion_no_aplican_estas_normas_a_las_asociaciones_mutuales_o_cooperativas_a0051e`).
  La suite lo reporta como informativo en RT-C6-1
  (`reports/revision_UB21_fase2/regression_KG-Reextraido_UB21_fase2.json`,
  «cláusula … (informativa)=AUSENTE»). Especie: amputación. La excepción queda
  más ancha que la norma.
- **Opciones.** (a) Regla de calificadores en el prompt de E1: toca el prefijo
  congelado, exige enmienda al laudo `2593d4d` y re-extracción completa (E2 de
  la tanda 0 costó USD 40,35); fuera de r2. (b) Criterio nuevo en el
  verificador E3: rota el namespace de E3 y re-verifica todo (E3 y reintentos
  de la tanda 0: USD 22,28). (c) **Recomendada:** en r2 la cláusula pasa de
  informativa a test que documenta la persistencia, y el remedio de raíz se
  agrupa con otros cambios de prompt en una release posterior (B2.6: «los
  cambios de prompt/catálogo se agrupan en releases»).
- **Módulos.** Con (c): `scripts/regression_kg.py` y una entrada nueva de la
  fixture. El pipeline no cambia.
- **Prueba de aceptación.** Con (c): el test existe, da «persiste» en r1 y en
  r2, y figura en el reporte del gate.
- **Costo.** USD 0 con (c).
- **Backlog.** Sin entrada todavía («candidata al backlog», changelog del
  27/09 del cierre de B2.1). La entrada se escribe al firmar, con
  `capa_pipeline` E1-prompt.

### §1.6 Otros destinos r2 escritos en el repo, sin el campo

| Ítem | Ancla | Toca | Recomendación |
|---|---|---|---|
| Completar `esquema_v3_clases.json` con los seis ids del perfil (102 / 101) | fila B6.0 fase 2a, hallazgo E1: «laudo para r2» | catálogo JSON; no el prefijo de E1 | **entra**: USD 0; S19 queda sin el FAIL conocido. **[30/09/2026]** Absorbido por U-CAT-UNICO (fuente única del catálogo; plan, B2.11, unidad 6) |
| Doble conteo del checkpoint de cierre | fila B6.0 fase 2a, hallazgo del runner; `runner_corpus.py:356-372` | runner | **entra** con el candidato 1: USD 0 |
| Guarda de modalidad (deber emitido como `Condicion`) | `laudo_esquema_congelado.md:97`: «candidata r2» | prompt, probablemente | **no entra** salvo que la lectura de la vigilancia (1) en la tanda 0 lo pida (§4) |
| Pendientes de U-B1a: rangos, 196 conflictos de properties, 5 cross-TO, 41 `padre_sugerido`, política de cola | párrafo «Pendientes de laudo que deja U-B1a» del bloque B1: «insumo de la release r2» | ensamblado | **decide la autora**; el (d) se cruza con el candidato 4 |
| R6b | fila ESQ-3 del plan (retoques): «residuo para r2» | esquema | **no entra**: el esquema congelado se modifica solo por la vía de A8. **[30/09/2026]** Con la ventana usada en el ciclo B2.11, se decide en L-ESQ-R2 (plan, B2.11, unidad 5) |
| `BKL-0028` y `BKL-0029` | backlog | prefijo de E1 | **no entra**: rotan el prefijo y re-extraen todo. **[30/09/2026]** Entran al ciclo B2.11: se laudan en L-ESQ-R2 y los aplica U-CAT-UNICO (unidades 5 y 6); la re-extracción es la de U-REEXT-T0 (unidad 11) |
| S20 (`verificacion_informativa`) | hallazgo S20 del bloque B2 | nada | **no entra**: en E2 de la tanda 0, `ext::10.4.3.1` dio `tipo_obligacion_normalizados` 0 y la Obligación salió como `presentacion_informativa`; por la regla asentada el 27/09 es residuo de la generación anterior, y r2 se regenera en modo v3 |

---

## §2. Orden y dependencias

Precondiciones: cierre de la tanda 0 y de U-TANDA0-2A-DIR (sus respuestas en
caché alimentan el candidato 1); copia de resguardo de las dbs de caché (§3.2).

1. **Candidato 1 (`BKL-0030`)**, casos de prueba `cap::3.1.14.1`,
   `cap::4.2.1.2`, `cap::4.3.3.1`. Va primero porque cambia salidas de E1 que
   todo lo de abajo consume. Viaja con él el doble conteo del checkpoint.
2. **Candidato 3 (RX-10)**. También cambia texto de chunks de E0. Si el
   cableado modifica el texto de alguna de las tres unidades de cap, la prueba
   del candidato 1 se repite sobre el texto nuevo.
3. **Candidato 4 (cuarentena)**. USD 0 e independiente; va antes del 2 porque
   el detector y la suite leen el campo.
4. **Completar el catálogo JSON** (§1.6, si entra). USD 0; antes del gate.
5. **Candidato 2 (`BKL-0031`)**: paso 1 sobre el grafo candidato de r2, ya
   con los cambios de arriba; paso 2 por la autora; paso 3 solo si la tasa lo
   justifica.
6. **Candidato 5 (mutuales)**: el test entra a la suite en cualquier momento
   antes del gate.
7. **Corrida única de r2** sobre el corpus que se fije al firmar, con la
   proyección de misses de la §3.2 antes de gastar.
8. **Gate de release** (§3.1) y **versionado**: KG-Reextraído-r2 con sha,
   tabla de la suite, reporte de shapes, intrínsecas y costo; entrada en
   `data/experiment/neo4j/grafos.py`.

Cada candidato es una unidad con mandato propio y freno. La corrida del paso 7
es la única que materializa r2; las unidades prueban sobre sus casos.

---

## §3. Gate de release y preservación de la caché

### §3.1 Gate

Si cualquiera de los tres primeros puntos falla, r2 no sale.

1. **Shapes con perfil congelado.** `scripts/shapes_validator.py --perfil
   congelado --kg <kg de r2> --excepciones
   data/experiment/esq_v3_miembros/esquema_v3_clases.json --out <ruta
   versionada de r2, fechada>`. Bloqueantes en PASS: S1–S6, S15, S19 y S20
   (`shapes_validator.py:156`). S19 admite el FAIL conocido por los seis ids
   solo si el catálogo JSON no se completó.
2. **Regression suite con la fixture `696f3f94…`**
   (`scripts/regression_kg_esperado.json`, `2012832`).
   `scripts/regression_kg.py --kg <kg de r2> --generacion 3 --catalogo
   esquema_v3_clases.json --politica-cuarentena <la de r2> --esperado
   scripts/regression_kg_esperado.json --out <ruta versionada>`. La fixture
   elige la entrada por `kg_sha256` (su `_convencion`), así que r2 necesita una
   entrada propia sellada por la autora ANTES de correr el gate (decisión 6bis
   de B2.1): el estado esperado de r1 ítem por ítem, cambiado solo en los que
   un candidato resuelve (`C2.tabla_1_2` con el candidato 3; T7 con el 4; la
   cláusula de RT-C6 según la opción del 5). Criterio: 0 regresiones. La
   fixture cambia de sha; el nuevo se registra en el plan. **[30/09/2026]** Decisión de la autora: la entrada de r2 sigue las propuestas de D1 de U-PRE-R2-DIAG (`reports/u_pre_r2/d1_suite.md`). T4, T5 y E4-a8 se re-direccionan en U-R2-CODIGO (plan, B2.11, unidad 8; T5 con esperado persiste, opción A de D1); T7 y E4-a7 pasan con el catálogo único (U-CAT-UNICO, unidad 6); T2 queda como regresión real con causa documentada, salvo que entre el candidato del §4 sobre la fusión por descripción.
3. **Contadores de E1** en la corrida de r2: vocabulario retirado = 0
   (pre-registro de la tanda 0, paso 5); `tipo_obligacion_normalizados`
   reportado.
4. **Intrínsecas de generación 3**, en modo informativo hasta el laudo B3.1
   (B2.6): `scripts/metricas_intrinsecas.py --gen3 --kg <kg de r2> --nombre
   KG-Reextraido-r2 --e0 <salida de E0> --manifiesto <manifiesto de r2>`,
   contra la línea de base de r1 (`d1fa3ee0…`). Las métricas atadas a un
   candidato son aceptación de su unidad, no umbral general: M10 (candidato 1)
   y M1/M2 (paso 3 del candidato 2).
5. **Indicadores de cita** (gate 6), informativos, con `python3` 3.12.
6. **Reproducibilidad.** Con el código de r2 y el perfil por defecto, el
   ensamblado de desarrollo reproduce `8e2eadee…` y `0226e947…` byte a byte, y
   los selftests del pipeline siguen en verde.
7. **Nunca EV2** (principio 7; B2.6).
8. **Tablero de correcciones** (`docs/tablero_correcciones.md`). Al cerrar el gate
   se llena su columna «después de r2» con el mismo comando de cada fila, y cada
   meta queda cumplida o con su residuo declarado. No bloquea la salida de r2: es
   condición de la tanda 1 (`docs/checklist_pre_escalado.md`, «Orden y condiciones
   de la tanda 1»). Agregado el 29/09/2026.

### §3.2 Re-extraer paga solo lo que cambió

La clave de caché es sha256 del namespace más el request canónico, que hashea
todos los kwargs (`data/experiment/evaluacion/llm_cache.py:110-126`). El
namespace de E1 lleva el hash del prefijo (tanda 0:
`e1_extraccion|cv=e1-extractor-v1-p54a111e2175f|think=0`) y el de E3 su
versión de prompt (`e3_verificacion|cv=e3-verificador-v1-p21a836c7de6d|think=0`).

1. **Ningún cambio al prefijo de E1 ni al prompt de E3 en r2.** Con eso, todo
   chunk con texto igual arma el mismo request y sale de la caché a USD 0. **[30/09/2026]** Superado para el prefijo de E1: el ciclo B2.11 cambia el prefijo (U-PROMPT-R2) y re-extrae la tanda 0 (U-REEXT-T0); el prompt de E3 no cambia. La medición r2a (solo código, unidad 9) no llama a la API.
2. **Cambios de E0** (candidatos 1b y 3) alteran solo el texto de los chunks
   afectados: esos pagan E1 y, como cambia su salida, E3.
3. **Cambios de E2 y del ensamblado** (candidatos 2 y 4, catálogo JSON) no
   llaman a la API.
4. **Reintento del candidato 1** a 16.384: el mismo request que la dirigida de
   la tanda 0, así que sale de la caché.
5. **Proyección de misses antes de pagar**, con el patrón de
   `data/experiment/reextraccion_v2/selftest_manifiesto.py:209-246` (claves
   computadas sin llamar a la API y buscadas en la caché). Las claves de E3
   dependen de las salidas de E1, así que se proyectan después de resolver E1
   desde la caché. La lista de misses proyectados debe coincidir con los
   chunks declarados como afectados; un miss de más es deriva de clave y FRENO
   sin gastar.
6. **Las dbs de caché no se versionan** (`.gitignore` de `e1_extractor/` y
   `e3_verificador/`; `e1_extraccion.db` pesa 185 MB): antes de la corrida de
   r2 se hace una copia de resguardo fuera del repo. Perderlas obliga a pagar
   de nuevo la extracción (E2 de la tanda 0: USD 40,35) y, como E1 corre sin
   temperatura fijada (decisión 7 del pre-registro), la nueva salida no sería
   la misma.
7. Rigen las decisiones 1 a 4 de `docs/decisiones_caching_extraccion.md`
   (prefijo con breakpoint, costo con la fórmula de caching, usage logueado en
   todo call site nuevo, corridas con prefijo idéntico en secuencia).

---

## §4. Hallazgos de la tanda 0 que se suman al cierre

Se completa al cerrar la tanda 0, antes de firmar. Fuentes previstas: las
incorrectas de la observación (12), que van al backlog con `capa_pipeline` para
r2 (enmienda `8e13be3`); la lectura de las vigilancias (1) a (9); el reporte de
la fase 2a (E6); la lectura de la fase 2b.

| Hallazgo | Fuente | capa_pipeline | Módulos | Sellos | ¿Entra a r2? | Prueba | Costo |
|---|---|---|---|---|---|---|---|
| Bajo el prompt v3, `cap::4.2.1.2` entró a 16.384: 11.925 tokens de salida y `stop_reason` `tool_use`; en r1, con el prompt v2, había cortado a 16.384. Las otras dos entraron con 8.371 y 9.212. La opción (a) de `BKL-0030` (reintento a 16.384) podría bastar sin partición. No es garantía: E1 corre sin temperatura fija (decisión 7 del pre-registro) y otra muestra de la misma unidad puede cortar. | U-TANDA0-2A-DIR, D2 (`5fc7d3a`): `corpus_tanda0/salida_dirigida/reextraccion_dirigida.json`; `e1_extraccion.db`, `run_label` `tanda0_dirigida_e1` | E1 | `cliente_e1.py:60` | cerrado por el circuito | Informa la elección de la §1.1 entre (a) sola y (a) con partición; decide la autora al firmar | Los tres casos de la §1.1 | USD 0 para estas tres si el request de r2 coincide con el de la dirigida (misma clave, verificado por la mesa el 28/09); la dirigida costó USD 0,461274 |
| **(28/09/2026, U-AUDIT-TIPOS-V3, H1 y H4) El resolvedor de remisiones no parte de los tipos nuevos ni lee `termino`.** Solo usa como origen Obligacion, Restriccion, Excepcion y Operacion (`TIPOS_ORIGEN`, `r1_referencias.py:51`, aplicada en `:243`) y escanea `descripcion`, `condicion`, `alcance`, `umbral`, `plazo` y `detalle` (`PROPS_TEXTO`, `:52`). `ensamblar_tanda0.py:131-143` redirige `INVENTARIO_TOS` pero no `TIPOS_ORIGEN`. En KG-Tanda0-Desarrollo-r1 quedan 2.090 nodos excluidos como origen (1.178 Condicion, 381 Potestad, 531 Definicion) y 4 Definiciones con remisión en `termino`. Simulación en memoria con control 4.242 / 4.242 idéntico: +3.687 aristas `referencia` desde 343 nodos, 0 perdidas. Caso: la Condicion del monto de `cla::5.1.1.1`, cuya descripción dice «establecido en el punto 3.7» (verificado por la mesa en el grafo; la simulación da totales y no lista aristas). | `reports/u_audit_tipos_v3/inventario_U-AUDIT-TIPOS-V3.md`, Tabla 1, H1 y H4; `reports/u_audit_tipos_v3/p2_referencias_sim.json` (`a325949`, `24e0116`) | ensamblado | `corpus_v2/r1_referencias.py` (cadena r1), `tanda0/code/ensamblar_tanda0.py` (redirección) | cerrado por el circuito | Candidato; decide la autora al firmar | Re-ensamblar el desarrollo y reproducir la simulación: +3.687 aristas, 0 perdidas, y la remisión de `cla::5.1.1.1` al `cla::3.7` | USD 0 |
| **(28/09/2026, U-CONS-ARCO-EJEMPLO, parte A) Remisiones falsas por paráfrasis.** En KG-Tanda0-Diez-r1 (`dd42d6d9…`), la remisión de `cap::8.2.3.3` a los puntos 6.5.1 y 7.2.1 de Clasificación de deudores se resolvió como interna y generó nueve aristas hacia nodos de riesgo de mercado de `cap::6.5.1`. Causa: el resolvedor lee la descripción escrita por el extractor («de normas de Clasificación de deudores») y no el texto del punto («de las normas sobre “Clasificación de deudores”»); además, `RE_NORMA` (`r1_referencias.py:63-65`) no reconoce «normas de», y los puntos sin norma reconocida se tratan como del mismo documento (`:180-187`). Las mismas nueve aristas están en KG-Tanda0-Desarrollo-r1 (C3 y C4); en KG-Reextraído-r1 (C1 y C2) no, porque su descripción conserva «normas sobre» (verificado por la mesa el 28/09/2026). | informe de U-CONS-ARCO-EJEMPLO, parte A (`reports/u_cons_arco_ejemplo/informe_U-CONS-ARCO-EJEMPLO.md`); `ens_diez/r1/referencias_remisiones.json` y `ens_desarrollo/r1/referencias_remisiones.json` (`1b8916c`); código citado | ensamblado (referencias de la cadena r1) | `corpus_v2/r1_referencias.py` (cadena r1); `tanda0/code/ensamblar_tanda0.py` si hace falta redirigir la fuente del texto | cerrado por el circuito | Candidato, corrección previa a la tanda 1, junto con H1 y H4 | Detectar las remisiones sobre el texto de E0 del punto de origen (por `chunk_id`) y no sobre la paráfrasis; cuantificar en el grafo de diez cuántas remisiones cambian de destino; `cap::8.2.3.3` llega a `cla::6.5.1` y `cla::7.2.1` | USD 0 |
| **(28/09/2026, U-AUDIT-TIPOS-V3, H2) Los tres tipos nuevos se funden por label.** `entity_slug_v3` (`e2_lib.py:122`, copia textual de `grafo_v2/code/assemble_v3.py:127`) deduplica Restriccion, Obligacion y Excepcion por descripción y el resto por label, así que Condicion, Definicion y Potestad caen en la rama por label. Conflictos de properties en E4 de KG-Tanda0-Desarrollo-r1: 43 de `descripcion` en 32 nodos (Condicion 27 en 19, Definicion 13 en 10, Potestad 3 en 3) y 8 de `Definicion.termino`. Gana la primera escritura y la variante descartada no queda en el nodo: riesgo de fundir contenidos distintos. **DECISIÓN ABIERTA de la autora: la clave de fusión de los tres tipos.** | `reports/u_audit_tipos_v3/inventario_U-AUDIT-TIPOS-V3.md`, Tabla 1, H2; `r1/e4_conflictos.json` del ensamblado | E2 | `e2_reduce/e2_lib.py` (su selftest exige la copia idéntica a `assemble_v3.py`) | cerrado por el circuito | Candidato con decisión abierta | Conflictos de properties de los tres tipos en E4 en 0 o declarados, y ningún nodo que funda contenidos distintos en una muestra | USD 0; cambia ids, así que exige actualizar la fixture de la suite |
| **(28/09/2026, U-AUDIT-TIPOS-V3, punto 3) Nodos sin ninguna arista en KG-Tanda0-Desarrollo-r1:** Condicion 35, Operacion 30, Definicion 13, Sujeto 12, Comunicacion 3, Obligacion 1. De las 35 Condicion, 33 perdieron todas sus relaciones por rechazos de la matriz congelada y 2 no tenían relaciones emitidas; en ninguna el extractor emitió `establecida_en`. Con H1 corregido, 9 de las 35 recibirían alguna remisión y 26 seguirían aisladas. **DECISIÓN ABIERTA de la autora: derivar `establecida_en` de la procedencia, en el ensamblado, para todo nodo de contenido que no la tenga.** | `reports/u_audit_tipos_v3/inventario_U-AUDIT-TIPOS-V3.md`, punto 3; `p3_resumen.json`, `p3_filas.json`, `p3b_cruce.json` | ensamblado | E2 o un paso nuevo del ensamblado | cerrado por el circuito | Candidato con decisión abierta | Cero nodos de contenido sin `establecida_en`; el resto de los aislados, declarado por causa | USD 0 |
| **(28/09/2026, U-CONS-EJEMPLO-Y-BUSQUEDA) Procedencia de las remisiones.** Verificado por la mesa en el código: la arista `referencia` copia como `provenance` la procedencia primaria del origen y como `provenances` su lista completa (`r1_referencias.py:232-233`), pero el TO y el punto de origen con que se resuelve la remisión salen solo de la primaria (`:245`, `:256`); la vista runtime que ve el agente usa solo la procedencia primaria (`neo4j/grafos.py:16-19`; mismo patrón en `comun_r1` y `comun_tanda0`). Que «seis puntos de ext nunca figuran como origen» está NO VERIFICADO por la mesa: no figura en el informe de U-CONS-EJEMPLO-Y-BUSQUEDA (repuesto el 28/09/2026) ni en los demás archivos de `24e0116`. | código citado; `reports/u_cons_ejemplo_busqueda/informe_U-CONS-EJEMPLO-Y-BUSQUEDA.md` (vacío en `24e0116`; repuesto el 28/09/2026, commit PENDIENTE) | ensamblado y vista del agente | `corpus_v2/r1_referencias.py`; `tanda0/code/comun_tanda0.py` y `ev2_r1/code/comun_r1.py` (vista) | cerrado por el circuito; la vista del cuarteto no se toca | Candidato; alcance a definir | Remisiones resueltas desde cada procedencia del origen; la vista del agente con todas las procedencias; puntos que nunca son origen en 0 o declarados | USD 0 |
| **(28/09/2026, U-CONS-EJEMPLO-Y-BUSQUEDA) Test nuevo de la suite: el ejemplo `cla::5.1.1.1`.** La Operacion con sus dos condiciones unidas y la remisión al `cla::3.7`. Hoy daría «persiste» en KG-Tanda0-Desarrollo-r1 (las dos Condicion sin aristas y sin remisión) y se cumple en KG-Reextraído-r1 (dos Restriccion con `limita` hacia la Operacion y `referencia` al 3.7). El gate de r2 exige «resuelto». | consulta U-CONS-EJEMPLO-Y-BUSQUEDA, A3 (recorrido de la mesa sobre los dos `kg.json`); `reports/u_med_ejemplo/umed2_analista_paso2_resultado.json` | regression suite | `scripts/regression_kg.py` y entrada nueva de la fixture, sellada por la autora | fixture sellada: la entrada nueva la sella la autora | Entra con el gate de r2 | «resuelto» sobre el grafo de r2 | USD 0 |
| **(28/09/2026, U-INV-CANDIDATOS-2 y U-CONS-EJEMPLO-Y-BUSQUEDA) Actualización de la fila «Procedencia de las remisiones»**, que no se edita. El informe de U-CONS-EJEMPLO-Y-BUSQUEDA quedó commiteado en `f96c5d0`; esa fila decía «repuesto el 28/09/2026, commit PENDIENTE». Los seis puntos que figuran en la lista completa de procedencias (`provenances`) de alguna remisión pero nunca como su procedencia primaria (`provenance`) son `ext::3.18.1.1`, `ext::3.18.1.2`, `ext::4.5.3`, `ext::4.6.1.3`, `ext::4.7.2` y `ext::7.1.4`, medidos sobre KG-Reextraído-r1 (`0226e947…`); con eso, lo que esa fila marcaba NO VERIFICADO queda respaldado. | `reports/u_inv_candidatos/v2_resultado.json`, clave `paso1.puntos_solo_en_provenances_no_en_provenance` (sha256 `fc2138f4…`, `791166d`); `reports/u_cons_ejemplo_busqueda/informe_U-CONS-EJEMPLO-Y-BUSQUEDA.md` (`f96c5d0`) | ensamblado y vista del agente | los de la fila «Procedencia de las remisiones» | los de esa fila | Actualiza ese candidato; decide la autora al firmar | La de esa fila: los seis puntos pasan a figurar como origen de sus remisiones, o quedan declarados | USD 0 |
| **(29/09/2026, lectura de la observación (12), orden 20) El catálogo v3 no tiene sujeto de nivel órgano.** En `lingob::2.3.2::intro`, la Obligacion «Alta Gerencia implementar procedimientos conducta profesional» tiene `aplica_a` hacia `Sujeto_entidad_financiera`, pero el obligado del punto es el Directorio: lingob separa Directorio, Alta Gerencia y Comité de auditoría (nota de la lectura asistida, hecha por una instancia de modelo y revisada por la autora; capa `catálogo`). Ni `esquema_v3_clases.json`, ni `prompt_v3_b54.py`, ni `perfil_e1.py` mencionan «directorio» (0 apariciones en cada uno, `grep -i -c`, 29/09/2026). El remedio es abrir un id de nivel órgano, y el catálogo v3 (`35e88c2dd0a2…`) es parte del prefijo de E1, que este laudo no toca («Qué no es»); completar solo el catálogo JSON no alcanza, porque E1 valida los sujetos contra el bloque v3 del perfil (hallazgo E1 de la fila B6.0 fase 2a del plan). Las otras cuatro incorrectas de (12) son `E1-prompt` (`BKL-0032`, `BKL-0033`, `BKL-0035`, `BKL-0036`) y quedan fuera de r2 por la misma regla. | `reports/tanda0/obs12_lectura/fila_obs12.md` (orden 20, índice del sorteo 1992); `veredictos_obs12.csv` (`f51bb1f`); `BKL-0034` | catálogo | `b54_catalogo_v3/code/prompt_v3_b54.py` (`BLOQUE_CATALOGO_V3`); `esq_v3_miembros/esquema_v3_clases.json` | prefijo de E1 SELLADO; re-sello como `BKL-0028` y `BKL-0029` | No con el alcance de este laudo: se agrupa con los cambios de prompt y con la decisión sobre la matriz congelada; decide la autora | La arista del índice 1992 re-leída: `aplica_a` hacia el id de órgano y no hacia `Sujeto_entidad_financiera` | Rota el prefijo: re-extracción del corpus de la release (referencia: E2 de la tanda 0, USD 40,35 para diez TOs) |
| **(29/09/2026, lectura de la matriz congelada, `bb90861`) Candidato: control de aristas entre dos nodos con la misma descripción.** En la lectura asistida de las 105 relaciones que la matriz congelada rechazó (instancia de modelo, revisada por la autora), 5 de las 12 incorrectas unen dos nodos con la misma descripción: C22 (Condicion `condicion_de` → Potestad, `cap::5.1.2`) y M56 a M59 (Condicion `condicion_de` → Condicion, con la misma etiqueta además; `cla::6.5.1.3`, `cla::6.5.1.6`, `ext::10.10.2.9`, `ext::3.5.1.5`). La nota de la lectura describe cada una como una arista que relaciona el punto «consigo misma». Una sexta fila con descripción idéntica, M50 (Excepcion `exceptua_obligacion` → Operacion, `ext::8.5.17.25`), está marcada como correcta en la lectura asistida: una regla que retirara estas aristas sin revisión habría retirado una correcta en esta muestra. **Alcance por medir:** la evidencia sale de relaciones rechazadas, antes de E3; cuántas aristas así hay en el grafo aceptado no está medido. | `reports/u_estudio_matriz/lectura/resultado_lectura_matriz.md`; lecturas asistidas en `bb90861` | ensamblado | script nuevo de solo lectura en la etapa de ensamblado; una regla de retiro, si se decide, en el ensamblado | cerrado por el circuito | Candidato; alcance a medir | Censo de aristas con origen y destino de igual descripción en KG-Reextraído-r1 y en los ensamblados de la tanda 0; sobre las relaciones de la lectura, el control marca las seis, M50 incluida como caso a revisar | USD 0 |
| **(30/09/2026, consulta de solo lectura y decisión de la autora) Afirmación falsa por tabla no detectada en `cap::1.2` (`BKL-0006`; asentada primero como `BKL-0023`, que es el rastro de esa inversión en el nodo de compañías financieras y no reaparece en la generación 3).** En r1 (`0226e947…`), KG-Tanda0-Desarrollo-r1 (`eab2fdd0…`) y KG-Tanda0-Diez-r1 (`dd42d6d9…`) las dos Restricciones de `cap::1.2` dicen bancos 2.500 y restantes entidades 5.000 millones de pesos; el PDF dice bancos 5.000 y restantes 2.500 (`data/backlog/propuestas/C2_montos_12.md:31-32`). E0 no marca el chunk como tabla (`chunks_cap.json`, `cap::1.2`, `contenido_tabular` falso), así que la regla del prompt contra copiar valores de celdas no se aplica. En desarrollo la suite da no aplica en `BKL-0006` y `BKL-0023` (`reports/tanda0/regression_ens_desarrollo.md:15-16`), un falso negativo; en la entrada de r1, `BKL-0006` persiste. | `data/backlog/backlog.jsonl:6` y el evento `nota` del 30/09 (`:87`); tablero, fila propia | E0 (detección de tablas) y suite | `e0_lib.py`; `scripts/regression_kg.py` (matchers de `BKL-0006` y `BKL-0023`) | fixture `696f3f94…` (la entrada de r2 la sella la autora) | **Entra**: U-R2-CODIGO (plan, B2.11, unidad 8; decisión de la autora del 30/09), con el candidato 3 (RX-10) | Montos iguales al PDF u omisión registrada; los dos ítems de la suite aplicables y en «resuelto» | USD 0 en código; re-extracción del chunk marcado dentro de U-REEXT-T0 |
| **(30/09/2026, D1 de U-PRE-R2-DIAG, `159c1e2`) T2: la fusión por descripción junta reglas distintas con igual redacción.** En KG-Tanda0-Desarrollo-r1, la Restriccion del 125 % de `ext::7.5.3` y la de `ext::7.8.5.1` quedan en un solo nodo: E2 deduplica Restriccion, Obligacion y Excepcion por descripción (`entity_slug_v3`, `e2_lib.py:122-123`) y las dos unidades emitieron la misma; en r1 no se funden (tres slugs distintos). La oración es idéntica, pero «Esta opción» remite a opciones distintas: la ampliación del plazo de liquidación en 7.5.3 y la acumulación de fondos en garantía en 7.8.5.1. El nodo fundido pierde a qué se aplica el tope (`reports/u_pre_r2/d2_ausencias.md:215-222`, clasificación asistida aceptada por la autora el 30/09). Regresión real, clase (a), del ítem T2 (`reports/u_pre_r2/d1_suite.md:62-79`). | D1 de U-PRE-R2-DIAG | E2 (clave de fusión) | `e2_lib.py` (`entity_slug_v3`) | cambia ids de nodo y la fixture | **Candidato, junto con H2 (fila de este §) y `BKL-0031` (§1.2):** la fusión no junta nodos de puntos distintos por igualdad de descripción; decide la autora al firmar | T2 resuelto sobre el grafo de r2 (al menos 5 nodos con «125 %» en ext); ningún otro ítem de la suite regresa | USD 0 (re-ensamblado) |
| | | | | | | | |

---

## §5. Decisiones de la autora a la firma

1. Qué candidatos de la §1.6 entran.
2. Opción del candidato 5 (recomendada: c).
3. Umbral del paso 3 del candidato 2 (tasa de candidatos correctos que
   justifica la regla de fusión).
4. Sobre qué corpus se materializa r2: los cinco TOs de desarrollo, como r1, o
   los diez de la tanda 0.
5. Tope de gasto de la release, con el censo del candidato 3 ya hecho.
6. Política de cuarentena que declara la entrada de r2 en la fixture.
7. Si el gate suma una muestra de precisión de aristas de extracción sobre
   KG-Reextraído-r2, con el método de la observación (12) (enmienda `8e13be3`
   §2.1: 30 aristas sorteadas, lectura contra el texto, Wilson al 95 %), como
   evidencia de mejora que no usa EV2 (§3.1, punto 7). Con 40 preguntas por
   celda, EV2 no distingue celdas (tabla pre-adjudicación de E5 de la tanda 0,
   `reports/tanda0/tabla_celdas_E5.json`). Agregado el 29/09/2026 desde el
   checklist previo al escalado.

## Firma

Pendiente.
