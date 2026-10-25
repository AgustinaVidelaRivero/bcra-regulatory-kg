# Pre-registro de A2.2: el grafo contra el sistema por fragmentos, sobre EV2 — BORRADOR

**BORRADOR, sin firmar.** Lo escribe la ejecutora del tramo 3 de A2.1 (mandato `docs/mandatos/A2_1_sistema_por_fragmentos_preregistro_A2_2.md`,
texto firmado en `c2b6cb60`, §5, `:128-154`, y §6, `:165`; A-D0, (a): registro, §99, decisión 2, `:3850`). Lo firma la autora y se sella
con su commit (A2.1, `:130`). Hasta la firma no rige nada de lo que dice, y nada de A2.2 corre.

- **Las fuentes,** leídas en HEAD `af4dab8e` (24/10/2026): «A2.1» (el mandato de arriba), «registro»
  (`docs/registro_decisiones_calidad_y_evaluacion_2026-10-15.md`), «U-NAV» (`docs/mandatos/UNAV_DISENO_navegacion_agente.md`), «Q8»
  (`docs/mandatos/Q8_juez_de_B63_y_su_verificacion.md`), «plan» (`docs/plan_tesis.md`), «protocolo de EV2» (`docs/protocolo_corrida_ev2.md`)
  y «método de EV2» (`docs/preregistro_evaluacion_fidelidad_ev2.md`). «FRENO A2.1-a» y «FRENO A2.1-b» son
  `data/experiment/banco_mcp/a2_1/FRENO_A2_1_a.md` y `FRENO_A2_1_b.md` (el segundo, en `7a9fe8ca`, sha256 `0d2d919d…`). Las rutas que
  empiezan con `a2_1/`, `agentes/`, `mcp_kg/`, `mcp_vector/` o `smoke/` cuelgan de `data/experiment/banco_mcp/`.
- **El insumo de la mesa** (v2, 23/10/2026, sha256 `d786544e…`, fuera del repo; registro, §99, `:3893`) da el orden de este borrador y
  sus anclas. La nota de la mesa sobre R5 y el tope (sha256 `01214f04…`, fuera del repo; registro, §106, `:4209-4217`) da las opciones de
  R5 y la cuenta del tope.
- **Marcas:** [DECIDE LA AUTORA], lo que ninguna fuente fija, con sus opciones; PENDIENTE, lo que falta hacer antes de correr; NO
  VERIFICADO, lo que no controlé contra una fuente del repo. La lista de las [DECIDE LA AUTORA] está en el §9.

## 1. Lo que dio el tramo 2 de A2.1 (los huecos A-1 a A-5)

| hueco | lo que dio | de dónde |
|---|---|---|
| A-1, la versión del CLI | 2.1.241, la sellada (`a2_1/config_agentes_a2_1.json:8`), en las sesiones pagas del smoke y de H-B2 | FRENO A2.1-b, §0 (`:29`) y §3 (`:100`); para H-B2, el campo `claude_code_version` de `a2_1/hb2/analisis_tramo2_A2_1.json` |
| A-1, el brazo del grafo de la fase B | no se re-validó: A2.1 lo pide solo si cambió el CLI (`:121-124`), y no cambió. El FRENO A2.1-b no lo dice con esas palabras: sale de su §3 (`:100`) | A2.1, `:121-124` |
| A-2, la señal de H-B2 | `--max-turns k` acota los mensajes del asistente (R-b CARACTERIZADO, en las dos lecturas): una sesión se corta si y solo si su mensaje número k pide tools; el CLI ejecuta esas tools y termina con `error_max_turns`, sin JSON final (R-c). `num_turns` = `tool_use` + mensajes del asistente sin `tool_use`, observada después de correr (R-a NO VERIFICADO con las candidatas declaradas). Las llamadas del log R1 coinciden con los `tool_use` | FRENO A2.1-b, §4 (`:122-140`), §5 (`:144-155`) y §6 (`:159-161`); registro, §106, `:4197` |
| A-3, el costo por sesión | R9 por sesión, con los tokens reales, igual al del CLI | FRENO A2.1-b, §3 (`:78-93`), §4 (`:108-117`) y §8 (`:191-199`); registro, §106, `:4194` |
| A-4, el lanzador y lo que corrió | `agentes/lanzar_agente.py`, `2f00742038324a8e01122d574981f50a4c23a3927f88aad6b1fe7c4cc8e3e0c5`, y `a2_1/lanzar_agente_a2_1.py`, `9553c6ef8d17ca045b06f28ac29ffaf5d48a0d322b416ddf662efaf1aed7cba2`; la configuración de los agentes, `a2_1/config_agentes_a2_1.json` (`2f6b60e2…`); el runner, `a2_1/correr_a2_1.py` del commit `6c6dcad9`. El venv del servidor de fragmentos, `~/INGENIERIA IA/TESIS/venvs/banco_vector_py312`, con `requirements_vector.txt` (`50a7da51…`) y su `pip freeze --all` (63 líneas), sha256 `24f4c0644699e4ffcd952a27ea572d6ccbae88e63382e5b1441fdae0479fb4cb` | FRENO A2.1-b, §0 (`:29-30`) y §1 (`:39-41`); los dos archivos del lanzador y la configuración, en `harness_R10` de cada meta de `smoke/resultados/a2_1/` y `a2_1/hb2/`; el venv, FRENO A2.1-a, §3 (`:167-176`), y registro, §49, `:1686` |
| A-5, el control del disco y el valor remoto | ningún freno del control del disco; el mayor resultado, lejos del tope anotado de 200.000 caracteres; `tengu_velvet_ibis` presente y vacía en cada sesión, sin ninguna tool del banco con número | FRENO A2.1-b, §2 (`:70-71`) y §7 (`:183-185`); registro, §106, `:4196` |

