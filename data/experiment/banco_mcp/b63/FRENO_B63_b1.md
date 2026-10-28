# FRENO B6.3-b1 — lo que no depende de N7 ni es pago (27/10/2026)

Unidad: B6.3, etapa b1 del runner. Mientras corría N6 hice lo que no depende de N7 ni es pago: USD 0, sin Neo4j, sin Docker y sin el
denso. La única llamada a la API fue la de la clave inválida: la API la rechazó con un 401 y `total_cost_usd` 0 (§3). En el repo
escribí solo archivos nuevos, en `data/experiment/banco_mcp/b63/v2/` (19), más su lista de sha256 y este FRENO. No commiteé nada.
Espero la revisión.

Los artefactos largos van en el paquete `revision_B63_FRENO_b1/` (§16), por su nombre.

## 0. Los criterios

| # | criterio | dónde | resultado |
|---|---|---|---|
| 1 | el paso 0, con lo que restauré | §1 | lo esperado; restauré el paquete de la etapa a y tres scripts desde la copia permanente |
| 2 | el diff de cada archivo nuevo contra su original de HEAD | §2 | 10 diffs en el paquete; `memoria_maquina`, igual a la de N6 |
| 3 | las formas reales: subtype, is_error, result y la clase del runner | §3 | 4 de falla de infraestructura y 1 desconocida |
| 4 | la atribución, el Neo4j, la P con su guarda y el juez a la vez, Docker, cada uno con su selftest | §4 a §8 | todos en PASS; en la atribución, el stream no está en la meta: falta, sin arreglar |
| 5 | el selftest, rama por rama, y las dos corridas iguales | §9 | 22 de 22 en PASS, dos veces; las dos salidas, iguales byte a byte |
| 6 | ningún proceso mío corrió un script del patrón | §10 | la lista de lo que lancé, por nombre: ninguno en el patrón |
| 7 | el repo: solo archivos nuevos en `b63/`, con su sha256; lo demás, igual antes y después; el grep, 0 | §11 y §15 | 19 nuevos en `b63/v2/`; 60.264 entradas comparadas, 0 cambian; grep 0 |

Hubo errores propios: dos de ellos leyeron archivos `*_SOLO_MESA*` para calcular su sha256 (§13).

## 1. El paso 0

Salida: `paso0_B63_b1.txt` (27/10/2026 20:54:50).
- **Lo que restauré.** La carpeta temporal de la sesión estaba vacía (recreada el 27/10 a las 18:04). Restauré con `ditto`, desde la
  copia permanente, `revision_B63_FRENO_a/` (20:54:38): 60 de 60 contra su `manifest.txt`, igual al permanente (`bf66679d…`). De él
  saqué `foto_repo.py` (`a377b766…`), `armar_manifest.py` (`5a7db724…`) y `enmascarar_paquete.py` (`65eaf9a2…`).
- **El repo.** `pwd` = `$HOME/INGENIERIA IA/TESIS/bcra-regulatory-kg`. HEAD = `800f3d14`, con `05999ad6` y `dbf2eef4` en su historia.
  `git status --porcelain --untracked-files=no` vacío; `b63/` sin nada sin rastrear.
- **Lo de HEAD.** `b63/sha256_etapa_a_b63.txt`: `shasum -c` OK (23 archivos). Los tres archivos de r5 están en HEAD y en el árbol, iguales:
  - `lanzar_lote_paralelo_r5.py`, `73b21753…`;
  - `guardas_lote_r5.py`, `04f81fe3…`;
  - la NOTA, `17b738b0…`.
- **La foto antes:** 20:55:38, 60.288 entradas (`foto_antes_B63b1_sin_sha_SOLO_MESA.json`). La tomó `foto_repo_b1.py`, que poda sin
  entrar 13 carpetas: las 12 vedadas y `b63/`. Leyó 24 archivos `*_SOLO_MESA*` (§13, error 1).

## 2. Los archivos nuevos y sus diffs contra HEAD

Todos en `b63/v2/`, sin rastrear. Ningún archivo de HEAD editado: `git diff --stat HEAD` vacío.

Los diffs están en el paquete, en `diffs/`, generados por `diffs_b1_B63b1.py` con `git show HEAD:<ruta>`; las funciones copiadas, por su segmento de `ast`.

