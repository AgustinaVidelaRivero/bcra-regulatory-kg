# REPORTE de R0, fase 1: E3-01 de la tanda 0, antes del re-sellado único (13/10/2026; USD 0, sin API, sin commit)

Rige la enmienda 7 al protocolo entre tandas (firmada en `4a33ce92`; la nota al pie del 09/10/2026, en `0c516af9`, deja solo
E3-01). Leí la enmienda en el commit de la firma y en el de la nota: entre los dos solo se agrega la nota (`git diff 4a33ce92
0c516af9`). Todo lo que corrí, corrió sobre una copia del repo sin enlaces en el scratchpad (`rsync -a --no-links`, sin `.git`,
`.venv`, `.venv-app`, `__pycache__` ni `.DS_Store`; 22.092 archivos, 0 enlaces), con `-B` y `PYTHONDONTWRITEBYTECODE=1`. Las rutas de
este reporte son de `data/experiment/reextraccion_v2/` salvo que digan otra cosa.

## 1. El reparto de las 20

`r0/controles/r0_f1_reparto_y_claves.py` → `r0/controles/r0_f1_reparto_y_claves.json`. Usa el código del pipeline: importa
`runner_corpus`, lo configura con `manifiestos/tanda0_10tos_r2b.json` y activa el camino del perfil r2 como `main()`
(`PERFIL_R2 = perfil_forma_r2(PERFIL)`). Para cada unidad de la lista sellada (`cc6b0cd6…`), toma su chunk de la E0
`e0_chunking/salida_tanda0_r2b`, su último registro de E1 en `corpus_tanda0/salida_r2b/<to>/extracciones_e1.jsonl` y la
verificación de O3 (`e3_listas/o3/a/respuestas_e3_o3.jsonl`). Evalúa esa verificación con `ratchet_e3.evaluar_veredicto` y aplica la
rama de `ratchet_e3.ciclo_ratchet`.

- **TO:** ext 19 y docvig 1. Estado en la tanda 0: 13 `aceptado_tras_reintento`, 5 `cola_humana` (con reintento) y 2
  `cola_humana_veredicto_inutilizable`.
- **Con el veredicto de O3:**
  - 16 se aceptan con el intento 0: 11 `completo_ok_directo` y 5 `aceptado_con_residuales`. De ellas, 11 eran
    `aceptado_tras_reintento` en la tanda 0 y 5 estaban en la cola: `ext::2.6.1.1`, `ext::3.5.6.1`, `ext::3.6.1.1`, `ext::3.6.4.2` y
    `ext::3.13.1.10`.
  - Reintentan 3: `ext::3.6.4.1`, `ext::3.16.2.1` y `ext::3.18.1.1`, con 1, 1 y 2 bloqueantes con cita verificada.
  - Vuelve a la cola `docvig::3.3.2` (`cola_humana_veredicto_inutilizable`: 1 bloqueante, sin cita verificada).
- **El reparto es el de la enmienda 7, §1.2** (16, 3 y 1, con las mismas unidades): `igual_a_enmienda7_1_2: true`.
- La evaluación con el código de HEAD reproduce la guardada de O3 (`e3_listas/o3/a/evaluacion_e3_o3.jsonl`) en 20 de 20.
- **E1 del intento 0:** en las 20, la clave que arma el perfil r2b está en `e1_extractor/cache/e1_extraccion.db`, con la respuesta
  igual al crudo guardado y el modelo `claude-haiku-4-5-20251001`. El registro de E1 es el del compactado en las 20, y ninguna tiene
  reintento por corte, reintento por forma, reparación ni tercer escalón.

## 2. Las tres preguntas de diseño

### a. La clave: sí, es la de O3 en las 20

La clave del runner sale de `cliente_e3.namespace_e3()`, más `prompt_e3.build_request_kwargs` con el chunk y la validación del
intento 0, más `llm_cache.compute_key`. La de O3 es la fila de `e3_listas/cache/e3_listas_o3.db` (`ab532154…`, 20 filas) con el mismo
mensaje. Resultado, en 20 de 20:

