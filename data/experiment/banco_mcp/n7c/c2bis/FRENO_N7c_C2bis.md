# FRENO de N7c, etapa C2-bis

30/10/2026. USD 0: ninguna llamada a la API y ninguna sesión real. Del repo leí con `git -C <repo> --no-optional-locks` (`log`,
`show`, `diff --name-only`, `status`) y `git archive HEAD`, salvo lo declarado abajo (el kg.json del grafo evaluado, leído en su
lugar para B1, y el python del `.venv`). No escribí en el repo ni en el Neo4j y no commiteé. Rutas con la carpeta personal como
`$HOME`; `R` es `$HOME/INGENIERIA IA/TESIS/bcra-regulatory-kg`; las rutas de la copia y de `preparado/` son relativas a
`data/experiment/banco_mcp/` salvo aviso. El detalle de cada paso está en `checkpoint_C2bis.md`.

**Resultado:** las dos partes, hechas y en verde. La parte A: N7c+ (`mcp_kg/familias_nav_rel_amp.py`), su servidor y su
configuración, sus pruebas (47 de 47, dos veces iguales; 17 mutaciones, las 17 detectadas) y B1 (prefijo, familia y cita en los
3.194 puntos; el techo da 8, lo mismo que midió la mesa). La parte B: el runner con los siete cambios y el lanzador (el octavo),
las dos configuraciones de agentes, las dos entradas, los controles de los servidores y del humo, el seco (66 de 66 en PASS, dos veces), el análisis
con su prueba (16 de 16) y los tres comandos PREPARADOS. La lista del 241: 54 archivos, 0 rutas en HEAD.
**Una decisión que la mesa tiene que mirar:** N7c+ va con la clave `N7c_amp` en la configuración de agentes, las entradas y los
ids de sesión, porque `+` no es válido en un id (`agentes/lanzar_lote_paralelo.py:74`); su nombre, «N7c+», va en `nombres` y en
lo que imprime el análisis.

## Paso 0

```
pwd: $HOME/INGENIERIA IA/TESIS/fuera_del_repo/unav_n7c_c2bis   (ls -A | wc -l: 0, vacía)
HEAD: 75166c725218a5cc6316a4c9068c5980c0edd1ac  Atribucion de B6.3: el runner sobre el brazo del grafo con la enmienda 1, su prueba, su sello, su corrida y el material de la lectura de la autora
el 238 (75166c72): HEAD mismo, renglón 1 de git log --format=%H
git diff --name-only 75166c72 HEAD: 0 renglones; en banco_mcp/ y neo4j/: 0
git status --porcelain --untracked-files=no, con las vedadas podadas: 0 renglones
sha256 de HEAD (12 primeros), los 26 OK:
  los 19 del paso 0 de la C2 (69aab27cc3be n6/correr_n6.py … e6759185b0b6 data/experiment/ev2_reporte/code/atribucion_fallas_nav.py)
  1bcadb445ef4 agentes/lanzar_lote_paralelo.py      86f88984e1aa paralelo/lanzar_agente_n6_prueba.py
  04fd32bc18e9 n6/seco/lanzar_agente_n6_seco.py     191e65bba552 lectura_tolerante_juez.py
  c27bc8882240 mcp_kg/familias_nav.py               b8a2e828314a mcp_kg/familias_nav_cand.py
  3a58e5be33f2 scripts/ucita2_indicadores_banco.py
lo de antes (8 primeros): los 12 de la C1, OK (1b368333 … 87d8e68f); de la C2, los 4 OK:
  78cb4a75 FRENO_N7c_C2.md   1112ed1c b2/diagnostico_B2_N7c_C2.md   ae0435ce controles/prueba_lanzador_sin_config.py
  4880a70c controles/factibilidad_humo.py
el índice por punto (unav_n7c/copia_head/…/indice_puntos/KG_Acumulado_Tandas0y1yFinal_r2b_sincola/):
  manifiesto.json ef036b670321… = sha256_manifiesto_indice de n7/config_mcp_kg_n7_evaluado.json; sus 4 archivos, los del manifiesto
preguntas_N3.json: igual a SHA_PREGUNTAS_N3 (correr_n6.py:107), por código
Neo4j de B6.3: control_neo4j_b63.py (git show, sin editar; 4f4cdac85842) en una copia mínima del scratchpad, NEO4J_URI=bolt://127.0.0.1:47687,
  --huella-esperada 2645da6d…: código 0; kg_meta_sha256 576c97256185…, 37.168 nodos, 128.552 aristas,
  huella de estado 4ace5d10833f…, de contenido 2645da6d0179…
pgrep -fl 'correr_juez_v3|corrida_cortada_v3|lanzar_agente|servidor_mcp|correr_n6|correr_b63': 0 renglones
procesos con la ruta del repo en su comando: 0; de claude -p, runners o jueces: 0
```

