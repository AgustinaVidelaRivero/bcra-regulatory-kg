# FRENO — U-BANCO-R5-a: el lanzador del lote con R5 de la entrada sellada y la guarda con `correr_b63.py`

Unidad a USD 0: sin API, sin Neo4j, sin Docker y sin el denso. No escribí en el repo, no commiteé y no edité ningún archivo de HEAD
ni de `b63/`. Todo lo nuevo está en la copia (`r5_y_patron/copia/`, HEAD `a9636f37b73dc5c9fafc6a37372b6236e83b37fc`) y en
`r5_y_patron/`. Espero la revisión de la mesa.

## 1. Lo que hice

1. **El paso 0** (§2), **el control de los renglones 328 y 330 del pre-registro** (§3), la foto sha256 del repo antes, **la
   copia** con el `rsync` del despacho y sus controles (§4).
2. Escribí en la copia, desde `git show HEAD:`, los 13 archivos que uso de `agentes/`, `paralelo/` y `b63/`, y controlé su
   sha256 (`salidas/escritos_desde_head_r5.tsv`: los 13 son iguales al blob de HEAD, en lo del rsync y en lo escrito). Tomé los
   sellos de HEAD en la copia antes: 2503 de 2503 iguales.
3. **Los archivos nuevos** (§5), en la copia:
   - `agentes/lanzar_lote_paralelo_r5.py`;
   - `paralelo/guardas_lote_r5.py`;
   - `agentes/NOTA_lanzar_lote_paralelo_r5.md`;
   - el selftest y la corrida en seco, con sus juguetes en `paralelo/seco_r5/`.
4. **El selftest**, 11/11 OK (§6), y **la corrida en seco**, 11/11 OK en el tercer intento (§7; los dos anteriores, en §11).
5. **El cierre:** los sellos de la copia y la foto del repo después (§10), el grep (§12) y el paquete (§13).

## 2. Paso 0 (con la carpeta personal como `$HOME`)

```
--- revision_* en el scratchpad y en la copia permanente:
$HOME/INGENIERIA IA/TESIS/fuera_del_repo/scratchpads/95486f81-2327-4620-90bc-f61b59d22c1a/scratchpad/revision_UBANCO_PARALELO
$HOME/INGENIERIA IA/TESIS/fuera_del_repo/scratchpads/95486f81-2327-4620-90bc-f61b59d22c1a/scratchpad/revision_UBANCO_PARALELO_b
<scratchpad>/revision_UBANCO_PARALELO
<scratchpad>/revision_UBANCO_PARALELO_b
revision_UBANCO_PARALELO: 55 de 55 contra el manifest de la copia permanente; distintos o faltantes: []; sin entrada: []
revision_UBANCO_PARALELO_b: 56 de 56 contra el manifest de la copia permanente; distintos o faltantes: []; sin entrada: []
--- 209 en la historia: sí; HEAD a9636f37; status: 0 líneas
1bcadb445ef4b3716d6977950e83c08075e7da58324d124e3f6490e9fa3df448  HEAD:data/experiment/banco_mcp/agentes/lanzar_lote_paralelo.py
73c317682951e2b01314db606f1a8682256f23330e1b88a735ae4e915c0528a2  HEAD:data/experiment/banco_mcp/paralelo/guardas_lote.py
--- data/experiment/banco_mcp/b63/: en el repo: sí | en HEAD: sí
shasum -a 256 -c data/experiment/banco_mcp/b63/sha256_etapa_a_b63.txt:   23 OK (rc 0); status de b63/: 0 líneas
```

- **Restauraciones:** ninguna. Los dos `revision_*` del scratchpad dan, archivo por archivo, el sha256 del `manifest.txt` de su
  copia permanente.
- **El `status`** del paso 0 es el de lo versionado (`--untracked-files=no`).
- **De `b63/` leí solo** `comun_b63.py`, `correr_b63.py` y, de `FRENO_B63_a.md`, sus títulos (`grep -n '^## '`) y los
  renglones 294 a 353, que son §8 y §9. Hubo una excepción, un error propio: §11, punto 2.

## 3. El control del pre-registro

`scripts/control_preregistro_r5.py` lee `git show HEAD:docs/preregistro_B6_3_evaluacion_final.md` y controla por código, sin
imprimirlos, que los números de los renglones 328 y 330 traigan, en ese orden, 30, 32 y 1,80, y 45, 47 y 3,30. Del pre-registro
no leí nada más.

