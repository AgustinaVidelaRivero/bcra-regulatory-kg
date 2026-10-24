# FRENO A2.1-b — tramo 2 de A2.1: el smoke de las dos configuraciones de fragmentos y la caracterización de H-B2

Mandato: `docs/mandatos/A2_1_sistema_por_fragmentos_preregistro_A2_2.md` (texto firmado en `c2b6cb60`, `b311859c…`), §4, §6, §7, §8 y
§9, con el «seguí» del tramo 2 del 23/10/2026, que la autora confirmó como suyo en esta sesión, con la lectura acotada de
`tengu_velvet_ibis` y el script de la mesa como modelo autorizados (registro, §97). Los pasos pagos los corrió la autora en su
terminal; yo no corrí ninguno ni usé el `.env`. Los cambios de código del primer momento están commiteados en `6c6dcad9`
(23/10/2026 16:53:24). Lo de este FRENO no está commiteado; ningún mensaje de commit preparado, nada en la memoria.

**En corto:**

- **Gasto del tramo 2:** USD 0,515819 en R9 y 0,515819 en el CLI (razón 1,0): el smoke, 0,305127 en 12 sesiones; H-B2, 0,210692
  en 8. Dentro del tope (3); el freno (2) no se acercó; el control del disco no cortó ninguna sesión.
- **Las 20 sesiones del diseño** tienen su meta: las 12 del smoke completas (R3), con el mapa R7, el log R1 con su `fin` y el
  aislamiento de punta a punta en los dos brazos; de H-B2, las 4 con `--max-turns` 1 y 2 cortaron (`error_max_turns`) y las otras 4
  terminaron.
- **H-B2, en las dos lecturas:** `--max-turns k` acota los **mensajes del asistente** (las llamadas del modelo a la API), no
  `num_turns` (R-b CARACTERIZADO). Corta cuando el agente ya mandó k mensajes y el k-ésimo pidió tools: el CLI ejecuta esas tools
  y termina sin otra llamada al modelo y sin JSON final. Con las candidatas declaradas antes, R-a da NO VERIFICADO; la cuenta que
  vale en las 32 sesiones, observada después de correr, es `num_turns` = `tool_use` + mensajes del asistente sin `tool_use`.
- **La nota de la mesa:** los brazos de fragmentos sí hicieron llamadas en paralelo (2 por mensaje en HB2-03 y HB2-07, 4 en
  HB2-05, y 2 en las ocho SMK), así que lo de A2.1 solo ya separa los mensajes del asistente de `num_turns`.
- **El valor remoto por tool:** en las 20 sesiones el `.claude.json` de la sesión trae `tengu_velvet_ibis` como un objeto vacío.
  Ninguna tool tiene número; tampoco las cinco del banco.

## 0. Paso 0 (23/10/2026, con `$HOME`)

Igual al del informe «LISTO PARA LOS PASOS PAGOS» (`revision_A2_1_LISTO/`, §1): `main`; `git status --porcelain
--untracked-files=no` vacío; `git merge-base --is-ancestor f619128d HEAD` da 0; `git status --porcelain --untracked-files=all --
data/experiment/banco_mcp` vacío; `claude --version` 2.1.241; el control del SDK sale con 0 (los cinco puntos en OK); el sha256 de
`agentes/lanzar_agente.py` en HEAD, `2f00742038324a8e01122d574981f50a4c23a3927f88aad6b1fe7c4cc8e3e0c5`. El `git log --format='%h %s' -8`
de ese momento empezaba en `0a6374ba` y `fde70c67`; los cinco commits posteriores a `f619128d` no tocan `data/experiment/banco_mcp`
(`git log f619128d..0a6374ba -- data/experiment/banco_mcp` vacío).

## 1. El primer momento: «LISTO PARA LOS PASOS PAGOS»

El informe completo, los diffs y las salidas están en `revision_A2_1_LISTO/` (62 archivos; `manifest.txt` `560a5bca…`; copia
permanente verificada, 62 de 62). En corto:

- **Los cambios**, los únicos que autoriza el «seguí» (`git show --numstat 6c6dcad9`):
  - `a2_1/correr_a2_1.py` (+148 −2): el control del disco y la lectura acotada del valor remoto, después de cada sesión y antes
    de la siguiente (§2);
  - `a2_1/corrida_en_seco_a2_1.py` (+158 −3): la rama nueva, con 12 casos;
  - `mcp_vector/test_fragmentos_a2_1.py` (+4 −2): los logs R1 de los dos transportes con un nombre por corrida, con la hora;
  - los dos JSON de controles, de la corrida en la copia de trabajo.
  `test_aislamiento_a2_1.py` corrió sin cambios con el lanzador de HEAD.
