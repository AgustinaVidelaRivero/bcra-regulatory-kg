# FRENO — U-BANCO-PARALELO: el lanzador del banco con P sesiones en paralelo

Sesión `95486f81-2327-4620-90bc-f61b59d22c1a`, 26/10/2026, con el agregado v7 del despacho (el testigo, §11). USD 0: no
corrí nada pago, no escribí en el repo ni commiteé.
Trabajé en una copia del repo en `banco_paralelo/copia/bcra-regulatory-kg/` (HEAD `2addcf32`), con un Neo4j propio.
Todas las cifras de este FRENO salen de los archivos del paquete que nombro al lado; los nombres de archivo son los del
paquete (con `_UBANCO_PARALELO`).

## 1. Resumen

- **El lanzador del lote** (`agentes/lanzar_lote_paralelo.py`) corre cada sesión como un proceso hijo de un lanzador de
  una sesión del banco, sin cambiar su lógica, con P lugares a la vez, la guarda del gasto global, la guarda de otro paso
  pago antes de cada tanda (modo real), el control del cwd compartido después de cada tanda y al final, y el registro
  del lote (horas, worker, carpeta de configuración, costo R9, R3, reintentos y 429, y la fecha del CLI).
- **Las sesiones de N6 no tienen en HEAD una configuración R10 ni un lanzador de una sesión** (registro, §82: su comando
  lo arma U-NAV en el paso 0 de N6). Para probar el lote sobre los servidores de N6 armé una configuración DE PRUEBA y un
  lanzador de una sesión con las piezas de `lanzar_agente.py`, como los de A2.1 y A2.2 (§6, punto 1). Es lo primero que
  la mesa tiene que mirar.
- **Los doce criterios dan bien** (§4), con dos cosas que la autora tiene que decidir antes del humo pago: con su tope y
  su freno (1 y 0,80) y el presupuesto por sesión de R5 (1,80), **el humo no lanza ninguna sesión** (§6, punto 2), y
  **la línea «Today's date is …» no está en las transcripciones copiadas de las sesiones reales** del banco (§6, punto 3).
- **El contenedor del repo escucha en 7474 y 7687** y no lo toqué: la prueba «nada escucha en 7687» no se puede dar; la
  reemplacé por `lsof` sobre los procesos de cada sesión (§6, punto 4).
- **El testigo (agregado v7, criterio 13): FRENO.** El control está escrito y sumado al test de aislamiento, y su prueba
  (9 sesiones con P = 3 y los dos negativos) da todo lo que pide: el positivo en las 9, ningún trecho ni token de ningún
  testigo en ningún pedido, stream, carpeta de configuración ni log R1, las tools de su brazo, los testigos sin cambiar,
  los plantados borrados, el cwd vacío y el negativo detectado en los dos brazos. Pero **salen pedidos de la máquina:**
  durante las tandas, los CLI abren conexiones a `160.79.104.10:443` y `34.149.66.165:443`, con el entorno del modo init
  del lanzador sellado, que el agregado no me deja cambiar. Freno antes de la corrida completa (§11).

## 2. Paso 0

`scripts/paso0_UBANCO_PARALELO.zsh` → `salidas/paso0_consola_UBANCO_PARALELO.txt` (lo corrí otra vez al armar el paquete;
la primera vez, al arrancar, dio lo mismo, con la carpeta vacía):

```
scratchpad: vacío (sesión nueva; ls -la: solo . y ..)
pwd: $HOME/INGENIERIA IA/TESIS/fuera_del_repo/banco_paralelo — vacía (ls -la: solo . y ..)
142 v2 entre los últimos 20 asuntos de git log --format=%s: 1 (es 17a51a42)
git log -1: 2addcf32 Preregistro de la evaluacion final: la nota al pie con las coincidencias con las citas y con las preguntas, los desvios de la relevancia, los reemplazos, lo que vio la mesa y la verificacion del juez
§52: 1   §53: 1   §85: 1   §88: 1   (grep -c '^## N\.' sobre git show HEAD:docs/registro_decisiones_calidad_y_evaluacion_2026-10-15.md)
git status --porcelain --untracked-files=no: 0 líneas
git show HEAD:data/experiment/banco_mcp/agentes/lanzar_agente.py: CLAUDE_CONFIG_DIR 6 veces, "lanzador" 2 veces y la línea
  ENTORNO_PERMITIDAS = ("PATH", "HOME", "NEO4J_URI")
cat-file -e en HEAD: 0 para mcp_kg/servidor_mcp_kg_nav.py, mcp_kg/mcp_kg_nav.json, mcp_kg/config_mcp_kg_nav_acumulado.json,
  mcp_vector/mcp_fragmentos_bm25_acumulado.json y mcp_vector/mcp_fragmentos_hibrida_acumulado.json
manifiesto instalado del índice por punto: 8b3b0d8daa28b5fead541201dc187ba1e1a8f17976a7074177a3a2741c560eb0 = el de HEAD
  (mcp_kg/manifiestos_indice_puntos/KG_Acumulado_Tandas0y1_r2b_sincola.json), byte a byte
indice_bm25.json de mcp_vector/indice/e0_acumulado_30tos_bm25/: 59e7acddf4ef8875207b8494192f8b56b2e99b959529e53bbed86c8f79a8a8ef
  = sha256_indice_esperado de config_fragmentos_bm25_acumulado_r2b.json
```

El scratchpad empezó vacío y no usé nada de él que se haya perdido.

## 3. Lo que armé

En la copia del repo (los blobs de HEAD de todo lo demás no cambian, §4, criterio 5), en `codigo/` del paquete con su
ruta y su sha256 en `codigo/rutas_en_la_copia_UBANCO_PARALELO.txt`:

| archivo (en la copia) | qué es |
|---|---|
| `agentes/lanzar_lote_paralelo.py` | el lanzador del lote (punto 4.a) |
| `aislamiento/test_aislamiento_paralelo.py` | el test de aislamiento sobre el lanzador en paralelo (punto 4.b) |
| `paralelo/guardas_lote.py` | la guarda de otro paso pago y el control de la extracción (4.a y 4.e) |
| `paralelo/config_agentes_n6_prueba.json` | la configuración de prueba de los brazos de N6 (no es R10; §6, punto 1) |
| `paralelo/lanzar_agente_n6_prueba.py` | el lanzador de una sesión de esos brazos, con las piezas de `lanzar_agente.py` |
| `paralelo/control_neo4j_propio.py` | responde el Neo4j de `NEO4J_URI` y su KG_Meta da el sha256 del acumulado |
| `paralelo/informe_lote.py` | una línea por sesión del registro: R3, R9, reintentos y 429 |
| `paralelo/corrida_en_seco_lote.py` | la corrida en seco (4.c) y las pruebas de las guardas |
| `paralelo/cli_falso/{claude, claude_falso.py, planes_seco.json}` | el CLI falso de la corrida en seco |
| `data/experiment/neo4j/docker-compose.banco_paralelo.yml` | el override del Neo4j propio (4.d) |

Fuera de la copia, en `banco_paralelo/comandos/`: `humo_lote_paralelo.zsh` y `lote_humo.json` (4.e).

**El lanzador del lote, en una línea por pieza:**

- recibe `--lote` (las sesiones con las entradas de `lanzar_agente.py`: `id`, `brazo`, `pregunta`, y un `bloque`), `-P`
  (3 por defecto), `--tope` y `--freno` (obligatorios), `--presupuesto-sesion` (1,80 por defecto, el `--max-budget-usd`
  de R5), `--lanzador` (`agentes/lanzar_agente.py` por defecto), `--sesiones` y `--out`;
- corre `python -B <lanzador> --brazo … --id … --pregunta … --out <out>/<id> --modo … --via … --sesiones <raíz>`: el
  cwd compartido es `<raíz>/cwd`, la carpeta de configuración `<raíz>/config/<session_id>` (la crea el lanzador de la
  sesión y frena si existe), el log R1 `<out>/<id>/log_r1_<id>.jsonl` y la salida `<out>/<id>/`;
- antes de lanzar nada frena (código 3) si se repite un id (también sin distinguir mayúsculas), una salida o un log, si
  una salida ya existe, si la raíz de las sesiones está en el repo o en git, o si el cwd compartido no está vacío. La
  carpeta de configuración no la elige el lote: la controla al terminar cada sesión (distinta y fuera del repo y de git),
  y si no, frena (código 5);
- la guarda del gasto no lanza una sesión si `acumulado + presupuesto × (las que corren + 1)` pasa el freno o el tope;
  espera a que termine una (`os.wait`) y vuelve a mirar; si no corre ninguna, frena (código 2). El acumulado es el R9 de
  cada sesión que termina (`LA.costo_desde_tokens` con los precios sellados sobre el `modelUsage` de su meta);
- la guarda de otro paso pago corre en modo real antes de la tanda 1 y de cada tanda (código 7); el control del cwd,
  después de cada tanda y al final (código 4); R5 igual en todas las sesiones (código 5);
- el registro (`<out>/registro_lote.json`) da por sesión inicio, fin, worker, tanda, carpeta de configuración, R9, R3,
  reintentos, 429 y fecha del CLI; el orden de fin; las superposiciones de horas; las fechas por bloque y el cambio.

## 4. Los trece criterios

| # | criterio | script → salida | resultado |
|---|---|---|---|
| 1 | aislamiento en paralelo: los cuatro de hoy y los nuevos, con las seis comprobaciones de fragmentos | `test_aislamiento_paralelo` → `aislamiento_paralelo_UBANCO_PARALELO.json` | PASS: init (9 sesiones), ejecución (3 tandas) y lo compartido |
| 2 | P = 3 da las mismas salidas por sesión que P = 1 | `corrida_en_seco_lote` → `corrida_en_seco_UBANCO_PARALELO.json` (`A_igual_B`) | OK: 12 de 12 sesiones iguales |
| 3 | la guarda global corta antes del freno | ídem (`C_guarda_del_gasto`) y `humo_con_sus_cifras_en_seco_UBANCO_PARALELO.txt` | OK: frena con 0,2152 de 2,00; el humo, con 0 lanzadas |
| 4 | los comandos pagos no llevan la clave | `control_sin_clave` → `control_sin_clave_UBANCO_PARALELO.txt` | OK: 0 valores con forma de clave, 0 asignaciones |
| 5 | los archivos sellados del banco no cambian | `sellos_banco` → `sellos_banco_{antes,despues}_UBANCO_PARALELO.txt` | OK: 2.357 archivos, la misma lista |
| 6 | el control negativo falla en sus dos casos | `test_aislamiento_paralelo` (`negativo`) | OK: fallan los dos |
| 7 | el control de la extracción frena con el proceso vivo y deja pasar sin él | `corrida_en_seco_lote` (`E_…`) | OK |
| 8 | el grafo con su codificador; fragmentos no alcanzan ni el codificador, ni el índice por punto, ni Neo4j; el grafo no abre los índices de fragmentos | `test_aislamiento_paralelo` (`ejecucion`) | PASS |
| 9 | el contenedor del repo y los otros, como antes; el propio, bajado | `docker_ps_a_{antes,despues}_UBANCO_PARALELO.txt` | OK: 278 iguales; el propio, bajado |
| 10 | el cwd compartido vacío después de cada tanda y al final; carpetas de configuración distintas y fuera del repo | los dos JSON | OK |
| 11 | `NEO4J_URI` llega al servidor del grafo de cada sesión por la lista, al puerto propio; ninguna de fragmentos se conecta | `test_aislamiento_paralelo` (`init` y `ejecucion`) | OK |
| 12 | la guarda de otro paso pago: el lote y el humo frenan con el proceso de prueba vivo y dejan pasar al cerrarlo; un shell o un editor no | `corrida_en_seco_lote` (`D_…`) | OK |
| 13 | el testigo: positivo en todas, ningún testigo llega, las tools de su brazo, los testigos sin cambiar, los plantados borrados, el cwd vacío, el negativo en los dos brazos | `testigo_aislamiento` → `testigo_prueba_UBANCO_PARALELO.json` y `reanalisis_tools_testigo_UBANCO_PARALELO.json` | **FRENO:** lo que pide da bien en la prueba, pero salen pedidos de la máquina (§11); la versión integrada, sin correr |