- la clave es la misma;
- el namespace es el mismo (`e3_verificacion|cv=e3-verificador-v1-p21a836c7de6d|think=0`);
- el pedido canónico es igual byte a byte;
- la clave de la fila, recomputada desde su namespace y su pedido, es la guardada;
- el mensaje tiene el sha256 del control de O3 (`o3/a/control_mensajes_o2.json`);
- la respuesta de la fila es la de `respuestas_e3_o3.jsonl`;
- el modelo es `claude-sonnet-5`.

Ninguna de las 20 claves está en la base de E3 del pipeline (0 de 20), como dice A3r.

El código del camino es el mismo que usó O3: entre `7fe848c` y HEAD, `git diff --stat` sobre `e3_verificador/`, `e1_extractor/`,
`runner_corpus.py`, `manifiestos/` y `pyd_r2/code` solo muestra una línea del runner (en `cerrar_e2_r2`, del E2 r2), `validador_r2.py`
(la verificación de la mención y el tipo de Comunicacion, del E2 r2) y dos selftests.

### b. La base: cuatro caminos, todos en `correr_r0.py --reuso-o3` y en la corrida en seco

| Camino | Qué escribe | Costo de las 20 verificaciones | A3r |
|---|---|---|---|
| b1 «sembrar» en la base del pipeline (`e3_verificador/cache/e3_verificacion.db`) | las 20 filas de O3 (13 columnas tal cual, sin su `access_log`), antes de la primera llamada; las llamadas nuevas, en las bases del pipeline | USD 0 (aciertos de la caché local) | las 20 quedan presentes: se redefine (enmienda 7, §1.5) |
| b2 «sembrar» en una base propia de R0 (`--db-e3` y `--db-e1r` en rutas nuevas) | una base nueva con las 20 de O3 y las llamadas nuevas, como la de O3 (unas 26 filas entre las dos bases) | USD 0 | no cambia: las bases del pipeline no se tocan |
| b3 «leer» | nada de O3: las devuelve desde su base, abierta en modo inmutable; las llamadas nuevas van a la base que se elija | USD 0 | no cambia si las llamadas nuevas van a una base propia |
| b4 «no» | las 20 se pagan de nuevo; E3 no fija la temperatura, así que el veredicto puede no ser el de O3, y el reparto, no ser 16/3/1 | USD 0,2382 más (20 × 0,011911) | las 20 quedan presentes |

En b1, los controles del sembrado son estos: las claves de O3 son las 20 esperadas; antes, cada una está ausente o presente con la
misma fila; después, las 20 están presentes e iguales a O3, y la base tiene las filas de antes más las insertadas. En la corrida en
seco, sobre una copia de la base, pasó de 7.698 filas a 7.718, con 20 iguales a O3. Para volver atrás, se borran las claves
registradas.

**Recomendación: b1.** Es lo que anticipa el §1.5 de la enmienda 7 («las 20 … que entran»): el re-sellado encuentra las 20 en la base
de siempre (nunca pagar dos veces). b2 es la alternativa conservadora: no toca ninguna base del pipeline, a cambio de que esas
verificaciones vivan fuera de ella. b3 y b4 no los recomiendo: b3 deja la verificación que decidió las 20 fuera de toda base que lea
el runner, y b4 paga de nuevo y puede cambiar el reparto.

### c. Dónde escribe: siempre primero en su carpeta, y después anexar o sellar la copia

`correr_r0.py` nunca escribe en `salida_r2b/` mientras corre. Corre `runner_corpus.fase_e3` sobre una carpeta de trabajo propia
(`r0/corrida/`), con el E1 del intento 0 de las 20, copiado byte a byte. Ahí quedan `finales`, `veredictos`, `reintentos_e3`, `cola_humana`
y `copias_nota_e3` (si hay copias de nota) por TO, más el presupuesto, el registro de llamadas y el resumen.