| archivo de `b63/v2/` | original de HEAD | +/− |
|---|---|---|
| `comun_b63.py` | `b63/comun_b63.py` | +58 −23 |
| `lanzar_agente_b63.py` | `b63/lanzar_agente_b63.py` | +10 −7 |
| `correr_b63.py` | `b63/correr_b63.py` | +343 −283 |
| `juez_b63.py` | `b63/juez_b63.py` | +104 −4 |
| `selftest_b63.py` | `b63/selftest_b63.py` | +440 −313 |
| `seco/claude_falso_b63.py` | `b63/seco/claude_falso_b63.py` | +24 −7 |
| `seco/config_agentes_b63_juguete_r5b.json` | `b63/seco/config_agentes_b63_juguete.json` | +4 −4 (el R5 B: 47, 45 y 3,30) |
| `ventana_b63.py`, `LoteVentana.correr` (`:69-169`) | `agentes/lanzar_lote_paralelo.py`, `Lote.correr` (`:409-489`) | +24 −4: el camino sin R5 admitido (el `correr` del lote de r5), los dos ganchos, un `break` después del freno de otro paso pago y las constantes con `BASE.` |
| `memoria_b63.py`, `memoria_maquina` (`:24-36`) | `n6/memoria_n6.py`, `memoria_maquina` (`:109-121`) | +0 −0: igual |
| `control_neo4j_b63.py`, `estado` (`:31-63`) | `paralelo/control_neo4j_propio.py`, `estado` (`:27-57`) | +24 −22: la URI y la huella esperadas, la configuración por parámetro (la del grafo evaluado), los dobles `ck` y `abrir`, y la huella de contenido siempre, controlada además del `KG_Meta` |

Los que no tienen original en HEAD: `docker_b63.py`, `levantar_neo4j_b63.zsh`, `formas_error_b63.py`, `formas_reales_b63.json`, y en
`seco/` `servidor_errores_b63.py`, `lanzador_falso_ventana.py`, `herramientas_b1.py`, `planes_b63_seco_v2.json` y
`preguntas_ventana_b63.json`.

Lo que trae cada pieza del despacho:
- **La NOTA r5.** `comun_b63.py` importa `lanzar_lote_paralelo_r5` como el lote. `cargar_entrada` admite solo los dos R5, con su
  `admitido()`; cada pasada arma el `Namespace` del lote con `entrada` y `sha256_entrada`.
- **La entrada.** Suma:
  - `banco_venv_vector.pip_freeze_sha256`, que el runner recalcula con `pip freeze --all` del venv y compara: con el del banco da
    `24f4c064…` (registro, §126, decisión 6, `:5424`);
  - `P`, en {1, 2};
  - `pico_sesion_gb`, mayor que 0;
  - `neo4j`: el uri `bolt://127.0.0.1:47687` y una huella de 64 hexadecimales.
- **El patrón de las guardas.** `PATRON_B1` = `guardas_lote_r5.PATRON_PAGO_REAL` + `|lanzar_lote_paralelo_r5\.py|correr_n6\.py`
  (`correr_b63.py:56-58`).
- **La ventana corrida.** Hasta P sesiones a la vez, en el orden firmado. Cada reintento va al primer lugar libre, con una tanda nueva, y
  hay hasta 3 intentos por brazo (§127, decisión 4).
- **La opción (d).** Una forma desconocida deja la sesión incompleta y se declara. Con la tercera, el lote frena con el código 12 (§127,
  decisión 3).

## 3. Las formas reales del error

Las medí con el CLI real sellado (2.1.241), lanzado directamente, con la configuración de juguete y el brazo kg, sin el lote. El script es
`b63/v2/formas_error_b63.py`; las salidas, `formas_error_corrida{1,2,3}_B63_b1.json` y sus consolas.
- La clave inválida la armé con `secrets` y no es ninguna clave real: nunca la imprimí ni la guardé.
- En las 8 sesiones, ninguna salida (stream, stderr ni transcripción) la trae: 0.
- `apiKeySource` = `ANTHROPIC_API_KEY` en todas.
- Los 8 streams van en el paquete, enmascarados (`stream_formas_<caso>_corrida<n>_B63b1.jsonl`); ninguno trae el prefijo de la clave.

