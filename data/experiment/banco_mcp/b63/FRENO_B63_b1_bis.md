# FRENO B6.3-b1 bis — tres decisiones de la autora, dos agregados de la mesa y la corrida en seco del runner v2 (27/10/2026)

Unidad: B6.3, etapa b1 bis del runner. Costó USD 0: sin API, sin ninguna sesión del CLI real, sin Neo4j, sin Docker y sin el denso.
En el repo escribí solo archivos nuevos: 18 en `data/experiment/banco_mcp/b63/v2/b1bis/`, más su lista de sha256 y este FRENO. No edité
nada de HEAD ni los 19 de la b1. No commiteé nada. Espero la revisión.

Los artefactos largos van en el paquete `revision_B63_FRENO_b1_bis/` (§15), por su nombre.

## 0. Los criterios

| # | criterio | dónde | resultado |
|---|---|---|---|
| 1 | el paso 0 | §1 | lo esperado; el scratchpad nuevo, restaurado desde la copia permanente (68 de 68) |
| 2 | el diff de cada archivo nuevo contra el de la b1 o el de HEAD, y su sha256 | §2 y §11 | 14 diffs en el paquete; 4 archivos sin original; la lista de los 18 |
| 3 | las claves de la meta sin texto y su control de las ventanas, con el positivo | §5 | 28 claves; 0 ventanas en la sin texto; en la completa, las tres fuentes |
| 4 | el selftest, rama por rama, dos veces iguales | §9 | 28 de 28 en PASS, dos veces, iguales byte a byte |
| 5 | la corrida en seco, rama por rama, o la salida de la guarda | §10 | 13 de 13 en PASS, con la guarda antes (no vio ningún paso pago) |
| 6 | el repo: solo archivos nuevos en `b63/v2/`, con su sha256; lo demás, igual antes y después; el grep, 0 | §11 y §15 | 19 nuevos en `b63/v2/b1bis/` (18 y su lista) y este FRENO; 60.264 entradas comparadas, 0 cambian; grep 0 en lo que escribí |

Hubo errores propios; dos de ellos, de las reglas de las carpetas vedadas y de los `*_SOLO_MESA*` (§13, errores 4 y 5).

## 1. El paso 0

Salida: `paso0_B63_b1bis.txt` (27/10/2026 23:08:31 -0300), con la carpeta personal como `$HOME`.

```
paso 0 de B6.3-b1 bis, 27/10/2026 23:08:31 -0300
scratchpad de esta sesión: <carpeta temporal>/d7b988e9-4130-42c4-b289-914468756f63/scratchpad (nueva, vacía a las 23:05)
manifest.txt de la copia permanente: e824d2276d006e8832376547672881726fb285694bb3dd6fddc7a88b638268e9
manifest.txt del scratchpad (restaurado con ditto): e824d2276d006e8832376547672881726fb285694bb3dd6fddc7a88b638268e9
scratchpad contra su manifest.txt: verificados 68 de 68; distintos o ausentes 0; sin entrada 0
pwd: $HOME/INGENIERIA IA/TESIS/bcra-regulatory-kg
HEAD: 23559e51a667bd664e790ab7c0b905de90662f5e
  800f3d14: en la historia de HEAD
commits desde 800f3d14:
  23559e51 Cobertura de T: la lectura de la autora en dos hojas, la importancia a ciegas de la posicion antes que la presencia, en una segunda nota al pie firmada por la autora
git status --porcelain --untracked-files=no, con las 12 vedadas podadas por ruta y *_SOLO_MESA*/NO_ABRIR_* por nombre: []
b63/v2 contra sha256_etapa_b1_b63.txt (19 renglones):
  OK
sin rastrear en b63/ fuera de b63/v2/ y de FRENO_B63_b1.md: []
sin rastrear en b63/v2/: 20
FRENO_B63_b1.md: b89300ad7b240251bf8f2f6b95a87ee6d0d79bd9d27ce6a08b5605c70b704b4c
```

- **El scratchpad.** El de esta sesión es nuevo y estaba vacío (23:05). Restauré desde la copia permanente, con `ditto`:
  - `revision_B63_FRENO_b1/`: 68 de 68 contra su `manifest.txt` (`e824d227…`, igual al permanente);
  - `revision_B63_FRENO_a/`, de donde saqué `armar_manifest.py` (`5a7db724…`) y `enmascarar_paquete.py` (`65eaf9a2…`).
  Los scripts de la b1 que uso salen del paquete b1, con el sha256 de su manifiesto.
- **Un intento anterior, cortado.** En el scratchpad de la sesión `94968c98…` hay una carpeta `b1bis/` de las 22:36: un paso 0 y una
  foto antes de esta misma unidad, con HEAD en `800f3d14`. Lo dejó un intento que se cortó antes de escribir en el repo: a las 23:08,
  `b63/v2/` seguía con sus 20 archivos sin rastrear (los 19 y la lista). No lo retomé: rehíce el paso 0 y la foto antes en esta sesión.
- **El HEAD.** Es `23559e51`, la segunda nota de la cobertura de T, commiteada a las 23:05:41 (`git log -1 --format=%ci`), después
  del intento de las 22:36. `git log 800f3d14..HEAD` da ese único commit, que cambia solo `docs/cobertura_T_control_de_30_D9.md`.
  `800f3d14` sigue en su historia.

