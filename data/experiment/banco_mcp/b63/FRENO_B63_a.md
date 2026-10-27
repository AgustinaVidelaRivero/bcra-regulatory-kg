# FRENO B6.3-a: el runner de B6.3, el juez encadenado y D-10, con su selftest y su corrida en seco

Etapa a del runner de B6.3, 26/10/2026, desde las 17:40 (el paso 0). USD 0, sin API y sin Neo4j. Rige el pre-registro de B6.3
FIRMADO, `docs/preregistro_B6_3_evaluacion_final.md`, leído en su commit de firma `adf20f3b` (`git show`; sha256 `1b3b6556…`), sin
reabrirlo; de las notas al pie posteriores leí, en el repo, la de `617f6652` (la fecha en el pedido, el orden y la cuenta por brazo y por
fecha), que no cambia el texto firmado. En el repo escribí solo en `data/experiment/banco_mcp/b63/`, nueva. No commiteé nada. Espero la
revisión de la mesa.

Ningún texto de una pregunta, un criterio o una cita de B6.3 ni de EV2 aparece en este FRENO ni en lo que escribí. En esta etapa no
abrí ni corrí ningún archivo de preguntas de B6.3 ni ninguna entrada sellada real: la entrada la arma la mesa para la etapa b. Las
preguntas de las pruebas son de juguete (`b63/seco/preguntas_juguete_b63.json`).

## 1. Lo que hice

1. El paso 0 dio todo lo esperado (§2). Faltaba un paquete en la carpeta temporal y lo restauré de la copia permanente.
2. Escribí el runner, `correr_b63.py`, sobre el lanzador del lote sin cambiar su lógica ni la de `agentes/lanzar_agente.py`.
   - Trae la entrada sellada y sus controles, el orden del §6 con su semilla, la fecha y su cuenta por brazo y por fecha, R5, los
     cortes, los reintentos de infraestructura en su lugar y las guardas.
   - El lanzador de una sesión de B6.3 corre `lanzar` de N6 con la configuración de la entrada.
   - El juez de EV2 va encadenado, con D-10 antes de cada juicio, su caché propia y el id opaco de B6.3 (§3 y §4).
3. Adapté el enmascarado de A2.1 a las carpetas de B6.3, con los originales fuera del repo.
4. Agregué, con las funciones de A2.1 sin editarlas, la lectura acotada de `tengu_velvet_ibis` y el control del disco, que el lanzador
   del lote no trae (§10).
5. Probé todo en una copia de trabajo, con datos de juguete: el selftest y la corrida en seco, en tres intentos (§13).
6. Lo llevé a `b63/` y corrí el selftest y la corrida en seco otra vez, en una copia final del repo (§5 a §7).
7. Dejé escrito lo que la etapa b necesita de la entrada sellada y cómo llama al testigo (§8 y §9).

## 2. Paso 0

Lo corrí a las 17:40, con la carpeta personal reemplazada por `$HOME` (salida: `paso0_B63_a_B63a.txt` del paquete):

```
paso 0 de B6.3-a, 26/10/2026 17:40:55 -0300
pwd: $HOME/INGENIERIA IA/TESIS/bcra-regulatory-kg
git log --format='%h %s' -12:
  8b45dc7a Tripletas: el corredor y el analisis de la prueba del juez de precision sobre T, con la regla de la corrida cortada, las 300 y el caso que no preve, se
  617f6652 Preregistro de la evaluacion final: la nota al pie con la fecha que cada sesion recibe en su pedido, el orden firmado de los brazos, la cuenta por braz
  4965b272 Banco en paralelo: el lanzador del lote con la guarda de la version del cliente y la fecha de su reloj, el testigo integrado, el Neo4j propio y los FRE
  50b373df Registro de decisiones: la fecha que el agente recibe en su pedido, las revisiones del analisis de la comparacion con los fragmentos, de la etapa f del
  303a5084 Banco del brazo de fragmentos: el analisis de la comparacion del grafo contra los fragmentos con las adjudicaciones de la autora, y el FRENO de su sesi
  4b94fae8 Registro de decisiones: el caso que la regla de la corrida cortada no preve, con su arreglo, y la guarda de la version del cliente
  8c064ad3 Preregistro de la evaluacion final: la nota al pie con la relevancia de las 96, los desvios de su tercera tanda, el humo, la fecha de cada sesion, la v
  c630204b Banco del brazo de fragmentos: las adjudicaciones de la autora de las respuestas que el juez dejo sin decidir, selladas y convertidas por id opaco
  89370cc2 Registro de decisiones: lo que se informa si las 300 no se completan, los bloques de ejemplos, el testigo, la etapa e con las 300, la relevancia y las 
  eb18a031 Registro de decisiones: la etapa e completa, la regla de la etapa de cada arista, el diagnostico sin la cota por herramienta, las 300 restantes y el ai
  2addcf32 Preregistro de la evaluacion final: la nota al pie con las coincidencias con las citas y con las preguntas, los desvios de la relevancia, los reemplazo
  300cc067 Juez de la evaluacion final: la lectura a ciegas de la autora de la mitad de verificacion, sellada y controlada, y su cruce con los juicios del juez de
rama: main
git status --porcelain --untracked-files=no: []
data/experiment/banco_mcp/b63/: no existe
pre-registro en la firma adf20f3b: 1b3b6556f6cad5d386154f739efb9948a3c3e866f5c3f223b5113b3308eb8bf4; cabecera: **FIRMADO por la autora el 25/10/2026** 
HEAD data/experiment/banco_mcp/agentes/lanzar_lote_paralelo.py: 1bcadb445ef4b3716d6977950e83c08075e7da58324d124e3f6490e9fa3df448
HEAD data/experiment/banco_mcp/paralelo/guardas_lote.py: 73c317682951e2b01314db606f1a8682256f23330e1b88a735ae4e915c0528a2
HEAD data/experiment/banco_mcp/a2_2/analisis/analisis_a2_2.json: a909247453e13563db36750b9488aee6e64cfc37d048a0c006ffe601fa1a8485
la nota de B6.3 con la fecha, entre los 20 últimos: 617f6652
paquetes de la carpeta temporal contra el manifest.txt de su copia permanente, archivo por archivo:
  revision_A2_1_FRENO_a: FALTABA entero en la carpeta temporal; lo restauré con ditto desde la copia permanente (17:40:41) y verifica 93 de 93, con el manifest.txt igual al permanente (f382bc9c…)
  revision_A2_1_FRENO_b: 133 de 133; revision_A2_1_FRENO_c: 31 de 31; revision_A2_1_LISTO: 62 de 62; revision_A2_2_FRENO_a: 91 de 91; revision_A2_2_b: 29 de 29; cada manifest.txt igual al permanente
scripts de la carpeta temporal que uso: foto_repo.py a377b766…, armar_manifest.py 5a7db724…, enmascarar_paquete.py 65eaf9a2… (el de revision_A2_2_b: 65eaf9a2…)
```