| caso | URL base | rc | result | subtype | is_error | api_retry | error_status | clase del runner |
|---|---|---|---|---|---|---|---|---|
| http_429 | servidor local `/c429` | 1 | sí | success | true | 10 | 429 (rate_limit) | falla_infra |
| http_500 | servidor local `/c500` | 1 | sí | success | true | 10 | 500 (server_error) | falla_infra |
| http_529 | servidor local `/c529` | 1 | sí | success | true | 10 | 529 (overloaded) | falla_infra |
| puerto_cerrado | `127.0.0.1:9` | 1 | sí | success | true | 10 | None (unknown) | falla_infra |
| clave_invalida | la API | 1 | sí | success | true | 0 | — (`api_error_status` 401) | desconocida |

- **Las corridas.**
  - Corrida 1, de 21:01:31 a 21:13:47: los cuatro primeros casos.
  - Corrida 2, de 21:14:40 a 21:17:39: la clave inválida fue al servidor local y no a la API (§13, error 3).
  - Corrida 3, de 21:18:55 a 21:22:06: la clave inválida fue a la API, sin `ANTHROPIC_BASE_URL` en el entorno de la sesión. Dio
    `api_error_status` 401, `terminal_reason` `api_error`, `total_cost_usd` 0 y uso 0 y 0, en 2,4 s.
- **El 429** dio la misma forma en las tres corridas: result, subtype, is_error, 10 api_retry, error_status y rc. Lo controla
  `armar_formas_reales_B63b1.py`.
- **Si el CLI reintenta solo.** Contesta 10 eventos `api_retry` y hace más pedidos que esos. Los POST a `/v1/messages`, todos con la
  clave inválida, fueron:
  - 429: 21, 22 y 22, en las corridas 1, 2 y 3;
  - 500: 22;
  - 529: 12.
  En cada caso del servidor hubo además un HEAD `/api/hello` sin clave.
- **Lo que compara el runner.** `b63/v2/formas_reales_b63.json` guarda por caso: si hay result, subtype, is_error, los api_retry (su
  cantidad, sus error_status y su error), rc, duración, URL base y clase, sin ningún texto. `correr_b63.clasificar` compara hay_result,
  subtype, is_error y el conjunto de los error_status. Las cinco formas reales tienen el mismo result (success, con is_error), así que lo
  único que las distingue es el error_status de sus reintentos. La clave inválida no tiene ninguno, y por eso no coincide con ninguna
  forma de infraestructura.
- **La clase de la clave inválida: desconocida.** No es un error de la API ni de la red: es uno de configuración, que se repetiría en
  todas las sesiones. Con la opción (d), las 3 primeras sesiones frenan el lote. La decisión es de la autora: la dejo PREPARADA (§14).
- **El CLI falso v2** (`seco/claude_falso_b63.py`, planes `seco/planes_b63_seco_v2.json`) suma un plan `forma_real: <caso>`. Emite,
  después del system/init y sin ninguna tool, los api_retry y el result medidos, y sale con el rc medido. El selftest lo corre por el
  lanzador v2 con cada forma, y el runner da la clase de la tabla (§9).

## 4. La atribución

Cada sesión deja en su carpeta su stream (`stream_<id>.jsonl`) y su log R1 (`log_r1_<id>.jsonl`). La meta trae el log R1, con su ruta y su
sha256. **El stream no está en la meta: falta.** No lo arreglé: el despacho pide decirlo y no arreglarlo sin preguntar. Lo mide el caso de
la atribución del selftest, con el CLI falso de la etapa a y el lanzador v2.

## 5. El Neo4j de B6.3, solo como código

- `levantar_neo4j_b63.zsh` (no lo corrí; `zsh -n` OK). Uso: `zsh levantar_neo4j_b63.zsh <repo> <huella>`. Antes de levantar, controla:
  - que la carpeta del override, `fuera_del_repo/indices_eval/copia_b/data/experiment/neo4j/`, no esté dentro del repo;
  - que sus dos compose sean iguales a los de HEAD;
  - que exista `volumen_indices_eval/data`; el volumen no lo abre, no lo copia ni lo lista: solo escribe su ruta;
  - que la VM de Docker no pase de 2.684.354.560 bytes.
  Después levanta con `docker compose -p neo4j_indices_eval -f docker-compose.yml -f docker-compose.indices_eval.yml up -d --wait`,
  espera la salud del contenedor y corre el control de la huella con `NEO4J_URI=bolt://127.0.0.1:47687`. El `down` queda en un comentario.