## 2. Los archivos nuevos y sus diffs

Todos en `b63/v2/b1bis/`, una carpeta nueva. Así el runner conserva su nombre, `correr_b63.py`, que es el que buscan las guardas de los
otros pasos (§126, decisión 4), y la carpeta es autocontenida: ningún módulo de la b1 bis se importa desde `b63/v2/`. La lista de sha256
es `b63/v2/b1bis/sha256_etapa_b1bis_b63.txt` (§11). Los diffs están en el paquete, generados por `diffs_b1bis.py`, que controla antes el
sha256 de cada original de la b1 contra `sha256_etapa_b1_b63.txt`.

| archivo de `b63/v2/b1bis/` | contra | +/− |
|---|---|---|
| `comun_b63.py` | `b63/v2/comun_b63.py (b1)` | +16 −12: el 16, `RESULTADOS` fuera del repo, el lanzador de esta carpeta; el primer párrafo del docstring, reajustado |
| `correr_b63.py` | `b63/v2/correr_b63.py (b1)` | +74 −28: la clave inválida, `frenado`, el patrón, la medición de memoria, `--out` fuera del repo |
| `ventana_b63.py` | `b63/v2/ventana_b63.py (b1)` | +10 −7: `al_terminar` también después de un freno; la carpeta |
| `juez_b63.py` | `b63/v2/juez_b63.py (b1)` | +2 −2: solo la carpeta (`parents[2]`) |
| `memoria_b63.py` | `b63/v2/memoria_b63.py (b1)` | +15 −0: un `main` que imprime la medición; `memoria_maquina`, igual |
| `docker_b63.py` | `b63/v2/docker_b63.py (b1)` | +0 −0: igual, byte a byte |
| `control_neo4j_b63.py` | `b63/v2/control_neo4j_b63.py (b1)` | +2 −2: solo la carpeta (`parents[2]`) |
| `lanzar_agente_b63.py` | `b63/v2/lanzar_agente_b63.py (b1)` | +70 −26: el stream en la meta, la meta sin texto, la cadena de la b1 bis, la carpeta fuera del repo |
| `selftest_b63.py` | `b63/v2/selftest_b63.py (b1)` | +271 −65: las ramas nuevas |
| `formas_reales_b63.json` | `b63/v2/formas_reales_b63.json (b1)` | +10 −4: la clase de la clave inválida (ningún valor medido cambia) |
| `corrida_en_seco_b63.py` | `b63/corrida_en_seco_b63.py (HEAD)` | +314 −484: otra corrida en seco: la de la etapa a era su modelo |
| `seco/claude_falso_b63.py` | `b63/v2/seco/claude_falso_b63.py (b1)` | +35 −12: el api_error_status, la clave de relleno inválida, `citas`, `result_fijo` |
| `seco/herramientas_b1bis.py` | `b63/v2/seco/herramientas_b1.py (b1)` | +36 −3: las rutas, las claves de relleno, `ProcesoConNombre`, `ventanas` |
| `seco/lanzador_falso_ventana.py` | `b63/v2/seco/lanzador_falso_ventana.py (b1)` | +17 −7: la clave inválida, las formas de la b1 bis |

Sin original: `comando_b63.zsh`, y en `seco/` `planes_b63_seco_b1bis.json`, `preguntas_meta_b63.json` y `preguntas_seco_b1bis.json`.

## 3. La clave inválida (decisión 1)

- **La forma propia.** `clasificar` mira primero el `api_error_status` del result del stream: si es 401, la clase es `clave_invalida`
  (`correr_b63.py:173`). Es la forma medida en la corrida 3 de la b1 (`formas_reales_b63.json` de la b1 bis: la misma forma, con su
  clase propia; `armar_formas_b1bis.py` controla que no cambie ningún valor medido).
- **El código: 16** (`comun_b63.CLAVE_INVALIDA`). Ningún otro freno lo usa: los del lote son del 2 al 7, el de la extracción es el 9 y
  los del runner, del 10 al 15.
- **Lo que hace** (`correr_b63.py:336-349`):
  - el lote frena a la primera, sin lanzar otra sesión;
  - esa sesión no entra en las sesiones del runner, ni en el final de su bloque, ni en sus intentos;
  - no va al juez ni cuenta como incompleta;
  - queda anotada en `clave_invalida` del estado y, en el registro del lote, con `no_cuenta`;
  - al retomar se corre con su mismo id, en una pasada nueva.
- **Lo que no cambia.** En la guarda del gasto, esa sesión cuenta su presupuesto entero (1,80), como toda sesión sin uso por modelo: lo
  pone el lote base (`agentes/lanzar_lote_paralelo.py:324-325`), que no edité. Su costo real es 0: el 401 da `total_cost_usd` 0 (la
  corrida 3 de la b1, `formas_error_corrida3_B63_b1.json`).
- **Con P = 2.** Si la clave deja de servir, toda sesión lanzada antes de que termine la primera con el 401 también lo da. Ninguna se
  lanza después del freno, y todas quedan fuera de las cuentas y se corren al retomar.
