# FRENO B6.3-b2 — la configuración sellada de B6.3, el testigo con ella, lo fijo y el pico, el juez fuera del repo y la salida que no se lee (28/10/2026)

Unidad: B6.3, etapa b2 del runner. Costó USD 0. Ninguna sesión llegó al modelo: el init apunta a un puerto cerrado y el testigo, a su
servidor de captura local (`ningun_pedido_al_modelo_sale_de_la_maquina: true`, `claves_distintas_de_la_invalida: 0`; §3).

En el repo escribí solo archivos nuevos: 23 en `data/experiment/banco_mcp/b63/v2/b2/` (22 y su lista de sha256), 2 en `aislamiento/` y
este FRENO. No edité nada de HEAD, de la b1 ni de la b1 bis. No commiteé nada. Espero la revisión.

**Lo que hay que decidir** (§12):
- **El testigo con la configuración de B6.3 no da PASS.** Una ventana de 8 palabras de la nota de la config de fragmentos llega al
  `log_r1` del servidor, que registra su config al arrancar; esa misma ventana está en el pre-registro. No llega a ningún pedido al
  modelo (§3).
- **La P.** La regla del despacho, con los picos medidos, da P = 2. Pero esos picos no traen el codificador: las sesiones del testigo
  terminan antes de cargarlo. Con la cifra de N6 a, lo fijo de después del reinicio deja P = 1 con 0,045 GB de margen, sin contar el
  CLI de cada sesión (§4).

Los artefactos largos van en el paquete `revision_B63_FRENO_b2/` (§13), por su nombre.

## 0. Los criterios

| # | criterio | dónde | resultado |
|---|---|---|---|
| 1 | el paso 0, con lo restaurado, Docker y la huella | §1 | lo esperado, antes y después del reinicio; restaurado 81 de 81 y 46 de 46 |
| 2 | la configuración: tres brazos, cada sha256 contra N7 | §2 | 12 de 12; `config_agentes_b63.json` `eaff32bb…` |
| 3 | el testigo: diff contra HEAD, selftest, controles, init, `PASS_de_B63` y `PASS_del_testigo_tal_cual` | §3 | diff solo en la configuración; selftest 3 de 3; los controles dan; **el testigo da FAIL**: `PASS_de_B63` false y `PASS_del_testigo_tal_cual` false |
| 4 | la memoria: lo fijo, el pico de cada brazo, el swap y la P | §4 | lo fijo 9,89 GB; picos 0,768, 0,556 y 0,33 GB; swap 0,0 y 0,0; la regla da P = 2, sobre picos sin el codificador |
| 5 | el juez fuera del repo, con sus pruebas | §5 | por defecto, fuera; dentro del repo frena con el 10; el manifiesto, sin texto |
| 6 | la salida que no se lee | §6 | en `errores_r{rep}.jsonl`, sin reintento; en la caché, por la clave; la lectura tolerante, un veredicto por criterio |
| 7 | el selftest, dos veces iguales, y la corrida en seco | §7 | 34 de 34 dos veces, iguales; 3 de 3 dos veces, iguales; corrida en seco 15 de 15, con la guarda antes |
| 8 | lo que lancé | §8 | ningún script del patrón fuera de la corrida en seco; la lista, por nombre |
| 9 | el repo: solo archivos nuevos, con su sha256; lo demás, igual; el grep, 0 | §9 y §13 | 26 nuevos; 60.290 entradas comparadas, 0 cambian; grep 0 |

Hubo errores propios (§10). Cuatro tocan reglas del despacho: la contraseña del Neo4j en la consola (1), renglones del pre-registro en
la consola (2) y tres búsquedas sin `--exclude-dir` (6 y 7).

## 1. El paso 0, antes y después del reinicio

**Antes** (`paso0_B63_b2.txt`, 07:55:34; `paso0_b2.zsh`):
- el scratchpad: `revision_B63_FRENO_b1_bis/` da 81 de 81 contra su `manifest.txt` (`2c866df7…`), igual al de la copia permanente;
- `pwd`: `$HOME/INGENIERIA IA/TESIS/bcra-regulatory-kg`;
- HEAD `1d1ff7f4`, con `83b45bfc` en su historia;
- `n7/n7_configuracion_sellada.json` da `dd425094…` en HEAD y en el árbol;
- los asuntos desde `23559e51`: `1d1ff7f4`, `65e63e11` y `83b45bfc`;
- `git status --porcelain --untracked-files=no`, con las vedadas podadas, vacío;
- en `b63/`, 41 sin rastrear, que dan `28408815…`; las listas de la b1 y de la b1 bis, OK;
- Docker, solo por nombre:
  - la VM, 2.524.311.552 bytes (el tope es 2.684.354.560);
  - `neo4j-bcra-kg-indices-eval`, running y healthy;
  - `neo4j-bcra-kg-n6`, no corre;
