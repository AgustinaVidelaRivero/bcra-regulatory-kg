# Pre-registro — Fidelidad EV2 de KG-Reextraído-r1 (U-B1.8, plan v7, issue #16)

Este documento se redacta ANTES de correr agente alguno sobre KG-Reextraído-r1
y ANTES de leer respuesta alguna, sin abrir el material sellado del examen
(las 40 preguntas y los 164 criterios no se leyeron para diseñar nada: todo lo
fijado acá sale del protocolo sellado y de los reportes agregados de la corrida
base). Se sella por commit de la autora antes de la fase B; toda modificación
posterior es enmienda separada, jamás ajuste silencioso (principios 7 y 9 del
plan; régimen de válvula de `docs/protocolo_corrida_ev2.md`).

**Declaración de ceguera:** al momento de redactar este pre-registro no existe
ninguna traza de r1 sobre EV2, no se abrió
`data/experiment/exploracion/ev2_fidelidad/preguntas_ev2_fidelidad.json`
(sha256 `1d58733699c325c90510e1ead5f18eac6c3cd970ee3b0ab7ff141da539162b40`,
verificado idéntico al manifest sellado `9c44516`), y el único material de EV2
consultado son los reportes agregados ya commiteados (`reporte_ev2.md`,
`atribucion_fallas.md`, protocolo y pre-registro de la corrida base).

## 0. Qué es y qué no es

- **ES** la única medición de KG-Reextraído-r1
  (`data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json`, sha256
  `0226e9477baee02d772bbfecee78a49441b189d0e0512ca5e22956dfb084196a`,
  6.529 nodos / 17.772 aristas, commit `185e042`) sobre el eje de fidelidad
  de EV2, con el instrumento sellado de EV2 sin ningún cambio. Rige el
  principio 7: r1 se mide sobre EV2 UNA sola vez; su resultado alimenta dos
  laudos de la autora (promoción a vigente; brazo KG de A2.1).
- **NO ES** una comparación de retrievers (harness congelado, índice booleano
  in-memory, mismas condiciones que la corrida base: la única variable es el
  grafo); **NO** corrige nada de r1 (principio 9: lo que falle va a r2);
  **NO** re-mide KG-Base / KG-Refinado / KG-Reextraído (sus tablas están
  selladas en `64de678` / `40603a9` / `85d9fdb` y se citan).

## 1. Instrumento (sellado, sin cambios)

- **Set:** las 40 preguntas / 164 criterios de fidelidad de EV2 (`9c44516`).
  El eje de navegabilidad NO se corre (no es objeto de esta unidad).
- **Agente:** cuarteto congelado
  `data/experiment/evaluacion/{loader,harness,judge,llm_cache}.py` (sha256
  verificados verbatim al inicio y al cierre de cada etapa; ninguno se edita),
  vía `runner_ev2.correr_grafo` (commit `bb89a8e`) sin editar: mismo modelo
  hardcodeado en `harness.MODEL`, misma captura completa (traza + steps_full
  + raw_turns_agent + metadata).
- **Juez:** v1 congelado (`data/experiment/ev2_juez/prompt_juez_v1.md` sha256
  `fd446f8e61f46033d7de9b862121c698b2c52dcc2696b7f10993f44e509f5455`,
  `juez.py`, `mapping.py`), N=3 ciego, mediante el pipeline ciego de la
  corrida base (`ev2_fidelidad_eval/code/pipeline_fidelidad.py`, `b624865`)
  sin editar. Mapping §2 en código; veredicto modal §4.
- **Encadenamiento §7:** re-corrida N=3 del agente para cada pregunta con
  veredicto base `parcial` (trigger mecánico único) + auditoría simétrica
  N=3 sobre ceil(10 %) de los `correcto` (mínimo 1; el laudo del mínimo es
  el de `9044a04`). Agregación por par con `agregar_par` IMPORTADO de
  `ev2_encadenamiento/code/agregacion_enc.py` (`9044a04`), incluida su regla
  de votos `requiere_adjudicacion` por invariancia.
- **Adjudicación:** worksheet ciego para la autora, molde `03ebe83`
  (`ev2_adjudicacion/code/`): fichas para todo `requiere_adjudicacion` +
  muestra simétrica ceil(10 %) de `correcto` y ceil(10 %) de
  `parcial`+`incorrecto` sobre veredictos FINALES; ids opacos; selftest
  no-fuga antes de entregar.