- **Su prueba:** el selftest (dos casos y uno directo, §9) y la corrida en seco (S5 y S6, §10).

## 4. El stream en la meta (decisión 2)

El lanzador de la b1 bis suma a la meta `stream`, con su ruta y su sha256, con la misma forma que el log R1: `rel_repo`, relativa al
repo, o con la carpeta personal como `~/` (`lanzar_agente_b63.py`, `archivo`). La atribución del selftest lo ve: el stream y el log R1
en su carpeta y en la meta, con su ruta y su sha256. En la b1 faltaba.

## 5. La meta sin texto (decisión 3)

- **Dónde.** El lanzador escribe la meta completa (`meta_<id>.json`) junto al stream, y al lado la meta sin texto
  (`meta_sin_texto_<id>.json`). Las dos van fuera del repo:
  - el runner, por defecto, escribe sus salidas en `fuera_del_repo/banco_b63/resultados/<modo>/` (`comun_b63.RESULTADOS`; en la b1,
    `b63/resultados/`, en el repo);
  - en modo real, el runner frena con el 10 si su `--out` está en el repo o en git (`correr_b63.py:465`);
  - el lanzador sale sin lanzar si la carpeta de la sesión lo está.
  La meta sin texto es la que se commitea. Llevarla al repo, con el manifiesto de sha256 de lo que queda fuera, es de un paso posterior.
- **Sus claves**, exactamente estas 28 (`lanzar_agente_b63.CLAVES_SIN_TEXTO`, en este orden):
  - las 18 de HEAD, tal cual: `pregunta_id`, `brazo`, `modo`, `contrato`, `unidad`, `generado`, `sesion`, `modelos_R8`,
    `credenciales`, `servidores_mcp`, `sha_fuentes`, `harness_R10`, `inventario_tools_R6`, `corte_R5`, `completitud_R3`, `tokens_R9`,
    `log_r1` y `duracion_s`;
  - las 5 que suma el lanzador, tal cual (las declaro con lo que traen; ninguna trae texto):
    - `hb2`, del lanzador de N6: los conteos de A2.1 (turnos, subtype, is_error, stop_reason, mensajes, tool_use, tool_result,
      llamadas del log R1, si hay result);
    - `unidad_del_lanzador_importado`: la unidad del lanzador de N6;
    - `banco_venv_vector`: la ruta del venv, con la carpeta personal como `$HOME`, y la versión de su Python, declarada y observada;
    - `control_disco`: la regla, las marcas, los nombres de los archivos de `tool_results_<id>/`, los largos y si frena;
    - `valor_remoto_por_tool`: los nombres de tool con sus números;
  - las 3 que cambian:
    - `mapa_R7`: cada llamada con su `n`, su `tool_use_id`, su `tool`, su `call_id_log`, su `coincide_tool_input` y el sha256 de su
      `input` en JSON canónico, sin el `input`;
    - `final_json_R4`: si está, el sha256 de su JSON canónico y la cuenta de sus citas;
    - `permission_denials`: su cuenta;
  - las 2 que se suman: `stream` y `meta_completa`, cada una con su ruta y su sha256.
  El JSON canónico: `json.dumps` con `sort_keys`, `ensure_ascii=False` y separadores sin espacios, en UTF-8.
- **Su prueba**, sobre una sesión de juguete con la pregunta MET01:
  - la consulta de su llamada es el texto de la pregunta, y su respuesta repite el criterio, así el control positivo tiene las tres
    fuentes en la meta completa;
  - la meta sin texto trae exactamente las 28 claves, en su orden;
  - las ventanas de 30 caracteres, en la sesión del selftest final (`meta_sin_texto_juguete_MET01_B63b1bis.json` y
    `meta_completa_juguete_MET01_B63b1bis.json`, en el paquete):

    | fuente | ventanas | en la meta completa | en la sin texto |
    |---|---|---|---|
    | la pregunta | 75 | 56 | 0 |
    | el criterio | 36 | 36 | 0 |
    | la respuesta | 117 | 117 | 0 |

    De la pregunta faltan en la completa las 19 ventanas que tocan su marca `[[b63:meta_texto]]`: en la meta, la pregunta está solo
    como consulta, sin la marca. El control positivo da en las tres fuentes;
  - el sha256 de `meta_completa` es el de la meta completa; `stream` es el de la completa; `mapa_R7` no trae ningún `input` y su
    `input_sha256` es el del JSON canónico del de la completa; `final_json_R4` trae el sha256 y 2 citas; `permission_denials`, 0;
  - las 23 claves que van tal cual son iguales a las de la completa.
- **En la corrida en seco** (S11, §10), cada sesión de S1 trae su meta sin texto con esas claves, el sha256 de su meta completa y el de
  su stream.

## 6. El patrón (punto 4)

- **El patrón nuevo.** `PATRON_B1` = el de la b1 (`PATRON_B1_V2`) + `SUFIJO_B1BIS` (`correr_b63.py:73-78`): los cuatro comandos de la
  cobertura de T y los dos drivers pagos de V. `control_patron` controla que estén los seis.