**1. El aislamiento en paralelo** (`aislamiento_paralelo_UBANCO_PARALELO.json`). El lote init: 9 sesiones con P = 3 por
`lanzar_lote_paralelo.py --modo init` (código 0, 9 terminadas), en tres tandas con sesiones del grafo y de fragmentos a la
vez: la 1 (`AISL-01-kg`, `AISL-02-fragmentos_bm25`, `AISL-03-kg`), la 2 (`AISL-04-fragmentos_hibrida`, `AISL-05-kg`,
`AISL-06-fragmentos_bm25`) y la 3 (`AISL-07-kg`, `AISL-08-fragmentos_hibrida`, `AISL-09-kg`); en cada una, dos pares
grafo-fragmentos con sus horas superpuestas en el registro del lote (entre 1,124 y 3,187 s, `tandas_superposicion_grafo_fragmentos`).
Por sesión:
- (a) el inventario de `system/init` es el esperado de su brazo, sin tools del otro brazo ni de archivos, shell o red, con
  `dontAsk` y el servidor `connected`: 9 de 9;
- (b) y (c), sobre `servidor_mcp_vector.py` y `bm25_fragmentos.py`: ningún import del grafo, ninguna mención a sus
  artefactos, ningún socket ni bolt, y `import neo4j` falla en el venv de fragmentos (`ModuleNotFoundError`);
- (d) la llamada real por el mismo JSON de MCP: la fase en ejecución (abajo);
- un proceso de servidor MCP por sesión: 9 pids distintos (del `inicio` del log R1), el mismo en todas las líneas de su log;
- el log R1 de cada sesión, con su tag en `inicio` y en cada `llamada` (la línea `fin` no lleva tag), de su servidor
  (`mcp_kg` o `mcp_vector`), con `inicio` y `fin`, 0 llamadas, como su stream (0 tool_use) y su mapa R7 (vacío);
- ningún archivo de una sesión en otra: los 8 archivos de cada salida llevan su id y ninguno el de otra; los 5 de cada
  carpeta de configuración, ninguno con el session_id de otra; `BANCO_LOG_R1` de cada comando es el suyo;
- 9 carpetas de configuración distintas, fuera del repo, de la copia y de git;
- el cwd compartido, vacío después de cada tanda, al final del lote y al final del test.

La fase en ejecución: por tanda, los servidores de sus tres sesiones vivos a la vez, cada uno lanzado por su JSON de MCP
con el entorno de su sesión (`N6.env_sesion`) y su log R1. En cada ronda las llamadas del grafo (`buscar_puntos` y después
`buscar_nodos`) y las de fragmentos (`buscar_pasajes`, dos por ronda) arrancan juntas, en hilos; después de cada llamada
de fragmentos, `lsof` sobre su pid y sus hijos. 16 controles de fragmentos (4, 8 y 4 por tanda); cada sesión de
fragmentos tiene al menos una llamada cuyo intervalo se superpone con el de una llamada del grafo (11 de los 16). Los logs
R1 de la fase: cada uno con su tag, su pid y solo las tools de su brazo, en el orden, con el input y el sha256 de la
salida que recibió el cliente.

Lo compartido de solo lectura, antes y después, igual: los 14 archivos del kg.json del acumulado y de los tres índices que
usan las sesiones (por sha256), el `pip freeze` del venv de fragmentos (`e363fdf2…`) y la base: KG_Meta `0435d41f…`,
20.833 nodos, 55.358 aristas, huella de estado `25594502…` y de contenido `a207d7fb…`.

**2. P = 3 contra P = 1** (`corrida_en_seco_UBANCO_PARALELO.json`, `A_P3`, `B_P1` y `A_igual_B`). La corrida en seco importa
`agentes/lanzar_lote_paralelo.py` por su ruta y llama a su `main` en modo real con el CLI falso primero en el PATH (su
`--version` dice «2.1.241-falso»; el `claude` del PATH es `paralelo/cli_falso/claude`), sin tocar el `sys.path` por fuera.
El lote: 12 sesiones, 6 por brazo (6 del grafo, 3 BM25 y 3 híbridas), intercaladas por pregunta, S01 a S06, con los dos
brazos seguidos en cada bloque, contra los servidores reales de N6 y su Neo4j. Con P = 3: 3 a la vez como máximo, los
workers 1, 2 y 3, 21 pares con horas superpuestas (14 grafo-fragmentos); con P = 1: 1 a la vez, el worker 1, ninguna
superposición. Las salidas por sesión (las llamadas del log R1 con su tool, input, sha256 y largo de la salida y error,
si el log cerró, R3, el JSON final, el R9 y la fecha) dan iguales en las 12. El orden de fin con P = 3 no es el de la
lista (`S01-fragmentos_bm25` termina primero) y no cambia nada.
- **La sesión que falla a mitad** (`S03-fragmentos_bm25`, por su plan: el CLI falso mata su servidor después de la
  primera llamada y sale sin `result`): incompleta con R3, «sin evento result» y «log R1 sin línea fin», con P = 3 y con
  P = 1; las otras 11, completas en las dos; ninguna frena.