- **La etapa corta:**
  - `test_fragmentos_a2_1.py` dio 8 de 8 en la copia de trabajo y dos veces más en la copia final (la segunda, después de
    `correr_tests` entero). En las tres corridas, las 13 + 13 salidas por MCP y el sha de los rankings del BM25 (`54146ece…`) son
    iguales a los del JSON de `5f0f29b5`.
  - En la copia final, los dos logs viejos quedaron intactos y los cuatro nuevos tienen 15 líneas cada uno.
  - El aislamiento, en modo init y con el lanzador de HEAD, da lo mismo que en `5f0f29b5`.
  - La foto del repo, antes y después de la copia final (15:44:28 y 16:31:52), da 0 cambios.
- **3.4, la copia final del tramo 1:** corrió sin los dos logs viejos porque, antes de la batería, borré en esa copia
  `a2_1/controles/` entero y `aislamiento/resultados/a2_1/`. Fue el comando que siguió a la copia (08:59:45 del 16/10); la batería
  arrancó a las 08:59:53. El FRENO A2.1-a no lo declara (§10, error 1).
- **3.5:** las siete salidas del aislamiento de `5f0f29b5`, iguales en HEAD, van en el paquete con su sha256.
- **La corrida en seco de los dos pasos pagos** (los dos scripts `zsh` con un archivo falso, `A21_MODO=init` y `A21_PYTHON`, desde
  la copia final): 12 y 8 sesiones init, ninguna nueva al reanudar, USD 0. El control del disco estuvo en las 20, sin frenos.
  El valor remoto, en las 20: la clave presente y vacía.

## 2. El control del disco

- **La regla** (`correr_a2_1.control_disco`, decisión de la autora del 23/10/2026): sobre lo que copió `LA.copiar_sesion`, la
  corrida frena con el código 3 sin lanzar otra sesión si algún `tool_result` de `sesion_<id>.jsonl` trae `<persisted-output>`
  o si `tool_results_<id>/` existe y no está vacía. En la meta: el largo de cada resultado en unidades UTF-16 (del `output_str`
  del log R1), el mayor, y su comparación con el tope anotado (200.000).
- **La prueba:** las 12 ramas nuevas de la corrida en seco, en la copia de trabajo y en la copia final, 12 de 12 en las dos. Son la
  referencia con una ruta con un espacio, la transcripción sin ella, `tool_results` vacía y con un archivo, el largo UTF-16 con un
  carácter fuera del plano básico, el código 3 en la corrida y al reanudar, y los tres `.claude.json` de juguete.
- **En los pasos pagos:** en las 20 sesiones la transcripción se copió, 0 tienen la marca y ninguna tiene `tool_results_<id>/`:
  0 frenos. El resultado más largo tiene 12.135 unidades UTF-16 (SMK-02, BM25), lejos de los 200.000 (tabla del §3 y del §4).

## 3. El smoke de las dos configuraciones (`smoke/resultados/a2_1/`)

Corrió el 23/10/2026 de 16:54:33 a 16:57:19 (registro). P0: 1.546 tokens de escritura de caché en el BM25 y 1.548 en el denso (en la
fase B, 2.728); la proyección dio USD 0,6415, por debajo del freno de 2,4.