## Los criterios

1. **El paso 0:** arriba (`controles/paso0_hashes.py` y su salida, `controles/neo4j_antes.json`, `controles/foto_antes.json`).
2. **La copia y su control.** `git archive HEAD` de las rutas y las exclusiones de la C2 y los ocho módulos (2.638 archivos, como
   la C2), más un módulo que pidió el juez falso del seco (`ev2_encadenamiento/code/agregacion_enc.py`, con un segundo
   `git archive` de las mismas rutas más ese: 2.639); de `b63/`, los tres de la C2 con `git show`. Encima, con `cp`, `preparado/`
   y los 5 archivos del índice por punto de la C1 (`controles/sincronizar_copia.sh`). Control por código
   (`controles/control_copia_c2bis.py`), al cerrar: **2.701 archivos** (2.639 del tar, 3 de `b63/`, 54 de `preparado/` y 5 del índice), **0 enlaces, 0 vedados, `preparado/` igual a la copia archivo por archivo (54 de 54), 0 de más**, de `b63/` solo los tres, el índice igual al de la C1 y 0 carpetas `__pycache__` (`controles/control_copia_final.json`) (control positivo: 1 enlace, 4 vedados, 1 distinto y 1 de más,
   detectados).
3. **La parte A.**
   - **N7c+** (`mcp_kg/familias_nav_rel_amp.py`, `d5e9aff19bd7…`): `NavegadorRelAmp` hereda de `NavegadorRel` sin editarlo y
     redefine solo `ver_punto`: la salida de N7c tal cual, un salto de línea, la familia (raíz, niveles, exclusiones, orden, tope
     y pie, «ninguno», como pide el mandato; el recorrido es el de `ver_descendientes`) y la línea «Para citar este punto: <PDF> |
     <unidad>», con «Punto n» o «Sección n», las formas de HEAD del instrumento. Un punto que no existe: la salida de N7c.
   - **El servidor y la configuración.** `diff` de `mcp_kg/servidor_mcp_kg_nav_rel_amp.py` (`caf496311442…`) contra el de N7c: el
     import, `VERSION_SERVIDOR = "1.0-nav-rel-amp"` y `FNRA.NavegadorRelAmp(` (con la sangría de sus dos renglones de
     argumentos). `n7c/config_mcp_kg_n7c_amp_evaluado.json` (`31b39342c736…`): solo `"version"`. `n7c/mcp_kg_n7c_amp_evaluado.json`
     (`ef76623881b8…`): el servidor y la ruta de su config. El docstring del servidor queda igual, como hizo la C1.
   - **Las pruebas** (`mcp_kg/selftest_familias_nav_rel_amp.py`; árbol de juguete de 35 puntos y el TO, doble del driver): **47 de
     47** en cada corrida, las dos salidas iguales byte a byte (`169f37edde4c…`): cada regla de la familia (el abuelo, el padre y
     ninguna), cada exclusión (la sección de N7c dentro de su tope sale; fuera de su tope, entra), el orden y los cinco
     parentescos, el tope de 13 con su pie, «ninguno», la línea de la cita leída por el instrumento (n7c/lector_cita_n7c_amp.py:
     las 35 como el punto mismo, en la forma «PDF» y fundadas; una con el id del TO en lugar del PDF se lee, pero no pasa la forma
     «PDF»), el prefijo exacto (105 de 105) y las diez herramientas iguales
     a las del servidor de N7. **Control negativo:** 17 mutaciones en memoria, las 17 hacen fallar casos
     (`n7c/c2bis/mutaciones_selftest_rel_amp.json`).
   - **B1** (`n7c/c2bis/b1_n7c_amp.py`, `n7c/c2bis/b1_n7c_amp_resultado.json`; dos corridas con el mismo sha256 de las 3.194
     salidas): **prefijo 3.194 de 3.194; familia igual a la calculada aparte 3.194 de 3.194** (el árbol de `puntos.json` y la
     sección de N7c desde el kg.json, con código propio); **cita 3.194 de 3.194** (igual a la calculada aparte, el PDF de la
     cabecera, leída por el instrumento como el punto mismo y en la forma «PDF»). Fundada contra lo que ve el lector en la misma
     salida, como descriptiva: 2.859; las 335 que no dan son, como conjunto, los 335 puntos sin texto propio. **Tamaño** de lo que
     suma N7c+: mediana 868 caracteres (312 tokens estimados), p95 1.046 (376), máximo 1.071 (385); familias con «ninguno» 130,
     cortadas por el tope 2.236. **Techo en N3: 8 de las 17, lo mismo que la mesa** (solo la sección de N7c, 5; sin la familia,
     5; sin la sección, 3; sin los topes, 10). Neo4j igual antes y después; 26.338 consultas de lectura.