- **Atribución causal post-corrida:** regla sellada de A0.2
  (`ev2_reporte/regla_atribucion.md`, commit `40603a9`) aplicada tal cual a
  las trazas de r1: mismas cuatro clases y precedencia, misma regla de censo
  (`resolucion.AnclaIndex`: match exacto, contenedores >10 excluidos), replay
  estándar y fuerte obligatorios, doble corrida byte-idéntica. La sensibilidad
  por descendientes se reporta como columna informativa (H24), fuera de la
  regla, igual que en `85d9fdb`.

## 2. Adaptador de r1 (extensión en módulo nuevo; nada sellado se edita)

- r1 conserva en cada provenance las claves `archivo`/`punto` de
  KG-Reextraído y agrega `chunk_id`/`paginas`/`ancestros` (provenance rica).
  El adaptador es el MISMO mapeo de la corrida base
  (`comun_ev2._map_prov_v2`: `{archivo, punto}` → `{source_doc, location}`),
  aplicado por `ev2_r1/code/comun_r1.py`:
  - **vista runtime** (lo que ven las tools): provenance PRIMARIA mapeada,
    construida con las dataclasses y el merge del loader congelado — el
    patrón exacto de `_cargar_runtime_v2` de la corrida base;
  - **vista de censo:** `provenances` COMPLETAS mapeadas (r1 ya trae la
    lista completa).
  Las claves ricas no viajan a las tools ni al censo: la regla del censo no
  cambia (comparabilidad con la corrida base).
- `comun_r1.py` registra la entrada `"r1"` en el dict `comun_ev2.GRAFOS`
  (en memoria) y reemplaza en memoria el despachador
  `runner_ev2.cargar_runtime` por uno que atiende `"r1"` y delega los demás
  grafos sin cambios. Ningún archivo sellado se edita en disco; los sha se
  verifican verbatim al inicio y al cierre de cada etapa.
- Verificación previa obligatoria: sha256 de r1 == `0226e947…` antes de toda
  operación (patrón `verificar_grafos`, extendido a r1).

## 3. Censo previo (fase A, antes de correr el agente)

Censo de las 40 anclas del gold sobre r1 bajo la regla sellada del censo EV2
(`resolucion.AnclaIndex.resolver`: match EXACTO de punto normalizado, sin
descendientes, contenedores >10 anclas excluidos — la misma regla de
`regla_atribucion.md` §2 y del censo de `5b02d22`). La regla NO se cambia.
Por ancla se reportan además dos columnas INFORMATIVAS (diagnóstico de
granularidad, H24, mismo formato que `atribucion_fallas.md` §4):
`crudo_incl_contenedores` y `con_descendientes`. Salida:
`ev2_r1/censo/censo_anclas_fidelidad_r1.{json,md}`, con la fila de r1 AL LADO
de las tres filas selladas de la corrida base (citadas, no recomputadas sobre
otros grafos: el recomputo corre solo sobre r1).

## 4. Corrida (fase B, tras el sello y la autorización)

- **Población:** las 40 preguntas de fidelidad. No hay descuento por censo:
  el censo de fidelidad es diagnóstico (la pregunta corre aunque su ancla no
  resuelva, igual que en la corrida base).
- **Orden:** lista de los 40 casos ordenada por id →
  `random.Random("orden-ev2-r1").shuffle` (semilla NUEVA declarada acá;
  mismo mecanismo del protocolo §5). Persistido en `ev2_r1/orden/`.
- **N:** agente N=1 base; juez N=3 por respuesta; re-corrida N=3 del agente
  SOLO para veredicto base `parcial` (trigger mecánico único, sin otra
  causal); auditoría simétrica N=3 sobre ceil(10 %) de los `correcto`,
  mínimo 1, muestreo `random.Random("auditoria-ev2-r1")` sobre ids
  ordenados (generador nuevo, misma regla que `9044a04`). Sesgo residual
  alcista declarado, idéntico al de la corrida base (regla compartida:
  la comparación con las tablas selladas queda limpia).