| sesión | R3 | R7 | log R1 con `fin` | llamadas | máx. `tool_use` por mensaje | largo mayor (UTF-16) | R9 (USD) | CLI (USD) | JSON final (respondible, citas) |
|---|---|---|---|---|---|---|---|---|---|
| P0, BM25 | sí | — | sí | 0 | 0 | 0 | 0,005649 | 0,005649 | no, 0 |
| P0, denso | sí | — | sí | 0 | 0 | 0 | 0,005653 | 0,005653 | no, 0 |
| SMK-01, BM25 | sí | 2 de 2 | sí | 2 | 2 | 4.181 | 0,025379 | 0,025379 | sí, 5 |
| SMK-01, denso | sí | 2 de 2 | sí | 2 | 2 | 3.798 | 0,023558 | 0,023558 | sí, 5 |
| SMK-02, BM25 | sí | 2 de 2 | sí | 2 | 2 | 12.135 | 0,037972 | 0,037972 | sí, 4 |
| SMK-02, denso | sí | 3 de 3 | sí | 3 | 2 | 5.917 | 0,035186 | 0,035186 | sí, 3 |
| SMK-03, BM25 | sí | 2 de 2 | sí | 2 | 2 | 8.562 | 0,032853 | 0,032853 | sí, 3 |
| SMK-03, denso | sí | 2 de 2 | sí | 2 | 2 | 6.780 | 0,027902 | 0,027903 | sí, 3 |
| SMK-04, BM25 | sí | 3 de 3 | sí | 3 | 2 | 5.677 | 0,039881 | 0,039881 | sí, 7 |
| SMK-04, denso | sí | 4 de 4 | sí | 4 | 2 | 5.439 | 0,044986 | 0,044986 | sí, 9 |
| E2E, BM25 | sí | — | sí | 0 | 0 | 0 | 0,009434 | 0,009434 | no, 0 |
| E2E, denso | sí | 1 de 1 | sí | 1 | 1 | 1.332 | 0,016674 | 0,016674 | no, 0 |

- Los costos de la tabla van redondeados a 6 decimales; la suma exacta, por sesión, está en `a2_1/hb2/analisis_tramo2_A2_1.json`.
- **Adaptación:** las 8 SMK quedaron adaptadas, con el mapa R7 coincidente y atribuibles, sin truncados por el transporte
  (`registro_smoke_a2_1.json`, `trazas`).
- **Aislamiento de punta a punta:** en los dos brazos, el `system/init` trae solo `mcp__fragmentos__buscar_pasajes`, y hay 0
  denegaciones (no hay capacidad que denegar). Las dos respuestas dicen que no pueden conectarse al puerto 7687 ni leer archivos.
  El denso hizo una búsqueda antes de responder.
- **R9 contra el CLI:** iguales en las 12 (razón 1,0); el banco sigue computando desde los tokens.
- Las 12 corrieron con CLI 2.1.241 (la sellada).
- Hubo llamadas del modelo interno (`claude-haiku-4-5-20251001`) en las 12 sesiones del smoke y en 6 de las 8 de H-B2 (no en
  HB2-01 ni HB2-02), como en la fase B (R8).

## 4. H-B2 (`a2_1/hb2/`), con las reglas del diseño (`a2_1/diseno_HB2.md`, §5)

Corrió el 23/10/2026 de 17:00:24 a 17:03:25.

| sesión | brazo | k | mensajes del asistente | con `tool_use` | `tool_use` | `tool_result` | máx. por mensaje | `num_turns` | `subtype` | log R1 (`fin`) | R3 | largo mayor | R9 (USD) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| HB2-01 | BM25 | 1 | 1 | 1 | 2 | 2 | 2 | 2 | `error_max_turns` | 2 (sí) | no | 6.045 | 0,002904 |
| HB2-02 | BM25 | 2 | 2 | 2 | 3 | 3 | 2 | 3 | `error_max_turns` | 3 (sí) | no | 5.675 | 0,018243 |
| HB2-03 | BM25 | 2 | 2 | 1 | 2 | 2 | 2 | 3 | `success` | 2 (sí) | sí | 8.551 | 0,034412 |
| HB2-04 | BM25 | 12 | 2 | 1 | 2 | 2 | 2 | 3 | `success` | 2 (sí) | sí | 8.551 | 0,015064 |
| HB2-05 | BM25 | 3 | 2 | 1 | 4 | 4 | 4 | 5 | `success` | 4 (sí) | sí | 9.575 | 0,062008 |
| HB2-06 | denso | 1 | 1 | 1 | 2 | 2 | 2 | 2 | `error_max_turns` | 2 (sí) | no | 4.742 | 0,003980 |
| HB2-07 | denso | 2 | 2 | 2 | 3 | 3 | 2 | 3 | `error_max_turns` | 3 (sí) | no | 6.778 | 0,022444 |
| HB2-08 | denso | 12 | 2 | 1 | 4 | 4 | 4 | 5 | `success` | 4 (sí) | sí | 6.156 | 0,051637 |

Dos lecturas, declaradas en el diseño antes de correr: con lo de A2.1 (las 8 de H-B2 y las 12 del smoke, 20 sesiones) y con el
antecedente de la fase B sumado (32). Las dos válidas en todas: ninguna sin `result`.