- **Su prueba.** Seis procesos de prueba propios, `/bin/sh -c 'read x' <carpeta del token>/<nombre>`, uno por nombre. Su línea de
  comandos se lee con `ps -p <su pid>`, sin ningún `pgrep`.
  - El patrón nuevo ve el nombre en cada línea, y el de la b1 no.
  - No son procesos de Python a propósito: la guarda de cualquier paso cuenta solo un proceso de Python cuyo guion tenga un
    nombre del patrón (`paralelo/guardas_lote.py:98-99`; `guardas_lote_r5.py:67-68`). Un Python con `extraer_cob_t.py` como guion lo
    contaría la guarda de cualquier paso que estuviera corriendo con ese nombre en su patrón, y lo frenaría. Por eso la línea de un
    Python con ese guion se prueba solo como texto (`script_python` y el nombre): el patrón nuevo lo ve y el de la b1 no.
  - El selftest controla también que `script_python` no cuente ninguno de los seis procesos.

## 7. El `env -i` (punto 5)

- **`comando_b63.zsh`**, en `b63/v2/b1bis/`, con dos acciones:
  - `medir <entrada>`: mide la memoria con el mismo entorno que el runner (`memoria_b63.py`, que suma un `main`), sin la clave;
  - `correr <entrada> <sha256> --modo …`: lanza `correr_b63.py`.
- **La lista cerrada:**
  - `PATH`, que tiene que traer `/usr/sbin`, porque ahí está `sysctl` (si no, frena con el 10);
  - `HOME`;
  - `NEO4J_URI`, la variable de la entrada: el comando la lee de la entrada sellada;
  - y, solo en `correr`, `ANTHROPIC_API_KEY`, si está en la Terminal, porque la vía api de las sesiones la necesita
    (`agentes/lanzar_agente.py:130-131`). Está fuera de la lista del punto 5: la declaro. Pasa sin imprimirse; el comando imprime solo
    los nombres de lo que pasa.
- **`B63_PYTHON`** cambia el Python, solo para las pruebas sobre una copia, que no trae el `.venv`. No pasa al runner.
- **El runner también se controla.** Antes de lanzar, en los dos modos, `memoria_maquina` tiene que andar; si no, frena con el 10
  (`correr_b63.py:550-553`).
- **Lo comprobé yo.** Con `LANG=es_AR.UTF-8`, `sysctl -n vm.swapusage` da `0,00M` y no `0.00M`, y la expresión de `memoria_maquina`
  (`used = ([\d.]+)M`) no lo toma: corta con un `AttributeError`.
- **NO VERIFICADO:** el renglón 68 de `comando_paso_pago_N6.zsh` y el §145 del registro que cita el despacho. Ninguno de los dos está en
  el repo (`git ls-files` del banco, con las vedadas podadas, y el registro de HEAD, que llega al §142), y no los busqué fuera.
- **El intérprete agrega `LC_CTYPE`.** Con `env -i`, Python suma `LC_CTYPE` a su propio entorno, en `C.UTF-8` (la coerción de la
  configuración regional C, PEP 538; la rama 21 del selftest). Esa variable no cambia el separador decimal, y la medición anda. La prueba
  la admite solo con un valor de esa coerción (`UTF-8`, `C.UTF-8` o `C.utf8`).

## 8. La sesión que termina después de un freno

- **El cambio** (`ventana_b63.py`, de la b1 bis, `:153-157`). En la b1, una sesión que terminaba después de un freno no pasaba por
  `al_terminar`; con P = 2 eso pasa con la que corría a la vez. Esa sesión quedaba sin registrar y, al retomar, se repetía.
- **Ahora** pasa con `frenado=True`. El runner la clasifica y la registra, sin insertar su reintento y sin juzgarla: los dos quedan para
  el retomar, que juzga lo pendiente antes de lanzar.
- **Por qué.** Lo necesita el «no repite ninguna terminada» de la decisión 1. Lo prueba un caso directo del selftest.

## 9. El selftest

Lo corrí en una copia mínima, como en la b1, con `copia_y_selftest_b1bis.zsh`:
- la copia: `data/experiment/banco_mcp` sin `a2_2/adjudicacion`, `ev2_juez` y los `.py` del primer nivel de `evaluacion`;
- el rsync de la cláusula: sin enlaces, sin `.env`, sin `NO_ABRIR_*` y sin `*_SOLO_MESA*`;
- la lista de lo copiado poda las vedadas y, por nombre, los `*_SOLO_MESA*` y los `NO_ABRIR_*`;
- `SELFTEST_B63_TMP`, obligatoria, en el scratchpad.

**El intento 4, el final** (`copia_selftest_intento4_B63_b1bis.txt`, de 23:46:18 a 23:49:41). Lo corrí con los 18 archivos finales
congelados (`b1bis_congelado_final_intento4_y_seco2_B63b1bis.sha256`; controlados también después de la corrida en seco 2):
- la copia: rsync rc 0; 0 `.env`, 0 `NO_ABRIR_`, 0 `SOLO_MESA` y 0 enlaces; sin `.git`; 2.786 archivos, 471 MB; igual al repo según la
  lista;
- lo copiado del repo, antes y después: igual; 0 `.pyc` en la copia;
- la memoria en uso: 11,28, 11,152 y 11,073 GB, con 0 de swap;
- el resultado: 28 de 28 en PASS en las dos corridas (`selftest_intento4_corrida{1,2}_B63b1bis.txt`), iguales byte a byte.