4. **Los ocho cambios**, cada uno con su prueba en el seco (las ramas C1 a C8, R0 y R1):
   1. las configuraciones: `CONFIG_AGENTES` (n7c/config_agentes_n7c.json); una entrada armada sin `--config-agentes` la toma;
   2. el Neo4j de B6.3: `precondiciones` usa `control_neo4j_b63.estado` (real y en lectura en el seco: da; con una huella
      equivocada: 8 sin lanzar nada); el control del Neo4j de N6 no se importa;
   3. las configuraciones por sha256 (N7, N7c y N7c+), que la de agentes las nombre y que sus brazos sean los del lanzador: da; un
      sha256 cambiado, 8; una configuración del lanzador con otro brazo, 8;
   4. el tope y el freno: 45 y 38; una entrada real con 130 y 100, 8;
   5. la semilla `N7C:orden:v1` (`armar_orden` reasignado, porque la de correr_n6 queda fijada en su firma, `:203`); una entrada
      con el orden de N6, 8;
   6. el contenedor `neo4j-bcra-kg-indices-eval`: en la entrada, en el registro de Docker al lanzar y en la guarda de cada tanda;
   7. la guarda: el patrón real ve `correr_n7c.py`, `correr_juez_v3.py` y `corrida_cortada_v3.py` (y los de N6), el de N6 no;
      una entrada con el patrón de N6, 8;
   8. `n7c/lanzar_agente_n7c.py`: las dos entradas lo nombran con su sha256 y cada sesión del seco se preparó con la configuración
      de B2 y el JSON de MCP de su brazo (33 de 33 en R1: el comando, la identidad, la meta y el registro del CLI falso).
   **Lo que queda como en N6, declarado** en el docstring de `correr_n7c.py`: las clases, el reintento, el orden de los lotes (el
   sin codificador, vacío), R5, la memoria y sus umbrales, Docker, el juez con su semilla, su sal y su prefijo, el prefijo «N6-» de
   los ids, `registro_n6.json`, la foto del repo, los códigos, el mensaje del freno de `cargar_entrada` (que dice 130 y 100 aunque
   compara con 45 y 38) y los valores por defecto de `--entrada`, `--salida` y `--lanzador` (los comandos los pasan siempre).