- la huella (`control_neo4j_b63.py` sobre 47687): `2645da6d…`, 37.168 nodos y 128.552 aristas, rc 0.

**El reinicio.** Antes de la corrida real medí lo fijo: 12,48 GB (§4). La autora decidió reiniciar. Antes del reinicio copié con `ditto`
a `fuera_del_repo/scratchpads/d7b988e9-…/scratchpad/b2_antes_del_reinicio/` lo de la b2 que estaba en el scratchpad y no en el repo.
Excluí las copias del repo (c1 y s1) y sus carpetas de trabajo, que traen carpetas `desanonimizacion_SOLO_MESA` de juguete. En la
copia verifiqué 46 de 46 contra su manifiesto (`2551ff70…`).

**Después.** La máquina arrancó a las 10:02:46 (`sysctl kern.boottime`) y el scratchpad estaba vacío.
- La restauración (`restauracion_despues_del_reinicio_B63b2.txt`, 10:06:28):
  - `revision_B63_FRENO_b1_bis/`, 81 de 81;
  - `b2/` y el checkpoint, 46 de 46;
  - `armar_manifest.py` y `enmascarar_paquete.py` del paquete de la etapa a, con su sha256 (`5a7db724…` y `65eaf9a2…`).
- Los controles (`control_post_reinicio_B63_b2.txt`, 10:07:04; `control_post_reinicio_b2.zsh`):
  - lo mismo que el paso 0;
  - en `b63/`, 63 sin rastrear: sin `b63/v2/b2`, los 41 que dan `28408815…`, como en el paso 0; en `b2/`, los 22 de la lista congelada;
  - en `aislamiento/`, solo los dos nuevos;
  - los 24 nuevos contra `b2_congelado.sha256` (`28152f7e…`), 24 de 24;
  - Docker y la huella, lo mismo que antes.

Antes de medir no corrí nada más.

## 2. La configuración de agentes de B6.3

`armar_config_agentes_b63.py` arma `config_agentes_b63.json` (`eaff32bbad93cb9bc1f9d66ea2c4887cba8268f71007be6bb7158cc97bf0d0c4`) desde
el registro de N7, y la controla.

**Los 12 sha256, contra el registro de N7, 12 de 12** (`config_agentes_controles_n7_B63b2.json`):
- el registro mismo (`dd425094…`);
- `n6/analisis/analisis_n6_con_lectura_tolerante.json`;
- los 5 de `n7/`: la config y el JSON de MCP del grafo, los dos bloques y la plantilla;
- el manifiesto del índice por punto;
- la config y el JSON de MCP de la híbrida y del denso.

`--verificar` rearma el JSON y da el del archivo.

**Los brazos:**

| brazo | rol | JSON de MCP | bloque | config del servidor |
|---|---|---|---|---|
| `kg` | grafo | `n7/mcp_kg_n7_evaluado.json` | `n7/bloque_tools_kg_n7.txt` | `n7/config_mcp_kg_n7_evaluado.json` |
| `fragmentos_hibrida` | fragmentos_principal | `mcp_vector/mcp_fragmentos_hibrida_evaluado.json` | `n7/bloque_tools_fragmentos_n7.txt` | `mcp_vector/config_fragmentos_hibrida_evaluado_r2b.json` |
| `fragmentos_denso` | fragmentos_denso | `mcp_vector/mcp_fragmentos_denso_evaluado.json` | `agentes/bloque_tools_vector.txt` | `mcp_vector/config_fragmentos_denso_evaluado_r2b.json` |

Lo común a los tres brazos:
- la plantilla `n7/plantilla_prompt_n7.txt` (`822aa4e7…`);
- el R5 del registro de N7: 32 turnos, 30 herramientas en el prompt y USD 1,80 por sesión;
- `NEO4J_URI` en `bolt://127.0.0.1:47687`, `MCP_TIMEOUT` 180000;
- la forma de `paralelo/config_agentes_n6_prueba.json`.

## 3. El testigo con la configuración de B6.3

**El testigo nuevo.** `aislamiento/testigo_aislamiento_b63.py` es `testigo_aislamiento.py` de HEAD (`e600e187…`), +52 −8
(`diff_testigo_aislamiento_b63_b2_contra_HEAD_B63b2.diff`). Cambia solo en la configuración:
- `--config-agentes` y `--sha256-config`: frena si la configuración no da su sha256; sin ellos, usa la de prueba de N6, como HEAD;
- el plan sale de la configuración:
  - con la de N6, las tandas, los negativos y el brazo exigido de HEAD;
  - con otra, una sesión a la vez, dos vueltas por sus brazos, los negativos sobre el rol grafo y el rol fragmentos_principal, y ningún
    brazo exigido en cada tanda;