Las ramas, en el orden de la salida:

1. R5: el A y el B pasan; otro frena.
2. R5 en el lote: con un R5 no admitido, la ventana frena con el 5 sin lanzar.
3. pip freeze --all: el `24f4c064…` pasa; otro sha256 frena; la entrada sin él frena.
4. La entrada: P = 2 pasa; frenan P = 3, el pico 0, otro uri, una huella mal formada y la entrada sin `neo4j`: 5 de 5.
5. El patrón: el real, los dos nombres de la b1 y los seis de la b1 bis; el real solo no los ve; el de prueba, un token propio.
6. El patrón de la b1 bis, con los seis procesos de prueba (§6): 6 de 6 nombres.
7. El patrón de prueba: `pgrep` ve un proceso de prueba propio vivo, y no al cerrarlo.
8. Las formas reales en el clasificador: las cuatro de infraestructura dan `falla_infra`, la clave inválida `clave_invalida` y una
   inventada `desconocida`.
9. La ventana con P = 1: 12 sesiones lanzadas, 1 pasada.
10. La ventana con P = 2: máximo 2 a la vez; 3 reintentos insertados.
11. Los reintentos: 3 intentos por brazo, `falla_infra_sin_terminar`, ningún cuarto.
12. La opción (d): 3 lanzadas antes del freno 12.
13. El corte sin juez, y el gasto: con freno 1,85, lanza 2 y frena antes de la tercera.
14. Los ganchos: memoria 13, Docker 14 y Neo4j 15.
15. La clave inválida con P = 1: 4 lanzadas, 1 con la clave inválida (fuera de las cuentas), 3 que cuentan, 0 terminadas después del
    freno y ninguna lanzada después; al retomar, 6 lanzadas, ninguna repetida; 9 finales completas y juzgadas.
16. La clave inválida con P = 2, inválida desde la primera: 2 lanzadas, las 2 con el 401, 1 terminada después del freno y ninguna lanzada
    después; al retomar, 9 lanzadas, ninguna repetida; 9 finales completas y juzgadas.
17. Después de un freno, directo sobre `al_terminar`: la completa queda registrada, con su juez pendiente; la falla de infraestructura,
    sin insertar su reintento, que queda para el retomar (el intento 2).
18. El Neo4j con el doble.
19. La memoria: la copia da lo mismo que la de N6.
20. La regla y la guarda: P por la regla 2, 1 y 0.
21. El comando con `env -i`: con LANG=es_AR.UTF-8 en el padre, `medir` mide bien. El comando dice que pasa `PATH, HOME, NEO4J_URI`, y
    el entorno de la medición trae `HOME`, `LC_CTYPE`, `NEO4J_URI` y `PATH`, con `LC_CTYPE` en `C.UTF-8`, del intérprete (§7). Sin el
    comando, la medición corta, y el runner frena con el 10.
22. Docker.
23. El juez de a tres, contra el de a una, y los namespaces: 6 pedidos.
24. El juez de a tres y la guarda.
25. La atribución y el stream en la meta (§4).
26. La meta sin texto (§5): 28 claves; ventanas en la sin texto 0, 0 y 0; en la completa, las tres.
27. Las formas reales con el CLI falso de la b1 bis, por el lanzador: la clase de cada una, la del 401 incluida.
28. Ningún subproceso de Python con un guion del patrón de la b1 bis:
    - 517 líneas;
    - 90 `pgrep`, todos con el token propio;
    - los 6 procesos `/bin/sh` de la rama 6;
    - guiones de Python lanzados: `lanzador_falso_ventana.py`, `lanzar_agente_b63.py`, `memoria_b63.py` y `prueba_b1bis_zq7xk2m4.py`.

**Los intentos anteriores:**
- el 1 (25 de 27) y el 2 (27 de 28) fallaron por la prueba, no por el runner (§13, errores 1 y 2);
- el 3 dio 28 de 28 en las dos corridas, iguales, pero la corrida en seco 1 encontró después la línea mal impresa del comando (§13,
  error 6). La corregí y sumé su control a la rama 21. Por eso corrí el 4.

## 10. La corrida en seco

**La guarda**, antes de todo: la de otro paso pago con `PATRON_B1`, el real, el único `pgrep` con el patrón real de la corrida. En las
dos corridas imprimió «guarda: ningún paso pago corriendo» (0 hallados) y la corrida siguió.

**La copia y la corrida 2, la final** (`copia_y_seco_b1bis.zsh`; `copia_seco2_B63_b1bis.txt`, de 23:49:41 a 23:53:50). Corrió con los 18
archivos finales congelados:
- la misma copia mínima que el selftest: rsync rc 0; 0 `.env`, 0 `NO_ABRIR_`, 0 `SOLO_MESA` y 0 enlaces; sin `.git`; 2.786 archivos;
  igual al repo según la lista;