- `control_neo4j_b63.py`, la versión nueva de la función de `control_neo4j_propio --huella` para la configuración del grafo evaluado
  (`mcp_kg/config_mcp_kg_nav_evaluado.json`). Controla:
  - que `NEO4J_URI` del entorno sea el de la entrada;
  - el `KG_Meta`;
  - que la huella de contenido sea la esperada (`2645da6d…`, registro, `:5928`).
  Si algo no da, frena con 15.
- **El runner.** En `controles()` compara el `NEO4J_URI` del entorno con el de la entrada, y en modo real llama al control antes de lanzar.
- **El selftest, con un doble:** la huella de la entrada pasa; otra huella, otro `KG_Meta`, otro `NEO4J_URI` o un Neo4j sin respuesta
  frenan. El gancho de la ventana frena con 15 sin lanzar.

## 6. La P, la guarda de memoria y el juez a la vez

- **La P.** La entrada trae P (1 o 2) y el pico por sesión. `memoria_b63.regla_P` da P = 2 si fijo + 2·pico ≤ 14,5 GB, P = 1 si
  fijo + pico ≤ 14,5 GB y, si no, 0.
- **Lo fijo.** Sale de `memoria_maquina()`, copiada de N6: el diff da igual (§2), y el selftest da lo mismo con las dos sobre un `vm_stat`
  falso (8,192 GB).
- **La guarda.** Corre antes de lanzar y antes de cada bloque: fijo + P picos ≤ 14,5 GB, y si no, frena con 13. La P no cambia sola.
- **El juez, con sus 3 repeticiones a la vez** (`juez_b63.TresJueces`):
  - un hilo, un cliente, una base y un namespace por repetición;
  - cada repetición se lanza cuando pasa la guarda del gasto, con lo gastado y el costo de una repetición calculados una vez por respuesta
    (§127, decisión 6);
  - el veredicto, por moda, como de a una.
- **El selftest:**
  - el juez de a tres da lo mismo que de a una;
  - con el SDK real sobre un transporte simulado y el `CachingClient` del repo, con sus bases en la carpeta del selftest, cada base
    tiene solo su namespace: 6 pedidos;
  - con el gasto al borde, lanza las 2 que entran, espera las que están en vuelo y corta antes de la tercera.

## 7. Docker

`docker_b63.control` corre antes de lanzar y antes de cada bloque:
- la VM no pasa de 2.684.354.560 bytes;
- el contenedor `neo4j-bcra-kg-indices-eval` da healthy;
- registra el `docker stats` del contenedor, la memoria de la máquina y el swap;
- si algo no da, frena con 14.

El selftest lo prueba con un `docker` falso: con la VM en 2,5 GiB y el contenedor sano, pasa y registra; con la VM más grande o sin
salud, frena. El gancho frena con 14 sin lanzar.

## 8. La ventana, los reintentos y la opción (d)

El selftest prueba la ventana con el lanzador falso `seco/lanzador_falso_ventana.py`, sin ningún CLI. Las preguntas de juguete son
`seco/preguntas_ventana_b63.json`.

| caso | resultado |
|---|---|
| P = 1 | el orden firmado; cada reintento, enseguida de su falla; 12 sesiones, 1 pasada, 9 filas del juez |
| P = 2 | nunca más de 2 a la vez; 3 reintentos insertados |
| reintentos | hasta 3 intentos por brazo; con la falla en los tres, `falla_infra_sin_terminar` y ningún cuarto |
| opción (d) | 3 sesiones lanzadas antes del freno 12 |
| gasto | la corrida cortada no va al juez; con freno 1,85, lanza 2 (1,80 más 0,0288 del juez por respuesta) y frena con 2 antes de la tercera |

## 9. El selftest

`b63/v2/selftest_b63.py` corre en una copia, con `SELFTEST_B63_TMP` obligatoria: nada en la carpeta temporal del sistema.

**La copia, mínima** (`copia_y_selftest_b1_B63b1.zsh`). Con N6 corriendo, la memoria en uso estaba en 11,352 GB
(`copia_selftest_intento1_B63_b1.txt`), y una copia del repo entero (`du -sh data`: 9,5 GB) llena la caché de archivos. Por eso copié solo lo que usa el selftest:
- `data/experiment/banco_mcp`, sin `a2_2/adjudicacion`;
- `ev2_juez`;
- los `.py` del primer nivel de `evaluacion`.