- el resultado nombra la configuración.

**Su selftest** (`selftest_testigo_aislamiento_b63.py`): 3 de 3, dos veces, iguales (§7).
- la configuración: sin parámetro, la de N6; con la de B6.3, la de B6.3; con otro sha256, frena;
- el plan: con la de N6, el de HEAD; con la de B6.3, 6 tandas de una sesión;
- la comparación con un init sintético, en los 3 brazos:
  - positivo: la sesión tal cual da PASS, con `ANTHROPIC_BASE_URL` como único valor distinto;
  - negativos: con otro `mcp_config`, o con una variable más, no da PASS.

**La corrida real** (`medir_testigo_b63.py`, desde la raíz del repo, con `env -i` PATH, HOME, `NEO4J_URI` en 47687 y `BANCO_VENV_VECTOR`,
sin ninguna clave; de 10:07:35 a 10:08:57; `medir_testigo_resultado_B63b2.json`):
- **la guarda**, con `PATRON_B1`: ningún paso pago corriendo;
- **Docker**:
  - la VM, 2.524.311.552 bytes, por debajo del tope de 2.684.354.560;
  - el contenedor, healthy, con 1,466 GiB de 2,351 GiB;
- **la huella**, `2645da6d…`;
- **el init**, con la configuración de B6.3 y una entrada DE TESTIGO (`ba19cbb0…`, preguntas de juguete, P = 1):
  - código 0;
  - las 3 sesiones con `PREGUNTA_INIT`, terminadas, rc 0;
  - el CLI 2.1.241, la versión sellada de la configuración;
- **el testigo**, de a una sesión:
  - 6 sesiones y 2 negativos;
  - cada sesión: `tools_PASS` y la comparación con el init, true;
  - los dos negativos, `FALLA_COMO_DEBE`;
  - `ningun_pedido_al_modelo_sale_de_la_maquina`, true;
  - `claves_distintas_de_la_invalida`, 0;
- **el control negativo de la comparación, sobre el init real**, en los 3 brazos: sin cambios, PASS; con otro `mcp_config` o una variable
  más, no da PASS;
- **las otras conexiones de los CLI**, declaradas como en U-BANCO-PARALELO-b (`paralelo/FRENO_UBANCO_PARALELO_b.md:157`), solo por
  dirección, puerto y muestras de `lsof`: `160.79.104.10:443` (1.594) y `34.149.66.165:443` (176).

**`leer_testigo`: `PASS_de_B63` false y `PASS_del_testigo_tal_cual` false.** El testigo da 16 renglones de FRENO:
- 12 son de la fecha, en `system` y `messages` de las 6 sesiones, declarados (§9 de la etapa a);
- 4 son «llega un testigo», uno en cada sesión de fragmentos: T2 y T5 de la híbrida, T3 y T6 del denso. Las del grafo, ninguno.

Dónde llega, por sesión (`testigo_resultado_B63b2.json`, `por_sesion`):

| lugar | sesiones de fragmentos | sesiones del grafo |
|---|---|---|
| campos de los pedidos (`system`, `messages`, `tools` y `otros`) | 0 | 0 |
| stream | 0 | 0 |
| carpeta de configuración | 0 | 0 |
| `log_r1` | 1, de `repo:docs/preregistro_B6_3_evaluacion_final.md` | 0 |

**Lo que llega, por su lugar en el registro** (`diagnostico_testigo_log_r1_B63b2.txt`; leí el pre-registro de HEAD en el proceso, sin
imprimir su texto):
- el renglón `inicio` del `log_r1`: el servidor de fragmentos registra ahí su config entera al arrancar;
- en el campo `config.nota` de las dos configs de fragmentos: la de la híbrida tiene 705 caracteres y la del denso, 549;
- es una sola ventana de 8 palabras, la misma en las dos. Tal como está en la nota, normalizada: «sobre el manifiesto de e del grafo
  evaluado» (la normalización saca los dígitos de «E0»);
- también está en el `log_r1` del negativo de la híbrida y en los dos del cliente que lee las descripciones (híbrida y denso); esos
  tres no cuentan para el FRENO.

**De dónde sale:**
- el pre-registro la trae desde su primer commit (`53b4f535`, 25/10 13:37) y en sus 7 versiones, incluida la firmada (`adf20f3b`);
- las dos configs entraron después, en `6b3dd5ab` (27/10 10:22);
- la nota de la config del grafo no comparte ninguna ventana con el pre-registro.