- lo copiado del repo, antes y después: igual; 0 `.pyc` en la copia;
- la memoria en uso: 11,272 y 11,339 GB, con 0 de swap;
- corrió desde la raíz de la copia, con `env -i PATH HOME`. Importa el runner de su carpeta, sin tocar el `sys.path` por fuera, y pasa
  por el lanzador de la sesión de la b1 bis, el de N6, el `claude` falso y el servidor de juguete de cada sesión, con el juez falso y los
  dobles de memoria, Docker y Neo4j.

**El resultado:** 13 de 13 en PASS (`corrida_en_seco2_consola_B63b1bis.txt` y `corrida_en_seco2_resultado_B63b1bis.json`).

| rama | qué | resultado |
|---|---|---|
| S1 | la ventana con P = 1 y el juez de a tres | código 0; 12 lanzadas, en el orden firmado y con cada reintento enseguida de su falla (la forma real del 429); 9 respuestas juzgadas de a tres; 27 pedidos al transporte; una base y un namespace por repetición |
| S2 | la ventana con P = 2 | código 0; máximo 2 a la vez; 3 reintentos, cada uno al frente |
| S3 | los reintentos | código 0; la forma real del 500 en los tres intentos de cada brazo; 9 lanzadas, ningún cuarto |
| S4 | la opción (d) | código 12; 3 desconocidas, 3 lanzadas |
| S5 | la clave inválida con P = 1 | código 16; 4 lanzadas, 1 con la clave inválida, fuera de las cuentas; ninguna lanzada después del freno; al retomar, código 0, 6 lanzadas y 0 repetidas; 9 finales, 9 juzgadas |
| S6 | la clave inválida con P = 2 | código 16; 2 lanzadas, las 2 con el 401; 1 terminada después del freno y ninguna lanzada después; al retomar, código 0, 9 lanzadas y 0 repetidas; 9 finales, 9 juzgadas |
| S7 | los cortes | código 0; cortadas el kg de SEC06 (`--max-turns`) y el bm25 de SEC07 (el presupuesto), ninguna juzgada; las otras 4, completas y juzgadas |
| S8 | el gasto del agente y el juez juntos | código 2; 2 lanzadas; 6 pedidos al transporte |
| S9 | los ganchos | códigos 13, 14 y 15; 0 lanzadas en cada uno |
| S10 | retomar sin repetir | la corrida de S1 otra vez: código 0, 0 pasadas nuevas |
| S11 | la meta sin texto y el stream, en cada sesión de S1 | 12 sesiones; en ninguna falla nada |
| S12 | el comando con `env -i` | por el comando, con LANG=es_AR.UTF-8 en el padre: rc 0, los controles OK, y el comando dice que pasa `PATH, HOME, NEO4J_URI, ANTHROPIC_API_KEY`; sin el comando: rc 10, por la medición de memoria |
| S13 | las líneas de comandos | 467 líneas; 93 `pgrep`, todos con el token; un solo guion del patrón, el runner sin el comando de S12 (el que corre por el comando lo lanza `zsh`); guiones lanzados: `correr_b63.py` y `lanzar_agente_b63.py` |

**La corrida 1** (`copia_seco_B63_b1bis.txt`, de 23:41:00 a 23:45:08), con la misma guarda, dio 11 de 13: fallaron S7 y S12 (§13,
error 6).

## 11. El repo

- **Lo nuevo:** 18 archivos en `b63/v2/b1bis/`, más su lista `sha256_etapa_b1bis_b63.txt` (18 renglones; `shasum -c` OK; su
  sha256, `6ec3a697…`), y este FRENO. En `b1bis/` hay 19 sin rastrear.
- **Lo que no cambió:**
  - nada de HEAD: `git status --porcelain --untracked-files=no`, con las vedadas podadas por ruta, vacío;
  - los 19 de la b1 dan su lista;
  - en `b63/` no hay nada sin rastrear fuera de `b63/v2/` y de los dos FRENOs;
  - no hay ningún `.pyc` ni `__pycache__` en `b63/`.
- **Las fotos** (`foto_repo_b1v2.py`; `fotos_comparacion_B63_b1bis.txt`). La foto antes, a las 23:08:39, y la foto después, de 23:54:12 a
  23:54:30, las dos con HEAD en `23559e51`: entre los dos HEAD no hay ningún commit (`git log`, vacío).
  - 60.264 entradas en cada una: 60.264 comparadas, 0 cambian, 0 están solo en una;
  - las 13 podadas (las 12 vedadas y `b63/`), iguales;
  - las 13 carpetas podadas por nombre (`*_SOLO_MESA*`), las mismas;
  - `.pyc` fuera de los venvs: 237 y 237.
- **Fuera del repo:** `banco_b63/` y `banco_mcp_originales_B63/` siguen sin existir. Las sesiones de las pruebas quedaron en el
  scratchpad.

## 12. Lo que lancé

Ningún proceso mío corrió un script del patrón, salvo los `correr_b63.py` de la rama S12 de las dos corridas en seco, dos en cada una y
después de su guarda (§10): el que lanza el comando y el que se lanza sin él. Ninguna llamada a la API, ninguna sesión del CLI real,
nada pago. No toqué `fuera_del_repo/banco_n6/` ni ningún proceso de N6 o de la cobertura. No usé el denso, Neo4j ni Docker.