```
renglón 328: OK (30, 32, 1,80, en ese orden)
renglón 330: OK (45, 47, 3,30, en ese orden)
HEAD:docs/preregistro_B6_3_evaluacion_final.md sha256 66f827410c8909664d8d0b1336e8cdde27def1c802b5376922c70434b5daaef6
los dos R5 del pre-registro: OK
```

## 4. La copia

Hice la copia con el `rsync` del despacho, tal cual (`copia.rsync.log`: 336 renglones, los 336 «skipping non-regular file»). El
control es `salidas/control_copia_r5.txt`:

```
--- nombres vedados (NO_ABRIR_*, *_SOLO_MESA*, .env, .env.*, *.env): 0
--- enlaces: 0
--- .git, .venv, .venv-app, .DS_Store, __pycache__: 0
test ! -e data/experiment/reextraccion_v2/corpus_tanda_final: no está
test ! -e data/experiment/tanda_final: no está
test ! -e logs: no está
test ! -e data/experiment/neo4j/volumen: no está
test ! -e data/experiment/banco_mcp/mcp_kg/indice_puntos: no está
--- las dos carpetas de adjudicación:
test ! -e data/experiment/segmentacion_oficial_e0r2/s1ter/adjudicacion: 0 (no está)
test ! -e data/experiment/segmentacion_oficial_e0r2/s1quater/adjudicacion: 0 (no está)
--- bases .db* de las dos cachés: 0
```

## 5. Los archivos nuevos, con su sha256

Las rutas son relativas a la copia salvo `bin/` y `scripts/`, que son de `r5_y_patron/`.

```
73b21753e826b91fb878b8ebc6f5fd34262e27be6a974fdb17051e825934e2e2  data/experiment/banco_mcp/agentes/lanzar_lote_paralelo_r5.py
04f81fe3bc522fb76166fe2190761b66de68e65e72191302b87c4461b532fae2  data/experiment/banco_mcp/paralelo/guardas_lote_r5.py
17b738b0d653ada6d5d881ec6732ea1907427304432b06e6c52310c4ed3f767b  data/experiment/banco_mcp/agentes/NOTA_lanzar_lote_paralelo_r5.md
29d02326b6eca92b6edf4a251c846f685cc9dd6f19953bf92b7f52be4daa913c  data/experiment/banco_mcp/agentes/selftest_lanzar_lote_paralelo_r5.py
919c29390df12c03b7ffcbc1e8f2e2f6c84c30ce0212419e4a626c8a6d942ba2  data/experiment/banco_mcp/paralelo/corrida_en_seco_lote_r5.py
08a650e92390b687ef4e2c965856b16451b06af0adaa8774a12a2b7928df59f2  data/experiment/banco_mcp/paralelo/seco_r5/lanzar_agente_r5_prueba.py
0f4931748b6d3139d9ada22ba201e5e728c2ce19af86c3eafba1544e55d9aba5  data/experiment/banco_mcp/paralelo/seco_r5/config_agentes_r5_A.json
ba29dfd5b7db171d3afec8003515a5acd976c2db1633a97c283f1f2d2575ec2b  data/experiment/banco_mcp/paralelo/seco_r5/config_agentes_r5_B.json
f4670840045aa8b6d4bb265fd2ea31fb6d6cd4691fdf32d261ca1ee7877d8d38  bin/claude
```

### `lanzar_lote_paralelo_r5.py`

- **Qué importa.** Importa `lanzar_lote_paralelo.py` de HEAD (`1bcadb44…`) sin editarlo. `Lote` es una subclase de `BASE.Lote`.
- **R5.** Lo toma de la entrada: `--entrada` y `--sha256-entrada`, con la clave `CLAVE_R5 = "R5"`.
  - `R5_ADMITIDOS` son los dos del pre-registro, en su orden. El primero es el `R5_ESPERADO` de HEAD.
  - Con otro R5, `correr()` frena con el 5 sin lanzar ninguna sesión y escribe el registro, con cada sesión «no lanzada».
  - Una sesión con otro R5 frena con el 5: `control_aislamiento` es el de BASE con el R5 de la entrada en lugar de
    `BASE.R5_ESPERADO`. Lo cambia solo durante el control y lo restituye en un `finally`.