## 2. Los brazos

- **El grafo,** por D-A (A2.1, `:191-192`): el de desarrollo re-sellado, `KG_Tanda0_Desarrollo_r2b_rs1`,
  `acb26dca0885e9ea83ab02637f15c1dac57885f0cf017c5fb16173ac7dfcac31` (nota del 15/10/2026 al pie de A2.1, `:253`). Está sellado:
  `commit_sellado` `4fe6ece` en `data/experiment/neo4j/grafos.py:188-193`, y el `kg.json` de HEAD
  (`data/experiment/reextraccion_v2/corpus_tanda0/ens_desarrollo_r2b_rs1/r2/kg.json`) da ese sha256. Por eso no va el sellado anterior
  (`6e756043…`; A2.1, `:132`). Su configuración: `mcp_kg/config_mcp_kg_a2_desarrollo_r2b_rs1.json` (`d80084b6…`; `:5` y `:7`).
  - **Precondición declarada** (PENDIENTE): la carga en Neo4j y el test positivo del brazo del grafo van al principio de A2.2 (A2.1,
    `:80-81`).
  - El comentario «r2b no se evalúa con EV2» de `grafos.py` es anterior a D5, que fija el grafo de desarrollo r2b como brazo del grafo de
    A2; se declara y `grafos.py` no se edita (A2.1, `:82-83`).
  - El servidor es `mcp_kg/servidor_mcp_kg.py`, con las tres herramientas del harness congelado (`buscar_nodos`, `ver_nodo` y
    `ver_vecinos`; `:70`). A2.2 no usa `ver_punto` (registro, §61, `:2138-2140`) ni `desde` en ningún brazo (registro, §50, `:1738-1739`, y
    §54, `:1875`).
- **Fragmentos BM25:** `mcp_vector/config_fragmentos_bm25_r2b.json` (`f76a0a51…`), índice `6b5da8b0…`, con el analizador `spanish` de
  Lucene 9.11.1 replicado y k1 1,2 y b 0,75 (`:5-10`).
  - Las diferencias con el analizador del grafo (A2.1, `:66-68`) están en el FRENO A2.1-a, §4 (`:189-246`). Las seis decisiones que su §14
    dejó abiertas quedaron como estaban (registro, §16, `:526-535`): el servidor se llama `fragmentos` en los dos brazos; la
    descripción de la tool nombra la medida; `limite` dice «(def. 5, máx. 5)»; la consulta pasa por el mismo analizador que los
    documentos; la norma de largo está cuantizada como en Lucene; y el stream de init del aislamiento queda fuera del repo.
  - **La asimetría de la consulta, declarada con sus cifras** (registro, §16, `:527-528` y `:536-539`): el brazo del grafo pre-tokeniza la
    consulta antes de Lucene (minúsculas, sin acentos, `[a-z0-9]+`; FRENO A2.1-a, `:225-233`) y el BM25 de fragmentos no. Con esa
    pre-tokenización, 1.846 de los 8.378 términos del índice no saldrían de ninguna consulta (111 con caracteres fuera de ASCII y 1.735
    números con separador), y 1.763 de los 1.768 pasajes tienen al menos uno
    (`data/experiment/controles_a2_2/consulta_pre_tokenizada_bm25_mesa.json`, campos `vocabulario`, `terminos_inalcanzables`,
    `de_ellos_con_caracteres_no_ascii`, `de_ellos_ascii_con_separadores` y `pasajes_con_algun_termino_inalcanzable`).
- **Fragmentos densos:** `mcp_vector/config_fragmentos_denso_r2b.json` (`fe2daf70…`), matriz `828caeff…`, `harrier-oss-v1-0.6b` (`:5-7`).
- **Las dos configuraciones** son principales (plan, `:339`, registro del 07/10/2026, D1). Corren sobre los 1.768 pasajes de la E0 r2b de
  desarrollo, en composición propio más herencia (A2.1, `:70`; `config_fragmentos_bm25_r2b.json:10` y `config_fragmentos_denso_r2b.json:16`),
  con top-k = 5 acotado por el servidor (D-D; A2.1, `:195`).
  - El despacho de A2.2 controla al empezar los sha256 de los índices de `mcp_vector/indice/` (registro, §16, `:545`). Su respaldo está en
    `fuera_del_repo/indices_banco/fragmentos_e0_r2b_desarrollo_A2_1/` (registro, §51, `:1799-1801`).