- **El cambio de fecha:** el registro da el bloque S04, dentro del bloque (`S04-kg` con 2026-10-26 y
  `S04-fragmentos_hibrida` con 2026-10-27), y S04 como el único bloque con fechas distintas entre brazos, con P = 3 y
  con P = 1.

**3. La guarda del gasto** (`C_guarda_del_gasto`). El mismo lote con P = 3, presupuesto 1,80, freno 2,00 y tope 2,50: con
una corriendo, la segunda daría 3,60 y espera; se lanzan de a una, y antes de `S03-kg` frena (código 2) con un acumulado de
0,2152 y 8 sesiones sin lanzar. El peor caso al lanzar cada una (acumulado + presupuesto de las que corren): 1,80, 1,8592,
1,9074 y 1,9668, todos por debajo del freno. Con las cifras del humo (tope 1, freno 0,80), el lote frena antes de la
primera, sin crear ninguna sesión (`humo_con_sus_cifras_en_seco_UBANCO_PARALELO.txt`; §6, punto 2).

**4. La clave** (`control_sin_clave_UBANCO_PARALELO.txt`). En `humo_lote_paralelo.zsh` y `lote_humo.json`: 0 valores con
forma de clave (Anthropic o AWS) y 0 asignaciones de `ANTHROPIC_API_KEY` o `AWS_*`. La clave llega solo por el archivo de
entorno que se pasa como argumento, con `a2_1/con_clave_del_entorno.py`, que no la imprime.

**5. Los archivos sellados** (`comparacion_sellos_UBANCO_PARALELO.txt`). Los 2.357 archivos versionados de
`data/experiment/banco_mcp/`, `data/experiment/neo4j/` y `data/experiment/tanda0/code/` en la copia (las configuraciones
R10, las plantillas, los bloques, los servidores y los lanzadores), por sha256, antes de escribir nada y al terminar: la
misma lista (`ac89389c…`).

**6. El control negativo** (`negativo`). La configuración de fragmentos con el servidor del grafo agregado (en la carpeta
temporal de la sesión, nunca la sellada): su `system/init` trae las 10 tools (9 del grafo) y el control 1 la marca. El
proceso de prueba con un socket al 37687 y el kg.json abierto (avisa que los tiene por su salida estándar y después solo
espera su entrada): el control 2 ve la conexión y el archivo. Los dos fallan como deben, así que el test vale.

**7. El control de la extracción** (`E_control_de_la_extraccion`). Con `python3 <tmp>/runner_corpus.py` vivo: lo encuentra
(su pid y `runner_corpus.py`) y la CLI frena con el código 9; al cerrarle la entrada termina (código 0) y la CLI deja
pasar (0); con un `sh -c` y un `grep` que nombran `runner_corpus.py` y un `ed` que lo abre, deja pasar (0).

**8. El grafo con el servidor de navegación** (`ejecucion`). Cada una de las 5 sesiones del grafo con su codificador, hijo
de su servidor, con 5 pids distintos; en cada control del lado del grafo, una conexión a `NEO4J_URI`, ninguna al 7687 y
ningún archivo de `mcp_vector/indice/` abierto (el servidor y sus hijos). En los 16 controles de fragmentos: ninguna
conexión al 37687 ni al 7687, ningún archivo abierto bajo el kg.json, `data/experiment/neo4j/` ni `mcp_kg/indice_puntos/`,
ningún descriptor de un codificador y ningún proceso hijo de un servidor del grafo. El control del descriptor tiene su
positivo: cada servidor del grafo sí tiene 2 descriptores de su codificador (sus dos pipes).

**9. Los contenedores** (`docker_ps_a_{antes,despues}_UBANCO_PARALELO.txt`). 278 contenedores con su nombre y su estado,
iguales antes y después: `neo4j-bcra-kg-compose` arriba y `neo4j-bcra-kg` salido (137), como estaban. El propio
(`neo4j-bcra-kg-banco-paralelo`) se creó después de la primera foto y lo bajé con `down` al terminar: no está en ninguna.

**10. El cwd compartido y las carpetas de configuración.** Vacío en las 4 tomas del lote init del test (3 tandas y el final)
y al terminar el test; en las 5 tomas del lote A (4 tandas y el final) y en las 13 del lote B (12 y el final). Las
carpetas de configuración: 9 en el test y 12 en cada lote, distintas y fuera del repo, de la copia y de git.

**11. `NEO4J_URI`.** Llega por la lista a las 9 sesiones del test (`entorno_de_la_sesion`: `bolt://127.0.0.1:37687`) y al
servidor del grafo de cada una: su `inicio` trae el backend `neo4j` y el KG_Meta del acumulado (`0435d41f…`), y durante el
lote init `lsof` (120 muestras, solo los puertos 37687 y 7687) ve el servidor del grafo de las 5 sesiones del grafo
conectado solo al 37687, y ningún proceso de las 4 de fragmentos conectado a ninguno de los dos. En ejecución, lo mismo
por pid. Como 7474 y 7687 escuchaban (el contenedor del repo), esta es la prueba en lugar de la del despacho (§6, punto 4).

**12. La guarda de otro paso pago** (`D_guarda_de_otro_paso_pago`). Con `python3 <tmp>/correr_prueba_T_v2.py` vivo, y
después con `python3 <tmp>/correr_a2_2.py` (un nombre del patrón de A2.2): el lote, en modo real, frena con el código 7
sin crear ninguna carpeta de sesión, y su guarda nombra el script; el humo frena con el 7 en su primera guarda (sin tocar
Docker ni la clave: las carpetas `salidas/humo_*` y `docker ps -a` no cambian). Al cerrarles la entrada terminan (0), el
lote lanza su sesión y `--solo-guardas` deja pasar (0). Con un `sh -c`, un `zsh -c` y un `grep` que nombran los scripts y
un `ed` que abre uno, `pgrep -f` con el patrón ve los 4 y la guarda ninguno: el lote lanza su sesión y el humo deja pasar.
El patrón es el del renglón 16 de `a2_2/guardas_a2_2.zsh` más `|correr_prueba_T_v2\.py` (`F_patron`).