- **`--presupuesto-sesion`.** Sale del `max_budget_usd` de la entrada. Uno distinto da un `SystemExit` de texto, que `main` convierte
  en el 3.
- **La guarda.** `BASE.G` pasa a ser `guardas_lote_r5`.
- **El registro.** Suma el bloque `R5`: la entrada (ruta, sha256, clave y R5), los admitidos, si fue admitido y el lanzador r5.
- **`--patron-de-prueba`.** Solo corre con un CLI falso en el PATH. Fija el patrón `<token>\.py|<token>_b63\.py`, que tiene la
  forma del real.

### `guardas_lote_r5.py`

- `PATRON_PAGO` es `guardas_lote.PATRON_PAGO + r"|correr_b63\.py"`. `PATRON_PAGO_REAL` lo guarda, aunque una prueba cambie el
  patrón.
- El filtro es el mismo objeto que el de BASE (`script_python`, `guardas_lote.py:87-99`).
- Excluye los ancestros, el proceso propio y los descendientes, propios y los del lote.
- `pgrep()` sirve para esperar, con el mismo patrón.
- `extraccion_corriendo()` es la de BASE, pero lee el `PATRON_EXTRACCION` de este módulo. Así vale el patrón de prueba que fija el
  runner (§8).

### La nota

`NOTA_lanzar_lote_paralelo_r5.md` dice qué cambia en `correr_b63.py`:

- los imports (`:65-66`);
- el `Namespace` de `:245-248`, que suma `entrada` y `sha256_entrada`;
- los códigos de `:255`;
- `fijar_patron_de_prueba` y `control_patron`.

En `comun_b63.cargar_entrada` (`:153-162`), cambia el control contra `R5_ESPERADO` por `admitido()`. La nota dice también lo que
pide el R5 B: una `config_agentes` con su `corte_R5`.

## 6. El selftest (`salidas/selftest_r5.json`): 11/11 OK

Corrió con `env -i PATH=/usr/bin:/bin HOME`, con el python del `.venv` del repo y con `-I -B`, sin lanzar ningún proceso.

| | Control | Resultado |
|---|---|---|
| T1 | los admitidos | los dos del pre-registro, en su orden; el primero es el de HEAD |
| T2 | la clave | `cargar_entrada` lee `e["R5"]` y exige «R5» entre los campos; el módulo no tiene una constante con ese valor |
| T3 | `admitido()` | sí con 4 formas de A y de B (en otro orden, 3,30 escrito así); no con 11 (C, `{}`, una clave de más o de menos, cada mezcla de A y B, 1,81, 48 y `"32"` de texto) |
| T4 | `r5_de_la_entrada()` | otro sha256, una entrada que no existe y una sin R5 frenan |
| T5 | el presupuesto | 1,80 con A y 3,30 con B; en init, la guarda en 0; uno explícito igual pasa y uno distinto frena (B con 1,8 y A con 3,3) |
| T6 | `control_aislamiento` | A con A y B con B pasan; A con B da «distinto de» y «pasa el presupuesto»; B con A, «distinto de»; `R5_ESPERADO` vuelve a A, también tras una falla adentro |
| T7 | el patrón y el filtro | `BASE.G` es `guardas_lote_r5`; el patrón es el de `guardas_lote` más `correr_b63\.py`, y el de `guardas_lote` es el renglón 16 más `correr_prueba_T_v2\.py`; sobre líneas escritas en el selftest, 5 cuentan y 8 no (`pgrep`, `zsh -c`, `grep`, `vim`, `less`, un Python que lo nombra como argumento, `correr_b63_copia.py`, un `.sh`) |
| T8 | el patrón de prueba | `rcinco_prueba_paso\.py\|rcinco_prueba_paso_b63\.py`; no ve el real y el real no lo ve |
| T9 | `main` | otro sha256, una entrada que no existe, una sin R5 y un presupuesto distinto dan el 3, sin registro; sin `--entrada`, el 2 de argparse |
| T10 | un lote inválido para `validar` (P = 0) | el `main` r5 da el 3; el de HEAD, un `SystemExit` de texto (§8) |
| T11 | `otro_paso_pago`, con una tabla de procesos, un `pgrep` y un `ps` de juguete | de 7 que da el `pgrep` de juguete, ve al hermano `correr_b63.py` y al hijo `correr_a2_2.py` de otro lote; con la raíz de ese lote, solo al hermano; no ve al padre, al abuelo, al hijo propio, al `pgrep` ni al shell |