## 3. Los archivos de `b63/`, con su sha256 y lo que hace cada uno

| archivo (en `b63/`) | sha256 | qué hace |
|---|---|---|
| `comun_b63.py` | `fb735811465ac51a…` | lo común: rutas, semillas y códigos; la entrada sellada y todos sus controles; la carga de las preguntas, solo por código; el orden del §6 y los ids; la cuenta por brazo y por fecha |
| `correr_b63.py` | `2d8a54aea76185fa…` | el runner: los controles previos, las guardas propias (el patrón, otro paso pago, la extracción), un lote del lanzador del lote por bloque con sus reintentos en su lugar del orden, la clasificación de cada sesión, el control del disco, D-10 y el juez encadenados, el estado para retomar; y, para la etapa b, `lote_init` y `leer_testigo` |
| `corrida_en_seco_b63.py` | `1db2a5d1928c6ebf…` | la corrida en seco: las ramas del punto 4 y del 4 bis, con el CLI falso, los servidores de juguete y el juez sobre un transporte simulado |
| `enmascarar_cwd_b63.py` | `d43606abff31d061…` | el enmascarado de los streams y las transcripciones: `a2_1/enmascarar_cwd_a2_1.py` adaptado a las carpetas de B6.3, con los originales fuera del repo |
| `juez_b63.py` | `16e439a3fcebb9c2…` | el juez de EV2 envuelto, sin editarlo: el instrumento y sus sellos, el control del SDK, el id opaco con la sal de B6.3, el caso ciego y su control, D-10, la guarda del juez, la caché propia, la agregación y la tabla de la mesa |
| `lanzar_agente_b63.py` | `36ca2aae471da131…` | el lanzador de una sesión con la interfaz del lote: `lanzar_agente_n6_prueba.lanzar` con la configuración de la entrada; agrega al comando y a la meta la cadena del lanzador, BANCO_VENV_VECTOR, el control del disco y el valor remoto |
| `seco/bloque_tools_juguete_fragmentos.txt` | `e17f030459e3485a…` | el de los dos de fragmentos |
| `seco/bloque_tools_juguete_kg.txt` | `45e76cb8edb73abc…` | el bloque de herramientas de juguete del grafo |
| `seco/claude_falso_b63.py` | `b41da44e24358199…` | el CLI falso de B6.3: el del banco, importado sin editar, más los planes de cortes, infraestructura, marcas, disco y valor remoto |
| `seco/config_agentes_b63_juguete.json` | `ee6683f0dc8fc9b5…` | la configuración de juguete de los tres brazos |
| `seco/config_agentes_b63_juguete_testigo.json` | `dc8509070a1c083f…` | la de juguete con los brazos del testigo (kg, fragmentos_bm25 y fragmentos_hibrida) |
| `seco/config_servidor_juguete_fragmentos_bm25.json` | `3706fd1057617fed…` | la configuración de juguete del servidor de fragmentos_bm25 |
| `seco/config_servidor_juguete_fragmentos_denso.json` | `f50090e0679c4d40…` | la configuración de juguete del servidor de fragmentos_denso |
| `seco/config_servidor_juguete_kg.json` | `3f2006bde63b077e…` | la configuración de juguete del servidor de kg |
| `seco/herramientas_seco.py` | `68ed04a69d5d7c34…` | lo que comparten el selftest y la corrida en seco: el CLI falso en el PATH, la entrada de juguete, el juez simulado, el proceso de prueba y el registro de las líneas de comandos |
| `seco/mcp_juguete_fragmentos_bm25.json` | `5facf3d4e7dadf37…` | el JSON de MCP de juguete de fragmentos_bm25 |
| `seco/mcp_juguete_fragmentos_denso.json` | `87cdaf3536503776…` | el JSON de MCP de juguete de fragmentos_denso |
| `seco/mcp_juguete_kg.json` | `48608d24b9d0e00a…` | el JSON de MCP de juguete de kg |
| `seco/planes_b63_seco.json` | `d008fb5e9798331f…` | los planes del CLI falso de B6.3 |
| `seco/plantilla_juguete.txt` | `f7849b0f61f4d0a0…` | la plantilla de juguete del prompt |
| `seco/preguntas_juguete_b63.json` | `d95e2e57a5fd2e26…` | las preguntas de juguete, con el esquema de EV2 |
| `seco/servidor_mcp_juguete.py` | `f2ed1cffd9a2f176…` | el servidor MCP de juguete, con el log R1 del banco |
| `selftest_b63.py` | `1774865fb9757a19…` | el selftest de las funciones que no lanzan sesiones |
| `sha256_etapa_a_b63.txt` | `c57442eaacc22296…` | la lista de los sha256 de los 23 archivos de arriba (no se incluye a sí misma) |

Los sha256 enteros, en `b63/sha256_etapa_a_b63.txt` (23 renglones, controlada con `shasum -c` en el repo y en la copia final). Todos son nuevos.

## 4. Cómo corre una sesión de B6.3 y qué controla el runner

- **La cadena:** `correr_b63.py` → `agentes/lanzar_lote_paralelo.py` (`Lote`, importado sin editar) → `b63/lanzar_agente_b63.py`, un
  proceso por sesión → `paralelo/lanzar_agente_n6_prueba.py`, `lanzar`, importado sin editar, y por él `agentes/lanzar_agente.py` →
  `claude -p` con el servidor MCP del brazo.
  - El lanzador de B6.3 le da a `lanzar` la configuración de la entrada (B63_CONFIG_AGENTES, con su sha256).
  - Después agrega al comando y a la meta la ruta y el sha256 de cada archivo de la cadena (ocho), y a la meta, BANCO_VENV_VECTOR
    con la versión de su Python.
  - La línea de comandos y el entorno de la sesión no los toca: son los de `lanzar` y de `LA.env_sesion`, con la lista cerrada, la
    carpeta de configuración nueva y el cwd fuera de git.
  - La lectura acotada de `tengu_velvet_ibis` (por código y en memoria) y el control del disco no los trae el lanzador del lote.
    Los agrega a la meta el lanzador de B6.3, con las funciones de A2.1 (`a2_1/correr_a2_1.py`, `valor_remoto_por_tool` y
    `control_disco`, sin editar).