## 5. El entorno de cada brazo, por nombre

Desde `entorno_de_la_sesion` de cada comando (los tres brazos usan `LA.env_sesion` como el brazo `vector`, así que dan
los mismos nombres):

- **modo init (el test, las 9 sesiones):** `ANTHROPIC_API_KEY`, `ANTHROPIC_BASE_URL`, `BANCO_LOG_R1`, `BANCO_REPO`,
  `BANCO_SESION_TAG`, `BANCO_VENV_VECTOR`, `CLAUDE_CONFIG_DIR`, `DISABLE_AUTOUPDATER`, `HOME`, `MCP_TIMEOUT`, `NEO4J_URI`
  y `PATH`, en el grafo, en BM25 y en la híbrida. La clave es la inválida del modo init de `lanzar_agente.py` (registrada
  por presencia) y `ANTHROPIC_BASE_URL` es su puerto cerrado;
- **modo real (la corrida en seco, las 12 sesiones del lote A):** los mismos sin `ANTHROPIC_BASE_URL`, en los tres brazos.
  La clave de la corrida en seco es un relleno que no es una clave, y el CLI falso no la usa.

`NEO4J_URI` está en los dos brazos, por la lista (§88), con el valor `bolt://127.0.0.1:37687`, la dirección de mi
contenedor. Ninguna sesión de fragmentos hereda otra variable de Neo4j ni del índice del grafo. No imprimí ningún otro
valor del entorno ni leí el de un proceso.

## 6. Lo que la mesa y la autora tienen que mirar

1. **La configuración de los brazos de N6 es de prueba.** HEAD no trae una configuración de agentes con el servidor de
   navegación ni con las configuraciones de fragmentos del acumulado, ni un lanzador de una sesión para ellas; el único
   lanzador que el despacho nombra para N6, `agentes/lanzar_agente.py`, toma sus brazos de `agentes/config_agentes.json`
   (el grafo con `agentes/mcp_kg.json` y R5 en 10, 12 y 0,30). Además, el servidor de navegación necesita
   `BANCO_VENV_VECTOR` para su codificador (`denso.requerido`), y `LA.env_sesion` solo lo pasa al brazo `vector`. Lo que
   hice, sin tocar nada sellado:
   - `paralelo/config_agentes_n6_prueba.json` junta los archivos sellados de cada brazo: `mcp_kg/mcp_kg_nav.json` con
     `agentes/bloque_tools_kg.txt` (el bloque con las familias, del 142 v2) y las nueve tools del servidor, en el orden
     alfabético en que las lista el CLI (`armar_meta` compara listas); `mcp_vector/mcp_fragmentos_{bm25,hibrida}_acumulado.json`
     con los bloques de `a2_1/`; la plantilla `agentes/plantilla_prompt.txt` (la de la parte común de la familia 6,
     decisión 9 de U-NAV-DISENO); R5 en 30, 32 y 1,80; base, `a2_2/config_agentes_a2_2.json` con su sha256;
   - `paralelo/lanzar_agente_n6_prueba.py` replica `lanzar_agente_a2_2.lanzar` con las piezas de `lanzar_agente.py` y
     pide `LA.env_sesion` como el brazo `vector` en los tres brazos (así el del grafo recibe `BANCO_VENV_VECTOR`);
   - el lote no depende de eso: corre cualquier lanzador con la interfaz de `lanzar_agente.py` (`--lanzador`).
   **PENDIENTE de la mesa:** si el humo y B6.3 usan esta configuración o esperan la de N6 (y la del grafo evaluado, sobre
   la que el test se repite antes de B6.3, USD 0).
2. **El humo, con sus cifras, no lanza ninguna sesión.** Con presupuesto por sesión 1,80 (el `--max-budget-usd` de R5) y
   freno 0,80, la primera ya da `0 + 1,80 > 0,80`: frena con el código 2 y USD 0 (`humo_con_sus_cifras_en_seco_UBANCO_PARALELO.txt`,
   el lote del humo con el CLI falso). Para tener 3 sesiones a la vez hace falta un freno de al menos 3 × 1,80 = 5,40. Dejé
   el comando con las cifras del despacho. **PENDIENTE de la autora:** el tope y el freno del humo, o el presupuesto que
   usa la guarda.
3. **La fecha del CLI no está en las transcripciones copiadas.** En las 120 transcripciones de `a2_2/resultados/n1/`
   (sesiones reales, CLI 2.1.241, `--bare`) `grep -c "Today's date"` da 0 en todas (lo conté por código, sin imprimir
   nada de ellas); tampoco está en sus streams, stderr, comandos ni metas. El lector del registro
   (`fecha_de_la_transcripcion`) funciona en la corrida en seco, donde el CLI falso escribe la línea, pero en una corrida
   real va a dar «sin la línea» (el registro las lista en `sesiones_sin_la_linea`). **PENDIENTE de la autora:** de dónde
   sale la fecha de cada sesión (por ejemplo, el primer `timestamp` de la transcripción, en hora local, declarado como
   aproximación). No lo agregué.
4. **7474 y 7687 escuchan durante todas las corridas:** el contenedor del repo (`neo4j-bcra-kg-compose`) estaba arriba al
   empezar y lo dejé así. En su lugar: durante el lote init, `lsof -iTCP:37687 -iTCP:7687` (solo esos dos puertos) ve
   cada servidor del grafo conectado al 37687 y ningún proceso de una sesión conectado al 7687; en ejecución, `lsof` por
   pid da lo mismo para los servidores lanzados con el entorno de su sesión.