## 7. La corrida en seco (`salidas/corrida_en_seco_r5.json`): 11/11 OK

- **Cómo corrió.** Con `env -i` (PATH del sistema, HOME, LANG y `BANCO_VENV_VECTOR`), el CLI falso por `bin/claude`, una clave de
  relleno y `ANTHROPIC_BASE_URL` en `http://127.0.0.1:9`. Solo usé el brazo `fragmentos_bm25`, cuyo servidor no carga ningún
  modelo ni el driver del grafo.
- **El patrón.** Cada llamada al lanzador llevó `--patron-de-prueba rcinco_prueba_paso`, y cada guarda que corrió la prueba, ese
  patrón: ningún `pgrep` llevó el patrón real.
- **El volumen.** Hubo 13 sesiones de juguete, en los 12 lotes que dejaron registro. El R9 sintético del `modelUsage` falso suma 0,6304: es la suma de
  `acumulado_R9_usd` de los 12 `registro_lote.json` de `salidas/seco/`. No es gasto: la API no recibió nada.

| | Rama | Resultado |
|---|---|---|
| D0 | el CLI y el token | sin un CLI falso en el PATH (`/usr/bin:/bin`), el token se rechaza; con el falso, se rechazan 7 tokens: `correr_b63`, uno con `correr`, uno con `juez`, uno con mayúscula, uno corto, `xrun_posthoc` y `ensamblar_tanda0`, estos dos por el patrón real |
| D1 | entrada A, sesiones A | 0; presupuesto 1,8 (sale de la entrada); 3 terminadas, 3 a la vez; cada una con `--max-turns 32`, `--max-budget-usd 1.8`, tope 30 en la meta y el prompt de su config; guarda de otro paso pago: `hallados []` |
| D2 | entrada B, sesiones B | 0; presupuesto 3,3; 3 terminadas, 3 a la vez; 47, 3.3 y 45 |
| D3 | entrada C (42, 40 y 2,60) | 5; «no es uno de los admitidos»; 2 «no lanzada», 0 carpetas de configuración y 0 de salida |
| D4 | otro sha256 | 3; «LOTE INVÁLIDO: la entrada sellada da 73da5f6b77a9…, no el sha256 fa50e558204f…»; sin registro ni carpeta |
| D5 | entrada A, sesiones B | 5 al terminar la primera: «R5 … distinto de …» y «su --max-budget-usd 3.3 pasa el presupuesto»; la segunda, «no lanzada» |
| D5 | entrada B, sesiones A | 5: «distinto de»; la segunda, «no lanzada» |
| D6 | presupuesto explícito con B | 1.8 da el 3 («no es el max_budget_usd del R5 de la entrada (3.3)»); 3.3 corre (0) |
| D7 | un hermano vivo con un nombre del patrón | con `rcinco_prueba_paso.py` y con `rcinco_prueba_paso_b63.py`: `pgrep()` lo ve; la guarda como comando da el 7 («FRENO: otro paso pago corriendo (…)»); el lote da el 7 con 0 lanzadas y 0 carpetas. Al cerrarle la entrada (rc 0), `pgrep()` ya no lo ve, la guarda da el 0 y el lote corre (0, 1 terminada) |
| D8 | sus ancestros con un nombre del patrón | un runner `rcinco_prueba_paso_b63.py` que corre el lote en su proceso, como `correr_b63.py`, y uno `rcinco_prueba_paso.py` que lo lanza como hijo: los dos con rc 0, 1 terminada y `hallados []`; `pgrep -a` ve a los dos, `pgrep` sin `-a` no ve a ninguno (§8), y la tabla de ps, con el filtro, ve al primero como del patrón |
| D9 | otras guardas a la vez | un proceso que se presenta como `pgrep -c … -f rcinco_prueba_paso.py\|rcinco_prueba_paso_b63.py`, un Python que espera con ese patrón como argumento y un `sh -c 'read x' rcinco_prueba_paso_b63.py`: `pgrep()` ve a los tres; la guarda da el 0 y el lote corre (0, 1 terminada, `hallados []`) |