- **Antes de lanzar nada** (`correr_b63.controles`; código 10 si algo no da):
  - la entrada sellada y sus sha256;
  - las preguntas;
  - el patrón de otro paso pago (`control_patron`: el de `guardas_lote` trae el renglón 16 de `a2_2/guardas_a2_2.zsh` y
    `correr_prueba_T_v2.py`, comparado por código: igual a ese renglón más T). Como los trae, el runner no agrega ninguna pieza;
    si alguna vez no los trajera, frena con el 10;
  - el juez (`juez_b63.controlar_instrumento`);
  - BANCO_VENV_VECTOR desde la entrada (`preparar_entorno`);
  - en modo real, el control del SDK (el 165), el primer control del paso pago del juez.
- **Antes de la primera sesión y antes de cada bloque, en modo real:**
  - la guarda de otro paso pago (código 7), la de `guardas_lote` sin el árbol propio, más la del lanzador del lote antes de cada
    tanda;
  - la de una extracción (código 9).
- **Cada bloque**, en el orden del §6:
  1. un lote del lanzador del lote, con su guarda del gasto, su guarda de la versión del CLI (código 6, al empezar el lote, antes de
     cada sesión y al terminarla) y sus controles de aislamiento y del cwd;
  2. la clasificación de cada sesión, con `clasificar`: completa, cortada, `falla_infra`, `incompleta_otra` o `no_lanzada`. Si el
     control del disco de alguna sesión frena, el runner para con el código 11, sin lanzar otro bloque;
  3. los reintentos de las fallas de infraestructura, en un lote nuevo, antes del bloque siguiente, hasta 3 intentos por brazo; si
     el tercero falla, `falla_infra_sin_terminar`;
  4. D-10 y el juez de cada respuesta completa.
  - Cada lote recibe como freno y tope los de la entrada menos lo gastado: el agente, con el presupuesto entero de cada sesión sin
    `result`, más el juez, por sus cachés.
- **El juez**, con `juez_b63.juzgar`:
  - las repeticiones que le faltan a la respuesta;
  - antes, su guarda: lo gastado más el costo mayor de una respuesta juzgada, o 0,0378 si no hay ninguna, contra el freno y el tope;
    si pasa, código 2;
  - una salida mal formada va a `errores_r{rep}.jsonl`, sin reintento;
  - la caché propia de B6.3, una base por repetición, `b63_juez_r{1,2,3}.db`.
- **Lo que escribe:**
  - en `--out`: `orden_b63.json`, `estado_b63.json`, `fechas_b63.json`, `resumen_b63.json` y `<bloque>/lote<n>/`, con el registro del
    lote y las carpetas de las sesiones;
  - en `--juez-dir`: `veredictos_r*.jsonl`, `errores_r*.jsonl`, `d10_b63.json` (por brazo, sin texto), `agregados_b63_ciego.json`
    (por id opaco, sin brazo) y `desanonimizacion_SOLO_MESA/tabla_id_opaco_b63_SOLO_MESA.json`.
  - Imprime solo cuentas.

## 5. El selftest

**La copia final 2** (`copia_final_b63.zsh`; salida: `copia_final2_selftest_y_seco_B63a.txt`): una copia nueva del repo, con el `rsync` de la cláusula más el volumen de Neo4j. Sus controles: «copia 26/10/2026 18:31:59»; «rsync rc=0 saltados=336»; «env: 0 | NO_ABRIR_: 0 | SOLO_MESA: 0 | enlaces: 0 | .git: no»; «lista sha256_etapa_a_b63.txt OK en la copia».

Corrí el selftest en esa copia, con `env -i PATH HOME SELFTEST_B63_TMP=<carpeta temporal> <repo>/.venv/bin/python -B data/experiment/banco_mcp/b63/selftest_b63.py`:

1. PASS: orden: determinista, con random.Random(f'B63:orden_corridas:v1:{id}:{r}').shuffle sobre los brazos ordenados, por pregunta y repetición — 6 bloques
2. PASS: ids: terminan con el brazo; los reintentos llevan -i2 y -i3; todos los admite el lanzador del lote
3. PASS: fechas: la cuenta por brazo y por fecha, con los reintentos, y el bloque con dos fechas
4. PASS: clasificación: completa, cortada (turnos y presupuesto), falla de infraestructura (sin result o is_error), otra, timeout, no lanzada e init
5. PASS: entrada: la de juguete pasa; frena con otro sha256 del comando, de config_agentes, de un config_servidor o de las preguntas — frena en 4 de 4
6. PASS: entrada: frena sin BANCO_VENV_VECTOR, con uno que no existe, con otro Python, con otro R5, con otros roles y con el freno sobre el tope — frena en 6 de 6
7. PASS: preguntas: el esquema de EV2 por defecto, cada criterio con solo su texto y su cita; un id que no está o un esquema distinto
8. PASS: D-10: las marcas del brazo (sus herramientas, con y sin prefijo, y la forma de su cita), sin editar la respuesta; la cifra por brazo — 7 marcas del grafo, 4 de BM25
9. PASS: id opaco: B63J- y 10 hexadecimales, determinista, distinto por brazo, repetición y respuesta — B63J-c23549a538
10. PASS: el pedido del juez sin el brazo: el de construir_kwargs con la pregunta, la respuesta y los criterios; frena con el brazo o una clave de más — 3 fugas en las pruebas en contra
11. PASS: la guarda del juez: con lo gastado más el costo mayor sobre el freno, levanta FrenoJuez sin llamar — 0,0378 mientras no hay ninguna juzgada
12. PASS: una salida mal formada del juez: va a errores_r{rep}.jsonl y no se reintenta
13. PASS: la agregación: modal por criterio y el mapping de EV2; una respuesta sin sus tres repeticiones, incompleta — parcial
14. PASS: el patrón: el de guardas_lote trae el renglón 16 de a2_2/guardas_a2_2.zsh y correr_prueba_T_v2.py; el de prueba no corre con el CLI real ni con un nombre de un paso pago
15. PASS: el testigo, leído para B6.3: los renglones de la fecha del día se cuentan y no frenan; cualquier otro, sí
16. PASS: el enmascarado: calcular, probar y aplicar sobre copias de juguete; la carpeta personal pasa a $HOME y el original queda afuera — después de aplicar, probar frena
17. PASS: retomar: el sha256 de la entrada sin el tope ni el freno es el mismo si solo cambian esos dos, y otro si cambia otra cosa
18. PASS: el lanzador de una sesión: frena sin B63_CONFIG_AGENTES o con un sha256 que no da; la cadena de archivos del lanzador, con su sha256
19. PASS: el juez de EV2 sin editar: prompt v1 fd446f8e…, claude-sonnet-4-6, temperatura 0, y los sellos de la entrada