5. **Una sesión que termina sin `result`** (cortada o caída) no tiene R9; la guarda la cuenta con el presupuesto entero
   (1,80) y su R9 queda en 0, declarado en el registro (`sin_result`, `acumulado_de_la_guarda_usd`). Es una decisión
   mía para que la guarda no subestime el gasto; si la mesa prefiere otra cosa, es una línea.
6. **El patrón de la extracción, tal cual, no ve un script con un espacio en su ruta:** `python3 "<tmp>/con espacio/runner_corpus.py"`
   no lo encuentra (`\S*?` no cruza el espacio), y la ruta del repo tiene uno («INGENIERIA IA»): una extracción lanzada
   con la ruta absoluta del script se le escaparía. La guarda de otro paso pago sí lo ve (su filtro toma rutas con
   espacios) y en el humo corre antes. En la corrida en seco, con ese proceso vivo, el control de la extracción
   dio «ninguna» (código 0) y la guarda de otro paso pago lo encontró (código 7, su pid y `runner_corpus.py`)
   (`E_control_de_la_extraccion.informativo_ruta_con_espacio`). **PENDIENTE de la autora:** si el patrón sigue tal cual.
7. **En el humo, la guarda de otro paso pago atrapa primero todo lo que atraparía el control de la extracción** (su patrón
   incluye `runner_corpus\.py`, `lanzar_t` y `correr_tanda`): con un `runner_corpus.py` vivo, el humo frena con el 7. El
   control de la extracción lo probé directo, con la misma CLI que llama el humo (`guardas_lote.py extraccion`).
8. **Decisiones chicas mías, declaradas:** el humo usa fragmentos BM25 (la base de F1) y las preguntas SMK-01 a SMK-03;
   el humo frena (código 11) si lo lanza una sesión de Claude (mira solo si existen `CLAUDECODE` o
   `CLAUDE_CODE_ENTRYPOINT`, después de las dos guardas), por la regla de la §82; en modo init el presupuesto efectivo de
   la guarda es 0; la guarda de otro paso pago deja fuera los procesos de pgrep que no son Python con un script del
   patrón (así un shell, un `grep` o un editor no frenan).
9. **La copia:** el rsync excluye además `data/experiment/neo4j/volumen` (el volumen del contenedor del repo, como en la
   §85), `.venv-app`, `.pytest_cache`, `__pycache__` y `.env.*` (deja fuera `run_2_papers/code/.env.example`, que no uso).
   El `.venv` del repo va clonado aparte con `cp -c` (como la etapa c2, §88): trae 3 enlaces adentro (`bin/python*`); el
   resto de la copia tiene 0.

## 7. Errores propios, con su causa

1. **Mostré en la consola la contraseña de desarrollo del grafo.** Para leer `data/experiment/neo4j/docker-compose.yml`
   tapé con `sed` las líneas con `AUTH` o `PASSWORD` seguidas de `=` o `:`, pero el comentario que la nombra y la línea
   del healthcheck (`cypher-shell … -p …`) pasaron. No la escribí en ningún archivo: el override no la lleva (la
   autenticación es la del archivo base) y mis scripts la toman de `conexion.py` por su código. Causa: tapar por nombre de
   clave en lugar de no imprimir el archivo. Después leí solo por `grep` con la salida tapada.
2. **La primera corrida en seco cayó después de lanzar su primera sesión:** guardé los archivos abiertos de cada lanzador
   en el dict de la sesión y el registro no se pudo serializar. El lote murió y la sesión `S01-kg` (CLI falso, USD 0)
   terminó sola, huérfana. Lo corregí (los archivos van en un dict aparte) y archivé la corrida en
   `banco_paralelo/salidas/intento1_registro_no_serializable/`.
3. **`tools_esperadas` del grafo, en el orden del servidor:** la primera sesión suelta en modo init dio R6 «no coincide»
   porque el CLI lista las tools en orden alfabético y `armar_meta` compara listas. Las ordené en la configuración de prueba.
4. **Dos pruebas de las guardas, vacías en la tercera corrida en seco:** la guarda de otro paso pago llamada dentro del
   mismo proceso deja fuera a sus descendientes, que eran justo los procesos de prueba, y la cuenta de `pgrep` la tomaba
   después de cerrarlos. Lo vi en los resultados (pgrep 0, y la guarda sin el script de la ruta con espacio). Ahora esas
   pruebas corren la CLI de la guarda como proceso aparte. Archivé la corrida en `salidas/intento3_guardas_dentro_del_proceso/`
   (la segunda, `intento2_antes_de_la_guarda_sin_result/`, dio bien, pero con la guarda de antes del punto 5 de la §6).
5. **El test de aislamiento, cuatro veces antes de la buena:** (1) esperaba el tag de la sesión también en la línea `fin`
   del log R1, que no lo lleva; (2) una carrera: el `ps` de la tabla de procesos aparecía como hijo nuevo al buscar el pid
   del servidor; (3) la prueba de que el grafo respondía a la vez era demasiado estricta (pedía que siguiera respondiendo
   cuando terminaba la llamada de fragmentos, y la primera híbrida, que carga el modelo, dura más): la cambié por la
   superposición de los intervalos, con las llamadas de fragmentos en hilos que arrancan junto con las del grafo;
   (4) dio PASS, pero antes de enmascarar la carpeta temporal en el resultado. Todas archivadas en
   `salidas/intento{1,2,3,4}_aislamiento_*/`; ninguna cambió un control de aislamiento.
6. **`control_copia_inicial_UBANCO_PARALELO.json` salió de una versión anterior del script,** sin el campo de los enlaces
   del `.venv` (entonces la copia no lo tenía); el final es de la versión del paquete.
7. **Corrí la prueba del testigo con pedidos saliendo de la máquina.** Confié en la sonda (una sesión, 0 conexiones fuera
   en 353 muestras) y corrí las 11 sesiones de la prueba; `lsof` vio las dos conexiones en las tres tandas. La condición
   del agregado («ningún pedido sale de la máquina») no se cumplió en esa corrida. Causa: tomé una sonda de una sesión como
   prueba de lo que hacen tres a la vez. Desde que lo vi no corrí ninguna sesión más.