## 8. Lo que encontré y declaro

1. **El `pgrep` de macOS.** Sin `-a`, deja fuera al proceso que lo llama y a todos sus ancestros (`man pgrep`, `-a`). Lo medí:
   `pgrep -f '^/bin/sh -c pgrep'` desde ese shell da 0, y con `-a`, 2. En macOS la exclusión de los ancestros ya la hace
   `pgrep`. La de `guardas_lote` (y la de `guardas_lote_r5`) sigue siendo necesaria donde `pgrep` no la hace; la ejercita T11.
   D8 muestra el comportamiento de punta a punta.
2. **El `main` de `lanzar_lote_paralelo.py` en HEAD sale con 1, no con el 3, ante un lote inválido.**
   - La causa: `validar` levanta `SystemExit` con texto y `main` no lo captura.
   - El runner de B6.3 no lo sufre, porque importa `Lote` y captura el `SystemExit` (`correr_b63.py:255`).
   - El `main` r5 lo captura y da el 3 (T10).
3. **La clave de R5.** `comun_b63.py` la define como el campo «R5» de la entrada: su docstring (`:17`), la lista de campos que
   exige (`:112`) y `e["R5"]` (`:155`). No hay una constante con nombre. Tomé «R5» y no frené. Si la mesa pedía una constante con
   nombre, este es el punto que hay que revisar.
4. **`BASE.G = guardas_lote_r5` vale para todo el proceso.** Lo cambia el import del lanzador r5. Un runner que importe a la vez
   el lanzador de HEAD y el r5 usa la guarda r5 en los dos.
5. **`control_patron` del runner.** Con `guardas_lote_r5`, `patron_igual_al_renglon_16_mas_T` daría `False`. Es informativo y no
   frena. La nota propone la comparación nueva.
6. **El R5 B pide una `config_agentes` con `corte_R5` 47, 45 y 3,30.** `cargar_entrada` (`:157-159`) compara la entrada con su
   configuración. La de hoy trae la A.
7. **Una observación sobre el filtro de BASE.** Un `python -c '…' …/correr_b63.py` cuenta, porque el filtro toma como script todo
   lo que sigue a las opciones hasta el primer `.py`. Frena de más, del lado seguro. Va en T7, fuera de su OK.
8. **El python.**
   - El CLI falso (`bin/claude`) y el selftest y la corrida en seco corrieron con el python del `.venv` del repo, en solo lectura y
     con `-B`. La copia no trae `.venv`, y por eso no usé `paralelo/cli_falso/claude` de la copia, que busca uno junto a ella.
   - El servidor BM25 corrió con el venv de `BANCO_VENV_VECTOR` (`$HOME/INGENIERIA IA/TESIS/venvs/banco_vector_py312`).
   - En la copia no quedó ningún `__pycache__`.
9. **La versión del CLI falso.** Dice «… de U-BANCO-PARALELO». Es el `claude_falso.py` de HEAD sin cambios.

## 9. Los criterios de aceptación

1. **El paso 0** (§2): todo da y no hubo nada que restaurar.
2. **El pre-registro** (§3): los dos renglones dan OK, sin imprimirlos.
3. **La copia** (§4): 0 vedados, 0 enlaces, sin las zonas excluidas y sin las dos carpetas de adjudicación.
4. **HEAD y `b63/` en la copia, antes y después.** `scripts/sellos_copia_r5.py` cubre los archivos versionados de `banco_mcp`,
   `neo4j` y `tanda0/code`, `b63/` incluida, y los 13 escritos desde HEAD:
   - antes: «2503 versionados; en la copia 2503; iguales al blob de HEAD 2503; distintos []; faltan []»;
   - después: lo mismo, medido contra `a9636f37`, el commit de la copia, porque HEAD se movió (§10);
   - `salidas/sellos_copia_comparacion.txt`: «antes y después iguales (2503 renglones)».
5. **El selftest y la corrida en seco** (§6 y §7): 11/11 y 11/11.
6. **El repo** (§10) igual antes y después, salvo las 4 rutas de los tres commits que entraron durante el cierre, ninguno mío; y
   **el grep** (§12): 0.

## 10. El repo, antes y después