El rsync de la cláusula: sin enlaces, sin `.env`, sin `NO_ABRIR_*` y sin `*_SOLO_MESA*`.

**El intento 2** (`copia_selftest_intento2_B63_b1.txt`, de 21:25:41 a 21:26:40):
- la copia: rsync rc 0; 0 `.env`, 0 `NO_ABRIR_`, 0 `SOLO_MESA` y 0 enlaces; sin `.git`; 2.766 archivos, 471 MB;
- la copia es igual al repo según la lista de sha256;
- lo copiado del repo, antes y después: igual;
- 0 `.pyc` en la copia;
- la memoria en uso: 11,218, 11,352 y 11,222 GB, con 0 de swap;
- después, la copia = los 19 archivos de `b63/v2/` del repo: `shasum -c` de `sha256_etapa_b1_b63.txt` en la copia, 19 OK
  (`copia_c2_contra_lista_b63v2_B63b1.txt`).

**El resultado:** 22 de 22 en PASS, en las dos corridas (`selftest_intento2_corrida{1,2}_B63b1.txt`). Las dos salidas son iguales byte
a byte, y no traen horas ni rutas. Las ramas, en el orden de la salida:

1. R5: el A y el B pasan; otro frena.
2. R5 en el lote: con un R5 no admitido, la ventana frena con 5 sin lanzar.
3. pip freeze --all: el `24f4c064…` del venv del banco pasa; otro sha256 frena; la entrada sin él frena.
4. La entrada: P = 2 pasa; frenan P = 3, el pico 0, otro uri, una huella mal formada y la entrada sin `neo4j`: 5 de 5.
5. El patrón: el real más los dos nombres nuevos; el real solo no los ve; el de prueba, un token propio.
6. El patrón de prueba: `pgrep` ve un proceso de prueba propio vivo, y no al cerrarlo.
7. Las formas reales en el clasificador: las cuatro de infraestructura dan `falla_infra`; la clave inválida y una inventada, `desconocida`.
8. La ventana con P = 1 (§8).
9. La ventana con P = 2 (§8).
10. Los reintentos (§8).
11. La opción (d) (§8).
12. El gasto del agente y el juez juntos (§8).
13. Los ganchos: memoria 13, Docker 14 y Neo4j 15.
14. El Neo4j con el doble (§5).
15. La memoria: la copia da lo mismo que la de N6.
16. La regla y la guarda: P por la regla 2, 1 y 0.
17. Docker (§7).
18. El juez de a tres, contra el de a una, y los namespaces (§6).
19. El juez de a tres y la guarda (§6).
20. La atribución (§4).
21. Las formas reales con el CLI falso v2, por el lanzador v2: la clase de la tabla del §3 en las 5.
22. Ningún subproceso con un script del patrón: 356 líneas, 62 `pgrep` y los 62 con el token propio.

**El intento 1** dio 13 de 22 en las dos corridas (§13, error 4).

## 10. Lo que lancé, por nombre de script

Ninguno está en el patrón de otro paso pago: el real de `guardas_lote_r5` más `lanzar_lote_paralelo_r5.py` y `correr_n6.py`.

- **Para las formas reales:**
  - `formas_error_b63.py`, 3 veces;
  - `claude`, el CLI real 2.1.241: `--version` 3 veces y 8 sesiones;
  - el servidor MCP de juguete de cada sesión, `b63/seco/servidor_mcp_juguete.py`;
  - `servidor_errores_b63.py`, que corrió como módulo, en un hilo.
- **Para el selftest:**
  - `copia_y_selftest_b1_B63b1.zsh` (con `rsync`, `find`, `shasum` y `du`);
  - `selftest_b63.py` v2, 4 veces;
  - lo que lanzó el selftest:
    - `lanzar_agente_b63.py` v2;
    - `lanzador_falso_ventana.py`;
    - el `claude` falso, un guion de shell que corre `b63/seco/claude_falso_b63.py` o el v2;
    - el servidor MCP de juguete;
    - el proceso de prueba del token `prueba_b1_zq7xk2m4`;
    - `pgrep`, solo con ese token;
    - los `vm_stat`, `sysctl` y `docker` falsos (guiones de shell);
    - `python -m pip freeze --all`.