- **Anti-cache (protocolo §4, patrón rt_c6_n3):** db propia por
  corrida/etiqueta bajo `ev2_r1/cache/` (gitignorado): agente base
  `ev2_r1_base.db`; juez base `ev2_r1_eval_r{1,2,3}.db`; agente §7
  `ev2_r1_enc_r{1,2,3}.db`; juez §7 `ev2_r1_enc_juez_r{1,2,3}.db`. Labels
  homónimos. **0 cross-hits exigido** entre repeticiones (keys disjuntas +
  access_log); hits intra-db esperables solo por textos idénticos
  (never-pay-twice), declarados y contados. Toda llamada va por
  `llm_cache.CachingClient` con el namespace vigente del circuito EV2
  (dominios `agent` / `juez_ev2`, mismos `make_namespace` de la base; el
  `graph_fingerprint` de r1 separa el namespace del agente por construcción).
- **Ceguera del juez:** input EXACTO prompt + (pregunta, respuesta,
  criterios), armado por `juez.construir_kwargs`; verificación estructural
  de no-fuga antes de llamar (patrón `verificar_ceguera_requests`). Ids
  opacos: respuestas base `EV2R1-` + sha256(`juez-ev2-r1|id_pregunta|r1|
  sha256(respuesta)`)[:10]; re-corridas `EV2E1-` + sha256(`juez-ev2-r1-enc|
  id_pregunta|r1|rep|sha256(respuesta)`)[:10]. Orden del juez: sorted por
  (id_pregunta, sha256 respuesta[, rep]) → shuffle con semilla `juez-ev2-r1`
  (base) / `juez-ev2-r1-enc` (§7). Tablas de des-anonimización fuera de las
  salidas ciegas (`ev2_r1/desanonimizacion_SOLO_MESA/`).
- **Worksheet:** fichas `ADJ1-` + sha256(`worksheet-ev2-r1|id_pregunta|
  sha256(respuesta)`)[:8], orden `random.Random("worksheet-ev2-r1")`;
  muestra simétrica con semilla `adjudicacion-ev2-r1` (declarada por el
  mandato) sobre ids ordenados, generador nuevo por estrato. Selftest
  no-fuga obligatorio antes de entregar. Con un solo grafo, la ceguera de la
  ficha protege contra el sesgo por origen (base / re-corrida / estrato de
  muestra) y por veredicto del juez: nada de eso viaja a la ficha.
- **Freno por proyección** en cada etapa (agente y juez), tope por CLI;
  precios verificados el día de la corrida; gasto real desde las dbs.

## 5. Predicciones (calibradas por la evidencia sellada; formato de lectura §7)

Referencias selladas (fuente `atribucion_fallas.md` §1.a y §4,
`cruce_definitivo_por_grafo_SOLO_MESA.md` vía `reporte_ev2.md` §2):
KG-Reextraído (`8e2eadee`) = 30/40 anclas presentes en censo (10 no
resueltas: 8 granularidad, 2 contenedor); clase × trazas base
ausencia_kg 9 / alcanzabilidad 1 / vista_no_consultada 5 / generacion 21 /
correcto 4; tabla definitiva 4 correcto / 27 parcial / 9 incorrecto.

- **P1 (ausencia / censo) — LA del mecanismo de granularidad.** El censo de
  r1 registra MÁS anclas presentes que las 30/40 de KG-Reextraído: la cola
  flaggeada (+351 nodos) y el re-ensamblado deberían reducir las ausencias
  por granularidad. **Umbral propuesto: presentes(r1) ≥ 31/40** (es decir,
  no-resueltas ≤ 9, estrictamente menos que las 10 de KG-Reextraído bajo la
  misma regla). El número observado queda registrado por el censo de fase A,
  ANTES de correr el agente; el umbral queda sujeto a laudo de la autora en
  el freno de fase A. Clase causal que debería moverse: `ausencia_kg`.
- **P2 (granularidad de ancla) — LA predicción central.** El perfil de falla
  propio de KG-Reextraído en el mapa causal (`85d9fdb`) es la ausencia por
  granularidad: 8/9 de sus trazas base `ausencia_kg` tienen el contenido
  solo en sub-puntos (crudo=0, desc>0) y 4/9 de sus incorrectos definitivos
  son `ausencia_kg`. r1 ataca exactamente esa clase. Predicción: **baja** —
  operativamente, (a) trazas base de r1 con clase `ausencia_kg` < 9, con las
  de diagnóstico granularidad < 8; (b) incorrectos definitivos de r1 con
  clase `ausencia_kg` < 4.