8. **La primera regla de las tools del testigo estaba mal planteada:** pedía que cada pedido trajera exactamente el
   inventario, y cada sesión manda primero un pedido auxiliar sin tools. La corregí (ningún pedido con una tool ajena, y el
   turno con el inventario entero) y la rehice por código sobre lo capturado, sin correr nada (§11).

## 8. Contenedores, repo y copia al terminar

- **El Neo4j propio, bajado** (`down`: contenedor y red removidos), las dos veces: al terminar los doce criterios, y después
  de la prueba del testigo, para la que lo levanté de nuevo con el mismo override. Su volumen queda en la copia,
  `data/experiment/neo4j/volumen_banco_paralelo/`, con el acumulado cargado (`carga_acumulado_resumen_cegado_UBANCO_PARALELO.json`:
  20.833 nodos y 55.358 aristas en las dos cargas, idempotente, `verificar_carga` bien, KG_Meta = sha256 del kg.json
  `0435d41f…`, huellas de contenido iguales entre el cargador y Neo4j, paridad 147 de 147): el humo lo levanta con el
  mismo override.
- **`docker ps -a`:** 278 contenedores, iguales antes y después (criterio 9).
- **El repo:** HEAD `2addcf32`, `status --porcelain --untracked-files=no` vacío (`repo_al_terminar_UBANCO_PARALELO.txt`).
- **La copia** (`control_copia_final_UBANCO_PARALELO.json`): de los 25.494 archivos regulares de HEAD, 25.447 en la copia,
  todos con su blob de HEAD; fuera por regla, 46 vedados y `run_2_papers/code/.env.example`; 0 enlaces fuera del `.venv`
  clonado (3 adentro); 0 nombres vedados; los 13 archivos nuevos de la unidad (con `aislamiento/testigo_aislamiento.py`);
  los índices con su sha256. Los sellos del banco, otra vez al terminar: los mismos 2.357.
- **En `banco_paralelo/` quedan,** fuera del paquete: la copia; `sesiones/` (las raíces de las sesiones, con sus cwd vacíos
  y sus carpetas de configuración); `salidas/` (los streams, los logs R1, las metas y las transcripciones de las corridas,
  que llevan texto de la tanda 1, y las corridas archivadas); `privado_captura/` (los cuerpos capturados de la sonda y de la
  prueba del testigo, sin abrir); `comandos/`; y `revision_trabajo/`, de donde sale el paquete. Los dos `CLAUDE.md`
  plantados ya no están.

## 9. Grep de convenciones

El del repo, `data/experiment/segmentacion_oficial_e0r2/s0_4/scripts/grep_convenciones.py` (en la copia), con
`LC_ALL=en_US.UTF-8`: los tokens del nombre los toma de `git config user.name` del repo, en la consola, y la salida los
nombra `nombre_1`, `nombre_2`; ningún archivo los lleva. Sobre los 55 archivos del paquete con el agregado (con la salida
de la vuelta anterior, que había dado 0 en 48):

```
control positivo: 16 de 16 términos encontrados
archivos revisados: 55
total por término: {} — total 0
```

(`salidas/grep_convenciones_UBANCO_PARALELO.txt`). Lo corrí otra vez sobre el paquete final, con este FRENO y esa salida
(55 archivos y el `manifest.txt`): total 0.

## 10. El paquete y su copia permanente

- **El paquete:** `banco_paralelo/revision_UBANCO_PARALELO/`, 55 archivos más `manifest.txt` (sha256, ruta y una
  descripción por archivo, desde `descripciones_UBANCO_PARALELO.json`), en `codigo/`, `comandos/`, `scripts/` y `salidas/`,
  con nombres únicos con la unidad. Los scripts de `scripts/` corren desde `banco_paralelo/revision_trabajo/`, con sus
  nombres sin el sufijo (de ahí los copia `armar_paquete.py`).
- **Lo que no va al paquete** (despacho, «lo que muestran»): ninguna salida de tool, ningún log R1, stream, meta ni
  transcripción; los resultados van por sha256 y por cuentas.
- **Sus copias, con `ditto`:** en la carpeta temporal de la sesión, `<scratchpad>/revision_UBANCO_PARALELO/` (regla g del
  `CLAUDE.md` del repo), y la permanente,
  `$HOME/INGENIERIA IA/TESIS/fuera_del_repo/scratchpads/95486f81-2327-4620-90bc-f61b59d22c1a/scratchpad/revision_UBANCO_PARALELO/`.
  Verificadas contra su `manifest.txt` (`armar_manifest.py --verificar`): 55 de 55 en cada una, sin archivos de más.
- **Lo que no va al paquete del testigo:** los cuerpos capturados (traen el texto del sistema del CLI y las descripciones de
  las tools, con sus ejemplos), que quedan en `banco_paralelo/privado_captura/`; van su sha256, sus bytes y las cuentas.

## 11. El agregado v7: el testigo (criterio 13)

**El código.** `aislamiento/testigo_aislamiento.py` (`fase_testigo`), sumado a `test_aislamiento_paralelo.py` como su fase
«testigo», después de la de ejecución (con dos argumentos nuevos, `--banco-paralelo` y `--privado`). Corrí la función sola
(la prueba); la versión integrada solo la importé, sin correrla, por el FRENO de abajo.

**La sonda** (`scripts/sonda_captura_UBANCO_PARALELO.py`, una sesión de BM25, antes de escribir el control): el CLI usa la
ruta de `ANTHROPIC_BASE_URL` (`/captura/<id>/v1/messages`), manda un `HEAD /api/hello` sin clave y dos `POST` con la clave
inválida del modo init, termina por el error 400 (rc 1, `result` con `is_error`) sin `api_retry`, y deja el cwd vacío.
`lsof -i` sobre el CLI, en 353 muestras: ninguna conexión fuera de 127.0.0.1.