Es una frase técnica que comparten la nota y el pre-registro, porque describen el mismo índice. No es contenido del pre-registro que
haya entrado a la sesión: el modelo no la ve, y el servidor la escribe en su propio registro. El testigo de HEAD solo excluye los trechos
del prompt, del bloque y de las descripciones. Las configs de servidor de la configuración de prueba de N6 (las tres) y la del grafo de
B6.3 no comparten ninguna ventana con el pre-registro de HEAD (punto 4 del diagnóstico).

No toqué la lógica del testigo ni de `leer_testigo`, ni la nota de la config (que es sellada). La decisión va en el §12.

## 4. La memoria: lo fijo, el pico y la P

**Lo fijo de antes del reinicio, DESCARTADA** (`fijo_antes_del_reinicio_B63b2.txt`): 12,48 GB en uso y 1,004 de swap, a las 08:30:19.
- La causa: la medí con aplicaciones abiertas y sin reiniciar. La decisión 4 pide lo fijo después del reinicio y antes de lanzar.
- Con 4,0 GB por sesión, la regla daba P = 0.
- La memoria que registraron los scripts de la copia mientras corrían el selftest y la corrida en seco (de 12,055 a 12,743 GB) también
  es de antes del reinicio. Ninguna entra en la P.

**Después del reinicio**, con la app de Claude como única aplicación abierta (dicho por la autora; NO VERIFICADO por mí):
- **lo fijo**, por el comando (`comando_b63.zsh medir`, con `env -i`), antes del init: 9,89 GB en uso y 0,0 de swap
  (`medir_testigo_resultado_B63b2.json`, `fijo.memoria`);
- **el swap**: antes 0,0, después 0,0, y 0,0 en las 921 muestras;
- **el pico de la huella física del árbol de cada sesión** (CLI, Node y servidor; `footprint -p`):

| brazo | pico | sesiones con muestras | duración de cada sesión |
|---|---|---|---|
| `kg` | 0,768 GB | 4 | de 3,7 a 4,5 s |
| `fragmentos_hibrida` | 0,556 GB | 4 | de 7,3 a 8,9 s |
| `fragmentos_denso` | 0,330 GB | 3 | de 0,9 a 1,3 s |

  El detalle por sesión, en `medir_testigo_resultado_B63b2.json` (`memoria.por_sesion`) y `muestras_memoria_B63b2.json`;
- **la regla del despacho** (`memoria_b63.regla_P`): 9,89 + 2 × 0,768 = 11,426 ≤ 14,5, así que da P = 2.

**Esa P no vale para las sesiones que cargan el codificador.**
- Las sesiones del init y del testigo no hacen ninguna llamada a herramientas y terminan en segundos.
- El servidor del grafo lanza el codificador al arrancar, pero el modelo recién queda cargado después de una consulta (así mide N6:
  `n6/memoria_n6.py`, docstring).
- Por eso ningún pico de hoy trae el codificador. El de los fragmentos no lo iba a traer de ningún modo, porque lo cargan en la primera
  llamada.
- Hay un error propio de diseño (§10, error 5).

**La cuenta con la cifra de N6 a** (registro, §135 y §136, `docs/registro_decisiones_calidad_y_evaluacion_2026-10-15.md:6027-6063`).
Cada sesión con su codificador ocupa 4,565 GB. Con eso:
- P = 2 pide lo fijo en 5,37 GB o menos: 9,89 no entra;
- P = 1 pide lo fijo en 9,935 GB o menos, sin el CLI de cada sesión: 9,89 entra por 0,045 GB (9,89 + 4,565 = 14,455);
- con el CLI y el Node de cada sesión no está verificado que entre: la medición de hoy no los separa del servidor.

La decisión 4 dice: «1, o 2 si lo fijo queda en 5,4 GB o menos con tu cuenta». La decisión 3 del §135 dice: «Si la memoria medida en
el testigo no da ni para P = 1, lo hablamos». La P la decide la autora (§12).

**Un dato más, con causa NO VERIFICADA** (`memoria_por_ventana_B63b2.txt`).
- En las tres sesiones de la híbrida del testigo (T2, T5 y el negativo), la memoria en uso de la máquina sube unos 4 GB dentro de la
  ventana de la sesión, mientras el árbol queda en 0,5 GB:
  - T2: de 9,145 a 13,207;
  - T5: de 8,907 a 13,003;
  - el negativo: de 8,844 a 13,090.
- En la híbrida del init no pasa (de 9,593 a 9,954), ni en las del grafo o del denso.
- El máximo de las muestras, 13,207 GB, está en la ventana de T2.
- La huella del árbol no lo ve. Que sean páginas de los archivos del índice contadas como activas es una hipótesis, NO VERIFICADA.