- **El híbrido de B1.9,** fuera de A2.2 (D-B; A2.1, `:193`).

## 3. Lo común a los brazos

- **El agente:** `claude-sonnet-5`, `--bare`, el CLI sellado 2.1.241 (`a2_1/config_agentes_a2_1.json:8-10`). El tramo 2 corrió con esa
  versión (A-1).
- **El prompt:** la plantilla sin el paréntesis de los cinco TOs de desarrollo, la misma para todos los brazos, entra antes de A2.2 en lo
  común de este pre-registro (U-NAV, §5, `:202-209`; registro, §29, `:1080-1081`). El diff entre brazos es solo el de `{{BLOQUE_TOOLS}}`
  (U-NAV, `:196-198`). El sha256 de la configuración sellada del banco (R10) cambia, y se declara (U-NAV, `:211`). A2.2 corre sin la
  parte común de la estrategia, que entra desde N6 (U-NAV, `:213-217`).
  - **Lo que encontré:** la plantilla de HEAD (`agentes/plantilla_prompt.txt:1`, sin cambios desde `1fa79de3`) todavía nombra los cinco
    TOs, y con ella corrieron las sesiones pagas del tramo 2: los `prompt_*.txt` de `smoke/resultados/a2_1/` y de `a2_1/hb2/` traen el
    paréntesis y «Tope de 10 llamadas». U-NAV decía que el tramo 2 validaba la plantilla nueva (`:210`) y que el cambio del texto iba en
    su despacho (`:212`). Así que la plantilla de A2.2 no está en el repo ni la validó ninguna sesión. **[DECIDE LA AUTORA] A-D5** (§9).
- **El contrato R4 y la vía de credenciales:** la vía `api`, con el envoltorio de A2.1, §4 (`:103-114`), y top-k = 5.
- **R5, el criterio de corte** (registro, §50, punto 4, `:1750-1751`), tal cual: «30 llamadas en el prompt, `--max-turns` 32 y
  `--max-budget-usd` 1,80, iguales en los dos brazos, en A2.2, N6 y B6.3. Si H-B2 caracteriza otra cuenta, `--max-turns` queda en tope + 2
  de esa cuenta, declarado antes de la firma de A2.2». El mismo tope en los dos brazos ya estaba decidido (registro, §49, `:1712-1713`).
  - **Lo que da la regla con la señal de H-B2** (A-2; registro, §106, `:4210-4211`): `--max-turns` 32, sin cambio, contado en mensajes del
    asistente (30 + 2). Se declara que **`--max-turns` no acota las llamadas:** con llamadas en paralelo, un mensaje pide más de una tool
    (hasta 4 en los brazos de fragmentos en A2.1; FRENO A2.1-b, §5, `:148-150`), así que 32 mensajes pueden traer más de 30 llamadas. El
    tope de 30 queda en el prompt y en el presupuesto de 1,80 por sesión. **«Al tope» se cuenta en llamadas, con el log R1** (que coincide
    con los `tool_use`; A-2).
  - **[DECIDE LA AUTORA] R5** (registro, §106, `:4212-4214`; las opciones de la nota de la mesa, §2):
    - **(1) R5 como está, con la señal declarada.** Por traza se registran los mensajes del asistente, los `tool_use`, las llamadas del log
      R1 y `num_turns`. «Al tope» es una sesión con 30 llamadas o más en el log R1; esas sesiones se informan por brazo, con su fracción y
      su intervalo de Wilson, y entran en la regla de N6 (registro, §50, punto 5, `:1752-1753`). Una traza cortada (`error_max_turns` o
      el presupuesto) queda incompleta por R3, sale de la métrica y se declara, con la sensibilidad que la cuenta como no cumplida (§50,
      punto 6, `:1754-1756`).
      Implica: ningún código nuevo y nada distinto de lo que la autora ya fijó; el tope de 30 llamadas no queda garantizado. Es la que
      recomienda la mesa.
    - **(2) Lo de (1), con un tope duro de 30 llamadas en los servidores:** el servidor rechaza la llamada 31 de la sesión, contada por su
      log, igual en todos los brazos. Implica: el tope queda garantizado, pero es código nuevo en los dos servidores, con su prueba y su
      revisión antes de A2.2, y cambia lo que ve el agente en la llamada 31.
    - **(3) Lo de (1), y excluir de la métrica las sesiones con más de 30 llamadas.** Implica: un filtro que recorta distinto a cada brazo,
      porque el brazo del grafo hace más llamadas (FRENO A2.1-b, §6, `:175-178`). La mesa no la recomienda.
    - La propuesta (a) del FRENO A2.1-b (§6, `:163-166`), `--max-turns` 12, viene de la configuración de la fase B y contradice R5: solo
      vale si la autora cambia R5. La (d), un tope sobre `num_turns`, el CLI no la aplica.
  - **La configuración de A2.2** lleva los valores de R5 en lugar de los de la base que usó el tramo 2 (10 llamadas en el prompt,
    `--max-turns` 12 y `--max-budget-usd` 0,30: `a2_1/config_agentes_a2_1.json`, `corte_R5`, y `smoke/resultados/a2_1/comando_*.json`).
    PENDIENTE, con la plantilla (A-D5).
