# FRENO — U-BANCO-PARALELO, el «seguí»: el testigo integrado, la versión del CLI, el patrón de la §198 y el humo

Sesión `95486f81-2327-4620-90bc-f61b59d22c1a`, 26/10/2026. USD 0: no corrí nada pago, no escribí en el repo ni commiteé.
Sigo con la copia del repo en `banco_paralelo/copia/bcra-regulatory-kg/`, puesta al día con HEAD `8c064ad3`, y su Neo4j
propio. El FRENO de la vuelta anterior (paquete `revision_UBANCO_PARALELO/`, `2c52d7cc…`) queda como está; acá va lo de
esta vuelta, con los nombres de archivo del paquete `revision_UBANCO_PARALELO_b/` (con `_UBANCO_PARALELO_b`).

## 1. Resumen

- **FRENO: el agente recibe la fecha en su pedido.** El test de aislamiento, corrido entero con el testigo integrado,
  encuentra la fecha del día en el turno de las 9 sesiones selladas, en los tres brazos: una vez en `system`
  (`AAAA-MM-DD`) y, en `messages`, una vez como `AAAA-MM-DD` junto con «Today's date» y «date is». El pedido auxiliar no la
  trae. Contradice lo que se iba a declarar («el agente no recibe la fecha en su pedido, como en A2.2»): no lo arreglo,
  lo decide la autora (§7, punto 1).
- **Todo lo demás del criterio 13 da bien,** con la opción (a): el positivo en las 9, ningún trecho ni token de ningún
  testigo en ningún pedido, stream, carpeta de configuración ni log R1, las tools de su brazo, un solo sha256 de `system`
  y uno de `tools` por brazo y tipo de pedido, todo `POST` al modelo capturado y ninguna respuesta del modelo, los testigos
  sin cambiar, los plantados borrados, el cwd vacío y el negativo en los dos brazos. Las otras conexiones de los CLI,
  registradas y declaradas.
- **La guarda de la versión del CLI, el patrón de la §198 y el humo con USD 8 y 6** dan bien en la corrida en seco (§4), y
  **los doce criterios de antes**, otra vez (§5). Los archivos sellados del banco no cambian.
- **HEAD avanzó dos veces:** a `8c064ad3` antes de empezar (puse la copia al día) y a `4b94fae8` mientras corría (solo
  el registro de decisiones; la copia quedó en `8c064ad3`, §9).

## 2. Paso 0

`scripts/paso0_b_UBANCO_PARALELO_b.zsh` → `salidas/paso0_b_consola_UBANCO_PARALELO_b.txt`:

```
lo que uso del scratchpad: checkpoint.md y revision_UBANCO_PARALELO/, están
pwd al arrancar: $HOME/INGENIERIA IA/TESIS/fuera_del_repo/banco_paralelo
repo: HEAD 8c064ad3; 2addcf32 en su historia: sí; status --porcelain --untracked-files=no: 0 líneas
desde 2addcf32: 4 commits (eb18a031, 89370cc2, c630204b y 8c064ad3); 26 archivos, 1.824 renglones agregados; 0 borrados
  o renombrados (la adjudicación de A2.2, el preregistro de B6.3 y el registro de decisiones)
manifest del paquete anterior: 2c52d7cca9aae260909812f903852535fa7aeae1f08765bdc5d26be39d146b6b; sus 55 archivos, 55 de 55
  en el paquete, en el scratchpad y en la copia permanente
```

**HEAD avanzó,** así que puse la copia al día con el rsync de siempre (sin borrar: ningún archivo se borró en el repo) y
la controlé (`salidas/control_copia_inicial_b_UBANCO_PARALELO_b.json`): de los 25.518 archivos regulares de HEAD, 25.471
en la copia, todos con su blob de HEAD (fuera por regla, 46 vedados y `.env.example`); 0 enlaces fuera del `.venv`
clonado (3 adentro); los dos índices con su sha256. **Los sellos del banco, otra vez:** 2.381 archivos
(`salidas/sellos_banco_antes_b_UBANCO_PARALELO_b.txt`): los 2.357 de antes con el mismo sha256 y 24 nuevos, los de la
adjudicación de A2.2.

