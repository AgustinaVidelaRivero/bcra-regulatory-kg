# Mandato de A2.1: el sistema por fragmentos en el banco y el pre-registro de A2.2 (versión para firmar, 15/10/2026)

Versión para firmar, de la mesa (hoja de ruta, §105 y §106), con las decisiones de la autora del 15/10/2026 (§8). Va en el
carril de la evaluación (enmienda 8, R6: se prepara sin mirar salidas del grafo) y no demora nada del camino a la tanda 1.

## 0. Para qué

- **A2.1** es el pre-registro sellado del sistema por fragmentos (`docs/plan_tesis.md:339`). Lo necesitan:
  - **A2.2,** que mide sobre EV2, una sola vez, el grafo contra los fragmentos y da las tasas de pares discordantes para el N de B6.3 (Q5;
    `:340`; registro de decisiones del 15/10/2026, §5);
  - **B6.3 (f),** que reusa el mismo sistema por fragmentos (laudo 2 del 20/09/2026, D-h2).
- **El sistema por fragmentos** es uno solo, con dos configuraciones que difieren solo en la medida de afinidad (`:339`, laudo 2 y D1 del
  07/10/2026):
  - BM25 y denso (`harrier-oss-v1-0.6b`), las dos principales, con Holm sobre las dos comparaciones;
  - fragmentos de E0 con herencia, top-k = 5, el mismo agente del banco con una sola herramienta de recuperación.
- **Lo que falta hoy** (mesa, 15/10/2026):
  - el banco no tiene el BM25 de fragmentos: `data/experiment/banco_mcp/` tiene `mcp_kg/` y `mcp_vector/`, y el servidor vectorial es
    solo denso;
  - el índice denso está sobre los 1.763 pasajes de la E0 vieja (`banco_mcp/README.md`, §2). D5 pide reconstruirlo sobre la E0 r2b de
    desarrollo: 1.768 unidades (`reextraccion_v2/e0_chunking/salida_tanda0_r2b/chunks_{cap,cla,ext,pro,ric}.json`: 462, 143, 973, 101
    y 89);
  - H-B2 sin caracterizar: `--max-turns 12` no disparó con `num_turns = 14` (`banco_mcp/README.md`, «Fase B»). El criterio de corte R5
    tiene que fijarse sobre una señal verificada antes de sellar (Q1).

## 1. Qué rige

- **El plan:** A2.1 (`:339`), A2.2 (`:340`), la nota F-2 de A1.8 (`:331`), A2.0-banco (R1 a R10, H-B2) y los principios 7 y 8.
- **El checklist:** Q1, Q2 y Q6 (`docs/checklist_pre_escalado.md:198-203`), y el bloque de decisiones del 07/10/2026 (desde `:214`).
- **Los laudos:** `docs/laudo_gate_trazabilidad.md` (R1 a R7), la fase B del gate (R8 a R10) y `docs/decision_modelo_embeddings.md`,
  §7 y §8.
- **El banco tal como está:** `data/experiment/banco_mcp/README.md`. `gate/` está sellado: se importa, no se edita.
- **La enmienda 8**, firmada, y la regla de caída.
- **CLAUDE.md, entero.**
- **El principio 7, en concreto:** A2.1 se diseña y se ajusta con material propio. **No abrís EV2:**
  - `data/experiment/exploracion/ev2_fidelidad/preguntas_ev2_fidelidad.json` se cita solo por su ruta y su sha256 (`1d587336…`);
  - tampoco abrís sus trazas, sus salidas del juez ni la tabla de EV2.

## 2. Paso 0, antes de cualquier otra cosa

Corré estos comandos y pegá su salida al principio de tu FRENO, **con la carpeta personal reemplazada por `$HOME`**:

```
pwd
git log --format=%s -5
git status --porcelain -- data/experiment/banco_mcp
claude --version
ls data/experiment/banco_mcp
```