- **La salida de las herramientas:**
  - el insumo cita la D-6 de la §72 (`:2555-2557`): `MAX_MCP_OUTPUT_TOKENS` en 70.000 en los dos brazos y el control por código de los
    resultados que llegan como referencia a un archivo, que tiene que dar 0. Lo que vino después: la anotación
    `anthropic/maxResultSizeChars` en 200.000 caracteres en todas las herramientas de los dos servidores, con la variable en 70.000
    (registro, §79, `:2824-2828`); los dos servidores la declaran (`mcp_kg/servidor_mcp_kg.py:68` y `mcp_vector/servidor_mcp_vector.py:74`;
    registro, §94, `:3617-3620`); con la anotación, un resultado va a disco solo si pasa los 200.000 caracteres, y ni la variable ni el
    presupuesto por mensaje actúan (registro, §96, `:3688-3690`). El despacho del tramo 2 dijo que la variable no se fija
    (`a2_1/config_agentes_a2_1.json:57`), y ninguna sesión paga del tramo 2 la tuvo en su entorno (`entorno_de_la_sesion` de los
    `comando_*.json`). **[DECIDE LA AUTORA] A-D6** (§9);
  - el control del disco después de cada sesión: si un resultado llega como referencia a disco, la corrida frena sin lanzar otra, y se
    registra el largo de cada resultado en unidades UTF-16 (registro, §96, `:3697-3699`). En el tramo 2 no frenó (A-5).
- **El entorno de cada sesión** (A-4): se lanza desde la Terminal (registro, §82, `:2933-2936`), con la lista cerrada de variables
  permitidas (§83, `:2972-2974`), una carpeta de configuración nueva y el cwd fuera de cualquier repo, con la ruta y el sha256 de cada
  archivo del lanzador en la meta (§84, `:3035-3046`), y la lectura acotada de `tengu_velvet_ibis` (§97, `:3761-3762`). El venv y el
  sha256 de su `pip freeze`, los de A-4 (§49, `:1686`).

## 4. EV2, la corrida y el juez

- **EV2:** sus 40 preguntas y 164 criterios (método de EV2, `:23-24`), por ruta y sha256, sin abrirlas (A2.1, `:34-36`):
  `data/experiment/exploracion/ev2_fidelidad/preguntas_ev2_fidelidad.json`,
  `1d58733699c325c90510e1ead5f18eac6c3cd970ee3b0ab7ff141da539162b40` (A2.1 da `1d587336…`; el sha256 completo lo tomé de HEAD con
  `shasum`, sin abrir el archivo).
- **La corrida:** N = 1 completa más N = 3 parciales, y la auditoría del 10 % con adjudicación simétrica, con el protocolo de EV2 (A2.1,
  `:139-140`; plan, `:340`). La regla de EV2 que elige las parciales, tal como está escrita:
  - N = 1 de las 40 preguntas en los tres brazos (protocolo de EV2, `:97-98`): 120 respuestas (Q8, `:61`);
  - re-corrida N = 3 «SI Y SOLO SI el veredicto de la corrida base es "parcial"», por brazo; agregación de las tres re-corridas por
    mayoría, y un empate triple resuelve a parcial (protocolo de EV2, `:104-108`). «La regla es idéntica para los tres grafos» (`:110`);
  - la auditoría simétrica: re-corrida N = 3 sobre el 10 % de los «correcto» de la corrida base de cada brazo (protocolo de EV2,
    `:115-122`);
  - las re-corridas se juzgan con el mismo método (método de EV2, `:90-94`).
  - **Lo que eso deja abierto:** cuántas preguntas van a N = 3 (P) no se sabe antes de correr: lo fijan los veredictos de N = 1. Por
    brazo, son las parciales más las auditadas, a lo sumo 40. El protocolo no fija cómo se redondea el 10 % (`:115-122`), ni si
    «re-corrida N = 3» son tres sesiones nuevas («las 3 re-corridas», `:106`) o dos más la base. Las dos cosas entran en el tope (§6).
  - **El orden de las corridas** (A-D1, decidida: registro, §99, decisión 14, `:3874`): el de B6.3 (registro, §89, `:3313-3314`), por
    pregunta y por repetición, con los brazos de cada pregunta seguidos en un orden sorteado, y la fecha de cada sesión registrada.
    **La semilla que propongo,** con la forma de la de B6.3 (`B63:orden_corridas:v1`; registro, §99, decisión 7, `:3856-3857`):
    `A22:orden_corridas:v1`, aplicada así:
    - el orden de las preguntas: `random.Random("A22:orden_corridas:v1").shuffle` sobre los 40 ids ordenados;
    - el orden de los brazos de cada pregunta en la repetición r: `random.Random(f"A22:orden_corridas:v1:{id}:r{r}").shuffle` sobre
      los nombres de los brazos ordenados;
    - las re-corridas van después de juzgar N = 1, por repetición y, dentro de cada una, en el orden de las preguntas de N = 1, con los
      brazos de esa pregunta que van a N = 3 seguidos.