## 5. El juez fuera del repo

- **El directorio por defecto:** `JUEZ_DIR = fuera_del_repo/banco_b63/juez`, con su caché, al lado de `RESULTADOS` (`comun_b63.py`).
- **En modo real**, `CorridaB63.correr` frena con el 10, antes de escribir nada, si `--juez-dir` está en el repo o en git
  (`correr_b63.py`).
- **`manifiesto_fuera`:**
  - cada archivo de `--out` y de `--juez-dir` va con su ruta relativa a `fuera_del_repo/`, su tamaño y su sha256;
  - un `*_SOLO_MESA*` o `NO_ABRIR_*`, solo con su tamaño y su fecha;
  - una carpeta con esos nombres, solo por su nombre, sin bajar a ella;
  - los enlaces, sin seguirlos.
- **Sus pruebas**, en el selftest (casos 29 a 31; §7):
  - con el directorio por defecto, la corrida de juguete no escribe nada en el repo, y quedan 3 archivos de veredictos fuera;
  - con un `--juez-dir` dentro del repo frena con el 10;
  - el manifiesto: 43 archivos, los 8 del juez con su sha256, 1 carpeta por nombre (la `desanonimizacion_SOLO_MESA`) y 0 ventanas de 30
    caracteres de la pregunta, el criterio o la respuesta de juguete. El control positivo: las tres fuentes sí están en los archivos.
- **En la corrida en seco**, la rama S14 repite el freno con el 10 y, con el juez en una carpeta de la misma forma que
  `fuera_del_repo/banco_b63/`, la corrida que no escribe en el repo y el manifiesto, con los mismos resultados.

## 6. La salida que no se lee

**El caso.** Con el juez simulado, una respuesta que trae la marca `[[juez:comillas]]` recibe una salida con un JSON roto: comillas sin
escapar en «fragmento».

**Lo que pasa** (selftest, caso 32; corrida en seco, S15, con SEC10 y el plan `juez_comillas` del CLI falso):
- la salida queda en `errores_r{rep}.jsonl` con su id opaco y su repetición;
- no se escribe ningún veredicto;
- al retomar no se reintenta: en S15, 9 pedidos y 0 más;
- la salida cruda está en la caché, que abro en solo lectura (un `UPDATE` falla). La encuentro por la clave del pedido:
  `llm_cache.compute_key` con el namespace de la repetición, y `canonical_request` de `juez.construir_kwargs`;
- la lectura estricta no la lee;
- `lectura_tolerante_juez.leer`, de HEAD sin editar, da un veredicto por criterio: `cumplido, cumplido, no_cumplido` en el selftest, y
  9 de 9 en S15;
- `aplica` da true con `end_turn`.

Esta etapa no aplica la lectura tolerante. Solo prueba que se va a poder aplicar.

## 7. El selftest y la corrida en seco

**El selftest** (`copia_y_selftest_b2.zsh`; copia c1, de 08:20:38 a 08:24:46; `copia_selftest_c1_B63b2.txt`):
- la copia: 2.837 archivos, sin `.env`, `NO_ABRIR_`, `*_SOLO_MESA*`, enlaces ni `.git`, igual al repo por sha256. Es
  `banco_mcp` sin `a2_2/adjudicacion`, más `ev2_juez` y los `.py` del primer nivel de `evaluacion`;
- **el de la b2**: 34 de 34 en PASS, dos veces, iguales byte a byte;
  - son los 28 de la b1 bis, con las rutas de la b2, y 6 nuevos (casos 28 a 33): la configuración, el juez fuera por defecto,
    `--juez-dir` dentro del repo, el manifiesto, la salida que no se lee y la memoria del testigo (árbol, ventanas, picos y la regla con
    2, 1 y 0);
- **el del testigo**: 3 de 3, dos veces, iguales;
- lo copiado del repo, antes y después: igual. `.pyc` en la copia: 0.

Fue el único intento: no hubo fallas.

**La corrida en seco** (`copia_y_seco_b2.zsh`; copia s1, de 08:24:57 a 08:29:54; `corrida_en_seco_consola_B63b2.txt` y
`corrida_en_seco_resultado_B63b2.json`):
- **su guarda**, antes de todo, con `PATRON_B1`: no vio ningún paso pago;
- **el resultado**: 15 de 15 en PASS, en una sola corrida;
  - S1 a S13, las de la b1 bis;
  - S14, el juez fuera del repo;
  - S15, la salida que no se lee;
- lo copiado del repo, antes y después: igual.