**La prueba** (`salidas/testigo_prueba_UBANCO_PARALELO.json`; USD 0):
- **Los testigos**, leídos por código antes de la primera tanda, sin imprimir texto: `CLAUDE.md` del repo (1.793 trechos de
  8 palabras) y `docs/preregistro_B6_3_evaluacion_final.md` (12.367), de HEAD con `git show`; `~/.claude/CLAUDE.md`, que
  existe (215); y dos `CLAUDE.md` plantados, en la raíz de las sesiones (`sesiones/testigo_prueba/`, la carpeta que
  contiene su cwd) y en `banco_paralelo/`, cada uno con un renglón con un token de `secrets.token_hex(16)`, distinto,
  escritos por código con su sha256. Trechos que la configuración de una sesión ya le da (su prompt, su bloque y las
  descripciones de sus tools, de `tools/list` por el mismo JSON de MCP) y que por eso no cuentan: 0 de cada testigo, en las
  11 sesiones.
- **Las sesiones:** 9 en tres tandas de P = 3, todas con el grafo (servidor de navegación) y fragmentos: kg, BM25 y kg;
  híbrida, kg y BM25; kg, híbrida y kg. Cada una, con la línea de comandos y el entorno de `lanzar_agente.py` en modo init
  (sus funciones; lo de su `main`, copiado): contra el comando de una sesión init del mismo brazo del lote init del test,
  la línea de comandos es igual (con el prompt, el session id y la ruta de MCP enmascarados), los nombres del entorno son
  los mismos y, fuera de los valores propios de cada sesión (`BANCO_LOG_R1`, `BANCO_SESION_TAG`, `CLAUDE_CONFIG_DIR`),
  cambia solo `ANTHROPIC_BASE_URL`: 9 de 9. Cada pregunta lleva un marcador aleatorio propio.
- **La captura:** 2 `POST` por sesión y un `HEAD /api/hello` (11 pedidos que no son `POST`, uno por sesión y por negativo);
  0 claves distintas de la inválida; 0 pedidos sin sesión. Los cuerpos quedan en `banco_paralelo/privado_captura/testigo_prueba/`,
  fuera del paquete; no los abrí ni los imprimí: por código saqué solo cuentas y sha256 (al paquete van el sha256 y los
  bytes de cada uno).
- **3.1, el positivo:** el marcador de cada sesión está en sus pedidos: 9 de 9.
- **3.2, ningún testigo llega:** 0 trechos y 0 tokens en los 18 pedidos de las 9 sesiones (en `system`, en `messages`, en
  `tools` y en lo demás), en sus streams, en lo que el CLI escribió en su carpeta de configuración (2 archivos por sesión;
  en modo init no hay transcripción, por `--no-session-persistence`) y en sus logs R1.
- **3.3, las tools:** el primer pedido de cada sesión es auxiliar (`tools: []`, sin thinking) y el segundo, el turno, trae
  exactamente las de su inventario de `system/init` (9 en el grafo, 1 en fragmentos); ninguno trae una tool ajena. Con la
  regla corregida (§7, punto 8), rehecha por código sobre lo capturado: 11 de 11 (`reanalisis_tools_testigo_UBANCO_PARALELO.json`).
- **3.4, los testigos no cambian:** el sha256 de los dos del repo (su blob de HEAD y el archivo) y el del de la cuenta,
  iguales antes y después; los dos plantados, borrados al final; el cwd, vacío en cada sesión y al final.
- **4, el negativo:** la línea de comandos de una sesión de cada brazo, copiada en la carpeta temporal, con
  `--append-system-prompt` y el renglón de un plantado (el grafo, el de la raíz de las sesiones; BM25, el de
  `banco_paralelo/`): el control 3.2 encuentra el token en el `system` de 1 de sus 2 pedidos (el turno), en los dos. Falla
  como debe, así que el testigo detecta.

**FRENO del agregado: salen pedidos de la máquina.** Mientras corrían las tandas, `lsof -i` sobre los CLI (340, 375 y 318
muestras) vio, en las tres, conexiones TCP a `160.79.104.10:443` y `34.149.66.165:443`. No son el pedido al modelo (ese
va a mi servidor, con la clave inválida), así que el costo es 0; qué llevan es NO VERIFICADO: no las intercepté ni resolví
las direcciones, para no mandar nada más. Que 160.79.104.10 sea una dirección de `api.anthropic.com` es NO VERIFICADO.
- Es el entorno del modo init del lanzador sellado (§83, §84 y §88: `PATH`, `HOME`, `NEO4J_URI` y lo del lanzador), que no
  trae nada que apague el tráfico propio del CLI, y el agregado dice que cambia solo `ANTHROPIC_BASE_URL`: no lo puedo
  apagar sin cambiar el lanzador o la lista.
- Lo mismo vale, NO VERIFICADO, para las demás corridas init del banco, incluidas las mías de la primera parte (ahí `lsof`
  miraba solo los puertos de Neo4j), y para las reales.
- La sonda no lo vio (una sesión de BM25, 353 muestras); con tres a la vez y el grafo apareció en todas las tandas. Por qué,
  NO VERIFICADO.
- **PENDIENTE de la autora:** (a) aceptar ese tráfico y leer «ningún pedido» como ningún pedido al modelo; (b) sumar al
  entorno de la sesión una variable del CLI que apague el tráfico no esencial (por ejemplo,
  `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC`; su efecto sobre estas dos conexiones, NO VERIFICADO), lo que cambia el
  lanzador sellado y la lista de la §88 y pide su propio despacho; o (c) correr el testigo con la red del CLI cortada. Hasta
  que decida, no corro la versión integrada ni ninguna sesión más.

**FRENO: espero la revisión de la mesa.**