## 3. Lo que cambió

- **`agentes/lanzar_lote_paralelo.py`:**
  - **la guarda de la versión del CLI** (código 6): al empezar el lote y antes de lanzar cada sesión, `claude --version`
    tiene que empezar con la `claude_code_version_sellada` de la configuración de su lanzador (para el de N6,
    `paralelo/config_agentes_n6_prueba.json`: `2.1.241`; `--config-agentes` la cambia), y el destino de `claude` en el
    PATH (su ruta, su `readlink` y su ruta real) tiene que ser el del comienzo; al terminar cada sesión, la
    `claude_code_version` de su `system/init` tiene que ser la sellada; y después de cada tanda, el destino otra vez. Si
    algo no da, no lanza ninguna sesión más, termina con el código 6 y el registro dice cuál y por qué (`cli`, con cada
    control). Hoy `claude` es un enlace a `~/.local/share/claude/versions/2.1.241`;
  - **la fecha de cada sesión** es la del reloj del lanzador al empezarla, en hora local (la decisión 4). La línea
    «Today's date is …» de la transcripción dejó de ser la fuente (saqué su lector). En la corrida en seco el reloj se
    fija con `RELOJ_FECHA`.
- **`paralelo/guardas_lote.py`:** `PATRON_EXTRACCION` es el de la §198, tal cual (`RUTA_CON_ESPACIOS` y el patrón,
  comparados por código contra el texto del despacho: iguales). El humo no lo nombra: llama a esta guarda.
- **`comandos/humo_lote_paralelo.zsh`:** tope USD 8 y freno USD 6, y en su cabecera, declarada, la configuración de prueba
  (la decisión 2). `HUMO_LOTE` cambia el lote, solo para su prueba con el CLI falso.
- **`aislamiento/testigo_aislamiento.py`** (integrado en `test_aislamiento_paralelo.py`): los sha256 de `system` y de
  `tools` por brazo y por tipo de pedido, la fecha en cada pedido y la lectura (a) del criterio 13 (§4).
- **`paralelo/cli_falso/`:** el CLI falso da la versión sellada (con la marca de falso en `--version`), no escribe ninguna
  fecha en la transcripción, sigue los enlaces, y sus planes cambian la versión de `system/init` o el destino del enlace
  `claude` a mitad de un lote; los del humo cuestan unos USD 0,90 por sesión, para que su guarda del gasto actúe.
- **`paralelo/corrida_en_seco_lote.py`:** el reloj que cruza la medianoche, las pruebas G (la versión) y H (el humo), y el
  patrón nuevo en E.

## 4. Los criterios de esta vuelta

| # | criterio | script → salida | resultado |
|---|---|---|---|
| 1 | el paso 0 | `paso0_b` → `paso0_b_consola_UBANCO_PARALELO_b.txt` | OK (HEAD avanzó: la copia, al día, y los sellos, otra vez) |
| 2 | el criterio 13 con la opción (a), en el test integrado y corrido entero | `test_aislamiento_paralelo` → `aislamiento_paralelo_b_UBANCO_PARALELO_b.json` | **FRENO:** la fecha del día en el turno de las 9 sesiones; todo lo demás, bien (§5, 13) |
| 3 | la guarda de la versión del CLI | `corrida_en_seco_lote` → `corrida_en_seco_b_UBANCO_PARALELO_b.json` (`G_…`) | OK: frena con el que cambia (las tres formas), deja pasar con el que no |
| 4 | el patrón de la §198 en el lote y en el humo | ídem (`E_…`) | OK: la ruta con espacios, atrapada; los cuatro que no tienen que frenar, no frenan |
| 5 | el humo con USD 8 y 6, tres a la vez, en seco | ídem (`H_humo`) | OK: tres a la vez y corta antes del freno |
| 6 | los doce de antes, otra vez | los dos JSON (§5) | OK, los doce (§5) |
| 7 | los archivos sellados del banco, sin cambiar | `cierre_b` → `comparacion_sellos_b_UBANCO_PARALELO_b.txt` | OK: 2.381 archivos, la misma lista (`2d78ef92…`) |