- `pwd` da la raíz del repo; `git status` no da nada en `banco_mcp/`.
- `claude --version`: la versión sellada es 2.1.241 (`banco_mcp/agentes/config_agentes.json`). Si es otra, lo declarás. El tramo 2
  re-valida el smoke con la versión nueva (README del banco, «Consecuencias de diseño para el plan»).
- Si algo más da otra cosa, frenás sin hacer nada y lo informás.

## 3. Tramo 1 (USD 0, sin API): el BM25 de fragmentos, el índice nuevo y el aislamiento

Todo sobre una copia del repo hecha con el `rsync` de la cláusula. Corrés los tests sobre la copia, y al final llevás al repo solo lo de
la §6, con los tests corridos de nuevo en el repo.

1. **La configuración BM25 del servidor de fragmentos.** Va dentro del servidor de fragmentos, como una segunda medida de afinidad
   (`:339`, Q2), no como un servidor aparte:
   - **sin Neo4j y sin el modelo:** en modo BM25 el servidor no importa `neo4j`, no carga `harrier` y no abre sockets (D3);
   - **la misma herramienta y el mismo contrato:** `buscar_pasajes(consulta, limite)`, con los mismos campos por pasaje, el mismo
     desempate (score desc, id asc);
   - **`limite` acotado a 5 por el servidor** (D-D), en las dos configuraciones de fragmentos, con su test: un pedido de más devuelve 5;
   - **el analizador,** lo más parecido al `spanish` de Lucene que usa el índice del grafo (`data/experiment/neo4j/README.md:96`):
     minúsculas, las palabras vacías de Lucene para el castellano y el stemmer liviano de Lucene. Cada pieza va con su fuente, y las
     diferencias que queden, en una sección del FRENO (Q2);
   - **los parámetros:** k1 = 1,2 y b = 0,75, los de Lucene, salvo que la doc de Neo4j diga otros para su índice: se cita;
   - **la composición del pasaje:** la misma del denso, propio más herencia, sobre las mismas 1.768 unidades.
2. **El índice denso sobre la E0 r2b de desarrollo** (D5):
   - `construir_indice.py` pasa a tomar un manifiesto de E0 y registra el sha nuevo;
   - con la E0 vieja tiene que dar el sha sellado `12d284d5…`, y si no da, frenás;
   - con la E0 r2b da un sha nuevo. Lo construís dos veces y las dos matrices tienen que coincidir byte a byte;
   - **sin descargas:** el modelo tiene que estar en la caché local con la revisión pinneada. Si no está, frenás.
3. **La configuración del brazo del grafo para A2** (`mcp_kg/`), por D-A (§8): un archivo de configuración por cada grafo posible,
   con su clave de `data/experiment/neo4j/grafos.py` y su sha esperado:
   - el de desarrollo r2b sellado (`KG_Tanda0_Desarrollo_r2b`, `6e756043…`), que está hoy;
   - el re-sellado, si al cerrar el tramo 1 el re-sellado único de la tanda 0 ya está sellado. Si no lo está, lo armás en el tramo 3.
   - No cargás nada en Neo4j en este mandato: la carga y el test positivo del brazo del grafo van al principio de A2.2, como
     precondición declarada.
   - El comentario «r2b no se evalúa con EV2» de `grafos.py` (de U-REEXT-T0, 06/10/2026) es anterior a D5 (07/10/2026), que fija el grafo
     de desarrollo r2b como brazo del grafo de A2 (`:339`). No editás `grafos.py`: lo declarás.
4. **Los tests, sobre la copia y después en el repo:**
   - **la regresión del denso:** el test (d) de `test_mcp_vector.py`, byte a byte, con el índice viejo;
   - **el BM25:**
     - determinismo (dos construcciones, el mismo sha del índice y los mismos rankings);
     - el analizador sobre una lista fija de palabras, con lo esperado y su fuente;
     - el transporte por MCP con `cliente_falso.py`, byte a byte contra el cálculo directo;
   - **el aislamiento** (`aislamiento/test_aislamiento.py`, en modo init, USD 0): (a) a (d) para la configuración BM25. El positivo del
     brazo del grafo queda para A2.2.