Va por el mismo camino de imports que la corrida real, sin arreglar el `sys.path` por fuera. Su entrada de juguete usa las
configuraciones de juguete de la etapa a (brazos `kg`, `fragmentos_bm25` y `fragmentos_denso`). La configuración de B6.3 la prueban el
selftest (una entrada con ella pasa los controles del runner) y el testigo real.

## 8. Lo que lancé

Ningún proceso mío corrió un script del patrón, salvo los dos `correr_b63.py` de la rama S12 de la corrida en seco, después de su
guarda: el que lanza el comando y el que se lanza sin él. No hice ninguna llamada a la API ni nada pago. No levanté, paré ni reinicié
ningún Neo4j, ni toqué su volumen. Lo único que listé de Docker son los dos contenedores, por nombre.

- **Los míos, en el scratchpad:**
  - `paso0_b2.zsh` y `control_post_reinicio_b2.zsh`, con `control_neo4j_b63.py` de la b1 bis y de la b2;
  - `foto_repo_b1v2.py`, para la foto antes y la foto después, y `comparar_fotos_b1.py`;
  - `copia_y_selftest_b2.zsh` y `copia_y_seco_b2.zsh`, una vez cada uno, con `rsync`, `find`, `shasum` y `du`;
  - `diffs_b2.py`;
  - `diagnostico_testigo_log_r1_b2.py` y `memoria_por_ventana_b2.py`, que solo leen. Primero los corrí en línea y después desde su
    archivo, con la misma salida byte a byte;
  - `armar_manifest.py`, `enmascarar_paquete.py` y el `grep_convenciones.py` de HEAD.
- **En el repo:**
  - `armar_config_agentes_b63.py`, con y sin `--verificar`;
  - `medir_testigo_b63.py`, una vez.
- **Lo que lanzó `medir_testigo_b63.py`:**
  - un `pgrep` con `PATRON_B1`, el real;
  - `docker info`, `docker inspect` y `docker stats`, solo del contenedor de los índices (`docker_b63.control`);
  - `control_neo4j_b63.estado`, en el proceso;
  - `zsh comando_b63.zsh medir`, que corre `memoria_b63.py`;
  - el lote init en el proceso (`lote_init`), con `lanzar_agente_b63.py`, el `claude` real en modo init y los servidores MCP de los tres
    brazos (`servidor_mcp_kg_nav_cand.py` y `servidor_mcp_vector.py`);
  - `testigo_aislamiento_b63.py`, que lanzó el `claude` real con los mismos servidores, su cliente que lee las descripciones de las
    herramientas y `lsof`;
  - `footprint`, `ps`, `vm_stat` y `sysctl`, desde el muestreo.
- **Lo que lanzaron el selftest y la corrida en seco:** lo de la b1 bis (§12 de su FRENO), con los archivos de la b2. Además:
  - el `claude` falso, con el plan `juez_comillas`;
  - en el selftest del testigo, nada: arma las sesiones sin correrlas.
- **Lo demás:**
  - `git`, con las vedadas podadas por ruta y `*_SOLO_MESA*`/`NO_ABRIR_*` por nombre: `status`, `log`, `rev-parse`, `merge-base` y `show`;
  - búsquedas con `grep -r`, con un `--exclude-dir` para `adjudicacion`, `*_SOLO_MESA*` y `NO_ABRIR_*`, salvo las de los errores 6 y
    7 del §10:
    - una con `-n` sobre los `.py` de `aislamiento`, `n6`, `agentes` y `b63/v2/b2`, la del venv de fragmentos;
    - dos con `-l`, que imprimieron solo nombres de archivo: la de las otras conexiones, sobre `banco_mcp` y `docs`, y la del pico de
      N6, sobre `n6` y `docs`;
    - una con `-n` sobre los `.md` de `docs`, `n6` y `n7`, sin el pre-registro ni la tesis, filtrada a renglones de memoria;
  - `find` sobre el scratchpad y sobre `fuera_del_repo/scratchpads/` (hasta 3 niveles), con `*_SOLO_MESA*` y `NO_ABRIR_*` podados
    por nombre;
  - `ditto`, `stat`, `date` y `sysctl`.

**La carpeta temporal del sistema:** no escribí nada fuera del scratchpad. El testigo escribió sus salidas, la captura y los plantados en
su `--tmp`, también en el scratchpad.

## 9. El repo

- **Lo nuevo:**
  - en `b63/v2/b2/`, 22 archivos y su lista `sha256_etapa_b2_b63.txt`, que tiene 24 renglones (`shasum -c` OK; `28152f7e…`); los 2
    renglones de más son los de `aislamiento/`;
  - en `aislamiento/`, `testigo_aislamiento_b63.py` y `selftest_testigo_aislamiento_b63.py`;
  - este FRENO.