- **Los míos, en el scratchpad:**
  - `paso0_b1bis.zsh`;
  - `foto_repo_b1v2.py`, la foto antes y la foto después;
  - `comparar_fotos_b1.py`;
  - `armar_formas_b1bis.py`;
  - `diffs_b1bis.py`;
  - `copia_y_selftest_b1bis.zsh`, 4 veces (con `rsync`, `find`, `shasum` y `du`);
  - `copia_y_seco_b1bis.zsh`, 2 veces;
  - `seccion_seco_b1bis.py`;
  - `armar_paquete_b1bis.zsh`, `descripciones_b1bis.py`, `enmascarar_metas_b1bis.py`, `armar_manifest.py` y `enmascarar_paquete.py`;
  - el `grep_convenciones.py` de HEAD.
- **Lo que lanzó el selftest, 8 veces en total (4 intentos, de 2 corridas cada uno):**
  - `lanzar_agente_b63.py` y `lanzador_falso_ventana.py`, los de la b1 bis;
  - el `claude` falso: un guion de shell que corre `seco/claude_falso_b63.py` de la b1 bis, o el de `--version`;
  - el servidor MCP de juguete, `b63/seco/servidor_mcp_juguete.py`;
  - el proceso de prueba del token `prueba_b1bis_zq7xk2m4`;
  - los 6 procesos `/bin/sh` de la rama 6;
  - `pgrep`, solo con el token;
  - `zsh comando_b63.zsh medir`, que corre `memoria_b63.py`, y `memoria_b63.py` directo;
  - `vm_stat` y `sysctl` reales (solo lectura) y falsos, y el `docker` falso;
  - `python -m pip freeze --all`;
  - `ps`.
- **Lo que lanzaron las dos corridas en seco:**
  - su guarda: un `pgrep` con `PATRON_B1`, el real (lo autoriza el despacho), uno en cada corrida;
  - `lanzar_agente_b63.py`, el `claude` falso y el servidor de juguete;
  - `zsh comando_b63.zsh correr` y `correr_b63.py` directo (S12);
  - `pgrep`, solo con el token propio;
  - `ps`.
- **Lo demás:**
  - `git`, con las vedadas podadas por ruta salvo el error 4 del §13: `status`, `log`, `rev-parse`, `merge-base`, `ls-files` y `show`;
  - `ditto`, `stat`, `date`;
  - `sysctl -n vm.swapusage` y `vm_stat`, con y sin `LANG=es_AR.UTF-8` (§7).

**La carpeta temporal del sistema:** no escribí nada fuera del scratchpad. El selftest exige `SELFTEST_B63_TMP`, y la corrida en seco
escribe en su `--tmp`, los dos en el scratchpad.

## 13. Errores propios, con su causa

1. **El selftest del intento 1 dio 25 de 27.**
   - La prueba de la clave inválida con P = 2 cambiaba la clave a mitad de corrida. Cuando la sesión buena que corría a la vez terminó
     antes que la del 401, el lote lanzó otra más, ya con la clave inválida: 5 en lugar de 4. El runner hizo lo correcto, pero la prueba
     dependía del orden en que terminan las sesiones, y las dos corridas tienen que dar lo mismo.
     Corregido: con P = 2, la clave inválida desde la primera sesión, sin carreras. Sumé el caso directo del registro después de un
     freno (rama 17).
   - El comando buscaba el Python en `<repo>/.venv`, que la copia no trae. Corregido con `B63_PYTHON`, solo para las copias.
2. **El selftest del intento 2 dio 27 de 28.**
   - Con `env -i`, el intérprete agrega `LC_CTYPE` (PEP 538), y la prueba no lo esperaba. Corregido: `memoria_b63.py` imprime su valor,
     y la prueba lo admite solo con el valor de esa coerción.
   - Además, en el intento 2 la comparación del repo dio «antes = después: NO». La causa: edité 6 archivos de `b63/v2/b1bis/` mientras
     corría (los encabezados reajustados, `memoria_b63.py`, el selftest y la corrida en seco). Comparé las dos listas: cambiaron esos 6
     y ninguno más. Por eso el intento final corrió con los archivos congelados, y los controlé antes y después.
3. **El reajuste de los encabezados rompió tres archivos.** Mi script para reajustar el primer párrafo del docstring de `comun_b63.py`,
   `correr_b63.py` y `ventana_b63.py` tomó el shebang como parte del párrafo. `ast.parse` lo detectó enseguida y lo corregí antes de
   cualquier corrida.
4. **Un `git ls-files` sin podar una vedada.** `git ls-files -- data/experiment/banco_mcp`, para buscar `comando_paso_pago_N6.zsh`, no
   podó `a2_2/adjudicacion`: recorrió en el índice los nombres de esa carpeta. Su salida pasó por un `grep` que no dio nada, así que no se
   mostró ningún nombre suyo. Lo repetí con las vedadas podadas por ruta.
5. **Un `grep -r` que bajó a dos carpetas `*_SOLO_MESA*`.** `grep -rl "def conteos_hb2"` sobre `banco_mcp`, con `--include='*.py'` y
   `--exclude-dir=adjudicacion`, listó lo que hay en `a2_2/juez/{n1,recorridas}/desanonimizacion_SOLO_MESA/`. No leyó ningún archivo:
   solo lee los `.py`, y esas carpetas traen solo `.json` (la foto de la b1). No excluí `*_SOLO_MESA*` por nombre.