5. **El diseño de la caracterización de H-B2,** escrito antes de correrla: qué sesiones, con qué `--max-turns`, con qué preguntas propias
   (`banco_mcp/smoke/preguntas_smoke.json` o preguntas nuevas tuyas, nunca de EV2), qué se registra y cómo se decide. Lo registrado
   incluye `num_turns`, las llamadas del log R1, los turnos del asistente, el `subtype` del resultado y si el corte disparó.

**El FRENO A2.1-a** lleva: el paso 0, los cambios de código con su diff, los tests, el sha del índice nuevo, el diseño de H-B2 y los
comandos del tramo 2 con su costo estimado. Frenás ahí.

## 4. Tramo 2 (con el «seguí» de la autora; paga, con el tope de la §8): H-B2 y el smoke

- **Los pasos que pagan los corre la autora en su terminal,** con los comandos que dejás preparados en el tramo 1: el lanzador toma
  `ANTHROPIC_API_KEY` del entorno (`banco_mcp/agentes/lanzar_agente.py:125-126`). Vos no cargás la clave ni abrís un `.env`.
- **Cómo llega la clave** (decisión de la autora): desde `data/experiment/evaluacion/.env`, el mismo que usan los runners de la
  extracción (`reextraccion_v2/corpus_v2/runner_corpus.py:98` y `:1370-1371`), dentro del mismo comando, sin que la autora la escriba ni
  la pegue, sin imprimirla y sin que quede en el historial de la terminal.
  - Usás el envoltorio de la mesa, `con_clave_del_entorno.py`. Lo copiás tal cual a `data/experiment/banco_mcp/a2_1/` desde
    `~/INGENIERIA IA/TESIS/fuera_del_repo/scratchpads/d0348a29-aaa4-4292-82f3-0c0149e3787e/scratchpad/hoja_de_ruta_tanda1_mesa/decisiones_106_mesa/a21/con_clave_del_entorno.py`,
    con su sha256 `83527b334ca6c6be6ec3ce277bb43f60c6679347a9da237253e9cf6beb06a397`. Si no da, frenás.
  - El envoltorio lee el archivo con `dotenv_values` y le pasa al comando solo esa variable, por su entorno: no la imprime ni la pone en
    la línea de comandos. Si falta el archivo o la variable, frena sin mostrar ningún valor. Las pruebas de la mesa, con un archivo falso,
    están junto a él (`salida_pruebas_con_clave_del_entorno.txt`).
  - Cada comando pago es un script `zsh` en `a2_1/`, que la autora corre con `zsh <script>`. Así la terminal guarda solo esa línea.
  - Forma de cada comando, con su tope y su freno:
    `"$R/.venv/bin/python" -I -B data/experiment/banco_mcp/a2_1/con_clave_del_entorno.py --entorno data/experiment/evaluacion/.env -- <comando del banco>`.
  - **Vos nunca lo corrés con el `.env` real.** Para probar los scripts usás un archivo falso tuyo que no se llame `.env` ni termine en
    `.env`, y lo borrás al terminar.
- **Los comandos usan las guardas del banco,** con el tope de USD 3 y el freno en 2 (D-C): `--autorizado-tope` y `--freno`
  (`banco_mcp/smoke/correr_smoke.py`). El costo se calcula desde los tokens con los precios sellados (R9).
- **H-B2:** corre el diseño del tramo 1. El FRENO da qué cuenta `num_turns`, si `--max-turns` corta y cuándo. Da también una propuesta de
  criterio de corte R5 sobre la señal verificada, con sus alternativas. El criterio lo fija la autora al firmar el pre-registro.
- **El smoke de las dos configuraciones de fragmentos** sobre preguntas propias, como la fase B: sesiones completas (R3), mapa R7, log
  R1, aislamiento de punta a punta y el costo R9. Si la versión del CLI cambió, también re-valida el brazo del grafo de la fase B
  (KG-Refinado), solo si ya está cargado en Neo4j: no cargás otro grafo. Si no está, lo declarás, y esa re-validación va al principio
  de A2.2.