- **Los diffs** (`diffs_B63b2.txt`): 19 archivos contra su original y 5 sin original.
  - 18 contra el de la b1 bis, con su sha256 de la lista de la b1 bis OK. De ellos, 9 son iguales byte a byte: `ventana`, `juez`,
    `memoria`, `docker`, `control_neo4j`, `formas_reales`, el lanzador falso, los planes de la b1 bis y las preguntas de la meta;
  - 1 contra HEAD: el testigo;
  - los 5 sin original: `armar_config_agentes_b63.py`, `config_agentes_b63.json`, `medir_testigo_b63.py`, `seco/planes_b63_seco_b2.json`
    y el selftest del testigo.
- **Al cierre** (`repo_al_cierre_B63b2.txt`): en `b63/` hay 65 sin rastrear, que son los 41 del paso 0, los 23 de `b2/` y este FRENO.
  En `b63/` y `aislamiento/` no hay ningún `.pyc` ni `__pycache__`.
- **Lo que no cambió:**
  - nada de HEAD: `git status --porcelain --untracked-files=no`, con las vedadas podadas, vacío;
  - en `b63/` fuera de `b63/v2/b2` y de este FRENO, los 41 del paso 0, con el mismo sha256;
  - los 24 nuevos, iguales a la lista congelada antes del reinicio.
- **Las fotos** (`foto_repo_b1v2.py`; `foto_despues_B63_b2.txt`). La foto antes es de las 07:55:56 y la foto después, de 10:14:03 a
  10:14:21. Las dos tienen HEAD en `1d1ff7f4` y entre los dos HEAD no hay ningún commit.
  - 60.290 entradas comparadas, 0 cambian, 0 solo en la antes;
  - 2 solo en la después, los dos nuevos de `aislamiento/`;
  - las 13 podadas, iguales;
  - `.pyc` fuera de los venvs: 237 y 237.
- **Fuera del repo:** no escribí en `fuera_del_repo/banco_b63/`. Las únicas escrituras fuera del repo y del scratchpad son las copias
  permanentes (§1 y §13).

## 10. Errores propios, con su causa

1. **Imprimí en la consola de la sesión la contraseña por defecto del Neo4j.** Salió en la salida de un `sed` sobre el docstring de
   `data/experiment/neo4j/conexion.py`. Mi filtro sacaba solo el renglón de la asignación, y la contraseña también estaba en el
   docstring. No está en ningún archivo que escribí y no la repito acá.
2. **Un `grep` del pre-registro por «bloque» mostró en la consola renglones con ids de preguntas y anclas de B6.3** (renglones 200, 451 y
   767). No mostró texto de preguntas, criterios ni citas. La causa: busqué el bloque del denso con un `grep` sobre el archivo entero,
   en lugar de una búsqueda que imprimiera solo números de renglón.
3. **`ls -p` de `data/experiment/neo4j` mostró el nombre de la carpeta `volumen/`.** No entré.
4. **La primera restauración no corrió:** su salida apuntaba a una carpeta que la misma restauración creaba. La repetí con la salida en
   la raíz del scratchpad.
5. **El diseño de la medición del pico.** Supuse que el pico del brazo del grafo en el testigo iba a traer el codificador, porque el
   servidor lo lanza al arrancar. No lo verifiqué contra `n6/memoria_n6.py`, que para tenerlo cargado le hace una consulta. Las
   sesiones del testigo terminan sin ninguna llamada, así que la regla aplicada a esos picos da una P que no es la de las sesiones con
   codificador (§4).
6. **Un `grep -rl` sin `--exclude-dir`**, sobre `n6`, `agentes`, `b63/v2/b2` y `b63/v2/b1bis`, buscando dónde se lee el venv de
   fragmentos. Imprimió solo nombres de archivo. En esas cuatro carpetas no hay ningún `*_SOLO_MESA*` ni `NO_ABRIR_*`, ni ninguna vedada
   por ruta: lo controlé después, por nombre con `find`, y dio 0. La causa: lo armé como una búsqueda chica y no le puse los
   `--exclude-dir` que pide el punto 8.
7. **Dos `grep -r` sin `--exclude-dir` sobre la carpeta `b1bis/` del scratchpad**, antes del reinicio, buscando la ruta del venv de
   fragmentos. Imprimieron solo los tramos que coinciden con la variable, con su cuenta. Que esa carpeta trajera carpetas
   `desanonimizacion_SOLO_MESA` de juguete, de los selftests de la b1 bis, es probable y NO VERIFICADO: el reinicio la borró, y no la
   restauré porque la b2 no la necesita. La causa es la misma del error 6.