`scripts/foto_repo_r5.py` toma el sha256 de cada archivo del repo:

- No entra en `.git`, en las dos carpetas de adjudicación ni en `NO_ABRIR_*` y `*_SOLO_MESA*`.
- Toma los `.env` por su tamaño y su fecha, sin abrirlos.

- **La primera foto de después**, tomada tras el segundo intento de la corrida en seco, dio «antes: 60957 entradas; después:
  60957; nuevos: 0; borrados: 0; cambiados: 0», con HEAD en `a9636f37`. Esa salida quedó en la consola: el cierre final
  sobrescribió el archivo.
- **La foto final**, tras el tercer intento (`salidas/foto_repo_comparacion.txt` y `salidas/status_repo_despues.txt`):

```
antes: 60957 entradas; después: 60960; nuevos: 3; borrados: 0; cambiados: 1
  nuevo: data/experiment/banco_mcp/mcp_kg/familias_nav_cand.py
  nuevo: data/experiment/banco_mcp/mcp_kg/selftest_familias_nav_cand.py
  nuevo: docs/protocolo_N4_UNAV_medicion_N6.md
  cambiado: docs/registro_decisiones_calidad_y_evaluacion_2026-10-15.md
HEAD: 43b4df8fee060e6366c5248f066a2505a54b1114
status de lo versionado (--untracked-files=no): 0 líneas
HEAD de la copia: a9636f37b73dc5c9fafc6a37372b6236e83b37fc; commits desde entonces: 3
  43b4df8fee060e6366c5248f066a2505a54b1114 2026-10-26 22:29:26 -0300 Navegacion del agente: la herramienta nueva de la vista de punto, que l
  f22b5ca8abd139cea23edfea94ddbdb29c6baa05 2026-10-26 22:29:20 -0300 Registro de decisiones: la prueba sobre T que no pasa y su precision co
  f69e95ea9753d0e40e0ec39383df0662194c67dc 2026-10-26 22:29:14 -0300 Navegacion del agente: el protocolo de medicion de las ablaciones, sell
cambios de la foto: 4; rutas de los commits: 4; la foto, explicada por los commits: True
```

- **HEAD se movió durante mi cierre.** Entraron tres commits, entre las 22:29:14 y las 22:29:26, que no hice yo: no commiteo.
  - Las 4 rutas que cambian en la foto son, una por una, las de `git diff --name-only a9636f37 43b4df8f`.
  - Fuera de ellas, el repo está igual.
  - Lo versionado no tiene cambios sin commitear.
  - Ningún commit toca `agentes/`, `paralelo/` ni `b63/`. Los dos archivos de HEAD que importa el lanzador r5 siguen siendo
    `1bcadb44…` y `73c31768…`.
- **Los sellos de la copia** se miden contra `a9636f37`, el commit de la copia (`sellos_copia_r5.py`, argumento `<rev>`). Contra
  `43b4df8f` darían 2 faltantes: los dos archivos nuevos de `mcp_kg/`, que la copia no tiene.
- **Las 18 rutas sin seguimiento.** El `status`, sin las dos carpetas de adjudicación, las trae, y las 18 ya estaban en la foto
  de antes, cada una con al menos una entrada bajo su ruta. No son mías.

## 11. Errores propios, con su causa

1. **D8 falló en el primer intento** (10/11).
   - La causa: supuse que un runner se ve a sí mismo con `pgrep -f`, y el `pgrep` de macOS lo deja fuera (§8.1). La guarda no
     frenó, que era lo correcto. Lo que falló fue la prueba de que el runner era un proceso del patrón.
   - La corrección: el runner se mira con `pgrep -a` y con la tabla de ps; sumé T11 para la exclusión del código.
   - El primer intento está archivado en `salidas/intento1_D8_pgrep_excluye_ancestros/`: su script, con sha256 `9ca98af5…`, sus
     salidas y su resultado. Volví a correr la corrida entera sobre carpetas vacías.
2. **Un `grep -rln guardas_lote` sobre `banco_mcp/` de la copia recorrió también los demás archivos de `b63/`.**
   - Recorrió los `.py`, `.zsh` y `.sh` de `b63/`, también los que el despacho no me deja leer: `corrida_en_seco_b63.py`,
     `enmascarar_cwd_b63.py`, `juez_b63.py`, `lanzar_agente_b63.py`, `selftest_b63.py` y los `.py` de `seco/`.
   - Devolvió los nombres de tres que nombran `guardas_lote`. No mostró ningún renglón.
   - La causa: busqué los usuarios de la guarda en todo el banco sin excluir `b63/`.