- **Qué cuenta `num_turns` (R-a).** Con las cuatro candidatas declaradas, NO VERIFICADO en las dos lecturas: `tool_result` + 1
  (y las otras dos equivalentes) coincide en 16 de 20 y en 28 de 32, y falla justo en las cuatro cortadas, donde `num_turns` vale
  `tool_result` y no `tool_result` + 1. Los mensajes del asistente coinciden en 4 de 20 y en 12 de 32. La cuenta que vale en las
  32 sesiones es `num_turns` = `tool_use` + mensajes del asistente sin `tool_use`, es decir, una vuelta por cada tool pedida más
  una por la respuesta final si la hubo (`a2_1/hb2/analisis_tramo2_A2_1.json`: 20 de 20 y 12 de 12). La observé después de
  correr; no es una de las candidatas pre-declaradas.
- **Si `--max-turns` corta y cuándo (R-b).** CARACTERIZADO en las dos lecturas: acota los mensajes del asistente. Es el único
  conteo compatible con todas las sesiones, y al cortar vale exactamente k (valor − k = 0 en los cuatro cortes). Lo excluyen:
  - `num_turns`, por HB2-03 (3 con k = 2), HB2-05 (5 con k = 3) y, en el antecedente, SMK-04-kg (14 con k = 12), todas sin corte;
  - `tool_use` y las llamadas del log R1, por HB2-05 (4 con k = 3) y SMK-04-kg (13 con k = 12).
  Una sesión que con el k-ésimo mensaje da la respuesta final termina bien (HB2-03: k = 2, dos mensajes, `success`). Corta la que
  con el k-ésimo mensaje pide tools.
- **Qué deja cada corte (R-c).** En los cuatro (HB2-01, HB2-02, HB2-06 y HB2-07):
  - `subtype` `error_max_turns`, `is_error` verdadero, `stop_reason` `tool_use`;
  - el CLI ejecuta las tools del k-ésimo mensaje: todos los `tool_use` tienen su `tool_result`, y el log R1 registra esas llamadas
    y tiene su `fin`;
  - no hay otra llamada al modelo ni JSON final, así que por R3 la traza queda incompleta («result.subtype=error_max_turns», «el
    resultado no contiene un bloque JSON») y sale de la métrica, declarada.
  - El costo de una sesión cortada es el de sus k llamadas (USD 0,0029 a 0,0224).

## 5. La nota de la mesa sobre H-B2

El `num_turns` 14 con tope 12 de la fase B vino de llamadas en paralelo, y allí solo las hizo el brazo del grafo: es el
antecedente, con 9 mensajes del asistente y 13 `tool_use`. En A2.1 las preguntas compuestas **sí** produjeron llamadas en paralelo
en los brazos de fragmentos. El máximo de `tool_use` por mensaje:

| sesión | HB2-03 | HB2-05 | HB2-07 | HB2-01 | HB2-02 | HB2-04 | HB2-06 | HB2-08 | SMK (las 8) | P0 y E2E-BM25 | E2E-denso |
|---|---|---|---|---|---|---|---|---|---|---|---|
| máximo | 2 | 4 | 2 | 2 | 2 | 2 | 2 | 4 | 2 | 0 | 1 |

Las preguntas solas (SMK-04 en HB2-01, HB2-02 y HB2-06, y las ocho SMK del smoke) también las produjeron, cosa que en la fase B el
brazo vectorial nunca hizo. Por eso, con lo de A2.1 solo, R-b ya separa los mensajes del asistente de `num_turns` (CARACTERIZADO).
El antecedente del grafo es coherente y lo confirma en la segunda lectura. La semántica es del CLI y no del brazo: vale igual para
el brazo del grafo.

## 6. Propuesta del criterio de corte R5, sobre la señal verificada

La señal verificada es **la cantidad de mensajes del asistente** (`message.id` distintos del modelo principal en el stream), que
es lo que el CLI acota con `--max-turns`. Las llamadas a tools se cuentan aparte, sin pérdida, en el log R1 (= `tool_use` en las 32
sesiones). El criterio lo fija la autora al firmar el pre-registro de A2.2.

- **Propuesta (a):** mantener `--max-turns 12` como corte duro, leído como «a lo sumo 12 mensajes del asistente: hasta 11 rondas
  de tools y la respuesta». Registrar por traza los mensajes del asistente, los `tool_use`, las llamadas del log R1 y `num_turns`.
  Una traza cortada (`error_max_turns`) queda incompleta por R3, sale de la métrica y se declara. Así no cambia nada de la config
  sellada y la regla se lee sobre la señal que el CLI aplica.