5. **La configuración de agentes**, armada por `n7c/armar_config_agentes_n7c.py` (con `--verificar`), cada campo con su fuente
   en `fuentes_de_los_campos`: `prompt`, `corte_R5`, `modelo`, `claude_code_version_sellada`, `modo_harness`, `env_por_sesion` y
   `base`, de `config_agentes_b63.json` tal cual; `R5` (30, 32 y 1,80), «sale del `corte_R5` de config_agentes_b63.json»;
   `kg_N7`, el brazo `kg` de B6.3 campo por campo; `kg_N7c` y `kg_N7c_amp`, el mismo con su JSON de MCP, su config y sus módulos;
   `configuraciones_n6`: N7, N7c y N7c+ (`N7c_amp`), 3 repeticiones, con codificador. La del humo es la misma salvo las tres
   repeticiones (el `diff` lo muestra) y sus brazos son los de B2 byte a byte; el lanzador usa la de B2 (rama K y C3 del seco).
6. **Las dos entradas**, de modo real, armadas con `correr_n7c.py entrada` desde la copia: `n7c/entrada_n7c_n3.json`
   (`78568a0215e4…`, 270 sesiones, 90 por configuración) y `n7c/entrada_n7c_humo.json` (`3e00a859a558…`, 3 sesiones, una por
   configuración). Las rutas: las de la configuración y el lanzador, relativas a `banco_mcp/`; la guarda, el juez y la lista de la
   familia 5, relativas al repo (las tres están en HEAD); las preguntas y el Python de las citas, con `~/`. Se cargan desde la
   copia (`cargar_entrada`, rama C1 y H del seco) y los archivos que nombran tienen el mismo contenido en la copia que tendrán en
   el repo (están en la lista del 241 o en HEAD). La pregunta del humo (`n7c/c2bis/elegir_pregunta_humo_n7c.py`, la regla del
   mandato, sobre el Neo4j de B6.3 en lectura): de las 5 de remisión, 4 cumplen; la regla da la primera. Escrita por código en
   `unav_n7c_c2bis/humo/preguntas_humo_N7c.json` (`a5eea29c…`), fuera del paquete y del commit.
7. **Los controles de los servidores y del humo, contra un juguete.** `n7c/control_servidores_n7c.py`, contra el servidor de
   juguete (`n7c/c2bis/prueba_control_servidores_n7c.py`): los tres en su lugar, 0 con todo en verdadero; N7c y N7c+ cruzados,
   1; N7 servido como N7c, 1; el humo con otro sha256, 8 sin levantar nada. `n7c/controlar_humo_n7c.py`, en el seco (rama H):
   la gemela seca del humo da «pasa» en las tres (N7 sin marcas, N7c con la sección, N7c+ con las tres); sobre R1, las 3 de
   infraestructura en sus dos intentos dan «no concluyente» (código 2); la salida de N7 leída como N7c o N7c+ da «no pasa».
8. **El seco**, dos corridas desde la copia: **66 de 66 en PASS en cada una**, con los mismos controles y veredictos (la primera, en `n7c/c2bis/corrida_en_seco_n7c_salida.json`; las dos, en `pruebas/`). Las ramas: R0 a R9 de N6 (de R8, su primera parte), K, C1 a C8 y H; el seco usa el Neo4j de B6.3 solo en C2, en lectura. Lo que no corre desde la copia, y qué lo cubre: los servidores
   reales (no están el `.venv` del JSON de MCP, el kg.json ni la matriz densa): `control_servidores_n7c.py` desde el repo y el
   humo; el CLI real y la API: el humo; la segunda parte de R8 de N6 (lo fijo que sube durante el primer lote): no aplica, porque
   en B2 ese lote está vacío.