- **c1 (recomendada): anexar.** `correr_r0.py --anexar` agrega esos renglones a `salida_r2b/{ext,docvig}/`, como manda la
  enmienda 5, §1.3, y el ensamblado del re-sellado toma la última versión sin cambios de código.
  - Controla que cada archivo quede igual a su versión anterior más los renglones nuevos, y que todos sean de las 20.
  - Corre una sola vez por carpeta de trabajo.
  - En la corrida en seco, sobre una copia de la salida, cambiaron 7 archivos con 48 renglones (ext: `finales` 19, `veredictos` 22,
    `reintentos_e3` 3, `cola_humana` 1; docvig: `finales` 1, `veredictos` 1, `cola_humana` 1). La última versión de cada una de las 20
    es la nueva, y el segundo anexo frena.
  - Efectos que hay que declarar:
    - `veredictos.jsonl` queda con dos verificaciones de las 20; los lectores toman la última, pero `exenciones_ampliacion` las lista a
      las dos;
    - hasta el ensamblado del re-sellado quedan viejos `resumen_e3.json`, `extracciones_finales_*`, los grafos, los reportes, el
      censo y `estado_corpus.json` de la salida.
- **c2: la copia se sella.** No se anexa, y `r0/corrida/` entra al commit como la copia. El re-sellado tiene que anexarla después, o
  armar una salida nueva completa con los renglones agregados (como `salida_dirigida/` en U-TANDA0-2A-DIR, unos 120 MB) y apuntar a
  ella los manifiestos del ensamblado.

El costo de API es el mismo en c1 y en c2.

## 3. El script: `r0/correr_r0.py` (y `r0/seco_r0.py`, `r0/esperados_r0.json`)

- **Importa, no copia.** Importa `runner_corpus` (que agrega `e1`, `e3`, `e2` y `e0` al `sys.path`), `cliente_e3`, `cliente_e1`,
  `ratchet_e3`, `prompt_e3` y `llm_cache`. El E3 de cada TO lo corre `runner_corpus.fase_e3` sobre la carpeta de trabajo: con solo el E1
  de las 20, `pares_de` toma justo esas unidades; las unidades del corpus salen de la E0 entera del TO, para la guardia B.
- **Clientes.** Son `cliente_e3.ClienteE3Real` y `cliente_e1.ClienteE1Real` (prefijo del perfil y transmisión como el runner),
  envueltos en dos subclases (`ClienteE3R0` y `ClienteE1R0`) que agregan la guardia y nada más.
- **Tope.** `--tope` es obligatorio, va hasta USD 1,50 y lo comparten los dos clientes con `runner_corpus.PresupuestoCompartido`, en
  `r0/corrida/presupuesto_r0.json` (lección de U-TANDA0-2A-DIR).
- **Controles previos, sin red.** Que tengan el sha256 de la fase 1 la lista, `runner_corpus.py`, `cliente_e3.py` y la base de O3; los
  namespaces; el registro de E1, que sea el del compactado; el E1 del intento 0, que esté en la caché (búsqueda en modo inmutable;
  R0 no llama a E1 para el intento 0); el mensaje de E3, que sea el del control de O3; y los esperados recomputados, que sean los
  sellados en `r0/esperados_r0.json` (`81598c97…`). Si el reparto no es 16/3/1, frena.
- **Guardia antes de cada llamada.**
  - El pedido sin el mensaje tiene que ser el del prefijo sellado (E3 `62ffe0a6…`, reintento de E1 `1bcee981…`).
  - El mensaje tiene que ser uno de los esperados: las 20 verificaciones, o los 3 reintentos de E1 armados desde el veredicto de O3
    (sin reuso, el de una de las 20 ya verificada).
  - La re-verificación de E3 se admite solo para una unidad que ya reintentó.
  - Después de cada respuesta, de la API o de la caché, controla el id del modelo (E1 `claude-haiku-4-5-20251001`, E3
    `claude-sonnet-5`).
  - Una guardia que frena queda frenada.
- **Usage.** Lo loguean los clientes (`logs/cache_usage.jsonl`, decisión 3 de caching), y R0 además registra cada llamada en
  `registro_llamadas_r0.jsonl`, con hora, unidad, paso, sha del mensaje, acierto, costo, modelo y usage. Las llamadas van en secuencia.
- **Línea de comandos.** Además de `--tope`, pide `--reuso-o3`, sin valor por defecto, porque es la pregunta b. El mandato da
  `--correr --tope 1.50`.

## 4. La corrida en seco

`r0/controles/r0_f1_corrida_en_seco.py` → `r0/controles/r0_f1_corrida_en_seco.json`. Corrió de 17:15:18 a 17:15:29.

- **Mismo camino que la corrida real.** Cada escenario llama a `correr_r0.py --seco` como proceso aparte, desde la copia, con el mismo
  intérprete y la misma línea de comandos que la corrida real, sin tocar el `sys.path`.