**3. La guarda de la versión del CLI** (`G_version_del_cli`; los tres con el código 6, «VERSION_CLI»):
- **G1, la versión de `system/init` cambia a mitad del lote** (el plan de S03-kg da `2.1.250`): con P = 3, el lote frena
  al terminar S03-kg («S03-kg: la claude_code_version de su system/init es '2.1.250', no '2.1.241'»); terminan las 7 que
  ya corrían o habían corrido y quedan 5 sin lanzar;
- **G2, `claude --version` no es la sellada** (un envoltorio que da `2.1.250`): frena al empezar el lote, sin lanzar
  ninguna;
- **G3, el destino del enlace `claude` cambia a mitad del lote** (el plan de S02-kg vuelve a apuntar el enlace del PATH a
  una carpeta hermana): con P = 1, frena después de la tanda 3 («el destino de `claude` cambió», con su `readlink`
  nuevo), con 3 lanzadas y 1 sin lanzar;
- **el que no cambia, deja pasar:** en los lotes A y B, 29 y 37 controles (al empezar, antes y al terminar cada sesión y
  después de cada tanda), todos bien, y `2.1.241` en el `system/init` de las 12 sesiones de cada uno.

**4. El patrón de la §198** (`E_control_de_la_extraccion`): `PATRON_EXTRACCION`, comparado por código con el texto del
despacho, es igual. Con `python3 <tmp>/runner_corpus.py` vivo, el control lo encuentra y la CLI frena con el 9; al
cerrarle la entrada, deja pasar. Con `python3 "<tmp>/con espacio/runner_corpus.py"` vivo, ahora también lo encuentra (9),
y la guarda de otro paso pago también (7); al cerrarlo, deja pasar. Con un `sh -c`, un `grep`, un `ed` y
`python3 <tmp>/otro.py <tmp>/runner_corpus.py` vivos (los cuatro nombran `runner_corpus.py`), no encuentra nada (0). En
el humo, la guarda es la misma CLI (`guardas_lote.py extraccion`); el comando no nombra el patrón.

**5. El humo, en seco** (`H_humo`): el comando entero, `comandos/humo_lote_paralelo.zsh`, desde un entorno con el CLI falso
primero en el PATH, una clave de relleno en un archivo de entorno de la carpeta temporal y `HUMO_LOTE` con su lote más la
marca de un plan de unos USD 0,90 por sesión. Pasa sus dos guardas, levanta el Neo4j propio, controla su KG_Meta, corre
el lote con tope 8 y freno 6 y lo baja al terminar. El lote lanza 3 a la vez (peor caso al lanzarlas: 1,80, 3,60 y 5,40),
espera cuatro veces a que termine una, y antes de la sexta frena (código 2): con 4,50 acumulado, la sexta daría 6,30. El
peor caso de cada lanzamiento nunca pasó de 5,40, y el acumulado terminó en 4,50, por debajo del freno.

## 5. Los doce de antes, otra vez, y el 13

Con lo que cambió (el lote con la guarda de la versión y la fecha del reloj, el patrón de la §198, el humo nuevo y el
testigo integrado), sobre la copia de `8c064ad3` y el Neo4j propio (`corrida_en_seco_b_UBANCO_PARALELO_b.json`,
`aislamiento_paralelo_b_UBANCO_PARALELO_b.json`):

1. **El aislamiento en paralelo: PASS** (init, ejecución y lo compartido). El lote init, 9 sesiones con P = 3 (código 0,
   9 terminadas, con la guarda de la versión del CLI real, `2.1.241`), en tres tandas con dos pares grafo-fragmentos
   superpuestos en cada una; (a) a (d) y los nuevos en las 9: un pid de servidor por sesión, cada log R1 con lo suyo,
   ningún archivo de una en otra, 9 carpetas de configuración distintas fuera del repo y de git, y el cwd vacío en las 4
   tomas del lote y al final. En ejecución, 16 controles de fragmentos sin nada del grafo, 14 con el grafo respondiendo a
   la vez (al menos uno por sesión de fragmentos). Lo compartido, igual antes y después (14 archivos y la base, KG_Meta
   `0435d41f…`).