selftest B6.3: 19 de 19 en PASS.

## 6. La corrida en seco, rama por rama

Corrida en la copia final 2, con `env -i PATH HOME <repo>/.venv/bin/python -B data/experiment/banco_mcp/b63/corrida_en_seco_b63.py --tmp <carpeta temporal> --resultado <json>`, desde su raíz. Empezó en «seco 18:33:39» y terminó en «fin 18:37:49». Importa el runner de su carpeta y llama a sus funciones en modo real, con el CLI falso primero en el PATH y una clave de relleno. Las guardas buscan el token `prueba_b63_zq7xk2m4`; ningún `pgrep` lleva el patrón real. Las ramas:

- `R1_orden`: OK
- `R2_principal`: OK
- `R2_principal:fecha`: OK
- `R2_principal:cortes`: OK
- `R2_principal:infra`: OK
- `R2_principal:juez`: OK
- `R2_principal:d10`: OK
- `R2_principal:juez_sin_el_brazo`: OK
- `R2_principal:retomar`: OK
- `R3_corte_del_juez_y_su_cache`: OK
- `R4_guarda_del_gasto`: OK
- `R5_version_del_cli`: OK
- `R5_version_del_cli:version_distinta_en_--version`: OK
- `R5_version_del_cli:version_distinta_en_system_init`: OK
- `R5_version_del_cli:version_sellada_con_el_falso_del_banco`: OK
- `R6_R7_entradas`: OK
- `R6_R7_entradas:sin_BANCO_VENV_VECTOR`: OK
- `R6_R7_entradas:BANCO_VENV_VECTOR_que_no_existe`: OK
- `R6_R7_entradas:config_agentes_con_otro_sha256`: OK
- `R6_R7_entradas:config_servidor_con_otro_sha256`: OK
- `R6_R7_entradas:entrada_con_otro_sha256`: OK
- `R8_otro_paso_pago`: OK
- `R9_init_runner_igual_al_lote`: OK
- `R9b_init_para_el_testigo`: OK
- `R10_enmascarado`: OK
- `R12_disco_y_valor_remoto`: OK
- `R11_ningun_nombre_del_patron_real`: OK

27 de 27 en OK («corrida en seco de B6.3: 27 de 27 en OK», «rc_corrida_en_seco=0»). R11 va al final porque revisa las líneas de comandos de todas las demás.

Lo que dice cada rama, con sus cifras (`resultado_s2_B63a.json` del paquete):

- **R1, el orden:** 6 bloques (3 preguntas por 2 repeticiones).
  - Sale igual en dos llamadas, con los brazos dados en otro orden.
  - Es el de `random.Random(f"B63:orden_corridas:v1:{id}:{r}").shuffle` sobre los brazos ordenados, recomputado a mano.
  - `orden_b63.json` da los mismos bytes en dos corridas.
  - En R2, cada lote lanzó sus sesiones en el orden del bloque.
- **R2, la corrida principal:** 8 bloques, P = 3, el CLI falso de B6.3; código 0.
  - **La fecha:** el reloj fijado de la corrida en seco (`LOTE.RELOJ_FECHA`) cambia del 26/10 al 27/10 en la quinta sesión, dentro
    del bloque JUG02-r1. Hay 27 sesiones lanzadas: fragmentos_bm25: 1 el 2026-10-26, 7 el 2026-10-27; fragmentos_denso: 2 el 2026-10-26, 7 el 2026-10-27; kg: 1 el 2026-10-26, 9 el 2026-10-27. Los bloques con fechas distintas son
    `JUG02-r1` (§7).
  - **Los cortes:** la del grafo de JUG03 por `error_max_turns` y la de BM25 de JUG04 por `error_max_budget_usd` quedan como
    «cortada», y en la tabla del juez hay 0 de ellas.
  - **La infraestructura:**
    - la del denso de JUG05 falló sin `result` en el intento 1 y terminó en el 2 (intento 1: falla_infra; intento 2: completa). Su reintento corrió antes del
      primer lote de JUG06: sí;
    - la del grafo de JUG06 falló con `is_error` en los tres intentos (intento 1: falla_infra; intento 2: falla_infra; intento 3: falla_infra) y quedó «falla_infra_sin_terminar»;
    - los ids de los reintentos: `B63-JUG05-r1-fragmentos_denso-i2`, `B63-JUG06-r1-kg-i2`, `B63-JUG06-r1-kg-i3`;
    - las sesiones con falla de infraestructura, por brazo: fragmentos_bm25, 0, fragmentos_denso, 1, kg, 3.
  - **El juez:**
    - 21 respuestas completas, y 21 en la tabla;
    - 63 pedidos al transporte simulado: 3 por respuesta, porque cada respuesta es distinta;
    - por repetición, 20 veredictos y 1 error: la salida mal formada
      del denso de JUG07, sin reintento.
  - **D-10:** de los 63 pedidos, 63 llegaron al
    transporte con la cuenta de D-10 de su respuesta ya escrita en la tabla. La respuesta de juguete de JUG02, con una marca de su
    brazo, quedó contada en los tres brazos (fragmentos_denso: sí, fragmentos_bm25: sí, kg: sí). En cada brazo hay 1 con marca y 0 editadas.
  - **El juez sin el brazo:** 63 de 63 pedidos traen solo
    `model`, `max_tokens`, `temperature`, `system` (el prompt v1) y un mensaje. Fuera de la respuesta, el mensaje no trae ningún brazo,
    ningún id de sesión ni ningún id opaco.
  - **Retomar:** una instancia nueva del runner, con la misma entrada, termina con el código 0, con
    0 sesiones nuevas y 0 pedidos nuevos.