- **Sin red.** Los clientes son los reales, con un transporte simulado (`seco_r0.py`) debajo de `llm_cache.CachingClient`, en lugar
  del cliente de la API. Sin clave, `ANTHROPIC_BASE_URL` apunta a un puerto local cerrado.
- **Bases.** Cada escenario trabaja sobre copias propias de las bases (o bases nuevas). Las esperas del reintento de API del runner se
  registran en lugar de dormir.

| Escenario | Resultado |
|---|---|
| base_sembrar | 11 + 5 aceptadas, 2 `aceptado_tras_reintento`, 1 `cola_humana`, 1 inutilizable; 20 sembradas; 6 llamadas simuladas; anexo y segundo anexo rechazado |
| base_propia_sembrar | igual, con las bases creadas por la corrida (0 → 23 y 0 → 3 filas) |
| base_leer | igual, con 20 verificaciones leídas de O3 y 3 filas nuevas en la base de E3 |
| sin_reuso | igual, con 26 llamadas simuladas |
| tope (0,12) | frena por el tope compartido después del primer reintento de E1 (0,0443 + 0,1040 > 0,12); relanzada con 1,50, termina igual que base, y el reintento ya pagado sale de la caché (5 llamadas, no 6) |
| reanudacion | corte del runner a las 5 unidades (salida 9) y relanzada que termina igual que base |
| error_transitorio | dos errores en el reintento de E1 de `ext::3.6.4.1` (esperas de 20 y 60 s) y después termina igual que base |
| error_persistente | frena el runner tras sus tres intentos (salida 3) |
| mal_formada (sin reuso) | sin tool_use en la verificación de `ext::2.6.1.2` → inutilizable; entidades que no son lista en el reintento de `ext::3.16.2.1` → `cola_humana_reextraccion_invalida`; sin tool_use en la re-verificación de `ext::3.6.4.1` → `cola_humana` |
| modelo_distinto | la guardia frena después de la primera respuesta con otro id; ninguna llamada más |
| mensaje_distinto | la guardia frena antes de la caché y de la red; 0 llamadas |

**Pasan 11 de 11.** Las bases de la copia no cambiaron. El repo tampoco: fotos de las 17:15:06 y las 17:15:29, con 50.450 archivos y
0 nuevos, 0 cambiados y 0 borrados. La primera versión de la corrida en seco, sin el escenario de la base propia, pasó 10 de 10
(17:11:29 a 17:11:41).

## 5. El costo estimado

`r0/controles/r0_f1_costo.py` → `r0/controles/r0_f1_costo.json`, con la fórmula de caching.

- **Tarifas, recomputadas desde sus fuentes:**
  - E3: 0,011911 por llamada (0,238213 / 20, `e3_listas/o3/a/presupuesto.json`).
  - E1 de reintento: 0,012072 (2,969671 / 246, las filas de `e1_reintentos.db` creadas durante la corrida T2, del 05/10/2026 de 14:38:15
    a 22:39). En ese namespace hay una fila más, del 06/10/2026 a las 08:48:34 (USD 0,119735), que no entra en la tarifa.
  - E1 del intento 0: 0,010085 (24,7195 / 2.451, `reext_t0/salida/contadores_t2.json`).
- **Escenarios** (USD):

  | Escenario | Recomputado | Del mandato |
  |---|---|---|
  | A, reusando las 20 de O3 | 0,0719 | 0,0719 |
  | B, sin reusarlas | 0,3102 | 0,3102 |
  | C, peor caso | 0,7179 | 0,7179 |
  | C sin la caché de E1 | 0,9196 | «unos 0,92» |

  La fuente de esos escenarios es un documento de la mesa que vive fuera del repo y no abrí: los recomputé desde las tarifas.
- **Estimación propia con reuso: 0,1555.**
  - 0,0967 por los 3 reintentos con el prefijo leído: las fichas de tokens del reintento de la tanda 0 de cada unidad, y el costo de O3
    de la unidad como aproximación de la re-verificación.
  - Más 0,0588 por la escritura de los dos prefijos en la caché de la API (27.840 tokens de E1 y 11.637 de E3; en la tanda 0 y en O3
    esa escritura quedó repartida).
  - Sin reuso, 0,3937.