2. **P = 3 y P = 1: 12 de 12 sesiones iguales.** La sesión que falla a mitad (S03, BM25), incompleta en los dos, con
   «sin evento result» y «log R1 sin línea fin»; las otras 11, completas. El cambio de fecha, ahora del reloj del
   lanzador fijado para la prueba, cae en el bloque S04, dentro del bloque, con P = 3 y con P = 1.
3. **La guarda del gasto corta antes del freno:** freno 2,00, acumulado 0,2152, 8 sin lanzar (peor caso al lanzar cada
   una: 1,80, 1,8592, 1,9074 y 1,9668); y en el humo, con 6,00, el acumulado queda en 4,50 (§4, 5).
4. **Los comandos pagos no llevan la clave** (`control_sin_clave_b_UBANCO_PARALELO_b.txt`): 0 valores con forma de clave y
   0 asignaciones en el humo nuevo y en su lote.
5. **Los archivos sellados no cambian:** 2.381 (los 2.357 de antes y 24 de la adjudicación de A2.2), la misma lista antes y
   después.
6. **El control negativo falla en sus dos casos:** la configuración contaminada trae las 9 tools del grafo y el control 1
   la marca; el proceso con el socket al 37687 y el kg.json abierto, el control 2 lo ve.
7. **El control de la extracción** frena con el proceso de prueba vivo (y ahora con la ruta con espacios) y deja pasar sin
   él (§4, 4).
8. **El grafo con el servidor de navegación:** 5 sesiones del grafo, 5 codificadores distintos, cada uno hijo de su
   servidor; ninguna de fragmentos alcanza un codificador, el índice por punto ni Neo4j; ninguna del grafo abre los índices
   de fragmentos.
9. **Los contenedores:** 278 con su nombre y su estado, iguales a la foto de esta vuelta y a la de la primera; el propio,
   bajado.
10. **El cwd compartido y las carpetas de configuración:** vacío en todas las tomas (4 en el lote init, 5 en A y 13 en B, y
    al final del test); carpetas distintas y fuera del repo (9, 12 y 12).
11. **`NEO4J_URI`:** llega por la lista a las 9 sesiones (`bolt://127.0.0.1:37687`); en el lote init, `lsof` (120
    muestras, solo el 37687 y el 7687) ve el servidor del grafo de las 5 sesiones del grafo conectado solo al 37687 y
    ningún proceso de las 4 de fragmentos conectado; en ejecución, lo mismo por pid.
12. **La guarda de otro paso pago:** con `correr_prueba_T_v2.py` o `correr_a2_2.py` vivos, el lote frena con el 7 sin crear
    ninguna sesión y el humo con el 7; al cerrarlos, el lote lanza su sesión y el humo deja pasar; con un `sh`, un `zsh`,
    un `grep` y un `ed` que los nombran (pgrep ve los 4), los dos dejan pasar.
13. **El testigo, con la opción (a)** (`testigo`): de las 9 sesiones selladas en tres tandas de P = 3 (todas con el grafo):
    - el positivo, 9 de 9; ningún testigo llega (0 trechos de los 1.793 del `CLAUDE.md` del repo, los 13.046 del
      preregistro de B6.3 y los 215 de `~/.claude/CLAUDE.md`, y 0 tokens de los dos plantados) a ningún pedido, stream,
      carpeta de configuración ni log R1;
    - las tools: ninguna ajena en ningún pedido y el turno con su inventario entero, 9 de 9;
    - **los sha256 de `system` y de `tools`, uno solo por brazo y tipo de pedido** en los seis grupos (grafo, BM25 e
      híbrida; auxiliar y turno): los feature flags no cambiaron el pedido de una sesión a otra;
    - **la lectura (a):** cada sesión mandó 2 `POST` a `v1/messages`, los dos llegaron a la captura, y su `result` es el
      error de la captura, sin ningún mensaje del asistente que no sea el sintético del CLI: 9 de 9. Las otras conexiones
      de los CLI, solo por dirección, puerto y muestras de `lsof`: `160.79.104.10:443` (914) y `34.149.66.165:443` (103),
      en las tres tandas;
    - la línea de comandos y el entorno, los de una sesión init, salvo `ANTHROPIC_BASE_URL`: 9 de 9; 0 claves distintas de
      la inválida; los testigos sin cambiar; los dos plantados borrados; el cwd vacío; el negativo detecta el token en el
      `system` en los dos brazos;
    - **la fecha:** aparece en el turno de las 9 (FRENO, §7, punto 1).