- **El juez, congelado antes de la firma:** el de EV2 tal cual (nota al pie de A2.1, `:241-244`; Q8, decisión 1, `:36-37`; registro, §9,
  `:302`):
  - `data/experiment/ev2_juez/juez.py`, sha256 `b4a74ba536dd5938aa0935ee088e8327bbad411229679887177653a698421236` en HEAD (último commit
    que lo toca, `1a0ac5c6`);
  - su prompt v1, `data/experiment/ev2_juez/prompt_juez_v1.md`, sha256 `fd446f8e61f46033d7de9b862121c698b2c52dcc2696b7f10993f44e509f5455`
    (el `fd446f8e…` de la nota al pie). `juez.py:45-46` elige el prompt con `JUEZ_PROMPT_VERSION`, que da v1 si no se fija: A2.2 corre sin
    esa variable, y cada llamada registra el sha256 del prompt (`juez.py:143`);
  - N = 3 por par (respuesta, criterio), con veredicto modal (método de EV2, `:54`), y el veredicto por pregunta en código (`:35-41`);
  - `claude-sonnet-4-6` con temperatura 0, anthropic 0.100.0 y la API 2023-06-01, con el control del SDK
    (`scripts/control_sdk_anthropic_juez_y_banco.py`) como primer control del paso pago (registro, §93, `:3558-3567`);
  - el juez recibe la pregunta, la respuesta final del agente y los criterios con sus citas textuales, «Nada más» (método de EV2,
    `:24-28`): ni el brazo ni nada que lo identifique (`:47-48`);
  - A2.2 y B6.3 usan el mismo (A2.1, `:244`).
- **La muestra simétrica, que es también la mitad de verificación del gold** (registro, §9, `:295-297` y `:302-303`): 20 de las 120
  respuestas (7, 7 y 6 por brazo), estratificadas también por el veredicto del juez, con la semilla `gold-q12-verificacion-a22-v1` (Q8,
  `:61-63`). La autora las lee a ciegas, sin ver ningún veredicto (nota al pie de A2.1, `:245-246`). El material lo arma la mesa después
  de A2.2, sin veredictos ni brazo de origen (Q8, `:64-65`).
  - **El criterio de aceptación del juez:** Wilson inferior de al menos 0,85 por criterio y al menos 18 de 20 por respuesta (A2.1,
    `:247-248`).
  - **Si no se cumple,** rige la decisión ya tomada por la autora, la 3 de Q8 (`:77`; registro, §99, decisión 16, `:3878-3879`), tal cual:
    «si la verificación no pasa, B6.3 se juzga con el juez, la cifra se informa con su acuerdo medido y todo lo dudoso va a mi lectura».
  - **La columna «error fuera de los criterios (sí o no, y cuál)»** va en esas 20, a ciegas al brazo (registro, §28, `:1011-1012`).
- **Lo que el protocolo de EV2 no fija para A2.2:** las semillas que nombra para sí (la auditoría, `auditoria-ev2-v1`, `:118-119`; el
  orden del juez, `juez-ev2-v1`, método de EV2, `:49`) y qué pasa con una pregunta `requiere_adjudicacion` (método de EV2, `:39-41` y
  `:81`) frente al disparo de N = 3. **[DECIDE LA AUTORA] A-D7 y A-D8** (§9).

## 5. El análisis

- **La cifra principal,** sobre todas las preguntas, y aparte la cifra sin las que caen en unidades de la cola (D5; A2.1, `:142`). La
  lista de ids de la cola es la sellada con el grafo (plan, `:339`): no la ubiqué en HEAD, y su ruta y su sha256 van acá antes de la firma
  (PENDIENTE).