- **R3, el corte del juez y su caché:**
  - con P = 1, el freno en 5,42 y tres sesiones de USD 1,79, el juez corta con el código 2 después de la
    primera respuesta (3 pedidos);
  - se simula un corte entre la tercera repetición pagada y su registro;
  - al retomar con el freno en 6,00 (la entrada cambia solo el tope y el freno; el estado registra 2
    entradas), hay 6 pedidos nuevos y 1 acierto de la caché: la
    repetición pagada no se vuelve a pagar.
- **R4, la guarda del gasto, la misma para el agente y el juez:** con el freno en 4,00:
  - el peor caso al lanzar cada sesión es 1.8, 3.6, 3.6 USD;
  - el segundo bloque recibe como freno 1.2136, que es 4,00 menos lo gastado por el agente y el juez
    (2.7864), y no lanza ninguna (código 2).
- **R5, la versión del CLI:**
  - con otra en `--version`, código 6, sin lanzar nada
    (0 carpetas de configuración);
  - con el CLI falso del banco y su plan que cambia el `system/init`, código 6;
  - con la sellada, en el mismo falso del banco, código 0.
- **R6 y R7, las entradas:** sin BANCO_VENV_VECTOR, con uno que no existe, con otro sha256 de `config_agentes` o de un
  `config_servidor` y con otro sha256 del comando: las cinco frenan con el código 10, sin crear ninguna carpeta de sesiones.
- **R8, otro paso pago:** con `python3 <tmp>/procesos_de_prueba/prueba_b63_zq7xk2m4.py` vivo, que solo espera su entrada estándar,
  el runner, como proceso aparte, termina con el código 7.
  - Lanzó 0 sesiones y creó
    0 carpetas de configuración; encontró
    `prueba_b63_zq7xk2m4.py`.
  - Al cerrarle la entrada, el proceso termina con 0, y el runner, con
    0 y 3 sesiones.
  - El patrón de las dos corridas es el del token: `prueba_b63_zq7xk2m4\.py`.
- **R9 (4 bis):** 3 de 3 sesiones init del runner tienen
  la misma línea de comandos que la del lanzador del lote, byte a byte salvo el `--session-id`, y los mismos nombres del entorno
  (ANTHROPIC_API_KEY, ANTHROPIC_BASE_URL, BANCO_LOG_R1, BANCO_REPO, BANCO_SESION_TAG, BANCO_VENV_VECTOR, CLAUDE_CONFIG_DIR, DISABLE_AUTOUPDATER, HOME, MCP_TIMEOUT, PATH).
  - Los únicos valores distintos son `BANCO_LOG_R1`, `CLAUDE_CONFIG_DIR`: los de
    cada sesión.
- **R9b:** el lote init de referencia del testigo, con los brazos de su `TANDAS` (`fragmentos_bm25`, `fragmentos_hibrida`, `kg`), y su
  `comparar_con_init` sobre él: 3 de 3 en PASS.
  - Prueba que el testigo encuentra y lee ese lote init. La comparación con sus propias sesiones es de la etapa b (§9).
- **R10, el enmascarado de R2:**
  - 54 archivos (27 streams y 27 transcripciones), con 27
    reemplazos;
  - después, 0 con la carpeta personal de juguete;
  - los originales, fuera, con su sha256: sí.
- **R11:** 309 líneas de comandos anotadas (las de las guardas, el lanzador del lote, el runner y los procesos
  de prueba).
  - 0 con un nombre del patrón real;
  - 45 `pgrep`, 45 con el token;
  - los nombres de los procesos de las sesiones con un nombre del patrón: ninguno.
- **R12, el disco y el valor remoto:**
  - con la marca del disco en la transcripción de la sesión del grafo de JUG14, el runner frena con el código 11 sin
    lanzar el bloque siguiente;
  - con el `.claude.json` de juguete de JUG15, la lectura acotada encuentra la clave en los tres brazos, con
    `mcp__fragmentos__buscar_pasajes`, `mcp__kg__buscar_nodos`.

## 7. La cuenta por brazo y por fecha de la corrida en seco

En R2, la corrida principal de la corrida en seco, hay 27 sesiones lanzadas, contando los reintentos: fragmentos_bm25: 1 el 2026-10-26, 7 el 2026-10-27; fragmentos_denso: 2 el 2026-10-26, 7 el 2026-10-27; kg: 1 el 2026-10-26, 9 el 2026-10-27.

- El bloque JUG02-r1 es el que cruza la medianoche: su primera sesión, el 26/10, y las otras dos, el 27/10.
- El cambio lo da el reloj fijado de la corrida en seco, el mismo mecanismo de la del banco en paralelo.
- La cuenta la escribe el runner en `fechas_b63.json`, sin ningún texto: por brazo y por fecha, por fecha, y los bloques con fechas distintas por brazo.

## 8. Lo que la etapa b necesita de la entrada sellada

La entrada sellada es un JSON que arma la mesa. El comando pago le pasa su sha256 en `--sha256-entrada`, y el runner frena con el
código 10 antes de lanzar nada si algo no da (`comun_b63.cargar_entrada`). Lo que trae:

| campo | qué es | lo que controla el runner |
|---|---|---|
| `preguntas` | `{ruta, sha256, ids_en_orden, esquema}`: el archivo de las preguntas de B6.3 que entran por el N, y sus ids en el orden de las olas aprobadas (§6). `esquema` dice dónde está cada campo; por omisión, el de EV2: `preguntas[*].{id, pregunta, gold.criterios[*].{criterio, cita_textual}}` | el sha256; que cada id esté, sin repetirse, y que el lanzador del lote lo admita; que cada pregunta tenga texto y cada criterio, su texto y su cita. Nada se imprime |
| `k` | las corridas por pregunta y por brazo (H-7) | un entero de al menos 1 |
| `config_agentes` | `{ruta, sha256}`: una sola configuración de agentes con los tres brazos, dentro de `data/experiment/banco_mcp/`, con la forma de `paralelo/config_agentes_n6_prueba.json` (su `base` con su sha256, `claude_code_version_sellada`, el modelo, el modo, `brazos` con `mcp_config`, `bloque_tools`, `allowed_tools`, `tools_esperadas`, `config_servidor` y `archivos_servidor`, `prompt.plantilla`, `corte_R5` y `env_por_sesion.MCP_TIMEOUT`) | el sha256; su base; que sus brazos sean los de `brazos`; que existan sus archivos; la versión sellada del CLI, que usa la guarda del lote |
| `brazos` | `{nombre: {rol, config_servidor: {ruta, sha256}, marcas_d10?}}`, con los roles `grafo` (la configuración de N7), `fragmentos_principal` y `fragmentos_denso` | los tres roles, una vez cada uno; el sha256 de cada `config_servidor`, y que sea el que nombra `config_agentes` |
| `R5` | `{max_turns, tope_tool_calls_prompt, max_budget_usd}` | que sea el de `config_agentes` y el `R5_ESPERADO` del lanzador del lote (32, 30 y 1,80) |
| `tope_usd`, `freno_usd` | el tope del §12, recalculado al sellar N7, y su freno, para el agente y el juez juntos | 0 ≤ freno ≤ tope |
| `banco_venv_vector` | `{ruta, python}`: el venv de `BANCO_VENV_VECTOR` (por ejemplo `~/INGENIERIA IA/TESIS/venvs/banco_vector_py312`) y la versión de su Python (la que da `<ruta>/bin/python --version`; en esta máquina, 3.12.13, medida por `comun_b63.version_python` en la corrida en seco) | que esté, que exista y que su Python dé esa versión. Sale de acá y nunca de la terminal (`correr_b63.preparar_entorno`) |
| `juez` | `{archivos: [{ruta, sha256}]}`: `data/experiment/ev2_juez/juez.py`, `mapping.py` y `prompt_juez_v1.md`, con su sha256 de HEAD (`b4a74ba5…`, `c905dd1a…` y `fd446f8e…`) | el sha256 de los tres archivos que importa el juez, y el instrumento (`juez_b63.controlar_instrumento`) |
| `P` | las sesiones a la vez (3, §5) | un entero de al menos 1 |

Fuera de la entrada:
- `ANTHROPIC_API_KEY` la pone el comando pago de la autora, como en A2.2.
- `NEO4J_URI` pasa desde la terminal, por la lista cerrada (§88).
- Los valores por omisión del runner:
  - las sesiones, en `~/INGENIERIA IA/TESIS/fuera_del_repo/banco_b63/sesiones/`, y sus lotes, en `sesiones/lotes/`;
  - las salidas, en `b63/resultados/real/`;
  - el juez, en `b63/juez/`;
  - los originales sin enmascarar, en `~/INGENIERIA IA/TESIS/fuera_del_repo/banco_mcp_originales_B63/`.
- El runner no controla el sha256 del `pip freeze` del venv del banco que nombra el §5 (`24f4c064…`): si la etapa b lo quiere en la
  entrada, es un campo más.

## 9. El testigo en la etapa b (punto 4 bis)

El control del testigo es el del banco en paralelo: `aislamiento/testigo_aislamiento.py`, `fase_testigo`, en HEAD `e600e187…`, sin
cambiarlo. Arma sus propias sesiones selladas con la captura del pedido a USD 0 y compara cada una con la sesión del mismo brazo de un
lote init de referencia, que recibe en `--init`. Lo hace con `comparar_con_init`, `:394-412`: la línea de comandos, salvo el
`--session-id`, y los nombres del entorno, con `ANTHROPIC_BASE_URL` como única diferencia admitida fuera de las variables de cada
sesión.

Para que esa referencia sean sesiones lanzadas por el runner, la etapa b corre esto:
1. **El lote init del runner:** `correr_b63.lote_init(e, out=<carpeta>, sesiones=<raíz>, lotes=<carpeta de lotes>, n=1,
   config_agentes={"ruta": "data/experiment/banco_mcp/paralelo/config_agentes_n6_prueba.json", "sha256": "479d83a1…"})`.
   - `e` es la entrada sellada ya controlada: `correr_b63.controles(<entrada>, <sha256>, "init")`.
   - Lanza, por `CorridaB63.correr_lote` (el camino de las corridas, en modo init), una sesión por brazo de esa configuración, con
     ids `B63-I1-r1-<brazo>`, que terminan con el brazo, como los busca el testigo, y la pregunta de prueba `PREGUNTA_INIT`, sin
     ninguna de B6.3.
   - Devuelve, en `lotes[0]["salida"]`, la carpeta que va en el `--init` del testigo.
   - `config_agentes` es la de prueba de N6 porque el testigo arma sus sesiones con ella: `N6.cargar_cfg()`, `:417`, con los brazos
     de `TANDAS`, `:76` (kg, fragmentos_bm25 y fragmentos_hibrida). Con otra configuración, su `comparar_con_init` no encuentra la
     referencia de un brazo o compara líneas de comandos de dos configuraciones distintas (§10).
2. **El testigo:** `testigo_aislamiento.py --init <salida del punto 1>`, con sus demás parámetros como en el banco en paralelo:
   `--out`, `--sesiones`, `--tmp`, `--privado` y `--banco-paralelo`, con `NEO4J_URI`.
3. **La fecha:** `correr_b63.leer_testigo(<el JSON del testigo>)`, por la decisión del punto 1.b.
   - El testigo, sin cambios, pone en su FRENO un renglón por cada pedido y campo en que aparece la fecha del día, de la forma «<id>,
     pedido <n> (<tipo>), <campo entre comillas invertidas>: la fecha del día (<k> apariciones)» (`:529-531`).
   - `leer_testigo` separa esos renglones, los cuenta por tipo de pedido y por campo (`fecha_por_tipo_y_campo`) y los declara: la
     fecha la pone el CLI, «El agente recibe la fecha del día en su pedido: la pone el CLI».
   - Cualquier otro renglón de FRENO sigue siendo un FRENO.
   - `PASS_de_B63` es el PASS del testigo sin los renglones de la fecha. `PASS_del_testigo_tal_cual` queda al lado.
   - Si el testigo cruza la medianoche, el sha256 de `system` deja de ser uno por brazo y tipo de pedido, porque `system` trae la
     fecha. Esos renglones del testigo no son de la fecha y quedan como FRENO: lo decide la mesa. NO VERIFICADO, como en la nota de
     `617f6652`.

## 10. Lo que encontré y declaro