9. **El análisis** (`n7c/analizar_n7c.py`), con su prueba (`n7c/selftest_analizar_n7c.py`, B2 de juguete de 6 preguntas y 18
   sesiones): **16 de 16**, dos corridas iguales (`255d6be89857…`): el juez con su lectura tolerante (por la clave de la caché, sin
   depender del orden), la fidelidad en el total y en dato directo, las de varios puntos que consultaron todas las anclas (con
   el lector de la enmienda 1), las citas por la línea de comandos del instrumento, el tope y la regla de adopción (D-B2-9), sobre
   el juguete y sola (los bordes del 5 % y de los 5 puntos, una medida que falta, (iv) que falla).
10. **Los tres comandos, PREPARADOS** (abajo).
11. **La lista del 241** (`unav_n7c_c2bis/lista_preparado_241.txt`, `controles/lista_241.py`): **54 archivos**, cada uno con su sha256 y su ruta del repo; **0 rutas existen en HEAD** (`git show HEAD:<ruta>` falla en las 54; control positivo: `n6/correr_n6.py`, detectada). Lo de la C1 (los 5 de `mcp_kg/` y `n7c/` y los 7 de `n7c/c1/`), lo de la C2 en `n7c/c2/` (4), y lo de esta etapa: N7c+ (`mcp_kg/`), el runner, las configuraciones, las entradas, los controles, el seco con `n7c/seco/`, el análisis y su prueba, los comandos y, en `n7c/c2bis/`, B1, las pruebas y sus salidas, la elección de la pregunta del humo y este FRENO (`controles/lista_241.json`). Ningún archivo trae texto de N3 (criterio 13).
12. **Iguales antes y después** (`controles/foto_estado.py`, `foto_antes.json` a las 00:14:14 y `foto_despues.json`): HEAD; el status con `-uno`, 0 renglones; el status con los no rastreados, el mismo sha256 (`540d3f699036…`); los 26 de HEAD; `unav_n3/` (97 archivos), `unav_n7c/` (3.318) y `unav_n7c_c2/` (2.689), archivo por archivo: **todo igual** (a las 01:21:59).
    El Neo4j: la misma salida del control al empezar y al terminar (código 0; huella de estado `4ace5d10…`, de contenido `2645da6d…`; la segunda, desde `copia_head/`; `controles/neo4j_despues.json`). Procesos pagos al cerrar: 0.
13. **Los tramos de 40 caracteres** (`controles/control_tramos40_c2bis.py`, el de la C2), sobre todo lo que escribí (este FRENO
    incluido), el scratchpad, la transcripción de la sesión y sus salidas guardadas, sin los `git archive` extraídos ni el archivo
    de la pregunta del humo: **0 tramos con letras de las preguntas de N3 y 0 del texto de los puntos de los 14 TOs** (control positivo: 1 y 1); los que coinciden con el texto de los puntos no tienen ninguna letra (renglones de guiones). Resultado en `controles/control_tramos40_final.json`. El archivo de la pregunta del humo (`humo/`) queda fuera, como pide el mandato.
14. **El grep de convenciones** (`LC_ALL=en_US.UTF-8 controles/grep_convenciones_c2bis.py`, el de la C2): **0** en lo que escribí, sin contar el propio script, que cita el patrón y la regex de rutas (control positivo: 2). Resultado en `controles/grep_convenciones_final.json`. El archivo de la pregunta del humo queda fuera (es texto de N3).

## Los tres comandos, PREPARADOS

Los corre la autora desde su Terminal, desde el repo y después del commit 241, en este orden. Cada uno arranca controlando el
sha256 de 18 archivos de N7c y N7c+ en HEAD y en el árbol (20 si alguno no da) y pasa al Python un entorno cerrado (`env -i`:
PATH, HOME, `NEO4J_URI=bolt://127.0.0.1:47687`, `BANCO_VENV_VECTOR` y, solo donde se lanzan sesiones, `ANTHROPIC_API_KEY`).