- **Las dos comparaciones:** el grafo contra fragmentos BM25 y el grafo contra fragmentos densos, cada una con Holm (A2.1, `:145`). «El
  grafo supera a los fragmentos» solo si supera a las dos configuraciones (plan, `:339`); si supera a una sola, se informa por
  configuración, sin la afirmación general (la misma regla que la autora pidió para B6.3: registro, §99, decisión 11, `:3866-3868`).
  - **La medida y la prueba** no las fija ninguna fuente que haya leído. **[DECIDE LA AUTORA] A-D9** (§9).
- **Las tasas de pares discordantes** de cada comparación, que van a la regla del N de B6.3 (Q5; registro, §5, `:173-179`; el N, §94,
  `:3625-3627`, y §99, decisiones 4 y 5, `:3853-3854`), y `c_agente` (Q6), el costo del agente por pregunta y por brazo que la válvula de
  costo de B6.3 compara con su estimación (plan, `:778`) (A2.1, `:146`). La regla del N las toma con `regla_del_N_B63_s94_mesa.py`, del
  paquete de la mesa, que no leí (NO VERIFICADO).
- **La no comparabilidad con la tabla de EV2** (principio 8), declarada (A2.1, `:147`; plan, `:339`): A2.2 corre con el agente del banco y
  no con el harness congelado de EV2, con otro grafo y con otro prompt.
- **Las predicciones** de `:339` (A2.1, `:143-144`), con su sentido esperado, escritas antes de la firma. Son predicciones, no hipótesis
  con prueba: la única prueba es la de las dos comparaciones.
  1. **Criterios cubiertos:** cada configuración de fragmentos cubre al menos tantos criterios como el grafo, y BM25 al menos tantos como
     el denso. Razón: los fragmentos le devuelven al agente el texto fuente entero, con su vocabulario y sus condiciones; el grafo, el label
     y la descripción del nodo (plan, `:339`, punto (a)); y BM25 es el rival más fuerte en lo literal (plan, `:339`, D1).
  2. **Incorrectos:** el grafo tiene al menos tantas preguntas con veredicto «incorrecto» como cada configuración de fragmentos, por la
     misma razón.
  3. **Abstenciones** (la clasificación auxiliar del juez, método de EV2, `:29-31`): el grafo se abstiene al menos tanto como cada
     configuración de fragmentos: con la representación comprimida, el agente encuentra menos veces la evidencia literal.
  4. **Latencia por pregunta:** mayor en el grafo que en cada configuración de fragmentos, porque hace más rondas de tools (en la fase B,
     hasta 13 `tool_use` en 9 mensajes en una sesión del grafo, FRENO A2.1-b, §5, `:144-145`; en A2.1, a lo sumo 4 llamadas en una
     sesión de fragmentos, en las tablas de su §3, `:78-91`, y de su §4, `:108-117`).
  5. **Costo por pregunta (`c_agente`):** mayor en el grafo que en cada configuración de fragmentos, por las mismas rondas.
  6. **La asimetría entre el texto crudo y la representación comprimida:** la ventaja de los fragmentos, si aparece, se concentra en los
     criterios cuya cita es literal del texto fuente; la del grafo, si aparece, en las preguntas que piden seguir una remisión o una
     relación entre unidades. Cómo se separan esas preguntas no se decide acá: es del diagnóstico posterior (§6).

## 6. El tope, cuándo corre y lo que no se decide

- **El tope:** unos USD 15 en el plan (`:340`); en EV2, la corrida del agente costó 14,88 (A2.1, `:148-149`, que cita
  `ev2_reporte/reporte_ev2.md:388-390` y `:403`; no abrí ese reporte, que trae los resultados de EV2).