- **Alternativa (b):** si lo que se quiere acotar son las **llamadas a tools** (el «tope de 10 tool calls» del prompt, que es solo
  instructivo), `--max-turns` no lo garantiza: con llamadas en paralelo, k mensajes pueden pedir muchas más de k tools (HB2-05: 4
  con k = 3; SMK-04-kg: 13 con k = 12). Habría que acotarlas en el servidor (que rechace la llamada N + 1 de la sesión, contada por
  el log R1), con su prueba. Es código nuevo en los servidores.
- **Alternativa (c):** el mismo corte de (a) y, después, excluir las trazas que pasen de N llamadas en el log R1, declaradas. No
  corta nada: es un filtro.
- **Alternativa (d):** un tope sobre `num_turns`. El CLI no lo aplica, y `num_turns` mezcla las rondas con la cantidad de tools
  en paralelo. No lo recomiendo.
- **Para el brazo del grafo:** con lo de A2.1 solo, R-b quedó CARACTERIZADO, porque los brazos de fragmentos hicieron llamadas en
  paralelo; el caso «INDISTINGUIBLE» que preveía la mesa no se dio. La propuesta no depende del brazo. El brazo del grafo hace
  más llamadas en paralelo (en la fase B, hasta 3 por mensaje y 13 `tool_use` en 9 mensajes), así que para él la diferencia entre
  (a) y (b) pesa más.
- [DECIDE LA AUTORA]: (a), (b), (c) o una combinación, y el valor de k o de N.

## 7. El valor remoto de cada sesión

En las 20 sesiones de los pasos pagos (y en las 20 init de la corrida en seco y la del aislamiento), el `.claude.json` de la
carpeta de configuración de la sesión existe y la clave `tengu_velvet_ibis` aparece una vez, como un objeto vacío: ningún nombre de
tool con número. Las cinco tools del banco con número: ninguna en ninguna sesión. El control del disco no frenó en ninguna.

## 8. El gasto

`a2_1/hb2/analisis_tramo2_A2_1.json` (`analisis_tramo2_A2_1.py`, en la misma carpeta; lee las metas, no escribe en el repo):

| paso | sesiones | R9 (USD) | CLI (USD) | cota (USD) |
|---|---|---|---|---|
| 1, smoke | 12 | 0,305127 | 0,305128 | 0,3827 |
| 2, H-B2 | 8 | 0,210692 | 0,210691 | 0,7478 |
| total del tramo 2 | 20 | 0,515819 | 0,515819 | 1,1305 |

El acumulado más alto antes de una sesión fue el de antes de HB2-08, USD 0,464182 = 0,515819 − 0,051637: con los 0,30 de
presupuesto, 0,764182, por debajo del freno de 2. No hubo freno, ni de proyección ni del disco. El gasto por sesión está en el §3 y
el §4.

## 9. La foto del repo, los `.pyc` y el grep de convenciones

Foto sha256 del repo entero sin `.git`, con los `.env` y los `NO_ABRIR_*` solo por tamaño y fecha (en el paquete, enmascaradas
como en el tramo 1):

| foto | hora (23/10/2026) | entradas | `.pyc` (fuera de los venvs) |
|---|---|---|---|
| antes de escribir | 15:17:32 | 58.927 | 10.158 (243) |
| después de escribir los cinco archivos | 15:43:51 | 58.927 | 10.158 (243) |
| antes y después de la copia final | 15:44:28 y 16:31:52 | 58.927 | 10.158 (243) |
| después de los pasos pagos | 17:07:54 | 59.077 | 10.158 (243) |
| al frenar, con este FRENO y el análisis | después de escribirlos (`foto_al_frenar_b_A2_1b.json`) | 59.080 | 10.158 (243) |

- **Contra la foto de antes de escribir:**
  - al escribir, 5 cambiados: `correr_a2_1.py`, `corrida_en_seco_a2_1.py`, `test_fragmentos_a2_1.py` y los dos JSON;
  - después de los pasos pagos, además 150 nuevos: 93 en `smoke/resultados/a2_1/` (las 12 sesiones con sus 7 archivos, el registro
    y las 8 trazas) y 57 en `a2_1/hb2/` (las 8 con sus 7 y el registro);
  - al frenar, 3 más: este FRENO, `a2_1/hb2/analisis_tramo2_A2_1.py` y su JSON;
  - 0 borrados y 0 fuera de las rutas autorizadas, en todas las comparaciones (`comparar_fotos_b`, en el paquete).
  - La última foto se toma después de escribir este archivo, y su resultado va en el mensaje del FRENO.