## 6. El entorno de cada brazo, por nombre

Como en la vuelta anterior (`entorno_de_la_sesion` de cada comando; los tres brazos, los mismos nombres): en modo init,
`ANTHROPIC_API_KEY`, `ANTHROPIC_BASE_URL`, `BANCO_LOG_R1`, `BANCO_REPO`, `BANCO_SESION_TAG`, `BANCO_VENV_VECTOR`,
`CLAUDE_CONFIG_DIR`, `DISABLE_AUTOUPDATER`, `HOME`, `MCP_TIMEOUT`, `NEO4J_URI` y `PATH`; en modo real, los mismos sin
`ANTHROPIC_BASE_URL`. `NEO4J_URI` vale `bolt://127.0.0.1:37687` en los dos brazos; ninguna sesión de fragmentos hereda otra
variable de Neo4j ni del índice del grafo.

## 7. Lo que la mesa y la autora tienen que mirar

1. **FRENO: la fecha llega al agente.** En el turno (el pedido con las tools) de cada una de las 9 sesiones selladas, en
   los tres brazos, la fecha del día de la sesión (2026-10-26) aparece una vez en `system` como `AAAA-MM-DD`, y en
   `messages` una vez como `AAAA-MM-DD` junto con «Today's date» y «date is» (una vez cada una): por las cuentas, una
   frase como «Today's date is 2026-10-26» en lo que el CLI agrega al mensaje del usuario (su texto no lo abrí). El pedido
   auxiliar no trae ninguna. Ninguna otra forma (`DD/MM/AAAA`, `D/M/AAAA`, `M/D/AAAA`, el mes en inglés o en castellano)
   aparece. Es el CLI sellado (`2.1.241`, `--bare`) con el entorno del lanzador sellado, el mismo de A2.2, así que que las
   sesiones de A2.2 también hayan recibido la fecha es probable y NO VERIFICADO (no hay captura de sus pedidos). La
   declaración prevista («el agente no recibe la fecha en su pedido, como en A2.2») no se sostiene. **PENDIENTE de la
   autora:** qué se declara y si cambia algo de B6.3 (por ejemplo, declarar que cada sesión recibe la fecha del día y usar
   la del reloj del lanzador, que ya va en el registro, para saber cuál recibió; o el orden intercalado de la §88). No
   cambié nada.
2. **Las otras conexiones de los CLI** (la opción a), declaradas: `160.79.104.10:443` y `34.149.66.165:443`, vistas en las
   tres tandas del testigo (914 y 103 muestras de `lsof`). Qué llevan, NO VERIFICADO.
3. **La copia quedó en `8c064ad3`:** el repo pasó a `4b94fae8` a las 16:00, con mis corridas en curso; entre los dos solo
   cambia el registro de decisiones, que no usa ninguna corrida (`copia_contra_el_head_al_terminar_b_UBANCO_PARALELO_b.txt`).
   No la volví a poner al día para no separarla de lo que corrió sobre ella.
4. **El humo en seco corre el comando entero** con `HUMO_LOTE` (su lote más la marca de un plan del CLI falso); el humo
   pago usa su lote, sin la marca. Con freno USD 6 y la reserva de 1,80 por sesión, tres a la vez caben mientras el
   acumulado no pase de 0,60; con más, la guarda baja a dos o a una, y no lanza ninguna sesión cuya reserva lleve el
   gasto comprometido por encima de 6.

## 8. Errores propios, con su causa