**El FRENO A2.1-b** lleva los resultados y el gasto. Frenás ahí.

## 5. Tramo 3 (con otro «seguí»; USD 0): el pre-registro de A2.2, en BORRADOR

`docs/preregistro_A2_2_sistema_por_fragmentos.md`, en BORRADOR. Lo firma la autora; se sella con su commit. Lleva:
- **los brazos:**
  - el grafo, con su sha, por D-A: el re-sellado, si al despachar este tramo está sellado; si no, el sellado (`6e756043…`), y se declara;
  - fragmentos BM25 y fragmentos densos, con el sha de cada índice y el analizador;
  - el híbrido de B1.9, declarado fuera (D-B);
- **lo común a los brazos:** el agente, el modelo, la versión del CLI, el prompt con su diff entre brazos, el contrato R4, la vía de
  credenciales (con el envoltorio de la §4) y top-k = 5, acotado por el servidor (D-D);
- **el criterio de corte R5,** sobre la señal de H-B2;
- **EV2:** sus 40 preguntas, por ruta y sha, sin abrirlas;
- **la corrida:** N = 1 completa más N = 3 parciales, y la auditoría del 10 % con adjudicación simétrica, del mismo protocolo de EV2
  (`:340`);
- **el juez de EV2,** con su modelo y su prompt por sha (`data/experiment/ev2_juez/juez.py`);
- **la cifra principal sobre todas las preguntas,** y aparte la cifra sin las que caen en unidades de la cola (D5);
- **las predicciones** de `:339`: incorrectos, criterios cubiertos, abstenciones, latencia y costo por pregunta, y la asimetría
  esperada entre el texto crudo y la representación comprimida;
- **el análisis:** las dos comparaciones con Holm;
- **las tasas de pares discordantes,** que salen para el N de B6.3 (Q5), y `c_agente` (Q6);
- **la no comparabilidad con la tabla de EV2** (principio 8), declarada;
- **el tope de A2.2** (unos USD 15 en el plan; en EV2, la corrida del agente costó 14,88: `ev2_reporte/reporte_ev2.md:388-390` y
  `:403`), a fijar por la autora;
- **cuándo corre:** apenas se selle este pre-registro, y no al mismo tiempo que la tanda 1, salvo que la mesa verifique antes los límites
  de la cuenta (decisión de la autora del 15/10/2026). La verificación la presenta la mesa, con su costo, y la decide la autora;
- **lo que no se decide en A2.1:** el diagnóstico posterior a A2.2 (decisión de la autora del 08/10/2026, `:340`).

Cada decisión que el borrador no puede tomar va marcada [DECIDE LA AUTORA], con sus opciones. **El FRENO final** lleva el borrador.

## 6. Escrituras

- **En el repo:**
  - `data/experiment/banco_mcp/mcp_vector/`: el servidor con la configuración BM25, `construir_indice.py` con el manifiesto, las
    configuraciones nuevas y sus tests. El `indice/` sigue fuera de git, con su sha declarado;
  - `data/experiment/banco_mcp/mcp_kg/`: solo el archivo de configuración nuevo del brazo del grafo para A2;
  - `data/experiment/banco_mcp/aislamiento/resultados/` y `smoke/resultados/`: carpetas nuevas de A2.1;
  - `data/experiment/banco_mcp/a2_1/` (se crea): los FRENOs, el REPORTE, el diseño de H-B2, sus resultados, tus scripts y tus
    controles;
  - `docs/preregistro_A2_2_sistema_por_fragmentos.md`, en BORRADOR.