- **Los `.pyc`:** 10.158 en todas, 243 fuera de los dos venvs; ningún `.pyc` en las dos copias.
- **Fuera del repo:** en `~/INGENIERIA IA/TESIS/fuera_del_repo/banco_sesiones/config/` hay 21 carpetas de configuración de mis
  corridas init (USD 0) y las 20 de los pasos pagos, que creó el lanzador en la raíz que él fija. El `cwd` compartido quedó vacío.
- **Grep de convenciones** (`LC_ALL=en_US.UTF-8`, el script de `segmentacion_oficial_e0r2/s0_4/scripts/`, sobre copias en el
  scratchpad):
  - los cinco archivos del primer momento, este FRENO y el análisis: total 0;
  - **las salidas de los pasos pagos:** 40 archivos con coincidencias, los 20 `sesion_*.jsonl` y los 20 `stream_*.jsonl` (12 y 12
    en el smoke, 8 y 8 en H-B2). Son salida literal del CLI y traen el `cwd` absoluto de la sesión, `banco_sesiones/cwd`, que está
    bajo la carpeta personal: la ruta lleva el nombre de la cuenta. Las metas, los comandos, los logs R1, los registros y las
    trazas no lo traen (el lanzador enmascara la carpeta personal). No los toqué: son la evidencia de la corrida paga.
  - En U-A2.0-banco esos streams quedaron en el repo y declarados (README del banco, «Nota de confidencialidad»); en el tramo 1
    saqué del repo el único stream de init, que era mío.
  - [DECIDE LA AUTORA], antes del commit: dejarlos así, declarados, o enmascarar el `cwd` en esas 40 copias.

## 10. Errores propios, con su causa

1. **El FRENO A2.1-a no declara que borré `a2_1/controles/` y `aislamiento/resultados/a2_1/` en la copia final del tramo 1**
   antes de su batería. Ese borrado es lo que dejó correr los tests sin los dos logs viejos (punto 3.4). Causa: lo tomé como
   preparación de la copia y no como un cambio a lo que la copia traía del repo.
2. **Dos conteos mal en el informe LISTO:** «+132 −2» y «+147 −3» para `correr_a2_1.py` y `corrida_en_seco_a2_1.py`. Los
   números son +148 −2 y +158 −3: mi expresión no contaba las líneas agregadas vacías. Y escribí «los tres commits que siguen a
   `f619128d`», cuando son cinco. Causa: no recomputé esas cifras contra el comando antes de escribirlas (CLAUDE.md §4.i). Acá van
   corregidas, con su comando.
3. **R-a sin la candidata correcta:** las cuatro candidatas pre-declaradas no incluían la cuenta que resultó valer en las 32
   sesiones; por la regla, R-a queda NO VERIFICADO y la cuenta va como observada después de correr. Causa: armé las candidatas
   sobre la fase B, donde ninguna sesión cortó.
4. Un separador `=====` de un comando de control falló en `zsh`. No cambió nada.

## 11. Lo que queda abierto

- [DECIDE LA AUTORA]: el criterio R5 (§6) y qué hacer con el `cwd` de los 40 streams y transcripciones (§9).
- El tramo 3, el pre-registro de A2.2 en BORRADOR, espera su «seguí».

## 12. Cierre

- Checkpoint: `checkpoint_A2_1.md`, en el scratchpad de la sesión, con su espejo en
  `~/INGENIERIA IA/TESIS/fuera_del_repo/scratchpads/94968c98-6fa5-449c-954b-42ee7ee26062/scratchpad/`.
- El paquete `revision_A2_1_FRENO_b/`, con su `manifest.txt`, y su copia con `ditto` en
  `~/INGENIERIA IA/TESIS/fuera_del_repo/scratchpads/94968c98-6fa5-449c-954b-42ee7ee26062/scratchpad/revision_A2_1_FRENO_b/`; la
  verificación va en el mensaje del FRENO. El de `revision_A2_1_LISTO/` sigue en su lugar.
- Nada commiteado, ningún mensaje de commit preparado, nada en la memoria.

FRENO A2.1-b. Espero el «seguí» del tramo 3.