8. **El primer intento de guardar los dos diagnósticos como archivos** los sacaba del transcript de esta sesión (`~/.claude/projects/…`,
   solo lectura), y tomó el mismo bloque para los dos. Su comparación dio distinta y borré esas salidas. Escribí los dos archivos con el
   código que había corrido, y desde ellos la salida es la misma. No escribí nada en `~/.claude/`.

## 11. Declaraciones

- **La guarda del gasto** cuenta 1,80 por la sesión de la clave inválida. El comando pasa `ANTHROPIC_API_KEY` sin imprimirla.
  Decisión de la autora del 28/10/2026, 07:27:21: «Lo demás de su §14 queda como está y se declara».
- **El bloque del denso** es `agentes/bloque_tools_vector.txt`, el de A2.1. El registro de N7 no lo nombra: lo tomé de A2.1. Que sea el
  de B6.3 está NO VERIFICADO por la autora.
- **Los nombres de los brazos de B6.3** son `kg`, `fragmentos_hibrida` y `fragmentos_denso`. La entrada sellada real, que arma la mesa,
  tiene que usarlos.
- **La lectura del pre-registro.**
  - El testigo de HEAD lee en el proceso los dos testigos del repo (`CLAUDE.md` y el pre-registro) para buscar sus trechos; no los
    imprime.
  - Mi diagnóstico del §3 leyó el pre-registro de HEAD y sus 7 versiones con `git show`, en el proceso. Imprimió solo cuentas, rutas de
    campos y la ventana común tal como está en la nota de la config.
- **La captura privada del testigo** (`testigo_privado_captura/`, los pedidos HTTP completos de las sesiones) no va al paquete. Queda en
  el scratchpad, que macOS limpia a los 3 días.
- **La corrida real y el init corrieron desde la raíz del repo**, porque los servidores leen el grafo y los índices del repo. Sus salidas
  van en el scratchpad. El repo lo controlan las fotos y la lista congelada.
- **El estado de la máquina después del reinicio** (solo la app de Claude abierta, Docker y el Neo4j de los índices arriba) es lo que
  dijo la autora; no lo verifiqué más allá de Docker y la huella.

## 12. Lo que queda para la autora (PENDIENTE)

1. **El testigo de B6.3 no da PASS**, por la ventana de la nota de la config de fragmentos que llega al `log_r1` (§3). Las opciones que
   veo, sin elegir ninguna:
   - a. declararlo como la fecha: la ventana sale de la config sellada, la escribe el servidor en su registro y no llega a ningún pedido;
   - b. una versión del testigo que excluya también los trechos de la config del servidor de cada brazo, con su selftest (cambia la
     lógica del testigo; pide mandato);
   - c. un `log_r1` sin la nota (cambia el servidor; pide mandato).
2. **La P de B6.3** (§4): la regla del despacho da P = 2 sobre picos sin el codificador. Con la cifra de N6 a, P = 1 entra por 0,045 GB
   sin el CLI. Medir el pico de una sesión con el codificador cargado pide una consulta a las herramientas, que estas sesiones no hacen.
3. **Los commits** de la b2: PENDIENTES, de la autora.
4. **La entrada sellada real** la arma la mesa (§11, los nombres de los brazos).

## 13. El grep de convenciones y el paquete

**El grep de convenciones.** Corrí `segmentacion_oficial_e0r2/s0_4/scripts/grep_convenciones.py` de HEAD, con `LC_ALL=en_US.UTF-8`, sobre
copias de los 25 archivos que escribí en el repo antes de este FRENO y de los 7 scripts del scratchpad que había entonces
(`grep_convenciones_b2_y_scripts_B63b2.txt`):
- control positivo: 16 de 16 términos;
- archivos revisados: 32;
- total por término: {} — total 0.

Al cerrar lo corro otra vez, sobre este FRENO y el paquete enmascarado. El resultado va en el reporte del cierre.

**El paquete:** `revision_B63_FRENO_b2/`, en el scratchpad de esta sesión, con nombres únicos y su `manifest.txt` (sha256 y una línea por
archivo). Trae:
- lo que escribí: los 23 de `b2/` como `b2__*`, los 2 de `aislamiento/` como `aislamiento__*` y los scripts como `script__*`;
- los diffs y los controles;
- las salidas del selftest, de la corrida en seco y de la corrida real, enmascaradas;
- las fotos, enmascaradas;
- un `tar.gz` de las salidas del testigo y del init, sin la captura privada.

Lo copio con `ditto` a `~/INGENIERIA IA/TESIS/fuera_del_repo/scratchpads/d7b988e9-4130-42c4-b289-914468756f63/scratchpad/` y verifico en
la copia los sha256 de su manifiesto. La ruta y el resultado van en el reporte del cierre.