1. **La guarda del destino de `claude`, mal en su primera versión:** registraba las rutas con `rel_repo`, que resuelve los
   enlaces, así que el `readlink` nuevo y el de antes salían iguales y la prueba G3 no frenaba (el CLI falso sí había
   cambiado el enlace). Lo vi en el registro de G3, paré esa corrida (`TaskStop`; sin procesos que quedaran vivos), lo
   corregí (las rutas van tal cual, con la carpeta personal como «~») y corrí todo otra vez con el código final. La
   corrida parada, archivada en `banco_paralelo/salidas/intento1_b_destino_resuelto/`. Causa: reusé `rel_repo` para algo
   que no se puede resolver.
2. **Mi primera versión de la búsqueda de la fecha contaba dos veces cada aparición** (en las cadenas y en el JSON crudo).
   Lo vi al probarla con textos de prueba, antes de correr nada, y la dejé sobre las cadenas.

## 9. Al terminar

- **El Neo4j propio, bajado** al terminar (lo levanté para la corrida en seco; el humo en seco lo bajó al terminar; lo
  levanté otra vez para el test y lo bajé). `docker ps -a`: 278 contenedores, iguales a la foto de esta vuelta
  (`docker_ps_a_antes_b`) y a la de la primera; el propio no está.
- **El repo:** HEAD `4b94fae8` (la autora commiteó a las 16:00), `status --porcelain --untracked-files=no` vacío.
- **La copia,** contra `8c064ad3` (`control_copia_final_b_UBANCO_PARALELO_b.json`): 25.471 blobs de HEAD, 0 distintos, 0
  enlaces fuera del `.venv` clonado (3 adentro), los 13 archivos nuevos de la unidad, los índices con su sha256.
- **Los sellos del banco:** 2.381, iguales antes y después.
- **Los plantados del testigo, borrados;** los cwd de las raíces de las sesiones, vacíos; ningún proceso de las corridas
  vivo.
- **Fuera del paquete,** en `banco_paralelo/`: `salidas/` (streams, logs R1, metas y transcripciones de las corridas, que
  llevan texto de la tanda 1, y las corridas archivadas) y `privado_captura/aislamiento_b/` (los cuerpos capturados, sin
  abrir).

## 10. Grep de convenciones

El del repo, `data/experiment/segmentacion_oficial_e0r2/s0_4/scripts/grep_convenciones.py` (en la copia), con
`LC_ALL=en_US.UTF-8`, como en la vuelta anterior: los tokens del nombre salen de `git config user.name` del repo, en la
consola, y la salida los nombra `nombre_1`, `nombre_2`. Sobre los 55 archivos del paquete antes de sumar su salida:

```
control positivo: 16 de 16 términos encontrados
archivos revisados: 55
total por término: {} — total 0
```

(`salidas/grep_convenciones_b_UBANCO_PARALELO_b.txt`). Lo corrí otra vez sobre el paquete final, con este FRENO y esa
salida (56 archivos y el `manifest.txt`): total 0.

## 11. El paquete y su copia permanente

- **El paquete:** `banco_paralelo/revision_UBANCO_PARALELO_b/`, 56 archivos más `manifest.txt` (sha256, ruta y una
  descripción por archivo, desde `descripciones_UBANCO_PARALELO_b.json`), en `codigo/`, `comandos/`, `scripts/` y
  `salidas/`, con nombres únicos con la unidad y la vuelta. El de antes, `revision_UBANCO_PARALELO/` (`2c52d7cc…`), queda
  como está. Los scripts de `scripts/` corren desde `banco_paralelo/revision_trabajo/`, con sus nombres sin el sufijo.
- **Lo que no va:** ningún cuerpo capturado, log R1, stream ni transcripción; de los pedidos capturados, sus sha256, sus
  bytes y las cuentas de los controles.
- **Sus copias, con `ditto`:** la permanente,
  `$HOME/INGENIERIA IA/TESIS/fuera_del_repo/scratchpads/95486f81-2327-4620-90bc-f61b59d22c1a/scratchpad/revision_UBANCO_PARALELO_b/`,
  y la de la carpeta temporal de la sesión (regla g del `CLAUDE.md` del repo). Verificadas contra su `manifest.txt`
  (`armar_manifest.py --verificar`): 56 de 56 en cada una, sin archivos de más.

**FRENO: espero la revisión de la mesa.**