- **[DECIDE LA AUTORA] A-D2 — el tope** (registro, §99, decisión 17, `:3880`, y §106, `:4215-4217`). La cuenta de la mesa (nota, §3):
  - el costo por sesión de fragmentos es el R9 de las 8 sesiones de pregunta del smoke (FRENO A2.1-b, §3, `:82-89`): BM25, media 0,0340 y
    máximo 0,0399; denso, media 0,0329 y máximo 0,0450;
  - el del grafo sale del modelo de costo de la §181 de la mesa, que el tramo 2 no midió y que no está en el repo: 0,0640 central, 0,1424
    medio y 0,2028 alto (NO VERIFICADO). El alto de fragmentos es el mayor entre su máximo y el alto de la §181, 0,1086 (NO VERIFICADO);
  - el juez, 3 llamadas de USD 0,0126 por respuesta (U-NAV, `:243`);
  - una pregunta en una corrida, con los tres brazos y su juez, cuesta 0,2443 central, 0,3407 medio o 0,5334 alto, y A2.2 cuesta
    (40 + 2P) veces eso, con P las preguntas que van a N = 3.

  | P | sesiones | central | medio | alto |
  |---:|---:|---:|---:|---:|
  | 0 | 120 | 9,77 | 13,63 | 21,33 |
  | 10 | 180 | 14,66 | 20,44 | 32,00 |
  | 20 | 240 | 19,55 | 27,26 | 42,67 |
  | 40 | 360 | 29,32 | 40,88 | 64,00 |

  - **La recomendación de la mesa:** el medio del P de este borrador, redondeado al dólar de arriba, con freno en el 75 %, como el tope de
    N6. Por ejemplo, con P = 10: tope 21 y freno 15,75.
  - **El freno del banco es un corte duro:** antes de cada sesión, el acumulado R9 más el presupuesto de la sesión no puede pasarlo
    (`a2_1/correr_a2_1.py:214-215`). Con el freno en el 75 % del medio, si el gasto real se acerca al medio la corrida frena antes de
    terminar, y decide la autora. Cuánto suma el presupuesto de cada sesión en el runner de A2.2 se fija con él (§8).
  - **Lo que agrega la regla de EV2** (§4): P no se conoce antes de correr; cuenta las parciales y las auditadas, a lo sumo 40 por brazo;
    y la cuenta con un solo P vale como cota si P es el mayor de los tres brazos. Con la lectura de tres sesiones nuevas por re-corrida
    (`:106`), la cuenta pasa a (40 + 3P): con P = 40, 480 sesiones y 39,09, 54,51 o 85,34.
  - **Las opciones:**
    - **(a) el tope para P = 40,** la cota de la regla: medio 40,88, tope 41 y freno 30,75; con tres re-corridas, medio 54,51, tope 55 y
      freno 41,25. Implica: cualquier P real entra en el tope en el escenario medio, aunque el freno puede cortar antes (lo de arriba);
      es el tope más alto;
    - **(b) el tope para un P menor que fija la autora** (por ejemplo, P = 10: tope 21 y freno 15,75), con el freno por proyección del
      protocolo de EV2 (`:143-148`): si con los P reales la proyección pasa el tope, la corrida frena antes de las re-corridas y decide la
      autora. Implica: las re-corridas pueden quedar sin hacer y A2.2, incompleta;
    - **(c) dos topes:** al firmar, el de N = 1 (P = 0: medio 13,63, tope 14 y freno 10,50); después de juzgar N = 1, el de las re-corridas,
      con los P reales y la misma regla, sin leer ninguna respuesta. Implica: el segundo tope se fija con un conteo de A2.2 a la vista
      (cuántas parciales), declarado; la regla de N = 3 es mecánica y no cambia con él.
    - Y la lectura de «re-corrida N = 3»: dos sesiones más la base, como la cuenta de la mesa, o tres sesiones nuevas, como dice `:106`.
- **Cuándo corre:** apenas se selle este pre-registro, en el carril pago, de a uno y nunca al lado de una extracción (registro, §26,
  `:919-923`). La condición de no correr junto a la tanda 1 (A2.1, `:150-151`) ya no aplica: la tanda 1 se selló (registro, §90, `:3386`).
- **Lo que no se decide acá:** el diagnóstico posterior a A2.2 (A2.1, `:152`; plan, `:341`).
  - **El diagnóstico y el grafo evaluado** (A-D3, decidida: registro, §99, decisión 15, `:3875-3877`). El punto de `:341` dice que lo
    corregible se corrige «antes de sellar el grafo evaluado y el pre-registro de B6.3», y con la prioridad del viernes (registro, §91,
    `:3441-3442`) el grafo evaluado se sella antes de A2.2. Por eso:
    - lo que el diagnóstico atribuya al agente o a la búsqueda de entrada entra solo si pasa su medición en N6, con N3 (U-NAV, §7, regla
      1, `:282`: el ajuste se hace solo con N3, nunca con EV2), y A2.2 no se vuelve a correr (U-NAV, §7, regla 2, `:283`);
    - lo que atribuya al contenido del grafo o a la segmentación va al grafo corregido o a una release posterior, declarado en los dos
      pre-registros.

## 7. Las sesiones de A2.2 en el repo

- Las transcripciones (`sesion_*.jsonl`) y los streams (`stream_*.jsonl`) son salida literal del CLI y traen el cwd absoluto, bajo la
  carpeta personal (`a2_1/enmascarar_cwd_a2_1.py`, docstring). Las del tramo 2 van enmascaradas en el repo (registro, §106,
  `:4198-4203`); las de las 24 sesiones pagas de la fase B (registro, §84, `:3041-3043`) siguen tal cual, entre los archivos del repo con
  el nombre de la cuenta (§106, `:4204-4206`). El README del banco dice que los streams no se editan
  (`banco_mcp/README.md:215-219`; su cambio, PENDIENTE de la autora: registro, §106, `:4207-4208`).