```bash
zsh data/experiment/banco_mcp/n7c/comando_humo_b2_n7c.zsh
```

El control de los tres servidores (USD 0; 0, 1, 7 u 8), el humo (3 sesiones, P = 1; los códigos de correr_n6) y su control (0
las tres pasan; 1 alguna no pasa; 2 alguna no concluyente). Hace falta el Neo4j de B6.3 sano (`neo4j-bcra-kg-indices-eval`), el
`.venv`, el venv del codificador y la clave. Gasto: como mucho USD 5,40 del agente más el juez de 3 respuestas.

```bash
zsh data/experiment/banco_mcp/n7c/comando_b2_n7c.zsh
```

Exige el control del humo en 0 (21 si no; `--humo-revisado` lo deja pasar con la revisión de la mesa), corre `controles` (13
memoria, 14 Docker; y 13 si lo fijo pasa de 9,70 GB) y después `todo` con P = 1 en los dos lotes (270 sesiones y el juez; 0, 2, 7,
8, 11, 12, 13, 14). Gasto: el tope de USD 45 y el freno de 38. Retomar es correr el mismo comando.

```bash
zsh data/experiment/banco_mcp/n7c/comando_analisis_b2_n7c.zsh
```

El análisis (USD 0, sin la clave ni el Neo4j): imprime cuentas, fracciones, sí o no y la configuración que adopta la regla; 0, 8
o 1.

## Decisiones mías, declaradas

- **La clave `N7c_amp`** para N7c+ (arriba). El análisis imprime «N7c+».
- **El kg.json del grafo evaluado, leído en su lugar para B1** (`R/data/experiment/reaplicacion_unica/acumulado/ens_128_r2b_sincola/r2/kg.json`,
  sin rastrear): el mandato pide la familia «calculada aparte desde el kg.json y el índice», y no hay otra copia; lo hizo así la
  C1. Solo lectura, con su sha256 (`576c9725…`) antes y después, igual al `kg_sha256_esperado`.
- **Los intérpretes:** el python del `.venv` del repo (`-B`, `PYTHONDONTWRITEBYTECODE=1`) para lo que usa Neo4j, el servidor y
  el corredor, como la C1 y la C2; un Python 3.12 para el instrumento de la cita y el lector de la enmienda, que no compilan con
  el 3.10 del `.venv` (el `python3` del PATH en las pruebas de juguete, y el de `~/INGENIERIA IA/TESIS/venvs/banco_vector_py312`,
  el de N6, en B1). Por eso hay dos lectores nuevos que corren en 3.12 y reciben todo por la entrada estándar (ninguna salida de
  `ver_punto` de N3 se escribió en disco): `n7c/lector_cita_n7c_amp.py` y `n7c/lector_anclas_n7c.py`.
- **La unidad de la cita:** «Punto n» y «Sección n» (las formas de la ubicación del harness, `RE_PUNTO` y `RE_SECCION`), que el
  instrumento lleva al mismo punto que la clave.
- **«Consultada» en el análisis:** la regla de la enmienda leída del log R1 (`leer_paso` para ver_punto y ver_descendientes;
  ver_nodo y ver_vecinos sobre los nodos del ancla, sin contenedores), sin la re-ejecución de las v1, que no cambia qué nodo se
  consultó. Una sesión sin llamadas no consultó ninguna ancla y cuenta en el denominador.
- **La lectura tolerante en el análisis:** por la clave de la caché del juez (`llm_cache.compute_key`), no por el orden de las
  filas como en N6, para que valga también si el juez se retoma.
- **«Al tope»** en (iii): 30 llamadas o más, o cortada por R5 (`analizar_n6.operativo`, la definición de N6).
- **El seco con un servidor de juguete** y un CLI falso que envuelve el de N6 (el servidor real no arranca desde la copia); los
  planes, los de N6 con llamadas al juguete. El juguete lleva `servidor_mcp` en su nombre para que la memoria lo cuente como
  servidor.