- **Los míos, en la carpeta de la sesión:**
  - `foto_repo_b1.py` y `foto_repo_b1v2.py`;
  - `comparar_fotos_b1.py`;
  - `armar_formas_reales.py`;
  - `diffs_b1.py`;
  - el `grep_convenciones.py` de HEAD;
  - `armar_manifest.py` y `enmascarar_paquete.py`.
- **Lo demás:** `git` (`status`, `show`, `ls-files`, `diff`, `config` y `grep`, restringido a `docs/` y al FRENO de la etapa a),
  `vm_stat`, `sysctl`, `ps` y `stat`.

No corrí `correr_b63.py` ni `corrida_en_seco_b63.py`: ni los de HEAD ni los v2. El selftest importa el runner v2, no lo corre. No toqué
`fuera_del_repo/banco_n6/` ni ningún proceso de N6. No usé el denso, Neo4j ni Docker.

**La carpeta temporal del sistema.** Lo nuevo en `/tmp` desde las 20:50, fuera de la carpeta de la sesión, no es mío: son los
sockets `cc-socks/*.sock` de procesos de Claude Code 2.1.309 de la app, y un archivo de las 21:00:30, anterior a mi primera corrida
(21:01:31). Las sesiones del CLI real corrieron con `env -i`, sin `TMPDIR`.

## 11. El repo

- **Lo nuevo:** 19 archivos en `b63/v2/`, todos sin rastrear, con su lista en `b63/v2/sha256_etapa_b1_b63.txt` (`shasum -c` OK), más
  este FRENO. No hay ningún `__pycache__` ni `.pyc` en `b63/`.
- **La foto después** (`foto_repo_b1v2.py`, de 21:27:24 a 21:27:43): 60.264 entradas.
  - Quedan fuera de la comparación las 24 entradas de la foto antes que están dentro de una carpeta `*_SOLO_MESA*`.
  - De esas carpetas, las 13 siguen, por su nombre, en la foto después.
  - Las 13 podadas son iguales en las dos fotos.
  - 60.264 entradas comparadas: 0 cambian, 0 están solo en la foto antes y 0 solo en la foto después.
  - `.pyc` fuera de los venvs: 237 en las dos.
  La salida está en `fotos_comparacion_B63_b1.txt`.
- **Fuera del repo:** `banco_b63/` y `banco_mcp_originales_B63/` siguen sin existir. Las sesiones de prueba quedaron en la carpeta
  temporal de la sesión.

## 12. Lo que queda para después

1. **La corrida en seco del runner v2, cuando termine N6.** Corre `correr_b63.py` v2, que está en el patrón: no puede correr mientras corre
   N6. Tiene que pasar por las ramas reales en el mismo camino de imports: la ventana, los reintentos, la opción (d), los cortes, el
   gasto, los ganchos y el juez de a tres.
2. **El testigo, después de N7:**
   - levanta ese Neo4j con `levantar_neo4j_b63.zsh`;
   - controla la huella (`2645da6d…`);
   - mide lo fijo y el pico de una sesión con la configuración sellada, para fijar la P con `regla_P`.
3. **La entrada sellada real.** La arma la mesa después de N7, con P, el pico, el Neo4j, el pip freeze y el R5 que dé N7.

## 13. Errores propios, con su causa

1. **La foto antes leyó 24 archivos `*_SOLO_MESA*`.** A las 20:55:38, `foto_repo_b1.py` bajó a 13 carpetas `*_SOLO_MESA*` y leyó 24
   archivos para su sha256. Causa: heredé de `foto_repo.py` la regla de leer solo por tamaño y fecha los `.env` y los `NO_ABRIR_*`, y no
   le sumé los `*_SOLO_MESA*`, aunque el despacho los nombra. No se imprimió nada de su contenido.
   - Corregido en `foto_repo_b1v2.py`: no baja a esas carpetas, toma esos archivos solo por tamaño y fecha, y lee con `F_NOCACHE`.
   - En el paquete, la foto antes va con esos 24 sha256 reemplazados por «omitido».