- **Fuera del repo:** el scratchpad de tu sesión y el paquete `revision_A2_1_FRENO_<tramo>/`.
- **Prohibido:**
  - todo lo demás;
  - en particular, `banco_mcp/gate/`, `mcp_kg/servidor_mcp_kg.py`, `data/experiment/neo4j/` y el contenedor de Neo4j;
  - el cuarteto hasheado y el cluster del verificador, y todo eval set y sus salidas, EV2 incluido;
  - lo del camino a la tanda 1: la segmentación oficial, la extracción, el catálogo, el re-sellado y `reext_t0/`;
  - la memoria compartida del proyecto y su índice, `.claude/` del repo y `.gitignore`;
  - commitear.

## 7. El checkpoint y el cierre

- `checkpoint_A2_1.md`, en el scratchpad de tu sesión: qué hiciste, qué falta, qué archivos tocaste con su ruta y qué quedó abierto. Lo
  escribís al terminar cada paso y das su ruta en cada respuesta.
- **Cada FRENO** lleva:
  - el paso 0, con `$HOME`;
  - lo de su tramo;
  - la foto sha256 del repo entero (sin `.git`, con los `.env` solo por su tamaño y su fecha) antes y después: solo cambia lo de la §6;
  - los `.pyc`;
  - el grep de convenciones.
- **El paquete** `revision_A2_1_FRENO_<tramo>/` va con su `manifest.txt` y su copia con `ditto` a
  `~/INGENIERIA IA/TESIS/fuera_del_repo/scratchpads/<sesión>/scratchpad/`, verificada (CLAUDE.md §4.g).
- Nada commiteado, ningún mensaje de commit preparado y nada escrito en la memoria. Sin esperas programadas ni `sleep`.

## 8. Las decisiones de la autora (15/10/2026, pedido recibido a las 15:16:05; hoja de la mesa, §106)

- **D-A, el grafo del brazo del grafo:** el de desarrollo re-sellado. Si al despachar el tramo 3 el re-sellado no está sellado, se usa el
  sellado (`6e756043…`, `bbc38dc`), y se declara.
- **D-B, el híbrido de B1.9:** queda declarado fuera. No entra a B6.3 en ningún caso (laudo 2).
- **D-C, el tope del tramo 2:** USD 3, con freno en 2. La fase B costó USD 0,534 de un tope de 3 (README del banco, «Estado»).
- **D-D, top-k = 5:** el servidor acota `limite` a 5.
- **Los pasos pagos** los corre la autora, con la clave cargada desde el `.env` del repo dentro del mismo comando (§4).
- **A2.2 no corre al mismo tiempo que la tanda 1,** salvo que la mesa verifique antes los límites de la cuenta (§5).

## 9. Las dos cláusulas de todo despacho

**Copias del repo sin `.env` ni `NO_ABRIR_`.** Ninguna copia del repo lleva un `.env` ni un archivo cuyo nombre empiece con `NO_ABRIR_`.
La copia se hace así:

```
rsync -a --no-links --exclude=/.git --exclude=/.venv --exclude=/.venv-app --exclude=.DS_Store --exclude=__pycache__ \
  --exclude='.env' --exclude='.env.*' --exclude='*.env' --exclude='NO_ABRIR_*' <repo>/ <copia>/
```

- Justo después, y antes de correr nada sobre la copia:
  `find <copia> \( -name '.env' -o -name '.env.*' -o -name '*.env' -o -name 'NO_ABRIR_*' \) | wc -l` tiene que dar 0. Si no da 0,
  frenás. Los encontrados se borran por nombre, sin abrirlos, y se declaran en el FRENO con su ruta (con la carpeta personal reemplazada
  por `$HOME`).
- Nunca abrís, mostrás, copiás ni imprimís un `.env`: ni con `cat`, `head`, `less`, `grep` o `sed`, ni con Read, ni desde un script.
  La clave la carga el runner, solo en la corrida real en el repo.
- La copia queda sin el `.env.example` rastreado de `run_2_papers/code/` y sin el `NO_ABRIR_` del repo
  (`data/experiment/med_umbrales/p/lote1/freno/`). Si un control compara la copia con el repo archivo por archivo, lo declara.