1. **El lanzador del lote dice otra cosa sobre la fecha.** Su docstring, en HEAD, dice: «el agente no recibe la fecha en su pedido, como
   en A2.2, y el testigo lo controla» (`agentes/lanzar_lote_paralelo.py:37-38`). La decisión de la autora del 26/10/2026, recibida a
   las 16:07:59, dice lo contrario, y la nota de `617f6652` la registra. No edité el lanzador: el runner no cambia ni saca la fecha del
   pedido, y la declara. El docstring queda para la próxima nota.
2. **El R5 del lanzador del lote está fijo.** Su `R5_ESPERADO` es 32, 30 y 1,80 (`:73`), y en modo real frena con el código 5 después
   de una sesión con otro R5 (`control_aislamiento`, `:363-364`). Si N7 sube R5 (§5: 45, 47 y 3,30; H-6), el lote frena después de
   pagar la primera sesión. Por eso el runner lo controla antes de lanzar nada y frena con el 10. La subida de R5 pide otra versión
   del lote, que no está en el alcance de esta etapa.
3. **El testigo está atado a la configuración de prueba de N6** (`testigo_aislamiento.py:417` y `:76`). Su `comparar_con_init`
   prueba que el camino del runner arma la misma línea de comandos y el mismo entorno que el del testigo con esa configuración, no
   con la sellada de B6.3, que va a tener otro `mcp_config` en el grafo (N7) y el brazo denso.
   - Lo que dice de B6.3 sale de dos cosas: que la línea de comandos y el entorno los arman el mismo código (`lanzar_agente.py` y
     `lanzar_agente_n6_prueba.py`, importados sin editar) y la misma lista cerrada; y la comparación del 4 bis (R9).
   - Si la mesa quiere el testigo con la configuración sellada de B6.3, el testigo necesita un parámetro para su configuración: es un
     cambio en `aislamiento/`, fuera de esta etapa.
4. **Un bloque a la vez.** El runner corre un lote del lanzador del lote por bloque (una pregunta y una repetición) y, en el mismo
   lugar del orden, los reintentos de infraestructura. Con P = 3 y tres brazos, las tres sesiones de un bloque corren a la vez y el
   bloque siguiente espera a que termine el anterior. Con un solo lote para todo, como en el banco en paralelo, los bloques se
   pisarían y un reintento no podría ir en su lugar del orden.
5. **La forma del error de la API es NO VERIFICADA.** Que una sesión cortada por el presupuesto termina con `subtype`
   `error_max_budget_usd` e `is_error` está anclado: las salidas reales de `gate/corrida_faseB/salidas_claude/` lo traen, por ejemplo
   `run_GATE-03.json`. La de `--max-turns`, `error_max_turns`, sale de A2.1 (`a2_1/lanzar_agente_a2_1.py:108`). La de un error de la API o
   de la red no está en el repo.
   - El runner toma como falla de infraestructura una sesión sin `result` (antes del timeout del lanzador) o con un `result` con
     `is_error` y un subtype que no es de corte.
   - El CLI falso de B6.3 prueba las dos formas.
   - Si el CLI real diera otra forma (por ejemplo, un `result` sin `is_error` que no trae el JSON final), la sesión quedaría como
     `incompleta_otra`, que no se re-corre ni se juzga y se declara.
6. **La guarda de una extracción** (código 9, `guardas_lote.extraccion_corriendo`) la agregué yo, antes de cada bloque. El §6 dice
   «nunca al lado de una extracción», y el lanzador del lote solo la trae en el humo. Lee `ps` y no hace ningún `pgrep` con un patrón.
7. **`correr_b63.py` no está en el patrón de otro paso pago.** Las guardas de los otros comandos pagos (`guardas_lote.PATRON_PAGO`)
   no lo ven mientras corre. No lo agregué: es un cambio fuera de `b63/`. Lo nombro para la mesa.
8. **Retomar.** El runner retoma con la misma entrada, o con una que cambie solo el tope y el freno: `estado_b63.json` registra cada
   una. Así sigue el juez después de un corte, sin repetir ningún bloque terminado. La caché del juez de B6.3 queda en
   `b63/juez/cache/` y guarda el pedido entero, como la de A2.2.
9. **Lo que la corrida real deja en el repo trae texto de las preguntas,** como en A2.2.
   - La carpeta de cada sesión, en `b63/resultados/real/<bloque>/lote<n>/<id>/`, trae su `prompt_<id>.txt` (la plantilla con la
     pregunta). Lo escribe el lanzador sellado.
   - Su stream y su transcripción, enmascarados, también traen la pregunta.
   - La caché del juez, en `b63/juez/cache/`, guarda el pedido entero, con la pregunta, los criterios, las citas y la respuesta. En
     A2.2 esas bases quedaron sin rastrear.
   - El lote que lee el lanzador del lote, con las preguntas, va fuera del repo, en `<sesiones>/lotes/`.
   - En esta etapa todo eso fue de juguete y quedó en la carpeta temporal.

## 11. Los criterios de aceptación

| # | criterio | dónde | resultado |
|---|---|---|---|
| 1 | el paso 0 | §2; `paso0_B63_a_B63a.txt` | lo esperado; un paquete restaurado de la copia permanente, 93 de 93 |
| 2 | el selftest y la corrida en seco, enteros, con sus casos y las ramas del punto 4 | §5 y §6 | selftest B6.3: 19 de 19 en PASS; corrida en seco de B6.3: 27 de 27 en OK |
| 3 | el juez de EV2 importado con el sha256 de HEAD, sin editarlo, y el pedido sin el brazo | §5, casos del juez; §6, R2 | `juez.py` `b4a74ba5…`, igual en HEAD y en el árbol; 63 de 63 pedidos sin el brazo |
| 4 | en el repo cambia solo `b63/`, todo nuevo, con la foto antes y después y los `.pyc` | §12 | 24 nuevos en `b63/`, 0 fuera; `.pyc` 10158 y 10158 |
| 5 | el grep de convenciones (`LC_ALL=en_US.UTF-8`), 0 en lo que escribí | §14 | total por término: {} — total 0 |
| 6 | la línea de comandos y los nombres del entorno de una sesión del runner, iguales a los del lanzador del lote | §6, R9 | 3 de 3 |
| 7 | la cuenta por brazo y por fecha con el bloque que cruza la medianoche; la guarda de la versión del CLI frena con otra versión | §7; §6, R5 | `JUG02-r1`; códigos 6 y 6, y 0 con la sellada |
| 8 | ningún proceso de prueba ni `pgrep` con un nombre del patrón real | §6, R11 | 0 de 309 líneas; 45 de 45 `pgrep` con el token |