- **Todo queda debajo del tope de 1,50.** El tope frena antes de cada llamada, con la proyección del cliente (E3 0,1040; E1 0,0501). Un
  reintento de E1 puede costar más que su proyección: unos 0,12 con 16.384 tokens de salida, la entrada mayor de las fichas (3.120) y la
  escritura del prefijo. Por eso, la última llamada puede pasar el tope en unos 0,07 como mucho.

## 6. Hallazgos y declaraciones

- **Hallazgo.** Si el reintento de E1 devolviera la misma extracción del intento 0, la re-verificación armaría el mismo pedido que la
  verificación y acertaría su fila de la caché, con el mismo veredicto, y la unidad iría a la cola. Es el comportamiento de siempre del
  runner. Apareció en la primera prueba del escenario base, cuyo transporte devolvía la extracción idéntica; desde entonces, el
  simulado le cambia la etiqueta a una entidad.
- **El E3 lo corre `runner_corpus.fase_e3` en la carpeta de trabajo.** Por eso la carpeta tiene `estado_corpus.json` y checkpoints con
  la proyección contra el tope del manifiesto (USD 80), que no aplica: el tope de R0 es el compartido.
- **La guardia frena con una excepción que el reintento de API del runner atrapa.** Trabada, sus dos reintentos frenan antes de la
  caché y de la red, y el runner frena tras sus esperas de 20 y 60 s. Con reintentos de API, `veredictos.jsonl` puede repetir la
  verificación de una unidad (comportamiento del runner, declarado en su encabezado).
- **La corrida en seco no ejercita los reintentos propios del SDK** (`max_retries=3`), porque el transporte simulado reemplaza al
  cliente de la API.
- **Error propio, con su causa.** La copia se armó con la lista de exclusiones de S0-6b, que no excluye `.env`: el `rsync` copió 6
  archivos `.env` al scratchpad. Los borré a las 16:54:12 sin abrirlos, y no hay otra copia. Las copias siguientes los excluyen.
- **Error propio, con su causa.** La primera cuenta de la tarifa de E1 sumaba los `resumen_e1.json` y `resumen_e3.json` de cada TO.
  En las fases reabiertas, esos archivos cuentan solo el último proceso: daba 0,012068 sobre 216 llamadas y 0,009621 sobre 1.981. Lo
  vi porque no reproducía 0,012072, y lo corregí, antes de escribir ninguna cifra, con las filas de la corrida T2 y los contadores de
  T2.
- **No abrí `fuera_del_repo/`.** Solo voy a escribir el paquete y su copia permanente.

## 7. Para la fase 2

- **Decisiones de la autora:**
  - el «seguí»;
  - b (b1 recomendada);
  - c (c1 recomendada);
  - las escrituras que la fase 2 hace y el mandato no enumera, que dependen de b: la base de E3 y la de reintentos de E1 que se
    elijan, y `logs/cache_usage.jsonl` (decisión 3 de caching; git lo ignora).
- **A3r.** Con b1 o b4, las 20 claves de las primeras verificaciones de los ítems entran a la base de E3 del pipeline, y el A3r de hoy
  («ausentes, exactamente, los 1.054 ítems») daría DISCREPANCIA. Redefinido como dice el §1.5: ausentes, los 1.034 ítems que no son de
  R0, y presentes, las 20. `mantenimiento/code/selftest_clave_cache.py` no está entre las escrituras del mandato. Propongo un control de
  R0, en `r0/controles/`, que corra `bloque_anclaje_r2b` sobre una copia y aplique la regla redefinida, más la nota en la tabla de
  reprocesamiento; editar el selftest necesita autorización aparte. Con b2 o b3, A3r no cambia.
- **Deprecaciones.** Antes de correr, la autora o la mesa consultan la página de deprecaciones de los modelos.
- **Comandos,** desde la raíz del repo:
  - `PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/reextraccion_v2/r0/correr_r0.py --correr --tope 1.50 --reuso-o3
    <b1/b2: sembrar | b3: leer | b4: no>` (con b2, además, `--db-e3` y `--db-e1r` en rutas nuevas);
  - con c1, después de los controles, `correr_r0.py --anexar`.