6. **La corrida en seco 1 dio 11 de 13.**
   - S7: mi prueba esperaba los 6 brazos cortados. Pero cada plan de corte de la etapa a se aplica a un solo brazo (`aplica_a`:
     `corte_turnos`, el kg; `corte_presupuesto`, el bm25), y el runner hizo lo correcto: 2 cortadas sin juez y 4 completas juzgadas.
     Además, la prueba rotulaba «cortadas» al total de finales. Corregido.
   - S12: el comando imprimía mal los nombres de lo que pasa: solo `PATH`. Dentro de comillas dobles, zsh junta el arreglo antes del
     `%%=*`; faltaba el `(@)`. Lo que pasaba al runner estaba bien: sus controles dieron OK. Corregido. El selftest no miraba esa línea;
     ahora la controla (rama 21).
   - Por los dos cambios, repetí el selftest (intento 4) y la corrida en seco (la 2) con los archivos congelados de nuevo.

## 14. Lo que dejo PREPARADO o declarado

1. **El directorio del juez sigue en el repo.** Por defecto, `b63/juez/` (comun_b63.JUEZ_DIR), con su caché. Sus veredictos traen
   texto (las justificaciones y los fragmentos), y la decisión del 26/10, 21:58:48 (registro, §127, decisión 5), deja «la caché del
   juez» fuera del repo. Esta etapa no lo cambia, porque el despacho no lo nombra. Queda PREPARADO para la decisión de la autora.
2. **La guarda cuenta 1,80 por la sesión de la clave inválida** (§3), del lado seguro.
3. **El registro del lote** (`registro_lote.json`, que escribe la base y no edité) lista la sesión de la clave inválida como lanzada y
   terminada, con `no_cuenta`. Leí «no entra en la meta del lote» como: no entra en las cuentas del runner ni en sus metas.
4. **El comando pasa también `ANTHROPIC_API_KEY`**, en `correr` (§7).
5. **El control de la carpeta de la sesión fuera del repo corre solo en modo real.** En modo init (el lote del testigo), no, para no
   cambiar su camino.
6. **Llevar las metas sin texto al repo, con el manifiesto de sha256 de lo que queda fuera, es de un paso posterior** (§5).
7. **La tabla del juez de juguete se llama `*_SOLO_MESA*`.** Las corridas de juguete del selftest y de la corrida en seco dejan su
   tabla de desanonimización en `desanonimizacion_SOLO_MESA/`, dentro de su carpeta de trabajo del scratchpad: el juez de B6.3 la
   escribe así por diseño, y el runner y las pruebas la leen, como en la b1. Es un dato de juguete, generado por esas corridas. Al
   revisar S7, listé la carpeta del juez de esa rama, con su nombre. No abrí ningún `*_SOLO_MESA*` del repo ni de la mesa, y el paquete
   no trae ninguno.
8. **Lo que queda para después:** el testigo, después de N7 (la b2: el Neo4j de los índices, la huella, lo fijo y el pico para la P), y
   la entrada sellada real, que arma la mesa.

## 15. El grep de convenciones y el paquete

**El grep de convenciones.** Corrí `segmentacion_oficial_e0r2/s0_4/scripts/grep_convenciones.py` de HEAD, con `LC_ALL=en_US.UTF-8`,
sobre copias de los 18 archivos de `b63/v2/b1bis/` y de los scripts del scratchpad (`grep_convenciones_b1bis_y_scripts_B63b1bis.txt`):
- control positivo: 16 de 16 términos;
- archivos revisados: 29;
- total por término: {} — total 0.

Al cerrar lo corro otra vez, sobre este FRENO y sobre el paquete enmascarado (`grep_convenciones_freno_y_paquete_B63b1bis.txt`). El
resultado va en el reporte del cierre.

**El paquete:** `revision_B63_FRENO_b1_bis/`, en el scratchpad de esta sesión, con nombres únicos y su `manifest.txt` (sha256 y una línea
por archivo). Trae:
- lo que escribí: los 18 de `b1bis/`, como `b1bis__*`, y los scripts, como `script__*`;
- los diffs y los controles;
- las salidas de los cuatro intentos del selftest y de las dos corridas en seco;
- las fotos y las metas de la sesión de juguete MET01, enmascaradas.

Lo copio con `ditto` a dos carpetas, y verifico en cada copia los sha256 de su manifiesto. La ruta y el resultado van en el reporte del
cierre:
- la del despacho: `~/INGENIERIA IA/TESIS/fuera_del_repo/scratchpads/94968c98-6fa5-449c-954b-42ee7ee26062/scratchpad/`;
- la de la regla g del CLAUDE.md, la misma ruta relativa que tiene el paquete bajo la carpeta del proyecto en la carpeta temporal:
  `…/scratchpads/d7b988e9-4130-42c4-b289-914468756f63/scratchpad/`.

El despacho nombra el scratchpad de la sesión de la b1, y esta sesión tiene otro. Por la regla d, mandan los archivos del repo: copio a
la ruta de la regla g, y también a la del despacho, para que la mesa la encuentre donde la busca.