## 12. El repo, antes y después

- **La foto** (`foto_repo.py`: el sha256 de cada archivo del repo, sin `.git`; los `.env` y los `NO_ABRIR_*`, solo por su tamaño y su fecha): antes, a las 17:41:05, 60944 entradas; antes de escribir este FRENO, 60968.
- **Entre las dos** (`comparar_fotos_b63.py`): 24 nuevos, todos en `b63/` (24); 0 borrados; 1 cambiados, del volumen de Neo4j; y 0 fuera de lo autorizado.
- **El volumen de Neo4j:** 0 nuevos, 0 borrados y 1 cambiados. El contenedor sigue levantado desde A2.2, y esta etapa no lo usó.
- **Los `.pyc`:** 10158 y 10158; fuera de los venvs, 243 y 243.
- **`git status --porcelain --untracked-files=no`:** vacío.
- **Fuera del repo:** no escribí en `fuera_del_repo/banco_b63/` ni en `banco_mcp_originales_B63/`; las dos siguen sin existir. Las sesiones de las pruebas quedaron en la carpeta temporal de la sesión.
- **Después de escribir este FRENO** tomo la foto final. Su comparación con la de antes va en el paquete (`comparacion_antes_vs_al_frenar_B63_a.json`); lo esperado es un archivo nuevo más, este FRENO, también en `b63/`.

## 13. Errores propios, con su causa

1. **Un índice de carpeta mal en las herramientas de la corrida en seco.**
   - El error: en `seco/herramientas_seco.py`, `REPO = BANCO_DIR.parents[1]` daba `data/` en lugar de la raíz del repo.
   - El efecto: la primera prueba de humo, de un bloque, frenó con «config_agentes: no existe experiment/…».
   - La causa: conté mal los niveles de `parents`.
   - El arreglo: `parents[2]`, que es la raíz que da `comun_banco.REPO_DIR`.
2. **El humo no contaba bien los pedidos al juez.** Llegaron 3 pedidos y se escribieron 9 repeticiones.
   - No era un error del juez: las tres respuestas de juguete eran el mismo texto, y la caché contestó las repeticiones idénticas.
   - Lo cambié en el CLI falso, para que cada sesión dé una respuesta propia; si no, las cuentas de la corrida en seco no prueban
     nada.
3. **La primera versión del corte del juez en R3 no simulaba bien el corte.** Borraba la línea de la repetición sin devolver la
   respuesta a los pendientes del runner, cosa que un corte real no hace. Lo vi antes de correrla.
   - Al corregirla, mi primer reemplazo frenó en su propio control: la palabra «primero» estaba también en la cabecera del archivo, y
     no escribió nada. Lo hice otra vez sin ese control.
4. **Me faltaban dos piezas del §5 en el diseño:** la lectura acotada de `tengu_velvet_ibis` y el control del disco.
   - La causa: di por hecho que las traía el lanzador del lote, y las traían los runners de A2.1 y de A2.2.
   - Lo encontré al redactar el FRENO, después del intento 2, buscando dónde se leía la clave (`velvet`: solo en
     `a2_1/correr_a2_1.py` y en las corridas en seco de A2.1 y A2.2).
   - Las agregué en el lanzador de la sesión de B6.3, con las funciones de A2.1 sin editar, con el código 11 en el runner y la rama
     R12.
5. **Horas sin ancla en el checkpoint.** Escribí «~18:15», «~18:40», «~19:10» y «~19:30» a ojo, y varias estaban mal: la corrida en
   seco del intento 1 fue de las 18:11:48 a las 18:14:49. Lo corregí en el mismo checkpoint, con las horas de las salidas.
6. **Un comando de búsqueda falló en zsh.** El `--include=*.py` de un grep no encontró coincidencias para el glob y cortó el comando.
   Lo repetí sin esa opción. Era una lectura y no tuvo efecto.
7. **La copia final 1 dio 26 de 27: R8 falló por el largo de una ruta de prueba.**
   - Al cerrarle la entrada al proceso de prueba, el runner terminó con el código 5 en lugar del 0.
   - Las tres sesiones quedaron en «falló el lanzador»: el lanzador sellado (`LA.copiar_sesion`) frenó con «File name too long».
     El CLI guarda la transcripción en `projects/<slug del cwd>/`, y el slug es un solo nombre de archivo, con un tope de 255. Con la
     carpeta temporal de la copia final, el de esa rama tenía 257 caracteres; en el intento 3, 252.
   - La causa: los nombres largos de las carpetas de prueba, que no medí.
   - Con la raíz real de B6.3 el slug tiene 85 caracteres.
   - El arreglo, en la corrida en seco: nombres cortos para esa rama, y un control que frena antes si el slug de prueba pasa de 230.
     La pasé al repo con la lista de sha256 rearmada y repetí la copia final (la 2).
   - Las salidas de la copia final 1 van en el paquete.

## 14. Grep de convenciones

- `data/experiment/segmentacion_oficial_e0r2/s0_4/scripts/grep_convenciones.py`, con `LC_ALL=en_US.UTF-8`, sobre copias de los archivos de `b63/` y del borrador de este FRENO: control positivo: 16 de 16 términos encontrados; archivos revisados: 25; total por término: {} — total 0 (`grep_convenciones_b63_y_freno_B63a.txt`).
- Después de escribir el FRENO en el repo, lo corro otra vez sobre él y sobre los archivos del paquete ya enmascarados. Esa salida, con sus cuentas por archivo y por término y la explicación de cada una, va en el paquete (`grep_convenciones_paquete_B63a.txt`).

## 15. El paquete

- **El paquete:** `revision_B63_FRENO_a/`, en la carpeta temporal de la sesión, con su `manifest.txt`.
- **La copia:** con `ditto`, en `~/INGENIERIA IA/TESIS/fuera_del_repo/scratchpads/94968c98-6fa5-449c-954b-42ee7ee26062/scratchpad/revision_B63_FRENO_a/`, verificada contra su `manifest.txt` (`armar_manifest.py --verificar`).
- **Lo que lleva:**
  - este FRENO y los archivos de `b63/`;
  - el pre-registro leído en su firma;
  - los controles y las salidas de los tres intentos y de las dos copias finales;
  - los resultados de las corridas en seco;
  - las fotos, enmascaradas, y sus comparaciones;
  - los scripts de la carpeta temporal y el checkpoint.