- **P3 (generación) — control negativo.** La clase `generacion` es modal en
  KG-Reextraído (21/40 trazas base) y el grafo no toca la política del
  agente. Predicción: **NO cambia** — generacion(r1) dentro de 21 ± 3
  trazas base (la banda de ruido que el plan declara: diferencias de 1–3
  preguntas no son señal). Fuera de la banda en cualquier dirección =
  hallazgo a reportar.
- **P4 (navegación / alcanzabilidad) — predicción honesta ≈ 0.** Las 5.645
  aristas `referencia` y el esqueleto E5 solo son alcanzables por
  `ver_vecinos`, y H17 dice que el agente no explota estructura nueva bajo
  el retriever booleano. Predicción: **efecto ≈ 0** — techo de retrieval de
  r1 (alcanzabilidad + vista_no_consultada, trazas base) dentro de 6 ± 3
  (KG-Reextraído: 1 + 5 = 6). Si baja de 3 con las mismas preguntas, es
  evidencia de uso espontáneo de estructura (hallazgo CONTRA H17, a
  reportar con las trazas que lo muestren).
- **P5 (agregado).** Incorrectos definitivos de r1 ≤ 9 (los de
  KG-Reextraído). La dirección del cambio en correctos/parciales se reporta
  con su tamaño y la nota de multiplicidad del plan (diferencias de 1–3
  preguntas no son señal; sin lectura de superioridad sobre esa base).

## 6. Costos (estimación previa obligatoria; tope propuesto USD 6)

Referencias de la corrida base (todas leídas de archivos sellados por
`ev2_r1/code/estimacion_r1.py`, que genera la tabla reproducible en
`ev2_r1/estimacion/estimacion_fase_b_r1.{json,md}`): agente por traza de
fidelidad de KG-Reextraído 0,03513 USD (40 trazas, total 1,4053 — la
referencia «agente ~USD 1,4/grafo» del mandato); juez base 4,3405 / 360
llamadas = 0,01206; §7 agente 6,4732 / 198 = 0,03269; §7 juez 6,7441 / 594
nominales = 0,01135. Margen de tamaño de r1 declarado: 1,0–1,2× sobre las
etapas de agente (r1 tiene +55,7 % de aristas que el sellado: outputs de
`ver_vecinos` más grandes). Desglose central para r1 (40 preguntas;
escenario parciales = 23, los de KG-Reextraído; auditoría 1 par):

| Etapa | Volumen | USD estimado (margen 1,0–1,2) |
|---|---|---|
| Agente base N=1 | 40 trazas | 1,41–1,69 |
| Juez base N=3 | 120 llamadas | 1,45 |
| §7 agente N=3 | 24 pares × 3 | 2,35–2,82 |
| §7 juez N=3 | 24 pares × 9 | 2,45 |
| Worksheet + atribución | offline | 0 |

El total central con 23 parciales es **USD 7,66–8,41: supera el tope
propuesto de USD 6**; el tope entra solo con parciales ≤ 14 (margen 1,0) /
≤ 12 (margen 1,2). La resolución del tope (mantener 6 con freno por
proyección y riesgo de detención a mitad del §7, subirlo, o autorizar por
etapas: agente base + juez base ≈ 2,85–3,13 y el §7 con tope propio una vez
conocidos los parciales) es laudo de la autora en el freno de fase A. Freno
por proyección activo en toda etapa; si frena, se reporta antes de continuar.

## 7. Lectura P1–P5 (formato fijo, sellado acá)

Al cierre (tras la adjudicación), la lectura de predicciones se entrega como
UNA tabla con exactamente una fila por predicción y las columnas:
`predicción | número predicho (umbral/banda) | número observado | veredicto`,
con veredicto ∈ {cumplida, no cumplida, no evaluable} — SIN narrativa
interpretativa (la interpretación es de los laudos de la autora). La tabla
final de r1 (correcto/parcial/incorrecto) se presenta AL LADO de las tres
filas selladas de EV2, citadas de `reporte_ev2.md` §2 sin re-medirlas.

## 8. Qué NO decide este pre-registro

La promoción de r1 a vigente y la elección del brazo KG de A2.1 son laudos de
la autora, fuera de esta unidad. Ningún resultado de esta corrida se usa para
corregir r1 (principio 9): los defectos que aparezcan se anotan como insumo
de la release r2.