**Carpetas vedadas.** No abrís, no listás ni copiás nada de estas carpetas, salvo que el despacho autorice un archivo por su ruta:
- en `~/INGENIERIA IA/TESIS/fuera_del_repo/`: `adjudicacion_s1ter/`, `adjudicacion_s1quater/`, `correccion_E0/`, `lecturas_ciegas/`,
  `lectura_lote2/`, `respaldo_memoria/` y `NO_ABRIR_evidencia_adjudicacion_s1quater/` (la evidencia de la adjudicación de S1-quater:
  una copia del scratchpad de una sesión y la carpeta `traspaso_etapa2`);
- `~/Desktop/traspaso_etapa2/`;
- ningún archivo cuyo nombre empiece con `NO_ABRIR_`, esté donde esté.

Si una búsqueda (`find`, `grep -r`, `rsync`, un script) puede recorrerlas, las excluye. Si algo de ellas aparece en una salida, lo
declarás en el FRENO, con su ruta y sin copiar su contenido.

FRENO.

## Firma

FIRMADO por la autora el 15/10/2026 a las 15:54:12 (por mensaje: «Firmo el mandato de A2.1 (b311859c…) tal como está»; hoja de ruta de
la mesa, §107). El texto firmado es el de arriba, hasta antes de esta sección, y su sha256 es
`b311859c0cf90ad6581cd4e639b37a7498bd8daad0ac8475e83ce604ddf7076d` (la versión para firmar de la mesa, `decisiones_106_mesa/a21/`). Rige
desde esta firma.

## Notas posteriores a la firma

- **15/10/2026 — El juez y la muestra simétrica de A2.2** (decisión de la autora sobre Q12, recibida a las 16:17:35; registro de
  decisiones del 15/10/2026, §9). El pre-registro de A2.2 que arma el tramo 3 (§5) lleva además:
  - **el juez, congelado antes de su firma:**
    - el de EV2 tal cual (`data/experiment/ev2_juez/juez.py`, prompt `fd446f8e…`), o el ajustado con la mitad de ajuste del gold de la
      autora (20 respuestas de EV2), con su sha;
    - A2.2 y B6.3 usan el mismo;
  - **su muestra simétrica:** 20 de sus 120 respuestas (7, 7 y 6 por brazo), estratificadas también por el veredicto del juez, como la
    de EV2. La autora las lee a ciegas, sin ver ningún veredicto. Es la mitad de verificación del gold;
  - **el criterio de aceptación del juez,** sobre esa mitad: Wilson inferior de al menos 0,85 por criterio y al menos 18 de 20 por
    respuesta. Si no se cumple, se frena y decide la autora;
  - **si el ajuste no está antes de la firma:** A2.2 corre con el juez de EV2, y el ajustado se verifica después sobre las mismas 20
    respuestas.
  - El texto firmado no cambia.

- **15/10/2026 — el re-sellado único de los grafos r2b de la tanda 0.** Los grafos sellados que cita este documento tienen una versión posterior, del re-sellado único (`docs/mandatos/URESELLADO_T0_resellado_unico_grafos_r2b.md`, firmado; FRENO en `data/experiment/resellado_t0/FRENO_resellado_T0.md`): `6e756043…` (KG-Tanda0-Desarrollo-r2b) → `acb26dca…` (KG-Tanda0-Desarrollo-r2b-rs1, 6.962 nodos y 23.311 aristas). Cambian por el código de U-OMISIONES-COD (`ded41d50`) y por las salidas de R0 (`1d690df3` y `2d0f5277`). El diff por campo y por causa está en `data/experiment/resellado_t0/salidas/`. Los sellados siguen sellados (principio 9); el commit del sello de los nuevos queda en `commit_sellado` de `data/experiment/neo4j/grafos.py`. Por D-A, el grafo de desarrollo re-sellado es `acb26dca…` (KG-Tanda0-Desarrollo-r2b-rs1), la versión posterior de `6e756043…`: es el brazo del grafo de A2.2 si está sellado al despachar el tramo 3. El texto firmado no cambia.