2. **La lista del intento 1 leyó 2 archivos `*_SOLO_MESA*`.** La función `lista` de `copia_y_selftest_b1.zsh` (21:23:09) bajó a
   `a2_2/juez/{n1,recorridas}/desanonimizacion_SOLO_MESA/` y leyó 2 archivos para su sha256. Causa: la función no tenía las exclusiones
   por nombre que sí tenía el rsync. La copia no los trajo (0).
   - Corregido en el intento 2: la función poda por nombre.
   - Las listas del intento 1 no van al paquete.
3. **La corrida 2 de las formas mandó la clave inválida al servidor local.** Fue a `/cinvalida`, que contesta 404, y no a la API. Causa:
   `{"puerto_cerrado": …, "clave_invalida": None}.get(caso) or srv.url(…)` toma el `None` como falta. Lo comprobé en el stream:
   `api_error_status` 404.
   - Corregido; la corrida 3 fue a la API.
   - Antes, en la corrida 1, la clave inválida no corrió: la guarda contaba el HEAD `/api/hello`, sin clave, como un pedido sin la clave
     inválida. El servidor pasó a contar por método.
4. **El selftest del intento 1 dio 13 de 22.** Causa: en `herramientas_b1.py`, `REPO = BANCO_DIR.parents[1]` apunta a `data/` y no a la
   raíz, así que las rutas de la entrada de juguete salían sin `data/`. Corregido (`parents[2]`).
   - Corregí también la lista de guiones del último caso, que contaba como guion el patrón de `pgrep`.
5. **Un diseño corregido antes de correr nada.** La guarda de `TresJueces` recalculaba lo gastado mientras escribían las repeticiones, y
   no daba siempre lo mismo. Ahora se calcula una vez por respuesta.
6. **Dos comandos de zsh fallaron.** Fallaron por un `=` al principio de una palabra (`print ==`, `echo ======`), sin otro efecto.

## 14. Lo que dejo PREPARADO para la decisión de la autora

1. **La clase de la clave inválida.** La puse como desconocida: es un error de configuración, que se repetiría en todas las sesiones y
   frenaría el lote a las 3. La alternativa es frenar a la primera, con un código propio.
2. **El stream en la meta (§4).** Falta. Lo agrego si se decide, en el lanzador v2, sin editar el de HEAD.
3. **La meta trae texto.** Según §127, decisión 5, se commitean solo las salidas sin texto, y entre ellas las metas. Pero la meta del
   lanzador trae `final_json_R4`, con la respuesta, y `mapa_R7`, con el `input` de cada llamada (`agentes/lanzar_agente.py:415,425`).
   Esta etapa no lo cambia.
4. **La firma de las formas.** Las cinco formas tienen el mismo result (success con is_error), y lo único que las distingue es el
   error_status de sus reintentos. Si una sesión de B6.3 se recupera después de algunos reintentos, la meta la da completa y no hay forma
   que clasificar.
5. **El juez de tripletas.** No lo leí: lo traté como vedado.

## 15. Grep de convenciones

Corrí `segmentacion_oficial_e0r2/s0_4/scripts/grep_convenciones.py` de HEAD, con `LC_ALL=en_US.UTF-8`, sobre copias de los 19
archivos de `b63/v2/` y de los scripts de la carpeta de la sesión (`grep_convenciones_v2_y_scripts_B63b1.txt`):
- control positivo: 16 de 16 términos encontrados;
- archivos revisados: 25;
- total por término: {} — total 0.

Al cerrar lo corrí otra vez, sobre este FRENO y sobre el paquete enmascarado (`grep_convenciones_freno_y_paquete_B63b1.txt`):
- control positivo: 16 de 16;
- en este FRENO, 0;
- en el paquete, 38, todas en las dos fotos del repo, 19 en cada una. Son rutas de archivos que ya estaban en el repo, las mismas en
  la foto antes, tomada antes de escribir nada. El detalle va en `grep_convenciones_explicacion_B63b1.txt`.

## 16. El paquete

`revision_B63_FRENO_b1/`, en la carpeta temporal de la sesión, con su `manifest.txt` (sha256 y una línea por archivo). Lo copio con
`ditto` a `fuera_del_repo/scratchpads/94968c98-6fa5-449c-954b-42ee7ee26062/scratchpad/revision_B63_FRENO_b1/` y verifico los sha256 de
su manifiesto en la copia. La ruta y el resultado van en el reporte del cierre.