3. **Dos `git status` del repo entero no excluyeron por ruta las carpetas de adjudicación.**
   - El primero, el del paso 0 (`--untracked-files=no`), revisa lo versionado de todo el árbol.
   - El segundo, en el primer cierre, también lo que no tiene seguimiento.
   - Los dos imprimieron solo la cuenta. La del segundo (18) es la misma que da después con las dos carpetas excluidas, así que no
     salió de ahí ningún nombre.
   - La causa: repetí el control del paso 0 sin la exclusión que pide el despacho para toda búsqueda que pueda recorrerlas.
   - El `status` del cierre final ya las excluye.
4. **Los sellos de después fallaron en el primer cierre** (rc 1, sin salida).
   - La causa: les pasé la copia por una ruta relativa, y `git -C <repo> hash-object --stdin-paths` la resolvió contra el repo.
   - `hash-object` sin `-w` no escribe. Con la ruta absoluta dieron 2503 de 2503.
5. **Correcciones antes de correr nada:**
   - `fijar_patron_de_prueba` controlaba el token contra el patrón vigente, y no contra el real.
   - `extraccion_corriendo` delegaba en la de BASE, que no veía el patrón de prueba del runner.
   - El selftest traía una ruta sintética en la carpeta de usuarios de macOS, que el grep habría contado. La cambié por
     `/home/u/…`, que también tiene espacios, y volví a correr el selftest.
   - Un `sed` con `#` en el reemplazo falló sin cambiar nada; hice el cambio con un editor.
   - En el cierre final, un heredoc anidado con el mismo delimitador cortó un comando de edición de `sellos_copia_r5.py` y
     `cierre_r5.zsh`. No escribió nada: los dos dieron el mismo sha256 antes y después. Hice el cambio con un editor.
6. **Los docstrings de `lanzar_lote_paralelo_r5.py` y `guardas_lote_r5.py` decían que la decisión fue «recibida a las 19:00:06».**
   - Esa hora es la del despacho, y apunta al origen conversacional de la decisión. La convención documenta la decisión por su
     fecha y su justificación, como lo hace HEAD (`lanzar_lote_paralelo.py:37`: «la decisión de la autora del 26/10/2026»).
   - La causa: copié la hora del despacho al citar la decisión.
   - Lo vi en el autocontrol del cierre, cuando la corrida en seco ya había dado 11/11 (el segundo intento, con los módulos
     `ecc0e769…` y `9a9ee7fc…`). Saqué esa hora, que fue el único cambio en los dos archivos, y volví a correr el selftest y la
     corrida en seco entera sobre carpetas vacías (el tercer intento, el de §6 y §7).
   - El segundo intento está archivado en `salidas/intento2_antes_del_docstring/`.

## 12. Grep de convenciones

`scripts/cierre_r5.zsh grep` corre `segmentacion_oficial_e0r2/s0_4/scripts/grep_convenciones.py` de la copia con
`LC_ALL=en_US.UTF-8`, sobre:

- los archivos nuevos, `bin/`, `scripts/` y `pruebas/`;
- este FRENO;
- las salidas del selftest, de la corrida en seco y de los controles.

```
control positivo: 16 de 16 términos encontrados
archivos revisados: 30
total por término: {} — total 0
```

## 13. El paquete

`revision_UBANCO_R5_a/` está en el scratchpad de la sesión, con su `manifest.txt`. Su copia con `ditto` está en
`$HOME/INGENIERIA IA/TESIS/fuera_del_repo/scratchpads/95486f81-2327-4620-90bc-f61b59d22c1a/scratchpad/revision_UBANCO_R5_a/`.

- **La verificación de los sha256** del manifest (`scripts/armar_paquete_r5.py`, y aparte `shasum -a 256 -c` en la copia
  permanente): 47 de 47 en el scratchpad y 47 de 47 en la copia permanente, 0 distintos.
- **El sha256 del manifest** va en el reporte, porque el manifest incluye este FRENO.

FRENO: espero la revisión de la mesa.