- **[DECIDE LA AUTORA] A-D4 — las sesiones de A2.2 en el repo:**
  - **(a) enmascaradas como las del tramo 2:** la carpeta personal reemplazada por `$HOME`, sin ningún otro cambio de bytes; los
    originales fuera del repo; el sha256 de cada original y de su versión enmascarada, en un JSON del repo. Con `a2_1/enmascarar_cwd_a2_1.py`
    adaptado a las carpetas de A2.2 (sus `CARPETAS` y su carpeta de originales). Implica: código nuevo chico, con su prueba sobre una copia;
    el repo no suma archivos con el nombre de la cuenta; los originales quedan fuera del repo y dependen de su respaldo;
  - **(b) tal cual, declaradas como las de la fase B.** Implica: ningún código nuevo, y el nombre de la cuenta entra al repo en cada
    transcripción y cada stream de A2.2.

## 8. Lo que falta antes de correr (PENDIENTE)

1. La plantilla nueva y la configuración de A2.2 (R10) con los valores de R5, con su sha256 nuevo declarado (§3; A-D5).
2. El runner de A2.2, con los tres brazos, el orden de §4, las re-corridas por la regla de EV2, el control del disco y la lectura del valor
   remoto en cada sesión, y su corrida en seco por el mismo camino de imports que la corrida real.
3. La carga en Neo4j y el test positivo del brazo del grafo (A2.1, `:80-81`).
4. El control de los sha256 de los índices al empezar (registro, §16, `:545`) y el del SDK antes del juez (§93, `:3564-3567`).
5. La lista de la cola sellada con el grafo, con su ruta y su sha256 (§5).
6. Lo que la autora pidió a la mesa antes de firmar este pre-registro (registro, §51, `:1802-1804`): qué más mejora la evaluación sin usar
   B6.3 para ajustar, y la confirmación de la vía de cobertura de la etapa V. La §52 trata los dos temas (`:1808`); no controlé si cierran
   el pedido.

## 9. Las decisiones de la autora

**Decididas** (registro, §99): A-D0, (a) (decisión 2, `:3850`); A-D1, el orden de B6.3 (decisión 14, `:3874`; §4); A-D3, el diagnóstico
y el grafo evaluado, con el agregado de la autora (decisión 15, `:3875-3877`; §6); si la verificación del juez no pasa, la decisión 3 de
Q8 (decisión 16, `:3878-3879`; §4).

**[DECIDE LA AUTORA], al firmar:**

| decisión | opciones, en corto |
|---|---|
| R5 (§3) | (1) R5 como está, con «al tope» en llamadas del log R1, informado por brazo (la recomienda la mesa); (2) lo mismo con un tope duro de 30 llamadas en los servidores, código nuevo; (3) lo mismo, excluyendo las sesiones de más de 30 llamadas. `--max-turns` 12 solo si cambia R5 |
| A-D2, el tope (§6) | (a) para P = 40: 41 con freno 30,75 (55 y 41,25 con tres re-corridas); (b) para un P menor, con freno por proyección antes de las re-corridas; (c) dos topes, el de N = 1 (14 y 10,50) al firmar y el de las re-corridas después de N = 1. Y la lectura de «re-corrida N = 3»: dos más la base o tres nuevas |
| A-D4, las sesiones en el repo (§7) | (a) enmascaradas como las del tramo 2, con el script adaptado; (b) tal cual, como las de la fase B |
| A-D5, la plantilla nueva (§3) | (a) una unidad USD 0 antes de A2.2 que la escriba junto con la configuración de R5, más una sesión corta paga por brazo, con tope de la autora, que la valide; (b) que la validen las primeras sesiones de A2.2 (una de prueba por brazo, sin pregunta de EV2), con freno si fallan R3 o R6; (c) A2.2 con la plantilla de HEAD, declarado como desvío de U-NAV, §5 |
| A-D6, `MAX_MCP_OUTPUT_TOKENS` (§3) | (a) sin fijar, como en el tramo 2, con la anotación de 200.000 caracteres como tope y declarado frente a la §72 y la §79; (b) en 70.000, como dicen la §72 y la §79: según la §96 no actúa con la anotación, y A2.2 corre con una variable que el tramo 2 no tuvo |
| A-D7, las semillas (§4) | el orden de las corridas: `A22:orden_corridas:v1`, aplicada como en el §4, u otra; la auditoría y el orden del juez: (a) las de EV2 tal cual (`auditoria-ev2-v1` y `juez-ev2-v1`); (b) propias con la forma de B6.3 (`A22:auditoria:v1` y `A22:orden_juez:v1`) |
| A-D8, `requiere_adjudicacion` y N = 3 (§4) | (a) la autora las adjudica entre N = 1 y las re-corridas, y una adjudicada «parcial» va a N = 3; (b) el disparo usa solo el veredicto del código, y las `requiere_adjudicacion` se adjudican al final, sin re-corrida, declarado |
| A-D9, la medida y la prueba (§5) | (a) las del pre-registro de B6.3, para que las tasas de Q5 salgan de la misma medida; (b) fijarlas acá: el veredicto por pregunta en dos clases (correcto contra no correcto) y la prueba exacta de McNemar sobre los pares discordantes, unilateral a favor del grafo, con Holm sobre las dos |