- **La configuración del humo** arma el orden y los lotes; cada sesión del humo usa la de B2 (el lanzador la fija), con los
  mismos brazos, controlado antes de lanzar.
- **El comando de B2 exige el control del humo en 0**, con `--humo-revisado` para la revisión de la mesa.
- **Los generadores** (`n7c/armar_config_agentes_n7c.py` y `n7c/c2bis/armar_comandos_n7c.py`) van en el 241, con `--verificar`.
  Las configuraciones de agentes y las entradas se armaron en la copia y se copiaron a `preparado/`.
- **Docstrings:** el del servidor de N7c+ queda igual al de N7c (como hizo la C1), para que el `diff` muestre solo el cambio.

## Errores propios, con su causa

1. Al empezar listé la carpeta de arriba (`fuera_del_repo/`, con `ls -A`), con los nombres de las carpetas vedadas, sin entrar en
   ninguna. La causa: listé para ubicar las carpetas de la C1 y la C2 sin podar las vedadas (el mismo error que declaró la C2).
2. En el paso 0 corrí un `find` sobre mi copia mínima del scratchpad para contar carpetas `__pycache__` (dio 0). El mandato dice
   «ningún `find`». La causa: el control lo escribí por costumbre; después los conté con `os.walk`.
3. En un comando corrí `git -C . ls-files` dentro de `preparado/`, que no es un repo; no dio nada. La causa: un resto de una línea
   de prueba.
4. En `correr_n7c.py` escribí primero los sha256 completos de las configuraciones de N7 de memoria, con marcadores para las de
   N7c+, y los reemplacé por los medidos por código antes de correr nada. La causa: escribí las constantes antes de medirlas.
5. La primera corrida del selftest de N7c+ falló dos veces antes de dar: la carpeta `scripts/` mal calculada (`parents[2]`) y
   después el instrumento de la cita, que no compila con el 3.10 del `.venv`. La causa: no revisé que `n6/analizar_n6.py` ya
   avisa que el instrumento pide 3.12. De ahí salió `n7c/lector_cita_n7c_amp.py`.
6. La primera corrida del seco se cortó: el juez falso de A2.2 importa `ev2_encadenamiento/code/agregacion_enc.py`, que no estaba
   en la copia. Lo agregué con `git archive HEAD`. La causa: no seguí las importaciones del juez falso antes de correr.
7. La segunda corrida del seco dio 65 de 66: el servidor de juguete no llevaba `servidor_mcp` en su nombre y la memoria de N6 no
   lo contaba como servidor. Lo renombré con `mv` en `preparado/` y en la copia. La causa: no leí `partes_del_arbol` antes de
   nombrarlo.
8. `correr_n7c.py entrada` (el `main` de correr_n6) imprime la ruta de la entrada que arma; las del seco y del selftest, que están
   en el scratchpad, salieron en la consola con su ruta absoluta. No quedaron en ningún archivo escrito por mí. La causa: el
   `print` de correr_n6, que no controlé.
9. Antes de correr el seco escribí una condición de R9 que esperaba el nombre del contenedor en el mensaje del freno de Docker,
   que no lo trae; la corregí antes de la primera corrida. La causa: no leí el mensaje de `correr_agente`.

## El paquete

`revision_N7c_C2bis/`, con `manifest.txt` y nombres únicos (la ruta, con «__»), sin el archivo de la pregunta del humo: este FRENO, el archivo de control, la lista del 241, `preparado/`, `controles/`, `b1/` y `pruebas/` (`controles/armar_paquete.py`). La copia con `ditto` está en `$HOME/INGENIERIA IA/TESIS/fuera_del_repo/scratchpads/d23f8b89-7160-4bdf-aca4-97f2011b5d81/scratchpad/revision_N7c_C2bis/`. Su verificación contra el manifest se informa en el mensaje del FRENO.

FRENO: espero la revisión de la mesa. El commit 241, el humo y B2 los corre la autora después.
